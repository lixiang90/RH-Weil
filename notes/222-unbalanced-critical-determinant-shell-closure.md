# 222. Unbalanced critical determinant shell 的双机制闭合

日期：2026-09-02

分支：MOM-1 / 路线 A2，接口 alternating/Farey ratio Gram

状态：moderate-aspect Bettin--Chandee 外筛、extreme-aspect 两线性形式直接筛、
同素数底短因子 gcd ledger、全 critical factor-box bound 及 critical-shell local Gram
闭合均为 [T]；所调用的 fixed-determinant formula 与 Selberg upper-bound sieve 为
[R]。本笔记不更新 PDF。

外部输入：S. Bettin--V. Chandee, *Trilinear Forms with Kloosterman
Fractions*, Corollary 1，<https://arxiv.org/abs/1502.00769>；G. Tenenbaum,
*Introduction to Analytic and Probabilistic Number Theory*, Chapter I.4，
<https://www.ams.org/bookstore/pspdf/gsm-163-prev.pdf>。

## 1. 主结果

沿用笔记 220 的记号。令 `L=log X`，固定 `0<rho<1`，考虑任意
ratio-compatible factor boxes

\[
 a\asymp A,\quad b\asymp B,
 \qquad c\asymp C,\quad d\asymp D,
\tag{1}
\]

满足

\[
 \frac AB\asymp\frac CD,
 \qquad
 XL^{2-\rho}\le AB,CD\le XL^2.
\tag{2}
\]

记

\[
 R=AD\asymp BC\asymp\sqrt{ABCD},
 \qquad H_R\asymp R/X.
\tag{3}
\]

weighted primitive determinant incidence 为

\[
 \mathfrak D_{A,B;C,D}(H)=
 \sum_{\substack{a,b,c,d\text{ in (1)}\\
                   \operatorname{base}(a)\ne\operatorname{base}(b)\\
                   \operatorname{base}(c)\ne\operatorname{base}(d)\\
                   0<|ad-bc|\le H}}
 \Lambda(a)\Lambda(b)\Lambda(c)\Lambda(d).
\tag{4}
\]

### 定理 222-A（uniform critical factor-box incidence）[T]

存在只依赖固定 boxes、`rho` 的常数 `C`，使式 (1)--(3) 的所有 relevant boxes
一致满足

\[
 \boxed{
 \mathfrak D_{A,B;C,D}(H_R)
 \ll_\rho RH_R(\log L)^C.}
\tag{5}
\]

换言之，式 (5) 是笔记 220-(8) 的 `sigma=0`，不是仅有 `sigma<1`。

### 推论 222-B（entire critical shell closure）[T]

笔记 218 的 critical local-box positive energy、bulk aggregate 与 finite aggregate
全部为 `o(N)`。更精确地，笔记 220-B 的 box ledger 给

\[
 O_\rho\!\left(
 N L^{-1}(\log L)^{C+2}
 \right)=o(N).
\tag{6}
\]

结合笔记 209--218，所有 primitive alternating/Farey ratio atoms 在完整 physical
product support `ab<=XL^2` 上 atomic diagonalize；central 与同素数 chains 仍由
笔记 209 的独立预算处理。本结论不闭合 adjacent `m>X` boundary pseudocovariance，
也不单独推出新的零点比例。

## 2. Aspect normalization

同时交换

\[
 (a,b,c,d,h)\longmapsto(b,a,d,c,-h)
\tag{7}
\]

保持式 (4) 不变。因此可设

\[
 A\ge B,\qquad C\ge D.
\tag{8}
\]

定义 geometric long/short scales 与 aspect length

\[
 U=(AC)^{1/2},\qquad V=(BD)^{1/2},
 \qquad K=U/V.
\tag{9}
\]

由 ratio compatibility，

\[
 K\asymp A/B\asymp C/D,
 \qquad R\asymp UV\asymp KBD.
\tag{10}
\]

式 (2) 还给

\[
 B/D=L^{O_\rho(1)},qquad A/C=L^{O_\rho(1)},
\tag{11}
\]

而 `UV=R>=XL^(2-rho)`，所以 `U` 至少是 `X` 的固定正幂。取固定

\[
 0<\delta<\frac14.
\tag{12}
\]

证明分成

\[
 \text{moderate aspect: }V\ge U^\delta,
 \qquad
 \text{extreme aspect: }V<U^\delta.
\tag{13}
\]

这两个区域穷尽所有 boxes；边界选择不随 box 改变。

## 3. Moderate aspect：把长坐标外筛

在式 (13) 的第一种情形，先删除四变量中的 proper prime powers。

