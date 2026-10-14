# MV 来源门：实际倒数相位、完整碰撞系数与局部间隔账本

2026-10-14；C021 保持 stopped/入口0，本稿仅来源审查，不编辑 STATE/cadence/Git/合同。
按 AGENTS 恢复 README/STATE、check/show、同 G20261014 Goal/frontier、C021、
D20261014Y、原 G2 审和 next-reciprocal-phase-source-location。
现场 HEAD=36810d109e184787027656c31fb636e880036d7f；root 的 Git属性/ignore与本来源目录
有进行中改动，非本稿编辑；子 get_goal=null 不代 root 的 active 实例。
固定基线0c4f3a3/≤538，唯一 cadence 不动；结构 check 不认证数学。

**裁定：** 原 MV real-spacing mean-square 可以形式合法接入实际矩阵；
全部 real exact collisions 合并后的真实系数质量可付 O(log²N)。
但 native 逐 child/local-gap 正账本不能由 actual Γ加任意固定polylogN支付：
下面给完整 proper-power、同源、合法原域的显式族，账本下界线性，而 Γ价仅对数。
这只否定这个未经 cluster 修复的来源运输，不是 actual carry 能量或 G2 的必要费。
direct centred-Gram、near-cluster、保接收源支撑的 signed 配对等逃逸仍在；不以此重开合同。

## 1. 原对象和每个 actual child 的精确系数

ALL整数 N≥4、L=logN/2、x=e^(u+L)∈(1,N)，原du=dx/x。
新 Π^a 的 r=a_Nφ、a_N=N^(-1/4)sqrtx，原 norm 精确为

    ||r||²=N^(-1/2)||φ||²_(dx)，
    R_a iff ∫_j^(j+1)φ dx=0，j=1,…,N−1。                    (1)

不是547旧 weighted-mean R；φ_j(v)=Σ_(m≠0)f_(j,m)e^(2πimv) 的各 cell/profile
全 independent complex。actual U_qφ=sqrtq φ(qx)，D_q=P_(q|m)U_q、C_q=(I−P_q)U_q。
保 strict q<N 和全部 actual Λ(p^a)=logp，不将 proper powers 权换成 log(p^a)。

detail adjoint C_q^*=R_flat U_q^*(I−P_q)，U_q^*φ(y)=q^(-1/2)φ(y/q)1_(q,N)(y)。
对 child n=1,…,N−1，只有 q≤n 才有 parent j=floor(n/q)≥1；令 s=n−qj∈{0,…,q−1}。
原完整 weighted arithmetic adjoint K_C^*φ=Σ_(q<N)Λ(q)/sqrtq C_q^*φ 的 child profile 为

    (K_C^*φ)_n(v)=Σ_(2≤q≤n) Σ_(m≠0,q∤m) z_(n;q,m) h_(m/q)(v)，
    h_λ(v)=e^(2πiλv)−I(λ)，I(λ)=∫_0^1e^(2πiλv)dv，
    z_(n;q,m)=Λ(q)/q ·f_(floor(n/q),m)e^(2πim s/q)
             =Λ(q)/q ·f_(floor(n/q),m)e^(2πin(m/q))。         (2)

最后一个 equality 用 m,j 都为整数，不丢 parent phase。
N整数保证每个保留 child 的 v 是完整(0,1)，其余 child按 zeroextension 为0；
没有未付 fractional child尾部。j小/大、正负m、所有properpowers都在(2)。

内积对第一变量线性，原 full signed quadratic 是

    B_C(r)=2N^(-1/2)Re〈φ,K_C^*φ〉。                          (3)

(2) 的 norm upper 不能替代 (3) 的同源 signed 费用或 full zeroextension Γ。

## 2. ALL real exact collisions：唯一 reduced prime-power 分母

actual λ=m/q 全在 Q\Z；m≠0且q∤m，不能引入任意独立 irrational phase标签。
写 q=p^a、λ=c/p^e 为最简分数，其中

    1≤e≤a，c∈Z\{0}，p∤c，m=c p^(a−e)。                    (4)

