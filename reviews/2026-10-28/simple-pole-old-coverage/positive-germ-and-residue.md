# Simple-pole旧覆盖：正测度germ、实收敛边界与留数校准

2026-10-28；`/root/rational_old_admission` 本次独占输出。已恢复 README／STATE、check→show、G20261027、耗尽 C049、D20261028W、当前来源结算与 next-simple-pole-old-classification-admission.md。这里只支付正测度／质量／abscissa腿；没有读取或提前消费另一运输腿稿。无web、新来源、下载、数值、STATE／cadence／Git修改。本稿为**旧561及正Laplace–Landau机制的明确应用0**，不是新数学合同或已root消费结果。

## 1. 冻结输入及两个不同坐标

Π是(0,∞)上的正Borel测度，存在实σ₀使

 B₀=∫e^(−σ₀u)dΠ(u)<∞。

给原右半面germ Z=exp(LΠ)，以及 Λ=Γ_R Z 的真实全域亚纯延拓，Γ_R(s)=π^(−s/2)Γ(s/2)。Λ满足精确 Λ(s)=Λ(1−s)，实际极点仅0、1且**都是简单极点**，留数−A、A，因此A≠0；暂不假A实正或A=1。

另给一个 c>max(σ₀,1)，在整个σ∈[1−c,c]和|τ|≥T₀上统一

 |Λ(σ+iτ)|≤C(1+|τ|)^(N₀)e^(−η|τ|)，C,N₀,T₀,η>0。

这个明示strip界由候选域提供，不从“finite order”、bare FE或正Π推出来。本腿的M、abscissa及A>0只用正germ与实际pole／全域延拓；strip界属于另一运输腿的责任。

u为Euler的log坐标，x=e^u为integer-side坐标。下面的N是M的指数推前**测度**；N([1,X])才是累积计数。它们不是physical r=e^(u/2)f的du范数或Weil谱测度。

## 2. 正卷积指数真实存在，且单位原子精确为1

令ν₀=e^(−σ₀u)Π，为有限正测度，质量B₀。在有限测度代数中

 exp_*ν₀=δ₀+Σ_(j≥1)ν₀^(*j)/j!

按总变差收敛，总质量exp(B₀)。因为指数权对加法卷积相乘，解权给

 M=δ₀+Σ_(j≥1)Π^(*j)/j!； e^(−σ₀u)M=exp_*ν₀。

这是[0,∞)上的局部有限正测度：对每个先固定R，指数解权在[0,R]有界，所以级数在该compact上的质量有限。不需要Π支撑与0隔开；B₀已经保证0附近有限质量。定义不依赖选用哪个合法实权，因为每个compact上的无权正级数相同。

Π本身不含0，故每个j≥1的有限卷积在{0}质量为0。正级数逐项在此集合求值给

 M({0})=1。

支撑趋0的无限多个正原子不会在这里产生额外的δ₀。对所有Re s≥σ₀，绝对Tonelli与卷积乘法给

 ∫e^(−su)dM(u)=exp(∫e^(−su)dΠ(u))。

在Re s>σ₀，此等式是解析身份；求导可用稍小的实权先支付各阶矩。特别对σ≥σ₀，

 Z_M(σ)=∫e^(−σu)dM=exp(B_σ)； B_σ=∫e^(−σu)dΠ≤B₀。

由Π无0原子及支配收敛，B_σ→0，故Z_M(σ)→1（σ→∞）。这是单位germ规范，不另选log分支或常数。

以上是[旧561 §1及§2的加权卷积机制](../../../notes/561-beurling-positive-measures-self-duality-and-integer-recovery.md)，本处写清任意合法σ₀及原子责任，不登记新定理。

## 3. 正M的Laplace收敛横坐标恰为1

定义

 α=inf{σ∈R:∫e^(−σu)dM(u)<∞}∈[−∞,σ₀]。

