# Prolate 候选的反演与端点缺陷

文档 006 证明：有限 Fourier 候选若为偶且系数和为零，其 Weil residual 平方尾从 `O(K^(-1))` 改善为 `O(log(K)^2/K^3)`。本笔记核对 Connes–Consani–Moscovici 的真实候选

`k_lambda(u)=E(h_lambda)(u),`

并解决两个不能跳过的问题：`k_lambda` 一般既不严格 inversion-even，也不严格端点为零。本笔记构造一个严格满足两条件的修正候选，并证明修正量具有 Hurwitz 路线所需的渐近速率。

## 1. 原始定义与容易混淆的三种“零”

令

`E(h)(u)=u^(1/2) sum_(n>=1) h(nu)`。                   (1)

论文取 `h_lambda` 为 prolate 算子在指标 `0,4` 的两个低态的线性组合，并要求

`integral_R h_lambda(x)dx=0`。                           (2)

这些 prolate 函数最初定义在 `[-lambda,lambda]`，用于 `E` 时向区间外零延拓。它们是**压缩 Fourier 变换**的特征函数：在 `|y|<=lambda` 上

`hat(h_(n,lambda))(y)=chi_n(lambda)h_(n,lambda)(y)`,      (3)

其中 `chi_n(lambda)->1` 极快，但对有限 `lambda`，不同指标的 `chi_n` 一般不相等。因此：

- 式 (2) 是 `hat(h_lambda)(0)=0`；
- 它不严格推出 `h_lambda(0)=0`；
- 它也不严格推出 `hat(h_lambda)=h_lambda` 或 `E(h_lambda)(u)=E(h_lambda)(u^(-1))`。

2021 年的原始 prolate 构造明确把 `f(0)=hat f(0)=0` 作为两个条件，并把 Fourier 特征值只写成近似 `+/-1`。故在证明中把“零积分”“原点为零”“自 Fourier”互换是不合法的。

## 2. `E` 的精确 Poisson 缺陷公式

采用 Fourier 变换

`hat h(y)=integral_R h(x)e^(2pi ixy)dx`。

### 定理 X（Poisson 反演缺陷）

设 `h,hat h` 足够衰减，使 Poisson 求和及以下级数成立。则

`E(h)(u)=E(hat h)(u^(-1))`

` +[u^(-1/2)hat h(0)-u^(1/2)h(0)]/2`.                  (4)

特别地，只有同时满足

`h(0)=hat h(0)=0`,                                      (5)

并且 `hat h=h` 时，才能推出 `E(h)(u)=E(h)(u^(-1))`。

#### 证明

Poisson 求和给出

`h(0)+2sum_(n>=1)h(nu)`

`=u^(-1)[hat h(0)+2sum_(m>=1)hat h(m/u)]`。

乘以 `u^(1/2)/2` 并按式 (1) 整理即得式 (4)。`□`

定理 X 精确定位了原始候选的奇部来源：一部分来自 `h_lambda(0)`，另一部分来自 `hat h_lambda-h_lambda`。二者虽可能极小，但不能在严格论证中删除。

## 3. 端点的精确表达与 Fourier 系数和

令 `L=2log(lambda)`，用论文的等距映射

`x=log(lambda u) in [0,L]`

把 `K_lambda(u)=E(h_lambda)(u)` 写成 `F_lambda(x)`。若 `h_lambda` 支持在 `[-lambda,lambda]`，则从区间内部取迹时

`K_lambda(lambda)=lambda^(1/2)h_lambda(lambda)`,           (6)

而

`K_lambda(lambda^(-1))=lambda^(-1/2)`

` *sum_(1<=n<=lambda^2)h_lambda(n/lambda)`，              (7)

其中上限按 `n/lambda<=lambda` 理解。

设 `c_n=<U_n,F_lambda>`，`U_n=L^(-1/2)e^(2pi inx/L)`。由于周期 Fourier 级数在端点取左右极限的平均值，若 `F_lambda` 分段 `C^1`，则其对称部分和满足

`lim_(M->infinity)sum_(|n|<=M)c_n`

