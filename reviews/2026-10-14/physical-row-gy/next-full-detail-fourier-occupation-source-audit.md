# 完整整数 detail 的 Fourier occupation：changed-head 来源准备

2026-10-14，独立审查，**零数学轮**；不建立 C021、不改 STATE/合同/cadence/Git。
新轮按 AGENTS 恢复 README/STATE、check/show、同 G20261014 Goal/frontier、
C020 stopped/D20261014V、547/546 原件。结构 check 通过不认证数学；
现场 HEAD `5e65cc4637fc2d89edd83a85a4e492a5a6cd3608`，root 的
STATE/git属性/审查目录有进行中改动。子 get_goal=null 不代 root 运行态。
本稿只付款下列 exact occupation 与 noncompact carry 事实；actual Γ 运输仍未付。

## 1. 首要对象修正与合法 changed head

整数 N≥4、L=(logN)/2，x=e^(u+L)∈(1,N)、du=dx/x，

    a(u)=e^(u/2)=N^−1/4sqrt x，b(u)=e^(−u/2)=N^1/4/sqrt x。

对 r(u)=a(u)φ(x)，原 norm **精确**为

    ||r||²_(du)=N^−1/2 ∫_1^N |φ(x)|²dx。              (1)

547 的旧 P 是每格原 du 常数head；其旧 R 条件是
∫_(j,j+1)r dx/x=0，换成 φ 后为 ∫φ(x)/sqrt x dx=0。
它不等于 ordinary cellmean φ=0。因此本稿 **不称 547 原 R 的证明**。

定义一个不同、合法的原 norm 正交投影 Π^a，head 由
a·1_(j,j+1)、j=1,…,N−1 张成。各 basis norm²=N^−1/2，互不相交，故

    Π^a(aφ)=a·Σ_j1_(j,j+1)∫_j^(j+1)φ(y)dy，
    R_a=I−Π^a，R_a(aφ)=aφ iff ∫_j^(j+1)φ dx=0。      (2)

rankΠ^a=N−1；(1) 是常数倍等距运输，不是更换原 Hilbert norm。
每个 fixed N，head 源在 u 上为有限BV，Fourier 为 O_N(1/|t|)，
属于 Dlog 和 actual Γ multiplier operator域。有限秩 Π^a:L²→Dlog
有 fixed-N 有界范数，所以 R_a 保 Dlog。此处未付 uniform-N 投影图范数。
不无声继承547旧P/R的逼近率或548 canonical Γ<100。

a 本身精确在新head，R_a a=0。原双pole算子为
Pole=|a〉〈b|+|b〉〈a|，于是

    R_a Pole R_a=0。                                (3)

但 R_a Pole Π^a 一般非零，Γ/prime的mixed也仍须付款；(3)不推完整Q正性。
这是一份 changed-head/domain 记录，而不是把旧R条件忽略掉。

## 2. actual dilation、所有 children/carry 与原 norm

在 flat dx 坐标定义 φ 在 (1,N) 外为零，

    U_qφ(x)=sqrt q·φ(qx)，q≥2。

它是原 partial translation T_q r(u)=r(u+logq) 的精确运输：
T_q(aφ)=a U_qφ。Jacobian给

    ||U_qφ||²=∫_q^N |φ(y)|²dy≤||φ||²，
    U_q*φ(y)=q^−1/2 φ(y/q)1_(q,N)(y)。              (4)

q≥N 时源的正测度 overlap为零，actual sum严格为 q<N。
对父cell (j,j+1)，其 children 是 (qj+r,qj+r+1)、0≤r<q，
只保 qj+r≤N−1 的实际整数cells；其余按 zeroextension 为零。
integer N 的终止点恰是完整child端点，(4)不漏尾部 fractional cell。
若每个 child mean为零，则

    ∫_j^(j+1)U_qφ dx=q^−1/2∫_(qj)^(qj+q)φ(y)dy=0，

