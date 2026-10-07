# 原短载体比值方差到标量四阶矩的完整准入

2026-10-08。基线 2681813154243e10cf4602f4e88514355060d379。
本次继续原域的短载体路线，新增原 shared spatial window 到一个原系数、
未移位 scalar high 四阶矩的一侧上界接口。没有得到该四阶矩的新算术上界。

## 1. 全文来源及审查

canonical UTF-8 LF 仅统一 CRLF/lone CR，不 trim 或改变 EOF。

| 完整来源 | SHA256 |
|---|---|
| [新 scalar 准入研究](../reviews/2026-10-08/hybrid-short-carrier-canonical-scalar-fourth-admission-research-radial.md) | f04279a9de54303d772859b2ee5e05010567404c53143c928a14e905eb51a0d7 |
| [原全部四阶 P 与 ratio 桥](472-original-short-carrier-fourth-compression-and-ratio-variance.md) | 9856885e932a892cf7c33ece82f430c2ec13004555eb52da2f1e8b1ec6bb2683 |

新源已有 [twisted 全文独审](../reviews/2026-10-08/hybrid-short-carrier-canonical-scalar-fourth-admission-review-twisted.md)
及 [compression 全文独审](../reviews/2026-10-08/hybrid-short-carrier-canonical-scalar-fourth-admission-review-compression.md)。
本笔记另由 [twisted 核对](../reviews/2026-10-08/474-original-scalar-admission-review-twisted.md)。
准入保留原 C² even taper、finite normalizer、half-Gram cross 和 472 的
共同载体选点；没有加入新的无零前件，也不把源中的 [O] 算术任务当成已付。

## 2. 真正支付的原窗口接口

取 X=T/(2π)、ℓ=log X，原 even taper φ，a_ℓ=||φ||₂²/ℓ，
原 genuine prime signal

\[
 P_H(t)=\sum_{\sqrt X<p\le X}
        \frac{\log p}{a_\ell\ell\sqrt p}e^{it\log p}.
\]

设 A 是原 high half，G=A* A，D_+ 是原 same-prime 项，R_+=G−D_+。
对原 E_σ 的每列 t_k=σ+2πk/ℓ，精确有

\[
 (GE_\sigma e_k)(u)=\ell^{-1/2}\phi(u)e^{it_k u}
 T_{\phi(u+\xi)}\!\left[
  \overline{T_{\phi(u-\xi)^2}P_H}\,P_H\right](t_k).
\]

两个关于 t 的真实 Fourier 乘子保留同一空间窗口。终端乘子是 L²
contraction，首乘子的 L⁴ 范数由总变差 V_ℓ=||(φ²)'||₁ 一致控制：
N_ℓ=(1+1/√2)V_ℓ=O(1)。源中自证所需 Hilbert transform 界。
全局 finite polynomial 先切到真实 Lᵖ 函数，不能直接套全实轴 norm。

依次使用正高度 guards [T,2T+s]、[T/2,3T]、[T/4,4T]，s=T/√ℓ；
C² kernel 的远尾 O(|v|^(−2)) 付清两次切窗费用。令

\[
 \mathcal M_T=T^{-1}\int_{T/4}^{4T}|P_H(t)|^4dt,
 \quad m_T=\sum_{\sqrt X<p\le X}\frac{\log p}{a_\ell\ell\sqrt p}.
\]

原 d=floor(Xℓ)、η=2π/ℓ 的 σ+k 平均有精确正高度密度，包含全部
endpoint strips。保留有限 prefactor 和可能增长的四阶矩，得到

\[
 A_T=\frac{a_\ell T}{2d\eta}(1+\eta/s),\quad
 E_T(M)=N_\ell\sqrt M+C_\phi(m_T/T)M^{1/4}+C_\phi m_T^2/T,
\]

\[
 \boxed{\operatorname{avg}_\sigma r_\sigma+S_T/2
 \le A_T E_T(\mathcal M_T)^2+C_\phi/\ell,}
 \qquad r_\sigma=\|R_+E_\sigma\|_{\rm HS}^2/d.
\]

这是对每个大 finite T 的增长一致上界。两尾量分别为
O(X^(−1/2)/ℓ) 与 O(ℓ^(−2))，首项仍乘 M^(1/4)，不能在未知增长下
擅自删成 additive o(1)。若将来支付 M_T=O(1)，才得到 avg r=O(1)
及相应原载体上界。窗口乘子没有额外 log log 增长费，也没有付 small-r。

## 3. 原截断的 Λ 卷积是具体下一算术任务

将 P_H 的 prime 系数替换为相同 sharp 截断的 Λ(n)，proper powers 在
normalized L⁴ 中为 O(X^(−1/12))。平方项用 base pq≤X 的 weighted
mean value；不能错误地按 p²q²≤X² 付该小量。

令 Y=√X、Λ_H=Λ 1_(Y<n≤X)、c_H=Λ_H*Λ_H。准确有

\[
 \widehat P_H(t)^2=(a_\ell\ell)^{-2}
       \sum_{X<n\le X^2}\frac{c_H(n)}{\sqrt n}n^{it}.
\]

在这个原范围内，完整 Möbius identity 为

\[
 c_H(n)=\sum_{d\mid n}\mu(d)\log^2(n/d)-\Lambda(n)\log n
 -2\sum_{\substack{ab=n\\a\le Y}}\Lambda(a)\Lambda(b)
 -2\sum_{\substack{ab=n\\a>X,\ b>Y}}\Lambda(a)\Lambda(b).
\]

最后的 upper-cutoff correction 在 n>X^(3/2) 可能非空，必须和 low
correction 一并保留。例如 X=16、n=95=5·19，末项正好删除原不允许的
19 因子。不能只估 μ*log² 就宣称估计了原列。

现在确切的充分目标是同一正高度窗的 signed mean-square

\[
 \frac1T\int_{T/4}^{4T}
 \left|\sum_{X<n\le X^2}\frac{c_H(n)}{\sqrt n}n^{it}\right|^2dt
 \le B_\phi(a_\ell\ell)^4,\qquad B_\phi=O(1),
\]

或更好的显式预算。Möbius 和两项 corrections 须共同估计；逐项取绝对值
不能付款所需 cancellation。顶块仍为原 balanced 两个大素数因子，长度
X²、高度 O(X)。直接 weighted mean value 只给 M_T≪1+X/ℓ²。
现有 shorter-polynomial large-value 改善没有自动覆盖原顶块。

## 4. 当前范围与复核

本次已付完整空间窗口到 canonical scalar fourth 的准入、正高度两级
guard、有限采样与增长费用、proper powers，以及两个 factor 截断的
精确完成。它是一侧充分接口，没有证明两个观测量双向相等。
具体 scalar 算术上界、实际比例或无零区域的改善仍未付。

[精确检查器](../scripts/hybrid_scalar_fourth_admission_checkpoint.py) 核对
finite frequency、采样重叠、尾幂和 formal prime-log 卷积。
[输出证书](../output/hybrid-scalar-fourth-admission-checkpoint.json) 记录
来源和独审绑定；finite algebra 不替代 Lᵖ 分析或素数均值证明。
