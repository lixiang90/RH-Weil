# 原Type II大一次素因子余项：平方满部分完整尾项与保留的零点留数

2026-10-08。作者：checkpoint_audit。仅新增本源；不修改冻结笔记、旧证明、
数值输出或Git。父线程基线为已推送f20c94b；本稿不依赖其Git状态作为数学证据。

**状态：完整自然子族证明，待不同作者全文独审。** 本轮新增的是原系数
中平方满部分t的大尾项付款，不是整个large-s signed余项的第四矩付款。
保持唯一的valuation恰为1分解k=st，保留原bV、genuine-prime m、
正高度窗、normalizer与共同乘积两sharp endpoints。证明一般H≥1下

\[
 \boxed{\ \mathcal M_{E_H}\ll_{\phi,\varepsilon}
               X^\varepsilon(1+X/H^2).\ }
 \tag{1}
\]

这里E_H包含全部允许平方满t(k)>H的项，s=1亦允许。
同一证明直接适用于原479 non-squarefull-k余项的t>H子族。
此外，实际small-t余项的生成函数在Re(z)>1精确写为
\(\zeta(z)C_{V,H}(z)/\zeta(2z)-1\)，其genuine-prime m卷积在
每个Re(ρ)>1/2的ζ零点仍有原负重数留数。
这不是新的whole增长、惯性常数、零点比例或无零条带。

## 1. 全文读取的冻结来源与一般对象

canonical UTF-8 LF仅统一CRLF/lone CR，不trim或改变EOF。
以下六项本轮均全文读取并独立核对hash，没有以已有PASS替代阅读。

| 完整输入 | canonical LF SHA256 |
|---|---|
| [480原小s及complete moment transfer](../../notes/480-original-type-ii-single-prime-part-and-whole-moment-transfer.md) | 13a6cbd697ad960cdb97543090861373f21b6970710bc2d247edac59bb08e791 |
| [479原实际因子归约](../../notes/479-original-type-ii-factor-reduction-and-diagonal-gauge.md) | 6b6e15f8a3a83d62e1d472cbeaa86a894c9e01740ccd682fc79ec99c2ec5a559 |
| [476 conditional whole增长](../../notes/476-original-fourth-growth-five-sevenths-with-ivic-density.md) | 179829dd25f92ff187359f73455aafad9f957d714df13cf871db47a76e9408b6 |
| [原小一次素因子完整子族源](hybrid-original-type-ii-small-single-prime-part-fourth-research-radial.md) | f0b740a85b09f70b68653bf3ec06288150876f1f761920ffb1107620fbf44580 |
| [原短Λ、稀疏族及最大prefix完整源](hybrid-original-type-ii-short-lambda-factor-fourth-research-radial.md) | b39876e0b9d91a06de57d1069cf6adac676252bd1fe737186bb065716015abb0 |
| [原短Möbius准入及完整Vaughan留数](hybrid-short-mobius-twist-and-vaughan-zero-residue-research-radial.md) | a970366e68b8d3526c0dadac49b8ee8f4a7b6984e763712a851f8b6d353a291d |

令X=T/(2π)、ell=logX、J_T=[T/4,4T]，a_ell≥c_phi>0，
\(\|F\|_{p,T}=(T^{-1}\int_{J_T}|F|^p)^{1/p}\)。
允许一般整数2≤V≤X、1≤U≤M0≤X，以及实数1≤Y<X、H≥1。
定义同一个finite divisor系数

\[
 b_V(k)=\sum_{d\mid k,\ d\le V}\mu(d),
\]

和原C4中的完整large-genuine-prime部分

\[
 G_{M_0}(t)=-\frac1{a_\ell\ell}
 \sum_{\substack{m>M_0,\ m\ {\rm prime}\\k>V\\Y<mk\le X}}
 \frac{\Lambda(m)b_V(k)}{\sqrt{mk}}(mk)^{it}.
 \tag{2}
\]

本稿的尾项估计对这些参数统一；它不自行证明任意新U,V,Y下
\(P_H-G_{M_0}\) 的其他Vaughan/low-block误差合同。
改变U,V或Y后必须对那个新对象重建完整Vaughan账本。

