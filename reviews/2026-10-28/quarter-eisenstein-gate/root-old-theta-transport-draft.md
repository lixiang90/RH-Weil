# Quarter packet的旧theta运输与threshold账本

2026-10-28；同Goal1793085111/原0c4f。Root已实际全文读545、C016和原whole-frequency稿§§8–9的必要段，并收到两个current具体咨询的独立运输／threshold核算。以下把旧exact公式的这一次应用写全，待两终稿与current fresh／root结算；不是C053、新来源或第590号。若下述延拓／尾未闭，结论保持未消费，不能仅凭Eisenstein标题称旧0。

## 1. 输入变换确在旧whole-L²域内

记s_t=1/4+it/2、Z(s)=π^(-s/2)Γ(s/2)ζ(s)，E*=Z(2s)E。545已经固定同一s_t。其pole-cleared family F_Y=s(s−1)Λ^Y E*给whole-L²源的HS map A_Y。

令qhat(t)=F_r(t)/[s_t(s_t−1)]。分母在real t无零，inverse是bounded O((1+t²)^−1)乘子，故q∈L²，即使q不compact。A_Yq在y≤Y处就是当前literal V_r。**G_Y是restriction norm，不是整个Λ^Y packet norm**；两者差y>Y的非constant Fourier modes能量，不能漏掉。

另一个更强旧表示由E*函数方程直接给出

\[
 E^*(z,s_t)=b(t)E(z,3/4-it/2),\qquad b(t)=Z(3/2-it).
\]

令hhat=F_r b。旧545 direct T_Y的whole-L² bound适用h，保full mixed项和原2π；不需要以critical ξ作除法，也不涉及未知零点位置。这里不将h冒作旧fixed-L compact源。

## 2. 旧theta核使新输入尾明确，而非一个未付norm

由Res>1的Mellin积分，b的inverse Fourier kernel为

\[
 k(u)=2e^{3u/2}\sum_{n\ge1}e^{-\pi n^2e^{2u}},\qquad h=r*k.
\]

k∈Schwartz，因Jacobi反演，u→−∞时

\[
 h(u)=\mu_-(r)e^{u/2}-\mu_{-3/2}(r)e^{3u/2}
       +O_r(\operatorname{poly}(e^{-u})e^{-c_re^{-2u}}),
\]

u→+∞为fixed幂乘superexponential小量。此处μ_a(r)=∫e^(au)r(u)du，μ_±=μ_(±1/2)。源r的支撑先固定，常数允许依r。故h∈L²且weighted polar integral ∫h e^(u/2)绝对收敛，但μ_-≠0时h不在旧uniform-Y的compact/fixed-L前件里。

令g_h(y)=y^(3/4)h(−logy/2)，则

\[
 g_h(y)=\mu_-(r)\sqrt y-\mu_{-3/2}(r)
        +O_r(\operatorname{poly}(y)e^{-c_ry})\quad(y\to\infty),
\]

而y↓0时g_h(y)=poly(y)e^(-c_r/y)。旧545 incomplete-Eisenstein的polar系数准确为

\[
 \frac6\pi\int h(u)e^{u/2}du
 =\frac6\pi F_r(i/2)Z(2)=\mu_+(r),\qquad Z(2)=\pi/6.
\]

## 3. 旧incomplete式的合法局部延拓

取0≤χ_N≤1的compact smooth截断h_N=χ_Nh。由h的Schwartz尾，h_N→h于L²；545全L² fixed-Y bound给T_Yh_N→T_Yh。Polar integral也由上述weighted可积性收敛。

对每fixed compact-height domain，g_h在小y的superexponential decay给Poincaré coset sum的一致domination，因此Θg_hN→Θg_h于该域的L²／局部一致意义。545原式由此延到本h，得到局部真实等式

\[
 V_r(z)=\Theta g_h(z)-\mu_+(r),\qquad
 \Theta g(z)=\sum_{\Gamma_\infty\backslash\Gamma}g(\Im\gamma z).
\]

没有将未截断V_r先假定为全L²向量。它事实上通常不是。

在cusp y→∞，identity coset给g_h(y)。其余c≥1时v=Imγz=y/|cz+d|²，故1/v≥c²y+(cx+d)²/y。以小v的poly(v)e^(-c_r/v)界，先对d作Gaussian求和再对c求和，得非identity总量O_r(poly(y)e^(-c'_ry))，uniform x∈[-1/2,1/2]。于是

\[
 V_r(x+iy)=\mu_-(r)\sqrt y
           -\mu_{-3/2}(r)-\mu_+(r)
           +O_r(\operatorname{poly}(y)e^{-c'_ry}).\tag{1}
\]

这也独立解释unitary contour上F_r(t−i/2)Z(1+it)的1/t threshold：E*(1/2)在每个z点可去，不代表其uncompleted spectral coefficient是L²。该系数在零点的可积性需要μ_-(r)=0。

## 4. 全Y而非fixed-Y的实际test

把(1)相乘并以dxdy/y²积分。leading项只为μ_-(r)overline(μ_-(s))/y，其余cross／constant／tail均绝对可积。因此对每对先fixed complex smooth compact源，

\[
 G_Y(r,s)=\mu_-(r)\overline{\mu_-(s)}\log Y+O_{r,s}(1).
 \tag{2}
\]

μ_-≠0时ordinary geometric norm对Y增长log；μ_-=0时V_r实际属于全L²，G_Y[r]有finite极限。不是从旧√Y粗界推出来，也不是把旧fixed-L界偷套非compact h。

r₀为原fixed正bump，μ_-(r₀)>0，故G_Y[r₀]>0最终成立。令α_Y=q₀/G_Y[r₀]，则全部fixed源对有

\[
 \alpha_YG_Y(r,s)\to
 \frac{q_0}{|\mu_-(r_0)|^2}\mu_-(r)\overline{\mu_-(s)}.
\]

任意source-independent positive β_Y若β_YG_Y[r₀]→q₀，也得同一结论。取r_*=(D²−1/4)r₀，非零、support[-1,1]且μ_±(r_*)=0；537原完整型Q_W[r_*]≥κ||r_*||du²>0。因此normalized geometric Gram在这个fixed source为0，完整目标缺陷趋Q_W[r_*]。原Γ/contact/全部properpowers/双pole没有被替换或删掉。

此rank1是一个**pole-coordinate**，不同于589的mean rank1。Finite-Y一般不stationary，也不自动是单变量正D′；其对完整目标的fixed-form必要test已经失败。

## 5. 最强旧净值与停止范围

Quarter参数、完整MS／Gram、completion、direct whole-L²运输、incomplete式／polar系数均为545已付。新增literal去p只需bounded输入乘子；threshold尾由旧FE＋Res>1 theta核及Jacobi明确算出，局部延拓／cusp求和是这些exact公式的标准旧组合。本记录支付这次应用的全部域和量词，不能把“以前未写同一符号”算成新独立输入或再消费545数学轮。

这是old0准入比较的拟结算，不改变latest589/cadence3/history53/formal17。它拒绝当前保留cusp再scalar校准的明确族，不是所有几何／unbounded frequency权／非紧新修复／joint signed方法边界。完整cusp扣费后的compact source map仍属545旧scope，不能把finitepart正性当免费新input。无新source、web、下载、数值或C053预算。

通过current两个终稿／fresh后停止此packet/规范，不换s／r／Y或读下一章来续。原Goal完成门、完整signed/corecoupling、非零primitive/principal/mixed及whole4/5UPPER仍未改。
