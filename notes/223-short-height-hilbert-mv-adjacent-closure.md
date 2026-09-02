# 223. 短高度 Hilbert--Montgomery--Vaughan 均值与相邻边界闭合

日期：2026-09-02

分支：MOM-1 / 路线 A

状态：Hilbert 值 Dirichlet 多项式均值、supercritical product-cluster 的任意短区间平均界、相对稠密 good heights 及 adjacent \(2+2\) 边界在这些高度上的闭合为 [T]；Montgomery--Vaughan 标量均值定理与 Riemann--von Mangoldt 公式为 [R]；从 adjacent 通道到完整四阶矩及新零点比例仍为 [O]；有限核检查为 [E]。

## 1. 结论

笔记 204 已证明，当 \(m>X\) 时 bulk product symbol 为零，并且真实有限边界簇满足

\[
 \sum_{X<m\le X^2}\|F_m^{\mathrm{fin}}(T)\|_{\mathrm{HS}}^2
 \ll 1+\log L,
 \qquad L=\log X.
\tag{1}
\]

此前的困难是式 (1) 只控制直和能量，不能逐高度控制不同 \(m\) 的相干和。本轮不再试图在固定高度对这些簇取绝对值，而是在高度变量上保留其精确相位。冻结 \(X,L,d\) 后，存在与高度 \(t\) 无关的有限矩阵 \(C_m=C_{m;X,d}\)，使

\[
 F_m^{\mathrm{fin}}(t)=m^{it}C_m,
 \qquad X<m\le X^2.
\tag{2}
\]

因此 supercritical aggregate 是 Hilbert--Schmidt 空间值 Dirichlet 多项式

\[
 G_{X,d}(t)=\sum_{X<m\le X^2}m^{it}C_m.
\tag{3}
\]

把 Montgomery--Vaughan 均值定理逐 Hilbert 坐标相加，得到对任意长度 \(H>0\) 的 interval \(I\)

\[
 \boxed{
 \frac1H\int_I\|G_{X,d}(t)\|_{\mathrm{HS}}^2dt
 \ll
 \left(1+\frac{X^2}{H}\right)(1+\log L).}
\tag{4}
\]

取

\[
 H_X=\frac{X}{\sqrt L},
 \tag{5}
\]

则式 (4) 右侧为

\[
 O(X\sqrt L(1+\log L))=o(XL).
\tag{6}
\]

所以每个这样的短区间都含有一个 \(t\)，使

\[
 \boxed{\|G_{X,d}(t)\|_{\mathrm{HS}}^2=o(N_X),\qquad N_X\asymp XL.}
\tag{7}
\]

由笔记 205 的 subcritical 闭合与笔记 206 的 pseudocovariance 等价式，adjacent \(2+2\) product channel 在相对稠密 good heights 上完整闭合。笔记 208 的 good-height transfer 随后允许把一个**已经在这些共同高度上闭合的完整零点比例不等式**传到所有高度。

这里最后一句有重要限制：本轮只闭合 adjacent \(2+2\) 通道；alternating、\(3+1\)、\(4+0\) 与 Gamma/continuum 尚未证明在同一组 good heights 上满足所需预算。因此本轮本身不产生新的零点比例。

## 2. Exact product-height factorization [T]

沿用笔记 204 的记号

\[
 b_n=-\frac1{2\pi}\frac{\Lambda(n)}{\sqrt n},\qquad
 x_n=\log n,
\]

\[
 R_t(x)=\beta_Le^{itx}T_d(q_x)D_d(x),
 \qquad \beta_L=\frac{2\pi}{a_LL}.
\tag{8}
\]

固定 \(X,L,d\)，并定义

\[
 F_m^{\mathrm{fin}}(t)
 =\sum_{ab=m}b_ab_bR_t(x_a)R_t(x_b).
\tag{9}
\]

### 引理 223-A（frozen product phase）[T]

