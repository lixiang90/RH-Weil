# 444 中央联合误差与全行节省独立审查

2026-10-07。审查人：progress_audit；非444及其中央联合误差推导的作者。结论：**限定 PASS [T/R]**。已全文读444、442、443及所需固定原源，未发现阻断444所声明结论的实质数学错误。PASS限于同一物理有限补偿表达式的联合central bound、实际count代入后的全部行区间saving及稿中指定的高度合同；不单独验收整篇外部算术来源，不在本报告完成445的continuation，也不是Lean或RH证明。

## 1. 版本绑定与原输入

本次主稿绑定：

| 文件 | canonical LF SHA256 |
|---|---|
| notes/444-joint-error-slots-and-uniform-central-high-saving.md | 47686e9b6b28239562e83e9ab5199349458fd19bf9abbe45cca67df8c876957c |
| notes/443-effective-kappa-and-actual-detector-capacity.md | 79bfb7f8770eb3865ccdfe0da416388b2182383bd425fd57b39f520b3fd59bc6 |
| notes/442-shared-contours-and-principal-signal-at-the-new-boundary.md | 87abb4dd86ccae9b8209e030606413ef2b8682631f9c4d9195afdd808ad1b6b7 |
| reviews/2026-10-07/hybrid-central-error-slots-and-high-saving.md | 3cd3f9ff46e38e76ae245a5123946992772cee163edcd0ecafe7718612c34c2e |
| reviews/2026-10-07/hybrid-shared-contour-extension-derivation.md | 07b9643b62e9e8e3f8d91150392f7c34f186b3a7546e49df880a0bb70ed68ff1 |

算法为CRLF及单独CR换为LF后对UTF-8字节计算SHA256。外部源只读：

E:\codex-build\math\preprints\The-Quasi-Riemann-Hypothesis-September-30-2026\build\paper.tex

固定提交adc7f1241b42e322a6451854ab7e4b4c146bf78a；canonical LF SHA256为42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3。下述原源行号绑定该版本。

主要检查位置：

| 输入及重放步骤 | 原源行号 |
|---|---:|
| global/buffered logarithmic control、删Euler因子 | 1531–1620、4250–4321 |
| 同源full tuple与dynamic有限分解 | 8707–8729、8852–8922 |
| off-row、ramified全表及联合conductor allocation | 8924–9049 |
| 原plain参数域、uniform mesh | 12492–12578 |
| 原prime bound、main/error幅度分箱 | 15015–15090 |
| whole-slot选择与实际count | 15110–15446 |
| central joint bound及实际g | 15774–15840 |
| floor与中间行 | 15843–15850、16146–16175 |
| finite windows、严格容量、损失与高度顺序 | 16238–16440 |

442的共享轮廓与outer接口及443的actualcount已有单独审查。本报告交叉阅读这些审查，并直接核对444合并时所需原前件；未将作者推导报告作为新增公理。

## 2. 动态商只在合法区域使用

444式(1)与原prop:probe-errors的通用实域完全一致，且该原命题没有固定ell=1/6前件。e固定后选P0，使slot primes满足\(|H_p-1|<1/2\)，因此dynamic retained points上\(B_p=G_p/H_p\)合法。444没有以此宣称一般join/global域的商全纯。

此前whole-bin移动用的是无商full tuple；随后才作式(2)的有限分解。physical supports在ray/masks前已不相交，故selected prime每次仅被操作一次。unselected factor估计来自大于等于一的正Euler majorant，删selected factors不要求复杂乘积的模具有单调性。main项保留原physical row、ray restriction与zero-on-nonunit mask；特别是\(p\mid u\)时main仍为零。

因此式(2)没有更换原物理对象，也没有预先对contour-dependent amplitude sets分别延拓。

## 3. 联合error slots只使用一次numerator导子

off-row四指数逐项核对原8924–8938：

\[
-a-4e,\quad-51/25+12e,\quad49/25-5a-68e,\quad
a-51/25+12e.
\]

在\(51/100\le a\le1,\ 0<e<10^{-3}\)中均不大于\(-51/100\)。每槽\(O(P_i)\)个理想及\(Q^{z-1}\)给\(P_i^{z_0-51/100+\epsilon}\)，强于central scale。

