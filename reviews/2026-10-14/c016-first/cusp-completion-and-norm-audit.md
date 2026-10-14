# C016：classical cusp、completion 与全源范数独立审查

2026-10-14；独立代理 `/root/c016_cusp_completion`。
本稿只写该审查文件，不修改 STATE、cadence、runtime Goal 或 Git。
原件与 classical 工具恢复是零数学轮；§7 的具体候选全频费用由 root 与其他独立组织复核后决定如何结算。
它不是 actual Weil 正性、RH 或宏观 Goal 完成证据。

## 1. 恢复、原件和对象

已依次读 AGENTS、goals/README、STATE，运行 research_state.py check/show，
再读本版 Goal、MACRO_FRONTIER、C016 与 D20261014Q。
结构检查通过；冻结成果基线仍为 `0c4f3a3eb609bb1d9564138fa4a35701f05605f2`，全部 ≤538 是输入。
现场 HEAD 为 `d924d2cae53c19c3ee99e8a1ace550072c4b4683`，读取时 working tree clean。
本代理 get_goal 为 null，不代替 root 的 G20261014 现场观察；无 producer 或续 exec session。

逐字节核原 PDF SHA256，并查看原页图像以补 text 缺失的共轭、分母和常数：

- [Zagier 原件](../c015-admission/sources/macro-zagier-eisenstein-selberg-I.pdf)，PDF pp.10–12，印刷 pp.312–314，§2 (2.1)–(2.8)：
  `a7ad2a85f9a90de14ac0b4affd723393b7ab61e16dd749dd6c4c0db881767b94`，3010889 bytes。
- [Garrett 原件](../c015-admission/sources/macro-garrett-maass-selberg.pdf)，PDF pp.4–7，2005-02-19：
  `b68fa97bb201ef2355884ba79c1dcb5dc14916dede42d4ddaccdd0d3731933f7`，120122 bytes。

