# 数域选择、反射角色与条件放大的第二独立审查

2026-10-07。审查人：`twisted_research`。结论：**限定 PASS**。
已全文核读被审数域报告及457，独立核对固定 OpenAI 源和所用 primary
文献。结论是直接 sextic→quartic 替换失败，而正确 Gaussian Gauss
约定确有可验证的平方自由信号；后者尚不供应新的完整反射、矩估计或
无零边界。原数学仓库、被审报告、正文、论文、脚本及 Git 均未编辑。

## 1. 实际绑定与审查范围

canonical LF 计算为 UTF-8 解码后，仅将 CRLF 和 lone CR 改为 LF，再
UTF-8 编码；不 strip、不 trim、不删 EOF。绑定如下。

| 文件 | canonical LF SHA256 | canonical bytes / 行 |
|---|---|---:|
| [被审数域报告](hybrid-number-field-choice-review.md) | `47453b09c0491a201ef39667a123d046c39ed2e2df906c866f101b0796a443bb` | 17196 / 335 |
| [457](../../notes/457-number-field-choice-and-relative-amplification.md) | `75079970955602644a9290709f66e2be331ad6116d2a637ed8fc97fb0dde5791` | 15254 / 327 |
| [固定 OpenAI 源](E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex) | `42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3` | 766316 / 16677 |

源版本为提交
[adc7f1241b42e322a6451854ab7e4b4c146bf78a](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)。
以下 source 行号按上述本地文件。没有编译 Lean，也没有把本报告视为
整篇外部论文或其形式化的认证。现有 sigma* 的结论仍受既有论文所列
引用输入包 [R] 限定；本次没有改该输入包。

## 2. sextic 信号的单位、归一化与局部反射方向

source568–625确认 O=Z[omega]、primary a≡1 mod3、q_a=|a|²、六单位、
自对偶 character/measure 和理想计数常数。primary 唯一性实用于相位，
不是只用于把理想数除以六。source627–699的固定 numerator Kummer/ray
接口则使用 mu6：F(a^(1/6))/F 的 automorphism 通过六次根的比值嵌入
mu6，故为 abelian。换到不含 mu6 的域不能沿用这一前件。

我独立复算了 source766–835 的两步相位证明。令 P=q_p、H=chi_p，
tau_j=tau(H^j)，J=J(H²,H²)。有限 Gauss–Jacobi 恒等式给

\[
 \tau_2\tau_4=P,\qquad
 \tau_2^3=J\tau_2\tau_4.
 \tag{1}
\]

J属于O，模p为0且|J|=sqrt(P)。将H²(x(1−x))写成omega的幂，乘积
为1，所得 exponent sum 为0 mod3，故 J≡P−2≡−1 mod3。于是 J=up，
而 primary p≡1 mod3 和六个单位的不同 mod3 residues 强制 u=−1。
归一化后确为

\[
 \gamma_2(p)^3=-p/\sqrt P=-\alpha(p).
 \tag{2}
\]

第二条 gamma1 gamma2 身份也与 source801–810 的 Gauss–Jacobi 变换
及 bar H(4) 的方向一致。source964–968的 squarefree 乘积因而是
gamma2(c)³=mu(c)alpha(c)，没有漏去单位或把绝对值身份当相位身份。

source2225–2235给反射方向的独立核验：conjugated cubic multiplier
贡献 chi(h)^(-2)，原 local Fourier 贡献 chi(h)^(-j)，相乘留下
chi(h)^(-j−2)。令 y=h^(-1) 后是 exponent j+2 的 Gauss sum，其对x
的 character 值为 chi(x)^(-j−2)。因此 source1789–1793显示的普通
分支正确。j=4 的 Ramanujan term 和 active j=0 另有分支，不能合并
为这一普通分支。

