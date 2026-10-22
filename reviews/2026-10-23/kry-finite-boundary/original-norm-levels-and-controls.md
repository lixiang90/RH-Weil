# KRY有限位—边界源：原norm、无限level与正反控制

2026-10-23；独立分支 `/root/finite_family_norms_controls_580`。供root核查，不自行结算合同或计轮。以下明确检验一条非标量公式，不把它升级为已存在的相对primitive循环：有限位取嵌套球／shell，arch投影系数为Gaussian平移相关。主实际实例固定KRY的 `k=Q(√−7)`、split位p=2、`ℓ=2log2`，对应有限缩放 `1_{2^jO}` 与原件的参数 `2^{2j}τ`；一般p／ℓ公式用于交叉核规范及合法逃逸。除非另证cycle/height运输，费用均属于指定Schwartz/Hilbert对象。

## 1. 对象、旧资产与本次可改变选择的门

物理源仍为全complex `r=e^{u/2}f∈S_exp`，原norm是du和全线零延拓

\[
 \|r\|_{Hlog}^2=(2\pi)^{-1}\int[1+\log(2+|t|)]|\widehat r(t)|^2dt.
\]

固定579实际Gaussian `φ*`、Haar及 `ν=||φ*||²`；设 `s(u)=sech(u/2)`，`\hat s(t)=2πsech(πt)`。不把raw Gaussian宽度或有限位体积当作可调完成化。405全Pan及全部平移、537固定17/16全complex非根分别验收；不能只检compact主关系的空交。

去重已核579、553、545及056：579已付单Gaussian/标量源、原du费和finiteEuler mixed；553全Pan稠密的bounded读出零是旧后果；545有不同modular-packet的无限盲空间；056的Poisson sampling用于不同Dirichlet多项式。这里不重复计它们。新增具体检验是**本条finite-lattice系数的实际Gram、精确全level alias盲源及有限位origin边界在Hilbert完成中的丢失**，而非再次命名未知primitive map。

## 2. 有限位实际Gram与全部mixed费用

设k为虚二次域，p为有理素数，p处取 `vol(O_{k,p})=1`；即便p分裂，k_p仍为Q_p的总维数2，所以

\[
 \psi_j=1_{p^jO_{k,p}},\quad
 \langle\psi_j,\psi_k\rangle=p^{-2\max(j,k)},\quad
 \varphi_j=p^j\psi_j,\quad
 \langle\varphi_j,\varphi_k\rangle=\rho^{|j-k|},\quad\rho=p^{-1}.
                                                        \tag{1}
\]

对任意有限整数level集合和任意complex系数a，Poisson核的正Fourier密度直接给

\[
 {1-\rho\over1+\rho}\sum|a_j|^2
 \le\Big\|\sum a_j\varphi_j\Big\|^2
 \le{1+\rho\over1-\rho}\sum|a_j|^2.                 \tag{2}
\]

这是实际finite Haar下的Riesz比较，不是自由替换原targetnorm。未单位化时须代 `a_j=p^{-j}b_j`。shells

\[
 h_j={\varphi_j-\rho\varphi_{j+1}\over\sqrt{1-\rho^2}}
     ={p^j(\psi_j-\psi_{j+1})\over\sqrt{1-\rho^2}}
                                                        \tag{3}
\]

支持互不相交，才是真正正交规范。将球差分错写成单位系数正交差分会遗漏ρ及相应费用。

现在固定ℓ>0，定义实际源

\[
 \Phi_N(r)=\sum_{j=0}^N T_*(\tau_{-j\ell}r)\otimes\varphi_j,
 \qquad c_j(r)=\int r(u)s(u-j\ell)du.                 \tag{4}
\]

degree2全局有理伸缩的几何步长为 `2log p`（方向按有限位伸缩约定反转）；下面分析也可单独检 `log p`，不能未经全局校准就声称二者是同一adelic action。投native weight1后的实际向量为

\[
 P_1\Phi_N(r)=\phi_*\otimes\sum_{j=0}^Nc_j(r)\varphi_j.
                                                        \tag{5}
\]

未投影源的完整mixed原费用是

\[
 \|\Phi_N(r)\|^2={1\over2\pi}\int
 2\pi\nu\operatorname{sech}(\pi t)|\widehat r(t)|^2
 \Big\|\sum_{j=0}^Ne^{-ij\ell t}\varphi_j\Big\|^2dt. \tag{6}
\]

