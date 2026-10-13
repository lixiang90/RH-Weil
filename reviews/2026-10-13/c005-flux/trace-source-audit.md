# C005最后一轮：实际Sonin trace、单边界素数账本与overlap剩余

核读日期2026-10-14（Asia/Shanghai）；输出目录沿用父任务指定的2026-10-13。
恢复AGENTS、README、STATE/check/show、C005、D20261013G及531后执行。
仅写本来源/独立推导审查，不改STATE/cadence，不独立计数学轮。

## 原件与可消费范围

1. [Connes–Consani作者稿Selecta.pdf](https://alainconnes.org/wp-content/uploads/Selecta.pdf)，55页，hash见C004 source receipt。重新核印页22–25，Proposition4.4、(75)–(82)、Theorem4.6、(84)–(91)。原arXiv2006.13771v1为57页、trace定理号4.7；不混用编号。实位ε由真实orthogonal Sonin projection及成对cutoff角分解得来，不是任意Hilbert同构。
2. [CCM arXiv2310.18423v2](https://arxiv.org/html/2310.18423v2)，版本/实物hash见C005 source receipt。这里只消费原(57)–(58)、Proposition4.7及Theorem4.6的实际θ/η/Fourier接口；它未提供新半局部ε符号或首prime trace定理。
3. [Burnol math/0208121v1](https://arxiv.org/pdf/math/0208121v1)，2002-08-15，7页；全文核读，视觉核印页5–7。它与[发表的四页C.R.335(2002),689–692](https://comptes-rendus.academie-sciences.fr/mathematique/item/10.1016/S1631-073X(02)02546-3.pdf)排版/编号不同，本文引用以7页v1为准。本地`tmp/pdfs/c005-flux/burnol-0208121v1.pdf`保留原字节。Lemma2/3及Theorem4给real cosine Sonin的projection/resolvent；Theorem8/9给structure function及Mellin evaluator的边界jump。本文没有S={∞,2}或weighted-norm prime渐近结论。

Burnol原字节SHA256：`1890a3867e745c342be3a70eeb2948c673bfb644fc4f392f9302d0b9c96acc3b`。

## 两cutoff blockGram合法，但不能逐块减无限trace

在physical共同表示中固定Sonin cutoff1。写F_v为实位F或实际Fp，C为低cutoff乘法投影，E=I−C。令`K_v=C F_v C`，`D_v=F_v C F_v`。531给K_p compact、norm<1但nonHS，实位K∞则快速谱衰减。

映射`V_v:RanC⊕RanC→H,(u,w)↦u+F_vw`有Gram

    Γ_v=[[I,K_v],[K_v,I]],
    Γ_v^(-1)=[[L_v,-L_vK_v],[-L_vK_v,L_v]],
    L_v=(I−K_v²)^(-1).

因此真实Sonin projection

    S_v=I−V_v Γ_v^(-1) V_v*.

这是Burnol Theorem4背后的bounded pair-projection公式，实际Fp的norm<1也足够支付它。这里**bounded逆存在**不等于它的每个块在源夹心后可单独取trace：在log坐标，lowcutoff是无限长半线；`A_g C`不是HS，相关对角trace有infrared logarithmic发散。应先保留完整projection或已证TC的relative difference，不写`∞−∞`。

## 单个实际边界：父任务候选的独立TC及常数核查

以下是新增独立推导，不假装原文已给。采用unitary log表示`L²(R,dy)`，`H_+=L²([0,∞))`，`U_a f(y)=f(y−a)`，`a=logp,q=p^(-1/2)`，`B=I−qU_a`。B及B^(-1)保持H_+，因此实际第二高空间

    Fp H_+=B F H_+.

再由F共轭，把它与FH_+的projection difference化为

    D=P_(B*H_+)−P_(H_+).

分解`y=θ+ja, θ∈[0,a),j∈Z`。每fiber上`B*H_+`是j≥−1的子空间中与

    v_j=√(1−q²)q^(j+1), j≥−1

正交的codimension-one空间；v_j对j<−1为0。于是若V将`L²(0,a)`等距送到上述fiber向量，

    D=P_[−a,0)−V V*.

此处θ连续，VV*不是整个ambient空间中的有限秩projection。

对`A_g=∫g(t)U_tdt`，`g∈Cc∞(R)`，两个源夹心皆**单独positive TC**：

    ||A_gP_[−a,0)||HS²=a||g||²,
    ||A_gV||HS²
      =a/(2π)∫|ĝ(s)|² (1−q²)/|1−qe^(−ias)|² ds.

第二式由fiber数组的Fourier级数
`√(1−q²)e^(ias)/(1−qe^(−ias))`和Plancherel得来。Poisson factor有界，故这不是形式相减。进一步

    ||A_g D A_g*||1 ≤ 2a/(1−q)||g||².

合法trace的精确结果为

    Tr(A_g D A_g*)
      = −a/π Σ_(k≥1) q^k ∫|ĝ(s)|² cos(kas) ds
      = −2a Σ_(k≥1) q^k Re∫g(t+ka)conj(g(t))dt.

请注意第一行系数按Plancherel：展开Poisson factor为`1+2Σq^kcos`后，系数是`−a/π`；第二行则用`(2π)^(-1)∫|ĝ|²cos=Re C_g(ka)`。这正是**actual全部p-primepowers的负贡献**，不是把prime权重改正号。明确定义

    Pprime_p(g)=a Σ_(k≥1) q^k [C_g(ka)+conj C_g(ka)],
    C_g(t)=∫g(y+t)conj(g(y))dy,

则上面trace等于`−Pprime_p(g)`；Pprime本身的correlation不预设正性。F反射源的自相关不改变此实偶配对。

因此实际第二高空间projection `Q_p=P_(Fp H_+)`相对`Q∞=P_(F H_+)`的同源trace差为完整prime functional；无需给ζ零点位置或增加样本。对冻结p=2两patch `g_R^±=h_R(t+a/2)±h_R(t−a/2)`，只有k=1真实相关，pole0，||h_R||=1，所以

    Tr[A_(g_R^±)(Q_2−Q∞)A_(g_R^±)*]=∓2w2,
    w2=log2/√2,

**对每个R精确成立**，而不只是R→∞渐近。两源同号正交norm²=2。这个结论只属于单边界，不能直接充当完整T2−T∞。

## 实际overlap的准确剩余与Connes ε接口

定义

    R_v=S_v−E−Q_v+I=S_v+C+D_v−I.

Sonin上Rv=0；每个generic角平面上其谱为±ν_j，其中ν_j是`C F_v C`特征值。因此R∞为ambient trace class，Rp为compact但nonHS。这个operator是成对boundary overlap，物理定义没有unknown投影。

精确operator identity为

    S_p−S∞=(Q_p−Q∞)+(R_p−R∞).

真实source Sonin夹心已由531分别TC，单边界source difference已在上节TC，故`A_g(R_p−R∞)A_g*`亦TC；再用R∞的ambient TC得`A_gR_pA_g*`TC。这不要求Rp自身为TC，不删除conditional cancellation。

为了核与2021ε一致，写角平面orthonormal basis ξ_j（low）和ζ_j（outside low），`F_vξ_j=ν_jξ_j+√(1−ν_j²)ζ_j`。在此basis

    R_v=[[ν_j²,ν_j√(1−ν_j²)],
         [ν_j√(1−ν_j²),−ν_j²]].

冻结real g使`Z_g=A_g*A_g`的Fourier multiplier `|ĝ|²`偶，所以与F_v交换。由`<ξ,Zξ>=<F_vξ,ZF_vξ>`得到

    <ξ,Zξ>−<ζ,Zζ>
       =ν_j/√(1−ν_j²)(<ξ,Zζ>+<ζ,Zξ>).

于是source角平面trace合并为`ν_j/√(1−ν_j²)`乘上述cross。这与作者稿(85)的ε两反演方向精确吻合：一边方向的cross因low/outside支持为0，不重复计两倍。实位R∞ ambient TC保证此合并可以逐项核并取trace，故

    E∞(g*g*)=Tr(A_gR∞A_g*).

半局部不能先把非绝对角series逐项换trace，但本节整体source TC已付，故可合法定义真实

    E_p(g*g*):=Tr(A_gR_pA_g*).

联合2021实位`T∞=W∞+E∞`及单边界exact prime identity，得到

    T_p(g)=Γ_actual(g)−Pprime_p(g)+E_p(g*g*),
    Γ_actual(g)=W∞(g*g*)=(2π)^(-1)∫2θ'(s)|ĝ(s)|²ds.

冻结pole0、仅含p=2的实际域因此有

    QW(g)−T2(g)=−E2(g*g*),
    d_R^±=∓2w2+Tr[A_(g_R^±)(R2−R∞)A_(g_R^±)*].

这是source已合法支付的signed身份。**最后的source overlap trace、其符号、固定L²质量界或高频趋零仍未证明。** ambient Rp compact只使高频窗夹心operator norm趋0，不使其trace自动趋0；无限多个小角可保总trace。R∞的source overlap趋0可用ambient TC和source强零证明，但Rp nonHS不能照搬这一理由。

## Burnol evaluator路线的具体准入缺口

Burnol v1 Theorem7/8用`(I±F_λ)^(-1)[2cos(2πλy)]`构造structure函数，Theorem9把该函数接到真实Mellin evaluator的边界jump。它支付的是实位smooth kernel的L² forcing与analytic continuation，并未给半局部weighted norm的高频密度。

实际Fp的boundary row，Sonin cutoff固定1，为distribution

    k_p(1,y)=2[(1−1/p)Σ_(n≥0)cos(2πp^ny)
                          −p^(-1)cos(2πy/p)].

取任意非零非负ρ∈Cc∞(0,1)，测试`ρ(y)Σ_(k≤N)cos(2πp^ky)`；norm为O(√N)，row配对为`(1−1/p)(∫ρ)(N+1)+O(1)`。频率gap及分部积分给所有offdiagonal统一O(1)。因此这个forcing在内部都不是L²。已知bounded L² resolvent不能原样作用于它；需要独立的distribution/Sobolev域及boundary evaluation控制，不能称其“相同Burnol公式”已付。这不否定实际entire-space evaluator存在，也不证明E2不连续。

原件给一般de Branges kernel表达，但本次核读没有取得S={∞,2}物理norm对应structure function的高频phase/diagonal渐近，故不假设所需source overlap趋0。把local E函数简单乘Euler factor会遇到meromorphic poles；原finite-S entire空间同构也没有说这种乘法是其实际structure function。

## 审查结论与唯一下一动作

本审查新增可消费内容是：真实单边界的TC账本精确支付全部primepowers；通过实际overlap角算子给完整Sonin source差的准确剩余，并核实与2021ε的一致性。已付目标`∓2w2`只在单边界；真正`d_R^±`尚有真实overlap trace。

最后准入条件已经具体：证明冻结域上`Tr(A_gR2A_g*)≤0`，或支付其source L²费用及必要符号；若先验只需高频首项，仍须证明该overlap trace对h_R^±趋0。不能用Rp compact、norm<1、已有de Branges existence或粗Γrelative尾替代。

父任务唯一下一动作：以不同组织逆审单边界TC/常数与完整overlap identity，决定是否有已付source overlap估计；缺该估计时按C005最后一轮止损，不继续unknown flux改名。父代理另外通知独立kernel审查正在评估sharp Mellin-window候选；该未完成候选没有在本文件消费为compact或符号定理。未修改STATE/cadence，无本辅助任务的下载或计算后台进程。

主代理协调收据：上述历史审查只独立支付singleboundary及overlap身份；
随后[direct-symbol-audit.md](direct-symbol-audit.md)与[reverse-audit.md](reverse-audit.md)
另行支付actualP/求值/完整G逆误差，消费为532的固定源紧桥。
这不将本文件未证明的低域符号升级。当前唯一动作从STATE的C006恢复。
