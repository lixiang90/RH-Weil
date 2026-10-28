# Frozen quiet source：原du frame、measurable全线尾与(Q)准入核证

2026-10-28；`/root/rational_first_gate`当前独占稿。已恢复README／STATE、check→show、G20261027／原0c4f、Goal／frontier／AL／quarter结算及当前[root冻结规则](root-fixed-band-and-signed-error-admission.md)，核实际工作树。C052／589与quarter旧0均已耗尽发布；本稿只核这份不同具体比较，不续scalar／degree／rank／height优化，不改g、4／6或频带，不web／新增source／PDF／数值，不改STATE／Git／cadence，不预C053／590。运行Goal现场观察由root负责；child调用get_goal返回null，不据此重建或改Goal。

**结论：(Q)在全部complex系数、全部大X上统一闭合，费用为`Ce^(−cℓ²)`。必要全线接口其实已在C052所核的差商正核内，fixed-f限制只属于随后Schwartz尾的推论。** 下文给出这一个接口的量词恢复、固定g的标准数学界及三段费用；不把589的fixed-source little-o直接套给moving源。这是已付uniform设施与标准frame／Gevrey代数的短直接组合，准入分类宜强旧应用0；其未逐字写出的source谱推论不单独创造新输入或计轮。

## 1. 冻结对象及真正调用的旧接口

沿560，actual source trace为

\[
 T_X[r]=\int_{\mathbb R}|\widehat r(t)|^2\rho_X(t)\,dt,
 \qquad k_X(t,t)=2\pi\rho_X(t).
\]

receiver Hilbert measure为dt/(2π)，实际投影S_X通过完整Euler Gram逆定义；它不是source operator A_X。以下并未以Gaussian trial下界替换S_X上界。

记ℓ=logX、A=√X/ℓ。调用C052已经根闭合的两个actual接口：

* 中央质量：`∫_|t|<1 ρ_X(t)dt ≤ C√X/ℓ²`。它直接弱于已付(6.8)的[-ℓ,ℓ] localized trace质量。
* 固定δ=1、B=6的(6.10)：存在c₁>0及X₁，使
  `sup_(1≤|t|≤ℓ⁶) ρ_X(t) ≤ C exp(−c₁A)`。

这里δ／B先固定；只变source，不变该接口的几何量词。第二项包括同一raw evaluator、weighted norm、真实`M_D G_X^(−1/2)`和全部2π，不能只从whole trial kernel推出。第一项和第二项均非589所述的某一fixed-f渐近，而是已核证明里的uniform actual质量／kernel结论。

## 2. 关键全线接口：任意measurable权，常数不依source

实际读C052 upper终稿§5、localization终稿§6，并对齐此前已读原件§4的(4.2)及767–780行。令`u_X=e^(iφ_X)`为actual Mellin scattering symbol。对全部t、全部X≥3，旧exact相位给

\[
 |\varphi_X'(t)|\le C a_X(t),\qquad
 a_X(t)=\sqrt X+\log(2+|t|).                         \tag{G1}
\]

常数为absolute固定数据：arch Γ的digamma界给log项；finite Euler所有proper powers给

\[
 \sum_{p\le X}\log p\sum_{k\ge1}p^{-k/2}
 =\sum_{p\le X}\frac{\log p}{\sqrt p-1}\le C\sqrt X
\]

（Chebyshev与分部积分足够）。没有漏掉k≥2，亦未给其错误的额外k。

若|v|≤1，沿t到t+v的`a_X`可由Ca_X(t)控制，故

\[
 |u_X(t+v)-u_X(t)|\le\min(2,Ca_X(t)|v|).
\]

|v|>1用2。在1/a_X(t)及1处分段，直接积分得

\[
 \int_{\mathbb R}\frac{|u_X(t+v)-u_X(t)|^2}{v^2}dv
 \le C a_X(t).                                      \tag{G2}
\]

这一步不使用φ″、fixed源的Schwartz seminorm或任何随X增长的Euler条件数。

令Π为Hardy投影。两个commutator input blocks的域正交；原(4.2)的非负difference-quotient kernel给，对每个bounded、compactly supported、非负measurable W，

\[
 \|M_{\sqrt W}[\Pi,M_{u_X}]\|_{\rm HS}^2
 \le C\int W(t)a_X(t)dt.                            \tag{G3}
\]

只是对非负核Tonelli；不调用含trace-class差分的(4.4)，故不要求W光滑、为某个fixed F的模平方或有source support常数。

