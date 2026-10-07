# 原 signed response 的 Type-I 准入、实际 Gram 幂界与 Type-II 缺口

2026-10-07。状态 [T/R]：相对于固定全导子无零半平面及其uniform reciprocal/logarithmic control，证明一个非空Vaughan分解的真实Type-I因子可以进入原six-window、sharp-cell、finite-frequency Hilbert Gram，完整支付其ghost double pole与height峰。其contour幂界仅强于最粗coefficient l1预算；本轮独审给同一固定balanced cell更强的无条件finite-ratio Schur基线，见§6。另证明原有限压缩的低Λ通道四范数预算。两者都不达到完整signed第四迹的常数预算，不提高零点比例。determinant/shifted-convolution残项仍为 [O]。

## 1. 实际待办与版本

先读197、198、225、226、305，再按其后续更新读232、238–240。不能把226早期全部mixed words重新列为未做：227已有相关闭合主张，232随后逆审定位了primitive高乘积区ab>XL²的漏区；239–240明确保留共同centered、six-window、finite-band的实际Möbius divisor response。下面选这个未闭合physical quotient中的一项Type-I块，而不是重新发明任意系数模型。

canonical LF SHA256绑定：

| 输入 | SHA256 |
|---|---|
| 197 | 98bd8ea89679030e0ffb8135d324b5654900f260b3f45c9ae816d5ea870eaae7 |
| 198 | d7d2d9a20e9c6437b55bb23e8494f2a969b1b1ba46d63b70fadd7d42de904e66 |
| 225 | 7b87d8e53007873edcb19d0cf42651baab71bcd40b21d7a3f3a3cd81eb35ddd0 |
| 226 | 46c3a17b079425c6b911df620f64c73fb6b24e6624278615d65c62c6a3b58d8c |
| 232 | 7580ad56dd32231762d5b4e980f284b58a99860848b5cc02e779c0f8d0bdaa56 |
| 238 | d46a8fca611f24ba3c647cfc9b2db6240d1a2a2d0372242b7b51d745bd22c82d |
| 239 | b35398ecdfbe65ce2ea04856a5e66f6676d61cc109b3de48e855b514db0cfa20 |
| 240 | 1867e490fed07598e4f6c44952352d2c3a7a0dc4b066b6c1720e8a96d3a0ed8a |
| 305 | fab0841ee5734d35db023f0b1305bf75f9b19fcd11feda2ff08c73b2562d1aa9 |
| hybrid-uniform-reciprocal-and-fourth-trace-interface.md | 25468f8c29dc195d08083dd0fb4b60b5aea48478c9c1ce93053875d5dcc7d83c |

最后一份报告位于本日期reviews目录，绑定已提交的最终canonical LF版本；不使用此前原始CRLF字节hash。外部源为OpenAI/math固定提交adc7f1241b42e322a6451854ab7e4b4c146bf78a的September-30 paper.tex，canonical LF SHA256：

42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3。

全导子输入仅以明确[R]使用：所有所涉primitive有限阶Dirichlet角色在Re s>θ无零；本轮取θ=7/8。源1531–1620的global logarithmic-control/deleted-Euler证明及上一接口报告给固定gap、全height的规范μ和Λ界。未重建外部Lean或整个算术来源。

## 2. 不能遗漏的原physical对象

令L=log X、D=round(XL)、τ_k=2πX+2πk/L。这里D沿238的finite-k notation；原AF实际frame维数为d=floor(XL)。下述准入及有限Schur估计逐式适用于任意D=XL+O(1)，包括原d，但floor与round的精确有限核不被当作恒等。选一个固定balanced高cell，a,b,c,d∈[cY,CY]，Y=X^(3/4)，其中0<c<C固定。其ab>XL²最终自动成立，故确在232定位的高乘积区域。

238的Hilbert空间为

\[
H=L^2(\mathbb R/L\mathbb Z,dz/L).
\]

原ratio feature可以精确写为

\[
F_{a,b}(z)=
\phi(z+\log(a/b))\phi(z)\phi(\log b-z)^2.
\tag{1}
\]

这由原P_i(z+s_i)代换所得，保留六窗cross overlap

