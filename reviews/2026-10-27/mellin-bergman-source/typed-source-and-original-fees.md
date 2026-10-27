# Mellin–Bergman源：半整数权类型、两个尖点与原费用

2026-10-27；/root/mb_source独占原稿。执行STATE指定的[实际source首门](../arithmetic-theta-section8/next-mellin-bergman-source-admission.md)，不改STATE/cadence/Git，不恢复C047预算，不预C048/585。本稿只支付该固定公式的类型／端点／源费用与实际像；Pan净后果由独立稿和root另行消费。出稿不代root验收。

## 1. 对象与两种变量

固定Kudla§8允许的一个算术模型及其level N=4D(B)，并固定原theta核匹配的半整数权automorphy。令S为这个固定level／automorphy的**holomorphic cusp sector**，κ=3/2，采用第一变量线性的Petersson积

\[
 (f,g)_{\rm Pet}=\int_{\Gamma'\backslash\mathfrak H}
 f(\tau)\overline{g(\tau)}v^\kappa\,\frac{dx\,dv}{v^2},
 \qquad \tau=x+iv .
\]

这里只使用固定holomorphic cusp空间的有限维性，不将未给出的smooth/Maass输入并入S。记d=dim_C S，选Petersson正交标准基f_1,…,f_d。d=0时以下所有和为空，A=0、C_B=0，像恰为S={0}，无需挑另一个level使其非零。

物理变量另记t∈R，r(t)=e^(t/2)f_phys(t)属于全部复S_exp；原du范数就是L²(R,dt)。固定已准入的imaginary ray与框架

\[
 \tau=i e^t,\qquad
 W_j(t)=e^{\kappa t/2} f_j(i e^t),\qquad
 A_r=\sum_{j=1}^d c_j(r)f_j,\quad
 c_j(r)=\int_{\mathbb R}r(t)\overline{W_j(t)}dt.       \tag{1}
\]

x,v是模变量，t是physical log-time，二者不偷换。正数e^(κt/2)是这个候选已经冻结的评价框架，不是物理中心化的替代。没有声称(1)与adelic限制、Hecke作用或真实Weil对应等变。

## 2. 半整数权尖点展开：不假定trivial multiplier

对每个相关cusp c取一个选定的metaplectic scaling lift。其slash后的holomorphic函数F_c在宽度h_c下可以有相位

\[
 F_c(z+h_c)=e^{2\pi i\alpha_c}F_c(z),\qquad
 F_c(z)=\sum_{n+\alpha_c>0}a_c(n)
       e^{2\pi i(n+\alpha_c)z/h_c}.                    \tag{2}
\]

α_c由原半整数权automorphy决定；不将它无声设为0。holomorphic cuspidality给全部实际出现的指数严格为正。对于给定非零f，最小非零指数是正数；若f=0则下面界平凡。正常收敛的q展开及其导数在每个充分高的半平面中给：存在a_c>0，使每个m≥0有

\[
 |F_c^{(m)}(iy)|\le C_{f,c,m}e^{-a_c y}\quad(y\ge Y_c).
                                                               \tag{3}
\]

可将a_c略减以统一控制各固定阶导数；不需要其数值。于是Euler导数满足

\[
 |(y\partial_y)^\ell F_c(iy)|
 \le C_{f,c,\ell}(1+y)^\ell e^{-a_c y}.                \tag{4}
\]

这一步允许fractional cusp exponent和非平凡unitary theta multiplier，未把weight3/2当普通weight2/trivial character。

∞端取F_∞=f本身（连同其原cusp框架）。对t充分大，y=e^t，(3)–(4)与(1)直接给

\[
 |D_t^\ell W_f(t)|
 \le C_{f,\ell}e^{(\kappa/2+\ell)t}e^{-a_\infty e^t}.
                                                               \tag{5}
\]

0端取S_0=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)
的一个固定metaplectic lift，令F_0=f|_\kappa S_0。它在cusp∞具有cusp0对应的展开(2)。沿imaginary axis，slash因子的绝对值为v^{-κ}，相位固定，故

\[
 f(iv)=\zeta_0 v^{-\kappa}F_0(i/v),\qquad|\zeta_0|=1 .
                                                               \tag{6}
\]

