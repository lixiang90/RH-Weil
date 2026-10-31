# 全对称幂 automorphy 的实际 tensor 首检：源命题与全球零点责任

2026-10-31。G20261027/runtime1793085111、原0c4f基线；这是一个指定原件引言门及标准代入比较，不是C065续轮或新数学合同。Root实际核PDF1–2的必要statement/context及图像，作者证明未审。独立strongest-old稿仍须对齐后才能结算。

## 输入、测试和可能净值

实际输入是Newton–Thorne《Symmetric power functoriality for holomorphic modular forms》，arXiv:1912.11261v3（2021-09-27），Theorem A。固定level1权12的Ramanujan Δ对应的GL2表示π，采用单位中心规范。与固定C2不同，此处Sym^(2j)随j出现新的高维尖点表示，不能套“只有两个固定L因子”的旧C2结论。

最便宜的测试是：即使无偿授予这些尖点L函数的完整解析性质，局部tensor与全阶pole是否能把**目标全球ζ零点**变成可放大的同一谱参数？如果能独立产生这种传递、或者给完整目标的新符号控制，才有数学准入；若只给已知的local Satake纯性，不为目标重开合同。

与FRS缺独立tail sign、Clark规范构造趋flat相比，这个输入实际支付了另一条责任：真实非平凡局部tensor族的全阶automorphy。本测试也可能证明它尚不支付全球目标责任；不存在“所核章节没有证明RH，所以全部方法不可能”的推论。

## 原文严格范围

原件101页、1249898bytes、SHA256 `6d50b558a6182a8d1515a6715529a33079807bf405c8db775e4ed252f5a2f379`；固定文件只存`literature/local/2026-10-31-newton-thorne/`并已核Gitignore。初次sandbox代理连接失败；同一个下载经已授权网络执行及10808代理成功，实际PDF签名/metadata/页数/首版本标记核过。

PDF1 context把R(π)的匹配定义在**每个place的local Langlands parameter**上。PDF2 Theorem A：π为level1 regular algebraic cuspidal GL2(A_Q)表示，则每个整数d≥2的Sym^(d−1)π存在，且为regular algebraic **cuspidal** GLd(A_Q)表示。这里“everywhere unramified”按finite level1理解，不把无穷处离散系列叫unramified spherical。PDF2必要开头解释包含weight≥2 holomorphic forms。

采用此已发表深定理的statement作为cited输入，不宣称独立审完其证明。相邻Theorem B、Corollary C、其后Strategy及脚注虽在整页抽取/图像中曝光，但不作Δ结论的额外输入；PDF1其余历史段、TOC也不等于各章已读。未顺读PDF3–101、参考文献、II或相关paper。期刊版116页与本固定arXiv版101页不同；不混合页码或文件hash。

以下另采用标准GLd尖点L解析定理：unitary cuspidal d≥2的completed standard L整、满足对偶FE，且standard L在s=1非零。这里只标**标准外部cited**，没有从Theorem A字面假装读出证明；有限全乘积的exact端点pole使用这项非零输入。如果暂不授予它，可只保代数Euler身份和条件pole后果，首检的不准入结论仍成立。下述arch公式来自标准real Weil parameter的直接对称幂分解，不归作者本页定理。

## 同一个局部fiber的全阶计算

令V为π的2维标准局部参数，det V=1。对p和k≥1记t_(p,k)=α_p^k+β_p^k；α_pβ_p=1，Δ实Hecke系数保证t_(p,k)实。偶次tensor的幂迹为t_(p,k)^(2n)≥0。这个实数性质本身不先要求Ramanujan界；α、β可以先是实互逆或单位圆共轭。

V在此是unitary local Langlands记号，不声称Δ的weight11 motive有一个实际half-Tate twist。若用标准Δ motive/ℓ-adic realization M表示同一偶幂，则合法对象为M^(⊗2n)(11n)，只需整数Tate twist；其分解中的Sym^(2j)M(11j)也只用整数twist。这里采用标准Frobenius/Tate号约定：M^(⊗2n)的weight为22n，twist(11n)减去22n使其归零。所需motive/Galois存在性只作标准背景，不把本页statement冒充已审全局motivic构造。当前解析比较直接在unitary automorphic参数和其L函数上进行，不需引入half-Tate motive。

SL2的标准Clebsch–Gordan分解给

    V^(⊗2n) = ⊕_(j=0)^n m_(n,j) Sym^(2j)V,
    m_(n,j) = binom(2n,n−j) − binom(2n,n−j−1),
    c_n = m_(n,0) = binom(2n,n)/(n+1),   D_n = 4^n.

这是标准表示环身份，可由乘法Sym^a V⊗V=Sym^(a+1)V⊕Sym^(a−1)V及Pascal归纳得到；含det因子的GL2身份在此det1规范后化成上述式子。n=1为1⊕Sym²V，n=2为2·1⊕3·Sym²V⊕Sym⁴V，维数分别4、16。这里不是新建普通全球zero-space的tensor。

在Re s充分右及全部finite places，level1没有遗漏bad prime：

    L_n(s) = ζ(s)^c_n ∏_(j=1)^n L(Sym^(2j)π,s)^m_(n,j),
    log L_n(s) = Σ_p Σ_(k≥1) t_(p,k)^(2n)/(k p^(ks)).

