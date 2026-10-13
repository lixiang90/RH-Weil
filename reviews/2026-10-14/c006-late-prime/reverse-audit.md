# C006：端点平方、同源取消与统一拓扑边界的不同组织逆审

2026-10-14（Asia/Shanghai）。恢复 AGENTS、README、STATE、check/show、
现 Goal、C006、D20261014A、532及实际工作树。只写本文件，不改STATE/cadence。
核对 direct-increment-audit.md 与 source-increment-audit.md；
采用 distribution forcing→真实右端点→实际整数scale→完整Gram逆→source核配对 的顺序。
不以 fixed-s 极限代替固定source的可积分估计，不另计研究轮。

## 1. Riesz evaluator 的 distribution 域与实际端点

固定实位Sonin cutoff1。物理空间H=L²((0,infinity),dx)，F核2cos(2pi xy)。
L为(0,1)低投影，H0=I-L，K=LFL，R=(I-K²)^-1。
实位K compact且norm<1，真实Sonin投影为

    P=H0-H0 F L R L F H0.

令 `e_s(x)=x^(-1/2+is)/sqrt(2pi)`，`gamma_s=m(-s)`；
e_s不是L²向量，不能直接写bounded P e_s。
完整homogeneous Fourier只在distribution意义给 `F e_s=gamma_s e_-s`。
合法低forcing是

    r_s=gamma_s L e_-s-L F L e_s,
    v_s=r_s+(R-I)r_s=r_s+J r_s,
    J=R-I=K R K.

r_s属于L¹(0,1)，其L¹范数对实s统一有界。
K的光滑cosine-even核使J有光滑核，所有有限阶导数统一有界；
故J可连续作用于L¹，Jr_s是smooth L²向量。
这里没有将通常非L²的r_s未经定义送入R；R在此L¹输入上的延拓准确由I+J给出。

从532使用的有限physical power截断恢复此式也合法：
其LF高power forcing逐点趋r_s，并有const_s x^-1/2的低区间可积控制，
由振荡积分的换元／一次分部积分得L¹收敛。
J作用后在所有低区间有限Cm范数收敛；FL作用在紧外区也可按L¹连续性取极限。
因此532的唯一弱Riesz极限在物理x≥1有真实外部表示

    k_s=H0(e_s-F L v_s).

裸求值的sqrt(2pi)因子与两份稿件一致；没有换为Gamma-completed evaluator。

为看清大x尾，令

    h_s=F L e_s-Jr_s   (在低区间的cosine-even光滑函数).

homogeneous power精确相消后，外部k_s可写为
`gamma_s F(H0 e_-s)+F(L h_s)`。
第一项是从1到infinity的Mellin cosine积分，任意正阶power导数可积；
第二项是光滑低区间cosine积分，0端的所有奇导数为0。
反复分部积分因此只有1端的sin/cos振荡，产生至少三阶、以及任意固定阶尾。
power导数的系数为s的有限多项式，h_s的所有固定Cm范数反而对实s统一有界。
选择足够多分部积分次数后，所需x导数的余项也有同一有限多项式(s)控制。

记 `kappa_s=k_s(1+)`、`beta_s=(Fk_s)(1+)`。
低表达准确给 `beta_s=v_s(1+)`、`kappa_s=e_s(1)-F L v_s(1)`。
P与F的交织及实结构给 `Fk_s=gamma_s conj(k_s)`，所以
`beta_s=gamma_s conj(kappa_s)`、|beta_s|=|kappa_s|。
端点是实际右侧光滑值，并非一般L²向量的点值。

准确头两阶为

    k_s(x)=-beta_s sin(2pi x)/(pi x)
              -(Fk_s)'(1+) cos(2pi x)/(2pi²x²)+O_s(x^-3).

逆审核出了direct稿最初显式cos系数的正号错误，已通知主代理；
当前direct稿已改成负号。这个纠错不改变下面的sin首项或p^-2平方系数，
但确定端点尾时必须保留准确符号；source稿使用未命名d_s不受影响。

## 2. 端点的高频与首项的非空实际范围

对低区间smooth函数h，weighted Mellin一次分部积分给
`integral_0^1 x^(-1/2+is)h(x)dx=O_h((1+|s|)^-1)`。
应用于FL e_s和Jr_s及其低端点导数，得到

    kappa_s=1/sqrt(2pi)+O(1/|s|),
    beta_s=gamma_s/sqrt(2pi)+O(1/|s|).

完整低forcing也使kappa、beta在全部实s上连续有界。
在|Im s|<1/2的更小紧strip中，r_s为holomorphic L¹族，
J及端点光滑行的作用连续；因而两者实轴上real analytic。
gamma的Gamma比在该strip附近无实轴奇点。

gamma(s)的相位最终严格旋转且无界，因为其相位导数为actual K(s)~log|s|。
于是有任意大s的gamma(s)=-1，而kappa_s趋正的非零常数。
所以 `kappa_s-beta_s`不恒为0，存在开频段上平方严格正。
这一步是非循环的actual Gamma/endpoint输入，不使用ζ零点。

