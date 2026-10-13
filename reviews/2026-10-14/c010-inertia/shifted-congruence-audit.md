# C010：same-congruence shifted finite matrix 独立审查

2026-10-14，同一研究轮辅助。恢复AGENTS/README/STATE/check/show及C010；
Goal仍active。原tex固定为
`tmp/c009-liu/w200-pub-2026-09-14/publication/manuscript.tex`，
主要核538–666、1802–1890及原03/04 core compiler纯文本。
只写本文件，不改STATE/cadence/git，不运行原外部code，不做224阶全乘法。

## 1. 结论

主代理给出的Pt与两个Kt公式成立，非交换顺序、正congruence尺度、
17/L²/Gram/S0/Cw因子正确。这是经原source费用支付的finite lower型的
条件归约，不是已经付了shifted惯性的证明。

重要额外条件：旧dclear不清移位后的新分母。t=10^-34时四correction
系数的精确Fraction分母bit lengths为75、750、750、750，故Kt通常为
rational Hermitian，不能用原integer checker前将每项截为int。
需要新的positive common-denominator清分母，或者从头采用exact rational
sign/inertia证明。没有必要改变正congruence本身。

## 2. shifted safe lower型及误差顺序

记完整下比较R=M+K+U，Q>=tau I+R。保守取t=s=10^-34丢tau时，
`Q−sI>=M_t+K+U`，M_t=M−tI，m_t=m−t。
独立Fraction核`0<t<m−n`，所以正complement仍成立，inverse合法。
A_t=A−tI，B_t=B−2tA+t²I，D_t=B_t−A_t²=D。
故D0=B0−A0²及原epsilonD原样保留，不能删费或按shift独立差再重复扣。

对0<t<m，functional calculus给

    G_t=E*(M−tI)^-1E <=(1−t/m)^-1G0,
    W_t=(1−t/m)^-1W0 >=G_t>0.

原W0的norm8、source-centering与inverse-upper费用已经付；这里只乘精确
positive scalar，不需再次使用原trial去近似M_t^-1。
恰有`W_t^-1=(1−t/m)W0^-1`。
以m_t重算原alpha/beta（theta=2^-48、chi=1固定）后，

    Pt=P0−(t/m)W0^-1−DeltaAlpha I−DeltaBeta(D0+epsilonD I).

这严格来自22逐项相减，J/H0/Uhat等未变。独立Fraction核
DeltaAlpha、DeltaBeta均正，display分别约2.87556214321024e−85、
2.4963393060256444e−45。D0+epsilonD I>=D>=0，所以Pt<=P0。
但原P0 PSD或原K0 Gram不支付Pt的惯性，需要新sign门。

## 3. 独立从正congruence逐项推Kt

原S0=2^257、Cw=29·2^769、T0=17·29·607630911·2^1282、
d=dclear=9617[9617·2^435−325(896·2^250+1)]>0。
原q_j=8(2degree_j+1)，使用真实Legendre degree；
Gamma=17Qd^-1，a/S0与braw/S0为raw M/M²中心。
V=Cw Qd Wraw Qd，其中Wraw=Gamma^(1/2)W0Gamma^(1/2)。
原Bc=Qd^-1/2V/(sqrt17 Cw)，Lambda=d·289 Cw²T0>0。

不预设交换性，直接计算给

    Lambda Bc* W0^-1 Bc =d·289 Cw T0 V,
    Lambda Bc* I Bc =d·17T0 VQd^-1V,
    Lambda Bc* B0 Bc =d·T0/S0 VbrawV,
    Lambda Bc* A0² Bc =d·T0/(17S0²) VaQdaV.

第一式用`Wraw^-1=Cw Qd V^-1Qd`，第二式保留Gamma，
第四式的middle Gamma^-1=Qd/17不能删。raw J0已含原L²换元，
此次没有额外L²乘法；前面17和289来自Gamma/congruence而非重写source。
故在同一固定Lambda/Bc下，Kt=Lambda Bc*PtBc，确为

\[
\begin{aligned}
K_t=K_0
&-(t/m)d\,289C_wT_0V\\
&-d\,17T_0(\Delta\alpha+\Delta\beta\epsilon_D)VQ_d^{-1}V\\
&-dT_0\Delta\beta/S_0\;Vb_{raw}V\\
&+dT_0\Delta\beta/(17S_0^2)\;VaQ_daV.
\end{aligned}
\]

A0²项的正号由`−DeltaBeta(B0−A0²)`产生，不是正prime权额外供给。
原code中的`(aV)*Qd(aV)`等于VaQdaV，需要a,V自伴；
未将aV与Va混为可交换对象。

## 4. symmetry、combined kernel及新分母

