# C006：晚素数actual Sonin增量的endpoint来源审查

2026-10-14；恢复AGENTS/README/STATE、check/show、C006、D20261014A及532。
仅写本独立审查，不改STATE/cadence，不独立计研究轮。
重大结论须父任务与不同组织逆审核后消费。

## 对象及原件

沿531–532，P是真实实位Sonin cutoff1，physical空间为`L²((0,∞),dx)`，F核`2cos(2πxy)`；在unitary log表示源scaling为平移。晚素数`p≥3,a=logp,q=p^(-1/2),U=U_a,B=I−qU`，

    Pp=B P G^(-1)P B*, G=(1+q²)P−q C,
    C=P(U+U*)P|RanP.

源`g`取原冻结两patch/矩零域；它的自相关支持跨度小于log3。因此每个晚p的actual primepower贡献严格0；以下`Tp−T∞`确为actual overlap增量。

一级接口为[CCM2310.18423v2 (57)–(59), Theorem4.6](https://arxiv.org/html/2310.18423v2)及实位Connes–Consani2021正迹，版本/原字节见既有receipt。端点投影原件为[Burnol math/0208121v1](https://arxiv.org/pdf/math/0208121v1)的Lemma2、Theorem4、Theorem8/9，实际核读范围和hash见C005 trace-source-audit。本审查使用真实实位two-cutoff resolvent重新推p→∞，不把Burnol的原文移称晚素数定理。

## 候选结论及准确拓扑

下文给出可供逆审核的完整组织。对每个**固定**`g∈Cc∞(U)`，候选为

    Tp(g)−T∞(g)=p^(-2) A_U(g)+O_g(p^(-5/2)),
    A_U(g)=1/(2π²)∫|ĝ(s)|² |κ_s−β_s|² ds,
    κ_s=k_s(1+), β_s=(Fk_s)(1+)=γ_s conj(κ_s), |γ_s|=1.

`k_s`是532的裸unitary Mellin求值向量；不能换为Gamma-completed evaluator。κ、β是actual cutoff外侧jump值。本首项是正平方，保留q项、q²return terms及全部真实Gram逆；不以粗O(q)的相对Gamma界冒充它。

可独立核的leading form满足`A_U=π^(-2)I+compact_U`，并有`0<c_U I≤A_U≤C_U I`。但是`O_g`余项依赖固定源的高阶seminorm；本审查**不**将其升级为全部L²源共同的`O(p^(-5/2))`operator norm预算，更不消费成长S中的真实增量。

## 1. 实际裸Mellin evaluator的端点及统一域

记L为physical低区间(0,1)投影，H=I−L，`K=LFL`，`R=(I−K²)^(-1)`。原实位K compact norm<1，故R bounded。实际投影

    P=H−H F L R L F H.

`R−I=K R K`有smooth、cosine-even核J。写`k_t=K(t,·)`，则`J(t,u)=<k_t,Rk_u>`；所有Cm bounds由fixed bounded R和smooth cosine rows直接成立，不需要交换prolate无限系数。

令裸power `e_s(x)=x^(-1/2+is)/√(2π)`，`F e_s=γ_s e_(-s)`（distribution意义）。低forcing

    r_s=L F H e_s=γ_s L e_(-s)−L F L e_s,
    v_s=r_s+R K²r_s.

r_s为L¹且L¹范数统一于实s；虽然它通常不是L²，`K²r_s`是smooth L²，因此第二项合法。真实求值向量外部表达为

    k_s=H[e_s−F L v_s].

可从532有限L²截断求值取极限核对，不对全域power直接应用bounded P。由`F H`及homogeneous Fourier身份消掉power，余下只由x=1的boundary forcing产生大x tail；低端0的odd derivatives为0（cosine-even smooth remainder）。因此

    k_s(x)=−β_s sin(2πx)/(πx)+d_s cos(2πx)/x²
                         +O_s(x^(-3)), x≥1,
    Fk_s(x)=−κ_s sin(2πx)/(πx)+d'_s cos(2πx)/x²
                         +O_s(x^(-3)).

这里余项常数及所需导数界至多是`(1+|s|)^M`；来自外部Mellin power分部积分的导数，smooth J项则统一。更高阶同样成立。**仅写O_s(x^-2)不能确定下文p^-3/2的系数**；第二oscillatory cos项及第三阶余项必须保留。

端点β_s=v_s(1+)及κ_s=e_s(1)−F L v_s(1)统一bounded。对任意smooth h，

    ∫_0^1 x^(-1/2+is)h(x)dx=O_h((1+|s|)^(-1))

由weighted Mellin分部积分成立；K²r_s及其Cm范数也O(1/|s|)。所以

    κ_s=1/√(2π)+O(1/|s|),
    β_s=γ_s/√(2π)+O(1/|s|).

P、F、Mellin的实结构还给`Fk_s=γ_s conj(k_s)`，因此|β|=|κ|。所有这些是actual boundary evaluator，未使用ζ零点。

## 2. actual q首阶及q²return费用

对固定s，support k_s及Fk_s均在x≥1。由上节tail、分部积分及actual prime整数`cos(2πp)=1`，

    Re<k_s,U_a k_s>
       =−p^(-3/2) Re(β_s conjκ_s)/(2π²)+O_s(p^(-5/2)),
    M1(s):=<k_s,Ck_s>
       =−p^(-3/2) Re(β_s conjκ_s)/π²+O_s(p^(-5/2)).

例如变x=pz后，leading积分是`p^(-1/2)∫_1∞sin(2πpz)conj(k_s(z))/z dz`；其endpoint等于`conjκ_s/(2πp)`。第二cos项另付一次非驻相，第三阶余项绝对可积。错误地将prime整数位置换为任意实p，会在首项留`cos(2πp)`。

两个return norm须实际投影后计算。对U_a k_s，令

    t=H U_(-a)Fk_s, r=L U_(-a)Fk_s.

因为U_a k_s lowcut严格0，`Kr=−L F t`。t的high tail范数为

    ||t||²=∫_p∞|Fk_s(x)|²dx
          =|κ_s|²/(2π²p)+O_s(p^(-2)).

其低Fourier泄漏`||L F t||=O_s(p^(-3/2))`：频率p±x在低cut x∈(0,1)远离0。精确正交化给

    ||P U_a k_s||²=||t||²−||R^(1/2)K r||²
                  =|κ_s|²/(2π²p)+O_s(p^(-2)).

对U_(-a)k_s，先取`t'=H U_(-a)k_s`，P消掉low part；同理

    ||P U_(-a)k_s||²=|β_s|²/(2π²p)+O_s(p^(-2)).

cross没有删除。`P U_a k_s`与`H F t`的norm差O_s(p^-3/2)，`P U_(-a)k_s`与t'同精度。将x分为x≤p/2和x>p/2：前区√p F t点值O_s(1/p)，后区√p t'的L² tail O_s(p^-1/2)。故

    |<P U_a k_s,P U_(-a)k_s>|=O_s(p^(-3/2)),
    M2(s):=<k_s,C²k_s>=||Ck_s||²
          =|κ_s|²/(π²p)+O_s(p^(-3/2)).

其leading两项相加是正费用；它与qM1联合，而不是作为未解释的q²mass项。

## 3. 全部Gram逆及裸mass的精确抵消

设`r=q/(1+q²),c(s)=cos(as),ρ∞=||k_s||²`。actual密度严格为

    ρp=(1−2r c) Σ_(j≥0) r^j Mj,
    M0=ρ∞, Mj=<k_s,C^jk_s>.

因此裸q²mass严格抵消；在operator trace组织中同样来自
`Tr(A_g U P U* A_g*)=Tr(A_g P A_g*)`，不需要猜测large-a。

由于C selfadjoint norm≤2，对j≥2有

    |Mj|≤2^(j−2)||Ck_s||².

故所有j≥3的完整逆余项是O_s(q³/p)=O_s(p^-5/2)。M1/M2的tail、r与q的差、`−2rc`cross也均已付入同阶或更小；未留下未知Neumann截断。得到

    ρp−ρ∞ =−2r cos(as)ρ∞
          +p^-2/π²[|κ_s|²−Re(β_s conjκ_s)]
          +O_s(p^-5/2).

这是密度组织，不声称pointwise密度的首项是p^-2：第一项仍有O(q)periodic factor，必须在同一actual source上消掉它。

## 4. 同源large-shift项：实位Γ/ε实际抵消

记`H_g(p)=∫|ĝ(s)|² cos(s logp)ρ∞(s)ds`。对每个fixed smooth compact source，本项可从实际P的kernel直接证明任意阶p-decay，避免prolate系数换和：

外部x,y≥1时`P(x,y)=δ(x−y)−(F L R L F)(x,y)`，`R=I+J`，J为第一节的smooth cos-even核。对ρ>1的scaling-diagonal，bare FLF项的kernel是

    [sin(2π(ρ−1)x)/(π(ρ−1)x)
       +sin(2π(ρ+1)x)/(π(ρ+1)x)].

这正是primary2021 `δ(ρ)+W∞(ρ)`的纯oscillatory部分：非oscillatory `ρ^-1/2/(1−ρ^-2)`已经与actualΓ kernel完全抵消。不能只取δ或ε的ρ^-1/2项再宣布1/p费用。

FLJLF项对第一个low坐标反复分部积分，也只留下endpoint1的sin/cos(2πρx)；endpoint0的odd derivatives全部0。令ρ=p exp(v)，v在源自相关的固定Cc∞支持内。**先对v配对**，每个phase的导数≥c_U p x，重复非驻相付任意p幂；x≥1的其余因子可积，深阶kernel余项也可直接付。于是

    H_g(p)=O_(g,N)(p^-N), every fixed N.

此组织使用smooth source和合法TC trace分布，不对未夹源的single UρP独立取trace。常数依赖自相关的seminorm；不是L²-only统一界。

## 5. fixed source的signed首项、求和及未付统一费用

第一至三节的s常数至多polynomial，fixed g∈Cc∞给ĝ Schwartz，所以可以积分pointwise误差。联合第四节即开头的候选

    Tp(g)−T∞(g)=p^-2 A_U(g)+O_g(p^-5/2),
    A_U(g)=1/(2π²)∫|ĝ(s)|²|κ_s−β_s|²ds.

这是首个actual signed项：非负，并且对非零源严格正。κ−β实轴上real analytic，非identically0（κ~constant，β~γ constant且Γ phase持续旋转），其零集不能有正测度；ĝ非零的L²源因此有正积分。

κ、β bounded给A_U bounded source-L² form。由第一节端点渐近，单位Fourier规范中的乘子为

    2π/π² [|κ|²−Re βconjκ]
       =π^-2(1−Re γ_s)+O(1/|s|).

Γ相位γ的inverse Fourier是actual smooth kernel`2e^(t/2)cos(2πe^t)`（可有反演，实部压缩同一结论）。在fixed finite U差集上它有界，source压缩为HS；O(1/|s|)项为C0压缩compact。因此`A_U=π^-2 I+compact_U`。positive form无kernel，Fredholm spectral theorem给actual `c_U>0`，不是把一个未知low projector定义成该常数。

对每个fixed非零g，存在有限p0(g)，使所有实际prime p≥p0(g)有

    Tp(g)−T∞(g) ≥ A_U(g)/(2p²)>0.

并且`Σ_p |Tp(g)−T∞(g)|<∞`（有限个小p的source trace已合法，尾由p^-2和p^-5/2控制）。此处是**从arch base分别添加单p**的actual增量，不是一般base-S添加p的增量。

剩余限制不能省略：A_U的coercivity只给首项；O_g依赖高阶source seminorm，没有证明全部L²源共同的p0或operator-norm summable tail。更未控制base S={∞,2}及growing S的混合terms/Gram inverse。旧514在另一种边界上的发散结果也不能反驳本single-p fixed-g求和。

## 核查状态与唯一下一动作

endpoint常数、actual q²返回、prime整数位置及完整inverse已明确到可逆审层次；新增证据针对同一真实源，非泛norm/旧同构。本文没有执行数值sample或拟合ζ零点。

父任务下一动作：不同组织逆审核裸Mellin distribution域、J smoothness、M1第三阶tail、全部cross及source large-shift配对；只有通过后才能升级fixed-g p^-2定理。再独立判断能否取得L²-only uniform tail或base-S运输，不能将fixed-g求和倒填成长预算或长期Goal完成。无本辅助任务的下载/计算进程。
