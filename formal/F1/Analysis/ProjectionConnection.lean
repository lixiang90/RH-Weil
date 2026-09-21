import Mathlib.Tactic.NoncommRing
import Mathlib.Algebra.Star.Basic

/-! Algebraic part of a projection connection. Analytic existence and domains
of the connection, and its actual arithmetic source, are not asserted here. -/
namespace RHWeil.F1

def projectionConnection {R : Type*} [Ring R] (p dp : R) : R := dp*p-p*dp

section Ring
variable {R : Type*} [Ring R]

theorem projection_derivative_corner (p dp : R)
    (hp : p*p=p) (hd : dp*p+p*dp=dp) : p*dp*p=0 := by
  have h := congrArg (fun x : R => p*x) hd
  simp only [mul_add, ← mul_assoc, hp] at h
  have h' : p*dp*p+p*dp = 0+p*dp := by simpa only [zero_add] using h
  exact add_right_cancel h'

theorem projection_connection_commutator (p dp : R)
    (hp : p*p=p) (hd : dp*p+p*dp=dp) :
    projectionConnection p dp*p-p*projectionConnection p dp=dp := by
  have hz := projection_derivative_corner p dp hp hd
  calc
    projectionConnection p dp*p-p*projectionConnection p dp =
        dp*(p*p)+(p*p)*dp-(p*dp*p+p*dp*p) := by
          unfold projectionConnection
          noncomm_ring
    _ = dp := by rw [hp,hz]; simpa using hd

theorem projection_connection_corner (p dp v : R)
    (hp : p*p=p) (hd : dp*p+p*dp=dp) (hv : p*v=v) (vh : v*p=v) :
    projectionConnection p dp*v-v*projectionConnection p dp=dp*v+v*dp := by
  have hz := projection_derivative_corner p dp hp hd
  have h1 : p*dp*v=0 := by
    calc
      p*dp*v = p*dp*(p*v) := by rw [hv]
      _ = (p*dp*p)*v := by simp only [mul_assoc]
      _ = 0 := by rw [hz,zero_mul]
  have h2 : v*dp*p=0 := by
    calc
      v*dp*p = (v*p)*dp*p := by rw [vh]
      _ = v*(p*dp*p) := by simp only [mul_assoc]
      _ = 0 := by rw [hz,mul_zero]
  calc
    projectionConnection p dp*v-v*projectionConnection p dp =
        dp*(p*v)+(v*p)*dp-(p*dp*v+v*dp*p) := by
          unfold projectionConnection
          noncomm_ring
    _ = dp*v+v*dp := by rw [hv,vh,h1,h2]; simp

theorem corner_derivative_parallel (p dp v dv : R)
    (hp : p*p=p) (hd : dp*p+p*dp=dp) (hv : p*v=v) (vh : v*p=v)
    (hl : dp*v+p*dv=dv) (hr : dv*p+v*dp=dv) (hzero : p*dv*p=0) :
    dv=projectionConnection p dp*v-v*projectionConnection p dp := by
  have h := congrArg (fun x : R => p*x) hr
  simp only [mul_add, ← mul_assoc, hv, hzero, zero_add] at h
  rw [projection_connection_corner p dp v hp hd hv vh]
  rw [← h] at hl
  exact hl.symm

theorem compressed_connection_defect (k q u : R) :
    q*(k*u-u*k)*q-(k*(1-q+q*u*q)-(1-q+q*u*q)*k) =
      -(q*k-k*q)+(q*k-k*q)*u*q+q*u*(q*k-k*q) := by
  noncomm_ring

end Ring

theorem projection_connection_skew {R : Type*} [Ring R] [StarRing R]
    (p dp : R) (hp : star p=p) (hd : star dp=dp) :
    star (projectionConnection p dp) = -projectionConnection p dp := by
  simp only [projectionConnection, star_sub, star_mul, hp, hd]
  noncomm_ring

end RHWeil.F1
