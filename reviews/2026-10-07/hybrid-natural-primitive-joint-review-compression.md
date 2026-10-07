# 459 自然逆列与 primitive 联合能量：独立全文审查（compression）

2026-10-07。结论：**全文限定 PASS；最终所绑定版本未发现 P1/P2 数学阻断。**
通过范围是同一中央归一化下的双向 Euler 恢复、固定尺度的有限恢复尾、
只含 primitive reciprocal poles 和指定 joins 的具体观测量，以及给定
误差门槛以内的 weighted strict-saving 等价。没有证明任一端的实际 saving，
也没有新无零边界、零点比例或 RH 证明。

仅新增本审查文件。被审稿、已有笔记与冻结审查、外部 math 源、Goal、Git
均未修改。本审查没有另派子 agent。

## 1. 实读对象与绑定

canonical LF 规则为 CRLF 和孤立 CR 转 LF，再作 UTF-8 SHA-256；不作
空白、数学或 Unicode 归一化。全文读入 459 与直接三列接口，相关 source
段逐段核对。最终绑定如下：

| 实读对象 | canonical LF SHA-256 | bytes | lines |
| --- | --- | ---: | ---: |
| `notes/459-natural-inverse-and-primitive-zero-joint-reduction.md` | `fe6046154965fb8e833e0a96adf0801f9aa4fd4b2ea8b27397748c79193477b6` | 8861 | 230 |
| `reviews/2026-10-07/hybrid-three-column-reflection-research.md` | `30929e068a6b1610a1ea64aea4e5a0d46623b9fd2f7e41c18f77044d7b209878` | 27422 | 524 |
| 外部固定 `paper.tex` | `42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3` | 766316 | 16677 |