source7697–7702在冻结 actual k_pow、k_sup 后，真正 moving residual
squarefree primes 的 exponent 是 j=1。它们反射后给 chi6^(-3)=chi6³，
恰为二次。source2640–2677核了 primitive conductor、finite reciprocity
sector、同 sector coprime primitive product 及 transpose orientation；
并明确不允许任意同时依赖 row 与 column 的 mask。
[Goldmakher–Louvel Definition1、Theorem1.1及Corollary1.2](https://arxiv.org/html/1112.1642v2)
确切要求这些 family 条件。故被审报告没有把“指数变二次”误当成整个
completed n b³ norm 已自动准入。

## 3. 直接 quartic 替换及 rho 条件

若保留 theta 的 chi² 和同一个 shift +2，只将 character 阶6改为4，
A=chi4² 已经是二次角色。对任意所用非平凡 additive character，
tau(A)²=A(−1)P=P，因此 gamma2²=1、gamma2³∈{±1}。例如 Gaussian
primary pi=−1+2i，norm5，alpha(pi)非实数；旧(2)无法成立。
另一方面 j=1 留下 chi4^(-3)=chi4，不能调用原二次终端 norm。
这只排除该直接替换，不排除新 probe 或不同的 Gauss 组合。

假定 good-prime character **具有确切阶2m**，retained exponent 仍为1，
新普通反射仅作 j↦−j−rho，则局部 character 是二次幂 chi^m，当且仅当

\[
 -1-\rho\equiv m\pmod{2m},\qquad
 \rho\equiv m-1\pmod{2m}.
 \tag{3}
\]

若只知 character 阶整除2m，应按其实际阶重做同余；不能省去这一假定。
(3)是该局部模板的充要算术测试，对存在可用的全局反射仍只是必要条件。
若 rho 由 chi^rho 的 theta multiplier 产生，其阶是

\[
 \frac{2m}{\gcd(2m,m-1)}=
 \begin{cases}m,&m\text{ 奇},\\2m,&m\text{ 偶}.\end{cases}
 \tag{4}
\]

独立检查 gcd 只可能为1或2；这也包括m=1时的平凡 multiplier。
所以 d4/rho1 在这个设计中需要 quartic multiplier，d6/rho2用 cubic。
报告已将 quartic theta 表述为候选实现，未声称它是所有可能架构中
唯一必要的实现，也未用(3)否定其他 retained exponent 的设计。

## 4. 457的 Gaussian 新信号与文献版本修正

这里有一项审查中发现并已由根节点修正的实质问题。DDHL旧v3的(3.11)
漏去 supplement；v5的(3.8)也将 inert Gauss 和的错误统一正号改成
绝对值。因此不能仅固定旧版本后，把 gamma1²/gamma2=−alpha 当成
已证的新信号。实际应使用
[David–Dunn–Hamieh–Lin v5 §3](https://arxiv.org/html/2306.11875v5)：

\[
 g_4(\pi)^2=-\epsilon_\pi\kappa_\pi\sqrt P\,\pi,
 \quad g_2(\pi)=\epsilon_\pi\sqrt P,
 \quad \kappa_\pi=(\bar\pi/\pi)_4^{-2}.
 \tag{5}
\]

对 degree-one primary pi=a+bi，P=a²+b² rational prime，a奇、b偶。
bar pi≡2a mod pi；P≡1 mod4后二次互反及P≡b² mod|a|给(a/P)=1。
所以 kappa=(2a/P)=(2/P)=epsilon。由(5)独立得到

\[
 \gamma_1(\pi)^2=-\alpha(\pi),\qquad
 \gamma_1(\pi)^2/\gamma_2(\pi)=-\epsilon_\pi\alpha(\pi).
 \tag{6}
\]

norm5的pi=−1+2i给精确J(chi,chi)=pi、epsilon=−1；norm17的pi=1+4i
给J=−pi、epsilon=1，故旧统一J=−pi不是可用身份。

对 inert rational p≡3mod4，primary pi=−p，alpha(pi)=−1。在F_(p²)，
chi(x^p)=bar chi(x)，DDHL additive trace Frobenius 不变，故 tau(chi)=
tau(bar chi)。又 chi(−1)=1，tau(chi)tau(bar chi)=p²；因此gamma1²=1
=−alpha。这里没有选定 gamma1 的正负号。最后 coprime primary CRT
multiplier经 quartic reciprocity属于{±1}，平方为1，alpha又精确相乘，
从而对全部 odd primary squarefree c得到

\[
 \gamma_1(c)^2=\mu(c)\alpha(c).
 \tag{7}
\]

这认证457(2a)–(2c)的范围与归一化，也解释为什么正确候选是平方信号，
而非未付相位的旧比值。普通 prime 相位可支付，仍不能从(7)推出平方
Gauss coefficient sum 的完整 theta/cusp reflection 或 Euler reciprocal。

DDHL §4.5确有24个 cusp 数据、K_(1/4)及部分 periodicity/square 系数
身份；其 exponent-one core 没有 cubic 情形的完整公式。Lemma9.2的
actual transformed numerator为 unit/ramified factor乘(alpha/m)²；在
对应 coprime部分，Gauss numerator移位带来 quadratic twist。它不是
所有 incoming quartic j 的同一个 uniform j↦−j−1公式。457准确保留了
这些区别。[DDHL v5 §4.5、Lemma9.2](https://arxiv.org/html/2306.11875v5)

## 5. 相对放大引理与 epsilon 量词

source12362–12460与457的 divisor 分解相容。对每个 multiplier a，将
squarefree n 分为 b m，b|rad(a)、(m,a)=1，自然零保留给精确身份

\[
 M_u(D;W)=\sum_{b\mid\operatorname{rad}(a)}
 \mu(b)\psi_u(b)(Nb)^{-1/2}M_{ua^d}(D/Nb;W).
 \tag{8}
\]

(Nb)^(-1/2)和 W 的同一缩放均未漏去；u,a共享 primes 时两边自然零
仍一致。对 coefficients 作 triangle/Cauchy，divisor mass为P^epsilon。
平均≳P个a，再用 d-free row representatives 的 injectivity和已假定的
raw row-scale supremum，得到 H/P，H=max(2U,D^(1+c))。严格先给

\[
 e_{d,c}(r)=\max\{1,[1+(d-1)(1+c)r]/d\}.
 \tag{9}
\]

审查要求补明的量词现已采纳：raw supremum对**每个固定c>0**可用；
固定r的有界范围及最终epsilon后先选小c，再请求其余小 power losses，
才可写e_d(r)=max{1,[1+(d−1)r]/d}。没有要求常数对c→0一致。
某个不可调整的固定c输入不能给这个无c公式。

e6−e4=(r−1)/12、e6−e2=(r−1)/3仅在r>1成立；r≤1都为1。这里是
U均方界指数，绝非sigma的改变。generic higher-order sieve的均衡
R^(4/3)费用也仅是同尺度组件比较；没有与完整 contour budget合并。
[Blomer–Goldmakher–Louvel Theorem1.3](https://arxiv.org/html/1112.1650v1)
只处理其指定 squarefree ideal family，并不供应 marked/plain moment。

## 6. 其余全文范围及尚未支付的接口

source1676–2418的 cubic completed reflection确切含三份 fixed cusp
coefficient functions、u lambda^k n b³支持、common n,b primes、
R(t)=prod Gamma(1+t±1/6)/Gamma(1−t±1/6)、首负pole−5/6和height
seminorm。[Dunn–Radziwill §5.1–5.3、AppendixA](https://arxiv.org/html/2109.07463v3)
的 Bessel/cusp/support组件与源一致；没有使用其 GRH prime asymptotic
作为本次数域结论输入。它们与普通 Hecke FE不是同一个接口。

source1440及12704–12726的 ordinary单gamma比值可在固定虚二次域
重新使用；固定CM degree2r则有Gamma(s)^r，但 conductor指数仍为
1/2−s，不能变为r(1/2−s)。457(11)与
[Goldmakher–Louvel (3.1)–(3.2)](https://arxiv.org/html/1112.1642v2)及
[Watkins §3.6](https://magma.maths.usyd.edu.au/~watkins/papers/hecke.pdf)
相容。高次CM的无限units使原norm-bounded element rows已无限；
ideal的linear count不能自行修复这个定义域。

Gaussian primary convention及odd ideal密度pi/8与
[Gao–Zhao §2.1、§3.1](https://arxiv.org/html/1707.00091v3)相符；固定
discriminant/covolume/density的变化不自行改变这里比较的渐近 powers。
source9250–9268的 marked inequalities、12531–12600的 plain容量/
5M/6阈值，以及3758、4045、6275的 sixth-free rows/zeta(6z)/double
residue都确切来自实际源。不存在已准入的6→4替换规则。

虚二次 norm-pullback可按split、inert、ramified Euler factors独立核验
L_K(s,chi∘N)=L(s,chi)L(s,chi chi_D)，删去/还原所需有限Euler因子。
这需要新的whole finite-order Hecke family无零结论；仅quadratic子族
不包含任意chi的pullback。source253–255也确言Poisson会引入全族twists。

最终仍未支付：新quartic probe 的完整 cusp/core 系数及反射，local
reciprocal Euler quotient及natural masks，principal cancellation，
marked/plain的actual uniform moments，contour的全部误差与全族延拓。
当前两份被审文件对此都保留明确条件。此前发现的 c量词、rho候选架构
措辞、lone-CR公式破损及DDHL旧版相位均已修正；本绑定版本没有未处理
的实质性阻断。限定PASS不表示新quartic无零域、全RH或形式化认证。

## 7. 本轮有限核验

在内存中完成：50个m的确切shift/order断言；norm7 sextic归一化点验；
102个degree-one Gaussian primary有限模型的Jacobi及supplement核验；
p=3,7,11,19四个F_(p²)的Frobenius和Gauss平方点验。全部通过。
这些有限模型仅辅助检查符号和归一化，不替代以上全域证明，也没有
生成或修改已冻结脚本/output。

另只读核了新仓库审计
[脚本](../../scripts/hybrid_number_field_exact_audit.py)和
[JSON](../../output/hybrid-number-field-exact-audit.json)：导入后调用
certify()，逐字段等于当前JSON，44个split、6个inert、10个shift模型
通过。script canonical SHA为
`ac82eb7aac59449ee218b39f33a3e3291e04066cb296a40033cd98f869589389`
（4522bytes）；JSON canonical SHA为
`e670c3ea1a3d8071ca7c124e83bb89d55feb223b3bd730dfab7cfe674e0122d9`
（3452bytes）。未执行写output的main入口。其明确仅认证有限Gaussian
residue/Jacobi及有理指数，不认证反射、矩、Euler quotient或无零区域。
