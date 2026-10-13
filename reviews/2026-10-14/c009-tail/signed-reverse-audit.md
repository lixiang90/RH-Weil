# C009：signed 尾供给、全 prime Schur 与辅助缺陷逆审

2026-10-14。固定原件为
`tmp/c009-liu/certified-weil-positivity-b6cd2183c1e79c6c27a34267812a7b2d73ed1b59/frozen-source/publication/manuscript.tex`。
行号均指该 tex。只读审查同版本 `frozen-source/reproduction/scalar.py`，
没有执行外部代码，没有改 STATE/cadence/git。恢复 AGENTS、README、
STATE、check/show、Goal、C009 与 D20261014G，核实际 HEAD
`3d9bbbfef989e0962d32f6af512b13bd6cd6a3ba`。本辅助不另计研究轮。

## 1. 结论

在本次核读的解析链中，没有发现可推翻 Theorem B 的符号、算子域或
遗漏 prime-power8 的反例。尾供给不是先假设有限正性：定量 Fourier
补空间估计独立给正下界，rank-two 供给由正型平方完成得到；全 prime
算子 M 的下界独立由 weighted Schur 支付。随后非交换 block-Schur
与 source-centered 误差运输方向成立。

已用本仓自行组织的 Fraction 算术重算七个 Schur cell，结果与原文
1969–1976的七个完整分数逐个精确相等；另重算了 projection、pole、
tail-column 和 unit-window two-block 的关键标量不等式。
这只支付解析/标量叶子，不证明原 finite targets 及源到整数证书全链。
`scalar.py` 或 Gram PASS 标签均不单独认证 Q 正性。

原 Obstruction 的 carrier 机制正确且可独立重建，甚至给该指定辅助型
无限负指数及有限连续约束仍失败的推论。但其对象为删除正尾后的
`D_chi=Q−S_chi`，不是 Q；不能导入为完整 Weil 负源、所有 localization
边界或 RH 后果。

## 2. 保留实际完整对象与正尾

97–142：源是任意 complex `Cc∞((-L,L))`，Fourier 取 `exp(−itu)`，
Gamma 为 actual `Re psi(1/4+it/2)−log pi`，prime 系数 `2 Lambda(n)/sqrt n`。
pole 是 `2 Re[F(i/2) overline F(−i/2)]`，不是强加矩零。
261 的 kernel `2cosh((u−v)/2)` 正好给该 indefinite pole：
even 正、odd 负，两者均保留。辅助 bounded operators 可作用全部 L²；
原 Q 最后仅在合法 smooth domain 消费，未借非法角 trace 或谱基换和。

246–272：L=17/16 的全部 prime powers 恰为2,3,4,5,7,8。
M=7/2 I−C_p 保留完整移位作用，K 保留低频 Gamma 与完整双 pole；
高频未被删除，而是以非负 form T_tail 独立保留。恒等式
`Q=<f,(M+K)f>+T_tail(f)` 在 smooth domain 精确，不能把 M+K 单独当 Q。
压缩 M 的平方必须是 `E* M² E`，并非 `(E*ME)²`；二者差 D_M
就是全 prime 向补空间耦合的费用。

## 3. 独立正尾与 rank-two 供给

1059–1117 的全 L² Fourier-band complement 证明可核。
归一化 norm1 后 `|F^(j)|<=sqrt(2L)L^j<2L^j`。
如果外部能量 E<1/2，带内 integral>pi，故某点 |F(t0)|>1/16。
4096 个宽 h=1/32 的相隔小区间全在256..512外部；均值给
`|F(x_j)|<=sqrt(2pi E/h)<16sqrt E`，节点间距至少 h|j−k|。
插值距离<768，用 factorial 分母求和给
`sum |ell_j(t0)|<=49152^4095/4095!<2^24570`。
取适当固定相位的实部，实 Lagrange remainder 有效，余项
`2(768L)^4096/4096!<2(3/5)^4096<1/32`。
因此 `sqrt E>2^-24579`，即 `I−B_band>=delta I`，delta=2^-49158。
这里没有预设未知有限矩阵正性，也没有排除 complex 源。

1125–1137：已由 Binet 独立给 exterior weight
`A(t)−7/2>C=123/1280>1/16`，故 `T_tail>=C(I−B_band)`。
该不等式可按扩展值解释，不把 unbounded 原 form 假装 bounded。

