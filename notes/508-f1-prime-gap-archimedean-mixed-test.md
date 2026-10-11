# 508. 素数间隙中的实位混合检验与有限加权闭类零性

2026-10-11。与[507](507-f1-canonical-periodic-phase-and-source-flux.md)合计一次研究迭代。
相位合同已在固定双有限位来源的有限源域完成。本稿把下一adelic桥的必要检验收窄为一个避开全部素数幂的测试：
旧物理读出严格为零，固定Weil混合配对的实位贡献严格为正。相位修复不能填补这个差值。
另证明仅用原有限源加权词修补的闭链必为零类。

## 1. 先固定卷积、反射和算术分布

保留[403](403-f1-support-locality-and-nonperfect-quotients.md)、[404](404-f1-adelic-periodic-orbits-and-mixed-local-trace.md)的约定

\[
 f^\sharp(x)=e^{-x}f(-x),\qquad
 (f*g)(x)=\int f(t)g(x-t)dt,
\]
\[
 h={f*g^\sharp+g*f^\sharp\over2},\qquad
 W_{\rm pol}(f,g)=N(h).
\]

对 \(h(0)=0\) 且在零附近消失的本稿测试，固定定义准确为

\[
 N(h)=\sum_{n\ge2}\Lambda(n)h(\log n)
 +\mathcal A_\infty(h),\qquad
 \mathcal A_\infty(h)=\int_0^\infty{e^{2x}h(x)\over e^{2x}-1}dx.
 \tag{1}
\]

全部和有限，积分远离0且紧支；没有单位元正则化或未付款的收敛问题。

## 2. 一个只含实位的严格正值

令

\[
 b={\log2+\log3\over2},\qquad
 0<\varepsilon<\min\{b/3,(\log3-\log2)/4\}.
\]

取非零非负 \(\varphi\in C_c^\infty((-\varepsilon,\varepsilon))\)，置
\(f=\varphi\)、\(g(x)=\varphi(x-b)\)。二者支集分离。
两项卷积的支集分别位于负、正 \(b\) 的 \(2\varepsilon\) 邻域，故 \(h\ge0\)、\(h(0)=0\)，且正支集完全落在
\((\log2,\log3)\)。在 \(b\) 处作 \(t=u+b\) 代换，得到

\[
 h(b)={1\over2}\int e^u\varphi(u)^2du>0.
 \tag{2}
\]

没有整数 \(n\ge2\) 的 \(\log n\) 落在这个开区间，因此

\[
 h(\log n)=0\quad(n\ge2),\qquad
 \boxed{W_{\rm pol}(f,g)=\mathcal A_\infty(h)>0.}
 \tag{3}
\]

严格正性由(2)、连续性和积分核的严格正性给出。这里不仅避开2、5，还避开全部素数幂。
没有假设RH、RR或任何新数值下界。

## 3. 原双有限位源在同一测试上准确为零

425采用的准确时间变换为

\[
 \eta(s)=e^{-s/2}h(-s).
 \tag{4}
\]

\(h^\sharp=h\) 使 \(\eta\) 为偶函数；\(\eta(0)=0\)，其支集避开所有
\(\pm m\log2,\pm m\log5\)（\(m\ne0\)）。435的完整球读出因而给

\[
 \Lambda(\eta)=0,
 \qquad \operatorname{Tr}(P A(\eta)P)=0
 \tag{5}
\]

在原精确式允许的足够深独立双截止上成立。两个体积项也为零。
507在 \(B=U(\eta)\) 上给常数对角 \(C_B=\eta(0)=0\)，零均值相位准确为零，并保留这个原读出。
所以相位修复后的 \(R(A(\eta))=0\)，仍与(3)不同。

这是收敛读出的实际缺项，不是437的振荡，也不是可调整的 \(\delta_0\) 常数。
物理时间取实数值并不赋予双有限位源一个实位几何分量。

作为归一化对照，若改回403的 \(b=\log2\) 并把正支集限制在 \((0,\log3)\)，同一计算给

\[
 W_{\rm pol}(f,g)=(\log2)h(\log2)+\mathcal A_\infty(h),
 \qquad {\Lambda(\eta)\over2}=(\log2)h(\log2).
 \tag{6}
\]

源端正负一次周期各贡献一份，二分后准确匹配2的局部项；实位正差值仍在。
单独通过素数2的原子测试不能成为完整混合检验。

## 4. 旧闭链电荷和有限加权修补的严格限制

432已有规范普通迹电荷
\(\Omega:HH_1(Q_{\rm src})\to\mathbb C\)，旧角闭链给

\[
 \Omega(qA(f)\otimes qA(g))=-4\int s f(s)g(-s)ds.
\]

本稿分离支集测试使该积分为零；将 \(g\) 换为 \(g^\sharp\) 后同样为零。
这两种直接接法都不能得到(3)。
相位读出在迹类理想上保持普通迹，因此不能改变这些已经闭合的一链电荷。
将旧链对称化也只会使交换子逐项抵消；这不是需要的对称Weil配对来源。

再令 \(F\in D_{\rm src}\)，原加权一链为

\[
 c_F=q(u^*)\otimes q(uF),\qquad
 b_1c_F=q(F-uFu^*).
\]

[431](431-f1-source-orbit-essential-symbol-and-boundary-injectivity.md)证明
\(1-\operatorname{Ad}u\) 在有限源商 \(D_{\rm src}/\mathcal S_1\) 上单射。因此

\[
 c_F\text{闭合}\Longrightarrow q(F)=0\Longrightarrow c_F=0.
 \tag{7}
\]

有限个同型源轨道加权词的和仍为某个 \(c_{F_{\rm total}}\)，所以闭合时也是零链。
这排除了这个受限有限修补，未排除不同第一张量因子、新边、新相对理想或有独立收敛证明的无限转移。
相位函数的改变不修改商映射或Hochschild边界，因而不改变(7)。

## 5. 下一合同需要实际实位边项

404已经有包含∞的有限 \(S\) 来源，按其已审经典半局部迹定理，在本稿测试上
\(S=\{\infty,2,5\}\) 给 \(\mathcal L(h)/2=\mathcal A_\infty(h)\)，两个有限位项为零。
这是现有来源定理的消费，不重称为新的全局迹证明。
其截断 \(R_\Lambda=(\mathcal F P_\Lambda\mathcal F^{-1})P_\Lambda\) 通常不是正交投影；不能据此推导正性。

下一轮固定本稿的 \(f,g,h\)，只做以下来源比较：

1. 在404实际有限 \(S\) 表示中指定实位算子及截止，计算产生(3)正值的原核或边项。
2. 给包含实际压缩、Fourier截止或新边的相对闭链，并证明迹类准入；不得用(7)的零链支付。
3. 从来源比较其电荷与 \(\mathcal A_\infty(h)\)，不按这个目标值反向定义链或配对。

同一交换群的裸表示积分算子本来交换，直接取它们的交换子仍为零；必须保留真实压缩／边界。
即使本例通过，也没有确定单位元常数、完整主关系、全测试类交叉或正性。
后续主商仍须通过403的
\(\ker\overline A\subset\ker M_0\cap\ker M_1\cap\operatorname{rad}W_{\rm pol}\)，以及405对真实限制关系的检验。

本轮新增的是(3)的实位间隙测试及(7)的有限加权闭类零性，证明由固定支持和既有实际公式直接给出。
完整独立核对见[桥接审查](../reviews/2026-10-11/f1-phase-adelic-bridge-review.md)。不声明完整Weil正性、RR、RH或新的无零界／零点比例。
