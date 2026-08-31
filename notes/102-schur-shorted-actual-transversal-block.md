# Actual metric 的 Schur-short transversal Hodge block

文档 101 构造了理想 completion `W+tau P^*BP`，但留下一个关键存在性问题：
这样的正 transversal block 是否来自 actual arithmetic metric，而不是人为改变
optimization？本节给出肯定的有限维结构答案。每个 `W>0` 都含有一个唯一最大
强度的 `tau P^*BP`；其强度是消去 distinguished response line 后的 Schur-short
coercivity。

这不会自动证明 RH，因为最大强度可能太小；但它把“构造新 Hodge block”改成
“估计 actual metric 内已存在的 canonical shorted block”。此外该强度对 spatial
shell gluing 超可加，因而可由局部正算术能量积累。

## 1. Green first moment

沿用文档 100--101 的记号：

`C_W=D^*W^(-1)D`, `C_B=D^*B^(-1)D`,

`v_B=B^(-1)D/C_B`,                                  (1)

`H=Z^*WZ`, `B_0=Z^*BZ`, `h=Z^*Wv_B`.               (2)

令

`a=v_B^*Wv_B>0`.                                    (3)

在文档 101 的 null generalized basis 中，记 eigenvalues 为 `lambda_i`、forcing
为 `g_i`。

### 定理 TR（null Green first-moment identity）

有 exact identity

`sum_i |g_i|^2/lambda_i=a-1/C_W`.                   (4)

因此若 `kappa=lambda_min(H,B_0)`，则

`A<=C_B(a-1/C_W)/kappa`.                            (5)

若右侧非零，定义 forcing-effective slope

`kappa_eff=(a-1/C_W)/(A/C_B)`.                      (6)

则 `kappa_eff>=kappa`，且

`A=C_B(a-1/C_W)/kappa_eff`.                         (7)

#### 证明

文档 100 的 response-zero minimization 给

`1/C_W=min_(D^*v=1)v^*Wv=a-h^*H^(-1)h`.            (8)

对白化后的 `H` 作 spectral expansion 即有
`h^*H^(-1)h=sum_i|g_i|^2/lambda_i`，得到式 (4)。文档 101 的
`A/C_B=sum_i|g_i|^2/lambda_i^2`；以
`lambda_i>=kappa` 得式 (5)。式 (6)--(7) 是同一 spectral measure 的加权
harmonic mean 表达。`□`

式 (5) 比文档 101 的 `C_BF_0/kappa^2` 多使用一次全局 response capacity，
因而在 forcing 不集中于最低 mode 时可显著更强。

## 2. 最大 actual transversal extraction

令

`P=I-v_BD^*`, `B_perp=P^*BP`.                       (9)

在 affine-adapted coordinates `[v_B,Z]` 中，

`W ~ [[a,h^*],[h,H]]`, `B_perp ~ [[0,0],[0,B_0]]`. (10)

定义 response-line shorted metric

`S_0=H-hh^*/a>0`,                                  (11)

及其 endpoint coercivity

`sigma=lambda_min(S_0,B_0)>0`.                     (12)

### 定理 TS（maximal contained transversal block）

对 `tau>=0`，

`W-tau B_perp>=0` 当且仅当 `tau<=sigma`.           (13)

所以有 canonical decomposition

`W=W_res+sigma B_perp`, `W_res>=0`,                (14)

且不存在强度更大的同形正 transversal block 被 `W` Loewner 支配。

#### 证明

坐标矩阵 `[v_B,Z]` 可逆。由式 (10)，`W-tau B_perp` 的左上 scalar block
仍为 `a>0`；Schur complement criterion 表明其半正定当且仅当

`H-tau B_0-hh^*/a=S_0-tau B_0>=0`.                 (15)

最后一个条件按 generalized Rayleigh quotient 恰等价于 `tau<=sigma`。`□`

因此文档 101 的 completion 并非只能外加。每个 actual positive metric 都已经
包含它，问题只在其 canonical strength `sigma` 是否足够大。

## 3. Shorted spectral identity

取 `B_0=LL^*`，令

`J_0=L^(-1)S_0L^(-*)`, `f=L^(-1)h`.                (16)

设 `J_0u_i=eta_i u_i`，并令 `q_i=u_i^*f`。于是
`sigma=min_i eta_i`。

