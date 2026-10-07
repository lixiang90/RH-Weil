# 449 自由b边界与全角色族continuation独立逆审

2026-10-07。审查人 twisted_research。**限定 PASS [T/R]。** 直接阅读全文并逆查
§5–7的actual count、new-b几何、完整error tuple、Euler/principal/outer、共同
Delta预算和全族Mellin合同；同时复算low归一化及连续证书的接口。
此结论依赖正文明确列出的外部通用[R]与全Hecke7/8 bootstrap，不认证原整篇证明、
外部Lean/kernel/Comparator或RH，不把AF比例作为新的行数输入。

审查对象：`notes/449-free-b-compensated-geometry-and-optimal-relative-boundary.md`。
canonical LF SHA256（CRLF及单独CR换为LF后UTF-8）：

`2d4b37628d6f68229fd687d6ac84c2ba03cb7223c412df5e00c07a0ff5e1a3bd`。

## 1. 来源、哈希与实际检查范围

外部source：OpenAI/math提交`adc7f1241b42e322a6451854ab7e4b4c146bf78a`的
September-30 `build/paper.tex`，canonical LF SHA256为
`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`。
本轮重读1123–1209/1288–1315（固定实幂、共同profile和external tails）、
2470–2506（实际row sectors及zero extension）、7663–7804（通用反射能量）、
8340–8360（完整Gram前件）、4385–4408（e0只依赖epsilon与有界长度范围）、
15097–15156/15369–15446（whole slots、原Theta、strict widths及no-slot）、
15469–15493/16191–16255/16303–16453（real/target/internal/external顺序与height ceiling），
以及5672–5728的完整多维integrated/trace tails。Euler与joint-error逐项对照442/444，
full-family Mellin与445原已审合同对照；没有直接引用固定b的low/high结论覆盖新参数。

新自由b推导 `hybrid-free-b-geometry-optimization.md` canonical LF SHA256：
`35dac7399af8507be7c39c0e3e69c37d47adf83ebda9125d2a5f62e663037f67`。
新精确审计 `scripts/hybrid_free_b_geometry_exact_audit.py` canonical LF SHA256：
`5a366da5e8114d158cb76b3a94060155786a0ca637a914b662ba17cd66afa63f`。
已只读重跑，841项检查PASS；其Q与Q(sqrt(921))算术只认证显示代数，
189个direct cases不是连续域证明，不认证实际素数、无穷轮廓或[R]。

正文所有5个本地链接均解析到现有文件，源commit和哈希匹配。
本审查的重点是原分析合同在new-b处是否成立；另一个代理的代数/low审查不代替本轮
对§5–7的独立检查。

## 2. Low、同物理身份和准确参考幂

generic smooth calculus明确允许固定实指数，故ell、b、ell_i不须有理。
completed cn³ sums、原mask、disjoint slots、finite compensation与两侧S没有改变。
保留M=1-ell、ell'=ell-d_J、M'=M-2d_J给M'+ell'-1=-3d_J，row loss仍
Td<=H-3d_J+small；这一B-energy关系不含b。new b只进入实际X',Y'和Gram。

在1/6<=ell<=1/5、0<b<=3(1-ell)/8内，M'>=1-3ell>0，
lx-d_J、ly-d_J均有正固定下界；Q,Y'>=1且为固定多项式范围。
P_a=q_(b_*)^(-1)Z^b>=1最终成立，阈值可依固定target datum。
通用Gram保留第三项，不能仅沿用441单项吸收。