存在与 \(t\) 无关的矩阵

\[
 C_m=\beta_L^2
 \sum_{ab=m}b_ab_b
 T_d(q_{x_a})D_d(x_a)T_d(q_{x_b})D_d(x_b),
\tag{10}
\]

使对所有实数 \(t\)

\[
 F_m^{\mathrm{fin}}(t)=e^{it(x_a+x_b)}C_m=m^{it}C_m.
\tag{11}
\]

特别地，\(C_m\) 已经包含所有 ordered factorizations \(ab=m\)、窗口、有限 Gabor 边界和正规化；式 (3) 不是把实际响应替换成任意系数模型。

#### 证明

把式 (8) 代入式 (9)。每个 \(ab=m\) 的 scalar height phase 都是

\[
 e^{itx_a}e^{itx_b}=e^{it\log(ab)}=m^{it}.
\]

其余因子在固定 \(X,L,d\) 后均与 \(t\) 无关，可以合并成式 (10)。\(\square\)

### 引理 223-B（supercritical coefficient energy）[T]

在笔记 204 的窗口假设下，

\[
 \boxed{
 \sum_{X<m\le X^2}\|C_m\|_{\mathrm{HS}}^2
 \ll 1+\log L.}
\tag{12}
\]

#### 证明

式 (11) 表明

\[
 \|C_m\|_{\mathrm{HS}}=\|F_m^{\mathrm{fin}}(t)\|_{\mathrm{HS}}.
\]

当 \(m>X\) 时，笔记 204 式 (14) 给 \(F_m^{\mathrm{bulk}}=0\)；其定理 AEP 在这些坐标上的限制正是式 (12)。这里用的是 direct-sum boundary energy，而不是 aggregate 的待证结论。\(\square\)

## 3. Hilbert 值 Montgomery--Vaughan 定理

### 定理 223-C（Hilbert-valued Dirichlet mean value）[T]；标量输入 [R]

令 \(\mathcal H\) 为 Hilbert 空间，\(v_n\in\mathcal H\) 只有有限多个非零。对任意实 interval \(I\) 长度 \(H\)，

\[
 \boxed{
 \int_I\left\|\sum_n v_nn^{it}\right\|_{\mathcal H}^2dt
 =H\sum_n\|v_n\|_{\mathcal H}^2
 +O\!\left(\sum_n n\|v_n\|_{\mathcal H}^2\right).}
\tag{13}
\]

隐含常数为绝对常数，与 \(\dim\mathcal H\)、interval 左端点及系数无关。

其中标量版本是 Montgomery--Vaughan 的 Dirichlet-polynomial mean-value theorem [R]。从标量版本到式 (13) 是 [T]。

#### 证明

取 \(\operatorname{span}\{v_n\}\) 的正交基 \(e_1,\ldots,e_r\)，写

\[
 v_n=\sum_{j=1}^r v_{n,j}e_j.
\]

由 Parseval，

\[
 \int_I\left\|\sum_nv_nn^{it}\right\|^2dt
 =\sum_{j=1}^r\int_I\left|\sum_nv_{n,j}n^{it}\right|^2dt.
\]

对每个 \(j\) 应用标量定理并求和；再用

\[
 \sum_j|v_{n,j}|^2=\|v_n\|^2
\]

即得式 (13)。因为标量常数不依赖 \(j\)，扩张是 dimension-free 的。对本轮矩阵空间而言本来就是有限维，不需要无限维交换极限。\(\square\)

文献输入：H. L. Montgomery and R. C. Vaughan, “Hilbert's Inequality”, J. London Math. Soc. (2) 8 (1974), 73--82。定理只涉及有限指数和，不含 zeta 零点信息。

## 4. 任意短区间平均与 good height [T]

### 定理 223-D（short-height adjacent mean）[T]

固定 \(X\ge3\)、\(L=\log X\) 和任意 admissible \(d\asymp XL\)。对任意长度 \(H>0\) 的实 interval \(I\)，式 (4) 成立。