两个 actual 标签的 real collision 是 m q'=m' q。
非整数最简分母唯一，因此 cross-prime p≠p' **没有 real exact collision**。
same-prime 不同 a 可以碰撞，且(4)列出全部这样的碰撞，不限 fixed m。
合并后的真实系数精确为

    β_(n;p,e,c)
      =e^(2πin c/p^e) logp
         Σ_(e≤a≤floor(log_p n)) p^(-a)
                 f_(floor(n/p^a), c p^(a−e))。               (5)

coherent cross 不能从 diagonal删除。若把各 issued z 当自由系数，|Σz|²/Σ|z|²
可达到 collision multiplicity；但这些 z 受 Λ/q、parent label 和 child重复约束。
下节直接支付原 flat parent 质量，不假设实际系数是某个单位 flat-label 方向。

## 3. 合并后的全部 cell 系数质量：原 parent 质量有 log²N 界

先有限 Fourier和，再用非负 Parseval质量极限进入全部 L² profiles。
令 A=floor(log_p n)，W_(p,e,n)=logp Σ_(a=e)^A p^(-a)，则

    W_(p,e,n)≤logp/[p^e(1−1/p)]，
    |β_(n;p,e,c)|²
       ≤W_(p,e,n)Σ_(a=e)^A logp·p^(-a)
                       |f_(floor(n/p^a),c p^(a−e))|²。        (6)

这是 weighted Cauchy，保所有 phases/complex coefficients，不把碰撞设为独立。
固定原 input label (j,m)，令 b=v_p(|m|)。在 q=p^a 的 nondiv部分必有 a>b，
e=a−b、c=m/p^b；它在 n=p^a j+s 的至多 p^a 个实际 children 中重复。
故 (6) 的全部 n/e/c/a 费用对这个 input 至多

    Σ_(a>b,p^a<N) (logp)²/[p^(a−b)(1−1/p)]
       ≤p(logp)²/(p−1)²。                                   (7)

这里 p^a children 的质量已经支付，不能后续再把所有 child当另一个免费单位球。
对全部 primes与原 labels求和，得到

    Σ_(n=1)^(N−1) Σ_(λ actual distinct real)|β_(n,λ)|²
       ≤[Σ_(p<N) p(logp)²/(p−1)²] Σ_(j,m≠0)|f_(j,m)|²
       ≤12 log²N ||φ||²_(dx)。                              (8)

末步用 p/(p−1)²≤4/p、logp≤logN，及546已付自含 Mertens
Σ_(q<N)Λ(q)/q≤3logN（ALL N≥4）；没有RH/未知零点前件。
(8) 是 full parent→merged-child-label mass，实际方向由(5)给定，非换 weighted norm。
未合并的 issued 系数也有粗界≤3log²N||φ||²；这两条并不宣称每个单collision
的 merged质量≤常数倍其 issued质量，亦不预付 distinct λ 的 frame能量。

原du消费只乘同一 N^(-1/2)。因此 exact collisions 本身的母质量已有可核控制；
但 (8) 尚无 actual h_λ Gram或 local-spacing权，不能由它直接得 G2。

## 4. mod1 collision 与 near collision：不能代换实际连续 Gram

λ−μ∈Z 的 exact mod1 collision，最简 fractional分母仍唯一：
同 prime p、同 reduced exponent e、numerators c≡c' mod p^e。
不同 prime分母不可能有非整数的 mod1 exact collision。
一个 mod1类含 λ=t+r/p^e 的所有 integer lifts，p∤r；它们在连续 unitcell中仍是
不同 real modes，不能合并成一个 β，也不能免费丢掉 lift 的 m频率/Γ价。

实际 centred Gram（linear-first）为

    〈h_λ,h_μ〉=I(λ−μ)−I(λ)overline(I(μ))。                 (9)

realλ相同时这是1−|I(λ)|²；若 λ−μ为非零整数，则第一项为0，
而非相同profile。MV模1 csc定理不是(9)的算子；使用它必须另付准确的kernel运输。
本题正确的直接mean-square接口是 distinct real λ 的原Corollary2。

