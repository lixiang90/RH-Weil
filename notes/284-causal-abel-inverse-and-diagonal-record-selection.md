# 284. 因果 Abel 逆核与整数对角记录选择

日期：2026-09-06。主线：NCE-8 / B1z；论文归属：Vaughan--Brownian response。

状态：[T] 因果指数可积逆核、离散历史桥梁及记录转移；
[T/R] 使用283实际强振荡输入的新整数对角共尾选择；
[T] 新序列的增长低频、加强质量下的高频归约及前缀接口；
[O] 剩余中频算术预算。
本篇不证明 RH、GRH 或任何零点比例，也不声称得到新的正性结构。

## 1. 对象、所需输入和新旧序列

固定 \(0<\sigma<\beta<1/2\)，记
\[
 \delta=\beta-\sigma>0,\qquad d_0=1/2-\sigma>0,
 \qquad \eta=1/2-\beta>0 .
 \tag{1}
\]
实际 von Mangoldt 源、右连续端点和连续项均不改变：
\[
 \psi(x)=\sum_{n\le x}\Lambda(n),\qquad
 R(x)=\psi(x)-x,\qquad \widetilde R(x)=R(x)+1,\qquad
 \widetilde R(1)=0,
\]
\[
 A_\sigma(Y)=M(Y,Y)
 =\sum_{2\le n\le Y}\Lambda(n)n^{-\sigma}e^{-n/Y}
       -\int_1^Yx^{-\sigma}e^{-x/Y}\,dx,\qquad Y\ge1 .
 \tag{2}
\]
本篇新增的选择满足 **\(Y=N\) 均为整数**，不预先要求 \(Y\) 为2的幂。
它不是[275](275-record-envelope-and-growing-low-frequency-closure.md)原认证算法的同一输出，
也不声称满足275预先指定的数值 guard 常数。

唯一用于产生实际共尾记录的振荡输入为
[283定理A](283-fixed-cutoff-abel-mass-oscillation.md)已单独建立的
\[
 A_\sigma(Y)=\Omega_\pm\!\left(Y^{d_0}\ell(Y)\right),\qquad
 \ell(Y)=\max(1,\log\log\log Y)
 \quad(Y\text{ 充分大}).
 \tag{3}
\]
本篇把(3)当作明确的独立输入，并不由逆核产生它。
以下逆核定理和历史不等式本身不需要(3)，不假设 RH。

## 2. 端点保留的 Volterra 恒等式 [T]

在 \(u\ge0\) 置
\[
 \mathcal B_\sigma(u)=e^{\sigma u}A_\sigma(e^u),\qquad
 r_\beta(u)=e^{-\beta u}\widetilde R(e^u),\qquad
 b_\beta(u)=e^{-\beta u}\mathcal B_\sigma(u)
           =e^{-\delta u}A_\sigma(e^u).
 \tag{4}
\]
这些是半轴上的函数，不是275的中心化 lag 测度 \(r\)。
小写 \(r_\beta\) 仅在本篇表示归一化历史误差。
卷积均为因果卷积
\((f*g)(u)=\int_0^u f(t)g(u-t)\,dt\)。

### 引理284-A

有精确恒等式
\[
 \boxed{\quad b_\beta=e^{-1}r_\beta+k_\beta*r_\beta,\qquad
 k_\beta(t)=e^{-\delta t-e^{-t}}(\sigma+e^{-t})\quad(t\ge0).\quad}
 \tag{5}
\]