正性与u≥0保证收敛实集是向右的区间；Z_M在Re s>α解析。M的δ₀只加常数，不影响有限收敛边界。使用[旧063 KR](../../../notes/063-one-point-abel-moment-criterion.md)、[283-C证明内Landau引理](../../../notes/283-fixed-cutoff-abel-mass-oscillation.md)及[当前正Borel版消费](../monotone-euler-increment/root-old-consequences.md)：正测度的Laplace变换若有有限横坐标α，则其和函数不能在实α附近解析延过。其Taylor／Tonelli论证适用于本M，不要求绝对连续性。

**先排α>1。** 这时α有限。Z_ext=Λ/Γ_R在实α附近全纯，因为Λ只有0、1极点，且Γ_R在实α>1有限无零。它在原右半面与Z_M相同，由解析唯一性在重叠域相同，于是延过真实收敛边界，与旧Landau矛盾。因此α≤1。

**再排α<1（含−∞）。** 取α<β<1使Z_M在Re s>β解析。原germ的唯一亚纯延拓Z_ext便在1应全纯；但Γ_R(1)=π^(−1/2)Γ(1/2)=1，Λ的实际simple pole在Z_ext中没有被取消，其留数正是A≠0。矛盾。

因此

 α=1； ∫e^(−σu)dM(u)<∞ 对每个实σ>1。

并且M在σ=1不收敛；否则正性与单调收敛会使σ↓1时Z_M(σ)趋有限值，冲突实际pole。此结论对**M**而非Π的收敛横坐标作断言；不无声把两者的边界行为等同。

若一份候选原始σ₀≤1却同时声称B₀有限和上述实际simple pole，所有输入就不相容：第2节使Z_M(σ₀)有限，与这里的α=1及边界发散冲突。可选更大的合法σ₀，但不能删除实际pole来修补该冲突。

## 4. A实且严格正，不依赖待核theta运输

原右半面内Π正，Z_M在实点正且满足共轭实型；Γ_R也实型。故Λ与Λ*(s)=overline(Λ(bar s))的全域亚纯延拓由相同germ唯一，Λ为实型，A为实数。

第3节使每个σ>1都有Z_M(σ)>0。实际Laurent展开为

 Z_ext(σ)=A/(σ−1)+O(1)； σ↓1。

若A<0，右侧充分接近1便负，与正M-Laplace矛盾；A=0又不合“实际简单极点”。所以

 A>0。

FE则与给定的0点留数方向一致：Λ(1−s)的A/((1−s)−1)=−A/s，故Res₀Λ=−A。这里没有借用未知ζ根、RH、prime误差或另一运输腿。

## 5. N的support、单位原子与tempered费用

令N=(u↦e^u)_*M，则N为[1,∞)上的正Radon测度，且

 N({1})=1； ∫_[1,∞)x^(−c)dN(x)=Z_M(c)=exp(B_c)≤exp(B₀)=:K。

对所有X≥1，

 N([1,X])≤K X^c。

不需要N离散或预设整数支撑。原初Mellin公式在Re s>σ₀成立，随后在Re s>1由同一正M-Laplace及唯一性成立：Z(s)=∫x^(−s)dN(x)。令ι是[1,∞)到R的包含，定义

 μ_A=Aδ₀+ι_*N+(−ι)_*N。

由A>0，μ_A为正、偶测度，且μ_A|_(−1,1)=Aδ₀。若m是任意整数m≥c，对每个f∈S(R)，

 |μ_A(f)|≤(A+2K) sup_x(1+|x|)^m |f(x)|。

因此μ_A确为tempered measure，费用由同一个c、原B₀和已定A支付。这个界在Schwartz测度配对中，不提供physical du／zero-extension Dlog的global统一比较。

## 6. 条件性接口：若运输腿给全t Gaussian身份，旧561立即校准A=1

**本节条件尚须root消费另一腿原稿后才可使用。** 假如同一N、同一个A已真正证明对所有t>0有

 Θ_N(t)=A(t^(−1/2)−1)+t^(−1/2)Θ_N(1/t)，
 Θ_N(t)=2∫_[1,∞)e^(−πt x²)dN(x)，

