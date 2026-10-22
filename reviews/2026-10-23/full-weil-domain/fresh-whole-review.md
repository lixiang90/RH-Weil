# 582／C045：独立 fresh 整体审查

2026-10-23；独占 `/root/full_weil_green_fresh_582`。本审查不改 STATE／cadence，不另计数学轮。已恢复 G20261014／固定0c4f、581停止范围、C045三句准入及三份当前原件；下列结论只认证数学消费范围，不认证Git发布或长期Goal完成。

最终结论：已实际全文读完root [582主稿](../../../notes/582-full-local-weil-strong-domain-and-actual-green-source-gates.md)及三分支原件，整体 **qualified PASS**。主稿没有把以下局部设施升级为primitive容量、Weil正性或宏观完成；没有发现阻止下列限定消费的critical错误。

## 1. 独立核算与对象边界

强域原件的紧开Gabor原子确为L²正交基：每个支撑coset上是完整字符基，STFT绝对值在相空间的单位coset块上等于对应系数绝对值。因此其S0范数正好为实际原子系数ℓ¹，而非仅凭抽象orbit定义的包络。normalized球向量的范数是p^|j|；两位H=2^|j|11^|k|，ΣH^-1=18/5和sech半宽核L²范数2，给原du费用36/5。A1嵌入S0并非等距、也不恢复原Bruhat域，这些区分保留。

独立以split Q=−x₁x₂计算chirp：当|b|=p^m>1，L上的非零Fourier系数恰有p^(2m)个、每个模p^-m，故算子范数为max(1,|b|)。这一步不除2，p=2同样成立。dilation费用max(|a|,|a|^-1)、Fourier等距，再由K等距及Cartan分解得到完整SL₂作用范数θ_p(g)=max entries |gᵢⱼ|_p。取实际逆K作用的窗口达到下界。稠密smooth原子、群紧集上局部有界给强连续；没有全群uniform、算子范数连续或算术functor结论。

arch raw接口的Gaussian-STFT费4√νcosh(u/2)与S_exp指数矩相容。双pole-zero compact源平移后，raw像的全L∞费按e^(T/2)增长、原du/Dlog不变；论证必须用全sup，不能用已被polezero杀掉的origin值。fixed Gaussian⊗F_w和另一个raw T*r是不同映射，其原费不能互换。

## 2. 完整λ、过滤和额外源

Bruhat分解给小cell读取F(0)，大cell读取∫F(x)ψ(bQ(x))dx。因此准确核为F(0)=0且Q_*F=0；有限复测度的Fourier唯一性合法，不要求该核为零。odd coset及O(Q)协变差给even非零核，文稿中p=2的支撑、体积及Hilbert费用均核对成立。读取原r的Y_o/Y_e确实是非标量、注入的解析物理源，但标准section/Eisenstein完全读不到该腿；不能因此预报非零算术循环。

点消失ideal不full-Weil不变，开闭支持过滤的理想幂恒等于自身；它们不是Cartier阶数。合法covariant过滤族并未被排。fullWeil也非原点乘的代数automorphism：chirp施于FG与分别施于F/G的相位相差一份chirp，p=2可直接取b=1/2、x=y=1检验。因此S0函数代数、equivariant DGA、截面乘法必须分别运输。

Y_o附加到旧J_w后解析信息确实增多，但原λ预算不变；其正交费用不等于相对principal或二次容量。405原非compact全平移的c_a严格负，额外λ零腿不能取消该charge。允许真实boundary读取更多信息；没有将所有regulator或所有kerλ算术解释一并否定。

## 3. arch-only全s右运输的实际Green门

原件公式g_τm(e^(u/2))=n(x)m(√(ve^u))正确：变化v而不缩放x，故整数Fourier指标不变。实际输出∫r(u)e^(u/2)φ(x+ive^u)du不等于φ(e^uτ)，也不等于standard延拓导数。std/tr差的section含两Iwasawa log之差，绝对值≤|u|/2；该修正被保留，未免费宣称算术等变。

正cycle幅度的du核平方积分是1/(4πnv)。独立展开β₁双重积分并换元，得到

\[
 \int_0^\infty e^{2y}\beta_1(2y)^2dy
 =\tfrac12\int_1^\infty\frac{\log t}{t(t-1)}dt
 =\frac{\pi^2}{12}.
\]

完整负幅度为2e^(u/2)e^(2πmve^u)β₁(4πmve^u)，其du平方费用为π/(6mv)，不是漏掉native因子2的四分之一。a_n、N_λ、q展开因子和全n总高度费尚须另付。平移源并令v=v₀e^-b给实际e^(b/2)费用，不能把fixed-height费用升级为全高度uniform。

