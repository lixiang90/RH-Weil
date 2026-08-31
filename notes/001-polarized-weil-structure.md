# 极化 Weil 结构定理

## 1. 为什么函数方程不够

函数方程只把零点 `rho` 与 `c-rho` 配对，实系数再把它与 `conj(rho)` 配对；这允许四元组

`rho, conj(rho), c-rho, c-conj(rho)`。

要把四元组压到中心线 `Re(s)=c/2`，需要一个**正定**结构，使相应算子在平移/归一化后成为酉算子或反自伴算子。正性是 Weil 方法不可删除的部分。

## 2. 最小有限维结构

### 定理 A（极化 Frobenius 模）

设 `H` 是有限维复向量空间，`F` 是可逆线性算子，`Q>0`。若 `H` 上存在正定 Hermite 内积 `h`，满足

`h(Fx,Fy) = Q h(x,y)`，

则：

1. `U=Q^(-1/2)F` 是酉算子；
2. `F` 可对角化；
3. `F` 的每个特征值 `alpha` 都满足 `|alpha|=Q^(1/2)`。

#### 证明

等式直接给出 `h(Ux,Uy)=h(x,y)`，故 `U` 酉。有限维酉算子的谱定理说明 `U` 可酉对角化且全部特征值模为 `1`。乘回 `Q^(1/2)` 即得结论。`□`

这个定理很短，但单独把 `h` 当作公理会有循环性：知道所有特征值在圆周上以后，常常可以反向制造这样的内积。下一节说明怎样由 Lefschetz 结构系统地产生它。

## 3. 极化 Lefschetz–Frobenius 代数

固定实数 `q>1` 和整数 `d>=0`。一个 **PLF 代数**（本笔记的术语）由以下数据组成：

- 有限维分次复交换代数 `H = direct_sum H^n`，只在 `0<=n<=2d` 非零；
- 反线性代数对合 `x -> bar(x)`；
- 顶次迹 `tau: H^(2d) -> C`，乘法配对 `H^n x H^(2d-n) -> C` 非退化；
- 一个实的 Lefschetz 元 `L in H^2`，对 `n<=d`，`L^(d-n):H^n -> H^(2d-n)` 是同构；
- 分次代数自同构 `F`，与共轭交换，并满足
  
  `F(Lx)=q L F(x)`, 以及 `tau(Fz)=q^d tau(z)`；
- 由 Hard Lefschetz 得到的 primitive 分解。若
  
  `P^a = ker(L^(d-a+1):H^a -> H^(2d-a+2))`,
  
  则每个齐次元素是若干 `L^r u`（`u in P^a`）之和。选择非零实常数 `c_(a,r)`，定义
  
  `S_n(L^r u)=c_(a,r)L^(d-a-r)u`, 其中 `n=a+2r`；
- 对每个 `n`，存在模为 `1` 的常数 `epsilon_n`，使
  
  `h_n(x,y)=epsilon_n tau(x S_n(bar(y)))`
  
  是 `H^n` 上的正定 Hermite 内积。

最后一条是抽象的 Hodge–Riemann 正性。常数和相位吸收通常的 Koszul 符号、阶乘与 Hodge 星号约定；下面的谱论只用到它的正定性以及 `S_n` 对 primitive 分解的形式。

### 定理 B（广义 Weil 结构定理，有限维版）

对任意 PLF 代数，`F|H^n` 的每个特征值 `alpha` 满足

`|alpha| = q^(n/2)`。

而且 `F|H^n` 可对角化。

#### 证明

先注意 `F` 保持 primitive 子空间。若 `u in P^a`，则由 `F L=q L F`（作为算子关系）及 `F` 可逆，

`L^(d-a+1)F(u)=q^(-(d-a+1))F(L^(d-a+1)u)=0`。

取 `x=L^r u in H^n`，其中 `u in P^a` 且 `n=a+2r`。直接计算：

`S_n F(x)=q^r c_(a,r)L^(d-a-r)F(u)`，

