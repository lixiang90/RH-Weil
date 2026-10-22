# 578：素数幂／极点signed预算、Selberg正反联检与实际补偿缺口

2026-10-22；C041，同G20261014／冻结0c4f。用户要求沿577找不使用未知零点的独立signed估计。来源首门实际取得完整Selberg与PNT正负联检后，准入一完整研究轮。结果是一个具体候选充分包的反测及准确费用定位；没有证明经典RH，没有排除更精细的算术／Γ联合恒等式。

## 1. 同一完整目标与实际被付费用

固定577的物理源r=e^(u/2)f、Fourier约定hat r(t)=∫r(u)e^(-itu)du、全部complex源及原du／zero-extension Dlog。记
\[
 W_\zeta=W_\Gamma+H-P,\quad H=2\cosh(u/2)du,
 \quad P=\sum_{n=p^k\ge2}\Lambda(n)n^{-1/2}
                  (\delta_{\log n}+\delta_{-\log n}),
\]
\[
 G_R=W_\Gamma+\phi_R(H-P),\quad g_R=\widehat G_R,
 \quad q_R=(-g_R)_+,\quad c_R=\|q_R\|_\infty,
 \quad m_R=\|q_R\|_1/(2\pi).                              \tag{1}
\]
φ_R=φ(u/R)为577已固定的非负正型自相关窗；不调窗口或按未知零点选系数。Γ(t)=Re ψ(1/4+it/2)−logπ的完整FP、奇性及指定contact保持；Λ(p^k)=logp的所有proper powers及两个pole不删。R是算术截断，物理源半窗L与频高T另记。

577已经给正层V_R=G_R+K_R du，K_R=F⁻¹q_R，无新增δ。独立Γ协同μ_R的原du／Fourier-L¹均为O(R⁻²)。未付的是实际q_R，不是这一Γ小误差。对每个fixed L全部原complex源，仍只有已付比较
\[
 |Q_{V_R}(r)-Q_\zeta(r)|
 \le [D_L/R^2+\min(c_R,2Lm_R)]\|r\|_2^2,
 \qquad D_L\ll(1+L^2)e^L.                                \tag{2}
\]
本轮不能把其他正对象的norm或平均费代入这项修补。

## 2. 从原数据扣除PNT主项：完整signed恒等式

