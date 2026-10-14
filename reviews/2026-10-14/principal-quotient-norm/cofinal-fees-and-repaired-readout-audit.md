# Principal quotient：成长紧支窗读出费用与合法修复逆审

2026-10-14；独立来源/范围审查，非新合同或数学轮。
仅消费 actual source quotient；已知零点读出不是独立正性输入。

## 1. 恢复、对象与最强旧扣除

按 AGENTS 恢复 README、STATE、check/show、同 G20261014 Goal、frontier、C021 stopped、
D20261014AA 和唯一 next-principal-quotient-norm gate。
check 仅结构通过；cadence 仍 1/8。现场 HEAD 为
`1d48bd538cd176091dbec90eeca46253a1473d70`；恢复时 `.gitattributes`、STATE 有其他代理编辑。
本代理未改公共状态、cadence、合同或 Git。子代理 get_goal 返回 null，不能替代 root 的 active 观察。

必要原件：405 §§2–6，519 §§1–5，520 §§3–5，523 §§2–6，526 §§1–7，
543 §§1–2。旧结果准确给：

* (F=\mathcal S_{\exp,\mathbb C})，(I=E\mathscr S_{e,0,\mathbb C})
  恰为所有 actual ζ 零点的完整必要 jets 消失空间，且在 F 中闭。
* (P_{\rm an}=I\cap\ker M(0)\cap\ker M(1))。
  405 的 (p=(D^2+D)h\ne0) 属于这一真实关系空间。
* 523 已证单线物理 L²/固定阶 Sobolev 完成中 I 稠密，非零 ζ 求值不能连续延拓。
  把 h 换成已有 p 的 translate-cyclic 论证，或由 H¹ 密度降到 Hlog，均为旧直接后果。
* 520/522 已把中心化平移的统一次指数责任接到实际零点实部；它不是已付算术估计。
* 526 已给保留全部 ζ-jets 的忠实双端权 Hilbert 商，及其准确指数费用和自然内积缺陷。
  因此“任何忠实非零读出不存在”是错误停止理由。

本稿补的是具体读出在 cofinal 紧支窗上的必要/充分费用与修复范围，不再次计旧闭包或谱实现。

冻结真实物理坐标

\[
 r(u)=e^{u/2}f(u),\qquad
 \ell_{\rho,j}(r)=M_f^{(j)}(\rho)
       =\int u^j e^{(\rho-1/2)u}r(u)\,du.                    \tag{1}
\]

写 α=Reρ−1/2、γ=Imρ，(I_L=(-L,L))，L>0。
源空间取全部 complex (C_c^\infty(I_L))，并在需要时延到原零延拓 Dlog 域；不只测试一个 probe。
全线 Fourier 为 (\widehat r(t)=\int r(u)e^{-itu}du)，原 L² 范数为 ∫|r|²du。
采用等价但明确的 positive graph norm

\[
 \|r\|_{H_{\log}}^2={1\over2\pi}\int W(t)|\widehat r(t)|^2dt,
 \qquad W(t)=1+\log(2+|t|).                                \tag{2}
\]

543 的 actual Φ=Γ−Γ(0) 和 (2) 的图范数等价，常数绝对且不依 L、ρ 或源。
所以本稿没有把 Γ 改成另一个 operator：费用在 ∥r∥²+JΓ(r) 上同阶。

## 2. 原 L²：ALL compact sources 的精确费用，含全部 jets 和双 poles

Riesz 核在 I_L 上恰为 (u^je^{(\bar\rho-1/2)u})。故

\[
 \boxed{\ \|\ell_{\rho,j}\|_{L^2(I_L)^*}^2
        =\int_{-L}^L u^{2j}e^{2\alpha u}du.\ }             \tag{3}
\]

这是必要且充分的 operatornorm，而非一个上界：截断 Riesz 核可由
I_L 内的光滑紧支函数在 L² 中逼近，故同一个 supremum 在原 smooth 测试类上成立。
对 j=0，

