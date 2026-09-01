# NCE-9：finite satisfiability 与 Brownian response 的非构造补全

文档 174 说明：若“类 Weil 结构”已经包含完整 divisor 与正极化，则裸存在性
与 RH/GRH 等价；紧致性不能免费制造正性。文档 194--195 则给出一个更小的
response-level structure：一个 scalar constant mode \(T\) 与一个
\(L^2\) primitive \(A\) 已足以控制 direct Cauchy response。

本笔记证明一个严格的非构造补全定理：

> 若每个有限 arithmetic test family 都能以同一个 Sobolev/Brownian budget
> 实现，则无需显式构造相容解；弱紧致性自动给出同时实现全部 tests 的全局
> response package。

进一步，有限可满足性等价于一族显式 finite Gram/Schur inequalities。这给
“不具体构造数域类 Weil 结构”一个精确可行版本，同时也显示其边界：统一预算
仍是必须由 primes、Gamma 与 continuum 证明的算术输入。

## 1. Response-level package

取 test space

\[
\Phi\subset H^1(\mathbb R),                       \tag{1}
\]

并设 \(b:\Phi\to\mathbb C\) 是从 finite Euler/Gamma/continuum explicit
formula 得到的 linear response datum。这里 \(b(\phi)\) 必须在 length side
直接定义，不能由未知 zeros 的位置定义。

一个 Brownian response package 是

\[
(T,A)\in\mathbb C\oplus L^2(\mathbb R)            \tag{2}
\]

使对全部 \(\phi\in\Phi\)，

\[
b(\phi)
=T\phi(0)-\int_{\mathbb R}A(x)\phi'(x)\,dx.       \tag{3}
\]

它定义 distribution

\[
q=T\delta_0+DA.                                   \tag{4}
\]

若 \(q\) 原本是 finite atomic response，则 \(T=q(\mathbb R)\)，而 \(A\)
就是文档 194 的 centered primitive。式 (2)--(4) 允许极限对象只是
\(H^{-1}\)-distribution；这是 response structure，不冒充完整 motivic
cohomology 或 measure-valued Euler product。

赋予

\[
\mathcal X=\mathbb C\oplus L^2(\mathbb R),\qquad
\|(T,A)\|_{\mathcal X}^2=|T|^2+\|A\|_2^2.         \tag{5}
\]

## 2. 无相容选择的弱紧致补全

### 定理 AHH（finite satisfiability compactness theorem）[U]

设 \(C<\infty\)。假设对每个 finite subset
\(\Phi_0\subset\Phi\)，都存在一个可能依赖 \(\Phi_0\) 的
\((T_{\Phi_0},A_{\Phi_0})\in\mathcal X\)，满足

\[
\|(T_{\Phi_0},A_{\Phi_0})\|_{\mathcal X}\le C     \tag{6}
\]

以及

\[
b(\phi)
=T_{\Phi_0}\phi(0)
-\int A_{\Phi_0}(x)\phi'(x)\,dx
\quad(\phi\in\Phi_0).                             \tag{7}
\]

则存在单个 \((T,A)\in\mathcal X\)，满足式 (3) 对全部
\(\phi\in\Phi\) 成立，且

\[
\|(T,A)\|_{\mathcal X}\le C.                     \tag{8}
\]

特别地，不需要预先选择 finite solutions 的相容子网。

#### 证明

令 \(K_C\) 是 \(\mathcal X\) 中半径 \(C\) 的闭球。Hilbert space 是
reflexive，故 \(K_C\) 在 weak topology 下 compact。对每个
\(\phi\in\Phi\)，令

