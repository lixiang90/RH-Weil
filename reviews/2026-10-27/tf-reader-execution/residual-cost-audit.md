# 固定q0执行：独立残差／成本审计

2026-10-27；`/root/q0_residual_audit`独占稿。已恢复README／STATE、check→show、G20261027及execution-handoff，核实际原件。只审固定h0=1_[1,2]、原F8、q0与原physical Hilbert范数；不改STATE／cadence／库、不新C047、不换source／F／L。本文的成本计算和原语复放不是q0验收。

## 1. 新组织仍是同一q0，未更换对象

实位Sonin M满足FM=M，所以FP=PF；FBF=B*。有限dilation相互交换，W=B*B满足FWF=BB*=W，故M上的G=PWP及其逆与F交换。记R=PG^−1P，则

\[
 F\Pi_FF=FB R B^*F=B^*R B,
 \quad q_0=\langle PBh_0,G^{-1}PBh_0\rangle.
\]

旧v=PB*Fh0与新v'=PBh0有v'=Fv；整个H上的mathcalA=PWP+(I−P)亦与F交换。因此相应trial和residual同作F变换时，J与真实Hilbert residual norm都不变。这个组织可避开先把Fh0离散为全空间step的成本，但不能删掉P内的真实Fourier作用／尾。

逐divisor项确为

\[
 Bh_0=\sum_{d\mid9699690}\frac{\mu(d)}d1_{[d,2d]}.
\]

我独立以exact Fraction sweep计算：256项、384个breakpoints、382个非零区段，且

\[
 \|Bh_0\|^2=\frac{19189712}{4849845}<4.
\]

所以||v'||≤2是同一固定输入的真正上界，优于全B的M_+≈13.637；不是新物理源或从浮点norm倒推。producer脚本也以全pair-overlap和endpoint-sweep两种exact算法复核此比值。

## 2. 原F8的有理区间与残差预算

独立用70位十进制尺度D、isqrt夹住各sqrt p，再以正有理数运算求积。以下为向外舍入的**认证包围**，非仅display digits：

| 量 | 下端 | 上端 |
|---|---|---|
| m | 0.012540998348664081461577 | 0.012540998348664081461578 |
| M_+ | 13.637193599936120830655501 | 13.637193599936120830655502 |
| d=m² | 0.000157276639581195218129 | 0.000157276639581195218130 |
| u=M_+² | 185.973049282138694801287859 | 185.973049282138694801287860 |
| rho=(u−d)/(u+d) | 0.999998308609691778512030 | 0.999998308609691778512031 |

可取安全真实残差norm目标η=0.002216956243797416622018，满足η²/d≤1/32。若采用正Neumann-prefix trial，||z||≤V/d，使用上述V=2时可取Z≤12716.446672091347。J误差为2Z ε_v+Z ε_Az加scalar inner-product arithmetic。为不把节点误差预算用尽，可取

\[
 \varepsilon_v\le(1024Z)^{-1},\quad
 \varepsilon_{Az}\le(512Z)^{-1},
\]

使action费≤1/256，另留arithmetic费1/256，总J半宽≤1/128。取保守全operator扰动||mathcalA(P)−mathcalA(P_N)||≤[1+3u]e_P（e_P≤1），得到一组足够预算display：ε_v约7.68×10^−8、ε_Az约1.54×10^−7、e_P约2.16×10^−14。它们是此种全局估计的充分精度，不是任意实现必须达到的最低精度。

Z≤V/d不能套于任意trial。若仅用Chebyshev residual polynomial的粗界，||z||≤3V/d；这会把上述e_P预算约再除9。实际实现应直接认证自己的||z||，无需强套worst case。

## 3. 低区间resolvent：Taylor截断不代有限逆算术（实际付款见§6）

用既有arch-gap JSON的真实kappa_bar与M0=10^6，独立逐N核

\[
 \eta_P(N)=M_0M_N\delta_N(\bar\kappa+\kappa_N),
 \quad\delta_N=2(2\pi_{hi})^{2N+2}/(2N+2)!.
\]

| N | η_P保守上界display | 对上述Neumann-trial J预算 |
|---|---|---|
| 20 | 4.753×10^−6 | 不足 |
| 24 | 5.333×10^−13 | 不足 |
| 25 | 7.939×10^−15 | 足够 |
| 26 | 1.096×10^−16 | 足够，亦过3V/d的粗Chebyshev预算 |
| 27 | 1.404×10^−18 | 足够 |

