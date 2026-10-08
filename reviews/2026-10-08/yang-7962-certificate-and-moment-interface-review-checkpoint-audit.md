# Yang–Yang 79.62%：有限证书、矩接口与 Lean 范围独立审查

2026-10-08，checkpoint_audit。仅写本份审查，不改外部来源、旧笔记或 Git。

结论分层：精确有理证书 **PASS**；有限全实谱条件消费 **PASS**；
给定模型矩的必要 PSD 检查 **PASS**。这些结果不认证实际 zeta 的无限矩输入，
不认证 79.62% 已成为公开最佳定理，也不认证全部论文或 C26。
原文零侧记号/共轭及 tail trace normalization 有可明确定位的接口偏差，
必须纠正或另证后才能声称按所写公式完整接上实际矩阵。

## 1. 固定版本、主源与读取范围

Primary：[Zenodo 21975237](https://zenodo.org/records/21975237)，Hongyi Yang、Shihua Yang，
August 2026 的 preprint。其 simple-critical 与 distinct 声明不同。
本次固定仓库 commit：

`d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`

[固定 paper.tex](https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/paper.tex)，
canonical UTF-8 LF SHA256：
`a2be2895348a26c93ca97ebf0f202c69cf2e3b447415c5e7174fd954601666f2`，
133073 bytes，2892 行。canonical 只统一 CRLF/lone CR，不 trim、不改 EOF。

[本地 Zenodo PDF](../../literature/unreviewed/2026-yang-7962-unreviewed-v1.pdf)
与固定 commit 的 paper.pdf 逐字节相同：598532 bytes，38 页，
MD5 `0811e74faaffe8ef7b216cc004481eb5`（亦与 Zenodo 公布值一致），
raw SHA256 `0abaa78e0eb4421fdbae647a0b3b6b0299a4dde5d49b0e56ca6f33831c5e3ea0`。

本审查全文读取所有四个 Lean 模块、两个 certificate Python 文件、README、
REPRODUCTION；paper.tex 精读完整 framework、zero-side、first-two-moment、
certificate、degree-six consumption、verification-status 和 A6 部分：
310–582、594–674、1823–1945、2065–2230、2770–2820 行，
并核读 abstract、framework relation、method overview 与 references。
未把此范围写成对全 2892 行或全部高矩解析证明的完整审查。

| 固定 commit 来源 | canonical SHA256 |
|---|---|
| [certify_lp.py](https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/certification/certify_lp.py)，81 行 | 43771f20c5b31280ef348add65ca6dc7c67d4a93bd46f062f9690f8c6e5b3df5 |
| [certificate_family.py](https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/certification/certificate_family.py)，92 行 | c9948aeca811ef897592ccbc8cfcbbeb230fc4609868eb23c8ebffbc2681c4a6 |
| [Anchors.lean](https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/lean/RhGate/Anchors.lean)，39 行 | 50f83a75219fcc203398a8ee04438904b58bd565274b253a8164fcfae6e8e30c |
| [Certificate.lean](https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/lean/RhGate/Certificate.lean)，145 行 | a64e428e60c6db69e753b05ac1fa532ea5cf2539f24452ca9e5885495d4b882e |
| [LocalClosure.lean](https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/lean/RhGate/LocalClosure.lean)，60 行 | 467ceb241dc8dbc55da84f79d2250ca818826035b7c62476c2d5587c08cd85aa |
| [LocalClosure2.lean](https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/lean/RhGate/LocalClosure2.lean)，66 行 | ac096e57174883f000d240f3cc58842963297ea2842c91f2a5c7f82e467dbcee |
| [README](https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/README.md)，56 行 | fe1234ec38480dc310f9f92aa1a6b3403eef51e85203409531113ccb3f4b6679 |
| [REPRODUCTION](https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/REPRODUCTION.md)，182 行 | e60c0bfa43195289b28334c17ff655f8b613a76dfe1434750721756c96ebd178 |

## 2. 精确 cubic-square 证书的独立重算

paper.tex 1846–1888、2770–2819 和 certify_lp.py 41–72 的输入是

\[
 (m_0,\ldots,m_6)=(1,1,4/3,2,13/4,101/18,12809/1260),
\]

消费只需前四矩固定、m₅ 的下界和 m₆ 的上界；不必把所有高矩等号当成前件。
令 a=5323/10000、b=6561/5000、c=10293/5000，
P(x)=[(x−a)(x−b)(x−c)]²/(abc)²。

本次使用 elementary symmetric coefficients 独立展开 cubic，
再作精确 Fraction 运算，不调用作者的 polymul 或优化器。
分母 (abc)²=129222147277358919747441/62500000000000000000000。
P(0)=1，P≥0 在整个实轴成立，全部 y_k 的符号严格交替。
特别地

\[
 y_5=-487887500000000000000000/129222147277358919747441<0,
\]
\[
 y_6=62500000000000000000000/129222147277358919747441>0.
\]

精确结果为

\[
 w_0=\sum_{k=0}^6y_km_k
 =829278553005924403328783/8140995278473611944088783,
\]

w₀=0.101864517130810716499815490599043281…，

\[
 1-2w_0=6482438172461763137431217/8140995278473611944088783
 =0.796270965738378567000369018801913437…,
\]
\[
 1-w_0=7311716725467687540760000/8140995278473611944088783
 =0.898135482869189283500184509400956719… .
\]

与 0.7962、0.8981 的严格余量分别为
2888658705366537738639877/40704976392368059720443915000，
2888658705366537738639877/81409952784736119440887830000。
因此所写 decimal headline 的精确算术正确。

本次也核得 y₅+6y₆=−112887500000000000000000/129222147277358919747441<0。
当前 inputs 已是 exact corner；早期 bands 的 correlated corner 优化不是
现在 headline 有效性的前件。作者的有限 LP solver/grid 也不是此证书的前件。

## 3. 完整实谱及有限误差的条件消费引理

原 degree-six lemma 1855–1861 只写 ν 在 [0,∞) 上的 origin mass。
无条件 Weil compression 可有负特征值，故不能直接假定实际谱 measure 为正支撑。
但本证书的形式允许一个直接且严格的全实轴修补，不需要 RH：

令 ν 为实轴上的概率 measure，六阶绝对矩有限（有限 Hermitian 矩阵自动满足），
0≤h<min(a,b,c)，C(h)=∏_{r∈{a,b,c}}(1−h/r)²>0。
若 x≤h，每个 1−x/r≥1−h/r>0，故 P(x)≥C(h)；
其余实轴 P(x)≥0。因此

\[
 \nu((−\infty,h])\le \frac{\int P\,d\nu}{C(h)}.
\]

这覆盖全部负谱、近零谱及趋于零的 threshold，而不是只控制 ν({0})。
六次系数严格交替，所以奇数矩的下界和偶数矩的上界足够。
若 m_k 对 target 的允许偏差为 ε_k，则对应方向的前件给

\[
 \int P\,d\nu\le w_0+\sum_{k=1}^6|y_k|\varepsilon_k.
\]

前四矩的两侧误差也可用同一式支付。独立精确重算
∑_{k=1}⁶|y_k|=7210232354796702966520000/129222147277358919747441。
由于 C(h)→1，固定有限误差预算和 vanishing threshold 可直接消费；
不能把 sample errors 或数值拟合自动视作 ε_k→0 的实际矩定理。

设实际同一 Hermitian matrix 的 normalized empirical measure 为
ν_T=d^{-1}∑δ_{λ_j(\widetilde G)/ℓ₁}。
计数桥用的 normalized threshold 必须是 h_T=θ_T/ℓ₁。
若零侧桥有效，且 d/N→1、h_T→0、实际矩误差受控，
则 simple-critical 与 distinct 的 liminf 下界分别为
1−2(w₀+∑|y_k|ε_k)、1−(w₀+∑|y_k|ε_k)。
若 λ<1 固定，需先保留 d/N→λ 的因子，最后再作 λ→1 的许可极限；
不得提前免费设 d=N。

## 4. 模型矩的必要 PSD 可行性检查

独立以 exact rational Gaussian elimination 检查
H₃=(m_{i+j})_{0≤i,j≤3} 和 xH₂=(m_{i+j+1})_{0≤i,j≤2}。
全部 22 个 principal minors 严格为正。
leading determinants 分别是

- H₃：1、1/3、5/108、283/108864；
- xH₂：1、2/9、23/1296。

所以该表没有 Hankel positivity 或非负支撑 localizer 的明显矛盾。
例如给定 m₀,…,m₄ 时 m₅ 的 localizer floor 为 177/32，
实际模型 m₅=101/18 的差为 23/288>0；
给定该 m₅ 时 m₆ 的 Hankel floor 为 50953/5040，
模型 m₆ 的差为 283/5040>0。

这是给定 moment table 的有限一致性检查。它不证明该表是实际 zeta compression
的矩，也不证明真实 G 非负，更不是把 sine-kernel/GUE 模型当成算术输入。
本次未重新验证 1310 项 polytope integrations 或其到实际 prime-cycle 的 transport。
即使那些 model integrals 精确成立，actual μ₃,…,μ₆ 的 pinning 仍需独立解析证明。

## 5. 实际 zero-side、归一化与两个明确接口偏差

paper.tex 419–482 所需的有限桥为：G=A+E Hermitian，
||\widetilde E||op≤θ₀；A 的 on-line contribution 正秩一，
off-line conjugate pair 为 hyperbolic pull-back。
Sylvester/Weyl 因而给 n_+^θ(\widetilde G)≤s₁+s₂+p，
而 N(I′)≥s₁+2s₂+2p，所以 s₁≥2n_+^θ−N(I′)。
rank A≤#Z(I′) 给 distinct bound；端点 N(I′\I)=o(N) 必须保留。
这些有限推论本身正确；不需要 evaluation vectors 独立或全部谱非负。
它们仍必须针对实际正确的 Weil matrix 和实际 tail 被证明。

计数口径是 N 计全部非平凡零点重数，N₀ˢ 计 simple AND critical，
N_d 计全 strip 的 distinct zeros。89.81% 不是 distinct critical 比例。

这里使用的 [C26 原 primary PDF](https://www-cdn.anthropic.com/564f962e60643842f5fcb4a17c9dbc8f608f1c37.pdf)
另与 [本地固定 PDF](../../literature/baseline/2026-claude-anthropic-zeta-23.pdf)
视觉核对第6页 (2.2) 和第11–12页 Proposition4.1–4.2；
本地 raw SHA256 `6792988e6cd0e17690621ce898abd5d534f98407741bc7cb14bbe7d07c77d72f`。
没有将这次局部核对称为整个 C26 的独立审查。

第一，坐标与复共轭不一致。C26 的坐标是 z_ρ=(ρ−1/2)/i，
原式为 W(f,g)=∑m_ρ h_f(z_ρ) overline{h_g(overline{z_ρ})}。
Yang 339–342 行及 PDF 第7页却写 ρ=β+iγ_ρ，
W=∑m_ρ h_f(γ_ρ) overline{h_g(γ_ρ)}。
后者按所写是 real-ordinate positive Gram，不能同时作原 complex Weil form 的重述。
即使把 γ_ρ 默认为复坐标，仍须纠正内层 conjugation；
390–391 行的双 φhat 同坐标才会与 C26 正确形式一致。
这是确定的公式/记号接口缺口，可由明确改写再接上 C26，
但本审查不能默默代作者改源，也不据此判 79.62% 命题必假。

第二，449–450 行把 trace-tail bound 的 normalization 换错。
C26 Proposition4.2 对 Ehat=E/(aL²) 给
||Ehat||₁≤θ₀/(aL)≤2θ₀/L；
Yang 却把后一个 RHS 写给 Etilde=E/L。
从所引 C26 可直接得到的是 ||Etilde||₁≤θ₀。
更强的 2θ₀/L 需要另证，不能仅按引用推出。
计数步骤只用 operator norm，故这一偏差不单独推翻上述条件消费；
但使用 trace tail 的实际高矩误差付款须按正确 normalization 复核。

另需避免一个错误质疑：398 行 μ_k=tr(G/L)^k/(dℓ₁^k) 确实包含 ℓ₁ normalization。
μ density≈ℓ₁/(2π)，Parseval ∫φhat²=2πaL，
所以 G/L 的 diagonal main≈aℓ₁，normalized μ₁→a→1。
这里不能丢掉 Parseval 的 2π 或 ℓ₁ 后再宣称第一矩不匹配。

## 6. Lean 真实覆盖与证据边界

lakefile.toml 以四个模块为 roots，无 mathlib packages，toolchain 为 Lean4 v4.33.0。
逐个读取 theorem 类型得到共 21 个声明：Anchors5、LocalClosure1、
LocalClosure2两个、Certificate13；README 的20个计数是旧描述。

Anchors.lean 23–35：任意 Rat anchors 下几项既定 rational expressions 的抵消；
37–39：13/18、31/36 的 rational arithmetic。
这些不是 actual matrix 的 μ₄、μ₅、μ₆ 极限定理。

LocalClosure.lean 51–60 和 LocalClosure2.lean 46–64：
固定 (b,p)=(4,5)、(4,7)、(5,5) 与写定 slopes 的完整 125/343/625 lock-vector cubes。
不是对所有 b、所有 p、所有 unit slopes 的一般 local-law 定理。
invMod 的 Fermat 注释也没有独立泛化为任意模数的逆元定理。

Certificate.lean：Rat polynomial expansion、Rat square nonnegativity、P(0) arithmetic、
M₅/M₆ 的 literal rational sums、y₆ positivity、w₀ corner、headline rational inequalities，
及 t₂₂₂、anchor arithmetic。没有 Real measure、empirical spectrum、ζ、zeros 或 inertia。
M5_exact/M6_exact 的 theorem 类型不提实际 Ursell integrals。
当前源码没有单独的 y₅+6y₆<0 corner-selection theorem；文档仍有旧 band/corner 描述。
该 sign 在本次独立 Fraction 运算中通过，但不能说当前那个声明已经由模块导出。

源码无 sorry 和额外 analytic axioms，并不意味着 analytic prerequisites 已形式化；
这里是根本没有声明它们，而不是通过 proof term 证明了它们。
本次未安装 Lean、未重新 lake build，故 maintainers 的 kernel-build 日志属于
作者提供的验证记录；本次结果是源码类型核验及独立 exact arithmetic。
paper.tex 2209–2217 本身亦明确 moment pinning、measure consumption、analytic chain 未形式化。
作者未提供本论文经过外部同行评审的证据；同作者自检和模型数值不是该证据。

README/REPRODUCTION 中还保留旧 bands、0.7947 和33页等描述，
但固定 paper.pdf 实为38页、当前 Certificate.lean 使用0.7962/0.8981。
这些 drift 不破坏重新算出的有限证书，审查须以固定源码的实际内容为准。

## 7. 对本项目的可用启发与优先级

完整读取 [197](../../notes/197-partial-weil-proportions-regions-four-moments.md) 325 行，
canonical SHA256 `98bd8ea89679030e0ffb8135d324b5654900f260b3f45c9ae816d5ea870eaae7`。
其 §§3–4、§9 的方向更贴近项目当前已登记的实际前件：
保留部分 Weil 配置、finite E₀/E₁、原观察窗/normalizer，
只支付 actual centered second moment v 与一侧 centered fourth upper B₄。
消费 (1−v)²/(1−2v+B₄) 要沿现有197/306/228的完整有效域与误差合同使用。
本次不重新认证这些旧来源的全部证明，也不引用197内旧文献阈值作为当前最佳。

这个优先级成立：不必为追逐79.62而同时认领六个精确模型矩，
也不必单独证明 m₃。centered two/four 信息不足以偷换成 raw m₁,…,m₆；
模型 table、有限 certificate、每个已付实际块三者应分别登记。
degree-six 全实谱引理可保留为后续条件消费工具，
而 actual original whole/coupling 的未付第四矩预算仍须先支付。

本次执行自写、只读、in-memory Fraction/PSD/PDF 核对代码，
并在全文读取后运行下节的 root 有限检查器 --check。
外部源码先全文阅读，未执行未知 pipeline、GPU suites、安装命令或外部 Lean 工程。
只写本审查文件，未改 Git、旧笔记或研究源。无限解析与实际比例结论均未认证。
## 8. 本轮 root 精确检查器与输出的独立全文复核

本节是随后获授权的同一审查补充，未改任何 source/checker/output。
完整读取 [root finite script](../../scripts/yang_7962_finite_audit.py) 149 行，
canonical 6464 bytes，SHA256：
`ff951d22c4247b873162cefc870913a330a6eeb8e07cb664ccfe1cacdf030c1b`。
完整读取 [saved JSON](../../output/yang-7962-finite-audit.json) 188 行，
canonical 5598 bytes，SHA256：
`a01c20f2e4f0dbfca5908ce17373006d97c8ff7740182a190e46e63e8ea5bb0a`。

独立审查结论：有限算术与明确标记的诊断范围 **PASS**。
37–76 行的 exact Fraction 消费和 comparison budgets 与前述独立展开一致；
142–144 行 --check 只读旧输出并精确比较，不写文件。
只在 --write 分支才会写 OUT；本次没有调用该分支。
105 行的作者 commit 只是固定 metadata；其真实来源已在本审查 §1 另外核实。
45–46 行 raw PDF binding 正确。

独立实际运行：

`C:\Python312\python.exe -B -X utf8 scripts/yang_7962_finite_audit.py --check`

exit 0，stdout：

`PASS: 16 exact finite checks; analytic inputs remain unproved.`

还以自写代码独立重算 comparison error budgets，并把 toy 的完整枚举区间
扩到 m,k,j∈[-3,3]、density displacement∈[-4,4]，保持原 support={0,1}。
仍得到 resolved energy 8、density Parseval energy 70、all-free-lock energy 18，
positive-k resolved energy 1。三者是不同有限对象。
mod3 offsets [0,-2,4,2] 禁止全部三个 residue，allowed=0；
twin offsets [0,-2] 仅余一个 residue，allowed=1。
这些是 generic finite identity/local-mask 诊断，不能单凭它们判定实际 prime
asymptotics 错误，也不是本审查新造的无限素数反例。

target p=841853/1250000=0.6734824 是本轮提供的 comparison datum，
本检查器不认证它的文献 provenance、条件或最优性。
固定 v=1/3 时，独立精确推得

\[
 B_{\rm cap}=\frac{(1-v)^2}{p}-1+2v
 =\frac{2474441}{7576677}
 =0.326586576146772523099506551486885345\ldots .
\]

因此若同一有效 finite configuration 的一侧 B₄ 严格小于此 cap，
并支付全部 normalization/endpoint/configuration errors，才得到严格超过 p 的
中心四阶条件消费。其他 actual v 应使用该式的 v，不能免费换成平窗1/3。
16/21 payoff 对 nominal (v,B₄)=(1/3,1/4) 的算术亦通过。

JSON common moment allowance≈0.0011003114 与单一 fourth/fifth/sixth allowances
都给恰等于 target 的预算端点；严格改善需要严格小于相应误差预算，
且有限 h 的 C(h) 和 count/configuration error 必须另付。
该有限输出将 analytic moments、zero proportion、zero-free proof flags 全部置 false，
与实际审查范围一致。没有将此 --check PASS 升格为无限解析证明。
## 9. 最终综合报告的全文复核与绑定

全文读取最终 [综合深审](../../literature/supplements/2026-10-08-yang-7962-deep-audit.md)，
231 行，12062 canonical bytes，SHA256：
`7e2be39fa25c6ffaa3c8a16c3437fd52c13ac31fd2b9e8edc40492aa1a2f6407`。

其 §2.1 全实谱正平方 majorant、有限 C(h) threshold、方向性 moment errors、
同一实际矩阵前件及先保留 d/N→λ 再取 endpoint 的计数消费，独立核对通过。
§6 精确 flat cap 与现有中心四阶路线的有限配置、m₀/m₁、E₀/E₁、
positive denominator、σ branch 及实际 B₄ 上界条件均已明确补入；
它不把 canonical scalar growth bound 直接代为 centered-fourth constant。
(v,B₄)=(1/3,1/4) 给 σ=1/8；比较 cap 的 σ 亦严格在 [0,3/4) 内。
该两处条件推导无阻断问题。

另全文读取 [独立解析引擎审查](yang-7962-analytic-engine-review-whole.md)，340 行，
canonical SHA256 `35cdf1da36b7c59ed6894c88b992df0534ab7a605063706535957ff113a528a6`。
本次额外核对 primary paper.tex 741–794、1070–1111、1152–1182、1256–1285：
原四腿/continuum 外权、全局 ℓ₁ 归一化、文面 cell-tail 与 FFT density 的对象
确实如综合报告定位。完整 toy 与 mod3 unit mask 的算术由本审查独立验证。
未将这些 generic finite tests 表述为实际 prime asymptotics 的反例。

这个绑定表示本审查全文核对了综合报告的证据层次和上述有限消费，
不表示独立重做上游全部 arc/transport proofs、原 third-through-sixth infinite estimates
或1310项 model integrations。那些解析输入仍未认证，尚不构成可调用的79.62%纪录。
本审查据此冻结；没有进一步修改 source、script、JSON、综合报告或 Git。
