# 515. 单素数与有限S的共同中央混合检测核

2026-10-11。[T/R] 接续[513](513-f1-single-prime-relative-chain-transfer.md)、
[514](514-f1-late-prime-tail-and-mixed-charge.md)。
在已准入的实际径向角内，紧支测试的一链家族可被中央混合电荷完全分离；
结论不识别全部HH₁的核，也不提供全局负性。

## 1. 实际家族与全部允许检测

取实偶 \(\eta\in C_c^\infty(\mathbb R)\)，
\(h(t)=e^{-t/2}\eta(t)\)、\(C_\eta=\Pi A_\eta\)。
在513明确构造的角商中，使用单位修正链
\[
 t_{U,\eta}=q(U^{-1})\otimes q(UC_\eta)-e\otimes qC_\eta.
                                                               \tag{1}
\]
U取真实单素数相位Vℓ或511的真实有限S Fourier–反演。
闭链性、来源、S₁准入均沿用原证明。

对每个实偶 \(\zeta\in C_c^\infty\)，实际卷积 \(A_\zeta\) 模S₁中央；
514的首因子链映射和显式b₂比较给
\[
 \Omega_\zeta([t_{U,\eta}])
       =\Omega([t_{U,\eta*\zeta}]).                            \tag{2}
\]
单位修正不可省略。这里仍是普通Hochschild同调，
不将首因子提升直接替换成未经核算的 \(\operatorname{Tr}(A_\zeta B_U)\)。

## 2. 任意支集的单素数共同核为零

固定 \(\ell\)、\(L=\log\ell\)、\(a=\ell^{-1/2}\)。定义实际电荷产生的有限正偶测度
\[
 \mu_\ell=L\sum_{n\ge1}a^n(\delta_{nL}+\delta_{-nL}),\qquad
 \mu_\ell(\mathbb R)=\frac{2La}{1-a}.                           \tag{3}
\]
由513的全部Euler电荷及(2)，
\[
 \Omega_\zeta([t_{\ell,\eta}])
 =2L\sum_{n\ge1}a^n(\eta*\zeta)(nL)
 =\int(\mu_\ell*\eta)(t)\zeta(t)\,dt.                           \tag{4}
\]
偶性支付最后相等；有限总质量与紧支输入支付换序。
\(F_{\ell,\eta}=\mu_\ell*\eta\) 实偶、光滑且属于L¹，
每阶导数有界，L¹范数至多 \(\mu_\ell(\mathbb R)\|\eta\|_1\)。

全部实偶紧支ζ检测为零等价于 \(F_{\ell,\eta}=0\)：
它是偶光滑函数，任意实测试可先偶化。
取无前因子的测试Fourier变换
\(\widehat\eta(\tau)=\int\eta(t)e^{-i\tau t}dt\)，得到
\[
 \widehat F_{\ell,\eta}=r_\ell\widehat\eta,\quad
 r_\ell(\tau)=
 \frac{2La(\cos(L\tau)-a)}{1-2a\cos(L\tau)+a^2}.                \tag{5}
\]
其零集恰是 \((2\pi k\pm\arccos a)/L\)，为离散集。
若F=0，连续的 \(\widehat\eta\) 在其稠密补集为零，遂处处为零。
Fourier唯一性给
\[
 \boxed{\bigcap_{\zeta\in C_{c,\mathrm{even}}^\infty(\mathbb R,\mathbb R)}
 \ker\{\eta\mapsto\Omega_\zeta([t_{\ell,\eta}])\}=\{0\}.}        \tag{6}
\]
不需要514的 \(L>2R_\eta\) 小支集条件。

实际上对每个非零η可选偶非负紧支χ，覆盖F的某个非零开区间，令
\(\zeta=\chi F_{\ell,\eta}\)。这是合法实偶紧支源，且
\[
 \Omega_\zeta([t_{\ell,\eta}])=\int\chi F_{\ell,\eta}^2>0.       \tag{7}
\]
检测器依赖η、ℓ；不声称一个统一有限支集的检测器能读出全部远端素数。