用Ψ(x)=Σ_{n≤x}Λ(n)区别于digamma。令
\[
 E(u)=\Psi(e^u)-e^u+1,\quad A(u)=e^{-u/2}E(u),\quad E(0)=0.
\]
正半轴上精确有(H−P)=e^(-u/2)du−e^(-u/2)dE。对所有实t，Stieltjes分部积分给
\[
 g_R(t)=\Gamma(t)+J_R(t)+S_R(t),                           \tag{3}
\]
\[
 J_R(t)=2\int_0^R\phi_R(u)e^{-u/2}\cos(tu)du\ge0,
\]
\[
 S_R(t)=2\int_0^R A(u)
 \left[\left(\frac{\phi'(u/R)}R-\frac{\phi(u/R)}2\right)\cos(tu)
                         -t\phi(u/R)\sin(tu)\right]du.
\]
上端φ_R的全部jets为0，下端E(0)=0，故无遗漏端点。若去掉定义中的+1，必须补回下端项，不能改有限部分。两个pole已分别进入扣主项与残余J_R，全部powers仍在E中。J_R是正型函数φ_R e^(-|u|/2)的Fourier变换，故确实非负；Γ+J_R却不自动处处非负。

令I_R=∫₀ᴿ|A|φ_R、I′_R=∫₀ᴿ|A||φ′(u/R)|。直接三角估计只给
\[
 |S_R(t)|\le2(|t|+1/2)I_R+2I'_R/R.                       \tag{4}
\]
旧294已核某个先固定a>0的PNT包络|Ψ(x)−x|≪x exp(−a√logx)，经此运输至多给一类增长upper I_R+I′_R≪1+exp(R/2−a√R)，常数依原输入；不取最新常数，也不扩大暂停的零自由区优化。实际窄窗可改善指数系数，仍未给方向或消失。这个upper不是实际q_R的必要lower。

即使**假设**经典全局平方根log²误差，(4)也只直接给O((1+|t|)(1+R)³)的upper。这里失败的是该绝对值运输；不能据此说平方根误差不能推出经典RH——经典全解析包中的全局平方根误差本来已是RH等价责任。169／299也已核过特定全尺度／单侧临界预算的等价强度，不将它们不同截断的定理硬搬到(1)。

在源端同样有真实费用：h=r*r*，h_e=(h(u)+h(−u))/2，
\[
 (\phi_R(H-P))(h)=2\int_0^R\phi_Re^{-u/2}h_e du
 +2\int_0^R A[(\phi'_R-\phi_R/2)h_e+\phi_Rh'_e]du.        \tag{5}
\]
用||h′_e||∞≤||r′||₂||r||₂支付的是H¹费用。固定窗调制r_T=e^(iTu)r₀保持原du范数，原Dlog范数平方仅为log(2+T)阶，导数费却为T阶；不能将(5)的三角估计当原du／Dlog统一费。返回原测度TV则恢复旧555／577的指数绝对预算，未得到signed小量。

## 3. Selberg及Euler平方实际控制哪一个对象

本轮唯一外部原件章节是[Selberg1949 §2，(2.8)](https://www.math.lsu.edu/~mahlburg/teaching/handouts/2014-7230/Selberg-ElemPNT1949.pdf)，印页307–310。原式为有序prime产品
\[
 \sum_{p\le X}(\log p)^2+\sum_{pq\le X}\log p\log q
                  =2X\log X+O(X).                        \tag{6}
\]
不能用它删去proper powers。由已付Chebyshev，线性补幂为O(√X log³(2X))=O(X)，卷积补幂至多
\[
 2\sum_{p^k\le X,k\ge2}\log p\,\Psi(X/p^k)
 \ll X\sum_{p,k\ge2}\log p/p^k\ll X.
\]
故全部幂的合法版本是
\[
 \sum_{n\le X}\Lambda(n)\log n
 +\sum_{mn\le X}\Lambda(m)\Lambda(n)=2X\log X+O(X).       \tag{7}
\]
这项真实独立预算仍不是(3)的signed估计。在Re s>1令U(s)=ΣΛ(n)n⁻ˢ，则
\[
 -U'(s)+U(s)^2=\zeta''(s)/\zeta(s).                      \tag{8}
\]
U²编码和频u+v／乘积；Hermitian |U|²编码差频u−v，二者不同。对有限D(t)=Σa_n e^(itlogn)，|D|²确实非负，却增加ratio频率、二次系数及contact Σa_n²；尚无它们与同一Γ、pole、线性P的预算身份。旧036已给乘积核与max-kernel逐系数不等的n=6反测，这个旧区别不重报为新定理。

正Euler／Toeplitz亦只给P_R(t)=2Σa_ncos(tlogn)的正核性质，a_n=Λ(n)n⁻¹ᐟ²φ(logn/R)≥0：
\[
 |P_R(t)|\le P_R(0),\qquad
 4P_R(t)\le3P_R(0)+P_R(2t).                              \tag{9}
\]
第二式由3−4cosθ+cos2θ≥0，方向正确但保留P_R(0)≪e^(R/2)大项。H_R也单独给正Toeplitz核；两正核之差不因此正。完整二阶矩的off-diagonal见平方分支；控制平均并不支付整个有效频高内的实际负部，更不能由有限网格推全t的c_R。

## 4. 同一真实continuous族：强PNT与完整Selberg总量正负皆过

这里使用562已证明的正primitive／全Π／正g-integers族，不只验证某个形式密度：
\[
 Z_c(s)=1+\frac c{s(s-1)},\quad 0<c\le1/2,
 \qquad \alpha+\beta=1,\quad\alpha\beta=c.
\]
它的native Γ=0、完整pole为0和1，E_c=s(s−1)Z_c精确自对偶。全部prime-power Chebyshev log密度为
\[
 v_c(u)=e^u+1-e^{\alpha u}-e^{\beta u}\ge0,\quad
 \Psi_c(e^U)=e^U-1+U-
 \frac{e^{\alpha U}-1}{\alpha}-\frac{e^{\beta U}-1}{\beta}. \tag{10}
\]
取正例c₊=5/16，α,β=1/2±i/4；负例c₋=3/16，α=3/4、β=1/4。正负两例均有真正positive primitive和全部Euler repeats，完整Weil分别为
\[
 W_+=2\cos(u/4)du,\qquad W_-=2\cosh(u/4)du.              \tag{11}
\]
这是从完整分布相消得到，未用未知零点选系数。

令b=max(Reα,Reβ)<1，d(u)=1−e^(αu)−e^(βu)，则|d(u)|≤C_c e^(bu)。由(10)，Ψ_c(x)=x+O_c(x^b+logx)，所以两例都满足每个预先固定a>0的O_{c,a}(x exp(−a√logx))误差。常数不在c变化下冒称统一。

更强的本次联检是两例也都过(7)同型总量。半线卷积直接算得
\[
 u v_c+(v_c*v_c)
 =2u e^u+2e^u\int_0^u e^{-v}d(v)dv+u d+(d*d)
 =2u e^u+O_c(e^u)+O_c(u e^{bu}).
\]
因此对全部X≥1，
\[
 \boxed{\int_0^{\log X}[u v_c(u)+(v_c*v_c)(u)]du
                    =2X\log X+O_c(X).}                  \tag{12}
\]
两个被积块本身都非负。另可从U_c=1/(s−1)+1/s−1/(s−α)−1/(s−β)及−U′_c+U_c²=Z″_c/Z_c交叉核：s=1二阶主部2/(s−1)²，其余极点实部<1。重根c=1/4只增加多项式×e^(u/2)，不改主项。

正例φ_RW₊正型，hard q_R=0。负例则在原物理源上确实不能付费：取非零非负偶η₀∈C_c∞，r₁=(D²−1/4)η₀，r₋=r₁−τ_h r₁，h≠0，τ_h r(u)=r(u−h)。两矩∫r₋e^(±u/2)du精确为0。记a=1/4，A₀=(a²−1/4)∫η₀e^(au)du≠0，则
\[
 Q_-(r_-)=2A_0^2(1-e^{ah})(1-e^{-ah})<0.                 \tag{13}
\]
正修补及固定源收敛迫
\[
 \liminf_R Q_{K_R}(r_-)\ge-Q_-(r_-)>0,
\]
并给liminf c_R≥−Q₋(r₋)/||r₋||₂²、liminf m_R≥−Q₋(r₋)/||r₋||₁²的原费用lower。此源不是经典405主关系，而是本模型的实际双polezero测试，不能混用角色。Γ=0模型的q_R可L¹但不声称有限频高支撑。

因此“positive primitive／g-integers＋精确对偶与双pole＋该强PNT＋ordinary Selberg O(X)总量”不是一般g系统中付完整Weil正号／修补消失的充分包。本次新增消费限这项具体联检；旧562模型本身及旧036区别已扣除。**没有把Γ=0反例冒充保经典Γ的反例**，也不排比(7)更精细的完整卷积／twist／Γ协同。

## 5. 真函数域：保全部returns的正号从哪里来

真曲线C/F_q的native周期pole、contact及全部returns保留，ℓ=logq：
\[
 W_C=\ell\sum_{n\in\mathbb Z}a_n\delta_{n\ell},\quad
 a_n=q^{-n/2}(q^n+1-N_n)\ (n>0),\quad a_{-n}=a_n,\quad a_0=2g.
\]
563／567已从同一对象的点数递推／RR、Hodge index给全Gram或U*HU=H。于是全部complex源的全alias平方和为
\[
 Q_{W_C}(r)=\ell\int_0^\ell
 \left\|\sum_j r(y+j\ell)E_{j+j_0}\right\|^2dy\ge0,      \tag{14}
\]
支撑只令本源求和有限，不删全分布returns。故φ_RW_C正型、hard修补0。正号来自同对象primitive交数／极化及trace身份，不是closed-place系数非负，也不是Selberg乘法平方。

不能把连续实x的无周期PNT／(12)字面强加函数域；native lattice的全部pole aliases须共同处理。也不能给该模型外加经典Γ改目标。真正有效的推广须搬运(14)所需的同源比较与容量，而非只搬点数误差的大小。

## 6. 405全关系、537及拓扑／成长责任

经典(3)、(5)、(7)均未改变405的actual noncompact p=(D²−1/4)H₀及全部固定平移；它们属于S_exp，完整Bζ(p,s)=0。577各V_R仍有高频严格正连续谱，故Q_{V_R}(p)>0，逐层exact商继续失败。每固定强源裸层有已付O(R⁻²)尾；还要另付实际c_R／m_R才谈近似关系。用compact交集检查Pan没有内容。

537原L₀=17/16窗全部complex原源仍无条件最终满足Q_{V_R}≥(τ−D_L₀/R²)||r||₂²；它保非根可见性，不给成长窗新正性。连续反测亦未否定这一经典旧固定窗结论。

G_R→Wζ于D′无条件；正层V_R是否趋同一目标仍欠K_R。对577特定family，c_R→0、m_R→0、K_R→0于D′仍各等价完整Weil正性／RH。D′不一般控制norm；该特定逆向依完整身份与RH。fixed窗误差只能用(2)，L=L(R)成长须同时支付D_L/R²及实际修补，不能由固定源／平均频高结论交换量词。全线Hlog统一目标差每层∞和Pan稠密障碍按553／577保持。

## 7. 新旧净值与停止

实际新增为本次对候选充分包的完整同族Selberg／强PNT联检及实际双polezero费用反测；全部算术signed重写和平方／原norm运输责任已显式核清。旧036、169、294、299、562、577的恒等式／模型／等价／费用准确扣除；没有新增经典signed小量、全源成长范围或whole结果。

strong-old542＋555→557 whole leading4/5仍为负惯性上预算，非负谱lower。独立容量、actual core／coupling／Ξ及长期Goal门未改。C041只统一一轮，不按三分支／来源／fresh计轮。

若把尚需的S_R≥−Γ−J_R−ε_R、ε_R原费用消失当定义，便回到577的RH等价条件；本轮在这里停止。不续PNT绝对包络／ordinary Selberg／Toeplitz／二阶矩参数，不串下一paper。重新准入须交实际独立twisted／signed身份和完整原费用，或同对象source→sections／primitiveRR实物。保joint、非局部、源适应、强拓扑／变域及有费无限修补；这个候选包失败不构成整个方法类的宏观完成边界。

原证明分支：[累计误差／原费](../reviews/2026-10-22/prime-pole-signed-admission/cumulative-error-and-original-cost.md)、[平方／对照](../reviews/2026-10-22/prime-pole-signed-admission/square-identities-and-controls.md)、[历史／Selberg来源](../reviews/2026-10-22/prime-pole-signed-admission/history-and-source-admission.md)。