### 引理 222-C（moderate proper-power deletion）[T]

至少一个变量是 `p^j,j>=2` 的贡献为

\[
 o_\delta(RH_R).
\tag{14}
\]

#### 证明

dyadic interval 上

\[
 \sum_{n\asymp Z,\ n=p^j,\ j\ge2}\Lambda(n)
 \ll \sqrt Z\,L.
\tag{15}
\]

若长变量 `a` 是 proper power，固定 `a,b,h` 后，congruence `ad=h mod b`
在 `d` box 中给 `O(1+D/B)` 个解；ratio/product compatibility 与式 (11) 只产生
`L^{O_rho(1)}`。Chebyshev sums 和其余两个 pointwise Lambda bounds 因而给相对
`RH_R` 的

\[
 U^{-1/2}L^{O_\rho(1)}=o(1).
\tag{16}
\]

若短变量 `b` 是 proper power，相同 argument 给相对误差

\[
 V^{-1/2}L^{O_\rho(1)}=o(1),
\tag{17}
\]

因为 `V>=U^delta`。其余位置由交换变量得到。`square`

所以本节可令四变量均为素数。取

\[
 W=\min(B,D).
\tag{18}
\]

由式 (11)、(13)，`log W asymp_delta log U asymp L`。选固定

\[
 0<\kappa<\frac1{78},qquad
 \mathcal D=W^\kappa,qquad z=\mathcal D^{1/s},
\tag{19}
\]

其中 `s` 是二维 Selberg upper-bound sieve 的充分大 fixed parameter。于是
`z=o(W)`，所有 sieve primes 都小于任意 admissible `b,d`。

### 引理 222-D（unbalanced exact divisibility main term）[T]

对 squarefree `q_1,q_2`、其素因子均小于 `z`，令 `A_(q_1,q_2)(h)` 表示
`q_1|a,q_2|c`、在 `a,c` 上保留 smooth windows、在 `b,d` 上保留 prime Lambda
coefficients 的 fixed-determinant sum。则

\[
 A_{q_1,q_2}(h)
 =\mathbf1_{(q_1,q_2)\mid h}
 \frac{(q_1,q_2)}{q_1q_2}X_h
 +r_{q_1,q_2}(h),
\tag{20}
\]

其中

\[
 X_h\ll R,
\tag{21}
\]

且对任意 `epsilon>0`

\[
 \begin{aligned}
 r_{q_1,q_2}(h)
 \ll_{\varepsilon,\rho}{}&
 L^{O_\rho(1)}U^\varepsilon
 (BD)^{17/20}(B+D)^{1/4}\\
 &\times(q_1q_2)^{7/20}(q_1+q_2)^{1/4+\varepsilon}.
 \end{aligned}
\tag{22}
\]

#### 证明

与笔记 221 相同，写

\[
 a=q_1m_1,quad c=q_2m_2,
 \qquad n_2=q_1d,quad n_1=q_2b.
\tag{23}
\]

因为 `z<W<=b,d` 且 `b!=d`（否则 `|h|>=min(b,d)>H_R`），

\[
 (n_1,n_2)=(q_2b,q_1d)=(q_1,q_2).
\tag{24}
\]

smooth arguments 精确变成

\[
 w_A\!\left(\frac{x+h}{dA}\right),
 \qquad
 w_C\!\left(\frac{x}{bC}\right),
\tag{25}
\]

故主积分与 `q_1,q_2` 无关。其支撑长度为
`O(AD)\asymp O(BC)\asymp O(R)`；除以 `bd` 后对两个 Chebyshev sums 求和，得到
式 (21)。

Bettin--Chandee Corollary 1 中

\[
 \begin{gathered}
 M_1\asymp A/q_1,\quad M_2\asymp C/q_2,\\
 N_1\asymp q_2B,\quad N_2\asymp q_1D,\\
 \mathcal R=AD/(CB)+CB/(AD)\asymp1,
 \end{gathered}
\tag{26}
\]

且

\[
 \|\alpha\|_2\|\beta\|_2
 \ll (BD)^{1/2}L.
\tag{27}
\]

代入其 error formula 即得式 (22)。`square`

### 引理 222-E（moderate-aspect incidence）[T]

在 `V>=U^delta` 中，一致地有

\[
 \mathfrak D_{A,B;C,D}(H_R)
 \ll_{\delta,\rho}RH_R(\log L)^C.
\tag{28}
\]

#### 证明

对 `a,c` 应用笔记 221-R2 的二维 Selberg sieve。式 (20) 给相同 local factors

\[
 v_h(p)=
 \begin{cases}
 1-2/p,&p\nmid h,\\
 1-1/p,&p\mid h,
 \end{cases}
\tag{29}
\]