## 3. 有限素数增量也不能相互免费消去

对非空有限素数集合F，令 \(\mu_F=\sum_{\ell\in F}\mu_\ell\)。
它是有限正偶测度，Fourier变换 \(r_F\) 连续，且
\(r_F(0)=\sum_{\ell\in F}2\log\ell/(\sqrt\ell-1)>0\)。

若 \(\mu_F*\eta=0\)，则 \(\widehat\eta\) 在0附近为零。
紧支η的Fourier变换整函数，恒等定理给η=0。
因此在包含这些实际运输链的共同有限角中，
\[
 \eta\ne0\quad\Longrightarrow\quad
       \sum_{\ell\in F}[t_{\ell,\eta}]\ne0.                    \tag{8}
\]
合法中央混合电荷给同调检测；不是从边界算子非零猜出(8)。

## 4. 含完整实位的固定有限S共同核为零

沿用511–512的实际密度，记 \(\psi=\Gamma'/\Gamma\)，
\[
 a_S(\tau)=\log\pi-\Re\psi(\tfrac14+\tfrac{i\tau}{2})
 +2\sum_{p\in S_f}\log p\sum_{n\ge1}p^{-n/2}\cos(n\tau\log p).
                                                               \tag{9}
\]
它实偶、连续、增长至多 \(O_S(\log(2+|\tau|))\)，且
\[
 a_S(0)=\gamma+\frac\pi2+3\log2+\log\pi
       +2\sum_{p\in S_f}\frac{\log p}{\sqrt p-1}>0.             \tag{10}
\]
这是原Gamma常数和实际Euler费用，不重新选择相位或补δ₀。

定义
\[
 F_{S,\eta}(t)=\frac1{2\pi}
       \int a_S(\tau)\widehat\eta(\tau)e^{i\tau t}\,d\tau.       \tag{11}
\]
每阶频率矩绝对可积，所以F实偶光滑。
真实有限S中央作用与(2)给
\[
 \Omega_{S,\zeta}([t_{S,\eta}])
 =\frac1{2\pi}\int a_S\widehat\eta\,\widehat\zeta
 =\int F_{S,\eta}\zeta
 =2N_S(h*k_\zeta),\quad k_\zeta=e^{-t/2}\zeta.                 \tag{12}
\]
Fourier常数与513–514的测试约定一致。

全部混合读出为零使F=0。L¹ Fourier唯一性给
\(a_S\widehat\eta=0\)；由(10)，\(\widehat\eta\) 在0附近为零。
整函数恒等定理再次给η=0：
\[
 \boxed{\bigcap_\zeta
 \ker\{\eta\mapsto\Omega_{S,\zeta}([t_{S,\eta}])\}=\{0\}.}       \tag{13}
\]
不需RH，也不需要 \(a_S\) 在整个实轴符号固定。

## 5. 实际同调结论与范围

(6)、(13)说明线性映射
\(\eta\mapsto[t_{\ell,\eta}]\)、\(\eta\mapsto[t_{S,\eta}]\)
在实偶紧支测试家族上单射；(8)给全部有限增量的非零性。
中央性涵盖实际卷积、反演、Fourier、Π及全部迹类生成元，
而非只对一个相位成立。因此这些检测可在后续已说明的有限角扩大中保留。

这不证明混合电荷分离任意HH₁类，不说明整个HH₁核为零，
也不认证几何principal或提供无穷素数链。
非紧支卷积属于另一个准入问题，不能因其标量公式存在就自动放入原纯代数角。

[516](516-f1-global-mixed-radical-and-mellin-jets.md)比较完整算术标量核与真实源闭像；
[517](517-f1-weak-observable-limit-and-source-cutoffs.md)给读出层的弱全局化与源截断。
