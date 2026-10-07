# Gaussian root-weight probe：独立全文审查

2026-10-07。审查人：`twisted_research`。全文独读新root-weight研究稿，
重推Poisson、unit isolation、两种hop、good-prime valuations及二维
additive large sieve，并读原固定source的marked/raw合同。只新建本审查；
未改被审稿、math、旧正文、Goal或Git。

结论：**限定 PASS**。真实Schwartz probe精确读出同一target的平滑
Möbius family；共同符号、固定数量disjoint once-prime slots的raw矩
确有(U+T_col²)(UT_col)^epsilon界。任意eta的completed reflection、
critical raw范围及新sigma都未付；本PASS不将它们注册为已证。

## 1. 最终版本及实际输入

SHA按UTF-8解码、CRLF→LF、lone CR→LF，不trim或删除末尾换行。

| 文件 | canonical LF SHA256 | canonical / raw bytes |
|---|---|---|
| [被审最终稿](hybrid-gaussian-root-weight-probe-research.md) | `4a6b33cae1944bc904216c202a62f04d48d2f47b0ff5a852f13a3af5a063bc3d` | 30381 / 30381 |
| [457冻结正文](../../notes/457-number-field-choice-and-relative-amplification.md) | `75079970955602644a9290709f66e2be331ad6116d2a637ed8fc97fb0dde5791` | 15254 / 15254 |
| [固定OpenAI source](E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex) | `42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3` | 766316 / 782993 |

