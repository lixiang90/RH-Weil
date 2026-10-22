# Arithmetic-site square与Frobenius对应：实际复合已存在，源积分尚不是截面桥

2026-10-22，用户指定非Ξ底空间／adelic restriction到平方RR的来源检验之独占原稿。
本稿只核Connes–Consani 2015的一个实际来源及其能否接受物理源；不打开下一篇论文链。
同G20261014、0c4f冻结基线；最新whole强旧仍542+555→557的4/5预算upper。
本稿不是新数学合同、全局RR、经典正性或Goal完成声明。

## 1. 恢复与原件核读范围

已读goals/README.md、STATE.json并执行research_state.py check/show；恢复Goal、C035、
最新source-dependent-family报告及405/567和363/365/366必要原件。当前family报告已给
H=(z²−1/4)Ξ(z)上的实际marked section，故不能再声称所有源map都不存在；
其base仍是旧完成谱商，这正是本次要避开的输入。

本次primary固定为[Connes–Consani, Geometry of the Arithmetic Site, 1502.05580v1](https://arxiv.org/html/1502.05580v1)。
实际核读HTML §6.3 Proposition6.12–6.13、§6.4 Proposition6.19、Lemma6.20、
Proposition6.21与Definition6.22，§7.1 Definition7.1及Lemma7.2，
§§7.2–7.4 Proposition7.3/7.4、Lemma7.5、Definition7.6、Theorem7.7及Lemma7.8的证明。
采用原文已证的半环square和reduced tensor复合；不声称本次重证全部topos／points定理。
2018§3.4的平方RR研究计划此前已来源0停止，未重读计为新容量。

## 2. 原件给出的非Ξ对象及准确复合

记S=Z_min⊗_B Z_min；其乘法为指数对相加，reduction γ取Newton凸包。
原件的平方为(N^××N^×)-topos及此结构半环；reduced square用Conv_≥(Z²)。
固定0<q<1，

\[
 F_\lambda\Bigl(\sum_i q^{a_i}\otimes q^{b_i}\Bigr)
   =q^{\min_i(\lambda a_i+b_i)},\qquad
 \Psi_\lambda=(R_\lambda,\ell_\lambda,r_\lambda),
\]

其中R_λ的指数为N+λN，ℓ_λ(q^n)=q^{λn}，r_λ(q^n)=q^n。
复合先作平衡tensor，再作乘法消去化，最后取两外侧作用生成的子半环。
其结果为

\[
 \Psi_\lambda\circ\Psi_\mu=
 \begin{cases}
 \Psi_{\lambda\mu},&\lambda\mu\notin\mathbf Q\text{，或}\lambda,\mu\in\mathbf Q,\\
 \mathrm{Id}_\epsilon\circ\Psi_{\lambda\mu},
 &\lambda,\mu\notin\mathbf Q,\quad\lambda\mu\in\mathbf Q.
 \end{cases} \tag{1}
\]

Id_ε取由q、q^{1+ε}生成的双侧连续germ半环，左右作用分别是q^{n(1+ε)}和q^n。
所以Ψ_2∘Ψ_3=Ψ_6，但Ψ_√2∘Ψ_(1/√2)=Id_ε。
这些是原文§§6–7的既有定理，**无需Ξ零除子定义base**；它们不是截面容量定理。

证明中最重要的范围是：tensor的乘法消去化不等于把参数直接相乘。
当终端乘积α无理时，每个有限支集的最小指数在ε=0唯一，故ε小邻域保持，
germ求值给R_α；α有理时可能并列，左右一阶斜率仍保留，不能直接求值删掉。
这是(1)的实际来源，并非“任何连续Frobenius必定构成无缺陷群”。

一个显式检测：在Id_ε内x(ε)=q、y(ε)=q^{1+ε}有x(0)=y(0)，但x≠y作为双侧germ。
因此specialization ε=0会遗失真正的相对数据。这个现象可能是相对载体的合法数据，
不能自动重命名为局部长度、Γ有限部分、规范线或独立平方RR的系数。

## 3. 为什么不能直接把复杂源当结构半环系数

这是一个直接范畴计算，不是排除所有F₁方法的定理。任意幂等加法半群T的加性群完成均为0：
在群完成中[x]+[x]=[x]，故[x]=0。因此不能“先把结构半环的加法做Grothendieck群完成，
再张量C”来取得非零全complex源空间；同理不存在从此结构半环到非零C代数的unital半环态射。
反方向的普通C加法群到zero-sum-free半环若要求保零且保加法，也只能为零：
φ(v)+φ(−v)=0强制二者均为零。

这只排除了**literal保加法结构半环线性化**。它不排：先独立构造有理／数值对应群，
再扩张C系数；Witt提升；derived／cyclic载体；源依赖family；实向量化或分布current。
函数域正例正是先有实际cycle、交数、截面乘法和RR，再扩张系数，
从不要求F_q结构环unital映入C。不能用以上小计算否定这种合法迁移。

365的P=U−V²在λ=2代入为0、但支集最小权为2，已经给全complex相消与Newton支集的失配。
366的全部字符族与带边界Jensen主除子是合法旧修复，却未提供平方上的有效性／RR。
本次没有把这些旧障碍当新净后果。

## 4. 一个具体非谱base积分候选及405/537检验

为真正检验“把源积分到对应”，暂在外加的complex current空间中定义

\[
 \mathcal C_r=\exp_*\bigl(r(u)\,du\bigr)\in M(\mathbf R_{>0};\mathbf C),
 \qquad r=e^{u/2}f. \tag{2}
\]

这是给参数标签Ψ_(e^u)的系数current，不冒称它已经是原site的global section或cycle。
对r∈S_exp，(2)合法且由exp双射严格单射。固定窗supp r⊂[−L,L]给

\[
 \|\mathcal C_r\|_{\rm TV}=\|r\|_{L^1(du)}
 \le\sqrt{2L}\|r\|_{L^2(du)}
 \le\sqrt{2L/\log2}\,\|r\|_{D_{\log}}. \tag{3}
\]

这里D_log采用原zero-extension Fourier加权范数；上式只是原du费用的足够上界，
不是精确D_log dual费，也没有统一全线常数。L→∞的费用不得删掉。

405关系r_p=e^{u/2}p≠0在(2)下仍非零；甚至同一明确矩给

\[
 \int_{\lambda>0}\lambda^{3/2}\,d\mathcal C_{r_p}(\lambda)
 =\int e^{2u}p(u)du=M_p(2)=\pi/6\ne0. \tag{4}
\]

换元、物理权与该Mellin矩均已对齐。p∈P_an且双degree为零，故(2)不能消405主关系。
537非根r_0=(∂_u²−1/4)ψ则因(2)单射而保留；仅过非根测试并不足。
若仅保两个degree矩∫e^{±u/2}rdu，可消p，却同样消r_0，因此也不构成修复。

若再把(2)的系数空间按exp_*(e^{u/2}P_an du)取商，关系当然消去，
但这是将405旧解析商装进target，尚未从site的局部单位、有效对应或restriction证明主除子身份。
不应因底空间没有书写V(Ξ)就报告独立算术输入。

### 4.1 连续积分不能无费忽略切向缺陷

在log坐标中，(1)的exceptional locus包含u+v∈log Q_{>0}且e^u、e^v无理。
它是可数条直线，对r(u)t(v)du dv这类绝对连续乘积测度为零。
因此在**只保标签、按a.e.识别**的measure卷积模型中，可以合法得到通常加法卷积。
这不证明原对应类别中的精确复合积分存在，更不证明其trace、对角restriction或有限部分与该a.e.模型相同。
例如atom λ=√2与其倒数的原复合仍是Id_ε，而普通标签卷积给δ_1。

此外以TV为拓扑，原子Riemann和不趋于非零绝对连续measure：两者互相奇异，
距离等于两者TV之和。故(2)虽然可直接定义，不能同时把它说成在TV中对δ_(e^u)的Bochner积分。
可换弱拓扑／distribution kernel实现，但须另付连续性、乘法、trace以及diagonal读出的原norm费用。
这些保留合法escape，既不把积分全盘判不可能，也不将缺费的相对trace当已得。

## 5. actual adelic restriction是合法非Ξ来源，但还不是squareRR

405的真实E来自S(A_Q)⋊Q^×限制到ideles、取矩阵trace。
其径向像Eη=2Ση(ne^u)与Poisson对偶是实际来源；它不是由Ξ零点先反造。
因而本稿的kernel=0只排(2)，**不排该actual restriction/cyclic余核**。
在正确的源空间和degree修正下，已有P_an关系可以由此构造接入。

未付箭头必须写完整：从这一restriction复形到原件square上的截面／对应群，
须有保持关系与非根的比较map，以及局部消失量、tensor／乘法、相同对象的global capacity。
原件F_λ的Newton评价是半环同态；E是复线性解析trace，二者不是仅凭同名“restriction”即可拼接的自然方块。
365/366提供有限支集／全字符局部比较，但没有给实际E的这个比较map。
若把cyclic余核直接命名H^0或把其谱trace命名Euler characteristic，RR的正有效性和容量仍未获得。

## 6. 平方RR检验与正反例必须区分的层级

真实square和复合是设施的一部分，尚不是所需的二次容量。567的曲面证明需同一对象上
l(nD)+l(K−nD)≥χ+½(n²D²−nDK)、有效性degree、实际截面乘法和固定／有控H^0(2K)。
Newton对象的二维指数集、次数乘法或一个任意toric多项式空间的O(n²)格点数，
并不自动把Euler二次系数识别成经典完整Weil交数；后者还含Γ对角finite-part及双pole背景。
本稿没有从2015 §§6–7提取一条并不存在于其结论中的平方RR不等式。

连续正反例采用567同一完整Π族Z_c(s)=1+c/[s(s−1)]：positive段与off-line段都允许
相同label卷积、transpose和formal graph复合；primitive 2×2 Gram在负段行列式−4sinh²(ah)<0。
这些是对“标签复合／正off-diagonal ⇒ Hodge正性”的反测，不是声称该连续g系统已带原算术site。
本稿没有无费将一般g分布赋予Q的additive adeles或其整数frame。

函数域的Γ_Frob复合为真正cycle复合，平方C×C的局部交重数和RR给同一signed组合的容量，
随后由完整点数／所有period aliases身份推出全complex Weil型。正号来自这个同对象容量，
并不来自只把Frobenius标签相乘。实际F5正例及正整数Euler负例仍按567原全递推范围消费。
这说明被推广的应是restriction→cycles/sections→同源RR链，不能以“已有square”省略中间两箭头。

## 7. 完整项、净后果与停止范围

本稿保留完整经典Γ、全部素数幂和极点项的目标规范；(2)不自带它们的trace，所以没有删项后宣布相等。
405已经用指定Tate/Fourier/Haar给原point contact和完整局部trace；该旧解析identity可消费，
但尚未成为2015 square上截面容量的Euler系数。2018计划不重复记为输入。

本次可消费的是一个具体分类与负测：(1)真实独立square/compose已存在；
literal semiring线性化失败，外加current有fixed-window原du费但不能消p；
a.e.积分可以忘掉实际切向数据；actual adelic cyclic余核保留为未排来源。
它没有比363/365/366/405/567及最新family门付出新的classic容量，故有界来源检验至此停止，0数学轮。
下一次此来源的准入必须展示actual E到square relative sections的非形式比较，
至少在p、其全部指定关系族、r_0上对齐并给原du/Dlog费用；随后才谈local order／global二次容量。
不能继续调参数、只增加Ψ样本或把旧谱商换名字。
