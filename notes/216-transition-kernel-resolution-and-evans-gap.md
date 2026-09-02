# 216. Transition kernel resolution 与 Evans factor-bin 覆盖障碍

日期：2026-09-02

分支：MOM-1 / 路线 A2，接口 NCE-8 / alternating transition Gram

状态：transition layer 的 exact scalar determinant kernel、Dirichlet
resolution threshold 与 diagonal mass saving 为 [T]；Evans Theorem 1.1/1.3
对 balanced polylog-shift cells 的覆盖缺口为 [N]；有限 signed-kernel 分层为
[E]；uniform transition frame bound 为 [O]。本笔记不更新 PDF。

## 1. 本轮结论

固定 \(0<\delta<1\)。笔记 215 把完整 primitive atomic diagonalization 推进到
\(ab\le X(\log X)^\kappa\)、任意 fixed \(\kappa<1\)，并把下一输入放在

\[
 X L^{1-\delta}\le ab,cd\le X L^{1+\delta},
 \qquad L=\log X.
\tag{1}
\]

本轮得到四个结论。

第一，transition bulk Gram 的 Toeplitz main term 可逐 cell 精确写成一个
scalar determinant sum：

\[
 \boxed{
 \beta_L^4
 \sum_{k=0}^{d_G-1}
 \sum_{a,b,c,d}
 b_ab_bb_cb_d\,W_{a,b;c,d}
 e^{i(T+kh_0)\log(ad/bc)}.}
\tag{2}
\]

这里 \(W_{a,b;c,d}\in[0,1]\) 是 exact translated six-window overlap。
所以矩阵问题已经严格降为 response-weighted shifted correlation；但
product-cell restrictions 使它不是简单的
\((\Lambda*\Lambda)(m)(\Lambda*\Lambda)(n)\) 乘积。

第二，若

\[
 m=ad,\qquad n=bc,\qquad r=m-n,\qquad m,n\asymp Y,
\tag{3}
\]

则 finite Dirichlet factor 的分辨率阈值为

\[
 \boxed{H_{\rm res}(Y)=Y/X.}
\tag{4}
\]

在 central transition scale \(Y\asymp XL\) 上，恰有
\(H_{\rm res}\asymp L\)。因此：

- \(|r|\lesssim L\) 是 nonoscillatory resolution core；
- \(|r|\gg L\) 是带 \(L/|r|\) envelope 的 oscillatory tail。

第三，整个式 (1) transition layer 的 atomic diagonal mass 已经是

\[
 \boxed{
 \sum_{(a,b)\in\mathcal T_\delta}
 \|F_{a/b}^{bulk}\|_{HS}^2
 \ll
 N\frac{\log L}{L}
 =o(N).}
\tag{5}
\]

所以闭合 transition layer 不需要证明每个 cross term 绝对可和；一个
uniform constant frame bound 相对于 transition diagonal 就已经足够。

第四，已发表的 Evans 输入不能直接提供这个 frame bound：

