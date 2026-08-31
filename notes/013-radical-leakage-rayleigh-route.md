# Radical leakage 与不使用 operator residual 的 Rayleigh 路线

文档 012 的定理 AM 使用

`dist(f_lambda,C xi_lambda)<=Delta_lambda/g_lambda`

把 operator residual 转成最低向量逼近。但固定 `lambda^2=13,M=16` 的探索值为

`mu=2.68e-20`, `Delta=2.77e-10`。

Rayleigh 值比 operator residual 小十个数量级，说明 residual 路线可能付出了不必要的导数/高频代价。本笔记利用 `E(S_0^ev)` 位于全局 Weil radical 这一结构，给出另一条只需 Rayleigh 值和谱夹逼的路线。

## 1. Fourier 泄漏如何变成乘法下尾

对函数 `r` 定义

`E(r)(v)=v^(1/2)sum_(n>=1)r(nv)`.                      (1)

### 引理 AN（`E` 的加权尾转移）

令 `lambda>0`、`epsilon>0`，且

`int_lambda^infinity x^(1+epsilon)|r(x)|^2dx<infinity`。

则

`||E(r)||^2_(L2((lambda,infinity),dv/v))`

`<=zeta(1+epsilon)lambda^(-1-epsilon)`

` *int_lambda^infinity x^(1+epsilon)|r(x)|^2dx`.        (2)

#### 证明

由带权 Cauchy–Schwarz，

`|sum_n r(nv)|^2`

`<=zeta(1+epsilon)sum_n n^(1+epsilon)|r(nv)|^2`.       (3)

注意 `|E(r)(v)|^2dv/v=|sum_nr(nv)|^2dv`。积分并令 `x=nv`，得到

`sum_n n^epsilon int_(n lambda)^infinity|r(x)|^2dx`

`=int_lambda^infinity|r(x)|^2`

` *sum_(n<=x/lambda)n^epsilon dx`.                     (4)

对 `X>=1` 使用 `sum_(n<=X)n^epsilon<=X^(1+epsilon)`，即得式 (2)。`□`

现在令 `h` 为满足 `h(0)=hat h(0)=0` 的偶 Schwartz 函数。Poisson 公式给出

`E(h)(u)=E(hat h)(u^(-1))`.                            (5)

若 `h` 支撑于 `[-lambda,lambda]`，则 `E(h)` 在 `u>lambda` 为零。令

`r_lambda=(1-P_lambda)hat h`。                         (6)

当 `v>lambda` 时，所有 `nv>lambda`，故

`E(hat h)(v)=E(r_lambda)(v)`.                          (7)

由 `u=v^(-1)` 及引理 AN，得到严格的下尾界

`||1_(0,lambda^(-1))E(h)||_2^2`

`<=zeta(1+epsilon)lambda^(-1-epsilon)`

` *int_lambda^infinity x^(1+epsilon)|hat h(x)|^2dx`.   (8)

因此同时支撑/带限的 prolate 缺陷确实定量控制 `E(h)` 落在目标乘法区间之外的部分；这里没有使用 RH。

## 2. 截断 near-radical 的能量恒等式

设 `QW` 是全局 Weil sesquilinear form，其 radical 包含 `E(S_0^ev)`。这正是 prolate near-radical 构造所用的一手输入。令

`r=E(h)`, `I_lambda=[lambda^(-1),lambda]`,

`g=1_(I_lambda)r`, `w=r-g`.                            (9)

若 `h` 支撑于 `[-lambda,lambda]`，则 `r` 没有 `u>lambda` 的上尾，所以 `w` 就是式 (8) 的下尾。

### 命题 AO（radical truncation identity）

假设 `r,w` 均在 `QW` 的 form domain，且 `r` 位于 radical，即

`QW(r,v)=0` 对所有 form-domain `v`。                   (10)

则

`QW_lambda(g,g)=QW(w,w)`.                              (11)

#### 证明

`g=r-w`，而 `QW(r,r)=QW(r,w)=QW(w,r)=0`。因此

`QW(g,g)=QW(r-w,r-w)=QW(w,w)`.                         (12)

由于 `g` 支撑于 `I_lambda`，左端正是半局部限制 `QW_lambda(g,g)`。`□`

式 (11) 给出“prolate 向量为何具有极小 Rayleigh 值”的精确结构解释：能量不是来自区间内部各巨大局部项分别很小，而是全局 radical 被截断后只剩 Fourier leakage 的能量。

要把式 (8) 直接转成 `|QW(w,w)|` 的数值上界，还需一个明确的 form-continuity 估计，例如

`|QW(w,w)|<=C_(lambda,s)||w||_(H^s_weighted)^2`.        (13)

引理 AN 控制其中的 `L^2` 部分；prolate 的光滑性可望控制高阶加权部分。式 (13) 的至多多项式常数是当前 defect-to-Rayleigh 缺口。它比文档 012 式 (31) 的 defect-to-operator-residual 更弱，也更符合现有极小 Rayleigh 数值。

此外，2025 年两模候选只严格满足 `hat h(0)=0`，其 `h(0)` 由文档 012 引理 AL 指数控制。可选择一个固定的偶光滑紧支撑函数 `psi`，满足 `psi(0)=1,int psi=0`，并用

`tilde h=h-h(0)psi`                                    (14)

把输入修正到 `S_0^ev`；式 (14) 的扰动与 `h(0)` 同阶。若同时平滑零延拓端点，则这些误差也必须进入式 (13)，不能把“指数小”误写成“严格为零”。

## 3. 谱夹逼优于 residual/gap 的情形

