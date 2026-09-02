# 217. Discriminant-uniform sieve 闭合 transition resolution core

日期：2026-09-02

分支：MOM-1 / 路线 A2，接口 NCE-8 / alternating transition Gram

状态：transition resolution core 的 absolute main term 为 [T]；证明使用
Henriot 文中记录的 Holowinsky discriminant-uniform shifted-multiplicative
upper bound [R]，并审计 2014 erratum；affine lattice fiber identity 与
coherent-clique necessary condition 为 [T]；有限 core spectra 为 [E]；
oscillatory tail 仍为 [O]。本笔记不更新 PDF。

## 1. 本轮结论

令

\[
 L=\log X,
 \qquad
 0<\delta<1
\tag{1}
\]

固定。笔记 216 把 transition layer 的 scalar determinant kernel 分成

\[
 |ad-bc|\lesssim H_{\rm res}(R)=R/X
\tag{2}
\]

的 nonoscillatory core 与其补集。原下一目标要求 core 相对于 atomic
diagonal 满足 uniform constant frame bound。本轮证明该条件远强于所需：

\[
 \boxed{
  \mathscr K_{\rm core}(X;\delta)
  \ll_\delta
  N L^{-(1-\delta)/2}(\log L)^5
  =o(N).}
\tag{3}
\]

这里 \(\mathscr K_{\rm core}\) 是所有 transition cells 的 off-diagonal
core main terms 的**绝对值总和**。所以 resolution core 已无条件闭合，
甚至不需要 height-phase cancellation。

证明的新输入不是 Evans 的 almost-all \(E_2\) asymptotic。它是对一般
multiplicative functions 的 discriminant-uniform upper-bound sieve。取

\[
 f_z(n)=z^{\Omega(n)},
 \qquad
 z=\frac2{\log\log R},
\tag{4}
\]

即可为 \(\Omega(n)=2\) 的支撑提取足够的 log density。

另一方面，有限谱实验发现 core graph 含有真实 affine prime-power cliques。
例如在 \(X=10^4\) 时，

\[
 (23,3449),(27,4049),(29,4349),(31,4649),(32,4799)
\tag{5}
\]

全部满足 \(b=150a-1\)，故任意两点的 determinant 等于两个 numerators
之差，并且绝对值不超过 \(\log 10^4\)。这说明逐层 degree-two 不能直接
升级成所有 small determinants 的 constant-degree statement。式 (3) 绕过
了这个不必要的 maximal obstruction，只控制全局 weighted mass。

## 2. 外部 discriminant-uniform sieve 输入

### 外部定理 217-A（Henriot--Holowinsky upper bound）[R]

令 \(\lambda_1,\lambda_2\) 为 multiplicative functions，且对某个固定
\(m\) 有

\[
 |\lambda_i(n)|\le \tau_m(n).
\tag{6}
\]

对每个固定 \(0<\varepsilon<1\)，一致于
\(1\le |h|\le x\)，有

\[
 \begin{aligned}
 \sum_{n\le x}
 |\lambda_1(n)\lambda_2(n+h)|
 \ll_{\varepsilon,m}{}&
 \tau(|h|)\frac{x}{(\log x)^{2-\varepsilon}}\\
 &\times
 \prod_{p\le x}
 \left(1+\frac{|\lambda_1(p)|}{p}\right)
 \left(1+\frac{|\lambda_2(p)|}{p}\right).
 \end{aligned}
\tag{7}
\]

这是 Henriot 论文 Introduction, Theorem 2 中记录的 Holowinsky bound；
Henriot 的 Theorem 3/5 给出更精确的 discriminant factor。本文只需式 (7)。

来源：

- Roman Holowinsky, *A sieve method for shifted convolution sums*, Duke Math.
  J. 146 (2009), 401--448；
- Kevin Henriot, *Nair--Tenenbaum bounds uniform with respect to the
  discriminant*, Math. Proc. Cambridge Philos. Soc. 152 (2012), 405--424；
- Kevin Henriot, erratum, ibid. 157 (2014), 375--377。

勘误明确说明原论文的 upper bounds 仍有效；主要错误是 Theorem 6 的 lower
bound 及由此声称的 sharpness。这里不使用 lower bound、sharpness 或
Theorem 6。

