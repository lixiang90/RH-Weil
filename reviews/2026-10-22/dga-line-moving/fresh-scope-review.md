# 独立逆审：实际 DGA 的 line／moving／base-change 来源门

2026-10-22。审查者 `/root/dga_line_fresh_1022`，独占输出，不改 STATE、cadence 或主稿。
已按当前仓库恢复规程读 README／STATE、check 后 show、G20261014／workflow／C036、
D20261022F／前沿，再读本轮主稿、三分支及其依赖的实际 DGA 原件。
以下为最终指定版本的**限定 PASS**；hash 只绑定版本，不支付数学前件或代替 root 消费。

## 1. 结论及消费范围

未发现阻断本来源结算的问题。主稿准确区分了已经实际实现的设施与仍未实现的函数域几何：

* 有非指数的具体自由图线、保 frame 的物理源标记，以及全 405 Pan 的实际同伦。
* Koszul 修复确实给出全 Pan 上严格、协同的 DG 同构，并可作 semi-free 的 derived scalar extension。
* 这些结果不能说成「没有线对象／没有任何拼接」，但图线 Pic 类和该 Koszul 的行列式呈现均恒定。
* 所得信息仍由旧保双 degree 商 R 及其 multiplication cone 承担；未给非平凡 Picard tensor 移动、整格过滤、同对象独立容量或完整 Weil 预算的新身份。

因此按用户条件停止这个**已执行的现成 free／unit／Koszul recipe**是有依据的。
它不是 Pic(A) 全体、任意非自由模、相对层、非仿射增强或所有 g-integer 几何的不可行性定理。
本结算为标准设施及旧推论的来源 0，不新增 574／C037，不把停止当作长期 Goal 完成。

## 2. 代数对象与源关系核查

1. 原 DGA 是非 unital 的交换 DGA；其 Peiffer 恒等式由 E_c 单射与实际卷积兼容支付。
   单位化 A=C⁺ 在 Φ⁺ 坐标下确为 F⁺×C²；附加 λ 同时进入三个因子，未将 δ₀ 冒充 F 的函数。
   H⁰(A)=R=(F/I_c)⁺×C²、H<0=0；物理源 x_r 的类为 ([r],µ₊r,µ₋r)，其线性 kernel 正是 P_c。
2. L_r=A(1,x_r) 严格自由，第一投影给逆。标记 s_r=x_r(1,x_r) 闭；
   精确 Pan-coset 声明属于保 frame 的标记同伦，而不是所有未加 frame 的抽象 pair 同构类。
   主稿已保留 r 与 2r 可被 unit 缩放识别的反测，未错误宣称后者忠实。
3. 对任意实际 q∈P_c，唯一 η_q 给 dη_q=x_q。
   E_q(1,x_r)=(1,x_(r+q))，标记差为 d(η_q(1,x_(r+q)))；
   E_qE_p=E_(q+p)。单位上的乘法同伦补项 K_q(1)=η_q 正确，未遗漏 λ 项。
4. K_r=A[ε_r]、|ε_r|=−1、dε_r=x_r、ε_r²=0 是两自由分次生成元的 semi-free 对象。
   ε_(r+q)↦ε_r+η_q 的微分正确；奇次交换使交叉项抵消，η_q²=0，逆与可加协同均成立。
   它不是 rank-one line；在 R 上是 [R→R]，H⁰=R/(x̄_r)、H⁻¹=ann_R(x̄_r)。
   这与底 A 自身含负次链的总复形层次没有混淆。
5. 537 给双 pole-zero 的 x̄_r0≠0；R/(x̄_r0) 的 annihilator 为非零理想 (x̄_r0)，
   因而与 faithful R 模 R 不同，非根确被保留。
   两个非零 degree 幂等同时被 x_r0 杀掉，所以这个指定标量 mark 不是整个保 degree base 上的 regular Cartier section。
   局部化 principal exact 元素会 contract；将 x_r0 可逆化会移去 degree 因子。主稿只消费这些指定操作的范围。