#### 证明

在定理 223-C 中取 Hilbert 空间为 \(d\times d\) 复矩阵配 Hilbert--Schmidt 范数，取 \(v_m=C_m\)，且只对 \(X<m\le X^2\) 求和。于是

\[
 \int_I\|G_{X,d}(t)\|_{\mathrm{HS}}^2dt
 =H\sum_{m>X}\|C_m\|_{\mathrm{HS}}^2
 +O\left(\sum_{m>X}m\|C_m\|_{\mathrm{HS}}^2\right).
\tag{14}
\]

因 \(m\le X^2\)，式 (12) 给

\[
 \sum_{m>X}m\|C_m\|_{\mathrm{HS}}^2
 \le X^2\sum_{m>X}\|C_m\|_{\mathrm{HS}}^2
 \ll X^2(1+\log L).
\]

除以 \(H\) 即为式 (4)。\(\square\)

### 推论 223-E（relative-dense adjacent good heights）[T]

令 \(H_X=X/\sqrt L\)。对任意 \(Y\asymp X\)，interval

\[
 I_X=[Y,Y+H_X]
\]

中至少存在一点 \(t_X\)，满足

\[
 \|G_{X,d}(t_X)\|_{\mathrm{HS}}^2
 \ll X\sqrt L(1+\log L)=o(XL).
\tag{15}
\]

此外可以构造递增序列 \(t_r\to\infty\)，使

\[
 t_{r+1}-t_r=O\!\left(\frac{t_r}{\sqrt{\log t_r}}\right)=o(t_r)
\tag{16}
\]

且式 (15) 在每个 \(t_r\) 成立。

#### 证明

平均值非负，所以 interval 内至少一点不超过式 (4) 的平均。取式 (5) 后，

\[
 \frac{X\sqrt L(1+\log L)}{XL}
 =\frac{1+\log L}{\sqrt L}\longrightarrow0.
\]

为构造序列，递归取基点 \(Y_{r+1}=Y_r+H_{Y_r}\)，并在每个半开区间

\[
 [Y_r,Y_r+H_{Y_r})
\]

内选择一个 good point；若均值最小值只在右端点取得，则以连续性取任意逼近该值的内部点，仍保持式 (15) 的同一 \(o(N)\) 结论。这样所选点严格递增。相邻两个 good points 的距离至多

\[
 H_{Y_r}+H_{Y_{r+1}}=O(Y_r/\sqrt{\log Y_r}),
\]

且 \(t_r\asymp Y_r\)，得到式 (16)。\(\square\)

## 5. 冻结 cutoff 与 Gabor 维数审计

上面的平均必须固定系数 \(C_m\)，所以不能让 \(X,L,d\) 随积分变量 \(t\) 连续变化。本节说明这不破坏现有接口。

### 引理 223-F（frozen-parameter admissibility）[T]

设 \(Y\to\infty\)，

\[
 X=Y,\qquad L=\log X,\qquad H=X/\sqrt L,
\]

并固定任意 \(d\asymp YL\)。则对所有 \(t\in[Y,Y+H]\)，一致有

\[
 t\asymp X,\qquad \log t=L+o(1),\qquad d\asymp t\log t.
\tag{17}
\]

因此笔记 204--206 中只要求 \(T\asymp X\)、\(d\asymp TL\) 的矩阵与能量估计可在该 interval 上用同一 \(X,L,d\)。

若最终 dyadic zero-count statement 的上端点从 \(Y\) 移到所选 \(t\in[Y,Y+H]\)，则 Riemann--von Mangoldt 公式给

\[
 N(t)-N(Y)=O(H\log Y+\log Y)=O(Y\sqrt L)=o(YL).
\tag{18}
\]

所以冻结长度与实际 endpoint 的差异在零点比例尺度上消失。

#### 证明

