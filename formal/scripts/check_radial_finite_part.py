"""Radial finite-part bookkeeping; analytic infinite sums are separate."""
from check_local_trace import main

if __name__ == "__main__":
    main(
        theorem_names=["radialTranslate_zero","radialTranslate_add","radialTranslate_inverse","radialRectangle_subtraction","radialComm_reverseShift","radialQuadrant_sourceAnomaly"],
        source_files=["F1/Analysis/RadialFinitePart.lean","checks/RadialFinitePartAudit.lean"],
        report_prefix="radial-finite-part",
        scope="Six algebraic results for finite-part translation, corner terms, rectangle subtraction, inverse and actual-source quadrant coefficient. No infinite sums, trace ideals, cyclic cohomology or full F1 build.",
    )
