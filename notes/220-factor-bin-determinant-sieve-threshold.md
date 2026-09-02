# 220. Critical factor-bin determinant sieve 的精确对数阈值

日期：2026-09-02

分支：MOM-1 / 路线 A2，辅助接口 NCE-8 / Vaughan--Kloosterman response

状态：四变量 factor-bin determinant incidence 的 `L^2` elementary baseline、
`sigma<1` closure theorem 与 `sigma=1` bookkeeping ceiling 为 [T]；
Bettin--Chandee fixed-determinant corollary 的直接适用缺口为 [N]；超过一个对数的
joint target-prime saving 在本笔记中为 [O]；后续笔记 221 已用间接二维 Selberg 接口闭合 balanced case，完整 unbalanced range 仍为 [O]。本笔记不更新 PDF。

## 1. 本轮结论

笔记 219 证明 scalar mass/second-moment/shift budgets 即使达到 natural size，也
不能闭合 critical shell。这里把“必须保留 factorization”进一步变成一个有明确
指数阈值的算术命题。

考虑 source 与 target dyadic boxes

\[
 a\asymp A,\quad b\asymp B,
 \qquad
 c\asymp C,\quad d\asymp D,
\tag{1}
\]

并假设 ratio-compatible：

\[
 A/B\asymp C/D.
\tag{2}
\]

记

\[
 P=AB,\qquad Q=CD,
 \qquad
 R=AD\asymp BC\asymp\sqrt{PQ}.
\tag{3}
\]

在 critical product shell 中，

\[
 XL^{2-\rho}\le P,Q\le XL^2,
 \qquad 0<\rho<1
\tag{4}
\]

固定。resolution length 为

\[
 H_R\asymp R/X.
\tag{5}
\]

定义保留四个 factors 的 weighted determinant incidence

\[
 \begin{aligned}
 \mathfrak D_{A,B;C,D}(H)
 ={}&
 \sum_{\substack{a\asymp A,\ b\asymp B\\
                   c\asymp C,\ d\asymp D\\
                   \operatorname{base}(a)\ne\operatorname{base}(b)\\
                   \operatorname{base}(c)\ne\operatorname{base}(d)\\
                   0<|ad-bc|\le H}}
 \Lambda(a)\Lambda(b)\Lambda(c)\Lambda(d).
 \end{aligned}
\tag{6}
\]

prime powers 可保留在定义中；proper powers 的较小质量也可另行删除。

本轮证明：

1. elementary counting 只给
   \[
   \mathfrak D(H)\ll RH L^2;
   \tag{7}
   \]
2. 若对所有 relevant box pairs 有某个 fixed `sigma<1` 的
   \[
   \mathfrak D(H_R)\ll RH_RL^\sigma(\log L)^C,
   \tag{8}
   \]
   则整个 critical shell 的 local-box energy 为 `o(N)`；
3. `sigma=1` 在完整 box ledger 上只给 `N(log L)^(C+2)`，不能推出
   little-oh；
4. 因而相对于式 (7)，必须从两个 target prime-power conditions 中联合取得
   **严格超过一个整对数**的 saving。expected upper-bound sieve `sigma=0`
   留有一个完整 `L` 的余量。

这比“需要四素数相关”弱得多：不需要 asymptotic、singular series main term 或
fixed-shift lower bound；只需要一个 uniform upper bound，且允许 `L^(1-epsilon)`
的损失。

## 2. Integer volume 与 natural prime scale

先忽略 primality。固定 `a,b,d` 后，条件 `|ad-bc|<=H` 把 `c` 限制在长度
`O(H/B)` 的 interval。故 ratio-compatible boxes 中的 integer volume 是

\[
 \#\{(a,b,c,d):|ad-bc|\le H\}
 \asymp R H
\tag{9}
\]

的尺度，而不是 `PQH`。在 balanced case `A,B,C,D asymp sqrt R` 时，这也可由
`A B D times H/B=RH` 直接看出。

四个 prime conditions 的 density 预期为

\[
 \frac1{\log A\log B\log C\log D},
\tag{10}
\]

而四个 `Lambda` weights 恰好抵消这些 densities。因此 weighted natural scale
正是

\[
 \mathfrak D(H)\asymp RH
\tag{11}
\]

，即式 (8) 的 `sigma=0`。本节只把式 (11) 用作尺度解释，不把它声明为已证
asymptotic。

## 3. Elementary `sigma=2` baseline

### 定理 220-A（factor-preserving trivial incidence bound）[T]

在式 (1)--(5) 的 boxes 中，一致地有

\[
 \boxed{
 \mathfrak D_{A,B;C,D}(H)\ll RHL^2.}
\tag{12}
\]

#### 证明

先设 `D>=B`。固定 primitive source `(a,b)` 与非零 determinant `h`。由
`gcd(a,b)=1`，方程

\[
 ad-bc=h
\tag{13}
\]

使

\[
 d\equiv a^{-1}h\pmod b.
\tag{14}
\]

长度 `asymp D` 的 target interval 中，该 residue class 至多出现

