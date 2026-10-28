# 源商自导子：不同组织的限定逆审

2026-10-29；G20261027、runtime1793085111、冻结0c4f。本稿只审本次三个实际输入，不开数学合同、不计轮、不增文献或来源预算。恢复check→show通过仅作结构检查，不代数学验收。

**判定：PASS，按最强旧的标准推论记old0。** 实际有限局部块、非幺导子及完整配对证明闭合；候选失败537非根测试。未发现需要新增无限谱综合、连续性、提升或全局单位元的前件。此结论不通过长期Goal的数学完成门。

## 1. 本次实际输入版本

以下为完整读取的规范UTF-8/LF版本，字节及SHA256绑定本次审稿；早发的9776-byte strongold不作本次输入。

| 同目录输入 | LF字节 | SHA256 |
|---|---:|---|
| root-source-formula-and-idempotent-test.md | 5840 | f44b603b664a5f700810357ad1c6df92f1744474c314206225479772ae3d580e |
| algebraic-idempotent-and-derivation-test.md | 6245 | 297763cd2b6c8b1cb3f1765ed946fb992d963e71bed7bbcdaa98f7ee76e85e17 |
| strongest-old-and-homology-scope.md | 9923 | fb85df02e434b72c758af8a543aade89392b796d81cd56bf89dc90ee17a58b5e |

独立对照旧405§§3、5–6，516全文、519全文、520全文，以及552§1、537§2；432§§1–2、573§§1–4和402§§1–4只核同调类型差别。没有新web、query、PDF或数值运行。三稿出稿和本fresh均不代root消费。

## 2. 实际对象与局部块：无无限插值偷渡

F=𝒮_exp,ℂ为旧卷积代数，原半范数p_(N,j)=sup e^(N|u|)|f^(j)(u)|；M_f(s)=∫e^(su)f(u)du。519付I=R_jet，P=P_an=I∩kerd∩kerc闭；A=F/P为原强商拓扑，d=M(1)、c=M(0)。A是解析商，尚不是算术principal对象。joint映射

    j:A→ℂ²×∏ρ ℂ[t]/(t^mρ)

由准确核P单射；只消费单射，不声称无限乘积满射或有限谱包稠密。乘法为逐坐标乘法，因为Mellin把实际卷积变乘积。

520给每个真实零点ρ、有限重数m的实际u_m∈F，其Mellin为H0/(s−ρ)^m，H0=ξ/2且H0(0)=H0(1)=1/4。令w=s(s−1)H0/(s−ρ)^m，则w在ρ非零，在其它零点保完整jets，且两degree为零。有限Taylor逆Pρ使Eρ=Pρw≡1 mod(s−ρ)^m。有限多项式乘子由−D作用，确保持F；没有取无限插值函数。

实际代表的类eρ满足eρ²=eρ：差的joint坐标全零，故在P。eρA只有ρ坐标，有限乘子(s−ρ)^jEρ实现全部0≤j<m坐标；因此角代数确为ℂ[t]/t^m，既单射也满覆盖这个有限块。eρ与其它零点块、405的两个degree幂等块正交。后两块各为ℂ；它们仅模P幂等。全局单位从未使用。

## 3. 非连续、非幺的自导子仍逐块落根

令δ:A→A为任意ℂ-linear Leibniz导子。e²=e给δe=2eδe，L_e²=L_e，故(Id−2L_e)²=Id，推出δe=0。于是δ(ea)=eδa，导子保持每个实际有限角代数。此为A上线性算子的代数恒等式，不要求拓扑连续或F提升。

在m=1块上，δ杀掉该块单位e，ℂ-linearity即给δ=0。在m≥2块上，

    0=δ(t^m)=m t^(m−1)δt

且charℂ=0、t^(m−1)≠0，所以δt常数项为零。任意δ输出的ρ值为零，两个degree块同理给dδa=cδa=0。joint坐标逐点检测足以推出

    δ(A)⊂N=R_val/P=rad(B_A)。

