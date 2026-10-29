# 全fixed-I源L²边界块的trace-class因子化：独立交叉检查

2026-10-29；`/root/onebody_variation` 的新明确任务，独占本文件。**Limited PASS：下述T=L(A_r*A_r)H的显式S1因子化，加上actual535在smooth密集域已闭的overlap身份，足以独立闭合whole fixed-I源L²上的晚single-prime上界 C_I(logp)/p。** 这与已冻结12150-byte稿所恢复的533 fixed-smooth p^(-2)定理具有不同量词；不能覆盖/改写533，也不能把新的whole-unit-ball结论混回已经停止的fixed-r重证明。

本稿未读取当前平行新原稿；按root给出的明确新input独立核了因子化、C1方向、series/trace域及source范数。原operator-first-variation.md的12150字节及hash保持不变。未修改STATE/cadence/Goal/库/Git，没有新来源/数值，不预授C065/602或Goal完成。

## 1. 恢复与被审的新范围

新任务到达后重读当前STATE/README、执行check后show；Goal/C064/AK/frontier在本任务前一阶段已经实读，当前C064仍stopped，runtime1793085111及远端73228ef为root现场观察。本文件不自行操作运行Goal。

Root明确授权的范围变化是：旧533 fixed smooth源的可求和p^(-2)已经paid；现只审**无source导数、同一fixed bounded I上的全部L²单位球**，允许source随p、X或carrier改变。需要实际完整source差额算子D_p^I，不是较弱fixed-r O(q/log^N p)重证明，也不是535裸kernel或534某个H3 localized scalar。

设I为固定有界log-source区间，宽W>0，源先实r∈Cc∞(I)，后扩张L²(I,C)。H_phys=L²((0,∞),dx)，cosine F核2cos(2πxy)；L=1_(0,1)，H=I−L，K0=LFL，κ0=||K0||<1。实位Sonin P、actualFp与Π_p保原fullinverse。记C=A_r*A_r、q=p^(-1/2)、N_p=L(Fp−F)L，h(K)=K(I−K²)^(-1)。

所有常数C_W及p0可依fixed I/κ0，**不依r的导数、频高、p或实际取值方向**。本结论不支付growing-I的常数，也不支付一般base-S添加prime。

## 2. 新的全源边界块S1因子化

在unitary log表示中，U_a是平移，A_r为r卷积。固定地平移I至[0,W]：r的整体平移只使A_r左乘一个unitary U_b，所以C=A_r*A_r精确不变，源du范数不变。此不是随p挑选新source。

在log表示令E=1_[0,W]。A_rL的输出可到W但不能超过W；A_rH的输出严格在正半轴。因此两者共同输出恰可插入E，严格有

    T:=LCH=L A_r*A_r H
        =(E A_r L)* (E A_r H)。                         (2.1)

这条身份由卷积核支撑直接核，不是假设TC。两个因子各自Hilbert–Schmidt，并有

    ||E A_r L||HS²≤W||r||du²，
    ||E A_r H||HS²≤W||r||du²，
    ||T||S1≤W||r||du²。                                (2.2)

例如第一个HS平方是∫_(0≤v≤W)∫_(u<0)|r(v−u)|²dudv，内积分≤||r||²；第二个同理。对任意compact L²源均成立，不用r的任何导数。

返回physical x坐标后，T的kernel是

    T(x,y)=c(log(x/y))/sqrt(xy)，
    e^(-W)≤x≤1≤y≤e^W，
    c(t)=∫overline(r(v))r(v+t)dv。

对real r，c实偶；其连续性来自L²平移强连续，且||c||∞≤||r||²。故此kernel在固定rectangle有统一bounded代表，bound为C_W||r||²。这里不要求c可微，也不从HS擅自升级S1；S1由(2.1)独立支付。

## 3. actual overlap的迹域：密集域身份与有界差额扩张

旧535及c007 trace-domain-proof对每个real smooth compact源已支付

    E_p[r]=2Re Tr_L[h(Kp) T Fp L]，
    E_0[r]=2Re Tr_L[h(K0) T F L]。                      (3.1)

