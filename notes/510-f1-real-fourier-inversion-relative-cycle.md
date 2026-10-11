# 510. 实位 Fourier–反演闭链与完整 Gamma 项的普通迹比较

2026-10-11。[T/R] 继续[508](508-f1-prime-gap-archimedean-mixed-test.md)、
[509](509-f1-real-cutoff-kernel-and-relative-boundary.md)。
在实际偶实位 Hilbert 空间上增加乘法反演边，构造按迹类取商的合法Hochschild一循环。
其普通边界迹等于固定完整实位项，含恒等元常数；508的缺失正值遂有实际局部闭链来源。
尚未把这条局部链提升到404的 \(S\)-unit 商表示，也没有证明全部Weil正性、主关系或RR。

## 1. 所有算子先由实际实位给定

取 \(\mathcal H_+=L^2(\mathbb R,dx)_{\rm even}\)，沿用509的加法 Fourier 变换。
乘法反演定义为
\[
 (\mathcal I\xi)(x)=|x|^{-1}\xi(x^{-1})\quad(x\ne0).
                                                               \tag{1}
\]
变元证明 \(\mathcal I\) 是酉自伴算子；它不是拟合目标值的谱乘子。
令
\[
 (W\xi)(u)=\sqrt2 e^{u/2}\xi(e^u),\quad
 (J\psi)(u)=\psi(-u),\quad
 \Pi=M_{\mathbf1_{(-\infty,0]}}.
                                                               \tag{2}
\]
\(W:\mathcal H_+\to L^2(\mathbb R,du)\) 酉，
\(W\mathcal I W^{-1}=J\)，且 \(\Pi\) 来自原 \(|x|\le1\) 红外投影。
新的实际酉边是
\[
 \mathsf S=W\mathcal F\mathcal I W^{-1}.                  \tag{3}
\]
本轮确实扩大了局部来源；不声称(1)已属于430的旧双有限位源代数。

对实 \(h\in C_c^\infty(\mathbb R)\)、\(h^\sharp=h\)，取
\[
 \eta(t)=e^{t/2}h(t)=\eta(-t),\quad
 \varphi(\tau)=\int_{\mathbb R}\eta(t)e^{-i\tau t}dt,\quad
 D=-i\partial_u,\quad A_\eta=\varphi(D),\quad C_\eta=\Pi A_\eta.
                                                               \tag{4}
\]
这里 \(A_\eta\) 正是509的实际 \(T_h\) 在偶对数坐标下的算子：
\(WT_hW^{-1}\psi(u)=\int\eta(t)\psi(u-t)dt\)。
两实符号的平均已消去奇子空间；没有再增添一个符号因子。

## 2. Mellin 计算固定实际相位及方向

