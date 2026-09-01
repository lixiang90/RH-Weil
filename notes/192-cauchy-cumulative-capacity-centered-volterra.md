# NCE-8：Cauchy cumulative capacity 与 centered Volterra factorization

文档 190 用 Gamma mixture 把 Cauchy state 分解成 Gaussian scales；文档 191
进一步把每个 Gaussian response 写成 signed cumulative heat profile。本笔记
证明两层辅助参数可以重新消去：Gaussian profile capacities 的 Gamma mixture
精确等于一个单一的 Cauchy cumulative capacity，

$$\mathcal C_C(q)=\int_0^\infty e^{-h}|Q_q(h)|\,dh.$$ (1)

与此同时，degree-two shifted-moment response 在 centered discrepancy primitive
上有一个共同 Volterra factorization。三、四、五阶 moments 不再作为三个独立
对象出现，而是同一 polynomial

$$ (M+z)^3(M-\alpha B+z)^2 $$                    (2)

作用在 primitive convolution tower 上。

这给 NCE-8 一个更接近 bounded finite-trace Hodge--Weil theorem 的接口：
直接控制 canonical Cauchy trace 的 signed cumulative capacity，不需要先分别
选择 Gaussian cutoff，也不需要逐 moment 取绝对值。

## 1. Direct Cauchy layer-cake identity

令 $q$ 是 finite real/Hermitian lag measure。把 numerical zero atom 记为

$$q_0=q(\{0\}),$$                                  (3)

并定义 nonzero signed cumulative profile

$$Q_q(h)=q(\{x:0<|x|\le h\}),\qquad h\ge0.$$       (4)

### 定理 AGT（Cauchy signed cumulative identity）[U]

有 exact identity

$$\int_{\mathbb R}e^{-|x|}\,dq(x)
=q_0+\int_0^\infty e^{-h}Q_q(h)\,dh.$$            (5)

因此定义

$$\mathcal C_C(q)
=\int_0^\infty e^{-h}|Q_q(h)|\,dh,$$              (6)

就有

$$\left|
\int e^{-|x|}\,dq(x)-q_0
\right|
\le\mathcal C_C(q)
\le\int_{x\ne0}e^{-|x|}\,d|q|(x).$$              (7)

#### 证明

把 nonzero response 写成 radial Stieltjes integral

$$\int_0^\infty e^{-h}\,dQ_q(h).$$                (8)

integration by parts 给式 (5)。第一条式 (7) 来自 triangle inequality。
若

$$V_q(h)=|q|(\{x:0<|x|\le h\}),$$                 (9)

则同一 identity 给

$$\int_{x\ne0}e^{-|x|}\,d|q|(x)
=\int_0^\infty e^{-h}V_q(h)\,dh.$$               (10)

由 $|Q_q(h)|\le V_q(h)$ 得第二条式 (7)。$\square$

这个 capacity 先在每个 multiplicative radius 内累加全部 canonical signs，
然后才取绝对值。它严格弱于 coefficient variation，但仍足以一致控制 nonexact
Cauchy response。

## 2. Gaussian mixture capacities collapse exactly

沿文档 190，normalized Gaussian lag kernel 与 Cauchy mixing density 为

$$K_U(x)=e^{-x^2/(4U)},\qquad
m(U)=\frac{e^{-U}}{\sqrt{\pi U}}.$$               (11)

文档 191 的 Gaussian profile capacity 为

$$\mathcal C_G(q;U)
=\int_0^\infty e^{-z}|Q_q(2\sqrt{Uz})|\,dz.$$     (12)

### 定理 AGU（mixture-capacity collapse）[U]

有

$$\int_0^\infty m(U)\mathcal C_G(q;U)\,dU
=\mathcal C_C(q).$$                               (13)

同样，

$$\int_0^\infty m(U)
\left[
\int_0^\infty e^{-z}Q_q(2\sqrt{Uz})\,dz
\right]dU
=\int_0^\infty e^{-h}Q_q(h)\,dh.$$                (14)

#### 证明

Gaussian layer-cake 在 radius variable 中是

$$\mathcal C_G(q;U)
=\int_0^\infty
\frac{h}{2U}e^{-h^2/(4U)}|Q_q(h)|\,dh.$$          (15)

