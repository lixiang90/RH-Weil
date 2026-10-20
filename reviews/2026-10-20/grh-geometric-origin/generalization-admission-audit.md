# 从完整g-prime源到primitive交叉形式：可检验构造与准入审计

2026-10-20，独立原稿。责任范围：给出实际可计算的source→intersection模型，
检验连续正反例、真曲线与290；明确何处需要额外几何。不是经典ζ正性证明，
不修改STATE或cadence。根合同及是否结算由root另审。

## 1. 恢复与强旧扣除

核读001/002/073、290、307、363、563–566及当前Goal/STATE/主合同/战略。
001/002已有positive polarization→purity；073已有双向次指数增长与Cesaro极化；
363§5已核完整source的双degree、HRR/截面有效化、正规化及CC2018§3责任；
307已有真椭圆曲线degree positivity与全幂迹；563已有有限ODE/全递推+H的全Weil证书；
566已有unitary bundle的closed form及完整heat identity。
因此本稿不能把正H、Hodge/Rosati的名称、已知连续平方和或函数域RH重新计作新来源。
本次可判新测试是：直接由完整Π平衡定义一个可能不定的graph-intersection模型，
精确核它在哪一步拒绝负例；再检查RR式独立来源能否支付其index。
它不改变actual经典ζ的whole leading4/5、560成长K/core/coupling或通常Ξ责任。

## 2. 曲线：全点数到primitive Frobenius图Gram的准确身份

固定光滑射影几何连通曲线C/F_q，亏格g，π为q-Frobenius，N_n=#C(F_{q^n})。
在C×C中统一约定

\[
 F_1=C\times\{P\},\quad F_2=\{P\}\times C,
 \quad F_1^2=F_2^2=0,\quad F_1F_2=1.
\]

Γ_n={(x,π^n x)}满足Γ_n F_1=q^n、Γ_n F_2=1。故必须取

\[
 D_n=\Gamma_n-F_1-q^nF_2,\qquad D_nF_1=D_nF_2=0.       \tag{2.1}
\]

若互换fiber名称，减项也必须互换，不能混用。由图的法丛/adjunction，以及
Frobenius的局部次数和1−π^k的可分性，得到全部m,n而非有限枚举：

\[
 \Gamma_n^2=(2-2g)q^n,\qquad
 \Gamma_m\Gamma_n=q^{\min(m,n)}N_{|m-n|}\quad(m\ne n). \tag{2.2}
\]

第二式的q^min是交点重数，不能把Frobenius仅看作点集bijection而删掉它。
展开(2.1)给

\[
 -D_mD_n=q^m+q^n-\Gamma_m\Gamma_n
 =q^{(m+n)/2}a_{m-n},\quad
 a_0=2g,\quad a_k=q^{-k/2}(q^k+1-N_k),\ a_{-k}=a_k.     \tag{2.3}
\]

Hodge index在(F_1+F_2)^⊥上给I(D,D)≤0，因而所有有限矩阵
(a_{m-n})_{0≤m,n≤M}都半正定。对整数D_n的整数线性组合先用几何定理，
再作有理延拓、连续性和实数对角缩放，合法得到q^{-n/2}的归一化；
不要求irrational组合本身是Cartier divisor。

