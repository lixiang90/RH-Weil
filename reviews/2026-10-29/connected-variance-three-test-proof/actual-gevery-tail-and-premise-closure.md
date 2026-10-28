# C054：固定Gevrey源的actual绝对尾与positive occupation前件闭合

2026-10-29；`/root/post_quiet_phase_fresh` 本次独占数学证明支链，区别于旧connected-variance准入终态。已恢复README／STATE、check→show、同Goal／runtime1793085111、C054、D20261029C／formal18和宏观前沿；现场C054 running、budget1、settlements空。root统一本次真实数学迭代，本稿不自行计轮、预591或完成Goal，不改STATE／cadence／Git／看板，无新primary／web／数值。

**本腿结论：对合同唯一固定ψ和g，每个先fixed δ>0都有 `B_Π,X(δ)→0` 的absolute界，统一支配所有共同 `0≤R_X≤Π_X`。一般R的HS因式、actual核／2π、非负killing均可闭合。使用的是旧C052强Tail及actual away-zero对角界，不是假设Cauchy离对角界，也不是把旧relative little-o升级为absolute。** 本稿原件仍待不同fresh及root消费。

## 1. 同一actual对象及严格weighted trace

receiver为 `H=L²(R,dt/(2π))`，第一槽linear；physical源原du、`f=rhat=∫r(u)e^(−itu)du`。原560／585投影为
\[
 \Pi_X=B_XP G_X^{-1}PB_X^*,\quad
 G_X=(PB_X^*B_XP)|_{\operatorname{Ran}P},\quad
 D_X(t)=\prod_{p\le X}(1-p^{-1/2-it}),\quad B_X=M_{D_X}.
\]
全Gram逆及全部returns保持。kernel相对 `dμ=dt/(2π)`，对角 `k_X(t,t)=2πρ_X(t)`；故
\[
 T_{\Pi,X}[f]=\|M_f\Pi_X\|_{HS}^2
       =\int|f(t)|^2\rho_X(t)dt
       =\int|f(t)|^2k_X(t,t)d\mu(t).
\]
每finite X及固定compact smooth源的HS域已付。下文可测切口的HS资格由强Tail另外支付，非将所有L²函数无条件放入原trace域。

一般occupation固定 `0≤R≤Π_X`，允许R依X／全部非局部资料／固定三测试组选择，但同层三源使用同一个R。先定义严格的
\[
 T_R(f,g)=\operatorname{Tr}(M_fR M_g^*),\quad
 C_R(f,g)=\operatorname{Tr}\bigl[(R^{1/2}M_fR^{1/2})
                    (R^{1/2}M_gR^{1/2})^*\bigr].
\]
`M_fR^(1/2)∈S₂`由positive operator order及 `T_R[f]≤T_Π[f]` 得到；C也是S₂×S₂。合同形式记号 `Tr(R M_fM_g*)` 按这个weighted positive sandwich／极化消费，**不宣称未夹源乘积本身S₁**。正确HS因式为
\[
 \Delta_R(f)=(I-R)^{1/2}M_fR^{1/2},\quad
 V_R(f,g)=\langle\Delta_R(f),\Delta_R(g)\rangle_{HS}=T_R-C_R.
\]
对R=Π恢复原 `(I−Π)M_fΠ`。对一般R不能用 `(I−R)M_fR` 冒充同一variance。

## 2. 两个已付旧接口：须区分actual k与bare Q

全文核C052当前两原件，采用其原量词：令 `L=logX,A=√X/L`。

**强Tail（upper/tail稿§5）**：actual Π_X的正operator比较、weighted commutator非负核／Tonelli给所有bounded measurable切口的
\[
 \int_{|t|>T}|F(t)|^2\rho_X(t)dt
 \le C_{tail}\int_{|t|>T}|F(t)|^2
                   [\sqrt X+\log(2+|t|)]dt.\tag{T}
\]
这里C_tail是固定常数，不依切口T、X。F为本稿唯一fixed `itG`，所以即使保守允许常数依该fixed源，也不影响任何量词。该原证明对可测乘法定位成立；不是仅 `T=L` 时的UT结论 `o(√X/L²)`，也不需要smooth-weight trace差公式。

