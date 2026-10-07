# 443. 固定有效 κ 后的实际 detector capacity 与行数

2026-10-07。状态 [T/R]：相对于下面指明的通用 witness、marked/inverse/plain
moments 与 smooth calculus，本稿支付新几何上的实际 detector-count 准入。
不是仅比较名义容量，也没有把 kappa<3/4 的未覆盖参数插入原 theorem。
中央联合误差与最后无零结论另行证明。

## 1. 来源与真实参数域

固定 [OpenAI/math September-30 paper.tex](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)，
提交 adc7f1241b42e322a6451854ab7e4b4c146bf78a，canonical LF SHA256
42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3。
使用441–442同一个physical finite compensation、原sixth-power-free rows、
fixed-ray data、zero-on-nonunit extensions、disjoint positive slots和原测试。
固定sigma1=69999/80000、ell1=10003/60000、h1=32503/40000、b=1/8。

原`lem:plain`，12532、12564–12578行，只允许3/4<=kappa<=1，
kappa<1时另需beta_*<=(1+kappa)/2。故beta_*<7/8时
不能取kappa=2beta_*-1后照引原lemma。
合法选择是

\[
 \kappa_{\rm eff}=\max\{3/4,2\beta_*-1\},\qquad
 \Delta_{\rm eff}=\max\{\beta_*-7/8,0\}.
 \tag{1}
\]

原Part I共同11/12输入给kappa_eff∈[3/4,5/6]，并保证
beta_*<=(1+kappa_eff)/2；这是通用plain theorem和mesh的原范围。
若接受原全Hecke 7/8结论作bootstrap，在反证sigma1<beta_*<=7/8下

\[
 \kappa_{\rm eff}=3/4,\qquad\Delta_{\rm eff}=0.
 \tag{2}
\]

不会把负的beta_*-7/8填入原非负容量loss。
设Delta1=beta_*-sigma1>0，一般也有0<=Delta_eff<=Delta1。
非floor actual bin 的a<=beta_*，故delta=2a-1满足
1/50<delta<=2beta_*-1<=kappa_eff<=alpha=5/6。
Floor不要求actual witness，本稿不以witness覆盖floor。

## 2. 实际调用的通用 [R] 前件

| 原条款和行号 | 本稿保留的适用条件 |
|---|---|
| `prop:detector-witness`，4510–4547 | t∈[1,3/2]、同presentation、相同twist height、实际dyadic witnesses与固定loss/height条件 |
| `lem:marked`，9220–9269 | 原masks、共同正/负orientation、row-independent prime coefficients、两个严格width |
| `lem:inverse-amplification`，12362–12389 | 原sixth-power-free rows、no-slot inverse、bounded actual lengths、rowwise smooth tests |
| `lem:plain`，12492–12578 | 固定Theta系数类、原moving-radical账本、inducing family排除、kappa_eff原范围及uniform mesh |
| physical prime bin bound，15015–15061 | fixed-ray expansion、同prime window/mask、统一累计height allowance |
| amplitude subdivision/spike/coefficient identity，15064–15170 | 按原actual whole slots取spike，不更换prime系数或support |
| `lem:smooth-calculus`，1123–1209 | 共同density及fixed Sobolev/height成本，不把系数改成row-dependent |

这些核心通用 theorem 为明确的外部[R]；本稿重放15185–15446的count证明，
核新长度实际调用，不直接引用原Part II固定几何的count结论。

## 3. Sixth-power slope 与 affine crossing

No-slot inverse amplification来自原injective map(u,a)↦ua^6，给

\[
 \sum_u|M_u(U^r)|^2\ll U^{e(r)+\epsilon},\qquad
 e(r)=\max\{1,(1+5r)/6\}.
 \tag{3}
\]

因此alpha=5/6来自sixth-power slope，不是ell1或h1定义的可调容量。
除以actual inverse spike U^{delta r-epsilon}，短r<=1得1-delta r，
长r>=1得1-alpha+(alpha-delta)r。
Actual r<=t+o(1)、delta<=alpha给长count
L(t)=1-delta+(alpha-delta)(t-1)。