ramified表不能用off-row式代替。444保留全部五个valuation分支，e=0幂及其e改动与原8947–8953一致。所有非strict boundary项严格小于\(-1/2\)；common R、V geometric tails及explicit rescaling项也保留该界。\(p\mid u\) labels仅divisor-many，这些error项不产生正amplitude gain。

strict项确为\(j\ge2,\ (e_0,l,k,m)=(1,0,1,0)\)，其局部normalized幂只有\(-w_r\)。444没有逐槽强行把它改成\(-1/2\)。原reciprocity/CRT给primitive conductor在每个good ramified prime恰为一次幂；对整个distinct strict集合J0同时有

\[
q_{\mathfrak f_u}\ll_S q_{\mathrm{rad}(u)}
\le q_u\prod_{p\in J0}Q_p^{-(j_p-1)}.
\]

取\(A_*=a-1/2+6e>0\)后，一次functional-equation allowance与全部strict因素联合估计。identity

\[
-w_r-A_*=-1/2
\]

使每个\(j_p\ge2\)的strict因素得到所需central幂。恢复该selected prime的原Euler因子为一，因primitive character在该prime本已取零；其余删除radical成本至多\(U^{6e+\epsilon}\)。这正是原9005–9041的同时分配，而非每个error slot重复支付完整\(U^{A_*}\)。

式(4)(5)因此正确。empty I也只花同一个numerator bound。原buffer同时保留numerator与conjugate，反射点\(1-w\)的实部为\(a+6e\)，并共享累计height allocation。bounded非平凡units由outer small-row接口处理；moderate非floor没有把L′零当作actual L零。

## 4. 实际g与count没有偷换

main gains来自原上下幅度分箱，error slots定义\(g_i=0\)，不从error要求lower spike。q的分母是全部physical slots的ell1。因此

\[
\sum_i\ell_i g_i=q\ell_1,
\]

式(6)的base-Z gain为\(g=q\ell_1\)，不是\(dq\ell_1\)，也不是以positive slots总长重定义的q。

443的count实际使用same-presentation witnesses、whole positive slots、固定Theta系数类和两条严格marked widths。plain使用两份同一witness，故spike是第四幂。新supply由\(\ell_1/d\)支付；当\(d\le h_1+\zeta\)时仍大于1/5，严格超过最大inverse需求7/37。K固定前已选择uniform mesh及capacity decrement；fixed real annular offsets在严格余量后由阈值吸收。

原plain前件只允许\(\kappa\ge3/4\)。444正确接受原全Hecke7/8为明确[R] bootstrap，取\(\kappa_{\mathrm{eff}}=3/4\)，且\(\beta_*\le(1+\kappa_{\mathrm{eff}})/2=7/8\)。于是\(\Delta_{\mathrm{eff}}=0\)，没有把负的旧gap放入正capacity loss，也没有额外加\(\Delta_1/4\)。

all-error I、q=0可选空prime list；该case仍由实际witness/no-slot count覆盖，不虚构prime spike。floor独立用R=1，中间小d用actual no-slot count；不会对floor或缺少witness的bounded rows套用式(7)。

## 5. 连续端点证书与reference

独立重算式(8)：\(a=(1+\delta)/2\)、\(h=1-l_x+\ell\)、原\(z=1/6\)留数给

\[
K_\sigma=2/3+\ell+b/6-\sigma.
\]

沿\(\sigma(\ell)=11/12-\ell/4\)时，\(K=-1/4+5\ell/4+b/6\)。这一reference变化必须同时计入；444已如此处理。

式(9)已用BigInt精确有理双变量多项式运算独立展开：清除J分母后，左右差的所有\((y,\delta)\)系数为零。此计算验证的是显示identity，positivity仍由正文显式完成平方证明给出，不由有限采样代替。\(y\in[0,1/2]\)、\(\delta\in[0,5/6]\)时\(9-13y\ge5/2\)、\(v\le17(3+5y)\)、\(0<J\le5/2\)，故\(-E_0\ge49/440640\)。

