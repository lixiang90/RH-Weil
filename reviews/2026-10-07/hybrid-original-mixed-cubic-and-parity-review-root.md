# 原 mixed cubic 与 parity 残差：root 独立全文审查

2026-10-08。两份完整推导限定 PASS。原背景含 low 的全部三次词
与 parity 必要约束通过；whole high fourth、实际 q/k 前件及新比例仍开放。

审查最终来源：

- [mixed cubic](hybrid-background-entire-mixed-cubic-research-compression.md)，
  canonical LF SHA256
  19c715587681c95c3e8750e4751a30bff798b372f68dc516f029c0a5e71020dd，
  13926 bytes、289 lines；
- [parity residual](hybrid-parity-resolved-residual-necessary-constraints-radial.md)，
  canonical LF SHA256
  6a5fb7db8467e80682d7351ee37a940af8d39de50fffe2f16b0b3a48d5dfc6f6，
  13209 bytes、350 lines。

均完整逐节读取；mixed 最终 complex-weight 补明也已重新核验。
未修改作者来源和既有冻结文件。根对 HHL alias positive 计数的建议
已由作者单独重算和写入完整证明，本审查另外检查其接口及全部限制。

## 1. 三次物理词的 near

三个 prime 的净位移不可能为零，包括重复标签。
原 finite K_d 在固定 near 支持内可准确写成
L/(2πidS) 乘两个 endpoint 指数，加 O(1/d)：
这是 1/(exp(2πiS/L)-1) 的局部展开，原 floor d 仍保留。

两个 intermediate φ²、终点 φ 与 smooth near gate一起 Fourier 分离。
LLL 只剩 low semiprime 对 low prime，HLL 只剩 low²对 high prime，
HHL 只剩 high×low 对 high prime；其他方向由范围严格排除 near。
每个 product prefix只限制同侧 factors，另一 prime side仍独立。
整数产品与 prime 无交集，Hilbert 的局部 spacing 为至少常数/n。
作者列出的两个乘积 energy bounds覆盖 phases、ordered multiplicity
和重复 labels，因而真实 near费用分别为
O(ell0³/(sqrt(X)L))、O(ell0³/L^(3/2))、O(ell0³/L)。
O(1/d) remainder也逐类支付，HHL未用未截断的原全质量。

该 Hilbert 输入与项目旧证明一致；已查阅
[Montgomery–Vaughan 原文](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)
关于局部分离实频率的加权形式。此查阅不代替本稿产品范围的重新验证。

## 2. HHL alias 与 canonical far

same-sign high 同号 low 的净位移超出原支持；反号 low的物理支持
强制 pq<Xr。以原正系数扩大 high masks后，二素数乘积质量
至多 sqrt(Y)log(Y)/L²，再对 low 求和，给 X/L²。
opposite high 的正 alias为空；负 alias 强制其中一个 high
不超过常数 sqrt(X)，给 X/L³ 总质量。端点 overlap与核相乘
为 O(1/X)，所以这两项都小。placement只改变中间窗，未改变这个 upper。

remaining middlefar g_L=(1-near)(1-alias)/(L sin(πS/L)) 在每个 pole
附近恒零。中央用 |S|、端部用 L-|S| 求前两阶导数，给
||g_L||_1=O(log L)、||g_L''||_1=O(1)。
Fourier L1及大频率尾均已付，再共同分离三个 shifted windows。
unshifted w(u)φ(u)保留，phase shifts不依赖 u，故任意 bounded w
没有变成 moving prime coefficients。

good Fourier coordinates的全部实际高度仍在原 [T/2,3T] 或其负区，
可以分别应用 genuine-prime sharp prefix，而 low长度虽为 sqrt(X)
其 height仍为 X量级。HHL主幂2.5a-2.25在θ<a<.9为负。
任一大 coordinate完全改用原 raw质量和C²尾，费用为 X^(-3/4)
乘对数因子，包括 principal峰。LLL/HLL远项则直接以原正质量付款，
无需 [R]。

## 3. 所有内部 P 与实际背景

LLL/HLL的原 raw leakage足以给 weighted四算子两crossing小误差。
HHL使用 good-band q_R和原 finite-carrier leakage
O(sqrt(L)q_R)，误差 Lq_H²q_L=o(d)。
复 weight的两个方向泄漏被明确保留：normal乘法与 finite trace
给 ell_w²=ell_w*²，作者未把非自伴 weight免费当成自伴。

finite raw/good单因子使用双packet S1尾；physical weighted
raw/good使用首个大频率跳跃 HS与左 wφ packet的 sqrt(d) norm。
其 normalized HHL费为 X^(-1/4)L^(-7/2)，严格小。
因此原 raw物理词、good物理词、good finite词、原 finite词四个
对象之间均有已付接口，没有删除或交换原 P。