actual receiver projection满足已付`0≤S_X≤(P𝓕_XP)²`，因为S_X reduces该自伴compression，且其square在Sonin range为I。后者的weighted Hardy-block HS平方由同一commutator energy支配。于是对上述W，positive trace比较给

\[
 \int W(t)\rho_X(t)dt
 =\|M_{\sqrt W}S_X\|_{\rm HS}^2
 \le C\int W(t)a_X(t)dt.                            \tag{G4}
\]

式中左侧receiver norm按dt/(2π)，因此恰为ρdt，无额外2π。若Hardy识别含output reflection，先把W变W(−t)，再用a_X偶性及变量替换，仍是(G4)。

对任意非负measurable W，用`W_n=min(W,n)1_[-n,n]`及单调收敛，得到同一(G4)，允许右侧为∞。等价地，

\[
 \boxed{\rho_X(t)\le C[\sqrt X+\log(2+|t|)]\quad\text{a.e. }t,}
                                                               \tag{G}
\]

C独立X、W、source、M及其系数；560的finite-X连续ρ还能将它读成全部t的点值界。这里实际恢复的是任意权的measure domination，不是从“每个fixed f的tail常数可依f”反推uniform性。C052终稿最后取fixed F Schwartz，只是(G4)的一个消费，未限制它的正核前件。

## 3. 不改literal g：Gevrey2与原du frame

587的同一固定g为`c exp[−1/(1−u²)]`于|u|<1、外零，c使||g||du=1。它不仅Schwartz。令d=1−|u|；对实u∈(−1,1)，取complex disk半径d/16。在该盘上`Re(1/(1−z²))≥c₀/d`，所以Cauchy给

\[
 |g^{(n)}(u)|\le C n!(C_0/d)^n e^{-c_0/d}
 \le C_1 C_2^n(n!)^2.                              \tag{H1}
\]

最后一式优化`d^(−n)e^(−c₀/d)`，用`n^n≤e^n n!`；同一个局部界也说明全部endpoint jets为0。积分后`||g^(n)||₁≤C₃ C₂^n(n!)²`。Fourier分部积分n次、取n为足够小的fixed常数乘√|t|的整数部分，得到

\[
 \boxed{|\widehat g(t)|\le C_g e^{-c_g\sqrt{|t|}}.} \tag{H2}
\]

全部常数只依这份已冻结g；没有换Gevrey source或调用一个未给uniformity的Schwartz尾。

对任意M及complex系数c_j，令`p(u)=Σ_(j<M)c_j e^(2πiju)`。它的|p|²以1为周期，且one-period积分为Σ|c_j|²。冻结源为

\[
 r(u)=g(u)e^{i\ell^4u}p(u),\quad
 \omega_j=\ell^4+2\pi j,\quad M=\lfloor\ell^6/(4\pi)\rfloor.
\]

g在[-1/2,1/2]有正minimum，且support[-1,1]恰覆盖两个period，故

\[
 c_g'\sum|c_j|^2\le\|r\|_{du}^2
 \le C_g'\sum|c_j|^2.                              \tag{H3}
\]

这给全部X／M统一Gram常数，精确维数M。carrier`e^(iℓ⁴u)`模为1，不改变原du；全部r仍属原Cc∞、zero-extension Dlog。没有将系数Euclidean norm免费等同原source norm。

## 4. 同一E_X的三段actual费用

以下C、c为固定正数，可逐式缩小c；不依X／M／coefficients。充分大X时`ℓ⁴≤ω_j≤3ℓ⁶/4`。记S=Σ|c_j|²，使用

\[
 |\widehat r(t)|^2
 =\left|\sum c_j\widehat g(t-\omega_j)\right|^2
 \le S\sum|\widehat g(t-\omega_j)|^2.               \tag{H4}
\]

**Core |t|<1。** 所有距离≥ℓ⁴−1，所以(H2)／(H4)及actual central mass给

\[
 T_X^{\rm core}[r]
 \le C S M e^{-c\ell^2}\frac{\sqrt X}{\ell^2}
 \le C\ell^4 e^{\ell/2-c\ell^2}\|r\|_{du}^2.        \tag{Q0}
\]

**Middle 1≤|t|≤ℓ⁶。** 对所有r同时用第1节的actual kernel upper，再用Plancherel：

\[
 T_X^{\rm mid}[r]
 \le C e^{-c_1A}\int|\widehat r(t)|^2dt
 =2\pi C e^{-c_1A}\|r\|_{du}^2.                    \tag{Q1}
\]