证明。因 \(d\widetilde R=d\psi-dx\) 且 \(\widetilde R(1)=0\)，对固定 \(Y\)
的正递减权 \(w_Y(x)=x^{-\sigma}e^{-x/Y}\) 作精确分部积分：
\[
 A_\sigma(Y)=w_Y(Y)\widetilde R(Y)
          +\int_1^Y\widetilde R(x)(-w_Y'(x))\,dx .
 \tag{6}
\]
这里没有把 \(\widetilde R\) 换回 \(R\) 后丢掉下端常数。
乘以 \(Y^\sigma\)，再令 \(Y=e^u,\ x=Ye^{-t}\)，得到
\[
 \mathcal B_\sigma(u)=e^{-1}\widetilde R(e^u)
 +\int_0^u e^{\sigma t-e^{-t}}(\sigma+e^{-t})
                         \widetilde R(e^{u-t})\,dt .
 \tag{7}
\]
乘以 \(e^{-\beta u}\) 即(5)。在整数 \(Y\) 处，\(\psi(Y)\) 及和式都取
完整原子；(6)--(7)同样成立，不使用半权端点。\(\square\)

## 3. 变换无零与真正的指数可积逆核 [T]

### 定理284-B

存在实因果核 \(l_\beta\in L^1([0,\infty))\)，满足某个
\(\omega>0\) 下的 \(|l_\beta(t)|\ll_{\sigma,\beta}e^{-\omega t}\)，并且
\[
 \boxed{\quad r_\beta=e\,b_\beta+l_\beta*b_\beta.\quad}
 \tag{8}
\]
对每个 \(U\ge0\)，因此有
\[
 \sup_{0\le u\le U}|r_\beta(u)|
 \le C_{\rm inv}\sup_{0\le u\le U}|b_\beta(u)|,\qquad
 C_{\rm inv}=e+\|l_\beta\|_1<\infty .
 \tag{9}
\]
等式(8)适用于任意满足(5)的局部有界可测历史，不要求历史具有任何正性。

### 3.1 Laplace 变换与无零性

写 \(\mathcal K_\beta(z)=\int_0^\infty e^{-zt}k_\beta(t)\,dt\)。
对 \(\Re z>-\delta\)，令
\(\gamma(s,1)=\int_0^1v^{s-1}e^{-v}\,dv\)（\(\Re s>0\)），则
\[
 F_\beta(z):=e^{-1}+\mathcal K_\beta(z)
 =(z+\beta)\gamma(z+\delta,1).
 \tag{10}
\]
事实上，换元 \(v=e^{-t}\) 给
\(\mathcal K_\beta=\sigma\gamma(z+\delta,1)+\gamma(z+\delta+1,1)\)，
再用分部积分恒等式
\(s\gamma(s,1)=e^{-1}+\gamma(s+1,1)\)。

为不把无零性当作形式假设，这里重建所需事实。
对 \(s=a+iv,\ a>0\)，
\[
 s\gamma(s,1)=e^{-1}
       +\int_0^\infty e^{-(s+1)t-e^{-t}}\,dt .
 \tag{11}
\]
当 \(v>0\) 时，右侧的虚部为
\(-\int_0^\infty g_a(t)\sin(vt)\,dt\)，其中
\[
 g_a(t)=e^{-(a+1)t-e^{-t}},\qquad
 g_a'(t)=(-a-1+e^{-t})g_a(t)<0 .
\]
它严格递减、正且可积。按相邻半周期配对，
\[
 \int_0^\infty g_a(t)\sin(vt)\,dt
 =\sum_{j\ge0}\int_0^{\pi/v}
 \{g_a(t+2j\pi/v)-g_a(t+(2j+1)\pi/v)\}\sin(vt)\,dt>0 .
 \tag{12}
\]
配对合法，因为原积分绝对收敛。因此 \(v>0\) 时(11)非实，\(v<0\)
用共轭，\(v=0\) 时原 \(\gamma\) 积分为正。故 \(\gamma(s,1)\) 在
\(\Re s>0\) 无零。又 \(z+\beta=0\) 位于 \(\Re z=-\beta<-\delta\)，所以
\[
 F_\beta(z)\ne0\qquad(\Re z>-\delta).
 \tag{13}
\]

### 3.2 除去首项后的可积 Bromwich 逆变换

固定 \(\omega=\delta/3,\ \omega_0=2\delta/3\)，故
\(0<\omega<\omega_0<\delta\)。核 \(k_\beta\) 及它的前两阶导数
都属于 \(L^1(e^{\omega t}dt)\)。两次分部积分给
\[
 \mathcal K_\beta(z)=\frac{k_\beta(0)}z+O_{\sigma,\beta,\omega}(|z|^{-2})
 \quad(|z|\ge1,\ \Re z\ge-\omega),
 \tag{14}
\]
其中余项的统一性直接来自
\[
 \mathcal K_\beta(z)
 =\frac{k_\beta(0)}z+\frac{k_\beta'(0)}{z^2}
       +\frac1{z^2}\int_0^\infty e^{-zt}k_\beta''(t)\,dt .
 \tag{15}
\]
这不只是在一条固定竖线上的渐近式。
由(13)、(14)，\(F_\beta^{-1}\) 在闭半平面 \(\Re z\ge-\omega\) 一致有界：
大 \(|z|\) 时 \(F_\beta\to e^{-1}\)，剩余紧集用无零性。
令
\[
 c_0=-e^2k_\beta(0)=-e(\sigma+1),\qquad
 H_\beta(z)=F_\beta(z)^{-1}-e-\frac{c_0}{z+\omega_0}.
 \tag{16}
\]
则 \(H_\beta\) 在包含上述闭半平面的开区域解析，并有统一界
\[
 |H_\beta(z)|\le\frac{C_H}{(1+|z|)^2}\qquad(\Re z\ge-\omega).
 \tag{17}
\]
所减有理项的唯一极点 \(-\omega_0\) 严格位于该半平面左侧。

定义对全部实 \(t\) 都绝对收敛的积分
\[
 h_\beta(t)=\frac{e^{-\omega t}}{2\pi}
       \int_{\mathbb R}H_\beta(-\omega+iv)e^{ivt}\,dv .
 \tag{18}
\]
它满足 \(|h_\beta(t)|\le C e^{-\omega t}\)。
还必须证明因果性，不能仅将(18)称作逆变换后默认它在负半轴为零。
对任意固定 \(X>0\)，在 \(-\omega\) 与 \(X\) 两条竖线间用 Cauchy 定理。
固定 \(t,X\) 时，水平边由(17)在高度趋于无穷后消失，故
\[
 h_\beta(t)=\frac{e^{Xt}}{2\pi}
             \int_{\mathbb R}H_\beta(X+iv)e^{ivt}\,dv .
 \tag{19}
\]
而当 \(X\ge1\)，
\(\int_{\mathbb R}|H_\beta(X+iv)|\,dv\ll(1+X)^{-1}\)。
令 \(X\to\infty\)，对 \(t<0\) 得 \(h_\beta(t)=0\)；同一估计也给
\(h_\beta(0)=0\)。这证明因果性。

### 3.3 Laplace 反演与卷积恒等式

对 \(\Re z>-\omega\)，(17)--(18)允许 Fubini，且刚证实负半轴为零，
所以
\[
 \begin{aligned}
 \int_0^\infty e^{-zt}h_\beta(t)\,dt
 &=\frac1{2\pi}\int_{\mathbb R}
       \frac{H_\beta(-\omega+iv)}{z+\omega-iv}\,dv\\
 &=H_\beta(z).
 \end{aligned}
 \tag{20}
\]
最后一等式是右半平面的 Cauchy 积分公式；可在右侧大矩形上应用，
再由(17)让其余三边趋于零。分母的符号已与左侧竖线向上积分的方向匹配。
因此置
\[
 l_\beta(t)=c_0e^{-\omega_0t}+h_\beta(t)\quad(t\ge0),\qquad
 l_\beta(t)=0\quad(t<0),
 \tag{21}
\]
就有 \(\mathcal L l_\beta=F_\beta^{-1}-e\)。
此核为实值，因为各变换满足共轭对称；且
\(|l_\beta(t)|\ll e^{-\omega t}\)，特别
\(l_\beta\in L^1(e^{\omega' t}dt)\) 对任意 \(0\le\omega'<\omega\) 成立。

现在
\[
 (e^{-1}+\mathcal L k_\beta)(e+\mathcal L l_\beta)=1
\]
给 \(L^1\) 函数 \(e\,k_\beta+e^{-1}l_\beta+l_\beta*k_\beta\) 的
Laplace 变换恒为零。取竖线上的 Fourier 变换并用 \(L^1\) Fourier 唯一性，
得到该函数几乎处处为零。这里的唯一性也可通过卷积 Gaussian 后反演，
再令 Gaussian 近似恒等核收缩来证明。于是测度卷积恒等式确为
\[
 (e\delta_0+l_\beta(t)dt)*
 (e^{-1}\delta_0+k_\beta(t)dt)=\delta_0 .
 \tag{22}
\]
对任意局部有界可测 \(r_\beta\)，有限时间区间上的卷积均绝对收敛，Fubini
和结合律合法。将(22)作用于(5)，逐点得到(8)，包括其右连续跳跃点；
再取历史上确界得(9)。这完成定理284-B。\(\square\)

## 4. 连续历史到整数历史的统一误差 [T]

令
\[
 b(x)=x^{-\delta}A_\sigma(x),\qquad
 B_N=\max_{1\le n\le N,\ n\in\mathbb Z}|b(n)|,\qquad
 P_\beta(N)=\max_{1\le n\le N,\ n\in\mathbb Z}\frac{|R(n)|}{n^\beta}.
 \tag{23}
\]
整数 \(n=1\) 时 \(b(1)=0\)，但 \(R(1)=-1\)。

### 引理284-C

有只依赖 \(\sigma,\beta\) 的有限常数 \(C_{\rm round}\)，使对所有整数
\(N\ge1\)，
\[
 \sup_{1\le x\le N}|b(x)|\le B_N+C_{\rm round},
 \tag{24}
\]
\[
 \boxed{\quad P_\beta(N)
       \le C_{\rm inv}(B_N+C_{\rm round})+1.\quad}
 \tag{25}
\]

证明。对非整数 \(Y\)，固定原子集合后直接求 Abel 参数导数：
\[
 A_\sigma'(Y)=Y^{-2}
 \left\{\sum_{n\le Y}\Lambda(n)n^{1-\sigma}e^{-n/Y}
                 -\int_1^Yx^{1-\sigma}e^{-x/Y}\,dx\right\}
                 -Y^{-\sigma}e^{-1}.
 \tag{26}
\]
仅以 \(\Lambda(n)\le\log n\) 和初等和式估计便有
\[
 |A_\sigma(Y)|\ll_\sigma Y^{1-\sigma}\log(2Y),\qquad
 |A_\sigma'(Y)|\ll_\sigma Y^{-\sigma}\log(2Y).
 \tag{27}
\]
所以在每个开整数单元，
\[
 |b'(Y)|\ll_{\sigma,\beta}Y^{-\beta}\log(2Y).
 \tag{28}
\]
右侧在 \(Y\ge1\) 有界。对 \(x\in[n,n+1)\)，从右连续值 \(b(n)\)
向右积分时不跨过下一个原子跳跃，故 \(|b(x)-b(n)|\le C_{\rm round}\)。
整数 \(x=N\) 已包含在最大值内，得到(24)。
对(9)取 \(U=\log N\)，再用
\(|R(n)|\le|\widetilde R(n)|+1\)，得(25)。\(\square\)

这里没有把 \(\sup_{\mathbb R}\) 与整数最大值直接等同。
(27)还表明 \(A_\sigma(Y)-A_\sigma(\lfloor Y\rfloor)
=O_\sigma(Y^{-\sigma}\log Y)\)；该误差在(3)的振幅尺度上为小量。
因而若283首先在实数尺度证明(3)，它也给出同强度的整数共尾点。

## 5. 新整数对角记录选择 [T/R]

### 定理284-D

假设实际振荡输入(3)。则有共尾整数 \(N_j\to\infty\)，取
\(Y_j=N_j\)，可使
\[
 |M(Y_j,N_j)|\gg_{\sigma,\beta}
           N_j^{1/2-\sigma}\ell(N_j),
 \tag{29}
\]
\[
 P_\beta(N_j)N_j^\delta
       <C_{\rm diag}|M(Y_j,N_j)|,\qquad
 C_{\rm diag}=4C_{\rm inv}.
 \tag{30}
\]
特别，充分大时同一新序列满足
\[
 |M(Y_j,N_j)|>N_j^{1/2-\sigma}\sqrt{\ell(N_j)}.
 \tag{31}
\]
常数 \(C_{\rm diag}\) 与尺度无关，但不声称等于或小于275指定常数。

证明。由(3)及整数化，存在无界整数 \(Q\) 使
\[
 |b(Q)|\ge cQ^\eta\ell(Q).
 \tag{32}
\]
在 \(1\le n\le Q\) 的整数中取 \(|b(n)|\) 的一个真正最大者 \(N\)。
则 \(B_N=|b(N)|=B_Q\)，且
\[
 |b(N)|\ge cQ^\eta\ell(Q)\ge cN^\eta\ell(N)
 \tag{33}
\]
在足够大参数处成立。这里 \(\eta>0\)、\(\ell\) 最终非减。
记录高度趋于无穷，所以所取 \(N\) 无界；抽取严格递增子序列即可。
乘以 \(N^\delta\) 得(29)，没有消耗 \(\ell\) 因子。

由(25)，当记录高度足够大时，
\[
 P_\beta(N)\le
 C_{\rm inv}(|b(N)|+C_{\rm round})+1
 \le2C_{\rm inv}|b(N)|<C_{\rm diag}|b(N)|.
 \tag{34}
\]
乘以 \(N^\delta\) 即(30)。最后
\(\ell(N)/\sqrt{\ell(N)}\to\infty\)，由(29)得到(31)。\(\square\)

这个选择取的是**归一化 Abel 质量 \(b(n)=n^{-\delta}A_\sigma(n)\) 的记录**，
不是未经归一化的质量记录，也不是窗口内最大值。
它首先是一条存在性定理：本篇未实现无界搜索，没有给 \(C_{\rm inv}\) 的
认证数值上界。即便固定参数可计算，也不能仅凭符号 \(C_{\rm diag}\) 就声称
已有按该阈值运行的认证算法。构造有效常数和实现属于另外的有限任务。

## 6. 新序列的增长低频闭合 [T]

在(29)--(31)的对角序列固定 \(Y=N\)，重新使用原实际路径
\[
 H_Y(u)=M(Y,e^u),\qquad 0\le u\le\tau=\log N=L.
 \tag{35}
\]
这里 \(H_Y\) 是真实累计差异，不是第3节复变量函数 \(H_\beta(z)\)。
275-C的分部积分证明只需要固定有限 \(Y\le N\le2Y\)，不需要 \(Y\) 为2的幂。
其结论与(30)给
\[
 \|H_Y\|_1\ll_{\sigma,\beta}|M|,\qquad
 \|H_Y\|_2^2\ll_{\sigma,\beta}M^2.
 \tag{36}
\]
具体是 \(\|H_Y\|_1\ll P_\beta(N)N^\delta\) 及
\(\|H_Y\|_2^2\ll P_\beta(N)^2N^{2\delta}\)；此处允许常数依赖本篇新的
\(C_{\rm diag}\)，绝不替换成275原认证程序的数值常数。

对真实中心化 lag 源有精确恒等式
\[
 \widehat r(\xi)=M(\cos(\tau\xi)-1)
            +\xi\int_0^\tau H_Y(u)\sin(\xi u)\,du .
 \tag{37}
\]
其端点和 \(-M\) 均保留。以
\[
 Q_E(r)=\frac1{2\pi}\int_E\frac{|\widehat r(\xi)|^4}{\xi^2}\,d\xi
\]
记裸四阶能量，275的完整 Plancherel/Young 证明给
\[
 \begin{aligned}
 Q_{|\xi|\le T}(r)
 &\le10M^4\tau+4T^2\|H_Y\|_1^2\|H_Y\|_2^2\\
 &\ll_{\sigma,\beta}M^4(L+T^2)\qquad(T>0).
 \end{aligned}
 \tag{38}
\]
这证明新的固定对角记录也无条件闭合 \(T=\sqrt L\) 的低频。
原实际正通道的上界及 \(D\asymp S^2L\) 在 \(Y=N\) 仍是相同的有限源事实，
可见[277](277-continuum-channel-coercivity-and-double-discrepancy-interface.md)；
因此同样可得
\[
 J_{4,|\xi|\le T}/\mu^4\ll_{\sigma,\beta}1+T^2/L.
 \tag{39}
\]

### 6.1 单独审计274的统一高频，并使用更强质量 [T/R]

不能直接援引274-B的原 dyadic 序列措辞；但274-A已明确对每个充分大实数
\(Y\)、整数 \(Y\le N\le2Y\)、\(T\ge1\) 给出统一有限预算
\[
 Q_{|\xi|>T}(r)\ll_\sigma
 \frac{Y^{2-4\sigma}L^2}{T}
 +\frac{Y^{4-4\sigma}W}{T^2}
 +\frac{M^4}{T}+\frac{Y^{4-4\sigma}}{T^5},
 \qquad W=\log(2L).
 \tag{40}
\]
它依赖已独立证明的实际素数乘积系数/间距预算，不依赖尺度选择。
本篇使用(40)，而非移用原算法输出；除以 \(M^4L\)，用(29)的
\(M^4\gg_{\sigma,\beta}Y^{2-4\sigma}\ell(Y)^4\)，即得
\[
 \frac{J_{4,>T}}{\mu^4}\ll_{\sigma,\beta}
 \frac{L}{T\ell^4}
 +\frac{Y^2W}{T^2L\ell^4}
 +\frac1{TL}
 +\frac{Y^2}{T^5L\ell^4}.
 \tag{41}
\]
这里的 \(\ell^4\) 来自本篇新记录的强质量，不是把275原来的
\(\sqrt\ell\) 门槛形式替换为 \(\ell\)。

因此定义
\[
 T_{\rm diag}(Y)=\frac{Y}{\ell(Y)^2}\sqrt{\frac{\log(2L)}L},
 \tag{42}
\]
便有 \(T_{\rm diag}/\sqrt L\to\infty\)、\(J_{4,>T_{\rm diag}}=O(\mu^4)\)。
在(41)中，四项依次为
\[
 \frac{L^{3/2}}{Y\sqrt W\,\ell^2},\qquad 1,\qquad
 \frac{\ell^2}{Y\sqrt{LW}},\qquad
 \frac{L^{3/2}\ell^6}{Y^3W^{5/2}},
\]
故除第二项外均趋零。对任意固定 \(\varepsilon>0\)，在更大阈值
\(\ell^\varepsilon T_{\rm diag}\) 外进一步有
\(J_{4,>\ell^\varepsilon T_{\rm diag}}/\mu^4=O(\ell^{-2\varepsilon})=o(1)\)；
其余三项仍被 \(Y^{-1}\) 或 \(Y^{-3}\) 的节省吸收。
**在(42)处只证明 \(O\)，不声称 \(o\)。**

结合(39)的低频、277-A在固定阈值以上的真实正通道双边比较，严格得到
\[
 J_4=O(\mu^4)
 \quad\Longleftrightarrow\quad
 Q_{\sqrt L<|\xi|\le T_{\rm diag}}(r)=O(M^4L)
 \quad\text{沿同一284-D序列}.
 \tag{43}
\]
充分性用低/中/高三个非负频带相加；必要性用中带最终高于277固定阈值。
相对于274的 \(T_*=Y\sqrt{W/L}\)，剩余频带上端确实缩小了 \(\ell^2\) 因子。
这仅是强质量与既有算术高频预算的直接合成；(43)右侧仍未证明，
也没有声称这是最优频率界。

### 6.2 同一新序列上的算术前缀接口 [T/O]

279的原应用绑定275序列，但其证明只用有限 Stieltjes 路径、真实连续 bulk
及尺度一致的历史 guard。对本篇(30)，同一有限证明给
\[
 |H_Y(u)|\ll_{\sigma,\beta}|M|e^{\delta(u-L)}
 \quad(0\le u\le L).
\]
取整数 \(2\le K\le Y/2\)，把 \(n\le K\) 及连续 \([1,K]\) 联合归为早段；
其 Fourier 端点公式与(37)相同，只把 \(L,M\) 换为 \(\log K,M(Y,K)\)。
由这个指数界积分及(38)的同一 Plancherel 证明，得到
\[
 Q_{|\xi|\le T}(r_e)\ll_{\sigma,\beta}
       M^4(K/N)^{4\delta}(L+T^2).
 \tag{44}
\]
这解释了为何证明不需要 dyadic 假设，也不需275指定的 guard 数值。
279的正源分母比较同样只用有限源与保留的 \([Y/2,Y]\) bulk，
故 \(K/Y\to0\) 时仍有 \(M_l/M,S_l/S,D_l/D\to1\)；
在固定阈值以上，原/尾部预算的 \(O\) 转移保持成立。

对 \(T=L,K=\lfloor N/L^h\rfloor\)，一般阈值为 \(h>1/(4\delta)\)，
因为(44)给 \(Q_{\le L}(r_e)/(M^4L)\ll L^{1-4\delta h}=o(1)\)；
等号只给 \(O(1)\)。
例如固定 \(\sigma=1/4,\beta=3/8,h>2\)，新的下一最小算术输入仍可先限定为
同一对角记录上
\[
 Q_{\sqrt L<|\xi|\le L}(r_l)\ll M^4L. \tag{45}
\]
它只是(43)的第一段；即使证明(45)也不自动闭合余下 \(L<|\xi|\le T_{\rm diag}\)。
没有把新选择规则或因果逆核当作此双误差预算的证明。

## 7. 依赖、循环性与停止边界

| 输入或步骤 | 作用 | 不可偷换的结论 |
|---|---|---|
| 真实匹配 Abel 权和 \(\widetilde R(1)=0\) | (5)的精确 Volterra 结构 | 非匹配端点需重建恒等式 |
| \(\delta>0\) | 正的 Laplace 解析带、可积逆核及275路径可积性 | \(\beta=\sigma\) 不在本证明范围 |
| Gamma 核无零及统一大频渐近 | (16)--(22)构造真正因果 \(L^1\) 逆 | 形式乘以 \(F^{-1}\) 本身不证明稳定逆 |
| 实际整数源的初等增长 | (24)把连续历史变成有限整数历史 | 不能无误差地等同两种最大值 |
| 283的独立强振荡 | (32)生成强度不损失的共尾记录 | 逆核本身既不产生振荡，也不产生 \(\sqrt\ell\) 因子 |
| \(\beta<1/2\) | (33)中正指数保留振荡强度 | 不能照搬到 \(\beta\ge1/2\) |
| 新固定 guard 常数 | (36)、(44)接回真实路径、低频与前缀 | 不声称是275原序列或原算法 |
| 274-A的实际统一乘积间距预算 | (40)--(43)与强质量合成缩小高频阈值 | 不由逆核或仅历史包络产生算术高频估计 |

逆核定理在更一般的局部有界可测历史上也成立，它只控制历史上确界，不控制
两份 discrepancy 的中频乘积或增量。因而与
[281的固定正整数替代源障碍](281-all-cutoff-chirp-obstruction.md)相容：
不能把一个 Abel 结构恒等式描述成新产生的中频正性。
本篇实际新选择所需的算术内容来自(3)，而不是非构造性完备化或逆变换本身。

新序列只证明整数对角 \(Y=N\) 的共尾存在性，不证明每个充分大整数、
每个 dyadic 窗口或 dyadic 对角都达到质量与 guard 条件。
返回原研究接口时必须保留这一量词区别。
数域 Weil 完整配置、Gamma gluing、上同调桥梁及无条件中频预算均仍开放。
特别，(3)的双向振荡并不保证(29)--(30)的绝对值记录有两种符号；
本篇没有提出这个额外结论。275的原认证算法保持原状，无需改写或废除。

主代理独立审阅全文；gap_exception_audit 与 midband_compute 独立逆向
复核了(5)--(39)，特别确认因果反演的方向、全半平面余项、整数历史和记录量词。
carrier_audit 完成写作和自审。新增(40)--(45)由主代理逐项重建有限接口，
gap_exception_audit 独立复核高频四项、首子带一般参数阈值和全部新序列量词。
内部证明不等于文献新颖性或外部同行评审。
