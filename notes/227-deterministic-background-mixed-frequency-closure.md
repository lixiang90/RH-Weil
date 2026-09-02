# 227. 确定性背景 mixed-frequency evacuation 与非循环共同高度选择

日期：2026-09-02

分支：MOM-1 / 路线 A1f；接口：显式公式型部分 Weil 配置

状态：one-prime/two-prime shifted upper bounds、有限 mixed-word Toeplitz
归约、所有含确定性背景的非零频率短高度消去、完整 centered fourth-trace
共同高度上界为 [T]；Henriot discriminant-uniform Nair--Tenenbaum 上界为
[R]；Montgomery--Taylor 窗口积分为 [E]；从相对稠密 good heights 转化为
全局简单零点比例以及 \(13/18\)、\(16/21\) 的适用条件仍为 [O]。

## 1. 结论

笔记 226 已把实际中心化矩阵写为

\[
 \mathcal C(t)=S_L+P(t)+E_{\rm ar}(t),
 \qquad
 \|E_{\rm ar}(t)\|\ll L^{-1},
 \qquad L=\log X,
\tag{1}
\]

其中

\[
 S_L=T_d(s_L),\qquad
 s_L(u)=\frac{\phi(u)^2}{a}-1
\tag{2}
\]

是确定性零频 Toeplitz 背景，\(P(t)\) 是 pure-prime Hermitian response。
令

\[
 H=\frac{X}{\sqrt L},\qquad N\asymp XL,\qquad \lambda=\log L.
\tag{3}
\]

本轮证明：对每个 \(I=[Y,Y+H]\)、\(Y\asymp X\)，

\[
 \boxed{
 \frac1H\int_I\operatorname{tr}(S_L+P(t))^4\,dt
 \le
 \{D_0(\psi)+D_{\rm mix}(\psi)+D_{22}(\psi)\}N+o(N).}
\tag{4}
\]

特别地，区间内存在 \(t_I\) 使

\[
 \boxed{
 \operatorname{tr}\mathcal C(t_I)^4
 \le
 \{D_0(\psi)+D_{\rm mix}(\psi)+D_{22}(\psi)\}N+o(N).}
\tag{5}
\]

式 (5) 的选择顺序至关重要。不能先在 pure-prime good set 上选点，再假设
mixed remainder 在同一点小；signed first means 不保证两个 good sets 相交。
本轮先对非负量

\[
 F_0(t)=\operatorname{tr}(S_L+P(t))^4
\tag{6}
\]

整体取平均并只选择一次。选点后，\(F_0(t_I)=O(N)\) 与
\(\|S_L\|_4=O(N^{1/4})\) 自动给

\[
 \|P(t_I)\|_4
 \le\|S_L+P(t_I)\|_4+\|S_L\|_4
 =O(N^{1/4}),
\tag{7}
\]

此时才能非循环地消去 \(E_{\rm ar}\)。

独立算术输入是

\[
 \boxed{
 \sum_{R<n\le2R}\Lambda(n)(\Lambda*\Lambda)(n+h)
 \ll
 \Delta(h)R\log R(\log\log R)^3+R\log R,}
\tag{8}
\]

\[
 \boxed{
 \sum_{R<n\le2R}\Lambda(n)\Lambda(n+h)
 \ll
 \Delta(h)R(\log\log R)^2+R,}
\tag{9}
\]

一致于 \(1\le |h|\le R\)，其中

\[
 \sum_{h\le U}\Delta(h)\ll U,\qquad
 \sum_{h\le U}\frac{\Delta(h)}h\ll\log(2U).
\tag{10}
\]

式 (8) 消去 mixed three-prime 的 \(++-\) 近对角，式 (9) 消去
mixed two-prime 的 \(+-\) 非对角。它们只使用 prime-side upper-bound
sieve，不使用 zeros、RH、Hardy--Littlewood 渐近或 Weil 正性。