`=sqrt(L)[K_lambda(lambda^(-1))+K_lambda(lambda)]/2`.     (8)

所以文档 006 的边界矩 `C_0=sum c_n` 对真实候选对应的不是单独的上端点，而是两个端点迹的平均值。

## 4. 严格偶且端点消失的修正

令 `Jf(u)=f(u^(-1))`，并定义

`K_lambda^+=(K_lambda+JK_lambda)/2`,

`b_lambda=[K_lambda(lambda^(-1))+K_lambda(lambda)]/2`,

`G_lambda(u)=K_lambda^+(u)-b_lambda`.                    (9)

### 定理 Y（规范修正）

`G_lambda` 严格满足

`JG_lambda=G_lambda`,

`G_lambda(lambda^(-1))=G_lambda(lambda)=0`.              (10)

并且

`||G_lambda-K_lambda||_2`

`<= (1/2)||JK_lambda-K_lambda||_2+sqrt(L)|b_lambda|`.    (11)

#### 证明

第一式由对称化定义立即得到。`K_lambda^+` 在两个端点的共同值正是 `b_lambda`，故减去常数后得到式 (10)。最后使用三角不等式；区间上常数 `b_lambda` 的 `L^2(d*u)` 范数是 `sqrt(L)|b_lambda|`。`□`

这个修正只使用反演、端点迹和常数函数，不涉及 zeta 零点，也不预设 Weil 最低态。

## 5. 用论文的 prolate 逼近估计修正量

论文给出一个极限 Hermite 组合

`h(t)=(pi/2)t^2(2pi t^2-3)e^(-pi t^2)`                 (12)

以及

`delta_lambda=sup_(|t|<=lambda)|h_lambda(t)-h(t)|`

`<=C lambda^(-2)`.                                      (13)

令 `k=E(h)`。由 `h(0)=hat h(0)=0`、`hat h=h` 和定理 X，`Jk=k`。为了补上逐点比较中常被省略的 `|t|>lambda` Gaussian 尾，定义

`A_lambda=sup_(t>=lambda)|h(t)|`,

`B_lambda=integral_lambda^infinity |h(t)|dt`,

`a_lambda=lambda delta_lambda+B_lambda`,

`d_lambda=A_lambda`.                                    (14)

对 `u in [lambda^(-1),lambda]`，单调积分估计给出

`|K_lambda(u)-k(u)|`

`<=a_lambda u^(-1/2)+d_lambda u^(1/2)`.                 (15)

这里第一项来自至多 `lambda/u` 个区间内采样点及 Gaussian 积分尾，第二项控制尾部的第一个采样点。`A_lambda,B_lambda` 都是 `e^(-pi lambda^2)` 乘一个多项式量级。

### 定理 Z（修正不破坏 Hurwitz 极限）

在式 (13) 下，

`||K_lambda-k||_2=O(lambda^(-1/2))`,                    (16)

`|b_lambda|=O(lambda^(-1/2))`,                          (17)

且

`||G_lambda-K_lambda||_2`

`=O(lambda^(-1/2)sqrt(log lambda))`.                    (18)

因此对每个固定 `a<1/2`，

`||G_lambda-K_lambda||_2=o(lambda^(-a))`.                (19)

#### 证明

把式 (15) 平方并在 `d*u=du/u` 下积分，得到显式界

`||K_lambda-k||_2^2`

`<=(a_lambda^2+d_lambda^2)(lambda-lambda^(-1))`

`+2a_lambda d_lambda L`.                                (20)

由式 (13)–(14)，`a_lambda=O(lambda^(-1))`，`d_lambda` 指数衰减，故式 (16) 成立。由于 `J` 酉且 `Jk=k`，

`||JK_lambda-K_lambda||_2<=2||K_lambda-k||_2`

`=O(lambda^(-1/2))`.                                    (21)

再在式 (15) 中分别取 `u=lambda,lambda^(-1)`，并使用 `k(lambda)=k(lambda^(-1))` 以及式 (12) 的 Gaussian 衰减，得到

