# 453：原低素数压缩的显式一侧四矩常数

2026-10-07。状态：新推导待独立审查。没有新的零点比例或无零边界。

本稿将 [448 §5](448-canonical-type-i-admission-finite-gram-and-low-prime-fourth-norm.md)
在 Z=√X 的未优化 O(N) 四范数界细化为显式常数。
保留原 AF finite frame、sharp prefix 和 normalizer，证明

\[
 \limsup_{T\to\infty}
 \frac{a_L^3}{N(T,2T)}
     \operatorname{Tr}P_{\le X^\rho}^4\le3\rho^4,
 \qquad 0<\rho\le\frac12.
 \tag{1}
\]

ρ 和原 profile 在 T 前固定。a_L=||φ_L||₂²/L 最终离零。
如果 a_L→a∞，右边可改写为
limsup Tr P⁴/N≤3ρ⁴/a∞³。
在原 flat window 的合法光滑 taper 极限 a∞=1、ρ=1/2，
这给 **3/16**；是实际低通道的 upper budget，不是其 exact 主项。
高低 mixed words、四 distinct primes 和完整背景仍开放。

## 1. 对象和引用范围

使用与 [452](452-subquarter-padding-and-fourth-trace-stability.md)
相同的 L=log(T/(2π))、X=e^L、αₖ=T+2πk/L、
D_T=⌊XL⌋ 及 N=N(T,2T)∼TL/(2π)。
φ_L 是原 AF C² compactly supported taper，support⊂[−L/2,L/2]，
0≤φ≤1、原二阶 Fourier 尾的常数统一；
a_L 最终有固定正下界。只需要 D_T∼N，不采用 D_T=N+O(L)。

令 Z=X^ρ，首先只取 genuine primes：

\[
 Q_Z(t)=\sum_{p\le Z}\frac{\log p}{\sqrt p}\,p^{it},
 \qquad M_Z(t)=-\pi^{-1}\operatorname{Re}Q_Z(t).
 \tag{2}
\]

fₖ(t)=\(\widehat\phi(t-\alpha_k)\)，
(Uz)(t)=Σₖzₖfₖ(t)，F=U/√(2πL)。原 Plancherel 和 support 内
critical grid 正交性给 F*F≤I。保留原有限压缩

\[
 P_Z^{\rm pr}=\frac{2\pi}{a_LL}F^*M_ZF.
 \tag{3}
\]

最后才加入 n=p^j≤Z、j≥2 的 proper powers，得到原 Λ cutoff
P_{\le Z}。不把 (3) 换成独立符号的平均，也不删除 finite carrier。

