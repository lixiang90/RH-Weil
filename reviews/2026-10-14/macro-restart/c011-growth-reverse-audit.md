# C011 成长窗固定分拆：全源、紧修复与费用逆审

2026-10-14。仅写本文件，不改STATE/Goal/cadence/Git。新任务开始恢复了
AGENTS、README/STATE，实际check/show；再读当前原Goal/C010/D20261014J
及537实际全源分拆。起始HEAD为0c4f3a3，get_goal在本次先前恢复时为null。
新Goal/合同正由主代理写入，本文不把旧状态当新运行态。

以下§1–6为独立连续论证。主代理的新exact Fraction脚本/结果尚未落盘时，
本文不消费未见原件的数值声明；待§7补审后才判最终数值门。
初次粗心算写C≈4.18是加法错误，已在消息中更正；独立Decimal60诊断为
4.08534372730742969656…，诊断不作有向证书。

## 1. 实际完整对象与比较器

令I_L=(−L,L)，Lebesgue L² norm，源zero-extend到R。采用537实际规范：

    F_f(t)=∫ f(x)e^(−itx)dx,
    h_f(a)=∫ f(x+a) conjugate(f(x))dx,
    Γ(t)=Re ψ(1/4+it/2)−lnπ=2θ′(t),
    Q_W,L(f)=2Re[F_f(i/2) conjugate(F_f(−i/2))]
       + (1/(2π))∫ Γ(t)|F_f(t)|²dt
       − Σ_(p^k<e^(2L)) [2lnp/√(p^k)] Re h_f(ln(p^k)).

边界p^k=e^(2L)相关为0，写≤不会增加非零项。Λ(p^k)=lnp，不可用ln(p^k)
替代，也不可删高次幂。所有源f∈Cc∞(I_L;C)合法，无pole-moment约束；复源没有
预设ζ零点为实。Γ系数、Fourier的2π与原norm均不可另缩放。

J_a是zero-extension后的双向平移平均压缩，<f,J_af>=Re h_f(a)。对有限β、Ω：

    M_β,L=βI−Σ c_(p^k) J_ln(p^k), c_n=2Λ(n)/√n,
    K_β,Ω,L=actual dual pole + compressed Γ−β finite-frequency band,
    T_β,Ω,L(f)=(1/(2π))∫_(|t|>Ω)(Γ(t)−β)|F_f(t)|²dt,
    Q_W,L=M_β,L+K_β,Ω,L+T_β,Ω,L.

K为selfadjoint compact：pole核2cosh((x−y)/2)为rank≤2，有限band kernel在
有界I_L²连续，故Hilbert–Schmidt。它确实保留odd负pole；其紧性不表示正性。

若某独立tail估计给T≥τI+U，bounded selfadjoint U为compact，则
R=M_β,L+K_β,Ω,L+U是**下界供应器**，Q≥τI+R。本文证明R负，不能倒推Q负。
τ也必须保留：供应器τI+R的负性需把τ加入其标量β；只证明R负不自动排除
极大τ的另一路正供应。537实际τ=2^-49162远小于下述严格余量。

## 2. 连续carrier与真正全源反例

归一化箱源g_0=(2L)^(-1/2)1_I具有

    h_g0(a)=(1−|a|/(2L))_+,
    C_L=Σ_(p^k<e^(2L)) [2lnp/√(p^k)](1−ln(p^k)/(2L)).

箱源是有限logarithmic-form域源，但证明全Cc∞时无需只依赖它：取real非负
strict-support smooth g_j，||g_j||=1，g_j→g_0于L²。有限平移有界且
|h_gj(a)−h_g0(a)|≤2||g_j−g_0||，故成本C(g_j)=Σc_n h_gj(lnn)→C_L。
任何β<C_L的严格余量都在某个固定Cc∞源g中保留。此后冻结g，不再让支撑
或参数随高频carrier变化。

有限素数的phase simultaneous return给T_j→∞、exp(iT_j ln p)→1。
这只需有限维torus的Dirichlet回归，不需PNT、ζ零点位置、对数线性独立猜想：
用ε→0的pigeonhole取整数回归；若回归整数无界则抽子列，若有界重复则得到
一次exact return，其倍数给无界return。p^k的phase也趋1，因为k为本窗有限值。

