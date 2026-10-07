# 467 两残差Schur与整个22交换子：独立全文审查

2026-10-07。twisted_research。全文限定 PASS。
没有修改被审稿、旧冻结研究、math、脚本、输出或 Git。

## 1. 最终源绑定和实际范围

被审稿：
[467](../../notes/467-two-residual-schur-and-commutator-budget.md)。
canonical LF SHA-256：
0089fd92c70d5e2b7b48bef0084675707f2fe283833f8a97745766ccf6899cb8。
UTF-8 原字节10830、312行；仅CRLF/lone CR→LF，不trim。
本次实读最终全文七节，未仅沿用465审查或作者摘要。

前置最终全文：

| 输入 | canonical LF SHA-256 |
| --- | --- |
| 465 | a9290d2d847c2a3f7942b26353bd1582a68b391e481acc109c4ac18d3d750464 |
| 466含sharp §5 | 0b955bdc26b4bf950ce457dec7bf18f635f702d85a73d73c8d6263df969cbbbe |

另重核454的原weighted二矩、461的actual entire13、462的low4，
455的proper powers、452的同响应padding与197/228的完整one-sided LP。
本PASS不独立认证这些[R]底层全链，不把原7/8 bootstrap当RH。

## 2. 低diagonal V的全部有限准入

V与W是同一个原窗口中分别取low/high同素数multiplication压缩，
均positive且sup、一二阶L1 derivative统一有界。
互换bounded weight不会改变465的middle-P comparison：
physical到finite的HH费用仍为
O(X log(2+log X)/(log X)²)=o(d)，HL/LL更小。

VHL及WHL是complex cross。用BH+zBL、z=1,i极化，physical高低频
labels不交，给complex cross本身o(d)。三矩阵顺序通过有限循环迹
和共轭保留；没有把HWL或HVL直接改为WHL/VHL。
每个physical二矩仍支付原全部difference Hilbert、±log X remainder、
sum-alias真实overlap和carrier相位。

WV的比较另有两次bounded multiplication crossing，
trace-norm error≤ell_w ell_v=O(log(2+log X))=o(d)。
因此(3)的九个极限均由已有二矩输入恢复，未调用未知high4。

## 3. 精确centered Gram与退化域

Γ、Δ、Z=(HL+LH)/2都是Hermitian，故real normalized HS确为内积。
逐项重展验证(7)：

- <Γ,Δ>=c−Tr(VH²+WL²−WV)/d；
- <Γ,Z>=b−ReTrWHL/d；
- <Δ,Z>=η−ReTrVHL/d；
- ||Z||HS²/d=(c+TrHLHL/d)/2=c−k/4。

这些只用actual有限循环迹；HL本身不需selfadjoint。
0≤k≤4c来自|TrHLHL|≤TrH²L²，非free operator ordering。
两个平方残差norm展开给a=S_H+q+o(1)、
δ_T=e_T−S_L+o(1)；显示误差不会乘未受控q。

Gram(9)是三个实际HS向量的Gram，必然PSD。
δ_T>0时在Δ方向正交投影给(10)，两右因子各非负。
δ_T=0时Δ=0、p=ε=0，不作除零；正文明确处理。
whole fourth非交换cyclic系数为a+e+6c−k+4b+4η，
所以有限(12)正确保留τ、ε及pε/δ。
未知q增长时，没有将这个最后项免费删除。

## 4. Bounded-q之后的极限和compact域

另有limsupq≤Q0才使a、c、k、p统一有界。
固定δψ>0后δ_T有正下界；τ、ε→0使有限Schur修正趋零。
平方根在非负compact域连同0端点连续，故(13)与positive-part说明合法。

liminfk≥κ0时可取达到limsupF的subsequence，由紧性将每个actual
limit放进(15)，从而(14)是正确upper。
域可以放松，但不能宣称域内每个点有原算术实现。
目标函数随q增大而增大、随k增大而减小；取Q0、κ0保守上界正确。
若没有actual k lower，只能使用0，正文没有从weighted二矩偷取它。

## 5. Flat常数与旧条件排除

本次Fraction独立积分重算：
S_H=19/480、S_L=7/240、C=23/960。
原actual low fourth e=19/240，因此δ=e−S_L=1/20，
并非把低diagonal平方当作完整low4。

466最终sharp有限式K≤4Mq与actual K=41/10080、M≤3/8+o
给liminfq≥41/15120；Q1/400及1/1600均排除。
新Q1/350与该标量障碍间余量11/75600准确，但不证明其可达到。

§5的代数诊断点q=41/15120、c=1/30、k=0满足放松域。
独立有理计算：
R=923/29030400，h=359/30240，
16R−h²=336311/914457600>0。
因此仅删掉k再给q upper的这个Schur envelope不能认证1/3。
这不是actual等号模型，更不是原路线不可能性的证明。

## 6. 最终新候选的连续有理证书

只在尚未支付的联合前件
limsupq≤1/350、liminfk≥1/40下检查全连续域。
合法c≤C+sqrt(Qδ)<C+3/250=863/24000。
取B=81/250，独立展开得到

R(c)=6367/28000−6c，
P(c)=320c³+(56/3)c²−(1257437/504000)c
     +717527777/14112000000。

在整个[0,863/24000]上R≥163/14000>0。
本次另用Fraction自写power→Bernstein变换，对正文同一32等份
计算全部128个系数；最小值精确等于
665078890949/6502809600000000>0。
这与正文一致，是连续正性证书，不是采样点最大值或浮点推断。
对可行域radicand非负，正R和P使平方比较方向合法，
故整个joint objective严格小于81/250。

## 7. Proper powers、背景与条件比例scope

只有获得bounded whole-prime fourth之后，才使用455的
proper-power小S4、454的flat V=Z=J=0及cubic Cauchy，
恢复原完整centered response。没有在未知增长的C³上免费删背景。
452再支付同一对象的zero-side padding、d/N→1。
197/228的首迹、二矩、padded重数和全部有限边界误差仍是前件。

精确LP计算：
(1−1/3)²/(1−2/3+81/250)=1000/1479>27/40，
辅助参数(1/3−81/250)/(2/3)=7/500∈(0,3/4)。
不需要另有三阶矩极限。这个比例仅是联合前件下的蕴含。

限定 PASS：新增finite三向Schur、实际weighted准入、强方差障碍
与连续有理conditional预算均相容。q upper和high/low k lower都仍未付，
底层[R]及完整四素数算术未因有限审计得到认证。
本报告不确认新67.5%以上实际比例，不登记新无零区域或RH证明。
