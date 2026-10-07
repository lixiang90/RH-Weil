# 原短 Möbius twist 的统一准入与完整 Vaughan 剩余的零点留数

2026-10-08。作者：radial_review。基线 main030576085955927fcb63742c770b5cd171cb925f。仅记录本轮新增的原对象准入和精确障碍；不修改477或旧稿。**没有新的 whole 四矩上界、比例或无零边界。**

## 1. 输入与实际 sharp 对象

使用原普通ζ的全高度输入[Rθ]：1/2≤θ<1，ζ无零于Re(s)>θ。原来源和 θ 的状态仍按冻结论文及475–477阅读，不从零密度单独推出这个输入。

令 X=T/(2π)、J_T=[T/4,4T]，固定0<a<1/4，
\[
 U=V=\lfloor X^a\rfloor,\qquad
 Y=X^{(2+4a)/3},\qquad
 G_W(s)=\sum_{n\le W}\mu(n)n^{-s}.
\]
W的和按原整数集合解释，不改变 sharp cutoff。以下得到真正的正高度统一界
\[
 \sup_{t\in J_T}|G_W(1/2-it)|
 \ll_{\theta,\delta,\varepsilon,a}
 W^{\theta-1/2+\delta}T^\varepsilon
 \quad(1\le W\le V),                         \tag{1}
\]
其中 δ>0先固定，ε>0任意固定。它是准入；不能只由(1)认领完整 mixed fourth 的付款。

## 2. Buffered reciprocal 的自证

可取0<δ<(1−θ)/4；更大δ只使(1)更弱。对大的|v|，在中心2+iv的圆盘上选
\[
 r_0=1/2,\quad r=2-\theta-\delta,\quad
 R_1=2-\theta-\delta/2,\quad R_2=2-\theta-\delta/4.
\]
R2盘的实部严格大于θ，且不含ζ的 pole1；[Rθ]允许从中心Euler值选择解析 logζ 分支。原普通ζ在固定实部带的多项式增长给Re logζ=O(log(|v|+3))，Borel–Carathéodory遂在R1盘给 |logζ|=Oδ(log(|v|+3))。r0盘完全在Re(s)≥3/2，Euler series给 |logζ|=O(1)。

三圆定理在r盘给
\[
 |\log\zeta(s)|\ll_\delta(\log(|v|+3))^{b_\delta},
 \qquad b_\delta=\frac{\log(r/r_0)}{\log(R_1/r_0)}<1.
\]
它覆盖θ+δ≤Re(s)≤3/2，更右侧由Euler直接处理。故对任意固定η>0，
\[
 |\zeta(\sigma+iv)^{-1}|
 \ll_{\theta,\delta,\eta}(1+|v|)^\eta
 \quad(\sigma\ge\theta+\delta).                \tag{2}
\]
低高度由紧集上的解析 reciprocal 处理；ζ在1的 pole只使1/ζ取零，不造成 reciprocal 极点。这里没有把无零条带直接当成 Lindelöf；(2)的 buffer、圆盘和分支均已明确。

## 3. 保原端点的 Perron 证明

W≥2时取w♯=floor(W)+1/2，与原n≤W的整数集合完全相同。以c=1/2+1/log w♯、H=T²在Re(z)=c使用 truncated Perron：
\[
 G_W(1/2-it)=\frac1{2\pi i}
 \int_{c-iH}^{c+iH}
 \frac{(w^\sharp)^z}{z\,\zeta(1/2-it+z)}\,dz
 +O\!\left((w^\sharp)^{1/2}\log^2(2w^\sharp)/H\right). \tag{3}
\]
该误差直接由 |μ(n)|≤1及
min(1,1/(H|log(w♯/n)|))求和给出。最近整数距w♯至少1/2；近端区按|n−w♯|的 harmonic sum，远端由Re(1/2+c)>1的绝对收敛支付。没有遗漏整数端点或把Π/半权当成原 sharp sum。

移到Re(z)=θ−1/2+δ>0。全矩形的 reciprocal 实部≥θ+δ，因此无零极点，也不跨z=0。ζ在1的 pole是 reciprocal 的零，没有新留数。该矩形的真实高度最多O(T²)；先在(2)选择足够小的η，使整个 reciprocal 费用≤T^(ε/2)。左线的1/|z|积分为Oδ(logT)，水平段费用为O(W^(1/2)T^(−2+ε/2))。因W≤X^a、a<1/4，(3)误差和水平段均可吸收；W=1直接处理。于是(1)对全部W和J_T统一成立。

