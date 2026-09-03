# NCE-8：response-specific Vaughan--Brownian channel Gram

> **2026-09-03 审计修正（笔记 242）**：本笔记有限表采用
> `U=V=floor(sqrt N)`；由 Type-II exact support floor
> `(U+1)(V+1)>N`，这些实验中的 Type-II channel恒为零。因此表中
> `diagonal/full=1.95--3.36` 只验证 prime--continuum cancellation，不能作为
> Type-I--Type-II cross evidence。AHE--AHG 的有限代数恒等式保持正确。笔记 242
> 已用 `U=V=floor(N^(1/3))` 重算非空 Type-II Gram，并把目标改为 cutoff-invariant
> physical prime--continuum correlation。

文档 194 把 degree-two canonical response 的 direct Cauchy 控制压缩为一个
constant mode 与一个 Brownian primitive energy。本笔记完成下一步代数分解：
对任意 exact Type I/II（以及 continuum）分通道，不展开五个多项式因子的所有
颜色组合，而通过一个公共 divided-difference multiplier 得到精确的有限
channel Gram。

主要结论是：

1. centered degree-two response 对任意加法分通道都有一个 exact linear
   primitive factorization；
2. Vaughan Type I、Type II 与 continuum 形成一个 positive semidefinite
   Brownian Gram，完整能量恰为其 all-ones quadratic form；
3. 通道 cross terms 必须保留；四个冻结尺度中，diagonal-only budget 比完整
   能量大约 \(1.95--3.36\) 倍；
4. 只对公共 multiplier 使用 total-variation/Young 不等式没有尺度收益。

这里的恒等式均为无条件有限代数事实；uniform arithmetic Gram bound 仍未证明。

## 1. 公共 divided difference

令 \(\mathcal M_c(\mathbb R)\) 是 compactly supported finite measures 的交换
卷积代数，单位为 \(\delta_0\)。取 finite Hermitian symbol

\[
d=\sum_{r\in\mathcal R}d_r,\qquad
M_r=d_r(\mathbb R),\qquad M=\sum_rM_r.             \tag{1}
\]

令

\[
\alpha={\sqrt3\over2},\qquad L=\alpha B,\qquad
F_L(z)=z^3(z-L)^2.                                \tag{2}
\]

文档 194 的 degree-two response 为

\[
q=-\kappa^2F_L(d),\qquad
\kappa={2a\over3B^2},\qquad
a={\alpha B\over\alpha B+\rho}.                   \tag{3}
\]

其 total coefficient 是

\[
T=q(\mathbb R)=-\kappa^2F_L(M).                   \tag{4}
\]

定义在 \(M\) 处的 polynomial divided difference

\[
R_{M,L}(z)={F_L(z)-F_L(M)\over z-M}.              \tag{5}
\]

直接除法给

\[
\begin{aligned}
R_{M,L}(z)
={}&z^4+(M-2L)z^3+(M-L)^2z^2\\
 &+M(M-L)^2z+M^2(M-L)^2.                         \tag{6}
\end{aligned}
\]

式 (6) 也定义卷积代数元素 \(R_{M,L}(d)\)。

### 定理 AHE（exact centered channel factorization）[U]

对每个 channel 置

\[
\bar d_r=d_r-M_r\delta_0,\qquad
q_r^\circ=-\kappa^2\bar d_r*R_{M,L}(d).           \tag{7}
\]

则

\[
q_r^\circ(\mathbb R)=0,\qquad
\sum_rq_r^\circ=q-T\delta_0.                      \tag{8}
\]

#### 证明

第一式来自 \(\bar d_r(\mathbb R)=0\)。又

\[
\sum_r\bar d_r=d-M\delta_0.                       \tag{9}
\]

由 divided-difference identity，

\[
(d-M\delta_0)*R_{M,L}(d)
=F_L(d)-F_L(M)\delta_0.                           \tag{10}
\]

式 (7) 对 \(r\) 求和，再用式 (3)--(4)，即得式 (8)。\(\square\)

这一定理没有把五个 slots 分别标记为 Type I/II；所有 channels 只在唯一的
centered factor 中出现，另外四阶 multiplier 保持完整 prime--continuum
cancellation。

## 2. Primitive Gram

令 \(A_r\) 是 \(\bar d_r\) 的 vanishing-at-infinity primitive：

\[
DA_r=\bar d_r.                                    \tag{11}
\]

