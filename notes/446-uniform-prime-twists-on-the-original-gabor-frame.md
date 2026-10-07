# 446. 全导子条带输入进入原Gabor矩阵：真实四迹弱界与剩余阈值

2026-10-07。状态 [T/R]：引用全Hecke/Dirichlet 7/8、固定gap logarithmic-control、
原AF显式公式和二矩结果，得到同一个AF有限矩阵的四次迹弱界。
没有得到更高的简单临界线比例，也不将单变量规范系数替换为完整signed四点算术。
此接口的意义是明确能传递的估计及其尺度，不声称文献首创。

## 1. 输入与计数对象

固定[OpenAI September-30原稿](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)，
提交adc7f1241b42e322a6451854ab7e4b4c146bf78a，canonical LF SHA256
42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3。
另一输入为[Alpöge–Furman v2](https://arxiv.org/html/2608.13637v2)的原finite frame、
显式公式(2.11)、二矩及zero tail；[197](197-partial-weil-proportions-regions-four-moments.md)
和[198](198-quadratic-fourth-moment-vaughan-channel.md)的完整惯性/净四矩条件保留。
N=N(T,2T)计所有零的重数；比例目标为简单且在线的N0^s/N。
不将distinct、simple或central的不同计数互换。

以下theta=7/8。对每个fixed delta>0足够小，a=theta+delta<1。
Delta在导子、tau及长度之前固定，不取delta=1/log T。

## 2. 真正全导子、全高度的规范块

原`lem:logarithmic-control`的Euler logarithm、fixed-strip增长和
Borel–Carathéodory/three-circles/Cauchy证明，在全导子zero-free输入下给

\[
 |L(a+it,\psi)|+|L(a+it,\psi)^{-1}|
 \ll_{\delta,\epsilon}\{Q(3+|t|)^2\}^\epsilon,
 \qquad |L'/L(a+it,\psi)|\ll_\delta\log\{2Q(3+|t|)^2\}.
 \tag{1}
\]

固定F的degree为2；Dirichlet同样证明用degree-one增长。
Principal先regularize极点；固定线a<1离s=1正距离，log derivative加固定常数仍满足(1)。
Imprimitive原zero extension给L_orig=L_primitive prod_{p∈R}(1-psi(p)Q_p^{-s})；
记录Q_eff=Q_primitive N R，inverse另花(NR)^epsilon，log derivative另花O(log(2NR))。
全部Q_eff若没有polynomial范围就必须显式保留。
Pure norm twist只是L-argument变为s-i tau，不是新finite-order角色。

对固定annular smooth W，Mellin inversion与(1)给原canonical块

\[
 N^{-1/2}\sum\mu(\mathfrak n)\psi_{orig}(\mathfrak n)
 W(N\mathfrak n/N)(N\mathfrak n/N)^{i\tau}
 \ll N^{a-1/2}\{Q_{eff}(3+|\tau|)^2\}^\epsilon,
 \tag{2}
\]
\[
 N^{-1/2}\sum\Lambda_F(\mathfrak n)\psi_{orig}(\mathfrak n)
 W(N\mathfrak n/N)(N\mathfrak n/N)^{i\tau}
 =1_{principal}N^{1/2}\mathcal MW(1+i\tau)
 +O\bigl(N^{a-1/2}\log(2Q_{eff}(3+|\tau|))\bigr).
 \tag{3}
\]

移线到a，fixed profile的Mellin transform任意阶衰减，horizontal joins由全height(1)处理。
Principal主项在tau≈0为O(sqrtN)，在|tau|~T以profile衰减；不能全局删掉。
这些估计只适用于生成函数恰为1/L或-L′/L的canonical系数，
fixed finite-ray角色组合可逐项用；一般bounded a_n不因此获准。
共同Fourier分离另需对应weighted L1 seminorm，prime系数仍必须row-independent。

## 3. 原sharp Lambda前缀：uniform Perron

AF实际前缀是Q_X(tau)=sum_{n<=X}Lambda(n)n^{-1/2+i tau}，
prime multiplier P_X(tau)=-pi^{-1}Re Q_X(tau)。保留sharp cutoff和原权重。
取x=floorX+1/2，c=1/2+1/logx，Y=(2x(3+|tau|))^4。
截断Perron为integral_{c-iY}^{c+iY}D(s+1/2-i tau)x^s ds/(2pi i s)，D=-zeta′/zeta。
原系数模与tau无关；x离每个整数至少1/2，近端harmonic sum与远端absolute series给
O(sqrtx log²(2x)/Y)截断误差。
移至Re s=a-1/2>0，s=0留在左边，唯一跨越的pole是s=1/2+i tau。
其留数为x^{1/2+i tau}/(1/2+i tau)。
Horizontal joins离该pole且Y>|tau|+2，(1)控制D；左线的1/s只花logY。
因此

\[
 Q_X(\tau)=\frac{x^{1/2+i\tau}}{1/2+i\tau}
 +O_\delta\bigl(X^{a-1/2}\log^2(2X(3+|\tau|))\bigr).
 \tag{4}
\]

在T/2<=tau<=3T可得
|Q_X|<<X^{a-1/2}log²(2XT)+sqrtX/T。
在tau≈0必须保留真实principal项或原绝对sqrtX界。
这里的tau是下一节原积分的绝对高度，不是某个four-cycle的时间差。

## 4. 同一finite frame的Bessel与外侧定位

令L=log(T/(2pi))、X=e^L~T，phi为AF原real even taper，support长度L、0<=phi<=1、
||phi″||1有uniform界，a_L=||phi||2²/L最终离零。
原grid alpha_k=T+2pi k/L∈[T,2T)，0<=k<d，d~TL~N。
定义f_k(tau)=hat phi(tau-alpha_k)、Uz=sum z_k f_k。
原prime channel正是

\[
 V=(a_LL^2)^{-1}U^*M_{P_X}U.
 \tag{5}
\]

Plancherel和长度L区间上原grid的正交性给||U||²<=2pi L。
令J=[T/2,3T]，只在J上应用(4)：

\[
 \|V_J\|_{op}\ll
 [X^{a-1/2}\log^2(2XT)+\sqrt X/T]/L.
 \tag{6}
\]

J外可能包含tau≈0，故不使用高height前缀界。
每个alpha_k距J外至少T/2，原real-axis二阶Fourier尾给

\[
 \operatorname{Tr}(U^*1_{J^c}U)
 =\sum_k\int_{J^c}|f_k(\tau)|^2d\tau
 \ll dT^{-3}\ll L/T^2.
 \tag{7}
\]

该矩阵positive，op不超过trace。
保留全高度|P_X|<<sqrtX后，
||V_{Jc}||op<<sqrtX/(LT²)。
这逐项支付了低绝对高度principal的费用。
合并X~T得||V||op<<delta T^{3/8+delta}logT。
原gamma density在J内O(L)，在J外把log权重加入(7)仍可控；
原pole multiplier在J内O(sqrtX/T)，外部用O(sqrtX)及(7)。
故原完整背景压缩减I的op=O(1)，无需另造translation-invariant模型。

## 5. 实际centered四迹的弱界

AF原等式G+E=I+A+V中，||A||op=O(1)，原zero-tail[R]给||E||1=o(1)。
因此||G-I||op<<1+T^{3/8+delta}logT。
G为Hermitian：原real even phi使反射配对零的矩阵项互为共轭；
同一finite row set保留这个配对，不能单独删离线partner。
AF原dimension/trace/二矩给
||G-I||HS²=TrG²-2TrG+d=O(N)。
对该同一Hermitian矩阵，lambda^4<=||G-I||op² lambda²，故

\[
 \boxed{N^{-1}\operatorname{Tr}(G-I)^4
 \ll_\epsilon T^{3/4+\epsilon}.}
 \tag{8}
\]

选固定delta小于epsilon/4后吸收logs；常数可依赖epsilon。
这是实际四迹弱上界，较直接absolute prime前缀的T^1尺度有power节省。
它随T增长，不能代入197改善比例所需的固定constant四矩预算。
没有将signed words拆开取绝对值，也没有把canonical moments直接当成response四点均值。
对一般fixed theta>1/2，同方法只给T^{2theta-1+epsilon}。
若接受445的引用证明，指数仅变为29999/40000+epsilon，仍为增长幂。
此处不声称所有moving-q AF矩阵的一致二矩，后者需另证。

## 6. 真短窗与两个准确尺度阈值

固定w∈C_c^infinity((-1,1))，H<=X/2、eta=H/X，W_eta(y)=w((y-1)/eta)。
Substitution y=1+eta u和integration by parts给
|MW_eta(a+it)|<<eta(1+eta|t|)^{-A}。
因此Mellin amplitude eta与frequency width eta^{-1}抵消；
integral |MW_eta|log^r(2Q_eff(3+|t-tau|))dt
<<log^r(2Q_eff(3+|tau|+X/H))。
对真正canonical b_1=Lambda、b_2=Lambda*Lambda的D(s)^r生成函数移线得

\[
 \sum_n b_r(n)\chi(n)w((n-X)/H)(n/X)^{i\tau}
 =\mathcal P_{r,\chi}+O\bigl(X^{\theta+\delta}
 \log^r(2Q_{eff}(3+|\tau|+X/H))\bigr),\quad r=1,2.
 \tag{9}
\]

Nonprincipal P=0；zeta r=1主项为对应积分，r=2为
integral w((x-X)/H)(x/X)^{i tau}(logx-2gamma)dx。
Imprimitive principal用真实Laurent常数，有限删除不改最高pole阶。
此接口要给o(H)的power控制，充分条件为H=X^xi、xi>theta。
它是这一解析接口的阈值，不是所有可能方法的不可能性定理。

Actualfourthprime词的双product长度X~T²、near difference H~X/T~T。
因此(9)误差相对H为T^{2theta-1+2delta}，
7/8时是T^{3/4+2delta}。即使按sqrtX正规化仍超过constant-scale目标。
这个接口要取得power-small误差需theta<1/2；theta=1/2只到临界，logs和相关算术仍待支付。
微小边界改善不解决此尺度问题。

Long-prime二矩若X=T^b、H=X/T，误差相对H为
T^{1-b(1-theta-delta)}。它要求b(1-theta)>1；7/8下为b>8。
接受445后也仅改为b>80000/10001，并不能处理b略大于1的目标区间。
原AF long-prime offdiagonal仍需真正双变量相消。

## 7. 全导子能传到加性相位，但有费用和截断缺口

单位群上的e(an/q)，(a,q)=1，可展开为sum_{chi modq}c_chi chi(n)，
Parseval给sum|c_chi|²=1，故sum|c_chi|<=sqrt(phi(q))。
(9)因此给coprime canonical加性短窗的error
sqrt(phi(q))X^{theta+delta}log^r(2q(3+|tau|+X/H))。
这是全导子输入的真实one-point传递；不能丢sqrt(phi(q))或原nonunit masks。
q=1时上述双product尺度已经过大，增加moduli不自动产生平均相消。

Actualprime square的系数是

\[
 C_{2,T}(m)=m^{-1/2}\!
 \sum_{\substack{ab=m\\a,b\le T}}\Lambda(a)\Lambda(b),
 \tag{10}
\]

并有原taper/response权重。m~T²处的双截断不能替换为完整D(s)^2的系数。
更未由(9)得到sum_{h~T,m~T²}C_{2,T}(m)bar C_{2,T}(m+h)K_T(m,h)
的signed净预算。真实四迹还含背景、3+1/4+0等mixed words。
原marked inverse必须canonical mu和row character，原plain第四矩也有限定Theta、mesh、
length-width和masks；这些不是任意response-dependent coefficients的定理。

可传入的新增input为(2)(3)的canonical Type-I块与全导子one-point加性界。
下一实质任务是保留(10)截断、原response kernel和全部signed mixed corrections的
Type-II/dispersion或shifted-convolution均值，达到constant-size一侧Gram净预算。
本稿没有改进67.250070…%的比例主常数，也没有宣布任何新的比例记录。

完整独立推导及来源范围：[uniform reciprocal / fourth trace报告](../reviews/2026-10-07/hybrid-uniform-reciprocal-and-fourth-trace-interface.md)。
旧225–226已有pure-prime transfer和背景比较；232的逆审随后定位到
ab>XL²的真实high-product漏区，239–240把当前缺口准确写为共同centered的
Möbius divisor response及adjacent-divisor mean-square。
后续应直接接这些保留six-window/finite-band的实际对象，而不重列已付通道。
