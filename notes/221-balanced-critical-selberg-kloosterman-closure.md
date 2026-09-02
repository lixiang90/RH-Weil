# 221. Balanced critical determinant box 的 Selberg--Kloosterman 闭合

日期：2026-09-02

分支：MOM-1 / 路线 A2，接口 NCE-8 / fixed-determinant response

状态：二维 Selberg 上界筛的 remainder form 与 Bettin--Chandee Corollary 1 为
[R]；精确局部密度、level ledger、singular-factor 平均、proper-power 删除以及单个
balanced critical box 的 natural-scale incidence bound 为 [T]。本笔记不更新 PDF。

## 1. 结论与范围

笔记 220 把 critical local Gram 的下一输入压成四因子 determinant incidence。
这里证明它的第一个非平凡情形。令 `L=log X`、`N=XL`，并取

\[
 A\asymp B\asymp C\asymp D\asymp Y,
 \qquad Y=\sqrt X\,L,
 \qquad H=L^2,
 \qquad R=Y^2=XL^2.
\tag{1}
\]

窗端点可取 sharp dyadic intervals；证明时用有限个非负 smooth majorants。定义

\[
 \mathfrak D_Y(H)=
 \sum_{\substack{a,b,c,d\asymp Y\\
                  \operatorname{base}(a)\ne\operatorname{base}(b)\\
                  \operatorname{base}(c)\ne\operatorname{base}(d)\\
                  0<|ad-bc|\le H}}
 \Lambda(a)\Lambda(b)\Lambda(c)\Lambda(d).
\tag{2}
\]

### 定理 221-A（balanced critical natural-scale incidence）[T]

当 `X -> infinity` 时，一致地有

\[
 \boxed{\mathfrak D_Y(H)\ll Y^2H=RH.}
\tag{3}
\]

常数只依赖固定的 dyadic/smooth partition。证明不使用 RH、GRH、素数对渐近、
Bombieri--Vinogradov 或零密度定理。

### 推论 221-B（单个 balanced critical local Gram 闭合）[T]

式 (3) 是笔记 220-(8) 的 `sigma=0` 情形。因此单个 balanced critical factor-box
pair 的 scaled local energy 至多

\[
 \frac{\beta_L^4d_G}{R}\mathfrak D_Y(H)
 \ll \beta_L^4d_GH
 \asymp \frac{X}{L}
 =\frac{N}{L^2}=o(N).
\tag{4}
\]

本笔记只声明固定 balanced aspect-ratio sector。它没有证明所有 unbalanced ratio
layers 的统一 bound，故尚不调用笔记 220-B 宣称整个 critical shell 已闭合。

## 2. 外部输入的精确版本

### 输入 221-R1（Bettin--Chandee fixed-determinant formula）[R]

对 `Delta != 0`，Bettin--Chandee Corollary 1 给

\[
 \begin{aligned}
 \mathcal T={}&
 \sum_{(n_1,n_2)\mid\Delta}
 \frac{(n_1,n_2)}{n_1n_2}\alpha_{n_1}\beta_{n_2}
 \int_{\mathbb R}
 f\!\left(\frac{x+\Delta}{n_2}\right)
 g\!\left(\frac{x}{n_1}\right)\,dx
 +O(\mathcal E),
 \end{aligned}
\tag{5}
\]

其中 `f,g` 是 derivative-controlled smooth dyadic weights，`alpha,beta` 可任意，且

\[
 \mathcal E\ll
 (\eta\mathcal R)^{3/2}\|\alpha\|_2\|\beta\|_2
 (N_1N_2)^{7/20}(N_1+N_2)^{1/4+\varepsilon}
 (M_1M_2)^\varepsilon.
\tag{6}
\]

这里 `mathcal R=M_1N_2/(M_2N_1)+M_2N_1/(M_1N_2)`。

来源：S. Bettin, V. Chandee, *Trilinear Forms with Kloosterman Fractions*,
Adv. Math. 328 (2018), Corollary 1，<https://arxiv.org/abs/1502.00769>。

### 输入 221-R2（Selberg upper-bound sieve, remainder form）[R]

