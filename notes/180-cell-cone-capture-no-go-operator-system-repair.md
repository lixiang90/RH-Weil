# Cell-cone capture no-go 与 operator-system compression 修复

文档 179 的 one-sided atomic theorem在 polar cone由 cell packets捕获时最有效。
本笔记直接计算最简单、也是最自然的 capture ratio，得到一个 sharp no-go：
单个不交 partition的 orthogonal cell projectors只生成 diagonal PSD cone；它对
完整 rank-one correspondence effects的最坏 capture error随 cell数趋于一。

因此不能把文档 179 的 exact orthogonal certificate直接冒充完整 finite Gram
certificate。一个诚实的修复是 operator-system compression：cell algebra内的
negative responses加上 off-cell trace-norm remainder，严格控制完整 finite-trace
negative index。

## 1. Orthogonal cell cone

令 `H=C^M`，`v_1,...,v_M` 是 orthonormal basis。记

`p_i=v_i v_i^*`,                                (1)

并定义 cell cone

`C_cell=cone{p_1,...,p_M}`.                     (2)

它正是该 basis下的 diagonal PSD cone。对 unit vector

`u=sum_i a_i v_i`, `sum_i|a_i|^2=1`,            (3)

记 full rank-one effect `P_u=u u^*`。

### 定理 AFA（exact cell-cone capture error）[U]

`P_u` 到 `C_cell` 的 Hilbert--Schmidt projection为

`proj_(C_cell)P_u=sum_i |a_i|^2 p_i`,           (4)

并且

`dist_HS(P_u,C_cell)^2`

` =1-sum_i|a_i|^4`.                             (5)

所以 unit rank-one effects的最坏 capture ratio为

`eta_M=sqrt(1-1/M)`.                            (6)

它由 flat vector `|a_i|=M^(-1/2)` 达到，并在 `M->infinity` 时趋于一。

#### 证明

`p_i` 在 Hilbert--Schmidt内积下 orthonormal，因为

`Tr(p_ip_j)=delta_ij`.                           (7)

又

`<P_u,p_i>_HS=Tr(P_up_i)=|a_i|^2>=0`.           (8)

故到 nonnegative orthogonal cone的 projection逐坐标为式 (4)。因
`||P_u||_HS^2=1`，Pythagoras给式 (5)。在
`x_i=|a_i|^2>=0`、`sum x_i=1` 下，`sum x_i^2` 的最小值为 `1/M`，
给式 (6)。`□`

定理 AFA说明：cell atoms的 nonnegative coercivity虽为 `gamma=1`，但它们只对
所生成的小 cone有效。coercivity好不等于 capture好。

## 2. Real-cell phase obstruction

若所有 packet vectors在固定 basis中为 real，则其 projectors都在 real
symmetric Hermitian subspace。取

`u=(v_1+i v_2)/sqrt2`.                           (9)

`P_u` 的 imaginary off-diagonal part Hilbert--Schmidt norm为 `1/sqrt2`，所以

`dist_HS(P_u,C_real)>=1/sqrt2`                  (10)

对任意仅由 real packets生成的 cone `C_real`成立。故加入许多 real shifted
cells仍不能一致捕获带任意 correspondence phases的 rank-one effects；必须加入
modulated complex packets，或证明 arithmetic operator system根本不需要这些
phase directions。

## 3. Cell pinching

定义 trace-preserving pinching/conditional expectation

`E_cell(X)=sum_i p_iXp_i`.                       (11)

在 basis `v_i` 中，它删除全部 off-diagonal entries。对 self-adjoint `X`，

`Tr[(E_cellX)_-]=sum_i (v_i^*Xv_i)_-`.          (12)

这正是文档 179 的 orthogonal one-sided packet ledger。

### 定理 AFB（negative-index compression inequality）[U]

对任意 finite-dimensional self-adjoint `X,Y`，

`|Tr(X_-)-Tr(Y_-)|<=||X-Y||_1`.                 (13)

特别地，

`Tr(X_-)`

` <=sum_i(v_i^*Xv_i)_-`

`   +||X-E_cell(X)||_1`.                        (14)

#### 证明

finite-trace negative-part variational formula为

