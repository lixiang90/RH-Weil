# Weil结构空间：可数有限可行性、紧性与独立正号的责任

2026-10-22；独占分支。输入为405/537/553、562/563/566及574–575；同G20261014／固定0c4f。本文不改STATE、合同或cadence。以下是标准正核／GNS／紧性工具的准确恢复与具体反控制；不把它们登记为新的经典正性定理。

## 1. 可以改为存在性问题，但存在的究竟是哪一层

固定物理空间
\[
 F=\mathcal S_{\exp,\mathbb C},\qquad
 p_{N,j}(r)=\sup_u e^{N|u|}|r^{(j)}(u)|,
 \qquad r=e^{u/2}f.
\]
预先固定由同一g-integer分布、完成化、分次权和全部缺陷给出的Hermitian Weil配对 \(B_W\)，记 \(Q_W(r)=B_W(r,r)\)。不得在选择结构时改变完成化或用自由因子B(s)重定目标。405的物理全关系记 \(P_c=C(P_{\rm an})\)，完整恒等式已给 \(P_c\subset\operatorname{Rad}B_W\)；不预设相等。537的固定非根 \(r_0=(D^2-1/4)\psi\) 满足 \(Q_\zeta(r_0)>0\)，只提供这一明确源的非零标定。

**最弱的Hilbert实现空间**可定义为所有 \((\mathscr H,J)\)（取适当酉同构类），满足
\[
 J:F\longrightarrow\mathscr H\text{ 复线性},\qquad
 \langle Jr,Js\rangle=B_W(r,s),\qquad
 \overline{J(F)}=\mathscr H.                                      \tag{1}
\]
该空间非空当且仅当完整 \(Q_W\ge0\)：正向由Hilbert正性；反向直接取
\(F/\operatorname{Rad}B_W\) 后完成。若源配对连续，J亦在F的Fréchet拓扑连续。这里 \(P_c\) 自动被消去，537自动保留，但不能因此报出一个独立的405几何同构或新的算术源映射。尤其405的 \(H=C h\) 有非零双degree而仍在完整Weil根空间；强行要求 \(\ker J=P_c\) 会错误排掉这一已付数据。几何marked源需要保留的关系商与Weil能量需要除掉的根空间，应分层保存。

这是一条合法的等价组织。**等价不意味着每一种存在性证明都循环**；若存在来自独立几何、有限评价、有效性或RR的构造，可以通过(1)消费到正性。当前没有此独立存在性证明；把(1)作为定义后仅引用GNS，并未付款。

真实regular线丛、局部消失、整性、乘法、determinant line、mixed RR和完整预算应放在更强的设施空间。其到(1)的忘却映射不必满，甚至未必已构造；证明(1)的非空也不会自动恢复这些设施。

## 2. 严格可数测试系统

选固定非负偶 \(\eta\in C_c^\infty((-1,1))\)，\(\int\eta=1\)。取所有有理a、正有理b的平移缩放 \(b^{-1}\eta((u-a)/b)\)，再作有限 \(\mathbb Q(i)\) 线性组合。由mollification及Riemann和，这一可数集合在每个compact测试的全部导数一致拓扑稠密；允许固定稍大支撑窗。加入其所有导数、反射、共轭、有理平移和两两卷积的有限闭包，仍可数，且仍包含稠密的原集合。

\(C_c^\infty\) 在F稠密：\(\chi(u/R)r\to r\) 于每个 \(p_{N,j}\)，尾部使用更强的指数半范数支付。因而上述 \(\mathbb Q(i)\) 代数D在F稠密。对连续Hermitian配对，
\[
 Q_W\ge0\text{ 于F}
 \iff Q_W\ge0\text{ 于D}
 \iff \big(B_W(r_i,r_j)\big)_{i,j\le n}\succeq0
       \quad\forall n.                                       \tag{2}
\]
最后一步包括全部complex混合系数：有理复系数的稠密性给任意有限复系数，不是只检查单源或对角。

可在D的枚举中再加入实际405的 \(r_p\)、其有理平移及537的 \(r_0\)。**有理平移cyclic族的Hlog稠密不等于该族在F中穷尽全部 \(P_c\)**。若独立设施须逐项实现全关系，可另选 \(P_c\) 的可数F稠密集合，并证明该设施对F连续和关系约束闭合；F可分、可度量保证这种集合存在，但并不自动给出可有效计算的关系枚举。在最弱空间(1)中，全关系来自405的完整配对恒等式，不能用compact关系测试替代它（553已给compact交为空）。

