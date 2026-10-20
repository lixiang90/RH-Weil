# Beurling 测度、固定 Gaussian 对偶与纯分析准入：原始文献审查

2026-10-20。独立分工原稿；供 root 消费，本文不改 STATE、Goal 或 cadence，不登记远端提交。
已恢复 README/STATE、check/show、G20261014、C023、最新 strategy、macro frontier；
当前冻结基线与原成长 core/Ξ 完成门不变。用户新方向要求扩大对象类和挖掘旧资产，
不能由整理、分类、函数方程或正测度合法性推定 RH 进展。

## 1. 一手来源与准确范围

本节只引用原作者论文/原作者机构稿。下文“内部命题”均有本稿自证，
不冒称为这些论文的现成定理，亦不宣称优先权。

| 来源 | 已核定位 | 能消费什么 | 不能消费什么 |
|---|---|---|---|
| Debruyne–Maes–Vindas, *Halász's theorem for Beurling generalized numbers*, arXiv:1902.03870v3 | §1 pp.1–2；§2 p.2，原稿 PDF p.2 | 非离散广义系统可由正 Stieltjes 测度对 `dN=exp_*(dΠ)` 定义；Mellin 像为指数 | 任意正 `dΠ` 不必来自正 primitive-prime 测度；普通群卷积分布也不能无条件取指数 |
| Diamond–Montgomery–Vorhauer, *Beurling primes with large oscillation*, Math. Ann.334 (2006),1–36 | 原文 p.1 abstract；定理内容在原文 introduction（本次 PDF 逐页读取接口失败，仅摘要与原作者后文回述核对） | 每个 `1/2<θ<1` 有离散系统 `N(x)=κx+O(x^θ)`，ζ 在 `σ=1−a/log t` 上无穷多零点；故此正则性不推 RH | 不把该结论扩成 `θ≤1/2`，不声称这些系统满足经典 Gamma 函数方程 |
| Broucke–Debruyne–Vindas, *Beurling integers with RH and large oscillation*, arXiv:2004.11501v2 | §1 p.1 对 DMV 的精确回述；Theorem 1.1，pp.2–3 | 正则性与 RH 是不同方向；论文构造 prime 误差 `O(√x)` 而 integer 计数有近线性振荡的系统 | 这里的 Beurling RH 主要是右半平面无零，不自动给经典完成化与反射全谱 |
| Burnol, *Deux extensions de Théorèmes de Hamburger*, arXiv:1106.4749v2, Expositiones Math.30 (2012),295–308 | Introduction pp.2–4；Theorem 1/Cor.2 pp.2–3；Theorem 2 p.4 | 精确区分普通 `Σa_n n^{-s}` 与一般 `Σa_n x_n^{-s}`；一般两侧 FE 下，有限多个 `Z` 平移支撑是额外条件及等价分类项 | Theorem 2 并未从函数方程自动推出格支撑；不能把普通整数 Dirichlet 支撑偷放进“纯分析恢复” |
| Soundararajan, *Degree 1 elements of the Selberg class*, arXiv:math/0306300 | Axioms pp.1–2；unnumbered Theorem p.2 | 普通 n 支撑、Ramanujan、degree 1 FE 等给周期系数；再加 prime-power Euler 公理给移位 Dirichlet L | 这些公理已显式输入普通 n/prime powers；分类没有证明这些 L 的 RH |

直接链接：