\[
 O(1+D/B)
\tag{15}
\]

次；每个 `d` 唯一决定 `c=(ad-h)/b`。使用 pointwise bounds

\[
 \Lambda(c)\Lambda(d)\le L^2
\tag{16}
\]

与 elementary Chebyshev estimates

\[
 \sum_{a\asymp A}\Lambda(a)\ll A,
 \qquad
 \sum_{b\asymp B}\Lambda(b)\ll B,
\tag{17}
\]

再对 `0<|h|<=H` 求和，得到

\[
 \mathfrak D(H)
 \ll HAB(1+D/B)L^2
 \ll HADL^2
 \asymp RHL^2.
\tag{18}
\]

若 `D<B`，交换 source 与 target，并把 `h` 换成 `-h`。此时相同证明给

\[
 HCD(1+B/D)L^2\ll HCBL^2\asymp RHL^2.
\]

这证明式 (12)。`square`

该证明完整保留 determinant factorization，但完全没有平均 target weights；
式 (16) 正是损失两个对数的位置。

## 4. 从 factor-bin bound 到 critical closure

对 source atom `i=(a,b)` 与 target atom `j=(c,d)`，笔记 218 的 local positive
Gram coefficient 由

\[
 |b_ab_bb_cb_d|W_{ij}
 \ll
 \frac{\Lambda(a)\Lambda(b)\Lambda(c)\Lambda(d)}
      {\sqrt{PQ}}
 \asymp
 \frac{\Lambda(a)\Lambda(b)\Lambda(c)\Lambda(d)}R
\tag{19}
\]

控制。因而单个 factor-box pair 的 scaled local energy 至多

\[
 \frac{\beta_L^4d_G}{R}
 \mathfrak D_{A,B;C,D}(H_R).
\tag{20}
\]

### 定理 220-B（`sigma<1` factor-bin closure criterion）[T]

假设存在 fixed `sigma<1` 与 fixed `C>=0`，使式 (8) 对全部 critical
ratio-compatible dyadic box pairs一致成立。则笔记 218-(43) 的整个 critical
local-box energy 为 `o(N)`。因此该 shell 的 bulk 与 finite aggregates 均为
`o(N)`。

#### 证明

由

\[
 \beta_L^4d_G\asymp X/L^3,
 \qquad H_R\asymp R/X,
\tag{21}
\]

式 (8)、(20) 给每个 box pair

\[
 \frac{\beta_L^4d_G}{R}\mathfrak D(H_R)
 \ll
 \frac{X}{L^3}H_RL^\sigma(\log L)^C
 \ll
 \frac{R}{L^{3-\sigma}}(\log L)^C.
\tag{22}
\]

由 `R<=XL^2=N L`，这至多为

\[
 N L^{\sigma-2}(\log L)^C.
\tag{23}
\]

现在计数 relevant box pairs。用 fixed multiplicative-width factor boxes，product
coordinate 在式 (4) 中只有 `O(log L)` 层，ratio coordinate 有 `O(L)` 层。
同一 local frequency box 强迫两个 ratio layers 相同或相邻，但两个 product
layers 可独立选择。因此最多有

\[
 O\bigl(L(\log L)^2\bigr)
\tag{24}
\]

个 relevant ordered box pairs。将式 (23) 求和得到

\[
 O\left(
 N L^{\sigma-1}(\log L)^{C+2}
 \right)=o(N),
\tag{25}
\]

因为 `sigma<1` fixed。

式 (25) 控制笔记 218 的 positive local energy。clustered Fejér theorem 随后
控制完整 bulk main；Toeplitz--Hankel 与 finite/bulk errors 仍由笔记
218-(36)--(37) 控制。`square`

### 障碍定理 220-C（endpoint `sigma=1` does not close）[N]

只把定理 220-B 的假设改成 `sigma=1`，其 box ledger 至多给

\[
 O\left(N(\log L)^{C+2}\right),
\tag{26}
\]

不是 `o(N)`。更一般地，式 (8) 必须在 powers of `L` 意义下严格优于 `RH L`，
除非另有跨 product layers 的 cancellation 或 six-window summability。

#### 证明

把 `sigma=1` 代入式 (25) 即得。这里的结论是 implication ceiling，不是实际
prime incidence 的 lower bound。`square`

所以相对于 elementary `sigma=2`，仅平均掉一个 target `Lambda` 的 pointwise
logarithm仍停在 endpoint；必须联合使用两个 target conditions，取得超过一个
logarithm 的 saving。

## 5. Bettin--Chandee determinant theorem 的范围审计

Bettin--Chandee, *Trilinear forms with Kloosterman fractions*, Corollary 1，研究
固定非零 determinant

\[
 m_1n_2-m_2n_1=\Delta
\tag{27}
\]

上的四变量和；它允许 `n_1,n_2` 带 arbitrary coefficient sequences，但要求
`m_1,m_2` 的 weights 是具有 derivative control 的 smooth functions。该结果来自
其 trilinear Kloosterman-fraction bound，并改善 DFI 的 determinant error。

