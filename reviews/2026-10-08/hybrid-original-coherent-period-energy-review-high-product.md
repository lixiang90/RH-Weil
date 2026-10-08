# 原 coherent 周期正能量：不同作者数学审查

2026-10-08，high_product_joint。研究轮2，基线 main 62469c0。
只新增本 peer；未改作者源、冻结依赖、输出、检查器或 Git。

**限定 PASS。** 对 checkpoint_audit 的191行作者源完成一次 FULL READ
并独立推导，未发现所述真实 coherent 正能量及其消费中的数学缺口。
这里通过的是 \(E_H\ll Q^3L^C\) 及费用 \(QS/X\)，不是新的高产品
whole 付款、独立 \(G\) 能量或六腿 shifted-covariance 省幂。

## 1. 全文读取与冻结身份

canonical UTF-8 LF 只转换 CRLF/lone CR，不 trim 或改变末尾换行。
作者源及下列实际依赖已全文读取，身份实际重新计算：

| 源 | 行数／LF字节 | SHA256 |
| --- | --- | --- |
| [本次作者源](hybrid-original-coherent-period-energy-research-checkpoint-audit.md) | 191／8960 | fe19e50f955c47b7abb22933d0b406a9bc339ac68056d8d115d1f7277be22c5f |
| [真实 period 与 edge](hybrid-original-high-product-minor-edge-and-coherent-period-research-checkpoint-audit.md) | 285／11326 | 85bd0985a63b56941be5a216111a53f95ec0494fbd08a29cbdf8ac8f20ed93e0 |
| [实际 unit](hybrid-whole-fourth-unit-unit-actual-research-whole.md) | 425／16428 | b3f14cf4ee5659f8e23bd51dc9bf71e853e783bd2d55e42ee8846d6e8d1e41dc |
| [准确 rational slice](hybrid-original-high-product-minor-rational-slice-research-high-product.md) | 337／14790 | 56219e9f136c0f0666c5b1ce028ec4d7d93ad33f5ebd43d5e4a5e34c399677a8 |
| [primitive 变换](hybrid-original-unit-band-primitive-reciprocal-transform-research-root.md) | 188／6954 | 4b13bec23ff399739b26003954a28e0d9d889617955bf6e7a43e428ab3a7aa2c |

另将已核读的 [minor464](hybrid-original-unit-band-minor-lift-research-pc8.md)
§1—5再次全文读回，确认其任意 \(Z\) 产品 cap 合同；该464源的
canonical SHA为 b6018e1254049b77dd5d7f73f4d3a7dc7272d5fe5dd3568f3c5ddf8cf73928b4。

## 2. 原对象与逐 \(q\) 独立重推

先用原 \(\nu\) 零支撑得到共同 \(J_q\subset(0,q^2)\)，再分离同一个
参数族。不得分离后继续使用 individual \((s,n)\) 频带指示。
完整周期的 \(j_0,j_1\) 与残类 \(a\) 无关；两套 rational complement
只决定 \(a\bmod q\)，没有 individual \(s\) 依赖。
原 sharp prime endpoints、真实 \(q\) 最大性及 \(PR\asymp QS\) 保持。

真实 \(k=pr<q^2\) 每个整数至多两条有序 prime factor pairs，
故 \(|C_{q,k}|\le C_\phi/\sqrt{PR}\)。写唯一 \(k=qz+v\)，

\[
0\le z,v<q,\qquad \#\{z:C_{q,qz+v}\ne0\text{ for some }v\}
\ll PR/q+1.
\]

任一共同 \(j\)-prefix 的 \(D_I(v)=\sum_{j\in I}e_q(-jv)\)
满足 \(\sum_v|D_I(v)|\ll q\log(2q)\)。\(v=0\) 在该上界中付
\(|I|\le q\)；实际 \(q\nmid pr\) 另使对应 \(C\) 为零。
作者没有免费删去这一项，也没有混用去 \(q\mid n\) 的 signed 差。

