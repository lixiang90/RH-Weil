# 447. 更大槽判别式、临界参数及全族共同gap的付款

2026-10-07。状态 [T/R]：引用445逐条列出的原通用算术/分析结果与全Hecke7/8bootstrap，
将同源可变几何推进到一个精确代数临界参数。不是外部原稿整链或Lean kernel的独立验收。
关键是high须相对C(beta_*)比较；相对C(sigma)的附加负余量可以为零。
AF简单临界线比例没有用于本稿的坏行count。

## 1. 固定来源与结果

原[OpenAI/math September-30 paper.tex](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)，
提交adc7f1241b42e322a6451854ab7e4b4c146bf78a，canonical LF SHA256
42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3。
通用low、完整physical high identity/contours、actualcapacity/counts、joint errors及continuation
分别是441–445已逐前件重放的接口。这里只支付新参数，不调用原fixed-geometry low/high定理。

令t_c为

\[
 q_0(t)=28224-164747520t-669772800t^2=0
 \tag{1}
\]

的唯一正根，明确地

\[
 t_c=\frac{56448}{164747520+
 \sqrt{164747520^2+4\cdot669772800\cdot28224}},
 \qquad\frac1{5842}<t_c<\frac1{5841}<\frac1{5800}.
 \tag{2}
\]

在上述确切[R]前提下，本稿得严格半平面

\[
 \boxed{\Re s>\sigma_c:=\frac78-\frac{t_c}{4}
       \simeq0.874957200615374}
 \tag{3}
\]

中全部有限阶Hecke L（F=Q(sqrt(-3))）及全部Dirichlet L无零，principal极点允许。
小数仅定位，证明使用(1)(2)的代数值。
另一个完全有理且有额外负余量的参数为t=1/5900、sigma=20649/23600；
其endpoint margin大于10^{-6}。
不对边界本身作无零断言，也未证明RH或更高零点比例。

## 2. 保留同源几何与实际count

对0<=t<=1/5800固定

\[
 \ell=1/6+t,\quad l_x=17/48-t/2,\quad l_y=23/48-t/2,
 \quad h=13/16+3t/2,\quad \sigma(t)=7/8-t/4,\quad b=1/8.
 \tag{4}
\]

主留数仍是w=1,z=1/6，C(s)=s+l_x/2-1+h/6=s-11/16。
Low交点为C(sigma)=(1-ell)/4-b/6；ell仍在441的[1/6,1/5]范围。
保持原finite compensation、S,T,xi、Gaussian、masks、zero extensions及disjoint slots。

反证beta_*>sigma(t)时，原7/8bootstrap给
Delta=beta_*-sigma(t)>0、Delta<=t/4。
443合法固定kappa_eff=3/4、Delta_eff=0。
每个非floor actual bin有delta=2a-1<=3/4；代数包络仍用alpha=5/6。
Error gains为0，q是所有slots的length-weighted mean；x=q/delta∈[0,1/2]。
令y=1/2-x，保留已准入的actualcount

\[
 D=(37+34y)/18,\quad P=(7+18y+8y^2)/9,
 \quad J=(\alpha-\delta)D+\delta P,
 \quad R_*=1-\delta+\frac{(\alpha-\delta)\delta P}{2J}.
 \tag{5}
\]

0<J<=5/2且1-delta<=R_*<=1-2delta/3。
这些函数不依赖t；actual供槽及所有strictwidth、系数类与family前件在§5重新核。
444的joint-error proof给g=qell，使用一个numerator的conductor deficit一次。

## 3. 连续判别式证书

将(4)(5)代入原同源Mellin幂，d=h的指数相对C(sigma(t))为

\[
 E_t=-1/48+5t/4-(1/16+y/6+ty)\delta
 +(13/32+3t/4)(\alpha-\delta)\delta P/J.
 \tag{6}
\]

直接清分母得p_t=10368J(-E_t)=A_t(y)delta²+B_t(y)delta+C_t(y)，其中

\[
 A_t=2448+6288y+4512y^2+1536y^3
      +t(6048+2304y+8064y^2+9216y^3),
\]
\[
 B_t=-1896-3016y-208y^2+t(11520+3360y-960y^2),\qquad
 C_t=370+340y-t(22200+20400y).
 \tag{7}
\]

Q_t=4A_tC_t-B_t²的y^0,…,y^4系数为

| i | q_i(t) |
|---|---|
| 0 | 28224−164747520t−669772800t² |
| 1 | 1198848−664266240t−775526400t² |
| 2 | 5344448−877278720t−893260800t² |
| 3 | 7154944−484362240t−1469952000t² |
| 4 | 2045696−113203200t−752947200t² |