`Tr(X_-)=sup_(0<=Q<=I)-Tr(XQ)`.                 (15)

对任意 effect `Q`，

`|Tr[(X-Y)Q]|<=||X-Y||_1||Q||<=||X-Y||_1`.      (16)

交换 `X,Y` 后得式 (13)。取 `Y=E_cellX`并用式 (12)即得式 (14)。`□`

式 (14)是 capture no-go后的严格修复：没有被 cell packets看到的 directions
不会消失，而进入显式 off-cell trace-norm remainder。

## 4. Tracial von Neumann 版本

令 `(M,tau)` 是 finite von Neumann algebra，`N subset M` 是 von Neumann
subalgebra，`E_N:M->N` 是 trace-preserving conditional expectation。对
self-adjoint `X in L^1(M,tau)`，同一 variational proof给

### 定理 AFC（tracial operator-system compression）[U]

`tau(X_-)`

` <=tau[(E_NX)_-]+||X-E_NX||_(L1(tau))`.        (17)

若 `N` 是由 mutually orthogonal arithmetic cell projections生成的 commutative
algebra，第一项就是 cellwise one-sided Hodge ledger。

该定理允许用比完整 correspondence algebra小得多的 operator system；代价是
必须独立证明 off-system remainder可和。

## 5. Compressed center-line criterion

对 dyadic blocks `T`，令 `X_T` 是 joint prime--continuum--Gamma current，
`E_T` 是到 arithmetic cell algebra `N_T` 的 trace-preserving expectation。

### 推论 AFD（compressed one-sided Hodge--Weil criterion）[C]

若

`sum_T {tau_T[(E_TX_T)_-]`

`       +||X_T-E_TX_T||_(L1(tau_T))}<infinity`, (18)

连同低高度与 approximation ledger，则目标 divisor全部非零 zeros位于中心线。

#### 证明

定理 AFC逐 block给完整 negative trace的可和上界，再应用 bounded
finite-trace Hodge--Weil theorem。`□`

式 (18)有两种可能的成功机制：

1. 选择 arithmetic operator system，使 `E_TX_T` 保留所有真正负方向，而
   off-system remainder由 smoothness/commutator控制；
2. 使用多组 modulated cell algebras并作 martingale refinement，使 remainder
   随尺度趋零，同时保持 one-sided ledger可和。

## 6. 多 shifts 不能只靠数量论证

加入 `S` 组 shifted partitions会产生至多 `SM` 个 rank-one packet rays，但
“packet多”不自动意味着 capture。要逼近完整 complex projective rank-one
boundary，必须同时控制：

- packet vectors在 `C^M` 中的 angular covering；
- projectors在 `Herm_M` 中的 conic covering；
- nonnegative synthesis coercivity；
- 近似后的 off-cone remainder。

有限 real packets还受式 (10)的 phase obstruction。因而下一步不应只增加 random
shifts；应构造与 vertical modulation相容的 complex packet frame，并直接测量
式 (14)的 off-cell trace norm。

## 7. 下一步

在一个 finite Type II rectangle上，构造：

1. physical modulation `n^(-iT)` 加权的 complex cell vectors；
2. 相应 pinching `E_(T,theta)`；
3. joint arithmetic current `X_T` 的 diagonal negative ledger；
4. off-cell Schatten `L1` 与较易计算的 `L2`/rank bounds。

有限维可先审计

`r_T=||X_T-E_TX_T||_1/Tr(X_T)_-`                (19)

及多个 shifts的最优值。若 `r_T` 不随 rectangle改善，cell operator-system路线
应降级；若它趋零，再研究式 (18)的共尾可和率。

## 8. 审计结论

本笔记无条件证明 orthogonal cell cone的 sharp capture no-go，以及
operator-system compression的 trace-norm修复。它说明：

- 文档 179 的 one-sided certificate本身正确；
- 单个 cell cone不能代表完整 PSD polar cone；
- 所有未捕获 directions必须进入显式 remainder；
- 真正可测试的新量是 modulated cell pinching后的 off-system Schatten norm。

这进一步把“非构造存在一个好子代数”的想法化成有限矩阵可证伪问题。