没有推出高阶jets全零。若全体零点简单，519给N=0，故δ=0；若有m≥2，θ=t∂t在该有限块非零，δ(a)=θ(eρa)再嵌回A确为全A导子：eρab=(eρa)(eρb)，θ输出仍受eρ支撑。因此Derℂ(A,A)=0当且仅当全部非平凡零点简单；该条件式不证明简单性或RH。

N每个有限局部块幂零不代表N整体为幂零理想，也不识别全局nilradical。没有付统一mρ上界、任意局部导子族的全局胶合或统一半范数费。

## 4. 原物理配对与修复量词

405/516的完整身份为

    2B(a,b)=d(a)c(b)+c(a)d(b)−T(a,b),
    T(a,b)=Σρ mρ M_a(ρ)M_b(1−ρ)。

对δa，两个degree和全部零点值均零，故B(δa,b)=T(δa,b)=0对全部b。N也受旧共轭/sharp保持，因零点集有相应对称；不要求δ本身与共轭/sharp交换，仍可消费复Hermitian配对。

候选Jδ(r)=δ([e^(−u/2)r])至少在e^(−u/2)r∈F上定义。552把原physical Q_W与T的相应Hermitian型精确对齐，全部Γ/contact、properpowers及双pole保留。因此Q_A(Jδr,Jεs)=0，甚至任一δ槽与任意A槽的完整mixed值均零。

537在原Lebesgue norm、fixed17/16内给非零compact complex源严格正性。552的r0=(D²−1/4)ψ≠0同时有两个pole矩零和Q_W(r0)>0。候选无法保持该实际非根。只加回d(a)e_d+c(a)e_c会让B出现双曲degree项，但仍不恢复任何ζ值，故Q=T仍零。不能把恢复后的B也报为零，或把degree能量冒作原Q的修复。原u→r指数换元不是物理norm等距；本反测用精确零值，无需未付norm运输。

N为闭卷积理想：它是所有连续degree/值坐标的共同核除以P。因此任意源适应选择δ、移动rank/gain、有限signed和及A乘子都不逃离N；实际在A强商拓扑收敛的cofinal输出仍在N。若只对已为零的完整mixed标量逐点取合法极限，结果也零。没有给发散的无限assembly定义值，也没有用闭性偷付新的完成或regulator。

520的−D与中心化平移是卷积乘子/线性作用，并非这里的卷积Leibniz导子；它们的真实Jordan行为不构成反例。其它值域模、非Leibniz源项、新regulator、relative/higher/noncommutative目标及有独立比较的不同极限仍未排。正D′一般机制也没有被强加逐层Pan/Leibniz条件。

## 5. 最强旧扣除与完成门

此处old0有实质依赖链：405已给actual algebra和degree块；519给exact joint full-jet核；520给逐零点实际局部函数；516给full配对恰只测值。剩余是有限Hermite逆、幂等元恒等式和char0截断多项式导子计算。不是仅因旧显式公式可代入任何新对象而判0，而是候选所需全部实际对象和分解已付，未新增算术输入、成长估计、独立signed比较或原norm容量。

可以把原旧资产的这一标准后果明确保存、停止同A同配对的自导子候选；无continuity/lift的广度不构成新的数学轮。它与593的actual moving-source norm净比较不同，不准C057/594，不改cadence3/history57/latest593/formal18或manifest132。

HH¹(A,A)=Derℂ(A,A)只使用通常degree1 cochain及交换性杀inner。没有证明HH₁、Ω¹、任意模值导子为零。432/573在不同非交换pair上的HH₁电荷−4及其下降反测、402普通Ω_(C/ℚp)的无限维事实均未受影响；下标同调与上标上同调不能互借。

核心primitive/principal/sections/mixed、dangerous signed core/coupling与成长Ξ未新增付款；whole leading4/5仍是旧负惯性UPPER。此局部标准推论未覆盖Goal要求的实质核心方法类及全部合法修复，不能完成长期Goal。停止本候选、不串来源/参数；下一准入仍须不同实际source/pair或能改变选择且扣强旧后的具体test，不能把未排逃逸改名成已获预算。
