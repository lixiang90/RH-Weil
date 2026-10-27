# 585：cofinal Sonin固定源迹下界与实际core误差必要费

2026-10-28；C048，同G20261027／runtime1793085111／冻结0c4f。核固定bramble_trace原作者v2 Theorem6.2 lower及必要支链，原件SHA541098…；不主张本仓首次发现该外部下界。H0／weighted两独占推导、必要原件及独立逆审另存，root统一前件与轮数结算。本稿不消费同定理upper、6.4sharp、6.5单步或后章，也不是RH证明。

## 1. 实际新结论、源与quantifiers

沿560的物理 \(\mathscr H=L^2(\mathbb R,dy)\)、实位Sonin正交投影P及M=RanP。对 \(F_X=\{p\le X\}\)，置
\[
 B_X=\prod_{p\le X}(I-p^{-1/2}U_{\log p}),\quad
 \Pi_X=B_XP(PB_X^*B_XP|_M)^{-1}PB_X^*,
 \quad A_r=\int r(a)U_a\,da.
\]
有限X时B有界可逆但非酉；\(\Pi_X\) 是到 \(B_XM\) 的真实物理正交投影，完整Gram逆与全部returns保留。源是原physical \(r=e^{y/2}f\)，不是bare求值向量／receiver。Fourier \(\widehat r(s)=\int r(y)e^{-isy}dy\)，Mellin侧norm为dt/(2π)。

对**每个先固定**非零complex \(r\in C_c^\infty(\mathbb R)\)，令 \(k=\operatorname{ord}_0\widehat r<\infty\)。则存在 \(c_r>0,X_r\) 使
\[
 \boxed{t_X(r):=\operatorname{Tr}(A_r\Pi_XA_r^*)
 \ge c_r\frac{\sqrt X}{(\log X)^{2k+2}}\quad(X\ge X_r).}\tag{1}
\]
每个finite-X的ordinary trace／HS域使用531／560已付输入；(1)是此实际源在素数集合成长时的新lower，不从正迹合法性直接推出。常数与起点依r，不给改变源／窗／频率族上的uniform du/Dlog界。

## 2. 原共同向量：用足够弱的前件闭合

先固定a>1的双gap cosine Sonin空间K_a。Burnol固定原文给非零空间、completed entire与连续评价；math/0203120v7 Prop4.3允许除去completed函数的一个零。在s=1/2处Gamma非零，对任一非零函数有限次除零即得到raw评价非零。因此存在实际Hermitian Riesz向量 \(g=k_{a,0}\)，其临界线raw Mellin值 \(G_a(0)=\|g\|^2>0\)。不把一般“评价连续”误作“评价非零”。

因K_a⊂K_1，旧532的raw评价界给
\[
 |G_a(t)|\le\|g\|\,\|k_{1,t}\|
 \le C_g\sqrt{\log(2+|t|)}.
\]
原稿更强的未平滑raw \(O(1/t)\) 断言不在本稿消费；较弱旧界已足。取固定δ<log a及积分1的compact Gevrey2核ψ，具体bump支撑取[-δ/2,δ/2]，严格在(-δ,δ)内。实际dilation-Bochner卷积
\[
 g_0=\int\psi(v)U_vg\,dv,\quad
 H_0(t)=\widehat\psi(t)G_a(t)
\]
保物理与cosine双gap至少 \(ae^{-\delta}>1\)。其原点值不消，且
\[
 H_0(0)>0,\qquad |H_0(t)|\le C e^{-c\sqrt{|t|}}.
\]
每阶 \(g_j=\int\psi^{(j)}(v)U_vg\,dv\) 同属此固定大gap，raw Mellin为 \((it)^jH_0\)，并有
\[
 \|t^jH_0\|\le AB^j(j!)^2\|g\|.
\]
所以**所有有限多项式倍**均在同一个实际Sonin域，常数与X／degree／源无关。未对原evaluator的cutoff jump强施导数，也未交换未付的无界算子。

## 3. 有限Euler权与全多项式的集中费用

记 \(\ell=\log X,A=\sqrt X/\ell,D_X(t)=\prod_{p\le X}(1-p^{-1/2-it})\)，w_X=|D_X|²。原物理range为D_XM，非等距；试探norm始终是 \(\|D_XpH_0\|_{L^2(dt/(2\pi))}\)。

必要的uniform prime-sum来自标准VK原定理（固定2212.06867v1 Th1.1，cited，不重证或优化零自由区）。对扭曲 \(\Psi_t(y)=\sum_{n\le y}\Lambda(n)n^{-it}\) 取Perron高度 \(y^{B+2}\)、移至窄无零条带，唯一跨pole为1−it；核z=0不跨。系数绝对值Λn不依t，误差uniform于|t|≤y^B。再在y≥√X用2B、去高powers、分部求和；twist已在Ψ内，微分权不添|t|。得到仅需的B=2绝对误差
\[
 \sum_{p\le X}p^{-1/2-it}
 =\frac{2Ae^{-it\ell}}{1-2it}+o(A),\quad |t|\le X^2.
\]
高阶Euler log仅O(loglogX)，因而
\[
 \log w_X(t)=-4A\Re\frac{e^{-it\ell}}{1-2it}+o(A).
\]
此式没有对任意频高作relative误差断言。