固定source的commit为adc7f1241b42e322a6451854ab7e4b4c146bf78a。
我独读9191–9276、12335–12386，核其共同nu/epsilon_chi、row-independent
prime coefficients和每个c>0的raw范围。外部文献浏览核对
[DDHL v5](https://arxiv.org/html/2306.11875v5)的(3.9)–(3.11)、
(4.24)–(4.28)、(4.35)–(4.39)。未以过时v3或未取得的Suzuki原扫描
代替这些实际输入；未重新认证DDHL全文。

最终修订补明H=X的有限截断、Gamma/angular依赖、odd-part product、
两sign hop、epsilon量词、S含lambda、slots取odd primary、profiles
支撑[1,2]及D/P_i≥1。末次P3只涉及状态与后两个前件，已从磁盘核对。

## 2. Gauss normalization、theta来源和真正的Poisson

新稿使用B(z,xi)=Re(z xi)，而非Re(z bar xi)。在这个明确的bilinear
pairing下，Z[i]仍自对偶，covolume为1；不用添一个隐藏conjugate。
DDHL additive character是exp(4pi i Re z)，实际Poisson采用exp(2pi i Re z)。
因n odd，2在O/n中可逆，故G_*,j=chi_n(2)^j G_j。这个phase已准确
留在c_j中，不能免费删掉。primitive finite Gauss identity在非unit
numerator上为零，和chi_n的natural zero extension一致。

已付squarefree signal gamma_1²=mu alpha可同时用于degree-one及inert
primes；后者只需gamma_1为实单位，不需错误的统一正号。CRT cross
factor平方为1。新probe直接使用这个有限Gauss weight，不依赖未知
exponent-one theta core。

§2的square coefficient仅作来源说明：N(m²)^(1/8)=q_m^(1/4)
抵消其quarter weight。已知fixed sector/cusp关系不是随意可除的
非零psi_beta(1)假设，更不是一个新root-index theta functional equation。
probe本身由有限gamma明确规定，剥去Bessel、改读root及插入eta
是新operator；不能沿用完整index的eta(n²)而声称同一eta。

我独立分a+nO并作Poisson：f(z)=F(beta z/sqrtH)的Fourier transform
为H Fhat(sqrtH xi/beta)，lattice nO的dual为(1/n)O。因此(3.2)准确为
H/q_n sum_k G_*,1(k,n) Fhat(sqrtH k/(beta n))。
取beta=bar alpha(n)，beta n=|n|；乘外系数后
chi_n(2)^(-1) gamma_1 bar alpha·chi_n(2) gamma_1=mu，
并得到(3.3)的H/q_n。这里没有少sqrtq或错误右伴随。

外n有限、内h Schwartz绝对收敛，逐项合法。任意eta(n)一直是外系数，
没有变成eta²；加入chi_n(u)^epsilon也逐真实u保留，非互素时自动零。
bad primes和全定义mask没有被除掉。因此读出的是带原固定local
exclusions的同一eta family，不是未经说明的完整Euler product。

## 3. Rotating tube、双hop和长度的严格界限

I=[1/sqrt2,1]。若k不为1，Im k非零时tk到I距离≥1/sqrt2；
实k≥2时≥sqrt2−1，实k≤0时≥1/sqrt2。这覆盖全部Gaussian
lattice点，不是有限sample猜测。Fhat在I邻域为1、支撑在半径1/4
tube，精确留下k=1，包括q_n=X和2X两个端点。F为固定Schwartz，
通常复值/nonradial；新稿没有把它冒认为原positive radial test。
W=tV给(4.3)的精确Möbius重写，其本身没有saving。

对双hop，j=1/3、sigma_j=1/−1，gamma_3=chi_n(−1) bar gamma_1，
于是gamma_j²=mu alpha^sigma_j。c_j=chi_n(2)^(-j)gamma_j alpha^(-sigma_j)
再次令Poisson系数恰为mu；j≡−epsilon mod4使unit dual保留
mu eta(n) chi_n(u)^epsilon。normalized inverse的q_n^(-1/2)只需
dyadic profile和提出X^(-1/2)，不会改变target。

两sign都满足
chi_n(2)^(-j)chi_n(h)^j chi_n(u)^(-j)=chi_n(2h³u)^(-j)，
所以actual numerator线性含u。固定正hop对正incoming row原来的
2(uh)³则仍在旧公式中保留；没有偷换两个不同物理设计。
all-modulus G_3(nu,c)=chi_c(−1) overline{G_1(nu,c)}，固定primary
mod4 sectors后补号已知；系数conjugation及ell翻转可给untwisted
conjugate completion，norm conductor同为Nnu。不能借此添任意eta FE。

angular expansion的n参数是ell+sigma_j。normalized DDHL completion
各Gamma含|ell|/2，并有alpha(nu)^(-ell) phase；新稿修订已保留。
Nnu/X≈q_h³q_u/X只能作为识别出的untwisted conductor/reference-length
账本。一般target、ramified cusp、pole/height和profile的联合完成仍缺，
不得把H³/X或H³U/X直接称为本probe已付的反射估计。
Schwartz截断已限定H=X≥2；任意指定负幂由固定足够高seminorm付款。
没有对超多项式H作无条件统一tail声明。

## 4. Full valuation、square-map候选和odd-part factorization

我按h=h0+pi y逐lift重推(6.1)：unit numerator的lift sum为0；
v=1给q次residue Gauss；v≥2给完整乘法character sum。principal
exponent仍只在units上取1，保留nonunit零，故v=1为−q、v≥2为q(q−1)。
四个effective exponents全覆盖，不把Ramanujan分支漏掉。

对任意L≥1、k=v_pi(nu)，nonprincipal local exponent只在L=k+1
非零，值q^k chi(kappa)^(-e)G_e；principal exponent还在L≤k
给phi(pi^L)，在L=k+1给−q^k。e=L mod4准确对应DDHL quartic
symbol模pi^L；双hop时改为jL mod4。powerful h/u全部可代入，
不需要numerator squarefree。表中k=0、3、6、9每个分支相容。

natural square-map在chi(−1)=−1时由y/−y配对消失；否则square
pushforward给两个order-eight rows。j=1乘quartic incoming后为
−3、−7两指数，仍非quadratic。这只排除所指定operator，未作
所有Gaussian设计的绝对no-go。

对h非零squarefree、u=1，good pi|h只能产生L=4的−q³；normalize
除q²及乘q^(-4s)恰给−q^(1−4s)。其它good primes只剩L=1。
pi⁴的CRT cross phase为1、primary mod4 sector也不变，故(6.6)
可逐项分解。product只取pi不整除lambda；ramified h保留为numerator/
cusp数据，lambda不能凭空增加L=4 modulus列。h=0没有进入Gauss DS。

formal eta(c)因multiplicativity给eta(pi)^4；若eta(pi)=0，local
factor为1，D_sf的系数也维持定义mask。这个系数恒等式在绝对收敛
half-plane合法；zeta/formal L completion添第四幂列不改变surviving
squarefree chi_c(h)的odd character。不推出target FE、短dual或saving。

## 5. 原始矩：共同符号、primitive conductor和零掩码

固定source9225–9248给M/Q同一个nu和epsilon_chi，prime coefficients
与支持不依赖当前u。新定理准确保持这些前件，k0固定、prime sets
互不相交、所有moduli odd primary。w/w_i支撑[1,2]和D/P_i≥1使
每expanded m=n product p_i满足Nm≤2^(k0+1)D product P_i。

local exponent仅epsilon或2epsilon：重叠n=p保留primitive quadratic，
其余为primitive quartic。finite conductor是rad(m)，不是m。不同m
产生不同conductor或不同local character；CRT上这些区别不能抵消。
同m的多种decompositions用fixed-k divisor multiplicity和Cauchy付
T_col^epsilon。Gaussian lattice count给各dyadic coefficient-square
sum=O(1)，无需PNT；logs以product A_i²明付。eta只需|eta|≤1和其
真实multiplicativity/zero extension，没有隐藏导子损失。

相反符号时n=p会成为principal+1_(u,p)=1 mask，随p产生near-duplicate
functions。不能用primitive同conductor正交消除这些coherent项。
新稿已正确排除该版本；这不是原共同符号定理的反例。

同一conductor先将实际A_chi合进Gauss coefficients；unit group的
character orthogonality给phi(c)/Nc sum|A_chi|²≤sum|A_chi|²。
primitive Gauss identity在nonunit numerator上为0，故完整自然mask
一直存在。conductor1只有一个常数frequency，亦无重复问题。

## 6. 二维additive LS的实际证明和最终范围

reduced a/c给不同torus frequencies；任意差减lattice点后分子是非零
Gaussian整数，故距离≥1/(|c c'|)≥1/T_col。odd c下trace-2改为2a/c
仍reduced。unit associates由unique primary generator处理。

新稿实际用positive Gaussian而非声称它bandlimited。Poisson给
K_U(delta)=pi U sum_v exp(−pi²U|v−delta|²)。所有lifted frequency
points仍以delta0≥1/T_col分离，半径delta0/3的disjoint disks给
ball count≤C(1+r/delta0)²。径向积分准确得到
sum_points exp(−pi²U r²)≤C(1+1/(U delta0²))；中间一次幂项
由x≤1+x²吸收。Schur row sum因此≤C(U+T_col²)，uniform于row radius。
Gaussian在目标disk上≥e^(-1)，故它是合法positive majorant。
这与非负bandlimited sinc²/packing的另一直接证明同尺度；不需
untwisted DDHL或quartic large-sieve conjecture。

将这个LS和前两节coefficient energy结合，(7.2)完整成立，包括
once-slot/inverse overlap、全部zero masks、empty slots及全Gaussian
rows（不先限制row为prime或primary）。fixed reciprocal sectors若另用
chi_u(n)方向，只需固定有限2-part处理；直接方向并不依赖该重写。

严格结果保留任意小幂。当U≥T_col²时得到O_epsilon(U^(1+epsilon))，
并非无epsilon的finite-constant O(U)。无slots只支付U≥D²，而原
source12343–12360需要每个c>0的H≥D^(1+c)合同。0<c<1的中间
范围仍开。order-four amplification仅作条件账本时，其envelope为
max(1,1/4+3r/2)，不是理想max(1,1/4+3r/4)，不能导出新sigma。

有限floating sanity checks不能认证全Poisson或LS；本审查以解析
公式核验为依据，不把这些未独立重跑的sample注册为新的精确证据。
没有发现最终稿在所声明范围内的实质数学缺口。未付范围是一般eta的
completed FE/共同profiles及critical raw cancellation，不是被本PASS
证明不存在；新的双hop保留给后续实际反射研究。