外部源为 `E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`，
固定 commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`。本轮重读
705–726、1425–1453、1602–1640、4221–4268、4390–4479、4610–4633、
12343–12360、12376–12408。其通用 Hecke、raw inverse 与 smooth-family
合同仍按被审稿的 [R] 处理；本审查不宣称重新认证整条源证明链。

初读版本的引言将 fixed-scale raw 段称为 supremum，且尾估计的逐项
不等式未明列 `t<1`。两点已向 root 和 radial_review 报告；作者修订后的
最终绑定版本分别给出 source 12394–12408 和 `0<t<1`。以下只审最终版。

## 2. 同一 target、中央归一化与 independent height

source 705–726 的 inverse 正是

\[
 X^{-1/2}\sum_n\mu(n)\psi(n)W(q_n/X),
\]

所有自然零值保留。459 用 `f=V(y)y^{-sigma-i omega}` 替换 test，仍然
使用相同的 `X^{-1/2}`、Möbius、finite target 与 character orientation。
primitive 列只改用同一 presentation 的 primitive inducer，没有平方 target。

source 4221–4268 将固定 exclusions 与 row 零值记录为 conductor primes
或 redundant radical；实际 detector 已排除会诱导 principal character 的
有限 physical rows。459 的非 principal 前件须按这个实际排除读取，保证
primitive inducer 非 principal。不能仅因带 zero extensions 的函数不恒等于
1，便宣称其 primitive inducer 非 principal。

`omega` 是原 inverse test 的独立长列 height。它既不并入 finite-order
Hecke character，也不与两个 plain heights 对角化。source 1437–1442
给 trivial infinite type 与 Gamma(s) 的 FE，故三列接口的 primitive constant

\[
 C_v=3Q_{\psi_v^*}/(2\pi)^2
\]

适用。这里 `C_v>=3/(2pi)^2>0`，只需要固定正下界；不需要字面 `C_v>=1`。
真正 FE 的使用仍属明列 [R]。

## 3. 双向恢复与全部 zero masks

记 `a_p=psi_v^*(p)`。在 primitive conductor 上，自然与 primitive
character 都为零；这些 primes 不放入 redundant `R_v`。在 `p|R_v`
上，primitive 值为单位，自然值在一切正 valuation 上为零。因此自然
inverse 的该局部 series 是 1，primitive inverse 的 series 是 `1-a_p t`。

将后者乘完整 geometric series `sum_(j>=0) a_p^j t^j`，正 valuation
`e>=1` 的系数精确为 `a_p^e-a_p a_p^(e-1)=0`，unit 系数为 1。
这逐 prime 证明 (3)，包括重复 powers；反向乘有限 factor `1-a_p t`
证明 (4)。在 `R_v` 外，两列局部系数相同。故 primitive-conductor、固定
exclusion、row-dependent redundant primes 的所有 zero masks 均保留。

中央归一化也逐项吻合：

\[
 \frac{\psi_v^*(h)}{\sqrt{q_h}}P_v(X/q_h;f)
 =X^{-1/2}\sum_m\mu(m)\psi_v^*(hm)f(q_hq_m/X).
\]

给定 X 时 `q_h<=c_1 X` 才可能非空，故 (3) 实际有限。反向式 (4)
是有限 inclusion–exclusion，不需要 analytic continuation。

特别，恢复在 `X=D/q_h` 上沿用原来的同一个 f。如果实际长列包含
`V_≤(Dy/D_*)`，其中 D 是原 block 的固定参数，不改成 `X`。这样 inner
test 在 `y=q_m/X` 上给 `V_≤(q_h q_m/D_*)`，正对应原自然指数 `hm`。
重新校准 cutoff 会破坏恢复。纯 phase 的 `q_h` 依赖同样已在这个 f 的
scaled argument 中，不再额外添加或删除一个 height factor。

对每个固定 `s>0`，有限小 norm primes 吸入常数，大 primes 的
`-log(1-q^-s)<=epsilon log q` 给 (5)。取 `s=1/2`，恢复系数的绝对
mass 以及反向有限加号 mass 都是 `O((NR_v)^epsilon)`。各 inner scale
不超过原 scale，因此 (6) 的双向 scale-supremum 比较成立。
这是 supremum 的比较，不是 fixed-scale 两列相等，也不是新的 cancellation。

若 `NR_v<=U^K`，先将 product epsilon 缩小即可给任意小 U 幂损失。
由于比较逐行成立，任意非负真实 row weight 都可乘入再求和；无需 R 与
weight 独立。这项事实不产生跨 rows 的共同 separating measure。

## 4. 固定尺度尾与恢复后的尺度范围

本域 ideals 的计数 `O(X)` 与 annular support 给
`|P_v(X;f)|<=C_f sqrt X`，对所有可能非空 `X>=1/c_1` 成立。
常数只需 f 在 annulus 上的绝对值；`|y^(-i omega)|=1`，所以此处对
independent omega 一致。

当 `0<t<1`，`q_h>D^theta` 时有

\[
 q_h^{-1}\le D^{-\theta(1-t)}q_h^{-t}.
\]

因此被审稿 (8) 正是 `sqrt D` 乘这项 geometric tail，幂为
`1/2-theta+theta t`。先固定 theta>1/2，再固定充分小 t，之后缩小
product loss，就得到 (14) 所需的任意小幂损失。没有使用 Möbius saving。

保留的 `h` 满足 `q_h<=D^theta`，故 primitive scales 精确落在
`[D^(1-theta),D]`。这里所有 f、finite characters 和 primitive zero set
仍然相同，scale 变化只进入中央 Mellin power。

## 5. Primitive poles、G 权重和恢复误差

三列接口在 R=1 时给 primitive inverse 的有限 rectangle identity。
负线 `s=-r+it` 的 reciprocal FE 是

\[
 L(s,\psi^*)^{-1}=\varepsilon^{-1}C^{s-1/2}
 \frac{\Gamma(s)}{\Gamma(1-s)}L(1-s,\bar\psi^*)^{-1}.
\]

取 `r=1/20`，右侧 Euler series 在 `Re(1-s)=1+r` 绝对收敛。
三列接口的 reciprocal kernel subtraction 后为 `O(y^-2)`，其常数
对 pure omega 一致；当 `CX>=1`，其完整负线 integral 为
`O(C^-3/2 X^-3/2)`。保留尺度的下端趋于无穷，且 C 有固定正下界，
所以 (10) 在充分大 D 对所有 retained scales 一致适用。

每一 primitive residue 与指定 horizontal join 都线性地保留。恢复后
Mellin factor 的精确计算是

\[
 q_h^{-1/2}(D/q_h)^{s-1/2}=D^{s-1/2}q_h^{-s}.
\]

故 (12) 的 `G_(v,theta)(s)=sum_h psi_v^*(h)q_h^-s` 正确；不是
`q_h^(-s-1/2)`，也不是未经恢复的 natural zero-extended phase。
G 是有限 entire polynomial，只能取消已有 poles，不能产生 redundant
Euler pseudozero poles。multiple zeros 的 higher residues 包含 G 的相应
derivatives，不能用 (15) 的 simple-zero 例式替代。

恢复负线误差的绝对和是

\[
 C^{-3/2}D^{-3/2}\sum_{q_h\le D^\theta}q_h
 \le C^{-3/2}D^{-3/2+\theta(1+t)}
       \prod_{p\mid R_v}(1-q_p^{-t})^{-1}.
\]

这是 (13)。与恢复尾使用同一小 t 时，两者 D 幂之差为 `2theta-2<0`；
故该负线误差确更小。C 的固定正下界足够吸入常数。

若 `Re rho>=beta_0>0`，取 `0<t<beta_0` 对 G 的 geometric tail 作同一
计算，得到 (15) 后的 `G(rho)=D_R(rho)^(-1)+error`。这保留 primitive
spike 的真实权重，没有提供 `1/L'(rho)` 的新上界。

