# 共享轮廓向 sigma1 的扩展：独立推导与精确来源

日期：2026-10-07。推导人：progress_audit。

本文为442的解析前件输入。外部的完整局部算术恒等式、原基础probe/补偿操作及固定ray素数渐近为 [R]；从这些明确输入推得的新Euler域、同源有限tuple全纯性、局部误差与轮廓重放为 [T/R]。本文不把参数代数变成实际中间行计数定理，不证明新的Hecke或ζ无零半平面，也没有运行Lean或重建外部项目。

## 1. 固定对象、哈希与参数

只读来源：

- 项目：E:/codex-build/math。
- 文件：preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex。
- 固定提交：[adc7f1241b42e322a6451854ab7e4b4c146bf78a](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)。
- canonical LF SHA256：42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3。
- canonical LF规则：CRLF及单独CR均换为LF，然后按UTF-8取SHA256。下文行号是该固定源文件的1起始行号。

沿用439/441的同一个物理有限补偿probe、原算术数据、Gaussian、ray calibration、zero-on-nonunit masks以及固定有限个disjoint annular prime slots，不改变角色或理想行。

\[
 b=\frac18,\quad \ell_1=\frac{10003}{60000}
 =\frac16+\frac1{20000},\quad
 \sigma_1=\frac{69999}{80000}
 =\frac78-\frac1{80000}.
 \tag{1}
\]

由原几何定义直接得

\[
 l_x=\frac{42497}{120000},\quad
 l_y=\frac{57497}{120000},\quad
 h=1-l_x+\ell_1=\frac{32503}{40000}.
 \tag{2}
\]

主信号为同一个固定双留数，

\[
 C(s)=s+\frac{l_x}{2}-1+\frac h6=s-\frac{11}{16};
 \tag{3}
\]

其中1/6是ζ_F(6z)的极点位置。槽长改变不改变此留数。

假设正在作反证，β_*为原全集有限阶primitive Hecke角色的共同零实部上确界，β_*>σ1。以下所用1/L的global bounds是在Re s>β_*，不是假设待证σ1半平面已经无零。若另已调用原全Hecke7/8结论，可加β_*≤7/8；本节局部解析和外行轮廓不依赖这项上界。

## 2. 原7/8限制的准确地图

| 源label与行号 | 真正限制 | 新边界的处理 |
|---|---|---|
| lem:local-euler，4010；eq:local-region-one，4054–4055 | D1要求s≥51/100、z≥17/50、w≥−1/100、s+w≥1+ε0；ε0可为任意固定正数 | 保留D1本身 |
| eq:local-region-two，4056–4057；D2定义，5574–5575 | 原D2写s≥7/8、z≥33/200、w≥19/20 | 本文§3扩为s≥σ1 |
| eq:shared-principal-data/nonvanishing，5520–5531 | 原Hη仅在Re s>7/8声明全纯并近1 | 440及本文§3给同一信号在Re s≥σ1的全纯和非零 |
| def:stage-high-data，5582–5623 | 完整校正而非逐槽商；需要每个固定box及q_u≤Z^D时固定B,J的全高度majorant | 本文§4直接保留无商tuple定义；J可取0 |
| lem:external-contour-tails，5672–5728 | 测试任意阶衰减及固定算术B,J | 没有7/8数值门槛 |
| lem:fixed-bin-contour，5808–5896 | 5811声明σ0≥7/8；证明实际使用D1、a≤β_*及buffered reciprocal | 本文§7按原证明重放 |
| lem:bin-contour-accounting，6021–6155 | 6024声明σ0≥7/8；6118调用上一轮廓引理 | 记账式对一般C(σ0)恒等；不另有7/8不等式 |
| lem:principal-residue-interface，6174–6301 | 6178声明σ0≥7/8；6230–6239使用D2，6290–6299使用Hη | 扩展D2及同一Hη；另外仍须付l_y/20、h/600、μ正余量 |
| eq:principal-local-approximation，9066–9077 | 四错误指数原均≤−7/8 | 本文§5改为≤−σ1，不能继续沿用−7/8 |
| lem:outer-row-tails，6342–6463；lem:compensated-absolute-local-bounds，9101–9195 | 6418–6419及9134写D1(3/8)，实际依赖β_*>7/8 | 小行改用固定D1(1/3)，局部表格重新检查 |
| sec:tails，15853–15918 | 小行有独立负幂余量；大行需固定z∞足够大 | 本文§8给新几何精确小行数值；原49/14400不涵盖这些外行 |

