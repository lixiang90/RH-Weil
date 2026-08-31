# 非零 resonance 的 packing 与调制 prolate 覆盖

文档 018 证明强 prime-phase resonance 的相对测度很小，并用 prolate
min–max 严格移除了中心井。本笔记进一步证明：每个强 resonance 点都带有
自然宽度 `asymp 1/log x` 的井，而这类井的 packing 密度为
`O(log^3x/x)`。随后给出一个一般的多井调制 prolate 定理，把剩余全球
Hodge–Riemann domination 化成总秩与总 concentration-eigenvalue 账本。

## 1. resonance 点不能无限尖

沿用

`F_x(t)=sum_(k<=x)w_k k^(it)`, `P(x)=sum_(k<=x)w_k`,

并定义第一对数矩

`M_1(x)=sum_(k<=x)w_k log k`.                           (1)

### 引理 BU（resonance derivative width）

`|(Re F_x)'(t)|<=M_1(x)` 对所有实 `t`。若 `0<eta<theta<1` 且

`Re F_x(t_0)>=theta P(x)`,                              (2)

则

`[t_0-r,t_0+r] subset {t:Re F_x(t)>=eta P(x)}`,        (3)

其中

`r=(theta-eta)P(x)/M_1(x)`.                            (4)

此外

`M_1(x)=2sqrt(x)log x(1+o(1))`,                        (5)

故固定 `eta<theta` 时 `r=(theta-eta)/log x*(1+o(1))`。

#### 证明

逐项求导并使用三角不等式得到第一条。均值定理给出

`Re F_x(t)>=Re F_x(t_0)-M_1(x)|t-t_0|`,                (6)

从而得到式 (3)–(4)。式 (5) 由素数定理对
`sum Lambda(k)k^(-1/2)log k` 作分部求和。`□`

所以强 resonance 与中心井一样，都具有 time-limited Fourier 变换能感知的
自然宽度，不能是零测度孤立点。

## 2. 强 resonance 井的 packing 密度

称一组点 `{t_j}` 是 `2r`-分离的，如果 `|t_i-t_j|>2r`。

### 定理 BV（strong-resonance packing bound）

设 `{t_1,...,t_N}` 是 `[-T,T]` 中满足式 (2) 的 `2r`-分离点集，其中
`r` 由式 (4) 给出。则

`N<=((2(T+r)+4xH_x)B_2(x))`

`   /(2r eta^2P(x)^2)`.                                (7)

若 `eta,theta` 固定且 `T/(xH_x)->infinity`，则

`N/(2T)=O_(eta,theta)(log^3x/x)`.                      (8)

#### 证明

引理 BU 给每个 `t_j` 一个半径 `r`、包含于较弱 `eta`-resonance 集的区间。
这些区间两两不交，并包含于 `[-T-r,T+r]`，所以

`2rN<=|R_x(T+r,eta)|`.                                 (9)

对右端应用文档 018 定理 BP 的未归一化形式，得到式 (7)。最后使用

`B_2~(1/2)log^2x`、`P~2sqrt x` 以及引理 BU 的
`r asymp 1/log x`。`□`

式 (8) 比单纯测度界多一个 `log x`，代价正是把坏集分解成临界宽度的井。
平均而言，固定强度 resonance 井之间的间距至少具有
`x/log^3x` 的尺度。

## 3. 任意频率井都是调制后的同一个 prolate 问题

令时间支撑区间长度为 `L`。对频率井

`I_j=[t_j-r_j,t_j+r_j]`                                (10)

定义 concentration operator

`K_j=P_L F^(-1)1_(I_j)F P_L`.                          (11)

乘法调制 `f(y)->exp(it_jy)f(y)` 把 `K_j` 酉等价到中心频带
`[-r_j,r_j]` 的 prolate operator。因此其特征值只依赖

`c_j=Lr_j/2`,                                          (12)

记为 `chi_0(c_j)>=chi_1(c_j)>=...`。

