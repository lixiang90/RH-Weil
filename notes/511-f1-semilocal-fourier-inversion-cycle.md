# 511. 同一有限 S-unit 商上的 Fourier–反演闭链

2026-10-11。[T/R] 继续[510](510-f1-real-fourier-inversion-relative-cycle.md)。
在[404](404-f1-adelic-periodic-orbits-and-mixed-local-trace.md)的同一半局部 Hilbert 表示中，
证明周期化像稠密、真实反演、共同 Fourier 的径向符号及整个空间的迹类边界。
固定 \(S=\{\infty,2,5\}\) 给这三个完整局部项；覆盖全部相关素数时才等于原固定 \(N\)。
几何主关系、全局Weil负性与RR仍开放。

## 1. 原完成覆盖整个乘法商，并明确Haar常数

先固定 \(S=\{\infty,2,5\}\)，写
\[
 A_S=\mathbb R\times\mathbb Q_2\times\mathbb Q_5,\quad
 O_S^\times=\{\pm2^m5^n:m,n\in\mathbb Z\},\quad
 J_S=A_S^\times,\quad C_S=O_S^\times\backslash J_S.
\]
每个乘法类恰有一个代表落在
\[
 \Delta=(0,\infty)\times\mathbb Z_2^\times\times\mathbb Z_5^\times,
 \quad C_S\simeq\mathbb R_+^\times\times K_S,\quad
 K_S=\mathbb Z_2^\times\times\mathbb Z_5^\times.             \tag{1}
\]
令 \(d^\times c=dr/r\,d\kappa\)，\(d\kappa\) 为紧群概率Haar，\(|c|=r\)。
沿用原周期化与范数
\[
 E_SF(c)=\sum_{q\in O_S^\times}F(qx),\qquad
 \|F\|_{X_S}^2=\int_{C_S}|E_SF(c)|^2|c|d^\times c.        \tag{2}
\]
Connes §VII证明它对全部 \(\mathcal S(A_S)\) 有意义，没有零值或零积分限制。
任意 \(g\in C_c^\infty(C_S)\) 在 \(\Delta\) 上提升、其余延零，
得到 \(F_g\in C_c^\infty(J_S)\subset\mathcal S(A_S)\)。
实支集远离0，有限单位壳层clopen，因此延零光滑。
在 \(\Delta\) 上周期化只留下 \(q=1\)，故 \(E_SF_g=g\)。
这些函数在带权 \(L^2\) 中稠密，分离后的完成于是给酉识别
\[
 \mathcal H_S=L^2(X_S)\simeq L^2(C_S,|c|d^\times c).       \tag{3}
\]
这只识别Hilbert完成，没有把 \(X_S\) 的拓扑或结构层等同于 \(C_S\)。

实位 \(dx\)、有限位自对偶加法Haar \(\operatorname{vol}\mathbb Z_p=1\) 给
\[
 dx_S|_\Delta=\rho_S|c|d^\times c,\quad
 \rho_S=\prod_{p\in S_f}(1-p^{-1})=2/5,\quad
 \|E_SF\|^2=\rho_S^{-1}\sum_q\langle F,U(q)F\rangle_{\rm add}. \tag{4}
\]
在本稿固定测度下，原文类型的内积展开需要保留该因子。
因 \(|q|_S=1\)，加法Fourier将(4)的 \(q\) 换成 \(q^{-1}\)，保持范数。
采用实位 \(e^{-2\pi ixy}\) 及导子 \(\mathbb Z_p\) 的自对偶有限位字符，
引用固定[Connes v1](../literature/f1/connes-trace-math-9811068v1.pdf)
§VII Lemma1/PDF29–31，获得共同 Fourier \(\mathcal F_S\) 的唯一酉延伸。
本轮根线程核读PDF29–36；这个引用没有RH前提。

## 2. 真实反演从稠密紧支源下降

在(3)定义
\[
 (\mathcal I_S\xi)(c)=|c|^{-1}\xi(c^{-1}).                  \tag{5}
\]
乘法Haar保持反演，换元证明其酉、自伴、平方为单位。
对 \(F\in C_c^\infty(J_S)\)，定义
\(\mathcal I_{\rm src}F(x)=|x|^{-1}F(x^{-1})\) 并延零；
它仍属于加法Schwartz，且 \(|q|_S=1\) 给
\[
 E_S\mathcal I_{\rm src}F(c)=|c|^{-1}E_SF(c^{-1}).          \tag{6}
\]
因此(5)有稠密真实源上的交织与唯一连续延伸。
不主张逐点反演保持所有 \(\mathcal S(A_S)\)。

原非酉缩放 \(U(a)\xi(c)=\xi(a^{-1}c)\) 满足
\[
 \mathcal F_SU(a)=|a|U(a^{-1})\mathcal F_S,\qquad
 \mathcal I_SU(a)=|a|U(a^{-1})\mathcal I_S.
\]
第一式从共同加法Fourier的源变元延伸，第二式从(5)计算。
故真实酉算子 \(\mathsf S_S=\mathcal F_S\mathcal I_S\) 与全部缩放交换。
这里使用共同 \(\mathcal F_S\)，没有假设单个部分 Fourier \(\mathcal F_p\)
能各自下降到同一S-unit商。