`|b_lambda|<=|k(lambda)|`

` +(a_lambda+d_lambda)(lambda^(1/2)+lambda^(-1/2))/2`

`=O(lambda^(-1/2))`，证明式 (17)。把式 (17)、(21) 代入定理 Y 的式 (11) 得到式 (18)。最后

`lambda^a lambda^(-1/2)sqrt(log lambda)->0`

对每个 `a<1/2` 成立，故得式 (19)。`□`

## 6. 与文档 006 尾界的拼接

`G_lambda` 是连续层面的正确候选。为得到有限证书，取偶 Fourier 投影 `P_MG_lambda`，并令

`epsilon_(lambda,M)=sum_(|n|<=M)c_n`,

`G_(lambda,M)=P_MG_lambda-epsilon_(lambda,M)V_0`.         (22)

则 `G_(lambda,M)` 有限支撑、严格偶，且系数和严格为零；因此文档 006 的定理 V 给出 `O(log(K)^2/K^3)` residual 平方尾。式 (22) 的附加误差完全由 Fourier 投影尾与 `epsilon_(lambda,M)` 控制，可用推论 W 记账。

由定理 Z，把原论文的 `K_lambda` 换成 `G_lambda` 不会破坏文档 004–002 所需的任意 `a<1/2` 加权 Hurwitz 收敛速率。这消除了“为了获得更好尾界而改变候选，可能损坏 Xi 极限”的顾虑。

## 7. 真正剩余的估计

本笔记解决了候选的代数整形问题，但没有证明它接近 Weil 最低态。剩余任务现在是：

1. 对 `G_lambda` 或式 (22) 直接估计 `||(A_lambda-mu_lambda)G_lambda||`；
2. 认证 even 块第二特征值与 odd 块底部的统一下界；
3. 选择 `M(lambda),K(lambda)`，使投影误差、定理 V 尾界和谱隙比值共同满足文档 006 式 (8)。

与未修正 `k_lambda` 相比，这三项中不再混有隐藏的反演或端点主项；任何失败都会来自真正的 Weil/prolate 比较，而不是 Fourier 边界伪影。文档 012 的定理 AM 已进一步把三项所需的 `lambda`-统一速率写成显式有限证书条件，并指出零延拓 prolate 模的微小内部跳跃必须单独平滑或估计，不能未经审计地套用周期 `H^1` 投影界。

## 8. Legendre 谱计算的数量级审计

脚本 [prolate_candidate.py](../scripts/prolate_candidate.py) 在正交 Legendre 基中表示

`-d/dz((1-z^2)d/dz)+(2pi lambda^2)^2z^2`，

取其指标 `0,4` 的偶低态，并按零积分条件组成 `h_lambda`。`z^2` 在该基中是三对角的，因此可用任意精度对称特征值计算核对高度相消的端点值。

对 `lambda^2=13`，80 与 100 个偶 Legendre 模给出一致结果：

- prolate 特征值约为 `80.9290775234757982`、`724.217552992516293`；
- `K_lambda(lambda^(-1))约-1.1668602233e-29`；
- `K_lambda(lambda)约-1.6984403772e-29`；
- `b_lambda约-1.4326503003e-29`。

用普通浮点在对数区间求得 `||K_lambda||_2约0.46935`。因此正规化候选的 Fourier 边界矩

`sqrt(L)b_lambda/||K_lambda||_2`

量级约为 `4.9e-29`。相比之下，文档 006 中 Fourier cutoff `M=8` 的 Weil 矩阵最低向量边界矩约为 `4.5e-11`，大约高 `18` 个数量级。这是强烈的诊断证据：有限 Weil 截面的边界缺陷主要来自截断及谱支错配，而不是连续 prolate 候选本身。

这些数值没有 directed rounding，不能证明 `10^(-29)` 的严格 enclosure。其可信部分是：80、100 模结果稳定，低特征值也与 float64 计算一致；而压缩 Fourier 特征值与 `1` 的差更小，仍受 Galerkin 截断误差支配，脚本不把打印出的差值解释为真实渐近常数。
