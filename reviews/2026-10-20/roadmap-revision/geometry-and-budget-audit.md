# 旧路线图之后的几何与全位预算审计：568、569及Landau–Siegel专题

2026-10-20。供修订路线图消费的独占审计稿；用户本轮要求战略回顾，未启动新数学合同。
同G20261014／0c4f≤538冻结基线。本稿不更新公共STATE、cadence或Git，不执行外网搜索，
不声称截至当前日期的最新文献综述。结论沿最终原件和root消费记录，不重新计算研究轮数。

## 1. 现在需要修订的主判断

旧[路线图](../../../goals/reviews/2026-10-20-generalized-weil-facilities-literature-roadmap.md)
的九项设施仍有用，但后三步研究使“缺什么”的表述必须收紧：

1. **不能再说完全没有由源构造的非退化评价载体。**
   [568](../../../notes/568-source-evaluation-carriers-local-jets-and-weil-capacity-gap.md)已给
   \(J_W:r\mapsto W*r\)、全配对根商、分离点评价以及每个有限维子空间上的非零minor。
   缺的是可乘的全局截面源、实际restriction/kernel和独立局部—全局容量；
   非退化卷积像不是局部函数环，不能用LS的乘积整除论证。
2. **不能再把双conormal固定权／finite-part门列为尚待执行。**
   [569](../../../notes/569-dual-carrier-gamma-normalization-and-budget-cocycles.md)已执行：
   单叶all-k链和共同character不匹配实Γ；独立normal parity可条件修复穿孔形状，
   完整contact由指定Tate/Fourier/Haar规范校准。直接标量翻译已停止，不能调κ续约。
3. **不能再把“允许各预算片协同变换”本身当容量新输入。**
   569已给完整实cocycle和全纯projective phase相消，连续正反例、函数域真反例都通过。
   这修复了568的“各片无补偿分别下降”失败，但没有区分primitive正号。
4. **评价det路线得到成功原型，但没有取得经典全源比较。**
   [LS专题](../../../goals/reviews/2026-10-20-landau-siegel-determinant-and-weil-facilities.md)
   的同一整数minor承受非零性、有限位整除和无穷位高度预算，是具体独立算术输入；
   它只控制真实二次character的标量惰性prime偏置，未给任意complex源的mixed预算身份。

因此几何主责不应继续写成“造非退化carrier／det line／匹配Γ”，而应写成：
**在真实可乘global source上，证明局部消失过滤与全局容量的约束，再识别其signed
primitive二次项为已经固定的完整W。** 当前没有这一步的经典新输入。

## 2. 旧承诺、实际落点与仍欠前件

| 旧路线图的承诺或候选 | 新研究实际闭合／失败的范围 | 仍欠、停止和可保留修复 |
|---|---|---|
| 设施F3：source-faithful／非根carrier | 568的signed \(\mathcal D/\ker J_W\)确实存在；全部point probes分离，finite-subspace minor可非零 | 不给pointwise乘法、整数格、Frobenius reduction、全局sections、Hilbert正metric或faithful trace重数 |
| F5：局部评价与jets | 闭点分布给真实finite étale代数、residue jet配对、raw正Frobenius；真曲线和290反模型都通过 | 自由local target不提供同一diagonal global source；raw点数载体不是primitive H¹；有限维大小不等于RR容量 |
| 经典评价的原norm合法性 | 完整Γ/pp/pole的J已明示；point/jet对原fixed-window Dlog不有界；fixed smooth probe合法 | 只排该J的无费point/jet；保Hˢ增强、平滑probe、relative/nonlocal和源适应修复，但必须支付返回原norm的费用 |
| 预算片下降与det line | 568在full-Q零类上pole和arch−prime为±1/8；569付全complex cross及phase的matched transport | 只排无补偿分别下降；真det evaluation complex、principal source及独立capacity仍欠；指数metric的纤维正不是正曲率 |
| 第1工作包：Γ双carrier来源 | 569核all-k共同权无匹配；最小log FP下完整contact已校准，κ=2差核可付 \(\pi/2+\log2\) | 差核Fourier变号；normal parity、Euler系数/负号/重数和global延伸须有真实来源；不排多叶/奇异/非局部几何 |
| 评价det／collision预算 | LS专题核同一个D的Wronskian非零、unitriangular高阶整除和全部高度/导数/阶乘费 | D≠0不是Weil Gram正；标量profile不是全部振荡mixed方向；不得用目标Q反定义arch上界 |
| 平方RR与增长容量 | 567的带cutoff预算仍是可用条件接口；本组研究没有补出经典 \(C_j,\epsilon_j,\eta_j\) | 2018§3.4仍不是已证平方RR；2023一次RR及2026实际O(D)不是所需二次项；393轮廓维数不代解析H⁰维数 |
| actual正迹备选 | 560同源positive ordinary trace−signed compact K＋完整双pole仍是几何比较器 | 本稿不重审570–572的技术证明；依各结算它们未付actual Sonin全源成长容量；不能把模型δ付费替换真实误差 |