## 3. 用同一稠密源族计算径向 Fourier

令 \(P_0=\int_{K_S}U(k)d\kappa\)，\(\mathcal H_{S,0}=P_0\mathcal H_S\)。
Fourier与反演各将 \(U(k)\) 换成 \(U(k^{-1})\)，所以这个块对两者均reducing。
其酉对数坐标与谱Fourier为
\[
 W_S\xi(u)=e^{u/2}\xi(e^u),\qquad
 \widehat v(\tau)=(2\pi)^{-1/2}\int e^{-i\tau u}v(u)du.     \tag{7}
\]
此处是商的单个正实代表，不再加510偶实位坐标的 \(\sqrt2\)。

取真实源 \(F_\phi=\phi\otimes\mathbf1_{\mathbb Z_2}\otimes\mathbf1_{\mathbb Z_5}\)，
\(\phi\in\mathcal S(\mathbb R)_{\rm even}\)。单位球条件与实符号给
\[
 E_SF_\phi(r,\kappa)=2\sum_{m,n\ge0}\phi(2^m5^nr).         \tag{8}
\]
记 \(v_\phi(u)=e^{u/2}\phi(e^u)\)、\(T_Lv(u)=v(u+L)\)，则
\[
 W_SE_SF_\phi=
 2(1-2^{-1/2}T_{\log2})^{-1}(1-5^{-1/2}T_{\log5})^{-1}v_\phi. \tag{9}
\]
几何级数在算子范数中绝对收敛，逆也有界。
任意 \(v\in C_c^\infty(\mathbb R)\) 可取
\(\phi(r)=r^{-1/2}v(\log r)\) 并偶延拓，故这个源族在径向块稠密。

对 \(\operatorname{Re}s>0\)，Schwartz与几何级数允许绝对Mellin换序：
\[
 M(E_SF_\phi)(s)=\frac{2M\phi(s)}{(1-2^{-s})(1-5^{-s})},
 \quad M\phi(s)=\int_0^\infty\phi(r)r^{s-1}dr.             \tag{10}
\]
自对偶单位球的Fourier仍是自身，共同 \(\mathcal F_S\) 只把 \(\phi\)
换成 \(\mathcal F_\infty\phi\)。在 \(0<\operatorname{Re}s<1\) 上，
510的实际偶Mellin计算给
\[
 M(\mathcal F_\infty\phi)(s)=
 \pi^{1/2-s}\frac{\Gamma(s/2)}{\Gamma((1-s)/2)}M\phi(1-s).
\]
在 \(s=1/2-i\tau\) 上因此得到实际算子
\[
 \widehat{\mathcal F_S}=M_{m_S}J_\tau,\quad
 \widehat{\mathsf S_S}=M_{m_S},\quad
 m_S(\tau)=m_\infty(\tau)\prod_{p\in S_f}
 \frac{1-p^{-1/2}e^{-i\tau\log p}}{1-p^{-1/2}e^{i\tau\log p}},
                                                               \tag{11}
\]
\[
 m_\infty(\tau)=\pi^{i\tau}
       \frac{\Gamma(1/4-i\tau/2)}{\Gamma(1/4+i\tau/2)}.
\]
计算先在真实稠密族成立，再由酉性延拓。
这是共同来源的因子分解，没有按局部标量拼接定义 \(\mathcal F_S\)。
任意其他固定有限 \(S_f\) 可用 \(\prod_{p\in S_f}\mathbf1_{\mathbb Z_p}\) 同样证明。

## 4. 真实紧群平均支付整个空间的迹类边界

对实 \(h\in C_c^\infty(\mathbb R)\)、\(h^\sharp=h\)，取
\[
 h_S(c)=h(\log|c|),\quad \eta(t)=e^{t/2}h(t),\quad
 \varphi(\tau)=\int\eta(t)e^{-i\tau t}dt,\quad
 A_h=U(h_S),\quad \Pi=M_{\{|c|\le1\}},\quad C_h=\Pi A_h.    \tag{12}
\]
\(\eta\) 实偶。共同群积分的紧群平均准确给
\[
 A_h|_{\mathcal H_{S,0}}=\varphi(D),\quad
 A_h|_{\mathcal H_{S,0}^\perp}=0,\quad D=-i\partial_u.      \tag{13}
\]
\(\Pi\) 与 \(P_0\) 交换。因此没有张量有限位单位引入无限迹重数。
对一般Schwartz \(\eta\)，可用规范化酉dilation的可积群积分定义 \(\varphi(D)P_0\)；
本稿算术输入始终采用(12)的紧支 \(h_S\)。

