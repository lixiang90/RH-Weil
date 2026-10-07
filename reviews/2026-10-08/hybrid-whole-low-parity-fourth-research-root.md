# 原路线完整低素数第四矩的奇偶分解

2026-10-08。作者 root。新推导，待另一作者全文独立审查。
本稿处理全部 genuine low primes p≤sqrt X、全部四词与原有限 carrier。
不是缩小素数范围的 cap 计算。新结论不需要 high 第四矩有界前件。
保留 endpoint taper 与内部 P；没有宣布新的实际比例或无零边界。

## 1. 原对象与准确结论

令 X=T/(2π)、ell=log X、d=floor(X ell)、I=[−ell/2,ell/2]。
E、P=EE*、Q=1−P、B_L、L=E*B_LE 均为原 AF 定义。
J=M_sign(u)、S=E*JE、U=sgn S，零特征值选 +1。
因此 U*=U、U²=I。所有迹归一化为 τ(A)=Tr(A)/d。
长度用 ell，矩阵 L 专指 low。

定义真实 finite 矩阵

\[
 L_{\mathrm e}=(L+ULU)/2,\qquad
 L_{\mathrm o}=(L-ULU)/2.                                \tag{1}
\]

这是 low 本身的分解，不是 low 平方的分解。各自 Hermitian，
U L_e U=L_e、U L_o U=−L_o。以下仅常数计算取 flat profile；
edge taper 仍为原来的固定宽度 O(1) 的真实光滑函数。

\[
 \boxed{\begin{aligned}
 \tau L_{\mathrm e}^{\,2},\ \tau L_{\mathrm o}^{\,2}
      &\longrightarrow1/12,\\
 \tau L_{\mathrm e}^{\,4},\ \tau L_{\mathrm o}^{\,4}
      &\longrightarrow1/60,\\
 \tau L_{\mathrm e}^{\,2}L_{\mathrm o}^{\,2}
      &\longrightarrow3/320,\\
 \tau L_{\mathrm e}L_{\mathrm o}L_{\mathrm e}L_{\mathrm o}
      &\longrightarrow1/240 .
 \end{aligned}}                                         \tag{2}
\]

含奇数个 L_o 的 finite 四词迹准确为零；含两个 L_o 的其余排列由
有限矩阵循环迹给出。整个低素数第四矩恢复为
2/60+4(3/320)+2(1/240)=19/240。

| 完整冻结输入 | canonical UTF-8 LF SHA-256 |
| --- | --- |
| [entire low4 与原路径、Hilbert、全部非零原子](../2026-10-07/hybrid-low-prime-exact-fourth-path-constant-research.md) | 798947fb9cd13f25b541025f0c180945590341bbab6f55cacbcf6c50e87ee080 |
| [low 平方 parity、sharp 恢复](../2026-10-07/hybrid-parity-resolved-residual-necessary-constraints-radial.md) | 6a5fb7db8467e80682d7351ee37a940af8d39de50fffe2f16b0b3a48d5dfc6f6 |
| [465 actual 带权 second](../../notes/465-centered-high-square-joint-fourth-budget.md) | a9290d2d847c2a3f7942b26353bd1582a68b391e481acc109c4ac18d3d750464 |
| [454 原 background 与带权矩准入](../../notes/454-original-background-and-weighted-prime-mixed-traces.md) | 8ab99d60c1b748dc561cac57ee498057a0c9fb19b9778a041261b1bad0750db7 |

canonical 只改换行，不删 EOF 字节。
本稿使用 454 的真实 bounded multiplication 与 low second 准入，
不将数值脚本作为 prime 渐近证明。

## 2. 固定 smooth 标记的全部 P 费用

取固定 epsilon>0，odd real contraction j_epsilon(t)，在
|t|≥epsilon 等于 sign t；J_epsilon=M_j_epsilon(u/ell)，
S_epsilon=E*J_epsilon E。
先定义 L_e,epsilon=(L+S_epsilon L S_epsilon)/2，
L_o,epsilon=(L−S_epsilon L S_epsilon)/2。
对应真实 physical operators 为
B_e,epsilon=(B_L+J_epsilon B_L J_epsilon)/2、B_o,epsilon 类似。

