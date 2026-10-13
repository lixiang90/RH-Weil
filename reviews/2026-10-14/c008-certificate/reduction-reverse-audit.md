# C008：固定 v2 frequency reduction 的独立逆审

2026-10-14。只审固定原件
`literature/background/zhu-2608.24827v2-src/main.tex`，主要为
207–238、790–1052、2440–2462；另核脚本
`scripts/c008_pointwise_envelope.py` 与其原有理结果。
恢复了 AGENTS、README、STATE、check/show、Goal、C008 与 D20261014E。
实际 HEAD 为 `4377e70b35dfe1da6ce5957a31e8c9b0ba01824e`；主代理正在更新
C008 状态，旧 Goal complete 不重开。本逆审不改 STATE/cadence/git。

## 1. 结论与消费范围

实际偶实源的频率切分及两块估计是合法的，补全显式尾界后确能把
无限维问题归约为一个有限矩阵及独立误差账本。原文并非遗漏整个补空间。
但原六文件源包没有 §17 所称矩阵、Cholesky 因子、账本或
`verify_certificate.py`；因此本次不能消费 support 1.6 的正性数字、
奇偶隔离或 simple-ground-state 声明。

原文存在三个可直接定位的可修错误：阈值偏移渐近量级、矩阵条目界的
积分因子、quadrature 的向上数值舍入。它们本身不推翻固定窗证书，
其可修余量仍远小于所声称的正间隙。另有一个实质量词错误：
`sup P_L=A_L` 仅证明**常数上包络**最优，不能推出所有随 t 变化的
pointwise 上包络的阈值最优。后者已有不使用零点的精确有理反例，见 §5。

## 2. 原对象、频率切分及有限归约

原文 181–192、513–528、536–549 定义的对象为

\[
Q(f)=2F(i/2)^2+(2\pi)^{-1}\int_{\mathbb R}|F(t)|^2\Psi_L(t)dt,
\quad \Psi_L=\Re\psi(1/4+it/2)-\log\pi-P_L(t),
\]

实偶 f 支持于 [-L,L]，F 使用无归一化 Fourier 变换。
Gamma 是完整 `Re psi−log pi`；prime comb 的系数是
`2 Lambda(n)/sqrt(n)`，pole 是偶实源上的正 rank-one。
Parseval 给 `(1/pi) integral_0^infinity |F|²=||f||²`。
对自然对数加权 form domain 原式有限；一般 L² 源可按闭型/扩展值解释。
R 本身是整个偶实 L² 上的有界型。不能仅凭此节改为奇源、复源或删除 pole。

792–817 的 Binet/shift 论证常数成立：
`1/(15t)+7/(2t²) <=1/t` 的临界点正好为 t=15/4。
由于 beta>0 已强制 T>2pi，适用域没有缺口。
886–896 的高频下界与 R 身份成立。C 是有界紧压缩 multiplier，
不是声称完整 Q 本身有界或由一个有限矩阵给出全部谱。

902 的 spherical-Bessel 界可由 Rodrigues/Poisson 加权积分证明。
令

\[
d_n=2\sqrt{L(n+1/2)},\quad
b_n=d_n(TL)^n/(2n+1)!!,\quad c_n=\min(d_n,b_n),
\quad M=\sup_{[0,T]}|\Psi_L-\beta|.
\]

则应使用

\[
|C_{nm}|\le (TM/\pi)c_nc_m. \tag{A}
\]

905–906 所写条目界漏了 `T/pi`，不能从积分定义直接推出。
其只在 n 一侧使用 forbidden-region 因子、另一侧仅用 d_m 的版本，
也不能对无限 tail 的 m 求和：`sum d_m` 发散。
修复是对两个指标都用 (A)，不是把有限头 N 项的说明套用无限 D 行。
922–928 的 `lambda_min >= min(lambda_min A,lambda_min D)−||B||`
是正确的 Hilbert 双块不等式；有限头/无限尾量词合法。

## 3. 尾与 pole：修复后固定参数仍有充足余量

独立普通高精度验算仅检查解析上界的大小，不代替原 PD 证书。
L=4/5、T=200、偶阶头 0..398、尾从400开始：

* A=2.9419735252236204555…，beta=0.5134667749150707384…；
* b400=4.2615246152364793…e−108，符合原文1006；
* `sum_tail b_n <4.438e−108`；比值
  `b_(n+2)/b_n=(TL)^2 sqrt((n+5/2)/(n+1/2))/((2n+3)(2n+5))`
  在 n>=400 单调下降，几何界可支付整个无限和；
