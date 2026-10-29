# L=9/8：固定 μ=1/8 的新 inverse／congruence 准入

2026-10-29。只读原科学源码与新 scalar 结果后的限定代数推导；没有运行数值矩阵、producer、trial、Gram 或参数搜索，没有改 STATE／cadence／Git／原 source。本稿待 root 对齐前件后消费，不预付 C058／595 或完整 Q 正性。

## 1. 结论及旧门的准确角色

**29/32 是原证书选择的 μ，不是 Certification Theorem 的必要数学阈值。** 原 TeX 的一般 theorem 只要求 `0<m≤b`、`n<m`；inverse upper identity 只需 `0<μ≤m`。因此新 cosh 行已付 `m=15/64,b=433/64` 后，固定 `μ=1/8<m` 有合法独立逆上界。不能把“尚未付 m>29/32”读成整个新窗口认证失败。

代码门关于 `m>29/32` 的正确范围是**旧 `32B−29A` trial／旧整数模板原样沿用**所需的门。本文重导新的 `8B−A`、误差、清分母和正 congruence，不沿用该模板的数值常数。它给一次固定实例的可执行代数入口，仍不给新窗口有限目标符号，更不决定原 Q 的正负。

本稿实际读：恢复 b6cd2183c1e79c6c27a34267812a7b2d73ed1b59 的 `publication/manuscript.tex` 一般 Certification Theorem（538–682）、inverse upper（391–411）、raw normalization（367–387）、projection／tail（1367–1418、1735–1792）及 Appendix E（1802–1910）；全文读科学模块 03、04、05、06、09、10、13、14。另读本门 scientific-code-and-precision-gate、analytic-transport-and-parameter-stop。固定源 bytes 的验包责任仍见 root 恢复收据，本文不是另一次全文验包或文献新版本。

## 2. 对象与不借用的费用

沿同一原 `L²((-9/8,9/8),du;C)`、zero-extension Dlog 和 448 个 Legendre modes。保全 pp2,3,4,5,7,8,9 的 M 与 `B=E*M²E`；B 不是 A²。V 在一般 theorem 中指完整 `K+U`，而下文整数矩阵另记 `V_int`，避免混同。

承接 root 的新 scalar：`||Cp||<209/64`，故 `m=15/64,b=433/64`；候选 `13/4` 失败仍保留。采用固定 `r=2^-85,p=2^-440` 时，一般解析误差候选为

    e=1389r+p, n=896r²+p, h=11696r²+p。

r 的整数 scalar PASS 不自动支付这个 projection theorem、全 cross／complement 或 p；这些要由 root 沿新 L 解析记录闭合。源费用 `εA=εB=2^-220`、`εH=2^-204+2^-220`、`σ=9·2^-512` 在本文所有后续数值编码中仍是**待新 source／column 完整认证的前件**。

## 3. 固定 μ 的逆上界，先于目标 sign

设 A=E*ME、B=E*M²E、G=E*M^-1E，X 是任意有限矩阵，`R_X=E−MEX`。直接展开（无需 X 自伴）给

    Uμ(X)=X+X*−X*AX+μ^-1(I−AX−X*A+X*BX),
    Uμ(X)−G=R_X*(μ^-1 I−M^-1)R_X ≥0。

M≥mI 和 0<μ≤m 先支付右边正号。没有用目标 P≥0、trial 最优性或某个数值 pivot。若 A0/B0 的正交坐标误差各≤ε，且 `||X||≤y`，则取 μ=1/8 得

    ΔX = [y²+8(2y+y²)]ε=(9y²+16y)ε,
    W=U_(1/8),0(X)+ΔX I ≥G>0。

这是旧 `(61y²+64y)ε/29` 的重新推导，不把旧 Δ 或 `||X||≤8` 照搬。y 可以是从实际 Z 完整 Frobenius 和得到的二进制上界；若另采用 y≤8，需要新实际 norm test。

固定 trial 仍可使用一次 stationary solve 提议 X：

    (8B0−A0)X=8A0−I。

其实际未扰动矩阵满足

    8B−A=E*M(8M−I)E ≥m(8m−1)I=105/512 I。

源中心误差≤ε 后，`8B0−A0 ≥(105/512−9ε)I>0`。所以 μ=1/8 已先付 trial solve 的正性前件；十进制 proposal 仍可能因具体精度／整数限制返回 inconclusive，不能据此判原 Q 负。即使不求 stationary trial，任意 X 也给合法 W，只是 finite comparison 未必够强。

## 4. 一次固定的新 Schur 预算

保持 θ=2^-48、χ=1，由一般 theorem 计算

    α=e·2^-48+2e²/(m−n),
    β=(2^48 e+n)/m²+2h²/[m²(m−n)]。

