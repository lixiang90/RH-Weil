# 原完整周期：真实外twist下的 Q³ coherent 正能量

2026-10-08，checkpoint_audit。研究轮2，基线 main 62469c0。
只新增本源，不修改冻结来源、输出、检查器或Git。
状态：完整结构证明，待root与不同作者全文审查。

本稿证明真实完整mod q周期的coherent H正能量为Q³乘polylog，
含原ν Mellin外twist。原接口的节省参数为h=1−w，S=X^w。
消费费用仍为QS/X；这没有超出464既有任意Z产品cap的已付方面比。
没有新的整个高产品预算、whole幂、中心常数四矩、比例或无零边界。

## 1. FULL READ输入与准确对象

本轮重新全文读下列四源，hash仅CRLF/lone CR转LF，不trim：

| 输入 | 行数 | canonical LF SHA256 |
| --- | --- | --- |
| [共同period与edge](hybrid-original-high-product-minor-edge-and-coherent-period-research-checkpoint-audit.md) | 285 | 85bd0985a63b56941be5a216111a53f95ec0494fbd08a29cbdf8ac8f20ed93e0 |
| [primitive准确变换](hybrid-original-unit-band-primitive-reciprocal-transform-research-root.md) | 188 | 4b13bec23ff399739b26003954a28e0d9d889617955bf6e7a43e428ab3a7aa2c |
| [actual unit](hybrid-whole-fourth-unit-unit-actual-research-whole.md) | 425 | b3f14cf4ee5659f8e23bd51dc9bf71e853e783bd2d55e42ee8846d6e8d1e41dc |
| [新rational slice](hybrid-original-high-product-minor-rational-slice-research-high-product.md) | 337 | 56219e9f136c0f0666c5b1ce028ec4d7d93ad33f5ebd43d5e4a5e34c399677a8 |

464既有完整cap付款沿其已准入证明使用；本稿不把该结论重新认领为新进展。
保持X=T/(2π)、L=logX、b_p=log p/(a_LL√p)、a_L≥c_φ>0。
q为真正最大genuine prime，全部s,p,r在(√X,X]，s,p,r<q。
固定原Q,S,P,R dyads，PR≍QS、P,R≲Q、q≍Q。
当前实际高产品域qs>Z=X^(1193/700)，故PR/q≍S≫1。
共同u、两套原C² profiles、g、ν、正height和floors均保留。

先以ν零支撑恢复共同J_q=[l_q,h_q]⊂(0,q²)，|J_q|≲qX/S。
完整period采用I_j=(jq,(j+1)q]，
j0=ceil((l_q−1)/q)、j1=floor(h_q/q)−1；空区间给零。
两个不完整端period另保留，不在individual s的旧频带上另选端点。
M=X/S≥1；所有完整period的j+a/q均在[cM,CM]，1≤a≤q。
因此period数O(M+1)=O(M)，也至多q；小M仍包括全部整数+1。

## 2. 真实系数、product quotient与geometric窗

沿337共同参数分离ν、g和原profiles。固定公共参数λ，写
\[
 F_q(a)=\sum_{s\in\mathcal S_q}u_s e_q(as),\qquad
 G_q(n)=\sum_{p,r<q}v_pz_r e_{q^2}(-npr).
 \tag{1}
\]
u_s含b_s(s/S)和原固定twists，v_p,z_r含b_p,b_r及固定twists。
这些系数可依赖q的实际sharp prefix，不能依赖a或j私下改变。
真实s集是与q阈值和产品上下cap相交的prime interval，与n无关。
先保留p=s或r=s，第6节完整支付准确修正。

合并k=pr，令C_{q,k}=Σ_(pr=k)v_pz_r。
genuine-prime有序factor pairs每个k至多2个，包括p=r仅1个。
因log p/L≤1、a_L≥c_φ，严格有
\[
 |C_{q,k}|\le C_\phi(PR)^{-1/2},\qquad 0<k<q^2.
 \tag{2}
\]
所有模长1的共同twists不增加这个幅度；没有丢弃真实prime mask。
写唯一k=qz+v，0≤z,v≤q−1。
k在原产品dyad(PR,4PR]中，故非空z数至多C(PR/q+1)。
这保留了整数+1；PR/q≍S≫1最终才将它吸收。

