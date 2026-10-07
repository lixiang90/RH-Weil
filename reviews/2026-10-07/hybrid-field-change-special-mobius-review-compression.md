# 换域 special Mobius 子族与 primitive joint 独审：compression_bridge

2026-10-07。结论：**全文限定 PASS；没有全 Gaussian raw saving 或新边界**。
只新增本独审，不改被审源、冻结 notes、论文、math、Goal、脚本、output 或 Git。

全文复读最终
[field-change 源稿](hybrid-field-change-special-mobius-next-research.md)，
canonical LF SHA256
`1afe4d0b2393f0c67997c2f83680f0e9ed46ae12e0f84f7b337e2a6e0fdb23db`，
7711 bytes / 153 lines。LF hash 仅将 CRLF 与 lone CR 换成 LF。
核对同一 458 的 eta、smooth W、完整 row-scale supremum，以及 459 的恢复。

## 1. 特殊第四幂行与明确的 reciprocal 前件

odd primary r 满足 r^4 仍 primary，primary r->r^4 注入，
N(r^4)=(Nr)^4。第四次符号在 (n,r)=1 时等于1，在不互素处等于0，
所以源 (2) 是 zero-extended 精确恒等式，不能将其 mask 删除。
Nr<=U^(1/4) 的实际 rows 数 O(U^(1/4))，无需 r squarefree。

通过源明列的同一 fixed eta 前件 [Z_eta]，不是所有 Gaussian characters
的无零/倒数前件。最终版本明确 `1/2<=theta_0<1`，选择 a>theta_0
因此 a>1/2；这保证 D'^(a-1/2) 对尺度递增，sup<=D 的处理合法。
fixed gap 和 subpower bound
`|1/L_eta*(sigma+it)|<<_(delta,eps,eta)(1+|t|)^eps`
是实际所需条件，固定正次数的 polynomial bound 不够。

原长 norm height 先固定在 U^A 内，再缩小该 subpower epsilon。
Mellin decay 只作用于原 untwisted W/profile，保留 height shift，不以
越来越高次数微分原 norm phase。这样 height 损失可吸入 U^epsilon。
这一新前件仍作用于原 eta，不能为了满足它换成另一个 Dirichlet target。

## 2. Gaussian norm base-change 与 finite factors

若原 eta 确为 chi∘N，ordinary natural Hecke presentation 的 Euler products
有 `L_K(s,chi∘N)=L(s,chi)L(s,chi chi_-4)`。
split primes 的两边是平方 local factor，inert primes 两个 rational factors
相乘为 `(1-chi(p)^2 p^(-2s))^-1`，ramified 2 也按实际 character 的零值
匹配。右侧 product character 可能 imprimitive，primitive eta 的 L 也可能
与该 natural norm presentation 差有限 deleted factors。

此外源 sum 只含 odd ideals，lambda 的实际零掩码亦须保留。
在固定 a>0 上，任一有限 Euler radical S 的两个界都可用：

\[
 \prod_{p\mid S}|1-a_pq_p^{-a-it}|^{\pm1}
 \ll_{a,\varepsilon}(NS)^\varepsilon,\qquad |a_p|\le1.
\]

小 primes 吸入固定常数，大 primes 用 q^-a<=epsilon log q 比较。
故从 Dirichlet [R] 输入转为同一 primitive ordinary L 的近线 inverse bound
只付真实 finite factors 的小幂损失，不需要删除它们的 poles/zeros。
这是原 eta 已满足 norm base-change 时的准入；任意 Gaussian eta 及全部
unit/lambda twisted targets 不自动在该范围内。

## 3. 第四幂子族的指数与 generic obstruction 区分

对每个 r，将其附加自然 mask 当真实 deleted Euler product 在线 Re s=a
估计，bound 为 (Nr)^epsilon。Mellin inversion 给
`sup_(D'<=D)|M_(r^4)(D')|<<D^(a-1/2)U^epsilon`；
small scales 是有限项，D>=1、a>1/2 已保证可被右侧覆盖。
principal L 的 s=1 pole 是 reciprocal zero，shift 不产生新 inverse residue。

平方并按真实 r 计数，得到 `U^(1/4+eps)D^(2a-1)`。
设 delta=a-theta_0，源选择 `0<delta<=min(3c/16,(1-theta_0)/2)`，
保证 a<1。又 theta_0<=7/8，故 `2a-1<=3/4+3c/8`。
U>=D^(1+c)、2a-1>0 于是给

\[
 \chi=\frac34-\frac{2a-1}{1+c}
 \ge\frac{3c}{8(1+c)}>0.
\]

该 bound 是特殊实际 Mobius 子族的上界。460 的 prime-only positive
coefficients lower bound 针对任意列系数 operator norm，不能转为此固定
Mobius/eta/W 的下界；反向也不能从这个子族 upper 推出 whole raw upper。
其他 quartic primitive conductors 随 u 的 a,b,c 部分变化，不由固定 eta 的
[Z_eta] 控制。ordinary Hecke FE 与 quartic metaplectic completion 分开。

## 4. 原 profile、norm phase 与 fixed-scale primitive 恢复

