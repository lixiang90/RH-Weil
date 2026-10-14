# 完整Γ与prime/pole signed桥：C012准入原件审查

2026-10-14；仅本文件归本代理所有。本文是C011转向所需的入口审查，
不自行结算新轮、不改root STATE/Goal/cadence/Git。
本次任务重新恢复AGENTS→README/STATE→check/show→本Goal/MACRO_FRONTIER/C011/
D20261014L，实际工作树已有C011-second并行文件；不把代理get_goal的null当root终态。
原成果基线仍0c4f3a3/≤538，下面先扣除旧恒等式，再列可核的新fee准入探针。

## 1. 实际对象和零频端点

采用原I_L=(-L,L)、zero-extension、Lebesgue norm、complex Cc∞源f，

    F_f(t)=∫f(u)e^(-itu)du，h_f(a)=∫f(u+a)conjugate(f(u))du，
    k(a)=Re h_f(a)，N=||f||²，k(0)=N。

h_f是positive-definite Hermitian correlation；k为偶实positive-definite函数。
positive-definite不是k(a)逐点非负。原合法complex carrier就使k(a)换符号，
不能对whole source消费“所有相关非负”。Cc∞时k为smooth compact-support，
其支撑严格包含于(-2L,2L)，且k′(0)=0。

实际完整型为

    Q_L(f)=Γ-form(f)+2Re[F_f(i/2)conjugate(F_f(-i/2))]
            -2Σ_(p^j<e^(2L)) logp/√(p^j) k(log(p^j))，
    Γ(t)=Reψ_digamma(1/4+it/2)-logπ=2θ′。

以下ψ_Cheb(x)=Σ_(n≤x)Λ(n)右连续且ψ_Cheb(1)=0；所有primepowers含完整权，
Λ(p^j)=logp而位置为jlogp。支持边界n=e^(2L)的相关为0，故无half-atom约定。

## 2. 保完整Γ的positive jump energy，actual系数

digamma差分的可积正核表达给

    Γ(t)-Γ(0)=∫_0∞ w(r)(1-cos(tr))dr，
    w(r)=2exp(-r/2)/(1-exp(-2r))，
    Γ(0)=-γ-π/2-3log2-logπ。

证明可先对ψ(1/4+it/2)-ψ(1/4)用其差分积分，再令u=2r；Jacobian2必保留。
原012的rho=e^(-r/2)/(1-e^(-2r))是旧half规范，actual这里为2rho。
按原2π Plancherel及Tonelli，精确得到

    Γ-form(f)=Γ(0)N+JΓ(f)，
    JΓ(f)=∫_0∞w(r)[N-k(r)]dr
         =(1/2)∫_0∞w(r)||T_r f-f||²dr≥0。          (S1)

T_r是R上zero-extended源的酉translation，不是只在overlap内取partial graph差。
w(r)~1/r近0，smooth源||T_rf-f||²=O(r²)||f′||²；远处w指数衰减，故S1有限。
对自然Dlog，非负Tonelli表达与Γ(t)-Γ(0)的log增长给同一闭positive型，
并非先拆两个近零发散积分。full unbounded Γtail全部保留，没有Ω scalar降级。

## 3. pole-mainprime精确cancel，Stieltjes端点不能丢

dual pole从原两个Laplace矩直接给

    pole(f)=4∫_0∞ cosh(a/2)k(a)da，
    prime(f)=-2∫_(0,∞) e^(-a/2)k(a)dψ_Cheb(e^a)。

独立从actual537原源重新核系数，而不只相信旧016：令
C(f)=∫f(u)cosh(u/2)du、S(f)=∫f(u)sinh(u/2)du，则
F(i/2)=C+S、F(-i/2)=C-S。两矩乘积交叉项为pure imaginary，所以

    pole=2(|C|²-|S|²)。

4cosh的单侧correlation积分与此相同：它来自full-line双侧相关的偶化，
不能把正平方误写成4|C|²。原positive reference中的pole正块为2|C|²，
odd负块为-2|S|²；若为控制更宽费用采用2|C|²+2|S|²的加强positive预算，
下面carrier上两项仍Schwartz下降，因而不改变无界结论。

置E(a)=ψ_Cheb(e^a)-e^a，则dψ_Cheb(e^a)=e^a da+dE(a)且E(0)=-1。
pole主项2e^(a/2)与连续prime主项精确cancel：

    pole+prime=2∫_0∞ e^(-a/2)k(a)da-2∫_(0,∞) z(a)dE(a)，
    z(a)=e^(-a/2)k(a)。                            (S2)

z compact-support、z(0)=N，分部积分须付

    ∫_(0,∞) z dE=[zE]_0∞-∫_0∞E z′ da=N-∫_0∞E z′ da，
    z′=e^(-a/2)(k′-k/2)。

