# 独立原件审查：Suzuki固定v2 §2与目标身份门

2026-10-28；unit_fresh独占。**限定PASS，来源0止范围准确，未发现需修补的数学消费错误。** 已独立核本地原PDF相关页，不只转述root报告。恢复了真实核／参数范围／Fredholm定义，但未得到新的临界同源输入，不准C050／587或后章proof。此结论不是Hankel／canonical-system全类边界。

## 1. 实际恢复、原件身份与阅读

恢复当前README／STATE、G20261027／1793085111、D20261028T及前沿顶部，check后show通过；按PDF技能使用bundled Python/pypdf，不安装依赖。全文读root当前源稿、source-read-record.json及两份pre-primary咨询。另回核174 OBS-1的实际观察／未付质量范围；没有续其其他分支。

实际复算固定PDF：432186 bytes，raw SHA-256 **2c4cf2aa7a5bca731e0f1ac356deaa082eb6137a07c465fdfe09198acc82ef38**，28页。实际提取并完整目视已有PNG对应PDF **6、7、8、9、14**：§1.7末、§2定义／Prop2.1／Th2.2–2.3及相邻参数／端点说明，p9必要Mellin因子，p14 §4.2的(4.7)–(4.10)定义。p14整页的相邻resolvent证明显示但不作为本审已核proof；未追§3后续、§4定理证明、§5或Appendix。首页只取来源标识／印页日期，邻近abstract及Prop1.1文字随提取显示，未另开其证明审查。

原PDF侧栏1204.1827v2／23 Sep2016、印页Version of September13,2018、metadata CreationDate2018-10-29均实际核到。HTML的2026-08-24按root实际网页观察记录保存，**本审未独立上网核HTML**；不把HTML／印页日期改认新的arXiv版本，不混HTML与固定PDF修订。消费以这组本地原字节为准。PDF／PNG仍仅本地ignored，本审未新下载／渲染／再分发。

| 当前实际LF记录 | bytes | SHA-256 |
|---|---:|---|
| primary-section2-and-target-gate.md | 5821 | 0f990b72fe733956f8c714e1f66a5c320b50a66691b85e0b645a979222e79c1c |
| source-read-record.json | 2862 | d41f3d50e025695458978e26013faf7b4aaea100083b9c5ac181ef985341b0d5 |
| source-normalization-and-cheapest-test.md | 10464 | af9f018129da64b2bc66f3230ebc6ddc376c6f8c48cfe622b5750ef2476aecf7 |
| old-assets-and-net-responsibility.md | 10266 | fb662b7c3964b7c5ae83ea27a266ddf2071ad8322f8b520a6feb336125ab6336 |

实际view的五张PNG raw SHA依页次6／7／8／9／14为c24fd670…／37e6195b…／f07d3cd4…／db01f4dd…／95a0accd…。两咨询是取得primary前的独立库存意见；其“未核原件／未冻结域”只按当时观察消费，当前由原件定义覆盖，不要求它们回写成已读新PDF。真正本地file链接与数学K[t](x,y)表记分开，不把后者的x,y误判为缺失链接。

## 2. 归一化与坐标确实对齐

p9给γ(s)=½s(s−1)π^(−s/2)Γ(s/2)、ξ=γζ，usual ξ无误。§2的cω(n)=n^ω∏_(p|n)(1−p^(−2ω))、gω的两项及hω(x)=x⁻¹Σ_(n≤x)cω(n)gω(n/x)与root稿一致；n为全部整数。Jordan权不是Λ，非负Euler乘积也不支付Hankel／Weil PSD。

hω在x<1为0，有限[1,b]的L¹／L²阈值分别是ω>0／ω>1/2；ω>1才有这里需要的连续核。整数端点奇性没有被随意填成连续。Prop2.1的绝对Mellin身份只在Im z>1/2+ω成立，s=1/2−iz；p9显示完整γ比与ζ比共同生成，不能只保ζ或arch近似。

原Hilbert域为L²((0,∞),dx)，Hankel积分为hω(xy)dy；Th2.2的乘法卷积则是hω(x/y)dy/y，两者没有被混成一个核。原截断P_a是(0,a)。酉换元v(x)=x⁻¹/²r(logx)给log域u<log a，核准确为

