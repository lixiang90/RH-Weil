# 原 Type II 短 Λ 与疏因子四矩付款：独立全文审查

2026-10-08。审查人：twisted_research。结论：**限定 PASS**。
独立实读作者完整524行；回核冻结 Vaughan、scalar/proper-power及476输入，浏览作者所用的原始经典引理，并逐项重建实际 cutoff 与剩余账本。未修改作者源、旧稿、脚本、输出、math 或 Git。

## 1. 最终源绑定和实际批准范围

canonical UTF-8 LF 只统一 CRLF 与孤立 CR；不 trim，不改变 EOF。

| 文件 | canonical LF SHA256 | 字节 / 行 |
|---|---|---:|
| [本次完整被审来源](hybrid-original-type-ii-short-lambda-factor-fourth-research-radial.md) | b39876e0b9d91a06de57d1069cf6adac676252bd1fe737186bb065716015abb0 | 21261 / 524 |
| [冻结 Vaughan 实际系数与旧付款](hybrid-original-vaughan-type-i-and-type-ii-reduction-research-radial.md) | cf58086aeb9eee63832ccd06f5499110ea236b4bd94396893757b62e75bdb9d4 | 12260 / 324 |
| [其冻结独审](hybrid-original-vaughan-type-i-and-type-ii-reduction-review-twisted.md) | 576a0841b5a5ad9bf8fbda74561bb83ca3d16654a0c2faac5f4aa80269fb296f | 9160 / 174 |
| [原 scalar 与 proper-power 准入](hybrid-short-carrier-canonical-scalar-fourth-admission-research-radial.md) | f04279a9de54303d772859b2ee5e05010567404c53143c928a14e905eb51a0d7 | 14699 / 370 |
| [476原五分之七增长结果](../../notes/476-original-fourth-growth-five-sevenths-with-ivic-density.md) | 179829dd25f92ff187359f73455aafad9f957d714df13cf871db47a76e9408b6 | 4448 / 96 |

批准的是同一个冻结 \(U=V=\lfloor X^{1/8}\rfloor,\ Y=X^{5/6}\) 的实际 \(C_4\) 内三个完整子族的上界，以及原 Type I 的强化。它们不是整个 \(C_4\) 的新增长指数，也不是原 finite matrix 的常数级四矩或新零点比例。

## 2. 经典输入与真实 Weyl 前件

