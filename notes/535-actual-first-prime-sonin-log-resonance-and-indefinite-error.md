# 真实首素数 Sonin 误差的对数共振与无限正负指数

2026-10-14；C007第一轮，起始HEADbbbd54c，长期比較基线仍为3a72930。
状态：proved，范围为真实单prime正来源的无费用比较与冻结连续源域。
证明由[独立符号推导](../reviews/2026-10-14/c007-sign/direct-sign-audit.md)、
[来源/源谱审查](../reviews/2026-10-14/c007-sign/source-sign-audit.md)、
[主迹域证明](../reviews/2026-10-14/c007-sign/trace-domain-proof.md)及
[不同组织逆审](../reviews/2026-10-14/c007-sign/reverse-sign-audit.md)核对。
未证明完整Weil型负值、RH、实际最低态或成长S预算；不声称世界优先权/外部评议。

## 1. 同一完整实际对象及结论

保留C004以来 `a=log2,b=log(3/2)/4,μ=13/5`，两patch中心±a/2，
每个patch满足ℓ₀=ℓ₁/₂=0。V为这些光滑源在原L²支持U中的闭包。
完整pole项严格零，actual primepower相关只有p=2。
[532](532-actual-sonin-prime-symbol-and-compact-weil-bridge.md)已给

\[
 Q_W(g)-T_2(g)=-E_2(g),\qquad E_{2,V}\text{ 是自伴紧源算子}.
\]

T₂为真实正交Sonin投影P₂的正迹，包含完整压缩Gram逆。
actualΓ规范仍为K(s)=2θ′(s)，不是旧half helper。
本轮不以紧性、正迹或有限S同构判断E₂符号。

**符号与方法边界定理。** E₂在原V上有无限正、负指数。
每个有限余维闭源子空间仍有无限正、负指数；任何有限秩自伴源修正亦不能
使QW−T₂半正定。故此真实含p₂正来源不能无费用地支配完整冻结Weil型，
也不能通过仅增加有限矩或有限秩修复获得该支配。
这与530的固定arch来源边界不同：首prime非紧Swap已付，剩余紧型自身仍有两种符号。
允许逃逸是已付的非有限秩紧修正、质量费用、不同source或多prime共同机制；没有排除它们。

更明确地，存在原合法光滑源族g_η^±，L¹质量一致有界，满足

\[
 E_2(g_\eta^\pm)=\pm\frac{\sqrt2}{2\log2}\log\frac1\eta+O(1),
 \qquad \eta\downarrow0. \tag{1}
\]

每个η的支持、实际prime位置与矩条件严格保持。
(1)不表示norm1源的误差发散：||g_η||²=O(η^-1)，norm化后尺度为ηlog(1/η)→0，
符合E₂紧性。更不表示QW负值：只是QW−T₂的比较失败。

## 2. 新增实际域输入：光滑源使裸cutoff核迹类收敛

physical H=L²((0,∞),dx)，L=1_(0,1)，H₊=I−L，F的核为2cos(2πxy)。
F_p=(1−1/p)Σ_(n≥0)q^nU_(-nlogp)F−qU_logpF，q=p^-1/2，K_p=LF_pL。
每个high-scale核F_r=2cos(2πrxy)实际没有额外q^n振幅。

对每个fixed smooth compact source，严格有

\[
 \|A_g L F_r L\|_1\le C_g\frac{1+\log r}{\sqrt r},\quad r\ge1. \tag{2}
\]

独立证明：unitary log输出v、physical输入y∈(0,1)的核为
2∫_0¹g(v−log x)x^-1/2cos(2πrxy)dx。
对每个v，cosine Plancherel给y平方积分≤||g||²/r；输出v导数仅把g换成g′。
在长度O(1+log r)的中段，input→H¹(output)为HS，
H¹→L²的自然嵌入也为HS（Neumann cosine谱，不要求端点零）。
两个HS因子给(2)的中段S1费用。
更深的v<−log r−fixed constant用cos Taylor作rank-one核展开，
绝对nuclear和O_g(r^-1/2)，不粗删无限log体积。
详细边界/反演源/常数域见主证明与逆审；C_g有导数费用，不是whole源L²统一界。

