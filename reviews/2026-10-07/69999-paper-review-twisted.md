# 69999/80000 正式论文独立全文审查

2026-10-07。审查人 twisted_research。**限定 PASS。** 直接阅读全文及冻结前新增的
完整反射能量式、局部表、实际capacity分支和共同参数合同，并对照原source。
本审查范围严格为441–445的69999/80000结果，没有加入447或后续critical研究。

审查对象：`papers/seven-eighths-boundary-improvement-paper.tex`。
最终版本 canonical LF SHA256（CRLF及单独CR换为LF后UTF-8）：

`92ba93da7cc568579b0b982bcd712e1382af749d05460c1fa4c8b25064df66d6`。

独立核对最终版仅在appendix前加入一行`\clearpage`；删除该行后准确恢复此前
已全文审查的数学冻结哈希`fa5a031ae40980c729aef83f272f9aa4dc77ce0295f4a5a49e21a36ad7fe772d`。
这次版面修改不改变下述数学审查结论。

在正文明确假定的 imported package R、其原全Hecke7/8 bootstrap及本稿逐前件
扩域范围内，参数选择、实际同物理low/high、late-height与全族Mellin反证闭合。
未见剩余实质缺口。本结论不认证外部原稿整条算术/分析链，不是Lean
elaboration、kernel、Comparator或RH证明。本报告审数学源，不验收PDF版面或编译。

## 1. 来源、绑定和条件结论

原source：OpenAI/math提交 `adc7f1241b42e322a6451854ab7e4b4c146bf78a`，
`E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`，
canonical LF SHA256：

`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`。

论文Definition R和Theorem main均明确写“Assume R”；摘要亦说明是cited-input derivation。
R含原coefficientwise probe/Poisson和local tables、smooth calculus/Gaussian annuli、
reflection sectors/generic reflected energy、additive Gram、global/buffered reciprocal、
Hecke增长与functional equation、detector witnesses、marked/plain/inverse/recursive
moments及sixth-power amplification、uniform mesh、fixed-ray prime asymptotic和
原全primitive finite-order Hecke7/8 theorem。没有把固定函数AF比例作为新的行数假设。

论文陈述的是F=Q(sqrt(-3))的全部有限阶Hecke及全部Dirichlet L在strict
Re s>69999/80000无零，允许principal pole；未对boundaryline或RH作断言。
本文不认证R本身正确性。引用checkpoint
`96fcb27a0b8788ad8a346238843906bce0285479`在本地存在，含445文件。

逐前件已核的441–445版本：

| 稿件 | canonical LF SHA256 |
|---|---|
| 441 | `dffcaa1899358d581fe3d6438ee87d075588e5e7e8f41ccd8a629fe5c31be0dd` |
| 442 | `87abb4dd86ccae9b8209e030606413ef2b8682631f9c4d9195afdd808ad1b6b7` |
| 443 | `79bfb7f8770eb3865ccdfe0da416388b2182383bd425fd57b39f520b3fd59bc6` |
| 444 | `47686e9b6b28239562e83e9ab5199349458fd19bf9abbe45cca67df8c876957c` |
| 445 | `99ac005976c7c22934b5597c25b0d6fc6d7f3f4d9be604f8cbd53e130eae0f2e` |

关键原source位置为373–502（全族supremum/continuation）、3327–3412（same S及
independent probe）、6868–6912（准确finite compensation）、4013–4067与8707–9049
（局部表及full tuple/joint conductor）、7663–7804/8340–8364（通用low输入）、
4385–4547/9220–9269/12362–12578/15015–15446（actual detectors）、
6174–6301（principal）、6520–6580及16191–16453（参数/height）、6715–6780（transfer）。
本轮重新读取physical probe/compensation及原参数、Mellin、principal和transfer原文；
其他通用输入按此前已保存的逐源独审交叉核对，不以原fixed low/high theorem覆盖新参数。

## 2. 物理表达式、完整局部表和same S