### 定理 BW（multiwell modulated-prolate removal）

设 `E subset union_(j=1)^J I_j`。对每个 `j` 选择整数 `R_j>=0`，令
`Q` 是所有 `K_j` 的前 `R_j` 个特征向量之线性张成。若 `f perpendicular Q`，
则

`int_E|hat f(t)|^2dt/(2pi)`

`<=sum_(j=1)^J chi_(R_j)(c_j)||f||^2`,                 (13)

其中 `R_j=0` 表示使用 `chi_0`、而不剥离该井。

更一般地，若 `d(t)>=0` 在 `E` 上且

`D_j=sup_(t in I_j)d(t)`,                              (14)

则

`int_E d(t)|hat f(t)|^2dt/(2pi)`

`<=sum_j D_j chi_(R_j)(c_j)||f||^2`.                  (15)

#### 证明

`f perpendicular Q` 蕴含它与每个 `K_j` 的前 `R_j` 个特征向量正交。
prolate min–max 给出

`int_(I_j)|hat f|^2/(2pi)<=chi_(R_j)(c_j)||f||^2`.     (16)

对覆盖求和得到式 (13)；乘以每个井上的 supremum 得式 (15)。区间重叠只会
使右端重复计数，不影响上界。`□`

## 4. 到 Euler–Weil domination 的直接接口

对 zeta 令 Fourier multiplier 的负部为

`d_lambda(t)=[2P_lambda-K_infinity(t)-G_lambda(t)]_+`. (17)

它的支撑是紧集：因为 `G_lambda>=0` 且
`K_infinity(t)->infinity`。把该支撑覆盖为有限频率井 `I_j`，并把奇极点锚
`s(y)=sinh(y/2)` 也加入有限核心 `Q_lambda`。

### 推论 BX（resonance-cover certificate）

若沿 `lambda->infinity` 可选择覆盖与整数 `R_j`，使

`sum_j D_j chi_(R_j)(c_j)=epsilon_lambda->0`,          (18)

则在 `Q_lambda^perp` 上

`QW_lambda(f,f)>=-epsilon_lambda||f||^2`.               (19)

若再对有限核心 `Q_lambda` 及其与正交补的耦合完成文档 016 式 (33) 的
Schur/interval 证书，并使总负误差为 `o(1)`，则由定理 BG 得到 RH。

#### 证明

在 `Q_lambda^perp` 上负极点锚消失。命题 BJ 表明其余负贡献正是式 (17)
乘以 `|hat f|^2` 的积分；定理 BW 给出式 (19)。最后应用文档 016、015 的
Schur 与过滤正性定理。`□`

BX 是可计算的非零 resonance 终点：每口井只贡献“负深度 × 下一 prolate
特征值”，而不是用整个坏集的 Lebesgue 测度粗估。

## 5. 已完成与未完成的定量账本

对固定 `0<eta<theta<1` 的强 resonance：

- 引理 BU：每口井半宽 `asymp1/log x`；
- 定理 BV：井中心 packing 密度 `O(log^3x/x)`；
- 因 `L=log x`，每口井的 `c_j=O(1)`；
- 定理 BW：每口井可用固定形状的调制 prolate 谱处理。

尚未完成的是把负集 (17) **全部**分层成固定强度 resonance。低
archimedean 频率处，阈值 `Re F_x(t)>K_infinity(t)/2` 可能只是很弱的
正 resonance，定理 BV 的常数随 `theta->0` 恶化。需要按
`theta=2^(-h)` 分层，并证明

`sum_(h,j)D_(h,j)chi_(R_(h,j))(c_(h,j))->0`            (20)

同时有限核心的总秩与 Schur 耦合仍可控制。式 (20) 是下一步精确的
非零 resonance 目标，而不再是未量化的“应用某个不确定性原理”。文档 020
已用 sinc kernel Taylor 展开证明弱井的显式高阶 prolate 尾，并说明最后
缺口可取为一个多井 residual blocks 的多项式 block-frame bound。
