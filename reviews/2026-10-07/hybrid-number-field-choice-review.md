# 数域选择独审：为什么源使用 Q(sqrt(-3))，换域能否加强无零域

2026-10-07。作者：`mixed_path_check`。只新增本报告；math 固定源只读，
不改旧稿、notes、脚本、output、Goal 或 Git；本轮没有再派代理。
上一份 22 all-distinct 新研究稿保持冻结。

结论：**在当前已经验收的接口中，换数域没有给出更强的数值无零边界。**
Q(sqrt(-3)) 的判别式、理想密度与六个单位主要进入固定常数；其真正关键
是 cubic theta + sextic residue 的组合，使 moving squarefree row 反射后
恰好成为 quadratic character。Q(i) 保留二维格和类数一，但失去这组
Gauss、theta 与 local reciprocal-signal 身份。只将6改成4不能得到一条
已证明的 Gaussian 边界，更不能比较它与现有 sigma*≈0.874957019420099。

比较换域必须区分三件事：换辅助域、换角色阶数、换 theta/probe 源。
它们在现有源中绑定在一起；只改变其中一个数字不会保留另外两个定理。

## 1. 固定来源及审查层级

只读实际来源：
[paper.tex](E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)，
固定提交
[adc7f1241b42e322a6451854ab7e4b4c146bf78a](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)。
本轮重算 canonical LF SHA256 为
`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`，
766316 UTF-8 bytes。下面行号均指这份实读源，不取 main 的另一版本。

已发布 primary sources 亦逐一核对：