式 (7) 的常数只依赖固定的 \(\varepsilon,m\)，所以允许本证明中的
\(z=z(R)\in(0,1]\)。这点是优化式 (4) 的必要 uniformity。

## 3. 两个 almost-primes 的逐 shift 上界

记

\[
 \mathbf e_2(n)=\mathbf 1_{\Omega(n)=2},
 \qquad
 \ell=\log R.
\tag{8}
\]

### 引理 217-B（optimized \(\Omega=2\) correlation）[T]

对固定 \(0<\varepsilon<1\)，一致于
\(1\le |h|\le R\)，有

\[
 \boxed{
 \sum_{R<n\le2R}
 \mathbf e_2(n)\mathbf e_2(n+h)
 \ll_\varepsilon
 \tau(|h|)
 \frac{R(\log\ell)^4}{\ell^{2-\varepsilon}}.}
\tag{9}
\]

#### 证明

对充分大 \(R\)，置

\[
 z=\frac2{\log\ell}\le1,
 \qquad
 f_z(n)=z^{\Omega(n)}.
\tag{10}
\]

则 \(f_z\) multiplicative、\(0\le f_z\le1\)，且

\[
 \mathbf e_2(n)\le z^{-2}f_z(n).
\tag{11}
\]

由非负性把 \(R<n\le2R\) 的和放大到式 (7) 中的 \(x=3R\)，并取
\(\lambda_1=\lambda_2=f_z\)、\(m=1\)。负 shift 交换两个 factors。Mertens upper
bound 给

\[
 \prod_{p\le 3R}\left(1+\frac z p\right)^2
 \ll
 \exp\left(2z\sum_{p\le3R}\frac1p\right)
 \ll \ell^{2z}\ll1,
\tag{12}
\]

因为 \(2z\log\ell=4\)。再由
\(z^{-4}\asymp(\log\ell)^4\) 得式 (9)。
\(\square\)

这里没有假设 fixed-shift Hardy--Littlewood asymptotic。式 (9) 是上界筛，
并保留显式 \(\tau(h)\) 依赖。

## 4. \(\Lambda*\Lambda\) 的逐 shift 上界

令

\[
 \mathcal A(n)=(\Lambda*\Lambda)(n).
\tag{13}
\]

沿用笔记 214-D 的非负分解

\[
 \mathcal A=\mathcal A_{oo}+\mathcal E,
\tag{14}
\]

其中 \(\mathcal A_{oo}\) 只保留两个 odd primes，而 factor \(2\) 与至少
一个 proper prime power 的项进入 \(\mathcal E\)。在固定倍区间上，

\[
 \sum_{n\le CR}\mathcal E(n)\ll_C R,
 \qquad
 0\le\mathcal A(n)\le(\log n)^2,
\tag{15}
\]

并且

\[
 \mathcal A_{oo}(n)\le2(\log n)^2\mathbf e_2(n).
\tag{16}
\]

为验证式 (15) 的 pointwise bound：若 \(n\) 含多于两个 prime bases，则
\(\mathcal A(n)=0\)；若 \(n=p^iq^j\)、\(p\ne q\)，则
\(\mathcal A(n)=2\log p\log q\le(\log n)^2\)；若 \(n=p^k\)，则
\(\mathcal A(n)=(k-1)(\log p)^2\le(\log n)^2\)。这不使用平均估计。

### 定理 217-C（uniform short determinant correlation）[T]

对固定 \(C>1\)、\(0<\varepsilon<1\)，一致于
\(1\le |h|\le R\)，有

\[
 \boxed{
 \sum_{R<n\le2R}
 \mathcal A(n)\mathcal A(n+h)
 \ll_{C,\varepsilon}
 \tau(|h|)R\ell^{2+\varepsilon}(\log\ell)^4
 +R\ell^2.}
\tag{17}
\]

#### 证明

式 (16) 与引理 217-B 给 \(\mathcal A_{oo}\mathcal A_{oo}\) 项的第一项。
对任何至少含一个 \(\mathcal E\) 的项，使用式 (15)：例如