由 \(H/Y=L^{-1/2}=o(1)\)，有 \(t/Y=1+o(1)\) 及

\[
 \log t-\log Y=O(H/Y)=O(L^{-1/2})=o(1).
\]

式 (17) 随即成立。式 (18) 是 Riemann--von Mangoldt 公式在长度 \(H=o(Y)\) interval 上的直接差分估计。\(\square\)

这里没有声称任何依赖精确等式 \(X=t\) 的、尚未写出的四矩归一化自动稳定。后续把其余通道汇合时，必须逐条确认它们对 \(t\asymp X\)、固定 \(d\asymp XL\) 一致；若某通道只在 \(X=t\) 的精确参数化下成立，则该稳定性另列为开放桥梁。

## 6. Pseudocovariance 与 adjacent 闭合 [T]

笔记 205 已证明 subcritical \(m\le X\) 的 aggregate 等于 direct-sum diagonal 加 \(o(N)\)。对 supercritical 部分，推论 223-E 给相对稠密 good heights 上

\[
 \left\|\sum_{m>X}F_m^{\mathrm{fin}}(t)\right\|_{\mathrm{HS}}^2=o(N).
\tag{19}
\]

这正是笔记 205 式 (6) 的实际 response 目标。由笔记 206 定理 206-C，在同一 good heights 上也有

\[
 \beta_L^4\|B_X(t)B_X(t)^{\mathsf T}\|_{\mathrm{HS}}^2=o(N).
\tag{20}
\]

所以 adjacent \(2+2\) product family 已在相对稠密高度上闭合。式 (20) 不要求

\[
 \beta_L\|B_X(t)\|_{\mathrm{op}}=o(1),
\]

因而与笔记 208 的 first-entry 正均方障碍完全相容：单个 boundary entry 或 covariance 可以保持自然尺度，而不同 product phases 在高度平均中仍使 aggregate/pseudocovariance 出现 good points。

## 7. 最小公理、删除审计与非同义反复性

1. **精确 product phase \(m^{it}\)**：负责把实际边界写成 Dirichlet 多项式。删除后，不能调用高度均值。该相位来自显式公式响应，不是人为加入的随机相位。
2. **direct-sum coefficient energy (12)**：负责主项与 Montgomery--Vaughan error 的统一预算。只有逐簇上界而无可和平方质量时，式 (4) 可失败。
3. **product support \(m\le X^2\)**：把 error 压到 \(X^2\sum\|C_m\|^2\)。若 support 延伸到 \(X^A\)，同一选择 \(H=o(X)\) 在 \(A>2\) 时不再闭合。
4. **高度 interval 长度 \(X/\sqrt L\)**：它在 \(o(X)\) 与 \(X^2/H=o(XL/\log L)\) 之间取得余量。若 \(H\ll X/L\)，当前 mean-value error 不足以给 \(o(N)\)。
5. **Hilbert 范数**：允许逐坐标应用标量均值且常数不随矩阵维数增长。把目标换成 operator norm 不产生同一恒等式，也没有在此被估计。
6. **Riemann--von Mangoldt**：只把 relative-dense endpoints 接到零点比例；它不构造 good points，也不参与式 (4)。

结论不是 RH 或待证 pseudocovariance 小性的改写：式 (19) 由 prime-side finite response、已证 direct-sum Hankel 能量和经典有限 Dirichlet 多项式均值推出，完全没有读取 zeros。真正未决的是其他四矩通道能否在同一 good heights 上闭合。

## 8. 模型范围

- **Riemann zeta**：定理 223-A--F 直接适用。
- **固定本原 Dirichlet \(L\)**：character phases 被吸收到 \(C_m\)，式 (13) 只读取 Hilbert norms；若笔记 204 的 direct-sum energy 对应版本成立，则同一结论成立。
- **Dedekind/automorphic \(L\)**：需要先证明其 product clusters 的式 (12) 型 Rankin--Selberg/direct-sum 能量；Hilbert--Montgomery--Vaughan 部分随后原样适用。
- **函数域**：height/Frobenius orbit 通常离散，必须以有限群上的离散大筛或轨道平均替代式 (13)；不能自动套用连续 interval。
- **仅有函数方程但 RH 类比失败的模型**：函数方程本身不给式 (12)，所以本定理不会错误推出中心线结论。

