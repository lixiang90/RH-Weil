# 423. 扭曲径向读出、不变性异常与实际混合周期见证

2026-10-04。[限定范围全文独立复核通过] 接续[422](422-f1-radial-finite-part-and-corner-anomaly.md)及[扭曲读出任务](../reviews/2026-09-21/f1-twisted-relative-periodic-readout-next-proof-plan.md)。
本稿在同一实际代数中完成该候选的准入和检验：非零时间确实可读出，但朴素扭曲循环性失败，且原源出现与原周期分布不相符的混合原子。
下述都是指定机制的结构与障碍，没有证明全局主除子、RR或RH；也不宣称这些经典迹障碍具有文献上的首创性。

## 1. 固定定义域与插入算子

使用422的 \(\mathcal A,\mathcal I,\mathcal M,\tau\)，及419的分离径向乘子 \(z_g\otimes1\)。
令 \(\gamma=(r,s)\in\mathbb Z^2\)，
\[
 W_\gamma=z_{-\gamma}\otimes1,\qquad
 \sigma_\gamma=\operatorname{Ad}W_\gamma,\qquad
 \tau_\gamma(F)=\operatorname{Tr}_t\lambda_{pq}(F_\gamma).
                                                               \tag{1}
\]
它们是新时间交叉积中的实际乘子与自同构，不能倒称为原 \(M(A)\) 中的径向乘子。
422的平移二次界给 \(\sigma_\gamma\) 及 \(\sigma_\gamma^{-1}\) 在各Fréchet范数上的连续性，并保 \(\mathcal I\)。
右乘 \(W_\gamma\) 只改群标签，故
\[
 \tau_\gamma(F)=\tau(FW_\gamma),\quad
 |\tau_\gamma(F)|\le p_0(F),\quad
 F\in\mathcal I\Longrightarrow
 \tau_\gamma(F)=\operatorname{Tr}(FW_\gamma).                    \tag{2}
\]
对一般 \(F\in\mathcal A\)，最后一个普通无穷迹不一定存在；第一式的有限部却有定义。

## 2. 全部边与角点的不变性异常

\(\sigma_\gamma(F)_\gamma=\beta_{-\gamma}(F_\gamma)\)。把422(7)用于S₁值系数再取时间迹，得
\[
 \Delta_\gamma\tau_\gamma(F):=
 \tau_\gamma(\sigma_\gamma F)-\tau_\gamma(F)
 =r\operatorname{Tr}_t e_p(F_\gamma)
  +s\operatorname{Tr}_t e_q(F_\gamma)
  +rs\operatorname{Tr}_t(F_\gamma)_c.                            \tag{3}
\]
此泛函连续，且在 \(\mathcal I\) 上为0，故是实际边界数据。
例如时间秩一投影 \(P\) 满足 \(\operatorname{Tr}P=1\)。
当 \(\gamma=(1,0)\)，取
\(F=H(j)\mathbf1_{k=0}z_\gamma\otimes P\)，则
\(\tau_\gamma(F)=0\)，\(\tau_\gamma(\sigma_\gamma F)=1\)。
当 \(r\ne0\) 时同一边函数给差r；当r=0、s≠0时改取 \(\mathbf1_{j=0}H(k)\) 给差s。
所以每个非零标签都缺少所需不变性。
改格点扣除起点只增加边与角泛函，不能消去(3)中固定的两个边系数。

## 3. 带插入交换异常与正确的Hochschild约定

先定义准确的实际读出
\[
 D_\gamma(A,B)=\tau_\gamma(AB-B\sigma_\gamma(A))
             =\tau([A,BW_\gamma]).                             \tag{4}
\]
单项 \(A=fz_g,B=vz_h\) 的贡献仅在g+h=γ时非零。
写g=(a,b)、\(k=\operatorname{Tr}_t(f\beta_g(v))\)，则
\[
 D_\gamma(A,B)=-ae_p(k)-be_q(k)-abk_c.                          \tag{5}
\]
422的乘法界保证一般群和绝对收敛。
任一因子在 \(\mathcal I\) 时，(4)是一个迹类算子与有界算子的普通迹交换子，因此为0。
故Dγ确实下降到 \(\mathcal A/\mathcal I\)，但这不自动使它循环。