当0<=t<=1/5000时，i>=1系数分别大于10^6、5·10^6、7·10^6、2·10^6。
在0<=t<=t_c，q0>=0、A_t(y)>0，因此对所有y>=0、delta∈R有

\[
 p_t=A_t\left(\delta+\frac{B_t}{2A_t}\right)^2+\frac{Q_t}{4A_t}\ge0.
 \tag{8}
\]

在真实rectangle上J>0，所以E_t<=0。这是连续多项式正性，不是网格外推。
Critical t=t_c时，唯一等号要求y=0及delta=-B_t(0)/(2A_t(0))；
该delta位于(1/50,3/4)。等号属于已准入count的包络，不声称物理坏行达到它。

### 有理严格余量

取t=1/5900，N=5900，A_N=N A_t、Q_N=N² Q_t。
A_N系数为(14449248,37101504,26628864,9071616)，
Q_N系数为(9797299200,37811952537600,180863397171200,246204393472000,70542025932800)。
A1<=3A0、A2<=2A0、A3<=A0，Q1>=3Q0、Q2>=2Q0、Q3>=Q0、Q4>0。
故A0Q_N-Q0A_N逐系数非负，得到

\[
 p_t\ge Q_N(0)/(4N A_N(0))=85046/2960089,
 \qquad -E_t\ge42523/38362753440>10^{-6}.
 \tag{9}
\]

这一步证明Q/A的ratio下界；没有误把A(0)当成A(y)的上界。
几何为ell=2953/17700、lx=25069/70800、ly=33919/70800、h=19181/23600、
sigma=20649/23600、C(sigma)=553/2950。

## 4. Critical共同gap与全部物理频率

从此固定t=t_c、sigma=sigma_c，在反证beta_*>sigma_c下工作。
真正high参考幂是C(beta_*)，故

\[
 E_{\beta_*}(d)=E_{\sigma_c}(d)-\Delta,
 \qquad\Delta=\beta_*-\sigma_c>0.
 \tag{10}
\]

§3的E_sigma(h)<=0遂给E_beta(h)<=-Delta。
不能因附加E_sigma margin为0就认定high无法关闭；
Delta是全角色族共同量，在目标前固定，允许所有real budgets依赖它。

Selected nonfloor 1/2<=d<=h的slope为
R_*+delta/2-17/50>=33/50-delta/2>0，故endpoint控制全区间。
Floor独立取delta0=1/50、R=1、q<=1/100。
No-slot中间d_min=1/100<=d<=1/2取共同actualuppercount R=76/75-2delta/3。
它们的slope分别67/100及101/150-delta/6，均正。
利用t_c<1/5800，分别有相对C(sigma_c)的准确包络

\[
 E_{floor}(h)\le-7/1200+(32/25)t_c<-1/200,
 \qquad E_{middle}(d)\le-49/14400+(177/200)t_c<-2/625.
 \tag{11}
\]

固定zeta=Delta/32。它满足zeta<=t_c/128<1/(5800·128)，
而5ell-h=1/48+(7/2)t_c>1/48，故actualsupply保持ell/(h+zeta)>1/5>7/37，h+zeta<1。
Upperextension slope保守界2，故成本<=Delta/16。
Selected high相对C(beta_*)仍至少15Delta/16节省；floor、中间另有独立负余量。
No-slot只说不把槽用于row moment，所有槽仍在full correction中。

Outer小行的完整442证明在global(beta_*+e,1/2,17/50)上用D1(1/3)，
相对C(beta_*)的指数为

\[
 -79/800+(51/100)t_c+63/5000<-2/25.
 \tag{12}
\]

它支付bounded nontrivial units与d<d_min；不以中间count覆盖它们。
大行先固定zeta，再在目标前固定足够大的z_infty，使442的绝对fulltuple总和
达到至少Delta的节省。All-height degree在后选external order之前固定。

## 5. 新参数的实际解析、low及capacity准入

Low由441的整个1/6<=ell<=1/5 theorem，所有rescaled subsets、actual residualdyads、
正row loss与tuple亏损均原样保留。不是以参数连续性猜测旧low结果可用。
Actualcount的443证明只另需(5)的compact ranges、供给与fixedmesh；
当前kappa=3/4合法，strictwidth第二条仍有9/37独立下界，zero capacities走no-slot。
Greedy wholepositive slots、固定Theta coefficients、整体共轭、inducing-family exceptions、
zeroextensions及内部pool分离均保留，选择时仍只d>=1/2、w_i<=2ell_i。

