# Ratio kernel、局部方差与每尺度二维 Hodge core

文档 046 把 triangular Abel energy 写成 signed prime current 的正 kernel，
但没有求出该 kernel。这里完成积分。结果不是一般的长程二维核，而是

`triangular kernel = max-kernel polarization - local variance defect`. (1)

defect 只耦合相同或相邻的 multiplicative scale。全部非相邻尺度耦合都
经过每块两个显式 moments。这把临界 tightness 问题严格降为“每尺度二维
core + block-tridiagonal centered remainder”。

## 1. 齐次 ratio profile 的闭式

沿用文档 046 的记号。令

`a=c+2sigma>0`, `M=max(u,v)`, `m=min(u,v)`, `z=m/M`. (2)

把 kernel (25) 的 `X` 下限由 `1` 换成 `0`，得到 tail kernel `K^0`。

### 定理 GZ（closed triangular ratio kernel）

有

`K^0_(sigma,q,c)(u,v)`

`=2sigma q^(-c-2) M^(-a) R_(a,q)(z)`,              (3)

其中 plateau value 为

`R_0=(q-1)(q^(a+1)-1)/[a(a+1)]`,                  (4)

而

`R_(a,q)(z)=R_0`,                    `0<z<=q^(-1)`, (5)

`R_(a,q)(z)`

`=q^(a+2)(a+2-az)/[a(a+1)(a+2)]`

` -(q-1)/[a(a+1)]-qz^(-a)/[a(a+1)]`

` +z^(-a-1)/[(a+1)(a+2)]`, `q^(-1)<z<=1`.         (6)

profile 在 `z=q^(-1)` 为 `C^2`，并且在第二段

`R'(z)=-z^(-a-2)[(qz)^(a+2)-(a+2)qz+(a+1)]`

`                         /[(a+1)(a+2)]<=0`.        (7)

所以 `0<R(z)<=R_0`，且

`R_0-R(z)=O((qz-1)^3)` 当 `z downarrow q^(-1)`.   (8)

#### 证明

由齐次性取 `M=1,m=z`。若 `z<=q^(-1)`，在 `X>=q^(-1)` 上较小 source
的 tent feature 恒为 `(q-1)X`。于是积分为

`(q-1)int_(1/q)^1 X^(-a-2)(qX-1)dX`

` +(q-1)^2int_1^infinity X^(-a-1)dX=R_0`.          (9)

若 `z>q^(-1)`，在 `[q^(-1),z]`、`[z,1]`、`[1,infinity]`
三段分别积分

`X^(-a-3)(qX-1)(qX-z)`,

`(q-1)X^(-a-2)(qX-1)`,

`(q-1)^2X^(-a-1)`,                                 (10)

化简即得式 (6)。代入 `z=q^(-1)` 并求导，函数值及前两阶导数与常数
分支相接；右三阶导数为 `-q^(a+4)`。式 (7) 中方括号是
`y^(a+2)-(a+2)y+(a+1)`，在 `y=qz>=1` 非负，证明单调性与式 (8)。`□`

plateau 是严格的，不是渐近：相差至少一个完整 multiplicative gap 的
sources 已完全失去较小位置的信息。

## 2. Max polarization 减局部正 defect

定义 plateau max-kernel

`P_(sigma,q,c)(u,v)=p_0 max(u,v)^(-a)`,             (11)

`p_0=2sigma q^(-c-2)R_0`,                          (12)

以及

`D_(sigma,q,c)=P_(sigma,q,c)-K^0_(sigma,q,c)`.     (13)

### 定理 HA（positive max-minus-local-variance decomposition）

`P,K^0,D` 都是正半定 kernels，并且

`K^0=P-D`,                                         (14)

`D(u,v)=0` whenever `min(u,v)/max(u,v)<=q^(-1)`.   (15)

若 `nu` 是有限 signed/complex current，`E(x)=nu((0,x])`，则

`<nu,D nu>=2sigma q^(-c-2)int_0^infinity X^(-a-3)`

` *{(q-1)X int_X^(qX)|E(x)|^2dx`

`                 -|int_X^(qX)E(x)dx|^2}dX>=0`.   (16)

#### 证明