- [Debruyne–Maes–Vindas 原稿](https://backoffice.biblio.ugent.be/download/8676933/8676934)。
- [DMV 原文机构 PDF](https://deepblue.lib.umich.edu/bitstream/handle/2027.42/46253/208_2005_Article_638.pdf)，[DOI](https://doi.org/10.1007/s00208-005-0638-2)。
- [Broucke–Debruyne–Vindas 原稿](https://arxiv.org/pdf/2004.11501)。
- [Burnol 原稿](https://arxiv.org/pdf/1106.4749)。
- [Soundararajan 原稿](https://arxiv.org/pdf/math/0306300)。

DMV 的完整原证明本次尚未逐页审读，故这里仅作条件鉴别证据，不把其构造细节
输入下游费用或核心比较；若后续真正使用该构造，须补齐原文定理参数和误差。

## 2. 先固定三个测度，避免把正性混成一项

取 `[1,∞)` 上的局部有限正测度 `dN`，其中单位质量为 1。乘法卷积为

\[
\int f\,d(\mu *_\times\nu)
=\iint f(xy)\,d\mu(x)d\nu(y).
\]

给定 `dΠ≥0`、`Π(1)=0`，且某 `σ0` 上 `∫x^{-σ0}dΠ<∞`，可在该加权测度
代数定义

\[
dN=\exp_{*_\times}(d\Pi)
=\delta_1+\sum_{j\ge1}\frac{(d\Pi)^{*j}}{j!},\qquad
Z(s)=\mathcal M(dN)(s)=\exp\mathcal M(d\Pi)(s).
\tag{2.1}
\]

若另外有 primitive-prime 测度 `dP≥0`，则 prime powers 的正确关系是

\[
d\Pi=\sum_{k\ge1}\frac1k(T_k)_*dP,
\quad T_k(x)=x^k,
\quad \log Z(s)=\int-\log(1-x^{-s})\,dP(x).
\tag{2.2}
\]

`dP` 与 `dΠ` 不同；`dψ(x)=log x·dΠ(x)` 又是第三个对象。经典 `dP` 为每个
primitive 原子的单位质量，`dΠ` 在第 k 次幂携带 `1/k`，`dψ` 才携带 `log p`。
若转到 `u=log x`，则 `T_k` 变成 `u↦ku`；密度 `p(u)du` 的 pushforward
为 `p(u/k)du/k`，加外面的 `1/k` 后为 `p(u/k)du/k²`。这个 Jacobian 不能丢。

任意正 `Π` 的形式 Möbius 逆可能是 signed；仅证明 `exp_*Π≥0` 不支付
`P≥0`。同理，`P≥0`、`Π≥0`、`N≥0` 全部成立也不支付完整 Weil 型正性。
一般 distribution 若没有支撑/阶/乘积/卷积收敛结构，不在 (2.1) 的合法类别内。

## 3. 一个自证的连续正 Π 鉴别族：很强 N 正则性仍不足

以下不依赖 DMV 构造。取 `0<α<1`、`β=(1+α)/2`、`γ>0`，定义 log 坐标测度

\[
d\Pi(e^u)=\frac{e^u+e^{\alpha u}-2e^{\beta u}\cos(\gamma u)}u\,du.
\tag{3.1}
\]

AM–GM 给分子非负；原点处为 `O(u²)`，故测度局部有限。Frullani 积分在
`Re s>1` 上给

\[
Z(s)=\frac{(s-\beta)^2+\gamma^2}{(s-1)(s-\alpha)}
=1+\frac C{(s-1)(s-\alpha)},\quad
C=((1-\alpha)/2)^2+\gamma^2>0.
\tag{3.2}
\]

由 Mellin 唯一性，

\[
dN=\delta_1+A(1-x^{\alpha-1})\,dx,\quad
A=C/(1-\alpha),
\]
\[
N(x)=Ax-\frac A\alpha x^\alpha+1-A+\frac A\alpha.
\tag{3.3}
\]

所以 `N=Ax+O(x^α)` 可有任意小的正指数，而 `Z` 在 `β±iγ` 有右半临界带
零点。该模型已付 `Π≥0,N≥0`，尚未在本稿支付 `P≥0`，也没有经典 Gamma FE。
因此准确结论仅是：**广义 pair-measure 类中的 N 误差，即使幂次很小，也不独立
强迫中心性。** 它不能用来否定带额外正 primitive 条件或固定 Gaussian FE 的命题。

## 4. Root 的更强联合鉴别族核对：正 primitive、近线性 N 与裸 FE

root 提出的模型比 §3 对本次问题更直接。取 `0<a<1,a≠1/2`，`b=1-a`，`c=ab`，

\[
Z_a(s)=\frac{(s-a)(s-b)}{s(s-1)}
=1+\frac c{s(s-1)}.
\tag{4.1}
\]

其 inverse 为

\[
dN_a=\delta_1+c(1-x^{-1})dx,\qquad
N_a(x)=1+c(x-1-\log x).
\tag{4.2}
\]

`Z_a(1-s)=Z_a(s)`，且 `s(s-1)Z_a=(s-a)(s-b)` 是 entire symmetric polynomial，
但零点为不居中的 `a,b`。log-prime 测度是

\[
d\Pi_a(e^u)=\frac{e^u+1-e^{au}-e^{bu}}u\,du
=\frac1u\sum_{m\ge2}\frac{A_mu^m}{m!}\,du,\quad
A_m=1-a^m-b^m>0.
\tag{4.3}
\]

定义

\[
p_a(u)=\frac1u\sum_{m\ge2}
\frac{A_mu^m}{m!\,\zeta(m+1)}\ge0,\qquad dP_a(e^u)=p_a(u)du.
\tag{4.4}
\]

这里 `ζ(m+1)=Σ_{k≥1}k^{-m-1}` 只是给 repeated-power operator 的显式正系数；
没有输入经典 ζ 的零点/素数性质。Tonelli 与 §2 的 Jacobian 给

\[
\sum_{k\ge1}\frac1{k^2}p_a(u/k)
=\frac1u\sum_{m\ge2}\frac{A_mu^m}{m!}
\frac{\sum_{k\ge1}k^{-m-1}}{\zeta(m+1)},
\tag{4.5}
\]

恰等 (4.3) 的密度。`p_a≤Π_a` 的密度逐项成立，故 `Re s>1` 的所需加权积分
与 Euler 对数绝对收敛也成立。这支付了同一个模型的 `P≥0,Π≥0,N≥0` 与裸 FE。

限制必须一起消费：它的 pole 在 `0,1`，没有经典固定 `Γ(s/2)π^{-s/2}`；
完成 polynomial 没有经典零点密度；不能据此否定“固定 Gaussian 反演”的条件。
与旧 [290](../../notes/290-positive-euler-duality-model-and-mass-moment-nonidentification.md)
比较：290 已有正离散 Euler、函数域风格 FE 和离线零点，
故“FE 不足”不是新增。这个连续族新增鉴别信息是同时实现 `N=Ax+O(log x)`
和正 primitive measure，而不是再一次证明一般对称不等于纯度。

## 5. 内部命题：固定 Fourier 核 + 正测度 + 单位 gap 无需输入 n 支撑便恢复 comb

这是可独立检验的分类命题，不依赖 Beurling Euler 结构，也不推出 RH。
Fourier 约定为 `Ff(ξ)=∫f(x)e^{-2πixξ}dx`，作用于 tempered distributions。

**命题 5.1。** 若 `μ` 为正 tempered Radon measure，满足

\[
\mathcal F\mu=\mu,\qquad \mu|_{(-1,1)}=\delta_0,
\tag{5.1}
\]

则 `μ=Σ_{n∈Z}δ_n`。无须先假设离散、整数支撑、均匀离散性或乘法分解。

**证明。** 选实偶 `h_j∈C_c^∞(-1/2,1/2)`，使 `h_j→1_{[-1/2,1/2]}` 在 L¹、L²
中成立。令 `f_j=|check h_j|²`，则为非负 Schwartz 函数，且

\[
\widehat f_j=h_j*\widetilde h_j,\quad
\operatorname{supp}\widehat f_j\subset(-1,1),\quad
\widehat f_j(0)=\|h_j\|_2^2.
\]

(5.1) 因而给

\[
\int f_jd\mu=\|h_j\|_2^2\to1,
\quad f_j(0)=\left|\int h_j\right|^2\to1.
\tag{5.2}
\]

扣去 `μ({0})=1` 的贡献，余项非负且趋 0。L¹ 收敛给 `check h_j` 一致收敛到
`sinc(πx)`；Fatou 得

\[
\int_{\mathbb R\setminus\{0\}}
\left|\frac{\sin\pi x}{\pi x}\right|^2d\mu(x)=0.
\tag{5.3}
\]

故 `supp μ⊂Z`。写 `μ=Σw_nδ_n`（正 tempered 允许至多 polynomial 增长）。
支撑在 Z 意味 `e^{2πix}μ=μ`，Fourier 后知 `Fμ` 是 1-periodic distribution。
`Fμ=μ`，故 μ 本身 1-periodic；结合中央 interval 的单位 atom，所有 `w_n=1`。
证毕。证明始终只对 Schwartz 函数使用 Fourier 恒等式，未把 sinc² 越域直接代入。

单位 gap 的半径与 Fourier 中 `2π` 的归一化绑定。若只要求 gap 半径 `r<1`，
分类即不真：对任意 `a>1`，

\[
\mu_a=\frac{\delta_{a\mathbb Z}+a^{-1}\delta_{a^{-1}\mathbb Z}}{1+a^{-1}}
\tag{5.3a}
\]

是原点质量 1 的正 Fourier-invariant measure，其 gap 半径为 `a^{-1}`，一般不等于
单位 comb。由 `a↓1`，gap 可任意接近 1。因此不能将“gap 几乎足够”或任意缩放
算作本命题。若将原点质量 1 改为已知 `c>0` 且保持精确单位 gap，则同证给 `c·comb`；
原点归一化决定恢复的整数权重。

**命题 5.2（Gaussian 版本）。** 设 μ 为正、偶、tempered measure，中央 gap 同上。
若对所有 `t>0` 都有精确式

\[
\Theta_\mu(t):=\langle\mu,e^{-\pi t x^2}\rangle
=t^{-1/2}\Theta_\mu(1/t),
\tag{5.4}
\]

则同样 μ 为 comb。

**证明。** 由 Gaussian Fourier 公式，`D=μ−Fμ` 是偶 tempered distribution，且
`<D,e^{-πt x²}>=0` 对每个 t 成立。在任一正 t 对 t 任意微分，得到 `D` 消灭
`x^{2k}e^{-πt x²}` 的全部配对。取 `t=1/(2π)`，这些函数张成全部偶 Hermite
functions 的有限线性组合；Hermite 展开在 Schwartz 拓扑中收敛。
D 偶且连续，故 D=0。这里 t 对 Gaussian 的微分在 Schwartz 拓扑中成立，
每个导数为 `(-πx²)^k e^{-πt x²}`；所用 Hermite 有限组合的稠密性也是 Schwartz
拓扑的稠密性，足供 tempered distribution 消灭极限。再用 5.1。证毕。

偶性不能省略：`comb+ε(δ_1−δ_{−1})` 在 `|ε|≤1` 仍是正测度，所有 Gaussian
配对完全不变，却一般不是 comb，也不 Fourier-invariant。式 (5.5) 的对称化明确支付偶性。

若在 g-integer 测度上定义

\[
\mu_N=\delta_0+\iota_*dN+(-\iota)_*dN,
\quad\iota:[1,\infty)\hookrightarrow\mathbb R,
\tag{5.5}
\]

则 `[1,∞)` 支撑自动给 (5.1) 的中央 gap；`N(x)=O(x^A)` 足够 tempered。
于是精确、固定 Gaussian 反演可纯分析恢复 `dN=Σ_{n≥1}δ_n`。
这是真正“从一般正测度恢复整数”的合适命题，primitive P 的解析恢复可留到其后。

**它没有给 RH。** 经典 comb 的 (5.4) 是已知 Poisson/Jacobi 恒等式；恢复出同一个
ζ，只说明对象分类正确。ζ 的完整 Weil 正性、成长补空间/耦合、Ξ determinant 极限
仍未由 (5.4) 证明。将“正 μ”换名为“正 spectral μ”会偷换对象：μ 是 integer-side
测度，零点侧正测度恰是仍需支付的结论。

## 6. 建议唯一后续门：固定核之后的“正性运输缺陷”，不再收集更泛 FE

本次最有价值的已付输入是 5.1/5.2：确能不用 n 支撑前提恢复整数。最便宜负对照
是 §4：正 primitive、很强 N 正则性及裸 FE 全有，仍不居中；它因 continuous 密度
必不满足固定 Gaussian 条件。因此 arbitrary-kernel FE 与固定 Gaussian FE 必须分开。

下一门应冻结为一个同对象测试：从 (5.4) 推导完整显式公式时，定位一个**显式
remainder/coupling kernel**，并与仓库 405 的 Poisson 主关系、554 的正跳和
560 的 `positive trace−compact+双 pole` 最强旧分解逐项比较。只有满足以下条件才
可建立新数学合同：

1. kernel/映射由 integer-side μ 与固定 Fourier/Gaussian 操作独立给出，不使用零点；
2. 全 complex source、原 norm、actual Gamma、全部 prime powers 与双 pole 同时在场；
3. 成功具体削弱现有成长 compact error/core/coupling 责任，而非重证分类或等价；
4. 失败有一个可证明的负方向或 paid repair 比较，能改变路线选择。

若只能再次导出 Weil 正性等价式、相同 principal 零关系或 `未知 remainder≥0`，
来源审查即停，不续一个新的“Gaussian positivity”标签。该停止条件来自现有
连续 source-only 经验，不另设轮数。本稿最强后果是明确类的识别与条件鉴别；
原成长关键瓶颈尚未改变。

## 7. 给 root 的消费记录

- 对象：Beurling 正测度 pair/triple；命题5 integer-side positive tempered μ。
- norm/domain：weighted variation algebra 与 Schwartz/tempered duality；不是原 Weil du norm 的新界。
- 量词：所有 `Re s>1`、所有 `u>0`、Gaussian 所有 `t>0`；非有限采样，非成长误差界。
- 已付：§2 合法字典；§3/4 有理函数计算；§4 正 primitive repeated-power 合成；§5 分类自证。
- 未付：经典 Gamma FE 不能由裸对称替代；Gaussian-to-Weil 正性/完整 source 费用和 Ξ 全局识别未付。
- actual coefficient：§4 负号 `−e^{au}−e^{bu}` 置于 Π 分子；N 密度 `+c(1−1/x)`；均未改变成 spectral 正性。
- 最强旧扣除：290 已排一般 Euler+FE⇒RH，405/554 已有 Poisson 主关系与正源；本稿不重复记成 RH 箭头推进。
- 阶段：独立原稿；需 root/另一组织审查后才能登记其确切范围；无数学完成或 Goal complete 主张。
