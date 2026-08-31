# Balanced Schur cell-energy criterion

文档 108 把 unit-cell projection error 精确压缩到 directional Green energy

`G_E=e^*bar H^(-1)e`。

这个量保留 cross-cell cancellation，数值上很尖锐，但其渐近估计仍需要理解
`bar H^(-1)` 对 signed forcing `e` 的作用。本节给一个互补路线：只用两个正块
`E` 与 `epsilon bar W-E` 的 Cauchy--Schwarz，不求解 Green equation，便把
`G_E` 控制成 relative error 的二阶量。对 Möbius unit cells，所得 bound 只含
positive cell energy

`q_E=sum_m theta_m |C_m^*bar v|^2`。

它略牺牲 finite sharpness，却把文档 108 的 signed/vector obstruction 换成完全正的
scalar asymptotic problem。

## 1. Setup

沿用文档 108 的记号。令

`W=bar W+E`, `0<=E<=epsilon bar W`,              (1)

`bar v=argmin{v^*bar Wv:D^*v=1}`,                 (2)

并令 `Z` 的 columns 张成 `ker D^*`。记

`C_bar=(bar v^*bar Wbar v)^(-1)`,

`bar H=Z^*bar WZ`, `E_0=Z^*EZ`,

`e=Z^*Ebar v`, `q=bar v^*Ebar v`,                 (3)

以及

`G_E=e^*bar H^(-1)e`.                             (4)

由于 `Z^*bar Wbar v=0`，在 basis `[bar v,Z]` 中

`bar W = diag(C_bar^(-1),bar H)`,                 (5)

而 `E` 的 block matrix 是

`[[q,e^*],[e,E_0]]`.                              (6)

由式 (1)，

`0<=E_0<=epsilon bar H`, `0<=q<=epsilon/C_bar`.   (7)

## 2. Two-sided block Cauchy

### 定理 UV（balanced Schur--Cauchy bound）

在式 (1)--(7) 的条件下，

`G_E<=epsilon q`,                                 (8)

`G_E<=epsilon(epsilon/C_bar-q)`,                  (9)

从而

`G_E<=epsilon min{q,epsilon/C_bar-q}`             (10)

`    <=epsilon^2/(2C_bar)`.                       (11)

#### 证明

令 `x=bar H^(-1)e`，则 `G_E=e^*x=x^*bar Hx`。若 `G_E=0`，结论平凡。

首先，式 (6) 半正定所诱导的 block Cauchy--Schwarz 给

`|e^*x|^2<=q x^*E_0x`.                            (12)

由 `E_0<=epsilon bar H`，

`G_E^2<=q epsilon x^*bar Hx=epsilon qG_E`.        (13)

约去 `G_E` 得式 (8)。

其次，对同样半正定的 complementary block

`epsilon diag(C_bar^(-1),bar H)-E`

应用 Cauchy--Schwarz。它的 off-diagonal block 为 `-e`，故

`G_E^2<= (epsilon/C_bar-q)`

`          *x^*(epsilon bar H-E_0)x`              (14)

`       <=epsilon(epsilon/C_bar-q)G_E`。

约去 `G_E` 得式 (9)。式 (10) 取两者较小者；式 (11) 使用
`min(q,a-q)<=a/2`，其中 `a=epsilon/C_bar`。`□`

这个证明不要求 `E_0` 或 complementary block 可逆，因而也覆盖 rank-deficient
cell frames。

## 3. Second-order projection stability

令

`bar kappa=lambda_min(bar H,Z^*BZ)`               (15)

为 projected null endpoint coercivity，`C_B` 为 endpoint capacity。文档 108
证明 exact shift radius `eta_dir` 满足

`eta_dir^2<=C_BG_E/bar kappa`.                    (16)

### 定理 UW（balanced second-order stability）

定义

`eta_bal^2=(C_Bepsilon/bar kappa)`

`          *min{q,epsilon/C_bar-q}`。              (17)

则

`eta_dir<=eta_bal`，                              (18)

并且

`eta_bal^2<=C_Bepsilon^2/(2C_bar bar kappa)`.      (19)

若 `A_bar`、`A_W` 分别是 projected/actual endpoint excess，则

`sqrt(A_W)<=sqrt(A_bar)+eta_bal`.                 (20)

#### 证明

式 (18)--(19) 由定理 UV 代入式 (16)。式 (20) 再使用文档 108 定理 UR 的
reverse-triangle inequality。`□`

文档 107 的 uniform radius squared 是

`C_Bepsilon/(C_bar bar kappa)`。                  (21)

式 (19) 在 `epsilon<=1` 时至少多省 factor `epsilon/2`。更重要的是，式
(17) 使用 actual response cell energy `q`；当 error 主要落在 response block 或
其 complement 的一侧时，还会额外变小。

若只知道显式 majorant `E<=M<=epsilon_Pbar W`，定理仍可直接取
`epsilon=epsilon_P`。若 exact relative eigenvalue `epsilon_E` 可计算，则取
`epsilon_E` 给更尖锐版本。右侧关于合法的 `epsilon` 单调，因此
`epsilon_E<=epsilon_P` 自动给 nested certificates。

