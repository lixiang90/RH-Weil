# 329. 质量加权窗口平均与有密度上限的相位选择

2026-09-06。周期5第5、6个数学动作，[T，已完成所列范围的独立复核]。
327的审查明确区分两种平均；本篇计算此前没有覆盖的那一种，并量化选择窗口时的集中程度。
固定同一对实际节点，沿用327的完整算子和原始权重；不证明这样的实际邻点存在。

## 1. 分别积分再相除

记p=e+d，D0=p²+Delta²，B0=2sqrt(ed)/sqrt(D0)，
phi=Delta L/2-arctan(Delta/p)。这里B0不是327第一节的Q0(0)。
取s<=d,e<=1/2、0<delta0<=|Delta|<=B<infinity，均为固定的范围常数。
0<=y<=H、H->infinity、H=o(L)，目标j、邻点w及其重数在积分内固定。
令
\[
 Z(y)=2m_wG_{e,y}|\Theta_{A_y}|^2,\qquad
 W(y)=2m_j\mathcal H_{d,y},\qquad
 \mathcal R_H={\int_0^H Z(y)\,dy\over\int_0^H W(y)\,dy}.
\]
分母严格正。由327-(2)、(5)，
\[
 \mathcal R_H
 ={m_w\over m_j}\left({d\over e}\right)^2T^{e-d}
 \left[
 {B_0^2\over2}\left(1-\Re\left\{e^{2i\phi}{e\over e+i\Delta}\right\}\right)
 +O_{s,B}\left(L^{-1}+e^{-sH}\right)
 \right].                                                \tag{1}
\]

证明直接保留权重：
\[
 \mathcal R_H={m_w\over m_j}{d\over e}T^{e-d}
 {\int_0^H e^{-ey}{L\over L-y}|\Theta_{A_y}|^2\,dy
  \over\int_0^H e^{-dy}{L\over L-y}\,dy}(1+O_s(L^{-1})).
\]
对最终H<=L/2，因0<=L/(L-y)-1<=2y/L，带e^{-ey}积分后的误差为O_s(L^-1)，
而不是直接丢弃依y变化的权。去掉L/(L-y)并代入主相位后，才把所得指数积分延长至infinity，尾误差O_s(e^-sH)。
原权不能跨过y=L延长。
最后使用
\[
 \int_0^\infty e^{-ey}\sin^2(\phi-\Delta y/2)\,dy
 ={1\over2e}\left(1-\Re\left\{e^{2i\phi}{e\over e+i\Delta}\right\}\right).
\]
分母等于1/d+O_s(L^-1+e^-sH)，即可得到(1)。
系数(d/e)²包含范数权的d/e和积分时标的d/e，不能只保留一个。

括号主项对所有phi至少为
\[
 {B_0^2\over2}\left(1-{e\over\sqrt{e^2+\Delta^2}}\right)
 \ge c_{s,\delta_0,B}>0.
\]
因此最终
\[
 \boxed{\mathcal R_H\ge
     c_{s,\delta_0,B}{m_w\over m_j}T^{e-d}.}                \tag{2}
\]
与327-(9)相比，此平均由y=O_s(1)的质量主导，没有e^{-(e-d)H}损失。
当(m_w/m_j)T^(e-d)本身趋零时，(2)不阻止整体小量；例如e<d且重数可比较。
质量密度W(y)/integral W在y=0附近约为d，不满足下一节固定C/H上限，不能混用两节。
本节特意要求|Delta|>=delta0；不能将它用于Delta->0后声称同一个正常数。
结论仍是单点正泄漏的条件性预算限制，不排除邻点负列或整个簇的带符号响应。

## 2. 有密度上限的窗口选择

现在回到归一化核平方，不先乘G_e/H_d。
令w_H为[0,H]上的任意非负Lebesgue密度，integral w_H=1，
且w_H(y)<=C/H，其中C>=1是固定常数。
允许w_H依赖L、Delta、e、d和节点的实际相位。
仍取|Delta|<=B，Delta!=0，并要求H|Delta|->infinity。

则
\[
 \boxed{\liminf_{T\to\infty}
 \left[\int_0^H w_H(y)|\Theta_{A_y}|^2\,dy
       -B_0^2 J(C)\right]\ge0,\quad
 J(C)={1\over2}-{C\over2\pi}\sin{\pi\over C}>0.}           \tag{3}
\]
当d,e,Delta随T变化时，(3)应按方括号中当期B0理解；
固定s、B保证B0²具有统一正下界。
该相位问题的常数J(C)是最优的，不是由Schur包络产生。

### 下界证明

对f(y)=sin²(phi-Delta y/2)、0<=lambda<=1，用密度上限得
\[
 \int w_H f\ge\lambda-{C\over H}\int_0^H(\lambda-f)_+\,dy.
\]
任一有界pi周期函数在这个线性相位区间上的均值与一周期均值差O(1/(H|Delta|))，
不依赖起始phi。选a=pi/(2C)、lambda=sin²a，其周期均值为
\[
 {2\over\pi}\int_0^a(\lambda-\sin^2t)\,dt
 ={2\over\pi}\left(\lambda a-{a\over2}+{\sin2a\over4}\right).
\]
故右端为J(C)+O(C/(H|Delta|))。由327的统一核误差，得到(3)。
正性来自sin u<u（0<u<=pi），C=1时J=1/2。

### 最优性的范围

令P=2pi/|Delta|、n=floor(H/P)、r=H-nP。
每个完整周期选择sin²最低的P/C长度，取w=C/H；总质量1-r/H，总贡献(1-r/H)J(C)。
在剩余r长度中另选长度恰为r/C的可测子集，取同一密度，补入质量r/H。
其贡献在0和r/H之间，故所得平均为J(C)+O(1/(H|Delta|))。
再用327-(5)核的均匀误差得到归一化混合核的可达性。
此构造总积分恰为1、密度上限恰满足，含C=1和r=0；只保证单对节点相位最优，
不证明同一个权重可以同时优化多对节点。
这里允许w依相位选择，未声称这些权重满足其他未列出的算术选择要求。

## 3. 对实际单点预算的含义

在327-(8)中，若e>=d，固定C且上述相位扫过条件成立，
区间最小权和(3)给
\[
 \int_0^H w_H(y){Z(y)\over W(y)}\,dy
 \ge c_{s,B} J(C){m_w\over m_j}
       T^{e-d}e^{-(e-d)H}                                \tag{4}
\]
最终成立；隐常数可以固定并将o(1)吸收进J(C)>0。
它覆盖均匀平均及任何相对于它有固定密度上限的相位适配选择。
若要使同深度、可比较重数节点的这个预算为o(1)，
单靠这类分散权重不够；须放开固定C、改变节点信息或使用其他带符号机制。

J(C)=pi²/(12C²)+O(C^-4)是C->infinity时的标量展开。
但(3)首先对固定C证明；若令C=C(T)，必须重新比较C/(H|Delta|)、核误差和J(C)，
不能把固定C结论直接升级为任意增长权重的障碍。
点质量窗口选择不满足密度上限；本篇没有排除特殊窗口。

## 4. 当前状态

这是同一有限变窗任务中对两种不同归一化及权重约束的核算。
[Franklin独立复核](../reviews/2026-09-06/329-window-density-review.md)已通过主公式，
有限区间的末尾质量账本、积分延长顺序已补准；不是实际覆盖、零密度或RH的新结论。
现停止已明列的两类平均小量论证；继续保留集中窗口、邻点负列、
多方向联合相位和新的算术相关输入作为未被排除的方向。
