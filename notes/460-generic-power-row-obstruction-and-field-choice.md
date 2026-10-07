# 460：幂次重复行对一般大筛的限制及换域含义

2026-10-07。回应辅助数域选择问题，补充 [457](457-number-field-choice-and-relative-amplification.md)
和 [458](458-gaussian-all-row-large-sieve-comparison.md)。
状态：一般角色矩阵的严格下界；没有得到新的无零边界。

## 1. 结论与适用对象

固定有限坏素数集，列 \(n\) 限为与它互素的 squarefree 理想、
\(D\le Nn\le2D\)，行 \(u\) 则包括全部 good 非零理想。
Gaussian 情形用相应的 primary generators 读同一矩阵。定义

\[
 B_d(U,D)=\sup_{\sum_n|a_n|^2=1}
 \sum_{0<Nu\le U}\left|\sum_n a_n\chi_n(u)\right|^2.
 \tag{0}
\]

这里列的 squarefree 限制是后面二次 Hecke-family upper bound 的前件；
行没有 squarefree 或 \(d\)-free 限制。

高斯域的四次放大在理想 raw Möbius 合同下有条件收益，但不能从任意列
系数的大筛中直接取得该合同。下面保留非互素处的自然零值，证明一般
全行矩阵至少有

\[
 B_d(U,D)\gg_K \frac{D U^{1/d}}{\log D}
 \quad(U^{1/d}<D)
 \tag{1}
\]

的重复行贡献。因此，即使四次 squarefree 大筛将来达到理想的线性
宽度，**全部实际行**上的任意系数线性 raw 合同仍需另行处理。
这里的下界属于可以任意选择列系数的算子范数，不是固定
\(\mu(n)\eta(n)W(Nn/D)/\sqrt{Nn}\) 逆列的下界。

## 2. 保留全部自然零值的证明

先在 \(K=\mathbf Q(i)\) 上取 \(d=4\)。奇理想使用唯一 primary generator。
记

\[
 \mathcal P_D=\{\mathfrak p\text{ good 奇素理想}:D\le N\mathfrak p\le2D\},
 \qquad P_D=|\mathcal P_D|\asymp D/\log D.
 \tag{2}
\]