原a,braw都是real symmetric中心；1840–1843中Z+Z*、Z*QdaQdZ、
Z*QdbrawQdZ、aQdZ+Z*Qda均自伴，所以V为real symmetric。
其定义来自W0>0，因此V>0、Bc nonsingular，先于目标sign。
Qd diagonal严格正，V列divisible by相应q_j的整数性质原C009已付。

令Y=VQd^-1、F=aQda−17S0braw，则Y通常不自伴，
必须保留`Y*=Qd^-1V`。逐项展开

    Y[−d17T0(DeltaAlpha+DeltaBeta epsilonD)Qd
      +dT0 DeltaBeta/(17S0²) Qd F Qd]Y*

恰给上式的I、B0、A0²三项。再减inverse项即原combined候选。
它保留所有非交换顺序。独立3×3、非commuting real symmetric a/b/V的
exact Fraction核对两种correction组织，结果逐单元相等；这只检查代数，
没有用小模型sign替代actual224阶惯性。

独立清分母检查四个scalar

    (t/m)d289CwT0,
    d17T0(DeltaAlpha+DeltaBeta epsilonD),
    dT0DeltaBeta/S0,
    dT0DeltaBeta/(17S0²)

均严格正rational但不全integer，分母bit lengths为[75,750,750,750]。
因此旧03/04 integer cap/assert/integerGram接口不能无修改消费Kt。
这不否定数学公式；如真需构造，取四分母的positive LCM乘Kt即可。
原dclear只用于固定t=0的alpha/beta清分母，其原bit constants不能假定
对新阈值仍清所有分母。新清分母不改变惯性，但新矩阵实际bit长度及
residual尺度必须另核，不继承原3353bit的Gram费用。

## 5. 惯性方向与停止条件

Lambda>0、Bc可逆，故`n_-(Kt)=n_-(Pt)`。完整source和positive complement
已付后，whole bound方向是

    N_Q(s)=n_-(Q−sI) <=n_-(M_t+K+U) <=n_-(Pt)=n_-(Kt).

不是n_-(Q−sI)=n_-(Kt)，亦不能从Kt负方向推出Q负。
odd Kt PSD与even Kt至多一负，再合actual even upper u<s，才给simple-even。
当前只核公式，没有新的完整矩阵惯性/frame sign，不能晋级whole lower。

本次实际u是已验收的dyadic

    u=7954159549289785371664718615168914673915149 /2^256 <7e−35,

所以t=s=1e−34满足u<s，但还不支付任何odd/second-even lower。
source代理若在原whole224 odd R中取得source-paid rational upper c<u，
应首先核更精确的`c+tau<u`（保留原positive tau时）；该严格gap会排除
**当前固定R供给、当前冻结u上界门**的odd零负惯性。
此时没必要重建昂贵Kt来验证早已不可能的固定门；source trial仍只界R，
不能当Qodd上界，且更强tail supplier或更好的actual even upper未被排除。
本review不预先消费尚未落盘的ceiling，不扩大C001/pilot或ζ拟合。

## 6. 固定一次全有限门：代码、prereg与精确向下目标

主代理随后明确授权与source协同执行唯一s=10^-34门；
只读审查新`shifted-inertia-preregistration.json`及自行编写
`scripts/c010_shifted_inertia_certificate.py`。完整224×2是原448 head，
不是扩大pilot/C001。固定80digits只用于proposal，未另sweep阈值/精度。
source实际一次进程结束，两个sector全row门通过。

新script四个Fraction correction、positive LCM D、ci/cd/cb/ca与§3–4一致。
其D为824bit，两个Kinteger为4177bit，真实
`Kinteger=D·Kt`。原source SHA、四个V/oldtarget SHA及其degree/shape/完整
raw键表经独立mapping审查和root reader再次绑定，见
`shifted-source-mapping-audit.md`、`independent-shifted-gram-result.json`。
旧原targets不能替换成只有同名的不同object，也不能只验新Gram而丢input链。

令B=max|Kinteger entries|bitlength，H=2^512 Kinteger/2^B。
脚本对每个entry执行integer floor（负数也向负无穷取整），L=floor(H)，
再取T=L−224I。实际逐entry验证0<=H_ij−L_ij<1。
E=H−L对称，||E||<=max absolute row sum<224，所以E+224I>0，
从而正确完整Loewner下界是

\[
T/2^{512}\preceq(D/2^B)K_t. \tag{C}
\]

没有假设entrywise positive E就是PSD；224I支付全部row norm。
实际旧live receipts曾把positive scale字符串写成D·2^B，数学实现始终(C)。
该文字错由独立mapping审查报出，当前script/prereg解释已修；旧receipt
历史保留，应另记correct interpretation而不重跑/改整数对象。
本审查严格只用D/2^B乘Kt，绝不用Kt/(D·2^B)，也不运输新scale为Rayleigh常数。

## 7. rank-one、guard及独立全row门

odd取target=T，无rank update；even取

    H_even=T_even+2^23 w w*, w∈Z^224非零。

