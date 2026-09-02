"""Exponent audit for the elementary power-high mass ledger.

For Y=X^theta and H=Y^2/X, the central scale
M=max(H,Y/H) forces the determinant cutoff HM to be at least Y and makes
H/M non-growing.  These are exponent identities only; no prime asymptotic is
claimed.
"""

from __future__ import annotations


def audit_theta(theta: float) -> None:
    h_exponent = 2.0 * theta - 1.0
    threshold_exponent = 1.0 - theta
    central_exponent = max(h_exponent, threshold_exponent)
    determinant_exponent = h_exponent + central_exponent
    mass_ratio_exponent = h_exponent - central_exponent

    assert 0.0 < central_exponent < 1.0
    assert determinant_exponent + 1.0e-12 >= theta
    assert mass_ratio_exponent <= 1.0e-12
    print(
        f"theta={theta:.6f}: H=X^{h_exponent:.6f}, "
        f"Y/H=X^{threshold_exponent:.6f}, "
        f"M=X^{central_exponent:.6f}, HM=X^{determinant_exponent:.6f}, "
        f"H/M=X^{mass_ratio_exponent:.6f}"
    )


def main() -> None:
    for theta in (0.51, 0.55, 0.60, 2.0 / 3.0, 0.75, 0.90, 0.99):
        audit_theta(theta)
    print("power-high central-scale and mass-ledger exponents passed")
    print("[scope] exponent identities only; incidence proof is in note 236")


if __name__ == "__main__":
    main()
