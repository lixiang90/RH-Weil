# C009：Liu固定原件的完整源、Fourier补空间及Block–Schur审查

2026-10-14；起始HEAD `3d9bbbfef989e0962d32f6af512b13bd6cd6a3ba`。
已恢复AGENTS/README/STATE/check/show、Goal、C009及D20261014G。
只写本辅助文件；不改STATE/cadence/git，不运行外部代码，不联系作者。
原C008保持止损；旧runtime Goal完成收据保留，不另创建Goal。

固定原件为提交 `b6cd2183c1e79c6c27a34267812a7b2d73ed1b59` 的
`tmp/c009-liu/certified-weil-positivity-b6cd2183c1e79c6c27a34267812a7b2d73ed1b59/frozen-source/publication/manuscript.tex`。
下述行号均指该TeX，不用PDF页码代替。数学正文只读核；原作者PASS保持cited。
§1–7保存首审时的conditional状态；同轮fresh B与primitive末审结论以§8为准。

## 1. 实际完整Weil对象与complex量词

97行明确legal域D_L=Cc∞((-L,L);C)、H_L=L²((-L,L);C)，Lebesgue norm；
102行Fourier采用F_f(z)=∫f(u)e^-izu du。113、123–125行是

    A(t)=Re ψ(1/4+it/2)−logπ=actual 2θ′(t),
    Q(f)=P(f)+(2π)^-1∫A(t)|F_f(t)|²dt
                    −Σ c_n Re h_f(log n),
    c_n=2Λ(n)/√n,
    P(f)=2Re[F_f(i/2)overline F_f(−i/2)].

该Γ是完整actual规范，不是half helper。所有prime powers的权用Λ(n)=log p，
位移用log n=jlog p；没有把8的权误写为log8。
设C_f=∫f cosh(u/2)、S_f=∫f sinh(u/2)，complex pole严格为

    P(f)=2(|C_f|²−|S_f|²).

因此odd pole负项保留。131–142行给
widehat h_f(z)=F_f(z)overline F_f(overline z)，以及正确的off-critical zeros乘积；
不把γρ预设为real。使用functional-equation成对γ、−γ可改写到Re h_f的even part，
zero-side绝对收敛由smooth compact support及无条件零计数支付。
这个论证不使用RH作为geometric-side等式前件，也不局限于real-even源。

Theorem A半窗L=1的完整prime powers是2、3、4、5、7；
Theorem B半窗L=17/16的完整prime powers为2、3、4、5、7、8（246、251行）。
它们与本仓同unitary log源对象一致。有限源basis/相位字典沿536：
中心指数basis需D_n=(-1)^n相位才literal匹配qw_matrix.py的w02/q_nm，
该unitary相位保持奇偶；没有额外norm缩放能将更大C001窗放进这两个窗。

## 2. bounded comparison不偷换unbounded Q的legal域

Theorem A用bounded R₁（193–195行）及Q≥R₁只作用原smooth f。
其Legendre分解、2816-mode head及全complement估计在H_1上进行，
225行明确不在discontinuous polynomial zero-extension上计算unbounded Q。
Theorem B同样把Q分为bounded M+K和非负exterior integral（271–272行），
435行只在最后回到原smooth f；辅助向量可以仅在H_L。
这与C008模糊的full-L²有限form措辞不同，未发现此处域量词偷换。

自然closed form域为

    D_log,L={f∈H_L:∫log(2+|t|)|F_f(t)|²dt<∞}.

实际Γ加常数后与1+log(2+|t|)双向可比；有限shift与双pole是bounded selfadjoint扰动，
故Q定义dense closed semibounded form，域外可作+∞解释。
以下独立core证明支付从全smooth到closed域的运输，而非只用L² density：
对f∈D_log,L先缩支撑f_ρ(u)=ρ^-1/2 f(u/ρ)，ρ↑1。
F_ρ(t)=√ρ F(ρt)；ρ近1时log-weight dilation统一有界，且在weighted L²中strong continuous
（先在compact-frequency连续函数验证，再用weighted L² density），所以f_ρ→f于form norm。
再用ηε∈Cc∞、∫ηε=1、ηε≥0对f_ρ卷积，ε<(1−ρ)L。
其Fourier multiplier绝对值≤1、趋1，weighted dominated convergence给form-norm收敛，
而支持保持在(-L,L)。故Cc∞((-L,L))确为form core。
若原smooth coercivity证书最终通过，其同一常数延拓到D_log,L，不增加未付边界条件。
此扩张不使Q成为full-L² bounded operator，也不自行认证数字。

