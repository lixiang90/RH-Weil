# 全导子 reciprocal 与同一 Gabor 四次迹：实际接口及指数障碍

日期：2026-10-07。推导人：progress_audit。

本文给出一项算术接口，未得到新的零点比例。假定外部全Hecke/Dirichlet7/8定理及确切来源的增长、显式公式和AF二矩结果 [R]，则规范纯norm-twist的高度成本可降到对数/任意小幂；这能进入原AF有限矩阵的算子范数，给实际中心四次迹的弱上界Oε(T^(3/4+ε)) [T/R]。它仍随T增长，远弱于改善比例所需的固定常数上界。长度T²、短差T的signed response相关和没有因此闭合。

## 1. 绑定来源与计数范围

只读主源：

- [OpenAI September-30 paper.tex，固定提交adc7f1241b42e322a6451854ab7e4b4c146bf78a](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)。本地E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex，canonical LF SHA256为42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3。
- [实际Nonvanishing Lean源码](https://raw.githubusercontent.com/openai/math/main/lean/OAI/NumberTheory/DirichletL/Nonvanishing.lean)，2026-10-07再读；theorem覆盖所有正模数及Dirichlet角色的Re s>7/8，principal pole另除。本文未重建Lean，也不把后续应用自动算成形式化。
- [原formalization scope](https://raw.githubusercontent.com/openai/math/main/lean/docs/003.md)，再次核对全导子Dirichlet、固定F=Q(√−3)的有限阶Hecke范围。
- [Alpöge–Furman，arXiv:2608.13637v2](https://arxiv.org/html/2608.13637v2)，2026-10-07再读§2、Prop5.2/5.4、Thm5.7及§7.2。原算术核心给同一有限Gabor矩阵的二次迹；长素数offdiagonal和更高矩需要额外信息。
- [Lamzouri，arXiv:2609.02882v2](https://arxiv.org/html/2609.02882v2)，只交叉核计数/二矩路线，本文未以其有限Hilbert不等式冒充四矩算术定理。

本项目旧稿只读绑定：

| 文件 | canonical LF SHA256 |
|---|---|
| notes/197-partial-weil-proportions-regions-four-moments.md | 98bd8ea89679030e0ffb8135d324b5654900f260b3f45c9ae816d5ea870eaae7 |
| notes/198-quadratic-fourth-moment-vaughan-channel.md | d7d2d9a20e9c6437b55bb23e8494f2a969b1b1ba46d63b70fadd7d42de904e66 |
| notes/305-post-6725-literature-baseline-audit.md | fab0841ee5734d35db023f0b1305bf75f9b19fcd11feda2ff08c73b2562d1aa9 |

197的四矩比例及198的三通道Gram均保留其完整误差/惯性前提。本文的N是零点计重数的N(T,2T)，讨论的比例目标为简单且在线的N0^s/N，不与distinct、全部simple或在线计重数混淆。305的67.3399%是待审比较标尺，不因本文使用其四矩门槛而得到认证。

## 2. 全导子输入真正给出的统一控制

令θ=7/8，取固定

\[
 0<\delta<(1-\theta)/4,\qquad a=\theta+\delta<1.
 \tag{1}
\]

δ在Q、T、长度和twist之前固定，不取δ=1/log T。假定所涉primitive有限阶角色的L函数在Re s>θ无零。源 lem:logarithmic-control，1531–1600，以以下确切输入证明：

1. 在2+it附近，Euler logarithm一致有界。
2. 固定宽real strip内的functional-equation增长是analytic conductor的固定幂。
3. 以2+it为中心的disk全部落在Re s>θ后，存在同一Euler分支的holomorphic logarithm。
4. Borel–Carathéodory、three-circles和Cauchy的disk余量是固定δ的倍数。

因此对primitive非principal角色，源1540–1548给

\[
 |L(a+it,\psi)|+|L(a+it,\psi)^{-1}|
 \ll_{\delta,\epsilon}\{Q(3+|t|)^2\}^{\epsilon},
 \tag{2}
\]

\[
 |L'/L(a+it,\psi)|
 \ll_\delta\log\{2Q(3+|t|)^2\}.
 \tag{3}
\]

这些常数独立于Q、角色及t；δ、ε、固定域/degree可影响它们。F为固定虚二次域；Dirichlet版本使用同一disk证明与标准degree-one functional-equation strip growth [R]。这不是从某一个χ的无零结论偷换成全导子常数。

principal时对(s−1)ζ_F(s)/(s+1)或对应ζ的regularization应用证明；(2)中的reciprocal仍传到1/ζ。原ζ'/ζ在s=1有极点，不能在整个右半平面声称(3)而不除pole。在固定线Re s=a<1上，距pole至少1−a，所以(3)加一个固定常数成立。之后的Perron移线将principal pole显式取留数。

对于原imprimitive presentation，

\[
 L_{\rm orig}(s,\psi)=L(s,\psi^*)
       \prod_{\mathfrak p\in R}(1-\psi^*(\mathfrak p)N\mathfrak p^{-s}),
 \tag{4}
\]

源 lem:deleted-euler-factors，1602–1620，给reciprocal额外(NR)^ε和logarithmic derivative额外O(log(2NR))。故用

\[
 Q_{\rm eff}=Q_{\psi^*}\,NR
 \tag{5}
\]

统一记录，不只保留primitive conductor。原物理行源4244–4257有Qψ≪q_u、NR≪_S q_u；这一账本保留原零延拓，并未加入独立mask。若Q_eff在T的固定多项式范围内，任意小幂可吸收成T^ε；若Q_eff任意大，则必须把它留在估计中。

纯norm twist不是新的finite-order角色。它仅把原L-argument移为s−iτ，实部不变；(2)(3)已对所有高度统一。因此τ∼T完全合法，代价是任意小幂或log(Q_eff T)，没有必然的T^A固定多项式损失。

## 3. 规范Möbius与素数块的实际新接口

设W∈C_c^∞((c,C))，0<c<C固定，使用源Mellin convention

\[
 \mathcal MW(s)=\int_0^\infty W(y)y^s\,dy/y.
\]

规范inverse块是

\[
 \mathcal M_\psi(N,\tau;W)
 =N^{-1/2}\sum_{\mathfrak n}
       \mu(\mathfrak n)\psi_{\rm orig}(\mathfrak n)
       W((\mathrm N\mathfrak n)/N)((\mathrm N\mathfrak n)/N)^{i\tau}.
 \tag{6}
\]

这里ψ_orig的自然zero extension和全部声明的R必须保留。它的Dirichlet series恰为1/L_orig，而不是任意系数多项式。Mellin inversion与整体移线至a给

\[
 \mathcal M_\psi
 =\frac{N^{-1/2-i\tau}}{2\pi i}
  \int_{(a)}\mathcal MW(s)N^s
            L_{\rm orig}(s-i\tau,\psi)^{-1}\,ds.
 \tag{7}
\]

所有高度上都无零，故不需将|τ|限制在原buffered bin。固定W的Mellin变换在任何固定real strip任意阶衰减；水平joins由同一固定gap及全高度(2)趋零。由于

\[
 (3+|t-\tau|)^{2\epsilon}
 \le (3+|\tau|)^{2\epsilon}(1+|t|)^{2\epsilon},
\]

由(7)严格得到

\[
 \boxed{|\mathcal M_\psi(N,\tau;W)|
 \ll_{\delta,\epsilon,W}
 N^{a-1/2}\{Q_{\rm eff}(3+|\tau|)^2\}^{\epsilon}.}
 \tag{8}
\]

高度增长可任意小；固定profile加normalized logarithmic derivatives也保留此性质。若要共同Fourier分离，只要其共同coefficient measure有相应(1+|t|)^(2ε)加权L1 seminorm，即可用Minkowski传递，不自动容许任意row-dependent profile。

对应规范Λ块

\[
 \mathcal P_\psi(N,\tau;W)
 =N^{-1/2}\sum_{\mathfrak n}
 \Lambda_F(\mathfrak n)\psi_{\rm orig}(\mathfrak n)
 W((\mathrm N\mathfrak n)/N)((\mathrm N\mathfrak n)/N)^{i\tau}
 \tag{9}
\]

使用Dψ(s)=−L_orig'/L_orig(s)，由(3)得到

\[
 \boxed{\mathcal P_\psi
 =\mathbf1_{\rm principal}
       N^{1/2}\mathcal MW(1+i\tau)
 +O_{\delta,W}\!\left(
 N^{a-1/2}\log\{2Q_{\rm eff}(3+|\tau|)\}\right).}
 \tag{10}
\]

principal的留数是N MW(1+iτ)，规范化后成为(10)的第一项；τ≈0时它确为O(√N)，不能删除。τ∼T且W固定时，该项以任意幂衰减。imprimitive principal的有限Euler删除只改变Dψ的analytic部分，不改变s=1的留数。

式(8)(10)是比原“固定多项式norm-twist height成本”更精确的点态接口：在N、Q_eff为T的多项式范围且|τ|∼T时，规范normalized块为N^(3/8+δ)乘任意小幂/log。它可用于保留这些规范系数的Vaughan块，但没有证明相应完整response Gram的均值。

若需无Λ的canonical prime annular sum，可将固定profile除以log(Ny)，再绝对删除高次prime powers；这些贡献至多O(N^1/2 log N)，规范化后小于N^(a−1/2)的主误差尺度。固定finite-ray角色系数的有限和也可逐项用(10)。一般有界a(p)不具有Dψ生成函数，不由此接口覆盖。

## 4. 原sharp素数前缀：principal主项和uniform Perron证明

为进入AF的原矩阵，不能把其sharp n≤X擅自换成新的smooth prime model。令

\[
 Q_X(\tau)=\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}n^{i\tau}.
 \tag{11}
\]

它是AF原P_X(τ)=−π^−1 Re Q_X(τ)。以下保留原Λ权重和前缀。

取x=⌊X⌋+1/2，c=1/2+1/log x，Y=(2x(3+|τ|))^4。截断Perron使用

\[
 \frac{1}{2\pi i}\int_{c-iY}^{c+iY}
       D(s+1/2-i\tau)\frac{x^s}{s}\,ds,
 \qquad D=-\zeta'/\zeta.
 \tag{12}
\]

系数的模为Λ(n)/√n，与τ无关。x距每个整数至少1/2，所以标准Perron截断核的误差可按近x与远x两段直接估计：

\[
 \sum_n\frac{\Lambda(n)}{\sqrt n}(x/n)^c
       \min\left(1,\frac1{Y|\log(x/n)|}\right)
 \ll \frac{\sqrt x\,\log^2(2x)}Y
\]

（远段使用绝对Euler series，近段用Λ(n)≤log n和harmonic sum）。无未控制的endpoint原子；x替换X只改变主项一个O(X^−1/2)量。

把(12)移到Re s=a−1/2>0。s=0留在左边；唯一经过的pole是s=1/2+iτ，其留数为

\[
 \frac{x^{1/2+i\tau}}{1/2+i\tau}.
 \tag{13}
\]

Y>|τ|+2，故水平joins远离此pole；(3)在离pole固定距离的real rectangle上一致给D(s+1/2−iτ)≪log(2x(3+|τ|))。水平积分为O(√x log(2x(3+|τ|))/Y)。左线的1/s只产生log Y，故

\[
 \boxed{
 Q_X(\tau)=\frac{x^{1/2+i\tau}}{1/2+i\tau}
 +O_\delta\!\left(X^{a-1/2}
                    \log^2(2X(3+|\tau|))\right).
 }
 \tag{14}
\]

同样证明对primitive nonprincipal Dirichletχ给无principal主项的版本，log中记录其conductor；imprimitive删除按§2保留。对ζ已足够支付下一节。常数对全部τ统一，δ固定。尤其

\[
 |Q_X(\tau)|\ll_\delta
 X^{a-1/2}\log^2(2XT)+\sqrt X/T
 \quad(T/2\le\tau\le3T).
 \tag{15}
\]

在τ≈0必须使用(13)或原绝对界O(√X)；不能把(15)套到frame的所有高度或任意u差。

## 5. 接入原有限Gabor矩阵，而非新的bulk model

本节只讨论AF的固定原窗：L=log(T/(2π))、X=e^L∼T，φ为其原smooth taper，support长度L、0≤φ≤1、||φ″||1≪1，a_L=||φ||2²/L最终离零。α_k=T+2πk/L，0≤k<d，d∼TL∼N。

令

\[
 f_k(\tau)=\widehat\phi(\tau-\alpha_k),\quad
 (Uz)(\tau)=\sum_{k=0}^{d-1}z_k f_k(\tau),\quad
 V=\frac1{a_LL^2}U^*M_{P_X}U.
 \tag{16}
\]

这正是原显式公式中prime channel。τ为AF(2.11)的绝对高度，不能将它认成四词分离后的时间差u。真实Λ(n)/√n及sharp cutoff均未改变。

### 5.1 Bessel界与高绝对高度部分

Plancherel、φ的support及原grid的正交性直接给

\[
 \|Uz\|_2^2
 =2\pi\int|\phi(u)|^2
       \left|\sum_kz_ke^{i\alpha_ku}\right|^2du
 \le2\pi L\|z\|_2^2.
 \tag{17}
\]

令J=[T/2,3T]。只在J上使用(15)，于是

\[
 \|V_J\|_{\rm op}
 \le\frac{2\pi}{a_LL}\sup_{\tau\in J}|P_X(\tau)|
 \ll_\delta
 \frac{X^{a-1/2}\log^2(2XT)+\sqrt X/T}{L}.
 \tag{18}
\]

(17)是同一个finite frame的界；没有逐项假定所有响应的norm twist都在T附近。

### 5.2 低高度和外侧尾的完整费用

J外仍有τ≈0的principal主项。对每个α_k∈[T,2T)，其到J外的距离至少T/2。原二阶傅里叶尾给

\[
 |\widehat\phi(r)|\ll(1+|r|)^{-2}
 \quad (|r|\ge T/2),
\]

常数对L统一。因为d∼TL，

\[
 \operatorname{Tr}(U^*\mathbf1_{J^c}U)
 =\sum_k\int_{J^c}|f_k(\tau)|^2d\tau
 \ll dT^{-3}\ll L/T^2.
 \tag{19}
\]

这个矩阵为positive，因此其operatornorm不超过其trace。全高度的原绝对prime bound为|P_X(τ)|≪√X；不要求其在τ≈0有相消。故

\[
 \boxed{\|V_{J^c}\|_{\rm op}
       \ll\frac{\sqrt X}{LT^2}.}
 \tag{20}
\]

这一项付清了(15)在低高度不能用的问题。它不是原zero cutoff tail的改进，而是实际prime multiplication压缩的时间localization。

合并X∼T，

\[
 \|V\|_{\rm op}
 \ll_\delta T^{3/8+\delta}\log T.
 \tag{21}
\]

### 5.3 原背景与完整中心四次迹的弱上界

原μ(τ)≪log(2+|τ|)，在J内为O(L)。由(17)其压缩op为O(1)；J外按(19)加入log权重，积分为O(d log T/T^3)，同样可控。原pole termΠ_X在J内为O(√X/T)，外侧保留O(√X)并用(19)。故Gamma/pole压缩减I_d后的背景A满足

\[
 \|A\|_{\rm op}=O(1).
 \tag{22}
\]

该结论直接针对原integral formula；不需改到translation-invariant背景后再忽略finite crossing。

AF原等式为G+E=A+I_d+V。只调用其原zero tail结果||E||1=o(1) [R]；本节没有再次研究padding。由(21)(22)得

\[
 \|G-I_d\|_{\rm op}
 \ll_\delta 1+T^{3/8+\delta}\log T.
 \tag{23}
\]

AF原trace、dimension和二次迹输入给

\[
 \|G-I_d\|_{\rm HS}^2=O(N).
 \tag{24}
\]

G−I_d为Hermitian，无需将signed四词拆开取绝对值。谱上λ^4≤||G−I_d||op² λ²，故

\[
 \boxed{\frac1N\operatorname{Tr}(G-I_d)^4
 \ll_\delta T^{3/4+2\delta}\log^2 T
 \ll_\epsilon T^{3/4+\epsilon}.}
 \tag{25}
\]

这是同一个实际有限压缩的四次迹弱界 [T/R]。没有将τ∼T误当成每个cycle的u差；低时间主项已经以(20)支付。相较直接绝对prime前缀导致的T^1量级，它有power改善；它不能提供比例所需的固定四矩常数，不能冒称MOM-1完成。对moving Dirichlet moduli，AF的二矩/背景常数另需uniform证明；本文不把(25)声称为所有moving q矩阵的一致定理。

更一般的固定无零θ>1/2给相同方法的T^(2θ−1+ε)弱界。即使θ逼近1/2，此接口也没有计算四矩常数及signed mixed corrections。

## 6. 真正短差尺度：Mellin宽度与精确指数阈值

为量化剩余差距，先研究真正可由D(s)^r控制的规范单变量系数，而不替换实际truncated double-prime coefficients。

令X≥2、1≤H≤X/2、η=H/X，固定w∈C_c^∞((-1,1))，

\[
 W_\eta(y)=w((y-1)/\eta).
\]

对固定real partσ，Mellin变换满足

\[
 |\mathcal MW_\eta(\sigma+it)|
 \ll_{A,w,\sigma}\eta(1+\eta|t|)^{-A}.
 \tag{26}
\]

证明是在y=1+ηu后，以u积分分部：phase t log(1+ηu)的导数与ηt同阶，全部系数在固定annulus内有界。于是

\[
 \int_{\mathbb R}|\mathcal MW_\eta(a+it)|
        \log^r\{2Q_{\rm eff}(3+|t-\tau|)\}\,dt
 \ll \log^r\{2Q_{\rm eff}(3+|\tau|+X/H)\}.
 \tag{27}
\]

关键是amplitude η与Mellin频宽η^−1恰好抵消；不会免费留下一个H/X的saving。

令b_1(n)=Λ(n)，b_2(n)=(Λ*Λ)(n)，其生成函数为D(s)、D(s)^2。对χ的规范完全乘性twist同理。Mellin移线至a给nonprincipal sum

\[
 \boxed{
 \sum_n b_r(n)\chi(n)
        w((n-X)/H)(n/X)^{i\tau}
 \ll_{\delta,w} X^a
        \log^r\{2Q_{\rm eff}(3+|\tau|+X/H)\},
 \quad r=1,2.
 }
 \tag{28}
\]

principal另加真实pole residue。对ζ、r=2，D(s)=1/(s−1)−γ+O(s−1)，所以该主项准确为

\[
 \int_0^\infty w((x-X)/H)(x/X)^{i\tau}
                         (\log x-2\gamma)\,dx.
 \tag{29}
\]

r=1的principal main为不含(log x−2γ)的相同积分。imprimitive principal用相应Dχ0的Laurent常数；finite Euler deletion不改变r=1留数或r=2最高阶pole。

在τ=0时，窗口主规模为H（r=2另有log X）。要由(28)得到o(H)的power控制，此移线接口要求

\[
 H=X^\xi,\qquad \xi>\theta
 \tag{30}
\]

（选固定δ<ξ−θ，再吸收logs）。这是该具体接口的充分指数阈值，不是“任何可能从无零区证明相关和的办法都不可能”的no-go。

同一μ reciprocal窗口用(2)得到X^a乘(Q_eff(3+|τ|+X/H))^ε的版本；全导子和high twists只影响任意小幂。它也没有H/X的额外saving。

### 6.1 长度T²、差长T

四次prime词中两个prime products的有效长度X∼T²。时间长T的核对log(m/n)在1/T尺度响应，故近共振差长H∼X/T∼T。此时(28)的误差规模为

\[
 X^{7/8+\delta}=T^{7/4+2\delta},
 \quad
 \frac{X^{7/8+\delta}}H=T^{3/4+2\delta}.
 \tag{31}
\]

给coefficients除以√X后，目标局部主规模H/√X∼1，而误差仍为T^(3/4+2δ)。这正是所见power障碍的同一指数。

对于一般θ，X=T²、H=T要求2θ<1才能由此接口得到power-small误差。θ=1/2处也只是临界，logs与实际correlation仍须另外处理。7/8→69999/80000的微小边界改进只将3/4指数微降，不把它变成常数级signed budget。

### 6.2 long-prime offdiagonal

若希望在bandwidth上取X=T^b、b>1，实际prime二矩的近共振长度为H=X/T=T^(b−1)。同样移线误差相对H为

\[
 T\,X^{\theta+\delta-1}
 =T^{1-b(1-\theta-\delta)}.
 \tag{32}
\]

要由此单变量接口取得power saving，需要b(1−θ)>1；7/8时为b>8，δ还要进一步取小。它不能处理b仅略大于1的目标区间。原AF Prop5.4的O(L²X) offdiagonal仍需要实际双变量相消，不因已知全部χ的fixed zero-free half-plane就自动变成o(TL³)。

## 7. 全导子怎样进入加性相位，以及其费用

这是比“两个结果独立”更具体的一项transfer。对(a,q)=1，在单位群上的函数e(an/q)可按全部Dirichlet角色展开

\[
 e(an/q)=\sum_{\chi\bmod q}c_\chi\chi(n),\quad(n,q)=1,
 \qquad \sum_\chi|c_\chi|^2=1.
 \tag{33}
\]

由有限群Parseval和Cauchy，

\[
 \sum_\chi|c_\chi|\le\sqrt{\varphi(q)}.
 \tag{34}
\]

因此(28)给规范coprime Λ或Λ*Λ短窗的additive estimate：principal main乘cχ0，加

\[
 O\!\left(\sqrt{\varphi(q)}\,X^a
      \log^r\{2q(3+|\tau|+X/H)\}\right).
 \tag{35}
\]

q可随T增长，因为全部χ的(3)常数统一；imprimitive导子/删除radical按§2记录。这确实使用了全导子，而不是只知道ζ的7/8。代价√φ(q)必须保留；q=1时(31)已经过大，all-conductor不会免费带来modulus-averaged相消。若用素数和去掉(n,q)=1，nonunit prime-power项还要单独付，不能将zero extension静默删除。

式(35)是one-point exponential sum接口。把它放进circle/dispersion decomposition后，是否可利用q、h和response之间的相消，是新的多变量算术任务；本文没有证明它给实际fourth response Gram足够强的均值。

## 8. 为什么canonical marked moments不能充当四迹

实际Q_T的平方系数是

\[
 C_{2,T}(m)=\frac1{\sqrt m}
       \sum_{\substack{ab=m\\a,b\le T}}
       \Lambda(a)\Lambda(b)
\]

并带原taper/response权重。m∼T²时的双因子截断不能从生成函数D(s)^2中删掉。完整Λ*Λ短窗的(28)甚至还没有证明这个截断系数的同样界，更没有证明

\[
 \sum_{0<|h|\lesssim T}\sum_{m\asymp T^2}
 C_{2,T}(m)\overline{C_{2,T}(m+h)}
 \,\mathcal K_T(m,h)
\]

的signed response总和。真实Gabor四迹的kernel、背景与3+1/4+0 mixed words须同时保留，不能只控制这一诊断性的2+2项。

源 marked inverse moment，9220–9268，必须保留μ(n)ψ_u(n)、原row zero extension及统一common角色；允许的prime-slot bounded coefficients独立于row，slots须disjoint，长度还要求r+2z≤m−c1、2r+8z≤3m−c2。它不是任意a_n上的inverse mean square。

源 plain fourth moment with short prime factors，12531–12578，prime-slot coefficients为固定有限ray角色线性组合，positive slots需mesh；κ<1时还要求β_*≤(1+κ)/2。全Hecke7/8确实允许κ=3/4，但n1+n2+6κz≤M及所有canonical mask/row前件仍保留。其pure-twist说明12870–12901仍记录固定height成本，并未自动给上述additive shifted response。

新接口(8)(10)可改善其中真正canonical pointwise block的高度成本，但不能将a_i(p)任意有界系数的旧average定理整体强化，也不能将cycle-dependent coefficients改成独立于row的固定mark。197/198所需的一侧Gram净预算还要求K02、K12等符号关联，分别取绝对值会丢失本来可能改善比例的负修正。

198的后续段还明确记录225已推进pure-prime finite transfer，226将背景缩为确定性Toeplitz及小op remainder。本文不把这些旧进展重新列为完全未做；它没有独立重审其全部证明，也没有声称(25)解决其剩余one-/two-/three-prime mixed-frequency ledger。

## 9. 可用结论与下一项真正算术前件

已得到的可复用接口 [T/R]：

1. 固定gap下对全部conductor与τ的canonical reciprocal/Λ pointwise bounds，natural deletion账本完整；τ∼T只付subpower/log。
2. 原sharpΛ前缀的uniform Perron估计，包括τ≈0的真实principal项。
3. 该前缀对原AF finite frame的absolute-height乘子压缩op bound；low时间由原窗尾另付。
4. 同一G−I的弱四次迹Oε(T^(3/4+ε))，不依赖把signed words拆开，也不改物理矩阵。
5. 真正短窗的Mellin η与η^−1取消，以及X=T²/H=T、long-prime b>1时的准确指数阈值；全conductor向coprime additive phases的√φ(q)费用。

真实缺口是：在保留原response kernel和全部signed背景交叉项的情况下，对截断Λ_T*Λ_T及near difference h∼T给constant-size一侧净预算或合适的dispersion/Type-II均值。可从(8)(10)(35)向该任务传入规范Type-I块，但需要另证带实际response约束的Type-II/shifted-convolution saving。不能因已有μ marked moments就称该步骤完成。

与305的待审目标p=0.673399相比，MT窗的固定中心四矩门槛约0.3266021983；本报告的T^(3/4+ε)弱界无法触及该门槛。没有得到更高比例，没有把全导子7/8定理重建为本项目Lean证明，也不宣称RH。
