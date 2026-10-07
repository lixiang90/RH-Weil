# 原 mixed cubic 与 parity residual 必要约束：独立全文审查

审查日期2026-10-08。审查人 twisted_research。结论：四份推导及468汇总均限定PASS。
独立实读完整正文、复算关键算术与算子桥；未编辑被审稿、冻结来源、
math、Goal或Git。没有认证外部 [R] 全部证明、Lean构建或RH。

## 1. 最终字节绑定及范围

canonical定义：UTF-8解码后仅CRLF→LF、lone CR→LF，不strip或trim。

| 被审完整稿 | canonical SHA256 | bytes / lines |
|---|---|---|
| [compression mixed cubic](hybrid-background-entire-mixed-cubic-research-compression.md) | `19c715587681c95c3e8750e4751a30bff798b372f68dc516f029c0a5e71020dd` | 13926 / 289 |
| [radial parity必要约束](hybrid-parity-resolved-residual-necessary-constraints-radial.md) | `6a5fb7db8467e80682d7351ee37a940af8d39de50fffe2f16b0b3a48d5dfc6f6` | 13209 / 350 |
| [relative actual cubic](hybrid-background-cubic-relative-actual-recovery-research-compression.md) | `1dbdad713d2694d9fce6391971fc0044fcbf18d0ad3dbdd2d3fba5111ba80d38` | 5564 / 127 |
| [无条件capped31](hybrid-thin-high-short-low-unconditional-three-one-research-radial.md) | `74e47ca7b791656c25067793a2d9068c47675f3f60f0afc4d5c5d344fef5ea34` | 7831 / 216 |
| [468原路线汇总](../../notes/468-original-mixed-cubic-and-parity-resolved-fourth-reduction.md) | `ad4cf9f8bb4c77e24487b32434dc64d28162745adf3b1e0555b230be3953baf7` | 8694 / 205 |

第一稿的完整mixed小量覆盖原weighted LLL、HLL、HHL所有placement、
directions与标签。HHL依赖同一conductor-one fixed-gap [R] theta<9/10；
LLL、HLL不需此输入。全背景 A C_Lambda³=o(d)仍须增长控制；
新relative补充将足够前件降至a_T=o(log²X)，不必先假whole high4有界。
第二稿给原实际parity必要条件，主high结论明列q有界，未支付q上界或k下界。
两稿都不能升级为新实际零点比例或完整第四矩常数。

## 2. mixed cubic：near与原标签范围

逐次零延拓作用直接给原式(1)的三个negative coefficients、两项
intermediate phi²、endpoint phi与原 K_d(S)。weight w(u)不展开且保持
同一u；normalized u integral至多M。没有循环physical末端P。

八个signs中只有two-versus-one可以near；S=0不可能，因为prime
不能等于两个primes之积，含重复标签亦成立。fixed2c<log2后：

- LLL的product prefix至多2sqrt X，两个整数column energies均O(sqrt X/L)。
- HLL只有high-single对low-pair可near；high乘low至少大于2sqrt X，
  对另一low的ratio不在这个near窗。energies为O(X/L)与O(X/L²)。
- HHL只有high×low对另一high可near；product prefix至多2X，
  两侧energies均O(X/L)，high/low factorization唯一。

这些prefix只限product一侧，再以smooth kappa(log(n/q))的Fourier
integral分离single-prime侧。shared windows在应用Hilbert前一起
分离，所有placement只改变unit phases。prime/semiprime整数集合
无重合；local log spacing的倒数O(n)与原normalizer相容。
准确K_d在near展开的O(1/d) remainder也逐类付款；尤其HHL使用
真正截断product mass O(sqrt X/L)，未偷换长product成canonical前缀。
三类near normalized费用分别为
O(ell0³/(sqrt X L))、O(ell0³/L^(3/2))、O(ell0³/L)。

## 3. mixed cubic：HHL整个far与alias