所以 sieve main term 至多

\[
 X_h(\log z)^{-2}\mathfrak S_2(h).
\tag{30}
\]

恢复两个长变量的 pointwise Lambda weights 支付
`O(log A log C)`；由 `log z asymp_delta log U`，该因子与式 (30) 的两个 sieve
logarithms 相消至常数。引理 221-E 给

\[
 \sum_{1\le|h|\le H_R}\mathfrak S_2(h)\ll H_R,
\tag{31}
\]

故主项为 `O(RH_R)`。

Selberg quadratic expansion仍只产生 `mathcal D^2` 个 ordered divisor pairs，且
`q_1,q_2<=mathcal D^2`。由式 (22)，总 remainder 在恢复长 Lambda weights并对
`h` 求和后，除以 `RH_R` 至多

\[
 L^{O_\rho(1)}U^\varepsilon
 \frac{(BD)^{17/20}(B+D)^{1/4}}{R}
 \mathcal D^{39/10}.
\tag{32}
\]

写 `B=Vtau,D=V/tau`，其中 `tau=L^{O_rho(1)}`。由 `R asymp UV`，式 (32) 为

\[
 L^{O_\rho(1)}U^\varepsilon
 \frac{V^{19/20+(39/10)\kappa}}U.
\tag{33}
\]

因为 `U>=V`，它至多

\[
 L^{O_\rho(1)}U^\varepsilon
 V^{-1/20+(39/10)\kappa}.
\tag{34}
\]

先固定 `kappa<1/78`，再取

\[
 0<\varepsilon<
 \frac\delta2\left(\frac1{20}-\frac{39}{10}\kappa\right).
\tag{35}
\]

由 `V>=U^delta`，式 (34) 是负的 `U` 幂乘 polylog，故为 `o(1)`。结合引理
222-C 得式 (28)。`square`

## 4. Extreme aspect：固定短因子后的两线性形式

现在设

\[
 V<U^\delta.
\tag{36}
\]

则

\[
 K=U/V>U^{1-\delta}.
\tag{37}
\]

这里只删除长变量 `a,c` 的 proper powers；短变量 `b,d` 的所有 prime powers
连同 cross same-base pairs 一并保留。

### 引理 222-F（extreme long proper-power deletion）[T]

`a` 或 `c` 是 proper prime power 的总贡献为 `o(RH_R)`。

#### 证明

固定 `a,b,d,h` 后 `c` 唯一。对 proper `a` 用式 (15)，对 `b,d` 用 Chebyshev，
对 `c` 用 pointwise Lambda bound，得到

\[
 H_R\sqrt U\,BD\,L^{O_\rho(1)}.
\tag{38}
\]

由 `R asymp U V`、`BD=V^2`，式 (38) 相对 `RH_R` 为

\[
 \frac V{\sqrt U}L^{O_\rho(1)}
 \le U^{\delta-1/2}L^{O_\rho(1)}=o(1),
\tag{39}
\]

因为 `delta<1/4`。`c` 的情形相同。`square`

固定短 prime powers `b,d`，令

\[
 g=(b,d),\qquad b=gb',\quad d=gd',\qquad (b',d')=1.
\tag{40}
\]

只有 `g|h` 时有解；写 `h=gh'`。任取一个 particular solution `(a_0,c_0)`，
全部解为

\[
 a=a_0+b'k,qquad c=c_0+d'k.
\tag{41}
\]

与 long boxes 相交的 `k` interval 长度满足

\[
 K_{b,d}\asymp gK
 \asymp \frac{Rg}{BD},
\tag{42}
\]

只要该交集非空；端点误差为 `O(1)`，由式 (37) 可吸收。

### 引理 222-G（two-linear-form upper sieve）[T]

对固定 `b,d,h'!=0`，式 (41) 中 `a,c` 同时为素数的数量满足

