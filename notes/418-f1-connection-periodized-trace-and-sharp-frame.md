# 418. 连接纠正后的原Γ周期化迹与近锐分割检验

2026-09-21。[T/O] 全文独立逆审通过。从[417](417-f1-projection-connection-and-time-evolution.md)的实际连接继续。
本稿在[414](414-f1-deep-boundary-unitary-and-time-defect.md)的原表示与原截止中
完成连接时间的迹类比较；最后检验这项直接纠正能否承担指定的边界周期差。
未改变通常ζ、原有理数作用、测试类或验收目标。

## 1. 对象与证明路线

固定 \(L=\log p,M=\log q,\rho_p=p^{-1/2},\rho_q=q^{-1/2}\)，
\(\Gamma=\mathbb Z^2\)，\(\ell_g=g_1L+g_2M\)。
原协变表示中的 \(P_g\) 同时作径向和时间平移；额外时间为 \(U_s\)。
417的实际连接具有有限形式
\[
 K=\sum_{n\in F}\kappa_n(t)P_{(n,0)},\qquad
 \kappa_n=c'(t)c(t-nL)-c(t)c'(t-nL),\quad K^*=-K.       \tag{1}
\]
\(F\subset\mathbb Z\) 有限，所有系数光滑紧支。
令
\[
 W'_s=\beta_{-s}(K)W_s,\quad W_0=1,\qquad U_s^c=U_sW_s.
\]
417已构造这个酉演化。这里始终保留 \(P_gU_sW_s\) 的次序；
不能假定 \(P_g\) 与 \(U_s^c\) 交换。

沿用原 \(C_N=E_p\otimes M_c+E_q\otimes M_{d_q}\)，记 \(d_p=c\)。
\(E_p=R_{N_p,p}\otimes S_{N_q,q}\)，
\(E_q=S_{N_p,p}\otimes R_{N_q,q}\)，
\(S_{N,r}=R_{N+1,r}-R_{N,r}\)，\(N_p,N_q\ge0\)。
\(d_r\) 是长度 \(l_p=L,l_q=M\) 的光滑紧支实非负平方分割，
所以 \(\int d_r^2=l_r\)。这里 \(C_N\) 为原有正算子，不是投影。

本稿依次证明
\[
 A_N^c(h)=\sum_{g\in\Gamma}C_NP_gU^c(h)C_N,\qquad
 U^c(h)=\int h(s)U_s^c\,ds,\quad h\in C_c^\infty(\mathbb R)         \tag{2}
\]
在每个固定 \(N\) 下绝对迹范数收敛，计算全部标量周期系数，
给出有限阶 Dyson 误差界，再证明在原近锐分割族中其 \(p\) 周期纠正趋零。
\(U^c(h)\) 的第一重定义为强算子积分；迹类性质必须另外支付。

## 2. 带群权和时间导数的 Dyson 系数

写 \(W_s=\sum_n w_n(s,t)P_{(n,0)}\)。
\(w_n=\mathbf1_{n=0}+\sum_{r\ge1}w_n^{(r)}\) 的第 \(r\) 阶公式为
\[
 w_n^{(r)}(s,t)=s^r
 \sum_{\substack{n_1,\ldots,n_r\in F\\\sum n_j=n}}
 \int_{\Delta_r}
 \prod_{j=1}^r
 \kappa_{n_j}\left(t+s\theta_j-L\sum_{i<j}n_i\right)d\theta,
 \quad
 \Delta_r=\{1\ge\theta_1\ge\cdots\ge\theta_r\ge0\}.                 \tag{3}
\]
\(|\Delta_r|=1/r!\)。负 \(s\) 的方向已包含在 \(s^r\) 中；
不能在负时间去掉此符号后沿用正时间排序。

