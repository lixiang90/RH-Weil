# 406有限修复逆审：Fredholm尾、源矩、次数与Green规范费用

2026-10-14，独立来源适配，零轮；不建立C022，不编辑STATE/Goal/cadence/Git。
已恢复AGENTS/README/STATE、check/show、同G20261014 Goal/frontier、D20261014Z、
next-adelic-primitive-source-gate、406与405必要原件。结构check不认证数学。
入口HEAD=56270972893773289738ad258151bb4174cb742a、working tree clean；
子get_goal=null不代root active实例。固定0c4f/≤538及唯一cadence不变。

**裁定：** finite rank、compact source、degree normalization和Green compensation均有合法构造，
不能由旧literal无限零点障碍将它们一并排除。下面支付其真实费用与最便宜有限反检验。
目前只有analytic/truncated接口，没有独立数域Hodge对actual全Weil的新增比较；来源入口0停止。

## 1. 实际η₀及标准有限Fredholm族

405/406固定实际源

    η₀(r)=P(πr²)e^(−πr²)，P(z)=4z⁴−28z³+41z²−9z，
    p(x)=Eη₀(x)=2Σ_(n≥1)η₀(ne^x)。                         (1)

源端η₀(0)=0、∫η₀=0，p∈S_exp、c(p)=d(p)=0，p≠0，是已付principal/root见证。
在真实idele参数λ=e^x上，对角A有±n二重特征值η₀(nλ)。定义固定rank截断

    p_R(x)=2Σ_(1≤n≤R)η₀(ne^x)，
    F_R(z,w)=Π_(n=1)^R(1−zη₀(ne^w))²。                     (2)

它是406标准linear-pencil Fredholm族的实际有限对角截断，不按Q反造对象。
F_R(0,w)=1，−∂_z logF_R|_0=p_R(w)。Gaussian strip |Imw|<π/4内全纯。
当各η₀(ne^w)非零时，z-degree精确为2R，含重数；例如实λ=2时全部非零：
z_n=π(2n)²>12，P(z)=z[4z²(z−7)+41z−9]>0。
这给具体非空finite divisor，不靠literal无限零点重复旧反例。

## 2. fixedcompact的完整tail/Green误差及growth费用

对实r，逐项max z^k e^(−z/2)≤(2k)^k，故安全显式界

    |η₀(r)|≤2^15e^(−πr²/2)。                              (3)

在 |Rew|≤A、|Imw|≤θ<π/4 的compact rectangle上，令

    c=(π/2)e^(−2A)cos(2θ)>0，Cθ=2^15 cos(2θ)^(-4)。

Gaussian绝对值及polynomial吸收给 |η₀(ne^w)|≤Cθ e^(−c n²)。
因为(n₀+j)²≥n₀²+(2n₀+1)j，n₀=R+1，实际trace-class尾有

    T_R:=2Σ_(n>R)|η₀(ne^w)|
       ≤2Cθ e^(−c(R+1)²)/[1−e^(−c(2R+3))]。               (4)

同理每个先固定w导数阶j有C_(j,θ)代替Cθ；compact C∞/trace-norm逼近已付。
不是all growth/A的uniform常数。

在 |z|≤Z、R足够使Z Cθe^(−c(R+1)²)≤1/2时，tail product有一个从z0固定的
无零log branch。记 F∞ 为406无限标准乘积，则

    |log(F∞/F_R)|≤2ZT_R，
    |∂_z log(F∞/F_R)|≤2T_R。                               (5)

所以Green差 −log|F∞|²+log|F_R|² 为同一smooth tail，绝对值≤4ZT_R。
在finiteR零点处两边共有相同singularity，(5)按可消去的ratio理解；不强迫Green分量为0。
这是actual标准族fixedcompact上的付费逼近，不是uniform adelic极限。

增长x-range的nuclear费用不能省掉：实x=−A、R≤e^A时，所有n∈[2e^A,3e^A]
都在tail。η₀在[2,3]严格正且有absolute lower c₀>0
（例如P≥20·12³、e^(−πr²)≥e^(−29)），A≥log4时整数个数≥e^A/2。
因而

    ||A_(η₀,−A)−A_(η₀,−A)^(R)||₁=T_R(−A)≥c₀e^A。          (6)

