# 459 独立审查：同一自然逆列的 primitive 联合归约

2026-10-07。审查人：twisted_research。结论：**限定 PASS**。
本报告逐式复核最终 459 及其实际三列负线接口。通过范围是有限恢复、
同函数的尺度 supremum 比较、有限恢复尾、primitive 残数/joins 表示与
条件 strict-saving 等价；并未证明其任一侧已有新的 saving。

## 1. 实际绑定与输入范围

- [459 正文](../../notes/459-natural-inverse-and-primitive-zero-joint-reduction.md)：canonical LF SHA256
  `fe6046154965fb8e833e0a96adf0801f9aa4fd4b2ea8b27397748c79193477b6`，
  8861 UTF-8 bytes，230 split lines。
- [三列研究](hybrid-three-column-reflection-research.md)：SHA256
  `30929e068a6b1610a1ea64aea4e5a0d46623b9fd2f7e41c18f77044d7b209878`。
- 只读来源 `E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`：
  canonical LF SHA256 `42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`。

哈希按 UTF-8 解码、CRLF 和单独 CR 转 LF 后计算，不 trim、strip 或删除 EOF。
核读来源 705–726 的归一化、1425–1453 的 FE、1602–1640 的 deleted
positive-half-plane product，以及 12343–12360 的 fixed-scale raw moment
和 12394–12408 的 scale-supremum。459 最终稿已准确区分后两者。
这些原始合同与 finite-order Hecke FE 仍属于 [R]；本审查不认证整个外部主稿。

## 2. 逐系数恢复与原 cutoff

在 primitive conductor 外的 redundant prime，primitive reciprocal 的局部
因子是 `1-a_p t`，自然 reciprocal 的因子是 1。前者乘
`(1-a_p t)^{-1}` 恢复后者，反向乘 `1-a_p t`。这直接给正文 (3)、(4)，
且中央归一化准确产生系数 `psi*(h)/sqrt(Nh)`。自然零掩码因此精确恢复，
没有以 primitive 角色不为零来取消自然零。

**每个 `P(D/Nh;f)` 都使用原来同一个 f。** 原 D 截断、原 annular profile、
原长列 height 均保留；不能在短尺度 `D/Nh` 改用重新归一化的新 cutoff。
给定 X 时 `Nh<=c_1 X` 才有项，因此无限 geometric 展开实际有限。

正文 (5) 对每个固定 s>0 成立：有限小 norm primes 合入常数，大 primes
满足 `-log(1-q^{-s})<=epsilon log q`。有限加号 product 同理。以 s=1/2
控制恢复系数总质量，得到 (6) 的逐行 scale-sup 比较。任何非负真实行权
均可随行而变；该步骤没有要求 R、权重或 heights 跨行独立。它也不给
固定尺度观测量的双向比较，更不给共同 separating measure。

## 3. 尾与 primitive 负线

本域 ideal count 的线性界及固定 annulus 给
`|P(X;f)|<=C_f sqrt(X)`，对 omega 一致。非空尺度满足 `X>=1/c_1`。
对固定 `0<t<1`，逐项

\[
 (Nh)^{-1}\mathbf1_{Nh>D^\theta}
 \le D^{-\theta(1-t)}(Nh)^{-t},
\]

证明 (8)。先固定足够小 t，再缩小 product epsilon，得到任意小幂损失。
最终稿的 `0<t<1` 明确且必要。保留尺度 (9) 精确为 `[D^{1-theta},D]`。

primitive 情形三列负线接口 (10) 使用同一 primitive conductor、同一 f、
同一 primitive rectangle 与同一 H_v。Bessel 核的 leading term是
`fhat(0)/y`；扣除此项后余核 `O(y^{-2})`，不是任意阶快速衰减。
这给 `C_v^{-3/2} X^{-3/2}`，而非靠增加外部 tail order 得到它。
对 (9) 的所有短尺度同用 H_v，故 primitive 零点集合和无零 boundary
不改变。全部 multiplicities、可能的 trivial zeros 与 horizontal joins
必须保留。

原 untwisted annular seminorm控制 vertical tails；换变量到 `t-omega`
不产生 `|omega|^N` 的额外费用。先固定 profile、contour 和长度范围，
再选 tau 与 external order。此顺序不消灭 horizontal inverse integral；
joins 仍是实际未付对象。primitive C_v 有固定正下界，足以使用该界，
不需要假称其数值大于等于 1。

## 4. 有限 G、残数和误差指数

检查最关键的中央因子：

\[
 (Nh)^{-1/2}(D/Nh)^{s-1/2}=D^{s-1/2}(Nh)^{-s}.
\]

因此 (11) 准确是 `fhat(s) D^{s-1/2} G(s)/L_primitive(s)` 的残数与
同一 joins。G 为有限 entire Dirichlet polynomial，没有 redundant Euler
pseudozero poles。自然 masks、R_v 和 primitive phases 留在 G 及恢复尾内。
多个 primitive 零点使用完整 Laurent residue，不能只用 (15) 的 simple
示例，也不能丢掉 G 的导数。

恢复负线误差为
`C_v^{-3/2}D^{-3/2} sum_{Nh<=D^theta} Nh`。使用 (5) 后即为 (13)。
它和恢复尾的幂次差是 `-2+2theta<0`，所以 (14) 正确；vertical errors
先取足够大的外部 order 后再吸收恢复质量、行数和其他固定幂。

对 `Re rho>=beta_0>0`，同一正半平面 geometric product 收敛并给正文的
G 尾估计。primitive spike仍在，未给 `L'(rho)` 下界，也没有得到新的
primitive cancellation。

## 5. 联合能量与结论的准确边界

从逐行误差 `D^{1/2-theta+epsilon}`，平方、乘原 `|B_v|^2<=U^{b+epsilon}`
并对 `#rows<=U^eta` 求和，得 (16) 的精确指数
`eta+b-ell(2theta-1)+epsilon`。B_v 保持原两 plain、once-prime slot、
自然零、所有不等 heights；不能免费把真实 b 改成 selected amplitude。

对每个固定 `0<chi<ell(2theta-1)`，误差 Hilbert norm 比目标 norm 有
严格幂余量，三角不等式双向给 (17)。任意非负实际行权或原 plain 峰集
指标也成立。这仅是同对象的条件等价；两侧 strict joint bound 均未支付。
`theta=3/4` 所得约 0.5621 是误差允许的 saving 范围，不能读成已实现 chi。

审查未发现 P1/P2 数学阻断。原 row-dependent R/h phases不能跨行分离；
primitive reciprocal residues、L'、multiple residues、horizontal joins 与
不等高度 plain 峰的相关性仍是下一步的具体联合输入。本结果没有新比例、
无零边界、RH 证明或新增全族原始平方平均。