设非负有限序列按 `n` 编号，并有

\[
 A_q=g(q)X+r_q
\tag{7}
\]

对 squarefree `q|P(z)` 成立，`g` 乘法且是固定维数的 sieve density。标准 Selberg
上界筛给：取仅依赖筛维数的充分大 fixed `s`、`D=z^s` 时，可取
`lambda_1=1`、支撑在 `d<=D` 的 Selberg
权，使

\[
 \mathbf 1_{(n,P(z))=1}
 \le
 \left(\sum_{d\mid(n,P(z))}\lambda_d\right)^2,
\tag{8}
\]

而主二次型为 `O_s(XV(z))`，其中

\[
 V(z)=\prod_{p<z}(1-g(p)).
\tag{9}
\]

展开式 (8) 后，remainder 只涉及 `[d_1,d_2]<=D^2`，其系数至多有固定 divisor
power 的增长。本笔记只用这个 upper-bound/remainder 形式，不用 parity-breaking
lower sieve。

可核对来源：G. Tenenbaum, *Introduction to Analytic and Probabilistic Number Theory*,
3rd ed., AMS GSM 163, Chapter I.4（Selberg sieve）；官方章节预览：
<https://www.ams.org/bookstore/pspdf/gsm-163-prev.pdf>。

## 3. 先删除 proper prime powers

### 引理 221-C（proper-power contribution）[T]

式 (2) 中至少一个变量是 `p^k, k>=2` 的贡献为

\[
 O\!\left(Y^{3/2}HL^3\right)=o(Y^2H).
\tag{10}
\]

#### 证明

在固定 dyadic interval 中，elementary 地

\[
 \sum_{\substack{n\asymp Y\\n=p^k,\ k\ge2}}\Lambda(n)
 \ll \sqrt Y\,L.
\tag{11}
\]

若例如 `a` 是 proper power，固定 `a,b,h` 后，方程 `ad-bc=h` 在 balanced boxes
中给 `O(1)` 个 admissible `d`；对其余 target weights 用 `Lambda(c)Lambda(d)<=L^2`，
并用 `sum_(b asymp Y)Lambda(b)<<Y`。对 `0<|h|<=H` 求和即得
`O(Y^(3/2)HL^3)`。其余三个位置由交换变量相同。除以 `Y^2H` 后为
`O(Y^(-1/2)L^3)=o(1)`。`square`

所以以下可把四个变量都限制为区间中的素数。特别地它们最终全为奇数；奇 `h`
没有贡献。固定 `h!=0` 且 `|h|<=H=o(Y)` 时还必有 `b!=d`，否则
`h=b(a-c)` 的非零绝对值至少为 `b asymp Y`。

## 4. 两坐标 divisibility data 的精确主项

取固定非负 `w in C_c^infty((1/2,2))` 覆盖一个 sharp box。对 squarefree
`q_1,q_2`（所有素因子小于稍后选择的 `z=o(Y)`）定义

\[
 \begin{aligned}
 A_{q_1,q_2}(h)={}&
 \sum_{\substack{ad-bc=h\\q_1\mid a,\ q_2\mid c}}
 w(a/Y)w(c/Y)\Lambda(b)\Lambda(d)
 \mathbf 1_{b,d\ \mathrm{prime}} .
 \end{aligned}
\tag{12}
\]

这里 `a,c` 尚未带 Lambda；它们是即将被筛的两个 smooth coordinates。

### 引理 221-D（exact two-coordinate density）[T]

若 `q_1,q_2<=Y^(1/10)`，则

\[
 A_{q_1,q_2}(h)
 =g_h(q_1,q_2)X_h+r_{q_1,q_2}(h),
\tag{13}
\]

其中

\[
 g_h(q_1,q_2)=
 \mathbf 1_{(q_1,q_2)\mid h}\frac{(q_1,q_2)}{q_1q_2},
\tag{14}
\]

\[
 X_h=
 \sum_{b,d\asymp Y}
 \frac{\Lambda(b)\Lambda(d)\mathbf 1_{b,d\ \mathrm{prime}}}{bd}
 \int_{\mathbb R}
 w\!\left(\frac{x+h}{dY}\right)
 w\!\left(\frac{x}{bY}\right)\,dx,
 \qquad X_h\ll Y^2,
\tag{15}
\]