## 3. 原du／Dlog只能给支撑相关包络

固定 \(\operatorname{supp}r,\operatorname{supp}s\subset[-L,L]\)，采用原全线zero-extension范数
\[
 \|r\|_{H_{\log}}^2=(2\pi)^{-1}\int
 [1+\log(2+|t|)]|\widehat r(t)|^2dt.
\]
经典 \(\Gamma_\infty(t)=\Re\psi(1/4+it/2)-\log\pi=2\theta'(t)\)。令
\[
 C_\infty=\sup_t\frac{|\Gamma_\infty(t)|}{1+\log(2+|t|)}<\infty,
 \quad
 C_L=C_\infty+2\sum_{n\le e^{2L}}\frac{\Lambda(n)}{\sqrt n}
                    +4\sinh L .                              \tag{3}
\]
由完整Γ乘子、原平移的L²等距性及两pole矩的Cauchy–Schwarz，
\[
 |B_\zeta(r,s)|\le C_L\|r\|_{H_{\log}}\|s\|_{H_{\log}}.        \tag{4}
\]
其中sum含全部proper powers；\(n>e^{2L}\)的相关实际为0，并非删掉定义。pole粗upper为 \(4\sinh L\)，不是声称其sharp operatornorm。Γ/contact正规化已固定。du alone不能一般上界Γ的高频log价格；必须保Dlog或另付正则费。

因此若(1)存在，固定窗可有 \(\|Jr\|^2\le C_L\|r\|_{H_{\log}}^2\)。\(C_L\) 允许成长，这只是已知包络，不是小费用或独立容量。全F可由完整配对连续性选指数半范数包络；它与全线原du/Dlog有限共同常数不同。

553的直接反门必须保留：若要求同一个J在全部F上有 \(\|Jr\|\le K\|r\|_{H_{\log}}\)，并精确消去全部 \(P_c\)，则cyclic密度迫J=0，矛盾于537。给每个全域映射不同有限 \(K_N\) 仍使每个都为0。合法逃逸是支撑相关域／Fréchet拓扑、有费的cofinal运输，而不是把全域bounded标签换名。

## 4. 真正的紧逆极限不需要surjectivity

枚举D为 \(r_1,r_2,\ldots\)，预先从(3)–(4)或F半范数给有限 \(M_i\ge|B_W(r_i,r_i)|\)。令 \(w_{ij}=B_W(r_i,r_j)\)，选 \(\varepsilon_N\downarrow0\)。定义有限Gram空间
\[
 K_N=\{G\in\operatorname{Herm}_N:
 G\succeq0,\ G_{ii}\le M_i,
 |G_{ij}-w_{ij}|\le\varepsilon_N\ (i,j\le N)\}.            \tag{5}
\]
PSD给 \(|G_{ij}|\le\sqrt{M_iM_j}\)，故 \(K_N\) 是有限维compact集。主子矩阵截取给连续 \(K_{N+1}\to K_N\)：误差门随N收紧。**若全部 \(K_N\ne\varnothing\)，其逆极限非空；不需要这些截取映射满射。**

证明：在全部 \(K_N\) 的compact乘积上施加相邻匹配闭条件。任意有限批匹配条件取最高层点，向下截取即可，故有有限交性质。极限 \(G=(g_{ij})\) 满足 \(g_{ij}=w_{ij}\)，于是(2)。也可直接对每个固定n，取N→∞的n主子矩阵得 \(W_n\succeq0\)。

因此(5)全部非空仍恰是全Weil正性；紧性只把**联合有限可行性**升级为全局，不创造有限正号。每个孤立局部子问题各自有解、却未形成一个共同约束的实际逆系统，才不能援引该定理。不能笼统声称“非空compact逆系统还缺surjectivity／兼容性”。

允许几何额外变量时，同样可用逐坐标compact包络和闭方程：有限乘法／对合、关系同构、局部过滤评价和预算误差等都在同一有限批约束中。要先证其真实对象、闭合、包络及联合有限非空；任意逐批重选结构不等于已构成此系统。

## 5. 可实际判定的近似因子空间及它没有付款的部分

在有限源子空间 \(Y_N\) 上，令 \(H_N\) 为原Dlog Gram。可要求独立候选因子 \(A_N\) 满足
\[
 G_N=A_N^*A_N\succeq0,\qquad
 -\delta_N H_N\preceq W_N-G_N\preceq\delta_N H_N,
 \quad G_N\preceq B_NH_N.                                \tag{6}
\]
rank不固定时，任意PSD Gram均有有限因子，因子本身不增加独立内容。\(H_N\) 若有核，须先核 \(W_N\) 同样消去该实际零源核；对由同一源列表计算的真实Weil Gram，这由线性性自动成立。随后(6)在实际源商上解释；其upper及PSD也强制候选消去零源。必要量是完整operator误差，不是每个entry看起来小。

对预先固定的 \(B_N\ge0\)、\(\delta_N\ge0\)，(6)的有限可行性准确等价于
\[
 -\delta_NH_N\preceq W_N\preceq(B_N+\delta_N)H_N.          \tag{6a}
\]
必要性直接相加；充分性在实际源商上以 \(H_N^{-1/2}\) 规范化W，将其每个特征值clip到 \([0,B_N]\)，再作congruence还原，即得G满足(6)。所以固定upper门时不能只保负谱下界。若 \(Y_N\) 支撑于 \([-L,L]\)，且允许预先取足够大的 \(B_N\ge C_L+\delta_N\)，则(4)已独立支付upper门，此时才可把可行性简写为 \(W_N\succeq-\delta_NH_N\)；可直接取 \(G_N=W_N+\delta_NH_N\)。若 \(\delta_N\to0\) 且Y_N覆盖全部固定测试，(6)推出(2)；这一结论仍不提供独立的有限可行性证明。

真正的新输入应是：从有限评价det／独立局部消失与global容量构造 \(A_N\)，并从该同一源对象证明(6)和全部费用；不是先对W_N做Cholesky再称其为几何。537只付固定17/16全源窗；不能从这个旧窗证书推出任意Y_N或全部成长L可行。

若因子向量直接放无限Hilbert弱闭球，内积等式通常不闭：标准 \(e_n\rightharpoonup0\)，却 \(\langle e_n,e_n\rangle=1\)。强闭球又不compact。故此处先用Gram坐标compact化，再GNS实现；不能由weak compactness保留全部等式。有限rank／整性／Cartier有效性等附加条件也须分别核其闭性，未核时不能由Gram极限恢复。

## 6. 连续正反例：一个完整2×2空性证书

采用562真实positive primitive及g-integer族
\(Z_c(s)=1+c/[s(s-1)]\)，两pole0、1全保，模型Γ=0是其指定背景。取 \(c_-=3/16\)，则完整平衡为 \(W_-(u)=2\cosh(u/4)\)。选非零非负偶 \(\eta\in C_c^\infty\)，令
\[
 r_1=(D^2-1/4)\eta,\qquad r_2=\tau_h r_1,
 \qquad A=\int\eta(u)\cosh(u/4)du>0,
 \quad h\ne0.
\]
两个源的双pole矩均精确0。分部积分给 \(\int r_1e^{\pm u/4}=-c_-A\)，从完整源直接计算
\[
 W_{-,2}=2c_-^2A^2
 \begin{pmatrix}1&\cosh(h/4)\\\cosh(h/4)&1\end{pmatrix},
 \qquad \det W_{-,2}<0.                                  \tag{7}
\]
各自对角严格正，mixed Gram却已失败。因此正primitive、精确反射对偶、真实光滑源、非零fiber正度量均不能保证结构空间非空。负特征向量为(1,−1)，给一个实际compact双pole-zero负源。D的稠密性将其逼近为有限有理测试反证，严格负号有余量。

取 \(c_+=5/16\)，同一 \(r_1,r_2\) 配方及 \(A_+=\int\eta(u)\cos(u/4)du\ne0\)（缩小η支撑确保）给
\[
 W_{+,2}=2c_+^2A_+^2
 \begin{pmatrix}1&\cos(h/4)\\\cos(h/4)&1\end{pmatrix}.
\]
所有有限Gram均由两个显式Fourier评价的平方和PSD，全部tower可行。这不是仅对角或有限N的数值外推。正反差别来自源ODE的参数符号；不使用未知零点位置。

## 7. 函数域：有限证书如何真正支付全tower

固定曲线、q、grading、全部点数递推。563/566的实付设施是有限U及独立 \(H>0\)，
\[
 U^*HU=H,\qquad a_n=\operatorname{Tr}U^n\quad\forall n.
\]
可在 \(\operatorname{Tr}H=1\)、\(H\succeq\delta I\) 的compact切片内求解线性不变方程，\(\delta>0\)须独立给出或由显式H验证。有限递推／Cayley–Hamilton支付全部n，才由同源unitary bundle构造全测试平方和及566的all-time普通heat identity。

仅 \(H\succeq0\)、trace1不够：\(U=\operatorname{diag}(1,2)\)、\(H=\operatorname{diag}(1,0)\) 满足方程却丢掉危险第二分量。随N令正定下界 \(\delta_N\downarrow0\)，极限也会退化。必须给full coverage／observability或统一正定门。有限初始点数若没有已证明的全递推，不能外推整个tower；曲线的独立polarization／有效性／RR承担这个正号，不是其函数方程独自承担。

## 8. 566的闭形式与heat身份不会自动随存在性附送

(1)的GNS完成不是原du上的Friedrichs闭包。566已指出：即使Weil正，孤立Fourier谱原子亦使Q在原全线L²不可闭；正确正能量可存在于另一载体。不能在空间定义时同时要求原L²闭性而误排真实连续正例或经典候选。

有限正算子／strong-resolvent紧性不保完整ordinary heat trace。明确例子：在 \(\ell^2(\mathbb N)\) 令 \(K e_j=j e_j\)，\(K_n\)只把第n个特征值改为0。则 \(K_n\ge0\)、每个heat trace有限、\(K_n\to K\) strong resolvent，但
\[
 \operatorname{Tr}e^{-tK_n}
 =\operatorname{Tr}e^{-tK}-e^{-tn}+1
 \longrightarrow\operatorname{Tr}e^{-tK}+1,
\]
而非极限算子的trace。每个固定t还有统一trace upper，仍会丢逃逸质量；需额外tail tightness／trace-norm比较。

正谱测度的state trace与ordinary Hilbert trace也不同：nonatomic谱通常无有限ordinary trace；单个质量1/2的正原子给GNS一维，但ordinary trace的重数是1。要求完整谱行列式／整数重数／无额外因子时，须独立编码这些条件。一般g-integer的state／半有限版本不应被ordinary-trace公理无理由排除。

## 9. 一个有真内容的存在性路线：独立正对象的像与闭包

设 \(\mathfrak G_+\) 是不通过Q符号定义的独立几何／评价／能量对象类，每个对象由已证定理给完整正型分布 \(\Phi(G)\)。若能证明
\[
 W_\zeta\in\overline{\Phi(\mathfrak G_+)}^{\,\mathcal D'},       \tag{8}
\]
则对每个compact h，\(h*h^*\)亦compact，分布收敛给
\(W_\zeta(h*h^*)=\lim\Phi(G_n)(h*h^*)\ge0\)。这一闭锥论证完全合法；可以是有意义的新existence工具，**尚未证明的是独立对象像的membership／近似构造**。

右半平面Euler产品或prime数据收敛不足以代(8)：它没有固定或控制完整Γ/contact、分次权、全部pole及预算重整化。564已给相同整数分布可有不同完成化的反控制。若需(8)以外恢复线丛、Cartier层和容量，仍须对这些对象本身给紧性／descent／properness；574的non-Hausdorff Pic及575的flat-jets丢失说明不能只用有限Taylor坐标compact化就自称得到真实移动族。

## 10. 分支结算范围

本分支支付的是存在性方案的准确量词、可数测试、compact性适用范围及便宜负控制。所有核心结论为标准工具或旧562–566的直接完整消费；2×2式(7)是旧连续模型的显式重排，不登记新经典input或新研究轮。

当前可选的真正新任务是：提出一个不以Q／零点标签定义的具体有限设施类，独立支付其全部联合有限可行性和逐坐标包络，或给(8)的完整分布近似。不再反复更名“正结构存在”；在没有这些输入前，不启动未知existence数学合同。

原du／Dlog fixed窗upper和Fréchet连续性已准确保留；全主关系、537非根、全complex mixed、完整Γ/contact、全部prime powers和双pole均未删除。强旧actual whole4/5、成长core／coupling／Ξ与独立mixed容量瓶颈未变。

本轮核对的primary来源入口：[Connes–Consani–Marcolli 2007](https://arxiv.org/abs/math/0703392)明确区分谱实现／trace pairing和RH等价正性；[Alpay–Jorgensen](https://arxiv.org/abs/1109.5273)为奇异谱测度及原L²可闭性背景，具体已付结论见566；[Egger–Steiner](https://arxiv.org/abs/1104.1364)为无限图strong-resolvent／trace研究原件，本文第8节逃逸反例由此处直接计算，不归该论文。
