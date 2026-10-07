# 自由b正式论文独立全文逆审

2026-10-07。审查人 twisted_research。**限定 PASS [T/R]。**
本轮从新tex全文重新审查，而非以449审查结论代替论文审查；重读新增定义、
物理补偿、完整反射能量、actual capacity、Euler/principal/outer及全族Mellin证明。
已提出的定义和公式遗漏均在绑定版本修正；当前没有待处理的阻断问题。

审查对象：`papers/free-b-compensated-probe-boundary-paper.tex`。
最终canonical LF SHA256（CRLF及单独CR换LF后UTF-8）：

`5df2b6ad687572229e2c4d41292bee6cf81b57a13b762173d26732169f1688db`。

最终排版重绑：第835行仅将审计命令的
`\src{python scripts/hybrid_free_b_geometry_exact_audit.py}`改为
`\texttt{python}\ \src{scripts/hybrid_free_b_geometry_exact_audit.py}`，使空格正确显示。
独立反向替换这一处，恰恢复已全文审查源哈希
`0fc6b3687b2545098482dbf14f7258f5fb26505eb7ba376387b4a13597caf7b7`。
没有数学内容差异，限定PASS保持。

## 1. 外部输入及独立审查范围

论文明确是相对Definition 1.1中mathcal R的推导；不独立认证外部整体证明、
Lean elaboration/kernel/Comparator、RH或新的临界线比例。
导入的是保持原系数类、uniformities和side conditions的通用命题，
并以原完整finite-order Hecke 7/8定理只给beta_*<=7/8。
quadratic factorization已列为独立导入项，未暗含新无零结论。

原source固定为OpenAI/math提交
`adc7f1241b42e322a6451854ab7e4b4c146bf78a`，
`preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`，
canonical LF SHA256
`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`。
本轮直接重读原7663–7804（通用energy完整前件与公式）、8340–8364（完整Gram）、
5582–5649（独立physical quantity及exact high identity前件）、
15097–15156和15369–15446（whole-slot gain、Theta系数、strict widths及no-slot）、
4385–4408（e0和实际height限制）、5672–5728（多维integrated/trace tails）、
400–502、6520–6580、6705–6780（全族continuation、late height和quadratic transfer），
以及5518–5528的实际principal H_eta定义。
其他local arithmetic与joint-error接口按论文Table 1的准确来源和已交付旧论文逐式对照，
没有以旧fixed-geometry low theorem覆盖自由b证明。

独立补充只读代理再次核了定义与physical/normalizer绑定，发现H_eta未明确定义；
最终版本已补同一final S的确切乘积。此补充不代替本轮全文逆审。
本报告不认证PDF渲染或排版；这些由root另行完成。

## 2. 同一物理表达式及低界的真实分支

论文§2子集公式保留marked操作
overline(eta(p)) I_(eta;p)(X,Y,Zq_p)，以及被减去的
q_p^(-3/2) I_eta(X/q_p,Y/q_p,Z)。多个操作组合时，J仅记录rescaled slots，
marked divisor与Z倍率均使用p_(J^c)；每个原window仍在自己的P_i。
completed cn^3 sums的绝对收敛是R输入，有限的是补偿子集与retained annular
分解，未误称全部completed sums有限，也未以high积分定义physical quantity。

Cb(s)=s+lx/2-1+h/6=s-2/3-b/6，w=1,z=1/6留数及
Gaussian exp((s-5/6)^2)保持准确。几何b与固定算术datum b_*不同。

对0<=d_J<=ell，M'=1-ell-2d_J、ell'=ell-d_J给
M'+ell'-1=-3d_J。实际powerful/residual dyads而非理想化等长行给
Delta_H=M'-O-H>=-eps_Z；由2A0<=O+eps_Z及原retained support，
Td<=H-3d_J+2eps_Z+|theta_N|。
最终论文完整列出E_ref、s_hyb、y_ref和frozen-part saving identity。
两分支及kernel saving的提取发生在平方和positive enlargement前；
powerful/supported fixed parts只计一次，原S-primes与zero extension保留。
这些通用前件及B-energy账本不含固定几何b。