一级在线原件分别是 [Zagier 作者 PDF](https://people.mpim-bonn.mpg.de/zagier/files/scanned/EisensteinSelberg/eisenstein-selberg-I-978-3-662-00734-1_11.pdf)
与 [Garrett 作者 PDF](https://www-users.cse.umn.edu/~garrett/m/v/maass_selberg.pdf)。
竖线 Gamma 估计现场核 [NIST DLMF 5.11.9](https://dlmf.nist.gov/5.11.E9)。
不用 general GL(n) 的未指定 Haar 因子来替代 classical norm。

设 M=PSL2(Z)\H，标准 fundamental domain

    D={|x|≤1/2, |z|≥1},       dμ=dx dy/y²。

Zagier 的原规范为 E(z,s)=Σ_(Γ∞\Γ) Im(γz)^s，初始 Re s>1；其 primitive-pair 表达带 1/2。
记 Λ(w)=π^(−w/2)Γ(w/2)ζ(w)，这里 Λ 不是 entire ξ。
常数 Fourier mode 与原散射比为

    c_s(y)=y^s+φ(s)y^(1−s),       φ(s)=Λ(2s−1)/Λ(2s)。

φ(1−s)φ(s)=1 和 φ(bar s)=overline(φ(s)) 按 meromorphic 恒等式消费。
对 Y>1，D 的 cusp 是宽度正好 1 的 rectangle。
在该 cusp 减 c_s，得 E_Y=E−1_(y>Y)c_s；这是 quotient 上的截断，不能换成仅限制 y≤Y。
参数 regular 指 E/φ 在该参数可取有限值；下面的 entire completion 则无需删参数。

## 2. 四项 Maaß–Selberg 的 classical 归一化

以下内积对第一变量线性。取初始 Re s>Re w>1。
截断 tail 在 D 上只来自 identity coset（Y>1）；其 Poincaré 表示的 seed 是

    h_s(y)=y^s           (0<y≤Y),
           −φ(s)y^(1−s) (y>Y)。

E_Y 与 w 的 tail 内积为零，因为 y>Y 上 E_Y 的 constant mode 为零。
所以 G_Y(s,w)=<E_Y(s),E_Y(w)>=<E_Y(s),E(w)>，且后一个积分绝对收敛。
按 seed 展开并展开 Γ∞\H，得到

    G_Y(s,w)=∫_0^Y y^s overline(c_w(y)) dy/y²
             −φ(s)∫_Y^∞ y^(1−s) overline(c_w(y)) dy/y²。

初始区域使下端和上端四项全部可积。积分 x∈[−1/2,1/2] 的长度为 1，
因此 dy/y² 前的因子确为 1。直接积分得

    G_Y(s,w)
      =[Y^(s+bar w−1)−φ(s)overline(φ(w))Y^(1−s−bar w)]/(s+bar w−1)
       +[overline(φ(w))Y^(s−bar w)−φ(s)Y^(bar w−s)]/(s−bar w)。       (MS)

初始 seed 的绝对展开可以用 Re s>Re w>1 的同样四个可积幂控制。
原 Bessel 续拓的 compact-uniform L² 界（§5）允许以 s 和 bar w 的 meromorphic continuation
把等式延至全部 regular complex 参数。Garrett p.4 四项及 p.5 unfolding 与此逐项一致，
但 classical common factor 已由 width1/hyperbolic measure 独立固定。

## 3. Coalescence，尤其 s=1/2

不能独立消费一个有零分母的项。令 z=bar w。

- z→s 时第二括号的可去极限为 `2φ(s)log Y−φ'(s)`。
- z→1−s 时第一括号的可去极限为 `2log Y−φ'(s)/φ(s)`。
  此处两个参数须 regular；函数方程先给 numerator 零，再给导数恒等式。
- s=σ+it，σ≠1/2、t≠0 时，对角原 norm 是

    ||E_Y(s)||²
      =[Y^(2σ−1)−|φ(s)|²Y^(1−2σ)]/(2σ−1)
       +[overline(φ(s))Y^(2it)−φ(s)Y^(−2it)]/(2it)。

- σ=1/2、t≠0 时第一项变为 `2log Y−Re(φ'(s)/φ(s))`，第二项仍完整保留。
  散射酉性仅用于这条 line 的 coalescence，不能把 mixed 项删掉。

Λ 在 0 的 residue 为 −1、在 1 的 residue 为 +1，故 φ(1/2)=−1。
Zagier 展开给 E*(z,1/2) finite，而 Λ(2s) 在此有 pole，因此整个 E(z,1/2)=0，
也有 E_Y(1/2)=0。MS 在双 coalescence 的两部分恰相消：
`2log Y+φ'(1/2)` 与 `−2log Y−φ'(1/2)`。
这不意味着 completed F_Y(1/2) 为零，也不意味着参数导数被排除。

## 4. Y0=2 的完整 cusp Gram，所有 complex packet 与 jets

对所有 Y≥2，在 band 2<y≤Y 上

    E_Y(s)=E_2(s)+c_s(y)，

其中 E_2 的 constant Fourier mode 为零，c_s 是 constant mode。
在 x 上的正交性逐对给

    G_Y(s,w)−∫_2^Y c_s(y)overline(c_w(y))dy/y²=G_2(s,w)。          (CUSP)

所以任意 finite regular complex 参数 s_j、复系数 a_j 满足

    Σ_(j,k) a_j overline(a_k)[G_Y(s_j,s_k)−B_(2,Y)(s_j,s_k)]
      =||Σ_j a_j E_2(s_j)||²≥0。

这里只说矩阵/packet 正型；off-diagonal 值不必为非负实数，Gram 也可能有 null directions。
费用 B 是完整 constant-mode Gram，保 y^s/φy^(1−s) 的两 cross terms，不能换成 scalar 2log Y。
对 parameter derivatives，在避开 pole 的 compact 集逐项微分，仍是同一个 Fourier 正交等式。
每个 finite jet order、每个 finite collection 都有效；不声称对所有 jet order 有一个无费常数。

## 5. Zagier completion 的 poles、half 相消与 entire L² family

原 (2.6) 用 ν=s−1/2 写为

    E*(z,s)=Λ(2s)y^s+Λ(2s−1)y^(1−s)
             +2√y Σ_(n≠0) τ_ν(n)K_ν(2π|n|y)e^(2πinx),
    τ_ν(n)=Σ_(ad=|n|, a,d>0)(a/d)^ν。

逐页图像确认 factor2、order s−1/2 以及 residue 的 1/2。
对 ν 的 compact 集 K，τ_ν(n) 被一个固定 polynomial in |n| 控制。
从 K_ν(v)=∫_0^∞ e^(−v cosh r)cosh(νr)dr，v>0，得 K_ν entire in ν，
并由 cosh r≥1+r²/2 得 compact-uniform `|K_ν(v)|≤C_K e^(−v)/√v` 对 v≥1。
这给非零 Fourier sum 在 y≥√3/2 上正常收敛，在 y→∞ 指数衰减；参数 Cauchy estimates 同样适用。
原文的 uniform 描述须按此 compact-uniform 解释，不能当所有无界参数已有统一常数。

E* 只有 s=0,1 的 simple poles，residues 分别 −1/2,+1/2，且独立于 z。
在 s=1/2，两个 constant terms 的 residues 为 +√y/2 和 −√y/2，完全相消。
若 a=(γ−log(4π))/2 是 Λ 在 0/1 的 finite constant，half 的有限 constant mode 是

    c_E*(y,1/2)=√y[log y+γ−log(4π)]。

置

    F(z,s)=s(s−1)E*(z,s),
    d_s(y)=s(s−1)[Λ(2s)y^s+Λ(2s−1)y^(1−s)]。

F 和 d 的括号整体都是 entire（两单项在 half 仍不可独立取值）。
F(z,0)=F(z,1)=1/2；F(z,s)=F(z,1−s)。
`d_(1/2)(y)=−√y[log y+γ−log(4π)]/4`。
截断

    F_Y=F−1_(y>Y)d_s

在 fixed Y>1 上是 entire map C→L²(M,dμ)。证明分两区：D∩{y≤Y} 有有限面积且 y 有正下界，
上述正常收敛与 constant cancellation 给 compact-uniform 有界；y>Y 只余非零 Fourier modes，
由指数衰减给同一个可积 majorant。强连续、局部 L² bounded 及 weak holomorphy（或 Cauchy integral）
因此给 Hilbert-valued holomorphy；所有 finite derivatives ∂_s^m F_Y 都属 L²。

端点的向量与 norm 还可精确核：

    F_Y(0)=F_Y(1)=(1/2)1_(D,y≤Y),
    ||F_Y(0)||²=||F_Y(1)||²=(π/3−1/Y)/4。

因为 area(D)=∫_(−1/2)^(1/2)(1−x²)^(−1/2)dx=π/3，cusp tail area=1/Y。
此 endpoint 值不随 Laurent 约定改变，不能误写成完成消 pole 后删掉 endpoint source。

同一 band orthogonality 给全部 complex s,w（包括0,1,half及原E共振点）

    H_Y(s,w)−∫_2^Y d_s(y)overline(d_w(y))dy/y²=H_2(s,w),
    H_Y(s,w)=<F_Y(s),F_Y(w)>。                                  (CCUSP)

任意 finite complex packet 和任意 finite parameter jets 均给正 Gram H_2。
对 actual ζ zero ρ（multiplicity m），sρ=ρ/2，Λ(2s) 的 zero order m 与 E 的 pole order m 相消；
Λ(ρ−1)=Λ(2−ρ) 在 Re(2−ρ)>1 非零，故完成 family 不需要假定 RH 或先删共振。
恢复原 E 的 Laurent data 要再除以 `q(s)=s(s−1)Λ(2s)`，不由 completion 自动获得原norm有界逆。

## 6. Completed MS 式，避免未知 inverse ζ

置 A(s)=s(s−1)Λ(2s)，B(s)=s(s−1)Λ(2s−1)。
在两者 regular 且原E regular 的区域，乘原 MS 式得到

    H_Y(s,w)
      =[A(s)overline(A(w))Y^(s+bar w−1)−B(s)overline(B(w))Y^(1−s−bar w)]/(s+bar w−1)
       +[A(s)overline(B(w))Y^(s−bar w)−B(s)overline(A(w))Y^(bar w−s)]/(s−bar w)。   (CMS)

再以 entire Hilbert family 延拓该完整表达，不能独立取其 half 的 A/B poles。
这是所有共轭、两个 mixed terms 和 classical factor 的明确校验。
其中不出现 1/ζ；unknown zeros 的原E奇点被完成后可去。

## 7. 冻结 quarter-line 的全频 Bochner 费用

此处是对 C016 指定实际参数与原 physical norm 的具体费用核验；不是原文摘要。
冻结 s_t=1/4+it/2，2s_t=1/2+it。
对 |t|≥1，下面的粗界无需 ζ 零点信息。

对整数 N≥1、Re z>0、z≠1，先在 Re z>1 用 Stieltjes 分部积分，再解析延拓，得

    ζ(z)=Σ_(n≤N)n^(−z)+N^(1−z)/(z−1)−z∫_N^∞ {x}x^(−z−1)dx。

若 z=1/2+it，选 N=ceil |t|，四项绝对值给 `|ζ(1/2+it)|≤C(1+|t|)^(1/2)`。
同时 |ζ(3/2−it)|≤ζ(3/2)，且 Λ(−1/2+it)=Λ(3/2−it)。
[DLMF 5.11.9](https://dlmf.nist.gov/5.11.E9) 的固定实部 Gamma 竖线估计于是给

    |A(s_t)|+|B(s_t)|≤C(1+|t|)^(9/4)e^(−π|t|/4)。               (AB)

这里指数 `π|t|/4` 来自 Γ 的 imaginary part t/2，不是 t；两个 ζ factor都保留。
CMS 的对角形式在 t≠0 是

    ||F_Y(s_t)||²=2[|B(s_t)|²Y^(1/2)−|A(s_t)|²Y^(−1/2)]
      +[A(s_t)overline(B(s_t))Y^(it)−B(s_t)overline(A(s_t))Y^(−it)]/(it)。

用 (AB) 及完整两 mixed terms 的上界，对 |t|≥1 得

    ||F_Y(s_t)||≤C Y^(1/4)(1+|t|)^(9/4)e^(−π|t|/4)， Y≥2。       (FULL)

|t|≤1 时，entire family compact bound 配合下面的 constant-mode 积分付同样形式（增大C）：
`∫_2^Y |A y^(1/4)+B y^(3/4)|²dy/y²≤C Y^(1/2)`，
其 cross 项为 log Y，并有 log Y≤C Y^(1/2)。H_2 在此 compact 参数段有统一上界。
所以 FULL 对整个实轴及所有 Y≥2 有效，常数不依赖 L、t、Y。

任意 fixed Y，Cauchy circles radius<1/8 把 Re s 保在 [1/8,3/8]；
同一 Euler integral 与 Gamma bounds 在圈上给 polynomial times同指数衰减，
因此每个 fixed m 的 `||∂_s^m F_Y(s_t)||≤C_(Y,m)(1+|t|)^B e^(−π|t|/4)`。
可取 B=19/8；Cauchy 的 m! 与 radius费用不能省。
这支付所有 finite parameter jets 的 wholefrequency integrability，不提供无费无限 jet operator。

令 physical f 是任意 complex L²(R)，Fourier 为 `hat f(t)=∫ f(u)e^(−itu)du` 的 Plancherel 延拓。
因为 FULL 的右边属 L²(dt)，Cauchy–Schwarz 付

    A_Y f=(2π)^(-1)∫_R hat f(t)F_Y(s_t)dt

为绝对 Bochner integral，且 `||A_Y f||≤C Y^(1/4)||f||_2`。
对同样所有 f,g，doublefrequency polarization 有绝对 majorant
`|hat f(t)hat g(v)| ||F_Y(s_t)|| ||F_Y(s_v)||`，可合法写成 H_Y 的双积分。
这特别包括任意 L、零延拓 L²((-L,L)) 与原 Dlog 域，不把 compact support 当 frequency cutoff。

同一 FULL 给 band constant-mode packet 的 Bochner 积分（可先由 H_Y=H_2+B 或直接 dy积分核）。
所有这些 f,g 满足

    <A_Y f,A_Y g>−<C_(2,Y)f,C_(2,Y)g>=<A_2 f,A_2 g>，
    C_(2,Y)f(y)=(2π)^(-1)∫ hat f(t)d_(s_t)(y)dt。

正交等式在共同原f上成立，费用真实为完整双频 cusp Gram；无 finite frequency 限制。
但 A_Y 的 Fourier-side kernel F_Y(s_t) 属 L²(dt;L²(M))，所以 A_Y 是 Hilbert–Schmidt。
对每个 fixed Y 与每个 nonempty source interval，它限制于 L²((-L,L)) 仍 compact。
无限维原norm上不可能从该 positive Gram 本身抽出 uniform positive lower norm bound。
这是一项来源准入费用；不推出 complete Weil Q 负，也不排除另有 signed bridge。

## 8. 无零 β、直接 source 逆权的合法域及限定逃逸

按 root 指定，置

    β(t)=B(s_t)=s_t(s_t−1)Λ(3/2−it)。

这不是含未知 critical zeros 的 A。绝对 Euler product 与绝对 1/ζ Dirichlet series给

    ζ(3/2)^(-1)≤|ζ(3/2−it)|≤ζ(3/2)。

Gamma 没有 zero，固定竖线的 Stirling 双边界加 compact t 连续性给
`|Γ(3/4−it/2)|≍(1+|t|)^(1/4)e^(−π|t|/4)`。
`|s_t(s_t−1)|≍(1+|t|)^2`，实部 1/4 确保两个 linear factor全轴都不为零。
因此真实同一 β 对所有 t∈R 有

    β(t)≠0，   |β(t)|≍(1+|t|)^(9/4)e^(−π|t|/4)。              (BETABOTH)

常数是绝对的，不假定 RH、critical ζ lower bound或样本 frequency window。
定义 Fourier-side multiplier M_β h=βh。
它在 L²(dt) 上 bounded/injective，range dense；其 inverse 在准确 range 上为合法 closed、dense-defined、unbounded operator。
没有一条结论说 known range 上 compensation不合法。

直接把原physical source变成 L² Fourier源 `hat f/β` 时，其 maximal legal域是

    D_inv={f∈L²(R): hat f(t)/β(t)∈L²(dt)}。

对任意 finite L>0，有严格等式

    D_inv∩L²((-L,L))={0}。                                    (EMPTY)

证明：写 hat f=βh，h∈L²。任意 0<η<π/4，BETABOTH给
`e^(η|t|)hat f∈L²`，因为 `e^(η|t|)β` 有界。
在 strip |Im z|<η，逆Fourier integral `g(z)=(2π)^(-1)∫hat f(t)e^(itz)dt`
由 Cauchy–Schwarz和剩余 exponential margin绝对收敛，所有 finite derivatives在compact子strip同样收敛。
于是 g holomorphic且其 real-line代表等于 f。
若 f的零延拓支持于[-L,L]，g在两个外部real interval上几乎处处为零；连续性使其处处为零，
identity theorem给g在connected strip恒零，因此f=0。所有complex f都包括，不仅real/even源。

EMPTY排的是先在原L² Fourier源空间实施inverseβ、再套已付bounded A_Y 的norm运输。
它不排另一种直接vector normalization：令 U_Y(t)=F_Y(s_t)/β(t)，
FULL与BETABOTH给 `||U_Y(t)||≤C Y^(1/4)`。
所以每个原Cc∞源的hat f∈L¹时，`(2π)^(-1)∫hat f(t)U_Y(t)dt`仍是合法Bochner积分，
即使hat f/β不是L²。这种定义与在integrand内补偿的形式相同，不能被EMPTY宣布不合法。
不能从pointwise bounded U推L²→Hilbert bounded性；下面独立支付其真正fixedL operator界。
actualQ比较、全parameterjets与signed/cross费用仍须另核。

### 8.1 直接 U 的真实对象，无零分母及全轴 coefficient

散射函数方程与同样的constant-term截断给精确等式

    U_Y(t)=F_Y(s_t)/β(t)=φ(s_t)^(-1)E_Y(s_t)=E_Y(1−s_t)。

最后一个等式按meromorphic延拓包括A(s_t)=0的点，不能在这些点独立除φ；
分母 β 全轴非零，使左端本来就合法。
记 r_t=1−s_t=3/4−it/2。此处原E的 denominator Λ(2r_t)=Λ(3/2−it) 无零，
没有criticalζ inverse。其constant mode为

    y^(r_t)+R(t)y^(1−r_t)，
    R(t)=A(s_t)/β(t)=Λ(1/2+it)/Λ(3/2−it)=φ(r_t)。

Γ(1/4+it/2)/Γ(3/4−it/2) modulus为 O((1+|t|)^(-1/2))，
elementary Euler bound与ζ(3/2) inverse lower给整个实轴 `|R(t)|≤C`。
这项变换恰是原r_t-line Eisenstein family，不是一个假设的newpositive source。

### 8.2 所有 Y≥2 的 fixedL 原L²直接 packet

对f∈Cc∞((-L,L))，置

    ψ_f(y)=y^(3/4) f(−(log y)/2)，
    Θψ_f(z)=Σ_(Γ∞\Γ)ψ_f(Im γz)。

ψ支持[a,b]=[e^(−2L),e^(2L)]。Mellin convention为

    m_f(r)=∫_0^∞ ψ_f(y)y^(−r)dy/y
          =2∫_(−L)^L f(u)e^(2(r−3/4)u)du，
    m_f(r_t)=2hat f(t)。

从Re r=2的绝对原E展开做Mellin inversion，再把contour移到Re r=3/4，
穿过的唯一pole是r=1。给所有Y≥2的Hilbert-valued精确恒等式

    T_Y f:=(2π)^(-1)∫_R hat f(t)U_Y(t)dt
      =Λ^Y[Θψ_f−(6/π)(∫_(−L)^L f(u)e^(u/2)du)·1]。             (DIRECT)

这里 residueE(r=1)=3/π，m_f(1)=2∫f e^(u/2)，故rank-one coefficient确为6/π。
Λ^Y在右侧是quotientL²的orthogonal projection：在cusp y>Y减x-average，其他位置不动。
其operatornorm为1，constant1的截断为1_(y≤Y)。不把fullcusp减法换成截掉全部Fourier modes。

contour费用可独立由已付MS核，而不依赖untruncated E的L²属性：
对3/4≤σ≤2、|v|≥1，φ(σ+iv)全带一致有界。
这是Γ ratio O(|v|^(-1/2))、numeratorζ(2σ−1+2iv)=O(|v|^(1/2))的Euler bound，
以及denominatorRe(2σ)≥3/2的绝对inverseζ下界共同给出的。
MS对角有2σ−1≥1/2且2iv不为零，故||E_Y(σ+iv)||≤C_Y。
m_f在该带的vertical方向superpolynomial下降，由compact smooth ψ的重复分部积分支付。
所以rectangle horizontal sides在L²范数下趋零，Bochner contour移位合法。
带内原E的常数项只可能在r=1有pole；Bessel series没有额外pole，Λ(2r)在Re r≥3/4无零。
其截断residue为(3/π)1_(y≤Y)，正与DIRECT右侧匹配。

最后给非最优但显式fixedL bound，不能只宣称finitecoset。
令y_min=√3/2，

    C_L=ceil(e^L/√y_min)，  D_L=ceil(e^(2L)+C_L/2)，
    N_L=1+C_L(2D_L+1)。

对z=x+iy∈D，任一非identitycoset用primitivepair(c,d)、c≥1表示。
ψ_f(Im γz)非零要求a≤y/|cz+d|²≤b，因此
`c≤e^L/√y_min=C_L`，且非identity的Im γz≤1/y使y≤b。
又`|cx+d|≤√(y/a)≤b`，故|d|≤b+C_L/2≤D_L。
identitycoset只有1个，且也须y≤b；因此所有z上最多N_L个非零summands，Θψ_f支持D∩{y≤b}。

Cauchy–Schwarz加nonnegativeunfolding给

    ||Θψ_f||²≤N_L∫_0^∞ |ψ_f(y)|²dy/y²
             =2N_L∫_(−L)^L e^(−u)|f(u)|²du≤2N_L e^L||f||²。

常数向量的norm为√(π/3)，故DIRECT与projection contraction给

    ||T_Y f||≤K_L||f||，   K_L=√(2N_L e^L)+√((24/π)sinh L)，
    所有Y≥2、所有complexf∈Cc∞((-L,L))。                       (FIXEDL)

以density延拓，FIXEDL给原L²((-L,L))上唯一boundedoperator，因而也保原Dlog源。
Cc∞上的integral由boundedU与Schwartzhat f绝对Bochner合法；一般L²源以该extension定义，
不能额外宣称每个一般源都满足absoluteBochner，因为hat f未必L¹。
这里没有变norm、删pole、取finitefrequency或拟合ζ零点。
N_L=O(e^(3L))，K_L=O(e^(2L))只是这一个finitecoset证明的粗上预算，
不是必要growth费用。下面的完整双频signedGram提供对fixedY独立于L的更强界。

来源准入结论必须修正为：rawcompletedA_Y是compact；先inverseβ的原L²路线为空域；
但直接uncompletedU_Y的原fixedLsource norm已支付。没有理由把C016的fixedL范数接口继续列unknown。
仍未支付的是actualQ/fullΓ/strictpp/dualpolesigned桥、成长净后果和全parameterjet运输。
knownrange逆、直接vectornormalization及signed响应未被EMPTY排除。

### 8.3 Full-cusp source blind band 与 noncompact 对照

下面是对原directU source的进一步独立校验，不能用rawcompletedcompact性替代。
先核一个fundamental-domain高度事实：对非identity coset(c,d)、c≥1，在D上有|cz+d|≥1。
当c≥2用c²y²≥3；当c=1,d=0用|z|≥1；d=±1用
`y²+(x±1)²≥1−x²+(x±1)²=2±2x≥1`，其余d更大。
同时|cz+d|²≥c²y²，因此

    Im γz≤min(y,1/y)≤1       (非identitycoset，所有z∈D)。

若ψ支持于y>1，则Θψ在D上只有identity项，正好为ψ(y)（y≤1处亦为0）。
令u0=(log2)/2，ℓ(f)=∫f(u)e^(u/2)du。

对任何fixedL>u0，子空间

    V_L={f∈Cc∞((-L,−u0)): ℓ(f)=0}

无限维。ψ_f全在y>2，Λ2删除其全部identityconstantmode；DIRECT的rankone项也因ℓ0消失。
于是严格全源等式

    T_2 f=0                 (所有f∈V_L)。                     (BLIND)

任意有限线性source条件后V_L仍无限维，条件可包括实际两pole线性functional。
不需要ζzero数据、finitefrequency或极限Y→∞。
按fullcusp正交identity，所有Y≥2的净Gram `||T_Yf||²−||C_(2,Y)f||²`
仍恰是||T2f||²，故variableY也不修复这条固定baseheight2的blind band。

因此任何fixedL>u0、任意有限条件、任意原L² boundedcompactselfadjointK及任何c>0，
不可能在这些合法smooth源上有

    ||T_2 f||²+<Kf,f>≥c||f||²。

证明是在V_L与finiteconditions的交中取原L² orthonormal smooth sequence。
该sequence弱趋0，compactK的quadratic值趋0，而T2恒零。
这只排uniformpositiveframe与compact修复；不推actualWeil负、不排无限秩非compact费用，
也不排改变baseheightY0(L)、源分块、多channel或真正signed桥。

另一方面，对每个L>0，令a_L=min(L,u0)，取

    W_L={f∈Cc∞((-a_L,0)): ℓ(f)=0}。

ψ_f支持1<y<2，Θψ只有identity项且Λ2完全保留，故

    ||T_2 f||²=∫_1^2 |ψ_f(y)|²dy/y²
                =2∫_(−a_L)^0 e^(−u)|f(u)|²du≥2||f||²。

W_L无限维；取原L²smoothorthonormal sequence，image norms不趋0，证明T2在每个原fixedL空间上noncompact。
此对照确认直接U的boundedsource运输与completedA_Y的compact运输确是不同算子。
不能把EMPTY或completedcompact性无声搬成“所有去completion的算子都compact/非法”。

### 8.4 完整双频 Cauchy/Hilbert–Hankel 给独立于 L 的全轴界

这是对packet代理进一步发现的独立逆核，全部常数重新计算。
设m(t)=R(t)=A(s_t)/β(t)，M=sup_R|m(t)|<∞，a=(logY)/2。
真实scalar源满足m(−t)=overline(m(t))，因为Γ/ζ对共轭参数的值共轭，且denominator全轴非零。
CMS除β(t)overline(β(r))给directU的完整Gram

    J_Y(t,r)
      =[m(t)overline(m(r))Y^(−1/2)e^(ia(t−r))−Y^(1/2)e^(−ia(t−r))]
           /[−1/2+i(t−r)/2]
       +[m(t)e^(ia(t+r))−overline(m(r))e^(−ia(t+r))]/[i(t+r)/2]。

第一行两项分别是Cauchy卷积与boundedphase/m乘子的夹心。
以频率平移变量x=t−r，

    C(x)=1/[−1/2+ix/2]=−2∫_0^∞e^(−u)e^(ixu)du。

卷积C的Fourier multiplier为−4πe^(−ξ)1_(ξ>0)（endpoint约定不改operator），norm恰4π。
所以第一行operatornorm≤4π(Y^(1/2)+Y^(−1/2)M²)。
第二行每项是reflection后的PV Hilbert卷积，PV1/x multiplier为−iπsgnξ，normπ；
因分母i(t+r)/2，每项额外factor2，给2πM，两项总界4πM。
anti-diagonal r=−t处numerator严格零；m smooth，所以合起来的kernel是原removable连续值。
在smoothcompactfrequencycoefficients上，分别PV的difference正等于完整kernel积分；
使用purePV而非未说明的i0boundaryvalue，不添delta项。

因此J_Y在原L²(dt)上的operatornorm≤4π[Y^(1/2)+Y^(−1/2)M²+M]。
先对compactfrequency源使用真实HilbertGram，再以该界定义其Cauchy极限，
packet(2π)^(-2)及Plancherel||hat f||²=2π||f||²给

    ||T_Y f||²≤B_Y²||f||²，
    B_Y²=2[Y^(1/2)+Y^(−1/2)M²+M]，所有complexf∈L²(R)。        (UNIFORM)

这付原整个L²(R) source norm，特别对所有L及原Dlog；fixedY常数独立于L。
完整base2 cusp扣除后的T2因此有统一成长source upperbound，而BLIND及noncompact对照仍成立。
没有必要的e^(2L)范数费，不能用旧K_L粗上界宣布growthnorm失败。

frequencycutoff的强H延拓与smoothcompactphysicalsource的绝对Bochner相同。
对每个一般L²源仅有逐源Fourier尾误差

    ||T_Y f−T_(Y,≤T)f||≤B_Y[(2π)^(-1)∫_(|t|>T)|hat f(t)|²dt]^(1/2)。

Dlog源还可把尾除以sqrt(log(2+T))并用原logweightedFourier能量控制。
这不是整个L²unitball上的uniform小误差；有限频率算子为HS，而T2非紧，
故这些有限频率截断不可能在原L²operatornorm趋于T2。
wholeaxisboundednorm与operatornormtailcontrol必须分开。

## 9. s completion 与实际 ξ 的 polynomial factor 不相同

设 w=2s。F用于清E*自身在s=0,1的pole；其first constant coefficient是

    A(s)=[w(w−2)/4]Λ(w)。

实际 entire ξ(w) 的规范为 `[w(w−1)/2]Λ(w)`，因此meromorphic关系为

    A(s)=[(w−2)/(2(w−1))]ξ(w)。

这里不能只说first coefficient是ξ：A在w=1有pole，必须由B的constant项相消；
ξ在w=1是finite。把整个E*换乘实际ξ的prefactor得到

    F_ξ(s)=2s(2s−1)E*(s)=[4(w−1)/(w−2)]F(s)。

该替换在w=2重新有pole，在w=1给额外zero，改变全参数pole/jet ledger。
原F(0)=F(1)=1/2的endpoint记账因此不能自动搬到F_ξ。
但冻结physical line w=1/2+it上，这个ratio与inverse均有界：其modulus位于[4/3,4]。
所以line上额外bounded Fourier multiplier并不修复completed A_Y 的compact性；
另一方面也不能把line上的因子差本身称为norm无界障碍。
若使用它，原compactphysicalsupport、全部parameterjets/poles与actualdual-pole对应须分别重新支付。

## 10. 净状态、未付前件与可消费范围

已支付：classical factor1 的四项、所有 coalescence、完整 cusp Gram、0/1及half completion、
entire compact-uniform L² family、全部finitejets、指定quarter-line整轴Bochner和原L²上bounded/compact运输，
以及β全轴无零双边费用、严格限定的directinverse原compactsource空域，
directU=E_Y(3/4−it/2)原fixedL boundednorm（所有Y≥2统一）、
更强的全L²(R)fixedY uniform-L norm、fullcuspblindband和noncompact对照。
原 Dlog 没有被替换，所有 complex f 均保留。

未支付：doublefrequency H/B 与 actual 单频 Γ=Reψ(1/4+it/2)−logπ=2θ′、
全部 strict primepowers、双 pole signed 型之间的同对象比较；原norm下可核误差；
危险 core/补空间、成长联合费用、完整 Ξ 识别。CMS 不是 actual Weil identity。
inverse q 必须另付其 zeros/poles、exponential inverse Gamma 及合法域；completion 不能自动保证可逆谱可见性。

这些 norm/orthogonality oldtool 本身不超旧016/028或新543的完整负惯性上预算。
BLIND是这个具体sourcepacket/framegate的实际费用边界，不是全modular几何方法类完成证书。
本稿不给新 whole-spectrum forcing，也不给整个modular几何方法不可能定理。
建议 root 用本稿与独立sourcepacket/逆审核 actual 桥；没有桥则停止本source主攻。
原PDF、classical公式恢复、代理数或文件编号均不消费cadence；
§§7–8的新实际common-source费用/BLIND完整准入可独立结算一次失败研究轮，
但不能把该sourcegate晋级为新whole-spectrumforcing或宏观完成。
会改变选择的证据是一个包含 actual全部项/原complexnorm/成长参数的 signed共同比较，
它严格弱于所求 Q 正性并胜过最强既有 consequence；单独Gram正性不满足这个门。
