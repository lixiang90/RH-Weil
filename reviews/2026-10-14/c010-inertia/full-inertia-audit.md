# C010：完整 Weil 型阈值惯性与当前正尾供给的实际范围

2026-10-14。先恢复AGENTS/README/STATE/check/show、Goal、C010与D20261014I，
当前Goal active；旧535完成收据仅历史。实际起始HEAD
`35609baea2fb3a4456b5ab9250648b198a9a4130`。本辅助不改STATE/cadence/git。
固定原tex为`tmp/c009-liu/w200-pub-2026-09-14/publication/manuscript.tex`，
其bytes与C009 b6cd218 frozen-source tex相同；原行号沿用C009审查。

## 1. 已付原输入与本轮可消费结果

原C009 fresh source-matrices、tail-columns、两trial及两target的bytes长度和
SHA重新与fresh frozen-manifest精确核对一致。重要两个source SHA为

    source-matrices: 4bce98228442805bc5ae16e9c26c8df88e85c35ab7ec8deffdd808adbf1217ac
    tail-columns:   2a88894c7405e01a37cbdef8671e9d628ddc60ae9cdb335fa2636fe49b6666a2

source parameters固定448度、L=17/16、omega256、raw输出grid2^256；
B明确为`E*M²E`保留middle compression，J0为raw L²换元kernel；
真实primitive/input/source误差已经由537及C009两份独立审查支付。
本轮没有把scalar/Gram标签替代这些原前件。

已付完整原比较为同Lebesgue norm及natural closed form域上的

\[
Q\succeq\tau I+R,\quad R=M+V,\quad V=K+U,
\quad mI\preceq M\preceq bI,
\]

tau=2^-49162、m=9617/10400、b=63183/10400。
P为448度orthogonal Legendre projection，E为对应isometry；
J=E*VE，R_res=V−EJE*（下文将原residual记为R_res以免与完整R混名）。
cross、complement费用分别为

    e=1389·2^-95+2^-440,
    n=896·2^-190+2^-440,
    h=11696·2^-190+2^-440.

本轮给严格阈值惯性运输公式，另取得两个实际forcing而非只写条件归约：

* 每个奇偶扇区的第225个真正Q min–max值至少tau+m−n>9/10；
* 独立全Fraction raw odd64源给`lambda1(Rodd)<2e−31`，见§5。

第一项是较粗的低谱数目上界，第二项是当前固定R供给的odd-gap天花板。
它们均不足以证明simple-even真正ground；已付原证书不含那个结论。

## 2. 合法域、阈值与完整惯性

Q是Dlog上的半有界closed Hermitian form，

    Dlog={f∈L²(I):∫log(2+|t|)|F_f(t)|²dt<∞}, I=(-17/16,17/16).

Cc∞(I)为form core，压缩Fourier的有限rectangle紧性及统一高频log尾
给compact form embedding，所以对应actual operator有compact resolvent。
这是同norm真正Q的谱实现，不是把R的bounded spectrum当Q spectrum。
反射保Dlog且commute Q，实/复及even/odd的源规范已付，min–max各自合法。

令目标阈值为s、t=s−tau，取M_t=M−tI，可精确保留tau；
若取t=s就是保守地丢tau，也合法但应说清。则

    Q−sI >= L_t:=M_t+V.

只在`m_t=m−t>n`的正complement区间应用本节。
对任意Hermitian型q，n_-(q)为其strict-negative子空间最大维数；
compact-resolvent Q的`N_Q(s)=n_-(Q−sI)=#{lambda_j(Q)<s}`。
form顺序直接给`N_Q(s)<=n_-(L_t)`，只向这个方向。
不需要bounded变换保持Dlog：先将合法Q负子空间嵌入Hilbert空间，
bounded L_t负型上界再在整个Hilbert空间证明。

移位全算子保留完整prime：

\[
A_t=A-tI,\quad B_t=B-2tA+t^2I,
\quad D_t=B_t-A_t^2=B-A^2=:D\succeq0.
\]