**Actual away-zero（localization稿§6(4)–(5)）**：每先fixed δ>0、B>0，
\[
 k_X(t,t)=|D_X(t)|^2Q_X(t),\quad
 Q_X(t)=\langle G_X^{-1}k_0(\cdot,t),k_0(\cdot,t)\rangle,
\]
\[
 \sup_{\delta\le|t|\le L^B}k_X(t,t)
 \le\exp[-(c_\delta+o_{\delta,B}(1))A],\quad
 c_\delta=4-\frac4{\sqrt{1+4\delta^2}}>0.\tag{L}
\]
原6.12先控制weighted evaluator Q，随后与actual `|D_X|²`相乘才得到(L)。本稿没有把裸inverse-Euler measure代替ρ，也没用positive trial子核冒actual全投影；2π按上节原measure保持。固定B的log-height在已付prime-sum范围内，非外推全线。

## 3. 合同同一个bump的自含Gevrey2 upper

冻结
\[
 \psi(u)=c\exp[-1/(1-(16u)^2)]\quad(|u|<1/16),
 \quad \psi=0\text{ elsewhere},\quad\int\psi=1,
\]
`g=ψ*ψ#`、`G=ghat=|ψhat|²≥0`；`g′hat=itG`。不使用任何bump Fourier lower或改源。

以下给明确可用常数。令 `b(x)=exp[−1/(1−x²)]`、d=1−|x|。在complex disk `|z−x|≤d/8` 上，
\[
 \Re\frac1{1-z^2}
 =\tfrac12\Re\left(\frac1{1-z}+\frac1{1+z}\right)
 \ge\frac1{4d}.
\]
最近端点那一项的real reciprocal至少 `56/(81d)`，另一项real part非负，故上述较弱常数有效。Cauchy给
\[
 |b^{(j)}(x)|\le j!(8/d)^j e^{-1/(4d)}
                  \le32^j(j!)^2.
\]
对j≥1最后令y=1/(4d)，用 `sup y^j e^{-y}=(j/e)^j≤j!`；j=0直接用|b|≤1。固定阶Cauchy界在端点趋0，零延拓光滑；缩放及support长度1/8给
\[
 \|\psi^{(j)}\|_1\le C_0 A_\psi^j(j!)^2,
 \qquad A_\psi=512,\quad C_0=\max(1,c/8).
\]
分部积分、`j!≤j^j`，在 `|t|≥16Aψ` 取 `j=floor√(|t|/(4Aψ))`，得到
\[
 |\widehat\psi(t)|\le C_\psi e^{-\gamma_\psi\sqrt{|t|}},
 \quad \gamma_\psi=\frac{\log4}{4\sqrt{A_\psi}},\quad C_\psi=4C_0.\tag{G}
\]
小t由 `|ψhat|≤1` 吸收。由(G)及多项式吸收，例如取 `bψ=2γψ`，存在只依该固定ψ的C_F，使
\[
 |tG(t)|^2\le C_F e^{-b_\psi\sqrt{|t|}}.\tag{G1}
\]
可取 `C_F=Cψ⁴[1+(2/γψ)⁴]`。这些固定常数不依X、δ、R或未知ζ零点。

## 4. Absolute away-zero tail闭合

对每个先fixed δ>0定义
\[
 B_{\Pi,X}(\delta)=\int_{|t|>\delta}t^2G(t)^2\rho_X(t)dt.
\]
取合同固定 `T=L⁴`，最终T>δ；分δ<|t|≤T与|t|>T。

(L)取B=4，存在 `X_loc(δ)` 使中段
\[
 B^{mid}_{\Pi,X}(\delta)
 \le e^{-c_\delta A/2}\int|tG(t)|^2d\mu(t)
 =\|g'\|_{du}^2e^{-c_\delta A/2}.\tag{M}
\]
用长度与sup的较弱polylog界亦可；此处用fixed Plancherel质量，不需moving-source一致性。