所以同一完整型有两种等价组织：

    Q=(Γ(0)-2)N+JΓ+2∫e^(-a/2)k
                   +2∫E e^(-a/2)(k′-k/2)，       (S3)

或令A(a)=E(a)+1=ψ_Cheb(e^a)-e^a+1、A(0)=0，得

    Q=Γ(0)N+JΓ+2∫e^(-a/2)k
                   +2∫A e^(-a/2)(k′-k/2)。       (S4)

不能把S3的E误配S4的mass常数：这会漏掉-2N。S2的Stieltjes式直接适用于
固定窗连续correlation（原有限atoms与compact连续项皆合法）；导数式S3/S4此处
只消费Cc∞，可延H¹，不能无费在全Dlog中预设k′存在或可积。

## 4. 原件重复审查：旧资产和候选严格分开

已完整核读016、405、518及当前539，定向检索全notes中的Gamma/Γ、derivative/
导数、variation/变差、Dlog/logarithmic、autocorrelation/h_f/k′等组合；另定向读
252、253、294及292–300的相关载波/端点/变差段落，并核041及529。
这是指定对象的重复审查，不声称全文重审全部历史或世界优先权。

| 基线文件 | 已有资产 | 与本候选的区别 |
|---|---|---|
| 016 | actual纠错后的prime图P-V、degree成长、分别norm失败 | 未见weighted autocorrelation primitive variation相对whole-log-Γ型无界命题 |
| 012/023及2026-10-13纠错 | rho核、digamma谱底及actual2θ′ | S1是旧核的精确规范恢复，不能凭positive jump改名成新来源 |
| 405/518–520 | 全部源/双矩/完整显式公式与ζ商谱 | 不是独立符号，S2–S4的重排不突破这个接口缺口 |
| 252/253/294 | d(ψ-x)匹配Stieltjes与中心化端点、PNT前缀费用 | 其测试核F_Yξ/Abel权不是原Weil autocorrelation全源Dlog门 |
| 237 | 累计primitive variation对非零band响应的过强/非必要证书；显式positive measure慢调制及有限determinant-grid反例 | 原测度随参数构造、比较对象为band physical response；没有冻结actual ψ current，也没有actual autocorrelation与log-Γ form的relative预算 |
| 292–300 | response Cauchy迹载波、端点BV、完整显式公式误差、临界shift费用 | 未见本B_E与实际JΓ+prime图positive能量的同一relative-form命题 |
| 041 | Euler–Bessel逐系数绝对值产生modified-Bessel指数损失 | 相邻absolute-cancellation思想已有；实际对象、源和比较norm不同 |
| 529/539 | whole-Q标准锥边界、prime carrier/compact供应器费用 | 不能把又一single-prime signed残差负方向记成新轮 |

S1–S4应作为新合同的**精确入口/原量词**，不作为新算术输入、数学轮或Goal成果。
下面S5的native费用测试未在本次定向审查找到同一旧命题，仍需root完整原证据核验
后决定是否为新准入轮；不能仅因文件标题或关键词未命中而认证新颖性。

追加核读237§6–11：其(23)已经明确指出||F||∞∫|K′|会抹去低频F与band K′的
正交性，这是本研究已有的absolute-variation思想警示。237-C/E的严格目标是
否定“cumulative discrepancy是小band response的必要/唯一输入”，并区分band-energy
充分证书与物理signed响应；它不否认该primitive bound本身作为充分上界的正确性。
本S5–S8则固定actual E(a)=ψ(e^a)-e^a，变原Weil合法autocorrelation source，
证明此实际absolute付款甚至不能在固定L由原logarithmic positive型以有限常数控制。
不能引用237的任意positive measure反例作为本native结论的原证据，也不能把
“绝对值丢振荡”思想再次登记为创新；若消费新的严格命题，只消费实际对象/norm/
全complex量词和无界rate这一不同接口。此补审零数学轮。

## 5. 可核全源探针：absolute-centeredψ variation并非log-form相对有界

候选错误消费门为：把S3最后signed积分按

    B_E(f)=2∫_0∞e^(-a/2)|E(a)| |k′(a)-k(a)/2|da   (S5)

支付，然后声称对全complex Cc∞源，有有限fixed-L常数c_L,d_L使

    B_E(f)≤c_L JΓ(f)+d_L N，                     (S6)

或以c_L times原Γ/prime图/positive pole总能量加finite norm/compact费支付。
这里E确为原算术primitive，没换成任意bad coefficient。

**严格探针。** 对任意L>0，选一个fixed nonzero real非负g∈Cc∞(I_L)，
支撑直径b<min(2L,log2)，并让其在支持内部正，normalize N=1。
令H(a)=h_g(a)；H smooth、非负、支撑在[-b,b]，且(0,b)中有严格正区间。
原全complex合法carrier为

    f_ω(u)=e^(iωu)g(u)，k_ω(a)=cos(ωa)H(a)。

