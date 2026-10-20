# 562. 一般 g-integer 的类 RH：连续正例、Weil 判据与带重数自伴谱

2026-10-20，C025，固定G20261014文件目标／0c4f≤538。由用户明确扩大问题范围。
561的单位gap／固定Fourier整数梳分类只是一种特殊识别结果，不作为一般类RH的定义。
本稿的模型／判据／算术原件及连续谱边界补件分别逆审并由root消费；不声明外部首创，不宣称经典RH进展。

## 1. 一般对象与三个层次的广义RH

在log坐标u≥0，以正局部有限测度P表示primitive g-primes，Π表示全部prime powers，
M表示g-integers：

\[
 \Pi=\sum_{k\ge1}k^{-1}(T_k)_*P,\quad T_k(u)=ku,
 \qquad M=\exp_*\Pi,\quad
 Z(s)=\int e^{-su}dM(u)=\exp\int e^{-su}d\Pi(u).
 \tag{1}
\]

先在指数权总质量有限的右半平面定义；一般signed distribution须另外给卷积指数存在性。
同一范数的不同生成元标签和重数保留，不能把理想范数等多重集改成无重数集合。

**没有指定completion／对偶时**，合理的一般RH型性质是一侧界：在实际延拓域内无零于Re s>c0。
中心c0必须由固定单位化／背景指定，不能从可随意放宽的N误差指数猜定。
无FE时，该条件不推出所有零点都在边界；计数误差的等价还须增长与Tauberian等额外前件。

**有固定完整反射对偶时**，令E(s)为完成后精确去极点／已知平凡因子的非零整个对象。
若全部相关零点在已知竖带，且除子关于R(s)=2c0−bar s闭合，
则右侧无零Re s>c0与全零点Re s=c0等价。反射本身不付后一结论。

**有同对象谱实现时**，才问具体中心化生成元在给定正Hilbert域上是否自伴、
是否涵盖全部零点／重数及无额外谱。后验按实零点造对角算子不同于独立构造自然算子。

还有一个比单线更宽的版本：有分次纯权的对象要求每个权分量的归一化特征值模为1，
整个zeta的零／极点可落在多条权线上，见§5。
这只是特征值／除子层的纯性；原始Frobenius可酉化还须核半单性、正内积及其相容性。

## 2. 连续正g-integers确有非空类RH：一个可完全核算的相变

对全体0<c≤1/2，取

\[
 Z_c(s)=1+\frac{c}{s(s-1)},\qquad E_c(s)=s(s-1)Z_c(s)=s^2-s+c.
 \tag{2}
\]

存在真正的正continuous primitive P_c，不只是正Π。具体令α+β=1、αβ=c，
A_m=1−α^m−β^m，C_m=Σ_{k≥1}k^{-m-1}，并取

\[
 dP_c(u)=p_c(u)du,\qquad
 p_c(u)=\frac1u\sum_{m\ge2}\frac{A_m u^m}{m!C_m}.
 \tag{3}
\]

c<1/4时α,β∈(0,1)，A_m>0是561旧段；c≥1/4时β=barα、|α|²=c，
A_2=2c>0，m≥3有A_m≥1−2c^{m/2}>0。统一取A_m≤3，
不能继承旧段A_m<1（例如c=1/2时A_3=3/2）。于是p_c>0、局部有限，
p_c(u)≤3(e^u−1−u)/u，所有σ>1指数权可积。

推前Jacobian和完整Euler重复度由正项Tonelli支付：

\[
 \sum_{k\ge1}k^{-2}p_c(u/k)
 =\frac{e^u+1-e^{\alpha u}-e^{\beta u}}u=:q_c(u),\qquad d\Pi_c=q_cdu.
 \tag{4}
\]

Frullani积分给∫e^{-su}dΠ_c=logZ_c(s)，Re s>1；分支从实s>1固定。
加权卷积指数总质量为exp(∫e^{-σu}dΠ_c)，Laplace唯一性再给

