# 原 Vaughan Type I 的 2/3 付款与完整 Type II 剩余

2026-10-08。作者：radial_review。研究基线：5b4c99e561ddec59f1818b8471da508036503745。

状态：完整子项推导，待不同作者独审。实际支付了原高段 Vaughan Type I 及较低长度块的 T^{2/3+ε} 四矩上界，并将原完整 genuine-prime scalar 归约到明确的原 Möbius-divisor Type II 多项式。**没有证明 whole M_T≤T^{2/3+ε}，没有新的常数预算、比例或无零边界。** 475/476 和全部冻结来源保持不变。

## 1. 原对象、量词与用到的输入

仍取

\[
 X=T/(2\pi),\quad \ell=\log X,\quad a_\ell\ge c_\phi>0,
 \quad J_T=[T/4,4T],
\]
\[
 P_H(t)=\frac1{a_\ell\ell}
 \sum_{\sqrt X<p\le X}\frac{\log p}{\sqrt p}p^{it},
 \qquad
 \mathcal M_T=\frac1T\int_{J_T}|P_H(t)|^4dt.
 \tag{1}
\]

定义 normalized 时间范数
\(\|F\|_{r,T}=(T^{-1}\int_{J_T}|F|^r)^{1/r}\)。
它仍是原正高度窗，未移到 t=0、扩大到长高度、改 normalizer 或平滑两端。

| 已冻结对象 | canonical LF SHA256 |
|---|---|
| [原正高度零包来源](hybrid-positive-height-zero-packet-fourth-upper-research-radial.md) | 8bcbd27da46d922d9e6e741fcf9a87012d565052f8d97b3ad12e99b3edbc2481 |
| [原 scalar 与 proper-power 准入](hybrid-short-carrier-canonical-scalar-fourth-admission-research-radial.md) | f04279a9de54303d772859b2ee5e05010567404c53143c928a14e905eb51a0d7 |
| [完整半素数 variance 研究](hybrid-canonical-semiprime-smooth-subtraction-and-variance-obstruction-research-compression.md) | 7fcb097ad17d77b7281acd1f7c7d0f1580c5519c015437e104823cdfabd52645 |
| [已提交 476 增长结果](../../notes/476-original-fourth-growth-five-sevenths-with-ivic-density.md) | 179829dd25f92ff187359f73455aafad9f957d714df13cf871db47a76e9408b6 |

