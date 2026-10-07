# 指定 determinant 算术参考与真实相关条件：全文独立审查

2026-10-07。root。
被审稿：[physical determinant average](hybrid-physical-determinant-average-research.md)，
canonical LF SHA256
4dcd7bf85ffb4a697f51a8c5160480b120dfe0f4c0d249ba817f76ed9e38a5d6，
17559 bytes、441 行。

结论：**PASS，限定于指定参考的 fixed-cell 费用及条件接入。**
没有证明 actual 四 Λ correlation、小四矩或新的零点比例。
全文保持明确 [T]/[O] 区别；审查没有把主项模型当作已证明的 prime asymptotic。

## 1. 实际 pooling 和参考定义

先用原 divisor completion 得 Λ(a)Λ(b)Λ(c)Λ(d)，再按 n=bc、h=ad−bc
聚合，(6)–(7) 是 finite sum 的准确重排。
原 masks、六窗、same-atom subtraction 和 proper powers 均保留。
这是一个 fixed balanced cell，不自动覆盖完整 four-word response。

连续 (a,b,n,h) 变换的 Jacobian 为 1/(ab)；
prefactor 1/√abcd=1/√[n(n+h)]，故 (8) 正确。
连续 reference 按原 m0 的有限几何 cuts 定义，不把 integer gcd 平滑化。
四个 unit variables 的 determinant count 在 p|h 时为 (p−1)³，
在 p∤h 时为 (p−1)²(p−2)。
用 p/(p−1)⁴ 归一后确实得到 twin-prime 形状的 local factor。
这只指定参考；它不证明该参考是实际主项。

## 2. 算术平均和 BV

Euler product 中
1+1/[p(p−2)]=(p−1)²/[p(p−2)]，
所以 Σα(d)/d=C₂⁻¹。α(d)≤3τ(d)/d 足以给
Σ_(d≤R)α(d)=O(log²R)、Σ_(d>R)α(d)/d=O(log R/R)。
floor(R/(2d)) 求和的主项为 R，累计 remainder O(log²R)。
Abel 的 (15) 是 prefix cancellation；逐 h 取绝对值不保留它。

在固定正 compact cell，ρ 的 sup 和 h-BV 均为 O(1/N)。
每个原 factor/aperture cut 随 h 只跨固定次数，log d 的 derivative 为 O(1/N)；
对 a,b 的 da db/(ab) 总质量 O(1)。对 n-BV，固定 t 后
c/d=a/(be^(t/X)) 不随 n 变化，γ_n 的 variation 为 O(1/X)。
这些论证覆盖正文定义的有限 cuts；并不适用于任意新 ghost mask。

## 3. finite carrier 与 continuum

在 |t|≤C₀X<Q/2，无 alias。
对原有限 geometric sum 求导必须保留 carrier；
|K′|=O(1/|t|) 的总 variation 为 O(L)，不是错误的 O(1/t²)。
weighted endpoint geometric sums 给 shell averages κ₀=O(M⁻²)、
κ_j=O(R_j⁻²)；中央 sine antiderivative 的 t=0 端点准确为 0。
相应 Kcent 的全部跳跃和 L¹ 费用也已支付。

h 的 BV lattice error 每 n 为 O(L/N)，总 O(L)。
n 的进一步 quadrature error O(L/X)；h=0 删除 O(1)。
连续 raw response 的 Gram identity 保留全部有限 k 和真实 carrier。
a-slice integration by parts 的 derivative 与有限 sharp edges 付
O(√Y/|τ|)，之后 b-integral O(√Y)，
故 raw continuum O(Y²/X²)=O(N/X²)。
没有在一个只有 O(1) 整数的 affine fiber 上使用连续 PNT。

continuous log-frequency density ≤O(N/X)=O(H)，
共同 κ subtraction 为 O(H/M)。
所以 (26) 为 O(L³+N/X²+H/M)。
在本文原 236/239 partition M=max(H,Y/H)=H 下是 O(L³)；
换成 M=1 时不再是该小量，不能忽略这项。

## 4. 条件与共同中心化

actual-minus-specified-reference measure 先按 |Xlog(1+h/n)| pooling。
每个原 shell 的累计差再减 total mass 的线性 ramp，
准确等于应用原共同 constant-density projection，不随 n,h/channel 改变。

在 Stieltjes convention 下，低端采用累计函数的左极限 0，
高端 centered cumulative 为 0。
因此 endpoint atoms（如实际 atom 正好位于 shell edge）仍可按原 partition
只计一次；不能错误地要求低端右极限也为 0。
在该一致 convention 下，正文无边项的 integration by parts 正确，
每个 dyadic shell 付 O(e_j)，中央付 O(e₀log(2M))。
于是 (28) 是 (29) 的充分算术条件。

这个条件要求所有 curved physical prefixes 的实际 four-Λ 差异，
完全没有由 one-point zero-free/PNT package 支付。
指定参考的 O(L³) 不能把未证 e_j≪L² 改称为 actual saving。
正文保留这一准确限定。

## 5. 支撑障碍和适用边界

balanced n=bc 且 n≡0 mod3 时，Λ(b)Λ(c) 非零必须有因子 3^k。
balanced range 只有 O(1) 个这样的 k，所以对应 n 只有 O(Y)，
而一个固定 interior n 区间含 Θ(N) 个 n。
如果连续参考在该 scaled rectangle 正，则许多 n 完全无 actual support，
它们的 uncentered reference mass 各有固定正下界。
因此正文否定的逐 n uncentered absolute 方案确实费 Ω(N)。
这不否定所有 centered per-n 或真正联合 dispersion。

可以登记：指定全几何/局部除数 reference 的有限费用已付、
原 pooled correlation 有一个明确新充分条件。
不能登记：actual fixed-cell o(L⁴)、all-cells/alias、
full signed fourth budget 或新的比例。本审查未运行外部 kernel。