论文eq:physicalsum与source6894–6902逐项一致：J是rescaled subset，系数
(-1)^|J|q_pJ^(-3/2)bar eta(p_Jc)，参数是
(X/q_pJ,Y/q_pJ,Z q_pJc)，标记仍为p_Jc|cn³。
每个window保留原P_i尺度；没有因另一个marked operation改变Z就重算slot windows。
同一original arithmetic masks、ray calibration、允许shared primes保留。
高积分由已独立定义的完成probe导出，未被用来重新定义一个方便的函数。

完成cn³行是initial Mellin line上的绝对收敛和；有限的是outer annular m,s以及
prime tuples/subsets的补偿。最终稿正确区分了二者。

原full local table的j=0,…,5、W_loc和W已分清；ramified p|u时D=W=0而
W_loc保留相位。Defect identity没有1−W分母。Good bound在一般域保留
theta=(-w_r)_+；D2*上theta=0。
第一域的实际margin为eps_H=min(eps0,1/50)，没有误称任意eps0都可直接用作
Euler衰减。D2*的新c_b=65199/80000、c_r=65999/80000严格正。

完整selected tuple不除以P_p/H_p；一般joins及global domains只用这个表达式。
仅在principal或retained dynamic域以positive tail确保local H_p非零后才用商。
Principal四error幂确以sigma1为最弱衰减，未偷保留旧7/8。

目标前选择P0和原固定T；目标后扩大S只删positive majorant因子。
最终同一个S用于probe、high身份、c_S、A_T、H_eta及f_eta。
Fixed-ray正窗渐近给A_T最终非零、inverse为任意subpower；有限追加S只改threshold。
原source3327–3343直接支持T不随S扩大而改变。

## 3. Low、实际counts及全physical高界

新增的反射能量full formula和两分支saving identity经直接代数核验一致。
在s_hyb不取z_a的分支，s_hyb>=v/2，再以y=v+3ell_b+e_lambda得到
rest>=Td/4−small loss；不是删掉正row loss。
Td−(H−3d_J)<=2eps_Z+|theta_N|保留实际residualdyad、powerful fixed parts
和shared primes。第二saving identity的剩余项2A0−N0+B0+4S0非负。
结合generic Gram和原Q球，tuple净费准确为
−d_J+(5ell−1+d_J)_+/8<=−7d_J/8。
故variable low指数为C(sigma1)=14999/80000，而非沿用固定geometry low定理。

Actualcount固定kappa=3/4合法，因为beta_*<=7/8；signed beta_*−7/8没有用于
容量loss。原sixth-power slope5/6不随ell改变。
Inverse/plain两分支各自请求减去nu0的strictwidth；第二inversewidth有9/37独立余量。
Zero capacities使用no-slot；floor使用R=1，不请求一个未保证存在的witness。

幅度定义用actual positive bins上下界，g=0覆盖errors和|Q_i|<=1的main因素。
q以全部slots长度加权；平方spike为2q，未发生factor-of-two或重分母错误。
相对psi的prime coefficients是bar nu(p)1_T的有限Theta组合；整体共轭保留系数类、
masks和支持。Inducing exceptions最终从selected大U范围消失，仍由outer小行保留。
Mesh先于K，whole-slot rounding只丢一个fraction；physical prime windows与plain内池
由明确fixed exponent gap分离。Source actualcount前件没有替换成任意名义行。

所有strict ramified labels共同使用一次numerator conductor deficit；j>=2时
−w_r−A*=-1/2正确。Restoring strict factors成本1。Errors记g_i=0，全部I包括emptyI
统一覆盖；pointwise partitions在whole-bin移线之后进行。

连续certificate是显示完成平方identity，不依赖网格外推。
m_ad=49/440640−1/12000=307/11016000已经相对C(sigma1)，比较C(beta_*)只再减
Delta1一次。d∈[1/2,h]斜率正；floor、中间no-slot、U<Z^dmin和U>Z^(h+zeta)
各有独立界。Bounded非principal units不被中间witness冒充覆盖。
zeta=m_ad/32的上端成本至多m_ad/16，supply及h+zeta<1保持。
以上覆盖全部physical rows，而非只核h端点。

