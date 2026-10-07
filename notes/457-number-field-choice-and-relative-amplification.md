# 457：辅助数域、反射角色阶数与换域的条件收益

2026-10-07。针对用户关于改用其他代数数域能否扩大无零区域的提问。
状态：来源依赖审查与相对放大引理；尚无新域的无零区域定理。

结论：当前方法中，Q(sqrt(-3)) 的主要作用是使 cubic theta 与 sextic
角色反射兼容，并把关键残余角色降为 quadratic。判别式、格密度和有限
单位数影响固定常数；真正影响指数的是角色、Gauss 信号、theta 完成和
矩估计的组合。Q(i) 是值得检验的候选，但四次放大的条件收益尚不能
抵偿或消除新反射接口的缺失。现有 strict sigma*≈0.874957019420099
仍仅在既有论文明列的引用输入 [R] 范围内成立，本轮没有改变该范围。

## 1. 来源与结论层级

原论文固定在
[OpenAI 源 adc7f124](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)。
只读本地 source 的 canonical LF SHA256 为
`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`。
以下行号按该版本，普通 Hecke 函数方程与 cubic theta 的函数方程分开。

完整数域依赖清单见
[逐接口审查](../reviews/2026-10-07/hybrid-number-field-choice-review.md)。
本笔记增加一个带完整前件的 order-d 放大推导、反射阶数检验、可替代的
quartic Jacobi signal 候选和同尺度的大筛费用比较。任何“候选”均未登记
成新的 completed reflection、marked/plain moment 或无零边界。

## 2. 为什么 −3 的选择影响很大

O=Z[omega] 是二维格和 PID，有唯一的 primary generator（理想与3互素时
取 a≡1 mod3），其范数是 |a|²。固定虚二次域的理想数均按 H 的一次幂
增长；改判别式、covolume、有限单位和有限 class sectors 不会把这个幂
变小。源中的放大系数 1/6 来自 a^6，不是把六个单位除掉。

虚二次域中，含 primitive cubic root 的域只能是 Q(sqrt(-3))，因为该根
的最小多项式次数已经是2。于是不存在另一个虚二次域，可以保留同一套
mu6、cubic residue、cubic theta 数据，只更换判别式。Q(i) 有 mu4；其余
虚二次域的根单位仅有±1。固定域的有限 class sectors 可处理，但类数
大于一会增加非平凡 conductor-one characters，源的 PID 证明不能照搬。

源766–835以 cubic Jacobi sum 的 primary 单位归一化证明

\[
 \gamma_2(p)^3=-\alpha(p),\qquad
 \gamma_1(p)\gamma_2(p)
 =\overline{\chi_p(4)}\gamma_3(p)\gamma_2(p)^3,
 \quad \alpha(p)=p/\sqrt{Np}.
 \tag{1}
\]

这不是一般虚二次域的 Gauss 恒等式。其 squarefree 乘积产生后续
Möbius/prime phase，局部 Euler quotient 才读出目标 L 函数的倒数。

