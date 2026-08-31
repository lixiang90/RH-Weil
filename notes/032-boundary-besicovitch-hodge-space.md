# 素数边界信号的 Besicovitch--Hodge 空间

文档 031 把 RH 等价地写成所有固定边界 Weil 能量的 `O(1)`。本笔记把
这个解析有界性组织成一个真正的正 Hilbert 结构：只用 von Mangoldt 数据
定义中心化边界信号，其有限时间均方 Gram forms 无条件正半定；若这些
forms 一致有界，则 RH 成立，而且其极限完备化携带一个酉平移群，自伴
生成元的谱正是 zeta 零点的纵坐标。

这给出一个由素数侧出发的 Hilbert--Pólya/Hodge 候选。它的有限截断存在性
无条件成立；尚未建立的紧性恰与 RH 等价，因而不能把该候选误报为证明。

## 1. 中心化边界信号

令测试空间

`T=C_c^infinity((0,infinity))`.                      (1)

对 `h in T` 记

`H(s)=int_0^infinity h(v)e^(-sv)dv`,                 (2)

并用文档 031 的端点素数和定义纯算术信号

`r_h(t)=sum_n Lambda(n)n^(-1/2)h(t-log n)`

`                         -e^(t/2)H(1/2)`, `t>=0`.   (3)

每个固定 `t` 的和有限，且式 (3) 不使用 zeta 零点。定义有限时间 Gram form

`G_T(h,k)=(1/T)int_0^T r_h(t)conjugate(r_k(t))dt`.   (4)

显然对任意有限测试族 `(h_j)`，矩阵 `(G_T(h_j,h_k))` 正半定。

定义 Besicovitch 上均方

`||r_h||_(B^2)^2=limsup_(T->infinity)G_T(h,h)`.       (5)

### 定理 EA（finite boundary mean square is equivalent to RH）

下列条件等价：

1. RH 成立；
2. 对每个 `h in T`，`||r_h||_(B^2)<infinity`；
3. 对某个 Laplace separating 子空间 `T_0 subset T`，每个 `h in T_0`
   都满足式 (5) 有限。这里 separating 指对每个 `w`、`Re w>0`，存在
   `h in T_0` 使 `H(w) !=0`。

#### 证明：RH 推出有限均方

文档 031 定理 DV 给出

`r_h(t)=-sum_rho H(rho-1/2)e^((rho-1/2)t)`

` -sum_(m>=1)H(-2m-1/2)e^((-2m-1/2)t)`.             (6)

若 RH 成立，第一行是绝对一致收敛的 Fourier 级数：

`sum_rho |H(i gamma)|<infinity`.                     (7)

第二行指数衰减。因此 `r_h` 有界，式 (5) 有限。

#### 证明：separating 有限均方推出 RH

若式 (5) 有限，则存在 `C_h`，使所有充分大的 `T` 满足

`int_0^T |r_h(t)|^2dt<=C_h T`.                       (8)

对每个 `sigma>0`，Cauchy--Schwarz 在单位区间求和给出

`int_0^infinity |r_h(t)|e^(-sigma t)dt<infinity`.    (9)

所以其 Laplace 变换在 `Re w>0` 解析。另一方面在 `Re w>1/2`，直接交换
积分与 Dirichlet 级数得到

`int_0^infinity r_h(t)e^(-wt)dt`

`=H(w)(-zeta'/zeta(w+1/2))-H(1/2)/(w-1/2)`.         (10)

若有 `Re rho>1/2`，右边在 `w=rho-1/2` 有极点；separating 性可选择
`H(w)!=0`，与式 (9) 的解析性矛盾。函数方程再排除中心线左侧零点。故
RH 成立。`□`

EA 比文档 031 的逐点一致有界判据更弱：只要求长期平均平方有界，但仍有
完整 RH 强度。

## 2. RH 下的极限 Gram 公式

把不同的零点纵坐标记为 `gamma in Gamma`，其重数为 `m_gamma`。在 RH 下，
式 (6) 的非平凡部分可按相同频率合并为

`-sum_(gamma in Gamma)m_gamma H(i gamma)e^(i gamma t)`. (11)

### 命题 EB（boundary spectral Gram formula）

若 RH 成立，则对所有 `h,k in T`，式 (4) 的极限存在且

`G_infinity(h,k)=sum_(gamma in Gamma)m_gamma^2`

`                    H(i gamma)conjugate(K(i gamma))`. (12)

特别地 `G_infinity` 是正半定 form，其 radical 为

`N={h:H(i gamma)=0 for every gamma in Gamma}`.        (13)

#### 证明

式 (7) 允许逐项计算 Cesaro 平均。不同实频率满足

`lim_(T->infinity)(1/T)int_0^T e^(i(gamma-delta)t)dt`

`=1_(gamma=delta)`.                                  (14)

平凡零点项及其与 Fourier 部分的交叉项平均趋零，得到式 (12)。正性和
radical 描述随即成立。`□`

式 (12) 出现 `m_gamma^2` 而不是 `m_gamma`：一个标量对数导数信号只能看到
重数加权后的单个频率通道，不能自动构造 `m_gamma` 个独立本征方向。这是
该边界模型与完整 cohomological trace space 之间一个明确的剩余缺口。

## 3. GNS 完备化与自伴生成元

