# 根来源核算草稿：真实section、theta RR与尚缺的mixed桥

2026-10-29；固定van der Geer–Schoof math/9802121v3，仅§3 Proposition1及必要§2定义／相邻Q例子，不顺读§4以后。本文是root独立核算，待独占source稿、不同fresh及根收据，不自称新数学成果。

## 1. 原件与实际范围

原始v3已从 https://arxiv.org/pdf/math/9802121v3 下载，405773 bytes、21pages、SHA256 39ddc65d010a2f568f46de7e5418ea0be3f995f6eb98dca2a850a0ac8ed52111，实际路径literature/local/arakelov-theta-rr-source-gate/van-der-geer-schoof-math-9802121v3.pdf。git check-ignore已核，全文／提取文本／页图仅本地。摘要显示v3修订1999-06-29，期刊出版2000；当前PDF标题同v3，pdfinfo显示文件由2024版Ghostscript重制，不能将文件制作时间当数学版本日期。

Root读PDF2–8整页提取文本，消费仅§2所需Div/Pic/degree/metric定义、§3 effectivity/h0、PDF7 Proposition1及PDF7–8开头Q例子；PDF4 variant、PDF8其它例子仅随整页出现，不消费为修补或新预算。已实际渲染并整页视觉核PDF5、6、7；Poppler渲染5/6有字体警告，但已核关键定义／公式清晰，不以退出码代视觉判断。固定runtime的pdftotext缺失，实际用已有TeXLive pdftotext提取；渲染/pdfinfo用bundled Poppler。没有新PDF编制或数值实验。

## 2. 来源明确支付的对象及RR

Arakelov divisor有限位系数是整数、无穷位系数是实数；I_D=∏P^(−x_P)，degree=Σx_P logNP+Σx_σ。Principal(a)有ord_P(a)，实位−log|σa|／复位−2log|σa|，由乘积公式degree0，Pic为真实principal商。I_(D+(a))=a^(-1)I_D，z↦az给保metric的O_F-linear同构，因此theta截面量在Pic类上定义。

原文先回顾smallsection集合，再明确采用不同的Gaussian加权全部sections：H_theta^0(D)作为群是无限格I_D，

    k_theta^0(D)=Σ_(f∈I_D) exp(−π||f||_D²)，
    h_theta^0(D)=log k_theta^0(D)。

不是log#smallsections，也不是几何vector-space维数。原文Proposition1为

    h_theta^0(D)−h_theta^0(κ−D)=degD−(1/2)log|Δ_F|，
    degκ=log|Δ_F|。

Poisson给两个Z-dual格的theta恒等式，Gaussian使两端对称。本文准确消费这个经典算术RR；没有独立h1而不借duality的构造（本页作者明确限定），也没有从RR差值推每项容量下界、两源Hodge index或经典完整Weil型。

**原版求和下标的限定纠正。** 独占source审稿指出、root再核完整PDF7可见：显示的Poisson求和下标印作f∈∂I^(−1)，而同页κ的ideal明确是different的inverse，§2的∂也是different。按同一divisor/ideal定义，I_(κ−D)=Iκ I_D^(−1)=∂^(−1)I^(−1)；trace-dual也须这个inverse different（Minkowski complex坐标允许标准共轭等距，不改Gaussian和）。所以不消费原印下标为generalF identity：先冻结该literal下标，再以这条实际canonical ideal计算重闭正确的RR源。原PDF保持不改，不将整个Prop1判错；F=Q的∂=1，此处下标差别消失，本文实际rank1／smallsection／product对照全部不受影响。此修正只限本次新来源记录，不外推既有KRY/CCM或别的semantic冻结。

## 3. Q的实际rank1 multiplication及两种计数

对Q，Pic(Q)经degree同构R。类D_x由I=Z、实位x表示；线对象L_x=(Z,||n||_x=|n|e^(−x))。

    L_x⊗_Z L_y ≅ L_(x+y)， n⊗m ↦ nm，
    ||nm||_(x+y)=||n||_x ||m||_y。

