# 显式 prolate 特征值尾与弱 resonance 分层

文档 019 把非零 resonance 的贡献化成

`sum_j D_j chi_(R_j)(c_j)`.                            (1)

弱 resonance 的 packing 常数随阈值 `theta->0` 恶化，但井宽及
time–bandwidth 参数同时按 `theta` 缩小。本笔记从 prolate sinc kernel 的
Taylor 展开证明一个显式有限秩尾界：剥离固定个数的模式后，下一特征值含有
任意高的 `theta` 幂。这解决了 dyadic 阈值方向的求和；剩余障碍不是单井
谱，而是巨大频率范围内许多井的 block-frame 合成。

## 1. sinc kernel 的有限秩 Taylor 逼近

把时间区间缩放为 `[-1,1]`，频带为 `[-c,c]`。prolate concentration
operator 的 kernel 是

`K_c(x,y)=sin(c(x-y))/(pi(x-y))`.                       (2)

其特征值按降序记为 `chi_0(c)>=chi_1(c)>=...`。

### 定理 BY（显式 prolate eigenvalue tail）

若 `0<c<=1`、`R>=1`，则

`chi_(2R-1)(c)`

`<=2e^2 4^R c^(2R+1)/(pi(2R+1)!)`.                    (3)

#### 证明

展开

`K_c(x,y)=sum_(n=0)^infinity`

` (-1)^n c^(2n+1)(x-y)^(2n)/(pi(2n+1)!)`.             (4)

截取 `0<=n<R`。由于 `(x-y)^(2n)` 展开为 `x^ky^(2n-k)`，截断 kernel 的
range 包含于次数至多 `2R-2` 的多项式空间，故秩至多 `2R-1`。

对 `|x-y|<=2`，指数级 Taylor 余项估计给出

`|K_c(x,y)-K_c^((R))(x,y)|`

`<=e^(2c)c^(2R+1)|x-y|^(2R)/(pi(2R+1)!)`

`<=e^2 4^R c^(2R+1)/(pi(2R+1)!)`.                     (5)

`[-1,1]^2` 的面积为 `4`，所以余项 operator norm 不超过其
Hilbert–Schmidt norm，后者至多式 (5) 右端的两倍。紧算子的 min–max/
approximation-number characterization 给出式 (3)。`□`

定理 BY 的常数很粗，但关键是 `c^(2R+1)/(2R+1)!`；固定 `R` 已给出任意
高奇次幂，令 `R` 增长则有阶乘加速。

## 2. 一个 dyadic 弱 resonance 层的单井代价

考虑层

`theta P(x)<=Re F_x(t)<2theta P(x)`,                   (6)

并在 packing 定理 BV 中取 `eta=theta/2`。引理 BU 给出的临界井半宽满足

`r_theta asymp theta/log x`,                            (7)

故 `L=log x` 时

`c_theta=Lr_theta/2=O(theta)`.                         (8)

该层的负 multiplier 深度至多粗界

`D_theta<=4theta P(x)+|m_infinity|`,                    (9)

因为 `K_infinity>=m_infinity`。在 `theta P(x)>=1` 的层上可吸收固定常数，
写成 `D_theta<=Ctheta P(x)`。更弱的 `theta P(x)<1` 只可能在
`K_infinity<4` 的固定紧频率区产生负部，可并入中心有限 core。

### 推论 BZ（弱井的高阶阈值收益）

对充分小的 `theta`，每口该层 resonance 井剥离前 `2R-1` 个调制 prolate
模态后，其“深度 × concentration tail”至多

`C_R P(x) theta^(2R+2)`,                               (10)

其中

`C_R=8e^2 4^R C^(2R+1)/(pi(2R+1)!)`                   (11)

且 `C` 是式 (8) 的绝对常数。

#### 证明

将 `c_theta<=Ctheta` 代入定理 BY，再乘以式 (9) 在
`theta P(x)>=1` 时的 `Ctheta P(x)`。`□`

定理 BV 的 packing 常数约为 `theta^(-3)`。所以单纯比较阈值幂时，

`theta^(-3)*P(x)theta^(2R+2)`

`=P(x)theta^(2R-1)`.                                   (12)