对每个k定义

\[
 s(k)=\prod_{v_p(k)=1}p,\qquad t(k)=k/s(k).
 \tag{3}
\]

于是k=st唯一，s squarefree、t squarefull、(s,t)=1，且允许s=1或t=1。
这是exactly-one-prime part，不是odd squarefree kernel。
原m与s或t之间没有互素前件；以下重排也不添加(m,k)=1。

## 2. 完整large-t子族与精确重排

在(2)中定义E_H为t(k)>H子族，并令Q_H=G_M0−E_H。
它们是精确不交分区，共同Y<mk≤X及原负号仍在。
对固定squarefull整数t定义真实有限n系数

\[
 c_t(n)=\frac1\ell
 \sum_{\substack{ms=n,\ m>M_0,\ m\ {\rm prime}\\
                   s\ {\rm squarefree},\ (s,t)=1,\ st>V}}
       \Lambda(m)b_V(st).
 \tag{4}
\]

允许s=1；若研究479原non-squarefull余项，则只在(4)增加s≥2。
所有整数乘积n=ms的允许m，包括m|s或m|t情形，都保留在(4)内。
因为\(\sqrt{mk}=\sqrt t\sqrt n\)、mk=nt，有限重排给

\[
 E_H(t_0)=-\frac1{a_\ell}
 \sum_{\substack{t>H\\t\ {\rm squarefull}}}
       \frac{t^{it_0}}{\sqrt t}
       \sum_{Y/t<n\le X/t}\frac{c_t(n)}{\sqrt n}n^{it_0}.
 \tag{5}
\]

这里t_0为高度，t为平方满整数；(5)不会混淆两种变量。
所有实际nt≤X，故m,s,t,n均≤X，外和实际有限。
条件st>V、prime m、squarefree s、(s,t)=1与m>M0均由(4)准确保留。
Y/t、X/t是原乘积掩码的实际移动实端点，不替换成rectangle。

## 3. varying-t系数的统一subpower前件

对任意整数s,t有\(\tau(st)\le\tau(s)\tau(t)\)，而
\(|b_V(st)|\le\tau(st)\) 的常数对V统一。
在实际n≤X上\(\Lambda(m)/\ell\le1\)，故

\[
 |c_t(n)|\le\tau(t)\sum_{m\mid n}\tau(n/m)
            =\tau(t)\tau_3(n).
 \tag{6}
\]

在为dyadic数组填零时只需n≤2X；此时Λ(m)/ell≤2可用同一个固定常数。
任意先固定η>0，标准divisor bound给
\(|c_t(n)|\ll_\eta X^\eta\)，对1≤t≤X、n≤2X及所有M0,V统一。
具体可对两个divisor各取η/2；限制只删除(6)的非负upper中的项。
这个步骤不把c_t换成τ系数，也不改变其signed definition。

原最大prefix源§8(22)对每个满足统一subpower前件的实际q给

\[
 \left\|\max_{N\le u\le2N}
    \left|\sum_{N<n\le u}\frac{q(n)}{\sqrt n}n^{it_0}\right|
 \right\|_{4,T}^4
 \ll_\rho X^\rho(1+N^2/X),\quad 1\le N\ll X.
 \tag{7}
\]

这里任意最终ρ>0先固定。
其binary-block平方product长度是4N²，均值费用是1+N²/X；
同层能量2^(-j)使maximal费用可求和，未使用ζ四矩。
该证明只使用uniform coefficient upper，不要求q独立于外参数。
因此可以逐个固定t取q=c_t，常数仍对t统一；
随后在外层用Minkowski是合法的，完全不需要一个未知的联合prime/μ矩。
这是直接给每个实际c_t证明norm upper，不是从signed总函数的norm
推断任意子集的norm。s≥2版本满足相同的(6)，也可直接使用(7)。

## 4. 所有dyads、共同sharp endpoints与尾项付款

若H>X则E_H=0。以下H≤X，平方满外层从真实H开始，
\(B_j=2^jH\)，以(B_j,2B_j]的整数交集覆盖t>H。
内层n≥2，从N_i=2^i、i≥0的(N_i,2N_i]覆盖；
相邻端点没有双计或遗漏，至多O(log²X)个非空带pair。

