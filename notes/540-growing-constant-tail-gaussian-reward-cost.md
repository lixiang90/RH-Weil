# 成长恒定尾供给的 Gaussian 全源费用与全频窗上界

2026-10-14；C011第二且最后一轮；冻结新增基线0c4f3a3/全部≤538。
新增为连续解析的必要费用，非新的算术正性，不推完整Q负或完成宏观Goal。
两份不同组织审查：[Gaussian原推导](../reviews/2026-10-14/c011-second/gaussian-leakage-derivation.md)、
[消元及量词逆审](../reviews/2026-10-14/c011-second/variable-envelope-reverse-audit.md)。
不调用有限矩阵、ζ零点或新数值扫描；所有参数和误差在下文逐项支付。

## 1. 对象与证明类：全源同一供应器

I_L=(-L,L)，H_L=L²(I_L,du)，原complex源零延拓；
Ff(t)=∫f(u)e^(-itu)du，Plancherel norm为(2π)^-1∫|Ff|²。
完整actual Q_L保Γ(t)=Reψ(1/4+it/2)−logπ=2θ′、dual pole和全部p^k<e^(2L)。
消费[539](539-growing-weil-prime-cost-and-constant-tail-boundary.md)的精确分拆

    Q_L=M_(L,β)+K_(L,Ω,β)+T_(L,Ω,β)，
    M_(L,β)=βI−Σ [2logp/√(p^k)]J_log(p^k)，
    T(f)=(2π)^-1∫_(|t|>Ω)(Γ(t)−β)|Ff(t)|²dt。

每个fixed L和有限Ω、β的K为L²-compact自伴；pole的odd负项没有删除。
本轮只审以下来源：先选一个逐点constant exterior envelope

    Γ(t)−β≥a≥0，|t|≥Ω，

再在**同一完整源空间**抽取

    a(I−B_(L,Ω))≥τI+U，τ≥0、U≥0，

其中B是原frequency-band投影在H_L上的压缩，核sin(Ω(u−v))/(π(u−v))。
最后以bounded供应器R=M+K+τI+U≥0证明Q≥R≥0。
U及其他加在R中的修复在每个fixed L上须compact，才能消费539的prime门。
rank、norm和所有标量可任意随L变化；不要求uniform compactness。
下面单独的尾scalar门只需U为bounded非负算子。

设

\[
C_L=\sum_{p^k<e^{2L}}\frac{2\log p}{\sqrt{p^k}}
             \left(1-\frac{\log(p^k)}{2L}\right).
\]

539已以合法smooth carrier/全compact和完整12项Fraction原件支付

    R≥0 ⇒ β+τ≥C_L；C_(3/2)>4>Γ(256)；C_L→∞。

这不是whole Q非负的必要门：R只能是指定lower供应器。

## 2. Gaussian 的准确截断、频尾与 norm 费用

对任意L>0、Ω>0，B为positive compact contraction。
δ=1−||B||严格在(0,1)：compact最大本征值若为1，非零源就同时time-limited和
band-limited；原时限源属L¹，其Fourier为entire，band外消失迫使它恒零。
B非零同理由成立。未宣称成长L上的uniform正下界。

冻结α=Ω/L，q=LΩ，并取全线norm1源及窗内截断

    h(u)=(α/π)^(1/4)exp(−αu²/2)，g=1_I h。

α使两个tail指数αL²与Ω²/α恰等于q，并最大化二者较小值。
准确Gaussian积分给

    r=||h−g||²=erfc(√q)，
    s=(2π)^-1∫_(|t|>Ω)|Fh(t)|²dt=r，||g||²=1−r。

外band投影的contraction/triangle完整支付截断造成的频域变动：

    ||P_out Fg||_(Plancherel)≤√s+√r=2√r。

故

\[
0<\delta\le\frac{4r}{1-r}<\frac4{e^q-1},\qquad
0<\delta<\min(1,5e^{-q}).\tag{1}
\]

这里erfc(x)<e^(-x²)由v=x+w的积分表示立即得到；q≤log5用δ<1，
q>log5用第一上界。没有遗漏负频、截断或重新归一化的分母。
Ω=0时δ=1、α=0无此Gaussian，明确排除；L=0无非零norm1源。
g不是Cc∞，但I−B及U有界，原Cc∞(I_L)稠密，所以全smooth型门延拓H_L；
也可用strict-support smooth g_j→g，norm一并归一化，取得同一infimum。
若要Dlog域，g的Fourier O(1/t)亦满足完整logarithmic norm，但本节无需whole Q计算。

由a(I−B)≥τI+U且U≥0，对所有norm1源取infimum，严格必要

\[
\tau\le a\delta.\tag{2}
\]

任意非负rank/norm修复不能改善这一scalar门；若U signed或只在删head后的补空间
证明型门，(2)的whole-source版本不自动成立。

## 3. 全参数消元：不遗漏 τ 或等号

联用同一来源的三个必要门

    β+τ≥C_L，β+a≤Γ(Ω)，τ≤aδ，a/τ≥0，0<δ<1，

