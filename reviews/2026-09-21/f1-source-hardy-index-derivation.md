# 原源酉元的正频率指数族：独立推导全文

2026-09-21。原始回包见[raw](f1-source-hardy-index-derivation.raw.json)。仅添加标题和本段，完整保留系数、归一化、指数丛构造和符号计算。主稿整合及全文逆审仍待完成。

**本侧题可以完整算出。** 按
\[
\widehat f(\xi)=\int_{\mathbb R}f(t)e^{-it\xi}\,dt,\qquad
P_+=\mathbf1_{[0,\infty)}(\xi),
\]
并以
\[
z_p=e^{i\theta},\quad z_q=e^{i\phi},\qquad
d\theta\wedge d\phi
\]
定向参数环面，采用指数“核减余核”的约定，实际压缩族
\[
T_z=P_+u_zP_+:\mathcal H_+\to\mathcal H_+
\]
满足：

\[
\boxed{
\operatorname{ind}T_z=0\quad\text{对每个 }z,\qquad
\left\langle c_1(\operatorname{Ind}T),[\mathbb T^2]\right\rangle=-1.
}
\]

下面直接从实际源构造指数线丛，不预认它等于某个 Thom 符号。只读核对了 414 的源定义；未写文件或运行构建。

1. **Hilbert–Schmidt 交换子的准确常数。**

