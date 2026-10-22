# 独立容量准入：算术 Hodge 旧前沿与一个 arithmetic Siegel–Weil 章节门

2026-10-23。独占分支；只做准入与来源核查，不改 STATE／cadence／Goal，不新增数学轮。

## 1. 先恢复可消费前沿

本分支已读 goals/README.md、STATE、G20261014、MACRO_FRONTIER、D20261022N，执行 research_state.py check／show，并核实际工作树。冻结基线仍为 0c4f3a3e／≤538；最新数学为578，cadence1，正式cycle15。当前 Γ／twist／Pick／shift／Riccati 已停止，不能再以寻找同名正核恢复旧预算。

最强实际 ζ 净后果仍是542＋555→557的 whole leading4/5负惯性**上预算**。577的完整Γ/contact正层与 (q_R=(-g_R)_+) 合法，但其消失对该族仍⇔完整Weil正性／RH。578与后续来源门没有独立付该费用。全源容量、危险core／coupling／Ξ识别均未改变。

本次去重用 rg 检查 notes、goals/reviews、reviews/2026-10-22 的 Arakelov／Hodge／Kudla／Siegel–Weil／theta lift 关键词。前两类已有实际候选与停止；未定位到下述1999原件的既有逐章消费。根部选定该原件后，本分支只消费这个**章节门**，不顺接后续 paper；此前定位到的推广版不作为本稿证据。

## 2. 不能遗漏的强旧：真实算术 Hodge 对象早已存在

[552](../../../notes/552-radial-adelic-green-principal-and-comparison-gate.md)已核 Yuan–Zhang arithmetic Hodge 的原假设；更强的具体资产是 (X=\mathbf P^1_{\mathbf Q})、有限位标准、无穷位径向 Green metric 的真实 adelic 对象。

