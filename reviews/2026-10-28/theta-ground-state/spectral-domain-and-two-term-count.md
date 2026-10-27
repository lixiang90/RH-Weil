# 固定theta基态谱：形式域、全整数尾与严格两项计数

2026-10-28；unit_height独占证明，C049。恢复STATE／D20261028P、同G20261027、[合同](../../../goals/contracts/C049-theta-ground-state-full-gamma-heat-gate.md)及root已消费的05251a4c…独立准入，check/show通过。固定原全整数Hθ、半线x与Dirichlet端点，不改sector／尺度／H幂／常数。无web／PDF／数值，不改STATE／cadence／合同／Git或其他稿。本文不代root消费，不独立计轮。

## 1. 本支结论与计数规范

采用405的真实整数源
\[
 H(x)=H_\theta(x)=
 2e^{x/2}\sum_{n\ge1}
 \pi n^2e^{2x}(\pi n^2e^{2x}-3/2)e^{-\pi n^2e^{2x}},
 \qquad x\ge0.
\]
H正、光滑、H(0)>0；405给其全线实偶S_exp来源。令
\[
 w=H'/H,\quad V=H''/H,\qquad
 q[f]=\int_0^\infty|f'-wf|^2dx,\quad
 f\in C_c^\infty(0,\infty).
\]

其Friedrichs闭包的**准确形式域**为
\[
 \boxed{\mathcal D(q)=H_0^1(0,\infty)
               \cap L^2((0,\infty),e^{4x}dx).} \tag{1}
\]
表示算子A自伴、非负、compact resolvent，且零不在谱中，故本征值按重数为
\(0<\lambda_1\le\lambda_2\le\cdots\to\infty\)。

定义本支计数只计每个半线本征值一次：
\[
 N_\theta(T^2)=\#\{j:\lambda_j\le T^2\}.
\]
存在仅依这一固定H的 \(C_\theta,T_\theta<\infty\)，使
\[
 \boxed{\left|N_\theta(T^2)
 -\frac{T}{2\pi}\bigl[\log(T/\pi)-1\bigr]\right|
 \le C_\theta\sqrt T(1+\log T),\quad T\ge T_\theta.} \tag{2}
\]
故余项为o(T)。本文**没有±谱的倍数2**；该倍数留给heat/source分支。没有用RH、零点位置、WKB或外部Weyl余项定理。

## 2. 全n导数尾：实际势而非n=1替身

写 \(z=\pi e^{2x}\ge\pi\)、\(a=3/2\)，n=1项为
\[
 H_1(x)=2\pi^2e^{9x/2}e^{-z}(1-a/z)>0.
\]
全和满足 \(H=H_1(1+\rho)\)，其中
\[
 \rho=\sum_{n\ge2}R_n(z)e^{-(n^2-1)z},\qquad
 R_n(z)=\frac{n^2(n^2z-a)}{z-a}
       =n^4+\frac{a(n^4-n^2)}{z-a}. \tag{3}
\]

用 \(D_x=2zD_z\)。对j=0,1,2,3，Leibniz和 \(z-a\ge(1-a/\pi)z\) 给
\[
 |D_x^j(R_n(z)e^{-(n^2-1)z})|
 \le C_j n^{4+2j}z^j e^{-(n^2-1)z}.
\]
因此由有限常数
\(\sum_{n\ge2}n^{4+2j}e^{-(n^2-4)\pi}<\infty\)，有
\[
 |D_x^j\rho(x)|\le C'_j z^j e^{-3z},
       \qquad x\ge0,\quad 0\le j\le3. \tag{4}
\]
这些同一可和majorant同时支付逐项求导及其一致性；没有只估函数尾后假定导数尾。

