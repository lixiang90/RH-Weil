# Weil 算子最低态的 simple-even 认证

本笔记直接研究 Connes–Consani–Moscovici 的半局部 Weil 二次型 `QW_lambda`。目标不是假定其最低态单重且为偶，而是把该结论化成有限矩阵、显式尾界和严格不等式。

## 1. 中心化对数坐标与偶奇分解

令 `ell=log(lambda)`，以 `y=log(u)` 把

`L^2([lambda^(-1),lambda],du/u)`

等距变成 `H=L^2([-ell,ell],dy)`。inversion `u->u^(-1)` 变成酉对合

`(Jf)(y)=f(-y)`。

论文的三类项都与 `J` 交换：

- archimedean 项在 Fourier 侧乘以偶实函数；
- 素数项是 partial translation 与其 adjoint 的和，而 `J S_a J=S_a^*`；
- 极点 `0,1` 的 rank-two 项在两个指数函数之间对称。

因此闭二次型 `QW_lambda` 满足 `QW_lambda(Jf,Jg)=QW_lambda(f,g)`，其关联自伴算子 `A_lambda` 与 `J` 强交换，并分解为

`A_lambda=A_lambda^+ direct_sum A_lambda^-`

作用在偶、奇子空间 `H^+`、`H^-` 上。

若使用论文的周期 Fourier 基 `V_n`，则 `J V_n=V_(-n)`。令

`E_0=V_0`, `E_n=(V_n+V_(-n))/sqrt(2)`,

`O_n=(V_n-V_(-n))/sqrt(2)` (`n>=1`)。

记 `W_(n,m)=QW_lambda(V_n,V_m)`。由 inversion 不变性，有限截面严格块对角化；在论文矩阵为实对称的约定下，

`W^+_(n,m)=W_(n,m)+W_(n,-m)`,

`W^-_(n,m)=W_(n,m)-W_(n,-m)` (`n,m>=1`)，且 `W^+_(0,m)=sqrt(2)W_(0,m)`。

这把 “even” 从对特征向量的事后观察变成两个独立变分问题：只需证明

`inf spec(A_lambda^+) < inf spec(A_lambda^-)`

并证明偶块最低特征值单重。

## 2. 一个阻止幼稚保正论证的符号事实

对 `f in H`，写

`C(f)=integral f(y)cosh(y/2)dy`,

`S(f)=integral f(y)sinh(y/2)dy`。

完成 zeta 函数的两个极点贡献为

`Q_(0,2)(f)=2 Re(hat(f)(i/2) overline(hat(f)(-i/2)))`

`=2(|C(f)|^2-|S(f)|^2)`.                                 (1)

所以：

- 若 `f` 偶，则 `Q_(0,2)(f)=2|C(f)|^2>=0`；
- 若 `f` 奇，则 `Q_(0,2)(f)=-2|S(f)|^2<=0`。

极点项单独看反而降低奇态能量。故 “算子反射对称，所以 ground state 偶” 不是证明；甚至不能直接把原始算子写成显然 positivity-improving 的 Schrödinger 算子。任何 Perron–Frobenius 路线都必须同时处理 archimedean multiplier、带负号的素数平移以及式 (1) 的不定 rank-two 扰动。

## 3. 一向量 simple-even 判据

### 定理 I（simple-even 变分认证）

令 `A` 为具有离散下有界谱的自伴算子，与酉对合 `J` 交换。记 `H^+`、`H^-` 为 `J` 的 `+1`、`-1` 子空间。若存在单位偶向量 `v`（在 form domain 中），令 `R=q(v,v)`，并且存在 `B_+,B_->R` 使

`q(x,x)>=B_+||x||^2` 对所有 `x in H^+` 且 `x perpendicular v`，

`q(y,y)>=B_-||y||^2` 对所有 `y in H^-`，

则 `A` 的最低特征值单重，且其特征向量为偶。

#### 证明

Rayleigh–Ritz 给出 `inf spec(A)<=R`。奇子空间的谱不低于 `B_->R`，故最低谱来自偶块。若偶块在 `B_+` 以下有两个计重数的特征值，则对应二维谱子空间中存在非零向量与 `v` 正交；其 Rayleigh quotient 小于 `B_+`，与第一条下界矛盾。因此 `B_+` 以下恰有一个偶特征值且重数为一。`□`

定理 I 的优点是无需先知道真正最低特征向量；`v` 可以取显式 prolate 候选 `k_lambda` 的正规化。

## 4. 有限块与尾部的可计算下界

### 引理 J（二乘二 Schur 型下界）

设 form domain 正交分解为 `U direct_sum V`，且

`q(u,u)>=a||u||^2`, `q(v,v)>=d||v||^2`,

`|q(u,v)|<=gamma||u||||v||`。

则

`q(u+v,u+v)>=L(a,d,gamma)||u+v||^2`，

其中

`L(a,d,gamma)=(a+d-sqrt((a-d)^2+4gamma^2))/2`.             (2)

#### 证明

把 `||u||,||v||` 记为两个非负标量，右侧最低可能值由实对称矩阵

