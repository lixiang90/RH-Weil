# 518. 全重数消失后的定量Mellin除法与真实Möbius源

2026-10-11。[T/R] 接续[405](405-f1-adelic-restriction-moments-and-radical.md)、
[516](516-f1-global-mixed-radical-and-mellin-jets.md)。
本稿支付此前未完成的增长条件：完整零点jets消掉后，除以ζ的固定条带快速衰减自动成立。
再由实际Möbius逆和逆Mellin恢复405原源，不假设RH、简单零点或零点间距下界。

## 1. 同一目标空间与完整重数

全部空间及拓扑采用405：
\[
 \mathcal S_{\exp}
 =\{f\in C^\infty(\mathbb R,\mathbb R):
        p_{N,j}(f)=\sup_t e^{N|t|}|f^{(j)}(t)|<\infty,\ \forall N,j\}.
\]
令 \(M_f(s)=\int e^{st}f(t)dt\)，ρ遍历不同的非平凡ζ零点，重数为mρ。
定义闭子空间
\[
 \mathcal R_{\rm jet}
 =\{f\in\mathcal S_{\exp}:
       M_f^{(j)}(\rho)=0,\ 0\le j<m_\rho,\ \forall\rho\}.       \tag{1}
\]
这里没有添加两个次数条件。每个导数求值由指数半范数控制，故(1)闭。
516已证原源像 \(J=E(\mathscr S_{e,0})\) 包含于(1)，本稿证明反向。

## 2. 不需要零点分离的局部除法估计

设F,H在闭圆盘 \(|w|\le3R\) 的邻域全纯，F(0)≠0，
且Q=H/F在整个圆盘全纯延拓。记
\[
 m=|F(0)|,\quad M=\max_{|w|\le3R}|F(w)|,\quad
 A=\max_{|w|\le3R}|H(w)|.
\]
则
\[
 \boxed{\max_{|w|\le R}|Q(w)|\le A\,M^2/m^3.}                \tag{2}
\]

H恒零时显然。否则选 \(r\in(2R,3R)\)，使F在半径r的圆周无零点；
紧盘内仅有有限个零点，故可选。令圆周上
\(u=\log M-\log|F|\ge0\)。Jensen的中心平均不等式给
\[
 \frac1{2\pi}\int_0^{2\pi}u(re^{i\theta})d\theta
       \le\log M-\log m.                                    \tag{3}
\]
对 \(|w|\le R\)，正规化Poisson核至多
\((r+|w|)/(r-|w|)<3\)。因此
\[
 P_r[\log|F|](w)
   =\log M-P_r[u](w)\ge-2\log M+3\log m.                     \tag{4}
\]
\(\log|Q|\) 次调和，圆周上
\(\log|Q|=\log|H|-\log|F|\)，故
\[
 \log|Q(w)|\le\log A-P_r[\log|F|](w)
             \le\log A+2\log M-3\log m.
\]
H或Q的圆周零点不影响可积的对数和次调和不等式；Q恒零已单独处理。
这证明(2)。没有估计零点彼此距离，也没有在零点附近点态估计1/F。
关键前提是商在整盘已经全纯；只消掉重零点的一次值不能套用此引理。

## 3. ζ商的全部固定条带快速衰减

对 \(f\in\mathcal R_{\rm jet}\) 令
\[
 G_f(s)=\frac{M_f(s)}{2\zeta(s)}.                             \tag{5}
\]
完整jets消掉全部非平凡零点。ζ的负偶整数零点简单，故G仅可在
\(-2,-4,\ldots\) 有简单极；ζ在1的极反而使 \(G_f(1)=0\)。
ζ(0)=−1/2保证0处没有极。