取 \(J_X=[\pi/\ell-\ell^{-2},\pi/\ell+\ell^{-2}]\)。H0在J_X上有fixed正lower。正规Legendre展开对ALL complex多项式deg p<n给
\[
 |p(t)|^2\le Cn^2\ell^2[C\ell^2(1+|t|)]^{2n}\int_{J_X}|p(v)|^2dv.
\]
Gevrey矩经u=√|t|变换由 \(C^{n+1}\Gamma(4n+2)\) 控制，故
\[
 \int|pH_0|^2\le e^{C_1n\log(n+\ell)}I_p,
 \quad I_p=\int_{J_X}|pH_0|^2.
\]
固定小δ_r使 \(|\widehat r(t)|\ge c|t|^k\) 于|t|≤δ_r。J_X的权exponent至少(4−o1)A；在δ_r≤|t|≤X²至多 \(4A/\sqrt{1+4\delta_r^2}+o(A)\)，在|t|≤π/(2ℓ)至多o(A)。选
\[
 n=\lfloor c_{\delta_r}A/\ell\rfloor
 \asymp\sqrt X/(\log X)^2
\]
使矩费用指数小于固定权gap的一半，就对整个多项式空间统一排除这两个坏区。

|t|>X²不能套compact-frequency gap：用全线Euler \(w_X\le e^{(4+o1)A}\) 和Gevrey尾。因 \(n=O(\sqrt X/\ell^2)\)，该全尾的 \((1+|t|)^{2n}\) 可由一半 \(e^{-c\sqrt{|t|}}\) 吸收，余量 \(O(e^{-c'X})\) 对全部deg<n统一。于是 \(V_X=\{D_XpH_0:\deg p<n\}\) 的每个单位向量有1−o1质量在
\[
 \pi/(2\ell)\le|t|\le\delta_r.
\]
这里所有先fixed量和极限次序明确；未从单个好向量推出整个增长维数的集中。

## 4. 真实迹下界与完整K的必要费

D_X实轴无零、H0在J_X非零，故V_X真实维数恰为n。其按dt/(2π)的正交基在实际RanΠ_X内；有限正项求和合法，得到
\[
 t_X(r)\ge\sum_{j\le n}\|\widehat r v_j\|^2
 \ge c_r n\ell^{-2k}(1-o1),
\]
即(1)。不是由ambient diagonal形式迹或有限数值试验所得。

取 \(X_n=n+1/2,L_n=\frac12\log X_n\)，strict／inclusive素数集合精确同一。固定r时Q_W(r)和完整双pole值均为常数，560的已付全型精确重排为
\[
 \langle r,K_{L_n}r\rangle
 =t_{X_n}(r)-Q_W(r)+P_{pole}(r),
\]
\[
 P_{pole}(r)=2|\langle r,\cosh(y/2)\rangle|^2
             -2|\langle r,\sinh(y/2)\rangle|^2.
\]
所以对每个先fixed非零compact smooth r，最终
\[
 \boxed{\langle r,K_{L_n}r\rangle
 \ge c'_r\frac{e^{L_n}}{L_n^{2k+2}}\longrightarrow+\infty.}\tag{2}
\]
不删除双pole，不要求其矩零；所有自相关可见properpowers最终都包含，Γ/FP/contact按原完整规范。

对任意先fixedη>0，旧完整密度粗上界
\[
 \rho_{F_L}(s)\le(M_L/m_L)^2 C\log(2+|s|),\quad
 \log(M_L/m_L)^2=(4+o1)e^L/L
\]
与fixed r的Schwartz Fourier尾，给 \(|s|\ge e^{\eta e^L}\) 的完整ε配对绝对o(1)：例如 \(|\widehat r(s)|\le C_r(1+|s|)^{-2}\)，尾由 \(e^{O(e^L/L)}\log A_L\,A_L^{-3}\) 及有限prime的 \(O(e^L)A_L^{-3}\) 支付。Γ尾亦如此。因此(2)的正增长可保留于 \(|s|<e^{\eta e^{L_n}}\)，即 \(\Gamma\lesssim\eta e^{L_n}\) 的actual频段。常数依r、η；这不是ALLchanging-source算子小费，也不是固定零频峰结论。

## 5. 费用方向、强旧与停止

取任一固定非零正bump \(r_0\in C_c^\infty((-1,1))\)，其k=0、原du／Dlog范数固定，537给Q_W(r0)>0常数；(2)却给实际误差必要费至少 \(c e^{L_n}/L_n^2\)。所以正迹与误差需要以成长大数相消，不能将K_L在所有原fixed源上免费当作O(1)／o(1)。这不是Q负例；也没有证明K_L在每一L对所有源PSD。

旧560全H inverse下界的输入不是Sonin evaluator／Weil source，固定F两号与安全高频运输也不蕴含(1)–(2)。新付款是**actual cofinal fixed-source lower及同型core必要误差**；底层Burnol/VK/Gevrey等标准前件不单独记轮，不重计537／560。

局部瓶颈改变：该cofinal实际K必要费用不再未知，原源固定时也正发散。宏观独立Weil正号、同一非零primitive／整过滤／截面／mixedRR、全source coupling与Ξ仍未付；542＋555→557 whole leading4/5仍为负惯性UPPER。

此结果不排有费非有限秩、source-adapted、Γ-relative或其它独立signed修复；也不推出所有变动有限秩补偿失败。C048在此一轮止，不优化常数／sharp6.4或自动续6.5／§7。下一须先核这个新必要费如何改变真实signed比较的选择，不把已得lower、原norm或source标签重开成新合同。长期Goal完成门仍open。
