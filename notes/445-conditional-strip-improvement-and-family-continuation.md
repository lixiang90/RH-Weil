# 445. 引用原通用结果下的边界改进与全角色族 continuation

2026-10-07。状态 [T/R]：在明确引用OpenAI原稿的通用算术/分析结果及其全Hecke
7/8结论后，441–444的新同源估计闭合至sigma1=69999/80000。
这是纸面引用证明，不是独立验收整篇原论文，也没有新增Lean kernel证书。
该结果来自可变槽几何；AF简单临界线比例没有进入此证明。

## 1. 结果及准确前件

固定[September-30原稿](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)，
提交adc7f1241b42e322a6451854ab7e4b4c146bf78a，canonical LF SHA256
42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3。
具体外部[R]依赖不是一句未展开的“有high界”，而是：

| 原输入 | 新稿逐前件准入 |
|---|---|
| 原coefficientwise probe/Poisson、finite compensation、局部算术表与ray校准 | 441–442保留独立physical表达式及准确high身份 |
| smooth calculus、Gaussian annuli、row sectors、通用reflected energy、additive Gram | 441给可变ell的完整low，保留正row loss与全部masks |
| fixed-bin/global/buffered reciprocal、Hecke增长/functional equation、外轮廓尾 | 442重放新sigma1的轮廓、principal与外行；444一次分配所有strict labels |
| detector witnesses、marked/plain/recursive moments、sixth-power amplification、uniform mesh | 443给合法fixed kappa=3/4下实际count与actualwhole slots |
| 原全primitive finite-order Hecke 7/8结论 | 仅作beta_*<=7/8 bootstrap；不假设新sigma1半平面无零 |
| fixed-ray prime asymptotic | 442给实际同一A_T的最终非零/subpower逆及主槽余留数 |

在这些来源结果成立的前提下，得到：

\[
 \boxed{L_F(s,\eta)\ne0\quad(\Re s>69999/80000)}
 \tag{1}
\]

对F=Q(sqrt(-3))的全部finite-order Hecke characters成立，principal s=1极点允许。
同一个严格半平面转移到全部Dirichlet L，特别包括zeta。
相对原7/8向左移动1/80000；不对边界线本身作无零断言。
以下给统一量词与Mellin反证，而不只依赖一个endpoint负指数。

## 2. 同一physical函数与同一信号

假设beta_*>sigma1。原7/8bootstrap给
Delta1=beta_*-sigma1∈(0,1/80000]。
几何固定为ell1=10003/60000、b=1/8、lx=42497/120000、ly=57497/120000、
h1=32503/40000。C(s)=s-11/16，C(sigma1)=14999/80000。
Sigma1、几何、下面所有real choices及slot系统都在目标eta之前固定。

按443选fixed even K及equal positive ell_i=ell1/K，原disjoint非负非零W_i。
按442选target-independent P0使同一个principal校正H_eta在Re s>sigma1全纯且
sup|H_eta-1|<=1/2。Target后扩大S仍保持同一正majorant。
固定目标的最终S后，所有physical sums、calibrations、high身份、c_S、A_T及H_eta
均使用该同一数据。
令

\[
 J_\eta(Z)=I_{\eta,\mathrm{modified}}(Z)/(c_S A_T(Z)),
\]
\[
 f_\eta(Z)=\frac1{2\pi i}\int_{(2)}
 Z^{C(s)}e^{(s-5/6)^2}\frac{H_\eta(s)}{L_F^S(s,\eta)}\,ds.
 \tag{2}
\]

A_T最终非零且逆为任意小幂，c_S>0。
J由原completed sums独立定义；f是同一principal双留数。
两个函数都不含analysis cutoff T1；T1只出现在估计中。

## 3. Low合同与不可循环的real参数顺序

441对新geometry给
|I_modified|<<Z^{C(sigma1)+epsilon_low}。
逆A_T再花任意epsilon_norm。先固定epsilon_low+epsilon_norm<=Delta1/2，得到