\[
F_\phi=\{(T,A)\in K_C:
T\phi(0)-\int A\phi'=b(\phi)\}.                   \tag{9}
\]

因为 \(\phi'\in L^2\)，式 (9) 是 weakly closed affine subset。
假设 (6)--(7) 说明集合族 \((F_\phi)_{\phi\in\Phi}\) 有 finite
intersection property。compactness 给

\[
\bigcap_{\phi\in\Phi}F_\phi\ne\varnothing.        \tag{10}
\]

任取交中的 \((T,A)\) 即得结论。\(\square\)

Hermitian symmetry、指定的 scalar normalization 以及任意由 weakly
continuous linear functionals 表达的 Gamma boundary conditions，都可作为
额外 closed constraints 加入同一证明。

## 3. 有限 Gram 判据

对 \(\phi,\psi\in\Phi\) 定义 Sobolev--Brownian kernel

\[
\mathcal K(\phi,\psi)
=\phi(0)\overline{\psi(0)}
+\int_{\mathbb R}\phi'(x)\overline{\psi'(x)}\,dx. \tag{11}
\]

给 finite family \(J=(\phi_1,\ldots,\phi_m)\)，记

\[
K_J=(\mathcal K(\phi_i,\phi_j))_{i,j},\qquad
b_J=(b(\phi_i))_i.                                \tag{12}
\]

### 定理 AHI（finite Gram/Schur existence criterion）[U]

以下条件等价：

1. 存在 norm 至多 \(C\) 的 Brownian response package 实现全部
   \(\Phi\)；
2. 对每个 finite \(J\subset\Phi\)，

\[
\begin{pmatrix}
K_J&b_J\\
b_J^*&C^2
\end{pmatrix}\succeq0;                            \tag{13}
\]

3. 对每个 finite \(J\)，\(b_J\in\operatorname{ran}K_J\)，且

\[
b_J^*K_J^\dagger b_J\le C^2.                     \tag{14}
\]

这里 \(K_J^\dagger\) 是 Moore--Penrose inverse。

#### 证明

令

\[
\ell_\phi(T,A)=T\phi(0)-\int A\phi'.              \tag{15}
\]

这些 functionals 在 \(\mathcal X\) 中的 Riesz representers 的 Gram 正是
式 (11)。有限 Hilbert interpolation 的最小 norm 平方为
\(b_J^*K_J^\dagger b_J\)，可解条件为
\(b_J\in\operatorname{ran}K_J\)。这证明 finite system 有 norm 至多 \(C\)
的解当且仅当式 (14) 成立。generalized Schur complement 又给式 (13) 与
式 (14) 等价。最后定理 AHH 把全部 finite systems 补全为 global solution。
\(\square\)

式 (13) 是一个真正有限、可证伪的非构造存在性接口。它只涉及：

- test functions 的显式 Sobolev Gram \(K_J\)；
- length-side arithmetic responses \(b_J\)；
- 一个所有 finite sets 共用的 constant \(C\)。

它避免构造 \(A\)，也避免在不同 finite levels 之间手工选择 compatible
solutions。

## 4. Direct Cauchy 与 generalized Weil 接口

取

\[
K_C(x)=e^{-|x|}\in H^1(\mathbb R).               \tag{16}
\]

对定理 AHH 得到的 package，定义

\[
b(K_C)=T-\int A(x)K_C'(x)\,dx.                   \tag{17}
\]

因为 \(\|K_C'\|_2=1\)，

\[
|b(K_C)|\le |T|+\|A\|_2\le\sqrt2\,C.             \tag{18}
\]

### 推论 AHJ（nonconstructive Brownian--Weil completion）[C]

设一族 cofinal canonical soft responses 的全部 finite arithmetic constraints
满足式 (13)，且同一个 \(C\) 对全部 cofinal levels 与 finite test families
有效。再假设文档 149、187、194 所需的 self-duality、finite-trace、
approximation 与 tail ledgers 一致成立，则 weak compactness 自动产生所需
global response packages，而对应 divisor 位于中心线。

非构造步骤只负责：

1. 消除 finite solutions 的 compatibility/choice 问题；
2. 取得 weak \(L^2\) primitive limit；
3. 保留式 (18) 的 Brownian budget。

它不负责证明式 (13) 的 uniform constant。

## 5. 与“裸存在性”的区别

文档 174 命题 AEH 排除的是：

\[
\text{完整 divisor + 完整 trace + positive polarization 的裸存在性}. \tag{19}
\]

定理 AHH--AHI 处理的是更窄的命题：

\[
\text{length-side finite responses + uniform Sobolev Gram budget}
\Longrightarrow
\text{global response distribution}.             \tag{20}
\]

式 (20) 有三个真实优点：

1. finite witnesses 可以彼此不相容；
2. existence 被化为明确的 finite block PSD 条件 (13)；
3. limit primitive 不需显式公式。

但它没有自动给：

- convolution multiplication 在 weak \(L^2\) limit 下的连续性；
- Euler product 或 determinant 的全局重建；
- arbitrary Weil tests 的 positivity；
- uniform constant \(C\)。

尤其，weak convergence \(A_n\rightharpoonup A\) 不保证 nonlinear convolution
expressions 收敛。若要补全完整代数结构，必须另有 bounded operator
coordinates、strong/weak-star multiplication stability 或 tracial
ultraproduct 定理；不能从本笔记的 response compactness 直接推出。

## 6. 循环性审计

### 情形一：由 zeros 定义 \(b\)

若 \(b(\phi)\) 先由目标 zeros 的 spectral sum 定义，再验证式 (13)，则这是
tautological Hilbert realization，路线立即停止。

### 情形二：由 primes/Gamma 定义 \(b\)，但 tests 已完备

若 \(\Phi\) 足够稠密，且 uniform \(C\) 经文档 194 推论 AHD 已推出 RH，
那么“对全部 finite \(J\) 的式 (13) 使用同一 \(C\)”也具有 RH 强度。
compactness 并未降低这个 bound 的逻辑强度，只把无限 compatibility 变成有限
PSD verification。

### 情形三：局部算术定理给 uniform finite feasibility

这是本路线唯一可能产生新突破的区域：若 Type I/II incidence、Gamma boundary
与 continuum gauge 能直接证明每个 finite block matrix (13) positive，且
constant 不随 \(J\) 或 scale 增长，则定理 AHI 无需构造 global primitive 就
给出结构存在。这会是一个真正的非构造性数域类 Weil existence theorem。

## 7. 与文档 195 的汇合

文档 195 把一个 canonical degree-two response 分成
Type I/Type II/continuum primitives \(U_r\)，并得到 finite channel Gram
\(G\)。本笔记提供两种非构造补全方式：

1. 对 all-ones physical response，只把 \(\sum_rU_r\) 作为 \(A\)，应用
   定理 AHH；
2. 在 direct-sum Hilbert space 同时保留各 \(U_r\)，把 channel cross moments
   加入 finite constraints，再应用同一 compactness proof。

第二种保留 provenance，但其 uniform bound 必须直接控制
\(\mathbf1^*G\mathbf1\)，不能用 diagonal-only budget 替代。

## 8. 有限 Cauchy-translate 审计

函数 cauchy_translate_compactness_ledger 使用精确 kernel

\[
\mathcal K(t,s)
=e^{-|t|-|s|}
+(1-|t-s|)e^{-|t-s|},                            \tag{21}
\]

计算式 (13)--(14)。在 \(Y=8,N=10\) 的冻结 degree-two response 上，嵌套
translate families 给：

| tests 数 | translates 范围/加密方式 | captured norm ratio |
|---:|:---|---:|
| 1 | \(\{0\}\) | \(0.0211\) |
| 3 | 加入 \(\{\pm1\}\) | \(0.0283\) |
| 7 | 再加入 \(\{\pm1/2,\pm2\}\) | \(0.0391\) |
| 15 | 再加密并扩到 \(\pm3\) | \(0.1453\) |
| 33 | 步长 \(1/4\)，范围 \([-4,4]\) | \(0.2293\) |

每个 finite block 在 actual package norm 作为 budget 时均 PSD；最小-norm
quotient 随嵌套 test family 单调增加。33 个 tests 仍只捕获约 \(23\%\)，说明
很小的 translate family 不能被误当成完整 Brownian energy。这既验证定理 AHI，
也给下一步一个停止审计：若 arithmetic generator family 必须趋于稠密才能获得
足够强的 bound，它可能逐渐恢复完整 criterion。

这些 double-precision values 只验证 finite interpolation algebra，不是 RH
证据或 interval certificate。

## 9. 下一最小引理与停止条件

### 最小引理 NCE-9.1

选定一个 finite square-root Vaughan rectangle 与一组 Cauchy translates
\(\phi_j(x)=e^{-|x-t_j|}\)。把 arithmetic responses \(b_J\) 写成文档 195 的
Type I/II/continuum incidence sums，证明 block matrix (13) 的 Schur
complement 可由一个 joint signed large-sieve form 表示。

### 晋级条件

找到不引用 zeros、full Selberg profile 或 arbitrary negative spectral effects
的 uniform finite-block positivity/budget。

### 停止条件

若让 translates \(t_j\) 稠密后，式 (13) 的最优 constant 精确恢复文档 194 的
完整 Brownian energy supremum，且没有更小 arithmetic generator family，
则 NCE-9 只剩等价重述，应降级为 completion lemma 而非 RH 主线。

## 10. 审计结论

“不具体构造类 Weil 结构”在 response level 上确实可行：共同 finite budget
加 weak compactness 足以产生 global Brownian primitive，且 finite
satisfiability 有精确 Gram/Schur 判据。非构造方法真正消除的是相容选择和极限
对象公式；它不能消除 uniform arithmetic budget。下一步应直接研究式 (13)
在 Vaughan Type I/II arithmetic generators 上是否有比 full RH criterion
更弱的证明。
