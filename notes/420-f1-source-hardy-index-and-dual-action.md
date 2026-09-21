# 420. 实际源的 Hardy 指数族、拼接符号与原时间对偶作用

2026-09-21。状态：全文独立逆审通过；实际族与指数计算，尚无算术主消失。基础对象与原迹接口采用[419](419-f1-original-time-crossed-product-and-trace-interface.md)；实际源关系来自[414](414-f1-deep-boundary-unitary-and-time-defect.md)。

本稿从原源构造真正的参数 Fredholm 族，计算其指数线丛，并保留原时间对偶作用及截止的准确变换。约定
\[
\widehat f(\xi)=\int_{\mathbb R}f(t)e^{-it\xi}\,dt,\quad
T_s f(t)=f(t-s),\quad P_+=\mathbf1_{\xi\ge0}.
\]
固定不同素数 \(p,q\)，\(L=\log p,M=\log q\)，及实光滑紧支 \(c\) 满足
\(\sum_n c(t-nL)^2=1\)。在 \(\zeta=(e^{i\theta},e^{i\phi})\) 上，实际源为
\[
e_\zeta=\sum_n\zeta_p^n M_{c(t)c(t-nL)}T_{nL},\qquad
v_\zeta=\sum_n\zeta_p^n\zeta_q M_{c(t)c(t-nL-M)}T_{nL+M},
\quad u_\zeta=1-e_\zeta+v_\zeta .
\]
各和只有有限项；\(e_\zeta\) 是投影，\(v_\zeta^*v_\zeta=v_\zeta v_\zeta^*=e_\zeta\)，故 \(u_\zeta\) 酉。419已证 \(u_\zeta-1\) 非紧；本稿不以它本身充当紧算子单位化中的类。

定向取 \(d\theta\wedge d\phi\)，指数取“核减余核”，\(c_1\) 取底层实二维丛按复定向的 Euler 类。结论为
\[
\operatorname{ind}(P_+u_\zeta P_+)=0,\qquad
\operatorname{Ind}(P_+u_\zeta P_+)=[\mathscr L]-[1],\qquad
\langle c_1(\mathscr L),[\mathbb T^2]\rangle=-1,
\]
其中线丛的具体拼接是 \((2\pi,z,\lambda)\sim(0,z,z\lambda)\)。这是固定压缩方向下的实际计算；未以外部教材的 Thom/Bott 符号代替本稿的端点核验，也未据此证明算术周期迹比较。

## 1. Hilbert–Schmidt 交换子的准确常数。

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

## 2. 连续 Fredholm 族及各点指数零。

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

## 3. 固定原 \(M\) 的实际乘法分解。

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

## 4. 实际 Green 等距嵌入及其过渡。

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

## 5. 把实际压缩换成可计算的 Green 压缩。

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

## 6. 一次秩一稳定化给出明确指数线丛。

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

## 7. 第一 Chern 数的符号核准。

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

## 8. 对偶作用与 \(\Phi\) 下的分解一致。

按本文采用的约定，
\[
\widehat\beta_\nu|_{i_A(A)}=\mathrm{id},\qquad
\widehat\beta_\nu(V_s)=e^{i\nu s}V_s.
\]
这里“固定原 \(A\)”是对其规范乘子像逐元素固定。因此
\[
\widehat\beta_\nu(P_g)=P_g,\qquad
\boxed{\widehat\beta_\nu(Z_g)=e^{-i\nu\ell_g}Z_g.}
\tag{31}
\]

另一方面，
\[
M_\nu T_sM_\nu^*=e^{i\nu s}T_s.
\]
结合
\[
\Phi(P_g)=z_g\otimes T_{\ell_g},\quad
\Phi(V_s)=1\otimes T_s,\quad
\Phi(Z_g)=z_g\otimes1,
\]
得到
\[
\boxed{
\Phi\widehat\beta_\nu\Phi^{-1}
=\gamma_\nu\otimes\operatorname{Ad}M_\nu,
\qquad
\gamma_\nu(z_g)=e^{-i\nu\ell_g}z_g.
}
\tag{32}
\]
特别地，\(P_g\) 上两因子相位相反，准确抵消。

深边界的公式因而是
\[
\boxed{
(\widehat\beta_\nu F)(\zeta)
=M_\nu F(r_\nu\zeta)M_\nu^*,
}
\tag{33}
\]
其中
\[
r_\nu(\zeta_p,\zeta_q)
=(e^{-i\nu L}\zeta_p,e^{-i\nu M}\zeta_q).
\]
对坐标函数 \(\zeta^g\) 代入即可检查负号。

连续性边界是：\(\gamma_\nu\) 和
\(\operatorname{Ad}M_\nu|_{\mathbb K_t}\) 逐元素范数连续；不需要、也不能据此声称 \(M_\nu\) 本身算子范数连续。

## 9. 原表示的实施酉及截止变换正确。