\[
 \|\ell_{\rho,0}\|^2=
 \begin{cases}2L,&\alpha=0,\\
 \sinh(2|\alpha|L)/|\alpha|,&\alpha\ne0.
 \end{cases}                                               \tag{4}
\]

对任意固定非负整数 j，critical 情况准确为

\[
 \|\ell_{\rho,j}\|^2={2L^{2j+1}\over2j+1}.                 \tag{5}
\]

对每个先固定 α≠0、j，L→∞ 时

\[
 \|\ell_{\rho,j}\|^2\sim {L^{2j}e^{2|\alpha|L}\over2|\alpha|}.
                                                               \tag{6}
\]

这里没有声称 (6) 对 α=α(L)→0 一致；这种情况用精确 (3)。
全部必要 multiplicity jets 是 (0\le j<m_\rho)，不能只保 j=0 后宣称忠实保留原商。

Pole reads 是 s=1、0，亦即 α=±1/2、γ=0；二者 norm² 都为 (2\sinh L)。
完整 signed pole form 是

\[
 \mathcal P_L(r)=2\Re[A_+(r)\overline{A_-(r)}],\qquad
 A_\pm(r)=\int_{I_L}e^{\pm u/2}r(u)du.                    \tag{7}
\]

其两个非零特征值准确是 (2L+2\sinh L) 与 (2L-2\sinh L)：
两核的 squared norms 为 a=2sinh L，交积为 b=2L，特征向量为两核的和/差。
因此 signed operatornorm 为 (2L+2\sinh L\asymp e^L)。
不能分别估 raw norms 后丢掉负方向，也不能把它当作两个独立的正费用。
在 (A_+=A_-=0) 的子域，(7) 正好为零。

关系角色必须分开：ζ 的必要 jets 消去完整 I；A± 只消去 P_an，
不消去完整 I（405 的 h 两矩均 1/4）。商 F/P_an 保留两个次数方向，商 F/I 则不保它们。

## 3. Hlog critical：uniform ALL γ、cofinal L 的 sharp order

对每个固定 j≥0，有常数 (0<c_j\le C_j<\infty)，使 ALL γ∈R、L≥1

\[
 \boxed{\quad
 c_j{L^{2j+1}\over W(\gamma)}
 \le\|\ell_{1/2+i\gamma,j}\|_{H_{\log}(I_L)^*}^2
 \le C_j{L^{2j+1}\over W(\gamma)}.\quad}                  \tag{8}
\]

Hlog(I_L) 在这里是全线零延拓的原图范数，不是 periodic/regional norm。
上界对整个原 Dlog 源域成立；下界由合法 smooth compact sources 给出。

**上界，支付 hard-window/sinc endpoints。**
令 (k_j(u)=u^je^{-i\gamma u}1_{I_L}(u))，并令

\[
 K_j(s)=\int_{-L}^L u^je^{-isu}du.
\]

L² Plancherel 与一次分部积分给

\[
 |K_j(s)|\le C_j L^{j+1},\qquad
 |K_j(s)|\le4L^j/|s|\ (s\ne0),\qquad
 {1\over2\pi}\int|K_j(s)|^2ds={2L^{2j+1}\over2j+1}.        \tag{9}
\]

j=0 可用更小常数2。边界值已计入第二式；没有假设 hard cutoff 导数为 L²。
对任意支在 I_L 的 r，weighted Fourier Cauchy–Schwarz 合法给

\[
 |\ell_{\rho,j}(r)|^2
 \le\|r\|_{H_{\log}}^2\,{1\over2\pi}
       \int {|K_j(t+\gamma)|^2\over W(t)}dt.               \tag{10}
\]

(10) 是全线 dual extension 的上界，不误称其为 restricted-domain 的精确 Riesz norm。
若 |γ|≤4，用 W≥1 与 (9)，即得 (8) 上界。
若 |γ|>4，分 (|t+\gamma|\le|\gamma|/2) 与补集。
第一部分 W(t)≥cW(γ)，由 (9) 付 (C_jL^{2j+1}/W(\gamma))。
第二部分由 (9) tail 付 (C_jL^{2j}/|\gamma|)，
因 L≥1 且 W(γ)/|γ| 有界，也不超过所需上界。
这一步保留所有 γ/L 相对尺度，未先固定 γ 后声称一致。

