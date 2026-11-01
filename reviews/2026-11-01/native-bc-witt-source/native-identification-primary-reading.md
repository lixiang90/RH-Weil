# Native BC／Witt identification：真实原生设施，经典源首门SOURCE0

2026-11-01；/root/bc72_primary_reader。独立SOURCE阅读稿，非ROOT消费、原创定理或新数学合同。SAME Goal1793085111/0c4f、C069 spent、cadence0/history70/latest606/formal22由当前恢复入口保留；本稿不修改这些状态。

## 1. 字节、范围及抽取纠正

原件为本次publisher PDF `connes-consani-emss64.pdf`，29页、3328150B，SHA256 **72a0bb1785f593cb447435812278379db471ce4b17944ed02fb85a2011465d60**，已现场核。严格使用ROOT在proof前保存的reading-scope-freeze：PDF7底§3 heading至PDF15上段§4之前，印453底–461上段；消费§3.1–3.4、3.11/3.12及直接论证。Theorem3.1和Almkvist背景只cited，不追[20]或其他引用。

文字抽取8–14完整，7底及15顶补读；共享120dpi PNG7–15逐页目视公式。另用唯一300dpi crop核PDF8系数字形，随后删除。**原文为Sbar=overline(mathbb S)，不是bar Z。** pdftotext把黑板S编码/显示成Zx；本分支最初随抽取发出的barZ简称已经通知ROOT纠正。以下Sbar始终指S-algebra S[M]，不是ordinary整数的代数闭包、Zbar或数域整数环。

曝光隔离：为定位最少BC定义，整页抽取PDF4–7，4–7的§1尾/§2 survey有机器曝光，但只消费7底integral Hecke/coefficient/两运算定义；这些已足够本识别，未从survey消费Weil主张。PDF15初次First42行抽取意外露出§4 heading及opening工具说明到首次map开头；完整页目视又曝光同页§4 intro及map。它们未被用于数学判断，未读§4证明/Schwarzian/spectral/ref，未顺读PDF16或其他版本。xref333 reconstruction warning的风险通过实际公式目视处理，原件未修复或改写。

## 2. 源对象、系数和相似关系

§3开头的integral BC模型是

    H_Z=Z[Q/Z] ⋊ N,
    sigma_n(e(r))=e(nr),
    rhoTilde_n(e(r))=Σ_{ns=r} e(s),    n≥1.

rhoTilde未除以n，是线性transfer，不是与sigma互为严格逆的unital ring endomorphism。这里e(r)为group-ring基元，e(r)e(s)=e(r+s)，系数是整数。

PDF8定义M=(Q/Z)_+，其中*为吸收零，M非零元为抽象roots of unity e(r)。Sbar=S[M]作为Gamma-op到pointed sets的functor为Sbar[X]=X∧M；乘法由M乘法给出。使用的有限free对象是E=Sbar[F]=Sbar∧F，F为finite pointed set。S-modules S[F](X)=F∧X及Lemma3.2的自然变换描述是本节的基础；本门没有从“绝对代数闭包”措辞新增一套普通scheme公理。

Prop3.4把End_{Sbar}(Sbar[n_+])与Mat_n^R(Sbar)对应：entries取M、**每列至多一个非零元**；矩阵乘法每个位置至多一个实际非零乘积，不须在M中定义普通加法。Mat_n^L每行至多一个非零；无稀疏限制的Mat_n(Sbar)则是左右matrix S-algebra的bimodule，不等同于原End。

Def3.6将alpha∈Mat_n(Sbar)称invertible，条件是它在**所有field extensions k of Sbar**中成为可逆k矩阵；field extension来自injective M→k。不能改读为alpha具有Sbar-native End逆或为某整数格上的unimodular矩阵。Def3.8的similarity正使用这类bimodule矩阵alpha和intertwining relation gamma alpha=alpha mu；证明中的Fourier矩阵因此合法，但其合法性不是原native End中“unit矩阵”的结论。

## 3. W0及universal invariant的准确含义

本节处理的是endomorphisms的Almkvist型universal ring **W0(Sbar)**，具体由Def3.8的invariant描述；不是ordinary K1、relative K0连接类或已识别的整个higher K-spectrum。一个invariant chi:Mat_*^R(Sbar)→R（R commutative ring）满足：

    chi(E,T)=chi(T(E),T)；
    wedge/direct-sum给加法，relative-smash/tensor给乘法；
    对Def3.6的similarity不变。

第一项除去nilpotent/transient部分；第二项实现环运算；第三项是本节特别指定的相似关系。不要无声替换为任意exact category的通常K0呈现。负整数是universal ring/group completion层的元素，有限实际(E,T)的非零特征值除子本身带非负multiplicities；roots of unity为basis labels，不是任意复数multiplicity。

Prop3.9取injective kappa:M→k，k为characteristic0的algebraically closed extension。先把T变为k矩阵，再取Almkvist nonzero-eigenvalue divisor并拉回abstract root labels：

    tau:Mat_*^R(Sbar)→Z[Q/Z],   tau(T)=kappa^{-1}(D_T).