## 2. \(\Omega=1,2\) 支撑筛

沿用笔记 224 的

\[
 \mathbf e_j(n)=\mathbf1_{\Omega(n)=j}.
\tag{11}
\]

外部定理 224-A 给：对 \(0<z_1,z_2\le1\)，

\[
 \sum_{R<n\le2R}z_1^{\Omega(n)}z_2^{\Omega(n+h)}
 \ll
 \Delta(h)\frac{R}{(\log R)^2}
 \prod_{p\le3R}
 \left(1+\frac{z_1}{p}\right)
 \left(1+\frac{z_2}{p}\right).
\tag{12}
\]

### 引理 227-A（one-prime/two-prime support correlation）[T]

\[
 \boxed{
 \sum_{R<n\le2R}\mathbf e_1(n)\mathbf e_2(n+h)
 \ll
 \Delta(h)\frac{R(\log\log R)^3}{(\log R)^2}.}
\tag{13}
\]

#### 证明

置 \(\ell=\log R\)，取

\[
 z_1=\frac1{\log\ell},\qquad
 z_2=\frac2{\log\ell}.
\tag{14}
\]

逐点有

\[
 \mathbf e_1(n)\mathbf e_2(m)
 \le z_1^{-1}z_2^{-2}
 z_1^{\Omega(n)}z_2^{\Omega(m)}.
\tag{15}
\]

Mertens 上界给

\[
 \prod_{p\le3R}
 \left(1+\frac{z_1}{p}\right)
 \left(1+\frac{z_2}{p}\right)
 \ll
 \exp((z_1+z_2)\log\ell+O(1))
 \ll1,
\tag{16}
\]

而 \(z_1^{-1}z_2^{-2}\asymp(\log\ell)^3\)。代入式 (12) 即得。
\(\square\)

### 引理 227-B（one-prime/one-prime support correlation）[T]

\[
 \boxed{
 \sum_{R<n\le2R}\mathbf e_1(n)\mathbf e_1(n+h)
 \ll
 \Delta(h)\frac{R(\log\log R)^2}{(\log R)^2}.}
\tag{17}
\]

证明同上，取 \(z_1=z_2=1/\log\ell\)。\(\square\)

## 3. von Mangoldt proper-power 账本

记

\[
 \Lambda=\Lambda_1+\mathcal E_1,
\qquad
 \Lambda_1(n)=\Lambda(n)\mathbf1_{n\ {\rm prime}},
\tag{18}
\]

并置

\[
 \mathcal A_2=\Lambda*\Lambda,\qquad
 \mathcal A_{2,0}=\Lambda_1*\Lambda_1,\qquad
 \mathcal E_2=\mathcal A_2-\mathcal A_{2,0}\ge0.
\tag{19}
\]

笔记 224 已证明

\[
 \sum_{n\le R}\mathcal E_1(n)\ll\sqrt R\log R,
 \qquad
 \sum_{n\ge1}\frac{\mathcal E_1(n)}n<\infty.
\tag{20}
\]

### 引理 227-C（two-factor proper-power decomposition）[T]

\[
 \sum_{n\le R}\mathcal E_2(n)\ll R,
\qquad
 \mathcal A_2(n)\ll(\log(2n))^4,
\tag{21}
\]

且

\[
 \mathcal A_{2,0}(n)
 \le2(\log(2n))^2\mathbf e_2(n).
\tag{22}
\]

#### 证明

\(\mathcal E_2\) 的每项至少有一个 factor 来自 \(\mathcal E_1\)。
Chebyshev 上界给

\[
 \sum_{ab\le R}\mathcal E_1(a)\Lambda(b)
 \ll R\sum_a\frac{\mathcal E_1(a)}a
 \ll R.
\tag{23}
\]

