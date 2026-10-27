# 固定ℓ11：实际q核、Γ0(11)类型、源费用与537控制

2026-10-27；`/root/ell11_source`独占稿。已按AGENTS恢复README／STATE、check→show、G20261027、D20261027I、宏观前沿及固定marked-cusp准入。本文不改STATE／cadence／看板，不造Maass／Green／height或变更level；Pan关系由独立分支检验。原件是[exact脚本](../../../scripts/ell11_source_controls.py)及[source-controls.json](source-controls.json)，已经实际运行terminal。

## 1. 真正的typed输入，不借名字替代

固定project变量q=e^(2πiτ)，

\[
 g(\tau)=\eta(\tau)^2\eta(11\tau)^2
 =q\prod_{n\ge1}(1-q^n)^2(1-q^{11n})^2.
\]

η乘积定义及变换式只引用实际核过的官方[DLMF27.14.12](https://dlmf.nist.gov/27.14.E12)、[23.18.5–7](https://dlmf.nist.gov/23.18)。本节之后的Γ0(11)有限生成元、cusp、费用及系数核算在项目中直接给出，没有套未读的eta-quotient定理。DLMF部分章节用e^(πiτ)为nome，本稿始终以τ公式/上述q定义消费，未混一次平方。

左商集合Γ0(11)\SL2(Z)（Γ0以左乘作用的轨道，随后SL2以右乘作用）以bottom row在P¹(F11)的类标记；取I及S T^r（0≤r≤10）共12个representatives。对右乘S、T、S^-1、T^-1的48个Schreier关系，脚本exact求h=rep·generator·rep_target^-1，均在Γ0(11)。乘−I不改weight2作用，故可规范c≥0。

对c>0，η变换在两个因子中对应矩阵h=(a,b;c,d)与h11=(a,11b;c/11,d)。两次平方后的总乘子为exp(2πi E_h)，其中

\[
 E_h=\frac{a+d}{c}-s(d,c)-s(d,c/11)-\frac12,
\quad s(d,c)=\sum_{r=1}^{c-1}\frac rc
          \left(\frac{dr\bmod c}{c}-\frac12\right).
\]

c=0时规范h=T^b，乘子为exp(2πib)。48个E_h以Fraction验出全部为整数；Schreier生成给所有Γ0(11)作用都为g(hτ)=(cτ+d)²g(τ)，**character确为trivial**。JSON保存完整48关系及phase，不是几个浮点样本。

η在H无零，故g在H无零。∞宽1，q首项q给ord∞g=1。对Fricke W11=(0,-1;11,0)，采用det^(k/2)(cτ+d)^−k规范，η的S变换直接给

\[
 g|_2W_{11}=-g.
\]

在0的归一化Fricke坐标同样首阶1；若用S坐标，其宽为11，g|S=−η(τ)²η(τ/11)²/11，以q0=e^(2πiτ/11)亦阶1。Fricke eigenvalue−1不等于U11 eigenvalue−1，二者不可混同。

Γ0(11)恰有两个cusps：reduced a/c在11|c时属于∞类，否则属于0类，Bezout直接构造相应Γ0矩阵；其宽分别1、11。−1与−3均非F11平方，所以无order2/3 elliptic stabilizer。由index12的orbifold Riemann–Hurwitz，compactX0(11) genus为1。因而g∈S2(Γ0(11))非零，且ω=g(q)dq/q是compact曲线上的无零全纯1-form。

这核的是scalarΓ0(11)对象，**不是原II2,2的trivial Weil表示**，更未给从此scalar对象到某个orthogonalρ、harmonic Maass／arithmeticChow的typed运输。

## 2. 源核、系数方向和全S_exp合法费用

复用583的F_r(q)=L_r(j(q))、a_n(r)，j=q^-1+744+Σ_(n≥1)c_nq^n且c_n>0，定义

\[
 K(u)=\frac1{2\pi i}\oint_{|q|=R}
          e^{uj(q)}g(q)\frac{dq}{q},\qquad
 \ell(r)=\int_{\mathbb R}r(u)K(u)du.
\]

g在|q|<1全纯、首项q，F_r在punctured disk全纯。对任意0<s<R<1，设A_s=max_|q|=s |Rej|、C_R=max_|q|=R|g|。583的|a_-m(r)|≤s^m p_A_s(r)、g的Cauchy界|c_g(m)|≤C_R R^-m给

\[
 \ell(r)=\operatorname{CT}(F_rg)
 =\sum_{m\ge1}a_{-m}(r)c_g(m),\qquad
 |\ell(r)|\le C_R\frac{s}{R-s}p_{A_s}(r).
 \tag{1}
\]

这里p_A(r)=∫|r(u)|e^(A|u|)du，与583相同；若用S_exp原sup seminorm，则对整数N>A有p_A≤2p_(N,0)/(N−A)。源r=e^(u/2)f不更改。绝对换序支付全noncompact源的这份强费用，未免费授予每一个405源都已在该域；实际Pan仍须逐项核其强矩。

对fixedR令M_R=max_|q|=R |j(q)|，有

\[
 |K^{(k)}(u)|\le C_R M_R^k e^{M_R|u|},
\quad
 |\ell(r)|\le C_R\sqrt{2L}e^{M_RL}\|r\|_{du}
 \quad(\operatorname{supp}r\subset[-L,L]).
 \tag{2}
\]

这里按583及当前source-quadrature原件消费的zero-extension symbol为
\(\|D_{\log}r\|^2=(2\pi)^{-1}\int\log(2+|t|)|\widehat r(t)|^2dt\)，Fourier约定\(\widehat r(t)=\int r(u)e^{-itu}du\)。它满足Dlog²≥log2·||r||²，所以fixed窗再乘(log2)^−1/2即为Dlog费用；不能与553的带额外1的Hlog等价范数无声混为精确同式，也不是全线uniform原norm或算术height费用。

脚本给一份完全有理的显式上费：s=1/1024、R=1/512。用σ3(n)≤n⁴及

\[
 \sum_{n\ge1}n^4x^n=\frac{x(1+11x+11x^2+x^3)}{(1-x)^5},
\quad
 \prod_{n\ge1}|1-q^n|^{-24}
 \le\exp\frac{24x}{(1-x)^2}
\]

构造|j|上界；用exp(t)≤1/(1−t)，并对g的两个产品同样处理，所有接受都为rational比较。JSON中正式上界的显示为

\[
 M_s<1989.942,\quad M_R<1754.306,\quad C_R<0.001960800.
\]

K和ℓ本定义为**复线性**。若之后称其为ξ(f_r)的cusp系数，ξ本身反线性，且Petersson线性腿和principal-part配对必须按BY(3.8)另核；本稿没有从C值functional直接取得native shadow、relativePic或Weil型。

## 3. 实际exact q控制与同一个537小支撑控制族

脚本用整数E4³／Δ和两个eta乘积，计算qj、g及K^(n)(0)=CT(j^n g)，至n=12全部为exact整数。前项为

\[
 g=q-2q^2-q^3+2q^4+q^5+2q^6-2q^7+\cdots,
\]
\[
 K(0)=0,\quad K'(0)=1,\quad K''(0)=1486,
\quad K'''(0)=2246795.
 \tag{3}
\]

537本身是全17/16窗定理，未固定唯一数值waveform。583的[关系原稿(15)–(17)](../cusp-transport/principal-relations-and-nonroot-test.md)实际使用同一类

\[
 r_\phi=(D^2-1/4)(u\phi(u)),
 \quad \phi\ge0\text{ nonzero even},\quad
 \phi\in C_c^\infty((-\epsilon,\epsilon)).
 \tag{4}
\]

本稿不换φ伪冒已验证的固定样本，而给**原控制族共同的充分小阈值**。设H=K''−K/4，旧constant核A=CTexp(uj)、V=A''−A/4。exact

\[
 H'(0)=8987179/4=2246794.75,\qquad V'(0)=1355202054.
\]

选择同一ε≤2^-20。由(2)和exp(M_Rε)≤1/(1−M_Rε)，脚本有理核

\[
 \sup_{|u|\le\epsilon}|H'(u)-H'(0)|
 \le\frac{\epsilon C_R(M_R^4+M_R^2/4)}{1-M_R\epsilon}
 <17741.14<H'(0),
\]
\[
 \sup_{|u|\le\epsilon}|V'(u)-V'(0)|
 \le\frac{\epsilon(M_R^4+M_R^2/4)}{1-M_R\epsilon}
 <9047910<V'(0).
\]

因此对(4)中的**每个同一φ**，双pole矩精确为0、rφ≠0，并且

\[
 \ell(r_\phi)=\int_0^\epsilon u\phi(u)[H(u)-H(-u)]du>0,
\quad a_0(r_\phi)>0,
\quad Q_\zeta(r_\phi)\ge2^{-49162}\|r_\phi\|^2>0.
 \tag{5}
\]

573的另一个evenχ cutoff源不是(4)这份odd控制族；本稿没有评价它。一个非零control也不代全源coverage，rank1ℓ当然有核；既有finite-rank／Baire反测不重计。

## 4. 全cusp与单腿的确切差别

ω=g(q)dq/q为X0(11)全纯微分，F_r=L_r(j)在开曲线全纯，只有∞和0可能是孤立essential。Residue theorem仍适用于这两处孤立奇点，故

\[
 \operatorname{Res}_{\infty}(F_r\omega)=\ell(r),\qquad
 \operatorname{Res}_{0}(F_r\omega)=-\ell(r).
 \tag{6}
\]

0腿若用S坐标须保cusp width11；若用归一化Fricke坐标，则g|W11=−g而F_r(W11τ)=L_r(j(11τ))。不能忽略width/Fricke后把两局部坐标的constant term直接同号相加。全pullback的两腿合计恒0；本候选正是只读∞，所以principal／Pan下降必须重测。这不排不同relative两腿读出，但(ℓ,−ℓ)边界数据也不自动给mixedRR。

## 5. 给Pan/Borel分支的标准几何前件

j:X0(11)→X(1)=P¹的degree为12，有限branchvalues只能是0、1728，另有∞处cusp分歧。原Γ0(11)无elliptic stabilizer，故有限点的局部ramification为3和2；∞两cusp widths1和11。ω无零，所以ω/dj的代数分支在有限branchpoints至多有z^-2/3或(z−1728)^-1/2的可积奇性。选择∞width1分支时，其大z展开从−z^-2起；这些只给后续Borel/Stieltjes推导的前件，完整slit/jump/endpoint符号由独立Pan稿证明。

在正q轴q_i=e^-2π，g(q_i)>0。由E4³−E6²=1728Δ和E6(i)=0有j(i)=1728；S不变性给j_q(q_i)=0。正q系数又直接给

\[
 j_{qq}(q_i)=2q_i^{-3}+\sum_{n\ge2}n(n-1)c_nq_i^{n-2}>0.
\]

这些是标准j/η输入及直接推论，不是新RH或Pan关系定理。本稿没有宣称ℓ杀任何Pan，也没有构造Maass／Green或算术height。source/typed/q-control部分按标准建设性范围交root消费；若后续完整Pan／尾给新的严格数学信息，由root按实际净值计轮，不能以本分支标签藏掉。