对405关系源 p，该对象的负自交为 (\|p'\|_2^2>0)，故不下降完整主关系。固定窗的双pole-zero高频源又给该能量 (\asymp t^2)，而完整经典 \(Q_\zeta\asymp\log|t|\)。这不是缺少 Hodge 定理或不懂构造对象，而是**源map／主关系与原费比较已具体失败**。

567已恢复函数域 (C\times C) 的截面乘法、RR二次项、固定canonical容量及 primitive mixed交数；574–575又已有非平凡clutch／Cartier设施。10-22实际 adelic-square 门已有真实 (\mathbf P^1_{\mathbf Z}) 的 (n^2) 小截面容量。不能把上述任一旧存在性重新记为新容量输入；缺的是同一个源对象上正确方向的预算身份。

## 3. 唯一外部章节门及准确读取范围

唯一消费原件：[Kudla–Rapoport–Yang, *On the derivative of an Eisenstein series of weight one*](https://www.math.uni-bonn.de/people/rapoport/myalggeom/preprints/tinynew.pdf)，IMRN1999作者预印本镜像，40页。根部给的 Cologne tinynew.pdf 此次web读取timeout，Bonn同名作者镜像可读。本次核引言Theorems1–3、§1的实际Schwartz定义、§4 Mellin证明与§5局部长度至Theorem5.12的接口；**未独立重审全部CM／Gross局部变形来源及§6全部推广。**

精确来源摘要：固定素数 \(q>3\)、\(q\equiv3\pmod4\)、\(k=\mathbf Q(\sqrt{-q})\)。Theorem3给CM模空间上正指标0-cycle degree \(\deg Z(n)=a_n(\phi)\)；非正指标另有arch项。§1的实际输入为 \(\mathcal S(C_\mathbb A)\)，经局部Weil表示在0评价得到induced section，未给原r。Theorem2／§4给

\[
 \mathcal M\phi(s)=\Lambda(s)\Lambda(s,\chi)
 \left[\log q+\frac{\Lambda'}{\Lambda}(s,\chi)-\frac{\Lambda'}{\Lambda}(s)\right],\qquad
 \Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s).
 \tag{A}
\]

这里 \(\Lambda(s,\chi)=\pi^{-(s+1)/2}\Gamma((s+1)/2)L(s,\chi)\)，导子外因子按原文保留。Lemma4.1在 \(\Re s>1\) 支付正项Mellin。**完整经典ζΓ确实出现在(A)中**；不能因另一项为odd \(\chi\) 就称原件没有经典Γ。degree身份、全局Mellin与局部length是同源实物，非自由谱标签。

## 4. 原域、系数方向和容量责任逐项检验

下列结论是本分支的**适用性判断**，不是作者声称已经处理经典 RH。

| 所需接口 | 这一个定理实际能否付款 |
|---|---|
| 原物理 \(r=e^{u/2}f\) 的全complex源map | 第一步必须从r给出 \(\varphi_r\in\mathcal S(C_\mathbb A)\) 及相容local cycles。(1.4)是Schwartz→induced section的线性evaluation map，不能直接读成r→Hermitian算术截面。 |
| 同一对象上的 Hermitian 二次容量 | Theorem3是 arithmetic degree 的**线性系数身份**。正指标有效0-cycle degree不推出任意mixed源平方正号，也不是567的primitive自交／截面乘法预算。 |
| 完整经典Γ | (A)的经典Γ已付，但与oddχ的Γ和 \(\Lambda\Lambda_\chi\) 乘子共同出现。抽出完整ζ预算须另付signed解卷积／paired-form比较；不能从已给正量相减或除以任意非负函数后，声称保正型。 |
| 全部素数幂与两个经典pole | (A)是完整亚纯身份，不能漏Γ/poles；局部length也是真实整性。但尚无逐源身份把CM coefficients转成 \(\sum_{p,k}(\log p)p^{-k/2}(r*r^*)(k\log p)\) 与两个经典pole矩。零指标常数不能直接改名经典pole缺陷。 |
| q预算与原范数 | 未给 \(c_R=\|q_R\|_\infty\)、\(m_R=\|q_R\|_1/(2\pi)\) 的新小量；没有原du／zero-extension Dlog到该lift／height的全尾与成长费用。 |

由定理“有真实有限位与arch同源性”能得到的选择信息是：**可接受的几何证书并不必须先是整数梳；但含有完整Γ的固定CM恒等式尚不等于经典Weil预算的正证书。** 尤其不能把 degree 正号当成 arithmetic Chow 全体的正Hermitian metric。

### 4.1 可立即核的净符号：正项Mellin不是临界Hermitian平方

从(A)中完整对数导数按Euler与digamma展开，在 \(\sigma>1\) 有

\[
 D_q(s):=\log q+\frac{\Lambda'}{\Lambda}(s,\chi)-\frac{\Lambda'}{\Lambda}(s)
 =\log q+\frac12\left[\psi\!\left(\frac{s+1}2\right)-\psi\!\left(\frac s2\right)\right]
 +\sum_{n\ge2}(1-\chi(n))\Lambda(n)n^{-s}.
 \tag{B}
\]

这里保留 ramified与所有proper powers；\(1-\chi(n)\ge0\)。对实 \(s=\sigma>1\)，digamma差也正，故安全轴正号可直接由原Euler／Γ给出，无须调用Weil正性。进一步标准digamma积分换元给

\[
 \frac12[\psi((s+1)/2)-\psi(s/2)]
   =\int_0^\infty\frac{e^{-su}}{1+e^{-u}}\,du,
 \qquad\Re s>0.
 \tag{C}
\]

因此**差的Γ核**在原点有界；完整Γ的奇性在这一步相减中取消。(A)仍含完整经典Γ的乘子，不能据(C)反称其缺Γ；也不能据(C)正号声称完整WeilΓ奇性已经获正。抽掉 \(\Lambda\Lambda_\chi\) 的formal meromorphic除法可做，但不是正型保持运算，临界全源与原norm费用须另证。

(B)–(C)是原件身份的标准Euler／digamma直接核，不是新RH输入，也未另计数学轮。其责任明确地落在同源signed运输，而不是再优化粗局部length。

### 4.2 原源接入的准确约束

任何候选 T 若在原全线du或Hlog连续、对405全部physical Pan的陪集不变并取值于Hausdorff正能量目标，则553稠密性迫其常值（线性时为0），537非根丢失。这是**旧553的直接消费**，不排强Fréchet域、level成长、非局部／源适应、有费无限载体或未闭正能量域。

把 \(r(\log m)\) 直接当special-cycle系数也未付款：有限点读出须先按568的原域费用核，405全关系没有从该写法自动消去。平滑读出可修连续性，却不自动修主关系与完整Weil身份。原件Schwartz源真实存在，不能把“还没有r→它的有费map”写成“没有任何Schwartz→自动形式map”。

## 5. 必须先过的正反对照及量词

**连续正反例。** 562／578的相同正primitive、精确对偶、强PNT及Selberg预算正负模型均保留。选一个外部CM格或给其值加自由正metric，不能说明源分布决定了该几何，也不能区分两者的Weil符号；有意义的transport必须明示负例在哪个独立有效性／局部整性条件失败。当前原件没有这项source transport，故本候选是未接入，而非已经通过连续检验。(A)的mixed completed对象不能插入 Γ=0 模型改换目标。

**函数域。** 567的真正控制已经在同一 \(C\times C\) 上给全部Frobenius graph mixed交数、双degree扣除、独立RR及所有returns／aliases。新候选须至少对这一控制恢复同对象 primitive身份。CM arithmetic degree公式可以是另一种真算术设施；没有比较map前不能把两种对象拼成一次成功检验。

**405与537。** 405要求非compact Pan全族及其全部平移的真实主同构／根消去，不能只查compact空交；537要求固定17/16窗的非根保留。当前无 T，二者均未通过本候选。577已付的逐固定强源尾费与537最终可见性不因本来源而扩大。

**固定／D′／成长。** 有限个cycle或一个fixedlevel lift只给其原域的陈述，不支付完整分布的 \(D'\) 逼近，更不支付成长 \(L\) 的原du/Dlog一致费用。即使未来独立推出该特定577族 \(q_R\to0\)，它有RH后果并非循环；本轮的问题是没有推出该新估计，而不是等价性本身禁止证明。

## 6. 本门决策、停止与可改变选择的实物

**不准入新的数学合同／579。** 新恢复的文献内容是一份真实但不同目标的 arithmetic Siegel–Weil 身份；扣除552／553／567与577强旧后，未新增实际 \(q_R\) 小费、primitive容量或whole后果，宏观瓶颈不变。在这个**单章节门**停止，不改核、扩level、串另一篇theta paper，亦不将未知 \(T\) 改名“theta源桥”后开合同。

重准入须收到实物而非愿望：一个不以完整Q／Ξ零坐标作标签的 T 或相对cycle公式；其405全关系与537非根检验；原du／Dlog、Γ规范、全部幂和pole的同源比较与尾费；以及同一对象上的独立signed容量或局部length到primitive二次型的系数方向。可以先为一个可变但明确的源域支付上述门，不要求一开始就解决所有成长尺度。新输入若只给另一份正height，而完整预算比较仍未知，继续不准入。

本输出为root选择提供“未取得新设施”的结论；具体准入与唯一下一动作由root合并其他分支后决定。未创建运行Goal、未动cadence／STATE／Git。