直接展开给
\[
 D_\gamma(A,B)+D_\gamma(B,\sigma_\gamma A)
                    =-\Delta_\gamma\tau_\gamma(AB).            \tag{6}
\]
并且 \(D(AB,C)-D(A,BC)-D(B,C\sigma A)=0\)。
后一个等式不能被误写成标准扭曲循环复形的Hochschild闭性。
为明确方向，置 \(\alpha=\sigma_\gamma^{-1}\)，采用
\[
 (b_\alpha\psi)(A,B,C)=\psi(AB,C)-\psi(A,BC)
                            +\psi(\alpha(C)A,B).
\]
则
\[
 b_\alpha D_\gamma(A,B,C)
       =-\Delta_\gamma\tau_\gamma(\alpha(C)AB).                 \tag{7}
\]
真正的Hochschild边界是
\[
 E_\gamma(A,B):=(b_\alpha\tau_\gamma)(A,B)
  =\tau_\gamma(AB-\alpha(B)A)
  =D_\gamma(A,B)+\Delta_\gamma\tau_\gamma(\alpha(B)A).          \tag{8}
\]
结合律及 \(\alpha(BC)=\alpha(B)\alpha(C)\) 直接给 \(b_\alpha E_\gamma=0\)。
其在任一开放理想因子上为0，亦可下降边界。
这给一项准确的代数修复，但还没有给不变、循环的相对链或算术配对。
不能把不同γ的不同扭曲直接相加为一个普通循环余圈。

## 4. 任意标签的标量扭曲迹扩张均有有限秩障碍

这比证明某个选定有限部不循环更强。令e=(1,0)，\(s(j,k)=H(j)\mathbf1_{k=0}\)，取
\[
 A=s z_e\otimes P,\qquad B=s z_{\gamma-e}\otimes P.
\]
二者都在 \(\mathcal A\)。点态计数给
\[
 s\beta_e(s)=H(j-1)\mathbf1_{k=0},\quad
 s\beta_{-e}(s)=H(j)\mathbf1_{k=0}.
\]
因此
\[
 (AB-B\sigma_\gamma(A))W_\gamma
       =[A,BW_\gamma]=-\mathbf1_{(j,k)=(0,0)}\otimes P,\qquad
 D_\gamma(A,B)=-1.                                             \tag{9}
\]
特别地 \(AB-B\sigma_\gamma(A)\in\mathcal I\)。
不存在任何线性泛函φ同时满足
\(\varphi(I)=\operatorname{Tr}(IW_\gamma)\) 对全部I∈𝓘，及
\(\varphi(AB)=\varphi(B\sigma_\gamma A)\) 对全部A,B∈𝓐。
否则同一实际有限秩算子被赋值为−1和0。此证明对所有γ，包括γ=0，成立；甚至不要求φ连续。
它不排除显式保留(3)、(5)的相对或更高链机制。

## 5. 原源与提升的扭曲准入

令 \(\ell_g=g_1L+g_2M\)，沿用422的原有限源
\[
 u=1+\sum_g f_g(t)P_g,
 \quad f_{(n,0)}=-c(t)c(t-nL),
 \quad f_{(n,1)}=c(t)c(t-nL-M).
\]
取 \(b_g=\mathbf1_{g=0}+f_g\)，以及
\(q_g(j,k)=H(j-\max(0,g_1))H(k-\max(0,g_2))\)。
则原提升 \(T=1+\sum_g q_g z_g\otimes M_{f_g}\mathsf T_{\ell_g}\in\mathcal M\)。
因为u的径向系数恒为1，\(\sigma_\gamma(u)=u\)。然而
\[
 \sigma_\gamma(T)-T=
 \sum_g(\beta_{-\gamma}q_g-q_g)z_g
                       \otimes M_{f_g}\mathsf T_{\ell_g}.       \tag{10}
\]
非零γ时零标签已有 \((\beta_{-\gamma}Q-Q)\otimes M_{-c^2}\ne0\)。
该差在双∞角点消失，却一般保留边条带；它不是开放理想中的已消失误差。
因而 \(T^*\otimes TK_h\) 不能仅凭u不变就认作合法的扭曲循环源链。

## 6. 实际源的非零时间公式，保留全部交叉项和单位

