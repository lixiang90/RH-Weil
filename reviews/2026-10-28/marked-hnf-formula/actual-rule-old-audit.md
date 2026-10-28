# Marked-HNF实际规则：全域费用、固定两源与强旧审计

2026-10-28；`/root/rational_old_admission` 当前具体式审核。只消费root明确指定的 actual-two-source-attempt.md 完整F1–F3／T1–T8版本，**9375 bytes，LF SHA-256 `cbd1739b6fb8055bdfa54ec9b6ac1fbe9ae398ad656ab5200cfc59ff96778e02`**。已全文核读，准备稿不代此次审核；不改prepare／main／STATE／Git，不形成第二候选，不web／来源／调权或后继proof。

**限定结论：当前式的T1–T8及cofinal失败成立。建议按标准工具＋已付完整target／原子门的前置自筛0消费，而非新完整数学迭代。** 理由是实际reader落入旧uniform L¹-test预算不能逼近孤立原子的类型，不是同raw数据、正文自称0或没证明RH便自动记0。下面将实际新计算和旧机制分开。

## 1. 原冻结与对象没有中途改写

现场独立取当前文件前3067 bytes，LF SHA精确为

 `b2aba545690c4e3fb3c0cdacb1941950e85c350a0d528ee75cdbcabfaa8c5260`。

这与主稿§3所记冻结版本一致；section3起始在byte3068。该原前段已经有T=e^(2v)和**√T** prefactor、减1与1/(nT)、Hermitian偶化、ad≤B和等权1/|H_B|、原h_rs及C_B。没有用未加权缺陷先失败后再补√T。后面诊断H=diag(1,n)、T=1/n也正确地针对旧无权反测的误用，不是本规则改参数。

完整theta求和是H Z²的实际Euclidean格点和；G_H、ambient标记及content原数据未被称作GL₂不变量／极化。C_B只是time-density reader，非principal商、Cartier截面、ordinary trace或已知正Weil型。

## 2. T1→T4：原全theta、shift与全部H／v量词闭合

对任意a≥1、实z及R≥0，N_(a,z)(R)=#{m:|am+z|≤R}≤1+2R/a，端点也不改变此上界。Gaussian layer-cake及Tonelli给

 Σ_m exp(−πT(am+z)²)=∫₀∞2πTR exp(−πTR²)N_(a,z)(R)dR
 ≤1+1/(a√T)。

这是主稿T1，第一积分为1、R²积分给1/(a√T)。先对每个k取z=bk，再对全部k使用同式，得到T2

 Θ_H(T)≤(1+1/(a√T))(1+1/(d√T))。

没有将b删除为0，没有只保一个primitive vector或n=1层。零向量给Θ_H≥1；二维Gaussian Poisson的covolume是n=ad，dual lattice是H^(-T)Z²，故Θ_H(T)=(nT)^(-1)Θ_dual(1/T)≥1/(nT)。这是原全格的标准Poisson，计数和维数／T幂均正确。

代入**原**F1后，上界为a^(-1)+d^(-1)≤2；两个lower分别是−1/(n√T)、−√T，合并为

 −min(√T,1/(n√T))≥−1/√n≥−1。

因此K_H、偶化κ_H及有限概率平均κ_B均满足−1≤κ≤2，**ALL H、ALL实v、ALL B≥1**。平均集非空，因为H=I在所有B≥1内。这一uniform费用足够决定目标门，不需要求κ_B的真实点态／分布极限。

## 3. Source槽、Hermitian方向与原norm

原h_rs(v)=∫r(x+v)overline{s(x)}dx第一槽线性、第二槽共轭线性。conj(h_sr(v))=h_rs(−v)，κ_B实偶给C_B(s,r)=conj C_B(r,s)。这没有使用Gram正定，也没有声称C_B≥0。

对r,s∈L¹∩L²，绝对Fubini给||h_rs||₁≤||r||₁||s||₁；T4给T5

 |C_B(r,s)|≤2||r||₁||s||₁。

它覆盖原全complex S_exp及Cc∞；它是**global L¹×L¹费用**，不是global L²／固定有限Sobolev reader界。原r=e^(u/2)f没有被换成f。若两个源支持I_L，各L¹≤√(2L)du，便得到4L du×du；原zero-extension Dlog²≥log2·du²给4L/log2的T6。B、L、频高和height量词未合并。

因此本式不能仅由553的global Hlog／Sobolev连续＋全Pan消去门判零，也没有要求有限B层消noncompact405。有限HNF索引亦没有被当作physical finite rank。这是主稿实际费用与预备门相容的部分。

## 4. T7：同一对fixed源、log2隔离及完整P／H方向

任选一份固定实非负ψ∈Cc∞(−1,1)，||ψ||₂=1；ε=1/256、α=log2固定后，sε=ε^(-1/2)ψ(u/ε)，rε(u)=sε(u−α)。它们不依赖B，du各为1、Dlog固定有限，且均在I₁。若需不用小数的支持检验，1/2≤log2≤5/6即可，后者可由∫₁^(3/2)1/x≤1/2、∫_(3/2)^2 1/x≤1/3得到。

