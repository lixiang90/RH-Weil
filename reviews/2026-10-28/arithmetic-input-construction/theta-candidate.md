# 整数theta格点mixed规则：实际公式与旧重编码筛除

2026-10-28；unit_height独占构造稿。恢复STATE／D20261028O、同G20261027、前沿、O结算及553，check/show通过。只做一次经典整数theta的源规则尝试；不复活rank2／wind／纵投影／MB／correctedtheta／Pet或源商。无web／PDF／数值，只写本稿，不改STATE／cadence／合同／Git。

**本次形成了具体算术公式，但扣旧后仅为579／582已付源的整数采样与Gram汇总，未形成新的数学输入。** 下述算术格点承担真实数据与费用，未任取曲线、未知正H或RR；发现其旧因式分解后停止，不调权／高度／采样点修补。

## 1. 从真实整数theta直接给规则

固定经典格 \(\mathbb Z\) 及Gaussian

\[
 \vartheta(t)=\sum_{n\in\mathbb Z}e^{-\pi n^2t},\qquad t>0.
\]

原physical \(r(u)=e^{u/2}f(u)\in S_{\exp}(\mathbb R;\mathbb C)\)，不换bare f。以正整数格点为实际载体 \(\mathscr K=\ell^2(\mathbb Z_{>0})\)，定义

\[
 k_n(u)=e^{u/2}e^{-\pi n^2e^u},\qquad
 (J_\vartheta r)_n=\int_{\mathbb R}r(u)k_n(u)\,du,
\]
\[
 G_\vartheta(r,s)=
 \sum_{n\ge1}(J_\vartheta r)_n
                  \overline{(J_\vartheta s)_n}. \tag{1}
\]

这是一份明确source／mixed生成规则，整数n²是原格的二次型，不由未知ζ零点、Weil值或任意PSD权选取。形式核实际为

\[
 \mathcal K_\vartheta(u,v)=
 \frac{e^{(u+v)/2}}2
 \bigl[\vartheta(e^u+e^v)-1\bigr], \tag{2}
\]

故所有整数项共同出现；不是把theta仅写进名称。式中减1准确排除格点0，对应(1)只用n≥1。它没有因此自动支付经典双pole，下面比较仍保完整原目标，亦不将0格点的处理称为principal消去。

有限前缀 \(G_{\vartheta,N}\) 由n≤N给出，规则本身固定，没有另选归一化／变权／源适应阈值。

## 2. 原norm与实际全源定义

每个坐标核在原du中有精确费用

\[
 \|k_n\|_{L^2(du)}^2
 =\int_{\mathbb R}e^u e^{-2\pi n^2e^u}du
 =\frac1{2\pi n^2}.
\]

因此

\[
 \sum_{n\ge1}\|k_n\|_2^2=\frac{\pi}{12},\qquad
 \|J_\vartheta r\|_{\ell^2}^2
 \le\frac{\pi}{12}\|r\|_{du}^2
 \le\frac{\pi}{12\log2}\|r\|_{D\log}^2. \tag{3}
\]

第二项使用原全线zero-extension
\(\|r\|_{D\log}^2=(2\pi)^{-1}\int\log(2+|t|)|\widehat r(t)|^2dt\)。
故J确为全L²、从而全complex S_exp上的Hilbert–Schmidt线性map；mixed和绝对收敛，有限前缀有同一上界。强半范数也可经
\(\|r\|_2\le N^{-1/2}p_{N,0}(r)\)、N>0控制。这里是充分实际费用，不以其充当算术height或primitive容量。

用核展开(2)时按有限和再取Hilbert–Schmidt极限，避免对双变量无界区间无说明地交换积分。此正Gram未证明只依u−v，事实上(2)依赖 \(e^u+e^v\)；不能直接把每个前缀称为单变量正D′分布。

## 3. 信息差核对：原整数数据并未越过旧源族

构造后须先作如下精确去重，而不是按新kernel或新索引计输入：

\[
 (J_\vartheta r)_n
   =(T_0r)(n,0)
   =L_{1,n^2/2}(r). \tag{4}
\]

第一项是579原raw Gaussian
\(T_0r(x)=\int r(u)e^{u/2}e^{-\pi e^u|x|^2}du\)
在二维raw模型的格点(n,0)的值；第二项是582已付Green系数
\(L_{m,v}(r)=\int r(u)e^{u/2}e^{-2\pi mv e^u}du\)
取m=1、v=n²/2。582的逐项费 \(1/(4\pi mv)\) 同样立即给(3)。

