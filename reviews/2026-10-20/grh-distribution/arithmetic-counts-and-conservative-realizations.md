# 点数分布到完整Weil平方和：圆周能量证书与精确曲线实例

2026-10-20，root原稿，C026。只消费下述确切有限／周期范围，不声称新外部首创。
562已付一般判据和连续正例；这里新增可直接从分布数据核验的算术证书及全周期平方和。

## 1. 输入应先于零点：全次数递推身份

设C/F_q为光滑射影几何连通曲线，g为亏格，N_n=#C(F_{q^n})，B_d为次数d的closed places数。
全部closed places（包括任何仿射模型遗漏的infinity）给positive primitive，
N_n=Σ_{d|n}dB_d支付全部proper powers。Riemann–Roch的有理性与函数方程先给

\[
 Z_C(T)=\exp\sum_{n\ge1}N_nT^n/n
 =P(T)/[(1-T)(1-qT)],\quad \deg P=2g,
 \quad P(T)=q^gT^{2g}P(1/(qT)).                 \tag{1}
\]

这些前件不含Weil零点绝对值结论。对(1)作形式log derivative，从P的系数得到全次数递推，
而非由有限采样外推无限n。上述先后顺序核
[Milne, pp.1–3](https://jmilne.org/math/xnotes/pRH.pdf)：有理性／FE与RH陈述明确分开。
本稿采用已证有理性，但在具体实例中不使用Hasse／Weil的绝对值定理。

令L=logq、m=2g，n≥1时定义

\[
 a_n=q^{-n/2}(q^n+1-N_n),\quad a_0=m,\quad a_{-n}=a_n.
 \tag{2}
\]

归一化完成对象E(s)=q^{g(s-1/2)}P(q^{-s})。在Re w>1/2有

\[
 \frac{E'}E(1/2+w)=gL+L\sum_{n\ge1}a_ne^{-nLw}. \tag{3}
\]

因此原算术数据给完整平衡分布

\[
 W=L\sum_{n\in\mathbb Z}a_n\delta_{nL}
 =2gL\delta_0+L\sum_{n\ne0}
 [2\cosh(nL/2)-q^{-|n|/2}N_{|n|}]\delta_{nL}.    \tag{4}
\]

(3)的gL是(4)原点质量的一半，固定了center contact项；不能删掉它。
(4)包含整个s-plane的周期polar背景，不把它当成普通rank2项。
初始增长由N_n给有限指数阶分布，在每个compact仅有限项；本证书成立后它还是tempered。
式(3)在右半平面精确恢复同一E的log derivative，规范由(1)固定，不是另造正kernel。

## 2. 有限可检验的正能量证书及全部complex源

假定直接由递推给矩阵U∈GL_m(C)，并核

\[
 a_n=\operatorname{Tr}(U^n)\quad(n\ge0),\qquad
 H=H^*>0,\quad U^*HU=H.                         \tag{5}
\]

全n的trace identity可以由特征多项式系数／Newton恒等式和同一精确递推核验，
不是拿有限点拟合未知尾部。H的leading principal minors与线性恒等式可独立精确检查，
不先解P的零点；但在一般大系统中H存在性仍可能是难的正性责任。
令V^{*_H}=H^{-1}V^*H，则U^{*_H}=U^{-1}。

任取complex g∈C_c^infinity(R)，设gstar(t)=bar g(-t)，并在0≤y<L定义有限和
B_y=Σ_{k∈Z}g(y+kL)U^k。直接展开，令n=k-l，给

\[
 \begin{aligned}
 Q_W(g)&=W(g*gstar)
   =L\sum_n a_n\int g(v)\overline{g(v-nL)}dv\\
 &=L\int_0^L\operatorname{Tr}(B_yB_y^{*_H})dy\ge0. \tag{6}
 \end{aligned}
\]

最后一步：H^{1/2}B_yH^{-1/2}的Hilbert–Schmidt范数平方等于该trace。
compact支持保证有限k、l，所有换序无尾误差。此式涵盖任意支持尺度／全部复源，
不是basis diagonal、有限Gram或热迹正性。它完全由点数、递推、H和周期lift推得。

同一结论可写为Toeplitz矩阵[a_{i-j}]≥0。反过来若把所有阶Toeplitz PSD直接假设，
仍只是圆周正型字典；(5)的具体正H和全递推证明才提供有限的可核证书。
规范化酉矩阵也给P的特征值模为sqrtq；这是证书输出，不是前提。

## 3. 一条不读取零点的完整曲线计算

取E/F5: y²=x³+x+1。判别式−16(4+27)≡4 mod5非零，曲线光滑，包含唯一infinity。
逐点枚举得N1=9，故t=q+1−N1=−3。(1)在g=1时给

\[
 P(T)=1+3T+5T^2,\quad S_0=2,S_1=-3,
 \quad S_n=-3S_{n-1}-5S_{n-2},\quad N_n=5^n+1-S_n.
 \tag{7}
\]

这一步只用已知degree2、FE系数关系和点数；不先输入根的模。
取原始有理矩阵和能量

\[
 A=\begin{pmatrix}0&-5\\1&-3\end{pmatrix},\quad
 H=\begin{pmatrix}1&-3/2\\-3/2&5\end{pmatrix},\quad
 A^THA=5H,\quad \det H=11/4>0.                  \tag{8}
\]

令U=A/sqrt5，(5)精确成立，而Tr A^n=S_n由Cayley–Hamilton和初始值支付。
因此(6)直接给完整Weil正性，再由(3)/(1)身份得到函数域RH。没有数值零点／零点拟合输入。
这是已知函数域定理的一个可核实例，不冒称新证明一般Weil定理。

脚本[scripts/grh_distribution_certificate.py](../../../scripts/grh_distribution_certificate.py)
用整数模运算独立枚举F5、F25、F125点数，结果为9、27、108；后二者只作交叉核验，
全次数责任仍由(1)/(7)支付。扩域多项式X²+2、X³+X+1均无F5根，分别二／三次不可约。
脚本用Fraction核(8)及principal minors，全程无浮点和ζ零点库。

## 4. 独立几何来源与指定原作用的边界

一般椭圆曲线的独立输入可来自deg(m−nπ)=m²−t mn+q n²≥0：
degree非负由实际代数映射给出，再推出t²≤4q，不需要预设ζ零点。
这是[Milne p.3](https://jmilne.org/math/xnotes/pRH.pdf)概述的Hasse机制。
在更高亏格中，correspondence／Rosati正性是额外几何结构，不由正点数本身自动推出。

注意(8)严格detH>0是本例直接证书；边界t²=4q时循环companion可有Jordan块。
半正H商空间可能只保C3而丢trace重数，不能自动代同维原Frobenius酉化。
若系数已知P=(1∓sqrtq T)²，可另外给±I于C²的trace实现，但它与指定原作用须分账。
本例H正定已避免该退化，未从Deligne纯性免费推半单。

## 5. 数域与经典ζ缺什么

数域的positive ideal-norm primitive及完成化FE只给数据与反射；它们不提供(5)。
其norm通常没有单一q^n周期，Gamma也不是有限circle contact项。
在已固定约定下，完整W含非零位置的负prime-power atoms；Gamma在这些位置光滑。
故W不能直接等于有限维常系数齐次ODE的解析matrix coefficient。
这只否直接有限实现，不能排无限维无界算子、平滑后相容证书或有符号relative误差修复。

经典所需的下一条真实箭头是：从prime/Gamma/pole实际数据独立给正能量实现，
并证明它对同一完整W在所有尺度成立，或用有控原域误差实现D'收敛。
光有函数方程、正P/N、有限窗或正型锥闭，都不支付这条箭头。

## 6. 最强旧对照与本门净值

562已付连续族完整平方和；本稿不把同族结果再计一次。新增解释是从有限算术递推和有理H
到全周期Weil平方和的可执行证书，及上述确切曲线／标准有理性依赖。
旧041已严格排plain centered Euler remainder的Laplace完全单调捷径，174已说明GNS／紧致性
不能凭空制造正性。本门不重启这些旧等价路线。
actualζ的542+555→557 whole4/5、560成长K/core/coupling和faithful Ξ仍未改善。