原 lem:buffered-bins，4281–4321，floor为51/100；lem:logarithmic-control，1531–1551，允许a∈[1/2,1]。二者没有独立7/8门槛。不能把声明有σ0≥7/8的旧引理直接作为已经适用于σ1的定理；下面支付的是其证明的相应新版本。

## 3. 基础Euler校正的新域

记Q=Np，x_r=Re x，w_r=Re w，z_r=Re z。原完整局部定义4013–4047及defect恒等式4139–4142为

\[
 H_p-1=
 \frac{D(V+W-VW)-VW+(1-V)(1-W)\mathcal E_p}{1-D},
 \qquad \mathcal E_p=P_p^*+D.
 \tag{4}
\]

没有1−W分母。保留原u的零延拓：p|u时D=W=0，式(4)成为(1−V)P_p^*。

考虑

\[
 D_2^*=\{x_r\ge\sigma_1,\quad
 z_r\ge33/200,\quad w_r\ge19/20\}.
 \tag{5}
\]

原j=0局部表在p不整除u时给

\[
 |\mathcal E_p|\ll
 Q^{4-6x_r-6z_r}+Q^{1-x_r-w_r-6z_r}.
 \tag{6}
\]

这里w_r>0，不需要负w修正。分母1−R、1−V、1−D一致离零，所有常数对虚部和单位模相位一致。逐项代入(4)得

\[
 |H_p-1|\ll Q^{-1-c_{\rm box}}\quad(p\nmid u),
 \qquad
 c_{\rm box}=
 \min\{6\sigma_1-401/100,\ \sigma_1-3/50,\ 47/50\}
 =\frac{65199}{80000}>0.
 \tag{7}
\]

最需检查的幂分别是Q^(301/100−6σ1)、DW的Q^(−σ1−19/20)及VW的Q^(−194/100)。在p|u时原j=1,…,5表的最近项为Q^(1−x_r−w_r)、Q^(3/2−3x_r)，其余项不大于它们，故

\[
 |H_p-1|\ll Q^{-c_{\rm ram}},\qquad
 c_{\rm ram}=\min\{\sigma_1-1/20,\ 3\sigma_1-3/2\}
 =\frac{65999}{80000}>0.
 \tag{8}
\]

通过O_F(y)理想计数，good-prime正乘积∏(1+CQ^(−1−c_box))收敛；有限ramified乘积由除数乘积估计为O_ε((Nu)^ε)。这些逐素数上界对所有高度及单位模相位一致。于是基础校正在D2*中正常收敛，在每点的一个邻域内全纯，且

\[
 |\mathcal H_{\eta,u}(x,w,z)|\ll_\epsilon (Nu)^\epsilon.
 \tag{9}
\]

邻域性不是仅凭闭轮廓点态收敛：所有指数在(7)(8)都有严格正余量，允许把三个实下界同时略微向外移动，分母仍一致离零。

对u=1，全部good-prime尾可令P0足够大，使整个D2*上

\[
 |\mathcal H_{\eta,1}-1|
 \le\exp(CP_0^{-c_{\rm box}})-1\le\frac12.
 \tag{10}
\]

P0可在目标前选择，因为常数只依赖固定域和相位模长，增加目标的有限排除集仍缩小同一个正majorant。沿用源校准扩大S，不改变T或掩码 [R]。主行每个H_p也可同时保证|H_p|≥1/2。

同一信号Hη(s)=H_{η,1}(s,1,1/6)还可用440的更准确闭式：

\[
 H_p(s,1,1/6)=\frac{1-Q^{-2}}{1-r}
 \left(1+\frac{Q^{-1}(D-r)}{1-D}\right),
 \quad r=a_p^2Q^{3-6s}.
 \tag{11}
\]

所以Hη在Re s>2/3全纯；对每个固定σ>2/3都能作统一近1/非零选择。本文只需固定σ=σ1，不要求σ↓2/3的统一常数，不对L作任何新的无零假设。

## 4. 完整有限tuple及全高度majorant

