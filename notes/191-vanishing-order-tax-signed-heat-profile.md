# NCE-8：高阶消失税与 signed Gaussian heat profile

文档 190 提出了两个互补想法：

1. 用任意高阶零点的 polynomial effect，把 broad Gaussian response 推到高
   convolution order；
2. 把 Cauchy cusp 压缩成 ultra-near multiplicative heat small-ball energy。

本笔记对第一条作定量审计，得到一个 sharp stopping rule：在 bounded Hodge
index 所需的 $\rho=O(1)$ regime，谱宽 $B\to\infty$ 会把 soft transition
压缩到 normalized width $\lambda=\rho/B$。任何 uniform polynomial approximant
不仅 degree 至少为 $\Omega(B/\rho)$；若强制 $r$ 阶零点，则所有逐 monomial
取绝对值的 moment proof 都要付出

$$B\theta(\theta/\lambda)^{2r}$$

级 coefficient tax。经典 PNT 只使 relative discrepancy $\theta\to0$，但其
absolute scale $B\theta$ 仍可增长，所以提高 $r$ 反而恶化该类上界。

因此 high-order ideal density 仍是正确的 qualitative existence theorem，却
不能与 coefficientwise absolute moment bounds 组合成 RH proof。可晋级的对象
是第二条路线的 signed cumulative heat profile；本笔记给出它的 exact
Abel--Volterra identity，并把它精确写成 balanced multiplicative short
intervals。

## 1. Cofinal soft transition 的 degree floor

在 $[-B,B]$ 上令

$$a_\rho(x)=\frac{(-x)_+}{(-x)_++\rho},\qquad
0<\rho\le B.$$                                    (1)

注意

$$a_\rho(0)=0,\qquad a_\rho(-\rho)=1/2.$$          (2)

### 定理 AGP（Bernstein soft-transition degree tax）[U]

若 real polynomial $p$ 的 degree 为 $D$，且

$$\|p-a_\rho\|_{L^\infty[-B,B]}\le\epsilon<1/4,$$ (3)

则令 $\lambda=\rho/B$，有

$$D\ge
\frac{\sqrt{1-\lambda^2}\,(1/2-2\epsilon)}
     {\lambda(1+\epsilon)}.$$                    (4)

特别地，当 $\rho=O(1)$、$B\to\infty$ 且 $\epsilon$ 与 $1/4$ 保持正距离时，

$$D=\Omega(B/\rho).$$                              (5)

#### 证明

令 $q(y)=p(By)$。由式 (2)--(3)，

$$|q(-\lambda)-q(0)|\ge1/2-2\epsilon.$$           (6)

mean-value theorem 给某个 $\xi\in(-\lambda,0)$，

$$|q'(\xi)|\ge(1/2-2\epsilon)/\lambda.$$           (7)

又有 $\|q\|_\infty\le1+\epsilon$。Bernstein polynomial inequality 给

$$\sqrt{1-\xi^2}|q'(\xi)|\le D\|q\|_\infty.$$      (8)

因为 $\sqrt{1-\xi^2}\ge\sqrt{1-\lambda^2}$，合并式 (7)--(8) 即得式
(4)。$\square$

这个下界与 Jackson upper rate 的 $B/(\rho D)$ 方向一致。它说明文档 190
冻结审计使用的 $\rho=B/3$ 只适合 finite diagnostics；在真正 cofinal
bounded-index criterion 中，$2\rho$ 必须一致有界，transition degree 必然增长。

## 2. 强制高阶零点的 coefficient tax

仍在 normalized variable $y=x/B$ 中。假设

$$p(By)=y^r s(y),\qquad r\ge0,$$                   (9)

并满足式 (3)。signed response polynomial 写成

$$R(y)=-y\,p(By)^2
      =-y^{2r+1}s(y)^2
      =\sum_k c_k y^k.$$                          (10)

### 定理 AGQ（vanishing-order absolute-ledger no-gain）[U]

对任意 $\theta\ge\lambda=\rho/B$，

