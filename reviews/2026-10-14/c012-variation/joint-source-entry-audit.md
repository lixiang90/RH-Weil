# C012转向：同源 signed 输入审查与完整局部化运输门

2026-10-14。此文件为独立来源审查，不改STATE/cadence/Git，不另结算研究轮。
恢复AGENTS、README/STATE、check/show、当前Goal/MACRO_FRONTIER/C012和D20261014M；
现场HEAD为6309e116e20e886b55a09e0674638b39e4edf349，初始工作树干净。
≤538/0c4f为冻结基线；539/540是本Goal已付费用，不能反复用便宜反例替代成长独立来源。

## 1. 来源筛查的真实结果

本次没有取得一份已经付清、能直接消费为成长域全complex Weil正性的新增signed算术定理。
以下是原件筛查，而非对全部文献或所有方法的穷尽证明。

* [Burnol math/0101068v1](https://arxiv.org/pdf/math/0101068)：核读印页2–3的支持条件正性定理与证明。
  其结论为存在c>1，在固定乘法支持[1/c,c]上正性成立；证明还明确需新想法才能到c=√2。
  它是真正无条件来源，但范围弱于已核537，不能再次登记成长输入。conductor算子解释局部显式公式，不自动给完整正性。
* [CCM2310.18423v2](https://arxiv.org/html/2310.18423v2)：核对引言及§4.4–4.7的局部/半局部对象。
  正trace与Sonin稳定性已有C005/C006及531–535消费。本文未发现一个新whole-source signed比较费；
  同构/稳定性不能直接升级为实际Weil与正trace无费相等。这里只核指定范围，未重新通读全篇。
* [Suzuki2606.09096v3](https://arxiv.org/html/2606.09096v3)：核读§1.2、§8.1及§7.9相关段落。
  原文的连续screw核正性仍有RH强度；small-a simple-even不是成长结论。
  Theorem1.5保留A_a−λI、λ<λ_a的移位norm产生实零函数；Corollary1.6的Ξ比值局部一致极限是额外条件。
  §7.9明确核空间收敛仅heuristic。这些结果没有支付λ=0的全成长正性或同对象极限，不能复活等价Hilbert路线。

这些来源均不是C008缺附件的替代完整证书。本审查不等待缺附件，也没有启动producer。

## 2. 可核多prime来源：Selberg signed关系存在，但桥尚缺

一级原件为[Selberg1949《An Elementary Proof of the Prime-Number Theorem》](https://www.math.lsu.edu/~mahlburg/teaching/handouts/2014-7230/Selberg-ElemPNT1949.pdf)。
核读印页307–310的(2.3)–(2.14)，尤其(2.8)/(2.12)。它独立于未知ζ零点位置，
同时约束单prime与双prime卷积，原文的θ是只计prime的函数。
要消费全部primepowers，须另付高幂项，不能把θ无声改为ψ。

全primepower算术系数的准确恒等式是

    Λ₂(n)=Λ(n)log n+(Λ*Λ)(n)=(μ*log²)(n).

这是逐系数关系，并非Weil半正定。有限求和中，一侧含primepower指数≥2的卷积质量
可由Chebyshev界与Σ_(p,k≥2)logp/p^k<∞付O(X)；Λ(n)log n的高幂质量
为O(√X log²X)=O(X)。因而原(2.8)运输到

    Σ_(n≤X)Λ₂(n)=2XlogX+O(X).

这个运输只给fixed确定常数存在，不在本审查声称新的最优显式常数。
定义R₂(X)=Σ_(n≤X)Λ₂(n)−2XlogX。对于compact C¹测试q，准确signed接口为

    Σ Λ₂(n)q(n)−∫2(logx+1)q(x)dx = −∫R₂(x)q′(x)dx.

若取真正Weil响应q(x)=x^(-1/2)k_f(logx)，右侧的绝对付款包含

    ∫e^(a/2)|k_f′(a)−k_f(a)/2|da.

所以Selberg关系确是不同于whole-Q的独立算术输入，却**没有**凭O(X)自动支付原Dlog
全complex源的费用。C012正核的native导数探针也不能靠把E改叫R₂逃逸。
若保signed，需给新的响应桥而不是重复此分部积分。

历史扣除：旧036§4已经区分Dirichlet乘积卷积与max-kernel平方，054–058已经提出
twisted Selberg hierarchy，474及相关hybrid审查已消费Λ*Λ的精确μ完成。
本次原件恢复及高幂运输不作为新数学轮。旧比例路线保持暂停。

最便宜的对象负对照应先于任何新合同：Λ*Λ在n=6处为2log2log3>0，
而原单prime Weil测度在n=6无atom；此外乘积位置log(ab)对应同向卷积，
L²平方要求反射后的差位置log(a/b)。不能将Λ₂的positive系数或D(s)²
移称原Weil autocorrelation的positive Gram。能改变准入的证据是明确、零点无关的
算术polarization/transport恒等式，把上述同向关系接到actual reflected响应，且费用
在全complex原Dlog域可付；本次尚无此原证明。

## 3. 完整局部化是精确备选，但固定scalar搬运已需付费用

此节只给备选的明确消费门，不建议将又一个免费搬运反例作为下一主攻。
它不同于537已核的Liu指定tail-dropping Dχ，但属于同一费用警示，不能扩大为所有localization失败。

采用actual Q、I_L、zero-extension、原L²及complex Cc∞，并保全部primepowers/dual pole。
令L₀=17/16，χ∈Cc∞((-L₀,L₀);R)、||χ||₂=1，χ_x(u)=χ(u−x)。
Kχ(a)=∫χ(v+a)χ(v)dv。于是Kχ(0)=1、1−Kχ(a)=O(a²)、Kχ(a)=0于|a|≥2L₀。
令k_f(a)=Re∫f(u+a)conj f(u)du、N=||f||²，w(a)=2e^(-a/2)/(1−e^(-2a))。
Fubini给连续partition恒等式

    ∫||χ_x f||²dx=N,
    ∫k_(χ_x f)(a)dx=Kχ(a)k_f(a).

actualΓ=Γ(0)N+∫w(a)(N−k_f(a))da，所以完整remainder为

    Rχ(f):=Q(f)−∫Q(χ_x f)dx
          =∫[4cosh(a/2)−w(a)](1−Kχ(a))k_f(a)da
           −Σ_(n<e^(2L)) (2Λ(n)/√n)(1−Kχ(logn))k_f(logn).

没有删除Γ高尾；两边完整log能量相减后，近0的1/a奇性被1−Kχ=O(a²)消掉。
固定L上连续项形成真实continuous compact自伴核。全pole差也在同一连续核中，
odd负pole没有被扔掉，norm identity没有scalar误差。
每个χ_x f平移后属于已核L₀窗，Q在整体平移下不变，因此537准确给

    ∫Q(χ_x f)dx≥τN，τ=2^-49162.

但这只说明局部块正，并不说明Rχ≥−τN。后者是新的充分输入，且比whole-Q正性强，
不能改名为所求独立弱来源。

## 4. 最便宜实际反例：第一新增primepower9

取a=log9>2L₀。对任意L>a/2，两个相同real非负smooth窄bump置于±a/2，
窄度使self相关避开所有logn≥log2、cross相关仅碰log9，并严格处于I_L。
有限actual atom集的最小gap为正，因此这样的固定g确存在。
归一化N=1后h_g(a)=1/2；所有其他actual primepower相关恰为0。
令f_m(u)=exp(iω_m u)g(u)、ω_m=2πm/a。合法复源weakly趋0，固定compact连续项趋0。
因为Kχ(a)=0且Λ(9)=log3，得到精确极限

    Rχ(f_m) → −(2log3/3)(1/2)=−log3/3 < −1/3.

ln3>1由e<3即可严格核验，无浮点/ζ零点。τ<1/3，故局部τ加任何fixed-L compact
修复都不能以Rχ≥−τI免费搬运到这个较大窗。Rχ+εI的负指数无限，只要ε<log3/3；
任意有限个合法源线性条件可先取充分分离carrier的负Gram，再取其有限核保留负方向。

这反的是remainder运输，不是Q；f_m的wholeΓ仍logω_m+O_g(1)，全部prime/pole
为bounded/compact，故whole Q最终为正。本节与539/535共享carrier机制，登记为路线准入
成本，而非新独立算术正性或新宏观方法边界完成。

## 5. 明确未排逃逸、停止与信息缺口

第4节χ及compact修复是在取carrier极限前冻结。χ可依L任意变化，只要每个L固定即可；
但χ依源/频率选择时连续Γ差不必统一compact，也不必沿carrier趋0。
因此source-adaptive partition、保留完整localized能量而不只抽τ、不同尺度的联合signed
支付与非compact补偿均未排。不能用本反例声称这些方法失败。

当前可付的是“现有固定窗正性不能通过固定scalar/compact remainder规则自动成长”。
当前仍缺的是一份真实算术signed响应估计，既弱于whole-Q责任，又能在原源上产生非循环净后果。
外部筛查没有填此缺口。下一准入若选择Selberg来源，首门必须是反射/同向卷积的真实
transport，而非再做矩阵或把Dlog换成含一阶导数的更强norm；若选择localization，首门必须
说明source-adaptation的独立规则和其全Γ费用，而非把Rχ PSD作为新公理。

本文件无科学pending进程，保存来源范围/准入目标后交由root宏观复盘决定唯一下一动作。
