# 450. 重证 lower-kappa plain moment 与真实 detector 容量

2026-10-07。状态 [T/R]。从固定源的底层输入重证其 generic plain lemma 至
37/50≤κ≤1，保留原实际角色、零延拓、素数槽、全部高度与 mesh 顺序。
这不是在原仅声明 κ≥3/4 的定理之外直接引用结论。
尚未由本笔记单独认证新的数值边界或新的简单临界线比例。

主推导和逐段源位置见[完整报告](../reviews/2026-10-07/hybrid-critical-count-witness-research.md)；
另一个作者从源全文重新核对的记录见
[独立审查](../reviews/2026-10-07/450-plain-kappa-extension-review-twisted.md)。
源仍为 OpenAI/math 的固定提交 adc7f1241b42e322a6451854ab7e4b4c146bf78a，
canonical LF SHA-256 为
42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3。
源仓库只读，已交付论文保持原版。

## 1. 准入命题与完整前件

使用原 rows q_k≪Z^m、原固定 τ 的 displayed moving residue factors 的
完整 radical 范围 Z^q，M=m+q。取消或六整除的 phase 仍保留自然零延拓；
额外 puncture 只能用同一个、原 polynomial-size fixed mask，不能随 varying row 改变。
原有限群 Θ、每个素数槽的固定 finite-ray coefficient expansion、disjoint
underlying supports、inducing-Θ exceptions、原 profiles 与 separated twists 均保留。

令 A=n_1+n_2+z，z 为全部 positive slot lengths 的和。
对 κ∈[37/50,1]，positive-slot 条件仍为
\[
 n_1+n_2+6\kappa z\le M,\qquad
 \beta_*\le(1+\kappa)/2\quad(\kappa<1).
\]
则相对原底层 [R] 有
\[
 \sum_{k\in\mathcal R_z}
 |S_{\psi_k}(n_1)S_{\psi_k}(n_2)Q_{\psi_k}|^2
 \ll Z^{M+\epsilon}.
\]
zero-slot case 保留原全部 bounded nonnegative plain lengths 和 nonprincipal
family。mesh 在固定长度范围和 ε 后、slot count 之前选择，
uniform 于上述 κ 区间及全部 moving moduli/masks/outer labels；
固定 slot data 后才选有限 seminorm/height 阶，后来的 external tail order 不改变这些阶。

## 2. 源全文中的数值依赖

源 12492–14974 的全证明按实际递归顺序重做。global prime contour 使用
s_κ=(1+κ)/2≥β_*，现在 s_κ≥87/100；无新 principal residue。
归一化 slots 的平方上界仍恰为 Z^(κz+ε)，其全高度因子由原 weighted
Fourier measure 支付。

terminal 原展示的 z≤2M/9 改为 z≤25M/111。真正付 terminal exponent 的
κz≤M/6 不变；前一个粗界没有在后面的 proof 被调用。

comparison 在 A>5M/6 时满足
\[
 (6\kappa-1)z\le M-A<M/6,\quad
 6\kappa-1\ge86/25,\quad z<25M/516<M/20 .
\]
由此原 A_comp≤23M/30+ξ 和
A_comp+(6κ−1)z≤14M/15+ξ 仍成立，原 M/15 margin 不变。
更精确的两个上界为 197M/258+ξ、40M/43+ξ。

two transforms、local F_2、whole-product support、原 Möbius indicators、
common characters、pool p^6、真实 child width decrease 与 exceptional
count 不含这一下限。child affine budget 只需 6κ−1≥0；
whole-slot greedy removal 的费用
κd_z≤F_act/6+κη≤F_act/6+η；
numerical Lipschitz 只需 0≤6κ−1≤5。所有这些条件在新范围成立。
原 padded zero-slot、先同带 uncentered 后 centered、先全部 zero-slot 后
positive-slot、finite depth 和 strict drop σ/2 保留。

有限代数脚本不证明这条无限分析归纳；完整源依赖与两位作者的全文核对分列记录。

## 3. 由新 lemma 得到的 actual crossing

取 δ=2a−1∈[1/50,3/4]，q 为原全部槽的加权 mean amplitude，
x=q/δ∈[0,1/2]，α=5/6，c=1/(3κ)。定义
\[
 D_\kappa=3-(1+2c)x,\quad
 P_\kappa=(2-2cx)(1-x),\quad
 J_\kappa=(\alpha-\delta)D_\kappa+\delta P_\kappa .
\]
两份同一个 plain witness 的四次 spike 必须保留。真实 inverse/plain counts 为
\[
 A_I(r)=1-\delta[x+(1-x)r],\qquad
 S_t(r)=1-\delta[cx+(2-2cx)(t-r)] .
\]
其 crossing、adaptive detector 和最终行数指数为
\[
 r_*=\frac{(2-2cx)t-(1-c)x}{D_\kappa},\quad
 t_\kappa=1+\frac{\delta P_\kappa}{2J_\kappa},\quad
 R_{*,\kappa}=1-\delta+
 \frac{(\alpha-\delta)\delta P_\kappa}{2J_\kappa}.
\]
这里使用同一个 character/presentation、原 mask、原 physical slot coefficients
和原 witness heights；不将两个不同高度假定为同一 phase。

可保守使用 D≥2、P≥3/4、J≥35/48、1<t<3/2、r_*≥3/5、
1/3≤t−r_*≤1/2。因此 inverse z_M≤1/5，plain
z_P≤1/(18κ)≤25/333<1/5，供给只需 ell/d>1/5 的严格 margin。
请求 z≤z_M−ν_0 或 z≤z_P−ν_0，分别保持
\[
 1-r-2z\ge2\nu_0,\quad
 3-2r-8z\ge8\nu_0+1/5-o(1),\quad
 1-2m-6\kappa z\ge6\kappa\nu_0 .
\]
zero capacities、r≥1、m≥1/2 仍走原 no-slot cases；whole-slot rounding、
uniform mesh、inducing exceptions、群组合及 cumulative T_1/2 allowance 全部保留。

## 4. 下一边界中的反馈

κ较低给真实更强的 count，但不能在反证 β_*>σ_* 中调用
κ_*=2σ_*−1 的 positive-slot lemma。实际调用必须取
κ_act=2β_*−1，使用其满足的 β_*=(1+κ_act)/2 前件。
纯代数微分给
\[
 0\le\partial_\kappa R_{*,\kappa}
 =\frac{(\alpha-\delta)^2\delta x(1-x)^2}
 {3\kappa^2J_\kappa^2}
 \le\frac{625}{36963}<\frac1{50}.
\]
故 κ_act−κ_*=2Δ 的 count 费用小于 Δ/25（h<1）；
同源 C_b(β_*) 比 C_b(σ_*) 增加 Δ，仍留下至少 24Δ/25。
完整连续参数证书和全部 family continuation 另见
[451](451-kappa-feedback-cubic-boundary-and-family-continuation.md)。