这里display向上略化，仅用于规模说明；实际通过比较使用有理δ_N及原gap witness。旧R0 Neumann以d0>10^−6和此预算，简单二进block证书可要约66,000,000次C0²作用；这只说明该保底组织昂贵，Taylor有限rank修补可避免此项，不是实际q0的必要成本下界。

**有限逆算术仍须另付。** N25/26的解析Taylor remainder小，不代表double-precision monomial CauchyGram的逆也同精度。该坐标矩阵病态；必须认证finite inverse／moments／conditioning和rounding，或仅把浮点解作确切rational trial、以独立true-H residual验收。不能只据N25的η_P栏就宣布P代码通过。

## 4. 全G保底次数：优先直接残差，不绕inverse-error乘u

对精确mathcalA，正Neumann-prefix z_n=c^−1Σ_(k=0)^(n−1)(I−mathcalA/c)^k v满足**直接**residual r_n=(I−mathcalA/c)^n v，因此||r_n||²≤||v||²rho^(2n)。经inverse operator误差再乘u的估计更弱，不应冒充必须成本。

对Chebyshev residual polynomial，q=(sqrt(u/d)−1)/(sqrt(u/d)+1)=(M_+−m)/(M_++m)，有||r_n||²≤4||v||²q^(2n)。只在精确operator reference上成立；inexact action／recurrence roundoff另付。

producer脚本以64位向外fixed-point exponentiation／binary search，对精确的输入norm²=19189712/4849845核同一直接残差充分包络≤d_low/128，已实际得到：**Neumann degree4,429,773，Chebyshev degree4451**。我独立in-memory执行build_record(64)，完整JSON数学字段一致；另核前一个index的power下端乘factor已严格大于target（两者比值约1.0000025584／1.0020670844），本index的上端比值约0.9999991756／0.9983877820。因此不是只依赖binary search的布尔单调假设。这里“第一个”仅指本充分包络的首个passing index；不是所有trial／实现的必要次数。

独立粗二进block计算（a^ceil(1/(1−a))≤1/2）给V=2、residual≤η/2时，一组可复核但非最优的充分次数：全G Neumann18,328,130、Chebyshev6540。它们只作独立安全对照；实际规模优先上段更紧的已认证充分值。这些次数尚未实际执行G迭代。

producer初稿输出rho_interval只包围rho_high本身，未必包实际rho；已报告并修为实际rho_low／rho_high。其power search原本即使用完整包围，degree证书不受此metadata修正影响。primitive P-action counts须保exact-reference-on-M限定：近似P_N不是真projection，不能免费假设每个inexact向量仍在M；若采用whole-H mathcalA组织，P次数和泄漏误差必须相应调整。

## 5. 已实际执行的Fh0原语：独立复放通过，尚非q0

已全文核 `scripts/tf_reader_step_certificate.py` 及step-engine-record。Fh0的精确式为[sin(4πx)−sin(2πx)]/(πx)。x<1导数≤6π<19；x≥a≥1导数≤6/x+2/(πx²)<7/a。dyadic midpoint step的L² mesh²界D²a³/(12n²)、near0／far∞尾、sin29阶Taylor与向外整数区间算术均正确。内域两误差以Young因子17/16和17合并，未把同域误差平方直接相加。

我独立in-memory重放实际97653个cells，以下exact fields与producer记录一致：coefficient stream SHA `9ae2e9aedf9b5179b073e30d5d35958ed89f5c7ca16a2b97a013f1f8a07803fb`、step norm²、有理L²误差平方与coefficient-error平方。显示值为

\[
 \|Fh_0-f_{step}\|\le0.021576244615<1/32,
 \quad\|f_{step}\|^2\approx0.999875943816.
\]

认证来自有理比较，不是小数打印精度。此处只执行了Fh0原语；脚本以stream hash／summary和可重放算法定义step coefficients，尚未将它接入P/G/trial／真实残差。它不能被报告为q0已计算或1/16验收通过。新q0等式可避开初始Fh0的全step展开，但不抹掉这次已执行原语的证据，也不说明任意后续F作用可无费用。

## 6. 新低频scalar原件：有限逆已付款，但仍未通过q0

