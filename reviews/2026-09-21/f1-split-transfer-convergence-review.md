# 416：分别收敛与循环换位的独立推导

2026-09-21。以下为完整子问题报告；原始工具回包另存。仅整理标题和行末空白。

**候选证法成立。** 在 [414](H:/codex-build/RH/RH-Weil/notes/414-f1-deep-boundary-unitary-and-time-defect.md) 的共同表示及 [415](H:/codex-build/RH/RH-Weil/notes/415-f1-defect-projection-and-cutoff-residue.md) 的实际 \(T\) 下，对每个固定 \(N=(N_p,N_q)\)，\(S,G,H\) 分别绝对迹范数收敛。右乘 \(T\) 引入的 \(t'\) 依赖可以控制。

逐 \(g\) 的循环公式也成立，但循环后的**算子级数通常不收敛**；其**标量迹级数**仍绝对收敛。下面分别证明。全程未修改文件、未运行 Git。

1. **有限展开及系数依赖。**

记
\[
x=(j,k),\qquad \ell_s=s_1L+s_2M,\qquad
P_s=\pi(U_s)=W_s\otimes U_{\ell_s},
\]
其中
\[
(W_s\xi)(x)=\xi(x-s).
\]
以下把表示中的 \(\pi(T)\) 简记为 \(T\)。

由 \(u-1=\sum_{s\in E}\tau_s(t)U_s\)，
\[
T=\sum_{s\in E\cup\{0\}}M_{a_s}P_s,\qquad
a_s(x,t)=\mathbf1_{s=0}+Q(x)Q(x-s)\tau_s(t).
\]
这里支集有限，\(\tau_s\in C_c^\infty(\mathbb R)\)。因此
\[
\sup_{x,t}|\partial_t^j a_s(x,t)|<\infty
\quad(j\ge0).
\]
单位项不紧支，但这不影响后面的双压缩估计。

乘法、伴随分别满足
\[
(M_aP_s)(M_bP_r)
 =M_{a(x,t)b(x-s,t-\ell_s)}P_{s+r},
\]
\[
(M_aP_s)^*
 =M_{\overline{a(x+s,t+\ell_s)}}P_{-s}.
\]
故 \(T^*,TT^*,T^*T\) 仍具有同样的有限展开和全局导数界。

还应记录一个供后面单侧压缩使用的事实：这些实际系数都是有限个
\[
q_\nu(x)\varphi_\nu(t)
\]
之和，其中 \(q_\nu\) 有界，\(\varphi_\nu\) 光滑且各阶导数有界。这来自 \(Q\) 与时间系数的分离及有限乘法。

2. **右乘 \(T\) 后的核：\(t'\) 和 \(g\) 都可一致控制。**

取展开中的两个单项
\[
A=M_aP_s,\qquad D=M_bP_r,
\]
令 \(k=s+g+r\)。直接代换积分变量可得
\[
(AP_gU(h)D\psi)_x(t)
 =\int K_g^{\mathrm{右}}(x;t,t')\psi_{x-k}(t')\,dt',
\]
其中
\[
K_g^{\mathrm{右}}(x;t,t')
 =a(x,t)\,
 b(x-s-g,t'+\ell_r)\,
 h(t-t'-\ell_k).
\tag{A}
\]
所以右系数确实依赖 \(t'\)，不能把该算子直接写成原先的纯张量积。

另一种次序为
\[
(AP_gDU(h)\psi)_x(t)
 =\int K_g^{\mathrm{左}}(x;t,t')\psi_{x-k}(t')\,dt',
\]
\[
K_g^{\mathrm{左}}(x;t,t')
 =a(x,t)\,
 b(x-s-g,t-\ell_s-\ell_g)\,
 h(t-t'-\ell_k).
\tag{B}
\]

两式都满足：对任意固定 \(i,j\)，存在与 \(g\) 无关的常数
\[
\sup_{x,t,t'}
 \left|\partial_t^i\partial_{t'}^j
 K_g^{\mathrm{右/左}}(x;t,t')\right|
 \le M_{i,j}.
\tag{C}
\]
原因逐项明确：

- \(x-s-g\) 只是整数坐标平移，取全局上确界后不影响界；
- \(t-\ell_s-\ell_g\) 只是时间平移，微分不产生 \(\ell_g\) 因子；
- \(t'+\ell_r\) 的微分由 \(b\) 的导数界控制；
- \(h\) 的所有平移具有相同导数上确界。

这正补上了候选证明中需要核准的右系数问题。

3. **非负基给出双几何界，壳层基的符号不构成障碍。**

置
\[
R=R_{N_p+1,p}\otimes R_{N_q+1,q}.
\]
两投影 \(E_p,E_q\le R\)。取 \(R\) 的张量正交基 \(\{\zeta_\mu\}\)，每个因子均来自 414 的 \(e_j,b_K\)，故其坐标非负。

对任意有界对角系数 \(m(x;t,t')\)，
\[
\begin{aligned}
\left|
 \langle\zeta_\mu,M_mW_k\zeta_\nu\rangle
\right|
&\le \|m\|_\infty
 \sum_x\zeta_\mu(x)\zeta_\nu(x-k)\\
&\le A_N\|m\|_\infty
 \rho_p^{|k_1|}\rho_q^{|k_2|}.
\end{aligned}
\tag{D}
\]
最后一步就是 414 式 (22) 的逐矩阵元版本及张量分解。

对 \(m\) 的时间导数同样成立。求和中各导数由可求和的非负重叠支配，所以逐项微分也合法。特别地，结合 (C)，得到所有所需核导数的相同几何界。

不能直接声称壳层 \(S_N\) 的基坐标非负；正确做法是先在 \(R\) 的非负基中估计，再左右乘 \(E_p,E_q\)。后者是收缩，不增大迹范数。

又因 \(s,r\) 只取有限多个值，
\[
\rho_p^{|g_1+s_1+r_1|}
\rho_q^{|g_2+s_2+r_2|}
\le
\rho_p^{-|s_1+r_1|}
\rho_q^{-|s_2+r_2|}
\rho_p^{|g_1|}\rho_q^{|g_2|}.
\tag{E}
\]
所以有限展开只改变常数，不破坏可求和性。

具体地，展开两个 \(C\)，每块时间核都带
\[
d_\alpha(t)d_\beta(t'),\qquad \alpha,\beta\in\{p,q\}.
\]
取固定紧区间 \(I\)，使两个截止支集严格位于其内部。每个横向矩阵元在 \(I^2\) 上光滑，并在边界附近为零；可以向周期圆作光滑延拓。

在 \(t,t'\) 各分部积分两次，其 Fourier 矩阵元满足
\[
|\widehat K_{\mu\nu}(m,n)|
\le
\frac{B_N\,\rho_p^{|g_1|}\rho_q^{|g_2|}}
 {(1+m^2)(1+n^2)}.
\tag{F}
\]
这里混合导数最多涉及 \(h^{(4)}\)，其界对所有平移一致。有限横向矩阵展开与时间 Fourier 秩一展开遂给
\[
\boxed{
\begin{aligned}
\|CAP_gU(h)DC\|_1
 &\le B_{N,A,D,h}\rho_p^{|g_1|}\rho_q^{|g_2|},\\
\|CAP_gDU(h)C\|_1
 &\le B'_{N,A,D,h}\rho_p^{|g_1|}\rho_q^{|g_2|}.
\end{aligned}}
\tag{G}
\]
这里 \(A,D\) 可以是上述任意固定有限多项式，包括单位元。常数允许依赖 \(N\)。

4. **\(S,G,H\) 的每个展开项分别可求和，无须利用相消。**

定义
\[
\begin{aligned}
X_g&=CTT^*P_gU(h)C,\\
Y_g&=CT^*P_gU(h)TC,\\
Z_g&=CT^*TP_gU(h)C,\\
V_g&=CT^*P_gTU(h)C.
\end{aligned}
\]
由 (G)，这四个级数分别绝对迹范数收敛。且
\[
S_g=X_g-Y_g,\qquad
G_g=Z_g-V_g,\qquad
H_g=V_g-Y_g.
\]
因此
\[
\sum_g\bigl(\|S_g\|_1+\|G_g\|_1+\|H_g\|_1\bigr)<\infty.
\tag{H}
\]
所用数值级数为
\[
\sum_{a,b\in\mathbb Z}\rho_p^{|a|}\rho_q^{|b|}
=
\frac{1+\rho_p}{1-\rho_p}
\frac{1+\rho_q}{1-\rho_q}<\infty.
\]

于是 415 式 (18) 可以在迹类空间中逐项求和：
\[
\sum_g C[T,T^*]B_gC=S-G-H,
\]
并可取普通迹：
\[
\Phi_N(F,h)=\operatorname{Tr}S-\operatorname{Tr}G-\operatorname{Tr}H.
\tag{I}
\]

5. **逐 \(g\) 循环成立，但必须先证明单侧压缩的迹类性。**

对 \(A=T^*\) 或 \(TT^*\)，上述有限分离展开写成
\[
A=\sum_\nu D_\nu\otimes M_{\varphi_\nu}U_{\lambda_\nu},
\]
其中 \(D_\nu\) 是有界横向算子。于是 \(CAU(h)\) 是有限个张量积之和，其横向因子为 \(E_\alpha D_\nu\)，具有有限秩；时间因子的核为
\[
d_\alpha(t)\varphi_\nu(t)
 h(t-t'-\lambda_\nu).
\]
因为 \(d_\alpha,h\) 紧支，该核在 \((t,t')\) 中具有紧支且光滑；同样的 Fourier 秩一展开证明它是迹类。因此
\[
CT^*U(h),\quad CTT^*U(h)\in\mathcal S_1.
\tag{J}
\]

利用 \(P_gU(h)=U(h)P_g\)，得到
\[
CT^*B_g,\quad CTT^*B_g\in\mathcal S_1.
\]
现在每次循环都有明确的迹类因子：
\[
\begin{aligned}
\operatorname{Tr}(CTT^*B_gC)
 &=\operatorname{Tr}(C^2TT^*B_g),\\
\operatorname{Tr}(CT^*B_gTC)
 &=\operatorname{Tr}(TC^2T^*B_g).
\end{aligned}
\]
第一行循环迹类因子 \(CTT^*B_g\) 与有界因子 \(C\)；第二行循环迹类因子 \(CT^*B_g\) 与有界因子 \(TC\)。

故确实有
\[
\boxed{
\operatorname{Tr}\bigl(C[T,T^*B_g]C\bigr)
 =
\operatorname{Tr}\bigl([C^2,T]T^*B_g\bigr).
}
\tag{K}
\]
右侧两个展开项 \(C^2TT^*B_g\)、\(TC^2T^*B_g\) 也分别是迹类。这并未把没有任何截止的 \(TT^*B_g\) 等算子当成迹类。

6. **循环后的算子级数为何不能声称收敛。**

令
\[
K_N=[C^2,T]T^*U(h)\in\mathcal S_1.
\]
则有精确等式
\[
[C^2,T]T^*B_g=K_NP_g,
\]
从而
\[
\boxed{\ \|[C^2,T]T^*B_g\|_1=\|K_N\|_1\quad\text{对所有 }g.\ }
\tag{L}
\]
所以若 \(K_N\ne0\)，这些项连迹范数趋零都不满足；循环后的算子级数不能按迹范数收敛。只有 \(K_N=0\) 时该级数才逐项为零。

两个分开的单侧压缩级数问题更明显。例如
\[
\|C^2TT^*B_g\|_1=\|C^2TT^*U(h)\|_1.
\]
当 \(h\ne0\) 时，此固定范数严格为正：取单位横向向量
\[
\xi\in\operatorname{ran}R_{N_p,p}
 \otimes\operatorname{span}\{e_{-N_q-1}\}.
\]
在这一子空间 \(Q=0\)，故 \(T=T^*=1\)，而
\[
C^2TT^*U(h)(\xi\otimes f)
 =\xi\otimes M_{c^2}U(h)f.
\]
\(M_{c^2}U(h)\ne0\)。因此该单侧压缩算子级数必定不按迹范数收敛；\(TC^2T^*B_g\) 同理。

另一方面，由 (K) 和已证明的双压缩估计，
\[
\sum_g
 \left|\operatorname{Tr}([C^2,T]T^*B_g)\right|
\le \sum_g\|S_g\|_1<\infty.
\]
所以合法的表达是
\[
\operatorname{Tr}S
 =\sum_g\operatorname{Tr}([C^2,T]T^*B_g),
\]
这里右侧是绝对收敛的**标量级数**，不能改写成一个未经定义的未双压缩算子和的迹。所有这些结论均限定于每个固定 \(N\)。
