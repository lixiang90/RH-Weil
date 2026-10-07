# 高素数 opposite 重复四词的原有限压缩小量

2026-10-07。作者：`twisted_research`。本报告只新增这一推导，不改冻结的
high 报告、其他正文、论文、脚本、math、Goal或Git。结论是原 finite
matrix 的

\[
 T_{\rm opp,H}=\sum_{\sqrt X<p\le X}
       \operatorname{Tr}(C_pC_HC_pC_H)=O_{\chi,\psi}(d/L)=o(d),
 \quad L=\log X,\quad d=\lfloor XL\rfloor.
 \tag{1}
\]

它把已经支付的 high repeated sector 从旧上界4S_psi改为实际极限
2S_psi；flat窗为19/240。证明保留所有 internal P、原carrier、真实
zero-extended translations及C²taper，不假定完整Tr C_H⁴有界，不用
零自由包[R]。四个不同high primes和mixed distinct sectors仍未支付。

## 1. 原始对象与已付二矩输入

固定
[AF v2 §2](https://arxiv.org/html/2608.13637v2#S2)的原窗和采样，采用
[冻结high推导](hybrid-high-prime-four-word-response-research.md)§1–4的
确切约定及已付有限二矩。设X=T/(2pi)、I=[−L/2,L/2]、tau_k=T+2pi k/L，
0≤k<d，

\[
 Ee_k(u)=L^{-1/2}\mathbf1_I(u)e^{i\tau_ku},\quad
 P=EE^*,\quad Q=1-P,
 \quad a_L=L^{-1}\|\phi\|_2^2.
 \tag{2}
\]

phi为原偶、非负C²taper，0≤phi≤1，a_L有上下固定正界。
R_s f(u)=f(u+s)，先在R上零延拓；以下不是周期物理平移。对high prime
sqrt X<p≤X，写

\[
 b_p=\frac{\log p}{a_LL\sqrt p},\quad
 B_p=-b_pM_\phi(R_{\log p}+R_{-\log p})M_\phi,
 \quad Y=B_H=\sum_pB_p,\quad C_p=E^*B_pE,\quad C_H=E^*YE.
 \tag{3}
\]

它确切是原(2pi/(a_L L))F* M_high F、F=mathscrF M_phi E；negative
sign在四次乘积中抵消。令ell_0=log(2+L)。已付输入为

\[
 \sum_pb_p^2=O(1),\quad \sum_pb_p\ll\sqrt X/L,
 \quad \|B_p\|\le b_p,\quad y:=\|Y\|\ll\sqrt X/L,
 \tag{4}
\]
\[
 l_p:=\|QB_pP\|_2\ll b_p\sqrt{\ell_0},\quad
 l_Y:=\|QYP\|_2\ll\sqrt{X\ell_0}/L,
 \quad Y_2:=\|YP\|_2=O(\sqrt d).
 \tag{5}
\]

第一组是Chebyshev–Mertens和high shifts的支撑性质；crossing bound来自
真实periodic系数 min(1,1/|n|,L/n²)的有限mode计数。最后的Y_2是
冻结high§4在原有限几何核上付清的二矩，含Montgomery–Vaughan输入，
不是从未知四矩倒推。这里||.||_2是Hilbert–Schmidt norm。

## 2. 三个 internal P 的独立删除证明

置A=B_p，a=||A||，l_A=||QAP||_2。有限矩阵迹等于
Tr(PAPYPAPYP)。从左到右删去三个internal P，相差项依次为

\[
 \operatorname{Tr}(PAQYPAPYP),\quad
 \operatorname{Tr}(PAYQAPYP),\quad
 \operatorname{Tr}(PAYAQYP).
 \tag{6}
\]

前两项绝对值均≤a y Y_2 l_A：分别配对PAQ与YPAPYP，以及QAP与YPAYQ。
第三项配对QYP与PAYAQ；把PAYAQ=PAPYAQ+PAQYAQ，得到
||PAYAQ||_2≤a²Y_2+a y l_A。所有末端P及Q都保留，所用迹为两个HS
因子的合法配对。于是

\[
 \left|T_{\rm opp,H}-\sum_p\operatorname{Tr}(PB_pYB_pYP)\right|
 \ll yY_2\sqrt{\ell_0}+Y_2l_Y+y l_Y\sqrt{\ell_0}
 \ll X\sqrt{\ell_0/L}+X\ell_0/L^2.
 \tag{7}
\]

这里聚合的是sum a_p²和sum a_p l_p，分别为O(1)、O(sqrt ell_0)。
不是对四个独立标签使用(sum b_p)^4，也没有假定prime泄漏正交。
(7)除以d为O(sqrt ell_0/L^(3/2)+ell_0/L³)，故为o(1)。

## 3. 真实交替路径与比端点alias更强的空路径事实

原有限carrier核为

\[
 K_d(s)=d^{-1}\sum_{k=0}^{d-1}e^{i\tau_ks}
 =e^{i[T+(d-1)\pi/L]s}
     \frac{\sin(d\pi s/L)}{d\sin(\pi s/L)}.
 \tag{8}
\]

对(p,q,p,r)物理词，设s_j为各signed log prime，S_j=sum_(i≤j)s_i，
S_0=0。其准确trace/d为b_p²b_qb_r sum_sign K_d(S_4)<W>，其中

\[
 W(u)=\phi(u)\phi(u+S_4)\prod_{j=1}^3\phi(u+S_j)^2,
 \qquad \langle W\rangle=L^{-1}\int_IW(u)\,du.
 \tag{9}
\]

五个位置必须同时落在长度L的I内。每一步high log>L/2，相邻同号
使某两位置距离>L，故16个patterns只剩+−+−及−+−+。
对+−+−，令a=log p、b=log q、c=log r，则

\[
 (S_0,S_1,S_2,S_3,S_4)=(0,a,a-b,2a-b,2a-b-c),\quad
 S:=S_4=\log(p^2/(qr)).
 \tag{10}
\]

若S≥L/2，则S_3=S+c>L；若S≤−L/2，则S_1−S=a−S>L。
两者都使路径为空。另一pattern反射相同。因此每个非零物理词均有
**|S|<L/2**，不存在靠近±L的finite-grid alias。并且span≥a，因为
第0、1两个位置相距a，所以实际共同重叠满足

\[
 0\le\langle W\rangle\le\frac{(L-a)_+}{L}
   =\frac{\log(X/p)}L.
 \tag{11}
\]

这也是原端点重叠界的直接加强，保留taper后仍成立。对非零S，(8)
和d≈XL给|K_d(S)|≤min(1,C/(X|S|))；carrier始终是(8)中的单位相位。

## 4. 远ratio、exact diagonal和近ratio系数

当|S|≥log2，非零支撑仍有|S|<L/2，故|K_d(S)|≪1/X。不用相位
cancellation，全部远区normalized费用为

\[
 \frac C X\sum_pb_p^2\left(\sum_qb_q\right)^2=O(L^{-2}).
 \tag{12}
\]

这包含全部远区，不只涵盖已接近的composite ratios。若路径为空，
准确为0；不在空路径外对Kd套错误的无alias界。

exact S=0即p²=qr。三个标签都是primes时只可能p=q=r，因此它是
全相同diagonal，normalized费用≤2sum b_p⁴=O(L^-4)。这里只用
sum_(prime p)(log p)^4/p²<∞及a_L下界，未改成任意整数diagonal。

近区0<|S|<log2中qr∼p²，b_p²b_qb_r≪1/p²。置Delta=p²−qr≠0，
则|S|≳|Delta|/p²。因此

\[
 b_p^2b_qb_r|K_d(S)|\langle W\rangle
 \ll\frac{\log(X/p)}{XL|p^2-qr|}.
 \tag{13}
\]

即使p²/(X|Delta|)>1，使用这个上界仍合法，只是较弱；不需假定原
finite核已经处在其非平凡decay分支。

## 5. 最小prime因子及零剩余的完整整数计数

交换dummy q,r至多损失2，取ell=min(q,r)、t=max(q,r)。近区给
ell≤sqrt2 p和ell≥p²/(2X)，并仍有sqrt X<ell≤t≤X。
分p∈(P,2P]、ell∈[Q,2Q)，其中Q从sqrt X起点倍增（最后一格可截断），于是

\[
 Q\le2\sqrt2 P,\qquad Q\ge\sqrt X,\qquad Q\ge P^2/(4X).
 \tag{14}
\]

为上界可把p和t放宽成相应整数，但ell仍保留为prime。这是唯一用到
quadratic residue两根计数的变量，不能把ell也放宽成合数后仍用两根。
固定ell∼Q，写p²=ell k+r_p，0≤r_p<ell。若r_p≠0，记
delta_ell(p)=min(r_p,ell−r_p)。直接对integer t≤X求harmonic sum给

\[
 \sum_{1\le t\le X}\frac1{|p^2-\ell t|}
 \ll\delta_\ell(p)^{-1}+L/\ell.
 \tag{15}
\]

所有相关非零差值都≤2X²，因此所用harmonic长度只费O(L)。每个
nonzero residue r∈F_ell的p²≡r最多两个根；每个root class在长P的
interval内出现≤P/ell+1次。于是

\[
 \sum_{P<p\le2P,\ \ell\nmid p}\delta_\ell(p)^{-1}
 \ll(P/\ell+1)\sum_{r=1}^{\ell-1}\frac1{\min(r,\ell-r)}
 \ll(P/\ell+1)L.
 \tag{16}
\]

零剩余也没有丢弃：当ell|p时，在删除Delta=0的exact t后，其余差
为ell的非零倍数，(15)相应变为O(L/ell)。这样的integer p有
O(P/ell+1)个。它们的总量仍被O((P/ell+1)L)控制。这包含原prime
exception p=ell；其exact diagonal已在§4单独保留。因此

\[
 \sum_{P<p\le2P}\ \sum_{1\le t\le X,\ p^2\ne\ell t}
          \frac1{|p^2-\ell t|}\ll(P/\ell+1)L.
 \tag{17}
\]

Chebyshev给ell∼Q的prime数O(Q/log Q)=O(Q/L)，因为Q≥sqrt X。
由Q≤2sqrt2 P，(17)逐block聚合不超过

\[
 \sum_{\ell\ {\rm prime}\sim Q}\sum_{p\sim P,t\le X,\Delta\ne0}
             |\Delta|^{-1}\ll(P+Q)=O(P).
 \tag{18}
\]

对于固定P，允许Q从max(sqrt X,P²/(4X))到2sqrt2 P，dyadic Q数
至多C(1+log(X/P))。这个上界利用min-factor，同时控制根计数里的
“+1”，不能用min-factor条件之前的独立L个Q-blocks粗账本。

## 6. 原端点重叠使全部近区为O(1/L)

取P_j=X/2^(j+1)，p∈(P_j,2P_j]，到sqrt X处截断最后一个block。
令M_j=log(X/P_j)=(j+1)log2。log(X/p)≤M_j，(13)、(18)给

\[
 \frac1d|T_{\rm near,offdiag}^{\rm physical}|
 \ll\frac1{XL}\sum_jP_jM_j(1+M_j)
 \ll\frac1L\sum_{j\ge0}2^{-j}(j+1)^2=O(L^{-1}).
 \tag{19}
\]

这是针对每个real X的统一有限求和；没有假定sqrt X或X与primes有
固定间距，也没有用素数对PNT、GRH、dispersion或未付矩估计。
所有terms先保持actual support再majorize；(11)来自真实支撑，并非
在高p尾任意添加的权重。没有只估近区而省略(12)的完整远区。

由(7)、(12)、diagonal和(19)，更明确有

\[
 \frac{|T_{\rm opp,H}|}{d}
 \ll_{\chi,\psi}L^{-1}+L^{-2}+L^{-4}
       +\frac{\sqrt{\log(2+L)}}{L^{3/2}}
       +\frac{\log(2+L)}{L^3}=O(L^{-1}).
 \tag{20}
\]

固定窗/taper后常数固定，对所有充分大X成立。这里只需既付二矩，
没有以full high fourth boundedness为输入。

## 7. 对既有重复partition的确切影响

冻结high报告§7的有限inclusion–exclusion为
S_rep=4T_0+2T_opp−2T_22−T_times−8T_3+6T_4。它已经分别证明
T_0/d、T_22/d→S_psi，T_times/d、T_3/d、T_4/d→0。本报告支付
T_opp/d→0，因此原实际有符号重复union有极限

\[
 S_{\rm rep,H}/d\longrightarrow2S_\psi,
 \quad S_\psi=\int_{-1/2}^{1/2}d_\psi(v)^2\,dv,
 \quad d_\psi(v)=\frac{\psi(v)}{a_\psi^2}
       \int_{1/2}^{1/2+|v|}r\psi(r-|v|)\,dr.
 \tag{21}
\]

flat d_psi(v)=(|v|+v²)/2，S_psi=19/480，所以2S_psi=19/240。
这是实际sector等式极限，比旧19/120的upper少一半；不是将一个
one-sided scalar upper误作实际四矩。MT同样从旧4S_MT改为2S_MT。
用d/N(T,2T)→1可转成相同N尺度，仍只是在重复sector的范围内。

尚未支付的原finite all-distinct high、13/31 mixed distinct、22 mixed
distinct及完整Hermitian背景混合不能由此相加成全四矩常数；(1)和
(21)没有推出新临界线比例或新无零边界。

状态：完整有限路径/投影/整数计数推导保存，待根节点及另一次独审。
