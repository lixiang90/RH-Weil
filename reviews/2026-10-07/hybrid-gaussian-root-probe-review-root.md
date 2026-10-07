# Gaussian 实际root probe：根节点全文审查

2026-10-07。限定 PASS；本报告核准实际 Poisson恒等式、good-prime局部表、
共同符号的窄raw二矩与sign-adapted双hop。完整任意target完成、critical raw
supremum、marked/plain全预算和新无零区域仍未证明。被审稿最终SHA与
全文独审统一绑定于[本轮检查点](root-probe-and-fourth-checkpoint.json)。
最终被审稿 canonical LF SHA256：
`4a6b33cae1944bc904216c202a62f04d48d2f47b0ff5a852f13a3af5a063bc3d`，
30381 UTF-8 bytes，保留终结LF。最终两处仅状态与显式dyadic支撑前件，数学不变。

实读[被审报告](hybrid-gaussian-root-weight-probe-research.md)全文，并核对
[已提交Gaussian来源报告](hybrid-gaussian-quartic-feasibility-research.md)、
[457](../../notes/457-number-field-choice-and-relative-amplification.md)的前件，
以及[DDHL v5 §3、§4.4–4.5](https://arxiv.org/html/2306.11875v5)。
另两份独审为[radial](hybrid-gaussian-root-probe-review-radial.md)、
[twisted](hybrid-gaussian-root-probe-review-twisted.md)。

## 1. 实际配对、归一化与unit dual

Re(zw)配对的Gaussian lattice自对偶。residue a+nO的dual是k/n；
F(βh/sqrtH)的Fourier变量因此为sqrtH k/(βn)，Jacobian为H。
β=barα(n)给βn=|n|，使所有n方向统一；不是用未知径向反射来替代
真实角窗口。DDHL trace2与该Re配对差一个2：变量1/2换元严格给
G_star,j=χ_n(2)^j G_j，原coefficient的χ_n(2)^(-j)正好抵消。

squarefree γ1²=mu α来自已核准split/inert prime与CRT，不是本轮用
有限样本猜测。原j=1 probe乘root weight γ1 barα后，Poisson得到
H mu η/Nn及χ_n(k)^(-1)，保留相同target η和全部非互素自然零。
两边的Schwartz sums均绝对收敛；若要求有限h截断，报告已限定H=X≥2，
不作任意超多项式H的未付款uniform尾声明。

H=X、Nn∈[X,2X]时，k=1落在real segment[1/sqrt2,1]。所有k≠1
到该segment的距离至少sqrt2−1，包括k=0、另三个单位和两端点。
固定Fourier bump的tube半径1/4因此准确隔离k=1，不用有限样本外推。
W(t)=tV(t)给精确原target Möbius和。F通常复值非径向；这只证明
可实现的实际probe和读出，尚无cancellation estimate。

## 2. 局部valuation与平方指标候选的边界

modulus π²而character只依modπ时，lift求和先强制numerator被π整除。
valuation1剩q倍finite-field Gauss，非principal character在valuation≥2
时为0；principal-zero-extension分别为−q和q(q−1)。四个twist分支
与报告表相符。成功的quartic分支把effective modulus降回n，不提供
新square-index automorphy。

一般modulus π^L的G4依character exponent L mod4：nonprincipal
conductorπ只在vπν=L−1非零；principal exponent0给Ramanujan分支，
vπν≥L时为φ(π^L)。由此逐式核准(6.5)及列出的powerful例子。
ν=2h³且h的odd部分squarefree时，oddπ|h只允许L=4，normalized系数
为−q，因此local factor为1−q^(1−4s)απ^(-4ell)。其它good primes
只留L=1，残余仍为quartic χ_c(h)。π=λ不在odd modulus family，
不能放进该Euler product或直接调用odd cube-coefficient vanishing。

natural square-map候选在χ(-1)=−1时由±y配对恒零；在q≡1mod8时
pushforward分成两order8 rows。它未产生所需quadratic终端。
这些只排除指定候选，不排除所有Gaussian新设计。

## 3. 共同符号窄raw二矩的真正付款

固定数量的disjoint once-prime slots使expanded column m=n∏p_i
的local exponents只有1或2。同一ε符号下分别为primitive quartic
或quadratic，所有zero masks保留；不同m给不同primitive characters。
同m的不同decompositions用divisor multiplicity付款，实际dyadic
sum1/Nn和sum1/Np有界，故列能量仅费T_col^eps乘显式slot权重。

同conductor的不同characters必须先合并Gauss coefficients再用字符
正交性：能量恰为φ(c)/Nc乘原能量。报告做了这一步，没有先作ℓ1相加。
primitive有限Gauss identity在非单位numerator也成立并为零。

reduced Gaussian fractions的torus距离≥1/T_col。positive Gaussian
majorant在Nu≤U上离零，Poisson核为πU乘periodized Gaussian，非负。
δ-separated lifted points用disjoint disks计数≤C(1+r/δ)²，径向
积分给Schur row sum≤C(U+δ^(-2))。因此完整additive width为
U+T_col²；结合已付能量即实际(7.2)，无需untwisted或arbitraryη FE。

η只作为modulus≤1的系数，故此窄界对任意finite target和固定height
phase有效。常数依固定slot数量/profile；不升级为源的全部参数合同。
mixed-sign overlap指数可能0，primitive证明不能直接套用；报告正确
限定共同符号。n=p的归一化coherence例只说明individual-energy证明
需重建，不能独自反证粗U+T_col²界。

## 4. 双hop降低row conductor的实际恒等式

根节点独推、另两位审查者分别核对：γ3=χ_n(-1)barγ1，所以
γ3²=mu barα。取j=−ε mod4∈{1,3}，σ1=1、σ3=−1，root weight
c_j=χ_n(2)^(-j)γ_j α^(-σ_j)，物理hop用χ_n(h)^j。
Poisson后的Gauss乘积始终为mu，unit dual始终保留ηχ_n(u)^ε。

物理n-column为G_j(2h³u,n)，因为−3j≡j和−j≡ε mod4。
两incoming方向因此都有linear row numerator，Nν=4 Nh³ Nu；原固定
正hop在正incoming方向的Nu³成本确实可以避免。这是新的局部/physical
构造进展，不能等同于quadratic终端或critical moment。

对全部odd modulus，G3(ν,c)=χ_c(-1)overlineG1(ν,c)。χ_c(-1)在
primary mod4 sector固定；对原untwisted24-vector完成作系数共轭与ell
翻转，可取得同Nν的参考完成。三个normalized Gamma shifts均有
+|ell|/2，FE单位phaseαν^(-ell)不能省略。参考dual length为
Nu Nh³/X；角参数、矩阵、2part和poles仍需逐项跟踪。

这没有给任意η乘在root-index上时的完整新反射。F的angular expansion
和outer Mellin测试必须保留；以现有untwistedFE识别conductor和长度
不代表已付实际arbitrary-target reflected norm或共同profile。

## 5. 对换域问题的结论

本轮推进了Gaussian实际同target构造，不能从这些恒等式断言换域
已优于−3。无slots时窄raw只在U≥D²成为线性；457需要每个c>0的
H≥D^(1+c)与scale supremum。直接用现有窄界作order4放大，其formal
envelope为max(1,1/4+3r/2)，比理想1/4+3r/4更贵。

接受范围：真实probe、unit-dual、good-prime局部表、共同符号窄raw，
双hop的linear-row numerator及无任意target的参考完成尺度。
未接受：critical raw、全Euler reciprocal/marked/plain合同、新sigma、
新比例、来源整链或外部kernel认证。现有三篇论文与sigma*保持原版。