指数形式还给Dirichlet系数非负。最初绝对收敛半平面可依n，用原holomorphic coefficients的粗polynomial界即足够，不偷用待推local纯性。标准尖点解析输入后，completed Λ_n可能的pole只在0/1；采用端点非零定理后均恰c_n阶。有限L_n在实s>1全纯。全阶pole控制在这个具体族是真的，不应继续写成“任何实际全tensor pole输入都没有”。

对每个fixed n，Landau非负Dirichlet级数定理把收敛横坐标的有限实奇点放在该横坐标；因L_n在实s>1无pole且原级数有有限横坐标，得到收敛横坐标≤1。这里零点不是L_n的奇点，不能拿离线零点当pole套Landau。若某个fixed p有|α_p|>1，则α、β实互逆，偶幂局部级数迫

    2n log|α_p| / log p ≤ 1.

对全部n再令n→∞，得|α_p|≤1；det1及对偶给二者模1。它控制的仍是**同一个局部α_p**。这是567§6所恢复的Deligne机制在新cited tower上的标准代入；Δ的local纯性本就已知，没有得到ζ全球零点ρ的新界。实际消费以此角色识别为止，不研究数值界或无零区域。

## ζ零点确实保留，但不是谱幂

取任何非平凡ζ零点ρ（0<Reρ<1），重数mρ。completed ζ因子在ρ也有相同零阶；其它completed Sym^(2j)因子整，故

    ord_ρ Λ_n = c_n mρ + Σ_(j≥1) m_(n,j) ord_ρ Λ(Sym^(2j)π) ≥ c_n mρ.

因此不能说此tower完全看不见ζ零点，或担心尖点整因子在ρ以pole抵消ζ零。反过来不需要知道尖点零点与ζ零点是否互不相交。实际保留的是**同一ρ、增加重数**；没有ρ移到1/2+n(ρ−1/2)，也没有原全球生成元的特征值乘积、Künneth或global trace实现。其它Sym因子还加入新的未知全球零点；它们不只是C2两个旧因子的复制。

一个未证的“Λ_n全体零点都在中心线”当然能通过这个保留关系推出RH，甚至固定n即可；Theorem A和无额外pole定理没有给该零点定位。Landau在全体n中看的仍是各local Euler参数制造的实奇点，不是Γ完成后的global零点。故不能把这个合法不抵消箭头和local纯性结论拼成RH。

## 完整Γ与同源费用的范围

权12单位规范下，设Γ_R(s)=π^(−s/2)Γ(s/2)、Γ_C(s)=2(2π)^(−s)Γ(s)，则

    L_∞(Sym^(2j)π,s) = Γ_R(s+ε_j) ∏_(a=1)^j Γ_C(s+11a),
    ε_j ≡ j (mod 2),  ε_j∈{0,1}.

该参数来自2维real Weil表示诱导的±11权；对称偶幂的中间字符为sgn^j，其余成对权产生所列Γ_C。j=0给Γ_R(s)。全部factor按m_(n,j)相乘，arch degree为

    Σ_(j=0)^n m_(n,j)(2j+1)=D_n=4^n.

因此D_n/c_n=4^n(n+1)/binom(2n,n)~√π n^(3/2)。这是**degree相对已保目标重数**的标准计账，不是任意joint signed修复的必要费用lower，不证明所有net误差都大，更不是整个automorphic/Deligne方法类的不可能定理。即使出现合法Γ抵消，全球谱幂箭头也需另证；反之没有谱幂本身不排其它直接全球正性机制。

对每个fixed n、fixed compact复源r，标准完整显式公式的直和线性仅给

    Q_n[r] = c_n Q_ζ[r] + Σ_(j≥1) m_(n,j) Q_(Sym^(2j)π)[r].

这里Q均按同一原r、du、zero-extension Dlog和完整各自Γ/contact、全部proper powers及双pole/entire区别定义；只使用共同的合法compact测试域。没有从不同degree直接运输norm或从普通Dirichlet系数非负领取Q_n≥0；后者是全球零点的另一层正性责任。此门未建立n→∞的Q范数极限或成长窗估计。

Π/Hecke的局部整性和tensor存在性都不是r→非零primitive divisor、405全Pan消去、537非根可见性或实际mixed RR。没有增加几何coverage，也没有给560危险signed core/cross有利估计。原leading4/5负惯性UPPER保持；不称PSD、比例、负惯性lower或Ξ。

## 强旧比较、停止与可推翻条件

002§2已排local纯性⇒global RH；073§4明确local Satake tensor不自动global zero-space tensor；567§6已把全阶even positivity＋monodromy/cohomological pole界的消费对象固定为local特征值。本门新读的Newton–Thorne statement确有独立数学内容，却只填了一个具体localtensor tower的automorphy槽；上述标准代入没有填原目标的全球谱桥。故不把已知local纯性重领为新Goal后果，不建C066/603或加数学轮。

停止范围是“本实际tower，仅以所核automorphy/standard pole/非负local coefficient输入直接调用Deligne提纯来证明目标ζ零点”的准入。不是对全部functoriality、relative/lax/graded RΓ、非有限monodromy、完成Γ的signed修复或其它global几何作边界定理。真正独立的global realization/trace及谱传递、或直接支付完整目标的新全球符号控制，才会推翻当前不准入选择；不能只换Sym阶数、CM/level或引用后章。

此稿只保存实际比较和cited来源范围，待独立稿/不同fresh/root逐项核后结算。唯一原cadence不动；原数学完成门仍open、同Goal active。