这个素理想计数不依赖本项目的无零输入：Gaussian split primes 来自
\(p\equiv1\pmod4\)，每个给出两个 norm 为 \(p\) 的素理想；固定模数的
素数定理已经给出 (2)。inert primes 的 norm 为 \(p^2\)，不影响该数量级。
固定删去有限个坏素数同样不改变数量级。相关经典输入可见
[Kedlaya 的 MIT 讲义 Theorem 5](https://kskedlaya.org/18.785/dirichlet.pdf)。

将列系数选为

\[
 a_n=P_D^{-1/2}1_{(n)\in\mathcal P_D},\qquad \sum_n|a_n|^2=1.
 \tag{3}
\]

取所有与固定坏素数集互素的奇 primary \(r\) 满足
\(0<Nr\le U^{1/4}<D\)，并令 \(u=r^4\)。
这些 \(u\) 都是全行矩阵中的实际行，且 \(Nu\le U\)。映射 \(r\mapsto r^4\)
在 primary generators 上注入：相同四次幂只允许单位之比，而 primary
条件唯一固定该单位。奇 primary 理想的线性格点计数给出
\(\gg U^{1/4}\) 个这样的行。

对每个所选素理想列 \(n\)，\(Nn\ge D>Nr\) 保证 \((n,r)=1\)。四次
符号在非单位处零延拓，因此精确有

\[
 \chi_n(r^4)=1_{(n,r)=1}=1.
 \tag{4}
\]

没有删掉 mask；所选支持使它确实恒等于一。于是每个行的内和都是
\(\sqrt{P_D}\)，从非负的全行和中只取这些行即得

\[
 \sum_{0<Nu\le U}\left|\sum_n a_n\chi_n(u)\right|^2
 \ge\#\{r:0<Nr\le U^{1/4},\ r\text{ good 奇 primary}\}\,P_D
 \gg \frac{D U^{1/4}}{\log D}.
 \tag{5}
\]

共轭符号给出同一下界。单位补充律不会改变 (4)，因为我们取的确实是
完整的四次幂，而不是未经归一化的等价行。

更一般地，若固定数域的 ideal-indexed order-dividing-\(d\) 矩阵保留
\(\chi_n(r^d)=1_{(n,r)=1}\)，且允许所有 \(u=r^d\) 理想行，理想幂映射
注入、固定去坏素数的理想计数为线性、素理想计数为 (2)，同一证明
得到 (1)。这条一般表述按理想计数，不把高次域的无限单位当成有限
element rows。Gaussian \(d=4\) 与 Eisenstein \(d=6\) 的 primary 实现
均直接符合上述条件。

## 3. 近临界线性合同的必要条件

假设一般全行矩阵对所有 unit-energy 列系数都有

\[
 B_d(U,D)\ll_\varepsilon U(UD)^\varepsilon.
 \tag{6}
\]

取固定 \(c>0\)、\(U=D^{1+c}\)，且 \(1+c<d\)。由 (1)，

\[
 \frac{B_d(U,D)}U
 \gg\frac{D^{[1-(d-1)c]/d}}{\log D}.
 \tag{7}
\]

若 \(c<1/(d-1)\)，右侧带固定正幂；选择足够小的
\(\varepsilon<[1-(d-1)c]/[d(2+c)]\)，即与 (6) 矛盾。因此该一般
线性合同在指数意义上至少需要

\[
 U\gtrsim D^{d/(d-1)}.
 \tag{8}
\]

这是必要条件，不是充分条件；临界处的 \(\log D\) 和任意小幂也不产生
新的可用 upper bound。

| 角色阶数/幂次 \(d\) | 任意列系数、全行线性宽度的必要指数阈值 |
|---|---:|
| 2 | \(U\gtrsim D^2\) |
| 4 | \(U\gtrsim D^{4/3}\) |
| 6 | \(U\gtrsim D^{6/5}\) |

对满足 quadratic Hecke-family 前件的 good ideal 矩阵，二次情形还有
相应通用 upper bound

\[
 B_2(U,D)\ll_{K,\varepsilon}\{U+D\sqrt U\}(UD)^\varepsilon.
 \tag{9}
\]

证明是逐 prime valuation 唯一分解 \(u=a r^2\)，\(a\) squarefree，
\(r\) 任意且允许与 \(a\) 重叠。固定 \(r\)，把
\(1_{(n,r)=1}\) 放入列系数，列能量仍不超过一；
[Goldmakher–Louvel Theorem 1.1](https://arxiv.org/html/1112.1642v2)
给 \(U/(Nr)^2+D\)，保留固定有限 reciprocity sectors。
求和 \(Nr\le\sqrt U\) 时，\(\sum_r(Nr)^{-2}\) 有界、理想数
\(O(\sqrt U)\)，即得 (9)。结合平方行下界，通用二次全行矩阵的
线性阈值 \(U\approx D^2\) 在指数层面已经匹配。
Gaussian 四次的 (8) 仅迫使 \(U\gtrsim D^{4/3}\)，而现有
[458](458-gaussian-all-row-large-sieve-comparison.md) 的 upper bound
需要 \(U\ge D^2\) 才线性；此中间区间不能由下界宣称已经解决。

限制起始行到 \(d\)-free rows 会删去这里的重复行，但原放大平均的
终端是 \(u a^d\)，会重新引入非 \(d\)-free 行；不能将起始行限制
未经说明地移到终端 raw family。

## 4. 为什么不否定实际 Möbius 合同

[457](457-number-field-choice-and-relative-amplification.md) 的 raw 前件
针对同一个真实逆列，要求每个固定 \(c>0\)、\(H\ge D^{1+c}\) 都有
线性均方界，并保留原 profile 的尺度 supremum、高度和自然零值。
它不允许任意替换系数。

(3) 的 prime-only 支持不等于实际固定 annular profile 的支持；实际
逆列还包含复合 squarefree ideals。它们可能与素数项抵消。
故 (5) 不能给实际逆列下界，也不能反驳已经导入的 Eisenstein raw
合同。相反，它说明这种 raw 合同必须利用特殊 Möbius/目标系数的
分析结构，不能由任意系数的大筛宽度直接推出。

较小的 \(d\) 在两处产生不同效果：

- 假设特殊 raw 合同已经支付，\(u\mapsto ua^d\) 的平均更有效，
  [457](457-number-field-choice-and-relative-amplification.md) 得到
  \(e_d(r)=\max\{1,[1+(d-1)r]/d\}\)，\(r>1\) 时较小 \(d\) 较好。
- 若只使用任意系数的一般全行矩阵，较小 \(d\) 让幂次重复行更密，
  (8) 的必要阈值反而更高。

两句话对应不同合同，可以同时成立。

## 5. 对辅助数域选择的具体判断

Eisenstein 域的当前优势仍是 cubic Gauss signal、sextic completed
reflection、quadratic terminal 的配合，而不是较小的格常数。
Gaussian 域已经有真实 quartic squarefree signal 和全行上界，但
其特殊 Möbius raw 合同、完整反射、local Euler quotient、marked/plain
预算仍需证明。普通大筛的额外费用见 [458](458-gaussian-all-row-large-sieve-comparison.md)；
即使单独改善其 squarefree 部件，也需说明如何绕过本笔记的全行
任意系数限制。

更直接的二次系统有条件 \(e_2\) 收益，也有更密的平方行。当前原
Poisson 的辅助 sextic twists 不封闭于 quadratic family，故不能只
限制目标角色阶数就取得该路线。

本笔记确认了一个一般估计的结构限制，没有给实际 Möbius 列的
新 upper bound，没有得到新的 \(\sigma\)。项目采用的既有引用
输入 [R] 下，已记录的 strict boundary 仍为
\(\sigma_*\approx0.874957019420099\)。
