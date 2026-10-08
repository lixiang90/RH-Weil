# 498. 无损分离消费旧 AM 八点证书：67.3546983423%

2026-10-08。本轮在研究 Knausgård 的67.3538200182%方法时，
将其近对剥离与分离集大筛机制用于项目已经准入的 AM 八点证书。
不同作者对全连续 majorant、所有滑窗端项、真实全零点算子及两次极限均已核验。
项目简单临界线比例更新为
\[
\boxed{\liminf_{T\to\infty}\frac{N_0^s(T)}{N(T)}
\ge\frac{66812491}{99194997}=0.6735469834229644\ldots .}
\]
分母计全部非平凡零点及重数，分子计简单临界线零点。
这是无条件解析推论，复用[483](483-admission-of-known-am-eight-point-proportion.md)
已准入的全域有限证书及其明确计算信任范围，不使用7/8条带前件。
不新增无零边界，也不把此比例称为RH证明完成百分比。

正式论文：[TeX](../papers/lossless-eight-point-simple-critical-paper.tex)、
[PDF](../output/pdf/lossless-eight-point-simple-critical-paper.pdf)。
最终源、PDF、数学审查与全页版面记录见
[构建清单](../reviews/2026-10-08/lossless-eight-point-paper-build-manifest.json)。
发布指推送到本仓库；外部期刊评审或arXiv提交不是本轮记录的事项。

## 1. 新的连续 majorant 与近对

保持483的原 AM13窗、十二个余弦系数、归一化质量Z₀和核K。
取θ=4/5、γ=61/100，
\[
g(u)=\gamma[\operatorname{sinc}(\theta(u-1/2))+
                  \operatorname{sinc}(\theta(u+1/2))]^2.
\]
精确有理区间在129个半窗节点证明g−f>9/100，
全域导数界<16、最近节点距≤1/512给整个闭窗g−f>47/800。
另有独立无网格 Bernstein 多项式证明，整个窗的余量>1/50。
两种证明均包含连续桥，不以浮点最小值或网格通过替代全域断言。

矩形 Fourier 因子的卷积给ĝ在|t|≥θ处为零，包括两端点；
Parseval质量Λ=(2γ/θ)(1+sincθ)≤61/32<2。
Chebyshev积分及有理Taylor下界另给|t|≤θ时
K_AM(t)>134/825，平方>1/40>c=805003/10⁸。
这不是把旧 AM 证书换到MT核上。

## 2. 消除平方根和分块损失

固定归一化平滑fε=fχε²/mε；先选mε>61/64，再令高度T趋无穷。
majorant为g/mε，所以任何θ-separated集的Gram范数≤Λ/mε<2。
谱函数φ₂(t)=t²−(t−2)₊²在此集上准确等于平方。

旧局部证书有c=.00805003、B=Σb_r=.00404350，
每个索引跨度的pair权质量≤2。对全部m−7八点滑窗直接求和得
E≥c(m−7)−B span；m≤7也由E≥0覆盖。
在全部n个简单临界线点中取极大不交近对，余集必θ-separated。
每对谱1±|Kε|≤2，支付两个点的2c奖励。
标量凸谱迹的pinching因而给整个实际n列Gram
\[
J(U)\ge cn-B\operatorname{span}(Y)-7c-42d_\varepsilon n,
\qquad d_\varepsilon=\|f_\varepsilon-f\|_1\to0.
\]
旧平方根装配的每点奖励约.00767845733646；新奖励准确为.00805003。
没有给每个簇重付边界，也没有删除首次/末次滑窗或非均匀gap费用。

## 3. 全部真实零点与AM自己的能量

原Hermitian算子A保留线外反射对和重数，trA=N。
取P为简单临界线单位列和，Q=A−P，正惯性p≤(N−n)/2。
完整minmax证明给trA²≥2N−n+J(U)，不要求A≥0。
BGST的无条件全零点相关定理对两个固定平滑测试分别应用，
撤掉相关权后给trA²=(C(fε)+oε(1))N。

先固定ε令T→∞，再ε→0；
span(Y)≤TlogT/(2π)=N+o(N)，C(fε)→C_AM。
重算AM窗自己的能量，仍严格有2−C_AM>67216841/10⁸，
所以比例为(2−C_AM−B)/(1−c)，采用保守有理下端即开头的分数。
没有使用MT未扰动二矩，也没有从带符号全零点双和删除线外项。

## 4. 独立审查、可复现范围与比较

完整解析源与不同作者审查：

- [方法及能量比较](../reviews/2026-10-08/knausgard-673-method-and-am-comparison-research-perron.md)；
- [含无网格Bernstein证书的独审](../reviews/2026-10-08/knausgard-673-lossless-am-review-checkpoint.md)；
- [第二份完整消费链独审](../reviews/2026-10-08/knausgard-673-lossless-am-independent-high-product.md)；
- [外论文局部/storage机制与限定诊断](../reviews/2026-10-08/knausgard-673-local-storage-research-high-product.md)。

新持久[小证书](../scripts/am_lossless_majorant_certificate.py)和
[精确输出](../output/am-lossless-majorant-certificate.json)只核连续majorant、
AM二矩有理下界、近对常数、span预算及比例代数。
在根目录运行python -B scripts/am_lossless_majorant_certificate.py --check。
程序拒绝-O，浮点显示不参与PASS。

旧PC8全域证书的240项任意精度整数编译求值、7项完整结构检查、
人工连续语义与通用Lean内核桥仍按483的组合信任范围消费；
不是240项纯内核证明，本轮不重建完整上游zeta工程。
新论文headline的native_decide计算公理不进入本成果。
本成果也不声称完整Lean形式化验收或外部同行评审已经完成。

相对[2610.08965v1](https://arxiv.org/abs/2610.08965v1)的固定主张，
精确差为719712074/81941515196805>0，即约0.0008783241个百分点。
相对项目旧准入67.3482429920796%，增加约0.0064553502个百分点。
这不是“增加4个百分点”；未把检索不到更高值当作全球优先权证明。

## 5. 下一步与轮数

零点侧保留同一窗与majorant，研究七gap的有界storage修正；
需要同时改善(2−C_AM−7α)/(1−x)，且证明整个连续域。
外论文固定自身窗八点方案上限<.67357，仅约束那一窗和接口，
不把它当ζ比例上限。减少storage oscillation只改善有限端点，不能单独改善渐近比例。

原算术线的[497四个上端素数核心](497-original-prefix-projection-and-low-label-mixed-core.md)
仍未支付signed省幂；本成果没有提供四阶常数或改善451条件边界。
本篇与497属于同一轮继续研究内的用户补充，复盘计数仍为第二周期后第1轮。
下次复盘仍按4–8轮、默认6轮进行。