这个 proof 不使用 ordinary reciprocal 在Re=1/2的未知界，也不在 Perron shift中穿过原零点。

## 4. 共同 product cutoff 与精确零点留数

原完整剩余保持
\[
 C_4(t)=-\frac1{a_\ell\ell}
 \sum_{\substack{m>U,\ k>V\\Y<mk\le X}}
 \frac{\Lambda(m)b_V(k)}{\sqrt{mk}}(mk)^{it},
 \qquad b_V(k)=\sum_{\substack{d\mid k\\d\le V}}\mu(d).
\]
置 F_U(s)=Σ_(m≤U)Λ(m)m^(−s)、Dζ=−ζ′/ζ。Re(s)>1上的完整、未作product截断的 generating function为
\[
 \mathcal H_{U,V}(s)
 =(D_\zeta(s)-F_U(s))(1-\zeta(s)G_V(s))
 =D_\zeta-F_U+\zeta F_U G_V+\zeta'G_V.       \tag{4}
\]
1−ζG_V在k≤V的系数全零，k>V的系数为−b_V(k)，故(4)严格保留m>U、k>V；再用两端 Perron差才产生共同Y<mk≤X，不能把它换成两个独立 rectangular sums。

对任何ζ零点ρ及其重数mρ，F_U、G_V都是 entire，而
\[
 1-\zeta(\rho)G_V(\rho)=1,\qquad
 \operatorname{Res}_{s=\rho}\mathcal H_{U,V}(s)=-m_\rho. \tag{5}
\]
即使重数大于1，此留数也不变；ζ′G_V在该点无极点。这是完整实际系数恒等式，不是某个positive sector的下界或抽象模型。

令x♯=floor(X)+1/2、y♯=floor(Y)+1/2。它们保持两 sharp cutoff的整数集合。对s=1/2−it，Perron kernel为
\[
 K_{X,Y}(z)=\frac{(x^\sharp)^z-(y^\sharp)^z}{z}.
\]
只要所用有限矩形绕开边界零点，每个被跨零点的确切贡献仍为
\[
 -m_\rho K_{X,Y}(\rho-s).                    \tag{6}
\]
U,V没有给原零点包增加减幅因子。ζ在1处的 Laurent展开还给
\[
 \mathcal H_{U,V}(w)
 =-\frac{G_V(1)}{(w-1)^2}
 +\frac{1-G_V'(1)+F_U(1)G_V(1)}{w-1}+O(1).
\]
故该pole的贡献是
\[
 -G_V(1)K_{X,Y}'(1-s)
 +(1-G_V'(1)+F_U(1)G_V(1))K_{X,Y}(1-s).
\]
在原t≈T≈X下，|G_V(1)|≪logX、|G_V′(1)|+|F_U(1)G_V(1)|≪log²X，未归一化贡献为O(X^(−1/2)log²X)，除原a_ell ell后为O(X^(−1/2)logX)。它不抵消(6)的top zero费用。

## 5. 此轮实际结论与未付项

(1)是原 sharp short Möbius twist 的真正全正高度准入；(5)–(6)说明不能据此把原 absolute zero-packet/density 方法的 top 费用减掉。原μ多项式在零点处的 factor恰好回到1。改变合法固定a或小幅移动cut只改变原剩余域，不能自动改变这个留数。

同样，G_V的点值/单独二矩不提供Λ(m)与b_V(k)在共同Y<mk≤X上的四份系数、全aspect ratio及共同正高度的联合矩。该步骤仍须证明真实带符号相消，或控制(6)各零点包的联合能量；ordinary ζ moments、AFE和small-factor结果不能凭(1)直接替代它。本轮没有证明 M_C4<T^(5/7)或O(1)，也没有由上述接口宣布新whole结果。

该障碍只针对这些具体搬用方式，不排除actual Möbius/prime算术产生新的相消。新六邻域实际比例研究是独立的二阶稳定性进展，不由本文件供应四阶常数。