因此对每个非零实际r，(2)给

\[
 {1-\rho\over1+\rho}(N+1)\|T_*r\|^2
 \le\|\Phi_N(r)\|^2
 \le{1+\rho\over1-\rho}(N+1)\|T_*r\|^2.             \tag{7}
\]

这是固定actual源的native Hilbert lift费用，非全空间norm lower冒充实际源费用。若改用ψ_j，则(6)中的向量也必须改ψ_j；正levels的 `Σp^{-2j}`可付全Hilbert upper，但不能把其收敛等同Schwartz或cycle拓展。

投影(5)有不同费用。Poisson分组和Cauchy–Schwarz给

\[
 \sum_{j\in\mathbb Z}|c_j(r)|^2\le A_\ell\|r\|_{du}^2,
 \quad A_\ell={1\over\ell}\sup_{|t|\le\pi/\ell}
 \sum_{k\in\mathbb Z}|2\pi\operatorname{sech}(\pi(t+2\pi k/\ell))|^2<\infty.
                                                        \tag{8}
\]

故(5)对全整数levels都有统一 `ν(1+ρ)/(1−ρ) A_ℓ` squared du upper，Hlog亦然。此与(7)无矛盾：native投影丢了大量原Schwartz信息。费用只付Gaussian⊗finite-Hilbert，不付Schwartz半范数、算术degree、Green或primitive height。

## 3. 405／537：向量确有收益，但有限rank仍不过全门

405实际正H给 `p=(D²−1/4)H`。所有a,j都有

\[
 c_j(\tau_ap)=-\tfrac12\int H(v)s^3(v+a-j\ell)dv<0. \tag{9}
\]

这里`s^3(x)=sech³(x/2)`，没有裁掉noncompact尾。于是raw向量仍保Pan，而不成为已证principal同构。任意有限distinct levels的Pan轨道值向量张成全部系数空间：若 `Σλ_j c_j(τ_ap)=0` 对全部a成立，Fourier唯一性给

\[
 \widehat p(t)\,2\pi\operatorname{sech}(\pi t)
                  \sum_j\lambda_je^{ij\ell t}=0.
\]

405的整个Mellin函数不恒零，实线零集测度零，有限指数多项式只能全零。因此，**固定有限channel后的线性relative投影若消全Pan，就杀全部channel像**；不用norm、未知零点位置或正性假设。它不排源依赖/非线性frames、变化domain或没有经这些系数的边界项。

非标量化的真实小收益也必须保留。579同一 `ψ(u)=uφ_even(u)`、`r*=(D²−1/4)ψ` 满足双pole-zero，`c_0=0`，但每个j>0有

\[
 c_j(r*)=-\tfrac12\int_0^\infty u\phi(u)
 [s^3(u-j\ell)-s^3(u+j\ell)]du<0,
 \qquad c_{-j}=-c_j.                                  \tag{10}
\]

所以增加一个实际finite channel确实救回579那个特定537漏失源；不能再将其误报为仍只经c_0。可是任意有限N的(5)仍漏537全窗：取窗内N+2个不交bump ψ_l，解N+1条 `c_j((D²−1/4)Σb_lψ_l)=0`，可得非零compact r。双pole矩由D²−1/4精确为零，537给完整Qζ(r)>0。这是源先由显式kernels选出，不用Q或零点标签。

## 4. 无限单格的精确alias盲源，并保完整Γ／all powers／poles

全整数level不是自动全源覆盖。这里取**实际步长ℓ=2log2**；对任意整数K≥1，令

\[
 A=K\pi/\ell,\quad g_A(u)=e^{-u^2}\sin(Au),\quad
 r_A(u)={g_A(u+i\pi)+g_A(u-i\pi)\over4\pi}.
                                                        \tag{11}
\]

两项之和为实奇Gaussian-trigonometric函数，属于S_exp。整函数移线的Fourier公式给

\[
 \widehat r_A(t)={\cosh\pi t\over2\pi}\widehat g_A(t),
 \quad r_A*s=g_A,
 \quad c_j(r_A)=g_A(j\ell)=0\quad(\forall j\in\mathbb Z).
                                                        \tag{12}
\]

同时 `cosh(±iπ/2)=0` 精确给 `μ_±(r_A)=0`。归一化掉非必要的巨大整体系数后，同一源可明确写成

