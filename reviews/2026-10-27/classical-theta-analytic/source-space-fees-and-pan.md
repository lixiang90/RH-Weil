# Classical theta analytic源：literal域失败，空间费用与Pan消费冻结

2026-10-27；/root/ct_norm独占稿。执行STATE唯一实际K/Phi的type／零模／空间原费首门；同G20261027、原0c4f基线。已恢复Goal／C047已完成状态／D20261027N／前沿和553。本文只编辑此路径，不改STATE、cadence或Git，不预C048/585。原本拟核无限目标费用；实际literal归一化首先失域，故没有一个已经付款的Phi、H^m范数界或Pan结论。

## 1. 实际模型、原式与本次阅读

作者56页CDM.revised.pdf沿同一已库SHA47ff2ff6f5151081dd029a1df680377b88d58fc09d6629f3a2b2c3b78bab0f54。本文目视PDF21/22相关原式；文本定位PDF4–6的V/Q/B/Γ/model、PDF25/29–30的配对陈述。没有审原外部证明或§9–11。

PDF4：V={x∈B:tr x=0}，Q(x)=ν(x)=−x²；B(x,y)=(x,y)=tr(xy^ι)，ι为canonical involution，故B(x,x)=2Q(x)。B_R≃M₂(R)，签名(1,2)，w(z)=[[z,−z²],[1,−z]]。PDF5–6取maximal order O_B、Γ=O_B^×、D≃C\R、M(C)≃Γ\D，为orbifold；D(B)>1后模型proper，空间compact。正负半平面最多给两个Γ轨道组件；无需先假设Γ有negative-norm unit或M(C)连通。

PDF21 Eq5.3与Prop5.1逐字给

\[
 R_{\rm print}(x,z)=|B(x,w(z))|^2/|B(w(z),\bar w(z))|,
 \quad \varphi^0_{\infty}(x,z)=
 [4\pi(R_{\rm print}(x,z)+2Q(x))-1]e^{-2\pi R_{\rm print}(x,z)}.
\]

PDF22 Eq5.7/5.8又称B(x,x)+2R_print为majorant，称
phi∞=phi∞⁰ exp(−2πQ)为Schwartz coefficient。当前next admission沿这些literal式定义native K，而非另外给了一套不同的B/R约定。以下直接核它们不能同时成立。

## 2. 原式的全rank格点反测；division假设不能补Gaussian

先固定z=i。任意trace-zero实矩阵可唯一写成

\[
 x=\begin{pmatrix}a&u+d\\u-d&-a\end{pmatrix}.
\]

直接矩阵乘法给

\[
 Q(x)=d^2-a^2-u^2,\quad B(w(i),\overline{w(i)})=-4,
 \quad B(x,w(i))=-2(u+ia),\quad
 R_{\rm print}(x,i)=a^2+u^2.
\]

所以

\[
 B(x,x)+2R_{\rm print}(x,i)=2d^2,
\]

是rank1半正定型，非正定majorant。在τ=iv，native K的实际单项为

\[
 k_v(x,i)=
 [4\pi v(2d^2-a^2-u^2)-1]e^{-2\pi v d^2}.       \tag{1}
\]

特别不能对这项套三维Schwartz Poisson。这个失败不限split B的rational diagonal向量：实际L=O_B∩V在V_R是fullrank3 lattice。选d=0平面内非零向量y，并给V_R任意Euclidean范数。L有有限covering radius C；对每个正整数n选x_n∈L满足||x_n−ny||≤C。于是d(x_n)有界、a(x_n)²+u(x_n)²→∞，并可抽取互异子列。每个固定v>0，(1)沿此列趋于−∞，尤其单项不趋0。

这直接否定literal全格点series作为通常收敛的theta函数。更可见其正部不能抵消上述负部：正项须a²+u²<2d²，故该区域||x||²≤3d²，所有正项由固定v的多项式Gaussian可和；负部因上述互异子列无限。这里只需单项必要条件已足，不将这个补充当一种新求和定义。

对任意固定z∈D，取实B-isometry g把z移到i，R_print(x,z)=R_print(gx,i)，Q不变；gL仍是fullrank3 lattice，上述covering-radius反测逐字成立。并未把gL假称原整格，也未改变模型/level。故不能通过选择某个z、division B无rational isotropic或compact fundamental domain避开失域。

## 3. P0、空间费用及高度：当前均不能消费

冻结公式是先K，再取

\[
 P_0K=K-\operatorname{vol}_\mu(M)^{-1}\int_MK\,d\mu,
 \quad \Phi_r=\int r(t)e^{3t/4}P_0K(i e^t,\cdot)dt.
\]

literal K已不定义，因而没有其空间均值、P0K、Phi_r或可交换的格点／时间／空间积分。P0为有定义函数上的有界投影，不是自动赋予发散series一种正则化。不能把“字面x0为−1，P0杀常数”升级为双端零模或空间H^m付款。独立的termwise P0、finite-part或其他renormalized lattice求和是不同对象，其选择、尾、Γ不变性和原费用都须另给；当前反测不排所有这些修复。