固定R在growth domain上不是小trace-class误差；至少需要R达到e^A量级后才可能付此absolute尾。
由(4)，对先固定θ/导数阶/权阶B，取足够constant乘
e^A sqrt((B+1)(A+1)+log(1/ε))的R即可使相应weighted compact error≤ε，0<ε≤1；
constants和各先固定阶数仍需保留。
这里A是406的logλ参数，不因记号相似就认作actual Weil support L。
允许signed/adaptive截断或别的norm是未排逃逸；(6)只针对这个真实nuclear截断。

## 3. 固定rank p_R：双矩保留，但全域拓扑与ζ因子未保留

令A₀(s)=∫₀^∞η₀(r)r^(s−1)dr。405 Gaussian计算精确给

    A₀(s)=s²(s−1)²π^(−s/2)Γ(s/2)/8，Re s>−2，
    M_(p_R)(s)=2H_R(s)A₀(s)，H_R(s)=Σ_(n≤R)n^(−s)。          (7)

finite求和允许合法Fubini，A₀(0)=A₀(1)=0，因此

    c(p_R)=0，d(p_R)=0，ALL R。                             (8)

不能误称有限截断必丢这两个矩。但p_R在x→−∞有

    p_R(x)=−18π[R(R+1)(2R+1)/6]e^(2x)+O_R(e^(4x))。          (9)

无限p由Poisson双源条件在两端super-exponential衰减；故任意有限R，p_R不在S_exp，
p−p_R的S_exp权阶N>2半范数为∞。fixedcompact逼近不能升级为405原Fréchet源逼近。
此外(7)没有ζ(s)因子；R1时H₁=1，A₀(ρ)对每个通常非trivialζ零点ρ都非零。
所以有限rank trace不能继承M_p(ρ)=0的实际像/root责任。
这不是把未知零点位置用于输入：只用ρ≠0,1及Γ无零的形式事实。
也不在(9)之外未经证明声明p_R在完整B/Q中的新符号。

## 4. 另一合法finiteη修复：真实源矩可以付，但不等于固定rank

选择固定实偶smooth cutoffχ，χ=1于|r|≤1、χ=0于|r|≥2。
先截源χ(r/R)η₀(r)，再修三个正半轴线性矩

    L₁(η)=∫η(r)dr，L₀(η)=∫η(r)dr/r，Llog(η)=∫η(r)logr dr。  (10)

η₀的三个值均为0：L₁=A₀(1)、L₀=A₀(0)、Llog=A₀′(1)。
取三个固定smooth bumps b₁,b₂,b₃，支撑分别近1、2、4，均远离0、正半轴积分为1，再偶延拓。
其三矩矩阵可选invertible：point-mass极限的列为(1,1/a,log a)，a=1,2,4，
det=−(log2)/4≠0；窄smooth bumps依连续性保持invertible，不用δ分布当源。
设矩阵为M，c_R=M^(-1)(L₁,L₀,Llog)(χη₀)，定义

    η^[R]=χ(r/R)η₀(r)−Σ_(j=1)^3(c_R)_j b_j(r)。              (11)

原三个矩0及Gaussian尾给c_R=O_b(poly(R)e^(−cR²))；所有先固定Schwartz半范数
η^[R]−η₀也同样小。η^[R](0)=0、L₁=0，是真实S_even,0源，而非形式标签。
由405已付E连续性，Eη^[R]→p在各先固定S_exp半范数成立；
M_(Eη^[R])=2ζ(s)A_(η^[R])(s)，L₀=0、A′(1)=Llog=0再给目标c=d=0。
因此这条修复确实保实际像及双矩，不被(9)排除。