B不能替换成A²，D虽shift不变却不等于0。
M_t的complement block仍>=m_t I，先支付inverse，不循环借目标sign。
令G_t=E*M_t^-1E，L_c,t=−(M_c−tI)^-1F，T_t=E+L_c,t。
有`G_t^-1=A_t−F*(M_c−tI)^-1F`及`L_c,t*L_c,t<=m_t^-2D`。
任意源f唯一表示T_t c+y，E*y=0；旧M_t的cross严格消去。

按原complex Young与补空间完成平方，令

\[
\alpha_t=e\theta+\frac{(1+\chi)e^2}{m_t-n},\quad
\beta_t=\frac{e/\theta+n}{m_t^2}
+\frac{(1+\chi^{-1})h^2}{m_t^2(m_t-n)}.
\]

真实有限Schur型S_exact,t满足

    S_exact,t >= G_t^-1+J−alpha_t I−beta_t D.

其exact complement是M_c−tI+R_res,11>=m_t−n>0；
有界可逆triangular congruence给
`n_-(L_t)=n_-(S_exact,t)`，不是只证两块diagonal的sign。
因此任何经误差支付的finite lower matrix P_t，只要
`P_t<=G_t^-1+J−alpha_t I−beta_t D`，均给

\[
N_Q(s)\le n_-(P_t). \tag{A}
\]

若n_-(P_t)<=k，则真正`lambda_(k+1)(Q)>=s`。
PSD给k=0；codimension-k上PSD同样给k上界，允许threshold恰为eigenvalue，
strict-negative计数不会把zero误当negative。
finite P_t的负方向不反向推出Q负方向或Q低谱下界。

## 3. source费用与G_t inverse上界

原errors记etaA=etaB=2^-220，etaH=2^-204+2^-220，sigma=9·2^-512。
J的原中心H0+Uhat及其误差不随t改变。
定义A0,t=A0−tI、B0,t=B0−2tA0+t²I，可用
`||B_t−B0,t||<=etaB+2|t|etaA`。
但是D的相关消去是exact，故D0,t=B0,t−A0,t²=D0=B0−A0²。
最便宜、正确的D费用保持原

    epsilonD=etaB+(2b+etaA)etaA,

不必将独立shift误差相加来恶化它，更不能因D不变而删除原误差。
同理若重做inverse-centered U，必须支付其真正shift费用，不盲复用原DeltaX。

一种合法做法：选0<mu_t<m_t，用任意重新认证norm<=y的trial X_t，
计算原U_mu公式但输入A_t,B_t。原residual identity照样给
`U_mu_t(X_t)>=G_t`，再加中心误差

\[
\Delta_{X,t}=y^2\eta_A+
\mu_t^{-1}\{2y\eta_A+y^2(\eta_B+2|t|\eta_A)\}.
\]

所得W_t>=G_t>0才可inverse-order运输。旧trial若直接复用仍需该shift费；
原norm8的独立Frobenius证明可复用因为X没变，但原DeltaX只适用于t=0。
在小正t可选mu_t=29/32−t；必须核其正性，不能任意越过29/32。

更便宜、完全复用已认证W0的保守做法：对0<=t<m，functional calculus给

    (M−tI)^-1 <= (1−t/m)^-1 M^-1,
    G_t <= (1−t/m)^-1 G0 <= W_t:=(1−t/m)^-1 W0.

对t<=0可取W_t=W0。这一步不需新trial或新增source预算，
但可能显著损失本就微小的finite gap；不能将保守失败冒充所有inertia法失败。

无论哪条inverse上界，safe finite lower matrix为

\[
P_t=H_0+\widehat U+W_t^{-1}
 -(\eta_H+\sigma+\alpha_t+\beta_t\epsilon_D)I
 -\beta_t(B_0-A_0^2). \tag{B}
\]

所有中心均是orthonormal坐标，不是raw数组相加就计inertia。
W_t>=G_t给W_t^-1<=G_t^-1，因此(B)是lower型，方向正确。
原K48是t=0、固定theta/chi/congruence的target，不能仅改一个diagonal
把它冒充(B)的新阈值target；W_t、alpha_t、beta_t及positive congruence
亦随阈值或trial变化。

