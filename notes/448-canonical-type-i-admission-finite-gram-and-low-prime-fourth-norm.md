# 448. 规范 Type-I 准入、有限比值 Gram 基线与低素数四范数

2026-10-07。状态：[T] 是下述固定 cell 的有限恒等式、无条件粗界及真实低素数压缩付款；
[T/R] 是明确规范无零／增长输入下的 Type-I、Type-II 前缀准入。
它们没有闭合原 signed response 的四阶常数，也没有提高简单临界线比例。

本稿承接 [446](446-uniform-prime-twists-on-the-original-gabor-frame.md) 和
238–241。区别三个问题：一个规范系数能否进入原算子；得到的界是否优于同域基线；
所得费用能否用于同一个完整四次迹。第一个问题的肯定答案不能代替后两者。

## 1. 版本、输入和两个物理对象

原 AF 窗、Fourier 约定、frame 和有限压缩来自
[Alpöge–Furman v2 §2](https://arxiv.org/html/2608.13637v2#S2)。
原 Montgomery–Vaughan 均值采用
[Hilbert's inequality, Corollary 3](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)。
两者是原始文献输入；本稿重算以下具体正规化和有限估计。

规范输入包沿用 [446](446-uniform-prime-twists-on-the-original-gabor-frame.md)：
固定 1/2<theta<1，所涉 primitive Dirichlet 全族在 Re s>theta 无零，
并有固定 gap 上的 uniform reciprocal、L 增长及 logarithmic control，
记全 primitive conductor 与 deleted Euler radical。
原 OpenAI September-30 paper.tex 固定于
[adc7f1241b42e322a6451854ab7e4b4c146bf78a](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)，
canonical LF SHA256 为
42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3。
此输入包 [R] 不在本稿独立认证；其结果允许 theta=7/8。
降低 theta 时须另引用对应边界证明的完整前件。

设 X=T/(2pi)、L=log X，原 AF 维数为 D=floor(XL)，
tau_k=2pi X+2pi k/L，0<=k<D。
238 的 round(XL) 也可用于下面固定 cell 的估计，但每次保留所选 D 自己的核；
两个不同整数维数的精确核不被认作恒等。

第一对象是 238 的 ratio synthesis。固定 0<c<C，Y=X^(3/4)，
两侧 atoms 满足 cY<=a,b<=CY、(a,b)=1。所有通道预先使用同一 mask m(a,b)，
0<=m<=1，包含原 factor/aperture cuts，在 distinct-base prime-power support 上等于原 mask。
规范移线还要求 fixed-b 切片是固定有限个区间，且原 feature 的 Hilbert BV 一致有界。
有限 Gram 基线本身不要求 mask 的 BV。

令 H=L²(R/LZ,dz/L)，原六窗交叉来自
\[
 F_{a,b}(z)=\phi(z+\log(a/b))\phi(z)\phi(\log b-z)^2,\qquad \|F_{a,b}\|_H\le1.
 \tag{1}
\]
同一 factor cell 内 log(a/b) 的跨度为 O(1)。
原有限 cosine 核准确写成
\[
 K_{XL,D}(Xv)=D^{-1}\sum_{k=0}^{D-1}
 \cos[(2\pi X+2\pi k/L)v].
 \tag{2}
\]
首参数不是 X；不能遗漏 L 或改用极限 sinc。

第二对象是 AF 原有限 frame 在整个实 height 轴的压缩，见 §5。
固定 cell 的 Gram 与整个压缩的四范数是不同命题，各自保留原窗、常数及范围。

## 2. 规范 Vaughan 通道、自然 mask 和 ghost 极点

取 U=V=Y^(1/4)，按原 one-factor identity 定义
\[
 J=\mu_{\le U}*1*\Lambda_{>V},\quad
 I=J+\Lambda_{\le V},\quad II=\Lambda-I.
 \tag{3}
\]
high cell 中 a>V，故 I(a)=J(a)。阈值 UV<Y 没有使整个 II 通道恒零：
若 n=pq、p,q>max(U,V) 是不同素数，则 J(n)=log(pq)、II(n)=-log(pq)。
该例只在 atom 被实际 mask 保留时适用，不声称每个任意空 mask 都有非零通道。

固定 b 的 coprime extension chi_b(n)=1_(n,b)=1 完全乘性。因此
\[
 {\cal J}_b(s)=M_{U,b}(s)L_b(s)[D_b(s)-D_{\le V,b}(s)],
 \tag{4}
\]
\[
 M_{U,b}=\sum_{r\le U}\mu(r)\chi_b(r)r^{-s},\quad
 L_b=\zeta(s)\prod_{p\mid b}(1-p^{-s}),\quad D_b=-L_b'/L_b.
\]
这是实际 truncated convolution；没有给任意 divisor 列配上 1/L。
rad(b)<=CY，所有 q_eff、U、V、height 的多项式范围先固定。

固定 theta<sigma_0<sigma<1。shifted Perron 直接针对
mu(n)chi_b(n)n^(-it)，随后 Abel 只微分实权 n^(-sigma)，给
\[
 M_{U,b}(\sigma+it)\ll_{\rm gap,\epsilon}
 [q_{\rm eff}(3+|t|)]^\epsilon
 \tag{5}
\]
且对 U 统一。不能先估 untwisted 前缀，再微分 n^(-it) 而漏掉 |t|。
同理，shifted Lambda 前缀和实权 Abel 保留
\[
 D_{\le V,b}(\sigma+it)=
 \frac{V^{1-\sigma-it}}{1-\sigma-it}
 +O_{\rm gap}(\log^2[2q_{\rm eff}(3+|t|)]).
 \tag{6}
\]
这里的 chi_b 是 principal punctured presentation；有限 Euler 删除不改变留数 1。
一般固定角色时，主项仅在 principal 情形出现。由规范 [R] 得
\[
 |{\cal J}_b(\sigma+it)|\ll
 [q_{\rm eff}(3+|t|)]^\epsilon
 \left(1+\frac{V^{1-\sigma}}{1+|t|}\right).
 \tag{7}
\]
低 height 峰仍在式中。

对 x~Y、tau~X 的 sharp prefix，取 floor(x)+1/2 的原整数 Perron，
移至 sigma-1/2，初始 coefficients 由 |J(n)|<=d(n)log n 控制。
截断 height 为 q_eff、X、Y、U、V 的固定充分大多项式。
峰的费用是
\[
 \int_{-H_0}^{H_0}\frac{dt}{(1+|t|)(1+|t-\tau|)}
 \ll \frac{\log(2H_0)}X.
 \tag{8}
\]
把 t 在 0、tau 附近的两块及其余尾分别估计即可；horizontal joins 和整数 endpoint
误差由先固定的 polynomial order 吸收。因此
\[
 \sum_{n\le x}J(n)\chi_b(n)n^{-1/2+i\tau}
 ={\cal P}_b(x,\tau)
 +O\!\left(Y^{\sigma-1/2}X^\epsilon
       [1+V^{1-\sigma}/X]\right).
 \tag{9}
\]

principal ghost completion 产生 double pole。置
r_b=prod_(p|b)(1-1/p)，A_b=r_b M_(U,b)(1)，
B_b=r_b[M'_(U,b)(1)-M_(U,b)(1)D_(<=V,b)(1)]。准确留数为
\[
 {\cal P}_b=x^{1/2+i\tau}
 \left\{ A_b\left[\frac{\log x}{1/2+i\tau}
                  -\frac1{(1/2+i\tau)^2}\right]
             +\frac{B_b}{1/2+i\tau}\right\}.
 \tag{10}
\]
因为 L_bD_b=-L_b' 的 simple-pole 系数为零，B_b 没有额外 Laurent 常数。
|A_b|、|B_b| 分别至多 log(2U)、log²(2UV)，故留数
O(sqrt(Y) X^(-1)log^C X)。ghost 主项不能删除。

## 3. 条件前缀进入原 finite Gram，但不是较强预算

对 r=I,II,Lambda，定义实际同 mask 合成及同 atom reference
\[
 S_{r,k}=\frac1{4\pi^2}\sum_{a,b}
 m(a,b)\frac{r(a)\Lambda(b)}{\sqrt{ab}}
 e^{i\tau_k\log(a/b)}F_{a,b},
 \tag{11}
\]
\[
 G_{rs}=D^{-1}\sum_k\langle S_{r,k},S_{s,k}\rangle_H,\quad
 A_{rs}=\sum_{a,b}\frac{m(a,b)^2r(a)\overline{s(a)}\Lambda(b)^2}
 {(4\pi^2)^2ab}\|F_{a,b}\|_H^2.
 \tag{12}
\]
逐 atom 有 S_Lambda=S_I+S_II，所有 composite ghosts 留在同一 mask 中。
fixed-b 的 Hilbert BV 将 (9) 接入 (1)；此后对 b 仅用
sum_(b~Y) Lambda(b)/sqrt(b)<<sqrt(Y)。遂
\[
 \|S_{I,k}\|_H\ll Y^\sigma X^\epsilon+(Y/X)\log^C X.
 \tag{13}
\]
完整 Lambda 的 generating function D_b 有 simple pole，
其前缀主项是 x^(1/2+i tau)/(1/2+i tau)，同样付款给 S_Lambda 的 (13)。
两次 canonical a-sum 各自完成后，精确相减得到 S_II 的同界。
没有把已经依赖 b 的 a-error 再作 b 的规范相消。

故任意小 epsilon 下，所有这些固定 cell 通道有
\[
 |G_{rs}|\ll_\epsilon X^{3\theta/2+\epsilon}.
 \tag{14}
\]
theta=7/8 给 21/16；已提交 69999/80000 论文的明确输入包给
209997/160000。式 (14) 量化单变量移线对 theta 的依赖。
它比下一节同域无条件基线弱，不能称新的 Gram 算术节省。

## 4. 约化比值的无条件有限 Schur 基线

不同 coprime atoms 的 log ratios s_i 互异，且
\[
 |s_i-s_j|\ge |ad-bc|/\max(ad,bc)\ge (C^2Y^2)^{-1}=:\delta_Y.
 \tag{15}
\]
跨度 O(1)<L/2，故几何级数给所选原有限核
\[
 \left|D^{-1}\sum_{k=0}^{D-1}e^{2\pi i k v/L}\right|
 \le\min\{1,[D|\sin(\pi v/L)|]^{-1}\}
 \ll\min\{1,(X|v|)^{-1}\}.
 \tag{16}
\]
carrier 模为 1；取实部也不增加界。排序后每侧第 j 个近邻距离至少 j delta_Y，
总 atom 数 O(Y²)，所以 row absolute sum
\[
 B_{X,Y}\ll1+(Y^2/X)\log(2Y).
 \tag{17}
\]
对原 feature 用 |<F_i,F_j>|<=||F_i||||F_j|| 及
2v_i v_j<=v_i²+v_j²，得到 G_rr<=B_(X,Y) A_rr。
这里没有假设 features 正交。

卷积直接给 |J(n)|<=d(n)log n、|II(n)|<=(d(n)+1)log n。
divisor bound 与 sum_(b~Y) Lambda(b)²/b<<log²(2Y) 得 A_rr<<_epsilon X^epsilon。
两个 Hilbert Cauchy 分别控制 G_rs 和 A_rs，因此
\[
 \boxed{|G_{rs}|+|G_{rs}-A_{rs}|\ll_\epsilon X^{1/2+\epsilon}.}
 \tag{18}
\]
这是有限 spacing/Schur 机制，不依赖零自由输入。它仍远大于 raw o(L^4)；
不把充分粗界当作必要条件，也不把共同 shell centering 的额外 mass projection 自动加进来。
若取消 coprime，须先合并重复 ratios；若跨 cells 使跨度达到 L，须另付原 grid alias。

## 5. 原 AF 完整低 Lambda 压缩的四范数

令 Z<=sqrt(X)，Q_Z(t)=sum_(n<=Z) Lambda(n)n^(-1/2+it)，保留 sharp cutoff。
Q_Z² 的 coefficients c_m 支持 m<=Z²。不同 prime bases 只有两种排列；
同一 prime 的所有额外碰撞由
sum_p(log p)^4 sum_(r>=2)(r-1)^2 p^(-r)<infinity 支付。因此
\[
 \sum_m|c_m|^2=2\left(\sum_{n\le Z}\Lambda(n)^2/n\right)^2+O(1)
 \ll\log^4(2Z).
 \tag{19}
\]
普通 Dirichlet 多项式均值给任意长度 O(X) 的 J
\[
 \int_J|Q_Z(t)|^4dt\ll(X+Z^2)\log^4(2Z).
 \tag{20}
\]
此处仍保留 off-diagonal 费用 Z²。

令 f_k(t)=hat(phi)(t-tau_k)，U_F z=sum z_k f_k，
F=U_F/sqrt(2pi L)，a_L=||phi||²/L 上下有固定正界。
原 support、Plancherel 和 critical grid 给 F*F<=1 及
sum_(k in Z)|f_k(t)|²=a_LL²。实际低 Lambda 矩阵为
\[
 P_{\le Z}=\frac{2\pi}{a_LL}F^*M F,\qquad M=-\pi^{-1}\Re Q_Z.
 \tag{21}
\]
对 F*MF 的每个单位 eigenvector，用 scalar x^4 Jensen，
将缺失质量 1-||Fv||² 放在 0，得
Tr(F*MF)^4<=Tr(F*M^4F)。这不需要 x^4 是 operator-convex。
finite frame 的点态平方和至多 a_LL²，故正积分在 J 内的费用是
8/(pi a_L³ L³) integral_J |Q_Z|^4。

取 J=[T/2,3T]。J 外保留 |Q_Z|<<sqrt(Z)，原 C² Fourier 尾给
sum_k integral_(Jc)|f_k|²<<D X^(-3)。正规化后得到
\[
 \boxed{\operatorname{Tr}P_{\le Z}^4\ll
 N\left(\frac{\log(2Z)}L\right)^4(1+Z^2/X)
 +\frac{Z^2}{X^2L^4},\qquad N\asymp XL.}
 \tag{22}
\]
正积分的 J/Jc 分割不是任意矩阵四迹的无 cross-term 分拆。
取 Z=exp(sqrt(L))，则 ||P_(<=Z)||_4=o(N^(1/4))，为无条件结果。

若剩余完整 Hermitian response H_> 另有 ||H_>||_4=O(N^(1/4))，
非交换 telescoping 与 Schatten Hölder 给
\[
 |\operatorname{Tr}(H_>+P_{\le Z})^4-\operatorname{Tr}H_>^4|=o(N).
 \tag{23}
\]
因此低通道可在同一完整四迹中以 o(N) 费用处理；H_> 的前件仍开放，
不从二矩、(14) 或 (18) 推出。固定 Z=X^rho 仅有未优化的 O(rho^4N)，不是新比例常数。

## 6. 真正剩余的联合算术问题

两侧 primitive mask 下 h=ad-bc=0 恰为同 atom reference。
固定 (a,b)=1、h!=0，所有整数解准确为
d=d_0+bj、c=c_0+aj、ad_0-bc_0=h。原余项含
\[
 \sum_j\Lambda(d_0+bj)\Lambda(c_0+aj)\,
 {\cal W}_{a,b,h}(j)\,
 K_{XL,D}\!\left(X\log\frac{a(d_0+bj)}{b(c_0+aj)}\right).
 \tag{24}
\]
W 保留 (abcd)^(-1/2)、原 six-window 和 masks；外层的 numerator coefficients 也保留。
balanced cell 中每个 h 的 j 区间只有 O(1) 个整数，resolution core 为
|h|~Y²/X；全部 tail 和 carrier 仍在实际求和中。
一个规范 Lambda 的 PNT 不提供两个 linear prime forms 的联合渐近。

沿 [241](241-divisor-scale-separation-no-go.md) 的准则，
必须在实际 determinant/frequency fiber 内先合并全部 divisor blocks，再估计。
当前目标是原 physical vector 的 G-A 净预算，以及共同 centering、跨 cells 与 alias 的联合账本；
不能把各通道的 (18) 独立相加接入零点比例。

完整推导及独审：
[规范准入报告](../reviews/2026-10-07/hybrid-response-type-i-admission-and-type-ii-gap.md)、
[有限基线](../reviews/2026-10-07/hybrid-finite-ratio-gram-baseline.md)、
[全文复核](../reviews/2026-10-07/type-i-and-low-lambda-full-response-review.md)。
本稿校正粗界的成果定位并保存已付接口；未给出新比例、完整四阶常数、外部 kernel 或 RH 证明。