$$\sum_k|c_k|\theta^k
\ge(1/2-\epsilon)^2\,
   \theta(\theta/\lambda)^{2r}.$$                 (11)

因此，若一个 proof strategy 只使用 normalized absolute moment majorants

$$|\tau[(H/B)^k]|\le\theta^k,$$                   (12)

则它给 response 所形成的 coefficientwise upper ledger 必至少为

$$B(1/2-\epsilon)^2
  \theta(B\theta/\rho)^{2r}.$$                   (13)

当 absolute discrepancy scale $B\theta>\rho$ 时，增加 vanishing order $r$
只会使这类证明预算变坏。

#### 证明

由 $p(-\rho)$ 对 $a_\rho(-\rho)=1/2$ 的逼近，

$$|s(-\lambda)|
\ge(1/2-\epsilon)\lambda^{-r}.$$                 (14)

写 $s(y)^2=\sum_jb_jy^j$。当 $\theta\ge\lambda$，

$$\sum_j|b_j|\theta^j
\ge\sum_j|b_j|\lambda^j
\ge|s(-\lambda)|^2.$$                            (15)

式 (10)、(14)--(15) 给式 (11)。乘回 physical response scale $B$ 得式
(13)。$\square$

定理 AGQ 是对 proof ledger 的下界，不是对 actual signed response 的下界。
它排除的正是“高阶零点 + 每个 moment 单独取绝对值”这一组合；它不排除不同
moments、product shells 或 Gaussian scales 之间的 signed cancellation。

### 对经典 PNT 输入的含义

文档 190 的 repeated-primitive bound 在 fixed Gaussian scale 上产生一个
relative discrepancy parameter，粗略为

$$\theta_Y(u)\asymp
\frac{|M_Y|+E_Y/\sqrt u}{B_Y}.$$                 (16)

经典 zero-free-region PNT 可给 $\theta_Y(u)\to0$，但在 $u=O(1)$ 上

$$B_Y\theta_Y(u)\asymp |M_Y|+E_Y/\sqrt u$$        (17)

不因此一致有界，更不会自动小于 fixed $\rho$。所以定理 AGQ 表明：用 increasing
$r$ 把 PNT relative saving 提到高次幂时，transition coefficient tax 会把同一
saving 抵消并可能放大。

这严格修正文档 190 的乐观部分：high-order ideal density 提供 existence，
但没有提供有用的 absolute arithmetic certificate。

## 3. Signed cumulative Gaussian profile

令 $q$ 是 finite real/Hermitian response lag measure，分离 numerical zero atom
$q_0=q(\{0\})$。定义 signed cumulative profile

$$Q_q(h)=q(\{x:0<|x|\le h\}),\qquad h\ge0.$$       (18)

对 $U>0$ 定义 Gaussian response

$$S_q(U)=\int e^{-x^2/(4U)}\,dq(x).$$              (19)

### 定理 AGR（signed Gaussian Abel--Volterra identity）[U]

有 exact identity

$$S_q(U)
=q_0+\int_0^\infty e^{-z}
       Q_q(2\sqrt{Uz})\,dz.$$                    (20)

因此定义 profile capacity

$$\mathcal C_q(U)
=\int_0^\infty e^{-z}
       |Q_q(2\sqrt{Uz})|\,dz,$$                  (21)

就有

$$|S_q(U)-q_0|\le\mathcal C_q(U)
\le H_q(U),$$                                    (22)

其中

$$H_q(U)=\int_{x\ne0}e^{-x^2/(4U)}\,d|q|(x)$$     (23)

是文档 190 的 coefficientwise heat small-ball variation。

#### 证明

把式 (19) 的 nonzero 部分写成 Stieltjes integral

$$\int_0^\infty e^{-h^2/(4U)}\,dQ_q(h).$$         (24)

integration by parts 后得到

$$\int_0^\infty
Q_q(h)\frac{h}{2U}e^{-h^2/(4U)}\,dh.$$           (25)

代换 $z=h^2/(4U)$ 得式 (20)。取绝对值得第一条式 (22)。令

