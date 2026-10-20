# 570. 实际联合Sonin误差：双素数mixed的log²与原范数费用

2026-10-20，C033。同G20261014／0c4f≤538冻结基线，执行560保存、用户本轮明确要求的
actual S={∞,2,3} signed准入。三个原稿、来源核查、逆审与同步统一归一完整研究迭代。
不续569的Γ/line来源链，不重跑560已停止的norm1高频ratio门。

**本轮结论：在固定双patch、每patch双极点矩为零的实际源上，完整联合误差有两种符号，
主项为±C23 log²(1/η)。全部returns没有被截断；它们的整体贡献是O(1)。
固定窗上的无限正负指数排除了这个真实联合正来源的无费比较和有限秩补丁，
但不排非有限秩紧修复、不推出Weil型负值，也不支付cofinal成长容量。**

## 1. 同一个实际对象与误差的角色

物理H=L²((0,∞),dx)，U_t f(x)=e^(−t/2)f(e^(−t)x)，F(x,y)=2cos(2πxy)，
L=1_(0,1)、H_+=I−L。实位Sonin空间M=kerL∩kerLF，P为其正交投影。
固定

\[
 B=(I-2^{-1/2}U_{\log2})(I-3^{-1/2}U_{\log3}),\quad
 G=(PB^*BP)|_M,\quad \Pi_{23}=BPG^{-1}PB^*.                \tag{1}
\]

B有界可逆但非酉。由FBF=B*及B与B*交换，F23=BFB⁻¹=B(B*)⁻¹F仍为自伴酉involution。
B及其逆保持high，故Sonin(F23)=BM；(1)与双cutoff对象是同一物理正交投影。
没有用B P B*或single-prime迹相加替代它，也没有语义更换需要撤回560。

对log变量复源r，A_r=∫r(t)U_tdt，T23(r)=Tr(A_rΠ23A_r*)≥0。
先对任意r定义560的完整overlap型

\[
 \mathcal E_{23}(r,s)=\frac1{2\pi}\int\epsilon_{23}(\xi)
             \widehat r(\xi)\overline{\widehat s(\xi)}d\xi,
 \qquad E_{23}(r)=\mathcal E_{23}(r,r).                    \tag{2}
\]

这里ε23=2πρ23−Γ+2Σ_(p=2,3)logp Σ_(k≥1)p^(−k/2)cos(kξlogp)∈C0，
Γ(ξ)=Reψ(1/4+iξ/2)−logπ，完整contact保留。
所以一般中间源E=T23−qΓ+所含prime-power型，不能无条件写T23−完整Q。
下面最终源上双pole及全部pp精确为零，才有E23=T23−Q_W。
φ、固定β等中间片不要求pole-zero，始终按(2)分解，避免丢失pole角色。

## 2. 固定源门：真正的双矩零和全部素数幂零

记a=log2、b=log3、d=b−a，固定0<δ<min(d,a−d)/2。
φ≥0、φ∈Cc∞(−1,1)、∫φ=1，φη(u)=η⁻¹φ(u/η)。
固定β1、β2∈Cc∞(−δ,δ)，支持有序分离且避开0，两列M±(βj)不成比例，
M±(r)=∫e^(±u/2)r(u)du。取唯一有界系数使

\[
 h_\eta=\phi_\eta-A_\eta\beta_1-B_\eta\beta_2,
 \quad M_\pm(h_\eta)=0,\qquad
 g_\eta^\pm(u)=\frac{h_\eta(u+d/2)\pm h_\eta(u-d/2)}{\sqrt2}. \tag{3}
\]

矩阵反演精确给(Aη,Bη)→M⁻¹(1,1)，一般误差Oη，偶φ时Oη²。
每个η的源仍在原Cc∞及zero-extension Dlog，L1质量一致有界。
两patch不交，总支持直径d+2δ<a；故对所有p、k≥1，相关R_g(±klogp)=0。
平移只给M±乘实指数，所以每个最终patch及其组合的两pole矩都精确为零。
这保留完整Γ、所有proper powers和双pole定义；只在这些输入上相应项取值零。