取 \(\operatorname{supp}h\subset[-S,S]\)，\(S\ge1\)，并设
\[
 b_n=\max_{0\le j\le4}\|\kappa_n^{(j)}\|_\infty,\quad
 B_4=\sum_{n\in F}\rho_p^{-|n|}b_n,\quad X=SB_4.
\]
令
\[
 e_{n,r}=\max_{a+b\le4}\sup_{|s|\le S,t\in\mathbb R}
       |\partial_s^a\partial_t^b w_n^{(r)}(s,t)|.
\]
逐项微分(3)：\(s^r\) 的 \(i\) 阶导数至多支付 \(r^iS^r\)，
其余 \(a-i+b\) 次导数分配到 \(r\) 个因子至多支付 \(r^{a-i+b}\)；
对 \(s\) 求导只多出绝对值至多1的 \(\theta_j\)。
累积群移位与 \(s,t\) 无关，不产生隐藏群指数因子。
Leibniz分配的系数和至多 \(2^a\le16\)。
再用 \(\rho_p^{-|\sum n_j|}\le\prod_j\rho_p^{-|n_j|}\)，得到
\[
 \sum_n\rho_p^{-|n|}e_{n,r}
       \le16(r+1)^4\,\frac{X^r}{r!}.                             \tag{4}
\]
因而若 \(e_n\) 是整个 \(w_n\) 的同一四阶上确界，
\[
 \sum_n\rho_p^{-|n|}e_n
 \le {\cal B}_4(S):=1+16\sum_{r\ge1}(r+1)^4\frac{X^r}{r!}<\infty. \tag{5}
\]
对任意更高固定导数阶数亦有阶乘支配，所以系数联合光滑。
这些估计也可视为在系数范数
\(\sum_n\rho_p^{-|n|}\sum_{j=0}^4\|\partial_t^ja_n\|_\infty/j!\)
中的 Dyson 构造：平移保范数，群权次乘，Leibniz给乘法连续。
表示后的解由417的有界ODE唯一性识别为原 \(W_s\)。

## 3. 本题有比一般有限带指数更强的支集控制

取紧区间 \(J\) 同时包含各 \(\operatorname{supp}\kappa_n\) 和
\(\operatorname{supp}\kappa_n-nL\)。
(3)中非零路径的首末因子分别给
\[
 t+s\theta_1\in J,\qquad t-nL+s\theta_r\in J.
\]
因此对于 \(|s|\le S\)，
\[
 t,\ t-nL\in J+[-S,S],\qquad |n|L\le\operatorname{diam}J+S.        \tag{6}
\]
故 \(W_s-1\) 在有界 \(s\) 区间内具有共同紧时间支集和共同有限群支。
导数也保持这些支集；(5)则进一步控制了它们的大小及阶数截断误差。
此结论来自两端紧支，而不是一般“有限带算子的指数仍有限带”这一错误规则。

