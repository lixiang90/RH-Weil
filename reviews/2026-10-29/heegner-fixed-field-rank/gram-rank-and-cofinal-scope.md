# 固定高度空间的共同Gram秩比较及cofinal范围

2026-10-29。独立数学／强旧原件。已恢复README／STATE，实际check后show通过，核G20261027、停止的C058、D20261029V、宏观前沿和唯一next-fixed-field-height-rank-comparison。本稿只证明有限维共同配对的标准矩阵后果并对齐537及既有rank资产；actual trace cycle的field／Mordell–Weil／height定义由另一独占原稿付款。没有把父代理或兄弟消息当成已读来源，未读新PDF／联网／扩章／做数值，不改STATE／cadence／Git／Goal，不准C059。

## 1. 必须先指定的实际对象

条件是：所有X的实际数据在同一个有限维height空间V中，或至少存在共同有限维数上界D；每层有一份对全部源对共同使用的sesquilinear／bilinear型h_X。核为

    K_X(r,s)=h_X(v_X(r),v_X(s))。

这里v_X可以nonlinear、rounded、source-adaptive、非局部、不连续，源系数／坐标／h_X的norm都可无界；不要求v_X预先线性。X和source固定选择顺序不互换，检验的是所有先fixed有限源对的K_X(r,s)逐项趋完整B_zeta(r,s)。共同配对和共同feature空间是必要前提，不把source-pair-dependent任意标量或任意不同form供应命名为同一Gram。

若实际目标是J0(37)(F)模torsion后tensor R的canonical-height空间，D指其Mordell–Weil向量空间维数，不是Jacobian的复维数。Rational coefficients、defined-over-F、类的torsion及height退化分别核。当前原件不假定这些算术前件已闭，也不猜M37的实际rank。允许height退化、甚至允许任意indefinite共同型时，以下rank证明仍成立；不靠height PSD给出否定。

## 2. 与非线性source map无关的矩阵恒等式

在一组n个先fixed源r_1,…,r_n上，把v_X(r_j)写作同一D维坐标列，组成A_X。按第一变量共轭线性的Gram约定，矩阵为

    K_X^(n)=A_X^* H_X A_X，   rank K_X^(n)<=D。       (1)

若原配对用另一Hermitian约定，只需转置／共轭，rank和正定性不改。Bilinear型用transpose而非adjoint，结论相同。每层整体乘任意scalar可吸入H_X，仍rank<=D。中心化v_X(r)-v_X(0)、fixed源适应的坐标选择或common moving basis也不增加维数。

式(1)只处理有限个已给向量，不在源函数空间上把v_X误作线性算子。因此source非线性、系数增长以及X依赖本身均不能逃此共同Gram秩上限；同时，式(1)并未证明v_X是合法物理映射、principal或height范数有原du上界。

复化要保所用域：若V_R的实维为d，标准Hermitian复化V_R tensor C的complex dimension仍d，complex Gram rank<=d。若只读两实height腿，或将Re h作为两腿realified配对，则可安全用实feature维数<=2d；不能无声把这个real rank界也记成d。若只有real源，原候选的imag腿可能实际为零，但须由真实rule核，不由本通用证明假定。

有限k个共同height通道可stack进direct sum，总feature维数至多kd；有限额外degree／pole腿也按实际finite rank相加。某个退化方向可降低有效rank，却不能增加它。下面统一用已经按实际scalar field和全部通道计好的有限上界D。

## 3. 537给出的固定有限测试族

537的已消费完整型在I=(-17/16,17/16)满足

    Q_zeta(r)>=tau ||r||_du^2， tau=2^-49162，
    r in C_c^infty(I;C)。                            (2)

它保完整Gamma/contact、proper powers和双pole，不需把Weil型简化为仅archimedean背景，也不外推成长窗。任意先fixed n可在I内取n个不交支撑的光滑bump，按原du归一化为r_j。对所有c in C^n，(2)作用于sum c_j r_j给完整mixed Gram

    G^(n)>=tau I_n，   rank G^(n)=n。                 (3)