## 3. 实际裸迹与所有returns如何同时付清

F23在operator norm中展开，先合并重复尺度再读分布核：

\[
 F_{23}(x,y)=\sum_r c_r\cos(2\pi rxy),\quad
 \begin{array}{c|c}
 r&c_r\\\hline
 2^j3^k,\ j,k\ge0&2/3\\
 3^k/2,\ k\ge0&-2/3\\
 2^j/3,\ j\ge0&-1/3\\
 1/6&1/3
 \end{array}.                                           \tag{4}
\]

核中没有额外r⁻¹/²；它已经与unitary dilation的核缩放抵消。
K=LF23L为紧自伴，Schatten插值给K∈S_p对所有p>2，尤其K∈S3。
η_op=(B*)⁻¹及其逆保持low，F23η_op=η_opF；Fourier紧支唯一性给κ=||K||<1。
更明确的fixed对象费用是

\[
 1-\kappa^2\ge(m/M_B)^2(1-\|LFL\|^2)>0,
 \quad m=\prod_{p=2,3}(1-p^{-1/2}),\quad M_B=\prod_{p=2,3}(1+p^{-1/2}). \tag{5}
\]

不把这个ambient Sonin cutoff gap当成长源窗或cofinal素数集的统一gap。
535的实际源平滑引理给
||A_r L F_λ L||1≤C_r(1+logλ)/√λ；双几何列的这些费用绝对可和。
于是每个fixed smooth r的第一裸因子在S1收敛、第二因子在operator norm收敛，
允许取ordinary trace的共同极限，不能先对ambient裸核逐项取迹。

令h(K)=K(I−K²)⁻¹，真实overlap O=Π23+L+F23LF23−I满足
O=Φ(h(K))，Φ(T)=LTLF23H_++F23LTLF23H_+F23。
在合法夹源迹中精确分离

\[
 h(K)=K+C,\quad C=K^3(I-K^2)^{-1}\in S_1,\qquad
 E_{23}(r)=\operatorname{Tr}(A_r\Phi(K)A_r^*)
            +\operatorname{Tr}(A_rD_{\rm ret}A_r^*),
 \quad\|D_{\rm ret}\|_1\le\frac{2\|K\|_{S_3}^3}{1-\kappa^2}. \tag{6}
\]

该式先对实r由实际block/源迹成立；实际ε23密度实偶，故可把复源写为实/虚两部并极化。
所有returns同时属于(6)后项；对L1=O1的源，其值≤||r||1²||Dret||1=O1。
返回源核Tr(Dret U_t)连续有界。没有有限return截断，也不把C0本身当符号证明。

## 4. 稠密比例的费用：需要独立算术，不是假设统一gap

裸项的正时间源核由真实矩形给

\[
 e_{\rm bare}(t)=\sum_{r,s}c_rc_s I_{r,s}(t),\quad
 I_{r,s}(t)=e^{t/2}\int_{e^{-t}}^1\int_0^1
        \cos(2\pi rxz)\cos(2\pi s e^t xz)\,dz\,dx.        \tag{7}
\]

偶延拓后Ebare(r)=∫R_r(t)e_bare(t)dt。Si两个端点的常数尾相消给
|I|≤C[(1+|r−e^t s|²)⁻¹+(1+|r+e^t s|²)⁻¹]，在固定t∈[0,t0]统一使用；
积分端点x≥e^(−t0)离零，该界不含1/t费用。
这是真实pair核的二阶相位费；对t→0的self另保积分区间收缩。

