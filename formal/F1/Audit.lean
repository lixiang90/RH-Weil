import F1

/-! Run separately with `lake env lean F1/Audit.lean`.
The printed lists expose transitive sorryAx dependencies, not merely source sorrys.
-/

#print axioms RHWeil.F1.prime_scaling_surjective
#print axioms RHWeil.F1.restrict_restrict
#print axioms RHWeil.F1.two_three_six
#print axioms RHWeil.F1.graphParam_injective
#print axioms RHWeil.F1.graphParam_surjective
#print axioms RHWeil.F1.graphEquiv
#print axioms RHWeil.F1.jensen_const_two
#print axioms RHWeil.F1.jensen_not_max_additive
#print axioms RHWeil.F1.exponentPresheaf_isSheaf
#print axioms RHWeil.F1.exponent_stalk_at_prime
#print axioms RHWeil.F1.mem_primeLocalization_iff
#print axioms RHWeil.F1.newtonEquivalent_iff_hull
#print axioms RHWeil.F1.finiteLift_circleIntegrable
#print axioms RHWeil.F1.jensen_finite_lift
#print axioms RHWeil.F1.finiteProfile_weakSecond
#print axioms RHWeil.F1.jensen_one_add_and_sub
#print axioms RHWeil.F1.weil_convergence
#print axioms RHWeil.F1.weilCriterion
#print axioms RHWeil.F1.nonpositive_of_existence
#print axioms RHWeil.F1.rh_of_existence
#print axioms RHWeil.F1.intersection_eq_of_equivalent
#print axioms RHWeil.F1.nonzero_of_positive_representative
#print axioms RHWeil.F1.sectionExistence_of_effectiveRepresentative
#print axioms RHWeil.F1.effectiveRepresentative_of_geometricRR
#print axioms RHWeil.F1.sectionExistence_of_geometricRR
#print axioms RHWeil.F1.nonpositive_of_geometricRR
#check RHWeil.F1.BareExistenceProblem
#check RHWeil.F1.SourceRelativeExistence
#print RiemannHypothesis