令f_j(x)=exp(iT_j x)g(x)。每个f_j属于同一Cc∞全complex源类，||f_j||=1；
Riemann–Lebesgue对g conjugate(v)∈L¹给f_j weak→0于L²，而

    <f_j,M_β,L f_j>=β−Σc_n cos(T_j lnn)h_g(lnn)→β−C(g)<0.

任何fixed-L bounded compact selfadjoint V满足||Vf_j||→0，故包括K和任意
compact U在内，<f_j,(M_β,L+V)f_j>→β−C(g)<0。
没有finite matrix、N极限或普通高精度特征值参与此全源论证。

若β+τ<C_L，同样令β+τ替代β，则τI+M+V也有负方向。
若β+τ=C_L，本论证不声称严格负；coercivity需单独支付等号边界。

## 3. 无限负指数与修复量词

R=M+V是bounded selfadjoint。若它的negative spectral projection为finite rank，
则上述unit weak-zero f_j在该projection上的norm趋0；正谱部分贡献≥0，
负部分贡献≥−||R||·||P_-f_j||²→0，与严格负极限矛盾。因此negative spectral
projection具有无限维range，存在任意N维strict negative子空间。这是无限负
指数，不是只展示某一个Rayleigh负值。
Cc∞在L²稠密；任意有限strict negative Gram具有稳定余量，故可把其有限组
向量逐个逼近为Cc∞源，保持strict sign。因此无限指数确实适用于合法smooth源，
不是只落在未获准的抽象Hilbert向量上。

量词为：**每个固定L和β<C_L，对每个bounded L²-compact selfadjoint修复V，
M_β,L+V有无限负指数**。允许V rank/norm很大，也允许V随L改变；在每个固定L
先取其carrier序列，所以“不统一compact”不逃逸这个逐L结论。
若修复本身非compact，或改动β/actual prime账本，本文未排除。
最初直接投影carrier的方法仅付L²连续条件，不能把那个投影论证偷换成
L²不连续的D_log/Cc∞条件。539随后采用§8的finite-smooth-Gram组织，
已另付一般有限个连续线性smooth源条件；这一更宽结论不依赖直接投影carrier。
无限多条件、非线性条件或改动源对象仍不在此结论内。

## 4. β(L)必要发散，不用PNT

若M_β,L+V在完整L²源上非负，上一节必要条件为β≥C_L。
若要求≥mI，则必要β≥C_L+m。对n=p^k≤e^L，overlap≥1/2，因此

    C_L≥Σ_(p^k≤e^L) Λ(p^k)/√(p^k)
       ≥(ln2)Σ_(p≤e^L)1/p →∞.

最后发散可在这里自给，无需外部PNT：若Σ_p1/p有限，则
Σ_p−ln(1−1/p)≤2Σ_p1/p有限，有限Euler products有统一上界。
但∏_(p≤N)(1−1/p)^(-1)的非负展开包含所有n≤N的1/n，故≥H_N→∞，矛盾。
所以growth中正供应器若只用M+compactV，标量β(L)必须无界。
这只给必要发散；未证明最优增长率，也未给所有Weil正性方法的费用。

## 5. 固定Ω pointwise规则的确切天花板

外部逐点tail规则若以Γ(t)−β≥0对所有|t|≥Ω为前件，必要β≤inf_(t≥Ω)Γ(t)，
特别β≤Γ(Ω)。同规范Binet递推到z=5/4+it/2给独立upper：

    Γ(t)≤ln(t/(2π))+1/(15t)+25/(8t²), t>0.

推导：ψ(z−1)=ψ(z)−1/(z−1)；Binet两个real reciprocal项被负向减去，
drop它们作upper。|s²+z²|≥2 Re(z)|Im(z)|=5t/4，
∫_0∞s/(e^(2πs)−1)ds=1/24，故完整Binet积分绝对费≤1/(15t)。
Re lnz≤ln(t/2)+25/(8t²)。这明确使用actual2θ′，不是half Γ。

故固定Ω给有限β天花板，而§4迫使β(L)→∞；这种逐点tail+compact remainder
供应机制不能固定Ω一路成长。若L=3/2证C_L>4且Γ(256)<4，则同一局部窗口
已无β同时满足supplier非负的必要条件和Ω=256外部逐点非负前件。

