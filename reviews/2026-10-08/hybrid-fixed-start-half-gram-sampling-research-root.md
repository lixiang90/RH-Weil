# 原 half-Gram 的固定起点采样准入

2026-10-08，root。基线 46106dc449ac7e6d91a3646b09e63b0b0e272cc1。
只新增本稿，不改冻结的 472、474、原论文或旧证书。

[T] 原 half-Gram 到同一个 canonical scalar fourth 的一侧上界现在
uniform 于全部原起点 sigma∈[T,T+s]，不只对 sigma 平均成立。
新的步骤是实际每列的频率宽度只有 ell/2，对原 eta-grid 做精确
sampling Parseval，再付正高度 guard 的远尾。
这不是 canonical scalar fourth 的算术上界。

## 1. 冻结对象与输入

canonical 只统一 CRLF/lone CR 到 LF，不 trim 或改变 EOF。

| 来源 | canonical LF SHA256 |
|---|---|
| [474 完整窗口乘子源](hybrid-short-carrier-canonical-scalar-fourth-admission-research-radial.md) | f04279a9de54303d772859b2ee5e05010567404c53143c928a14e905eb51a0d7 |
| [原 half-ratio 与 uniform cross](hybrid-whole-short-carrier-ratio-and-distinct-criterion-research-twisted.md) | c7ff142ebe15232542626e4feda3c05a1285cbf7bff64f462e734c662dafea53 |
| [472 原载体与全 P 桥](../../notes/472-original-short-carrier-fourth-compression-and-ratio-variance.md) | 9856885e932a892cf7c33ece82f430c2ec13004555eb52da2f1e8b1ec6bb2683 |

保留 X=T/(2pi)、ell=log X、eta=2pi/ell、d=floor(X ell)，
s=T/sqrt ell、I=[−ell/2,ell/2]、I_+=[0,ell/2] 和原 even C²
zero-extended taper phi。E_sigma 的列是
ell^(−1/2)1_I exp(i(sigma+k eta)u)，0≤k<d。
原 genuine high primes 为 sqrt X<p≤X，
b_p=log p/(a_ell ell sqrt p)，a_ell=||phi||₂²/ell。

记原 high half 为 A，G=A*A，原 same-prime 为 D_+，
R_+=G−D_+，r_sigma=||R_+E_sigma||HS²/d，
S_T=ell^(−1)int_I w_T²。
474 的实际 finite polynomial

\[
 z_u(t)=\sum_{p,q}b_pb_q\phi(u-\log p)^2
   \phi(u+\log(q/p))e^{it\log(q/p)}
\]

满足 (GE_sigma e_k)(u)=ell^(−1/2)phi(u)e^(it_k u)z_u(t_k)，
且所有输出位于 I_+。保持实际零延拓和 same-prime 中心。
定义 m_T=sum_p b_p，M_T=T^(−1)int_[T/4,4T]|P_H(t)|⁴dt。
Chebyshev 给 m_T≪sqrt X/ell；也有无算术消去的 M_T≪m_T⁴。

## 2. 实际每列的窄频带

若 z_u 的 (p,q) 项非零，则
u−log p≥−ell/2，且 v=u+log(q/p) 在 I。
由于 log p、log q>ell/2，

\[
 u>0,\qquad v=(u-\log p)+\log q>0.
\]

所以 u,v∈I_+，而该项真实频率 xi=log(q/p)=v−u 满足

\[
 -u\le\xi\le\ell/2-u.
 \tag{1}
\]

这是实线上的区间，宽度仅 ell/2，未按 ell 取模或删除边界。
令 c_u=ell/4−u，选固定 even C∞ 函数 0≤b≤1，
b=1 于 [−1/4,1/4]，support b⊂(−3/8,3/8)，并设
m_u(xi)=b((xi−c_u)/ell)。
其 support 宽度小于 3ell/4<ell，而 m_u 等于一于 (1)。
因此对原 finite polynomial 精确有 T_(m_u) z_u=z_u。

关于 t 的 kernel 是

\[
 K_u(v)=e^{ic_uv}\ell\check b(\ell v),\qquad
 |K_u(v)|\le C_N\ell(1+\ell|v|)^{-N},
 \tag{2}
\]

其中 check b(v)=(2pi)^(−1)int b(xi)e^(ivxi)dxi。
常数 uniform 于 u,ell；||T_(m_u)||_(2→2)≤1。

## 3. 原网格的精确 sampling Parseval

若 h∈L²(R) 的 Fourier support 在长度小于 ell 的区间内，
则对每个真实 sigma，

\[
 \sum_{k\in\mathbb Z}|h(\sigma+k\eta)|^2
       =\eta^{-1}\int_{\mathbb R}|h(t)|^2dt.
 \tag{3}
\]

这里 h 的 compact Fourier support 也使 Fourier transform 属 L¹，
故各 sample 是其连续代表。为直接证明 (3)，把 support 放入一个
长度 ell 的频率 cell，令 H(xi)=hat h(xi)e^(i sigma xi)，
在 cell 上作普通 Fourier-series Parseval。其第 k 个 coefficient
是 ell^(−1)int H(xi)e^(ik eta xi)dxi；h(sigma+k eta) 是它的
ell/(2pi) 倍。Parseval 再用实线 Plancherel 即给 (3)。
只在这一采样证明中使用 frequency cell，没有周期化物理平移算子、
将实线 trace 循环成 torus trace，或使两个不同 prime ratios 相同。

