# 实际高矩全频账本成立，完整谱净改善未通过

2026-10-14；C013首个完整准入轮，冻结基线0c4f3a3/全部≤538。
新增是实际坏频集的成长all-band算术预算；合同所需whole谱净后果失败，应一轮止损。
独立原件：[全band推导](../reviews/2026-10-14/c013-moments/growing-measure-derivation.md)、
[source/成长范围](../reviews/2026-10-14/c013-moments/source-and-growth-scope-audit.md)、
[完整惯性及更强基线逆审](../reviews/2026-10-14/c013-moments/whole-inertia-reverse-audit.md)。
不调用ζ零点、矩阵、拟合、盲增N或数值producer；不完成本版宏观Goal。

## 1. 完整对象和准确有限输入

L≥1，I=(-L,L)，原Lebesgue L²与complex Dlog闭型域、零延拓。
Ff(t)=∫f(u)e^(-itu)du，actual Γ=Reψ(1/4+it/2)−logπ=2θ′，Γ0=Γ(0)。
X=e^(2L)，保全部strict primepowers：

    P_L(t)=Σ_(p^j<X) logp/p^(j/2) exp(itlog(p^j))，S_L=Σ_(p^j<X)logp/p^(j/2)，
    P_1(t)=Σ_(p<X)logp/√p exp(itlogp)，V_L=Σ_(p<X)(logp)²/p，
    R_pp(L)=Σ_(p^j<X,j≥2)logp/p^(j/2)，|P_L−P_1|≤R_pp。

实际multiplier b_L=Γ−2ReP_L，E_L={t:b_L(t)<1}；Q_L精确为

    (2π)^-1∫b_L(t)|Ff(t)|²dt+2|C(f)|²−2|S_pole(f)|²。

dual pole未删除；C=∫f cosh(u/2)、S_pole=∫f sinh(u/2)。
不同source/域/规范的旧二矩不能直接消费到这里。

## 2. 一级均值、重复prime与所有误差

消费[Montgomery–Vaughan1974原文](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)
Theorem2(1.6)/Corollary2(1.8)的最小spacing Hilbert界；两endpoint给2π。
Corollary3只给绝对O(n)版本，不能把显式2π归到它。
有限Σ_(n≤N)a_n n^(it)在任意起点的长T区间有

    ∫_[T,2T]|Σa_n n^(it)|²dt≤(T+2πN)Σ|a_n|²。

P_1^k按prime指数向量α、Σα=k聚合，系数为(k!/∏α_p!)∏a_p^α_p。
因k!/∏α_p!≤k!，multinomial平方和≤k!V_L^k。对所有整数k≥1，

\[
\int_T^{2T}|P_1(t)|^{2k}dt
 \le (T+2\pi\lceil X^k\rceil)k!V_L^k.\tag{1}
\]

碰撞/重复prime、k增长与长度X^k均保留。MV和factorial是旧工具，不孤立登记新成果。