并且

\[
 r_{q_1,q_2}(h)
 \ll_\varepsilon
 Y^{39/20+\varepsilon}L
 (q_1q_2)^{7/20}(q_1+q_2)^{1/4+\varepsilon}.
\tag{16}
\]

#### 证明

写

\[
 a=q_1m_1,\qquad c=q_2m_2,
 \qquad n_2=q_1d,\qquad n_1=q_2b.
\tag{17}
\]

则 determinant equation 成为

\[
 m_1n_2-m_2n_1=h.
\tag{18}
\]

在式 (5) 中取

\[
 f(m_1)=w(q_1m_1/Y),\qquad
 g(m_2)=w(q_2m_2/Y).
\tag{19}
\]

它们的 derivative parameter `eta` 有绝对界。因为 `b,d asymp Y` 是不同素数，
而 `q_1,q_2` 只含小于 `z=o(Y)` 的素因子，故

\[
 (n_1,n_2)=(q_2b,q_1d)=(q_1,q_2).
\tag{20}
\]

更重要的是，式 (5) 的两个 smooth arguments 精确化为

\[
 f\!\left(\frac{x+h}{n_2}\right)
 =w\!\left(\frac{x+h}{dY}\right),\qquad
 g\!\left(\frac{x}{n_1}\right)
 =w\!\left(\frac{x}{bY}\right).
\tag{21}
\]

所以主积分完全不依赖 `q_1,q_2`；prefactor 恰给式 (14)，不是近似 density。

再者

\[
 M_1\asymp Y/q_1,\quad M_2\asymp Y/q_2,
 \quad N_1\asymp q_2Y,\quad N_2\asymp q_1Y,
 \quad \mathcal R\asymp1.
\tag{22}
\]

Chebyshev bound 给

\[
 \|\alpha\|_2\|\beta\|_2
 \ll YL.
\tag{23}
\]

把式 (22)--(23) 代入式 (6) 即得式 (16)。式 (15) 中积分长度为 `O(Y^2)`，
除以 `bd asymp Y^2` 后为 `O(1)`；再用两个 Chebyshev sums 得 `X_h<<Y^2`。
`square`

## 5. 局部筛密度与 singular factor

对奇素数 `p`，式 (14) 给

\[
 g_h(p,1)=g_h(1,p)=\frac1p,
 \qquad
 g_h(p,p)=\frac{\mathbf 1_{p\mid h}}p.
\tag{24}
\]

所以排除 `p|a` 或 `p|c` 后的 local survival factor 是

\[
 v_h(p)=1-\frac2p+\frac{\mathbf 1_{p\mid h}}p
 =
 \begin{cases}
 1-2/p,&p\nmid h,\\
 1-1/p,&p\mid h.
 \end{cases}
\tag{25}
\]

定义

\[
 \mathfrak S_2(h)=
 \prod_{\substack{p\mid h\\p>2}}
 \frac{1-1/p}{1-2/p}
 =\prod_{\substack{p\mid h\\p>2}}
 \left(1+\frac1{p-2}\right).
\tag{26}
\]

Mertens product estimate 因而给

\[
 \prod_{2<p<z}v_h(p)
 \ll \frac{\mathfrak S_2(h)}{(\log z)^2}.
\tag{27}
\]

### 引理 221-E（singular factor 的一阶平均）[T]

\[
 \sum_{1\le |h|\le H}\mathfrak S_2(h)\ll H.
\tag{28}
\]

#### 证明

展开正乘积得

\[
 \mathfrak S_2(h)=
 \sum_{\substack{d\mid h\\d\ \mathrm{odd\ squarefree}}}
 \prod_{p\mid d}\frac1{p-2}.
\tag{29}
\]

交换求和后，式 (28) 的正半轴至多

\[
 H\sum_{\substack{d\ge1\\d\ \mathrm{odd\ squarefree}}}
 \frac1d\prod_{p\mid d}\frac1{p-2}
 =H\prod_{p>2}\left(1+\frac1{p(p-2)}\right)\ll H.
\tag{30}
\]