这不是只检n个对角值：由同一完整二次型及其polarization定义G。原du正交仅给(3)的下界，不称这些bump在Q中恰正交。源组和n只依固定D选择，均在取X极限之前固定，不使用X-dependent matching Pan源。

取n=D+1，(1)令det K_X^(n)=0。若所有这些fixed pairs逐项K_X(r_i,r_j)->B_zeta(r_i,r_j)，有限维det连续性给det G^(n)=0，和(3)矛盾。无需源等距、uniform source上界、全Pan逐层exact消去、对X的Gram单调性或不连续map的Baire论证。

同一标准矩阵计算还给robust版本：取K_X^(n)的kernel单位向量c_X，则||G^(n)-K_X^(n)||op>=tau，因此max_ij |G_ij-K_X,ij|>=tau/n。此c_X可依X，不改变先fixed有限源组；若全部finite pairs各自收敛，finite max必趋0。该lambda_min/n只是(1)–(3)的直接矩阵后果，不是新独立严格费用、成长率或新数学轮；也不据此称哪一个fixed pair在所有X都失败。

这里有效kernel rank指全部finite Gram矩阵rank的sup，不是把nonlinear v_X误当线性算子的rank。若每层该rank有限而无共同上界，fullfixed-pair收敛的必要条件是它趋无穷：否则存在cofinal子列rank<=D，沿同一fixed D+1测试族重复矛盾。它只是一条必要维数条件，未给任何增长率或构造独立算术核。

## 4. 对角匹配不等于共同height-pair匹配

以下是不可删的标准反控制。仅在537已经独立支付的fixed窗上，取一条形式unit height方向e，定义

    v(r)=sqrt(Q_zeta(r)) e。

则h(v(r),v(r))=Q_zeta(r)对所有fixed窗源精确成立，但height-pair核为sqrt(Q(r)Q(s))，rank1。取两条Q正交unit源，其真实mixed项为0而此height-pair为1。这里sqrt用已付fixed窗Q，所以只是逻辑控制，不是假造经典全域RH正来源。

若实际只许有理系数，给定一条已存在且height h0>0的有理class P，可用floor(X sqrt(Q(r)/h0))/X乘P，使每个fixed源的对角height趋Q(r)；共同pair核仍rank<=1。这里P存在及h0非零本身是算术条件，本稿不宣称M37已经有此P；例子仅说明有理舍入也不修复“对角自动等于mixed”的推理。

即便复合标量r->h(v(r),v(r))恰是quadratic，按r±s、r±is在源端极化出来的B'也未必等于h(v(r),v(s))。前例的B'=B_zeta可以无限rank，而实际height-pair仍rank1；这不违反(1)。所以不能把任何nonlinear diagonal height表示、单边正性或独立positive-Dprime方案一并排除。

若另已证明v_X在height norm中渐近additive及complex-homogeneous，并付固定源的相应误差／norm费用，则才可能把diagonal convergence运输到共同mixed convergence；那是新增前件。Literal rounding的系数误差小不自动给height-norm additivity小，尤其cycle heights／H_X和标签数可成长。没有这些付款就停在diagonal-vs-pair区别，不用形式polarization跨过它。

同样，仅有一个下侧比较Q_zeta>=某finite-height正核，并未承诺mixed逼近；rank缺口不否定另有独立positive residual。旧10-27比较已明确上侧／双侧误差与正性下侧不同，本稿不把当前determinant矛盾扩大成全部正性证明路线边界。

## 5. 固定M／F也可能有无穷总通道

“每个fiber是同一finite-MW空间”不等于“全部feature只有D维”。若取V tensor ell2或L2(clock;V)，或对越来越多通道求和／积分，总source Gram秩可成长甚至无穷，尽管M与F都固定。只要有非零height方向，形式map y->r(y)e已给这种无限feature的普通du核；它不等于完整Weil型，却足以说明fiber有限rank不排整个family。

既有fixed窗Q正投影控制更强：在537 Q-Hilbert完成中取e_j，K_N(r,s)=sum_(j<=N)B(r,e_j)overline(B(s,e_j))逐fixed pair趋完整B，rank随N成长。这是10-27已付合法逃逸，使用已知fixed窗B，不提供经典全域独立正性、实际arithmetic class family或平移不变W_N。