$$V_q(h)=|q|(\{x:0<|x|\le h\}),$$                 (26)

同样的 layer-cake identity 给
$H_q(U)=\int_0^\infty e^{-z}V_q(2\sqrt{Uz})dz$；
由 $|Q_q(h)|\le V_q(h)$ 得第二条式 (22)。$\square$

式 (20) 是比 absolute heat energy 更合适的 NCE-8 target：它在每个 radius
先累加 canonical coefficient signs，再对 radius 作 positive Abel average。

## 4. Product-ratio short-interval identity

沿文档 188 的 formal lag group，写一个 lag 为

$$g=(a/b,\mathbf k),\qquad
\ell(g)=\log(a/b)+\mathbf k\cdot\boldsymbol\lambda,$$ (27)

其中 $a,b$ coprime positive integers。固定 continuum shift

$$c=\mathbf k\cdot\boldsymbol\lambda.$$            (28)

### 定理 AGS（heat profile is a signed multiplicative interval sum）[U]

对任意 $h\ge0$，

$$|\ell(g)|\le h$$

当且仅当

$$b\,e^{-c-h}\le a\le b\,e^{-c+h}.$$              (29)

所以对 response map $q$，

$$Q_q(h)=
\sum_{\substack{g\ne0\\
 b e^{-c-h}\le a\le b e^{-c+h}}}q_g.$$           (30)

对 degree-two map

$$q_2=-c_2^2
[d^{*5}-2\alpha B d^{*4}+\alpha^2B^2d^{*3}],
\qquad\alpha=\sqrt3/2,$$                          (31)

相应 profile 精确为

$$Q_{q_2}(h)=-c_2^2
[Q_5(h)-2\alpha BQ_4(h)+\alpha^2B^2Q_3(h)],$$    (32)

其中 $Q_k$ 是 $d^{*k}$ 在式 (29) 的 balanced multiplicative intervals
上的 signed cumulative mass。

#### 证明

式 (29) 由
$-h\le\log(a/b)+c\le h$ exponentiate 得到。对 coefficients 求和得式
(30)；式 (32) 是式 (31) 的线性展开。$\square$

定理 AGS 把下一算术引理明确连接到 Volterra/Mellin machinery：不是估计所有
近 product tuple 的数量，而是估计三个指定 convolution orders 的共同 signed
短乘法区间组合。

## 5. Finite implementation

脚本 scripts/formal_lag_response.py 新增：

- degree-two response map 的 Gaussian heat-distance shells；
- signed cumulative layer-cake 的 exact finite summation；
- profile capacity、coefficient variation 与 cancellation ratio。

脚本 scripts/soft_negative_moment.py 新增：

- 定理 AGP 的 Bernstein degree floor；
- 定理 AGQ 的 coefficient-ledger lower bound。

回归测试验证：

1. heat shells 与 direct Gaussian response 完全一致；
2. layer-cake sum 与 direct response 完全一致；
3. $|S-q_0|\le\mathcal C_q\le H_q$；
4. 当 $B\theta>\rho$ 时，高阶 coefficient tax 随 $r$ 严格增长。

## 6. Frozen scale audit

对 degree-two frozen prime--continuum models，profile capacity 如下。所有数字
仍是 double-precision diagnostics。

