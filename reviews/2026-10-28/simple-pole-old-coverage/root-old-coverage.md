# simple poles、留数质量与旧561的完整覆盖

2026-10-28；G20261027/runtime1793085111/原0c4f。执行上一唯一next-simple-pole-old-classification-admission的实际旧覆盖比较。此处仅重闭已知正测度、Fourier/Mellin和561的依赖，不建C050/587或新数学轮。两独占稿及独立fresh另按根收据绑定；本稿不把任一未核代理稿当输入。

## 1. 原对象及唯一明示增长域

Π≥0在(0,∞)，某实σ0使K0=∫e^(−σ0u)dΠ<∞；M=exp_*Π，Z(s)=LM(s)。N=(u→e^u)_*M。给真实右半面germ Λ(s)=π^(−s/2)Γ(s/2)Z(s)的全域亚纯延拓、Λ(s)=Λ(1−s)，实际简单poles恰为0和1，留数−A、A。

另外给一个c>max(σ0,1)，以及C,N0,T0,η>0，使σ∈[1−c,c]、|τ|≥T0时

 |Λ(σ+iτ)|≤C(1+|τ|)^N0 exp(−η|τ|)。

这是本次类别的原前件；不从正Π/FE/finite order自动制造它。不弱化finite order、不扩PL证明，不续Hamburger或任何paper。以下全为每个先给对象、全部t>0的精确结论，没有全族统一C或原physical全du/Dlog费用。

实际非空基例是经典Πζ，取σ0=3/2、c=2。旧10-11的f1-mellin-source-analysis-review§3已消费DLMF25.2.10给任意扩大fixed实部条带的ζ无条件多项式界；旧003来源索引与10-20 canonical-completion-source-and-uniqueness又已消费DLMF5.11.9的一致vertical Stirling。两旧输入在[−1,2]给Λζ的poly×exp(−π|τ|/4)，可弱化取η=π/8，不编数值C/N0。本轮只重读这些项目消费定位，没有重读DLMF网页或新增增长定理。

## 2. M单位、计数增长、实际收敛边界及A正

指数权下卷积质量相乘，Tonelli给∫e^(−σ0u)dM=exp(K0)<∞；各项支撑非负。Π无0原子，故每个正阶卷积无0原子，M{0}=1。于是N支持[1,∞)，N{1}=1，并非把整数支撑预设进输入。

令Z_c=∫x^(−c)dN=Z(c)<∞。对R≥1，N([1,R])≤Z_c R^c。因此正偶测度N+反射N以及加任意有限0原子都tempered。指数u的权与加法x的polynomial增长不可混成physical源范数。

设α是正M的Laplace收敛横坐标，α≤σ0有限上界。若α>1，Z=Λ/Γ_R在实α解析，矛盾旧正测度Landau实边界引理；Γ_R=π^(−s/2)Γ(s/2)在那里非零正则。若α<1（含−∞），原Laplace在1邻域解析，矛盾Λ在1的实际pole与Γ_R(1)=1。故α=1。

所以每个实σ>1的Z(σ)>0，且Z=其实际正测度积分；Schwarz对称使A实。Laurent主项A/(σ−1)和实际simple pole迫A>0。FE把1点留数A反射成0点−A，未先假A=1。旧063KR/261-B的Taylor＋Tonelli正Borel版本适用M，允许其0原子。

## 3. 原Mellin公式、全部尾与正确±A

定义Θ_N(t)=2∫_[1,∞)e^(−πtx²)dN(x)。在Re s=c，Gaussian Mellin inversion给

 2e^(−πtx²)=(1/(2πi))∫_(c)Γ(s/2)(πt)^(−s/2)x^(−s)ds，
 Θ_N(t)=(1/(2πi))∫_(c)Λ(s)t^(−s/2)ds。

这里s=2w时ds=2dw恰给第一式左边的2；没有额外半因子。绝对Fubini费用为π^(−c/2)t^(−c/2)Z(c)∫_R|Γ(c/2+iτ/2)|dτ。该Γ积分有限可直接由Fourier证明：v→exp(cv/2−e^v)为Schwartz，其频率τ/2的Fourier变换为Γ(c/2+iτ/2)。无需把未知Λ的增长当作Gamma原件。