每个四词展开成有限个闭合 finite word，每项恰有四个 B_L，
至多八个 J_epsilon，所有内部 P 在展开时保留。
原 low crossing 给

\[
 y=\|B_L\|\ll X^{1/4}/\ell,\quad
 l_L=\|QB_LE\|_{\rm HS}\ll y\sqrt{\log(2+\ell)},\quad
 l_{J,\epsilon}=\|QJ_\epsilon E\|_{\rm HS}
       =O_\epsilon(\sqrt{\log(2d)}).                    \tag{3}
\]

这里对 smooth J 使用较宽的 log d 估计，容许 periodic endpoint jump。
J 为真实实线乘法，绝不与 P 交换。各 adjoint crossing 相同。
闭合 word 中把 physical identity 改为 P 的每个差项至少两次跨越
P/Q；逐一固定首次退出与最终返回，夹在两 crossing 间的所有 operators
以其 op norm 控制。finite 个项的费用至多

\[
 C_\epsilon\{y^2 l_L^2+y^3l_L l_{J,\epsilon}
                         +y^4l_{J,\epsilon}^2\}=o(d).  \tag{4}
\]

若 crossing 全在 J 上，四个 B 的费用就是 y⁴；
若一个或两个 crossing 在 B 上，各自少一个 y。最后一项/d
O_epsilon(ell^−4)，其余更小。因此 (4)没有用未知 high4，
没有用 operator-small 的 projection error。额外一个固定 bounded
smooth row weight 的闭合 word 同样成立，常数只依该 weight。

## 3. 非零低素数原子的整个准入

给定 signs、primes 与累积位移 s_j，physical 四词是原来的
prod b_p K_d(s_4) times 一个真实 overlap 积分。标记在各节点额外乘
(1±j_epsilon(t_j)j_epsilon(t_{j+1}))/2；
其值位于 [0,1]，且仅有原四个 translated row 节点。
把每个节点的 phi、phi² 与 j_epsilon 的幂合并成一个固定 C² window。
其 Fourier L¹ norm 为 O_epsilon(log(2+ell))，所以原 joint Fourier
分离仍只付固定次幂 log ell。载波 endpoint phases 全部保留。

原 exact n=m 必须先剔除，再做 Hilbert。各符号类的完整范围为：

| signs | 整个 near 的真实产品 | weighted energy | normalized near fee |
| --- | --- | --- | --- |
| two+/two−，n≠m | n=pq,m=rs≤X | E_LL≪X/ell² | O_epsilon((log ell)^m/ell²) |
| three+/one− | n=pqr≤2h≤2sqrt X | E_3,E_1≪sqrt X/ell | O_epsilon(X^−1/2(log ell)^m/ell) |
| four+ | s_4≥log16 | 没有 near | 0 |

负 signs 数更多时整体反转 gives 同样费用；所有 sixteen signs 已包含。
这里使用的非等间距 Hilbert inequality 是
[Montgomery–Vaughan 原文的 Theorem 2](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)；
仅在上述真实整数 log frequencies 的并集上，先去准确零频，再极化成
双线性式。该经典不等式不供应尚未付款的 whole high-fourth cancellation。
对 entire far（包括 ±ell alias），真实 overlap 与原式一样
|s_4|≥ell 时为零；非零支持且 |s_4|≥log(3/2) 时，
|K_d(s_4)| times overlap≪X^−1。
原 low whole mass、真实 product support 给 three 类费用
O(ell^−4)、O(ell^−2)、O(X^−1/2/ell)。
额外 [0,1] 节点标记不放大这些 absolute estimates。

因此不是只保留配对模型：所有 nonzero atoms、distinct primes、
所有 middle placements、alias 与原 P 已在 (3)–(4)及本节付成 o(d)。
固定 epsilon 后 T→∞，没有新增 [R] 或高矩前件。

## 4. S4 中 sharp U 的恢复

新增的 sharp 恢复必须作用于 L 本身，而不只作用于 L²。
取 smooth 非负 g_epsilon≥|J−J_epsilon|²，支撑在 |u|≤2epsilon ell，
且 g_epsilon≤4，G_epsilon=E*M_g_epsilon E。
本稿第二、三节同样准入 τ(G_epsilon L⁴)：
zero path 每个起点只在一个宽度 4epsilon 的条带积分，prime measure
总量有界，故

