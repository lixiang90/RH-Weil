# Cofinal principal-quotient readout：独立反向审查

2026-10-14；`/root/principal_final_reverse`。本稿仅核已存在的来源门原稿，
不新建合同、不改 STATE/Goal/cadence/Git，也不重新派发已缺失的旧代理。

恢复顺序已执行：AGENTS、README、STATE、`research_state.py check` 后 `show`、
G20261014 原文、MACRO_FRONTIER、C021 stopped、D20261014AA、最新战略及唯一
next-principal-quotient-norm gate。结构 check 通过，不认证数学。
现场 HEAD 为 `1d48bd538cd176091dbec90eeca46253a1473d70`；工作树已有 root 的
`.gitattributes`、STATE 与本来源目录改动。实际代理 inventory 中没有旧 c017 handles，
故不据 STATE 的旧 running 字段重启它们。root 的 Goal 现场观察另付，子审不代它。

被核原稿为 `cofinal-fees-and-repaired-readout-audit.md`，全文已读；入口 raw SHA256：
`988d93e02d8dc8bb9877abddb1cd00c40312351c68810742360f1b4d70238204`。
本稿未静默改动该原稿。并核读原 405 的实际 Mellin/配对正规化、519、520、523、526，
543 的 actual Γ 图范数及本门 `cyclic-density-and-bounded-readout.md`。

## 1. 结论与消费边界

原稿中本次重点要求的五项计算通过：紧支窗原 L² 上完整 ζ-jets 的精确范数；
critical Hlog 的所有 γ/成长 L 估计；同时消去双 pole 的合法 probes；
固定 offcritical ρ 的必要/充分指数费用；完整 signed pole 的两条特征值。
未发现需要改正原公式的数学错误。

必须随原证明一起消费的限定如下：

- critical 常数依赖先固定的 jet 阶数 j；不提供对全部重数阶数统一的常数。
- full-source critical 界对所有 L≥1；指定 pole-free probe 的一致下界只在 L≥L_j。
- offcritical 比较先固定 ρ、j；常数可依赖 ρ，不能用于 α(L)→0 的一致结论。
  它不假定实际存在 offcritical 零点。
- 单坐标全高度估计不代 joint bound。原稿对人为选取的小正权另给了真正 full-height
  sufficient fee，但该权与完整 Weil 的实际 signed 系数无同对象识别。
- compact principal intersection 为零的证明必须保全部必要 jets，以重数计 ζ 零点；
  不能仅以所有 distinct values 消失和含重数零点计数作该推理。
- complex 源上的零读出需 complex-linear 并消去完整 complex principal，或 real-linear
  并消去完整 realification；只消去 real principal 不排 imaginary 部分。

这些是旧资产的显式费用与范围恢复，研究轮分类为 **0**。未支付独立算术符号、
实际 full Q 比较或成长 core；不升级为 Goal 第 2/3 项的完成。

## 2. 对象、坐标、原 norm 与精确 L² 费用

保持 F=S_exp,C、I=完整必要 ζ-jets 关系理想，
P_an=I∩ker M(0)∩ker M(1)。physical coordinate 是 r(u)=e^(u/2)f(u)，
故对 κ=ρ−1/2：

    ell_(ρ,j)(r)=∫ u^j exp(κu) r(u) du。

在 I_L=(-L,L) 的原 L²(du) 上，内积第一变量线性，Riesz 核为
u^j exp(barκu)1_(I_L)。由 Cauchy–Schwarz 及该核的 smooth compact L² 逼近，
同一 supremum 在原 Cc∞ 测试源上取得极限：

    ||ell_(ρ,j)||² = ∫_(−L)^L u^(2j) exp(2αu) du，α=Reρ−1/2。

因此 j=0 精确为 2L（α=0）或 sinh(2|α|L)/|α|（α≠0）；critical 任意固定 j
精确为 2L^(2j+1)/(2j+1)。固定 α≠0 时，端点 Laplace 积分给
L^(2j)exp(2|α|L)/(2|α|)。两端都保留，未把固定 α 的渐近式套给 α→0。

physical graph norm 固定为

    ||r||²_Hlog=(2π)^−1∫[1+log(2+|t|)]|hat r(t)|²dt。

543 原 actual Γ=Reψ(1/4+it/2)−logπ=2θ′，Φ=Γ−Γ(0)，给
1+Φ 与上述 spectral weight 的绝对等价；域仍是 full-line zeroextension Dlog。
这种等价只运费用阶，不把某精确数值常数或 Riesz 核自动运到实际 Γ 内积。

