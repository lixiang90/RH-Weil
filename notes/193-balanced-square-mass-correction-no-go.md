# NCE-8：balanced square core、mass correction 与不可分离性

文档 192 把 degree-two response 写成 centered primitive tower。该展开在
total mass $M=0$ 时具有一个漂亮的 convolution-square core。本笔记证明这个
square 确实是 canonical 的，但也证明不能先单独控制 square core、再把
$M$-terms 当作 relative-small perturbation：

- absolute Banach-algebra perturbation 只给 $O(|M|)$，不是 $O(|M|/B)$；
- finite audit 中 $M/B$ 变小并不使 mass correction 单调消失；
- square core 与 mass correction 在实际 signed response 中发生主阶抵消。

正确主对象因而是一个保留完整 $M$ dependence 的 divided-difference Volterra
polynomial，而不是 isolated square。

## 1. Exact balanced-square core

令 $d$ 是 even finite lag measure，谱宽 majorant 为 $B$，并写

$$d=M\delta_0+\nu,\qquad \nu(\mathbb R)=0,\qquad
\nu=DA,$$                                         (1)

其中 $A$ 取 odd primitive。记

$$L=\alpha B,\qquad \alpha=\sqrt3/2.$$             (2)

degree-two response measure 为

$$q(d)=-c_2^2d^{*3}*(d-L\delta_0)^{*2}.$$         (3)

把 centered symbol $\nu$ 代入同一 polynomial，得到

$$q_{\mathrm{bal}}
=-c_2^2\nu^{*3}*(\nu-L\delta_0)^{*2}.$$           (4)

### 定理 AGX（balanced response has a primitive-square factor）[U]

定义

$$H=\nu*(\nu-L\delta_0),$$                         (5)

则

$$q_{\mathrm{bal}}
=-c_2^2D\left[A*H^{*2}\right].$$                 (6)

在 smooth even model 中，其 symmetric cumulative profile 为

$$q_{\mathrm{bal}}([-h,h])
=-2c_2^2[A*H^{*2}](h).$$                         (7)

#### 证明

由 $DA=\nu$，

$$D[A*H^{*2}]
=\nu*[\nu*(\nu-L\delta_0)]^{*2}
=\nu^{*3}*(\nu-L\delta_0)^{*2}.$$                (8)

这给式 (6)。$A$ odd，$H^{*2}$ even，所以 convolution 为 odd；对式 (6)
在 $[-h,h]$ 积分，两个 boundary values 相差两倍，得到式 (7)。$\square$

这个 square 是真实的 algebraic structure：$H^{*2}$ 在 Fourier side 对应
real multiplier $\widehat H(t)^2\ge0$。但式 (7) 仍是 odd primitive 与
positive-definite square 的 convolution，并不自动具有固定符号。

## 2. Mass correction 的 absolute perturbation scale

定义

$$q_M=q(d)-q_{\mathrm{bal}}.$$                    (9)

令

$$R=\max(\|d\|_1,\|\nu\|_1).$$                    (10)

### 定理 AGY（relative centering does not give an absolute small error）[U]

有

$$\|q_M\|_1
\le c_2^2|M|
\left[
5R^4+8LR^3+3L^2R^2
\right].$$                                       (11)

若 $B=\|d\|_1$、$|M|\le B$，则 $R\le2B$。又
$c_2^2\le4/(9B^4)$，故

$$\|q_M\|_1\le C|M|$$                              (12)

其中 $C$ 为 absolute constant。这个 argument 不产生
$O(|M|/B)$。

#### 证明

在 commutative convolution Banach algebra 中，

$$\|d^{*k}-\nu^{*k}\|_1
\le k|M|R^{k-1}$$                                 (13)

由 telescoping identity 得到。展开

$$d^{*3}*(d-L\delta_0)^{*2}
=d^{*5}-2Ld^{*4}+L^2d^{*3}$$                     (14)

及 $\nu$ 的对应式，对三项应用式 (13)，得到式 (11)。$R\le B+|M|\le2B$
及 $c_2^2\le4/(9B^4)$ 给式 (12)。$\square$

所以即使 $M/B\to0$，只要 $|M|$ 本身不一致有界，absolute perturbation ledger
也不能把 $q_M$ 撤离。经典 PNT 给 relative discrepancy saving，但不自动给
$M=O(1)$；后者在 critical cofinal regime 可能已有接近 RH 的强度。

## 3. Full divided-difference Volterra primitive

把 $M$ 保留在 polynomial 中。定义

$$F_M(z)=(M+z)^3(M-L+z)^2,$$                      (15)

$$R_M(z)=\frac{F_M(z)-F_M(0)}{z}.$$               (16)

$R_M$ 是 degree-four polynomial；文档 192 的 $b_1,\ldots,b_5$ 正是它的
ascending coefficients。

### 定理 AGZ（full centered divided-difference factorization）[U]

在 distributional convolution algebra 中，

$$q(d)
=-c_2^2
\left[
F_M(0)\delta_0
+D\{A*R_M(\nu)\}
\right].$$                                       (17)

当 $M=0$，

$$R_0(z)=z^2(z-L)^2=[z(z-L)]^2,$$                 (18)

所以式 (17) 退化为定理 AGX。对一般 $M$，全部 square-core / mass-correction
cancellation 都保留在单一 object $A*R_M(\nu)$ 中。

#### 证明

functional calculus in the commutative convolution algebra 给