负半轴相同。`square`

## 6. Selberg remainder ledger

记 `P(z)=prod_(2<p<z)p`。取固定

\[
 0<\kappa<\frac1{78},\qquad D=Y^\kappa,
 \qquad z=D^{1/s}
\tag{31}
\]

其中 `s` 是输入 221-R2 中充分大的 fixed sieve parameter。于是
`log z asymp log Y asymp L`。

把式 (8) 用于 `n=ac`。对 squarefree `q`，条件 `q|ac` 的主 density 是
式 (24) 的 inclusion--exclusion product

\[
 g_h(q)=\prod_{p\mid q}
 \left(\frac2p-\frac{\mathbf 1_{p\mid h}}p\right),
\tag{32}
\]

故它确为乘法 sieve density。展开 `[d_1,d_2]=q` 后，条件 `q|ac` 对每个
`p|q` 可分成 `p|a`、`p|c`、或二者同时成立三种 signed choices。因此它是至多
`3^omega(q)` 个式 (12) 的组合，且所有出现的

\[
 q_1,q_2\le q\le D^2.
\tag{33}
\]

标准 Selberg weights 的 fixed-divisor-power bound 与 `3^omega(q)<<_epsilon
q^epsilon` 给总 remainder

\[
 \begin{aligned}
 \mathcal R_h
 &\ll_\varepsilon
 D^{2+\varepsilon}
 \max_{q_1,q_2\le D^2}|r_{q_1,q_2}(h)|\\
 &\ll_\varepsilon
 Y^{39/20+\varepsilon}L D^{39/10+\varepsilon}.
 \end{aligned}
\tag{34}
\]

这里 `D^2` 来自 ordered pair `(d_1,d_2)`；式 (16) 在
`q_1,q_2<=D^2` 上再损失

\[
 (q_1q_2)^{7/20}(q_1+q_2)^{1/4+\varepsilon}
 \ll D^{19/10+\varepsilon},
\tag{35}
\]

合计即 `D^(39/10+epsilon)`。先固定 `kappa<1/78`，再在 Bettin--Chandee bound 中选择充分小的 `epsilon>0`；无 `epsilon` 的核心指数满足

\[
 -\frac1{20}+\frac{39}{10}\kappa<0.
\tag{36}
\]

### 引理 221-F（two-prime sifted count）[T]

对每个非零 `|h|<=H`，

\[
 \sum_{\substack{ad-bc=h\\a,c\ \mathrm{prime}}}
 w(a/Y)w(c/Y)\Lambda(b)\Lambda(d)
 \mathbf 1_{b,d\ \mathrm{prime}}
 \ll
 \frac{Y^2}{L^2}\mathfrak S_2(h)
 +Y^{39/20+\varepsilon}L D^{39/10+\varepsilon}.
\tag{37}
\]

#### 证明

区间中的 primes `a,c` 不被任何 `p<z` 整除，所以左边不超过相应
`(ac,P(z))=1` 的 sifted count。对式 (13) 应用输入 221-R2。主项由
`X_h<<Y^2`、式 (27) 与 `log z asymp L` 给第一项；remainder 由式 (34) 给第二项。
`square`

## 7. 定理 221-A 的证明

在四个变量均为素数时，

\[
 \Lambda(a)\Lambda(c)\ll L^2.
\tag{38}
\]

用式 (38) 乘式 (37)，再对 `1<=|h|<=H` 求和。由引理 221-E，主项为

\[
 L^2\frac{Y^2}{L^2}
 \sum_{1\le|h|\le H}\mathfrak S_2(h)
 \ll Y^2H.
\tag{39}
\]

误差为

\[
 \begin{aligned}
 &L^2H\,Y^{39/20+\varepsilon}L D^{39/10+\varepsilon}\\
 &\qquad=
 Y^2H\cdot
 Y^{-1/20+\varepsilon}L^3D^{39/10+\varepsilon}
 =o(Y^2H)
 \end{aligned}
\tag{40}

\]

由式 (36) 及 `L^3=Y^{o(1)}`。加回引理 221-C 的 proper-power contribution，
得到式 (3)。`square`

