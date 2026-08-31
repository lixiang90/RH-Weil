# 数域类 Weil 结构的非构造存在性与研究分支图

本文研究一个区别于“直接构造数域上 Weil 上同调”的问题：能否先从有限、局部或对偶的算术条件出发，再用投影、紧致性、超积、逆极限或重建定理，非构造性地得到足以迫使零点位于中心线的全局结构？

结论分成两层。

1. **裸存在性不可行。** 若对象已经同时包含完整 divisor/determinant、Gamma--Euler 迹公式和正极化，那么它的存在性就是 RH/GRH 的等价重述。
2. **自动补全仍然可行。** 非构造方法可以免去最优 predictor 的公式、有限层之间的相容选择或极限 Hilbert/von Neumann 对象的显式描述；但必须保留一个由 primes、Gamma 与 continuum 独立验证的统一算术输入。

本文先给出一个与文档 173 直接衔接的投影--分离定理，再把候选路线按可检验性分级。这里没有宣称已经证明 RH；除标为 `[U]` 的泛函分析命题外，中心线应用都是条件性的。

## 1. 逻辑边界

设一个“完整类 Weil package”具有：

- 精确恢复目标完备 zeta/L 函数 divisor 的谱或正规化 determinant；
- 精确恢复 primes、Gamma、continuum 与极点项的 trace/supertrace；
- 足以应用文档 001、058、149 或 173 的正极化或有限迹负指标界。

### 命题 AEH（裸存在性的循环性审计）[U]

若上述 package 的存在推出中心线，而在假设中心线后又可用 divisor 谱的 tautological Hilbert realization 构造它，则“该 package 存在”与相应 RH/GRH 等价。

#### 证明

正向蕴含是结构定理；反向蕴含是在中心线假设下以零点作为正交谱、用反射对称给出伴随关系，再按 divisor multiplicity 定义 determinant/trace。故任何未附加算术来源条件的裸存在性定理都没有减少原问题。`□`

有效的非构造论证必须满足三条纪律：

1. **有限数据纪律：** 生成元、矩、kernel 与 current 只由 primes、Gamma、continuum、有限 combinatorics 或已证算术恒等式定义；
2. **补全纪律：** 选择公理、紧致性、GNS、Tannaka、dilation 或极限只负责补全对象，不负责凭空制造正性预算；
3. **稳定性纪律：** 迹、determinant、负指标和 divisor visibility 必须在所用极限拓扑下可传递。

## 2. 正算术锥的非构造投影

固定 dyadic height block `T`。令

`H_T=L^2(B_(0,T)^(-1)dmu_T;R)`，

其中 `B_(0,T)>0` 是文档 173 的零点无关正背景，`R_T` 是 joint prime--continuum--Gamma residual。固定 `0<epsilon<1`，置

`X_T=R_T+(1-epsilon)B_(0,T)`.                 (1)

令 `A_T subset H_T` 是由长度侧 arithmetic correspondences、threshold-complex incidence 与允许的 functional-calculus closure 生成的闭实线性空间，并假设 `B_(0,T) in A_T`。定义闭凸锥

`K_T=A_T cap H_(T,+)`,                          (2)

其中 `H_(T,+)` 是非负函数锥；非交换版本使用 tracial `L^2` 的正锥。

### 定理 AEI（positive arithmetic cone projection--separation theorem）[U]

对每个 `T`，存在唯一最近点

`E_T^*=proj_(K_T)X_T`.                          (3)

令

`C_T^*=E_T^*-(1-epsilon)B_(0,T)`.              (4)

则 `C_T^*>=-(1-epsilon)B_(0,T)`，并且在 `C in A_T`、`C>=-(1-epsilon)B_(0,T)` 的安全 predictors 中，

`e_T=inf_C ||R_T-C||_(H_T)^2`

`   =dist_(H_T)(X_T,K_T)^2`.                   (5)

若 polar cone 为

`K_T^o={Y:<Y,E><=0 for all E in K_T}`,          (6)

则 Moreau 分解给出

