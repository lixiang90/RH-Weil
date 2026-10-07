# 根节点审查：数域选择、Gaussian signal 与条件放大

2026-10-07。限定 PASS：本次回答研究的是辅助数域的依赖及可替代接口，
没有得到新的无零边界。原目标仍 active；已有三次论文的 [R] 范围不变。

已全文读取数域逐接口报告、457、Gaussian quartic 新研究；逐段核原固定
paper.tex 的766–835、1676–1815、2640–2672、7697–7702、12362–12460，
并浏览 GL/BGL 原始大筛、DDHL v5 §3/§4.5/Lemma9.2 及 Watkins §3.6。
没有运行或认证外部整链 Lean kernel，也没有把一般文献摘要当成新的
completed reflection 输入。

## 接受的数学范围

1. 原−3系统的 decisive savings来自 cubic theta 与 sextic反射后 residual
   j=1降到 quadratic。直接 Gaussian chi²/+2 替换同时破坏旧 Gauss phase
   和二次终端；这排除的是该字面设计。固定域的判别式、格密度及finite
   unit factor影响常数，source1/6来自a⁶而非六个单位。
2. single-shift模板下 rho≡m−1 mod2m、chi^rho的阶表严格正确。
   d4要求rho1只是这个模板的条件；quartic theta是具体候选架构，
   不是一般方法唯一可能的构造。
3. 457 的 inverse-column divisor identity含Nb^-1/2和全部 natural
   zeros。每个固定c>0的raw scale supremum、linear multipliercount、
   compatible injective rows等前件足以给e_d(r)。必须先按bounded r
   与最终epsilon选c，某个固定c的bound只能给e_(d,c)。未假定Gaussian
   新域已经有raw moment，更没有将unmarked lemma替代marked/plain。
4. DDHL v3 Gauss印刷式的漏项在v5已修。degree-one处补因子等于epsilon
   的二次互反证明有效，得gamma1²=−alpha；inert处通过Frobenius与trace
   invariance得平方1，未擅自定Gauss正负。quartic CRT因子属于±1，
   平方后消失，故全部odd-primary-squarefree c有gamma1(c)²=mu(c)alpha(c)。
   相位变化、坏素数与nonunit不能丢。这个真实signal不供应全Euler商。
5. Gaussian研究定义的有限核K_j，不是冒充已存在的global theta theorem。
   先对h求和再令t=1/v，j1/2给tau_j^-tau_(j+1)^+ chi(x)^(-j-1)，
   j3给Ramanujan分支，j0给−q^-1/2tau1^+chi(x)^-1。四分支与zero
   extensions正确。rho1在local algebra可行；whole moving-row完成仍开。
6. DDHL平方指标公式与specific square-numerator Voronoi确为已证起点，
   但未评价general exponent-one core。把所有characters作用于n²b⁴会
   改为even incoming exponent和target eta²。在同一固定ray群寻找
   square root不总合法；扩modulus/改变probe须另外证明兼容性。
   此障碍限literal square-index/full-index-weight设计，不是全Gaussian
   绝对不可能性。坏nonunit的Gauss列须用实际primepower表。
7. CM普通FE的conductor指数1/2−s不乘度数；gamma比值的阶数变为r2。
   高次CM无限单位使按所有norm-bounded elements计数失效，ideal count
   linear并不自动修复row合同。普通FE不可替代cubic/quartic theta完成。

## 实际修正与验证

数域初稿含一个 lone CR 损坏了 `\rm sf`。根节点修复为合法TeX；
依独审意见补齐“每个固定c>0”的量词，并将rho1与quartic实现区分。
457 曾在研究过程中读旧DDHL v3，尚未提交时已全部改为v5、补入
supplement及split/inert/CRT证明，最终正文不保留漏项推论。

[精确脚本](../../scripts/hybrid_number_field_exact_audit.py)使用Gaussian
整数、有限Fp/Fp²及Fraction，核44个split与6个inertprime、10个shift模型。
输出对象与保存JSON一致。它证伪旧版uniform quotient的q5读法并核
显示的有理指数；不把样本代替一般证明，不认证theta/解析矩/无零域。

另用独立有理函数运算核定量逆审的 short/long 恒等式：short(ell)−2/3
等于其显示的三次多项式余式，long6(ell)=2/3；重平衡差的第一表达式
为有理恒等式，第二表达式须使用既有隔离三次根，分子除以该三次式
余数为零。因此在原cutoff，改进long alone的总count收益为0；反事实
保留原short合同并重选cutoff才得该报告的较小条件收益。这仍非sigma。

冻结数学稿：457 canonical LF SHA256
`75079970955602644a9290709f66e2be331ad6116d2a637ed8fc97fb0dde5791`，15254bytes。
修复后的数域报告SHA256
`47453b09c0491a201ef39667a123d046c39ed2e2df906c866f101b0796a443bb`，17196bytes。
其他最终文件与来源保全绑定见
[数域检查点](number-field-choice-checkpoint.json)。

结论：可以继续试验Gaussian的实际quartic完成；已经有真实sf signal与
local quadratic核，但所有决定边界的global合同仍需证明。无新sigma、
无新比例，本轮不触发另写边界论文的条件。