`[[a,-gamma],[-gamma,d]]`

的最小特征值控制；该特征值正是式 (2)。`□`

现在令 `P_N` 为 `|n|<=N` 的周期 Fourier 截面，它与 `J` 交换。对奇块取

- `a_N^- = lambda_min(P_N^- A P_N^-)`；
- 高频尾下界 `d_N^-`；
- 低高耦合界 `gamma_N^-`。

引理 J 给出整个奇块的严格下界 `L(a_N^-,d_N^-,gamma_N^-)`。

对于偶块，选择单位测试向量 `v in P_N^+H`，把低频空间换成 `P_N^+H intersect v^perp`，同样得到 `a_N^(+,perp),d_N^+,gamma_N^+`。如果

`R < min(L(a_N^(+,perp),d_N^+,gamma_N^+), L(a_N^-,d_N^-,gamma_N^-))`,   (3)

定理 I 就给出连续算子 `A_lambda` 的 simple-even 性。式 (3) 是可以用 interval arithmetic 认证的有限不等式。

这里的耦合常数也能由论文的矩阵元素直接控制。若 `{u_j}` 是所选低频子空间的标准正交基，且这些基向量在 `D(A_lambda)` 中，则

`gamma_N^2 <= sum_j ||(1-P_N)A_lambda u_j||^2`

`=sum_j sum_(|m|>N)|QW_lambda(V_m,u_j)|^2`.                (3a)

第一个不等式是矩形算子的 Hilbert–Schmidt 上界。因而认证所需的无限信息只剩显式矩阵尾和；可以用解析衰减界包住，而不必把未知特征向量延伸到无限维。

文档 [005](005-matrix-tail-bound.md) 已从论文公式证明：对固定低模 `n`，先有初等平方尾 `O_(lambda,n)(log(N)^2/N)`；进一步分离无穷处核 `1/(2x)` 后改进为 `O_(lambda,n)(1/N)`，并给出完整显式常数。若低频维数随 cutoff 同时增长，则需使用核心、有限 buffer、远端尾三层分解，不能把逐行界误当成统一算子界。

## 5. 高频尾下界并非假设

下面给出一种从 archimedean multiplier 的增长导出 `d_N` 的方法。

令区间长度 `L=2ell`，周期频率 `omega_n=2pi n/L`，`P_N` 如上。使用单位 Fourier 变换 `F`。对 `T>0` 且 `omega_(N+1)>T`，定义

`kappa_N(T)^2 = (4T/(pi L)) sum_(|n|>N)(|omega_n|-T)^(-2)`. (4)

### 引理 K（高周期模态的低频泄漏）

若 `f in (1-P_N)H`，则

`||1_[-T,T] Ff|| <= kappa_N(T)||f||`。

#### 证明

单位周期模态 `e_n(y)=L^(-1/2)e^(i omega_n y)` 的 Fourier 变换满足

`|F e_n(t)| <= sqrt(2/(pi L))/(|omega_n|-T)` 对 `|t|<=T`。

算子 `1_[-T,T]F(1-P_N)` 的算子范数不超过 Hilbert–Schmidt 范数；对 `|n|>N` 求平方并在长度 `2T` 的区间积分，正得到式 (4)。`□`

设 archimedean 部分在单位 Fourier 侧为实 multiplier `w(t)`，其中 `w(t)->+infinity`；令

`m_0=inf_R w(t)`, `m_T=inf_(|t|>T)w(t)`。

其余极点与素数部分组成有界算子 `B_lambda`，`||B_lambda||<=C_lambda`。则引理 K 给出，对 `f in (1-P_N)H`，

`QW_lambda(f)>=d_N(T)||f||^2`,

`d_N(T)=m_T-(m_T-m_0)kappa_N(T)^2-C_lambda`.               (5)

这是因为 Fourier 质量至多有 `kappa_N(T)^2` 落在低频带，其余至少受到 `m_T` 的权重。

所有量都可无条件估计。一个很粗但显式的有界扰动界是

`C_lambda <= 2(lambda-lambda^(-1)) + 2 sum_(1<n<=lambda^2) Lambda(n)n^(-1/2)`,  (6)

第一项来自式 (1) 的 rank-two 算子范数，第二项使用 partial translation 的范数至多为 `1`。式 (6) 很松，但因 `m_T->infinity`，对固定 `lambda` 仍能令式 (5) 最终超过任意给定阈值。实际认证应使用矩阵元素和更紧的 operator/form bound，避免天文大的 `N`。

## 6. 从 residual 到 Hurwitz 所需加权收敛

### 引理 L（residual / gap 特征向量界）

设 `A` 的最低两个特征值为 `lambda_0<lambda_1`，最低单位特征向量为 `e_0`。若 `||f||=1`，

`mu=<Af,f><lambda_1`, `delta=||(A-mu)f||`，

则

`dist(f,C e_0) <= delta/(lambda_1-mu)`.                    (7)

#### 证明

按 `A` 的谱分解写 `f=sum_j c_j e_j`。对所有 `j>=1`，`|lambda_j-mu|>=lambda_1-mu`，故