\[
 R_A(u)=e^{-u^2}
 [\sin((A+2\pi)u)+e^{-2\pi A}\sin((A-2\pi)u)].       \tag{13}
\]

它仍满足所有(12)及双pole-zero，且

\[
 \|R_A\|_{du}^2\longrightarrow\tfrac12\sqrt{\pi/2}>0,
 \qquad\|R_A\|_{Hlog}^2=(\log A)\|R_A\|^2+O(1).     \tag{14}
\]

这次还可独立证明实际非根，而不只给一个nonzero raw标签。实际完整
`Γ(t)=Re ψ(1/4+it/2)−logπ` 在Gaussian频包 `±(A+2π)` 上给

\[
 Q_\Gamma(R_A)=(\log A)\|R_A\|^2+O(1).              \tag{15}
\]

所有proper powers按原Λ(n)保留。其自相关满足

\[
 |h_{R_A}(v)|\le4\sqrt{\pi/2}\,e^{-v^2/2},
 \quad |P(R_A)|\le8\sqrt{\pi/2}
 \sum_{n\ge2}{\log n\over\sqrt n}e^{-(\log n)^2/2}<\infty,
                                                        \tag{16}
\]

一致于A≥0，仅用 `0≤Λ(n)≤log n`。双pole恰为零，非删定义。因此

\[
 \boxed{Q_\zeta(R_A)=(\log A)\|R_A\|^2+O(1)>0
        \quad\text{对所有充分大整数K}.}               \tag{17}
\]

这不是用未知Weil正性或零点来选K。完整Γ连同其FP/contact按原Fourier multiplier消费，未只保渐近背景；渐近仅用于已合法原form在具体源上的估计。所有无限prime tail已由(16)付款，pole由矩精确计算。新反测是该**无限单格native-vector family**的非compact全源盲区，早于算术二次容量。canonical boundary／pole补偿若只读所有c_j与μ±，亦无法区分R_A与零源；任何由它们构造且在零源为零的relative链仍看不见R_A。它没有排更丰富boundary、continuous relative数据或直接从r读入别的信息。

量词要准确：这不表示无限单格也漏537固定compact窗。相反，若r compact且所有j≥0的c_j为零，定义

\[
 F(z)=2\int r(u)e^{u/2}(1+ze^u)^{-1}du.
\]

F在0附近解析，j充分大时 `c_j=e^{-jℓ/2}F(e^{-jℓ})`。零点聚于0迫F恒零，全部正指数矩消失；换元x=e^u并用compact区间上的多项式稠密性给r=0。故无限levels确能补finite-rank的compact覆盖；(11)–(17)精准区分全S_exp及fixed窗，不能合并。

## 5. 两个不相称prime步长：保覆盖的代价必须在actual向量核算

若允许两独立prime的所有正负levels，`a_{jk}=jℓ_p+kℓ_q`稠密，c(a)的连续性和convolution注入性使所有c(a_jk)=0迫r=0，故单格盲源不是全位no-go。不同prime的log比不是有理数，不能误称所有finite-prime grids都commensurate；本反测只含一个基本步长的整格。

但两个单位化finite格的actual Gram为

\[
 G_{(j,k),(j',k')}=\rho_p^{|j-j'|}\rho_q^{|k-k'|}.
\]

其Riesz下界为两个(2)下界的乘积。对任意先固定非零r，c(a)在某个区间绝对值≥δ>0；该区间含无限个distinct a_jk。因此该**无衰减权**全level投影向量的实际norm由 `Σ_{j,k}|c(a_jk)|²` 发散，而原du/Hlog(r)有限。此为一个固定actual源的费用，不是用ambient operator norm作必要费。

衰减权、单边levels、非Hilbert/强拓扑、源适应frames或别的有限位基均可能绕过；不能将本差别提升为所有算术source的必要lower。新的权须有实际cycle、principal与height/预算身份，不能把可选择正权本身当独立Weil输入。

## 6. 相对边界与Hilbert完成：哪个电荷真的被支付

正level的最便宜边界反测是

\[
 \sum_{j=0}^N(\psi_j-\psi_{j+1})=\psi_0-\psi_{N+1},
 \quad\|\psi_{N+1}\|^2=p^{-2N-2}\to0.              \tag{18}
\]

