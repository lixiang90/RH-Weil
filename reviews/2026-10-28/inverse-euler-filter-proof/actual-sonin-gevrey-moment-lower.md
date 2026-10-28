# C053：实际 Riesz 向量的物理端点与全大阶矩下界

2026-10-28；`/root/moment_fresh_audit` 当前独占证明稿。对象和量词按 C053 冻结；本稿不是旧准入审计的续写。已恢复 README/STATE、check→show、同一 Goal/runtime1793085111、AX 及准入消费记录。本稿只用项目已付的 cosine/Sonin/raw Mellin 定义及解析评价，以下新增计算不读原 PDF、新章、网络或数值，不改 STATE/Git/cadence。

**本腿结论：冻结对象上的全大整数阶下界可闭合。** 存在只依固定对象的 `C,n0`，对每个整数 `n≥n0`，

\[
 J_n^g=\int_{\mathbb R}|\widehat g(t)|^2|t|^{2n}|H_0(t)|^2\frac{dt}{2\pi}
       \ge \exp(4n\log n-Cn).                                      \tag{M}
\]

证明走合同允许的同对象等价物理端点方法：实际 Riesz 向量在双 gap 的右端具有非零有限阶解析芽；两个**原正 bump**的卷积保留 `ε^N exp(−A/ε)` 下包络；Taylor 余项直接控制每阶导数范数。它不使用未付的 raw `G2(t)=O(1/t)`、Fourier 两波主项、相位独立、单个好点或只沿子列的 lower。是否整体 C053 成果可消费仍由另一 norm-transport 腿、不同 fresh 和 root 最终闭合决定。

## 1. 冻结对象和原范数

记 `a=2`、`δ=log2/4`，原物理 Hilbert 空间为 `H=L²((0,∞),dx)`，第一槽线性，

\[
 (\mathcal Cv)(x)=2\int_0^\infty\cos(2\pi xy)v(y)\,dy,
 \qquad \mathcal K_a=\{v:1_{(0,a)}v=1_{(0,a)}\mathcal Cv=0\}.
\]

`k=k_(a,0)` 是该实际空间上 raw Mellin 原点评价的 Hermitian Riesz 向量：

\[
 E_{a,0}(v)=\mathcal Mv(0)=\langle v,k\rangle,
 \quad G_a(t)=\mathcal Mk(t),\quad G_a(0)=\|k\|^2>0.
\]

这些连续、解析延拓和非零性为585共同向量稿已付输入。取合同唯一的

\[
 \psi(v)=C_\delta e^{-1/(1-(2v/\delta)^2)}1_{|v|<\delta/2},
 \quad\int\psi=1,\qquad H_0=\widehat\psi G_a,
\]

以及587固定的 `g(u)=c exp[−1/(1−u²)]1_(|u|<1)`，`c>0` 使 `||g||_(du)=1`。不改变这些函数或接收向量。原酉 log map 和 Fourier 约定为

\[
 (Wv)(y)=e^{y/2}v(e^y),\quad
 \widehat f(t)=\int f(y)e^{-ity}dy,\quad
 \|f\|_{du}^2=\int|\widehat f(t)|^2\frac{dt}{2\pi}.
\]

本稿下面的辅助卷积是证明该原范数矩的工具，不是把 physical 测试源换成另一源，也不把 completed Mellin norm 当 raw norm。

## 2. 有限区间 cosine 压缩的真实投影公式

令 `L=1_(0,a)`，将 `L H` 识别为 `H_a=L²(0,a)`，令 `K=L C L|_(H_a)`。核 `2cos(2πxy)` 在有限方块上光滑，所以 K 为紧自伴 contraction。事实上 `||K||<1`：若等号，紧性给一个非零 norm-attaining 向量；等号 `||L C L v||=||v||` 迫 `Cv` 亦支持于 `(0,a)`。而紧支撑 L² 向量的 cosine 变换延拓 entire，不能在 `(a,∞)` 恒零而非零。故下述逆在这个**固定 a** 上有界；不声称随 a 一致。

定义 `T:H→H_a⊕H_a` 为 `Tv=(Lv,L Cv)`，则

\[
 TT^*=\begin{pmatrix}I&K\\K&I\end{pmatrix}>0,
 \quad P_a=I-T^*(TT^*)^{-1}T                                  \tag{1}
\]

是真正到 `ker T=K_a` 的正交投影。特别若 `Lh=0`，令

\[
 v=L\mathcal Ch,\qquad w=(I-K^2)^{-1}v,
\]

解两个 block 方程得到

\[
 P_a h=h+LKw-\mathcal C Lw,
 \quad (P_a h)(x)=h(x)-(\mathcal C Lw)(x)\quad(x>a).             \tag{2}
\]