\[
 |J_\eta(Z)|\ll_\eta Z^{C(\sigma_1)+\omega},
 \qquad\omega=\Delta_1/2\in(0,\Delta_1).
 \tag{3}
\]

Omega与这些exponents在目标前固定，constants及阈值允许依赖eta。

High的central基础margin由444给m_ad=307/11016000。
先以m_ad的fixed小份选择count/moment losses、capacity decrements、plain uniform mesh及rounding。
再取fixed even K使2ell1/K<min(mesh,b_round,1/185)，确定原disjointwindows。
此时才选

\[
 \mu=\frac{\sigma_1\ell_1}{2K}>0,
 \qquad m_w=57497/2400000,\quad m_z=32503/24000000.
 \tag{4}
\]

Mu<sigma1 min ell_i，支付442principal余留数。
不能先用依赖K的mu来选择需要先于K的moment mesh。
Central count预算只需m_ad；K固定后principal预算可以另取任意更小e及powers。
也在K之后选依赖min ell_i的amplitude宽度与prime preliminary losses。
e满足原detector-dyads的e0（保留原pre-saturation bounded ranges），
central real总loss、multiplicity与inverse-normalizer成本小于m_ad/4。
Principal三项分别满足
(1+h1)e+epsilon_pr<m_w/4、e+epsilon_pr<m_z/4、e+epsilon_pr<mu/4。

固定zeta=m_ad/32，满足443actualsupply且h1+zeta<1。
444的上端cost<=m_ad/16；余量至少15m_ad/16，
扣central real预算后还大于m_ad/2。
442小行独立margin172249/2000000，选其loss小于一半；
大行先固定足够大的z_infty使margin至少m_ad，再选小loss。
这些real choices和固定real boxes均在目标前确定。
令

\[
 m_0=\min\{m_{ad},m_w,m_z,\mu,172249/2000000\}>0,
 \qquad m=m_0/4>0.
 \tag{5}
\]

此前已选central budget无需改为m0：其剩余>=m_ad/2>=m0/2。
Principal、小行及大行也保留>=m0/2，故共同使用m不会倒转选择顺序。

## 4. Actual high的全部物理行与height ceiling

442–444的分解覆盖全部physical dyads：

- u=1：同一A_T、c_S的principal residue，三个余项由(4)支付。
- U<=Z^{d_min}、d_min=1/100：完整无商tuple的小行界，D1(1/3)替代旧D1(3/8)。
- Z^{d_min}<U<=Z^{h1+zeta}：whole-bin先移线，再作finite pointwise error/amplitude/witness分箱；
  no-slot中间、floor与actual selectedcount分别有444的uniformmargin。
- U>Z^{h1+zeta}：完整绝对selected/unselected界及fixedz_infty。

所有moderate行共同使用合法kappa_eff=3/4。
不把floor或bounded units硬塞进actualwitnesscount。
所有strict ramified error labels共用一次numerator conductor预算。

目标确定后，固定它的arithmetic datum与最终S，再固定全部internal moment、Sobolev、seminorm阶。
统一finite A_eta支配所有retained height幂；fulltuple与global/absolute estimates给finite B_eta。
二者不依赖稍后external N。Physical Im z、witness及prime frequencies共用原固定矩阵的
cumulative T1/2 allocation；不能逐步骤重新定义buffer。
设epsilon_ht>0为先前指定的有限detector height allowances之最小。
令A_ht,eta<=A_eta支配它们，固定

\[
 \tau_{0,\eta}=\frac{d_{\min}\epsilon_{ht}}{20(1+A_{ht,\eta})}>0.
 \tag{6}
\]

当0<tau<=min(d_min/100,tau0,eta)、T1=Z^tau时，moderate U>=Z^{d_min}给
T1<=U^{1/100}，(1+T1)^{A_ht,eta}<=U^{epsilon_ht/10}最终成立。
故每个literal detector height hypothesis成立，原crude error
U^{-189/100+o(1)}T1²<=U^{-187/100+o(1)}趋0。
Small与absolute large rows无需buffered detector cutoff。

Finite types、dyadic multiplicities、normalizer与principal allowance分配后，得到