若同时允许从**constant-envelope** tail抽取scalar τ，上面结论可精确加强：
先有Γ−β≥a>0及T≥a(I−B_Ω)，再由a(I−B_Ω)≥τI+U给供应。B_Ω在固定
支持窗上compact，任意weak-zero unit carrier给1−B期望→1、U期望→0，
所以必τ≤a。又a≤Γ(Ω)−β，因此effective scalar β+τ≤Γ(Ω)。
所以C_L>Γ(Ω)也排除这个constant-envelope类别的任意scalar提取及compact
修复；没有忽略τ或将原极小τ当成任意τ。直接消费Γ的非constant增长则不在此类。

严格限制：Γ−β在一小频带为负，并不证明支持窗上的compressed tail必负，
因为Fourier源不能任意精确限制于该频带。这里排除的是指定pointwise-premise
规则，不是所有band-sensitive tail论证。成长Ω、用非compact真正Γ尾、joint
signed算术估计，均未被这项费用边界排除。

## 6. 为什么不反驳whole Q或完成新宏观Goal

对于冻结smooth g的高频carrier，F_fj(t)=F_g(t−T_j)。actualΓ(t)随|t|约ln|t|，
Schwartz频尾使真正T_β,Ω(f_j)=lnT_j−β−ln(2π)+o(1)，故完整Q_W(f_j)
最终正向无界。被compact U丢失的是Γ高频的非compact供给；lower supplier
的负值与wholeQ的值方向完全不同。

本边界定位“将537 fixed split/rank-two Schur供应器原样搬到成长窗”的新费用，
没有证明RH、有全成长窗正性，或排除所有arithmetical signed/geometry机制。
它不复活C001增N、C008附件等待、等价Hilbert路线或暂停比例/无零区优化。
不能用本指定fixedsplit局部失败或数学组织改进单独完成新宏观Goal。

## 7. 新exact证据消费门：全原件及独立Fraction检查通过

初审先冻结了消费门：exp3边界、全部p^k账本、lnp与lnn区别、每项sqrt/log
向外方向、余项、C_L严格lower、β=7/2的negative余量，以及Ω=256 Γupper。
以下门现已付；上文4.085…仍仅ordinary诊断，不作为结论输入。

本节末审已完整只读新原件：

- `scripts/c011_growth_split_gate.py`，bytes SHA256
  `c12bd4e5128db49ffb490be87424212c74bd391d9d8653b1dbe88744fa52df82`；
- `reviews/2026-10-14/macro-restart/c011-growth-split-exact.json`，12个完整atom
  与每项log/sqrt/contribution两个有理endpoint，非作者或内部旧PASS。

producer对q≥1先二分缩到1≤x<2；atanh z=(x−1)/(x+1)为非负且z<1/3，
ln2另用z=1/3。128terms截断余项
2z^(2N+1)/[(2N+1)(1−z²)]合法upper，下界为正项截断；再按2^-256向外round。
sqrt来自integer floor sqrt(n·2^512)，精确平方核lower/upper；perfect square保持等号。
exp3的80次正Taylor和余项ratio≤3/82给合法geometric upper，向外grid仍严格在(20,21)。
枚举primes到20并逐幂校验恰好12项2,3,4,5,7,8,9,11,13,16,17,19，primepowers
4/8/9/16的Λ取lnp，而位移取k lnp。这些项全为正overlap，故乘lower/upper没有
符号翻转；即使lnp与overlap相关，这种区间独立化仍是安全包围。

还实际执行一个**只读、不同组织**的exact Fraction检查，exit0：不导入producer，
不二分log或调用其helpers；直接对原q用atanh recurrence，prime logs取1024terms、
Gamma q=128/3取2048terms。更窄的独立log包围完全落在producer的原log endpoints内。
逐行核sqrt端点平方、p^k/Λ/overlap及所有12项贡献的原有理式，重组总和，重组exp80
及完整几何余项，再核outward目标bounds与原source bytes SHA。这是证明输入的精确
复核；完整continuous推论仍依§1–6，未用有限矩阵代替它。

严格消费结果为

    C_(3/2) ≥ 473050485437491860147655801256974374701129526603514073240991709999379949509303 / 2^256 > 4,
    β+原τ−C_(3/2) < −1/2, β=7/2, τ=2^-49162,
    Γ(256) ≤ 434651784722252208139127029150636435549227542022310900118717201977119232799417 / 2^256 < 4.

