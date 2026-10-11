# 523. 自然Hilbert完成的源商退化与独立增长缺口

2026-10-11。[T/N] 接续[519](519-f1-closed-source-image-and-degree-moments.md)的实际闭源像、
[520](520-f1-source-quotient-spectrum-and-centered-growth.md)的完整Fréchet商，以及
[522](522-f1-optimal-centered-growth-and-rh-equivalence.md)的增长比较。
证明每个单一实指数权Hilbert完成都会把实际源商压成零。
这限制指定的自然完成，不排除其他具有独立算术结构的Hilbert实现。

## 1. 保持实际源像及原拓扑

沿用复化的
\[
 F=\mathcal S_{\exp,\mathbb C},\qquad
 I=E\mathscr S_{e,0,\mathbb C}=\mathcal R_{\rm jet,\mathbb C},
 \qquad X=F/I.
\]
519已证明I在F的全部指数半范数拓扑中闭；520在X中保留全部真实零点和重数。
取405原来的实际非零源
\[
 h_0=E\theta_0\in I,\qquad
 H_0(s)=M_{h_0}(s)=\xi_{\rm Riemann}(s)/2.
\]
H0整且不恒零。I在全部平移
\((\tau_a f)(t)=f(t-a)\)下不变，所以含h0的全部平移。
这里不更换来源、源准入或关系空间。

## 2. 每个单一实指数权中实际源像稠密

对任意固定实数σ，令
\[
 H_\sigma=L^2(\mathbb R,e^{2\sigma t}\,dt),\qquad
 U_\sigma f(t)=e^{\sigma t}f(t).
\]
Uσ是到普通L²(dt)的酉同构；F连续嵌入Hσ，且因含紧支光滑函数而稠密。
特别是h0属于Hσ。

有准确恒等式
\[
 U_\sigma\tau_a h_0
    =e^{\sigma a}\tau_a(U_\sigma h_0).
\]
所以实际I的Hilbert闭包包含Uσh0的全部普通平移所张成的空间。
设v∈L²(dt)正交于这些平移。取Fourier变换
\(\widehat g(T)=\int e^{-iTt}g(t)\,dt\)，Plancherel给
\[
 \int_{\mathbb R}
   \widehat v(T)\,
   \overline{\widehat{U_\sigma h_0}(T)}e^{iaT}\,dT=0,
                                      \qquad a\in\mathbb R.
\]
该乘积由Cauchy–Schwarz属于L¹，所以Fourier唯一性适用，得到
\[
 \widehat v(T)\,\overline{H_0(\sigma-iT)}=0
                                      \quad\text{a.e.}
\]
H0的零点在整个复平面局部有限，因而固定竖线上的零集离散、测度为零。
于是 \(\widehat v=0\) 几乎处处，v=0。这证明
\[
 \boxed{\ \overline I^{\,H_\sigma}=H_\sigma
                                      \quad(\sigma\in\mathbb R).\ }       \tag{1}
\]
没有使用RH、简单性或零点间距。

因此指定Hilbert完成的商是零空间，
\[
 H_\sigma/\overline I^{\,H_\sigma}=0,\qquad
 \inf_{\theta\in\mathscr S_{e,0,\mathbb C}}
                 \|f-E\theta\|_{H_\sigma}=0\quad(f\in F).                \tag{2}
\]
实际源确实足以任意逼近一个固定Hilbert范数；这没有控制逼近源在其他指数半范数中的代价。

## 3. 固定阶单线Sobolev完成也有同一退化

这一结论可加有限个导数，范围仍限于同一个σ。
对固定整数k≥0，令
\[
 \|f\|_{\sigma,k}^2
   =\sum_{j=0}^k\|D^j(U_\sigma f)\|_{L^2(dt)}^2.
\]
其完成由Uσ识别为普通Sobolev空间Hᵏ(R)，Fourier权是
\(w_k(T)=\sum_{j=0}^kT^{2j}>0\)。

若v∈Hᵏ正交于Uσh0的全部平移，
\[
 w_k(T)\widehat v(T)\overline{H_0(\sigma-iT)}
\]
同样由加权Cauchy–Schwarz属于L¹，且其Fourier变换恒为零。
H0竖线上的零集仍测度为零，故v=0。
所以I在每个这样的固定阶单线Sobolev完成中也稠密。
这里没有加入其他实部的指数权，也没有声称任意物理坐标多项式权的完成具有同一性质。