(T)和(G1)给远段
\[
 B^{far}_{\Pi,X}(\delta)
 \le C_{tail}C_F\int_{|t|>L^4}
 e^{-b_\psi\sqrt{|t|}}[\sqrt X+\log(2+|t|)]dt
 \le C_\psi'(\sqrt X+1)e^{-b_\psi' L^2},\tag{F}
\]
例如可取 `bψ′=bψ/2`，Cψ′只依C_tail、C_F、bψ；令y=√|t|后，仅为多项式×e^(−bψy)的尾。因为 `log√X=L/2`，(F)绝对趋0，而非仅相对 `√X/L²` 小。

合并得到所有实际real X充分大时
\[
 \boxed{B_{\Pi,X}(\delta)
 \le\|g'\|_{du}^2e^{-c_\delta A/2}
       +C_\psi'(\sqrt X+1)e^{-b_\psi'(\log X)^2}
 \longrightarrow0.}\tag{AT}
\]
δ先fixed；起点可依δ和固定ψ，没有δ_X／moving source／频率或cofinal极限交换。Γ／all primepowers只作为旧(T)/(L)的完整输入保留。

## 5. R≤Π的actual kernel、killing与统一尾

`R=ΠRΠ`由positive order得到。设κ_t为RanΠ中的实际raw评价代表，则
\[
 k_R(t,s)=\langle R\kappa_s,\kappa_t\rangle,\quad
 0\le k_R(t,t)\le k_\Pi(t,t),\quad
 \int|k_R(t,s)|^2d\mu(s)=k_{R^2}(t,t)\le k_R(t,t).
\]
连续评价及R有界给合法连续kernel；不是假设R有额外光滑性。正性指kernel的PSD及对角／行质量，不声称k_R(t,s)逐点非负。令 `ρ_R=k_R(t,t)/(2π)`，非负killing measure为
\[
 d\lambda_R(t)=[k_R(t,t)-k_{R^2}(t,t)]d\mu(t).
\]
严格HS配对给jump+killing分解
\[
 V_R[f]=\tfrac12\iint|f(t)-f(s)|^2|k_R(t,s)|^2d\mu(t)d\mu(s)
                      +\int|f(t)|^2d\lambda_R(t).\tag{JK}
\]
对fixed `F_δ=itG·1_|t|>δ`，它是bounded measurable multiplier；(T)使M_FδΠ为S₂。由operator order，正sandwich及其trace合法，且
\[
 B_{R,X}(\delta)=\|M_{F_\delta}R^{1/2}\|_{HS}^2
               \le B_{\Pi,X}(\delta)\longrightarrow0.\tag{OT}
\]
所以(AT)统一于**全部共同**R_X，任意rank／infinite rank／非局部依赖均不改变常数；未断言 `|k_R(t,s)|≤|k_Π(t,s)|`，该逐点支配并非operator order后果。

## 6. 三源不等式扩展所需前件确实够用