`e_T=sup_(Y in K_T^o)`

`        {2<X_T,Y>-||Y||_(H_T)^2}`.            (7)

对任意有限 block 集 `F`，

`sum_(T in F)e_T`

` =sup_(Y_T in K_T^o)`

`   sum_(T in F){2<X_T,Y_T>-||Y_T||^2}`.       (8)

#### 证明

闭凸集的 metric projection 唯一存在。由 `E_T^*>=0`，式 (4) 满足安全下界；而 `R_T-C_T^*=X_T-E_T^*`，故得式 (5)。Moreau decomposition

`X_T=proj_(K_T)X_T+proj_(K_T^o)X_T`

的两项正交，所以式 (5) 等于 `||proj_(K_T^o)X_T||^2`。在 `K_T^o` 上配方即得式 (7)；对有限直和 Hilbert 空间应用同一结论即得式 (8)。`□`

### 推论 AEJ（dual-separator centerline criterion）[C]

若存在与 `F` 无关的 `C`，使每个有限 block 集 `F` 都有

`sup_(Y_T in K_T^o)`

` sum_(T in F){2<X_T,Y_T>-||Y_T||^2}<=C`,      (9)

且文档 173 的低高度与 approximation ledger 一致有界，则 `sum_T e_T<=C`，定理 AEG 推出目标 zeta/L 函数的非平凡零点全在中心线上。

这严格回答了“能否不具体构造结构”：**可以不写出最优 predictor；最近点定理自动给出它。** 但工作被精确转移为零点无关的 separator bound，并没有免费得到 RH。

若 `A_T` 是闭子空间，则

`K_T^o=closure(A_T^perp+H_(T,-))`.              (10)

有限维时无需 closure。对偶证人由 arithmetic annihilator 与单侧负 effect 组成。若把 `A_T` 取成全部可测函数，投影就退化为逐点负部截断；若 `A_T` 由零点投影生成，也同样循环。因此下一步必须识别长度侧 polar cone 的极端或近极端 rays。

## 3. 近期主攻分支

### NCE-1：polar cone 的长度侧极端射线

**目标。** 在单个 square-root Type II rectangle 中，证明 `K_T^o` 的近极端 separator 可由 boundary-shell layer-cake effects 与 arithmetic annihilator 逼近，且常数不随 `T` 恶化。

文档 170 已把 effects 搬到 capped positive-definite correspondences；文档 166--168 已给 threshold boundary、profinite gcd Gram 与 Volterra transport。式 (10) 首次把它们与文档 173 的 clipped loss 放入同一精确对偶问题。

**最小引理。** 写出一个 finite Type II rectangle 的 `A_T` Gram 描述，求出有限维 `K_T^o`，并把 extremal separator 约化到数量受控的 boundary-shell rays。

**晋级条件。** 得到只含 joint prime/Gamma/continuum current、且严格弱于 full Weil negative-part energy 的 separator bound。

**停止条件。** 若复杂度增长时极端 rays 稠密逼近任意 spectral effect，则本路线只是 Weil criterion 的对偶重述。

### NCE-2：threshold Hilbert complex 与小谱密度

把文档 166 的乘法 threshold complexes `K_U(q)` 和 logarithmic interval incidence 组织成 `Z/2`-分次 Hilbert complex `(C_T,D_T)`，令 `Delta_T=D_T^2`。寻求

`X_T=E_T+Rcal_T`, `E_T in K_T`,                (11)

其中 `Rcal_T` 只由 harmonic boundary projection 或 `Delta_T` 的小特征值谱产生。候选输入是

`tau_T(1_[0,lambda](Delta_T))<=a_T lambda^alpha` (12)

及 compatible incidence bound，使 `sum_T||Rcal_T||^2<infinity`。

**非构造部分。** Hodge representative 与 harmonic projection 由闭算子谱理论自动产生，无需计算同调基。

**最小引理。** 在有限模型中证明

`e_T<=int_0^(lambda_0)w_T(lambda)`

