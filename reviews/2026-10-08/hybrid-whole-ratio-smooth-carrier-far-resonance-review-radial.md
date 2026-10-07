# 原完整 ratio 的正光滑短载体 far 证书：独立全文审查

2026-10-08，radial。结论：限定 PASS。
只新建此审查文件；没有修改被审作者源、旧冻结材料、math、Git 或输出。
被审对象是原正光滑短载体的远共振付款，不是原四阶矩或 near 的完整上界。

## 1. 绑定与全文范围

canonical UTF-8 LF 仅统一 CRLF/lone CR，不 trim 或改变 EOF。
全文实读被审稿的 359 行：

| 来源 | SHA256 | bytes / lines |
|---|---|---|
| [被审完整 smooth-carrier 源](hybrid-whole-ratio-smooth-carrier-far-resonance-research-twisted.md) | 9b8c6064731f65eb4449a3e9da353077baa856a4cb27f93fd5063b6f6a578054 | 14285 / 359 |
| [已冻完整 short-carrier ratio 输入](hybrid-whole-short-carrier-ratio-and-distinct-criterion-research-twisted.md) | c7ff142ebe15232542626e4feda3c05a1285cbf7bff64f462e734c662dafea53 | 11396 / 276 |
| [228 原 moving-block 合同](../../notes/228-relative-dense-zero-block-transfer.md) | 2cc8a3f5eb0e66ef0a6306a317a1e2b03c046c62b8284a87ccbee8e8130181ae | 旧冻结输入 |

后两份亦实读全文，核对本稿引用的增长一致性、同一短载体、factor 2、
whole-P L¹ 误差与零侧 moving-block 的实际量词。
被审稿引用的 472/474 保持各自已冻结的作者证明及独审范围；
本次没有声称重证底层 AF 零侧 [R] 或完整旧论文。

## 2. 原 half-ratio、共同 u 与相位

被审 (3)–(4) 是原 R_+=A* A−D_+ 的完整 column 平方。
直接作用 A* A 于 E_σ e_k 可得到

\[
 (R_+E_\sigma e_k)(u)
 =L^{-1/2}\phi(u)e^{i(\sigma+k\eta)u}
   \sum_{p\ne q}c_{pq}(u)e^{i(\sigma+k\eta)\xi_{pq}}.
\]

φ、b_p 均实，c_{pq}≥0，所以展开 norm 时第二个因子取共轭只翻转
其指数；相位恰为 S=ξ_{pq}−ξ_{p'q'}，不为两者之和。
式 (4) 因而保留同一个 u、每个 p≠q、p'≠q' 的完整 repeated/distinct
标签和全部 k。b_p 是原 log p/(a_L L√p)，没有替换 normalizer。

非零项中 z=u−log p∈I，且 v=z+log q=u+ξ_{pq}∈I。
high 条件 log q>L/2 强迫 v>0；log p>L/2 同样强迫 u>0。
因此 v,v'∈I_+，|S|≤L/2。这个论证确实用了两个 incoming high
prime，而非仅终端 φ 的长度；±L alias 被排除。

carrier 特征函数用正号 Γ_χ(z)=∫χ(v)e^{izv}dv，故平均相位
e^{iTS}Γ_χ(sS)K_d^0(S) 正确。绝对质量至多 m_H⁴/2 来自
I_+ 的长度 L/2 与所有 φ≤1；不要求四个素数互异或独立随机相位。
任意 tuple 子集的 (9) 都由这个完整质量上界得到。

## 3. 无限卷积确实产生固定正 C∞ 密度

逐项核验被审 (10)–(12)：

- a_n=1/[4n(n+1)]，Σa_n=1/4，第一宽度 a₁=1/8。
  平移后的所有有限卷积支撑于 [3/8,5/8]，非负、积分一且 ∞ norm≤8。
- uniform interval 的特征函数是 sinc(za_n/2)，因此分母准确为
  8n(n+1)，并有共同的中心相位 e^{iz/2}。
- 每个固定 z 的尾部差为 O_z(a_n²)，可求和。先固定 k>m+1，
  前 k 因子给 (1+|z|)^−k 可积 domination；Fourier inversion 使
  N≥k 的 χ_N 在 C^m norm 收敛。有限卷积的小 N 不需已有任意阶
  smoothness。极限由 compact support 和 uniform convergence 继承
  positivity、积分一、支撑与 ∞≤8。
- |z|≥256 时 N₀=floor(√|z|/8)≥√|z|/16；
  对 n≤N₀，8n(n+1)≤16N₀²≤|z|/4，故每个对应 sinc 模≤1/4。
  无限乘积的其余因子模≤1，于是
  4^−N₀≤exp(−√|z|/16)。

这是一份实际固定 profile 的解析构造，未用 N 或 profile 随 T
变化的导数常数。compact support 在合法窗口内部，无 carrier 扩宽。

## 4. 全部 far 的 absolute 小量和准确 near 宽度

独立代入 s=T/√L=2πX/√L 与 Δ_T=1024L^(5/2)/X：