本节给出的理由是稳定像上的weighted permutation具有有限阶，非零eigenvalues全为roots of unity；所得abstract divisor不依赖kappa。Nilpotent branches被trim，wedge/tensor和field similarity的性质来自Almkvist invariant。该上游性质本门按cited使用，未重新打开其证明。

3.1只引用[20,Th2.3]：W0(S)识别为Z[Q/Z]在Aut(Q/Z)=Zhat^×作用下的invariant part。**3.11不是只指向外文献**：本节有实际完整的关键归约及Fourier论证；其声明为

    W0(Sbar) ≅ Z[Q/Z],  tau universal,

并扩展3.1的additive invariant。对任意chi，令beta(r)=chi([e(r)])；trim稳定像后分解成weighted cycles，再经diagonal root rescaling写成e(s)C(m)，最后经Fourier similarity化成e(s)Delta(m)。由additivity/multiplicativity得chi=beta∘tau，一维[e(r)]给唯一性和所有group-ring generators。

一项规范范围需保留：Def3.8字面三条未另列chi([e(0)])=1，而3.11 proof写beta:Q/Z→R^×并延成ring homomorphism。本门按作者native universal statement及其通常unital目标约定记录，**不宣称独立补齐这项约定**；也不据此宣布作者erratum或扩读[20]。若容许非unital chi，相关表达须在chi(1)的idempotent corner中解释。经典物理源首门不依赖此规范问题。

## 4. Fourier与F／V的方向、因子及非零generator

Prop3.10的实际矩阵为

    C(n)_{ij}=1 (i≡j+1 mod n),  其余0；
    Delta(n)_{jj}=e(j/n),
    V_{ij}=e(ij/n),  W_{ij}=e(-ij/n),
    Delta(n)V=VC(n),  C(n)W=WDelta(n).

在field extension中n≠0、V^{-1}=W/n；这是代数Fourier intertwining。V一般非Mat^R矩阵，1/n只在field逆中出现，不能由此取得native integral inverse、physical Fourier Plancherel或du/Dlog等距。

§3.4在endomorphism pairs上定义

    F_n(E,T)=(E,T^n),
    V_n(E,T)=n份E的循环置换，最后一次用T闭回第一份。

视觉核(5)–(8)：

    tau(F_n x)=sigma_n(tau x),
    tau(V_n x)=rhoTilde_n(tau x).

F_n为ring endomorphism，V_n为additive transfer。因子方向在原整系数上是sigma_n rhoTilde_n=n Id，而rhoTilde_n sigma_n(e(r))=Σ_{nk=0}e(r+k)；不是两边都等于Id。未引入概率归一1/n。

实际一维T_r=[e(r)]有tau(T_r)=e(r)≠0。取r=0、n=2，V_2(T_0)为rank2 cyclic permutation，tau=e(0)+e(1/2)；其F_2为rank2 identity，tau=2e(0)。这个非零generator检查在同一root-coefficient类别内验证F/V方向及整数2，未运行数值或把这些root标签当物理primepower权。

Theorem3.12在(5)–(8)之后声明integral BC-system H_Z与**endowed with F/V的W0(Sbar)**的canonical identification，correspondences为sigma_n→F_n、rhoTilde_n→V_n。准确消费为“系数环识别＋指定F/V运算的structured comparison”；**不称非交换crossed-product H_Z与裸交换环W0(Sbar)同构**。本门核本节显示的intertwining及direct argument，不独立重建上游完整Hecke presentation／所有analytic representations。

## 5. 与最强旧的净关系和首门止点

这确实是365的C[R_+^×]半线性系数、Deninger rational-Witt flow、CCM KK/perfect/Todd或ordinary K1→relativeK0之外的**实际native arithmetic facility**。不能把旧unit连接类0或573 ideal反测跨对象移来抹去它；本节也没有用Q_zeta数值定义tau，故不只是574 Q-marker换名。

但本节的输入为finite pointed sets及root-weighted sparse endomorphisms，range为整系数group-ring invariant和F/V运算；没有实际rho=e^{u/2}f的全complex S_exp源公式、405 full noncompact Pan及平移的principal/isomorphism消去、537到全源coverage，也没有原du／zero-extension Dlog或强源/尾/增长运输。其“divisor”是特征值的abstract root divisor，不是已经建成的算术曲面Cartier divisor。整数multiplicity、F/V和可逆field Fourier都不自动给同一整对象的sections、filtered capacity、RR／Hodge正号。

尤其没有在本授权段将native运算识别为SAME complete Hermitian Weil mixed form：Gamma/contact、全部proper powers的实际weights、双pole及growth/coupling均仍open。n可遍历正整数不等于这些项已由source matching支付。原文§2/§4 survey的Weil角色不在本门补证范围内，也不由它自动续另一章。

因此建议 **native identification cited/checked in stated scope；SOURCE0 for classical core**。停止只针对这份指定来源门没有different actual physical entry，不是Witt／BC／higher或source-adaptive方法的普遍边界。无新whole/core/coupling/Xi后果，最强旧whole17/16、9/8 head及SAME605补空间正完成、whole4/5负惯性UPPER保持；三Goal门与实际瓶颈不变。不续§4／引用／来源／新公式，不建C070/607，不消费cadence。ROOT须结合独立审查决定最终范围。
