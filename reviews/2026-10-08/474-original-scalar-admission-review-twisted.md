# 474 原 short-carrier 标量四阶矩准入：独立全文审查

2026-10-08。结论：限定 PASS。独立实读最终笔记全部 121 行，回核
另一作者的完整 f04279 源及本审查人对其完整 proof 的逐式复算。
474 正确汇总一侧准入，不把尚未支付的标量算术上界当作结论。

## 1. 最终字节绑定

canonical LF 只将 CRLF/lone CR→LF，不 trim 或改变 EOF。

| 文件 | canonical LF SHA-256 | canonical bytes /行 |
|---|---|---:|
| [474 最终笔记](../../notes/474-original-short-carrier-canonical-scalar-fourth-admission.md) | 37306c6d403f48c93d5d0f92782088225084e2e4b6b694cd89644a75fe39e99f | 5350 /121 |
| [完整准入源](hybrid-short-carrier-canonical-scalar-fourth-admission-research-radial.md) | f04279a9de54303d772859b2ee5e05010567404c53143c928a14e905eb51a0d7 | 14699 /370 |
| [源的完整独审](hybrid-short-carrier-canonical-scalar-fourth-admission-review-twisted.md) | f9b42278677a371bd38d8cb9555ac4306635336bd23a566be19e7a61eba047c3 | 8156 /164 |
| [472 原 P/ratio 桥](../../notes/472-original-short-carrier-fourth-compression-and-ratio-variance.md) | 9856885e932a892cf7c33ece82f430c2ec13004555eb52da2f1e8b1ec6bb2683 | 9037 /194 |

审查曾指出显示式缺少左括号命令的反斜线；最终稿已修为
$T_{\phi(u+\xi)}\!\left[\cdots\right]$。仅这项排版修复，无数学变化。

## 2. 原对象、系数和 one-sided 含义

474 保留 $X=T/(2\pi)$、finite $a_\ell$、genuine high primes
$\sqrt X<p\le X$、原 $b_p$、half-Gram $G=A^*A$、
same-prime $D_+$ 和完整 $R_+=G-D_+$。
每个 frequency $\log(q/p)$ 的源系数是
$b_pb_q\phi(u-\log p)^2\phi(u+\log(q/p))$；
因此首乘子 $\phi(u-\xi)^2$ 和终端 $\phi(u+\xi)$ 的符号
与右伴随平移一致。$p=q$ 项准确恢复 $D_+$。
摘要没有删掉 shared spatial window 或重选 prime phases。

原空间窗到未移位 $P_H$ 的准入是两个真实 Fourier 乘子：
terminal $L^2$ contraction，首个 $L^4$ norm 安全常数
$(1+1/\sqrt2)V_\ell$。源自证的 Hilbert/BV proof 支持此常数；
不是由粗 kernel $L^1$ 的 $\log\ell$ 界免费推出 uniform norm。
height cuts 后才使用全轴 $L^p$ 界；两个 positive guards 的
外部 tail 经 $C^2$ kernel 远端积分付款，未删除 height 0 的贡献。

## 3. 有限 prefactor、growth 和 carrier

源的 $\sigma+k$ overlap density 精确积分为一、支撑在
$[T,2T+s]$，并保留两端 strips 和 $d=\lfloor X\ell\rfloor$。
half spatial integral 为 $a_\ell/2$，所以
$A_T=a_\ell T(1+\eta/s)/(2d\eta)$ 准确，没有漏二倍系数。

474 保留的有限式是

\[
 \operatorname{avg}_\sigma r_\sigma+S_T/2
 \le A_T\left(
  N_\ell\sqrt{\mathcal M_T}
 +C_\phi(m_T/T)\mathcal M_T^{1/4}
 +C_\phi m_T^2/T\right)^2+C_\phi/\ell.
\]

首尾 $m_T/T$ 仍乘 $\mathcal M_T^{1/4}$，
$m_T^2/T=O(\ell^{-2})$ 的 cross 也未在未知增长四矩时删掉。
因此该式是 finite、growth-uniform 的一侧 upper。
只有将来证明 $\mathcal M_T=O(1)$，才可得到 bounded avg ratio
并调用 472 的共同 good carrier 选点；它没有支付 small ratio 常数，
没有把 $q_{\rm sq}$ 与完整实线 residual 等同。

## 4. proper powers 与两项 cutoff correction

摘要准确保留 normalized $L^4$ proper-power norm 差
$O(X^{-1/12})$。平方项的 base product 为 $pq\le X$，
frequency $2\log(pq)$；其第四矩的 weighted mean-value 支持
$L^4$ norm $O(X^{-1/8}\ell^{-1/2}+X^{-1/4})$，
不按 $p^2q^2$ 的 $X^2$ 长度付费。更高 powers 的 absolute
bound 经过原 $\ell$ normalizer 同样足够。
norm 差不能在未知增长四矩上先展开为 additive $o(1)$；
474 没有作这一步。

$\widehat P_H^2$ 的 $c_H=\Lambda_H*\Lambda_H$ 长度仍为
$X<n\le X^2$。对
$\Lambda_H=\Lambda-\Lambda1_{n\le\sqrt X}-\Lambda1_{n>X}$
完整展开，$L*L=U*U=0$ 仅在这个显示 product range 中成立。
$-2U*\Lambda+2U*L$ 合成末项的 $a>X,b>\sqrt X$。
474 的两个 correction 与源 (21) 一致，$X=16,n=95$
的例子也准确。源独审另行核过全部 240 个 finite formal coefficients；
该有限检查不认证正高度 mean-square。

## 5. 未付任务及证据边界

474 把剩余任务明确定位为同一个 $O(T)$ positive window 上、
全部 $c_H$ corrections 保留的 signed scalar mean-square。
它是一项真实充分算术输入，而非已证明的上界，也不是观测量之间
的双向相等。产品长度 $X^2$/高度 $O(X)$ 保留；
直接 weighted MV 的 $O(1+X/\ell^2)$ 明确不足。
Möbius、low 和 large-factor 项必须联合估计，不能逐项绝对化后
声称已经支付 cancellation。

本审查确认笔记的数学汇总及输入范围。末尾 finite checker/output
正在另行生成，将独立核验；未把尚不存在的输出当作本次 proof
证据。该检查也不能认证 Hilbert/BV 分析、实际 prime mean、
新比例、无零区域或 RH。限定 PASS。