在矩形[c,1−c]×[−T,T]上移线。对每个fixed t>0，两horizontal绝对值各至多

 (2c−1) C max(t^(−c/2),t^((c−1)/2)) (1+T)^N0 e^(−ηT)，

故趋零；两vertical尾也由同一实权指数界绝对可积。唯一两留数分别为At^(−1/2)、−A。左线令z=1−s并用FE，方向翻转后得t^(−1/2)Θ_N(1/t)。因此

 Θ_N(t)=A(t^(−1/2)−1)+t^(−1/2)Θ_N(1/t)，对全部t>0精确成立。

这不是只在有限Gaussian样本/渐近t上成立，也没有移除proper powers或pole缺陷。先固定t移线，得到全t精确身份；后续全性消费不需把有限T误差错误宣作moving-t统一。

## 4. μ_A、单位gap、A校准及完整Euler数据

令μ_A=Aδ0+N+反射N。它正、偶、tempered，且μ_A在(−1,1)恰为Aδ0。上一式等价于θ_(μ_A)(t)=t^(−1/2)θ_(μ_A)(1/t)。旧561固定Gaussian→Fourier段与正性/unitgap定理用于μ_A/A，给μ_A=AΣ_(n∈Z)δ_n。

比较x=1原子：左边N{1}=1，右边为A，所以A=1；进而N=Σ_(n≥1)δ_n、M=Σ_(n≥1)δ_(logn)，Z=ζ。未借用ordinary整数Dirichlet支撑、free generation、离散性、间距假设或RH。整数支撑是结论。

若需要Π层，实际右半面germ中logZ=LΠ，分支由实+∞趋0固定。Z=ζ后，加权有限测度Laplace唯一性给Π=Σ_(p,j≥1)j^(−1)δ_(jlogp)，全部proper powers保原1/j。Π正不自动等于已有正primitive；若**另给**P≥0并满足全部repeat关系，则P≤Π使其有log2 gap，有限causal Möbius反演给P=Σ_pδ_(logp)。没有由Π正免费宣称任意primitive存在。

## 5. 强旧净值与准确停止

该类别的全部非经典正Π模型已由旧运输＋561排空，不必再投入原域内的signed替换/finite-coset model selection。它允许原Π−Πζ一般signed差；不是只处理上一轮的单调增量或finite rational(s)，但现在多了完整simplepole/Γ/FE及明示全strip增长前件。不能把几组不同前件的类别合并成任意正Π唯一性。

同一证明还已蕴含更强的旧覆盖：若直接给正N支持[1,∞)、N{1}=1、一个Mellin实权有限，并给相同Λ/FE/simplepoles/strip界，则也分类为普通整数计数。令M=(log)_*N即可复用实收敛边界和A正；整数识别不依赖Π正性、Euler product、离散性或free generation。Π/P的恢复仅在它们另有实际给定时使用，不由这一更强N分类免费产生Euler数据。

这是强旧完整依赖链的应用0；没有新的独立算术输入、完整Weil净号、core/coupling费用、非零primitive或mixedRR。固定对象识别为ζ，恰说明“该类全都满足Weil正性”仍与经典RH等强，不构成证明。Whole4/5仅负惯性UPPER，原source→primitive/RR/完整Weil主责未改。

增长前件之外、不同pole阶/背景、不同Γ、只极限有FE/整性的正D′层及joint signed修复未被否定；它们也不会因未被否定自动成为有效层。Watkins第一步骤按pole位置的宽读继续冻结，仅本次明示simplepole/质量/增长分支重闭。原物理r=e^(u/2)f、du/zero-extension Dlog和全complex源没有新统一运输，不能由加法x正测度免费取得乘法log的Weil号。

停止在该已识别类别继续搜nonclassical模型或弱化增长来制造逃逸；下一先做本结果后的因果投入审视，选真正同源mixed/完整signed新实物。当前没有已形成的新candidate、proof或source章节，不以恢复/整理/推送完成长期Goal，也不调整唯一cadence。
