# 475 原四阶增长幂与完整 far 入口：独立全文审查

2026-10-08，radial。结论：限定 PASS。
只新增本审查，不修改笔记、作者来源、旧冻结文件、math、Git 或输出。
被审摘要的作者为 root；本审查不是对 radial 自己的零点包来源重复宣称独审。

## 1. 最终对象和实读来源

canonical UTF-8 LF 仅统一 CRLF/lone CR，不 trim 或改变 EOF。

| 实读来源 | SHA256 | bytes / lines |
|---|---|---|
| [475 最终结果入口](../../notes/475-original-fourth-power-saving-and-whole-far-resonance.md) | cd295de4a909d82e50f8db4635d18cb3dfb9dffbbab8a5a4f00167aced1bf55b | 7592 / 158 |
| [固定起点完整采样源](hybrid-fixed-start-half-gram-sampling-research-root.md) | 7ed68a71d4d22d0bf1d90c61cef231534737188131aad9842669cd11f19c82cc | 7522 / 199 |
| [固定起点 compression 独审](hybrid-fixed-start-half-gram-sampling-review-compression.md) | 9f5b4b76bab1483cf0eee8607928f5b85b41feb3e14aa652c838416f37b68cf8 | 5786 / 119 |
| [root 对 power / far / 主质量的完整独审](hybrid-original-fourth-power-and-far-review-root.md) | 65a4e75ac9ca79dc2c9a2752902ec89acb968eae8c696ad4d54ab1148ec26f6c | 8377 / 137 |
| [全标签 actual far 完整源](hybrid-whole-ratio-smooth-carrier-far-resonance-research-twisted.md) | 9b8c6064731f65eb4449a3e9da353077baa856a4cb27f93fd5063b6f6a578054 | 14285 / 359 |
| [半素数主质量完整源](hybrid-canonical-semiprime-smooth-subtraction-and-variance-obstruction-research-compression.md) | 7fcb097ad17d77b7281acd1f7c7d0f1580c5519c015437e104823cdfabd52645 | 10722 / 212 |

原零点包来源
[8bcbd27da46d922d9e6e741fcf9a87012d565052f8d97b3ad12e99b3edbc2481](hybrid-positive-height-zero-packet-fourth-upper-research-radial.md)
是 radial 的已冻结作者证明，另由 root 上表逐行独审。
本次核摘要是否准确引用这一输入及其条带、cutoff、正常化和增长范围。
我的完整 far 独审另在
[独立报告](hybrid-whole-ratio-smooth-carrier-far-resonance-review-radial.md)，
SHA bab74da7a1416aeea7083f47d5e398e7164f8d6f511e821919b61d1c040aae0b。

全文实读原 158 行最终摘要及上表来源；没有以有限脚本 PASS 替代分析核对。

## 2. 条带、普通密度和 genuine sharp signal

475 §2 准确保留 X=T/(2π)、a_ℓ≥c_φ、√X<p≤X 两 sharp cutoffs
和正高度窗 [T/4,4T]。条带前件明确是 ζ 的全部非平凡零点 β≤θ，
固定 5/6<θ≤7/8。没有免费转用全 Hecke family 的相同密度。

摘要的 combined Perron 叙述保留两关键项：F=(x^z−y^z)/z 为整个核；
真实 critical zero 的 D-pole 仍贡献留数，所有 signed heights 与重数
保留。直接 twisted Perron 的避零双横边、principal、左线及端点费用
与作者源和 root 独审吻合。

中间 log³ 费用不是遗漏 harmonic tail：k=ℓ/(1+ℓ|v|)，
Σk≪ℓ²、∫k≪ℓ；三次权和及最后积分，再除原 ℓ⁴，给 ℓ³/T。
普通 Ingham/Huxley 只在先固定的有限 σ 网格使用；两段连续函数
递增且在 3/4 接值 3/5，最大值是摘要显示的 B(θ)。

\[
 B(7/8)=19/26,\qquad
 (2\theta-1)-B(\theta)
 =\frac{(1-\theta)(6\theta-5)}{3\theta-1}>0.
\]

数值 θ_* 与旧/新幂的表项同公式相符。这里仍相对原条带 [R]，
不重新认证底层无零论文。474 的 proper-power 差用 L⁴ norm
Minkowski 返回 genuine primes；摘要没有在未知增长下把两四矩
additive 等同，也没有倒用 packet upper 证明新的无零结论。

## 3. 同一 fixed carrier 的真实采样准入

独立重新核对 fixed-start 源，不仅依赖 compression 的结论。
z_u 中非零路径强迫 u 与 v=u+log(q/p) 都在 I_+，
所以每列真实 t-frequency 支撑于 [−u,ℓ/2−u]，宽 ℓ/2。
取支撑宽度 <3ℓ/4 的固定 bump，modulation 只改变其 kernel 相位，
衰减常数对 u 一致。原实线平移没有周期化。

对真正 L² 的 h_u=T_m(z_u 1_Jz)，compact Fourier support 给连续
代表及完整 η-grid Parseval：

\[
 \sum_{k\in\mathbb Z}|h_u(\sigma+k\eta)|^2
 =\eta^{-1}\|h_u\|_2^2.
\]

