# 第421稿BV极限的独立复核

2026-09-21。[raw](f1-weighted-hardy-bv-limit-review.raw.json)保存完整回报；范围为§7–8及§9第二个量化界。

核验通过。所读文件 SHA-256 与指定值完全一致；仅审查了 §7–8 和 §9 的第二种量化界。**未发现需要修改的常数、迹交换或极限结论。新增论证确实允许未加权 HS／迹范数发散，并仍排除统一 BV 预算下的原子极限。**

下面给出独立推导，并明确几个定义边界。

**1. BV 估计与统一 \(L^2\) 预算。**

采用稿件约定
\[
\widehat f(\omega)=\int f(t)e^{-it\omega}\,dt,\qquad
\mathcal F=(2\pi)^{-1/2}\widehat{\phantom f}.
\]
这里 \(\operatorname{Var}f\) 应理解为**整个实线上的分布变差**
\(\lVert Df\rVert_{\mathrm{TV}}\)，包含紧支函数两端的跳跃。

对 \(f\in BV(\mathbb R)\cap L^1(\mathbb R)\)，
\[
|\widehat f(\omega)|\le\|f\|_1,\qquad
|\omega\widehat f(\omega)|=|\widehat{Df}(\omega)|
\le\operatorname{Var}f.
\]
直接相加便得
\[
(1+|\omega|)|\widehat f(\omega)|
\le\|f\|_1+\operatorname{Var}f.
\tag{A}
\]
因此稿件的 Fourier 界没有遗漏常数。

设
\[
u_\zeta=1+\sum_{g\in F}\zeta^gM_{f_g}T_{a_g},\qquad
A_f=\sum_{g\in F}(\|f_g\|_1+\operatorname{Var}f_g).
\]
有限个 BV 紧支系数本身已经保证 \(u_\zeta\) 有界：每个 \(f_g\) 本质有界，且 \(F\) 有限。

以下 \(K_\zeta\) 专指异号频率块的核；恒等项因 \(P1Q=0\) 已删除：
\[
K_\zeta(\xi,\eta)
=\frac1{2\pi}\sum_{g\in F}
 \zeta^g\widehat f_g(\xi-\eta)e^{-ia_g\eta}.
\]
由 (A)，
\[
|K_\zeta(\xi,\eta)|
\le\frac{A_f}{2\pi(1+|\xi-\eta|)}.
\tag{B}
\]

对 \(\xi\ge0\)，分别定义
\[
q_{1,\zeta}(\xi)=\int_{\eta<0}|K_\zeta(\eta,\xi)|^2\,d\eta,\qquad
q_{2,\zeta}(\xi)=\int_{\eta<0}|K_\zeta(\xi,\eta)|^2\,d\eta.
\]
两者均有限。因为
\[
\int_{-\infty}^0\frac{d\eta}{(1+\xi-\eta)^2}
=\frac1{1+\xi},
\]
所以
\[
0\le q_{j,\zeta}(\xi)
\le\frac{A_f^2}{4\pi^2(1+\xi)}.
\tag{C}
\]
令 \(d_\zeta=q_{1,\zeta}-q_{2,\zeta}\)。使用两项之和估计，
\[
|d_\zeta(\xi)|
\le\frac{A_f^2}{2\pi^2(1+\xi)},\qquad
\|d_\zeta\|_{L^2(0,\infty)}
\le\frac{A_f^2}{2\pi^2}.
\tag{D}
\]
最后用了 \(\int_0^\infty(1+\xi)^{-2}d\xi=1\)。稿件式 (15) 是正确的宽界。

于是对 \(h\in C_c^\infty(\mathbb R)\)，
\[
\Psi_h^{\mathrm{reg}}(\zeta)
=\int_0^\infty\widehat h(\xi)d_\zeta(\xi)\,d\xi
\]
绝对收敛，并满足
\[
\boxed{
|\Psi_h^{\mathrm{reg}}(\zeta)|
\le\frac{\sqrt{2\pi}\,A_f^2}{2\pi^2}\|h\|_2.
}
\tag{E}
\]
这里 \(\|\widehat h\|_2=\sqrt{2\pi}\|h\|_2\)，故式 (16) 的常数准确。