`       d tau_T(1_[0,lambda](Delta_T))`

`     + 已控制项`.                              (13)

**循环风险。** `D_T` 不能由 zeta zeros 定义，也不能直接假设 heat supertrace 正或 harmonic mass 可和；谱密度必须来自 divisor lattice、boundary Morse pairing 或 profinite expansion。

### NCE-3：只随机分区的概率方法

随机化 log-dyadic shift、multiplicative grid 或 character packet 的表达方式，但保持实际 `mu(n)`、`Lambda(n)` 与 Gamma 数据不变。若

`sum_T E_omega K_T(epsilon,omega)<infinity`,     (14)

则 Tonelli/Fubini 保证存在一个确定 realization 使总 clipped residual 有限。

**最小引理。** 证明 shifted multiplicative grid 下

`E_omega sum_T K_T(epsilon,omega)`

` <= profinite gcd diagonal`

`    + 可和 boundary probability`.             (15)

不得随机化 Möbius/prime coefficients。文档 165 还表明，只换 basis/gauge 而不改变 physical current，不会自动降低凸损失；本路线应作为 NCE-1/2 的证明工具。

### NCE-4：算子系统正延拓与 dilation

只在有限 arithmetic correspondences 生成的小 operator system `S_T` 上构造正线性泛函或完全正 map，再用 Arveson--Stinespring 型延拓/dilation 自动产生 Hilbert realization。

**最小引理。** 证明 finite moment positivity 可在不扩大 negative-index budget 时延拓，并保持 Euler germ 与 determinant visibility。

**循环风险。** 延拓只传播已有正性；若 finite moments 已遍历全部 Weil tests，前提仍与 RH 等价。

## 4. 相容性与极限分支

### NCE-5：逆极限 / Mittag--Leffler extension

令 `X_n` 为满足前 `n` 个 primes、height blocks、Gamma moments 与误差 `2^(-n)` 的有限 packages。若每个 `X_n` 非空紧、restriction maps 连续，并且加入一个 prime/block 时旧块预算只增加可和误差 `epsilon_n`，则逆极限非空，无需显式选择相容序列。

**最小引理。** one-prime/one-block extension lemma，且 `sum_n epsilon_n<infinity`。

**停止条件。** 若 extension 需要完整 finite Weil positivity，或 conditioning 随 `n` 无界恶化，则逆极限没有减弱问题。

### NCE-6：连续逻辑与 tracial ultraproduct

把 bounded correspondences、trace、resolvent、有限精度 Euler germ 及

`tau(min(H_-,m))<=C`                            (16)

编码为连续逻辑公理。若每个有限子理论都有使用同一个 `C` 与统一 modulus 的零点无关模型，则 compactness/ultraproduct 产生全局 tracial 模型。

**最小引理。** 证明截断负部、resolvent trace 与 Euler germ 在 tracial ultraproduct 中稳定，并找到真正局部的 finite satisfiability theorem。

这一路线只解决“有限层皆可行但无法选择相容对象”，不能产生统一 `C`；无界算子与正规化 determinant 必须通过 bounded resolvents 编码。

## 5. 观察分支

### OBS-1：canonical system / de Branges 参数紧致性

Suzuki 对由 xi 函数构造的 `Theta_omega` 在 `omega>1` 时无条件构造了 canonical system，并指出若能延拓到所有 `omega>0`，就得到 RH 的 canonical-system 判据。可尝试由局部质量一致有界、normalization 非退化和 transfer-function 相容性，经 Helly/Banach--Alaoglu 弱紧性取得临界参数 Hamiltonian。

**最小引理。** 从 Euler/Gamma integral equation 而非零点展开证明

`sup_(omega in [omega_1,omega_2])`

` int_0^L tr H_omega(x)dx<infinity`              (17)

及 determinant-one/noncollapse。风险在于临界紧性可能恰在 off-line zero 处爆炸，仍有 RH 全强度。