## 3. Critical Hlog：对所有 γ/L 的反算

令 W(t)=1+log(2+|t|)、K_j(s)=∫_(−L)^L u^j exp(−isu)du。
一次分部积分显式保两个端点，给 |K_j(s)|≤4L^j/|s|；
Plancherel 给 (2π)^−1∫|K_j|²=2L^(2j+1)/(2j+1)。
这不要求 hard cutoff 的导数是 L²。

weighted Fourier Cauchy–Schwarz 的 upper certificate 是

    |ell_(1/2+iγ,j)(r)|²
      ≤||r||²_Hlog (2π)^−1∫ |K_j(t+γ)|²/W(t) dt。

它是全线 dual extension 的 upper，非 restricted-domain exact dual norm。
|γ|≤4 时用 W≥1；|γ|>4 时分 |t+γ|≤|γ|/2 与其补集。
前者 W(t)≥cW(γ)，后者 sinc tail 积分≤C_jL^(2j)/|γ|。
因 L≥1、W(γ)/|γ| 在 |γ|>4 有界，二者都被
C_jL^(2j+1)/W(γ) 支配。没有遗漏 γ≫L、γ≪L 或 γ 随 L 变的区域。

下界取固定非负非零偶 χ∈Cc∞(−1,1)，
g=exp(−iγu)(u/L)^jχ(u/L)，a_j=∫v^(2j)χ(v)dv>0。
则 ell_j(g)=L^(j+1)a_j，且 Fourier 缩放准确给

    ||g||²_Hlog = L/(2π)∫W(s/L−γ)|hat(v^jχ)(s)|²ds
                 ≤C_j L W(γ)。

最后一步是 W(s/L−γ)≤W(γ)+log(1+|s|) 与固定 smooth bump 的 rapid decay。
相除即得原稿 (8) 的两侧同阶界，常数只依赖 j 与所选固定 χ，ALL γ、L≥1。

## 4. 双 pole 零 probe 与固定 offcritical ρ

对 r=(D²−1/4)g，所有边界项确实为零，A_±(r)=0。
直接把二阶导数移到 u^j exp(κu) 上，得到

    ell_j(r)=(κ²−1/4)ell_j(g)+2jκell_(j−1)(g)
             +j(j−1)ell_(j−2)(g)。

critical κ=iγ、上述 g 的 j−1 项因 χ 偶准确为零；主项绝对值
(γ²+1/4)L^(j+1)a_j，而剩余项是 j(j−1)L^(j−1)b_j，
b_j=∫v^(2j−2)χ(v)dv（j<2 时为零）。例如选 L_j²≥8j(j−1)b_j/a_j
便保主项至少一半，统一于所有 γ。

将 r 展开为 exp(−iγu) 乘以下三项：

    −(γ²+1/4)ψ_j(u/L)，−2iγ L^−1ψ'_j(u/L)，L^−2ψ''_j(u/L)。

每项按上一节付同一个调制图范数，故
||r||²_Hlog≤C_j(1+γ²)² L W(γ)。
(γ²+1/4)/(1+γ²)≥1/4，使 pole-free 比值仍有
c_j L^(2j+1)/W(γ) 下界。这不依赖 pole 方向，也不声称小 L 的固定 probe 无抵消。

对先固定 actual ρ，α≠0，取 χ=exp(−iγu)χ₀、χ₀ 非负非零 compact；
其 ell_(ρ,0)(χ)=∫exp(αu)χ₀du 非零。令 ψ=(D²−1/4)χ，则

    A_±(ψ)=0，ell_(ρ,0)(ψ)=ρ(ρ−1)ell_(ρ,0)(χ)≠0。

对 τ_aψ（a=signα(L−A−1)），原 Hlog 平移等距、支撑在 I_L、双 moments 仍零。
ell_(ρ,j)(τ_aψ)=exp(κa)Σ_(k≤j)binom(j,k)a^(j−k)ell_(ρ,k)(ψ)，
polynomial 的 leading coefficient 非零。因此必要费为
c_(ρ,j)L^(2j)exp(2|α|L)，上界由 exact L² fee 与 Hlog≥L² 付清。
这只在固定 ρ、j 的 cofinal 窗成立。s=0/1 的 pole norm 同阶 exp L，
但不能使用上述 multiplier，因为 s(s−1)=0；在 pole-free 域其读出本来为零。

## 5. 完整 signed pole、joint norm 与最强旧逃逸