tuple数Z^d、原q_(p_J)^(-3/2)与sqrt(X')缩短合计为-d；完整额外幂为

\[
 F(d)=-d+\frac12(11b/6-l_y+d)_++\frac18(5\ell-1+d)_+.
 \tag{1}
\]

四种斜率-1、-1/2、-7/8、-3/8都负，最大在d=0。因ell<=1/5，完整low
确为max((1-ell)/4-b/6,b/2)。所取b范围使第一分支占优；两个候选又处于
更强all-J Gram安全范围内部，正gap没有靠端点延拓取得。empty marks、共同profile
先提kernel saving及平方前恢复全部slot、powerful部分和固定S-prime前件均保留。

同一主双留数的位置w=1,z=1/6给

\[
 C_b(s)=s+l_x/2-1+h/6=s-2/3-b/6.
 \tag{2}
\]

所以low交点准确为sigma=11/12-ell/4，Gaussian仍exp((s-5/6)^2)。没有改变
normalizer以倒填信号；X/Y也没有与448的AF height尺度混淆。

## 3. 连续证书及最优性范围

原actual R_*采用kappa=3/4、alpha=5/6、delta<=3/4；D、P、J不含几何b。
J>=35/54且<=5/2。独立将完整unfactored Mellin幂代入可得正文(13)(22)；
b导数R_*/2-1/3正确。

A,B,C及Q=4AC-B²的证书由F=-1296JE和完成平方给整个连续rectangle，
不是由189个cases推出。critical处A正、Q_0=0及其余系数正，故E_sigma<=0；
唯一等号y=0、delta=(49-sqrt(921))/48确在真实[1/50,3/4]范围。

独立核这个delta满足R_*=2/3；代回给
-5/12+3ell/4+(1/2+3ell/2)delta，与b无关。其ell斜率严格正，零点正是
e=(33+8sqrt(921))/1653。因此正文“最优”确只针对相同low交点、原R_*和完整
amplitude rectangle；不是实际坏行达到包络或所有方法最优的声明。

有理见证的A_0Q-Q_0A逐系数非负是必要的比较步骤。完成平方给F>=Q_0/(4A_0)，
再用J<=5/2得-E>=Q_0/(12960A_0)=10580567/347281513800000>10^(-8)。
主文没有仅用Q系数正便错误地把A_0当成A的上界。与447和critical的两个严格比较
都可用原有理式核准，无需小数排序。

## 4. §5 actual counts、new-b供给及全部physical d

bootstrap只用beta_*<=7/8，所以kappa_eff=3/4、Delta_eff=0合法。
新正gapDelta=beta_*-sigma_circ不能写成旧signed beta_*-7/8来改变原count。
非floor实际bin有a<=beta_*及delta<=3/4，floor仍不强行要求witness。

源的common physical presentation、fixed Theta finite组合、zero-on-ramified main
slot、整体共轭和outside-S primitive inducing排除均与b无关。主slot实际g_i在
[0,delta/2]，error/zero slots g_i=0，q仍以全部ell长度为分母。whole-slot greedy
lower spike、每侧共同density和source的两个witness不变；没有用虚构prime因素
或任意row-dependent系数。strict labels与同一numerator联合只扣一次conductor deficit。

新供给满足5ell-h>1/50；zeta=Delta/32<1/384000使
ell/(h+zeta)>1/5>7/37且h+zeta<1。仅d>=1/2使用selected slots，因此w_i<=2ell_i。
先给count losses、nu_0、mesh和rounding，再取fixed even K，可使2ell/K满足全部
width/rounding/spare supply要求，actual O_K(1/log U) offsets最后由threshold吸收。
physical supports与internal plain pool仍有固定指数间隙。

inverse r_*>=23/37给第二marked width至少9/37；第一width由nu_0严格缩短。
plain用z<=z_P-nu_0得1-2m-6kappa z>=6kappa nu_0；z_P<=nu_0或r>=1/m>=1/2
改走source无槽版本，不能将趋零width代入marked theorem。所有S-supported exceptions
仅在bounded/small行出现并另付，未误塞进selected count。

对selected非floor，d-slope>=33/50-delta/2>=57/200>0，故[1/2,h]由endpoint控制。
floor直接R=1；middle原no-slot共同包络R=76/75-2delta/3覆盖floor，正slope使
[d_min,1/2]只须d=1/2。正文floor/middle/all-J Gram正gap均与候选数值吻合。
q<=delta/2且实际delta系数正，middle最大值取delta=3/4的步骤合法。

reference必须相对C_b(beta_*)。准确身份为E_beta(d)=E_sigma(d)-Delta；critical
E_sigma(h)=0不阻断反证。h到h+zeta仅花2zeta=Delta/16，给15Delta/16中央预算，
没有另扣7/8-sigma_circ或将新gap重复付费。

## 5. §6 Euler、principal及small/large rows

local table只涉及s,w,z及固定算术数据，几何b不进入其系数。sigma_circ>5/6给
D2*的所有分母一致离零。原完整defect而不是含1-W分母的错误式产生
c_b=sigma_circ-3/50>81/100、c_r=sigma_circ-1/20>82/100；正常收敛和全height
majorant真实成立。D1的theta=(-Re w)_+、epsilon_H=min(epsilon_0,1/50)保留。

一般row采用无商G_p完整tuple；只有已近one的dynamic/principal区域可除H_p。
whole-bin在global线上先移动，pointwise amplitude/witness labels后置。没有假定
待证sigma_circ已经是zero-free half-plane来调用reciprocal。

principal四错误幂仍是-s、-6z、4-5s-6z、1-w-6z，最弱衰减sigma_circ，
故B_p=-1+O(Q^(-sigma_circ))。target-independent正majorant选P0使H_eta近1；
target后扩大同一S只缩小majorant。所有表达式、c_S、A_T、H_eta均用同一final datum。
fixed-ray asymptotic、nonnegative窗和positive ell_i给A_T最终非零及subpower逆；
mu=sigma_circ ell/(2K)在K后选，真正满足mu<sigma_circ min ell_i。
主双留数仍w=1,z=1/6，1/L的principal s轮廓最后只向右至2，未跨target零点。
m_w=ly/20、m_z=h/600、mu三项余量全部正。

small实际用D1(1/3)，因为sigma_circ+1/2>4/3；没有将旧D1(3/8) statement
直接套入。h(13/75)-ly/2+63/5000<-2/25独立覆盖d<1/100及bounded units。
large绝对完整tuple在(2,2,z_infty)给B_0=7/4-3ell/4+b/4；先固定zeta>0，
再固定足够大z_infty，然后小loss和tail orders，仍是target前固定有限real box。
completed cn³ sums靠绝对收敛，有限的是compensation和retained annuli，并未混称。

## 6. §7共同Delta、参数顺序与全族反证

顺序正确：固定exact geometry/bootstrap/global Delta；以Delta支付central count、
capacity、mesh与rounding，随后K/windows；再选mu、amplitude widths、prime小幂与e。
principal另用其mu/m_w/m_z预算，floor/middle/small另用独立正margin。
即使mu远小于Delta，也无需用mu回选pre-K mesh；central剩余大于m_0/2，
principal及各外行亦保留至少m_0/2，故共同m=m_0/4的合同(28)有充分余量。

所有real exponents、zeta、z_infty、e、moment losses及槽系统先于target。
target后确定arithmetic data和同一S，再固定internal moment/Sobolev/seminorm阶。
原smooth calculus和external contour tails保证A_eta、B_eta先于external N；
增加N只改变external test seminorm和threshold，不反过来重用internal moment。
retained变量只共用一次cumulative T1/2 allocation。

literal ceiling先固定；例如tau_(0,eta)=d_min epsilon_ht/(20(1+A_ht,eta))，
tau<=min(d_min/100,tau_0,m/(4(A_eta+1)))使T1<=U^(1/100)及所有detector
height假设成立。随后才选N_eta使B_eta-N_eta tau_eta<C_b(beta_*)-m/2，最后threshold。
sigma_hi=m_0/8全族共同，tau/N/常数/threshold可依target。
独立physical J_eta与同principal f_eta都不含T1，所以这不是换函数实现收敛。

low与逆A_T的总小幂omega=Delta/2，high共同saving=m_0/8；
epsilon_*=min(Delta/2,m_0/8)>0在target前确定，beta_*-epsilon_*>sigma_circ。
C_b斜率1，使445的Z->0右移、Fourier line2 identity、Mellin局部一致收敛
逐式重放。H_eta非零排除numerator cancellation。supremum无需attained，
某个target的零有Re rho>beta_*-epsilon_*，与它自己的reciprocal全纯延拓矛盾。

finite Euler factors在Re s>0非零；quadratic Dirichlet transfer与445相同。
strip内因子没有极点以抵消零，s=1的principal例外由L(1,chi_-3)>0另排除。
所以得到全部finite-order Hecke及全部Dirichlet的严格Re s>sigma_circ半平面，
不声称boundary line无零或AF比例提升。

全文未发现剩余实质缺口。PASS仅在正文确切[R]范围，逐前件重放和同物理合同之内。
本轮只新增本审查，不编辑449、旧notes、论文、math或Git。