`F S_n(x)=q^(d-a-r)c_(a,r)L^(d-a-r)F(u)`。

因为 `a+2r=n`，得到关键交换式

`S_n F = q^(n-d) F S_n`.                                  (1)

于是，对 `x,y in H^n`，使用 `F` 与共轭交换、`F` 保乘法、式 (1) 以及顶次迹的缩放关系，

```
h_n(Fx,Fy)
 = epsilon_n tau(Fx S_n(bar(Fy)))
 = q^(n-d) epsilon_n tau(F(x S_n(bar(y))))
 = q^n h_n(x,y).
```

定理 A（取 `Q=q^n`）立即给出结论。`□`

### 哪条公理真正做了工作？

- 迹公式把 zeta 函数变成 `F` 的特征行列式；
- Poincare 对偶和 Hard Lefschetz 构造 `S_n`；
- `F(L)=qL` 算出缩放指数恰好是 `n`；
- **Hodge–Riemann 正性**把形式变成 Hilbert 空间内积，从而把“谱关于圆周对称”加强为“谱就在圆周上”。

删掉最后一项，只剩函数方程式的成对对称，不能推出绝对值。

## 4. Weil 原始方法的迹界版本

上面的定理把正性实现为上同调空间本身的正定 Hermite 形式。Weil 对曲线的原始论证也可抽象为另一条路线：correspondence 的正交叉形式先给出所有 Frobenius 幂的迹界，再由函数方程提供 reciprocal pairing。

### 定理 C（reciprocal pairing + 幂迹界）

给定非零复数 `alpha_1,...,alpha_N`（计重数）和 `Q>0`。假设：

1. 该多重集在 `alpha -> Q/alpha` 下不变；
2. 存在与 `m` 无关的常数 `C`，使所有 `m>=1` 都满足
   
   `|sum_j alpha_j^m| <= C Q^(m/2)`。

则每个 `alpha_j` 都满足 `|alpha_j|=Q^(1/2)`。

#### 证明

令 `beta_j=alpha_j/Q^(1/2)`、`p_m=sum_j beta_j^m`。假设 2 说明幂级数 `sum_(m>=1)p_m z^m` 的收敛半径至少为 `1`。另一方面，在原点附近

`sum_(m>=1)p_m z^m = sum_j beta_j z/(1-beta_j z)`。

合并相等的 `beta_j` 后，右边在每个 `z=beta_j^(-1)` 都有非零留数，所以没有极点抵消；其收敛半径是 `1/max_j|beta_j|`。故 `max_j|beta_j|<=1`。假设 1 在归一化后变成多重集在 `beta -> 1/beta` 下不变，因此也有 `min_j|beta_j|>=1`。两者合并即 `|beta_j|=1`。`□`

在有限域曲线情形，transpose correspondence / Poincare 对偶给出 reciprocal pairing；Hodge index（等价地 Jacobian 上 Rosati involution 的正性）配合 Cauchy–Schwarz 给出 `|Tr(F^m|H^1)|<=2g q^(m/2)`。定理 C 随即给出所有 reciprocal roots 的模为 `sqrt(q)`。

这个版本说明正性不一定要先延拓成整个复上同调上的内积；它也可以位于一个算术定义的 correspondence 代数上，只要足以产生**对所有 `m` 一致**的幂迹界。

## 5. 从迹公式到 zeta 零点

### 定理 D（抽象 Lefschetz 迹公式）

在定理 B 的条件下，另设一列“点数”满足

`N_m = sum_n (-1)^n Tr(F^m | H^n)`。

定义

`Z(T)=exp(sum_(m>=1) N_m T^m/m)`。

则作为 `T` 的形式幂级数（因有限维也作为有理函数）有

`Z(T)=product_n det(1-TF|H^n)^((-1)^(n+1))`.               (2)

`H^n` 所贡献的每个 reciprocal zero/pole `alpha` 满足 `|alpha|=q^(n/2)`。令 `T=q^(-s)`，相应因子的零点或极点满足

