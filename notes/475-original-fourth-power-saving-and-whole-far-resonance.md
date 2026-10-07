# 475. 原路线的四阶增长幂改进与完整远共振付款

2026-10-08。回到原 ζ / Gabor / sharp high-prime 路线，不更换代数数域。
基线 main=46106dc449ac7e6d91a3646b09e63b0b0e272cc1。

本轮得到两项可用于原对象的改进：在原 7/8 条带输入下，正高度标量
四阶矩及原固定起点有限矩阵的增长幂从 3/4 降至 19/26；合法短载体
光滑平均将全部远乘积共振项付为 o(1)，只留下 polylog(X)/X 的近带。
两者仍未给改善零点比例所需的常数预算，也没有新的无零边界。

## 1. 完整证明与审查

本笔记是结果入口；解析证明在下列完整作者源，已由不同作者全文审查。
canonical UTF-8 LF 只统一 CRLF/lone CR，不 trim 或改变 EOF。

| 新输入 | canonical LF SHA256 |
|---|---|
| [正高度零点包四阶上界](../reviews/2026-10-08/hybrid-positive-height-zero-packet-fourth-upper-research-radial.md) | 8bcbd27da46d922d9e6e741fcf9a87012d565052f8d97b3ad12e99b3edbc2481 |
| [固定起点 half-Gram 采样](../reviews/2026-10-08/hybrid-fixed-start-half-gram-sampling-research-root.md) | 7ed68a71d4d22d0bf1d90c61cef231534737188131aad9842669cd11f19c82cc |
| [全标签 actual 远共振](../reviews/2026-10-08/hybrid-whole-ratio-smooth-carrier-far-resonance-research-twisted.md) | 9b8c6064731f65eb4449a3e9da353077baa856a4cb27f93fd5063b6f6a578054 |
| [半素数主质量与 centered variance](../reviews/2026-10-08/hybrid-canonical-semiprime-smooth-subtraction-and-variance-obstruction-research-compression.md) | 7fcb097ad17d77b7281acd1f7c7d0f1580c5519c015437e104823cdfabd52645 |

独审：[root 全文核对](../reviews/2026-10-08/hybrid-original-fourth-power-and-far-review-root.md)、
[固定起点独审](../reviews/2026-10-08/hybrid-fixed-start-half-gram-sampling-review-compression.md)、
[光滑远区独审](../reviews/2026-10-08/hybrid-whole-ratio-smooth-carrier-far-resonance-review-radial.md)。
其中 root 对三个其他作者源均逐行审查；固定起点由 compression 独审。
本轮未改原论文、旧证书或 readonly math 数学源。

## 2. 实际 canonical 算术上界：19/26

保留原 X=T/(2π)、ell=log X、a_ell=||phi||₂²/ell≥c_phi>0 及两个
sharp cutoffs。定义

\[
 P_H(t)=\frac1{a_\ell\ell}
       \sum_{\sqrt X<p\le X}\frac{\log p}{\sqrt p}p^{it},
 \qquad
 M_T=\frac1T\int_{T/4}^{4T}|P_H(t)|^4\,dt.
\]

令 [Rθ] 为 ζ 的全部非平凡零点满足 Re ρ≤θ，固定 5/6<θ≤7/8。
在这一明确输入下，本轮证明

\[
 \boxed{M_T\ll_{\phi,\theta,\epsilon}T^{B(\theta)+\epsilon},
 \qquad B(\theta)=4\theta-3+
                  \frac{3(1-\theta)}{3\theta-1}.}
 \tag{1}
\]

先将 Λ 的两个 Perron prefix 合为整个核 (x^z−y^z)/z，再逐 t 选
H_t≈T 的双横边避零高度。原正高度 principal term、截断、左线及
横边全部付清，保留全部 signed-height zeros 与重数。
零点包核 ell/(1+ell|t+γ|) 的加权 Jensen 给精确中间上界

\[
 \widehat M_T\ll_\phi\frac{\ell^3}{T}
    \sum_{|\gamma|\le16T}X^{4(\beta-1/2)_+}
       +O(X^{-2}\ell^4).
 \tag{2}
\]

Ingham/Huxley 的普通 ζ 密度在固定实部网格上的最大指数恰为 B(θ)；
474 已付的 proper-power L4 norm 差用 Minkowski 返回 genuine primes。
没有在未知增长下删掉四阶差，亦没有以零点包上界反向推无零。

| 原条带输入 | 446 已有四阶增长幂 | 本轮增长幂 |
|---|---|---|
| θ=7/8 | 3/4 | 19/26 |
| 451 的 θ*=0.874957019420098946…，相对原 [R] | 0.749914038840198… | 0.730694976215313… |

在 7/8 时严格节省 1/52。一般差为
(1−θ)(6θ−5)/(3θ−1)>0。这里没有声称经典密度或一般零点包方法的新颖性；
新结果是在本项目相同 sharp signal、正高度窗和原 normalizer 上完成付款。

