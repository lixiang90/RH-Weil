# 原正高度 high-prime 四矩：零点包与密度给出的严格增长幂改进

2026-10-08。作者 radial。状态：完整推导待独立全文审查。
基线 46106dc；本稿只新增这个研究文件，不修改原论文、旧笔记或数学源。
在一个明确的 Riemann zeta 零自由条带输入下，得到原标量四矩的更强增长幂上界。
没有得到 O(1) 四矩、固定比例改善或新的零自由区域。

## 1. 同一原对象及来源

canonical UTF-8 LF 仅统一 CRLF/lone CR，不 trim 或改变 EOF。

| 已冻结完整输入 | SHA256 |
|---|---|
| [446 原有限矩阵的 strip 上界](../../notes/446-uniform-prime-twists-on-the-original-gabor-frame.md) | 08060477a6ea806d559fd67533d9e6d3b96483a755842cca9a048b6ab5e110cf |
| [451 原家族继续与边界](../../notes/451-kappa-feedback-cubic-boundary-and-family-continuation.md) | 17ce7fea8c881ebd4034657b7039e99897d4ff9532348993ba329c46e3c4d487 |
| [474 原 scalar 准入](../../notes/474-original-short-carrier-canonical-scalar-fourth-admission.md) | 37306c6d403f48c93d5d0f92782088225084e2e4b6b694cd89644a75fe39e99f |
| [474 的完整作者源](hybrid-short-carrier-canonical-scalar-fourth-admission-research-radial.md) | f04279a9de54303d772859b2ee5e05010567404c53143c928a14e905eb51a0d7 |

固定数学源仍是 OpenAI September-30 稿、commit
adc7f1241b42e322a6451854ab7e4b4c146bf78a，canonical LF SHA256
42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3。
本稿没有重新证明该源或 451 的完整无零合同。

令 X=T/(2π)、ℓ=log X，取 AF 原 even C² taper φ，
a_ℓ=||φ||₂²/ℓ，且 a_ℓ≥a₀>0。保留两个原 sharp cutoff：

\[
 P_H(t)=\frac1{a_\ell\ell}
       \sum_{\sqrt X<p\le X}\frac{\log p}{\sqrt p}p^{it},
 \qquad
 {\cal M}_T=\frac1T\int_{T/4}^{4T}|P_H(t)|^4\,dt.
 \tag{1}
\]

用相同 cutoff 定义

\[
 A_H(t)=\sum_{\sqrt X<n\le X}\Lambda(n)n^{-1/2+it},
 \qquad
 \widehat P_H=(a_\ell\ell)^{-1}A_H,\quad
 \widehat{\cal M}_T=T^{-1}\int_{T/4}^{4T}|\widehat P_H|^4.
 \tag{2}
\]

条带输入 [R_θ] 是：ζ 的每个非平凡零点 ρ=β+iγ 都满足 β≤θ，
其中固定 5/6<θ≤7/8。只使用这一条 Riemann ζ 输入；不把任意
Hecke family 的零密度当成同一个已证定理。原 7/8 或 451 的 θ_* 输入
可以分别代入，但各自保留原 [R] 范围。

结论是：对每个固定 ε>0，

\[
 \boxed{{\cal M}_T\ll_{\phi,\theta,\epsilon}T^{B(\theta)+\epsilon},
 \qquad
 B(\theta)=4\theta-3+\frac{3(1-\theta)}{3\theta-1}.}
 \tag{3}
\]

在 θ=7/8 时 B=19/26；原 446 的 2θ−1=3/4 比它大 1/52。
在 451 的 θ_*=0.874957019420098946… 下，B≈0.730694976215313，
而 2θ_*−1≈0.749914038840198。小数只是展示，证明使用式 (3)。

## 2. 普通 ζ 输入的精确外部范围

使用 ζ 的普通解析延拓、functional equation、Hadamard product，
以及以下两个经典性质：

