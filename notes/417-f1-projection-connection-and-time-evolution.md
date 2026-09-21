# 417. 原始 Green 投影的连接、真实时间演化与素数协变代价

2026-09-21。[T/O] 全文独立复核及范围修正采纳已闭环；演化由范数收敛级数给出。
[416](416-f1-split-transfer-and-periodic-coefficients.md)排除的仅是指定有限传递项的有界线性组合。
这里允许新的导数项，其近锐极限确实无一致范数界；这本身不提供算术比较。

## 1. 固定对象与结论范围

沿用[414](414-f1-deep-boundary-unitary-and-time-defect.md)的
\(L=\log p,M=\log q,\Gamma=\mathbb Z^2\)，不同素数 \(p,q\)，以及
\(Y=(\mathbb Z\cup\{\infty\})^2\times\mathbb R_t\)。
群元 \(g=(a,b)\) 的长度为 \(\ell_g=aL+bM\)，乘法约定
\[
(fU_g)(bU_r)=f(t)b(t-\ell_g)U_{g+r}.                     \tag{1}
\]
记 \(A=C_0(Y)\rtimes\Gamma\)，\(I=C_0(Y\setminus D)\rtimes\Gamma\)，
\(D=\{(\infty,\infty)\}\times\mathbb R\)，\(J=C_0(\mathbb Z^2\times\mathbb R)\rtimes\Gamma\)。
\(A_D=C_0(\mathbb R)\rtimes\Gamma\) 通过径向常值系数嵌入 \(M(A)\)。
这是乘子嵌入，不是把所有这些元素认作 \(A\) 的元素。