### 定理 TT（actual-block spectral formula）

有

`sum_i |q_i|^2/eta_i=a(aC_W-1)`,                   (17)

以及

`A=C_B/(aC_W)^2 sum_i |q_i|^2/eta_i^2`.            (18)

特别地，

`A<=C_B(aC_W-1)/(sigma a C_W^2)`.                  (19)

#### 证明

白化后的 null metric 为 rank-one update

`K_0=J_0+ff^*/a`.                                  (20)

记 `T=f^*J_0^(-1)f=sum_i|q_i|^2/eta_i`。Sherman--Morrison formula 给

`K_0^(-1)f=J_0^(-1)f/(1+T/a)`.                    (21)

另一方面式 (8) 给

`1/C_W=a-f^*K_0^(-1)f=a^2/(a+T)`.                 (22)

故 `T=a(aC_W-1)` 且 `1+T/a=aC_W`，证明式 (17)。Feshbach shift 的
`B_0`-norm 是式 (21) 的 Euclidean norm squared，得到式 (18)。最后以
`eta_i>=sigma` 把 second Green moment 估为 first Green moment 除以 `sigma`，
即得式 (19)。`□`

式 (18) 是 actual-contained completion 的精确版本；它没有修改原 metric 或
zeta problem。

## 4. Spatial shell gluing

设 actual metric 分解为正 blocks

`W=sum_s W_s`.                                      (23)

对每个 block 定义

`a_s=v_B^*W_sv_B`, `h_s=Z^*W_sv_B`, `H_s=Z^*W_sZ`,

`S_s=H_s-h_sh_s^*/a_s`.                            (24)

这里先假设 `a_s>0`；若 `a_s=0`，positivity 强迫 `h_s=0`，并取 `S_s=H_s`。
令 `r_s=h_s/a_s`、`a=sum_sa_s`、`r=(sum_sh_s)/a`。

### 定理 TU（shorted-shell superadditivity）

total shorted metric 满足 exact variance decomposition

`S_0=sum_s S_s+Delta`,                              (25)

其中

`Delta=sum_s a_s(r_s-r)(r_s-r)^*>=0`.              (26)

若 `sigma_s=lambda_min(S_s,B_0)`、
`sigma_Delta=lambda_min(Delta,B_0)`，则

`sigma>=sum_s sigma_s+sigma_Delta`.                 (27)

#### 证明

展开式 (24) 并使用 `sum_sa_sr_s=ar`，得到

`sum_s a_sr_sr_s^*-arr^*=sum_s a_s(r_s-r)(r_s-r)^*`，即式
(25)--(26)。又 `S_s>=sigma_sB_0`、
`Delta>=sigma_Delta B_0`，求和即得式 (27)。`□`

`Delta` 与普通 cancellation 不同：即使所有 `h_s` 同号，只要 ratios
`h_s/a_s` 不相同就产生正增益。此外不同 `S_s` 的最低方向旋转还可使式 (27)
严格增强。因此 actual transversal strength 可由三部分生成：shell 自身 coercivity、
coupling-slope dispersion、以及 soft-direction rotation。

## 5. Automatic-short centerline criterion

### 定理 TV（actual transversal Hodge structure theorem）

在文档 094--101 的 fixed-determinant setup 中，minimum-`W` polynomial 满足

`R_c(P)<=c_1+|t| sqrt((R+1)/C_B`

` *[1+C_B(aC_W-1)/(sigma a C_W^2)]).`              (28)

若式 (28) 为

`o(sqrt(log N)/loglog(3N))`,                        (29)

则全部 fixed reduced-determinant principal strata 为 `o(1)`。因此，对任何
Euler--Tate package，只要其余 Weil/Hodge 公理已把 centerline 归约到这些 strata，
且 actual metric 的四个 canonical scalars `C_B,a,C_W,sigma` 满足式 (29)，其
zeta zeros 位于中心线。

#### 证明

把定理 TT 式 (19) 代入文档 100 定理 TM 的
`R_c(P)<=c_1+|t|sqrt((R+1)(1+A)/C_B)`，再应用文档 094 定理 SP。`□`

这是比文档 101 推论 TQ 更内在的结构条件：所有量均从 actual positive Hodge
metric 自动抽取，不再假设外部 completion decomposition。对经典 zeta，尚未证明
式 (29)；该 quantitative statement 仍可能具有 RH 的全部难度。