* `sum_head d_n <4762`。取 M=20，(A) 给
  `||C_tail|| <2.41e−212`，Schur 两因子给
  `||C_head,tail|| <2.29e−102`。

故即使补漏的积分因子，所称 `epsilon_D,epsilon_B <=1e−100`
在该固定偶实参数上仍有解析可行余量；没有据此找到实际负矩阵。
这些数值仅为以上公式验算；若正式导入数字证书，仍应对比值、求和、M
实施向外包围。

pole 必须在 B 中计入，不能仅因正 rank-one 而整项丢掉。
设 p_n=<T_n,cosh(x/2)>，偶 n 的修改 Bessel 表示给

\[
|p_n|\le d_n e^{L/2}(L/2)^n/(2n+1)!!.
\]

因此 `||p_tail||` 有同类几何界，`||B_pole||=2||p_head||||p_tail||`。
D 中的 `2p_tail p_tail*` 为正，可以直接舍去，故 epsilon_D 不必为其
支付负费用。固定参数 pole400 的上界远小于1e−390，原文1007的量级安全。
原文908、1007仅说 pole decay，没有完整列出这一 B 费用公式；
正式全源证书必须支付它。没有发现 pole 尾能推翻所留1e−100余量。

另：207–238 的定理上下文是实偶源，232 的简写“all f”应保留这一限定；
奇源负 pole 必须另行审查，不能由本节的正 pole 论证自动继承。

## 4. Quadrature 与有限证书的误差边界

980–1002 的 analytic extension 正确：取两个 digamma 的 half-sum，
不把实部当复解析函数。宽1/4面板的半宽1/8，rho=6.55 对应 ellipse
竖半轴 `(1/8)(rho−rho^-1)/2=0.399833015…<0.4`，因此确在最近
digamma 极点 ±i/2 以内。Poisson 的 `|j_n(z)|<=exp(|Im z|)` 正确。

取最大 n,m=398、M_symbol=20，原文自身公式给

\[
M\le 4(0.8)(398.5)e^{0.64}20=48367.84834579…;
\]

\[
4M\rho/((\rho-1)(\rho^{64}-1))=1.31559397794…\,10^{-47}.
\]

故未缩放公式不能向上写成 `<=1.3e−47`、`800*=1.03e−44`、
`200*800*=2.06e−42`；安全未缩放数应略大于
1.316e−47、1.053e−44、2.106e−42。
但实际面板积分还乘半宽1/8；保留此缩放后原文所列预算反而宽裕。
这属于可修的舍入/缩放说明，不构成8.9e−18的反证。

`|Psi−beta|<=20` 的复 ellipse 界在996被直接断言，源包没有原向外
证明或账本。它需独立支付，不能用实轴采样代替。当前逆审确认了
ellipse 几何和 Bessel 部分，未认证该复域最大值。

pole quadrature 亦可不用模糊 ellipse 口号：Gauss320 对次数<=639
多项式精确，头最大 n=398 时，与 cosh 的 Taylor 多项式至240阶相乘
仍精确。余项可用 `exp(.4)*.4^242/242!` 及正权重支付，远小于1e−40。
但 leading-block 账本还须支付 digamma/Bessel/Miller recurrence 的
数值评价、所有求和与矩阵构造 roundoff，不能把 quadrature 离散误差
独自认作 `||A−Atilde||` 的完整误差。

1019–1029 的 residual lemma 本身成立：对称 residual 的 spectral norm
不超过其 induced infinity norm，PSD 的 LL* 给 Weyl 下界。
前提是 residual、product slack 和输入矩阵误差都是真正向外包围；
“same floating arithmetic”或 mpmath 工作精度本身不支付这些前提。
2440–2462 明确说附件是证明组成部分，六文件源包实际只有 tex、README、
四张图，没有所需矩阵/verifier。故 Cholesky succeeds、r、s、原PD、
完整8.9e−18数字均继续 cited/unconsumed。不能借本逆审制造替代矩阵。

1190–1194 的 nonorthonormal Householder frame 还有独立费用。
精确 PSD 时 full rank 确实足够给 codimension-one 子空间的 min–max；
但如果实际仅取得
`H*(M−sI)H >= −delta I`，则在 `range H` 的运输下界是
`s−delta/lambda_min(H*H)`，不能省略 Gram frame 下界。
full rank 只说该数为正，不能给有效量化；将 H 任意缩小即可使一个
真实负方向的 restricted residual 任意小。因此 frame slack 的完整
账本必须含 Gram 下界（或一个经认证的近正交界）。已读主笔记536，
其将此列为未付预算的分类正确，不把 full rank 单独消费成数值谱隔离。