`Re(s)=n/2`。

#### 证明

有限维恒等式

`-log det(1-TF)=sum_(m>=1)Tr(F^m)T^m/m`

逐次数相加即得 (2)。定理 B 给出 `alpha` 的绝对值；`1-alpha q^(-s)=0` 取绝对值即得 `q^(-Re(s))=q^(-n/2)`。`□`

### 曲线特例

若 `d=1`，则

`Z(T)=det(1-TF|H^1)/[(1-T)(1-qT)]`。

分子 reciprocal roots 的模都是 `sqrt(q)`，所以 `T=q^(-s)` 下全部非平凡零点位于 `Re(s)=1/2`。这正是有限域曲线的 RH 形状。

高维情形必须按权重分层：`H^n` 位于 `Re(s)=n/2`，并非整个未归一化 zeta 函数只有同一条中心线。

## 6. 无限维/数域的谱版本

### 定理 E（极化生成元定理）

令 `mathcal H` 为 Hilbert 空间，`Theta` 为稠密定义闭算子。设某个实数 `c` 满足

`D(Theta)=D(Theta*)` 且 `Theta*=cI-Theta`.                  (3)

则 `A=Theta-(c/2)I` 是反自伴算子。特别地，`Theta` 的每个特征值 `rho` 都满足

`Re(rho)=c/2`。

#### 证明

式 (3) 给出 `A*=-A`。若 `Theta v=rho v`，则

`2 Re(rho)||v||^2 = <(Theta+Theta*)v,v> = c||v||^2`，

故 `Re(rho)=c/2`。`□`

若进一步有一个不预先使用零点位置的迹/正规化行列式公式

`Lambda(s)=E(s) det_infinity(s-Theta)`，

其中 `E` 无零，则 `Lambda` 的全部非平凡零点位于中心线。对自对偶、纯权 `w` 的 motivic L 函数，通常 `c=w+1`；单位化以后中心可写成 `1/2`。

非自对偶情形可以在对偶成对后的空间上使用同一定理：把 `M` 与 `M^vee`（或 Dirichlet 特征 `chi` 与 `bar(chi)`）的谱块取直和，要求 adjoint 把两个块互换且总算子满足 `Theta*=(w+1)-Theta`。若总正规化行列式是 `Lambda(M,s)Lambda(M^vee,s)` 乘无零因子，则乘积的所有零点在中心线，因而两个因子各自的全部零点也在中心线。这覆盖通常 GRH 所需的非自对偶 L 函数形式。

## 7. 逻辑强度警告

给定一组已经知道位于中心线的零点，可以在以零点为基的空间上对角定义 `Theta`，再宣布该基正交；这会自动满足定理 E。反过来，若 `det_infinity(s-Theta)` 的零点恰好是目标零点且 (3) 成立，定理 E 就已经证明了 RH。

所以对经典 zeta 函数，“存在某个这样的 Hilbert 空间和算子”在最低抽象层面与 RH 等价。有效的存在性定理必须额外满足：

1. 对象由素数、idele 类空间、算术 scheme 或其他独立算术数据构造；
2. 正定性不借用 RH；
3. 迹/行列式等式严格恢复完成 L 函数，包括无穷处因子；
4. 无限维时处理定义域、闭性、谱型与正规化收敛。

这四项防止把结论偷偷放回公理。

文档 073 将 exact adjoint/similitude 公理放宽为 two-sided tempered dynamics：
正反 powers 只有 subexponential growth 已足以推出 purity；若 orbit uniform
bounded，则 Cesaro averaging 会自动重建一个等价 exact polarization。该
版本还对 tensor、dual、subquotient 与 Schur functors 封闭。

文档 077 再把 ordinary Hilbert dimension推广为 semifinite trace dimension：
允许 minimal eigenspace一维但 `tau(P_rho)=m_rho`，仍可用 tracial spectral
determinant按正确重数恢复 zeta divisor。