## 3. Theorem B的全Fourier补空间：独立解析核通过

1059–1117行声称E(f)=(2π)^-1∫_|t|>256|F|²≥δ||f||²，δ=2^-49158。
本审查逐步核其量词与常数，未发现仅有限basis或real源的限制：

1. ||f||=1及bounded support给|F^(j)(t)|≤√(2L)L^j<2L^j，适用全部H_L。
   若E<1/2，band integral>π，some t₀∈[-256,256]有|F(t₀)|>1/16。
2. N=4096个disjoint intervals长h=1/32，位于[256,512]。
   积分均值给每个x_j满足|F(x_j)|≤√(64π E)<16√E，
   |x_j−x_k|≥h|j−k|，|t₀−x_j|≤768。
3. 选constant phase令G=Re(e^-iαF)在t₀取|F(t₀)|，普通real Lagrange remainder合法。
   权和≤(768/h)^(N−1)Σ[j!(N−1−j)!]^-1
         =49152^4095/4095!<2^24570。
   last bound由e<3与3·49152<64·4095。
4. remainder≤2(768L)^4096/4096!<2(3/5)^4096<1/32。
   因而1/16<16√E·2^24570+1/32，得√E>2^-24579及E>δ。

这是对全H_L的严格、很粗的uncertainty bound，无RH/zero拟合输入。
Plancherel给I−B_band≥δI，不把frequency band projection误当支持域上的orthogonal projection。
它本身只付一个tail supplier，不付低频Weil符号或有限矩阵PD。

736–754行exterior A下界也可独立核：Binet将z=5/4+it/2，
|u²+z²|≥5t/4，∫u/(e^(2πu)−1)=1/24。
real logarithm/reciprocal bound给A≥log(t/2π)−1/(15t)−7/(2t²)，
t≥15/4后≥log(t/2π)−1/t。
1125–1137行rational comparison给|t|≥256时A−7/2>C=123/1280，
所以T_tail≥C(I−B_band)对全H_L的extended tail成立，smooth源上有限。

## 4. rank-two positive tail是真的供给，不是删odd pole

1165–1221行定义S=I−B_band−δI、h_j=Sv_j，v₀/v₁为constant/linear规范化Legendre源。
上节给0≤S≤I。parity保证<v₀,Sv₁>=0；e_j=<v_j,(I−B)v_j>，e_j−δ>0。
对任意complex z₀,z₁最小化S半范数的平方，得到

    <f,Sf>≥Σ |<h_j,f>|²/(e_j−δ).

这只是positive-form Bessel/square-completion，没有假设S invertible或h_j彼此L²正交。
1170–1195行real Fourier积分给e₀/e₁上下界；c=272时e_j>2^-11>δ。
正integer inequalities支付81e₀<C、27e₁<C，而Cδ>δ/16=τ。
本辅助另用原生BigInt独立重算两清分母正差，分别恰为13473024和2251158528；
123·16>1280亦exact成立。没有运行原作者程序，这不是ordinaryprecision实验。
于是严格有

    T_tail(f)≥τ||f||²+81|<h₀,f>|²+27|<h₁,f>|²,
    τ=2^-49162.

U为positive rank-two supplier，来自完整exterior Γ余量；negative odd pole仍在K内。
它不声称整个tail为rank-two，也没有将finite-dimensional positivity极化到全源。
取更弱bound U≤C S不影响上述消费，但不能据此替代原certified finite head。

## 5. bounded Block–Schur与inverse order的消费链

538–640行Certification Theorem独立核通过：M∈[m,b]、m>0先行，
E为isometry，A=E*ME，B=E*M²E，G=E*M^-1E，D_M=B−A²=F*F≥0。
这里B必须是完整M²的压缩，不能替换为A²；1646–1682行明确全13 shifts和169 ordered pairs
以及三重support intersection，符合这一必要接口。