令 \(\mathcal F=(2\pi)^{-1/2}\widehat{\phantom f}\) 为酉 Fourier 变换。对 \(f\in C_c^\infty(\mathbb R)\)，
\[
\bigl(\mathcal F[P_+,M_fT_a]\mathcal F^{-1}\bigr)(\xi,\eta)
=
\frac{\mathbf1_{\xi\ge0}-\mathbf1_{\eta\ge0}}{2\pi}
\,\widehat f(\xi-\eta)e^{-ia\eta}.
\]
固定 \(\omega=\xi-\eta\) 后，两频率异号的 \(\eta\)-集合长度恰为 \(|\omega|\)。因此
\[
\boxed{
\|[P_+,M_fT_a]\|_2^2
=\frac1{4\pi^2}
\int_{\mathbb R}|\omega|\,|\widehat f(\omega)|^2\,d\omega.
}
\tag{1}
\]
常数与 \(a\) 无关。等价地，
\[
\|[P_+,M_fT_a]\|_2^2
=\frac1{4\pi^2}
\iint_{\mathbb R^2}
\frac{|f(t)-f(t')|^2}{|t-t'|^2}\,dt\,dt'.
\tag{2}
\]

记
\[
f_n(t)=c(t)c(t-nL),\qquad
g_n(t)=c(t)c(t-nL-M),
\]
并设
\[
H(f)=\frac1{2\pi}
\left(\int|\omega|\,|\widehat f(\omega)|^2\,d\omega\right)^{1/2}.
\]
两组系数均只有有限多个非零项。于是
\[
[P_+,u_z]
=-\sum_nz_p^n[P_+,M_{f_n}T_{nL}]
+\sum_nz_p^nz_q[P_+,M_{g_n}T_{nL+M}],
\]
并有显式统一界
\[
\boxed{
\sup_z\|[P_+,u_z]\|_2
\le\sum_nH(f_n)+\sum_nH(g_n)<\infty.
}
\tag{3}
\]
有限个相位多项式还直接给出
\[
z\longmapsto[P_+,u_z]\in\mathcal S_2
\]
的连续性，事实上为 \(C^\infty\) 连续族。这里没有把算子范数连续误当成 HS 连续。

2. **连续 Fredholm 族及各点指数零。**

414 的实际酉关系在每个参数表示下给出 \(u_z^*u_z=u_zu_z^*=1\)。同时 \(z\mapsto u_z\) 算子范数连续。因此 \(T_z\) 范数连续，且
\[
\begin{aligned}
T_zT_z^*-1_{\mathcal H_+}
&=-P_+u_z(1-P_+)u_z^*P_+,\\
T_z^*T_z-1_{\mathcal H_+}
&=-P_+u_z^*(1-P_+)u_zP_+.
\end{aligned}
\tag{4}
\]
右侧是两个 HS 因子的乘积，故为迹类，并随 \(z\) 迹范数连续。这证明了 Fredholm 性及连续参数子。

普通指数在连通的 \(\mathbb T^2\) 上恒定。考察 \(z=(1,1)\)：此时 \(u_z\) 的系数和时间平移均为实，故与复共轭 \(C\) 交换。给定 Fourier 约定下，
\[
CP_+C=1-P_+,
\]
其中零频点对 \(L^2(\mathbb R)\) 无影响。

于是正、负频压缩具有相同指数。另一方面，\(u_{(1,1)}\) 与两个压缩的直和仅差紧算子，故两指数之和为零。因此
\[
\boxed{\operatorname{ind}T_z=0\quad\forall z\in\mathbb T^2.}
\tag{5}
\]
这只确定指数束的秩，并不排除非零的约化指数类。

3. **固定原 \(M\) 的实际乘法分解。**

写 \(e_\theta=e_{e^{i\theta}}\)，并令
\[
b_\theta=1-e_\theta+v_{e^{i\theta},1},
\qquad
a_{\theta,z_q}=1-e_\theta+z_qe_\theta.
\]
由于 \(e_\theta v_{\theta,1}=v_{\theta,1}e_\theta=v_{\theta,1}\)，有准确分解
\[
\boxed{u_{\theta,z_q}=a_{\theta,z_q}b_\theta.}
\tag{6}
\]
两个因子均酉，且与 \(P_+\) 的交换子均为 HS 连续族。压缩乘法满足
\[
T(a)T(b)-T(ab)
=-P_+a(1-P_+)bP_+,
\tag{7}
\]
右侧为连续迹类族。因此指数束的乘法可加性给
\[
\operatorname{Ind}T(u)
=\operatorname{Ind}T(a)+\operatorname{Ind}T(b).
\tag{8}
\]

其中 \(b_\theta\) 仅依赖 \(z_p\)，且它就是原族在 \(z_q=1\) 上的限制。由 (5)，其普通指数为零。复向量丛在圆周上的稳定类仅由秩决定，所以
\[
\operatorname{Ind}T(b)=0\in K^0(S^1).
\]
拉回参数环面后仍为零。故
\[
\boxed{\operatorname{Ind}T(u)=\operatorname{Ind}T(a).}
\tag{9}
\]
这一步始终保留原 \(M\)，没有对时间平移 \(T_M\) 作未经证明的算子范数同伦。

4. **实际 Green 等距嵌入及其过渡。**

令
\[
\mathcal E=L^2(\mathbb R/L\mathbb Z,dr).
\]
在 \(\theta\in[0,2\pi]\) 上定义
\[
(J_\theta f)(t)
=c(t)e^{i\theta t/L}f([t]).
\tag{10}
\]
平方分割直接给
\[
\|J_\theta f\|_2^2
=\int_0^L|f(r)|^2\sum_jc(r+jL)^2\,dr
=\|f\|_2^2.
\]
而逐项计算给
\[
J_\theta J_\theta^*\psi(t)
=\sum_n e^{in\theta}c(t)c(t-nL)\psi(t-nL)
=e_\theta\psi(t).
\tag{11}
\]
所以 \(J_\theta\) 是实际投影 \(e_\theta\) 的 Green 帧，不是另选的抽象秩一投影。

由于 \(c\) 紧支，\(J_\theta\) 随 \(\theta\) 算子范数连续。令
\[
(Rf)(r)=e^{2\pi ir/L}f(r).
\]
端点满足
\[
\boxed{J_{2\pi}=J_0R.}
\tag{12}
\]
在圆周 Fourier 基
\[
\varphi_m(r)=L^{-1/2}e^{2\pi imr/L}
\]
中，
\[
R\varphi_m=\varphi_{m+1}.
\tag{13}
\]
这是后面符号的实际来源：正向绕 \(z_p\) 一周，Green 过渡把模式 \(m\) 提升为 \(m+1\)。

定义
\[
Q_\theta=J_\theta^*P_+J_\theta.
\]
它是正压缩，满足 \(0\le Q_\theta\le1\)，以及
\[
Q_{2\pi}=R^*Q_0R.
\tag{14}
\]

令 \(P_{\rm circ}\) 为圆周模式 \(m\ge0\) 的投影。下面核准
\[
\boxed{Q_\theta-P_{\rm circ}\text{ 是连续紧算子族。}}
\tag{15}
\]
事实上它是 HS 连续族。因为
\[
J_\theta\varphi_m
=L^{-1/2}c(t)e^{i(2\pi m+\theta)t/L},
\]
正、负频泄漏的平方范数分别由
\[
\frac1{2\pi L}
\sum_{m\ge0}\int_{-\infty}^0
\left|\widehat c\!\left(\xi-\frac{2\pi m+\theta}{L}\right)\right|^2d\xi,
\tag{16}
\]
和
\[
\frac1{2\pi L}
\sum_{m<0}\int_0^\infty
\left|\widehat c\!\left(\xi-\frac{2\pi m+\theta}{L}\right)\right|^2d\xi
\tag{17}
\]
给出。这两个和由 \(\widehat c\) 的 Schwartz 衰减在
\(0\le\theta\le2\pi\) 上一致收敛，并对参数连续。因此
\[
P_+J_\theta-J_\theta P_{\rm circ}
\]
为 HS 连续族，而
\[
Q_\theta-P_{\rm circ}
=J_\theta^*(P_+J_\theta-J_\theta P_{\rm circ}),
\]
证明 (15)。

5. **把实际压缩换成可计算的 Green 压缩。**

令
\[
A_\theta=P_+J_\theta:\mathcal E\to\mathcal H_+.
\]
则
\[
T(a_{\theta,z_q})
=1_{\mathcal H_+}+(z_q-1)A_\theta A_\theta^*.
\tag{18}
\]
其伴随大小的压缩为
\[
F_{\theta,z_q}
=1_{\mathcal E}+(z_q-1)A_\theta^*A_\theta
=1+(z_q-1)Q_\theta.
\tag{19}
\]

二者指数束相同。一个直接核验是对矩阵
\[
\begin{pmatrix}
1&A_\theta\\
-(z_q-1)A_\theta^*&1
\end{pmatrix}
\]
分别按两个单位对角块作 Schur 消元，得到与
\[
\operatorname{diag}(T(a),1)
\quad\text{及}\quad
\operatorname{diag}(1,F)
\]
的连续可逆三角等价。

这里 \(\mathcal E\) 在 \(\theta\)-圆周上的粘合由 (12) 决定：
\[
(2\pi,\eta)\sim(0,R\eta).
\tag{20}
\]
相应地，(14) 保证 \(F\) 是这个 Hilbert 丛上的全局 Fredholm 族；不能忽略此过渡而把端点硬认成同一矩阵。

现在选连续光滑函数 \(\tau:[0,2\pi]\to[0,1]\)，端点附近分别为 \(0,1\)，且仅一次以正导数经过 \(1/2\)。设 \(E_{-1}\) 为模式 \(\varphi_{-1}\) 的投影，定义
\[
Q_\theta^{\rm mod}
=P_{\rm circ}+\tau(\theta)E_{-1}.
\tag{21}
\]
因为
\[
R^*P_{\rm circ}R=P_{\rm circ}+E_{-1},
\]
它满足与 (14) 相同的端点粘合。

凸同伦
\[
Q_\theta^{(r)}
=(1-r)Q_\theta+rQ_\theta^{\rm mod}
\]
保持 \(0\le Q_\theta^{(r)}\le1\)、端点粘合和“模紧等于 \(P_{\rm circ}\)”的性质。因此
\[
1+(z_q-1)Q_\theta^{(r)}
\]
始终是连续 Fredholm 族。指数计算遂归约到显式模型
\[
F^{\rm mod}_{\theta,z_q}
=1+(z_q-1)Q_\theta^{\rm mod}.
\tag{22}
\]

该模型在各模式上为
\[
\begin{cases}
z_q,&m\ge0,\\
1,&m\le-2,\\
f(\theta,z_q):=1-\tau(\theta)+\tau(\theta)z_q,&m=-1.
\end{cases}
\tag{23}
\]
唯一非可逆点满足
\[
\tau(\theta)=\frac12,\qquad z_q=-1.
\tag{24}
\]

6. **一次秩一稳定化给出明确指数线丛。**

为计算指数束，选一个单位截面
\[
v_\theta
=a(\theta)\varphi_0+b(\theta)\varphi_{-1},
\qquad a^2+b^2=1,
\]
满足：

- \(\theta=0\) 附近 \(a=1,b=0\)；
- 在 (24) 附近及直至 \(2\pi\)，\(a=0,b=1\)。

由于
\[
v_{2\pi}=\varphi_{-1}=R^*\varphi_0,
\]
它与 (20) 相容。

增广族
\[
\widetilde F_{\theta,z_q}:
\mathcal E\oplus\mathbb C\longrightarrow\mathcal E,
\qquad
(x,\lambda)\longmapsto F^{\rm mod}_{\theta,z_q}x+\lambda v_\theta
\tag{25}
\]
处处满射：在唯一非可逆点，附加列正好补上缺失的
\(\varphi_{-1}\) 方向。因此其核组成线丛 \(\mathscr L\)，并有
\[
\boxed{\operatorname{Ind}F^{\rm mod}=[\mathscr L]-[1].}
\tag{26}
\]

它的过渡可以直接算出。简写 \(z=z_q\)、\(f=1-\tau+\tau z\)。在参数圆柱上，核的处处非零帧为
\[
k(\theta,z)
=
\left(
a(\theta)fz^{-1}\varphi_0+b(\theta)\varphi_{-1},
\ -f
\right).
\tag{27}
\]
在唯一的 \(f=0\) 点，\(b=1\)，所以该帧仍非零。

两个端点为
\[
k(0,z)=(z^{-1}\varphi_0,-1),\qquad
k(2\pi,z)=(\varphi_{-1},-z).
\]
按 Green 粘合对第一分量施加 \(R\)，得到
\[
(R\oplus1)k(2\pi,z)
=(\varphi_0,-z)=z\,k(0,z).
\]
所以指数线丛的准确粘合关系是
\[
\boxed{
(2\pi,z_q,\lambda)\sim(0,z_q,z_q\lambda).
}
\tag{28}
\]

7. **第一 Chern 数的符号核准。**

为避免仅凭“粘合函数绕数”口头判号，可直接数一个截面的零点。

最后坐标投影
\[
\ell:\mathscr L\to\underline{\mathbb C},
\qquad \ell(x,\lambda)=\lambda,
\]
是 \(\mathscr L^*\) 的全局截面。它只在 (24) 处为零。在该点附近，帧 (27) 为
\[
(\varphi_{-1},-f),
\]
故截面的局部函数为 \(-f\)。

写 \(z_q=e^{i\phi}\)，零点为 \((\theta_*,\pi)\)，其中
\(\tau(\theta_*)=1/2\)、\(\tau'(\theta_*)>0\)。有
\[
\partial_\theta(-f)=2\tau'(\theta_*),\qquad
\partial_\phi(-f)=\frac{i}{2}.
\]
相对于参数定向 \(d\theta\wedge d\phi\)，这个零点的实 Jacobian 为正，故是一个正的简单零点。因此
\[
\left\langle c_1(\mathscr L^*),[\mathbb T^2]\right\rangle=1,
\qquad
\boxed{
\left\langle c_1(\mathscr L),[\mathbb T^2]\right\rangle=-1.
}
\tag{29}
\]

等价的谱流说明是：Green 过渡 \(R\) 把 Fourier 模式提升一级，模型 (21) 中恰有一个模式由 \(0\) 向 \(1\) 上穿 \(1/2\)，谱流为 \(+1\)。在本次实际压缩与“核减余核”约定下，它产生的指数线丛 Chern 数为 \(-1\)；此符号已经由上述零点计算独立核准。

结合 (9)、(18)–(29)，最终得到
\[
\boxed{
\operatorname{Ind}\bigl(P_+u_zP_+\bigr)
=[\mathscr L]-[1]\in K^0(\mathbb T^2),
\quad
\operatorname{rank}=0,\quad c_1=-1,
}
\tag{30}
\]
其中 \(\mathscr L\) 由 (28) 明确给出。

这是从实际 \(e_z,v_z,u_z\) 经乘法分解、Green 帧、紧扰动同伦和秩一稳定化得到的指数束。它不是先挑选一个抽象生成元再配给源对象，也不意味着原始 \(T_z\) 的核处处组成线丛。计算没有使用预定 Thom/Bott 符号，更未涉及算术迹扩张或边界补偿。