任一共同j-prefix I⊂[j0,j1]，令
\[
 D_I(v)=\sum_{j\in I}e_q(-jv),\qquad 0\le v<q.
 \tag{3}
\]
prefix包括空、单点和整个区间，长度≤q。
geometric和给v≠0时|D_I(v)|≤min(|I|,(2||v/q||)^(-1))，
v=0付|I|≤q。因此全族harmonic和严格为
\[
 \sum_{v=0}^{q-1}|D_I(v)|\ll q\log(2q),
 \tag{4}
\]
对所有prefix统一。实际q∤pr使C_{q,qz}=0，但(4)仍明确支付v=0。

## 3. slow相位准确Taylor与逐阶Parseval

先去掉第4节将恢复的ν外twist，定义
\[
 H_I^0(a)=\sum_{j\in I}G_q(a+qj)
 =\sum_{z,v}C_{q,qz+v}D_I(v)e_q(-az)e(-av/q^2).
 \tag{5}
\]
slow因子不是1。对所有1≤a≤q、0≤v<q准确展开
\[
 e(-av/q^2)=\sum_{h=0}^{\infty}
       \frac{(-2\pi i)^h}{h!}(a/q)^h(v/q)^h.
 \tag{6}
\]
它在该紧域绝对一致收敛。置
B_{z,h}=Σ_v C_{q,qz+v}D_I(v)(v/q)^h。
因(v/q)^h≤1，(2)–(4)给每h统一的
\[
 \sum_z|B_{z,h}|^2
 \ll_\phi(PR/q+1)\frac{q^2}{PR}\log^2(2q).
 \tag{7}
\]
这里每个B_{z,h}与a无关；slow因子的a依赖只在外面的(a/q)^h。
后者在a的l2上是收缩。z∈[0,q−1]没有aliases，所以完整mod q Parseval给
\[
 \sum_{a=1}^q\left|\sum_z B_{z,h}e_q(-az)\right|^2
       =q\sum_z|B_{z,h}|^2.
 \tag{8}
\]
先逐h取l2 norm，再用Minkowski；全部Taylor系数的absolute和仅e^(2π)。
故包括+1的准确界为
\[
 \|H_I^0\|_{l^2(a)}^2
 \ll_\phi q^2(1+q/(PR))\log^2(2q)
 \ll_\phi q^2\log^2(2q).
 \tag{9}
\]
这不是把private a-coefficients塞进Parseval，也不截Taylor阶数。
它使用实际prime-product幅度与产品区间，未消费角色大筛或新外部定理。

## 4. variable-a vector Abel恢复原n外twist

ν分离后的原外因子为(n/(qX))^(itν)，另外的q,u公共因子不依赖a,j。
因此准确权为w_j(a)=((j+a/q)/X)^(itν)，模长1。
大M时在全部真实完整period上j+a/q≍M。相邻j的差满足
sup_a|w_(j+1)(a)−w_j(a)|≤C|tν|/M，全部j总variation≤C|tν|。
M有界时只有O(1)个完整period，逐single-j应用(9)再triangle。
每个w_j(a)只是模长1的diagonal，不需以j=0作导数分母；空period仍给零。

对a向量的部分和H_I^0作准确Abel；权是a上的对角乘法算子。
每个prefix都由(9)统一控制，其operator norm增量取sup_a。
不用对各a另选最大prefix，然后交换最大值与积分。
于是保留原全部twist的H_q为
\[
 H_q(a;\lambda)=\sum_{j=j0}^{j1}w_j(a)G_q(a+qj;\lambda),\qquad
 \sum_a|H_q(a;\lambda)|^2
 \ll_\phi(1+|t_\nu|)^2q^2\log^2(2q).
 \tag{10}
\]
式中tν表示同一个ν Mellin参数；没有删除n^(itν)或逐j改选twist。
任意固定mod q residue maskΩ_q(a)只使这个非负平方和减小。
它允许当前两套rational complement，也允许q相关mask；
该mask仍必须与individual s无关。