由于ρ≥0，分母1+ρ无零，(4)给
\[
 (\log(1+\rho))'=O(ze^{-3z}),\quad
 (\log(1+\rho))''=O(z^2e^{-3z}),\quad
 (\log(1+\rho))'''=O(z^3e^{-3z}).
\]
直接计算n=1的log导数：
\[
 w_1=\frac92-2z+\frac3{z-a},\qquad
 V_1=w_1^2+w_1'
 =4z^2-22z+\frac{33}4+\frac3{z-a},
\]
\[
 V_1'=16z^2-44z-\frac{6z}{(z-a)^2}.
\]
故全势满足
\[
 V-V_1=O(z^2e^{-3z}),\qquad
 V'-V_1'=O(z^3e^{-3z}), \tag{5}
\]
\[
 V=4z^2+O(z),\qquad V'=16z^2+O(z).
\]

尤其可选固定x₀≥1，使V在[x₀,∞)严格递增且为正，并可选固定C、C₀使
\[
 |V(x)-4\pi^2e^{4x}|\le C\pi e^{2x}\quad(x\ge0), \tag{6}
\]
\[
 2z^2-C_0\le V(x)\le6z^2+C_0,\qquad
 |w(x)|\le C(1+z). \tag{7}
\]
有限区间的常数由H正和光滑保证。这里校准了早期非正式常数项：81/4不是H₁的准确V常数；应保上式33/4及有理尾。本计数只用(6)–(7)，不依赖该常数值。

旧10-14已付H尾／V leading不再计作新结果；本段补齐本谱证明实际使用的全n导数、全局比较及终单调前件。

## 3. 原形式域、自伴实现和严格正谱

对core函数分部积分，端点项为零，得到
\[
 q[f]=\int_0^\infty(|f'|^2+V|f|^2)dx. \tag{8}
\]
由(7)，q加一个固定倍数的L²范数，与
\[
 \|f'\|_2^2+\|zf\|_2^2+\|f\|_2^2
\]
双向控制；因q≥0，q+||f||²也给等价范数。因此core闭包确为(1)，而不是无边界条件的maximal一阶域。

完整性与core稠密可直接核：先用尾cutoff在该weighted-H¹范数逼近；cutoff导数项由尾L²控制。对所得compact support、trace0函数，在固定有限区间按H₀¹用内部光滑函数逼近，权有界，故仍在同一范数收敛。反向的Cauchy极限在H₀¹及weighted L²中存在且一致。因此q闭、稠密、非负。由 \(|w|\le C(1+z)\)，(8)与原平方表达都连续延伸到同一形式域。

按已在项目闭形式处理中使用的Friedrichs／闭形式表示，得到唯一对应的非负自伴A。其准确算子域可写为
\[
 \mathcal D(A)=
 \{f\in\mathcal D(q): -f''+Vf\in L^2
       \text{（分布意义）}\},\qquad Af=-f''+Vf. \tag{9}
\]
光滑V给 \(H^2_{\rm loc}\) 正则性，原端点trace是f(0)=0；没有凭平方形式另加Robin条件。

形式域到L²的嵌入紧：有界形式球在[0,R]中H¹有界，可由有限分段平均逼近，L²误差≤mesh·||f′||₂；有限维逼近给compactness。尾部统一满足
\[
 \int_R^\infty|f|^2dx
 \le(\pi^2e^{4R})^{-1}\|zf\|_2^2\longrightarrow0.
\]
故全嵌入compact，A有compact resolvent。

若Af=0，则q[f]=0，局部一阶方程f′=wf给f=cH。H(0)>0而f(0)=0，迫c=0。零不为本征值；compact resolvent及非负性进一步给 \(\lambda_1>0\)。不能把全线的H基态误放入半线Dirichlet域。

## 4. 分割上下界：逐格取整误差有控制

以下所有区间分割都对(8)的**Schrödinger形式**进行：在人工切口加Dirichlet，或放松为独立H¹的Neumann区间。不得逐格继续写原平方形式而略端点项，否则会变成另一Robin问题。

固定足够大的T，置E=T²，要求E大于[0,x₀]上V的最大值及V(x₀)。由终单调，存在唯一 \(a_T>x_0\) 满足V(a_T)=E。由(7)，
\[
 a_T=\tfrac12\log T+O_\theta(1). \tag{10}
\]
取 \(\delta=T^{-1/2}\)，
\[
 m=\left\lceil\frac{a_T-x_0}{\delta}\right\rceil,\quad
 x_k=x_0+k\delta,\quad b_T=x_m.
\]
则m≥1，b_T≥a_T，且
\[
 m=O_\theta(\sqrt T(1+\log T)). \tag{11}
\]

Neumann尾区间[b_T,∞)没有≤E谱：V(x)>E对x>b_T成立，其Schr形式减E||f||²为非负且非零函数不可能取零。因此上计数不遗漏尾部，V(b_T)=E的可能端点也不产生零能态。

常势v、长度ℓ区间的DD谱为 \(v+(\pi k/\ell)^2\)、k≥1；NN谱取k≥0。按≤E计数，对所有v都有
\[
 \left|N_D(E;v,\ell)-\frac{\ell}{\pi}\sqrt{(E-v)_+}\right|\le1,
\quad
 \left|N_N(E;v,\ell)-\frac{\ell}{\pi}\sqrt{(E-v)_+}\right|\le1. \tag{12}
\]
在E=v时NN恰有一个态，仍在该误差内。这保留了整数恰落阈值的边界情形。

定义 \(F_T(x)=\sqrt{(T^2-V(x))_+}\)。在[x₀,b_T]上F_T递减，末端为0。每个cell的V介于两端值，故min–max／D–N bracketing及(12)给
\[
 \sum_{k=0}^{m-1}
  \left(\frac{\delta}{\pi}F_T(x_{k+1})-1\right)
 \ \le\ \text{tail-cell下计数},
\]
\[
 \text{tail-cell上计数}\ \le\
 \sum_{k=0}^{m-1}
  \left(\frac{\delta}{\pi}F_T(x_k)+1\right). \tag{13}
\]
左侧负项无害；它只是合法lower bound。

在初始有限区间[0,x₀]用V的最小／最大常势夹住DD／NN计数。由(12)，其上下界都是
\(x_0T/\pi+O_\theta(1)\)。
同时
\(\int_0^{x_0}F_T(x)dx=x_0T+O_\theta(T^{-1})\)。
原Dirichlet端点在下界保留；上界即使放松为NN也只多O(1)。

递减函数的左右Riemann和差恰为
\[
 \delta[F_T(x_0)-F_T(b_T)]\le\delta T
\]
（x₀已选V(x₀)>0）。故从所有cuts和常势比较合并可取
\[
 \left|N_\theta(T^2)
   -\frac1\pi\int_0^\infty F_T(x)dx\right|
 \le 2m+C_\theta+\frac{\delta T}{\pi}
 =O_\theta(\sqrt T(1+\log T)). \tag{14}
\]
这里每cell只用一次floor误差；不需要F_T在转折点有有界导数或Prüfer／WKB余项。

## 5. 实际势到纯指数势：误差为O(√T)

置 \(W(x)=4\pi^2e^{4x}\)，
\[
 I_V(T)=\int_0^\infty\sqrt{(T^2-V(x))_+}dx,\qquad
 I_W(T)=\int_0^\infty\sqrt{(T^2-W(x))_+}dx.
\]
用初等不等式
\[
 |\sqrt{A_+}-\sqrt{B_+}|\le\sqrt{|A-B|}.
\]
两积分在各自转折点之后为0；其支撑并集在
\([0,\tfrac12\log T+O_\theta(1)]\)，由(6)得
\[
 |I_V(T)-I_W(T)|
 \le C_\theta\int_0^{\frac12\log T+O_\theta(1)}e^x dx
 =O_\theta(\sqrt T). \tag{15}
\]
这一步保留全n势；不是将A替成n=1算子再假定谱相同。有限低势负区也已由同一全局(6)覆盖。

## 6. 纯指数积分的线性T常数

对T>2π，令 \(\alpha=2\pi/T\)。换元 \(y=2\pi e^{2x}/T\) 给准确式
\[
 I_W(T)=\frac T2\int_\alpha^1\frac{\sqrt{1-y^2}}y\,dy
 =\frac T2\left[
  \log\frac{1+\sqrt{1-\alpha^2}}\alpha
  -\sqrt{1-\alpha^2}\right].
\]
对0<α≤1/2，括号与 \(\log(2/\alpha)-1\) 的差被Cα²控制（直接用sqrt和log在该区间的Taylor余项界）。因此
\[
 I_W(T)=\frac T2[\log(T/\pi)-1]+O(T^{-1}). \tag{16}
\]

(14)、(15)、(16)给(2)，其中各常数独立于T。所需常数仅来自(3)–(7)的显式可和整数尾、固定x₀的有限区间bounds、每格的(12)和初等积分；没有新增外部谱渐近定理。

## 7. 可交付heat分支的范围与限制

可直接使用的谱前件是：固定半线Dirichlet实现(1)/(9)、\(\lambda_1>0\)、compact resolvent，以及按≤、含重数一次的严格(2)。特别
\(N_\theta(T^2)\ll_\theta T\log(2+T)\)。
由Stieltjes积分或分段求和，任意t>0有
\[
 \operatorname{Tr}e^{-tA_\theta}
 =\int_0^\infty e^{-t\lambda}\,dN_\theta(\lambda)<\infty.
\]
本支不加±的2、不移除虚构零模，也不改变原Dirichlet sector。

由计数到热的归一化常数、完整Γ目标、Gaussian共同cutoff及physical源费用由另一独占腿负责；在root对齐前不得只凭本计数声称已闭Weil分布运输。本支证明不产生RH反例、whole4/5改善、独立signed/corecross或一般confining类no-go。

原whole目标、物理时间u与算子坐标x、全部Γ/contact、properpowers、双pole和源成长量词继续分开。本文不混入另一个二维theta采样Gram，不优化参数或续算子recipe；实际数学轮与合同结算只由root在统一逆审后消费。
