# 数域 zeta / L 函数的结构存在性审计

## 1. 目标包

对完成的自对偶 L 函数 `Lambda(s)`，把所需的“算术 Weil 包”压缩成四项。非自对偶时把对象与其对偶的谱块取直和，并把下面的 `Lambda` 换成两者之积；乘积的中心线结论会逐因子推出 GRH。

**G1（全局上同调/谱空间）**：存在 Hilbert 复形或适当的核空间 `H^bullet`，其相关部分上有闭算子 `Theta`。

**G2（行列式）**：在明确的正规化下，

`Lambda(s) = E(s) product_i det_infinity(s-Theta|H^i)^((-1)^(i+1))`，

其中 `E` 的零极点完全已知。

**G3（全局 Lefschetz 迹公式）**：`Theta` 的分布迹等于所有素数幂与无穷处项组成的显式公式。素数在这里应扮演闭轨道/闭点，而不是彼此无关的一族局部 Frobenius。

**G4（极化）**：相关谱块上有正定内积并满足

`Theta*=(w+1)I-Theta`。

由文档 001 的定理 E，G1–G4 立即推出对应的 GRH。

## 2. 为什么逐素数套用 Weil 定理不够

一个容易犯的错误是：每个有限素数 `p` 的局部因子都有“纯”Frobenius 参数，于是全局 Euler 乘积的零点也应在中心线。这个推理不成立。

最直接的反证式例子就是

`zeta(s)=product_p (1-p^(-s))^(-1)`。

每个局部因子只有最简单的参数 `1`，不存在局部 RH 障碍；但全局 Euler 乘积解析延拓后的非平凡零点位置仍正是经典 RH。局部纯性控制 Satake/Frobenius 参数的大小，全球 RH 控制的是**跨所有素数解析耦合后**的谱，两者是不同层次的问题。

因此必须构造一个单一的全局 `Theta` 和一条把“素数侧”与“零点侧”相连的全局迹公式。

## 3. 三种存在性尝试的严格状态

### 3.1 从零点直接造空间：成立但完全循环

取形式基 `e_rho`，令 `Theta e_rho=rho e_rho`。若 RH 成立，可令这些基向量正交，得到 `Theta*=1-Theta`（对称性和重数作适当配对）。反向则由文档 001 的定理 E 推出 RH。

结论：最小谱结构的存在性与 RH 等价，不提供独立证明。

### 3.2 Weil 显式公式的二次型：最接近“交叉形式”

Weil 的显式公式把零点和素数幂写成同一个分布的两种表达。对适当测试函数 `f`，构造卷积平方 `f*f^*`；Weil 判据断言，相应二次型在整个允许测试空间上非负，当且仅当 RH 成立。

这与有限域交叉理论的角色高度一致：

- 测试函数/对应物相当于 correspondences；
- 显式公式相当于 Lefschetz 迹公式；
- Weil 二次型相当于 Hodge index / Rosati 正性。

但“证明整个 Weil 二次型非负”本身就是 RH 的等价形式。研究价值在于寻找一个几何 Hilbert 空间，使该二次型成为显然的范数平方，而不是直接估计它。

### 3.3 Deninger / Connes 型全局几何：结构部分存在，决定性极化尚缺

Deninger 提出：对算术 scheme 应有某种上同调与流，其无穷小生成元 `Theta` 的正规化行列式给出 zeta/L 函数；素数对应闭轨道，显式公式对应动力 Lefschetz 公式。对 `Spec Z` 尚未构造出满足全部 G1–G4 的理论。

Connes 的 adele 类空间给出零点的谱解释和显式公式的非交换几何版本，但已有结果没有排除非临界零作为 resonance 的可能；所需全局正性仍是核心。

## 4. 2025–2026 自伴有限截断路线

Connes–Consani–Moscovici 研究 Weil 二次型 `QW_lambda` 在

`L^2([lambda^(-1),lambda],du/u)`

上的限制；支集条件使素数侧只涉及 `p<=lambda^2`。再投影到 scaling 算子的前 `2N+1` 个 Fourier 模态，得到有限矩阵 `QW_lambda^N`。

这里有一项必须保留的条件：若 `QW_lambda^N` 的最低特征值 `epsilon_N` 是单重的、对应特征向量 `xi` 是 inversion-even，论文才证明相应 rank-one perturbation `D_log^(lambda,N)` 自伴，并证明