来源：Sandro Bettin, Vorrapan Chandee, *Trilinear Forms with Kloosterman
Fractions*, Advances in Mathematics 328 (2018), 1234--1262，Corollary 1：
<https://arxiv.org/abs/1502.00769>。

### 障碍定理 220-D（direct black-box substitution misses two prime weights）[N]

Bettin--Chandee Corollary 1 的正式假设不能直接以

\[
 f(m_1)=\Lambda(m_1),
 \qquad g(m_2)=\Lambda(m_2)
\tag{28}
\]

代入，因为 von Mangoldt weights 不满足其 smooth derivative hypotheses。若只用
`Lambda<=L` 把这两个 weights 替换成 smooth interval majorants，则支付 `L^2`，
恰好回到定理 220-A 的 `sigma=2` baseline，不能验证定理 220-B。

#### 证明

第一句是 Corollary 1 的 hypothesis check。第二句由两个 pointwise replacements
各损失一个 `L`，而其余 determinant lattice volume 为 `RH`；因此所得 factor
为 `RH L^2`。定理 220-C 随即排除由该 bound 自动闭合。`square`

这不说明 Bettin--Chandee 方法太弱。它说明真正需要的桥梁是：先对式 (28) 做
Vaughan/Heath--Brown decomposition，再把产生的 Type I/II pieces 放进其
Kloosterman framework，并证明所有 determinant shifts 与 box pairs 的总成本
仍满足某个 `sigma<1`。该工作尚未由黑箱定理完成。

## 6. 删除审计、循环性与模型范围

1. **primitive source**：在式 (14) 使用 `gcd(a,b)=1`。删除后 residue modulus
   降为 `b/gcd(a,b)` 并产生 gcd factor；同素数 chains 必须像笔记 209 那样分开。
2. **ratio compatibility**：给 `AD asymp BC` 与单一 scale `R`。删除后 integer
   volume和 coefficient normalization不能由同一参数表达。
3. **four separate Lambda factors**：式 (8) 的潜在 saving正来自它们；若先 collapse
   成两个 `Lambda*Lambda`，笔记 219 的 scalar no-go重新出现。
4. **product/ratio box ledger**：负责式 (24)。把每对 boxes 粗计为全部
   `O(L^2(log L)^2)` pairs 会多损失一个 `L`，错误地把阈值改成 `sigma<0`。
5. **clustered Fejér bridge**：只在式 (25) 后把 local mass提升到完整 sampled Gram；
   它不制造 determinant sieve saving。

循环性审计：定理 220-A--C 全部是 finite prime-side implications；不使用 RH、
GRH、zero density、Weil positivity、unitarity或 Hardy--Littlewood lower bound。
定理 220-D 只审计已发表 theorem hypotheses，不声称其方法无法经新分解达到目标。

模型范围：

- Riemann zeta 与 fixed primitive Dirichlet `L`：unit character phases 在 positive
  incidence majorant中消失；criterion不变。
- Dedekind/automorphic `L`：需要四个 coefficient factors 的 analogue；只知
  Rankin--Selberg second moment不能提供式 (8)。
- 函数域：固定 determinant 变成 polynomial determinant，degree sieve可能直接给
  `sigma=0` analogue。
- 无 Euler factorization 的 spectral models：式 (6) 不存在，因而本 criterion
  明确不是函数方程或 abstract positivity 的改写。

## 7. 下一最小引理 220-E [O]

只处理一个 balanced critical box

\[
 A\asymp B\asymp C\asymp D
 \asymp \sqrt{X}\,L,
 \qquad H\asymp L^2.
\tag{29}
\]

对两个 target von Mangoldt factors 作一次完整 Vaughan decomposition，并保持
source factors、determinant equation 与 physical box weight。证明各 Type I/II
piece合计满足

\[
 \boxed{
 \mathfrak D_{A,B;C,D}(H)
 \ll R H L^{1-\varepsilon_0}}
\tag{30}
\]

对某个 fixed `epsilon_0>0`，或证明当前 Bettin--Chandee exponent bookkeeping
不能达到 `sigma<1`。

晋级后再处理 unbalanced boxes 与 `O(L(log L)^2)` 总 ledger。若分解后仍只能得到
`RH L`，则由定理 220-C 立即止损，并转向 six-window summability或跨
adjacent/continuum/Gamma cancellation。

## 8. 后续更新（笔记 221）

笔记 221 证明式 (29)--(30) 的 balanced 目标，而且得到更强的 `sigma=0`：不把
Lambda 直接塞入 Bettin--Chandee 的 smooth slots，而是对这两个坐标作二维 Selberg
上界筛。对 `a=q_1m_1,c=q_2m_2`，Corollary 1 的主积分对 `q_1,q_2` 精确不变，
局部 density 为 `1_((q_1,q_2)|h)(q_1,q_2)/(q_1q_2)`；其 power-saving error 支撑
fixed positive sieve level。因此本笔记 220-D 的 direct-substitution no-go 仍成立，
但由它推测必须先作 Vaughan decomposition 已被修正。下一输入改为 unbalanced
aspect layers 的统一 level ledger。