\[
 \#\{\rho:\ |\gamma-v|\le1\}\ll\log(2+|v|),
 \tag{4}
\]
\[
 \frac{\zeta'}{\zeta}(\sigma+iv)
 =\sum_{|\gamma-v|<1}\frac1{\sigma+iv-\rho}
   +O(\log(2+|v|)),\quad -1\le\sigma\le2,\quad |v|\ge v_0,
 \tag{5}
\]

重数始终计入。式 (4)–(5) 可由 completed ζ 的 Hadamard logarithmic
derivative减去 σ=2 上的值证明；远零部分有
O(1/(1+|v−γ|²))，由 (4) 求和。公式中的 pole/gamma 项在大高度是
O(log|v|)。一个完整 primary 证明见
[Fesenko–Ricotta–Suzuki, Appendix A, Proposition A.1 及 (A.6)](https://www.numdam.org/article/AIF_2012__62_5_1819_0.pdf)。
本稿使用它们的 ζ 特例，不使用 mean-periodicity 结论。

零密度输入是

\[
 N(\sigma,H)\ll_{\sigma,\varepsilon}H^{n(\sigma)+\varepsilon},
 \quad
 n(\sigma)=
 \begin{cases}
 3(1-\sigma)/(2-\sigma),&1/2\le\sigma\le3/4,\\
 3(1-\sigma)/(3\sigma-1),&3/4\le\sigma<1.
 \end{cases}
 \tag{6}
\]

N 计 β≥σ、|γ|≤H 的所有重数。两段分别是 Ingham 和 Huxley；
[原研究论文 Guth–Maynard 的 (1.2)–(1.3)](https://arxiv.org/html/2405.20552v1)
明确记录这些公式和原出处。本稿引用的是 (6)，没有将该论文只在较短
Dirichlet polynomial 上的新 large-value 定理套到原长度 X² 的 Λ 卷积。
以下仅在先固定的有限 σ 网格使用 (6)，不需要未声明的 σ 随 T
变化一致常数。σ=1/2 处普通零点总数 O(H log H) 已足够。

## 3. 直接 twisted Perron：没有 Abel 的 t 费用

取 x=floor X+1/2、y=floor√X+1/2。这两个半整数给出 (2) 的原整数
集合，且与每个整数相距至少 1/2。令

\[
 s_0=\tfrac12-it,\quad c=\tfrac12+\ell^{-1},\quad
 D(s)=-\zeta'(s)/\zeta(s),\quad
 F_{x,y}(z)=\frac{x^z-y^z}{z},\quad F_{x,y}(0)=\log(x/y).
 \tag{7}
\]

F 是整个函数。把两个 prefix 在移线前合并是必要的：单独的 x^z/z
在 z=0 有核极点，直接跨越会出现 D(s₀)；(7) 没有这个伪额外项。
若 s₀ 本身是 ζ 的零点，真实 D-pole 仍存在，其留数是
−m_ρ F(0)，以下零点和确实包括它。

对每个 t∈[T/4,4T]，可选择 H_t∈[10T,11T]，使两横边的 ζ 高度
−t±H_t 与所有零点 ordinate 的距离至少 c₁/ℓ，c₁>0 为固定小常数。
证明：这些高度只涉及 |γ|≤16T；(4) 给 O(Tℓ) 个 ordinate。
删去 H 区间内每个条件对应的半径 c₁/ℓ 邻域，删去总长度至多
C c₁ T。先选 c₁ 使该长度小于 T，即有可选 H_t。无需 H_t 连续。

截断 Perron 直接对 n^{-1/2+it} 应用，得到

\[
 A_H(t)=\frac1{2\pi i}\int_{c-iH_t}^{c+iH_t}
             D(s_0+z)F_{x,y}(z)\,dz
       +O(X^{-1/2}\ell^2).
 \tag{8}
\]

这里没有先写 ψ(x) 再 Abel 分部积分。截断误差的系数模与 t 无关：
近 x 的项用 |log(x/n)|≳|x−n|/x 和 harmonic sum，
给 O(√x log²x/H_t)；n≤x/2 及 n≥2x 用
ΣΛ(n)n^{-1−1/ℓ}≪ℓ，连同 1/(H_t|log(x/n)|)，给相同或更小界。
y-prefix 同理。半整数距保证最靠近端点的项也在这个界内。

将 (8) 移至 Re z=−3/2，即 Re(s₀+z)=−1。ζ 在这条线上无零，
普通 functional equation 与 σ=2 上绝对收敛给

\[
 |D(-1+iv)|\ll\log(2+|v|).
\]

左边积分绝对值至多 C y^{-3/2}ℓ²=O(X^{-3/4}ℓ²)。
横边上由 (5) 和所选 ordinate 距得 |D|≪ℓ²，
而 |F|≪√X/H_t；两横边总费用 O(X^{-1/2}ℓ²)。
未跨越 −2,-4,… 的 trivial zeros。跨越的 ζ-pole s=1 和全部非平凡
zeros 给

\[
 A_H(t)=F_{x,y}(\tfrac12+it)
 -\!\!\sum_{\substack{\rho=\beta+i\gamma\\|\gamma+t|<H_t}}
        m_\rho F_{x,y}(\beta-\tfrac12+i(\gamma+t))
 +O(X^{-1/2}\ell^2).
 \tag{9}
\]

m_ρ 可以理解为对 distinct zeros 的重数；下文等价地逐重数求和。
ζ-pole 留数为正，zero 留数为负。原正高度窗内
|F(1/2+it)|≪√X/t≪X^{-1/2}。没有删掉一个靠近 t=0 的大 principal
项后假装全高度均小；(9) 此处只用于既定 t∈[T/4,4T]。

## 4. 保重数的零点包四矩上界

设 z=a+iv、−1/2<a<1/2。由

\[
 F_{x,y}(z)=\int_{\log y}^{\log x}e^{zu}\,du
\]

和分式表达式分别得 |F|≪ℓ X^{a_+} 与
|F|≪X^{a_+}/|v|。定义

\[
 k_\ell(v)=\frac{\ell}{1+\ell|v|},\qquad
 |F_{x,y}(a+iv)|\ll X^{a_+}k_\ell(v).
 \tag{10}
\]

这个界在 a=0,v=0 合法，不除以 β−1/2，也不假设零点彼此简单。
将 (9) 的实际 row-dependent 零点集合在取绝对值后扩大到
所有 |γ|≤16T；记 K_T(t)=Σ k_ℓ(t+γ)，逐重数计。由 (4)，

\[
 \sup_{t\in[T/4,4T]}K_T(t)\ll\ell^2,\qquad
 \int_{T/4}^{4T} k_\ell(t+\gamma)\,dt\ll\ell.
 \tag{11}
\]

第一界的 |t+γ|≤1 部分至多 O(ℓ) 个零点、每项至多 ℓ；
其余 unit bins 用 k≪1/|t+γ| 和 harmonic sum。第二界直接积分。

对 c_ρ=X^{(\beta−1/2)_+}，加权 Hölder 给

\[
 \left(\sum_\rho c_\rho k_\rho\right)^4
 \le\left(\sum_\rho k_\rho\right)^3
       \sum_\rho c_\rho^4k_\rho.
 \tag{12}
\]

于是 (9)–(12)，除以原 (a_ℓℓ)^4，严格得到

\[
 \boxed{\widehat{\cal M}_T
 \ll_\phi \frac{\ell^3}{T}
       \sum_{|\gamma|\le16T}X^{4(\beta-1/2)_+}
       +O(X^{-2}\ell^4).}
 \tag{13}
\]

这是 signed 原 polynomial 的上界；证明中零点包取了绝对值。
没有将该上界反向用作某个零点不能被其他零点包抵消的 detector。

## 5. 连续实部范围与 19/26

β≤1/2 的部分在 (13) 中至多 O(Tℓ)。对 β∈[1/2,θ]，先固定
网格宽 η>0，然后按 β-bin 使用 (6)。若 bin 左端为 σ，右端不超过
σ+η，则该 bin 对 (13) 的 T 指数至多

\[
 4\sigma-3+n(\sigma)+4\eta+\varepsilon_1.
 \tag{14}
\]

跨过 3/4 的 bin 单独拆开。θ-bin 可以取左端 θ−η；因此不要求
密度常数在靠近 θ 的 moving line 上一致。两个连续函数的导数为

\[
 \frac d{d\sigma}\left(4\sigma-3+
       \frac{3(1-\sigma)}{2-\sigma}\right)
 =4-\frac3{(2-\sigma)^2}>0,\quad 1/2\le\sigma\le3/4,
\]
\[
 \frac d{d\sigma}\left(4\sigma-3+
       \frac{3(1-\sigma)}{3\sigma-1}\right)
 =4-\frac6{(3\sigma-1)^2}>0,\quad 3/4\le\sigma\le\theta.
 \tag{15}
\]

两函数在 3/4 都为 3/5，第一函数在 1/2 为 0。
故全区最大值恰为 B(θ)。给定目标 ε，先选 η、ε₁ 足够小，
再取 T 大以吸收所有固定网格常数及 ℓ³，得到 (3) 的 Λ 版本。

原 474 的 proper-power 证明在同一窗给

\[
 \|P_H-\widehat P_H\|_{L^4(dt/T)}\ll_\phi X^{-1/12}.
 \tag{16}
\]

用 L⁴ norm 三角不等式传递 (3)；不在一个可能增长的四矩上直接
声称两矩差是 additive o(1)。最后比较恰为

\[
 (2\theta-1)-B(\theta)
 =\frac{(1-\theta)(6\theta-5)}{3\theta-1}>0,\quad
 5/6<\theta\le7/8.
 \tag{17}
\]

这说明相对 446 的弱界是真正严格的幂节省。未声称经典密度公式、
一般零点包方法或所得 exponent 在文献中首次出现。

## 6. 对原 ratio 的现有严格后果及限度

只用已冻结 474 的现有准入，令 s=T/√ℓ、m_T≪√X/ℓ。
它的有限公式为

\[
 \operatorname{avg}_\sigma r_\sigma+S_T/2
 \le A_T\left[N_\ell\sqrt{{\cal M}_T}
       +C_\phi(m_T/T){\cal M}_T^{1/4}
       +C_\phi m_T^2/T\right]^2+C_\phi/\ell,
 \quad A_T,N_\ell=O_\phi(1).
 \tag{18}
\]

代 (3) 可得 avg r_σ≪T^{B(θ)+ε}。保留 finite crossing terms：
例如首二项 cross 可以仍随 T 增长，因此这里仅将它们吸收到主幂，
没有全部改写为 additive o(1)。原 472 的共同 carrier 选点亦可给
一个同阶原 actual high 四阶增长界。此稿没有把 averaged r、
fixed-start r、band q_sq 和 full half-Gram ratio norm 相互认同；
未来独立 fixed-start sampling 证明若成立，才是额外新输入。

B(θ)>0，故式 (3) 不给 r=O(1)，更不付显式小 residual。
不能代入任何已被 470 排除的 Q 前件，也没有付款原惯性比例的
constant-size whole fourth budget。这里是实际 canonical 算术上界
的进展，而不是 scalar 准入的重新命名。

## 7. O(1) 目标能严格推出什么，哪些必要性尚未证明

假设原同一 (1) 的 M_T=O(1)。选择 C∞ frequency cutoff，等于 1 于
[ℓ/2,ℓ]，支撑于一个固定倍数的 ℓ 区间。其 kernel 为
K_ℓ(v)=ℓ e^{icℓv}K(ℓv)，K 为固定 Schwartz 函数，
||K_ℓ||_(4/3)≪ℓ^(1/4)。原 finite polynomial 精确满足
P_H=K_ℓ*P_H。对 t∈[T/2,3T]，把输入切到 J=[T/4,4T]；外部距离
至少 T/4，且全实轴粗界 |P_H|≤m_T。因此

\[
 \boxed{
 |P_H(t)|\ll_\phi (T\ell{\cal M}_T)^{1/4}
   +C_A m_T(T\ell)^{-A},\qquad T/2\le t\le3T.}
 \tag{19}
\]

这是可证明的 local Nikolskii 后果：bounded M 强迫原 high signal 的
内部高度尖峰不超过 O(T^(1/4)ℓ^(1/4))。它比单独条带给出的
T^(θ−1/2+ε) pointwise 界强，但没有自动证明 3/4 零自由。

原因是从 (9) 的一项 amplitude X^(β−1/2) 到原 polynomial 的
L⁴ 下界，需要真实 noncancellation detector。式 (12) 是上界，
不能反向。仅作尺度计算，若某个 γ≈−T 的 zero packet 可以在
固定小窗中单独检出，它的第四阶费用将涉及 X^(4β−3)（另带 log
因子）；3/4 就从这里出现。该检出假设本稿没有证明。

此外，对任意先固定的有限零点集合，t∈[T/4,4T] 时各项有
|F(β−1/2+i(t+γ))|≪_ρ X^{(β−1/2)_+}/T，其正规化贡献随 T 衰减。
因此不能从这一 diagonal length X≈height T 的渐近窗预算，借单个
固定低高度项就排除有限离线例外。这不是给 ζ 构造反例，而是指出
该推理缺少的量词及 cancellation 步骤。

当前严格结论是 (3)、(13)、(18)、(19)。bounded M 的可行性、它对
真实零点的更强必要密度条件，以及 O(1) signed Λ_H*Λ_H budget，
仍须另证。没有用经典 shorter-polynomial large values 偷换原顶块。