取实 \(d\in C_c^\infty(\mathbb R)\)，\(K_h=Q\otimes M_dU(h)M_d\)。
其与T的乘积均在422定义域内，所以(4)可准确计算，即使尚无循环链解释。
对g≠0，令
\[
 r_i(g,\gamma)=\max(0,g_i,\gamma_i),\qquad
 C_\gamma(g)=g_1r_2+g_2r_1-g_1g_2,
\]
\[
 J_\gamma(g)=\int\overline{f_{-g}(x)}\,b_{\gamma-g}(x)
                   d(x-\ell_{\gamma-g})d(x+\ell_g)\,dx.
\]
则
\[
 \boxed{D_\gamma(T^*,TK_h)=
             h(-\ell_\gamma)\sum_{g\ne0}C_\gamma(g)J_\gamma(g).} \tag{11}
\]
证明：径向乘积 \(q_g\beta_g(q_{\gamma-g})\) 的两个阈值恰为r₁、r₂；代入(5)给Cγ。
时间乘积的总平移为ℓγ；其对角核给 \(h(-\ell_\gamma)\)，再以x=t−ℓg换元给Jγ。
迹类性由422(18)及乘子的有界性保证，不能对两个裸时间乘子自由循环。
g=0的径向异常恒为0；\(\gamma-g=0\) 的独立单位由b₀完整保留。
γ=0时(11)准确退回422(23)，不是人为替换h(0)。
固定c的非零群标签只有有限个，故(11)仅在包含0的源标签集合的差集上可能非零。
全γ求和在此实际源上是有限和；尚未由它产生原迹的几何壳层权重。

## 7. 实际混合原子严格为正，而原周期分布在此为零

γ=(a,1)时只有g₂=0贡献，变元换回y后(11)的系数简化为
\[
 m_c(y)=\sum_{n\in\mathbb Z}n c(y+nL)^2,
\quad
 D_{(a,1)}(T^*,TK_h)=h(-aL-M)
 \int m_c(y)c(y)c(y-aL-M)d(y)d(y-aL-M)\,dy.                    \tag{12}
\]
在每个紧y区间和有限，来自原源而非自由指定权重。

取421§8的合法近锐 \(c_\varepsilon\)：在(0,ε)为sin(πθ(y/ε)/2)，在[ε,L]为1，
在(L,L+ε)为cos(πθ((y−L)/ε)/2)，并满足 \(\sum_n c_\varepsilon(y+nL)^2=1\)。
选择θ在内部严格递增。p≠q为素数，M/L无理；令
\[
 a=-\lceil M/L\rceil,\quad \delta=-aL-M\in(0,L),\quad
 0<\varepsilon<\min(\delta,L-\delta).
\]
取非空小区间I⊂(0,ε)，实非负光滑d支撑在 \(I\cup(I+\delta)\)，且在相应更小区间严格为正。
积分中只有y∈I贡献，且
\[
 m_c(y)=c_\varepsilon(y+L)^2>0,\quad
 c_\varepsilon(y)>0,\quad c_\varepsilon(y+\delta)=1.
\]
因此h(δ)=1时(12)严格为正。
γ是真混合标签，δ不是任何非零整数p或q周期；否则给素数间的非平凡整数幂等式。
取h紧支于δ附近并避开0与两条轴周期集合。
422(20)的原周期算子却满足
\[
                 \tfrac12\operatorname{Tr}A_N(h)=0
                 \quad\hbox{对每个固定N}.                    \tag{13}
\]
所以恢复非零时间不等于恢复正确算术权重：此同源混合见证直接排除把(11)作为原周期分布的逐标签比较。
它还随c、d改变。固定源的有限标签支撑亦不能给原两轴无限多个素数幂原子。
还可以准确核验(8)的原始修复数值，不能把D的源式直接当成E的源式。
在同一γ=(a,1)、双峰d选择下，若d在两峰取相同非负函数η的平移，则
\[
 E_\gamma(T^*,TK_h)=h(\delta)\int_I c_\varepsilon(y)c_\varepsilon(y+\delta)
       2c_\varepsilon(y+L)^2
                         \eta(y)^2\,dy>0.                     \tag{13a}
\]
证明保留g=0：T*的独立单位与TK_h的γ标签给系数−2a；其f₀交叉项的双有限部差也是−2a。
准确地，第二乘积的Q也必须被群乘法平移：
\(\beta_\gamma(q_\gamma)\beta_\gamma(Q)=\beta_\gamma(q_\gamma)\)。
因此这两项合为 \(-2a(1-c_\varepsilon(y)^2)\)，不能遗漏f₀或将第二Q误置在原点。
对其余可能的g=(x,0)，AB阈值为 \((\max(0,x),1)\)，
\(\sigma^{-1}(B)A\)阈值为 \((a+\max(0,-x),2)\)，
两有限部之差为 \(\max(0,x)-2a-2\max(0,-x)\)。
换元y=t+xL后，近锐下过渡只有x=−1贡献，系数与p方向源的负号合给
\((2a+2)c_\varepsilon(y+L)^2\)。与上述零标签项相加，利用
\(c_\varepsilon(y)^2+c_\varepsilon(y+L)^2=1\)，即为(13a)。
因此(13a)严格为正，并在这个下过渡测试上准确等于2Dγ。故裸E的实际源数值也不能直接识别为原周期分布。
零标签抵消还有一个必要检验：取很短的 \(I\Subset(\varepsilon,L-\delta)\)，
\(d(y)=\eta(y)+\eta(y-\delta)\)，使两峰都在cε=1的平台内，且I与I+δ不交。
此时Dγ=0，Eγ的全部非零g源项也为0，g=0的独立单位和f₀项准确抵消：
\[
                  E_\gamma(T^*,TK_h)=0.                       \tag{13b}
\]
固定I、d及足够小ε₀后，对全部0<ε≤ε₀均成立。不能从下过渡正性宣称平台正性，
也没有在这里证明混合正见证对固定d的ε→0极限保持非零。
这仍未否定携带全部边条带、角点、链修正的完整相对机制；(8)的Hochschild闭性也保持正确。