对实际(1)，两端分别含 \(c\) 或 \(c'\)，可直接取 \(J\) 为
\(\operatorname{supp}c\) 的凸包。
这项加强随后用于近锐估计，避免用随 \(\varepsilon\) 发散的导数范数控制标量极限。

## 4. 原次序的时间核及迹类界

对径向坐标 \(x=(j,k)\)，原次序给
\[
 (P_gU_sW_s\psi)_x(t)
   =\sum_n w_n(s,t-\ell_g-s)
     \psi_{x-g-(n,0)}(t-\ell_g-nL-s).
\]
设 \(k=g+(n,0)\)、\(\sigma=t-t'-\ell_k\)，积分后的第 \(n\) 项核为
\[
 h(\sigma)\,w_n(\sigma,t'+nL).                                   \tag{7}
\]
\(t'+nL\) 是实际参数，不能省去 \(nL\)。

记 \(V(k)=V_{p,-k_1}\otimes V_{q,-k_2}\)。
第 \((\alpha,\beta,g,n)\) 个压缩块准确为
\[
 E_\alpha V(k)E_\beta\ \otimes Q^{\alpha\beta}_{g,n},
\quad
 q^{\alpha\beta}_{g,n}(t,t')
 =d_\alpha(t)d_\beta(t')h(\sigma)w_n(\sigma,t'+nL).                \tag{8}
\]
系数不依赖径向坐标，因此这个张量分解合法。

给出足够显式的时间常数。取长度为 \(T_I\) 的紧区间 \(I\)，
两截止支集严格位于其内部，令
\(D_d=\max_{\alpha=p,q;\,0\le j\le2}\|d_\alpha^{(j)}\|_\infty\)。
核在 \(I^2\) 边界附近为0，可以周期延拓。
对中间函数，\(\partial_t=\partial_\sigma\)、
\(\partial_{t'}=-\partial_\sigma+\partial_y\)，其中 \(y=t'+nL\)。
各变量至多两次微分只用到(5)中的总四阶导数。
Leibniz和这两个线性算子的展开给保守界
\[
 \max_{i,j\le2}\|\partial_t^i\partial_{t'}^j q^{\alpha\beta}_{g,n}\|_\infty
 \le1024 D_d^2\|h\|_{C^4}e_n.                                   \tag{9}
\]
\(e_n\) 对全部 \(y\) 取上确界；\(\sigma\) 被 \(h\) 限制于 \([-S,S]\)。

采用区间 \(I\) 的归一化 Fourier 基，在两个变量各分部积分两次。
矩阵元的绝对值至多
\[
 \frac{T_I\|(1-\partial_t^2)(1-\partial_{t'}^2)q\|_\infty}
 {(1+(2\pi m/T_I)^2)(1+(2\pi l/T_I)^2)}.
\]
由积分比较，
\(\sum_{m\in\mathbb Z}(1+(2\pi m/T_I)^2)^{-1}\le1+T_I/2\)。
秩一展开及(9)遂给
\[
 \|Q^{\alpha\beta}_{g,n}\|_1
 \le C_{\rm time}\|h\|_{C^4}e_n,\qquad
 C_{\rm time}=4096\,T_I(1+T_I/2)^2D_d^2.                         \tag{10}
\]
这证明真正迹类性，不是由酉性或有界性推断。

径向方面，取
\(R=R_{N_p+1,p}\otimes R_{N_q+1,q}\)，有 \(E_\alpha\le R\)。
414的环带与最内球基中，每个一位矩阵元满足
\[
 |\langle\zeta_i,V_{r,a}\zeta_j\rangle|
 \le \rho_r^{-2K}\rho_r^{|a|}\quad(\zeta_i,\zeta_j\in R_{K,r},\ K\ge1).
\]
环带—环带项只在 \(|a|\le2K-1\) 出现；球尾项直接用其几何尾公式，球—球项为
\(\rho_r^{|a|}\)。对 \(2K+1\) 个基底逐矩阵元秩一求和，可取
\[
 A_N=(2N_p+3)^2(2N_q+3)^2
       \rho_p^{-2(N_p+1)}\rho_q^{-2(N_q+1)}
\]
使
\[
 \|E_\alpha V(k)E_\beta\|_1\le A_N r(k),\qquad
 r(k)=\rho_p^{|k_1|}\rho_q^{|k_2|}.                              \tag{11}
\]
常数随 \(N\) 增长，未宣称一致截断估计。

## 5. 全Γ收敛及可计算 Dyson 尾界

四个块由(10)–(11)控制，且
\(r(g+(n,0))\le r(g)\rho_p^{-|n|}\)。
令 \(C_*=4A_NC_{\rm time}\)、
\({\cal R}_\rho=(1+\rho_p)(1+\rho_q)/((1-\rho_p)(1-\rho_q))\)，得到
\[
 \|C_NP_gU^c(h)C_N\|_1
 \le C_*\|h\|_{C^4}{\cal B}_4(S)r(g),\qquad
 \sum_g\|C_NP_gU^c(h)C_N\|_1
 \le C_*\|h\|_{C^4}{\cal B}_4(S){\cal R}_\rho.                    \tag{12}
\]
实际上这些估计控制了 \(g,n,\alpha,\beta\) 的联合绝对求和。
因此重排群指标、逐项求迹和在迹范数中求 Dyson 和均合法。

若 \(A_N^{(r)}(h)\) 表示用 \(W_s^{(r)}\) 代入(2)，
\[
 A_N^c(h)=A_N(h)+\sum_{r\ge1}A_N^{(r)}(h)
\]
在迹范数中收敛；截断到阶数 \(R_0\) 后的误差至多
\[
 16C_*\|h\|_{C^4}{\cal R}_\rho
       \sum_{r>R_0}(r+1)^4\frac{X^r}{r!}.                        \tag{13}
\]
给定本稿实际 \(c,d_q,N,S\) 后，所有常数都已指定。
这不保证当连接尖锐化时数值计算高效；(1)的高阶导数确实可发散。

## 6. 全部周期系数与精确比较

定义实际系数和
\[
 F_c(s,t)=\sum_n w_n(s,t+nL),\qquad
 J_\alpha(s)=\int_{\mathbb R}d_\alpha(t)^2F_c(s,t)\,dt.            \tag{14}
\]
由(5)及更高阶版本，和与任意固定阶导数在紧 \(s\) 区间一致绝对收敛。
这是明确的系数求和，不是交叉积上的增广同态。
\(W_0=1\) 给 \(F_c(0,t)=1,J_p(0)=L,J_q(0)=M\)。

(8)的交叉块横向迹为0。对角块时间对角积分为
\[
 h(-\ell_k)\int d_\alpha(t)^2w_n(-\ell_k,t+nL)\,dt .
\]
在(12)之后合法重排 \(k=g+(n,0)\)，得到
\[
 \operatorname{Tr}A_N^c(h)
 =\sum_{k\in\Gamma}h(-\ell_k)
      \sum_{\alpha=p,q}\operatorname{Tr}(E_\alpha V(k)E_\alpha)J_\alpha(-\ell_k).
\]
混合项的消失发生在重排后的总次数 \(k\) 上；不能在最初丢掉原次数 \(g\) 的混合项。
414的精确壳层迹式于是给
\[
\begin{aligned}
 \tfrac12\operatorname{Tr}A_N^c(h)
 ={}&D_Nh(0)
   +\sum_{a\ne0}\rho_p^{|a|}J_p(-aL)h(-aL)\\
   &+\sum_{b\ne0}\rho_q^{|b|}J_q(-bM)h(-bM),\\
 D_N={}&(2N_p+1)L+(2N_q+1)M .                                   \tag{15}
\end{aligned}
\]
原单位扣项准确不变，所有 \(N_p,N_q\ge0\) 都成立。

与原 \(A_N(h)\) 比较，
\[
\begin{aligned}
 \Delta_c(h):=\tfrac12\operatorname{Tr}(A_N^c(h)-A_N(h))
 ={}&\sum_{a\ne0}\rho_p^{|a|}[J_p(-aL)-L]h(-aL)\\
    &+\sum_{b\ne0}\rho_q^{|b|}[J_q(-bM)-M]h(-bM).                \tag{16}
\end{aligned}
\]
因此标量差与 \(N\) 无关、没有单位时间原子。
对每个紧支 \(h\)，这两个轴向和实际上只有有限项；
这是先完成全 \(\Gamma\) 求和后的结果，不是事先删除稠密混合长度。
没有断言算子差本身与 \(N\) 无关。

## 7. 有限积分及 Duhamel 的准确顺序

从(3)得到
\[
\begin{aligned}
 J_\alpha(s)&=l_\alpha+\sum_{r\ge1}J_\alpha^{(r)}(s),\\
 J_\alpha^{(r)}(s)
 &=s^r\int d_\alpha(t)^2
   \int_{\Delta_r}\sum_{n_1,\ldots,n_r\in F}
       \prod_{j=1}^r
       \kappa_{n_j}\left(t+s\theta_j+L\sum_{i=j}^r n_i\right)d\theta\,dt .
                                                                    \tag{17}
\end{aligned}
\]
每阶是有限群和与有限积分。
第一阶为
\[
 J_\alpha^{(1)}(s)
   =\int d_\alpha(t)^2\int_0^s\sum_n\kappa_n(t+nL+r)\,dr\,dt .
\]
若 \(B_0=\sum_n\|\kappa_n\|_\infty\)，则
\[
 \left|J_\alpha(s)-l_\alpha-\sum_{r=1}^{R_0}J_\alpha^{(r)}(s)\right|
 \le l_\alpha\sum_{r>R_0}\frac{(|s|B_0)^r}{r!}.                   \tag{18}
\]
不按目标周期差定义补偿；(16)每个系数可由原始函数计算并控制截断误差。

由原积分方程直接得到
\[
 U_s^c-U_s=\int_0^s U_{s-r}K\,U_r^c\,dr.                         \tag{19}
\]
将右侧先以 \(h(s)\) 平滑为强算子积分 \({\cal D}(h)\)，则
\[
 A_N^c(h)-A_N(h)=\sum_g C_NP_g{\cal D}(h)C_N
\]
由已证估计在迹范数中绝对收敛。
不能未经证明把普通迹移入两个时间积分：
固定 \(s,r\) 的 \(C_NP_gU_{s-r}KU_r^cC_N\) 未被断言迹类。
需要逐阶求迹时应使用(13)、(17)的合法级数。

## 8. 近锐族的p系数趋于原值

现在限定为417第3节的实际 \(c_\varepsilon\)，\(0<\varepsilon<L/4\)，
并允许任意合法辅助 \(d_q\)。对固定 \(S>0\)，置
\(m_S=4+2\lceil S/L\rceil\)。本节证明一个不依赖高阶导数的界：
\[
 \sup_{|s|\le S}|J_p(s)-L|
 \le2\varepsilon\bigl(\sqrt{2m_S}+\sqrt2-1\bigr)
 \longrightarrow0.                                             \tag{20}
\]

按 \(t\in[0,L)\) 将 \(B\) 表示在 \(\ell^2(\mathbb Z)\)，记
\(c_t(j)=c(t+jL)\)。平方分割给 \(\|c_t\|_2=1\)。
(1)的纤维矩阵及其演化为
\[
 K(t)=c'_tc_t^T-c_t(c'_t)^T,\qquad
 W'_s(t)=K(t+s)W_s(t).
\]
矩阵均实，\(W_s(t)\) 正交。
\(\langle c_t,c'_t\rangle=0\)，所以
\(\frac d{ds}c_{t+s}=K(t+s)c_{t+s}\)。
初值唯一性给
\[
 W_s(t)c_t=c_{t+s}.                                              \tag{21}
\]

把(14)中 \(t\) 按模 \(L\) 分拆、重排行列指标，有
\[
 J_p(s)=\int_0^L {\bf1}^T W_s(t)(c_t^{\odot2})\,dt.               \tag{22}
\]
这里 \({\bf1}\notin\ell^2\)，(22)仅表示有限输出支集上的坐标和，
不是把 \({\bf1}\) 当作Hilbert向量。
具体地，矩阵第 \(j,k\) 项是
\(w_{j-k}(s,t+jL)\)；固定输入 \(k\) 求输出 \(j\) 和，
正是(14)在 \(t+kL\) 处的 \(F_c\)。

由(6)，\(W_s-1\) 的输出时间位于
\([-\varepsilon-S,L+\varepsilon+S]\)。
\(c_t^{\odot2}-c_t\) 的输入时间本已在 \([-\varepsilon,L+\varepsilon]\)，
所以其输出至多有 \(m_S\) 个坐标。
区间长度为 \(L+2\varepsilon+2S<3L/2+2S\)，按步长 \(L\) 计数即得此安全上界。
实正交性和 Cauchy–Schwarz 给
\[
 |{\bf1}^TW_s(t)(c_t^{\odot2}-c_t)|
       \le\sqrt{m_S}\|c_t^{\odot2}-c_t\|_2.
\]
模 \(L\) 的过渡区长度为 \(2\varepsilon\)。
在它之外 \(c_t\) 只有一个坐标为1，差为0；
在过渡区至多两个坐标非零，故差的范数至多 \(\sqrt2\)。
积分后的贡献因此至多 \(2\varepsilon\sqrt{2m_S}\)。

另一方面，由(21)，
\[
 \int_0^L{\bf1}^TW_s(t)c_t\,dt
   =\int_0^L\sum_jc(t+s+jL)\,dt=\int_{\mathbb R}c(x)\,dx.
\]
在过渡区，周期化和为 \(\sin\theta+\cos\theta\in[1,\sqrt2]\)，
其余为1，所以
\[
 0\le\int c-L\le2\varepsilon(\sqrt2-1).
\]
将两部分相加就是(20)。
整个估计与 \(d_q\) 无关；未声称 \(J_q(s)\) 有同样极限。

## 9. 对直接主补偿候选的明确限制

原两边有符号周期目标为
\[
 {\cal B}_{p,q}(h)
   =-L\sum_{a\ne0}\rho_p^{|a|}h(-aL)
      +M\sum_{b\ne0}\rho_q^{|b|}h(-bM).                          \tag{23}
\]
因 \(L/M\) 无理，\(-L\notin M\mathbb Z\)。
选 \(h\in C_c^\infty\)，\(h(-L)=1\)，支集充分靠近 \(-L\)，
避开0、其他 \(p\) 周期及全部 \(q\) 周期。
由(16)、(20)，
\[
 \Delta_{c_\varepsilon}(h)
      =\rho_p[J_p(-L)-L]\longrightarrow0,\qquad
 {\cal B}_{p,q}(h)=-L\rho_p\ne0.                                 \tag{24}
\]
因此 \(\Delta_c\) 不能对全部合法分割规范地等于
\({\cal B}_{p,q}\) 或其相反数。
任何一致有界标量倍数也无法跨此族恢复(23)的这个 \(p\) 系数。
这里并未证明某个单独分割绝无偶然系数匹配，也未把 \(q\) 项极限当作已知。

本连接确实实现417的平行性，并给出(15)这个收敛且可计算的新周期迹；
但“把原时间换成该连接时间，再直接取两迹之差”仍不足以承担固定边界主补偿。
新的相对特征、额外算术可观测量或不同连接若要继续，须交付与(23)的真实比较，
不能用外等价、平行性或有限计算的存在替代。
第417–418轮的结构与这些范围内限制均不达到GOAL第十节的较远期完成标准。

## 10. 推导、复核及形式化边界

[原Γ收敛和全部系数的独立推导全文](../reviews/2026-09-21/f1-connection-periodized-trace-derivation.md)
与[原始回包](../reviews/2026-09-21/f1-connection-periodized-trace-derivation.raw.json)
保存第2–7节的前置推导。第8–9节的近锐检验及本稿新增显式常数另作独立核对。
全文最终状态以完成的审查记录为准。

本稿使用417的实际连接及414的已审径向矩阵元。
[连接演化代数Lean](../formal/F1/Analysis/ConnectionEvolutionAlgebra.lean)
仅核验两种cocycle群律、压缩残差和相位导数；四项无sorryAx依赖。
Dyson导数估计、全Γ迹范数收敛、无限维纤维及(20)未在Lean中形式化，
不能由该四项代数检查替代本文证明。

## 11. 完成复核与保存边界

[近锐p系数独立核验](../reviews/2026-09-21/f1-connection-sharp-coefficient-review.md)
核准纤维指标、正负时间、有限输出和模L过渡测度，并给出更强常数；
正文保留已经足够的较宽(20)。
[全文逆审](../reviews/2026-09-21/f1-connection-periodized-trace-full-review.md)
独立覆盖全部十节和(1)–(24)，包括新增显式常数及近锐结论，
核对正文SHA256
`bbe2302ecf2db4245fd3c4a7c8b8958f2f2d40f3e17c067a5c1bf1778eca43ff`。
必要改正为无；此后第1–10节未改，仅更新状态并添加本节。
两份前置推导及本次全文原始回包均保留，未以摘要代替审查。

此轮结算真实连接周期迹及其直接主补偿限制，停止以同一个迹差的更名或有界倍数完成目标。
下一有限任务是[保留原物理时间的交叉积及原观测量比较](../reviews/2026-09-21/f1-original-time-crossed-product-next-proof-plan.md)；
具体同构也须携带原算术读出，不默认它产生所需相对特征。
本轮不改变长期GOAL及第十节，不认证新的零点比例、非零区域或RH结论。