所以它在finite Hilbert中趋ψ0，但每个有限和在origin为0，ψ0(0)=1。actual诱导section的identity读出是 `λ(φ)(1)=φ(0)`；这个边界没有随小Hilbert尾支付。Schwartz–Bruhat拓扑中origin evaluation连续，故(18)不在Schwartz中收敛。不能凭L²的无尾费宣布KRY循环/constant term/相对frame已望远镜闭合。

更一般地，`Σ_j T_*(τ_{−jℓ}r)⊗ψ_j` 在正levels可能有Hilbert极限，但在finite valuation=j层相邻值的差是非零 `T_*(τ_{−(j+1)ℓ}r)`，因此没有统一finite level的局部常值；非零r时不属于原restricted Schwartz空间。即使另造更大空间，也须重新证明λ、E′、Green和cycle身份及原费用，不能当原定理的合法输入。

系数层的相对差分也不能只看charge。令 `b_j=c_j(r)−c_{j+1}(r)`。S_exp给c_j指数衰减，所以双侧charge `Σ_j b_j=0` 对**所有源**都成立，而b_j(p)通常不零；仅取总charge便同时杀非根。反方向若要求 `c_j=B_j−B_{j+1}` 且B在两端为0，则必要 `Σc_j=0`。405由(9)给每个c_j<0、绝对可和，从而 `Σc_j<0`，首门即失败。允许非零端frame可以补电荷，但必须保它的实际boundary值、norm与principal identity，不得按定义把它消掉。

## 7. 连续正反例、真函数域与二次容量

采用579同一奇compact源r*，`d=±1/16` 的真实连续positive-primitive族具有同双pole与nativeΓ=0，完整Weil值异号非零。上面所有Gaussian/finite Gram及c_j(r*)在两段相同；(10)虽修复c0漏失，却不从这些共同positive Hilbert费用中产生distribution-sensitive signed号。未构造连续族到CM cycles的运输，故不称它们满足或反驳KRY。它们只拒绝“通用positive lattice能量即完整W”的未经证明身份。

真FF仍按567在**同一**C×C上取

\[
 E_n=q^{-n/2}(\Gamma_n-F_1-q^nF_2),\qquad
 -E_mE_n=a_{n-m}=q^{-|n-m|/2}(q^{|n-m|}+1-N_{|n-m|}),
 \quad a_0=2g.                                         \tag{19}
\]

Hodge负性由同对象RR、实际截面乘法及固定有限容量给出。完整source是

\[
 Q_C(r)=(\log q)\int_0^{\log q}
       \big\|\sum_jr(y+j\log q)E_{j+j_0}\big\|^2dy,
                                                        \tag{20}
\]

这里先对compact源按567取统一j_0使所有活跃j+j_0≥0；全部Gram只依指标差，所以不改变源型。全S_exp须由已证Toeplitz型的独立完成另行消费，不假造负Frobenius图。保全returns/aliases与H⁰/H²的pole扣除。finite-local Gaussian Gram `ρ^{|j−k|}`有全rank的Poisson连续圆周谱，不能当成(19)这个依同一点数数据而来的有限维primitive交数。其ρ依finite体积而非N_n；degree-zero/shell归一化不提供该运输。同对象mixed交数/实际source比较与RR容量仍是独立新输入，不能由(1)正号或线性degree预算代付。

## 8. 消费范围与下一准入

已付对象：指定finite格/壳的actual Gram，raw与native投影的不同mixed原费用；有限向量救回一个579漏失源但不覆盖全部537；全单格实际alias非根及完整Γ/allpowers/pole估计；dense双格的指定无权源费用；Hilbert telescoping实际丢origin边界的反测。不是新Weil正性或KRY循环capacity定理。

仍欠：不经这些采样系数的实际relative边界，或有算术来源的非整格/有权family；全Pan的principal同构而不是定义商；537及全S_exp非根可见性；同一整模型上局部过滤、primitive mixed交数与二次RR容量；完整KRY signed解卷积到Qζ的同源身份及原du/Hlog量词。所有有关无限cycle/height身份均open，不能从合法Schwartz前缀推出。

553的bounded-quotient零仍是旧输入，不另计新no-go；strong-old542+555→557 whole leading4/5负惯性上预算、actualq、成长core/coupling/Ξ均未改变。本recipe的单格有限/无限及无权dense修复在此有精确范围，保源依赖frames、付费强拓扑和新relative公式等逃逸。是否准入统一数学轮由root/fresh核对整体后决定。