444的dynamic域a+16e、1-a-6e、17/50与conductor联合分配不含固定ell。
新K固定后可重新分配有限error-subset losses，g仍为qell。
Whole-bin move在pointwise partitions前完成；完整contour身份不以商定义一般H_p。

新sigma_c>7/8-1/23200>5/6且>401/600。
442局部证明在D2*(sigma_c)给positive-product margins
c_b=sigma_c-3/50>81/100、c_r=sigma_c-1/20>82/100；
principal四error幂的最弱衰减仍为sigma_c。
Outer域sigma_c+1/2>1+1/3。故D1/D2*全纯、全heightmajorant、principal B_p=-1+O(Q^{-sigma_c})
逐项重放，H_eta在Re s>sigma_c可统一近1。
P0在目标前选择；后加目标固定excluded primes仍缩小同一positive majorant。
不借待证新zero-free half-plane来取得这些解析域。

Fixedray asymptotic使同一个A_T最终非零、逆为subpower。
主留数余量为m_w=l_y/20>0、m_z=h/600>0和任意mu<sigma_c min ell_i。
所有physical sums、c_S,A_T,H_eta与signal使用同一个目标最终S。

## 6. 完整参数顺序、lateheight与continuation

先固定critical geometry、bootstrap与Delta；以Delta的fixed小份选count/moment losses、
capacity decrements、rounding及uniform plain mesh，再取fixed even K和原disjointwindows。
此后才选mu=sigma_c ell/(2K)>0、amplitude宽度、prime preliminary小幂与e。
Central real总loss、logarithmic multiplicity、normalizer allowance取小于Delta/4。
Principal三项分别loss小于m_w/4、m_z/4、mu/4；
floor/mid/small的loss各小于其独立margin的一半。
Zeta和z_infty也在目标前固定；K无需由尚未固定的mu倒选。

令

\[
 m_0=\min\{\Delta,m_w,m_z,\mu,1/200,2/625,2/25\}>0,
 \qquad m=m_0/4.
\]

此前central剩余>Delta/2>=m0/2，principal/outer同样留>=m0/2。
Target后固定最终arithmetic data与internal Sobolev/height orders，得到finite A_eta、B_eta，
以及原literal detector height ceiling tau0,eta>0；它们不依赖external N。
所有频率使用singlecumulative T1/2 allocation。
同一physical J_eta=I_modified/(c_S A_T)和principal f_eta均无T1，得到

\[
 |J_\eta-f_\eta|\ll_{\eta,N}
 Z^{C(\beta_*)-m}(1+T_1)^{A_\eta}+Z^{B_\eta}T_1^{-N}.
 \tag{13}
\]

445的ceiling与lateheight选择按同式重放：
tau_eta<=min(d_min/100,tau0,eta,m/[4(A_eta+1)])，
再选N_eta使B_eta-N_eta tau_eta<C(beta_*)-m/2，最后threshold。
得target-independent sigma_hi=m0/8>0。
Low与inverseA_T的小幂合计取omega=Delta/2<Delta，故low合同亦满足。
Epsilon_*=min(Delta/2,m0/8)>0在目标前固定。
445的小Z rapiddecay、Mellin/Fourierline识别、H_eta非零以及全族supremum反证逐式成立，
无需supremum达到；故beta_*<=sigma_c。
Finite Euler deletion、quadratic factorization及s=1 principal例外按445转移到全部Dirichlet L。

## 7. 本参数族的包络边界及下一真正改进点

t=t_c是固定b=1/8、原R_*与amplitude矩形下E_sigma严格负的极限；
本稿说明零附加margin的critical参数仍能借全族Delta付款。
不是所有possible detector或L函数理论的最优性结论。
例如t=1/5800、y=0、delta=57215/147963、q=delta/2给
p_t=-29297/1430309、J=2164165/1775556，E_sigma=29297/18075106080>0。
Delta可任意小，因此这个正包络不能一律由Delta支付。
该代数见证不证明实际badrows达到包络，亦不证明有相应L零。

进一步边界改进应利用真实count/gain关联或调几何，而不是把附加margin=0误作延拓失败。
比例方向446仍只给T-growth的四迹弱界；当前真实算术对象是232–240的
high-product、共同centered Möbius divisor及adjacent-divisor response。
独立参数推导见[优化报告](../reviews/2026-10-07/hybrid-next-boundary-certificate-optimization.md)；
连续判别式的精确代数与来源的无限分析/Lean验收分别记录。