本结果属于显式公式型部分 Weil 配置的 finite-to-bulk/height-selection 桥梁；它没有构造上同调、Frobenius 极化或 Hard Lefschetz，也不主张两类 Weil 结构等价。

## 9. 循环性与结论边界

- [T] 式 (4)、(15)、(19) 是无条件 prime-side 定理；[R] 仅为 Montgomery--Vaughan 均值和 Riemann--von Mangoldt 计数。
- 本轮闭合的是 adjacent \(2+2\) supercritical aggregate 在 relative-dense good heights 上的输入，不是 all-height pointwise bound。
- 每个 interval 选择的 good point 由整个 adjacent aggregate 决定；不能为其余通道分别选择不同高度再把结论拼接。
- 尚未闭合 alternating/Farey、\(3+1\)、\(4+0\)、Gamma/continuum 及完整 response-specific Schur budget。
- 因此不能从本轮单独声称改进 \(0.6725\ldots\)，更不能声称 \(13/18\) 已无条件达到。
- 若后续其余通道也有非负高度平均 \(o(N)\) 预算，可以先把它们相加，再在每个 interval 选择一个共同 good point；这是下一轮应采用的 joint ledger，而不是交叉选择多个 exceptional sets。

## 10. 下一最小引理 [O]

建立一个 **common-good-height fourth-word ledger**：把 alternating、\(3+1\)、\(4+0\) 以及 Gamma/continuum remainder 写成同一非负 defect \(\mathcal D_X(t)\)，并证明

\[
 \frac1{H_X}\int_Y^{Y+H_X}\mathcal D_X(t)dt=o(N_X),
 \qquad H_X=X/\sqrt{\log X},
\tag{21}
\]

一致于 \(Y\asymp X\)。adjacent 项可由本轮定理直接加入该 ledger。若某通道只有 signed scalar 平均而非非负 defect，则必须保留与 Schur residual 的交叉项，不能用逐通道 absolute majorant 替代。

止损条件：若任一剩余通道的 Montgomery--Vaughan error 因有效 Dirichlet 长度超过 \(X^2\log^{1-o(1)}X\) 而在所有 \(H=o(X)\) 上达到 \(\Omega(N)\)，则记录为严格的 short-height obstruction，并转向 response-specific cross cancellation；不得靠延长到 \(H\asymp X\) 后仍宣称 relative-gap transfer。

## 11. 可复现检查 [E]

脚本 `scripts/adjacent_short_height_audit.py` 检查：

1. 随机复矩阵系数的 Hilbert 值指数和积分等于 exact finite kernel quadratic form；
2. 平移 interval 只给系数附加单位相位，不改变 diagonal/error ledger；
3. \((1+\log L)/\sqrt L\to0\) 的选取尺度；
4. 递归短区间产生 relative gaps \(o(T)\)。

脚本不实现 Montgomery--Vaughan 外部定理，不证明式 (12)，也不包含零点或 RH 证据。

## 12. 后续推进（笔记 224）

笔记 224 已执行本节要求的 single-selection 原则，但只针对 pure-prime bulk ledger：Henriot 型 shifted sieve 给 `3+1` 的 signed first mean，固定频率间隙给 `4+0`，二者按真实四词系数与本笔记的 adjacent defect 先相加再选一个高度；alternating primitive support 在同一点 uniform 为 `o(N)`。因此下一最小引理不再是“汇合 pure-prime bulk 通道”，而是 finite-to-bulk signed fourth-cycle boundary 与 Gamma/continuum mixed-word Schur defect。