固定(B,2B]和(N,2N]。每个实际t的n区间是

\[
 (\max(N,Y/t),\ \min(2N,X/t)].
 \tag{8}
\]

空区间先判为0，否则它精确是同一c_t数组的两个prefix之差。
端点可clamp到[N,2N]而不改变整数集合；(7)对全部端点统一。
任意squarefull整数可唯一写为a²b³，b squarefree，所以

\[
 \#\{B<t\le2B:t\ {\rm squarefull}\}\ll\sqrt B,
 \qquad
 \sum_{\substack{B<t\le2B\\t\ {\rm squarefull}}}t^{-1/2}\ll1.
 \tag{9}
\]

证明为\(\sum_b\sqrt{2B}b^{-3/2}\ll\sqrt B\)，其中取掉b的
squarefree限制仅用于此upper。包括整数1的约定也不改变统一常数。

现在只对平方满外t使用L4 Minkowski与(9)，保留内层signed c_t，得

\[
 \|E_{B,N}\|_{4,T}
 \ll_{\phi,\rho}X^{\rho/4}(1+N^2/X)^{1/4}.
 \tag{10}
\]

非空带有实际t>B、n>N、nt≤X，因此BN<X，且B≥H，故

\[
 1+N^2/X\le1+X/B^2\le1+X/H^2.
 \tag{11}
\]

将O(log²X)个完整带pair再作L4 Minkowski，取第四幂，日志至多log⁸X。
对给定最终ε>0，先在(7)及(6)分配ρ=ε/2以及更小的固定divisor损失，
再将log⁸X费用吸收到X^(ε/2)。这证明(1)对任意固定ε成立。
全部参数与取整端点只改变原整数集合，常数对其统一。
没有把polylog负幂写成X负幂，也没有用有限数值样本替代任何∞估计。

## 5. 原479/480的真实缩约与一般幂费用

对冻结V=floorX^(1/8)、M0=floorX^(1/4)、Y=X^(5/6)，
在原R0中直接给s≥2的(4)使用上证，得

\[
 \mathcal M_{E_H^{\rm nsf}}\ll X^\varepsilon(1+X/H^2),
 \quad
 R_0=E_H^{\rm nsf}+Q_H^{\rm nsf}.
 \tag{12}
\]

若bV(st)≠0，则rad(k)>V；由于rad(t)²|t，有

\[
 s\operatorname{rad}(t)>V,\qquad t>V^2/s^2.
 \tag{13}
\]

取480的确切整数Ssharp=floorX^(5/96)，以及真实实数
\(H_{\rm old}=V^2/S_{\rm sharp}^2\)。所有原D_Ssharp非零项
都满足t>H_old，因此D_Ssharp完整包含于本次E_Hold^nsf子族。
原Rsharp中的额外子族s>Ssharp、t>H_old现在也完整付款。
这里包含指原整数项族；不是从一个signed多项式upper推出子集upper。

对大X，V≥X^(1/8)/2、Ssharp≤X^(5/96)，故

\[
 X/H_{\rm old}^2=XS_{\rm sharp}^4/V^4
       \ll X^{17/24}.
 \tag{14}
\]

余项Q_Hold^nsf的所有非零项满足t≤H_old且s>Ssharp。
它比旧Rsharp增加了一个真实必要条件；在相同冻结m截止下，
原项族被进一步限制，但不声称signed norm单调或已给整个余项更小upper。

一般H=floorX^h、固定h>0时，(1)给显示成本max(0,1−2h)。
H≥X^h/2可付floors；当H>X时尾项本来为空。
若1≤H≤V²，所有非零squarefull k满足t=k>V²≥H，
因而包含于完整E_H，small-t余项自动没有s=1项。
其非零项必要满足

\[
 s>V/\sqrt H,\qquad s\operatorname{rad}(t)>V.
 \tag{15}
\]