- [Dunn–Radziwill, §5 与 Appendix A](https://arxiv.org/html/2109.07463v3)：
  Eisenstein cubic-theta 的 cusp/Bessel/coefficient 数据；原文的 GRH prime
  asymptotic 不是当前源使用的输入。
- [Goldmakher–Louvel, Definition 1 / Theorem 1.1 / Corollary 1.2](https://arxiv.org/html/1112.1642v2)：
  满足其 reciprocity 与 primitive-product 条件的 quadratic Hecke family
  有 `(U+V)(UV)^epsilon` 大筛；不是任意 row-column mask 的定理。
- [Blomer–Goldmakher–Louvel, Theorem 1.3](https://arxiv.org/html/1112.1650v1)：
  含所需根单位的数域上的指定 higher-order ideal family，有
  `U+V+(UV)^(2/3)` 大筛；其存在不等于当前 completed-probe/moment 存在。
- [Gao–Zhao, §2.1 与 §4](https://arxiv.org/html/1707.00091v3)：
  Q(i) 的 primary convention、quartic/quadratic characters 和相应 quadratic
  moment，是可用的 Gaussian 组件；没有提供当前 cubic completed reflection。

当前源与项目已有边界都按此前明确的 cited-input / [R] 范围使用。
本报告审查数域依赖和可迁移前件，没有重新验收整份外部 Lean 或整篇源的
所有分析证明。下文“新条件”不登记成已证数域定理。

## 2. 哪些只是固定常数，哪些是结构

源568–582同时使用以下事实：

\[
 F=\mathbf Q(\sqrt{-3}),\quad\mathcal O=\mathbf Z[\omega],\quad
 q_a=|a|^2,\quad\mathcal O^\times=\mu_6.
 \tag{1}
\]

三角格的 Euclidean division 给 PID；六个单位在 O/3O 的六个 unit classes
中恰好各出现一次。因此每个与3互素的理想有唯一 `a≡1 mod3` 的 primary
generator，且 primary generators 相乘仍 primary。

source608–625的自对偶 Fourier convention、covolume、理想计数为

\[
 e(z)=e^{2\pi i\operatorname{Tr}(z/\lambda)},\quad
 d\mu=(2/\sqrt3)dxdy,\quad
 \#\{\mathfrak a:N\mathfrak a\le H\}
 =\frac{\pi}{3\sqrt3}H+O(\sqrt H+1).
 \tag{2}
\]

对一个固定 imaginary quadratic field，二维格、有限单位和有限 class
sectors 仍给理想范数的 linear count；改变 discriminant / covolume /
finite unit factor 改的是常数及阈值，不自动改 H 的一次幂。Q(i) 的全部
理想密度为 pi/4，去掉2后 primary odd ideals 密度为 pi/8；后者在上述
Gao–Zhao §3.1的格计数中也有明确记录。两个密度较大或较小都不能直接
转换成 better sigma，因为边界比较使用 powers，固定正密度进入常数。

同样，source1440的 `3Q` 改成 `|D_K|Q`，若 K 固定，discriminant只改变
固定常数。**source amplification 的1/6不是“六个单位除出来”的指数**；
它来自下面 a^6 的范数放大与可平均的理想数。

类数一的意义不止减少常数：它使所有 ideal columns、element rows、
prime generators、norms和 exact multiplicative primary phase 用同一套
变量。类数大于一时，source1460“conductor one没有非主角色”失效；
无分歧 class-group characters 和 class cusps 必须加入。一般 Hecke
functional equation仍成立，但该行的 elementary lattice proof不能原样调用。

## 3. mu6 是 sextic Hecke 角色存在与有限 ray sector 的前件

source627–639在 good prime ideal 上使用 `q_p≡1 mod6`，定义 chi_p∈mu6，
并强制所有六整除幂仍为 zero-on-nonunit 的 `1_(gcd=1)`。
source646–699的 `lem:fixed-numerator-ray` 用

\[
 F(a^{1/6})/F\text{ 是 abelian},\qquad
 \operatorname{Gal}(F(a^{1/6})/F)\hookrightarrow\mu_6,
 \tag{3}
\]

把固定 numerator 变为 finite-order Hecke/ray character。mu6缺失时，该
Kummer extension一般不是这种 abelian sextic extension；源的定理调用失效。

在 imaginary quadratic fields 中，含 primitive cubic root 的域只能是
Q(sqrt(-3))：其 minimal polynomial degree已为2。所以不存在“另一个
imaginary quadratic field，继续保留相同mu6/cubic sextic系统”的选择。
Q(i) 只有 mu4，其他 imaginary quadratic fields只有±1。

若换成含mu6的高次 CM域，固定-numerator Kummer/ray 这一个接口可保留；
其 unit classes模六与S-valuations模六可经有限 partition处理。但这只
解决角色和固定ray数据，不解决 theta、element-row count或moment。

## 4. Gauss signal 与反射后二次角色：换域最先失败的两行

source766–835的 prime Gauss identity不是任意 number field Gauss identity：

\[
 \gamma_2(p)^3=-\alpha(p),\qquad
 \gamma_1(p)\gamma_2(p)
 =\overline{\chi_p(4)}\gamma_3(p)\gamma_2(p)^3.
 \tag{4}
\]

这里 chi^2 是 cubic symbol。证明用 cubic Jacobi sum属于 Z[omega]、
被 primary p 整除且范数相同，再用 `J≡-1 mod3` 唯一固定其单位，得到
`J(chi²,chi²)=-p`。source964–968因而得到 squarefree signal

\[
 \gamma_2(c)^3=\mu(c)\alpha(c),\qquad
 \gamma_1(c)\gamma_2(c)=\mu(c)\alpha(c)G(c).
 \tag{5}
\]

有限 Gauss相位 G 还用 source841–1039的 mod4 four-class table、cubic
reciprocity和mod2 supplementary character；这些表不能移植成同一张
Gaussian表。它们随后进入 original reciprocal Euler factor与zero masks。

更直接的结构测试来自source1789：completed reflection的 local factor是

\[
 B_p(x)=\chi_p(x)^{-j_p-2}\quad(j_p\ne0,4).
 \tag{6}
\]

source7700的 surviving squarefree residual row有 j_p=1，故(6)恰为
`chi_p(x)^(-3)=chi_p(x)^3`，一个 quadratic character。source2640–2672
正因此可调用 GL 的 `(U+V)` sieve；source2680–2737再支付 completed
`n b³` 的 gcd/square-collision masks，不能把这一步换成任意 higher-order
large sieve而仍保留原 low exponents。

**直接 mu6→mu4 替换的反例测试。**若保留“theta使用chi²”及同一个+2
shift，Gaussian chi4² 是 quadratic character，finite-field恒等式给
`gamma2(p)²=chi4²(-1)=1`，而generic Gaussian primary p的alpha(p)不是±1。
因此第一条(4)已不能成立。同时 residual j=1留下
`chi4^(-3)=chi4`，仍为quartic，无法用该 quadratic terminal norm。
这两个失败都发生在任何数值 contour optimization之前。

可作一个**相对接口的必要算术测试**：若另一份 order `d=2m` 的 theta
reflection有 local shift `j -> -j-rho`，要让 retained j=1变成quadratic，
必须有

\[
 \rho\equiv m-1\pmod{2m}.
 \tag{7}
\]

d=6取rho=2，对应现有cubic theta；d=4必须取rho=1。新的
quartic-theta Gauss input 是候选实现，并非唯一可能的架构；绝非把
quadratic chi4² 放进旧cubic公式。
d=2需要rho=0，旧非平凡 theta/Gauss signal机制已经不同。(7)只是检验
候选源的必要关系，不是构造了新 reflection theorem或新无零域。

## 5. cubic theta 的具体不可替换定理调用

source1676的 `prop:completed-reflection` 明确从 DR §5/Appendix A及
Patterson cubic theta取得 three fixed cusp coefficient functions。保留

\[
 \operatorname{supp}d\subset\{u\lambda^k n b^3:n\ {\rm sf}\},\quad
 |d(u\lambda^k n b^3)|\le27\,3^{k/6}|b|,
 \tag{8}
\]
\[
 R(t)=\prod_{\pm}\frac{\Gamma(1+t\pm1/6)}{\Gamma(1-t\pm1/6)},
 \quad K=(2\pi)^4/27.
 \tag{9}
\]

source1945–2009还保留 common primes n,b、原lambda ramification、cubic
supplementary laws与fixed modulus先于moving primes的选择。source2335–2418
从 cusp Bessel K_(1/3)导出(9)，first negative pole为−5/6及 polynomial
height seminorm。DR实际§5.2的 K_(1/3)、Z[omega] 与lambda support均可
在原始论文直接核对。

因此 Gaussian、其他 imaginary quadratic 或 higher CM 的以下调用都
没有同源准入：completed reflection本身；fixed cusp/support公式；(4)–(5)
signal；同一个 local Euler quotient/correction；由(9)给出的 strip和test
seminorm；随后利用二次终端的 reflected energy。一般 metaplectic theory
存在不能代替这几条具体公式和uniformity。

普通 Hecke gamma不要与(9)混淆。对任意固定 imaginary quadratic K，
finite-order角色的complex infinite type平凡，普通 functional equation有
单个Gamma(s)，所以source12704–12726的plain reflection kernel
`Gamma(s)/Gamma(1-s)`的相对形式仍可用。对高次 CM、r2>1则普通 completed
function含Gamma(s)^r2；height bounds与common profile须重证，不可沿用
原source的单gamma seminorm/order。这个普通 reflection不能供应cubic-theta
(8)–(9)或产生(5)的Möbius reciprocal signal。

## 6. marked/plain moments不是已发布generic sieve的同义词

源marked inverse moment在9250–9268要求

\[
 r+2z\le m-c_1,\qquad 2r+8z\le3m-c_2.
 \tag{10}
\]

其 proof闭合 source9296的canonical family：Gauss coeff gamma2(n)、
chi_n(k)、额外chi_n(f)^4、product-form marks、真实puncture、两次masked
Poisson、principal/tails，terminal用上述 reflected energy。
换域时 BGL Theorem1.3只能供应其中一个generic sieve组件；不能直接
供应(10)的marked moment，也不能许可任意新的composite column。

源plain moment12531–12578使用 two plain factors、固定inducing-character
group Theta、natural zero extensions、slot mesh，并要求

\[
 n_1+n_2+6\kappa z\le M,\qquad
 \beta_*\le(1+\kappa)/2\quad(\kappa<1).
 \tag{11}
\]

source12592–12600说明5M/6 threshold来自transformed inducing rows的
sixth-power count与volume，principal products必须按common profiles做
centered cancellation。故(11)不是由“quartic sieve换一个次数”立即得到。
系数6kappa、marked的2/8/3和low/principal contour exponents均需从新
recursion和新source重新推导；不能统称为单位个数带来的数字。

已有generic quadratic GL和higher-order BGL的relative接口是可以保留的：
新ideal family必须核对primitive conductors、finite reciprocity sectors、
same-sector primitive product和column独立于row。含mu_d及同一个large-sieve
指数2/3并不自动满足当前Gauss-normalized canonical family。

## 7. 可单独迁移的2m amplification指数

source12362–12455确实有一组纯粹来自六次放大的数字。将次数记为d=2m，
它的**相对**推导只要求：

1. 相应zero-extended order-d角色有
   `psi_(u a^d)(n)=psi_u(n)1_(gcd(n,a)=1)`。
2. 对每个固定 c>0，raw rows q_v<=H有normalized inverse moment
   `sum|M_v(D)|²<<H(HD)^epsilon`，H>=D^(1+c)，含scale supremum与row tests。
3. 有≫P个可用的ideal multipliers a，norm<=P，指定generator/row
   representative使 `(u,a)->u a^d` 在d-free rows上injective。
4. 相同natural masks、Möbius divisor decomposition与fixed seminorm uniformity。

然后

\[
 H=\max(2U,D^{1+c}),\quad P=(H/U)^{1/d},\quad
 H/P=U^{1/d}H^{1-1/d},
 \tag{12}
\]
\[
 e_d(r)=\max\{1,[1+(d-1)r]/d\},\qquad
 \alpha_d=1-1/d.
 \tag{13}
\]

严格先得到 e_(d,c)(r)=max{1,[1+(d-1)(1+c)r]/d}；
(13)使用上述 raw bound 对每个固定 c>0 成立的量词，在 bounded r 范围内
先按目标 epsilon 选足够小 c，才能吸收 c 项。仅某个固定 c 的 raw
bound 不足以推出(13)。这是从源proof可抽出的相对lemma，不要求换域theta定理已存在。
在当前d=6有e6(r)=max{1,(1+5r)/6}、alpha6=5/6。
如果一个Gaussian d=4系统另行满足以上四条，则r>1这一branch的指数
比d=6小 `(r-1)/12`；d=2比d=6小 `(r-1)/3`。r<=1时三个均为1，
没有这项saving。该数值比较**仅覆盖unmarked inverse amplification**。

与之不同，source3758的Poisson rows `u a^6` 和source4045的zeta_F(6z)
来自actual completed-probe local table；principal pole z=1/6、source6275
的Gaussian exp((s−5/6)²)与normalization由这个table及theta共同产生。
若新order-d probe真有对应zeta_K(dz)，pole会在1/d；但这一步是新
reciprocal-signal身份的条件，不能只从(12)的amplification推出。
特别是最终7/8或当前优化sigma*都不是 `1-1/d` 的直接函数。

## 8. 四类替换的具体比较

| 候选 | 已有可用组件 | 源中失效或新增前件 | 当前能否给更强sigma |
|---|---|---|---|
| Q(i)，order4 | PID、finite mu4、unique primary mod(1+i)^3、二维Poisson；generic quadratic/quartic Hecke-family sieve；ordinary single gamma | 原chi²不再cubic；Gauss signal失败；旧+2反射留下quartic。需新的quartic-theta源、local reciprocal quotient及marked/plain recursion | 不能；只得到条件e4 branch比较 |
| 仅quadratic target/family | GL quadratic sieve、ordinary Hecke reflection；条件d2 amplification | 原Poisson sextic twists不封闭于quadratic targets；非平凡theta signal与全部row induction未替换 | 不能由当前源限制族得到更强边界 |
| 其他imaginary quadratic | 二维格、finite unit/class sectors、ideal count、ordinary Hecke FE；可建ideal quadratic family | 不含mu3/mu6；sextic Kummer及DR cubic theta调用失败；非principal classes需加入，primary/cocycle重建 | 无已证新数值 |
| 更高CM且含mu6 | order6 Kummer/ray、ideal-family GL/BGL、linear ideal count | infinite unit rank、多个complex places、element norm行不有限；需unit quotient/height、new cusp/Gauss/reflection、gamma profile和recursion | 保留d6的alpha5/6本身不改；无自动saving |

高次CM特别不能把source的element count搬过去：r2>1时单位rank为r2−1，
无限多个units的absolute norm都为1，所以 `sum_(0<N(u)<=U)` 若仍按
所有elements，甚至U=1也已无限。理想count仍linear，不等于element-row
family已经定义。需先选择unit fundamental domain或ideal/finite-unit-mod-d
代表，并付archimedean height/common-profile费用。即使类数一也不能免此步。

更高CM中的cubic Jacobi sum仍落在Z[omega]，不能自动等于K的一个prime
ideal的chosen generator；source的q_p=|p|²和alpha(p)单complex-place身份
也不再是全部absolute norm。base change或“含mu6”不足以认证(4)–(9)。

## 9. 范围与Dirichlet转移

source253–255明确指出：即使目标只是zeta，Poisson rows仍引入sextic
Hecke twists，故当前论证需whole finite-order Hecke family。只保留quadratic
目标，不会让这些twists消失。若重新设计完全quadratic且对auxiliary twists
封闭的source，那是另一套证明，而非现有moment的限制子族。

对任意fixed imaginary quadratic K，若已经证明其**全部finite-order Hecke**
L函数在某个half-plane无零，norm-pullback仍有

\[
 L_K(s,\chi\circ N)=L(s,\chi)L(s,\chi\chi_{D_K})
 \quad\text{（保留相应有限Euler因子）}.
 \tag{14}
\]

所以Dirichlet transfer这一个接口不特属于−3，finite Euler nonvanishing
和principal s=1例外仍需同样处理。反之，仅有quadratic Hecke family的
结论一般不包含任意高阶Dirichlet chi的norm-pullback，不能宣称all Dirichlet。

对abelian higher CM extension，可用相应finite product of Dirichlet twists
重做transfer；一般higher field的induced representation不再是两个
Dirichlet factors，当前quadratic transfer proposition不能原样调用。
这里不声明未经核验的general Artin-factor holomorphy。

最终判断：当前瓶颈是可核验的theta/reciprocal/row-moment接口，不是−3的
固定理想密度。换域有研究价值的具体候选是“新quartic-theta reflection
保留quadratic terminal，并证明其complete signal与marked/plain量级”，
其次才是比较d4 amplification与全套contour margins。只有(12)–(13)的
单branch数值不足以宣称这个候选会改善sigma，更不能直接给6→4的边界。

状态：独立只读数域依赖审查完成；新域的核心theorems明列为待证条件。
没有改math、旧稿、Goal或Git，也没有把换域条件登记成新的无零域。
