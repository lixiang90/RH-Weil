# C015：最强旧资产扣除与不同几何来源的入口范围

2026-10-14；独立代理 `/root/c015_macro_source_next`。
本稿只供 root 准入决策：旧资产恢复、外部原件定位、来源选择均为零数学轮。
不修改 STATE、cadence、runtime Goal 或 Git，不提交一个新的编号定理。

## 1. 恢复与本版宏观责任

已经依次读 AGENTS、README、STATE，运行 `research_state.py check` 和 `show`，
再读 Goal、MACRO_FRONTIER、C015 与 D20261014P。
结构 check 通过，不能用它认证数学。初始实际 HEAD 是
`8cba2c811ca301a17816a8330b40a2a1ef87c5d3`，当时 working tree clean。
代理自身 `get_goal` 返回 null；这不是 root Goal 的终态证据。
root 仍须以自身现场工具核 G20261014。此代理无 producer 或待续 exec session。

冻结成果基线 `0c4f3a3eb609bb1d9564138fa4a35701f05605f2`，全部 ≤538 为输入。
539–543 的新增范围以各原件为准；543 已给 cofinal 全复源 `1+C exp(S_L)`
惯性上预算，但并未消除危险 core 的指数规模、全域正性或 Ξ 识别责任。
本次工作不能把一项已知 local identity 恢复成新 independent forcing。

## 2. C015 与最强旧资产的对应

独立读取 017、510、531、532、533、534、535 的指定相关段，得到：

| 本次拟恢复的接口 | 冻结资产已支付的实质 | 尚未支付 |
|---|---|---|
| 每 prime 的 Fourier/Poisson 平方 | 017§§1–2 已给同一零延拓 complex f 的酉 Euler 平方，全部实际 pp 与原 L² | 全球 domination，不由 local 平方推出 |
| 原实位相位/Γ 来源 | 510§§2–6 已从真实 Fourier–反演及合法普通相对迹给 actual Γ，含 identity 常数 | 提升到新的共同算术表示并支付 positive comparison |
| 独立正 trace 的实际 source norm | 531 支付正交 Gram 逆、真实正迹和完整 source cross 接口 | 不同 prime 同时消费及统一成长费用 |
| 真实首 prime 主项运输 | 532 支付 fixed p、fixed source-domain 的全部 pp 及 source compact 余项 | compact 余项的所需符号及成长 joint budget |
| 晚 prime 返回 | 533–534 有 fixed smooth-source 及部分 whole-source 子项 | 完整 signed trace 分离、统一求和与成长 S/U |
| 无费 ordinary 正迹比较 | 535 已严格排 fixed single-prime canonical Sonin 的无费桥及有限条件/秩修复 | 无限秩费用或真正不同 multi-prime/source 几何 |

017 的旧 half-Γ 历史规范必须用其现有纠正和 510 的 actual `2θ′` 消费；
不能凭旧 half scalar 数字推出新结论。这里用的是其不受该纠正影响的原 Euler 平方。