这是actual source夹心ordinary trace，经完整overlap block身份及合法两半TC循环给出，不是534仍conditional的任意角截断高尾猜测。原p≥任何fixed素数都保全Gram inverse，不换projection product。

(2.2)现在直接使(3.1)右侧对全部L²(I)成为ordinary TC×bounded局部迹，且随r的L²逼近连续；不需要再对h(Kp)做角谱截断。左侧的实际差额在fixed-I也已有bounded source实现：560给

    t_p−t_empty=−P_p^prime + K_p^I−K_0^I。

其中每个K_B^I为自伴紧source算子；primepower项是有限个bounded shifted相关。对于p>e^W，全部该prime powers相关严格0，所以D_p^I:=K_p^I−K_0^I就是smooth域的t_p−t_empty，并在全L²(I)有唯一连续延拓。

因此在密集real Cc∞(I)用(3.1)估计actual差，再凭L²连续性延拓，即得**bounded差额**的whole-unit-ball结论。没有定义一般L²源各自可能无限的t_p、t_empty后再作∞−∞。对complex源，Π_p和P为real算子，smooth混合S1 trace给t_p[r1+i r2]=t_p[r1]+t_p[r2]；actual difference的real Hermitian source核使此等式在L²延拓仍成立。故分别界real/imag两项即得同一常数乘||r||²，不能对complex C直接冒用C与Fp交换。

## 4. 全返回的operator二阶余项统一付费

actual operator-norm展开为

    Fp=(1−p^(-1))Σ_(n≥0)F_(p^n)−p^(-1)F_(1/p)，
    F_λ(x,y)=2cos(2πλxy)，||F_λ||op=λ^(-1/2)。

等价于旧q^nU_(-nlogp)F形式；high-scale核中没有额外q^n振幅。于是D:=Fp−F满足||D||op≤2q/(1−q)，N=L D L亦O(q)。选择p≥p0使||Kp||≤(1+κ0)/2，所有R_(σ,p)=(I−σKp)^(-1)共同有界，σ=±1。

因h(K)=1/2[(I−K)^(-1)−(I+K)^(-1)]，精确resolvent身份给

    h(Kp)−h(K0)
      =1/2 Σ_(σ=±1) R_σ N R_σ + Q_p，
    ||Q_p||op≤C q²，R_σ=(I−σK0)^(-1)。                 (4.1)

Q_p不是未控Neumann截断；其每个项含两个N和一个完整R_(σ,p)，故保全部actual returns。R_σ为fixed arch对象。

将Fp=F+D代(3.1)，得到三类项：

    E_p−E_0
      =Re Σ_σ Tr(N C_σ) +2Re Tr(h(K0) T D L)+Rem，
    C_σ=R_σ T F L R_σ，
    |Rem|≤C_W q²||r||²。                               (4.2)

余项包括Q_p T FpL与线性h差乘T D；全部只是TC×bounded，费用由||T||1、||D||=O(q)、||h(Kp)−h(K0)||=O(q)付清。这里无需534的S6/H3角消费，也不把localized乘积认成actual高尾。

## 5. 第一线性项：C1必须在正确的input坐标

固定R_σ的kernel为I加smooth kernelS_σ。一个无新外部定理的证明是

    R_σ−I=σK0+K0 R_σ K0。

K0的cosine rows及其任意有限阶导数在L²(0,1)一致有界；中间R_σ bounded，所以S_σ在闭low square具有全部有限阶bounded derivatives。h(K0)=1/2(S_+−S_−)也有smooth kernel。

T仅有(2.2)及bounded continuous rectangle kernel，但T F L的**input x∈[0,1]**的C1由F提供：

    (T F L)(y,x)=∫_1^(e^W)T(y,z)2cos(2πzx)dz。

z在固定finite band，故该式及∂_x均≤C_W||r||²；不微分T或c。右乘R_σ的smooth S_σ保input C1，左乘R_σ保output y的bounded bound。因此C_σ有满足

    sup_(x,y∈[0,1])(|C_σ(y,x)|+|∂_x C_σ(y,x)|)
         ≤C_W||r||²                                  (5.1)