这里不要求Fricke算子保持原S或选择一个Fricke特征基；F_0只是这个cusp的局部slash表达。令s=−t、v=e^t，则

\[
 W_f(-s)=\zeta_0 e^{\kappa s/2}F_0(i e^s).
\]

因此t充分负时

\[
 |D_t^\ell W_f(t)|
 \le C_{f,\ell}e^{-(\kappa/2+\ell)t}e^{-a_0 e^{-t}}.     \tag{7}
\]

中心的有限t区间由holomorphy给全部导数有界。结合(5)/(7)，对每个N、ℓ，

\[
 p_{N,\ell}(W_f)=\sup_t e^{N|t|}|D_t^\ell W_f(t)|<\infty,
 \qquad \boxed{W_f\in S_{\exp,\mathbb C}.}              \tag{8}
\]

常数依固定f／模型／level／cusp框架；没有跨level或cofinal family统一常数。特别是所有W_j同时在L²和S_exp中，不需要crop两端。

## 3. (1)确为复线性、基无关的实际源

对任意r∈L²，Cauchy–Schwarz已使每个c_j(r)绝对收敛，所以(1)先在整个原L²源域上定义，而不仅在compact测试上。原全部S_exp是该域的子空间，特别包含405的实际noncompact Pan及其平移；公式没有先取关系商。

源r出现在第一变量，不取conjugate(r)，故A按r复线性。若换成任意Petersson正交标准基

\[
 f'_a=\sum_jU_{aj}f_j,\qquad U\ \hbox{unitary},
\]

则W'_a=Σ_jU_ajW_j，c'_a=Σ_j overline(U_aj)c_j，故

\[
 \sum_a c'_a f'_a
 =\sum_{j,k}c_j
    \left(\sum_a\overline{U_{aj}}U_{ak}\right)f_k
 =\sum_jc_jf_j.                                        \tag{9}
\]

因此A不依基。等价地，令K_t=Σ_j overline(W_j(t))f_j，它是S中加权evaluation的Riesz向量，(1)是有限维Bochner积分A_r=∫r(t)K_tdt。这个内在描述仍依冻结的ray／评价框架；不能据此称它是已证的算术或Hecke source functor。

## 4. 原du、zero-extension Dlog及强源费用

由(8)，

\[
 C_B^2:=\sum_j\|W_j\|_{du}^2
       =\sum_j\int_0^\infty v^{\kappa-1}|f_j(iv)|^2dv
       <\infty .                                      \tag{10}
\]

κ=3/2时幂为v^(1/2)。这个ray积分不是二维Petersson范数；正交标准基不允许把C_B替换成1或√d。C_B本身基无关，因为Σ|W_j(t)|²是加权Bergman evaluation密度。

对整个r∈L²(R,dt)，

\[
 \begin{aligned}
 \|A_r\|_{\rm Pet}^2
 &=\sum_j |(r,W_j)_{du}|^2\\
 &\le\left(\sum_j\|W_j\|_{du}^2\right)\|r\|_{du}^2,
 \qquad \boxed{\|A_r\|_{\rm Pet}\le C_B\|r\|_{du}.}
 \end{aligned}                                         \tag{11}
\]

C_B是一个充分upper fee（Hilbert–Schmidt上界），不是已计算的sharp operator norm或necessary lower。固定源窗I中还可用C_(B,I)²=Σ_j∫_I|W_j|²≤C_B²；所以(11)对同一固定模型的全部源窗也成立。改变模型／level则没有统一C_B。

沿原Fourier／Plancherel规范，原zero-extension Dlog满足

\[
 \|r\|_{D_{\log}}^2
 =\frac1{2\pi}\int_{\mathbb R}\log(2+|\xi|)
             |\widehat r(\xi)|^2d\xi
 \ge\log2\,\|r\|_{du}^2.
\]

故同域有

\[
 \boxed{\|A_r\|_{\rm Pet}
 \le C_B(\log2)^{-1/2}\|r\|_{D_{\log}}.}                 \tag{12}
\]