已全文核 `scripts/tf_reader_lowband_step.py`，并独立完整重放make_record(260,26)：68,037个T频率、384个边端系数、53维shifted-Legendre trial；除elapsed_seconds外，全部JSON字段exact match。script相对原运行的后续修改只删无效dead branch；重放覆盖当前实际版本。

其解析对象是f=Bh0、g=L Ff、C0=L F L，R0=(I−C0²)^−1。由于Lf=0，真实投影能量为

\[
 \|Pf\|^2=\|1_{(1,\infty)}Ff\|^2
            -\langle C_0g,R_0C_0g\rangle.
\]

tail使用T(n)=2πn(π/2−Si(2πn))，整数n的积分恒等式∫_1^∞cos(2πnx)x^−2dx=1−T(n)，n=0时T(0)=0；因此sin×sin grouping的符号和1/(2N_F²π²)正确。g的monomial moments包含sum tau=0的常数消去，sin积分递推与code一致。T的大频率余项由

\[
 T(n)=\int_0^\infty\frac{e^{-s}}{1+(s/(2\pi n))^2}\,ds
\]

的有限几何恒等式给符号交替、大小≤下一factorial项的严格余项；小频率用Si Taylor及|Si′|≤1的π端点运输。额外300位mpmath对n=1,2,39,40,100,9699690的独立值均在有理区间内；这只是sanity check，认证仍来自上述有理余项。

shifted Legendre矩阵的l行带2l+1，实际H norm²为Σ|x_l|²/(2l+1)；producer没有用坐标Euclidean残差偷换。150位mpmath只选130位有理trial；验收重新以260位向外区间计算真实polynomial-H residual，所得平方上界约5.660×10^−205，scalar quadratic余费约4.748×10^−98。该residual只针对R_N低区间trial，**不是full G residual**。

全operator替换使用η_R≥||R0−R_N||。关键是C_jR_jC_j=R_j−I，所以

\[
 \langle C_0g,R_0C_0g\rangle
 -\langle C_Ng,R_NC_Ng\rangle
 =\langle g,(R_0-R_N)g\rangle.
\]

因此代码中的η_R||f||²运输已包含C0g→C_Ng forcing替换，无需再漏补一个forcing费。实际η_R上界约5.476×10^−17、quadratic运输上界约2.167×10^−16。此处有限逆算术和全Hilbert截断误差确实都付了，不能再笼统列为“有限逆仍未知”。

display-only结果：tail能量≈0.20647567977209647，R_N correction≈0.05593987727662816，最后

\[
 \|PBh_0\|^2\in
 [0.15053580249546810,\;0.15053580249546854],
\]

这里短十进制端点向外略化，实际JSON有理区间宽约4.333×10^−16。由d/u得到q0粗谱区间约[0.0008094495577533444,1]，宽约0.99919；**宽≤1/16失败**。没有非零full-G trial、全G的J区间或真实residual。低频norm窄界不能当成q0点值或其验收。

## 7. 当前可消费／未付范围与执行止门

允许消费：同对象FΠF恒等式、BH输入exact范数、Fh0原语的实际全H误差和有限成本、真实residual／J所需数值阈值、保底次数组织和Taylor改进空间。zero trial z=0给J=0及q0∈[0,1]是有效但不通过的证书，不能据其产生一个“q0≈0”的点值。

新增允许消费：同一固定输入||PBh0||²的认证窄界、R_N的实际有理trial／真H residual及全R0运输。scalar程序自身没有输出可复用PBh0物理向量；随后经root指定的vector提取已补成显式analytic向量，见§9的实际版本修正，仍未实现full-G action enclosure。

尚未支付：非零full-G trial的实际构造、P/full inverse对它的全H action enclosure、J实际区间、full-G true residualnorm和最终q0宽≤1/16；原五源T/E/cross表及Hfin均更未运行。不能把已支付的R_N residual再次列为全然未知，也不能把它升级为这些未支付项目。

本次full-G执行应**止于这些实际partial结果和明确未付项**。在初次scalar checkpoint，新lowband输入只给scalar谱质量，无actual-G比较可改变full-G实现选择；不能由此自动续partial-reader／global-cost优化循环。§9随后实际补付analytic-vector输入，足以准入一次预先固定的unitary-pair设施测试，不能升级为full-G比较已经准入或完成。source-adapted trial／Krylov可能比保底包络快，仍是合法未测选项；任何未来full-G比较须先指定同一h0/F8下能实际输出全H residual/J的试验及止门，不能只再降低一个参考次数。

