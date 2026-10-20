# 直接正Π跳跃形式与连续正反例：闭性、热迹和源身份分开

2026-10-20，C029 root原稿。一般输入P、Π、M及Z沿用562/563；
不以未知零点构造内积。本文的Hilbert空间写明，避免把Weil测试空间和heat载体混同。

## 1. 安全半平面上的正计数给一个真实正闭形式

在log变量u>0，选已付收敛的实σ使

    dνσ(u)=e^{-σu}dΠ(u),     mσ=νσ((0,∞))<∞.

可以改用uΠ等实际对数导数正测度，只要该σ下总质量有限；以下命题一样。
在H=L²(R,dx)，T_u f(x)=f(x+u)，定义

    eσ[f]=(1/2)∫ ||T_u f-f||² dνσ(u).                 (1)

0≤eσ[f]≤2mσ||f||²，因此domain=H，bounded positive form且闭（form norm与原norm等价）。
其关联bounded自伴算子为

    Kσ=∫[I-(T_u+T_{-u})/2]dνσ(u),  0≤Kσ≤2mσ I.      (2)

积分在弱／strong Bochner意义存在；T_u强连续且ν有限，逐f可积分。
在Fourier约定Ff(ξ)=∫e^{-ixξ}f(x)dx下，multiplier为

    kσ(ξ)=∫(1-cos(uξ))dνσ(u)≥0.                     (3)

式(1)还满足实normal contraction的Dirichlet截断不等式，故是一个真实保正跳跃构造。
标准closed-form/Dirichlet接口可核[Baudoin本人Lecture5](https://fabricebaudoin.blog/2019/02/11/lecture-5-dirichlet-forms/)；
(1)–(3)与以下trace结论由本稿直接证明。

**它没有所需的ordinary heat trace。** 任何t>0，

    exp(-tKσ) ≥ exp(-2tmσ) I.

H无限维，取任意正交单位序列，正算子迹的有限部分和任意大，故Tr exp(-tKσ)=∞。
同样的bounded jump构造即使放到有限长度circle／interval，只要载体仍无限维，仍失败。
加有限非负killing常数也不改变结论。

更一般的无限质量translation-invariant正jump（如Γ）可以是unbounded closed form；
但在整条R上非零heat Fourier multiplier不是compact：在其绝对值≥ε的一块正Lebesgue测度集上
选无限正交列，像的范数≥ε。因此仍无非零ordinary trace-class heat。
这只排**原全线translation-invariant载体的ordinary trace**；保有限体积但unbounded、
confining非平移势、其他载体、半有限trace/单位体积、relative/regularized trace等合法逃逸。
换trace必须重新支付目标身份，不能把∞称为原Θ_W。

正Π的两连续段都通过(1)，都在ordinary trace处失败；它没有区分pure与nonpure的能力。
这是safe Euler正性与完整Weil热量的具体分离，非对一般正闭形式的否定。

## 2. 连续族：直接由源ODE构造有限闭形式，不先求根

完整源平衡已在563给全D′身份

    Wc″+d Wc=0, Wc(0)=2,Wc′(0)=0, d=c-1/4.

这来自全部positive Π和两个pole，Gamma=0。以下是旧身份的构造消费，不重计反例。
在Hc=C²标准内积上，从参数直接给

    kc[v]=d ||v||²,   Dom kc=C²,  Kc=d I2.             (4)

d≥0时它是正闭形式且ordinary trace=2e^{-td}。
源ODE唯一解的Gaussian配对给完全同一个Θc(t)=2e^{-td}，all t>0，error0。
可由展开偶次ODE级数并用Gaussian矩积分证明，或直接热方程积分分部；
Gaussian尾吸收该有限指数阶源，全部步骤不读取ζ根。
d=0仍用C²，trace=2，保持二重根所需普通重数，而非把半正G商的一维当两维。
d<0时同一源给Θc=2e^{|d|t}递增，任何K≥0且all-time ordinary trace-class都不可能匹配。
正闭K的trace非增，此负控制无需先定位根。

这不是由一般positive P/duality自动构造K≥0；决定性额外信息是独立核验d≥0。
在本有限参数类中它与pure阈值等强，但直接算d及完整ODE不是循环假设未知零点。

## 3. 自动正平方会换掉热量

以源递推的companion C=[[0,1],[-d,0]]为例，在标准C²上强行取

    k_square[v]=||Cv||²,  K_square=C* C=diag(d²,1).      (5)

它对正负d始终positive closed，却有trace=e^{-td²}+e^{-t}，通常不等于2e^{-td}。
在t=0一阶导数相等要求1+d²=2d，即(d-1)²=0；本族d∈(-1/4,1/4]全不满足。
因此连连续正段也不能用任意标准范数的C*C冒充目标heat。
在d>0时，563已给G=diag(d,1)>0，C^{*_G}=-C，才有C^{*_G}C=dI2，
其trace与(4)一致。内积的源侧正性不能被自动squaring免费补出。

## 4. 尝试经典全prime跳跃时，哪里真正出现责任

经典完整Q的算术项为-2Σ a_n Re h_f(logn)，a_n=Λ(n)/sqrt(n)，
h_f(u)=〈T_uf,f〉，原compact smooth f的支撑有限。
对有限X令A_X=Σ_{2≤n≤X}a_n及

    J_X[f]=Σ_{2≤n≤X}a_n||T_logn f-f||²≥0.

准确恒等式是

    Q_prime,X[f]=J_X[f]-2A_X||f||².                   (6)

不是把prime负项改成J_X就完成正性。A_X→∞：若∑Λ(n)/sqrt(n)<∞，
则由正系数支配-ζ′/ζ(σ)在σ↓1有界，与ζ在1的已知简单pole矛盾；无需PNT。
对任意非零f∈L²(R)，h_f(u)→0（|Ff|²∈L¹的Riemann–Lebesgue），
故||T_uf-f||²→2||f||²>0。于是未减项的J_∞[f]=∞，domain恰{0}，不稠密。

相反，对于compact f，n>exp(diameter supp f)的相关为0，
(6)中J_X和2A_X的无限大部分精确相消，Q_prime,X最终稳定。
它付的是renormalized signed source；不能沿用原J_X≥0推出减项后的正性。
在fixedL用regional edges/degree profile的精确平方分解早在016/543已付，
同样留有负degree与pole/Γ coupling，不能把该旧分解重计新正性。

Γ部分的已知w(u)=2e^{-u/2}/(1-e^{-2u})有近0的1/u奇性，
却具有合法Dlog正jump能量（541/543），说明“无限质量”本身不必导致零域：
这里导致零域的是**远处**质量无限且translations趋不相关。
Γ的finite-part contact常数、全部primepowers和完整双pole必须再合成原Q。
在fixed窗上可闭的Q算子之heat，不是自动等于W(k_t)的谱heat；两个heat参数/载体不可混用。
旧529已排指定成长窗标准锥保正shortcut，563/565已标同源identity责任，本稿不扩大这些旧边界。

## 5. 净范围

新固定测试是两个具体“automatic positive form”路线分别丢失ordinary trace或目标heat，
以及在函数域unitary bundle真lift之前对载体/内积/renormalization的准确分层。
continuous纯性、Γ jump、finite-window degree分解、CM等价和正极化标准蕴含均归旧。
没有classic独立全heat identity；actual whole4/5、560成长K/core/coupling不变。