## 4. 有限惯性、frame与真正ground门

即使P_t不PSD，也可通过exact rational LDL*的已分离pivot sign证明惯性，
或构造exact codimension-k frame F并证明F*P_tF>=0。
congruence保持惯性而不保持Rayleigh尺度；矩阵缩放/raw Gamma及残差
必须支付后才能将finite count运输到(A)。原两块t=0 Gram只认证各PSD，
没有给任何positive-threshold的n_-<=1测试。

exact PSD frame仅需full rank及正确codimension，不一定orthonormal。
但有限residual若只给`F*P_tF>=−dI`，full rank不能自动消费用；
range F的norm下界需除`lambda_min(F*F)`。
若P_t输入另有norm不确定eps，frame中至少扣`eps F*F`
（保守扣eps||F||²I），不可只扣eps I。最好将proposal frame固定成exact
rational，重验完整Gram；此时proposal来自数值而证明不依赖其近似正交。

simple-even的真正门为：同一threshold s上

    N_Qodd(s)=0, N_Qeven(s)<=1,
    actual geometric even Rayleigh upper u<s.

compact resolvent确保ground attained，后二项使even底存在于s下且multiplicity1，
前项使odd没有更低谱。原tau coercivity只给两个sector共同下界；
任一合法even上界均>=tau，故旧共同下界不能分离这三门。
R的finite least vector给R上界，不能给Q上界，因为Q−tau−R保留正尾。
实际geometric Q上界需原dual pole、full prime及Gamma/positive omitted tail全付。

已有原complement直接给一个粗但真正forcing：对f∈rangeP⊥∩Dlog，
`Q(f)>=(tau+m−n)||f||²`。各parity head维数224，故

\[
\lambda_{225}(Q_{even}),\lambda_{225}(Q_{odd})\ge\tau+m-n>9/10,
\quad N_Q(9/10)\le448.
\]

这是actual fullQ min–max推论，不需P_t finite sign；但远非index1/odd-gap，
也不是新的独立来源输入或宏观合同成功。

## 5. 当前固定R供给的严格odd天花板

parent与source原scale 16/32/64普通80digit pilot结果一致，无已证负R源。
这些finite排序不认证Q排序。本辅助按新授权做最低费用的exact upper，
没有扩N或输入ζ零点：

* 脚本：`scripts/c010_odd_rational_ceiling.py`；
* exact结果：`reviews/2026-10-14/c010-inertia/c010-odd-rational-ceiling.json`；
* pilot SHA：`a7c1ac311188b6121899826d09d6c207eeea82f35bcf279faff0508e2f8b43aa`。

从已冻结odd64 raw向量仅提案，round成denominator10^50的64个精确有理
Legendre系数，原degree1,3,…,127；JSON完整存整数分子及分母。
任意提案向量都允许，round不须近似eigenvector保证。
完整Araw、J0raw triangular centers为endpoint sums/2^257，
两tail raw列为endpoint sums/2^641。按raw Gamma=17/[8(2n+1)]计算exact norm，
按原648/17 rank-two update计算full rational Rayleigh；未丢cross或negative
pole。最后支付整个orthonormal operator误差

    epsilonR=2^-204+2·2^-220+9·2^-512.

所有比较为Fraction整数判定，得到

\[
0<\|f_{odd}\|^2,\qquad
\frac{\langle f_{odd},R f_{odd}\rangle}{\|f_{odd}\|^2}
 \le R_{center}(f_{odd})/\|f_{odd}\|^2+\epsilon_R
 <2\cdot10^{-31}. \tag{C}
\]

display center约1.8402410427064023e−31、norm约1；这些小数不参与门。
源是zero-extended finite polynomial，属L²且Fourier为O(1/t)，所以亦属Dlog；
可用已付core逼近smooth源，不存在用非法原Q域消耗惯性的例外。
作为R的上界本来也只需L²。