令 `V_0` 为所有形式平移

`tau_a r_h(t)=r_h(t+a)`, `a in R`, `h in T`          (15)

的有限线性张成；负 `t` 上任意局部延拓不影响长期均值。若 RH 成立，利用
式 (12) 及平移相位定义

`<tau_a r_h,tau_b r_k>_B`

`=sum_gamma m_gamma^2 H(i gamma)conjugate(K(i gamma))`

`                         e^(i gamma(a-b))`.          (16)

商去零空间并完备化，得到 `H_B`。

### 定理 EC（prime-defined boundary Hilbert--Pólya structure）

在 RH 下：

1. `(H_B,<,>_B)` 是由式 (3) 的素数信号及其长期 Gram 极限规范生成的
   Hilbert 空间；
2. `U_s[tau_a r_h]=[tau_(a+s)r_h]` 延拓为强连续酉群；
3. 存在自伴生成元 `D_B`，使 `U_s=e^(isD_B)`；
4. `D_B` 的点谱是不同的 zeta 零点纵坐标集合 `Gamma`。每个不同纵坐标
   在这个标量模型中重数为一。

反过来，若式 (3) 的 separating 测试族具有一致有限的式 (5)，使上述
长期 Gram 完备化存在，则 RH 成立。

#### 证明

式 (16) 把 `tau_a r_h` 等距映到

`(m_gamma H(i gamma)e^(i gamma a))_(gamma in Gamma)` (17)

所在的 `ell^2(Gamma)`。因此它正且完备化良定义。平移在右边逐坐标乘
`e^(i gamma s)`，故为强连续酉群；Stone 定理给出自伴生成元，逐坐标为
乘法 `gamma`。

对每个 `gamma_0` 可选窄 bump 使 `H(i gamma_0)!=0`。酉群在频率
`gamma_0` 的平均谱投影把相应向量投到该坐标，所以该坐标轴属于闭包；
故每个不同 `gamma` 都是点谱。反向蕴含就是定理 EA。`□`

这实现了抽象谱结构 `Theta=1/2+iD_B`，并自动满足

`Theta^*=1-Theta`.                                   (18)

与文档 001 的无限维中心线结构定理完全一致。关键区别是：这里的内积和
平移候选均由素数侧式 (3) 指定，而不是先把已知零点放进一个 Hilbert
空间；但证明极限内积存在目前仍需要 RH 强度的估计。

## 4. 广义边界 Hodge 结构定理

考虑文档 031 定理 DZ 的 Gamma--Euler 数据 `Z`，中心为 `c/2`。减去已知
右侧 poles 后，以 Euler 系数 `b(n)` 定义中心化信号 `r_(Z,h)(t)`，并照
式 (4) 定义有限时间 Gram forms。

### 定理 ED（Besicovitch boundary-Hodge structure theorem）

假设：

1. `Z` 的完备 divisor 关于 `Re s=c/2` 对称；
2. Euler 对数导数及标准增长条件允许文档 031 的 Mellin 公式；
3. 存在 Laplace separating 测试空间，使每个中心化算术信号的
   Besicovitch 均方有限。

则 `Z` 的全部非平凡零点位于 `Re s=c/2`。此外，若相应 Cesaro Gram
极限存在，则其 GNS 完备化携带规范酉平移群，自伴生成元的谱支撑等于
中心化 divisor 的纵坐标支撑。

#### 证明

条件 3 如定理 EA 一样使每个信号的 Laplace 变换在 `Re w>0` 解析；条件
2 把该变换识别为

`H(w)(-Z'/Z(c/2+w))-known pole terms`.               (19)

separating 性排除中心线右侧零点，条件 1 再排除左侧零点。Gram/GNS 结论
与定理 EC 相同。`□`

ED 是本项目又一个广义结构定理：有限域 Hodge--Riemann 正性在这里被
“所有有限时间 arithmetic Gram forms 的一致紧性”替代；极限正内积使
截断平移成为酉 Frobenius 流，从而迫使权重纯正。

## 5. Zeta 情形的存在性审计

对经典 zeta，目前可无条件构造：

1. 测试空间、素数信号式 (3) 及所有有限 `T` 的 Gram 矩阵；
2. 每个有限 Gram 矩阵的正半定性；
3. prime--pole 主项的精确消去，以及文档 031 的零点无关 Mellin 恒等式；
4. PNT 给出的 `r_h(t)=o(e^(t/2))`，故每个有限时间 form 有限。

尚不能无条件证明：

`sup_(T>=1)G_T(h,h)<infinity`                        (20)

对一个 separating 测试族成立。定理 EA 证明式 (20) 已与 RH 等价。因此
不能把“取 Cesaro 极限并 GNS 完备化”当作免费的泛函分析步骤；缺失的正是
防止 off-center 指数模态进入极限 Hilbert 空间的算术紧性。

一个非循环证明必须从额外几何/代数结构推出式 (20)，例如：

- 把 `G_T` 实现为某个真实上同调范畴中的极化 Gram form，并得到与 `T`
  无关的范数控制；或
- 将文档 029 的 canonical Hodge defect 与这里的时间平均 Gram 连接，证明
  一个不引用零点的 uniform Feshbach/compactness 不等式。

这精确区分了“已构造的有限正结构”和“尚不存在证明的极限 Hodge 结构”。