\[
 dM_c(u)=\delta_0+c(e^u-1)du,\qquad
 dN_c(x)=\delta_1+c(1-x^{-1})\mathbf1_{x>1}dx,
 \quad N_c(x)=1+c(x-1-\log x).
 \tag{5}
\]

primitive和g-integer非单位部分均在所有正开区间有连续正密度。
两个原始极点0、1全部保留，模型Gamma项为0；不把它称为经典Gamma完成化。
完整Weil线性平衡在h∈Cc∞(R)上是

\[
 W_c(h)=\int[2\cosh(t/2)-|t|e^{-|t|/2}q_c(|t|)]h(t)dt,
 \qquad Q_c(g)=W_c(g*g^*),\quad g^*(t)=\overline{g(-t)}.
 \tag{6}
\]

当1/4≤c≤1/2，令τ=√(c−1/4)。由(4)精确相消，不用零点假设即得

\[
 W_c(h)=\int2\cos(\tau t)h(t)dt,\qquad
 Q_c(g)=|\widehat g(\tau)|^2+|\widehat g(-\tau)|^2\ge0,
 \quad\widehat g(\xi)=\int g(t)e^{-i\xi t}dt.
 \tag{7}
\]

全部complex compact源均适用，误差为0。E_c的两个零点确为1/2±iτ；
τ>0时取D_c=diag(τ,−τ)于C²，有

\[
 E_c(1/2+iz)=\tau^2-z^2=-\det(zI-D_c).
 \tag{8}
\]

c=1/4时D_c=0于C²，E_c(1/2+iz)=−z²，完整重数仍为2。
c<1/4时W_c=2cosh(rt)，r=√(1/4−c)，取非零非负偶φ及实奇g(t)=tφ(t)，则Q_c(g)<0。

所以**同一正continuous P/N族中，c=1/4正好是中心线／Weil正型的分界**。
它非空零点、非空连续primitive，并非s/(s−1)的无零点真空例。
详细原证明及所有域见[连续模型原稿](../reviews/2026-10-20/grh-general/continuous-positive-rh-model-and-transition.md)。
这一范围新增于561的离线段；不尝试分类c>1/2，不声称文献首次。

## 3. 一个不输入整数的广义Weil判据

设E≠0 entire、阶≤1，全部零点在有限竖带，反射R保持完整正整数重数m_ρ。
对h∈S_exp（所有导数对任意指数权均有界），令

\[
 F_h(s)=\int h(u)e^{(s-c_0)u}du,
 \quad W_E(h)=\sum_\rho m_\rho F_h(\rho),\quad
 Q_E(h)=W_E(h*h^*)=\sum_\rho m_\rho F_h(\rho)\overline{F_h(R\rho)}.
 \tag{9}
\]

有限阶零点计数与竖带快速衰减付绝对收敛。则

\[
 \{\Re\rho=c_0\ \forall\rho\}
 \quad\Longleftrightarrow\quad
 \{Q_E(h)\ge0\ \forall h\in C_c^\infty(\mathbb R)\}.
 \tag{10}
\]

全compact测试包括任意支撑尺度，不是固定窗或有限组。
正向是Σm_ρ|F_h(ρ)|²。反向若ρ0与ρ1=Rρ0不同且阶m，取
G=E/((s−ρ0)^m(s−ρ1)^m)，再选一次L，使F=e^{(s−c0)^2}GL在两点取1、−1。
F在每条固定竖带快速衰减，逆变换h∈S_exp；(9)中其他零点精确为0，Q_E(h)=−2m。
零点竖带宽B给分部积分界

\[
 |F_h(\rho)|\le C_{B,N}(1+|\Im\rho|)^{-N}
 \sum_{j\le N}\sup_u e^{(B+1)|u|}|h^{(j)}(u)|.
 \tag{11}
\]

因此W_E连续于S_exp。光滑compact截断χ(u/R)h在全部S_exp半范数收敛，
卷积连续，某个有限R即保负。这支付compact分离，不偷换无限尾或测试代数。