故真正`lambda1(Rodd)<2e−31`，与已付R非负一致。
这严格限制**当前固定比较Q>=tau+R**：若尝试只靠它证明odd全底>=s，
而s>=tau+2e−31，则Rodd+tau本身已有低于s的方向，
不可能得到n_-(Rodd+tau−s)=0。改善P_t inverse、frame、rounding或
matched compiler不会改变这个实际upper。进一步tail supplier/新U或
直接保留positive余尾可以改变R，是未排除的逃逸。

不能从(C)说Qodd<2e−31；Q的真实剩余正尾可能抬高该源。
只有当另有actual even upper必须落在上述天花板之上时，这才直接阻止
当前R供给完成simple门；本轮该几何Q上界仍待独立供给。
反之即使拿到u<2e−31，也仍需真实odd/second-even finite lower sign门，
不可将finite R排序代替它。

## 6. 本轮改变与唯一下一消费条件

已取得whole-inertia合法运输、coarse actual min–max计数，以及当前R固定
供给的source-paid odd threshold上限；没有取得simple-even实际谱隔离。
一般条件归约不计合同成功，(C)的边界范围也仅是这个固定tail supplier。
原C009正性保持；不以辅助negative或小upper反推Q负/RH。

唯一仍值得消费的下一动作是核独立geometric actual even upper与当前R的
odd/second-even ceiling是否有可行交集；若无，则停该固定supplier的排序
路线，重准入须新的signed正尾供给或同对象更强lower comparison。
不扩大原pilot N，不调整C00112组，不恢复C008等待/暂停路线。
本辅助无pending process，STATE/cadence由主代理统一结算。

## 7. actual even geometric upper：不同组织独立精确验收

这是同一轮后续消费审查，不另计轮。已只读核
`geometric-source-audit.md`、`sonin_source_geometric_upper.py`、
`sonin-even64-rational-source.json`及`sonin-even64-geometric-upper.json`。
没有运行会覆盖原source/output的脚本；独立用std-lib Fraction重算。
固定rational source SHA为
`4bd25aab1f1574ae156884aedef90829f047a328cd2f897330b3311b6e83ff1c`，
原自行编写脚本SHA为
`8dbc244f2099fbd4c9c0262b04ddab1a1ff6474a3ae46d56293763a71ffb0ff3`。
vector proposal来自既定even64 geometric R压缩，非零点拟合；冻结为
64个exact rational raw coefficients后，proposal精度不构成证明前件。

### 7.1 完整endpoint Fourier身份与符号

令f=indicator_I sum c_n P_n(u/L)，n=0,2,…,126。
真实norm是`sum c_n²·17/[8(2n+1)]`，本次独立Fraction计算严格>0。
endpoint derivatives用

    d_k=f^(k)(L)=L^-k sum_(n>=k) c_n (n+k)!/[2^k k!(n−k)!]

