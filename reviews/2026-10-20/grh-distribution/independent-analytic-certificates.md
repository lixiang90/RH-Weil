# 分布侧的独立充分证书：有限正能量实现、连续相变与经典 Γ 的范围边界

2026-10-20。独立研究原稿；只消费562已闭合的 positive primitive／全部 powers／pole 身份，
不修改公共 STATE／cadence／Git。固定 G20261014 与0c4f≤538基线。
这里证明的是一种可以直接从**完整物理平衡分布**核验的充分证书；
不声称已为经典 ζ 找到该证书，也不把一般正型／Pick 等价重新命名成独立输入。

## 1. 输入对象和独立性的准确含义

在 log 坐标，先固定 positive primitive 测度 P，以及

\[
 \Pi=\sum_{k\ge1}\frac1k(T_k)_*P,\quad T_k(u)=ku,
 \qquad M=\exp_*\Pi,
 \qquad Z(s)=\exp\int_0^\infty e^{-su}\,d\Pi(u).
 \tag{1}
\]

所有交换先在一个指数加权总质量有限的右半平面进行。指定 completion、
Gamma 背景和**全部**极点后，以原显式公式定义线性分布 W∈D'(R)。
本稿始终取

\[
 g^*(t)=\overline{g(-t)},\quad Q(g)=W(g*g^*),\quad
 g\in C_c^\infty(\mathbb R;\mathbb C).
 \tag{2}
\]

若要从 Q≥0 推 RH，还须另有同一整个完成化对象 E 的完整显式公式、
有限竖带和增长前件，见562§3。下述证书本身只涉及 P／Π／Gamma／pole 所给出的 W，
不引用 E 的零点，也不由零点反向选择矩阵。它比“存在正谱测度”具体得多：
候选矩阵、有限数据及一个全分布恒等式必须能从输入独立算出。
若这最后一个身份尚未证，矩阵自伴与数值拟合均不构成证书。

## 2. 有限常系数 ODE 的正能量证书

**命题 A。** 设 p 为次数 d≥1 的首一多项式，W∈D'(R) 满足

\[
 p(\partial_t)W=0\quad\text{于整个 }D'(\mathbb R).
 \tag{3}
\]

给定有限矩阵 C∈M_m(C)、G=G*≥0 及 v∈C^m，并已核

\[
 p(C)=0,\qquad C^*G+GC=0,
 \qquad W^{(k)}(0)=v^*GC^kv\quad(0\le k<d).
 \tag{4}
\]

则 W 实际是解析函数

\[
 W(t)=v^*Ge^{tC}v,
 \qquad
 Q(g)=\left\|\int_{\mathbb R}g(t)e^{tC}v\,dt\right\|_G^2\ge0
 \tag{5}
\]

对全部复值 compact g 成立，且误差为0。这里 ||x||_G²=x*Gx；G 可半正定。
若 G 有核，(4) 令 ker G 对 C 不变；在 C^m/ker G 上得到真正正内积及反自伴生成元。

**证明。** 对状态分布 Y=(W,∂W,…,∂^{d−1}W)，(3) 是 Y'=A_pY，
A_p 为 companion matrix。乘以光滑矩阵 e^(−tA_p)，得到导数为0的向量分布，
故该分布是常向量。这同时证明 W 解析、初值有意义及 d 个初值的唯一性。
令 r(t)=v*G e^(tC)v，p(C)=0 给 p(∂)r=0；(4) 及唯一性给 W=r。
由 C*G+GC=0 得 e^(tC)*G e^(tC)=G，因此

\[
 \langle e^{uC}v,e^{wC}v\rangle_G=W(w-u).
\]

将 (g*g*)(t)=∫g(u)overline{g(u−t)}du 代入，Fubini 在 compact 区间合法，
即得 (5)。全程没有谱位置假设。□

这个证书的有限部分是 exact 线性代数：p(C)=0、Hermitian Lyapunov 等式、
G 的全部主子式非负及有限初值。难度可能集中在 (3)，但 (3) 是**线性**的源侧分布身份，
可由显式密度或递推独立验证，并非对所有 g 重述 Q(g)≥0。
它是一个强而窄的充分类；不能由“对每个窗口拟合出一个矩阵”代替。

## 3. 连续 positive g-integer 相变的非循环检验

采用562已证的同一族

\[
 Z_c(s)=1+\frac{c}{s(s-1)},\quad 0<c\le\frac12,
 \qquad dM_c=\delta_0+c(e^u-1)du.
 \tag{6}
\]

其正 continuous primitive P_c 及所有 proper powers 已由562(3)–(4)核出。
记 d=c−1/4。为避免从任何零点位置推出正性，可以全用实系数递推：

\[
 S_0=2,\quad S_1=1,\quad S_m=S_{m-1}-cS_{m-2},\quad
 H_c(t)=\sum_{m\ge0}S_m\frac{t^m}{m!}.
 \tag{7}
\]

由递推 H_c''−H_c'+cH_c=0。完整 Π 的密度满足

\[
 q_c(t)=\frac{e^t+1-H_c(t)}t\quad(t>0).
 \tag{8}
\]