准确 slow 相位是 \(e(-av/q^2)\)，其全 Taylor 展开把
\((v/q)^h\) 留进 \(B_{z,h}\)，把 \((a/q)^h\) 留为残类向量的对角收缩。
每个 \(B_{z,h}\) 与 \(a\) 无关，且

\[
\sum_z|B_{z,h}|^2\ll (PR/q+1)q^2(PR)^{-1}\log^2(2q).
\]

因为 \(z<q\) 无 aliases，逐阶模 \(q\) Parseval 后，Minkowski
只付固定的 \(\sum_h(2\pi)^h/h!=e^{2\pi}\)。独立得到

\[
\sum_a|H_I^0(a)|^2\ll q^2(1+q/(PR))\log^2(2q)
\ll q^2\log^2(2q).
\]

整数 \(+1\) 直到使用 \(PR/q\asymp S\gg1\) 才吸收。
估计对全部 prefixes、共同 twists 和实际 \(q\)-prefix 一致；
没有把随 \(a\) 改变的私有系数塞进 Parseval。

## 3. 真实外 twist 与可积参数

337源给唯一 \(n\)-dependent 外 twist \( (n/(qX))^{it_\nu}\)。
其余 profile、\(g\) 参数只产生固定 prime twists 或 \(n\)-无关外因子。
大 \(M=X/S\) 时，真实 \(j+a/q\asymp M\)，对角乘法权的总 variation
为 \(O(|t_\nu|)\)。向量 Abel 使用共同 prefix 的范数及权增量的
operator norm，所以给 \( (1+|t_\nu|)^2q^2L^2\)。
有界 \(M\) 时只有 \(O(1)\) 个 \(j\)，逐 single-\(j\) triangle 合法；
不用 \(j=0\) 作导数分母，也不用逐 \(a\) 私选最大 prefix。

置 \(h(u)=X\nu(2\pi Xe^u)\)，准确 Mellin 规范为

\[
M_\nu(t)=(2\pi)^{-1}\int h(u)e^{-itu}\,du,
\qquad V(y)=\int M_\nu(t)y^{it}\,dt.
\]

425(13) 给任意固定阶 \(\|h^{(m)}\|_1\ll L^{m/2}\)，
而概率归一化给 \(\|h\|_1\ll1\)。分界 \(|t|=\sqrt L\)，取 \(m=4\)
直接核得 \(\int(1+|t|)^2|M_\nu(t)|dt\ll L^{3/2}\)。
这足以恢复上述平方能量的增长；原 \(C^2\) profile 仍只用原绝对
Fourier \(L^1\) 包络，未被升级光滑性或要求不可积的额外 moments。

## 4. 消费、端周期及范围

任意原允许的 residue mask 只缩小 \(H\) 的非负平方和，故整族
\(E_H\ll Q^3L^C\)。真实 \(s<q\) 的模 \(q\) Parseval 给
\(\sum_qb_q^2\sum_a|F_q(a)|^2\ll QL^C\)，原前因子
\(S/(QX)\) 及同族 Cauchy 正确消费为 \(QS/X\)。
高产品的两端周期仍需另付；作者§6直接以 \(E_F\ll Q\)、
\(E_G\ll Q^3\) 支付整个 edge 同一费用，没有用 \(H\) 自动覆盖它们。

三项 \(s\) 排除修正直接重用真实 \(h=s(q-r)\) 的正 Parseval：
系数能量 \(\ll1/S\)，费用 \(Q/\sqrt X\)；双点至多二对一。
该证明直接适用本 mask，全族 \(O(\sqrt X L^C)\)，
且 \(S\gtrsim\sqrt X\) 使 box 修正不超过 \(QS/X\)。

因此接口的 \(h=1-w\) 消费条件准确等价于 \(u+w<12/7\)。
464一般 cap 本来已覆盖这个产品方面比；作者没有将它重算为新域。
这里的 \(E_H\) 是 \(j\) 方向 signed 和之后的正能量，不能替换
逐 \(n\) 的 \(E_G\) 或324源的 JSC 六腿能量。顶端 \(Q,S\asymp X\)
仍给 \(X\) 费用，尚无新的高产品完整付款、whole、比例或条带边界。