`det_reg(D_log^(lambda,N)-z)=-i lambda^(-iz) hat(xi)(z)`，

其中 `hat(xi)` 是整函数、全部零点为实数。这些实零数值上极高精度地逼近 `zeta(1/2+it)` 的低零点，但一般的 simple-even 条件和极限仍未证明。

### 定理 F（同一直线上零点的局部一致极限）

设 `Omega` 是平面区域，`D_j` 在 `Omega` 上全纯，全部零点位于固定直线 `ell`。若 `D_j` 在 `Omega` 的每个紧集上一致收敛到不恒为零的全纯函数 `D`，则 `D` 在 `Omega` 中的全部零点也位于 `ell`。

#### 证明

若 `D` 在直线外一点 `rho` 有零，取包含于 `Omega` 的闭圆盘，使其边界及内部均不碰 `ell`，且边界上 `D` 无零。局部一致收敛和 Rouché 定理说明充分大的 `j` 中，`D_j` 在圆盘内与 `D` 有相同的正数个零，矛盾。`□`

### 可检验的 RH 桥接命题

若能在非平凡零点对应的开带 `Omega={z:|Im(z)|<1/2}` 中证明有限自伴截断的正规化行列式 `D_(lambda,N)(z)`：

1. simple-even 条件成立，因而每个都是整函数且所有零点在实轴；
2. 存在显式无零正规化因子 `E_(lambda,N)(z)`；
3. `E_(lambda,N)D_(lambda,N) -> Xi(z)=xi(1/2+iz)` 在 `Omega` 中局部一致；

则定理 F 说明所有非平凡 zeta 零点对应的 `z` 都是实数，即 RH。这里前两项来自有限维自伴性；新的数学集中在证明 simple-even 及第三项，而不能仅靠数值谱逼近。

### 论文已经完成到哪里

论文构造 prolate wave operator 的低特征函数 `h_(0,lambda),h_(4,lambda)`，令 `h_lambda` 为其中积分为零的特定线性组合，并令

`k_lambda(u)=E(h_lambda)(u)=u^(1/2) sum_(n>=1) h_lambda(nu)`

（限制在 `[lambda^(-1),lambda]`）。它证明：适当正规化后，`hat(k_lambda)` 在开带 `|Im(z)|<1/2` 的每个闭子带上一致趋于 Riemann `Xi(z)`。

因此决定性的缺口已经缩成：证明真正的 Weil 算子最低特征向量 `xi_lambda` 与 `k_lambda`（乘一个标量后）在足以控制 Fourier 变换局部一致收敛的范数中趋近。

### 定理 G（从最低向量逼近到 RH）

设存在一列 `lambda_j -> infinity`；以下所有极限只沿这列取。假设：

1. 每个 `QW_(lambda_j)` 的最低特征值单重，归一化最低特征向量 `xi_(lambda_j)` 为 inversion-even；相应构造给出整函数 `hat(xi_(lambda_j))`，其零点全为实数；
2. 存在非零标量 `c_(lambda_j)`，使对每个 `0<a<1/2`，
   
   `integral |c_(lambda_j) xi_(lambda_j)(u)-k_(lambda_j)(u)|(u^a+u^(-a))du/u -> 0`；
3. `hat(k_(lambda_j))->Xi` 在 `|Im(z)|<1/2` 中局部一致（这是论文已证明的全参数极限的一个子列）。

则 RH 成立。

#### 证明

按 Fourier–Mellin 约定 `hat(f)(z)=integral f(u)u^(-iz)du/u`。当 `|Im(z)|<=a` 时，

`|u^(-iz)|=u^(Im(z)) <= u^a+u^(-a)`。

所以假设 2 说明 `c_(lambda_j) hat(xi_(lambda_j))-hat(k_(lambda_j))` 在每个闭子带上一致趋于 `0`。结合假设 3，`c_(lambda_j) hat(xi_(lambda_j))->Xi` 在开带内局部一致。每个近似函数的零点全在实轴，定理 F 说明 `Xi` 在该带内的零点也全在实轴。`s=1/2+iz` 把 zeta 的整个临界带 `0<Re(s)<1` 对应到 `|Im(z)|<1/2`；故所有非平凡零点满足 `Re(s)=1/2`。`□`