本稿只做 exact Fraction scalar，已检查 `n<m, α<2^-122, β<2^-22`。可冻结向上 dyadic `α0=2^-122,β0=2^-22`，免去旧 9617/63183 及 m−n 分母。

这个加大 β 的步骤合法，因为 `D_M=B−A²≥0`。有源误差时先保

    D_M ≤ D0+εD I,  D0=B0−A0²,
    εD=εB+(2b+εA)εA。

`D0+εD I≥D_M≥0`，所以用 β0 同时替换有限 D0 项和其 εD 付款，仍是一般充分条件；不能单独对可能不正的 D0 加大系数而删去误差。若新 εA/B=ε=2^-220 已付，则

    εD=(465/32)·2^-220+2^-440。

在新 εH、σ 也实际付清后，取

    λ0=εH+σ+α0+β0 εD
       =2^-122+2^-204+2^-220+465·2^-247+2^-462+9·2^-512。

需认证的有限矩阵就是

    P0=H0+Û+W^-1−λ0 I−β0(B0−A0²)。

`P0≥0` 足以支付一般 theorem 的全 Hilbert `M+K+U≥0`，再由原完整 comparison 的 tail 标量转回 Q 下界。本文尚无 P0 sign，没有替 root 消费该全型比较或 δ/16。

### 可便宜重闭的 576 解析 scalar

以下只算精确整数，没有运行新 columns／moments：

    576^2049·2^513 < 2·2049!                         PASS,
    914·576^2048·2^399 < 2048!                       PASS。

第一式配 π>2 给新 sinc operator Taylor 误差 `<2^-513`；第二式给 kernel Taylor `<2^-399`。旧代码的 544 不能因此留下，实际新 polynomial 必须用 576。

若新 1152-bit moment packet 完整独立包含且 width≤2^55，则 midpoint 误差≤2^-1098；`cosh576<2^864`（e²<8）给放大后 `<2^-234`，故 `(9/4)(2^-399+2^-234)<2^-204`。Binet 已在真 moment interval 内只付一次，不能另加旧表成功作假设。这个条件没有证明 6144/6400-bit 工作精度实际通过，仍须全 1024 项 containment／width／negative controls。

新 Γ 使所有 n<448,j≤1 有 `ΓnnΓjj>1/1024`（最小值取 n=447,j=1）。若 raw columns 的逐项误差 `<2^-524`，则 normalized column 误差 `<2^-514`；加 sinc、Machin `<2^-646` 后仍 `<2^-512`，再按已闭 h0/h1 norm 给 `σ=9·2^-512`。这里只重闭解析运输；896 项与 parity zeros 的实际 interval replay 仍未执行。

## 5. 原 norm 的完全有理 raw transport

设 `Q=diag(q_i), q_i=8(2i+1)`，i 是原 Legendre degree，`g=18, Γ=gQ^-1`，`S=2^257,R=2^256`。原新 raw integer centers a,b,j 代表 `a/S,b/S,j/S`，均 symmetric；`Ûraw=36∑t_s t_s*/2^1282`，其中完整 tail midpoint integers t_s 的分母为 2^641。每个 parity 只有相应一列非零，但公式可保两列。

取整数 Z，定义

    Y=QZ/R, X=Γ^(1/2)YΓ^(-1/2)
      =Q^(1/2)ZQ^(1/2)/R。

因此 `||X||²≤||X||F²=Σq_i q_j|Zij|²/R²`，原 q-grid 的 norm 计算结构不依 g；须对本次实际完整 Z 重新算。新 raw stationary solve 正是

    Q(8b−a)Q ·(Z/R)=8Qa−18S I。

只提议 Z，不给 finite sign。旧 `32b−29a`、`493=29·17`、旧 y 的执行数据不进入新计算。

令

    Cw=S R²=2^769,
    c=8Cw+(9y²+16y)2^549,
    F=18SR(Z+Z*)−Z*QaQZ+8Z*QbQZ−8R(aQZ+Z*Qa),
    V_int=QFQ+18cQ。

逐项由 §3 展开得到

    Wr=Γ^(1/2)WΓ^(1/2)=Cw^-1 Q^-1 V_int Q^-1。

这里 W>0 已在 sign 前由 inverse order 支付，故 Wr 和 V_int 都正定。V_int symmetric，每列可除以对应 q_j；这是必须实际核验的整数结构，不以目标 sign 反推。原输入为实数时用 transpose，数学全 complex norm/sign 用 adjoint。

## 6. 具体清分母与两个新 compiler 身份

固定 β0、λ0 后，定义 raw

    C0=j/S+Ûraw−λ0 Γ−β0[b/S−(a/S)Γ^-1(a/S)]。