h_rs(v)=h_ss(v−α)非负，h(α)=1，支撑在α±2ε，且

 ||h||₁=ε||ψ||₁²≤2ε。

该支撑正且避开所有负pp。最邻近的另一正pp位置是log3，log(3/2)≥1/3>4ε；所有其余pp更远。所以P的**全部**原求和只有+log2项非零，精确

 P(h)=log2/√2。

这里没有误乘±的2倍，也没把Λ(2^j)改成jlog2；其他properpowers是由同一fixed支持精确为0。log2≥1/2、1/√2≥1/2给P(h)≥1/4，T7正确。

H(h)=∫2cosh(v/2)h(v)dv是原双pole mixed配对；它没有因两源非偶而被删除。支撑上|v|<2，故0≤H(h)≤4||h||₁。这一H确是μ₊(r)conj μ₋(s)+μ₋(r)conj μ₊(s)，不是F1二维零／volume项已经运输到经典pole的证明。

## 5. T8：统一全B的13/64与极化范围

T5使|C_B(rε,sε)|≤2||h||₁，故

 |C_B−(H−P)(h)|≥P(h)−|C_B|−H(h)
 ≥1/4−6||h||₁≥1/4−12/256=13/64。

常数和减项方向均正确。B_B=qΓ+C_B与Bζ=qΓ+(H−P)在**同一**actual源对上复用同一Γ／FP/contact，因此其Γ腿准确相消；本稿没有用Γ热近似或忽略constant来制造差。

这是一个fixed h与两个fixed源对全部B的uniform lower，足以否定任何B→∞子列的完整mixed极限，也否定κ_Bdu→H−P于D′。它不是finite-B某个pp系数不符后跳判极限。后者原则在准备稿仍保持；当前是已支付了所需全B同测试门。

对Hermitian差型D_B，第一变量线性的极化为

 D_B(r,s)=1/4{Q_D(r+s)−Q_D(r−s)
             +iQ_D(r+is)−iQ_D(r−is)}。

四个源固定、合法compact且不依赖B。若四个quadratic差都趋0，mixed差必趋0，与13/64冲突。因此本规则也不能对全部compact卷积平方成立。这里只保证四个fixed平方不能全趋0；未从pigeonhole误说其中一份对所有B都有同一个liminf lower。

## 6. 强旧扣除：具体新计算不是新独立核心输入

583已经支付同一HNF／Hecke raw族、gcd／square aliases、native全norm／Green与尾；但它没有仅凭raw索引排掉本marked热functional。本次实际审计也没有证明C_B经旧L_r(j)／principal current因子化，所以不套583 closed-base结论。548–550的特定canonical／samephysical行族费亦不运输到此theta reader。

决定本式的是T1–T4的标准shifted Gaussian计数／Poisson计算，再接完整经典原子target。更强的旧类型门已经在[421 §6、§9](../../../notes/421-f1-weighted-hardy-trace-and-atomic-obstruction.md)及其[原推导§原子比较](../../2026-09-21/f1-weighted-hardy-kernel-derivation.md)支付：统一L¹测试预算的分布极限仍继承|F(h)|≤C||h||₁，不能产生孤立非零原子；取一个先固定的小支持h便同时分离所有候选。本式没有借421的Hardy／trace-class对象身份，只复用其中一般的L¹预算／孤立原子机制，T4独立验证它的实际前件。

主稿T7用555／577–578已完整支付的logp／sqrt(pp)原权、H双pole与Γ角色，在+log2将这条门直接实现成合法mixed两源。它未新增prime算术相消、未弱化一个关键前提，也未给实际signed缺陷消失。T1–T4是对这份新reader确实完成的原norm计算，应保存为真实自筛证据；但其净后果已经由标准预算类型和最强旧target决定。这里不以“工具初等”或“结论局部”作为唯一计0依据，而是以已付一般机制加现在直接核出的前件作分类。

因此建议**前置标准自筛0**，不建C050／587。若把本式进一步称为某个统一bounded-density方法类的全局新no-go，便重复旧421的类型结论；当前也没有覆盖允许发散预算、不同signed/joint、relative或非局部修复的Goal核心类责任。

## 7. 根消费范围与停止

可消费链为：当前原freeze含√T → 全theta shifted count／layer-cake与Poisson → ALL H,v,B的uniform L∞密度 → 原L¹及fixed窗du／Dlog费 → fixed ε源孤立原pp → 原H／P与同Γ相消 → ALL B的13/64 → cofinal及全部quadratic身份失败。

不消费：本规则为principal／primitive对象、全线L²有界、每层Pan消去、Bζ负源、经典RH反例、whole4/5改善、一般marked-HNF／theta／正D′类边界或Goal完成。实际瓶颈仍是独立完整signed净信息／同一非零primitive mixed机制。

仅停止当前F1–F3及原平均／target角色，不改√T、权、cutoff、norm、source域、level或Γ外腿再试；本稿没有第二formula或后继proof任务。原0c4f、≤582输入、单cadence0／历史50／latest586／formal17保持，最终消费／结算由root按当前绑定版本负责。