这是从实际两个 gap 的 Gram block 直接求逆；没有用 single-gap 截断、近似投影或自由结构函数。

## 3. 从可积 Mellin 评价逼近实际原点评价

现在只取**实参数** `1/2<s≤3/4`，令

\[
 h_s(x)=1_{[a,\infty)}(x)x^{-s}\in H,
 \quad p_s(x)=x^{-s}\ (0<x<a),\qquad
 \chi(s)=2(2\pi)^{s-1}\Gamma(1-s)\sin(\pi s/2).
\]

`p_s` 只按 L¹ 使用；不将它误放入 L²。由 Abel 因子 `e^(−εy)` 的 Gamma 积分后令 `ε↓0`，对 `0<s<1,x>0` 有条件 cosine 积分

\[
 2\int_0^\infty y^{-s}\cos(2\pi xy)dy=\chi(s)x^{s-1},
 \quad\chi(s)\chi(1-s)=1,\quad\chi(1/2)=1.                    \tag{3}
\]

无穷端的普通振荡积分亦由一次 Dirichlet/分部积分收敛。截断 `h_s` 在 H 中收敛，故其 L² cosine 变换与该点值表达 a.e. 一致。因此

\[
 v_s=L\mathcal Ch_s=\chi(s)p_{1-s}-Kp_s,\qquad
 w_s=(I-K^2)^{-1}v_s.                                        \tag{4}
\]

这里 `p_(1−s)∈L²(0,a)` 对 `s>1/2`，而 `Kp_s` 是紧区间 L¹ 的光滑积分。写

\[
 w_s=\chi(s)p_{1-s}+r_s,
 \qquad r_s=(I-K^2)^{-1}b_s,
 \quad b_s=-Kp_s+\chi(s)K^2p_{1-s}.                           \tag{5}
\]

这是把 (4) 乘 `I−K²` 的直接恒等式。对闭参数区间 `s∈[1/2,3/4]`，两种幂在 L¹ 中连续且范数有界；有限 cosine 积分对参数连续进入每个 `C^j[0,a]`。故 `b_s` 如此连续，`r_s` 在 L² 连续。再用

\[
 r_s=b_s+K^2r_s
\]

及 `K²:L²(0,a)→C^j[0,a]` 有界，得到 `r_s→r_(1/2)` 在每个 C^j 中，特别 C¹ 中收敛且一致有界。这一结论没有将极限 `p_(1/2)` 当 L² 向量。

由 (2)，令 `k_s=P_a h_s`，则在 `x>a`，

\[
 F_s(x):=k_s(x)=x^{-s}-(\mathcal CL[\chi(s)p_{1-s}+r_s])(x).
                                                                    \tag{6}
\]

用 (3) 把奇异幂的**全半线**变换先配对相消，得到等价的普通振荡尾式

\[
 F_s(x)=\chi(s)\,2\int_a^\infty y^{s-1}\cos(2\pi xy)dy
                  -2\int_0^a r_s(y)\cos(2\pi xy)dy.           \tag{7}
\]

第一项分部积分一次的边界和余项分别由

\[
 a^{s-1}/(2\pi x),\qquad
 (1-s)(2\pi x)^{-1}\int_a^\infty y^{s-2}dy
\]

控制；第二项用 C¹ 一致界分部积分。于是存在固定 C，使

\[
 |F_s(x)|\le C/x\qquad(x\ge a,\ 1/2\le s\le3/4).             \tag{8}
\]

该界是**物理 x 变量**的 tail；不是未经证明的 raw Mellin `G_a(t)=O(1/t)`。由 (6) 的 L¹ 参数连续性有逐点极限，由 (8) 的 L² 主控得到

\[
 k_s\longrightarrow k_*:=1_{[a,\infty)}F_{1/2}\quad\text{in }H.
                                                                    \tag{9}
\]

每个 `k_s∈K_a`，闭性给 `k_*∈K_a`。对任意 `v∈K_a` 和实 `s>1/2`，

\[
 \langle v,k_s\rangle=\langle v,h_s\rangle
              =\int_a^\infty v(x)x^{-s}dx.
\]

积分由 Cauchy–Schwarz 绝对收敛，是同一 raw Mellin 解析函数在该半平面的值。已有解析延拓使其随 `s↓1/2` 趋原点评价，而 (9) 使左边趋 `⟨v,k_*⟩`。Riesz 唯一性遂给

\[
                         k_*=k_{a,0}.                         \tag{10}
\]

这一步把构造明确绑回冻结的实际 Hermitian Riesz 向量；不是另造一个具有较好边界的非零 Sonin trial。

## 4. 原 Riesz 向量有非零有限阶右端点