令 S=I−B_band−delta I，正 contraction；v0、v1 是正交 parity vectors，
`<v0,Sv1>=0`。对复系数 z0,z1 完成 S 型平方，确得

    <f,Sf> >= sum_j |<Sv_j,f>|²/(e_j−delta).

原 Fourier e0/e1 积分与归一化正确。1182–1184 可由 sin²/cos² 拆分及
一次分部积分核读；e1 的 cross term 按绝对值支付，符号无反转。
e_j>2^-11>delta，`81e0<C`、`27e1<C` 严格成立。
所以 C/(e0−delta)>81、C/(e1−delta)>27，且 Cdelta>tau=delta/16。
这给 `T_tail>=tau I+U`，U 为真正正 rank-two，但其存在不意味着
整个 tail 只是 rank-two。正 mass tau 来自全补空间下界。

本仓独立 Fraction 重算通过：81U0<C、27U1<C、
U0<1/29²、U1<9/2500（Uj 为原上界）。因 S²<=S，
`||h_j||²=<v_j,S²v_j><=e_j`；故两列 norm 的严格界正确。
列误差 eps 引出的 rank-one 费用
`2(81/29+81/50)eps+108eps²<9eps` 也正确。
它是正规化源 L² 列误差，不能把 raw coordinate 单项误差直接当 eps。

## 4. 全 prime8 weighted Schur 的独立验算

1241–1249 的正 weight q(u)=1+(5/8)(u/L)²，用 complex Young 支付
paired shift 的 Hermitian quadratic 值，给
`|<f,C_p f>|<=integral r_q |f|²`。这是完整 C_p 的 L² norm 界，
不要求其移位彼此交换，也不需要未知低谱 sign。

权重 w_n=Lambda(n)/sqrt n，shift t_n=log(n)/L；n=4,8的权重仍是
log2，位移才分别用2log2、3log2。本文和 scalar 都正确区分。
有理 log64 的正 atanh series及几何尾确夹住所列1e−6端点，
根端点由整数平方验证。已自行重算这些夹界，没有导入外部脚本结果。

七 cell 通过负位移允许稍早、正位移保留稍晚覆盖真实 support switches。
对负位移 numerator 的 `−2xt` 用 t_lower、t²用 t_upper，正位移二者
均用 t_upper，且每个非负 numerator 整体用 w_upper；因此1333–1334
的下界方向成立，没有将负线性项错用上端。
端点之外不活跃项的安全覆盖亦已逐个精确检查。

七个 quadratic 的端点/内部凸 vertex 最小值独立 Fraction 重算，逐个
精确等于1969–1976原分数。以下小数仅显示，判断用精确分数：

|cell|minimum approximately|
|---|---:|
|1|1.35274576138426|
|2|0.32319706668115733|
|3|0.038113034020350565|
|4|0.9050243583542271|
|5|0.13484944606594515|
|6|0.04383547760939146|
|7|0.20607489576513405|

均严格>3/100，因此 `r_q<83/32−(3/100)/(13/8)=26783/10400`，
给 m=9617/10400、b=63183/10400。特别 m>29/32>0，先于 finite target
sign；原证明没有借已想证明的 Q 非负来定义 M inverse。

## 5. 投影与 two-block 误差阶数

1367–1379：Legendre best approximation/Chebyshev ellipse majorant 中
L 的 measure factor保留正确。独立精确重算
`153*68^227*2^1085 <25^227*3^896`，所以 uniform band residual norm<r=2^-95。
1383–1389：Taylor pole 残差及两个 rank-one 差给36/448!，独立重算
其<2^-440。pole 不按正型丢弃，负 odd pole 也支付。

每个带内 rank-one kernel 的 head/full vector norm<sqrt(2L)<3/2，
cross 用 `kappa*(3/2)*r`，complement 用 `kappa*r²`。
kappa<896 由有限-band Gamma 上下界支付；原 digamma split tail 的
`128² sum_(n>=256)n^-3<=129/1024` 方向正确。
两列 outsideP norm<10r，由 Cauchy–Schwarz 加 Plancherel 得到，
无 source derivatives 或未经准入的 angle evaluation。

U 的 cross<`10(81/29+81/50)r<45r`；U complement 本身为正，
对 lower estimate不扣它，对绝对norm则必须加
`(81+27)*(10r)²=10800r²`。故1406–1418中

    e=1389r+p, n=896r²+p, h=11696r²+p

分别用于 cross norm、complement负费用、complement绝对norm，
分类正确。没有将全误差一律算成一阶 r，也没有把 positive U 的 norm
错误归零。p 的 pole 误差在每个适用界中保守重复允许，未遗漏。