交换 factors 得式 (21) 第一式。若 \(\mathcal A_2(n)\ne0\)，两个
factors 都是 \(n\) 的 prime-power divisors；ordered pairs 数至多
\(O(\Omega(n)^2)\)，每个权至多 \(O((\log n)^2)\)，故得到 pointwise
\(O((\log n)^4)\)。两个 prime factors 只有两个 ordered permutations，
得到式 (22)。\(\square\)

### 定理 227-D（shifted \(E_2\)-prime correlation）[T]

式 (8) 对正、负 shifts 都成立。

#### 证明

先处理 \(\Lambda_1(n)\mathcal A_{2,0}(n+h)\)。由式 (13)、(22) 及
\(\Lambda_1(n)\le\log(3R)\)，

\[
 \sum_{R<n\le2R}
 \Lambda_1(n)\mathcal A_{2,0}(n+h)
 \ll
 \Delta(h)R\log R(\log\log R)^3.
\tag{24}
\]

含 \(\mathcal E_2(n+h)\) 的项由式 (21) 和
\(\Lambda(n)\le\log(3R)\) 控制为 \(O(R\log R)\)。
含 \(\mathcal E_1(n)\) 的项只在 proper prime powers 上出现；由
pointwise bound，其总贡献为

\[
 O(\sqrt R(\log R)^6)=o(R\log R).
\tag{25}
\]

交换两个 shifted variables 处理负 \(h\)。\(\square\)

### 定理 227-E（shifted prime-pair upper bound）[T]

式 (9) 对正、负 shifts 都成立。

#### 证明

prime-prime 部分由式 (17) 乘两个 \(\log(3R)\) weights 得到
\(\Delta(h)R(\log\log R)^2\)。至少一个 proper prime power 的部分由
式 (20)、\(\Lambda\le\log(3R)\) 控制为
\(O(\sqrt R(\log R)^2)=O(R)\)。\(\square\)

当 \(h=0\) 时，

\[
 \mathcal A_2(p^k)=(k-1)(\log p)^2,
\tag{26}
\]

故

\[
 \sum_{n\ge1}\frac{\Lambda(n)\mathcal A_2(n)}n
 =
 \sum_p\sum_{k\ge2}
 (k-1)\frac{(\log p)^3}{p^k}<\infty.
\tag{27}
\]

mixed \(++-\) 的 exact zero frequency 不产生新主尺度。

## 4. 有限 mixed words 的 Toeplitz 表示

写

\[
 P(t)=\sum_{n\le X}b_n\{R_t(x_n)+R_t(x_n)^*\},
\quad
 b_n=-\frac1{2\pi}\frac{\Lambda(n)}{\sqrt n},
\quad x_n=\log n.
\tag{28}
\]

考虑含 \(j\in\{1,2,3\}\) 个 prime responses、\(4-j\) 个 \(S_L\)
的固定 cyclic word。给定 prime factors 与 signs，令

\[
 u=\sum_{\nu=1}^j\varepsilon_\nu\log n_\nu.
\tag{29}
\]

笔记 204、225 的 modulation covariance 精确给

\[
 W_{j,\boldsymbol\varepsilon}(t;\mathbf n)
 =
 \beta_L^je^{itu}
 \operatorname{tr}\{T(f_1)T(f_2)T(f_3)T(f_4)D_d(u)\},
\tag{30}
\]

其中每个 \(f_k\) 是 \(s_L\) 或平移后的 \(q_{x_n}\)，且统一满足

\[
 \|f_k\|_\infty+\|f_k'\|_1+\|f_k''\|_1\ll1.
\tag{31}
\]

四因子 Toeplitz telescoping 因而给

\[
 W_{j,\boldsymbol\varepsilon}
 =
 W_{j,\boldsymbol\varepsilon}^{\rm bulk}
 +W_{j,\boldsymbol\varepsilon}^{\partial},
\tag{32}
\]

\[
 |W_{j,\boldsymbol\varepsilon}^{\rm bulk}|
 \ll \beta_L^jd,
\qquad
 |W_{j,\boldsymbol\varepsilon}^{\partial}|
 \ll \beta_L^j(1+\log L).
\tag{33}
\]