整HHL rawmass/X增长，因此不能只近核付款后宣布entire。
被审稿正确先保原endpoint overlap，在固定±L strip作positive计数：
两个high同向、low反向时physical support pq<Xr给mass O(X/L²)；
两个high反向时反射成p/(qr)，positive alias为空，negative alias强制
p<=e^(2A)sqrt X，给mass O(X/L³)。同向三步physical为空。
原K_d的pole与endpoint overlap共同给O(M/X)，三placement皆覆盖。

剩余g_L(S)=(1-kappa)(1-alpha_L)/(L sin(pi S/L))在0、±L
固定邻域为零。直接分central和endpoint距离积分，得到
||g_L||1=O(logL)、||g_L''||1=O(1)，故Fourier L¹=O(ell0)，
highfrequency L¹尾O(1/T)。同三个真实window因子共同分离后，
每个prime保持其原独立sharp前缀，w(u)phi(u)未分离也不改coefficients。

原floor d的两个carrier endpoints保留。good coordinates使每个
prime height绝对值在[T/2,3T]，canonical HHL费用是
q_H²q_L/X=O(X^((5/2)a-9/4)polylogX)，固定theta<a<9/10确有节省。
bad coordinates则取原m_H²m_L全height质量，费用
O(X^(-3/4)ell0^C/L³)；其中tau≈0主峰没有使用高height cancellation。
LLL、HLL far原全部质量/X分别为O(X^(-1/4)/L³)、O(L^-3)。
没有漏掉middlefar、alias或共有prime标签。

## 4. mixed cubic：全部P与最后conditional桥

LLL/HLL raw两次crossing以及HHL good两次crossing均保持三个内部P。
后者是O(Lq_H²q_L)，除以d确为负幂；所有weight/op及左右泄漏明列。
最终稿的complex w补明正确：Mw为normal乘法，D=E*MwE，
两方向leakage平方分别为TrE*|w|²E−TrD*D和
TrE*|w|²E−TrDD*，有限迹相等。因此ell_w*=ell_w，不能在一般
非normal算子上仿用这条恒等式。原背景real h满足前件。

finite bad compression用S1 O(m/T²)；physical good/raw用right原phi
packet及first-far HS O(1/T)，left wphi packet HS O(sqrt d)。
HHL normalized费用m_H²m_L/(T sqrt d)=O(X^(-1/4)L^(-7/2))，
不是以op尾乘d的错误付款，也不将P与height cutoff交换。

whole high4有界后，既有parity weighted high³相对界才趋零；
Schatten Minkowski给whole prime4有界，actual背景op O(1/L)误差
乘normalized cubic trace趋零，455 proper-power S4=O(1/L)由Holder
恢复。这个顺序支持其(9)–(10)，没有提前假设full4来付款mixed项。
没有whole high4前件时，仅mixed小量和high³相对界可使用。

## 5. parity residual：clip与两次极限

U为实际finite involution；E_U、O_U为real HS正交投影，不能把H的
二范数近odd性质直接升级成H²的二范数近even性质。源稿保留了这一缺口。
bounded W,V与原sharp J的交换及所有Q误差给它们的odd部分o(sqrt d)。

fixed clip的HS Lipschitz式通过spectral projection交叉权重
Tr(P_iQ_j)>=0直接证明，且odd clip保持近odd。对R²>=M_T，
D_R=H²-H_R²>=0，H_R²在其支撑上准确等于R²；所以
TrGamma_R D_R>=(R²-M_T)TrD_R>=0，
q-q_R>=||D_R||²/d。由此finite r界中的两项error及PSD正号都正确。
sharp4M应用于H_R无需另一个commutator假设；
|sqrtK-sqrtK_R|<=2M_T sqrt(a_T)/R也保持实际有限矩阵。