费用/类别必须分开：η^[R]是非零smooth compact source，其支持在|r|≤max(2R,5)。
每个real λ的Fredholm fibre只有n≤max(2R,5)/λ项，所以是finite polynomial；
其z-degree随x约为O(R e^(−x))，不是固定2R family degree。
非零compact源不能作为r的全纯函数（identity theorem）；因此该cutoff不再给406的
holomorphic w-strip Fredholm族，只给real-x smooth family。
它可以作为真实adelic Schwartz源，但不能免费升级成two-variable analytic Cartier或number-field模型。
允许不同analytic/relative/weighted修复仍在；本稿没有称全部finiteη方案不可能。

## 5. finite divisor次数、规范读出与degree normalization

在固定generic realx上，F_R是C[z]多项式degree2R。其P¹_C rational divisor是

    div(F_R)=D_R^+−2R[∞]，
    D_R^+=Σ_(n≤R)2[1/η₀(ne^x)]，deg D_R^+=2R。              (12)

有效零部分是O(2R)；完整principal divisor是degree0。
把D_R^+作为primitive而不支付degree correction不合法；subtract2R∞使它principal。
degree normalization ­D_R^+/(2R)给Q-linebundle的degree1，但标准inverse-zero readout也随之变为

    R_z(D_R^+/(2R))=p_R(x)/(2R)→0，fixedx。                  (13)

要保原trace必须再乘2R；若消费bilinear intersection/energy，尺度平方也要相应支付，
不能一边用degree1预算一边用未缩放trace配对。
对λ=2，η₀(2n)→0、零点α_n→∞，所以normalized零点概率measure
(1/R)Σδ_(α_n)弱收敛δ∞。完整(12)/(2R)因而弱趋0。
这个合法normalization确实避免字面无限有效次数，却会压掉这项固定坐标source读出；
nonliteral Green/weighted normalization若保剩余数据须另交费用，不由(13)排除。

## 6. 一个finite、可定位的number-field fixed-coordinate反检验

即使R1也不能免费声称F_R对全部actual idele参数都是K-polynomial。
η₀(r)>0且在r≥2严格递减：令z=πr²≥4π>12，
P′−P=−4z⁴+44z³−125z²+91z−9<0。
取τ=π·10^(-100)，η₀(2)>1/100>τ，而η₀(20)<10^(-300)<τ，
所以有唯一可由monotone bisection定义的λ*∈(2,20)，η₀(λ*)=τ。
这些界由12<4π<13、1200<400π<1300和(3)等elementary bounds支付。
它是固定真实η₀源的合法real idele参数，不按Q值构造。

    F₁(z,logλ*)=(1−τz)²。                                (14)

τ超越，故(14)在406固定z坐标下不是任何number-field K上的多项式，
其有限zero也不是P¹_K的algebraic closed point。此为finite actual family的具体fixed-coordinate miss。
但是改坐标z′=τz后有(1−z′)²这个Q-model；不能扩大成所有nonliteral模型不可能。
修复的source读出代价准确是∂_z=τ∂_(z′)、trace=2τ；
这一步是transcendental坐标变换，未作为K-morphism或全place规范付清。
允许真实archmetric携带τ数据仍是一条逃逸，尚未独立给actual全Weil比较。

## 7. principal/Green整体与任意holomorphicunit规范