只用经典 Chebyshev/Mertens 界、weighted Hilbert mean value、
原 AF frame 恒等式与 C² Fourier 尾。
Hilbert 输入可见 [AF v2 Lemma 2.2 和 (2.12)](https://arxiv.org/html/2608.13637v2)
所列 Montgomery–Vaughan 不等式，原文书目 [MV74]：
H. L. Montgomery and R. C. Vaughan, *Hilbert's inequality*,
J. London Math. Soc. (2) 8 (1974), 73–82。
本稿不调用 7/8、σ*、RH 或新的四点相关。

## 2. Q² 的加权误差比 length×mass 界更小

记 b_p=(log p)/√p，

\[
 S_Z=\sum_{p\le Z}b_p^2
     =\frac12\log^2Z+O(\log(2Z)),\qquad
 R_Z=\sum_{p\le Z}(\log p)^2\ll Z\log(2Z).
 \tag{4}
\]

第一式由原 Λ²/n 的 Mertens 估计减去收敛的 proper-power 总费；
第二式由 log p≤log Z 和 Chebyshev。
Q_Z²=Σₙcₙn^{it}，n≤Z²。
unique factorization 给 c_(pq)=2b_pb_q（p≠q）、c_(p²)=b_p²，因此

\[
 \sum_n|c_n|^2=2S_Z^2-\sum_{p\le Z}b_p^4
             =2S_Z^2+O(1),
 \tag{5}
\]

\[
 \sum_n n|c_n|^2
 =2R_Z^2-\sum_{p\le Z}(\log p)^4
 \ll Z^2\log^2(2Z).
 \tag{6}
\]

不能将 (6) 替换成 Z²Σ|c|² 后还保留显式主常数。
对全部整数频率 log n 的间隔 δₙ≥1/(2n)，weighted Hilbert
对两个 endpoint 各给 O(Σₙ|cₙ|²/δₙ)。
所以任意实起点 A 和长度 H≥0 都有

\[
 \int_A^{A+H}|Q_Z(t)|^4\,dt
 =H\!\left(2S_Z^2-\sum_pb_p^4\right)
  +O(Z^2\log^2(2Z)).
 \tag{7}
\]

常数与 A 无关，不以时间起点≈0替代真实高度 T。
Z²≤X∼T 时，(7) 的 error 为 o(TL⁴)，包括 endpoint ρ=1/2。

## 3. 实部四矩的所有不平衡项

scalar expansion 为

\[
 (\operatorname{Re}Q)^4
 =\frac38|Q|^4+\frac12\operatorname{Re}(Q^3\overline Q)
  +\frac18\operatorname{Re}(Q^4).
 \tag{8}
\]

后两项必须实际付费，不能从 complex fourth moment 直接套入高斯系数。

### 3.1 四个同号

Q⁴ 中每个频率 log(p₁p₂p₃p₄)≥log16。
任意 interval 的 exponential integral 至多 2/|frequency|，
而 Σₚ≤Z(log p)/√p≪√Z。因此

\[
 \left|\int_A^{A+H}Q_Z(t)^4\,dt\right|\ll Z^2.
 \tag{9}
\]

这与 H 无关，仍保留真实 endpoint phases。

### 3.2 三正一负的近整数 gap

令

\[
 C_3(n)=
 \sum_{\substack{p_1p_2p_3=n\\p_j\le Z}}
 (\log p_1)(\log p_2)(\log p_3).
 \tag{10}
\]

Q³\(\overline Q\) 的原系数是
C₃(n)(log p)/√(np)、phase log(n/p)。
n 不可能等于 prime p；这里允许 p₁=p₂ 或三个全相同，
仍不会发生 n=p 的 diagonal。

Chebyshev 迭代及 Σₚ≤y(log p)/p≪log(2y) 给

\[
 \sum_{n\le y}C_3(n)\ll y\log^2(2y).
 \tag{11}
\]

证明：去掉 pⱼ≤Z 限制只增加 positive 总和，再先对第三个 prime
用 Θ(y/(p₁p₂))≪y/(p₁p₂)，最后付两个 prime harmonic sums。

分 near region p/2≤n≤2p 和其余部分。
near 中 n≤2Z，p∼n，整数 gap 非零，且
1/|log(n/p)|≪n/|n−p|。因此对每个 n

\[
 \sum_{\substack{p\le Z\\p/2\le n\le2p}}
 \frac{C_3(n)\log p}{\sqrt{np}\,|\log(n/p)|}
 \ll C_3(n)\log(2Z)
       \sum_{\substack{1\le m\le Z\\m\ne n}}\frac1{|n-m|}
 \ll C_3(n)\log^2(2Z).
 \tag{12}
\]

把 prime sum 放大成所有整数只是本误差的上界，
没有把 actual Λ coefficient 改成 independent mask。
(11) 求和给 O(Z log⁴(2Z))。
far 中 |log(n/p)|≥log2，直接使用
ΣₙC₃(n)/√n=(Σₚb_p)³≪Z^(3/2)
及 Σₚb_p≪√Z，得到 O(Z²)。
所以

\[
 \left|\int_A^{A+H}Q_Z(t)^3\overline{Q_Z(t)}\,dt\right|
 \ll Z^2+Z\log^4(2Z).
 \tag{13}
\]

不使用 twin primes 或三个乘积与第四个 prime 的渐近。
在 endpoint Z=√X，此类全部非对角费用仍是 o(TL⁴)。

## 4. 真实有限压缩的 scalar Jensen majorant

合并 (7)–(13)，对固定 0<ρ≤1/2、H=O(T) 有

\[
 \int_A^{A+H}(\operatorname{Re}Q_Z(t))^4\,dt
 =\frac34 H S_Z^2
  +O(H+Z^2\log^2(2Z)+Z\log^4(2Z)).
 \tag{14}
\]

由 (4)，主系数是 (3/16)H log⁴Z，error 可写
O(H log³(2Z)+Z²log²(2Z)+Zlog⁴(2Z))。

取 (3) 的任一单位 eigenvector v，令 λ=〈v,F*M_ZFv〉。
measure |Fv|²dt 的总质量≤1，缺失质量放在 0，
scalar Jensen 给 λ⁴≤∫M_Z⁴|Fv|²。
对原有限维 eigenbasis 求和得到

\[
 \operatorname{Tr}(P_Z^{\rm pr})^4
 \le\frac{8}{\pi a_L^4L^5}
     \int_{\mathbb R}
          \left(\sum_{0\le k<D_T}|f_k(t)|^2\right)
          (\operatorname{Re}Q_Z(t))^4\,dt.
 \tag{15}
\]

这不需要 x⁴ 的 operator convexity，也不是把压缩的四迹当成符号四矩。
原 infinite-grid identity 给 Σfinite|fₖ(t)|²≤a_LL²。

先在 T 前固定 0<ε<1/4，再取
Jε=[(1−ε)T,(2+ε)T]。其长度为 (1+2ε)T。
在 Jε 用 (14) 及点态 finite-grid bound，得到

\[
 \operatorname{Tr}(P_Z^{\rm pr})^4\big|_{\rm positive\ majorant,\ J_\epsilon}
 \le\frac8{\pi a_L^3L^3}
       \left(\frac3{16}(1+2\epsilon)T\log^4Z+o_\epsilon(TL^4)\right).
 \tag{16}
\]

这里只将 (15) 的 positive integral 分割；没有把 matrix fourth
拆成两个各自四次迹而丢掉 cross terms。
Jε 外保留 |Q_Z|≪√Z。原 Fourier 尾对每个 αₖ 的距离至少 εT 给

\[
 \sum_k\int_{J_\epsilon^c}|f_k(t)|^2dt
 \ll_\epsilon D_TT^{-3}.
 \tag{17}
\]

外侧 (15) 的全部费用是 Oε(Z²/(T²L⁴))=o(N)。
它包括 t≈0，未偷用 t∼T 的素数相消。

现在 log Z=ρL、N∼TL/(2π)，(16) 的正规化因子精确给

\[
 \frac{a_L^3}{N}\operatorname{Tr}(P_Z^{\rm pr})^4
 \le3\rho^4(1+2\epsilon)+o_\epsilon(1).
 \tag{18}
\]

先 T→∞，再 ε→0 得 (1) 的 prime-only 版。
ε 固定时 (17) 的常数允许依赖 ε；
不把 ε_T→0 代入而忽略 C² 尾常数。

## 5. 原 Λ prefix 的 proper powers 与非交换 transfer

令 Q_Z^pp=Σ_{p^j≤Z,j≥2}(log p)p^(−j/2+ijt log p)，
E_Z^pp 按同一个 (3) 压缩。
全高度的绝对 bound 为

\[
 |Q_Z^{\rm pp}(t)|
 \le\sum_{p\le\sqrt Z}\frac{\log p}{p}
     +\sum_{p,j\ge3}\frac{\log p}{p^{j/2}}
 \ll\log(2Z).
 \tag{19}
\]

Bessel 因子 1/L 给 ||E_Z^pp||op=O(1)。
其 squared coefficient mass Σ_(p,j≥2)(log p)²/p^j 收敛。
weighted Hilbert 对原 prime-power 整数频率的 error 至多
O(Σ_(p^j≤Z,j≥2)(log p)²)≪√Z log²(2Z)。
因而 ∫_(Jε)|Q_Z^pp|²=Oε(T)。

原 scalar squared Jensen 和 (17)（Jε 外仍保留 (19)）给

\[
 \operatorname{Tr}(E_Z^{\rm pp})^2\ll N/L^2,\qquad
 \operatorname{Tr}(E_Z^{\rm pp})^4
 \le\|E_Z^{\rm pp}\|_{\rm op}^2
       \operatorname{Tr}(E_Z^{\rm pp})^2
 \ll N/L^2=o(N).
 \tag{20}
\]

对 Z≤√X，以上常数统一。没有把 arbitrary subsequence 的取消
从完整 pp sum 免费移植；(19) 与 mean value 均直接针对此 sharp cutoff。

(18) 已先证明 ||P_Z^pr||₄=O(N^(1/4))，所以在同一原低通道
P_≤Z=P_Z^pr+E_Z^pp 上，Minkowski 与非交换 telescoping/Hölder 给

\[
 |\operatorname{Tr}P_{\le Z}^4-
           \operatorname{Tr}(P_Z^{\rm pr})^4|=o(N).
 \tag{21}
\]

这里不需要假设完整高低 response 的四范数有界；
它只用于已独立界定的 low matrix，故没有 circular fourth-moment input。
由 (21)，(1) 对原 Λ cutoff 成立。

## 6. 得到了什么，尚未得到什么

相比 448 的 coarse O(N)，本稿为原低 Λ channel 提供显式一侧常数，
并在 product length Z²=X 的 endpoint 支付 weighted offdiagonal。
它没有宣称压缩的 exact main term 是 3ρ⁴/a∞³：
scalar Jensen 可以损失 finite support 的具体路径几何。
MT 或其他 profile 的 a∞ 不等于 1，不能直接沿用 flat 的 3/16。

即使高 prime repeated sector 也被独立支付，其费用不能与本常数
简单相加就算出完整 B₄。真实
Tr(P_low+P_high+A)^4 包含 low/high mixed terms、four-distinct high
words 和 A 的全部 mixed terms；原 signed finite carrier 与 cross-cell/alias
必须保留。需要先付这些净费用，才可以接入 197 的四矩惯性比例链。

本轮没有新比例，没有新无零边界；因此没有追加“新边界”论文。
新的 [精确有限审计](../scripts/hybrid_prime_sector_exact_audit.py) 与
[输出](../output/hybrid-prime-sector-exact-audit.json) 分别检查 cyclic
partition、prime-product coefficient collisions、indicator 积分和指定
local determinant factors；不认证均值、无限素数或实际四点相关。
下一项可行动问题是用实际路径窗口细化 low 的 one-sided 常数，
或控制全 distinct/mixed physical response 的净主预算。