在1/6<=ell<=1/5、0<b<=3(1-ell)/8内，M'>=2/5，
lx-d_J、ly-d_J均正。Q,Y'最终>=1，位于固定多项式范围；
P_a=Y'^2/Q=q_(b_*)^(-1)Z^b>=1最终成立，允许阈值依固定target datum。
完整Gram的第三项P_a^2/Y'确实保留；其系数是原固定ray/Gauss组合，
没有给arbitrary row-dependent coefficients准入。

tuple数、q_(p_J)^(-3/2)、sqrt(X') shortening合计-d_J。
相对lx/2+b/12的额外幂为

\[
F(d)=-d+\tfrac12(11b/6-l_y+d)_++\tfrac18(5\ell-1+d)_+.
\]

每段斜率最多-3/8，故最大值在d=0；ell<=1/5给
L_low=max{(1-ell)/4-b/6,b/2}。
论文明示b范围恰选择第一分支，并得到sigma=11/12-ell/4。
较强all-subset Gram gap在最终参数亦成立，但没有把它误作整个宽范围的必要条件。
任意小幂先指定、moving rows/tuples及prime labels不改变其常数选择；
固定data及target可改变常数和最终阈值。

## 3. 连续证书、actual counts及所有行范围

beta_*现在明确定义为全primitive finite-order Hecke非平凡零点实部的supremum，
含1/2兜底并剔除principal pole。旧bootstrap使合法plain参数可固定kappa=3/4；
不把负的beta_*-7/8代入原正excess comparison。
nonfloor a<=beta_*给delta<=3/4，alpha=5/6仍来自sixth-power amplification。
q平均所有slot长度，errors和zero slots取gain 0，不能只平均positive slots。

inverse/plain crossing与long-witness comparison给原D,P,J,R_*；
paper参数化y=1/2-x准确。J在实际rectangle严格正，
1-delta<=R_*<=1-2delta/3。R_*的准入依实际moment前件与供给，
未从AF simple-zero percentage改造坏行数。

重跑`hybrid_free_b_geometry_exact_audit.py`的841项检查全部PASS；
脚本canonical LF SHA256为
`5a366da5e8114d158cb76b3a94060155786a0ca637a914b662ba17cd66afa63f`。
其189个direct cases仅implementation checks；连续rectangle由
-1296J E_sigma=A delta^2-B delta+C、A>0和Q=4AC-B^2逐系数正性证明。
临界处Q0=0，其余Q_i>0；完成平方只在y=0、
delta=(49-sqrt(921))/48等号，且该点在真实delta范围内。

有理见证的margin同时使用A0 Q-Q0 A逐系数非负与J<=5/2，
故Q0/(12960A0)=10580567/347281513800000成立；
没有以A0充当A(y)上界。最优性只针对所声明的low intersection、
R_*与完整amplitude rectangle；固定等号点R_*=2/3消去b，
ell斜率为3/4+3delta_circ/2>0，不能推广成所有方法的最优无零边界。

generic d账本经正确unfactored式重写，selected slope>=57/200>0；
floor独用R=1无需witness，middle使用独立no-slot count并包括floor。
从h到h+zeta的费用<=Delta/16，zeta=Delta/32由全族共同gap选择。
真实参照是Cb(beta_*)，E_beta=E_sigma-Delta只扣一次；
临界E_sigma=0仍留下15Delta/16的中央预算，而非阻止闭合。
floor、middle、small分别保留独立的1/200、1/50、2/25余量。

已核inverse branch r>=r_*(t)、plain branch r<=r_*(t)及明确的
z<=z_M-nu0或z<=z_P-nu0。前者second width>=9/37-o(1)，
后者保留plain width；r>=1、m接近1/2及small capacities使用原no-slot版本。
ell/(h+zeta)>1/5>7/37；只在d>=1/2选physical slots，wi<=2ell_i。
先mesh/decrement/rounding后K，使whole-slot rounding loss及内部plain pool
分離满足严格前件。原Theta有限系数、whole-product conjugation与natural masks
保持；实际coefficient是overline(nu(p))1_T的固定有限组合，不要求eta(p)=1。
outside-S inducing exceptions仍排除，剩余有限S-supported rows由bounded rows覆盖。

## 4. Euler、principal/outer及全族选参

局部系数不依几何b；新sigma仍大于5/6，good/ramified defects分别
sigma-3/50>81/100、sigma-1/20>82/100。一般good的
4-6s-6z项保留theta=(-Re w)_+，D1使用eps_H=min(eps0,1/50)。
这支付正常收敛及all-height majorants；未直接引用旧Re s>7/8的解析域。
whole bins先global move再buffered local move与pointwise partitions。
完整selected tuple用G_p，不除一般H_p；strict local errors与numerator只扣一次
conductor deficit，ell q不因每个ramified label重复扣除。

最终H_eta明确绑定同一final S的actual principal correction
prod_(p notin S)H_p(s,1,1/6)=mathcal H_(eta,1)(s,1,1/6)。
target-pre P0控制positive product majorant，target后增大S只缩小它。
Si、AT=(-1)^K Z^(-ell/6)prod Si、cS都绑定原ray/calibration和同一S；
AT最终非零且逆为subpower，只在大Z正常化physical函数。
principal s始终global，w/z跨原1/1/6留数后主s仅向右移至2。
三项margin mw=ly/20、mz=h/600、mu<sigma min ell_i均正。

small rows重证D1(1/3)，而非借用不够的新域D1(3/8)；
relative small exponent<-2/25已相对Cb(beta_*)，不可再扣Delta。
large rows保留完整absolute tuple；zeta先定，fixed z_infty随后在target前选，
不随moving row、Z或后选external N改变。

统一顺序为：共同Delta和geometry，count/moment losses、strict capacities、mesh和rounding，
then even K/windows，then mu=sigma ell/(2K)、amplitude widths/prime powers/e，
then target arithmetic datum/final S/internal orders，then actual ceiling/tau，
then external N，最后threshold。源e0只依epsilon和有界长度范围，
故没有隐含用target-dependent e回选共同K的问题。
principal损失单独小于mw/4,mz/4,mu/4；central损失小于Delta/4。
m0取这些共同正量的minimum；mu可极小，不导致回选mesh的循环。

## 5. Cutoff-independent Mellin反证及最终范围

J_eta只在充分大Z定义；f_eta在全部Z>0定义，二者都不含T1。
internal A_eta/B_eta先于N固定，multidimensional retained frequencies
共用一次T1/2 allocation。源external tails允许增加N仅增加external test seminorms，
而不增加A_eta/B_eta或已支付的real powers。

实际detector ceiling可在target/internal orders后固定为正数；
U>=Z^d_min与固定height cost使tau0存在。
选tau<=min{d_min/100,tau0,m/[4(A_eta+1)]}后才取N，
得到target-pre saving sigma_hi=m0/8，即使tau、N和threshold依target。
omega=Delta/2支付low及inverse AT，epsilon_*=min{Delta/2,m0/8}>0共同固定。

大Z由low/high给f_eta增长；小Z仅对f_eta向右移至任意fixed B>2。
mathcal F_eta=integral f_eta(Z)Z^(-Cb(s))dZ/Z在Re s>beta_*-epsilon_*
局部一致收敛，初始line2的Gaussian Fourier识别给原实际H_eta/L_F^S。
这里使用Cb斜率1；没有移线跨目标零点，也无需小Z的AT逆或J定义。
epsilon_*<Delta保证延拓域仍在已支付的H_eta域，|H_eta|>=1/2排除numerator抵消。
supremum无需attainment：共同epsilon_*先于选择任何逼近它的target zero。
deleted Euler factors在Re s>0非零；quadratic factorization及s=1的
L(1,chi_-3)=pi/(3sqrt3)排除principal pole-zero cancellation。
因此相对mathcal R得到严格新half-plane，包括imprimitive角色并允许principal pole；
没有包含boundary line或暗称RH。

旧已交付论文canonical LF SHA仍为
`92ba93da7cc568579b0b982bcd712e1382af749d05460c1fa4c8b25064df66d6`。
449正文绑定`2d4b37628d6f68229fd687d6ac84c2ba03cb7223c412df5e00c07a0ff5e1a3bd`。
本轮没有编辑它们或math源；论文bibliography中的本地路径均存在。
**最终结论：绑定版本限定PASS [T/R]，无待修阻断问题；原整体输入正确性与新结果的
形式化仍分别属于未认证范围。**