故 U_q 保 flat-zero-mean detail，即保 R_a。其 full adjoint一般不保detail；
full selfadjoint detail compression 的 adjoint是 R_a U_q* R_a。
Π^a T_q R_a=0 只消去一个方向；R_a T_q Π^a/coupling不可删。

## 3. exact all-complex occupation lemma

每格完整 Fourier 为

    φ_j(v)=φ(j+v)=Σ_(k∈Z\{0}) f_(j,k)e^(2πikv)，0<v<1。

所有 f_(j,k) 完全独立complex；不是共同profile或有限scalarvector。
Parseval用原 unitcell dx，||φ||²=Σ_(j,k≠0)|f_(j,k)|²。
定义 P_q 为每格 Fourier频率 m 可被 q 整除的正交projection，
D_q=P_q U_q（在零均值域 m=0分量仍为零）；它是contraction。
令

    L_cell(φ)=Σ_(j,k≠0)log|k|·|f_(j,k)|²∈[0,∞]。

对任意 η>0、全部 independent complex profiles，

    2Σ_(2≤q<N)Λ(q)/sqrt q Re〈D_qφ,φ〉
       ≤η L_cell(φ)+η^−1Σ_(q<N)Λ(q)/q·||φ||²
       ≤η L_cell(φ)+(3/η)logN·||φ||²。              (5)

内积对第一变量线性。证明逐 q 保 source/target 的同一个 φ：
〈D_qφ,φ〉=〈D_qφ,P_qφ〉，Young给

    2Λ(q)/sqrt q |〈D_qφ,P_qφ〉|
      ≤ηΛ(q)||P_qφ||²+η^−1Λ(q)/q||D_qφ||²。

第二项由 (4) contraction付款。第一项对所有 k≠0 交换非负和：

    Σ_(q<N)Λ(q)||P_qφ||²
       =Σ_(j,k≠0)[Σ_(q<N, q divides |k|)Λ(q)]|f_(j,k)|²
       ≤Σ_(j,k≠0)log|k|·|f_(j,k)|²。

使用全部proper prime powers的exact Σ_(d|m)Λ(d)=logm；k=±1的费用为零。
旧546的自含Chebyshev/Mertens工具给
Σ_(q<N)Λ(q)/q≤logN+4log2≤3logN，N≥4，得到明确常数。
(5) 不假设RH或未知zero位置，不消费外部positive声明。
L_cell=∞时为extended inequality；实质有限费域为 L_cell<∞。
本稿不先宣称它与actual Dlog的uniform-N图范数等价。

回到原du，只须 (5) 全式乘 N^−1/2。令
L_cell,u(r)=N^−1/2 L_cell(φ)，projected arithmetic项精确满足

    O_D(r)≤ηL_cell,u(r)+(3/η)logN||r||²_(du)。        (6)

因此(6)是真实合法源上的独立算术账本付款，但**仅付款 D-part**，
不能把 arithmetic divisor bookkeeping单独标为新whole或宏观forcing。

## 4. 原 Fourier矩阵与 non-divisible leak 非紧性

取单child n=qj+r，profile e^(2πik t)、k≠0。父cell上的实际输出是
sqrt q·e^(2πik(qv−r))1_(r/q,(r+1)/q)(v)。其目标频率 m 的 exact coefficient是

    (U_q)_(m;child k)=q^−1/2 e^(−2πimr/q)
                           ∫_0^1 e^(2πi(k−m/q)t)dt。 (7)

m=0时为零。m=qℓ时仅 ℓ=k 的项非零，系数 q^−1/2；所有children对
该频率的 e^(−2πikr) 因子为1。因此 D-part精确读取

    (D_q f)_(j,qk)=q^−1/2Σ_(0≤r<q,qj+r≤N−1)f_(qj+r,k)。 (8)

(8) 保全部children而非仅r=0，Cauchy亦直接证D_q contraction。
但 m不可被q整除时 (7)一般非零。实际 one-sided prime严格分成

    U_q=D_q+C_q，C_q=(I−P_q)U_q；
    O_full(r)=O_D(r)+N^−1/2·2Σ_(q<N)Λ(q)/sqrt q Re〈C_qφ,φ〉。 (9)

