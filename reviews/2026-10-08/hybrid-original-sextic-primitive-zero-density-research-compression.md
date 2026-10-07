# 原六次幂自由行的冻结高次部分、统一 AFE 与 primitive-zero raw 密度

2026-10-08。基线 2d5621dbc999e0cf313ea224b825d6d56547c45c。
只新增此研究源，不改原数学论文、451、472、旧审查或 Git。

结论是一个原域、原六次特征、原零掩码的 **raw bad-bin 计数**。
它不能由 BGL 的 squarefree-row corollary 直接推出；下面逐个冻结
powerful 部分，以原 squarefree sextic sieve 和标准 primitive AFE 重证。
在 a=7/8 得 raw 指数 7/13，原 raw 指数是 5/8；在
1/2<a≤5/6 得 8(1−a)/(7−6a)。这不是新的无零边界。
451 的实际 critical bin a≈0.694 已有最终 whole-slot/amplification
包络 2/3，新 raw 指数在那里约 0.863。第9节还证明，在原完整
δ、κ、amplitude rectangle 中，本文 raw 指数处处比最终包络大，
直接取 min 不能改善任何 actual bin。

[T/R]：本文给出相对于原 sextic squarefree sieve、标准 Hecke AFE、
原 primitive-character/logarithmic-control 输入的完整推导。
[O]：另一作者全文独审；与原 simultaneous inverse/plain witnesses 的
联合 amplification 接口；重新优化全部物理范围及 β_* bootstrap。
不把下述 auxiliary classical detector 替换成原探针，也不认证 RH、
全 Weil 正性、新 simplecritical 比例或新的 whole-family 无零边界。

## 1. 来源、对象与实际 zero implication

原数学源只读：
`E:\codex-build\math\preprints\The-Quasi-Riemann-Hypothesis-September-30-2026\build\paper.tex`。
其 UTF-8 canonical LF SHA256 为
`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`。
实读入口：4195–4390 原 presentation/ramification/zero bins；
4510–4547 simultaneous witnesses；4701–4724 sextic sieve statement 及
其后原证明；5181–5445 raw row envelope；12343–12408 marked/sup means。

