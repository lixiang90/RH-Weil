# Notes 301–437：Weil/F₁历史回顾

固定仓库：`E:/codex-build/RH-Weil`，HEAD `331107b2ba0716d2fb78ec1f605f05fe57393274`，复查日期2026-10-11。本报告只讨论历史与后续研究准入，没有续跑比例、无零或507AM计算。共137篇：75篇全文深读（307、363、365–437），62篇实质全篇结构survey（301–306、308–362、364）。后者核读全节结构、节首数学对象、命题/证明路径与结算/限制摘录，未逐行重算中间公式；不把它们冒称全文深读。外部论文的已引用结果与本次独立本地推导始终分开。逐篇路径、原字节SHA256、readscope与判断见[reading-ledger.json](../weil-f1-retrospective-coverage.json)。全部源文件哈希在交付前复核未变。

## 判断

这段历史不是“不断失败所以F₁不存在”。它已建立真实的单p截面—Cartier—零测度接口、实际adelic来源的完整算术恒等式、真实交叉积与源保持域、真实相对HH₁电荷。失败集中在把这些对象接成同一个全局Weil平方：普通主商会塌缩两次数，通常逆/双对偶极限会抹去图，原算术周期读出不能在源稳定的范数完成中连续传递，而原线性物理有限部甚至不能定义于一个合法有限源词。无限全局RR、有效截面及正交叉并未因此得到。