采用酉 Fourier
\(\widehat\psi(\tau)=(2\pi)^{-1/2}\int e^{-i\tau u}\psi(u)du\)，
则实位Mellin是
\[
 (\mathcal M\xi)(\tau)=\pi^{-1/2}
       \int_0^\infty\xi(x)x^{-1/2-i\tau}dx.
\]
偶 Fourier 的 Mellin 核直接给
\[
 \mathcal M\mathcal F\mathcal M^{-1}=m(\tau)J_\tau,\qquad
 m(\tau)=\pi^{i\tau}
       \frac{\Gamma(1/4-i\tau/2)}{\Gamma(1/4+i\tau/2)},\qquad
 \widehat{\mathsf S}=M_m.                                \tag{5}
\]
例如先给余弦核乘 \(e^{-\epsilon x}\)，用
\(\int_0^\infty x^{s-1}\cos x\,dx=\Gamma(s)\cos(\pi s/2)\)
在 \(0<\operatorname{Re}s<1\) 计算，再用Gamma复制与反射公式。
所得因子为
\(2(2\pi)^{-s}\Gamma(s)\cos(\pi s/2)
=\pi^{1/2-s}\Gamma(s/2)/\Gamma((1-s)/2)\)；
代 \(s=1/2-i\tau\) 即(5)。在稠密的正半轴紧支光滑偶测试上完成计算，
用酉性延到 \(L^2\)。余弦 Mellin 公式来源核对
[NIST DLMF 5.9.6](https://dlmf.nist.gov/5.9.E6)。

特别地 \(|m|=1\)，且
\[
 \frac{m'(\tau)}{m(\tau)}=-i b(\tau),\qquad
 b(\tau)=\operatorname{Re}\psi(1/4+i\tau/2)-\log\pi,
 \quad \psi=\Gamma'/\Gamma.                             \tag{6}
\]
本约定中的 \(\log|x|\) 变为 \(i\partial_\tau\)，所以实际conductor
\(\log|x|+\mathcal F\log|x|\mathcal F^{-1}\) 的乘子为 \(b\)。
这个无界算子只在公共稠密域上作来源核对；闭链由(3)–(4)的有界算子构成。
\(m^{(j)}(\tau)=O_j((1+\log(2+|\tau|))^j)\)、\(j\le3\)，
由psi的竖线渐近与导数界得到；参见
[DLMF 5.11.2](https://dlmf.nist.gov/5.11.E2)，紧区间由Gamma无极点控制。
所需 \(b',b''\) 的一致界也直接由下一节使用的psi积分微分得到：
对 \(k=1,2\)，
\(\left|\psi^{(k)}(1/4+i\tau/2)\right|
 \le\int_0^\infty v^k e^{-v/4}/(1-e^{-v})\,dv<\infty\)。

## 3. 真正的商闭链：不是用有限截止乘积作电荷

取实际有界星代数
\[
 \mathfrak A_\infty=
  \operatorname{alg}^*(1,\mathsf S,\Pi,A_\eta:
                     \eta\in\mathcal S(\mathbb R))+\mathcal S_1,
 \quad \mathfrak Q_\infty=\mathfrak A_\infty/\mathcal S_1. \tag{7}
\]
任意Schwartz \(\eta\) 均定义有界 \(A_\eta\)；算术比较只需(4)的实偶紧支类。
令
\[
 c_h=q(\mathsf S^*)\otimes q(\mathsf S C_\eta),\qquad
 B_\eta=C_\eta-\mathsf S C_\eta\mathsf S^*.               \tag{8}
\]
其Hochschild边界正是 \(q(B_\eta)\)。下面独立证明 \(B_\eta\in\mathcal S_1\)，
因此(8)合法闭合，不能仅靠标量截止极限代替这个准入。

在频率表示中，\(\Pi\) 的分布核为
\[
 \tfrac12\delta(\xi-\zeta)+\frac{i}{2\pi}
                           \operatorname{PV}\frac1{\xi-\zeta}.
\]
共轭差消去 \(\delta\) 和对角主值奇点，给光滑普通核
\[
 K_\eta(\xi,\zeta)=\frac{i}{2\pi}
       \frac{1-m(\xi)\overline{m(\zeta)}}{\xi-\zeta}
                    \varphi(\zeta),\quad
 K_\eta(\tau,\tau)=-\frac{b(\tau)\varphi(\tau)}{2\pi}.     \tag{9}
\]
这个符号来自 \(\Pi_{u\le0}\)；若取相反半线，电荷相反。

## 4. 迹类准入的完整证明

令 \(H=1+\zeta^2-\partial_\zeta^2\) 为一维harmonic oscillator；
它的本征值为 \(2n+2\)，所以 \(H^{-1}\) 为Hilbert–Schmidt算子。
右乘 \(H\) 的核为
\[
 \widetilde K=(1+\zeta^2)K_\eta-\partial_\zeta^2K_\eta.   \tag{10}
\]
证明 \(\widetilde K\in L^2(\mathbb R^2)\)：

- 若 \(|\xi-\zeta|\le1\)，差商可写成
  \(-\overline{m(\zeta)}\int_0^1m'(\zeta+t(\xi-\zeta))dt\)。
  其前两次 \(\zeta\) 导数只需 \(m',m'',m'''\)，
  在这条宽度2的带中由(6)的polylog界和 \(\varphi\) 的Schwartz衰减控制。
- 若 \(|\xi-\zeta|>1\)，差商及前两次导数由
  \(O((1+\log(2+|\zeta|))^2)/|\xi-\zeta|\) 及更高负幂控制。
  对 \(\xi\) 的平方积分有限，\(\zeta^2\varphi,\varphi',\varphi''\)
  的快速衰减付清另一变量。

因此 \(B_\eta H\) 在Schwartz域上有Hilbert–Schmidt延拓；
\[
 B_\eta=(B_\eta H)H^{-1}\in\mathcal S_1.                 \tag{11}
\]
恒等式先在 \(H\mathcal S=\mathcal S\) 上验证，再用有界性延拓。
这一步只对右变量加oscillator，避免错误地要求左尾 \(1/\xi\) 具有平方矩。
同一估计还给连续准入界
\[
 \|B_\eta\|_1\le C_m\sum_{j=0}^2
 \|(1+\tau^2)(1+\log(2+|\tau|))^3\varphi^{(j)}(\tau)\|_2.
\]
\(C_m\) 只依赖固定实际相位；不是由目标Weil值指定的参数。

固定 \(0\le\chi\le1\) 光滑紧支、在 \([-1,1]\) 为1，
取 \(\chi_N(\tau)=\chi(\tau/N)\)，点态趋1且乘法算子强趋单位。
\(M_{\chi_N}B_\eta M_{\chi_N}\) 有光滑紧支核，双Fourier级数绝对收敛，
其普通迹为 \(\int\chi_N^2(\tau)K_\eta(\tau,\tau)d\tau\)。
迹类算子的强压缩在迹类范数中趋原算子；
而 \(b\varphi\) 可积，故支配收敛给
\[
 \operatorname{Tr}B_\eta
       =-\frac1{2\pi}\int_{\mathbb R}b(\tau)\varphi(\tau)d\tau.
                                                               \tag{12}
\]
没有仅凭连续核就假设无限对角迹公式。

## 5. 普通相对电荷与非零类

沿用[432](432-f1-relative-cycle-charge-and-source-invariant-cutoff.md)的普通电荷：
商一循环的有界提升满足 \(\sum[A_r,B_r]\in\mathcal S_1\)，
电荷为其普通迹。改变迹类提升不改变迹；二边界的交换子和恒为零。
故它下降到 \(HH_1(\mathfrak Q_\infty)\)，且
\[
 \Omega_\infty(c_h)
 =\operatorname{Tr}[\mathsf S^*,\mathsf S C_\eta]
 =\operatorname{Tr}B_\eta.                              \tag{13}
\]
在508测试上下一节给严格正值，所以该链不是商二边界。
这不同于交换乘子链 \(m^{-1}\otimes m\) 的Hilbert交换子零，也不同于509两积均迹类的零电荷。
对非零 \(\eta\)，\(C_\eta\) 非紧：它在 \(u\to-\infty\) 的平移上保留非零卷积响应；
两个顺序乘积不属于 \(\mathcal S_1\)，只有差已由(11)付清。
这是测试加权的 \(HH_1\) 电荷，未认证为整数Fredholm指数；
未加权 \(\varphi=1\) 不在本次Schwartz准入域。

把红外边界移到 \(|x|\le e^a\)，得到 \(\Pi_a\)；
平移与 \(\mathsf S,A_\eta\) 交换，使 \(B_{\eta,a}\) 为 \(B_{\eta,0}\) 的酉共轭。
普通电荷保持，不通过自由有限部指定常数。

## 6. 全部原sharp紧支测试的实位比较，含恒等元

psi的积分公式
[DLMF 5.9.16](https://dlmf.nist.gov/5.9.E16) 给
\[
 \psi(z)+\gamma=\int_0^\infty
                   \frac{e^{-v}-e^{-zv}}{1-e^{-v}}dv
                  \quad(\operatorname{Re}z>0).
\]
代 \(z=1/4+i\tau/2\)，与(12)配对并变 \(v=2t\)，得到
\[
 \Omega_\infty(c_h)
 =(\log\pi+\gamma)\eta(0)
  +2\int_0^\infty
        \frac{e^{-t/2}\eta(t)-e^{-2t}\eta(0)}{1-e^{-2t}}dt
 =2\mathcal A(h)+(\log\pi+\gamma)h(0),                   \tag{14}
\]
\[
 \mathcal A(h)=\int_0^\infty
                      \frac{e^{2t}h(t)-h(0)}{e^{2t}-1}dt.
\]
换序不能拆掉近零抵消。将
\(e^{-2t}-e^{-t/2}\cos(\tau t)\) 整体处理：
在 \(0<t\le1\) 除以 \(1-e^{-2t}\) 后由 \(C(1+\tau^2)\) 控制，
与Schwartz \(\varphi\) 可绝对积分；远处有指数衰减。
Fourier反演给 \((2\pi)^{-1}\int\varphi=\eta(0)\) 及
\((2\pi)^{-1}\int\varphi\cos(\tau t)=\eta(t)\)，因此(14)合法。

(14)正是405固定加法字符下的完整 \(L_\infty(h)\)；
实位恒等元常数也由实际 Fourier–反演相位确定，没有待选的 \(\delta_0\)。
对508的同一混合 \(h\)，\(h(0)=0\)，于是
\[
 \boxed{\tfrac12\Omega_\infty(c_h)
          =\mathcal A_\infty(h)=W_{\rm pol}(f,g)>0.}      \tag{15}
\]
结合509，还得到在这一测试上的实际标量比较
\[
 \Omega_\infty(c_h)=\lim_{\Lambda\to\infty}
                       \operatorname{Tr}(Q_\Lambda P_\Lambda T_h),
\]
具有509(9)的显式误差。不是把截止强极限当成迹类范数极限。

## 7. 本轮推进与下一关口

本轮跨过的是**局部偶实位的非零相对闭链与完整实位标量比较**。
实际反演、Fourier和红外投影先给定；Gamma是其Mellin计算结果。
局部Gamma及conductor机制属于经典来源；不主张世界首次，
本项目新进展是给508指定混合测试支付普通迹类边界，并与404–405接口接合。

下一步应在404的同一 \(S=\{\infty,2,5\}\) 周期化商表示中实现相应边，
证明 \(S\)-unit 等价类上的算子良定义、实际 Fourier/Mellin 比较、
同一相对理想中的边界准入，以及有限位项与实位项的共同读出。
局部(1)的反演不能未经证明就作为该商上的算子；
经典局部gamma乘积也不能代替同一商表示的证明。
若先试局部有限位闭链，须固定真实Haar、反演及单位壳层；
不能把三个标量加起来就命名为全局几何对应。

后续主商仍须保留405的两次数与完整混合根空间。
没有全测试类Weil正性、算术主除子、有效截面或RR，
没有新的零点比例或无零边界。本轮也未新增Lean或内核认证。

本轮[核与边项审查](../reviews/2026-10-11/f1-real-cutoff-kernel-review.md)、
[闭链逆审](../reviews/2026-10-11/f1-real-relative-cycle-review.md)与
[谱桥逆审](../reviews/2026-10-11/f1-real-spectral-bridge-review.md)分别保留实际阅读范围。
[数值诊断](../reviews/2026-10-11/f1-real-relative-cycle-diagnostics.json)由
[脚本](../scripts/real_relative_cycle_diagnostics.py)复算核积分、Gamma相位与完整时间／谱配对。
非紧支Gaussian测试仅作诊断；浮点结果不证明迹类准入、无限比较或RH。