这里是同一实际整数格／rank1 tensor的metric等距，不是complex weighted cycles或原Weil源的假线丛。Smallsections S_x={n∈Z:|n|≤e^x}满足S_x S_y⊂S_(x+y)，但set product有大量碰撞，不能把它叫两个section集合的injective tensor计数。作为Z-modules的tensor同构则完全合法，二者不能混。

    hat h_small^0(x)=log(2 floor(e^x)+1)，
    h_theta^0(x)=log Σ_(n∈Z) exp(−πn²e^(−2x))。

对任意x<0，前式=0而后式>0（±1项均正），故不是同一统计；无需数值诊断。Q的RR是h_theta^0(x)−h_theta^0(−x)=x，保两端，κ=0／Δ=1。Principal类=0时theta h0仍等于其固定基值h0(0)>0；这只是非线性section量在零类的值，不是principal产生非零除子类，不能拿它错误反驳principal商。

Gaussian权也不是乘法character。设a=|n|e^(−x)、b=|m|e^(−y)，productsection的权是exp(−πa²b²)，而两个section权的乘积是exp(−π(a²+b²))。例如n=m=1，取x=y=−log2得a=b=2，前者严格小于后者；取x=y=log2得a=b=1/2，方向反转。所以合法norm乘法不自动给全sections的Gaussian权单向比较，碰撞也不能忽略。这里只否定这个直接权搬运，不排付费／不同组织的容量定理。

两者在固定x=y=0也可用n=m=1／2给反向权比较。进一步，Theta(L_x)Theta(L_y)是独立(n,m)的正交直和格Theta(L_x⊕L_y)，不是rank1 tensor线L_(x+y)的Theta；前者的h0可加不能移给后者。Theta的整数幂对应rank增长的directsum，真实line的tensor幂仍rank1、参数nx；不能把这种幂免费作为Goal所需非平凡local tensor／全阶global pole输入。本门没有读取或消费后文两变量zeta章。

## 4. 两槽mixed和原源接口

本章给单divisor的非线性函数及dual RR，未给project所需的实际r↦D_r／same nonzero primitive、全405 Pan及平移的principal证书、537非根和全源coverage。原文此章的principal是a∈F*；405的无限维非compact源关系不是它的别名。不能把∫r(x)[L_x]dx按定义叫整线，或将Pan像改称principal。

若另提案只把r送到固定有限个linear degree/metric参数，再对h_theta^0取mixed Hessian，则Q rank1给h_theta''(x)ell(r)conj(ell(s))之类有限rank槽。旧有限channel核反测已付：原537正窗中有限多个linear条件有非零compact共同kernel，完整Q_W在那里严格正。此条件比较仅适用于该实际有限参数提案，不排growing/source-adaptive family、额外relative frame或非local强域；它们在本章没有给出。

RR的成立不等于mixed capacity成立，norm乘法也不等于Gaussian权乘法，更不等于完整Weil identity。新颖性扣旧：573已有P¹_Z integer sections／过滤／metric控制，307已有真函数域RR/Hodge，552/553及correctedscalar theta已有合法metric/Poisson／源费；本章增补实际theta-h0语义和精确经典来源，未给比这些更强的核心输入。

## 5. 拟消费结论及停止

应保存并入库这一原件及准确source scope；既有同paper直接消费没找到，不声称历史首次读。一次§3来源门已实际执行，不晋级C056/593，不计数学轮；不因后文未读、引用或rank2／两变量标题继续来源队列。旧sameB/closedbase/CCM语义冻结及paused比例／无零区域保持。

完整Γ/contact、properpowers及双pole、原du/Dlog／strong源费、成长coverage/coupling均未由此RR运输；sameprimitive/principal/sections/mixed和signed corecross/Ξ关键瓶颈未改变，whole4/5仍负惯性UPPER。只停止本章直接提供桥的提案，不否定算术RR或全部relative/higher几何。长期Goal同实例active/open/noteligible。
