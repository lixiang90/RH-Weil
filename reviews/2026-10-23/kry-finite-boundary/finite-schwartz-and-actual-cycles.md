# Split finite Schwartz 的实际循环、完整边界与全 Pan 通道门

2026-10-23；独立分支，供 root 核读，不改 STATE／cadence。接续 [579](../../../notes/579-kry-physical-gaussian-source-and-native-primitive-obstruction.md)。固定 KRY1999 的 q=7、实际 Gaussian／加法字符／自对偶 Haar，不读取完整 Q 或零点作标签。本文的 positive-n cycles、负指标 arch divisor 及 constant 的身份分开；没有构造相对 primitive 的正二次配对。

## 1. 原件消费范围与一个实际有限位公式

唯一外部原件为 [Kudla–Rapoport–Yang1999作者版](https://www.math.uni-bonn.de/people/rapoport/myalggeom/preprints/tinynew.pdf)：§1(1.4)–(1.6) 的 Schwartz／standard section；§2 的 native Whittaker、完整常数项；§5 的 special-endomorphism cycles 及 Theorem5.11 的厚度；§6(6.16) 的负指标 arch divisor。§6 对任意有限 Schwartz 的循环推广仅作变体规划，本文不把它当成已证明的 general-cycle theorem。以下 split 的精确特例由局部积分及既有 cycles 直接闭合。

在 split p=2，\(k_2=\mathbb Q_2\oplus\mathbb Q_2\)，实际 lattice 为 \(L_2=\mathbb Z_2^2\)，其自对偶 Haar 体积为1。对 j≥0 令

\[
 \psi_j=\mathbf1_{2^jL_2}\otimes\bigotimes_{\ell\ne2,\infty}
                  \mathbf1_{O_{k,\ell}},\qquad
 \varphi_j=\varphi_*\otimes\psi_j .                    \tag{1}
\]

注意只有2处改变。局部 Weil 公式为

\[
 \omega_2(m(2^{-j}))\mathbf1_{L_2}=2^j\mathbf1_{2^jL_2}.
                                                               \tag{2}
\]

split 的 χ₂(2)=1，无额外 character 符号；(2) 的2^j不可省。令 Φ_j(s) 为 \(\lambda(\varphi_j)\) 的**标准**延拓，采用原件同一个全局归一化，定义

\[
 \phi_j(\tau)=-v^{-1/2}\left.\partial_s
 E^*(g_\tau,s,\Phi_j)\right|_{s=0}.
\]

以下局部计算给出完整而非仅正系数的身份

\[
 \boxed{\phi_j(\tau)=\phi_0(2^{2j}\tau).}               \tag{3}
\]

此处没有把 \(\lambda\) 的 s=0 等变性误当 standard 延拓导数等变性。(3) 用包括 constant 的逐项计算证明。

## 2. Standard 延拓的局部积分与 constant 协同

暂写 p=2。对于 g=wn(b)，Q₂ 可选为 −xy，split Weil 指数为1，故

\[
 F_j(b):=\lambda_2(\mathbf1_{p^jL_2})(wn(b))
 =\begin{cases}p^{-2j},&|b|_p\le p^{2j},\\|b|_p^{-1},&|b|_p>p^{2j}.
 \end{cases}                                          \tag{4}
\]

标准延拓乘 \(\max(1,|b|_p)^{-s}\)。在 s=0 换元 b'=p²ʲb，二维体积 p⁻²ʲ与 db 的 p²ʲ完全抵消，得到

\[
 W_{n,2}(0,\psi_j)=W_{n/p^{2j},2}(0,\psi_0).           \tag{5}
\]

若 n 不被 p²ʲ整除，(5) 为0；incoherent 全局 product 仍在某个 nonsplit／arch 位有强制零，因此其一阶 derivative 系数也为0。若 n=p²ʲt，2以外的 finite 位由平方单位 p²ʲ保持 native 量，正 n 的 arch 值仅改变 e(nτ)，负 n 的 arch derivative 保留完整 β₁(4π|n|v)。于是

\[
 a_n(\phi_j)=\mathbf1_{p^{2j}\mid n}a_{n/p^{2j}}(\phi_0)
 \quad(n>0),                                         \tag{6}
\]

负 n 的同式应把右侧 v 改为 p²ʲv；没有截断 β₁ 或任何 return。

常数项不能由(5)跳过。记 raw 局部 intertwiner 的 identity 值为

\[
 M_j(s)=p^{-2j}\left[1+(1-p^{-1})\sum_{k=1}^{2j}p^{k(1-s)}\right]
       +(1-p^{-1})\frac{p^{-(2j+1)s}}{1-p^{-s}}.       \tag{7}
\]

原 native \(M_0=(1-p^{-s-1})/(1-p^{-s})\)。两者在0有同一 residue，且 Laurent 常数之差为 −2j(1−p⁻¹)，所以可消奇性的比值满足

\[
 R_j(0)=1,\qquad R_j'(0)=-2j\log p,
 \qquad R_j=M_j/M_0.                                 \tag{8}
\]

原件 normalized E* 的 constant 两腿在0抵消。第二腿乘 R_j 之后，\(-v^{-1/2}E^{*,\prime}\) 的 constant 精确多出 −2jh_k log p，故

\[
 a_0(\phi_j,v)=a_0(\phi_0,v)-2jh_k\log p
             =a_0(\phi_0,p^{2j}v).                   \tag{9}
\]

这里 h_k=1，但保 h_k 可看出来源。双腿必须协同变化；仅缩放 positive coefficients 而保 constant 不变会丢掉真实的(9)。结合(6)和 negative coefficients 即证(3)。

去 constant 的完整 Mellin 由变量替换给

\[
 \mathscr M_j(s)=p^{-2js}\mathscr M_0(s),
\quad\mathscr M_0
 =\Lambda_0\Lambda_\chi
   (\log7+\Lambda_\chi'/\Lambda_\chi-\Lambda_0'/\Lambda_0).
                                                               \tag{10}
\]

完整 \(\Gamma(s/2)\)、所有 proper prime powers、相伴 χ 的项均在右侧，constant 通过(9)恢复。p⁻²ʲˢ是由指定 finite lattice 固定的无零 level 因子，不是任意完成化 B(s)，也没有隔离出经典 Weil 型。

## 3. 有限位对应的实际 scheme，及这个 split 选择的作用

对 n>0 定义模态问题

\[
 Z_j(n)(S)=\{(E,\iota,z): z\in V(E,\iota),\quad p^{2j}Q(z)=n\},
 \qquad y=p^jz.                                      \tag{11}
\]

它在 p²ʲ|n 时与原 \(Z(n/p^{2j})\) 真正同构，否则为空。这里是以 z 为对象、记录 y 的实际模态问题，而非把所有几何 y 的 fiber 任意赋权。End(E) 无整数 torsion，使可除的 z 唯一。

对 split p=2，原 special cycles 在 char2 为空。在其余支撑位，y 的2-adic divisibility等价于 y 杀 E[2ʲ]；因 [2ʲ] 的 finite étale kernel，商的泛性质给 y=[2ʲ]z。其 vanishing 在 deformation 上 rigid，所以它定义 Z(n) 的 clopen union，既有局部厚度不变。关键不是“2在 base 上可逆就自动可除”：可除性来自 Tate／torsion 条件；base可逆只用来保持该条件的 étale rigidity。

因此(11)在这个 split 特例确为 finite Schwartz (1) 对 native special cycles 的筛选，且

\[
 \deg Z_j(n)=\mathbf1_{p^{2j}\mid n}\deg Z(n/p^{2j}).     \tag{12}
\]

负指标则在原 arch lattice 取 y∈pʲV：

\[
 Z_j(n,v)=Z(n/p^{2j},p^{2j}v)\quad(n<0,p^{2j}\mid n),  \tag{13}
\]

否则0。(13) 是完整 β₁ 的真实 arch divisor；constant 的**degree**按(9)协同。原件常数项的 Faltings 身份不等于已构造一个 canonical relative chain，本文没有从其 degree 反推该 chain。

令 ψ_A=ψ₀−ψ₁。因 split divisibility子模态是 clopen，正指标

\[
 Z_A(n)=Z(n)-Z_1(n)                                   \tag{14}
\]

是真有效 complement，并非形式 signed cycle伪装成有效。完整 modular function 为 φ_A=φ₀−φ₀(4τ)，其 constant 是 +2h_k log2。q7时

\[
 \deg Z(1)=2\log7,\quad \deg Z(4)=6\log7,
 \quad\deg Z_1(1)=0,\quad\deg Z_1(4)=2\log7.           \tag{15}
\]

所以两个完整 coefficient families \(\mathbf Z_A,\mathbf Z_1\) 不成比例。这是实质非标量 target，不是复制同一 Z 的两个名称。

## 4. 显式物理源：两个独立通道、全原 norm、完整预算

取 a=log4。沿579的实际 Gaussian轨道，先各作固定 D₋ₐ 后投到 native weight1线，得到

\[
 c_b(r)=\int r(u)\operatorname{sech}((u-b)/2)du,
 \qquad b=0,a.                                       \tag{16}
\]

实际有限 Schwartz／cycle源为

\[
 \mathcal S(r)=\varphi_*\otimes[c_0(r)\psi_A+c_a(r)\psi_1],
 \qquad\mathcal C(r)=c_0(r)\mathbf Z_A+c_a(r)\mathbf Z_1.
                                                               \tag{17}
\]

两通道选择只用 p、Gaussian和原source，不依赖 Q 或零点。c₀、cₐ不成比例；(15)证明 target也非比例。它进入 actual Schwartz及 native standard sections，并按(3)、(9)、(12)、(13)分别接完整 finite／arch／constant **degree**身份。一般源系数非整数，故(17)是实／复系数循环，不假称整线丛。

记 μ=||ψ₀||²（全部 finite Haar 规范固定）、ν=||φ*||²。ψ_A与ψ₁支撑不交，有限范数分别3μ/4、μ/4，故实际 mixed 费用无遗漏：

\[
 \|\mathcal S(r)\|^2
 =\nu\mu[\tfrac34|c_0(r)|^2+\tfrac14|c_a(r)|^2]
 \le4\nu\mu\|r\|_{du}^2.                              \tag{18}
\]

原 zero-extension Dlog 控制 du，所以(18)同样支付原 Dlog→此 Hilbert 像；不是 height／primitive pairing 的界。各 fixed有限Schwartz半范数也由相同两个 bounded functionals 支付。这比 raw dilation 的全线 section sup 费用好，但没有新的 Γ 高频能量；固定维值域仍不能编码全 \(\log|t|\) 原型。

完整输出 modular function和 Mellin 分别是

\[
 \phi_r(\tau)=c_0\phi_0(\tau)+(c_a-c_0)\phi_0(4\tau),
 \qquad\mathscr M_r(s)=[c_0+(c_a-c_0)4^{-s}]\mathscr M_0(s).
                                                               \tag{19}
\]

这没有删 Γ、prime powers、伴随 χ 或 constant。但 bracket 仍是 source-dependent signed multiplier；native有效性不是 bracket的正逆，也不是 \(Q_\zeta(r)\) 的预算身份。

## 5. 405 全主关系的 finite-channel spanning；fixed relative 仍全死

恢复405真实关系 \(p=(D^2-1/4)H\ne0\)，H>0、H∈S_exp。对全部实平移 τ_b，直接分部积分给

\[
 c_{a_j}(\tau_bp)=-\tfrac12\int H(v)
       \operatorname{sech}^3((v+b-a_j)/2)dv.             \tag{20}
\]

令其 j=0 的函数为 F(b)，则 F 是负的 L¹ 连续函数，∫F≠0。因此 Fourier 在0附近不为0。若有限 distinct shifts a₁,…,a_m及常数 d_j 满足

\[
 \sum_jd_j c_{a_j}(\tau_bp)=0\quad\forall b,
\]

Fourier 后 \(\widehat F(t)\sum_jd_je^{-ia_jt}=0\)。在0附近的指数多项式恒零，故每个 d_j=0。于是

\[
 \operatorname{span}_{\mathbb C}\{(c_{a_1}(\tau_bp),\ldots,
              c_{a_m}(\tau_bp)):b\in\mathbb R\}
       =\mathbb C^m.                                  \tag{21}
\]

这是 exact 全 noncompact Pan轨道，不是双pole矩或 finite-window近似。式(17)本身在 n1的 degree为 \(c_0(\tau_bp)2\log7<0\)，已非principal。

任意 fixed 线性 relative／boundary／primitive运算 Π，如果只读这有限通道 target且满足所有405关系，(21)迫使 Π逐个杀尽 target directions。于是 Π∘C=0。多通道确实逃出了579的单 c(r)，却没有逃出 finite-dimensional source信息门；固定 subtract-degree、固定 matched boundary及对这些数据的事后quotient，都不能同时消全405且保非根。源依赖补偿若最终仍经同一个固定线性quotient，也归此情形；任意非线性zero-preserving后处理的漏失另由下一节显式核源证明。真正读取额外非标量源信息或改变载体的边界未被排除。

## 6. 537 的同窗、双pole-zero、全通道漏失

这不是只用全空间维数声称源费用。固定 I=(−17/16,17/16)，选 m+1个互不交支撑的非零 smooth bumps ψ_k∈Cc∞(I)。令

\[
 A_{jk}=\int\psi_k(u)\operatorname{sech}^3((u-a_j)/2)du.
\]

取明确有限矩阵 A 的任一非零零向量 η（不读 Q），定义

\[
 \psi=\sum_k\eta_k\psi_k\ne0,
 \qquad r_*=(D^2-1/4)\psi.                             \tag{22}
\]

compact ODE唯一性给 r*≠0，分部积分给双pole矩为0，且每个 c_aj(r*)=0。原537全complex定理同一源上给

\[
 Q_\zeta(r_*)\ge2^{-49162}\|r_*\|_{du}^2>0.            \tag{23}
\]

因此(17)把一个实际 fixed537非根送为0，即使后续 Π不是线性，也不可能从零数据恢复该源的 full Hermitian pairing。这里有限Schwartz norm可支付，不解决 coverage。增加任何有限个 shifts仍有(21)、(22)；不再续参数。无限family／变域／strong topology／读取额外原source的relative边保留。

## 7. Inert p=3：schematic divisibility、point筛选与standard导数三者不同

一个直接核查能防止把上面的 split身份免费延至危险位。q7的3为inert。n=27时所有 native special endomorphism几何点均可写 y=3z、Q(z)=3，但 Gross厚度不同：ν₃(27)=2，ν₃(3)=1。因此

\[
 \deg Z(27)=8\log3,\qquad
 \deg\{(E,\iota,z):y=3z,Q(y)=27\}=\deg Z(3)=4\log3.     \tag{24}
\]

后者是真 moduli 的 schematic divisibility；前者只在几何点上筛 y∈3V后保旧 deformation厚度。它们不能混同。

甚至固定 standard s-extension 的 ψ₃=1₃L中央导数也不是这两个量之一。原 unramified anisotropic norm lattice有

\[
 F_0(b)=\begin{cases}1,&|b|\le1,\\(-1)^k3^{-k},&|b|=3^k,k\ge1.\end{cases}
\]

F₁(b)=3⁻²F₀(3²b)。对 n27 的 additive shell 积分，令 X=3⁻ˢ，raw Whittaker精确为

\[
 W_{27,3}(s,\psi_3)=\tfrac19+\tfrac29X+\tfrac23X^2
                         -\tfrac23X^3-\tfrac13X^4.     \tag{25}
\]

其0值为0、导数为16log3/9。乘同一个 \(L_3(s+1,\chi)=(1+3^{-s-1})^{-1}\) 后，normalized derivative是4log3/3；native normalized derivative是2log3。其他位相同、唯一zero在3，所以实际新的完整正指标系数为

\[
 a_{27}(\psi_3)=\tfrac23a_{27}(\psi_0)=\tfrac{16}3\log3.
                                                               \tag{26}
\]

这三者 8、4、16/3均乘log3而不同。式(25)的逐shell计算还用到：对 v₃(n)=3，\(\int_{|b|=3^k}\psi(-nb)db\) 在1≤k≤3为(1−1/3)3ᵏ，在k4为−3³，之后0。native多项式则为 \((1+X/3)(1-X+X^2-X^3)\)，提供独立代数复核。

因此“改变有限φ并保standard延拓”等于“只改可除性过滤／保全旧局部length”是错误运输。这里没有说一般Schwartz算术theta不存在；需要指定 level 的实际 integral模型及其导数／vertical correction，不能由 weight1 native theorem或 s0等变性直接领取。下一节给出这个特定 finite位的实际 correction，不续参数。

## 8. 可支付的 transported family 与实际局部 cocycle

这一补充来自 root 提议后的本分支独立核算；不是原件关于任意level循环的 theorem。取任一 p≠7，a=p⁻¹、\(c_p=\chi_p(a)^{-1}|a|_p^{-1}\)，定义同一个 I_p(s,χ)中的两条真实family

\[
 \Phi^{\rm std}_{\psi_p}(g,s)=\lambda(\psi_p)(g)|a(g)|^s,
 \qquad
 \Phi^{\rm tr}_{\psi_p}(g,s)=c_p\Phi_0(gm(a),s).         \tag{27}
\]

s=0严格同为 λ(ψp)，但导数不同。split p2有 c₂=1/2，inert p3有 c₃=−1/3；这个负符号是χ，不是可选归一化。由
\(wn(b)m(a)=m(a^{-1})wn(ba^{-2})\)和 db 的Jacobian，transported raw Whittaker满足

\[
 W^{\rm tr}_{n,p}(s)=p^{-s}W_{n/p^2,p}(s,\Phi_0).       \tag{28}
\]

式(28)保全部 local derivative，没有忽略 standard延拓差。还有一个保全s及character的独立校验：用全局 rational m(p)作left translation，把finite p处的m(p⁻¹)移到arch，得到τ→p²τ；其余finite单位仅在q7处留下native Iwahori eigen χ₇(p)。全局character的乘积公式给χ₇(p)=χ_p(p)⁻¹，因此 \(c_p\chi_7(p)=1/p\)。classical v⁻¹ᐟ²归一化与v'¹ᐟ²=pv¹ᐟ²恰好补回该1/p。于是每个s的adelic完成化family精确为 Etr*(gτ,s)=p⁻¹E0*(g_{p²τ},s)；只有乘classical v⁻¹ᐟ²后才是τ→p²τ的exact pullback。inert时c₃和χ₇(3)两个负号都不能省。

对非零 n，这也给 transported positive cycle系数正好 deg Z(n/p²)，negative arch divisor为 Z(n/p²,p²v)，从而完整

\[
 \phi^{\rm tr}_{\psi_p}(\tau)=\phi_0(p^2\tau).          \tag{29}
\]

常数独立核：transported first leg在identity乘pˢ，second leg由(28)乘p⁻ˢ；所以 constant derivative精确导致 \(a^{\rm tr}_0(v)=a_0(v)-2h_k\log p=a_0(p^2v)\)。native fixed-Haar ν不改变；s=0 Schwartz仍是ψp，新的导数边界不是Gaussian norm重定义。

两family的精确局部差为

\[
 \delta_p(g)=\left.\partial_s(\Phi^{\rm std}_{\psi_p}
                    -\Phi^{\rm tr}_{\psi_p})(g,s)\right|_0
 =\lambda(\psi_p)(g)
      \log\frac{|a(g)|}{|a(gm(p^{-1}))|}.               \tag{30}
\]

这是 I_p(0,χ)中的明确源无关localcocycle。在 wn(b)且|b|=pᵏ的单元上，其log因子依次为+logp（k≤0）、0（k1）、−logp（k≥2）；不是任意principal／正边界标签。把它与其余实际native局部section张量，normalization不变，则

\[
 \phi^{\rm std}_{\psi_p}-\phi^{\rm tr}_{\psi_p}
   =-v^{-1/2}q^{1/2}\Lambda(1,\chi)\,E(g_\tau,0,
             \delta_p\otimes\Phi_{\ne p}(0)).          \tag{31}
\]

这里 E 采用未完成化的(1.6)记号，前因子是同一原件的完成化；两family在0相同使normalizing factor的导数贡献抵消。(31)是实际section／Eisenstein边界公式，**还不是一个算术relative链的principal同构或height恒等式**。δ可含coherent方向；不能因原family在0 incoherent而将 E(0,δ)删掉。

inert3,n27时(28)给 normalized derivative=log3，完整coefficient=4log3，正好 schematic divisibility cycle(24)。因此(26)与它之间差+4log3/3，确由(31)承接。constant也有非零差：原 anisotropic local integral在 X=p⁻ˢ记号下给

\[
 M_0(s)=\frac{1+X/p}{1+X},\qquad
 M_1(s)=p^{-2}+(1-p^{-1})p^{-1}X+(1-p^{-1})X^2
                 -(1-p^{-1})\frac{X^3}{1+X}.
\]

由此直接得到

\[
 (M_1/M_0)'(0)=-2(1-p^{-1})\log p\quad(p\ \text{inert},j=1),
\]

所以p3 standard constant是a₀(v)−4h_k log3/3，transported为a₀(v)−2h_k log3，两者差+2h_k log3/3。完整 finite／arch／constant不能只修 n27而保原constant。

费用边界也明确：在compact picture k∈SL₂(Zp)，\(|\log(|a(k)|/|a(km(p^{-1}))|)|\le\log p\)，故

\[
 \|\delta_p\|_{L^2(K_p)}\le(\log p)
                         \|\lambda(\psi_p)\|_{L^2(K_p)}. \tag{32}
\]

这是同一actual局部section的固定p导数费。源系数仍由(16)的原du费支付；每fixedτ-compact的E读出还有独立固定moderate-growth常数。它不免费给全高度、无限p、原Dlog→primitive height或RR容量。若把(31)按有限cs作协同relative修补，整个信息仍经finite vector，(21)–(23)照样成立；因此它填了具体局部边界而未填405／coverage。

## 9. 范围、同对象二次容量与净后果

新具体交件是(1)–(19)的 split finite位实际非标量源、完整constant协同与精确cycle筛选，(20)–(26)的 relation／coverage／危险位反测，以及(27)–(32)的同初值transported family／实际localcocycle。所有原du费用在同一个物理r上；finiteSchwartz或localcompact section范数不是 height或RR费用。

未交件：不经有限cs的新relative arithmetic-chain公式；405 principal同构而不杀537；同一整对象上 mixed交数、局部消失过滤、乘法与平方RR容量；完整 mixed KRY式经过 signed deconvolution 到经典 Qζ 的身份和原费用。(19)的 Mellin multiplier与(31)的解析localcocycle不是这些容量的替代品。

continuous正反分布若都经(17)，所得额外正Gaussian范数仍非其 native相反号Weil型；尚无continuous→CM算术运输。函数域的 C×C全Frobenius mixed交数／双degree扣除及RR正号没有被(17)的dimension0 degree取代；必须保所有aliases／H⁰,H²，而非一条scalar生成函数。需要的对照结论是设施类型不能偷换，非否定算术theta的所有更高维／relative推广。

strong-old542+555→557 whole leading4/5负惯性上预算与classic独立容量、actualq、成长core／coupling／Ξ未变。本分支停止 finite-channel fixedrelative及无correction的 inert筛选；不续level／shift数、以Q标签的primitive商或下一paper。真正源依赖、非有界／strong topology、无限有费family及不同相对链不在本门排除范围。
