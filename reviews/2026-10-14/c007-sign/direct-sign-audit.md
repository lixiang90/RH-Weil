# C007 独立符号审查：真实首素数对数共振及严格有符号光滑源

2026-10-14。恢复 AGENTS、README、STATE/check/show、Goal、C007、
D20261014C，并核起始 HEAD `bbbd54c26e1f335c4238877a7954edd02146dab8`。
本文件只记独立推导，不改 STATE/cadence，不单独计轮。

## 1. 对象及消费界限

冻结 `a=log2,b=log(3/2)/4`，两 patch 中心为 `±a/2`，每 patch
保留 `ell_0=ell_{1/2}=0`。实际比较仍是

    E2(g)=(2pi)^(-1) integral |g-hat(s)|^2 epsilon2(s) ds,
    epsilon2=2pi rho2-K+2a sum_(n>=1)2^(-n/2)cos(nas),
    QW(g)-T2(g)=-E2(g).

`rho2` 包含实际完整 G2 逆；532 已付源紧性，没有付符号。
本审查不使用 C006 未认证角 trace 分离，不把正 T2 或 compact 当符号。
本轮早期只支付裸机制并明确拒绝消费 actual 符号；第 5–6 节保留该
早期审查记录。随后核读主代理 [trace-domain-proof.md](trace-domain-proof.md)、
来源 [source-sign-audit.md](source-sign-audit.md)，并以独立 cosine Plancherel
组织支付第 7 节的 S1 域及共同核极限。
**当前结论：第 4 节同一严格矩零 smooth 源满足
`E2(g_eta^±)=±sqrt2/(2log2) log(1/eta)+O(1)`，故 actual E2 两种符号均存在。**
没有执行数值实验；不声称给出了一个数值 eta 阈值。

## 2. 实际 h(K2)-K2 的尾给连续有界源核

物理偶 Fourier 归一化是 `F(x,z)=2cos(2pi xz)`。实际 p=2 低截断核为

    K2(x,z)=sum_(n>=0)cos(2pi 2^n xz)-cos(pi xz),  0<x,z<1,

按实际 operator-norm 收敛级数理解，不按逐点收敛理解。
534 的插值给 K2 in S_r for r>2，尤其 K2 in S3，且 ||K2||<1。
故完整 resolvent 的精确分解

    h(K2)=K2(I-K2^2)^(-1)=K2+J,
    J=K2^3(I-K2^2)^(-1)

有 `J in S1`。这是固定 p=2 的非扰动分解，保留完整逆。

令 L=低截断、H=I-L。若裸/尾的完整 trace 身份成立，尾的 quadratic
functional 是 `2Re Tr(J L Z_g H F2 L)`，`Z_g=A_g* A_g`。
置 `D=H F2 L J L`，则 D 是 ambient TC，norm1 不超过 norm1(J)。
由 cyclicity，尾为 `2Re Tr(A_g D A_g*)`。
函数 `d(t)=Tr(D U_t)` 因 U_t 强连续而连续有界，`|d(t)|<=||D||1`。
所以任何有界 L1 质量的窄源在该尾上的值一致有界。

更强地，压到任意有限测度源 U，该尾是 **source TC**，费用
`<=2|U| ||D||1`。证明：D 的核范数分解 `sum s_j |f_j><h_j|`
满足 `sum s_j=||D||1`；映射 `B_f:g -> A_g f` 的 HS 平方为
`|U| ||f||2^2`。每个 source block `B_h*B_f` 为 HS×HS，TC norm
不超过 `|U|||f||||h||`，绝对相加即可。
仅 TC 本身不推出高载波 o(1/R)，这里没有使用该错误推论。

## 3. 相邻真实二进尺度在 t=log2 的对数共振

对任意正尺度 r1,r2，定义真实裸 low/high cross 的标量核

    I_(r1,r2)(t)=e^(t/2) integral_(e^-t)^1 integral_0^1
                     cos(2pi r1 xz)cos(2pi r2 e^t xz) dz dx,  t>0.

设 A=r1-r2 e^t,B=r1+r2 e^t，则精确为

    e^(t/2)/(4pi) * {
       [Si(2pi A)-Si(2pi A e^-t)]/A
      +[Si(2pi B)-Si(2pi B e^-t)]/B },

在 A=0 用连续极限。实际核 `I2(t)` 是上述核按尺度
`r_n=2^n,n>=0`，系数 +1，及 `r_-1=1/2`，系数 -1 的双和。
这不是另造 Fourier 模型：每个项来自实际 F2 的完整 norm 级数。

