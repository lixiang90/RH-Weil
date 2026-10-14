# MV来源门：真实合并质量、间隔账本止损与whole净门逆审

2026-10-14；只编辑本稿，不改STATE/cadence/Git、不重开C021、不建立C022。
按AGENTS恢复README/STATE/check/show、现行Goal/frontier、D20261014Y、
C021 G1/G2/root闭合与next-reciprocal-phase-source-location。
入口HEAD `36810d109e184787027656c31fb636e880036d7f`；实际树有root的
.gitattributes/.gitignore改动及c021-mv-source新目录，非clean。check/show结构通过。
同G20261014、固定0c4f3a3/≤538，C021 stopped、G1已付/G2 open，cadence仍1。
运行Goal/远程/后续进程须root现场盘点，本稿不将文件观察当运行工具证明。

## 1. 一级原页与来源真正提供的内容

使用PDF读审技能，实际查看缓存PDF的印刷页73、74；没有凭缺公式OCR补定理。
一级作者[Montgomery–Vaughan, Hilbert's Inequality (1974)](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)，
本地PDF为sources/mv-hilbert-1974.pdf，10页、538953 bytes，SHA256
`0dbcddf24bc41c65d1920c59aafe7fe85f13a7519b0edf9be9164c84d1cc6db4`。
元数据只确认版本；适配本对象仍须下列推导。

Thm1用于**distinct modulo 1**点：csc核的全局间隔费为δ⁻¹Σ|u|²，
局部版为(3/2)Σ|u_r|²/δ_r。Thm2用于**distinct real**点：

    |Σ′u_r overline(u_s)/(λ_r−λ_s)|≤πδ⁻¹Σ|u_r|²，
    local版≤(3π/2)Σ|u_r|²/δ_r。

Cor2(1.9)为∫₀ᵀ|Σa_r exp(iλ_rt)|²dt
=Σ|a_r|²(T+3πθ₂δ_r⁻¹)，|θ₂|≤1。
因此对unitcell内e(λv)=exp(2πiλv)，实线局部间隔给

    ∫₀¹|ΣA_λe(λv)|²dv≤Σ(1+3/(2δ_λ))|A_λ|²。       (MV)

均值投影是contraction，可据此上估ΣA_λ[e(λv)−I(λ)]。
这一步合法，但其发出账本仍含全部inverse-spacing权。
原MV及普通Dirichlet均值是旧工具，不因读出原页或新名字登记新input。

## 2. exact全源运输及合并：没有额外自由label质量

保C021新的Πᵃ，r=a_Nφ、norm²=N⁻¹/²||φ||²_dx；每cell ordinary mean0，
独立complex Fourier系数f_(j,m)，m≠0，全部strict q<N actual primepowers。
记e(z)=exp(2πiz)、I(λ)=∫₀¹e(λv)dv、h_λ=e(λv)−I(λ)。
完整detail adjoint H*=Σ_(q<N)Λ(q)/√q C_q*在child n上的精确式是

    (H*φ)_n(v)=Σ_λ A_(n,λ)(f) h_λ(v)，
    A_(n,λ)=e(λn)Σ_(q≤n, m/q=λ, q∤m) Λ(q)/q ·f_(floor(n/q),m)。 (1)

其中1≤n≤N−1，非法parent/缺失cell系数为零；q≤n与N截尾保实际完整children。
式(1)是实际同一源的所有q/child/频率系数，不是任意新label单位球。
必须先合并**相同real λ**。λ与λ+integer的child phase在整数n相同，
但v-profile不同，不能按mod1合并为同一个h_λ。
全profiles含m及m+q，故不合并直接套Thm1的distinct-mod1前件也失败；
real Thm2/Cor2是合法入口，仍须收费。

由于q全为primepowers，非整数λ的reduced denominator恰是p^b，b≥1。
其exactcollision只跨同一p的q=p^a、a≥b；不同base不可能有相同非整数λ。
用weighted Cauchy，

    |A_(n,λ)|²≤W_λ Σ_(a≥b) (logp/p^a)|f_(floor(n/p^a),λp^a)|²，
    W_λ≤Σ_(a≥b)logp/p^a≤2logp/p^b≤2logp/p。

对n、λ求和，每个(q,j,m)至多q个child，故有一个自含安全估计

    Σ_(n,λ)|A_(n,λ)|²
      ≤Σ_(p,a:p^a<N)2log²p/p ·||f||²
      ≤2logN Σ_(p<N)logp/p ·||f||²
      ≤4log²N||f||²。                                      (2)

最后只用旧factorial恒等式给Σ_(q≤N)Λ(q)/q≤2logN。
因此12log²N的安全版本亦成立。有限profiles先证、非负和/Tonelli再延拓到全部L²；
不引入共同profile、外加全1标签或源适应常数。
换回原du全式乘N⁻¹/²，量词ALL N/ALL independent complex source不变。

**裁定：(2)是真实actual coefficient方向的collision质量付款。**
它不同于549“unitlabel Gram小但全1质量M未付”的缺口：这里已经代入actual Λ(q)/q
和同一f，质量没有隐藏回标签空间。但频率函数h_λ的frame费用还没有付。
Σ|A|²小不能代替||ΣA h_λ||²小，更不能直接代替signed B_C的Γ-relative界。

## 3. 允许exactcollision合并后，原MV账本仍有合法反费族

本节只否定明确的**先对完整adjoint发出(MV) norm²账本**配方。
不把一个coarse上界当actual necessary，不否定direct signed或adaptive clustering。

令b≥1、s=9^b=3^(2b)，t为严格大于s的最小2-power。
s<t<2s，t−s≡7 mod8≥7，coprime且两者都是actual properpowers；
Λ(s)=log3、Λ(t)=log2，不能误用log s/log t。
取Bezout模式1≤m_s<s、m_t=(m_s t−1)/s，则

    m_s t−m_t s=1，0<m_t<t，1<m_t/m_s<2，
    λ_s=m_s/s，λ_t=m_t/t，λ_s−λ_t=1/(st)。          (3)

λ_s、λ_t的reduced denominators分别为s、t。
t-parent1的children[t,2t)与某个s-parent j（j=1或2即可）的children
[sj,s(j+1))有至少s/2个共同整数child：j1长度2s−t，j2长度min(s,2(t−s))，
二者最大至少2s/3。取N=4t，所有child/source和strict pp合法。

φ在parent j取m_s模式、在parent1取m_t模式，各系数1/√2，其余零。
若j=1，两模式不同且正交，仍||φ||²_dx=1，每cell mean0。
各λ可能来自更高同base power时要求mode乘3^h或2^h；(3)的mode比在(1,2)，
源只有上述两个模式，因此这些目标λ无其他source collision可抵消。
对每个共同child，exactcoalesced A中的这两项各恰有模
(log3)/(√2 s)、(log2)/(√2 t)。其他频率只会让局部间隔更小。
δ_(n,λ_s)、δ_(n,λ_t)≤1/(st)，故(MV)发出的正账本满足

    L_MV(f):=Σ_(n,λ)(1+3/(2δ_(n,λ)))|A_(n,λ)|²
       ≥(3/8)log²3 ·s。                                  (4)

原du单位源为ρ=√xφ，即原φ坐标额外乘N^1/4；共同norm因子恰抵消，(4)不变。
ρ的support在x<4，BV≤Ct。平移u=logx−L不改actualΓ能量；
Fourier上低区|ξ|≤t²用Γ≤C logt，高区用BV/|ξ|尾，得

    ||ρ||²_du=1，ρ∈R_a∩Dlog，JΓ(ρ)≤C logt。                (5)

因此L_MV不能在ALL N下被A JΓ+C log^pN控制，无论固定有限A,C,p为何。
这是原来源配方发出的账本lower，而不是实际H* norm²或B_C lower。
两模式同时改成m_s+s、m_t+t时，频率同加1、(3)行列式不变、mode比仍(1,2)，
无collision结论与(4)/(5)保留。此variant的λ∈(1,2)，故不能仅以low-λ的h_λ小修复原账本。

相反，该源actual B_C本身仍O(1)：support x<4，仅q2、3有actual forward overlap，
其余q在同源quadratic pair为零。Γ价格也真实付清，所以本族**不是G2反例**，
更不是whole Q负性证据。近λ的native h-Gram有界而非inverse-gap爆炸；
spacing账本失效留下directGram/nearcluster/联合signed逃逸。

## 4. 来源成功、失败、unknown与最强旧净审

成功范围：(1)准确运输全部q/cell/child/frequency，(2)支付real exactcollision后的
actual coefficient质量，原页常数/域已核。来源阶段有可保存的准入信息。

失败范围：Cor2(1.9)逐child unclustered inverse-spacing正账本，即使exactcollision
先合并，仍不能与同源Γ加任何fixed polylog norm费接合。Thm1直接套全profiles还有
distinct-mod1对象错配。结论不扩大成“所有MV应用失败”或“所有carry必有线性费用”。

unknown范围：native mean-zero frame、跨q/commonchild与Γ相对的真正signed费用；
adaptive近频簇或不同全joint运输尚无已核费用/合法核心反例。G2仍open，C021不重开。

最强旧比较保持016 exact graph/profile、028负迹与core density、543 cofinal exp(S_N)
及550 frozen topband actualII O(1)。式(2)只是系数质量；式(4)只停止来源配方，
两者都不产生新的whole count/PSD/Ξ。550的O(1)只fixed physical band，不覆盖全部R_a；
但本反费源亦不能据其合法全Dlog身份冒充wholecore强制后果。

若另付真正ALL N/ALL R_a的B_C≤δJΓ+C log^pN、δ<1及全部误差，
G1/occupation/finitecodim/028才给N−1+C logN exp(C log^pN)，
任何固定p都沿543同records严格胜exp(c√N)。目前这个箭头没有付款。
旧539/541已经说明一些免费/绝对包络不能支付Γ，但没有代替本actual reciprocal-phase
coalescence和合法issued-ledger配对。新增的是**此旧定理来源适配的准确止损信息**，
不是重复自由norm反例，也不是新宏观forcing或Goal第3门方法类完成。

## 5. 下一现实备选的准入边界

不再选择另一paper标签。最接近当前实际对象的修复是原始mean-subtracted joint Gram：

    G_h(λ,μ)=I(λ−μ)−I(λ)overline(I(μ))，
    〈C_q*e_(j,m),C_q′*e_(j′,m′)〉
       =(qq′)^−1/2 G_h(λ,μ)
          ·Σ_(n∈[qj,qj+q)∩[q′j′,q′j′+q′)∩[1,N)) e(n(λ−μ))。 (6)

它保native finite geometric相位及全部child截尾，exactcollision/nearcollision连续合法，
不能把它换成Σ1/|λ−μ|。式(2)/(6)是已知可核输入；(6)只是恒等式，
**不是已经存在的全域signed估计**。本次没有找到能据此完成core费用的独立known定理。

一个更强、可充分消费的候选是ALL N/fullcomplex的

    ||H*φ||²_dx≤AΣ_(j,m)log(2+|m|)|f_(j,m)|²
                    +C log^pN||φ||²_dx。                    (7)

如果(7)独立成立，Young取小参数、用G1可付G2和严格wholecount。
但是(2)/(6)尚不证明(7)，它仍是未付frame命题，不能把其式子本身当input。
本节没有核到一个已知独立fulljoint定理可免费支付它，故不据(7)建立C022。

唯一可执行的来源审查动作是先冻结(7)最便宜的actual necessary响应门：
φ只在parent1取单位模式m≠0，但保完整q和全部signed cross。精确输出为

    F_(N,m)(n,v)=Σ_(n/2<q≤n, q<N, q∤m) Λ(q)/q
                      ·e(mn/q)[e(mv/q)−I(m/q)]，
    R_N(m)=Σ_(1≤n<N)∫₀¹|F_(N,m)(n,v)|²dv。                 (8)

原du单位源ρ=√xφ有JΓ(ρ)=log(2+|m|)+O(1)，uniform N。
下一原件/推导只针对(8)真实reciprocal-phase响应的联合费用，
尤其m∈[N,2N]的成长带（Γ为OlogN）：给uniform polylog收费或合法超polylog反族。
这保全部properpowers/commonchild/phase，不能再用MV inverse-gap账本或丢cross代替。
只fixedm、旧finiteband 48sqrtK、更多普通矩阵或某个upper未通过都入口停止。
成功仅是必要source门，仍须(7)的全profile混合才能晋级；失败只排该强adjoint配方，
不反direct B_C的较弱joint门。它不作为另一个薄positive类持续主攻。

之后现实source/test/net三句应明确如下，未齐则只保存来源审查，不建数学合同：

1. 输入必须是在(6)实际coefficient方向上新证明的共同子块/相位收费，或一个不同独立
   算术/几何定理，含全成长参数与原域；“native Gram正”或(2)本身不能再充当whole input。
2. 新joint输入须保(3)近频族、(8)actual必要门及fullprofile/全q；
   给出的实际block lemma或来源定理和其适用量词必须先落原证明，不能把最终G2当已知前件。
3. 净门必须关闭上述fullcarry箭头并得严格超543的whole预算，或给允许这些合法cluster/joint
   修复后仍成立的实质核心必要费。只修复本两模式、只fixedm或再付O(1)topband不足准入。

另一现实方向是完整physical row的ΛΛ/实际全1/allheight相关输入；
GY/AP混合槽及旧sieve O(1)已经消费，必须确实新增该槽的联合费用才有资格。
目前两方向均无本稿已核的独立wholecore来源；如实保留缺失，不用未知domination改名填空。
本轮来源入口按原规则零数学轮收口；root负责最终策略、STATE与唯一cadence。