[Burnol 原件](https://arxiv.org/html/math/9901051)现场为 math/9901051v2；
其 local conductor、非负 time-delay 和有分次 trace 被清楚分开。
在 ζ 的 trivial/unramified δ=0 分量，正 time-delay 的 Poisson 符号
是 `log(p) P_(p^-1/2)`，而 conductor 是 `log(p) I − T_p`。
原对象是单一 non-archimedean field，不包含跨 prime 的新共同源估计。
因此外部原声明不是一个已支付的数域极化输入。

## 3. 共同 norm 与单位项相消也只是已知恒等式

以下是对旧 017 同对象恒等式的另一种组织，不登记为新研究结果。
置 `a=log p`、`r=p^-1/2`，对 `f∈L²(R)` 定义

    Z_p f(v,θ)=Σ_(k∈Z) f(v+ka) exp(ikθ),   0≤v<a.

它按 fiber 的 Fourier-series Plancherel 定义为 L² 元素；无需先要求点态收敛。
于是

    ∫_0^a∫_circle |Z_p f|² dθ/(2π) dv = ||f||².

Poisson 符号 `P_r(θ)=1+Σ_(m≥1)r^m(exp(imθ)+exp(-imθ))`
的绝对系数和有限。可先有限展开、再用 L² 收敛及有界乘子延拓，得到

    ∫_0^a∫ P_r |Z_p f|²
      = ||f||² + 2Σ_(m≥1) r^m Re R_f(ma),

其中 `R_f(t)=∫f(u+t)overline(f(u))du`，方向换号不改实部。
所以每个实际 p 的单位项必须先相消：

    logp ||f||² − logp∫∫P_r |Z_p f|²
      = −2Σ_(m≥1)logp p^(-m/2) Re R_f(m logp).

对零延拓 `f∈L²((-L,L))`，`R_f(t)=0` 对 `|t|≥2L` 成立；
故精确还原所有 strict `p^m<exp(2L)`，包括等号处的零项。
这也保留原 Dlog 域：prime 型 fixed L 上有界，Γ 域没有被 Zak 变换替换。
full Q 仍须另保 actual Γ 与 `2|C(f)|²−2|S_pole(f)|²`。

`p≥exp(2L)` 时 conductor 在此共同源上的贡献为零，
但未相消的正块 `T_p` 仍等于 `logp ||f||²`。
因此不能把所有正 `T_p` 的 direct sum 当可求和的数域正性；
单位项分开求和先发散，而逐 p 相消后得到的仅是原 prime 型。
这不是证明所有 graded/multi-prime 方法失败，只是说明当前恢复没有新增 joint 输入。

**准入建议：**若另外两项原件/domain 审查没有找到独立的新 coupling、
common-source 费用或 dangerous-core 后果，C015 在入口即停止，settled 数学轮保持空。
不因恢复三份原件、写出 Zak 证明或外部 old theorem 通过而制造 544。
主合同预算是上限，不是必须填满的轮数。实际宏观瓶颈没有改变。

## 4. 不同来源：modular Eisenstein 的真实几何正 Gram

定向全仓检索 `Maass/Maaß/Zagier/Iwaniec/Eisenstein series/truncated Eisenstein`
未发现 ≤538 对这一个 PSL₂(Z) truncated-Eisenstein 对象的同源消费。
其他 Eisenstein 命中为 Q(√−3) 等先前算术域，不是这里的 modular series。
“检索未命中”只支持新来源候选的选择，不认证世界新颖性或必有净结果。

两份作者一级来源已现场打开并读指定证明：

1. [Zagier, *Eisenstein Series and the Selberg Trace Formula I*](https://people.mpim-bonn.mpg.de/zagier/files/scanned/EisensteinSelberg/eisenstein-selberg-I-978-3-662-00734-1_11.pdf)，
   §2，(2.1)–(2.8)、Proposition 1；PDF pp.10–12。
   原 primitive-pair Fourier 展开给真正的 ζ coefficient 及 completed functional equation。
2. [Garrett, *Truncation and Maaß-Selberg Relations*](https://www-users.cse.umn.edu/~garrett/m/v/maass_selberg.pdf)，
   dated February 19, 2005；PDF pp.4–7。
   原 self-associate 四项 inner-product、unfolding 证明和 pole corollary；
   其 general GL(n) Haar normalization 到这里的 hyperbolic norm仍须单独核。

这里用 `Λζ(w)=π^(-w/2)Γ(w/2)ζ(w)`，不是 entire ξ 的同名混用。
对 modular group 的 normalized series，原常数项是

    y^s + φ(s)y^(1−s),
    φ(s)=Λζ(2s−1)/Λζ(2s)
        =√π Γ(s−1/2)/Γ(s) · ζ(2s−1)/ζ(2s).

候选独立 positive source 是实际 hyperbolic measure 下的

    G_Y(s,w)=⟨Λ^Y E(·,s), Λ^Y E(·,w)⟩,

`Y>1`，cusp 内减完整 constant term，两实参数一致。
每个 regular 参数的 truncated vector 是 L²，finite complex Gram ≥0。
这不是旧 finite matrix 测试，而是真实几何 Hilbert norm；
它也不是已付的实际 Weil 正型或全源运输。

## 5. 便宜 scope gate：不能从 ordinary pole sign 逼 quarter-line

将原四项 formula 用 classical 参数书写，候选确切式是

    G_Y(s,w)
      = [Y^(s+barw−1) − φ(s)overlineφ(w)Y^(1−s−barw)]/(s+barw−1)
        + [overlineφ(w)Y^(s−barw) − φ(s)Y^(barw−s)]/(s−barw).

共振分母按 removable limits 消费；specialization 的 measure/common factor
仍待 root 独立核，不能从 general Garrett formula 偷取 norm 常数。
下面的符号结论只依赖该因子为正，不受这一 normalization 未知影响。

若 `ρ` 是 actual nontrivial ζ zero，`0<Reρ<1`，则 `sρ=ρ/2` 在 `Re s<1/2`。
numerator `Λζ(ρ−1)=Λζ(2−ρ)` 在 `Re(2−ρ)>1` 非零，
因此这是 φ 的真实 pole，order 保持；不假设 RH、不改变零点。
几何 unitary line `Re s=1/2` 对应 ζ arguments 的 Re 0/1；
实际 RH 在此 response 的目标却是 `Re s=1/4`。
这两个 line 的区别是 exact variable mapping，不是数值精度问题。

在任意 lower-half 参数 `Re s,Re w<1/2`，φ-φ 项的 kernel 为

    K_Y(s,w)=Y^(1−s−barw)/(1−s−barw)
            =∫_0^Y y^(−s) overline(y^(−w))dy.

因此它本身是严格正 Gram：任意有限个 distinct 下半平面参数和复系数，
积分等于一个平方；指数函数的线性独立还给非零系数时严格正。
任意 finite pole family 的最高 Laurent 双极点系数正好是此 kernel
以真实 residues/coefficient 夹心，兼容所有这些 `sρ` 的位置和 multiplicity。
单 pole `s₀=σ₀+it₀`、order m、leading coefficient a 的最高对角量为

    |a|² |s−s₀|^(−2m) Y^(1−2σ₀)/(1−2σ₀) > 0

对 `σ₀<1/2`；其他 terms 在 fixed `t₀≠0` 时至多单极点级。
`σ₀>1/2` 此 double-pole coefficient 才负，给原右半平面排 pole 机制。
这是原 Maass–Selberg corollary 的 scope 复核，不作为新方法类定理或额外数学轮。
不构造 actual 离线 ζ 零点，只说明所有未知 critical-strip resonances
都落在 direct Gram pole-sign 已允许的范围。

还不能把 `E(·,sρ)` 当 self-adjoint Laplacian 的 L² eigenvector：
左侧 resonant state 在未截断 cusp 中增长，truncation 有 boundary subtraction。
例如 actual critical ζ 参数 `w=1/2+it` 对应
`s=w/2=1/4+it/2`，`s(1−s)=3/16+t²/4+it/4` 为非实，
无矛盾地说明这是 resonance parameter，不是一个实谱特征值。

## 6. C016 更具体的共同来源：完整 cusp Gram 精确扣除

root 后续明确指定这一个 source gate。对 `1<Y₀<Y`，
令 `c_s(y)=y^s+φ(s)y^(1−s)`。在 fundamental domain 的 rectangular cusp
`−1/2≤x≤1/2, y>1` 内，`Λ^Y E−Λ^Y₀ E`
恰为 band `Y₀<y≤Y` 上的 constant Fourier mode `c_s(y)`。
该 band 上 `Λ^Y₀ E` 仅有 nonzero Fourier modes。
按 x 积分的正交性因此给**所有 complex regular s,w** 的精确恒等式

    G_Y(s,w) − B_(Y₀,Y)(s,w) = G_Y₀(s,w),
    B_(Y₀,Y)(s,w)=∫_(Y₀)^Y c_s(y)overline(c_w(y)) dy/y².

任意 finite coefficient packet 同样成立，并且 `G_Y₀` 是正 Gram。
这里扣除完整四项 cusp constant-mode Gram；不是只减对角 `2logY`，
也没有忽略 φ 的 mixed source terms。无需 Y→∞ 或未知 zero 位置。
这个输入是现实独立几何 norm，但扣除恒等式本身是 Fourier orthogonality，
目前只作来源准备，不单独结算数学轮。

为保全 actual resonances，source不能未经检查固定成有 poles 的 E。
依 Zagier completed series，先取

    F(z,s)=s(s−1) E*(z,s),
    E*(z,s)=Λζ(2s) E(z,s),
    c*_s(y)=s(s−1)[Λζ(2s)y^s+Λζ(2s−1)y^(1−s)].

原 completed poles 在 0/1，而 1/2 的常数项 poles互相相消；
`F` 的 entire source/domain结论须按原 Bessel series和uniform compact bounds核。
截断 `F_Y=F−1_(y>Y)c*_s` 后，定义全 complex completed Gram

    H_Y(s,w)=⟨F_Y(·,s),F_Y(·,w)⟩.

相同 band orthogonality应给

    H_Y(s,w) − ∫_(Y₀)^Y c*_s(y)overline(c*_w(y))dy/y² = H_Y₀(s,w) ≥ 0.

最后的 ≥0 是 finite全complex Gram的意思，不是每个 off-diagonal scalar都非负。
这一 pole-clearing 用整个已给原 source，不假设 ζ zero-free 或删掉其 zeros。
还须明确原 E* 与 entire ξ 的常数、0/1 multiplicity、
所有 parameter-dependent source norm费用，不能只凭“completed”命名消费。

具体 actual variable freeze可取 `s_t=1/4+it/2`，使 `2s_t=1/2+it`，
原 Γ 因子的位置与实际 Weil规范相同。
对原 physical `f∈Cc∞((-L,L))`，候选 packet是

    A_(Y,f)=∫_R hat f(t) F_Y(·,s_t)dt,

Fourier convention须由 root 固定，并先证明此 Bochner integral 与其 polarization合法。
它的双频 positive energy由 H_Y 给，完整 cusp费用由 c*_s 同一 packet给；
这只是一个明确、无未知zero拟合的共同source提案。
尚未证明它等于完整 actual Q，也没有支付原 L²/Dlog normtransport或finite-rank费用。
原Q的 Γ 单频、全部strict pp、dual pole与此双频 geometry之间必须给真实桥。

## 7. 真正下一动作与停止/重准入条件

因此只对“ordinary Gram positivity 排 pole”有肯定 scope 检验，尚没有新 signed/core bridge。
不同来源仍比 C015 更有同对象信息：φ 精确包含 actual ζ，
几何 norm/cusp 消减是独立可审来源；不需要 Selberg log(ab) → 反射的未知运输。
但新 joint forcing 目前是 unknown，不能把它换成一个假设当输入。

建议 root 如要继续这个来源，唯一首动作应是：独立重建 §6 的全 complex
Maass–Selberg与完整 cusp Gram扣除、completed 0/1 pole-clearing和 exact hyperbolic norm；
再消费上述 same physical f packet，审原 Dlog unit ball、随 L/Y joint 的
真实 signed/core response及 actualQ桥，先查最便宜 whole-source费用/净值失败条件。
不得单靠 Pick/inner upper-half contractivity、unitarity 或去 residual pole 就登记 forcing。

若首个实际 source packet 没有可核 norm/complete-variable bridge，
或只得到普通 upper-half pole exclusion，入口止损并保存缺失桥，仍零新数学轮。
只有新增 actual common-source inequality/explicit core effect，
且扣除 016/017/028/531–535/543 强后果后，才开始 1–2完整轮新合同。
这里不预先承诺“Maass–Selberg 一轮必须失败”，保留 full subleading/source-adaptive
与全 complex joint kernel 的逃逸；§5只审 direct highest-polar-sign门。

两份作者原 PDF已冻结至本目录 [sources](sources/macro-primary-source-receipt.json)，
并以 PyMuPDF保存对应全文 text。原 PDF SHA256：

- Zagier：`a7ad2a85f9a90de14ac0b4affd723393b7ab61e16dd749dd6c4c0db881767b94`，3010889 bytes，53 pages。
- Garrett：`b68fa97bb201ef2355884ba79c1dcb5dc14916dede42d4ddaccdd0d3731933f7`，120122 bytes，7 pages。

未关闭 TLS验证；Python对 Garrett 的 issuer-chain失败后用 Windows trust读取。
本地原件可复查，不把下载成功或 text提取当数学认证。

另一个真正 number-field 几何来源已经定位：
[Yuan–Zhang, arithmetic Hodge index I](https://web.math.princeton.edu/~shouwu/publications/hodge-I-version2.pdf)，
Theorem 1.3（PDF p.4）及其 proof §2：normal/projective/geometrically connected X、
integrable adelic M、nef/big L_i、generic-degree orthogonality给负交叉自交。
curve case 的独立前件是 degree-zero integrable M，不依赖 RH。
但原 source f 到实际 adelic M_f、local pp 和 Γ 配对均无已定位构造，
比 modular exact ζ response更远；所以不另开第二合同，不并行漫游。
将来准入这条几何来源的首动作必须先给 canonical M_f/local pairing 原构造，
不能仅把未知 Q 正性写成“存在满足 Hodge 的 M_f”。

本稿准确净状态：C015 旧资产扣除支持入口停止；modular/Yuan–Zhang 为 cited来源与
cheap scope gate 准备，未支付新的 complete Weil domination、growth PSD、Ξ 识别。
actual bottleneck 未改变；本稿与所有来源读取不消费原 cadence。