这里是全线／零延拓范数，不改为regional或periodic norm；另加1的Hlog也未改称同一个范数。对强源半范数，任意N>0有
\(\|r\|_{du}\le N^{-1/2}p_{N,0}(r)\)，所以(11)同样证明A:S_exp→S连续。没有额外原权e^t被吸入r；physical centering仍是r=e^(t/2)f_phys。

## 5. 实际像A(S_exp)=S，而非只给一个合法中间输入

假设d>0。若Σ_jz_jW_j(t)=0于L²，因该函数smooth，它对全部t为0。除去e^(κt/2)后，holomorphic cusp formΣ_jz_jf_j在整条positive imaginary ray上为0；holomorphic唯一性给Σ_jz_jf_j=0，因f_j为基而z=0。因此W_j线性独立。

更实际地，令

\[
 G_{ij}=\int_{\mathbb R}W_j(t)\overline{W_i(t)}dt .
\]

G是正定Hermitian矩阵。给定s=Σ_i a_i f_i∈S，令z=G^(-1)a并取

\[
 r_s=\sum_jz_jW_j\in S_{\exp,\mathbb C}.
\]

直接代(1)得c_i(r_s)=Σ_jG_ij z_j=a_i，故

\[
 \boxed{A(S_{\exp,\mathbb C})=S.}                       \tag{13}
\]

这给出了在实际物理源空间中的右逆，不把delta distribution当源。若需要固定模型的原du价格，
\(\|r_s\|_{du}^2=a^*G^{-1}a\le\lambda_{\min}(G)^{-1}\|s\|_{\rm Pet}^2\)；
各强半范数也由有限Σ_j p_(N,k)(W_j)及G^(-1)给出。没有跨模型的λ_min lower，有限右逆也不恢复任意原源、更不等于classic全源coverage。

## 6. 接算术lift时实际已付／未付

§8的Θ:S→arithCH^1是已定位的cited线性lift；其原证明、stack/index及height责任保持上一来源记录的等级。对(1)，组合可按有限和

\[
 J_r=\Theta(A_r)=\sum_jc_j(r)\Theta(f_j)
\]

解释，因而没有在这一有限组合步骤新引入无限Green求和。但(11)/(12)支付的是Petersson输入费；不能将它直接叫作自然Arakelov height／positive energy的已知数值norm界。未给Theta(f_j)的非零性、vertical分量、具体height矩阵或完整经典Weil身份。

尤其(13)只说实际像覆盖所选S；原Pan的像、537非根是否在新arith目标可见，以及principal／base下降必须由同一个实际map另测。源合法和满射都不自动成为primitive/RR或符号。经典全部Γ/contact、properpowers、双pole与growth/core/coupling/Ξ不由本稿取得。

## 7. 净分类与前件摘要

所付步骤是标准holomorphic cusp展开／unitary半整数权slash、有限维Riesz／Gram及Cauchy–Schwarz的直接应用，原物理域和费用现已明确。结合553的关系首门是否只为强旧合成，应由独立Pan稿/root/fresh统一比较；本稿建议**标准实际source准入0新数学轮**，不因有新公式或right inverse就领取独立经典正性。

| 消费项 | 本稿范围 |
|---|---|
| actual object/source | 固定matching half-integral holomorphic S，冻结imaginary ray；allcomplex physical S_exp→A_r∈S |
| 原norm／量词 | 每fixed模型/level全L²du bound C_B，原Dlog及强源费另列；无cofinal模型uniform价格 |
| cusp／误差 | 0/∞可有fractional exponent；(5)/(7)全部导数双指数尾，无crop／numerical step |
| coefficient方向 | c_j=∫r barW_j；basis换U时c换barU；A复线性且基无关 |
| 实际像 | W_j独立／Gram可逆给实际S_exp右逆，A(F)=S；S=0单列 |
| 未付coverage／coupling | 关系下降、同源537、算术整过滤／mixedRR、完整classic signed／成长及actualq/core/coupling/Ξ |
| strongest-old | source步骤标准；Pan与宏观净值须先扣553，不把合法输入当新独立设施 |

止于冻结公式。不调ray、level/B、basis、阻尼或新增paper；nonholomorphic无限输入、cofinal变域、额外实际数据和未逐层Pan的D′修复仍未被本稿排除，也未因其名称而获得准入。本文件只编辑自身独占路径。