## 3. 传回同一个原固定起点

474 先前只给短载体平均的 scalar 准入。本轮观察到原 half-Gram 每列
z_u 的真实 ratio 频带为 [−u,ell/2−u]，宽 ell/2。取 support 宽
小于 ell 的实线 multiplier，先对切窗后的真正 L² 函数使用
原 eta=2π/ell 网格的精确 Parseval，再单独付 Schwartz exterior tail。
这没有周期化物理平移或把不同 ratios 按 ell 取模。

对全部原 sigma∈[T,T+s]，s=T/sqrt ell、d=floor(Xell)，得到

\[
 r_\sigma+S_T/2\le\frac{a_\ell T}{2d\eta}E_T(M_T)^2
                         +C_\phi/\ell,
 \tag{3}
\]
\[
 E_T(M)=N_\ell\sqrt M+
    C_\phi(m_T/T)M^{1/4}+C_\phi m_T^2/T,
 \quad m_T\ll\sqrt X/\ell,\quad N_\ell=O_\phi(1).
\]

exact floor 和全部 guard cross 保留在 (3)。新增采样尾在 raw
M≤Cm_T^4 下已付 O(ell^(−6))，不要求未知 fourth bounded。
代入 (1) 后，原每个固定起点的 r_sigma、actual finite high fourth、
entire prime fourth 均有 O(T^(B(θ)+epsilon)) 的一侧增长上界。
最后返回同配置 centered zero matrix 时，继续使用 AF 原背景与
真正未归一化 S1 o(1) 的尾项合同；此末步仍相对 AF [R]。
仅有 normalized S1 o(1) 不足以免费完成该转移。

因此此幂节省能用于原固定 carrier，而非只证明平均中存在一个未知起点。
Schatten triangle 传递的是上界，没有新 quartic additive 等式或常数。

## 4. 完整远乘积共振现在可付清

对合法短载体起点使用固定非负 C∞ 密度 χ；它由长度
a_n=1/[4n(n+1)] 的 uniform densities 无限卷积构成，中心在 1/2。
完整证明给 support χ⊂[3/8,5/8]、int χ=1、χ∞≤8，及

\[
 |\Gamma_\chi(z)|\le e^{-\sqrt{|z|}/16}\quad(|z|\ge256).
\]

每个 actual prime atom 都准确满足
C_(p,ε)(sigma)=e^(i sigma εlog p) Ctilde_(p,ε)。四个 atoms 的
三个内部 P 全部保留，σ 相位为 e^(i sigma S)，S=Σ εlog p。
取

\[
 \Delta_T=1024\ell^{5/2}/X
\]

时，整个 |S|≥Δ_T 的平均核≤X^(−4)。完整 prime 系数质量
O(X²/ell^4) 因而给整体远区 O(X^(−2)ell^(−4))=o(1)。
这统一覆盖全部 H/L ordered words、signs、repeated、four-distinct
及任意 σ-independent label 子集，无需逐 tuple 删除 P。

χ∞≤8 同时保留 472 的 whole-P mean absolute 小量与同一合法
good carrier / moving zero block 合同。若另证 near budget，选点时
仍需在可能增长的预算中保留 good-set probability 分母。

对 half-ratio 的四全异近项，S=log(qp'/pq')。剩余长度仍 X²，
determinant 宽度为 O(Xell^(5/2))；在 |S|≈1/X 时 Γχ(sS)→1。
所以近共振本身仍需真实 signed prime-product 算术上界。

## 5. 平滑主质量扣除与接下来的具体目标

原 c_H=Λ_H*Λ_H 的连续主质量精确为 triangular ρ_X，
其 Mellin transform 是
V_X(t)^2=[(X^(1/2+it)−X^(1/4+it/2))/(1/2+it)]²。
在原正高度窗扣除这个 continuous term 后，Λ 版本的 normalized scalar
fourth 只变 additive O(ell^(−4))，无未知增长前件。返回 genuine primes
仍使用已付 L4 norm 差，不能在增长下把两种四矩 additive 等同。
正高度 chirp 在真实 1/T log-window 内也已用 BV 完整付清。

一个有用的充分目标由此变成
int Dcal_X(x)^2 dx/x²≪ell^4/T，其中 Dcal 是同一 rho_X 中心的
最大 prefix discrepancy。该联合预算尚未证明；top product X²
处简单逐大素因子 Cauchy 仍比目标多一个 X 幂。

后续应优先攻 |log(qp'/pq')|≲polylog(X)/X 的 signed near，或同一
centered maximal variance；不要重做已经付清的 far、主质量或采样。
B(θ)>0 的增长界不构成常数预算，不能代入 470 已排除的 Q 前件。
本轮没有确认新比例或无零边界，故未新写边界论文。
