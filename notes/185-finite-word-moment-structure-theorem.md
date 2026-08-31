# Finite-word moment 指标结构定理与 arithmetic walk-SOS 接口

文档 182 的 Kaplansky theorem 使用所有 arithmetic squares `a^*a`，看起来仍是
一个无限条件。文档 183--184 在每个 finite connected rectangle 上证明生成代数
等于全部 matrix algebra。本笔记把两者合并成一个完全有限的结构定理：最多到
degree `d^2-1` 的 generator words 已张成 `M_d`，而 current positivity 精确等价
于相应 word-moment matrix 半正定。

这不是 RH 的证明，因为 moment entries 的 PSD 仍需算术证明；但它把非构造
order-density 条件转化为一个明确的 finite SDP，并把 entries 写成 labelled
transport graph 上的 weighted-walk correlations。更重要的是，moment matrix
不仅检测正性：在正交 word basis 下，它的完整负谱质量与原 Hodge current 的
negative trace 精确成比例，因此保留文档 149 真正需要的 bounded-index 条件。

## 1. Word-span stabilization

令 `G={g_1,...,g_s}` 是 `M_d(C)` 中包含 adjoints 的 finite generator set。
令 `W_L` 为所有长度至多 `L` 的 words（含 empty word `I`）的线性 span。

### 定理 AFT（universal finite word bound）[U]

若 `alg^*(G)=M_d(C)`，则

`W_(d^2-1)=M_d(C)`.                              (1)

更精确地，只要某一步 `W_(L+1)=W_L`，之后所有 word spaces 都稳定；所以在达到
dimension `d^2` 前每一步 dimension 至少增加一。

#### 证明

`W_(L+1)` 由 `W_L` 与所有 `g_jW_L` 张成。若 `W_(L+1)=W_L`，则 `W_L`
在各生成元左乘下不变，并含 `I`；归纳得所有更长 words 都在 `W_L` 中，所以
`W_L=alg^*(G)`。若生成代数为 `M_d`，稳定前 dimension 必严格增加。从
`dim W_0=1` 到 `d^2` 至多需要 `d^2-1` 次。`square`

这个 bound 很粗但完全 uniform；对 labelled paths/threshold complexes，实际
stabilization degree 可由有限计算显著降低。

## 2. Word-moment matrix

令 `tau=Tr/d`。取 `W_L=M_d(C)` 的一个 `L^2(tau)`-orthonormal word-linear
combination basis `w_1,...,w_(d^2)`，令 `X=X^* in M_d(C)`，定义

`M_L(X)_(i,j)=tau(Xw_i^*w_j)`.                   (2)

### 定理 AFU（finite word-moment inertia identity）[U]

`M_L(X)` 是 right-multiplication `R_X:a->aX` 在上述 basis 中的矩阵。因此

`spec(M_L(X))=spec(X)`, 每个 eigenvalue重复 `d` 次， (3)

并且

`n_-(M_L(X))=d n_-(X)`,                          (4)

`Tr_(d^2)[(M_L(X))_-]=d^2 tau(X_-)`.             (5)

特别地，以下条件等价：

1. `X>=0`；
2. `M_L(X)>=0`；
3. `tau(Xa^*a)>=0` 对所有 `a in W_L` 成立。

若 `X` 有负方向，则存在 degree至多 `d^2-1` 的 word linear combination

`a=sum_i c_iw_i`                                 (6)

使 `tau(Xa^*a)<0`。

#### 证明

trace cyclicity 给

`M_L(X)_(i,j)=tau(w_i^*w_jX)=<w_i,R_Xw_j>_(L2(tau))`. (7)

所以 `M_L(X)` 是 `R_X` 的矩阵。把 `X` diagonalize 后，`M_d` 的每一行
subspace 都给 `X` 的一份 spectral copy，得到式 (3)--(5)。另一方面，对
`a=sum_i c_iw_i`，

`c^*M_L(X)c=tau(Xa^*a)`.                         (8)

故条件 2 与 3 等价，且 `X>=0` 显然推出它们。反之若 unit vector `v` 满足
`v^*Xv<0`，取任意 unit `e` 并令 `a=ev^*`，则

`a^*a=vv^*`, `tau(Xa^*a)=d^(-1)v^*Xv<0`.        (9)

因 `W_L=M_d`，这个 `a` 可写成式 (6)，矛盾。因此条件 3 推出 `X>=0`。
最后结合定理 AFT 得 degree bound。`square`

若使用任意 nonorthogonal word basis，moment matrix与 `R_X` 只作 invertible
congruence：正负 eigenvalue 的个数仍由 Sylvester inertia law 保留，但式 (5) 的
negative trace identity一般失效。因此 bounded-index 估计必须先作明确的
`L^2(tau)` orthonormalization，并记录其 conditioning。

对 generalized bounded-index theorem，可把 strict PSD 替换成 moment matrix 的
negative-index/Schur complement ledger；但近似 defect 必须相对于 operator-norm
unit ball 标定，不能只用任意 coefficient Euclidean norm。

## 3. Labelled graph words are weighted walks

令 `L=diag(ell_v)` 是 vertex label，`B=B^*` 是 weighted adjacency。考虑交替
word

`w=L^(a_0)B L^(a_1)B ... B L^(a_k)`.             (10)

### 定理 AFV（exact weighted-walk expansion）[U]

其 matrix entry 为

`w_(u,v)=sum_(u=v_0~v_1~...~v_k=v)`

` ell_(v_0)^(a_0) B_(v_0,v_1) ell_(v_1)^(a_1)`

