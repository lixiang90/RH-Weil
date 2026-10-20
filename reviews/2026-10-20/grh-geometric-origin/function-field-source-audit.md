# 函数域正性的来源审查：交数、section预算、Rosati与Deligne

2026-10-20；独立来源原稿，供root逐前件消费。固定G20261014／0c4f≤538；
不改STATE、不自行启动或结算合同。对象是光滑射影几何连通曲线C/F_q。
本稿恢复已知几何机制并展开同源Gram恒等式，不声称新的函数域RH证明。

## 1. 来源与逻辑边界

技术来源已浏览作者原件[Milne，The Riemann Hypothesis](https://jmilne.org/math/xnotes/pRH.pdf)：
Thms1.2、1.5、Cor1.6及§Correspondences（印刷8–11页），Thms1.27–1.30
（21–22页），以及§3标准猜想与§5 Deligne证明。
几何基础给Hodge index；下面§2–4是把这些输入代入同一Frobenius图后的代数推导。
Rosati路线恢复至ample交数；其trace、对偶与Frobenius身份来自同一几何对象。

高维证明另核[Deligne原文，Weil I](https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf)，
§3 Thm3.2及Lemmas3.3–3.6、§§4–7。其高维纯性证明不以一般标准Hodge正性为前提。
不得把已证Weil猜想等同于一般标准猜想已证，亦不得由纯性单独推出原Frobenius半单。

## 2. Hodge index之前：为什么负号可以独立支付

在代数闭域k上的光滑射影整曲面S上（H0(O_S)=k），以h0(D)=dim H0(S,O(D))记section数，K为canonical class，
H为任一给定射影嵌入的hyperplane class。几何独立给：

1. 所有h0(D)有限；非零section乘法无零因子，故h0(E)>0时h0(E+F)≥h0(F)。
2. h0(D)>1推出D线性等价于非零有效除子，因而D·H>0。
   后一步来自正维projective曲线与hyperplane适当相交时的非空性及局部交重数非负。
3. surface Riemann–Roch和Serre duality、h1≥0给

   h0(nD)+h0(K−nD) ≥ χ(O_S)+(n²D²−nD·K)/2.

设D·H=0。第2项同时给h0(nD)≤1和h0(−nD)≤1。
若D²>0，第3项分别对n、−n使用，得到h0(K−nD)、h0(K+nD)均为cn²−O_D(n)以上。
当n充分大，两者均非零；选0≠s∈H0(K+nD)，乘法给

    H0(K−nD) --×s--> H0(2K)

单射。左边维数趋∞，右边固定有限，矛盾。因此D²≤0。

这条证明不使用零点、纯性、未知正H，也不要求H本身光滑；无需额外Bertini。
真正源输入是Riemann–Roch的二次系数、有效性的degree约束、section乘法与一个固定容量h0(2K)。
将其写成一般分析条件时，不能只给同名h0符号，必须构造实际section空间及乘法/预算。

若坚持直接使用固定degree统一上界，可另外选smooth integral veryample H并付Bertini；
对E·H=d，restriction及曲线上h0(L)≤max(0,deg L+1)反复给

    h0(E) ≤ Σ_{j≥0} max(0,d−jH²+1).

因负ample degree的有效除子不存在，右边只有有限项。这是另一个合法证明，
但增加了smooth integral hyperplane的来源责任，非上一证明所需。

## 3. 从全部对应的交数到完整点数Gram

在S=C_k×C_k，k为F_q的代数闭包，固定

    F1=C×pt，F2=pt×C，F1²=F2²=0，F1·F2=1；
    d_i(D)=D·F_i，D°=D−d2(D)F1−d1(D)F2。

于是D°·F1=D°·F2=0。上一节作用于H的ample正倍数，或直接由Hodge index的index-one推论，给

    I(D,E)=−D°·E°
          =d1(D)d2(E)+d2(D)d1(E)−D·E，
    I(D,D)≥0。

此处H=F1+F2是ample divisor；可取足够正倍数为veryample。对复系数作Hermitian延拓。
对应composition的交数规则又给

    σ(D)=d1(D)+d2(D)−D·Δ，
    σ(D∘D^t)=I(D,D)。

因此Weil正性中的transpose来自交换两个几何因子，trace来自同一个diagonal交数；
其正号来源为上一节的几何预算，不是另选一个与点数无关的Hilbert内积。

令Γ_n为q-Frobenius的第n次幂的graph，n≥0。几何先给

    d1(Γ_n)=q^n，d2(Γ_n)=1，Γ_n²=(2−2g)q^n。

自交式由graph≅C、曲面adjunction直接推出。若0≤m<n，则

    Γ_m·Γ_n=q^m N_{n−m}。

这里F^{n−m}−id的固定点是C(F_{q^{n−m}})，局部差的导数为−id，固定点交重数1；
共同复合F^m后，局部uniformizer差被提升为q^m次幂，交重数恰q^m。
不可仅按固定点集合计数而漏此inseparable重数。

置v_n=q^{−n/2}Γ_n°，a0=2g，a_r=q^{−r/2}(q^r+1−N_r)，a_{−r}=a_r。直接代入即得

    I(v_m,v_n)=a_{n−m}，m,n≥0。

对n=m，contact a0由graph自交而非人为补常数给出。
任意有限整数指标可整体平移成非负指标，故每个有限Toeplitz矩阵(a_{j−k})均为这个交数的Gram。
先取得全部complex系数正性，再从点数/有理性识别非平凡zeta部分；不存在从根反造Gram的步骤。

## 4. 与全周期Weil源的精确衔接

采用563中已核的完成化与所有周期pole，令L=log q，

    W_C=L Σ_{n∈Z} a_n δ_{nL}。

对每个g∈Cc∞(R;C)，按x=y+kL分割积分，得到

    W_C(g*g*)
      =L∫_0^L Σ_{k,l∈Z} g(y+kL) overline{g(y+lL)} a_{k−l}dy ≥0。

每个y只有有限项，compact support给统一有限指标范围，不需未经控制的无穷交数求和。
全部proper powers在N_n中，全周期pole/contact在W_C中；这不是只保一个fundamental spectral strip。

此identity说明曲线几何为何付出完整Weil正性；并未产生新的classical Γ来源。
它也不允许把cyclic correspondence Gram空间的维数冒充2g的ordinary-trace重数：
Frobenius有重特征值时，cyclic Gram载体可比原Tate空间小。若要566的ordinary heat trace，
应继续使用全部点数对应的原2g维trace/完整递推，保重数，不按Gram核商后的维数重算。

## 5. Rosati路线：正性与q缩放是两笔独立费用

Jac(C)的canonical ample polarization给λ及α†=λ^{-1}α∨λ。
令A为任一有定义于F_q的polarization的abelian variety，维数g_A。
其characteristic/Tate trace满足

    Tr(αα†)=(2g_A)/(D^{g_A}) · (D^{g_A−1}·α*D)>0，α≠0。

这里D为相应ample class；正性来自实际ample交数。另由Weil pairing的Frobenius相容性
及Tate作用的忠实性给F†F=qI。后者单独只是非退化对偶中的similitude；
前者才排除双曲的互反谱。二者合并给normalized F的正极化和纯性。
Jacobian trace与曲线的对应trace/全部N_n相合，因而不是对另一个对象证明正性。

曲线交数路线与Jacobian Rosati路线是同一正性机制的两种实现在此范围内相接；
307已由椭圆同态degree把这条来源逐项具体化，001已有抽象充分定理。
本次将其恢复为全部曲线的source责任清单，不重计旧抽象定理或旧genus-one能量。

## 6. 高维Deligne：tensor positivity与全局pole预算

Deligne Weil I §3的原始链是：U0是P1/F_q的非空有限去点开集，F0为其上非零lisse Q_l-sheaf，
l≠char(F_q)，有非退化交替配对F0⊗F0→Q_l(−β)，β∈Z；
几何π1的像在相应symplectic group中为open subgroup，且每个闭点的局部characteristic polynomial有理。
全部even tensor powers的局部幂迹为(Tr F_x^n)^{2k}≥0；
monodromy识别tensor coinvariants，cohomological trace formula精确控制全局tensor L函数的pole；
非负系数的收敛半径比较给|α_x|≤q_x^{β/2+1/(2k)}，k→∞并用对偶给纯性。
这里q_x=q^{deg x}，局部α_x来自同一F0的闭点Frobenius，非整个base的全球zeta零点。
Lefschetz pencils及rationality步骤将此输入应用于一般smooth projective variety。

值得迁移的是“全部tensor阶的正系数＋独立全局pole预算”这对接口；
bare正Euler只支付前一类计数正性，不支付tensor coinvariant或pole位置。
假设所构造tensor L函数已满足所需pole界，却无独立来源，只是把纯性责任换地方。

一般高维Hodge standard conjecture、所有原Frobenius半单，不是Weil猜想已证的自动后果。
旧073 §7首项若被读为一般有限域对象已有Hodge–Riemann positive exact/strong package，会过强；
应限于已独立给正极化的类，或仅将一般高维结论记录为Deligne已证weight purity。
001的PLF是条件定理，307已明确奇次J_a须另付，本稿不消费073的过宽读法。

## 7. 推广到g-integers时的准确准入与负对照

可迁移的输入不必是literal scheme，但至少须有独立定义的对应/section系统，
其Riemann–Roch二次系数、effective degree及section容量经过证明；
再有同一source的exact map将完整Weil pairing识别为primitive负交数。
只把I定义为−Q_W再假设它满足Hodge index，是Weil正性的改名。
只定义一个positive closure再猜trace，则重蹈566非酉端点/自动平方的反测试。

290有真正正整数closed-point Euler、全次数trace、Poincare及formal HL，却没有上述实际section预算。
q=5时a0=2，a1=√5，故2×2 Toeplitz Gram det=4−5=−1；
它不可能成为正primitive交数Gram，尽管N_n和全部primitive closed-point counts均正。
这清楚标出有效性必须强于“原始closed-point质量非负”。

连续Z_c正反段的原始P/Π/M同样为正，局部守恒能量阈值c≥1/4由563已付；
其正段可给分析对应载体，但尚未构造来自P本身的独立section/RR结构。
允许连续载体、无限维及distributional trace以免错误排除classical ζ，
却必须重付全部Γ/contact/prime powers/pole的same-source identity与极限域。

最强旧比较：001/002已有“正极化＋迹公式⇒纯性”及循环审计；073已有双向subexponential机制；
307已有真实genus-one degree来源；563有全周期Gram lift，566有闭form/heat lift。
更强的直接前件已在[363§5](../../../notes/363-f1-arithmetic-geometry-and-existence-audit.md)保存：
Connes–Consani 2018 §3已将实际s(f,f)解释为自交，列出RR截面存在、非零有效性、
双degree相容及完整有限部分/边界身份责任。因此“RR⇒Hodge index⇒RH”策略及这些责任并非本次新输入。
本原稿只作前端section固定容量付款和全图交数到全点数Gram的经典机制展开。
没有新增classic ζ的独立正性、whole4/5/core/coupling改善；是否成立新的RR分析准入由root另审。

停止条件：若无法给由实际g-integer分布构造的section容量、或能改变具体候选选择的新同源测试，
在此来源章节停止，不以unknown H、unknown K、unknown tensor pole budget再开数学合同。

## 8. root提出的有限容量RR接口：独立代数核验

本节核验root提出的量化综合，不把该条件接口登记为classical ζ的新独立输入。
对每个cutoff j，给实际section维数l_j(E)∈Z_{≥0}，均有限，
以及同一系统的K_j、D_j和整数n_j≥1。要求非零section乘法为单射，
特别是两侧K_j±n_jD_j相加确为同一2K_j，不能混用不同cutoff或不同正规化。
置C_j=l_j(2K_j)，并假定

    l_j(n_jD_j)≤a_j，l_j(−n_jD_j)≤a_j，
    l_j(±n_jD_j)+l_j(K_j∓n_jD_j)
      ≥χ_j+n_j²d_j/2∓n_jb_j/2−ε_j，
    d_j=D_j²，b_j=D_j·K_j，ε_j≥0。

a_j为已支付上界，d_j、b_j为相同quadratic/linear RR系数；ε_j须控制两种符号的全部剩余误差。
记x_j=l_j(K_j−n_jD_j)，y_j=l_j(K_j+n_jD_j)。若二者都正，
选另一侧任一非零section相乘，分别给x_j≤C_j、y_j≤C_j；
若某侧为零，则直接有min(x_j,y_j)=0≤C_j。因此总有

    min(x_j,y_j)≤C_j。

RR及a_j上界同时给

    x_j≥χ_j+n_j²d_j/2−n_jb_j/2−ε_j−a_j，
    y_j≥χ_j+n_j²d_j/2+n_jb_j/2−ε_j−a_j。

两式取min，联立上述容量界，得到精确量化结论

    d_j ≤ [2(C_j+a_j+ε_j−χ_j)+n_j|b_j|]/n_j²。       (RR-budget)

该证明只使用这个单一整数n_j的两条RR不等式，不要求先证明每个cutoff上的完整Hodge index。
若对每个固定测试g，实际同源source识别独立给d_j(g)→−Q_W(g)，且(RR-budget)右边→0，
便得Q_W(g)≥0。cutoff和n_j可依赖固定g；无须先给所有g一致的数值预算。
C_j本身允许趋∞，只要连同a_j、ε_j、χ_j及n_j|b_j|的实际总上界归一化后趋0。
不得把未经证明的误差、负χ_j的增长或degree缺陷从此右边删掉。

实际sections通常定义于integral divisor或清分母后的rational real class。
若只支付实测试的D_j(g)，不能自动声称覆盖全部complex测试。
在本研究经典的实偶W类，g=g_R+ig_I给Q_W(g)=Q_W(g_R)+Q_W(g_I)，因此实测试覆盖可扩充；
一般仅Hermitian而非实偶的分布可能有交叉项，需要额外complex source构造或准确Hermitian极化。
从rational稠密测试扩充至smooth测试，还须核目标W的分布连续性和近似域，不能仅以section记号略过。

相对363§5，新增内容限于：把既有RR/effectivity责任压成single-scale、允许增长容量的可量化充分预算。
它没有构造任何尚缺的g-integer section空间，没有证明其乘法、RR余项或同一完整Γ/pp/pole source识别。
若这些前件不能独立支付，该式只是准确的conditional迁移接口，不是新的独立正性或RH证明。
