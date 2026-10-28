# Inclusion-cone精确边界：独立全链逆核

2026-10-28；`/root/euler_scope_fresh` 当前新任务独占稿。已恢复README/STATE、check→show、Goal、耗尽C049、D20261028AA、宏观前沿/summary及唯一next，核实际工作树。全文读取actual-boundary-test、独立右因子化稿、root与下一因果门；post-test-choice-consult本次已实际出稿，另按事实/范围读取，不代root作选择。只逆核当前pair/norm/source，不web、新source、数值、第二candidate或STATE/Git/cadence变更。

**限定PASS。** 原eη的实际边界和3sqrtη/2误差正确；同一闭C*理想的左右两种因子化均给有限tensor的精确原始元，故源类在unreduced与reduced同调都零。更强结论不依赖读出连续性，但不推出bounded linear contraction、全cone同调零或全部relative方法失败。按573已付理想归属＋标准因子化＋普通边界展开的直接旧应用0结算合理，不预C050/587或Goal完成。

## 1. 原链域、Hochschild符号和finite tensor资格

固定unital Abar=C*(A_src)、闭双侧C*理想Jbar=closure(D_src)，用原算子范数的完成projective链C_n(E)。S_n=C_n(Abar)⊕C_(n−1)(Jbar)取sum norm，D=(bx+i y,−by)。旧573已在其指定扩大域支付ALL L1 raw F_r∈Jbar、||F_r||≤2||r||1；不是声称较小原代数的代数ideal等于这个闭ideal。

对a∈Abar、B∈Jbar，z(a,B)=(a⊗B,−[a,B])闭。给e,c∈Jbar，

 P=−a⊗e⊗c，Q=ae⊗c+ca⊗e。

Q的四个槽均在Jbar，由双侧理想性支付；P在C2(Abar)，都是实际finite tensors。b2的最后项为正号zx⊗y，故

 b2P=−ae⊗c+a⊗ec−ca⊗e，
 b1Q=aec−cae+cae−eca=[a,ec]。

于是D2(P,Q)=z(a,ec)，且||(P,Q)||≤3||a||||e||||c||。无需把completed-projective的i_n假设成单射/等距；包含诱导的有界chain map及这些finite tensor等式已足。没有用excision或“商里B=0”替代实际边界。

## 2. 原eη test确付reduced结论和误差

T=BB*≥0，eη=T(T+η1)^(−1)在Jbar且||eη||≤1。原finite tensor式给D2(P(eη,B),Q(eη,B))=z(a,eηB)，primitive费用≤3||a||||B||。

|(1−eη)B|的C*范数平方为sup_(t∈spec T) η²t/(t+η)²，标量函数最大不超过η/4。因此

 ||z(a,B)−D2(P(eη,B),Q(eη,B))||≤(3/2)||a||sqrtη。

原source a=u*范数1，正是3sqrtη/2；误差在冻结的projective sum norm中，不是弱算子收敛或辅助norm。它实际给reduced类零，但“primitive序列有界”本身不使其收敛，也不证明imD2闭。两原稿与root均没有作这个跳步。

## 3. 左右因子化分别闭合exact，不假polar元属于代数

**左T^(1/4)构造。** E=T^(1/4)∈Jbar，Cη=(T+η1)^(−1/4)B∈Jbar。标量gη(t)=sqrt(t)/(t+η)^(1/4)一致趋t^(1/4)，误差≤η^(1/4)。C*范数计算给||Cη−Cδ||≤η^(1/4)+δ^(1/4)，所以原算子norm-Cauchy；Jbar闭使其极限C仍属Jbar。||B−ECη||由sup sqrt(t)[1−(t/(t+η))^(1/4)]控制，≤sqrtη，故EC=B。另由CηCη*=T/(T+η)^(1/2)及范数极限，||C||=||E||=sqrt(||B||)。B=0单独取0因子。

**独立右|B|构造。** 令t=|B|=(B*B)^(1/2)、D=t^(1/2)∈Jbar，Cε=B(t+ε1)^(−1/2)∈Jbar。fε(λ)=λ/sqrt(λ+ε)与sqrtλ的误差≤sqrtε，给Cε为norm-Cauchy并收敛到C∈Jbar。Cε*Cε=t²/(t+ε)→t，故||C||=||D||=sqrt(||B||)。sup λ[1−sqrt(λ/(λ+ε))]≤ε给CεD→B，于是CD=B。

两构造各自正确，不要求左构造的C等于右构造的同名C，也不混用它们的E/D。所用逆幂都先有η/ε>0；未把无界T^(−1/4)、t^(−1/2)或polar partialisometry写成Abar/Jbar中的元素。闭性只用于得到同一Jbar中的实际因子，之后就是同一finite tensor恒等式的**精确**输入。

因而有实际w(a,B)∈S2满足D2w=z(a,B)，||w||≤3||a||||B||。这证明z在imD2，不仅在closure(imD2)；unreduced零来自这份精确原始元，绝不是reduced/closure结论的改名。

## 4. 最强可消费范围与原physical费用

