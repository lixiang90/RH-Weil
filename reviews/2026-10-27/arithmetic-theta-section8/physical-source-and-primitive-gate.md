# Kudla §8：实际primitive设施与物理源桥的准入范围

2026-10-27；/root/theta8_bridge 独占原稿。执行 STATE 唯一[§8来源门](../joint-oldform-tower/next-arithmetic-theta-section8-admission.md)，不修改STATE/cadence/Git，不建立C048/585，不续§9–11或引用链。本稿是实际来源／强旧比较，须与typed原稿、fresh和root消费记录一同验收。

## 1. 这次读了什么，尚未核什么

原件为已库作者PDF，SHA256为47ff2ff6f5151081dd029a1df680377b88d58fc09d6629f3a2b2c3b78bab0f54。本分支独立提取并完整目视PDF31、32中的§8，止§9标题；没有消费该标题后的论述。另仅定位实际被引用的陈述：Theorem6.3及其分解说明（PDF23末／24首），Proposition7.1的分解／符号陈述（PDF25），Theorems7.2（PDF26）与7.4（PDF30）。这些前置结果只作cited，不宣称其证明已审。

PDF32的C∞₀(M(C))并非compact support记号；PDF24的定义是相对于μ积分为0的smooth functions。有限modular输入／有限Arakelov分量与这个无限smooth分量不能混同。PDF31在§8以前可见的Theorem7.5只作背景定位，不作为本项目新的原证明。

## 2. 本章确实给出的实际设施

固定源文的quaternion/算术曲面数据，输入为Γ′=Γ0(4D(B))的weight3/2 cusp forms。§8以Petersson积分定义复线性lift；实际 integrand 是

\[
 f(\tau)\,\overline{\widehat\theta(\tau)}\,
 v^{3/2}\,\frac{du\,dv}{v^2}.
\]

这里τ=u+iv是模变量，f是模形式，不是本项目的physical f=e^(−t/2)r。height pairing第二变量反线性；把上式改为overline(f)·theta会改变线性方向。输入必须匹配原半整数权automorphy，不能仅凭Γ0记号追加“trivial character”。

本章先由adjointness及cited结果给与两个degree/Hodge方向的零配对，再在**f holomorphic**条件下消去mean-zero analytic分量，得到

\[
 \widehat\theta(f)\in
 \widetilde{\mathrm{MW}}\oplus\mathrm{Vert}^{0},
 \qquad
 \mathrm{Vert}^{0}=\mathrm{Vert}\cap
           \ker\langle\,\cdot\,,\widehat\omega\rangle .
\]

这是有实际算术载体的正交分量结论，不是将Pan像按定义叫作boundary；但它不是pure MW结论，也没有在§8证明lift一定非零、MW分量一定非零、或对每个f给严格符号。cited Proposition7.1将MW部分的height与负Néron–Tate pairing对齐；该符号只有在实际分量及其非零性已给出后才可消费。它不能自行证明经典Weil型的符号。

§8对S3/2的定义只写cusp forms，随后明确另加“f holomorphic”才得上述组件。因此只能对**明确指定的fixed-level holomorphic sector**使用有限维性；不能把可能的smooth/Maass cuspidal扩展也无声当成有限维。本稿不补一个源文未完整规定的非holomorphic输入拓扑／增长域。

这里仅消费analytic分量的零配对。Theorem7.4陈述中的classical theta normalization有1/2，§8零式中的theta(φ)记号未在本门进一步对齐；非零height／norm常数不能从这一零等式免费运输。

## 3. 对经典physical源的首门尚未支付

### 3.1 类型与实际映射

本项目原源是全部复S_exp上的r(t)=e^(t/2)f_phys(t)，带原du及zero-extension Dlog。§8没有给