363已经指出算术site及其平方有真实已知构造，不能说“整个平方尚未构造”；缺的是指定ζ算术与平方交叉、主关系、RR、有效下降的共同实现。[363:12](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/363-f1-arithmetic-geometry-and-existence-audit.md?plain=1#L12)、[363:180](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/363-f1-arithmetic-geometry-and-existence-audit.md?plain=1#L180)。截至437，正确问题仍是“哪条来源自然、域稳定的比较先能成立”，不是再假定目标正性包存在。

## 实际交付及没有交付的东西

| 链段 | 已有实际对象/已证比较 | 尚不能推出 |
|---|---|---|
| 301–303 | 移动簇相位抵消；实际前缀硬商负秩保留而负迹塌缩；共同计数/固定germ不识别边界预算 | 不是ζ离线零点模型，也不验证实际尖锐窗残余Gram下界 |
| 304–306、308–346 | 凸谱二阶接口、现有文献基线与勘误；深簇/共同λ条件性预算；真实物理determinant、有限域/Kloosterman及Poisson转换有合法中心/端点/尾成本 | 近点廉价、实际覆盖、非零相关相消仍未获独立算术输入；改写可逆不产生节省 |
| 347–362、364 | 固定半径实际传递；R≤4指定势的全窗口上限；R=5精确窗口/核界；有限图PASS与连续候选FAIL明确分开；冻结表完整验收 | 未得全域有界势；停止指定候选不排全部谱路线 |
| 307 | F5椭圆曲线先由有效同态次数得到正二次型，再核准F、J、全扩域迹与ζ | 这是非循环的经典模型基准；不是数域全局正对应/统一Frobenius/全H¹比较 |
| 365–371 | Witt全character算术作用、solenoid/周期解析层、实际局部线丛/截面；几个特定层的明确no-go | 单character、普通复幂、局部有限circle层不能免费提供全实算术作用与线性系 |
| 372–375 | 真实period ring、twisted φ modules及FF曲线；允许整数degree/χtorsion的有效截面；带闭点次数权的Div/principal/Pic comparison | 只有单p及整数部分；不等于全部实Pic、算术平方交叉或ζ全局RR |
| 376–389 | 真实实指数系数扩张与perfectoid annuli/φ解析商；所有既有非零完成global函数在有理局部Cartier；唯一几何Radon零测度、fullsupport、单位/乘积/pullback/φ下降及精确heightpush | 不包括任意局部函数延拓、全GAGA、两侧degree、连续实对应及全局RR |
| 390–403 | source容器与G字段准入明确；真正H⁰分类、profile满射；实际perfectoid平方/完整图；pro/ind对象及精确极限缺陷 | 容器非空不是好结构非空；profile维数不是解析RR；fullgraph不是通常Cartier；局部支集配对与固定Weilmixed冲突 |
| 404–406 | 真实adele点/周期轨道、Jacobian及有限S局部迹；完整sharp测试的L/2=N；实际限制闭理想与双矩/完整配对的正确radical；实际单位/Fredholm铅笔 | 谱消失不是主除子；logdet单位标签不下降；辅助z除子不是算术主除子 |
| 407–420 | 实际有限箭头/源完成/相对扩张；fullQ相对类、Haar横向压缩的ρ权及Lp；真实timecrossedproduct、Green源/提升、Hardy指数线丛与dualaction | 普通K类线性读出失prime-power权；缩pZ不是完整Q源；ordinary指数/Chern数不携带完整算术迹；有限循环迹扩张有实际端点矛盾 |
| 421–437 | S₁/ℓ¹ finitepart与边角异常；source-stable周期核代数、精确有限词商、canonical HH₁电荷；全部固定源共轭Haar迹及完成平均读出；真实有限词FP反例 | weightedchain未闭；相对锥简单补链抹去全部周期；源不变截止失原p周期；norm极限不保period；全J线性physicalFP不可自动存在 |

单p链是有实质正向交付的。375把period轮廓接到了同一个实际FF曲线的几何主除子、有效截面和Picard商，核不是被假定消失。[375:80](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/375-f1-geometric-divisor-and-picard-comparison.md?plain=1#L80)、[375:117](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/375-f1-geometric-divisor-and-picard-comparison.md?plain=1#L117)。389把接口推广到全部既有global完成函数，零测度按真实Kummer计数稳定极限构造；其单位相容性没有凭径向权重宣告。[389:96](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/389-f1-canonical-zero-measures-for-completed-functions.md?plain=1#L96)、[389:137](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/389-f1-canonical-zero-measures-for-completed-functions.md?plain=1#L137)、[389:181](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/389-f1-canonical-zero-measures-for-completed-functions.md?plain=1#L181)。这些应保留作局部来源，不能因为后面的全局接法失败一并丢弃。

算术恒等式也已超过“形式猜测”。404从真实adele周期、局部Jacobian及固定有限S截止得到离开单位元的混合比较，并明确该测试不能确定δ₀常数。[404:69](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/404-f1-adelic-periodic-orbits-and-mixed-local-trace.md?plain=1#L69)、[404:184](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/404-f1-adelic-periodic-orbits-and-mixed-local-trace.md?plain=1#L184)。405按指定Fourier有限部分固定了单位常数，给

\[
2B(f,g)=d(f)c(g)+c(f)d(g)-T(f,g),\qquad
P_{\rm an}=I\cap\ker d\cap\ker c=I\cap\operatorname{rad}B.
\]

真实限制关系h=ξ/2有d(h)=c(h)=1/4，B(h,h)=1/16；故I⊂radT不意味着I⊂radB。非零p=(D²+D)h才满足双矩与全Bradical。[405:125](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/405-f1-adelic-restriction-moments-and-radical.md?plain=1#L125)、[405:199](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/405-f1-adelic-restriction-moments-and-radical.md?plain=1#L199)、[405:227](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/405-f1-adelic-restriction-moments-and-radical.md?plain=1#L227)。这是真正通常ζ的来源/恒等式，不是新“假想ζ”；但P_an是来源中的解析最大可容许子空间，还没有由几何函数/截面的单位商与主除子图实现。

## 全局RR、截面与正交叉仍缺哪些联合条件

不能把393的CCfiltered dimension formula当作解析Euler定理：正w的H⁰实际为无限维；Banach非零截面的profile局部常值，其诱导商拓扑离散，而CCprofile拓扑允许连续实常数变化。[393:124](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/393-f1-profile-surjectivity-and-filtered-dimension.md?plain=1#L124)、[393:127](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/393-f1-profile-surjectivity-and-filtered-dimension.md?plain=1#L127)。全局所需截面必须在同一个来源、拓扑、主关系与平方上有效下降；不能只逐对象找到一个有相同profile的截面。

尚缺的合约是：实际D_f的全实对应与复合异常；双次数在主变换下不变；对角自交/相对迹含单位和实位有限部分，二次项精确比较；足以从错号自交导出非零有效代表的RR不等式、对偶性及剩余上同调控制；最后证明非零有效对应不能degree=codegree=0。[363:180](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/363-f1-arithmetic-geometry-and-existence-audit.md?plain=1#L180)。363引用CC的s(f,f)≤0符号，与仓库正W约定相反；不得混换。当前没有证明这整套假设弱于RH。

395给了十分具体的缺口：若把当前singlecurve零测度生成空间及P₀当作整个除子/主空间，所有连续principal不变量仅总质量，分别连续且principal消去的B只能是k·mass⊗mass。扩大weakclosure也不恢复第二个degree。[395:64](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/395-f1-geometric-measure-principal-quotient.md?plain=1#L64)、[395:133](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/395-f1-geometric-measure-principal-quotient.md?plain=1#L133)。396的flatline区分b/pb及397的真实norm/pushforward修补动作，并没有恢复独立的两侧degree/交叉来源。

## 指定模型no-go与F₁总体问题的界线

| 已证停止点 | 精确排除范围 | 未排除范围 |
|---|---|---|
| 370、371 | 局部有限circle解析周期层；通常复Tate几何p=id与算术p id的指定intertwining | 无限Witt层、其他base/范畴；更大F₁/Λ方案 |
| 377、395 | 有理值Gauss完成不能给指定irrationalprofile；当前单曲线continuousmeasure主商仅mass | 真实实指数扩张（378已实现）；额外平方、metric/relative/derived几何数据 |
| 398 | 给定perfectoid平方上完整闭图核I=closureI²，因此通常有效Cartier解释失败；每个有限F_n仍Cartier | 其他square或广义cycle；不是所有F₁平方不存在 |
| 400–402 | 通常O层lim=(O,1)；stalk/lim失配；J非locallyfinitegen且J∨∨=O；intrinsicFF普通Qp对角conormal无限 | pro/ind保留数据、层化/堆化对象、continuous/derived不同base；这些必须单独付新比较 |
| 403 | 高度比分层+保支集叠加+支集不交配对零三个条件共同失败 | 有真实非局部贡献的来源；G0–G8没有强制所有B支集局部 |
| 406 | 指定expunit的无补偿Cartier型logdet读出及连续线性killunit后双矩保留失败 | 带实际metric/Green补偿的单位商；规范线性铅笔除子可恢复trace，但仍缺算术来源 |
| 419、421–424、427 | 保ordinaryrank1归一化的有限scalarcyclictrace；完整A₂非scalarweighted闭性；指定S₁/BV原子机制；标量twisted扩张/简单锥；全corner循环扩张 | 非半单四分量、真实relative/higher链；原全Γ测试后迹不受fixedB前提排除 |
| 429、431、436、437 | 旧corner域不source稳定；有限支持词的1−Adu单射；norm完成不传period；指定p2q5合法源词无linearvolumeFP | 新source稳定域（430已给）、无限固定sector（433已给）、保phase/截止传递并独立认证的relative机制 |

尤其400的通常极限与pro对象不同：图点先取茎才得到乘F₀的非满比较，不同层的局部逆无法在共同邻域给一个相容解析序列；未层化Čech需要跨所有integer分支统一sourcelevel而失败，局部stackification可组织对象但不能宣称普通全局pro塔/RR已获得。[400:162](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/400-f1-cartier-tower-limit-and-stalk-defect.md?plain=1#L162)、[400:188](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/400-f1-cartier-tower-limit-and-stalk-defect.md?plain=1#L188)、[400:247](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/400-f1-cartier-tower-limit-and-stalk-defect.md?plain=1#L247)。401逐茎rank1/flat不等于局部线丛，O/J有限Tor维仍非perfect，不能直接给行列式交叉。[401:71](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/401-f1-dual-cartier-ideal-and-reflexive-collapse.md?plain=1#L71)、[401:111](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/401-f1-dual-cartier-ideal-and-reflexive-collapse.md?plain=1#L111)、[403:50](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/403-f1-support-locality-and-nonperfect-quotients.md?plain=1#L50)。

## 八条跨篇经验与目标漂移

1. **先拿实际对象，保留比较的方向。** 307从曲线次数到正性再到纯谱是可靠范例；372–389从真正环/模/函数到divisor也有实质交付。反过来先赋pure spectrum/positive norm，或者按W值定义几何B，会把目的当输入。
2. **source、relation、radical、principal是四件事。** 405给h的1/16残差，406给exp(p)的unitdivisor0，即使p已经Bradical也不能把它标签叫几何principal。源有非零关系不等于已存在主除子理论。[406:108](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/406-f1-adelic-units-and-determinant-divisors.md?plain=1#L108)
3. **逐对象存在不够，必须同一线性系与拓扑。** 367–369、375、389可局部有效化；393显示实际profile满射不提供连续sectionlift/解析RR。301同germ不同boundary、302小负迹仍负秩、359有限图PASS/连续FAIL，都在提醒不能把弱观察当全配置。
4. **补全/商/下降/茎不能任意换顺序。** 394–395 weak主closure塌缩degree；399strong图核与TV不同；400ordinarylim抹图；401doubledual抹J；433有限word边界单射但完成有noncompactfixedsector。它们是精确反例，不是抽象说“无限很难”。
5. **允许换对象，但须登记失去的合同。** Hp→Q（368）杀torsion；FF→realcoeffperfectoid（378）支付realPL却失旧regularNoetherian接口；ordinarysquare→pro/ind/FFintrinsic（398–402）需新Cartier/trace；fullQ→pZ（409–410）恢复Fredholm但缩源；u→T（426–429）只给商unit并丢非紧新边。这些合法实验不能在后文被倒算为原合同成功。
6. **有算术迹不意味着principal消去，有K类不意味着正确权重。** 411实际τ=2a logp而Weilprimepower系数应logp；412实际Haar壳/时间平滑才给ρ^a。413–420K边界/ordinaryChern不携带全部标记；同一boundary不等于Bradical。禁止重新命名整数或给图自由标(b,1)。
7. **域稳定比形式循环公式更早。** 419真实移位的交换子迹1阻止有限循环extension；421bΨ_W非零；423twisted修复仍有wrongmixedatom；424简单relativecone取消全部period。427真实ω非零，429实际u不保旧域，430才把finiteword准入补齐。止损有效，重用旧域会成为目标漂移。
8. **截止来源不能由强/范数极限抹去。** 425physicalball与wavecutoff同stronglimit而period不同；432source-invariantxcutoff只有unit；435fixedconjugates保持period却unitflux依partition；436normCesaro极限丢p周期；437finiteword无任何linearFP。正确停机对象是全J无phase线性FP路线，不是全部F₁。

## 优先研究合同一：先付437的相位，暂停RR

固定437的真实p=2,q=5、合法c,d、原A/u/J及Y=A(h)uA(k)，不引入假定的neededsource。该词已在真实最小源理想中。其p边原Haar迹是

\[
T_K=\sum_{n=1}^{K}P(nL)+H(KL),\quad
H(\theta)=(1-r_0)\sum_{d\ge1}r_0^{d-1}P(\theta+dL),\quad r_0=1/2,
\]

其中P由原periodic Gram核与c²的实际积分给出，M周期且非恒定；θ_K=KL modM是真实cutoff相位。[437:46](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/437-f1-finite-source-word-without-a-linear-physical-finite-part.md?plain=1#L46)、[437:69](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/437-f1-finite-source-word-without-a-linear-physical-finite-part.md?plain=1#L69)。不能再尝试减常数aK得scalarFP。

第一有限命题是：从**该source-derived P**证明或反驳有连续/光滑M周期G满足

\[
G(\theta+L)-G(\theta)=P(\theta+L)-\overline P,\qquad
\int_0^M G(\theta)d\theta=0.
\]

若成立，由望远镜精确得到

\[
T_K=K\overline P+G(KL)-G(0)+H(KL).
\]

这保留相位及Haar球尾；零均值以实际周期Haar与原赋值起点固定，不能用期望Weil数值挑G。Fourier形式必须处理\(\widehat G_n=z_n\widehat P_n/(z_n-1)\)，\(z_n=e^{2\pi inL/M}\)。单凭无理性不足：须独立核实log2/log5的有效对数线性型下界或直接给这批P的收敛界。现在没有把任何尚未核读的外部小分母定理当作已付输入。

验收是实际G、收敛/正则性界、原434核迹到此精确等式及S₁误差Tr(P_KSP_K)→TrS；随后仅检验一个闭合的finite-source-word子族在乘积、u/u*、伴随下的phase传递律及更换合法辅助分割的变化，不能宣称覆盖全部J。退出条件：Fourier级数不能在合同正则性收敛；只形式添加phase字段没有真实截断等式；需要挑subsequence/自由平均；或者u/乘积产生未经认证新边。成功只支付source-word截止自然性，不恢复旧scalarFP、不选择prime weights、不证明RR。

## 优先研究合同二：真实闭链与403的非局部混合benchmark

在合同一实际允许的phase域或另一个逐词已证域中，保留原source A_src、普通S₁ ideal、原physicalball与432真实source-invariantx cutoff的差异、435的Wh(0)、427的ω及完整混合行。432已给**只对商上一循环**定义的canonical

\[
\Omega(c)=\operatorname{Tr}\sum_r[A_r,B_r],\quad
\Omega:HH_1(Q_{\rm src})\to\mathbb C.
\]

它不是尚待假设的新泛函；但是原q(u*)⊗q(uF)的边界q(F−uFu*)非零，不能强称闭链。[432:21](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/432-f1-relative-cycle-charge-and-source-invariant-cutoff.md?plain=1#L21)、[432:56](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/432-f1-relative-cycle-charge-and-source-invariant-cutoff.md?plain=1#L56)。先从实际两个截止/源变换的边通量与phase传递构造一个**规范且合法闭合**的relative chain（复形、各腿理想、边界公式必须明确），再计算，不能先假定规范i∈I存在而把目标period填进去。

第一道算术检验固定403的f=φ、g=φ(·−log2)，0≠φ≥0小紧支。430–437的两个有限位Hilbert来源虽保留物理实时间，却不能自动等同于无穷位局部几何：403的完整N还含实位积分。故先以404已经存在的固定有限S={∞,2,5}源为输入，明确它到上述relative chain的真实比较；这座桥必须构造/检验，不能作为额外存在假设。仅在原两有限位域算出prime2原子属于局部比较，不能算完整G6测试通过。桥成立后必须从实际source chain独立算出非局部混合贡献，并与

\[
W_{\rm pol}(f,g)=N((f*g^\sharp+g*f^\sharp)/2)
\ge \frac{\log2}{2}\int e^u\phi(u)^2du>0
\]

比较，保留原反射f♯(x)=e^(−x)f(−x)、半迹及实位。[403:18](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/403-f1-support-locality-and-nonperfect-quotients.md?plain=1#L18)、[403:35](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/403-f1-support-locality-and-nonperfect-quotients.md?plain=1#L35)。只证明某个prime2原子或下界还不是完整混合比较；此测试不在双矩零子空间，验证的是G6全部测试量词，不用RH。

现有旧corner循环q(A(f))⊗q(A(g))读出的ω=−4∫s f(s)g(−s)ds在这一分离支集测试为零，故ω本身不能充当该B。[427:104](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/427-f1-corner-product-algebra-and-unavoidable-trace-cocycle.md?plain=1#L104)、[432:48](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/432-f1-relative-cycle-charge-and-source-invariant-cutoff.md?plain=1#L48)。需要的非局部贡献必须真来自新闭链/边通量，不能沿用locality失败模型。

退出条件：仍为431–432的非闭finiteweightedchain；424的exactrelativeboundary只把全部period取消；得到428任意time-distribution自由度；丢原Haar球或依赖436禁止的norm延续；437线性FP再次被默认；从W倒定义链/配对；只换K群或auxz除子名称。一条出现即停止该接法并记为范围内no-go。若混合例子通过，还须单位时间/Fourier常数、辅助分割传递、实际单位商与双矩radical联合测试；这些成功之前不进入RR/positiveintersection，更不声称全G6/G8。

## 交付边界

本报告未修改正式笔记、formal、论文、旧review或Git；只在指定late目录保存阅读审计材料。没有外部网页新检索、没有重新跑证明脚本、没有认证外部论文全证明。判断基于上述本地源；数值/Lean PASS始终限各源自己声明的有限代数/组件范围。真正应保留的是实际局部Cartier与全ζ恒等式资产、真实源域及已经清晰化的失配；真正应停的是没有新source比较却不断重命名同一trace/readout的研究循环。