由[NIST Binet原式](https://dlmf.nist.gov/5.9#E15)，z=5/4+it/2、recurrence与
|u²+z²|≥5t/4给remainder≤1/(15t)。两reciprocal费≤1/t、2/t，故

    Γ(t)≥log(t/(2π))−46/(15t)≥logt−G，t≥1，G=log(2π)+46/15。

定义Y=2S_L+G+1、Ω=e^Y。所有|t|≥Ω上b_L≥1，E_L有界开集，真正tail精确为空。
正band T≥1，D=G+1+2R_pp、u(T)=(logT−D)/2；若u>0，(1)给

\[
|E_L\cap[T,2T]|\le\min\{T,
 (T+2\pi\lceil X^k\rceil)k!V_L^k/u(T)^{2k}\}.\tag{2}
\]

u≤0时付整块T。负频由于b_L偶对称精确乘2，不把density当绝对measure。

## 3. 无PNT的成长全band预算

自含central-binomial估计给ψ(x)≤Cψ x、ψ(x)≥cψ x于大x，
可用Cψ=4log2、cψ=(log2)/2、lower x≥16。原推导§4付所有整数/strict端点。
partial summation给S_L≍e^L、logS_L=L+O(1)、V_L=O(L²)、R_pp=O(L)。
高幂j=2的绝对质量为O(L)，不是O(1)；j≥3由收敛Σlogn/n^(3/2)支付。

冻结M=4V_L/L、H=max{L³,4D,4L,4M}，T0=e^H。完整低head付2e^H。
若Y≤H则J=0；否则J=ceil((Y−H)/log2)，T_j=T0·2^j、y_j=logT_j、
k_j=floor(y_j/(2L))、0≤j<J。最后band允许overshootΩ，只会多付。
所有使用band有u_j>0、k_j≥1、X^k≤T_j，ceilX^k≤T_j+1≤2T_j。
准确有限all-band ledger为

\[
U_L=2e^H+2\sum_{j<J}\min\{T_j,
 (T_j+2\pi\lceil X^{k_j}\rceil)k_j!V_L^{k_j}/u_j^{2k_j}\},
\qquad |E_L|\le U_L.\tag{3}
\]

y≥H时kV/u²≤M/y≤1/4，k!≤k^k和floor费用给

    |E∩[T,2T]|≤(1+4π)exp F_L(y)，
    F_L(y)=y−(y/(2L)−1)log(y/M)。

prime2的V下界与Chebyshev上界使log(Y/M)=L+O(logL)，
所以F′=1−[log(y/M)+1]/(2L)+1/y在全部H≤y≤Y最终统一正。
F(Y)≤S_L+O(S_L logL/L+L)，J=O(S_L)的求和对数费仅O(L)，H=O(L³)=o(S_L)。
因此新的actual全band预算严格给

\[
\log(1+|E_L|)\le\log(1+U_L)
 \le S_L+O(S_L\log L/L+L^3).\tag{4}
\]

O常数绝对，未用PNT/零点位置。相同head/bands/threshold的k=1上预算U_L^(2)
有log(1+U_L^(2))=2S_L+o(S_L)；其lastband T=e^(2S+O1)、u=S+O(L)
和V正上下界直接核出。这只证明两个certified upper ledgers的严格差异，
不是实际E的lower、最优性或whole谱净改善。

## 4. Whole-source运输成立，但必须比较更强旧资产

b_L≥−B、B=2S_L−Γ0。原time-frequency concentration算子K_E的trace=L|E|/π。
对任意严格负m维型子空间，交ker S_pole后至少m−1维；每个norm1源有
⟨K_Ef,f⟩>1/(1+B)，正even pole保留。Bessel/trace求和给安全整数门

    n_−(Q_L)≤floor[(1+2S_L−Γ0)L|E_L|/π]+1。

此桥来自旧027，对全部complex Dlog和重数成立，不是finite matrix门。
联(4)的leading S_L界是真命题；然而只以旧Fourier absolute的2S_L作对照是错误的。

旧[016 §§1、5](016-prime-graph-hodge-inequality.md)已付exact正prime图能量减degree：

    D_L(u)=A_<(e^(L−u))+A_<(e^(L+u))，a.e. |u|<L，
    A_<(x)=Σ_(n<x)Λ(n)/√n。

一步cutoff≤e^L、另一步<X，故完全有限M_old=S_L+A_<(e^L)满足
||D_L||∞≤M_old。strict/closed差仅有限u，essential sup与型积分不变。
actual规范纠错不影响图恒等式；完整Q已给

    Q_L≥Γ-form−M_old N+2|C|²−2|S_pole|²。

更强的是旧[028负迹](028-core-renormalized-negative-trace.md)，不能只取027的粗计数。
对H_Γ=Γ_I−M_old，n_−(H_Γ)≤Tr(H_Γ−1)_-，旧Bessel负迹给

    n_−(Q_L)≤1+(L/π)∫_R[M_old+1−Γ(t)]_+dt。

|t|≤1用Γ≥Γ0，|t|≥1用paid Γ≥log|t|−G；
∫_1^(e^a)(a−logt)dt=e^a−a−1，a=M_old+1+G。因此

\[
n_-(Q_L)\le1+C L e^{M_{\rm old}},\qquad
\log(1+n_-(Q_L))\le S_L+A_<(e^L)+\log(1+L)+O(1).\tag{5}
\]

A_<(e^L)=O(e^(L/2))远小于(4)的O(S_L logL/L+L³)。
这些是≤538资产准确组合的强后果，不登记为新forcing或另外一轮。

若另消费016已有PNT渐近A(x)~2√x，甚至有||D_L||∞=S_L于所有充分大L：
较小cutoff<2时该项为0；否则较大≤X/2、较小≤√X，
D≤A(X/2)+A(√X)<S_L最终成立。endpoint小条带上全部原atoms都入一侧，D=S_L。
所以旧negative-trace基线还给n_−≤1+C L e^(S_L)，非新的C013结论。

## 5. 准入判定、停止与下一实际输入

本轮(3)/(4)是新actual坏集算术预算，完整运输也真；但其whole上界被更强旧degree/负迹基线覆盖。
C013的严格净谱门不通过，立即停止，不优化k、微常数或增N维持成功叙述。
实际正性/Ξ瓶颈没有缩小；改变的是对照基线与行动优先级。
不能将本轮强旧资产恢复、generic MV/k!/trace或止损写成宏观成果；Goal仍active。
原cadence仅结算本次完整新all-band准入/逆审一次，旧资产恢复和各审查另计零轮。

下一C014保留D_L(u)实际空间profile而不抽全局sup，审完整Γ的killed jump heatkernel
与bounded-potential trace运输。候选弱门是s>1时

    n_−Q≤1+CΓ(s)∫_I e^(sD_L(u))du，CΓ(s)=(2π)^-1∫e^(-sΓ(t))dt。

只讨论Γ的正jump semigroup，不消费529已排的wholeQ标准锥保正。
s↓1的CΓ(s)发散、actualstep profile与primepower端点都必须付，
PNT的o(S)不能无声进指数；新的scalar arithmetic record可能提供可核cofinal profile输入。
准备不计C014轮；只有完整新joint运输和超最强(5)的实际净后果才可晋级。