\[
 A:\mathcal F=S_{\exp,\mathbb C}\longrightarrow
 S_{3/2}(\Gamma',\text{matching automorphy})
\]

的物理公式、范数或成长量词。积分中的u不能与log-time t混同。Petersson-lift本身从一个已给automorphic输入开始，不能代替这个缺失箭头。

584的g11是weight2 cusp form；583的F_r=L_r(j)是weight0模函数，一般有essential cusp。二者都不是§8的weight3/2 cuspidal输入。乘／除一个theta factor、投影到holomorphic sector、改character或level都会增加实际前提，不能作为免费类型转换。579–582虽已给全physical源的Schwartz／section／Green强域，其局部Weil可操作性也不等于此处global arithmetic theta functor的源／循环兼容定理。

### 3.2 关系、非根与完整配对

本章正交于1、ω及a(φ)，并不等于消去本项目405真实noncompact Pan及其全部平移。要消费一个新组合J=theta_hat∘A，必须在给出的同一目标／base／mixed pairing中核实际Pan如何成为principal／base或相应配对根；不能先将其像命名为boundary，也不错误要求ker J恰好等于Pan。

同样，537的fixed17/16全复源正性已给真实双polezero非根r0；没有A(r0)便没有该来源的可见性检验。§8不能仅凭存在算术height将这个源认成非零MW类。

本门未支付A的原du／Dlog或必要强半范数费用、source/window/level成长、全部Green尾／vertical项、以及与完整Γ/contact、所有proper powers、双pole的经典signed身份。Petersson积分的定义或有限输入空间中的某个辅助norm常数都不是这些物理费用。

## 4. 必须扣除的最强旧后果

| 旧输入 | 本门必须保留的责任 |
|---|---|
| 519/520实际源商及完整ζ-jets／Jordan谱 | 新几何可以底层factor这个解析商，但必须新增独立结构／费用／符号／mixed比较，不能只重命名谱商 |
| 537固定窗全复源正性 | 可作为明确非根测试，不能替代新source map或成长正性 |
| 552实际径向adelic metric | 合法非零算术对象曾把Pan送到非零energy；所以“有对象／负Hodge号”并不自动支付principal兼容 |
| 579–582实际Schwartz／cycle／Green源 | source合法、局部Weil稳定、全源可见性及强域已付；global primitive／关系／mixed RR并未随之取得 |
| 583/584及finite-cover/tower审查 | raw坐标、principal闭商、actual Pan商和同B后处理分开；不能把旧cusp读出直接当这里的arithmetic lift输入 |

对固定holomorphic sector，若另外强加一个线性A及精确全源Gram身份，使537无限维正窗完全经该固定有限输入编码，则仍受旧finite-rank检验；这只是条件性的旧线性代数责任。§8没有断言这样的A。它不排除单边lower、移动family／cofinal变域、非线性额外数据、nonholomorphic输入，或未逐层消Pan的D′正逼近。

本次获得的是一个真实算术曲面lift的准确组件／输入边界，尚无本项目的新独立primitive源或正号。最强经典542+555→557 whole leading4/5负惯性UPPER及actualq/core/coupling/Ξ未改。建议按**来源／强旧准入审查0数学轮**保存，章门到此止，不预C048/585，不把本章缺桥升级为整个算术theta方法不可能。

## 5. 一个已给公式的后续候选：仅作准入建议，尚未执行

root已提出一个实际Mellin–Bergman候选，区别于仅要求“将r送进S3/2”的未知插值。固定本章同level／automorphy的holomorphic sector S，取其Petersson正交标准基f_j，κ=3/2，拟定义

\[
 W_j(t)=e^{\kappa t/2}f_j(i e^t),\qquad
 A_r=\sum_j\left(\int_{\mathbb R}
             r(t)\overline{W_j(t)}\,dt\right)f_j,\qquad
 J_r=\widehat\theta(A_r).
\]

它不挑新quaternion／level参数；S=0时自然为零。这个候选有清楚的下一首测：核基无关、半整数权类型、0/∞ cusp衰减和全source du/Dlog费用，并检验A的实际像（例如通过imaginary-axis holomorphic唯一性核A(F)=S）。再先扣553真实Pan平移的L² cyclic密度：如果A确为全域有界有限rank读出，其Pan像与全部源像的相等可由密度及有限维闭性检验；再经线性theta_hat后仍是同一像集。因此可先检验同数据的全关系下降是否退化，无需预先证明theta_hat某个MW分量非零、环境arithmetic Chow的Hausdorff性或height正号。这里的有限维代数门与需要closed-base的ambient连续闭商门分开。

本段只确认此候选具有**可执行的actual formula/test/净比较**，不在本次来源门消费其cusp尾、原norm费用或Pan结论为已完成证明。它适合一次短的标准／强旧准入，非新数学合同；若被553直接覆盖便止，不再换basis/level/seed。其失败不覆盖nonholomorphic无限输入、不逐层Pan的极限或真正不同的cofinal域；fixed全域exact下降的有界成员与那些合法逃逸必须分开。

该建议不是第二执行权威；唯一下一动作及是否准入由root在STATE决定。没有实际新结构时，不应顺读§9–11或另一paper来替代缺失的physical桥。
