# C003：连续同源接口与完整 Weil 保正路线的独立审查

2026-10-13。恢复并读取 AGENTS、README、STATE、check/show、Goal、C003、
D20261013C；初始工作树干净，STATE 无 pending_processes，未启动后台计算。
本审查只写本文件，不改 STATE、cadence 或主稿。没有扩大 N、拟合 ζ 零点。

读取004、016、527、528、实际矩阵实现。仓库没有本论文的本地全文；
核读一级来源 [Connes–Consani–Moscovici, Zeta Spectral Triples v1](https://arxiv.org/html/2511.22755v1)
的 §§2–4，具体接口 (2.6)、(3.17)、(3.19)–(3.22)、(4.1)–(4.4)。
下文先独立恢复物理变量，再以连续函数直接检查主代理提出的新候选。
有限核恒等式恢复本身不登记成新增数学结果。

## 1. 周期基、实奇函数与偶伙伴

令 ell=log(lambda)，L=2ell，I=[-ell,ell]，xi_n=2pi n/L。
原文 V_n=kappa(U_n) 给出中心变量 y=log u 中

    V_n(y)=(-1)^n exp(i xi_n y)/sqrt(L).

不能把代码系数 v 直接放在未带 (-1)^n 的中心 sine 中。
对实有限正指标系数 v，定义

    s_v(y)=sqrt(2/L) sum_(n>=1) (-1)^n v_n sin(xi_n y),
    c_v(y)=sqrt(2/L) sum_(n>=1) (-1)^n v_n cos(xi_n y),
    e0(y)=1/sqrt(L).

二者延拓为区间外零。s_v 实奇、c_v 实偶且均无常数 Fourier 模；
范数均为 ||v||。原奇基 O_n=(V_n-V_-n)/sqrt(2) 是 i 乘实 sine 基，
该全局 i 不改变 sesquilinear quadratic energy。
周期 Hilbert transform 约定 H_per exp(i xi_n y)=-i sign(n) exp(i xi_n y)，
于是 c_v=-H_per s_v。它是同系数的周期伙伴，**不是**逐点绝对值 |s_v|。

写来源 W=P+A+R，其中 P=w02，A=-w_real，R=-w_primes。
对每一来源 s，正指标 T_s(n,m)=W_s(n,m)、H_s(n,m)=W_s(n,-m)，
d_s(n)=W_s(n,0)。基变换直接给

    Q_s(s_v,s_v)=v^T(T_s-H_s)v=o_s(v),
    Q_s(c_v,c_v)=v^T(T_s+H_s)v=o_s(v)+2h_s(v),
    h_s(v)=[Q_s(c_v,c_v)-Q_s(s_v,s_v)]/2,
    d_s^T v=Q_s(c_v,e0)/sqrt(2).

这些是 same-source 表达，来源相加之后也成立；不能把 h_R 当作奇能量。
作为连续定义可在 joint domain

    D_pair={s real odd: s in D(QW), -H_per s in D(QW)}

上使用；有限三角多项式均在此域。本文没有另证 H_per 在实际零延拓
logarithmic form-domain 上的全域有界性，故没有偷称 D_pair=D(QW)^-。
后面的完整对象反例完全不需要这个未付伙伴域结论。

## 2. 原始连续源与 h_R、d_R、完整奇能量

对实函数 f,g 在 I 外延零，a>=0，定义

    C_a(f,g)=int_(-ell)^(ell-a) f(y)g(y+a) dy,
    q_a(f,g)=C_a(f,g)+C_a(g,f).

q_a 已含 ±a 原子对；对实 f 有 q_a(f,f)=2C_a(f,f)。
所以实际素数权 w_k=Lambda(k)/sqrt(k)、a_k=log k 给

    Q_R(f,g)=-sum_(k<=exp(L)) w_k q_(a_k)(f,g),
    h_R(v)=-sum_k w_k [C_(a_k)(c_v,c_v)-C_(a_k)(s_v,s_v)],
    d_R^T v=-(1/sqrt(2)) sum_k w_k q_(a_k)(c_v,e0).

直接积分 c_v 与常数的两个重叠区间给

    q_a(c_v,e0)=-sqrt(2) sum_n v_n sin(xi_n a)/(pi n),
    d_R^T v=sum_k w_k sum_n v_n sin(xi_n a_k)/(pi n).

最后一式与实际脚本 q_(n,0) 的分支一致，无额外 factor 2。
反向项亦恢复

    H_(R,k)(n,m)=w_k [sin(xi_n a_k)+sin(xi_m a_k)]/[pi(n+m)].

为了完整保留质量重整，设

    rho(a)=exp(a/2)/(exp(a)-exp(-a)),
    b_L=(gamma+log(4pi*(exp(L)-1)/(exp(L)+1)))/2.

对 piecewise smooth 实 f,g，完整源为

    Q_P(f,g)=2[C(f)C(g)-S(f)S(g)],
    C(f)=int_I f(y)cosh(y/2)dy,
    S(f)=int_I f(y)sinh(y/2)dy,
    Q_A(f,g)=-b_L q_0(f,g)
      -int_0^L [exp(a/2)q_a(f,g)-q_0(f,g)]/[exp(a)-exp(-a)]da.

q_0=2<f,g>；a=0 的 subtraction 不能对 diagonal/奇能量删除。
对实奇 f，C(f)=0，故

    QW(f,f)=Q_A(f,f)-2|S(f)|^2-2sum_k w_k C_(a_k)(f,f).

等价的 graph 表达是

    QW(f,f)=Q_A(f,f)+sum_k w_k E_(a_k)(f)
              -int_I D_lambda(y)|f(y)|^2dy-2|S(f)|^2.

这一式是016已有内容，不作为 C003 新输入。
注意一级来源全线 multiplier 为 2 theta'(t)，搭配单位 Fourier transform；
不能从使用非单位 transform 的 dt/(2pi) 约定中丢掉这一 2。
上述 q_a 实空间归一化与实际 w_real 逐项一致，故不依赖 multiplier 名称约定。

## 3. 新候选的不同组织复核：从两条不交正函数出发

主代理提出比较 f 与 |f| 的完整型。为避免只重做极点奇符号，
本审查用 disjoint positive supports 的 off-diagonal form 组织证明。
设非零 u>=0，u in C_c^infinity(J)，J subset (0,ell)。定义

    g_+(y)=u(y) (y>0), otherwise 0,
    g_-(y)=u(-y) (y<0), otherwise 0,
    f=g_+-g_-, phi=g_++g_-=|f|.

这四个函数都 C_c^infinity(I)；远离0，故 |f| 不产生 cusp。
延拓后 Fourier transform 快速下降，archimedean logarithmic weighted
energy 有限；素数与极点有限／有界。因此属于实际 form-domain。
f 实奇，phi 实偶，且 ||f||=||phi||；支持在固定 I 内，非数值截面试探。

令 g(a)=int u(r)u(a-r)dr，u 在正半轴外零。
不交支持使 q_0(g_+,g_-)=0。对 a>0，仅正向跨越重叠非零，故

    q_a(g_+,g_-)=g(a).

这一步可直接令 y=-r、y+a=s 得 r+s=a，并非按单原子双算。
因此

    Q_P(g_+,g_-)=2 intint u(r)u(s)cosh((r+s)/2)drds,
    Q_A(g_+,g_-)=-intint u(r)u(s)rho(r+s)drds,
    Q_R(g_+,g_-)=-sum_k w_k g(log k).

极点的第一式还可用 C(g_-)=C(g_+) 和 S(g_-)=-S(g_+) 校核。
sesquilinear expansion 给精确差

    QW(phi,phi)-QW(f,f)=4 QW(g_+,g_-)
      =4 intint u(r)u(s)[2cosh((r+s)/2)-rho(r+s)]drds
       -4sum_k w_k int u(r)u(log k-r)dr.                 (* )

因此主代理的 4/8 系数正确。作为另一检查，直接计算相关差
C_a(phi,phi)-C_a(f,f)=2g(a)，q 差是4g(a)；与 (* ) 一致。
archimedean diagonal 常数／a=0 subtraction 因质量差零消失，
不是对某个原 form 的重整常数近似删除。

## 4. 实际无原子窗口给严格正交叉

取

    J=(0.5 log(9/4),0.5 log(11/4)), lambda>sqrt(11/4).

J 位于 (0,ell)。任意 r,s 属于 supp(u) 时，

    r+s in (log(9/4),log(11/4)).

这个区间对应 exp(r+s) in (9/4,11/4)，没有任何整数，
故所有实际 prime-power 原子项均**精确零**；不改变它们的权或位置。
设 z=exp(a)>1，直接通分：

    2cosh(a/2)-rho(a)=(z^3-z-1)/[sqrt(z)*(z^2-1)].

在 z>9/4 上，z^3-z-1>0；例如分子在9/4为521/64>0，
导数3z^2-1>0。分母严格正。u 非零、连续且非负，
u(r)u(s)>0 在正面积集合上，因此

    QW(|f|,|f|)>QW(f,f)

对每个 lambda>sqrt(11/4)、每个这样的非零 u 都严格成立。
证据不依赖 RH、ζ零点、N、未知最低态、λ增长渐近或 PNT。
同一固定 u 在所有容纳支持的更大 I 中仍是同一全线零延拓函数，
本反例不会因加大 lambda 消失；新增远端素数原子相关全为零。

**准确阈值。** 令 alpha 是 z^3-z-1 的唯一 z>1 根。函数在 z>1
严格递增，端点1、2处一负一正，故 1<alpha<2 且根唯一。
对任意 mu=lambda^2>alpha，可在 (log alpha,L) 选择 a0 避开有限
实际 prime-power 原子。取 a0/2 附近足够小的 J，其闭包仍在(0,ell)，
J+J 位于(log alpha,L)且与全部原子不交。上一证明原样成立。
因此 failure 区间实为 **lambda>sqrt(alpha)**；显式9/4、11/4窗只是
避免使用代数根的便捷固定样例，不是最佳阈值。

## 5. 排除何种方法、为何不等于 Weil 非正

质量相等使任意 scalar shift q_c=q+c||.||^2 保持严格差；
更一般的实局部 multiplication potential 也保持差。
若某个下有界真实自伴 A 的 e^(-tA) 对标准逐点正锥保正，
则对于不交正函数 g_+,g_- 和足够大的 scalar shift B=A+c>=0，

    <g_+,e^(-tB)g_->>=0, <g_+,g_->=0,
    q_B(g_+,g_-)=lim_(t down 0)<g_+,(1-e^(-tB))g_->/t<=0.

等式对 form-domain 成立：谱函数 (1-e^-tx)/t 增至 x，
先对平方使用单调收敛，再极化恢复交叉。另一方面 (*) 给
q_B(g_+,g_-)=QW(g_+,g_-)>0，矛盾。
故原实际 Weil 自伴算子在这整个 lambda 区间的热半群不保正，
任意 scalar shift 或加局部实势不能修复此标准锥结论。
保正已失败，更强 positivity-improving 当然不能直接成立。
不必只引用 Beurling–Deny criterion；上述必要条件已独立证明。

也可直接使用 operator-domain：上述 g_+、g_- 全线延拓 C_c^infinity，
其 Fourier transform 是 Schwartz，乘以 logarithmic multiplier 仍 L2；
prime/pole 是 bounded，故 g_± in D(A)。谱定理给

    lim_(t down 0)<g_+,exp(-tA)g_->/t=-QW(g_+,g_-)<0.

分子因此在所有充分小的正 t 为负，直接违反保正。
bounded cone isomorphism 的相似共轭也不能修复：若 U 和 U^-1 均
映正锥到自身，那么 U exp(-tA) U^-1 保正当且仅当 exp(-tA) 保正。
这里 cone isomorphism 是明确假设，不推广到任意非局部共轭／新正锥。

**小支持的 converse 可完整闭合。** 若 1<mu<=alpha<2，则没有任何
prime-power 原子，且 F(a)=2cosh(a/2)-rho(a)<=0 对 0<a<=L。
对任意实 smooth core g，直接把完整核按 y,z 写出，得到

    QW(|g|)-QW(g)
      =intint_(I²) F(|y-z|)[|g(y)||g(z)|-g(y)g(z)]dy dz<=0. (**)

delta质量和 arch subtraction 因相同逐点平方完全相消。
[]>=0；并且 []<=(g(y)-g(z))²/2，在 near diagonal 是 O(|y-z|²)。
rho(a)=O(1/a)，故此 difference 积分绝对收敛，不能把两个单独发散
off-diagonal 积分先拆开再相减。|g| 在 I 上 Lipschitz、零延拓 BV，
Fourier decay O(1/|t|)，所以它在实际 logarithmic form-domain 内。

现取任意实 f in D(QW)。利用原文真实 form-core，用实三角多项式
g_n 在 form norm 中逼近 f；实部投影在加充分常数后的 form norm
中连续，因为实型实虚分解。于是 g_n→f 且 QW(g_n)→QW(f)。
abs 的 L2 contraction 给 |g_n|→|f|。由 (**)、真实闭型的 lsc 及下有界性，

    QW(|f|)<=liminf QW(|g_n|)<=QW(f)<infinity.

因此 modulus-domain closure 与全域 modulus-lowering 均已支付，
而不是从 smooth 单例免费推广。
取 B=A+c>=0，h>=0 时 coercive functional

    q_B(u)+tau||u||²-2<h,u>, tau>0,

具有唯一实最小器 (B+tau)^-1 h。取 |u| 不增前两项、也不增最后项，
唯一性迫使最小器非负。故所有这些 resolvents 保正。
强极限 (1+tB/n)^-n→exp(-tB) 则证明热半群保正。
综上准确边界为

    exp(-tA_lambda) 对标准正锥保正 (全部 t>=0)
       iff 1<lambda²<=alpha.

边界处 F(L)=0 不影响符号／闭型证明。这里不声称 positivity-improving。

排除的是对原完整对象、标准函数正锥、通过直接热半群／模量降低
建立 Perron–Frobenius ground-state parity 的路线。不是任意 Hilbert
实现／任意非局部共轭后的正锥，更不是所有 simple-even 方法。
该严格差没有判定 QW(f,f) 自身正负；即使两个能量都非负也相容。
不能由此推 RH 假、Weil 最低值负、奇最低值低于偶最低值或最低态不单重。
phi=|f| 是确定的偶测试函数，但它不是所有偶测试函数中的最优者。

## 6. 非重复性、未付条件与宏观结算

检索 notes/reviews 的 positivity-preserving、positivity-improving、保正、
热半群、Beurling-Deny、QW/|f| 等。004 §2只给极点来源不定与幼稚
推理警示；002只建议先变换为保正形式。没有在这些原件或本次关键词
检索结果中找到 (*) 的全实际源比较、无 prime 原子窗口或热半群反证。
没有全文审计526篇，也不声明世界首次。016的图平方及528辅助反向
相对费用与本反例的对象／量词不同：这里真的是完整连续 QW。

新增独立输入是全源 cross interaction 的实空间精确符号与实际空原子窗；
所得非重复后果是全 lambda>sqrt(11/4) 上标准锥保正方法的严格失败。
阈值加强及converse证明把该后果提升为1<lambda²<=alpha的准确分类，
全lambda²>alpha失效；单个显式窗仍保留为无需定位alpha的样例。
这是实际核心对象的一条方法类边界，强于只否定 H 的背景费用。
是否足以达到整个长期Goal的“实质规模方法类”终止强度，须由主代理
逐项对旧Goal第十节及新Goal审计；本子审查不自行宣布complete。

宏观正性瓶颈没有消失：仍未得到独立完整 Weil 正性、最低态识别或
增长支集的统一净后果；改变的是标准锥保正 shortcut 已从未付变为否定。
对 Hilbert companion 的全域闭合、实际低奇态的 h/d 联合费用仍未付。
不恢复暂停比例／无零区优化，也不从来源更换正锥免费恢复等价酉化。

停止：不再尝试原型 scalar shift 或局部 potential 的模量降低/直接
保正热半群；它们无法改变不交支持的正交叉。
重新准入：新的非局部几何正锥须与原完整 Weil 配对、域、谱作用
独立比较；或给实际 signed joint domination，而非命名新的条件。
唯一建议下一动作：主代理消费前复核 (*) 的连续原型和全量词，
以另一份独立审查审计这种方法边界的宏观强度，再决定 C003 结算和机制筛选。
无 pending processes。