` ... B_(v_(k-1),v_k) ell_(v_k)^(a_k)`.         (11)

求和遍历 transport support graph 上长度 `k` 的 walks。

#### 证明

逐次展开 matrix multiplication；每个 `B` 选择一条 nonzero support edge，每个
diagonal `L^(a_j)` 在当前 vertex 贡献 label weight。`square`

因此 `M_L(X)` 的 entries 是成对 arithmetic walks 的有限相关和。对
threshold--Volterra generators：

- internal steps 是 simplicial face incidence；
- channel--product steps 是 Vaughan synthesis；
- product--prefix steps 是 Volterra interval incidence；
- diagonal weights 是 `log q`、face-product length、terminal height 与
  prefix endpoints。

这给 finite-word positivity recursion 一个具体组合解释：需要把 paired walks
组织成 squares 或由 boundary involution 配对消去。

## 4. Conditional finite arithmetic structure theorem

对每个 finite dyadic rectangle `T`，令 `G_T` 是不依赖 zeros 的 self-adjoint
arithmetic generators，`d_T=dim H_T`，`X_T` 是 joint signed current。假设
support/label theorem 已证明 `alg^*(G_T)=M_(d_T)`。选取 degree至多
`d_T^2-1` 的 word basis，形成 `M_T(X_T)`。

### 推论 AFW（finite arithmetic moment Hodge-index criterion）[C]

若对每个 `T` 取 `L^2(tau_T)`-orthonormal word basis，并且

`sup_T {d_T^(-2)Tr[(M_T(X_T))_-]+eta_T}<infinity`, (12)

其中 `eta_T` 包含各 finite currents 与 target explicit-formula current 的
低高度、Gamma、tail 和 quotient error，则 bounded finite-trace Hodge--Weil
theorem 推出目标 zeta/L divisor 的非平凡 zeros 位于中心线。

零预算 special case `M_T(X_T)>=0` 给 `X_T>=0`，但一般并不需要逐 block正性。

#### 证明

定理 AFU 给

`tau_T((X_T)_-)=d_T^(-2)Tr[(M_T(X_T))_-]`.       (13)

代入文档 149 的 bounded finite-trace Hodge--Weil theorem。`square`

式 (12) 是有限的，但 matrix size 最坏达到 `d_T^2`。若只是通过计算完整
`M_T(X_T)` 的负谱，它与直接计算 `tau_T((X_T)_-)` 精确等价。新内容只能来自
moment entries 的 arithmetic factorization、短 degree closure，或不形成完整
matrix 就能得到的 negative-trace majorant。

## 5. Graded Hodge audit

Möbius threshold complex 的 raw supersymmetric density

`X_raw=Gamma exp(-tDelta)`                        (14)

通常不是 positive：odd chain degrees 本来就带负号。故不能把式 (12)直接放进
零预算 PSD criterion，再把失败解释为 threshold structure失败。正确做法是二选一：

1. 对 raw graded current 使用式 (5)/(12) 的 bounded negative-trace ledger；
2. 先完成 primitive quotient、polarization 或 Schur shorting，再对所得 physical
   current测试 PSD。

这与有限域 Hodge--Riemann 机制一致：交叉形式先有 signature，primitive
polarization 后才得到所需正性。word-moment construction保留 inertia，不会把这
一步静默抹去。

## 6. Constructive and nonconstructive readings

### 非构造读取

support connectivity + simple labels 自动保证某个有限 degree 的 witness 存在。
若 RH 失败，某个 finite rectangle、finite degree moment matrix 必出现负方向。
这给反例一个 finite-word certificate。

### 构造读取

若能从 local identities 直接构造

`M_T(X_T)=R_T^*J_TR_T+E_T`,                      (15)

其中 `J_T` 是 Hodge-index signature、`E_T` 的 negative budget可和，就得到真正
的 arithmetic Hodge structure。最理想情形是 `J_T=I` 和 `E_T>=0`。

### No-free-lunch

因为 full word basis 张成全部 `M_d`，未经结构化的式 (12)与原 negative trace
bound 精确等价。不能把 moment reformulation 本身算作证明。必须展示独立于
zero locations 的短递推、walk involution、SOS factorization 或可和 defect。

## 7. 下一最小引理

当前最具体的后续任务是从 degree one 开始计算 block moment matrix

`[tau_T(X_T g_i g_j)]_(i,j)`                    (16)

（生成元取 self-adjoint，并包含 `I`），然后：

1. 用 exact summation-by-parts 展开 product--prefix entries；
2. 用 Möbius threshold McKean--Singer pairing 展开 face-incidence entries；
3. 分离 Gamma boundary 与 physical quotient kernel；
4. 将 grading/polarization sector显式分开，再检查 degree-one moment 的
   negative trace是否已有不可消除增长。

若 degree one 失败且负 minor随 scale不消失，这条 SOS 路线应降级；若它具有统一
Schur complement，再尝试 word-length induction。

## 8. 审计结论

本笔记给出了一个完全有限的广义结构判据：full-generating arithmetic graph 上，
zeta current 的 negative Hodge index 精确等价于正交 finite-word moment matrix
的归一化负谱迹；PSD 只是零负指数 special case。它把抽象 Kaplansky 存在性、
有限 transport graph 与可计算 SDP 接在一起，同时保留了 graded Hodge
signature。尚缺的、也是唯一可能产生真正 RH 进展的部分，是用算术/Hodge
identities证明这些 moments 的结构化指标界，而不是事后数值验正。