## 6. Finite Möbius--Farey audit

下表使用 exact `W^sp=W^[0,N^2]`。`old/A`、`first/A`、`short/A` 分别是
文档 101 式 `C_BF_0/kappa^2`、定理 TR 式 (5)、定理 TT 式 (19) 与 exact
`A` 的比。

| `N` | `R` | `A` | `kappa` | `sigma/kappa` | `old/A` | `first/A` | `short/A` | `aC_W` |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 10 | 2 | 675 | `3.01e-5` | 0.646 | 1.00 | 1.00 | 1.00 | 1.55 |
| 10 | 3 | 9506 | `1.33e-7` | 0.976 | 12262 | 23.5 | 15.1 | 1.59 |
| 20 | 3 | 2046 | `2.50e-7` | 0.992 | 15955 | 53.3 | 35.4 | 1.52 |
| 30 | 2 | 116 | `2.21e-5` | 0.950 | 1.00 | 1.00 | 1.00 | 1.05 |
| 30 | 3 | 46946 | `5.36e-7` | 0.633 | 32.5 | 1.29 | 1.16 | 1.75 |
| 50 | 3 | 880 | `3.60e-7` | 0.996 | 15582 | 74.6 | 49.8 | 1.51 |
| 100 | 2 | 19.3 | `2.05e-5` | 0.990 | 1.00 | 1.00 | 1.00 | 1.01 |
| 100 | 3 | 34598 | `1.06e-6` | 0.396 | 1.25 | 1.01 | 1.002 | 2.53 |

`R=2` 时 null space 一维，三个 bounds 均为等式。`R=3` 时 first-moment identity
把最坏松弛从约 `10^4` 降到 `10^1--10^2`；shorting 再有所改善。在最低 mode
高度主导的 `N=30,100` 样本，shorted bound 已几乎精确。

下表采用 `[0,N],[N,2N],...,[2^jN,N^2]` dyadic shells。`local%` 是
`sum_s sigma_s/sigma`，`disp%` 是 `sigma_Delta/sigma`，剩余部分来自 generalized
soft-direction rotation。

| `N` | `R` | `sigma` | `local%` | `disp%` | `rotation%` |
|---:|---:|---:|---:|---:|---:|
| 10 | 2 | `1.95e-5` | 94.9 | 5.09 | 0.00 |
| 10 | 3 | `1.29e-7` | 88.2 | 0.076 | 11.7 |
| 20 | 3 | `2.48e-7` | 73.7 | 0.058 | 26.2 |
| 30 | 2 | `2.10e-5` | 87.4 | 12.6 | 0.00 |
| 30 | 3 | `3.39e-7` | 72.9 | 0.455 | 26.6 |
| 50 | 3 | `3.59e-7` | 77.7 | 0.391 | 21.9 |
| 100 | 2 | `2.03e-5` | 86.9 | 13.1 | 0.00 |
| 100 | 3 | `4.21e-7` | 84.5 | 0.165 | 15.3 |

所以 actual transversal block 的大部分强度已经逐 shell 存在，并非仅由全局
coupling cancellation 偶然生成。然而其绝对 `sigma` 仍约为
`10^(-7)--10^(-5)`，不足以从当前有限数据推断式 (29) 的渐近尺度。

## 7. 下一存在性目标与计算实现

经典 RH 的下一目标现可选为：

1. 对 dyadic Möbius--Farey blocks 证明可求和的 lower bounds
   `sigma_s`, 再用定理 TU gluing；
2. 利用 determinant/cotangent structure 直接证明 shorted spectral second
   moment 在式 (18) 中受控；
3. 在 infinite metric 的文档 099 finite sandwich 下，传播 `a,C_W,sigma` 的
   双侧有限证书。

`scripts/qw_matrix.py` 的 alignment certificate 现新增 Green first moment、
effective slope、shorted metric/spectrum/forcing、两种强化 upper bounds。
`endpoint_transversal_hodge_shorting` 返回 maximal strength 与 residual metric；
`endpoint_spatial_shell_coercivity` 返回逐 shell shorted forms、coupling-slope
dispersion matrix、superadditive gain 与 rotation gain。回归测试核对全部 exact
identities、最大性和 shell gluing。