Gamma producer使用π>3得到conservative ln(128/3)，再付1/(15·256)+25/(8·256²)，
而不是用Γ实际approx小数或half规范。独立2048term ln(128/3) upper加相同fees仍
严格≤上述recorded Γupper。Γupper与C lower之间的严格margin亦逐有理式重核。
所以β=7/2、原τ和任意compact修复的供应器在实际L=3/2有无限负指数；
该Ω=256 constant-envelope类别即使调整β并任取可由其抽出的τ，也无法做到
全源非负，因为effective β+τ须同时≥C_(3/2)>4及≤Γ(256)<4。

新Goal与C011合同已在主代理落盘后核读，成果基线为0c4f3a3/≤538；旧535/537/538
不可重复完成。本首轮strict growth-admission失败及必要费用审查已付，当前宏观
成长正性/Ξ身份瓶颈没有被解决，只是已否定“原fixed split直接扩窗”这一候选。
下一准入应先指定允许成长β/Ω或完整noncompact Γtail的新joint预算；普通增N、
再次fixed scalar反例或此边界的保存不够完成新Goal。本文无pending执行进程；
不改STATE/cadence/Git，不独立结算研究轮。

## 8. 539连续原推导的终消费与有限条件扩展

主代理落盘
`notes/539-growing-weil-prime-cost-and-constant-tail-boundary.md`后，已完整核读
§1–6；新AGENTS/README/瘦STATE/check/show、新Goal/宏观前沿/C011/D20261014K
也已重新恢复。当前root记录的新Goal active、C011首轮未结算；这是root现场
receipt观察，不以本代理此前工具隔离的null去覆盖。新成果基线仍是0c4f3a3/≤538。

539的actual Q分拆、全部12项与边界primepower、same-L compact K/pole、
β+τ而非β单独的必要条件、phase return顺序、weak0及所有compact修复量词、
Euler无PNT发散、constant-envelope scalar extraction和fixedΩ256范围均与本逆审一致。
没有将finite scalar gate单独当whole定理，未删除原Γ非compact高尾，未把负supplier
升级为Q负。539§4更精细的Euler log上界也正确：

    −ln(1−1/p) ≤ 1/p+1/[p(p−1)],
    Σ_(p≤x)1/[p(p−1)] ≤ Σ_(n≥2)1/[n(n−1)]=1。

因此其harmonic product反证自含，且只给必要发散、不填未付增长率。

**一般有限线性条件的新组织通过。** bounded B_L负指数无限先给任意N+m维
strict negative Hilbert子空间；选一组basis，finite Gram负定有严格最小余量。
用Cc∞(I_L)逐basis向量L²逼近，由B_L有界使所有Gram entries连续变化，足够
接近后仍strict negative；由负定性，这些smooth向量仍线性无关。有限个源条件
在这个有限维合法smooth空间上的限制是一张有限linear map，其kernel最多删m维。
故条件交集仍有至少N维strict negative smooth源空间。

此步不把L²不连续functional作用于某个L²极限，也不对原carrier做无界投影。
linear条件若定义在Cc∞/D_log且仅在其原拓扑连续，仍可先限制到这个已经构成的
有限smooth空间；事实上此有限维维数论证无需额外连续性。539只声明连续线性
源条件，属于已付范围。若条件按real-linear解释，额外同时施加ℓ(if)=0可取
complex-linear核（或用real维数计数），仍只删除有限维；不能将此延伸到非线性
条件、无限条件组，或任意未知的源空间变化。

所以539现在可消费的全源边界包括：任意fixed-L selfadjoint L²compact修复，
以及合法smooth源上的任意有限连续线性条件，仍不能修复β+τ<C_L的负指数。
这些条件是否在growth中需要越来越多并不改变逐fixed-L的有限条件结论；但本审查
没有给uniform carrier频率、derivative成本或新growth的正预算。

终scope为C011第一轮原split/constant-envelope成长准入失败与必要费用；
固定Ω256的whole bounded supplier不能延到L≥3/2，effective scalar及frequency
必须成长。允许变Ω、完整Γtail或新joint signed来源仍未排除，第二轮准入仍需
真正独立输入。此交付改变候选优先级，不消除宏观成长/Ξ/RH瓶颈，也不能完成
新Goal。所有本代理核验已终态、无pending进程，结算/保存/推送由root完成。