在0<a<b<log2没有任何primepower，所以ψ_Cheb(e^a)=0，E(a)=-e^a精确，
不靠PNT或零点。S5因而精确是

    B_E(f_ω)=2∫_0^b e^(a/2)
           |-ωH(a)sin(ωa)+cos(ωa)(H′(a)-H(a)/2)|da。

由||x+y|-|x||≤|y|，差去主项后的误差统一有界于
2∫e^(a/2)|H′-H/2|da。非negative L¹权phi=e^(a/2)H的|sin|周期平均给

    lim_(ω→∞) B_E(f_ω)/ω
      =(4/π)∫_0^b e^(a/2)H(a)da>0。             (S7)

周期平均可用|sin|绝对可和Fourier级数及Riemann–Lebesgue逐项付，或逐周期
Riemann sums；不用ordinary采样/拟合。误差是O_g(1)加周期平均的o_g(ω)，
没有虚写uniform O(1)的averaging remainder。

若改用S4的centered A=E+1，则0<a<b中|A|=e^a-1，完全同样有

    lim B_A(f_ω)/ω=(4/π)∫_0^b (e^(a/2)-e^(-a/2))H(a)da>0。

所以把起点改为0也不逃逸；必须保signed cancellation而非换primitive名。

另一方面Γ同规范Binet给Γ(t)=log(|t|/(2π))+O(1/|t|)于大|t|；
F_g Schwartz，按s=t-ω分为|s|≤ω/2与其Schwartz尾，支付

    JΓ(f_ω)=logω+O_g(1)。                         (S8)

所有本窗实际primepower相关恰好0，因此原partial prime图positive能量等于其
degree mass项，只取决于|g|²，为fixed-L O(1)；也可直接逐项E_a≤4N，有限总权
给uniform O_L(1)。actual positive pole平方2|C(f_ω)|²的Laplace-weighted Fourier
integral Schwartz下降；更强2|C|²+2|S|²预算同样下降。任意fixed-L bounded
positive scalar/compact修复贡献O_L(1)。
因此原positive Γ+primegraph+evenpole参考能量为logω+O_(L,g)(1)，S7–S8迫
任何S6或上述增强reference预算失败。常数可以依L任意大，只要在这个fixed L
有限，就不能付全source；rank/norm随成长L任意变化也不救逐L carrier。

按positive reference型normalize f_ω之后，该B_E仍以ω/logω无界；这正是
**不具统一Dlog relative-form控制**，不是只发现||f′||大。无需断言每个Dlog源的
B_E已经定义或等于∞：在原smooth core上无界已经排除任何这样连续型预算。

## 6. signed真实残差与whole-Q仍保持正确方向

S5的爆炸是支付法丢signed source振荡后的伪费用。原真实残差

    R_E(f)=-2∫z dE=2∫e^(a/2)k(a)da

在上述prime-free carrier上只是compact smooth-weight Fourier积分，趋0；
S3里端点-2N和未取绝对值的primitive derivative积分精确配合。
整个pole亦Schwartz趋0，prime项为0，而Γ-form=logω-log(2π)+o(1)。
所以该族whole Q最终为正并增长。S7不能推Q负、RH失败或实际signed来源不存在。

另一个first-prime signed residual无限±carrier探针可用于标签负对照，但它已由
539的同源carrier/compact逻辑涵盖，不宜记为新的数学轮。

若root把S5–S8用于C012首轮，实际新边界须限定为：原完整Γ/primegraph positive
energy不能uniform控制这种**绝对化centered Chebyshev primitive derivative fee**。
这比generic bad-derivative警示精确，但它只排该支付法，未排保留signed E的费用，
源分块、不同可独立支付的非局部正性或成长域联合结构。不能仅凭这项准入完成
本版Goal第三门；需总体宏观范围审计及真正核心影响。

## 7. C012准入建议与唯一待核对象

不将S3/S4整式重新写成“证明残差≤positive energy”并当独立来源；该整式全域
domination就是原Weil正性责任。先冻结S5这一常见PNT-envelope消费门，验证S7–S8
及其与≤538区别；若未有同一旧命题，可作为一轮严格新支付法边界。若发现已有
同对象旧证明，则不结算此轮，转向真正保signed的source-local trace/kernel输入。

实际下一候选必须明确一份比全Weil正性弱、原件可核的signed primitive response
估计，并同时核原Dlog norm/所有complex源/growth参数/primepowers/pole端点；
普通PNT |E| upper加S5已不能作为它的全源付款。完整S1 Γjump能量继续保留。
本代理没有启动数值/原科学process；本入口交付及保存不独立消费cadence。