参考：Masatoshi Suzuki, [A canonical system of differential equations arising from the Riemann zeta-function](https://arxiv.org/abs/1204.1827).

### OBS-2：finite-trace generalized Pick/Pontryagin realization

对 arithmetic transfer candidate `F_n` 考虑

`K_n(z,w)=[F_n(z)+F_n(w)^*]/[z+conj(w)]`.       (18)

目标是把“有限负平方数”推广为“有限规范负谱迹”：由有限 Pick matrices 的统一负部迹非构造地产生 bounded-index colligation，再与文档 149 的 normality 接合。

**最小引理。** 建立 tracial negative-square realization theorem，并识别 kernel negative trace 与 Cauchy Hodge index。精确 Pick positivity 已与中心线等价；固定负平方数也未必排除有限多个异常极点。

## 6. 长期几何分支

### LONG-1：C-star tensor / Tannakian reconstruction

尝试由 Arakelov correspondences、idele dynamics 与 threshold complexes 构造 rigid symmetric star-tensor category，具有 positive categorical trace、numerical radical quotient 与 unitary normalized prime flow，再由重建定理产生 Hilbert fiber functor。

普通 Tannakian 形式只给代数群，不自动给 compact real form 或 Hodge--Riemann positivity。已有 graded-Tannakian 构造从给定 Weil cohomology/homological functor 出发，不能为 `Spec Z` 免费创造所需上同调。

**最小引理。** 证明 threshold complex 是 dualizable object，其 categorical supertrace 等于 truncated Möbius defect，且 numerical quotient 上的 star-trace 对 boundary-shell morphisms 为正。

参考：Daniel Schäppi, [Graded-Tannakian categories of motives](https://arxiv.org/abs/2001.08567).

### LONG-2：函数域到数域的退化 / q-to-1 极限

若一族有限域 polarized packages 的 closed-orbit measures、Lefschetz traces、polarizations 与 normalized Frobenius flows 在适当有限迹拓扑中收敛到 primes、Gamma/continuum 与数域 flow，则弱极限会给出数域 package。

**最小引理。** 只做 fixed support `L` 的窗口版本：构造 function-field explicit formulas 向 zeta 窗口显式公式收敛，并审计 polarization normalization 对 `L` 的依赖。

风险是：完整正 Weil distributions 若已收敛到 zeta 的完整 Weil distribution，闭性立刻给 RH；这种“完整正性保持的收敛”本身可能包含全部难点。

## 7. 明确降级的伪非构造路线

以下方法不能单独成为主攻方向：

- 用零点作谱后应用 GNS，或用 Zorn 选择最大正子空间；
- 直接假设完整 Pick kernel 正；
- 对每个 finite Gram 独立选 PSD completion，却不给 uniform bound 与相容性；
- 用 invariant mean/Cesàro 构造极化，却不先证 two-sided uniform boundedness；
- 随机化 Möbius/prime coefficients；
- 只由局部 Satake purity 推 global zero purity；
- 把 tightness、normal family 或 compactness 本身称为“算术估计”。

这些至多重述文档 032、073、074、131、145、149、165 与 169 已识别的等价性或 no-free-lunch 边界。

## 8. 下一轮执行顺序

1. **主线 NCE-1：** 在 finite Type II rectangle 上计算 `K_T`、`K_T^o` 与 extremal separators；
2. **概念线 NCE-2：** 构造 threshold Hilbert complex 的 incidence Laplacian，验证式 (13) 的有限模型；
3. **工具线 NCE-3：** 检查 random shifted multiplicative grids 是否只支付 boundary probability；
4. **备用线 NCE-4/5：** 只在有限正性已得而 extension 卡住时使用；
5. **观察/长期线：** canonical systems、tracial Pick、Tannakian 与 q-to-1 暂不挤占主线计算。

下一轮最小交付物是以下二者之一：

- finite Type II rectangle 的 polar cone/extreme-ray 定理；
- clipped residual 到 threshold Laplacian 小谱质量的有限维不等式。

若失败，也应给出反例或复杂度爆炸率，据此降级分支，避免在同一等价重述上继续堆叠形式。