已直接读本地Gillet–Soulé原PDF pp126–127（PDF35–36）：
§3.3.3–3.3.4使用整体principal pair (div f,−log|f|²)及其算术Chow商。
其f须是实际指定算术子簇的rational function；
arch Green分量非零并不妨碍整个principal pair在商中为0。
不能要求Green单独为0，也不能从smooth源unit推其已是算术rational function。
原件[链接](https://numdam.org/item/PMIHES_1990__72__93_0.pdf)本次web超时，
本地原PDF可读，采用上述原页定义，不以失败附件暂停来源门。

对finite (2)，arch analytic pair (div F_R,−log|F_R|²)是合法principal current。
若F_R真来自K-rational function、各place资料一致，它的完整principal算术类为0是正确结论，
不是把一个非零Green函数消掉的错误。局部analytic pair并不自行补finite-place metrics。

另一方面任意holomorphicunit代表自由仍有具体费用。
406的真实源unit给U_t(z,w)=exp(t z p(w))，t∈R arbitrary；定义

    F_R^t=U_t F_R，F_R^t(0,w)=1，div_zF_R^t=div_zF_R，
    −∂_z logF_R^t|_0=p_R(w)−t p(w)，
    G_R^t−G_R=−2t Re[zp(w)]。                             (15)

p(log2)>0，因为η₀(2n)>0对所有n。可具体取x₀=log2、z₀=2^(-16)，
由(3)所有finiteR factors在该点非零，即有
|G_R^t−G_R|(z₀,x₀)=2|t z₀p(x₀)|→∞。
所以degree2R、F(0)=1和固定zero divisor不足以给任意unit representative的uniform Green/readout fee。
这不是要求principal pair的Green为0；(15)是代表/metric变换的实际费用。
unit exp(tzp)通常不作为P¹_K的rational unit延拓，不能当已存在的adelicprincipal修复。
standard linear-pencil规范和完整divisor inverse-zero读出仍可排除这类自由，
代价是固定z坐标/范畴并另付全place归属；此合法逃逸不被(15)禁止。

## 8. actual source坐标与非根probe：不能混淆405的B和physicalQ

先仅在实S_exp源f上固定真实坐标

    r(u)=e^(u/2)f(u)，
    M_f(s)=∫r(u)e^((s−1/2)u)du，d(f)=A_+(r)，c(f)=A_−(r)。   (16)

sharp变为r的reflection。f*f^sharp=e^(−a/2)C_r(a)，C_r是实际autocorrelation。
用actualΓ₀=−γ−π/2−3log2−logπ及543jump核，可以逐项核

    qΓ(r)−2Σ_(n≥2)Λ(n)n^(-1/2)C_r(logn)=−2B(f,f)，
    Q_actual(r)=−2B(f,f)+2d(f)c(f)=T(f,f)。                 (17)

constant check使用2∫₀∞(e^(3a/2)−1)/(e^(2a)−1)da=π/2+3log2；
所有源super-exponential使properpower/pole/Γ项绝对合法，未删identity常数。
这是真实real源上的whole对象接合，不外推allcomplex、任意finite-L cut或新adelic交数。

因此p=Eη₀的physical r_p=e^(u/2)p确实Q=0；h虽B(h,h)=1/16，
也被其dc=1/16的完整pole补偿为Q=0。主类/root方向送0可以正确，不能拿它负证primitive存在。
旧537的nonzero compact r₀=(D²−1/4)ψ则Q(r₀)>0且A_±=0，
其405坐标f₀=e^(−u/2)r₀不属于I（若属于I，T=0将与(17)及旧正性矛盾）。
所以当前η₀/Fredholm principal方向没有覆盖这个已付actual非根probe。
本稿不因此否定其它source→geometry映射；只是必须实际构造覆盖和比较，不能按名字认同。

## 9. 最强旧净值、准确停门与未排修复

已付新的核算范围：fixedcompact有限tail/Green误差(4)/(5)，growth nuclear lower(6)，
finite rank的矩保留与源拓扑/ζ因子分离(7)–(9)，真实compact源的三矩修复(11)，
degree-normalized读出费(13)，finite fixed-coordinate field probe(14)，unit Green费(15)，
以及real actual坐标(16)/(17)。Gaussian/Fredholm/GS工具和405/406既有结果不登记新来源定理。

仍未付：canonical normal projective X/K、actual各place integrable metric与nef/big/primitive数据，
principal quotient后的非根范围、allcomplex源及growth norm、fullactualΓ/properpowers/dual poles
到同一交数的独立signed比较和误差；强旧543 wholecount/537 fixedwindow/550原费没有被改善。

当前 finite/truncated/analytic构造不自动变成algebraic/adelic构造；
principal整体正确不自动给非退化positive输入。旧literal∞scope不作为本稿停止理由。
允许标准规范、补全Green、allplace/nonliteral/relative/weighted修复均保留，
但无上述实际费用与input/test/net三句就不建立数学合同。
本来源按一次适配门入口0停止，不反造Qmetric，不以η₀零主类/已有定理结束宏观Goal。
下一动作由root统一登记；本子任务无待跑进程。