只有增加 whole high4 bounded后，才合并相对 high³、Minkowski、
实际 R_T和455 proper-power S4，得到完整实际 A CΛ³小量。
没有此条件时作者没有声明无条件 Y=o。
移除非平窗口 Cauchy附加费的式(10)也保留该前件。

## 4. 高残差 fixed clip 与共同极限

HS Lipschitz的双谱公式每项权重Tr(P_iQ_j)非负，odd 1-Lipschitz
clip确实保持渐近 high parity。bounded W与U的交换用原 QJE
和乘法泄漏付款，未假设 P与J交换。

D_R=H²-H_R²≥0，在其支持上 H_R²=R²。
R²≥M_T时 TrΓ_R D_R≥0，故 q-q_R≥||D_R||²/d。
HS奇部的投影收缩与有限 e_R给作者(9)；sharp4M可直接用于 H_R。
||H-H_R||²/d≤a_T/R²给 commutator平方根误差，
没有丢任一 tail或centering项。

在明确 q_T bounded之后 a_T才一致有界。先固定 R取T极限，再取R极限，
严格得 liminf(q_T-r_T)≥41/15120。
作者使用共同子列 (q,r)，没有把来自不同子列的limsup混在一起。
该结论并不声称 Γ的odd部分无条件小量。

## 5. low平方的全部P与sharp半区

L²与E*B_L²E的HS gap≤y ell；U L² U与E*JB_L²JE的gap
O(y ell+y²ell_J)。它们除sqrt(d)均小，T_odd的Q crossing也小。
已付整个 low4先保证两端HS norm有界，随后才传递norm平方。

插入固定 smooth Jε时，nonzero atoms仍由共同 Fourier/Hilbert近核及
原 far/alias正质量付款；额外 bounded masks只增加固定ε的seminorm。
作者显示六因子两crossing费中 y²ell²、y³ell ell_g、y⁴ell_g²
除d都小。weighted low4的正边界条带为O(ε)，compression Schwarz
给 smooth-to-sharp误差，顺序为先T后ε，没有将sharp符号当成C²窗。

零原子中第一相邻配对两步后回原点，对odd norm不贡献；
另两配对同号crossing长度为min(x+y,1-x-y)，异号为|x-y|。
根逐条检查其原中间位置约束，并独立按x≥y及x+y≤1/2分区积分，
得到δodd=13/480。再由已付δ=1/20得δeven=11/480。
没有只算配对积分就代替整个四词的准入。

## 6. covariance的严格范围

real HS的even/odd正交分解和两次Cauchy确实给作者(25)–(26)。
Q=1/350时r最多11/75600，小于根号和的极大位置13/8400；
因此代入端点给严格小于1/100的upper。
根独立复算平方余量4883/28576800000000>0与两个外包络端点。

作者没有把整体 Δ⊥Z拆成两个parity分别正交，也没有排除或实现
467候选、给实际 q/k前件或构造prime model。两份来源的限定结论通过；
analytic estimates仍依赖完整书面推导，精确脚本只认证有限代数。

## 7. 无bounded-fourth前件的实际cubic相对恢复

另完整读取
[relative actual cubic补充](hybrid-background-cubic-relative-actual-recovery-research-compression.md)，
最终 canonical LF SHA256
1dbdad713d2694d9fce6391971fc0044fcbf18d0ad3dbdd2d3fba5111ba80d38，
5564 bytes、127 lines。限定 PASS：其整个组合使用 mixed cubic 的
原 θ<9/10 [R]，static high相对估计本身来自原parity。

先由整个Λ已付二矩及proper-power normalized S4恢复prime二矩O(1)，
无需high4有界。Minkowski给f_pr≤8(a_T+low4)，所以sqrt(f_pr)
至多常数(sqrt(a_T)+1)。actual R_T乘prime cube分成(R_TC)C²，
两个S2给||R_T||op sqrt(c_T f_T)，保留真实背景误差。

作者列出(C+P)³-C³的全部七个非交换词。根逐项检查有限循环位置、
S2/S4指数和归一化d因子：一个P的三词均至多M sqrt(f_T) ε_T，
两个P的三词均至多M sqrt(c_T) ε_T²，三个P词至多M ε_T³。
这里ε_T=||Pproper||4,d=O(1/L)，并非假定proper-power op小量。
APC²、CPC、PCP没有被交换或遗漏。

与static high relative sqrt(a_T)/L及七个含low词的已付小量相加，
严格得到实际 |Tr A CΛ³|/d≪(sqrt(a_T)+1)/L+o(1)。
因此a_T=o(L²)足够使该项小，但没有给a_T任何新增长上限；
完整比例转换所需常数预算仍未支付。此更弱前件限定通过。
