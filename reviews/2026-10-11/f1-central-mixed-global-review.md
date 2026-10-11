# 515–517 提交前内部独立全文审查

2026-10-11。审查者：研究线程独立子代理 prime_transfer_chain。
已完整阅读当前515、516、517及诊断脚本；逐项数学核算如下。
结论：通过；早期索引澄清已采纳，当前无必须修正的数学问题。
这是内部独立审查，不是外部同行认证、Lean验证或RH证明。

审查冻结的LF-SHA256：
- 515-f1-common-central-mixed-kernels.md：
  dc7318475e1f2e5a1f019312339622d2e980ef8a2e5b68bb4d51e4287a64d27f
- 516-f1-global-mixed-radical-and-mellin-jets.md：
  d21496da1ee280a0f733f322baddf46eb4cac4b50242494ae76b0d464533bbbd
- 517-f1-weak-observable-limit-and-source-cutoffs.md：
  7aecd286712b16628eccea614ca5d3eab8d8772ae1e4cd255426ae398889d4f1

## 1. 515：单素数及有限来源共同检测核——通过

实际单位修正闭链、中央首因子链映射及改测试的b₂比较均沿用513–514已支付准入。
μℓ的有限质量为2La/(1−a)，实偶卷积换序与Fourier系数全部正确。
rℓ零集恰为所列离散集，因此连续ηhat在稠密补集消失就处处消失；
单素数共同核零不需要小支集条件。

ζ=χFℓ,η是合法实偶紧支源，读出为正平方积分；
这不需要η本身非负。有限非空F的rF(0)>0，
与紧支ηhat整性给μF*η的injectivity，
故有限新增类和的非零性来自合法混合同调检测。

有限S密度aS含完整Γ常数与Euler项，aS(0)>0。
aSηhat∈L¹及Fourier唯一性给固定S共同核零。
证明不误用整个aS非负，不消去单位项，
只分离指定紧支链家族，不宣称整个HH₁的共同核零。

## 2. 516：完整标量radical、source jets与条件性差别——通过

当前§2明确η_fg=e^(t/2)k_fg，并用t_(S,η_fg)与ΠAη_fg，
消除了sharp原h与normalized even η的索引混淆。
卷积极化公式及偶近似单位给K_mix=rad(B)正确；
compact在S_exp稠密及B联合连续来自405。

平移式(6)、Laplace式(7)的指数和两次数极符号正确。
系数在零点带快速衰减，带重数零点计数足以支付正常收敛；
端点极±1/2与零点极不同。
κ可对每个ρ另取足够窄正支集，保证Mκ(1−ρ)非零，
因此留数确给全部零点值消失，不要求先知道RH。
sharp直接读出K_h的偶性、原Gamma/constant归一化以及同一留数结论也正确。

rad(B)=R_val是完整标量结论，不被称为全局HH核或几何principal。
405实际非零p的Mellin常数、双矩与全部零点值准确，I∩R_val=P_an通过。

compact核零明确使用Conrey1989的正比例simple/distinct零点输入，
再与Jensen给出的compact Mellin O(T)零数矛盾；
没有仅用含重数N(T)跳过distinct条件。
这是既有外部定理依赖，不由有限诊断重新证明。

source θ偶且θ(0)=0使Mellin因子在Re s>−2全纯，
故真实像保留每个ζ重数要求的全部jets；
导数求值连续把它延到闭像I。
仅值radical不能凭重数系数自动取得这些jets。

§8的条件性重零点构造通过：
轨道Q为实系数、s↔1−s不变；
(D+λ)的两端primitive及除法符号λ−s准确，
其S_exp半范数界与导数递推合法。
逐个不同轨道点只除一次，保留零阶消失但减少恰一阶jet，
Mellin唯一性给实sharp，从而条件性严格包含成立。
稿件没有断言ζ实际有重零点，也没有声称简单时自动取得像闭包等号。

## 3. 517：有限来源direct system及弱读出极限——通过

A_S↑明确由全部T⊆S实际径向角运输像共同生成，
不把任意全空间压缩称为同态。
自然单位壳层源映射与径向满酉J₀的复合相容，
给有限角代数及按共同S₁理想的商单射；
普通迹、S₁范数及真实卷积运输相容。

中央性覆盖每个运输后的旧角字、当前Fourier/反演/Π、
全部卷积及S₁生成元，因此也覆盖新共同有限角的全部有限字。
当前(3)明确F非空有限且F∩S_f=∅；
513的b₂与515的有限增量injectivity给真正非零差，
并由后续仍合法的中心检测保证它不被以后有限扩大自动杀掉。
这不是仅从代数单射推HH单射；证明实际用了非零混合读出。

F_Sη=Gη+Σμp*η保留完整Γ/constant。
固定compact K只有nlogp≤Rη+RK相关，故全部导数在K上最终准确一致。
这给C∞loc最终精确稳定；有界Cc∞测试集合具有统一compact支集，
因此强D′读出收敛也合法。
μp并非全素数有限测度，范数尾不被这项分布结果修复。

原算术值2N(h*kζ)由先覆盖合成支集再比较获得。
移动支集检测器不在固定有界测试族内，
故非coherent HH类与局部精确稳定不矛盾。
本文不构造无限链t∞、faithful ζ Hilbert谱或全局Hodge正性。

## 4. 517：非compact尾与保双矩源截断——通过

非compacth仅用405标量连续延拓，未自动放进原compact生成代数。
(8)的prime-power整数无重复、权重logp≤log(p^n)及p₂,₀界
给O((1+logP)/P)尾准确。
统一compact/半范数有界ζ族由卷积界给统一标量收敛，
这不成为S₁边界范数收敛。

当前稿明确D(fsharp)=(-Df−f)sharp，
因此D²+D与sharp交换，偶χ_R保持sharp。
p_R=(D²+D)(χ_Rh₀)实sharp、compact、准确双次数零；
紧支ODE核为零给p_R非零。
误差展开及所有支集在|t|≥R给S_exp半范数e^(−R)界，
再由B、N连续给固定有界测试族统一观测误差。

§6已明确normalizedη_R=e^(t/2)p_R用于实际固定S链。
覆盖S_R需随R及组合支集增长，稿件没有固定S后颠倒极限。
p_R未被称为source像或principal，
观测趋零也未被称为HH边界/链范数趋零。

## 5. 诊断脚本的有限用途

全文核读scripts/central_mixed_kernel_diagnostics.py。
SymPy模型轨道与jets为假设重零点的有限多项式运算，
不声称展示ζ实际重零点。
数值部分核有限素数权重、Γ(1/4)常数、局部支集稳定、
一般支集混合检测以及显式Gaussian ODE的Mellin除法符号。
这些都只是有限代数/浮点诊断；
Conrey定理、实际来源、无限分析、全局根空间或HH完成不由脚本认证。

脚本LF-SHA256：
bc2f1bd3888ecb1e5c8da9023af07464876a533cc18f86728753bcd179cfc722

子代理另外独立运行该脚本，输出到本目录independent-diagnostics.json。
exit code=0、status=PASS：21项精确假设轨道检查，29项40位有限浮点检查；
最大观察误差1.1116686809924836159e−37，并非区间误差证书。
与公开reviews/2026-10-11/f1-central-mixed-kernel-diagnostics.json比较：
非hash内容经JSON解析完全相同；source LF hashes也完全相同，故完整parsedJSON完全相同。
比较进程exit code=0。独立重跑没有修改任何公共文件。

三篇当前完整稿通过内部独立终审，可按上述范围公开存档。
