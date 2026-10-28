# C050：Jacobi交换子、三源gap及先fixed degree推论

2026-10-28；`/root/rational_first_gate` 当前独占证明稿。已恢复 README／STATE、check→show、同 G20261027／runtime1793085111／原0c4f、C050、AE、frontier／summary。当前执行的是已冻结 C050，非旧概率平均任务或C049续算。本稿不web／查source／数值，不改 STATE／Git／cadence。第1–4节支付本腿；第5节显式使用另一腿的全线norm／tail与physical frame结论，在root对齐消费前保持conditional。draft不代root结果或计轮。

## 1. 冻结尺度、辅助measure与Euler曲率

沿合同固定 `ℓ=logX、A=√X/ℓ、N=⌊cA/ℓ⌋`，c为旧ALLpoly门允许的一个固定小正常数；以下均只需充分大X，不改c／H₀／源。记

\[
 D_{E,X}(t)=\prod_{p\le X}(1-p^{-1/2-it}),\quad
 w_X(t)=|D_{E,X}(t)|^2,\quad
 d\mu_X(t)=w_X(t)e^{-t^2}\frac{dt}{2\pi}=e^{-V_X(t)}\frac{dt}{2\pi},
 \quad V_X=t^2-\log w_X.
\]

μ_X只是辅助多项式norm。Gaussian不是Sonin向量或新physical正Weil族；实际向量始终保 `D_(E,X)pH₀`。finite X 的 w_X 为严格正、偶、光滑函数，原finite Euler乘子上下有界，所以μ_X与Gaussian逐fixed-X可比，全部moments有限，且任意非零多项式norm严格正。

对单个 `q=p^(−1/2)、l_p=logp`，绝对一致收敛的Fourier级数给

\[
 \log|1-qe^{-il_pt}|^2=-2\sum_{k\ge1}\frac{q^k}{k}\cos(kl_pt),
\quad
 \left|\frac{d^2}{dt^2}\log|1-qe^{-il_pt}|^2\right|
 \le2l_p^2\frac q{(1-q)^2}.
\]

于是

\[
 |V_X''(t)|\le2+2\sum_{p\le X}(\log p)^2
                  \frac{p^{-1/2}}{(1-p^{-1/2})^2}.
 \tag{1}
\]

分母以p≥2的固定正常数控制。只用Chebyshev的 `θ(y)=Σ_(p≤y)logp≤Cθ y`，分部求和得

\[
 \sum_{p\le X}\frac{\log p}{\sqrt p}
 =\frac{\theta(X)}{\sqrt X}
  +\frac12\int_{2}^{X}\frac{\theta(y)}{y^{3/2}}dy
 \le C\sqrt X.
\]

再用 `logp≤ℓ`，得到一个固定常数 C_Λ，使可选

\[
 \Lambda_X=C_\Lambda\sqrt X\log X=C_\Lambda A\ell^2,
 \qquad |V_X''|\le\Lambda_X.
 \tag{2}
\]

可将C_Λ一次放大以令 `N/(2Λ_X)≤1`，不作常数或零自由区优化。V_X′在实线为 `2t` 加一个逐fixed-X有界的光滑周期和，所以 `|V_X′(t)|≤2|t|+C_X`。这也支付下节所有乘法域与IBP可积性。

## 2. 无抽象operator-Lipschitz前件的Jacobi lower

令p_n为L²(μ_X)中的实orthonormal多项式，leading coefficient正。even measure给 `p_n(−t)=(−1)^n p_n(t)`，三项递推为

\[
 tp_n=a_{n+1}p_{n+1}+a_np_{n-1},\qquad
 a_n>0\ (n\ge1),\quad a_0=0,\quad p_{-1}=0.
 \tag{3}
\]

下文暂略X下标。若κ_n为leading coefficient，递推给 `a_n=κ_(n−1)/κ_n`。对n≥1，在[−T,T]做ordinary IBP再T→∞，得到

\[
 \begin{aligned}
 \langle V'p_n,p_{n-1}\rangle_{\mu}
 &=\int(p_n'p_{n-1}+p_np_{n-1}')\,d\mu\\
 &=n\frac{\kappa_n}{\kappa_{n-1}}
 =\frac n{a_n}.
 \end{aligned}\tag{4}
\]

这里 `p_(n−1)'` 的degree≤n−2而与p_n正交；p_n′在p_(n−1)上的系数为其leading coefficient比。边项是多项式乘逐fixed-X有界w_X乘e^(−T²)，趋零；V′至多线性和全部Gaussian moments保证被积项绝对可积。因此(4)未使用未付的无界算子形式操作。