有限 k 集只是该网格子集。完整 finite polynomial 不在全轴 L²；
源中将其 exterior 部分用 raw |z_u|≤m_T² 和 Schwartz kernel
单独付款，故没有非法的全轴采样应用。
全部原 t_k∈[T,2T+s] 至 J_z 外有固定倍 T 的距离。

两个原 C² guards 保留 E_T(M) 的完整三项。外加采样尾在 N=3 下
用 raw M≤Cm_T⁴ 得 cross 和平方费用 O(ℓ^−6)，不需要未知
M bounded。φ 的 even half mass 精确为 a_ℓ/2；T/(dη) 保持 floor，
得到摘要 (3)。不能将其 relative small factor 或 E_T 的增长 cross
直接改为 additive o(1)，摘要准确没有这样做。

B(θ)<1，代入 (1) 后每个同一原 σ∈[T,T+s] 都有 r_σ=O(T^(B+ε))。
half-Gram 的反线性 factor 2、scalar fourth compression inequality
随后给 actual finite high fourth 上界。whole low fourth 和
Schatten triangle 使 entire prime fourth 继承同幂。
此处只需要一侧 upper，不假设 fixed carrier 的 fourth P-gap=o(1)，
亦没有把 band q_sq、r_σ 或 physical residual 宣称相等。

## 4. 原零侧最后接口必须保留真正 S1

475 §3 最后明确区分了 unnormalized Schatten S1 o(1) 与
normalized S1 o(1)。原同配置 AF 背景有 bounded normalized S4；
若 error 的真正 ||error||S1=o(1)，则

\[
 d^{-1/4}\|\mathrm{error}\|_4
 \le d^{-1/4}\|\mathrm{error}\|_1=o(1).
\]

所以 triangle 可将 prime-channel 增长 upper 传到相同 centered
zero matrix，不需 quartic additive equality。仅有
d^−1||error||S1=o(1) 一般不能得到这个结论：转到 normalized S4
可以多出 d^(3/4)。摘要已经保留这一必要范围。

本审查不重新证明 AF 的 tail、trace、二矩或 functional-equation
pairing；这些仍是原明示 [R]。结果不是新的原无零前件或惯性常数。

## 5. 正光滑载体的全标签 far 与未付 near

475 §4 与我的完整 far 独审一致。固定无限卷积密度是真正
C∞、非负、积分一、支撑 [3/8,5/8] 且 ∞≤8；sinc 产品给
exp(−√|z|/16)。Δ_T=1024ℓ^(5/2)/X 使 sΔ_T≥4096ℓ²，
因此整个 far carrier factor≤X^−4。

actual atom 的调制恒等式对 adjoint 同样成立；方向翻号后相位共轭。
四个 atoms 的全部三内部 P 保留，归一化 coefficient 模≤Πb_p，
全质量 O(X²/ℓ⁴)。故所有 H/L ordered words、signs、标签及
σ-independent 子集的 far 整体 O(X^−2ℓ^−4)，没有逐 tuple 删除 P。

χ∞≤8 继承的是 entire-word L¹ P error，不是 near 个体标签误差。
合法选择的载体仍在 [T,T+s]；near upper 若将来支付，增长时
good-set probability 的分母仍要保留。没有新 carrier/零侧量词循环。

真正 |S|≈1/X 的 Γχ(sS)→1。four-distinct half-ratio 的 product
长度仍 X²、determinant 宽度 O(Xℓ^(5/2))。摘要准确把这一共同
signed near 上界留为未付，而不是从 far o(1) 推 whole upper。

## 6. 连续主项、chirp 与对象澄清

全文核对 compression 源的 triangular ρ_X、Fubini 和 log-measure
normalization。continuous transform 为

\[
 V_X(t)^2
 =\left[
 \frac{X^{1/2+it}-X^{1/4+it/2}}{1/2+it}\right]^2.
\]

特别是下端幂为 it/2，不能写成 it。在原 J2，V²=O(X^−1)，而
raw Q_X=O(X)，其 mean-square 扣除才确实 additive O(ℓ^−4)。

审查时提出的对象歧义已在最终 475 §5 修正为“Λ 版本”。
它不把上述 additive 结论免费扩给 genuine primes；后者仍用
已冻结 proper-power L⁴ norm 差。原 Gallagher/log-window 的
chirp variation t₀δ=O(1) 由 BV 支付，最大 prefix discrepancy
的中心确实是同一 ρ_X。摘要只将该 variance 列为充分目标，
没有声称原 count、majorant 或另一个 Selberg center 自动付款。

## 7. 最终结论

最终 475 忠实连接了不同作者已审的完整证明，限定 PASS。
实际新增是相对原 ζ 条带的更强增长幂、对所有原 fixed carriers
的一侧转移、合法短载体的全标签 far 付款和准确的连续主质量扣除。
B(θ)>0，近共振/最大 centered variance 仍未付；没有 O(1)
四矩、比例改善、新零自由边界、RH 或 Weil 算术桥证明。
没有重新提出 470 已排除的 Q 前件，也没有把有限检查器当分析证书。