## 3. actual p 与 q 的联合极限：两个矩项

固定实s，写k=k_s、z=kappa_s、t=beta_s，q=p^-1/2、a=logp。
物理dilation为 `U_a k(x)=p^-1/2 k(x/p)`，故

    <k,U_a k>=sqrt(p) integral_1^infinity conj(k(py))k(y)dy.

首sin尾代入后为
`-conj(t)/(pi sqrt(p)) integral_1^infinity sin(2pi py)k(y)/y dy`。
在actual整数prime上sin(2pi p)=0、cos(2pi p)=1；端点分部积分给

    <k,U_a k>=-q³ conj(t)z/(2pi²)+O_s(q⁵),
    M1=<k,P(U_a+U_a*)Pk>
       =-q³ Re(gamma_s conj(z)^2)/pi²+O_s(q⁵).

第二cos尾另付一次非驻相；三阶余项绝对积分至O_s(q⁵)。
一般实scale会留下cos(2pi p)等端点相位，不能将本结论随意推广到所有实p。

令 `u=H0 U_a* k`。首尾给

    u(x)=-q t sin(2pi p x)/(pi x)+O_s(q³x^-2),
    ||u||²=q²|z|²/(2pi²)+O_s(q⁴).

低Fourier泄漏LFu为O_s(q³)，因为低频x∈(0,1)的p±x均远离0。
真实Sonin projection公式给 `P U_a* k=u+O_s(q³)`。
另一branch利用P FL=0和F交织，而不是删除U_a k的低部分：

    P U_a k=gamma_s F conj(u)+O_s(q³).

因此两个return的leading norm相同。其cross须另审：
在1≤x≤p/2，Fu的点值为O_s(q³)，而∫|u|=O_s(q logp)；
在x≥p/2，u的L²尾O_s(q²)，Fu的总L²范数O_s(q)。
故cross为O_s(q⁴logp)+O_s(q³)，可统一吸入O_s(q³)。
实际完整第二矩为

    M2=||P(U_a+U_a*)Pk||²=q²|z|²/pi²+O_s(q³).

这些误差均有固定有限阶polynomial(s)常数。若只知道一般Sonin L²性、
或只保留O_s(x^-2)不确定尾，无法合法确定M1的常数；第1节已经支付这两个前件。

## 4. 全 Gram 逆、裸质量抵消及固定s范围

设C=P(U_a+U_a*)P、alpha=1+q²、r=q/alpha、d=2cos(as)。
实际密度是

    rho_p=(1-rd) sum_(j>=0) r^j Mj, M0=rho_inf.

所以分子中的q²rho_inf和Gram逆的alpha在零阶精确消去，
不是q²T_inf加一个被遗忘的负项。
对所有j≥2，C自伴、norm≤2给
`|Mj|≤2^(j-2)M2`。
这条实际矩界使完整j≥3尾为O_s(q⁵)，而不是仅按||k||²的粗O(q³)尾。
p≥3时2r≤sqrt(3)/2<1有统一gap；r与q的差、所有乘d cross亦付入O_s(q⁵)。
得到

    rho_p-rho_inf=-2r cos(as)rho_inf
       +q⁴/pi²[|kappa_s|²-Re(beta_s conj(kappa_s))]+O_s(q⁵).

pointwise密度仍有第一项O(q)，不能删除它或声称pointwise leading为p^-2。
平方恒等式尚须同源积分之后才可消费。

## 5. actual source 上的快速大移位取消

对fixed g∈Cc∞，需要审
`J_g(a)=integral |ghat(s)|² rho_inf(s)exp(ias)ds`。
它是合法TC的同源translated trace，不是独立ambient Tr(U_aP)。
source稿的直接实际核组织通过：在physical外部x,y≥1，

    P(x,y)=delta(x-y)-(F L R L F)(x,y), R=I+J.

FLF的裸kernel为
`sin(2pi(x-y))/(pi(x-y))+sin(2pi(x+y))/(pi(x+y))`。
在large scaling-diagonal上，delta的source贡献因相关支撑远离该large shift为0。
缩放trace的module因子sqrt(rho)需保留；它只改变所需非驻相次数。
源自相关v为fixed Cc∞，rho=p exp(v)。两个bare相位的v导数均至少const_U p x。
先作v配对再对x积分，反复v分部积分后x尾绝对可积。

FLJLF项的第一low变量在0处odd derivatives全零；低变量分部积分
只留下端点1的sin/cos(2pi rho x)及任意深阶可积余项。
其端点系数是fixed smooth cosine-row作用，不依赖p；
v非驻相支付任意指定p负幂，深阶余项直接用(rho x)^-M及sqrt(rho)支付。
因此

    J_g(logp)=O_(g,N)(p^-N), every fixed N.