214 的阈值偏移还有明确渐近笔误。若 T0 为 beta=0 的根、
T1=2pi exp A，则 `T0 log(T0/T1)=1`，展开得

\[
T_0-T_1=1-(2T_1)^{-1}+O(T_1^{-2}),
\]

不是 `O(T1^-1)`。固定 .8 时 delta=0.995847726788…，与原文
120.1 对119.1的例子一致，错误不影响 T>T1 的必要性。

## 5. 宽泛 pointwise barrier 已被精确反例否定

819–841 的 constant optimum 保留：正系数给 P<=A，t=0等号；
连续 Kronecker/Weyl 及 log primes 的 Q 线性独立还给任意高频的
sup P=A。有限 prime powers 的同素数相位约束不改变上最大值。
843–862 对 Aeff 的 sign 纠错也正确。

但上述 sup 不给任何指定有限 t 区间的上界等于 A，更不能把“任意
高频可近对齐”变成“在门槛 T1 的紧邻一定近对齐”。
415–416、443–449、2298–2302、2408–2410 使用更宽的
“all pointwise bounds/envelopes”量词，超出了819–828确实证明的
`P_L(t)<=C` 常数类。

原有理脚本给最便宜反例，无任何零点、矩阵或 RH 前件：

\[
L=4/5,\quad \Psi_L(t)\ge1/200\quad( |t|\ge118 ),
\qquad T_1=2\pi e^{A_L}>118.
\]

在118..121用实际 prime powers2,3,4的随 t 上包络，121以上用原
constant mass envelope。独立只读重算了30个面板、全部Fraction
端点及已保存JSON，一致 PASS：panel最低下界>1.658814839，
121以上粗界起点>0.00767549115。实际使用的统一 beta 仅为1/200。

具体向外性已核：

* `log_bounds` 使用2atanh正项级数，尾
  `2z^(2m+1)/((2m+1)(1−z²))` 是合法几何上界；
* Machin `pi=16 atan(1/5)−4 atan(1/239)` 的交替夹界及负系数方向正确；
* isqrt 给 sqrt(n) 的上下界，正系数取 lower log/upper sqrt 与相反者；
* cosine 使用40阶偶 Taylor，即41阶 Taylor 的42阶 Lagrange 余项；
  exact检查了所有 |y|<=16/5，最大约3.082735806；
* nearest-period k 是任意选定整数即可，实际全为13..27。
  Lipschitz费用含面板半宽、log常数半宽和2k*pi半宽，全部向外；
* 余弦上界负时必须乘 coefficient lower；脚本正确处理，实际有34项
  负 upper cap，未偷用正系数 upper；
* base 取118与pi upper，-1/118；其后单调性合法。tail取121并减 Aupper。
  `log(118/(2pi))<A` 用 pi lower 对左侧作 upper，正确证 T1>118。

三组 prime powers 恰是支持窗内项：`log4<1.6<log5`；脚本这一对象识别
采用已知初等严格界，不含素数尾遗漏。显示用float不参与任何assert。
我仅导入其纯函数并独立重算，不调用会覆盖JSON的 main。

因此广义 pointwise “threshold cannot be lowered”是明确假命题，
不仅是附件不可验证。constant-mass 的 T1 barrier 与这种特定归约的
成本估计仍保留。反例不证明任意成长L的复杂度降阶，不给全窗Q正性，
不排除真正 signed/coupled certificate 另有成本障碍。

## 6. 本轮瓶颈与下一消费条件

新增独立输入是宽量词 pointwise threshold 的精确反例，以及可核的
tail/pole修复公式。没有新增实际 Weil 正性或最低态来源。
核心有限证书 bottleneck 未消除：原 leading matrices/factors/verifier、
完整向外误差账本，及奇偶/simple对应的无限补空间预算仍未取得。
这些附件未支付时应精确止损，不能扩 N 或把普通 Cholesky 冒充证书。
唯一可继续动作是核原附件的实际可得性及其完整误差/谱隔离对象；
若无法取得，保存缺失范围、上述明确量词反例与重准入条件。
本次不新计独立研究轮，也不改变历史 Goal 完成判断。