保持源 eq:holomorphic-selected-tuple，8707–8711 的定义：

\[
 \mathfrak H_{\eta,u,Z}
 =\sum_{(p_i)\in\prod_i\mathcal P_i(Z)}
 \prod_{i=1}^K
 \left[W_i(q_{p_i}/P_i)q_{p_i}^{z-1}G_{p_i}\right]
 \prod_{\substack{p\notin S\\p\notin\{p_1,\ldots,p_K\}}}H_p,
 \quad P_i=Z^{\ell_i},\quad \sum_i\ell_i=\ell_1.
 \tag{12}
\]

K、正数ℓ_i、窗、norm-ratio紧区间和disjoint supports都在Z及目标前固定。式(12)没有逐槽P_p或H_p的除法。每个Z的素数tuple集有限；selected因子是原完整有理表达式，其分母仅1−R、1−V、1−D，在D1和D2*都一致离零。

由§3，在D2*任何固定real box内，不论删去哪个有限selected集合，unselected正乘积均满足

\[
 \prod_{p\ {\rm unselected}}|H_p|\ll_\epsilon (Nu)^\epsilon.
 \tag{13}
\]

D1内则用源8733–8747及ε_H=min(ε0,1/50)>0。因删去selected因素只是删去正majorant的某些≥1因素，(13)不依赖tuple；不能把它写成除以可能为零的H_p。

在固定box中，准确局部表给|G_p|≪Q^B，B只依赖该box，且对所有高度统一。每槽至多O(P_i)个理想、Q∼P_i，故