| $Y,N$ | $U$ | exact | nonexact signed | profile capacity | coefficient variation | capacity/variation |
|---:|---:|---:|---:|---:|---:|---:|
| $4,7$ | $.01$ | $.02722$ | $-.02038$ | $.02101$ | $.07651$ | $.2746$ |
| $4,7$ | $.16$ | $.02722$ | $-.02447$ | $.02634$ | $.3459$ | $.07614$ |
| $4,7$ | $2.56$ | $.02722$ | $-.02319$ | $.02368$ | $1.100$ | $.02151$ |
| $8,10$ | $.01$ | $.03132$ | $-.02521$ | $.02681$ | $.09616$ | $.2788$ |
| $8,10$ | $.16$ | $.03132$ | $-.02882$ | $.03072$ | $.4346$ | $.07069$ |
| $8,10$ | $2.56$ | $.03132$ | $-.03003$ | $.03066$ | $1.437$ | $.02134$ |
| $12,12$ | $.01$ | $.03067$ | $-.02514$ | $.02715$ | $.1145$ | $.2370$ |
| $12,12$ | $.16$ | $.03067$ | $-.02614$ | $.02853$ | $.5115$ | $.05576$ |
| $12,12$ | $2.56$ | $.03067$ | $-.02973$ | $.03053$ | $1.739$ | $.01755$ |
| $16,15$ | $.01$ | $.02876$ | $-.02259$ | $.02447$ | $.1303$ | $.1878$ |
| $16,15$ | $.16$ | $.02876$ | $-.02065$ | $.02314$ | $.5666$ | $.04084$ |
| $16,15$ | $2.56$ | $.02876$ | $-.02737$ | $.02842$ | $1.963$ | $.01448$ |

在这些小尺度上，coefficient variation 明显增长，而 profile capacity 保持在
约 $.021--.032$。宽 Gaussian scale 的 capacity/variation 从约 $2.15\%$
下降到 $1.45\%$。冻结 $Y=8,U=.01$ 的最内 heat shell
$|\ell|\le\sqrt U$ 中，signed/variation ratio 只有约 $1.68\%$。

这些趋势支持 signed cumulative target，不能外推成 uniform theorem 或 RH
证据。特别是当前 degree-two audit 仍取 $\rho=B/3$，不满足 cofinal
$\rho=O(1)$ 的最终 schedule。

## 7. 分支决策

### 停止

以下组合不再作为独立主线：

1. high-order ideal density；
2. classical PNT repeated-primitive moments；
3. monomial moments 逐项取绝对值。

定理 AGQ 说明其 coefficient tax 在 relevant regime 抵消高阶 PNT saving。

### 晋级

NCE-8 的下一主对象改为 mixture-integrated signed profile capacity：

$$\int_0^\infty m(U)\mathcal C_{q_Y}(U)\,dU.$$     (33)

若 along a cofinal schedule 可证明

$$q_Y(\{0\})=O(1),\qquad
\int_0^\infty m(U)\mathcal C_{q_Y}(U)\,dU=O(1),$$ (34)

再加 polynomial/effect 与 explicit-formula error ledger，则文档 149 的
bounded finite-trace Hodge--Weil theorem 推出中心线结论。

式 (34) 仍有 RH 强度；本笔记没有证明它。其价值在于它只要求 canonical
signed cumulative short-interval combination，不要求 full Selberg profile、
全部 moment PSD 或 arbitrary-direction large sieve。

## 8. 下一最小引理

1. 对式 (32) 做一次 common Abel/Volterra summation by parts，寻找
   $Q_5-2\alpha BQ_4+\alpha^2B^2Q_3$ 的 boundary cancellation；
2. 分离 prime count、continuum integral 与 mixed terms，但保持三阶组合共同
   gauge，不逐 component 取绝对值；
3. 证明或否证
   $\int m(U)\mathcal C_{q_Y}(U)dU=O(1)$ 是否已等价于文档 169 的 full
   Selberg profile；
4. 若仍过强，改用 response 本身的 signed integral，而不是 capacity 的绝对值；
5. 对真正 $\rho=O(1)$ 的 growing-degree Chebyshev effect 重复 profile audit，
   明确记录 degree conditioning。

## 9. 审计结论

高阶零点的非构造存在性没有消失，但其与 absolute moment estimates 的组合被
Bernstein transition tax 和 coefficient tax 严格阻断。新的可行接口是 signed
Gaussian cumulative profile：它有 exact layer-cake identity、精确
multiplicative short-interval解释，并在有限尺度上比 coefficient variation
小一到两个数量级。下一轮应直接研究式 (32)--(34) 的 common Volterra
cancellation，而不是继续提高 polynomial vanishing order。