538–640 的一般 Certification theorem 可从独立完成平方验证。
M_c>=mI保证 inverse 合法；G^-1=A−F*M_c^-1F、D_M=F*F。
将 f=Tc+y，T=E−M_c^-1F，先严格消去原 M cross，而不是假定 M commuteP。
R00=0 后 head correction>=−e theta I−(e/theta+n)m^-2 D_M。
新 cross Z=R10+R11 L_c 的范数平方由 complex Young 给
`Z*Z<=(1+chi)e²I+(1+chi^-1)h²m^-2D_M`。
补空间>=m−n，余下完成平方恰对应18的 alpha/beta。
这是充分条件而非必要条件，不反推出失败 target 等于 Q 负。

644–666 的 source-centered方向正确：epsilonD支付 B 与 A² 的误差，
`D_M<=B0−A0²+epsilonD I`；W>=G>0给 W^-1<=G^-1。
因此22的 finite PSD足以给19。401–411的 residual identity也正确，
`mu^-1 I−M^-1>=0` 使用 mu<m，先于目标 sign。
X norm<=8及 orthonormal coordinate错误界仍须原完整证书支付。
670–682 的正 nonsingular congruence与每个Hermitian residual行和给
complex PSD；这里只运输 sign，故无需错误地用fullrank运输定量gap。

167–209及Appendix A的unit-window bridge另需其finite premise；不能由B较小tau
推出A较强constant。自行精确重算了
`(2^-150−2^-151)(1/32−2^-151)−2^-166>0`，这是A two-block的
正确条件式，未认证A retained finite matrices。

`scalar.py` 文本审查：Machin两交替方向、e余项、atanh log尾、integer roots、
negative coefficient方向及精确factorial/幂比较成立；其输出明写
`AfinitePremiseProved=False` 和 scalar-only scope。代码由std-lib执行叶子
而非读取历史PASS；安全功能本身不构成数学认证。本次未直接运行它。

## 6. 独立重建 Obstruction，及它真正约束的对象

445–528 对任意固定 real chi∈Cc∞((-1,1))、norm1，rho_chi是偶实相关，
rho(0)=1，1−rho(x)=O(x²)，support在(−2,2)。Fubini身份合法。
15的连续 kernel 在0的奇性被该二阶零抵消，形成固定窗上的 continuous
integral kernel，故 compact（直接为HS）。

更直接的算子组织如下，避免先引用 Obstruction 标签：
R1=beta0 I+compact（finite-band连续kernel加finite-rank双pole）。
局部化积分 M_chi 的identity部分仍为beta0 I，kernel部分乘rho_chi，
仍连续，因此 M_chi=beta0 I+compact。故

\[
D_\chi=\beta_0 I-
\sum_{\log n<2L}c_n(1-\rho_\chi(\log n))J_{\log n}+K_\chi,
\quad \beta_0=1/16,\quad K_\chi\text{ compact selfadjoint}. \tag{A}
\]

选择a=log8，L>a/2，两个等形极小smooth bumps中心±a/2；窄度d取原值
`min(1/256,(L−a/2)/2)`。这使self相关避开log2，cross相关避开所有
integer log，除log8（最近7/9的严格gap已足够）。支持严格合法；
H_g(a)=||g||²/2，rho_chi(a)=0。modulation T_k=2pi k/a使prime8相位为1。
连续compact项对weak-zero carrier趋0，故(A)立即给

\[
D_\chi(e^{iT_k u}g)/\|g\|^2\longrightarrow
1/16-\log2/(2\sqrt2)<-1/8.
\]

factor c8/2=log2/(2sqrt2) 正确；其他 actual primes不是随意删除，
而是该固定合法源相关精确为0。极点在compact项中，不当作消失moment。
原对compact repair的结论成立；fixed compact费用沿carrier确实趋0。

附属但可核的后果：D_chi负谱子空间无限维，否则有界自伴算子的有限
负谱部分compact，而其非负剩余型与上面的weak-zero负limit矛盾。
任意有限个L²连续linear源约束也不能删掉这些负方向：取独立约束的
fixed smooth correction vectors，从carrier减去其约束坐标；这些坐标
由weak-zero趋0，源仍smooth、修正L²趋0，bounded D_chi的负limit保留。
亦可选任意N个充分分离的carrier，cross相关趋0后得到N维strict-negative
Gram，再作相同finite correction。于是所有fixed compact/finite-rank
修复及finite continuous条件均失败于这个**指定 D_chi 方法类**。