上表消费范围以
[568根收据](../evaluation-carrier/root-consumption-scope.json)、
[569根收据](../dual-gamma-cocycle/root-consumption-scope.json)、
[LS根收据](../landau-siegel-inspiration/root-consumption-scope.json)为准。
哈希只固定版本，不支付证明或容量前件。

## 3. 三种source角色不能再压缩成同一个商

固定完整Hermitian源W、原紧支复测试 \(\mathcal D=C_c^\infty(\mathbb R;\mathbb C)\)，
以及\(B_W(r,s)=W(r*s^*)\)。非compact Gaussian关系仅在已合法延拓的
\(\mathcal A_{\exp}=e^{u/2}\mathcal S_{\exp}\)中测试，不能塞入\(\mathcal D\)。

| 角色 | 合法对象、map及domain/range | 不可随之宣称的结论 |
|---|---|---|
| 物理Weil source | 旧f先运输为\(r=e^{u/2}f\)；原du与zero-extension Dlog；J把r送入C∞ | image拓扑不自动等于商拓扑；point读出不自动有原norm界 |
| full-Q非退化载体 | \(V_W=\mathcal A/\operatorname{rad}B_W\simeq J_W(\mathcal A)\)，配对可不定 | 非退化不意味positive；此商不提供原ζ的全部Jordan/trace重数 |
| 405的关系／双次数载体 | 旧\(P_{an}=I\cap\operatorname{rad}B\)；\(I/P_{an}\)保双次数双曲平面；\(Q=T\)则消去整个physical I | 不可把旧B根改成I，亦不可把Q商叫作同时承载旧B和双次数的同一个对象 |

新principal-compatible几何map至少要显式回答：用的是旧f、物理r，还是含双次数的扩张？
消去哪个关系空间，在哪里取primitive商？给定
\(p=E\eta_0\in P_{an}\)，旧坐标须杀[p]，物理坐标须杀\([e^{u/2}p]\)；
给定小窗\(r_0=(D^2-1/4)\psi\)，537的\(Q_W(r_0)>0\)确保非根方向必须可见。
568的J已通过这两项，故**重复它们不能报新的几何进展**。
若几何需要双degree，应允许在\(\mathcal S_{\exp}/P_{an}\)保留\(I/P_{an}\)，
由真实principal/det transition协调局部片；只有完整Qprimitive商才杀整个I。

乘法也须给原运算：源卷积不是image的逐点乘法；时间微分不是这个卷积代数的
Leibniz和式。把二维\(e^{\pm at}\)像扩成对称代数虽合法，新增频率/过滤/容量必须重付。
从J的非零minor或复数评价清分母，不能补出LS的模p reduction或Frobenius同余。

## 4. Γ、finite-part、parity和cocycle的精确责任

569的单链核经过唯一共同half-density character后为
\(H_\kappa(u)=1/[2\sinh(|\kappa||u|/2)]\)。UV/IR同时比较排除任何常数倍等于
\(a(u)=e^{-|u|/2}/(1-e^{-2|u|})\)。这已经是执行完的限定失败，不是等待选参数。
真实normal reflection按even-k过滤能给a，但还要实际反射、dual pairing、Euler/trace
系数及global extension；裸g-integer乘法源没有这些设施。

