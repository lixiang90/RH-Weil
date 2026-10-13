# 晚素数的统一源质量子项与完整返回迹的消费缺口

2026-10-14；C006第二且最后一轮，起始HEAD
`44337d2e1492c093dcb263f5ecf57c4676eed3e6`；长期比较基线保持3a72930。
证据分为proved的子项/算子估计与open的完整预算。
[主独立核](../reviews/2026-10-14/c006-uniform/kernel-subterm.md)、
[直接kernel审查](../reviews/2026-10-14/c006-uniform/direct-budget-audit.md)、
[来源/联合负对照](../reviews/2026-10-14/c006-uniform/source-budget-audit.md)及
[不同组织逆审](../reviews/2026-10-14/c006-uniform/reverse-budget-audit.md)保留原推导和降级。
未证明完整D_p的可求和范数，也未找到actual发散反例。

## 1. 原目标与已付新增

沿[533](533-actual-late-prime-sonin-boundary-square.md)，冻结两patch支持U，
跨度W=log√6<log3，V为逐patch两矩零合法源的L²闭包。
所有p≥3的实际primepower项在V严格0。
真实D_p=T_p−T∞在V紧；fixed smooth源的p^-2正首项和求和已付，
uniform首项norm渐近严格不可能，但uniform绝对上界未被排除。
本轮原目标仍是||D_p||≤Cp^-2或较弱∑_p||D_p||<∞。

真实密度的完整组织为

\[
 \rho_p-\rho_\infty=-2r\cos(as)\rho_\infty
  +(1-2r\cos(as))\sum_{j\ge1}r^jM_j(s),
 \quad r=\frac{q}{1+q^2},\ q=p^{-1/2},\ a=\log p.
\]

裸q²mass已精确取消；M_j=〈k_s,[P(U_a+U_(-a))P]^jk_s〉。

**本轮已证的实际全源子项：**令J_a(g)=∫|ĝ(s)|²cos(as)ρ∞(s)ds。
它在固定有界源U的L²压缩满足

\[
 \|J_a\|\le C_U e^{-3a/2},\quad a>W,
 \qquad \|-2rJ_{\log p}\|\le C_U p^{-2}\quad(p\ge3). \tag{1}
\]

不需要g的导数，包含所有joint carrier/p。它支付完整密度的第一个子项，
不支付其余完整signed返回和。

## 2. actual off-diagonal核与无导数源费用

实位L=(0,1)、H=I−L、K₀=LFL、R₀=(I−K₀²)^(-1)，
P=H−HFLR₀LFH。R₀−I=K₀R₀K₀有smooth cosine-even核J。
ρ>1时实际缩放trace分布的非identity核来自
−√ρ∫_1∞(FLR₀LF)(ρx,x)dx。

bare FLF给

\[
 -\sqrt\rho\sum_\pm\frac1{\pi(\rho\pm1)}
       \int_1^\infty\frac{\sin(2\pi(\rho\pm1)x)}x\,dx.
\]

∫_1∞sin(kx)/x dx=π/2−Si(k)=O(1/k)，故该核O(ρ^-3/2)。
这是actualΓ与δ的全部非振荡项取消后的核，仍按2θ′，
不能先分别对两个ρ^-1/2项取绝对值。

smooth J修正先在低变量t积分：endpoint1首项为
sin(2πρx)f₀(x)/(ρx)，f₀(x)=∫_0¹J(1,u)cos(2πxu)du。
对u再作端点积分得f₀,f₀′=O(1/x)，于是f₀/x及其导数可积。
x一次非驻相给O(ρ^-2)，恢复√ρ后为O(ρ^-3/2)。
其他低端点/深余项同阶或更小；t=0的奇导数为0。
这里先用有限physical cutoff辨认连续off-diagonal核，再在合法source trace分布消费，
不宣称未夹源的U_ρP是ambient TC。

对源U×U，|t−u|≤W，j(a+t−u)的实对称核被C_Ue^(-3a/2)控制。
Schur或||R_g||₁≤|U|||g||²给(1)。冻结p≥3的ρ最小为3/√6>1，
所以没有靠近identity的额外未付前件。与533相比rate较弱，whole L²量词更强。

## 3. 实际cutoff的Schatten输入与局部TC费用

真实F_p=BFB^(-1)，K_p=LF_pL，δ_p=K_p−K₀。
actual operator-norm身份为

\[
 F_p=(1-q^2)\sum_{n\ge0}q^nU_{-na}F-qU_aF.
\]

low square中的第n项q^nLU_(-na)FL有核2cos(2πp^nxy)，HS norm≤2、
operator norm≤q^n。因此对r>2，Schatten插值给
||δ_p||_(S_r)≤C_rq^(1−2/r)，尤其S₆≤Cq^(2/3)，而op≤Cq。
反向low修正实际kernel幅度−2q²，不是粗unitary norm q。
所有足够late p的||(I±K_p)^(-1)||共同有界，因为||K₀||<1及δ op→0。
原531非HS结论保持；这是固定cutoff1，不是growing cutoff/S的gap。

