# Variational spectral equivalence of Hodge data

文档 111 证明 Möbius finite-head metric 与 exact spatial metric 满足

`W_(N,M)<=W_N<=(1+epsilon_M)W_(N,M)`,             (1)

其中 `epsilon_M=O(1/M)` 且与 `N`、rank 无关。本节抽离一个一般结构事实：这种
relative Loewner equivalence 自动传递到 Weil-style proof 真正使用的三个派生对象：

1. response capacity；
2. homogeneous/null Hodge spectrum；
3. Schur-shorted transversal polarization。

第三项尤其重要，因为 shorted form 同时含 response/null coupling，看起来并非简单
principal block；其稳定性来自一个变分最小化公式，而不需要逐项控制 coupling。

## 1. Abstract polarized response data

令 `V` 为 finite-dimensional complex vector space，`D` 为非零 response functional，
`K=ker D^*`。取任意 `v_0` 满足 `D^*v_0=1`，并以 `Z` 标识 `K`。令 `B_0>0`
是 `K` 上的 endpoint polarization。

对正定 Hermitian form `W`，定义

`delta_W=min_(D^*v=1)v^*Wv=C_W^(-1)`,            (2)

null restriction

`H_W=Z^*WZ`,                                      (3)

以及 response-shorted null form

`z^*S_Wz=min_(alpha in C)`

` (alpha v_0+Zz)^*W(alpha v_0+Zz)`.               (4)

式 (4) 与任意 adapted block matrix 的 Schur complement 相同，且不依赖 `v_0`
的选择。

## 2. Generic variational transfer

### 定理 VE（variational spectral-equivalence theorem）

设两个正定 forms 满足

`X<=Y<=cX`, `c>=1`.                               (5)

则：

`delta_X<=delta_Y<=c delta_X`;                    (6)

`H_X<=H_Y<=cH_X`;                                 (7)

`S_X<=S_Y<=cS_X`.                                 (8)

因此，对 fixed endpoint metric `B_0`，全部 ordered generalized eigenvalues 满足

`lambda_i(H_X,B_0)<=lambda_i(H_Y,B_0)`

`                         <=c lambda_i(H_X,B_0)`, (9)

`lambda_i(S_X,B_0)<=lambda_i(S_Y,B_0)`

`                         <=c lambda_i(S_X,B_0)`. (10)

若 `r=dim K`，还得到 determinant sandwiches

`1<=det(H_Y)/det(H_X)<=c^r`,                      (11)

`1<=det(S_Y)/det(S_X)<=c^r`.                      (12)

#### 证明

对 affine hyperplane `D^*v=1` 上每个 `v`，式 (5) 给

`v^*Xv<=v^*Yv<=c v^*Xv`。                        (13)

分别取 infimum 得式 (6)。把式 (5) restricted 到 `K` 立即得式 (7)。

对每个 fixed `z`，式 (5) 对所有 `alpha` 给

`Q_X(alpha,z)<=Q_Y(alpha,z)<=cQ_X(alpha,z)`.       (14)

左边两项分别对 `alpha` 取 infimum给 `S_X<=S_Y`。右侧先用
`Q_Y<=cQ_X` 再取 infimum，给 `S_Y<=cS_X`，故得式 (8)。

式 (9)--(10) 由 generalized Courant--Fischer min--max principle；式
(11)--(12) 是相应 eigenvalue products。`□`

定理 VE 对任意 positive approximation scheme 成立，不限于 Möbius/Nyman 数据。
它说明在广义 Weil 结构中，若 chain-level polarization 可作 relative positive
approximation，则 capacity、primitive/null spectrum 与 Lefschetz-style shorted
polarization无需分别重证稳定性。

## 3. Finite-head Hodge convergence

### 定理 VF（uniform convergence of Möbius Hodge data）

取文档 111 的 `W_(N,M)`、`W_N` 与

`c_M=1+7/[3pi^2(M-1)]`.                           (15)

则同时有

`1<=delta_(W_N)/delta_(W_(N,M))<=c_M`,            (16)

`1<=lambda_i(H_(W_N),B_0)`

`      /lambda_i(H_(W_(N,M)),B_0)<=c_M`,          (17)

`1<=lambda_i(S_(W_N),B_0)`

`      /lambda_i(S_(W_(N,M)),B_0)<=c_M`.          (18)