\[
K_\omega(u+w)=e^{(u+w)/2}h_\omega(e^{u+w}).
\]

外面的e^((u+w)/2)不可省，也不能把原域改[-a,a]。ω>1、每fixed a的aM bound是原连续Hankel读出的充分费用；常数依a／ω，不是完整Bζ预算。physical源窗、cutoff a、ω及频高仍分别量化。

## 3. 边界乘子、causal身份与不同ω范围

实轴a.e.模1给合法L²边界乘子／Watson involution；这不自动给其等于算术因果hω的全域算子。p6明确H**=Hω须inner前件。Th2.2逐项给**所有**f∈L²((1,∞),dx)上的卷积身份、相应支持保持或全输出L²条件与inner性等价。高线绝对Mellin表示不足以无条件移到实轴因果读出。

Th2.3的完整显式系统按ω>1、全部a>0引用：连续核HS自伴，a≤1时H=0，I±H可逆；m=det(1+H)/det(1−H)，Hamiltonian为diag(m⁻²,m²)，在a=1匹配原(Aω,Bω)。内外比值、幂次和端点规范均与root稿一致。这是有准确前件的cited定理，本审不重证。

p8–9另外陈述ω>1/2的HS／I±H可逆、以及ω≥1/2的inner性已有无条件结论；这些不等于完整显式系统已推广。原文把系统向ω>1/2的推广写为plausible，向全部ω>0的推广还涉及RH前件。严格大于／大于等于的阈值不合并。p9明确a→∞端点行为**即使ω>1也仍开放**；每fixed a的系统存在或正矩阵不支付该端点及ω↓0的共同量词。

## 4. det定义与未付目标

实际目视p14 §4.2(4.7)–(4.10)：det由连续核的经典Fredholm级数及积分minor定义。不是本门已证明的trace-class算子谱积；HS本身不证明trace class，也不允许悄换det₂。这不是断言实际核必非trace class，更不否定在原ω>1定理范围内已引用的det非消失；只是保原定义和实际证明等级。

174的Hamiltonian det-one／noncollapse是另一项未付质量责任，不能拿来代Fredholm det(I±H)非零。实对称／自伴核也不等于PSD，Hamiltonian正号首先属于它自己的canonical域，不自动给原physical两源Bζ。

形式字典∂ωlogΘ|₀=−2ξ′/ξ仅在合法非零解析域校准，保Γ、1/s、1/(s−1)和ζ′/ζ；它不是critical核／算子可微性、D′极限或独立positive identity。字面Θ₀=1也只在相应解析意义下约分，不是临界分布极限平凡的反证。有限ω的完整高阶内容不能仅凭一阶字典抹去；旧literal和核反测也没有直接否定本Hankel构造。

实际未付仍是canonical／shifted读出到同一未移位完整Weil型的两源运输、原norm及临界／端点费用。完整Γ／FP-contact、全部Λ(p^k)=logp和双pole不能因同名ξ已在比值中就视为正确接入。已读范围未给承担这项新净预算的原命题；不据此声称整篇没有相关数学。

## 5. 来源0、停止与长期范围

当前真正新增的是原件身份和具体设施／前件范围的恢复。174已经有该准确locator及安全ω canonical观察，原件核读没有支付all-ω临界非退化、a∞或完整目标身份的独立新输入。因此单章来源0止准确：不准小ω可逆性、HS延拓、临界紧致性或后章proof合同，不建C050／587，不续§5／Appendix／新paper。

这不因RH等价强度排斥未来真实非循环算术证明，也不泛排Hankel／canonical系统。正D′规则不被强加逐层exact Pan／ordinary trace；553只在actual total必要读出确有原global norm前件时使用，不套未定义或不同空间的reader。比例／zero-free优化继续暂停。

本审只写本文件；现有cadence0／历史50／latest586／formal17保持。Whole4/5仍仅负惯性UPPER，独立signed/corecross／同一非零primitive mixed／Ξ瓶颈未改，Goal同实例active、open／noteligible。没有新增证明、core-class边界或已存在的继任公式；不把未付前件改名input，不因来源停止complete／blocked长期Goal。root后续实际消费、发布及远端核验不由本稿预认证。