在 t 的 a 邻域，唯一无限共振族是 `r1=2^(n+1),r2=2^n,n>=0`。
令 delta=t-a，A=2^n(2-e^t)。在 delta=0，该族每项的差相位项为

    e^(a/2)(1-e^-a)/2 = sqrt2/4.

和相位项 B 的和绝对收敛。对于 `2^n|delta|<=c`，Taylor 余项为
`O(|delta|+(2^n delta)^2)+O(4^-n)`；相加 O(1)。对更高尺度，
Si 端点差及其 pi/2 消去给 `O(4^-n delta^-2)`，尾和仍 O(1)。
所有非共振尺度在该邻域满足 `|A|>=c max(r1,r2)`；同一 Si 端点
估计给 `O(max(r1,r2)^-2)`，双和绝对有界。涉及 n=-1 的项有限，
不能改变对数系数。因此作为局部可积实际裸核，

    I2(t)=sqrt2/(4a) log(1/|t-a|)+O(1),  t -> a.       (A)

有界余项可以有 log-periodic 波动；没有声称它有导数或高频小余项。
此机制在 C006 p>=3 的固定 U 上不存在，因为那里 e^W<p 有相位 gap。

在 t=0 邻域，同尺度族给 `O(t(1+log(1/t)))`：当 rt<=1 时每项
`O(t)`，当 rt>1 时 Si 差给 `O(1/(r^2 t))`，分别相加即可。
非同尺度的 gap 估计绝对可和，每一项在 0 为 0，故 dominated
convergence 给连续零极限。因而 I2 在 0 附近有界；它没有在 self
channel 中产生 (A) 的对数发散。所有别的二进共振 n a 都在冻结
差支持 W=log sqrt6<a*2 外。

## 4. 严格合法的矩零窄源及裸 signed 后果

取非负 `phi in Cc-infinity(-1,1)`，integral phi=1。
取两个固定非负归一化 smooth bumps `psi_-,psi_+`，分别支撑在
`-b/2,+b/2` 的足够小邻域，避开 0。其 ell_(1/2) 值 m_-<m_+。
对 0<eta 足够小置 `phi_eta(y)=eta^-1 phi(y/eta)`，并令

    c_-+c_+=1,
    c_- m_-+c_+ m_+=integral e^(y/2) phi_eta(y) dy,
    h_eta=phi_eta-c_-psi_--c_+psi_+.

矩阵可逆，系数随 eta 一致有界。于是 h_eta 支撑于原 patch，
严格同时有 ell_0=ell_(1/2)=0，L1 norm 一致有界。定义原合法源

    g_eta^±(t)=h_eta(t+a/2) ± h_eta(t-a/2).

每一个 eta 都是明确合法 smooth 源；没有用近似矩零或不同支持。
裸功能定义为

    B2(g)=2Re integral_0^W R_g(t) I2(t) dt.

两 patch self channel 因第 3 节的 t=0 有界核及有界 L1 质量一致有界。
cross 中仅 phi_eta 与其同形 translate 的配对有 logarithmic 发散。
以 y=eta v,u=eta w 缩放，(A) 给 `log(1/eta)+O(1)`；
`integral phi(v)phi(w) log(1/|v-w|)dvdw` 有限。
所有 fixed correction/correction 或 narrow/fixed 配对一致有界，
因为 logarithmic singularity 在固定 smooth bump 上局部可积。
所以严格得到

    B2(g_eta^±)=±sqrt2/(2a) log(1/eta)+O(1).             (B)

第 7 节已经支付第 5 节早期留下的身份前件，连续有界尾不能改变 (B)，
因此同样渐近严格成为 actual E2 的有符号反例。尤其正号给合法 smooth 源 E2>0，否定
`QW>=T2` 无费桥；负号也有 E2<0。这只否定该比较，不否定 QW>=0。
本节的窄源证明本身只给两种符号；无限指数若消费，另核来源稿的
对角 S1 / cross 非S1 与有限余维压缩证明，不从单个 Rayleigh 冒称。

## 5. 本轮早期记录：曾未付的唯一消费前件

以下保留早期审查，不是第 7 节支付新域以后仍未付的状态。

两投影的 exact bounded block operator 给 actual overlap R2。
在 K2 的每个 generic angle 平面，Z_g 与实际 F2 交换（real 源的
|g-hat|2 偶），因此有限角代数给

    Tr_angle(Z_g R2)=2Re Tr_angle[h(K2) LZ_g H F2 L].

但 A_g R2 A_g* 已知 TC，**不自动保证**任意有限角 trace 的共同极限。
需要新证明 actual smooth-source 的 absolute angle trace，或者直接
从双 cutoff block identity 支付 scalar distribution trace 的共同极限，
使

    E2(g)=B2(g)+2Re Tr(A_g D A_g*)                     (C)

