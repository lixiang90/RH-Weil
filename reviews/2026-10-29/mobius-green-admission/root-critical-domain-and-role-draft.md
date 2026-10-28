# 根核草稿：临界响应域、次数与最强旧

2026-10-29；本稿在两独占审稿执行时作root独立核算，尚不是最终根消费收据。仅本已形成实物比较，无C056/593。

## 1. 原物理源及合法换序

令r=e^(u/2)f，f∈S_exp,C。对t在任意compact、各j，原响应及导数的尾受C_(N,j,t)n^(−N−1/2)控制，取N>1/2，故定义连续的S_exp,C→C∞_loc映射。

    V_r(t)=Σ μ(n)n^(−1/2)r(logn−t)
          =e^(−t/2)Σ μ(n)f(logn−t)
          =2e^(−t/2)θ_f(e^(−t)).

518(11)与(18)–(19)已经支付实际Möbius源和双重除数重建。取f=Eη时，用Σ_(n|m)μ(n)=δ_(m,1)合法重排（每fixed e^(−t)>0有绝对双和界），严格给

    V_r(t)=2e^(−t/2)η(e^(−t)),
    ||V_r||²_(L²(dt))=4∫₀∞|η(x)|²dx=2||η||²_(L²(R)).

最后一式用η偶性，仅换元x=e^(−t)，因子2不能删。V的u-导数与t-导数符号相反；物理平移τ_a r(u)=r(u−a)对应V_(τ_a r)(t)=V_r(t+a)。Bare f的τ_a对应物理e^(a/2)τ_a r，故需另带e^(a/2)；两种平移不混。

所有真实405关系、其平移和519闭像I均进入L²；这里甚至消掉全I而非仅P_an。此结论没有用RH。它不是把Pan的像按定义当成几何boundary，而是准确的解析响应公式。

## 2. 非零compact源的普通临界能量不能有限

设0≠r∈C_c∞,C，supp r⊂[−L,L]，L>0。每fixed t只有限n项，t<−L时V_r=0，全部导数为O_(r,L,j)(e^(t/2))（t≥−L）。记

    M_r(z)=∫ r(u)e^(zu)du。

Re z=σ>1/2时，换序的绝对费为

    ∫ Σ n^(−1/2)|r(logn−t)|e^(−σt)dt
      = (∫|r(u)|e^(σu)du) Σ n^(−σ−1/2)<∞。

所以F(z)=∫ V_r(t)e^(−zt)dt=M_r(z)/ζ(1/2+z)在该半面成立。

反设V_r∈L²。Cauchy–Schwarz在[−L,∞)给每σ>0

    |F(σ+iτ)|≤||V_r||₂ e^(σL)/(2σ)^(1/2)。

各compact子半面的积分导数也由同样指数余量控制，F在Re z>0全纯。商的同一性延拓为此半面内的亚纯同一性；ζ在s=1的极只对应商的零，不改变其余零点的论证。

M_r不恒为零（Fourier唯一性），且|M_r(z)|≤||r||₁ e^(L|Re z|)。在某个M_r(z₀)≠0处用Jensen，以半径2R盘控制半径R盘的零数，得圆盘零数O_r(R)，按重数计。ζ的Riemann–von Mangoldt计数为常数×TlogT+O(T)，对称ρ↦1−conjρ在正高度内保重数，所以至少一半零点满足Reρ≥1/2。位移z=ρ−1/2仍在半径O(T)盘中。因此存在未被M_r以全重数消去的零点z₀，Re z₀≥0；事实上未消重数随T增长，但只用一个。

若Re z₀>0，商的真pole违反F全纯。若z₀=iγ，商在z₀邻域有整数阶k≥1真pole，因此沿σ+iγ其模≥cσ^(−k)，与上式O(σ^(−1/2))矛盾。二者合并排除V_r∈L²。

此结论不要求RH、简单性、零间距、1/ζ临界线上有界或某个零点的数值位置；在RH成立时边界极本身也足以拒绝普通能量。它不拒绝截断、有费增长、其它范数或signed比较；禁止据此继续调damping/权等参数来延长本门。

## 3. 关系、商、次数及正性角色

裸ambient商C∞(R)/(C∞(R)∩L²(R))只有代数非零类可用：compact r的响应由§2给非零类，Pan由§1确实消去。但是smooth compact cutoff把任意smooth V在C∞_loc中逼近，分母在这个ambient拓扑稠密，Hausdorff化为0。不能据此自动断言限制到V(S_exp)的分母也稠密；cutoff V未被证明仍来自S_exp。不同拓扑也未被排除。

519已经给更强且Hausdorff的实际Fréchet商S_exp/I及完整jets，520已给全部Jordan模式。本Green记号并不支付几何principal、整过滤/sections或mixed RR，也未给一项原du/Dlog连续的全源正Hilbert能量（§2正阻止这项裸能量）。Noncompact关系消掉和compact类非零可以同时成立，不能将这两项本来已付的合法性合成更强的primitive几何定理。

全I消去还丢掉degree：405 Gaussian h∈I，c(h)=d(h)=1/4且B(h,h)=1/16，但其physical响应在L²，所以裸商把它消掉。要代表完整对象必须独立保两个degree，例如旧405(14)的R²×(S_exp/I)已经解决这个解析分裂，补上它不算新输入。B(h,h)是405原bare归一化，不能冒作另一个physical Q的未经换算数值。

Γ/contact/proper powers/双pole仍在原完整Weil型；本响应的Laplace poles是ζ除法的解析信息，不是完整型的正平方身份。537非根源虽映到非零代数类，仍没有可比较的有限正范数、算术局部单位或有效section。

## 4. 当前可消费方向（待两原稿与不同fresh核后最终结算）

518换坐标＋519原源逆与degree＋标准Jensen/RvM/Laplace给本门；525(1)甚至已写同一W_f(x)=θ_f(1/x)，本V=2e^(−t/2)W_f(e^t)完全同一actual响应。525§4已识别全smooth族临界ε增长的RH强度，§5已给实际剩余pole阶max(mρ−ordρ M_f,0)和fixed探针盲点；本ordinary L²端点比较不支付该未知增长。522商次指数等价与526忠实多权商／近频率缺陷／critical退化都是更强旧资产，不能把本ambient类冒作新carrier或metric修复。

080已有真正finite incidence Green且finite acyclic不消其inverse，081已有不同的critical Hodge Gram/target distance，082表明conditioning不代target。不能把本L²定义域空误作Nyman–Beurling逼近不可能，也不能借finite acyclic宣布所有Green无效。本次不是重开525增长／截断／参数的预算，只恢复同公式强旧并完成一个普通端点域比较。

扣最强旧后预期为标准old0，而非新的arithprincipal/关键瓶颈移除或whole改进。原whole542+555→557 leading4/5仍是负惯性UPPER，primitive/principal/sections/mixed/signed corecross/成长Ξ未付。最终需审稿明确是否发现不同净后果，才由根消费；数学计数暂不动。
