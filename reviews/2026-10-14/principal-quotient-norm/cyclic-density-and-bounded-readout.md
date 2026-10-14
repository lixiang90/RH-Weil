# Principal quotient norm：实际中心化cyclic密度与bounded readout

2026-10-14，独立推导及范围审查；只写本稿，不改STATE/cadence/Git。
按AGENTS恢复README/STATE/check-show、同Goal/frontier、D20261014AA、唯一next-principal
norm门、405/406/518/519/523/526与552。结构check不认证数学。
入口HEAD `1d48bd538cd176091dbec90eeca46253a1473d70`；root正在编辑STATE及git属性。
子get_goal=null，不代root同epoch观察。固定基线0c4f/≤538；本稿不计轮、不建合同。

**先扣强旧：** 523§2–3已有actual Gaussian关系像在全部single-line L²及固定阶Sobolev
完成中稠密的同一证明；405已给非零p∈P_an。将p代入该证明，并加标准weighted版本，
即得下面门。Hlog还可由H¹版本直接蕴含。因此本稿是原对象/关系范围及norm责任的
准确恢复，**不是新的宏观方法类边界或算术input**。以下仍将完整假设逐项付清。

## 1. 原source、physical中心化与实际平移

405固定实Fréchet空间

    F_R=S_exp={f smooth real: sup_u e^(N|u|)|f^(j)(u)|<∞，ALL N,j}。

519已识别I=E(S_even,0)=完整ζ-zero-jets关系理想，
P_an=I∩ker c∩ker d；F_C、I_C、P_an,C是明确complexifications。
中心化map C f(u)=e^(u/2)f(u)是F_R/F_C上的连续线性同构；
physical Fourier固定hat r(t)=∫r(u)e^(−itu)du、Plancherel因子1/(2π)。

旧实际Gaussian

    η₀(r)=(4z⁴−28z³+41z²−9z)e^−z，z=πr²，
    p=Eη₀=(D²+D)h，p≠0，p∈P_an，
    r_p=Cp=e^(u/2)p(u)。

p及所有导数两端比任意指数快；故r_p是Schwartz，也属于下面每个有限Sobolev空间。
所有real a的τ_a p(u)=p(u−a)仍在P_an：
真实η_a(r)=η₀(e^−a r)保源准入，M_(τ_ap)(s)=e^(as)M_p(s)保全部必要jets，
c/d只乘非零标量而其原值零。准确physical关系是

    C(τ_a p)=e^(a/2)τ_a r_p。                       (1)

所以centered principal空间C(P_an)含r_p的全部ordinary translates，
并非在两个不同坐标中无声使用同一个τ。
中心化群V_a=e^−a/2τ_a在C下恰变ordinaryτ_a。

## 2. actual Fourier式与非零a.e.，不假设RH

405的准确Mellin式M_h(s)=ξ_Riemann(s)/2与分部积分给

    M_p(s)=s(s−1)ξ_Riemann(s)/2，
    hat r_p(t)=M_p(1/2−it)
       =s(s−1)ξ_Riemann(s)/2，s=1/2−it。            (2)

M_p entire且不恒零，已由M_p(2)=π/6核非零。
因此(2)在任何fixed竖线上零集局部离散，实t的零集测度零：

    hat r_p(t)≠0 for almost every t∈R。              (3)

不用证明ζ零点在中心线、简单或有spacing lower；其中存在临界零点也不影响a.e.结论。
对于real p，functional equation/sharp给r_p real-even，但下面复密度不需要even性。
“非零a.e.”不能升级成逐点lower bound；在ζ零点附近不允许免费除以hat r_p。

## 3. Weighted cyclic lemma：full源与拓扑的自含证明

取measurable spectral weight W(t)≥1、finite a.e.，定义

    H_W={r∈L²(R,du): ||r||²_W=(2π)^−1∫W(t)|hat r(t)|²dt<∞}。

