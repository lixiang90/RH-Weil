# Li–Liu实际高度身份：余下前提、规范与physical消费范围

2026-10-28；/root/unit_height独占原稿，执行[唯一unitary前提来源门](../causal-strategy/next-unitary-modularity-premise-gate.md)。同G20261027／原0c4f基线；C047预算已耗，不预C048/585，不改STATE/cadence/Git。这里只核固定原件中必要定义和定理陈述，模性前提的Raum§5运输由独占modularity稿/root另消费；本稿出稿不代root/fresh验收。

## 1. 固定版本与实际阅读范围

原件为Chao Li–Yifeng Liu，[*Chow groups and L-derivatives of automorphic motives for unitary groups*](https://arxiv.org/abs/2006.06139v5)，arXiv2006.06139v5，66页／1263440字节／raw SHA256 `b3705e15817c142a2319660f12b07bf3871e13389d6d5557397c776809cec289`。本轮没有新下载、外部网页或引文读取，不将HTML动态日期混作版本日。

实际核读并完整目视PDF4–7（Assumption1.3、root-number设置、Th1.7及说明）、24–25（Hyp4.5、Prop4.7陈述和Def4.8）、30–32（Hyp6.6/Rem6.7、Prop6.10陈述、Def6.11）。为规范补读必要定义：PDF10–11的moment／Schwartz／nearby空间；PDF13–16的复共轭、对偶、CH域、Ass3.1和local doubling定义；PDF18的Def3.8／Rem3.9；PDF28的§6高度引言。另完整目视PDF10、18、28。整页提取/显示带有相邻proof片段，本稿未审核或消费这些证明，也未审Li–Liu§3–11整章proof；不把页级定位扫描当全文已读。

新渲染缓存均在本地忽略的原文目录，前缀`uh-`；既有PDF6–7渲染也复用。没有改变原PDF。

## 2. 删除Hyp4.5不等于删除其余设置

Th1.7在固定v5中仍以Assumption1.3、奇数个almost-unramified inert places以及Hyp6.6为前件。Assumption1.3实际要求：

* CM扩张E/F在有限位无ramification，全部2-adic places在E中split；文中明确推出[F:Q]为偶数。
* π为G_r=U(r,r)上的cuspidal automorphic representation，n=2r；无穷位是规定Harish–Chandra参数的holomorphic discrete series，split有限位为principal series，inert位为unramified或指定almost-unramified，后者还附基域在该位对Q不分歧的条件；所有有限位tempered。
* S_π为almost-unramified inert places的集合。原根数为ε(π)=(-1)^(r[F:Q]+|S_π|)，因此在本设置下|S_π|奇使根数为-1，V_π为totally positive definite incoherent hermitian空间。

这些不是本项目k=Q(√-7)、F=Q的原native模型已满足的条件，也不能因Raum适用于广的CM字段便无声扩大Li–Liu v5定理。Remark1.4提及可由其他工作减条件，本门不追这些证明或把这些提示作已经支付的升级。

Hyp6.6是关于中间度2r-1的π-nearly-isotypic ℓ-adic cohomology及Galois表示半单化的准确比较，不是模性假设的另一名称。固定v5 Rem6.7对n=2给cited已知情形，对更一般情形指向分类/KSZ输入；本次没有核这些外部proof或更新其当前证明状态。因此它按来源前件保留，不能由Corollary B自动去掉。

## 3. 真正的theta映射、复线性方向和CH域

Hyp4.5(PDF24)的量词是每个compact open L、每个L不变的有限adelic Bruhat–Schwartz φ^∞、每个代数C-linear functional l:CH^m(X_L)_C→C，标量生成级数绝对收敛并有规定模性。其条件不是预先给CH范数；也没有断言整个Chow群有限维。Prop4.7的结论为每个输入生成级数落入代数有限tensor，足以解释下面的CH值积分。Raum是否按全部原量词支付该前件，须随另一原稿/root的实际运输范围消费。

Def4.8的实际公式是

\[
 \Theta_{\phi^\infty}(\varphi)_L
  =\int_{G_r(F)\backslash G_r(\mathbb A_F)}
       \varphi^{\mathtt c}(g)\,Z_{\phi^\infty}(g)_L\,dg
       \in\mathrm{CH}^r(X_L)_\mathbb C.
\]

这里varphi为规定automorphic lowest-weight空间中的向量；phi^∞是另一个有限adelicSchwartz输入。Theta对varphi反线性，对phi^∞线性，不能把两者混成一个任意physical源。其在colim_L CH^r(X_L)_C中的类与选取的固定L相容；这不是已构造的r↦Theta物理源map或无费用的cofinal逼近。

Prop6.10陈述在相应L=L_R L^R、F≠Q及π/Hecke设置下使该类落入CH^r(X_L)^0_C；在Hyp6.6下还落入定义高度所需CH^r(X_L)^⟨ℓ⟩_C（ℓ须R-good）。Notation2.5中后者按所有有限位的ℓ-adic cycle class消失定义，包含于de Rham同调平凡CH^r0。不能把“同调平凡”或primitive-type位置当给定源的非零性、严格正高度或整截面容量。

必要归一化另有一处不可省略：Li–Liu Notation2.2(H1)的moment为T_LL(x)=((x_i,x_j)_V)，不另乘1/2；arch Gaussian为exp(-2πtrT_LL(x))，Fourier使用同一hermitian form／ψ_E及self-dual Haar。若与Raum的半Gram记号匹配，须明示form／Weil representation／dual-lattice字典，而非同字母直接代入；该完整运输属另一稿/root范围。

## 4. Height规范、local因子与真实符号

PDF28 §6引言先取F≠Q（X_L projective），在适当good ℓ上构造Beilinson型高度

\[
 \langle\ ,\ \rangle^\ell_{X_L,E}:
 \mathrm{CH}^r(X_L)^{\langle\ell\rangle}_\mathbb C
 \times\mathrm{CH}^r(X_L)^{\langle\ell\rangle}_\mathbb C
 \longrightarrow\mathbb C\otimes_\mathbb Q\mathbb Q_\ell,
\]

第一变量C-linear，conjugate symmetric，因此第二变量反线性。本文用这个确切规范，不把它当原Pet积或在所有Chow类上已定义的PSD范数。

Def3.8(PDF18)先以Whittaker归一化定各H(F_v)上的dh_v，再取

\[
 d^\natural h=b_{2r}(0)^{-1}\prod_vdh_v,
 \qquad\operatorname{vol}^{\natural}(L)
   =\operatorname{vol}_{d^\natural h}(H(F_\infty)L).
\]

Def6.11(PDF32)的level-independent量是

\[
 \langle\Theta_1,\Theta_2\rangle^\natural_{X,E}
 =\operatorname{vol}^{\natural}(L)
   \langle\Theta_{1,L},\Theta_{2,L}\rangle^\ell_{X_L,E}.
\]

是**乘volume**而非除volume；level独立由原projection formula陈述保证，不能据此免费选择发散Gram权或搬运此前未平均Pet的统一du费用。严格说初值在C⊗Q Q_ℓ；Th1.7及其脚注对其所计算的pairing给落C并与ℓ无关的后果，不能先推广为所有Chow高度均有这个性质。

Th1.7的确切mixed形式为

\[
 \langle\Theta_{\phi_1^\infty}(\varphi_1),
        \Theta_{\phi_2^\infty}(\varphi_2)\rangle^\natural_{X,E}
 =\frac{L'(1/2,\pi)}{b_{2r}(0)}\,
      C_r^{[F:\mathbb Q]}
      \prod_{v\text{ finite}}\mathfrak Z^\natural_{\pi_v,V_v}
       (\varphi_{1v}^{\mathtt c},\varphi_{2v},
        \phi_{1v}^\infty\otimes(\phi_{2v}^\infty)^{\mathtt c}).
\]

无穷位的两个test vectors须最低weight且满足原配对归一化⟨varphi_1v^c,varphi_2v⟩_(π_v)=1；有限Schwartz为原纯tensor输入。第一automorphic腿的c与第二finite腿的c保持不同角色。PDF15–16将π^∨实现于V_π^c，tautological pairing为π_v^∨×π_v→C；局部归一化为Z^natural=(L(s+1/2,π_v)/b_(2r,v)(s))^(-1)Z，取s=0，不能用未归一化local项替换。Th1.7说明几乎所有有限位因子为1。

其中b_(2r)(0)>0，而

\[
 C_r=(-1)^r2^{r(r-1)}\pi^{r^2}
       \frac{\Gamma(1)\cdots\Gamma(r)}
            {\Gamma(r+1)\cdots\Gamma(2r)}.
\]

**必须同时消费Assumption1.3的[F:Q]偶数条件：本公式实际出现的C_r^[F:Q]为正。** 不能拿r奇时raw C_r<0制造一个不存在的全局负号反测。另一方面，列出此positive prefactor并不支付normalized height的全域PSD、各mixed local项的统一正号、或L′的独立号；这些须有自己的定理/域，不能从“inner product”字样自动取得。

Th1.7(2)在其全部设置及L′(1/2,π)≠0时给相应theta representation到colimCH^r0的Hom非零。这是有条件、且关于某些适当数据的非零设施；不是任意varphi/phi像均非零，不是已经核过本项目某个537源的非根。

## 5. 与本项目原physical源的准确比较

这个L(s,π)是原doubling／standard base-change L函数，原无穷因子有n=2r的规定参数；不能冒充完整经典Qζ。既有source如果要进入这里，至少要给具体map

\[
 r\longmapsto (\varphi(r),\phi^\infty(r))
 \longmapsto\Theta_{\phi^\infty(r)}(\varphi(r)),
\]

并核它确在这些automorphic／Schwartz／level和cohomological域中，是否线性/可极化，全部真实405关系成为principal或mixed根、537非根及whole coverage、原du／zero-extensionDlog或强源费用、完整Γ/contact／properpowers／双pole比较。原文没有给这条本项目physical map；不能把Hyp4.5的每个Chow dual量词反向误认成任意physical r均可作输入。

[582及当前根收据](../../2026-10-23/full-weil-domain/root-consumption-scope.json)已经支付fixed原native模型的S0／A1强域、全局部Weil作用和某些原du/强费用，但**没有把原Bruhat域恢复**，也没有延拓全Eisenstein总和、cycle或height functor。它的原字段F=Q和k=Q(√-7)更不自动符合这里Assumption1.3的CM/有限不分歧/[F:Q]偶数设置。局部strong域合法不等同新的finiteSchwartz输入或新unitary算术映射。

同样，arch T*r的Gaussian加权源虽有真实强费，也未证明仍是这里固定最低weight的cusp向量；原Green／scalar源并未自动成为CH^r0类。Raum的modularity是实际重要前提，但不提供这些未给的norm／primitive／physical运输。原literal及整体orthogonal Theta/7.4冻结不会被unitary新来源解冻。

这些都是当前消费缺口，不是由“另一个L函数”推导所有未来比较不可能；不同实际relative／higher载体、有费unbounded/source-adaptive和非逐层Pan正D′仍保持合法，须另有实物。

## 6. 净值与本单门停止

本稿确认的是一个真实算术mixed高度设施的准确设置及规范；是否已用Raum付款Hyp4.5仍随modularity稿/root范围。此处没有新的经典完整signed／primitive物理桥、成长core/coupling/Ξ输入，也没有全方法类边界；542＋555→557 whole leading4/5仍仅负惯性UPPER。

建议按**指定来源／标准前件核查0数学轮**消费，保原cadence2／历史48／cycle16。单门章末如仅得上述L′(π)高度设施而没有本项目实际运输，则停止本recipe，不续rank/level/weight/后章/paper，不捏cofinalheight族或新数学合同；不能以source0隐藏以后若真正出现的新完整运输结果。长期Goal仍open。
