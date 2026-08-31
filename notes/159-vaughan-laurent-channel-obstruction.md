# Vaughan Laurent 主部通道、物理维数障碍与 paired rank-two 候选

文档 158 留下的首要问题是：冻结整数通道是否能从 Vaughan convolution identity
的连续主项解析导出？本节逐项计算四个未中心化 Vaughan Dirichlet series 在
`s=1` 的 Laurent 主部。结论是否定而且有结构性：两个极点抵消方向都严格位于
物理向量 `e=(1,1,1,1)` 的正交补，故它们的二维 span 不可能就是此前观察到的
physical leading rank-two core。

这个失败产生三个正面结果：

1. 得到一个完全解析、与 zeros 无关的 pole-cancellation Hodge subspace；
2. 证明“两个 Laurent directions 同时充当二维 physical core”的维数 no-go；
3. 从旧整数平面抽出一个精确零和方向，并简化成新的固定 paired 候选
   `span{(1,1,1,1),(8,-8,-3,3)}`。

最后一个候选在九个 finite blocks 上稳定，但其中 `8:3` 仍是 data-suggested
比例，不是 RH 证明，也尚未从 convolution algebra 独立导出。

## 1. 四个未中心化 Dirichlet series

令 `z=s-1`，并记

`M_U(s)=sum_(d<=U)mu(d)d^(-s)=m_0+m_1z+O(z^2)`,   (1)

其中

`m_0=sum_(d<=U)mu(d)/d`,

`m_1=M_U'(1)=-sum_(d<=U)mu(d)log(d)/d`.           (2)

再令

`L_V(s)=sum_(m<=V)Lambda(m)m^(-s)=ell_0+O(z)`.    (3)

文档 153 的四个未中心化 Vaughan components 的 Dirichlet series 是

`P_1=M_U(-zeta')`,

`P_2=-M_UL_Vzeta`,

`P_3=(1-M_Uzeta)(-zeta'/zeta-L_V)`,

`P_4=L_V`.                                        (4)

它们逐点满足

`P_1+P_2+P_3+P_4=-zeta'/zeta`.                    (5)

这里 component order 始终为

`(Type-I log, Type-I correction, Type-II, low prime power)`. (6)

### 定理 ABU（exact Vaughan Laurent principal-part theorem）

式 (4) 在 `s=1` 的 double-pole 与 simple-pole coefficient vectors 分别为

`d_U=m_0(1,0,-1,0)`,                              (7)

`r_(U,V)=(m_1,-m_0ell_0,1+m_0ell_0-m_1,0)`.       (8)

特别地，

`e^Td_U=0`, `e^Tr_(U,V)=1`.                       (9)

#### 证明

使用标准展开

`zeta(1+z)=z^(-1)+gamma+O(z)`,

`-zeta'(1+z)=z^(-2)+O(1)`,

`-zeta'/zeta(1+z)=z^(-1)-gamma+O(z)`.             (10)

于是 `P_1` 的两项主部为 `m_0z^(-2)+m_1z^(-1)`，而 `P_2` 的
simple residue 是 `-m_0ell_0`。对第三项，

`1-M_Uzeta=-m_0z^(-1)+(1-m_0gamma-m_1)+O(z)`,

`-zeta'/zeta-L_V=z^(-1)-gamma-ell_0+O(z)`.        (11)

故 `P_3` 的 double coefficient 是 `-m_0`，simple coefficient 是

`m_0(gamma+ell_0)+1-m_0gamma-m_1`

`=1+m_0ell_0-m_1`.                                (12)

`P_4` 在 `s=1` 解析。合并即得式 (7)--(8)，坐标求和给式 (9)。`□`

注意式 (12) 中 Euler 常数完全消去；这是 exact Vaughan identity 在 principal
part level 的一个非平凡一致性检查。

## 2. 多 cutoff 混合与 pole-cancellation Hodge subspace

取不同 cutoffs `(U_j,V_j)` 与实权 `w_j`，满足 `sum_jw_j=1`。令

`d=sum_jw_jd_(U_j)`, `r=sum_jw_jr_(U_j,V_j)`.     (13)

再把 continuum residue 按实 shares

`alpha=(alpha_1,...,alpha_4)`, `e^Talpha=1`        (14)

分配到四个 components，并置

`b=r-alpha`.                                      (15)

### 定理 ABV（balanced singular-channel theorem）

由式 (13)--(15) 得到的 singular principal-part matrix

`R_sing=[d b]`                                    (16)

满足

`e^TR_sing=0`.                                    (17)

因而

`S_sing=Ran(R_sing) subset e^perp`, `dim S_sing<=2`. (18)

这些对象只依赖 `mu,Lambda` 的有限 Dirichlet sums、cutoffs 与 continuum shares，
不依赖任何 zero ordinate 或 zero location。

#### 证明

定理 ABU 给每个 `e^Td_(U_j)=0`、`e^Tr_(U_j,V_j)=1`。权重和为一，故
`e^Td=0,e^Tr=1`；再由 `e^Talpha=1` 得 `e^Tb=0`。`□`

