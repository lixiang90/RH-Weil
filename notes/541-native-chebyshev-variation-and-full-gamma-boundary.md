# 实际 Chebyshev 绝对变差不能由完整 Γ 的原域统一支付

2026-10-14；C012唯一准入轮，新增基线0c4f3a3/全部≤538。
本轮独立消费前轮[入口草稿](../reviews/2026-10-14/c011-second/full-gamma-signed-bridge-entry.md)，
下文给全连续对象、误差及量词；入口准备不重复计轮。
这是原实际算术primitive的支付法边界，非新正性或宏观Goal完成。
不使用ζ零点、矩阵、参数拟合、PNT渐近或数值producer。

## 1. 实际完整对象与两个准确中心化式

I_L=(-L,L)，L>0，Lebesgue norm；complex Cc∞源零延拓。
Ff(t)=∫f(u)e^(-itu)du，h_f(a)=∫f(u+a)overline(f(u))du，
k_f=Re h_f、N=||f||²、k(0)=N、k′(0)=0。
positive-definite相关不保证k(a)逐点非负。
完整actual Q保Γ(t)=Reψ_digamma(1/4+it/2)−logπ=2θ′、dual pole和所有primepowers：

    Q(f)=(2π)^-1∫Γ(t)|Ff(t)|²dt
          +2Re[Ff(i/2)overline(Ff(−i/2))]
          −2Σ_(p^j<e^(2L)) logp/√(p^j) k(log(p^j))。

ψ_Cheb(x)=Σ_(n≤x)Λ(n)右连续、ψ_Cheb(1)=0，E(a)=ψ_Cheb(e^a)−e^a。
全部权Λ(p^j)=logp，位移log(p^j)，端点相关为0，无漏primepower或half-atom。

