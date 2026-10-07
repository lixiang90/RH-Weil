# 原坏行密度与最终联合包络的全参数比较

2026-10-08，root。基线 2681813154243e10cf4602f4e88514355060d379。
仅新增本稿；既有 source、论文、检查器与计数结论保持冻结。

结论 [T]：即便对全部原 sixth-power-free 行完整证明 BGL 形式的
密度指数 g(a)，直接和 450 的最终联合行数指数取 min，也不会改善
任何 above-floor actual bin。不是只在现有边界的等号角落无效，
而是在整个原参数域上已被原联合包络严格支配。
本稿不否定新 raw-density 估计的独立价值，也不否定另证联合放大的
可能性；它明确排除没有新联合证明的直接替换。

## 1. 实读来源与适用域

| 原来源 | canonical UTF-8 LF SHA256 |
|---|---|
| [450：实际 κ 容量及最终联合包络](../../notes/450-plain-kappa-extension-and-actual-capacity.md) | f16807e0f80461e3005b3173e313218b00f5f86abfa860a4ead79e425dd6bee5 |
| [451：现有边界与实际反馈](../../notes/451-kappa-feedback-cubic-boundary-and-family-continuation.md) | 17ce7fea8c881ebd4034657b7039e99897d4ff9532348993ba329c46e3c4d487 |

canonical 只统一 CRLF/lone CR 为 LF，不 trim 或改 EOF。
另实读一手 [Blomer--Goldmakher--Louvel, Corollary 1.6,
Lemma 2.1](https://arxiv.org/pdf/1112.1650)。该文的 density family 是
primitive squarefree-ideal twists；不能把它原样套给本项目全部
sixth-power-free rows 或冻结 powerful part 后随导子变化的 twist。
下面只比较它明确给出的 g；原全行的准入必须另行重证。
这不把一个尚未证明的 family extension 当成已经支付的输入。

设 actual buffered bin a>51/100，delta=2a−1。
原 whole-family 7/8 bootstrap 的反证域给
\[
 1/50<\delta\le3/4,\qquad
 x=q/\delta\in[0,1/2],\qquad
 \kappa\in[37/50,1],\quad c=1/(3\kappa).
 \tag{1}
\]
450 的实际 κ 调用另须 beta_*≤(1+κ)/2；这个分析前件不由
本稿比较消除。闭端点 delta=1/50 仅用于以下代数延拓，
floor 的实际 count 仍是独立 #rows≪U，不能使用 actual witness 包络。

记 alpha=5/6，
\[
 D=3-(1+2c)x,\quad P=(2-2cx)(1-x),\quad
 J=(\alpha-\delta)D+\delta P .
\]
450 已证明的最终 adaptive count 为
\[
 R_{*,\kappa}(\delta,x)
 =1-\delta+\frac{(\alpha-\delta)\delta P}{2J}.
 \tag{2}
\]
它已经包含同一个 inverse/plain witness、全部正素数槽与合法
sixth-power amplification。它不同于最初的 raw sextic row count
min{1,max(1−delta/2,4/3−delta)}。

## 2. 最终包络的同一全域 upper

因为 c∈[1/3,50/111]、0≤x≤1/2，
\[
 2D-3P=2x(2+c-3cx)\ge0,\quad P/D\le2/3.
 \tag{3}
\]
D、P 为正，alpha−delta≥1/12>0。
固定 delta 后函数 t↦(alpha−delta)delta t/
[2(alpha−delta+delta t)] 对 t≥0 单调增加。
把 t=P/D≤2/3 代入 (2)，直接得到
\[
 \boxed{R_{*,\kappa}(\delta,x)
 \le r_0(\delta):=\frac{15-16\delta}{15-6\delta}.}
 \tag{4}
\]
(4) 不需要选 particular κ、x 或现有边界的等号点，
也不调用新的算术估计。在 x=0 时取等；这只是 count 包络的
worst-x upper，不能把现有 high-exponent 的等号位置改成 x=0。

## 3. 与 g 的两段精确比较

把文献中的 g(a) 写为 delta 变量：
\[
 g((1+\delta)/2)=
 \begin{cases}
 4(1-\delta)/(4-3\delta),&0<\delta\le2/3,\\
 (5\delta-2)(1-\delta)/(6\delta-3\delta^2-2),
                         &2/3\le\delta\le3/4 .
 \end{cases}
 \tag{5}
\]
在两段交界均为 2/3；没有拼接 discontinuous 常数。

第一段的完整差恰为
\[
 g-r_0=
 \frac{\delta(25-24\delta)}
 {(4-3\delta)(15-6\delta)}>0 .
 \tag{6}
\]
对闭区间 [1/50,2/3]，25−24delta≥9，分母≤60；
所以 g−r_0≥3/1000。这个保守 margin 是全区间 exact rational
bound，不是有限网格观察。

第二段的完整差为
\[
 g-r_0=
 \frac{-\delta(18\delta^2-24\delta+5)}
 {3(2\delta-5)(3\delta^2-6\delta+2)}>0 .
 \tag{7}
\]
其分母为 (15−6delta)(6delta−3delta²−2)，严格为正。
二次式在 [2/3,3/4] 单调增加，最大值是 −23/8<0。
还可用 delta≥2/3、分母≤11·13/16，给 g−r_0≥92/429。
结合 (4)，整个 actual above-floor 域有
\[
 \boxed{g((1+\delta)/2)>r_0(\delta)
                    \ge R_{*,\kappa}(\delta,x).}             \tag{8}
\]

## 4. 对原边界优化的实际含义

假如一个新、完全 uniform 的实际密度证明给 #bad rows≪U^(g(a)+eps)，
在 (1) 的同一 fixed data、同一 height 允许量与相同原 rows 上，
与 (2) 直接取 min 仍是 (2)。正高度幂只能在原 tau 选择后支付，
不会使较大的 g 获得负指数费用。
因此不能由这个直接替换降低 451 的任何 count 数值，
不能由“raw count 比以前小”宣称新无零区域。

451 的唯一参考高侧等号点另给
\[
 \delta_*=(5-9e_*)/(6+18e_*)\approx0.388583354266,\quad
 a_*=(1+\delta_*)/2\approx0.694291677133,\quad R_*=2/3.
\]
这里的 a_* 是 row bin，不是最高零族 beta_*。
g(a_*)≈0.862897287510 明显大于 2/3，与全域证明一致。
对高 bin a≈7/8，g(7/8)=7/13 也不能据此声称边界改善：
原联合包络在 delta=3/4 已有 r_0=2/7<7/13。

任何进一步收益需要另证把新 zero-density 和原列放大联合使用的
actual moment/count，不是机械对 g 取幂，也不是把不同零点角色、
高度或 mask 当成相同数据。本稿未支付这种联合估计。
此外已付 472 的 short-carrier fourth P bridge 并不提供角色族密度
的该接口；也不把角色 count 替代标量 prime-ratio 方差。

## 5. 检查与范围

root 用 Sympy 精确复算 (3)、(6)、(7)，分母符号和连续范围如正文。
完整符号证明在正文中，有限数值不是全域证明的替代。
待另一作者按最终全文/hash 独立核对。
没有修改 actual 比例、sigma_*、README 或边界论文，
没有把新的 raw-family 密度前件宣称为已证明的新边界。

本次改变的研究行动是：不再把直接 g 替换作为原边界优化的
候选收益；继续攻击原 scalar short-window ratio 方差，或另证
密度与原 finite prime-slot 放大的联合准入。