此处核另一腿所需R扩展，而不以输出稿存在代其root消费。a=1/2，G≥0；译源Fourier为 `e^(−iat)G(t)`。killing项对译源不变，(JK)直接给
\[
 A_R:=V_R(\tau_a g)-V_R(g)
   =\iint G(t)G(s)[1-\cos((t-s)/2)]|k_R(t,s)|^2d\mu^2\ge0.
\]
对 `0<δ≤1`，写A=G(t),B=G(s)≥0。双内区有
`|tA−sB|²≤2δ²|A−B|²+2(t−s)²AB`，且 `(t−s)²≤16[1−cos((t−s)/2)]`。若一槽在δ外，用另一槽的δ界和 `|t−s|≤2|t|`（t为外槽）；若双外则直接平方和。统一放宽后可用
\[
 |tA-sB|^2\le2\delta^2|A-B|^2
 +64[1-\cos((t-s)/2)]AB
 +8[t^2A^2 1_{|t|>\delta}+s^2B^2 1_{|s|>\delta}].
\]
积分jump项给 `2δ²V_jump(g)+32A_R+8B_(R²)(δ)`。killing内区至多δ²V_kill(g)，外区为 `B_R−B_(R²)`。因为 `0≤B_(R²)≤B_R`，合并不多收一个tail常数，得到
\[
 \boxed{V_R(g')\le2\delta^2V_R(g)+32A_R+8B_R(\delta).}\tag{J}
\]
这也说明一般R的killing不能被省掉；正确纳入后2/32/8仍有效。Π是killing0的特例。

## 7. 完整目标、强旧净值与消费边界

三个源g、g′支持±1/8，τ_(1/2)g支持[3/8,5/8]，同在537 fixed正窗。g及g′非零，所以原完整 `q₀=Q_W(g)>0,q₁=Q_W(g′)>0`。平移不变性给 `Q_W(τ_(1/2)g)=q₀`：Γ／pp自相关不变，双pole为 `2ℓ_c²−2ℓ_s²` 的Hermitian表达，译源时μ±分别乘e^(±a/2)，其mixed product不变。g′并非被宣为polefree，完整目标未裁项。

由(J)+(OT)，若同一R_X在这三个fixed源均趋完整目标，则每fixedδ≤1有 `q₁≤2δ²q₀`，再δ↓0矛盾。全是fixed源，不用旧准入r_τ或unpaid Cauchy bound。合同定量gap常数也足够：δ₀、ε按合同固定；取X₀使B_Π(δ₀)≤q₁/64，若三误差均<ε，则 `V_R(g)≤q₀+ε`、`A_R≤2ε`，(J)迫
`q₁≤q₁/8+65ε+q₁/8≤q₁/2`，矛盾。X₀由(AT)确定，统一于全部共同R_X，不依其rank／选择规则。

强旧扣除须分开：

* (T)/(L)、fullG／2π和Gevrey upper是既有或标准支付资产；(AT)是其对当前唯一固定源的严格absolute消费，不单独领新source／数学轮。
* 旧scalar／poly只定特定加权迹／校准规则，anchor是source补全，quiet是moving source低谱，C053是另一个inverse-Euler权；它们没有同一个 `R≤Π` covariance的三fixed-source coupled anomaly结论。
* 上一准入只付V合法性、exact `Q−V=C−K+indefinitepole`及条件Cauchy界，没有支付本(J)与实际tail的联合反测；不能把前次未被旧门排除本身算输入。当前真实新连接是positive jump/killing把导数费用与平移异常耦合。

未核到更强旧sameclass结论已决定本三测试障碍。它拒的是共同positive occupation covariance `0≤R_X≤Π_X` 的完整fixed-pair／D′目标身份，覆盖其本类内rank-growing、infinite、非局部和固定测试组自适应选择；外部scalar／growing gain、signed修复、其它carrier或逐源改R而不定义共同型的构造不由此排除。whole4/5 UPPER、独立arithmetic primitive／principal／mixed等主责不在此证明中闭合，长期Goal完成门另由root总体审计。

## 8. 实际版本与读域

全文读两C052原稿，重点核upper/tail§1–5与localization§2–7／§9；只读项目原件，没有读primary新页或C052未核的6.4／6.5／后章。另全文恢复前准入 `strongest-old-domain-and-net.md`，其“当前未准合同／界未证”为当时历史状态，不覆盖本次C054。actual560／585及前准入HS/kernel规范按已核范围保留。LF版本绑定：

| 文件 | LF bytes | SHA256 |
|---|---:|---|
| C054合同 | 4874 | `7e95d495b356df3dd9ff8c554ed98f6441ee03c7517d65fd226582e24d6fd7d2` |
| C052 `source-upper-and-tail-proof-audit.md` | 10211 | `bab769113b4ce8c858dfd4b7a83dea6abd8808436a599d2206ea9a9bf0915fff` |
| C052 `source-localization-proof-audit.md` | 11459 | `809bc7ffc6f1fbf4dd24af0d710af05fb7ca1bc259992430c3fd6760912ffcb1` |
| 537完整fixed窗正性 | 8155 | `269a500556d37fc04a4e44efd2f0899414787743e529506dbbe7395a34eea9f8` |

另一腿输出须另由root对齐，不以口头消息代证明；本腿terminal不等于root已消费或统一计轮。