**下界。** 固定非零、非负、偶 (\chi\in C_c^\infty(-1,1))，令

\[
 g_{L,\gamma,j}(u)=e^{-i\gamma u}(u/L)^j\chi(u/L).
\]

设 (a_j=\int v^{2j}\chi(v)dv>0)，则

\[
 \ell_{1/2+i\gamma,j}(g)=L^{j+1}a_j.
\]

令 ψ_j(v)=v^jχ(v)。Fourier 缩放给

\[
 \|g\|_{H_{\log}}^2
 ={L\over2\pi}\int W(s/L-\gamma)|\widehat\psi_j(s)|^2ds
 \le C_j L W(\gamma).                                    \tag{11}
\]

最后一步用 L≥1、

\[
 W(s/L-\gamma)\le W(\gamma)+\log(1+|s|)
\]

及 ψ_j 的 rapid Fourier 衰减。两式相除给 (8) 下界。
源频率、窗长和零点高度都进入原 (2)；没有免费忽略调制的 Γ 价格。

**同时保双 pole 零。** 可把 g 换成

\[
 r=(D^2-1/4)g.
\]

所有边界项为零，所以 A±(r)=0，且 κ=iγ 时

\[
 \ell_{\rho,j}(r)
 =(\kappa^2-1/4)\ell_{\rho,j}(g)
  +2j\kappa\ell_{\rho,j-1}(g)
  +j(j-1)\ell_{\rho,j-2}(g).                              \tag{12}
\]

负下标项按零处理。
χ 偶使 j−1 项准确为零。主项是 (-(\gamma^2+1/4)L^{j+1}a_j)，
j−2 项仅为 (j(j-1)L^{j-1}\int v^{2j-2}\chi(v)dv)。
因此存在只依 j、χ 的 (L_j\ge1)，使 ALL γ、L≥L_j 的主项至少保留一半。
同 (11) 应用于 g 的前两阶导数，得

\[
 \|r\|_{H_{\log}}^2\le C_j(1+\gamma^2)^2 L W(\gamma).
\]

因 ((\gamma^2+1/4)/(1+\gamma^2)\ge1/4)，相除仍给 (8) 下界。
所以 critical cofinal 费用并非 pole 方向假象；双矩零子域也有同阶费用。
此处准确是 L≥L_j，不声称每个小 L 的这一固定 probe 都不会发生 (12) 中的抵消。

## 4. Offcritical：允许 cofinal 非uniform费的真实逃逸

对每个先固定 actual ρ、α≠0 和 j≥0，存在正有限常数，使 L 充分大时

\[
 \|\ell_{\rho,j}\|_{H_{\log}(I_L)^*}^2
       \asymp_{\rho,j} L^{2j}e^{2|\alpha|L}.               \tag{13}
\]

上界由 ∥r∥_Hlog≥∥r∥_L² 与精确 (3)、(6) 即得。
下界甚至在双 pole 零的 compact 子域成立：
取 χ∈Cc∞(-A,A)，使 (ell_{\rho,0}(\chi)\ne0)。
例如取 (\chi(u)=e^{-i\gamma u}\chi_0(u))，χ0 为非负非零实 bump。
令 (psi=(D^2-1/4)\chi)，则

\[
 A_\pm(\psi)=0,\qquad
 \ell_{\rho,0}(\psi)=\rho(\rho-1)\ell_{\rho,0}(\chi)\ne0.  \tag{14}
\]

非平凡 ζ 零点不是0或1；(14) 没有借未知位置。
全线 Hlog 平移是等距。对 a 取 sign(α)(L−A−1)，L>A+1，有

\[
 \ell_{\rho,j}(\tau_a\psi)
 =e^{(\rho-1/2)a}
   \sum_{k=0}^j{j\choose k}a^{j-k}\ell_{\rho,k}(\psi).     \tag{15}
\]

