# Modular packet 的原范数、完整 cusp 盲带与 Weil 运输门

2026-10-14；C016 一次完整来源准入。冻结基线仍为 0c4f3a3、全部≤538。
原 classical 工具恢复不计新结果；本轮交付是指定 actual source 的全频费用、
直接 uncompleted 逃逸及完整扣费后全源 frame 失败范围，不是 RH 或宏观 Goal 完成。
独立审查：[classical/completion](../reviews/2026-10-14/c016-first/cusp-completion-and-norm-audit.md)、
[physical packet](../reviews/2026-10-14/c016-first/whole-frequency-packet-and-object-gate.md)、
[actual对象/宏观净值](../reviews/2026-10-14/c016-first/actual-weil-and-macro-net-audit.md)。
最终消费版本和来源 byte hashes 另存 root-consumption-scope.json；准备消息不当作最终原件。

## 1. 冻结对象与已知工具的准确归属

M=PSL₂(Z)\H，dμ=dxdy/y²，cusp 周期宽度1。Λ(w)=π^(−w/2)Γ(w/2)ζ(w)，
不是 entire ξ。原 normalized Eisenstein 的常数项是

    E(z,s): y^s+φ(s)y^(1−s)，φ(s)=Λ(2s−1)/Λ(2s)。

Zagier §2 原展开/函数方程及 Garrett 的 truncation/unfolding proof 为已知工具，
作者原 PDF/text 已逐字节冻结于[c015来源收据](../reviews/2026-10-14/c015-admission/sources/macro-primary-source-receipt.json)。
用原 classical measure 独立 Green identity 得 common factor1 的四项：

    G_Y(s,w)=[Y^(s+barw−1)−φ(s)barφ(w)Y^(1−s−barw)]/(s+barw−1)
       +[barφ(w)Y^(s−barw)−φ(s)Y^(barw−s)]/(s−barw)。

所有 coalescence 按 removable limit，不能从 GL(n) 规范偷用常数。
E*=Λ(2s)E 只有 s=0,1 的简单极点，residue 分别 −1/2,+1/2；
s=1/2 的两个 constant poles 内部相消。F=s(s−1)E* entire。
原 Bessel 非零 modes 在参数 compact 上一致指数衰减，故

    F_Y=F−1_(y>Y)[α(s)y^s+β(s)y^(1−s)]，
    α(s)=s(s−1)Λ(2s)，β(s)=s(s−1)Λ(2s−1)，Y≥2

是 compact-uniform holomorphic 的真实 L²(M) family，保所有 finite parameter jets。
F_Y(0)=F_Y(1)=1/2·1_(y≤Y)，norm²=(π/3−1/Y)/4；这不是 actual dual-pole 型。

原 physical 空间始终为 complex L²(I_L)，I_L=(−L,L)，Lebesgue norm、零延拓，
hat f(t)=∫f(u)e^(−itu)du；Dlog={∫log(2+|t|)|hat f|²<∞}。
冻结 s_t=1/4+it/2，2s_t=1/2+it 为 actual ζ 变量；不用有限频窗、偶实条件或未知 ζ 位置。

## 2. Completed packet：全轴费用、极化及完整扣费

写 α(t)=α(s_t)，β(t)=β(s_t)。原 MS 对角式在 t≠0 给

    ||F_Y(s_t)||²=2√Y|β(t)|²−2Y^(−1/2)|α(t)|²
          +2 Im[α(t)barβ(t)Y^(it)]/t。                         (1)

t=0 的 mixed 商以导数支付。head 上 α、β及一阶导数有 compact 上界，
|sin(t logY)|≤|t|logY、logY≤C√Y，使 head 费用对全部 Y≥2 有界于 C√Y。

