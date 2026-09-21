import Mathlib.Tactic.NoncommRing

/-! Algebraic bookkeeping for a cocycle-perturbed evolution.
No continuity, unbounded-operator domain, Dyson convergence, or trace statement. -/
namespace RHWeil.F1

theorem right_twisted_cocycle_group_law
    {S R : Type*} [Add S] [Monoid R]
    (u w : S → R) (a : S → R → R) (s t : S)
    (hu : u (s+t) = u s*u t)
    (hw : w (s+t) = a t (w s)*w t)
    (hm : w s*u t = u t*a t (w s)) :
    (u s*w s)*(u t*w t) = u (s+t)*w (s+t) := by
  calc
    (u s*w s)*(u t*w t) = u s*(w s*u t)*w t := by simp only [mul_assoc]
    _ = u s*(u t*a t (w s))*w t := by rw [hm]
    _ = (u s*u t)*(a t (w s)*w t) := by simp only [mul_assoc]
    _ = u (s+t)*w (s+t) := by rw [← hu, ← hw]

theorem left_cocycle_group_law
    {S R : Type*} [Add S] [Monoid R]
    (u v : S → R) (a : S → R → R) (s t : S)
    (hu : u (s+t) = u s*u t)
    (hv : v (s+t) = v s*a s (v t))
    (hm : u s*v t = a s (v t)*u s) :
    (v s*u s)*(v t*u t) = v (s+t)*u (s+t) := by
  calc
    (v s*u s)*(v t*u t) = v s*(u s*v t)*u t := by simp only [mul_assoc]
    _ = v s*(a s (v t)*u s)*u t := by rw [hm]
    _ = (v s*a s (v t))*(u s*u t) := by simp only [mul_assoc]
    _ = v (s+t)*u (s+t) := by rw [← hv, ← hu]

theorem compressed_parallel_defect
    {R : Type*} [Ring R] (k q a : R) :
    q*(k*a-a*k)*q -
        (k*(1+q*a*q)-(1+q*a*q)*k) =
      -(k*q-q*k)*a*q-q*a*(k*q-q*k) := by
  noncomm_ring

theorem parallel_factor_derivative
    {R : Type*} [Ring R] (k f df v dv : R)
    (hf : k*f=f*k) (hv : dv=k*v-v*k) :
    df*v+f*dv-(k*(f*v)-(f*v)*k) = df*v := by
  rw [hv]
  have hm : k*(f*v) = f*(k*v) := by
    rw [← mul_assoc, hf, mul_assoc]
  rw [hm]
  noncomm_ring

end RHWeil.F1
