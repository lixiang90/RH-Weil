# Raw mean与bounded T：实际Pan的联合闭包和连续mixed范围

2026-10-28（承接10-27已指定准入；路径沿本任务）。/root/rm_joint独占稿。恢复Goal／STATE／D20261027Q及[唯一raw mean首门](../corrected-theta-source/next-raw-mean-joint-source-admission.md)。只消费同一明确R_g/K_g的已有数据；不调模型/ray/weight/阻尼，不改STATE/cadence/Git，不预C048/585或下一source。出稿不代root消费；mean原稿与本稿须按实际终版重闭。

## 1. 对象、原norm与实际mean前件

令F=S_exp,C，物理r=e^(t/2)f_phys。P是405实际physical Pan关系的complexification，包含同一非零

\[
 p=(D^2-1/4)H,\qquad p_b(t)=p(t-b),\quad b\in\mathbf R,
\]

及全部有限复线性组合，H>0沿405原件。不是按本读出kernel重新命名的几何principal像，也不将p_b裁成compact源。553已付

\[
 \overline{\operatorname{span}_{\mathbf C}\{p_b\}}^{L^2(du)}
 =L^2(du),\qquad \|p_b\|_{du}=\|p\|_{du}.
 \tag{1}
\]

记上一门已经实付的smooth源为T:F→C∞(M)，它在整个原L²du延拓，且每个m≥0有

\[
 \|Tr\|_{H^m}\le C_m\|r\|_{du}.
 \tag{2}
\]

空间均值为零，实际模型的共轭对称性还给逐组件均值零；不由一般global mean-zero自动推出。T及原du/Dlog/C∞费用、F∞和component范围只沿[已闭费用稿](../corrected-theta-source/original-fees-infinite-pan-and-net.md)消费。

沿同一raw K_g定义m(t)=e^(3t/4)average_M K_g(i e^t)、ℓ(r)=∫r(t)m(t)dt，并令

\[
 S r=(\ell(r),Tr),\qquad R_{\rm raw}r=Tr+\ell(r)\mathbf1.
 \tag{3}
\]

本稿需要[mean原稿](mean-strong-fees-and-actual-pan.md)按实际版本支付：ℓ在全F的强域有定义/连续，且对α=3/4、c_L=Cov_B(L)>0有精确分解

\[
 m(t)=-e^{\alpha t}+c_L^{-1}e^{-\alpha t}+\nu(t),
 \quad\nu\in L^2(du),
 \tag{4}
\]

以及actual Pan读出

\[
 \ell(p_b)=-A_+e^{\alpha b}
           +c_L^{-1}A_-e^{-\alpha b}+o(1),
 \quad A_\pm=(\alpha^2-1/4)\int H(t)e^{\pm\alpha t}dt>0.
 \tag{5}
\]

(4)来自已付raw两端零模取消后剩下的L²项，不是任意另加补偿核；(5)的bounded remainder是ν与p_b的L²平移配对，趋0所需的弱平移论证由mean稿付款。下面只需b→+∞时|ℓ(p_b)|→∞；不需知道T是否非零、是否有闭像或实际无限rank。±3/4不是classic physical双pole ±1/2，不能偷换其角色。

## 2. 归一化actual关系给真正的竖直极限

由(5)，全部充分大的正b均有ℓ(p_b)≠0。取

\[
 h_b=\frac{p_b}{\ell(p_b)}\in P.
\]

则

\[
 \ell(h_b)=1,\qquad
 \|h_b\|_{du}=\frac{\|p\|_{du}}{|\ell(p_b)|}\longrightarrow0.
 \tag{6}
\]

因此由(2)，对每个固定m有||Th_b||_Hm→0，并同时在C∞ Fréchet拓扑中趋0，故

\[
 S h_b\longrightarrow(1,0).
 \tag{7}
\]

每个h_b均为原强域内的actual Pan；没有将极限(1,0)宣称为某个真实r=0的非零对象像，也没有说h_b在原S_exp强拓扑趋0。这里是指定目标拓扑中的闭包论证。仅从一个ℓ(p_b)非零不能得到(7)；必要新增信息是读出发散，而原du范数及T费用不随平移增长。

