# 自由 b 的几何优化、连续证书与完整准入

日期：2026-10-07。作者：radial_review。状态：新增研究推导限定 PASS [T/R]；未改任何旧笔记、论文、README、数学源或既有审计。此报告不是新的无条件无零定理。

在确切的通用源输入成立时，自由 b 的原 compensated-probe 几何可以达到
\[
 \ell_\circ=\frac{11}{551}+\frac{8\sqrt{921}}{1653},
 \qquad
 b_\circ=-\frac4{29}+\frac{230\sqrt{921}}{26709},
 \qquad
 \boxed{\sigma_\circ=\frac{1507-2\sqrt{921}}{1653}}
 \simeq0.874957069799168740.
\]
这严格小于 note 447 固定 b=1/8 的 critical boundary，约改善 1.31·10^(-7)。此最优性仅针对本报告的 low 交点、原 R_* count、kappa=3/4 和整个原 amplitude rectangle；不排除改进 moment、改变物理对象或另一种准入域。

还得到容易复算的有理见证
\[
 b_r=\frac{617}{5000},\quad
 \ell_r=\frac16+\frac1{5825}=\frac{5831}{34950},\quad
 \sigma_r=\frac{40773}{46600}\simeq0.8749570815450644,
\]
带严格连续正余量。下面支付 low、完整 d 范围、actual slots、解析区与临界全族量词。没有把 441 固定 b=1/8 的结论直接换参数。

## 1. 固定输入、方法和精确审计

外部只读输入为 OpenAI September-30-2026 build/paper.tex，commit adc7f1241b42e322a6451854ab7e4b4c146bf78a，canonical LF SHA-256：

42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3。

使用的是通用 smooth calculus/Gaussian annuli (1123–1209、1288–1315)、reflection sectors (2470–2506)、generic reflected energy (7663–7804)、quantitative additive Gram (8340–8360)、coefficientwise physical/Poisson/local identities，以及 detector witnesses、marked/plain/inverse moments、buffered reciprocal、growth/functional equation、fixed-ray prime asymptotic和原全 Hecke 7/8 bootstrap。局部与 continuation 的确切输入范围同已审 441–445；本报告重算其几何相关前件，不把原以 sigma_0>=7/8 陈述的 shared-interface lemma 直接应用到新边界。

新增独立脚本：

scripts/hybrid_free_b_geometry_exact_audit.py

canonical LF SHA-256：5a366da5e8114d158cb76b3a94060155786a0ca637a914b662ba17cd66afa63f。

脚本仅使用 Fraction 与 Q(sqrt(921)) 精确运算，不使用浮点、不写文件，不运行旧审计。执行 841 项显示代数检查全部通过。continuous certificate 由多项式恒等式、正系数及 completing square 给出；189 个 finite direct endpoint cases 仅核公式实现，不证明连续范围。脚本也不认证实际素数、无穷轮廓、外部分析定理、RH 或外部 kernel。

独立子审 free_b_low 只读复核了 generic low/Gram 前件、逐 J 归一化及下述完整 Gram envelope；没有写文件。

## 2. 几何与 low 交点

取固定实参数 ell,b，定义
\[
 l_x=\frac{1-\ell-b}{2},\quad
 l_y=\frac{1-\ell+b}{2},\quad M=1-\ell,\quad
 h=\frac{1+3\ell+b}{2},
 \quad C_b(s)=s-\frac23-\frac b6 .
\]
不改变 completed index cn^3、原 masks、Gaussian、ray calibration、disjoint prime windows、marked/rescaled operations、tuple coefficient q_(p_J)^(-3/2) 或 Poisson scalar quotient。只是改变这些固定尺度的实指数。