\[
 |\mathfrak H_{\eta,u,Z}|
 \ll_\epsilon (Nu)^\epsilon
       \prod_iP_i^{z_r+B}
 \ll_\epsilon (Nu)^\epsilon Z^{B'}.
 \tag{14}
\]

B′固定，不能随稍后外尾积分分部阶数N变化。每个Z的有限和与正常收敛乘积说明完整\(\mathfrak H\)在D1/D2*全纯；对于Nu≤Z^D，式(14)直接给源 eq:stage-all-height-majorant，5614–5619 的B固定、J=0版本。它只证明完整校正的解析准入，不证明central error-slot或detector容量计数。

同源身份也必须保留。原 eq:selected-local-operation，8717–8719 的局部算术等式

\[
 \overline{\eta(p)}Q^{x+z-1}P_p^*-Q^{z-w-1}P_p
 =\frac{1-D}{(1-V)(1-W)}Q^{z-1}G_p
 \tag{15}
\]

不含ℓ或X/Y的固定数值。disjoint slots确保每个selected prime只出现一次。对每个固定Z，原物理补偿仍是基础probe恒等式的有限线性组合；在绝对起始线(3,3,2)提取同一个标量商即得到(12)。这是源8714–8728、8774–8790的有限代数操作在新长度下的重放 [R]，不允许把(12)另定义为物理I的替代品。基础probe/finite-compensation算术身份仍是外部输入；本文未重新认证整篇算术来源。

## 5. 主槽误差指数及实际normalizer

原 old-eq:5.13b，8808–8816，给p∤u的准确抵消式。对物理主行u=1，identity-ray selected prime有χ_p(1)=1；目标η(p)仍可为任意单位相位。由原表、(4)和有界分母，其归一化错误的四个幂为

\[
 -x_r,\qquad -6z_r,\qquad
 4-5x_r-6z_r,\qquad 1-w_r-6z_r.
 \tag{16}
\]

在D2*中这四个最大值准确为

\[
 -\frac{69999}{80000},\quad -\frac{99}{100},
 \quad-\frac{21839}{16000},\quad-\frac{47}{50}.
 \tag{17}
\]

其中最弱的正衰减是σ1。因|H_p|≥1/2，主行的合法乘子B_p=G_p/H_p满足

\[
 \boxed{B_p=-1+O(Q^{-\sigma_1})\quad\hbox{在整个 }D_2^*.}
 \tag{18}
\]

原−7/8不能直接保留：第一错误项仅给Q^(−x_r)，x_r可能落在(σ1,7/8)。一般扩域σ>401/600时可用
min{σ,99/100,5σ−301/100,47/50}作为正指数；恰好在σ=σ1它等于σ1。

由(18)及正unselected乘积，G_p=O(1)的主行tuple界为

\[
 |\mathfrak H_{\eta,1,Z}(s,w,z)|
 \ll Z^{\ell_1\Re z}
 \quad \hbox{在 principal box 内，所有高度统一}.
 \tag{19}
\]

这支付源 eq:principal-correction-bound，6185–6189。不用逐点限定高度，不把期望消去当作绝对上界。

固定ray素数渐近 [R]，源15563–15592，仍给

\[
 S_i(Z)=\sum_{p\in\mathcal P_i(Z)}W_i(q_p/P_i)q_p^{-5/6}
 \sim c_i\frac{P_i^{1/6}}{\log P_i},\quad c_i>0,
 \quad
 A_T(Z)=(-1)^K Z^{-\ell_1/6}\prod_iS_i(Z).
 \tag{20}
\]

所有ℓ_i固定且为正，所以A_T最终非零，|A_T|∼(log Z)^−K，逆为任意小幂。该渐近允许阈值依赖目标有限S，不要求在moving conductor上一致。

在w=1,z=1/6，逐槽应用(18)和W_i≥0，得到ρ_i=O(P_i^−σ1)。因此选择任意

\[
 0<\mu<\sigma_1\min_i\ell_i
 \tag{21}
\]

即可得同一源的实际余留数比较

\[
 \mathfrak H_{\eta,1,Z}(s,1,1/6)
 =H_\eta(s)Z^{\ell_1/6}A_T(Z)
      (1+\mathcal R_{\eta,Z}(s)),\qquad
 |\mathcal R_{\eta,Z}(s)|\ll Z^{-\mu},
 \quad \Re s=\beta_*+e.
 \tag{22}
\]

K固定，误差只来自有限个(1+ρ_i)的乘积。μ在目标前指定，不能在Z之后选择。源15619的旧(7/8)minℓ_i必须改为(21)。

## 6. 主留数轮廓及三种误差

重放源 lem:principal-residue-interface，6224–6301：

1. 在global s=β_*+e上，把w,z分别移至1+e、1/6+e。再移w至19/20，跨w=1；在其留数中移z至33/200=1/6−1/600，跨z=1/6。
2. 所有路径处于D2*；w/z标量极点只按原方式取留数。1/L始终global，不额外跨越目标零点。
3. 对水平joins和原维数/取留数后二维核，使用固定B,J的外部尾引理，不以某条轴上的估计替代其他轴的控制。
4. 只将主留数积分右移到s=2，使用同一Hη的全纯与global reciprocal；余误差在原global线上估计，不能混入主信号。

原raw Mellin幂为l_x/2+s−1+h z+l_y(w−1)，所以改几何不改变计算。仍得源6214–6216形状：

\[
 \frac{\mathscr P_\eta(Z)}{c_SA_T(Z)}-f_\eta(Z)
 \ll
 Z^{C(\beta_*)+(1+h)e-m_w+\epsilon}
 +Z^{C(\beta_*)+e-m_z+\epsilon}
 +Z^{C(\beta_*)+e-\mu+\epsilon},
 \tag{23}
\]

\[
 m_w=\frac{l_y}{20}=\frac{57497}{2400000}>0,\qquad
 m_z=\frac h{600}=\frac{32503}{24000000}>0.
 \tag{24}
\]

e和其余实损失可在目标前选小，使三项保留固定负余量；这是一项必须检查的独立数值条件，不是单凭扩域就自动没有误差。

c_S的正性仍是原5521–5543的非负测试和ζ_F^S正留数；取同一S、同一A_T作为low与high两边normalizer，不能另换一个较易非零的标量。

## 7. retained fixed-bin轮廓与中央记账

源buffered bins本来就在a∈[51/100,1]给定，a≤β_*。固定bin及有限物理row集合后，先沿D1把z移到17/50、s移到β_*+20e，再把w移到1−a−6e：

\[
 \Re(s+w)\ge1+(\beta_*-a)+14e\ge1+14e.
 \tag{25}
\]

取ε0=10e；w≥−6e>−1/100，z=17/50。在global s线上先剔除原高度box外部尾；随后只把retained s段移到a+16e，

\[
 \Re(s+w)\ge1+10e,\qquad
 \Re s\ge a+16e>a+6e.
 \tag{26}
\]

buffered reciprocal界适用于后一步和s-joins；其高度原box参数≤1/2，原论证没有出现σ0的7/8下界。标量ζ的z始终>1/6；非主numerator为entire。由§4全高度majorant及外尾lemma，discarded部分和joins仍为
O_{\eta,N}(Z^{B_\eta}T_1^−N)，Bη在N之前固定。

这逐前件支付了新σ0=σ1版本的lem:fixed-bin-contour。不得先把bin按contour-dependent detector数据切开再各自移动；原whole-bin轮廓必须先完成。

源bin-contour-accounting的记账恒等式6142–6152相应原样成立：

\[
 E_{\sigma_1}(d;R,g)
 =a-\sigma_1+h(z_0-1/6)-a l_y
       -\ell_1/2+g+d(R+\delta/2-z_0).
 \tag{27}
\]

其附加real损失仍为(16−6l_y)e+(1+d)ε_c+dε_d+ε_p，以及固定height成本(1+T1)^Aη。式(27)并不给出R、g的实际新上界；那些仍需同源error-slot、inverse/fourth moment及detector capacity来支付。仅用439的名义R_*代入(27)不能替代这些前件。

## 8. 原外行：新的D1选择与精确小行余量

原outer-row-tails及absolute-local-tuple-bounds在小行选

\[
 (x_r,w_r,z_r)=(\beta_*+e,\ 1/2,\ 17/50).
 \tag{28}
\]

旧证明6418–6419、9134使用D1(3/8)。如果β_*只略大于σ1，该条件确实不再有保障。固定改用

\[
 \boxed{D_1(1/3),\qquad
 \sigma_1+\frac12>1+\frac13.}
 \tag{29}
\]

其余域条件都保留；ε_H=min(1/3,1/50)=1/50。此选择在目标前固定，非从待证零区推出；轮廓路径先移z再降s/w可留在该域。

### 8.1 小行完整selected因子

off-row p∤u的局部错误四指数变为

\[
 -x_r,\quad-\frac{51}{25},\quad
 \frac{49}{25}-5x_r,\quad-\frac{77}{50},
 \tag{30}
\]

在x_r≥σ1全部负，H_p有界，故G_p=O(1)，无需除以H_p。

ramified p|u必须保留D=W=0。把原J_j表乘Q^x后，边界指数为

\[
 -\frac12,\quad\frac32-2x_r,\quad
 \left(\frac32-2x_r,\ 2-3x_r\right),\quad
 2-3x_r,\quad 3-5x_r.
 \tag{31}
\]

只要x_r≥1/2，这些均≤1/2；原strict项为1−w_r=1/2，共同R项49/25−5x_r更小。几何族比
|R|=Q^(4−6x_r−6z_r)、|V|=Q^−51/25在当前域严格<1，常数对全部高度一致。因此G_p≪Q^1/2，包括H_p零点。

每槽ramified素数divisor-many，源9175–9179的正和仍是

\[
 \sum_{p\in\mathcal P_i(Z)}
 |W_i(q_p/P_i)|q_p^{z_r-1}|G_p|
 \ll P_i^{z_r}+U^\epsilon P_i^{z_r-1/2}
 \ll U^\epsilon P_i^{z_r}.
 \tag{32}
\]

结合unselected正乘积并在固定K槽间分配ε，得到完整tuple界
\(|\mathfrak H|\ll U^\epsilon Z^{17\ell_1/50}\)，所有高度统一。这是原小行lemma证明的新版本；不能直接引用它限定β_*>7/8的旧statement。

### 8.2 小行sum的精确saving

nonprincipal numerator的固定宽条带增长仍为源 eq:hecke-growth，1425–1433 的U^(3/5+ε)乘固定height多项式；w=1/2没有改动。行数O(U)、q_u^−z0及该增长给总行幂

\[
 1+\frac35-\frac{17}{50}=\frac{63}{50}.
 \tag{33}
\]

源eq:small-row-sum，6371–6373，相对C(β_*)的误差自由指数为

\[
 h\left(\frac{17}{50}-\frac16\right)-\frac{l_y}{2}
       +\frac{63}{50}d_{\min}.
 \tag{34}
\]

沿用Part II sec:tails，15855 的d_min=1/100。新几何准确给

\[
 h\frac{13}{75}-\frac{l_y}{2}
 =-\frac{79}{800}+\frac{51}{2000000}
 =-\frac{197449}{2000000},
 \tag{35}
\]

\[
 \boxed{\text{精确小行指数}
 =-\frac{172249}{2000000}<0.}
 \tag{36}
\]

若沿用源15880–15889的较粗63/50<2，

\[
 \boxed{\text{粗小行指数}
 =-\frac{157449}{2000000}<0.}
 \tag{37}
\]

两式还须加原e+ε及有限额外real损失，然后选它们足够小。原中间行49/14400余量从未覆盖d<d_min；本文(36)(37)单独支付外小行。

若另用bootstrap β_*≤7/8，把(36)的尾界换到C(σ1)参考幂，最多加β_*−σ1≤1/80000；误差自由saving仍至少172224/2000000。这个换参考幂只是可用的进一步余量，不是小行证明所需的假设。

### 8.3 大行与外部高度阶数

大行保留(s,w,z)=(2,2,z∞)，z∞>2固定。源9185–9195每个selected G_p=O(1)，tuple正和为O(U^εZ^(ℓ1 z∞))，对所有rows与高度一致。由原outer-row-tails，6386–6396，

\[
 B_0=l_x/2+1+l_y=\frac{53}{32}-\frac{3}{4}\frac1{20000}
 =\frac{264994}{160000},
 \tag{38}
\]

\[
 \sum_{U>Z^{h+\zeta}}|\mathscr R_\eta(U;Z)|
 \ll Z^{B_0+(h+\zeta)(1+\epsilon)-\zeta z_\infty+\epsilon}.
 \tag{39}
\]

任意固定ζ>0后可在目标前选足够大的z∞，使(39)达到所需负幂，再选ε、height order及尾阶数。没有额外7/8数值障碍；不能让z∞随着Z或目标改变。完整绝对tuple bound支付最终估计，absolute路径中的暂时每dyad常数只用于证明等式，不能污染最终sum的统一常数。

外部尾引理5672–5728本身仅是positive kernel积分。它要求B,J先固定，随后选测试衰减阶L>N+J+m；不允许以改N来改善一个依赖N的算术B或J。源fixed-bin和principal proof中三维/二维核的real参数留在固定紧box，z_r始终在(0,∞)，所以原测试衰减和coordinate trace-tails都可保留。

## 9. 本文支付和仍待支付的范围

本文给出的具体新接口是：

- 同一基础Euler correction的D2*全纯、positive-product bound及主信号nonvanishing。
- 同一无商有限tuple correction的全纯与固定B′、J=0全高度majorant；保留同源有限操作，不另造high object。
- principal局部B_p的正确指数σ1、实际固定slot normalizer以及μ>0的余留数比较。
- 同样的fixed-bin轮廓和中央Mellin记账在σ1下的重放。
- 原物理外小行的精确saving和大行的uniform absolute控制。

以上仅条件于逐一指明的外部算术/基础probe/固定ray渐近 [R]，没有增加待证新无零假设。441另行支付的low估计不在本文重证。

以下仍不由本文完成：

1. 中央error-slot与numerator联合估计在新几何的全部实际前件和所有层级label范围。
2. inverse、fourth-moment、recursive detector capacity与新retained row counts；原外部bootstrap给δ≤3/4本身不代替这些定理。
3. 实际R,g来自这些同源计数后，central E最大值的uniform严格saving及从d≈h到h+ζ的统一扩展。
4. 原order-of-choices与continuation的整套新版本，包括有限多个real损失、target-dependent height powers及所有尾界共同兼容。

442若采用本报告，可明确引用上面已支付的局部解析、principal和外行接口；完整high asymptotic comparison、capacity及新无零定理仍须独立闭合。本文不宣称Lean/RH证明。

## 10. 复核方式与限制

全部源引理、实际证明及相关full tuple定义按固定paper.tex读取；式(1)–(39)以显示的无限乘积、局部表达式和轮廓论证为依据。h、l_y、小行(36)(37)与principal四指数由另一个代理独立Fraction核验一致。该有限有理核验只核数值，不替代正常收敛、all-height或whole-bin轮廓论证。没有运行数学仓库构建、改动源稿/当前notes/索引或声称外部Lean验收。