取L_c=−M_c^-1F、T=E+L_c，bounded变量f=Tc+y消去M的cross。
R=V−EJE*满足R₀₀=0，Young给
T*RT≥−eθI−(e/θ+n)m^-2D_M。
剩余cross Z=R₁₀+R₁₁L_c有
Z*Z≤(1+χ)e²I+(1+χ^-1)h²m^-2D_M。
complement≥m−n>0，square completion费用确为(18)的αI+βD_M。
没有先假设desired finite sign才invert M，也没有M、V commuting假设。

391–411行trial inverse envelope也正确：直接展开

    U_μ(X)−G=(E−MEX)* (μ^-1I−M^-1)(E−MEX)≥0

当0<μ<m时成立。source intervals给W≥G>0后逆序W^-1≤G^-1，
不是拿trial inverse的ordinary residual当exact positivity。
644–682行所有source allowances和positive congruence是必须的后续门；
Gram整数目标只在这些门先支付后才推出全H_L bounded comparison。

1367–1418行projection/error接口没有把O(r)与O(r²)混合：
band cross≤1344r、retained-tail cross<45r，negative complement只需896r²+p，
norm complement另含positive U费用10800r²。源norm和Gram normalization在367–387行明示，
L² raw change-of-variables不是额外orthonormal center缩放。
本辅助没有执行完整source-matrix或integer congruence检查；数值sign仍cited。

## 6. 最便宜反例的正确范围

441–528行Obstruction Theorem给真实合法complex modulation族，独立核其对象后成立：
a=log8>2，L>a/2，取两窄bump g=φ(u+a/2)+φ(u−a/2)，
T_k=2πk/a、f_k=e^(iT_ku)g。任何χ∈D_1、||χ||=1都有ρ_χ(a)=0。
g的相关只遇prime power8，h_g(a)=||g||²/2；continuous defect核为L¹，
Riemann–Lebesgue使该部分趋0。局部R₁−(1/16)I为compact，modulation弱零。
所以文中指定tail-dropping comparison Dχ满足

    lim Dχ(f_k)/||f_k||²=1/16−log2/(2√2)<−1/8.

这个解析反例不依赖有限sign计算，且fixed compact repair沿该弱零族消失。
但Q=Dχ+Sχ，Sχ≥0尚被保留；它不是Q负源，也不反驳Theorem B。
它与本仓535均排除各自特定无费用比较，不能互换对象或复活canonical Sonin桥。
Theorem B的global source-exact M/完整tail保留不等于这个已失败localization/drop-tail方案。

本辅助未找到反驳Theorem B解析全源归约的更便宜合法源；
不能将粗norm、极小τ或公开PASS标签当反例/证明。

## 7. 净后果、未付输入及唯一下一动作

若原完整source/error/congruence/Gram门被主审和不同组织逆审核通过，
Theorem A/B确可分别给actual Q≥2^-151/2^-49162于全complex smooth半窗1/17/16，
并依§2延到closed form域。这是固定窗真实下界，不是有限N诊断或RH等价重述。
本仓原C007 V的source外端≈0.44794小于两个半窗，因此可继承该actual下界；
仍不推出E₂≤0或QW≥T₂，不与535矛盾。

C001 μ=13对应半窗log13/2≈1.282>17/16>1，两个窗均不覆盖其原12冻结矩阵。
本原件也未给simple-even真正ground的lower/upper gap证书；coercivity本身不推单重、
lowest/prolate相认、成长支持或RH。closed form的compact-resolvent存在性可另按536核得，
但不支付ground parity/排序。

首审新增独立核：全complex object、quantitative全H_L Fourier complement、rank-two tail square completion、
bounded Block–Schur/inverse order以及smooth→closed core运输；当时原数值下界仍cited，
随后fresh B及最终primitive消费更新见§8。
唯一下一动作由主代理检查原完整source→interval/Gram/congruence链并决定最低费用重放，
不以单个整数PD替代缺失数学门；若全链缺项按C009 1–2轮止损。
无辅助pending process，不修改STATE/cadence/git，不执行外部code。

## 8. 同轮最终消费补审：primitive到全operator误差链

本节覆盖原TeX D.1–D.5（1432–1792行），只读交叉原包
`reproduction/source/01-check.py`、`02-produce.py`、`07-check.py`、`08-produce.py`、
`11-checker_quotient.py`、`12-raw_column_producer.py`的相关实现。
代码行号以下明确带文件名。没有执行这些外部程序；主代理的fresh FULL_REBUILD另记录。
再次恢复STATE/check/show时唯一C009仍running，原session5748已登记，未重复启动。

