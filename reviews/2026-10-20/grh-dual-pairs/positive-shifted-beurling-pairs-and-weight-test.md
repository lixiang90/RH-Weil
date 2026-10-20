# 正continuous Beurling双对象：反射搬运不固定各自的权中心

2026-10-20，root原稿，C027。以562已付同族为输入，新增的是primitive闭合的移位对偶测试，
不是扩参数优化或实际ζ正性新输入。不声明世界首创；原始HL离散系统的假设另核，
本稿属于用户允许的continuous distribution推广，不冒充HL任意discrete dual存在性定理。

## 1. 不能免费tilt primitive：须重构全部重复幂

固定0<c≤1/2、h>−1/2，令

\[
 Z_{c,h}(s)=1+\frac{c}{(s-h)(s-h-1)},\quad
 E_{c,h}(s)=(s-h)(s-h-1)+c.                       \tag{1}
\]

在Re s>1+h定义原Euler支。若α+β=1、αβ=c，取

\[
 A_m(h)=(h+1)^m+h^m-(h+\alpha)^m-(h+\beta)^m,
 \quad C_m=\sum_{k\ge1}k^{-m-1},\quad
 p_{c,h}(u)=\frac1u\sum_{m\ge2}\frac{A_m(h)u^m}{m!C_m}.     \tag{2}
\]

虽然Π的密度可tilt成e^{hu}q_c，不能将P也直接乘e^{hu}：T_k推前会产生e^{hu/k}，
与要求的e^{hu}不同。(2)重新支付primitive正性与全部proper powers。
令b=h+1/2>0、Δ=1/4−c∈[−1/4,1/4)。二项式展开给精确实系数身份

\[
 A_m(h)=2\sum_{k=1}^{\lfloor m/2\rfloor}
 \binom m{2k}b^{m-2k}[(1/4)^k-\Delta^k]>0.                \tag{3}
\]

每个括号非负，k=1严格正，b>0，所以全部m≥2严格正；m=0,1均为0。
四个底数绝对值均≤R=h+1：Δ≥0时用实区间，Δ<0时
|b±i√(−Δ)|²=b²−Δ≤b²+1/4<(b+1/2)²。于是

\[
 0<A_m(h)\le4R^m,\qquad
 0<p_{c,h}(u)\le4(e^{Ru}-1-Ru)/u.                         \tag{4}
\]

正P=pdu局部有限，且对每个σ>R指数权总质量有限。正项Tonelli与pushforward Jacobian给

\[
 \Pi=\sum_{k\ge1}k^{-1}(T_k)_*P,\quad
 q_{c,h}(u)=\sum_{k\ge1}k^{-2}p_{c,h}(u/k)
 =\frac{e^{(h+1)u}+e^{hu}-e^{(h+\alpha)u}-e^{(h+\beta)u}}u
 =e^{hu}q_c(u).                                          \tag{5}
\]

Frullani（或先求导再由实s→∞定常数）给logZ_{c,h}=∫e⁻ˢᵘqdu，Re s>R。
加权正卷积指数真存在，Laplace唯一性给

\[
 dM_{c,h}(u)=\delta_0+c(e^{(h+1)u}-e^{hu})du,\qquad
 dN_{c,h}(x)=\delta_1+c(x^h-x^{h-1})\mathbf1_{x>1}dx.       \tag{6}
\]

密度严格正；全部primitive、powers与nonunit integers连续。h≠0时
N=1+c[(x^{h+1}−1)/(h+1)−(x^h−1)/h]，h=0取对数极限。
dominant exponent是1+h；以下权中心是1/2+h，不等于一般的(1+h)/2。
仅凭主项增长指数的一半不能给twist相容的统一RH中心。

## 2. 两个不同positive系统精确对偶，却不必共享1/2

限制|h|<1/2，以同时支付±h的primitive正性。直接代入(1)得

\[
 Z_{c,h}(1-s)=Z_{c,-h}(s),\qquad E_{c,h}(1-s)=E_{c,-h}(s). \tag{7}
\]

h≠0时两ζ不同。模型Gamma=0，极点分别为h,h+1和−h,1−h，完整保留，
反射把两组极点也一并运输。不要把它们改称两边都有相同0、1极点。

在各自输入预定的pole中点a_h=1/2+h单位化后，完整线性Weil平衡为

\[
 W_{c,h}^{[a_h]}(g)=\int
 [2\cosh(u/2)-|u|e^{-a_h|u|}q_{c,h}(|u|)]g(u)du=W_c(g).
 \tag{8}
\]

这使用本成员自身的精确反射s↦2a_h−s；权由pole与移位数据事先给定，非从零点后选。
c≥1/4时令τ²=c−1/4，(8)给完整平方和与零点
a_h±iτ；c<1/4给a_h±√(1/4−c)的离线对与负Weil测试。
所以两段都满足真正positive arithmetic及(7)，纯性仍是额外性质。

pair相对w=1的权中心互补a_h+a_−h=1，而不是分别被迫为1/2。
对h≠0的正段，以两个不同权中心陈述的pair-RH成立；强求共同1/2的版本失败。

## 3. 自对偶乘积不会制造正性：一个严格负测试

取c=1/4及0<|h|<1/2。各自相对a_±h的Weil核均为2，原零点在各自中心，重数2。
但共同中心1/2下的self-dual product E_hE_−h给核

\[
 W_{\rm common}(u)=4\cosh(hu).
 \tag{9}
\]

取g(u)=uφ(u)、φ为非零非负偶compact光滑函数，则
Q_common(g)=−4(∫g(u)sinh(hu)du)²<0。
两个positive g-integer系统的ζ乘积仍有positive primitive（P相加）、M卷积正，
而其共同中心的Weil正型仍失败。self-dual doubling只增加反射对称，不创造居中或正性。
这与每个成员以正确不同权满足(8)没有矛盾。

## 4. 预定分次纯性可以有多条线

令h1=0、h2=1/4，c1=5/16、c2=13/36。以**给定构造分级**形成
Z_+=Z_{c1,0}Z_{c2,1/4}，Z_−=Z_{c1,0}Z_{c2,−1/4}。
primitive相加、Π相加、M卷积，右半平面取σ>max(1+h_j)，全部正性及powers成立。
两侧仍满足Z_+(1−s)=Z_−(s)。完成化清除四个真实实极点，无复零点／实pole抵消。

正侧两权线为1/2、3/4；负侧两权线为1/2、1/4。
相应imaginary heights为±1/4、±1/3，可直接从已付源平方和读出，而非猜定参数。
预定分次的每一因子都纯，whole却无单一中心线。
这一grading是额外输入；不声称从任意裸分布可以唯一恢复，更不允许按已知零点后验拆权。

## 5. 可消费范围

本稿新付：±h两个不同真正positive primitive系统与精确pair反射、预定权中心测试，
及同一输入的common-product负平方／多权纯性例。
不把Pi正性冒充primitive，不隐去任何pole，不与经典Gamma混同，不调用ζ未知零点。
一般建议是“给定对偶与分次权后，陈述归一化谱的纯性”，而不是普遍的共同Re s=1/2。
任意general distribution可能不延拓／无canonical dual／有branch cuts，届时须换接口，
不强行谈非零entire的连续零除子。来源和正极化前件另见两个独立原稿。
actualζ4/5、成长K/core/coupling与faithful Ξ未改变；本门不完成宏观Goal。
