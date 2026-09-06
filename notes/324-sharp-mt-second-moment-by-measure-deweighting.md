# 324. 用有限测度去权补出同一sharp MT算子的二阶公式

2026-09-06，持续GOAL周期4第4轮。[T/R，已完成所列范围的独立复核]。
由只读旁线Euler提出，主线程展开；不是直接套用304的固定平滑结论。
原始算术输入已经存在，本篇补的是sharp对象的合法接口，不作新比例或显著突破声明。

## 1. 对象与原始输入

令L=log T，N=N(T)，mathsf A为312–323同一原始半窗L/2的完整实际有限算子，
保留正高度前缀0<gamma<=T的全部零点和重数，tr mathsf A=N，rank mathsf A<=N。
在缩放变量t=u/L下，
\[
 f_0(t)=c_0\cos(\sqrt2t)\mathbf1_{[-1/2,1/2]}(t),\quad
 c_0={1\over\sqrt2\sin(1/\sqrt2)},\quad Q_0=f_0*f_0 .
\]
此处c0是密度归一化常数，不是简单零点比例C0。

令Delta=rho-rho'。以已归档BGST修正版
*Pair Correlation ... I*，arXiv:2501.14545v3（2026-09-01）第7–8页式(3.3)–(3.5)为[R]：
\[
 F_T(v)=\sum_{0<\gamma,\gamma'\le T}
             T^{v(\rho-\rho')}{4\over4-(\rho-\rho')^2}
 ={TL^2\over2\pi}T^{-2v}(1+O(L^{-1/2}))
       +{TL\over2\pi}v+O(T\sqrt L),\quad 0\le v\le1.       \tag{1}
\]
误差对v一致；双和含重数。交换两零点给F_T(-v)=F_T(v)。
因此sup_{|v|<=1}|F_T(v)|<=C TL²。
不把该公式用于深右筛选子和或不匹配的短高度区间。
来源已经归档；本候选使用修正版而非只引用2023旧稿。

## 2. 端点原子必须保留

f0是紧支撑BV函数，其分布导数为有限符号测度
\[
 \mu=-\sqrt2 c_0\sin(\sqrt2 t)\mathbf1_{(-1/2,1/2)}\,dt
       +c_0\cos(1/\sqrt2)(\delta_{-1/2}-\delta_{1/2}).
\]
故Xi=D²Q0=mu*mu是支撑在[-1,1]的固定有限符号测度，
总变差至多||mu||_TV²。
它含端点和中心原子，不是普通的光滑Q0''函数。
Q0本身连续、紧支撑且Lipschitz；例如平移f0的L1变差界和||f0||infinity可直接证明。

由有限和交换及分布积分分部，对每个Delta，
\[
 \int e^{L\Delta v}\,\Xi(dv)
 =(L\Delta)^2\int e^{L\Delta v}Q_0(v)\,dv .
\]
可在支撑邻域外插入恒为1的光滑紧支撑截断，使分布配对完全合法。
于是用1/w(Delta)=1-Delta²/4得精确恒等式
\[
 \boxed{\operatorname{tr}\mathsf A^2
 =\int_{-1}^1F_T(v)Q_0(v)\,dv
       -{1\over4L^2}\int_{[-1,1]}F_T(v)\,\Xi(dv).}         \tag{2}
\]
这是304有限HS恒等式的同一双和；共轭多重集重排保证trace公式，
没有把各个复数项取绝对值后保持等号。
第二项按sup|F_T|与有限总变差为O(T)。

## 3. 第一项及准确常数

由Q0在0的Lipschitz性，
\[
 \int_{-1}^1 T^{-2|v|}Q_0(v)\,dv
 ={Q_0(0)\over L}+O(L^{-2}).
\]
将(1)代入第一项，得
\[
 \int F_TQ_0={TL\over2\pi}
       \left(Q_0(0)+\int_{-1}^1|v|Q_0(v)\,dv\right)
       +O(T\sqrt L).
\]
此处固定Q0有界可积，(1)的一致误差足以积分，不需要平滑日程。
对0<=v<=1，直接卷积为
\[
 Q_0(v)={c_0^2\over2}
   \left((1-v)\cos(\sqrt2v)
           +{\sin(\sqrt2(1-v))\over\sqrt2}\right).
\]
代入并作初等积分，得到经典MT常数
\[
 C_{\rm MT}=Q_0(0)+2\int_0^1vQ_0(v)\,dv
     ={1\over2}+{1\over\sqrt2}\cot(1/\sqrt2).
\]
再用N=TL/(2pi)+O(T)，(2)给
\[
 \boxed{\operatorname{tr}\mathsf A^2
     =(C_{\rm MT}+O(L^{-1/2}))N.}                          \tag{3}
\]
sharp窗是同一窗口，没有先固定delta后直接换成delta(T)。
这补充309只列出固定平滑接口时留下的技术缺口，不声称原先已证明(3)。

## 4. 任意共同正则化下可用的上界

P>=0为全部正列，任意lambda>0给0<R=lambda(P+lambda I)^-1<=I。
由mathsf A=A_+-A_-，
tr(R mathsf A R)_-<=tr(R A_- R)<=tr A_-。
又由迹范数、rank<=N和(3)，
\[
 \operatorname{tr}\mathsf A_-
 ={ \|\mathsf A\|_1-N\over2}
 \le{\sqrt{N\operatorname{tr}\mathsf A^2}-N\over2}
 =\left({\sqrt{C_{\rm MT}}-1\over2}+O(L^{-1/2})\right)N.    \tag{4}
\]
系数约0.0760857784；不声称此单独上界最优。
更有用的接口是||R mathsf A R||_HS<=||mathsf A||_HS=O(sqrt(TL))，
它允许保留共同效应的秩而不先放大成全负迹。

## 5. 核查范围及下一动作

Euler核读BGST上述原始条款，并对照Lamzouri Lemma3.2的平滑去权范围。
Franklin已交叉核对原始BGST第4、6–8页、端点与中心原子、逐对精确去权及独立常数推导；
[完整复核记录](../reviews/2026-09-06/324-325-sharp-rank-review.md)保存范围与异议。
不以PDF归档、有限数值或经典常数相符替代该审查。
下一步分别核算全负迹与保留效应秩的计数后果，防止把正则化成本节省直接当作零密度节省。