令 `q(x)=x^(−1/2)` 于 `(0,a)`，按 L¹ 使用。由于 `χ(1/2)=1`，(5) 在端点给

\[
 r_0=(I-K^2)^{-1}(-K+K^2)q=-(I+K)^{-1}Kq,\qquad w_0=q+r_0\in L^1(0,a).
                                                                    \tag{11}
\]

最后的化简只对 `Kq∈L²` 作有界算子代数，未对 q 施未定义的 L² 逆。由 (6)、(10)，原 k 在 `x>a` 的代表为

\[
                 F(x)=x^{-1/2}-2\int_0^a w_0(y)\cos(2\pi xy)dy.
                                                                    \tag{12}
\]

紧区间 L¹ 的 cosine 积分 entire，而 `x^(−1/2)` 在正轴邻域解析。因此 F 在 `x=a` 的一个双侧正轴邻域实解析，且在 `(a,∞)` 实解析。所有参数/算子为实，所以 F 实值。若其在 a 的全部导数为零，解析唯一性迫 `F≡0` 于 `(a,∞)`，由 k 的 gap 得 `k=0`，与 `G_a(0)=||k||²>0` 矛盾。因此有一个固定整数 `m≥0`、`η>0`、`c_*>0` 及 `σ∈{±1}`，使

\[
 \sigma F(a+x)\ge c_*x^m\quad(0<x<\eta).                     \tag{13}
\]

无需知道 m 的数值、声称 m=0 或无 jump；任一有限阶足以付 (M)。令 `b=log a`、`v=Wk`。则 v 在 `y<b` 为零，且由解析换元 `e^(b+x)−a=a x+O(x²)`，缩小 η 后

\[
              \sigma v(b+x)\ge c_1 x^m\quad(0<x<\eta_1).     \tag{14}
\]

这里 k 的边界有限阶是本稿新付的实际前件，不由一般 entire 非零或 Gevrey upper 推出。

## 5. 两个原正 bump 的共同物理端点 lower

定义唯一辅助函数

\[
 h=g*\psi*v\in L^2(\mathbb R),\qquad
 \widehat h=\widehat g\,\widehat\psi\,G_a=\widehat g H_0.
                                                                    \tag{15}
\]

卷积使用原 du Lebesgue measure，无 Fourier 常数。紧支撑光滑 g、ψ 与 L² 的 v 卷积给 `h∈C∞`、全部导数属于 L²。特别 Plancherel 给

\[
                         J_n^g=\|\partial^n h\|_2^2.          \tag{16}
\]

其左端点为 `L0=b−1−δ/2`：`h=0` 于 `y≤L0`，从而 h 的各阶导数在那里为零。对足够小的 `ε>0`，把 `h(L0+ε)` 的卷积变量写成

\[
 u=-1+x_1,\qquad z=-\delta/2+x_2,\qquad
 (L0+\varepsilon)-u-z=b+x_3,\quad x_3=\varepsilon-x_1-x_2.
\]

所有非零贡献均有 `x_i≥0`、`x_1+x_2+x_3=ε`。由 (14)，整个非零积分都同号 σ；g、ψ 非负，故可只保留矩形

\[
 x_1,x_2\in[\varepsilon/4,\varepsilon/3],\qquad
 x_3\in[\varepsilon/3,\varepsilon/2].                         \tag{17}
\]

当 ε 足够小使 `x_1≤1`、`x_2≤δ/2` 时，冻结的显式定义直接给

\[
 g(-1+x_1)\ge c\,e^{-1/x_1}\ge c e^{-4/\varepsilon},
\]

因为 `1−(−1+x_1)²=2x_1−x_1²≥x_1`；同理

\[
 1-(-1+2x_2/\delta)^2
 =4x_2(1-x_2/\delta)/\delta\ge2x_2/\delta,
 \quad\psi(-\delta/2+x_2)\ge C_\delta e^{-2\delta/\varepsilon}.
\]

结合 (14) 和矩形面积 `(ε/12)²`，有固定 `c_2>0,A0=4+2δ>0,ε0>0`，使**每个** `0<ε<ε0` 均有

\[
 |h(L0+\varepsilon)|
       \ge c_2\varepsilon^{m+2}e^{-A0/\varepsilon}.           \tag{18}
\]

这里没有选择频率好点、只取子列或假相位独立；物理支持迫所有卷积变量同时处于原三个端点的小邻域，(17) 的同一个小箱直接给共同 lower。

## 6. Taylor 余项给每个大整数阶的原矩

对任意整数 `n≥1`，h 在 L0 左侧光滑恒零，故