同 prime、不同 reduced分母的非零 real距离≥p^(-max(e,e'))，同分母距离≥p^(-e)。
cross-prime λ=c/p^e、μ=d/ℓ^f 则

    λ−μ=(cℓ^f−dp^e)/(p^eℓ^f)，非零距离≥1/(p^eℓ^f)。          (10)

Bezout可达到这个尺度；properpowers不能按仅primes spacing消费。
对 fixed N 的全部 m 合并后，real-spacing至少 (N−1)^(-2)，所以 weighted无限域
可合法进入 MV，但 source-blind global upper失 N²，不是必要损失。
只fixedm估计、只mod1去重或用所有可能λ的全局最小值，都没有支付成长全joint。

## 5. 原 MV 接口和 native positive certificate 的定义

一级[Montgomery–Vaughan 原PDF](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)，
JLMS(2)8(1974),73–82，§1 Theorem2/Corollary2；关键原页视觉/无限域/常数另见
[独立原件审查](primary-hilbert-formulas-and-domain-audit.md)。旧MV工具不登记新输入。
cycles λ 换 angular2πλ，unitinterval Cor2(1.9) upper为

    ||Σ_λ β_λ h_λ||²≤Σ_λ[1+(3/2)/d_λ]|β_λ|²，
    d_λ=inf_(μ≠λ)|λ−μ|。                                  (11)

先 real碰撞合并，再使用(11)；mean subtraction只降norm，原常数3π/(2π)=3/2。
finite support可以用自身local spacing；无限集需相同weightedℓ²质量有限。
对全actual矩阵定义其 **native issued positive certificate**

    M_N(φ)=Σ_n Σ_(λ:β_(n,λ)≠0)[1+(3/2)/d_(n,λ)]|β_(n,λ)|²， (12)

单频cell直接按norm处理，不对空spacing集合赋值。
(12) 是一种实际mean-square upper账本，不等于 ||K_C^*φ||²，更不等于 B_C。
接下来反驳的是欲以 actualΓ+固定polylogN控制此未经cluster修复的(12)的运输。

## 6. 显式合法 proper-power 族：局部 gap账本线性，而原Γ仅对数

取 integer b≥1，s=3^(2b)=9^b，t=2^ceil(log_2 s)，于是

    s<t<2s，s≡1 mod8，t≡0 mod8，t−s≥7，N=4t。                (13)

s/t是 actual properpowers；Λ(s)=log3、Λ(t)=log2，不是log s/log t。
由coprime s,t选唯一1≤m_s<s、1≤m_t<t使

    m_s t−m_t s=1。

存在性由 t在mod s的逆元；m_t=(m_s t−1)/s 正整数、<t。
(13)给 m_s(t−s)>1，因此

    1<m_t/m_s<t/s<2。                                      (14)

为避开smallλ/mean suppression的无关讨论，直接升一个 integer lift：

    M_s=m_s+s，M_t=m_t+t，
    λ_s=M_s/s∈(1,2)，λ_t=M_t/t∈(1,2)，
    λ_s−λ_t=1/(st)，1<M_t/M_s<2。                           (15)

det/gcd不变，3∤M_s、2∤M_t。因此它们的 reduced分母为s和t。
两输入mode的比值严格在(1,2)，不能是2^h或3^h，h∈Z。
故对全部 actual q<N，λ_s只能由(q,m)=(s,M_s)发出，
λ_t只能由(t,M_t)发出：同base其它指数不能collision，cross-prime也不能。
选定两系数在real精确合并后仍唯一，其他properpower标签不能抵消它们。

large parent1 的 child interval (t,2t) 与 small s-grid 的某个
(js,(j+1)s)、j∈{1,2,3} 有至少 s/2长度的完整child重叠。
证明：该大区间在(s,4s)中；若跨三个small格则含一个完整s格，
若至多两个则某格交长≥t/2>s/2。端点全整数，所以至少s/2个 actual完整children。
它们均在(1,N)，不借截尾扩大。

定义同一个 flat单位源，只取两个母label

    f_(j,M_s)=1/sqrt2，f_(1,M_t)=1/sqrt2，其余0。              (16)

若j=1，M_s≠M_t，仍是两个正交integer模式；每cell mean0且 ||φ||²=1。
取原du单位源 ρ=N^(1/4)a_Nφ=sqrtx φ。支持x≤4，是finite BV、full zeroextension
Dlog/actualΓ operator-domain 源，ALL b合法。
其真正 flat input 是 N^(1/4)φ；原du归一化后的certificate恰为
N^(-1/2)M_N(N^(1/4)φ)=M_N(φ)。下面(18)与(19)比较的正是同一原du单位源，
不是把flat单位质量和du单位质量混用。

在每个 commonchild n 上，合并后的选定系数严格为

    β_(n,λ_s)=(log3)/(s sqrt2)e^(2πinλ_s)，
    β_(n,λ_t)=(log2)/(t sqrt2)e^(2πinλ_t)。                   (17)

有两distinct实频，所以无论额外issued frequencies如何，
d_(n,λ_s),d_(n,λ_t)≤1/(st)。按(12)的正项，

    M_N(φ)≥(3/2)(s/2)st[(log3)²/(2s²)+(log2)²/(2t²)]
             ≥c s，absolute c>0。                           (18)

这是真正 local spacing（不是盲目global最小值）、真实coef和完整children质量的
**certificate下界**。更小的localgap只会增加该native upper账本。
同parent coefficient在O(s)个actual child中重复，不能消费单child O(1)费用后忘掉此质量。

实际Γ价格与这个源的m共同核算：M_s≤2s、M_t≤2t，支持x∈(1,4)，
原u只是一个fixed-length compact源的平移，norm1。
全部pieces的phase derivative2πM x在[c t,C t]中；非驻相分部积分（含jumps）给
低|ξ|≤ct Fourier质量O(1/t)、高|ξ|≥Ct log尾O(logt/t)。
543实际 Φ(ξ)=Γ(ξ)−Γ(0)=log(e+|ξ|)+O(1)、Parseval因此给

    JΓ(ρ)=logt+O(1)≤C logt。                                (19)

这里保持fullzeroextension Γ=actual2θ′及2π，未用periodiccell energy代Γ。
同源下(18)不可能由 δJΓ(ρ)+C_δlog^pN 支付，任何先固定有限p均如此。
升lift使λ∈(1,2)，故简单再乘 min(1,λ²) 的lowλ修复也不能救这个 native账本。

## 7. 准确未排逃逸：这个账本反例不是G2反例

对近频率 λ,μ，mean projection是contraction，所以

    ||h_λ−h_μ||₂≤||e^(2πiλv)−e^(2πiμv)||₂≤(2π/sqrt3)|λ−μ|。 (20)

只看(17)两个实际term，direct centred-Gram/norm bound 给每child的energy≤C/s²，
全部commonchildren仅O(1/s)，而不是(18)的Ω(s)。它们是一个实际 nearcluster；
带coherent系数的cluster合并、direct hGram或其他joint方法没有被排除。
mod1合并integer lifts仍不合法，但同一近cluster的真实连续Gram可以另核。

更直接地，(16)原φ只支持x≤4，actual forward pairing只有q=2,3可能有overlap；
所有q≥4在(3)的同源receiver上严格为0。故这个合法族的实际 B_C(ρ)=O(1)，
而native adjoint输出把费用发到远child，receiver那里为0。
保receiver支撑/局部Cauchy也是现实逃逸。不能由(18)反向推actualnorm/actualpair lower。

因此本稿的严格负结论只适用于：逐child先realcollision合并，随后不作nearcluster或
同源receiver修复，直接将Cor2 local-gap的正右侧(12)拿作Γ+固定polylog预算。
允许适应cluster、signed重组、改变权或直接Gram后，此负结论没有覆盖它们。
这是source准入所需的运输诊断，不承担完整G2方法类责任，不达到宏观Goal边界门。

## 8. 消费记录、停止与最小open项

已付：exact全q/child/complex系数(2)，全real/mod1碰撞分类，母质量(8)，
MV合法前件/2π转换，以及一个true local-gap certificate损失族和同源actualΓ价。
这些组织/旧工具/具体运输核算只属于当前唯一source审查；不结算新数学轮。

未付：近cluster合并后的全frame/multi-q/common-child/signed运输，
相对同一源actualΓ的fullG2，条件wholecount、成长核心/allheight与ζ/Ξ后果。
(8)不自动支付spacing；(18)不自动支付actual必要费；(19)不外推任意profiles。

本来源若仅消费native MV spacing，入口0止损；保其原定理与合法cluster/joint逃逸。
没有超强旧且关闭核心箭头的新transport，不能形成input/gate/net三句准入、
不建立新合同、不重开C021预算、不把本稿升级成Goal完成。
下一行动只由root据当前战略唯一登记，本子任务无待跑进程。