固定实非负 \(c\in C_c^\infty(\mathbb R)\)，
\[
\sum_n c(t-nL)^2=1.
\]
设 \(c_n(t)=c(t-nL)\)、\(d_n(t)=c'(t-nL)\)，并固定实际原对象
\[
 e=\sum_n c_0c_nU_p^n,\quad
 v=\sum_n c_0c(t-nL-M)U_p^nU_q,\quad u=1-e+v .
                                                               \tag{2}
\]
所有群和有限；414已证明 \(e=e^*=e^2\)、\(v^*v=vv^*=e\)、\(u\) 酉。
\(Q=H(j)H(k)\)，其中 \(H(j)=1\) 当 \(j\ge0\) 或 \(j=\infty\)，否则为0。
\(T=1+Q(u-1)Q\in A^\sim\) 是414的原压缩提升。

\(\delta=\partial_t\) 逐系数作用，原时间为
\(\beta_s(fU_g)=f(t-s)U_g\)，故其生成导数是 \(-\delta\)。
在414的忠实协变表示
\(\mathcal H=\mathcal H_{\rm rad,p}\otimes\mathcal H_{\rm rad,q}\otimes L^2(\mathbb R)\)
中，\(P_g=\pi(U_g)\) 同时移动径向坐标和时间，原额外时间 \(U_s\psi(t)=\psi(t-s)\)
与每个 \(P_g\) 交换。下文省略有界算子的 \(\pi\)。

本稿证明：实际有限系数 \(K=[\delta e,e]\) 定义反自伴连接
\(D_c=\partial_t-K\)，并产生强连续酉群 \(U_s^c\)。
它使 \(e,v,u\) 平行，使 \(T\) 仅模 \(I\) 平行；
它一般不保留原 \(P_p,P_q\) 的时间固定性。
在原旋转满角上，它给出明确的圆周旋转流。
这些结论未建立固定通常ζ的算术读出，也未建立主消失、完整B、双次数或RR。

## 2. 从原系数计算连接与角内导数

由平方分割求导，
\[
 \sum_n c_n^2=1,\qquad \sum_n c_nd_n=0.                 \tag{3}
\]
和局部有限，故求导合法。在(1)中直接卷积：
\[
 (\delta e\,e)_n=d_0c_n,\qquad (e\,\delta e)_n=c_0d_n.
\]
于是
\[
 K=[\delta e,e]=\sum_n\kappa_n(t)U_p^n,\qquad
 \kappa_n=d_0c_n-c_0d_n.                               \tag{4}
\]
若 \(|n|L>\operatorname{diam}(\operatorname{supp}c)\)，系数为0。
系数与所有时间导数光滑紧支，且
\(\|K\|\le\sum_n\|\kappa_n\|_\infty<\infty\)。
投影及其导数自伴，所以 \(K^*=-K\)。

实际 \(K\in B=C_0(\mathbb R)\rtimes p^\mathbb Z\subset A_D\)；
它进入原空间后属于 \(M(A)\)，却不属于 \(A\)。
确实，\(\sum_n\kappa_n(t)c_n(t)=c'(t)\)，而非零紧支平方分割不能恒常，
故 \(K\ne0\)。至少一个非零 Fourier 系数在 \(j,k\) 方向常值，
沿 \(j\to-\infty\) 不衰减，因而不在 \(C_0(Y)\)。
离散约化交叉积的系数唯一性排除 \(K\in A\)。

令 \(c_{n,M}=c(t-nL-M)\)、\(d_{n,M}=c'(t-nL-M)\)。再次使用(3)，
\[
\begin{aligned}
 (\delta v)_{(n,1)}&=d_0c_{n,M}+c_0d_{n,M},\\
 (e\,\delta v)_{(n,1)}&=c_0d_{n,M},&
 ((\delta v)e)_{(n,1)}&=d_0c_{n,M},\\
 e\,\delta v\,e&=0,&
 (Kv)_{(n,1)}&=d_0c_{n,M},&
 (vK)_{(n,1)}&=-c_0d_{n,M}.
\end{aligned}                                                       \tag{5}
\]
例如 \(e\delta v\) 中含 \(c_md_m\) 的和为0，另一项含 \(\sum c_m^2=1\)；
再右乘 \(e\) 用在 \(t-M\) 处的(3)即得角内导数为0。
从而
\[
 \delta e=[K,e],\qquad \delta v=[K,v],\qquad \delta u=[K,u].          \tag{6}
\]
第一式亦由 \(e^2=e\)、\(\delta e\,e+e\,\delta e=\delta e\) 直接推出。

这里角内导数的消失是(2)的特定事实，不能只由角内酉关系推出。
若 \(f(t)=e^{2\pi it/L}\)，则 \(\widetilde v=fv\) 仍满足
\(\widetilde v^*\widetilde v=\widetilde v\widetilde v^*=e\)，但
\[
 e\,\delta(\widetilde v)e=(2\pi i/L)\widetilde v\ne0.                \tag{7}
\]
\(f\) 与 \(e,K\) 交换，因为它是 \(L\)-周期函数。

## 3. 压缩残差的理想位置及非零见证

只有 \(p\) 群次数的 \(K\) 与 \(Q_q=H(k)\) 交换。令 \(R=[K,Q]\)，则
\[
 R=\sum_n\kappa_n(t)\bigl(H(j-n)-H(j)\bigr)H(k)U_p^n.               \tag{8}
\]
当 \(n>0\)，括号仅在 \(0\le j<n\) 等于 \(-1\)；
当 \(n<0\)，仅在 \(n\le j<0\) 等于 \(1\)；在 \(j=\infty\) 为0。
每项支集包含于 \(Y\setminus D\) 内的紧集
\[
 \{\text{有限多个整数 }j\}\times(\mathbb Z_{\ge0}\cup\{\infty\})
 \times\{\text{紧时间集}\}.
\]
故 \(R\in I\)，所有时间导数仍属于 \(I\)。
相反，裸 \([K,Q_p]\notin A\)：\(\kappa_0=0\)、\(K\ne0\) 给非零的非零次数，
其边界条带沿全部 \(k\) 常值，在 \(k\to-\infty\) 不衰减。

在 \(H^1(\mathbb R;\mathcal H_{\rm rad,p}\otimes\mathcal H_{\rm rad,q})\)
上定义 \(D_c=\partial_t-K\)。有限平移和光滑有界系数保持此定义域，
所有以下交换子均从该域上的等式延拓成有界算子。
(6)给 \([D_c,e]=[D_c,v]=[D_c,u]=0\)。
置 \(a=u-1\)，展开得
\[
 F_c:=[D_c,T]=Q[K,a]Q-[K,QaQ]=-RaQ-QaR\in I.                      \tag{9}
\]
这里乘子乘法保持闭理想；也可用(8)逐项看到有限群支和紧时间支集。

(9)一般不为0。取 \(0<\varepsilon<L/4\)，让光滑单调函数 \(\theta\)
在 \(r\le-\varepsilon\) 为0，在 \(r\ge\varepsilon\) 为 \(\pi/2\)，端点平坦。
定义平方分割 \(c_\varepsilon\)：在 \([-\varepsilon,\varepsilon]\) 为
\(\sin\theta(t)\)，在 \([\varepsilon,L-\varepsilon]\) 为1，在
\([L-\varepsilon,L+\varepsilon]\) 为 \(\cos\theta(t-L)\)，其余为0。
在 \(t=L+r,|r|<\varepsilon\)，仅有 \(c(t)=\cos\theta(r)\)、
\(c(t-L)=\sin\theta(r)\) 两项非零，\(\kappa_1(t)=-\theta'(r)\)。
(9)的 \(q\) 次数0部分为 \(ReQ+QeR\)，其单位群系数为
\[
 (F_c)_{(0,0)}(0,0,L+r)
       =2\theta'(r)\sin\theta(r)\cos\theta(r).                     \tag{10}
\]
这是两个相反的 \(p\) 次数配对，各贡献 \(\theta'\sin\theta\cos\theta\)。
过渡内部有点使其严格为正；含 \(v\) 的项有 \(q\) 次数1，无法抵消。

此外 Fourier 系数映射是压缩表示中的收缩映射，故
\[
 \|K_\varepsilon\|\ge\|\kappa_1\|_\infty
    \ge \frac{\pi}{4\varepsilon}.                                \tag{11}
\]
最后一步用 \(\int_{-\varepsilon}^{\varepsilon}\theta'=\pi/2\)。
因此本连接族的算子范数不一致有界。416只限制指定三个传递读出及其系数一致有界的有限线性组合，
不能直接判定本连接生成的新演化读出；该读出与原周期分布及上述组合类的关系仍须完成第8节比较。

## 4. 范数 Dyson 级数构造真实演化

记 \(G=\partial_t\)、\(\operatorname{Dom}G=H^1\)；原 \(U_s=e^{-sG}\)。
在 \(B\) 中令 \(K_s=\beta_{-s}(K)\)。此路径范数光滑，
\(K_s^*=-K_s\)，\(\|K_s\|=\|K\|\)。
在 \(B^\sim\) 中解
\[
 W'_s=K_sW_s,\qquad W_0=1.                                       \tag{12}
\]
对 \(s\ge0\) 的显式解为
\[
 W_s=1+\sum_{n\ge1}
 \int_{0\le r_n\le\cdots\le r_1\le s}
 K_{r_1}\cdots K_{r_n}\,dr_n\cdots dr_1 .                         \tag{13}
\]
负 \(s\) 取同一有向迭代积分；每项范数至多
\((|s|\|K\|)^n/n!\)。所以级数在紧 \(s\) 区间一致范数收敛，
可由积分方程逐项得到(12)。Picard差的同一阶乘估计给唯一性。
非恒等项属于 \(B\)，故 \(W_s-1\in B\)。

求导 \(W_s^*W_s\) 得0；而 \(W_sW_s^*\) 满足
\(X'=K_sX-XK_s\)、\(X(0)=1\)。同一唯一性给 \(W_sW_s^*=1\)，所以 \(W_s\) 酉。
对固定 \(t\)，以下两条关于 \(s\) 的路径解同一个初值问题：
\[
 W_{s+t},\qquad \beta_{-t}(W_s)W_t.
\]
它们的初值都是 \(W_t\)，导数都是 \(K_{s+t}\) 左乘该路径。于是
\[
 W_{s+t}=\beta_{-t}(W_s)W_t.                                     \tag{14}
\]
令
\[
 U_s^c=U_sW_s,\qquad V_s=\beta_s(W_s),\qquad U_s^c=V_sU_s.         \tag{15}
\]
因为 \(W_sU_t=U_t\beta_{-t}(W_s)\)，(14)给
\(U_s^cU_t^c=U_{s+t}^c\)。两因子分别强连续、范数连续，
故得到真正的强连续酉群，且 \(V_s\in B^\sim\)、
\(V_{s+t}=V_s\beta_s(V_t)\)。

生成元及其完整定义域也由本构造决定。任意 \(\xi\in\mathcal H\) 有
\[
 \frac{U_sW_s\xi-\xi}{s}
 =U_s\frac{W_s-1}{s}\xi+\frac{U_s-1}{s}\xi.
\]
第一项对所有 \(\xi\) 收敛到 \(K\xi\)。
第二项存在极限当且仅当 \(\xi\in H^1\)，这可直接由时间 Fourier 变换
及乘子 \((e^{-is\xi}-1)/s\) 的 \(L^2\) 极限判定。
因此 \(U_s^c\) 的生成元准确为 \(-G+K=-D_c\)，定义域准确为 \(H^1\)。
强连续酉群生成元定理亦给 \(D_c\) 在此域反自伴。
这里不需要绝热谱隙、渐近定理或未经证明的高阶估计。

## 5. 保持代数、理想及源对象

用(15)定义
\[
 \alpha_s^c=\operatorname{Ad}(V_s)\circ\beta_s.                   \tag{16}
\]
原 \(\beta\) 保持 \(A,I,J,A_D,B\)，\(V_s\) 是这些表示中的有界酉乘子，
故(16)在 \(A\) 上为强连续的 C* 动力系统，并保持 \(I,J\)。
乘子保持理想可用近似单位证明：若 \(x\in I,m\in M(A)\)，
则 \(mx=\lim_\lambda (ma_\lambda)x\in I\)，右乘同理。
\(\beta\) 在 \(A\) 上范数连续，\(V_s\) 范数连续，故(16)在每个 \(a\in A\) 上范数连续。
不要求 \(\beta\) 在整个 \(M(A)\) 上范数连续。

对 \(a=e,v,u\)，(6)给
\[
 \frac{d}{ds}\beta_{-s}(a)
      =[K_s,\beta_{-s}(a)].
\]
\(W_saW_s^*\) 解同一有界线性ODE且有相同初值，故二者相等。
代入(15)得到
\[
 \alpha_s^c(e)=e,\qquad\alpha_s^c(v)=v,\qquad\alpha_s^c(u)=u.       \tag{17}
\]
它们是乘子中原实际对象的等式，不是在任意抽象同构后重命名。

对压缩提升，(16)在光滑有限系数处的导数是
\(-\delta+[K,\cdot]=-[D_c,\cdot]\)。于是
\[
 \alpha_s^c(T)-T=-\int_0^s\alpha_r^c(F_c)\,dr\in I.                \tag{18}
\]
积分在 \(I\) 的范数中存在；任意有限 \(s\) 成立，负 \(s\) 为有向积分。
因此 \(T\bmod I\) 固定，但(10)表明不能将(18)加强为 \(T\) 全程固定。

## 6. 原素数平移不再被时间固定

在同一 \(H^1\) 域上，原 \(G\) 与所有 \(P_g\) 交换，因而
\[
 [D_c,P_g]=-[K,P_g].                                            \tag{19}
\]
对 \(r=p,q\)，若 \(K\) 与 \(P_r\) 交换，由原协变性及 Fourier 系数唯一性，
每个 \(\kappa_n(t)\) 都分别为 \(L\)-或 \(M\)-周期函数。
紧支连续周期函数只能是0，这与 \(K\ne0\) 矛盾。
所以对于每一个生成元，实际均有
\[
 [K,P_p]\ne0,\qquad [K,P_q]\ne0.                                 \tag{20}
\]
若 \(U_s^c\) 对所有 \(s\) 与某一 \(P_r\) 交换，在共同不变域求导会推出
\([D_c,P_r]=0\)，故(20)也排除了这一强交换性质。
这只针对本稿的有限紧支 \(K\)，未排除别的连接。

本连接平行的是经过 Green 修正的箭头 \(v=wU_q\)，不是裸 \(U_q\)。
(16)确为原作用的乘子酉 cocycle 扰动；这种外等价不保证
原指定有理对应、原测试函数读出和通常ζ显式公式保持不变。
414联合迹的计算曾使用 \(U_sP_g=P_gU_s\)，因此把其中 \(U(h)\)
直接替换为 \(U^c(h)\) 后不能照抄其公式或主消失结论。

## 7. 满角上的流可显式识别

令 \(z=e^{2\pi it/L}e\)，即414的第一旋转酉元。
对任何 \(L\)-周期光滑 \(f\)，乘子 \(f(t)\) 与整个 \(B\)、\(W_s\)、\(V_s\) 交换。
由(17)与 \(\beta_s(f)=f(t-s)\)，
\[
 \alpha_s^c(fe)=f(t-s)e,\qquad
 \alpha_s^c(z)=e^{-2\pi is/L}z,\qquad
 \alpha_s^c(v)=v.                                               \tag{21}
\]
414已将满角 \(eA_De\) 识别为由 \(z,v\) 生成的无理旋转代数，
\(zv=e^{2\pi iM/L}vz\)。
因此(21)确定其整个流，且在此角上周期为 \(L\)。
整个 \(\mathcal H\) 上的 \(U_s^c\) 无需具有周期 \(L\)，不能把角上共轭周期误作酉群周期。

该流的普通规范GNS时间迹有一个明确限制。由 \(q\) 次数条件期望
和圆周积分得到规范忠实迹 \(\tau\)，归一化 \(\tau(e)=1\)。
在稠密 Laurent 代数上，
\[
 \tau(z^av^b)=\mathbf1_{a=b=0},\quad
 \langle z^av^b,z^{a'}v^{b'}\rangle_\tau
       =\mathbf1_{a=a',\,b=b'}.
\]
正性由条件期望保证；迹性也可直接用旋转交换关系核对。
这些单项式构成 \(L^2(eA_De,\tau)\) 的正交基。
由(21)诱导的酉群 \(\mathscr U_s\) 满足
\[
 \mathscr U_s(z^av^b)=e^{-2\pi ias/L}z^av^b.
\]
所以对 \(h\in C_c^\infty(\mathbb R)\)，
\[
 \mathscr U(h)(z^av^b)=\widehat h(2\pi a/L)z^av^b,\qquad
 \widehat h(\xi)=\int h(s)e^{-i\xi s}\,ds.                        \tag{22}
\]
若任一 \(\widehat h(2\pi a/L)\ne0\)，固定该 \(a\)、变化 \(b\) 就有无穷正交序列，
其像范数恒正，故算子不紧，更非迹类。
若所有这些采样为0，则该算子为0。
特别地，\(\int h\ne0\) 的平滑时间测试不能单靠规范GNS实现给出有限普通时间迹。
这只限定这一具体GNS实现，不否定414的另加径向压缩或新的相对迹。

## 8. 真实已交付的结构与剩余比较

本稿交付了 \(B\subset A_D\) 中、经嵌入成为 \(M(A)\) 元素的有限群支撑连接，
以及具有完整定义域的演化、
模边界理想的平行提升及满角上的精确动力系统。
近锐连接范数发散、裸素数协变丢失、规范GNS无穷重数也都有具体证明。

仍需在414的原表示与原 \(C_N\) 中定义并核验
\[
 A_N^c(h)=\sum_{g\in\Gamma}C_NP_gU^c(h)C_N,\qquad
 U^c(h)=\int h(s)U_s^c\,ds,
\]
其中积分首先只按强算子意义定义。
必须另证逐 \(g\) 的迹类和全 \(\Gamma\) 迹范数收敛，再计算与 \(A_N(h)\) 的实际差。
有界酉演化本身不提供这些迹性质，有限带 \(K\) 的指数也可能产生无限群支。
要支付群权、时间核导数、径向衰减和原素数平移不交换的全部成本。
只有比较回固定源的周期分布、单位项与分割相容性，才可能进一步研究主消失。
本稿没有把新的特征定义成所需分布，也没有据此宣称F₁存在性或RH进展。

## 9. 来源和 Lean 范围

[Avron–Seiler–Yaffe原文及勘误核读](../reviews/2026-09-21/f1-projection-connection-source-read.md)
保留原PDF、公式位置和阅读范围。
投影连接与平行传输是已有方法；本稿的新工作范围是固定(2)、
原 \(A/I\)、原 \(\Gamma\) 和原时间表示中的实际系数与比较。
不使用勘误涉及的高阶绝热估计或原Lemma2.7有缺陷的证明。

[独立系数推导全文](../reviews/2026-09-21/f1-projection-connection-coefficient-review.md)
已覆盖(4)–(10)及理想位置；本稿后续演化与满角结论另作完整逆审。
[ProjectionConnection.lean](../formal/F1/Analysis/ProjectionConnection.lean)
及其[内核报告](../formal/checks/projection-connection-verification.json)
保存六项可复用投影微分、角内平行、反自伴与压缩恒等式：
Lean 4.32.2、固定mathlib、无sorryAx依赖。
实际Green系数、H¹定义域、Dyson级数、C*理想及GNS结论由本文直接证明；
第8节的原Γ迹性质与比较仍待证。未宣称这些解析结论已由六条Lean恒等式形式化。

## 10. 完成复核与紧邻比较

[417全文逆审](../reviews/2026-09-21/f1-projection-evolution-full-review.md)
核对原稿SHA256
`695860911f0c7f6e54ee5459808e0186c500f68c85bab770d3e11639a7cc7677`。
采纳其P3范围修正：连接范数发散不单独分类标量读出；
另明确乘子位置及第8节当时的待证范围。
[采纳闭环与418全文审查](../reviews/2026-09-21/f1-connection-periodized-trace-full-review.md)
核对修订稿SHA256
`3743fb7e6b54e4b6e2dddd5009832b84b885e23e706e2d1c0e0518bacae440cf`。
此后第1–9节未改，仅更新状态并添加本节；原稿和修订稿均在根archive按原字节保存。

[ConnectionEvolutionAlgebra.lean](../formal/F1/Analysis/ConnectionEvolutionAlgebra.lean)
新增四项可复用代数，固定Lean 4.32.2、固定mathlib、仅propext、无sorryAx。
[内核报告](../formal/checks/connection-evolution-algebra-verification.json)
和[源码审计](../formal/checks/connection-evolution-algebra-source-audit.json)
记录26份项目源码及原十处admission，历史报告保持，未全构建F1。

紧邻的[418](418-f1-connection-periodized-trace-and-sharp-frame.md)现已解决第8节的原Γ迹问题：
给出绝对迹范数收敛、全部周期系数与原迹的精确差。
它还证明本题两端共同紧支使有界时间区间内的群支实际上有限，
从而支付本节此前的一般有限带警示；不能对任意有限带指数无条件作此断言。
连接确实存在，但418的实际近锐p系数检验排除了该直接迹差作为对所有合法分割的固定主补偿。
继续[保留原时间的交叉积准入](../reviews/2026-09-21/f1-original-time-crossed-product-next-proof-plan.md)，
Goal第十节保持，未宣称主除子、完整B、双次数、RR或RH完成。