在固定physical log最小对数FP下，完整源为
\[
 A_\Gamma=-\operatorname{FP}a-(\gamma+\log(2\pi))\delta_0,
 \qquad\Gamma_0=\psi(1/4)-\log\pi.
\]
其独立已知锚点是实局部域的指定加法角色、自对偶Haar和sign sector。
odd sector给不同Γ参数，这说明parity有实际局部来源，并不说明conormal源已经具备它。
固定其余全部源后，已知非零关系能检测单独contact改变；这不排一般同时改核的B(s)。

预算片\(q_j\)的
\(c_j(r,h)=2\Re b_j(r,h)+q_j(h)\)在full radical上满足精确cocycle且\(\sum_jc_j=0\)。
全纯transport还带\(e^{i\Im b_j(h,k)}\)，完整tensor的模和phase一起消去。
这些对负型同样成立。以\(e^{-Q}\)为metric再要求曲率半正，等价于要求Q半正；
不是独立极化来源。真正有限评价复形\([S\xrightarrow{E}J]\)的det line虽另有规范意义，
其存在与换基law不支付\(\det E\ne0\)、local order、capacity或signed全源身份。

因此修订路线图应把**规范/协同视为已审可用的相容性设施**，
把真实indicial arithmetic map及独立容量视为未付输入；不再让前者充当后者。

## 5. LS机制教给下一几何准入什么

LS的三件事不能拆给三个不同对象：

- 加法评价格和带权多项式空间，靠特征0次数/重数证明评价满秩，选择同一非零整数minor D；
- 实际Frobenius同余与对局部替换封闭的空间，给同一D的非负高阶valuation；ordinary jets的p因子保留；
- 同一D全部共轭的高度、导数和阶乘费，加product formula支付总预算。

这说明研究对象设计应先问“局部操作是否留在同一filtered source，换行基是否仍保同一D”，
再问logdet如何近似目标，而非先造\(\lvert\det\rvert^2\)正volume。
全部方向的预算身份
\((A_n(r)-L_n(r))/c_n=Q_W(r)+o(1)\)仍未给；
如果A由右边反定义再假设上界有效，正性已藏在前件。
若只得到另一个大正费，也不能说识别出完整Weil二次型。

### 唯一几何候选门：真实O(D)的restriction／乘法究竟能否接收源

这是**保留的章节来源准入候选，当前未晋级、未执行，不是合同队列**。
对象不再叫“未知RR”：沿旧
[Connes/F₁审计§2](../grh-literature-roadmap/connes-f1-facility-audit.md)，
只选择已定位的2602.15941v1 Thms8.5/8.6/8.15中的一个真实O(D)及其tensor乘法，
审它在一个有限place集合及指定arch frame下的实际restriction对象。
本轮未重开该外部原文，故不声称下列map已经存在。

一次准入必须交以下具体台账；任一项只有名字即不晋级：

1. **同一section source。** 写出\(S(D)\)、局部\(J_E(D)\)与restriction
   \(E_{D,E}:S(D)\to J_E(D)\)。若原对象是模/半模，保其原范畴；
   不未经证明改成复vector space或套ordinary dim。
2. **真实kernel和乘法。** kernel须由同一restriction计算；
   能否给\(S(D)S(D')\to S(D+D')\)及对局部vanishing过滤的具体控制？
   若只有周期维数而无过滤单调性，不代入567容量式。
3. **source transport及双测试。** 写明原f或physical r的实际map、relation与degree扩张；
   查\(r_p\)和\(r_0\)，且查map不只是568的J换名。
   若目前根本没有map，只记录“未准入”；不能先假设source-faithful再开RR合同。
4. **最小独立费用。** 至少一个local消失/碰撞lower或一个global filtration容量upper
   能由原对象而非目标Q算出；同时列原Dlog/局部frame运输费。
   获得这个真估计后，才考虑同一nonzero det和full-W预算身份。

**成功的有限净后果**最多是新增实际source→section/kernel或一项独立容量估计，
不自动是全Weil正性；它确实填补当前没有的几何箭头，因而可能改变选路。
**停止条件**：只得到O(D)名称、一次曲线RR、局部自由jets、568重复minor、
569指数budget line，或把Q曲率半正当假设，立即来源止损；不续读2018§3.4、
不扩jet阶、不建立“存在未知det/RR”合同。