## 4. Positive unit-cell formula

对 Möbius unit-cell decomposition

`E=sum_m theta_m C_mC_m^*`,                       (22)

其中 `theta_m>0`，有

`q=sum_m theta_m |C_m^*bar v|^2`.                 (23)

与文档 108 的 current

`e=sum_m theta_m(Z^*C_m)(C_m^*bar v)`             (24)

不同，式 (23) 没有 signed cross-cell cancellation，也没有 inverse null operator；
每项均非负，适合 dyadic summation、large-sieve energy bound 或直接 determinant
majorization。

### 定理 UX（positive cell-energy centerline criterion）

令 `A_hat_bar` 是文档 106 的 projected three-capacity upper，并令
`epsilon_P` 由文档 107 的 Poincaré majorant 给出。定义

`q_P=bar v^*Ebar v`

`   =sum_m theta_m|C_m^*bar v|^2`,                (25)

`eta_P,bal^2=(C_Bepsilon_P/bar kappa)`

` *min{q_P,epsilon_P/C_bar-q_P}`,                 (26)

以及

`A_P,bal=(sqrt(A_hat_bar)+eta_P,bal)^2`.           (27)

则

`A_W<=A_P,bal`.                                   (28)

因此 minimum-`W` endpoint polynomial 满足

`R_c(P)<=c_1+|target|`

`          *sqrt((R+1)(1+A_P,bal)/C_B)`.          (29)

若式 (29) 是

`o(sqrt(log N)/loglog(3N))`,                       (30)

则 fixed reduced-determinant principal strata 全部为 `o(1)`；在其余
Euler--Tate/Weil package 公理下，相应 zeta function 的 zeros 位于中心线。

#### 证明

式 (22) 给式 (23)。因为 `E<=M_P<=epsilon_Pbar W`，定理 UW 给
`sqrt(A_W)<=sqrt(A_bar)+eta_P,bal`。projected centered susceptibility 给
`A_bar<=A_hat_bar`，于是得到式 (28)。把它代入文档 100 定理 TM 与文档 094
定理 SP，即得式 (29)--(30) 的结论。`□`

## 5. Finite audit

下表使用与文档 108 相同的 exact spatial metric `W^[0,N^2]`。`epsilon_P` 是
Poincaré majorant relative bound；`q` 是式 (23)；`eta_bal` 使用式 (26)；最后
一列是式 (27) 对 actual excess 的倍率。

| `N` | `R` | `epsilon_P` | `q` | `eta_bal` | `A_P,bal/A_W` |
|---:|---:|---:|---:|---:|---:|
| 10 | 2 | 0.0196 | 3.99e-4 | 0.198 | 1.135 |
| 10 | 3 | 0.0252 | 3.14e-4 | 3.483 | 1.367 |
| 20 | 3 | 0.0204 | 3.02e-4 | 2.340 | 1.380 |
| 30 | 2 | 0.0116 | 1.29e-3 | 0.312 | 1.315 |
| 30 | 3 | 0.0195 | 3.47e-4 | 1.624 | 1.129 |
| 50 | 3 | 0.0164 | 2.65e-4 | 1.603 | 1.344 |
| 100 | 2 | 0.00894 | 1.92e-3 | 0.236 | 1.527 |
| 100 | 3 | 0.0148 | 1.33e-4 | 0.578 | 1.048 |

所以不使用 signed Green cancellation 的完全正 certificate 仍只松
`1.048--1.527`。它略弱于文档 108 direct Green certificate 的 `1.04--1.46`，但
远优于文档 107 一阶 uniform certificate 的 `1.25--7.08`。

## 6. 对经典 RH 的新分叉

现在有两条互补的充分路线：

1. **directional route**：直接证明
   `G_E=e^*bar H^(-1)e` 很小，保留全部 cross-cell cancellation；
2. **positive route**：证明
   `epsilon_P min(q,epsilon_P/C_bar-q)/bar kappa` 很小，只处理 positive
   cell energies。

第二条路线不再要求估计 signed vector current。其尚未证明的经典 RH 输入是

`sqrt(A_hat_bar)`

` +sqrt[(C_Bepsilon_P/bar kappa)`

`        *min(q,epsilon_P/C_bar-q)]`

` =o(sqrt(log N)/loglog(3N))`.                     (31)

式 (31) 仍是充分条件而不是已完成的 RH 证明；关键任务变为联合估计 projected
susceptibility、positive cell energy `q` 与 null coercivity `bar kappa` 的渐近率。

## 7. 计算实现

`endpoint_projection_alignment_stability_certificate` 现返回 exact/majorant 两种
complementary Schur energy upper、balanced Schur energy upper、对应 radii 与
excess uppers。回归测试验证

`G_E <= balanced upper <= complementary upper`,

exact-relative certificate 不劣于 Poincaré-majorant certificate，并覆盖 null
dimensions 1 与 2。