## 8. 原开放算术算子上的扭曲交换异常仍为零

422已单独证明 \(A_N(h)\in\mathcal I\)。对B∈𝓜，
\[
 D_\gamma(B,A_N(h))
   =\tau([B,A_N(h)W_\gamma])
   =\operatorname{Tr}[B,A_N(h)W_\gamma]=0.                     \tag{14}
\]
这个等式保留全部γ、完整混合项、N依赖及两个半迹归一化：零交换异常没有可调整的归一化因素。
\(\tau_\gamma(A_N(h))\) 本身可非零，它是带径向插入的普通迹，不能与(14)混同。
所以仅重插原截止不能把边界异常变成原周期迹的补偿。

## 9. 本轮结算与下一项必须支付的比较

本轮完成：(1)实际定义域；(3)全部不变性异常；(5)边角交换式；(8)正确Hochschild修复；
(9)任意标签有限秩扩张障碍；(11)实际源的完整非零时间读出；(12)–(13a)原读出及裸Hochschild修复的混合原子不相容；(14)原截止上的全标签消失。
停止把朴素标量扭曲迹、裸(11)或裸E的源数值当成算术主补偿。
下一有限问题是把(3)、(5)、(8)、(10)组织成合法的边／角相对链，并计算其原源及截止极限。
必须证明或反驳分割独立、混合项消去，以及与完整原周期分布的同源比较。
尤其(14)对每个固定N为0；任何非零极限贡献必须明确指出哪项定义域／连续性在N→∞失去一致性，并给实际界。
没有这条比较，就仍未推进G5主根空间和G6固定Weil配对的联合准入，不能直接进入RR正性结算。

## 10. 核验范围与原始来源

[精确格点脚本](../scripts/twisted_radial_witness_audit.py)直接从实际格点余项取有限部，
另核100项不变性式、625项单项交换异常、81个标签有限秩见证；
另从实际乘积独立核验600项非零源标签的修复阈值及50项零标签单位／f₀交叉项；
[结果](../reviews/2026-10-04/f1-twisted-radial-witness-audit.json)均为精确整数。
任意标签的(9)由正文证明，有限网格不替代该证明；无穷算子与混合正性也不由此脚本认证。

[TwistedRadialWitness.lean](../formal/F1/Analysis/TwistedRadialWitness.lean)
直接形式证明(9)中的一维／二维点态有限秩系数及任意γ的两个乘积标签。
[四项Lean核验](../formal/checks/twisted-radial-witness-verification.json)在固定4.32.2通过，
仅依赖propext、Quot.sound，无sorryAx；不认证无穷迹、循环理论或RH。
该模块只需Lean核心库，避免把已有mathlib缓存的机器路径当作新的分析前提。

扭曲复形约定核对Rennie–Sitarz–Yamashita作者稿
[Twisted cyclic cohomology and modular Fredholm modules](https://rennieillawarramath.com/website-pdfs/JournalArticles/2013RSY-Prepub.pdf)，Definition 2.1（PDF第2页）；
不能省略不变性再套用循环配对。Weil/RR背景参照
[Connes–Consani 2018](https://arxiv.org/abs/1805.10501)的实际复提升构造，及
[2020单实位工作](https://arxiv.org/abs/2006.13771)的半局部范围；本稿没有把这些原文当作数域全局正性证明。
[独立推导](../reviews/2026-10-04/f1-twisted-research-derivation.md)及
[最终全文复核](../reviews/2026-10-04/f1-twisted-radial-independent-review.md)保存了源公式、标准扭曲方向及混合见证的核验。
复核抓到并修正了g=0右侧Q漏平移：下过渡E=2D>0，平台E=D=0；错误的平台正见证已撤销。
限定PASS仅覆盖本稿实际构造与障碍，不认证全局主关系、RR或RH。