令
\[
R_\nu=D_\nu\otimes M_\nu,\qquad
D_\nu\delta_m=e^{-i\nu\ell_m}\delta_m.
\]
直接计算
\[
D_\nu\lambda_gD_\nu^*=e^{-i\nu\ell_g}\lambda_g.
\]
故原表示中
\[
R_\nu(\lambda_g\otimes T_{\ell_g})R_\nu^*
=\lambda_g\otimes T_{\ell_g}.
\]
原系数乘法算子也与 \(R_\nu\) 交换，而
\[
R_\nu(1\otimes T_s)R_\nu^*
=e^{i\nu s}(1\otimes T_s).
\]
因此
\[
\boxed{
\Pi(\widehat\beta_\nu(b))
=R_\nu\Pi(b)R_\nu^*.
}
\tag{34}
\]

在原坐标上，\(R_\nu\) 是乘法
\[
e^{i\nu(t-\ell_m)};
\]
在 \(x=t-\ell_m\) 坐标上就是 \(e^{i\nu x}\)。这核准了它与原 \(\pi(A)\) 交换的说法。

这里的实施酉位于具体表示的 \(B(\mathcal H)\)；不能仅由 (34) 宣称对偶作用是交叉积乘子内部的内自同构。

因为 \(M_\nu\) 与 \(M_{d_\alpha}\) 交换，
\[
\boxed{
C_N^\nu=R_\nu C_NR_\nu^*
=\sum_\alpha D_\nu E_\alpha D_\nu^*
 \otimes M_{d_\alpha}.
}
\tag{35}
\]
各 \(E_\alpha\) 有限秩，所以其共轭仍属于径向紧算子理想；(35) 与将 \(C_N\) 放在时间交叉积乘子代数中的解释相容。原截止一般不固定。

## 10. 完整 \(\Gamma\) 迹的相位确实逐项抵消。

定义
\[
h_\nu(s)=e^{i\nu s}h(s).
\]
由于原 \(P_g\) 固定，
\[
\boxed{
R_\nu\bigl(C_NP_gU(h)C_N\bigr)R_\nu^*
=C_N^\nu P_gU(h_\nu)C_N^\nu.
}
\tag{36}
\]
因此每项的迹范数保持不变，原绝对迹范数收敛立即传递到右侧，并有
\[
R_\nu A_N(h)R_\nu^*
=\sum_gC_N^\nu P_gU(h_\nu)C_N^\nu.
\tag{37}
\]
这无需重新从调制后的导数界证明收敛。

直接求迹也核准上述符号。径向对角块满足
\[
\operatorname{Tr}
\bigl(E_\alpha^\nu\lambda_gE_\alpha^\nu\bigr)
=e^{i\nu\ell_g}
\operatorname{Tr}(E_\alpha\lambda_gE_\alpha),
\tag{38}
\]
而时间对角因子为
\[
h_\nu(-\ell_g)
=e^{-i\nu\ell_g}h(-\ell_g).
\tag{39}
\]
两相位相消。交叉块仍因
\[
E_\alpha^\nu E_\beta^\nu=0\quad(\alpha\ne\beta)
\]
而具有零横向迹。因此对全部 \(g\) 都成立，没有预先删除混合次数。

结论是
\[
\boxed{
\operatorname{Tr}\bigl(R_\nu A_N(h)R_\nu^*\bigr)
=\operatorname{Tr}A_N(h),
}
\tag{40}
\]
**不是**
\(\operatorname{Tr}A_N(h_\nu)=\operatorname{Tr}A_N(h)\)。

这里使用419第7节已证的开理想归属，故也可将实施酉共轭写成 \(\widehat\beta_\nu(A_N(h))\)。

## 11. 实际源固定与阈值压缩的等变式正确。

源族中的每个非恒等单项形如
\[
\zeta_p^n\zeta_q^bM_fT_{nL+bM}.
\]
代入 \(r_\nu\zeta\) 产生相位
\(e^{-i\nu(nL+bM)}\)，而 \(\operatorname{Ad}M_\nu\) 产生相反相位。故逐项有
\[
\boxed{M_\nu u_{r_\nu\zeta}M_\nu^*=u_\zeta.}
\tag{41}
\]
这里“源固定”指**整个乘子截面在基空间旋转和时间共轭的联合作用下固定**；并非单独断言 \(u_{r_\nu\zeta}=u_\zeta\)。

给定 Fourier 约定下，
\[
\widehat{M_\nu f}(\xi)=\widehat f(\xi-\nu),
\]
因此
\[
\boxed{
M_\nu P_+M_\nu^*=P_\nu
=\mathbf1_{[\nu,\infty)}(\xi).
}
\tag{42}
\]
结合 (41)，得到准确等变式
\[
\boxed{
P_\nu u_\zeta P_\nu
=M_\nu\bigl(P_+u_{r_\nu\zeta}P_+\bigr)M_\nu^*.
}
\tag{43}
\]

应明确其 Fredholm 解释：左侧作用在
\[
\mathcal H_\nu=P_\nu L^2(\mathbb R),
\]
而 \(M_\nu:\mathcal H_+\to\mathcal H_\nu\) 是酉同构。故已有真实 Hardy Fredholm 族立即给出所有阈值的 Fredholm 族，不需要任何紧扰动论证。

