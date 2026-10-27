# Fixed full-gap：实际相对表达、边界费用与未付余项

2026-10-28；独占消费支持稿，待 fresh／root。恢复 README／STATE／Goal／D20261028J、宏观入口与唯一 next-fixed-full-gap-type-and-fee-gate，运行 research_state.py check／show，通过结构检查。实际读532全文、C005 projection-transport／trace-source审查、560完整Gram全型、585／前轮fullgap意见及当前门；不查网／下载／数值，不实施另一投影，不改STATE、cadence或其他稿。

**判定：能从旧C005取得真实同源相对表达，以及两条有限strip合计2log b的原du费用；其余合并overlap差虽已合法TC，却没有已付cofinal独立signed预算。** 这一组织是旧公式和标准HS的直接组装，0止本首门，不准新数学合同，不调b／H0或续paper。

## 1. 原来源及norm的准确归属

532的正文算术／clipping／C0定理明确固定Sonin cutoff1；不能把它叫作任意b、更不能叫任意b的cofinal完整误差定理。一般fixed cutoff的arch投影设施来自Burnol math/0208121v1及C005的参数化运输，允许常数依fixed cutoff。Burnol原页的Pλ为低cutoff，πλ才是真Sonin投影；本文P_b统一指项目中的**true Sonin投影**，不把两个P记号混用。

采用原positive-halfline cosine norm \(\int_0^\infty|g(x)|^2dx\)，酉log字典 \((\mathcal Wg)(y)=e^{y/2}g(e^y)\) 给 \(\mathscr H=L^2(\mathbb R,dy)\)，Mellin侧dt/(2π)。不另加even-full-line的2倍。源仍是原physical r=e^(u/2)f，\(A_r=\int r(a)U_a da\)、\(U_af(y)=f(y-a)\)；裸evaluator、原物理源和窗口carrier保不同角色。

固定H0共同双gap b*>1内的一个1<b≤b*，写β=log b。b不依r、X、未知Q或零点选择。令

\[
 C_\beta=1_{(-\infty,\beta)},\quad H_\beta=I-C_\beta,
 \quad M_b=\operatorname{Ran}H_\beta\cap\mathcal F\operatorname{Ran}H_\beta,
 \quad P_b=\operatorname{proj}_{M_b}.
\]

这是两腿物理／cosine gap，不是一个支撑条件。b=1对应β=0。固定有限 \(F_X=\{p\le X\}\)，保

\[
 B_X=\prod_{p\le X}(I-p^{-1/2}U_{\log p}),\quad
 G_{X,b}=P_bB_X^*B_XP_b|_{M_b},
\]
\[
 \Pi_{X,b}=B_XP_bG_{X,b}^{-1}P_bB_X^*.
\tag{1}
\]

令m_X=∏(1−p^(−1/2))、M_X=∏(1+p^(−1/2))，则m_X²I≤G_X,b≤M_X²I；B_X有界可逆而非酉。每finite X的range闭，全部Gram逆／returns不删。其m/M费用不能成为cofinal O(1)。

## 2. C005因果性确实对齐同一F_X与fixed双cutoff

原C005给 \(\mathcal F_X=B_X\mathcal FB_X^{-1}\)，它在同一物理norm下为unitary involution，且 \(\mathcal F_XU_a=U_{-a}\mathcal F_X\)。有限Euler各因子与其inverse为非负log delay的范数收敛级数。因此B_X、B_X^−1均保持每个Hβ，且

\[
 B_X\operatorname{Ran}H_\beta=\operatorname{Ran}H_\beta.
\tag{2}
\]

对偶的B_X*及其inverse则保持低半线Cβ。这里是固定β的标准因果性，不是B_X保持Sonin或与P_b交换。

利用可逆map对intersection的运输与 \(B_X\mathcal F=\mathcal F_XB_X\)，精确得到

\[
 B_XM_b=\operatorname{Ran}H_\beta
        \cap\mathcal F_X\operatorname{Ran}H_\beta.
\tag{3}
\]

所以(1)确是同一实际F_X在两条**同β cutoff**上的真Sonin投影；没有只搬一条边界、换Fourier或换inner product。此结论使用旧C005有限乘子／因果inverse组织，不是新cofinal费用。

嵌套range给Π_X,b≤Π_X,1，但不能把 \(\Pi_{X,1}-\Pi_{X,b}\) 换成 \(B_X(P_1-P_b)B_X^*\)。非酉正交化与两套G^−1仍在。

## 3. 实际合并相对表达与可单独取迹的两条strip

令 \(S_\beta=H_0-H_\beta=1_{[0,\beta)}\)，此处H0为β=0的高半线投影，不是共同raw向量H₀。为避免两者混淆，下式直接使用Sβ。定义C005意义的bounded overlap operator

\[
 \mathcal O_{X,\beta}
 =\Pi_{X,b}-H_\beta-\mathcal F_XH_\beta\mathcal F_X+I.
\]

两套原projection公式合并后，实际operator identity为

\[
 \Pi_{X,1}-\Pi_{X,b}
 =S_\beta+\mathcal F_XS_\beta\mathcal F_X
  +(\mathcal O_{X,0}-\mathcal O_{X,\beta}).
\tag{4}
\]

这是同一F_X、同一source下可核的相对表达。两个strip的源夹心都能**单独**付款：直接积分convolution kernel给