\[
 |J_\eta-f_\eta|
 \ll_{\eta,N}Z^{C(\beta_*)-m}(1+T_1)^{A_\eta}
                         +Z^{B_\eta}T_1^{-N}.
 \tag{7}
\]

对每个N，估计在上述固定ceiling下成立；lower threshold可依赖eta,N,tau。
增加N只增external test seminorm，不将internal moment应用到新外部导数，
不改变A_eta、B_eta、mesh或real powers。

## 5. Late height关闭与全族量词

在target及internal阶之后选

\[
 0<\tau_\eta\le
 \min\{d_{\min}/100,\tau_{0,\eta},m/[4(A_\eta+1)]\}.
\]

于是(7)第一项<<Z^{C(beta_*)-3m/4}。
再取fixed整数N_eta使B_eta-N_eta tau_eta<C(beta_*)-m/2，
最后提高threshold，得到

\[
 |J_\eta-f_\eta|\ll_\eta Z^{C(\beta_*)-\sigma_{hi}},
 \qquad\sigma_{hi}=m/2>0.
 \tag{8}
\]

Omega与sigma_hi都与target无关；tau、N、constants及threshold可依赖target。
T1没有进入J或f定义，故不同target选不同tau不会改变同一个函数合同。

## 6. Mellin反证：不跨目标零点

令epsilon_*=min(Delta1-omega,sigma_hi)>0；它在target前固定，且epsilon_*<Delta1。
(3)(8)与C斜率1给|f_eta(Z)|<<Z^{C(beta_*)-epsilon_*}于大Z。
H_eta有界，Re s>=2的reciprocal Euler product有界，Gaussian使水平joins趋0；
将(2)向右移至任意fixed B>2得|f_eta(Z)|<<_{eta,B}Z^{B-11/16}于0<Z<=1。
故

\[
 F_\eta(s)=\int_0^\infty f_\eta(Z)Z^{-C(s)}\frac{dZ}{Z}
 \tag{9}
\]

在Re s>beta_*-epsilon_*局部一致收敛并全纯。
写Z=e^u，(2)是e^{-(2-11/16)u}f_eta(e^u)的Fourier inversion。
两端已证integrability，因此在Re s=2有
F_eta(s)=e^{(s-5/6)^2}H_eta(s)/L_F^S(s,eta)，
再由identity theorem在Re s>1一致。

因为beta_*-epsilon_*>sigma1且|H_eta|>=1/2，
e^{-(s-5/6)^2}F_eta(s)/H_eta(s)
在Re s>beta_*-epsilon_*给1/L_F^S的全纯延拓。
Supremum定义给某个target有零rho满足Re rho>beta_*-epsilon_*，
无需beta_*被任何target达到。
Deleted factors在Re s>0非零，该rho的reciprocal有极点，矛盾。
故beta_*<=sigma1，得到primitive Hecke的(1)。

## 7. Dirichlet与zeta转移及范围

有限Euler因子非零于Re s>0，故Hecke conclusion延至imprimitive角色。
原quadratic transfer的恒等式为
L_F^S(s,chi∘Norm)=L^S(s,chi)L^S(s,chi chi_{-3})。
在0<Re s<1两Dirichlet因子全纯，零不能由另一因子的极点抵消；
Re s>1由absolute Euler product，s=1+it、t不等于0由同一乘积。
唯一s=1可能的pole-zero cancellation涉及principal与chi_{-3}，
但L(1,chi_{-3})=pi/(3sqrt3)>0。
因此全部Dirichlet L，包含zeta，均满足同一个严格边界；principal pole允许。

441–445完成的是引用原generic results后的新纸面推导：low改变主交点，
443的actualcounts与444的uniform余量确保high继续成立，442支付源identity与解析域。
没有把AF 67.25%作为Hecke坏行幂节省，没有由比例推出RH。
本项目的finite algebra审计及独立读源审查，不等同于外部Lean elaboration/kernel/Comparator；
原依赖整体正确性与本次改进的形式化仍须分别验证。