\[
 0\le\tau(G_\epsilon L^4)
              =O(\epsilon)+o_\epsilon(1).               \tag{5}
\]

这里 (5) 的有限迹为正；(4)已支付其 physical-to-actual 的差，
不以未经准入的 pointwise row 演算代替。

写 D_1=U−S、D_2=S−S_epsilon。compression Schwarz 给
D_2²≤G_epsilon、||D_2||≤2。
对 Hermitian A,B，Tr(A²B²−ABAB)=||[A,B]||HS²/2≥0；
令 A=D_2²、B=L²，得到

\[
 \begin{aligned}
 \|D_2 L\|_{4,d}^4
  &=\tau(D_2^2L^2D_2^2L^2)\\
  &\le\tau(D_2^4L^4)
   \le4\tau(D_2^2L^4)
   \le4\tau(G_\epsilon L^4).                            \tag{6}
 \end{aligned}
\]

原 sharp J 泄漏给 ||D_1||HS²≤||QJE||HS²=O(log(2d))，
||D_1||≤1；于是
||D_1 L||4,d⁴≤y⁴||D_1||HS²/d=O(ell^−4)=o(1)。
LD_i 是其 adjoint，S4 norm 相同。Minkowski 与 (5)–(6)推出

\[
 \|(U-S_\epsilon)L\|_{4,d},\
 \|L(U-S_\epsilon)\|_{4,d}
       =O(\epsilon^{1/4})+o_\epsilon(1).                 \tag{7}
\]

准确差 ULU−S_epsilon L S_epsilon
=(U−S_epsilon)LU+S_epsilon L(U−S_epsilon)。
所有 U,S_epsilon 为 contraction，所以 (7)控制 L_e−L_e,epsilon
以及 L_o−L_o,epsilon 的 S4 norm。
已付 whole τL⁴=O(1) 先保证这些矩阵的 S4 norms 有界；
四因子 Hölder 再把每个实际 sharp 四词传到 smooth 极限。
顺序严格是 fixed epsilon、T→∞、epsilon→0。
既未假设 high4，也未丢掉低平方残差的 centering。

## 5. zero 路径的 exact half-line 积分

四步 zero 只来自原 three pairings A、A'、O，
有序 p,q 与 sigma,eta=±1 全部保留：

\[
 A=(\sigma x,-\sigma x,\eta y,-\eta y),\quad
 A'=(\sigma x,\eta y,-\eta y,-\sigma x),\quad
 O=(\sigma x,\eta y,-\sigma x,-\eta y).                 \tag{8}
\]

x=log p/ell,y=log q/ell 均在 [0,1/2]。相同素数 intersection 的六种
two+/two− sign words 各减一次，absolute error O(ell^−4)，
含额外 [0,1] 标记仍成立。
原 Mertens measure sum(log²p/(ell²p)) delta_x→x dx；
两素数 measure 给 xy dxdy，不在 x=0 添加固定素数原子。

给定四个 e/o 标签、初始 half h_0=±1，逐步 e 保持 half，
o 改变 half。累积位移 c_j(x,y)，j=0,...,4。
half + 对应 [0,1/2]、half − 对应 [−1/2,0]。
准确 allowed starting-row 长度为

\[
 \ell_{\rm path}(x,y)
 =\left(\min_j\{b_{h_j}-c_j\}
                -\max_j\{a_{h_j}-c_j\}\right)_+.        \tag{9}
\]

四个 e/o 标记物理极限正是这些 half constraints；smooth 标记
epsilon→0 的 bounded dominated convergence 得 (9)。
含 odd 数目 o 时无法闭合。其余将 xy ell_path 在整个 square 积分，
对 three pairings、four orientations、two initial halves 全部求和。

| word | A | A' | O | total |
| --- | --- | --- | --- | --- |
| eeee | 7/960 | 7/960 | 1/480 | 1/60 |
| oooo | 1/120 | 1/120 | 0 | 1/60 |
| eeoo、ooee | 13/1920 | 0 | 1/384 | 3/320 |
| eooe、oeeo | 0 | 13/1920 | 1/384 | 3/320 |
| eoeo、oeoe | 0 | 0 | 1/240 | 1/240 |