`K^0` 是 tent features 的 Gram kernel。`P` 是正 max kernel；事实上

`max(u,v)^(-a)=a int_0^infinity`

`1_(u<=x)1_(v<=x)x^(-a-1)dx`.                     (17)

对式 (16) 的第一项交换 `X,x`，所得 kernel 恰为式 (11)–(12)；第二项
是 `K^0`。花括号由区间 `[X,qX]` 上的 Cauchy--Schwarz 非负，故 `D`
正半定。式 (15) 来自定理 GZ 的精确 plateau。`□`

所以文档 046 的 Hardy domination 实际是 Loewner 不等式

`0<=K^0<=P`;                                        (18)

其 gap 不是松弛常数，而是一个明确的局部 variance square。

## 3. Geometric blocks 的 semiseparable 结构

取 blocks

`I_j=[q^j,q^(j+1))`, `j=0,1,...`,                  (19)

并写 `nu_j=nu|_(I_j)`。定义两个 block moments

`beta_j=int_(I_j)dnu_j(u)`,

`alpha_j=int_(I_j)u^(-a)dnu_j(u)`.                 (20)

### 定理 HB（long-range coupling has one oriented channel）

若 `j>=k+2`，则

`<nu_j,K^0 nu_k>=p_0 alpha_j conjugate(beta_k)`.   (21)

因此全部 long-range Hermitian coupling 为

`2Re p_0 sum_(j>=2)alpha_j conjugate(B_(j-2))`,    (22)

`B_J=sum_(k=0)^J beta_k`.                          (23)

同时，local defect `D` 的 block matrix 严格 block-tridiagonal：

`<nu_j,D nu_k>=0` for `|j-k|>=2`.                  (24)

#### 证明

`j>=k+2` 时，对 `u in I_j,v in I_k` 有 `u>=qv`（端点零测集无关）。由
式 (3)–(5)，`K^0(u,v)=p_0u^(-a)`，积分即得式 (21)。对所有 ordered
pairs 求和给式 (22)。式 (15) 给式 (24)。`□`

式 (22) 是 semiseparable/prefix-sum coupling：它不是每对 blocks 各有
独立自由度，而是由一个 high weighted moment 与一个 low cumulative mass
通道承载。

## 4. 每尺度二维 core 的精确抽离

令 `L_j=q^j,R_j=q^(j+1)`。对给定 `alpha_j,beta_j`，定义

`A_j=[alpha_j-beta_j R_j^(-a)]/[L_j^(-a)-R_j^(-a)]`,

`B_j=[beta_j L_j^(-a)-alpha_j]/[L_j^(-a)-R_j^(-a)]`, (25)

以及 endpoint core 与 centered remainder

`nu_j^core=A_j delta_(L_j)+B_j delta_(R_j)`,

`tilde(nu)_j=nu_j-nu_j^core`.                       (26)

### 定理 HC（two-moment core plus nearest-neighbor remainder）

每个 remainder 满足

`int dtilde(nu)_j=0`,

`int u^(-a)dtilde(nu)_j=0`.                         (27)

若 `|j-k|>=2`，则任何含至少一个 centered remainder 的 cross term 都
为零：

`<tilde(nu)_j,K^0 nu_k>=<nu_j,K^0 tilde(nu)_k>=0`. (28)

所以完整 current space 精确分解为：

- 每个 scale 的二维 endpoint core，承载所有 long-range coupling；
- centered infinite-dimensional remainder，只保留同块和最近邻耦合。

#### 证明

式 (25) 是匹配 moments `(beta_j,alpha_j)` 的二乘二线性方程的唯一解，
故式 (27) 成立。远距离 ordered kernel 为 `p_0u^(-a)`：high remainder
由第二个 moment 消去，low remainder由第一个 moment 消去。`□`

这里的“二维”不是估计所得的有效秩，而是精确 algebraic quotient

`nu_j -> (beta_j,alpha_j)`.                         (29)

它与文档 030 的 endpoint rank-one channel 相呼应，但现在在每个几何尺度
成立，并且同时给出余空间的严格有限传播。

## 5. 临界 Hodge--Riemann domination 的新形式