合法成立。C006 未付的 jointtrace 身份不能照搬。
K2^3 TC 使 (C) 比 C006 的非交换多 δ 展开明显更便宜，但它本身没有
证明裸 K2 M 的 trace regularization 与已知 actual trace 一致。
特别是 `A_g|R2|A_g*` TC 不是已有 `A_gR2A_g*` TC 的推论。

一个不用 absolute-angle trace 的新具体组织如下。按 low/high 写
`F2=[[K,T*],[T,Dh]]`，则 `T*T=I-K^2,Dh T=-TK`。置

    Y=[[0,K^2 R0 T*],[-T K^2 R0,0]],  R0=(I-K^2)^(-1).

直接 block 相乘给精确 bounded identity

    R2=R_bare+R_tail-(1/2)[F2,Y],
    R_bare=[[0,KT*],[TK,0]],
    R_tail=[[0,K^3R0T*],[TK^3R0,0]].

R_tail 为 ambient TC。**如果**另付 `A_gR_bare A_g*` TC，则剩余
source commutator 也 TC，并且其 trace 严格为零：Z_g 的平方根与
F2 交换，A_g 的 Fourier 极分解把 source commutator 的 trace 化成
`Tr[F2,Z_g^(1/2)Y Z_g^(1/2)]`。一个 bounded involution F 与任意
bounded Y 的 TC commutator 在 F 的 ± eigenspace 中对角均为零，故
trace 为零。这避免把强收敛当 trace 收敛，也避免拆无限角绝对和。
这里 `A_gR_bare A_g*` TC 仍是需要支付的真实 smoothing 前件；
仅证明 `A_g L K2` HS 不足以支付它。本文件未把该替代证明路径当完成。

## 6. 本轮早期交付记录

新增独立输入：实际 p2 裸核的精确 logarithmic cross 共振、严格矩零
窄源的裸 signed 渐近，以及完整 resolvent TC 尾的连续源核/source TC
传递。实际 E2 符号的消费瓶颈缩到 (C) 的共同 trace 身份，没有被消除。
不把此有希望的条件反例算宏观 Goal 完成，不改 frozen samples。
本辅助审查无后台计算/下载进程。

唯一下一动作：用实际双 cutoff block 或 smooth-source absolute-angle
估计支付 (C)，然后将同一 g_eta^+ 的 (B) 消费为实际反例；若 (C)
本轮未付，保留此精确前件，不能无声升级裸功能为 actual E2。

## 7. 同轮新输入的不同组织核查：前件现已支付

恢复 STATE/check/show 后核 HEAD 仍为 bbbd54c；当前 worktree 新文件均属
同轮 C007 独立输出。Goal/C007/D20261014C 对象和量词保持。
下面的证明不使用早期 commutator 条件路径，也不调用 C006 的角截断。

### 7.1 精确 Plancherel 平滑费用

对 `F_r(x,y)=2cos(2pi rxy),r>=1`，输出改 unitary log 坐标 u，
输入保留 physical y∈(0,1)，`A_g L F_r L` 的 kernel 准确为

    B_r(u,y)=2 integral_0^1 g(u-log x)x^(-1/2)cos(2pi rxy) dx.

取 supp g⊂[−c,c]。按完整 cosine Plancherel，在每个 u 上有

    integral_0^infinity |B_r(u,y)|^2dy
       =r^-1 integral_0^1 |g(u-log x)|^2 dx/x
       <=r^-1 ||g||2^2.

输出导数只把 g 换 g'，相同 row 费用成立。故在
`J_r=[−log r−c−d,c]`（fixed d>0）上，向 H1(J_r) 的 map 为 HS，
费用不超过 `C_g sqrt((1+log r)/r)`。Neumann cosine 谱直接给
`H1(J_r)->L2(J_r)` embedding 的 HS norm 不超过 `C sqrt(1+|J_r|)`。
HS×HS 得中段 S1 norm `C_g(1+log r)/sqrt r`。无需对输出端点加边界条件。

深输出 u<−log r−c−d 的 cos Taylor 为绝对核范数收敛 rank 列

    2 sum_(k>=0) (-1)^k (2pi r)^(2k)/(2k)!
        *e^((2k+1/2)u) y^(2k) I_k,
    I_k=integral g(t)e^(-(2k+1/2)t)dt.

输出和输入 rank norm 的乘积为
`e^((2k+1/2)u0)/(4k+1)`，而 `|I_k|<=||g||1 e^((2k+1/2)c)`。
全部 r^(2k) 消去后仅留 r^-1/2；factorial 列绝对可和。
u>c 的输出严格为0。所以独立得到

    ||A_g L F_r L||1 <= C_g (1+log r)/sqrt r.          (D)