### D.1：actual Γ primitive moments

1440–1442行moment θ_q=(256/π)∫₀¹x^(2q)(A(256x)−7/2)dx，q=0..1023，
包含Γ常数−logπ与−7/2。shift256后s=1025/4、b=128，recurrence负号和256项
reciprocal和都与ψ(z+256)=ψ(z)+Σ_j(z+j)^-1一致。
1471行Binet denominator控制为finite remainder估计，不是假设Bernoulli级数收敛。
AM–GM给513!≤257^513，6s>2^10、257/(6s)<1/5，所以
4·513!/(6s)^514<2^-1034，moment贡献<2^-1026。
1480–1505行J/H/log的积分recurrences由一次微分/分部积分直接核准，
H更新只除rs，不除可能为0的d+1−r。

01-check.py 178–235行原生dyadic rational oracle与02-produce.py 147–203行producer
分别构造constants/Bernoulli及全部moments；01的229–235行把uniform Binet余项
在积分后、正256/π缩放前只支付一次。新moment receipt的1024项完整containment及
binetRemainderPaidOnce已读取。3-unit width on2^-1024 grid使midpoint error<2^-1023。
没有把finite moment packet的PASS当full Q证书。

### D.2：uniform kernel到dimension-independent operator error

1541–1542行k₀(2Ly)的pole系数2L^(2q)来自2cosh(Ly)，
band系数(−1)^q544^(2q)θ_q来自Ω·2L=544，规范及尺度都正确。
1536–1558行cos real-Taylor余项与pole余项合付
914·544^2048/2048!<2^-758；moment midpoint替换误差
<2^-1023 cosh544<2^-207。e²<8给e^544<2^816，故该放大仍被预算覆盖。
两项相加得到uniform kernel error<2^-206。
窗口长度2L=17/8给||K−K₀||≤(17/8)2^-206<2^-204，
对整个H_L有效，绝非将entry-wise error与448混淆。
Binet项已在moments里，operator支付没有重复加或删除它。

### D.3：Legendre seeds及expanded boundary

1576–1638行boundary Rodrigues权w_mj和F/T closed seeds可通过factorial cancellation
及vanishing endpoint Legendre primitives直接推导。
constant核和quadratic核的00/11位置另独立代入核对相位/符号。
07-check.py 279–309行用closed F/T seeds，08-produce.py 210–238行用boundary seeds；
两路虽共享合法Legendre recurrence，但其seed构造不同，完整containment检查能审seed误装。
expanded domain r≤j、r+j≤894、r≤447确覆盖每个(r−1,j+1)依赖：总阶不增加，
row0须到894且boundary须到895，row1到893，最终447,447仍在域内。
07的312–340和08的242–278保留这些域，核count895 seeds+99681 updates，
最后才抽取50400个同parity上三角条目。没有在448×448边界直接补0。

### D.4：完整M²、boundary term及raw norm

07-check.py 132–189行从true primitive log/root重新包13 centers，每个shift/weight误差≤η=2^-2048，
paired ±shift同weight；total absolute weight<10有明确检查。weight的4/8用log2，位移仍log4/log8。
08的175–200及07的242–267遍历169 ordered pairs；三重交集为
I∩(I−a)∩(I−b)，无交集置0。新receipt记录107 nonempty、62 empty，13 A shifts。
这给B=<Mp_i,Mp_j>而非(PMP)²；07 overlap fixture把错误13/8与真实9/8区分开。

1703–1713行g_(i+1)−g_(i−1)在internal support端点的primitive值相消，所以weak derivative公式合法；
external ±L one-sided trace一般不相消。08的259–261及07的332–334确加入该B更新项，
不把所有Legendre endpoint都当0。对角/对称paired shifts使实际奇偶selection一致。