但是16保留 `Q=D_chi+S_chi`，S_chi为真正非负外部form。
S_chi可能且必须沿这些carrier提供至少
`log2/(2sqrt2)−1/16` 的归一化补偿；原14量词只对这条序列及同一对象。
它不是额外假设全Weil负值，更不排除noncompact supplier、其它localization
或 signed全源机制。Theorem B正是保留另一正尾供给来避开这个逃逸，
与该Obstruction不矛盾。

## 7. 净输入、未付链与下一动作

本逆审独立支付：fullprime8 L² lower/upper比较、定量全源 Fourier补空间、
合法 rank-two tail supply、非交换 block-Schur/error阶数，以及指定
tail-dropping比较的精确负carrier机制。没有发现本段解析失败，因此不能
仅以常数极小或有限维证书语言为由止损。

仍未支付的是原 source primitive intervals到A0/B0/H0/Uhat的完整矩阵
operator误差、trial inverse norm、两个精确congruence、完整integer targets
及每个Gram residual单元和行。finite positivity标签、scalar PASS或少量
矩阵抽样不能替代这些前件。Theorem A的retained packet与B fresh source
也必须分开，不把一者的重放当另一者证明。

下一唯一动作应由主代理核原完整证书可得性与source/error/sign桥，按
已读代码选择最低费用的完整消费；若完整链缺失再明确止损。本辅助没有
pending process，不等待C008、不给成长窗/RH/lowest结论，不新增runtime Goal。
该指定辅助方法边界虽属actual arithmetic，规模不能独自冒充新的宏观
完整Weil进展；此前535的大方法边界完成判断保持其原范围。

## 8. 最后消费审查：新 fresh targets、正 congruence 与闭型域

这是同一研究轮的最终不同组织逆审，不新计轮。主代理随后完成了
`tmp/c009-liu/fresh-b-20261014` 的 FULL_REBUILD，当前原 fresh result
记56个scalar checks，完整数值阶段退出成功。它不含Theorem A。
我另读本仓 `scripts/c009_verify_gram.py`，核其逐单元/逐行逻辑与
`independent-gram-result.json`，并核该receipt所绑定的两个target与factor
SHA仍和当前fresh文件完全相等。没有运行原外部代码或重复FAST。

### 8.1 独立有限 sign 门

自己的 std-lib checker 强制两个224阶实对称整数target、正确原Legendre
parity indices、三角integer factor的完整shape，计算每个下三角单元

    K_ij −2^2329 sum_(k<=min(i,j)) F_ik F_jk −2^2873 delta_ij.

off-diagonal绝对值计入对应两行，diagonal只计一次，所以确是完整
Hermitian residual的absolute row sums，不是只验下三角半行。
全部448行各自strict<2^2848，因而每块
`K >=(2^2873−2^2848)I >2^2872 I`。
factor乘积为真正 Gram，complex向量也适用。
当target第一个diagonal改成负2^3353，同一完整测试拒绝，negative control
正确。target实际bit length 3353与原b_s scale给2329/2873一致；本次需要
的是sign，故即使不用该metadata解释，直接整数identity本身已给正矩阵。
原标签不参与checker的正性判断，且我核了输出各224个row sum的长度与
严格门及绑定hash。这个门独立于source/analytic预算。

### 8.2 不以“两个编译器一致”替代正确性

独立从22及Gamma=17Q_d^-1推导，不先假定1821–1890正确。
定义W_r=Gamma^(1/2)WGamma^(1/2)、V=C_w Q_d W_r Q_d。
原Bc可改写为 `Gamma^(1/2)V/(17C_w)`。对任意raw matrix R：

    Bc* [Gamma^(-1/2) R Gamma^(-1/2)] Bc
      = V R V/(289 C_w²),
    Bc* I Bc = V Q_d^-1 V/(17 C_w²),
    Bc* W^-1 Bc = V/C_w,
    Bc* A0² Bc = V a Q_d a V/(289 C_w²·17 S0²).

第三式使用 `W_r^-1=C_w Q_d V^-1 Q_d`；不交换非commuting矩阵。
将22乘正因子 `d_clear·289 C_w² T0`，kernel/retainedU/inverse项成为
d_clear K_*，人工引入的lambda_*由c0项精确消去，剩余A0²/B0项恰为
`−c1 V b_raw V+c2 V a Q_d a V`。故1877–1879是真正正congruence，
没有漏17、L²、Gram或inverse因子。

