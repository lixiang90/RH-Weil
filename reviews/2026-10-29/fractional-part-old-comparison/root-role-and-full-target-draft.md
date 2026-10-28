# 固定fractional-part核的角色、Pan与完整目标：强旧0

2026-10-29。待本次两个独占旧范围稿及不同fresh/root最终消费；不是C054/591，不是新来源/数学轮。只固定root-fixed-rule中的h、J、B，不另选权或target。

## 1. 对象与原范数

h(u)=e^(-u/2){e^u}，u∈R。u<0时h=e^(u/2)，u≥0时0≤h≤e^(-u/2)。所以h∈L¹∩L²(du)，||h||₁≤4，M=||h||₂²≤2，且h≠0。对任意complex physical r∈L²(du)定义Jr=h*r；Young给||Jr||₂≤4||r||₂。h是receiver/convolution核，r仍是原physical源，不能把h改称405关系或几何primitive。

采用rhat(t)=∫r(u)e^(-itu)du，Plancherel测度dt/(2π)。令s=1/2+it，x=e^u给

    H(t)=∫_0^∞{x}x^(-s-1)dx=−ζ(s)/s，
    B_NB(r,s0)=〈Jr,Js0〉
             =∫rhat(t)overline(s0hat(t))|H(t)|²dt/(2π)。

上式积分在0、∞绝对收敛：0<x<1处{x}=x；∞用{x}≤1。Mellin恒等式是081§3原输入，不由RH推出。第一槽linear，s0为第二源而s为Mellin变量。ν_NB=|H|²dt/(2π)为正有限测度，质量M≤2；不额外添2π。

081的原空间L²((0,∞),dx)及r_n(x)={1/(nx)}由酉映射

    (Uf)(u)=e^(-u/2)f(e^(-u))

送到同du空间，且U r_n=n^(-1/2)h(u−log n)。这是integer dilation features的同一完成化，不是新的两源输入。原targetχ=1_(0,1)另送为e^(-u/2)1_(u>0)；不能把targetχ与h/J或原Weil源互换。原RH等价的d_N只针对n≥1的整数右半群features/Dirichlet系数及该target。当前J若允许任意全R的Cc∞源，则因H非零a.e.，其L²乘法range已无条件稠密；Cc∞于L²稠密及J有界使J(Cc∞)同样稠密。该放宽range的distance消失不是RH，丢失了整数半群限制。有限正Gram或写成B_NB均不支付原081受限d_N消失。

## 2. 不消实际Pan：在原physical角色首检

用405§4–5实际Gaussian源η_0给出的非零p=(D²+D)h_405∈P_an。它在原bare S_exp中，两矩恰为0，

    M_p(z)=z(z−1)ξ(z)/2，M_p(2)=π/6≠0。

令r_p(u)=e^(u/2)p(u)，这是原physical非零S_exp源，保持全部非compact尾。其Fourier值为M_p(1/2−it)，非零整函数在real轴只可能有离散零。H(t)=−ζ(1/2+it)/(1/2+it)也不恒零，real零离散。因此

    B_NB(r_p,r_p)=∫|r_phat(t)|²|H(t)|²dt/(2π)>0，

而405完整Weil配对Q_W(r_p)=0，且与全部S_exp源的mixed值为0。不是漏掉双pole：405已令d(p)=c(p)=0，并在含contact的完整身份中消去关系。

这也可直接由553更强旧后果看出：J有全局du（从而Hlog）有限界，若还消全部Pan及平移，就必须为0；本J非零且Fourier乘子a.e.非零，实际上在L²上injective。这里没有声称553适用于所有强拓扑、有费无界或逐层D′机制；它只正确作用于当前h的全局有界J。原p是noncompact，未冒充紧支测试。

若有人只主张B_NB=Q_W在全部原compact complex源成立，仍不能避开：固定光滑crop χ_R r_p→r_p于S_exp；405完整Q的S_exp连续性与J的L²连续性允许取极限。如此会强迫上面两个不同的对角值相等，矛盾。这是固定h的全目标角色失败，非经典Q存在负源、非RH反证。

## 3. 有限谱质量给同一个更早旧atom门

令W_NB(φ)=∫φhat(t)dν_NB(t)。其physical核连续有界，|W_NB(φ)|≤M||φ||₁≤2||φ||₁。完整目标保

    W_ζ=W_Γ+2cosh(u/2)du
        −Σ_(n=p^k≥2)Λ(n)n^(-1/2)(δ_log n+δ_(-log n))，

并保Γ的FP/contact及Λ(p^k)=log p。取a=log2及充分小fixed邻域U避开0与其它primepower，W_ζ|U=−c₂δ_a+b(u)du，c₂=log2/√2，b光滑。任取0≤η∈Cc∞(−1,1)、η(0)=1；选一次固定ε使support ψε⊂U且

    (2+||b||∞)ε||η||₁≤c₂/2，ψε(u)=η((u−a)/ε)，

则|W_ζ(ψε)−W_NB(ψε)|≥c₂/2。

这是421及10-28 Gaussian最强旧atom门的直接代入，不是新591。一般非负线性ψε不是Weil卷积平方，不能据此宣称Q_W负。Stationary Hermitian两源身份若对所有compact complex r成立，可由极化及卷积近似恒等元确定整份分布；所以上述差异确实拒绝完整身份，而非只拒绝一种记号。

固定h无成长族；禁止把它的有限质量失败加总成所有Nyman、growing mass、非局部、signed或source-adaptive机制的失败。它也不禁止Nyman RH等价判据本身成立。这里拒的是把现成fractional-part正核直接当完整Weil或同非零primitive的关系下降。

## 4. 强旧净后果与停止

081已给独立真实fractional-part Hilbert carrier及有限Gram；087–097有actual constrained response/局部parabolic/cotangent/gcd算术，不能从“joint非零”再付一次。当前核读另发现091一般δ的two-distinct-residue/even-g句缺p∤δ前件，受影响消费先冻结；δ=±1及exact有限T_g筛不受此纠正影响，须据本轮纠错原件重闭后才引用其准确范围。553已给全局有界关系下降的障碍；421/10-28 atom已给bounded finite-mass全目标障碍。当前两个首检全是旧直接后果，不是新方法类边界。

扣上述最强旧后，本h/B未提供新signed core/cross、actual q_r/principal或mixed RR/整截面身份，whole542+555→557 leading4/5负惯性UPPER不变，关键瓶颈不变。Source0，math0，原cadence0/history54/latest590/formal18保持；无C054/591/参数或来源后继。重新考虑须实际不同独立输入及可改变选择的test，不能只把distance/core缺口改名为“joint arithmetic”。

本稿使用项目原件081、405、553与10-28 Gaussian已消费atom段，不新读外部primary/PDF，不把附文指令当授权。Root最终须对齐两个支持本次终稿、原件版本与实际进程后才消费本稿。