取非奇异正运输

    Bc=Q^(-1/2)V_int/(sqrt(18) Cw)。

直接把正交坐标代回给

    18² Cw² Bc*P0 Bc = V_int C0 V_int+18² Cw V_int。

方向是原 Hilbert finite compression→raw→integer正 congruence，未换 physical norm；Bc 非奇异来自先前 W>0。整式只用 rational raw objects，Γ 的 square roots 在最终式完全消去。

在上述源误差和 tail grid 前件下，**明确可取** `T0=9·2^1282>0`。清分母后的全整数目标为

    K = cJ V_int j V_int + cU Σ(V_int t_s)(V_int t_s)*
        −cΓ V_int Q^-1 V_int −cB V_int b V_int
        +cAA (aV_int)* Q(aV_int)+cW V_int，

    cJ=9·2^1025, cU=324,
    cΓ=162·2^1282 λ0,
    cB=9·2^1003, cAA=2^745, cW=2916·2^2051。

每个系数是整数；`V_int Q^-1 V_int` 的整性由列可除 q_j 支付。Scalar exact check 的六个系数 bit lengths 依序为 `1029,9,1168,1007,746,2063`。恒等式为

    K=T0·18² Cw² Bc*P0 Bc。

所以完整 K≥0 才推出本次 P0≥0。未求任何历史 target／K*／factor；没有旧 607630911、1324960000、1309 或 3353-bit observed target scale。

两个独立实现可直接按以下等式核 whole-object equality，不需新的未明参数：

1. Direct compiler 逐项计算上式六个 contraction，单独检查所有 scalar integral、V_int symmetry／column divisibility。
2. Combined-kernel compiler 令 `Yv=V_int Q^-1`（整数），

       Ainner=cJ j−cB b+cAA aQa,
       Hinner=Q Ainner Q−cΓ Q+cU Σ(Qt_s)(Qt_s)*,
       K=Yv Hinner Yv*+cW V_int。

第二式使用独立累计顺序，且直接保 Γ／aQa 的角色。不能调用 direct compiler 来当“独立”结果。若以后源错误允许值变化，须改 λ0/T0 及积分清分母 record，不能继续用本节固定 coefficients。

### 有限整数 cap 的新上预算

若先核本次 source integers `|aij|,|bij|,|jij|≤2^273`、`|Zij|≤2^272`、`|t_i|≤2^641`，每 sector n≤224、q_i<2^13，则 Frobenius 允许取 `y≤2^37`。按 sum 项数 `<2^8`（二重 contraction `<2^16`）逐项累加，有 `|Fij|<2^864`、`|V_int,ij|<2^891`。上列 coefficients、`λ0<2^-121` 再给 `|Kij|<2^3200` 的保守上界。

这是重新推导的整数范围，不是要求实际 bit scale 等于某个旧观测值。原 Z cap 或 source cap 任一没过时，本上界不消费；可以准确返回 NONPASS，而非关掉 assert。实际矩阵未生成，本文没有验证这些 caps。

## 7. 完整 sign 的最后门与停止范围

仍须原新参数签名贯穿：15 shifts／225 ordered pairs、所有 source rows 的独立 containment／归一化误差、完整 896 tail coordinates、原完整 Γ／properpowers／双pole、全 complement／cross、stationary trial proposal与实际 norm、两个新 compiler 的全部 entries equality、两个完整 224-sector 的 integer residual rows。

最终 Gram 规则取一般形式：`K=aFF*+dI+Rcert`，`a≥0,d>0,max_i Σ_j|Rcert_ij|<d`，用 exact arithmetic 全行付正号。数值 Cholesky 只给 proposal；其 failed pivot 或單个 positive direction 都不代 sign。若选择旧 2^-480/2^-512 factor 格式，也必须核本次实际 scale b 和全行严格余量，不继承旧 observed 3353 或余量。原 09.gram_check 的布尔值只是 residual routine，不验证本节的 coefficient 语义；尤其不能绕过新 congruence。

存在合法新 μ 只解除“旧逆模板阈值不可迁移”这一局部门。新 finite target 可能因比较过粗或实际 source 精度返回 NONPASS，这仅停止这个固定 L／M／θ／μ／N 的认证，不推出 full Q<0，不自动授 L、weight、degree 或 θ 搜索。

当前可执行下一步是 root 先关闭新解析费用，再决定一个固定新 source pilot；尚无 whole certificate。即使最终扩大到 9/8 原全窗，也只是相对 17/16 的实际 fixed-window净增；primitive／principal／sections／mixed RR、growing core／coupling／Ξ 和长期 Goal 完成门均未由本稿支付。
