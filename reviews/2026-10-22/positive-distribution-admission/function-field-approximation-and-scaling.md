# 真函数域完整分布的逼近门：缩放、正primitive与闭包的准确范围

2026-10-22，独占分支，供root消费；不改STATE／cadence／合同。本稿不证明经典Weil正性。无缩放gap已见旧 `grh-six-note-review/next-direction-admission-audit.md`，不重计。下面真正新增的可判候选，是**同一已付椭圆曲线的base change＋centered dilation**，并逐项核其all-powers、正实权primitive、完整pole和原源费用。RR正性、Bochner与Diophantine／Riemann和工具归标准来源，不能冒称新的外部定理。

## 1. 固定对象及准入结论

取563／566／567已付的
\[
 E/\mathbb F_5:y^2=x^3+x+1,\quad N_1=9,\quad
 F=\begin{pmatrix}0&-5\\1&-3\end{pmatrix},\quad
 H=\begin{pmatrix}1&-3/2\\-3/2&5\end{pmatrix}>0,
 \quad F^THF=5H.
\]
令 \(U=F/\sqrt5\)，其两个特征值记作 \(e^{\pm i\theta}\)，仅用于记已由正H认证的全递推；\(2\cos\theta=-3/\sqrt5\)。原正性来源是实际曲面RR／Rosati而非未知经典零点。函数域全点数、完整zeta与对偶的来源可核[Milne §1](https://www.jmilne.org/math/xnotes/pRH.pdf)；567已把实际RR接到全mixed源。高维trace、对偶与纯性须分开，见[Deligne Weil I](https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf)。

本门的准确结论为：

* 不缩放的真函数域完整分布及趋恒等的compact抹平，不能逼近经典完整分布；这只是旧gap门。
* 允许每个正权分量各有centered dilation后，实际base change给 \(2\cos(tu)du\) 的独立正逼近，并可维持真正的**正实权primitive分布**，不只维持正log-Euler系数。
* 再允许任意正实权有限混合，则其**未标记完整分布**的闭包是全体实偶正型分布锥。它不是固定完成化／权／pole标签的纤维闭包，也不自动提供普通整函数行列式。
* 该密度不构造经典目标的正谱测度。经典进入此闭包，仍承担完整Weil正性的责任；不能用未知测度选择近似再称非循环。

## 2. 无缩放gap：旧资产及有限抹平边界

对真曲线 \(C/\mathbb F_q\)，\(L=\log q\ge\log2=:L_0\)，完整分布为
\[
 W_C=L\sum_{n\in\mathbb Z}a_n\delta_{nL},\qquad
 a_n=\operatorname{Tr}(U^n),\quad a_0=2g,\quad |a_n|\le2g.       \tag{1}
\]
全部周期aliases、proper powers和pole已由点数公式合并。任何有限组合——此处甚至不必正权——在 \((0,L_0)\) 为0。D′极限保留这个共同open gap。经典在prime之前的穿孔区却有
\[
 W_\zeta|_{(0,L_0)}=
 \left(2\cosh(u/2)-\frac{e^{-u/2}}{1-e^{-2u}}\right)du,       \tag{2}
\]
密度在靠近0的一段严格负，故单个非负compact测试即否决。base change把L增大，不修gap。式(2)只在穿孔区使用；没有丢掉原点finite-part／contact，亦没有把它当全分布通常密度。

取非负谱乘子的compact近似恒等核 \(\eta_\epsilon\)，例如归一化 \(\phi_\epsilon*\phi_\epsilon^*\)，支撑 \([-\epsilon,\epsilon]\)。卷积保正型且支撑只扩张ε，故ε→0仍保任何固定 \(I\Subset(0,L_0)\) 上的零，权和genus成长不影响这个结论。

Gaussian核无compact支撑，应另付尾费。对正权混合且 \(M_j=\sum\lambda_C2g_CL_C<\infty\)，用 \(|a_n|\le2g\) 可统一估其尾为 \(M_jO(e^{-c/\epsilon_j})\)。若抹平完整分布在D′收敛，取支撑在 \((-L_0/4,L_0/4)\)、原点值1的非负测试，原点项为 \(M_j(1+o(1))\)，其余项为 \(M_jo(1)\)，故 \(M_j\) 有界；随后固定gap测试仍趋0。此处ε按Gaussian variance参数，c依测试距离固定。这个结论限正权／有限M及趋恒等Gaussian；不把任意signed重整化或不趋恒等核一并排掉。

## 3. Centered dilation：完整pole、powers和原范数

对 \(C/\mathbb F_Q\) 及 \(a>0\)，定义
\[
 Z_{C,a}(s)=Z_C\bigl(\tfrac12+a(s-\tfrac12)\bigr),\qquad
 h=a\log Q.
\]
它的完整分布是
\[
 W_{C,a}=a(S_a)_*W_C
          =h\sum_{n\in\mathbb Z}\operatorname{Tr}(U_C^n)\delta_{nh}.
                                                               \tag{3}
\]
这是自然log-derivative／零除子归一化，不能漏前面的a。新对偶仍中心1/2；原0/1 pole变成
\[
 \tfrac12\pm\frac1{2a}+\frac{2\pi i k}{h},\qquad k\in\mathbb Z.  \tag{4}
\]
不作center修正的 \(Z_C(as)\) 保原unit Euler因子，却把中心移到1/(2a)。因此不能同时把缩放当成保经典0/1和原分次权的操作。

记 \(\mathcal T_ar(v)=\sqrt a\,r(av)\)，则
\[
 \|\mathcal T_ar\|_{L^2(dv)}=\|r\|_{L^2(du)},\qquad
 Q_{C,a}(r)=aQ_C(\mathcal T_ar),                              \tag{5}
\]
\[
 \mu_\pm(\mathcal T_ar)=a^{-1/2}
       \int e^{\pm u/(2a)}r(u)du.                            \tag{6}
\]
固定物理窗[-R,R]变成native窗[-R/a,R/a]；不能把native固定窗费用直接套用。原zero-extension Hlog／Dlog有准确运输
\[
 \|\mathcal T_ar\|_{H_{\log}}^2=(2\pi)^{-1}\int
 [1+\log(2+a|t|)]|\widehat r(t)|^2dt.                         \tag{7}
\]
0<a≤1时它不超过原Hlog；反向比较会付log(1/a)。这只说源运输费用，不说全pole或全预算收敛。

Γ=0的真函数域经过此缩放仍无经典无穷位Γ。若给(3)额外加经典Γ并换回0/1 poles，修正为signed分布，正型不由原RR自动保留。**但是**路线B只需未标记的完整W收敛；各近似pole不等于经典pole，不单独否决这种收敛。须区分固定标签纤维与完整源像的闭包。

## 4. 同一真曲线的base change构造任意预先指定cos源

\(\theta/(2\pi)\) 无理：否则 \(e^{i\theta}\) 为root of unity，\(-3/\sqrt5\) 是代数整数，进而其平方9/5是有理代数整数，矛盾。因此存在 \(m_j\to\infty\)，使
\[
 \delta_j=\operatorname{dist}(m_j\theta,2\pi\mathbb Z)>0,
 \qquad\delta_j\to0.                                       \tag{8}
\]
这是无理旋转的标准Dirichlet／稠密性输入；可通过已知F的矩阵递推和严格区间认证逐项寻找，不需要任何ζ零点。base change \(E_j=E/\mathbb F_{5^{m_j}}\) 的相位是 \(\pm\delta_j\)。

给**预先指定** \(t>0\)，取
\[
 Q_j=5^{m_j},\quad h_j=\delta_j/t,\quad
 a_j=\frac{\delta_j}{t m_j\log5}.
\]
则(3)精确为
\[
 W_j=h_j\sum_{n\in\mathbb Z}2\cos(nt h_j)\delta_{nh_j}
       \longrightarrow 2\cos(tu)du                         \tag{9}
\]
于D′，甚至S′。证明直接是Riemann和，不从未知根读取：对 \(\varphi\in C_c^1\)，
\[
 |W_j(\varphi)-\int2\cos(tu)\varphi(u)du|
 \le h_j\bigl\|(2\cos(t\cdot)\varphi)'\bigr\|_1.            \tag{10}
\]
S′版可用Schwartz半范数同样控制。t=0可令 \(h_j=\sqrt{\delta_j}\)、\(a_j=h_j/(m_j\log5)\)，此时 \(\delta_j/h_j\to0\)，极限是常数2。所有整数n／全部returns始终保留，不取最低频截断。

每个 \(W_j\) 的独立正号来自同一实际E_j的RR／正H及(5)，而非从目标 \(2\cos\) 的正性反求E_j。极限式展示其标准平方和
\[
 Q_t(r)=|\widehat r(t)|^2+|\widehat r(-t)|^2.
\]
固定support[-R,R]的每个源还满足
\[
 |Q_j(r)|\le(8R+2h_j)\|r\|_2^2,\qquad
 Q_t(r)\le4R\|r\|_2^2.                                    \tag{11}
\]
前式由 \(|r*r^*(nh)|\le\|r\|_2^2\) 和 \(|nh|\le2R\) 的项数直接给。式(10)先对smooth源，随后以(11)与L²稠密性延到每个原du固定窗源；不产生额外H1费用。mixed式由极化。这里是**逐源**收敛，非原L²算子范数收敛：用频率约 \(2\pi/h_j+t\) 调制同一compact profile，grid alias仍可见而极限cos读出趋0。Dlog强化或uniform source班次另核，不能拿逐源式代付。

## 5. 真实正primitive检验：不是只保positive logΠ

centered dilation的一条local Euler因子通常变成加权因子，不能从每个local因子直接声称标准primitive为正。对本节的实际曲线族却可以独立付清。

暂取 \(Q=5^m\ge25\)、0<a≤1、相位δ，并设
\[
 A=Q^{(1+a)/2},\quad B=Q^{a/2},\quad C=Q^{-(1-a)/2},\quad h=a\log Q.
\]
右半平面内精确有
\[
 \log Z_{E/\mathbb F_Q,a}(s)
   =\sum_{n\ge1}\frac{c_n}{n}e^{-snh},\quad
 c_n=A^n+C^n-2B^n\cos(n\delta).                             \tag{12}
\]
故完整Π为 \(\sum c_n\delta_{nh}/n\)。其**标准all-powers primitive**必须按Möbius反演，而非把 \(c_n/n\) 当primitive：
\[
 b_n=\frac1n\sum_{d\mid n}\mu(d)c_{n/d},\quad
 P_{Q,a}=\sum_{n\ge1}b_n\delta_{nh},\quad
 \Pi=\sum_{k\ge1}\frac1k(T_k)_*P_{Q,a}.                      \tag{13}
\]
下面给全部n的真实正号。因为A≥5B、B≥1、0<C≤1，
\[
 c_1\ge3A/5>0,\quad c_n\ge23A^n/25\quad(n\ge2),\quad
 0<c_k\le7A^k/5+1.
\]
令d=floor(n/2)≥1，全部proper divisor对应的指数在1,…,d中，因此
\[
 \sum_{\substack{e\mid n\\e>1}}c_{n/e}
 \le\frac75\sum_{k=1}^dA^k+d
 \le\frac{39}{20}A^d\le\frac{39}{100}A^n.
\]
其中 \(\sum A^k\le(5/4)A^d\)、\(d\le A^d/5\)，及n−d≥1。于是
\[
 \boxed{b_1\ge3A/5,\qquad
 b_n\ge\frac{53}{100n}A^n>0\quad(n\ge2).}                  \tag{14}
\]
这是实际Möbius全次数估计；未用有限数表外推。故此family在**正实权分布型g-primes**内，\(M=\exp_*\Pi\)亦为正。它不声称b_n是整数，或对应普通无权离散g-prime序列。

其收敛abscissa为 \(\log A/h=(1+a)/(2a)\)，与(4)右pole一致；不是经典abscissa1。对本属1情形，完整pole comb和prime-power comb确切为
\[
 \begin{split}
 H_a&=h\sum_{n\in\mathbb Z}2\cosh(nh/(2a))\delta_{nh},\\
 \mathcal P_a&=h\sum_{n\ne0}e^{-|n|h/2}c_{|n|}\delta_{nh},\\
 W_a&=H_a-\mathcal P_a
       =h\sum_n2\cos(n\delta)\delta_{nh}.
 \end{split}                                               \tag{15}
\]
原点2h及全部周期poles没有删除。对(9)的极限，H_a与prime项在正距离离原点的正测试上通常各自发散，完整差仍有(10)的精确预算。不能说它们分别趋经典pole／prime／Γ；其抵消在每个近似由(12)／(15)精确付清，而**与经典目标全源相等**仍完全未付。

## 6. 正实权有限混合的闭包：有实物，但普适性恰好不选出经典目标

令 \(\mathcal C_{\rm FF}\) 是上述实际base change与每分量centered dilation之完整W的**正实权有限锥**。每个对象从实际函数域证书独立为正，(9)给每个 \(2\cos(tu)du\) 属其D′闭包。

标准Bochner–Schwartz表示将任意实偶正型分布写成实偶正tempered测度的逆Fourier变换。用截断及有限正离散测度近似该测度，再对每个有限cos和使用(9)，即可取对角序列使
\[
 \boxed{\overline{\mathcal C_{\rm FF}}^{\mathcal D'}
       =\{\text{实偶正型分布}\}.}                          \tag{16}
\]
反向由每个fixed compact平方测试上的正型锥闭性；没有使用待证经典正号。Bochner／positive spectral measure工具是标准资产，相关测度与二次型框架可核[Alpay–Jorgensen §§1–3](https://arxiv.org/pdf/1109.5273)。式(16)不必宣称此前外部文献已有此**特定函数域族**的相同表述；本稿只是给出由已付曲线、标准旋转与Riemann和直接拼成的候选／检验。

必须保留三条范围：

1. 各分量允许各自a，不是一个共同缩放或固定pole／权纤维。
2. 任意正实权保证positive primitive及源Gram，但 \(Z^\lambda\) 在非整数λ时可有branch；不能自动成为通常亚纯completed zeta或具有整数重数的ordinary determinant。若限整数权／通常行列式类，(16)的全锥结论不由本证明给出。
3. (16)的“对某个已知正型W选测度”不是独立经典近似算法。把W换成经典Wζ来调用正测度，恰好先用了完整Weil正性。当前并无从经典Γ、Λ(n)、pole直接产生正混合系数及误差→0的方法。

因此已有一个非零、足够丰富的实际positive原料族，且无需先找极限scheme。未付责任精确缩到：**直接从经典完整算术分布给这些独立正原料的非负混合与全测试误差**。不能再泛称“函数域近似绝不可能”，也不能把普适性作为RH已得。

## 7. 405／537及原费用的source gate

原source仍为物理 \(r=e^{u/2}f\)，不是native曲线坐标。式(5)／(7)与(11)给了该候选的真实原du、Dlog运输及固定窗逐源费用。whole、成长源uniform误差未由(10)付清；混合总权／频率成长会进入(10)／(11)。

单个positive原料不要求消经典405解析关系；固定目标纤维却要求。它们确实一般不消：405的 \(p=(D^2-1/4)H\)、H>0且快速衰减，有 \(\int p=-\frac14\int H\ne0\)，而t=0的极限给
\[
 Q_0(p)=2|\textstyle\int p|^2>0.
\]
所以“原料全正＋源map真实”不等于已满足经典主关系。该结论适用于其全部平移，不能只核compact交空。对于537非零compact r0，可从预先可计算的Fourier非零处选某个t，使 \(Q_t(r_0)>0\)，并由(9)在足够后层保持非根；它不补405全关系。

若最终独立给 \(W_j\to W_\zeta\) 于D′，在compact源上完整Q正性即传递，足以走经典Weil判据；若还要声称所有S_exp中的405关系于实际几何层下降、原norm lift、普通heat／determinant，则须另付更强源域及trace尾tightness。D′收敛不是这些附加设施的同义词。

## 8. root消费与停止建议

真实输入：已认证E/F5及其全递推／H／真实base change，标准无理旋转，明确centered dilation，(12)的实际positive all-powers数据。可判检验：(8)的相位小回归、(10)完整分布误差、(14)全primitive正号、(15)同源抵消、405／537与原费用。

扣旧净后果：旧gap不重计；本稿给函数域缩放原料的显式非空与正实权primitive检验，并说明其扩展正锥的普适闭包。它改变“有无合法positive逼近原料”的局部答案，**没有**给经典完整W的独立近似、RR容量、405比较、原成长费用，亦不改strong-old542＋555→557的whole4/5上预算或core／coupling／Ξ。

下一若只引用(16)“存在某个正测度”来选择经典系数，立即作为等价责任停止；不调m/a拟合未知ζ零点。可重新准入的真正新输入，是从完整Γ/contact、全prime powers、0/1 pole直接计算的非负混合规则，及在逐测试／固定窗原norm中的同步误差界；或一个有实际几何／capacity来源、能独立付这些非负系数的映射。固定标签、整数trace、共同缩放、或新的无限／signed修复均未被本稿排除，须各自重新核量词与费用。
