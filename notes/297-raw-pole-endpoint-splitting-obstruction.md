# 297. 原始极点核的端点拆分障碍与补偿核参数界

状态：[N] 原始复极点核逐项 Cauchy 绝对求和发散；[T] 双端点补偿核的
参数一致界与高度尾界；[R] 经典零点计数；[O] 随算术尺度增长的真实有符号预算。
本篇是短辅助备忘，不是一篇新论文，也不声称机制新颖。

## 1. 对象、端点及与旧文的边界

记
\[
 d\mu_C(t)=\frac{dt}{\pi(1+t^2)},\qquad
 \tau_C|F|=\int_{\mathbb R}|F(t)|\,d\mu_C(t).
 \tag{1}
\]
固定 \(Y>2\)，令 \(L=\log Y\)、\(u_0=\log2\)，并取
\(\sigma'\in[1/2,3/4]\)、\(\rho=b+i\gamma\)、\(b\in[0,1]\)、
\(\gamma\ne0\)。定义未中心化的测试函数及两个复核
\[
 \begin{split}
 f_t(x)&=x^{-\sigma'}e^{-x/Y}\cos(t\log x),\\
 K_\rho(t)&=\int_2^Y x^{\rho-1}f_t(x)\,dx,\\
 I_\rho(t)&=\frac1\rho\int_2^Y x^\rho f_t'(x)\,dx.
 \end{split}
 \tag{2}
\]
这里没有 \(\cos-1\) 或质量中心项。一次分部积分恰给
\[
 I_\rho(t)=\frac{Y^\rho f_t(Y)-2^\rho f_t(2)}\rho-K_\rho(t).
 \tag{3}
\]
两端均不可删。若用实际显式公式，须将完整右端点与固定早段共同池化，
不能把(3)右边的两个无穷级数分别当作绝对可和级数。
实际全权原子端点的处理见
[285 §2](285-shallow-zero-deletion-and-finite-deep-response.md)；本篇的连续单核
并不替代那里的全权原子、早段与平凡零点项。

[282](282-rh-conditional-endpoint-preserving-response-bound.md)的逐项绝对
majorant 已隐含固定 \(Y\) 的全轴 \(L^1(\mu_C)\) 收敛：取实部 majorant
\(1\)，其证明给 \(Y^{1-\sigma'}\log^2(2+|t|)\) 量级，而该函数 Cauchy
可积；\(1-\sigma'\ge1/4\) 保证这里的参数一致性。因此该定性收敛不作为
本篇新成果。下面新增的明确审计点是原始核拆分障碍，以及保留单极点实部的界。

## 2. 固定尺度原始复核的绝对发散 [N]

### 命题297-A

每个固定 \(Y>2\) 都存在 \(c_Y>0\)、\(G_Y<\infty\)，使
\[
 \tau_C|K_\rho|\ge\frac{c_Y}{|\gamma|}
 \quad (|\gamma|\ge G_Y)
 \tag{4}
\]
统一适用于 \(b\in[0,1]\)、\(\sigma'\in[1/2,3/4]\)。常数允许依赖
\(Y\)，不声称当 \(Y\to\infty\) 或 \(Y\downarrow2\) 一致。

证明。置 \(a=b-\sigma'\)、\(h(u)=e^{au-e^u/Y}\)。取
\[
 t_0=\frac\pi{2L},\qquad c_0=\cos(t_0u_0)>0.
 \tag{5}
\]
上端 \(\cos(t_0L)=0\)，而下端不为零。全参数范围内
\[
 h(u_0)\ge m_Y:=2^{-3/4}e^{-2/Y},\qquad
 h(L)\le H_Y:=Y^{1/2}e^{-1}.
 \tag{6}
\]
取以 \(t_0\) 为中心的闭区间 \(J_Y\)，其正半长 \(\varepsilon_Y\) 满足
\[
 \varepsilon_Y\le\min\left\{
 \frac{t_0}2,\frac{c_0}{2u_0},
 \frac{m_Yc_0}{4LH_Y}\right\}.
 \tag{7}
\]
则在整个 \(J_Y\) 上，下端幅度至少 \(m_Yc_0/2\)，上端幅度至多
\(m_Yc_0/4\)。两次对 \(e^{i\gamma u}\) 分部积分给
\[
 K_\rho(t)=
 \frac{[e^{i\gamma u}h(u)\cos(tu)]_{u_0}^{L}}{i\gamma}
 +O_Y(|\gamma|^{-2}).
 \tag{8}
\]
余项在所述 \(b,\sigma',t\) 的紧参数集上一致：一阶边界导数及二阶导数
的积分均有共同上界。反三角不等式使边界分子的模至少
\(m_Yc_0/4\)，与两个复相位无关。因此充分大的 \(|\gamma|\) 时
\[
 |K_\rho(t)|\ge\frac{m_Yc_0}{8|\gamma|}
 \quad(t\in J_Y).
 \tag{9}
\]
积分即得(4)，例如可取 \(c_Y=\mu_C(J_Y)m_Yc_0/8>0\)。当 \(Y=2\)
核恒为零，这也是必须排除该端点的原因。\(\square\)

现在只对实际 Riemann zeta 的非平凡零点求和，重数计入。[R] 经典
Riemann--von Mangoldt 计数为
\[
 N(T)=\#\{\rho:0<\Im\rho\le T\}
 =\frac{T}{2\pi}\log\frac{T}{2\pi e}+O(\log T).
 \tag{10}
\]
可核查来源是 Hasanalizade--Shen--Wong,
[Counting zeros of the Riemann zeta function, Corollary 1.2](https://arxiv.org/pdf/2107.06506)。
这里只使用其蕴含的经典渐近与单位高度 \(O(\log(2+T))\) 上界，不使用或
宣称当前最优显式常数。Stieltjes 分部求和给，对每个固定 \(G>0\)，
\[
 \sum_{G<\gamma\le V}\frac1\gamma
 =\frac1{4\pi}(\log V)^2+O_G(\log V).
 \tag{11}
\]
故(4)严格推出
\[
 \boxed{\ \sum_\rho\tau_C|K_\rho|=\infty\ }
 \quad\text{对每个固定 }Y>2.
 \tag{12}
\]
这是逐个**复模式**取绝对值的结论。它不推出
\(\sum_{\gamma>0}\tau_C|2\Re K_\rho|=\infty\)，也不排除按共轭、
对称高度或其他已证明规则组织的条件收敛。式(8)的复模下界不能直接换成
实部下界；本篇不证明实际共轭配对后的发散。

## 3. 补偿核的统一实部、共振与高度界 [T]

### 引理297-B

取 \(Y\ge4\)，令
\[
 W=Y^{\max(a,0)},\qquad
 \eta=1+\min\{L-u_0,|a|^{-1}\},\qquad a=b-\sigma',
 \tag{13}
\]
其中 \(a=0\) 时最小值取 \(L-u_0\)。则有绝对常数 \(C\)，使
\[
 \tau_C|I_\rho|
 \le C W\,
 \frac{\log(2+(1+|\gamma|)\eta)}{|\rho|(1+|\gamma|)}.
 \tag{14}
\]
特别当 \(|\gamma|\ge1\) 时，可把分母换为 \(1+\gamma^2\)。此处
\(C\) 不依赖 \(Y,b,\sigma',\gamma\)，也没有假定 \(|b-\sigma'|\)
与零分离。

证明。将 \(h\) 及 \(h_1(u)=(\sigma'+e^u/Y)h(u)\) 在 \([u_0,L]\)
外延拓为零。\(h\le W\)，且其内部导数的符号至多改变一次，故包含两个
延拓跳跃的 \(TV(h)\le4W\)。乘数 \(\sigma'+e^u/Y\) 有一致有界的
上界和变差，所以 \(TV(h_1)\le CW\)。此外
\[
 \|h\|_1\le W\min\{L-u_0,|a|^{-1}\},\qquad
 \|h_1\|_1\le C W\eta.
 \tag{15}
\]
第一式在 \(a=0\) 按(13)解释；其余情形直接积分 \(e^{au}\)。因此若
\(\widehat h(v)=\int h(u)e^{ivu}du\)，并定义
\(\phi_\eta(v)=\min\{\eta,|v|^{-1}\}\)、\(\phi_\eta(0)=\eta\)，则
\[
 |\widehat h(v)|+|\widehat h_1(v)|\le C W\phi_\eta(v).
 \tag{16}
\]
对(2)直接求导，得到保留符号的精确式
\[
 I_\rho(t)=-\frac1\rho\int_{u_0}^{L}e^{i\gamma u}
       \{h_1(u)\cos(tu)+t h(u)\sin(tu)\}\,du.
 \tag{17}
\]
于是其模至多
\(CW(1+|t|)|\rho|^{-1}
 [\phi_\eta(t-\gamma)+\phi_\eta(t+\gamma)]\)。

所需的初等 Cauchy 积分为
\[
 \int_{\mathbb R}\frac{1+|t|}{1+t^2}\phi_\eta(t-g)\,dt
 \le \frac{C\log(2+(1+|g|)\eta)}{1+|g|}.
 \tag{18}
\]
由对称性先设 \(g\ge1\)。在 \(|t-g|\le g/2\) 上，前一权重为
\(O(1/g)\)，而 \(\int_{-g/2}^{g/2}\phi_\eta(v)dv
 \le C\log(2+g\eta)\)。在 \(|t|\le g/2\) 上，
\(\phi_\eta(t-g)\le2/g\)，权重的积分为 \(O(\log(2+g))\)。
剩余区域为 \(t<-g/2\) 或 \(t>3g/2\)，被积函数为 \(O(t^{-2})\)，
积分为 \(O(1/g)\)。这三个区域覆盖实轴，至多共享边界。
若 \(|g|<1\)，在 \(|t|\le3\) 上直接积分 \(\phi_\eta\) 得
\(O(\log(2+\eta))\)，其余区域仍由 \(t^{-2}\) 控制。
这证明(18)，代入(17)即得(14)。\(\square\)

### 推论297-C：实际零点的粗全谱尾界

对 \(Y\ge4\)、\(V\ge2\)，统一于 \(\sigma'\in[1/2,3/4]\)，
\[
 \sum_{|\gamma|>V}\tau_C|I_\rho|
 \le C Y^{1-\sigma'}\frac{\log^2(2V)}V.
 \tag{19}
\]
证明。求全谱粗尾时，不必在(14)中直接用 \(\eta\le1+L\)。利用
\(b\le1\)、\(1-\sigma'\ge1/4\)，可以一致地改用
\[
 \|h\|_1+\|h_1\|_1+TV(h)+TV(h_1)
 \le C Y^{1-\sigma'}.
 \tag{20}
\]
其中 \(L^1\) 由积分 \(e^{(1-\sigma')u}\) 控制，变差由上面的单峰及
乘积论证控制。故(16)--(18)允许取固定 \(\eta=1\)（调整绝对常数），给
\[
 \tau_C|I_\rho|\le
 C Y^{1-\sigma'}\frac{\log(2+|\gamma|)}{1+\gamma^2}
 \quad(|\gamma|\ge1).
 \tag{21}
\]
由(10)推出的单位高度计数求和，尾部至多
\(CY^{1-\sigma'}\sum_{n\ge\lfloor V\rfloor}
 \log^2(2+n)/(1+n^2)\)，从而得到(19)。有限低零点的
\(1/|\rho|\) 可单独处理；不存在用 \(1+\gamma^2\) 偷换任意趋零复
\(\rho\) 的一致界。\(\square\)

## 4. 晋级与停止边界

- [T，旧结论的接口说明] 对固定 \(Y\)，\(\sum I_\rho\) 在
  \(L^1(\mu_C)\) 中绝对收敛；这已由282的可积 majorant 隐含。
- [N] 与之相反，(12)禁止把实际原始复核级数和(3)的端点级数分别按逐项
  Cauchy 绝对和处理。这只排除该特定拆分方法，不排除有符号求和。
- [T] (14)保留单极点的实部大小、物理共振及跨 \(b=\sigma'\) 的损失；
  (19)给出可直接审计的有限到增长高度代价。它们不产生算术正性。
- [O] (19)没有证明随 \(Y\) 增长的尾部小于
  [294](294-pnt-envelope-gain-and-fixed-source-saturation.md)的交点尺度。
  固定有限极点包的小量也不是实际 \(\Lambda\) 整体的小量。
- [O] 289的多对数谱高度对应增长阶余核与中频四阶范数，不能直接改称本篇
  原始补偿核的全轴小尾。当前仍需真实有符号求和或更强的一致尾估计。

本篇未引入新的源模型，未声称 RH/GRH 推论，未将数值实验纳入证明链。
主代理与gap_exception_audit分别完整读取并独立复核全文，均PASS；包括小窗的统一端点下界、
三域积分、任意小 \(\rho\) 时保留的分母、粗谱尾与旧结论去重。
这属于内部复核，不是外部同行评审或新颖性确认。
