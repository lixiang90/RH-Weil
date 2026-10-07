# Gaussian root-weight probe：真实 Poisson、局部障碍与共同符号的窄 raw 二矩

日期：2026-10-07。状态：完整研究稿，root / radial / twisted 全文限定 PASS；范围见审查报告。

本稿只研究新 probe，不修改 checkpoint 457、已有数域报告、固定 `paper.tex`、Goal 或 Git。结论有两层：

1. 可以用已知 quartic theta 的 square coefficient 所提供的 **root Gauss weight** 定义一个真实 Schwartz probe。旋转窗口使 Poisson 的 unit dual 恰为 `k=1`，并保留任意同一 finite-order target `η(n)`。它给出一个精确的平滑 Möbius identity；该 identity 本身没有 cancellation estimate。
2. 对固定数量的 disjoint once-prime slots，按固定源的 **共同角色符号**，可以直接证明真实 raw inverse × prime 二矩 `≪ (U+T_col²)(UT_col)^ε`。这保留 inverse/slot overlap 和零掩码，是一个窄范围定理。无 slot 时它只在 `U≥D²` 给出任意小幂损失的 `O_ε(U^(1+ε))`，不足以替代 checkpoint 457 所需每个 `c>0` 的 `U≥D^(1+c)` 合同，因此不宣称新的无零边界。

## 1. 固定输入和归一化

固定源为只读文件

`E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`，

commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`，canonical LF SHA-256
`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`。
原 raw statement 在 12343–12360；marked contract 的共同 `ν, εχ` 和 slot 权重在 9219–9265。本稿与原合同比较时，保持这两个合同的范围。

Gaussian 原始输入采用 David–Dunn–Hamieh–Lin 的 v5（2026-01-30）：
[Quartic Gauss sums over primes and metaplectic theta functions](https://arxiv.org/html/2306.11875v5)，尤其 §§3、4.5、9。先前版本的 degree-one phase 和 inert-prime 定号不能代替 v5。详细来源审查已在已提交的 `hybrid-gaussian-quartic-feasibility-research.md` 完成；这里不重复来源判断。

设 `K=Q(i), O=Z[i], λ=1+i`。奇 primary 元素满足 `n≡1 mod λ³`；每个奇理想取其唯一 primary generator。`q_n=Nn=|n|²`，`α(n)=n/|n|`。固定排除集合 `S` 默认包含 `λ` 和 target 的全部坏素数。`n` 以下若未另说均为奇 primary squarefree，且避开 `S`。角色

\[
 \chi_n(h)=(h/n)_4
\]

在所有非单位 residue class 上延拓为零。定义 DDHL 的 additive character、Gauss sum 和 normalized Gauss sum 为

\[
 \check e(z)=\exp(4\pi i\Re z),\quad
 G_j(n)=\sum_{h\bmod n}\chi_n(h)^j\check e(h/n),\quad
 \gamma_j(n)=G_j(n)/\sqrt{q_n}.
\]

已有严格 squarefree signal 是

\[
                         \gamma_1(n)^2=\mu(n)\alpha(n).                 \tag{1.1}
\]

其 degree-one 局部式为 `γ₁(π)²=−α(π)`。v5 的额外 factor
`(barπ/π)_4^(−2)` 在 primary degree-one `π=a+bi` 上等于
`(2/p)_2=χπ(−1)`；`(a/p)_2=1` 由 `p=a²+b²` 和 quadratic reciprocity 得到。inert primary `π=−p` 处 Frobenius / conjugation 证明 `G₁(π)` 为实数，结合 `|G₁|=p` 只需得 `γ₁²=1=−α(π)`；不使用错误的统一 `γ₁=1`。primary CRT 的 quartic reciprocity cross factor 为 `±1`，平方后消失。这些已证输入适用于全部奇 squarefree `n`，含 inert primes。

实际 Fourier 计算使用自对偶 lattice `O` 的 convention

\[
 e_*(z)=\exp(2\pi i\Re z),\qquad
 \widehat F(\xi)=\int_{\mathbb C}F(z)e_*(-z\xi)\,dx\,dy.             \tag{1.2}
\]

这里 real bilinear pairing 是 `Re(zξ)`，没有隐含 conjugation；`O` 的 covolume 为 1。设 `G_{*,j}` 是把 `check e` 换成 `e_*` 的 Gauss sum。由于 `n` 奇、`1/2` 在 `O/n` 中可逆，变量替换给出

\[
 G_{*,j}(1,n)=\chi_n(2)^jG_j(n),\quad
 G_{*,j}(k,n)=\chi_n(k)^{-j}G_{*,j}(1,n).                         \tag{1.3}
\]

第二式对非单位 `k` 两侧均为零，因为 `χ_n^j` 在下文使用的 `j=1,2,3` 都是 primitive at every good local prime。`χ(2)` 来自 trace-2 与 Re 的转换，不是可任意去掉的 phase。

## 2. Square theta coefficient 实际提供什么

DDHL v5 (4.39) 在 squarefree primary `m`、`(m,ν)=1` 上给出

\[
 \psi_\beta(m^2\nu)=q_m^{-3/4}\overline{g_4(\nu,m)}
 \begin{cases}
 \psi_\beta(\nu),&m\equiv1\pmod4,\\
 \epsilon_\beta\psi_{\beta(1+\lambda^3)}(\nu),&m\equiv1+\lambda^3\pmod4.
 \end{cases}                                                     \tag{2.1}
\]

在 `ν=1`、固定有限 sector / cusp vector 后，square coefficient 是
`q_m^(−1/4) barγ₁(m)` 乘已知固定 sector factor。theta Fourier term 的 index 是 `m²`、其 norm 是 `q_m²`；Fourier normalization 中的 `N(m²)^(1/8)=q_m^(1/4)` 恰抵消该 quarter weight。取 conjugate 和有限 sector 线性组合，可把 root Gauss weight `γ₁(m)` 作为本稿显式 probe 的来源。

这并不把新 root-indexed series 变成原完整 theta。剥去 Bessel factor、把 full index `m²` 改读 root `m`、插入 `η(m)` 和下面的旋转窗口，是一个新 operator。若逐字在完整 index 上插入 target，只会得到 `η(m²)=η(m)²`；本稿的 root weight 选择避开了这一代数障碍，但没有自动获得任意 `η` 的新 theta functional equation。

## 3. 一个保留 target 的真实 one-hop Poisson probe

设 `W∈C_c^∞((0,∞))` 支撑在 `[1,2]`，`F∈S(C)`，`X,H>0`。`H` 表示物理 additive averaging 的 norm scale；第 7 节 raw theorem 的 row radius另用 `U`。定义

\[
 c(n)=\chi_n(2)^{-1}\gamma_1(n)\overline{\alpha(n)},
\]

\[
 \mathcal P_\eta(X,H;W,F)=
 \sum_n^{\mathrm{sf}}
 \frac{\eta(n)c(n)}{\sqrt{q_n}}W(q_n/X)
 \sum_{h\in O}\chi_n(h)
 F\!\left(\overline{\alpha(n)}h/\sqrt H\right).                  \tag{3.1}
\]

`η` 是同一个任意 finite-order ray target，按固定坏素数零延拓。其 modulus 只影响外系数 / 固定 support；这里不假设新 conductor FE。外 `n` 和内 `h` 的 sums 都是真实 sums：外和有限，内和 Schwartz 绝对收敛。若要求完全有限的物理近似，在后续实际使用的 `H=X≥2` 范围，可在 `N h≤H X^(2δ)` 截断，并由固定 Schwartz seminorm 使绝对尾项小于任意指定 `X^(−A)`（支付依赖 `A,δ` 的有限 seminorm）。未限制的超多项式 `H` 不包含在此尾项声称中；精确恒等式采用全 Schwartz 和，对全部 `X,H>0` 有效。

对任意 `|β|=1`，分 residue classes 和 lattice Poisson 给出

\[
 \sum_h\chi_n(h)F(\beta h/\sqrt H)
 =\frac H{q_n}\sum_kG_{*,1}(k,n)
       \widehat F\!\left(\frac{\sqrt H k}{\beta n}\right).          \tag{3.2}
\]

这是 `Re(zw)` pairing 的真实配对；在取 residue `a+nℓ` 时，dual lattice 为 `k/n`，缩放 / 旋转的 Jacobian 为 `H`。取 `β=barα(n)` 后 `βn=|n|`，从而 (1.1)–(1.3) 给出精确式

\[
 \boxed{\mathcal P_\eta(X,H;W,F)=
 H\sum_n^{\mathrm{sf}}\frac{\mu(n)\eta(n)}{q_n}W(q_n/X)
 \sum_k\chi_n(k)^{-1}
 \widehat F\!\left(\sqrt{H/q_n}\,k\right).}                     \tag{3.3}
\]

`χ_n(2)^(−1)` 与 (1.3) 的 `χ_n(2)` 精确抵消，`γ₁² barα=μ`。`η(n)` 没有被平方；全部 zero masks 仍在式内。若同时外乘 `χ_n(u)^ε`，(3.3) 仍对每个真实 row `u` 成立，非互素 row 自动被零延拓。故 probe 可以定义同一 target 的 inverse family，而不是只定义一个 untwisted Möbius sum。

## 4. 固定旋转窗口恰隔离 unit dual，包含两个端点

取 `H=X`，令 `I=[1/√2,1]⊂R⊂C`。对 `q_n∈[X,2X]`，
`t=√(X/q_n)` 属于闭区间 `I`。对所有 `k∈Z[i]`, `k≠1`，有

\[
                           \operatorname{dist}(tk,I)\ge\sqrt2-1.  \tag{4.1}
\]

证明逐 lattice 类别如下：若 `Im k≠0`，其 imaginary distance 至少 `1/√2`；若 `k` 是实整数且 `k≥2`，则 `tk≥√2`；若 `k≤0`，与 `I` 的距离至少 `1/√2`。三类穷尽全部 `k≠1`，尤其包括另外三个 Gaussian units 和 `k=0`。

选一个固定 `\widehat F∈C_c^∞(C)`，在 `I` 的邻域恒为 1，支撑在距 `I` 小于 `δ=1/4` 的 tube 内。其 inverse Fourier transform 是一个固定 Schwartz `F`，且 `δ<√2−1`。于是包括 `q_n=X` 与 `q_n=2X` 两端点，

\[
 \sum_k\chi_n(k)^{-1}\widehat F(tk)=1.
\]

因此

\[
 \mathcal P_\eta(X,X;W,F)=X\sum_n^{\mathrm{sf}}
                     \frac{\mu(n)\eta(n)}{q_n}W(q_n/X).          \tag{4.2}
\]

写 `W(t)=tV(t)`，得到同一任意 target 的精确 identity

\[
                  \mathcal P_\eta(X,X;tV,F)=
                  \sum_n^{\mathrm{sf}}\mu(n)\eta(n)V(q_n/X).   \tag{4.3}
\]

这比一个 formal signal 更具体：固定 Schwartz window、物理 norm scale、所有 lattice dual 和 endpoints 都已付款。不过 `F` 通常复值、非 radial；原 positive radial profile theorem 不能直接读作 (3.1)。式 (4.3) 是重写，不是对任意 `η` 的 Möbius saving。

## 5. 物理 n-window 的 angular / Mellin 成本与实际反射长度

把 `F(re^{iθ})=Σ_ℓ f_ℓ(r)e^{iℓθ}` 展开，则

\[
 F(\overline{\alpha(n)}h/\sqrt H)=
 \sum_{\ell\in\mathbb Z}f_\ell(|h|/\sqrt H)
                          \alpha(h)^\ell\alpha(n)^{-\ell}.      \tag{5.1}
\]

乘外 `barα(n)` 后，`n` Dirichlet series 实际 angular parameter 是 `ℓ+1`。这是方向依赖的准确展开；不能略去后把径向 `n` theorem套上。外 `W(q_n/X)` 的 Mellin transform 控制 norm / height；任意固定 height twist `q_n^(it)` 的 modulus 为 1。`F` 的 angular coefficients 对 `ℓ` 快速衰减，但应用 reflected estimates仍需它们对 `ℓ` 与 Mellin height 的 polynomial uniformity和可求和的固定 seminorm。一般 `η` 还需新的 finite-conductor / cusp completion，未由 (5.1) 自动证明。

在正向 physical row 中，

\[
 \chi_n(2)^{-1}\chi_n(h)=\chi_n(2h^3)^{-1};                     \tag{5.2}
\]

故 DDHL Gauss Dirichlet series 的实际 numerator 是 `ν=2h³`，不是 `h`。对正 incoming row `χ_n(u)`，它是 `ν=2(uh)³`；对负 incoming row `χ_n(u)^(−1)`，同一个正向 physical hop 则给 `ν=2h³u`。两者都是奇 quartic row，固定 2-part 不能使 odd local exponent变成 quadratic。下文 `2(uh)³` 的专门示例均指正 incoming row；一般 valuation table适用于两种符号。

以 normalized series `\widetilde\psi(s,ν,ℓ)=Σ_c g₄(ν,c)q_c^(−1/2)α(c)^(−ℓ)q_c^(−s)` 记，DDHL 的已知 completion含 `ζ_{K,λ}(4s−1,ℓ)`、三个 complex gamma factors
`Γ_C(s+|ℓ|/2−1/4), Γ_C(s+|ℓ|/2), Γ_C(s+|ℓ|/2+1/4)`，和 24-cusp rational matrix。它反射 `s↦1−s, ℓ↦−ℓ`，带 `Nν^(1/2−s)α(ν)^(−ℓ)`；angular phase虽为单位模，不能从完整 FE 中省略。这说明在固定 height 下，长度 `X` 的未加任意新 finite target 的 `n` 和，dual norm length 约为

\[
                           N\nu/X\asymp q_h^3/X.               \tag{5.3}
\]

在窗口 `H=X` 的典型 physical range `q_h≈X`，它约为 `X²`。带正 incoming row `u` 时约为 `q_h³q_u³/X`，带负 incoming row时约为 `q_h³q_u/X`。这是实际长 dual，不能把 (4.3) 解释成已付的短反射。这里尚未改 physical hop的符号，也不声称两个 incoming signs都有后一个较短 `u`-aspect。

已知 `ψβ(m³ν)=0`（奇 squarefree `m≠1,(m,ν)=1`）确实给出一个具体可用消失项：`h` 为奇 squarefree非单位时，numerator `2h³` 的 theta residue 为零。若 `h` 含 `λ`，只可对其非平凡 odd squarefree部分应用该式，ramified部分保留在 cusp数据；仅含 `λ` 的 `h` 不由此消失。但需要估计的 completed quartic Gauss remainder 与 (5.3) 仍存在。单位、powerful `h` 和 incoming row `u` 都不能免费按同一消失式删除。

### 5.1 按 incoming sign选择 hop，可把两种 row的 numerator降为同一个 `2h³u`

这里是一个另外已逐式核准的 physical设计，不把原 (3.1) 的正 hop费用偷偷改写。对 `j=1,3`，令 `σ₁=1,σ₃=−1`。complex conjugation和变量替换 `x↦−x` 给

\[
 \gamma_3(n)=\chi_n(-1)\overline{\gamma_1(n)},\qquad
 \gamma_j(n)^2=\mu(n)\alpha(n)^{\sigma_j}.                       \tag{5.4}
\]

取 `εχ≡−j mod4`，即 negative incoming row取 `j=1`，positive incoming row取 `j=3`。定义

\[
 c_j(n)=\chi_n(2)^{-j}\gamma_j(n)\alpha(n)^{-\sigma_j},
\]

\[
 \mathcal P_{\eta,u}^{(j)}=
 \sum_n^{\rm sf}\frac{\eta(n)c_j(n)}{\sqrt{q_n}}
     W(q_n/X)\chi_n(u)^{-j}
 \sum_h\chi_n(h)^j F(\overline{\alpha(n)}h/\sqrt H).             \tag{5.5}
\]

非互素时仍零延拓。对 `χ^j` 重做 (3.2)，用 `G_{*,j}=χ(2)^jG_j`，得到真实配对

\[
 \mathcal P_{\eta,u}^{(j)}=
 H\sum_n^{\rm sf}\frac{\mu(n)\eta(n)}{q_n}W(q_n/X)\chi_n(u)^{-j}
       \sum_k\chi_n(k)^{-j}\widehat F(\sqrt{H/q_n}k).            \tag{5.6}
\]

第 4 节的同一个固定 tube窗口、`H=X,W(t)=tV(t)` 同时给

\[
                \mathcal P_{\eta,u}^{(j)}=
                \sum_n^{\rm sf}\mu(n)\eta(n)\chi_n(u)^{\epsilon_\chi}
                                      V(q_n/X).                 \tag{5.7}
\]

由 (7.1) 的实际 `1/√q_n` norm weight要读 normalized inverse时，只需在固定 dyadic bin上把 `V` 换成含 `t^(−1/2)` 的 profile并提出 `X^(−1/2)`；不是改变 target。

另一方面，在尚未 Poisson的物理 `n` 列中，

\[
 \chi_n(2)^{-j}\chi_n(h)^j\chi_n(u)^{-j}
                  =\chi_n(2h^3u)^{-j}.                         \tag{5.8}
\]

因此两种 incoming signs都由 `G_j(2h³u,n)` 的 normalized row读出。现在 good-prime numerator valuation确为 `3vπ(h)+vπ(u)`；(6.5) 相应把每一 local exponent `L mod4` 改为 `jL mod4`，principal分支完全相同。参考 conductor `Nν=4q_h³q_u`，故 reference dual length对两种 signs都是

\[
                                q_h^3q_u/X.                     \tag{5.9}
\]

这比固定正 hop、正 incoming row的 `q_h³q_u³/X` 少付一个 `u²`。它仍有 typical `h` 的 `q_h³` 费用，并不推出新 raw / σ saving。

`j=3` 的未加任意 finite target 的 Gauss completion可以明确来自 `j=1`：对同一个 numerator `ν`，`G₃(ν,c)=χ_c(−1) overline{G₁(ν,c)}`；固定 mod4 sectors后 `χ_c(−1)` 是有限已知 sign，系数 conjugation、`s↦bar s` 与 angular parameter翻转给 conjugate 24-cusp matrix，norm conductor仍是同一个 `Nν`。实际 angular expansion的 `n` 参数是 `ℓ+σ_j`，ramified 2-part / residue cases仍保留。这里仅记录这个可核的 untwisted conjugate接口；任意 `η`、其有限 conductor和所有 uniform profiles的 completion仍是新输入。

## 6. 逐 good-prime 的 modulus / numerator 计算

### 6.1 Full square-index 加 quartic residue twist

固定 good Gaussian prime `π`，`q=Nπ`，unit numerator `κ`，`χ=χπ`。若完整 theta index 是 `π²`，原角色是 `χ²`；再乘 `χ(h)^a`，实际 local exponent是 `e=2+a mod4`。定义

\[
 S_a(\nu)=\sum_{h\bmod\pi^2}\chi(h)^e e_*(\nu h/\pi^2),
                  \qquad \nu=\pi^v\kappa .                    \tag{6.1}
\]

对四个 `a`，非单位 `h` 都取零。按 `h=h₀+πy` 的 lift orthogonality 计算：

| numerator valuation | `e=1,2,3` | `e=0`（单位上的 principal，仍零延拓） |
|---|---|---|
| `v=0` | `0` | `0` |
| `v=1` | `q χ(κ)^(−e) G_{*,e}(1,π)` | `−q` |
| `v≥2` | `0` | `q(q−1)` |

所以 `a=0` 只在 valuation 1 产生 quadratic Gauss；`a=1` 产生 conjugate quartic；`a=2` 是 Ramanujan 分支；`a=3` 才产生所需 `G₁`。对 squarefree `n`，最后一项就是

\[
 \sum_{h\bmod n^2}\chi_n(h)e_*(\nu h/n^2)=
 \begin{cases}q_nG_{*,1}(k,n),&\nu=nk,\\0,&n\nmid\nu.
 \end{cases}                                                     \tag{6.2}
\]

故 twist 的成功分支使有效 modulus 降回 `n`：Poisson 时 `ν=nk`，dual `q_k≈q_n/H`，不是 `q_n²/H`。它精确恢复第 3 节 one-hop physical probe；没有产生一个保持完整 square-index automorphy的新 reflection。

一般 local modulus `π^L`、nonprincipal exponent `e=1,2,3` 的 character conductor 仍仅 `π`，非零 Gauss sum要求 `vπ(ν)=L−1`，结果为

\[
                      q^{L-1}\chi(\kappa)^{-e}G_{*,e}(1,\pi).   \tag{6.3}
\]

完整 index `π^(2+4b)` 或改变 averaging modulus，不能仅凭 tame quartic residue twist把 conductor提升到 `π^(2+4b)`。该指定候选的 valuation obstruction 已逐 good-prime 完整描述。

### 6.2 Natural square-map average 不是所需 odd-row reflector

另一个具体候选是

\[
 A_j(x)=q^{-1/2}\sum_{y\in( O/\pi)^*}\chi(y)^j e_*(xy^2/\pi),
                          \quad j\text{ odd}.                 \tag{6.4}
\]

若 `χ(−1)=−1`，配对 `y,−y` 使它恒为零。degree-one `q≡5 mod8` 已给出这一整类 obstruction。若 `q≡1 mod8`，选有限 residue field 上 `χ₈²=χ`，则 square pushforward是

\[
 \sum_{y^2=v}\chi(y)^j=\chi_8(v)^j+\chi_8(v)^{j+4}.
\]

其 Fourier 是两个 order-eight Gauss rows。对 `j=1`，乘原 quartic incoming factor `χ^(−1)=χ₈^(−2)` 后的角色指数是 `−3,−7`，仍 order eight。这个指定 natural square-map candidate在一类 primes 消失，另一类引入 order eight；没有终端 quadratic row。此结论不排除其它新 operator。

### 6.3 实际 odd numerator `2(uh)³` 的所有 local branches

这给出对 powerful rows也有效的明确计算。设 `k=vπ(ν)≥0`、`ν=π^kκ`。对于 DDHL unnormalized `g₄(ν,π^L)`（fixed good prime），当 `L≥1`：

\[
 g_4(\nu,\pi^L)=
 \begin{cases}
 q^k\chi(\kappa)^{-e}G_e(1,\pi),&L=k+1,\quad e=L\bmod4,\\
 \varphi(\pi^L),&L\le k,\quad 4\mid L,\\
 0,&\text{otherwise}.
 \end{cases}                                                     \tag{6.5}
\]

在第一行 `e=0` 用单位 residue class 的 `G₀=−1`；`L=0` 的局部项是 1。这是 lift orthogonality和 nonprincipal / principal conductor的完整区分，不假设 numerator squarefree。正 incoming row的 `ν=2(uh)³` 给 `k=3vπ(uh)`；负 incoming row的 `ν=2h³u` 给 `k=3vπ(h)+vπ(u)`，均直接代入 (6.5)。以下表格专列正 row，例如：

| `vπ(uh)` | 非零的 `L>0` 分支 |
|---|---|
| `0` | `L=1`, `G₁` |
| `1` | `L=4`, `−q³` |
| `2` | `L=4`, `φ(π⁴)`；`L=7`, `q⁶χ(κ)^(−3)G₃` |
| `3` | `L=4,8`, `φ(π^L)`；`L=10`, `q⁹χ(κ)^(−2)G₂` |

当 `h≠0` squarefree、`u=1` 时，只有 `h` 的 odd local primes 可取 `L=4`，其它 good primes只可取 `L=1`；modulus `c` 一直是 odd primary。CRT 因 `π⁴` 是 fourth power而无新 quartic cross factor，于是 normalized all-modulus Gauss DS 有准确 factorization

\[
 \widetilde\psi(s,2h^3,\ell)=
 \prod_{\substack{\pi\mid h\\\pi\nmid\lambda}}\left(1-q_\pi^{1-4s}\alpha(\pi)^{-4\ell}\right)
 D_{\rm sf}(s;h,\ell),                                         \tag{6.6}
\]

其中 product只取 good odd primes，`λ` 不产生 modulus `L=4` 列；`h` 的 ramified部分由 numerator / cusp数据保留。`X≥2` 时 physical `h=0` 项为0，不进入该 Dirichlet series。`D_sf` 的列 `c` odd squarefree且 `(c,h)=1`，系数为
`γ₁(c)χ_c(2)^(−1)χ_c(h)α(c)^(−ℓ)`。若 formal 系数另带 `η(c)`，相同直接 CRT 计算把乘积内改成
`1−η(π)^4 qπ^(1−4s)απ^(−4ℓ)`。乘 DDHL completion 的 zeta / 相应 formal `L(4s−1,η⁴,4ℓ)` 只会引入额外 fourth-power列；它不把 surviving squarefree `χ_c(h)` 变成 quadratic。一般 target 的 completed FE仍是新输入，不能从这个系数恒等式推出。

## 7. 可独立证明的真实 raw inverse × once-prime 窄二矩

下面不是抽象缺口，而是一个已有完整证明的新 narrow input。其 orientation与固定源 9225–9248 相同。

固定 slot 数 `k₀≥0` 和 mutually disjoint odd Gaussian prime sets `P_i`，都避开固定 `S`（含 `λ`），并取各理想的唯一 primary generator；`D,P_i≥1`，`Np∈[P_i,2P_i]`。取固定 smooth profiles `w,w_i`，均支撑在 `[1,2]`；因此每个 inverse index满足 `Nn∈[D,2D]`。`η` 任意有限阶 target、零延拓，`|η|≤1`。取同一个 `εχ∈{1,−1}`，定义

\[
 M_u=\sum_n^{\rm sf}\frac{\mu(n)\eta(n)}{\sqrt{q_n}}
                     w(q_n/D)\chi_n(u)^{\epsilon_\chi},
\]

\[
 Q_{i,u}=\sum_{p\in P_i}\frac{a_i(p)\eta(p)}{\sqrt{q_p}}
                     w_i(q_p/P_i)\chi_p(u)^{\epsilon_\chi},
                    \quad |a_i(p)|\le A_i.                    \tag{7.1}
\]

设

\[
 T_{\rm col}=\max\{2,2^{k_0+1}D\prod_i P_i\}.
\]

每个实际 expanded column `m=n∏p_i` 都满足 `Nm≤T_col`。固定源的 `D^(−1/2)W(q_n/D)` 与这里的 `q_n^(−1/2)w(q_n/D)` 完全等价（令 `w(t)=√tW(t)`）；slots同理。若 once-slot 用 `log Np/√Np`，则取 `A_i≲log(2P_i)`；若要求 source bounded coefficient，把它除以 `log(2P_i)`。因此 log weight费用明确是 `∏A_i²`，可吸进任意 `T_col^ε`。固定 imaginary height factor modulus为1；固定 real `s` 所产生的 dyadic norm power可单独提出相应确定的 `D,P_i` 次幂，不能伪装成新的 saving。

**定理。** 对所有 `U≥1`，所有真实 rows `u∈O,0<Nu≤U`，任意 `η` 和 (7.1) 的 coefficients，

\[
 \boxed{\sum_{0<q_u\le U}\left|M_u\prod_iQ_{i,u}\right|^2
 \ll_{\epsilon,k_0,w,w_i}
 (U+T_{\rm col}^2)(UT_{\rm col})^\epsilon\prod_i A_i^2.}          \tag{7.2}
\]

这里允许 inverse index `n` 与 slot primes 重叠；角色的全部 zero masks保留。证明只用 `|η|≤1`、有限角色和 additive Poisson，不需要新 target FE或 uniform conductor theorem。

### 7.1 Expanded columns、overlap 和 coefficient energy

按真实乘积 `m=n∏p_i` 合并多种 decomposition，写系数为 `A_m`。每个 local prime exponent为 1或2：inverse `n` squarefree，slot sets disjoint，同一个 prime至多出现在一个 slot。当它同时出现在 `n` 与一个 slot时，角色指数是 `2εχ`，即 primitive nonprincipal quadratic；否则是 `εχ`，即 primitive quartic。

故角色的 good-prime conductor是

\[
                         c=\operatorname{rad}(m),               \tag{7.3}
\]

不是 `m` 本身。`εχ=1` 的 local exponent是 1/2；`εχ=−1` 是3/2。不同 `m` 给不同 conductor或至少一个不同 local character；primitive local characters在 independent CRT factors上区别，因此 `m↦χ_m^{εχ}` 是注入。对于同一个 `m`，不同 decomposition确会发生；不能假设没有。

固定 `k₀` 时 decomposition multiplicity至多 `d(m)^{k₀+1}≪_ε T_col^ε`。先对每个 `A_m` 用 Cauchy，再按实际 product indices求和，得

\[
 \sum_m|A_m|^2
 \ll_\epsilon T_{\rm col}^\epsilon\prod_i A_i^2.                \tag{7.4}
\]

这里 `Σ_{n≈D}1/Nn≪1` 与每个 `Σ_{p≈P_i}1/Np≪1` 用 Gaussian ideal lattice count即可，不需要 PNT。`η(n)∏η(p_i)=η(m)`，包括 fixed zero exclusions；重叠项 `m` 中的 `p²` 已被保留，绝未删除。

**共同符号是本 primitive proof的实质前件。** 若 inverse用 `χ_n^(−1)` 而 slot用 `χ_p`，`n=p` 的 local指数变成0，产生 `1_(u,p)=1` 的 principal row和降导子；不同 `p` 成为近重复函数。若这些 overlap项的真实 coefficients是 `b_p`，large-row coherent energy约为 `U|Σ_p b_p|²`，而 individual coefficient energy是 `Σ_p|b_p|²`。在 (7.1) 的 normalized `D≈P`、`b_p≈1/D` 情形，前者约为 `U(#p/D)²`，比 individual energy乘 `U` 多 `#p`。same-conductor primitive orthogonality不能直接处理该降导子 family。不过此例本身没有反证 (7.2) 的最终粗预算，因为 normalized coherent项仍可在 `U` 量级以内。mixed-sign theorem未在本稿证明；固定原源合同确实是共同符号。

### 7.2 同 conductor 先正交，再 Gauss 展开

令 `χ` 为 conductor `c` 的 primitive character。以 (1.2) 的 `e_*` 定义 normalized `τ_{barχ}`，`|τ_{barχ}|=1`。对全部 `u`，包括 `(u,c)≠1`，有限 Gauss identity是

\[
 \chi(u)=\frac1{\sqrt{Nc}\,\tau_{\bar\chi}}
       \sum_{a\in(O/c)^*}\bar\chi(a)e_*(au/c).                  \tag{7.5}
\]

primitive character的 Gauss sum在非单位 numerator上正是0，故零掩码没有丢失。先固定同一个 conductor `c`，把实际 coefficients `A_χ` 合并进

\[
 B(c,a)=\frac1{\sqrt{Nc}}
       \sum_{\chi:\,\operatorname{cond}\chi=c}
                      A_\chi\tau_{\bar\chi}^{-1}\bar\chi(a).
\]

不同 primitive characters在 `(O/c)^*` 上正交，给出

\[
 \sum_{a\in(O/c)^*}|B(c,a)|^2
       =\frac{\varphi(c)}{Nc}\sum_{\chi:\operatorname{cond}\chi=c}|A_\chi|^2
       \le\sum_{\chi:\operatorname{cond}\chi=c}|A_\chi|^2.        \tag{7.6}
\]

这是关键：没有先对 individual `τ` 做 ℓ¹相加，也没有把同 radical的多个 primitive characters付成额外 multiplicity。结合 (7.4)，全部 additive coefficients的 ℓ²能量已付款。

### 7.3 Reduced fractions和二维 positive Schur proof

把 `a/c` 视作 `C/O` 上频率，`(a,c)=1`，`Nc≤T_col`。不同 primary conductor和 reduced numerator给出不同 torus fraction；若两个 frequency差不是 lattice点，Gaussian integer numerator非零，故

\[
 \operatorname{dist}(a/c-a'/c',O)\ge1/(|c c'|)\ge1/T_{\rm col}.  \tag{7.7}
\]

此处 prime ideals已通过 primary generators处理；不把未处理的 unit associates当成新 columns。配对仍是 `Re(uξ)`。若使用 DDHL trace-2 convention，则频率是 `2a/c`；因 `c` 奇，仍是 reduced fraction和相同量级 separation，只需固定常数。

以下给出完整 positive-kernel Schur证明，而不是无引用 packing assertion。令 `g_U(u)=exp(−|u|²/U)`，在 disk `Nu≤U` 上至少 `e^(−1)`。二维 lattice Poisson给出

\[
 \sum_{u\in O}g_U(u)e_*(u\delta)
      =\pi U\sum_{v\in O}\exp(-\pi^2U|v-\delta|^2).             \tag{7.8}
\]

右侧非负。将 `Σξ Bξe_*(uξ)` 的平方乘 `g_U` 后展开，其 Hermitian kernel就是 (7.8)。对固定 `ξ`，所有 lifted points `ξ'+v` 以 `δ₀≥1/T_col` 分离。以每点为中心放半径 `δ₀/3` 的 disjoint disks。一个半径 `r` 的 disk能包含的点数至多

\[
                               C(1+r/\delta_0)^2,              \tag{7.9}
\]

因为这些 disjoint disks包含在半径 `r+δ₀/3` 的 disk中，比较面积即可。把径向 Gaussian分层积分或 annuli求和，(7.9) 给出

\[
 \sum_{\xi',v}e^{-\pi^2U|v+\xi'-\xi|^2}
       \le C\left(1+\frac1{U\delta_0^2}\right).                \tag{7.10}
\]

例如用积分 `Σ e^(−aUr²)=∫₀^∞ 2aUr e^(−aUr²) #\{|point|≤r\}dr`，展开 `(1+r/δ₀)²`，并以 `x≤1+x²` 吸收中项，即得 (7.10)。Schur row sum乘 `πU` 后至多 `C(U+T_col²)`。于是

\[
 \sum_{q_u\le U}\left|\sum_\xi B_\xi e_*(u\xi)\right|^2
       \ll (U+T_{\rm col}^2)\sum_\xi|B_\xi|^2.                 \tag{7.11}
\]

这是 positive Gaussian Schur majorant；不需要声称 Gaussian compact bandlimited。若希望 compact Fourier-support形式，也可在 radius `\asymp\min(T_col^{-1},U^{-1/2})` 选 smooth nonnegative Fourier bump，取其 inverse transform平方作非负 bandlimited majorant，缩放使它在 `|u|≤√U` 为正；Fourier support小于 separation后 Poisson使 off-diagonal消失，total mass `≪U+T_col²`。本稿的证明实际使用 (7.8)–(7.10)，无需这个替代构造。

联用 (7.4)、(7.6)、(7.11) 就得到 (7.2)，包括所有 zero masks和所有允许 overlaps。

### 7.4 Reciprocity方向与 fixed 2-part

(7.2) 直接证明的是 `χ_n(u)` 方向，它本身就是固定源的 `ψ_u(n)=ν(n)χ_n(u)^εχ`，无需把 row `u` 先取为 prime或 primary。若要重写成 `χ_u(n)` 以和另一 Hecke / ideal notation比较，只能在互素时用 quartic reciprocity，并固定有限 mod4 / unit sectors。其 sign是有限 sector matrix，可在固定 sector吸进 coefficients；非互素处两方向保持真实零延拓。由此引入的 conductor 2-part是固定的，只使 (7.7) 的 `T_col` 乘固定常数。不能把此有限处理省略后称所有 ideal representatives已付款；也不需要它来证明本稿直接方向的 (7.2)。

## 8. 此结果实际支付什么，哪里仍未闭合

无 slots时 `T_col≈D`，(7.2) 给

\[
             \sum_{0<Nu\le U}|M_u|^2\ll(U+D^2)(UD)^\epsilon.   \tag{8.1}
\]

所以 `U≥D²` 是一个真实 raw `O_ε(U^(1+ε))` 窄前件（重命名任意小幂 `ε`），任意 finite target、固定 heights和zero masks均保留；有slots时对应 `U≥(D∏P_i)²`。它不只证明 Möbius rewrite，因为其真实 rows、inverse coefficients、prime-slot product和 column energy都已估计。

固定源 12343–12360 则要求每个固定 `c>0`，在 `U≥D^(1+c)` 即有同量级 raw bound。`D^(1+c)≤U≪D²`（`0<c<1`）仍未付款。不能把新 theorem当作原前件或原 marked fine budgets的替代。

若仅把 (8.1) 放进 order-four amplification，代价的 formal envelope是
`max{1,1/4+(3/2)r}`，而理想 quartic版本会需要
`max{1,1/4+(3/4)r}`；斜率多一倍。这没有形成比 checkpoint 457 更强的σ certificate。本稿不更新原 cubic certificate / σ。

新 probe的下一步可检验目标因而很具体：固定正 hop (3.1) 的正 incoming row为 `2(uh)³` / dual length `q_h³q_u³/D`，负 incoming row为 `2h³u` / dual length `q_h³q_u/D`；按 sign选择 hop的 (5.5) 使两种 incoming signs都为 `2h³u` / dual length `q_h³q_u/D`。对该实际 `η`、angular profile和所有局部 valuations，仍需证明能使 raw bound从 `U+D²` 降到原合同的 `O_ε(U^(1+ε))` 的 cancellation，并给出任意 finite target、uniform angular / Mellin height及zero-mask合同。已知 square coefficient与 (1.1) 足够定义 physical probe和精确 unit-dual identity；它们未支付这一 analytic estimate。扩大 averaging modulus或重复 natural square-map averaging的两个指定候选已有第 6 节局部障碍，不能无计算地视为此 saving。

## 9. 独立的有限核算记录

以下均只在内存执行，没有修改数学源或旧 script/output。

- 对 `π=−1+2i` (`q=5`) 和 `π=3+2i` (`q=13`)，枚举 `O/π²`，核查四个 effective exponents和 numerator valuation `0,1,2,≥3` 的 32 个 prime-power Gauss cases；最大 floating discrepancy约 `1.04×10^(−11)`，与 (6.1) table一致。
- 对 `q=5` 的所有 `x` 核查 (6.4) odd-row恒零；对 `q=17` 的所有 `x` 核查 two order-eight pushforward公式，共 22 cases。
- Unit isolation用 (4.1) 的解析统一距离，不以有限 samples代替所有 lattice点证明。

这些小核算只是 normalization sanity checks；(3.2)、(6.5) 和 (7.2) 的结论由正文给出的解析证明支持。