取 J_z=[3T/4,5T/2]。当 T 足够大且 s<T/4，全部原样本
t_k∈[T,2T+s] 距 J_z 外至少 T/4。
把 z_u 精确切为 z_u1_(J_z) 及补集，并令
h_u=T_(m_u)(z_u1_(J_z))。该函数属于 L²，且有上述窄 support。
(3)、contraction、有限样本集包含于全整数网格给

\[
 \left(d^{-1}\sum_{k=0}^{d-1}|h_u(t_k)|^2\right)^{1/2}
       \le(d\eta)^{-1/2}\|z_u\|_{L^2(J_z)}.
 \tag{4}
\]

另一方面 |z_u(t)|≤m_T²，(2) 给每个样本的完整 exterior tail

\[
 |T_{m_u}(z_u1_{J_z^c})(t_k)|
      \le C_Nm_T^2(\ell T)^{1-N}.
 \tag{5}
\]

全实线有限多项式虽不在 L²，此处只对真正 L² 的 h_u 使用
(3)，补集经有界 signal 与可积 kernel 单独支付。
有限样本 Minkowski 结合 (4)–(5) 合法。

## 4. 同一 positive-height scalar guard

J_z 到 J_1=[T/2,3T] 外、J_1 到 J_2=[T/4,4T] 外的距离
均至少固定倍 T。474 的两次 C² kernel 切窗证明因此保持原式：

\[
 T^{-1/2}\|z_u\|_{L^2(J_z)}
 \le E_T(M_T):=
 N_\ell\sqrt{M_T}
 +C_\phi(m_T/T)M_T^{1/4}+C_\phi m_T^2/T,
 \tag{6}
\]

uniform 于 u。其中 N_ell=(1+1/sqrt2)||(phi²)'||₁；
没有用粗 kernel L¹ 的 log ell 增长界替换 uniform BV-L⁴ norm。
所有 guards 为正高度 O(T)，scalar input 仍是原 [T/4,4T]。

代入每列 (4)–(6)，再对 ell^(−1)phi(u)²du 积分，
even window 的 half integral 为 a_ell/2，得对全部原起点

\[
 \frac{\|GE_\sigma\|_{\rm HS}^2}{d}
 \le\frac{a_\ell}{2}\left[
  \sqrt{\frac{T}{d\eta}}E_T(M_T)
     +C_Nm_T^2(\ell T)^{1-N}\right]^2 .
 \tag{7}
\]

这是 finite、growth-uniform 的准确一侧上界。
特别取 N=3，利用已显示的 raw M_T≪m_T⁴、E_T(M_T)≪m_T²、
d eta≈T 与 m_T≪sqrt X/ell，新增 sampling-tail 的全部平方和
cross 费用至多 C m_T⁴(ell T)^(−2)=O(ell^(−6))。
这一步不要求未知 fourth bounded，也不丢掉第 (6) 式本身的费用。

## 5. 固定起点的 actual ratio 及四阶转移

原 uniform cross 给
||GE_sigma||HS²/d=r_sigma+S_T/2+O(ell^(−1))。
因此 (7) 严格给

\[
 \boxed{\quad
 r_\sigma+\frac{S_T}{2}
 \le\frac{a_\ell T}{2d\eta}E_T(M_T)^2+C_\phi/\ell
 \quad(\sigma\in[T,T+s]).\quad}
 \tag{8}
\]

它无需 sigma 平均。prefactor 保留 exact floor，不能在未知
增长下把其 relative o(1) 免费替为 additive o(1)。
两原窗口 guard 费用仍完整留在 E_T，不能删除其中的 cross。

若另付原 scalar M_T≪X^(B+eps)，0≤B<1，则 (8) 给
uniform r_sigma≪X^(B+eps)。B 是另一算术输入，不由采样推出。
真实 physical high fourth 满足
Phi_H,sigma/d=2||GE_sigma||HS²/d；
有限压缩的 scalar Jensen 给
Tr(E_sigma* H E_sigma)^4/d≤Phi_H,sigma/d。
因此同一固定起点的 entire finite high fourth 同样是
O(X^(B+eps))。用 Schatten triangle 与已付 whole low fourth，
可得 entire prime-channel 的增长上界；这里不追求 constant。

原背景有 bounded normalized S4，零点尾若在该原起点满足 AF 的
trace-norm o(1)，Schatten triangle 又可给 same-configuration 的
centered zero-matrix fourth 上界 O(X^(B+eps))。
此 upper 转移不需要先证明 quartic 差为 additive o(1)；
不能据它恢复更精细的等式或固定常数。
涉及 AF 的末一步仍相对其明确的 [R]，不由本文重证其无限分析。

## 6. 范围

新付款是原窄 half-Gram band、固定起点 sampling 及完整 exterior tail，
没有把 canonical scalar fourth 重新命名为已证原算术 upper。
若另有新的 scalar power upper，本稿使其可传到原 fixed carrier，
而非只在短平均中存在一个未知起点。
没有新比例、无零边界、新的 prime cancellation 或 RH 证明。
全文和最后的引用范围待其他作者独立审查。