该定理把“足够接近”的含义精确化了：仅有普通 `L^2` 收敛不自动够用，因为支集随 `lambda` 增长；必须控制与闭子带宽度相匹配的指数权。

注意这里只需构造**某一列** `lambda_j -> infinity`，不需要先证明 simple-even 对所有实参数 `lambda` 成立。这显著降低了存在性任务的量词强度，并允许将严格有限截面证书作为候选输入。

### 引理 H（谱隙把变分估计转为特征向量逼近）

令 `A` 为下有界自伴算子，最低两个谱值满足 `lambda_0<lambda_1`，最低特征向量为 `e_0`。若 `||f||=1` 且 `mu=<Af,f>`，则

`dist(f,C e_0)^2 <= (mu-lambda_0)/(lambda_1-lambda_0)`。

#### 证明

写 `f=a e_0+y`，`y` 与 `e_0` 正交。谱定理给出

`mu >= lambda_0|a|^2+lambda_1||y||^2 = lambda_0+(lambda_1-lambda_0)||y||^2`。

而 `dist(f,C e_0)=||y||`，移项即得。`□`

因此，要证明定理 G 的假设 2，一个自然的两步法是：先用 `k_lambda` 的 Rayleigh quotient 与严格谱隙证明其 `L^2` 谱投影集中到 `xi_lambda`；再利用算子方程或核估计把 `L^2` 控制升级为定理 G 所需的指数加权 `L^1` 控制。

## 5. 下一阶段应攻击的精确子问题

### 子问题 A：证明 lowest eigenspace 的 simple-even 性

论文已经证明 `QW_lambda` 下有界、下半连续并有离散谱，但尚未证明其最低特征值对所有充分大 `lambda` 单重，及相应特征向量在 `u -> u^(-1)` 下为偶。

可检验的切入点：

- 先把 inversion 对称性分解成偶、奇两个闭子空间；
- 比较两个子空间的 Rayleigh quotient 下确界，证明严格谱隙；
- 在偶子空间尝试 positivity-improving / Perron–Frobenius 型论证，但必须先把核变换成保正形式；原始 `QW_lambda` 的素数平移项带负号，不能直接套定理；
- 若走微扰路线，需要给出从 prolate 算子到 `QW_lambda` 的算子范数或 form-norm 误差，小于 prolate lowest spectral gap。

### 子问题 B：证明 `xi_lambda` 与 `k_lambda` 的定量逼近

论文已证明构成 `k_lambda` 的 prolate 函数趋于 Hermite 函数，因而 `hat(k_lambda)->Xi`。还需证明 `k_lambda` 是 `QW_lambda` 的 quasimode：若归一化后

`||(QW_lambda-mu_lambda)k_lambda|| <= delta_lambda`

且最低谱与其余谱之间有 gap `g_lambda>0`，则 Davis–Kahan/谱投影估计给出

`dist(k_lambda, span(xi_lambda)) <= delta_lambda/g_lambda`。

所以一个具体证明目标是同时得到 `delta_lambda/g_lambda -> 0`，并把该 `L^2` 型接近升级为带指数权的 `L^1` 控制，从而保证 Fourier 变换在 `|Im(z)|<=1/2-epsilon` 上局部一致接近。

### 子问题 C：避免把 Euler 尾部估计偷偷建立在 RH 上

所有候选收敛证明都应做依赖审计。若用到 `Xi'/Xi` 在整个半平面无极点、零点密度的 RH 强版本、或 Weil 二次型的全局非负，则产生循环。允许使用的无条件输入包括函数方程、Hadamard 分解、经典零点自由区和已知零点计数渐近，但每项必须明确标注。

## 6. 当前判断

- “广义结构定理”的有限维和谱版本可以严格证明，见文档 001。
- 对经典/广义 RH，尚不能证明目标结构存在；这会解决开放问题。
- 最有信息量的存在性目标不是再命名一个抽象上同调，而是证明一个具体有限自伴模型的正规化行列式局部一致收敛，或者把 Weil 二次型实现成独立构造的范数平方。
- 当前优先路线：证明 `k_lambda` 的 quasimode residual `delta_lambda` 小于 `QW_lambda` 的 lowest spectral gap，并单独建立 even/odd Rayleigh quotient 的严格分离；并行保留 Deninger 的 G1–G4 作为结构检查表。
