# 574. 实际双位覆盖的非平凡相对 Picard 族与物理源准入

2026-10-22。[C037](../goals/contracts/C037-actual-cover-picard-clutch-and-source-gate.md)的一轮原件；同G20261014／固定0c4f基线。
本轮新增的是实际覆盖上指定指数拼接族的精确同构核、双边界刚性化及不变度量门。
它不以Ξ零除子为底空间，也确实不只是给自由等变线换frame；但试验的源桥仍未提供独立算术容量。
不主张外部首创；不分类整个Picard群，不宣称新的经典Weil正性或RH证明。

## 1. 从函数域应当运输什么

函数域的degree-zero线不是任意复参数：局部DVR中的valuation给Cartier除子，全局有理函数给principal同构，曲线proper性给有限维截面与base change。
RR与曲面上的有效性／Hodge指数把这些**同一对象**上的数据联系起来，再作用于Frobenius对应；正号并非单由每条线的Hermitian纤维度量产生。
已有567和本轮前的真实genus2控制是输入，不再把已知Weil证明当新定理。
[Milne的Jacobian讲义§§1、7.6](https://www.jmilne.org/math/xnotes/JVs.pdf)中移动、好有效图与Picard校正是本轮参照。

因此先问实际adelic覆盖是否已有非平凡线族，再问源、主关系、费用、整性和截面是否落在同一对象上。前一问肯定不自动支付后一问。
旧410/411/420已有真正核丛、相对K类及指数线；“以前只有自由线”不是准确的强旧对照。

## 2. 真实双位覆盖与指定线族

固定p=2、q=3，L=log2、M=log3。使用[413](413-f1-two-place-boundaries-and-virtual-class-collapse.md)已付的紧单位商：

\[
T=\mathbb Z\cup\{\infty\},\quad Y=T^2\times\mathbb R_t,
\quad(a,b)(j,k,t)=(j+a,k+b,t+aL+bM).
\]

删双∞层得O；Wp={k有限}、Wq={j有限}为实际Γ=Z²不变开覆盖，交B=Z²×R。
共同bulk坐标始终为x=t−jL−kM。每一side作用proper，商分别为Z_L、Z_M；整个O作用非proper，不能换成Hausdorff轨道空间。
每个Z_L是螺旋`x↦(e^x,e^(2πix/L))`加负端圆；负尾加圆紧，正端不补点。
这来自半局部Q₂×Q₃×R₊；实坐标始终非零，不能冒称全部adeles已覆盖。

在两side取trivial Γ-action的平凡复线，在交上以

\[
g_z(x)=e^{zx},\qquad z\in\mathbb C                                      \tag{1}
\]

拼接为𝓛_z。它给O上的真实连续等变复线及任意连续参数base change。
side各自常数frame在闭边界P、Q上给既定标架；保留它们定义本稿的relative对象。
对象范畴是实际群胚的连续等变线，尚非regular／Arakelov线、原Schwartz DGA可逆模或有限支C*投影。

## 3. 新增精确分类与度量门

令Λ=(2π/L)Z+(2π/M)Z。则本指定子族满足

\[
\mathscr L_z\simeq\mathscr L_w\iff z-w\in i\Lambda;\qquad
(\mathscr L_z,\mathrm{fr}_P,\mathrm{fr}_Q)
\simeq(\mathscr L_w,\mathrm{fr}_P,\mathrm{fr}_Q)\iff z=w.             \tag{2}
\]

独立详细证明见[周期拼接原件](../reviews/2026-10-22/adelic-cover-picard/periodic-clutch-classification.md)。其关键不是读零点，而是：

1. 每个side unit负端一致趋于相应圆上的周期unit，且模有正上下界。
2. 若e^(zx)是两side units之比，负尾有界先迫Re z=0；三频紧环面近回归把渐近周期恒等式变为全实线恒等式。
3. 两个周期unit的绕数加有界周期log迫Im z∈Λ；反向直接用两个周期gauge构造。保两frame时gauge负端均趋1，又迫z=0。

具体𝓛_(iπ/L)非平凡，且absolute中为二阶类；否则1/2=m+nL/M，与L/M无理矛盾。
故真实覆盖允许非平凡的**相对可变线族**，不是旧free graph恒类。这里只有指定子族的分类；不声称全Pic等于C/iΛ。
Λ稠密，C/iΛ只作为自然参数商使用；不能擅自赋给全部Pic模空间或套Hausdorff分离定理。
`z↦t z`同时给真实连续族，因此旧普通Hausdorff／paracompact底空间的同伦不变性不能直接用于此非proper等变范畴。

另有准确度量门：𝓛_z有Γ不变、连续、处处正的Hermitian metric，当且仅当Re z=0。
必要性来自两边界紧圆上度量的正上下界及transition模e^(2Re z x)；充分性是两side均取1。
这只排**等变不变**度量；底层Hausdorff O上的普通非不变度量仍可由partition of unity给出，奇异或带权修补亦未排。
纯虚族全有正纤维度量，仍没有独立RR／mixed正性。

## 4. 两个实际源构造：一个平凡，一个失败全主关系

物理源固定为r=e^(u/2)f∈F_c=S_exp,C，关系为405的全部physical P_c，而非compact交。
先取固定κ∈Cc∞，g_r=exp(κ*r)。因κ*r负端趋0，g_r可在任一side延拓且边界为1。
这给显式relative gauge，故所有源均为相对平凡类，537非根也消失。代表费用真实可付：

\[
\|\kappa*r\|_\infty\le\|\kappa\|_2\|r\|_{du}
\le\|\kappa\|_2(\log2)^{-1/2}\|r\|_{D\log}.
\]

反之直接选择mean参数

\[
z(r)=\ell_0(r)=\int r(u)du,
\qquad r\longmapsto(\mathscr L_{z(r)},\mathrm{fr}_P,\mathrm{fr}_Q)       \tag{3}
\]

确实给实际非平凡线移动，且不预设零点位置。537取0≠ψ≥0、compact于17/16窗，r₀=(D²−1/4)ψ：
μ±r₀=0、Qζ(r₀)>0、ℓ₀(r₀)=−(1/4)∫ψ<0，因此(3)看见这个真非根。
但405的实际h=Eη_h>0、H=e^(u/2)h>0给

\[
P=(D^2-\tfrac14)H\in P_c,\qquad\mu_\pm P=0,
\qquad\ell_0(P)=-\tfrac14\int H<0.                                  \tag{4}
\]

全部端点项由405的S_exp衰减支付。于是零商类被送到非平凡线；(3)失败**全部主关系的同构消去**。
纯相位修补z=iℓ₀(r)在实源上有不变度量，但缩放同一个P使ℓ₀(P_scaled)=π/L，仍给(2)的非平凡类。
只用μ±选参数能消全P_c，却杀双矩零的r₀。405的h本身保两degree(1/4,1/4)，不可误当principal而一并删去。

## 5. 原du／Dlog费用及一般标签修补的范围

源支撑[-A,A]时

\[
\|\ell_0\|_{du}=\sqrt{2A},\qquad
|\ell_0(r)|\le\sqrt{2A/\log2}\,\|r\|_{D\log}.                         \tag{5}
\]

后一项是upper，不称Dlog精确dual norm。覆盖上另取|x|≤B才有
`||g_z||∞,||g_z^−1||∞≤exp(B|Re z|)`；A与B不是同一截断。
纯虚参数模1，但对参数求导仍有x费用；非纯虚参数在负端的等变度量门已经失败。
这些是选定representative/frame的充分费用，不冒称所有源lift的必要lower或同源算术高度。

任一复线性标签ℓ若使absolute类消全P_c，(2)先迫ℓ(P_c)⊂iΛ。
P_c对所有标量闭合，而iΛ可数，所以ℓ(P_c)=0。relative情况由零kernel直接得同一结论。
若ℓ本身还在全线原du／Dlog上连续，553的P_c稠密性迫ℓ=0。
这里**先论标签后论密度**，没有把非Hausdorff的C/iΛ直接当Hausdorff target套旧结论。
Fréchet、有费fixed窗／cofinal、变域和非线性路线仍保留。

若用Mellin标签ℓ_z(r)=∫e^(zu)r，405准确给
`ℓ_z(P)=1/2 (z²−1/4) ξ(1/2+z)`；消全主关系的单evaluation坐标回到两degree或旧完整零点坐标。
经过旧源商本身并非错误或循环；问题是当前只换标签，未新增独立整性、metriclift或容量。

## 6. 必须保留的强合法修补：用完整Q标记真实线

不能由(3)失败推出所有actual source map不存在。取实c≠0，定义

\[
z(r)=ic\,Q_\zeta(r).                                                \tag{6}
\]

405完整identity给P_c为Q的radical，故(6)消全部principal coset；取c=π/[L Qζ(r₀)]又使r₀映到非平凡𝓛_(iπ/L)。
它用分布侧完整Q定义，不读未知零点位置，且有Γ不变正纤维度量。
但它非线性，不把源加法送成tensor；并且只将旧完整Weil数值包装为线参数，无法从此反向证明数值非负。
对每个先fixed窗，旧Γ form和有限prime／pole扰动给
`|Qζ(r)|≤C_A||r||²_Dlog`及相应极化差界；完整Γ在纯du上无同级bounded form，不能偷换费用。
(6)证明“非平凡线＋消关系＋537＋正纤维度量”四门一起仍不足以提供独立容量。
一般g系统在Q_g定义后也能做同样标记；这不是从g分布独立恢复Weil正性的机制。

## 7. 连续正反例与真函数域检验

沿562的真实连续正测度系统Z_c(s)=1+c/[s(s−1)]，d=c−1/4=±1/16。
primitive实现R_d=C[w]/(w²+d)、w†=−w，a_r=∫r(u)e^(uw)du=A_r+B_rw；完整型是

\[
Q_c(r)=2|A_r|^2+2d|B_r|^2.
\]

取偶φ≥0非零、support在(−1,1)，g=uφ，r=(D²−1/4)g。则μ±r=0、ℓ₀(r)=0，mean族在两模型均平凡；
A_g=0、B_g>0，a_r=−(d+1/4)a_g，故

\[
Q_c(r)=2d(d+\tfrac14)^2B_g^2
\]

在两段严格异号。正段真实primitive方向也被mean标签漏掉。(6)式Q-marker在正负两段都能给unitary line，仍不能选出正号。
模型自身Γ=0、双pole及完整连续prime分布都保留；没有给它们虚构经典adeles。
控制所否定的是普通clutch/fiber metric/source标签作为充分条件，不是一般g必有这个半局部底空间。

函数域正控制使用真C/F₅:y²=x⁵−x+1、P=(0,1)、Q=(1,1)，L₀=O(P+Q−2∞)非平凡degree0。
K~2∞，canonical评价矩阵[[1,1],[0,1]]的det=1给h⁰(K−P−Q)=0；RR给h⁰(L₀)=0、h⁰(K⊗L₀)=1，而h⁰(K)=2。
这是真正移动改变有效化后截面的实例，有proper族、DVR过滤及Picard校正overlap；本轮连续等变线的非平凡性尚无这些设施。
这项旧正控制被实际代入比较，不再次计数学轮，也不声称任意degree0线都有非零截面。

## 8. 完整经典目标与仍欠的独立输入

令r*=conj r(−·)，μ±r=∫e^(±u/2)r。目标始终是

\[
\begin{aligned}
Q_\zeta(r)={}&2\Re(\mu_+r\,\overline{\mu_-r})
 +[\psi(1/4)-\log\pi]\|r\|_2^2\\
&+\tfrac12\int_0^\infty {2e^{-v/2}\over1-e^{-2v}}
       \|\tau_vr-r\|_2^2\,dv\\
&-2\sum_{p,k\ge1}(\log p)p^{-k/2}
       \Re(r*r^*)(k\log p).                                      \tag{7}
\end{aligned}
\]

其arch Fourier multiplier为Γ(t)=Re ψ(1/4+it/2)−logπ=2θ′(t)。所有proper powers、contact及双pole共同保留。
真实覆盖的logp圆和正纤维metric还不能识别(7)；尤其只建p=2,3子对象远未覆盖全部finite places及arch规范。
仍须独立给出：

- 全P_c对应实际rational/local-unit同构、保primitive覆盖的源桥，含原norm的metric／section lift；
- 同一整模型的valuation消失过滤、乘法及proper／有控截面空间，不能只给复拓扑绕数；
- 不读取Q的符号、零点位置或等价Hodge假设的有效性／mixed RR容量；
- 该容量预算与(7)完整Γ、每个p^k及pole缺陷的同源identity，全部成长费用和补空间协同。

用Q来定义“容量”、或假设完整heat trace等于Weil热量又由正算子推出正性，只是旧等价／conditional接口；独立identity或几何容量才是新输入。

## 9. 净后果、停止与后续准入

新增(2)和等变metric iff Re z=0的精确命题，关闭“这个真实覆盖是否仅允许平凡clutch”的局部未知。
旧410/420非平凡K线本身不蕴含本子族的完整kernel；本轮不以source0隐藏这段新证明，统一计一完整轮。
mean与decayingclutch入口已按用户停止；合法Q-marker保留为旧包装反控制，不继续调scalar、probe或frame。
**宏观瓶颈未改变**：关系保持的独立源桥／同对象整性过滤、primitive容量及完整预算比较仍欠。
最强实际ζ后果仍542+555→557的whole leading4/5负惯性上预算；本轮无新whole/core/coupling/Ξ后果，Goal门仍open。

下一仅验收一份区别于(6)的具体relative Cartier／valuative源数据：先实际算其405同构、537及连续双符号响应、原费，再谈capacity合同。
若无这项新数据，不自动延长本子族或串另一篇来源。非标量、新相对层、强拓扑、变域及有费无限修补均未被排除。
