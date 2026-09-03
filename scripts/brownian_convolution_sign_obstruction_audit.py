"""Exact finite audit for the common-convolution sign obstruction.

The primitive pair U=-1_[0,1), V=1_[0,3) has pointwise nonpositive
product. A common signed atomic multiplier nevertheless reverses its
integrated correlation. All arithmetic below is integer-exact.
"""

from __future__ import annotations


def main() -> None:
    multiplier = (2, -3, -1, 4, -2, -4, 4, 2, -4, 1, 3, -2)

    norm_square = sum(value * value for value in multiplier)
    lag_one = sum(
        multiplier[index] * multiplier[index - 1]
        for index in range(1, len(multiplier))
    )
    lag_two = sum(
        multiplier[index] * multiplier[index - 2]
        for index in range(2, len(multiplier))
    )
    toeplitz_form = norm_square + lag_one + lag_two

    # If A=U*R and B=V*R, then on [j,j+1),
    # A=-r_j and B=r_j+r_(j-1)+r_(j-2). Thus <A,B>=-toeplitz_form.
    convolved_correlation = -toeplitz_form
    base_correlation = -1

    assert sum(multiplier) == 0
    assert norm_square == 100
    assert lag_one == -30
    assert lag_two == -72
    assert toeplitz_form == -2
    assert base_correlation == -1
    assert convolved_correlation == 2

    print(f"multiplier mass={sum(multiplier)}")
    print(
        "Toeplitz ledger: "
        f"norm={norm_square}, lag1={lag_one}, lag2={lag_two}, "
        f"form={toeplitz_form}"
    )
    print(
        f"base correlation={base_correlation}, "
        f"common-convolution correlation={convolved_correlation}"
    )
    print("Brownian common-convolution sign obstruction passed")
    print("[scope] exact finite no-go; no RH asymptotic")


if __name__ == "__main__":
    main()
