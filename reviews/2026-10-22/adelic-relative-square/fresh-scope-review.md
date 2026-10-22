# 独立逆审：actual restriction、相对 DGA 与平方容量

2026-10-22。结论：**限定 PASS，无需阻断修复。** 本稿只审数学及消费范围，不改 STATE、cadence、公共原件或 Git，不认证尚未发生的 root 消费／远程同步。

恢复已执行 README／STATE、check 后 show，并读 G20261014、workflow、C035、D20261022B、macro frontier 及前次 family 主稿必要范围。固定基线 0c4f 不变；长期门 open。已检查现场工作树为本轮主稿、三独占稿及 STATE 的未结算变动。审阅对象为：

- `goals/reviews/2026-10-22-adelic-restriction-relative-square-and-quadratic-capacity.md`，含后补一般 g 前件与 P¹ 两种 primitive 区别。
- 同目录 `actual-restriction-and-chain-carrier.md`、`frobenius-square-and-composition.md`、`quadratic-capacity-norm-and-controls.md`。

主稿含 Poisson 链对偶补充后的审阅版本 LF SHA256 为 `f6575df97169168dc55f02974feff59dc20a79223180de15cec3a57c129d78c1`；链稿为 `cb58537d128235e45c4500def54fc648ef545d0472e1f0ece3e5908cec6fe95c`；site 稿为 `3ed1cf2a5536b54e712a1cab332dc082992d7bb11e1be8ddfe748fc52f8c87d3`；容量稿为 `7dd3c9b35861b737f89bf0800231d5cb9a64bd3ab2e116a54eaf446d015658f0`。Hash 只定版本，不代下面的前件核查。

## 1. 全关系、非根与源同伦

主稿(1)的边界是实际 E_c 与两个连续矩的图；E 单射给 H⁻¹=0，闭像给分离 Fréchet 商。j(r)=0 当且仅当 r=E_cη 且两个矩均零，故核恰为 physical P_an。H⁰ 的分解公式直接抵消边界；其与 F_c/(CP_an) 的满射性另用405实际 u_d、u_c：两矩分别(1,0)、(0,1)，不是假设一般商可分裂。已对读405§§5–6。h 两矩1/4故 class 非零；完整 Q(h)=0 与此并不矛盾，不能将保 degree 商称为最小 Q 正商。

物理权核算：将 r*E_cη 的定义展开，恰得 E_cU_rη，U 核必须含 e^(−t/2)。U 仍保偶性、原点零值、零积分；带权 L¹ 控制各 Schwartz 半范数，换序合法。对任意 q=Eη_q∈P_an，K_q(g,a,b)=U_gη_q 在次数0给 ∂K_q=(r_q*g,0,0)，在次数−1将两边送入单射 E_c 后同为 r_q*E_cη。因此(3)覆盖全 principal，不是仅过 p。

537 的 r₀ 双矩为零而固定窗完整 Q(r₀)>0，足以反证 j(r₀)=0；若其同调作用全零，紧支近似恒等元及 Pan 闭性又反证 r₀∈Pan。此论证不预设未知零点位置，不推出成长结论。对应 action、类 map 与源 lift 角色清楚。

## 2. 显式 DGA 合法，旧“非自动”不能升为“不可能”

独立展开 Φ(α⋆β)：第二分量为 ac+aµ(h)+cµ(g)+µ(g)µ(h)=(a+µ(g))(c+µ(h))，负字符同理。因此 Φ 确为到 F_c×C² 的拓扑代数同构，∂S 对应 CI×0×0。混合次数 Leibniz 的 degree 分量为 −µ(g)µ(E_cη)，a、b 项精确相消。两个负次数的 Leibniz 是 Peiffer 等式，单射 E_c 与卷积交换性确实给出。令负次数相乘为零、B 只由首分量 U_g 作用，即得到非 unital 交换 DGA。

F_c 不含卷积单位；两个局部幂等并非全单位。j₀ 是代数映射且左乘正是已给 T_r；canonical projection 到 H⁰ 是 quasi-isomorphism。它在源层有实际 E 的定义，不以 Ξ 零除子作底空间；但取同调后的代数仍是405旧商，不能凭这一 presentation 获得独立算术结构层、有效 Cartier 类或 RR。链稿§2的“未自动成为 DGA”已由§3.1准确修补，主稿没有继承过时否定。

补充独立核主稿§4的链对偶：源在0的零值和零积分使 Poisson 的两个缺陷项都为零，故 E(hatη)(u)=e^(−u)Eη(−u)，中心化后恰为 E_c(hatη)(u)=E_cη(−u)。Fourier 平方是反演，偶源上 J²=1。矩满足 µ_±(g*)=overline(µ_∓(g))，于是 ∂J=(∂)† 且 † 保持⋆。直接 Fourier 换元，或送入单射 E_c 后使用卷积 involution，均给 J U_r=U_(r*)J。该反线性链对偶与 DGA 相容；它没有指定正 pairing，不能替代独立极化／RR 正号。