本次浏览 [Montgomery–Vaughan 作者书 Volume II](https://personal.science.psu.edu/rcv4/Vol2/Vol2.pdf) 的 Theorem16.7、Lemma16.8及其填零差分证明（印刷第8、11页）。另核该书 Theorem16.16证明的式(16.24)，其中相同对数和的三长度分支已经明确出现。作者的新付款使用这一经典基础；不把 generic Weyl 界本身认作新定理。

以下逐项核查作者自己的实际实例，保持 \(t\in[T/4,4T]\)：

- \(R\le T^{1/3}\) 时项数 \(O(R)\) 被 \(T^{1/6}\sqrt R\) 覆盖，包括有界 \(R\)。
- \(R\ge T^{2/3}\)、\(R\le CT\) 时，\(f(x)=t\log x/(2\pi)\) 的负二阶导数在整个dyad满足统一的 \(T/R^2\) 上下界。取共轭可用原正导数版本，得到 \(\sqrt T+R/\sqrt T\)，两项均不超过固定倍 \(T^{1/6}\sqrt R\)。
- 中段对任意sharp子区间填零到长度 \(N\asymp R\) 的完整数组，差分引理没有遗漏短区间的边界。差分交集仍是整数区间，且
  \[
  f_h''(x)=\frac{th(2x+h)}{2\pi x^2(x+h)^2}
  \asymp hT/R^3>0
  \]
  只在 \(x,x+h\in[R,2R]\) 使用；第二导数测试的上下常数与当前端点无关。

差分代入后，三个实际费用为
\[
\frac{R^2}{H},\qquad \sqrt{TRH},\qquad
\frac{R^{5/2}}{\sqrt{TH}}.
\]
取 \(H=\max(1,\lfloor R/T^{1/3}\rfloor)\) 后，前两项均为 \(O(RT^{1/3})\)，第三项为 \(O(R^2/T^{1/3})\)，在 \(R\le T^{2/3}\) 可吸收。\(H=1\) 时差分和为空，仍是有效的同级上界。填零长度可取完整dyad长度，保证 \(H\le N\)。

所以式(4)对所有真实partial endpoints、全部 \(1\le R\le CT\) 统一。没有调用整数 \(m\) 方向的退化二阶导数，也没有把 Type II 乘积相位当作非退化的二维和。

## 3. 临界权、斜 product cutoff 与短 m 的实际二矩

\(r^{-1/2}(\log r)^j\)、\(j=0,1\) 的sup和总变差在dyad均被
\(R^{-1/2}(\log(2R))^j\) 控制。对全部partial端点作 Abel 求和，再切一般区间为 \(O(\log X)\) 个dyads，得到作者式(8)–(9)。实际 \(r\) 长度至多 \(X\asymp T\)，在已经证明的域内。

令 \(M_0=\lfloor X^{1/4}\rfloor\)。原 \(Y<mk\) 与 \(m\le M_0\) 给
\(k>Y/M_0>V\)，因此短 m 子族中的 \(k>V\) 的确是冗余条件；它不是被改变成另一个函数。展开原有限 \(b_V(k)\) 后，精确得到原
\[
\sum_{U<m\le M_0}\frac{\Lambda(m)m^{it}}{\sqrt m}
\sum_{d\le V}\frac{\mu(d)d^{it}}{\sqrt d}
\sum_{Y/(md)<r\le X/(md)}\frac{r^{it}}{\sqrt r}.
\]
每个moving inner区间都保留共同两端，没有矩形替换。其最小下端至少 \(X^{11/24}\)，上端至多 \(X\)。所有重排都是有限和。

外层绝对费用可由初等上界支付：
\(\sum_{m\le M_0}\Lambda(m)/\sqrt m\ll\sqrt{M_0}\log(2M_0)\)、
\(\sum_{d\le V}|\mu(d)|/\sqrt d\ll\sqrt V\)。
故sup指数准确是
\[
\frac16+\frac{1/4+1/8}{2}=\frac{17}{48}.
\]
原normalizer及日志可放入最终任意固定正 \(\varepsilon\)。

实际 n 系数在保留原负号、\(\Lambda(m)\) 和 \(b_V(n/m)\) 后，模至多
\(\tau_3(n)/\sqrt n\)。这是实际 divisor Cauchy；没有用任意 \(\mu(n)\) 代替它。作者式(14)由直接展开时间二矩和 harmonic sum 给
\[
\|F\|_{2,T}^2\ll
\left(1+\frac{Z\log(2Z)}T\right)\sum|\alpha_n|^2,
\]
对原正高度起点统一。在 \(Z=X,\ T=2\pi X\) 时只增加日志；固定 divisor 损失先在最终 \(\varepsilon\) 中分配。因此真实子族二矩为 \(X^\varepsilon\)，不是额外假设。

与sup平方合并，短 m 的四矩为 \(X^{17/24+\varepsilon}\)；
\(5/7-17/24=1/168\) 精确。只有在随后固定 \(\varepsilon<1/168\) 时才可称显示指数严格低于5/7，作者已保留这个限制。

## 4. 同一原 Type I 的 7/12 及参数前沿

冻结 \(I_2\) 的实际outer长度 \(UV=X^{1/4+o(1)}\) 及其 \(g_{U,V}\) 系数没有变化；\(I_3\) 的长度为 \(V\)。原inner两端 \(Y/d<r\le X/d\) 用上述 \(j=0,1\) 的sharp版本覆盖，sup的主要指数是
\[
\frac16+\frac18=\frac7{24}.
\]
原系数的二矩重新经式(14)支付，故 Type I 四矩为 \(X^{7/12+\varepsilon}\)。\(I_3\) 单独的 \(11/48\) sup指数更小，不增加此上界。没有用未声明的原 Type I 混合正交。

冻结 lower block 的四矩仍是 \(X^{2/3+\varepsilon}\)，因此原 \(P_H-C_4\) 的整体范数费用仍为 \(X^{1/6+\varepsilon}\)。7/12不自动变成整个误差费用。

一般固定参数的短 m 成本
\(1/3+a+b\)、合法斜掩码前件 \(a+b<y<1\)，以及
\(a+b<8/21\) 的严格低于5/7条件均正确。
冻结 \(a=1/8\) 对应 \(b<43/168\)，而当前 \(b=1/4\) 留下1/168。另选 \(a=1/16,b=5/16,y=3/4\) 虽同样有17/24，却同时改变原 \(b_V\) 和下截断；作者未将该不同对象的费用免费迁移到冻结余项。

## 5. 最大 prefix 四矩：真实长度与全部 moving endpoints

作者§8的系数 \(q(n)\) 是对当前 \(X,V\) 固定的实际有限数组，统一满足固定 divisor 次幂上界。它不随当前高度 \(t\) 改变。在dyad \((A,2A]\) 的二进制数组中，第j层block的系数能量为
\(O(X^{2\delta}2^{-j})\)。

平方多项式的系数能量严格满足
\[
\sum_v\left|\sum_{n_1n_2=v}a_{n_1}a_{n_2}\right|^2
\le \max_{v\le4A^2}\tau(v)
       \left(\sum|a_n|^2\right)^2.
\]
对平方应用弱二矩，**实际长度是 \(4A^2\)**，因此留下
\(1+A^2/X\)，没有把长度缩为A或使用ζ的未知四矩。
同层 \(2^j\) 个blocks求和后费用为
\(X^\varepsilon(1+A^2/X)2^{-j}\)。
每prefix至多选每层一个block；取所有blocks的第四次幂和上界，再在L4中Minkowski，利用
\(\sum_j2^{-j/4}<\infty\)。这证明式(22)，没有遗漏最大partial prefix的增长费用。

任意sharp区间是两个prefix之差，逐t由同一最大prefix控制。原 \(Y<mk\le X\) 随外因子移动的两个端点因而都保留。固定prime mask可放入实际 \(q(n)\) 并填零；不能从一个signed全函数的范数直接删去任意标签。

## 6. Squarefull-k 的自然零域与全子族付款

Squarefull的定义是每个prime valuation至少2，故
\(\operatorname{rad}(k)^2\mid k\)。当 \(1<k\le V^2\) 时，所有非零 \(\mu(d)\) 的除数都在 \(d\le V\)，于是
\[
b_V(k)=\sum_{d\mid\operatorname{rad}(k)}\mu(d)=0.
\]
原 \(k>V\ge2\) 已排除1。自然零域使用真实原截断，未加新mask。

表示 \(k=a^2b^3\)、b squarefree，按偶/奇valuation唯一；由此 dyadic squarefull 项数为 \(O(\sqrt K)\)。与统一 \(|b_V(k)|\le\tau(k)\) 合并，每个外k dyad的绝对权
\(\sum_{\rm squarefull}|b_V(k)|/\sqrt k\ll X^\delta\)。

固定k后的 m 区间严格是
\((\max(M,m_0,Y/k),\min(2M,X/k)]\)，两个真实Λ-prefix的差。非空块满足 \(MK<X\)，且 k 的dyads可以从 \(V^2\) 开始，所以 \(M<X/V^2\)。最大prefix引理给每块 \(1+M^2/X\)；全部 \(O(\log^2X)\) 个块通过L4 Minkowski和预分配 \(\varepsilon\)，产生
\[
X^\varepsilon(1+X/V^4)=X^{1/2+\varepsilon}.
\]
这覆盖整个 squarefull-k 子族，也覆盖ledger中 \(m>M_0\) 为 genuine prime 的子族：后者以实际 \(q(m)=\Lambda(m)1_{\rm prime}\) 重新使用prefix引理，未作非法signed范数删mask。

## 7. Large m proper prime powers 与不重叠账本

在每个 \(m\asymp M\) dyad，平方base的整数项数至多 \(O(\sqrt M)\)，更高powers的base项数至多 \(O(M^{1/3}\log M)\)。与真实 \(\Lambda(p^j)=\log p\) 和临界权合并，外proper-power绝对权为 \(O(\log^2X)\)。没有丢掉高powers，也没有以n整体proper-power替代内部m标签。

固定m的 k 区间
\((\max(K,V,Y/m),\min(2K,X/m)]\)
用实际 \(q=b_V\) 的最大prefix；所有非空 \(m>M_0\) 块给 \(K<X/M_0\)。因而四矩上界为
\[
X^\varepsilon(1+X/M_0^2)=X^{1/2+\varepsilon},
\]
保留全部k，不调用短μ的FE、点值界或随机性。

最终partition依次为：全部short m；large proper-power m 的全部k；large genuine-prime m 的 squarefull-k；large genuine-prime m 的 non-squarefull-k。它们互不交且覆盖原非零Λ系数，原负号、normalizer和共同 \(Y<mk\le X\) 全部一致。

三已付项先合成一个真实误差函数，L4范数至多
\(X^{17/96+\varepsilon}\)。再加原 lower/Type I/proper-power 迁移，仍同级，因为 \(1/6<17/96\)、\(1/8<17/96\)。
只在最后一次使用 \((u+v)^4\le8(u^4+v^4)\)，得到源式(29)两向coupling；没有把各阶段常数8错误相乘后写作8，也没有把第四矩当作additive相差小量。

## 8. 本次实际有限复算及范围

除完整数学审查，另在内存执行 Fraction 指数检查：17/48、17/24、1/168、7/24、7/12、11/24、43/168以及改变固定参数的17/24均准确。
对 \(2\le V\le16\) 的185个 squarefull 例子独立检查自然零 \(b_V(k)=0\)。
用三组整数 \((U,V,M,Y,X)\)：
\((3,3,6,40,160)\)、\((2,4,7,50,200)\)、\((4,5,9,60,250)\)，
以 \(\log p\) 作形式标签分别枚举123、186、171个 n/prime-label系数。原完整C4、四项partition和短m的divisor展开逐系数一致。

这些有限检查只认证所列整数系数模型和有理指数，没有认证渐近 Weyl、最大prefix或原解析准入；后者来自前面的完整证明审查。本次没有生成或修改数值证书文件。

**实际结论：** 作者已支付三个完整的原 \(C_4\) 子族并强化原 Type I，余项精确收缩为 genuine-prime \(m>M_0\)、non-squarefull \(k>V\) 的完整共同cutoff函数。其balanced prime×prime及全部剩余 μ-divisor相消仍未付。原whole五分之七增长结果没有被本稿改成17/24，常数级四矩、实际新比例和无零边界均不能由这些子族上界推出。
