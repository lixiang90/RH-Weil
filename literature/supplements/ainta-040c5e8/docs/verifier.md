# Verifier design

The verifier is deliberately smaller than a general interval package. Arb
handles every transcendental enclosure; the search phase only combines
nonnegative lower bounds.

## Kernel cells

For an integer grid size $G$, cell $i$ is the closed interval

$$
[i/G,(i+1)/G].
$$

`python-flint`/Arb evaluates the entire formula

$$
K(x)=\frac12\left[
\mathrm{sinc}(\pi x-1/\sqrt2)+
\mathrm{sinc}(\pi x+1/\sqrt2)
\right]
$$

on each cell at 128-bit precision. From the Arb absolute lower endpoint, the
code obtains a lower bound for $w=k^2$. Conversion to binary64 is widened
downward with `math.nextafter`.

The search then uses only:

- downward-rounded addition and multiplication of nonnegative bounds;
- an O(1) sparse-table range minimum;
- exhaustive bisection of integer cell ranges;
- an upward-rounded exact rational target.

If a terminal grid cell cannot be discarded, verification fails loudly.

## 3-point search

- Grid: $G=16000$.
- Domain: $u,v\ge0$, $u+v\le4$.
- Target: $221/10^6$.
- Box lower bound: independent range minima for $w(u),w(v),w(u+v)$.

The box cover is conservative near the diagonal boundary: boxes may include
points with $u+v>4$, which can only weaken a lower bound.

## 7-point search

- Grid: $G=4000$.
- Target: $19/5000$.
- Pressure cutoff: if $\sum g_i\ge11.4$, the linear pressure alone proves
  the target.
- One-body pruning: each gap contributes
  $U(g)=g/3000+w(g)/3$. Cells on which $U\ge19/5000$ are removed before
  the six-dimensional product is formed.
- Remaining boxes: every consecutive partial sum in (4.1) receives its
  range-minimum lower bound, and the widest coordinate range is bisected.

The surviving one-body components are derived by the program and recorded in
the run report. They are not assumptions.

## Trust base

The finite verifier trusts:

1. Python and IEEE-754 binary64 semantics;
2. `python-flint` and the Arb/FLINT libraries;
3. the short source code in this repository;
4. the operating system and hardware executing them.

It does not trust sampled floating-point optimization, cached interval tables,
or the committed run logs. A stronger future artifact could replace the Python
search with a proof-assistant-checked certificate consumer.