当前排序不应由本候选覆盖已保存的actual变分门。按572结算，先做一次
\(P_MS_Tw_R\)的原域/cofinal clipping与完整\(D_{var}\)检验；
该门若只恢复旧clipping加未知平方缺陷，则停止。此时上面的几何候选也须先有新的
原文map/估计证据才启动，不能靠“分析门停了”自动获得准入。

## 6. 验证对象要如何否定过弱或过强条件

| 对象 | 已知可用的真实独立设施／检验值 | 新候选必须尊重的分界 |
|---|---|---|
| 连续\(Z_c=1+c/[s(s-1)]\)，d=c−1/4=±1/16及0 | 两段都具positive P/Π/M、实际非零eval、固定0/1门、有限jet容量、完整cocycle；Q=2\|A\|²+2d\|B\|² | 共通设施不筛符号；独立ODE正能量只在相应正段支付目标。不能强迫literal有限位格；阈值nilpotent商须保trace权，不能要求faithful正Hilbert jet作用 |
| 真\(E/\mathbb F_5\)与290反模型 | 都有正整数closed points、perfect局部jets、raw正Frob、det权和全周期cocycle；primitive Gram det为11/5与−1 | 真曲线另给diagonal函数域、\(\ker ev_E=H^0(D-E)\)、RR和平方交数。自由local target不自动给它们；保全部periodic pole aliases及contact，不能用一个cosh矩替代 |
| 数域／经典ζ | 加法整数格、所有嵌入、ideal valuations与norm/product formula是独立额外结构；Tate Fourier指定完整Γ | 保ideal标签、ramification、residue degree、判别式及全部Γ_R/Γ_C。相同Dedekind ζ未必唯一恢复ring；不排多来源实现或纯分析正性。LS标量class不能直接推广到所有complex profiles |
| 经典完整W与实际Sonin | fullΓ/contact、全部\(\log p/p^{k/2}\)及双pole；560同源正迹比较器，568实际J及norm费用 | 新几何预算要接同一W，不能改成J*J、\(\lvert\det\rvert\)或忽略pole。572的weighted模型receiver费不代actual误差、原源运输或全source capacity |

对函数域，ordinary Wronskian在特征p下可把1和z^p误判；须在实际对象上重付
separable/Hasse jet非退化与order。LS数域证明不能随意除j!，与正特征需要divided-power
工具是不同语境。模型反测的目的在于定位失败前件，不能按“几何”标签剔除负例。

## 7. 修订后的净结论与阅读范围

这组研究把“缺carrier／规范／下降”改成了更精确的“缺真实global乘法、kernel、
独立capacity及signed primitive比较”。这是决策信息与局部设施进步；
没有独立经典Weil正性，没有最强旧542＋555→557 whole leading4/5的改善，
成长core/coupling、actual Sonin运输及通常Ξ仍欠。Γ匹配、det line协同与容量是三条不同箭头。

本稿实际读取：

- 恢复入口README、STATE、check/show、Goal、C035、572结算、D20261020O及工作流程；
  MACRO_FRONTIER读恢复输出中的当前因果位置、资产表和停止/重准入部分。
- 旧路线图全文；568、569主件全文；568/569结算及两份root-consumption-scope全文。
- LS专题全文、LS root消费收据、elementary-proof-audit及facility-transfer-audit全文。
- 568 classic原稿§§1–3及§§5–8；function-field-evaluation-budget全文。
- 569 budget-cocycle-and-determinant-line及continuous-function-field-tests全文。
- 旧Connes/F₁来源审计§§1–3；旧repository/source-bridge审计仅rg定位的role/393/405/406/560条目。

未做：本轮未重开任何外部PDF/网页、未核新文献版本、未重审全部原证明，
未重跑有限算术/符号证书，未读568 continuous独立原稿或569 dual-conormal独立原稿全文，
未直接重读405/552/563/567数学主件，未审570–572技术原证明。
这些依赖只按上述最终主件/消费记录及恢复前沿使用；不得将继承范围写成本轮外部新核查。

本稿没有新数学定理、合同、cadence结算或长期Goal完成主张。root须与其他独占审计的
实际对象/量词/费用对齐后，才能消费为修订路线图。