令P_n为到 `span{p₀,…,p_(n−1)}` 的正交投影，finite kernel

\[
 K_n(t,s)=\sum_{j<n}p_j(t)p_j(s).
\]

对实f=t或f=V′，每个fp_j都在L²(μ)。因此M_fP_n是定义于全H的bounded finite-rank算子，P_nM_f在原乘法域上的限制延拓为其bounded adjoint。两者之差的延拓有L²(μ×μ)核

\[
 (f(t)-f(s))K_n(t,s).
\]

核的L²可积性也可逐finite sum由 `fp_j∈L²` 直接核实；此处不需全无界乘法算子的operator-norm Lipschitz定理。由(2)的点态均值定理，

\[
 \|[M_{V'},P_n]\|_{HS}^2
 \le\Lambda_X^2\iint|t-s|^2|K_n(t,s)|^2d\mu(t)d\mu(s)
 =\Lambda_X^2\|[M_t,P_n]\|_{HS}^2.
 \tag{5}
\]

由(3)，t的commutator仅跨过degree n−1／n的一条edge，所以

\[
 [M_t,P_n]
 =a_n(|p_n\rangle\langle p_{n-1}|-|p_{n-1}\rangle\langle p_n|),
 \quad\|[M_t,P_n]\|_{HS}^2=2a_n^2.
\]

另一方面，(4)使 `[M_(V′),P_n]` 在这两个相反matrix entries的绝对值均为n/a_n，故其HS norm平方至少 `2n²/a_n²`。代入(5)即得对所有n≥1的本腿结论

\[
 \boxed{a_n^2\ge n/\Lambda_X.}\tag{6}
\]

这一步不假设V凸，也不要求V′作为bounded multiplier；支付的是finite polynomial projection两边的实际HS域。

## 3. 明列另一腿输入：统一Jacobi upper

以下conditional使用[另一独占证明腿](gaussian-trial-norm-and-physical-transport.md)的结论U：存在不依X的C₀≥1，使

\[
 a_n^2\le C_0\qquad(1\le n\le N+1).
 \tag{U}
\]

它不能从(6)或旧scalar585推得。另一腿所申报的支付方式为：在μ_X下，对deg≤N+2的全部complex多项式有统一t²weighted全线tail；因而 `∫t²|p_j|²dμ_X≤δ²+o(1)≤C₀`。由(3)该积分等于 `a_j²+a_(j+1)²`，取得(U)需要的全部indices。该tail／norm证明须由root实际对齐，而非本稿假称Gaussian bound已属于旧actual Sonin lower。

## 4. ALLcomplex二次source polynomial的共同gap

取任意complex a,b,c，令

\[
 P(t)=a+ibt-ct^2.
\]

取整数j在 `J_N={ceil(N/2),…,N−1}`。对充分大N，(6)、(U)均适用于j、j+1、j+2，且所有这些j对应的最大index为N+1。置 `h=N/(2Λ_X)≤1`、`d_j=a_j²+a_(j+1)²≤2C₀`。实际投影分别为

\[
 \langle Pp_j,p_j\rangle=a-cd_j,\quad
 \langle Pp_j,p_{j+1}\rangle=ib\,a_{j+1},\quad
 \langle Pp_j,p_{j+2}\rangle=-c\,a_{j+1}a_{j+2}.
\]

parity使这些投影没有来自其它degree的交叉项；三个basis向量互相正交，a,b,c可独立complex。因此

\[
 \|Pp_j\|_\mu^2
 \ge|a-cd_j|^2+h|b|^2+h^2|c|^2.
 \tag{7}
\]

若 `|a|≥4C₀|c|`，第一项≥|a|²/4；若相反，`|a|²≤16C₀²|c|²`，最后一项控制a、c两系数。两种情形都给一个固定γ>0（只依C₀），使

\[
 \|Pp_j\|_\mu^2\ge\gamma h^2(|a|^2+|b|^2+|c|^2).
\]

求和j∈J_N，得到

\[
 \boxed{\sum_{j<N}\|Pp_j\|_\mu^2
 \ge c_2\frac{N^3}{\Lambda_X^2}
              (|a|^2+|b|^2+|c|^2)
 \ge c'_2\frac{\sqrt X}{(\log X)^8}
              (|a|^2+|b|^2+|c|^2).}\tag{8}
\]

N的floor只使充分大X后 `N≥(c/2)√X/ℓ²`。此处是同一个fixed三维源空间的ALLcomplex系数共同估计，系数可随X变；从未给585输入一个moving source去交换其起点／常数。

## 5. 条件运输到actual三源moment／完整K／rank2

本节不把μ_X的p_j当成Sonin向量。使用另一腿的明确输入T：

1. 对所有deg q≤N+2，真实trial norm `||q||²_H=∫w_X|H₀|²|q|²dt/(2π)` 与μ_X norm满足 `c_H||q||²_μ≤||q||²_H≤C_H||q||²_μ`，常数固定；两边的全部全线tails已付。
2. fixed δ>0满足 `|F₀(t)|≥h_δ>0` 于|t|≤δ，且对deg q≤N+2，H-norm的core至少为固定比例总norm，故 `∫|F₀q|²w_X|H₀|²dt/(2π)≥c_T||q||²_μ`，c_T>0不依q／X。
3. 实际 `v_j=D_(E,X)H₀p_j∈RanΠ_X`；其finite Gram H_M在任一所用initial segment有 `c_H I≤H_M≤C_H I`，实际orthogonal frame projection为 `Q_M=V H_M⁻¹V*≤Π_X`。

这些条件所需degree未超合同：j<N及degP≤2给deg(Pp_j)≤N+1。源 `r=a r₀+b r₁+c r₂` 的Fourier为F₀P；原physical A_r在Mellin侧乘F₀P。ordinary trace／HS域由560／585保持，所以

\[
 \begin{aligned}
 t_X(r)&\ge\operatorname{Tr}(A_rQ_MA_r^*)\\
 &=\operatorname{Tr}\bigl(H_M^{-1}[\langle A_rv_j,A_rv_i\rangle]_{i,j}\bigr)\\
 &\ge C_H^{-1}\sum_{j<N}\|A_rv_j\|^2
 \ge C_H^{-1}c_T\sum_{j<N}\|Pp_j\|_\mu^2.
 \end{aligned}\tag{9}
\]

middle matrix为PSD；最后一步正是输入T，不把nonorthogonal v_j冒作orthonormal Gaussian基。所有2π只在原physical／trial Plancherel规范中使用一次，actual `m_j=∫t^(2j)|F₀|²ρ_Xdt` 不另改ρ规范。

结合(8)，实际三源Gram满足conditional结论

\[
 G_X=\begin{pmatrix}m_0&0&-m_1\\0&m_1&0\\-m_1&0&m_2\end{pmatrix}
 \succeq c_*\frac{\sqrt X}{\ell^8}I_3.
\]

even block最小eigenvalue≥同lower，而 `𝔇_X=(m₀m₂−m₁²)/(m₀+m₂)` 在该eigenvalue的一半与本身之间。因此

\[
 \boxed{\mathfrak D_X\ge\tfrac12c_*\sqrt X/\ell^8\to+\infty.}\tag{10}
\]

fixed I=(−17/16,17/16)包含合同r₀及全部导数的support。只有X覆盖全部可见prime后，用原完整mixed式 `K_X^E=G_X+P_pole^E−Q_W^E`；Q/P均固定有限矩阵。完整Γ／FP-contact、全部Λ(p^k)=logp与两pole的正负号不删，不施pole-zero条件。减一个固定矩阵不改变(10)的共同发散lower。

任意同一源域上的共同Hermitian rank≤2补偿R_X，E₃压缩仍rank≤2，故有kernel单位向量。原fixed物理norm下的residual压缩norm因而至少是K_X^E最小eigenvalue，趋于∞，即使补偿norm无界、range移动／非局部／有signed系数。若所有fixed源residual均O_r(1)，固定九个复极化测试（r_j以及每对的r_j+r_k、r_j+i r_k）就使该3×3 residual矩阵有界，矛盾。这是conditional于U/T闭合后的actual net，非仅辅助Gaussian model结论。

## 6. 同一lemma的最强先fixed degree后果

本节不追加degree预算。先固定任一有限整数d≥0；令 `P(t)=Σ_(ℓ=0)^d c_ℓ t^ℓ`，只用j满足

\[
 \lceil N/2\rceil\le j<N-d.
\]

N充分大于d后，这样的j有≥N/3个、j≥d，而且deg(Pp_j)<N。原T的N+2范围足够，不需要N+d新norm／tail预算。

对k=0,…,d，设 `y_k=⟨Pp_j,p_(j+k)⟩`。递推(3)把 `⟨t^ℓp_j,p_(j+k)⟩` 写成length ℓ、steps ±1、从j到j+k的有限Jacobi paths。ℓ<k时为零；ℓ=k时只有全up path，其product为

\[
 A_{j,k}=\prod_{h=1}^{k}a_{j+h},\qquad A_{j,0}=1.
\]

对任意ℓ≥k、ℓ≤d的有效path，从j走到j+k必至少穿过每条edge `(j+h−1,j+h)` 一次。因此每个path product**都含**A_(j,k)，提出它后只剩ℓ−k个Jacobi factors，没有除以可能很小的a。所有访问indices在[j−d,j+d]⊂[0,N−1]；由U，剩余每factor≤√C₀，path数≤2^d。于是

\[
 y=\operatorname{diag}(A_{j,0},…,A_{j,d})\,U_jc,
\]

其中U_j是diagonal1的upper triangular矩阵，全部entries由仅依d、C₀的常数控制。其strict-upper part幂到d+1为零，所以有限几何和给 `||U_j⁻¹||≤C_d`，不依j／X；这一步没有除以任何a。

由(6)，`A_(j,k)≥h^(k/2)≥h^(d/2)`，h=N/(2Λ_X)≤1。因此

\[
 \|Pp_j\|_\mu^2\ge\sum_{k=0}^d|y_k|^2
 \ge c_d h^d\sum_{\ell=0}^d|c_\ell|^2.
\]

求和这≥N/3个j，得同一已付lemma的直接后果

\[
 \boxed{\sum_{j<N-d}\|Pp_j\|_\mu^2
 \ge c_dN(N/\Lambda_X)^d\|c\|_2^2
 \ge c'_d\frac{\sqrt X}{\ell^{3d+2}}\|c\|_2^2.}\tag{11}
\]

T的同一finite frame运输适用于该initial segment和所有deg(Pp_j)<N。对 `r=Σ_(ℓ≤d)z_ℓ r₀^(ℓ)`，有 `c_ℓ=i^ℓz_ℓ`，系数norm不变，因此conditional actual `(d+1)`-derivative-source trace Gram有相同lower。固定导数源线性独立：Fourier侧F₀非零，非零有限多项式不能乘F₀恒零；故其du和Dlog基Gram都固定正定，(11)换成原范数只改依d／r₀的固定常数。

再减完整固定Q/P矩阵，得到：**对每个先fixed d，任意共同Hermitian source-rank≤d的R_X，都不能使actual K_X−R_X在所有fixed compact源上有界。** 固定 `(d+1)²` 个复极化测试已足消费；R_X range、norm／符号可随X变。本结论说的是源配对的rank，不能把物理trial frame的dimension N−d误认源rank。

常数和起点允许依d，强烈保留“d先fixed”。没有d_X→∞的uniformity，没有排rank随X成长的全类，没有改 source／H₀／norm或新增degree优化轮。d=0/1与旧scalar／parity后果重合，d=2给本合同原首门(10)；本节只如实保更强同lemma有限代数后果。

## 7. 本腿终态与前件闭合记录

本腿无条件完成(1)–(6)的finite Euler曲率／Jacobi lower，条件于明确U完成(8)、(11)的共同多项式gap；条件于另一腿完整T才得(9)–(10)及actual fixed-rank net。U/T若未闭，actual 𝔇 只能报未证，不能用本稿Gaussian gap代替。根审应核另一稿的deg≤N+2全线norm、H₀ core、t²tail、finite frame inverse和实际HS域，再解除conditional。

终稿前已全文核另一腿当前12142-byte版本、LF SHA256 `1ce4ebc02ba8790d21b83642683cf910d8102802af5769f640b6dc1192603ed4`：其(EQ)/(T2)/(FRAME)/(TR)分别给本稿U/T，所用initial frame可由其N+2维frame取子空间。两稿在归一化、indices和源角色上匹配；此版本对齐不替root／fresh独立消费。第6节通过缩短j-range，只需其已给N+2，不消费另加N+d的范围。

该链使用旧ALLpoly actual域作为设施，却新增统一source coefficient的spread估计；不从三个scalar lower偷换量词。辅助commutator／有限代数不分别计轮，整个C050仅root统一结算一次。whole542＋555→557 leading4/5仍只负惯性UPPER；primitive/principal/mixed、完整Q正号、全core/cross及Ξ不由此闭合。更强的每fixed rank后果也不complete长期Goal。本稿无STATE／Git／cadence操作，无source/query或其它参数后继。