保留两个 pole 0、1 且 Gamma=0，从**算术平衡**直接算得

\[
 W_c(t)=2\cosh(t/2)-|t|e^{-|t|/2}q_c(|t|),
 \qquad W_c''+dW_c=0,
 \quad W_c(0)=2,\quad W_c'(0)=0.
 \tag{9}
\]

其中 t>0 时 W_c=e^(−t/2)H_c；其右导数在0为0，偶延拓无额外 δ，
所以 ODE 是整个 D'(R) 的身份，不只是去掉0后的微分等式。
正性证书选

\[
 p(\lambda)=\lambda^2+d,\quad
 C=\begin{pmatrix}0&1\\-d&0\end{pmatrix},\quad
 G=\begin{pmatrix}d&0\\0&1\end{pmatrix},\quad
 v=\sqrt2\begin{pmatrix}0\\1\end{pmatrix}.
 \tag{10}
\]

p(C)=0 和 C*G+GC=0 由乘法直接核验；前两个初值是2、0。
**G≥0 恰在 c≥1/4**，故命题 A 不查询 Z_c 的零点即给完整 Weil 正性。
阈值 d=0 时 G 有核，在一维正商空间上仍给 Q=2|∫g|²；
这不是完成化二重零点的 trace 空间，重数接口仍须另核，不能重犯562的标量 L² 权误读。

若 d>0、τ=√d，(5) 展开为

\[
 Q_c(g)=2\left|\int g(t)\cos\tau t\,dt\right|^2+
        2\left|\int g(t)\sin\tau t\,dt\right|^2
       =|\widehat g(\tau)|^2+|\widehat g(-\tau)|^2.
 \tag{11}
\]

反段 c<1/4 时 d=−r²，(9) 唯一解为2cosh(rt)。取实奇 g=tφ(t)，
φ 为非零非负偶 compact 光滑函数，则

\[
 Q_c(g)=-2\left(\int g(t)\sinh(rt)\,dt\right)^2<0.
 \tag{12}
\]

这同时排除了任何满足 (3)–(4) 且保持同一 W_c 的替代正能量证书；
不能仅称本次选取的 G 失败就排除所有 G，但实际负测试已经给更强结论。
也可以用正能量实现必有 |W(t)|≤W(0) 而 cosh 无界作有限实现的独立反证。
positive P、positive M、N(x)=cx+O(log x) 及裸 FE 在两段均成立，
故它们不能独立代替正能量符号条件。

## 4. 可付误差的版本，以及它没有自动解决的责任

**命题 B。** 给定 a≥0、一个命题 A 的正能量核 K，以及 Hermitian 有限复测度 ν，
若独立核出完整分布身份

\[
 W=a\delta_0+K(t)dt+\nu,\qquad \|\nu\|_{TV}\le a,
 \tag{13}
\]

则全部 complex compact g 有

\[
 Q(g)\ge(a-\|\nu\|_{TV})\|g\|_2^2+
          \left\|\int g(t)e^{tC}v\,dt\right\|_G^2\ge0.
 \tag{14}
\]

证明只用 |(g*g*)(t)|≤||g||₂²；不存在频率截断或未计补空间。
对一个固定 R，只须 (13) 在(−2R,2R)上成立且用该区间的 TV 范数，
即可覆盖 supp g⊂(−R,R)。如果对**每个** R 都能独立付费，则覆盖全部 compact 测试；
不要求不同 R 的矩阵相同，但不能只核有限多个 R。

这是严格的“显式正余量吸收误差”版本。若只把 a 改名成未知的实际底谱，
或 ν 的 TV／算子范数只是待证的全源不等式，则没有新增分析输入。
特别是有限秩 K 在无限维测试空间上没有全 L² 强制正下界；
不能无 aδ0 的余量便凭“小误差”保正性。
若只知 K_n→W 于 D'(R) 且每个 K_n 已通过独立证书，则562的闭锥论证给 Q≥0；
真正的新责任是构造这些**完整、同对象** K_n 并核这种分布收敛。

## 5. 经典 ζ 与数域：为何这个直接有限证书不适用

经典完整物理分布具有精确组成

\[
 W_\zeta(h)=W_\Gamma(h)
  -\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}[h(\log n)+h(-\log n)]
  +\int_{\mathbb R}2\cosh(t/2)h(t)dt.
 \tag{15}
\]

