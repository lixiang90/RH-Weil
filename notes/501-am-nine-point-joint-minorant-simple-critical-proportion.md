# 九点共享核值证书与新的简单临界线比例

2026-10-08；基线 `37eb770afac0317b9329435fe0eabb50bc0f0874`。
继续研究2610.08965v1的分离集、局部证书与全零点计数机制。
在[483](483-admission-of-known-am-eight-point-proportion.md)明确披露的连续审查和组合计算准入范围内，
本轮补齐[500](500-am-nine-point-low-slack-cover-and-adaptive-spectrum.md)的所有兼容域，得到
\[
 \boxed{\liminf_{T\to\infty}\frac{N_0^s(T)}{N(T)}
 \ge\frac{66812491}{99194897}
 =0.6735476624367078076607\ldots .}
\]
分母计全部非平凡零点及重数，分子计简单临界线零点。
该解析推论不使用RH、普通ζ的7/8条带或更高相关猜想；它保留原PC8计算信任范围。
不同作者分别重建全部有理矩阵、连续覆盖和完整计数链。
按用户“确认新比例后写论文”的要求，完整证明另保存为
[正式论文](../papers/nine-point-joint-minorant-simple-critical-paper.tex)和
[10页PDF](../output/pdf/nine-point-joint-minorant-simple-critical-paper.pdf)。

## 1. 固定输入与比较

保持AM13原窗、原权表和总压力
\(B=404350/10^8\)，旧奖励记\(c_0=805003/10^8\)。
设\(\theta=4/5\)、\(\delta=10^{-6}\)、\(c_1=c_0+\delta=805103/10^8\)。
八个真实连续间距\(g_r\ge\theta\)的左右七间距帧分别为\(h^-,h^+\)，定义
\[
 F_9(g)=\tfrac12\{F_8(h^-)+F_8(h^+)\}
                +2K(g_0+\cdots+g_7)^2.
\]
每个索引跨度的总权≤2，八个间距费用总和仍B。
新局部结论是完整非紧域\([4/5,\infty)^8\)上\(F_9\ge c_1\)。
跨度8只消费非负性；本次实际增益已由两帧共享的33个旧物理核平方给出。

相对[498](498-lossless-am-eight-point-simple-critical-proportion.md)，实际比例提高
\[
 \frac{66812491}{99194897}-\frac{66812491}{99194997}
 =\frac{6681249100}{99194897\cdot99194997}>0,
\]
即约0.0000679013743个百分点。
相对2610.08965v1固定基准\(1669159/2478195\)，提高约0.0009462254721个百分点。
这不是穷尽所有并行工作的全球优先权声明，也不是RH证明的完成百分比。
451条件无零边界、原全局四阶增长幂和实际中心常数均未改变。

## 2. 完整低集与真实重叠

令\(T=\{h\ge\theta:F_8(h)<c_0+2\delta\}\)。
任一帧不在T，旧全域证书及平均已给\(F_9\ge c_1\)。
500已完整排除旧small-gap、clear-COV、large-gap、方向和空叶的未付可能，
保持全部32根、闭边界、旧reward/cursor与连续语义，捕获70个闭胞。
全span反射给140个带来源标签、132个几何不同的胞。
19600个有序拼接对保留全部八间距和27长跨度，精确差分闭包后共有289对。
这些外胞允许重叠，不能将域数量当成零点配置数量或覆盖体积。

本轮增加每胞26组RAW10与YA16，恢复原有效点、导数区间、完整仿射式和Farkas比较。
首先联合最小化原仿射线，回收独立角点和原Farkas损失，支付206对；仍有83对。
最终保留每个启用点的独立有效下界及两帧共用核变量，全部289对支付。
数学恢复及第一层诊断见[167行研究源](../reviews/2026-10-08/am-affine-leaf-minorant-research-perron.md)。

## 3. 两端锚定切线与有限盒对偶

旧连续原子在真实\([l,u]\)上担保
\(w(x)\ge v+d(x-p)\)、\(v\ge v_0\)、\(d_-\le d\le d_+\)，且启用点\(p\in[l,u]\)。
这里\(w=K^2\)；只有点值和点导数不足以担保完整切线。
有效的两条独立线为
\[
 L_p(x)=v_0+d_+(l-p)+d_-(x-l),\qquad
 U_p(x)=v_0+d_-(u-p)+d_+(x-u).
\]
原切线减L为\((d-d_-)(x-l)+(d_+-d)(p-l)\ge0\)，
减U为\((d_+-d)(u-x)+(d-d_-)(u-p)\ge0\)。
不能误用\(v_0+\max\{d_-(x-p),d_+(x-p)\}\)。
点锚使用原真实端点；零宽查询的扩大区间只用于constant lb。
每一实际距离共用一个z变量，汇总两帧全部constant与启用切线。
AM密度正、质量1，故真实\(0\le z=K^2\le1\)。