因此本比较只排**总feature dimension有共同有限上界、以共同class-height配对逐项恢复全mixed B**的方案。不排growing/continuum通道、changing field/level/carrier、未取trace的CM点、infinite algebraic extension、独立infinite-dimensional Green/local/relative数据，或另有实物的principal函数/metric信息。任意source-pair-dependent form/权也可破坏(1)，但这时必须自己提供新的共同几何/算术身份，不能继续调用finite-height Gram标签。

## 6. 与最强旧结果的比较及计轮建议

直接旧链是537 fixed窗strict positivity，加标准有限矩阵rank闭性。10-27 modular-capacity原件已经以同一537排除fixed finite-rank线性数据的exact全Gram，保nonlinear源map及growing-rank/连续family；它还给原Hlog的更强uniform上侧／双侧误差门，不能拿本次较弱tau/n重报整体改进。本稿补齐nonlinear feature map也受共同Gram rank约束的理由，靠的是式(1)，不是此前source-linearity的非零核证明；未声称旧稿逐字已经写出所有这些量词。

587另已证明actual Sonin共同源补偿必须rank趋∞，含有费／移动range／signed/nonlocal，并特别指出receiver rank1不等于源型rank1。它的实际moment-spread与成长率不属于当前Heegner数据，不能搬来当MW高度费；但其rank角色警告正好防止本次误排固定M/F的连续通道。当前纯matrix必要性没有新的arithmetic输入、actualheight费或whole净后果。

故在actualfield／target经另一稿关闭后，本比较可以准确停止共同有界feature class-height核的cofinal全mixed修复；这是标准直接旧消费／准入范围核查，建议0新增数学轮，不建C059／596，不改cadence1/history59/latest595/formal19。若field或target仍欠，则以上只conditional，不能借matrix证明自行补算术前件。任一情况均不排完整Heegner／relative／Green路线，也不完成长期Goal。

主arithmeticprimitive/principal/sections/mixed、危险signed corecross／growingXi未付；strongestwhole仍542+555->557 leading4/5负惯性UPPER。Root须消费本原件、field原件及不同fresh后才结算，不以文件存在升级。此任务只写本原件，终态无numeric session／子任务／后继工作。

## 实际项目输入与版本

537读完整消费定理、原完整型和§4源域；10-27 root/old-net/fresh核rank／误差方向及投影/continuous-family逃逸相关段；587核§5源rank与receiver rank区别；其余只是本次恢复和准入范围。下列hash仅绑定版本，不替代数学或field来源证明。

| Path | bytes | SHA256 |
|---|---:|---|
| notes/537-source-exact-weil-window-positive-tail-admission.md | 8155 | 269a500556d37fc04a4e44efd2f0899414787743e529506dbbe7395a34eea9f8 |
| goals/reviews/2026-10-27-modular-principal-part-capacity-and-legal-completions.md | 10256 | c5d2572e880a98d338d048e9e04ac23ea4baed577b83b0cf235c48a238263116 |
| reviews/2026-10-27/modular-capacity/old-net-and-escapes.md | 13588 | af45262b46797166bd974b61a912d0e3b99a97a807c4c2cd395d015383ff38ce |
| reviews/2026-10-27/modular-capacity/fresh-review.md | 7280 | 7c0f9c2e7b306faec8794218d306db5bd1c9b09ac1ceb267267cfe003b87061c |
| notes/587-actual-sonin-moment-spread-and-growing-source-rank-necessity.md | 8681 | e4d30cfb6d07299386014cb4c4e3e3979ab5111264355dfb37b24629f121ac82 |
| reviews/2026-10-29/heegner-principal-source/next-fixed-field-height-rank-comparison.md | 2723 | 1c4d2f9522b4a163acfd392e513640f60743f5a0976d49e89548a3013d7b6708 |
| goals/review-cadence.json | 6681 | 73ef5152185e3213a7b076a76a656c0a5a0acf9ace994c612def2de270584f4b |