正确。因f在有限区间是even polynomial，从`F=2 integral_0^L f cos(tu)du`
成对分部积分：第一步是+f(L)sin(Lt)/t；第二步是+f'(L)cos(Lt)/t²；
再一对变为−f''(L)sin(Lt)/t³、−f'''(L)cos(Lt)/t⁴，依次交替。
u=0的sin项为0，odd derivatives为0，没有藏住origin boundary。
第127导数为0，所以到degree126完全终止，zero-extension不光滑的
端点效应正由这些boundary项支付，不能删去它们。
由此精确得到原S/C表示：

    F(t)=2[sin(Lt)S(t)+cos(Lt)C(t)],
    S=sum_j (-1)^j d_(2j)t^(-2j−1),
    C=sum_j (-1)^j d_(2j+1)t^(-2j−2).

`|F|²<=8(S²+C²)`为保守正确界；甚至Cauchy–Schwarz可给4倍，但本次
不改变原预算来提高结果。两个series内部的所有signed cross必须保留。
本次独立组织直接成对endpoint indices的积分（diagonal计1、off-diagonal
计2），没有调用原convolution字典或作者module；所得I0/I1/I2/J均为
严格exact Fraction，逐个非负。
负系数没有逐项absolute化或错误向上round，而是所有rational cross先精确
相加；它们作为integral of square或log times square的非负性可核。

### 7.2 actual Gamma tail与向外constants

Binet使用z=5/4+it/2的同一actualGamma规范。recurrence中
`−Re(1/(2z))−Re(1/(1/4+it/2))`均非正，upper可舍；
Binet remainder绝对值<=1/(15t)；
`Re logz<=log(t/2)+25/(8t²)`由log(1+x)<=x。
所以完整尾的weight满足

    A(t)−7/2 <= log(t/(2pi))−7/2+1/(15t)+25/(8t²).

actual weight在t>=256为正，已由C009 exterior C独立支付；
该upper亦正，所以能将F²上界相乘，未因signed weight反转方向。
实even F的正/负半线合并给1/pi，不是1/(2pi)；最终8/pi因子正确。
有限带之外的完整Gamma没有被删除，prime/pole已在head精确保留。

Machin160的even-length alternating partial是lower，下一正项给upper；
`16atan(1/5)−4atan(1/239)`的负系数方向正确。
对x=128/pi_lower进行2的range reduction后，x∈[1,2)，atanh的positive
series和geometric尾给log上界；log2 likewise用z=1/3，不借浮点log。
所有最后constants向外round到256bit dyadic。
I0非负，故用log_upper−7/2与pi_lower把tail向上运输合法。
我独立重算了这三个constants，与原JSON逐个exact相等。
JSON `tail_source`简写漏掉右侧−7/2，仍是较弱的true upper；真正计算和
audit均使用上述较强式，没有因这段metadata缩写低估budget。

### 7.3 head source费用、结果重算与合法原源upper

head仅用Araw+J0raw，即M+K；不能加入U后再加整个tail。
已核source bytes绑定，endpoint sums/2^257及真实raw Gamma正确。
本次独立只遍历存储upper-triangle，diagonal计1、off-diagonal计2，
重新算head Fraction，支付`epsilonA+epsilonH=2^-204+2·2^-220`。
已包含原full-operator kernel及primitive norm误差；没有把它当raw entry费。
tail直接用固定rational源解析计算，故不再扣或加U的sigma。

独立计算的最后向上dyadic与原结果**精确相等**：

\[
u=\frac{7954159549289785371664718615168914673915149}{2^{256}}
 <7\cdot10^{-35}.
\]

用于核对的display数为：head/norm≈5.051587961666327e−35、
tail upper/norm≈1.817758296511737e−35、u≈6.869346258178065e−35。
这些display不参与任何比较；最终门由完整Fraction和integer判定。

该f为finite zero-extended polynomial，Fourier=O(1/t)，log-weight能量有限，
所以f∈Dlog。保evenness的缩支撑+even mollifier给Cc∞ even form-core逼近，
norm及Q收敛，严格u<7e−35还容许选足够近的合法smooth even source。
因此可消费真正同窗结论

\[
\lambda_1(Q_{even})\le u<7\cdot10^{-35}.
\]

它不只界R，不借任何作者Q数值、zeta zeros或未知RH。
和537的全域tau下界合并给真正lowest在[tau,u]的enclosure，但不认证
ground属于even、更不认证simple，因为odd或第二even可能更低。

### 7.4 更新后的唯一未付门

§6的actual even upper前件现在已付。u严格低于§5的Rodd ceiling，
所以当前fixedR supplier**尚未被这个ceiling排除**；不能因此止损或
声称方法类全失败。仍需一个严格s>u的actual
`N_Qodd(s)=0`及`N_Qeven(s)<=1`全源门（可由§2–4的safe matrices/frame支付）。
64阶ordinary R排序与有理R upper只给提案/ceiling，均不能替代这些lower。
唯一下一动作变为核该阈值的完整shifted source/inverse/congruence/inertia
或codimension-frame sign；若只有条件公式/finite排序，则C010仍未完成。
本补审没有pending process，不改STATE/cadence/git，不扩N。