每域共有八g和34z，即42变量，矩阵\(Ax\le b\)与有效有限盒\(\ell\le x\le u\)。
整数目标q满足\(q^tx=2\cdot10^8F_9\)。
任意非负有理乘子\(\lambda\)和残量\(r=q+A^t\lambda\)严格给
\[
 F_9\ge\frac{-\lambda^tb+
 \sum_i r_i(\ell_i\mathbf1_{r_i\ge0}+u_i\mathbf1_{r_i<0})}{2\cdot10^8}.
\]
浮点HiGHS仅定位乘子；全部舍入残量按完整盒以Fraction支付。
不依赖浮点可行性、驻点、互补松弛或最优状态。
最低112/42的精确下界为
\[
 M=\frac{65955289561887369906031994339}{8192000000000000000000000000000},
 \quad M-c_1=\frac{1251801887369906031994339}{8192000000000000000000000000000}>0.
\]
未单凭这个有限余量提高统一奖励；低集外分支仍以当前\(2\delta\)阈值付款。

## 4. 从连续局部域到全部实际零点

完整反射覆盖及289份对偶给所有分离九点窗\(F_9\ge c_1\)。
滑窗每span≤2、总压力B给\(\sum_{i\ne j}K(y_i-y_j)^2\ge c_1(m-8)-B\,span(Y)\)。
近对剥离后的分离集仍用498已证的质量<2 majorant；原窗能量不变。
固定平滑ε时，九点总权≤16，每核平方变化≤\(2d_\varepsilon\)，
因此完整Gram收益\(J(U)\ge c_1n-B\,span(Y)-8c_1-32d_\varepsilon n\)。
近对奖励\(2c_1-4d_\varepsilon\)和scalar convex pinching支付其余点。

保留全部离线反射对、重复点的真实μ权及简单P。
原Hermitian/minmax计数给\(tr A^2\ge2N-n+J(U)\)。
无条件BGST相关经两个固定光滑test准确撤权，先T→∞、后ε↓0。
既有精确能量\(2-C(f)>67216841/10^8\)给
\[
 \liminf n/N\ge\frac{2-C(f)-B}{1-c_1}
 >\frac{67216841-404350}{10^8-805103}
 =\frac{66812491}{99194897}.
\]
这里只改变已付局部奖励和滑窗端项，不删除线外零点，也不替换扰动窗的能量成本。
正式论文完整写出解析引用、连续majorant、惯性及两次极限。

## 5. 实际验证与信任范围

[236行标准库程序](../scripts/am_nine_point_epigraph_certificate.py)和
[完整原子及289份稀疏对偶](../output/am-nine-point-epigraph-certificate.json)已持久保存。
`--check`重建原guard、矩阵、目标、有效盒、全部分数残量与最终ratio。
`--replay`从固定原Solution及两个准入桥重建隔离capture，
实际Lean v4.34.1 exit0、41项旧检查全true，70组RAW/YA逐字段等于持久记录。
Root实际执行两种模式；`-O`实际退出1，拒绝关闭assertions。
旧240项表验证和连续语义沿483准入复用，没有谎称在新41项中重新运行。
它不是整条定理的纯Lean内核证明，也不消费Knausgård headline native计算公理。

不同作者[130行对偶／覆盖独审](../reviews/2026-10-08/am-nine-point-epigraph-review-high-product.md)
不导入作者模块、不使用SciPy，独立重建1820原子和全部19600配对、289矩阵/乘子/残量，实跑通过。
最终论文的不同作者全链复核及全部源/PDF哈希见
[构建清单](../reviews/2026-10-08/nine-point-joint-paper-build-manifest.json)。
PDF全部10页已渲染逐页检查；内部AI协作审查与外部同行评审分开。
majorant精确核验、注册覆盖和目录回归实际通过；core=89、all=91，仅核本轮相关检查，未重跑整套91项。

## 6. 原算术目标与下一轮

[174行真实短窗源](../reviews/2026-10-08/original-product-fiber-short-window-research-checkpoint.md)
保留\(k=pr\)、全部\(D_\gamma(v)\)及slow相位，准确恢复partial-Fourier Gram
\(\sum_{k,k'}d_k\bar d_{k'}D_\gamma(v)\overline{D_\gamma(v')}L_q((k'-k)/q^2)\)。
完整共享素因子行和付\(qJ(1+q/P_{min})\log q\)，外F消费后为\(X^{1/2}\log^C X\)。
互素产品signed covariance在全部真实q、参数及packet聚合后只取一次正部，仍未付。
顶端充分目标是\([C_{cop}]_+\ll X^{1+2B_*-\eta}\)，\(\eta>0\)，保留B*全部前件。
这不是新的全局四阶或条带界；普通ζ7/8依然不能替代451的完整Hecke输入。

若以新p作为flat中心四阶比较值，需\(B_4<4/(9p)-1/3
=196342115/601312419\approx0.32652263415168214\)，另付实际配置误差。
条件67.356%的适应性谱正平均前件仍开放；500中的条件代数未自动升级。
本轮是上次复盘后第4轮。实际比例改变触发提前
[第三周期复盘](../goals/reviews/2026-10-08-original-route-review-cycle-3.md)，完成后重新计数。
下一轮优先新的完整低集阈值／多帧有效切线证书，并行攻真实互素产品带状相关。
原完整Goal保持active；不以辅助付款、论文交付或这次小幅比例改进替代完整目标。