`delta^2=sum_j |c_j|^2(lambda_j-mu)^2 >= (lambda_1-mu)^2 sum_(j>=1)|c_j|^2`。

最后一个和正是到最低特征直线的距离平方。`□`

### 引理 M（增长支集上的加权 `L^1` 升级）

设 `g_lambda` 支持于 `[lambda^(-1),lambda]`。对 `a>0`，

`integral |g_lambda(u)|(u^a+u^(-a))du/u`

`<= [2sinh(2a log(lambda))/a+4log(lambda)]^(1/2) ||g_lambda||_2`.  (8)

特别地，若 `||g_lambda||_2=o(lambda^(-a))`，则式 (8) 的左侧趋于零。

#### 证明

在 `y=log u` 中对 Cauchy–Schwarz 不等式应用权函数 `e^(ay)+e^(-ay)`。其平方在 `[-log(lambda),log(lambda)]` 上的积分恰为

`2sinh(2a log(lambda))/a+4log(lambda)`。

该量的平方根是 `O_a(lambda^a+sqrt(log(lambda)))`，得到最后结论。`□`

结合文档 002 的定理 G，若对某列 `lambda_j->infinity`，正规化 prolate 候选 `f_j` 满足

`mu_j=<A_(lambda_j)f_j,f_j><lambda_1(lambda_j)`

且对每个 `a<1/2`，

`delta_j/(lambda_1(lambda_j)-mu_j)=o(lambda_j^(-a))`,       (9)

则引理 L、M 给出定理 G 所需的指数加权 `L^1` 逼近。式 (9) 是比笼统的 “quasimode 很好” 更精确的最终估计目标。

## 7. 探索性数值结果（不是证明证书）

脚本 [qw_matrix.py](../scripts/qw_matrix.py) 直接实现论文 (3.13)、(4.1)–(4.4) 的矩阵公式，并在偶奇基中高精度对角化。对 `lambda=sqrt(13)`：

| cutoff `N` | lowest even | lowest odd | odd-even gap | next-even gap |
|---:|---:|---:|---:|---:|
| 8 | `7.6744e-23` | `3.9148e-20` | `3.9072e-20` | `9.6236e-18` |
| 12 | `2.1397e-29` | `1.4589e-26` | `1.4567e-26` | `4.6819e-24` |
| 20 | `1.5661e-39` | `2.1073e-36` | `2.1057e-36` | `1.5566e-33` |

`N=8` 的结果在 60 与 80 位工作精度下显示的数字一致，且矩阵满足 `W_(-n,-m)=W_(n,m)` 到计算精度。尽管绝对谱隙极小，最低偶值比最低奇值仍小约 `10^2`–`10^3` 倍，偶块内部下一谱值也明显更高。

这些数据只说明式 (3) 的方向与数值实验一致。普通高精度积分/对角化没有 directed rounding，不能充当严格证书；而且有限截面差距不能自动排除连续高频尾部产生更低奇态。

### 截面 ground state 的谱支不稳定

进一步把小截面最低偶向量零延拓到较大截面并计算 residual，得到：

| embedding | 小截面 Rayleigh 值 | 大截面 residual | 大截面中低于该值的特征值数 |
|---:|---:|---:|---:|
| `N=8 -> 12` | `7.6744e-23` | `8.7356e-13` | `2` |
| `N=12 -> 16` | `2.1397e-29` | `4.8143e-16` | `1` |

residual 比 Rayleigh 值大许多数量级，且增大 cutoff 会在其下插入新的极小特征值。因此这些小 `N` 的 “ground state” 并未稳定追踪同一个连续谱支；不能把表中最低值随 `N` 下降解释为最低特征值已经收敛。

这也说明定理 I 的测试向量应优先取连续定义的 prolate 候选 `k_lambda`，或取已经用 residual 和谱计数证明属于目标谱支的大截面向量。仅凭有限矩阵中“它是最小特征向量”不足以进入引理 L。

## 8. 得到的存在性推进与剩余目标

1. simple-even 已被化成严格的、非循环的有限截面条件 (3)，尾部由式 (4)–(6) 控制。
2. 只需沿某一列 `lambda_j->infinity` 完成认证，不必对每个实 `lambda` 证明；这足以配合文档 002 的定理 G 和 Hurwitz 极限。
3. 文档 005–016 已依次给出低高耦合衰减、候选 residual 证书、prolate 规范修正、二至四阶相消尾界、全阶 resolvent 证书、三类最低态判据、过滤渐近正性定理 BA/BB，以及素数图极化分解 BF。定理 BE 证明把素数平移逐项取 operator norm 必然留下 `2lambda+o(lambda)` 的负误差，所以当前优先路线是 BG：在 prolate near-radical 空间的正交补上联合证明 archimedean kinetic、素数图梯度与极点平方支配 degree 势；AW 保留为独立的行列式/Hurwitz 路线。
4. 即使 simple-even 沿子列成立，仍须证明 `xi_(lambda_j)` 与 `k_(lambda_j)` 的指数加权逼近；两者是独立缺口，不能用本笔记的谱型认证代替。
