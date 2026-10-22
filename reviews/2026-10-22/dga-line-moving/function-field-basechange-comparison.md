# 函数域 degree-zero 移动／base change 与实际相对 DGA：对象不能省去的差别

2026-10-22。本稿是用户指定准入门的独占函数域比较稿，供 root 消费；不更改 STATE、cadence 或合同。
已恢复 README、STATE、check/show、Goal／workflow／C036、D20261022F 和前沿，重读新路线图 §8、
前次 genus-two 门及实际 adelic DGA 主稿。以下标准几何和旧模型的直接后果不新增数学轮。

## 1. 原件究竟支付什么

定点核读 [Milne, JVs §§1、5、7，Thm 7.6](https://www.jmilne.org/math/xnotes/JVs.pdf)：
degree-g 族在 h⁰=1 开集有 canonical relative effective divisor；special fiber 先作 degree-zero twist，
再以 Jacobian 平移校正，校正后的 Picard 映射在交叠一致。§1 的 family 按 base 拉回线丛取商。
**这不声称不同 chart 的有效除子或其 canonical sections 直接相等。**

另核 [Stacks 36.30.4](https://stacks.math.columbia.edu/tag/0A1G)：proper flat finite-presentation 的
perfect 对象有 derived base change；[Stacks 17.25](https://stacks.math.columbia.edu/tag/01CR)
区分 invertible 与 globally trivial；[Stacks 35.3](https://stacks.math.columbia.edu/tag/023F)
要求真正的 descent datum 及 cocycle。下文具体计算自行展开，不把 these facilities 当新的 RH 结论。

### 一个容易先犯的类型错误

真光滑射影、几何连通曲线上，若 degree-zero 线丛 L 有非零全局截面，则其零除子有效且 degree 为零，
故零除子为空，截面处处生成 L，因此 L≅O。于是非平凡 L∈Pic⁰ 通常应有 h⁰(L)=0。
不能同时要求“每个实际源产生非平凡 degree-zero 线对象”和“该 line 自身有非零 effective section”。
函数域的操作先用固定正 degree 基准 M，再在 M⊗L 中取截面；最后在 Picard 类中记住 M 的扣除。
这与给一个 free module 取非零向量完全不同。

## 2. 一个在 F5 原域上实际存在的非平凡 twist

继续用真实光滑曲线 C/F5：y²=x⁵−x+1，g=2，唯一 infinity 记 ∞。
K∼2∞，H⁰(K) 的基为 ω₀=dx/y、ω₁=x dx/y；这些事实已在前次门独立核过。
取原域有理点 P=(0,1)、Q=(1,1)，并定义

\[
  M=\mathcal O_C(2\infty)\simeq\omega_C,
  \qquad L_0=\mathcal O_C(P+Q-2\infty).
\]

这是真 degree-zero 线对象。canonical 评价矩阵为

\[
 H^0(K)\longrightarrow K|_P\oplus K|_Q,
 \qquad \begin{pmatrix}1&1\\0&1\end{pmatrix}.
\]

行／列采用转置约定不影响 determinant=1。因此 H⁰(K−P−Q)=0。曲线 RR 给

\[
  h^0\mathcal O(P+Q)=1,
  \qquad h^0(M)=2,
  \qquad h^0(M\otimes L_0)=1.
\]

特别 L₀ 非平凡：若它平凡，则 O(P+Q)≅K，其 h⁰ 应为 2；矛盾。
由上一节，h⁰(L₀)=0。**degree-zero tensor 可真正改变 degree-g 线丛的 special 性；
任何同一线丛的 global unit automorphism 则不会改变 h⁰。**
这一差别由实际线对象检测，不涉及 Frobenius 根、点数界或 RH。

### 局部 frames 与不是 global unit 的 transition

令 D=P+Q−2∞。在足够小的 U_P、U_Q、U_∞ 上，可用 local Cartier equations

\[
 f_P=x,\quad f_Q=x-1,\quad f_\infty=(x^2/y)^{-2},
\]

并在避开 D 支撑的开集上用 1。这里 U_P、U_Q 须去掉相应的另一个 hyperelliptic 共轭点，
其余零极点也按需要缩去；∞ 处 x²/y 的阶为 1。以 e_i=f_i^{-1} 为 O(D) 的 frame，
交叠 transition 是 e_i=(f_j/f_i)e_j，且 g_ij g_jk=g_ik。
这些 g_ij 是各自交叠上的 units。若全部 transition 是 global frame 的 coboundary，则 L₀ 平凡，
与上面的 h⁰ 计算矛盾。因此“transition 本来就是 units”不等于“一个 global unit 就实现该 twist”。

## 3. 真正 family、base change 与校正后的 gluing

令 T⊂C×C 为有限点 pair (P_t,Q_t) 满足 x(P_t)≠x(Q_t) 的开集。
在 C_z×T 上，两个 graph Γ_P、Γ_Q 及 ∞×T 都是相对 Cartier divisors。实际 family 是

\[
 \mathscr L=\mathcal O(\Gamma_P+\Gamma_Q-2(\infty\times T)),
 \qquad \mathscr N=p^*M\otimes\mathscr L
             =\mathcal O(\Gamma_P+\Gamma_Q).
\]

每个几何 fiber 的 canonical evaluation determinant 为 x(Q_t)−x(P_t)≠0。
故 h⁰(N_t)=1、h¹(N_t)=0。对 q:C×T→T，由 cohomology/base-change，V=q_*N 是 line，
且任意 T′→T 有 V|T′≅q′_*N|T′；也可在此具体 family 直接看到每 fiber 的 effective section。
evaluation q*V→N，等价于 O→N⊗q*V⁻¹，给相对有效 Cartier divisor。
这里 divisor 是 finite flat degree 2：fiber 长度 2、proper，加上相对 Cartier/flatness 的事实共同负责。
不以任意 raw matrix 的非零 minor 代替上述 family 条件。

对一般 degree-g family N，在 good chart U_i 选 degree-zero L_i，使 N_i=N⊗p*L_i 的
h⁰=1。设由 N_i 得到的有效 divisor 为 D_i。取固定 reference M₀（degree g），则

\[
 [N\otimes p^*M_0^{-1}]
   =[\mathcal O(D_i)\otimes p^*M_0^{-1}]-[p^*L_i]
       \quad\text{in }\operatorname{Pic}(C\times U_i)/q^*\operatorname{Pic}(U_i).
\]

base pullback 的 q*V_i 因子在这个商中消失。在 U_i∩U_j，右端是同一个 Picard 类，
所以表示的 J-map 相同。通常 D_i≠D_j，且它们的有效 sections 不需相等。
若需 glue 具体线丛，须给

\[
 \mathcal O(D_i)\otimes p^*L_i^{-1}
 \simeq\mathcal O(D_j)\otimes p^*L_j^{-1}\otimes q^*N_{ij}
\]

及 triple-overlap cocycle；若还需 marked section/metric，则要同步记其 frames、base lines 和变换。
Milne 的校正后的 Picard gluing 不能免费升级为“所有 raw evaluation determinants 有同一全局 scalar”。
这正是 determinant line/relative family 能修复的合法范围，不是把 gluing 一概排除。

### 常数域与 descent 的边界

上面 P、Q、L₀ 和具体 good family 均在 F5 上定义，因而这个正控制没有偷偷使用扩域。
一般曲线的 generic good point／twist 则未必在原 F_q 上有 rational 选择；可以到有限扩张寻找，
再以真实 Galois descent data 检验是否下降。存在几何点不等于存在原域的 chosen divisor。
即使一个 class 下降，所选 section/frame 仍需相应下降数据；若取 norm，会改变 degree 并引入扩张次数。
这些代数步骤不给 physical du/Dlog 的 uniform constant；后者必须另证。

## 4. 与已有实际 adelic DGA 逐项比较

记已给 DGA 为 A，A⁻¹=S、A⁰=B=F_c⊕C²，
∂η=(E_cη,−µ₊E_cη,−µ₋E_cη)，B 上用原稿的 degree-cocycle ⋆，而非错误的裸逐分量乘法。
其经 Φ(g,a,b)=(g,a+µ₊g,b+µ₋g) 变为 F_c×C² 的形式。
实际 physical source r=e^{u/2}f 给 j₀(r)=(r,0,0)，卷积作用和源 lift U_r 已有明确公式。

一个真正合法而最小的 line-object 候选，是在 unitization A⁺ 上的 free rank-one dg-module

\[
 \mathscr F=A^+,\qquad s_r=j_0(r)\in Z^0(\mathscr F).
\]

这给**具体 line 与 marked source**；源不是只写一个“未知 section”标签。
对 q∈P_an，r_q=Cq，原有实际 null-homotopy T_rq=∂K_q+K_q∂；
537 的 r₀ 在 H⁰(A) 中非零；把同伦延到 unitization 时定义 K_q(1)=η_q，
因为 µ±(r_q)=0，仍有 ∂η_q=(r_q,0,0)。因此此 free-line section 的关系／非根检查本来通过。
但 r 改变的是 s_r，line 始终是同一个 free object；这没有复现 §2 的 L₀ 非平凡 twist。
它的 H⁰ 仍是旧 F_c/(CP_an) degree-扩张实现，不能再当新 Picard 空间。

| 函数域真实操作 | A 上已给实际操作 | 可以消费／仍不可消费 |
|---|---|---|
| tensor 非平凡 L₀∈Pic⁰ 改变 h⁰(M) | free line 上乘 source、换 global unit/frame | 合法作用／自动同构；没有产生非平凡 tensor class 或改变同一对象的 h⁰ |
| q:C×T→T proper，R q_*N 控制 H⁰/H¹ 与 jumps | 既有两项复形及旧商的 scalar extension | 可给 constant family；未给 proper pushforward、good locus 与 special-fiber 变换 |
| N_i 的 effective divisor，经 Picard translation 校正 | 主关系 ∂η 的 chain homotopy | 同伦消全部 Pan；不是 Cartier rational function、degree-zero line twist 或 relative effective divisor |
| 真 open cover 的 transition 与 triple cocycle | 单个 B 中 unit，或 conjugation 公式 | 只有明确 localizations/covers/transition 的 datum 才构成新 gluing；单个 global automorphism 不足 |
| M⊗L 的截面空间、tensor powers、局部消失与 RR | 任意正 Hilbert norm、外 tensor 维数平方 | 不产生同对象 primitive RR coefficient 或完整 Weil 正号 |

特别：C→R 的**代数** scalar extension 对向量空间是 exact，故
H⁰(A⊗_C R)=H⁰(A)⊗_C R，H⁻¹=0。
这项 constant-family base change 是真实而便宜的，却没有制造 curve-family 的非恒定 cohomology。
若改 completed topological tensor、变参数闭像或非平坦 ring，则须按那个实际对象重证；
这里既不声称全部完成张量失效，也不以 algebraic exactness 付款一个未知 analytic proper-base-change。

本比较不证明 Pic(A⁺)=0，不排非自由 projective、真正 local sheaf/stack、非仿射/derived families，
也不排较强 topology 下的新对象。要求是把它们写出来，并给出与 j₀(r) 的实际 map 和费用。
“可考虑所有 modules”本身既没有一个所需 line，也没有 physical source 到它的映射。

### degree 的类型也须比较

A 的 µ± 是复线性的卷积字符，不是已识别的整值 Chern degrees。
真 line bundle 的 fiber degree 在 connected algebraic family 中局部常值。
405 的 h 有两字符 1/4，不能未经 normalization/complexified correspondence 说明就把它们叫作线丛 degree。
可以先以 integral geometric generators 构造线对象，再在 correspondence/trace 层扩复系数；
但该比较和已定权必须独立给出，不能按目标 Q 或零点位置事后指定。

## 5. 原 du／Dlog 费用：已付作用和未付图册不是一项

固定 supp r⊂[−L,L]，已给 actual U_r 在源半范数
q_ab(η)=sup|x^aη^(b)(x)| 上满足

\[
 q_{ab}(U_r\eta)\le q_{ab}(\eta)
      \int |r(t)|e^{(a-b-1/2)t}\,dt.
\]

这是原 actual dilation 的 weighted-L¹ 费用；用 Cauchy–Schwarz 可换成固定 L 的原 du bound，
Dlog 版本再用 ||r||₂≤||r||Dlog/√log2。目标卷积作用费≤||r||₁≤√(2L)||r||₂，
µ± 的原 du dual norm 为 √(2sinh L)。这些是作用或所选代表的上界，不是必要 source lift fee。

它们没有估计某个新 Picard chart 的选择、transition、解 section、integral lattice 或 metric 的费用。
某个坏 minor 趋零也不能证明这些实际费用必要发散：前次 flat 双点模型已有好 minor 恒 1。
在全线原 du/Dlog 上，553 的全 principal 平移族稠密仍排除任意连续、全 coset-invariant 的
非退化 Hausdorff realization；Fréchet、fixed-window、变域/族和 cofinal 费用仍合法，须明确量词。

## 6. 连续正反控制：同一种 module/Pic 测试不会给同一种符号

用旧 562／563／567 完整 continuous Π 正反族，取 d=±1/16（c=1/4+d）。
primitive algebra 及 involution 是

\[
 R_d=\mathbf C[z]/(z^2+d),\quad z^\dagger=-z,
 \quad a_r=\int r(u)e^{uz}\,du.
\]

两种 R_d 都是 C⊕C；有限半单 ring 上 rank-one invertible module 均 free，ordinary tensor、
scalar base change、free-line/source 与 unit 变换都可做。可 exact 计算

\[
 \operatorname{Tr}(a_ra_r^\dagger)=2|A_r|^2+2d|B_r|^2,
 \qquad a_r=A_r+B_rz.
\]

正段 e^{uz}=cos(u/4)+4z sin(u/4)，负段为 cosh(u/4)+4z sinh(u/4)。
同 fixed 窗可给 |A_r|、|B_r| 的 √(2L)×各 sup-coefficient×||r||₂ 上界；Dlog 再除√log2。
负段取非零奇 r(u)=uφ(u)，φ≥0 偶 compact，则 A_r=0、B_r≠0，所以目标型严格负。
正段该型半正。忘掉 involution 的 algebra/Pic/free-module 设施完全相同，符号责任并未消失。

该控制保原模型的全部 prime-power 密度、两个 poles，Γ=0 是该模型本身的背景而非删项。
它不声称两模型已带上经典 E/adeles；这里只测试被推荐为普遍充分的 module/line 操作。
若以后构造 genuine non-free positive geometric realization，必须指出反段在哪个独立输入失败，
不能在 realization 定义中直接要求上述 trace≥0 再当作新证明。

## 7. 完整 Γ／prime powers／poles 的责任与本门停止

经典目标仍是旧规范的同一 Q_W(r)：双 µ pole 项、ψ(1/4)−logπ contact、
完整 Γ 平移能量及所有 (p,k≥1) 的 log(p)p^(−k/2) 自相关项。
已有解析 identity 不因把它写为 free-line 或 det-line 而变成独立 RR 正号。
本比较未给 Γ 的同对象 arch metric capacity、p^k 的同一 local filtration、双 pole 的同一 RR defect，
更未给它们在同一 integral model 上的 mixed quadratic 预算身份及成长误差。

这次正控制具体付出：非平凡 L₀、原域存在性、degree-g 的 h⁰ 改变、local transitions、
family good open 与 corrected Picard overlap，且把 degree-zero line 与有效化 section 分开。
对 actual DGA，现有 free-line/source、null-homotopy 和 scalar extension 均真实但仍回旧商。
因此**该现成 module recipe 在此停止**；不能把未给的 Picard family 或容量改名再建未知合同。

重准入至少须有新的实际 formula/data：

1. 不以 Ξ divisor 为 base 的非平凡可移动 line/relative object，及 full physical-source 比较；
2. 全 405 Pan 的相容 tensor/trivialization 或 source homotopy，537 r₀ 可见，并保两 degree 的真实角色；
3. 真 base-change/open-overlap datum 和同对象 integral local-vanishing filtration；
4. 原 du/Dlog 或明确付费强 topology 下的 actual source lift／metric 费用；
5. 独立有效性/RR/ample mixed 容量，再与完整 Γ、全部 p^k、双 poles 的预算识别。

这些不是已经满足的定理，也不是“它们不可能”的总否定。函数域正号来源仍在这些真实几何设施中；
经典独立容量输入、whole 4/5 后果、危险 core、coupling／Ξ 与长期 Goal 门均未改变。
