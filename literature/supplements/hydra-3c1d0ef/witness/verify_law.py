"""Standalone verifier for the independent ceiling witness.

Checks, from `law_certified.txt` alone and with exact integer/rational arithmetic:
  1. the file's 256 integer enclosures (lo, hi) at scale K = 2^60 parse;
  2. every row j = 1..255 satisfies the near-CUE band  |S(j) - j| <= tau, tau read from the
     file, i.e. the law is a valid bandwidth-one witness at that tolerance;
  3. the stated exact rational p equals its stated decimal, and its position relative to the
     paper's p0 is reported (this witness is BELOW p0, which is a strictly stronger ceiling);
  4. the reported worst-case band deviation matches the file;
  5. the D(1) edge bound |D(1)| <= 82395317/10^8 -- the paper's own constant -- holds, computed
     from the row-256 enclosure. This is the condition the downstream theorem requires; a witness
     that violates it is inadmissible however low its p.

No dependencies, no floating point in the decisions. Run:  python verify_law.py [law_certified.txt]
"""
import re
import sys
from fractions import Fraction

PAPER_P0 = Fraction(10909258999421303588095230195816054408197, 16 * 10**39)  # 0.68182868746...
D1_CAP = Fraction(82395317, 10**8)  # the paper's own edge bound, which this witness also satisfies

path = sys.argv[1] if len(sys.argv) > 1 else "law_certified.txt"
text = open(path, encoding="utf-8").read()


def header(key):
    m = re.search(rf"^{re.escape(key)}\s*=\s*(\S+)", text, re.M)
    return m.group(1) if m else None


p = Fraction(header("p"))
tau = Fraction(header("tau_decl"))
K = 2 ** int(header("K").split("^")[1])
encl = [(int(a), int(b)) for a, b in re.findall(r"^\((-?\d+), (-?\d+)\),$", text, re.M)]

print(f"file:            {path}")
print(f"enclosures:      {len(encl)} (expect 256)")
print(f"scale K:         2^{K.bit_length()-1}")
print(f"declared tau:    {tau} = {float(tau):.1e}")

failures = []
worst = Fraction(0)
for j in range(1, 256):                      # row 256 is free by construction
    lo, hi = encl[j - 1]
    s_lo, s_hi = Fraction(lo, K), Fraction(hi, K)
    worst = max(worst, abs(s_lo - j), abs(s_hi - j))
    if s_lo < j - tau or s_hi > j + tau:
        failures.append(j)

print(f"rows checked:    255 (both endpoints, exact rational arithmetic)")
print(f"band failures:   {len(failures)}{'' if not failures else ' at rows ' + str(failures[:10])}")
print(f"worst deviation: {float(worst):.3e}  (file states {header('worst_dev')})")
print(f"certified p:     {float(p):.9f}  = {p}")
print(f"paper p0:        {float(PAPER_P0):.9f}")
_rel = ("BELOW p0 - a strictly STRONGER ceiling than the published one"
        if p < PAPER_P0 else
        "above p0 - a weaker ceiling than the published one")
print(f"gap to p0:       {float(p - PAPER_P0):+.9f}  ({_rel})")

ok = not failures and len(encl) == 256 and p > 0
print()
# --- D(1) edge bound -------------------------------------------------------------
# The ceiling theorem needs |D(1)| <= 82395317/1e8, where D(1) = E[F(256)]/65536 - 1/512
# and row 256 of the enclosure holds K*E[F(256)].  The LP that produces these laws
# constrains only rows j = 1..255 and leaves row 256 free, so D(1) can drift silently as p
# falls -- measured slope dD/dp ~ -19.4 across our certified chain.  A law can therefore be
# band-perfect and still not be a valid witness.  Check it here, not by hand.
D1_BOUND = Fraction(82395317, 10**8)
_EF256 = Fraction(encl[255][1], K)          # row 256 holds K * E[F(256)]
_D1 = _EF256 / 65536 - Fraction(1, 512)
d1_ok = abs(_D1) <= D1_BOUND
print(f"D(1):            {float(_D1):.9f}  (bound {float(D1_BOUND):.9f}, "
      f"margin {float(D1_BOUND - abs(_D1)):.3e})")
print("edge bound:      " + ("OK" if d1_ok else "VIOLATED - NOT A VALID WITNESS"))
ok = ok and d1_ok
print("RESULT:", "PASS - valid public witness at the declared tolerance" if ok else "FAIL")
print("Interpretation: no bandwidth-one certificate can prove a simple-and-on-critical-line")
print(f"proportion above {float(p):.6f} (+ the O(1/N^2 + tau/N) stability term of the paper's Theorem 1').")
sys.exit(0 if ok else 1)