特别地，若 `M=M(N)->infinity`，则 capacity、每个 fixed-rank null eigenvalue、
shorted eigenvalue 以及其 determinant products 全部以 relative `1+o(1)` 收敛，
且 convergence uniform in `N`。

#### 证明

文档 111 定理 VC 给式 (1)。对 `X=W_(N,M)`、`Y=W_N`、`c=c_M` 应用定理
VE 即得式 (16)--(18)。`M->infinity` 时 `c_M->1`。`□`

这比单独的 metric tail bound 更接近 cohomological existence statement：finite-head
model 的 transversal polarization strength 与 actual spatial model 的 strength 具有
相同渐近阶，远端 variances 不可能隐藏一个额外的小特征值或破坏已有的 primitive
gap。

## 4. Stable finite-head Weil criterion

### 定理 VG（spectrally stable finite-head Weil transfer）

考虑任意 fixed-rank Euler--Tate/Weil package，其 archimedean positive form为
`W_N`，并以 `W_(N,M)` 构造 finite-head approximation。若存在 `M(N)->infinity`
使

`sqrt(A_hat_(N,M))`

` +sqrt{C_(B,N)epsilon_(M(N))^2`

`        /[2C_(N,M)kappa_(N,M)]}`                (19)

满足文档 094 的 reduced-determinant threshold，即相应 Riesz upper 是

`o(sqrt(log N)/loglog(3N))`,                       (20)

则 actual package 的 fixed principal strata 为 `o(1)`，其 zeta zeros 位于中心线。

此外，式 (19) 中的 capacity 与 null/shorted coercivity 可替换为 actual quantities，
只损失 relative factor `1+o(1)`。

#### 证明

第一段正是文档 111 定理 VD。定理 VF 给 capacity inverse 与全部 relevant
coercivities 的 relative `1+o(1)` equivalence；取平方根后仍为 `1+o(1)`，不改变
strict little-`o` threshold。最后应用文档 100 定理 TM 与文档 094 定理 SP。`□`

定理 VG 抽象出的普遍机制是：

`relative positive approximation`

` => variational Hodge-data equivalence`

` => stable Weil centerline criterion`.           (21)

这可用于任何能构造类似 `X<=Y<=(1+o(1))X` 的 arithmetic/cohomological
approximation，而不依赖本项目的具体 Möbius basis。

## 5. Finite audit

下表取 `R=3`。`cap` 是 inverse-capacity ratio；`nullMax`、`shortMax` 是 actual/head
relative spectra 的最大值；`kappa`、`sigma` 分别是 null 与 shorted 最低
generalized eigenvalue ratios。

| `N` | `M` | `c_M-1` | `cap` | `nullMax` | `shortMax` | `kappa` | `sigma` |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 30 | 4 | 7.88e-2 | 1.000705 | 1.007649 | 1.004042 | 1.003867 | 1.001905 |
| 30 | 8 | 3.38e-2 | 1.000404 | 1.003529 | 1.001231 | 1.002120 | 1.000751 |
| 30 | 32 | 7.63e-3 | 1.000135 | 1.000852 | 1.000235 | 1.000506 | 1.000124 |
| 100 | 10 | 2.63e-2 | 1.000186 | 1.002816 | 1.000893 | 1.002330 | 1.000484 |
| 100 | 30 | 8.15e-3 | 1.0000788 | 1.000964 | 1.000247 | 1.000838 | 1.000159 |
| 100 | 100 | 2.39e-3 | 1.0000270 | 1.000280 | 1.0000627 | 1.000241 | 1.0000336 |
| 100 | 300 | 7.91e-4 | 1.00000884 | 1.0000919 | 1.0000200 | 1.0000796 | 1.0000110 |

universal factor 明显保守，但所有 actual/head ratios 均严格落在 `[1,c_M]`，并随
`M` 稳定趋于 1。shorted spectrum 通常比 raw null spectrum 更稳定，说明远端
cell variances 对 response coupling 与 null energy 的影响大幅共同抵消。

## 6. 计算实现

`mobius_unit_cell_tail_projection_certificate` 现计算 inverse-capacity ratio、完整
null/shorted relative spectra、null coercivity ratio 与 shorted coercivity ratio。
回归测试逐项验证它们位于定理 VE 的 `[1,1+epsilon_M]` interval。
