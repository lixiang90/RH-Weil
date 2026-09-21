import F1.Analysis.DefectProjection

/-! Reusable Schur eliminations over an arbitrary noncommutative ring.
These check multiplication order and signs only. They do not formalize
Fredholm index bundles, Hilbert-bundle continuity, or rectangular blocks
between different Hilbert spaces. -/
namespace RHWeil.F1
section Ring
variable {R : Type*} [Ring R]

theorem schur_upper_inverse (a : R) :
    block2 1 a 0 1 * block2 1 (-a) 0 1 = 1 ∧
    block2 1 (-a) 0 1 * block2 1 a 0 1 = 1 := by
  constructor <;> simp [block2_mul, block2_one]

theorem schur_lower_inverse (b : R) :
    block2 1 0 b 1 * block2 1 0 (-b) 1 = 1 ∧
    block2 1 0 (-b) 1 * block2 1 0 b 1 = 1 := by
  constructor <;> simp [block2_mul, block2_one]

theorem schur_lower_elimination (a b : R) :
    block2 1 0 (-b) 1 * block2 1 a b 1 * block2 1 (-a) 0 1 =
      block2 1 0 0 (1-b*a) := by
  simp only [block2_mul]
  ext i j
  fin_cases i <;> fin_cases j <;> simp [block2] <;> noncomm_ring

theorem schur_upper_elimination (a b : R) :
    block2 1 (-a) 0 1 * block2 1 a b 1 * block2 1 0 (-b) 1 =
      block2 (1-a*b) 0 0 1 := by
  simp only [block2_mul]
  ext i j
  fin_cases i <;> fin_cases j <;> simp [block2] <;> noncomm_ring

end Ring
end RHWeil.F1