因此取\(S_{\rm nat}=\lfloor V/\sqrt H\rfloor\) 时，
全部nonzero 2≤s≤S_nat已被尾项吸收。
不能将S_nat无误差地换成另一个floorX^a：V和H各自取整可能产生边界项。
本尾项证明不需要另外选择s截止。

例如在冻结V下H=floorX^(1/6)给tail四矩≤X^(2/3+ε)，
并使实际small-t剩余满足s>V/√H≈X^(1/24)。
这只是tail费用；原固定M0=X^(1/4)的short-m误差仍为17/24。
若另下移m截止或改变U,V,Y，完整总误差必须另算，
不得把新余项与旧Rsharp作未经验证的包含断言。

## 6. large once-prime分区的精确系数与目前未付处

令p为s(k)中最大的素因子，并写s=pr，(p,rt)=1。
p按此规则唯一，r squarefree且每个素因子<p；允许r=t=1。
对所有这样的原项，有限divisor分成含p与不含p两类，严格有

\[
 b_V(prt)=b_V(rt)-b_{V/p}(rt).
 \tag{16}
\]

这里\(b_W(a)=\sum_{d\mid a,d\le W}\mu(d)\)，W<1时为空和0，
实际整数集合等价于d≤floorW；所有μ符号保留。
p>V时第二项确为0，故bV(prt)=bV(rt)。
在p>V这一支中，若rt>1且此系数非零，则rad(rt)>V，特别rt>V。
若rt=1则k=p、bV(k)=1，这个真实prime×prime子族继续存在。
不能将large s误当成large单个p：许多小once primes的乘积也可超过阈值。

仅以同一generic maximal bound并对p外层求和不能付款整个large-p块。
具体在p∈(P,2P]固定p，把其余实际乘积合并成u，实际u≤X/p，
signed u系数仍有subpower upper，但prime外L1只给O(√P)。
这条已明确计算的路线所得成本为

\[
 X^\varepsilon P^2(1+X/P^2)
       =X^\varepsilon(P^2+X),
 \tag{17}
\]

不足以改善5/7或17/24。式(17)仅是这条特定估计的付款，
不是large-p余项必须有此大小，也不是任何相消方法的不可能性判定。
保留(16)后可继续寻求actual joint μ/prime付款；本稿不代付该步骤。

## 7. small-t实际生成函数：完整μ展开仍留一个−1

以下在每个固定X对应的有限V,H,M0下推导精确生成函数。
暂在Re(z)>1，所有无限s或prime系列绝对收敛，有限重排合法。
对squarefull t设

\[
 F_{V,t}(z)=
 \prod_{p\mid t}(1+p^{-z})^{-1}
 \sum_{\substack{q\mid\operatorname{rad}(t)\\q\le V}}\mu(q)
 \sum_{\substack{a\le V/q\\a\ {\rm squarefree},\ (a,t)=1}}
       \mu(a)a^{-z}\prod_{p\mid a}(1+p^{-z})^{-1}.
 \tag{18}
\]

每个非零μ-divisor d|st因(s,t)=1唯一为d=aq，
a|s、q|rad(t)，且原d≤V恰为a≤V/q。
又对squarefree a、(a,t)=1，

\[
 \sum_{\substack{s\ {\rm squarefree},\ (s,t)=1\\a\mid s}}s^{-z}
 =a^{-z}\frac{\zeta(z)}{\zeta(2z)}
       \prod_{p\mid at}(1+p^{-z})^{-1}.
 \tag{19}
\]

此式是写s=ar、(r,at)=1后逐素数Euler乘积，
不会将odd squarefree kernel混入唯一k分解。
所以完整实际系数给

\[
 \sum_{s\ {\rm squarefree},\ (s,t)=1}b_V(st)s^{-z}
       =\frac{\zeta(z)}{\zeta(2z)}F_{V,t}(z).
 \tag{20}
\]

定义有限
\(C_{V,H}(z)=\sum_{t\le H,\ t\ {\rm squarefull}}t^{-z}F_{V,t}(z)\)。
对于全部k>V、t(k)≤H、s≥1的实际系数系列，