\[
 h(L0+\varepsilon)=\frac1{(n-1)!}
     \int_{L0}^{L0+\varepsilon}(L0+\varepsilon-y)^{n-1}
                                      \partial^n h(y)dy.
\]

Cauchy–Schwarz 和 (16) 给

\[
 J_n^g\ge |h(L0+\varepsilon)|^2
              ((n-1)!)^2(2n-1)\varepsilon^{-2n+1}.           \tag{19}
\]

取每个充分大整数 n 的 `ε=1/n<ε0`，将 (18) 代入，得

\[
 J_n^g\ge c_2^2((n-1)!)^2(2n-1)
                    n^{2n-2m-5}e^{-2A0n}.                  \tag{20}
\]

由整数 factorial 的 elementary Stirling lower（亦可用 `log(n!)≥∫_1^n logx dx`），

\[
 \log J_n^g\ge4n\log n-O(n)-O_m(\log n).
\]

固定 m、c2 和 A0 的费用可并入一个固定 `C n`，即得 (M)。量词是存在固定 `C,n0` 后**所有** `n≥n0`；因此可向 transport 腿交付合同规定的 `n_X=ceil(2A/log A)`，不要求 n 的子列、不换该 n recipe，也没有 degree-uniform 常数的虚假承诺。

## 7. 交付状态、最强旧比较与停止范围

本腿新付的短链为：actual 两 gap 投影 (1)–(2)；临界评价 Riesz 向量的 L² 极限/识别 (3)–(10)；其非零有限阶物理右端点 (11)–(14)；同一 g、ψ 的正卷积端点下包络 (15)–(18)；原 `dt/(2π)` 全大阶矩 (19)–(20)。无需把尚未另证的 raw Mellin 高频两波/余项补为输入。补助 bump Fourier 稿可有独立用途，但不是本证明依赖。

585/587 的合法多项式域和 Gevrey upper 只付 `J_n` 的上界，不能倒推 (M)；589/C052 的全线 evaluator upper 和局部抑制也不单独给它。因此本稿不把此 all-n lower 归为旧准入0，也不把此前裸测度 strongS′0/Sg,Sg′→0 冒作 ratio 已决定。新 lemma 仅为 C053 同一个完整数学迭代的一个新责任，不单独计轮。

**本腿无未付的 Riesz/端点/all-n 前件。** 仍未由本稿消费的是：actual `||D_Xt^nH0||` 三段 norm 运输、由其推出的 `S_X[g]≥e^(−o(A))`、归一化谱逃逸、原 `g′` fixed-test 对完整 finite `q1` 的失败，以及独立 fresh/root 最终确认。这些必须保完整 finite Euler Gram inverse、raw norm 和原 physical 源，不以本稿替代。

本稿不称 `g′` polefree，不删完整 Γ/contact/所有 proper powers/双 pole，不给 Q 的负值或 RH 反例，不排其它 weights、signed/joint/primitive 或非局部修复，不改 whole4/5 负惯性 UPPER，也不完成长期 Goal。无新来源、PDF/章节、数值、pending process、STATE/Git/cadence 更改。

## 必要输入版本绑定

- `goals/contracts/C053-inverse-euler-growing-moment-and-normalized-escape.md`：5773 LF bytes；SHA256 `94a8d147ba05067678d56b691799ee3fac54f7bda8e719d272ce0c6c082de8d1`。以现场冻结文件为合同；本稿只消费其第3节对象及允许的等价物理边界方法。
- `reviews/2026-10-28/inverse-euler-filter-admission/root-admission-consumption-scope.json`：4146 LF bytes；SHA256 `cde3a40832cd010977ebfdb5565e6df409ce384a09c9316be18c512bc3427887`。status 为 `root-fresh-admission-closed-old-zero-and-one-c053-unpaid-proof-budget`；原 runtime1793085111／baseline0c4f，admission 不代数学证明。
- `reviews/2026-10-28/fixed-test-lower/common-sonin-vector-and-polynomial-domain.md`：16348 LF bytes；SHA256 `dcdf8e91b408423e3647f116f8bd72e040feaf24cf80f9b92db30d776398af85`。消费 actual raw Riesz、同一 K_a/酉 log map 和 H0 模板；不消费其明确未付的 raw O(1/t)。
- `reviews/2026-10-28/sonin-scalar-normalization/source-upper-and-tail-proof-audit.md`：10211 LF bytes；SHA256 `bab769113b4ce8c858dfd4b7a83dea6abd8808436a599d2206ea9a9bf0915fff`。仅对照固定 cosine 压缩/原范数角色；本稿不需其 gap1 completed E 公式，更不把 gap1 公式无声搬为 a=2。

本稿状态：当前任务 **terminal，局部证明闭合，待不同 fresh/root 消费**。
