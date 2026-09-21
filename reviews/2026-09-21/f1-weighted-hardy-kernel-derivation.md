# 原源带权Hardy迹：独立核推导全文

2026-09-21。完整原始回包见[raw](f1-weighted-hardy-kernel-derivation.raw.json)。本回报覆盖平滑源与一般迹范数有界读出；后续BV极限另审。

结论成立，而且有两个不同层次：**实际源的规范 Haar 平均逐频率为零；任意固定迹类算子的时间配对则具有 \(C_0\) 密度。进一步，迹范数一致有界的逼近族，其分布极限只能具有 \(L^\infty\) 密度，因而也不能逼近非零周期原子。** 后一个结论不能加强成“极限仍在 \(C_0\)”。

以下直接使用 [420 的实际系数和 Fourier 约定](H:/codex-build/RH/RH-Weil/notes/420-f1-source-hardy-index-and-dual-action.md:5)，不使用指数零来推导带权迹消失。

**实际系数、迹合法性与全部交叉项。**

固定
\[
T_af(t)=f(t-a),\qquad
\widehat f(\xi)=\int_{\mathbb R}f(t)e^{-it\xi}\,dt,\qquad
\mathcal F=(2\pi)^{-1/2}\widehat{\phantom f}.
\]
在频率空间中
\[
P=\mathbf1_{[0,\infty)},\quad R=1-P,\quad
U(h)=M_{\widehat h}.
\]
最后一个等式没有额外的 \(2\pi\) 因子。

令 \(b\in\{0,1\}\)，并记
\[
\begin{aligned}
\ell_{n,b}&=nL+bM,\\
k_{n,b}(t)&=c(t)c(t-\ell_{n,b}),\\
F_{n,b}(\omega)&=\widehat{k_{n,b}}(\omega),\\
\epsilon_0&=-1,\qquad \epsilon_1=1.
\end{aligned}
\]
于是
\[
u_z=1+\sum_{n,b}\epsilon_bz_p^nz_q^bM_{k_{n,b}}T_{\ell_{n,b}}.
\tag{1}
\]
所有和均为有限和：若 \(J=\operatorname{supp}c\)，则非零系数要求
\(\ell_{n,b}\in J-J\)。

首先分离恒等项：
\[
R1P=P1R=0.
\tag{2}
\]
因此不能把恒等项的 Fourier \(\delta\) 核放进后面的平方积分；但实际群零项
\[
-M_{k_{0,0}}=-M_{c^2}
\]
必须保留。

设
\[
X_z=Ru_zP,\qquad Y_z=Pu_zR,\qquad
B_z=X_z^*X_z-Y_zY_z^*.
\tag{3}
\]
这正是题设中被 \(U(h)\) 加权的两个缺陷之差。

单项 Fourier 核为
\[
\bigl(\mathcal FM_fT_a\mathcal F^{-1}\bigr)(\xi,\eta)
=\frac1{2\pi}\widehat f(\xi-\eta)e^{-ia\eta}.
\tag{4}
\]
由此
\[
H(f)^2:=\|[P,M_fT_a]\|_2^2
=\frac1{4\pi^2}\int_{\mathbb R}|\omega|
          |\widehat f(\omega)|^2\,d\omega.
\]
令
\[
H_c=\sum_{n,b}H(k_{n,b})<\infty.
\]
则 \(X_z,Y_z\) 是 HS 算子，而且
\[
\boxed{
\|B_z\|_1
\le \|X_z\|_2^2+\|Y_z\|_2^2
=\|[P,u_z]\|_2^2
\le H_c^2.
}
\tag{5}
\]
有限相位展开还给出 \(z\mapsto B_z\) 的 \(C^\infty\) 迹范数连续性。

对 \(\xi\ge0\)，定义两个非负频率密度
\[
\begin{aligned}
d_z^{(1)}(\xi)
&=\frac1{4\pi^2}\int_\xi^\infty
 \left|
 \sum_{n,b}\epsilon_bz_p^nz_q^b
 F_{n,b}(-\omega)e^{-i\ell_{n,b}\xi}
 \right|^2d\omega,\\
d_z^{(2)}(\xi)
&=\frac1{4\pi^2}\int_\xi^\infty
 \left|
 \sum_{n,b}\epsilon_bz_p^nz_q^b
 F_{n,b}(\omega)e^{-i\ell_{n,b}(\xi-\omega)}
 \right|^2d\omega,
\end{aligned}
\tag{6}
\]
并令 \(d_z=d_z^{(1)}-d_z^{(2)}\)。

这里外部频率为 \(\xi\ge0\)，内部频率为 \(\eta<0\)，换元是
\(\omega=\xi-\eta>\xi\)。第一个平方来自 \(u_z(\eta,\xi)\)，第二个来自
\(u_z(\xi,\eta)\)，故两个移位相位不同。