主稿§4新增一般 g 前件范围正确：没有 E 单射时 Peiffer 不由 equivariance 单独推出，也不能宣称 H⁻¹=0／quasi-isomorphism；需另证或更高复形。任意 g-integer 分布本身不自动提供加法 adeles、两个中心字符、整性或 Poisson 源；非自对偶情况需两边及对偶配对。未将经典特殊输入冒充普遍定理。

## 3. 原费用与容量方向

在 supp r⊂[−L,L] 时，卷积乘子在全线 du、Dlog 上均有 ||r||₁ 上界；degree 的 du dual squared norm为 ∫₋Lᴸe^(±u)du=2sinh L。Schwartz 费用来自 ∫e^(2κt)dt=sinh(2κL)/κ；κ=a−b−1/2 对整数 a,b 非零，连续值说明无害。Dlog≥√log2·du 的转换方向正确。主稿明确这是 representative action 的上界，未下降为正商 norm、必要源费用或全线统一界。

553 的全 Pan 平移稠密及 coset-invariant 非线性退化保持旧归属；保 Fréchet／固定窗／变域逃逸。y_r=EA_Lr 的实际最小 lift 费用≤||A_Lr||²亦正确，未拿全空间坏 singular value 或坏 minor 当实际源下界。

容量稿的 finite external square 是域上的 Künneth 恒等式，χ=(u−v)²不能自行当 signed RR。真 P¹×P¹ 限制序列确给 RΓO(n−2,n−2)，n=0 的χ=1来自 H²。F₁−F₂只对 ample F₁+F₂ primitive，平方−2；要求与两 fibre 同时交零时 P¹×P¹ 的数值方向仅零。这两个陈述已在主稿区分，不能以一维 ample-primitive 冒充本题双 degree 零的 r₀ 方向。

P¹_Z 的真实 n² 小截面容量成立：a>0 固定，toric 连续 metric 下各系数由单位圆 Cauchy 控制；系数盒半径 e^(an)/(n+1) 给下界，半径 e^(an) 给上界，故 log#=a n(n+1)+O_a(n log n)。这纠正了“所有曲线截面容量只有线性”的过强说法；没有新增源→该 metric／线丛的 relation-compatible map 或 primitive 系数身份。a 按待证 Q 选择会循环，稿中未这样消费。

407 的逐 idele acyclicity 及合法外 tensor 仍可缩，不反推源范畴零；balanced tensor 的双模与 Tor 责任、Z/p 两相邻同调的交错 log-order 为0亦正确。保 boundary／gluing／regulator 逃逸。

## 4. Site 例外、正反控制与完整目标

已独立打开 [1502.05580v1 的 §7.4](https://arxiv.org/html/1502.05580v1)，核 Definition7.6／Theorem7.7及其证明的终端 germ 论证：两参数无理且乘积有理时确为 Id_ε∘Ψ_(λµ)，不是 Ψ_(λµ)。稿中√2与其倒数例子和 literal 幂等半环加性群完成退化均正确；未据此排除 cycle 群、Witt、relative 提升。

current 的 exp pushforward 单射；405 的 ∫λ^(3/2)dC_(Cp)=M_p(2)=π/6 权正确，明确失败 Pan。a.e. 标签卷积与原 correspondence 的 diagonal／有限部分不可混为一体；TV 中原子与非零绝对连续测度互奇异，不能据弱 Riemann 和免费宣称 TV Bochner 实现。

568 的连续 d=±1/16 控制保各自实际 dagger 时 Q=2|A|²+2d|B|²，tensor Gram 为 diag(4,4d,4d,4d²)，负 d 仍有负方向。函数域局部 jets 与真正 C×C、signed RR／Hodge／全 period Gram 区分准确；已对读567/568相应公式及11/5、−1数据。没有将一般连续系统额外赋予 Q 的加法 adeles。

主稿(8)保完整 Γ/contact、全部 k≥1 素数幂、双 pole 及 complex mixed 项，规范归405/568；未把 DGA／site germ 本身识别成这些容量项。相同 determinant line 或 cocycle 仍需独立同对象身份和正号。strong-old 542+555→557 leading4/5继续是负惯性 upper 预算，非实际负谱 lower，core／coupling／Ξ 未改。

## 5. 消费结论与停止

主稿及三稿本地 Markdown 文件链接均存在。未见需修复的数学或范围阻断。可 root 消费为：**旧 actual restriction 的明确链／DGA presentation、准确 site 来源核查，以及标准／旧正反设施测试。** 它澄清“非 Ξ 定义来源存在”和“真实算术 n² 容量存在”，但没有把两者耦合为同源 primitive RR／完整 Weil 预算。

本轮 source0 分类可接受：DGA 是旧闭理想及 degree 字符的显式坐标 presentation，finite tensor、P¹ 与 toric 计数为标准设施检验；没有新的成长全源费用、classic 独立正性或实质方法类排除被隐藏为零轮。不得把“设施缺口缩小”表述为长期关键瓶颈已消除。下一须实际非形式比较／relative regulator 及可判同对象过滤或 primitive 系数，不能仅改商名字、续 tensor 次数或把等价充分包当证明。