实现 `vaughan_laurent_channel_data` 返回每个 cutoff 的 `(m_0,m_1,ell_0)`、
式 (7)--(8)、混合向量、全部 residue residuals，以及

- singular basis `span{d,b}`；
- physical-double basis `span{e,d}`；
- physical-simple basis `span{e,b}`。

线性相关 seeds 会被自动降秩，所以代码实现的是定理中的 `dim<=2`，而非强行制造
二维空间。

## 3. 物理方向的维数障碍

### 定理 ABW（rank-two principal-part obstruction）

设 `d,b` 线性独立。则：

1. `dim S_sing=2` 且 `S_sing perp e`；
2. `dim span(S_sing,e)=3`；
3. 任意包含全部 `S_sing` 的 rank-two core 都把 `e` 完全留在 tail；
4. 任意包含 `e` 的 rank-two core 至多包含 `S_sing` 的一个独立方向。

进一步，若 `P_sing` 是 `S_sing` 的投影，`P_*` 是任意 rank-two target projector，
则

`||P_sing-P_*|| >= ||P_*e||/||e||`.               (19)

#### 证明

前四项是式 (18) 与维数公式的直接结果。令 `f=e/||e||`。因为
`P_sing f=0`，

`||P_sing-P_*||>=||(P_sing-P_*)f||=||P_*f||`,     (20)

即式 (19)。`□`

因此，如果 leading spectral plane 对物理方向的 participation 接近一，任何纯
Laurent singular plane 的 principal sine 必然接近一。这不是 cutoff、数值精度或
Gram--Schmidt 选择造成的，而是 residue conservation `e^TR_sing=0` 的精确后果。

## 4. Feshbach scalar excess 的两个退化极端

相对 core projector `P` 与 `Q=I-P` 写

`G=[[A,B],[B^*,C]]`, `e=x+y`, `x=Pe`, `y=Qe`.     (21)

对 `epsilon>||C||`，文档 157 的 majorant 在物理方向给

`e^*M_epsilon e`

`=x^*Ax+x^*B(epsilon I-C)^(-1)B^*x`

` +epsilon||y||^2`.                               (22)

### 定理 ABX（physical Feshbach degeneracy/no-go）

有两个相反的退化情形：

1. 若 `Pe=0`，则式 (22) 等于 `epsilon||e||^2`；core 完全看不见物理能量。
2. 若 `Pe=e`，则 `y=0` 且

   `e^*M_epsilon e=e^*Ge`

   ` +<(epsilon I-C)^(-1/2)B^*e,`

   `   (epsilon I-C)^(-1/2)B^*e>`,                (23)

   所以当 `epsilon->infinity` 时上界趋于 exact physical energy。

第二种情形通常没有 finite optimal `epsilon`；除非 `B^*e=0`，infimum 只在
`epsilon=infinity` 达到。因而一个精确包含 `e` 的 core 可以自动产生任意小的
scalar Feshbach excess，但 core 项 `e^*Ae=e^*Ge` 本身正是原待证能量。小 excess
单独并未简化算术估计。

#### 证明

把 `x=0` 或 `y=0` 代入式 (22)。当 `y=0` 时 correction 非负并随 `epsilon`
单调下降到零；若 `B^*e ne0`，对每个 finite `epsilon` 它严格为正。`□`

这修正了对 rank-two diagnostics 的解释：必须同时报告 fixed finite threshold 下的
tail/coupling capacity 与 principal angle，不能仅按物理方向的 optimized excess
选择 basis。本节统一使用

`epsilon=||C||+lambda_1(G)`                       (24)

作 finite comparison。

## 5. 从旧整数平面到 paired physical plane

文档 158 的旧 seeds 为

`a_1=(17,-1,4,10)`, `a_2=(3,-17,-10,-2)`.        (25)

它们的坐标和分别为 `30,-26`，故旧平面内的 exact zero-sum direction 是

`13a_1+15a_2=2(133,-134,-49,50)`.                (26)

把旧平面的“几乎物理”方向替换为 exact `e`，得到 physicalized plane

`C_phys=span{e,(133,-134,-49,50)}`.               (27)

式 (26) 的第二向量又极接近更简单的 paired vector

`v=(8,-8,-3,3)`.                                  (28)

事实上两方向夹角满足

`sin^2 angle(v,(133,-134,-49,50))`

`=227/5919716`,                                   (29)

故 `sin angle approximately .00619`。式 (28) 对两个 Type-I components 作一组
反差，对 Type-II/low components 作另一组反差，并严格满足 `e^Tv=0`。

### 定理 ABY（frozen paired-channel conditional RH criterion）

令

`C_pair=span{(1,1,1,1),(8,-8,-3,3)}`              (30)