\[
W_{a,b;c,d}=\langle F_{a,b},F_{c,d}\rangle_H.
\]

coefficients仍是\(b_ab_b=\Lambda(a)\Lambda(b)/(4\pi^2\sqrt{ab})\)。实际finite frequency kernel始终为

\[
\frac1D\sum_k\cos\!\left(\tau_k\log\frac{ad}{bc}\right).
\tag{2}
\]

没有换成limiting sinc kernel，没有只保留resolution core，也没有删除carrier或全部背景cross terms。

为与238的kernel参数严格一致，以下记Q=XL及
\(K_{Q,D}(t)=D^{-1}\sum_{k=0}^{D-1}\cos(2\pi(1+k/Q)t)\)。
因而式(2)准确为\(K_{XL,D}(X\log(ad/bc))\)，不得将其首参数换成X。

为使composite ghost extension具有可核canonical前件，固定如下合法extension：primitive pair mask取1_(a,b)=1，另乘原rectangular/factor/aperture的有限interval cutoffs；它在原distinct-base prime-power support上准确等于physical mask，在composite处也在U、V、估计目标和k之前固定。每个固定b时，其a切片有固定有限个interval边界。该选择是238允许的channel-independent整数mask准入条件，不能把本报告的定理扩到任意鬼点mask。

\(\|F_{a,b}\|_H\le1\)，且固定b时作为log a的函数，其Hilbert-valued总变差在固定annulus中一致有界：导数只落在式(1)第一个φ上，uniform C²窗足够。finite interval cuts只加入固定数目的jump。互素mask不会被当成smooth profile，而在下一节作为自然zero extension保留。

## 3. 非空canonical Vaughan通道

取U=V=Y^(1/4)。用238–239同一个one-factor identity：

\[
J_{U,V}=\mu_{\le U}*1*\Lambda_{>V},\qquad
I_{U,V}=J_{U,V}+\Lambda_{\le V},\qquad
II_{U,V}=\Lambda-I_{U,V}.
\tag{3}
\]

high cell中a>V，所以I(a)=J(a)。II不是square-root-vacuous：(U+1)(V+1)<cY最终成立；其composite ghost support允许r>U、v>V、rvw≈Y。II在很多单素数a上为零不表示该整体通道为空。

对固定b，置χ_b(n)=1_(n,b)=1。完全乘性准确给

\[
J(n)\chi_b(n)
=(\mu\chi_b\,1_{\le U})*(1\chi_b)*
  (\Lambda\chi_b\,1_{>V})(n).
\]

所以它的Dirichlet series是

\[
{\cal J}_b(s)
=M_{U,b}(s)L_b(s)\{D_b(s)-D_{\le V,b}(s)\},
\tag{4}
\]
\[
M_{U,b}(s)=\sum_{r\le U}\mu(r)\chi_b(r)r^{-s},
\quad L_b(s)=\zeta(s)\!\prod_{p\mid b}(1-p^{-s}),
\quad D_b=-L_b'/L_b.
\]

这是完整canonical truncated convolution，不是给任意a_n配上一个1/L。全部punctures都在rad(b)，effective conductor包括删除radical，且rad(b)≤CY。固定其他base finite-order角色时，只需把χ_b换成该角色的自然punctured presentation，q_eff仍须完整记账。

## 4. Type-I generating function的uniform边界

固定

\[
\theta<\sigma_0<\sigma<1,\qquad
\sigma_0=\theta+\delta/3,\quad\sigma=\theta+\delta,
\tag{5}
\]

δ>0先于X、U、V、b、τ确定。以下q_eff、U、V、Y在X的固定多项式范围内；常数允许依赖该范围，不能令它随后增长。

规范sharp μ Perron移线到θ以上、但低于σ_0的固定线，再吸收log与任意小conductor/height幂，给

\[
\sum_{n\le Z}\mu(n)\chi_{\rm orig}(n)n^{-it}
\ll_{\delta,\epsilon} Z^{\sigma_0}
       \{q_{\rm eff}(3+|t|)\}^{\epsilon}.
\tag{6}
\]

截断误差只用|μχ|≤1；截断高度可取Z、q_eff、3+|t|的固定大多项式，没有新角色或任意系数。