对每个 rescaled subset J，令
\[
 d=\sum_{i\in J}\ell_i,\quad 0\le d\le\ell,\quad
 \ell'=\ell-d,\quad M'=M-2d,\quad
 X'=XZ^{-d}/r_J,\quad Y'=YZ^{-d}/r_J ,
\]
其中 r_J=q_(p_J)/Z^d 属于固定 compact positive interval。
\[
 M'+\ell'-1=-3d,\quad Q=q_{b_*}X'Y'\asymp Z^{M'} .
\]
Gaussian completed scale仍为 Z^(1+ell')，所有 surviving marked slots在取同一 row norm 前求和；common profile及全 annular tails 的处理与 coefficient product form不因 b 改变。actual residual row H 的 support不变。

原 generic reflected-energy lemma只要求固定 bounded logarithmic lengths、actual row dyads、independent fixed masks和原 separated coefficients。它给出与 441 相同但这里重新支付的 row exponent
\[
 M'+\left(\frac{5\ell-1+d}{4}\right)_+ +\epsilon .
\]
推导依赖 M'+ell'−1=−3d、Td<=H−3d+small及完整 E_ref；不含 b。因此 empty marks、powerful part counted once、kernel saving先从common profile抽出、原 permitted S-primes等前件均不变。

### 2.1 单项吸收的直接安全范围

source 8340–8360 的 Gram 前件为 Q,Y'>=1、固定 polynomial ranges和
\[
 P_a=Y'^2/Q=q_{b_*}^{-1}Z^b\ge1 .
\]
它实际给出
\[
 \sum |A_m(Y')|^2
 \ll (Q/Y')(1+P_a^{1/6}+P_a^2/Y')Z^\epsilon
\]
及固定 seminorm height cost，系数限于原 ray/Gauss 类。

对全部 J，geometry正余量为
\[
 M'\ge1-3\ell,\quad
 l_x-d\ge\frac{1-3\ell-b}{2},\quad
 l_y-d\ge\frac{1-3\ell+b}{2}.
\]
若直接逐 J 吸收 P_a^2/Y' 到 P_a^(1/6)，所需是
\[
 l_y-\ell-\frac{11b}{6}
 =\frac{1-3\ell}{2}-\frac{4b}{3}\ge0 .
\]
因此
\[
 1/6\le\ell\le1/5,\quad
 0<b\le\frac{3(1-3\ell)}8
\]
是安全范围。边界非严格也给有界常数；本报告两个候选都具有宽裕严格余量。

### 2.2 支付完整第三项后的更宽范围

单项吸收不是必要的。带回完整 Gram factor，Cauchy normalization Q^(-1/2)及同一 row ball给固定 tuple：
\[
 (X')^{1/2}
 Z^{\frac12\max\{0,b/6,2b-l_y+d\}
      +(5\ell-1+d)_+/8+\epsilon}.
\]
比例 r_J只贡献固定常数。tuple数量 Z^(d+epsilon)、原 q_(p_J)^(-3/2)、(X')^(1/2)缩短合计恰为 −d；没有改变 normalization。

b>0时，相对 l_x/2+b/12 的额外 exponent为
\[
 F(d)=-d+\frac12(11b/6-l_y+d)_+
                +\frac18(5\ell-1+d)_+ .
\]
所有分段斜率为 −1、−1/2、−7/8 或 −3/8。因此 max F 在 d=0。ell<=1/5 时最终 low exponent为
\[
 L_{\rm low}=\frac{l_x}{2}+\frac b{12}
                 +\frac12(11b/6-l_y)_+
 =\max\left\{\frac{1-\ell}{4}-\frac b6,\frac b2\right\}.
\]
于是仍保留原 low exponent的较宽范围是
\[
 \boxed{\,1/6\le\ell\le1/5,\quad
 0<b\le\frac{3(1-\ell)}8\,}.
\]
这个范围自动保持上述 geometry正余量。超过该范围时不能继续宣称原 low交点；b/2分支须另行匹配，交点不再独立于 b。

b<=0 不满足本次直接输入的 Pa>=1 前件，未在本报告中偷偷扩展 generic Gram。即使原 Gram证明可能重证 Pa>0版，那也是独立待付输入。本次最优候选在强安全范围内部，不依赖这类端点扩展。

当保留原 low分支时，
\[
 C_b(\sigma)=\frac{1-\ell}{4}-\frac b6
 \quad\Longleftrightarrow\quad
 \boxed{\sigma=\frac{11}{12}-\frac\ell4}.
\]
b消去是同一 physical normalization 的精确计算，不是只在旧 b成立的公式。

## 3. Endpoint 的自由 b 多项式

采用原 actual counts接口：kappa=3/4、alpha=5/6，
delta∈[1/50,3/4]，x=q/delta∈[0,1/2]，y=1/2−x。
\[
 D_x=3-\frac{17x}{9},\quad
 P_x=(2-\frac{8x}{9})(1-x),\quad
 J_x=(5/6-\delta)D_x+\delta P_x,
\]
\[
 R_*=1-\delta+
       \frac{(5/6-\delta)\delta P_x}{2J_x},\qquad
 J_x\ge35/54>0 .
\]
These coefficients come from the actual inverse/plain crossing; they are not reoptimized using a hypothetical extra supply.

在 low交点上，endpoint
\[
 E_\sigma(h)=
 -\frac14+\frac{5\ell}{4}+\frac b6
 +(\tfrac12+\ell)\delta+\ell\delta x-h(1-R_*)
\]
满足
\[
 \partial_bE_\sigma=R_*/2-1/3 .
\]
定义正比例 numerator
\[
 F_{\ell,b}(y,\delta)=648(-2J_x E_\sigma(h))
                      =A(y)\delta^2-B(y)\delta+C(y),
\]
其中
\[
\begin{aligned}
 A(y)&=252+756\ell-576b\\
 &\quad +(648+288\ell+720b)y
 +(288+1008\ell+864b)y^2+1152\ell y^3,\\
 B(y)&=624-1440\ell-1176b
 +(504-420\ell-456b)y
 +(-48+120\ell+432b)y^2,\\
 C(y)&=555-2775\ell-370b
 +(510-2550\ell-340b)y.
\end{aligned}
\]
脚本独立用原 endpoint 公式核实 F=−1296JE，而非只测试 A,B,C 的相互一致性。

令 Q(y)=4A(y)C(y)−B(y)^2。只要 A>0、Q>=0，就有
\[
 F=A\left(\delta-\frac{B}{2A}\right)^2+\frac{Q}{4A}\ge0.
\]
这证明整个 continuous rectangle 的 E_sigma<=0。

y=0时的判别式为
\[
 Q(0)=-530496b^2+1887840b\ell-184032b
             -10465200\ell^2+678240\ell+170064 .
\]
对于固定 ell，b方向极大点与值恰为
\[
 b_{\rm opt}(\ell)=\frac{2185\ell-213}{1228},\quad
 Q_{\max}(0)=
 -\frac{1631700}{307}(1653\ell^2-66\ell-35).
\]

## 4. 精确最优 saddle 的全 y 证书

取 e=ell_circ 为 1653e²−66e−35=0的正根，b=b_opt(e)。有
\[
 1/6<e<167/1000,\qquad 123/1000<b<124/1000.
\]
这些隔离界可直接平方 sqrt(921) 的有理端点核实。

在临界二次关系下，A的系数化为
\[
 A_0=\frac{108036-82548e}{307},\quad
 A_1=\frac{160596+481716e}{307},\quad
 A_2=\frac{42408+781416e}{307},\quad A_3=1152e .
\]
它们全部严格正。Q的系数是
\[
\begin{aligned}
 Q_0&=0,\\
 Q_1&=\frac{17404800(5465-31728e)}{169157},\\
 Q_2&=\frac{1200(47597384-214807491e)}{169157},\\
 Q_3&=\frac{4800(131691060e-18009311)}{169157},\\
 Q_4&=\frac{14400(1377691e-209998)}{8903}.
\end{aligned}
\]
Q_1,...,Q_4严格正，单用 1/6<e<167/1000即可验证符号。故对所有 y>=0，Q>=0；对y>0严格正。在原rectangle及J>0范围：
\[
 E_{\sigma_\circ}(h)\le0.
\]
唯一等号为
\[
 y=0,\qquad
 \delta=\delta_\circ=\frac{49-\sqrt{921}}{48}
           \simeq0.388583712271103409,
\]
因为 B(0)/(2A(0))恰为此值。它确实在[1/50,3/4]内部。

### 4.1 本几何/接口中的真正最优性

在固定 y=0、delta=delta_circ处，有 R_*=2/3。因此 endpoint完全不依赖 b，并等于
\[
 -\frac5{12}+\frac{3\ell}{4}
                  +(\tfrac12+\tfrac32\ell)\delta_\circ .
\]
零点恰为 ell=e，ell方向斜率
3/4+3delta_circ/2>0。所以任何 ell>e、任意 b都会在这个实际rectangle内的点产生 E_sigma>0。不存在仅换 b、仍用原 R_*和此low交点，把全部 endpoint降到非正的更大 ell。

这比只最大化 Q(0) 更强：反例点明确在需要的 delta范围内。它仅是该代数/接口优化的障碍，不能解释为实际 L零点、RH反例或所有方法的最优无零区。

critical endpoint只有非正；它并不阻断 continuation。下一节以实际 global Delta>0支付 real losses，正如447的critical逻辑。

## 5. 有理严格见证

对 t=1/5825、ell_r=1/6+t、b_r=617/5000，几何为
\[
 l_{x,r}=2480617/6990000,\quad
 l_{y,r}=3343183/6990000,\quad
 h_r=1891861/2330000,\quad \sigma_r=40773/46600 .
\]
A,C各系数正，Q各系数全正。脚本给出 Q_0>0，并逐系数核准
A_0Q(y)−Q_0A(y)>=0。因为 J<=5/2，
\[
 -E_{\sigma_r}(h_r)
 \ge\frac{Q_0}{12960A_0}
 =\frac{10580567}{347281513800000}
 \simeq3.04668304518\cdot10^{-8}.
\]
可保守取 m_ad=1/100000000。这个数是全 continuous rectangle 的正余量，不是网格经验值。

note447精确给 t_c<1/5841；而1/5825>1/5841。因此有理sigma_r=7/8−1/(4·5825)已经严格优于447critical，无需用decimal比较。

## 6. 全部 d 范围、floor与供给

general d的原 accounting在此几何仍为
\[
 E_\sigma(d)=K_\sigma+(\tfrac12+\ell)\delta+\ell q
 -h(1-R)+(d-h)(R+\delta/2-z_0),
\quad K_\sigma=\frac23+\ell+\frac b6-\sigma,\ z_0=17/50.
\]
可由完整 unfactored exponent
a−sigma+h(z_0−1/6)−a l_y−ell/2+qell+d(R+delta/2−z_0)
直接验证。source pointwise joint conductor estimate 与 moment counts的q相同；b不修改错误项、character presentation 或primitive conductor savings。

对 central R_*，R_*>=1−delta，使 d斜率至少
33/50−delta/2>=57/200>0。故 [1/2,h]由endpoint控制。floor a=51/100独用R=1，不杜撰witness。

middle使用原无槽common bound
R=76/75−2delta/3，覆盖floor。其 d斜率为101/150−delta/6>0。最坏q<=delta/2后，精确有
\[
 E_\sigma(1/2)=
 -73/300+(13/50)\ell-(49/300)b
 +\delta(1/6+3\ell/4-b/4).
\]
当前候选的delta系数正，最坏delta=3/4，得
\[
 E_{\rm middle}\le -71/600+(329/400)\ell-(421/1200)b .
\]
这些是本轮重算的实际envelope，不照搬旧固定b的geometry-variation常数。

在optimal b=(2185e−213)/1228下，全部余量化为
\[
\begin{aligned}
 {\rm Gram}_{allJ}&=(1347-7133e)/1842>2/25,\\
 5e-h&=(6411e-1015)/2456>1/50,\\
 E_{\rm floor}(h)&=(290401e-49533)/184200<-1/200,\\
 E_{\rm middle}&=(292151e-84703)/1473600<-1/50,\\
 E_{\rm small}&=(2020475e-1127329)/9210000<-2/25 .
\end{aligned}
\]
上述bounds由同一有理隔离区间核实，脚本还直接以代数数核符号。

实际slots supply条件是ell/(h+zeta)>7/37；更强的ell/(h+zeta)>1/5由5ell−h−zeta>0提供。root包已有 inverse/plain branch strict margins、actual full-slot greedy selection和zero-capacity treatment。此处重新验证 supply，未由供给比增加直接推导 moment theorem。

rational:
\[
 {\rm Gram}_{allJ}=148903/1747500,\quad
 \ell_r/h_r-7/37=3420319/209996571,\quad
 5\ell_r-h_r=155417/6990000.
\]
可取zeta=m_ad/32，全部余量严格正，h+zeta<1。

critical:在反证sigma_circ<beta_*<=7/8下，令
Delta=beta_*−sigma_circ>0，取zeta=Delta/32。因为
\[
 \Delta\le(e-1/6)/4,\qquad
 \zeta\le(e-1/6)/128<1/384000 ,
\]
5e−h>1/50足够保证actual supply，且h+zeta<1。d斜率上界2，延伸到h+zeta的费用至多Delta/16。critical的E_beta=E_sigma−Delta，故扩区后仍有至少15Delta/16的中央余量，尚未扣小量。

mesh/rounding/whole-slot lengths先按global Delta（有理见证则m_ad）选择，再选固定even K。由于w_i=ell_i/d<=2ell_i，能让每个w_i小于plain uniform mesh。internal amplifier pool与actual prime slots仍是严格分离，而非包含关系。Theta固定有限系数、full conjugation、outside-S inducing exceptions与S-supported finite units均保持；zero-capacity端点仍用无槽moment。所有 annular offsets最后在固定K阈值吸收。

## 7. 局部解析、principal和独立outer

geometry变动不更改任何local P_p^*/H_p/G_p 的系数。令sigma取sigma_circ或sigma_r，沿原新域D2*(sigma)直接重放有限local table证明：

- sigma>5/6>401/600；所有R,V,D分母保持严格距离。
- good defect c_b=sigma−3/50>81/100。
- ramified defect c_r=sigma−1/20>82/100。
- principal四error幂仍为 −x、−6z、4−5x−6z、1−w−6z；最弱为−sigma。
- 全tuple先用G_p替换；general contour不除H_p。principal及dynamic近one区域才用quotient。
- D1中theta=(-w_r)_+和epsilon_H=min(epsilon_0,1/50)仍保留，whole-bin先global再local，amplitude/error partitions后置。

固定target-independent P0仍可使positive product majorant小于1/2。相同S与same actual ray slots产生same非零c_S A_T，A_T~(logZ)^(-K)，mu可取sigma ell/(2K)>0。double residue仍在w=1,z=1/6，Gaussian仍为exp((s−5/6)^2)；只有linear Mellin normalization变为C_b。principal余量为
\[
 m_w=l_y/20>0,\qquad m_z=h/600>0,\qquad\mu>0.
\]
不能为改善low另造normalizer。

small rows仍用全physical absolute tuple，D1(1/3)因sigma+1/2>4/3而准入。源small绝对lemma内写D1(3/8)在新边界未直接引用；这里重新核局部界及实际D1(1/3)。采用d_min=1/100，前节显示的negative small margin来自
h(17/50−1/6)−l_y/2+(63/50)d_min。

large rows仍在(2,2,z_infty)保留full tuple与所有u，绝对量
\[
 B_0=l_x/2+1+l_y=7/4-3\ell/4+b/4,
\]
\[
 Z^{B_0+(h+\zeta)(1+\epsilon)-\zeta z_\infty+\epsilon}.
\]
先zeta再选固定足够大z_infty，任意prescribed saving均可；这需要generic all-height/absolute bounds，费用固定于external tail order之前。它可能给很大但有限的fixed orders和阈值，无需声称数值实用。

full numerator的strict ramified conductor budget仍只使用一次；实际b不改变local labels、joint subset或buffered reflected value的范围。q、delta及all amplitude bins始终同源。

## 8. Critical闭合的真实量词与尚未认证的输入

critical参数可固定为上述精确代数数，generic输入允许固定实长度；不要求lengths有理。唯一endpoint等号不产生actual zero。

在global反证gap Delta>0下，次序是：

1. 用Delta支付low与inverse-normalizer损失，取共同omega=Delta/2。
2. 中央high由E_beta<=−Delta提供预算；先选moment losses、strict capacity decrement、uniform mesh、rounding，再选K/windows。
3. 随后选mu=sigma_circ ell_circ/(2K)，amplitude bins、prime小幂、e以及principal/outer余量；不因mu较小回选mesh。
4. zeta=Delta/32，支付extension至多Delta/16，所有中央real losses可继续压到Delta的小份额。
5. 选target后的arithmetic data与same S，然后internal moment/Sobolev/seminorm orders，得不随external N变化的A_eta,B_eta。
6. 用actual detector height ceiling先限制tau_eta，之后选external N_eta，再阈值。physical z、witness、prime frequencies仍共享一次cumulative T1/2 allocation。
7. 取共同m0为Delta、m_w、m_z、mu、floor/middle/small等正margin的最小值的一固定小份额。得到target-independent sigma_hi>0，而tau_eta,N_eta、常数、阈值允许依target。
8. 相同normalized physical probe与principal f_eta满足以C_b为linear exponent的low/high合同。Gaussian给Z→0右移；共同saving给Mellin局部一致收敛；|H_eta|>=1/2排除取消。supremum非attained也提供矛盾target。有限Euler factors及quadratic Dirichlet transfer处理同441–445。

这是相对于确切[R]的完整参数推导接口。它不重证generic reciprocal/moment/energy/Poisson/Hecke输入自身，不把固定σ0>=7/8的shared lemma当作可直接代入，也不宣称external Lean或analytic kernel已经通过。

有理见证可在固定m_ad=10^(-8)上重复同一先mesh/K后mu的次序，无需用critical的零附加余量。报告至此停止扩展；将来主稿需独立再审并绑定其最终hash。
