# 464：辅助数域选择的结论、收益门槛与共轭障碍

2026-10-07。回应用户关于 Q(sqrt(-3)) 及替代代数数域的提问。
本稿整理 [457](457-number-field-choice-and-relative-amplification.md)、
[458](458-gaussian-all-row-large-sieve-comparison.md) 与
[460](460-generic-power-row-obstruction-and-field-choice.md)，并给出两个
有限代数核查：single-shift 模板的最小非平凡 theta 阶数，以及 Gaussian
原始行不能统一从 Dirichlet norm base-change 取得无零前件的明确例子。
没有确认新无零边界。

## 1. 主要判断及原机制

换域可以成为新研究路线，但现有证明不能通过更换判别式直接改善。
当前 Q(sqrt(-3)) 的优势是以下接口同时成立：

- Eisenstein 整数有精确的 primary 生成元与乘法归一化；
- cubic Gauss 信号给 squarefree 系数
  \(\gamma_2(c)^3=\mu(c)\alpha(c)\)；
- cubic theta 的完成反射，在实际 retained \(j=1\) 上把
  \(\chi_6^j\) 送到 \(\chi_6^{-j-2}=\chi_6^3\)；
- 该终端是二次角色，核对导子与互反律后可使用
  \((U+V)(UV)^\varepsilon\) 的二次大筛；
- 特殊 Möbius 全行均方与六次放大 \(u\mapsto ua^6\)，连同
  marked/plain、Euler 留数及延拓，完成整个预算。