的kernel代表，且C_σ∈S1。这里y是trace中N(x,y)的第二坐标，x是C_σ的input坐标；不能把只在output有正则性错放到本次积分变量。

对每个λ≥1，LF_λL与C_σ均HS，故其乘积的ordinary trace由HS×HS核公式给

    Tr(LF_λL C_σ)=2∫_0^1∫_0^1cos(2πλxy)C_σ(y,x)dxdy。

对fixed y，(5.1)的一次x分部积分给C_W||r||² min(1,1/(λy))。分y≤1/λ和y>1/λ积分，得到

    |Tr(LF_λL C_σ)|
          ≤C_W (1+logλ)/λ ||r||²。                    (5.2)

这只用input C1及boundedness，不借smooth source。实际N展开为

    N=−p^(-1)K0 +(1−p^(-1))Σ_(n≥1)LF_(p^n)L
                        −p^(-1)LF_(1/p)L。

该series在operator norm收敛，C_σ是TC，所以逐项取trace合法；(5.2)又给绝对可和的trace费用。两个low项的low-square kernel都O(1/p)。因此

    |Tr(N C_σ)|≤C_W (logp)/p ||r||²。                  (5.3)

log来自y趋0的input积分，不是source导数或未知返回gap。

## 6. 第二线性项：正则性改由h(K0)的output提供

令V=h(K0)T:H_band→L。它是TC，input y只在[1,e^W]；smooth h(K0)给**output x**的bounded C1：

    sup_(x∈[0,1],y∈[1,e^W])(|V(x,y)|+|∂_xV(x,y)|)
          ≤C_W||r||²。

对单个F_λ，trace为∫_(x∈[0,1],y∈[1,e^W]) V(x,y)2cos(2πλxy)dydx。因为y≥1，一次x分部积分没有y≈0的log费用，得到C_W λ^(-1)||r||²。low/reverse项仍由finite rectangle kernel给O(1/p)；fullseries在operator norm收敛，V TC付trace极限。故

    |Tr(h(K0)T D L)|≤C_W/p ||r||²。                    (6.1)

这一项与§5采用不同坐标的C1来源，两者均不要求T/c可微。若只写“kernel光滑”而不分清这两个方向，会误用L² source正则性；本次已逐项核正方向。

## 7. 新whole fixed-I界及准确后果

(4.2)、(5.3)、(6.1)与q²=1/p合成，对p>max(p0,e^W)，所有real smooth r∈Cc∞(I)有

    |t_p[r]−t_empty[r]|
       ≤C_I (logp)/p ||r||du²。

按§3延拓及real/imag拆分，得到actual bounded source算子

    ||D_p^I||_(L²(I,C)→L²(I,C)) ≤C_I (logp)/p。          (7.1)

包括source/carrier随p改变，但I固定。这不是533已排的uniform p²首项norm渐近，也不证明Σ_p||D_p^I||<∞；(7.1)的充分upper本身不对prime可求和，不能反说实际norm和发散。

按Chebyshev/PNT的旧prime费用，Σ_(p≤X)(logp)/p=O(logX)，有限head吸收入C_I。故whole unit ball的empty-base onebody差额满足

    ||Σ_(p≤X)D_p^I|| ≤C_I(1+logX)。                    (7.2)

若写原source K_≤1^I=K_0^I+Σ_(p≤X)(K_p^I−K_0^I)，还须保全部actual P_p^prime：K_p−K0=D_p+P_p^prime。fixed I仅有限个p^k≤e^W可见，故这些source-shift算子的全部和有fixed C_I费用，不会随X增长。于是同样||K_≤1^I||≤C_I(1+logX)。Γ/contact与共同pole在差分系数中取消，不是从完整目标中删除。

