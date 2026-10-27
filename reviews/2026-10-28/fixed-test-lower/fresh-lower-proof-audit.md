# Th6.2 lower 独立逆审：共同域、uniform权界与actual固定源费用

2026-10-28；`/root/unit_fresh` 独占审稿。同G20261027／runtime1793085111／原0c4f。本次按D20261028F和唯一lower门实际执行；执行中root准入的当前合同为 **C048 running、预算1**，已实际核读该合同，不以已完成C047恢复当前动作。不改STATE/cadence/Git，不执行upper、6.4、6.5或下一候选。

**限定PASS：必要前件按本项目较弱raw求值补注重闭后，Th6.2的actual fixed-nonzero-source lower可消费。** 本次有新的actual cofinal固定源总迹lower及完整K配对必要增长，建议C048统一记一个完整数学轮；来源恢复、共同域补注、两个分支与fresh不分别计轮。不是全Th6.2认证，不消费sharp系数或后章，不完成长期Goal。

## 1. 最终绑定与审查组织

先独立核原lower与Lemma6.1，逐项尝试最便宜断点：临界点评价可能为零、poly倍可能离开Sonin域、twisted误差可能只compact-height、单个trial不能代表全子空间、compact频段权差不能控制全尾、range同构不能当等距。随后实际全文核以下终稿并复核字节；没有用draft预PASS：

| 原件 | bytes | CRLF→LF SHA-256 |
|---|---:|---|
| [共同向量/原域](common-sonin-vector-and-polynomial-domain.md) | 16348 | `dcdf8e91b408423e3647f116f8bd72e040feaf24cf80f9b92db30d776398af85` |
| [加权poly lower](weighted-polynomial-trial-lower.md) | 9829 | `1206390454a52188d508f6cdc1377c736795d4514b6cd7e4ba5385301536c2ba` |

H0旧稿9bbec3…不再绑定；root消费前将具体bump支撑改为|v|<δ/2，严格落在Cc∞((−δ,δ))，本审已全文核修后稿。这只修支撑记法，b=a e^(−δ)>1仍是合法安全余量。

原作者v2 Markdown为61862 bytes，raw/LF SHA `541098314b2ddc5f8645babf82086e87d16c46188268cbc7ed6cfc1f98720058`。实际核其§6定义、Lemma6.1全部、Th6.2 lower全部及必要references；平台Accept与作者账户不作证明资格。原稿较强的未平滑raw section O(1/t)没有被认证，也不进入本次lower依赖链。

## 2. 共同H0：原点非零、两gap及全部poly域闭合

取先固定a>1的实际双gap空间K_a。必要Burnol前件为K_a非零、completed Mellin entire及连续评价、Prop4.3在临界轴的合法除零。原点是s=1/2／raw t=0；Gamma(1/4)有限非零，不能误作s=0的pole。对非零entire变换，若该点有零，只能有限阶；逐次合法除零仍在同K_a，最终得到非零原点评价。因此有实际Hermitian Riesz向量k_(a,0)，其原点评价值为||k_(a,0)||²>0。连续本身不推出非零，这一步已单独支付。

K_a⊂K_1使评价范数受旧532的gap1裸评价控制：

\[
 \|k_{a,t}\|\le\|k_{1,t}\|,\qquad
 \|k_{1,t}\|^2\le C\log(2+|t|).
\]

故raw kernel section G_a(t)至多C_a√log(2+|t|)。这个旧界已经足够，不需要从Burnol的completed结构函数猜O(1/t)；也没有使用待证cofinal trace upper，故不循环。

固定Gevrey2的ψ、intψ=1、suppψ⊂(−δ,δ)、δ<log a。实际酉dilation U_v满足C U_v=U_(−v) C，两gap均至少a e^(−δ)>1。Bochner向量g_j=∫ψ^(j)(v)U_v k_(a,0)dv对每个j都在同一K_b，且