新子项估计不使用 [Rθ] 或任何新密度。用到的外部经典输入仅为二阶导数 exponential-sum test，已核 [Montgomery–Vaughan 作者书 Volume II](https://personal.science.psu.edu/rcv4/Vol2/Vol2.pdf) Theorem 16.7（PDF 第 18 页，印刷第 8 页）；对负二阶导数取共轭即可。Vaughan 系数恒等式参照同书 (17.4)–(17.7)，以下也给出直接验证。系数 divisor bounds 与时间二矩在下文完整支付。

对每个固定 ε>0，先选择下文的固定 divisor 损失 δ>0，再令 T→∞。所有日志费用纳入 ε；未采用随 T 移动的外部系数合同。

## 2. 一个足够的原时间均值引理

若 \(F(t)=\sum_{n\le Z}\alpha_n n^{it}\)，则任意长为 O(T) 的真实时间区间 J 都有

\[
 \frac1T\int_J|F(t)|^2dt
 \ll \left(1+\frac{Z\log(2Z)}T\right)
       \sum_{n\le Z}|\alpha_n|^2.
 \tag{2}
\]

证明：对角贡献为 |J|Σ|α_n|²；非对角积分绝对值≤2/|log(n/m)|。对 1≤m<n≤Z，

\[
 \log(n/m)\ge(n-m)/n\ge(n-m)/Z.
\]

再以 2|α_mα_n|≤|α_m|²+|α_n|² 消去乘积，对差 n−m 求 harmonic sum，即得 (2)。此较弱的有日志均值已经足够；不需要假定完整 prime 四矩或调用未知 signed correlation。

固定 k,b 后，若 \(v(n)\ll \tau_k(n)(\log(2n))^b\)，则任意固定 δ>0 有 |v(n)|≪δ n^δ。故对 (A,Z] 的系数 α_n=v(n)/sqrt(n)，有

\[
 \sum_{A<n\le Z}|\alpha_n|^2
 \ll_\delta Z^{2\delta}\log(2Z).
 \tag{3}
\]

例如二矩的一个额外 log 和 (3) 的 log 都由先选足够小的 δ 与最后的 ε 支付。这一步明确供应 Type I 的二矩，不将它记为免费 X^ε。

## 3. 较低长度块先付款

取

\[
 Y=X^{5/6},\qquad
 U=V=\lfloor X^{1/8}\rfloor,\qquad D=UV\le X^{1/4}.
 \tag{4}
\]

T 足够大时 U,V≥2、U<sqrt(X)<Y。令

\[
 L_Y(t)=\frac1{a_\ell\ell}
 \sum_{\sqrt X<n\le Y}\frac{\Lambda(n)}{\sqrt n}n^{it}.
\]

平方后的实际有限系数为

\[
 L_Y(t)^2
 =\frac1{(a_\ell\ell)^2}
 \sum_{n\le Y^2}\frac{c_Y(n)}{\sqrt n}n^{it},
 \quad
 c_Y(n)=
 \sum_{\substack{ab=n\\\sqrt X<a,b\le Y}}\Lambda(a)\Lambda(b).
 \tag{5}
\]

精确有 |c_Y(n)|≤τ(n)(log Y)²；这保留了原 lower cutoff，而不是换成一个无限 Λ*Λ。以 (2)、(3) 应用于平方，Z≤Y²，得

\[
 \|L_Y\|_{4,T}^4
 \ll_\varepsilon (1+Y^2/T)X^\varepsilon
 \ll_\varepsilon X^{2/3+\varepsilon}.
 \tag{6}
\]

最后一个等式使用原 T=2πX。此处没有正半素数计数当成 signed 上界；直接估计原平方的完整时间 L2 范数。系数二范数、均值误差及日志都已列明。

## 4. 原高段的精确 Vaughan 恒等式

定义

\[
 g_{U,V}(d)=-
 \sum_{\substack{ab=d\\a\le U,\ b\le V}}\Lambda(a)\mu(b),
 \qquad
 b_V(k)=\sum_{\substack{d\mid k\\d\le V}}\mu(d).
 \tag{7}
\]

对 n>U，逐系数恒等式为

\[
 \Lambda(n)=
 \sum_{d\mid n}g_{U,V}(d)
 +\sum_{\substack{d\mid n\\d\le V}}\mu(d)\log(n/d)
 -\sum_{\substack{mk=n\\m>U,\ k>V}}\Lambda(m)b_V(k).
 \tag{8}
\]

g 支撑 d≤UV。直接验证可在 Re(s)>1 使用有限 F=Σ_{m≤U}Λ(m)m^{-s}、G=Σ_{d≤V}μ(d)d^{-s} 和 Dζ=−ζ'/ζ：

\[
 D_\zeta=
 F-\zeta FG-\zeta'G+(D_\zeta-F)(1-\zeta G).
 \tag{9}
\]

右边展开后确切等于 Dζ。最后因子 1−ζG 的 k≤V 系数全零；k>V 的系数为 −b_V(k)。因此 (8) 的最后负号和 k>V 域是原对象，不是新增角色掩码。n>U 后 F 的系数为零。

于是原高段 \(Y<n\le X\) 的 Λ scalar 精确分解为 I₂+I₃+C₄，其中

\[
 I_2(t)=\frac1{a_\ell\ell}
 \sum_{d\le UV}\frac{g_{U,V}(d)}{\sqrt d}d^{it}
 \sum_{Y/d<r\le X/d}\frac{r^{it}}{\sqrt r},
\]
\[
 I_3(t)=\frac1{a_\ell\ell}
 \sum_{d\le V}\frac{\mu(d)}{\sqrt d}d^{it}
 \sum_{Y/d<r\le X/d}\frac{\log r}{\sqrt r}r^{it},
\]
\[
 C_4(t)=-
 \frac1{a_\ell\ell}
 \sum_{\substack{m>U,\ k>V\\Y<mk\le X}}
 \frac{\Lambda(m)b_V(k)}{\sqrt{mk}}(mk)^{it}.
 \tag{10}
\]

所有不等号按原实数 cutoff 的整数集合解释。U,V 向下取整不会产生边界余项；(8) 对这些精确整数值成立。

## 5. 原 sharp Type I 的点值与二矩

将 (Y,X] 分为 \(N<n\le\min(2N,X)\)，取 N=2^jY；每个块 N≥Y，块数 O(log X)。对应 inner r 是 \((N/d,\min(2N,X)/d]\)。令 R=N/d。

原相位是 \(f(r)=t\log r/(2\pi)\)。在任意这样的子区间，

\[
 |f''(r)|\asymp T/R^2
 \quad(t\in J_T).
\]

Theorem 16.7 给所有 partial endpoints 的统一界

\[
 \left|\sum_{r\in A}r^{it}\right|
 \ll \sqrt T+\frac R{\sqrt T}
 \tag{11}
\]

（若右边大于项数，仍是合法的 trivial majorant）。不是只证明一个光滑 inner sum。权 r^{-1/2} 或 r^{-1/2}log r 在该块的 supremum 加总变差≤C R^{-1/2}(log X)^j，j=0 或 1。逐项 partial summation 因而给

\[
 \left|\sum_{r\in A}r^{-1/2}(\log r)^j r^{it}\right|
 \ll R^{-1/2}(\log X)^j
       \left(\sqrt T+\frac R{\sqrt T}\right).
 \tag{12}
\]

这同时支付真实 sharp 下端和上端，不要求 cutoff 为整数，也不补一个未付 endpoint polynomial。

乘外部 d^{-1/2} 后，右边是

\[
 (\log X)^j\left(\sqrt{T/N}
                         +\frac{\sqrt N}{d\sqrt T}\right).
\]

因 N≤X≈T、d≥1，第二项由第一项的固定倍控制。又
|g(d)|≤τ(d)log(2d)，因此

\[
 \sum_{d\le D}|g(d)|\ll_\delta D^{1+\delta}\log(2D),
 \qquad \sum_{d\le V}|\mu(d)|\le V.
\]

加总原有限块，并保留 a_ell≥c，得

\[
 \sup_{t\in J_T}|I_2(t)+I_3(t)|
 \ll_\varepsilon X^\varepsilon D\sqrt{T/Y}
 \ll_\varepsilon X^{1/3+\varepsilon}.
 \tag{13}
\]

独立支付二矩：I₂ 的 n 系数≤log(2n)τ₃(n)，因为
Σ_{d|n}τ(d)=τ₃(n)；I₃ 的系数≤τ(n)log(2n)。它们支撑 Y<n≤X。按 (3) 加上原 (a_ell ell)^{-1}，系数能量≤X^{2δ}log X；(2) 的均值乘子为 O(log X)，因为 Z=X、T=2πX。所以

\[
 \|I_2+I_3\|_{2,T}^2\ll_\varepsilon X^\varepsilon.
 \tag{14}
\]

给定最终 ε 后，在 (13)、(14) 分配更小固定损失。以 sup²×L2² 得完整 Type I 四矩付款

\[
 \boxed{\ \|I_2+I_3\|_{4,T}^4
                  \ll_\varepsilon X^{2/3+\varepsilon}.\ }
 \tag{15}
\]

它是实际系数、完整 N≥Y 范围和整个 J_T 的估计，不仅 generic 参数代入。

## 6. 返回原 genuine primes：已证的完整归约

按 (5)、(10)，原两 sharp endpoints 的 Λ 版本恰为

\[
 \widehat P_H=L_Y+I_2+I_3+C_4.
 \tag{16}
\]

冻结 proper-power 准入给原完整
\(\|\widehat P_H-P_H\|_{4,T}=O(X^{-1/12})\)。
这个范数误差保持所有 prime powers；本稿不在未知增长下将两第四矩差删为 additive o(1)。

由 (6)、(15) 与 Minkowski，对于每个固定 ε>0，

\[
 \|P_H-C_4\|_{4,T}
 \ll_{\phi,\varepsilon}X^{1/6+\varepsilon}.
 \tag{17}
\]

定义实际剩余
\(\mathcal M_{C_4}=T^{-1}\int_{J_T}|C_4(t)|^4dt\)。
再次分配 ε，再以 (a+b)^4≤8(a^4+b^4)，严格得

\[
 \boxed{\quad
 \mathcal M_T\le 8\mathcal M_{C_4}
                +C_{\phi,\varepsilon}X^{2/3+\varepsilon}.
 \quad}
 \tag{18}
\]

同样有反向
\(\mathcal M_{C_4}\le8\mathcal M_T+C_{\phi,\varepsilon}X^{2/3+\varepsilon}\)。
这是 norm coupling 的有限原对象结论，不是两个第四矩 additive 等同，也没有供应 M_C4 的新有用上界。与 476 的 5/7 相比，已付款部分的 2/3 严格更小，差为 1/21；原整个 scalar 的已证上界目前仍是 476。

### 6.1. 固定 cut 的精确 tradeoff

同一证明可取任意先固定的 \(0<a<1/4\)，令

\[
 U=V=\lfloor X^a\rfloor,\qquad
 Y=X^y,\qquad y=\frac{2+4a}{3}.
 \tag{18a}
\]

此时 \(2/3<y<1\)，所有 sharp 区间、floor 和系数域仍满足上述前件。
低块 (6) 的幂为 \(2y-1\)；Type I 的 sup 成本是
\(X^{2a+(1-y)/2+\varepsilon}\)，二矩仍已付 \(X^\varepsilon\)，
故其第四幂成本是 \(4a+1-y\)。两者恰相等：

\[
 2y-1=4a+1-y=\frac{1+8a}{3}.
 \tag{18b}
\]

原选择 \(a=1/8\) 给 \(y=5/6\)、幂 \(2/3\)；
\(a=1/7\) 给 \(y=6/7\)、幂 \(5/7\)。
所以固定 \(a<1/7\) 可让已付子项严格低于 476 的 \(5/7\)。
与此同时剩余 C₄ 改为所有 \(m>U,k>V,Y<mk\le X\) 的实际系数；
减小 a 扩大了其允许因子范围，不能把原未付 C₄ 上界视作随 a 自动统一。
这说明 cut choice 的成本取舍，没有证明新的 whole exponent。

## 7. 原 Type II 的真正障碍与下一算术对象

(10) 的 b_V(k) 是实际 truncated divisor Möbius 系数；不能改成任意 μ(k)，也不能扔掉 Y<mk≤X 的共同 product mask。

例如 p,q 是均大于 U,V 的不同素数：

- n 为大素数时 C₄ 的系数为零，I₃ 的 n 系数为 log n；
- n=pq 时 I₂ 系数为零，I₃ 为 log p+log q；
- C₄ 两个 ordered 因子贡献 −log p−log q，因此合计 Λ(pq)=0。

p² 情形 C₄ 只有 −log p，和 I₃ 的 2log p 返回 Λ(p²)=log p。可见这里的 prime/composite cancellation 不是人为剥离的额外模型。

当 m,k≈sqrt(X) 且二者为素数时 b_V(k)=1；这个实际 sector 没有 small factor。它的四矩已是两 prime factors 的 eighth-degree joint mean，不能以各因子的已付 fourth moment 或 small-twist theorem 直接相乘。上述 sector 只定位剩余，**不作为 whole C₄ norm 的下界**；不同 sector 和 Type I 的带符号相消仍须保留。

具体 logarithmic phase 对通用 Type-II Cauchy 差分完全退化：

\[
 (mj)^{it}\overline{(mk)^{it}}=(j/k)^{it}.
 \tag{19}
\]

m 的导数为零；共同 product endpoints 只改变 m 的 interval。这与 additive e(αmn) 双线性不同，不能拿原 t≈X 的非零二阶导数给该差分免费付款。

核对 [Guth–Maynard 原论文](https://arxiv.org/html/2405.20552v2) Theorem 1.1 的实际范围：完整 prime polynomial 长度≈X、height≈X 不在其声明的新增改善区域 N≤T^{5/6−ε}。balanced factor 长度≈sqrt(X) 虽满足较短长度，但这里只知道单一 large-value theorem，未付款两个原系数共同八次矩及其全 product masks；尤其高幅层 σ>4/5 不是该定理的新增改进区。这是具体前件未满足，不是方法不可能性定理。

同样，[Heap 的长 Dirichlet polynomial 研究](https://arxiv.org/abs/2201.02108) 明确假设 RH 和受限制的 transform weights，不能由原 [Rθ] 加两 sharp cutoffs 免费调用。

当前最窄实际目标是 (10) 的**完整带符号** mixed mean：Λ(m) 与 b_V(k) 的所有 dyadic aspect ratios、共同 Y<mk≤X、原 positive-height J_T。只估计 balanced positive count、改变成小因子家族或丢共同边界，均不支付 (18)。本稿没有证明该目标；不将这个明确剩余接口称作新的 whole-chain 认证。