\[
 \|A_rS_\beta\|_{HS}^2=\beta\|r\|_{du}^2,
 \quad
 \operatorname{Tr}(A_rS_\beta A_s^*)=\beta\langle r,s\rangle_{du}.
\tag{5}
\]

又因 \(A_r\mathcal F_X=\mathcal F_XA_{\check r}\)、\(\check r(u)=r(-u)\)，unitary与合法TC共轭给

\[
 \operatorname{Tr}(A_r\mathcal F_XS_\beta\mathcal F_XA_s^*)
 =\beta\langle\check r,\check s\rangle
 =\beta\langle r,s\rangle.
\tag{6}
\]

各项TC norm≤β||r||du||s||du，合计为2β原du费用，Dlog按既有log2常数运输。没有Plancherel 2π再扣：这里是物理kernel的精确HS式。两strip结论对L2源核夹心成立；整个Sonin相对式仍先用旧允许的compact smooth／fixed窗Dlog源域。

记

\[
 T_{X,b}^{rel}(r,s)=\operatorname{Tr}
       (A_r(\Pi_{X,1}-\Pi_{X,b})A_s^*),
\]
\[
 \Omega_{X,b}(r,s)=\operatorname{Tr}
       (A_r(\mathcal O_{X,0}-\mathcal O_{X,\beta})A_s^*).
\]

前者由嵌套投影、旧A_rΠ_X,1的HS域成立；(4)减去两个已付strip TC才证明后者的**整个合并差**TC。得到精确同源身份

\[
 \boxed{T_{X,b}^{rel}(r,s)
       =2\log b\,\langle r,s\rangle_{du}+\Omega_{X,b}(r,s).}
\tag{7}
\]

固定b的2log b是超出“仅存在投影”的明确边界账本，但它来自旧C005加finite-strip标准HS，不是新的独立全relative估计。剩余Ω不是任意命名的误差：它在(4)中由两套实际Sonin／double-cutoff overlap合并给定；然而知道这个对象不等于已知其cofinal值／norm／号。

## 4. 不允许的逐block取迹，以及旧粗证书实际付到哪里

C005 pair map从Ran Cβ⊕Ran Cβ送(u,v)到u+F_Xv，bounded block Gram逆公式保完整Sonin投影。即使各fixed参数下该逆存在，A_rCβ仍一般非HS，因低cutoff为无限log半线；不同展开中的单个对角块可能有无限trace。本文没有对Hβ、F_XHβF_X、I分别取迹，也没有将O_X,0、O_X,β的单个source trace从合并TC反推出来。式(7)合法性只来自合并(4)与独立strip TC，不是∞−∞。

现有可消费的整体粗界仍只有

\[
 0\le T_{X,b}^{rel}(r,r)\le t_{X,1}(r)
 \le(M_X/m_X)^2t_{arch,1}(r),
\tag{8}
\]

以及相应mixed Cauchy–Schwarz。它是Sonin／Gamma型相对费，非cofinal原du统一质量界。由(7)与(8)也只得

\[
 \Omega_{X,b}(r,r)\ge-2\log b\|r\|_2^2,
 \quad
 \Omega_{X,b}(r,r)
 \le(M_X/m_X)^2t_{arch,1}(r)-2\log b\|r\|_2^2.
\]

这项lower仅重述相对正迹；未给有利净差所需的uniform upper／signed cancellation。560的fixed-F full inverse与C0身份、安全high，以及532的fixed-p载波，都不自动支付Ω在X成长时的新相对费用。全Gram与全部returns仍待共同估计，不能把(M_X/m_X)吞进O_b(1)。

## 5. 与560完整型、585及停止的关系

用同一实际 \(C_{X,b}(r,s)=\operatorname{Tr}(A_r\Pi_{X,b}A_s^*)\) 从t_X,1及560的K_X同步扣除，原完整型只成为

\[
 K_X(r,s)-C_{X,b}(r,s)
 =T_{X,b}^{rel}(r,s)-Q_W(r,s)+P_{pole}(r,s).
\tag{9}
\]

在X_j=j+1/2、L_j=logX_j/2的原cofinal同集消费，fixed源的Q_W／双pole常数保原值；所有自相关可见proper powers、Γ／FP-contact均按560保持，没有声称任意b另有新Weil身份。式(7)代入(9)后只有原du边界项独立于X，Ω的剩余cofinal费用尚无已付输入，因此也没有支付K_X−C_X,b的小费、号或corecross。

585共同H0的ALLpoly均属M_b，原finite-EX的较大W见证也已在B_XM_b内。不能再凭同degree余量反测此fullgap，也不能从t_X,1与C_X,b各自有lower推二者之差增长。另一向量的nonmembership若无到B_XM_b的实际定量距离及源响应，也不作残余证书。

本门有实际类型差、真实合并相对operator及标准边界2log b账本，但**没有新的独立cofinal相对kernel费用／signed方向**；不满足input／test／扣最强旧净后果的数学准入。按一次门的止损，统一来源／标准0止fixed fullgap候选，不调b／H0，不实施另一投影，不续newproof／paper或预C049／586。

Whole542＋555→557 leading4/5仍为负惯性UPPER；完整净signed、同一非零primitive／mixed容量、危险corecoupling／Ξ没有新付款。此停止不证明fullgap残差必定大或必定小，不排真正有费非局部／source-adapted／Γ-relative或正D′／几何输入，也不完成长期Goal。cadence3／历史49／cycle16保持。