原 pole form 为 2Re(A_+bar A_−)，核 h_±=exp(±u/2)1_(I_L)。
||h_±||²=a=2sinh L，〈h_+,h_−〉=b=2L。
其 rank-two selfadjoint operator 将 h_++h_− 乘 a+b，将 h_+−h_− 乘 b−a。
所以两个 nonzero eigenvalues 恰为

    2L+2sinh L，2L−2sinh L。

后者对全部 L>0 严格负，operatornorm 是前者；原稿没有把 signed rank-two 项当 PSD。
A_+=A_−=0 时该 form 恰为零。两 raw coordinates 不杀 I，但杀 P_an，
所以含双次数的忠实目标是 F/P_an；只有 ζ-jets 的目标是 F/I。

finite weighted coordinate map 的 squared norm 是原稿 (17) Gram 的最大特征值。
若按 first-linear 约定把矩阵写为 TT*，其 entries 是展示 Gram 的转置/共轭，
但 Hermitian positive spectrum 相同；该约定不改变 claimed exact norm。
无限坐标有界必须对全部有限子集有统一 eigenvalue 上界。每个对角有限不足。

原稿指定 ω_a=2^−a/(1+b_a²)、b_a=2^(j_a+2)j_a!（枚举 a≥1），确能对全部实际
heights 与必要 multiplicity jets 付 F 上连续性及 compact-window fee：
||ell_a||²≤2L^(2j_a+1)exp L，除 b_a² 后求和得到
L exp L/8·sup_j[(L/2)^(2j)/(j!)²]≤L exp(2L)/8。
这是有效的 full-height sufficient certificate，不只是 diagonal 口号；
但任意枚举/人为权不提供实际 full Weil 的自然系数或独立算术输入。

最强旧 526 更早给 δ=1/2 的忠实全 jets 商，其 compact source upper 是
q²≤∫2cosh u|r|²≤2cosh L||r||²。加双次数坐标后，
同一个全源 map 的 kernel 恰为 P_an，squared source fee≤2cosh L+4sinh L=O(exp L)。
故原稿的人为 coordinate sum 没有比最强旧 whole quotient 费用更强的净后果。
原 source upper 的等号不能传给 quotient norm；526 的非酉/非等价酉化缺陷仍保留。

## 6. Closure、完整 ζ 对象和净后果

523 已给 I 的 single-line L²/固定阶 Sobolev 密度；405 的 p∈P_an 非零，
其 entire Mellin 在任何 fixed vertical line 非零 a.e.，将 p 代入相同 weighted cyclic
证明即给 principal physical L²/Hlog 密度。此更具体 relation 版本为旧直接后果。
bounded principal-compatible Hilbert/mod-base map 的零性不排 F-continuous、
cofinal 非uniform、变 domain/target/place 或非全局连续的 nonlinear 修复。
PSD quadratic energy 的零性另需真 PSD、全部源 global bound 与 principal radical 条件。

I∩Cc∞={0} 的 Jensen 推理也通过：compact Mellin 为 finite exponential type，
含重数零点计数 O_f,L(R)；I 的 full necessary jets 要它包含全部实际 ζ 零点及真实重数，
与无条件 Riemann–von Mangoldt 计数 ≍RlogR 矛盾。
截断真实 noncompact principal 通常失去 exact ζ-jets；fixed-source tail 上界与平移
p_B(τ_ag)≤exp(B|a|)p_B(g) 相容，不能免费提升为统一 source-adapted closure 费。

在原 405 正规化，real 完整 Q 是 T(f,f)=−2B(f,f)+2d(f)c(f)，
ζ 展开为 Σ_ρm_ρ M_f(ρ)M_f(1−ρ)。complex Hermitian 延拓保留
M_f(ρ)overline(M_g(1−barρ))。原稿的 |ell|² 正 sum 不能替换这一实际 signed pairing；
actual Γ、全部 primepowers、双 pole 和全部 multiplicities 仍须同对象比较。

520/522 已把忠实中心化次指数费与实际零点实部责任联系，523/526 已同时给
physical collapse 和合法忠实非uniform escape。本稿核到的费用不产生独立 RH 输入，
不改善 543 whole count，也不关闭 G2/fulljoint/core/通常 Ξ 识别。

root 可消费本来源门为准确 **旧恢复/来源 0 止损**，保留其明列修复。
未来重新准入须提供不依未知零点位置的真实几何/算术 readout 与全源成长费用，
再核上述单坐标/joint 必要费、全部 jets、actual coefficient direction 和最强旧净值。
这次审查不授权 C022，不重开 C021，不消费 cadence，不完成宏观 Goal。