并以固定顺序 Gram--Schmidt 得 projector `P_pair`。若 `P_pair` 对 zeta Vaughan
simplex Grams 满足文档 158 定理 ABR 的 frozen core/tail/coupling capacity bound，
则 RH 成立。同样结论适用于满足 Gamma--Euler hypotheses 的一般数据。

#### 证明

式 (30) 的两向量正交且非零，故无条件定义一个与 height、Abel scale、cutoffs、
zeros 均无关的 rank-two projector。应用定理 ABS 与 ABR。`□`

ABY 是完全明确的条件判据，但没有证明其 capacity hypothesis。尤其，式 (28) 的
paired 形状由 component labels 支持，`8:3` 比例却仍来自对式 (26) 的小整数化；
目前不能称为独立的 convolution-algebra derivation。

## 6. 九 block finite audit

使用文档 155 的参数 `delta=.1,theta=.25,h=theta/T`，continuum 在
`[.001,log(N+1)]` 上作 20-cell midpoint quadrature。每块先独立求 stable simplex
cutoff/background weights；Laurent candidates 因而已经得到有利的 block-adaptive
选择。所有 Feshbach comparisons 都用式 (24)，并直接检查 `M-G>=0`。

九块上的范围为：

| basis | physical overlap | principal sine | tail / `lambda_1` | finite-threshold excess |
|:---|---:|---:|---:|---:|
| `span{d,b}` | `0` exact | `.999917--.999993` | `.686--.937` | `109%--198%` |
| `span{e,d}` | `1` exact | `.720--.834` | `.313--.548` | `2.15%--8.61%` |
| `span{e,b}` | `1` exact | `.595--.900` | `.225--.634` | `1.24%--11.64%` |
| old integer plane | `.994091` | `.0239--.138` | `.0931--.157` | `.169%--1.11%` |
| `C_pair` | `1` exact | `.0646--.188` | `.0922--.158` | `.0767%--.634%` |

第一行验证定理 ABW 的预言：pure singular span 并非 observed PCA plane。把 `e`
加入但只保留一个 Laurent direction 仍远弱于旧整数横向通道。最后两行说明旧
整数平面的主要 spectral geometry 可以在精确包含 `e` 后保留，而且 paired 小整数
vector 没有明显恶化。

`C_pair` 的逐块结果是：

| `(N,Y,T)` | principal sine | tail/`lambda_1` | coupling/`lambda_1` | excess at (24) |
|---:|---:|---:|---:|---:|
| `(80,30,2)` | `.1882` | `.1583` | `.0467` | `.1124%` |
| `(80,30,4)` | `.0962` | `.1315` | `.0280` | `.1225%` |
| `(80,30,8)` | `.0691` | `.1266` | `.0407` | `.1841%` |
| `(80,30,16)` | `.0646` | `.1256` | `.0441` | `.1969%` |
| `(160,60,2)` | `.1418` | `.1456` | `.1026` | `.6344%` |
| `(160,60,4)` | `.0961` | `.1161` | `.0707` | `.3249%` |
| `(160,60,8)` | `.0947` | `.1111` | `.0671` | `.2757%` |
| `(160,60,16)` | `.0989` | `.1112` | `.0681` | `.2663%` |
| `(240,90,8)` | `.0695` | `.0922` | `.0273` | `.0767%` |

这张表使用统一 finite threshold，不可与文档 158 对每块优化 `epsilon` 后更小的
excess 直接比较。计算由 `audit_vaughan_laurent_channels.py` 完整复现；它是普通
高精度 floating-point diagnostic，不是 interval enclosure。

## 7. 证据边界与下一步

本节解析地排除了一个候选解释，但没有证明 RH：

- Laurent principal parts 无条件给 `S_sing subset e^perp`；
- 这解释的是 pole cancellation，不是 observed physical rank-two core；
- `C_pair` 的固定 projector 无条件存在，但 uniform dyadic capacity 未证；
- 精确包含 `e` 会使 scalar Feshbach infimum退化，真正需要分别估计 transverse
  channel、tail 与 coupling，而不是引用小 excess；
- 九个 finite blocks 不控制 `Y->infinity`，midpoint/prime tails也未作 interval
  enclosure。

下一步应针对 regular 而非 principal Laurent data：

1. 计算式 (4) 的 constant terms，并在 pole-cancellation quotient 中投影；
2. 检查 paired difference space
   `span{(1,-1,0,0),(0,0,-1,1)}` 是否由 Vaughan incidence/boundary map规范产生；
3. 若能解析得到 transverse ratio，比较它是否为 `8:3` 或随 scale 有可控变化；
4. 对 `C_pair` 分别证明 `A` 的 transverse entry、`B` 与 `C` 的 Type I/II
   dyadic bounds，避免用 `e^*Ae` 重述原问题；
5. 将文档 156 的 vector-error Loewner radius加入同一个 fixed-threshold audit。

所以本节的净进展是：continuous principal matrix 已完全算清，并严格证明它不是
所求二维 core；新的 proof target 已缩小为一个 physical direction 加一个 regular
paired transverse direction。