得到

\[
\Gamma(\Omega)\ge C_L,\qquad
0\le\tau\le\frac{\delta}{1-\delta}\,[\Gamma(\Omega)-C_L].\tag{3}
\]

例如β≥C_L−τ，故τ≤δ[Γ(Ω)−C_L+τ]，移项即可。
等号Γ(Ω)=C_L强制τ=a=0、β=C_L、U=0；它不自动证明R≥0。
没有偷偷替换成β≥C_L，也没有要求β为正或固定7/2。
对q≥log10，由(1)单调消元得到

\[
\frac{\delta}{1-\delta}\le
\frac{4e^{-q}}{1-5e^{-q}}\le8e^{-q}.\tag{4}
\]

## 4. actual Γ 单调性与不扫描 Ω 的统一费用

由[NIST digamma部分分式](https://dlmf.nist.gov/5.7#E6)，在每个compact t区间可绝对
一致逐项求导，x_n=n+1/4，得

\[
\Gamma'(t)=\frac t2\sum_{n\ge0}
       \frac{x_n}{(x_n^2+t^2/4)^2}>0\quad(t>0).
\]

539原件给L≥3/2时C_L>4>Γ(256)，所以可行Ω必须>256。
沿用538/539同规范已付的完整Binet上界（原norm与Γ未改）

    Γ(t)≤log(t/(2π))+1/(15t)+25/(8t²)，t≥256。

因π>3、log(2π)>1，而两个fee在256处之和<1，故Γ(t)<log t。
于是Γ(Ω)≥C_L迫使Ω≥e^(C_L)。设

    A_L=L e^(C_L)，x=LΩ≥A_L。

L≥3/2给A_L>(3/2)e^4>log10，(4)自动适用。对**每个**可行Ω，

\[
\tau\le8e^{-x}[\Gamma(\Omega)-C_L]
      \le8e^{-x}\log(x/A_L)
      \le\frac8{A_L}e^{-x}(x-A_L).
\]

用sup_(y≥0) ye^-y=e^-1，不改变任何源或Γ的量词，得

\[
\boxed{\quad0\le\tau\le\frac8{A_L}e^{-A_L-1},\qquad
 A_L=L e^{C_L},\quad L\ge3/2.\quad}\tag{5}
\]

这是允许β(L)、Ω(L)、a(L)及任意非负compact修复变化后的全Ω统一必要界。
不需PNT渐近；539自含Euler论证给C_L→∞，故A_L/L→∞，(5)还意味着
τ(L)=o(e^-cL)对每个固定c>0。没有宣称此常数或指数为最优。
任何要求uniform τ₀>0或τ(L)最终明显超过(5)的此类计划都失败。

## 5. 量词逃逸与宏观判定

此上界允许τ(L)>0而极快趋零；本轮没有支付成长程序必需误差的不可消除下界，
所以不能说所有逐窗恒定供给证明都失败。亦不能用小δ替代实际非constant Γ-tail的上界。
完整Q高频Γ能量仍增长，R的不足不推出Q负、RH失败或无界窗正性不可能。

必须保留以下未排路径：

- 按source选择β/a或不同joint机制，不形成单一whole-source bounded供应器。
- 先分离有限head，只在补空间抽scalar再支付head/cross；删B的有限个大本征模式
  可使restricted δ≥1/2，Gaussian不必属于该补空间。539的finite条件prime门不能
  无声与本轮的whole Gaussian门拼接成任意条件后的(5)。
- 完整非constant Γ-tail与prime/pole同源signed比较，或indefinite/noncompact修复。
- 新多prime/算术几何来源，或改变domain并重新支付实际ζ可见性。

若仅U按source选但始终U_f≥0，且固定a、τ仍统一于所有源，丢U后(2)仍真；
这不能扩大成对所有source-adaptation的排除。

新增独立输入是完整Gaussian不确定性费用，新增净后果是(5)的全参数scalar约束；
未取得独立算术正性或完整signed成长预算。实际全域正性/Ξ识别瓶颈没有消除，
只是供给费用与路线优先级变得明确。C011已用两轮，应停止继续该split的扩窗/扫描。
新Goal第三分支要求更强joint/source-adaptation核心边界，本轮不满足完整完成门。

## 6. 停止、重新准入与唯一下一动作

停止C011的constant-envelope搬运主攻，保留539/本轮为必要费用前件。
重新准入需实际signed修复/完整Γ余量或全head/complement新来源，
包含成长全complex量词、全部误差及非循环净后果；仅更小τ、更大N或更高精度不够。

下一主合同C012保留完整Γ，用实际Chebyshev primitive把prime与pole共同中心化，
先审绝对primitive-variation误差能否在原Dlog全source上受完整Γ能量统一控制。
这是精确可证伪准入目标，先扣除旧016/252/292–300/405/518等对象的重复范围；
若绝对值费用失败，只有可核同源signed抵消新输入可继续，不把一般恒等式或RH等价晋级。
入口审查与合同准备不另计轮；本轮只消费原cadence一次。