source-center Lipschitz费也有足够量化余量：i,j≤447时|P_i|≤1、
|P_i'|≤100128；移动两个shift各≤η给overlap长度损失≤2η，common part误差
≤[i(i+1)+j(j+1)]η。total weight<10使M²全加权损失
小于100·400514η。12个nonzero weights各误差≤η，故全部ordered weight-product误差
≤240η+144η²<241η；每overlap integral绝对值≤2L<3，费用<723η。
最终raw entry total<40052123η<2^26η=2^-2022<2^-2021。
这是直接比较最终i,j≤447的真实/中心overlap积分：common overlap中两套polynomial
arguments都在[-1,1]，derivative界合法；若某套overlap为空，endpoint loss仍≤2η。
不把这项primitive费用沿expanded895 recurrence传播。expanded中心矩阵的计算误差
另由directed intervals及complete independent containment包住，最后只对最终raw entries
支付真实source-center费用，因而895的较大derivative不进入此项预算。
与07/08为A/B的source-radius支付一致，不依赖只核finite numerical中心。

raw Γ_nn=2L/(2n+1)=17/[8(2n+1)]。
J₀由dimensionless integral乘L²=289/256后才raw-normalize；07的321行及08的267行确如此。
半width radius on2^-256 grid给weighted norm allowance
max_i Σ_j width_ij·4(2i+1)/(17·2^256)，不是少了Γ中的2；
07的354–380行支付全部448行。新A/B/J₀ receipt均给≤2^-220。
因此orthonormal source errors为ε_A=ε_B=2^-220、ε_H=2^-204+2^-220，
dimension-independent Γ kernel误差与raw rounding分别支付。

### D.5：complete tail columns及rank-two normalization

1735–1748行sin Taylor到2048度的零偶系数仍纳入remainder，
|sin x/x−s₁₀₂₄(x)|≤|x|^2048/2049!；uniform kernel乘窗口长度给
||B_band−B_tilde||≤544^2049/(π·2049!)<2^-513。
Machin rational pπ误差<2^-646，pπ>2，B_p=(π/pπ)B_tilde的误差由
||B_band||≤1及前一operator误差支付，<2^-513+2^-646。

1761–1768行raw column factorΩL²=289正确；11-checker_quotient.py 55–104行
直接factorial summands及12-raw_column_producer.py的seed ratios保持同一raw量。
δ=2^-49158虽很小，formula中仍exact保留，opposite parity coordinates正好0。
Γ_nnΓ_jj>1/1024、sqrt448<32使每raw coordinate2^-524误差的完整norm
<2^-514；再加full band error得到每normalized column error<2^-512。
新tail receipt明确896坐标/448 parity zeros完整重核。

1785–1792行81/Γ_00=27/Γ_11=648/17，故raw U update是
(648/17)(r₀r₀*+r₁r₁*)，随后才Γ^-1/2 congruence。
旧tail checker的单独aggregate标签不是最终费用；新stage receipt明确currentCoefficients=[81,27]、
currentRankTwoError=9·2^-512、legacy allowance unused。该σ与1226–1232行两rank-one差一致。

### 实际fresh门与最终范围

已直接读取`tmp/c009-liu/fresh-b-20261014/verification-summary.json`、`theorem-b-result.json`及
moments/tails/matrices/core0/core1 receipts；新FULL_REBUILD elapsed326.172秒，
1024 moments、13 centers、169 pairs、151200 intervals、896 tail coordinates、
100352 target coordinates、448 Gram rows全部完成，两sector各224行。
scalar assertions56，两完整compiler equality与Gram residual闭合由主/逆审另核。
本辅助没有重跑pipeline；较大integer JSON用自写只读parser抽关键字段，未执行原外部code。
本机CPython3.12.5与原tested3.12.10不同，不能声称环境逐字复制；实际exact enclosures、
integer acceptance与source hashes提供本机复核证据，不以版本标签代替它们。
新summary亦明确externalHumanReproduction=false、formalProofVerification=false。

本来源审查对D.1–D.5 primitive→full operator预算**通过**；未发现剩余解析消费缺口。
结合§1–5及主代理已核的完整正congruence/compiler/Gram门，支持消费固定Theorem B：

    Q(f)≥2^-49162||f||²，所有f∈Cc∞((-17/16,17/16);C)，

并由§2独立core论证扩到D_log,17/16。该结论来自数学桥+本机实际完整checks，
不从exit0、原作者PASS或result中的无缺口字符串单独推出。
Theorem A本机未重放，不能随B一起导入；B不证明simple/even ground、
更大C001窗、growth/RH/世界优先权或独立external human验证。
本同轮补审不新增轮数；无辅助pending process，主进程终态由主代理保存。