将 \(d_\zeta\) 在负半轴延为零，记作 \(\widetilde d_\zeta\)。其时间密度是
\[
k_\zeta=\widehat{\widetilde d_\zeta}
\quad\text{按 }L^2\text{ Fourier 变换定义},
\]
且
\[
\|k_\zeta\|_2=\sqrt{2\pi}\|d_\zeta\|_2,\qquad
\Psi_h^{\mathrm{reg}}(\zeta)=\int h(s)k_\zeta(s)\,ds.
\tag{F}
\]
此处一般不能直接使用双重积分 Fubini；可以先截断
\(d_\zeta\mathbf1_{[0,R]}\)，再用 \(L^2\) 收敛证明 (F)。稿件没有对 \(k_\zeta(0)\) 或逐点连续性作额外声明，这一点正确。

**2. 式 (17) 的真实算子定义成立。**

令
\[
m=\widehat h|_{[0,\infty)},\qquad
R_h=M_{\sqrt{|m|}},\qquad
V_h=M_{m/|m|},
\]
零集上相位取零。对于当前测试类，\(m\) 有界且属于 \(L^2\)，故 \(R_h,V_h\) 都是 \(\mathcal H_+\) 上的有界算子；\(V_h\) 是收缩，不必是酉。

设两个从 \(\mathcal H_+\) 到 \(\mathcal H_-\) 的算子为
\[
X_h=Qu_\zeta PR_h,\qquad Z_h=Qu_\zeta^*PR_h.
\]
其核分别为
\[
K_\zeta(\eta,\xi)\sqrt{|m(\xi)|},\qquad
\overline{K_\zeta(\xi,\eta)}\sqrt{|m(\xi)|},
\quad \eta<0,\ \xi\ge0.
\tag{G}
\]
第二式保留了正确的转置、共轭次序。

由 (C)，
\[
\begin{aligned}
\|X_h\|_2^2&=\int_0^\infty |m(\xi)|q_{1,\zeta}(\xi)\,d\xi,\\
\|Z_h\|_2^2&=\int_0^\infty |m(\xi)|q_{2,\zeta}(\xi)\,d\xi,
\end{aligned}
\]
且每项至多为
\[
\frac{A_f^2}{4\pi^2}
\int_0^\infty\frac{|m(\xi)|}{1+\xi}\,d\xi
\le\frac{A_f^2}{4\pi^2}\|m\|_2.
\tag{H}
\]
所以两个加权块确为 HS。这一证明没有使用未加权块为 HS。

对有界缺陷
\[
B_\zeta=Pu_\zeta^*Qu_\zeta P-Pu_\zeta Qu_\zeta^*P
\]
有准确因子分解
\[
R_hB_\zeta R_h=X_h^*X_h-Z_h^*Z_h.
\tag{I}
\]
右侧迹类，因此 \(V_hR_hB_\zeta R_h\) 迹类。HS 平方的乘法加权迹给出
\[
\begin{aligned}
\operatorname{Tr}(V_hX_h^*X_h)
 &=\int_0^\infty m(\xi)q_{1,\zeta}(\xi)\,d\xi,\\
\operatorname{Tr}(V_hZ_h^*Z_h)
 &=\int_0^\infty m(\xi)q_{2,\zeta}(\xi)\,d\xi.
\end{aligned}
\]
因而
\[
\boxed{
\operatorname{Tr}(V_hR_hB_\zeta R_h)
=\int_0^\infty m(\xi)d_\zeta(\xi)\,d\xi.
}
\tag{J}
\]
这证明了式 (17)，也证明合成后的读出对 \(h\) 复线性。

实际上还有整个正则化算子的迹范数界
\[
\|V_hR_hB_\zeta R_h\|_1
\le\frac{A_f^2}{2\pi^2}
\int_0^\infty\frac{|m(\xi)|}{1+\xi}\,d\xi.
\tag{K}
\]

当源平滑、\(B_\zeta\) 已迹类时，循环确实合法：
\[
\operatorname{Tr}(V_hR_hB_\zeta R_h)
=\operatorname{Tr}(R_hV_hR_hB_\zeta)
=\operatorname{Tr}(W_hB_\zeta).
\tag{L}
\]
在 BV 极限中，使用的是 (I)–(J)，不是继续使用 (L)。稿件没有声称极限的 \(W_hB_\zeta\) 迹类，处理正确。

定义范围上只需保持一个区分：读出可由 (E) 延拓到全部 \(L^2\) 测试；但若一般 \(h\in L^2\) 的 \(\widehat h\) 不有界，不能不加说明地继续把 \(R_h\) 当有界乘法算子。当前稿件的算子公式用于 \(C_c^\infty\) 测试，没有这个问题。

**3. 实际近锐族的共同预算与系数极限。**