定义 response primitive

\[
U_r=-\kappa^2 A_r*R_{M,L}(d).                    \tag{12}
\]

则 \(DU_r=q_r^\circ\)。置

\[
G_{rs}=\langle U_r,U_s\rangle_{L^2(\mathbb R)}.  \tag{13}
\]

### 定理 AHF（response-specific channel Hodge Gram）[U]

矩阵 \(G=(G_{rs})\) Hermitian positive semidefinite，且

\[
\mathcal E_B(q)
=\left\|\sum_rU_r\right\|_2^2
=\mathbf1^*G\mathbf1.                            \tag{14}
\]

因此 direct Cauchy response 满足

\[
\left|\int e^{-|x|}\,dq(x)\right|
\le |T|+\sqrt{\mathbf1^*G\mathbf1}.              \tag{15}
\]

#### 证明

式 (13) 是 \(L^2\) vectors 的 Gram，故正半定。定理 AHE 表明
\(\sum_rU_r\) 是 \(q-T\delta_0\) 的 primitive。文档 194 定理 AHB 给
式 (14)，定理 AHA 再给式 (15)。\(\square\)

### Vaughan 专门化

文档 164 定理 ACP 给 prime coefficient 的 exact quotient

\[
\Lambda=I_{U,V}+II_{U,V}.                        \tag{16}
\]

把相同 Abel/modulation weight 乘到式 (16)，并把 continuum symbol 记为
\(d_c\)，则

\[
d=d_I+d_{II}+d_c.                                \tag{17}
\]

对式 (17) 应用定理 AHE--AHF，得到 canonical \(3\times3\)
Type I/Type II/continuum Brownian Gram。也可通过文档 164 的 continuum gauge
把 \(d_c\) 分配给前两个 channels，得到 exact \(2\times2\) Gram。两种写法的
all-ones quadratic form 相同。

这就是 response-specific Type I/II factorization：它只要求控制一个指定
nonlinear response 的 Schur/cross Gram，而非 full Selberg profile 的全部
prefix directions。

## 3. 为什么不能立即对 multiplier 取绝对值

令

\[
\|d\|_{\rm TV}=B,\qquad x={|M|\over B}\le1.       \tag{18}
\]

由式 (6) 和卷积 Young 不等式，

\[
\|R_{M,L}(d)\|_{\rm TV}
\le B^4 C_\alpha(x),                              \tag{19}
\]

其中

\[
C_\alpha(x)
=1+(x+2\alpha)+(x+\alpha)^2
+x(x+\alpha)^2+x^2(x+\alpha)^2.                  \tag{20}
\]

所以

\[
\|U_r\|_2
\le \kappa^2B^4C_\alpha(x)\|A_r\|_2
\le {4\over9}C_\alpha(1)\|A_r\|_2
<6.31\|A_r\|_2.                                  \tag{21}
\]

### 命题 AHG（normalization-neutral Young no-gain）[U]

只使用 \(\|d\|_{\rm TV}\le B\)、\(|M|\le B\) 与 convolution Young
不等式，不能从式 (12) 获得任何随 \(B\to\infty\) 消失的因子。

#### 证明

式 (21) 已给出的 upper bound 是 absolute constant。更直接地，写
\(d=Bd_1\)、\(M=Bm_1\)、\(L=\alpha B\)，并取 \(\rho=\beta B\)。
则 \(R_{M,L}(d)=B^4R_{m_1,\alpha}(d_1)\)，而
\(\kappa^2=B^{-4}[2\alpha/(3(\alpha+\beta))]^2\)。二者精确抵消。
\(\square\)

所以未来估计必须使用 \(R_{M,L}(d)\) 与 \(A_I,A_{II},A_c\) 的 joint frequency
geometry、cross Gram 或 Schur complement。把 multiplier 换成 variation
majorant 会退回 base-symbol Brownian/Selberg 难度。

## 4. 有限 Type I/II 审计

脚本 scripts/formal_lag_response.py 新增：

- degree_two_centered_response_channel_maps：实现式 (6)--(10)；
- brownian_primitive_component_gram：在共同 lag partition 上一次 prefix
  scan 计算完整 channel Gram。

scripts/audit_soft_zeta_orbit.py 使用文档 164 的 exact Vaughan coefficients，
把 prime atoms 分成 Type I/II，再与 continuum 形成式 (17)。冻结结果为：