固定源为
[adc7f124](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)。
上述具体接口分别见源 568–625、766–835、1789–1793、
2640–2672、7697–7702、12362–12460；完整来源核查见
[数域审查](../reviews/2026-10-07/hybrid-number-field-choice-review.md)。
二次大筛的 family 前件见
[Goldmakher–Louvel Theorem 1.1](https://arxiv.org/html/1112.1642v2)。

固定域的判别式、格密度与有限单位数进入常数；固定有限类群增加
有限 sectors，并要求重新核对原 PID 接口，但不会单独改善理想计数的一次幂。
这里的 \(d=6\) 是角色及放大阶数，不是数域次数，也不是除以六个单位。
若域随主参数变化，判别式和类群费用不再是可随意吸收的固定常数。

## 2. 为什么同一模板偏好 cubic/sextic

限定为 [457] 的模板：row 角色阶 \(d=2m\)，retained \(j=1\)，
普通反射 \(j\mapsto-j-\rho\)，而 shift 来自 theta Gauss 角色
\(\chi^\rho\)。要求终端为二次角色的充要同余是

\[
 \rho\equiv m-1\pmod{2m}.
\]

该 theta 角色的阶数遂为

\[
 n_\theta=\frac{2m}{\gcd(2m,m-1)}
 =\begin{cases}m,&m\text{ 奇},\\2m,&m\text{ 偶}.\end{cases}
\]

因为 \(\gcd(2m,m-1)=\gcd(2,m-1)\)，这个公式不靠有限枚举。
在非平凡情形 \(m\ge2\) 中，最小 \(n_\theta\) 是 3，且只在
\(m=3,d=6\) 达到；\(d=4\) 对应 \(n_\theta=4\)。
所以减少 row 阶数并不自动减少需要完成的 theta 阶数。
\(d=2,\rho=0\) 对应平凡 theta 角色，须另造 signal，不能沿用本模板。
本结论不排除改变 retained row 或设计其他反射。

若使用要求 \(\mu_d\subset K\) 的 Kummer/Hecke-family 构造，则
\(\mathbf Q(\zeta_d)\subset K\)，从而 \([K:\mathbf Q]\ge\varphi(d)\)。
在虚二次域内，保留 \(\mu_6\) 的选择唯一是 Q(sqrt(-3))；
Q(i) 可以容纳 \(\mu_4\)，其他虚二次域只有 \(\mu_2\)。
这不否认其他域上存在高阶有限角色；它限制的是这里指定的构造。

## 3. Q(i) 的真实机会与量化门槛

Gaussian 候选已有真实 squarefree 信号
\(\gamma_1(c)^2=\mu(c)\alpha(c)\)，split/inert 及 CRT 的完整处理见 [457]。
需要采用
[David–Dunn–Hamieh–Lin v5](https://arxiv.org/html/2306.11875v5)
的补充因子及约定。其 quartic theta 的 prime core coefficient 公式
仍不完整（该文 §4.5）；平方 Gauss 身份不能免费供应线性 theta 完成反射。

只有先证明同一特殊 Möbius raw 合同、全部自然零掩码及 profile/height
一致性，order-\(d\) 放大才给
\[
 e_d(r)=\max\{1,[1+(d-1)r]/d\},\qquad D=U^r.
\]
按当前 [451](451-kappa-feedback-cubic-boundary-and-family-continuation.md)
的参考临界点
\[
 t_*=\frac{1+3e_*}{8e_*}=1.124227146786\ldots,
\]
理想四次路线的单个未标记逆列均方收益为
\[
 e_6(t_*)-e_4(t_*)=(t_*-1)/12
 =0.010352262232\ldots .
\]
理想二次路线相应为 \((t_*-1)/3=0.041409048929\ldots\)。
这些都是 \(U\) 的均方指数差，不是 \(\sigma\) 的改善幅度。

即使假定原 short detector 合同全部保留，在旧 cutoff \(t_*\)
只改善 long 分支也不会降低整体 count：short 仍为 \(2/3\)。
允许合法重选 cutoff 后的反事实四次 count 收益仅为
\(0.002993619562\ldots\)。推导与全部额外前件见
[定量审查 §4](../reviews/2026-10-07/hybrid-number-field-quantitative-review-radial.md)。
实际 \(\kappa\) 必须使用 \(2\beta_*-1\)，还需重证全参数范围；
这些数值不能注册为 Gaussian 边界。

相比之下，已付 Gaussian 全行估计是
\[
 \sum_{Nu\le U}\sup_{D'\le D}|M_u(D')|^2
 \ll\{U+(UD)^{2/3}+D U^{1/3}\}(UD)^\varepsilon.
\]
其中 \(M_u\) 是 [458] 的同一固定 Möbius 逆列。
在 \(D=U^{t_*}\) 时，本上界指数为
\(t_*+1/3=1.457560480119\ldots\)，高于原六次合同的
\(1.103522622322\ldots\)。差约 \(0.354037857798\)，远大于理想四次
放大的 \(0.01035\) 收益。因此现有通用大筛预算不能认证换域改进；
这不是对特殊 Möbius cancellation 的不可能性证明。
squarefree 高阶大筛来源为
[Blomer–Goldmakher–Louvel Theorem 1.3](https://arxiv.org/html/1112.1650v1)。

## 4. 不能把已有 Dirichlet 条带免费覆盖整个 Gaussian 行族

对任意固定虚二次域 \(K\)，正确处理有限 Euler 因子后，
\[
 L_K(s,\chi\circ N)=L(s,\chi)L(s,\chi\chi_{D_K}).
\]
因此新的全 Hecke 族无零结果可以转给 Dirichlet；反方向仅覆盖
norm base-change 子族，不会自动覆盖所有原始行。

下面直接展示 [458] 的实际 quartic 行，在 \(\eta=1\) 时就可能不是该子族。
在 Z[i] 中取 primary 元素
\[
 \pi=-1+2i,\quad \nu=3+2i,\quad\bar\nu=3-2i;
 \qquad N\pi=5,\quad N\nu=N\bar\nu=13.
\]
它们互素且都是奇 primary，所有自然零掩码在这里确实为 1。
按 \((a/b)_4\equiv a^{(Nb-1)/4}\pmod b\) 的约定：

- 模 \(\nu\)，\(i\equiv5\pmod{13}\)，故
  \(\pi\equiv9,\ \pi^3\equiv1\)，得到 \((\pi/\nu)_4=1\)；
- 模 \(\bar\nu\)，\(i\equiv8\pmod{13}\)，故
  \(\pi\equiv2,\ \pi^3\equiv8=i\)，得到 \((\pi/\bar\nu)_4=i\)。

于是同一真实 row \(\psi_\pi(n)=(\pi/n)_4\) 在两个相同范数的
理想上取不同值；共轭符号 convention 的两值相应为 \(1,-i\)，
结论一样。任何 \(\chi\circ N\) 必在这两个理想上取相同值，
所以该 row 不是 norm base-change。有限 ray-sector 分拆不会把这个
全局 Hecke 角色变成 norm base-change，也不能据此取得其普通 L 的无零前件。
从导子角度，单支 split-prime 导子的奇部不共轭不变，亦给同一障碍。

已付
[第四幂 Möbius 子族估计](../reviews/2026-10-07/hybrid-field-change-special-mobius-next-research.md)
仍有效：\(u=r^4\) 的剩余 quartic twist 消失但掩码保留。
它只控制该子族与满足明列 reciprocal 前件的固定目标；
不能由此推出上述随行变化的 quartic primitive 族的全行均方。

## 5. 其他数域与下一研究目标

| 选择 | 可能收益 | 必须解决的主要问题 |
|---|---|---|
| Q(i) 的新 quartic 探针 | 条件四次放大更有效 | 同一完成反射、二次终端、Euler 信号，以及特殊 Möbius 近线性全行均方 |
| 其他虚二次域 | 可尝试完全不同的 quadratic 或高阶设计 | 不能保留原 cubic/sextic 数据；类群与新的 signal 需要处理 |
| 实二次域 | 可使用二次角色家族 | 无限单位、实无穷位及新 theta/kernel；没有现成更强边界接口 |
| 高次 CM 域 | 可容纳更多根单位 | 单位商、多个无穷位与高度预算；保留 \(d=6\) 本身没有放大收益 |

固定 degree-\(2r\) CM 域的 ordinary completion 含 \(\Gamma(s)^r\)，
导子范数在普通函数方程中的指数仍是 \(1/2-s\)，不会因次数增加而
获得额外导子节省。单位 rank 为 \(r-1\)，原样按所有 norm-bounded
elements 求和会包含无限多个单位，必须改为理想或有控制的单位商。
这些属于额外待证接口，并不是所有高次域方案不可能的结论。

最窄的继续研究目标是：在同一 Gaussian 探针、固定目标与原有高度下，
证明变化的 quartic primitive 行及全部自然掩码满足
\[
 \sum_{Nu\le H}\sup_{0<D'\le D}|M_u(D')|^2
 \ll_{c,\varepsilon}H(HD)^\varepsilon,\qquad H\ge D^{1+c},
 \quad\text{每个固定 }c>0.
\]
须利用特殊 Möbius 系数：[460] 已证明任意列系数的全行矩阵不可能
在这个全部近临界范围具有同一线性宽度。再完成 reflection、
marked/plain 和全族延拓，才能比较新的最终 \(\sigma\)。

仓库当前边界仍是原明列引用输入 [R] 下的
\(\sigma_*=0.874957019420098946\ldots\)；本稿不触发新边界论文。