Gaussian finite-order ordinary characters有同一 Gamma(s) archimedean factor，
只有 fixed discriminant/conductor constant 改变，primitive C 有固定正下界。
因此 459 的局部 Euler identities、ideal count、negative Bessel kernel、
same-row rectangle 及尾界适用于这个原 presentation；principal inverse
使用已另审的 meromorphic FE，s=0 的 apparent Gamma pole 抵消。

源 (1) 的 n^-1/2 normalization 对应 source459 的
`f(y)=y^(-1/2+i omega)W(y)`，外面有 `D^(i omega)`。
该 unit phase 必须保留。finite G 仍为
`sum_(Nh<=D^vartheta) psi_u*(h)(Nh)^(-s)`；norm height 已在 fhat 的
shift 中，不可再给 G 多加一个 h^(i omega) 而重复计数。
若改用实际短尺度 raw columns，所需 h^(i omega) 恰来自 global D phase
与短尺度 (D/Nh) phase 的比值，两个表示必须一致。

各 primitive scales D/Nh 仍用同一个原 f，不重新校准 cutoff。
same row 的 retained scales 使用同一个 primitive-zero rectangle，
全部 actual zeros/multiplicities、h/R phases 与 horizontal joins 保留。
恢复的逐行误差 `D^(1/2-vartheta+eps)U^eps` 与原 independent height
量词相容：先定 profiles、length/height polynomial ranges 与 internal orders，
再选 H 的幂长度，最后选 external tail order。在所讨论 U>=D^(1+c) 中
D<=U，尺度范围满足该要求，不存在反向选择 profile。

O(U) Gaussian rows 平方后给源 (7)。vartheta=3/4 时误差相对 U 为
D^-1/2 小幂损失。Hilbert norm triangle 只给 raw 与同 rows 的 primitive
residues/joins 能量的线性 upper 等价，未给 Z 的实际 joint estimate。

## 5. Sup 接口的小尺度补充核验

sup 必须在误差已经对同 row、同 profile、同 contour 一致之后取。
不能把逐尺度大筛直接交换到逐 row sup。对大尺度，先固定
epsilon<vartheta-1/2，源 (6) 的 pointwise error 的 sup 至多 U^epsilon，
平方求和 O(U^(1+epsilon))。

小尺度的 M 是有限项，可并入 O(U)。若同时将 Z 的小尺度也计入 full
sup，应沿源 finite G 定义在当前 D' 截 `Nh<=D'^vartheta`：
D'<1 时 G 为空、Z=0；1<=D'<=固定 D_star 时 h 数有固定上界，
primitive X=D'/Nh>=1 且<=D_star。其 raw primitive column bounded。

原 Bessel kernel还有对所有 y>0 的 loose、height-uniform bound
`|f_+(y)|<< y^-2`：直接用
`|J_0(2/sqrt(ty))-1|<=C/(ty)` 与 t 的 fixed annulus 即可。
所以这些有限小尺度的 negative-line integral 也是 O(1)，primitive C
固定正下界足够。由原 Cauchy identity，residues 加 joins 的整个 Z aggregate
也是 O(1)；这里不声称单独 residues 或 joins 小。
因此两种 full sup 的 small-scale contributions 都能并入 O(U)，linear
目标的 triangle 比较成立。也可仅对 D'>=D_star 取 Z sup 再另加 O(U)。

## 6. 单位项基线与最终范围

非零 smooth W 在 [1,2] 中取 W(y_0)!=0，D_0=1/y_0 在 [.5,1]。
此区间的 Gaussian odd ideals 唯有单位理想；lambda norm2 已排除，
odd nonunit 的最小 norm 实际至少5。mu(1)=eta(1)=mask(1,u)=1，
任何原 norm phase 在1也为1，所以 `M_u(D_0)=W(y_0)` 对所有 u 精确。
全部非零 Gaussian rows 数为 Omega(U)，给 full scale-sup 的真实
`Omega_W(U)` 基线。它不依更换列系数，亦不是 finite-prime asymptotic 模型。

这只排除该 full sup 的 strict U-power saving，不排除固定 large scale 或
实际 marked peak-set 的 saving；若另一原 test 删除单位或限制 large scale，
本基线不可挪用。whole Gaussian raw 的线性合同与 quartic marked joint
completion 仍未支付，458 的 mixed (UD)^(2/3) 费用也未因本归约改善。
因此源的结论范围正确，没有新 sigma、比例或 RH claim。

## 7. 指定三列源排版更正的只读逆还原核验

根节点授权并完成三列源第292行 control-space 改为显式 thin-space。
只读核验 canonical current source 为
`30929e068a6b1610a1ea64aea4e5a0d46623b9fd2f7e41c18f77044d7b209878`，
27422 bytes / 524 lines。只有 byte offset14101 从旧空格32变为逗号44；
将该处逗号逆变回空格精确得到旧 hash
`72c6f95ef52bd6a759da23067e3c3e8d32d1e7278c9fb68adacafed733cefc15`。
这是数学表达的排版间距更正，其他 source bytes 保持。

本人既有459独审只被根节点替换表内该 source hash：current canonical
`7dc87637dff9aa95690d2028dee76fe9742e2d026c754186346600793f68282c`，
12031 bytes / 247 lines。将该一个 hash 逆换回旧值，精确得到本人原审查
`5cde2cec73abb06f33bb68dc90b69721fde97e1cbcd022fbdf89393c107f7df7`。
本次没有再改该审查或 source，也没有把指定更正扩展到其他冻结文件。