Euler 求和（N=ceil(1+|t|)）直接给 |ζ(1/2+it)|≤9√(1+|t|)。
Λ 功能方程给 β=s_t(s_t−1)Λ(3/2−it)；Euler/Möbius 绝对级数给
1/3≤|ζ(3/2−it)|≤3。结合[NIST Γ竖线双尾](https://dlmf.nist.gov/5.11.E9)，
对全实 t 有

    |α(t)|+|β(t)|≤C(1+|t|)^(9/4)e^(−π|t|/4)，
    ||F_Y(s_t)||²≤C√Y(1+|t|)^5e^(−π|t|/2)。                 (2)

这些费用不含 critical zero-free 前件，正负双尾均保留。于是

    A_Y f=(2π)^−1∫_R hat f(t)F_Y(s_t)dt

在整个 L²(R) 上是 absolute Bochner、Hilbert–Schmidt map，
||A_Y||HS²=(2π)^−1∫||F_Y(s_t)||²dt≤C√Y。
限制到原 L²(I_L) 不增加费用；Dlog 为同一 source 的限制，非换 norm。
双频极化由 |H_Y(t,r)|≤||F_Y(t)|| ||F_Y(r)|| 的绝对可积性付 Fubini。
截频 tail operator error ≤C Y^(1/4)(1+T)^(5/2)e^(−πT/4)，不是有限样本推定。

F₂ 在 2<y≤Y 只有非零 x-modes，F_Y−F₂ 在该 band 为完整 constant mode。
正交性对所有 complex 原源给

    <A_Y f,A_Y g>−∫_2^Y c^*_f(y)bar(c^*_g(y))dy/y²
        =<A₂ f,A₂ g>。                                      (3)

扣费不是只减 2logY 或某个 scalar。任何 finite Y(L)≥2，甚至单源 finite Y(f)，
扣完整同一 mode 后对角净值仍为 ||A₂f||²；后者不能自动称作 source-adaptive linear Gram。
每 fixed L 的 A₂ 紧，任何 bounded 输入/输出/频权及 finite-rank 修复仍紧，不能给原 norm 的全源底。
此结论不排无界权、不同非紧 source、付费 cusp 或危险 core 上真正 signed 比较。

## 3. Inverse-domain 空域只否定一种操作，不能否定直接还原

β 全轴非零，且由 Γ 双边界及绝对 Euler/Möbius 系数有

    |β(t)|≍(1+|t|)^(9/4)e^(−π|t|/4)。                       (4)

因此 maximal inverse domain 满足

    Dom β(D)^−1 ∩ {f∈L²(R): supp f⊂[−L,L]}={0}，每 finite L。 (5)

若 hat f/β∈L²，则任意 0<a<π/4 有 e^(a|t|)hat f∈L²；
Fourier inverse 在 |Imu|<a 为 holomorphic 代表，compact support 外实开区间为0，
identity theorem 给 f=0。有限源条件或 finite L 成长不能改变此量词。
β 在自己的 analytic range 上当然有合法闭无界 inverse；(5)不排那种操作。

更重要的是，**直接 vector 补偿不是先 inverse 一个 L² source**。
函数方程给原件精确等式

    U_Y(t)=F_Y(s_t)/β(t)=E_Y(r_t)，r_t=1−s_t=3/4−it/2。       (6)

分母 Λ(2r_t)=Λ(3/2−it) 无零。(6)用 meromorphic 等式在 α=0 处消费，不能独立除 φ。
R(t)=α(t)/β(t)=φ(r_t) 全轴 bounded，因为 Γ ratio O((1+|t|)^−1/2)
与 Euler critical bound相消。||U_Y(t)||≤C Y^(1/4)，所以 Cc∞ 源直接 Bochner 合法。
若只看到(5)就宣布整个 β 补偿不合法，会漏掉这个实际逃逸。

## 4. Direct 的全 L² 范数及不同组织的 incomplete-Eisenstein 核验

这里先支付比 fixed-L 粗 overlap 更强的全轴费用。令 M=sup|R(t)|<∞，a_Y=logY/2。
原完成四项除 β(t)barβ(r)，给 direct Gram

    J_Y(t,r)=[R(t)barR(r)Y^(−1/2)e^(ia_Y(t−r))−√Y e^(−ia_Y(t−r))]
                    /[−1/2+i(t−r)/2]
       +[R(t)e^(ia_Y(t+r))−barR(r)e^(−ia_Y(t+r))]/[i(t+r)/2]。

首项是 bounded phase/R 夹心的 Cauchy convolution。
1/(−1/2+ix/2)=−2∫_0^∞e^(−u)e^(ixu)du 的 Fourier multiplier
为 −4πe^(−ξ)1_(ξ>0)，operator norm4π。mixed 的每项为 reflection 后的
PV Hilbert transform，norm2πM；PV1/x 的 multiplier −iπsgnξ 可由 Abel arctan 积分自含证明。
R(−t)=barR(t)，所以 antidiagonal t+r=0 上 numerator 为0：相同 PV prescription
合起来正是原 removable kernel，任何同一 boundary-value 的 δ 项也相消。
不能各选不同 prescription 造额外符号。

对 compact-frequency coefficient 用真实 Gram，再以有界性取频率 cutoff 的 Hilbert 强极限。
原 packet factor(2π)^−2 和 Plancherel factor2π 给

    ||T_Y f||²≤B_Y²||f||²，
    B_Y²=2[√Y+Y^(−1/2)M²+M]，全部 complex f∈L²(R)。           (6a)

fixed Y 时该费独立于 L；因此 base2 运输的 source uppernorm 已对成长 L 支付。
一般 L² 的定义是强延拓，Cc∞ 上与直接 Bochner相同。
逐源 cutoff 误差 ≤B_Y[(2π)^−1∫_(|t|>T)|hat f|²]^(1/2)，
Dlog 还可用 logweight 总能量除以 √log(2+T) 控制；这不是 L² unitball 上的 operatornorm 尾界。

对 Cc∞ 原源定义

    g_f(y)=y^(3/4)f(−(log y)/2)，
    Θg_f(z)=Σ_(Γ∞\Γ)g_f(Imγz)，
    k(f)=(6/π)∫_(−L)^L f(u)e^(u/2)du。

g 支持 [a,b]=[e^(−2L),e^(2L)]，Mellin transform
m_f(r)=2∫f(u)e^(2(r−3/4)u)du，m_f(r_t)=2hat f(t)。
从 Re r=2 移到 3/4 的 Mellin contour 仅跨 E 的 r=1 pole，res E=3/π，故

    T_Y f:=(2π)^−1∫ hat f(t)U_Y(t)dt=P_Y[Θg_f−k(f)·1]。     (7)

P_Y 是在 y>Y 删除 x-average 的 L² 正交投影。constant residue 因子6/π和源系数均保留。
contour vertical superpolynomial decay来自 compact smooth 源，
水平边 Hilbert norm 由 MS 与 3/4≤Re r≤2 上 bounded φ 支付，详见独立原证。
不对未截断单个 E 假定 L²。

令 y_min=√3/2，C_L=ceil(e^L/√y_min)，D_L=ceil(e^(2L)+C_L/2)，
N_L=1+C_L(2D_L+1)。这是 coset overlap 上界，不是 actual Weil degree D_L(u)。
标准 fundamental domain 上非identity项 Imγz=y/|cz+d|²≥a 迫 c≤C_L、y≤b、|d|≤D_L。
Θg 的每点最多 N_L 项，并支持 y≤b；Cauchy–Schwarz及 nonnegative unfolding 给

    ||Θg_f||²≤2N_L∫e^(−u)|f(u)|²du≤2N_L e^L||f||²，
    ||T_Y f||≤K_L||f||，K_L=√(2N_L e^L)+√((24/π)sinh L)。    (8)

(8)是另一种组织的、对全部 Y≥2 统一的 fixed-L bound，以 density 延拓所有原 complex L²(I_L)/Dlog。
一般 L² 的 packet 以该 extension 定义，不额外声称 hat f∈L¹ 或 absolute Bochner。
K_L=O(e^(2L)) 只是此 overlap 证明的非最优 upper，不是必要费用；
fixed Y 更强的(6a)已经 uniform L。不能用粗界恢复一个不存在的 source norm 成长瓶颈。
direct source 的原范数接口已付，不能继续记作 unknown 或 compact smoothing。

## 5. Direct source 非紧，但完整扣费后有真实无穷维盲带

记 u₀=log2/2。若 f 的支持在 u<0，g_f 支持 y>1。
在 reduced fundamental domain 中非identity γ 满足 Imγz≤y；
当 y>1 时又有 Imγz≤1/y<1。因此 g>1 时 Θg=g(y) 只在 rectangle cusp。

第一族：f∈Cc∞((−min(L,u₀),0))、k(f)=0。
则 g 支持 1<y<2，T₂f=Θg，且

    ||T₂f||²=2∫e^(−u)|f(u)|²du。                            (9)

这给无限维子空间的下底，T₂对每 L>0 都**非紧**，不能沿用 A₂ 的 compact 标签。

第二族：对每 L>u₀，取 f∈Cc∞((−L,−u₀))、k(f)=0。
则 g 支持 y>2，Θg 为该 cusp 的 constant mode，P₂ 整体删除它。因此

    T₂f=0。                                                 (10)

在上述开区间上增加任意有限个 L²-continuous 线性条件，交空间仍有无限维合法 smooth 源。
完整 band 正交性对 direct source 也给

    ||T_Yf||²−∫_2^Y |y^(3/4)f(−log y/2)
                 +y^(1/4)(R(D)f)(log y/2)|²dy/y²
        =||T₂f||²。                                         (11)

所以所有 finite Y(L)≥2、乃至单源 finite Y(f)，完整扣费后仍有同一盲带(10)。
选其中 L² orthonormal smooth 列 f_j，f_j⇀0；任意 fixed-L L²-compact 自伴修复 K_L 有
<K_Lf_j,f_j>→0。故净 Gram 加这种修复也不能满足任何 ε_L>0 的 whole-source frame 底。
允许 compact norm/rank 随 L 增长不救每个 fixed L>u₀ 的失败。
这不是 Q 负源，也不是 ζ 零点位置的反例；它排的是指定完整 cusp 扣费供应器的原范数稳定性。

未排：保留并支付 cusp 账本、改变 base Y₀(L)/seed 或 source 域、非紧新修复、
真正 signed/full Γ/prime/pole 联合 core 比较。尤其不能从(10)断言所有 modular 几何失效。

## 6. 实际 Weil 对象、两套 pole 与宏观净值

actual Q 始终保 Γ(t)=Reψ(1/4+it/2)−logπ=2θ′、全部 n<e^(2L) 的 strict primepowers，
以及 2|∫f cosh(u/2)|²−2|∫f sinh(u/2)|²。其 Γ 能量在合法 carrier e^(iωu)h 上为
logω+O_(L,h)(1)，fixed-L prime 项 bounded，pole 趋0。
A₂ Gram趋0，T₂ Gram由(8)有界。因此任一 Gram 都不能以 bounded L² 残差等同 Q。
方向性的 signed 比较或保留 Γ 的分解不被此检验排除，必须独立证明。

F 的清极点因子 s(s−1) 对 w=2s 是 w(w−2)/4；actual ξ 是 w(w−1)Λ(w)/2。
两者在 physical line 的 ratio bounded 且 bounded inverse，但参数 poles/jets 不同；
几何 s=0,1 的 residue 不能自动付款 actual w=0,1 的 dual-pole 型。
最高 φφ polar Cauchy Gram 在 Re s<1/2 本来正，兼容全部 ρ/2；RH 是 quarter-line，
ordinary unitary half-line不提供新零点排除。

Zagier另有 actual variable w 的 diagonal Rankin trace divisibility，可保全部 ζ multiplicity，
但 positive h只给Σh(r_j)|f_j|²，原 theorem不控制 j≠k 的完整 complex packet。
其 common ζ factor 是原定理，未给 independent signed cofactor/core 输入；不自动成为下一数学轮。

本轮没有超旧016/028或543的 whole负惯性后果，没有成长 PSD、Ξ识别或 RH。
新交付是(2)–(11)同一 source 的完整准入，特别是 direct实际逃逸与扣费盲带。
它完成一次失败准入；classical恢复、三个代理、来源附件和补审不另计轮。

## 7. 六项结算与止损

问题：modular正Gram能否独立承担实际成长Weil source范数及signed运输？
新增：指定packet全频费用、direct全L²/成长L统一原norm运输及完整cusp扣费的无限维核/compact修复范围。
未付：actual Γ/全部pp/dual-pole同源joint bridge、危险core、成长净值与Ξ。
瓶颈：fixedY source uppernorm对全部成长L由unknown改paid；净供应器frame失败明确，宏观signed瓶颈未缩小。
停止：C016一轮止损，不优化Y/频窗，不从inverse-domain扩大方法类，Goal仍active/open。
重准入：新actual joint定理或paid cusp/变base/seed带来可核core信息，且超最强旧后果。
唯一下一动作从 STATE 恢复；先保真实prime graph与Γ跳核的联合费用，不再恢复正Gram或ζ公因子。