\[
 \#\{k:a,c\text{ prime}\}
 \ll
 \frac{K_{b,d}}{(\log K_{b,d})^2}
 \mathfrak S_2\!\left(h'\operatorname{rad}(b'd')\right)
 +K_{b,d}^{2\kappa_0+\varepsilon},
\tag{43}
\]

其中任取 fixed `0<kappa_0<1/2`，隐常数一致。

#### 证明

对奇素数 `p`，若 `p` 不整除 `b'd'`，两线性形式各排除一个 residue；由

\[
 d'a-b'c=h'
\tag{44}
\]

两 roots 重合当且仅当 `p|h'`。因此 local excluded-residue count 为

\[
 \nu(p)=
 \begin{cases}
 2,&p\nmid h'b'd',\\
 1,&p\mid h',\ p\nmid b'd'.
 \end{cases}
\tag{45}
\]

若 `p|b'd'`，则对任何有 prime solution 的 tuple 必有 `p\nmid h'`，否则另一
long form 恒被 `p` 整除；此时也只有一个 excluded residue。`p=2` 由选择正确
parity class 支付绝对常数。

故 Selberg sieve product 相对 generic dimension-two product只在
`p|h'rad(b'd')` 处乘

\[
 \frac{1-1/p}{1-2/p}=1+\frac1{p-2},
\tag{46}
\]

即式 (43) 的 singular factor。对长度 `K_(b,d)` 的 interval，squarefree modulus
`q` 的 residue count 是

\[
 \frac{\nu(q)}qK_{b,d}+O(\nu(q)).
\tag{47}
\]

取 Selberg support `Delta=K_(b,d)^kappa_0`；quadratic expansion 的 remainder
为 `O(Delta^2 K_(b,d)^epsilon)`，得到式 (43)。这只是标准 upper-bound sieve 的
直接 residue-count specialization。`square`

### 引理 222-H（extreme-aspect incidence）[T]

在式 (36) 中，一致地有

\[
 \mathfrak D_{A,B;C,D}(H_R)
 \ll_\rho RH_R(\log L)^C.
\tag{48}
\]

#### 证明

由式 (37)、(42)，

\[
 \log K_{b,d}\asymp_\delta\log U.
\tag{49}
\]

因此恢复 long prime weights `Lambda(a)Lambda(c)` 时，式 (43) 主项的两个
sieve logarithms抵消两个 pointwise logarithms。对 fixed `b,d`，只对
`h=gh'` 求和。引理 221-E 及

\[
 \mathfrak S_2(h'\operatorname{rad}(b'd'))
 \ll \mathfrak S_2(h')
 \prod_{p\mid b'd',\ p>2}\left(1+\frac1{p-2}\right)
\tag{50}
\]

给

\[
 \sum_{1\le|h'|\le H_R/g}
 \mathfrak S_2(h'\operatorname{rad}(b'd'))
 \ll \frac{H_R}g
 \prod_{p\mid b'd',\ p>2}\left(1+\frac1{p-2}\right).
\tag{51}
\]

每个 `b,d` 都是 prime powers，所以式 (51) 最多含两个额外 Euler factors，且
各自至多 `2`。利用式 (42)，fixed `b,d` 的 main contribution 至多

\[
 \Lambda(b)\Lambda(d)K_{b,d}\frac{H_R}g
 \ll
 \Lambda(b)\Lambda(d)K H_R.
\tag{52}
\]

对 `b,d` 用 Chebyshev sums，得到

\[
 KH_R\sum_{b\asymp B}\Lambda(b)
       \sum_{d\asymp D}\Lambda(d)
 \ll KBDH_R\asymp RH_R.
\tag{53}
\]

这一步同时处理 `base(b)=base(d)`：`g` 在 `K_(b,d)` 中增加的 factor 与可用
shift 数 `H_R/g` 精确抵消，没有遗漏 same-base chain。

式 (43) 的 remainder 相对其 fixed-pair natural main scale
`K_(b,d)H_R/g` 至多

\[
 L^{O_\rho(1)}K_{b,d}^{-1+2\kappa_0+\varepsilon}.
\tag{54}
\]

取例如 `kappa_0=1/10` 与足够小 `epsilon`。由
`K_(b,d)>=K>U^(1-delta)`，式 (54) 一致为 `o(1)`。对短 weights 求和后仍为
`o(RH_R)`。最后加回引理 222-F，得到式 (48)。`square`

## 5. 定理 222-A 与推论 222-B 的证明

式 (13) 穷尽所有 normalized boxes。moderate 区由引理 222-E、extreme 区由引理
222-H 控制，所以式 (5) 成立。它以 `sigma=0` 验证笔记 220-B 的全部假设；代入
该定理即得式 (6) 与 critical-shell bulk/finite closure。再与笔记 209--218 的
central、same-prime、subcritical、transition 与 Fejer transfer 结论拼接，得到推论
222-B。`square`

## 6. 最小输入、删除审计与循环性

1. **ratio compatibility**：在 moderate 区保证 Bettin--Chandee ratio parameter
   `mathcal R asymp1`；在 extreme 区保证两 long intervals 产生同一长度 `K_(b,d)`。
   删除后两种机制都可能失去 uniformity。
2. **Bettin--Chandee `1/20` power saving**：只用于 moderate 区式 (34)。删除后
   Selberg remainder不再自动小于 `R`。
3. **direct residue law (47)**：只用于 extreme 区；它利用 determinant fiber
   已退化成一参数 affine line。以 arbitrary-coefficient Bessel bound替换它会丢掉
   两个 long prime logarithms。
4. **aspect split**：moderate 区需要短 factors 足够大以把 sieve primes置于其下；
   extreme 区需要 `K` 是 `U` 的固定正幂以支付直接筛 remainder。式 (13) 保证二者
   无缝覆盖。
5. **gcd ledger**：式 (40)--(53) 处理 `base(b)=base(d)`。若错误地假设 `(b,d)=1`，
   会漏掉小短因子与 `g|h` 的全部层。
6. **shift average**：逐 shift singular factor 不一致有界；引理 221-E 在式 (31)、
   (51) 中不可删除。
7. **proper-power separation**：moderate 区全部删除；extreme 区只删除 long powers，
   short powers保留在 gcd ledger。把 extreme short powers粗略 pointwise 删除会在
   `V=O(1)` 时失去 uniformity。

循环性审计：式 (5) 完全位于 finite prime-side determinant incidence。外部输入只有
Bettin--Chandee Corollary 1 与标准 Selberg upper-bound sieve；不使用 RH、GRH、
zero-density、Hardy--Littlewood asymptotic、Weil positivity或有界负指标。推论
222-B 使用的是此前已证明的 finite-to-bulk/clustered Fejer implications，不把所求
四矩结论藏入公理。

## 7. 模型范围与论文接口

- Riemann zeta：定理直接闭合 alternating/Farey primitive critical shell。
- 固定本原 Dirichlet `L`：absolute positive majorant中 unit character phases消失，
  同一 bound适用；完整四矩仍受 adjacent boundary channel 限制。
- Dedekind/automorphic `L`：需要把 short coefficients 的 Chebyshev first moment 与
  long two-linear-form prime sieve替换为相应 coefficient estimates；现有
  Rankin--Selberg second moment不自动给式 (53)。
- 函数域：应有 polynomial determinant 的 degree-aspect analogue，但本整数
  Kloosterman/sieve theorem不直接声称适用。
- 无 Euler product 的谱 zeta：没有式 (4) 的 four-factor interface，不在范围内。

论文接口：笔记 220--222 已形成一条独立的“critical determinant shell”论文级
lemma chain；在宣称文献新颖性前仍需专门检索现有四素数 determinant upper bounds。
对四矩主论文，alternating/Farey channel 的剩余工作由此降为结果拼装与归一化复核，
真正未闭合的算术通道回到笔记 206--208 的 adjacent supercritical boundary
pseudocovariance。

## 8. 下一最小引理 222-I [O]

回到 actual `m>X` adjacent boundary block `B_X(T)`。在 relative gaps 为 `o(T)` 的
共同 good heights 上，证明

\[
 \beta_L^4\|B_X(T)B_X(T)^{\mathsf T}\|_{\mathrm{HS}}^2=o(N),
\tag{55}
\]

或构造保留 prime phases 与 physical windows 的主尺度 lower bound。不得用
`B_XB_X^*` covariance、任意系数 Bessel bound 或 natural lower/upper pairing 代替
无共轭 pseudocovariance。

## 9. 后续逆审计修正（笔记 231）

定理 222-A 与 primitive critical-shell 推论保持不变；原第 1、5 节把 central
block 说成由笔记 209 的独立预算处理，不能单独推出 central--primitive cross
为 `o(N)`。笔记 231 已证明该 cross 在每个标准短高度区间上的 signed first mean
为 `o(N)`。所以“完整 alternating ledger”必须引用笔记 231；本笔记自身只给
primitive--primitive 的 uniform closure。

## 10. 后续全局覆盖修正（笔记 232）

定理 222-A 与式 (6) 的 critical-shell closure 保持 [T]。笔记 232 由 exact
alternating support 和受限 paired diagonal 证明，`ab<=XL^2` 不是完整 physical
support；其外 atomic diagonal 有正主质量。因此推论 222-B 必须读作
“entire critical shell closure”，不能读作完整 primitive alternating closure。

## 11. 后续 fixed-polylog 推广（笔记 233）

笔记 233 逐项复核 moderate/extreme proof，证明式 (5) 对任意 fixed polylog
product band `XL^K_-<=AB,CD<=XL^K_+` 一致成立；原文的上端 `XL^2` 不是
determinant theorem 本身的极限。与全局 Fejer/finite ledger结合后可闭合所有
`ab<=XL^K,K<3`，但不能据此进入 fixed-power high-product 区。
