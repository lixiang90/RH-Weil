# 300. 分离完整端点的全轴复模误差与临界日程

日期：2026-09-06。B1z 亚纯接口周期第3轮；实际完成候选的日程研究。
状态：[T] 初等核的变差、Cauchy 积分与完整端点代数；[R] 经典显式公式、
零点计数及 Hadamard 展开；[T] 算术端点修正与共尾小端点整数；
[C/RH] 实际全轴复模误差、两项负迹分类及真实全谱的临界渐近。
本篇闭合[298 §6](298-actual-critical-window-and-fast-shift-obstruction.md)
所列的 RH 条件误差候选，不将条件结果当作无条件算术输入。

## 1. 实际对象、端点与范数

令 \(\psi(x)=\sum_{n\le x}\Lambda(n)\) 右连续，\(\Lambda(1)=0\)，
所有素数幂端点取完整权。以下允许实数 \(Y\ge4\)，素数幂与连续项都截在
同一 \(Y\)，并保留同一 Abel 权。记
\[
 E(x)=\psi(x)-x+1,\quad E(1)=0,\qquad
 L=\log Y,\quad 0<\delta\le\tfrac14,\quad q=\delta L,
 \quad \sigma=\tfrac12+\delta,\quad s=\sigma+it,
 \quad w_Y(x)=x^{-s}e^{-x/Y}.
 \tag{1}
\]
为避免与 \(E(x)\) 混淆，下文记 \(\varepsilon=e^{-q}=Y^{-\delta}\)。
采用[293 §5](293-poisson-transport-and-right-shifted-record-currents.md)
已经独立核对 Poisson/germ 条件的实际候选：
\[
 \begin{split}
 G(s)&=\frac1s-\frac12\log\pi+
              \frac12\frac{\Gamma'(s/2)}{\Gamma(s/2)},\\
 D_Y(s)&=\sum_{n\le Y}\Lambda(n)w_Y(n)-\int_1^Yw_Y(x)\,dx,\\
 F_Y^\sharp(\delta+it)&=G(s)-D_Y(s).
 \end{split}
 \tag{2}
\]
不额外加入 \(1/(s-1)\)，也不删除 Gamma 项或重新缩放实际迹。规范为
\[
 d\mu_C(t)=\frac{dt}{\pi(1+t^2)},\qquad
 \tau_C|H|=\int_{\mathbb R}|H(t)|\,d\mu_C(t),\qquad
 \kappa_Y(\delta)=\int_{\mathbb R}
                 (\Re F_Y^\sharp(\delta+it))_-\,d\mu_C(t).
 \tag{3}
\]
第4节估计的是复函数差的模，而不只是实部差，也不是未加权积分或二阶矩。
第5节分类另要求 \(q\ge1\)；不把该限制偷偷加到第4节，也不擅自将
第5节扩至 \(q<1\)。

## 2. 两个完整端点与无限补偿公式

### 2.1 实际有限恒等式 [T/R]

取 \(u_0=\log2\)，并置
\[
 C_E=1-\frac{\zeta'(0)}{\zeta(0)},\qquad
 T_0(x)=-\tfrac12\log(1-x^{-2}),\qquad
 D_{12,Y}(s)=\Lambda(2)w_Y(2)-\int_1^2w_Y(x)\,dx.
 \tag{4}
\]
对每个非平凡零点 \(\rho\)，计重数，定义
\[
 \begin{split}
 I_\rho^Y(s)&=\frac1\rho\int_2^Yx^\rho w_Y'(x)\,dx,\\
 B_Y(s)&=D_{12,Y}(s)-w_Y(2)E(2)
       -C_E\{w_Y(Y)-w_Y(2)\}-\int_2^YT_0(x)w_Y'(x)\,dx.
 \end{split}
 \tag{5}
\]
完整 Stieltjes 分部积分及普通积分内的显式公式给
\[
 \boxed{\quad
 D_Y(s)=e^{-1}Y^{-s}E(Y)+B_Y(s)+\sum_\rho I_\rho^Y(s).
 \quad}
 \tag{6}
\]
这是[285 §2](285-shallow-zero-deletion-and-finite-deep-response.md)及
298-(9)--(14)的未减包版本。为说明端点约定，先拆 \((1,Y]\) 为
\((1,2]\) 与 \((2,Y]\)。只在后一段的普通积分中使用几乎处处的
\(E(x)=-\sum_\rho x^\rho/\rho+C_E+T_0(x)\)；先固定 \(Y,s\)，再令
对称截断高度趋于无穷。282/285中显式公式截断误差的支配收敛证明适用。
积分后的一次振荡分部积分给高零点 \(O_{Y,s}(|\gamma|^{-2})\)，所以
补偿和在紧 \(s\) 集局部一致绝对收敛。\(n=2\) 的完整原子仅在
\(D_{12,Y}\) 首项出现一次；没有在端点上把 \(\sum Y^\rho/\rho\)
当作绝对收敛级数。

因 \(T_0'(x)=-1/[x(x^2-1)]\)，(5)等价于
\[
 \begin{split}
 B_Y(s)={}&D_{12,Y}(s)
 +(C_E-E(2)+T_0(2))w_Y(2)\\
 &-(C_E+T_0(Y))w_Y(Y)+\int_2^YT_0'(x)w_Y(x)\,dx.
 \end{split}
 \tag{7}
\]
这个写法保留两端，同时避免用 \(|s|\) 去粗估平凡零点部分。

### 2.2 无限补偿与 Euler 开集识别 [C/RH]

定义 \(D_{12,\infty}=\Lambda(2)2^{-s}-\int_1^2x^{-s}dx\)，并令
\[
 \begin{split}
 B_\infty(s)&=D_{12,\infty}(s)
 +(C_E-E(2)+T_0(2))2^{-s}
                  +\int_2^\infty T_0'(x)x^{-s}dx,\\
 I_\rho^\infty(s)&=-\frac{s}{\rho}\int_2^\infty x^{\rho-s-1}dx
                 =-\frac{s\,2^{\rho-s}}{\rho(s-\rho)}.
 \end{split}
 \tag{8}
\]
第二行的积分先在 \(\Re s>\Re\rho\) 使用。假设 RH 后，它对所有
\(\Re s>1/2\) 均成立；\(\sum I_\rho^\infty\) 在此半平面的紧集上
局部一致绝对收敛，因为高处为 \(O_K(|\gamma|^{-2})\)。
\(B_\infty\) 在该半平面全纯，故可以先在 \(\Re s>1\) 识别
\[
 \boxed{\quad
 G(s)-B_\infty(s)-\sum_\rho I_\rho^\infty(s)
                         =\frac{\xi'}{\xi}(s),
 \qquad \Re s>\tfrac12\quad\text{在 RH 下}.
 \quad}
 \tag{9}
\]

这里不需要先引用 RH 的点态 PNT 误差来丢弃无限端点。具体地，在 Euler
开集对 \(x^{-s}\) 使用(6)的同一无 Abel 权版本，令其完整截断端点
\(X\to\infty\)。初等界 \(|E(X)|=O(X\log(2X))\) 已给
\(X^{-s}E(X)\to0\)。对紧 \(\Re s>1\) 集，利用 \(\Re\rho<1\)，
每个积分尾恰为
\(-sX^{\rho-s}/[\rho(s-\rho)]\)，其绝对和
\(O_K(X^{1-\Re s})\to0\)；低零点有限，高处由 \(\gamma^{-2}\) 求和。
将(7)中的权也换成 \(x^{-s}\)，相应的有限补偿项同样趋于
\(B_\infty\)。于是 Euler 域内
\(B_\infty+\sum I_\rho^\infty=-\zeta'/\zeta-1/(s-1)\)。
标准 \(\xi\) 的完成恒等式证明(9)在该开集成立；RH保证等式两边在
\(\Re s>1/2\) 全纯，恒等定理遂给全部该半平面。没有对未知的无权
端点级数单独作绝对求和。

此外，(7)--(8)直接给无条件的一致有限早段界
\[
       |B_Y(s)-B_\infty(s)|\le C Y^{-\sigma},
       \qquad \sigma\in[1/2,3/4],\quad t\in\mathbb R.
 \tag{10}
\]
证明：固定 \([1,2]\) 的权差及 \(w_Y(2)-2^{-s}\) 都为 \(O(Y^{-1})\)，
上端为 \(O(Y^{-\sigma})\)。剩下积分的差以
\(1-e^{-x/Y}\le x/Y\)、\(|T_0'(x)|\le Cx^{-3}\) 控制，至多
\(CY^{-1}\int_2^Yx^{-\sigma-2}dx+C\int_Y^\infty x^{-\sigma-3}dx\)。
这为 \(O(Y^{-1}+Y^{-\sigma-2})\)，且 \(Y^{-1}\le Y^{-\sigma}\)。
估计在分部积分后使用 \(|x^{-it}|=1\)，没有付全轴不可积的 \(|t|\)。

## 3. 两个差核的完整变差 [T]

本节仅为初等分析。仍取(1)的参数，在 \(u<u_0\) 将下列函数延拓为零：
\[
 \begin{split}
 k(u)&=e^{-\delta u}
       \{1-e^{-e^{u-L}}\mathbf1_{u\le L}\},\qquad u\ge u_0,\\
 v(u)&=e^{-\delta u}e^{u-L}e^{-e^{u-L}}
                        \mathbf1_{u\le L},\qquad u\ge u_0.
 \end{split}
 \tag{11}
\]
其 \(BV(\mathbb R)\) 变差包括 \(u_0\)、\(L\) 的延拓或截断跳跃。
有统一界
\[
 \boxed{\quad
 TV(k)=2\varepsilon,\quad \|k\|_1\le\frac{4\varepsilon}{3\delta},
 \qquad TV(v)\le2\varepsilon,\quad \|v\|_1\le\frac{4\varepsilon}{3}.
 \quad}
 \tag{12}
\]
证明。对 \(u<L\)，置 \(x=e^{u-L}\in(0,1]\)。\(k\) 的导数符号由
\(-\delta(1-e^{-x})+xe^{-x}>0\) 决定，后一式来自
\(1-e^{-x}\le x\)、\(e^{-x}\ge e^{-1}>1/4\)。故它从下端的零值上跳
后递增，在 \(L\) 由 \(\varepsilon(1-e^{-1})\) 上跳到
\(\varepsilon\)，再指数递减到零；总变差恰为 \(2\varepsilon\)。
下段积分至多 \(\varepsilon/(1-\delta)\)，尾段积分为
\(\varepsilon/\delta\)，两者之和至多 \(4\varepsilon/(3\delta)\)。
又 \(v=\varepsilon x^{1-\delta}e^{-x}\)，内部至多单峰，峰值不超过
\(\varepsilon\)，含两端跳跃的变差至多 \(2\varepsilon\)。换元后
\(\|v\|_1\le\varepsilon\int_0^1x^{-\delta}dx\le4\varepsilon/3\)。
\(\square\)

采用 \(\widehat f(\nu)=\int_{\mathbb R}f(u)e^{i\nu u}du\)；对 \(BV\)
导数测度分部积分，与 \(L^1\) 界合用，得到
\[
 |\widehat k(\nu)|\le C\varepsilon\min\{\delta^{-1},|\nu|^{-1}\},
 \qquad |\widehat v(\nu)|\le C\varepsilon\min\{1,|\nu|^{-1}\}.
 \tag{13}
\]
零频处按各自的第一项解释。

在 RH 下写 \(\rho=1/2+i\gamma\)。对(5)、(8)直接换元给精确式
\[
 \begin{split}
 I_\rho^Y(s)&=-\frac1\rho\int_{u_0}^L
 e^{i(\gamma-t)u}e^{-\delta u-e^{u-L}}(s+e^{u-L})\,du,\\
 I_\rho^Y(s)-I_\rho^\infty(s)
     &=\frac1\rho\{s\widehat k(\gamma-t)-\widehat v(\gamma-t)\}.
 \end{split}
 \tag{14}
\]
\(s\widehat k\) 是正号，\(\widehat v\) 是负号。特别是 \(k\) 在
\(L\) 的正跳跃 \(\varepsilon/e\) 仍在(13)中；这不是平滑掉完整上端。

## 4. 三域 Cauchy 积分、全谱求和与全轴误差

### 4.1 初等积分引理 [T]

对 \(\eta\ge1\) 定义 \(\phi_\eta(x)=\min(\eta,|x|^{-1})\)。则
\[
 \int_{\mathbb R}\frac{1+|t|}{1+t^2}\phi_\eta(t-g)\,dt
 \le C\frac{\log(2+(1+|g|)\eta)}{1+|g|}.
 \tag{15}
\]
这是[297-(18)](297-raw-pole-endpoint-splitting-obstruction.md)的同一初等
引理，现重述分区以检查参数。由对称性先取 \(g\ge2\)。共振区
\(|t-g|\le g/2\) 上，前一权为 \(O(1/g)\)，后一函数积分为
\(O(\log(2+g\eta))\)。低频区 \(|t|\le g/2\) 上，后一函数至多
\(2/g\)，前一权积分为 \(O(\log(2+g))\)。其余为
\(t<-g/2\) 或 \(t>3g/2\)，被积函数 \(O(t^{-2})\)，贡献
\(O(1/g)\)。这些区域覆盖实轴，仅边界重复。\(|g|<2\) 时，在
\(|t|\le4\) 直接积分 \(\phi_\eta\) 得 \(O(\log(2+\eta))\)，
尾部仍是 \(O(t^{-2})\)。由此得(15)。

### 4.2 实际全谱的补偿差 [C/RH]

因 \(|s|\le C(1+|t|)\)，且 \(\delta^{-1}\ge4\)，(13)--(15)给
\[
 \tau_C|I_\rho^Y-I_\rho^\infty|
 \le C\varepsilon\,
 \frac{\log(2+(1+|\gamma|)/\delta)}{|\rho|(1+|\gamma|)}
 \le C\varepsilon\,
 \frac{\log(2+(1+|\gamma|)/\delta)}{1+\gamma^2}.
 \tag{16}
\]
第二步在这里合法，因为 RH 已固定 \(\Re\rho=1/2\)；不向任意趋零
复参数推广。两种符号的零点都计入，不必先取共轭实部。

[R] 经典 Riemann--von Mangoldt 计数蕴含单位高度区间中零点数，计重数，
为 \(O(\log(2+|\gamma|))\)。沿用297所核的
[Hasanalizade--Shen--Wong, Corollary 1.2](https://arxiv.org/pdf/2107.06506)，
这里只用经典量级，不使用最优显式常数。由
\(\log(2+(1+g)/\delta)\le C+\log(2+1/\delta)+\log(1+g)\)，有
\[
 \boxed{\quad
 \sum_\rho\tau_C|I_\rho^Y-I_\rho^\infty|
       \le C\varepsilon\log(2+1/\delta).
 \quad}
 \tag{17}
\]
所有交换都可由非负 Tonelli 或(17)的绝对 \(L^1(\mu_C)\) 收敛支撑。
这和297的原始 \(K_\rho\) 逐项复模发散相容：我们只对包含补偿的
\(I_\rho^Y-I_\rho^\infty\) 求绝对值，从未拆开原始端点级数。

### 定理300-A：保留实际端点的全轴复模误差 [C/RH]

假设 RH。存在常数 \(C\)，对所有 \(Y\ge4\)、\(0<\delta\le1/4\)，
\[
 \boxed{\quad
 \tau_C\left|F_Y^\sharp(\delta+it)
                 -\frac{\xi'}{\xi}(1/2+\delta+it)\right|
 \le C\left\{e^{-q}\frac{|E(Y)|}{\sqrt Y}
             +e^{-q}\log(2+1/\delta)+Y^{-1/2-\delta}\right\}.
 \quad}
 \tag{18}
\]
常数与 \(Y,\delta\) 无关。这里的 \(E(Y)\) 是实际完整端点差值，
没有以绝对零点和或 PNT 点态 majorant 替代。

证明。相减(6)、(9)给完整复恒等式
\[
 F_Y^\sharp(\delta+it)-\frac{\xi'}\xi(s)
 =-e^{-1}Y^{-s}E(Y)-(B_Y-B_\infty)(s)
                 -\sum_\rho(I_\rho^Y-I_\rho^\infty)(s).
 \tag{19}
\]
端点项的复模在全部 \(t\) 上恰为
\(e^{-1-q}|E(Y)|/\sqrt Y\)，其 Cauchy 范数亦如此。
其余分别用(10)、(17)，即得(18)。\(\square\)

这比293-F保留更细的实际端点，并控制复模而非仅实部；机制仍是经典显式
公式的补偿与初等振荡积分。RH 在(8)--(9)、(14)、(16)--(18)中实质使用，
不因为分析步骤完整就把整条实际结论标为无条件 [T]。

## 5. RH 下的端点与谱边界层两项分类

### 定理300-B [C/RH]

假设 RH。存在固定 \(c,C>0\) 及 \(Y_0\)，统一于
\(Y\ge Y_0\)、\(1\le q\le L/4\)、\(\delta=q/L\)，有
\[
 \boxed{\quad
 c\left[1+e^{-q}\left\{\frac{|E(Y)|}{\sqrt Y}+\log L\right\}\right]
 \le 1+\kappa_Y(\delta)
 \le C\left[1+e^{-q}\left\{\frac{|E(Y)|}{\sqrt Y}+\log L\right\}\right].
 \quad}
 \tag{20}
\]
常数可依赖证明中一次选定的零点及固定频窗，不依赖 \(Y,q,E(Y)\)。
这是一致双边比较，不宣称精确首项常数。

证明上界。在 RH 下，经典成对 Hadamard 展开给
\[
 \Re\frac{\xi'}\xi(1/2+\delta+it)
 =\sum_{\gamma>0}m_\gamma
  \left\{\frac{\delta}{\delta^2+(t-\gamma)^2}
        +\frac{\delta}{\delta^2+(t+\gamma)^2}\right\}\ge0.
 \tag{21}
\]
此处沿用[131-XQ](131-positive-real-boundary-impedance-weil.md)及293 §7.1
的成对展开；成对和在右半平面局部一致收敛。它明确以 RH 为条件，
不是独立产生的 Weil 正性。于是负部至多(18)的复误差。又因 \(q\ge1\)，
\(\log(2+1/\delta)=\log(2+L/q)\le C\log L\)，这证明(20)上界。

端点下界。选固定正宽紧窗 \(J_0\)，与全部实际零点高度有正距离；
RH 下高度离散，故此选择合法。将298-A的证明用于未删除任何包的
版本（即 \(m=0\)），得到
\[
 \Re F_Y^\sharp(\delta+it)
     =-a_Y\cos(Lt)+O_{J_0}(1),\qquad
 a_Y=e^{-1-q}E(Y)/\sqrt Y,\qquad t\in J_0.
 \tag{22}
\]
为免依赖形式替换：无包版本正是(6)，在 \(J_0\) 上 \(G,B_Y=O(1)\)；
\(h=e^{-\delta u-e^{u-L}}\) 及 \((s+e^{u-L})h\) 的零延拓变差一致有界，
故 \(|I_\rho^Y|\le C_{J_0}/(|\rho||\gamma-t|)\)，全谱和一致有界。
这直接证明(22)。正、负余弦半波的周期平均均为 \(1/\pi\)。因此由
有界去均值原函数的分部积分，统一于 \(a_Y\) 的两种符号，充分大 \(L\) 时
\[
 \kappa_Y(\delta)\ge c_0e^{-q}|E(Y)|/\sqrt Y-C_0.
 \tag{23}
\]
具体地，先证明
\(\int_{J_0}(\pm\cos Lt)_+d\mu_C=\mu_C(J_0)/\pi+O_{J_0}(L^{-1})\)，
使周期平均最终有固定正下界，再乘 \(|a_Y|\)。并未把含 \(|a_Y|/L\)
的误差当作绝对有界项。

谱边界层下界。当 \(1\le q\le\log\log L\) 时，298-(33)在一个实际
临界零点附近，用完整负半周期测试精确消掉任意共同载波，给
\[
 \kappa_Y(\delta)\ge c_1e^{-q}\log\frac{L}{1+q}-C_1
                    \ge c_2e^{-q}\log L-C_1.
 \tag{24}
\]
第二步对全部所述 \(q\) 在充分大 \(L\) 上一致。若
\(q>\log\log L\)，则 \(e^{-q}\log L<1\)，这一项已经被常数1吸收。
令 \(A=e^{-q}|E(Y)|/\sqrt Y\)、\(B=e^{-q}\log L\)，(23)--(24)分别给
\(A\le C(1+\kappa)\)、\(B\le C(1+\kappa)\)；相加即得(20)下界。
\(\square\)

必须保留 \(1+\kappa\)；本证没有断言 \(\kappa\asymp A+B\) 在两项都趋零
时成立。也不把(20)扩至 \(q<1\)：(18)中的
\(e^{-q}\log(2+1/\delta)\) 此时不再由 \(e^{-q}\log L\) 一致控制。
第4节的误差结论本身仍适用于任意严格 \(0<\delta\le1/4\)。

298已经无条件排除过快日程；本节只在 RH 下给出可行日程所需的两个
实际量及其充分性。它没有证明任一趋中心线日程的无条件有界负迹，
也不把已知的“有界负迹日程推出 RH”倒用为正性来源。

## 6. 显式算术端点修正及其独立接口 [T]

对 \(\Re z\ge0\)，仍写 \(s=1/2+z\)，定义
\[
 \widehat F_Y(z)=F_Y^\sharp(z)+e^{-1}Y^{-s}E(Y),\qquad
 \widehat\kappa_Y(\delta)
       =\tau_C(\Re\widehat F_Y(\delta+it))_- .
 \tag{25}
\]
该项由同一有限 Mangoldt 前缀计算，不读取零点或负谱。
因为 \(E(Y)=\sum_{n\le Y}\Lambda(n)-\int_1^Ydx\)，等价的有限式为
\[
 \widehat F_Y(z)=G(s)+\int_1^Y\{w_Y(x)-w_Y(Y)\}\,dx
 -\sum_{n\le Y}\Lambda(n)\{w_Y(n)-w_Y(Y)\}.
 \tag{26}
\]
这只把每个有限权锚定为在完整上端取零，未改变下端、连续项或Gamma。
另由 Stieltjes 分部积分和 \(E(1)=0\)，有
\[
 \widehat F_Y(z)=G(s)
 -\int_1^Y E(x)x^{-s-1}e^{-x/Y}(s+x/Y)\,dx .
 \tag{27}
\]
固定 \(z\) 时，右侧对全部实 \(Y>1\) 连续：在每个有界 \(Y\) 邻域，
被积函数有可积的共同上界，移动上限的差也趋零。
整数 \(n\) 处，原候选的跳跃
\(-e^{-1}n^{-s}\Lambda(n)\) 与(25)的跳跃正好抵消。
这里不把 \(\Lambda(n)-1\) 与作为实 \(Y\) 变量的跳跃 \(\Lambda(n)\) 混同。

必须独立证明新族的145接口，不能从两个负迹预算相减获得它。
固定 \(Y\)，\(F_Y^\sharp-G\) 是支持于 \(0\le u\le L\) 的有限实
lag源的 Laplace 变换；(25)只新增实原子
\(e^{-1}Y^{-1/2}E(Y)\delta_L\)。故有限部分在闭右半平面有界、
全纯且 real-type。这个结论使用有限源，**不**从(27)粗估出
一个随 \(|s|\) 增长的不可积界。

固定 \(\delta>0\)，Gamma渐近给 \(\Re G(1/2+z)\to+\infty\)，
在 \(\Re z\ge\delta,\ |z|\to\infty\) 上一致。因此边界负部连续且最终
为零。将其非负 Poisson 积分加回 \(\Re\widehat F_Y\)，在充分大的
右半圆上用最小值原理，再扩大半圆，即得145-(5)的 admissibility。
这与293的证明相同，但针对新族重新执行。

在任意 Euler 紧集 \(\Re s\ge1+\epsilon\)，Chebyshev
\(E(Y)=O(Y)\) 使修正项为 \(O(Y^{-\epsilon})\to0\)。
原族的局部一致 Euler-germ 收敛由293已经无条件核验；
所以新族仍以 \(\xi'/\xi(1/2+z)\) 为 Euler germ。由145，
任何 \(Y_j\to\infty,\delta_j>0\to0\) 的有界
\(\widehat\kappa_{Y_j}(\delta_j)\) 仍推出 RH。

构造、连续性与该条件接口均无条件；一致正性没有因此产生。
这不是131的全局无零势函数替代，也不是132中任加小常数就使整个半平面
passive的尝试；(25)只处理已识别的有限端点载波。

在 RH 下，相减(19)并精确消去载波，得到
\[
 \widehat F_Y-\frac{\xi'}\xi
       =-(B_Y-B_\infty)-\sum_\rho D_\rho,\qquad
 D_\rho=I_\rho^Y-I_\rho^\infty,
 \quad
 \tau_C\left|\widehat F_Y-\frac{\xi'}\xi\right|
 \le C\{\varepsilon\log(2+1/\delta)+Y^{-\sigma}\}.
 \tag{28}
\]
左侧自变量为 \(\delta+it\) 和 \(s=1/2+\delta+it\)。
本式对全部实 \(Y\ge4\) 成立，不依赖特殊截断的选择，但明确为[C/RH]。

## 7. 真实全谱的临界渐近 [C/RH]

### 定理300-C

假设 RH。固定任意 \(A>0\)。则当 \(Y\to\infty\)，统一于
\(1\le q\le A\log\log L\)、\(\delta=q/L\)，有
\[
 \boxed{\quad
 \frac{\widehat\kappa_Y(q/L)}{e^{-q}\log L}
 \longrightarrow C_\zeta,\qquad
 C_\zeta=\frac4{\pi^2}
       \sum_{\gamma>0}\frac{m_\gamma}{1+\gamma^2}
       =\frac2{\pi^2}\frac{\xi'}{\xi}(3/2)>0 .
 \quad}
 \tag{29}
\]
重数全部计入。这是实际全谱、原 Cauchy 迹的渐近，不是合成有限模型。
常数中的最后一项位于 Euler 域，可由 \(\Lambda\) 与Gamma表达；
用它作首项系数的证明仍以 RH 为条件。
特别地，若固定 \(c\in\mathbb R\) 且
\(q=\log\log L+c+o(1)\)，则
\[
                 \widehat\kappa_Y(q/L)\longrightarrow C_\zeta e^{-c}>0.
 \tag{30}
\]
不能将“临界负迹有界”误写为“临界负迹已经趋零”。

### 7.1 有限模式分解：只对固定包拆端点

对一个固定零点 \(\rho\)，令
\[
 K_{\rho,L}(s)=\int_1^Y x^{\rho-s-1}e^{-x/Y}\,dx .
\]
对有限区间和无限无权区间分别分部积分，完整保留 \(x=2\) 后，有
\[
 \begin{split}
 -D_\rho(s)
 &=K_{\rho,L}(s)-\frac1{s-\rho}
          -\frac{e^{-1}Y^{\rho-s}}{\rho}+R_{\rho,Y}(s),\\
 R_{\rho,Y}(s)
 &=\int_1^2 x^{\rho-s-1}(1-e^{-x/Y})\,dx
       -\frac{2^{\rho-s}}{\rho}(1-e^{-2/Y}).
 \end{split}
 \tag{31}
\]
例如 \(I_\rho^Y=e^{-1}Y^{\rho-s}/\rho
-2^{\rho-s}e^{-2/Y}/\rho-\int_2^Yx^{\rho-s-1}e^{-x/Y}dx\)；
\(I_\rho^\infty=-2^{\rho-s}/\rho-\int_2^\infty x^{\rho-s-1}dx\)。
相减后把两个积分的下端从2移回1，恰得(31)，没有遗漏常数项。

对任意固定有限零点包，\(R_{\rho,Y}=O(Y^{-1})\) 统一于全部实 \(t\)
及 \(\sigma\in[1/2,3/4]\)。第一项用 \(1-e^{-x/Y}\le x/Y\)，
第二项用 \(|2^{-it}|=1\)。有限上端项为 \(O_\rho(\varepsilon)\)。
**仅在固定有限包内使用(31)**；不能把 \(R_{\rho,Y}\) 或原始模式在
全部零点上直接绝对求和，297的拆分障碍仍有效。

固定 \(V\)，不取为零点高度，令 \(\mathcal S_V\) 包含
\(|\gamma|\le V\) 的全部非平凡零点及完整重数，成对闭合。
写
\[
 \begin{split}
 P_V(t)&=\sum_{0<\gamma\le V}m_\gamma R_{\gamma,\delta,L}(t),\\
 H_V(s)&=\frac{\xi'}\xi(s)-\sum_{\rho\in\mathcal S_V}\frac1{s-\rho},\\
 c_V&=\frac4{\pi^2}\sum_{0<\gamma\le V}\frac{m_\gamma}{1+\gamma^2},\\
 a_V&=\sum_{|\gamma|>V}\frac1{1+\gamma^2},\qquad
 b_V=\sum_{|\gamma|>V}\frac{\log(2+|\gamma|)}{1+\gamma^2}.
 \end{split}
 \tag{32}
\]
尾和也计重数；\(a_V,b_V\) 有限且趋零。
\(R_{\gamma,\delta,L}\) 是296的完整共轭有限包，故
\(\Re\sum_{\rho\in\mathcal S_V}K_{\rho,L}=P_V\)。
由(28)、(31)，全轴有
\[
 \Re\widehat F_Y
   =P_V+\Re H_V-\Re\sum_{|\gamma|>V}D_\rho
                           +O_V(\varepsilon+Y^{-\sigma}).
 \tag{33}
\]
所有 \(O_V\) 常数允许依赖这个**固定**包，未对增长包声称一致。

### 7.2 固定包的负迹：用窗口证明相加

在 \(\mathcal S_V\) 的每个不同高度 \(\pm\gamma\) 附近取固定、互不相交的正宽紧窗，
并确保每个窗与其余全部实际零点高度有正距离。
296的矩形核(8)及Abel差(10)表明：在一个模式自己的两个窗之外，
其负迹为 \(O_V(\varepsilon)\)。理由是矩形核的 Poisson 主项非负，
振荡余项在 \(|t\mp\gamma|\ge h_V>0\) 上的 Cauchy 积分为
\(O_V(\varepsilon)\)，Abel差在全轴同阶。另一方面，该模式在另一个
模式的固定窗内的实部为 \(O_V(\delta+\varepsilon)\)。

因此，上界用负部的次可加性；下界在互不相交的窗分别积分，并用负部的
Lipschitz性控制所有非共振模式。由296-A可得
\[
 \tau_C(P_V)_-
      =c_V\varepsilon\log L
       +O_{V,A}\{\varepsilon[1+q+\log(1+q)]+\delta\}
      =c_V\varepsilon\log L+o_{V,A}(\varepsilon\log L).
 \tag{34}
\]
对本定理整个参数范围，最后一步一致，因为
\[
 \frac{1+q+\log(1+q)}{\log L}\longrightarrow0,\qquad
 \frac{\delta}{\varepsilon\log L}
   =\frac{qe^q}{L\log L}
   \le\frac{A(\log\log L)(\log L)^{A-1}}{L}\longrightarrow0 .
 \tag{35}
\]
这里没有把 \((\sum f_j)_-\) 直接等同于 \(\sum(f_j)_-\)。

### 7.3 全谱上界与局部下界

RH和成对Hadamard展开给 \(\Re H_V(s)\ge0\)；这是上界中可利用的
正背景。将(16)保留为尾和，得到与 \(V\) 无关的常数 \(C\)：
\[
 \sum_{|\gamma|>V}\tau_C|D_\rho|
 \le C\varepsilon\{\log(2+1/\delta)a_V+b_V\}.
 \tag{36}
\]
由(33)、负部不等式及(34)，
\[
 \frac{\widehat\kappa_Y}{\varepsilon\log L}
 \le c_V+o_{V,A}(1)
       +C\left\{\frac{\log(2+1/\delta)}{\log L}a_V
                       +\frac{b_V}{\log L}\right\}.
 \tag{37}
\]
因为 \(q\ge1\)，第一个比值一致有界；
\(Y^{-\sigma}/(\varepsilon\log L)=Y^{-1/2}/\log L\to0\)。

下界不能在全轴粗估正背景。只使用7.2的有限组隔离窗。在这些窗的并集
\(J_V\) 上，未选零点与 \(t\) 有固定正距离。于是(13)--(14)给
\[
 \sum_{|\gamma|>V}|D_\rho(s)|
 \le C_{J_V}\varepsilon
        \sum_{|\gamma|>V}\frac1{|\rho|\,|\gamma-t|}
       =O_V(\varepsilon).
 \tag{38}
\]
高处为 \(\gamma^{-2}\)，有限低处由谱间隔控制，故这里全谱绝对求和合法。
同样由(21)，未选零点的正 Poisson 核在这些窗内满足
\(\Re H_V(s)=O_V(\delta)\)。
结合(33)及非共振的已选模式，在每个窗内可写
\(\Re\widehat F_Y=m_\gamma R_{\gamma,\delta,L}
+O_V(\varepsilon+\delta+Y^{-\sigma})\)。
利用296的窗外负迹 \(O_V(\varepsilon)\)、(34)--(35)，得
\[
 \frac{\widehat\kappa_Y}{\varepsilon\log L}
                      \ge c_V-o_{V,A}(1).
 \tag{39}
\]

**极限顺序**是先固定 \(V\)，令 \(Y\to\infty\)，且误差对
\(1\le q\le A\log\log L\) 一致；再令 \(V\to\infty\)。
(37)--(39)给的上下夹逼中，\(a_V\to0\)、\(c_V\to C_\zeta\)，
所以得到真正的统一比值极限(29)。没有让 \(V\) 随 \(Y\) 增长后
悄悄使用 \(O_V(1)\)，也未以数值截断代替无限尾。
最后在RH成对展开中取 \(z=1\)，得到
\[
 \frac{\xi'}\xi(3/2)
        =2\sum_{\gamma>0}\frac{m_\gamma}{1+\gamma^2}.
 \tag{40}
\]
已知非平凡零点存在使此数严格正。由此确认(29)的常数；(30)直接代入。
\(\square\)

## 8. 不借 RH 或强振荡幅度的小端点整数 [T]

### 引理300-D

定义完全由同一实际算术前缀给出的整数集合
\[
 \mathcal C=\{n\ge2:E(n-1)>0\ge E(n)\}.
 \tag{41}
\]
则 \(\mathcal C\) 无界，且每个 \(n\in\mathcal C\) 满足
\(-1<E(n)\le0\)。因此按递增顺序枚举便得到一条不读取零点的固定共尾序列。
本引理不使用 RH、Littlewood 强振荡量级或284的记录选择。

证明。先证明 \(E(x)\) 在任何尾部既无有限上界，也无有限下界。
在 \(\Re s>1\)，直接对 \(\psi(x)-x+1\) 作Mellin变换得到
\[
 M_E(s)=\int_1^\infty E(x)x^{-s-1}dx
       =\frac{D(s)}s,\qquad
 D(s)=-\frac{\zeta'}\zeta(s)-\frac1{s-1}.
 \tag{42}
\]
积分交换由绝对收敛的 Euler 级数支撑；在 \(s=1\)，两个极点正好抵消。
对 \(0<s<1\)，交错级数
\(\eta(s)=\sum_{k\ge1}\{(2k-1)^{-s}-(2k)^{-s}\}>0\)
给 \(\zeta(s)=\eta(s)/(1-2^{1-s})<0\)；对实 \(s>1\)，Euler乘积非零。
所以 \(D(s)/s\) 在每个正实点的复邻域全纯。
另一方面，已知存在非实非平凡零点；用函数方程反射后，可选
\(\rho\) 满足 \(\Re\rho>0\)。在 \(\rho\) 处，(42)的亚纯延拓
有非零留数 \(-m_\rho/\rho\)。只使用经典零点存在性，不假设该零点在中心线。

若 \(x\ge X\) 时 \(E(x)\le B\)，则
\(f(u)=B-E(e^u)\ge0\) 对 \(u\ge\log X\) 成立。在Euler域内，其尾Laplace变换为
\[
 \int_{\log X}^\infty e^{-su}f(u)\,du
   =\frac{BX^{-s}}s-\frac{D(s)}s
                         +\int_1^X E(x)x^{-s-1}dx .
 \tag{43}
\]
Chebyshev给此非负Laplace积分的收敛横坐标 \(\lambda\le1\)。
若 \(\lambda>0\)，非负Laplace变换的Landau实轴奇点性质与(43)
在正实点 \(\lambda\) 的解析性矛盾。所需最小引理已在299 §5.2重证：
若和函数在 \(\lambda\) 附近解析，可取 \(x_0>\lambda\) 和严格内半径
\(x_0-\lambda<r<R\)，Taylor的交错导数为非负积分；
Tonelli使Taylor在位移 \(r\) 的收敛级数之和（其值有限）等于
\(\int e^{-(x_0-r)u}f(u)du\)，从而越过收敛横坐标，矛盾。
若 \(\lambda\le0\)（包含 \(-\infty\)），左侧已在整个
\(\Re s>0\) 全纯，而右侧在 \(\rho\) 仍有非零极点；由解析延拓唯一性再次矛盾。
假设尾部存在下界时，对 \(E(e^u)-B\ge0\) 同样论证。
这里仅得所需双向无界，不另声称强振荡幅度或有效高度。

若 \(n\le x<n+1\)，右连续完整原子约定给
\[
 E(n)=E(x)+(x-n),\qquad
 E(n)-E(n-1)=\Lambda(n)-1\ge-1 .
 \tag{44}
\]
第一式将双向无界传给整数点；每个充分远的正点之后仍有非正点。
取其后的首个非正整数，便在 \(\mathcal C\) 中，故此集合无界。
第二式同时给 \(-1<E(n)\le0\)。
没有把实尺度的跳跃 \(\Lambda(n)\) 改成整数步长差，
也没有假设下降交点必为合数，2的幂同样可能有负步长。
\(\square\)

在 \(Y\in\mathcal C\) 上，由(25)及负部的Lipschitz性，
\[
 |\kappa_Y(\delta)-\widehat\kappa_Y(\delta)|
 \le \frac{e^{-q}}{e\sqrt Y}
              =o(e^{-q}\log L).
 \tag{45}
\]
所以在RH下，300-C的统一渐近及临界极限(30)也对原候选沿
这条共尾算术截断序列成立。这些点不是284的强质量记录：
没有相应的 \(\ell(Y)\) 质量增益或历史支配证明，不能回填旧记录的其它接口。

## 9. 日程的完整校准与循环性审计

对任意 \(Y_j\to\infty,\delta_j>0\to0\)，记
\[
 L_j=\log Y_j,\qquad q_j=\delta_jL_j,\qquad
 h_j=q_j-\log\log L_j.
 \tag{46}
\]
以下是上述结果的逻辑收束，不登记为把RH削弱成新的算术假设：
\[
 \begin{split}
 \sup_j\widehat\kappa_{Y_j}(\delta_j)<\infty
 &\quad\Longleftrightarrow\quad
       \mathrm{RH}\ \text{且}\ \inf_j h_j>-\infty,\\
 \widehat\kappa_{Y_j}(\delta_j)\longrightarrow0
 &\quad\Longleftrightarrow\quad
       \mathrm{RH}\ \text{且}\ h_j\longrightarrow+\infty .
 \end{split}
 \tag{47}
\]
各式忽略任意有限前缀；充分大的 \(j\) 自动满足 \(0<\delta_j\le1/4\)。
若 \(Y_j\in\mathcal C\)，(47)也适用于原候选 \(\kappa_{Y_j}\)。
对未修正的任意截断，不能删除300-B中独立的端点预算。

证明。第6节已无条件核验新族的145接口，所以有界负迹首先推出RH。
在RH分支，298临界窗的载波公式经(25)修正后变成
\(\Re\widehat F_Y=mR_{\gamma,\delta,L}+O(1)\)。
298-B取共同载波系数为零，得到
\[
 \widehat\kappa_Y(\delta)
    \ge c e^{-q}\log\frac{L}{1+q}-C,\qquad
                         0<q\le\log\log L .
 \tag{48}
\]
所以有界负迹要求 \(h_j\) 有下界；否则选 \(h_j\to-\infty\) 子序列，
(48)的右侧趋于无穷。这同样证明新族的过快日程无条件发散：
若发散失败，取有界子序列，先由145推出RH，再使用(48)得到矛盾。
不从此反证宣称无条件增长率。

反向，RH及 \(h_j\) 有下界保证最终 \(q_j\ge1\)。由(28)、(21)，
\[
 \widehat\kappa_{Y_j}(\delta_j)
   \le C e^{-q_j}\log(2+L_j/q_j)+C Y_j^{-\sigma_j}
   \le C e^{-h_j}+o(1).
 \tag{49}
\]
这证明有界充分性，也证明 \(h_j\to+\infty\) 时趋零。
若负迹趋零但 \(h_j\not\to+\infty\)，前述有界必要性先给 \(h_j\)
下界；再选 \(h_j\) 上下都有界的子序列。此时
\(1\le q_j\le2\log\log L_j\) 最终成立，(29)给
\(\widehat\kappa_{Y_j}/e^{-h_j}\to C_\zeta>0\)，与趋零矛盾。
由(45)，原候选在 \(\mathcal C\) 上与新族的负迹差趋零，
故同样得到(47)。\(\square\)

这完成了本轮的有限目标：原全轴误差缺口与临界门槛得到精确条件校准。
独立小端点与有限端点修正均不提供缺失的正性；
“证明(47)左侧”依然具有RH全强度，不能重命名为弱局部预算或紧性公理。
本篇没有证明RH/GRH、新零密度、零自由区或零点比例。

## 10. 输入作用、删除条件与下一最小问题

| 输入/条件 | 使用位置 | 删除后的失效或限制 |
|---|---|---|
| 真实源、完整两端与同一Abel权 | (6)、(19)、(25)--(28)、(31) | 原始极点和与端点各自绝对求和仍被297排除 |
| RH | (9)、(14)、正余谱、全谱渐近 | 振幅变成随实部增长的指数；余谱不再提供该正背景 |
| 原Cauchy迹及计数 | (15)--(17)、(36) | 无权全轴积分或高阶矩不能照搬 |
| 固定有限谱包，先尺度后谱高极限 | (31)--(39) | 固定包的间隔常数不对增长包或L函数族自动一致 |
| 隔离窗 | (22)、(34)、(38)--(39) | 下界不能从全轴粗尾界恢复正确首项系数 |
| \(1\le q\le A\log\log L\) | (29)、(35)、(37) | 此精确渐近未外推到任意靠线日程；一般日程仅由(47)分类 |
| 非负Laplace实轴奇点与已知非实极点 | (41)--(44) | 小端点的共尾性不是任意固定符号源的自动性质 |
| 新族独立Poisson/Euler验证 | 第6、9节 | 不能因修正了一项就默认其仍识别同一除子 |

本轮仍是显式公式型配置的有限到整体审计；没有上同调、极化或
Hard Lefschetz构造，也不认定两类Weil结构等价。
初等Cauchy引理与Hadamard/Landau机制是已知分析，不以重新命名主张新颖性。
新的内部内容是补偿差的参数预算、真实全谱的条件临界常数及严格适用边界。
文献优先权、外部同行审查和发表价值尚未确认，不构成Goal阶段完成。

本固定zeta候选的上述条件日程校准已闭合，不继续通过改写(47)扩张框架。
下一最小可证伪问题仅针对第7节的**一致性边界**：[O] 在合成的两个中心
极点对中，固定 \(\gamma>0,A>0\)，令高度差为 \(\pi/L\)，检查
\[
 \kappa_-\!\left(R_{\gamma,\delta,L}
                    +R_{\gamma+\pi/L,\delta,L}\right)
       \stackrel{?}{=}o(e^{-q}\log L),
       \qquad 1\le q\le A\log\log L .
 \tag{50}
\]
这是随 \(L\) 变化的模型族，不是固定zeta的新零点假设。
若(50)成立，便精确说明固定谱包的主系数不能在没有簇控制时直接向
增长谱包或L函数族外推；若不成立，则登记反例并停止该猜测。
只允许一次完整双包核计算与一致误差检查，不以新增等价预算替代算术输入。
本篇暂归独立response论文的有限化/亚纯接口部分，继续用Markdown；
下一次论文更新须先完成周期收束和文献定位，不并入四矩比例论文。

## 11. 复算与独立审计登记

[endpoint_separated_kernel_probe.py](../scripts/endpoint_separated_kernel_probe.py)
仅用六组合成参数，比较原lag积分与32阶有限指数展开；\(k\) 的无穷尾
解析计算，并保留两个下端/截断跳跃。每个级数截断都有显式阶乘尾界。
作者和主代理分别运行通过：48次MP50单核核验，主代理脚本约2.21秒；
最大级数与独立积分差 \(2.783\cdot10^{-39}\)，最大误差/阶乘尾界
\(0.972231\)。L1、变差和Fourier上界均通过。
这些全部为[E]；不是区间算术认证、实际零点表或全轴Cauchy范数计算，
更不证明(29)的无限谱渐近。

最终50式全文由主代理、carrier_audit、gap_exception_audit、
midband_compute分别完整读取并逆向复核通过。核验重点包括无限补偿的
Euler开集识别、全轴复模而非实部、完整两端、固定包与全谱的两次极限、
正背景的上下界不同用法、小端点整数以及(47)的必要充分量词。
已把Landau证明中的Taylor“有限和”澄清为收敛级数的有限数值，
避免误读为有限项截断。内部交叉审计不是外部同行评审或新颖性确认。

仓库布局检查、11项布局回归和77项检查的注册/mock调度核验通过；
未重跑77项重型计算。本轮不更新PDF，Goal保持研究中。
