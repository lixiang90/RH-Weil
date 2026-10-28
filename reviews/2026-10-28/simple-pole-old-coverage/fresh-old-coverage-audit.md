# Simple-pole旧覆盖：独立全链逆核

2026-10-28；`/root/euler_scope_fresh` 本次新任务独占稿。已恢复README/STATE、check→show、Goal、耗尽C049、D20261028W及宏观前沿，核工作树和当前两独占稿。本稿只逆核实际执行的旧覆盖比较，不复用前一来源门审稿为本轮结论，不改STATE/cadence/Git，不作web/PDF/数值或新来源核读。

**限定PASS。** 原正Π/M/N、真实simple 0/1 poles ±A、一次给定的全strip指数界，足以闭合M单位、α_M=1、A>0、全fixed-t Mellin/移线、μ_A/A的旧561输入和A=1。root新增的更强正N覆盖也正确。分类是标准旧链应用0；不准C050/587，不把对象识别升级为独立Weil正型、核心类完成或RH。

## 1. 原正germ、收敛边界和留数不循环

对Π于(0,∞)且∫e^(−σ0u)dΠ=K0<∞，加权卷积指数在有限测度代数中按总变差收敛，质量exp(K0)。去权在每个compact有界，故无权M=δ0+ΣΠ^(*j)/j!是真实正Radon测度。每个j≥1项在{0}质量为0，正级数逐集合相加给M{0}=1；支撑趋0的无限小原子不产生额外δ0。由此N支持[1,∞)，N{1}=1，未预设整数支撑。

α_M≤σ0给有限上界。若α_M>1，Λ/Γ_R在实α_M解析并延过该真实收敛边界，违反旧正Borel测度Laplace–Landau机制；Γ_R在那里无零且正则。若α_M<1，含−∞，Laplace积分在1邻域解析，冲突Λ在1的实际simple pole及Γ_R(1)=1。因此α_M=1。旧063 KR、283/261的Taylor–Tonelli版本允许M的0原子；它只加常数，不改变有限边界。

正germ的Schwarz唯一延拓使A实；对每个σ>1，同一正M积分Z(σ)>0，Laurent项A/(σ−1)及“实际pole”使A>0。这个证明不借theta或A=1，因而可以先于运输腿消费。FE将1点留数A反射成0点−A，方向正确。若给定某σ0≤1却又称其积分有限，这组输入本身不相容；不靠删除pole修复。

固定c权Z(c)<∞给N([1,R])≤Z(c)R^c，亦给∫x^(−c)dN<∞。因此正偶N+反射N及有限原点原子为tempered：取整数m≥c，(1+x)^(−m)≤x^(−c)于x≥1即可付款。这里的计数/S′费用不等于physical全du/zero-extension Dlog的界。

## 2. Gamma反演、2/π/ds与Fubini

令f_a(v)=exp(av−e^v)，a=c/2>0。它确在S(R)，且∫f_a(v)e^(iyv)dv=Γ(a+iy)；反选Fourier符号只令y换−y，不影响绝对L1或反演常数。由Fourier反演得到

 e^(−y)=(1/(2πi))∫_(a)Γ(w)y^(−w)dw。

换s=2w时dw=ds/2，所以2e^(−y)=(1/(2πi))∫_(c)Γ(s/2)y^(−s/2)ds。将y=πtx²代入并对同一N积分，交换的绝对费用为

 (πt)^(−c/2)Z(c)/(2π) · ∫_R|Γ((c+iτ)/2)|dτ <∞。

故Θ_N(t)=2∫e^(−πtx²)dN=(1/(2πi))∫_(c)Λ(s)t^(−s/2)ds。Gaussian Mellin正向公式的2Λ(s)与此式相容，正是ds=2dw的结果。原π、正负x的2和同一个Z均未改变；Γ的L1由Schwartz变换付，不用未知Λ的增长代替。

## 3. 固定一条strip界付整个矩形与全部t

前件为一次给定c>max(σ0,1)和C,N0,T0,η>0，对所有σ∈[1−c,c]、|τ|≥T0统一的poly×exp(−η|τ|)界。它没有从“finite order”推出，也没有改成只控两条竖线。每个先fixed t>0时K_t=max_(σ∈[1−c,c])t^(−σ/2)<∞，两horizontal长度2c−1，原界分别给(2c−1)CK_t(1+T)^N0e^(−ηT)→0；两vertical尾由同一可积界支付。有限高度的竖线不经过0/1，并由亚纯延拓在compact上有界。

矩形右线上行减左线上行的方向，给两留数At^(−1/2)及−A。左线s=1−z时上下端和ds同时反转，FE给I_(1−c)(t)=t^(−1/2)I_c(1/t)。所以全部t>0的精确身份为

 Θ_N(t)=A(t^(−1/2)−1)+t^(−1/2)Θ_N(1/t)。

这是任意先fixed t的证明，已足以供旧Gaussian全性使用；没有额外声称移动t→0/∞的统一有限高度误差。Double poles会有log项，故本分支不能解冻前一原页只列pole位置的宽读。