稿件的 \(c_\varepsilon\) 单调上升一次、下降一次，各幅度为 \(1\)，故
\[
\|c_\varepsilon\|_\infty=1,\qquad
\operatorname{Var}c_\varepsilon=2.
\]
端点平坦保证与常值段、零延拓光滑拼接。

在一个基本区间内，过渡处的两项分别是同一角度的正弦和余弦，因此
\[
\sum_n c_\varepsilon(t-nL)^2=1.
\]
支撑包含于 \([0,L+\varepsilon_0]\)。对任一实际系数
\[
f_{g,\varepsilon}(t)=\pm c_\varepsilon(t)c_\varepsilon(t-a_g)
\]
有
\[
\|f_{g,\varepsilon}\|_1\le L+\varepsilon_0,
\]
以及 BV 乘积不等式
\[
\operatorname{Var}f_{g,\varepsilon}
\le
\|c_\varepsilon\|_\infty\operatorname{Var}(T_{a_g}c_\varepsilon)
+\|T_{a_g}c_\varepsilon\|_\infty\operatorname{Var}c_\varepsilon
\le4.
\tag{M}
\]
非零乘积要求 \(|a_g|\le L+\varepsilon_0\)，所以稿件选取的共同有限 \(F\) 有效，包括可能实际为零的端点项也无害。

记
\[
A_*:=|F|(L+\varepsilon_0+4).
\]
则 \(A_{f_\varepsilon}\le A_*\)，极限系数也满足同一预算。

此外
\[
c_\varepsilon\longrightarrow c_0=\mathbf1_{[0,L]}
\quad\text{几乎处处及在 }L^1\text{ 中}.
\]
甚至有直接估计
\[
\|c_\varepsilon-c_0\|_1\le2\varepsilon,\qquad
\|f_{g,\varepsilon}-f_{g,0}\|_1\le4\varepsilon.
\tag{N}
\]
于是
\[
\sup_\omega
|\widehat f_{g,\varepsilon}(\omega)-\widehat f_{g,0}(\omega)|
\le\|f_{g,\varepsilon}-f_{g,0}\|_1\longrightarrow0.
\tag{O}
\]

固定 \(\xi\)，(O)、有限 \(F\) 及共同核包络 (B) 给出
\[
\sup_\zeta|d_{\zeta,\varepsilon}(\xi)-d_{\zeta,0}(\xi)|
\longrightarrow0.
\]
这里先在内部负频率变量上使用可积包络
\((1+\xi-\eta)^{-2}\)。再由
\[
\sup_\zeta|d_{\zeta,\varepsilon}(\xi)-d_{\zeta,0}(\xi)|
\le\frac{A_*^2}{\pi^2(1+\xi)}
\]
及其平方可积，得到
\[
\boxed{
\int_0^\infty
\sup_\zeta|d_{\zeta,\varepsilon}(\xi)-d_{\zeta,0}(\xi)|^2\,d\xi
\longrightarrow0.
}
\tag{P}
\]
这比稿件声称的环面一致 \(L^2\) 收敛还略强。相应地，
\[
\sup_\zeta\|k_{\zeta,\varepsilon}-k_{\zeta,0}\|_2\longrightarrow0.
\tag{Q}
\]
标量读出的收敛还满足
\[
\sup_\zeta|\Psi_{h,\varepsilon}-\Psi_{h,0}^{\mathrm{reg}}|
\le\sqrt{2\pi}\,
\sup_\zeta\|d_{\zeta,\varepsilon}-d_{\zeta,0}\|_2\,\|h\|_2.
\tag{R}
\]

**4. 强伴随极限和加权迹范数极限都成立。**

各 \(f_{g,\varepsilon}\) 几乎处处收敛且一致有界，因此对每个固定向量，
\[
M_{f_{g,\varepsilon}}T_{a_g}\to M_{f_{g,0}}T_{a_g},
\qquad
T_{-a_g}M_{\overline{f_{g,\varepsilon}}}
\to T_{-a_g}M_{\overline{f_{g,0}}}
\]
均强收敛。有限相位和给出 \(u_{\zeta,\varepsilon}\) 及其伴随的强收敛；对固定向量，该收敛也对 \(\zeta\) 一致。