旧533给每个fixed smooth源的onebody和收敛，极化后每个fixed finite源组Gram有界；它已经蕴含旧585/587所有fixed-r/fixed-E的manyprime归因。这些**不作新结果**。本次新scope是(7.1)–(7.2)在整个fixed-I L²单位球上的共同operator norm费用，含改变source、频高和joint source选择；它不能由逐fixed-source有界/收敛或有限E矩阵界推出。

对all-pair connected和，actual J_X^I=K_(F_X)^I−K_≤1^I，因此(7.2)给该同对象分解的whole-unit-ball误差O_I(logX)。它仍不提供J_X的有利sign、growing I的共同常数、fullQ正性、principal/mixed RR或成长Ξ；whole4/5负惯性UPPER及Goal关键瓶颈不能因此自动宣称改变。

## 8. 与旧534/535的最强实际消费比较

本稿定向重读534正文及c006-uniform的source-budget-audit、direct-budget-audit。它们已经支付M0=LCH_band F L的HS×HS TC、Mdelta仅HS，以及H3局部乘积的可求和费用；原文明确没有把任意完整h(Kp)M_p局部trace消费为actual whole-L²高尾。它们没有使用§2的T本身S1因子化，也没有消费(7.1)或(7.2)。

535后来对smooth源支付了完整actual overlap两半S1与局部ordinary trace身份；这个paid输入在本次使用，不重新计源域lemma。新T-S1使整个局部full-return表达有统一L²连续费，因而可用already-bounded fixed-I差额密集扩张；再以§5/6的正确C1方向直接估计完整一阶和op二阶余项，不走旧未付的任意角切分/低cycle分类。

所以本检查未发现指定旧消费记录已经包含此whole-unit-ball O(logp/p)结论。数学新credit是否成立、是否需要登记C065/602以及宏观节奏，仍由root结合其它旧exact分解与不同fresh判断；不能仅因standard因子化/IBP就强定0，也不能靠“whole”标签直接完成Goal。

## 9. 原件与执行范围

本任务只写本新文件；旧12150-byte原稿及所有历史533/534/535不改。实际核对535、c007 trace-domain-proof；本scope重读534、c006-uniform的source-budget和direct-budget全文；本子任务未读当前平行新稿、没有外部primary/PDF/数值。以下hash只认版本，不代root完整消费或所有nestedsource审计。

| 输入 | bytes | raw SHA256 |
|---|---:|---|
| `reviews/2026-10-29/onebody-full-returns/operator-first-variation.md` | 12150 | `1c1f5ed54b9030e866c886fae819091413e81090698f17ce9517ebd4c0f13599` |
| `notes/533-actual-late-prime-sonin-boundary-square.md` | 9978 | `3b15593b57a0b5dab22409df4baac440fc04491fcff1b2f10b6451404b7ca478` |
| `notes/534-actual-uniform-sonin-subterms-and-trace-consumption-gap.md` | 8097 | `19fa13a6fda7d3deaf84c78a2794d759ca784c3e0248fa7f904adca60d554c28` |
| `notes/535-actual-first-prime-sonin-log-resonance-and-indefinite-error.md` | 9910 | `e83c3e080d19c2534425fb3c0e469367012f6c566a470b3baba703fb6def146f` |
| `reviews/2026-10-14/c007-sign/trace-domain-proof.md` | 5507 | `bae082f91a0f01a44fa3e3d1e9e0685bfa28e63a8dca32b822f395ad7b306094` |
| `reviews/2026-10-14/c006-uniform/source-budget-audit.md` | 9039 | `0931ae5bedd5d0d1e57b4a9eac7e2bbe0397268bbc04b2f39257ccd4d31775ba` |
| `reviews/2026-10-14/c006-uniform/direct-budget-audit.md` | 12054 | `f5493d2f2b1a3b2bb612943d9d1ae73471f2c5573ee3aecf13cb32b8e16dd039` |
| `notes/560-joint-finite-place-sonin-primepower-cancellation-and-compact-weil-bridge.md` | 9263 | `9c2e6cd5a9eae269ad04b332699c21eec7403a230f9557afa8b895c45d4228d3` |
