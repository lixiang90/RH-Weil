# 素数相位 resonance 的均方与密度界

文档 017 把 zeta 的正 prime-graph multiplier 写成

`G_lambda(t)=4sum_(k<=lambda^2)w_k sin^2(t log(k)/2)`,

`w_k=Lambda(k)/sqrt(k)`.                               (1)

要证明算术 Hodge–Riemann domination，需要理解 `G_lambda(t)` 何时显著
小于其自然均值 `2P_lambda`。本笔记给出一个完全无条件的第一步：强
resonance 在任何足够长有限窗口中具有趋零的相对测度。证明只使用 Dirichlet
多项式的直接均方展开、素数定理和初等调和和估计。

## 1. resonance 等价于 Dirichlet 多项式偏大

令 `x=lambda^2`，

`P(x)=sum_(k<=x)w_k`,

`F_x(t)=sum_(k<=x)w_k exp(it log k)`.                   (2)

### 引理 BN（prime graph–phase identity）

`G_lambda(t)=2P(x)-2Re F_x(t)`.                         (3)

#### 证明

使用 `4sin^2(theta/2)=2-2cos(theta)` 逐项求和。`□`

脚本函数 `prime_phase_sum` 与 `prime_graph_symbol` 分别计算式 (2)–(3)，
回归测试在多个频率上直接核对恒等式。

因此对 `0<theta<1` 定义强 resonance 集

`R_x(T,theta)={t in [-T,T]:Re F_x(t)>=theta P(x)}`.     (4)

在其补集上有

`G_lambda(t)>=2(1-theta)P(x)`.                          (5)

## 2. 一个自足的有限窗口均方界

记

`B_2(x)=sum_(k<=x)w_k^2`, `H_x=sum_(1<=h<=x)1/h`.      (6)

### 引理 BO（初等 Dirichlet 多项式均方界）

对每个 `T>0`，

`int_(-T)^T |F_x(t)|^2dt`

`<=(2T+4xH_x)B_2(x)`.                                  (7)

#### 证明

展开平方。对角项为 `2T B_2(x)`。若 `m<n`，相应两个共轭非对角项的积分
绝对值之和不超过

`4w_mw_n/log(n/m)`.

由 `log(n/m)>= (n-m)/n >=(n-m)/x`，非对角总和至多

`4x sum_(m<n)w_mw_n/(n-m)`.                            (8)

使用 `2w_mw_n<=w_m^2+w_n^2`。对每个固定指标，左右距离的倒数和至多
`2H_x`，所以式 (8) 不超过 `4xH_xB_2(x)`。`□`

这个常数不是最优；使用 Montgomery–Vaughan 型均值定理可去掉多余的
`H_x`，但式 (7) 已足够证明密度趋零，而且没有调用任何零点信息。

## 3. resonance 相对测度趋零

### 定理 BP（prime resonance density bound）

对 `0<theta<1`，

`|R_x(T,theta)|/(2T)`

`<=(1+2xH_x/T) B_2(x)/(theta^2 P(x)^2)`.               (9)

特别地，若 `theta` 固定且 `T>=2xH_x`，则

`|R_x(T,theta)|/(2T)=O(log^2(x)/x)`

`                         =O(log^2(lambda)/lambda^2)`. (10)

#### 证明

在 `R_x(T,theta)` 上，`|F_x(t)|^2>=theta^2P(x)^2`。
Chebyshev 不等式与引理 BO 给出式 (9)。由素数定理和分部求和，

`P(x)=2sqrt(x)+o(sqrt(x))`.                            (11)

另一方面，prime powers `p^m,m>=2` 对 `B_2` 的总贡献有界，而

`sum_(p<=x)(log p)^2/p=(1/2)log^2x+o(log^2x)`,         (12)

故 `B_2(x)=(1/2)log^2x+o(log^2x)`。代入式 (9)。`□`

所以固定比例的高相干 prime phases 在长窗口中极稀疏；对绝大多数频率，
prime graph 本身已贡献接近 `2P_lambda` 的 kinetic mass。

## 4. 酉扭曲 Euler 数据的同一结论

设 primitive Dirichlet character 的多项式为

`F_(x,chi)(t)=sum_(k<=x,(k,q)=1)w_k chi(k)k^(it)`.     (13)

因为 `|chi(k)|=1` 于 unramified 项，引理 BO 的证明逐字成立，`B_2` 不变，
而缺失有限个 prime 的主质量不改变式 (10) 的阶。

更一般地，若 degree `d` 的 tempered Euler coefficient 是 `d` 个单位相位
之和，则对每条相位分别应用均方界，或使用 Cauchy 得到至多 `d^2B_2`；
总 edge mass 是 `dP(x)`，所以固定 `d` 时式 (10) 的阶仍不变。

### 推论 BQ（unitary Euler resonance density）

定义 BK 的固定 degree 酉 Euler 数据，其强相干 twisted-prime resonance
在 `T>=2xH_x` 的窗口中具有 `O_d(log^2x/x)` 的相对测度。

该推论是局部纯性第一次产生的**全球定量收益**：不仅每条 edge 是正平方，
而且大量不同 prime phases 除了稀疏 resonance 外会共同提供宏观 coercivity。

## 5. 为什么密度界尚未证明 RH

式 (10) 控制相对测度，不控制所有 resonance 分量的总绝对长度和排列。
archimedean multiplier 要单独压过 `2P_lambda~4lambda`，需到非常大的
`|t|`；在这样巨大的窗口中，即便相对密度为 `O(log^2lambda/lambda^2)`，
坏集的绝对测度仍可很大。