### 引理 AP（Rayleigh–双谱夹逼）

令 `A` 为下有界自伴算子，最低两谱值为

`lambda_0<lambda_1`，最低单位向量为 `e_0`。令 `||f||=1`、`mu=<Af,f>`。若有严格证书

`L_0<=lambda_0`, `lambda_1>=B_1>mu`,                   (15)

则

`dist(f,C e_0)^2<= (mu-L_0)/(B_1-mu)`.                 (16)

#### 证明

文档 002 引理 H 给出

`dist(f,C e_0)^2<=(mu-lambda_0)/(lambda_1-lambda_0)`.  (17)

由 `lambda_0<=mu`，分子不超过 `mu-L_0`，分母满足

`lambda_1-lambda_0>=B_1-mu`，

得到式 (16)。`□`

引理 AP 只需要 Rayleigh 值以及最低、第二谱值的外侧夹逼，不需要计算 `Af`。这正适合命题 AO：near-radical 机制天然先控制二次型能量，而不是 operator graph norm。

## 4. Rayleigh 有限证书到 RH

沿用文档 012 的连续参考候选 `G_j`、有限 Fourier 候选 `f_j`、投影/平滑误差

`tilde eta_j=||f_j-G_j||_2`，以及 `lambda_j->infinity`。

令

`mu_j=QW_(lambda_j)(f_j,f_j)`.                         (18)

### 定理 AQ（不使用 operator residual 的 RH 判据）

假设沿某子列：

1. 通过文档 004 的偶奇分块及 Schur/interval 证书，证明最低谱值 `lambda_(0,j)` 单重且最低向量 `xi_j` 为偶；
2. 同一证书给出

   `L_j<=lambda_(0,j)`, `lambda_(1,j)>=B_j>mu_j`;      (19)

3. 对每个 `a<1/2`，

   `lambda_j^a tilde eta_j->0`,                        (20)

   `lambda_j^a sqrt[(mu_j-L_j)/(B_j-mu_j)]->0`;        (21)

4. 连续 prolate 候选经允许的非零标量正规化后，其 Mellin 变换在开临界带内局部一致趋于 `Xi`，且文档 007 的规范修正误差满足既有速率。

则 RH 成立。

#### 证明

由引理 AP，可选择相位使

`||f_j-xi_j||_2<=sqrt[(mu_j-L_j)/(B_j-mu_j)]`.         (22)

再与 `||f_j-G_j||_2=tilde eta_j` 合并。式 (20)–(21) 及文档 004 引理 M 给出最低向量与连续 prolate 候选的指数加权 `L^1` 收敛。最后完全同文档 002 定理 G，最低向量 Fourier–Mellin 变换的零点均在实轴，局部一致极限为 `Xi`，Hurwitz/Rouché 推出 RH。`□`

定理 AQ 与定理 AM 是两条独立可选的有限证书路线：

- AM：证明 `operator residual / gap` 很小；
- AQ：证明 `Rayleigh bracket / gap` 很小。

对于当前 prolate 数据，AQ 更贴合已观察尺度；但它要求最低谱下界 `L_j` 非常接近真实底部，不能把未经证明的 `QW_lambda>=0` 当作 `L_j=0`。若直接假设所有 `lambda` 的 Weil 正性，就会循环回 RH。合法做法是对选定子列用文档 004 的有限 interval/尾证书逐个证明式 (19)，再证明其统一率。

## 5. 数值尺度与下一步

固定 `lambda^2=13` 时：

| `M` | Rayleigh `mu_M` | 完整 residual 上界 | 有限最低态平方重叠 | 低于 `mu_M` 的有限偶特征值数 |
|---:|---:|---:|---:|---:|
| 4 | `1.1851e-5` | `5.3507e-3` | `0.92972` | 3 |
| 8 | `9.2426e-10` | `4.8641e-5` | `0.98488` | 3 |
| 12 | `3.6144e-15` | `9.4439e-8` | `0.99527` | 3 |
| 16 | `2.6806e-20` | `2.7734e-10` | `0.99825` | 3 |

Rayleigh 值随分辨率下降得显著快于 operator residual，且候选对有限最低态的重叠趋近 `1`，这两点支持优先研究命题 AO 后的 form-continuity 与谱支锁定。另一方面，四个已审计截面中始终有三个偶特征值低于 `mu_M`，所以定理 AQ 要求的 `B_j>mu_j` 在这些有限矩阵上**尚不成立**。小量 Rayleigh 和高 ground-state overlap 不能替代第二谱值排序。

这些仍是普通高精度数据；有限截面会插入新的极小谱支，不能用小矩阵的第二特征值直接充当式 (19) 的连续 `B_j`。要挽救 AQ，必须证明这些额外低支在无限维认证中被排除/重新排序，或把定理推广为先认证一个低能谱簇、再用额外结构在簇内锁定目标向量。文档 014 已完成后一抽象步骤：定理 AT/AV 用 trial space 内的 Weil–Ritz 旋转与簇外耦合识别最低直线，并证明只知道谱簇几何逼近在逻辑上不够。仅增加数值精度没有解决这个问题。

下一项最具体的分析目标是二选一：

1. 证明式 (13)，把 prolate Fourier 泄漏的指数界转成 `mu_j` 的统一上界；
2. 用文档 004 的三层 Schur 分解同时给出 `L_j` 与 `B_j`，检查式 (21) 是否可能成立。

若第二项失败，例如 `B_j-mu_j` 比 leakage 能量更快塌缩，则 AQ 路线被严格排除，仍可回到 AM 的 operator residual 路线；两者不会互相掩盖失败。