任取 `R>=1`，对 dyadic `theta=2^(-h)` 的弱端求和都收敛；`R>=2` 时还有
`theta^3` 以上的宽裕。**因此弱阈值本身不是发散来源。**

## 3. 巨大频率长度仍使逐井求和失败

packing 定理在长窗口中的井数是

`N_theta(T)=O(T theta^(-3)log^3x/x)`                   (13)

（省略 `T` 不足时的 endpoint 项）。把式 (10) 对所有井独立相加只得到

`O(T P(x)log^3x/x * theta^(2R-1))`

`=O(T log^3x/sqrt(x) * theta^(2R-1))`.                 (14)

archimedean multiplier 最终会使负集紧，但只用
`K_infinity(t)~(1/2)log|t|` 与 `|F_x(t)|<=P(x)`，所得最坏截止可达
`T=exp(O(P(x)))`。因此式 (14) 即使有任意固定 `theta` 幂，也不能对如此大的
窗口趋零。

### 命题 CA（independent-well summation no-go）

定理 BV 的 packing 数乘以定理 BY 的**逐井** operator-norm 尾，单独不足以
证明文档 019 式 (18)；还必须利用不同调制井之间的近正交/frame 结构，或
得到远强于全局均方的频率截止。

#### 证明

式 (14) 在允许的最坏 `T=exp(O(sqrt x))` 上发散。该结论只排除把所有井的
同一向量上界直接求和的方法，不排除真实 concentration operators 的联合
operator norm 很小。`□`

## 4. 所需的 block-frame 输入

对 dyadic 层 `h` 的井记其 concentration operators 为 `K_(h,j)`，前
`2R_h-1` 个特征空间投影为 `Pi_(h,j)`。令 `Q` 包含所有这些有限秩空间。

需要的不是井数，而是正交补上的 block Bessel bound，例如

`||sum_j (1-Pi_(h,j))K_(h,j)(1-Pi_(h,j))||`

`<=A_h chi_(2R_h-1)(Ctheta_h)`.                        (15)

### 定理 CB（dyadic block-frame 到弱层可求和）

假设式 (15) 成立，且存在固定 `q>=0`、`A>0` 使

`A_h<=A theta_h^(-q)`.                                 (16)

则第 `h` 层在 `Q^perp` 上的负贡献至多

`C_(R_h)P(x)theta_h^(2R_h+2-q)||f||^2`.                (17)

若从某个 `theta_*` 以下取固定 `R`，满足 `2R+2>q`，则所有弱层总误差至多

`C_R P(x)theta_*^(2R+2-q)`.                            (18)

特别地，可令 `theta_*=P(x)^(-alpha)`，其中 `0<alpha<1`；只要

`alpha(2R+2-q)>1`，式 (18) 趋于 `0`。

#### 证明

式 (15)、定理 BY 与层深度 `O(theta_hP(x))` 给出式 (17)。对 dyadic
`theta_h` 求几何级数得到式 (18)。最后代入 `theta_*`。`□`

CB 证明了一个重要的量词事实：不需要每口井使用随 `x` 无界增长的 prolate
秩；只要多井 residual blocks 形成具有多项式 frame bound 的族，固定充分大
的 `R` 就能求和全部弱层。

## 5. 下一步被压缩成一个 frame theorem

对分离调制的单一指数族，经典大筛/Hilbert 不等式的 frame 常数只依赖频率
最小间距，而不依赖点数。当前需要把它推广到每个中心携带固定维 prolate
block 的情形，并允许同一 dyadic 层的重叠井先合并。

一个足够的具体目标是证明：若合并后的井中心间距至少为其半宽之和，且
`c_j<=Ctheta`，则式 (15) 可取

`A_h=O(theta^(-q))`                                    (19)

对某个绝对 `q`。一旦得到任意有限 `q`，定理 CB 允许增大固定 `R` 吸收它。
文档 021 已用分离 Fourier 导数采样和调制多项式 core 证明该结论可取
`q=1`。因此全部弱 dyadic 层的无限维误差已经求和；剩余缺口是显式有限
resonance core 的矩阵正性与 Schur 耦合。