固定amplitude bin内q∈[0,delta/2]为原length-weighted mean，x=q/delta∈[0,1/2]。
原effective row width为1：q_u<<U，presentation nu固定，没有额外moving-conductor radical。
Inverse容量z_M=(1-r)/2；plain使用两份同一个S_m，
因此spike为|S_m|^4，容量z_P=(1-2m)/(6kappa_eff)，不能改用|S_m|²。
基准kappa0=3/4的两短count affine式为

\[
 A_I(r)=1-\delta[x+(1-x)r],\qquad
 S_t(r)=1-\delta[4x/9+(2-8x/9)(t-r)].
 \tag{4}
\]

其crossing给

\[
 D_x=3-17x/9,\quad P_x=(2-8x/9)(1-x),\quad
 r_*(t)=\frac{(2-8x/9)t-5x/9}{D_x},
\]
\[
 R_{\rm short}(t)=1-\delta+\frac{\delta P_x}{D_x}(3/2-t).
 \tag{5}
\]

实际kappa_eff>=3/4的plain capacity减少只带来非负cost

\[
 2q(1-2m)\left(2/9-1/(6\kappa_{\rm eff})\right)
 =\frac{24q(1-2m)\Delta_{\rm eff}}
 {(9/2)(9/2+12\Delta_{\rm eff})}
 \le\Delta_{\rm eff}/4+O(\epsilon),
 \tag{6}
\]

其中m>=1/3-O(epsilon)、2q<=1。
Bootstrap (2)下此cost为0，不需再人为添加Delta1/4。

## 4. Witnesses 与两种严格width

同presentation的actual witness满足r+m>=t-o(1)、r<=t+o(1)、
t-1/2-O(epsilon)<=r、0<=m<=1/2+O(epsilon)，以及
|M_r|²>>U^{delta r-epsilon}、|S_m|²>>U^{delta m-epsilon}。
先对实际dyadic pair及有限presentations分箱，再用共同smooth密度；
prime coefficients始终独立于当前row。
纯代数给r_*(t)>=23/37、1/3<=t-r_*(t)<=1/2、r_*(3/2)=1。

固定小nu0>0。在inverse侧r>=r_*(t)、r<1、z_M>nu0，
只请求z<=z_M-nu0，故

\[
 1-r-2z\ge2\nu_0,\qquad
 3-2r-8z=4(1-r-2z)+(2r-1)
 \ge8\nu_0+9/37-O(\epsilon).
 \tag{7}
\]

两条marked width分别有fixed正余量。
Plain侧r<=r_*(t)给m>=1/3-O(epsilon)；当m<1/2、z_P>nu0，
请求z<=z_P-nu0，得到
1-2m-6kappa_eff z>=6kappa_eff nu0>=(9/2)nu0。
实际annular offsets在之后由阈值吸收，不把等号冒充严格width。
最大需求z_M<=7/37、z_P<=2/27+O(epsilon)。

## 5. 原physical slots的实际spike、系数类和例外

同一个main slot是

\[
 Q_i(u;z)=P_i^{-1/2}\sum_{p\in\mathcal P_i(Z)}
 \overline{\chi_p(u)}W_i(Q/P_i)(Q/P_i)^{z-1}.
 \tag{8}
\]

p|u的main项按原zero extension为0。Error slots记g_i=0；main gains g_i∈[0,delta/2]，
q=sum ell_i g_i/ell1。此均值以全部slots的ell1作分母，不用仅positive slots重定义q。
在U=Z^d中actual lengths为w_i=ell_i/d。
按g_i降序填requested z并删至多一个fractional slot，可取whole positive slots使

\[
 \left|\prod_{i\,\mathrm{selected}}Q_i\right|^2
 \ge U^{2qz-\delta\max_iw_i}.
 \tag{9}
\]

若positive supply少于z则全取，gain>=qz；没有虚构缺失prime factor。
Capacity decrement另外cost<=2qnu0。
在固定presentation psi(n)=nu(n)bar chi_n(u)下，(8)相对psi的coefficient为
bar nu(p)1_{p∈1_T}=|T|^{-1}sum_{theta∈T_hat}(bar nu theta)(p)，
属固定Theta有限组合。Inverse可用共同negative orientation。
Plain将两份witness及全部selected factors整体共轭，系数变为nu(p)1_{p∈1_T}，
仍属同一固定群；所有masks和underlying disjoint supports保留。