该 polynomial 的 leading coefficient 是 (14) 的非零数，故 squared ratio
至少为 (c_{\rho,j}L^{2j}e^{2|\alpha|L})。
源支在 I_L，双 moments 随平移仍为零，且原 norm 不变；这完成必要费用。
该 argument 对 complex 全源合法；需要实源时，固定复 probe 的实/虚两部分中至少一个保有非零值。

对 poles s=0、1 同样 argument 给 Hlog squared readout fee ≍ e^L；
此时不能用 (14)，因为乘子 s(s−1) 正好为零，且 pole-free 子域的 poles 读出本来就是零。

若一个拟议 principal-compatible map 的输出能以固定正比例读出某 actual ζρ 坐标，
它的 cofinal squared physical operator fee 必须至少支付 (13) 或 (8)。
固定非零 α 时，任意全源 (e^{o(L)}) squared fee 都不够；若不预知 α，
独立证明所有 actual readouts 的这种次指数费会排 offcritical。
这准确是旧520/522增长责任的另一表达，不能把待证费定义成新算术输入。
临界 j=0 的 L/W(γ)、高阶 jets 的 L^(2j+1)/W(γ) 与次指数费相容，亦不自行证明RH或简单性。

## 5. 全高度/联合坐标：单个费用不能免费合成

每个必要 jet (1) 在 F 中连续：对 B>|α|，

\[
 |\ell_{\rho,j}(r)|\le p_{B,0}(r)
                   \int |u|^j e^{-(B-|\alpha|)|u|}du.      \tag{16}
\]

它消去 I，且由 compact probes 非零，因此是实际非零商坐标。
在实际零点集合上使用 (0\le j<m_\rho) 的全部这些坐标共同分离 F/I，
正是519；这不声称原商拓扑等于一个无约束 sequence Hilbert 空间。

为防止单坐标费被升级：对任意有限坐标集合 ᴀ、正权 ω_a，
在 L²(I_L) 上 (r\mapsto(\sqrt{\omega_a}\ell_a(r))_{a\in\mathsf A})
的 squared operatornorm 精确为下列 Gram 的最大特征值：

\[
 G_{ab}(L)=\sqrt{\omega_a\omega_b}
   \int_{-L}^L u^{j_a+j_b}
           e^{(\bar\rho_a+\rho_b-1)u}du.                  \tag{17}
\]

这是所有 source directions 的 exact necessary/sufficient test，保留共轭与跨坐标交项。
例如 (\max_a G_{aa}\le\lambda_{\max}G\le\sum_aG_{aa})；trace 上界不是必要 joint fee。
无限集合的 weighted ℓ² readout 在同一窗有界，当且仅当所有有限子集的
(17) operatornorm 有同一个有限上界。此处没有证明那个 fullheight bound。
Hlog 上也必须核相应 restricted-domain Riesz Gram；(10) 的 wholeline kernels
给联合 upper certificate，不能把它当成精确 restricted Gram，也不能以所有对角有限代联合有界。

下列逃逸确实非空：选实际 finite ζ 坐标的 |ℓ|²，或对全部 necessary jets
选择充分小正权，使 (16) 的半范数上界平方可求和，得到 F 上连续的非零 PSD 读出。
例如对 countable 坐标 a，因 actual 0<Reρ<1，可统一取 B=1；
设 (b_a=\int |u|^{j_a}e^{-|u|/2}du<\infty)，取

\[
 \omega_a={2^{-a}\over1+b_a^2}.
\]

则 ∑ω_a|ℓ_a(r)|²≤p_(1,0)(r)²；所有权正时保留全部 quotient jets。
这个同一个 fullheight readout 在每个 compact window 上也可直接付费，
并非仅逐坐标声明。因为 (b_a=2^{j_a+2}j_a!)、
\(|\alpha_a|<1/2\)，(3) 给

\[
 \sum_a\omega_a\|\ell_a\|_{L^2(I_L)^*}^2
 \le {L e^L\over8}\sup_{j\ge0}{(L/2)^{2j}\over(j!)^2}
 \le {L\over8}e^{2L}.                                    \tag{17a}
\]