\(2D_x-3P_x=4x(11-6x)/9\ge0\)确给\(1-\delta\le R_*\le1-2\delta/3\)。对于同一\(\delta,q,R_*\)，新旧端点差为

\[
t_0(-1/4+\delta+q+3R_*/2)\le5t_0/3.
\]

因此式(10)精确margin为\(307/11016000>0\)。已相对\(C(\sigma_1)\)记账，不能再扣1/80000；比较\(C(\beta_*)\)仅使指数再减正的\(\Delta_1\)。这与稿中说明一致。

## 6. 全物理d覆盖及精确余量

selected非floor区间的slope至少\(33/50-\delta/2>0\)，所以端点包络覆盖每个实际d，不要求同一actual pair在端点dyad实际出现。floor的slope为67/100，独立margin为\(-4327/750000\)。

中间\(d_{\min}\le d\le1/2\)用共同R=\(76/75-2\delta/3\)，既覆盖floor又覆盖非floorno-slot上界。slope为\(101/150-\delta/6>0\)，沿reference路径的变化系数为\(13/50+\delta/4+q\le177/200\)，所以式(12)为\(-120907/36000000\)。该中间结论没有延伸到\(d<d_{\min}\)。

固定\(\zeta=m_{ad}/32\)确小于\(5\ell_1-h_1=2521/120000\)及\(1-h_1\)；actual supply保持严格。以2保守界全部extension slopes后，只花\(m_{ad}/16\)，剩\(15m_{ad}/16=307/11750400\)。

outer小行单独用442的\(D_1(1/3)\)、完整selected G及unselected正majorant，margin为172249/2000000；bounded nontrivial units包含在其中。outer大行先固定正zeta，再选固定\(z_\infty\)足够大，获得指定saving。大行最终估计使用统一absolute tuple bound，不依赖临时fixed-dyad移动常数。上述区间合起来确实覆盖全部physical row norms。

## 7. 损失、内部阶数与高度合同

444的顺序与原source 16238–16440相容：

1. fixed geometry/bootstrap及requested count loss先确定，再选capacity decrements、uniform moment mesh与rounding预算。
2. 随后选fixed K和windows。mesh依赖bounded length ranges与loss而不依赖target或slot count；internal smooth/height阶数可依赖最后固定的slot count。
3. positive min ell_i已固定后，才选amplitude width、prime-bin small powers、e及detector pre-saturation参数。不能在K之后反向缩早已需用的moment mesh。
4. target确定后固定arithmetic datum、Theta、internal Sobolev/height阶及A_eta、B_eta。共同cumulative frequency allocation在全部调用中保留。
5. literal height ceiling及tau在external tail order前固定。提高external order只改变外部test seminorm常数和阈值，不再次调用internal moments，也不增大其已固定A_eta或full-tuple degree B_eta。

central显式real losses在固定d范围中系数有界。finite subsets、amplitude bins为固定乘数，dyadic/witness multiplicity仅固定log powers；分配任意小幂后可以把总损失及一次inverse normalizer成本压到\(m_{ad}/4\)内。principal合同另使用442已经支付的新local decay \(\sigma_1\)，不是沿用未经付款的7/8衰减。

因此式(14)可作为保留analysis height的同源high合同。其physical expression、signal与normalizer本身没有T1；此处尚未完成late-height closure、低界合并及continuation。A_eta和B_eta独立于随后选的external N是合同中的真实量词要求，不能删去后直接任意优化T1。

## 8. 限定结论

当前绑定稿无需数学修正。新解析合并已在明确[R]前件下支付：一次联合conductor deficit、mixed main/error实际g、actual row count、连续端点margin、floor/intermediate/outer覆盖及正确reference均一致。

所保留[R]包括原probe/Poisson与局部算术identity、ray-prime输入、finite-order Hecke反射/增长/global和buffered reciprocal、actual witness、marked/plain/recursive moments及sixth-power amplification，另有原全Hecke7/8 bootstrap。本报告没有把这些外部证明替换为有限数值审计；没有用AF比例减少坏行数，没有声称新signed fourth-trace常数改善，也没有认证Lean、RH或新的几何算术正性桥。

本次仅新建本报告，未改444、旧稿或math仓库，未构建、提交或push。