## 4. 中心化酉性存在，但自然商没有谱

520的中心化群为 \(V_a=e^{-a/2}\tau_a\)。
直接换元得到
\[
 \|V_a f\|_{H_\sigma}
       =e^{(\sigma-1/2)a}\|f\|_{H_\sigma}.
\]
在σ=1/2时，V_a本来就是酉群；在上述同一单线Sobolev完成中也酉。
可是(1)–(2)使其完成后的源商为零。它不能成为520非零商X的忠实Hilbert实现。

源自身的中心化伸缩在L²(dr)上也可酉化，但E识别的是子空间I，
而需要研究的是余核X；源空间上的酉性不提供余核上的正定范数。
这个指定模型的失败已有准确原因，而不是尚待选择一个归一化常数。

520另证：任何忠实正定Hilbert酉化都会同时排除离线零点和非平凡Jordan块，
因此还会迫使全部简单零点，强于RH本身。这里的自然完成甚至更早退化为零；
两种障碍的适用对象不同。

## 5. 零点jets为什么不能连续延拓到单线Hilbert空间

对任意非平凡零点ρ，Mellin求值
\[
 L_\rho(f)=M_f(\rho)=\int_{\mathbb R}e^{\rho t}f(t)\,dt
\]
在F连续、在I上为零，且不恒为零。它不能连续延拓到任意Hσ。
一方面，若能延拓，(1)会迫使其恒为零，矛盾。

也可直接由Riesz表示核验。在Uσ坐标中，若该求值有L²连续延拓，
其Riesz核在紧支光滑测试上必须等于
\(e^{(\overline\rho-\sigma)t}\)。但
\[
 \int_{\mathbb R}e^{2(\Re\rho-\sigma)t}\,dt=\infty
\]
对每个σ都成立：实部差非零时一端发散，差为零时核为常数。
因此没有这样的L²核。
完整导数求值
\[
 M_f^{(j)}(\rho)=\int t^j e^{\rho t}f(t)\,dt
\]
的核多一个多项式因子，仍不属于L²；也不能连续延拓。

不能因此把结论扩到所有指数权的交空间。原F拓扑同时控制两端，正使这些求值连续。
甚至有限的**双端**指数权已经不同：若N>|Reρ|，在
\[
 H_N^{\rm two}
  =L^2\!\left(\mathbb R,(e^{2Nt}+e^{-2Nt})\,dt\right)
\]
中Cauchy–Schwarz用
\[
 \int_{\mathbb R}
  \frac{e^{2\Re\rho\,t}}{e^{2Nt}+e^{-2Nt}}\,dt<\infty
\]
给连续Mellin求值。I在这个空间中便不稠密，因为该非零连续求值杀掉I。
所以(1)是每个单线完成的结论，不是多个实指数权交空间的结论。

## 6. 剩余合同是统一的实际源修正代价

[522式(17)](522-f1-optimal-centered-growth-and-rh-equivalence.md)已给520(8)的实际源修正版本及等价证明。
其量词要求：对每个输出指数半范数序号n及每个ε>0，
存在一个有限输入半范数P_m和常数C，对所有a、f都能选取合法实际源，
把中心化平移后的误差控制在 \(C e^{\epsilon|a|}P_m(f)\) 内。
源可依赖n、ε、a、f，但m、C不能逐a或逐f选择。

(2)只付清一个Hilbert误差可以任意小；这个增长合同还要求控制
其他指数权和导数中的代价。单线密度不能提供这种统一控制。
[521](521-f1-moving-source-correction-and-uniform-resolvent.md)的移动实际源已消除Gaussian校准的Gamma指数损失；
[522](522-f1-optimal-centered-growth-and-rh-equivalence.md)比较完整商群增长与实际零点带宽。
这些比较没有独立缩窄零点带宽，中心化次指数控制仍须新的算术输入。

几何principal、真实对应复合、全局HH链、截面／RR与完整Weil符号仍开放。
分析源闭像和某个完成中的稠密性，都不能代替这些来源比较。