bulk symbol 非零还要求 signed prime walk 的跨度不超过 \(L\)。每个
\(q_x(u)=\phi(u)\phi(x-u)\) 同时记录 edge 的两个端点；插入 \(s_L\)
不改变 walk 位置。因此：

1. 三个同号 prime factors 强制 \(n_1n_2n_3\le X\)；
2. \(++-\) 经 cyclic rotation 后强制两个正号乘积 \(n_1n_2\le X\)；
3. \(+-\) 只留下 ordinary ratio frequency \(\log(n_1/n_2)\)。

finite crossing boundary 不必满足 path constraints，但式 (33) 删除了维数
\(d\)，其全盒贡献仍可单独求和。

## 5. 短高度核

令

\[
 K_I(u)=\frac1H\int_Ie^{itu}\,dt,
\qquad
 |K_I(u)|\le\min\left(1,\frac2{H|u|}\right).
\tag{34}
\]

若 \(m,n\asymp R\)、\(m=n+h\ne n\)，则

\[
 |K_I(\log(m/n))|
 \ll\min\left(1,\frac{R}{H|h|}\right).
\tag{35}
\]

由式 (10) 及 Abel summation，

\[
 \sum_{1\le|h|\le R}
 \Delta(h)\min\left(1,\frac{R}{H|h|}\right)
 \ll\frac RH\log(2R),
\tag{36}
\]

ordinary unweighted sum同样成立。标准 partial summation 给

\[
 \sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}\ll\sqrt X,
\quad
 \sum_{m\le X}\frac{\mathcal A_2(m)}{\sqrt m}\ll\sqrt X\,L,
\quad
 \sum_{r\le X}\frac{\mathcal A_3(r)}{\sqrt r}\ll\sqrt X\,L^2.
\tag{37}
\]

## 6. Mixed-frequency evacuation [T]

### 定理 227-F（bulk mixed words）

展开

\[
 4\operatorname{tr}(S_L^3P)
 +4\operatorname{tr}(S_L^2P^2)
 +2\operatorname{tr}(S_LPS_LP)
 +4\operatorname{tr}(S_LP^3).
\tag{38}
\]

删除 zero-prime main 与 balanced two-prime diagonal 后，其余 bulk
部分在任意式 (3) 的 \(I\) 上的 signed first mean 为 \(o(N)\)。

#### 证明

固定 cyclic ordering；有限多个 orderings 和 signs 只改变常数。

一个 prime 的频率至少为 \(\log2\)，所以

\[
 \frac{d\beta_L}{H}
 \sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}
 \ll \sqrt{XL}=o(N).
\tag{39}
\]

两个同号 primes 同理：

\[
 \frac{d\beta_L^2}{H}
 \left(\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}\right)^2
 \ll\frac X{\sqrt L}=o(N).
\tag{40}
\]

两个异号 primes 的 exact diagonal保留为 \(D_{\rm mix}N\)。off-diagonal
在 comparable dyadic range 中由式 (9)、(35)--(36) 控制；除以
\(\sqrt{n_1n_2}\asymp R\)，再乘
\(d\beta_L^2\asymp X/L\)，得到

\[
 \ll X\sqrt L\,\lambda^2+\frac X{\sqrt L}
 =o(XL).
\tag{41}
\]

三个同号 primes 由 path support 和式 (37) 给

\[
 \frac{d\beta_L^3}{H}
 \sum_{m\le X}\frac{\mathcal A_3(m)}{\sqrt m}
 \ll\sqrt{XL}=o(N).
\tag{42}
\]

对两个正号、一个负号，置 \(m=n_1n_2\)、\(n=n_3\)。bulk path
support 给 \(m\le X\)。comparable ranges 中，式 (8)、(35)--(36)
在除以 \(\sqrt{mn}\asymp R\) 后给

