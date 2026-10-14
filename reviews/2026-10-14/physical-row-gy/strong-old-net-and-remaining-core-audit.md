# GY physical row入口：最强旧后果、未付核心与下一门逆审

2026-10-14，/root/c017_macro_net。只编辑本稿；不改STATE、Goal、cadence或Git，
不自行结算轮数。本稿是来源与最强旧恢复，不是新独立算术输入或宏观完成。

## 1. 恢复的总体责任

已按AGENTS恢复README/STATE、check/show、当前Goal/frontier、549和D20261014V。
固定基线仍0c4f3a3eb609bb1d9564138fa4a35701f05605f2（全部≤538），
同G20261014。入场Goal LF SHA256为
8defa1fb1480596bb35ff892dc12b390e1cfe79c32ecdb9862edc4ac7b8d7690；
实际HEAD为5e65cc4637fc2d89edd83a85a4e492a5a6cd3608，root STATE为并行审查运行态。
最新数学549，原cadence1；C020一次结算stopped，GY只是唯一来源审查，没有C021。
结构脚本通过不认证数学，child运行态不代root的active宏观Goal。

549已付原du、全部cofactor单位flat-label及normalized Γ/Q费；actual全1合成有成长质量，
未付完整physical方向。GY即便付prime/divisor mixed相关，仍须扣最强旧跨表示后果，
保actualΓ=2θ′、全部primepowers、双pole及原complex/Dlog源；来源名不晋级定理标签。
本次明确补强旧账本：549所列O(log^6Y)不是本平方根physical band的最强旧后果，
下面的旧positive Gram/sieve及TypeI整理已蕴含O(1)。恢复此直接推论不计新轮。

## 2. 实际mixed对象与GY允许的修复

冻结h=1/T、sqrtY≤T≤2sqrtY、|tau|≤T、n∈(Y,2Y]，

    s_n=n^(−1/2−i tau)e^(−n/Y), E_n=1_[logn−h,logn],
    p(f)=Σ_(Y<n≤2Y) f(n)s_nE_n,
    c(u)=∫_Y^(2Y) v^(−1/2−i tau)e^(−v/Y)E_v(u)dv.

原164 V=1逐项给

    I_U(n)=Σ_(d|n,d≤U)mu(d)log(n/d), II_U=Lambda−I_U,
    I_U(n)=Lambda_U(n)+log(n/U)a_U(n),
    Lambda_U(n)=Σ_(d|n,d≤U)mu(d)log(U/d),
    a_U(n)=Σ_(d|n,d≤U)mu(d).                         (1)

a_U不能丢，也不能由只有big-O的Lambda_R相关公式求导免费获得。
完整mixed核是所有|j|≤CY/T的

    Σ_n Lambda(n) I_U(n+j) w_j(n),
    w_j(n)=1_(Y<n,n+j≤2Y)[n(n+j)]^(−1/2)e^(−(2n+j)/Y)
             exp[−i tau log(n/(n+j))]
             [h−|log(n/(n+j))|]_+ .                 (2)

原BV/prefix、正负j、两端cutoff、complex phase和properpowers保持。每w_j的
sup/总BV是O(h/Y)，故若全j、全prefix误差统一为E(Y,U)，总费用为O(E/T²)。