## 4. 旧561的原质量输入与Euler数据的条件恢复

μ_A=Aδ0+N+反射N已正、偶、tempered，在(−1,1)恰为Aδ0。上式使θ_(μ_A)(t)=t^(−1/2)θ_(μ_A)(1/t)。A>0已独立支付，因此μ_A/A满足旧561固定Gaussian/单位gap的全部前件，得到μ_A=AΣ_Zδ_n。此后才比较同一测度的{1}质量：N{1}=1=A。于是N、M和Z分别是普通整数计数、其log推前及ζ。没有用离散性、free generation、整数Dirichlet支撑或间距作为输入。

若另有原Π，LΠ与logζ的分支由实右端趋0固定，取充分右的实权使差测度有限，沿整条竖线用Fourier唯一性给Π=Σ_(p,j≥1)j^(−1)δ_(jlogp)。如果又**另给**正P和全部repeat关系，j=1正项给P≤Π，故P有log2 gap；compact内j≤R/log2，causal Möbius逆的有限换序系数是n^(−1)Σ_(d|n)μ(d)，遂恢复P=Σ_pδ_(logp)。正Π不被无声升级成预先存在的正primitive，proper powers也未被删掉。

Root最新§5提取的**更强可消费后果**成立：直接给正N支持[1,∞)、N{1}=1和一个Mellin实权有限，加同一Λ/FE/simplepoles/strip前件，令M=(log)_*N即可复用α/A及后续全链。整数识别本身根本不需要Π正、Euler乘积或free generation；Π/P只在另给时读回。这是去掉链中未用前件的旧后果，不能继续拿较弱的单调增量/finite-F分类冒充最强覆盖，亦不由任意N免费生产Euler数据。

## 5. 非空、归属与停止范围

经典Π_ζ取σ0=3/2、c=2确给非空基例。Root新列的10-11 f1-mellin-source-analysis-review§3实际记载DLMF25.2.10的扩大fixed-strip ζ多项式界；003来源31和10-20 canonical-completion-source-and-uniqueness§3实际记载bounded-real-part uniform Gamma Stirling。两旧消费记录支持Λζ于[−1,2]的poly×e^(−π|τ|/4)，故可取较弱η=π/8。这里只核这些内部locator，不将其记作本轮重审DLMF原页，不编数值C/N0，也没有新增长定理。

561的Gaussian/Hermite/单位gap与加权测度机制、旧正Laplace边界以及本稿已逐常数重闭的标准Mellin运输，足以支付上述分类。HL记录只作运输角色背景，未把其原连续函数定理的前件直接扩大到任意测度；这里的真实N反演/Fubini已单独付款。两生产稿中一腿将另一腿标为conditional，root按同一N/A/c核闭后才合并消费，当前不存在循环依赖。

分类只识别Z=ζ；“此类全部有乘法Weil正型”仍与经典RH等强。没有新独立signed/core费用、非零primitive/mixedRR或全源成长运输，whole4/5仅负惯性UPPER保持，Goal完成门仍open。正加法x测度/Fourier号不代替physical log变量的完整Γ/contact、全部pp、双pole和全complex du-Dlog责任。

旧应用0分类合理，不开C050/587或数学轮，不动cadence0/历史50/latest586/formal17。增长前件之外、不同pole阶/Γ/完成背景、仅极限FE/整性的正D′层和joint signed修复仍未排，也不因未排自动有效。Watkins第一桥宽读继续冻结，仅本明示simplepole/质量/strip分支重闭。

next-post-classification-investment-review.md是**尚未执行**的因果投入审视，非formal18、非新source或proof合同；它要求回到同源mixed/完整signed实际新输入，不先弱化当前增长或pole背景造模型。恢复、分类、审稿和推送均不能完成长期Goal。

## 6. 当前版本绑定

规范LF SHA-256，绑定的是本次实际阅读版本；hash不替数学证明或下一动作执行。

| 原件 | raw bytes | LF SHA-256 |
|---|---:|---|
| root-old-coverage.md | 6682 | c97afdce49dcef3b4a6539d7413fc17cdd552ddcdc879ba8a66834fb343731de |
| positive-germ-and-residue.md | 9645 | 5d25e86c84c640baf61e2c87770c351acfbc8d32ce81a554170259c131aa196c |
| mellin-theta-and-classification.md | 8187 | 3e7cde1a948acd303e44ec8d563f0ee857ca2bcb9b1c9afc70a323b6268f9ccf |
| next-post-classification-investment-review.md | 2056 | 2fb307912fa42024661c84de6a78b47238d4050626909840516af66d8ea3b2df |

复核未变的旧核心：561 LF `2494d9b2305979836670d32f3a7558f058e57be361c27edb948ec2ed037571e7`；063 LF `c38ce029f6fa4a26f177e452f13ae324d5fc2045df86c0883aa5dcc75fb0fb1a`；HL原核账 LF `e580fea89efb0ff62ee9718059f856a53d5ee691160d076d72d6f45b08e4302d`。旧件只消费上文所列依赖段，不冒称重审其全部历史。