整数格确使所有n²与可求和费用固定，theta核由此真实决定；但这个采样／汇总没有给原族之外的principal边、非零primitive类或独立mixed-Weil身份。它也不是KRY一般cycle／height functor的新延拓。不能将已有模态代入一串整数参数，称为摆脱已止Green recipe的新载体。

因此(1)只能作为本次构造尝试保存，**不能作为新来源首门或已准数学合同**。

## 4. 最便宜全405测试：系数553及实际noncompact见证

若拟以(1)作为精确经典mixed型，则对全部physical Pan的必要条件是
\(G_\vartheta(p,p)=0\)。正和使每个坐标 \(L_{1,n^2/2}(p)=0\)。各坐标已由(3)独立globaldu连续且非零，553的真实Pan平移线性稠密性便使这个必要条件不可能对全Pan成立。这里不是把whole map强费误当免责；必要坐标本身已经满足强旧假设。

并有旧582现成的exact关系控制，不必重跑证明：取405真实
\(p=(D^2-\tfrac14)H\)、H>0、H∈S_exp，以及原physical平移p_b。由同一积分的准确换元，

\[
 (J_\vartheta p_b)_n
 =e^{b/2}L_{1,n^2e^b/2}(p).
\]

旧582小v式
\(L_{1,v}(p)=-4\pi v M_H(3/2)+o(v)\)，
\(M_H(3/2)>0\)，给每个先fixed n

\[
 (J_\vartheta p_b)_n
 =-2\pi n^2e^{3b/2}M_H(3/2)+o(e^{3b/2})<0
 \quad(b\to-\infty). \tag{5}
\]

故一个充分负的固定平移就有G(p_b,p_b)>0，而完整Weil型在该真实Pan上为零。源没有crop，全部强尾与平移来自旧405／582；没有从拓扑闭包升级exact成员。(5)是已付公式的直接代入，不是本次新strict反例。

这一判断只拒绝本份正Gram的精确principal／mixed角色，不把所有D′中间层强制逐层杀Pan。

## 5. 即使改称近似正规则，原fixed前缀也无目标净果

若只把 \(G_{\vartheta,N}\) 当不逐层消Pan的正近似族，仍有对全部N同一 \(\pi/12\) globaldu上界。旧552完整Γ高频门已经给：固定非零
\(\chi\in C_c^\infty((-17/16,17/16))\)，取 \(r_R=\chi e^{iRu}\)，

\[
 Q_\zeta(r_R)=\log R\,\|\chi\|_{du}^2+O_\chi(1).
\]

完整primepowers与contact／双pole均在这个旧式中，未删背景。先选一个固定且有限的大R₀，使
\(Q_\zeta(r_{R_0})>(\pi/12+1)\|\chi\|_2^2\)，则对所有N

\[
 Q_\zeta(r_{R_0})-G_{\vartheta,N}(r_{R_0},r_{R_0})
 >\|\chi\|_2^2>0. \tag{6}
\]

故这份原规则不能逐fixed compact源趋完整Weil型，不涉及交换R与N极限。若要求双polezero，可直接沿旧552已付dual-template修正后的同类测试；不把pole漏项当本次唯一障碍。

这是552＋(3)的旧后果，与已止Pet反测的责任同类。本文没有换到发散权／去零模补偿／Möbius重组，也不将这些尚未给出的规则作为本candidate的后续计划。

## 6. 本次构造状态

独立原料是真实经典整数theta，实际公式为(1)–(2)，最便宜测试是必要坐标553／(5)，近似解释另被(6)挡住。相对强旧没有新的箭头付款：原Gaussian／Green模态(4)已存在，正整数平方采样的可和upper不产生独立原norm净费或经典相消。

因此本次是**形成明确算术尝试后识别为旧重编码，未形成合格新candidate**。这不是任取proper曲线的重复，也没有把theta／positiveGram名称当成正性输入。停止本格点Gram recipe，不调参数／权或续source章；不与root另提出的theta微分算子potential混作一个候选或重复其证明。

没有新数学合同／编号／计轮，也没有全theta／非局部／强费／源适应方法类no-go。完整Γ/FP-contact、所有properpowers、双pole、allcomplex及原source/growth量词保留；whole4/5仍为负惯性UPPER，独立signed/corecross／primitive mixed与Ξ未新付。长期Goal仍由自主研究推进，不转交用户为唯一输入来源。
