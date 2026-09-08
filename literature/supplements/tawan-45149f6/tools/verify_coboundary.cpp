#include <algorithm>
#include <array>
#include <bit>
#include <gmp.h>
#include <cfenv>
#include <cmath>
#include <cstdint>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <optional>
#include <stdexcept>
#include <string>
#include <vector>

#pragma STDC FENV_ACCESS ON

namespace {

constexpr int kCoarseGrid = 4000;
constexpr int kCoarseCells = 43247;
constexpr int kDerivativeStart = 3500;
constexpr int kTargetNumerator = 577;
constexpr int kTargetDenominator = 100000;
constexpr double kNegativeInfinity = -std::numeric_limits<double>::infinity();
constexpr double kPositiveInfinity = std::numeric_limits<double>::infinity();
static_assert(std::numeric_limits<double>::is_iec559);

inline double DownAdd(double a, double b) {
  return std::nextafter(a + b, kNegativeInfinity);
}
inline double UpAdd(double a, double b) {
  return std::nextafter(a + b, kPositiveInfinity);
}
inline double DownSubtract(double a, double b) {
  return std::nextafter(a - b, kNegativeInfinity);
}
inline double DownMultiply(double a, double b) {
  return std::nextafter(a * b, kNegativeInfinity);
}
inline double UpMultiply(double a, double b) {
  return std::nextafter(a * b, kPositiveInfinity);
}
inline double DownRatio(std::uint64_t a, std::uint64_t b) {
  return std::nextafter(static_cast<double>(a) / static_cast<double>(b),
                        kNegativeInfinity);
}
inline double UpRatio(std::uint64_t a, std::uint64_t b) {
  return std::nextafter(static_cast<double>(a) / static_cast<double>(b),
                        kPositiveInfinity);
}

struct Interval {
  double lower;
  double upper;
};
Interval IntervalAdd(Interval a, Interval b) {
  return {DownAdd(a.lower, b.lower), UpAdd(a.upper, b.upper)};
}
Interval IntervalMultiply(Interval a, Interval b) {
  const std::array<double, 4> lower_products = {
      DownMultiply(a.lower, b.lower), DownMultiply(a.lower, b.upper),
      DownMultiply(a.upper, b.lower), DownMultiply(a.upper, b.upper)};
  const std::array<double, 4> upper_products = {
      UpMultiply(a.lower, b.lower), UpMultiply(a.lower, b.upper),
      UpMultiply(a.upper, b.lower), UpMultiply(a.upper, b.upper)};
  return {*std::min_element(lower_products.begin(), lower_products.end()),
          *std::max_element(upper_products.begin(), upper_products.end())};
}
double AbsoluteUpper(Interval value) {
  return std::max(std::abs(value.lower), std::abs(value.upper));
}

std::uint32_t ReadBigEndian32(std::istream& input) {
  unsigned char bytes[4];
  input.read(reinterpret_cast<char*>(bytes), 4);
  if (!input) throw std::runtime_error("truncated table header");
  return (std::uint32_t(bytes[0]) << 24) |
         (std::uint32_t(bytes[1]) << 16) |
         (std::uint32_t(bytes[2]) << 8) | std::uint32_t(bytes[3]);
}
double ReadBigEndianDouble(std::istream& input) {
  unsigned char bytes[8];
  input.read(reinterpret_cast<char*>(bytes), 8);
  if (!input) throw std::runtime_error("truncated table data");
  std::uint64_t bits = 0;
  for (unsigned char byte : bytes) bits = (bits << 8) | byte;
  double value;
  std::memcpy(&value, &bits, sizeof(value));
  return value;
}

std::vector<double> ReadKernelTable(const std::string& path, int expected_grid,
                                    int expected_cells) {
  std::ifstream input(path, std::ios::binary);
  if (!input) throw std::runtime_error("cannot open table: " + path);
  char magic[4];
  input.read(magic, 4);
  if (!input || std::string(magic, 4) != "CWK2")
    throw std::runtime_error("invalid kernel-table magic");
  const auto grid = ReadBigEndian32(input);
  const auto count = ReadBigEndian32(input);
  if (grid != static_cast<std::uint32_t>(expected_grid) ||
      count != static_cast<std::uint32_t>(expected_cells))
    throw std::runtime_error("unexpected kernel-table dimensions");
  std::vector<double> values(count);
  for (double& value : values) {
    value = ReadBigEndianDouble(input);
    if (!std::isfinite(value) || value < 0.0)
      throw std::runtime_error("invalid kernel-table entry");
  }
  char extra;
  if (input.read(&extra, 1))
    throw std::runtime_error("trailing kernel-table bytes");
  return values;
}

class RangeMinimum {
 public:
  RangeMinimum(std::vector<double> values, double outside)
      : length_(static_cast<int>(values.size())), outside_(outside) {
    if (values.empty()) throw std::runtime_error("empty range table");
    levels_.push_back(std::move(values));
    for (int width = 1; 2 * width <= length_; width *= 2) {
      const auto& previous = levels_.back();
      std::vector<double> current(length_ - 2 * width + 1);
      for (int index = 0; index + 2 * width <= length_; ++index)
        current[index] = std::min(previous[index], previous[index + width]);
      levels_.push_back(std::move(current));
    }
  }
  double Query(int left, int right) const {
    if (left < 0 || right < left) throw std::runtime_error("invalid RMQ");
    if (right >= length_) return outside_;
    const int count = right - left + 1;
    const int level = std::bit_width(static_cast<unsigned>(count)) - 1;
    const int width = 1 << level;
    return std::min(levels_[level][left],
                    levels_[level][right - width + 1]);
  }
 private:
  int length_;
  double outside_;
  std::vector<std::vector<double>> levels_;
};

struct DerivativeRaw {
  std::vector<double> second_lower;
  std::vector<double> value_lower;
  std::vector<double> value_upper;
  std::vector<double> first_lower;
  std::vector<double> first_upper;
};
DerivativeRaw ReadDerivativeTable(const std::string& path) {
  std::ifstream input(path, std::ios::binary);
  if (!input) throw std::runtime_error("cannot open derivative table: " + path);
  char magic[4];
  input.read(magic, 4);
  if (!input || std::string(magic, 4) != "CWD2")
    throw std::runtime_error("invalid derivative-table magic");
  const auto grid = ReadBigEndian32(input);
  const auto cells = ReadBigEndian32(input);
  const auto start = ReadBigEndian32(input);
  if (grid != kCoarseGrid || cells != kCoarseCells ||
      start != kDerivativeStart)
    throw std::runtime_error("unexpected derivative-table dimensions");
  DerivativeRaw result;
  result.second_lower.resize(cells);
  for (int i = 0; i < static_cast<int>(cells); ++i) {
    result.second_lower[i] = ReadBigEndianDouble(input);
    if (i >= static_cast<int>(start) &&
        !std::isfinite(result.second_lower[i]))
      throw std::runtime_error("invalid second-derivative entry");
  }
  const int points = 2 * static_cast<int>(cells) + 1;
  auto read_points = [&](std::vector<double>& values) {
    values.resize(points);
    for (double& value : values) value = ReadBigEndianDouble(input);
  };
  read_points(result.value_lower);
  read_points(result.value_upper);
  read_points(result.first_lower);
  read_points(result.first_upper);
  for (int i = 2 * static_cast<int>(start); i < points; ++i) {
    if (!std::isfinite(result.value_lower[i]) ||
        !std::isfinite(result.value_upper[i]) ||
        !std::isfinite(result.first_lower[i]) ||
        !std::isfinite(result.first_upper[i]) ||
        result.value_lower[i] > result.value_upper[i] ||
        result.first_lower[i] > result.first_upper[i])
      throw std::runtime_error("invalid point-derivative entry");
  }
  char extra;
  if (input.read(&extra, 1))
    throw std::runtime_error("trailing derivative-table bytes");
  return result;
}

struct DerivativeData {
  RangeMinimum second_minimum;
  std::vector<double> value_lower;
  std::vector<double> value_upper;
  std::vector<double> first_lower;
  std::vector<double> first_upper;
  explicit DerivativeData(DerivativeRaw raw)
      : second_minimum(std::move(raw.second_lower), kNegativeInfinity),
        value_lower(std::move(raw.value_lower)),
        value_upper(std::move(raw.value_upper)),
        first_lower(std::move(raw.first_lower)),
        first_upper(std::move(raw.first_upper)) {}
  bool PointAvailable(int half_grid_index) const {
    return half_grid_index >= 2 * kDerivativeStart &&
           half_grid_index < static_cast<int>(value_lower.size());
  }
  Interval Value(int half_grid_index) const {
    return {value_lower[half_grid_index], value_upper[half_grid_index]};
  }
  Interval First(int half_grid_index) const {
    return {first_lower[half_grid_index], first_upper[half_grid_index]};
  }
};

struct CellRange { int left; int right; };
struct Box { std::array<CellRange, 6> coordinates; int depth = 0; };
struct Statistics {
  std::uint64_t nodes = 0;
  std::uint64_t splits = 0;
  std::uint64_t pressure_pruned = 0;
  std::uint64_t interval_pruned = 0;
  std::uint64_t tangent_pruned = 0;
  int maximum_depth = 0;
};
struct Rational { std::uint64_t numerator; std::uint64_t denominator; };
struct CoefficientInterval { double lower; double upper; };

constexpr std::array<std::uint64_t, 6> kPressureNumerators =
    {946, 1177, 877, 877, 1177, 946};
constexpr std::uint64_t kPressureDenominator = 1920000;
constexpr std::array<Rational, 6> kNearestRationals = {
    Rational{31343, 100000}, Rational{1, 3},
    Rational{105971, 300000}, Rational{105971, 300000},
    Rational{1, 3}, Rational{31343, 100000}};
constexpr std::array<Rational, 7> kSpanRationals = {
    Rational{0, 1}, Rational{0, 1}, Rational{2, 5}, Rational{1, 2},
    Rational{2, 3}, Rational{1, 1}, Rational{2, 1}};

struct Coefficients {
  std::array<CoefficientInterval, 6> nearest{};
  std::array<CoefficientInterval, 7> span{};
  Coefficients() {
    for (int j = 0; j < 6; ++j)
      nearest[j] = {DownRatio(kNearestRationals[j].numerator,
                              kNearestRationals[j].denominator),
                    UpRatio(kNearestRationals[j].numerator,
                            kNearestRationals[j].denominator)};
    for (int r = 2; r <= 6; ++r)
      span[r] = {DownRatio(kSpanRationals[r].numerator,
                           kSpanRationals[r].denominator),
                 UpRatio(kSpanRationals[r].numerator,
                         kSpanRationals[r].denominator)};
  }
};

Interval ScaleInterval(Interval value, CoefficientInterval coefficient) {
  return IntervalMultiply(value, {coefficient.lower, coefficient.upper});
}
double LowerScaledSecond(double second_lower,
                         CoefficientInterval coefficient) {
  if (!std::isfinite(second_lower)) return kNegativeInfinity;
  const double chosen = second_lower >= 0.0 ? coefficient.lower
                                            : coefficient.upper;
  return DownMultiply(chosen, second_lower);
}

double BoxLower(const Box& box, int grid, const RangeMinimum& ranges,
                const Coefficients& coefficients) {
  std::array<int, 7> low_prefix{};
  std::array<int, 7> high_prefix{};
  for (int j = 0; j < 6; ++j) {
    low_prefix[j + 1] = low_prefix[j] + box.coordinates[j].left;
    high_prefix[j + 1] = high_prefix[j] + box.coordinates[j].right;
  }
  double lower = 0.0;
  for (int j = 0; j < 6; ++j)
    lower = DownAdd(lower,
      DownRatio(std::uint64_t(box.coordinates[j].left) *
                    kPressureNumerators[j],
                std::uint64_t(grid) * kPressureDenominator));
  for (int j = 0; j < 6; ++j)
    lower = DownAdd(lower,
      DownMultiply(coefficients.nearest[j].lower,
                   ranges.Query(box.coordinates[j].left,
                                box.coordinates[j].right)));
  for (int span = 2; span <= 6; ++span)
    for (int start = 0; start < 7 - span; ++start) {
      const int left = low_prefix[start + span] - low_prefix[start];
      const int right = high_prefix[start + span] - high_prefix[start]
                        + span - 1;
      lower = DownAdd(lower,
        DownMultiply(coefficients.span[span].lower,
                     ranges.Query(left, right)));
    }
  return lower;
}

bool PressureAlonePrunes(const Box& box, int grid, double target_upper) {
  double lower = 0.0;
  for (int j = 0; j < 6; ++j)
    lower = DownAdd(lower,
      DownRatio(std::uint64_t(box.coordinates[j].left) *
                    kPressureNumerators[j],
                std::uint64_t(grid) * kPressureDenominator));
  return lower >= target_upper;
}
int WidestCoordinate(const Box& box) {
  int selected = 0, widest = -1;
  for (int j = 0; j < 6; ++j) {
    const int width = box.coordinates[j].right - box.coordinates[j].left;
    if (width > widest) { widest = width; selected = j; }
  }
  return selected;
}

class ExactRational {
 public:
  ExactRational() { mpq_init(value_); }
  ExactRational(const ExactRational& other) {
    mpq_init(value_);
    mpq_set(value_, other.value_);
  }
  ExactRational& operator=(const ExactRational& other) {
    if (this != &other) mpq_set(value_, other.value_);
    return *this;
  }
  ~ExactRational() { mpq_clear(value_); }
  mpq_t& get() { return value_; }
  const mpq_t& get() const { return value_; }
  int sign() const { return mpq_sgn(value_); }
  ExactRational& operator+=(const ExactRational& other) {
    mpq_add(value_, value_, other.value_);
    return *this;
  }
  ExactRational& operator-=(const ExactRational& other) {
    mpq_sub(value_, value_, other.value_);
    return *this;
  }
  ExactRational& operator*=(const ExactRational& other) {
    mpq_mul(value_, value_, other.value_);
    return *this;
  }
  ExactRational& operator/=(const ExactRational& other) {
    if (other.sign() == 0) throw std::runtime_error("exact division by zero");
    mpq_div(value_, value_, other.value_);
    return *this;
  }
 private:
  mpq_t value_;
};

ExactRational operator*(ExactRational left, const ExactRational& right) {
  left *= right;
  return left;
}
ExactRational operator/(ExactRational left, const ExactRational& right) {
  left /= right;
  return left;
}

ExactRational ExactDouble(double value) {
  if (!std::isfinite(value)) throw std::runtime_error("nonfinite exact double");
  ExactRational result;
  if (value == 0.0) return result;
  const std::uint64_t bits = std::bit_cast<std::uint64_t>(value);
  const bool negative = (bits >> 63) != 0;
  const int exponent_bits = int((bits >> 52) & 0x7ffU);
  const std::uint64_t fraction = bits & ((std::uint64_t(1) << 52) - 1);
  mpz_t numerator, denominator;
  mpz_init(numerator);
  mpz_init_set_ui(denominator, 1);
  int exponent;
  if (exponent_bits == 0) {
    mpz_set_ui(numerator, fraction);
    exponent = -1074;
  } else {
    mpz_set_ui(numerator, fraction);
    mpz_setbit(numerator, 52);
    exponent = exponent_bits - 1023 - 52;
  }
  if (exponent >= 0) mpz_mul_2exp(numerator, numerator, exponent);
  else mpz_mul_2exp(denominator, denominator, -exponent);
  mpq_set_num(result.get(), numerator);
  mpq_set_den(result.get(), denominator);
  mpq_canonicalize(result.get());
  if (negative) mpq_neg(result.get(), result.get());
  mpz_clear(numerator);
  mpz_clear(denominator);
  return result;
}

struct HessianTerm { int start; int span; double scalar; };

bool FloatPositiveDefinite(const std::vector<HessianTerm>& terms) {
  double matrix[6][6]{};
  for (const auto& term : terms)
    for (int i = term.start; i < term.start + term.span; ++i)
      for (int j = term.start; j < term.start + term.span; ++j)
        matrix[i][j] += term.scalar;
  double lower[6][6]{};
  double diagonal[6]{};
  for (int column = 0; column < 6; ++column) {
    double pivot = matrix[column][column];
    for (int previous = 0; previous < column; ++previous)
      pivot -= lower[column][previous] * lower[column][previous] *
               diagonal[previous];
    if (!(pivot > 1e-11)) return false;
    diagonal[column] = pivot;
    lower[column][column] = 1.0;
    for (int row = column + 1; row < 6; ++row) {
      double value = matrix[row][column];
      for (int previous = 0; previous < column; ++previous)
        value -= lower[row][previous] * lower[column][previous] *
                 diagonal[previous];
      lower[row][column] = value / pivot;
    }
  }
  return true;
}

bool ExactPositiveDefinite(const std::vector<HessianTerm>& terms) {
  ExactRational matrix[6][6];
  for (const auto& term : terms) {
    const ExactRational scalar = ExactDouble(term.scalar);
    for (int i = term.start; i < term.start + term.span; ++i)
      for (int j = term.start; j < term.start + term.span; ++j)
        matrix[i][j] += scalar;
  }
  ExactRational lower[6][6];
  ExactRational diagonal[6];
  for (int column = 0; column < 6; ++column) {
    lower[column][column] = ExactDouble(1.0);
    ExactRational pivot = matrix[column][column];
    for (int previous = 0; previous < column; ++previous)
      pivot -= lower[column][previous] * lower[column][previous] *
               diagonal[previous];
    if (pivot.sign() <= 0) return false;
    diagonal[column] = pivot;
    for (int row = column + 1; row < 6; ++row) {
      ExactRational value = matrix[row][column];
      for (int previous = 0; previous < column; ++previous)
        value -= lower[row][previous] * lower[column][previous] *
                 diagonal[previous];
      lower[row][column] = value / pivot;
    }
  }
  return true;
}

std::optional<double> ConvexTangentLower(
    const Box& box, const DerivativeData& derivative,
    const Coefficients& coefficients) {
  std::array<int, 7> low_prefix{};
  std::array<int, 7> high_prefix{};
  for (int j = 0; j < 6; ++j) {
    low_prefix[j + 1] = low_prefix[j] + box.coordinates[j].left;
    high_prefix[j + 1] = high_prefix[j] + box.coordinates[j].right;
  }

  std::vector<HessianTerm> hessian_terms;
  hessian_terms.reserve(21);
  for (int j = 0; j < 6; ++j) {
    const double second = derivative.second_minimum.Query(
        box.coordinates[j].left, box.coordinates[j].right);
    const double scalar = LowerScaledSecond(second, coefficients.nearest[j]);
    if (!std::isfinite(scalar)) return std::nullopt;
    hessian_terms.push_back({j, 1, scalar});
  }
  for (int span = 2; span <= 6; ++span)
    for (int start = 0; start < 7 - span; ++start) {
      const int left = low_prefix[start + span] - low_prefix[start];
      const int right = high_prefix[start + span] - high_prefix[start]
                        + span - 1;
      const double second = derivative.second_minimum.Query(left, right);
      const double scalar = LowerScaledSecond(second, coefficients.span[span]);
      if (!std::isfinite(scalar)) return std::nullopt;
      hessian_terms.push_back({start, span, scalar});
    }
  if (!FloatPositiveDefinite(hessian_terms) ||
      !ExactPositiveDefinite(hessian_terms))
    return std::nullopt;

  Interval value{0.0, 0.0};
  std::array<Interval, 6> gradient{};
  for (int j = 0; j < 6; ++j) {
    const std::uint64_t midpoint_numerator =
        std::uint64_t(box.coordinates[j].left +
                      box.coordinates[j].right + 1) *
        kPressureNumerators[j];
    const std::uint64_t midpoint_denominator =
        std::uint64_t(2 * kCoarseGrid) * kPressureDenominator;
    const Interval pressure{
        DownRatio(midpoint_numerator, midpoint_denominator),
        UpRatio(midpoint_numerator, midpoint_denominator)};
    value = IntervalAdd(value, pressure);
    gradient[j] = IntervalAdd(
        gradient[j],
        {DownRatio(kPressureNumerators[j], kPressureDenominator),
         UpRatio(kPressureNumerators[j], kPressureDenominator)});
  }

  auto add_kernel_term = [&](int start, int span,
                             CoefficientInterval coefficient) -> bool {
    const int point_index =
        (low_prefix[start + span] - low_prefix[start]) +
        (high_prefix[start + span] - high_prefix[start]) + span;
    if (!derivative.PointAvailable(point_index)) return false;
    value = IntervalAdd(
        value, ScaleInterval(derivative.Value(point_index), coefficient));
    const Interval first =
        ScaleInterval(derivative.First(point_index), coefficient);
    for (int j = start; j < start + span; ++j)
      gradient[j] = IntervalAdd(gradient[j], first);
    return true;
  };
  for (int j = 0; j < 6; ++j)
    if (!add_kernel_term(j, 1, coefficients.nearest[j]))
      return std::nullopt;
  for (int span = 2; span <= 6; ++span)
    for (int start = 0; start < 7 - span; ++start)
      if (!add_kernel_term(start, span, coefficients.span[span]))
        return std::nullopt;

  double lower = value.lower;
  for (int j = 0; j < 6; ++j) {
    const double radius = UpRatio(
        std::uint64_t(box.coordinates[j].right -
                      box.coordinates[j].left + 1),
        std::uint64_t(2 * kCoarseGrid));
    lower = DownSubtract(
        lower, UpMultiply(AbsoluteUpper(gradient[j]), radius));
  }
  return lower;
}

}  // namespace