明确q_T有界后才有a_T有界；先固定R、T趋无穷，再R趋无穷，
得到liminf(q-r)>=41/15120。共同有界子列的陈述正确，未混用
来自不同子列的limsup。它给新的even成本分配，不能解释为odd
fourth tails全部消失。

## 6. parity residual：low的全部迁移与sharp J恢复

源稿(15)的compression差准确为−(QB_LE)*(QB_LE)，HS<=y ell。
(16)同时保留U−S、QJE及low两factor投影。y²ell_J=o(sqrt d)，
故实际UAU到physical J B_L² J的比较合法。T_o的outside leakage
o(sqrt d)支持HS平方差传递；先由已付whole low4获得有界HS norms。
不是从一个formal zero-path常数跳到实际finite square。

sharp J先用fixed smooth j_epsilon及g_epsilon付款。对每个fixed
epsilon，共同窗口Fourier/Hilbert、far原质量以及closed word两次
crossing给o(d)。g_epsilon weighted low4的每个zero-path只有translated
宽O(epsilon) strip，故其主项O(epsilon)。compression Schwarz式(20)
控制(S−S_epsilon)²；乘A²=L⁴时仍是positive trace，不能非法换序。
U−S项以y²ell_J支付，最后先T再epsilon。整个迁移不依赖high4。

zero-path中T_o²的系数准确为(1−sign(t)sign(t+S_2))/2。
A两步已回原点，odd系数为零；A'、O在same orientation的crossing
长度为min(x+y,1−x−y)，opposite orientation为|x−y|。所有中间点
在原interval的条件已逐项核算，含x<y时的另一半。
三积分独立用有理多项式积分复算为1/480、1/960、7/1920，给
delta_odd=13/480、delta_even=11/480。all-repeat correction仍趋零。

## 7. covariance及实际开放范围

parity两部分HS Cauchy得到共同极限的必要约束
|c−23/960|<=sqrt((q−r)11/480)+sqrt(r13/480)，
r<=q−41/15120。它未把整体Delta垂直Z拆成分量各自垂直。
在尚未证明Q=1/350前件下，允许r区间确在根号和的递增段；
极值r<=11/75600。独立Fraction复算两根号内数、strict平方证书：
3077/90720000>0及4883/28576800000000>0，故|c−23/960|<1/100。
必要区间67/4800<=c<=163/4800与文本一致，不能据此实现或排除
整个实际q/k候选。

未见阻断性数学缺口。上述有限有理复算只核常数与代数，不认证
渐近分析或素数correlation。whole high4、全31/22 signed净预算和
467的实际q上界/k下界仍须付款；四稿的新增结论保留这些范围。

## 8. 468汇总全文范围核验

独立逐节实读468最终完整205行。其(1)–(2)保留原normalizer、finite
carrier及零延拓，日志长度ell与low矩阵L区分明确。显式公式响应
mathcal M的(7)保留明列的high fourth控制前件，不将它直接当作
新的零点比例输入。

其(3)–(4)把LLL/HLL无[R]与HHL需fixedtheta<a<9/10分开，
对象是A0，不提前用op O(1/ell)改成actual A。其(5)–(7)首先依序
先付prime whole4 bounded，再actual背景及proper powers。
新增(7a)给较弱a_T=o(ell²)的恢复合同，由§9核查的实际二矩配对
证明；454的原中心展开o(1)本就不需要F_T bounded，因此该较弱
前件也足以得(7)渐近等式。这仍不提供用于比例的常数四矩预算。

其(8)–(10)范围、16signs、netgap和无条件raw bound与§10新来源
一致；[R]的三个更强有理指数仍对应原作者稿。较大的至多一个bulk
标签分区明确要求同一[R]，仅宣称12非交替signatures。
本段只核汇总陈述对应来源，不将本人作者稿的自核作为另一份独立
审查；它们的另一作者审查见
[compression完整独审](hybrid-three-high-one-low-gate-and-capped-review-compression.md)。

