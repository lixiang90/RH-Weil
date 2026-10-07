# 原固定起点 half-Gram 采样准入：独立全文审查

2026-10-08，twisted_research。结论：限定 PASS。
实读 root 完整源全部 199 行，逐式复算真实频带、sampling Parseval、
两个正高度 guard 与 finite/growth 费用，不改被审源或 Git。

| 来源 | canonical LF SHA-256 | bytes /行 |
|---|---|---:|
| [完整被审源](hybrid-fixed-start-half-gram-sampling-research-root.md) | 7ed68a71d4d22d0bf1d90c61cef231534737188131aad9842669cd11f19c82cc | 7522 /199 |
| [474 完整原窗口乘子源](hybrid-short-carrier-canonical-scalar-fourth-admission-research-radial.md) | f04279a9de54303d772859b2ee5e05010567404c53143c928a14e905eb51a0d7 | 14699 /370 |

canonical LF 只统一 CRLF/lone CR，不 trim 或改变 EOF；
两个绑定已实际核对。

非零 (p,q) 项满足 u−log p∈I，而
v=u+log(q/p)=(u−log p)+log q∈I_+，因为 q>sqrt X。
所以原每列的频率准确在 [−u,L/2−u]，宽度 L/2。
新增 smooth cutoff 的频率 support 宽度小于 L，
并等于一于原有限 frequency set；没有改变 prime 系数或 terminal window。

对真正 L² 的窄频带函数 h，把其 Fourier support 放进一个长度 L
的 cell。Fourier-series Parseval 的 coefficient 为
L^(−1)∫hat h(ξ)e^(iσξ)e^(ikηξ)dξ，
sample 是该 coefficient 的 L/(2π) 倍。
再用实线 Plancherel 精确给
\[
 \sum_{k\in\mathbb Z}|h(\sigma+k\eta)|^2
       =\eta^{-1}\int_{\mathbb R}|h(t)|^2dt.
\]
这里仅为证明采样而作频率 cell 的 Fourier series；
原实线平移、interval zero extension 与物理 trace 均未周期化。
compact Fourier support 的 L² transform 也为 L¹，
所以 sample 使用其准确 continuous representative。

实际 finite polynomial z_u 不在全轴 L²。
源先取 h_u=T_m(z_u 1_{J_z})，
J_z=[3T/4,5T/2]，再对这个真正 L² signal 应用上式。
原 t_k∈[T,2T+s] 距 J_z 外至少 T/4（s<T/4），
遗漏补集经 Schwartz sampling kernel 全尾付为
C_N m_T²(LT)^(1−N)。没有漏掉 height 0 或无限尾。
finite samples 的 Minkowski 与 terminal contraction 因而给原 (4)。

两个 C² 原窗口 guards 在 J_z→[T/2,3T]→[T/4,4T] 仍有距离 cT，
所以 474 的 E_T(M_T) 完整继承。
even profile 的 half integral 准确为 a_L/2，
得到原 (7) 的 exact dη prefactor。
取 N=3，raw M_T≤C m_T⁴ 足够使全部新 sampling cross
≤C m_T⁴(LT)^(−2)=O(L^(−6))；
这里不要求未知 fourth 先 bounded。
原 E_T 自身的 growth cross 仍保留，未被这一新尾界删掉。

uniform D_+R_+ cross O(1/L) 支持 (8) 对全部合法起点 σ 一致。
原 ratio 是完整 half-Gram remainder norm；
actual high fourth 只通过 compression Jensen 获得一侧 upper，
没有将 q_sq、physical ratio 与 actual residual 自由等同。
背景与 zero-tail 的末步转移仍条件于该 same-configuration 的 AF [R]。

限定 PASS：新的付款是固定起点采样及完整尾，支持另付 scalar
growth upper 的 fixed-carrier 转移。本源没有支付 scalar arithmetic
upper、constant-size ratio、新比例、零自由边界或 RH。