## 4. 参数顺序及共同高界合同

正式稿的选择顺序无循环：固定global Delta1和low loss；然后用m_ad的固定份额
选count/moment losses、capacity decrements、uniform plain mesh、rounding；再选
fixed evenK与原disjointwindows；之后才选mu=sigma1 ell/(2K)、amplitude与prime losses、e。
Mu不能倒用于需要先于K的mesh；本文没有这样做。

Central extension与real costs后余量>=m_ad/2；principal三项分别由m_w、m_z、mu
支付，outer小行另留一半，large line先于target固定到所需余量。
统一m0=min(m_ad,m_w,m_z,mu,172249/2000000)>0，m=m0/4在target前固定。
之前central预算不必回缩成m0，因为其剩余已经>=m0/2。

Target后固定最终S、Theta和全部internal Sobolev/seminorm/moment orders，得到
有限A_eta、B_eta及detector ceiling，均先于externalN。
实际J_eta=I_mod/(c_S A_T)与实际principal f_eta不含T1；只能估计依赖T1。
所有频率共享原singlecumulative T1/2矩阵预算，不能重复扩大buffer。
因此eq:highestimate确符合原late-height lemma的合同，而非仅形式上的幂比较。

Tau0按dmin eps_ht/[20(1+A_ht,eta)]定义，U>=Z^dmin使literal detectorheight条件成立。
随后目标后选tau_eta，再选N_eta，再增threshold。增加N只改变external seminorms，
不重做内部moment，也不改变A_eta、B_eta或real powers。
最终sigma_hi=m/2=m0/8与目标无关；tau,N、constants和threshold可依赖目标。

## 5. Mellin continuation、supremum和quadratic transfer

Low和inverseA_T可指定任意小幂，在target前合计取omega=Delta1/2。
epsilon_*=min(Delta1/2,m0/8)>0与目标无关，且epsilon_*<Delta1，
所以beta_*−epsilon_*>sigma1。完整beta_*定义保留{1/2}、实际primitive finite-order
Hecke零族及poles excluded；没有以一个固定L的高度比例代替共同supremum。

Principal只把main residue向右移到2，没有跨目标zero。小Z也只向右移到B>2；
Gaussian、boundedH及absolute reciprocal使horizontal joins消失。
两端界保证Mellin局部一致收敛；line2 arithmeticfunction连续可积，Z=e^u后的函数
也可积，ordinary Fourier inversion识别同一个H_eta/L_F^S，再由identity theorem到Re>1。
|H_eta|>=1/2使它给全纯reciprocal延拓。

共同epsilon_*先确定后，supremum定义才选一个实际target zero；不要求supremum达到。
Deleted factors在Re>0非零。Principal s=1 pole使reciprocal有zero，不形成额外阻碍。
这正是source400–502允许任意sigma0∈(1/2,1)的通用criterion，未暗用旧7/8下界。

Primitive/imprimitive恢复只乘有限非零因子。Quadratic transfer沿source6715–6780：
split/inert Euler factors先在Re>1相等，再meromorphic continuation；strip内两Dirichlet
因子全纯，s=1+it、t非零也无pole；s=1唯一pole-zero可能由
L(1,chi_-3)=pi/(3sqrt3)>0排除。因此全Dirichlet与zeta的strict边界声明准确。

## 6. 审计和未认证范围

附录有限审计输出确记录16,728 finite-frequency cases；其scope明确仅检查显示
代数，不认证analytic hypotheses、infinite contours、physical identities或external Lean。
本文也以连续identity而非audit网格承担无限正性。上述限制与正文R一致。

初审指出的完成和有限性、D1 eps_H、q的幅度/平方区别、零幅度bin、完整beta定义
及原window scales均已在本版本修正。无剩余阻断问题。
本报告限定PASS为所绑定数学source的引用输入证明；编译、PDF布局、push及其manifest
由主任务另行处理。外部来源整链正确性与本改进的形式化不在PASS内。