## 5. ν weighted moments、F配对和准确费用

V(y)=Xν(2πXy)在固定正紧区间支撑。actual425(13)对任意固定m合法。
置h(u)=V(e^u)，则∥h^(m)∥1≲L^(m/2)，且由ν正概率归一化有∥h∥1≲1。
准确Mellin规范为Mν(t)=(2π)^(-1)∫h(u)e^(−itu)du、V(y)=∫Mν(t)y^(it)dt。
分部积分给|Mν(t)|≲min(1,L^(m/2)|t|^(−m))。
以√L分界，取m=3支付weighted1为O(L)，取m=4支付weighted2为O(L^(3/2))：
∫(1+|tν|)^2|Mν(tν)|dtν≲L^(3/2)。
φ没有被升级光滑性；其参数仍只需原C² Fourier绝对L1包络。
其它p,r,s twists在(2),(9)中uniform，所以没有要求这些参数额外moments。
共同参数积分可支付(10)的明确tν增长，而非声称其常数对tν一致。

q族至多O(Q)个actual primes，故固定参数的能量为
\[
 E_H(\lambda):=\sum_q\sum_{a\in\Omega_q}|H_q(a;\lambda)|^2
 \ll_\phi(1+|t_\nu|)^2Q^3L^2.
 \tag{11}
\]
按原正包络消费或作加权平方积分后，右边为Q³L^C。
另一方面s<q的真实residues无aliases，|u_s|≤C/√S，故
由mod q Parseval，Σ_q b_q²Σ_(a modq)|F_q(a)|²≪Q L^C。
原prefactorS/(QX)和同一q,a Cauchy给完整period主项费用
\[
 \frac S{QX}\sqrt Q\sqrt{Q^3}\,L^C=\frac{QS}{X}L^C.
 \tag{12}
\]
原Q/q固定因子、同一u积分、全部profiles和四种最大标签位置只添L^C。
285的旧接口基线是(X/S)Q³，故(11)准确给h=1−w，而非仅h=0。

## 6. edge、s排除与完整范围

共同J_q的两个不完整端period中，每个mod q residue至多出现2次。
因此weighted F能量≤Q L^C；真实k<q²、至多2pairs的完整q² Parseval
给G能量≤Q³L^C。该整个edge族对同一Ω mask也付QS/X。
所以本稿的fullperiod与edge可精确合并为整个共同J_q频率族。

原p,r≠s以减两单点加双点恢复。对准确Ω及period/edge mask，
只分离ν，其余same-u profile与g(r/q)保留为bounded、n无关系数。
p=s时h=s(q−r)∈(0,q²)，每h≤X²至多3个prime s>√X因子，
各s唯一恢复r；两个原b_s合并，系数l2²≤C/S。
完整q² Parseval给Q³/S，另一正因子Σ_qb_q²|J_q|≤CQX/S。
原prefactor遂付Q/√X；r=s同理，双点h=s(q−s)至多二对一且费用更小。
这些是直接对本真实mask的positive upper，不从signed全块限制子族。
S≳√X使box修正≤CQS/X；全union另记O(√X L^C)。

本稿允许原qs上下cap，保留真实s interval、commonJ_q及全部q-prefix。
得到的是actual χ-carrier signed主频带预算，不是canonical M_PH的任意子块。
在Q=X^u、S=X^w上，整个box费用指数u+w−1；严格跨过5/7仍需u+w<12/7。
顶端Q,S≈X仍退化至X，所有高产品方面比并未支付。
完整period的新正能量结构较原j-Cauchy节省X/S，但whole费用回到既有cap。
无额外有限检查器；未使用[Rθ]、Dirichlet-L全族前件或generic聚簇反例。
真实prime/spectral covariance的进一步省幂仍待证明。