它是Hilbert，translations是unitary；假设r_p∈H_W。
则

    closure_H_W span_C{τ_a r_p:a∈R}=H_W。           (4)

证明：若g∈H_W正交全部translates，linear-first Plancherel给

    ∫ A(t)e^(iat)dt=0，ALL a∈R，
    A(t)=W(t)hat g(t)overline(hat r_p(t))。

weighted Cauchy–Schwarz给A∈L¹；Fourier唯一性得到A=0 a.e.。
为避免引用不明域的Tauberian定理，这里L¹唯一性可直接由Gaussian近似恒等元证明：
A*G_ε的每个点由Fubini和Gaussian逆Fourier写成零Fourier值的积分，所以A*G_ε=0；
G_ε在L¹是approximate identity，ε↓0得A=0。
再由(3)及W>0得hat g=0，因此g=0。这证(4)。

取W_log(t)=1+log(2+|t|)，Hlog=H_(W_log)。actual543给

    ||r||²+JΓ(r)=(2π)^−1∫[1+Γ(t)−Γ(0)]|hat r(t)|²dt，
    Γ(t)=Reψ(1/4+it/2)−logπ=actual2θ′。

此范数与Hlog等价，域为全line zeroextension Dlog；不是regional/periodic Γ。
所以(1),(4)准确给

    closure_L² C(P_an,C)=L²(R;C)，
    closure_Hlog C(P_an,C)=Hlog。                    (5)

这里**全line**r_p、所有real translates均合法。
fixed-support I_L 的closed form域不是这个cyclic对象；r_p的尾并未截掉。

对每个fixed有限real s≥0，可取W_s=(1+t²)^s；或取
W_(s,log)=(1+t²)^s[1+log(2+|t|)]。
r_p Schwartz保证r_p∈这些H_W，故(4)/(5)同样成立。
固定整数k的normΣ_(j≤k)||D^jr||²与W_s,k版本等价，正是523§3旧范围。
有限个这类translation-invariant spectralnorm之和仍是一份此类weight，不能靠
追加有限阶导数保一个非零principal Hilbert商。
本稿不声称任意physical-u权、多线指数权或所有Fréchet拓扑有同一密度。

**实组别。** 对本稿各even positive W，real functions形成real Hilbert子空间H_W,R。
若real g正交span_R translates，A(−t)=overline(A(t))，上述Fourier积分本来为real；
real正交使完整积分零，仍得g=0。因此

    closure_H_W,R span_R{τ_a r_p}=H_W,R。             (6)

不可把仅real span在complex H中直接称complex dense；其complexification才给(4)。

## 4. Readout定理：准确domain、mod-base与normBound

设Y是Hilbert，B⊂Y是**closed linear base subspace**，Q_Y=Y/B为Hilbert quotient。
也可直接以一个已给的mod-base energy completion作为Q_Y。
设D⊂H_W是linear source domain，包含全部principal translates(1)，
且T:D→Q_Y为linear，并有一个finite **global** K：

    ||T r||_(Q_Y)≤K||r||_W，ALL r∈D；
    T(Cf)=0，ALL f∈P_an（及所需complexification）。 (7)

则

    T=0 on D；其连续extension H_W→Q_Y也是零。       (8)

因为D含(4)的dense span，(7)与target completeness使T唯一连续延拓；
kernel含dense principal span，故extension零。
若有一个bounded lift Ttilde:D→Y，(8)只说image⊂B，
**不说lift字面为零**。若base并非closed、能量completion尚未定义或norm仍为
未证明的半正型，不能先叫它Hilbert quotient来套(8)。

此定理对nonlocal kernel、arbitrary finite/infinite place组合或其他source-defined
linear读出都一样：不要求局部性、translation-equivariance或单place。
只要求它们合成后的**同一global normBound**确实是(7)。
没有给arithPic几何对象自动赋予该norm，没有按Q值反造metric。

组别须分别消费：