一级[GY math/0111212v1](https://arxiv.org/html/math/0111212v1)§4.1
的mixed AP机制有native W_U(j)，不应因Thm1.1/1.3的公开R/j声明miss而否定
直接AP求和或允许大log-power的逃逸。对U_B=T/log^B(e+T)，选择固定B支付
经典Bombieri--Vinogradov level的log损失，可能合法修复全j与cutoff范围。
pure CRT的U_B²log²Y/T²在B>1时趋零；mixed需要另支付原BVlevel与a_U槽。
冻结B=2不自动满足任意所需BVlog预算，B的改变也不能无声删TypeI/II companion。
本审不把native W替成错域singularseries，也不补GY未提供的Lambda--Lambda非零shift槽。
direct AP若成立，是经典CRT/BV在新表示的准入；是否计数学轮须另有真正新core/net后果。

## 3. 更强旧aggregate：TypeI、连续项和mixed已近合

旧085已消费经典Korobov--Vinogradov/Walfisz型Mertens估计，旧159保m0、m1，

    m0(U)=Σ_(d≤U)mu(d)/d,
    m1(U)=−Σ_(d≤U)mu(d)logd/d.

这些旧输入与原zeta在s=1的simplepole规范给
m0=o(log^(−A)U)、m1−1=o(log^(−A)U)，每固定A。可由partial summation核：
mu加权尾绝对由Mertens bound控制，Σmu/d=0、−Σmu logd/d=1为1/zeta在1的值和导数。
这不是RH强度平方根Mertens输入，也没有恢复暂停的无零区域优化。

对任何固定u，原window截到(Y,2Y]后，每个d≤U的AP Euler求和有

    |Σ_(a<kd≤b) f(kd)−d^(−1)∫_a^b f(v)dv|≤C||f||_BV,
    f(v)=log(v/d)v^(−1/2−i tau)e^(−v/Y),
    ||f||_BV≤C logY/sqrtY.                          (3)

费用含两个端点；tau·h≤1，因而phase变化也已包含，不删modulation。
按|mu(d)|求和得到pointwise误差CUlogY/sqrtY。连续密度精确是
m0(U)logv+m1(U)，不是未经证明的常数1。对冻结U=floor(T/log²(e+T))，
logU与logY可比，因此旧Mertens输入把此密度与1的差压至任意负log幂。
在sqrtY≤T≤2sqrtY上，continuous amplitude∫window v^(−1/2)dv=O(1)，
共同support的du长度O(1)，于是

    ||p(I_U)−c||=O(1/logY).                         (4)

这是真实aggregate TypeI的最强旧推论，不需全individual-j GY定理。
对固定B>2有对应更小grid费；不能把(4)扩大到全部低T或任意变B无共同误差。

下面附节从旧167的Haar正Gram直接恢复r=1上界筛，给

    ||p(Lambda)||²=O(1), ||c||²=O(1).               (5)

全部primepowers与complex phases保留。即便不消费此筛推论，旧Chebyshev和
Lambda(n)≤log(2Y)亦已给O(logY)，比549的O(log^6Y)强；(5)才是本band应扣的账本。

actual prime--continuum mixed也已有普通PNT消费。其精确n权为

    A(n)=∫_(|z|≤h) exp[(1/2+i tau)z]
                   exp[−n(1+e^z)/Y](h−|z|)
                   1_(Y<ne^z≤2Y) dz.

n的原modulation在两source配对中精确消去；z相位仍保。A有sup/总BV≤Ch²，
包含moving endpoints。PNT的uniform prefix误差o(Y)经Stieltjes/Abel求和给

    <p(Lambda),c>−||c||²=o(Yh²)=o(1).              (6)

由(4),(5)，完整prime/TypeI mixed与pure TypeI也已经满足

    <p(Lambda),p(I_U)>−||c||²=o(1),
    ||p(I_U)||²−||c||²=o(1).                        (7)

这些不是每个shift或任意BV输入的GY声明；它们正是冻结原physical aggregate消费槽。
即便新direct-AP证明逐shift更强，不能用其paper或更细标签重复登记(7)为新whole/core付款。

特别地，same-source fullII与actual prime--continuum能量已有

    ||p(II_U)||²=O(1),
    ||p(Lambda)−c||²=||p(II_U)||²+o(1)=O(1).        (8)

在本有限平方根height band除beta≈logT，本来就是o(1)。这纠正最强旧比较，
不滚动基线，不创造新定理来源或新轮数。低height/body across cofinal Abel参数仍未付。

## 4. paid mixed仍保哪个真正未知槽

不论U_B怎样合法变化，原TypeI/II gauge仍精确守恒Lambda。即使(7)全付，

    ||p(Lambda)−c||²
      =||p(Lambda)||²−2Re<p(Lambda),c>+||c||²
      =||p(Lambda)||²−||c||²+o(1).                  (9)

在Gram中，Lambda--Lambda近差块的系数仍为+1。GY未给它，mixed或proxy正Gram
不能替它给upper。一般positiveGram/knownmixed信息只给未知norm的lower，
不限制orthogonal剩余；这只是逻辑消费门，不是actualLambda增长或Q负反例。
允许更多cutoff/变尺度/全prefix相关不自动改变(9)，除非新证据量化覆盖或该剩余。

上界筛虽给本band(8)，在T低于sqrtY的growing核心仅给O(Y/T²)量级；
它不支付完整height-sum的signed prime/continuum偏差。更强旧016/028的完整profile/
负迹和543的cofinal Ce^S仍是whole比较，068/548的critical条件仍RH强度。
新mixed槽不能把这些未知完整责任换成另一个“已知独立来源”名称。

准确停止：停止GY作为当前physical aggregate mixed付款主攻，来源入口0轮；
不以增加B/缩R/多paper继续已付(7)。保individual-j原AP新范围（若真有独立用途）、
Lambda--Lambda signed近差、joint Γ/prime/pole、不同source/head、独立几何等逃逸。
不排GY原定理、不排大B direct修复，也不宣称全部prime相关或实际Weil失败。

## 5. 不重复薄域的下一具体core门

可考虑不同且有具体arith输入的全cell占用来源，但必须改正投影对象。
547原P是dx/x格均值；其raw-dx像的mean functional不是普通flatmean。
新head应明确用

    H_N=L²((1,N),dx/x), a_N=N^(−1/4)sqrtx,
    Pi_N^a=orthogonal projection onto span{a_N 1_(j,j+1):1≤j<N}.

经unitary F(x)↦f(x)=F(x)/sqrtx到L²(dx)，Pi_N^a就是unit-length cells的flat
均值投影。R_a=1−Pi_N^a为每cell raw Fourier k≠0。它与547旧R不同，
不继承旧canonical Gamma100。a_N精确在head，故原dual-pole压到R_a时为零。
rankN−1、全部cell/fullsource有限codim；它不是546的稀薄comb或固定profiletensor。

原primeforward在rawdx为U_q f(x)=sqrtq f(qx)，zeroextension，contraction，
保持flatcellmean0。令P_(q|k)取每cell Fourier频率q整除的块，D_q=P_(q|k)U_q。
其range确为q|k，Young及全部primepowers的Σ_(q|k)Lambda(q)=log|k|给

    2Σ_(q<N) Lambda(q)/sqrtq Re<D_q f,f>
      ≤eta Σ_(j,k≠0)log|k||f_(j,k)|²
          +eta^(−1)Σ_(q<N)Lambda(q)/q ||f||².       (10)

尾sum不需外部PNT：log(N!)=Σ_(q≤N)Lambda(q)floor(N/q)，
floor(N/q)≥N/(2q)，故Σ_(q<N)Lambda(q)/q≤2logN。
这是全cell不同频率方向的actual占用输入；
它不是完整U_q或Gamma-relative已付。nondivisible carry仍在：单child mode k的
q=2、output mode2k+1的系数绝对值sqrt2/pi不随k趋零。因此不能free/small-L²删carry；
此例不排Gamma-relative或joint修复，且不作为Goal第三门边界。

建议唯一预算一候选的实际门：在这个changed合法head，核原Dlog/domain和
cell-log-frequency到actualGamma的统一费用，并支付**全部**nondiv carry，最终证明
或合法否定allcomplex R_a上的

    B_N(f)≤eta J_Gamma(f)+C log²N ||f||²,
    fixed eta<1, absolute C, all integer N≥4.        (11)

B_N是全forward及其自伴quadratic prime块，不是D_q部分；Gamma规范保持2theta'。
新输入为(10)的actual整除占用，(11)仍candidate，不能改名为已知source。
若domain、fullcarry和(11)全付，finitecodim与旧028可消费成

    n_minus(Q_(logN/2))≤N+C logN exp(C' log²N),       (12)

quasipolynomial预算严格小于旧543的exp(c sqrtN)量级，触及whole危险core。
这是明确的if-paid净后果，不是RH等价目标改名或特殊源正性。全部head、Γ/pp/pole、
closedform误差及旧强界仍须原件核；本稿不证明(11)/(12)，不自行创建C021或completeGoal。
这个changed全cell方向足以区别546的薄comb与549 flatlabel成功，但只有允许relative
收费的全carry原门或合法联合反例才值得结算，不能用(10)/singleq例就结束宏观研究。

已独立只读核root550原稿，读时SHA256为
9c7615fc8c923b77b3f6d5cb3a121f738c32897bf4e2651d3843152345bb6aa6。
其§3–§5的phase消去、旧sieve O1、Gamma型tail与normalized完整Q接近费符合本稿范围；
没有补Lambda--Lambda或把singleband推广fullAbel。C021草稿采用r=a_Nphi，
norm=N^(−1/2)||phi||²_dx；本稿unitary f=r/sqrtx等于N^(−1/4)phi，
故(10)与其带N^(−1/2)的版本完全相同，不能遗漏这个固定norm因子。
ready依据是changed合法head、真实occupation输入、待核G1/G2和(12)的conditional净门；
不是现已支付actual全carry、Γrelative或当前core。root最终版本仍须消费final原hash。

## 附：旧167 Haar正Gram直接蕴含本band上界筛

此附节仅恢复最强旧推论。对任意real sieve weights lambda_d，d≤z，
旧167正Haar/gcd Gram与gcd(d,e)=Σ_(r|d,e)phi(r)精确给

    S_lambda=Σ_(d,e≤z)lambda_d lambda_e/[d,e]
      =Σ_(r≤z)phi(r)(Σ_(r|d,d≤z)lambda_d/d)².       (13)

置G(z)=Σ_(r≤z)mu(r)²/phi(r)，y_r=mu(r)/(phi(r)G(z))，

    lambda_d=d Σ_(d|r,r≤z)mu(r/d)y_r.

有限Möbius反演给Σ_(r|d)lambda_d/d=y_r，lambda_1=1及S_lambda=1/G。
对squarefree d，

    lambda_d=mu(d)d/phi(d) *G_d/G,
    G_d=Σ_(s≤z/d,(s,d)=1)mu(s)²/phi(s).

G含r=ds的子和G_d/phi(d)，所以|lambda_d|≤d；非squarefree d为零。
Σ|lambda_d|≤z²。由squarefree harmonic sum及phi(r)≤r，G(z)≥c logz。

每个prime p>z满足Σ_(d|p,d≤z)lambda_d=1。长度H的任意平移区间J中

    #{p∈J:p>z}≤Σ_(n∈J)(Σ_(d|n,d≤z)lambda_d)²
       =H/G+O((Σ|lambda_d|)²)≤H/G+Cz⁴.

选择z=floor(H^(1/8))；p≤z的至多z项也被O(z⁴)吸收，
得π(J)≤C H/logH，uniform所有平移。
本band可把任何被截window包含于一个H≈sqrtY、x≈Y的完整区间，所有prime>z。
对proper power p^k,k≥2，每k的rootinterval长度
≤H/(k x^(1−1/k))，在H≈sqrtY时O(1)；k≤log_2(2Y)，乘logp后总费O(log²Y)。
因此actualψ短窗质量≤C H+C log²Y≤C'H，原phase绝对值为1，

    |p(Lambda)(u)|≤Y^(−1/2)C'H=O(1).

support du长度O(1)，故(5)。同source c直接同量级。没有外源BT名字、新零点信息、
比例/零区优化或finite矩阵认证，也没有把positive筛代理替成actualLambda相消定理。