时间支撑长度为 `2log lambda` 的 Fourier 变换不能集中在单个很短区间，
但可能在许多分离的 resonance 窗口间分配质量。因此下面的错误推理必须
排除：

`resonance density ->0  => Fourier mass on resonance ->0`. (14)

要从 BP 到定理 BG，还需至少一种更强输入：

1. 对每个单位长度/对数长度窗口的**局部** resonance 测度界；
2. resonance 中心的分离及宽度界，结合 Logvinenko–Sereda/Nazarov 型
   不确定性；
3. 对带权 Fourier 质量 `|hat f(t)|^2dt` 直接成立的大筛不等式；
4. 把低频 resonance 投影到有限个 prolate 模态，并由 `C,S` 锚逐个认证。

下一步最具体的目标是第 3 项：证明某个 time-limited large-sieve bound

`int_(R_x) |hat f(t)|^2dt/(2pi)`

`<=rho_lambda||f||^2+finite-rank anchor terms`,         (15)

其中 `rho_lambda->0`。若能做到，式 (5) 与 archimedean 高参数控制即可合成
文档 017 的全球 domination。

## 6. 不可消失的中心 resonance 井

记第二对数矩

`M_2(x)=sum_(k<=x)w_k(log k)^2`.                        (16)

### 引理 BR（中心 resonance 的强制宽度）

对所有实 `t`，

`G_lambda(t)<=t^2M_2(x)`.                              (17)

并且

`M_2(x)=2sqrt(x)log^2x(1+o(1))`.                       (18)

因此式 (4) 的 resonance 集必定包含中心区间

`[-r_(x,theta),r_(x,theta)]`,

`r_(x,theta)=sqrt(2(1-theta)P(x)/M_2(x))`

`             =sqrt(2(1-theta))/log x*(1+o(1))`.       (19)

#### 证明

由 `4sin^2(u/2)<=u^2` 逐项得到式 (17)。对
`sum Lambda(k)k^(-1/2)(log k)^2` 使用素数定理的 Stieltjes 分部求和，
主积分是

`int_1^x t^(-1/2)(log t)^2dt`

`=2sqrt(x)log^2x(1+o(1))`,                             (20)

得到式 (18)。当 `|t|<=r_(x,theta)` 时，式 (17) 不超过
`2(1-theta)P(x)`；结合引理 BN 即有 `Re F_x(t)>=theta P(x)`。`□`

所以强 resonance 的全局密度虽趋零，中心处永远存在一口自然宽度
`1/log x` 的井。

## 7. 该宽度恰是 prolate 临界尺度

测试函数在中心坐标的支撑区间长度为

`L=2log lambda=log x`.                                 (21)

中心井的 time–bandwidth product 是

`c_(x,theta)=(L/2)r_(x,theta)`

`             ->sqrt((1-theta)/2)`.                    (22)

它既不趋零也不趋无穷，而是固定 prolate 参数。

### 命题 BS（纯测度法不能移除中心井）

存在支撑于长度 `L` 区间的单位函数，其 Fourier 质量落在式 (19) 中心井内
的比例保持为正，不随 `x->infinity` 消失。

#### 证明

取区间上的归一化常数函数 `f=L^(-1/2)`，零延拓。其 Fourier 变换为

`hat f(t)=2sin(tL/2)/(t sqrt L)`.                       (23)

中心井中的质量为

`(1/(2pi))int_(-r)^r|hat f(t)|^2dt`

`=(2/pi)int_0^c (sin u/u)^2du`,                        (24)

其中 `c=Lr/2`。由式 (22)，右端趋于严格正的常数。`□`

这给出式 (14) 失败的一个显式见证。常数方向同时被极点锚 `C(f)` 强烈
检测，所以正确结论不是中心井不可控，而是它必须由有限秩锚/prolate 模态
单独控制，不能交给 density estimate。

## 8. 中心井可由有限秩 prolate 投影严格剥离

令 `K_c` 是“限制到长度 `L` 的时间区间，再限制 Fourier 频率到
`[-r,r]`”的 concentration operator。其特征值记为

`1>chi_0(c)>=chi_1(c)>=...->0`,                         (25)

对应 prolate 特征函数 `phi_n^(c)`。

### 定理 BT（central-resonance prolate removal）

若 `f` 与前 `R` 个 `phi_0^(c),...,phi_(R-1)^(c)` 正交，则

`(1/(2pi))int_(-r)^r|hat f(t)|^2dt`

`<=chi_R(c)||f||^2`.                                   (26)

对式 (19) 的 `c=c_(x,theta)`，任取 `R(x)->infinity`，右端一致趋于 `0`。

#### 证明

式 (26) 是紧自伴 concentration operator 的 min–max 原理。由式 (22)，
`c_(x,theta)` 最终位于某个固定紧区间 `[0,c_0]`；concentration operator
随频带单调，所以 `chi_R(c)<=chi_R(c_0)`。固定 `c_0` 时紧性给出
`chi_R(c_0)->0`。`□`

BT 严格完成了 resonance 三段计划中的“中心井”部分：只要把增长缓慢的
有限个 prolate 模态纳入 Hodge core，中心 resonance 在其正交补上的 Fourier
质量就趋零。剩余的真正困难缩小为**非零 resonance 井**：需要证明它们在
archimedean multiplier 尚未占优的频率范围内满足可求和的分离/宽度界，
或者对其调制 prolate 投影给出总秩与总误差控制。文档 019 已证明强井的
packing 密度 `O(log^3x/x)` 及任意多井的调制 prolate 误差公式；剩余缺口
是弱到强 resonance 的 dyadic 总和。