\[
 B_{V,H}(z)=\sum_{\substack{k>V\\t(k)\le H}}b_V(k)k^{-z}
       =\frac{\zeta(z)}{\zeta(2z)}C_{V,H}(z)-1.
 \tag{21}
\]

最后−1不是近似：对2≤k≤V，全部μ-divisor已纳入，bV(k)=0；
k=1有t=1≤H、bV(1)=1，原k>V准确扣去这唯一非零low项。
因此(21)对每个有限H≥1都成立。
若H≤V²，1<t≤H且t squarefull有bV(t)=0，
故删除s=1不再改变(21)的实际k>V系列。
这正是(15)的non-squarefull small-t余项。

## 8. genuine-prime m与原top零点留数

令

\[
 A_{M_0}(z)=\sum_{p>M_0}(\log p)p^{-z}
 =-\frac{\zeta'(z)}{\zeta(z)}
       -Q_{\rm pp}(z)-F_{M_0}^{\rm prime}(z),
 \tag{22}
\]

其中\(F_{M_0}^{\rm prime}=\sum_{p\le M_0}\log p\,p^{-z}\)为finite entire，
\(Q_{\rm pp}=\sum_p\sum_{j\ge2}\log p\,p^{-jz}\)在Re(z)>1/2
局部一致绝对收敛：固定σ>1/2后由
\(\sum_{n\ge2}\log n\,n^{-2\sigma}\)支付。
因此(22)在该半平面给meromorphic continuation。
C_VH的有限分母1+p^(-z)在Re(z)>0非零，故C在该域解析。
在Re(z)>1/2，ζ(2z)由绝对Euler乘积非零。

对ζ任一非平凡零点ρ=β+iγ、β>1/2、重数mρ，(21)给

\[
 B_{V,H}(\rho)=-1,\qquad
 \operatorname{Res}_{z=\rho} A_{M_0}(z)=-m_\rho.
\]

故small-t原负系数卷积的未归一化生成函数
\(\mathcal H_{M_0,V,H}(z)=-A_{M_0}(z)B_{V,H}(z)\)严格满足

\[
 \boxed{\operatorname{Res}_{z=\rho}\mathcal H_{M_0,V,H}(z)
                 =-m_\rho.}
 \tag{23}
\]

若重数>1，ζ因子仍使B+1在ρ处取零，而A仅有simple pole，
上述留数计算不变。原normalizer只再除以a_ell ell。
本节不宣称Re(ρ)=1/2上的proper-power continuation已由绝对收敛支付。

实际Y<mk≤X的两端可用x♯=floorX+1/2、y♯=floorY+1/2
保持原整数集合。Perron移线若实际跨过ρ，且边界等已合法支付，
这个精确留数所对应的核仍为

\[
 -\frac{m_\rho}{a_\ell\ell}
   \frac{(x^\sharp)^{\rho-z_0}-(y^\sharp)^{\rho-z_0}}
        {\rho-z_0},\qquad z_0=1/2-it_0.
 \tag{24}
\]

这里只记录exact local residue和核，不由(24)免费认领完整移线尾项付款。
H、M0以及有限μ相消没有供应一个小于1的top-zero减幅。
原短Möbius[Rθ]点值准入也不能直接套到(18)的带依赖权finite sums，
更不能从它删除(21)的−1。
这说明原absolute zero-packet density路线的top输入仍在，
并不排除signed零点包能量或actual μ/prime新相消带来改善。

## 9. 本轮交付范围

新的完整付款是原genuine-prime m、原bV与共同sharp cut的t>H子族；
全部t dyads、所有aspect ratios、m与k共享素因子及真实端点均保留。
没有未付款的本子族边界或高t-tail。
small-t剩余继续是实际signed scalar；large-s条件只是由自然零域
推出的必要支持条件，不能充当整个剩余的第四矩upper。

(1)与(21)–(23)是本轮新增可审推导，均不依数值实验或新的外部文献输入。
关于更低M0或新的U,V,Y组合，父线程另行核验完整Vaughan参数化后
才可合成新的误差成本；本稿不把另一个因子分区冒充旧Rsharp的直接付款。
476 conditional whole5/7、既有p_dg、sigma*与原κ反馈仍按其冻结前件阅读。