为明确height量词，(6)用的是已twisted coefficients μ(n)χ(n)n^−it 的Perron，不从untwisted summatory乘n^−it作分部积分。可先取移线实部θ+δ/4，H=(2Zq_eff(3+|t|))^C；重新命名任意小analytic-conductor指数后，vertical bound为Z^(θ+δ/4)(q_eff H(3+|t|))^η log H。先固定充分大C，再令η同时小于δ/[24(C+1)]及所需ε/[4(C+1)]，即可吸收log H并得(6)。initial coefficients模不变，horizontal/truncation以Z/H及固定log powers支付。此后Abel只对实权n^−σ微分，系数仍携同一个fixed t，完全没有额外|t|导数。因σ>σ_0，普通μ Dirichlet series在该线收敛，得到

\[
M_{U,b}(\sigma+it)
\ll_{\delta,\epsilon}\{q_{\rm eff}(3+|t|)\}^{\epsilon},
\tag{7}
\]

对全部U统一。这里使用的是实际μχ_b，而不是238–240合成后任意divisor column。

上一报告的sharp Λ Perron输入，以同一个较低σ_0再做Abel，给

\[
D_{\le V,b}(\sigma+it)
=\mathbf1_{\rm principal}\frac{V^{1-\sigma-it}}{1-\sigma-it}
+O_\delta(\log^2\{2q_{\rm eff}(3+|t|)\}).
\tag{8}
\]

端点及lower-limit常数已在O项中；\(\sigma-\sigma_0>0\)使误差积分对V统一。principal的有限Euler删除不改变D的s=1留数。

具体地，先用shifted Λ Perron得到B(Z,t)=Σ_(n≤Z)Λ(n)χ(n)n^−it=1_principal Z^(1−it)/(1−it)+O_δ(Z^σ0 log²(2Zq_eff(3+|t|)))。Abel也只微分实权n^−σ。误差成本不超过V^(σ0−σ)log²(2Vq_eff(3+|t|))+σ∫_1^V u^(σ0−σ−1)log²(2uq_eff(3+|t|))du，统一为O_δ(log²(2q_eff(3+|t|)))。principal积分准确化为(8)主项加−σ/[(1−it)(1−σ−it)]，后者由fixed gap控制。这里若从untwisted B(Z,0)微分n^−σ−it，会错误加入|t|；本证明没有此步骤。结合global L和D控制得到

\[
|{\cal J}_b(\sigma+it)|
\ll_{\delta,\epsilon}\{q_{\rm eff}(3+|t|)\}^{\epsilon}
\left(1+\frac{V^{1-\sigma}}{1+|t|}\right).
\tag{9}
\]

式(9)对t≈0保留真实V^(1−σ)峰；不能把它整个换成high-height subpower。L本身的principal regularizer在固定σ<1线上距pole有固定余量。等式L_bD_b=−L_b′还说明式(4)在L零点处可去，不以分母零点判定其解析性；零自由输入用于(7)(9)的强界。

## 5. Sharp Type-I前缀与不可删除的double pole

令τ∈[c_1X,C_1X]，固定0<c_1<C_1，x≈Y。准确前缀为

\[
{\cal I}_b(x,\tau)
=\sum_{n\le x}\frac{J(n)\chi_b(n)}{\sqrt n}n^{i\tau}.
\tag{10}
\]

其coefficients满足\(|J(n)|\le d(n)\log n\)。Perron实际取x♯=floor x+1/2，随后将该半整数重新记为x；原整数prefix完全相同。若最终主项用原实x，(13)对x的导数为x^(−1/2+iτ)(A_b log x+B_b)，故只差O(Y^−1/2 log^C(2YUV))，吸收到(12)。取初始Perron线Re s=1/2+1/log x、截断高度H为(q_eff X Y U V)的固定充分大幂。原sharp整数截断保留，误差用该divisor majorant和harmonic endpoint sum支付。

移到Re s=σ−1/2>0。由(9)，左线除通常log H外，还需支付

\[
\int_{-H}^{H}
\frac{dt}{(1+|t|)(1+|t-\tau|)}
\ll\frac{\log(2H)}{X}.
\tag{11}
\]

