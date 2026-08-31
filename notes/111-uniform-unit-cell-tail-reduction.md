# Uniform unit-cell tail reduction

文档 107--110 把 exact spatial metric 与 unit-cell projection 的差写成 positive
rank-one sum，并逐步把 transfer error 压缩成 directional、positive-energy 与
capacity-relaxation quantities。本节证明一个此前缺失的 uniform approximation
theorem：只保留前 `M-1` 个 exact cell-variance corrections，所有后续 cells 的
总误差在 Loewner order 中是 `O(1/M)`，且常数与 `N`、jet rank 无关。

所以 continuous spatial metric 可统一约化为

`all unit-cell means + finitely many exact cell variances`,

尾部对 endpoint alignment 的影响有显式 `O(1/M)` stability radius。

## 1. Mean/variance coordinates on each cell

令 `bar W_N` 是区间 `[0,N^2]` 上全部 unit-cell means 的 Gram metric。对任意
coefficient vector `a`，记

`s=a^*slopes`                                      (1)

为首 cell `[0,1]` 的 mean，并记

`p_m=a^*p_m_vec`, `1<=m<N^2`,                     (2)

为 cell `[m,m+1]` 的 mean。若 `C_m` 是 cumulative-charge vector，

`p_m=s-log(1+1/m)a^*C_m`.                         (3)

设

`ell_m=log(1+1/m)`,                               (4)

`theta_m=1/[m(m+1)]-ell_m^2`,                    (5)

`rho_m=theta_m/ell_m^2`.                          (6)

则 cell variance energy 满足 exact identity

`theta_m|a^*C_m|^2=rho_m|s-p_m|^2`.              (7)

另一方面，projected energy 为

`a^*bar W_Na=|s|^2+sum_(1<=m<N^2)|p_m|^2`.        (8)

## 2. Uniform decay of the variance weights

### 定理 VB（cell variance/mean ratio bound）

对每个 `m>=1`，

`0<rho_m<=7/(6pi^2m^2)`.                          (9)

#### 证明

unit-interval Wirtinger--Poincaré inequality 给

`theta_m<=[m^(-3)-(m+1)^(-3)]/(3pi^2)`.           (10)

又由 `log(1+x)>=x/(1+x)`，

`ell_m>=1/(m+1)`.                                 (11)

因此

`rho_m<=([m^(-3)-(m+1)^(-3)]/(3pi^2))(m+1)^2`

` =(3m^2+3m+1)/(3pi^2m^3(m+1))`

` <=7/(6pi^2m^2)`,                                (12)

最后一步使用

`(3m^2+3m+1)/(3m(m+1))`

` =1+1/[3m(m+1)]<=7/6`. `□`

## 3. N-uniform Loewner tail

定义 cutoff tail

`E_(>=M)=sum_(M<=m<N^2)theta_mC_mC_m^*`,          (13)

其中 `2<=M<N^2`。

### 定理 VC（uniform finite-head approximation）

有

`0<=E_(>=M)<=epsilon_M bar W_N`,                  (14)

其中

`epsilon_M=7/[3pi^2(M-1)]`.                       (15)

令

`W_(N,M)=bar W_N`

` +sum_(1<=m<M)theta_mC_mC_m^*`.                 (16)

则 exact spatial metric `W_N` 满足

`W_(N,M)<=W_N<=W_(N,M)+epsilon_Mbar W_N`          (17)

`                    <=(1+epsilon_M)W_(N,M)`.     (18)

这些 inequalities 对所有 `N`、所有 finite direction ranks 同时成立。

#### 证明

由式 (7)，对任意 `a`，

`a^*E_(>=M)a=sum_(m>=M)rho_m|s-p_m|^2`

` <=2(sum_(m>=M)rho_m)|s|^2`

`   +2sum_(m>=M)rho_m|p_m|^2`.                   (19)

因为每个 `rho_m<=sum_(j>=M)rho_j`，式 (8) 给

`a^*E_(>=M)a`

` <=2(sum_(m>=M)rho_m)a^*bar W_Na`.              (20)

定理 VB 与 decreasing-series integral bound 给

`sum_(m>=M)rho_m`

` <=[7/(6pi^2)]sum_(m>=M)m^(-2)`

` <=7/[6pi^2(M-1)]`.                              (21)

代入式 (20) 得式 (14)--(15)。式 (16) 加回 head corrections 后立即给
式 (17)；又 `bar W_N<=W_(N,M)`，故得式 (18)。`□`

定理 VC 的重点不是对固定 `N` 截断有限和——那当然成立——而是 error constant
不含 `N` 或 rank。可先令 `N` 变化，再独立选择任意缓慢趋于无穷的 `M(N)`。

## 4. Endpoint stability of the finite-head model

令 `C_(N,M)` 是 `W_(N,M)` 的 response capacity，`kappa_(N,M)` 是其 null
endpoint coercivity。令 `A_hat_(N,M)` 为这个 finite-head metric 的 three-capacity
susceptibility upper。

### 定理 VD（finite-head centerline reduction）

