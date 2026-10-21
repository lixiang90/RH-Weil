# 真实 rank-one 载体的有限位 kernel、乘法过滤与原高度容量

2026-10-22。单一来源准入稿；不是 C036，不执行 actual 高频门，不结算轮数。
本稿独占分析 2602.15941v1 所定义的 rank-one subgroup／有限 frame／实 metric。
目标是把一个可计算的前端写完整，同时核它是否已承担 567 的平方 RR 责任。

## 1. 继承范围和此次原文核读

先恢复 README、STATE、check/show、G20261014、frontier、D20261020Q 和新版路线图 B。
冻结基线 0c4f／同 Goal，最强旧 542+555→557 whole leading 4/5 不变。
actual 变分门已执行并停止；安全高层 actual epsilon／原 du 的高频部件归旧强合成。
本稿不复跑它，也不把旧门的停止改成一切 D_var 未知。

此次实际打开的一手来源为 Connes–Consani,
[On the Jacobian of the Arakelov compactification of Spec Z, v1](https://arxiv.org/html/2602.15941v1)。
定位核读 §§2.1–2.2、3–4 的 rank-one／metric 定义，§5.1–5.2 的 sheaf 定义，
§8.1–8.2 的 frame 与 tensor 命题，并定位 8.15 的 framed/rooted 对偶。
本稿下面的 quotient、计数、filter 和 height 不等式是从明确群模型给出的证明，
不是声称原文已证明完整 Weil 正性、RR 容量或解析源运输。

原文的代数对象是 torsion-free rank-one abelian group；带 metric 的 unit ball 是
Gamma-set／相应模块的有界部分。它不是复向量空间，不能把下述 cardinality 写成普通复维数。
8.5／8.6／8.15 给模对象、乘法和对偶的分类／兼容，不独立提供正极化。

### 1.1 必须保留的 §5.2 字面 localization 问题

§2 明确定义 valuation subgroup L(D)，但 §5.2 对 L(V) 的一句描述同时要求：
元素在 L 内，且其约分后分母仅含 V 的补集中的 primes。
若逐字如此取值，则 V=Spec Z 时是 L∩Z，而不总是 L；取 L=(1/2)Z 时已不同。
而在 V=Spec Z 去掉 2 的例子，1/2 属于这个字面集合，结构环含 1/2，
乘积 1/4 却不在 L；因而这个字面集合不构成所需 Z[1/2]-module。
所以不能用这一句话，不经解释便把标准 restriction 当作已证的 sheaf 结论。

下面先只使用 §2 和 §8 明确给出的群与 frame；在 finite-support stratum 上，
若在非空 Zariski open V 上采用标准 quasi-coherent localization L(V)=L[S^{-1}]，并另置 L(∅)=0，确能得到通常 fractional-ideal sheaf，
并有下述 finite-place restriction。此 localization 是一个显式澄清／修复选择；
本稿不默称它由 §5.2 的字面版本已经推出。即使完全不采用该修复，下面的群 quotient 仍可独立核验。

## 2. 有限支撑／非退化 metric：可支付的精确模型

令 D 的有限部分只有有限多个整数系数 n_p 非零，令

\[
 L=L(D)=\{q\in\mathbb Q:v_p(q)\ge-n_p\ (\forall p)\}
       =h\mathbb Z,\qquad h=\prod_p p^{-n_p}>0.
 \tag{1}
\]

给定非零实 frame tau(q)=tq，t≠0；norm 是 |tau(q)|，令

\[
 \lambda=|t|h>0,\quad d=-\log\lambda,\quad
 B_R(L)=\{q\in L:|\tau(q)|\le R\},\qquad R>0.
 \tag{2}
\]

实际 sheaf 的 one-coordinate unit ball 对应 R=1。
允许 R 的意思是明确变 metric／高度截断，不能把 R=1 的有界部分当作加法群。
有限 frame xi(q)=a_f q 满足 xi(h)=u∈Zhat^×；这是 finite idele stratum 的单位平凡化。

令 E=Σe_p[p] 为有效有限除子，N=∏p^{e_p}。无需先选复结构，真正的评价为

\[
 \operatorname{ev}_{E}:L\longrightarrow
       \widehat{\mathbb Z}/N\widehat{\mathbb Z}
       \simeq\prod_{p\mid N}\mathbb Z/p^{e_p}\mathbb Z,
 \qquad q\mapsto\xi(q)\pmod N.
 \tag{3}
\]

写 q=hn，评价就是 n↦un mod N。u 在每个因子为单位，因此它是满射，且

\[
 0\longrightarrow NL\longrightarrow L
   \xrightarrow{\operatorname{ev}_E}\mathbb Z/N\mathbb Z
   \longrightarrow0,\qquad NL=L(D-E).
 \tag{4}
\]

未选 frame 时，正确的 canonical target 是 L/NL；选 h 或 frame 后才与 Z/N 识别。
这是 integral abelian groups 的 exact sequence；不能原样改成 unit ball 的 short exact sequence。
对 B_R 只是有界集合的 restriction，其零纤维为

\[
 B_R(L)\cap NL=B_R(NL),\qquad
 \#B_R(NL)=2\Big\lfloor\frac{R}{N\lambda}\Big\rfloor+1.
 \tag{5}
\]

这里右侧 NL 继承同一 tau；没有另选更有利的 metric。
image 的精确大小是 min{N,2 floor(R/lambda)+1}：整数区间
[-floor(R/lambda),floor(R/lambda)] 是连续的，乘 u 置换 residue classes。
故球上 restriction 未必满射。

对一般有限 pointed set X 的 s 个非基点，原 unit ball 条件是

\[
 \lambda\sum_{i=1}^s|n_i|\le1,
 \qquad \phi_i=hn_i.
 \tag{6}
\]

评价／kernel 可逐坐标取，但不能丢掉这条共同 l1 费用。增加标签数不是免费增加维数。

### 2.1 算术例：同一截断下有时无非零 kernel

取 L=(1/6)Z，a_f=6，tau(q)=3q，则 lambda=1/2。
one-coordinate unit ball 是 {−1/3,−1/6,0,1/6,1/3}。
N=5 时评价恰覆盖五个 residue classes，kernel 只有 0；
N=2 时 kernel 为 {−1/3,0,1/3}。
这不是一般“局部 jets 任意可插值”的结论：同样的代数 quotient 加上原高度后，非零消失可被直接禁止。

## 3. 乘法与消失过滤：相对同一 lattice 的 order

有限支撑的两个载体 L=hZ、L'=h'Z 按有理数乘法给

\[
 L\otimes_{\mathbb Z}L'\simeq hh'\mathbb Z=L(D+D'),
 \qquad hn\otimes h'm\mapsto hh'nm.
 \tag{7}
\]

tensor frame 是 tau_tensor(qr)=tau(q)tau'(r)，所以 lambda_tensor=lambda lambda'。
若 |tau(q)|≤R、|tau'(r)|≤R'，则 tensor norm≤RR'；Gamma-set 的 tuple l1 预算也由乘积求和保持。
这是 §8 tensor 乘法在本 stratum 的直接实现，不是构造了算术曲线平方上的全体截面。

额外消失必须相对原 D 定义：

\[
 F_p^eL=p^eL=\{q\in L:v_p(q)\ge v_p(h)+e\},\qquad
 (F_p^eL)(F_p^fL')\subset F_p^{e+f}(LL').
 \tag{8}
\]

所以 E 的 restriction kernel、tensor 乘法和局部 order 在同一对象上相容。
目标 Z/p^e 是 p-adic thickening，不能未经比较便称 F_p[epsilon]/(epsilon^e) 的函数域 jet。
本构造也没有自动产生 LS 证明所用 Frobenius／高阶导数整除。

## 4. 原高度提供的独立容量，而非按 Q 反定义

由 q=hn 立即得到

\[
 \#B_R(L)=2\lfloor R/\lambda\rfloor+1.\tag{9}
\]

特别地，若存在非零 q∈B_1(L) 且 ev_E(q)=0，则 q=hNm，m∈Z\{0}，从而

\[
 N\lambda\le1,
 \qquad \sum_p e_p\log p\le d.\tag{10}
\]

反过来 Nlambda≤1 时 q=hN 就满足条件，因此 (10) 对这个 rank-one 问题还是充要条件。
局部 order 下界与无穷位上界确实落在同一个非零 q 上；d 由原 lattice 和原 metric 算出，
不读取 zeta 零点，不通过 Q_W 的目标值反定义。这是一条真实、可独立检验的前端预算。
没有 metric 正性、离散性或非零性时，不能消费它。

主变化亦不会制造预算：D'=D+div(c)、h'=h/|c|，配合 |t'|=|c||t|，
map q↦q/c（符号包含在有理数同构）保持原 norm，lambda 和 (9)–(10) 不变。
有限 frame 同时变换而不是每处另选对象。

### 4.1 同一非零 determinant 的可核扩展，及其额外范畴

rank-one L 在 Q 中的 ordinary linear rank 是 1；取多个标量 section 并不会得到 rank r 的评价矩阵。
若要写 r×r determinant，必须额外构造 rank-r 载体、polynomial sections 或真实 jet 评价。
不能把 r 个标签当作已经得到这些设施。

这里给一个完全明确的辅助扩展以说明正确预算方向，但不称它是原文给出的解析载体：
取 V=⊕_{i=1}^r h_i Z，给每列 v_j=(h_i n_ij)_i 原 l1 高度
Σ_i lambda_i|n_ij|≤R_j，且 lambda_i>0、R_j>0。
令 A=(n_ij)∈M_r(Z)，Delta=det A≠0。
diag(lambda_i)A 的第 j 列 Euclidean norm 不超过 R_j，Hadamard 给

\[
 |\Delta|\le\frac{\prod_jR_j}{\prod_i\lambda_i}.
 \tag{11}
\]

每个 p 处使用同一 A 的单位 frame。若经过 det 为 p-adic 单位的行变换，
第 i 行有 p^{e_{p,i}} 的共同因子，则
v_p(Delta)≥Σ_i e_{p,i}。这只取已实际证明的 orders；不会自动给高阶整除。
令 ell_p 为所得的下界，则非零整数 Delta 满足

\[
 \prod_p p^{\ell_p}\le|\Delta|
 \le\frac{\prod_jR_j}{\prod_i\lambda_i},\qquad
 \sum_p\ell_p\log p\le\sum_j\log R_j-\sum_i\log\lambda_i.
 \tag{12}
\]

这精确实现“同一非零 determinant＋有限位整除＋无穷位上界”。
原有理 determinant section 为 det(h_i n_ij)=(∏h_i)Delta，(11) 对应其 tensor metric，
不是另把每个地方的有利 minor 拼在一起。
例如 r=2、lambda_1=lambda_2=1/4、R_1=R_2=1、A=4I，
Delta=16，两个 p=2 的行 order 均为 2；上下界同取 16。

本扩展只用有理 lattices 与原高度；它不提供从复解析源 r 到这样的 V、A、R_j 的 map，
不把 direct sum 的列预算等同于完整 Weil norm。

## 5. 非 idele／奇异 stratum 的实际负对照

### 5.1 L=Z[1/p]：局部 target 会消失，arch 球却无限

取 a_p=0、a_ell=1（ell≠p），tau(q)=q。
则 L=L_a=Z[1/p]，且 pL=L，所以 L/p^eL=0；finite frame 的 p-component 本来就是 0。
因此这里不能继续声称到 Z/p^e 的满评价，更不能人为恢复失去的 target。
对 ell≠p，L/ell^eL≅Z/ell^e，评价以 p 的逆元计算，确仍非退化。
然而任何 R>0 的 B_R(L) 都含无限多个 p^{-k}，故 cardinality 不是 (9) 的有限值。
同一个模块保留良好局部评价并不支付全局有限容量。

### 5.2 无限支撑，但每个局部 target 均非零

令所有 finite n_p=1，则 L={约分后分母 squarefree 的有理数}；取 norm=|q|。
其 adelic representative 为 a_p=p（每处 valuation 1），是有限 adele，但不是 finite idele。
每个 L/p^eL 都仍是 Z/p^e，finite frame 在相应局部最低 valuation 上给单位。
但 B_1(L) 含所有 1/p，再次无限。故“有限个或全部局部 thickening 评价良好”仍不能代替离散全局高度容量。

更一般地，任意 rank-one H⊂Q 对固定 p：若 H 是 p-divisible，则 H/p^eH=0；
若不是，则 v_p(H) 有有限下界，且取到一个最小值，H⊗Z_(p)=p^kZ_(p)，
因此 H/p^eH≅Z/p^e。证明最后一步可先 localize；模 p^e 时所有与 p 互素的整数本来已可逆，
所以 localization 不改变 quotient。有限 N 再由 CRT 分解。
此分类仅支付实际 quotient；它没有证明 bounded arch sections 有限。

### 5.3 零 seminorm 与一般非循环群

即使 H=hZ 是循环群，tau=0 时 B_1(H)=H 无限，arch 上界不能用于 (10)。
若 tau≠0，而 rank-one H 非循环，则任意 R>0 的 B_R(H) 仍无限。
证明：取 h_0∈H 非零，h_0^{-1}H⊂Q 含 Z；非循环意味着其约分分母无界。
若 a/b 属于该群且 gcd(a,b)=1，Bezout 说明 1/b 也属于该群；所以 H 有趋零的不同非零元素。
反之 hZ 的有界球显然有限。
因此 finite-cardinality 原高度容量恰要求非零 seminorm 和循环的底层 rank-one 群，
不能从“正 norm”单独推出，也不能覆盖所有原文为了 spectral realization 而保留的奇异 strata。

## 6. 这条容量为什么还不是 567 的平方 RR 输入

对固定 finite-support D 的 tensor powers，lambda_n=lambda^n。由 (9) 得

\[
 \log\# B_1(L(D)^{\otimes n})
   =\max\{nd,0\}+O(1),\qquad |O(1)|\le\log3.
 \tag{13}
\]

这里仅计算有界点数的 logarithm，不把它冒认成 Gamma-module 的独立 dimension 定理。
这是一次增长；若再 tensor 一个固定 K，则为 max{d_K+nd,0}+O(1)。
在 degree-zero 方向 d=0，该计数保持常量，没有 n^2 自交系数。
567§2／§6 的机制则要求同一平方／对应上的实际 sections 和乘法，
以及 l(K±nD) 的独立 RR 下界中出现 n^2 D^2/2，才能注入固定或有控增长的 H0(2K) 容量而迫使 D^2≤0。
本 rank-one 曲线线性容量不能直接填入那个二次项的位置。

这不是排除一切 generalized RR／连续容量；也不是证明某个未来的 arithmetic-square 构造不可能。
它只说明：这里已算出的 degree、finite-place kernel、tensor product 和 (10)/(12)，
尚未给出所需平方对象、同源 self-intersection 或 RR 二次下界。
把 (13) 的斜率命名为“无限 genus 修正”不会产生缺少的项。

## 7. 原源、正反系统和消费边界

本稿实际闭合的是：明确 finite-support rank-one lattice 的 finite-place evaluation、
kernel、额外消失过滤、tensor 乘法和独立原高度上界；奇异／无限支撑 stratum 有精确反测试。
新增的前端比“存在 H0／RR”有内容，但尚无
physical r=e^(u/2)f → section／correspondence 的实际 map。
因此不能执行 principal relation 与537小窗非根 r0 的双测试，不能称它已通过。
亦无原 du／Dlog 到列高度 R_j 的有费运输。

函数域的真实曲线上，O(D)→O(D)|E 的 kernel 和乘法是合适对应物；
但完整 Weil 正性仍用平方上的有效性／RR／Hodge，而不只单曲线 restriction。
连续 Z_c 正负段本身不给 rational prime places、frame 或离散 lattice；不能凭 Euler 对偶把它们塞进本 finite-support 模型。
强行外加相同 lattice/metric 时，(10) 对两段一样成立，故它不是区分正负段的证书。
数域可用 fractional ideal 与各 arch metric 替换，但 ideal labels、判别式、复位和完整局部 normalization 均须另付；
本 Q 上的计数不自动恢复 Gamma_R/Gamma_C、prime-power trace 或 pole 缺陷。

尤其，本文没有把原定义的 tau-norm 比较成经典 zeta 的完整 Gamma 热量，
没有用 finite Euler numerator 替换全部 prime powers，也没有删掉任何双极点项。
完整 Weil 二次型仍保留这些成分；它们根本尚未出现在 (10)/(12) 的同源预算中。
若先把全位预算差定义为 Q_W 再假设其非负，仍是 Weil 正性的等价改写，不是本稿的新输入。

结论：这是可独立检查的 arithmetic 前端和明确容量边界，不是已准入的完整 Weil 合同。
在没有 analytic source→sections／同一 determinant 的 map 之前，应在此停止本候选来源门；
不以已有线性高度新建 unknown RR 合同，不追加 jet 阶或重跑 Sonin 高频。
重准入至少需要实际 map＋原范数费用，或一个不按 Q 反定义的 arithmetic-square 二次容量／完整预算身份。
宏观容量、危险核心、coupling、通常 Xi 识别及最强旧 whole 4/5 均未改变。