另外独立用Fraction从m,b,e,n,h,theta、epsilonD和lambda_*重算
`d_clear,c0,c1,c2`。四者均严格正integer，bit lengths精确为
462、1704、1489、1228，`c1=17S0 c2`。再用03-core_checker里的
展开整数公式自行重写同一计算，四个integer与Fraction结果精确相等。
不是只比producer/checker最终标签。
1890的combined kernel由Y=VQ_d^-1及F=aQ_da−17S0b_raw展开后，
恰恢复1879四项；使用V自伴及原真实度数q_j，而非本地sector index。
因此matched compilers潜在共同代数错误已由独立22推导排除于此链。

### 8.3 W正性与norm8费用

每个fresh trial的整数Z已独立读取并重算
`sum q_i q_j Z_ij²<=2^518`；两个实得分子均517bit。
X=Gamma^(1/2)(Q_dZ/2^256)Gamma^(-1/2)的entry恰为
`sqrt(q_i q_j) Z_ij/2^256`，故Frobenius²<=64，operator norm<=8。
direct-sum取两sector operator norm的max，不误加两个Frobenius²。

原mu=29/32<m，residual identity给 `U_mu(X)>=G>0`。
source-center差额仅来自A/B，任意normX<=y的费用为

    [y²+mu^-1(2y+y²)]·2^-220.

y=8给 `4416/(29·2^220)=DeltaX`，故W>=G>0，在target sign之前合法。
从W_r反推整数V公式：`C_w=29 S0 (2^256)²`，其I项为
`17[32S0(2^256)²+(61·8²+64·8)2^549]Q_d`；
其A/B/quadratic/cross项分别给1840–1843所列系数。
这独立核对了C_w、61/64/4416、17与W-positive nonsingularity。
V的column divisibility使K_*中的Q_d^-1分母合法；Bc nonsingular来自W>0，
不循环借integer target PD。

11/22的allowance分层仍必须保留：A/B各2^-220，H为2^-204+2^-220，
U为9·2^-512；alpha/beta支付projection cross/complement而非source误差，
epsilonD支付A²/B误差。W的DeltaX只付inverse upper中心运输。
没有把2^-204的full-operator kernel误差漏掉，也没有将它在congruence
变换后按raw单项误差重新扣一次。通过这些门，22的sign严格运输到19。

### 8.4 最终可消费条件与量词

**若主代理和source审查已经逐项确认fresh full-source误差及完整消费链，
本逆审允许消费Theorem B：**

\[
Q(f)\ge2^{-49162}\|f\|_2^2\quad
\text{对所有complex }f\in C_c^\infty((-17/16,17/16)).
\]

finite targets给M+K+U>=0，全smooth源最后用真实恒等式7与tail供给8，
所以tau来自全补空间，不把微小integer sign下界直接当Weil gap。
两个parity覆盖448维head；对complex空间无需额外的实数极化或pole矩零。
我的最后逆审没有留下congruence、norm8或该量词的额外条件；
剩余source误差门须由实际完整证据支付，不能仅凭fresh exit0推定。

自然闭型域延拓可以严格补足，不能只说L² smooth density。
置

\[
\mathcal D_{\log,L}=\{f\in L^2((-L,L)):
\int_{\mathbb R}\log(2+|t|)|F_f(t)|^2dt<\infty\}.
\]

Gamma加常数后的positive form与此weighted norm等价，bounded真实prime及
dual pole扰动保持closedness。Cc∞((-L,L))是这一form的core：
先用保L²缩放 `f_s(u)=s^-1/2 f(u/s)`（s↑1）将支持严格缩入窗内；
Fourier为s^(1/2)F(st)，dilation在log-weight L²上strong continuous，
可由compact-frequency函数稠密及log weight比较证明。再以小支撑smooth
mollifier卷积，Fourier multiplier趋1且绝对值<=1，dominated convergence
给log-weight范数收敛，支持仍严格在窗内。取对角序列便得到smooth core。
prime/pole型对L²连续，故Q在此core近似下收敛，下界延拓为

\[
Q(f)\ge2^{-49162}\|f\|_2^2\quad(f\in\mathcal D_{\log,17/16}).
\]

域外可用Q=+infinity的extended读法。延拓的是同Hilbert norm的closed
Weil型，不是声称零点侧级数在所有L²绝对收敛。
Theorem A、simple/ground multiplicity、别的窗或成长S/U/RH均不在此次消费。
