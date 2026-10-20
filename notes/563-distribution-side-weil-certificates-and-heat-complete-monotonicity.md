# 563. 从分布侧认证Weil正性：守恒能量、完整热变换与算术检验

2026-10-20，C026；固定G20261014／0c4f≤538。用户要求从一般g-integer分布独立检验，
不预设零点位置。本稿给强而可核的有限证书及准确的一变量判据，明确经典应用仍欠什么。
一般来源恢复不冒称新外部首创；同一合同统一结算，不按三个原稿／工具／推送计轮。

## 1. 先固定完整对象，再区分证书与等价改写

log变量u≥0上，P为positive primitive，Π=Σk⁻¹(T_k)_*P保全部powers，M=exp_*Π；
右半平面先用加权variation保证Z(s)=exp∫e⁻ˢᵘdΠ存在。
指定同一completion、中心c0和全部Γ／pole后，才能从原始算术数据定义完整线性分布W。
其Weil二次型为

\[
 Q_W(g)=W(g*g^*),\quad g^*(u)=\overline{g(-u)},
 \qquad g\in C_c^\infty(\mathbb R;\mathbb C).                 \tag{1}
\]

不能任意改Gamma／删pole以便正性。用562的整个阶／竖带／完整反射除子前件，
同一W的全部compact正型即推出相关零点居中；本稿不重复把该等价当独立机制。

“不预设零点”有两种强度：
* 用prime／Gamma表达定义一个全阶正性条件，它可以在逻辑上仍等价于RH；
* 给有限可核矩阵、递推和完整分布身份，由精确代数推出全源平方和。
本轮真正的证书是第二种；它很窄，不能由一般正P／N自动保证。

## 2. 非循环充分条件：完整分布的守恒能量实现

设p为次数d的首一多项式，原始分布满足全域线性身份p(∂)W=0。
从其系数及初始数据独立给有限矩阵C、G=G*≥0、向量v，并核

\[
 p(C)=0,\quad C^*G+GC=0,\qquad
 W^{(k)}(0)=v^*GC^kv\quad(0\le k<d).                       \tag{2}
\]

则分布ODE先保证W解析及初值有意义；唯一性给

\[
 W(u)=v^*Ge^{uC}v,\qquad
 Q_W(g)=\left\|\int g(u)e^{uC}v\,du\right\|_G^2\ge0.        \tag{3}
\]

证明不使用零点：把ODE写成一阶companion系统，乘e⁻ᵘᴬ后导数为0，得到唯一解析解；
C*G+GC=0保内积，展开(1)即得(3)。G有核时用C不变的kerG作商，只支付正型，
不自动保普通trace重数。有限核验包括矩阵恒等式、主子式及d个初值；
另须证明**整个分布**的ODE，而非在删掉原子／原点后成立或有限数据拟合。
详见[证书原稿§2](../reviews/2026-10-20/grh-distribution/independent-analytic-certificates.md)。

有限可检验不等于逻辑上弱于RH。在已知有限递推类里，这类证书可能与谱稳定等价；
其价值是正性可以由输入数据的有限精确运算支付，而非“假设所有零点已居中”。

## 3. 连续正反分布的真实区分力

562的Z_c=1+c/[s(s−1)]、0<c≤1/2已付正continuous P／Π／M和
N_c=1+c(x−1−logx)。不再从其根读正性，而从实际系数递推
S_0=2、S_1=1、S_m=S_{m−1}−cS_{m−2}构造指数母函数H_c。
完整双pole−全部Π平衡直接给

\[
 W_c''+(c-1/4)W_c=0,\qquad W_c(0)=2,\ W_c'(0)=0.          \tag{4}
\]

偶延拓在0无额外δ，(4)确为全D'身份。置d=c−1/4，取

\[
 C=\begin{pmatrix}0&1\\-d&0\end{pmatrix},\quad
 G=\operatorname{diag}(d,1),\quad v=\sqrt2(0,1)^T.          \tag{5}
\]

(2)的等式直接成立，G≥0恰在c≥1/4；故正段无需读取零点即获(3)。
阈值商空间一维仍给2|∫g|²，不能代二重零点的二维trace空间。
反段W=2cosh(ru)，r²=1/4−c，取实奇g=uφ_even、φ≥0非零，则Q<0。
正P、正M、极强N误差和裸FE在两段都成立，所以均不是足够的独立正性条件。

有显式余量时可吸收误差：若原分布精确等于aδ0+K(u)du+ν，
K已有正能量证书、ν为Hermitian有限测度且||ν||TV≤a，则

\[
 Q_W(g)\ge(a-\|\nu\|_{TV})\|g\|_2^2+Q_K(g)\ge0.           \tag{6}
\]

