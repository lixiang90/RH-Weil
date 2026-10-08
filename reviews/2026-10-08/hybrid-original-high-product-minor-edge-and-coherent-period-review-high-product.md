# 高产品次弧 edge 与 coherent-period 的不同作者全文审查

2026-10-08，high_product_joint。基线 main
`3afd19318bf9c6fd6b3a1472929d13b4484698d3`。
**结论：限定数学 PASS；没有要求作者修改冻结源。**

本轮一次 FULL READ [作者研究源](hybrid-original-high-product-minor-edge-and-coherent-period-research-checkpoint-audit.md)
全部285行，11326 canonical LF bytes，SHA256
`85bd0985a63b56941be5a216111a53f95ec0494fbd08a29cbdf8ac8f20ed93e0`。
canonical LF只替换CRLF/lone CR，不trim。
连续研究轮已全文读489、337行切片源、actual425及minor464，
本轮也核其实际量词。以下是数学审查，没有有限采样或新的无限估计检查器。

## 1. 共同频窗与完整整数 period

作者先以 \(\nu\) 的零支撑恢复 \(J_q=[l_q,h_q]\cap\mathbb Z\)，
再分离公共参数；不在分离后保留 individual \((s,n)\) 频带mask。
原两套有理排除严格随 \(n\mapsto n+q\) 只平移整数 \(m\)，
所以剩余 \(K\) 的有理mask只依赖 \(n\bmod q\)。

对 \(I_j=(jq,(j+1)q]\cap\mathbb Z\)，其全部整数落在 \([l_q,h_q]\)
当且仅当 \(jq+1\ge l_q\)、\((j+1)q\le h_q\)。
故作者的
\[
 j_0=\lceil(l_q-1)/q\rceil,\qquad j_1=\lfloor h_q/q\rfloor-1
\]
准确，包括可整除端点。\(j_0>j_1\) 时没有完整period。
剩余 \(E_{q,S}\) 最多两个长度严格小于 \(q\) 的端interval；
每个模 \(q\) residue出现至多两次。短窗跨网格边界时也成立。
这是共同 \(J_q\) 的分解，未把原每个 \(s\) 的 \(\mathcal I_{q,s}\)
端点改写成公共端点。

## 2. cap内的实际 edge付款

固定 \(0<\eta<1/100\)、\(Z_2=X^{12/7-\eta}\)，
\(Z<qs\le Z_2\) 对每个 \(q\) 只给真实 \(s\) interval再加
\(Z/q<s\le Z_2/q\)。它仍与 \(n\) 无关；strict endpoints保持。
因 \(s<q\)，所有 \(s\) 的模 \(q\) residues互异。
对任一固定共同参数，一个完整 \(q\)-period的 \(F\) 正能量为
\(q\sum_s|b_s(s/S)|^2\ll qL^C\)。最多两次residue给
\[
 E_{F,\mathrm{edge}}
 \le2\sum_qb_q^2q\sum_s|b_s(s/S)|^2\ll QL^C.
\]
这里可直接保留实际 \(q\)-相关系数；不是联合大筛中自由换系数。

\(p,r<q\) 使 \(0<pr<q^2\)，每个整数prime-product至多两个有序pairs。
完整 \(q^2\) 正Parseval给 \(E_{G,\mathrm{edge}}\ll Q^3L^C\)，
可以合法限制到本准确非负频率mask。两项在同一公共参数上Cauchy得
\[
 \frac S{QX}\sqrt Q\sqrt{Q^3}\,L^C=\frac{QS}{X}L^C.
\]
非空 cap box有 \(QS<qs\le Z_2\)，恢复全部boxes、同一 \(u\)
及四个真实最大位置后为 \(X^{5/7-\eta}L^C\)。
等价省幂是 \(f=1-w,g=0\)，真实cap的 \(u+w\le12/7-\eta\)
给 \(f+g-(2u+w-17/7)\ge2\eta-O(1/L)\)。
没有把整个这些方面比的 \(K\) 当成已付款。

## 3. 原 s排除与准确新剩余