[Stacks 22.37.1](https://stacks.math.columbia.edu/tag/09S5) 的 quasi-isomorphism／derived-module 等价适用。
它仅核普通代数范畴；不提供 Fréchet tensor、正闭形式、metric、valuation 或整格的比较。
有限自由 presentation 的 det 相消也没有被升级为「任何 determinant metric 无信息」或 Pic(R)=0。

## 3. 原范数、真实源费与成长量词

原 du／zero-extension Dlog 的卷积表示给 ||conv_r||≤||r||₁，
固定支撑 [−L,L] 上 ||r||₁≤√(2L)||r||₂，两个 moment 的 dual norm 为 √(2sinh L)。
故主稿 M_r 及 graph／mark／unipotent 的费用均为合法充分上界。
Dlog 右侧除 √log2 正确；µ±=0 可退至 √(2L)。

此 Hilbert 表示作用于次数零的代表元，实际 principal 的卷积仍可非零；
它不下降为 R 的正表示，不能用这些上界构造免费正商 norm。
负次链的 U_r 费用保留 ∫|r(t)|e^((a−b−1/2)t)dt 及 η_q 的 Schwartz 半范数。
特别新增的实际平移核查正确：
η_qv(x)=e^(−v/2)η_q(e^(−v)x)，E_cη_qv=τ_vq，
du／Dlog 的 q 源 norm 不变，q_ab(η_qv)=e^((a−b−1/2)v)q_ab(η_q)。
这是 E_c 单射给出的**这个实际 inverse lift**的固定半范数等式；主稿未把它说成所有新几何 lift 的必要费用下界。

553 已有的全线稠密结论只约束共同 Hausdorff 目标上全域连续、精确 coset-invariant 的实现。
本稿保留 Fréchet、fixed／变域、非共同 source-family 目标及有费 cofinal 修复；
未把 compact principal 空交当作全 Pan 的通过，也未把某个坏 minor 当必要源费。

## 4. 函数域的实际正控制

对 C/F₅:y²=x⁵−x+1，P=(0,1)、Q=(1,1)，M=O(2∞)≅K，
L₀=O(P+Q−2∞) 确为 degree zero。
canonical 评价矩阵 determinant=1，所以 H⁰(K−P−Q)=0；RR 给 h⁰(M⊗L₀)=1 而 h⁰(M)=2。
由此 L₀ 非平凡；非平凡 degree-zero line 自身没有非零全局截面，故先加正 degree 基准的区分必要。
分支给出的 ∞ 处 uniformizer x²/y 和局部 Cartier equations 也有正确的阶。

在有限点且 x(P_t)≠x(Q_t) 的真实开集 T 上，两条 graph 不交，
N=O(Γ_P+Γ_Q) 的每几何 fiber h⁰=1、h¹=0；q:C×T→T smooth proper，line N flat/perfect。
所以 q_*N 为 line、任意基变相容；评价给真正相对有效 degree-two Cartier divisor。
这由真实曲线、flat family 和 cohomology 条件支付，非 scalar extension 的别名。

已独立核 [Milne JVs §7 Thm 7.6](https://www.jmilne.org/math/xnotes/JVs.pdf) 和
[Stacks 36.30.4](https://stacks.math.columbia.edu/tag/0A1G)：
special fiber twist 后需 Jacobian 平移校正，一致的是校正后的 Picard/J-map；
不同有效除子或截面不必字面相同。分支保留 base-line、overlap 同构和一般扩域下降责任，未越界。
本正控制在 F₅ 原域给出，未靠未知 Frobenius 根或零点位置。

## 5. 连续双 pole-zero 正反、完整预算及脚本责任

连续控制的 c=1/4±1/16 均在原真实 positive g 分布族内。
R_d=C[z]/(z²+d)、z†=−z 的既定实对偶给
Tr(a_ra_r†)=2|A_r|²+2d|B_r|²，不能用普通矩阵 adjoint 偷换。
取同一 recipe g=uφ（φ 非负偶、compact 于 |u|<1），r=(D²−1/4)g，
两段均 µ±r=0、A_g=0、B_g>0、a_r=−(d+1/4)a_g，故完整型为相反严格符号。
这核查同样存在的 free／Koszul／base-change 设施不足决定目标符号；
没有声称连续控制已承载经典加法 adeles 或排除能独立拒绝负段的更强极化。

经典目标的 Γ/contact 能量、所有 p^k 与 signed 双 pole mixed 项均完整保留。
本门没有构造它们为同一截面的 arch 容量、局部整性过滤及 RR 缺陷的身份，
更没有独立 mixed 正系数或成长误差；按 Q 定义容量再假设正仍属等价／充分条件改写。

已独立执行 scripts/dga_line_moving_controls.py，全部 assertions 通过，
其解析后 JSON 与保存 exact-controls.json 完全一致。
脚本只核普遍多项式身份与有限旧控制，不认证全 Pan 解析域、Picard family 或 RH；
Koszul 的 signs／coherence 与上述几何论证由正文直接核查负责。

## 6. 版本绑定与最终准入

以下 SHA256 均按规范 LF（CRLF→LF）计算，审核前已读最终三分支及主稿新增平移段。

| 文件 | LF SHA256 |
|---|---|
| `goals/reviews/2026-10-22-actual-dga-line-moving-and-basechange-admission.md` | `461d0fb8610acf83efc10074263124f06938e7c0b5a1fb978d493eba1114810c` |
| `reviews/2026-10-22/dga-line-moving/actual-line-and-source-map.md` | `e43d22a4f24011b82c8adcfdc18e46e8e8cc96ed309c65d094a92467d2625ca8` |
| `reviews/2026-10-22/dga-line-moving/function-field-basechange-comparison.md` | `1d2c6fd55ca737199f2ddf9e25f37d450a113f55107c79b9f16dbbdb06ec5ea7` |
| `reviews/2026-10-22/dga-line-moving/norms-and-positive-negative-controls.md` | `34a48ef4c53fb5dac07c9f04ce9e6effa08afd67312a0f09d3575ea3a825850d` |
| `scripts/dga_line_moving_controls.py` | `d7e83fb4fc884d3f9f384583a42470489b887b82b43eb61342cfb9ff0339671e` |
| `reviews/2026-10-22/dga-line-moving/exact-controls.json` | `aaddb9cfdcea238fecab866e21f7d1dd5f4be162c0267b423b199d38124c768d` |

**限定 PASS**：可以 root 消费为本现成 recipe 的来源 0 结算，并按用户停止条件收口。
最强旧 542+555→557 的 whole leading 4/5 仍是负惯性上预算；本门没有实际负谱下界、
core／coupling／Ξ 或独立容量的新后果，宏观瓶颈未变。
再准入须提供实际非平凡 relative 对象、physical map／全关系／原费，以及至少一项独立过滤或容量数据。
不得仅换指数、Koszul 长度、图册名字或下一 paper 自动续合同；合法新几何和付费修复仍未排除。