则θ_(μ_A)(t)=A+Θ_N(t)满足精确θ_(μ_A)(t)=t^(−1/2)θ_(μ_A)(1/t)。第4–5节已经独立给A>0、正偶tempered及精确gap。于是μ_A/A满足旧561固定Gaussian版的**全部**前件，直接得到

 μ_A=AΣ_(n∈Z)δ_n。

比较**同一测度**在点{1}的质量：左边为N({1})=1，右边为A，所以A=1。遂

 N=Σ_(n≥1)δ_n； M=Σ_(n≥1)δ_(log n)； Z=ζ。

不能先把μ_A的原点质量写成1再应用旧分类，否则正是把待校准的A偷放进输入。也不需要新增uniform discreteness、finite-coset分类或n支撑假设。

可选的A符号检查同样依赖这份**已付后**的theta身份：由N的c权和x≥1，Θ_N(1/t)=O_c(K e^(−π/(2t)))（0<t≤1）。所以Θ_N(t)=A t^(−1/2)−A+o(1)。左侧非负且≥2e^(−πt)，便排A<0及A=0。该替代证明不能在运输消费前使用；本稿第4节已不依赖它。

## 7. 条件性分类后，Π及已给primitive的恢复

仍条件于第6节的实际运输／分类闭合。对Re s>max(σ₀,1)，exp(LΠ)=ζ。实σ足够大时LΠ(σ)为实数，故等于正实logζ(σ)；两者解析身份及σ→∞趋0固定同一log分支，得到

 LΠ(s)=logζ(s)=Σ_(p,j≥1)j^(−1)p^(−js)。

右端是全部proper powers的Π_ζ Laplace变换。取一个a>max(σ₀,1)，e^(−au)(Π−Π_ζ)为有限signed measure，其在s=a+iτ上的Fourier变换对所有τ为0；旧加权测度唯一性给

 Π=Π_ζ=Σ_(p,j≥1)j^(−1)δ_(jlogp)。

**若输入另有实际正primitive P，并已核全部repeats Π=Σ_(j≥1)j^(−1)(T_j)_*P，**才进一步消费P的识别。正项j=1给P≤Π_ζ，故P支撑≥log2。对任意compact[0,R]，所有repeat和及下面Möbius逆都只有有限个j可贡献：

 P=Σ_(j≥1)μ(j)j^(−1)(T_j)_*Π_ζ=Σ_p δ_(logp)。

有限compact换序的合成系数为n^(−1)Σ_(d|n)μ(d)，除n=1外为0，故该逆合法。不从任意正Π免费生产正P，也不删去j≥2来识别prime；本节仅对已给且满足全repeats的P作条件性恢复。

## 8. 依赖闭合与强旧净值

本稿独立已付：任意合法实权的M存在与单位质量、N support／polynomial／tempered费、M收敛横坐标1、A实正。依赖仅正测度卷积字典、germ唯一性、实际simple pole及旧正Laplace边界；FE只核Res₀方向。明示strip界保留原样，不声称被正性推出。

尚须另一腿且未被本稿提前消费：同N的Mellin反演、移线、两simple pole的全部系数和全t Gaussian身份。该腿一旦root核闭，A=1及M／Π／条件P识别便是旧561与测度唯一性的直接应用，准确恢复该**明示增长/simplepole类别**的已有分类强度，不重计数学轮。

此结果只决定该类是否还容非经典model selection，不提供经典乘法Weil正型、原complex source→primitive/mixed RR、危险core/coupling净费或faithful Ξ正性。whole4/5仍仅负惯性UPPER，Goal完成门未过。不同pole阶、增长域之外、只极限FE／整性、非局部joint signed和D′修复不由此分类排除；本稿也不将它们按定义称为有效新输入。

没有新外部来源、proof合同、计轮或后台进程。本稿及另一腿都须root核相同对象、常数与量词再消费，稿件落盘不代结算。