将(10)用于一个g-integer，必须先把**同一个**物理平衡A_Γ−prime/power＋全部pole
在全部compact测试上精确识别为W_E；任意正kernel不能代此身份。
该一般判据是正确的RH等价组织，分离测试使用E，并未提供经典ζ的独立正性证明。

若使用乘法Mellin约定Mf(s)=∫f(x)x^s dx/x，则临界反演为
f^{sharp_c0}(x)=x^{-2c0}overline(f(1/x))；用户x^{-1}是c0=1/2的版本。
应先定义线性W，再对卷积平方定义二次Q。对所有f把线性式直接要求≥0会由f→−f迫其恒零。

## 4. 自伴、正谱测度和正确行列式之间差什么

全compact上的正型分布W由Bochner–Schwartz给正tempered测度σ，
Q(h)=∫|hat h(t)|²dσ(t)。GNS平移群为酉，Stone生成元是在最大域
{g∈L²σ:∫t²|g|²dσ<∞}上的实乘法Dg=tg。
这支付自伴性，但尚未支付它与原E的全部零点、trace重数及determinant的身份。

即使σ=Σm_γδ_γ，**标量L²σ每个原子只给一维本征空间**。
例如本族阈值σ=2δ0：L²σ一维，普通det(zI−D)=z，不能识别−E=z²。
必须使用K=⊕_γC^{m_γ}及D|_γ=γI，使Tr E_D=Σm_γδ_γ。
若D有compact resolvent、m0=dimkerD有限、非零谱部分D_perp^{-1}为Hilbert–Schmidt，
正确genus-one接口为

\[
 F(z)=e^{a+bz}z^{m_0}\det{}_2(I-zD_\perp^{-1}),
 \qquad F(z)=\eta E(c_0+iz)\text{ real-type}.
 \tag{12}
\]

必须独立识别F及规范a,b；Σm_γ/(1+γ²)<∞只付乘积收敛。
一个自伴连续谱算子可以合法存在，但连续σ不能成为非零entire函数的通常零点计数测度。
若改谈谱位移、相对determinant或branch cut，须给新的接口，不可继续逐支持点写整个零点积。

中心零点也不保证预先指定的source算子可酉化：F=z²既可由D=0于C²实现，
也可由非零nilpotent伴随矩阵实现；后者的Jordan链不容正内积自伴。
旧520/526的完整Jordan／域／norm责任不能由后验对角实现抹去。

在real-type阶≤1规范下，另有完全解析的等价判据

\[
 F\text{全实零点}\iff -F'(z)/F(z)\text{在上半平面全纯且虚部}\ge0.
 \tag{13}
\]

实genus-one积给虚部Σm_γ y/((x−γ)²+y²)及中心零项m0y/|z|²；
反向全纯先排上半平面零点，再由real-type排下半平面。
额外高次零自由因子会破坏(13)，如e^{z²}无零而−F'/F=−2z非Pick。
对经典Ξ，(13)仍等强RH；由正P的右半平面Laplace性不能免费推出该全上半平面不等式。

### 4.1 连续谱也能正，但通常要离开整个零除子框架

固定0<a<b≤1/2，取[a,b]上的均匀概率ν，令c_τ=1/4+τ²。
对已付正族作**对数混合**而非直接平均integer测度：

\[
 P_\nu=\int P_{c_\tau}d\nu,\quad
 \Pi_\nu=\int\Pi_{c_\tau}d\nu,\quad M_\nu=\exp_*\Pi_\nu,
 \qquad Z_\nu(s)=\exp\int\log Z_{c_\tau}(s)d\nu.
 \tag{14}
\]

(3)的参数一致正界支付Tonelli及所有σ>1的加权范数，所以primitive为正连续密度，
M_ν的非单位部分也绝对连续。一般M_ν并不等于∫M_c dν。
保模型全部双pole且Gamma=0，完整线性泛函W_ν的核为2∫cos(τt)dν，故