令R_(σ,p)=(I−σK_p)^(-1)，R_(σ,0)=(I−σK₀)^(-1)。
h(K)=K(I−K²)^(-1)的精确三阶及以上resolvent余项为

\[
 H_{3,p}=\tfrac12\bigl[(R_{+,0}\delta_p)^3R_{+,p}
                     +(R_{-,0}\delta_p)^3R_{-,p}\bigr].
\]

全部actual inverse保留，两个尾是加号。严格有
||H₃||op≤Cq³、||H₃||HS≤Cq²。

对real source置Z=A_g*A_g，M_p=LZH F_pL。Z的physical核为
R_g(log(y/x))/√(xy)，LZH只连接
x∈[e^(-W),1]、y∈[1,e^W]。所以
||LZH||HS²=∫_0^W t|R_g(t)|²dt≤W²||g||⁴/2。
写M_p=M₀+M_δ，有限high band使M₀为HS×HS的真正TC，
||M₀||₁≤C_U||g||²；||M_δ||HS≤C_Uq||g||²。
由op×TC及HS×HS得到**独立localized product**

\[
 \|H_{3,p}M_p\|_1\le C_Uq^3\|g\|^2
                       =C_Up^{-3/2}\|g\|^2. \tag{2}
\]

(2)是可对素数求和的真实TC乘积费用。
它本身不证明该ordinary trace就是完整actual overlap中合法分离的高阶尾。

## 4. 另付kernel块与joint负对照

直接审查给actual bare两Fourier high-scale砖块的源费用：
同scale r的核含
[r·2sinh(t/2)]^-1{Si(2πr(e^t−1))−Si(2πr(1−e^-t))}。
t≤r^-1/2时幅度≤C/r，外区≤C/(r²t²)，故L¹_t norm≤Cr^-3/2。
不同p幂scale的phase有gap（p>e^W），Si的π/2项取消给O(p^-2max(n,m))。
Young给无源导数的source-L²费用。
相邻两fast cutoff另有精确K_r²=r^-1[L−LFH_rFL]，
H_r=1_(x>r)；在固定smooth低dress/source边界核上，
其r^-1质量与余项可明确区分，不据此删掉所有nonadjacent/low cross。
具体域与残余费用见direct稿；这些砖块不冒充完整resolvent预算。

R≈p或p²的窗口也没有给实际反例。
finite fiber中B的range projection rank等于原band rank，
phase平均trace差的零harmonic在所有q阶精确0。
只保留q²M₂会伪造1/p质量；遗漏分子cross同样错误。
实际Γ窗口误差若比目标费用大，只说明现有误差不够，不能宣称actual norm大。

## 5. 迹域降级与完整预算未付

本轮最重要的逆审纠正是：
已付A_gR_pA_g* TC，不自动授权任意finite-angle截断trace的收敛；
强收敛不是迹收敛，正负无限角的拆分必须保持共同极限。
h(K_p)M_p整体未在whole L²上证明TC。
H₃绕K₀的非交换展开，一般不与K_p交换，
不能把全h的逐角标量恒等式未经证明套到这个子项。

因此“从E_p扣除2ReTr(H₃M_p)得到actual零、一、二阶aggregate”的消费目前conditional。
该差作为数值定义有意义，但还不证明它等于所声称的有限低cycle核。
需要ambient双cutoff block公式与source-cutoff trace的合法联合极限。
主代理发现这个风险，来源稿已降级，逆审保留它。
没有把localized TC费用升级为实际完整高尾，也没有把它升级为完整D_p预算。

逐项positive-return界仍留高载频logR：对固定p、长Γ窗口，C_a在内部作用近2cos(aR)，
M₂可随K(R)增长。完整返回与分子signed取消必须先付，
不能用533固定s polynomial误差或generic relativeΓ替代whole源L²费用。
当前既没有∑||D_p||<∞证明，也没有实际不求和反例。

## 6. 结算、实际瓶颈与停止/重新准入

新增可消费输入是(1)的actual全源p^-2子项、实际cutoff的S_r控制、
localized TC乘积(2)及高scale砖块；不是仅增加文件或重复固定源渐近。
来源消费箭头局部改善，但完整signed统一费用的瓶颈没有消除，
迹域审查又明确了一个此前被轻率跳过的前件。
本轮不提供实际ζ谱带、完整Weil正性或最低态约束；长期Goal保持active。

C006按第二末轮止损，停止继续用未知返回预算命名新条件。
成长single-p费用路线只在有actual共同trace-kernel身份及新的低cycle signed界时重新准入；
原uniform绝对上界、positive compact增量及Sobolev限制仍未被排除。
不能说这条实际方法已证明发散，不在此缺口未付前运输base S或扩大S/U。

唯一下一动作转[C007](../goals/contracts/C007-first-prime-compact-overlap-sign.md)：
借532已经支付的first-prime非紧桥，在原冻结实际V上审
QW−T₂=−E₂的剩余紧型符号，直接用真实Mellin density/完整G₂逆，
尝试证明E₂≤0或给合法源的严格正E₂反例。
不把未知low投影定义成新正性，不恢复C001扩N或旧实位紧修复。