单点 \(p=s\) 的相位是 \(e_{q^2}(ns(q-r))\)。
\(h=s(q-r)\in(0,q^2)\)，每个非零 \(h<X^2\) 最多三个
prime因子 \(s>\sqrt X\)，给系数正能量 \(O(1/S)\)。
原同一 \(u\) profile与 \(g(r/q)\) 留在 \(n\) 无关系数；cap仍与 \(n\) 无关。
\(q^2\) 正Parseval以及作者保留的共同 \(J_q\) 外权给 \(Q/\sqrt X\)。
\(r=s\) 对称；\(h=s(q-s)\) 最多二对一的双点更小。
全部修正为 \(O(\sqrt X L^C)\)，被 \(X^{5/7-\eta}\) 支配。
作者直接重证该mask的正上界，未由signed全次弧界推子集界。

新剩余身份准确：\(qs>Z_2\) 保留全部旧 \(K\) 频率，
\(Z<qs\le Z_2\) 仅删除共同 \(J_q\) 的两个端period。
旧cap、两套已付有理弧和旧physical误差仍沿489的整体范围。
作者(13)没有免费删除较高产品的edge，也没有重切旧signed误差。

## 4. 产品感知 G点界与 Lp费用

\(\alpha=n/q^2\asymp X/(qS)>0\)，\(b=\lfloor1/\alpha\rfloor\)。
在连续 \(b\) 个 \(r\) 中，\(1\le h\le b-1\) 给圆距离
至少 \(\min\{\alpha,1-\alpha(b-1)\}\ge1/(b+1)\)。
每块普通additive大筛付 \(P+b\)，先与真实 \(r\) 系数Cauchy，
再对全部 \(O(R/b+1)\) 块Cauchy，得到
\[
 |G|^2\ll(PR/b+P+R+b)L^C\ll XL^C.
\]
最后使用 \(PR\asymp QS\)、\(q\asymp Q\)、\(P,R\ll q\)、
\(b\asymp qS/X\ll X\)。全部twists模为1，strict prefix只置零，
常数对共同参数大小一致，原 \(C^2\) 包络只需 \(L^1\) 恢复。

作者Lp表使用 \(A=Q^2X/S\) 的固定尺度归一化，实际点数至多 \(CA\)。
\(D_2(F)\ll L^C\)、\(D_2(G)\ll\sqrt{QS/X}L^C\)、
\(D_\infty(G)\ll\sqrt X L^C\) 的消费与(6)—(7)指数均核准。
\(p\le2\) 插值的额外费用因子 \((X^2/(QS))^{1/2-1/p'}\ge1\)；
\(L^4/L^{4/3}\) 新输入门槛为 \(3t-h_4>4\gamma-20/7\)，
最容易处 \(t>179/2100-O(1/L)\)、balanced端点 \(t>8/21\)。
这些是当前已知上界的费用门槛，不是实际矩或能量的下界。

## 5. coherent H的真实 j集合与scope

完整period写 \(n=a+qj\)，\(1\le a\le q\)、\(j_0\le j\le j_1\)。
\(a=q\) 已被旧小分母弧排除，\(F_{q,n}=F_q(a)\)。
\(H_q(a;\lambda)\) 严格保留 \(\varepsilon_{q,a+qj}(\lambda)\)，
包括 \(n^{it}\) 等真实外相位；不为不同 \(j\) 改twists。
真实 \(j_0,j_1\) 与 \(a\) 无关，来自上述完整period网格。
两个产品区间在完整period中可按原 \(s\) 系数精确相加，恢复全部
\(qs>Z\) 的该组件；高于 \(Z_2\) 的edge仍是另一个未付组件。

\(F\) 的残类加权能量 \(\ll QL^C\)，若作者(15)的coherent能量输入
成立，严格消费为 \(Q\sqrt{S/X}X^{-h/2}L^C\)。
普通 \(j\)-Cauchy只供 \(h=0\)，因为真实完整period数 \(O(X/S)\)。
作者未假装证明该新输入，也明确(15)单独不控制较高产品edge。

本审查支持无条件 \(\sqrt X\) 点界与 cap内完整edge子族付款，
并支持其准确剩余及coherent输入消费。它不认证未证的coherence省幂、
完整 \(K\) 预算、whole界、常数中心四矩、零点比例或无零边界。
未修改作者源、其他冻结文件或Git。