全部v的Laplace family在全S_exp注入，确实恢复native scalar所漏的537奇非根；但对每个固定405平移，小v主项是−4πv e^(3b/2)M_H(3/2)，非零。o_b(v)只逐固定b。constant还保M'_r(1/2)，405给其非零，不可由双polezero删除。该输出所以尚非principal；把其非零像按定义商掉，仍是旧源商。

root最终§5的whole协同补充已实际重读：native各模态多项式增长／小高度指数界与S_exp支付每个fixed v的全x-Fourier绝对收敛。若完整(x,v)family对所有x为principal，其degree周期函数必须恒零，n1系数也必须零；constant及负频不能对所有x取消非零n1。因此准确结论是每个fixed b、小v存在x使完整family非principal，不声称所有x或每v。§6的M_P(1/2−z)=z(z−1)M_H(1/2−z)及实z>1时完整ℳ₀(z)>0还给完整非constant预算的独立旁证。这里并未拿一份子预算失败代替whole比较。

固定q=7 coarse Spec O_H的CH¹_R计算也限定成立：norm-Euclidean余项≤11/16证明h=1，H=k；每个prime ideal由principal关系化到唯一arch分量，degree商为R。它只拒绝在此固定native coarse CH¹中寻找额外degreezero primitive方向，不排stack/higher/framed/relative、不同载体或整(n,v)family的全源注入。

## 4. 完整预算与旧资产扣除

常数减除后的Mellin换序先在Re s>1绝对收敛，由S_exp支付指数矩，得到M_r(1/2−s)ℳ₀(s)。完整Γ与全部Euler powers、两constant腿均保留；s=0,1处源零可能只降低原double pole阶数，不能与经典Qζ的pole二次型偷换。原native KRY身份可核[作者原件Theorems1–3及§6](https://www.math.uni-bonn.de/people/rapoport/myalggeom/preprints/tinynew.pdf)，其一般Schwartz算术推广仍是提出的事项。S0背景可核[Enstad–Jakobsen–Luef §3](https://comptes-rendus.academie-sciences.fr/mathematique/item/10.1016/j.crma.2018.12.004.pdf)，本次精确split费用由原件内计算承担。

既有R_A与compact高频源说明有限个固定有界local帧范数不能付完整Γ的log高频量；全部素数幂无穷尾和双pole已在实际源上处理。该机制应扣552/579/581旧资产，不重报新classic正号或成长后果。它不排增长帧、付费无界height或读取更多物理源的真实Green。

continuous±对照的原Γ为0；它们只检出universal局部设施不能决定native signed预算，不伪称保classicΓ的CM几何反例。函数域正号来自同一C×C的primitive mixed交数、有效截面／乘法、RR/Hodge/Rosati，并保全returns/aliases和H⁰/H²；两个place步长相称，不能套用2/11的dense-grid可见性。

## 5. 限定消费与停止

可消费的新设施是：A1到实际full-local强域的精确有界作用及原费；准确的λ核与covariant过滤门；读取额外原r的native cycle/Green family及其fixed-height费用、405/537首门和完整Mellin身份。它们没有在同一对象上闭合principal、整section局部消失／lift／乘法与primitive二次RR。

停止所列S0本身、λ零extra腿或arch-only native线性Green积分自动付容量的recipe。保真实新relative/higher regulator、不同载体、强域上付费无界Green及同对象principal cocycle。长期独立容量和542+555→557 whole leading4/5负惯性UPPER、actualq/core/coupling/Ξ均未改变；本审不作Goal完成主张。

## 6. 最终原件版本绑定

下列为本次实际读到的LF-normalized SHA256；绑定版本不替代证明。

- notes/582-full-local-weil-strong-domain-and-actual-green-source-gates.md：`52198de059b8cfc23565f8fcf7ecc2e93ccd07867ecd4cdfdd94922bf6e19723`。
- full-local-domain-and-source-fees.md：`3d0ef72e9924ee74ddd962532ae057c2c5e7bc29da11d3ce8f9b98290ee0b505`。
- local-filters-rr-and-controls.md：`e856e771e38c2e6bdd88779c3997553c0e6d3fa1570dd4fe6f09aee3aebce93a`。
- actual-regulator-cycle-and-principal-test.md：`10c0cc6c5c708bb1b59c5c5887853532284c9ff55d74e3b34c7de2722b5287ea`。

已核root整合中特别容易错用的五个接口：fixedarch原费与raw强费不换；fullλ核与源family注入不换；standard／right-transported导数不换；逐项fixed-height费与全高度／全n费用不换；固定coarse natural-divisor degree商与抽象Pic张量、relative/higher或整family不换。不存在把失败candidate的primitive门扩成所有算术载体不可能的结论。