最后一步由该非负项的和不超过
\((\sum_j(L/2)^j/j!)^2=e^L\)；∑_a2^(-a)≤1。
因此 (17a) 对 ALL compact L² 源、全部 actual heights 和全部必要 multiplicity jets 成立，
在 Hlog 上亦为充分费。再加 |A+|²+|A−|²，得 F/P_an 的忠实 positive readout，
其 compact squared operator fee 上界为 (Le^{2L}/8+4\sinh L)。
这是完整的 nonuniform cofinal 逃逸；任意枚举和人为权并不提供 fullWeil 的自然系数方向。
它只是在已知实际谱坐标上选择了一个很弱的正完成，常数/高度权任意，
没有独立算术对应或实际完整 Weil 型的识别。
若只取 zero values，重零点的额外 jets 会消失；519/516 已区分这比完整商多出的 radical。

还必须扣更强的旧526 whole-quotient 对照：取 δ=1/2，物理源 norm 是
\(\int2\cosh u\,|r(u)|^2du\)。其忠实商范数准确满足

\[
 q_{1/2}([f])^2\le\int2\cosh u\,|r|^2du
                \le2\cosh L\,\|r\|_{L^2(I_L)}^2.         \tag{17b}
\]

这保全部 actual heights/jets；不把一个 source upper bound 的等号传给商。
对 F/P_an，可使用同一个全源映射
\(r\mapsto(A_+(r),A_-(r),[e^{-u/2}r]_{Y_{1/2}})\)。
它在 F 连续、kernel 正好为 P_an，compact squared physical fee 不超过
\(2\cosh L+4\sinh L=O(e^L)\)。
所以允许 nonuniform cofinal 费用后，合法 fullsource/fulljet/双次数 escape
已经由最强旧资产提供；本稿 (17a) 的 raw-coordinate upper 不是新的净费用改进。
该 positive 目标范数仍不是 actual full Q，且旧526的自然内积/成长缺陷保持。

完整 Q 的实际方向也不能混同这个人为 PSD sum：实源时

\[
 Q(r)=-2B(f,f)+2d(f)c(f)
     =\sum_\rho m_\rho M_f(\rho)M_f(1-\rho).              \tag{18}
\]

Hermitian 极化保留 (\overline{M_g(1-\bar\rho)})；只有先证critical等实质前件后
才能把全部项解释成正 squared values。归一化、全部 multiplicities、poles 及 Γ/pp
的同源误差不能被 (16)/(17) 或一项 |ℓ|² 替代。

## 6. Closure 的修复范围：global physical boundedness 并非全部几何

F 中闭、physical L²/Hlog 中稠密并不矛盾；是两个拓扑。
原 Mellin coordinates 是 concrete nonlocal、source-defined、principal-compatible 的合法例子，
在 F 连续，在每个紧支窗有界，在全线 physical norm 无连续延拓。
对全线 Hlog，(8)/(13) 的 L→∞ 下界亦直接证明其无界；不只是抽象 closure 障碍。

紧支源与关系不可静默换域。实际上

\[
 I\cap C_c^\infty(\mathbb R)=\{0\}.                     \tag{19}
\]

证明：非零 compact f 的 Mellin entire function 有有限 exponential type；
取 M_f(s0)≠0，Jensen 在半径2R圆盘配合
log|M_f(s)|≤L|Re s|+log∥f∥_L¹，给半径R零点数 O_f,L(R)。
若 f∈I，则它消去所有实际非平凡 ζ 零点，而标准实际零点计数为 ≍ RlogR，矛盾。
没有使用RH，重数只加强矛盾；这也是519的直接范围后果。
故“在 compact window 上消去 compact principal relations”本身甚至是空条件，
不能据此声称已核全部真实 noncompact principal 关系。

将真实 principal g 截成 χ_Lg 通常失去 exact ζ-jets 消失。
固定 g∈F 的尾在 (16) 中可定量支付：对 B>|α|，

\[
 |\ell_{\rho,j}((1-\chi_L)g)|
 \le C_{B,\rho,j}p_{B,0}(g)(1+L)^j e^{-(B-|\alpha|)L},   \tag{20}
\]