证明分别取|t|≤|τ|/2、|t−τ|≤|τ|/2及其余部分；在前两块另一个分母为Ω(X)，余下尾为可积平方衰减。因而

\[
{\cal I}_b(x,\tau)
={\cal P}_{U,V,b}(x,\tau)
+O_{\delta,\epsilon}\!\left[
Y^{\sigma-1/2}X^\epsilon
 \left(1+\frac{V^{1-\sigma}}X\right)\right].
\tag{12}
\]

horizontal joins及Perron endpoint误差通过所选fixed polynomial H吸收；q_eff≤X^B时原conductor小幂只计入X^ε一次。实际U=V=Y^(1/4)<X使括号有一致常数。

principal时式(4)具有double pole，来源是ghost completion，不是完整Λ的简单pole。写

\[
r_b=\prod_{p\mid b}(1-p^{-1}),\quad
A_b=r_bM_{U,b}(1),\quad
B_b=r_b\{M'_{U,b}(1)-M_{U,b}(1)D_{\le V,b}(1)\}.
\]

因为\(L_bD_b=-L_b'\)的simple-pole系数准确消失，所以principal留数为

\[
{\cal P}_{U,V,b}
=x^{1/2+i\tau}
\left[
A_b\left(\frac{\log x}{1/2+i\tau}
-\frac1{(1/2+i\tau)^2}\right)
+\frac{B_b}{1/2+i\tau}
\right].
\tag{13}
\]

\(|A_b|\ll\log(2U)\)、\(|B_b|\ll\log^2(2UV)\)，故该项为O(√Y X^−1 log^3(2YUV))。非principal没有此留数。没有将τ≈0的ghost peak静默删去：它在移线t≈τ处由(11)及经过的pole同时支付。

## 6. 真实Type-I Hilbert Gram块的contour预算与有限比值基线

在原finite heights上定义

\[
S_{I,k}=
\frac1{4\pi^2}
\sum_{a,b\in{\cal C}_Y}
\frac{J(a)\Lambda(b)}{\sqrt{ab}}\,
1_{(a,b)=1}\,
e^{i\tau_k\log(a/b)}F_{a,b}.
\tag{14}
\]

式(14)是238的actual synthesis换成原I系数；保持全部ghost原子、原mask、six-window及有限k，未替换为任意矩阵。

固定b，以(12)(13)及Hilbert-valued Abel估计a-sum。上一节前缀是χ_b的canonical sequence；式(1)及finite cuts的变差成本统一，因此

\[
\left\|
\sum_{a\in{\cal C}_Y}
\frac{J(a)\chi_b(a)}{\sqrt a}
 a^{i\tau_k}F_{a,b}
\right\|_H
\ll_{\delta,\epsilon}
Y^{\sigma-1/2}X^\epsilon+\frac{\sqrt Y}{X}\log^C X.
\]

只在已经完成该canonical估计后，以
\(\sum_{b\asymp Y}\Lambda(b)/\sqrt b\ll\sqrt Y\)
付denominator绝对和，得到

\[
\boxed{\|S_{I,k}\|_H
\ll_{\delta,\epsilon}Y^\sigma X^\epsilon
+\frac YX\log^C X.}
\tag{15}
\]

对原有限k平均直接给

\[
\boxed{G_{I,I}:=\frac1D\sum_k\|S_{I,k}\|_H^2
\ll_{\delta,\epsilon}X^{3\sigma/2+\epsilon}
+X^{-1/2}\log^C X.}
\tag{16}
\]

θ=7/8、δ及ε任意固定充分小时，这是O_ε(X^(21/16+ε))。最粗绝对coefficient l1平方预算为X^(3/2+ε)，相对此粗预算改善3/16。它已经合成canonical Vaughan convolution、自然moving zero extension、Hilbert feature、sharp factor cell与全部实际finite frequencies，但不是本cell的最佳Gram上界，也不将这项比较宣称为新的算术saving。

独立推导 `hybrid-finite-ratio-gram-baseline.md` 进一步给：同一coprime整数mask使所有ratio a/b约化且互异，balanced固定区间内不同log-ratios间距至少c_0/Y²。原有限复核的几何级数满足
\[
 |D^{-1}\sum_k e^{2\pi i k(s_i-s_j)/L}|
 \le\min(1,C_0/(X|s_i-s_j|)).
\]
排序加Schur得到
\[
 G_{rr}\ll\left(1+\frac{Y^2}{X}\log(2Y)\right)A_{rr},
 \quad A_{rr}\ll_\epsilon X^\epsilon,
 \qquad |G_{rs}|+|G_{rs}-A_{rs}|\ll_\epsilon X^{1/2+\epsilon}
 \tag{16a}
\]
对r,s∈{I,II,Λ}均成立，包括I–II mixed，保留原features和全部finite k。
这里用的是J、II的divisor majorant，而非新的零自由区。
此界比(16)更强；因此本节contour推导的主要价值是canonical因子的真实准入、
uniform prefix、ghost pole及height峰账本。式(16a)仍远大于raw o(L⁴)，
不作为必要Bessel证书，不扩大到cross-cell alias，也不自动覆盖共同shell-centering的额外mass项。

其范围也必须准确：这是238–239未闭合alternating physical-response Gram的一个内部I–I块，不是完整四次迹。它仍远大于所需raw o(L^4)。同atom reference A_(I,I)必须按238(42)原样扣除；I–II、II–II及ghost diagonal相消仍在fixed vector(1,1)中联合保留。不能把(16)独立相加成目标预算。

特别不能再对b使用一次canonical prime界：a-sum的误差和χ_b依赖b，它们不是b变量的固定ray coefficient。对b取上述绝对和是本定理明确支付的费用；全导子uniform不会自动产生跨b的dispersion。

## 7. 一个真正o(N)的低Λ full-compression块

此付款不需要新无零区，是经典短Dirichlet多项式均值进入实际matrix的量化版本。它同时控制原(3)中的低Λ项，并避免以“Λ≤V很短”为由不付full kernel费用。

令Z≤X^(1/2)、\(Q_Z(t)=\sum_{n\le Z}\Lambda(n)n^{-1/2+it}\)，保留原sharp cutoff。若c_m是Q_Z²的coefficients，则

\[
\sum_m|c_m|^2
=2\left(\sum_{n\le Z}\frac{\Lambda(n)^2}{n}\right)^2+O(1)
\ll\log^4(2Z).
\tag{17}
\]

不同prime bases只给两个排列；同一prime的collision总和由
\(\sum_p(\log p)^4\sum_{r\ge2}(r-1)^2p^{-r}<\infty\)
支付。原Montgomery–Vaughan inequality遂给任意长度O(X)的height interval J：

\[
\int_J|Q_Z(t)|^4dt
\ll (X+Z^2)\log^4(2Z).
\tag{18}
\]

在原AF finite compression中，令U_F z=Σ z_k f_k，f_k(t)=hat φ(t−α_k)，并置
F=U_F/√(2πL)。原critical frame给F*F≤1。低Λ矩阵为

\[
P_{\le Z}=\frac{2\pi}{a_LL}F^*M_{-\pi^{-1}\Re Q_Z}F.
\]

对F*MF的每个normalized eigenvector，用标量凸函数x⁴的Jensen（把缺失概率放在0），准确得到

\[
\operatorname{Tr}(F^*MF)^4
\le\operatorname{Tr}(F^*M^4F).
\tag{19}
\]

这里未使用错误的“x⁴ operator-convex”。critical discrete Parseval还精确给
\(\sum_{k\in\mathbb Z}|f_k(t)|^2=a_LL^2\)，故finite sum不超过它。

在扩大正height interval J内应用(18)；J外保留
\(|Q_Z|\ll\sqrt Z\)，用原C² Fourier尾及Σ_k∫_(Jc)|f_k|²≪d X^−3支付。于是

\[
\boxed{
\operatorname{Tr}P_{\le Z}^4
\ll N\left(\frac{\log(2Z)}L\right)^4
 \left(1+\frac{Z^2}X\right)
+\frac{Z^2}{X^2L^4}.}
\tag{20}
\]

原Λ系数、finite frame、sharp prime截断及低height峰均保留。取log Z=o(L)，例如Z=exp(√L)，得到unconditional \(\|P_{\le Z}\|_4=o(N^{1/4})\)。

若剩余完整Hermitian response H_>已另外证明\(\|H_>\|_4=O(N^{1/4})\)，非交换telescoping与Schatten Hölder给

\[
|\operatorname{Tr}(H_>+P_{\le Z})^4-\operatorname{Tr}H_>^4|=o(N).
\tag{21}
\]

式(21)联合保留背景、one-/two-/three-prime交叉项，不分别取绝对词预算。H_>的四范数是明确未支付前件，不从二矩或(16)推出。固定Z=X^ρ只给O(ρ⁴N)的粗预算，隐含常数没有优化，不能网格宣称可用的比例constant gain。

## 8. 全导子界可准入哪些实际factor

合法factor和费用：

| actual factor | 准入 | 必须支付的费用 |
|---|---|---|
| μ≤U的自然χ零延拓 | 规范1/L前缀，式(6)(7) | fixed σ−σ_0、完整q_eff、任意小height/conductor幂 |
| Λ>V与natural mask | D−D≤V，式(8)(9) | principal V^(1−σ)/(1+|height|)峰 |
| J_UV完整convolution | 精确式(4)，非任意a_n | ghost double pole、sharp Perron与actual cell BV |
| 固定finite-ray组合Σ cχ χ | 逐χ应用全q输入 | Σ|cχ|；不允许coefficients跟随同一内层row |
| 单一reduced AP 1_(n≡r mod q) | 1/φ(q)Σχ barχ(r)χ(n) | character系数ell1恰1；principal main除φ(q) |
| additive unit-group phase e(an/q) | 全χ展开 | 至多√φ(q)的ell1费；非单位项另付 |
| 原centered divisor kernel列T_r−T_(r+1) | 不自动准入 | divisibility跳跃、共同mask及完整actual variation |
| 经过a-sum后依赖b的误差 | 不再canonical | 本报告取denominator绝对和；新的signed平均须另证 |

全q界对moving natural masks与fixed outer labels一致成立；并不意味着已取得modulus-averaged相消。对Riemann zeta上述χ_b仅是principal punctured character；此处primitive全family输入并非额外制造了一次独立增益。

## 9. 余下determinant fiber的精确Type-II/相关映射

239–240的剩余对象仍为

\[
\Lambda^*B_X^{\rm cent}\Lambda
=\sum_{r,r'}\mu(r)\mu(r'){\cal K}_X(r,r'),
\]

其中B_X^cent已经保留six-window、finite-frequency核、全部denominator Λ、sharp masks及共同linear shell centering。换成Mu kernel本身没有新saving。

对原primitive factors(a,b)=1，固定determinant h=ad−bc，准确有

\[
d=d_0+b\ell,\qquad c=c_0+a\ell,\qquad
ad_0-bc_0=h.
\tag{22}
\]

因此h非零的原off-diagonal离散inner correlation为

\[
\sum_{\ell:\ c,d\in{\cal C}_Y}
\Lambda(d_0+b\ell)\Lambda(c_0+a\ell)
\,{\cal W}_{a,b,h}(\ell)
\,K_{XL,D}\!\left(X\log\frac{a(d_0+b\ell)}
                         {b(c_0+a\ell)}\right).
\tag{23}
\]

\({\cal W}\)含原平方根正规化、six-window及mask；primitive distinct atoms下h=0准确属于同atom reference，已按原式扣除。共同centering另扣239的明确linear density term，在physical quotient求和后施加，不改成逐fiber绝对预算。原Type-I/II coefficients可代入a,c，但(23)的另一个Λ不能改成任意有界测试后仍称canonical。

balanced a,b≈Y使每个固定h的ℓ区间只有O(1)个整数。核心尺度
\[
|h|\lesssim Y^2/X=X^{1/2}
\]
来自实际log-resolution；全部tail h及其carrier仍必须联合求和。无零条带不为(23)提供两个linear prime forms的joint asymptotic或signed band average。AP准入只控制一个canonical Λ，另一个Λ连同response权重不是固定finite-ray系数。

原finite band可以逐k拆成真实pure twistsτ_k≈X，因此式(12)的Type-I支付合法；但为达到o(L⁴)，至少还需跨b、divisor、h和k的response-specific相关估计，不能再分别取绝对值。有限affine mapping (22)(23)把余项定位为明确的prime-pair/Type-II correlation，而非“零区和比例独立”的泛泛判断。

## 10. 该接口自身的准确分辨阈值

固定r、w和其余factors后，Type-I canonical prime variablev长度为
N_v≈Y/(rw)≤CY。若只想用单变量D(s)移线在determinant core中解一个response cell，它的v-width是H_v≈N_v/X。Mellin amplitude H_v/N_v与frequency宽度N_v/H_v相消，明确[R]的logarithmic control只给error N_v^σ，主规模至多H_v。

因而该特定single-factor移线要有power-small relative error，要求

\[
N_v^{1-\theta}>X.
\tag{24}
\]

θ=7/8时要N_v>X^8，而实际N_v≤Y=X^(3/4)。若同时限制一个AP，主项还需除φ(q)，阈值只更严。很多实际core widths甚至小于1，不能用连续PNT主项代替整数fiber。

式(24)是本接口的充分saving门槛及当前失败的精确量化，不是“所有从7/8条带可能推出的相关估计都不可能”的绝对no-go。更强global reciprocal或稍微降低θ只微调指数；没有支付(23)的Type-II/dispersion接口。

## 11. 与公开方法的实际新颖性边界

primary核查：[AF v2 §7.2](https://arxiv.org/html/2608.13637v2#S7.SS2)已把higher moments定位到超出其二矩对角方法的prime correlations；[Montgomery–Vaughan原Hilbert inequality](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)提供本报告(18)使用的Dirichlet-polynomial mean-value机制。

因此(17)–(21)是经典short-polynomial付款及实际compression bookkeeping，不宣称新的公开analytic theorem。原Vaughan identity和(16a)的有限spacing/Schur付款也是经典机制。新工作限于本项目此前未支付的具体准入：保持其合法ghost extension、moving natural mask、six-window、finite-k及sharp cell，完整证明canonical Type-I generating function的ghost pole与height峰费用。式(16)弱于同域无条件(16a)，不据其相对最粗l1预算的改善宣称国际新颖性。

## 12. 下一步与结论

已证明的有限成果：

1. 真正非vacuous、保留自然mask的canonical Type-I convolution可用于原high-cell physical synthesis。
2. canonical contour得到actual I–I块O_ε(X^(21/16+ε))，仅相对最粗l1预算改善；同域finite-ratio Schur给全部I/II/Λ块更强的无条件O_ε(X^(1/2+ε))。两者仍远大于raw o(L⁴)，不替代physical Gram净相消。
3. 原低Λ≤exp(√L) full-compression块的Schatten–4范数为o(N^(1/4))；背景cross terms的统一稳定传递需要剩余完整response的四范数前件。
4. 全导子factor准入的系数常数、height峰、ghost pole及AP/additive费用均明确；实际余额精确映射为(23)的signed affine prime correlation。

真正下一算术任务是对(23)或其共同centered divisor pullback证明跨label联合预算，保留原finite band和physical vector。不能以(16)代替该目标、不能把canonical μ marked moments改成任意系数，也不能把各channel的absolute upper bounds当成完整Gram净saving。

另一代理twisted_research已只读独立核§4–6：核准shifted μ/Λ Perron后只作实权Abel、uniform U/V/q/height量词、double-pole及finite-height峰、natural-mask/BV下的Hilbert付款，未发现该有限lemma的实质错误；这不是对整个外部输入或剩余Type-II的验收。

2026-10-07全文独审续核§7–10后，准确化K_{XL,D}参数并补入(16a)基线；
审查和canonical theta更新的有限mixed推导分别保存于
`type-i-and-low-lambda-full-response-review.md`及`hybrid-finite-ratio-gram-baseline.md`。

没有得到新的简单临界线比例、固定四矩常数或RH结论。本次只新增本报告，不改math、旧notes、索引，不运行构建、提交或push。
