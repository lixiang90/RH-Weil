# 成长Weil窗的实际prime费用与恒定尾供给边界

2026-10-14；C011首轮；本版基线0c4f3a3/≤538。新的实际全源准入边界，
不是RH反例，不完成新宏观Goal。原Γ规范/全primepowers/complex源/norm均保留。
自主精确[标量核验](../scripts/c011_growth_split_gate.py)和
[原结果](../reviews/2026-10-14/macro-restart/c011-growth-split-exact.json)
只付算术常数；全源运输另由下文及[独立逆审](../reviews/2026-10-14/macro-restart/c011-growth-reverse-audit.md)支付。
不重复537/538原证书、增加Galerkin阶数或使用ζ零点。

## 1. 真正完整对象与指定lower来源

I_L=(-L,L)，Lebesgue L²，零延拓源，原complex Hermitian Q_L：
actual Γ(t)=Reψ(1/4+it/2)−logπ=2θ′，完整dual pole与全部相关primepowers。
对有限Ω和任意实β，可精确分解

    Q_L= M_(L,β)+K_(L,Ω,β)+T_(L,Ω,β)，
    M_(L,β)=βI−Σ_(p^k<e^(2L)) [2log p/√(p^k)]J_log(p^k)，
    T(f)=(2π)^-1∫_(|t|>Ω)[Γ(t)−β]|Ff(t)|²dt。

J_a是零延拓平移的paired symmetric compression（两侧平均）。
prime项在log n=2L时相关为0，strict边界没有遗漏。
K保有限Γband的真实kernel及dual pole；有限Ω上的Γ连续，压缩kernel连续于I_L平方，
所以band为Hilbert–Schmidt；pole为有限秩。故每个fixed L/Ω/β有K compact self-adjoint。
这里的Γ与原537相同，没有再乘1/2；odd负pole保留。

考察替换尾后的bounded供应器

    B_L= M_(L,β)+D_L+τI，D_L为任意self-adjoint L²-compact修复。

D_L允许原K+rank-two U，也允许任意非有限秩诱导compact费。
该类不是完整Q：真实unbounded Γ尾没有因下面的carrier消失。
若试图从Q≥B_L再靠B_L≥0证明正性，必须先检验B_L全源符号。

## 2. actual constant源费用，全部primepowers

g0=(2L)^-1/2 1_I，norm1，自相关

    <g0,J_a g0>=(1−a/(2L))_+。

故真实全prime constant费用为

\[
C_L=\sum_{p^k<e^{2L}}\frac{2\log p}{\sqrt{p^k}}
          \left(1-\frac{\log(p^k)}{2L}\right),
\quad \langle g_0,M_{L,\beta}g_0\rangle=\beta-C_L.\tag{1}
\]

每项关于L非减，入窗时为0，因此C_L整体非减。
L=3/2时exp3在(20,21)，完整primepowers为

    2,3,4,5,7,8,9,11,13,16,17,19。

Λ4/8/16=log2、Λ9=log3，而位移仍log n，不以Λn=log n误装。
自主Fraction脚本用128项atanh log及完整geometric remainder、256bit向外sqrt isqrt区间，
positive interval乘法逐项支付，再向外dyadic，给严格

\[
C_{3/2}>4.\tag{2}
\]

exp80项的余项也完整支付，primepower inventory由1,…,20的整数trial division另核。
ordinary decimal约4.0853437273仅展示，不参与门。
对原β=7/2、τ=2^-49162，Fraction另核β+τ−C_(3/2)<−1/2。
因此同一结论对每个L≥3/2成立。箱源在L²中可由strict-support smooth源逼近，
M有界，严格margin保留；后面的合法源不用非光滑domain逃逸。

## 3. 同时实际prime相位返回与全compact修复

**全源定理。** 对任意fixed L，若β+τ<C_L，则对所有self-adjoint compact D_L，
B_L有无限负指数；即使再加任意有限个连续线性源条件也保持无限负指数。
因此B_L≥0的必要条件是

\[
\beta+\tau\ge C_L.\tag{3}
\]

证明：先选norm1 real g∈Cc∞(I_L)，使<Mg,g>+τ<−d<0，
由(1)严格margin和bounded-M连续性可以做到。
该fixed L只有有限个实际primepower位移a_j。
同时Dirichlet逼近/有限维torus recurrence给ω_r→∞，e^(iω_r a_j)→1对全部j成立。
若逼近序列频率有界重复，则存在exact period，取其unbounded倍数；不预设log p的有理独立性。
取f_r(u)=e^(iω_r u)g(u)。每个f_r属于原complex Cc∞域且norm1；真实paired相关为

    <f_r,J_a f_r>=cos(ω_r a)<g,J_a g>，

所以<M f_r,f_r>→<Mg,g>。
f_r weak→0由Riemann–Lebesgue（g·overline h∈L¹，对任意h∈L²）。
compact D_L因此D_L f_r→0，<D_Lf_r,f_r>→0。
最终<B_L f_r,f_r><−d/2，合法全源负方向不受有限head/finite-rank修复遮住。

