# 517. 实际有限角的相容读出与保双次数源截断

2026-10-11。[T/R/N] 接续[513](513-f1-single-prime-relative-chain-transfer.md)、
[515](515-f1-common-central-mixed-kernels.md)、
[516](516-f1-global-mixed-radical-and-mellin-jets.md)。
支付读出层的弱全局化，以及非零实际源关系的紧支逼近。
没有把这层极限称为全局HH₁链、几何主商或忠实Hilbert谱完成。

## 1. 明确共同有限目标代数

为避免每次只扩大一对角而遗漏此前来源，对有限S定义
\[
 \mathfrak A_S^\uparrow=
 \operatorname{alg}^*\bigl(
   \alpha_{T,S}(\mathfrak A_{T,0}),\ T\subseteq S,\
   \mathcal S_1(P_{0,S}\mathcal H_S)\bigr).                    \tag{1}
\]
各集合均含实位，T的有限位子集只有有限多个。
\(\alpha_{T,S}\) 是513由真实单位壳层源嵌入支付的径向角星同构。
张量嵌入复合准确相容，故 \(S\subseteq S'\) 给精确单射
\[
 \mathfrak A_S^\uparrow\longrightarrow\mathfrak A_{S'}^\uparrow,\quad
 Q_S^\uparrow\longrightarrow Q_{S'}^\uparrow.                 \tag{2}
\]
后者模去全部径向S₁；源运输保持S₁范数，故商映射单射。
单位仍是对应径向角单位，不把全空间任意压缩当精确同态。
不要求星代数范数闭合。

紧支实偶中央卷积Aζ在运输中准确交织；
514逐生成元中央性覆盖(1)全部有限字。
普通电荷Ω、中央作用及混合电荷在(2)下相容。

515给任何非零紧支η和非空有限新增素数集合F（\(F\cap S_f=\varnothing\)）：
\[
 [t_{S\cup F,\eta}]-\alpha_{S,S\cup F}[t_{S,\eta}]
                  =\sum_{\ell\in F}[t_{\ell,\eta}]\ne0.       \tag{3}
\]
显式b₂由513支付。后续有限扩大也不能使右侧变成边界：
原非零中央混合读出由(2)保持。
因此这些类不是按(2)相等的相容族；仅建立代数的并，
不会凭空给出一个无限素数链 \(t_\infty\)。

## 2. 完整Gamma项与实际Euler读出函数

固定实偶紧支η，记 \(h=e^{-t/2}\eta\)。
取515的 \(\mu_p\)，并令
\[
 a_\infty(\tau)=\log\pi-\Re\psi(\tfrac14+\tfrac{i\tau}{2}),\quad
 G_\eta(t)=\frac1{2\pi}\int
              a_\infty(\tau)\widehat\eta(\tau)e^{i\tau t}d\tau.
                                                               \tag{4}
\]
全部频率矩可积，Gη实偶光滑；(4)来自511已支付的实际实位普通迹，
含原Gamma及恒等元正规化，不另加自由常数。

实际有限S混合电荷准确写成
\[
 D_{S,\eta}(\zeta)
 =\Omega_{S,\zeta}([t_{S,\eta}])
 =\int F_{S,\eta}(t)\zeta(t)dt,
\quad
 F_{S,\eta}=G_\eta+\sum_{p\in S_f}\mu_p*\eta.                  \tag{5}
\]
所有系数、符号及1/(2π)沿用实际源公式。

若 \(\operatorname{supp}\eta\subset[-R,R]\)，固定 \(|t|\le K\)，
只有 \(n\log p\le R+K\) 可能使 \(\eta(t\pm n\log p)\) 非零。
因此
\[
 F_\eta=G_\eta+\sum_{p\ {\rm prime}}\mu_p*\eta                 \tag{6}
\]
是局部有限的光滑函数和。在任何固定紧区间，S覆盖
\(p\le e^{R+K}\) 后，F_S与F及所有导数准确相同。

由此得到 \(C^\infty_{\rm loc}\) 的最终精确稳定，
也得到强分布收敛：每个支集统一且所有导数一致有界的测试族，
在同一个有限S之后读出差同时为零。
这远强于只对一个ζ比较标量，却仍然只在电荷读出层。

(6)不宣称 \(\sum\mu_p\) 是有限测度或实轴上的可积Fourier乘子。
粗略计数全部整数已足以给
\[
 |\partial^jF_\eta(t)|\le C_{\eta,j}(1+|t|)e^{|t|/2};
\]
这里不需PNT，也不据此声称F必为tempered分布。

## 3. 同一固定测试上的完整算术值

对实偶紧支ζ，(5)在覆盖 \(R+R_\zeta\) 后准确为
\[
 D_\eta(\zeta)=2N(h*k_\zeta).                                \tag{7}
\]
这是源公式先给有限S读出、再按组合支集付款得到的完整值。
它与516的显式公式密度 \(K_h\) 相等。
固定测试族的统一支集使覆盖阈值统一；
随素数扩大的检测器不属于一个固定支集族，故515的非零检测仍成立。

没有建立保持所有HH类的拓扑完成。
514的实际边界范数下界仍排除绝对S₁尾；
(3)也仍表明普通有限同调类之间确有非零增量。
采用(6)只保留一族观测值，不能据此宣布全局谱识别或Hodge正性。

## 4. 非紧支输入只做完整标量延拓

对sharp实 \(h\in\mathcal S_{\exp}\)，定义 \(D_h(\zeta)=2N(h*k_\zeta)\)。
405的连续性支付它，516识别其共同核。
这不把非紧支卷积自动加入原511纯代数角，更不把(6)的
紧支局部有限理由套到非紧支h上。

有限S标量 \(N_S\) 同样可对这类h使用。
遗漏素数p>P的原素数项由
\[
 \sum_{p>P}\log p\sum_{n\ge1}|k(n\log p)|
 \le p_{2,0}(k)\sum_{m>P}\frac{\log m}{m^2}
 \le C\,p_{2,0}(k)\frac{1+\log P}{P},\quad P\ge2              \tag{8}
\]
控制。prime powers在整数m中无重复，
\(\log p\le\log(p^n)\)，故上界可用全部整数积分支付。
遗漏项不涉及实位常数。

对于固定h和支集/半范数有统一界的ζ族，
405卷积界统一控制 \(p_{2,0}(h*k_\zeta)\)。
所以(8)给全素数标量读出的统一收敛，但不提供统一S₁边界范数。
如果要给非紧支h真正的固定S链，须另行指定实际Bochner卷积的代数扩大；
本稿不以标量延拓替代这项准入。

## 5. 保持两个次数的实际源截断

取516真实源 \(h_0=E\theta\)、\(p=(D^2+D)h_0\)。
选实偶 \(\chi\in C_c^\infty([-2,2])\)，在[-1,1]上为1，
\(R\ge1\)、\(\chi_R(t)=\chi(t/R)\)，定义
\[
 u_R=\chi_Rh_0,\qquad p_R=(D^2+D)u_R.                        \tag{9}
\]
p_R实sharp、支集在[-2R,2R]。实偶χ保持sharp，
而 \(D(f^\sharp)=(-Df-f)^\sharp\) 使 \(D^2+D\) 与sharp交换。且
\[
 M_{p_R}(s)=s(s-1)M_{u_R}(s),\qquad
 c(p_R)=d(p_R)=0                                            \tag{10}
\]
准确成立，未用数值近似消掉次数。
p_R非零：若 \((D^2+D)u_R=0\)，紧支解 \(A+Be^{-t}\) 只能为0，
与u_R非零矛盾。未声称p_R仍属于实际像I。

展开得
\[
 p_R-p=(\chi_R-1)p+2\chi_R'h_0'+(\chi_R''+\chi_R')h_0.
\]
所有差项支集在 \(|t|\ge R\)，故
\[
 p_{N,j}(p_R-p)\le C_{\chi,j}e^{-R}
                      \sum_{k\le j+2}p_{N+1,k}(h_0).        \tag{11}
\]
因此p_R于 \(\mathcal S_{\exp}\) 收敛到实际p。
405连续性与516的 \(D_p=0,\ B(p,g)=0\) 给
\[
 \sup_{\zeta\in\mathcal B}|2N(p_R*k_\zeta)|\le C_\mathcal B e^{-R}, \tag{12}
\]
其中 \(\mathcal B\) 是任意固定支集/导数有界的实偶紧支测试族。
同样对固定g∈Cc，
\[
 \sup_{\zeta\in\mathcal B}|2B(p_R,g*k_\zeta)|
                                 \le C_{g,\mathcal B}e^{-R}. \tag{13}
\]
这些是观测误差界，不是全局链范数误差界。

## 6. 顺序不能颠倒

读出(12)的有限S覆盖需 \(p\le e^{2R+R_\mathcal B}\)；
读出(13)需 \(p\le e^{2R+R_g+R_\mathcal B}\)。
先按R及组合支集选S_R，再用(11)–(13)趋零。
不能固定S再让R无限增大并声称原算术值仍准确。

每个p_R非零且紧支，按 \(\eta_R(t)=e^{t/2}p_R(t)\) 构造515的
固定S实际链，其类非零；
516的经典不同零点输入还给其完整标量混合读出并非处处为零。
然而对每个固定有界测试族，适当覆盖后的读出一致趋于0。
这解释有限链可检测与非零实际全局源关系p标量消失为何相容。

本稿没有认证p_R为principal，也没有把观测趋零称为HH边界趋零。
下一任务是保留重数jets的真实源商及其增长约束；
独立全局Weil非正性、全零点谱识别和RH仍开放。