Σn(1+nlog p)p^-n/2可和，使A_g L K_p在S1中按actual scale cutoff收敛。
A_g L h(K_p)亦为S1，h(K)=K(I−K²)^-1，完整逆保留。
这不使ambient K_p变成HS；531的nonHS结论保持。

## 3. 完整投影的ordinary trace与合法裸/返回分离

真实overlap O_p=P_p+L+F_pLF_p−I 的bounded block身份是

\[
 O_p=\Phi_p(h(K_p)),\qquad
 \Phi_p(T)=LTLF_pH_+ +F_pLTLF_pH_+F_p.
\]

对real smooth g，A_g normal，F_pA_g*=A_gF_p，Z_g=A_g*A_g与F_p交换。
(2)使这两个source夹心项各自为TC，可以普通循环，得到

\[
 E_p(g)=2\Re\operatorname{Tr}_{L}
      [h(K_p)LZ_gH_+F_pL]. \tag{3}
\]

不是从完整TC反推角谱强极限的迹；两个半项的域真正单独支付。
复源可分实/虚部，actual密度实偶使混合项抵消。

534给K_p∈S_r(r>2)，尤其K_p∈S3。因此
h(K_p)=K_p+C_p，C_p=K_p³(I−K_p²)^-1∈S1。
Φ_p(C_p)为ambient TC，其源修正有连续有界kernel Tr(DU_t)，
在任何L¹质量有界的窄源上是O(1)。
任意ambient D∈S1还诱导sourceS1：g↦Tr(A_gDA_g*)的源trace norm≤|U|||D||1，
因g↦A_gψ为HS、HS²=|U|||ψ||²，再按D的nuclear展开求和。

bare Φ_p(K_p)的实际double-scale核也可合法辨认：第一因子源S1收敛由(2)支付，
第二因子F_p级数operator-norm收敛；finite boundary source矩形给普通积分。
先使用完整F_p的合法半迹，随后才取第二核的有限scale极限；
有限F_N通常不满足F_N²=I，本证明没有套用它的involution或Φ身份。
共振列的源kernel L¹费用O(p^-m)，其余列相位gap可求和。
所以核共同limit与actual ordinary trace一致，不套用C006的未付角分离。

## 4. 真正log2处的算术共振

actual F₂核为Σ_(n≥0)cos(2π2^nxy)−cos(πxy)。
取振幅1的cos×cos核

\[
 I_{r_1,r_2}(t)=e^{t/2}\int_{e^{-t}}^1\int_0^1
        \cos(2\pi r_1xz)\cos(2\pi r_2e^txz)\,dz\,dx.
\]

它由Si的两真实端点差明确给出。t≈a时唯一无限共振族为
r₁=2^(m+1)、r₂=2^m，m≥0。t=a时difference-phase平均cos²项为√2/4。
对2^m|t−a|≤1，偏离该常数的误差总和O(1)；对更高尺度，
Si的π/2项在同号两端点取消，tail O(2^-2m|t−a|^-2)亦总和O(1)。
故bare even源核具有

\[
 e_{2,\mathrm{bare}}(a+\delta)
    =\frac{\sqrt2}{4a}\log\frac1{|\delta|}+O(1). \tag{4}
\]

余项可有bounded log-periodic波动，不需要将它认作TC或小载频误差。
在t=0附近，同scale列为O(|t|(1+log(1/|t|)))，其余列连续有界。
冻结差支持W=log√6<2a，没有其他无限共振点。
完整返回修正连续有界，故不能消除(4)的正log奇性。
这在C006的p≥3冻结域不出现，因为那里W<logp有phase gap。

## 5. 严格矩零窄源及无限指数

