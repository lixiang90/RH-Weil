# 修补K_g的原费用、无限像Pan闭包与净值

2026-10-27；/root/kg_fees独占稿。执行STATE唯一[明确修补核准入](../negative-plane-green/next-corrected-kernel-source-admission.md)，恢复Goal／D20261027P／553及原literal冻结。这里只消费项目独立R_g版本，不将结论写回原literal R/K，也不借作者Prop5.1／Th7.4／modularity当证明。不改STATE/cadence/Git，不预C048/585，不调模型/ray/level/weight/阻尼或另造source候选。出稿不代root消费；最终Poisson输入版本由root/fresh一同重闭。

## 1. 固定对象、Γ不变性及原物理源

沿同一fixed division quaternion B、V={tr x=0}、Q(x)=ν(x)、Bform(x,y)=tr(x y^ι)、L=O_B∩V、D=C\R与compact orbifold M(C)=Γ\D，Γ=O_B^×。项目明确独立

\[
 R_g(x,z)=-B_{\rm form}(\operatorname{pr}_{z,-}x,
                           \operatorname{pr}_{z,-}x),\quad
 \varphi_g^0(x,z)=[4\pi(R_g(x,z)+2Q(x))-1]e^{-2\pi R_g(x,z)},
\]
\[
 K_g(\tau,z)=\sum_{x\in L}
 \varphi_g^0(\sqrt v x,z)e^{2\pi i\tau Q(x)},
 \quad\tau=u+iv.
\]

对γ∈Γ，Adγ保L、Q与Bform，负平面投影等变；故R_g(x,γz)=R_g(γ^−1xγ,z)，实际换格点变量给K_g(τ,γz)=K_g(τ,z)。它是quotient上的scalar smooth kernel；这一步不等于算术theta的modularity或height身份。

本轮物理时间另记t，r(t)=e^(t/2)f_phys(t)，原du就是dt及L²(R,dt)。固定已给ray与框架

\[
 U(v)=P_0K_g(iv,\cdot),\quad
 P_0f=f-\operatorname{vol}_\mu(M)^{-1}\int_M f\,d\mu,
 \quad W(t)=e^{3t/4}U(e^t),
 \quad T r=\Phi^g_r=\int_{\mathbb R}r(t)W(t)dt.
\]

native K_g无额外v^(3/4)；它只出现在这个冻结的物理公式。源r按复线性进入，不取conjugate(r)，没有把模实部u偷换为物理t。

## 2. 实际零模输入如何支付空间／时间费用

配套[Poisson稿](polynomial-gaussian-poisson-and-zero-modes.md)须按实际最终版本重闭下述对象与量词：B-selfdual测度及原B Fourier使F_Bφ_g=−φ_g；large-v raw零项为−1，small-v dual零项为+Cov_B(L)^−1v^−3/2。二者都与z无关，确被同一个global P0杀掉。有限compact lifts对L及B-dual L给正定Gaussian统一下界，从而对每个固定k、ℓ，存在A_(k,ℓ)、c_(k,ℓ)>0使

\[
 \|\partial_t^\ell W(t)\|_{C^k(M)}\le
 \begin{cases}
 A_{k,\ell}e^{3t/4}e^{-c_{k,\ell}e^t},&t\ge0,\\
 A_{k,\ell}e^{-3t/4}e^{-c_{k,\ell}e^{-t}},&t\le0.
 \end{cases}                                                    \tag{1}
\]

所有固定阶导数的有限多项式v或v^−1费用均可缩小c后吸入Gaussian尾；不对k、ℓ或模型给同一数值常数。K_g是新明示版本的真实格点和，原literal失域证明保持，不能用本式替旧核补定义。

给compact orbifold选择标准smooth Sobolev空间H^m，m为非负整数；例如以原μ及非正号hyperbolic Δ定义||f||_(H^m)=||(1−Δ)^(m/2)f||_L²。P0是global常数的正交补投影，和这个spectral Δ相容，所以在此规范下为contraction。局部C^k规范也有||P0f||_Ck≤C_k||f||_Ck；正阶空间导数杀掉所减常数。**没有**使用P0与任意空间向量场D_z交换的错误等式：一般D_zP0f=D_zf，而P0D_zf另有一个均值。

有限chart和compactness使C^m尾蕴含H^m尾；因此由(1)，对每个m、ℓ、N均有