每个 \(u_{\zeta,\varepsilon}\) 酉。强收敛同时适用于伴随，加上统一范数界，允许通过两个乘积：
\[
u_{\zeta,0}^*u_{\zeta,0}
=\operatorname*{s-lim}_{\varepsilon\to0}
u_{\zeta,\varepsilon}^*u_{\zeta,\varepsilon}=1,
\]
另一个乘积同理。故 \(u_{\zeta,0}\) 确实酉。此处没有只有单边强收敛的问题，也不产生算子范数收敛或 Fredholm 性的推论。

固定 \(h\)，考虑 (G) 中的两个加权块。核差逐点趋零，且对 \(\zeta\) 一致；其平方之和由常数乘
\[
\frac{|m(\xi)|}{(1+\xi-\eta)^2},
\qquad \xi\ge0,\ \eta<0,
\]
控制。该函数的二重积分是
\[
\int_0^\infty\frac{|m(\xi)|}{1+\xi}\,d\xi<\infty.
\]
因此
\[
\sup_\zeta\|X_{h,\zeta,\varepsilon}-X_{h,\zeta,0}\|_2\to0,
\qquad
\sup_\zeta\|Z_{h,\zeta,\varepsilon}-Z_{h,\zeta,0}\|_2\to0.
\tag{S}
\]
再用
\[
\|X_\varepsilon^*X_\varepsilon-X_0^*X_0\|_1
\le(\|X_\varepsilon\|_2+\|X_0\|_2)\|X_\varepsilon-X_0\|_2,
\]
以及 (H) 的统一界，得
\[
\boxed{
\sup_\zeta
\|V_hR_hB_{\zeta,\varepsilon}R_h
 -V_hR_hB_{\zeta,0}R_h\|_1\longrightarrow0.
}
\tag{T}
\]
所以密度极限、平滑源读出极限及真实夹持算子的迹极限确实是同一个对象。

实系数的 Fourier 对称性仍适用于 BV 系数，因此 Haar 平均零也可以直接逐频率重证；通过 (P)–(R) 传递同样合法。

**5. §9 第二种量化界及其量词准确。**

为区分近锐参数，以下用 \(r\) 表示测试支撑尺度：
\[
h_r(s)=\psi((s+L)/r),\qquad
\|h_r\|_2=\sqrt r\,\|\psi\|_2.
\]
支撑足够小时，原周期分布取值为
\[
\mathcal P_{p,q}(h_r)=L\rho_p=:a_0>0.
\]
若某个 BV 读出在这个具体测试上满足
\[
|\Psi_{h_r}^{\mathrm{reg}}-\mathcal P_{p,q}(h_r)|
\le a_0/2,
\]
则由 (E)
\[
\frac{a_0}{2}
\le|\Psi_{h_r}^{\mathrm{reg}}|
\le\frac{\sqrt{2\pi}\,A_f^2}{2\pi^2}
      \sqrt r\,\|\psi\|_2.
\]
所以必要条件准确为
\[
\boxed{
A_f^2\ge
\frac{2\pi^2}{\sqrt{2\pi}}\,
\frac{L\rho_p}{2\sqrt r\,\|\psi\|_2}.
}
\tag{U}
\]
与式 (21) 第二个界完全一致。

统一 BV 预算还给出更一般的闭性结论：若这些读出分布收敛且 \(A_f\) 一致有界，则极限满足统一的 \(L^2\) 测试范数界，因而由 \(L^2\) 对偶性具有 \(L^2\) 密度。它不能含非零周期原子。这不需要任何未加权迹范数界。

若使用与测试函数无关的有限复参数测度 \(\mu\)，有效预算为
\[
\int A_{f,\zeta}^2\,d|\mu|(\zeta);
\]
在当前系数预算不依赖 \(\zeta\) 的情形，就是
\(A_f^2\|\mu\|_{\mathrm{TV}}\)。将此预算代替 (U) 左侧即可。

稿件对速率的限定也正确：

- 一般分布收敛到非零原子，迫使上述有效预算趋于无穷，但不给出相对于任意指定近似参数的速度。
- \(r^{-1/2}\) 的 \(A_f^2\) 下界，要求明确满足针对变化测试 \(h_r\) 的半误差条件。
- §8 的实际近锐族具有固定 \(A_*\)，因此不具备这种逃逸；即便其未加权 HS／迹范数发散，正则化读出仍强收敛于上述 \(L^2\) 密度。

可补明的定义仅有三点：BV 变差计入实线端点跳跃；式 (17) 的有界算子写法用于当前光滑测试类；参数测度在作为一个分布读出时独立于 \(h\)。这些都是现有论证的准确范围，不构成公式或结论的实质修订。
