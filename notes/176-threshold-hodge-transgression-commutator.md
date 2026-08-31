# NCE-2：threshold Hodge transgression、交换子障碍与小谱修正

文档 174 提议用 threshold Hilbert complex的小 Laplacian谱控制文档 173 的
clipped residual。本笔记首先证明一个必要修正：**小谱密度本身不可能控制到
正算术锥的距离。** 要让 supersymmetric bulk cancellation在插入 logarithmic
incidence后仍成立，真正需要控制的是 incidence insertion与 threshold Dirac
operator的交换子。

本笔记给出 inserted McKean--Singer的精确 transgression公式、谱密度上界及
diagonal face weights的 boundary-gradient恒等式。由此，NCE-2 的开放输入从
模糊的“小谱少”改成两个可分离量：

1. harmonic boundary capacity；
2. incidence--Dirac commutator capacity。

**后续接口修正（文档 178）：** 对文档 167 的 canonical Type II lift，external
feature在每个 `K_U(q)` fiber上为 scalar identity，故交换子严格为零，内部
harmonic reduction已经精确。交换子定理只用于 face-dependent refinement；真实
未决量是不同 fibers经 logarithmic interval synthesis后的 external Bessel
capacity。文档 178证明其 universal尺度为 `Theta(1+Nh)`。

## 1. 小谱密度单独不足

### 命题 AEN（spectral-density-only no-go）[U]

不存在一个只依赖 `Delta` 在 `[0,lambda_0]` 上谱质量、且当该谱质量为零时也
为零的 universal bound，可以对任意 closed positive cone `K` 与向量 `X`
控制 `dist(X,K)^2`。

#### 证明

取 `H=R^2`、`Delta=I`、`0<lambda_0<1`、`K=R_+^2` 与
`X=(-1,-1)`。此时

`1_[0,lambda_0](Delta)=0`,                      (1)

但

`dist(X,K)^2=2`.                                (2)

故任何仅由小谱计数、且在零小谱质量处消失的上界都失败。`□`

该反例说明：必须另证 high-spectrum part落入正算术锥，或证明 incidence与
Hodge differential相容。谱隙只会放大这种相容性，不能替代它。

## 2. Inserted McKean--Singer transgression

令 `C=C^+ direct_sum C^-` 是有限维 `Z/2`-graded Hilbert space，grading为
`Gamma`。令 `D=D^*` 为 odd operator，

`Gamma D=-D Gamma`, `Delta=D^2`,                (3)

并令 `P_0=1_{0}(Delta)`、`P_+=I-P_0`。对 even operator `A` 定义

`Str(A)=Tr(Gamma A)`,                            (4)

`F_A(t)=Str(A exp(-t Delta))`.                   (5)

记 `Delta^dagger` 为在 `P_+C` 上的 inverse、在 kernel上为零的
Moore--Penrose inverse。

### 定理 AEO（inserted Hodge transgression）[U]

对每个 `t>=0`，

`F_A'(t)=1/2 Str([D,A]D exp(-tDelta))`,          (6)

并且

`F_A(t)-Str(AP_0)`

` =-1/2 Str([D,A]D Delta^dagger`

`                     exp(-tDelta)P_+)`.         (7)

因此

`|F_A(t)-Str(AP_0)|`

` <=1/2 ||[D,A]P_+||_HS`

`   *(sum_(lambda>0)e^(-2tlambda)/lambda)^(1/2)`, (8)

其中正特征值按 multiplicity计。特别地，若 `[D,A]=0`，则

`F_A(t)=Str(AP_0)` 对所有 `t>=0`。             (9)

#### 证明

`A` 与 `exp(-tDelta)` 都是 even，而 `AD exp(-tDelta)` 是 odd。supertrace
消灭 supercommutators，所以

`0=Str([D,AD exp(-tDelta)]_s)`

` =2Str(A Delta exp(-tDelta))`

`   +Str([D,A]D exp(-tDelta))`.                 (10)

结合 `F_A'(t)=-Str(A Delta exp(-tDelta))` 得式 (6)。当 `t->infinity`，
`exp(-tDelta)->P_0`。从 `t` 到无穷积分，并用

`int_t^infinity D exp(-sDelta)ds`

` =D Delta^dagger exp(-tDelta)P_+`,             (11)

得到式 (7)。最后以 Hilbert--Schmidt Cauchy--Schwarz及 `Gamma` 的酉性估计
trace；第二个 Hilbert--Schmidt norm的平方正是式 (8)中的谱和。`□`

若正谱底为 `lambda_1>0`、正谱总维数为 `N_+`，式 (8)给较粗但直观的

`|F_A(t)-Str(AP_0)|`

` <=1/2 ||[D,A]P_+||_HS`

`    sqrt(N_+/lambda_1)e^(-tlambda_1)`.         (12)

更一般地，式 (8)的第二因子可写成 spectral-density积分