由[NIST原digamma积分](https://dlmf.nist.gov/5.9#E16)对实部取差并作u=2a，

    Γ(t)−Γ(0)=∫_0∞w(a)(1−cos(ta))da，
    w(a)=2e^(-a/2)/(1−e^(-2a))，
    Γ(0)=−γ−π/2−3log2−logπ。

故完整positive jump能量（Tonelli，未裁尾）为

\[
J_\Gamma(f)=\frac12\int_0^\infty w(a)\|T_a f-f\|^2da
=\frac1{2\pi}\int[\Gamma(t)-\Gamma(0)]|Ff(t)|^2dt.\tag{1}
\]

T_a是全线酉translation。w~1/a近0，smooth源差平方O(a²)，远处指数衰减。
它与N给原Dlog闭型域的norm；不是更强的一阶导数norm。

准确双pole=4∫_0∞cosh(a/2)k(a)da=2(|C(f)|²−|S(f)|²)，
C=∫f cosh(u/2)、S=∫f sinh(u/2)。prime项为−2∫e^(-a/2)k dψ_Cheb(e^a)。
置z=e^(-a/2)k，连续prime主项与pole的2e^(a/2)项精确cancel。
E(0)=−1，z(0)=N，z在高端flat零；Stieltjes分部积分必须付

    ∫_(0,∞)z dE=N−∫_0∞E z′，z′=e^(-a/2)(k′−k/2)。

因此同一完整Q为

\[
Q=(\Gamma(0)-2)N+J_\Gamma+2\int e^{-a/2}k
                +2\int E(a)e^{-a/2}(k'-k/2).\tag{2}
\]

若A=E+1，则A(0)=0，等价式把质量常数改为Γ(0)。
两式不能混用并漏−2N。导数式先在smooth core消费；不预设每个Dlog源的k′费存在。
(1)–(2)是旧对象/规范恢复，不能登记为独立算术正性或研究轮。

## 2. 冻结真正可证伪的全源费用门

审查实际绝对支付费

\[
B_E(f)=2\int_0^\infty e^{-a/2}|E(a)|\,|k'(a)-k(a)/2|da,\qquad
B_A(f)=2\int_0^\infty e^{-a/2}|A(a)|\,|k'(a)-k(a)/2|da.\tag{3}
\]

候选消费门是每个fixed L存在有限c_L,d_L，使所有原complex smooth源满足

    B_E(f)≤c_L JΓ(f)+d_L N，                       (4)

或增强右侧为actual正prime图能量、positive pole及任意fixed-L bounded修复。
不是generic bad coefficient：E/A固定为实际全部Chebyshev primitive。
PNT等pointwise majorant即使按source选，只要仍逐点≥|E|，所得绝对费不会小于(3)。

## 3. 原合法源的严格线性费用及完整余项

任意L>0，冻结一小interval J⊂I_L，长度b<min(2L,log2)，
取real非负g∈Cc∞(J)，在其支持内部正并normalize N=1。
H(a)=h_g(a) smooth非负、支撑于[-b,b]，H(0)=1且在(0,b)中有严格正区间。
合法复载波f_ω=e^(iωu)g给k_ω(a)=cos(ωa)H(a)。
0<a<b没有实际primepower，故ψ_Cheb(e^a)=0、E(a)=−e^a精确，A(a)=1−e^a。
因此

    B_E(f_ω)=2∫_0^b e^(a/2)
        |−ωH(a)sin(ωa)+cos(ωa)(H′(a)−H(a)/2)|da。

用||x+y|−|x||≤|y|，去副项误差≤M_g=2∫e^(a/2)|H′−H/2|，有限且与ω无关。
再令P(y)=∫_0^y(|sin v|−2/π)dv。它有周期π且有界。
对smooth权φ，分部积分完整给

    |∫_0^b φ(a)(|sin(ωa)|−2/π)da|
       ≤||P||∞/ω·(|φ(0)|+|φ(b)|+∫_0^b|φ′|)。

φ_E=e^(a/2)H，φ_A=(e^(a/2)−e^(-a/2))H，二者都满足上述有限费用。
故不是仅ordinary平均或未支付o(ω)；严格得

\[
B_E(f_\omega)=\kappa_E\omega+O_g(1),\quad
\kappa_E=\frac4\pi\int_0^b e^{a/2}H(a)da>0,\tag{5}
\]
\[
B_A(f_\omega)=\kappa_A\omega+O_g(1),\quad
\kappa_A=\frac4\pi\int_0^b(e^{a/2}-e^{-a/2})H(a)da>0.\tag{6}
\]

起点改A(0)=0不能逃逸。真实权/完整norm/副项和周期平均误差均已付。

## 4. 完整 Γ 谱尾与实际正参考能量

主代理用谱侧、逆审用time-jump侧分别核下面费用。
由[NIST Binet原式](https://dlmf.nist.gov/5.9#E15)及digamma recurrence，
取z=5/4+it/2、z₀=1/4+it/2。|u²+z²|≥5|t|/4，原Binet remainder≤

    (8/(5|t|))∫_0∞u/(e^(2πu)−1)du=1/(15|t|)。

实部reciprocal为O(t^-2)，Re logz=log(|t|/2)+O(t^-2)。于是原同规范

    Γ(t)=log(|t|/(2π))+O(1/|t|)，|t|≥1，
    |Γ(t)|≤C+log(2+|t|)于全R。

令μ(s)=|Fg(s)|²/(2π)，∫μ=1且μ为Schwartz。
Ff_ω(t)=Fg(t−ω)，所以保完整谱尾的Γ-form为∫Γ(ω+s)μ(s)ds。
在|s|≤ω/2，|log(1+s/ω)|≤2|s|/ω，全部误差≤
(2/ω)∫|s|μ+O_g(1/ω)。在|s|>ω/2，ω≤2|s|，
Γ(ω+s)及logω的差绝对值≤C+2log(2+|s|)；乘Schwartz μ积分为O_g(1/ω)。
缺失mass乘logω亦由同一tail支付。因此

\[
\Gamma\text{-form}(f_\omega)=\log\omega-\log(2\pi)+O_g(1/\omega),\quad
J_\Gamma(f_\omega)=\log\omega-\log(2\pi)-\Gamma(0)+O_g(1/\omega).\tag{7}
\]

没有把频移后的tail当0，亦没有只比较有限band或令其compact消失。
独立time侧可把w=1/a+O(1)、H=1+O(a²)代入(1)，
余项绝对可积，主要∫_0^b(1−cosωa)/a=logω+O_g(1)，包含整个jump尾。

所有实际prime相关在该族上恰为0。actual partial graph能量E_a≤4N，
每个fixed L只有有限atoms，故ΣΛ(n)/√n E_logn=O_L(1)。
positive pole 2|C(f_ω)|²以及增强2|C|²+2|S|²均由smooth带Laplace权的Fourier
积分Schwartz下降。任意fixed-L bounded算子修复贡献≤||D_L||N=O_L(1)。
所以即使取正参考型

    P_L=JΓ+ΣΛ(n)/√n E_logn+2|C|²

并加入任意fixed-L bounded正修复和N，仍为logω+O_(L,g)(1)。
由(5)–(7)，B_E/P_L及B_A/P_L按κ·ω/logω无界，(4)及这些增强版本全部失败。
按P_L+N重新normalize也同样无界，因为所有费用对f具有degree2齐次性。
这严格排Dlog relative-form预算；不声称每个Dlog源已定义B_E或其值必为∞。

## 5. 真实 signed 费用和完整 Q 的方向

真正残差R_E=−2∫z dE在本probe上为2∫e^(a/2)cos(ωa)H(a)da→0。
对未取绝对值的(2)最后一项直接分部积分给

    2∫E z′=2N+2∫_0^b e^(a/2)cos(ωa)H(a)da→2N，
    2∫A z′=2∫_0^b e^(a/2)cos(ωa)H(a)da→0。

这与E0的−2N恰配；不是signed导数积分也线性爆炸。
完整pole Schwartz下降、prime项恰0、Γ-form由(7)增长，故

    Q_L(f_ω)=logω−log(2π)+O_g(1/ω)>0最终成立。

绝对费爆炸是支付法的损失，不能推Q负、RH失败或实际signed来源不存在。

## 6. 修复与源量词：哪些仍未排

各fixed L的常数/rank/norm可任意大，只要对所有源统一有限，carrier仍破坏(4)。
任意fixed bounded/compact正参考修复无法把logω变为ω。
同一actual点wise majorant≥|E|不救absolute费，即使这个majorant按source选择。

有限个L²-continuous线性条件也可保留反例：在上述J内取其受限image的fixed smooth
右逆v_j；weak-null carrier使所有条件值o(1)。加fixed span中的r_ω=o_(H¹)(1)
满足条件，仍support J且norm趋1。相关导数的cross费O(ω||r_ω||+||r_ω′||)=o(ω)，
故B_E=κ_Eω+o(ω)。positive Γ型Cauchy使JΓ变化o(√logω)+o(1)，所以JΓ/logω→1。
prime仍无相关，pole/bounded费有界；同一无界ratio保持。一般smooth分布条件未由此支付。

以下逃逸明确未排：频率依赖或source依赖的新参考能量/不统一常数；
删除无限源方向；真实signed primitive响应；source分块后joint交叉抵消；
用H¹等更强norm支付导数但另付成长/ζ消费责任；新的非局部算术或几何来源。
fixed-L B_E确可用const_L(√N||f′||+N)支付；它是更强norm费用，不是(4)。

## 7. 基线扣除、宏观影响与停止

016已有graph P−V及分别norm成长损失，041/237已有absolute丢振荡的思想边界，
252/292–300已有不同Abel/response的primitive端点与variation预算。
405/518是实际源/谱接口，不付独立符号。(1)–(2)也属于旧资产规范恢复。
本轮新增仅是冻结actual E/A和原Weil autocorrelation、比较完整Dlog/Γ+graph/pole
参考型的逐fixed-L无界命题与严格ω/logω费用；不声称外部首创。
定向旧件搜索与原文对象比较支持此扣除，不声称全文重审所有旧笔记。

它关闭“已有PNT pointwise包络即可付全source”的消费shortcut，
并将真正signed residual与其absolute费用严格分开。完整growth联合正性和Ξ识别仍未付。
C012一轮预算用尽，停止absolute-PNT包络主攻；本版Goal仍active，数学完成门open。
本结果不是独立正性，指定absolute费用边界未覆盖全部joint/source-adaptation核心，
不能凭此完成新Goal。重新准入须弱于wholeQ的实际signed响应原定理与全域消费桥。

本輪由原cadence3→4一次并作cycle10宏观复盘；审查/恒等式/合同停止不另计轮。
下一动作须由复盘选择明确新实际来源，不以another generic absolute反例继续消耗主攻。