外部主源是 [BGL, L-functions with n-th order twists](https://arxiv.org/pdf/1112.1650)，
Corollary 1.6、§2、§5 的 AFE 和 classical zero detector。
其 corollary 的星号限制为 squarefree ideal rows；原项目是
sixth-power-free **element** rows，不可删除这个差别。原域是
F=Q(ω)、O=Z[ω]，d_F=2、μ_6；所有 squarefree/powerful 均指理想，
不指其有理整数范数。固定 S 含 6 上方素理想和全部固定 conductor primes。
除第4节 primitive AFE 特别分出的 S-supported n_0 外，本文列理想
均位于 I(S)，保持原固定 S 和原自然零延拓。

原族为
\[
 \psi_{u,\nu,\varsigma}(n)=\nu(n)\chi_n(u)^\varsigma,
 \qquad \nu\in\Theta,\quad\varsigma\in\{-1,1\}.                 \tag{1}
\]
Θ 是固定有限组；负幂在非单位仍取原零值。ψ* 是 primitive inducing
character，L_orig 是带原自然零延拓的 L 函数。原源给出
\[
 L_{\rm orig}(s,\psi)=L(s,\psi^*)
       \prod_{\mathfrak p\in E_u}(1-\psi^*(\mathfrak p)q_p^{-s}).\tag{2}
\]
删去因子的非平凡零点仅在 Re s=0；在正实部区，实际 primitive 零点
与原 L_orig 的零点一致。不能由一个大 inverse/plain value 免费推出零点。
这里按原 a>51/100 bin 的定义，先已有一枚实际 primitive 零点
β≥a、|γ|≤3iT_1，才把该行纳入本文计数。
floor bin a=51/100 不保证有零点，仍只使用 #rows≪U。
principal inducing rows 由原 ramification 论证限于 S-supported
sixthfree 元素，数目有界；它们先移除，不能用于下面 nonprincipal AFE。

物理 dyad q_u≈U=Z^d，d 在固定紧区间；各比较常数固定。
所有最终 ε 估计均先取更小的 preliminary ε 以吸收有限 Mellin、dyadic、
Sobolev 和固定长度幂的损失；σ 可以在离1/2有固定距离的紧区间中一致。
令 C(U;σ,H) 为这些保留原行中，至少一个 presentation (1) 的 ψ*
具有 Re ρ≥σ、|Im ρ|≤H 的行数。我们只证明这个 **行数**；
无需将所有同一行零点重数改称独立行。

## 2. 冻结 powerful 部分与 conductor

唯一分解原理想为
\[
 (u)=\mathfrak s\mathfrak w\mathfrak k,
 \quad \mathfrak s\text{ supported on }S,
 \quad \mathfrak w\text{ has exponents }2,3,4,5,
 \quad \mathfrak k\text{ squarefree outside }S,
 \quad (\mathfrak w,\mathfrak k)=1.                              \tag{3}
\]
固定 s 的有限估值、unit、ν、ϛ 和 finite ray labels。取原 primary
generators，冻结 v=unit·s_gen·w_gen，于是对全部列 n 精确有
ψ_vk(n)=ν(n)χ_n(v)^ϛχ_n(k)^ϛ，包括 n 与 v 或 k 不互素时的零值。
不扩大 S 使其依赖 w；只把 (k,w)=1 当成已冻结的 row restriction。

令 q_w≈V，M≈U/V，R_w=N rad(w)≤V^(1/2)。powerful w 的数目≪V^(1/2)
（固定域的 squarefull-ideal 计数）。该层物理行本身也满足
#rows≪V^(1/2)M=U V^(−1/2)。

在 p∉S，估值 j=1,…,5 产生 order 6/gcd(6,j)>1 的 tame local
character；ν 在 p 不分歧，不能抵消。因此每个 p|wk 的 primitive
conductor exponent 恰为 1。S 内 conductor exponent 被固定阶数与
固定 ray modulus 一致限制；把其有限 local types 分层后，
\[
 Q_{\psi}=C_{\mathcal A,\text{class}}\,q_k R_w\asymp_{\mathcal A}M R_w.
                                                                    \tag{4}
\]
有限 S-data、infinity type 的常数与 moving w 无关；root numbers
只作为模1因子，不要求把它们分成有限种值。
原 presentation 和 primitive coefficients 在 S 外一致；(2) 中额外未
分歧但删去的 primes 只在固定 S 内。故临界线上的 finite-factor upper
是统一常数；更一般的原 deleted-factor lemma 也只付 U^ε。

固定 orientation 后，primitive local data 在 S 外记录 j mod 6，恢复
每个 j∈{1,…,5}；单位、S-values、Θ 和 orientation 有限。因此
physical row→primitive label 的 multiplicity≪_A1。本文实际按行求和，
即使不借这个有限 multiplicity 来改 family indexing，以下证明也成立。
不能把 all-sixthfree family 偷换成原 BGL squarefree primitive family。

唯一大筛输入是原源的 [R]：对固定于 k-sum 之前的 arbitrary coefficients，
\[
 \sum_{k\ {\mathrm{sf}},\ q_k\le M}
  \left|\sum_{n\ {\mathrm{sf}},\ q_n\le D}c_n\chi_n(k)^\varsigma\right|^2
 \ll_{S,\epsilon}(MD)^\epsilon
       [M+D+(MD)^{2/3}]\sum_n|c_n|^2.                         \tag{5}
\]
固定 row restrictions 和 coefficient support masks 允许。finite reciprocity
phases 在固定 ray classes 中成为固定 coefficient factors；不产生任意 row
coefficients。下面只用 (5)，不额外假设 twisted large sieve。

## 3. 所有列的大筛扩展：原 masks 和非 squarefree 系数

任意列理想唯一写成 n=c d²，其中 c squarefree，d 任意，二者可以共享
素理想。对每个固定 d，ψ_vk(d²) 是一个模≤1 的 row factor；取绝对值
后只剩 (k,d)=1 的固定 row restriction，以及冻结 v 的零值。
原 zero values 在此绝不替换为独立选取的 mask。

若 |a_n|≪q_n^ε，q_n∈[B,2B]，Minkowski 和 (5) 给出
\[
 \sum_k\left|\sum_{B\le q_n\le2B}a_n\psi_{vk}(n)\right|^2
 \ll_{\mathcal A,\epsilon}(UMB)^\epsilon
                  [M+B+(MB)^{2/3}]B.                         \tag{6}
\]
具体地，固定 d 后 coefficient energy≪(B/q_d²)B^ε；平方根费用分别为
√(MB)/q_d、B/q_d²、M^(1/3)B^(5/6)/q_d^(5/3)。第一项的
Σ_(q_d≤√B)q_d^−1≪log(2B)，后两项收敛，平方后给 (6)。
ν(c d²)χ_(c d²)(v) 等固定于 k 之前；row factor 不在大筛内改变 c_n。
同样的证明对临界权 q_n^−1/2 给
\[
 \sum_k\left|\sum_{q_n\le B}a_n q_n^{-1/2-it}\psi_{vk}(n)\right|^2
 \ll (UMB)^\epsilon[M+B+(MB)^{2/3}]                         \tag{7}
\]
当 a_n 是有界 dyadic profile 或其 logarithmic derivatives 时成立。
对 n=c d²，平方根三项为 √M/q_d、√B/q_d²、(MB)^(1/3)/q_d^(5/3)。
这些界对 fixed subintervals、partial sums 和 conjugate orientation 一致。

## 4. Frozen-w uniform critical second via AFE

对 |t|≤C H、H≥1，标准 primitive Hecke AFE 的两侧长度为
\[
 B\asymp (M R_w)^{1/2}(1+H)^{d_F/2}(UH)^\epsilon.              \tag{8}
\]
有限 infinity/local types 中权函数由 gamma-ratio Mellin integral 给出。
rapid tail 可截到上述 B，损失只为可任意缩小的 (UH)^ε。
将 Mellin line 放在 ε 上，Q_ψ^((ε+iz)/2) 的 moving-k 部分是
q_k^(ε/2)q_k^(iz/2)：前者在 dyad 上付 M^ε，后者是模 1 的 row factor。
它在每个 fixed-z 的绝对平方外消失；不能将它称为 arbitrary row
coefficients 后直接用 (5)。其余 Mellin kernel 的 L¹ 范数由标准
Stirling/gamma-ratio 界付 (UH)^ε。有限 Q_S 类在 (4) 已分层。

dual AFE 的 ε_ψ 是模 1 的 row factor，在取绝对平方之前提出；dual
coefficients 是 conjugate orientation 和 conjugate fixed ν。
primitive coefficients 位于 S 的部分先按 S-supported n_0 分开，
用 Minkowski 的收敛几何级数 Σq_(n_0)^−1/2−ε；其余列正是 (7) 中
的原 presentation。finite S-deletion 多项式对 |L| 有统一有界 upper。
不以 fixed ζ、Dirichlet family 或未分离的 conductor-dependent weight 替代。

于是 (7)、(8) 给完整统一估计
\[
 \sup_{|t|\le CH}\sum_{k}|L_{\rm orig}(1/2+it,\psi_{vk})|^2
 \ll_{\mathcal A,\epsilon}(UMH)^\epsilon(1+H)^{d_F/2}
             \mathcal L_w,
 \quad \mathcal L_w=M+(M R_w)^{1/2}+M R_w^{1/3}.              \tag{9}
\]
第三项确为 (M B)^(2/3)=M R_w^(1/3)·(1+H)^(d_F/3)，
不是 (M²R_w)^(1/3)。统一取高度指数 d_F/2 同时覆盖三项。
所有 implied constants 对 moving w、固定前件内的 masks、paired sextic
family、conductor 和 primitive root numbers 一致。
特别地，对每个实 t 可取 H'=1+|t| 应用 (9)，得到任意高度的
polynomial bound；没有只在原 fixed detector height 内声明该估计。

辅助 classical mollifier
\[
 M_X(s,\psi)=\sum_{q_n\le X}\mu(n)\psi(n)q_n^{-s}
\]
有 squarefree columns，(5) 直接给
\[
 \sup_{t\in\mathbb R}\sum_k|M_X(1/2+it,\psi_{vk})|^2
       \ll (UMX)^\epsilon[M+X+(MX)^{2/3}].                  \tag{10}
\]
这里 M_X 是新的计数工具；不是原 saturated inverse witness M_r，也不
改变原 D、N、W profiles、normalizer 或 simultaneous witness constraint。

## 5. Classical zero-row detector 逐层重证

固定 1/2<σ<1，常数可依其离 1/2 的固定距离。记 C_w(σ,H) 为 fixed
w/labels 层有实际 primitive zero 的 k 行数。选每行一枚 ρ=β+iγ，
β≥σ、|γ|≤H，不需要 arbitrary independent row coefficients。
在 Re s>1，有 L_orig(s,ψ)M_X(s,ψ)=Σc_nψ(n)q_n^−s，其中
c_n=Σ_(d|n,q_d≤X)μ(d)，c_1=1，c_n=0 (1<q_n≤X)，|c_n|≪q_n^ε。
取 Y>X≥2，将
\[
 {1\over2\pi i}\int_{(2)}L_{\rm orig}(\rho+z,\psi)
           M_X(\rho+z,\psi)\Gamma(z)Y^z\,dz
 =e^{-1/Y}+\sum_{q_n>X}c_n\psi(n)q_n^{-\rho}e^{-q_n/Y}       \tag{11}
\]
移到 Re z=1/2−β。nonprincipal 无 pole，z=0 的 residue 因
L_orig(ρ)=0 消失；允许 β=1 时，此条线位于
[−1/2,1/2−σ]⊂[−1/2,0)，仍未跨 Γ 的负整数 poles。
Γ 的 rapid vertical decay 与原 polynomial growth 保证移线及整轴收敛。
故每行必须有 critical LM integral 或 dyadic polynomial 的固定正下界。

critical 项不截到 |t|≤C H，而在整实轴积分。对 σ≤β≤1、|γ|≤H，
Γ(1/2−β+i(t−γ)) 有统一 majorant
G_H(t)≪_σ exp(−c dist(t,[−H,H]))·(1+dist(t,[−H,H]))^C。
逐行求和、Cauchy，再以 H'=1+|t| 的 (9) 和任意 t 的 (10) 积分，
费用由 ∫_R G_H(t)(1+|t|)^(d_F/4+ε)dt≪H(1+H)^(d_F/4+ε) 支付。
因此固定 H=1 也完整有效，不把 fixed C 的 Gamma 尾假设为 U^−A。
dyadic 项以 partial summation 去掉 q_n^−(β−σ) 及 e^−q_n/Y。
对 rowwise γ 用一维 Sobolev：sup_|t|≤H |P(t)|² 由
∫_(−H−1)^(H+1)(|P|²+|P'|²) 控制；P' 只在固定 coefficients 上乘 log q_n。
partial-sum maxima 用 binary interval decomposition 付 log²Y；每块是
fixed column support。于是所有大筛作用的系数先于 k-sum 固定。
tails q_n>Y^(1+ε) 由 e^−q_n/Y 支付，可先固定任意大的 tail order。
这些步骤只付 (UHXY)^ε 和 H，而非未声明的 moving-row profile assumption。

Cauchy、(6)、(9)、(10) 因而给
\[
\begin{split}
 C_w(\sigma,H)\ll &(UHXY)^\epsilon H\bigl[
 Y^{1/2-\sigma}(1+H)^{d_F/4}
       (\mathcal L_w[M+X+(MX)^{2/3}])^{1/2}\\
 &+MX^{1-2\sigma}
   +M^{2/3}X^{5/3-2\sigma}
   +M^{2/3}Y^{5/3-2\sigma}+Y^{2-2\sigma}\bigr].             \tag{12}
\end{split}
\]
这就是所需逐 frozen-w 的 detector，已列出其 uniform analytic 前件。
它数实际行；不直接套 BGL 的星号 family theorem，不从 raw inverse 大值
推出不存在的实际零点，也不要求原 auxiliary witness 具有 squarefree row。

取 X=2U^h、Y=C U^y(1+H)^[d_F/(6−4σ)]，h≤y，C 足够固定保证 Y>X。
高度贡献统一为
\[
 (1+H)^{p(\sigma)},\qquad
 p(\sigma)=1+{d_F(1-\sigma)\over3-2\sigma}.                \tag{13}
\]
Type I 的额外指数 d_F/4−(σ−1/2)d_F/(6−4σ) 恰为 p−1；
Y^(2−2σ) 也一样；positive Y-cross 的高度指数更小，negative Y-cross
不增加费用。X-terms 只有最外面的 H。

## 6. 把 moving w 全部计回：精确优化对象

写 M=U^x，V=U^(1−x)，0≤x≤1；dyad 比较常数与 log U rounding
付 U^ε。由 R_w≤U^((1−x)/2)，
\[
 \mathcal L_w\ll U^{\ell(x)},\quad
 \ell(x)=\max\{x,(1+x)/4,(1+5x)/6\}
 =\begin{cases}(1+x)/4,&x\le1/7,\\(1+5x)/6,&x\ge1/7.\end{cases} \tag{14}
\]
令 Eσ(h,y;x) 是下列五数的最大值：
\[
\begin{gathered}
 {\ell(x)+\max\{x,h,2(x+h)/3\}\over2}-(\sigma-1/2)y,\\
 x+(1-2\sigma)h,\qquad 2x/3+(5/3-2\sigma)h,\\
 2x/3+(5/3-2\sigma)y,\qquad (2-2\sigma)y .                \tag{15}
\end{gathered}
\]
完整层计数 exponent≤
\[
 \min\{(1+x)/2,\ (1-x)/2+E_\sigma(h,y;x)\}.               \tag{16}
\]
第一项是 actual row cardinality；第二项来自全部 powerful w。不能把
冻结的 w 计数丢掉，也不能把 rad(w) 当 q_w 放大之后宣称同一个优化。
下面给 continuous exact certificates，而非有限网格 PASS 代替分析证明。

## 7. 1/2<σ≤5/6 的所有 sixthfree raw count

置 r=7/6−σ、c=5/3−2σ≥0，g_low=8(1−σ)/(7−6σ)≥2/3。
x≤1/5 时 (16) 的第一项≤3/5<g_low，直接付原 cardinality。
x≥1/5 时 ℓ=(1+5x)/6，选择
\[
 h=x/2,\qquad y={1+3x\over12r}.                           \tag{17}
\]
有 h≤y≤2x：前者由 r≤2/3 和 1≥x；后者由 r≥1/3、x≥1/5。
因此 max{x,h,2(x+h)/3}=x。Type I 与 Y-cross 同为
E=2x/3+c y；Y-plain≤E 等价 y≤2x；X-cross≤Y-cross 由 c≥0。
X-first 为 x(3/2−σ)，而
\[
 g_{\rm low}-(3/2-\sigma)
 ={ -6(\sigma-1/2)(\sigma-5/6)\over7-6\sigma}\ge0,
 \qquad E\ge g_{\rm low}x,                               \tag{18}
\]
后者由 y≥x/(3r) 得到。因此 (15) 恰为 E。
再加 w-count，
\[
 (1-x)/2+E={1\over2}+{c\over12r}
            +x\left({1\over6}+{c\over4r}\right)
 \le {2\over3}+{c\over3r}=g_{\rm low}.                   \tag{19}
\]
对所有 x 连续成立，得到
\[
 C(U;\sigma,H)\ll_{\mathcal A,\sigma,\epsilon}
 U^{8(1-\sigma)/(7-6\sigma)+\epsilon}
 (1+H)^{1+d_F(1-\sigma)/(3-2\sigma)+\epsilon},
 \quad 1/2<\sigma\le5/6.                                \tag{20}
\]
它是 all-sixthfree 的逐层重证，非 squarefree-family theorem 的误用。

## 8. σ=7/8 的有理分段证书及邻域

此时 (15) 可删 Y-cross，剩
\[
 E=\max\{(\ell+\max\{x,h,2(x+h)/3\})/2-3y/8,
          x-3h/4,\ 2x/3-h/12,\ y/4\}.                  \tag{21}
\]
以下每段直接代入 (21)，所有 dominance 为 affine inequalities：

| x-range | h | y | E | (1−x)/2+E |
|---|---|---|---|---|
| [1/7,1] | (22x−2)/13 | 2(1+41x)/39 | (1+41x)/78 | (20+x)/39 |
| [2/15,1/7] | (29x−3)/13 | (1+25x)/13 | (1+25x)/52 | (27−x)/52 |
| [0,2/15] | max{0,x−1/15} | x+1/5 | (1+5x)/20 | (11−5x)/20 |

前两段 h≥x/2、h≤2x，大筛最大项为 2(x+h)/3；Type I、X-cross、
Y-plain 相等，X-first≤E。第三段 h≤x/2，最大项为 x；Type I 和
Y-plain 相等，X-first≤E，X-cross≤E。第一段总指数≤7/13，
第二段总指数<7/13；第三段 x≤1/15 用 cardinality≤8/15，
x≥1/15 用最后一列≤8/15。故
\[
 C(U;7/8,H)\ll U^{7/13+\epsilon}(1+H)^{6/5+\epsilon}.      \tag{22}
\]
这里 d_F=2；7/13 与 BGL squarefree g(7/8) 数值一致，但准入证明不同。
旧 raw R(3/4)=5/8，(22) 在 raw 层严格更强。

固定上述 h,y，max y=28/13。对 σ∈(5/6,7/8]，每个 (15) 分支
相对 7/8 的增长≤2y_max(7/8−σ)；σ≥7/8 时所有分支不增。
于是安全的 σ-neighborhood 公式为
\[
 G_{\rm safe}(\sigma)
 =\min\{1,7/13+(56/13)(7/8-\sigma)_+\},
 \quad C(U;\sigma,H)\ll U^{G_{\rm safe}(\sigma)+\epsilon}
                         (1+H)^{p(\sigma)+\epsilon},
 \quad 5/6<\sigma<1.                                    \tag{23}
\]
不宣称 (23) 是全部高 σ 的最优 LP。在 [17/20,7/8]，
G_safe=56(1−σ)/13，且严格小于旧 raw R=3/2−σ；一般该比较需要
σ>73/86。先固定 σ 邻域与 ε，再选原小 τ，不能在 T_1 之后反向变常数。

## 9. 原 detector、reciprocal good rows 与最终包络的不同层次

对原 a>51/100 bin，取 σ=a、H=3I T_1。原 bin 已有实际 ψ* zero，
故 #bin≤C(U;a,3I T_1)，finite Θ、orientations、ray labels 和 dyadic w
的次数均付 U^ε。新计数可以与原 raw R(2a−1) 取 min。
原 large inverse/plain witnesses 的共同 presentation、shared height、
profiles、r+m≥t、r≤t、m≤1/2 等约束都保持原版本。辅助 X,Y 可比
原 witness 长，这是零点计数证明的长度，不是新的物理 probe slots。
本文没有支付新的 marked/supscale amplification moment。

除去实际 zeros 的 buffered rectangle 后，原 logarithmic-control lemma
在 Re s≥a+6e、inner height |t|≤(3i+2)T_1 给 |L_orig|+|L_orig^-1|≪U^ε。
我们沿用同一 a+2e zero-free outer rectangle、固定 positive gap 和
deleted-factor bounds；不从 density 独自推出逐行 reciprocal bound。
在更一般固定 σ 的应用也必须先排除 outer rectangle zeros，再保留
固定向右 buffer 和 inner height。自然 zero masks 不在恢复中丢失。

必须区分三种指数：

1. 原 inverse-only raw R(δ)=min{1,max{1−δ/2,4/3−δ}}；
2. 本文实际 primitive-zero raw count (20)、(23)；
3. [451 的最终 whole-slot/amplification envelope](../../notes/451-kappa-feedback-cubic-boundary-and-family-continuation.md)
   R_{*,κ}(δ,q)，已经联合原 inverse/plain 信息。

451 的等号不是 a≈7/8，而是
δ_*=(5−9e_*)/(6+18e_*)≈0.388、a_*=(1+δ_*)/2≈0.694、q=δ_*/2。
在那里原 raw 约 0.945，新 g_low(a_*) 约 0.863，最终已付 envelope
恰为 2/3。直接再取 min 新 raw 与最终 envelope **没有提升**。
β_* 是全族最高零点实部；a 是 moving row bin，两者不能混为一个参数。
高 σ raw count 的节省也不能仅因 a≈β_* 就被称为新的 continuation boundary。

实际上可从 [450 的已付公式](../../notes/450-plain-kappa-extension-and-actual-capacity.md)
直接作全域比较。令 δ∈[1/50,3/4]、κ∈[37/50,1]、z=q/δ∈[0,1/2]，
c_κ=1/(3κ)、D=3−(1+2c_κ)z、P=(2−2c_κz)(1−z)。则
2D−3P=2z(2+c_κ−3c_κz)≥0。450 的实际 R 公式遂给
\[
 R_{*,\kappa}=1-\delta+
 { (5/6-\delta)\delta P\over2[(5/6-\delta)D+\delta P]}
 \le R_{\max}(\delta)={15-16\delta\over15-6\delta}.       \tag{24}
\]
δ≤2/3 时，(20) 的指数 g_low((1+δ)/2) 与 R_max 的差为
\[
 {\delta(25-24\delta)\over(4-3\delta)(15-6\delta)}>0.      \tag{25}
\]
δ∈[2/3,3/4] 时，(23) 的指数是 28(1−δ)/13，其差为
\[
 {225-380\delta+168\delta^2\over13(15-6\delta)}>0.         \tag{26}
\]
分子在该区间递减，最小值为69/2。因此本文真正证明的两个 raw 指数
在原所有 actual bins 中都严格弱于最终 amplification envelope。
这个全域结论不依赖仅看某一个最高 β_*，也不要求未付的 full high4。
用于 actual above-floor 行时 δ>1/50；闭端点 δ=1/50 仅保留代数比较。
原 floor bin 没有实际零点见证，其计数仍独立使用 U，不能以 (25) 替换。

实际后续最低接口是：在原共同 inverse/plain presentation 和原 probe
slots 内，重新证明新的 density 约束如何与其 amplitude information 联合，
给严格低于最终 R_{*,κ} 的完整 row envelope；然后重付 whole high/low、
principal、Euler deletions、heights 与 all physical ranges。
不能把两个独立 upper bounds 相乘、机械取幂或重新命名而冒充该联合证明。
该接口目前 [O]。本文只交付可逐式审计的原 raw 计数候选及统一 analytic
推导；独审通过后可相对原 [R] 记录，不因此发布新无零界或新 RH 结论。