\[
 \sum_{R<n\le2R}\mathcal E(n)\mathcal A(n+h)
 \le
 \sup_{m\le CR}\mathcal A(m)
 \sum_{n\le CR}\mathcal E(n)
 \ll R\ell^2.
\tag{18}
\]

交换 factors 及 \(\mathcal E\mathcal E\) 相同。
\(\square\)

## 5. Transition resolution core 的 absolute closure

定义 transition atom set

\[
 \mathcal T_\delta
 =
 \{(a,b):
 XL^{1-\delta}\le ab\le XL^{1+\delta},
 \ \Lambda(a)\Lambda(b)\ne0\},
\tag{19}
\]

并令

\[
 m=ad,
 \qquad
 n=bc.
\tag{20}
\]

把笔记 216-A 的 off-diagonal main kernel 限制到

\[
 0<|m-n|\le C\frac{\min(m,n)}X.
\tag{21}
\]

其绝对值总和记为 \(\mathscr K_{\rm core}(X;\delta)\)。定义中保留全部
product/ratio cells 和 six-window weights；证明上界时才利用非负性删除这些
restrictions。

### 定理 217-D（transition core absolute closure）[T]

式 (3) 成立。

#### 证明

按

\[
 R<\min(m,n)\le2R
\tag{22}
\]

作 dyadic decomposition。若式 (21) 非空，则 \(R\gg X\)；由

\[
 mn=(ab)(cd)\le X^2L^{2+2\delta}
\tag{23}
\]

及 \(m\asymp n\)，有

\[
 R\ll XL^{1+\delta},
 \qquad
 \log R\asymp L.
\tag{24}
\]

记 \(H_R=CR/X\)。由
\(0\le W_{a,b;c,d}\le1\)、
\(|\mathcal D_{d_G}|\le d_G\)，并删除 factorization/cell restrictions，
该 dyadic range 的 absolute main term至多

\[
 C\beta_L^4d_G\frac1R
 \sum_{1\le |h|\le H_R}
 \sum_{n\asymp R}
 \mathcal A(n)\mathcal A(n+h).
\tag{25}
\]

这里 \(R^{-1}\) 来自
\((mn)^{-1/2}\asymp R^{-1}\)，而
\(\mathcal A(m)\mathcal A(n)\) 正是删除 restricted factorizations 后的
四个 von Mangoldt factors。

取

\[
 \varepsilon=\frac{1-\delta}{2}>0.
\tag{26}
\]

由定理 217-C 与 elementary divisor average

\[
 \sum_{h\le H}\tau(h)\ll H\log(2H),
\tag{27}
\]

式 (25) 至多

\[
 \begin{aligned}
 &C_\delta\beta_L^4d_G R^{-1}
 \left[
 RH_RL^{2+\varepsilon}(\log L)^5
 +RH_RL^2
 \right]\\
 &\qquad\ll_\delta
 R L^{-1+\varepsilon}(\log L)^5+\frac RL,
 \end{aligned}
\tag{28}
\]

其中使用 \(\beta_L^4d_G\asymp X/L^3\) 与 \(H_R\asymp R/X\)。

对 dyadic \(R\) 求和是 geometric sum，故由式 (24)

\[
 \begin{aligned}
 \mathscr K_{\rm core}(X;\delta)
 &\ll_\delta
 XL^{\delta+\varepsilon}(\log L)^5+XL^\delta\\
 &=N\left[
 L^{-(1-\delta)/2}(\log L)^5+L^{\delta-1}
 \right],
 \end{aligned}
\tag{29}
\]

即式 (3)。\(\square\)

式 (3) 闭合的是 bulk translated-symbol 的 core main term。笔记 216-I 的
aliases 与 Hankel remainder 预算不会制造新的 small-determinant arithmetic
input；但在 tail 尚未控制前，不能仅由 aggregate finite defect 的小范数把一个
人工截断的 core Gram 单独搬回 finite matrices，因为相应交叉误差仍依赖整体
bulk aggregate norm。正确的 finite transfer 应在 tail 闭合、整体 bulk norm
已受控后统一执行。本定理不提前声称 standalone finite-core decomposition。

## 6. Affine determinant fibers

core 的有限谱并非 atomwise bounded-degree。其精确算术原因如下。