## 8. 删除审计与非循环性

1. **Bettin--Chandee power saving**：式 (40) 使用其 `Y^(39/20)`，即相对
   `Y^2` 的 `Y^(-1/20)`。删除后 Selberg remainder 可能与主项同阶，证明中断于
   式 (36)。
2. **两个 smooth coordinates**：它们允许把 primality 改成 roughness 并用
   `L^2/(log z)^2` 抵消。只筛一个坐标只省一个对数，会回到笔记 220 的
   `sigma=1` endpoint。
3. **精确 gcd 主项**：式 (21) 保证 divisibility level 不扭曲 physical windows。
   若主项只知一个无结构 upper bound，就没有乘法 density `v_h(p)`，Selberg
   主二次型不能产生两个对数。
4. **fixed small level**：`kappa<1/78` 不是优化常数，而是保守地支付完整
   Selberg quadratic expansion。令 `kappa` 过大只破坏当前 remainder ledger，
   不构成 incidence bound 失败的反例。
5. **shift average**：逐 `h` 的 singular factor 可大于常数；式 (28) 是对
   `|h|<=H` 求和时不可删除的输入。
6. **balanced geometry**：使四个 scales 都是 `Y` 且 `mathcal R asymp1`。
   unbalanced boxes 需要重新计算式 (16)、(34)，本笔记没有默认为一致。

循环性审计：唯一非初等输入是公开的 fixed-determinant Kloosterman bound 与标准
Selberg upper-bound sieve。两者均是纯 prime-side finite estimates，不预设零点在
中心线。筛法只给 upper bound，不越过 parity barrier，也不声称四素数渐近。

模型范围：

- Riemann zeta：式 (2) 正是 alternating/Farey positive majorant 的 balanced
  determinant box，定理直接适用。
- 固定本原 Dirichlet `L`：unit character phases 在 absolute positive majorant 中
  消失，同一 incidence upper bound 适用；这不等于已闭合该函数的全部四矩误差。
- Dedekind 与一般 automorphic `L`：若局部系数不能由有限个单位相位 Lambda 型
  分量 pointwise 控制，则式 (37) 没有现成替代，定理不自动推广。
- 函数域：需要 polynomial determinant 与相应二维上界筛；本整数 Kloosterman
  输入不直接适用。
- 无 Euler factorization 的谱 zeta 模型：没有四因子 incidence，因此不在范围内。

## 9. 对笔记 220-D 的修正与下一最小引理

笔记 220-D 的 direct-substitution no-go 仍正确：不能把两个 smooth slots 直接放入
Lambda。但它遗漏了一个可行的间接接口：保留这两个 slots 为 smooth divisibility
weights，用 Selberg sieve 把 prime conditions 外置。Bettin--Chandee 的精确主项
随后给足够的 level of distribution；因此 balanced box 不需要 Vaughan decomposition。

下一最小引理 221-G [O]：令

\[
 A/B\asymp C/D,\qquad AB,CD\asymp XL^2,
\tag{41}
\]

但允许 `A/B` 穿过完整 `O(L)` ratio range。对每个 aspect layer 选择较短的两个
smooth sieve coordinates，重新计算 Bettin--Chandee error，并证明某个统一
`kappa>0` 仍满足 Selberg level ledger；或者严格识别首先失效的 aspect threshold。
只有得到对全部 relevant factor boxes 一致的 `sigma<1`，才能由笔记 220-B 宣称
整个 critical shell closure。
## 10. 后续更新（笔记 222）

笔记 222 已完成本笔记 221-G：以 `V>=U^delta` / `V<U^delta` 分区，前者继续使用
Bettin--Chandee 外筛，后者把 determinant fiber 参数化为两条长 affine prime forms
并直接 Selberg 筛。短 factors 的 `g=(b,d)` 使参数长度乘 `g`、可用 shifts 数除
`g`，二者精确抵消，因此 same-base short prime powers也被统一保留。所得 bound 对全部
critical factor boxes 为 `D(H)<<RH(log L)^C`，由笔记 220-B 闭合完整 critical shell。