\[
 \sup_t e^{N|t|}\|\partial_t^\ell W(t)\|_{H^m}<\infty,
 \quad
 C_m^2:=\int_{\mathbb R}\|W(t)\|_{H^m}^2dt<\infty.       \tag{2}
\]

同样C^k值的L²(dt)费用D_k²=∫||W(t)||_Ck²dt有限。空间均值／有限chart导数／时间积分的交换将在下节由这些实际绝对可积majorants支付，不凭compact M自动跳过全部尾。

## 3. 全域du、zero-extension Dlog及强源费用

对任意r∈L²(R,dt)，(2)及Cauchy–Schwarz给

\[
 \int|r(t)|\|W(t)\|_{H^m}dt\le C_m\|r\|_{du},
 \qquad
 \boxed{\|Tr\|_{H^m}\le C_m\|r\|_{du}.}                \tag{3}
\]

故对每个m，该积分为H^m值的Bochner积分；各m所得元素在连续嵌入下相容，是同一个distribution。交集⋂_mH^m=C∞，所以这同一个T在**整个原L²du**上取smooth值，并对每个H^m半范数有界。也可直接用D_k得到||Tr||_Ck≤D_k||r||du。不是只在compact测试源或单个window上的定义。

对任意固定阶空间微分算子，取足够高m后可穿过H^m→H^(m−k)连续映射；点值及C^k交换由相应D_k绝对可积majorant给出。均值是L²(M)连续泛函，故∫_MTr dμ=0。所有noncompact S_exp源及405实际Pan、全部平移和有限复线性组合仍在域内，没有crop关系。

原Plancherel下zero-extension Dlog满足

\[
 \|r\|_{D_{\log}}^2=
 \frac1{2\pi}\int\log(2+|\xi|)|\widehat r(\xi)|^2d\xi
 \ge\log2\,\|r\|_{du}^2.
\]

因此(3)给||Tr||_Hm≤C_m/√log2·||r||_Dlog。对S_exp强半范数p_(N,0)(r)=sup_t e^(N|t|)|r(t)|，N>0，∫e^(−2N|t|)dt=1/N，故

\[
 \|Tr\|_{H^m}\le\frac{C_m}{\sqrt N}p_{N,0}(r).          \tag{4}
\]

这些是充分upper，不是sharp operator norm／necessary lower；C_m依fixed B/L、空间规范和m。由于(3)本来全域成立，同一C_m同时控制全部compact源窗，但没有跨模型/level/cofinal family统一费用。physical f的原weighted费用仍为∫e^t|f_phys|²dt=||r||du²；未将强源、height或Petersson norm冒称同一费用。

## 4. 实结构、components与能量closed base

对real x，w(barz)=barw(z)及Bform实系数给R_g(x,barz)=R_g(x,z)，所以K_g(τ,barz)=K_g(τ,z)。在ray τ=iv，实际各项、P0K及W都是实函数。canonical conjugation c:z↦barz与real Γ作用交换，故在Γ\D下降。

这也与原模型的真实F∞一致：按已恢复PDF5的period描述λ_z(b)=b(z,1)^T，b为real矩阵，overline(λ_z(O_B))=λ_barz(O_B)，于是conjugate torus A_z=C²/λ_z(O_B)正是A_barz，O_B作用一同保留。不是凭一个formal function随意指定arith real structure。

μ作为**positive volume measure**在c下保体积；作为定向2-form，anti-holomorphic pullback则有c*μ=−μ，二者不能混说。正体积测度下P0与c相容；real r给real、F∞不变的Tr，complex r按这个实空间的复化得到。因而在原cited算术Chow定义范围内，a(Tr)=(0,Tr)是可解释的smooth metric类；这不是作者Th7.4或classicWeil身份。

M=Γ\D最多两个组件：若Γ交换D±，quotient连通；否则两半平面分别给两个组件，c给它们保正体积同构。由于K_g(cz)=K_g(z)，两组件的体积和K积分分别相等，组件均值一致；本**实际源**的global P0遂使每个组件均值为0。这个额外结论来自当前模型的对称性，不能泛称任意global mean-zero函数自动逐组件均值零。

无论是否使用该额外对称性，分离能量域均可明确为H¹(M)/B_lc，其中B_lc是各组件locally constant函数的有限维closed空间。取原Δ、μ的