这项 C_g 有固定 support/导数费用，绝不当 whole-source L2 uniform bound。
实际 dyadic 系数使 (D) 可求和，低反向 r=1/2 为 smooth S1 核。
因此 `A_g L K2` S1 且 scale cutoff 在 S1 norm 收敛。
完整 inverse bounded 给 `A_g L h(K2)` S1；反演源同样成立。

### 7.2 完整 overlap 的 ordinary trace 身份

写 `F2=[[K,T*],[T,Dh]]`，真实 overlap 的四块为

    R2=[[K^2,KT*],[TK,-T K^2(I-K^2)^(-1)T*]].

置 `X=Lh(K)L F2 H`，block 相乘及 `Dh T=-TK` 给精确 bounded identity

    R2=X+F2 X F2.                                   (E)

(D) 使 `A_g X A_g*` S1。real g 有 `F2 A_g*=A_g F2`，反演源的 (D)
使另一半 `A_g F2 X F2 A_g*` 也单独 S1。
normal A_g 满足 A_g*A_g=A_gA_g*=Z_g；Z_g 与 F2 交换。
因此兩半可合法循环，给

    E2(g)=2Re Tr_low[h(K2) L Z_g H F2 L].             (F)

fixed smooth g 的 `LZ_gH` 更是 S1：只连接有限 physical rectangle，
kernel 为 smooth 的 `R_g(log(y/x))/sqrt(xy)`；先在 rectangle 外作
smooth 延拓，H1/HS factorization 给 S1，再乘 cutoff projection。
于是 (F) 的 low trace 本身也是 ordinary trace，不需任何条件角和。

完整 `h(K)=K+J` 中 J ambient S1，故源夹心和普通 trace 可直接分离。
第 2 节连续有界尾确为 actual return，而非另设局部功能。

### 7.3 两次 scale cutoff 和核归一化

第一个 K2 scale cutoff 经 (D) 在 source S1 norm 收敛；第二个 F2
scale cutoff 在 operator norm 收敛。TC×bounded 正当控制其共同 trace
极限，不能把非酉有限 F2 cutoff 代成新的 Sonin 投影。
每个有限 pair 的 physical trace 就是第 3 节 I_(r1,r2) 的普通积分。

double pair 在冻结 t∈(0,W) 的 L1 norm 绝对可和：
相邻共振列在 t=a 近旁满足 `C min(1,4^-m|t-a|^-2)`，积分 O(2^-m)；
same-scale 在 t=0 近旁满足 rt<=1 的 Ct 和 rt>1 的 C/(r^2t)，
L1 费用 O((1+log r)/r^2)。其余 ratio 有严格 gap，max scale r 的
L1 费用 O(r^-2)，每个 max index 只有 O(m) 个 pair。有限反向块无影响。
故绝对 L1 求和确定同一 actual bare functional，身份 (C) 已支付。

**倍数核查：** 本文件 I2 采用 actual 振幅1 cos×cos，
`I2(a+delta)` 的 log 系数 c0=sqrt2/(4a)。
(F) 给 `B2(g)=2Re integral_(t>0) R_g(t)I2(t)dt`。
对 real 源，等价为 `integral_R R_g(t)I2(|t|)dt`；even 延伸后不得再乘2。
g_eta^± 在 positive a 只有一个 cross autocorrelation，negative a 由
even 延伸补另一个。因此 (B) 的系数严格为 ±2c0，
即 `±sqrt2/(2a)`，不是 ±4c0。

## 8. 当前可消费结论与实际限制

第 7 节以新 fixed-smooth S1 输入支付此前真正缺失的域。
同一冻结合法源 g_eta^+ 对所有足够小 eta 严格有 actual E2>0，
g_eta^- 严格有 actual E2<0，渐近常数如第 4 节。
这排除整个冻结 V 的 `E2<=0` 和 `E2>=0` 两条无费比较；
特别正源使 `QW-T2=-E2<0`，而未证明 QW 本身负值。
源归一化会使值变为 eta log(1/eta) 量级，与532紧性相容。
无需ζ零点、无精度迭代、无给定 eta 数值阈值或有限矩阵代替全域。

独立输入改变了 actual first-prime bridge 的剩余符号箭头：域与符号
现在已付为严格失败；actual QW 正性、lowest、conditioned base-S/
growing-S/U 和宏观 Goal 门槛仍未完成。不自动复活旧修复或 C006预算。
本辅助输出無 pending process；后续唯一主动作由父代理综合逆审及 STATE
决定，不在本文件另立合同或消费 cadence。