取非负φ∈Cc∞(−1,1)，∫φ=1；取两个fixed normalized smooth bumps ψ₋、ψ₊
在patch内避开窄源中心，且m₋=ℓ₁/₂(ψ₋)<m₊=ℓ₁/₂(ψ₊)。
置φ_η(y)=η^-1φ(y/η)，以精确两方程
c₋+c₊=1、c₋m₋+c₊m₊=ℓ₁/₂(φ_η)
定义h_η=φ_η−c₋ψ₋−c₊ψ₊。
系数一致有界，ℓ₀(h_η)=ℓ₁/₂(h_η)=0且L¹质量有界。
530已付的矩零像定理还保证这些h_η属于D(D+1/2)Cc∞(patch)，
没有将原合法源生成器换为更大的未准入空间。
g_η^±是原两patch同h_η的等号/反号组合。

(4)使窄源与其真实log2 translate的cross为±2c log(1/η)+O(1)，
c=√2/(4a)。self kernel有界；narrow/fixed或fixed/fixed的log配对可积且统一有界；
完整TC返回核亦O(1)。于是得到actual (1)。
正方向存在就严格排除全V的QW≥T₂无费桥，负方向也实际存在。

任给N，在patch中选N个不同中心x_i，避开两个固定矩修正bumps，
分别构造h_(i,η)及g_(i,η)^σ，σ=±1。
其actual E₂ Gram矩阵为

\[
 \bigl(E_2(g_{i,\eta}^{\sigma},g_{j,\eta}^{\sigma})\bigr)_{i,j=1}^{N}
   =\sigma\frac{\sqrt2}{2a}\log\frac1\eta I_N+O_N(1).
\]

不同中心的cross离开log奇性中心，所有offdiagonal有界；
η小便分别给N维strict positive/negative源空间。
这是无限正负指数的直接证明，不需指定carrier或依赖S1余项渐近。
再加任何有限个连续源条件，只能删除有限维，仍有无限指数；
有限秩自伴修复在其kernel亦不能除去这些指数。

独立source审查还以对角H¹→S1与cross Fejér非S1给同一无限指数后果；
主证明选择前件更少的N个窄源组织。

## 6. 固定单prime族的范围与宏观影响

相同证明适用于每个固定实际素数p。
其bulk核系数2(1−1/p)，共振r₁=pr₂在t=logp给

\[
 c_p=\frac{2\sqrt p(1-1/p)^3}{\log p}>0,
 \qquad E_p(g_\eta^\pm)=\pm2c_p\log(1/\eta)+O_p(1).
\]

选择足够小patch隔离actual p相关并排除其他primepowers；
每个源支持窗λ>√p都可容纳这样的两patch合法子域。
在那里QW−T_p=−E_p，故每个固定single-prime来源的无费桥与有限条件修复均失败。
这不处理一般finite S的稠密mixed-scale共振，不宣称uniform p费用或成长S边界。
相对启动基线，513/514处理不同的singleboundary/绝对范数尾，
未给本文真实双cutoff的源平滑迹类域、log共振和actual无限指数；
531/532的新接口也不已含本文符号结论。未作世界优先权全局检索。

实际瓶颈有所改变：真实first-prime桥的剩余符号现已判定为不定，
不能继续把E₂≤0当未知正性来源。光滑源S1引理支付了一个此前缺失的trace域；
成长费用仍须完整signed低cycle核及共同预算，不自动复活C006。
原固定源紧性、534历史conditional状态按新证据另记消费范围，不删除旧纠错。

独立[宏观完成审计](../goals/reviews/2026-10-14-goal-method-boundary-completion-audit.md)
按原Goal第三分支及旧Goal§10B/C验收了这一个定理的实质方法类规模，
并非累计旧小障碍或降低为合同完成。所有fixedsingleprime/λ>√p、
无限实际反向空间及finiteconstraints/rankrepair的失败，给出核心正来源比较的
量化分界和修复责任。完成保存、远程核验及runtime Goal操作后可按该分支结束。

未排除非有限秩紧费用、多prime联合抵消或独立几何正性，
未证明RH、实际ζ谱带、lowest/prolate排序或全域Weil正性。
这些是明示的逃逸和更远目标，不是边界分支的隐藏完成前件。
另新定位的compact-window primary候选尚未核原证明/证书，保持cited/open且未启动；
不以它完成本Goal，也不在结束后自动替换为第二个研究Goal。