## 12. 投影差不紧，但指数传递不受影响。

对 \(\nu\ne0\)，
\[
P_\nu-P_+
=
\begin{cases}
-\mathbf1_{[0,\nu)}(\xi),&\nu>0,\\
+\mathbf1_{[\nu,0)}(\xi),&\nu<0.
\end{cases}
\tag{44}
\]
非零有限区间上的 \(L^2\) 空间仍为无限维，故该投影差无限秩、不紧，范数为 \(1\)。更一般，
\[
\|P_\nu-P_\mu\|=1\qquad(\nu\ne\mu).
\]
因此不能把这些投影视为固定 Hilbert 空间上的范数连续投影路径。

但用 \(M_\nu\) 识别移动的 Hilbert 空间后，(43) 变成
\[
M_\nu^*
\bigl(P_\nu u_\zeta P_\nu|_{\mathcal H_\nu}\bigr)M_\nu
=T_0(r_\nu\zeta).
\tag{45}
\]
右侧是已证范数连续的参数族。因此这一识别后，连 \((\nu,\zeta)\) 的联合范数连续性也直接成立。

指数束满足
\[
\boxed{\operatorname{Ind}T_\nu=r_\nu^*\operatorname{Ind}T_0.}
\tag{46}
\]
\(r_\nu\) 是与恒等同伦的环面平移，所以普通 \(K^0\) 类不变。接上已经完成的实际指数计算，每个阈值仍有
\[
\operatorname{rank}\operatorname{Ind}T_\nu=0,\qquad
\langle c_1(\operatorname{Ind}T_\nu),[\mathbb T^2]\rangle=-1,
\]
沿用 \((\arg\zeta_p,\arg\zeta_q)\) 的定向和“核减余核”约定。

这里的信息边界是：**带标记的对偶作用保留**
\[
\ell_g=g_1L+g_2M
\]
及频率 \(L,M\)；普通指数类本身则只有这里的秩与 Chern 数据，且所有 \(r_\nu\) 在普通 \(K^0\) 上作用相同。它不能据此恢复完整周期迹。后续应同时保存对偶作用、原截止及测试算子的变换规则，不能用普通指数类替代这些数据。

## 13. 依赖、来源与仍缺少的算术连接

第1–7节的[独立构造回报](../reviews/2026-09-21/f1-source-hardy-index-derivation.md)及其raw保存完整；第8–12节的[对偶作用复核](../reviews/2026-09-21/f1-original-time-dual-action-review.md)逐项核对原表示、全部Γ、截止及频率阈值。它们是分块证据，不能提前代替本整合稿的全文复核。

复圆周丛平凡性、拼接及Euler/Chern背景见[Hatcher原件阅读范围](../reviews/2026-09-21/f1-source-hardy-index-source-read.md)。具体HS常数、压缩模型、稳定化核线、符号和对偶作用都由本文实际计算，未从教材直接移入。

这里已经回答“原非紧源是否能给出真正的连续Fredholm族及其实际指数类”。它尚未回答“哪个相对／循环读出能恢复固定通常ζ的周期分布”。原来的 \(A_N(h)\) 在普通边界商中为零，而普通指数类的秩与Chern数也未记录测试函数 \(h\)、截止、全部周期系数。因此下一步须构造并比较保留这些数据的具体相对读出；不能仅把本稿的整数或线丛重新命名为算术交叉数。

主除子根空间、两次数、RR、完整Weil形式、实际F₁目标空间非空及RH仍未由本稿解决。

## 14. 全文验收与可复用形式化

[完整独立逆审](../reviews/2026-09-21/f1-source-hardy-index-full-review.md)及[raw](../reviews/2026-09-21/f1-source-hardy-index-full-review.raw.json)
逐节覆盖十三节、(1)–(46)，无必要改正；审稿SHA256为23888acba701fff24f9fb79109a2164974f6730d568873d68eb1f98c7e022b25。
第1–13节保留该审稿正文。分块回报现在有全文审查衔接，不扩大为原教材全书或外部同行评审。

[SchurIndexAlgebra.lean](../formal/F1/Analysis/SchurIndexAlgebra.lean)保存任意非交换环上
上下三角双侧逆元和两种二阶Schur消元共四条结果。
[固定Lean4.32.2内核报告](../formal/checks/schur-index-algebra-verification.json)通过，无sorryAx；
SHA256为050a5484a8af91cf71b214ba211f166fe19e5997c04a76ec08707563a6f57118。
它只核验通用同型方块的乘法次序和符号，不把不同Hilbert空间间的矩形块、全局Hilbert丛、
HS分析、Fredholm指数或Chern计算算作机器形式化。完整数学范围由上述纸面证明与逆审承担。

后续执行[保留时间测试的迹缺陷任务单](../reviews/2026-09-21/f1-hardy-weighted-trace-defect-next-proof-plan.md)。
