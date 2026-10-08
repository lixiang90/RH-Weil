# 489. 保留外层素数相消后的高产品次弧切片

2026-10-08。基线 main `a4e4c8cf3de71450325174028f0ed09dd5ef4dec`。
在487的准确高产品次弧内，本轮完整支付新增有理子族
\[
W<d\le B,\quad(a,d)=1,\quad|n/q-m-a/d|\le1/S,
\qquad |\mathfrak J_{W,B,>Z}|\ll B\sqrt X\log^C X.
\]
保持 \(W=X^{1/10}\)、\(Z=X^{1193/700}\)，取 \(B=X^{1/5}\) 时费用为
\(X^{7/10}\log^C X\)。全部原素数权、共同空间变量、真实最大标签、
正高度载体和 sharp endpoints 保留。

完整推导见[新有理切片研究源](../reviews/2026-10-08/hybrid-original-high-product-minor-rational-slice-research-high-product.md)，
不同作者全文复核见[独立审查](../reviews/2026-10-08/hybrid-original-high-product-minor-rational-slice-review-peer.md)。
[独立素数腿研究](../reviews/2026-10-08/hybrid-original-high-product-minor-prime-leg-research-checkpoint-audit.md)
另核实际 \(F\) 的最大区间大筛接口和普通点值路线的费用门槛。
新增付款不使用新的无零假设，没有 finite 素数采样。

## 1. 两套准确条件

旧主弧仍是 \(d\le W\)、半径 \(W/(dS)\)。
本次仅在其 complement 且 \(qs>Z\) 中，支付 \(W<d\le B\)、半径 \(1/S\)
的全部原频率。这里 \(S\) 为 dyadic scale，与 individual \(s\) 无关。
不能把新子族改写成半径 \(B/(dS)\) 的完整主弧。

新域的真实 \(s\) 支撑是 dyadic interval 与 \(s<q\)、
\(q-s>4q\delta_{\rm near}\)、\(qs>Z\) 的交集。
这是端点随 \(q\) 变化的素数区间；证明只推广到固定有限个区间的 union，
不推广到任意 \(q\)-私有稀疏掩码。

由当前高产品支撑，\(B^2\ll S\)、\(QS>64BX\)、\(q>B\)。
对新非空 packet，\(c=dm+a\) 满足 \(1\le c<q/16\)，
\(c/(dq)\) 已约分且唯一恢复 \(q,d,a,m\)。
固定 \(H<d\le2H\) 的频率模1距离至少 \(1/(16H^2Q^2)\)。

## 2. 共同参数后保留两个素数和

先用 \(\nu\) 的零支撑把所有真实频率写入共同 \(J_q\)，再作 Mellin 分离。
原 \(g(pr/(qs))\) 单独分离，全部 \(C^2\) profile 保留同一 \(u\)。
写 \(\beta=n-cq/d\)，有 \(|\beta|\le q/S\)。
外、内相位分别成为
\[
e_q(ns)=e(as/d)e(\beta s/q),\qquad
e_{q^2}(-npr)=e(-cpr/(dq))e(-\beta pr/q^2).
\]
用固定的 \(s/S\) 和 \(pr/(PR)\) 光滑窗支付 residuals，
两套共同 Mellin 包络绝对积分均为 \(O(1)\)。
后一窗与 \(s\) 无关；不能用旧依赖 \(s\) 的绝对包络破坏外层相消。

对每组固定共同 twists，外素数区间和由 \(R_{d,a}\) 支配。
在 \(a/d\) 的整个频率族上，最大区间 additive 大筛给
\[
\sum_{d,a}R_{d,a}^2\ll(H^2+S)\log^C X\ll S\log^C X.
\]
内素数产品在完整 \((q,d,a,m)\) 族的大筛能量为 \(H^2Q^2\log^C X\)；
genuine-prime 产品至多两对因子，严格 \(q\)-前缀以 binary 区间恢复。
两项都是共同参数的固定系数估计。

## 3. 联合付款与准确剩余

每个 \(q,d,a\) 的 \(m\) 数为 \(O(X/S)\)，\(\sum_qb_q^2\ll1\)。
所以外素数和的加权 packet 能量为 \(O(X\log^C X)\)。
与内产品能量在同一个完整族作 Cauchy，得到 \(HQ\sqrt X\log^C X\)。
每个 packet 的整数 \(n\) 个数 \(O(Q/S+1)\)，保留 \(+1\)；
原前因子 \(S/(QX)\) 因而给
\[
H(Q+S)\log^C X/\sqrt X.
\]
恢复全部 \(H\le B\)、boxes 和真实最大标签，得 \(B\sqrt X\log^C X\)。
原 \(p=s,r=s,p=r=s\) 的精确容斥重新在这个准确 \(q,n,S\) 掩码上
用全周期正 Parseval 支付到平方根尺度，不从 signed 总界推子集界。

令 \(\mathfrak K_{W,B,>Z}\) 为旧高产品次弧中再删除此已付切片后的准确余项。
严格有
\[
\boxed{\mathfrak L_U=\mathfrak K_{X^{1/10},X^{1/5},>X^{1193/700}}
 +O(X^{493/700}\log^C X)+O(X^{7/10}\log^C X).}
\]
剩余同时排除旧小分母宽弧和新增中分母 \(1/S\) 弧。
一般 \(B=X^\kappa\)、\(1/10<\kappa<3/14\) 也可低于 \(5/7\) 支付；
\(1/5\) 是保持当前 \(7/10\) 费用的具体值。

高产品余项仍保留全部原 \(qs>Z\)、prime-product、方面比及共同参数。
尚未证明它的完整 signed \(F G\) 预算或独立 \(G\) restricted-band 能量。
完整四矩、中心四阶常数、零点比例及既有无零边界没有改善。