更关键的是 source1789–1793 的 completed reflection：普通分支的局部
因子为 chi_p(x)^(-j-2)。实际 retained squarefree residual row 的 j=1
（source7697–7702），反射后 chi6^(-3)=chi6^3 恰是二次角色。满足
Hecke-family 前件后，可用
[Goldmakher–Louvel 的 Theorem 1.1](https://arxiv.org/html/1112.1642v2)
给出的 (U+V)(UV)^epsilon，而非一般高阶族的额外 (UV)^(2/3) 费用。
源2640–2672还实际核对导子、互反律和同 sector primitive product。

## 3. 直接换成 Q(i) 的失败与可检验的新设计

保留旧的 chi² 和 +2 shift、只把 sextic 改成 quartic，有两个明确失败：

1. chi4² 是 quadratic；其归一化 Gauss sum g2 满足 g2²=chi4²(-1)=1。
   因而 g2³ 是±1，不能等于 generic Gaussian prime 的 -alpha(p)。例如
   norm17 的 primary prime 1+4i，其 alpha 不是实数。旧(1)不成立。
2. retained j=1 反射后 chi4^(-3)=chi4，仍是四次角色。旧二次终端大筛
   无法调用。

但这只排除了该直接替换，不排除不同的 quartic Gauss 设计。对有限域
大小 q、order4 角色 chi，记归一化 g_j=tau(chi^j)/sqrt(q)。Gauss–Jacobi
恒等式直接给

\[
 \frac{g_1^2}{g_2}=\frac{J(\chi,\chi)}{\sqrt q},
 \qquad J(\chi,\chi)\in\mathbf Z[i],\quad
 |J(\chi,\chi)|^2=q.
 \tag{2}
\]

因 chi、chi² 非平凡，g2非零。对 norm 为 rational prime 的 Gaussian
prime，J 是该素数之上一支 prime generator 乘单位；究竟对应哪一支及
哪个 primary 单位，必须用所选 residue orientation 和 supplementary
law 固定，不能从范数等式独自决定。好 inert prime 的局部分支也须另核。
所以(2)提供候选 prime phase，但没有提供已完成的 Euler reciprocal。
特别是 g1 的平方和 g2 的除法会改变原来线性的 theta-coefficient sum；
必须证明新完成，而不能宣称旧 reflection 自动给出该乘积。

一般地，保留 retained j=1，设新反射在普通分支为 j -> -j-rho，order
d=2m 角色的二次幂是 chi^m。降为该二次幂的必要且充分同余是

\[
 -1-\rho\equiv m\pmod {2m},\qquad
 \rho\equiv m-1\pmod {2m}.
 \tag{3}
\]

若 shift 仍来自局部 theta Gauss 角色 chi^rho，其角色阶数为

\[
 n_\theta=\frac{2m}{\gcd(2m,m-1)}
 =\begin{cases}m,&m\text{ 奇},\\2m,&m\text{ 偶}.\end{cases}
 \tag{4}
\]

| row 角色阶 d | 需要的 shift rho | chi^rho 的阶 | 已有当前 completed 数据 |
|---|---:|---:|---|
| 2 | 0 | 1 | 无旧非平凡 theta signal |
| 4 | 1 | 4 | 需要新的 quartic 完成与局部表 |
| 6 | 2 | 3 | 原 cubic theta / sextic 配对 |
| 8 | 3 | 8 | 需要新的 octic 数据与域 |
| 10 | 4 | 5 | 需要新的 quintic 数据与域 |

因此 row 阶数 6→4 并不使这个设计中的 theta 角色阶数变小：cubic 会变
为 quartic。(3)–(4)仅适用于所述 j=1 / single-shift 模板；重设 probe、
改变 retained j 或做不同反射可能另有设计，没有在此被排除。

具体 Gaussian 输入已经存在，不能只把它称为抽象设想。需使用
[David–Dunn–Hamieh–Lin v5](https://arxiv.org/html/2306.11875v5) 的 (3.9)–(3.11)，
而非遗漏 supplement 的旧 v3。(3.11)在其 additive/residue convention 下
对 degree-one primary prime pi 给出未归一化 Gauss 关系

\[
 g_4(\pi)^2=-\epsilon_\pi\kappa_\pi\sqrt q\,\pi,
 \quad g_2(\pi)=\epsilon_\pi\sqrt q,
 \quad\epsilon_\pi=\left(\frac{-1}{\pi}\right)_4,
 \quad\kappa_\pi=\left(\frac{\bar\pi}{\pi}\right)_4^{-2}.
 \tag{2a}
\]

这里 kappa_pi∈{±1}，不能把它无条件删除。对 degree-one pi=a+bi，
q=p=a²+b² 是 rational prime，a奇、b偶、gcd(a,b)=1。因 bar(pi)≡2a mod pi，
kappa_pi=(2a/p)_2。p≡1 mod4 使二次互反律给
(a/p)_2=(p/|a|)_Jacobi=(b²/|a|)_Jacobi=1；a=±1 单列显然，负a亦无
(-1/p)损失。因此 kappa_pi=(2/p)_2=(-1)^((p−1)/4)=epsilon_pi。得到

\[
 \gamma_1(\pi)^2=-\alpha(\pi),\qquad
 \frac{\gamma_1(\pi)^2}{\gamma_2(\pi)}
 =-\epsilon_\pi\alpha(\pi).
 \tag{2b}
\]

例如 norm5 的 pi=−1+2i，精确 J(chi,chi)=pi；norm17 的 pi=1+4i，
J=−pi。旧版统一 J=−pi 的读法已经被这个有限反例排除，v5的
supplement与两例均一致；(2b)的平方信号则一致成立。

对 degree-two good prime，pi=−p、p≡3 mod4，alpha(pi)=−1。其残余域是
F_(p²)，quartic chi 的 Frobenius 变换 chi(x^p)=bar(chi(x))，而 DDHL
的 additive character 是该残余域 trace character，在 Frobenius 下
不变。故 tau(chi)=tau(bar chi)，chi(-1)=1，又
tau(chi)tau(bar chi)=p²，得到 gamma1(pi)²=1=−alpha(pi)。这里只需平方，
不能沿用旧v3的 gamma1(pi)=1；例如 pi=−3 的 Gauss 符号为−1。

最后，DDHL (3.5)–(3.6) 的 coprime primary CRT multiplier 属于±1
（quartic 互反后是 quadratic residue 乘固定 reciprocity sign）。它的
平方为1，primary generators的alpha乘法精确。因此所有odd primary
squarefree c 有真正的 squarefree signal

\[
 \gamma_1(c)^2=\mu(c)\alpha(c).
 \tag{2c}
\]

(2c)保留2处mask，覆盖split与inert primes，不涉及任意 incoming
quartic row 的反射。它不是新的无零定理，也尚未产生原 whole completed
probe 的 Euler quotient；但比只说 quartic signal 可能存在更具体。

该文 §4.5 的 quartic theta 有24个 cusp 和 K_(1/4) 展开；Suzuki 的
(4.37)–(4.39) 给出 fourth-power periodicity、cube vanishing 以及 coprime
square coefficient 的精确关系。但 exponent-one core coefficients 尚无
与 cubic 相当的完整已证公式：该文 §4.5 末尾讨论仍开放的 Patterson
quartic coefficient conjecture。Lemma9.2 的实际 Voronoi formula 的
Gauss numerator 含 (alpha/m)²；当 (c,alpha/m)=1 时，通过(3.4)产生
quadratic twist ((alpha/m)/c)_4²（并保留坏素数及 nonunit 分支）。
这是特定 square-numerator 系列的已证接口；不等于所有 incoming
quartic j 的 uniform j→−j−1 completed reflection。此区别正是候选的
可用起点与当前 missing theorem 之间的界线。

## 4. 相对 order-d 放大引理及证明

固定数域 K、固定有限坏素数集、固定 d≥2，所有 ideals 及 divisor 在
该集合外。对 d-free rows u，设 zero-extended order-d 角色满足

\[
 \psi_{u a^d}(n)=\psi_u(n)1_{(n,a)=1}.
 \tag{5}
\]

定义真正未加 marks 的逆列

\[
 M_u(D;W)=\sum_{n\ {\rm sf}}\mu(n)\psi_u(n)(Nn)^{-1/2}W(Nn/D).
 \tag{6}
\]

假定以下接口已经独立证明：

- raw row-scale supremum：对每个固定 c>0，H≥max(2,D^(1+c)) 时，对所需全部 tests,
  sum_(Nv≤CH) sup_(0<D'≤D)|M_v(D';W)|² ≪ H(HD)^epsilon，带所需的
  profile/height/parameter uniformity；不能仅用 fixed-scale moment。
- 对 Na≤P 有≫P个可用 multiplier ideals；所选 row representatives
  使 (u,a)->u a^d injective，且 N(u a^d)=Nu(Na)^d。
- (5)、全部自然 zero masks、平方自由 divisor 分解和同一 W 的缩放
  都与该 raw family 兼容。若 rows 是 elements，单位与 class 问题
  必须先处理；不能把 ideal injectivity 当成未经处理的 element statement。

令 Nu≈U，H=max(2U,D^(1+c))，P=(H/U)^(1/d)。对每个 a，精确分解
n=bm，b|rad(a)、(m,a)=1，得到

\[
 M_u(D;W)=\sum_{b\mid\operatorname{rad}(a)}
 \mu(b)\psi_u(b)(Nb)^{-1/2}M_{u a^d}(D/Nb;W).
 \tag{7}
\]

即使 (u,a)≠1，(7)仍成立：同一 nonunit 的自然零在两边保留。所用
divisor 的系数绝对值和 ≤tau_K(a)≪P^epsilon。因此

\[
 |M_u(D;W)|^2\ll P^\epsilon
 \sup_{D'\le D}|M_{u a^d}(D';W)|^2.
 \tag{8}
\]

平均 a 再求和 u，injectivity 使每个 v=u a^d 只计一次，Nv≪UP^d=H。
raw supremum 遂给

\[
 \sum_{Nu\asymp U}|M_u(D;W)|^2
 \ll\frac HP(UD)^\epsilon
 =U^{1/d}H^{1-1/d}(UD)^\epsilon.
 \tag{9}
\]

上述 epsilon 可任意缩小；令 D=U^r、r 位于固定有界非负区间，先对给定
最终 epsilon 选足够小的 c>0，得相对指数

\[
 e_d(r)=\max\{1,[1+(d-1)r]/d\}.
 \tag{10}
\]

这是一般条件引理。d=6 对应 source12362–12460 的实际 unmarked inverse
amplification；d=4、2 的 raw 前件和 completed source 未由本引理证明。

若 r>1，相同前件下 e6−e4=(r−1)/12，e6−e2=(r−1)/3；r≤1 均为1，
该步没有改进。以既有 critical scale ell≈1.1242271468 举例：

| d | 条件 e_d(ell) | 相对 d=6 的指数减少 |
|---|---:|---:|
| 6 | 1.1035226223 | 0 |
| 4 | 1.0931703601 | 0.0103522622 |
| 2 | 1.0621135734 | 0.0414090489 |

这些数字是一个 U-均方界的指数；绝非 sigma 边界减少了对应小数。
mark 的 moving row、两次正列、prime slots 及 height 合同没有包含在(6)。

## 5. 较低放大次数为何还不能保证更好无零域

若 Gaussian 直接替换留下 quartic 终端，只调用
[Blomer–Goldmakher–Louvel Theorem 1.3](https://arxiv.org/html/1112.1650v1)，
可用宽度是 U+V+(UV)^(2/3)。在均衡 U=V=R 时，一般高阶界为 R^(4/3)，
二次界为 R，单个 squared norm 的费用多 R^(1/3)（取平方根后是 R^(1/6)）。
这说明不能忽略丢失二次终端；该均衡例子的费用大于上述 critical
unmarked amplification 的约0.01035指数收益。不同实际尺度须重新计算，
此比较不声称已经完成新 proof 的总预算或得到了不可能性定理。

现有 marked 条件 r+2z≤m−c1、2r+8z≤3m−c2，plain 条件
n1+n2+6 kappa z≤M，以及 reciprocal pole、low contour、principal
cancellation 和 family continuation 都来自整套源。不存在已证的
“把6 kappa改成4 kappa”的推广。只有新 reflection、local Euler quotient
与 marked/plain recursion 都付清后，才能重新优化最终 sigma。

## 6. 高次域与 Dirichlet 转移

对固定 CM 域 degree=2r、finite-order Hecke 角色，普通 completion 为
L(s)(|D_K|Nf)^(s/2)(2pi)^(-rs)Gamma(s)^r（无关的固定2幂可略）。
令 C_K=|D_K|Nf/(2pi)^(2r)，普通函数方程是

\[
 L(s,\psi)=\varepsilon(\psi)C_K^{1/2-s}
 \left[\frac{\Gamma(1-s)}{\Gamma(s)}\right]^r
 L(1-s,\bar\psi).
 \tag{11}
\]

**conductor 的指数仍是 1/2−s，不是 r(1/2−s)。**次数增加的是 gamma
比值的阶数、height 的幂及 reflected profile 的复杂度。可直接核对
[Goldmakher–Louvel (3.1)–(3.2)](https://arxiv.org/html/1112.1642v2)
和[Watkins §3.6](https://magma.maths.usyd.edu.au/~watkins/papers/hecke.pdf)。
普通 FE 可推广不代表 cubic theta 的 K_(1/3)、cusp support、Gauss signal
和 reciprocal Euler table 已推广。

高次 CM、r>1 时单位 rank=r−1>0；无限多个 elements 的 absolute norm
为1，源的按所有 norm-bounded elements 的 row sum 因此已经无限。
ideal count 仍是 linear，须先改为 ideal/unit quotient 或选控制所有
archimedean embeddings 的代表，再证明 profiles、heights 和矩估计。
含 mu6 只保住一部分 Kummer 输入；d=6 的放大指数本身不会因扩域变小。

最后，目标是 zeta 或 Dirichlet，并不必须使用 −3 这个辅助域。对任何
固定虚二次 K，正确处理 finite Euler factors 后有

\[
 L_K(s,\chi\circ N)=L(s,\chi)L(s,\chi\chi_{D_K}).
 \tag{12}
\]

所以若另一个域的 whole finite-order Hecke family 获得更强无零半平面，
同样可以转移给 Dirichlet。问题在获得该全族估计；仅控制 quadratic
子族不会包含任意高阶 chi，且旧 Poisson 引入的 sextic twists 也不封闭
于 quadratic 子族。

## 7. 本次研究结论与可验收下一步

| 候选 | 对指数最有价值的可能变化 | 当前缺失 |
|---|---|---|
| Q(i) 与新 quartic source | 条件 d4 amplification；若新 shift=1 则保留 quadratic terminal | 完整 theta/cusp 数据、local Gauss phase、Euler reciprocal 和 marked/plain moments |
| 其他虚二次域 | 固定格/class 数据可重建；可能重新设计 quadratic probe | mu6/cubic source 不存在于该域；需另造闭合 probe |
| 高次 CM 且含 mu6 | 可保留 order6 Kummer/ideal-family 部件 | unit/height、多个 gamma、new completed reflection；d6 放大本身无收益 |

优先检验 Gaussian 的具体 quartic theta 文献及 prime-power 系数，按(2)
尝试构造 signal，再按(3)验证 residual quadratic terminal。只有该步
通过，才计算 local Euler reciprocal、principal branch、natural zero
和 marked/plain 全预算；只在总 contour margins 改善且全族延拓成立后
才登记新 sigma 并另写正式论文。本轮属于数域机制研究进展，无新边界。