### 引理 217-E（affine lattice fiber identity）[T]

令 \((p,q)\in\mathbb Z^2\) primitive，
\((a_0,b_0)\in\mathbb Z^2\)，并置

\[
 r=a_0q-b_0p\ne0,
 \qquad
 v_t=(a_0+tp,b_0+tq).
\tag{30}
\]

则对任意整数 \(s,t\)，

\[
 \boxed{\det(v_t,v_s)=r(s-t).}
\tag{31}
\]

#### 证明

直接展开：

\[
 \begin{aligned}
 &(a_0+tp)(b_0+sq)-(b_0+tq)(a_0+sp)\\
 &\qquad=(s-t)(a_0q-b_0p).
 \end{aligned}
\]

\(\square\)

因此一条 affine fiber 上所有同时为 prime powers 的点，只要其 parameter
diameter 不超过 \(CH_{\rm res}/|r|\)，就形成 complete determinant-core
clique。

### 定理 217-F（coherent-fiber necessary condition）[T]

考虑同一 affine fiber 上的 \(M\) 个 transition atoms \(v_{t_j}\)。设：

1. 它们对应的 cross products 均 \(\asymp R\)；
2. \(|r|\max_{i,j}|t_i-t_j|\le cR/X\)，其中 \(c>0\) 足够小；
3. normalized six-window overlaps 有一致下界 \(w_0>0\)。

则其 normalized core main Gram 的最大 eigenvalue 满足

\[
 \lambda_{\max}\ge 1+c_1(w_0)M.
\tag{32}
\]

#### 证明

由式 (31) 与 logarithm mean-value theorem，所有 ratio-log differences
满足 \(|\Delta_{ij}|\ll c/X\)。笔记 216-B 的 centered Dirichlet formula
给

\[
 e^{i\alpha_*\Delta_{ij}}
 \frac{\sin(d_Gh_0\Delta_{ij}/2)}
      {d_G\sin(h_0\Delta_{ij}/2)}.
\tag{33}
\]

取 \(c\) 足够小，式 (33) 的 real sinc factor 有正下界。以 diagonal unitary
\(\operatorname{diag}(e^{-i\alpha_*s_j})\) conjugate 后，全部 normalized
entries 的实部至少为只依赖 \(w_0\) 的正常数。对 all-ones vector 应用
Rayleigh quotient 即得式 (32)。\(\square\)

这说明 uniform atomwise frame bound 会强迫每条短 affine prime-power fiber
的一致 occupancy bound。式 (3) 并不需要这个极强的 maximal statement；
它只使用所有 shifts 的 weighted upper-bound sieve 总预算。

## 7. Exact finite certificate 与谱实验

在 \(X=10^4\) 时，式 (5) 的五个点满足

\[
 b=150a-1,
 \qquad
 150a-b=1.
\tag{34}
\]

它们的每个 coordinate 都是 prime power，且 products 位于实验采用的
\(XL^{0.75}\le ab\le XL^{1.25}\) band。由引理 217-E，任意两点的
determinant 为 parameter difference，最大为 \(9<\log10^4\)。因此这是
一个 exact five-vertex core clique [T]。

脚本 `scripts/transition_core_frame_audit.py` 对 exact flat-window kernel 做
diagonal normalization，并用 sparse Lanczos 测量实际 Hermitian 最大特征值：

| \(X\) | vertices | mean degree | max Schur row | \(\lambda_{\max}\) | largest affine clique |
|---:|---:|---:|---:|---:|---:|
| 300 | 632 | 0.3165 | 1.0471 | 1.9209 | 2 |
| 600 | 1294 | 0.3771 | 1.6307 | 2.3864 | 4 |
| 1200 | 2570 | 0.3393 | 1.8334 | 2.7466 | 3 |
| 2500 | 5550 | 0.2941 | 2.0336 | 2.6881 | 3 |
| 5000 | 11562 | 0.3377 | 2.2359 | 2.9266 | 4 |
| 10000 | 23180 | 0.3009 | 3.1546 | 3.7929 | 5 |
| 50000 | 120466 | 0.2701 | 2.6470 | 3.4001 | 4 |