成本停止只能是这份具体实现／充分certificate的执行止门，不是所有source-adapted trial、另一合法representation或真实signed费用的不可能定理；不能因此完成或block长期Goal。原范数、固定source/F/L、完整Γ/powers/poles与strongest-old whole4/5UPPER保持。此审计不另设计轮器，root负责共同消费和同步。

## 8. 本次审查的实际版本

以下为LF正规化SHA256，便于root关闭同一原件；hash不是数学证明：

| 原件 | SHA256 |
|---|---|
| tf_reader_step_certificate.py | 1ee87e7351cea59774f5c33f63262faf79a5174ed244bb5e7cc30e020680e2cd |
| tf_reader_q0_cost_certificate.py | 479b8c29a9aecff1cee26f3a226f61cb4d946dc0cda2c88672b5b7dfeccb35a3 |
| tf_reader_lowband_step.py | d3c5689eec3614127c870d88383b2b7c0669ce3ee4702d2e7a540ed734a537f5 |
| step-engine-record.json | 0fb69e25a1df7a8783482753adc1c9ca37192c0164d432f084859270ae04f5a9 |
| variational-cost-certificate.json | 54107bf48566b22f2ae8587e9dceb02f40bdd6aec25547f9e9fd42c7df4cc0b3 |
| lowband-step-certificate.json | cd1b078ed4a495764e7a728c23681f9f177c03e3ab24e836c377a6e55daa3ac1 |
| tf_reader_lowband_vector.py | 97157a0f8106a63036333953f1754a26b8665f778c33b3c667aff8d7e1dbb9f5 |
| lowband-vector-input.json | 24f308d253860c35713649559eb06499431a64b6347199b1fe7ecad405a0f612 |

## 9. 后续analytic-vector提取：新的显式输入限定PASS

root在上述scalar checkpoint之后明确指定只提取已有trial，不重跑scalar／不运行G。已全文核 `scripts/tf_reader_lowband_vector.py` 和 `lowband-vector-input.json`，独立执行build_record，全部JSON字段exact match；源scalar/gap的LF hash与§8及既有gap原件一致。该修改补充了旧“只有scalar”的缺项，不能沿用该历史描述否认当前已产向量。

令t为旧53个Legendre trial区间的确切有理midpoint。当前原件所有区间均为singleton，因此t就是原已认证trial；即使保区间表达，旧outward residual也覆盖所选midpoint。脚本重新求27个exact moments，并为C_Nt的even-monomial系数求向外区间，其midpoint定义27个**确切有理**系数p*。我另以

\[
 L_l(y)=\sum_{k=0}^l(-1)^{l-k}\binom lk\binom{l+k}k y^k
\]

的独立binomial展开核全部27个trial moments，以及53项p*→Legendre转换，均exact相等；没有只依赖producer的factorial闭式。系数半径之和δ_poly给全L²(0,1)误差上界，因为每个y^(2j)在此区间的norm≤1。

定义

\[
 \ell_{app}=1_{(0,1)}(g+p_*),\qquad
 v_{app}=f-1_{(1,\infty)}F\ell_{app}.
\]

这是可复用analytic向量：g由384项带共同整数分母的sin/y公式精确定义（y=0可去奇点），p*由保存的有理系数定义；外部F保为确切cosine transform，**未截断无限物理尾**。它不是finite-step向量，也未支付对该transform的未来数值评价／积分成本。

若e=C_Ng−(I−C_N²)t，则R_Ng=g+C_NR_N(C_Ng)，故

\[
 \|R_0g-\ell_{app}\|
 \le \eta_R\|g\|+\kappa_N M_N\|e\|+\delta_{poly}.
\]

实际脚本故意用κ_N≤1、M_N≤10^6放宽第二项；均已由当前有理gap/Taylor界重新核，不是隐去κ_N。所保存ledger的向外上界display为：resolvent-input约1.06030×10^−16、trial-solve约7.5230×10^−97、系数rounding约2.6350×10^−140，总δ_v=δ_ell<1.061×10^−16<2×10^−16。full-H误差运输由||1_(1,∞)F||≤1给出；不借finite-section residual或tail省略。所有小数只作摘要，接受来自JSON有理比较。

