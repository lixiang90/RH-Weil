# 跟进独立复核：306-spectrum-followup

日期：2026-09-06。保留报告原文，复核范围及剩余事项按正文。

**谱删除、MT/一侧账本及 padded 分子损失的问题已关闭。AEJ 的近似矩阵处理和 GNS 有界性也已修复；但“递增序列穷尽全部约束”还需补一句可数化说明。** 本轮未重复审查已通过部分，也未写文件。

- [谱删除](/F:/codex-build/RH/RH-Weil/papers/partial-weil-configurations-paper.tex:332)：\(b_0=\min(d,\lfloor b\rfloor)\)、非负预算及 \(b_0=d\) 分支均正确。
- [MT 与一侧账本](/F:/codex-build/RH/RH-Weil/papers/partial-weil-configurations-paper.tex:1452)：现在正确调用 `cor:quartic-upper`，补齐同一配置的小边界、归一化条件并使用 \(\liminf\)。
- [notes228](/F:/codex-build/RH/RH-Weil/notes/228-relative-dense-zero-block-transfer.md:232)：先应用 padded 配置，再支付两个分子的边界损失，已关闭原接口问题。

AEJ 的具体复核如下：

**Hermitian 化没有额外损坏矩阵误差。** 对自伴 \(q\)，记
\[
M_q(L)=[L(u_i^*qu_j)]_{ij}.
\]
则严格有
\[
M_q(\widetilde L)=\frac{M_q(L)+M_q(L)^*}{2}.
\]
因此，按新增的 Hermitian-part 约定，Gram、\(Q\)-localizer 及
\(M_h+\varepsilon M_1\succeq0\) 都保持原来的矩阵条件。归一化保持为 \(1\)；指定矩和迹关系在纳入对应的星关系后至多改变为 \(O(\varepsilon)\)，仍趋零。

由此，[新增一致界](/F:/codex-build/RH/RH-Weil/notes/202-archimedean-localizing-weil-completion.md:170)
\[
|\widetilde L(a)|^2
\le(1+\varepsilon)(R_a^2+2\varepsilon)
\le2(R_a^2+2)
\]
成立，不存在遗漏的矩阵维数因子。

**GNS 有界性推导正确且没有循环。** 极限中
\[
L(p^*a^*ap)\le R_a^2L(p^*p)
\]
既保证零范数空间在左乘下保持，也保证商空间上的左乘算子满足
\(\|\pi(a)\|\le R_a\)。因此 \(\pi(h)\) 延拓为有界自伴算子；稠密子空间上的
\(L(p^*hp)\ge0\) 确实推出 \(\pi(h)\succeq0\)。

**剩余文字缺口：** [notes202](/F:/codex-build/RH/RH-Weil/notes/202-archimedean-localizing-weil-completion.md:179) 和[结构论文](/F:/codex-build/RH/RH-Weil/papers/rh-weil-structure-paper.tex:437) 的“每条固定约束最终均被包含”尚不能仅由可数 word 张成推出：\(Q\) 通常仍不可数。这不是定理反例，可以补为：

> 取穷尽代数的递增有限维 \(*\)-空间 \(V_j\)，在每个 \(Q\cap(V_j)_h\) 中选可数稠密子集，连同 word 的 Gram、\(h\)、迹及指定矩约束进行可数穷尽。极限泛函在每个 \(V_j\) 上线性而连续，故正性由这些稠密子集延拓到全部 \(Q\)。

构造紧圆盘中的近似点时，只记录已经加入自身坐标界的坐标，其余暂填零即可。这样不需要假定新引入的辅助坐标已经有界。也可以直接改用按有限约束集索引的有向网。

下面是原 **540 项检查**整理后的完整代码，已重新运行。它覆盖 **90 个配置，其中 58 个非对易**，并非 540 个都非对易。仅依赖 SymPy；全部计算使用精确整数、有理数。完整配置可取 \(E_0=E_1\)。

```python
import random
import sympy as sp


def main():
    rng = random.Random(20260906)
    sigmas = (
        sp.Integer(-3),
        sp.Rational(-29, 10),
        sp.Integer(-1),
        sp.Integer(0),
        sp.Rational(1, 8),
        sp.Rational(749, 1000),
    )
    checked = noncommuting = 0
    minima = [None, None]

    for d in range(1, 6):
        for case in range(18):
            rank = rng.randrange(d + 1)
            U = sp.Matrix(
                d, rank,
                lambda i, j: sp.Rational(rng.randrange(-3, 4), 3),
            )
            P = U * U.T  # Exactly positive semidefinite.

            # Unit lower triangular: invertible with determinant 1.
            V = sp.eye(d)
            for i in range(d):
                for j in range(i):
                    V[i, j] = sp.Rational(rng.randrange(-3, 4), 2)

            qdiag = [
                sp.Rational(rng.choice([-7, -2, 0, 1, 5]), 3)
                for _ in range(d)
            ]
            Q = V * sp.diag(*qdiag) * V.T
            G = P + Q
            noncommuting += int(P * Q != Q * P)

            s = (
                max(sp.Integer(P.rank()), sp.trace(P))
                + sp.Rational(case % 3, 5)
            )
            # Sylvester's law gives n_+(Q) exactly from qdiag.
            b = (
                sp.Integer(sum(1 for q in qdiag if q > 0))
                + sp.Rational(case % 4, 7)
            )
            N = sp.Rational(d + case % 3, 2)
            E1 = (
                max(sp.Integer(0), s + 2*b - N)
                + sp.Rational(case % 2, 9)
            )
            D = s + b
            # E0 = E1 also satisfies tr(P) + 2*b <= N + E0.

            for sigma in sigmas:
                a = 1 - sigma
                L = sp.trace(
                    -G**4 + 4*G**3
                    - (6 - 2*sigma)*G**2 + 8*a*G
                ) / N

                # Equivalent forms of the two finite bounds,
                # computed directly from tr(p_sigma(G)).
                lower_s = (L - 4*a*(1 + E1/N)) / a**2
                lower_d = (
                    L - a*(3 + sigma)*(1 + E1/N)
                ) / (2*a**2)

                margins = [s/N - lower_s, D/N - lower_d]
                assert all(v >= 0 for v in margins), (
                    d, case, sigma, margins
                )
                minima = [
                    v if old is None else min(v, old)
                    for v, old in zip(margins, minima)
                ]
                checked += 1

    assert (checked, noncommuting) == (540, 58)
    assert minima == [
        sp.Rational(3077, 6480),
        sp.Rational(1, 5),
    ]
    print(
        f"checks={checked}; configurations=90; "
        f"noncommuting={noncommuting}"
    )
    print("minimum margins:", minima)


if __name__ == "__main__":
    main()
```

复跑输出：

```text
checks=540; configurations=90; noncommuting=58
minimum margins: [3077/6480, 1/5]
```