\[
 s\Delta_T=2048\pi L^2\ge4096L^2,\qquad
 |\Gamma_\chi(sS)|\le X^{-4}\quad(|S|\ge\Delta_T).
\]

m_H≪√X/L，因此全标签 far mass≤C m_H⁴ X^−4
=O(X^−2 L^−4)。这是对 signed far contribution 的模作上界；
没有把整个 ratio square 改成一份 positive tuple kernel。
sharp far indicator 合法，因为原 prime sum 有限，不产生 Fourier gate
tail。一般固定 C∞ profile 只能给文中的相应 power-threshold 版本；
显式无限卷积才提供现在的 polylog near。

box 对照 (17) 也核对正确：无 alias 范围内 |K_d^0(S)|≪1/(X|S|)，
box sinc 另给 1/(s|S|)，因此为 L^−(7/2)Δ^−2。
此 fixed-order 界没有被冒充新的 stretched-exponential 衰减。

four-distinct half-ratio 的 A=qp'、B=pq' 在 (X,X²]，unique
factorization 给 A≠B。near 只将 determinant 宽度降到
O(XL^(5/2))，并未把 product 长度 X² 变成 X。
对 S=c/X，sS→0 和 Γ_χ(sS)→1 严格成立，证明真实自然 near 没被
此次合法短平均消掉。完整 near 上界仍未付。

## 5. Actual atoms 的 modulation 保留所有内部 P

这是本次需独立核验的关键实际对象。R_t f(u)=f(u+t)，所以

\[
 M_{e^{-i\sigma u}}R_tM_{e^{i\sigma u}}
 =e^{i\sigma t}R_t.
\]

M_φ 与 modulation 交换，E_σ=M_σE₀，因而被审 (18) 精确成立。
adjoint 把 direction ε 翻号，相位变为共轭，没有遗漏负 direction。
每个 C̃_{p,ε} 仍是原有限 E₀ 压缩，norm≤b_p。

四个有限矩阵相乘后，其三个内部 E₀E₀* 全部保留。由于每个
σ-dependence 恰为 scalar 相位，完整 tuple 只有
exp(iσΣ ε_j log p_j)。归一化迹的模≤乘子 norm 产品，即≤Πb_p。
这一步没有使 finite P 与 real-line Fourier projection 交换，也没有
调用 free cyclic physical trace。

任意 ordered H/L word、方向和标签子集的 far 直接由同一 X^−4
因子控制。有限 16 个 sign choices 只改常数；m_L、m_H 各自用
Chebyshev 粗上界，不需假设 m_L≤m_H 的精确次序。physical tuple
的 overlap/K_d 模≤1 也给同样付款，即使其他 physical word 存在 alias。
因而 (20) 是对原 actual 内部 P 的直接证明。

## 6. Weighted good set、[R] 和增长量词

χ 是 probability density 且 ∞≤8，所以非负误差的 χ 平均≤8 倍
原 box 平均。原 raw whole-P bridge 的 16 个 mean absolute word
errors O(L^−2) 全部继承。weighted Markov 得 μ_χ(G_T)≥1−O(L^−1)
与同一 G_T 上的全 16 词 O(L^−1)。这里没有声称 density support
本身具有全区间 Lebesgue measure 1−o(1)。

原 c7ff 输入 (8)–(13) 的 weighted HH centering、factor 2 和 repeated
union 对每个合法 carrier 一致，其误差不乘未知 q 或 high fourth。
因此 (23) 的 whole L¹ 桥可被 χ∞≤8 直接继承。
只传递 entire word 的 P error；被审稿明确没有把它任意拆给 near
单个标签，避免了一个实际常见的非法转移。

若未来有 signed near 平均 upper B_T，r≥0 才允许在 G_T 中选点。
也可直接对 q 使用 ∫_G q≤2∫r+∫|q−2r|，得到被审 (25)。
当 B_T 增长时 μ_χ(G_T) 的分母必须保留，不能吞为 additive o(1)；
原稿已经明确。点仍在 [T,T+s]，故 228 的 endpoint discrepancy
O(s log T)=o(N) 适用，不要求点的 Lebesgue density。

far 的新解析证明及 modulation 不需 [R] 或 bounded fourth。
把所选 carrier 用于原零侧比例账本仍须保留 AF 的原 tail、trace、
二矩、functional-equation pairing 及原同配置合同。
没有因使用正 χ 就免费得到新的惯性证书或新的实际比例。

## 7. 验收范围

限定 PASS 的新付款：固定正 C∞ profile 的构造及明确衰减；原
same-u half-ratio 无 alias；所有实际四 tuple 与原内部 P 的精确相位；
全 prime 范围、任意标签 far 的 O(X^−2L^−4)；以及原短 carrier
whole-P/good-point 输入的合法继承。

这不认证 near 上界、O(1) ratio、bounded q、高四矩常数、比例改善、
新的零自由区域、RH 或 Weil 上同调算术桥。被审作者稿未越过这些边界。
未发现需要修改该冻结源的数学阻断。