对实际下限 `X>=1` 的 arithmetic kernel，低端只影响第零 block；所有
`j>=1` 的 tail 公式不变。记相应二次型为 `mathcal P_sigma`、
`mathcal D_sigma`、`mathcal J_sigma`。则

`mathcal J_sigma=mathcal P_sigma-mathcal D_sigma>=0`. (30)

### 定理 HD（local-variance saturation criterion）

对 zeta 的 current

`nu=-delta_1+sum Lambda(n)delta_n-dx`，RH 等价于

`mathcal D_sigma(nu)>=mathcal P_sigma(nu)-O(1)`

`                         as sigma downarrow0`.     (31)

更明确地，证明式 (31) 只需在 cofinal finite block truncations 上统一控制：

1. cores `(beta_j,alpha_j)` 的 semiseparable quadratic form；
2. centered remainders 的 block-tridiagonal form；
3. 两者之间只发生在同块/相邻块的 Schur coupling。

若还对 `d_h'` 的同类 forms 得到该控制，则定理 GV 产生连续
Hilbert--Pólya operator `Theta=1/2+iA`。

#### 证明

由式 (30)，式 (31) 等价于 `mathcal J_sigma(nu)=O(1)`。定理 GR 说明这
等价于 RH。定理 HB–HC 给出三项 finite block reduction；Sobolev 结论由
定理 GV。`□`

HD 仍不是 RH 的证明：式 (31) 是 arithmetic current 上接近饱和
Cauchy--Schwarz 的断言，具有 RH 的全部强度。但它把需要证明的全球正性
改写成一个 exact nearest-neighbor/二维-core 问题，不再需要控制任意
远尺度的无限维耦合。

## 6. 一般 Gamma--Euler 数据

### 定理 HE（general two-moment scale-core theorem）

定理 GZ–HC 对任意 `c>0`、`sigma>0`、`q>1` 及有限 complex
Gamma--Euler discrepancy current 原封不动成立。若该 datum 具有中心对称
divisor 与文档 GY 的显式公式，则其中心线结论等价于相应 arithmetic
current 的 local-variance saturation (31)；Sobolev 版本产生连续
dilation--de Rham Weil 复形。

#### 证明

GZ–HC 只使用参数 `a=c+2sigma`、tent features、Cauchy--Schwarz 和两个
block moments，不使用系数为实数或正数。中心线等价由定理 GT/GY。`□`

## 7. 存在性审计

现在无条件存在的对象包括：

- 每个 finite Euler truncation 的 `P,D,K=P-D` 三个正 matrices；
- defect `D` 的精确 block-tridiagonal sparsity；
- 每尺度二维 core `(beta_j,alpha_j)`；
- zeta 在 `sigma>=1/2` 的 infinite forms。

尚缺的是证明实际 von Mangoldt current 使 `D` 在临界极限几乎饱和 `P`。
这不能由 operator inequality `D<=P` 推出；它必须利用 primes 与 continuum
在每个 block 的联合相消。下一步最具体的量是 endpoint core 的
`2 x 2` block transfer/Schur recurrence，以及 centered remainder 的最近邻
large-sieve 下界。

### 数值公式审计

在临界 profile 参数 `a=1,q=2`，

| `z=m/M` | `R(z)` | `R_0-R(z)` |
|---:|---:|---:|
| 0.25 | 1.5 | 0 |
| 0.50 | 1.5 | 0 |
| 0.60 | 1.49629630 | 0.00370370 |
| 0.75 | 1.46296296 | 0.03703704 |
| 1.00 | 1.33333333 | 0.16666667 |

对 `sigma=0.35,c=1,q=2` 及 points `2,3,5,9`，`K^0` 的本征值为

`0.00048716, 0.00142856, 0.00518061, 0.04000353`,   (32)

而 `D=P-K^0` 的本征值为

`0.00046118, 0.00125210, 0.00296010, 0.00597342`.   (33)

脚本还用 tent integral 独立恢复闭式 kernel，并随机构造一个高尺度 signed
current；抽去式 (25) 的两个 endpoint moments 后，其非相邻尺度 coupling
在 60-digit 精度下为零。这些是公式/正性审计，不是临界 saturation 证据。