\[
 \sum_{m\ne n}
 \frac{\mathcal A_2(m)\Lambda(n)}{\sqrt{mn}}
 |K_I(\log(m/n))|
 \ll
 \frac RH\,L^2\lambda^3.
\tag{43}
\]

乘 \(d\beta_L^3\asymp X/L^2\)，对 \(R\le X\) 求和，得到

\[
 \ll X\sqrt L\,\lambda^3=o(N).
\tag{44}
\]

noncomparable ranges 用式 (37) 与 \(|K_I|\ll H^{-1}\)，得到

\[
 \frac{d\beta_L^3}{H}(\sqrt X\,L)(\sqrt X)
 \ll\frac X{\sqrt L}=o(N).
\tag{45}
\]

其余 signs 由 conjugation 或 cyclic rotation 化到上述情形。
\(\square\)

### 定理 227-G（finite crossing mixed words）

式 (32) 中所有 mixed crossing boundaries 的 signed first mean总和为
\(o(N)\)。

#### 证明

对 resonant \(+-\) 与 \(++-\) comparable ranges，重复式 (41)、(43)，
只把 \(d\beta_L^j\) 换成 \((1+\log L)\beta_L^j\)，因而比 bulk
bound 再小 \((1+\log L)/d=o(1)\)。

boundary 没有 path support。对 noncomparable 或同号 frequencies 使用
\(|K_I|\ll H^{-1}\)。最坏的 \(j=3\) 全盒质量为 \(O(X^{3/2})\)，故

\[
 \frac{(1+\log L)\beta_L^3}{H}X^{3/2}
 \ll
 \frac{\sqrt X(1+\log L)}{L^{5/2}}
 =o(N).
\tag{46}
\]

\(j=1,2\) 更小。若 \(++-\) 的 product \(n_1n_2\) 与 \(n_3\le X\)
comparable，则自动有 \(n_1n_2\ll X\)，已进入 shifted bound；否则进入
式 (46)。\(\square\)

## 7. 主对角与共同高度

### 引理 227-H（deterministic main ledger）[T]

\[
 \operatorname{tr}S_L^4=D_0(\psi)N+o(N),
\tag{47}
\]

而 opposite prime signs 的 exact diagonal 对式 (38) 的贡献为

\[
 D_{\rm mix}(\psi)N+o(N).
\tag{48}
\]

#### 证明

对 \(S_L^4\) 使用四因子 Toeplitz telescoping。bulk trace 是
\(dL^{-1}\int s_L^4=D_0d\)，crossing trace norm 为
\(O(1+\log L)=o(N)\)，且 \(d/N\to1\)。

对式 (48)，在
\(4\operatorname{tr}(S_L^2P^2)+2\operatorname{tr}(S_LPS_LP)\)
中枚举 opposite signs。两个 \(S^2P^2\) orientations 分别给
\(2C_1\)，两个 \(SPSP\) orientations 给 \(2C_2\)。再用

\[
 L^{-2}\sum_{n\le e^L}\frac{\Lambda(n)^2}{n}
 \delta_{\log n/L}\Longrightarrow r\,dr.
\tag{49}
\]

finite crossing 每个 \(n\) 为
\(O((1+\log L)\beta_L^2)\)；乘
\(\sum_{n\le X}\Lambda(n)^2/n=O(L^2)\) 后仍为
\(O(1+\log L)=o(N)\)。\(\square\)

### 定理 227-I（centered fourth trace at relative-dense heights）[T]

式 (4)--(5) 成立。

#### 证明

笔记 225 给 pure-prime 部分在每个 \(I\) 上的 one-sided average

\[
 \frac1H\int_I\operatorname{tr}P(t)^4dt
 \le D_{22}(\psi)N+o(N).
\tag{50}
\]