## 3. 更短的图闭包证明：先在C×L²构造actual Pan逼近

可在T之前核清全部联合信息。给任意g∈L²(du)及z∈C，由(1)取q_n为有限Pan组合，使q_n→g于L²。ℓ(q_n)可能无界，所以不能直接宣布S q_n收敛。

按(6)选充分大的b_n，使

\[
 |z-\ell(q_n)|\,\|h_{b_n}\|_{du}\le1/n.
\]

若差为0可任取合法b_n。令

\[
 q'_n=q_n+(z-\ell(q_n))h_{b_n}\in P.
\]

则每个n都**精确**满足ℓ(q'_n)=z，同时

\[
 \|q'_n-g\|_{du}
 \le\|q_n-g\|_{du}+1/n\longrightarrow0.
 \tag{8}
\]

所以得到的是明确的图闭包恒等式

\[
 \boxed{
 \overline{\{(\ell(p),p):p\in P\}}^{\mathbf C\times L^2}
 =\mathbf C\times L^2.}
 \tag{9}
\]

P中的同一个actual序列既修正了标量坐标，又保原L²极限。它不是对每个空间阶分别选一个不相容序列，更不依赖有限维像闭性。强域费用可沿n发散，未付款uniform S_exp强费。

## 4. 投到实际joint目标：只闭包同一，绝非exact同像

令

\[
 E_m=\overline{T(F)}^{H^m}
     =\overline{T(L^2)}^{H^m},\qquad
 E_\infty=\overline{T(F)}^{C^\infty}
          =\overline{T(L^2)}^{C^\infty}.
\]

右侧等式已由(1)/(2)的同一逼近序列支付。将(8)用于连续map(z,r)↦(z,Tr)，每个m有S q'_n→(z,Tg)。同一(8)和每个C_m分别成立，又给C∞收敛。再取相应闭包，得到

\[
 \boxed{
 \overline{S(P)}^{\mathbf C\times H^m}
 =\overline{S(F)}^{\mathbf C\times H^m}
 =\mathbf C\times E_m,}
 \tag{10}
\]
\[
 \boxed{
 \overline{S(P)}^{\mathbf C\times C^\infty}
 =\overline{S(F)}^{\mathbf C\times C^\infty}
 =\mathbf C\times E_\infty.}
 \tag{11}
\]

反向包含只用S(F)⊂C×E及E闭。这不证明S(P)=S(F)、S(F)=C×T(F)，也不判T的kernel/rank。584的fixed finite B(P)=B(F)不能拿来替代这里的图逼近与无限目标闭包。

对actual raw smooth函数也可等价表述：T(F)在global mean-zero闭子空间中，E_m及E∞亦然。map(z,u)↦u+z1在C×E中是到C1⊕E的拓扑同构，逆由positive volume average及P0给出。于是

\[
 \overline{R_{\rm raw}(P)}^{H^m}
 =\overline{R_{\rm raw}(F)}^{H^m}=\mathbf C\mathbf1\oplus E_m,
 \tag{12}
\]

并有C∞版本。这里空间常数的独立极限来自(7)，不是新的算术cycle或经典pole坐标。

## 5. 连续mixed与连续下降的准确后果

令V=S(F)，在C×Hm或C×C∞子空间拓扑中给一个固定sesquilinear配对β。只要求：对每个固定r∈F，x↦β(x,Sr)在V上连续。若全部actual Pan成为mixed根，

\[
 \beta(Sp,Sr)=0\quad(\forall p\in P,\ r\in F),
\]

对s∈F在(8)取g=s、z=ℓ(s)，实际q'_n∈P满足S q'_n→S s；因而

\[
 \boxed{\beta(Ss,Sr)=0\quad(\forall s,r\in F).}
 \tag{13}
\]

β只在实际源像V定义亦足够；不需要把它免费延拓到整个闭包。无需literal Sp=0、ker S=P、image closed或S非零。若某个完整经典Weil Gram身份声称通过该同一连续joint数据，则405使Pan mixed根，(13)迫拉回全零，与537已付的正非根冲突；此处未构造该经典身份，也未删Γ/contact/properpowers/双pole。

同理，对仅依同一V数据的continuous后处理G:V→Y，若G(Sp)=y0对**全部**p∈P成立且{y0}在Y闭，则上面的实际逼近给G(Sr)=y0对全部r。Hausdorff目标足够；只逐个孤立p_b测试、无连续性、非闭base或带V以外的源数据不能由此消费。closed-point责任不能因旧583未限定continuous短语而遗忘。

若另外给global同F的PSD continuous pullback G(r,s)=g(Sr,Ss)且G(r,r)≤Qζ(r)，则Pan上G=0，PSD Cauchy–Schwarz使mixed项零，再按(13)得整G=0。这仅限该同一全域continuous表式；不证明Qζ≥0，不排fixed-window/变域/signed误差或不逐层消Pan的lower方案。

## 6. natural metric配对早已忽略常数，须先扣强旧

当前raw函数只是T r加空间常数。按前门的原Δ、μ定义E(φ,ψ)=−∫Δφ·barψ dμ，常数在两腿均为根，因此

\[
 E(R_{\rm raw}r,R_{\rm raw}s)=E(Tr,Ts).
 \tag{14}
\]

cited metric height为−E/4，也有同一等式。这个特殊height不需要新增图闭包即可看出恢复mean不能修复当前metric recipe，不能将(14)算为新的正号／耦合结果。

常数metric类本身未被说成算术Chow中的零；它可与其他具有非零degree的算术类配对。这里仅消费源像由pure metric函数组成时的限制，以及(13)对任何实际continuous joint comparison的条件后果。未给额外divisor/cycle legs的完整Weil身份。

## 7. 最强旧比较、净值及停止

553单独只付T的bounded-leg闭包，不能因为ℓ没有全du界就直接套到whole S；本门用source的actual mean leading及(6)–(9)补上准确前件。另一方面，(4)也表明新增mean是两个固定实Mellin读出加一个原L²有界reader；归一化actualPan和初等图闭包是标准rank-one extension机制。结合405/553已经给的强域、实Mellin系数、cyclic密度及584的finite/closure角色，净分类为**标准实际准入／强旧直接合成0数学轮**，不是新经典whole或实质全方法边界。

强源raw map存在与不连续于globaldu的事实均须在source稿明记，但它们没有阻止same joint data的Pan闭包扫满其源像闭包。停止这个fixed raw mean／bounded T recipe；不增probes、不调核/B/level/ray/weight/阻尼、不读下一paper，不因此完成长期Goal。其他实际不同source域、有费unbounded或非局部额外数据、cofinal修复及未逐层Pan正D′并未被本稿泛排，也不因名称自动准入。

经典非零primitive载体／整过滤／截面乘法／mixedRR、完整signedgrowth/actualq/core/coupling/Ξ及542+555→557 whole leading4/5负惯性UPPER均未改变。原literal R/K失域及整体arithmeticTheta/7.4/modularity/stack-index运输冻结保持；当前只消费明确独立R_g scalar版本及其实际raw数据。

## 8. 实际mean终稿的前件对齐

本稿已完整核读mean终稿，确认其(3)/(4)精确分解、ν仅具指数衰减而不冒称S_exp、全F强费及raw Bochner定义、(13)/(14) actual Pan两端系数和o(1)、(16)归一化关系与本稿所用前件相同。c_L为B-selfdual格covol，不与空间体积混同；H偶与正性给A_+=A_->0。原全线du/Dlog/Hlog费用失败未被误用作whole S已经下降的结论。

当前消费的mean版本为UTF-8、LF规范化SHA256：

* mean-strong-fees-and-actual-pan.md：f2c0a7ddb7db17bce68f0d2ca59fbff6bd7bdda0c6d282d525bfbdb16f21ac0f（8707 bytes）。

根收据仍须对齐T费用、553及本稿实际版本；本文件存在或hash相符不代root/fresh的语义审查。没有在此执行下一source比较、记录新轮或完成长期Goal。
