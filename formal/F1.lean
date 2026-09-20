import F1.Arithmetic.FiniteSupport
import F1.Arithmetic.Sheaf
import F1.Geometry.RationalCorrespondence
import F1.Geometry.ReducedSquare
import F1.Analysis.Jensen
import F1.Analysis.LocalTrace
import F1.Analysis.EndpointDefect
import F1.Analysis.BoundaryClutch
import F1.Analysis.BoundaryResolvent
import F1.Analysis.OrbitDecay
import F1.Analysis.WeightedArrows
import F1.Analysis.UnitDescent
import F1.Analysis.TraceRadical
import F1.Geometry.Existence
import F1.Geometry.GeometricRealization

/-! Entry point of the F₁ arithmetic geometry blueprint. -/

namespace RHWeil.F1

/-- The target is mathlib's actual Riemann hypothesis, not an abstract proxy. -/
abbrev Target : Prop := RiemannHypothesis

end RHWeil.F1

import F1.Analysis.TransverseTrace
import F1.Analysis.BoundaryGluing