准确结果为
\[
\boxed{
\Psi_h(u_z^*,u_z)
=\int_0^\infty \widehat h(\xi)d_z(\xi)\,d\xi.
}
\tag{7}
\]

这不是未经论证的“取迹类核对角线”。例如对任意有界非负 \(\varphi\)，
\[
\operatorname{Tr}(M_\varphi X_z^*X_z)
=\|X_zM_{\sqrt\varphi}\|_2^2,
\]
以及
\[
\operatorname{Tr}(M_\varphi Y_zY_z^*)
=\|M_{\sqrt\varphi}Y_z\|_2^2.
\]
HS 核公式证明它们的密度分别是 (6)，再分解一般复值有界
\(\varphi\) 即得 (7)。全过程没有把 \(U(h)\) 移过 \(u_z\)。

为明确保留全部交叉项，写
\[
\Delta=(n-m)L+(b-d)M.
\]
则 (6) 完整展开为
\[
\boxed{
\begin{aligned}
d_z(\xi)
={}&\frac1{4\pi^2}
\sum_{\substack{n,m\\b,d\in\{0,1\}}}
\epsilon_b\epsilon_d
z_p^{n-m}z_q^{b-d}e^{-i\Delta\xi}\\
&\quad{}\times\int_\xi^\infty
\left[
F_{n,b}(-\omega)\overline{F_{m,d}(-\omega)}
-e^{i\Delta\omega}
 F_{n,b}(\omega)\overline{F_{m,d}(\omega)}
\right]d\omega .
\end{aligned}}
\tag{8}
\]
四类项的符号和相位如下；表中还共同乘有 \(z_p^{n-m}\)。

| 系数配对 | 符号 | \(z_q\) 相位 | \(\Delta\) |
|---|---:|---:|---|
| \(f_n,f_m\) | \(+\) | \(1\) | \((n-m)L\) |
| \(g_n,g_m\) | \(+\) | \(1\) | \((n-m)L\) |
| \(f_n,g_m\) | \(-\) | \(z_q^{-1}\) | \((n-m)L-M\) |
| \(g_n,f_m\) | \(-\) | \(z_q\) | \((n-m)L+M\) |

作为额外核对，全部 \(f\)-\(f\) 项汇总后已经为零，因为
\(e_z=e_z^*\)，故
\[
|(Re_zP)(\eta,\xi)|^2=|(Pe_zR)(\xi,\eta)|^2.
\]
这不允许逐个删除 \(f\)-\(g\) 交叉项；完整公式仍是 (8)。

**规范 Haar 平均逐频率为零。**

取
\[
dm(z)=\frac{d\theta\,d\phi}{(2\pi)^2}.
\]
角色正交性给出
\[
\int_{\mathbb T^2}z_p^{n-m}z_q^{b-d}\,dm(z)
=\mathbf1_{n=m}\mathbf1_{b=d}.
\]
因而对每个 \(\xi\ge0\)，
\[
\int_{\mathbb T^2}d_z(\xi)\,dm(z)
=\frac1{4\pi^2}\sum_{n,b}
\int_\xi^\infty
\bigl(|F_{n,b}(-\omega)|^2-|F_{n,b}(\omega)|^2\bigr)d\omega.
\tag{9}
\]
实际 \(k_{n,b}\) 为实函数，所以
\[
F_{n,b}(-\omega)=\overline{F_{n,b}(\omega)}.
\]
(9) 中每个被积函数均为零。因此
\[
\boxed{
\int_{\mathbb T^2}d_z(\xi)\,dm(z)=0
\quad(\forall\,\xi\ge0),
\qquad
\int_{\mathbb T^2}\Psi_h(u_z^*,u_z)\,dm(z)=0
\quad(\forall\,h\in C_c^\infty).
}
\tag{10}
\]

抵消机制是：Haar 平均删除不同群指标间的交叉项，剩余同群项由实系数的正负频率对称性抵消。这里没有使用普通指数零。

对一般有限展开，若多个项具有同一群指标，必须先合并其系数：
\[
a_g(t)=\sum_{j:g_j=g}a_j(t).
\]
Haar 平均会保留这些项之间的交叉项；正确剩余量是
\(|\widehat a_g(-\omega)|^2-|\widehat a_g(\omega)|^2\)，不能只保留每个原始项的模方。合并后的系数若为实函数，上述抵消仍成立。标量恒等项则先由 (2) 删除。

(10) 只证明 Haar 平均后的**时间配对**为零，没有证明
\(\int B_z\,dm(z)=0\) 作为算子成立。

**实际时间密度的连续性和一致性。**

