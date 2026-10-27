# Joint oldform tower：原坐标拓扑、两种闭商与常数通道

2026-10-27；/root/tower_quotients 独占稿，执行 STATE 已指定的 [joint tower 准入](../finite-cover-trace/next-joint-oldform-tower-admission.md)。本稿只处理拓扑／强旧消费；[同源与序列反演](source-and-sequence-inverse.md)由另稿支付。本文不修改 STATE、cadence 或 Git，不预建 C048/585；出稿不代 root 消费。以下均为519/520/553、583及标准 entire-function/有限维操作的直接运输，建议0新数学轮。

## 1. 对象与三种不可混同的拓扑

令 \(\mathcal F=S_{\exp,\mathbb C}\)，physical \(r=e^{u/2}f\)，
\[
 L_r(z)=\int_{\mathbb R}r(u)e^{uz}du,\qquad
 \mathcal P=C(P_{{\rm an},\mathbb C})\subset\mathcal F,\quad
 C f=e^{u/2}f .
\]
\(\mathcal F\) 的原 Fréchet 拓扑控制所有指数权和导数。记
\[
 \mathscr H=\mathcal O(\mathbb C)
 \quad\text{with compact-open topology},\qquad
 E=\{a=(a_m)_{m\ge1}:\ p_Q(a)=\sup_m Q^m|a_m|<\infty
          \text{ for all }Q\ge1\}.                         \tag{1}
\]
Q取正整数已给同一 Fréchet 拓扑。E 比坐标 product 拓扑强；\(\mathcal F\to E\) 连续不意味着其逆在实际像上连续。

对任意 entire \(F\)，而不只对实际 Laplace 像，定义
\[
 \alpha(F)=\operatorname{CT}_q F(j(q)),\qquad
 A(F)_m=[q^{-m}]F(j(q)),\qquad
 \pi_0F=F-\alpha(F).
                                                               \tag{2}
\]
固定 \(0<s<1\) 的 q 圈使所有系数有实际意义；整个圆像 \(j(|q|=s)\) 是有限 compact。改变小圈不改变 Laurent 系数。\(\alpha\) 是 \(\mathscr H\) 的连续线性泛函，\(\alpha(1)=1\)；\(\mathscr H_0=\ker\alpha\) 是一个选定的 constants 商截面。下文 \(\pi_0\) 并非物理源的 relation quotient。

## 2. E 正是 entire Faber 函数的 constants 商