定理 227-F--G 消去 mixed nonzero frequencies，引理 227-H 给主对角，
从而得到式 (4)。因为 \(F_0(t)\ge0\)，存在 \(t_I\in I\) 使
\(F_0(t_I)\le H^{-1}\int_IF_0(t)dt=O(N)\)。式 (7) 给
\(\|P(t_I)\|_4=O(N^{1/4})\)。再由
\(\|E_{\rm ar}(t_I)\|_4=O(N^{1/4}/L)\) 与 Schatten telescoping，

\[
 |\operatorname{tr}\mathcal C(t_I)^4-F_0(t_I)|
 \ll N/L=o(N).
\]

这证明式 (5)。\(\square\)

## 8. 数值尺度与结论边界

对 Montgomery--Taylor 窗，

\[
 \begin{aligned}
 D_0&=0.000078787511\ldots,\\
 D_{\rm mix}&=0.007840799168\ldots,\\
 D_{22}&=0.244589382034\ldots,
 \end{aligned}
\]

所以

\[
 \boxed{B_{\rm MT}=0.252508968714\ldots.}
\tag{51}
\]

窗口积分为 [E]，式 (5) 对由这些积分定义的精确常数为 [T]。当前不把
式 (51) 表述为新的无条件简单零点比例。仍需独立审计：

1. finite matrix 的 rank/simple-zero counting inequality 对“每个
   \(X/\sqrt L\) interval 存在一个 good height”的精确需求；
2. \(13/18\) Christoffel certificate 需要 pointwise、averaged 还是
   cofinal-subsequence fourth trace；
3. \(16/21\) inertia certificate 是否使用同一 trace normalization。

这些接口完成前，式 (51) 是无条件 fourth-trace configuration constant，
不是已发布零点比例。

## 9. 最小公理与删除审计

1. **Henriot discriminant-uniform upper bound**：产生式 (8)--(10)。
   删除 bounded-mean \(\Delta\) 后，short-height harmonic sum可能多损失一个
   \(L\)，式 (44) 不再闭合。
2. **\(\Omega=1,2\) 双参数优化**：给恰好三个
   \(\log\log R\) powers；固定参数会损失固定 \(\log R\) power。
3. **proper-power ledger**：\(\Lambda*\Lambda\) 不是 multiplicative
   function；不拆出 \(\mathcal E_2\) 就不能直接套 Henriot。
4. **actual response path support**：三个同号 prime factors 必须限制在
   product \(\le X\)。删除后式 (42) 的全盒质量超过 \(N\)。
5. **response-specific Toeplitz crossing**：boundary 每个 tuple 只有
   \(O(\log L)\)，而非 \(d\)。
6. **whole-fourth-trace selection**：修复 pure/mixed good sets 未必相交的
   逻辑缺口；删除 \(F_0\ge0\) 后不能在选点后反推 \(\|P\|_4\)。

结论不是 RH 的改写。新增输入都在 prime side，只给相对稠密高度上的有限矩阵
fourth-trace upper bound；零点比例接口明确保留为下一开放审计。

## 10. 模型范围与 Weil 接口

- Riemann zeta：式 (4)--(5) 直接适用。
- 固定本原 Dirichlet \(L\)：绝对上界删除 character phases，shifted
  bounds 保留；Gamma shift 已由笔记 226 吸收。
- Dedekind/automorphic \(L\)：需要 degree-two coefficient convolution
  的 discriminant-uniform shifted sieve；Rankin--Selberg 二矩不自动给出。
- 函数域：continuous short-height kernel 应换成 Frobenius orbit characters。
- 只有函数方程而无 Euler-product sparsity的模型缺失式 (8)--(9)。

本轮属于显式公式型 partial Weil configuration 的第四负迹预算；没有构造
上同调分次、Frobenius 或极化，也不建立两类 Weil 结构的等价。

## 11. 下一最小引理 [O]

路线 A1g：relative-dense fourth trace 到 zero counting 的接口审计。从
Alpöge--Furman 的有限矩阵定义出发逐式重证：