Tonelli theorem 允许交换两个 nonnegative integrals。文档 190 的
Cauchy--Gaussian characteristic identity 对 $h$ 求导给

$$\int_0^\infty m(U)
\frac{h}{2U}e^{-h^2/(4U)}\,dU=e^{-h}.$$           (16)

代入式 (15) 得式 (13)。signed 情形对 finite $q$ 用 Fubini，得到式 (14)。
$\square$

所以 Gaussian decomposition 是发现与局部估计工具，不是最终 theorem 的额外
结构。最终 capacity 就是原 Cauchy trace 上的式 (6)。

## 3. Centered discrepancy primitive

令 $d$ 是 compactly supported even finite signed lag measure，total mass 为

$$M=d(\mathbb R).$$                                (17)

写

$$d=M\delta_0+\nu,\qquad \nu(\mathbb R)=0.$$       (18)

取 odd distributional primitive $A$ 使

$$DA=\nu.$$                                        (19)

令

$$\alpha=\sqrt3/2,\qquad N=M-\alpha B.$$           (20)

degree-two response measure 是

$$q_2=-c_2^2d^{*3}*(d-\alpha B\delta_0)^{*2}.$$   (21)

定义 coefficients $b_j$：

$$ (M+z)^3(N+z)^2=\sum_{j=0}^5b_jz^j.$$          (22)

显式地，

$$b_0=M^3N^2,$$                                    (23)

$$b_1=2M^3N+3M^2N^2,$$                            (24)

$$b_2=M^3+6M^2N+3MN^2,$$                          (25)

$$b_3=3M^2+6MN+N^2,$$                             (26)

$$b_4=3M+2N=5M-2\alpha B,\qquad b_5=1.$$          (27)

### 定理 AGV（common centered Volterra factorization）[U]

在 compactly supported distributions 的 convolution algebra 中，

$$q_2=-c_2^2
\left[
b_0\delta_0+\sum_{j=1}^5b_jD^j(A^{*j})
\right].$$                                        (28)

若 $d$ 有 smooth even density，且 $h>0$，则 symmetric interval cumulative
满足

$$q_2([-h,h])
=-c_2^2\left[
b_0+2\sum_{j=1}^5b_j
D^{j-1}(A^{*j})(h)
\right].$$                                        (29)

对 finite measures，式 (29) 以 mollification 后避开 boundary atoms 的
distributional limit 解释。

#### 证明

由式 (18)--(20)，

$$d=M\delta_0+DA,$$

$$d-\alpha B\delta_0=N\delta_0+DA.$$              (30)

把式 (30) 代入式 (21)，再按 $DA$ 的出现次数展开。每个
$(DA)^{*j}=D^j(A^{*j})$，coefficient 正是式 (22) 的 $b_j$，得到式 (28)。

对式 (28) 在 $[-h,h]$ 积分，把一个 distributional derivative 移到 interval
boundary，得到

$$D^{j-1}(A^{*j})(h)
-D^{j-1}(A^{*j})(-h).$$                           (31)

$A$ 为 odd；$A^{*j}$ 的 parity 是 $(-1)^j$，再作 $j-1$ 次 derivative 后总为
odd。因此式 (31) 等于两倍其在 $h$ 的值，得到式 (29)。$\square$

## 4. 为什么这个 factorization 比三个 moment bounds 更窄

当 $M/B$ 较小时，式 (23)--(27) 的 leading coefficients 是

$$b_3=\alpha^2B^2+O(|M|B+M^2),$$                 (32)

$$b_4=-2\alpha B+O(M),\qquad b_5=1,$$             (33)

而 $b_0,b_1,b_2$ 都至少含一个 $M$ factor。于是式 (29) 的 leading part 是

$$-2c_2^2
\left[
\alpha^2B^2D^2(A^{*3})
-2\alpha BD^3(A^{*4})
+D^4(A^{*5})
\right](h).$$                                    (34)

这恰是原

$$Q_5-2\alpha BQ_4+\alpha^2B^2Q_3$$              (35)

的共同 primitive 表达，而不是三条独立 inequalities。

若分别对式 (34) 的三项取绝对值，就退回文档 190 的 fixed-degree PNT barrier；
真正的新可能性是对整个 differential polynomial 作一次 common
Volterra/energy estimate，使三项共享 boundary gauge。

## 5. Cauchy profile criterion

