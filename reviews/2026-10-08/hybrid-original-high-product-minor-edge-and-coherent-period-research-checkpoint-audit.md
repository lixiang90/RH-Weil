# 原高产品余项：产品感知点界、完整频率端period付款与coherent接口

2026-10-08，checkpoint_audit。基线 main 3afd193，复盘后第1轮。
只新增本源，不修改冻结输入、旧peer、输出或Git。

本稿有两个无条件实际估计。真实正频带的素数产品腿可统一付
|G|≪√X log^C，所有 twists和sharp q-prefix均在；
在真实产品 Z<qs≤X^(12/7−η)、固定0<η<1/100内，共同J_q的
至多两个不完整mod q端period，整个K频率mask付款为
O(X^(5/7−η)log^C X)。后者是自然完整频率子族，确实跨过
相应f+g门槛；它不是该产品方面比内整个K的付款。

本稿另给不同L^p配对的准确新输入门槛，以及完整period中
真正保留j方向signed coherence的接口。尚未证明该coherence
节省或完整K预算，没有新whole、常数中心四矩、比例或无零边界。

## 1. 当前准确对象与冻结身份

本轮 FULL READ [489](../../notes/489-original-high-product-rational-minor-slice.md)
全部85行和[337行新切片源](hybrid-original-high-product-minor-rational-slice-research-high-product.md)；
沿连续研究轮已全文核读的[actual425](hybrid-whole-fourth-unit-unit-actual-research-whole.md)
与[minor464](hybrid-original-unit-band-minor-lift-research-pc8.md)继续。
canonical UTF-8 LF SHA256：

- 489：c39081acaf5d1bd22685df4a918d42b1bffa635bb15a09b41b66794654ecdddd；
- slice337：56219e9f136c0f0666c5b1ce028ec4d7d93ad33f5ebd43d5e4a5e34c399677a8；
- actual425：b3f14cf4ee5659f8e23bd51dc9bf71e853e783bd2d55e42ee8846d6e8d1e41dc；
- minor464：b6018e1254049b77dd5d7f73f4d3a7dc7272d5fe5dd3568f3c5ddf8cf73928b4。

保持X=T/(2π)、L=logX、b_p=log p/(a_LL√p)、a_L≥c_φ>0。
所有prime在(√X,X]，q是真正最大prime；s<q、p,r<q。
原χ-carrier signed平均、两套same-u profiles、ν正高度和floors、
carry interior、产品窗g和sharp endpoints均沿489的已准入对象。
不从某个完整signed误差界限制出新的频率子族。

令W=X^(1/10)、B=X^(1/5)、Z=X^(1193/700)。
当前K在qs>Z且真实interior上，n同时不存在
d≤W、半径W/(dS)的整数平移有理表示，也不存在
W<d≤B、半径1/S的表示。S始终是dyadic scale。
该mask只依赖q,n,S，并且严格mod q周期：n→n+q时平移m→m+1。
不能改写成分母B、半径B/(dS)的另一个合同。

先利用ν零支撑恢复唯一共同

\[
 J_q=\left[\frac{q\theta_-}{4\pi S},
            \frac{q\theta_+}{2\pi S}\right]\cap\mathbb Z
       =[l_q,h_q]\cap\mathbb Z,\quad
 |J_q|\ll qX/S,\quad J_q\subset(0,q^2).
 \tag{1}
\]

再分离V(y)=Xν(2πXy)、g和原C² profiles。
对每个固定共同参数λ，准确两腿为

\[
 F_{q,n}=\sum_{s\in S_q}b_s(s/S)s^{it_s}e(ns/q),\qquad
 G_{q,n}=\sum_{p,r<q}b_pb_rp^{it_p}r^{it_r}e(-npr/q^2).
 \tag{2}
\]

全部实际dyadic supports保留，PR≍QS、P,R≤q up to固定倍数。
前因子准确为(2πS/(QX))·(Q/q)·(s/S)·V(sn/(qX))；
模长1的n-twist留在外面。共同参数的正包络L1为L^C，
全部空间积分仍是同一个u。分离之后不保留individual(s,n)频带指示。

## 2. 真实G的统一√X点界