- D complex、T complex-linear：即使先知T杀real P_an，complex线性也使它杀
  全complex principal span，(8)作用于全部complex源。
- D real、T real-linear：用(6)，(8)作用于全部real源与real Hilbert target。
- D complex、T仅real-linear且只杀real principal：只能推出T在real physical空间零，
  不能推出imaginary部分也零。合法反例T(r)=Im r；它bounded，杀real principal，却非零。
  若要求杀full realification P_an+iP_an，则(8)才作用于wholecomplex domain。

若readout仅定义在C(I)而非含非根physical源的D上，(8)不会凭空扩domain。
已有519指出ordinaryE没有f₀前像；source覆盖是不同于norm boundedness的前件。

## 5. 非零probe的必要費，仅定性，不能写成新growth定理

取552保存的非根compact smooth r₀=(D²−1/4)ψ，原537 Q_W(r₀)>0。
若D含r₀且T(r₀)≠0 mod-base，同时T正确杀全部principal，则(7)不可能。
由(4)/(6)，可选finite translate组合s_n∈C(P_an)使

    ||r₀−s_n||_W→0。

这些s_n的actual原源就是η₀的有限linear组合与scalings：
C^−1(τ_a r_p)=e^−a/2τ_a p=E[e^−a/2η₀(e^−a·)]。
所以不是只用抽象formal关系。每个s_n及r₀−s_n均在centered F。
线性/principal下降给T(r₀−s_n)=T(r₀)，于是

    ||T(r₀−s_n)|| / ||r₀−s_n||_W
       =||T(r₀)|| / ||r₀−s_n||_W→∞。                (9)

(9)付“必须global-unbounded”，但**不提供**逼近translate参数、coefficient质量、
support-growth或其余S_exp半范数的rate。不能把它写成随L的特定必要费用，
也不能将source-adapted/cofinal K_L当已否定。r₀−s_n不是fixed I_L的compact源。

## 6. 合法逃逸、强旧净值与停止范围

518/519：principal relation/jets空间在原F的指数Fréchet拓扑闭、非退化商非零；
该拓扑严格强于单线Hilbert完成。523已经给I的单线L²/finiteSobolev collapse与
Mellin-jets不连续；本稿principal p的版本是同机制的直接旧推论。
Hlog可直接独证，也可由principal H¹ cyclic density加H¹在Hlog稠密蕴含，
不应因log norm或mod-base的新名称计新net。
526另给忠实双端指数权商和非等价酉化缺陷，**不**声称该商零。

明确允许的不同域逃逸已经有实际旧readout：取实际ζ零点ρ，

    ell_ρ(r)=M_(C^−1r)(ρ)=∫e^((ρ−1/2)u)r(u)du。

它在centered F的指数Fréchet拓扑连续，按519杀I/P_an，且在wholeF非零。
它不满足任何本稿single-line global H_W bound；这正与(8)相容。
finite-window/cofinal eval费用、双端u指数权保continuous eval，也不在(7)内。
本稿不把这些source-adapted/nonuniform费用变成已付款的fullWeil比较。

本稿严格只排如下类：一个有限translation-invariant spectral Hilbert norm
（含physical L²、fullDlog/Hlog与任意fixed有限Sobolev增强），global bounded线性读出，
全部actual centered principal translates在kernel，且target是已定义Hausdorff Hilbert mod-base。
它确允许任意nonlocal/all-place内部构造，但不涵盖不同norm/domain、原指数Fréchet、
growth-dependent bounds、nonlinear/source-adapted repairs、变target或未证明的geometry energy completion。
这些逃逸既不能免费消费，也不能由(8)/(9)自动排除。

实际closure/bounded门成立；source与physical角色不混，complex组别/2π/domain均付。
主要fullWeil/growth/core/Ξ瓶颈未缩小；此门按强旧扣除属于范围恢复零轮。
不据它晋级Goal3或以“所有principal compatible几何失败”结束宏观Goal。