一般结论覆盖任意bounded a∈Abar、B∈Jbar的同型z(a,B)，所以只按源适应/非局部/任意joint参数选择这些a、B并不救同型source类。范围不是任意a∈B(H)或任意相对cycle；理想性和所给chain域必须保留。

原a=u*、B_r=uF_r对全部complex r∈L1合法，||B_r||≤2||r||1，故exact原始元费≤6||r||1。它涵盖全S_exp/真实noncompact Pan及平移、Cc∞和537非根，不是只消关系却保另一个未核子域。Fixed I_L时为6sqrt(2L)du、6sqrt(2L/log2) zero-extension Dlog费；不删除L依赖或外推global L2/Hlog。这里是raw链费用，不是任意L1源上完整Γ/pole型域的延拓。

因子化可非线性依赖B。逐source存在有限费primitive不提供有界**线性**右逆/chain contraction，更不证明整个S复形acyclic。Factor也只属于闭C*对象，未给较小A_src/D_src、trace-norm或强完成化的归属/费用，不能免费搬回那些域。

若读出真正定义在这个unreduced H1上并对boundary不变，exact源类为0就使线性读出为0，无需连续性；sesquilinear mixed型若每腿只经这些classes也为0。仅有raw链连续性而不消边界的函数不在此结论内，反过来“不连续/无界”也不能救同一全链域上的exact零类。

537对du归一的非零r0∈Cc∞(−17/16,17/16)已给完整Qζ(r0)≥2^(−49162)>0。因此**纯H1-class-factor总模型**不可能承担该目标。这个判断不把零中间correction冒作含其它腿的总型；Γ/FP/contact、全部pp和双pole由旧537完整目标承担，没有删项或从source边界制造Weil负源。

旧573另一quotient-fiber cone的−4 HH1电荷、411轴迹及432原电荷没有被回滚；pair、链域和source代表不同。Exact零不等于Hodge primitive已构造或所有higher/C*方法无效，也没有给新的signed消失、core/cross或whole净预算。

## 5. 旧应用分类、运行Goal与下一动作

当前最短链确是573已付的闭理想/raw归属与原费→同一C*理想标准函数演算精确因子化→通用Hochschild finite边界展开。两原稿显式付了所有域、符号、误差及常数，未只凭定理名称。原573没有逐字写本次原始元，因此不能称该原稿早已逐式陈述新cone结论；但该source存活的净后果已由其结构和一般恒等式直接决定，未引入新的独立算术/几何输入或关键Weil前提削弱。按直接强旧应用0停门合理，不是仅因计算初等、结果局部或没证RH而定0，也不把exact/unreduced标签作为新轮或核心类完成门。

副代理get_goal返回null不构成root原1793085111 Goal终态的证据；本审稿不据子代理句柄改变或否定root同实例active观察，也不创建/完成/暂停Goal。实际root运行实例仍由其当前工具核验负责。

post-test-choice-consult已出5892b，内容只盘点事实/资格；其中“没有合格下步”限所核原件，不是一般方法不存在。本审稿没有代root采纳该后继选择或新造candidate。next-post-cone-causal-review只保留**一次尚未执行的因果选择**，明确非formal18、不改cadence，不续本pair/norm/source、不改trace-norm/metric/regulator、不编paper或再发泛形成计划。来源需准确未耗尽locator和later scope核对；未知secondary/filling/RR或domination名称不算input。

本结果立即停止当前source-survival门；任何另一个实际pair/强域必须自给原式、费用和完整coupling，不顺延预算。Whole4/5仅负惯性UPPER、primitive/mixed及完整signed/core/Ξ瓶颈保持，Goal完成门open。单cadence0/history50/latest586/formal17不增不归零，未准C050/587。

## 6. 版本绑定

规范LF SHA-256；只认证所核版本，不由hash认证未来因果选择或发布状态。

| 原件 | raw bytes | LF SHA-256 |
|---|---:|---|
| actual-boundary-test.md | 7328 | e4b36b196a76d290fb00cb99ab2b87289b40ee6286700b511e8d2585924bf65c |
| strongest-old-factorization-audit.md | 8368 | 8e2fbd01b4d8743ea48ba79de0c3e9e3a6e229a9daff887327116b95980c7c2d |
| root-exact-survival-review.md（审中版） | 4565 | 6d3aaaabfcad3376fdb374e0a5c529647e4919ca757786edd3f861ea02085bfd |
| next-post-cone-causal-review.md（未执行） | 2914 | d149f58aba770503aded01c6d203d4cbcad6a99e3560a656ce69d663697a5c12 |
| post-test-choice-consult.md（事实/资格咨询） | 5892 | 74c8aebba051c47ed373a06485cdc25a27c422960a46804d4c20f27af76cda66 |

原准入next为3804b/LF `955c019afa19bbe3ccd903bec6d74245bfaf28d4b752911f6fcfcc071b5086d1`。573 LF `da5ed121715fa71ce3e83c61aef7160825778ce0beeca8df39d4ae55fbb4cd93`，仅消费指定扩大域及闭ideal/raw费用与旧relative类范围；没有重审全部历史proof。