在由 \(1,\mathcal F_S,\mathcal I_S,P_0,\Pi\)、
\(U(g)\)（\(g\in C_c^\infty(C_S)\)）及全部
\(\mathcal S_1(\mathcal H_S)\) 生成的星代数 \(\mathfrak A_S\) 中，按迹类取商，
定义
\[
 c_{S,h}=q(\mathsf S_S^*)\otimes q(\mathsf S_SC_h),\quad
 B_{S,h}=C_h-\mathsf S_SC_h\mathsf S_S^*.                  \tag{14}
\]
整个空间的边界是径向边界加零块。写 \(m_S'/m_S=-ib_S\)，则
\[
 b_S(\tau)=b_\infty(\tau)
 -2\sum_{p\in S_f}\log p\sum_{n\ge1}p^{-n/2}\cos(n\tau\log p),
 \quad b_\infty=\operatorname{Re}\psi(1/4+i\tau/2)-\log\pi. \tag{15}
\]
有限位相位各阶导数有界，固定 \(S\) 的 \(m_S^{(j)}\)、\(j\le3\) 仍为polylog界。
径向核
\[
 K_{S,h}(\xi,\zeta)=\frac{i}{2\pi}
 \frac{1-m_S(\xi)\overline{m_S(\zeta)}}{\xi-\zeta}\varphi(\zeta)
\]
完全满足510的右变量谐振子证明：
\(B_{S,h}H\in\mathcal S_2\)、\(H^{-1}\in\mathcal S_2\)，其中
\(H=1+\zeta^2-\partial_\zeta^2\)。
径向边界迹类，加零块后仍在整个 \(\mathcal H_S\) 的 \(\mathcal S_1\) 中。
510的强压缩对角迹证明遂给真正商闭链及普通电荷
\[
 \Omega_S(c_{S,h})=\operatorname{Tr}B_{S,h}
                  =-\frac1{2\pi}\int b_S\varphi.          \tag{16}
\]
常数依赖固定 \(S\)；没有随 \(S\) 一致的迹类界。

## 5. 完整局部和、两个混合检验与量词

(15)的级数绝对收敛，Fourier反演及
\(p^{-n/2}\eta(n\log p)=h(n\log p)\) 给有限位贡献
\(2\sum_{p\in S_f}\log p\sum_{n\ge1}h(n\log p)\)。
结合510含恒等元的实位比较，得到
\[
 \boxed{\tfrac12\Omega_S(c_{S,h})=N_S(h)},\qquad
 N_S(h)=\sum_{p\in S_f}\log p\sum_{n\ge1}h(n\log p)
       +\mathcal A(h)+\tfrac{\log\pi+\gamma}{2}h(0),       \tag{17}
\]
\[
 \mathcal A(h)=\int_0^\infty\frac{e^{2t}h(t)-h(0)}{e^{2t}-1}dt.
\]
自对偶单位球固定有限位单位壳层正规化，没有新增自由 \(\delta_0\)。

508同一间隙测试的正支集在 \((\log2,\log3)\)，全部素数幂求值为零；
在 \(S=\{\infty,2,5\}\) 的整个商上
\[
 \tfrac12\Omega_S=\mathcal A_\infty(h)=W_{\rm pol}(f,g)>0.
\]
所以这次非零 \(HH_1\) 类已在404的同一半局部来源中。
403的 \(\log2\) 分离例子若支集小到只命中2，
半电荷也准确为 \(\log2\,h(\log2)+\mathcal A_\infty(h)>0\)。

对任意原紧支实 \(f,g\)，令 \(h=(f*g^\sharp+g*f^\sharp)/2\)，
取 \(M\) 覆盖 \(\operatorname{supp}h\)。
若固定 \(S_f\) 包含全部 \(p\le e^M\)，遗漏素数幂的求值为零，(17)才给
\[
 \tfrac12\Omega_S(c_{S,h})=N(h)=W_{\rm pol}(f,g).          \tag{18}
\]
不声称三个固定位置对全部紧支测试已给完整 \(N\)。

若 \(h\) 在0附近消失，Connes Theorem4还给同一来源的标量比较
\[
 \Omega_S(c_{S,h})=\lim_{\Lambda\to\infty}
 \operatorname{Tr}((\mathcal F_SP_\Lambda\mathcal F_S^{-1})
                         P_\Lambda U(h_S)).
\]
这是消费已证半局部迹定理，没有交换普通迹与强极限。
一般 \(h(0)\ne0\) 的常数已由(16)固定；
这里不另认证每种硬截止主项的有限部分。

## 6. 下一关口

本轮支付了同一有限 \(S\) 的来源融合、普通闭链和两个必要混合测试。
扩大有限 \(S\) 后对固定 \(h\) 的标量稳定，没有提供不同商复形的相容映射、
全adele链或迹类范数极限。
[512](512-f1-finite-place-double-moment-sign-test.md)进一步给固定 \(S\)
在双矩零目标符号上的严格检验。
后续主关系仍须同时落入[405](405-f1-adelic-restriction-moments-and-radical.md)
的两次数与完整混合根空间；对应复合、有效性、Hodge不等式及RR都不能由(18)替代。