1. good height \(t_I\) 对应的 zero block 覆盖范围；
2. rank、trace、二矩与第四矩正规化；
3. \(13/18\) Christoffel 与 \(16/21\) inertia 证书的量词；
4. 若 relative-dense selection 不足，给出最小额外 averaged/covering lemma；
5. 若足够，才把式 (51) 转化为新的比例定理。

若某步要求所有高度成立或先知道 simple zeros，必须标为新开放输入或形成
obstruction，不能把 relative-dense good heights 偷换成全局渐近。

## 12. 可复现检查 [E]

脚本 scripts/mixed_background_evacuation_audit.py 检查：

1. \((\Lambda*\Lambda)(p^k)=(k-1)(\log p)^2\)；
2. mixed sign walk 的 product-support 分类；
3. 式 (39)--(46) 相对于 \(N=XL\) 的指数预算；
4. whole-trace selection 后的 Schatten 三角；
5. MT 常数的分项相加。

脚本不实现 Henriot 定理、不证明 prime asymptotics，也不执行 zero-counting
接口，因此不能单独作为零点比例证据。

## 13. 后续更新（笔记 228）

笔记 228 已闭合本笔记留下的 zero-block coverage 量词。若把 Gabor grid 起点从
`T` 平移到本笔记选出的 `u in [T,T+T/sqrt(log T)]`，对应 AF 零点块从
`[T,2T]` 平移为 `[u,u+T+O(1/log T)]`；两块对称差中的零点只有 `o(N)`。
因此 relative-dense good heights 足以传回固定 dyadic 与累计计数。

当前中心二矩 `v_MT=0.3274992963...` 与本笔记中心四矩前件
`B_MT=0.2525089687...` 通过 quartic rank--trace--inertia certificate 形式上给
simple/distinct 常数 `0.7569026657...`、`0.8784513329...`。该逻辑蕴含已证明，
但由于它会构成记录级改进，项目把无条件实例保持为 `[C]`，下一步改为对笔记
203--227 的 prime-side 链作逆向独立复核。当前数据没有第三矩，不能直接调用
AF 的 `13/18` Christoffel 数值；笔记 228 给出了严格的数据不足反例。

## 14. 后续逆审计（笔记 229--230）

笔记 229 已按 Henriot 2014 勘误把 shifted-sieve 外部输入改用 corrected
`rho-check_R`，并证明对 primitive monic `X,X+h` 的上界及 `z_j->0` 统一性不变；
Bettin--Chandee/单序列 Selberg level 也通过核验。笔记 230 又从十二条 raw paired
paths 和六个 mixed placements 独立恢复 `D_22`、`D_0`、`D_mix` 的全部重数与
MT 总常数 `0.252508968714...`。这些通过项仍不替代笔记 218--225 内部
Fejer/box/frozen-grid 拼装的剩余逆审计，故记录级比例保持 `[C]`。

## 15. 后续逆审计修复（笔记 231）

笔记 231 发现笔记 225 的 pure-prime 输入漏列 central--primitive alternating
cross，并用已在本笔记定理 227-E 审计的 shifted prime-pair bound 将其短高度
signed mean压到 `o(N)`。该项加入 whole-fourth-trace average 后不改变
`D_0,D_mix,D_22`，也不需要第二次 good-height selection。因此定理 227-I 的
pure-prime 前件经此局部修复恢复；记录级比例仍等待其余 box/frozen-grid 全链复核。

## 16. 后续高乘积漏区修正（笔记 232）

本笔记的 mixed-frequency evacuation、共同高度选择与候选常数重建保持 [T]/[E]。
笔记 232 发现纯素数 alternating family 的 `ab>XL^2` primitive off-diagonal 尚未
进入该共同账本。因此 `0.2525089687...` 继续只能作为 [C] 实例，不能升级为
Riemann zeta 的无条件第四矩常数。