int main(int argc, char** argv) {
  try {
    if (argc < 3 || argc > 4) {
      std::cerr << "usage: verify_coboundary COARSE_TABLE DERIVATIVE_TABLE "
                   "[BOX_CODE]\n";
      return 2;
    }
    if (std::fesetround(FE_TONEAREST) != 0 ||
        std::fegetround() != FE_TONEAREST)
      throw std::runtime_error("cannot select round-to-nearest mode");
    const RangeMinimum coarse_ranges(
        ReadKernelTable(argv[1], kCoarseGrid, kCoarseCells), 0.0);
    const DerivativeData derivative(ReadDerivativeTable(argv[2]));
    const Coefficients coefficients;
    const double target_upper =
        UpRatio(kTargetNumerator, kTargetDenominator);

    constexpr int kScanCells = 60000;
    std::array<std::vector<CellRange>, 6> components;
    for (int coordinate = 0; coordinate < 6; ++coordinate) {
      const double terminal_pressure = DownRatio(
          std::uint64_t(kScanCells - 1) * kPressureNumerators[coordinate],
          std::uint64_t(kCoarseGrid) * kPressureDenominator);
      if (terminal_pressure < target_upper)
        throw std::runtime_error("unsafe scan cutoff");
      for (int index = 0; index < kScanCells; ++index) {
        double one_body = DownRatio(
            std::uint64_t(index) * kPressureNumerators[coordinate],
            std::uint64_t(kCoarseGrid) * kPressureDenominator);
        one_body = DownAdd(
            one_body,
            DownMultiply(coefficients.nearest[coordinate].lower,
                         coarse_ranges.Query(index, index)));
        if (one_body < target_upper) {
          if (components[coordinate].empty() ||
              index > components[coordinate].back().right + 1)
            components[coordinate].push_back({index, index});
          else
            components[coordinate].back().right = index;
        }
      }
      std::cerr << "coordinate=" << coordinate
                << " components=" << components[coordinate].size();
      for (const auto component : components[coordinate])
        std::cerr << " [" << component.left << ',' << component.right << ']';
      std::cerr << '\n';
    }
    std::uint64_t total = 1;
    for (const auto& choices : components) total *= choices.size();
    std::uint64_t begin = 0, end = total;
    if (argc == 4) {
      begin = std::stoull(argv[3]); end = begin + 1;
      if (begin >= total) throw std::runtime_error("invalid box code");
    }
    std::vector<Box> stack;
    for (std::uint64_t code = begin; code < end; ++code) {
      std::uint64_t quotient = code; Box box{};
      for (int coordinate = 0; coordinate < 6; ++coordinate) {
        const auto& choices = components[coordinate];
        box.coordinates[coordinate] = choices[quotient % choices.size()];
        quotient /= choices.size();
      }
      stack.push_back(box);
    }
    Statistics coarse;
    while (!stack.empty()) {
      const Box box = stack.back(); stack.pop_back();
      ++coarse.nodes;
      coarse.maximum_depth = std::max(coarse.maximum_depth, box.depth);
      if (PressureAlonePrunes(box, kCoarseGrid, target_upper)) {
        ++coarse.pressure_pruned; continue;
      }
      const double lower = BoxLower(box, kCoarseGrid, coarse_ranges,
                                    coefficients);
      if (lower >= target_upper) {
        ++coarse.interval_pruned; continue;
      }
      const auto tangent = ConvexTangentLower(box, derivative, coefficients);
      if (tangent && *tangent >= target_upper) {
        ++coarse.tangent_pruned; continue;
      }
      const int coordinate = WidestCoordinate(box);
      const int width = box.coordinates[coordinate].right -
                        box.coordinates[coordinate].left;
      if (width == 0) {
        std::cerr << std::setprecision(17)
                  << "verified=false level=terminal lower=" << lower
                  << " box_code=" << begin << " cells=";
        for (const auto cell : box.coordinates)
          std::cerr << '[' << cell.left << ',' << cell.right << ']';
        std::cerr << '\n';
        return 1;
      }
      const int midpoint = (box.coordinates[coordinate].left +
                            box.coordinates[coordinate].right) / 2;
      Box a = box, b = box;
      a.depth = b.depth = box.depth + 1;
      a.coordinates[coordinate].right = midpoint;
      b.coordinates[coordinate].left = midpoint + 1;
      stack.push_back(a); stack.push_back(b);
      ++coarse.splits;
    }
    std::cout << "verified=true begin=" << begin << " end=" << end
              << " total=" << total
              << " coarse_nodes=" << coarse.nodes
              << " coarse_splits=" << coarse.splits
              << " coarse_pressure=" << coarse.pressure_pruned
              << " coarse_interval=" << coarse.interval_pruned
              << " coarse_tangent=" << coarse.tangent_pruned
              << " coarse_depth=" << coarse.maximum_depth << '\n';
  } catch (const std::exception& error) {
    std::cerr << "error: " << error.what() << '\n';
    return 2;
  }
}