对应512-grid的actual rank update是
`rho |w/2^192><w/2^192|`，rho=2^-105，因为512−105−2·192=23。
所以正号、正系数与rank<=1严格成立。
w不须实际特征向量、norm1或与精确ground对齐；其80digit来源仅proposal。
更新型PD仅给原T_even至多一负，绝不能直接说原T_even PD。
无需以一个未经认证的frame近似正交代替rank-one事实。

guard g=2^372在512-grid对应2^-140。
ordinary Cholesky对`(H−gI)/2^512`仅提出L；floor到256-bit整数factor F
后，F F*恰为512-grid，不需要额外乘/除2^512。
只要完整整数residual E_H=H−FF*−gI满足每row absolute sum<g，
便有H>=gI+E_H>0。floor factor或mp误差不作前提，全部由这一exact门支付。

root另写且实际运行`c010_verify_inertia_gram.py`，不导入producer module或
PASS标签。最终版本先核5个固定原input hashes和新compile/target/factor
hash绑定；矩阵全224×224 integer/symmetric、original parity indices、
guard/grid与rank系数均强制验证。producer储full-square factor且upper为0，
reader现在明确检验upper zeros，亦可接受triangular schema；
最初reader要求三角row长度的问题已修，是存储接口问题，不重算factor。

reader只逐下三角计算Gram，但offdiagonal absolute residual计入对应两row，
diagonal一次，所以每块224行的**全行**范数确已支付。
每块25200个triangle entries、两块448rows均完整覆盖；不是只抽diag/pivots。
actual结果`independent-shifted-gram-result.json`为pass，
两块max row residual均263bit<g=2^372，strict floor>0；
两个wrong-sign diagonal控制由同一完整row门拒绝。
我另读所有result row sums、直接核长度/strict guard、packet rank非零、
target/factor bytes hash以及reader code hash一致，没有覆盖原结果或冒称
重复跑过昂贵finite编译。

最终独立reader code SHA：
`9853a5022f0911bd6406d9f8a3297fdc5b3dcfd35ad285fb08a3309c5167ec59`。
当前producer code SHA：
`5dd87f78fcf2e68e0b7c1908bc8ceb056d43da628403b54bcac67ce1a2faf72e`，
对应修正metadata后的bytes；不倒称这是旧live字段版hash。

因此实际有限门已付：T_odd>0；T_even+positive rank-one>0。
任何二维strict-negative子空间与w⊥有非零交，故rank-one正更新PD严格
推出n_-(T_even)<=1，无需任何eigenproposal认证。
结合(C)的positive scale及正congruence，得到

    n_-(Pt_odd)=n_-(Kt_odd)=0,
    n_-(Pt_even)=n_-(Kt_even)<=1.

这里第二行不宣称Pt_even PSD，不把lower目标的数值谱当Q spectrum。

## 8. 最终whole-form运输与真正simple-even结论

原C009 actual source/error、正尾、m/complement与samecongruence链已付，
本次t=s=10^-34保持m−t>n，原D/epsilonD不变；
W_t合法upper与alpha_t/beta_t费用已由§2支付。
所以本次finite signs通过完整Block–Schur的strict-negative计数给

\[
N_{Q_{odd}}(s)=0,\qquad N_{Q_{even}}(s)\le1.
\]

另一方面不同组织的actual geometric even bound（full-inertia-audit §7）
给lambda1(Q_even)<=u<s。其trial为非零closed-domain source且有保even的
smooth form-core逼近，因此N_Qeven(s)>=1，最终**恰为1**。
closed compact-resolvent接口确保真正eigenvalue attained；
odd无s下谱，even恰一个s下eigenvalue（按complex multiplicity计），故
同一actual fixed-window operator的ground是simple且even。

可以消费的完整同窗结论为

\[
\tau\le\lambda_1(Q)\le u<s=10^{-34}\le\lambda_2(Q),
\quad \lambda_1(Q)\text{ simple and even},
\]

其中lambda2为完整complex Hilbert谱按重数的第二值，不仅是第二even。
gap也有严格exact门：

\[
\lambda_2(Q)-\lambda_1(Q)\ge s-u>3\cdot10^{-35}.
\]

我独立Fraction重算s−u>3e−35；display为3.1306537418219355e−35，
display不参与验证。这不是从537的旧coercivity或finiteR排序猜得，
而是新actual upper加完整shifted source/rounding/congruence/inertia门。

结论严格限于L=17/16、Lebesgue L² norm、同actualGamma/dual pole/全部prime
powers及Dlog closed realization。原Cc∞(I;complex)源下界与其闭型域兼容，
不需要pole矩零或RH；没有认证其他窗/成长S/U、prolate/Ξ相认、ζ谱可见性
或RH。trueQ simple-even可明确声明，当前宏观Goal完成须另按实际完整门槛
审计，本文件不因一轮或合同成功自行修改Goal/STATE。