## 6. Family、vertical tails 与参数顺序

对同一 row 的所有 retained scales，使用以同一个 omega 为中心的
rectangle，选同一个 `H_v≈U^tau`。Boundary zero 条件只依赖 primitive
L，不依赖 scale；在固定 positive-width H interval 中避开离散坏 heights
即可。这个选择不要求随 row/profile 光滑，本稿也不对它求导。

`fhat(c+it)` 是 untwisted V 的 Mellin transform 在 `t-omega` 的 translate。
右 absolute line 的 reciprocal Euler product一致有界；负线由 FE 和
Stirling 有

\[
 |L(-r+it,\psi^*)^{-1}|
 \ll C^{-1/2-r}(1+|t|)^{-1-2r}.
\]

因此外部高阶 Mellin decay 对 V 求导，没有 `|omega|^N` 的新费用。
在 `X in [D^(1-theta),D]` 上，vertical error 的 scale prefactors 有一个
预先固定的 U 幂上界。求恢复和时
`sum_h q_h^-1/2<=O((NR_v)^epsilon)`，所以也不按 retained h 的数量
支付额外大费用。

合法顺序是先固定 arithmetic family、长度范围、cutoff family、有限
internal/Sobolev orders 与 cumulative added-frequency allowance；再选小
的正 tau，最后选 external tail order N 支付任意预先给定的有限 A。
source 4610–4633 的实际 cutoff transition argument 有界，因此原 untwisted
annular seminorm确可统一。scale supremum 的有限 derivative 可能付固定
polynomial height order，这一 order须在 tau 之前固定；不能与 external N
混用。实际 independent inverse height 始终保持。

horizontal joins 含未付的 primitive reciprocal 值，完整保留在 Z 中。
“Boundary 无零”只保证积分合法，不给一致 inverse bound；增加 external N
也不消灭这些 joins。459 没有作这种偷换。

原 raw scale supremum来自 source 12394–12408 的 Sobolev argument。
其 raw 行范围仍需要 fixed positive margin `H>=D^(1+c)`。实际 whole
amplification 的 `eta>ell` 留出这个 margin；(6) 仅传递已有预算，不推广
该 raw 合同到任意 eta 或任意 live row-dependent coefficients。

## 7. Weighted chi 等价的独立计算

写 `Delta_v=M_v-Z_(v,theta)`。由 (14)、`D=U^ell` 和任意小损失，

\[
 |\Delta_v|^2\ll U^{-\ell(2\theta-1)+\epsilon}+O(U^{-A}).
\]

结构 rows 数至多 `U^eta`，原 two-plain/once-slot 实际 cap 为
`|B_v|^2<=U^(b+epsilon)`。故 (16) 的 exponent 精确为
`eta+b-ell(2theta-1)+epsilon`。external A 可在最终误差目标、row 数与
B 的 polynomial cap固定之后增大，以吸收这些乘子；这只改变尾 order。

令 `Gamma_tail=ell(2theta-1)`。对 fixed `0<chi<Gamma_tail`，若
`||MB||_2^2<=U^(eta+b-chi+epsilon)`，Hilbert triangle 给

\[
 \|ZB\|_2\le\|MB\|_2+\|\Delta B\|_2.
\]

后项有严格更小幂，故推出同型 Z bound。反向完全相同。这证明 (17)，
不需要先展开或删除 cross terms。任意小 epsilon 必须在固定严格 margin
`Gamma_tail-chi` 之后缩小。

取原 plain peak set 的 indicator 为 weight 时，删去 B 后同理得到 restricted
unweighted energy 的等价。family、peak set、profiles、所有 physical once
slots 和各自 heights保持原对象，不能按 desired covariance 重新选择。
在 reference `theta=3/4` 下门槛为 `ell/2≈0.5621135734`；该数只描述
误差允许的 saving 范围，绝不证明 chi 为正或达到这个值。

## 8. 最终通过范围

通过了同对象 natural/primitive 双向恢复、所有 local zeros 的精确保留、
scale supremum 的逐行加权比较、finite G 的正确 Mellin 权重、primitive
负线及恢复尾、fixed family/independent height/vertical order 的合法量词，
以及 `chi<Gamma_tail` 的 weighted norm 等价。

仍未支付 primitive residues 与实际 plain/prime peaks 的联合去集中、multiple
residue 大小、horizontal inverse bounds、共同 separating measure、实际
strict mixed saving、全域 continuation或新 sigma certificate。移走显式
pseudozero poles并不删掉原 natural masks；它们转入 row-dependent G 与
定量恢复余项。这是已证明的归约，未成为新的边界证明。