因此这次确有新input：同一v=PBh0的显式analytic表达及真H误差，而非再次打印norm或抽象存在。对任意实际定义的有界A，可运输||A(v−vapp)||≤||A||δ_v；对固定unitary U，有

\[
 |\langle v,Uv\rangle-\langle v_{app},Uv_{app}\rangle|
 \le\delta_v(2\|v\|+\delta_v)<8.250\times10^{-17},
\]

其中||v||<0.389由已付norm窄界精确比较。它可支撑root随后预冻结的一次c2=<v,U_log2 v> finite-pair计算／尾误差测试：结果仅改变此analytic representation的pair可执行性判断，实际积分／系数／尾仍须支付。若该测试失败就止，不自动扩G／Krylov；在原件和验收门出现前不宣称测试已经运行。

该vector不提供Gv、full-G的非零trial/J/residual或q0宽1/16，不提供五源T/E/Hfin，也不移除长期数学瓶颈。§7的full-G止门与Goal open保持；仅“没有显式Pv向量”这一具体缺项现已实际修正。

## 10. root结算／前件记录和固定pair下一门：实际版本限定fresh PASS

已全文独立核当前root主稿、`next-fixed-pair-test.md`、`root-consumption-scope.json` draft。root记录的14个LF hash全部与现场文件一致；本次核到的主稿LF SHA为`af3c17b7bc4cb13b974254cb1c71481f5aa90a09249d0214221b293033e377c6`，next门为`c3d9fe243e5d663801ba12739c78c282cacdc5b3b43d53ca6026ea1a6a8329b9`。root收据draft（status=root-scope-drafted-awaiting-final-fresh）的LF SHA为`9533e57908ccb731d7db64ce5b994086aae7c612a9dd69b1088b484d680e9eda`；其后只填root-consumed/fresh审核状态与审核hash不改变本数学消费范围。

finite-pair恒等式重新推导如下。冻结U=U_log2、U h(x)=2^−1/2h(x/2)、a=Fell*、Hcut=1_(1,∞)，于是UHcut=1_(2,∞)U。展开v*=f−Hcut a的四项后，两个cross分别经U*和F*=F运输为

\[
 \langle\ell_*,F Hcut U^{-1}f\rangle,\qquad
 \langle\ell_*,F Hcut U f\rangle.
\]

最后一项因UHcut a支撑在(2,∞)，有

\[
 \langle Hcut a,UHcut a\rangle
 =\langle a,Ua\rangle-\int_0^2a(x)2^{-1/2}a(x/2)\,dx
 =\langle\ell_*,U^{-1}\ell_*\rangle
   -\int_0^2a(x)2^{-1/2}a(x/2)\,dx.
\]

因此root下一门的全部正负号、U方向和截断端点2正确。实输入限定明示；第四项支撑(0,1/2)，两个cross只读ell*的低支撑，clipped dilated f仍是确切有限steps。这里是真正的Plancherel/cutoff运输，没有丢掉原物理无限尾。

一次固定c2总有理enclosure宽≤1/1024的验收门明确包含δ_v输入运输及finite-domain算术／quadrature余项；不能只用约8.3×10^−17的输入费就预填pass。root已保conditioning、大频率消去、large polynomial coefficients、真实Fell*评价及有限积分余项的责任。目前**没有c2结果，也没有G/c2后台进程**由本次审稿启动；本文只审其准入和恒等式。

限定结论为**PASS**：实际新vector输入→恰一次可证伪的mixed pair设施测试，能改变当前解析表示是否可执行的判断；fixed c2通过不代actual G、whole q0或五源T/E。失败保存准确缺项后停表示的自动扩展，通过仍须新的whole-G input/test/net比较，不自动续prime／Krylov／paper。当前q0宽1/16失败、0数学轮、cadence1／历史47／cycle16及whole4/5UPPER／关键瓶颈未变的结算相容。

root收据保physical域／norm、原F8/h0和dilation方向、real当前系数／原五源linear-first complex约定、源成长量词／付费依赖、coverage-coupling、strongest-old和净后果／停止；未发现系数方向或全量词遗漏。该PASS不认证尚未运行的finitepair算术、full-G J/residual、Hfin、RH或长期Goal完成门，也不以任何充分成本构造方法类不可能性。
