# 从固定候选证书到 `lambda`-统一 RH 判据

文档 011 已把任意固定有限支撑候选的无限 residual 化为有限平方和与显式几何余项。本笔记解决下一个量词问题：要沿 `lambda_j->infinity` 进入 Hurwitz 路线，究竟需要哪些统一估计？同时补上连续 prolate 候选到有限 Fourier 候选之间的投影误差账本。

本文不假定数值趋势自动延续到 `lambda->infinity`。特别地，[2025 年原论文](https://arxiv.org/html/2511.22755)仍把 `k_lambda` 称为最低向量的 educated guess，并明确把二者的严格逼近列为主要缺口；[2021 年 prolate 构造](https://arxiv.org/html/2106.01715)说明全局 Weil radical 的输入须同时满足 `h(0)=hat h(0)=0`，而压缩 Fourier 特征值只近似 `+/-1`。

## 1. 半局部正弦项的无条件增长

沿用文档 011 的

`H_m=I_m+J_m`, `H_*=2+R_lambda+P_lambda`.               (1)

### 引理 AJ（`H_*` 的初等统一界）

当 `lambda>=2`、`L=2log(lambda)` 时，

`P_lambda<=2L(lambda-1)`,                              (2)

`R_lambda=O(log(2+L))`,                                (3)

从而

`H_*=O(lambda log(lambda))`.                           (4)

这些界不使用素数定理或 RH。

#### 证明

由 `Lambda(k)<=log k<=L` 及单调积分判别，

`P_lambda<=L sum_(2<=k<=lambda^2)k^(-1/2)`

`<=L int_1^(lambda^2)x^(-1/2)dx=2L(lambda-1)`，

得到式 (2)。另一方面

`rho(x)=e^(-x/2)/(1-e^(-2x))`。

函数 `rho(x)-1/(2x)` 在 `x=0` 有可去奇点，故其在 `(0,1]` 的绝对积分有统一常数界；对 `x>=1`，

`|rho(x)-1/(2x)|<=e^(-x/2)/(1-e^(-2))+1/(2x)`。

积分到 `L` 得到式 (3)。结合文档 009 的 `|H_m|<=H_*` 即得式 (4)。`□`

因此文档 011 的未计算远尾范数至多具有尺度

`O(R_*/T^(3/2)+lambda log(lambda) C_*/T^(5/2))`.        (5)

对每个固定有限候选，`T->infinity` 时 `R_*,C_*` 有界，故未计算尾可压到任意精度。真正需要统一证明趋零的是已经显式计算的 residual 与谱隙之比。

## 2. Fourier 投影及端点修正不会免费收敛

在长度 `L` 的圆上使用单位正交 Fourier 基 `V_n`。先设 `G` 是单位范数、偶、属于周期 `H^1` 且端点为零的连续候选，

`G=sum_n c_nV_n`, `D(G)=||partial_yG||_2`.              (6)

令

`epsilon_M=sum_(|n|<=M)c_n=-sum_(|n|>M)c_n`,           (7)

`G_M=P_MG-epsilon_MV_0`.                              (8)

则 `G_M` 严格有限支撑、偶且系数和为零，正是文档 007 与程序所用的代数修正。

### 引理 AK（投影–端点修正误差）

定义

`eta_(lambda,M)=L D(G)/(2pi)`

` *{1/(M+1)+sqrt(2/M)}`。                              (9)

则

`||G_M-G||_2<=eta_(lambda,M)`.                         (10)

若 `eta_(lambda,M)<1`，正规化向量 `f_M=G_M/||G_M||` 满足

`||f_M-G||_2<=2eta_(lambda,M)`.                        (11)

#### 证明

Parseval 给出

`sum_n n^2|c_n|^2=[L/(2pi)]^2D(G)^2`.                 (12)

所以

`||(1-P_M)G||_2<=L D(G)/[2pi(M+1)]`.                  (13)

又由 Cauchy–Schwarz 与

`sum_(|n|>M)n^(-2)<=2/M`，

`|epsilon_M|<=sqrt(2/M)L D(G)/(2pi)`.                 (14)

式 (10) 来自三角不等式。最后 `| ||G_M||-1|<=eta`，故

`||G_M/||G_M||-G||_2`

`<=|1-||G_M|||+||G_M-G||_2<=2eta`.                    (15)

`□`

结合文档 004 引理 M，一个充分的 cutoff 条件是：对每个 `a<1/2`，

`lambda^a eta_(lambda,M(lambda))->0`.                  (16)

若只知道 `D(G_lambda)`，式 (16) 就是选择 `M(lambda)` 的明确规则，而不是“取足够大的 Fourier cutoff”这一非定量说法。

这里有一项不可省略的正则性审计：2021 构造和本仓库程序把 prolate 模在 `[-lambda,lambda]` 外零延拓；若模在支撑端点不严格为零，`E(h_lambda)` 会在有限多个阈值处有极小跳跃，因而不自动属于周期 `H^1`。对原始零延拓候选，应改用一般误差

`tilde eta_(lambda,M)=||f_(lambda,M)-G_lambda||_2`,      (16a)

并单独证明其速率；或者先用光滑 cutoff 消去跳跃，再把 cutoff 误差记入 `tilde eta`。引理 AK 是后一类光滑候选的充分估计，不能在未证明正则性时直接替代式 (16a)。数值上的极小端点值支持这种平滑可能只造成极小扰动，但不构成证明。

## 3. Prolate 输入已有的指数小缺陷

设 `phi_(0,lambda),phi_(4,lambda)` 是归一化、零延拓的两个 self-Fourier 型 prolate 模，在 `[-lambda,lambda]` 上满足压缩 Fourier 关系

`P_lambda F phi_n=chi_n phi_n`, `n=0,4`,               (17)

其中 `chi_n>0` 且趋于 `1`。取

`h_lambda=a_lambda phi_0+b_lambda phi_4`               (18)

使 `hat h_lambda(0)=int h_lambda=0`。

### 引理 AL（零积分组合的另一边界缺陷）

若 `chi_4!=0`，则

`h_lambda(0)=a_lambda phi_0(0)(chi_4-chi_0)/chi_4`.     (19)

此外

`||Fh_lambda-h_lambda||_2`

`<=|a_lambda|sqrt(2(1-chi_0))`

`  +|b_lambda|sqrt(2(1-chi_4))`.                       (20)

#### 证明

压缩 Fourier 关系在零频给出

`int phi_n=chi_n phi_n(0)`。                           (21)

零积分条件是

`chi_0a phi_0(0)+chi_4b phi_4(0)=0`。

消去 `b phi_4(0)` 即得式 (19)。对单个支撑于区间内的单位模，区间内的 `Fphi_n-phi_n` 为 `(chi_n-1)phi_n`，区间外 Fourier 质量平方为 `1-chi_n^2`；两者正交，因此

`||Fphi_n-phi_n||_2^2=(1-chi_n)^2+1-chi_n^2`

`=2(1-chi_n)`.                                        (22)

对线性组合使用三角不等式得到式 (20)。`□`

原论文给出的 `n=4` 渐近为

`1-chi_4(lambda)~(2^14/3)sqrt(2)pi^5`

` *exp(-4pi lambda^2+9log lambda)`.                    (23)

由原论文的 Hermite 一致极限，`phi_(0,lambda)(0)` 也保持有界。因此只要组合系数保持有界，式 (19)–(20) 比任意 `lambda` 负幂衰减更快。这解释了为什么提高 Fourier 分辨率后 residual 持续急降，也把下一缺口精确定位为：需要把 `h_lambda(0)` 与 Fourier 泄漏的指数小量，经由 `E` 映射和半局部 Weil 算子，转成一个具有至多多项式损失的 operator-residual 估计。

文献已经说明 `E(S_0^ev)` 位于全局 Weil radical，并用上述 prolate 泄漏构造 near-radical；但它没有给出文档 004 式 (9) 所需的 uniform operator-residual/gap 比值。因此不能从式 (23) 直接宣布 quasimode 定理。

## 4. 完全有限可认证的 RH 充分判据

对一列 `lambda_j->infinity`，令 `G_j` 为正规化的偶、端点消失 prolate 参考候选（允许把零延拓产生的跳跃计入误差），`f_j` 为有限、偶、系数和为零的正规化 Fourier 候选，支撑半径为 `M_j`。定义

`tilde eta_j=||f_j-G_j||_2`.                            (23a)

若使用引理 AK 的光滑候选，则可取 `tilde eta_j<=2eta_(lambda_j,M_j)`。选 `K_j>=2M_j`、`T_j>=K_j` 与 Taylor 阶 `q_j>=1`。

令

`E_core,j=sum_(|m|<=K_j)`

` |sum_(|n|<=M_j)W_(m,n)c_(j,n)-mu_jc_(j,m)|^2`,      (24)

其中 `mu_j=<A_(lambda_j)f_j,f_j>`；令 `E_tail,j` 为文档 011 定理 AI 的 exact-resolvent 尾上界，并定义

`Delta_j=sqrt(E_core,j+E_tail,j)`.                     (25)

### 定理 AM（有限证书到 RH）

假设沿上述子列：

1. `A_(lambda_j)` 的最低特征值单重且最低向量 `xi_j` 为偶；并有经严格证书得到的

   `lambda_1(lambda_j)-mu_j>=g_j>0`;                   (26)

2. 对每个 `a<1/2`，

   `lambda_j^a tilde eta_j->0`;                        (27)

3. 对每个 `a<1/2`，

   `lambda_j^a Delta_j/g_j->0`;                        (28)

4. 乘以允许的非零正规化标量后，连续 prolate 候选的 Mellin 变换在开带中按文档 002/原论文收敛到 `Xi`，且文档 007 的规范反演–端点修正误差仍满足其已证明的 `O(lambda^(-1/2)sqrt(log lambda))` 界。

则 RH 成立。

#### 证明

由式 (23a) 与 residual/gap 引理，式 (25)–(26) 给出

`dist(f_j,Cxi_j)<=Delta_j/g_j`.                        (29)

因此选择适当相位与非零标量后，

`||c_jxi_j-G_j||_2<=tilde eta_j+Delta_j/g_j`.          (30)

式 (27)–(28) 和文档 004 引理 M 把式 (30) 升级为每个闭子带所需的指数加权 `L^1` 收敛。再加文档 007 的连续候选修正误差与原论文的 `hat G_j->Xi`，得到文档 002 定理 G 的全部假设；Hurwitz/Rouché 遂推出 RH。`□`

定理 AM 的意义不是把 RH 藏进新记号：

- `tilde eta_j` 是实际 Fourier/平滑误差；在周期 `H^1` 情形，引理 AK 把它控制为一个导数范数与显式 cutoff；
- `Delta_j` 只有有限矩阵元、有限正弦系数和几何余项；
- `g_j` 与 simple-even 可由文档 004 的有限 Schur/interval 条件认证。

剩余开放性恰在证明这些有限证书沿某列满足式 (27)–(28)，而不是无限尾或“截断应当收敛”的未经量化假设。

## 5. 固定 `lambda^2=13` 的分辨率审计

对同一规范 prolate 候选，提高 Fourier 半径并取 `K=2M,T=2K,q=6`，得到：

| `M` | 端点修正距离 | exact-resolvent 尾平方 | residual 下界 | residual 上界 |
|---:|---:|---:|---:|---:|
| 4 | `1.6464e-2` | `2.3918e-6` | `5.1223e-3` | `5.3507e-3` |
| 8 | `2.3468e-5` | `4.2007e-12` | `4.8598e-5` | `4.8641e-5` |
| 12 | `7.4632e-8` | `6.6695e-18` | `9.4403e-8` | `9.4439e-8` |
| 16 | `1.4545e-10` | `5.0777e-23` | `2.7725e-10` | `2.7734e-10` |

`M=16` 使用 100 个 Legendre 偶模，其余使用 80 个。四级 residual 与 Fourier 端点/投影修正同步下降；全阶远尾在 `M>=8` 后已明显不是主导误差。这是“连续 prolate 向量处于 near-radical”的强数值证据，与文献的机制一致。

但该表只改变 `M` 而固定 `lambda`，所以它证明的是 Fourier 离散化在收敛，不能证明式 (28) 的 `lambda->infinity` 速率，更不能提供未知谱隙 `g_lambda` 的下界。下一步应优先证明一个形如

`||(A_lambda-mu_lambda)G_lambda||_2`

`<=poly(lambda,log lambda)`

` *{|h_lambda(0)|+||Fh_lambda-h_lambda||_X}`            (31)

的 defect-to-residual 不等式，并独立给出不会比右端更快塌缩的 lowest spectral gap。若式 (31) 中只损失多项式，式 (19)–(23) 就会给出超多项式 quasimode 速率；这才可能满足定理 AM，而不是单靠更多固定参数数值。

文档 013 又给出一条更弱但可能更经济的替代桥梁：全局 radical 截断后的 Rayleigh 能量等于被截去的 Fourier leakage 能量；若能严格夹逼最低两谱值，则定理 AQ 不需要 operator residual。文档 014 进一步处理多个极小谱支：定理 AV 允许先认证低能谱簇，再在 near-radical trial space 内作 Weil–Ritz 旋转。当前应并行比较 AM、AQ 与 AV 的分母速率，而不是预先假定其中一条必定成功。