每个 compact h 只见有限多个 prime powers；原 du／Fourier 约定下
Γ(ξ)=Re ψ(1/4+iξ/2)−log π，即 actual 2θ'，没有除掉全部 proper powers。
由 [NIST DLMF 5.9.16](https://dlmf.nist.gov/5.9#E16) 的 digamma 积分，减去 ξ=0 后换元可得

\[
 \Gamma(\xi)-\Gamma_0=\int_0^\infty w(a)(1-\cos\xi a)da,
 \quad w(a)=\frac{2e^{-a/2}}{1-e^{-2a}},
 \quad \Gamma_0=\Gamma(0),
 \tag{16}
\]

从而

\[
 W_\Gamma(h)=\Gamma_0h(0)+\int_0^\infty w(a)
       \left[h(0)-\frac{h(a)+h(-a)}2\right]da.
 \tag{17}
\]

(17) 在0由二阶 Taylor 差分收敛，∞由 w 衰减收敛；给同一闭型域 Dlog 的 Γ，
不是可随意替换的模型背景。精确原域与 Γ 正跳证明已在543§2消费，不另计新资产。

有两个直接范围障碍。

1. 在 t=log 2 旁，Γ 核与 pole 核光滑，而 (15) 有非零的负 δ 原子。
   任意有限常系数**齐次** ODE 的分布解均解析；故 (15) 不可能满足命题 A 的 (3)。
   数域也有素理想 norm 的负原子及 archimedean 项，直接有限 ODE 同样不适用。
   这不排除无限维正能量系统，也不排除先平滑再作正实现与合法极限。
2. 在一个不含非零 prime-power 点的0邻域，(17) 的离0核是
   −w(|t|)/2∼−1/(2|t|)。它的总变差在任意0邻域发散，
   而 δ0 无法抵消穿孔邻域的发散。因此 W_ζ 在0附近不是局部有限 Radon 测度。
   这排除“有限正能量核+aδ0+有限 TV 残差”直接等于经典 W_ζ 的版本。
   即使删除全部 prime 原子，Γ 仍保留此障碍。

这些是对本证书类的范围检验，不是对一般独立正性路线的不可能定理。
正型分布可以奇异且具有无限谱；Γ 的正跳部分本身给无限维非局部能量。
经典应用需要新的是：一个允许这类奇性／无限秩、又能把**同一** negative prime powers
与全部 poles 耦合的正能量或 Gram 身份；或者从独立正对象到 (15) 的全 D' 逼近。
只说“Γ 是正跳核”仍没付 Γ0、prime subtraction、odd pole 的共同符号。
560已给每 fixed L 的 positive trace−compact error+双pole桥，
其中剩余 K_L 的全源符号／相对费及成长控制正是未付责任，不能用“能量实现”改名消去。

数域的 Γ_R／Γ_C 背景及理想范数标记均须留在该共同身份中。
positive ideal P、解析延拓及 FE 并不已知给一般数域的 G／全域正比较；
否则已经证明相应数域 RH，不能把数域误列为证书已验证正例。

## 6. 函数域检验的正确离散版本

曲线的完整 s-plane 分布也不是有限解析 ODE 核：周期谱 lift 在物理 log 轴上产生 Dirac comb。
因此应先在 Z／频率圆周上工作，而非声称命题 A 在 R 上直接覆盖它。
令 L=log q、a0=2g，n≥1 时

\[
 a_n=\frac{q^n+1-\#C(\mathbb F_{q^n})}{q^{n/2}},\quad
 a_{-n}=\overline{a_n}.
 \tag{18}
\]

若由点数／递推独立给有限矩阵 U、G>0 并核 U*GU=G，以及
a_n=Tr(U^n)（这里的 trace multiplicity 必须与 a0 相符），
则对任意有限复序列 z_n 有

\[
 \sum_{j,k}a_{j-k}z_j\overline{z_k}\ge0.
 \tag{19}
\]

证明：G^(1/2)UG^(−1/2) 为 unitary，矩阵多项式的普通 Tr(B*B)≥0。
这条有限矩阵等式不输入特征值位置，且 trace 自动保重数。
若只核有限多个 a_n，还需 exact recurrence 将身份传播到全部 n；
单个有限 Toeplitz 主块 PSD 不足以推出 (19)。
到实线的完整 lift 是

\[
 W=L\sum_{n\in\mathbb Z}a_n\delta_{nL},
 \tag{20}
\]

对应全部周期零点，而不是只保一个 fundamental strip。若从 point counts 出发，
(18) 中 q^n+1 正是完整 periodic polar subtraction，不能只保 s=0、1 两个极点。
本稿不把“存在这样的 G”当作从任意点数序列自动得到；
一般曲线的独立存在性须由几何正极化／Weil定理等另付。
root 的函数域具体案例将独立核该 G、点数递推和 (20)，本稿不替代它的消费。

## 7. 本原稿可消费的新增和停止范围

* 已证明：全分布 ODE＋有限可核正能量矩阵＋初值匹配 ⇒ 全 complex compact Weil 平方和；
  semidefinite G 的 quotient 处理、阈值、完整误差 TV 余量均列明。
* 已实际验证：562连续正／反族中，源侧递推判 c≥1/4，反段有明确负测试。
  这是一个非循环适用类的证书展示，不宣称经典 ζ 的净输入或文献首次。
* 已排本证书的错误直接应用：经典／数域原子和 Γ 的 finite-part 奇性，
  函数域实线 comb；保无限维、离散圆周、平滑及有控 full D' 极限的合法修复。
* 仍未付：经典 (15) 的独立无限维平方和／全源有符号比较，以及原自然算子域和 faithful Ξ identity。
  actual whole leading4/5、成长 core／K_L／coupling 均不变；不完成长期 Goal。

本稿没有把“正型核分解存在”当作从分布可自动算出的结论。
下一步若只有未知 G／未知 full residual inequality 的重述，没有同对象新数据或可核反例，便停在此范围。