\[
 \mathcal Mg_j=(it)^jH_0,\quad
 \|g_j\|\le A B^j(j!)^2\|k_{a,0}\|.
\]

这不是向未平滑jump直接施任意Euler导数；physical生成元为x∂_x+1/2。Mellin/Fourier乘子及原点评价经共同K_b的连续评价运输合法。于是H0(0)>0、全部t^jH0∈S0H，且固定平滑器给|H0(t)|≤C exp(−c√|t|)。常数先于X、degree、poly及源选择，满足全子空间证明所需量词。

这项项目补注只把原稿较强未核断言换成足够的已付弱界；交付的是同一个(H)前件、同样原范数和目标，未改变待证lower。原强句继续不消费，不必为它虚留已经闭合的(H)缺口。

## 3. Lemma6.1：扭Perron的绝对uniform误差

必要外部输入仅为固定v1 [Mossinghoff–Trudgian–Yang Theorem1.1](https://arxiv.org/pdf/2212.06867v1)的Vinogradov–Korobov型零自由区，按陈述cited；本审未重证其上游深定理或优化常数。取任意更小固定c，δ_T=c(logT)^(−2/3)(loglogT)^(−1/3)即可，bounded高度由既有零自由事实和compact性处理。

独立检查原推导：对Ψ_t(y)=Σ_(m≤y)Λ(m)m^(−it)，固定B而|t|≤y^B，Perron高度T=y^(B+2)远大于twist。半整数endpoint的截断费只见|Λ(m)m^(−it)|=Λ(m)，不多出t；移线Re z=1−δ_(2T)时，ζ'/ζ(z+it)的局部zero公式、O(logT)近零数及水平安全距离给固定log幂上界。唯一跨过的pole是z=1−it，不跨kernel的z=0。竖边费用y^(1−δ)log^C y，横边和截断更小，故可吸收log幂得到原文的绝对uniform误差。

round endpoint时main term y^(1−it)/(1−it)的y导数模为1，因此仍uniform。对prime sum的[√X,X]改用exponent 2B，保证|t|≤X^B≤y^(2B)。prime powers去除的O(√y log²y)可积；对y^(−1/2)/logy作partial summation时twist已在Ψ内，g′不产生|t|。低端O(X^(1/4))、末端振荡积分以|1/(1/2−it)|≤2付O(A/logX)，均为o(A)，A=√X/logX。

所以需要的|t|≤X² **absolute** uniform式成立：

\[
 \log|D_X(t)|^2
 =-4A\Re\frac{e^{-it\ell}}{1-2it}+o(A),\qquad\ell=\log X.
\]

Euler log的高次项用Σ_(p≤X)1/p=O(loglogX)支付；没有在large t处要求main term相对误差小，也没有退回仅compact频段PNT。

## 4. 整个增长维数poly空间的全线集中

J_X=[π/ℓ−ℓ^(−2),π/ℓ+ℓ^(−2)]上H0有固定正下界。独立由正规Legendre基及Cauchy–Schwarz核得，对ALL complex p、deg p<n和ALL实t，

\[
 |p(t)|^2\le Cn^2\ell^2[C\ell^2(1+|t|)]^{2n}
                  \int_{J_X}|p|^2.
\]

积分配合H0的Gevrey衰减，u=√|t|给Γ(4n+2)矩费，故

\[
 \int_{\mathbb R}|pH_0|^2
 \le e^{C_1n\log(n+\ell)}\int_{J_X}|pH_0|^2.
\]

C1不依p、X、n。这排除了“只有一个trial向量集中却拿n个正交向量求和”的失效模式。

固定非零源r，k=ord₀rhat有限，先取δ>0使|rhat(t)|≥c_r|t|^k于|t|≤δ。Euler权在J_X的log≥(4−o1)A；δ≤|t|≤X²的log≤(4/√(1+4δ²)+o1)A；|t|≤π/(2ℓ)的log≤o(A)。令Δ_δ=4−4/√(1+4δ²)>0，选择一个与p无关的小c_δ，使

\[
 n=\lfloor c_\delta A/\ell\rfloor,\qquad
 C_1c_\delta<\Delta_\delta/2.
\]

因log(n+ℓ)≤ℓ，poly entropy被固定指数gap吸收，两个坏区的质量对整个deg<n空间统一指数小。

|t|>X²不能套该compact-frequency权差。此处用global Euler上界exp((4+o1)A)与Gevrey尾，余下比例至多

\[
 e^{O(A+n\log\ell+\log n)}
 \int_{|t|>X^2}(1+|t|)^{2n}e^{-c\sqrt{|t|}}dt.
\]

u=√|t|≥X时，n logu/u在起点的上界O(1/(√Xℓ))→0，整段多项式均可被一半指数吸收，尾余exp(−c′X)压过前置费用。故ALL unit v∈V_X={D_XpH0:deg p<n}在π/(2ℓ)≤|t|≤δ上有1−o(1)质量，o(1)不依向量。

## 5. actual domain、维数与普通迹lower

所有pH0在同一个真实gap1空间；finite D_X有界可逆，旧range equality给V_X⊂Ran S_X。D_X及H0在J_X非零使多项式map单射，真实dim V_X=n。range同构没有被当成酉；按原加权norm正规化的basis已保留完整Gram逆的作用和全部returns。

每个fixed finite X的A_rS_X为HS，沿560原compact smooth/Dlog trace域消费，不对ambient未平滑核取迹。取V_X的dt/(2π)正规正交基v_j，有限正项求和给

\[
 \begin{aligned}
 t_{\{p\le X\}}(r)&=\|A_rS_X\|_{HS}^2
 \ge\sum_{j=1}^n\|\widehat r\,v_j\|^2\\
 &\ge c_r\ell^{-2k}n(1-o(1))
 \ge c'_r\frac{\sqrt X}{(\log X)^{2k+2}}.
 \end{aligned}
\]

不交换无限basis/X极限，2π在所有norm比例中消去；没有再扣一个Fourier因子。覆盖每个先固定非零complex compact smooth physical源，k、δ、c_r及起点允许依r。并不覆盖ALL changing-source共同常数、noncompact405的全部强源或全Dlog统一lower。

## 6. 560完整K与危险尺度的准确新增责任

source就是physical r，原du、zero-extension Dlog不改。冻结X_n=n+1/2、L_n=(logX_n)/2，strict/inclusive prime集合精确一致；只先消费此cofinal序列。固定r自相关可见的prime powers最终全包含，完整Q_W(r)与两个pole值均为常数。故560(2)给

\[
 \langle r,K_{L_n}r\rangle
 =t_{F_{L_n}}(r)-Q_W(r)+P_{\rm pole}(r)
 \ge c''_r e^{L_n}/L_n^{2k+2}
\]

最终成立，常数项由调小lower并提高r依赖起点吸收。完整Γ/contact、全部proper powers及不定双pole均未删。该正方向是Q=t−K+pole中必须相消的误差，不推出Q负或Q正、K全PSD。

旧安全16已付ALLdu高层小费；本次不能重计。更细fixed-source定位用旧粗界
ρ_F(s)≤(M/m)² Clog(2+|s|)，log(M/m)²=(4+o1)e^L/L。对于每个先固定η>0及r，rhat的充分阶Schwartz尾在|s|≥exp(ηe^L)外压过这一prefactor；Γ及prime symbol的粗exp(O(L))费用亦同，故同一完整K配对的外尾绝对o(1)。因此上述增长位于Γ≲ηe^L的actual频段。

这项tail费用依r/η，非ALL-source operator估计、Dlog图域不变或compact Fourier分量，不定位某个固定零频峰。它给固定源上的actual core必要误差，未给有利signed domination或core—补空间coupling控制。537全fixed正窗非根可作已有控制：同一r即使Q_W(r)>0也可有t/K共同正发散，故不把本结果误报负Weil源。

## 7. 强旧去重、计轮与停止

强旧560提供同一全型及fixed-F compact误差，但t_F≥0只给一个r依赖常数lower，不给随cofinal F的正发散。其全H inverse norm lower的测试输入不在Sonin evaluator／Weil source角色；535／570的fixed-F不定和571／572/安全高层的receiver或actual tail控制也不直接蕴含本lower。没有找到另一份已付exact分解能给这个实际固定源总迹的成长率。

本次新内容不是一般“正迹存在”或“多项式可用”：共同域之后还实际闭合Euler-cofinal权的uniform算术误差、全poly entropy、增长维数、全线尾和源乘子lower，得到该actual cofinal输出。它属于一个完整新source／必要误差测试，而非只把旧定理换名。故建议C048统一 **1数学轮**；H0弱化、Perron/VK陈述核验、旧高层恢复、下载、审查与同步均不另计。不是世界优先权主张，也不因缺RH后果降为来源0。

合同一轮完成后止此lower，不优化c_δ、零阶、sharp系数、试探窗口或续upper/6.4/6.5/后章。保非有限秩、Γ-relative、source-adapted、独立几何/signed修复；本固定源必要费未覆盖这些合法修复，也不消除primitive/mixedRR、危险core有利号/coupling、Ξ或whole leading4/5负惯性UPPER的宏观缺口。长期Goal门仍open；由root消费及统一结算，不由此审稿修改计数。

## 8. 必要外部事实与真实阅读

本审实际恢复README/STATE、check/show、Goal/宏观入口/D28F/唯一proof门及执行中新C048；数学原件为固定v2§6必要定义、Lemma6.1及Th6.2 lower，旧532评价/560全型、10-20安全高层root收据及本轮终稿。两分支终稿均全文实际核读；未核upper、6.4、6.5或§7。

外部前件按以下实际范围消费，未宣称重证整篇：

| 原件 | 本审实际范围与状态 | 固定raw SHA |
|---|---|---|
| Burnol math/0203120v7，25页/321788 bytes | PDF5/8/18必要文本；另独立整页目视PDF8 Prop4.3/Note9。非零空间／连续评价等沿必要原陈述cited，结合本地有限除零推导；不读其余零点完备性证明 | `cff449f51fe65cb8ae72f64b17e3dd4d9f5fb903776f9b825be77bfd75606039` |
| Burnol math/0208121v1，7页/117262 bytes | 本审消费H0终稿已逐页定位/目视的必要非零双gap陈述及旧原件范围；未冒称本审再次目视其7页或核其全proof | `1890a3867e745c342be3a70eeb2948c673bfb644fc4f392f9302d0b9c96acc3b` |
| Mossinghoff–Trudgian–Yang 2212.06867v1，27页/616040 bytes | 固定原PDF已本地保存，实际整页目视PDF2 Theorem1.1；只引用既有零自由区陈述，不复核外部证明/数值认证，不优化暂停路线 | `127c32eb86d0aea264cc5b1ba96cc83243ef6b763451591e1560edaca1767300` |

VK原件保存在 `literature/local/2026-10-28-fixed-test-lower/`；默认socket权限失败后通过已授权10808代理以同一固定URL下载成功。未覆盖旧原件、未改全局代理。使用PDF技能和Poppler渲染；fresh自有目视图为同目录`mty-v1-page02.png`、`burnol-v7-fresh-page08.png`。PDF提取一次GBK输出失败只影响文本打印，已以UTF-8必要提取和实际图像核对，不影响原字节。

无pending下载/计算。交回的是当前lower独立限定PASS及准确前件补注、实际费用与统一计轮建议；root消费、管理结算、GitHub同步和长期Goal状态另由root记录。