最后一行可由模块入口调用 `audit_core(50000, 1.0)` 复现。所有谱值是 [E]，
不是 uniform asymptotic。它们只说明 average degree 很小与 maximal coherent
fiber 可以同时发生；这正是式 (3) 采用全局筛预算而不追求 maximum-degree
bound 的原因。

## 8. 修正后的下一最小引理 217-G [O]

resolution core 已由定理 217-D 绝对闭合。下一输入只剩 oscillatory tail：

\[
 |ad-bc|>C\frac{\min(ad,bc)}X.
\tag{35}
\]

必须保留 centered phase、Dirichlet sinc 与 six-window overlap，证明所有
transition product/ratio cells 的 signed tail 总和为 \(o(N)\)。不能再用
普通 harmonic absolute majorant：在 transition scale，它自然停在主尺度。

下一轮优先测试两种可证伪分解：

1. 沿 affine fibers \(v_t=v_0+t(p,q)\) 对真实 sinc kernel 做一维
   large-sieve/Cotlar bound；
2. 把不同 affine fibers 的交叉项写成 response-specific bilinear form，检查
   centered height phase 是否给出全局 \(R/X\)-scale cancellation。

若两者均只能恢复 absolute harmonic budget，则应形成 tail no-go，而不是重新
引入已经不需要的 constant core frame axiom。

## 9. 公理作用、删除审计与循环性

1. **discriminant-uniform shifted sieve**：给式 (9) 的逐 shift density saving；
   删除后 Cauchy 只给 \(O(RL^3)\) per shift，core 总预算恰停在 \(O(N)\)。
2. **\(z^{\Omega}\) optimization**：把 exactly-two-prime support 转成 uniform
   multiplicative majorant；固定 \(z\) 会损失一个固定 log power。
3. **prime-power error mass**：把 \(\Lambda*\Lambda\) 与 odd prime-prime
   support 的差独立压到式 (18)；不能假装 \(\Lambda*\Lambda\) 本身
   multiplicative。
4. **Dirichlet resolution cutoff**：使 shift count 只有 \(R/X\)；若把 core
   扩到 fixed proportion of \(R\)，式 (29) 不再是 little-oh。
5. **transition product ceiling**：式 (23)--(24) 把 dyadic geometric sum
   限制在 \(XL^{1+\delta}\)；需要 \(\delta<1\) 才能选择式 (26)。

删除审计：

- 只用 second moment/Cauchy 给每 shift \(O(RL^3)\)，对 \(R/X\) 个 shifts
  求和后正好失去式 (3) 的 log saving。
- 只用 fixed-\(h\) degree two 不能控制并集；式 (5) 已给 exact five-clique。
- uniform constant frame 是充分但非必要条件；继续追求它会把问题错误升级成
  maximal short prime-tuple statement。
- Henriot erratum 不可省略；本证明明确避开被修正的 lower-bound sharpness。

循环性审计：全部输入在 prime side，且只使用已发表 upper-bound sieve、
elementary divisor average、local prime-power mass 与 exact Toeplitz kernel。
不使用 RH、GRH、零点比例、Weil positivity、谱酉性或 fixed-shift
Hardy--Littlewood conjecture。

## 10. 模型范围与部分 Weil 接口

- **Riemann zeta**：定理 217-D 直接闭合当前 alternating transition core。
- **Dirichlet \(L\)**：单位 character phases 在 absolute core 上消失，所以同一
  closure 保留；tail 会改变。
- **Dedekind/automorphic \(L\)**：需要把式 (7) 替换成相应 coefficient-support
  sieve；不能从 Rankin--Selberg second moment 自动推出。
- **函数域**：\(z^{\Omega}\) sieve 对应多项式因子数筛，可能给更强的 exact
  degree bound。
- **负向 spectral models**：没有 Euler product/prime-power support 时，式
  (14)--(18) 不存在，说明该 closure 是独立算术输入，不是函数方程改写。

在部分 Weil 配置中，定理 217-D 把 prime-side negative/excess budget 的
nonoscillatory transition component严格降为 \(o(N)\)。剩余障碍已经唯一化到
actual response 的 oscillatory tail，而不是抽象 positivity。