定义

`eta_(N,M)^2=`

` C_B epsilon_M^2/[2C_(N,M)kappa_(N,M)]`,          (22)

`A_(N,M)^up=(sqrt(A_hat_(N,M))+eta_(N,M))^2`.      (23)

则 exact spatial excess 满足

`A_(W,N)<=A_(N,M)^up`.                            (24)

所以 minimum-`W_N` endpoint polynomial 满足

`R_c(P)<=c_1+|target|`

` *sqrt((R+1)(1+A_(N,M)^up)/C_B)`.                (25)

若存在 `M=M(N)->infinity` 使式 (25) 是

`o(sqrt(log N)/loglog(3N))`,                       (26)

则 fixed reduced-determinant principal strata 全部为 `o(1)`；在其余
Euler--Tate/Weil package 公理下，相应 zeta function 的 zeros 位于中心线。

#### 证明

定理 VC 给

`0<=W_N-W_(N,M)<=epsilon_MW_(N,M)`.               (27)

把文档 109 定理 UW 应用于 projected metric `W_(N,M)` 与 tail error。其 universal
balanced estimate 是

`eta_tail^2<=C_Bepsilon_M^2`

`             /[2C_(N,M)kappa_(N,M)]`,            (28)

故

`sqrt(A_(W,N))<=sqrt(A_(N,M))+eta_(N,M)`.         (29)

再用 `A_(N,M)<=A_hat_(N,M)` 得式 (24)。式 (25)--(26) 由文档 100 定理 TM
与文档 094 定理 SP 得出。`□`

定理 VD 是一个 genuine finite-rank reduction：除全部 cell means 的 discrete Gram
外，只需前 `M-1` 个 rank-one variance corrections；余下约 `N^2-M` 个 exact
variances 由一个 rank-independent scalar `epsilon_M` 一次性控制。

## 5. Finite audit

下表取 `R=3`。`exactRel` 是 actual tail 相对 `W_(N,M)` 的真实最大 generalized
eigenvalue；`epsilon_M` 是定理 VC 的 uniform bound；`eta_cap` 使用文档 110 的
exact tail capacity relaxation，`eta_bal` 使用定理 VD 的完全 uniform bound；最后
两列为相应 strict excess upper 对 actual excess 的倍率。

| `N` | `M` | `exactRel` | `epsilon_M` | `eta_cap` | `eta_bal` | `A_cap/A` | `A_bal/A` |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 30 | 4 | 7.79e-3 | 7.88e-2 | 0.291 | 2.123 | 1.1118 | 1.1297 |
| 30 | 8 | 3.85e-3 | 3.38e-2 | 0.298 | 1.052 | 1.1119 | 1.1192 |
| 30 | 16 | 1.98e-3 | 1.58e-2 | 0.176 | 0.566 | 1.1114 | 1.1152 |
| 30 | 32 | 9.85e-4 | 7.63e-3 | 0.095 | 0.289 | 1.1112 | 1.1131 |
| 100 | 10 | 2.95e-3 | 2.63e-2 | 0.0927 | 0.334 | 1.0411 | 1.0437 |
| 100 | 30 | 1.03e-3 | 8.15e-3 | 0.0368 | 0.121 | 1.0409 | 1.0419 |
| 100 | 100 | 3.07e-4 | 2.39e-3 | 0.0130 | 0.0383 | 1.0409 | 1.0412 |
| 100 | 300 | 1.01e-4 | 7.91e-4 | 0.00429 | 0.0126 | 1.0409 | 1.0410 |

真实 tail relative norm 呈清楚的 `1/M` 衰减；uniform theorem 保守约 factor
`8--10`，但 balanced stability 把它平方后，strict excess upper 很快接近 finite-head
susceptibility 的固有 `4%--11%` 松弛。

## 6. 对经典 RH 的新局部化

此前 continuous-to-discrete existence 需要同时理解约 `N^2` 个 cell variances。
定理 VC--VD 把它改写为：任选 `M(N)->infinity`，只需分析

1. 全部 unit-cell means 的 Gram `bar W_N`；
2. 前 `M(N)-1` 个 cumulative-charge rank-one corrections；
3. finite-head susceptibility、capacity 与 null coercivity；
4. 显式 tail scalar `7/[3pi^2(M(N)-1)]`。

例如取 polylogarithmic `M(N)`，tail metric error 已无条件为 inverse polylogarithmic。
这尚未证明经典 RH，因为 finite-head susceptibility/coercivity 仍需达到式 (26)；但
它证明了远端 cell variances 不可能是独立障碍，真正的算术困难已局部化到 cell
means 与缓慢增长的 initial charge window。

## 7. 计算实现

新增 `mobius_unit_cell_tail_projection_certificate`。它构造 `W_(N,M)`、exact tail、
finite weight-sum bound、定理 VC 的 uniform majorant，并复用 balanced Schur 与
capacity-relaxation stability certificates。回归测试核对 exact head+tail
reconstruction、Loewner domination 与 directed endpoint-excess upper。
