# 函数域的正闭形式与完整 Weil 热迹：源递推到圆周 holonomy

2026-10-20，566 独占辅助原稿。状态：[proved] 在明确有限递推／正能量输入下的全时间普通热迹身份；
[obstruction] 非酉端点形式仍正，但不保算术热迹；[open] 经典 ζ 的同源正闭形式。
不修改 STATE、cadence 或 Git。以下新信息是显式闭形式及其全周期热核实现；
正极化证书本身已经由 563 支付，不把标准圆周热核技术称为新纯性机制。

## 1. 输入来自全点数递推，不来自 ζ 零点

继承 [563 算术原稿](../grh-distribution/arithmetic-counts-and-conservative-realizations.md) 的准确范围。
对光滑射影几何连通曲线 C/F_q，先有 Riemann–Roch 有理性及函数方程

\[
 Z_C(T)=\exp\!\left(\sum_{n\ge1}N_nT^n/n\right)
       ={P(T)\over(1-T)(1-qT)},\qquad \deg P=m=2g.
 \tag{1}
\]

包含 infinity 的所有 closed places 给 N_n=Σ_{d|n}d B_d，所以全部 proper powers 已计。
令 L=log q，a_0=m，a_n=q^{-n/2}(q^n+1-N_n)，a_{-n}=a_n。所选完成化
E(s)=q^{g(s-1/2)}P(q^{-s}) 给完整源分布

\[
 W_C=L\sum_{n\in\mathbb Z}a_n\delta_{nL}
 =mL\delta_0+L\sum_{n\ne0}
 \bigl[2\cosh(nL/2)-q^{-|n|/2}N_{|n|}\bigr]\delta_{nL}.
 \tag{2}
\]

其同源身份可先在 Re w>1/2 的绝对收敛半平面核验：