这里无需M因子或source-dependent supremum。所有复系数允许随X任意变。

**Outer |t|>ℓ⁶。** 每个中心≤3ℓ⁶/4，故`|t−ω_j|≥|t|/4`。用(H2)、(H4)、(G)，有

\[
 T_X^{\rm out}[r]
 \le C M S\int_{|t|>\ell^6}
 e^{-c\sqrt{|t|}}[\sqrt X+\log(2+|t|)]dt.
\]

设y=√|t|，在y≥ℓ³用`log(2+y²)≤C(1+y)`。显式积分polynomial乘exponential，得到

\[
 T_X^{\rm out}[r]
 \le C[\ell^9e^{\ell/2}+\ell^{12}]
                 e^{-c\ell^3}\|r\|_{du}^2.          \tag{Q2}
\]

这付清growing M及整条无穷频率尾，未把只在|t|≤X²的算术渐近外推到∞。

合并(Q0)–(Q2)，本次可交的具体费为

\[
 \epsilon_X\le C\left[
 \ell^4 e^{\ell/2-c\ell^2}+e^{-c_1\sqrt X/\ell}
 +(\ell^9e^{\ell/2}+\ell^{12})e^{-c\ell^3}\right]
 \le C'e^{-c'\ell^2}.                              \tag{Q}
\]

即`∀X≥X₀ ∀r∈E_X, T_X[r]≤ε_X||r||du²`。X₀只依固定g、旧δ=1／B=6接口及固定普适常数。没有先固定r、coefficients或dimension后再取X。

## 5. 三句、最强旧与准入停止范围

**Input：** 同一actual S_X／完整Gram逆、C052已经付清的central mass／(6.10)及其measurable正核前件，配587 literal g形成的原du E_X。没有独立新算术、几何或signed来源。

**Test：** 唯一(Q)的frame与三段积分已闭；必要关键是(G4)而非589 fixed-f little-o，g的Gevrey2责任由(H1)–(H2)显付。若将来(G4)的actual block比较被更正，须冻结(Q2)及全部谱消费，不能仅保fixed-f结论仍用moving族。

**Net：** 可将(Q)交给root／另一具体审作source谱min–max及完整K负压缩消费，且应扣除它是强旧uniform设施的短直接后果这一事实。它与585／587的每先fixed lower、588 weak-nonzero coercivity、589 fixed-f upper量词不同；差异由源频率逃逸／weak limit0承担，不与旧结果矛盾。但“新写出的cofinal空间／谱后果”不自动是新输入或一数学轮，本稿建议旧0止此具体比较，不建C053／590或续优化。

本腿不重复另一稿的整套K谱证明。full Q仍为560的`T_X−K_X+P_pole`；在原小窗537正性下，polefree V_X上的负K方向对Q的符号有利，不是Q负源。Γ／FP-contact、全部proper powers与双pole没有删除；两个pole条件也不等于mean zero。whole4/5负惯性UPPER、primitive／mixed与完整signed核心／Goal完成门均未由本稿改变。

## 6. 原件与当前版本

实际核：当前root规则全文；587 literal g及fixed-d范围；560 density／du／2π；C052最终upper稿§5和localization稿§6，沿它们既有阅读范围核原(4.2)／767–780的量词。无新增章节／primary来源或下载。绑定：

* root当前规则：4350 bytes，LF SHA256 `875939127b6b68deb89846b4fe0afa6cd0c0a981db77ccb58e5129bb14281fe3`。
* [C052 upper/tail原审](../sonin-scalar-normalization/source-upper-and-tail-proof-audit.md)：10211 bytes，LF SHA256 `bab769113b4ce8c858dfd4b7a83dea6abd8808436a599d2206ea9a9bf0915fff`。
* [C052 localization原审](../sonin-scalar-normalization/source-localization-proof-audit.md)：11459 bytes，LF SHA256 `809bc7ffc6f1fbf4dd24af0d710af05fb7ca1bc259992430c3fd6760912ffcb1`。
* [587](../../../notes/587-actual-sonin-moment-spread-and-growing-source-rank-necessity.md)：8681 bytes，LF SHA256 `e4d30cfb6d07299386014cb4c4e3e3979ab5111264355dfb37b24629f121ac82`。

本稿是已执行具体准入证据，非root已消费／数学结算。cadence3/history53/latest589/formal17保持，无共享STATE／Git变更。