这个组织在已付source TC／trace分布中成立，不把两个发散ambient traces相减。
它等价于primary actual Gamma off-diagonal
`-rho^-1/2/(1-rho^-2)`与delta核的非振荡项准确相消；
若使用half Gamma，取消会失败。
没有依据粗normtransport推快速取消，也没有换用未绝对控制的prolate求和。

source常数依赖有限次自相关导数。固定smooth g的ghat为Schwartz，
第3–4节的polynomial(s)误差因而可积分；这最终支付fixed-g定理

    T_p(g)-T_inf(g)=p^-2 A(g)+O_g(p^-5/2),
    A(g)=1/(2pi²) integral |ghat(s)|² |kappa_s-beta_s|²ds.

每个nonzero固定g有A(g)>0；故所有充分大的actual primes给严格正增量。
fixed smooth single-p增量的绝对和收敛，常数可在fixed支持的足够高Sobolev有界集统一。
没有支付L²-only余项，也没有支付从其他base S连续添加prime的量词。

## 6. leading form 的 source L²范围及强制 coercivity

由第2节，A在unitary source Fourier规范中的乘子为

    a(s)=2pi/(2pi²)|kappa_s-beta_s|²
        =pi^-2(1-Re gamma_s)+O(1/|s|).

原Gamma相位gamma的inverse Fourier是actual log-cosine kernel的反演：
`2exp(-t/2)cos(2pi exp(-t))`；实部再作对称，均在有限差集上光滑有界。
因此对固定 **bounded** 源支持U，其压缩为HS；O(1/|s|)项是C0乘子的compact压缩。
所以准确地

    A_U=pi^-2 I_U+compact_U.

裸求值sqrt(2pi)、source Parseval2pi及原F核2cos共同给此质量系数，
不能将其误写成1/(2pi²)I。
positive multiplier不恒零，零集由real analyticity无正测度；
或者对bounded U直接用source Fourier的整延拓和一个正开频段即可。
所以A_U无kernel。positive selfadjoint Fredholm算子由此有实际c_U>0的coercive下界。
这给 **首项** 的真实L²质量，不给p依赖余项的同一拓扑。
有限矩零、两个patch等finite-codimension闭子空间的压缩仍有同一pi^-2质量主项。

## 7. 本轮实际证明的 uniform asymptotic 不可能边界

主代理提出、现已核准的边界应直接消费，而非作为下一轮待证目标。
在原冻结源域，每个p≥3的所有primepower相关严格0。
532因而给 `Delta_p=T_p-T_inf` 在source L²上是compact。
令V为原合法矩零闭子空间（可以使用逐patch零矩），V无限维；
则每个Delta_p|V仍compact，而 `A_V=pi^-2I_V+compact`。
故对每个actual p≥3，

    p²Delta_p-A_V=-pi^-2I_V+compact,
    ||p²Delta_p-A_V|| >= pi^-2.

无需调用额外未知谱：对原smooth单位weak-zero h_R两patch组合，
固定p的compact项趋0，A_V的型趋pi^-2；其Rayleigh差趋-pi^-2。
所以fixed-g渐近 **严格不能** 升级为全source L²单位球的
`||Delta_p-p^-2 A_V||=o(p^-2)`，更不能有uniform O(p^-5/2)余项。
这是实际量词／拓扑边界，不是一个假想模型反例。

未排除统一绝对上界 `||Delta_p||≤C p^-2`，其他可求和上界，
或在明确Sobolev有界集／固定向量上的已付渐近。
compact算子经p增长可以强近似非compact质量块，不能从本边界反推出其norm必发散。
joint频率R=R(p)仍适合检验真正uniform绝对预算，但不再追不可能的norm渐近。

## 8. 宏观复盘强度意见及唯一下一动作

相对启动基线，这一轮给 actual fixed-source late-prime 的新signed正平方，
严格p-rate、single-p可求和净费用、coercive leading form，
以及全L² norm渐近类的真实无限维边界；超出旧同构、条件预算或有限诊断。
532的首prime非紧桥与本轮正项都接上真实physical Sonin／同一实际源，
但不能把几份local后果累计当成完整Weil关键输入已支付。

宏观实际变化是：arch-base的fixed smooth late-prime费用现在可消费，
“fixed-g渐近→uniform L²渐近”的捷径已严格关闭。
关键全对象前件仍未削弱到可消费的共同预算：原冻结QW−T2低域compact符号、
统一source L² **绝对** late费用、conditioned base-S cross和成长S/U均未付，
真正最低态／prolate亦未接上。因此整体Goal完成审计仍不成立，
不由周期复盘、合同完成、严格正leading或保存行为宣告complete。
世界优先权、外部评议和形式化按未认证状态保留。

唯一下一动作：在同一冻结矩零源域检验尚未排除的uniform source L²绝对预算
或joint R(p)反证；保持完整actual projection，不再追uniform p^-2 norm渐近。
base-S运输待该单prime绝对预算实际支付后再审，不自动复活暂停路线。
本审查无待处理计算／下载进程，不修改STATE/cadence。