\[
 Q_\nu(g)=\int|\widehat g(t)|^2d\sigma_\nu(t),\qquad
 d\sigma_\nu(t)=\frac{\mathbf1_{[-b,-a]\cup[a,b]}(t)}{b-a}dt.
 \tag{15}
\]

σ_ν质量为2，D=t在标量L²σ_ν上有界自伴、全连续谱且无本征值。
这不意味着存在具有连续零集的非零整个函数：令F_ν(z)=−E_ν(1/2+iz)，
E_ν=s(s−1)Z_ν，相位须先由原Euler半平面（对应Im z<−1/2）固定。
在上半平面用各Log(z±τ)的标准支给

\[
 F_\nu(z)=\exp\int[\operatorname{Log}(z-\tau)+\operatorname{Log}(z+\tau)]d\nu,
 \qquad -\frac{F_\nu'}{F_\nu}=\int\frac{d\sigma_\nu(t)}{t-z}.
 \tag{16}
\]

后式是虚部正的Herglotz函数。若d=b−a，则它的导数为
d⁻¹[(z−b)⁻¹+(z+a)⁻¹−(z−a)⁻¹−(z+b)⁻¹]，在b的residue为1/d≠0。
单值亚纯函数的导数不可能有非零residue，故F_ν不能成为全平面单值亚纯函数。
端点有分支；不能把cut内点误称自然边界，也不能把σ_ν称为整个零点计数测度。
包含整条中心线的带内亚纯C1也失败，所以此例不是严格C1+C3的反例。

可以在交换代数的有限trace下定义局部log determinant，但那是新trace数据：
对任何σ_ν(B)>0，普通Hilbert projection trace Tr E_D(B)=∞，并非σ_ν(B)。
因此连续arithmetic可满足标准中心零点RH；连续spectral则可满足正型／自伴的更宽类RH，
其与zeta的接口必须明确容许分支／相对行列式。完整分支与加权证明见
[独立混合边界原稿](../reviews/2026-10-20/grh-general/continuous-spectral-mixture-boundary.md)。
本节是已付正族的直接混合后果，同C025不增轮，也不满足经典完成化的全部前件。

## 5. 数域、函数域和纯权的成员范围

数域K：在物理x轴上P_K=Σ_p δ_{Np}、N_K=Σ_a δ_{Na}保素理想／整理想标签，
是带重数的正离散g-integer系统；一般不是单位整数梳。
Λ_K=|D_K|^{s/2}Γ_R(s)^{r1}Γ_C(s)^{r2}ζ_K(s)自对偶，
相关RH一般未证，不能把已知FE说成已知C3。
此公式核Sutherland[Lecture19, Remark19.13](https://math.mit.edu/classes/18.785/2019fa/LectureNotes19.pdf)。

F_q上亏格g曲线：closed places的q^{deg v}和有效除子的q^{deg D}给lattice分布，
Z_C(T)=P_C(T)/((1−T)(1−qT))，P_C=∏(1−α_jT)。
Weil RH的|α_j|=√q意味着Z_C(q^{-s})零点1/2+i(θ_j+2πk)/logq。
因此**nonlattice不是类RH必要条件**。自然谱是归一化Frobenius酉相位；
实线自伴版本要保所有周期副本。核[Milne §0–1](https://jmilne.org/math/xnotes/pRH.pdf)。

函数域在整个s平面还有0和1的无限周期极点副本。
若Kimi的H严格只许两个有限秩缺陷，则这个包本身就漏掉函数域；
须在T变量／频率圆周上处理，或明确清除整个周期极点除子。

更高维光滑射影V的Weil–Deligne RH是分次纯性
Z_V(q^{-s})=∏_jdet(I−q^{-s}F_j)^{(-1)^{j+1}}、|α(F_j)|=q^{j/2}，
并非整个Z的所有零点都在同一条线。单线是固定纯权因子单位化后的特例。
这些纯权因子未必各自属于positive primitive子类；分次几何数据是另外的输入。
详细成员、归一化及来源见[数域／函数域原稿](../reviews/2026-10-20/grh-general/number-function-field-and-distribution-examples.md)。

## 6. C1–C5的裁决及真正的证明机制

| 条件 | 合法的修订 | 它单独没付什么 |
|---|---|---|
| C1 | 固定背景、完整延拓／除子、竖带及增长；整个积另需全局规范 | 带内亚纯不付全球Hadamard；finiteorder/genus并非同义 |
| C2 | 保精确反射／对偶身份及预先列明缺陷 | 给成对而非居中；不能任意删有限离线零点；多纯权须分级 |
| C3 | 线性W作用于全部complex卷积平方，独立平方和可作真正输入 | 对同完整E通常正是RH等价；不是普通P/N正性，也非任意OS正性 |
| C4 | 纯点整数重数、zero0因子、trace multiplicity与(12)精确身份 | 任意正σ、标量L²或无标定det不能支付原zeta识别 |
| C5 | 一种特定finite-to-global充分路线；需同一非零F的局部一致极限 | lowest simple/even不是普遍必要，有限Gram／低谱拟合不付目标determinant收敛 |

特别，Weil卷积正型的difference kernel和Osterwalder–Schrader半轴sum kernel不同：
本例2cosτt在前者给2(|C|²+|S|²)，后者给2(|C|²−|S|²)，可取C=0、S≠0得负。
所以“反射正性”必须先定含义，不能把OS与Weil当成同一公理。

C3加完整显式公式已经足以得(10)，C4是额外实现，C5是实现／逼近的另一条充分路线，
并非五条全部同时必要。若F_n全实零点且F_n→F≠0紧集一致，Hurwitz即保F全实；
不要求简单最低态。CCM的Theorem1.1确有其特定simple/even/边界前件，
而Ξ极限仍是[§7–8的缺失步骤](https://alainconnes.org/wp-content/uploads/zeta-spectral-triples-1.pdf)。

修正Q为W(f*f^sharp)后，在交换卷积代数中Q(f^sharp)=Q(f)本身自动成立，
因为f^sharp*f=f*f^sharp；这条Q对称不能另充当C2的函数方程证据。
C2真正需要的是同一completed函数／除子的精确对偶。
同样C4允许已知零自由因子；e^{a+bz}不改变零点，危险的是未知除子、漏重数或错误trace身份。

正性逼近还有一个比特定C5更一般的充分路线：若已识别的完整分布W_n均正型，
且W_n→W于D'(R)，则对任意compact h，W_n(h*h^*)→W(h*h^*)≥0。
所以正型锥在该拓扑下闭，配完整显式公式即可用(10)。
这不要求每个最低本征向量简单；却要求**完整**Γ／pole／properpower的同对象分布收敛，
不能只用有限低谱吻合，或将函数域不同conductor／Gamma的对象形式拼接。

可行的独立机制是：物理完整平衡先得到平方和／几何先得到相容正极化，
随后证明同一除子和规范的(12)或(10)。本族(6)→(7)是这一因果顺序的小型已闭合样本；
函数域几何纯性是另一个已知样本。对经典ζ尚无本稿新增的对应恒等式或成长不等式。
“经典ζ是正性锥唯一极端点”也未获证明，连锥及affine slice都须先固定。
而且唯一性分类不能替代属于该正性锥的存在性证明。
普通整数梳是加性物理x轴上的格；{log n}并非等距格，间距log(1+1/n)趋零，
也不满足通常Delone的uniform separation。不能把theta的加性Poisson自对偶直接当成
log坐标Weil正性；561的识别与已停止的直接运输反测试正是这一区别。

## 7. 净后果和未付责任

相对561新增：连续正primitive／N的非空RH段、全源精确平方和、同族相变，
及C3→C4重数反测试；一般判据与来源分账不冒称新外部定理。
实际ζ的强旧whole4/5、成长K_L／core／coupling／Ξ缺口均不变。
本轮不续整数梳、直接Fourier运输或未知Poincaré改名；宏观Goal门仍open。
完整逐式证明、测试空间、来源定位和修订版本见三原稿、连续谱边界补件及本轮root收据。