固定 \(|\Re s|\le B\)，取 \(R>B+3\)，圆心为 \(2+iT\)。
当 \(|T|>3R+2\)，外盘不含ζ的极或任何平凡零点，G在整盘全纯。
绝对Euler逆给统一锚点
\[
 |\zeta(2+iT)|\ge1/\zeta(2).                                 \tag{6}
\]
在扩大后的任意固定实部带内，存在只依赖R的C、b，使
\[
 \max_{|w|\le3R}|\zeta(2+iT+w)|
                       \le C_R(1+|T|)^{b_R}.                \tag{7}
\]
这是无条件的固定条带多项式上界。
可从[NIST DLMF 25.2.10](https://dlmf.nist.gov/25.2#E10)的有限阶
Euler–Maclaurin展开取得：固定足够大的阶数，使周期Bernoulli积分
在条带最左实部也绝对收敛；其系数仅为固定次数的s多项式。
这里不消费任何无零条带或最新边界。

对(2)取F=ζ、H=M_f/2。由(6)–(7)，
\[
 \sup_{|w|\le R}|G_f(2+iT+w)|
 \le C_R(1+|T|)^{2b_R}
                  \sup_{|w|\le3R}|M_f(2+iT+w)|.              \tag{8}
\]
在任意固定 \(|\sigma|\le L\) 带内，分部积分给
\[
 |M_f(\sigma+i\tau)|
 \le 2p_{\lceil L\rceil+1,j}(f)|\tau|^{-j},
                     \quad|\tau|\ge1.                       \tag{9}
\]
取j任意大就吸收(8)的固定多项式损失。因此对所有B、n、k，
\[
 \sup_{|\sigma|\le B,\ |\tau|\ge1}
      (1+|\tau|)^n|G_f^{(k)}(\sigma+i\tau)|<\infty.            \tag{10}
\]
高处导数由带内留余量的固定半径Cauchy估计取得；
有界高度、\(|\tau|\ge1\) 的剩余紧集由可去除法控制。
相应常数由f的有限个指数半范数控制。
实轴上的负偶极不能混进(10)，也没有被强行消掉。

## 4. 先构造真正的正实源

对r>0定义
\[
 \boxed{\theta_f(r)=\frac12\sum_{n\ge1}\mu(n)f(\log(nr)).}    \tag{11}
\]
这是实际Möbius函数，不按零点任意拼出符号。
对任意N>1，\(|f^{(j)}(\log nr)|\le p_{N,j}(f)(nr)^{-N}\)；
故(11)及其全部Euler导数 \(L_r=r\partial_r\) 在r的紧子区间绝对一致收敛。
普通导数是 \(r^{-j}\) 乘Euler导数多项式，所以θ在r>0光滑，
在r≥1的全部普通导数任意阶快速衰减。

在 \(\Re s>1\)，由
\(\sum n^{-\Re s}\int e^{\Re s\,t}|f(t)|dt<\infty\) 支付Fubini：
\[
 \int_0^\infty\theta_f(r)r^{s-1}dr
     =\frac12M_f(s)\sum_{n\ge1}\frac{\mu(n)}{n^s}
     =G_f(s).                                               \tag{12}
\]
固定σ>1，\(e^{\sigma u}\theta_f(e^u)\) 是Schwartz函数：
大正u用上述更大N界；大负u对f的双端快速衰减在乘法格点和中分段，
可得每阶Euler导数 \(O(e^{-u})\)，σ>1足以支付。
也可用绝对加权L¹的各阶导数与(12)的Fourier唯一性得到同一逆变换。
由逆Mellin，
\[
 \theta_f(r)=\frac1{2\pi i}
        \int_{\sigma-i\infty}^{\sigma+i\infty}G_f(s)r^{-s}ds. \tag{13}
\]

## 5. 平凡零点的留数支付偶原点Taylor展开

对任意K≥1，将(13)左移到 \(c_K=-2K-1\)。
(10)使全部水平边及带有限Euler导数的水平边趋零。
只经过负偶整数的可选简单极，其留数为
\[
 \alpha_k=\frac{M_f(-2k)}{2\zeta'(-2k)}.                     \tag{14}
\]
因此
\[
 \theta_f(r)=\sum_{k=1}^K\alpha_k r^{2k}+\mathcal E_K(r),
 \qquad L_r^j\mathcal E_K(r)=O_{f,K,j}(r^{2K+1}),
                      \quad0<r\le1.                        \tag{15}
\]
普通j阶导数的余项为 \(O(r^{2K+1-j})\)。对每个j可取K任意大，
故偶延拓 \(\theta_f(-r)=\theta_f(r)\) 在0光滑，且
\[
 \theta_f(0)=0,\quad
 \theta_f^{(2k)}(0)=(2k)!\alpha_k,\quad
 \theta_f^{(2k+1)}(0)=0.                                    \tag{16}
\]
θ是实偶Schwartz函数，通常并非原点平坦，也不要求Taylor级数收敛。
平凡零点在这里保留为源的偶Taylor数据。

现在真正的θ Mellin积分在 \(\Re s>-2\) 全纯，与(12)解析延拓一致。
由 \(G_f(1)=0\)，
\[
 \int_{\mathbb R}\theta_f(r)dr=2G_f(1)=0.                    \tag{17}
\]
于是θ进入405完全相同的合法源空间
\(\mathscr S_{e,0}=\{\theta\in\mathscr S(\mathbb R,\mathbb R):
 \theta\text{偶},\theta(0)=0,\int\theta=0\}\)。

## 6. 原E映射的点态重建

对固定r>0和N>1，
\[
 \sum_{k,n\ge1}|f(\log(nkr))|
             \le p_{N,0}(f)r^{-N}\zeta(N)^2.                 \tag{18}
\]
故可按除数合法分组：
\[
 2\sum_{k\ge1}\theta_f(kr)
   =\sum_{m\ge1}f(\log(mr))\sum_{n\mid m}\mu(n)
   =f(\log r).                                              \tag{19}
\]
这准确重建实际 \(E\theta_f=f\)，含原因子2。
没有将只在Re s>1的形式Euler逆直接当成原点平滑性；
这项平滑性由(2)–(16)另行支付。

完整闭像、两次数与来源相容见[519](519-f1-closed-source-image-and-degree-moments.md)，
实际Fréchet商的谱与增长关口见[520](520-f1-source-quotient-spectrum-and-centered-growth.md)。
本稿不提供独立Weil符号、几何principal或全局HH链。