\[
 {E'\over E}(1/2+w)=gL+L\sum_{n\ge1}a_ne^{-nLw}.
 \tag{3}
\]

因此 (2) 的 origin contact 是 mL，不能删成没有原点的 prime 级数。
q^n+1 是分母在整个 s-plane 的周期极点背景；不能只保某个基本 strip 内的两极点。
本稿从 (1)–(3) 出发，不读取 E 的零点。

额外有限输入是从同一精确递推核出的 U∈GL_m(C)、H=H*>0，满足

\[
 U^*HU=H,\qquad \operatorname{Tr}(U^n)=a_n\quad(n\in\mathbb Z).
 \tag{4}
\]

全 n 的 trace 身份必须由 P 的系数、Cayley–Hamilton／Newton 恒等式与同一全次数递推支付；
有限点数拟合不足。曲线 real-type／reciprocal 情形保证 a_{-n}=a_n∈R。
一般复系数酉 holonomy 只有 a_{-n}=overline(a_n)，热量只读取偶部；
不能把 563 的实偶热判据直接套到单个非实角色。完整酉实现本身仍给全复检验正型。

## 2. 从输入矩阵定义正稠密闭形式

固定 Hilbert 空间

\[
 \mathscr H=L^2((0,L),\mathbb C^m;H\,dx),\quad
 \langle f,g\rangle=\int_0^L f(x)^*H g(x)\,dx,
\]

及形式域、形式

\[
 \mathscr V_U=\{f\in H^1((0,L),\mathbb C^m):f(L)=Uf(0)\},
 \qquad \mathfrak q_U(f,g)=\int_0^L f'(x)^*H g'(x)\,dx.
 \tag{5}
\]

这里 x 是 log-norm circle 的空间坐标，t>0 是热时间；H 是正定 fibre metric。
它不是物理整数轴上的 Gaussian 能量，也不是把未知 Weil 形式先宣称为正。

端点评价在 H¹ 中连续，所以 V_U 是 H¹ 的闭子空间。H>0 使
||f||_H²+q_U(f,f) 与通常 H¹ 范数等价，因此 q_U 正且闭。
C_c^∞(0,L;C^m)⊂V_U 保证稠密性。一次分部积分精确给形式表示算子

\[
 K_U f=-f'',\quad
 D(K_U)=\{f\in H^2:f(L)=Uf(0),\ f'(L)=Uf'(0)\}.
 \tag{6}
\]

导数边界的推导先给 U*H f'(L)=H f'(0)，再用 U*HU=H 才变成 (6)。
表示定理因此给 K_U≥0 自伴。也可先由同一酉边界定义 D_U=-i∂_x 自伴，再有 K_U=D_U²。
后一结论不允许在非酉情况下照抄。

H¹(0,L) 紧嵌入 L²，故 K_U 有紧 resolvent。普通热迹的有限性也直接付清：
V_U⊂H¹，而 q_U 是同一 Neumann 能量的限制；min–max 得

\[
 \operatorname{Tr}(e^{-tK_U})\le
 m\left(1+\sum_{k\ge1}e^{-t\pi^2k^2/L^2}\right)<\infty
 \quad(t>0).
 \tag{7}
\]

这里保留完整 fibre 维数 m，既不取标量 cyclic GNS 商，也不合并重复 eigenphases。

## 3. 不读取零点的 image heat kernel 与同源身份

把 f∈V_U 延拓为 f(x+nL)=U^n f(x)。由 (4)，U^n 在 H 范数中等距，故延拓无增长。
取实线热核 k_t(v)=(4πt)^(-1/2)exp(-v²/(4t))，定义

\[
 \mathcal K_U(t;x,y)=\sum_{n\in\mathbb Z}U^n k_t(x-y-nL),
 \qquad 0\le x,y\le L.
 \tag{8}
\]

任意 t∈[ε,T]、x,y∈[0,L] 及有限阶 t,x,y 导数，Gaussian 尾使级数一致绝对收敛。
它满足

\[
 \mathcal K_U(t;x+L,y)=U\mathcal K_U(t;x,y),\qquad
 \mathcal K_U(t;x,y+L)=\mathcal K_U(t;x,y)U^{-1},
\]

以及相同的导数边界。将实线卷积按 y+nL 分段，直接得到 (8) 的半群律；
实线 approximate identity 给 t↓0 的 L² 强收敛。由 U^{*_H}=U^{-1} 和 k_t 偶性，
K_U(t;x,y)^{*_H}=K_U(t;y,x)，并且热方程为 ∂_t K=∂_x²K。
故 (8) 正是 (6) 的热半群，不是另造一个具有相似迹的核。

正 trace-class 半群的连续 diagonal trace，或将 t 拆成 t/2 后计算 Hilbert–Schmidt 范数，给

\[
 \begin{aligned}
 \operatorname{Tr}_{\mathscr H}(e^{-tK_U})
 &=\int_0^L\operatorname{tr}_{\mathbb C^m}\mathcal K_U(t;x,x)\,dx\\
 &=\frac{L}{\sqrt{4\pi t}}\sum_{n\in\mathbb Z}
       \operatorname{Tr}(U^n)e^{-n^2L^2/(4t)}\\
 &=\langle W_C,k_t\rangle=:\Theta_{W_C}(t),\qquad t>0.
 \end{aligned}
 \tag{9}
\]

最后一等号只用已由算术源全递推付清的 (2)/(4)。所有 n 的绝对收敛使换序无误差。
没有 ζ 零点输入，没有先假设 heat-CM，也没有只保单个 period。
由 (9) 和 K_U≥0，所有 (-1)^j Θ^(j)(t)=Tr(K_U^j e^{-tK_U})≥0。
逐阶微分由 λ^j e^{-tλ}≤C_{j,t}e^{-tλ/2} 及 (7) 支付。
曲线 real-even 源在 563 已付域内，因此可再经 heat-CM 判据恢复完整 Weil 正性。
不过同一 (4) 早已在 563 直接给全 compact 平方和，故这里不登记第二份新纯性结果。

标准的圆周 bundle 热核／trace 技术可参照 H. D. Fegan,
[Homogeneous bundles and the trace of the heat kernel, §3/§5](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/DEEBCBCE0661A40F76797C115BB95403/S1446788700026501a.pdf/homogeneous_bundles_and_the_trace_of_the_heat_kernel.pdf)。
本稿所需的特定 flat holonomy 公式已在 (5)–(9) 独立证明，不将外部来源当作算术身份的替代。

## 4. F₅ 真曲线：保重数的具体正实现

E/F₅: y²=x³+x+1 的 N₁=9，genus-one 有理性／FE 给 P(T)=1+3T+5T²。
563 已独立枚举 N₂=27、N₃=108，并由全递推而非有限枚举支付所有次数。
所用有理证书为

\[
 A=\begin{pmatrix}0&-5\\1&-3\end{pmatrix},\quad
 H=\begin{pmatrix}1&-3/2\\-3/2&5\end{pmatrix},\quad
 \det H=11/4>0,\quad A^THA=5H.
 \tag{10}
\]

令 U=A/√5、L=log5；Tr A⁰=2、Tr A=-3，Cayley–Hamilton 给
S_n=-3S_{n-1}-5S_{n-2}，a_n=5^{-n/2}S_n。
det U=1 及二次特征恒等式同时给 Tr U^{-n}=Tr U^n，故 (4) 的 signed n 身份全付。
于是 (5)/(10) 是直接可写出的 rank-two Hilbert bundle 正闭形式，(9) 是它的完整普通热迹。
特别 n=0 项为 2L/√(4πt)，原点质量及 rank-two multiplicity 均保留。
这不是先求 P 的两根再造 Hilbert 空间；矩阵能量恒等式在零点计算之前直接核验。

若某个半正证书只允许 quotient 后 rank 降低，则不能继续使用原 m 的普通 trace。
本例 H 严格正定，故无需这一修复；一般重根／Jordan 问题仍按 565 分账。

## 5. 关键负对照：任意 holonomy 的正能量不保源热量

对任意可逆 M 和任意正定 H₀，同样定义

\[
 V_M=\{f\in H^1:f(L)=Mf(0)\},\qquad
 q_M(f)=\int_0^L f'^*H_0f'\,dx.
 \tag{11}
\]

它照样稠密、正、闭、有紧 resolvent，且普通热迹受 (7) 控制。
但形式表示算子的实际边界是

\[
 f(L)=Mf(0),\qquad M^*H_0 f'(L)=H_0 f'(0),
 \tag{12}
\]

而不是 f'(L)=Mf'(0)。只有 M*H₀M=H₀ 时这两种导数边界相同。
形式 (11) 本身的正性完全不需要算术纯性；把 (12) 擅改为同 holonomy 的导数边界，
正是将未付极化偷运进热迹身份的位置。

具体取 [290](../../../notes/290-positive-euler-duality-model-and-mass-moment-nonidentification.md) 的 q=5 正闭点 Euler 反模型：

\[
 P_-(T)=1-5T+5T^2,\qquad
 A_- =\begin{pmatrix}0&-5\\1&5\end{pmatrix},\qquad
 M=A_-/\sqrt5.
 \tag{13}
\]

它已有正整数 closed-point Euler、精确曲线型对偶和全递推。
det M=1，Tr M=√5>2，故特征值为 r,r^{-1}，r=(√5+1)/2>1。
这是已指定二次矩阵的初等计算，不使用未知 ζ 零点。
source a_n=Tr M^n=r^n+r^{-n} 给完整源热量

\[
 \Theta_-(t)=\frac{L}{\sqrt{4\pi t}}
       \sum_{n\in\mathbb Z}(r^n+r^{-n})e^{-n^2L^2/(4t)}.
 \tag{14}
\]

每个 t>0 级数绝对收敛且正，但它在 t→∞ 无界增长。
严格下界：写 h=log r>0，取整数 n_t 距离 2ht/L² 至多 1/2，则

\[
 \Theta_-(t)\ge\frac{L}{\sqrt{4\pi t}}
   \exp\left(\frac{h^2}{L^2}t-\frac{L^2}{16t}\right)
   \longrightarrow\infty.
 \tag{15}
\]

所以 (14) 不可能是任何 K≥0、全 t>0 ordinary trace-class 半群的热迹；
这样的 trace 对 t 必须非增，且 t≥t₀ 时有界于 Tr e^{-t₀K}。
特别 (11) 的正闭形式不能给 (14)。更具体地，M 无特征值 1，
故 K_M 的零能量常数核为 0；紧 resolvent 给正 spectral gap，Tr e^{-tK_M}→0，
与 (15) 的行为相反。

若仍写 Σ M^n k_t(x-y-nL)，Gaussian 可压住指数增长，因此这个 image sum 也收敛。
它确实满足 f(L)=Mf(0)、f'(L)=Mf'(0)，但这恰好是与 (12) 不同的非自伴边界问题。
在正 Hilbert 空间中它不表示 (11) 的正算子；“image sum 收敛”不能补相容正极化。
反模型把 q>0 与 source identity 两项责任严格分开，而不只报告 H_- 不正。

## 6. 净消费、量词与经典 ζ 的剩余责任

- 对象：固定 finite-rank log-circle bundle，原 H fibre norm、通常 L²(dx)、H¹ twisted 形式域；
  所有 t>0、全部 integer n、完整 rank m；不是 scalar quotient、finite time samples 或 relative trace。
- 输入：(1) 的全算术有理性／FE、(2) 的 contact/pole/proper-power 规范、(4) 的独立正 H 和全递推。
  无截断／逼近误差；有限点数检查不能替代全递推。
- 新增可消费信息：将已有矩阵能量证书显式提升为正闭形式，并从 image kernel 直接证明同源普通热迹；
  290 同端点正形式的精确失败发生在导数边界／metric holonomy 相容性，而不是形式闭性。
- 强旧扣除：563 已给同一 U,H 的全周期 Weil 平方和；565 已给一般正形式＋同源 heat 的充分接口。
  本稿补具体构造与负对照，不给新的函数域 RH／一般极化来源。
- 经典限制：log p 没有单一 L-lattice，完整 Γ 有原点 finite-part，prime-power 系数为负而非各自的正边能量；
  经典源不直接具有 (2)/(4) 的 finite-circle trace 结构。
  无法把每个 prime 任意做成正闭边后将热迹相加，便声称得到完整 Weil 热量。
  需要真正共同 Hilbert 空间／domain／闭形式，以及从全部 Γ、prime powers、极点推导的精确 trace 身份。
  仅假设该身份、或从欲证零点反建 K，都仍是 RH 强度的责任。

本稿不排一般图／无限维／relative signed heat／有控分布极限等合法修复。
actual ζ 最强旧 542+555→557 whole leading 4/5、560 成长 K/core/coupling、faithful Ξ 均未改变。