这一证明用已实际核读完整命题及证明的
[Kedlaya作者讲义 Theorem17.5](https://kskedlaya.org/ant/chapter-17.html)：
模1的ρ-separated频率族对长度N fixed coefficients付ρ^(-1)+N。
以下系数可依赖q和共同λ，因为估计逐q,n且对任意系数成立；
没有向一个联合q-family大筛塞入私有系数。

对真实n∈J_q，置α=n/q²。正guard和(1)给
α≍X/(qS)>0。高产品QS>Z/4保证充分大X时α<1/2。
令b=floor(1/α)，则b≥2、1/(b+1)<α≤1/b、b≍qS/X。
在任一b个连续r整数内，两个不同频率差为αh，1≤h≤b−1；
到整数的距离至少
min{α,1−α(b−1)}≥1/(b+1)。
这是不绕回的实际间距，不是任意rational approximant假设。

将原R区间按连续b个整数分块，块数≤C(R/b+1)。
对每块，由additive大筛和一次r-coefficient Cauchy，
该块的双线性和平方≤C(P+b)·||a||2²·||b_block||2²。
再在完整块族作Cauchy，得到

\[
 |G|^2\ll(P+b)(R/b+1)
           \left(\sum_p|b_pp^{it_p}|^2\right)
           \left(\sum_r|b_rr^{it_r}|^2\right)
 \ll (PR/b+P+R+b)L^C.
 \tag{3}
\]

g/profile已通过共同参数分离；真实strict q-prefix只在原系数中置零，
不增加l2。全部twists模长为1；常数不随参数大小增长。
PR≍QS、q≍Q、P,R≲q≤X，b≍qS/X≤CX，
故每项在(3)均≤CX，严格得到

\[
 \boxed{|G_{q,n}|\ll_\phi\sqrt X\,L^C,\qquad n\in J_q.}
 \tag{4}
\]

恢复原共同包络只添L^C。此估计不要求n在K，也不使用[Rθ]
或任何DirichletL全族RH。在非平衡q/S上，它比旧TT*的
√(qX/S)更准；下节明确它本身未支付完整K。

## 3. 高矩/不同L^p不能免费替代新的G分布

在一个真实box中，令A=Q²X/S，把未出现的(q,n)位置置零。
对该有限counting集合定义D_p(F)=A^(-1/p)(Σ|F|^p)^(1/p)。
真实b_q≪Q^(-1/2)，因此原signed functional的absolute上界为

\[
 C_\phi\sqrt Q\,D_p(F)D_{p'}(G)L^C,\qquad 1/p+1/p'=1.
 \tag{5}
\]

mod q Parseval及J_q重复次数给D_2(F)≪L^C；
完整mod q²正能量给D_2(G)≪√(QS/X)L^C。
(4)给D_∞(G)≪√X L^C。所有端点/q-related区间直接保留；
这些是每组共同参数的真估计，并非假设参数独立。

若p≤2、r=p'≥2，F用powermean，G用2/∞插值，费用恰为
原CS费用Q√(S/X)再乘

\[
 \left(\frac{X^2}{QS}\right)^{1/2-1/r}\ge1.
 \tag{6}
\]

若p≥2、r≤2，即使额外给出理想flat高矩D_p(F)≪L^C，
现有G的powermean也仍只回到原CS费用。
所以提升F高矩而不给G低p分布或真实joint输入，不跨过门槛。
这是一条已知norm输入的费用结论，不是实际prime-product下界。

更具体，若

\[
 D_4(F)\ll X^{h_4/4}L^C,\qquad
 \sum_K|G|^{4/3}\ll
      A(QS/X)^{2/3}X^{-t}L^C,
 \tag{7}
\]

则费用指数为γ+h4/4−3t/4，其中γ=u+w/2−1/2，
Q=X^u、S=X^w。这一真实L4/L^(4/3)输入跨过5/7的条件为
3t−h4>4γ−20/7。理想h4=0时，在高产品域最容易处也须
t>179/2100−O(1/L)，balanced处须t>8/21。
这些门槛比单独“F高矩好”明确；本稿没有证明(7)的新t。

两类已删有理弧也不能在Hölder里免费节省样本总数。
每个mod q period内，旧弧删除点数≤C(qW²/S+W²)，
新弧≤CB²(q/S+1)。因为q>S，合计≤CqB²/S=o(q)。
此计算含每个interval的整数+1并允许全部overlaps上界。
实际共同J_q长度≍qX/S≳q，其period重复只将删除比例放大固定倍数。
这说明准确K仍有该频带的绝大多数整数点；不声称其F能量下界。

## 4. 至多两个共同端period的真实付款

固定0<η<1/100，令Z2=X^(12/7−η)。真实产品先分成
Z<qs≤Z2和qs>Z2；前者每个q的S_q是原dyadic prime interval与
Z/q<s≤Z2/q、s<q、interior阈值的交集，仍与n无关。
不在individual s的原频带上另选端点。

在共同整数J_q=[l_q,h_q]中使用固定mod q网格

\[
 I_j=(jq,(j+1)q]\cap\mathbb Z,\qquad
 j_0=\left\lceil\frac{l_q-1}{q}\right\rceil,\quad
 j_1=\left\lfloor\frac{h_q}{q}\right\rfloor-1.
 \tag{8}
\]

完整period为j0≤j≤j1的I_j（j0>j1时为空）。
定义E_(q,S)=J_q减去这些完整period；它由至多两个
长度<q的端interval组成。因此每个residue mod q在E最多出现2次，
包括端点floor、ceil、空period情形，无需免费删除+1。
新付款严格取原K mask与E的交，再保留真实Z<qs≤Z2。

固定共同λ，F严格mod q周期，真实s<q没有residue aliases。
一整period的Parseval为qΣ_(s∈S_q)|b_s(s/S)|²≪qL^C。
因此完整端族的加权F能量为

\[
 E_{F,\rm edge}=\sum_qb_q^2\sum_{n\in E_{q,S}\cap K}|F_{q,n}|^2
       \ll\sum_qb_q^2q\,L^C\ll QL^C.
 \tag{9}
\]

G系数合并到k=pr，每个k至多两个ordered genuine-prime factor pairs，
实际p,r<q保证0<k<q²、没有mod q² aliases，系数l2≪L^C。J_q⊂(0,q²)允许在非负平方和
中放大到一个完整q² period，给

\[
 E_{G,\rm edge}\ll Q^3L^C.
 \tag{10}
\]

共同前因子和Cauchy直接给

\[
 |\mathfrak E_{\eta,Q,S,P,R}^{\rm unmasked}|
       \ll \frac S{QX}\sqrt{Q}\sqrt{Q^3}L^C
       =\frac{QS}{X}L^C.
 \tag{11}
\]

真实Z<qs≤Z2的非空box有QS<qs≤Z2，故所有boxes、
最大标签四位置和同一个u恢复，仅添L^C，得到Z2/X。
相对原E_F≤QX/S，这里真的节省S/X；f=1−w、g=0。
u+w≤12/7−η+O(1/L)严格满足f+g>2u+w−17/7，
余量至少2η−O(1/L)。这只对完整端period族成立。

## 5. s排除、actual signed范围与新的准确剩余

原p,r≠s不能在(11)免费删掉。对这个准确(q,n,S)端mask和
真实s产品cap，直接重做minor464第6节的非负能量：
p=s的真实phase为e_(q²)(n s(q−r))。只分离ν，其余同-u
profile和g(r/q)留在n无关系数中。h=s(q−r)严格在(0,q²)；
每个h≤X²最多3个prime s>√X，各s唯一恢复r。
两个原b_s合并后Σ_h|c_(q,h)|²≪1/S。全部q² Parseval给
Q³/S；另一外因子Σ_qb_q²|J_q|≪QX/S，原prefactor付Q/√X。
r=s对称。双点p=r=s的h=s(q−s)最多二对一，能量更小。
产品上下cap及端mask只限制该非负upper的项，故所有修正
完整付O(√X L^C)，不是从signed全minor上界限制出子集上界。

因5/7−η>493/700>1/2，(11)和修正严格给

\[
 \boxed{|\mathfrak E_\eta|\ll_\phi X^{5/7-\eta}L^C,
            \qquad 0<\eta<1/100\ {\rm fixed}.}
 \tag{12}
\]

以原tuple和共同频率mask定义K_new=K−E_η，精确分区：
qs>Z2仍保留全部K频率；Z<qs≤Z2只保留共同J_q的完整period。
沿489已有整块付款而不是重切旧signed误差，有

\[
 \mathfrak L_U=\mathfrak K_{\rm new}
  +O(X^{493/700}L^C)+O(X^{7/10}L^C)
  +O(X^{5/7-\eta}L^C).
 \tag{13}
\]

所有旧physical/nn/graph/chirp/aliases/carry误差保持原整体付款范围。
本稿仅在已准入K对象中新增真正端族估计，未声称对原raw
individual频率可重新插入g或局部化那些旧signed误差。

## 6. 完整period的coherent H接口

在(8)完整period内写n=a+qj，1≤a≤q，j0≤j≤j1。
K只依赖a；q|n的a=q本来已被旧弧排除。F_(q,n)=F_q(a)。
把原固定共同参数后的外模长1因子准确记为ε_(q,n)(λ)，定义

\[
 H_q(a;\lambda)=\sum_{j=j_0}^{j_1}
      \varepsilon_{q,a+qj}(\lambda)G_{q,a+qj}(\lambda).
 \tag{14}
\]

这是实际j方向signed和，包含n^(it)及全部同一外参数；
不能删掉它或为各j另选twist。完整period端点j0,j1与a无关。
F残类能量Σ_qb_q²Σ_(a modq)|F_q(a)|²≪Q L^C，
所以完整period主项若有真正输入

\[
 \sum_q\sum_{a\in K_q}|H_q(a;\lambda)|^2
       \ll (X/S)Q^3X^{-h}L^C
 \tag{15}
\]

且参数常数uniform或在原包络中可积，就付到
Q√(S/X)X^(-h/2)L^C。门槛恰为h>2u+w−17/7。
不要求独立每n的G能量达到旧Q²X/S强目标。
普通j-Cauchy只给h=0；本稿没有把coherent signed和当成已付款。
更高产品的两个端period仍是(13)准确剩余的一部分，(15)单独
不控制它们，也不自动控制整个K_new。

本轮新估计为(4)与(12)，新未付接口为(7)、(15)。
全论证不使用普通ζ无零假设或新角色族输入；无有限采样、
无常数级预算、无新whole/比例/κ/strip，尚不能发布纪录论文。