积分可按 max lower、min upper 的 affine arrangements 精确分区。
[独立有理积分脚本](../../scripts/hybrid_whole_low_parity_exact.py)
对 square 做 Fraction 半平面裁剪；每个 cell 三角化，再用
∫_simplex r^i s^j drds=i!j!/(i+j+2)! 积分 xy times affine length。
所有 cell 为有理凸多边形，重叠只有边界；八种 odd-label 自动零。
脚本核算 (9)，不证明本稿第二至第四节的 analytic admission。

可另简核 all-e：每个半区长度 b=1/2，
∫xy(b−max(x,y))=b⁵/20、∫_(x+y≤b)xy(b−x−y)=b⁵/120；
两半区总 2(4b⁵/20+8b⁵/120)=1/60。
all-o：A、A' 各给 2∫xy min(x,y)，O 无可行四步；
∫xy min(x,y)=2b⁵/15，所以总 8b⁵/15=1/60。
表中全部 finite 循环迹与全 low4 19/240 互相一致。

## 6. 完整带权 second 与 residual 常数

令 V_e、V_o 为 physical B_e²、B_o² 的 p=same-p opposite-sign
zero atoms 的乘法函数经 E compression。其 exact finite-X 函数保留
原 phi² 与 translated phi²；V_e+V_o=V（原 total-low diagonal）。
flat row 坐标 t=|u|/ell，0≤t≤1/2 的 profile 极限为

\[
 v_e(t)=1/8-t/2+t^2,\quad
 v_o(t)=1/8-t^2/2,\quad
 w(t)=t(t+1)/2.                                       \tag{10}
\]

例如同半区低 shift ranges x≤t 与 x≤1/2−t；
crossing range t<x≤1/2，所以原 prime measure x dx 直接给 (10)。
二步非零原子与 finite P 费用为整个原 weighted-second 的费用；
先 fixed smooth J、bounded row weights，再 sharp 恢复：
S4 (7)保证 second products 的 S2 收敛，bounded multiplier 可乘。
固定 smooth row 函数的 diagonal 主项为其与 (10) 的积分。

V_e,X,V_o,X 的 exact prime functions 虽可能有 jump，不能免费套 C²；
可先用原 Mertens 在离两个 endpoint strips 宽度 delta 的 compact
部分作 uniform 逼近，再用固定 smooth majorant of these strips。
weighted second 的 zero 主项在 strip 中为 O(delta)，其他原子仍 o(1)；
uniform boundedness 及正 multiplier sandwich 支付误差。
先 T 后 delta 的步骤同时支付 τH²V_o−τWV_o→0，
以及 V_o 与 sharp U 的渐近交换。后者也可直接用 bounded variation
Fourier crossing O(sqrt(log(2d)))，因为 physical diagonal 的 variation
是原 bounded prime measure 与固定 taper 的 total variation。
没有假设任意 T-dependent weight 的免费准入。

全部 constants 为

\[
 \begin{array}{c|cccccc}
 &\tau V_e^2&\tau V_o^2&\tau V_eV_o&
    \tau WL_e^2&\tau WL_o^2&\tau WV_o\\ \hline
 \lim&7/960&1/120&13/1920&9/640&19/1920&19/1920 .
 \end{array}                                         \tag{11}
\]

每个 mixed second diagonal，例如 τV_o L_o²，也等于相应 row
integral 1/120；交叉项不能用任意两个抽象 low matrices 代替。
因此

\[
 \boxed{\tau(L_o^2-V_o)^2\to1/120,\quad
 \tau(L_e^2-V_e)^2\to3/320,\quad
 \tau(H^2-W)V_o\to0.}                                 \tag{12}
\]

两 low-square residual 的 covariance 为
3/320−13/1920=1/384。它们相加是 U-even part of Δ，variance
3/320+1/120+2/384=11/480；
U-odd part {L_e,L_o} 的 variance
2(3/320+1/240)=13/480，与冻结来源的独立计算相符。

本稿付款的是 whole 原 low 对象的必要联合常数。
未知 whole high-square q upper、整个 mixed31/22 净 upper 仍未付。
这些低常数可供下一份完整 parity Gram 使用，但自身没有改变比例或边界。