`[int_(0,infinity)e^(-2tlambda)lambda^(-1)dN(lambda)]^(1/2)`. (13)

所以小谱密度只控制 transgression的传播因子；算术内容位于 `[D,A]`。

## 3. Face-weight insertion 的精确 boundary gradient

对有限 simplicial chain complex取 orthonormal oriented-face basis。令
`A_w` 是 diagonal even insertion，

`A_w e_S=w(S)e_S`.                              (14)

若 `partial` 的 incidence coefficient为 `[S:T] in {0,+-1}`，则

`[partial,A_w]_(T,S)`

` =[S:T](w(S)-w(T))`.                           (15)

对 Hodge--Dirac `D=partial+partial^*`，

### 定理 AEP（incidence commutator = shell gradient）[U]

有精确恒等式

`||[D,A_w]||_HS^2`

` =2 sum_(T face S)|w(S)-w(T)|^2`,              (16)

其中对每条 oriented codimension-one incidence只计一次。若只在一个 face
transition集合 `B` 上权发生变化，则交换子完全支撑于 `B`。

#### 证明

式 (15)由逐矩阵元计算。`[partial^*,A_w]` 是
`-[partial,A_w]^*`，二者位于相反 grading blocks，因此 Hilbert--Schmidt
平方相加，得到式 (16)。`□`

对文档 166 的 multiplicative threshold complex，face transition
`T -> S=T union {p}` 对应 divisor由 `d` 变成 `pd`。若 `w` 是 logarithmic
window、Fejer incidence或平滑 modulation，则

`w(S)-w(T)=w(pd)-w(d)`.                         (17)

于是有两类具体控制：

- hard threshold weight时，式 (17)只支撑于 crossing shell；
- `L`-Lipschitz logarithmic weight时，
  `|w(pd)-w(d)|<=L log p`。                     (18)

这把文档 166 的 one-vertex shell localization从 Euler characteristic提升为
一个 operator commutator ledger。

## 4. Harmonic capacity 与 clipped residual

令 `J_T` 是把各 `q` 的 inserted supertraces综合到 height block `H_T` 的
joint incidence synthesis；所有 prime、continuum、Gamma项必须在进入
positive cone `K_T` 前完成 gluing。假设存在 `E_T in K_T` 及分解

`X_T=E_T+J_T h_T+r_T`,                          (19)

其中

`h_T(q)=Str(A_(q,T)P_(0,q))`                    (20)

是 harmonic boundary ledger，而 `r_T` 是式 (7)的 transgression综合。

### 定理 AEQ（commutator-corrected Hodge cone criterion）[C]

在式 (19)下，

`dist(X_T,K_T)`

` <=||J_T h_T||+||r_T||`.                       (21)

若对某个 `t_T>=0`，`r_T` 可由逐 `q` 的式 (7)经一个 Bessel synthesis
majorant控制，且

`sum_T (||J_T h_T||+||r_T||)^2<infinity`,       (22)

则文档 174 的 AEJ/文档 173 的 AEG 给出中心线结论。

#### 证明

式 (19)中 `E_T in K_T`，故 metric distance不超过
`||X_T-E_T||`，再用 triangle inequality得式 (21)。式 (22)给 clipped
residual的可和上界，应用 AEJ/AEG。`□`

式 (21)刻意不把 harmonic项与 transgression分别解释为独立 prime/Gamma
budgets；`J_T` 必须是 joint synthesis，否则会丢失文档 153、170 强调的 cross
cancellation。

## 5. 非构造性真正出现的位置

这条路线可以在三个位置使用非构造工具：

1. `P_0` 由 spectral theorem自动产生，不必显式选择 homology basis；
2. 若只知道有限层 harmonic ledgers一致有界，可由弱 compactness选择极限；
3. 一旦式 (22)成立，positive arithmetic cone中的最近点由 AEI自动存在。

但式 (16)、(18)与 synthesis Bessel bound仍必须由 arithmetic incidence证明。
compactness不能替代这些 uniform estimates。

## 6. 下一步与停止条件

下一步应在一个 finite Type II rectangle上同时计算：

1. face weights `w_(q,T)` 对应的 exact commutator shell式 (16)；
2. harmonic ledger `h_T(q)` 的 gcd/profinite Gram；
3. transgression packets经文档 175 rank-one dual后的 Bessel常数；
4. prime/continuum/Gamma joint synthesis下式 (21)是否优于 full physical Gram。

NCE-2 的晋级条件是：得到 rectangle-uniform

`commutator capacity + harmonic capacity`       (23)

并且除以 Cauchy barrier后可和。停止条件是：若最小 commutator capacity与 full
near-product Gram等价，或 harmonic ledger可实现任意 rank-one packet，则本路线
只是另一种系数重写。

本笔记的无条件成果是 no-go、transgression与 shell-gradient恒等式；AEQ仍是
条件结构定理，不构成 RH 证明。