其(11)–(15)明确flat、q有界、共同子列及futureQ前件；odd预算
11/75600与strict c根号余量准确。没有把必要约束当作实际q/k预算，
亦没有非法拆用Delta与Z的整体正交性。结尾保持原sigma及比例不变，
未由小块重复常数拼出全四矩。该汇总未扩大四份新推导的前件或范围。

## 9. 新relative actual cubic恢复全文独审

追加独立全文实读
[relative actual恢复](hybrid-background-cubic-relative-actual-recovery-research-compression.md)，
canonical SHA `1dbdad713d2694d9fce6391971fc0044fcbf18d0ad3dbdd2d3fba5111ba80d38`，
5564 bytes / 127 lines，限定PASS。它是新补充，不修改原mixed冻结稿。

原C_pr二矩O(1)由原Lambda二矩及已付proper-power S4差获得，不假设
high4 bounded。normalized Schatten Minkowski给f_pr<=8(a_T+low4)，
故sqrt(f_pr)<=C(sqrt(a_T)+1)。static cubic只把已付七个low-containing
词记成r_T趋零，未知high项仍以sqrt(a_T)/L显式保留。

actual背景R_T C_pr³分成(R_T C_pr)C_pr²，S2–S2配对确给
||R_T||op sqrt(c_pr)sqrt(f_pr)，没有较粗f_pr^(3/4)费用。
完整proper-power非交换展开的七词独立核对正确。第一组三词
AC²P、ACPC、APC²各不超过M sqrt(f_pr)epsilon；第二组三词
ACP²、APCP、AP²C各不超过M sqrt(c_pr)epsilon²；AP³不超过
M epsilon³。有限迹循环只用于改变配对位置，没有交换非交换因子。
所有Schatten norms均按d归一化，指数之和为1，无隐藏d因子。

所以原actual全背景cubic严格满足
|Tr A C_Lambda³|/d<=C(sqrt(a_T)+1)/L+o(1)，
不先假a_T有界。较弱a_T=o(L²)即可使cubic消失；它仍不提供任何
a_T新上界，更不单独提供全四矩常数或实际比例。其[R]仍来自原
mixed HHL fixed-gap合同；static high相对界本身不需新[R]。

## 10. 新无条件capped31全文独审

追加独立全文实读
[radial无条件原载波简证](hybrid-thin-high-short-low-unconditional-three-one-research-radial.md)，
绑定表中最终74e47ca7版本，限定PASS。与本人较强[R]推导不同，
本节逐式核验作者重新证明的raw bridge和positive mass论证。

单向translation的g_s=phi(u)phi(u+s)具有uniform一、二阶L¹
derivative界。交叉导数项用||phi'||infty||phi'||1付款，compact
C²零延拓给||phi'||infty<=||phi''||1，即使step靠端点也不失常数。
实际原完整Fourier基矩阵核(8)正确；两次IBP无边界项，分别给
|c_n|<=C/n及C ell/n²。outside pairs恰min(d,|n|)，因此
每个单向factor的leakage²<=C b_p² log(2+ell)。反向伴随是原
相反step，完全同界；Minkowski对实际prime sum得到双方leakage。

非自伴six-term two-crossing保持每个ell_i*与ell_j的方向，没有
以selfadjoint恒等式代替。raw actual/physical差因而只有
O(log(2+ell)m_t³m_s)，不乘未知全fourth，也不改原projection。
所有16signature中12物理词为空，余四逐tuple netgap正确。
固定sin下界给|K_d|<=C/d；原floor及全carrier heights都已包含，
不需height截断或ghost恢复。positive mass只用于这个固定gap子块。

独立Fraction核算3(11/40)+1/6=119/120，所以除以d后正质量及
projection费均有X^(-1/120) ell^(-5)节省，最终(20)的额外log因子
准确。所有repeated/distinct标签保持在factorized范围sum中。
无需[R]或unknown high4；扩caps或其他原标签仍未支付。