由 (6) 和 HS 范数，
\[
\int_0^\infty d_z^{(1)}=\|X_z\|_2^2,\qquad
\int_0^\infty d_z^{(2)}=\|Y_z\|_2^2,
\]
故
\[
\|d_z\|_{L^1}\le H_c^2.
\tag{11}
\]
每个 \(F_{n,b}\) 都是 Schwartz 函数，而 (8) 是有限和。因此
\(d_z(\xi)\) 在 \(\mathbb T^2\times[0,\infty)\) 上光滑，其任意参数、频率导数都在
\(\xi\to\infty\) 时一致快速衰减。

定义
\[
\tau_z(s)=\int_0^\infty e^{-is\xi}d_z(\xi)\,d\xi.
\tag{12}
\]
由 Fubini，
\[
\boxed{
\Psi_h(u_z^*,u_z)=\int_{\mathbb R}h(s)\tau_z(s)\,ds,
\qquad
\|\tau_z\|_\infty\le H_c^2.
}
\tag{13}
\]
于是 \(\tau_z\in C_0(\mathbb R)\)，且所有时间导数也属于 \(C_0\)，对 \(z\) 一致。具体地，一次分部积分给出
\[
|\tau_z(s)|
\le\frac{|d_z(0)|+\|\partial_\xi d_z\|_1}{|s|}
\qquad(s\ne0),
\tag{14}
\]
右侧分子对固定 \(c,L,M\) 一致有界。

同时，(10) 给出
\[
\int_{\mathbb T^2}\tau_z(s)\,dm(z)=0
\qquad(\forall s\in\mathbb R).
\tag{15}
\]

**固定迹类配对的一般定理。**

更一般地，令 \(B\in\mathcal S_1(\mathcal H_+)\)，且 \(B\) 不依赖测试函数 \(h\)。存在唯一的 \(b_B\in L^1([0,\infty))\)，使
\[
\operatorname{Tr}(M_\varphi B)
=\int_0^\infty\varphi(\xi)b_B(\xi)\,d\xi
\quad(\forall\varphi\in L^\infty),
\qquad
\|b_B\|_1\le\|B\|_1.
\tag{16}
\]

一个直接构造是取奇异值展开
\[
B=\sum_j s_j\,|a_j\rangle\langle b_j|
\]
并置
\[
b_B(\xi)=\sum_j s_j a_j(\xi)\overline{b_j(\xi)}.
\]
该和在 \(L^1\) 中绝对收敛，因为
\[
\sum_j s_j\int|a_jb_j|
\le\sum_j s_j=\|B\|_1.
\]
等价地，\(b_B\,d\xi\) 是谱测度
\(E\mapsto\operatorname{Tr}(\mathbf1_E B)\) 的密度。

所以
\[
\begin{aligned}
\tau_B(s)
&=\operatorname{Tr}(T_sB)
=\int_0^\infty e^{-is\xi}b_B(\xi)\,d\xi
\in C_0(\mathbb R),\\
\operatorname{Tr}(U(h)B)
&=\int h(s)\tau_B(s)\,ds,
\end{aligned}
\tag{17}
\]
并且
\[
\boxed{
|\operatorname{Tr}(U(h)B)|
\le\|B\|_1\|h\|_{L^1}.
}
\tag{18}
\]
这里 \(C_0\) 性来自实际时间表示的绝对连续频谱及 Riemann–Lebesgue 引理，不是任意酉群表示都自动具有的性质。

还有连续性估计
\[
\|b_B-b_{\widetilde B}\|_1
\le\|B-\widetilde B\|_1,\qquad
\|\tau_B-\tau_{\widetilde B}\|_\infty
\le\|B-\widetilde B\|_1.
\tag{19}
\]
若参数空间紧且 \(z\mapsto B_z\) 迹范数连续，则其像在迹范数中紧。通过有限网和 (19) 可得
\[
\lim_{R\to\infty}\sup_z\sup_{|s|\ge R}|\tau_{B_z}(s)|=0,
\]
以及联合连续性和对 \(z\) 一致的时间连续性。

对于固定迹类 \(B\)，(17) 已严格排除与任何带非零原子的分布相等。

**有限变差参数测度及一致有界逼近族。**

设 \(\mu\) 是参数空间上的复测度，\(z\mapsto B_z\) 强可测，并满足
\[
C_\mu:=\int\|B_z\|_1\,d|\mu|(z)<\infty.
\tag{20}
\]
则 Bochner 积分
\[
B_\mu=\int B_z\,d\mu(z)
\]
属于迹类，且
\[
\begin{aligned}
b_{B_\mu}&=\int b_{B_z}\,d\mu(z)&&\text{在 }L^1\text{ 中},\\
\tau_{B_\mu}&=\int\tau_{B_z}\,d\mu(z)&&\text{在 }C_0\text{ 中},\\
\left|\int\operatorname{Tr}(U(h)B_z)\,d\mu(z)\right|
&\le C_\mu\|h\|_1.
\end{aligned}
\tag{21}
\]
实际族自动满足
\[
C_\mu\le H_c^2\|\mu\|_{\mathrm{TV}}.
\]
在 (8) 中，这种积分只是将角色
\(z_p^{n-m}z_q^{b-d}\) 替换为相应的测度矩
\(\int z_p^{n-m}z_q^{b-d}\,d\mu\)。非 Haar 权重可以保留交叉项，但所得时间分布仍具有 \(C_0\) 密度。