不省 (9) 的signed carry，也不以D-part的频率occupation代全prime。

在任意固定 N≥4，取 q=2、父j=1、单child n=2（r=0），
φ^(k)只在cell2取 e^(2πikv)，k→+∞。它们正交、norm1、weak→0，
对应 r_k=aφ^(k)是合法 R_a∩Dlog BV源。目标 m=2k+1给

    |(U_2 φ^(k))_(1,2k+1)|=sqrt2/π。               (10)

此外 ||U_2φ^(k)||=1、D_2仅有频率2k且平方norm=1/2，故

    ||C_2 φ^(k)||=1/sqrt2，所有k。                  (11)

由 weak-zero有界序列，(11)证明 C_2 **非compact**。
任何fixed finite-rank K都满足 ||Kφ^(k)||→0，因而
liminf||(C_2−K)φ^(k)||≥1/sqrt2。
原du归一化只乘共同 N^1/4，不改变这一结论。
也可直接核全部signed carry算子 K_C=Σ_(q<N)Λ(q)/sqrt q·(C_q+C_q*)：
在上述cell2序列上，投影到父cell1的输出只有 q=2 的forward项；
q≥3的forward为空，所有adjoint项支持在 x≥2q≥4。因此该cell1分量norm
恒为 (Λ(2)/sqrt2)(1/sqrt2)=log2/2，K_C同样非compact。
这个负对照保multi-q，仍只是免费compact删除的反例。
这排除免费/finite-rank删除该实际 carry 的运输捷径；不反驳某个有Γ费用的
全carry相对界，也不证明完整Q负性或两个worstfees同源同时饱和。

如需在547旧R作同类负对照，可将singlechild e^(2πikv)改为
e^(2πikv)−c_k，其中 c_k=(∫e^(2πikv)/sqrt(n+v)dv)/(∫1/sqrt(n+v)dv)=O(1/k)。
它准确满足旧weighted mean，且 (10)/(11)的非零极限保持；这仍只核非紧carry，
不把(5)的zeroordinarymean occupation误赋给旧R。

## 5. 能消费什么、不同于546及最小未付门

新 R_a 是整个成长区间的余维 N−1 complement，含任意cell内独立complex profile。
546只给 thincomb正域且其补空间仍捕获fixed core；这里改变了几何对象，
不是重新用thincomb结论完成一遍Goal。finite-codimension minmax可以消费
**若另已付款**的 full R_a Γ-relative/carry界，用来约束 whole负惯性；
head/mixed的PSD责任与此不同，(3)仅删除detail pole。

然而本稿尚未付款：

- L_cell,u 与actual zeroextension Γ=2θ′ 的 uniform-N norm/domain比较；
  unitcell periodic Fourier energies不能直接当作actual Γ。
- (9)的全部 non-divisible signed carry之Γ-relative费用。非紧性不排付费逃逸。
- Π^a/R_a 的成长coupling、head和全mixed；不继承旧547/548的投影或canonical费用。
- 结合上述后能胜016/028/543等最强旧资产的完整净后果，以及成长谱/Ξ识别。

一个明确可审的后续门是同时付款

    L_cell,u(r)≤A JΓ(r)+C logN||r||²，
    O_C(r)≤δ JΓ(r)+C_δ logN||r||²，ALL N、ALL r∈R_a∩Dlog，

并保全量词/域，使occupation系数 ηA+δ<1。当前没有预付这些式子；
不能用“准备算术输入”消去C或宣布原547 candidate已证。
若某合法source-adapted合并给更弱充分费用，也须先核与最强旧的净差。

结论：changed-head occupation来源准备成立，免费/finite-rank carry捷径明确失败；
actual Γ与fullcarry主门仍open。本稿零轮、无新合同或Goal完成声明。