- Theorem 1.1 可到 \(H\ge L^{19+\varepsilon}\)，但只处理一个由 \(H\)
  指定的 small-factor window \(E_2'(P)\)；
- Theorem 1.3 处理 general \(E_2\)，但要求
  \(H\ge\exp((\log Y)^{1-\varepsilon})\)；
- balanced factor cells 与 polylog shifts 同时落在二者覆盖之外。

这不是说所需 correlation estimate 为假；它是对现有文献输入的严格
scope obstruction。

## 2. Exact response-weighted determinant kernel

沿用笔记 214 的 notation，并把 Gabor matrix dimension 记为 \(d_G\)，
以区别 arithmetic denominator \(d\)：

\[
 s=\log(a/b),\qquad t=\log(c/d),\qquad \Delta=s-t=\log(ad/bc).
\tag{6}
\]

把 coefficient 从 singleton symbol 中提出，写

\[
 Q_{a/b}(u)=b_ab_b\,P_{a/b}(u),
\tag{7}
\]

其中

\[
 P_{a/b}(u)
 =\phi(u)\phi(u-s)\phi(x_a-u)^2.
\tag{8}
\]

定义 normalized translated overlap

\[
 W_{a,b;c,d}
 =
 \widehat{P_{a/b}P_{c/d}^{[\Delta]}}(0)
 =
 \frac1L\int_{-L/2}^{L/2}
 P_{a/b}(u)P_{c/d}(u-\Delta)\,du.
\tag{9}
\]

由 \(0\le\phi\le1\)，有

\[
 0\le W_{a,b;c,d}\le1.
\tag{10}
\]

### 定理 216-A（exact transition scalarization）[T]

对任意 primitive singleton atom families \(\mathcal U,\mathcal V\)，其
bulk cross Gram 的 translated-symbol main part 精确等于

\[
 \boxed{
 \begin{aligned}
 K_{\mathcal U,\mathcal V}^{main}
 ={}&
 \beta_L^4
 \sum_{\substack{(a,b)\in\mathcal U\\(c,d)\in\mathcal V}}
 b_ab_bb_cb_d\,W_{a,b;c,d}\\
 &\times
 \sum_{k=0}^{d_G-1}
 e^{i(T+kh_0)\log(ad/bc)}.
 \end{aligned}}
\tag{11}
\]

#### 证明

笔记 213-A 的 exact trace identity 给单 atom pair 的 main part

\[
 \beta_L^4 e^{iT\Delta}
 \widehat{Q_{a/b}Q_{c/d}^{[\Delta]}}(0)
 \sum_{k=0}^{d_G-1}e^{ikh_0\Delta}.
\]

由式 (7)--(9)，Fourier zero mode 等于
\(b_ab_bb_cb_dW_{a,b;c,d}\)。再用式 (6) 并求和即得式 (11)。
\(\square\)

式 (11) 是 scalarization，而不是把目标换名为 positivity axiom。它显式保留：

1. 四个 von Mangoldt factors；
2. product/ratio cell restrictions；
3. physical six-window weight；
4. exterior Gabor index \(k\)；
5. actual height phase。

令

\[
 \mathcal R_{\mathcal U,\mathcal V}(r;k)
 =
 \sum_{\substack{(a,b)\in\mathcal U,\ (c,d)\in\mathcal V\\ad-bc=r}}
 b_ab_bb_cb_dW_{a,b;c,d}
 e^{i(T+kh_0)\log(ad/bc)}.
\tag{12}
\]

则式 (11) 等于

\[
 \beta_L^4\sum_{k=0}^{d_G-1}\sum_{r\ne0}
 \mathcal R_{\mathcal U,\mathcal V}(r;k),
\tag{13}
\]

加上 \(r=0\) 的 atomic diagonal。式 (12) 是下一算术输入的明确对象。

## 3. Dirichlet resolution threshold

置

\[
 \mathcal D_{d_G}(\Delta)=\sum_{k=0}^{d_G-1}e^{ikh_0\Delta}.
\tag{14}
\]

### 引理 216-B（exact centered phase and resolution scale）[T]

精确地有

\[
 e^{iT\Delta}\mathcal D_{d_G}(\Delta)
 =
 e^{i\alpha_*\Delta}
 \frac{\sin(d_Gh_0\Delta/2)}{\sin(h_0\Delta/2)},
\qquad
 \alpha_*=T+\frac{d_G-1}{2}h_0.
\tag{15}
\]

若 \(m,n\asymp Y\)、\(|r|=|m-n|\le cY\)，则

\[
 |\Delta|\asymp |r|/Y
\tag{16}
\]

并且

\[
 |\mathcal D_{d_G}(\Delta)|
 \ll
 \min\left(d_G,\frac{LY}{|r|}\right).
\tag{17}
\]

在 \(d_G\asymp XL\)、\(h_0=2\pi/L\) 下，两项交换主导的位置为

\[
 |r|\asymp Y/X=H_{\rm res}(Y).
\tag{18}
\]

此外，当 \(|r|\le c_0Y/X\) 且 \(c_0>0\) 足够小时，有反向界

\[
 |\mathcal D_{d_G}(\Delta)|\gg d_G.
\tag{19}
\]

#### 证明

式 (15) 是有限 geometric sum 的 centered form。式 (16) 由 logarithm
mean-value theorem 得到。再用

\[
 \left|\frac{\sin(d_Gz/2)}{\sin(z/2)}\right|
 \ll\min(d_G,|z|^{-1}),
\qquad z=h_0\Delta,
\]

得到式 (17)。令 \(d_G\asymp XL\)，解
\(d_G\asymp LY/|r|\) 得式 (18)。若
\(d_G|z|\le c\) 足够小，则
\(|\sin(d_Gz/2)|\asymp d_G|z|\)、\(|\sin(z/2)|\asymp|z|\)，得到式 (19)。
\(\square\)

式 (15) 还说明 tail phase 的自然变化尺度也是 \(Y/X\)：因
\(\alpha_*\asymp X\)，

\[
 \alpha_*\Delta\asymp Xr/Y=r/H_{\rm res}(Y).
\tag{20}
\]

所以 transition core 不能靠“快速 oscillation”自动消失；tail 才可能利用
phase cancellation。

## 4. Transition atomic diagonal saving

定义

\[
 \mathcal T_\delta
 =
 \left\{(a,b):
 \Lambda(a)\Lambda(b)\ne0,\qquad
 \operatorname{base}(a)\ne\operatorname{base}(b),\qquad
 XL^{1-\delta}\le ab\le XL^{1+\delta}
 \right\}.
\tag{21}
\]

### 引理 216-C（local \(\Lambda^2/n\) shell budget）[T]

一致地有

\[
 \sum_{\substack{a,b\le X\\XL^{1-\delta}\le ab\le XL^{1+\delta}}}
 \frac{\Lambda(a)^2\Lambda(b)^2}{ab}
 \ll_\delta L^3\log L.
\tag{22}
\]

#### 证明

对整数 \(j\ge0\)，由 Chebyshev bound 与 partial summation，

\[
 U_j
 :=
 \sum_{e^j<n\le e^{j+1}}\frac{\Lambda(n)^2}{n}
 \ll 1+j.
\tag{23}
\]

条件 (21) 把 \(j+k\) 限制在中心为
\(L+\log L\)、宽度 \(O_\delta(\log L)\) 的整数区间。固定
\(z=j+k\asymp L\) 时，

\[
 \sum_{j+k=z}(1+j)(1+k)\ll z^3\ll L^3.
\tag{24}
\]

可取的 \(z\) 只有 \(O_\delta(\log L)\) 个。求和即得式 (22)。
\(\square\)

### 定理 216-D（transition atomic diagonal is negligible）[T]

式 (5) 成立。

#### 证明

对 singleton bulk atom，

\[
 F_{a/b}^{bulk}
 =
 \beta_L^2e^{iTs}T_{d_G}(Q_{a/b})D_{d_G}(s).
\]

Parseval、\(0\le P_{a/b}\le1\) 给

\[
 \|T_{d_G}(Q_{a/b})\|_{HS}^2
 \le d_G\sum_r|\widehat Q_{a/b}(r)|^2
 \le d_G|b_ab_b|^2.
\tag{25}
\]

因此式 (22)、\(\beta_L^4d_G\asymp X/L^3\) 给

\[
 \sum_{(a,b)\in\mathcal T_\delta}
 \|F_{a/b}^{bulk}\|_{HS}^2
 \ll
 \frac{X}{L^3}\,L^3\log L
 =
 X\log L
 =
 N\frac{\log L}{L}.
\]

\(\square\)

由笔记 209-D，同一 transition subset 的 finite/bulk atomic diagonal sums
相差 \(o(N)\)，所以 finite diagonal 也为 \(o(N)\)。

### 推论 216-E（constant frame bound suffices）[T]

若存在与 \(X\) 无关的 \(C_\delta\)，使

\[
 \left\|
 \sum_{(a,b)\in\mathcal T_\delta}F_{a/b}^{fin}
 \right\|_{HS}^2
 \le
 C_\delta
 \sum_{(a,b)\in\mathcal T_\delta}
 \|F_{a/b}^{fin}\|_{HS}^2+o(N),
\tag{26}
\]

则整个 transition layer 为 \(o(N)\)。

#### 证明

定理 216-D 与 atomic finite/bulk transfer 使式 (26) 的右端为
\(o(N)\)。\(\square\)

这把目标从“所有 cross terms 绝对可和”严格降低为一个 response-specific
constant frame inequality。

## 5. Evans published-input coverage audit

记 \(Y\asymp XL\)，所以 \(\log Y\asymp L\)。

### 外部定理 216-F（Evans Theorem 1.1）[R]

对 restricted set

\[
 E_2'(P)
 =
 \{n=p_1p_2:\ p_1\in(P,P^{1+\delta_0}]\},
\tag{27}
\]

Evans 对 almost all \(|r|\le H\) 证明 Hardy--Littlewood asymptotic，
其中

\[
 H\ge(\log Y)^{19+\varepsilon}.
\tag{28}
\]

关键是 \(P\) 不是任意 factor bin，而由 \(H\) 指定为

\[
 P=
 \begin{cases}
 (\log Y)^{17+\varepsilon},
 &H\le\exp((\log Y)^{\varepsilon^3}),\\
 \exp((\log\log Y)^2),
 &H>\exp((\log Y)^{\varepsilon^3}).
 \end{cases}
\tag{29}
\]

exceptional shifts 的数量为 \(O(H(\log Y)^{-\eta})\)，其中
\(\eta=\eta(\varepsilon)>0\)。

### 外部定理 216-G（Evans Theorem 1.3）[R]

对 general \(E_2\)，almost-all shift asymptotic 的范围为

\[
 H\ge\exp((\log Y)^{1-\varepsilon})
\tag{30}
\]

且 exceptional set 可取 \(O(H(\log Y)^{-B})\)。

来源：Natalie Evans, *Correlations of almost primes*,
Math. Proc. Cambridge Philos. Soc. 174 (2023), 301--344,
Theorems 1.1 and 1.3：
<https://doi.org/10.1017/S0305004122000251>。

### 障碍定理 216-H（balanced polylog cell is uncovered）[N]

固定 \(A>0\) 与 \(0<\sigma<1/2\)。考虑 balanced semiprime cell

\[
 \mathcal B_\sigma(Y)
 =
 \{n=pq\asymp Y:\ Y^\sigma\le p,q\le Y^{1-\sigma}\}
\tag{31}
\]

以及 polylog shift range

\[
 1\le H\le(\log Y)^A.
\tag{32}
\]

对充分大 \(Y\)，Evans Theorem 1.1 与 1.3 均不对
\(\mathbf1_{\mathcal B_\sigma}\) 的 correlations 给出结论。

#### 证明

Theorem 1.3 的 lower threshold
\(\exp((\log Y)^{1-\varepsilon})\) 大于每个 fixed power
\((\log Y)^A\)，所以不覆盖式 (32)。

Theorem 1.1 的两个 \(P\) choices 都满足

\[
 P^{1+\delta_0}=Y^{o(1)}<Y^\sigma
\]

对充分大 \(Y\) 成立。因此 balanced cell (31) 与
\(E_2'(P)\) 不交；Theorem 1.1 对它的 indicator correlation 没有信息。
\(\square\)

该障碍只审计这两条 published inputs 的逻辑适用范围；它不声称不存在其他
方法，也不把“文献尚未覆盖”升级为 arithmetic lower bound。

## 6. Exact finite experiment [E]

脚本 scripts/transition_ratio_kernel_audit.py 使用：

1. 实际 prime-power atoms 与 coefficients；
2. \(T=2\pi X\)、\(d_G\approx XL\) 的 exact Gabor lattice；
3. flat compact window 的 exact interval overlap；
4. transition band
   \(XL^{0.75}\le ab\le XL^{1.25}\)；
5. ordinary ratio radius \(0.35\)；
6. determinant bins
   \(|r|\le L\)、\(L<|r|\le4L\)、\(4L<|r|\le16L\)、\(|r|>16L\)。

输出为：

| \(X\) | atoms | signed/diagonal | absolute/diagonal |
|---:|---:|---:|---:|
| 300 | 720 | -0.0553 | 0.4383 |
| 600 | 1510 | -0.0388 | 0.4934 |
| 1200 | 3242 | -0.0412 | 0.5343 |

在 \(X=1200\) 时，signed contribution 的分层为：

| determinant bin | signed/diagonal | absolute/diagonal |
|---|---:|---:|
| \(|r|\le L\) | -0.0369 | 0.1140 |
| \(L<|r|\le4L\) | -0.00608 | 0.0805 |
| \(4L<|r|\le16L\) | +0.00318 | 0.0969 |
| \(|r|>16L\) | -0.00144 | 0.2429 |

这些有限数据只说明：

- 取绝对值确实损失显著；
- signed tail 有强抵消；
- resolution core 在这些尺度上主导 signed remainder；
- 一个 constant frame bound 与数据相容。

它们不证明 asymptotic frame inequality，也不证明 signed ratio 稳定在
\(-4\%\)。

## 7. Transition frame reduction

把 transition cells 按 product excess 与 ratio 分解为
\(\mathcal C_{r,\nu}\)。对一对 ordinary cells，定义 exact scalar kernel
\(\mathcal R_{\mathcal C,\mathcal C'}(h;k)\) 如式 (12)。

### 条件性桥梁 216-I（core-tail frame criterion）[C]

令 \(\mathfrak C_{tr}\) 为全部 transition product/ratio cells，
\(\mathcal E_{ord}\) 为其中包含 self-loops 的 ordinary cell-pair graph。若 core kernels
存在一个全图 Schur charge assignment：

\[
 \sum_{\mathcal C':(\mathcal C,\mathcal C')\in\mathcal E_{ord}}
 q_{\mathcal C\mathcal C'}
 \le C_0D_{\mathcal C},
 \qquad
 |K_{\mathcal C\mathcal C'}^{core}|
 \le q_{\mathcal C\mathcal C'}+q_{\mathcal C'\mathcal C},
\tag{33}
\]

其中 \(C_0\) 与 \(X\) 无关，并且全部 cell pairs 的 tail 满足全局预算

\[
 \beta_L^4
 \sum_{(\mathcal C,\mathcal C')\in\mathcal E_{ord}}
 \sum_k
 \left|
 \sum_{|h|>C H_{\rm res}}
 \mathcal R_{\mathcal C,\mathcal C'}(h;k)
 \right|
 =o(N),
\tag{34}
\]

则式 (26) 成立。这里

\[
 K_{\mathcal C\mathcal C'}^{core}
 =\beta_L^4\sum_k
 \sum_{0<|h|\le C H_{\rm res}}
 \mathcal R_{\mathcal C,\mathcal C'}(h;k).
\tag{34a}
\]

这里 \(D_{\mathcal C}\) 是该 cell 的 atomic diagonal mass。式 (33) 已经是
全 graph statement，不能用逐 edge 的 \(o(N)\) 代替；否则笔记 212-G 的
PSD path 反例仍适用。式 (34) 也明确包含二维 product/ratio cell count，
没有遗漏 \(O(\log L)\) 个 product layers。

#### 证明

式 (11)--(13) 把每个 ordinary cell pair 的 main term 分成 core 与 tail。
对式 (33) 的 oriented charges 求和，把全部 core contribution 控制在
\(2C_0\sum_{\mathcal C}D_{\mathcal C}\) 内；式 (34) 直接控制全局 tail。
far apertures、aliases 与 Hankel trace remainders 的 moving-cutoff proofs
只用引理 215-D 的 mass bound。这里 \(Z=XL^{1+\delta}\)，故其显式预算分别为

\[
 O\!\left(\frac{Z\log L}{L^2}\right),
 \qquad
 O\!\left(\frac{Z(1+\log L)}{L^3}\right),
\]

均为 \(o(N)\)。aggregate finite defect 仍满足
\(\|E\|_{HS}^2\ll Z(1+\log L)/L^2=o(N)\)。这些估计不使用
\(\kappa<1\) 的 ordinary theorem；不能笼统引用整个 215-I。

因此 bulk aggregate norm square 被 transition atomic diagonal 的固定倍数加
\(o(N)\) 控制，finite defect 再把该结论传到真实 finite aggregate。最后用
推论 216-E 得结论。\(\square\)

条件性桥梁 216-I 不是完成证明：式 (33)--(34) 正是尚缺的 arithmetic
core-tail estimates。但它把缺口从整个 matrix Gram 缩成了两个 scalar、
response-specific、可分别证伪的命题。

## 8. 修正后的下一最小引理 216-J [O]

先只处理 balanced transition core：

\[
 a,b,c,d\in
 [Y^{1/4},Y^{3/4}],
\qquad
 |ad-bc|\le C\,Y/X,
\qquad Y\asymp XL.
\tag{35}
\]

证明一个 weighted incidence/frame bound

\[
 \boxed{
 \text{core Gram}
 \preceq
 C\,\text{atomic transition diagonal}}
\tag{36}
\]

其中 \(C\) 与 \(X\) 无关，并给出全 determinant graph 的 Schur charge
assignment。若式 (36) 失败，则构造实际 prime-power lower-bound family，
而不是任意 Hilbert vectors。

晋级后再处理 oscillatory tail；在 core 未闭合前，不继续把 Evans 1.1
外推到它不覆盖的 factor bins。

## 9. 公理作用、删除审计与循环性

1. **Toeplitz modulation covariance**：负责 exact scalarization (11)。
2. **critical Gabor density**：把 resolution threshold 定为 \(Y/X\)。
3. **product/ratio cells**：保留 restricted factorization；删除后只剩过粗的
   \((\Lambda*\Lambda)(m)(\Lambda*\Lambda)(n)\) majorant。
4. **local Mertens budget**：给 transition diagonal 的
   \(N\log L/L\) saving。
5. **Evans Theorems 1.1/1.3**：只用于 scope audit；本轮没有把其结论外推到
   balanced polylog cells。
6. **constant frame criterion**：它是 [O] arithmetic input，不是 Weil
   positivity、unitarity 或 bounded negative index。

删除审计：

- 只知道 transition diagonal 为 \(o(N)\) 不能推出 aggregate 为 \(o(N)\)；
  coherent vectors 可把小 diagonal mass 放大。
- 只知道每条 core edge 是 \(o(N)\) 仍不能求和；必须有全 graph assignment。
- 只使用 unweighted \(E_2\) indicator correlations 不决定式 (12) 的
  factor-restricted log weights。
- 把 finite experiment 的约 \(-4\%\) 升级为 asymptotic constant 会违反
  [E]/[T] 边界。

循环性审计：式 (11)--(36) 全在 prime side，不引用 RH、GRH、零点比例、
Weil 完全正性或谱酉性。条件性桥梁 216-I 的输入比完整四矩严格局部：只涉及
transition factor cells 的 determinant core/tail。

## 10. 模型范围与部分 Weil 接口

- **Riemann zeta**：所有 [T]/[E] statements 直接适用于当前 response。
- **Dirichlet \(L\)**：absolute geometry 保留；core phase 要加入角色权。
- **Dedekind/automorphic \(L\)**：transition diagonal 需要相应 local
  Rankin--Selberg shell budget，determinant kernel 变为 coefficient
  convolution。
- **函数域**：\(H_{\rm res}\) 变成 degree-resolution threshold，balanced
  factor cells 可能由有限域大筛直接闭合。
- **负向 spectral models**：没有 Euler factorization 时式 (12) 不存在，
  再次说明该结构不是函数方程的同义反复。

在部分 Weil 配置中，定理 216-D 提供一个新的 prime-side small diagonal
budget；障碍定理 216-H 明确说明缺失的是 balanced short-shift arithmetic，
而不是抽象 compactness 或隐藏的 full positivity。
## 11. 后续更新（笔记 217）

笔记 217 使用 erratum-corrected discriminant-uniform multiplicative
upper-bound sieve，已无条件证明 fixed `0<delta<1` 的整个 transition
resolution core absolute contribution 为

\[
 O_\delta\!\left(NL^{-(1-\delta)/2}(\log L)^5\right)=o(N).
\]

因此本笔记 216-J 的 uniform constant frame/Schur assignment 不再是必要的
下一引理；它只是一个过强的充分条件。实际 prime-power core 已出现 affine
five-clique，进一步说明 maximum-degree 路线不自然。修正后的唯一 A2 输入是
保留 centered phase 与 sinc 的 oscillatory tail estimate。