$$F_M(\nu)
=F_M(0)\delta_0+\nu*R_M(\nu).$$                  (19)

而 $\nu=DA$，故

$$\nu*R_M(\nu)=D[A*R_M(\nu)].$$                  (20)

式 (3) 恰为 $-c_2^2F_M(\nu)$，得到式 (17)。式 (18) 直接代入
$M=0$。$\square$

### Cauchy cumulative form

在 smooth even model 中，$A*R_M(\nu)$ 是 odd，因此 nonconstant symmetric
profile 为

$$Q_{q(d)}(h)
=-2c_2^2[A*R_M(\nu)](h),$$                       (21)

相应 direct Cauchy profile capacity 是

$$\mathcal C_C(q(d))
=2c_2^2\int_0^\infty e^{-h}
|A*R_M(\nu)(h)|\,dh,$$                           (22)

另加 formal/numerical exact-atom ledger。式 (22) 是比文档 192 的五项展开更
canonical 的下一算术 target。

## 4. Finite decomposition audit

脚本 scripts/formal_lag_response.py 精确构造：

1. centered symbol $\nu=d-M\delta_0$；
2. balanced-square response $q_{\mathrm{bal}}$；
3. mass correction $q_M=q-q_{\mathrm{bal}}$；
4. full response 的 exact reconstruction；
5. 三部分各自的 Cauchy signed profile。

冻结 models 给：

| $Y,N$ | $B$ | $M/B$ | part | signed response | exact | nonexact | capacity |
|---:|---:|---:|:---|---:|---:|---:|---:|
| $4,7$ | $2.313$ | $-.1892$ | balanced | $.000027$ | $.003431$ | $-.003404$ | $.004481$ |
|  |  |  | mass | $.004915$ | $.02379$ | $-.01887$ | $.01953$ |
|  |  |  | total | $.004942$ | $.02722$ | $-.02228$ | $.02372$ |
| $8,10$ | $3.683$ | $-.08846$ | balanced | $.000986$ | $.01307$ | $-.01209$ | $.01369$ |
|  |  |  | mass | $.003509$ | $.01824$ | $-.01473$ | $.01514$ |
|  |  |  | total | $.004495$ | $.03132$ | $-.02682$ | $.02876$ |
| $12,12$ | $4.552$ | $-.008785$ | balanced | $.004924$ | $.02824$ | $-.02332$ | $.02565$ |
|  |  |  | mass | $.000708$ | $.002426$ | $-.001718$ | $.001795$ |
|  |  |  | total | $.005632$ | $.03067$ | $-.02504$ | $.02743$ |
| $16,15$ | $5.230$ | $.05828$ | balanced | $.01713$ | $.04894$ | $-.03181$ | $.03536$ |
|  |  |  | mass | $-.009176$ | $-.02018$ | $.01100$ | $.01205$ |
|  |  |  | total | $.007958$ | $.02876$ | $-.02080$ | $.02332$ |

关键现象：

- relative mass 的绝对值总体变小，但 mass response 不单调；
- balanced capacity 从 $.00448$ 增至 $.03536$，并未显示单独有界趋势；
- 在 $Y=16$，balanced signed response $.01713$ 与 mass response
  $-.00918$ 发生主阶抵消；
- 分别 majorize 两部分会把 total capacity $.02332$ 放宽到至少
  $.04741$，丢掉约一半预算。

这些仍是 finite floating diagnostics，不是 asymptotic theorem；但它们明确
反驳了“relative $M/B$ 小，所以 $q_M$ 可先绝对处理”的启发。

## 5. 分支停止与晋级

### 停止：isolated balanced square

以下 strategy 不再单独推进：

1. 对 $q_{\mathrm{bal}}$ 用 square/positive-definite arguments；
2. 对 $q_M$ 用 $|M|/B$ perturbation；
3. 最后 triangle inequality 合并。

定理 AGY 只给 $O(|M|)$，finite audit 又显示两部分的 signs 在主阶相消。

### 晋级：full divided-difference primitive

保留式 (22) 的完整

$$G_M=A*R_M(\nu).$$                                (23)

下一目标是直接证明

$$c_2^2\int_0^\infty e^{-h}|G_M(h)|\,dh=O(1)$$    (24)

along a cofinal schedule，连同 exact/Gamma/approximation ledger。若能无循环
证明式 (24)，文档 192 推论 AGW 与 bounded finite-trace Hodge--Weil theorem
给中心线结论。

## 6. 下一最小引理

1. 寻找 $R_M$ 的 polarization identity，使 square core 与 $M$ corrections
   在同一 sesquilinear energy 中出现；
2. 对 $G_M$ 做 Cauchy resolvent convolution，而不是对 coefficients 做
   total variation；
3. 审计 $M$ 的 Euler-open-set information 是否能与 $A$ 的 Volterra boundary
   terms共同抵消，而非单独要求 $M=O(1)$；
4. 检查式 (24) 是否可由 response-specific Type I/II bilinear estimate推出；
5. 若任何 estimate 必须先给 $|M|=O(1)$，立即审计该输入是否已等价于
   center-line zero-free region。

## 7. 审计结论

balanced model 中确有一个 canonical convolution square，但它不能与 mass
correction 分离估计。正确结构是 full divided difference
$A*R_M(\nu)$：它同时包含 square core、constant mode 与三至五阶 shifted
moments 的共同 cancellation。NCE-8 的下一阶段必须直接作用于这个完整
Volterra primitive。
