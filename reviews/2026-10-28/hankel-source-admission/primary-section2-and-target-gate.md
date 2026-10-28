# Suzuki1204v2：原核、边界模型与目标身份首门

2026-10-28；G20261027/runtime1793085111/原0c4f。按174已有准确locator只核一次§2来源门及其定义依赖，不准C050/587。两份库存咨询在root取得原PDF之前已冻结，其中“未核primary”是当时观察；不能用其旧提议的加法核/截断符号代替以下原定义。

## 原件身份与阅读范围

Masatoshi Suzuki，*A canonical system of differential equations arising from the Riemann zeta-function*，[固定arXiv1204.1827v2](https://arxiv.org/abs/1204.1827v2)。本地PDF为432186bytes，raw SHA256 `2c4cf2aa7a5bca731e0f1ac356deaa082eb6137a07c465fdfe09198acc82ef38`，28页，存ignored `literature/local/2026-10-28/`，不向Git再分发。

Root实际提取并渲染核读PDF6–9（§1.7末／§2及p9的§3.1 Mellin计算）和PDF14的§4.2式(4.7)–(4.10)行列式定义；不是重审§3全部、§4定理证明、§5或Appendix A。§2定理在本记录为有精确前件的**cited**来源，不标root新证明。§4.2仅消歧det的定义，不启动后章证明预算。

固定URL的arXiv页／PDF边栏标v2、2016-09-23；本地PDF印Date为2018-09-13、metadata CreationDate为2018-10-29，而当前HTML打印Date为2026-08-24。这些观察保留，不把渲染日期直接当新作者版本；消费以固定URL返回的本地字节为准，不混合HTML/PDF修订。2026另一篇screw文仅作旧审去重，不作为此源的proof。

## 实际公式与坐标

源文使用usual \(\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)\)，实\(\omega>0\)，\(s=\frac12-iz\)。式(2.1)–(2.3)为
\[
 c_\omega(n)=n^\omega\prod_{p\mid n}(1-p^{-2\omega}),\qquad
 h_\omega(x)=x^{-1}\sum_{n\le x}c_\omega(n)g_\omega(n/x)
 \quad(x>1),
\]
\[
 g_\omega(x)=\frac{2\pi^\omega}{\Gamma(\omega)}
 \left[x^{2-\omega}(1-x^2)^{\omega-1}
 -\omega x^{\omega-1}\int_{x^2}^{1}t^{1/2-\omega}(1-t)^{\omega-1}dt\right]
 \quad(0<x<1).
\]
g在x>1、h在0<x<1为0。h在有限[1,b]上属L1当ω>0、属L2当ω>1/2，ω>1时核连续；端点值不随意补成连续。n是全部整数，不把cω本身认作Λ，也不由其非负乘积推出H或Weil正性。

Proposition2.1只在\(\Im z>\frac12+\omega\)给绝对收敛的Mellin身份
\[
 \int_0^\infty h_\omega(x)x^{1/2+iz}\frac{dx}{x}
 =\Theta_\omega(z)=\frac{\xi(1/2-\omega-iz)}{\xi(1/2+\omega-iz)}.
\]
§3.1 p9显示其由完整γ比和ζ比共同产生；γ包含s(s−1)，不是只给ζ或arch近似。

原算子是\(L^2((0,\infty),dx)\)上的乘法Hankel核hω(xy)，截断为P_a投到(0,a)，a>0；不是先定义在[-a,a]。令v(x)=x^(-1/2)r(logx)，则\(\|v\|_{dx}=\|r\|_{du}\)，原截断对应u<log a，和核为
\[
 K_\omega(u+w)=e^{(u+w)/2}h_\omega(e^{u+w}).
\]
w是第二个对数积分坐标。物理源窗、a、ω和频高分别量化。ω>1、先fixed a时，M=sup[0,a]²|hω(xy)|有限，核双线性读出有\(aM\|v_1\|_2\|v_2\|_2\)上界；两Dlog腿可再付1/log2。这只是该Hankel读出的费用，不是完整Qζ的预算。

## 实际断点先于Hamiltonian扩建

实轴Θω模1定义一个L2边界乘子；PDF6的Watson involution可据此成立。它与算术因果hω的算子身份是另一件事。Theorem2.2把**对所有**v∈L2((1,∞),dx)的\(\widehat\Theta_\omega v=h_\omega*v\)、相应支持保持或全输出L2条件，与inner性等价。高线Mellin身份不自动给实轴逆变换；不能把边界isometry搬给未识别的causal核。该等价来源陈述也不是已给独立算术估计。

Theorem2.3的显式系统仅按ω>1、全部a>0引用：I±Hω,a可逆，m=det(1+H)/det(1−H)，Hamiltonian条目为m^-2和m²，匹配点在a=1。PDF14定义det为连续核的经典Fredholm级数(4.7)–(4.10)，不是本门已证trace-class谱积；HS本身不补普通operator determinant，亦不无声改det2。

PDF8–9还区分ω>1/2时HS/可逆的已有陈述与完整显式系统向该域的预期推广，后者不按已证消费。PDF9明确a→∞的端点行为即使ω>1也未闭。小ω的因果身份／非退化与大a端点是不同责任，不能用每个fixed a的正矩阵拼成同时极限。

## 最强旧与准入结论

在合法非零解析域，形式参数字典\(\partial_\omega\log\Theta_\omega|_0=-2\xi'/\xi(s)\)保留Γ、1/s、1/(s−1)及ζ′/ζ。它只是旧对数导数恒等式，不是核／算子critical可微性或完整D′极限；单纯恢复μ*log=Λ也未给新的signed净量。有限ω的高阶joint系数仍在原规则中，不由一阶字典宣布它们无算术内容。

174已有这条路线与未付质量/noncollapse接口；本次原件把缺口精确定位到上述causal/inner、det规范及端点量词，未取得独立支付这些前件的新原命题。没有在已读范围中给出从该Hamiltonian/Gram到全部physical \(W_\zeta(r*s^*)\)的未移位两源净预算；不据有限页数声称整篇没有任何相关结果。完整Γ/FP-contact、所有properpowers/双pole、原norm与全源成长仍欠同对象运输。

因此这次单章来源恢复为0，不建小ω可逆性/HS延拓/临界紧致性合同，不续§4证明、§5、Appendix或另一paper。不是所有Hankel/canonical系统失败，也不因等价性拒绝未来真实非循环算术证明；只是不把等价前件当已给input。正D′路线不逐层强加Pan；553仅在actual total必要读出满足原global范数前件时用，不套未定义reader。比例/无零区优化继续暂停。

当前待独立fresh及root消费；本稿出稿不计数学轮。cadence0/history50/latest586/formal17保持；whole4/5UPPER与同一primitive/mixed、signed/corecross/Ξ瓶颈未改。当前没有后继公式或proof；下一仍须自主形成实际两源身份／有符号净量及可判input-test-net，不把此处未付条件改名为已准合同，也不等待用户许可。

## 原发稿后的消费状态

独立fresh已限定PASS并绑定当前原PDF与五页阅读，root全文核后按[来源结算](../../../goals/reviews/2026-10-28-hankel-section2-source-gate.md)以来源0消费。上文“待审”保发稿时观察；这里只追加状态／链接，原公式、范围与未付前件未改。
