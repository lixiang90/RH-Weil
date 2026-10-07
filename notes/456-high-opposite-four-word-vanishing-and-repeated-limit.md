# 456：高素数 opposite repeated 四词消失与实际重复主项

2026-10-07。推导完成，两份独立全文审查未发现数学阻断。没有新比例或无零边界。
本稿在原有限 AF frame 中证明

\[
 T_{\rm opp}=\sum_{p>\sqrt X}\operatorname{Tr}(C_pC_HC_pC_H)=o(N).
 \tag{1}
\]

结合既有 exact partition 与已付主项，高素数的整个 repeated sector
因而有实际极限，而不是仅有一侧上界：

\[
 \frac{S_{\rm rep,H}}N\longrightarrow2S_\psi,
 \qquad S_\psi=\int_{-1/2}^{1/2}d_{H,\psi}(v)^2\,dv.
 \tag{2}
\]

flat profile 的值为19/240；旧19/120是该子族的一侧上界。
这不包含 high四distinct、低素数mixed或整个响应的fourth预算，
不能直接改变简单临界线零点比例。

## 1. 原对象与已经支付的输入

沿用已提交的
[高素数报告](../reviews/2026-10-07/hybrid-high-prime-four-word-response-research.md)
及[高低重复四词](../reviews/2026-10-07/hybrid-low-high-mixed-four-word-research.md)。
原frame来自[AF v2 §2](https://arxiv.org/html/2608.13637v2#S2)。
取X=T/(2pi)、L=logX、d=floor(XL)、N=N(T,2T)∼d、I=[−L/2,L/2]，
原carrier tau_k=T+2pi k/L。保留原fixed taper phi及a_L=||phi||²/L。

\[
 E e_k=L^{-1/2}1_Ie^{i\tau_k u},\quad P=EE^*,\quad Q=1-P,
 \quad b_p=\frac{\log p}{a_LL\sqrt p},\quad \ell_p=\log p,
\]
\[
 B_p=-b_pM_\phi(R_{\ell_p}+R_{-\ell_p})M_\phi,
 \quad B=\sum_{\sqrt X<p\le X}B_p,
 \quad C_p=E^*B_pE,\quad C_H=E^*BE.
 \tag{3}
\]

所有shifts是物理zero-extended平移，未换成周期平移。原C²窗满足
0≤phi≤1；Fourier crossing只用于计算这个P，保留精确floor d。
记ell0=log(2+L)。既有全文验收的bounds为

\[
 \sum_p b_p^2=O(1),\quad \sum_p b_p\ll\sqrt X/L,\quad
 \|B_p\|\le b_p,\quad y:=\|B\|\ll\sqrt X/L,
\]
\[
 l_p:=\|QB_pP\|_2\ll b_p\sqrt{\ell_0},\quad
 l_Y:=\|QBP\|_2\ll\sqrt{X\ell_0}/L,\quad
 Y_2:=\|BP\|_2=O(\sqrt d).
 \tag{4}
\]

最后一个bound来自原finite carrier上的weighted二矩，绝不预设CH4有界。
以下新算术仅用Chebyshev、有限几何核和素数模数的平方剩余至多两根。

## 2. 三个内部P的重复指标聚合付款

与原actual Topp比较的physical量是

\[
 T_{\rm phy}=\sum_p\operatorname{Tr}(E^*B_pBB_pBE).
 \tag{5}
\]

physical trace不预先认作实数或正数。高低重复四词§5的P删除引理，
取A_i=B_p、Y=B，逐个删三个internal P，单项费用分别为

\[
 b_p^2Y_2l_Y,\qquad b_pyY_2l_p,\qquad
 l_Y(b_p^2Y_2+b_pyl_p).
 \tag{6}
\]

第三项使用准确的right-projection分解BA_iP=BP A_iP+BQ A_iP，
所以||BA_iP||₂≤b_pY₂+yl_p。按(4)聚合，得到

\[
 |T_{\rm opp}-T_{\rm phy}|
 \ll Y_2l_Y+yY_2\sqrt{\ell_0}+yl_Y\sqrt{\ell_0}
 \ll X\sqrt{\ell_0/L}+X\ell_0/L^2=o(d).
 \tag{7}
\]

重复p的平方可求和，故无需逐对q,r用其l1质量付款。本引理不能推广
到四distinct的全部词。这一步已把真正finite compression误差单独付清。

## 3. 全部physical高四步、carrier与endpoint

对word(p,q,p,r)，记s_i=epsilon_i log p_i、S_j=sum_(i≤j)s_i、S0=0。
准确finite-k求和给

\[
 \frac1d\operatorname{Tr}(E^*B_pB_qB_pB_rE)
 =b_p^2b_qb_r\sum_{\epsilon\in\{\pm1\}^4}
 K_d(S_4)\langle W_\epsilon\rangle,
\]
\[
 K_d(s)=\frac1d\sum_{k=0}^{d-1}e^{i\tau_k s},\qquad
 W_\epsilon(u)=\phi(u)\phi(u+S_4)\prod_{j=1}^3\phi(u+S_j)^2,
 \quad\langle W\rangle=L^{-1}\int_IW.
 \tag{8}
\]

每一步长度>L/2，所以相邻同号使支撑为空。只有两个alternating
patterns可能非零。取+−+−，置a=logp、b=logq、c=logr，五个位置为

\[
 0,\ a,\ a-b,\ 2a-b,\ S=2a-b-c.
 \tag{9}
\]

若S≥L/2，S3=S+c>L；若S≤−L/2，S1−S=a−S>L。故非零physical
词严格有|S|<L/2，另一pattern同理。原grid alias没有被忽略，而是由
实际五点支撑排除。因此对S≠0，原finite几何核直接有

\[
 |K_d(S)|\ll\min\{1,L/(d|S|)\}\ll1/(X|S|).
 \tag{10}
\]

carrier相位保留在Kd；此处仅对其取合法绝对上界。更重要的是，位置
0与a必须同时在I，给共同endpoint权重

\[
 0\le\langle W_\epsilon\rangle\le\frac{L-a}{L}
 =\frac{\log(X/p)}L.
 \tag{11}
\]

后续按dummy q,r交换大小，只对共同正majorant排序，不交换operator
或进行未经付款的physical cyclic rotation。

## 4. diagonal与far ratio

S=0即p²=qr。全部指标为genuine primes，唯一分解强制q=r=p。
该部分normalized绝对值≤2sum_p b_p⁴=O(L^-4)。

若p²/(qr)不在[1/2,2]，则|S|≥log2。由(10)与W≤1，far全部费用为

\[
 \ll\frac1X\sum_pb_p^2\left(\sum_qb_q\right)^2\ll L^{-2}.
 \tag{12}
\]

所有可能支撑、正负patterns和原carrier都覆盖；若path为空，其费用为0。
没有使用prime-pair或prime-triple correlation的猜想。

## 5. near ratio的平方剩余计数引理

先证明如下integer majorant。对奇prime ell、P≥1，令p遍历[P,2P]内
全部正整数，q遍历1≤q≤X，并准确剔除p²=ell q。那么

\[
 \sum_{P\le p\le2P}\sum_{\substack{1\le q\le X\\p^2\ne\ell q}}
 \frac1{|p^2-\ell q|}
 \ll(P/\ell+1)\log(2X),\qquad\ell\le X.
 \tag{13}
\]

当ell不整除p，记delta_ell(p)=dist(p²,ell Z)≥1。沿间距ell的整数
progression，把最多两个最近项单列、其余按距离编号，给

\[
 \sum_{1\le q\le X}\frac1{|p^2-\ell q|}
 \ll\frac{\log(2X)}\ell+\frac1{\delta_\ell(p)}.
 \tag{14}
\]

将p区间分为mod ell的完整blocks和残块。任意非零residue的平方根
至多2个，故每block的sum delta^-1≤2sum_(a=1..ell−1)1/min(a,ell−a)
≪log(2ell)。block数O(P/ell+1)，得到非零residue部分(13)。

ell整除integer p的分支不能遗漏：此时p²/ell为整数；剔除q=p²/ell
后，q求和至多O(log(2X)/ell)，包括中心在q区间外的情形。此类p个数
O(P/ell+1)，其费用也被(13)吸收。实际prime p=ell正是此分支中的一个，
没有把它错误赋予非零delta，也没有删除其q≠p项。

## 6. dyadic prime模数与endpoint共同节省

near且非diagonal时，令Delta=p²−qr≠0。因为qr≈p²，

\[
 b_p^2b_qb_r\ll1/p^2,\qquad
 |\log(p^2/(qr))|\gg|\Delta|/p^2.
\]

将(10)–(11)一起使用，实际每项normalized绝对费用为

\[
 b_p^2b_qb_r|K_d(S)|\langle W\rangle
 \ll\frac{\log(X/p)}{XL|p^2-qr|}.
 \tag{15}
\]

取p∈[P,2P]，P=X/2^(j+1)、j≥0，仅保留与p>sqrtX相交的bins。
令qs=min(q,r)、ql=max(q,r)，qs再按[Q,2Q]分bin；最多因子2的dummy
排序处理q,r，相等项原样保留。near强制

\[
 q_s\le\sqrt2p\le2\sqrt2P,\qquad
 q_s\ge p^2/(2X)\ge P^2/(2X),\qquad q_s>\sqrt X.
 \tag{16}
\]

所以相关Q满足Q≤C P、Q≥c max(sqrtX,P²/X)。在这些bins，
Chebyshev给实际qs primes的个数O(Q/L)。对每个ell=qs用(13)，
把p、ql放大至所述整数范围，仅用于positive upper bound。由Q≤CP，

\[
 \sum_{\substack{q_s\in[Q,2Q]\\q_s\ {\rm prime}}}
 \sum_{p\in[P,2P]}\sum_{\substack{q_l\le X\\p^2\ne q_sq_l}}
 \frac1{|p^2-q_sq_l|}
 \ll\frac QL(P/Q+1)L\ll P.
 \tag{17}
\]

设lambda_P=log(X/P)=(j+1)log2，则log(X/p)≤lambda_P。
对固定P，相关Q的bin数为O(1+lambda_P)：P≤X^(3/4)时
log(P/sqrtX)≤log(X/P)，P≥X^(3/4)时lower bound P²/X给相同上界；
固定倍数与boundary bins均只增O(1)。于是near全部费用≤

\[
 \sum_P\frac PX\frac{\lambda_P(1+\lambda_P)}L
 \ll\frac1L\sum_{j\ge0}2^{-j}(j+1)^2\ll L^{-1}.
 \tag{18}
\]

不使用p²≈qr的稀疏素数猜想。该O(1/L)依赖原真实endpoint overlap；
若粗暴使用W≤1，最上端bins的费用不能按这个证明趋零。

## 7. 回到actual有限矩阵与重复主项

(12)、(18)与diagonal给|Tphy|/d≪1/L。结合(7)，

\[
 \frac{|T_{\rm opp}|}d
 \ll\frac1L+\frac{\sqrt{\ell_0}}{L^{3/2}}+
 \frac{\ell_0}{L^3}=o(1).
 \tag{19}
\]

旧高素数报告的exact partition保持原样：

\[
 S_{\rm rep,H}=4T_0+2T_{\rm opp}-2T_{22}-T_\times-8T_3+6T_4.
 \tag{20}
\]

已付T0/N→Spsi、T22/N→Spsi、Tcross/N→0、T3/N→0、T4/N→0，
故(1)给(2)。这是actual finite compression的signed sector主项。
flat有d_H,psi(v)=(|v|+v²)/2、Spsi=19/480，遂2Spsi=19/240。
MT的严格系数为2int d_MT²，按旧报告的积分显示约0.0620202440072，
不把显示小数当作新的严格有理比例证书。

剩余full CH4仍包括所有四distinct词，且完整prime响应还有22distinct、
13/31、low预算、实际背景AC³等。新main不能与其他子预算直接相加来
冒充完整四阶常数。455已把whole proper powers在S4层面付小，仍只在
将来whole预算有界时传递其total fourth difference。本轮不登记新比例。

有限一致性检查见[精确脚本](../scripts/hybrid_high_opposite_exact_audit.py)
与[输出](../output/hybrid-high-opposite-exact-audit.json)：六个真实 cyclic-word
重复分解模型、1134个非零剩余与225个零剩余 progression 核验，及19/480
的有理积分。它们不认证无限素数估计、physical 支撑或三个内部P的付款；
这些步骤由本稿及两份独立全文审查给出。