\[
 E(\phi,\psi)=-\int_M(\Delta\phi)\overline\psi\,d\mu,
 \quad E(\phi,\phi)=\int_M|\nabla_h\phi|^2d\mu,
\]

先在smooth实输入上定义再作first-linear Hermitian复化；它连续延至H¹，正半定，核为B_lc。这个E范数与别的“usual energy”数值缩放不混用。compact orbifold的Poincaré不等式使能量在组件均值零子空间或H¹/B_lc上为分离Hilbert norm。(3)的m=1费用支付相应连续性。

前轮已定位的PDF25 Eq7.6与PDF30 Eq7.24若按其cited Arakelov前提应用于这些合法a(φ)，给h(aφ,aψ)=−E(φ,ψ)/4；half、negative sign及原Δ/μ保持。没有在此重证外部stack/index或将正E叫作原算术height。本门的新计算是smooth source／原费，原height陈述仍为cited依赖。

## 5. 扣553：无限像只先闭包同一，连续mixed必退化

令F=S_exp,C，P为405真实physical Pan关系的complexification；553已付P中实际p_b的有限复span在原L²du稠密。给任意r∈L²，取q_n为这些有限Pan组合、q_n→r于L²。对每个m，(3)给

\[
 \|Tq_n-Tr\|_{H^m}\le C_m\|q_n-r\|_{du}\to0.          \tag{5}
\]

因此在每个H^m中，closure(TP)=closure(TF)=closure(T(L²))。同一逼近序列(5)对全部m分别成立，故在C∞ Fréchet拓扑中也有同一闭包等式。**不**推出TP=TF：无限维像可能不闭；也未说P在原S_exp强拓扑稠密。

设β为源像上一个固定sesquilinear配对，且对每个固定r∈F，φ↦β(φ,Tr)在所用目标H^m或C∞拓扑连续。若它把全部Pan放在mixed根，即β(Tp,Tr)=0对所有p∈P、r∈F成立，则由(5)直接得到β(Ts,Tr)=0对所有s,r∈F。无需literal Tp=0、ker T=P或exact同像；目标对象可非零而配对全退化。

上述E及cited metric height拉回实际满足H¹连续性，所以它们不能同时兼容全部Pan mixed根，又精确识别537已付的完整Qζ正非根。这个否定只在提出了**同一完整Weil配对身份**时使用；本项目没有由K_g构造该身份，也没有删除Γ/contact、properpowers或双pole。

若强要求T本身在H¹/B_lc消全部Pan，(3)与553使quotient map全零；这是更窄literal下降条件。另若使用同一T数据的continuous后处理到Hausdorff／closed-point目标，并把全部Pan送同一base，(5)迫它在源像常值；无连续性、非闭base或另带T以外源数据不在此结论内。

一个条件旁注仍限于同一全部global F：若G(r,s)=g(Tr,Ts)是PSD、g在相应目标拓扑连续且G(r,r)≤Qζ(r)，则Pan上G=0，PSD Cauchy–Schwarz使其为mixed根，(5)迫G全零。这个旁注不付Qζ≥0，也不排fixed-window、变域、signed误差或非逐层Pan的lower策略。

## 6. 净值和停止范围

本轮真实支付了这个**独立修补K_g**的smooth/F∞源与全globaldu/H^m/C^k/能量费用；其数学输入是明确polynomialGaussian、标准Poisson/compact lifts及Cauchy–Schwarz。Pan后果又被553既有密度与continuity直接蕴含。因此按**标准actual-source／强旧准入0数学轮**保存，不把一个新的公式或完整费用写成新的经典whole／primitive定理，也不以0轮藏掉上述已付运输范围。

停止本fixed scalar analytic metric recipe；不再调ray/B/level/weight/阻尼或跑probe。它不提供independent primitive整模型、截面乘法／mixedRR、完整classic signed/growth/actualq/core/coupling/Ξ；最强旧542+555→557 whole leading4/5仍是负惯性UPPER。原literal失域及其所有未重闭定理运输保持冻结，局部R_g与这里直接定义的scalar源不自动继承作者7.4/modularity/算术整体theta。

没有证明T是否非零，也无需该非零性才能排除上述exact relation-compatible Gram身份。别的有费unbounded／强源map、真正变化source domain、额外relative/source-adaptive数据、或不逐层消Pan的独立正D′逼近仍未被排除；它们需实际定义和净比较，不由名称自动准入。本稿不提出下一source或新合同，也不完成长期Goal。
