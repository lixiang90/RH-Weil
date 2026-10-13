# C010：固定移位的exact全惯性sign与连续最低态消费

2026-10-14；同一C010研究轮。恢复AGENTS/README/STATE/check/show、Goal及当前合同。
新增门只用s=t=10^-34、原224每parity head及80dps；未扫描其他s/N/digits，未使用ζzero。
先冻结[shifted-inertia-preregistration.json](shifted-inertia-preregistration.json)，
自写[scripts/c010_shifted_inertia_certificate.py](../../../scripts/c010_shifted_inertia_certificate.py)。
不改STATE/cadence/git或旧证据；本次脚本最终exit0约135.015秒，无pending process。

## 1. 精确移位、顺序和新的分母

原C009已经支付m≤M≤b、source errors及正inverse envelopeW₀≥G₀>0。
t=10^-34<m−n；M_t=M−tI仍有positive complement。原D=B−A²保持：
A_t=A−tI、B_t=B−2tA+t²I，B_t−A_t²=D。
采用G_t≤(1−t/m)^-1G₀，W_t=(1−t/m)^-1W₀，
W_t^-1=(1−t/m)W₀^-1；不拿未认证trial来逼近新inverse。

以m_t重算原α/β，θ=2^-48、χ=1不变，得到

    P_t=P₀−(t/m)W₀^-1−ΔαI−Δβ(D₀+ε_D I).

同一λ>0和B_c nonsingular的congruence得到Kt，
详式与非交换顺序已由[独立congruence审查](shifted-congruence-audit.md)核准。
脚本没有将任何scalar直接int截断，而是Fraction构造四个rational corrections。
各denominator bit lengths为75/750/750/750，共同positive LCM的bit length为824，
并逐个核`scalar_integer/D == scalar`。

combined exact编译取Y=VQ_d^-1、F=aQ_da−17S₀b_raw，并用Y*，
没有假设Y自伴或a、V commuting。原a/b由source raw endpoint sums构造，
V、K₀来自C009新重建原packets；其input SHA在compile receipts及主独立审查绑定。
base raw source-matrices hash仍为4bce98228442805bc5ae16e9c26c8df88e85c35ab7ec8deffdd808adbf1217ac。

## 2. scaled lower target：正比例说明纠正

脚本先exact编出K_integer=D Kt。两个sector的max entry bit B均为4177，
定义512-grid integer

    Z_ij=floor(2^512 K_integer,ij/2^B),
    T=Z−224I.

因为symmetric entry rounding error在[0,2^-512)，全row norm<224·2^-512，严格有

    T/2^512 ≤ K_integer/2^B = (D/2^B)Kt.              (1)

D/2^B>0，故惯性方向保持。不是Kt/(D·2^B)。
运行时加载的旧metadata串写反比例，而矩阵计算从始至终是上述正确公式；
代码与预注册文字已修，旧runtime receipt不改数学结果、不重跑编译。
[shifted-scale-interpretation-receipt.json](shifted-scale-interpretation-receipt.json)
明确纠正解释并绑定原target/Gram hashes。仅这项文字错误不影响(1)。

## 3. odd PSD与even rank-one门

固定guard g=2^372，物理512-grid为2^-140。
odd直接取T；even只取一个ordinary80 inverse-iteration direction，
冻结integer w_i≈2^192 v_i，ρ=2^-105，exact512-grid rank-one更新为

    W=2^23 w w^T≥0,
    W/2^512 = ρ(w/2^192)(w/2^192)^T.

w无需exact unit norm或认证为leastvector，rank(W)≤1就足够。
普通even direction Rayleigh约−2.170914878e−37仅用于proposal，未当成惯性证书。
取ordinary Cholesky of (T+W−gI)/2^512，然后floor256-bit factor为整数F。
这个factor是proposal，最后必须exact验证

    T+W = FF^T+gI+E,
    max_i Σ_j |E_ij| < g.                            (2)

odd的W=0。所有224行及完整Gram cells都保留，不从Cholesky pivot或旧3353-bit费用推新sign。
本辅助两sector各自完整row检查通过，max residual bit length均263，远小于guard bit length373。
目标及factor packets为`shifted-sector-{0,1}-target.json`、`shifted-sector-{0,1}-gram.json`；
结果为[shifted-inertia-result.json](shifted-inertia-result.json)。factor保存full square且upper triangle为0，
没有把full square当错误的triangular schema忽略其余entries。

主代理另写自主reader/Gram checker，实际重核两个224的全部448 rows、
两个完整上三角共50400 cells、upper-zero结构、源/目标/compile hashes和wrong diagonal负对照，
见[independent-shifted-gram-result.json](independent-shifted-gram-result.json)。该新全行结果已直接读核。
本消费不只依赖生产者PASS。

(2)给odd T≻0；even T+W≻0，所以T在w⊥正，n_-(T)≤1。
结合(1)与positive congruence，有

    n_-(P_t,odd)=n_-(Kt,odd)=0,
    n_-(P_t,even)=n_-(Kt,even)≤1.

positive lower approximation的方向没有倒置；Kt负方向本身仍不等于Q负方向。

## 4. whole-source惯性运输及真正ground

原bounded Block–Schur变坐标、positive complementary block及全部source allowances先已支付；
新m_t/α_t/β_t仍满足同一条件。square completion与finite lower P_t给

    n_-(Q−sI,parity) ≤ n_-(M_t+K+U,parity) ≤ n_-(P_t,parity).

左侧是closed form negative index，不把finite target的惯性等同于Q的惯性。
完整τ正项此处保守丢弃，s=t严格合法；未重复删除 Γ/pole/prime。
simple结论还须actual even upper，不从odd positive head自己推出。

已逆审的even rational closed-form source给

    λ₁_even≤u=7954159549289785371664718615168914673915149/2^256 <10^-34=s.

其完整Γ high tail与head source errors已付，不能以R Rayleigh代替u。
上面的whole index门使Q的odd sector无eigenvalue<s，even sector至多一个（multiplicity计数）。
actual even upper同时强制even sector至少一个eigenvalue<s。
536/537已经给same-norm closed form及compact resolvent，因此bottom attained而非只infimum。
奇偶core可在原缩支撑/卷积论证中选even mollifier，保持even/odd与real/complex子域，
所以不在auxiliary polynomial零延拓上偷换legal域。

于是本门与实际上界共同严格给

    λ₁_odd≥10^-34,
    λ₂_even≥10^-34,
    0<τ≤λ₁_even≤u<10^-34,

真正full-window最低eigenvalue在even sector且complex multiplicity1。
从real commuting kernel可选择real even ground vector；不是ordinary proposal的性质。
global第二谱距ground至少s−u>3·10^-35。

## 5. 本轮净后果与范围

消费成立于actual完整complex Weil窗L=17/16、原Lebesgue norm及完整source/error/complement链。
这是同对象真正ground排序的新有限窗输入，超出537仅coercivity和pilot有限谱。
没有证明增长λ、C001 μ13窗、RH或与ζ/Ξ/prolate的全域相认；535无费用Sonin桥不复活。
不将script、整数PASS、合同完成或保存推送当宏观Goal完成。
source/sign门本次无剩余conditional：数学positive scale/rank/连续运输与主独立全行校验都已支付。
本辅助终态已保存，无pending process，不修改STATE/cadence/git或旧证据，不新增轮数。