独立几何输入是交数理论和Hodge index，不是点数的正性。这里的最小source身份
是(2.2)；如果只有有限N_n或拟合递推，它不足以保证整个Gram。
Hodge index及intersection/degree基础核作者原文
[Milne §1，Theorem1.2、1.5、Example1.7，printed pp8–10](https://jmilne.org/math/xnotes/pRH.pdf)。
本稿(2.3)及以下full-source展开是对这些已证基础的直接计算，不冒称新的几何定理。

### 全周期Weil型直接来自同一个Gram

取L=logq，完整源W_C=LΣ_{n∈Z}a_nδ_{nL}（含a0与全部周期pole背景）。
给g∈Cc∞(R;C)，按u=y+jL分块，选择一个共同整数shift j0使相关j+j0≥0。
以E_j=q^{-j/2}D_j，primitive quotient的能量为⟨E_m,E_n⟩=a_{m-n}。
则有限和、换元直接给

\[
 Q_{W_C}(g)
 =L\int_0^L\left\|\sum_j g(y+jL)E_{j+j_0}\right\|^2dy\ge0. \tag{2.4}
\]

j0不改变内积，因为(2.3)只依赖指标差。Cc支撑保证每个y只涉及统一有限多个j；
没有未付尾或误差。此处可先作复化，实对称Gram的复Hermitian延拓保正。
这条身份直接给全complex compact Weil正性，不先假设Frobenius单位圆谱，
也不需要先给563的U,H。数值点数、有限Gram或单一fundamental strip都不能代替(2.2)及几何index。

## 3. 连续Π的同型源模型：算术能造配对，不能自动造index

先限定一个可核子类：自然完成化、中心1/2及Γ=0已经指定；极点只贡献0、1背景，
完整W确为实偶连续密度；Π在u>0的全部prime-power密度是q_Π(u)，并且

\[
 p(u)=e^u+1,\quad n(u)=u q_\Pi(u),\quad
 W(u)=e^{-u/2}\{p(u)-n(u)\}\quad(u>0),\quad W(0)=2.    \tag{3.1}
\]

n不是g-integer累计计数N，也不是primitive P密度。Π=Σk^{-1}(T_k)_*P必须先付全部powers。
若存在额外Γ、contact、pole或非连续奇性，就须更换完整身份，不能继续把(3.1)当作全源。

取实自由空间生成元F1,F2,Γ_t（t≥0），按

\[
 F_1^2=F_2^2=0,\ F_1F_2=1,\quad
 \Gamma_tF_1=e^t,\ \Gamma_tF_2=1,\quad
 \Gamma_s\Gamma_t=e^{\min(s,t)}n(|s-t|)                  \tag{3.2}
\]

定义对称双线性配对；n(0)=0所以Γ_t²=0，对应本模型的g=1自项。
Γ_t只是形式生成元，(3.2)没有声称它是真实scheme的图或有实际section空间。
置

\[
 D_t=\Gamma_t-F_1-e^tF_2,\qquad E_t=e^{-t/2}D_t.
\]

逐项展开、不读取零点即得完整source identity

\[
 \boxed{-E_sE_t=W(t-s).}                               \tag{3.3}
\]

因此完成背景与Π确实能给一个自然的、通常可能不定的primitive配对。
但“配对存在”不意味着其index为1；(3.3)上直接另假设−I≥0，仍是同一Weil正性。
Mellin双对象对偶只约束这一配对的反射/transpose兼容性，不提供正号。
本构造始终以固定完成化/预定权为输入，不能反过来无条件排掉564的B(s)自由。

### 用真实连续正primitive族逐点检验

563已从完整Π核明Z_c(s)=1+c/[s(s−1)]，0<c≤1/2的源ODE

\[
 W_c''+dW_c=0,\ W_c(0)=2,\ W_c'(0)=0,\quad d=c-1/4.
\]

令d=τ²≥0或d=−r²<0，则

\[
 W_c(u)=2\cos(\tau u)\quad\text{或}\quad2\cosh(ru),\qquad
 n_c(u)=e^u+1-e^{u/2}W_c(u).                            \tag{3.4}
\]

0<c<1/4时0<r<1/2，故两段对所有u>0均有n_c(u)>0：
正段用cos≤1，负段用cosh(ru)<cosh(u/2)。所以(3.2)的所有不同图之间的交数
均为正，degree与pole背景也都正；它们仍不能保证primitive index。

对任意h>0，归一化2点energy Gram为

\[
 G_h=\begin{pmatrix}2&W_c(h)\\W_c(h)&2\end{pmatrix}.
\]

负段detG_h=−4sinh²(rh)<0；正段全部finite Gram半正定，由cos加法公式可直接写为
两个实向量的Gram；阈值W=2时rank为1。primitive配对的负段已有一个正方向，
加上fiber hyperbolic plane，整个(3.2)的正index至少2，而真正曲面只有1。
正段在primitive quotient上负半定，fiber提供唯一正方向。
这精确区分“互不相同有效图交数非负”与“Hodge index”。

取任意实偶非负φ∈Cc∞、φ≠0，以及

\[
 g(u)=\phi(u-h/2)-\phi(u+h/2).
\]

这是合法实奇compact测试，负段有精确全源值

\[
 Q_{W_c}(g)
 =-8\sinh^2(rh/2)\left(\int\phi(u)\cosh(ru)du\right)^2<0. \tag{3.5}
\]

不需要用δ测试或有限频率采样。正段由sin/cos加法公式给平方和。
(3.4)的有限ODE使形式graph span除radical后至多二维，故其平滑积分D_g可以在
该有限维空间直接定义；阈值rank1不代表零点ordinary trace重数从2降为1。
所有这些源的P/Π/M正性已由562/563支付，不从n_c≥0反推P≥0。
新比较是同一完整Π同时给positive graph-pair intersections与失效的primitive signature，
不是重新证明连续RH相变。

### 完整连续平移/transpose代数也能同时通过两段

(3.2)可无改动扩到t∈R，仍只在n的非负实参数上取值。定义

\[
 T\Gamma_t=e^t\Gamma_{-t},\quad TF_1=F_2,\ TF_2=F_1,
 \qquad S_r\Gamma_t=\Gamma_{t+r},\ S_rF_1=F_1,\ S_rF_2=e^rF_2.
\]

直接计算得T²=I、I(Tx,Ty)=I(x,y)、I(S_rx,S_ry)=e^rI(x,y)。
对v_t=E_t，有Tv_t=v_{-t}，e^{-r/2}S_rv_t=v_{t+r}。
这些是精确对偶/归一化平移关系，两段都成立；它们没有正性结论。

另取有限支撑group algebra C[R]，基Γ_t，乘法Γ_t∘Γ_s=Γ_{t+s}，
反线性transpose Γ_t^*=e^tΓ_{-t}；degree characters为d1(Γ_t)=e^t、d2(Γ_t)=1。
以已给source定义trace

\[
 \sigma(\Gamma_t)=e^t+1-I(\Gamma_t,\Gamma_0)
                  =e^{t/2}W(t).
\]

其*对称性、trace循环性及degree的互换均直接成立，且

\[
 \sigma(\Gamma_t\circ\Gamma_s^*)
 =e^t+e^s-I(\Gamma_t,\Gamma_s)=-I(D_t,D_s).              \tag{3.6}
\]

证明中e^sI(Γ_{t-s},Γ0)=I(Γt,Γs)也在t<s时成立，不能省掉负参数的e^min因子。
用单位化基u_t=e^{-t/2}Γ_t，得到u_t^*=u_{-t}、σ(u_t)=W(t)、
σ(u_tu_s^*)=W(t−s)。所以smearing后的σ(AA*)恰是完整Q_W。
有限ODE允许本族在有限秩quotient逐项积分，不涉及无控group-algebra completion。

这强化了反测试：一整套graph pairing、精确transpose、scaled flow、degree characters、
commutative correspondence composition和完整trace/source identity，都可在非pure段存在。
缺失的是trace的*正性，或能独立证明它的section/effectivity/RR机制。
这不是Hilberdink–Lapidus任意Mellin对象都有该代数的定理，也没有生产实际scheme或截面。

## 4. lattice真反例的整数检验与RR所承担的实际责任

对于曲线型Z=P(T)/[(1−T)(1−qT)]，点数全递推及g给(2.3)；
即使没有真实几何，也能形式定义Γ_n和fiber配对。真正F5例N1=9、g=1给

\[
 -(D_iD_j)_{i,j=0,1}=\begin{pmatrix}2&-3\\-3&10\end{pmatrix},
 \qquad\det=11>0.
\]

290的q=5,N1=1、g=1模型则给

\[
 -(D_iD_j)_{i,j=0,1}=\begin{pmatrix}2&5\\5&10\end{pmatrix},
 \qquad\det=-5.
\]

取整数primitive divisor symbolD=2D0−D1，有

\[
 I(D,D)=2>0.                                           \tag{4.1}
\]

这是完全整数的最小反测试；没有使用α或β的值。等价degree多项式
m²−5mn+5n²在(m,n)=(2,1)取−1。真F5的同向量energy=30>0。
本次用标准库整数独立复算了这两个Gram、det及向量值；这是有限代数核验，
全n Euler正整数、FE、formal HL/PD及对应源责任来自290的原证明，而非本复算。

### RR增长条件是合法充分接口，但存在性不能自动当输入

本节的RR/section迁移责任已见363§5，不登记为本次新机制。

对任一真实或源构造的primitiveD，假设有独立定义的非负section/cohomology quantities
h_i(n,D)，且所有整数n→∞有

\[
 \chi(n,D)=h_0-h_1+h_2
 =\frac12 n^2 I(D,D)+o(n^2),\qquad
 h_0(n,D)+h_2(n,D)=o(n^2).                              \tag{4.2}
\]

因为χ≤h0+h2，立刻I(D,D)≤0。若I(D_g,D_g)=−Q_W(g)，就得Weil正性。
在(4.1)负例，χ=n²+o(n²)，所以(4.2)必有一项失败：
even quantities至少二次增长、h1变负，或Euler/source identity不成立。
连续负段(3.5)给相同严格障碍。

(4.2)作为抽象“存在这些数量”是强度未减少的证书包；不能令h1=−χ、
在欲证χ≤0后截断定义h_i，或用Q本身制造section空间。真正新输入必须是：
从同一算术/解析对象定义spaces、证明维数/entropy非负，独立付Euler系数以及边界增长。
它允许一般分析section量而不要求曲线或离散分布，但这些基本性质也不由positive P自动推出。

更贴近原始几何的RR入口不必预设h2的小量：用共同canonicalK、有限l(2K)、
非零section乘法的注入性、primitive度数导致l(±nD)≤1，再用RR迫使l(K±nD)
同时二次增长，乘法将其注入固定H0(2K)而矛盾。这里有额外的共同乘法结构和固定空间；
两个独立toy spaces不足。这个来源比未知H/CM更具体，但经典ζ上尚没有这样的
同源section algebra、RR与完整Γ/pp/pole交数身份。

## 5. 最广合法延伸及明确停止门

bare正P/Π/M+宽Mellin双对象对偶的全体不可能有统一pure定理，
因为连续负段和290同时属于这个宽类。可以一般化的是“同源的独立index来源”，
而不是把所有positive counting systems命名为polarizable。

可保的无限维/连续延伸是：

1. 先固定natural completion、全部Γ/pole/contact及预定分次权，定义完整W。
2. 从算术分布和对偶构造真实correspondences、section algebra或另一独立能量载体；
   对分布奇性使用smearedD_g，不能把经典W的finite-part/atoms强行当连续point-kernel。
3. 独立证明RR/section multiplication/effectivity/degree增长中的index来源。
4. 证明所有compact g的同源I(D_g,D_g)=−Q_W(g)，及所需continuity/limit。

这是一个可容纳continuous、lattice、nonlattice与graded系统的充分框架，
不是“最大的数学范畴”已被唯一刻画，更不是所有g-integers的已证定理。
相应Hilbert/GNS商可在正性之后完成，但faithful trace/determinant、原Frobenius半单
或普通heat trace另需责任；本稿不由商空间rank推这些结论。

一般数域理想计数只有正Euler与完整显式公式，没有共同全局Frobenius图和曲面index来源；
逐个有限素数的local positivity不足以替代这个跨处global结构。
经典源特别包含−Λ(n)/√n δ_{±logn}、Gamma finite-part和完整双pole。
(3.2)的Γ=0 smooth模型不覆盖它；(2.4)的logq周期模型也不能未经transport直接逼近它。
若使用source-defined smeared intersection，这条identity可以定义出来，却仍欠独立section/index证明。


### 经典源的off-diagonal coincidence测度：正性同样不够

由563已付的完整Γ/pp/pole式直接恢复，在u>0、避开原点时，

\[
 W_\zeta=2\cosh(u/2)\,du
 -\frac{e^{-u/2}}{1-e^{-2u}}\,du
 -\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\delta_{\log n}. \tag{5.1}
\]

这里系数是w(u)/2，不能误写成w(u)；全R偶延拓已承担另一半。故pole background减W的
正侧测度为arch+prime，乘e^{u/2}得到raw coincidence measure

\[
 d\mathcal N_\zeta(u)=\frac{du}{1-e^{-2u}}
                    +\sum_{n\ge2}\Lambda(n)\delta_{\log n}. \tag{5.2}
\]

它在每个[ε,R]上局部有限且正，但原点附近arch密度~1/(2u)，质量无限。
因此(3.2)不能原样用于经典point-graphs：对角Γ_t²无有限值，Γ接触项/finite-part必须付。
可以先对g,h作平滑，按fiber−Q定义formal intersection；若g,h非负且支撑正距离分离，
contact/diagonal项消失，(5.2)确给正的off-diagonal pairing。
然而所有不相交有效测试之间的这种正号，并不约束同一测试的renormalized自交。
这与(3.4)中两段均有positive graph-pair intersections而primitive index不同的反测试一致。
(5.1)–(5.2)是563完整公式的直接强旧推论，不另登记为经典新算术正性。

当前最具体的下一准入物是一个实际section/multiplication构造及其Euler quadratic coefficient，
或新的经典完整Γ/pp/pole恒等式。若仅“存在RR量/正H/正K/完整CM”，则停止该门；
不再用同一个抽象正性改名延长预算。此次source test可以结算构造检验，但不能改变
宏观完成门或声称经典实际正性的瓶颈已解除。