因此下列目标均保持**未定义／未付款**：

* ALLcomplex物理F=S_exp、原r=e^(t/2)f_phys上的Phi源map，以及du或zero-extension Dlog全域费用；
* 固定空间H^m/C^k/Dirichlet费用、两端／全部空间导数、P0与导数／时间积分交换；
* Phi是否非零、全源coverage、全部noncompact Pan及其平移的像或下降。

compact orbifold本身只给可用的Sobolev框架，不能补上述失败。在未来真正定义的smooth源中，global mean-zero仍须与energy kernel分开：Dirichlet seminorm的核是各连通组件上的locally constant函数，形成有限维closed base B_lc；若保global mean-zero，只去掉全局常数未必去掉全部B_lc。H¹正范数或H¹/B_lc的energy completion可明确使用，不能声称当前Phi已经落在分离能量域。

源文PDF25 Eq7.6有高度系数1/2；PDF30 Eq7.24是ddcφ=(1/2)Δφ·μ，且Δφ_λ=−λφ_λ。因此若这些cited陈述适用于某个已经合法的a(φ)，高度与正Dirichlet能量的方向是负，形式上h(aφ,aψ)=−(1/4)E(φ,ψ)。这里严格定义E(φ,ψ)=−∫_M(Δφ)·barψ dμ，先按实输入再作first-linear Hermitian复化；不将它无声换成另一缩放的usual hyperbolic energy。它不是当前literal Phi的已付自然height界，也不是作者stack/index证明已审。本文没有用正能量范数代替原算术height或删除系数/sign。

## 4. 无限目标下553的正确消费条件；本次不能启用

为避免下一次把前轮finite-A推理搬错，单列一个已有标准条件规则，**不是对当前Phi的成功结论**。若另有实际T:L²(du)→H^m(M)且有限全域bound，553的实际Pan cyclic密度只给

\[
 \overline{T(\operatorname{span}_{\mathbf C}\{p_b\})}^{H^m}
 =\overline{T(F)}^{H^m}.                              \tag{2}
\]

无限维image不自动闭，不能据(2)写T(P)=T(F)。若同一个已经定义的mixed配对h对第一腿连续于H^m，且h(Tp,Tr)=0对全部p∈P、r∈F成立，取Pan组合逼近任一s∈F便有h(Ts,Tr)=0。无需image闭；无需literal Tp=0；不强迫T对象零。若只有强S_exp费用、未给这种目标连续性或没有closed base，这条条件规则不能使用。当前由于T=Phi未定义，连(2)的实际前提也未付款。

同理，未来若真能证明W(t)=e^(3t/4)P0K(i e^t,·)在L²(dt;H^m)，Cauchy–Schwarz会给||Tr||_Hm≤C_m||r||du、C_m²=∫||W(t)||²_Hm dt；Dlog费用再除sqrt(log2)。这是明确的待付判据，当前C_m并非已定义有限数。没有跨模型/level uniform费用，无源窗裁剪，更无此范数自动等于算术height的消费。

## 5. 净值、受影响依赖与下一动作意见

本轮是原式之间的标准归一化／actual-domain反测，建议来源准入0数学轮：没有建立新完整无限源或空间费用，不以source0藏一次实际成功运输，也不以单候选literal失域领取完整方法边界。553仍是旧有界门；582的实际full-local/arch源与583的独立Faber/II2,2 Green全尾均不依本PDF这组R公式，不能回滚。前轮固定holomorphic Mellin–Bergman源只用cusp/Gram/Petersson与553，亦不依此R，因此原结论保持。

受影响的是“已定位classicalK为Schwartz、只剩双端空间费用”这一当前next定义消费，以及依此欲开展的Poisson、H^m和Pan推论；应先freeze，并追加规范纠正，再重闭来源角色。独立primitive physical桥、整过滤/截面乘法/mixedRR、完整Γ/contact/properpowers/双pole、signed growth/actualq/core/coupling/Ξ及whole4/5负惯性UPPER均未改变，Goal门open。

下一最便宜的同源短门是先核负平面正交投影与单x Green规范的一致性。若定义

\[
 R_{\rm geom}(x,z)=-B(x_-,x_-)=2R_{\rm print}(x,z),
\]

则z=i有R_geom=2(a²+u²)，B(x,x)+2R_geom正定。它可成为一个**明确不同、由本项目独立定义**的条件修补，但不能默默写回作者Eq5.3并移植Th7.4/height身份。先把同一PDF的B/R/majorant/Green系数歧义闭合，比继续不存在的Phi费用或追另一paper更有信息。即使之后独立修补核合法，仍须实付Poisson/空间原费并先扣553，再判是否只有标准直接运输；不能仅因factor修补授予C048或经典正性。
