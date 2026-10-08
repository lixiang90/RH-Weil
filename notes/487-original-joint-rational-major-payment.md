# 487. 原全部有理频率的联合主弧付款

2026-10-08。基线 main `e51a51e2225c9216b23cc7b12bc97e8fa8cf2ea1`。
继续原数域、原 unit 主频带、真实最大素数和同一空间变量。

原完整主弧费用从 \(D^3\sqrt X\log^C X\) 降为
\[
\boxed{|\mathfrak L_{F,\mathrm{major}}^g|
 \ll D^2\sqrt X\log^C X,\qquad 1\le D\le X^{1/10}.}
\]
因此原允许的全部 \(D\) 域现在均可低于 \(X^{5/7}\) 支付。
这项解析付款不增加新的无零假设；高产品次弧仍未付清，
不能据此认领原完整四矩、常数级中心四阶预算、比例或新无零边界。

全部原权、共同参数和完整推导见
[联合有理频率研究源](../reviews/2026-10-08/hybrid-original-unit-band-joint-rational-large-sieve-research-high-product.md)，
不同作者全文复核见
[独立审查](../reviews/2026-10-08/hybrid-original-unit-band-joint-rational-large-sieve-review-peer.md)。
[残类压缩中间稿](../reviews/2026-10-08/hybrid-original-unit-band-major-residue-compression-research-high-product.md)
另给 \(D^{5/2}\) 的独立 CRT 推导，保留作为中间研究证据。

## 1. 准确主弧及固定系数

保持485的真实 \(q,s,p,r,u\)、\(\nu\)、正高度及全部 sharp endpoints。
先完整支付 \(QS\le64DX\) 的低产品 boxes。
在剩余 dyadic boxes中，主弧仍定义为
\[
|n/q-m-a/d|\le D/(dS),\quad
1\le d\le D,\quad0\le a<d,\quad(a,d)=1.
\]
包括 \(d=1,a=0\)；使用的是固定 dyadic \(S\)。
次弧是这一真实有理族的准确 complement。

对一个有实际 \(s,n\) 的非空 packet，置
\[
c=dm+a,\qquad \alpha=\frac c{dq},\qquad
\beta=n-cq/d.
\]
原正高度和高产品 guards给 \(1\le c<q/16\)、\(q>D\ge d\)，
且 \((c,d)=1\)、\(q\nmid c\)，所以 \(\alpha\) 已约分。
约分分母唯一恢复大素数 \(q\) 和 \(d\)，分子再恢复 \(m,a\)。
不同 packets确实给不同频率，不能把重复频率当成分离集合。

单列 \(d=1\)，其余按 \(H<d\le2H\) 联合。
频率的分母至多 \(4HQ\)，且全部在 \((0,1/16)\)，因而模1距离至少
\(1/(16H^2Q^2)\)。这里 \(H\) 只是分母尺度，与486的平方丰满截断无关。

## 2. 先合并整个频率族，再作外权 Cauchy

对与 \(q\) 无关的固定两条 binary 区间和公共 twists，合并真实产品系数
\[
C_k=\sum_{pr=k}b_pb_rp^{it_1}r^{it_2}.
\]
产品长度 \(O(PR)\ll Q^2\)。每个整数产品至多有两个有序素数因子对，
所以 \(\sum_k|C_k|^2\ll1\)。
[加性大筛 Theorem 17.5](https://kskedlaya.org/ant/chapter-17.html)
直接支付整个 \((q,d,a,m)\) 族的能量 \(O(H^2Q^2)\)。
原 principal贡献和全部模 \(d\) 残类包含在这个加性和中，无须另删。
随后通过完整 binary 展开恢复全部 \(q\)-相关严格前缀，代价只有日志。

原产品窗与 residual chirp使用对整个 \(H\) 族共同的 Mellin包络，
绝对积分 \(O(1+D/H)\)；全部 \(C^2\) profile保留同一 \(u\)。
真实 \(p=s,r=s\) 和双点容斥的 sup修正另在整个族中支付。
因此存在非负共同包络 \(F_{q,d,a,m}(u)\)，满足
\[
\sum_{q,d,a,m}F_{q,d,a,m}(u)^2
 \ll(H+D)^2Q^2\log^C X.
\]
这一大筛不作用于真正次弧的原 \(n/q^2\) 频率。

另一 Cauchy 因子来自实际 packet计数：
\(\sum b_q^2\ll H^2X/S\)。每个 packet的整数频率数为
\(O(QD/(HS)+1)\)，其中 \(+1\) 保留。
原 \(s\) 正质量和 \(\nu\) 前因子给整个 \(H\) 族的费用
\[
\frac{(H+D)(QD+HS)}{\sqrt X}\log^C X
 \ll\frac{D^2(Q+S)}{\sqrt X}\log^C X.
\]
恢复所有 \(H\)、全部原 boxes及最大标签位置，得到开头的完整主弧付款。
节省来自内外两次均在完整有理族中求和，不来自删除一个 signed子族。

## 3. 完整产品 cap和扩大后的剩余

对任意 \(n\) 无关的 \((q,s)\) region，重新使用上述共同正包络，
其 \(s\) 正质量不超过全族，故同样可支付该 region的完整主弧。
结合485的完整 \(n\) 产品 cap，严格得
\[
|\mathfrak I_D(qs\le Z)|\ll
(Z/X+1)\log^C X+D^2\sqrt X\log^C X.
\]
它来自完整 cap减去重新支付的完整主弧。
不把 individual次弧频率说成只在物理 near中有支撑。

取 \(Z=X^{1193/700}\)、\(D=X^{1/10}\)，原完整 unit主项缩约为
\[
\boxed{\mathfrak L_U=
\mathfrak I_{X^{1/10},>X^{1193/700}}
+O(X^{493/700}\log^C X)+O(X^{7/10}\log^C X).}
\]
原低产品、\(q\mid n\) 加回、chirp、graph、aliases和边界费用保留。
全部次弧的三个 \(s\) 排除修正仍可按485付到平方根尺度。

在同一 \(D=X^{1/10}\) 下，旧 \(D^3\)、中间 \(D^{5/2}\)、
当前 \(D^2\) 的指数分别为 \(4/5\)、\(3/4\)、\(7/10\)。
只有当前费用低于 \(5/7\)，所以它实际扩大了已付有理频率族。
本笔记暂不扩大原 \(D\le X^{1/10}\) 合同。

剩余仍保持 \(qs>Z\)，因此
\(q>X^{1193/1400}\)、\(s>X^{493/700}\)、\(q/s<X^{207/700}\)，
产品窗还给 \(p,r>s/2\)。原 same-u profiles和所有方面比保留。
尚未证明这个准确高产品次弧的完整 \(F\cdot G\) 联合预算，
也未准入独立 \(G\) 的 \(Q^2(X/S)\) 能量。
项目已知比例、引用输入下的既有边界及完整四矩基线保持。