Plain的positive-slot case排除primitive inducing character属于Theta的rows。
实际sixth-power-free u在S外有valuation j=1,…,5时局部阶为6/gcd(6,j)>1；
固定Theta在该prime unramified，不能消去它的primitive ramification。
剩余rows全supported on固定S，sixth-power-freeness与有限units使其有限。
在selected range U>=Z^{1/2}下最终没有这些例外；完整physical high中的bounded rows仍由442处理。

## 6. 新supply、固定mesh与内部pool

仅d>=1/2范围使用selected primes；d_min<=d<=1/2走原no-slot count。
故w_i<=2ell_i。新几何精确给

\[
 \ell_1/h_1=20006/97509,\qquad
 \ell_1/h_1-7/37=57659/3607833>0.
 \tag{10}
\]

扩至d<=h1+zeta只须固定

\[
 0<\zeta<5\ell_1-h_1=2521/120000;
 \quad \ell_1/(h_1+\zeta)>1/5>7/37,
 \quad1/5-7/37=2/185.
 \tag{11}
\]

先选count loss、nu0、uniform plain mesh与rounding allowance。
再取fixed even K、ell_i=ell1/K，使2ell1/K<min(mesh,b_round,1/185)。
选原16253–16261的互不相交I_i⊂(1,2)及非负非零smooth W_i。
Underlying supports在ray与row masks前已经disjoint。
实际norm ratio将U-length改变O_K(1/log U)，只在strict margins之后由阈值吸收。
原plain centered pool从U^{sigma_width/3}/2开始，mesh<sigma_width/6，
因此与physical slots Q<=2U^{mesh}在充分大U后隔离。
新ell1,h1不改变这个内部width参数。

## 7. Zero capacities与长witness端点

r>=1用(3)的sixth-power amplification，不用strict marked theorem。
m>=1/2用原zero-slot plain case，不限制bounded lengths。
若r<1而z_M<=nu0，no-slot inverse count为1-delta+2delta nu0；
若m<1/2而z_P<=nu0，zero-slot plain count<=1-delta+6delta nu0。
这两种邻域都用已指定小loss吸收，不能以趋零width调用marked moment。
若delta=alpha，adaptive t=3/2、actual r>=1-O(epsilon)，
(3)两支给count U^{1-delta+epsilon}(1+T1)^A；此时crossing capacity为0。
Bootstrap (2)下delta<=3/4<alpha，不会实际出现该端点。

## 8. 实际行数与量词顺序

前述spikes、width、系数类和supply逐前件支付后，实际count为

\[
 \#\mathcal B\ll
 U^{\max\{R_{\rm short}(t),L(t)\}+\Delta_{\rm eff}/4+\epsilon}
 (1+T_1)^A.
 \tag{12}
\]

对0<delta<alpha取

\[
 \mathcal J=(\alpha-\delta)D_x+\delta P_x,\qquad
 t=1+\frac{\delta P_x}{2\mathcal J},\qquad
 R_*=1-\delta+\frac{(\alpha-\delta)\delta P_x}{2\mathcal J}.
 \tag{13}
\]

D_x∈[37/18,3]、P_x∈[7/9,2]、J∈[35/54,5/2]、D_x-P_x>0，
所以1<t<3/2，R_short=L=R_*。含zero-capacity endpoint的统一结论是

\[
 \boxed{\#\mathcal B\ll U^{R_*+\Delta_{\rm eff}/4+\epsilon}(1+T_1)^A.}
 \tag{14}
\]

在(2)下loss Delta_eff/4为0。No-slot t=1还给
#B<<U^{1-2delta/3+epsilon}(1+T1)^A，不需prime supply。

量词顺序：先固定几何、bootstrap、bounded length范围与可支付count loss；
再选nu0、moments/mesh/rounding、K及windows，再选amplitude和prime-bound小loss。
目标确定后固定arithmetic datum、Theta、internal Sobolev/height阶，
所有retained Fourier变量共用一个累计T1/2预算。
随后取T1=Z^tau满足原height ceiling，tau可依赖已固定target/internal阶。
最后选external tail order并增大Z阈值。
更换external order不能改变已固定moment、mesh或height exponent。

本稿只认证actual counts；完整central error-slot×numerator联合界与(14)代入442后的
全部frequency saving仍需独立证明。原generic moments是确切[R]，没有新猜想前件。
详细准入推导见[独立容量报告](../reviews/2026-10-07/hybrid-effective-kappa-and-capacity-admission.md)。