只用|(g*g*)(u)|≤||g||₂²。每个R的局部版本也可用，但须所有R均独立支付，
有限秩K没有全L²正gap，不能无正余量就靠“小误差”传正性。

## 4. 热条件的精确答案：全正值不够，完全单调确切够用

假设完整W实偶，且存在a,C,m使
|W(h)|≤CΣ_{j≤m}sup e^{a|u|}|h^(j)(u)|，在超指数下降测试上连续。
这是可由源增长检验的有限指数阶前件，不偷设tempered或零点位置。定义

\[
 k_t(u)=(4\pi t)^{-1/2}e^{-u^2/(4t)},\quad
 \Theta_W(t)=W(k_t),\qquad t>0.                            \tag{7}
\]

全部Gamma finite-part、proper powers和pole都先相加，再作(7)。则

\[
 Q_W\ge0\text{ 于全部complex compact源}
 \iff (-1)^n\Theta_W^{(n)}(t)\ge0\quad(\forall n\ge0,t>0).
 \tag{8}
\]

正向由Bochner–Schwartz及ν=(ξ↦ξ²)_*σ，Θ=∫e⁻ᵗλdν。
反向由Bernstein得到ν≥0。w_t=W*k_t为偶整个函数，热方程给
w_t^(2n)(0)=Θ^(n)(t)，而∫cos(x√λ)e⁻ᵗλdν也是整个函数且Taylor系数全相同。
故w_t是正型；t↓0时在D'收敛，闭锥传正型至W。
Gaussian非compact配对、全部导数和极限均由上述指数阶界支付。
实偶不可省：带相反有符号原子权的Hermitian非偶谱可能有完全单调热量，仍非正型。
完整证明见[热原稿§1–3](../reviews/2026-10-20/grh-distribution/heat-stieltjes-and-weil-positivity.md)；
Bernstein正表示核[原书Theorem1.4](https://api.pageplace.de/preview/DT0400.9783110215311_A15706968/preview-9783110215311_A15706968.pdf)。

这给一变量的**等价**检验，尚非独立经典正性来源。若要成为证书，须从源算出ν≥0的表示，
或独立证明全部交错导数；有限t／有限n／数值采样不够。
同理，热位移后R_ε(x)=∫₀∞e⁻ˣᵗΘ(t+ε)dt的正Stieltjes表示可作证书，
但仅正轴上R_ε>0不是该条件，也不能忽略Γ的紫外端。

连续族在源侧精确给

\[
 \Theta_c(t)=\begin{cases}2e^{r^2t},&c<1/4,\\
                         2e^{-\tau^2t},&c\ge1/4.
             \end{cases}                                  \tag{9}
\]

所以**所有热时间的正值仍不足**：反段第一次导数即破坏CM。
正段ν=2δ_{τ²}是从算术代数身份付出的证书；连续谱log混合给区间上的正ν，
也通过(8)，但其完成对象有分支、失败严格C1，热条件不把它修成entire零除子。

还须避免把安全Euler半平面的CM偷换成(8)。只要Π≥0，logZ、−Z'/Z的交错导数
自动有符号，正反段都满足。更朴素的background−prime Laplace CM甚至无条件失败：
旧041的F(s)=1/(s−1)−(−ζ'/ζ)(s)有含负prime atoms的唯一逆Laplace测度。
右移或等距采样不消除负原子。这是[041§3](041-euler-bessel-cancellation-no-go.md)强旧恢复，
不另计新结果，也不否完整Gaussian变换(8)。

## 5. 函数域：从点数／递推到全周期平方和的有限证书

曲线C/F_q的N_n=#C(F_{q^n})、亏格g给a0=2g、
a_n=q⁻ⁿ/²(qⁿ+1−N_n)，a_−n=a_n。令L=logq，有理性与FE先识别

\[
 E(s)=q^{g(s-1/2)}P(q^{-s}),\qquad
 W_C=L\sum_{n\in\mathbb Z}a_n\delta_{nL}.                  \tag{10}
\]

完整原点质量与全部周期pole见[算术原稿§1](../reviews/2026-10-20/grh-distribution/arithmetic-counts-and-conservative-realizations.md)。
若从精确递推核U、H>0满足U*HU=H及a_n=TrU^n，则设
B_y=Σ_k g(y+kL)U^k、V^{*_H}=H⁻¹V*H，直接分段换元给

\[
 Q_{W_C}(g)=L\int_0^L\operatorname{Tr}(B_yB_y^{*_H})dy\ge0. \tag{11}
\]

这是全部complex compact源及全部周期副本的平方和，不使用零点或单个fundamental strip。
U与H的有限关系须配全次数递推；有限个Toeplitz主块或有限点数拟合不能支付尾部。

具体E/F5: y²=x³+x+1，含infinity直接数得N1=9。
Riemann–Roch有理性及g=1的FE给P(T)=1+3T+5T²，不使用Hasse界。
取

\[
 A=\begin{pmatrix}0&-5\\1&-3\end{pmatrix},\quad
 H=\begin{pmatrix}1&-3/2\\-3/2&5\end{pmatrix},\quad
 A^THA=5H,\quad\det H=11/4>0,\quad U=A/\sqrt5.             \tag{12}
\]

全n的trace递推S_n=−3S_{n−1}−5S_{n−2}由Cayley–Hamilton支付；(11)因此成立。
[精确脚本](../scripts/grh_distribution_certificate.py)还独立枚举N2=27、N3=108，
用Fraction核(12)，没有浮点／零点输入；全次数责任仍来自有理性，非有限枚举外推。
这是已知函数域正性的具体认证，不冒称新的一般Weil证明。

一般函数域可有几何度数／correspondence正性给独立能量；模1结论本身不自动给
指定原Frobenius半单或正内积。退化半正H商也不能免费保trace重数。
有理性、Hasse几何输入的原始范围核[Milne pp.1–3](https://jmilne.org/math/xnotes/pRH.pdf)。

## 6. 数域与经典ζ：具体缺口，而非把条件换名

数域ideal primitive正性、理想范数标签、判别式／Γ_R／Γ_C和FE给完整源，
没有给(2)、(5)或(8)的独立正性。一般数域RH仍未证，不能标成这些证书已通过。

经典完整分布含−Λ(2)/√2 δ_{±log2}，而Gamma与pole在log2旁光滑。
有限齐次常系数ODE的所有分布解却解析，所以(2)的直接有限类不覆盖经典ζ。
Gamma在0还有finite-part的−1/(2|u|)穿孔核，非局部有限Radon测度，
因此“有限能量光滑核+aδ0+有限TV残差”也不能直接等于它。
这些只排明确直接类；保无限维、unbounded正能量、平滑后证书与严格分布极限。

可以严格执行的扩展是：从源给完整正型W_j，并证W_j→W于D'，则(1)逐测试传正性。
但闭性已在562支付，真正未付的是**相同Gamma／全部properpowers／pole／原点接触项**
的身份与收敛。未知正G、未知误差支配、未知determinant收敛都不能由重命名视为已证。
旧174已明确GNS／紧致性只补全已有正性，560则留下actual K_L符号／相对费及成长core。

对经典ζ，现在可以精确表述最小未付箭头：

令Γ0=ψ(1/4)−logπ、w(u)=2e⁻ᵘ/²/(1−e⁻²ᵘ)。不引用零点即可逐源计算

\[
 \Theta_\zeta(t)=2e^{t/4}+\frac1{\sqrt{4\pi t}}
 \left[\Gamma_0+\int_0^\infty w(u)(1-e^{-u^2/(4t)})du
 -2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}e^{-(\log n)^2/(4t)}\right].
 \tag{13a}
\]

积分差分保留Gamma的原点finite-part，求和保全部prime powers，2eᵗ/⁴是完整双pole。
每个固定t>0及有限阶导数的尾可由Gaussian和Λ(n)≤logn控制；
能计算这些值不等于已证所有t、所有阶的符号。所欠的是从(13a)独立推出

\[
 \text{实际prime/Gamma/pole数据}
 \ \Longrightarrow\ \Theta_\zeta(t)=\int_0^\infty e^{-t\lambda}d\nu(\lambda),\quad\nu\ge0,
 \tag{13}
\]

或同强度的独立完整正能量／全源平方和身份。不能令ν=Σδ_{γ²}并先假设γ实来支付。
在这个实偶全域类，(13)存在性本身仍等价；需要的是其算术来源证明。

## 7. 净后果、测试与停止范围

| 候选／测试 | 连续正段 | 连续离线段 | 函数域 | 数域／经典 |
|---|---|---|---|---|
| 正primitive／强N正则／裸FE | 成立 | 同样成立 | 可有 | 不付RH |
| 所有热量Θ>0 | 成立 | 同样成立，故不足 | 非平凡部分成立 | 不能代PSD |
| 完整热量全CM | 成立 | 一阶即失败 | 几何／能量证书可付 | 未独立支付，等价责任 |
| 精确递推＋正H守恒＋完整W身份 | ODE证书通过 | 同对象负测试排除 | 圆周证书及(11)通过实例 | 直接有限类不覆盖；无限维修复open |

相对562，新输出是输入数据到全源正性的有限认证机制、准确热接口与算术lift测试；
不把已付连续平方和／标准Bernstein／旧041／174／闭锥再次结算。
本门统一一次后停止，未改善actualζ强旧542+555→557 whole4/5、成长K/core/coupling或faithful Ξ。
长期Goal门仍open；下一步若只有未知正性改名或更多玩具例，不准入新数学合同。