若negative index有限，bounded自伴B_L的负spectral子空间有限维；
其投影作用于weak-null f_r趋0，而正补空间上的型非负，负块范数有界，
矛盾于uniform负Rayleigh。故负指数无限。
若条件为L²-continuous，finite-codimension投影修正f_r的L²距离趋0。
一般有限个连续线性smooth源条件也可处理：Cc∞在L²稠密且B_L bounded，
每个finite-dimensional严格负Hilbert子空间可逐向量smooth逼近并保严格Gram符号；
在任意大的这种合法smooth负空间交有限kernel，仍有任意大负空间。
允许L-dependent rank或compact norm任意大；每个fixed L仍由weak0支付，
不声称carrier/导数费uniform于成长L。

这是完整实际prime而非某个辅助反射H；正tail原抽scalar τ没有丢掉。
原537/538固定L=17/16不在上述L≥3/2失败域，二者相容。
完整Q的Γ尾在carrier上约随log|ω_r|上升，不能套compact消失，
故本文没有得到Q负值、ζ离线零点或RH失败。

## 4. 不借PNT的成长必要费用

对L>0，所有n≤e^L的因子1−log n/(2L)≥1/2，故

    C_L≥Σ_(p^k≤e^L) log p/√(p^k) ≥Σ_(p≤e^L)log p/√p。

右侧发散：Euler给Σ_p1/p发散，无需PNT。其自含证明是
有限Euler product∏_(p≤x)(1−1/p)^-1包含每个n≤x的1/n，因而≥H_floor x→∞。
但其log≤Σ_(p≤x)1/p+Σ_(n≥2)1/[n(n−1)]≤Σ1/p+1；若prime reciprocal和有界便矛盾。
对p≥3，log p/√p≥1/p，有限p=2不影响。因此

\[
C_L\longrightarrow+\infty.\tag{4}
\]

所以M_L+compact型coercive供应器的effective scalar β(L)+τ(L)必须无界。
若τ=0才可单说β≥C_L；不删除未知scalar reward或倒填增长率。
本文未付C_L最优渐近、任何统一导数/返回预算，不能宣称所有signed方法失败。

## 5. 恒定外部Γ包络的必要frequency成本

若仅使用同一split的逐点constant exterior bound

    Γ(t)−β≥a≥0，|t|≥Ω，

则T≥a(I−B_Ω)，B_Ω为原支撑窗sinc压缩。fixed L/Ω下B_Ω compact。
若再从这一个供应器a(I−B_Ω)抽出τI+compact U作lower，
沿weak-null carrier有<B_Ω f_r,f_r>→0、<U f_r,f_r>→0，必τ≤a。
逐点规则和Γ连续性又给a≤Γ(Ω)−β。所以

    β+τ≤Γ(Ω)。

结合(3)，该类证明对每个L成功的必要条件为

\[
C_L\le\Gamma(\Omega).\tag{5}
\]

这是constant-envelope/compact replacement的费用责任，不是任何compressed tail正性的充分必要条件。
不从一个小负band断言真实tail负，也不删除Γ非恒定正余量。
用538已核Binet同规范上界

    Γ(t)≤log(t/(2π))+1/(15t)+25/(8t²)，t≥256，

π>3和Fraction log128/3上包络，脚本另核Γ(256)<4。
故L≥3/2时C_L>4>Γ256，排除这个固定Ω=256的constant-envelope供给程序，
包括任意β/允许scalar提取τ/所有compact修复，范围比只固定β7/2更完整。
但变Ω、非constant fullΓtail或不同same-source signed机制未排。
(4)–(5)使任何成功的该类成长程序必须Ω(L)→∞：Γ在每个bounded frequency集有界。
这里没有给足够的增长率或证明新的uncertainty/补空间费可承受。

## 6. 宏观净值、止损与唯一下一动作

新增实际量词门是：原fixed-window source不能靠同一Ω256和compact尾修复搬到所有成长窗；
有效scalar与frequency必须承担真实全prime的无界费用。
已消除“只多生成矩阵即可延伸旧来源”的选择，未支付成长全Q符号或Ξ识别。
本版Goal仍active：一个fixed split/恒定包络边界不是预设宏观完成门。

C011首轮之后停止原参数扩窗。唯一下一动作是在(3)–(5)约束下审一个具体变尺度或
直接保完整Γtail的独立whole-source joint来源，先付其最便宜反例与费用。
若第二轮只剩未知条件改名，则合同止损转不同signed/几何来源，不复活C008等待或旧C006无新输入。
重准入须新的actual核/正尾供应与全source成长预算；不增加C001N/ζ拟合。
首轮只消费原cadence一次，组织/新Goal启动/补审另不计轮，原件和逆审保存后才结算。