对 cofinal response measures $q_Y$，假设 formal/numerical exact mismatch、
quadrature、Gamma 与 tail errors 已单列。由定理 AGT：

### 推论 AGW（signed cumulative Cauchy criterion）[C]

若

$$\sup_Y |q_Y(\{0\})|<\infty,$$                   (36)

以及

$$\sup_Y\mathcal C_C(q_Y)<\infty,$$               (37)

并且 polynomial soft-effect 与 explicit-formula error ledger 一致有界，则
canonical negative Hodge response 一致有界。结合文档 187 的 soft sandwich
与文档 149 的 bounded finite-trace Hodge--Weil theorem，目标 divisor 的全部
非零 zeros 位于中心线。

式 (36) 对 degree two 已由文档 189 的 parity-breaker theorem 更强地得到
$o(1)$。当前唯一新的 arithmetic core 是式 (37)，或者更弱地直接控制式 (5)
的 signed integral。

这个 criterion 没有宣称式 (37) 已证明；它是把现有广义结构定理压缩到一个
明确 Cauchy--Volterra capacity 的条件接口。

## 6. Finite audit

脚本 scripts/formal_lag_response.py 实现 finite response map 的 exact Cauchy
layer-cake summation、profile capacity 与 coefficient variation。冻结
degree-two models 给：

| $Y,N$ | total response | exact | nonexact | Cauchy capacity | coefficient variation | capacity/variation |
|---:|---:|---:|---:|---:|---:|---:|
| $4,7$ | $.004942$ | $.02722$ | $-.02228$ | $.02372$ | $.4521$ | $.05245$ |
| $8,10$ | $.004495$ | $.03132$ | $-.02682$ | $.02876$ | $.5761$ | $.04993$ |
| $12,12$ | $.005632$ | $.03067$ | $-.02504$ | $.02743$ | $.6845$ | $.04008$ |
| $16,15$ | $.007958$ | $.02876$ | $-.02080$ | $.02332$ | $.7633$ | $.03056$ |

profile capacity 保持在约 $.023--.029$，而 coefficient variation 随尺度增长；
capacity/variation 从约 $5.25\%$ 降到 $3.06\%$。这说明 cumulative ordering
保留了逐系数 absolute value 完全丢失的 cancellation。

这些是小尺度 double-precision diagnostics，且仍使用 $\rho=B/3$；不构成式
(37) 的 cofinal proof 或 RH evidence。

## 7. 与 Selberg profile 的循环性审计

式 (37) 与 full Selberg profile 的关系尚未确定：

- full Selberg profile 控制大量 arbitrary short-interval energies，显然足以
  majorize 某些 absolute versions；
- $\mathcal C_C(q_Y)$ 只读取一个 canonical shifted-moment polynomial 的 signed
  cumulative profile；
- capacity 在 radius 内先保留 prime、continuum 与不同 convolution orders 的
 共同 signs；
- 因此目前不能把它直接标为文档 169 的等价重述。

下一步必须尝试从式 (28)--(34) 独立证明 common energy estimate。若任何证明被迫
分别控制 $D^2A^{*3},D^3A^{*4},D^4A^{*5}$ 的 absolute square functions，并恰好
恢复 full Selberg profile，则 NCE-8 应停止。

## 8. 下一最小引理

1. 为 polynomial (22) 寻找一个 common antiderivative 或 completed square，
   避免式 (34) 三项分离；
2. 审计 $M$ 是否能由 constant-probe Euler--continuum cancellation 一致控制，
   从而压低 $b_0,b_1,b_2$；
3. 对 $A^{*3}$ 引入 logarithmic Volterra energy，检查式 (34) 是否是其二阶
   boundary derivative；
4. 在真正 $\rho=O(1)$、degree growing 的 canonical Chebyshev response 上计算
   direct Cauchy capacity；
5. 证明或否证 uniform Cauchy capacity 是否已经蕴含 full Selberg profile。

## 9. 审计结论

Gaussian scale mixture 最终可完全消去：其 signed profile capacities 精确汇合
成原 Cauchy trace 上的单一 cumulative capacity。degree-two response 又可在
centered discrepancy primitive 上写成一个共同 Volterra polynomial。当前
RH-strength input 因而被压缩为：不用 full Selberg profile，证明式 (28)--(37)
的 canonical signed cumulative capacity 一致有界。