这里 χ_L 在 [-L,L] 为1，外侧截止在固定比例更大区间。
所有平移/逼近源的一致控制不能从 fixed-g (20) 免费得到：

\[
 p_{B,0}(\tau_ag)\le e^{B|a|}p_{B,0}(g).
\]

source-adapted/cofinal family 因而可让 physical-small error 带着 large readout constants；
这正是密度不支付 quotient growth 的原因。

对拟议几何修复，准确结论如下。

| 允许的类 | closure 实际能排什么；剩余费用 |
|---|---|
| 一个 fixed global linear (T:F_r\to\mathcal K)，目标为 Hilbert/mod-base energy completion，∥Tr∥≤K∥r∥_Hlog，消去全部 P_an | centered principal 平移稠密迫使 T=0，不能同时在非根 f0 上有非零 class。须作用于 class，不能把 raw Green 非零当 class 非零 |
| cofinal T_L 或同一 T 的 compact restrictions | 只要 K_L 非uniform，即不被 global argument 排除；实际 (1) 已构造逃逸，费用按 (3)/(8)/(13)，joint/fullheight 再付 |
| source/place/height 依赖的输出和范数 | 每个坐标/输出的固定 uniform bound 若满足以上条件仍零；若常数随源/place/height变化则该推论不成立。需另给兼容的共同 target、范数、极限和全部源量词 |
| different 双端权或 F 拓扑 | 526 现成忠实逃逸，保全部必要 jets；中心化原权群费 e^(δ|a|)，商只是相应 upper bound，不能传成 exact quotient fee。旧自然内积不等于 full Weil |
| nonlinear readout | 若真正对 principal cosets 不变、且在同一个 global physical Hilbert 拓扑连续，密度使它常值；若仅每个 generator 的某 raw值零、只 F-continuous、或 T_L/domain 变化，则不能套该结论 |
| PSD quadratic energy/seminorm quotient | 如果全源 energy≤K²∥r∥_Hlog² 且 principal energy零，PSD Cauchy–Schwarz使 principal 为 radical，closed nullspace稠密故energy全零。F-continuous而physical-unbounded的|ℓ|²合法非零；必须证明它与实际full Q/几何能量的比较，不能按Q反造 |

principal pair 必须整体消费。真实几何的 “(div f,−log|f|²)” 即使 Green 非零，
仍可能在 arithmetic principal 商中为零；本稿只测试降到实际 mod-base energy class 后的映射。
不强求 Green 函数本身零，不以 rawmetric 式子替代该 class 的范数。
nonlocality 本身也不解或不破 closure：决定因素是准确 domain/topology、principal 消去及共同 norm fee。

## 7. 消费收据与止损判断

已付：actual complete ζ-jet readout 的 full compact-source L² 精确费；
Hlog critical ALL γ/cofinal L sharp order，offcritical 固定ρ/j的指数必要/充分费；
双 pole 零 probes、signed fullpole 特征值；finite/full coordinate联合门；
cofinal/source/domain/nonlinear/PSD quotient 修复范围。
这些是旧519/520/523/526输入的显式定量后果，不是新独立 ζ 算术正性。

未付：不依未知零点位置的 source-defined geometric readout/对应、
同 actual full Q 的 principal-compatible comparison、共同 allheight/multiplicity norm费、
Γ/全部 pp/双poles 的同源 signed comparison和成长净 core 后果。
不能以个别 ℓ、有限 PSD coordinate 或 faithful quotient 本身补齐这些责任。

本门准确停止于来源/范围恢复0：允许 nonuniform cofinal fee 后 closure 不给新的 whole-object 排除。
它纠正 “physical bounded失败⇒全部quotient/几何失败”，但不削弱宏观的未付核心箭头。
若未来来源给独立 allsource/cofinal 费用，先对照 (8)/(13)/(17)、全部jets及最强旧520/522/526，
再核 fullWeil/coupling 和严格净后果；没有这些输入不建 C022、不重开 C021，不消费 cadence。