| \(Y,N\) | \(\mathcal E_B\) | diagonal sum | cross sum | diagonal/full |
|---:|---:|---:|---:|---:|
| \(4,7\) | \(0.0002995\) | \(0.0010049\) | \(-0.0007054\) | \(3.36\) |
| \(8,10\) | \(0.0004782\) | \(0.0010377\) | \(-0.0005594\) | \(2.17\) |
| \(12,12\) | \(0.0005780\) | \(0.0011251\) | \(-0.0005470\) | \(1.95\) |
| \(16,15\) | \(0.0005433\) | \(0.0013444\) | \(-0.0008011\) | \(2.47\) |

每个 Gram 的最小 eigenvalue 在 double precision 下非负，channel sum 与文档
194 的独立 Brownian energy 相差不超过 \(10^{-10}\)。这些表只验证有限恒等式；
cutoff 选择 \(U=V=\lfloor\sqrt N\rfloor\)，不代表渐近最优选择。

cross sum 在四个尺度都为负，且与 diagonal 同阶。若分别估计 Type I、Type II
与 continuum norms，立即损失约 \(2--3\) 倍；更重要的是，渐近上这种损失可能
破坏 barrier summability。

## 5. 新的条件接口

在文档 194 推论 AHD 的 hypotheses 下，把每个 \(q_n\) 由 exact arithmetic
channels \(r\in\mathcal R_n\) 构造，并令 \(G_n\) 为式 (13) 的 Gram。若

\[
\sup_n\left[
|T_n|+\sqrt{\mathbf1^*G_n\mathbf1}
+2\rho_n+5\epsilon_n\tau_n(|H_n|)+\eta_n
\right]<\infty,                                  \tag{22}
\]

则相应 self-dual divisor 位于中心线。

式 (22) 与文档 194 的 energy criterion 数值相同，但现在其 arithmetic
provenance 已精确分成 Type I/II/continuum channels，能够应用：

1. Type II bilinear large sieve 于 \(G_{II,II}\)；
2. centered Type I summation-by-parts 于 \(G_{I,I}\)；
3. joint prime--continuum estimate 或 Schur shorting 于 cross blocks。

不能把三条 diagonal estimates 相加后宣称完成；必须直接控制
\(\mathbf1^*G\mathbf1\)，或证明一个保留负 cross term 的合法 Schur majorant。

## 6. 下一最小引理

1. 在单个 square-root Vaughan rectangle 上写出
   \(G_{II,II}\) 的 product-incidence kernel，并保留公共 multiplier；
2. 计算 \(G_{I,c}\) 的 exact Abel summation-by-parts，检查 continuum 是否消去
   Type I 的 normalization-neutral 主项；
3. 对 \(3\times3\) Gram 做 continuum-channel Schur shorting，比较 shorted
   \(2\times2\) energy 与 full energy；
4. 若任何 universal bound 必须先控制 \(\|A_I\|_2^2+\|A_{II}\|_2^2\)，则由
   命题 AHG 降级该路线，因为它恢复 full Selberg-type 输入。

## 7. 审计结论

degree-two Brownian certificate 已获得一个 exact Vaughan channelization。
它是构造性的有限 Hodge structure，保留所有通道间相消，并把下一算术问题变成
一个明确的低维 response Gram bound。新的严格障碍是：普通 Young/variation
估计在 Chebyshev normalization 下尺度中性；突破必须来自算术 cross-channel
geometry，而不是更粗的 coefficient norm。

## 8. 后续 cutoff 与 quotient 修正（笔记 242）

笔记 242 证明 simultaneous square-root cutoff使 `II_(U,V)(n)` 在全部 `n<=N`
恒为零，故本笔记第 4 节的旧有限表不能支持 Type-I/II cancellation。修正后的
cube-root cutoff给非零 Type-II energy，且 finite Type-I/II coherence约为
`-0.91` 到 `-0.94`；仅记 [E]。

更重要的是，common divided-difference map的线性性给
`u_I+u_II=u_p`，所以 physical prime energy、prime--continuum cross与 full energy
均与 cutoff无关，而三通道 diagonal sum可由 split gauge任意放大 [T/N]。因此
本笔记原先以 diagonal/full 描述的“改善”降为 decomposition diagnostic；新的
intrinsic [O] 是在 physical quotient 上证明 uniform negative
prime--continuum correlation，详见笔记 242-(25)。