更强的统一结论如下。设一族与 \(h\) 无关的迹类算子满足
\[
\sup_i\|B_i\|_1\le C.
\]
若
\[
h\longmapsto\operatorname{Tr}(U(h)B_i)
\]
在 \(\mathcal D'(\mathbb R)\) 中收敛到 \(\Lambda\)，则由 (18)
\[
|\Lambda(h)|\le C\|h\|_1.
\]
将其连续延拓到 \(L^1\)，得到
\[
\boxed{
\Lambda(h)=\int h(s)F(s)\,ds
\quad\text{其中 }F\in L^\infty(\mathbb R),\
\|F\|_\infty\le C.
}
\tag{22}
\]
对变动的参数族和测度，只需替换为一致预算
\[
\sup_i\int\|B_{i,z}\|_1\,d|\mu_i|(z)\le C,
\tag{23}
\]
同一结论成立。所有算子及测度均须独立于 \(h\)。

必须保留 \(C_0\) 与 \(L^\infty\) 的区别。例如在频率空间取
\[
\psi_\varepsilon=\varepsilon^{-1/2}\mathbf1_{[0,\varepsilon]},
\qquad
B_\varepsilon=|\psi_\varepsilon\rangle\langle\psi_\varepsilon|.
\]
则 \(\|B_\varepsilon\|_1=1\)，但
\[
\tau_{B_\varepsilon}(s)
=\frac1\varepsilon\int_0^\varepsilon e^{-is\xi}\,d\xi
\longrightarrow1
\]
局部一致收敛。每个成员属于 \(C_0\)，极限却不属于 \(C_0\)。迹范数有界本身也不保证等度连续：将上述频率区间改为 \([n,n+1]\)，时间函数便带有任意快的 \(e^{-ins}\) 相位。

**与 414 原周期原子的具体比较。**

[414 式 (23)](H:/codex-build/RH/RH-Weil/notes/414-f1-deep-boundary-unitary-and-time-defect.md:245) 为
\[
\frac12\operatorname{Tr}A_N(h)
=D_Nh(0)
+L\sum_{a\ne0}\rho_p^{|a|}h(-aL)
+M\sum_{b\ne0}\rho_q^{|b|}h(-bM).
\tag{24}
\]
其中 \(\rho_p=p^{-1/2}\)。

由于 \(L/M\) 无理，
\[
\delta:=\min\{L,\operatorname{dist}(L,M\mathbb Z)\}>0.
\]
取 \(\varphi\in C_c^\infty((-1,1))\)，\(\varphi(0)=1\)，并令
\[
h_\varepsilon(s)=\varphi((s+L)/\varepsilon),
\qquad 0<\varepsilon<\delta/2.
\]
其支撑避开 \(0\)、其他 \(p\) 周期点和全部 \(q\) 周期点，故
\[
h_\varepsilon(-L)=1,\quad h_\varepsilon(0)=0,\quad
\frac12\operatorname{Tr}A_N(h_\varepsilon)=L\rho_p,
\tag{25}
\]
而
\[
\|h_\varepsilon\|_1=\varepsilon\|\varphi\|_1.
\]

对于任意迹范数预算不超过 \(C\) 的候选，(18) 给出
\[
\left|
\frac12\operatorname{Tr}A_N(h_\varepsilon)
-\operatorname{Tr}(U(h_\varepsilon)B)
\right|
\ge L\rho_p-C\varepsilon\|\varphi\|_1.
\tag{26}
\]
选择足够小的一个固定 \(\varepsilon\)，即可使右侧至少为
\(L\rho_p/2\)，**同时排除预算为 \(C\) 的所有候选**。式 (23) 的参数积分族也一样。

因此，若此类候选确实分布收敛到 (24) 的非零周期原子分布，其有效迹范数预算必须趋于无穷；仅仅改变环面参数或使用一致有界的有限变差权重不能做到这一点。对于规范 Haar 平均，(10) 更直接：其值恒为零，与 (25) 已明确冲突。

本结论的范围是“先有一个与 \(h\) 无关的迹类算子，再与 \(U(h)\) 配对”，及满足 (20) 的参数积分。414 的 \(A_N(h)\) 是先引入 \(h\) 平滑后才得到迹类的构造，不属于这里的前提。这一核验严格排除了题设的直接 Hardy 迹缺陷读出及其一致有界迹范数版本，没有排除其他相对迹构造。
