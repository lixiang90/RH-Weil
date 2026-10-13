# C003：完整原算子的半群／预解逆向审查

2026-10-13。内部独立审查；单独从完整原分布的交叉项出发，
不采用有限矩阵最低向量、数值零点、辅助 H 的结论或未证低谱投影。
先恢复 AGENTS、README、STATE，运行 research_state.py check/show；
当前 C003、D20261013C，HEAD 为 03f7631，cadence 为 3。
没有启动计算进程，本文件不修改 STATE 或消费 cadence。

## 1. 对象、原件和归一化

取 I=[−ell,ell]，L=2ell，lambda=e^ell，mu=lambda²=e^L。
H=L²(I,dy)，所有函数在 I 外延零，Fourier 变换为
hat f(t)=∫ exp(−ity)f(y)dy。内积反线性于第一变量。
q 是实际完整 Weil 型，A 是它的原生下有界自伴关联算子。

原件只核读 [arXiv:2511.22755v1](https://arxiv.org/html/2511.22755v1)
的 (3.7)–(3.20)、Proposition 3.3–3.4、关联算子与 Theorem 3.6。
本地必要前件为 004 §1–2 与 016 的 partial translation 恒等式。
不把论文的未知最低态、RH、simple-even 或其数值结果当作前件。

原型的拱位 multiplier 是 m(t)=2theta′(t)，非 theta′(t)：

    q(f,g)=∫ m(t) conjugate(hat f(t))hat g(t)dt/(2pi)
      +∬_{I²} 2cosh((y−z)/2) conjugate(f(y))g(z)dy dz
      −sum_{2≤k<mu} w_k [C_{a_k}(f,g)+C_{−a_k}(f,g)],
    w_k=Lambda(k)/sqrt(k), a_k=log k,
    C_a(f,g)=∫ conjugate(f(y))g(y+a)dy.

边界 k=mu 的重叠为零，严格／非严格上限产生同一型。
rho(a)=exp(a/2)/(exp(a)−exp(−a))，a>0。
原件 (3.8),(3.19) 明确给 2theta′；Theorem 3.6 的证明文字却写
theta′，旧 016 §3 也写 theta′ 并给一半的谱底。
这是局部系数歧义；本审查由原分布 (3.15) 及 (3.19) 确认原型，
不使用旧 m_infinity 数字，也不自动修改其他历史笔记。

## 2. 域：光滑 bump 不只是 form-domain 元素

原型的闭域为延零后的 logarithmic Fourier form-domain，
即 ∫log(2+|t|)|hat f(t)|²dt<∞；有界极点与有限平移不改变域。
特别地，f∈C_c^∞(int I) 的 Fourier 变换快速衰减，
m(t)hat f(t)∈L²(R)。

令 M 为全线实 multiplier m(D)，P_I 为区间压缩，B 为有限平移及
极点组成的有界自伴算子。对全部 g∈D(q)，Fourier 配对给

    q(f,g)=<P_I M f+Bf,g>.

表示定理因此给 f∈D(A)，Af=P_I M f+Bf。
这里没有声称 D(A) 等于全线 multiplier 的压缩域；
只证明本次所有光滑 bump 落在原生算子域，这已足够。

## 3. 直接交叉核与精确阈值

取实 u≥0、非零，u∈C_c^∞(J)，J⊂(0,ell)。
设 u_+(y)=u(y)，u_−(y)=u(−y)。两者支撑不交。
由原分布的半轴公式，交叉卷积在零处消失，故重整常数项为零；
拱位交叉恰为负的 rho 核，极点交叉恰为 2cosh 核：

    q(u_+,u_−)=∬_{J²}u(r)u(s)F(r+s)dr ds
      −sum_k w_k ∫u(r)u(a_k−r)dr,
    F(a)=2cosh(a/2)−rho(a).

后一项的支撑要求 a_k∈J+J；无额外因子 2。
也可由 C_{a_k}+C_{−a_k} 核对：两支撑有固定顺序，只有其中一项非零。
若 J+J 避开所有 log 素数幂，这个完整算术交叉项严格为零。

令 x=e^a>1，则

    F(a)=(x³−x−1)/(sqrt(x)(x²−1)).

多项式 x³−x−1 在 x≥1 上严格递增，1 处为 −1、2 处为 5。
故存在唯一 alpha∈(1,2)，alpha³−alpha−1=0，且

    F(a)>0  iff  a>log alpha.

对每个 mu>alpha，开区间 (log alpha,log mu) 非空，
其中有限个实际素数幂对数不能覆盖开区间。
先选不在原子集的 a_0，再取足够小的 J 围绕 a_0/2，
使 J⊂(0,ell)、J+J⊂(log alpha,L)，且 J+J 无实际原子。
这样的 J 在每一个 mu>alpha 上存在，而非只在素数端点存在。
于是 q(u_+,u_−)>0。

设 f=u_+−u_− 为奇函数，|f|=u_++u_− 为它的偶伙伴，则

    q(|f|)−q(f)=4q(u_+,u_−)>0.

两者相同 L² 质量，所以任何 scalar shift 都不能改变这个反例。
这不是辅助 H 的反例，也不声称 q(f)<0。

补审主稿 529 的固定窗口：J=(log(9/4)/2,log(11/4)/2)，
mu>11/4 时合法；J+J⊂(log(9/4),log(11/4)) 无整数，
所以也无素数幂原子。对 z=e^(r+s)∈(9/4,11/4)，

    z³−z−1≥(9/4)³−9/4−1=521/64,
    sqrt(z)(z²−1)≤sqrt(11/4)((11/4)²−1)=105sqrt(11)/32.

两端分别利用正单调分子和分母，不假设其商单调。
故 F(r+s)≥eta=521/(210sqrt(11))>0，
q(|f|)−q(f)≥4eta(∫u)²。定量常数、正方向和质量因子均通过。

## 4. 半群与预解：不依赖模量准则的逆向证明

因 u_−∈D(A)，下有界谱的函数演算给强导数

    (exp(−tA)u_−−u_−)/t → −Au_−  (t↓0).

结合 <u_+,u_−>=0 与 <u_+,Au_−>=q(u_+,u_−)>0，得到

    <u_+,exp(−tA)u_−>=−t q(u_+,u_−)+o(t)<0

对全部充分小的正 t 成立。非负函数的半群像不可能与另一非负
函数有负内积；因此原热半群不保持标准逐点正锥。
同一构造排除 positivity-improving，但不证明每个大 t 都失败。

还有独立的预解检测。令 c→+∞ 并取 c>−inf spec(A)，
由 c(A+c)^{-1}→I 强收敛及 resolvent 恒等式，

    c²<u_+,(A+c)^{-1}u_−> → −q(u_+,u_−)<0.

证明只用 u_−∈D(A)，不要求它在 D(A²)。
故全部充分大的 c 也有负的预解交叉。

任意实 scalar shift b 满足
exp(−t(A+bI))=exp(−tb)exp(−tA)，不能修复保正。
更一般地，任意有界实 measurable multiplication potential V
保留 D(A+V)=D(A)、自伴性和下有界性，并且
<u_+,Vu_−>=0。因此 §4 的正交叉和短时负半群结论对 A+V
同样成立；q_V(|f|)−q_V(f)=4q(u_+,u_−)>0 亦不变。
有界局部对角势不能修复此失败。
设 T 是有界可逆的正序同构，即 T 与 T^{-1} 均保持正锥，
可作用于同一或另一个 L² lattice。则

    T exp(−t(A+V+bI)) T^{-1}

保正当且仅当 exp(−t(A+V+bI)) 保正。因为两边可以用 T 和 T^{-1}
正性来回转移，此结论不要求 T 酉或变换后的算子自伴。
因此排除全部这些序同构 conjugations。只要求 T 正而未要求
T^{-1} 正，或任意 Hilbert 相似变换，不属于本定理量词。

## 5. 反向区间：保正阈值的 sufficiency

以下从全线正跳能量重组原完整型，并非从某个试探函数推广。
令 E_a^R(f)=∫_R|f(y+a)−f(y)|²dy。由 digamma 积分或
原分布的重整恒等式，对光滑函数有

    q_infinity(f)=m(0)||f||²+∫_0^∞rho(a)E_a^R(f)da,
    m(0)=−gamma−pi/2−3log 2−log pi.

Fourier 一致性检验为

    m(t)−m(0)=2∫_0^∞rho(a)(1−cos(ta))da.

Tonelli 的非负能量和 Fourier 公式使该恒等式扩展到全部闭域。
它同时确认 m=2theta′ 与交叉项 −rho 的归一化。

若 1<mu≤alpha<2，则没有任何实际素数项。把极点项完成平方后，
在 I 上精确得到

    q(f)=1/2∬_{I²}[rho(|y−z|)−2cosh((y−z)/2)]
                       |f(y)−f(z)|²dy dz
         +∫_I V(y)|f(y)|²dy,
    V(y)=m(0)+∫_{R\I}rho(|y−z|)dz
                   +∫_I2cosh((y−z)/2)dz.

边界处的 exterior 积分可发散；它是非负 measurable potential，
只在 a.e. 内点有限。原闭域与该能量表达相同，不删掉边界费用。
因 |y−z|≤L≤log alpha，跳核 rho−2cosh 非负。
V(y)≥m(0) 且 modulus 保持 potential 和 L² 质量。
| |f(y)|−|f(z)| |≤|f(y)−f(z)| 因此在全部闭域给

    |f|∈D(q), q(|f|)≤q(f).

可不援引外部 Beurling–Deny 定理而直接证明保正。
取 c>−m(0)，g≥0，最小化
q(f)+c||f||²−2Re<g,f>。型实、严格凸，唯一最小器为
(A+c)^{-1}g；换成 |f| 降低 jump 能量并增加 <g,f>，
故最小器非负。于是这些 resolvents 保正。
再由强极限 (I+tA/n)^{-n}→exp(−tA)，对 n 足够大每个
因子都是正预解的正标量倍，推出全部 t≥0 的热半群保正。
此处不声称 positivity-improving 或 Weil 型非负。

结合 §4，得到完整原算子在标准正锥上的精确分类：

    exp(−tA_lambda) 全部 t≥0 保正  iff  1<lambda²≤alpha.

等号处仅在最大距离可能 F=0，不影响非负跳能量和闭域结论。

2026-10-13 补审：充分方向也对每个有界实局部乘法势 V 成立。
q_V=q+∫V|f|² 与 q 同域且下有界，且逐点质量相同严格给
q_V(|f|)−q_V(f)=q(|f|)−q(f)≤0。
在上一最小化证明中取 c>−m(0)+||V_-||_infinity 即为 coercive，
唯一最小器的非负性、正预解和 Euler 强极限逐项不变。
这与 §4 的必要方向合起来证明 529 的增强量词：

    对每个 bounded real local multiplication V，
    exp(−t(A_lambda+V)) 全部 t≥0 保正
      iff  1<lambda²≤alpha.

因此之前只写原生 A 的 iff 是保守的范围陈述，
无需额外来源前件即可扩大到全部上述有界实局部势。

## 6. 非重复性、宏观影响与逃逸

核查 004 §2 的原命题仅指出极点不定及不能直接套 Perron–Frobenius；
它没有证明完整型的模量反例或半群不保正。
002 的对应段是建议先变换核，016 是图能量恒等式和逐块范数损失。
另检索 notes/reviews 中 positivity-preserving、positivity-improving、
保正、Beurling–Deny、order-isomorphism 与阈值多项式：
当前 C003 同轮草稿外未定位到上述完整分类与序同构量词。
这是可定位的内部非重复审查，不是世界优先权或全部历史逐字复审。

新结论对每个增长支撑有效，使用实际完整 Weil 型、全部原子和原权；
不是孤立有限线代反例，确实关闭标准函数正锥上直接热半群／模量
降低／序同构修复的 lowest-state Perron–Frobenius 方法类。
其算术稳健性来自原子离散性：极点与拱位的正交叉在原子空窗中
无法由真实 prime shifts 修复。没有用 RH 或任何零点位置。

但完整 Weil 正性、真正最低态偶性、prolate 与实际最低态的比较、
全补空间费用与增长支撑上的统一后果均未支付。
逃逸包括直接有符号比较、非标准锥且非序同构的实现、特定子空间
上的机制、真正几何／算术新极化；并不排除这些路线。
奇子空间的标准非负锥只有零向量，故不能把全 H 保正失败解释成
某个“奇子空间保正”定理，也不证明最低态必须奇或多重。

宏观瓶颈仍是完整算术正性。改变的是一类此前仅未付的 standard-cone
shortcut 被严格否定，并具有 sharp 可行性分界。
这是旧 Goal 第十节“有效机制严格边界”的实质候选证据；
是否足以完成长期 Goal 还须主代理逐项审计原强度、范围、保存和净意义，
本审查不宣告 Goal complete。

精确 iff 阈值对原生 A 及任意有界实局部乘法势 A+V 均成立；
不声称覆盖所有无界局部势及其可能不同的闭域／自伴实现。

停止条件：不再寻找 scalar shift、有界局部对角势、正权序同构
或增大 N 来恢复此保正路线。
重新准入：提供不受本序同构量词覆盖的独立实际机制并保留同一完整对象。
唯一下一动作由主代理在同源账本与两条独立审查会合后确定；
本辅助任务已审结，无待处理进程。
