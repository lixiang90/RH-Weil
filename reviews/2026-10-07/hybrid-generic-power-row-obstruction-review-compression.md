# 460 幂次重复行与数域选择：独立全文审查（compression）

2026-10-07。结论：**最终全文限定 PASS，未发现 P1/P2 数学阻断。**
通过的是任意列系数、good squarefree columns、全部 good rows 的算子范数
下界、必要指数阈值与二次情形的匹配 upper。没有给实际 Möbius 逆列下界，
没有反驳既有 [R] raw 合同，也没有得到新无零区域。

仅新增本审查文件；被审稿、旧笔记、冻结审查、外部 math、Goal、Git
均未修改。本审查没有另派子 agent。

## 1. 最终输入绑定和引用核验

全文初读并在作者澄清后全文复读
`notes/460-generic-power-row-obstruction-and-field-choice.md`。canonical LF
规则为 CRLF/孤立 CR 转 LF，再作 UTF-8 SHA-256。最终输入：

~~~text
9625c0d618854769de90edfb3ee3b8d8b89e1d3b2b83d676dffccb927e09d85f
7891 bytes；195 lines
~~~

初读建议显式定义 B_d 的 squarefree column 范围，避免将 GL upper
误读成 all-ideal columns。作者已在 (0) 明列 good squarefree columns、
unit coefficient energy 和全部 good rows；最终稿消除了这个歧义。
随后作者把 prime columns、multiplier r 和显示的计数集合都明确限为 good
支持。本审查对这个真正最终版本再次全文复读，以下计数保留该固定 exclusions。

实际浏览了 [Kedlaya 的 MIT 讲义 Theorem 5](https://kskedlaya.org/18.785/dirichlet.pdf)
和 [Goldmakher–Louvel Theorem 1.1](https://arxiv.org/html/1112.1642v2)。
前者给固定模数 AP 素数定理，后者明确要求 squarefree ideal family。
本审查不重新认证项目 451 的 strict boundary 或其整链 [R] 输入。

## 2. Gaussian 行数、单位注入与 exact masks

固定 mod 4 的 AP 素数定理给 norm 在 [D,2D] 的 Gaussian split prime
ideals 数量为 D/log D 的量级；每个 p=1 mod 4 给两个 prime ideals。
inert prime 的 norm 为 p²，其数量仅 O(sqrt D/log D)。固定删去有限坏
primes 不改量级。因此 (2) 在 D 充分大的渐近范围合法，不依赖项目的新
无零结论。

每个 odd ideal 有唯一 primary generator。固定坏素数排除可用 CRT 和
有限 residue classes 处理，只改变正密度常数。格点计数给 norm 不超过 Y 的
good odd primary generators 数量为常数乘 Y 加 O(sqrt Y)，因此有至少 cY
个；有限的小 Y>=1 可用 unit ideal 调整常数。

若 r1^4=r2^4，则 r1/r2 是 Gaussian 的四次根单位。两者都是 primary，
同一 ideal 的 primary generator 唯一，故 r1=r2。这里用的是实际 primary
elements 的注入，不是未经处理的单位 quotient。

所选 prime column n 满足 Nn>=D>Nr，故 n 不可能整除 r。于是
zero-extended quartic symbol 精确满足
`chi_n(r^4)=1_(n,r)=1`。该步骤保留了 mask，再利用所选支持证明它等于
一，没有删除 nonunit 分支。共轭 orientation 与 unit supplement 均不改变
真正第四幂的值。

选 unit-energy coefficients `a_n=P_D^-1/2`，每个这些行的平方响应为
P_D。非负 row sum 可只取 pure-power rows，得到 (5)。在 general ideal
表述中，理想 prime valuations 保证 r->r^d 注入；无限单位不被计作有限
element rows。其 explicit multiplicativity、natural mask 和计数前件必须
保留，460 已明列这些前件。

## 3. epsilon 量词与必要阈值

固定 c>0、U=D^(1+c)，且 U^(1/d)<D。由下界直接除 U 得

\[
 B_d(U,D)/U\gg D^E/\log D,
 \qquad E=[1-(d-1)c]/d.
\]

若 c<1/(d-1)，E>0。假设 (6) 对每个 epsilon>0 成立，其右方除 U 是
`O_epsilon(D^((2+c)epsilon))`。先固定 c，再取
`0<epsilon<E/(2+c)`，常数不能依赖 D；D 趋于无穷时矛盾。因此 (7)
和所写 epsilon 上界正确。

等价的必要 exponent threshold 为 d/(d-1)：d=2、4、6 分别给 2、4/3、6/5。
这不是 critical endpoint 的精确 log threshold，也不是充分 upper 条件。
Gaussian lower 仅迫 U 至少为 D^(4/3) 的指数，而 458 的现有 upper
线性范围是 U>=D²；两者之间的区间仍未解决。460 没有误称该 gap 已关闭。

## 4. 二次 generic upper 的独立推导

good ideal u 的唯一分解为 u=a r²，a squarefree，允许 a 与 r 有共同
prime。固定 r 后，multiplicativity 和 zero extension 给
`chi_n(a r²)=chi_n(a)1_(n,r)`。将这个真实 mask 放入 column coefficient，
其平方能量仍不超过 1。

GL Theorem 1.1 在 row norm A=U/(Nr)²、column norm不超过2D时给
`O((AD)^epsilon(A+D))`，固定有限 ray/reciprocity sectors 只改常数。
Nr<=sqrt U 保证 A>=1，满足 theorem 的范围。求和 r 得

\[
 U\sum_r(Nr)^{-2}+D\#\{r:Nr\le\sqrt U\}
 \ll_K U+D\sqrt U.
\]

固定域的 ideal counting 及 zeta_K(2) 的绝对收敛支付上述两个和，因此
(9) 成立。其 generic linear threshold U≈D² 与 pure-square lower 在
指数层面匹配。这个 upper 仍按 (0) 的 squarefree columns 读取，不扩展
到有重复 square factors 的任意 column family。

## 5. 与真实 inverse 及换域收益的区别

prime-only arbitrary coefficients 不等于同一个 annular test 的
`mu(n)eta(n)W(Nn/D)/sqrt(Nn)`。真实列包含 composite squarefree ideals，
这些项可以与 prime 部分抵消；算子范数 lower 不能成为这条特定列的 lower。
因此不能据此反驳已导入的 Eisenstein Möbius raw 合同，也不证明 quadratic
或 quartic 的 Möbius-specific raw 合同不可能。

限制 starting rows 为 d-free 也不删除 amplification terminal ua^d 的重复
power rows。较小 d 使 conditional amplification 更有效，同时使 generic
pure-power rows 更密，是关于两个不同合同的结论，没有逻辑矛盾。

当前 Eisenstein 的 cubic signal、sextic reflection 和 quadratic terminal
仍是完整路线的关键。换 Gaussian 或直接用 quadratic symbols，需要新的
同对象 probe/completion 与 Möbius-specific estimates；单独减少 d 或改变
判别式没有产生新 sigma。460 对既有 boundary 只作 [R] 范围的状态引用，
本审查通过这一范围划分，不把它重证为无条件定理。