沿583使用 \(P_m(z)\)：
\[
 -\frac{qj'(q)}{j(q)-z}=1+\sum_{m\ge1}P_m(z)q^m,\qquad
 P_m(j(q))=q^{-m}+O(q),\quad \alpha(P_m)=0.                 \tag{3}
\]
583的 Cauchy/Faber 重构只使用F在有限 compact上全纯，故同一论证对任意 \(F\in\mathscr H\) 给
\[
 F(z)=\alpha(F)+\sum_{m\ge1}A(F)_m P_m(z).                  \tag{4}
\]
不需要F具有某个未经给出的源增长。

连续性可逐项直接支付。给定Q，取 \(s<\min(1,Q^{-1})\)；Cauchy有
\[
 p_Q(A(F))\le \sup_{|q|=s}|F(j(q))|.                       \tag{5}
\]
反向，对任意compact K，583生成函数的小R圆给
\(|P_m(z)|\le D_{K,R}R^{-m}\)；取Q使 \(QR>1\)，则
\[
 \sup_K\left|\sum_{m>N}a_mP_m\right|
 \le D_{K,R}p_Q(a)
       \frac{(QR)^{-N-1}}{1-(QR)^{-1}} .                  \tag{6}
\]
这构成从E到 \(\mathscr H_0\) 的连续逆。对 q 圈像这个compact应用一致收敛，允许逐项取Laurent系数；(3)核出逆的系数确为a，常数项为0。因此
\[
 \boxed{\mathscr H/\mathbb C\simeq \mathscr H_0\simeq E}
                                                               \tag{7}
\]
是明确拓扑同构，而不是将物理 \(\mathcal F\) 与全部E等同。

实际源的 \(a(r)=A(L_r)\) 连续、单射：若负系数全零，(4)给 \(L_r\) 常值，而虚轴Fourier衰减迫常值0；Fourier唯一性给r=0。其像在E中稠密。一个实际证明是
\[
 g_\varepsilon(u)=(4\pi\varepsilon)^{-1/2}
                  e^{-u^2/(4\varepsilon)},\qquad
 L_{P(-D)g_\varepsilon}(z)=P(z)e^{\varepsilon z^2}.
                                                               \tag{8}
\]
这里每个固定ε>0的源都在 \(\mathcal F\)。ε→0在\(\mathscr H\)中趋于任意给定多项式P，而多项式的Faber负系数恰为finite sequences；后者在E中稠密。这里没有说 \(g_\varepsilon\) 在原物理 Fréchet 拓扑趋于一个函数，也没有把Dirac分布当原源。

另稿若闭合 multiples-transform \(T:E\to E\) 的连续自同构，则真正联合数据为
\[
 \mathcal B_\infty(r)=T a(r).
                                                               \tag{9}
\]
它只在E中换坐标；(7)与以下商均可经T运输。不能因每个坐标各自合法而免除另稿的绝对逆、d因子和原费用。

## 3. Finite principal 完成化的闭商为何全零

E中的finite sequences记 \(E_{\rm fin}\)。对a∈E，
\[
 p_Q(a-a^{(N)})\le 2^{-N-1}p_{2Q}(a)\longrightarrow0.      \tag{10}
\]
而T和其Dirichlet逆若按另稿成立，都保持finite support，故 \(T(E_{\rm fin})=E_{\rm fin}\)。

这些finite系数对应583的真实Faber多项式输入；583先对每个整数基 \(J_m=P_m(j)\) 给真实 native principal divisor/Green pair，再复化。**如果沿用这一principal recipe，且新的目标／base商连续并杀掉这些finite principal records的全部复线性span**，并且base闭（等价地在所用Hausdorff商中零类闭），则(10)使全部E像为base，联合tower也全零。仅逐个杀孤立basis不足以约束一般非线性处理；非闭base／非Hausdorff商不能套这个闭商结论。此结论不要求Pan在E稠密。

这里的“principal”具有实际前提：不能把任意oldform residue值本身自动命名为几何principal divisor。所说的是583同一个finite Faber/native principal pair的连续运输，或一个确实把其全部finite基送到base的目标。583的balanced \(L^1\times\)mass tail给了原native完成化；E中的任意固定指数/多项式系数费也由较大 \(p_Q\) 支配。没有从这一点推出一般ordinary Pic／算术Chow都接受未定义的无限principal对象。

本节全吞结论限于已经忘掉a0的E。若补回 \((a_0,a)\in\mathbb C\times E\)，weight0 finite \(J_m\) 的principal span是 \(\{0\}\times E_{\rm fin}\)，其闭包仅为 \(\{0\}\times E\)；a0的原line/metric标签不能因此叫作principal。583/584已给actual \(a_0(p_b)\ne0\) 的关系反例，所以保留该line也未付Pan下降。

## 4. actual Pan 的强E闭包反而是一个 proper closed spectral subspace

沿405/584固定实际正H，
\[
 M_H(z)=L_H(z)=\xi_{\rm Riemann}(z+1/2)/2,\qquad
 w(z)=(z^2-1/4)M_H(z),\qquad
 p_b=\tau_b(D^2-1/4)H\in\mathcal P .
                                                               \tag{11}
\]
全部b∈R的实际关系在同一全源域，且
\[
 L_{p_b}(z)=e^{bz}w(z).                                   \tag{12}
\]
这保留noncompact尾。w的零点为两simple pole方向 \(z=\pm1/2\)，及全部 \(z=\rho-1/2\)（重数 \(m_\rho\)）；\(\xi(0)=\xi(1)=1/2\) 保两pole处阶数恰为1。不假设RH或简单性。

由519完整jets识别和双次数，
\[
 L(\mathcal P)=L(\mathcal F)\cap w\mathscr H .              \tag{13}
\]
这是在明确源空间中的旧结果：中心化只将 \(M_f(s)\) 改为 \(L_r(z)=M_f(z+1/2)\)。w除法仅指entire可除；不附带新源范数界或把任何entire商因子当作源。

理想 \(M=w\mathscr H\) 在 \(\mathscr H\) 中闭：它等于在w全部零点处按其重数消失的完整jet条件之交；反向正是局部holomorphic除法，零点离散保证商entire。另一方面，(12)的有限差分
\[
 h^{-n}(e^{hz}-1)^n w(z)\longrightarrow z^n w(z)
 \quad(h\to0,\ h\in\mathbb R)
                                                               \tag{14}
\]
在每个compact上一致，左边为有限个实际 \(L_{p_{jh}}\) 的复线性组合。多项式在\(\mathscr H\)中稠密，于是
\[
 \overline{\operatorname{span}_{\mathbb C}
     \{L_{p_b}:b\in\mathbb R\}}^{\,\mathscr H}
 =\overline{L(\mathcal P)}^{\,\mathscr H}=M.                \tag{15}
\]
这是同一实际轨道的closure，不是另造“按定义消零”的关系。

\(M+\mathbb C\) 也闭。它可以直接写成：F在w所有零点处取一个共同的值，且在重零点的1至 \(m_\rho-1\) 阶导数为0；这些是闭线性条件。于是 \(\pi_0(M)\) 在 \(\mathscr H_0\) 中闭，令
\[
 J=A(M)=A(M+\mathbb C)\subset E .
 \qquad
 \boxed{\overline{a(\mathcal P)}^{\,E}=J,\quad
 E/J\simeq \mathscr H/(w\mathscr H+\mathbb C).}             \tag{16}
\]
下界由(15)及连续投影给出，上界由J闭及(13)给出。J是proper：例如F(z)=z在±1/2取不同值，故不属于 \(M+\mathbb C\)。对应joint tower的闭包为 \(TJ\)，不是全E。

这与有限前缀/product稠密并不矛盾。上一finite-cover门给 \(\mathcal B_\infty(\mathcal P)\) 的每个finite投影等于源投影；结合(8)/(9)的稠密和有限维线性像闭合，每个finite坐标投影实际都是整个相应 \(\mathbb C^n\)。所以Pan联合像product稠密，却在E强拓扑中只稠密于proper闭子空间TJ。一个由无限Faber系数计算的entire值／jet泛函可以检测TJ，finite-support product连续泛函不能。

## 5. 忘常数后的pullback kernel：必须支付消常数的一步

从 \(a(r)\in J\) 只能先得
\[
 L_r(z)=w(z)G(z)+c,\qquad G\in\mathscr H,\ c\in\mathbb C .
                                                               \tag{17}
\]
不能直接删去c。在fixed竖带 \(|\Re z|\le1/2\)，合法分部积分n次给
\[
 |L_r(\sigma+it)|\le4p_{1,n}(r)|t|^{-n}
 \quad(|\sigma|\le1/2,\ |t|\ge1).                          \tag{17a}
\]
原源的所有导数和指数权使边界消失；上界用 \(\int e^{-|u|+\sigma u}du\le4\) 即足。因此 \(L_r\) 在该带任意多项式阶衰减。ζ非平凡零点有无界虚部，且其中心化实部在这个fixed带内。在这些w零点代入(17)，得到 \(c=L_r(\rho-1/2)\to0\)，故c=0。再用(13)，才得
\[
 \boxed{a^{-1}(J)=\mathcal P,\qquad
   \mathcal F/\mathcal P\hookrightarrow E/J
   \text{ 连续且代数忠实。}}                              \tag{18}
\]
对doublepolezero源，直接在±1/2代入(17)已迫c=0；但all-source版本不能以这个特殊域代替上面的固定strip论证。

实际537双polezero非根在该Pan商仍非零：若其像属于J，(18)会使其属于Pan，与原完整正Weil值矛盾。这不是新的正号，所用537非根是旧输入。

不把(18)称为原physical Fréchet商与该completion的拓扑同构，也不声称其像是全部E/J。其像稠密，但有明显非physical的完成化类，例如 \([z]\)：若实际 \(L_r=z+c+wG\)，在无界虚部的w零点有 \(L_r(\rho-1/2)=\rho-1/2+c\)，与fixed-strip快速衰减矛盾。故该连续单射有proper dense image；是否有别的受控completion，不由一个新标签解决。

## 6. 全源平移的常数反测与doublepolezero合法修复

E忘掉的是F的常数类，乘子 \(F\mapsto e^{bz}F\) 在b≠0时不保持constants。故不能从raw坐标的连续性声称它自动定义E上的实际平移动力学。

一个完全实际的反测仍用(8)的normalized \(g_\varepsilon\)：
\[
 A(L_{g_\varepsilon})\to0\quad\hbox{in }E,\qquad
 A(L_{\tau_b g_\varepsilon})\to A(e^{bz})\ne0
 \quad(b\in\mathbb R\setminus\{0\}).                       \tag{19}
\]
第一项因为 \(e^{\varepsilon z^2}\to1\)；第二项因为其平移Laplace极限是 \(e^{bz}\)，为非constant entire。于是由actual源的单射性代数定义的平移，在 \(a(\mathcal F)\) 的E子空间拓扑中并不连续。这不是 \(g_\varepsilon\to0\) 于原 \(\mathcal F\)；其强半范数随ε发散。另稿T自同构只搬运这个反测，不能消除它。

同一问题在 \(E/J\) 的actual物理像中仍成立：\(e^{b/2}\ne e^{-b/2}\) 保 \(e^{bz}\notin M+\mathbb C\)，所以(19)在该商中的第二个极限仍非零。连续whole-source action或原520增长合同不能凭(18)自动继承。补回 \(\alpha(F)\)，回到完整 \(\mathscr H\)，可恢复标准continuous乘子；但它的增长没有得到独立算术约束。

**必要范围收紧。** 对
\(\mathcal F_{00}=\{r:L_r(\pm1/2)=0\}\)，忘常数有合法的连续修复。令
\[
 E_{00}=\{a\in E:\Phi_a(1/2)=\Phi_a(-1/2)\},
 \qquad \Phi_a=\sum_{m\ge1}a_mP_m ,
\]
则
\[
 a\longmapsto\Phi_a-\Phi_a(-1/2)
\]
把闭hyperplane \(E_{00}\) 拓扑同构到
\(\mathscr H_{00}=\{F:F(\pm1/2)=0\}\)。它正好恢复任何actual \(r\in\mathcal F_{00}\) 的 \(L_r\)。乘 \(e^{bz}\) 保持 \(\mathscr H_{00}\) 和 \(M=w\mathscr H\)，因而给 \(E_{00}/J\) 的标准连续作用。全源(19)不能排除这个已分离双次数的子域，也不能否定保留a0或额外degree记录的修复。

这个子域商仍只是完整ζ零点jets的entire完成化；独立中心化增长／Weil符号的责任恰是520/553的旧责任。连续作用并没有证明双向次指数growth，Jordan重数也未被去掉。

## 7. 强旧净值、原费用及后续准入

本次净链为：
\[
 \text{583 Faber/raw系数}
 \longleftrightarrow E\simeq\mathscr H/\mathbb C
 \xrightarrow[\text{另稿}]{T\text{ oldform坐标}}
 E ,
\]
加上519完整jets、405实际轨道与标准entire理想closure。它准确说明strong Pan商未被finite reader门排除，但所得谱性恰是519/520已知谱商的弱完成化，没有新的算术principal来源、整过滤、截面乘法、mixedRR、完整signedWeil身份或独立growth约束。583的finite principal完成化全吞与(16)的Pan proper商是两个不同前提，不能相互替代。

原费用不因这些同构消失。r→entire compact seminorm取有限 \(p_{N,k}\)；(5)的Q改变需换q圈及 \(j(q)\) 的target compact，583原 \(p_{A_s}\) 随之改变。fixed窗du／zero-extension Dlog按583分别付费；E半范数不是原物理norm，(18)没有有界原norm逆。没有跨d/cofinal高度统一费，也没有将强目标预算升级为经典whole后果。

故建议**标准旧坐标／强旧商运输0数学轮**。不建C048/585，不恢复已用C047预算；不把“无限联合／strong商非零／continuous action”当成新primitive输入。最强经典542+555→557 whole leading4/5负惯性UPPER及actualq/core/coupling/Ξ、算术/primitive瓶颈均未改变。

后续不应再换seed/level/sequence权或对同spectral quotient反复付坐标费。数学晋级须给实际source到非零primitive/relative对象的独立整模型、乘法／RR、原费用／正号或完整比较净后果，或从经典原数据给完整signed缺陷消失的独立正逼近规则。它不能仅是旧商的形式改名；但底层线性map允许代数上factor经过旧 \(L_r\) jet商，真正新增的独立结构／费用／同源比较仍可成为关键输入。一个具体来源门须将这些实物及其关系消去、同源非根和净后果写成可核首测；当前tower没有给出这样的新桥。没有该实物时不推荐下一数学合同，更不能用“去读另一paper”代替缺失设施。root可依既有策略选择一个具名章级来源门，但本稿不自行扩展或建立第二执行权威。

## 8. 消费前件摘要

| 项目 | 本稿限定 |
|---|---|
| 对象/domain-range | physical \(\mathcal F\to\mathscr H\to E\)，常数商明确；T原源/反演由另稿支付 |
| relation/商角色 | actual \(\mathcal P\) 为519全jets+双pole；principal finite基闭包与Pan强闭包分离 |
| 量词/极限 | 全complex源、全部real b；compact-open/E收敛与原Fréchet不混同；Gaussian每fixedε合法 |
| paid误差 | Faber(6)几何尾、差分compact一致收敛、source fixedstrip积分分部；无数值替证明 |
| 净结论 | E坐标重编码；Pan completion proper且代数忠实，但无新独立正号/算术capacity |
| 动力学 | 全源忘常数反测；保a0/双polezero子域可修，仍欠旧独立growth |
| strongest-old比较 | 519/520/553/583直接标准运输，建议0轮，不以new quotient标签升级 |
| 未覆盖/未付 | 其他actual source-map、额外relative几何、不同有费completion、未逐层Pan的D′正逼近；均需新实物 |

本稿的结论须与另稿source/sequence inverse、fresh及root消费范围一起验收。hash只绑定版本，不认证数学；STATE/cadence/Git由root统一处理。
