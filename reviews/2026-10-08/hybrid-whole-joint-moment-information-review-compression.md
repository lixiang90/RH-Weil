# whole joint moment information amplification 的独立全文审查

2026-10-08。审查者 compression_bridge；来源作者 radial_review。
已 FULL READ 冻结 final 359 行；只新增本审查，不修改源、旧冻结文件或 Git。

| 完整来源 | canonical UTF-8 LF SHA-256 | bytes / lines |
|---|---|---|
| [whole joint 信息模型](hybrid-whole-joint-moment-information-amplification-research-radial.md) | f9e3ffa1aa8c0be583b1c11fc952f8f09bd6deeee9f7bdfa31f3abda1523863e | 14884 / 359 |

canonical 为 CRLF/lone CR 转 LF，不 trim。结论：**限定 PASS**。
精确 finite tensor 公式、固定 m 后 T 的量词、两个 parity covariance、
最新470兼容性与 uniform-upper 信息限制均成立。
结论只针对第1节列出的 trace/Gram 接口；不是实际 scalar prime 算子、
单份原 carrier、same-prime operator diagonal 或零侧惯性模型的实现。

## 1. finite word 引理与已付输入目录

辅助 A 的 normalized moments 是 σA=σA³=0、σA²=1、σA⁴=m/2。
任何 word 的 base factors 不交换也不影响 tensor 乘积逐因子分解；
高因子数 j 的 trace 只乘 σA^j。此证明不调整内部次序。
因而全部0-H、2-H tracewords严格保持，1-H、3-H词为准确零。

核对现有已付目录，没有发现必须保留的非零 odd-H 主项：
weighted first/cross、one-H marked13、weighted high³、partial/capped31
均是零极限或 upper；带 high³ 的相对估计也容许零。
新 weighted H²L cubic 虽不是 odd-H，却有恰两个 H，故精确保留。
low³ 与整个 low16 parity四词不含 H，亦严格保持。
本核对不把未知 entire b=τH³L 或其 parity分量指定成实际已付数值。

任意有限 F、G 的 τFHG H、commutator quadratic、ΓF、
Γ与Δ的两parity covariance均由同一 finite word引理保持，
不限于一个 K 常数或有限几个 scalar W moments。
functional calculus f(W⊗I)=f(W)⊗I 精确成立；只延续 base 已获准的测试，
没有因这个恒等式替 base 新增 moving/adaptive weight 准入。

## 2. parity 分量、中心化与准确盲方向

U⊗I 是 involution；各 lifted parity分量正是原分量 tensor相同辅助因子。
high normalized HS parity error不变，low所有词不变。
Δ'=Δ⊗I、Z'=Z⊗A；因此 Δ'_j与Z'_j各自准确正交。
Γ'_j与Z'_j的两项分别乘 σA³、σA，也准确为零。
这是独立分量的 finite 验证，不是从总正交拆出未经证明的两个结论。
Z_j的norm、c、k及Γ_j–Δ_j covariance原数值保持；q、r不保持。

令 D=A²-I。σD=σDA=0、σD²=m/2-1，给
Γ'=Γ⊗I+H²⊗D。两个 auxiliary modes正交，故
q'=q+(m/2-1)a，且各parity有源(13)的准确norm公式。
新增 H²⊗D 对所有 lifted rowtests、low residuals与Z分量同时正交。
因此 rowtest中心化、两个Schur或负commutator项均看不见该成本。

整个 parity gap 满足
g'=g+(m/2-1)τ(H²UH²U)≥g；正号来自两个PSD矩阵的trace乘积，
无需H²与UH²U交换。于是q与g均不减，470的两个最新必要下界保持。
本模型没有复活已被排除的 Q=1/350。

## 3. 全第四矩与固定 m 的统一上界量词

有限循环展开 F=a+e+6c-k+4b+4η及lifted F'=(m/2)a+e+6c-k正确。
c=τH²L²≥0，k≤4c，e≥0；所以F'≥(m/2)a≥(m/2)(τH²)²。
原 second极限1/6使liminf F'≥m/72。

若基序列a无界，low4有界及normalized Schatten反三角已经使原F无界。
若基序列存在bounded-a子列，则每个固定m的lifted q仍有界，
所有bounded-q条件输入仍在域内；任意大m却使F'下界任意大。
因此没有独立于m、仅由共同已付trace/Gram数据给出的有限常数upper。
这不声称构造一个m随T增长且满足所有原定量率的模型。
原dimension、carrier、raw/tail和scalar系数约束不属于该信息结论。

complete residual的三个 auxiliary modes I、D、A两两正交，
源(20)严格保留 (m/2-1)a 的正成本；signed b=0与保留-k不能消除它。
正辅助变体 σ(A+)²=1、σ(A+)⁴=m，奇数词乘固定常数后仍保留零极限；
其反三角障碍成立，但不能把该变体的finite奇数词误写成exact0。

## 4. same-prime 与 carrier scope 的必要区别

final 第2节已明确：选定center W⊗I仅保持paid rowtest矩阵数据。
若把每个真实prime factor字面lift为B_p⊗A，则其同prime quadratic
diagonal会成为W⊗A²，差异不是o(1)。所以本模型不保留原same-prime
operator定义，不能把其large fourth当实际genuine-prime的反例。

E⊗I、P⊗I可形式保留全部projection次序；但fiber coefficient表示
已改变scalar carrier及算术。不能据此声称原physical准入、[R]、
raw/good替换、zero features或partial-Weil惯性实现均保持。
源首段与第6节准确限定了这些边界；upper信息不足不等于所有惯性比例证书失效。

## 5. 对实际下一付款的准确含义

q=τΓH²-τΓW是严格finite恒等式。对已付固定rowweights的中心化
没有控制H²方向的upper；tensor新增成本正好落在此方向。
因此该审计支持继续研究真实scalar balanced四素数signed covariance，
或原P的fourth compression deficit，不能用更多同类rowtest Cauchy代替。
它没有证明actual q或full fourth无界，也没有得到实际upper或比例改进。
作者的小矩阵32条核验只作有限代数辅助；本审查依据上述逐式证明，
没有将其运行结果当prime渐近或任何未付算术证明。