新增消费的独立外部实例为[Bugeaud–Mignotte–Siksek Annals163(2006) Thm9.4 pp988–989](https://annals.math.princeton.edu/wp-content/uploads/annals-v163-n3-p05.pdf)，
来自Matveev的既有对数线性型定理。历史507核过2,5，本轮实际重开原刊并核2,3实例：
K=Q、D=1、α1=2、α2=3、A1=a、A2=b，B≥max(3,|m|,|n|)。
定理先给乘积|2^m3^n−1|≥cB^(−M0)，在有界log范围用均值定理才转换为

\[
 |m a+n b|\ge c'(1+|m|+|n|)^{-M_0}\quad((m,n)\ne(0,0)). \tag{8}
\]

非零性由唯一分解给出，M0可以极大但固定，不用未知ζ零点位置。
它是已知深算术输入，不是一般g-integer log群自动具有的分析正则性。

尺度写r=2^J3^K/6，以H=max(J+K,J'+K')计height，每层pair数O((1+H)³)。
在可比范围r,s≥ce^(aH)。对t=d+Oη，非exact项由(8)在中心给c(1+H)^(−M0)的log gap。
选择固定ε>0、εM0<1，先切H≤η^(−ε)，则充分小η保留一半gap，全低height费用被
Σ_H (1+H)^(3+2M0)e^(−2aH)<∞控制。
高height不再用gap，而对宽η、L∞=O(η⁻¹)、L1=O1的平滑核用
∫|ψη I|≤C/(ηs)，全尾≤Cη⁻¹Σ_(H>η^(−ε))(1+H)³e^(−aH)=o1。
不可比pair直接绝对可和。

因此所有nonexact项的窄源**平滑平均**共同为O1，不是穿孔邻域逐点O1。
比例集合稠密，其他共振尖峰也稠密；不能省略平均顺序或照搬single-prime gap。
同一无η的区间积分界给整个裸pair核局部L1收敛，故此分布极限与(6)的实际迹相同。

## 5. Exact二维列给actual log²，两号都存在

内部共振r=(3/2)s、s=2^j3^k、j≥1,k≥0，两振幅乘积4/9。
在t=d，每pair difference-phase主项是sinh(d/2)=1/(2√6)。
令Lη=log(1/η)，二维三角计数为
#{j≥1,k≥0:ja+kb≤Lη}=Lη²/(2ab)+O(Lη)。
低scale展开误差与高scale平均尾各O(Lη)，sum-phase可和；边界行仅一维，亦O(Lη)。
故cross平均主系数为

\[
 C_{23}=\frac{(4/9)\sinh(d/2)}{2ab}
       =\frac1{9\sqrt6\log2\log3}>0.                     \tag{9}
\]

self中心t=0的exact r=s项由|I|≤Cmin(t,1/r)给O(ηLη²)；
nonexact沿同样height分裂给O1。固定β与窄φη的cross由ε23有界、βhat∈L1给O1，
fixed/fixed及全部returns也是O1，矩修正不改(9)。最终(3)的1/√2校准后得到

\[
 \boxed{E_{23}(g_\eta^\pm)=\pm C_{23}L_\eta^2+O(L_\eta).} \tag{10}
\]

所以mixed差[E(g+)-E(g−)]/2=C23Lη²+O(Lη)>0，
各自E(g+)正、E(g−)负。它是同一个完整逆的actual误差，而非B*B中裸ratio系数。
这里只给充分小η的严格存在性；Baker常数与固定operator费用很大，不声明数值阈值或实验拟合。

### 5.1 固定窗的无限指数与有限修复

任给N，利用<log2,log3>稠密，选x_i=logq_i落在同一patch内小区间，
q_i=5^i2^(m_i)3^(n_i)∈Q+，m_i,n_i为fixed整数。
这里5只用于选择源中心，Sonin算子仍固定S={∞,2,3}。
不同中心的5-adic valuation不同，q_i/q_j不属于<2,3>。
对各中心做相同双矩修正；中心间self/cross差均非exact。
用同一外部定理的2,3,5三个正有理数实例、fixed N后有限常数，所有off-diagonal平均O_N1。
每个diagonal由(10)给同号主项，故Gram为

\[
 [\mathcal E_{23}(g_{i,\eta}^\sigma,g_{j,\eta}^\sigma)]
 =\sigma C_{23}L_\eta^2 I_N+O_N(L_\eta),\quad\sigma=\pm1. \tag{11}
\]

在固定原L²源窗、每patch双pole-zero的闭子空间V上，E23有无限正、负指数。
任意有限余维闭条件或有限秩自伴源修复，因其kernel只删除有限维，仍保无限两号。
复源是该实Gram的Hermitian复化，不把实测试结论当全部未知full mixed正性。
这是fixed S={∞,2,3}的边界，未扩为所有finite S或cofinal S_L。

## 6. 原范数价格与完整Q的方向

记Cφ=∫|φ|²，Cφ,log=(2π)⁻¹∫log|v| |φhat(v)|²dv。
原du L²与zero-extension Dlog严格有

\[
 \|g_\eta^\pm\|_2^2=C_\phi/\eta+O(1),\qquad
 \|g_\eta^\pm\|_D^2=\eta^{-1}(C_\phi L_\eta+C_{\phi,\log})+O(L_\eta).
                                                               \tag{12}
\]

Dlog权是log(2+|ξ|)，不是log|ξ|，其低频差造成O(Lη)，不能改写为O1。
所有fixed corrections及分离patch的该norm cross一致有界。
完整Γ自身（含接触项）的价格则为

\[
 q_\Gamma(h_\eta)=\eta^{-1}
 [C_\phi L_\eta+C_{\phi,\log}-\log(2\pi)C_\phi]+O(1).     \tag{13}
\]

两patch完整Γ mixed有有限极限CΓ，其核是−e^(−|t|/2)/(1−e^(−2|t|))；
偶φ、镜像β的子族可证明CΓ<0。contact仅落在对角，未被删掉。
完整Q(g±)=qΓ(hη)±CΓ+o1，pp/pole由§2精确零，所以两族Q自身均在η小时为正，
Γ主价η⁻¹Lη远大于(10)。537的全源固定窗正性本来也覆盖这里，不报新正性。

由(10)/(12)，原L²规范化的误差为
±(C23/Cφ)ηLη²+O(ηLη)，Dlog规范化的误差为±(C23/Cφ)ηLη+Oη，均趋0。
这与560紧性一致；L1未归一发散绝不能冒充norm1发散或Q负。
560原全逆账本的平衡弱幂率也允许log²离点核，不单凭compact/弱幂尾判符号。
该旧账本后果及精确Γ mixed见norm原稿，不将常数优化当新whole输入。

## 7. 容量、fixed窗与成长尺度的边界

本轮使用了独立的有限log算术下界，但它给出的actual后果是比较误差不定，
不是Q的独立正容量。T23≥0与Q=T23−E23同时保留；E23≥0或≤0的无费设想均被实际反测否定。
有限矩/有限秩不能修这项fixed联合来源比较；560已经付的非有限秩紧K修复合法保留。
source-adapted、Γ-relative、不同共同inverse或独立几何容量也未被排除。

成长窗必须另核：S_L及K_L符号/范数，κ与S3/returns费，有限log常数随素数数目/高度的变化，
真正actual receiver像与source coverage、补空间/coupling、全Γ/pp/pole的同对象比较。
不能把fixed2,3的Baker参数当全g分布或growing S的统一控制。
最强旧542+555→557 whole leading4/5未改；通常Ξ与长期完成门仍open。

**局部瓶颈改变了：实际joint E23的未知号现已判定不定。宏观成长容量瓶颈未改变。**
这比“只恢复S3/域”强，按570统一结算一轮；不是新的外部Baker定理、world priority或RH证明。
C033一轮后停止追加η样本、return次数或第三素数。
下一准入应只检查560 exact residual的实际receiver像，是否存在保非有限秩/Γ修复的可判signed门，
先保存map/domain/norm及强旧净后果；若只有粗全H norm下界或unknown domination改名就入口止。

三原稿：[实际对象/迹域](../reviews/2026-10-20/joint-sonin-signed/actual-kernel-and-source-trace.md)、
[dense mixed/符号](../reviews/2026-10-20/joint-sonin-signed/mixed-returns-and-sign.md)、
[原norm/Γ/容量](../reviews/2026-10-20/joint-sonin-signed/narrow-source-norm-and-capacity.md)。
最终证明消费以独立终审及root前件收据为准。
