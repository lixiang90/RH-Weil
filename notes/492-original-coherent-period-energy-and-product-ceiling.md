# 492. 原完整周期的正能量付款及产品上限

2026-10-08。基线 main 62469c0ec568ad5680f07413714a8320bedb40f8。
这是上次复盘后的第2轮。继续[491](491-original-period-edges-and-signed-core-statistics.md)
的实际完整周期，不改变原素数函数、数域、观察窗或冻结输入。

本轮证明了491中原先未付的coherent正能量输入：
\[
\boxed{\sum_{q\sim Q}\sum_{a\in\Omega_q}
 |H_q(a;\lambda)|^2
 \ll_\phi (1+|t_\nu|)^2 Q^3\log^C X.}
\]
其中 \(t_\nu\) 是原时间权的共同Mellin参数。
其带权矩可积，所以恢复全部参数后只有对数损失。
相比普通j-Cauchy的 \(Q^3X/S\)，实际节省了 \(X/S\)。
这里先沿j保留相位求和，再取残类正能量；
不能反推未合并的 \(\sum_n|G_{q,n}|^2\) 或旧JSC能量也有同一节省。
但原主项费用仍为 \(QS/X\)：这只回到此前已知的完整产品cap，
没有扩大 \(QS>X^{12/7}\) 的已付范围，也没有改善完整四矩、
实际中心四阶常数、零点比例或无零边界。

完整证明见[研究源](../reviews/2026-10-08/hybrid-original-coherent-period-energy-research-checkpoint-audit.md)，
不同作者审查见[独审](../reviews/2026-10-08/hybrid-original-coherent-period-energy-review-high-product.md)。

## 1. 实际素数产品与完整周期

保留原最大prime \(q\)、\(p,r<q\)、dyadic \(PR\asymp QS\)、
共同参数、sharp前缀与两套同一空间变量的profile。
先由 \(\nu\) 的零支撑得到共同 \(J_q\)，再作参数分离。
完整周期写成 \(n=a+qj\)，\(1\le a\le q\)，共同整数两端
\(j_0\le j\le j_1\) 与 \(a\) 无关。
原两套有理删弧的剩余mask只依赖 \(a\)，记 \(\Omega_q\)。

对任何共同j-prefix \(I\)，合并实际乘积系数
\[
C_{q,k}=\sum_{pr=k}b_pb_rp^{it_p}r^{it_r},\qquad
|C_{q,k}|\ll(PR)^{-1/2},\quad 0<k<q^2.
\]
关键是每个整数乘积至多两个有序genuine-prime因子对。
写 \(k=qz+v\)，\(0\le z,v<q\)。实际z支持只有
\(O(PR/q+1)\) 个整数；这个 \(+1\) 必须保留。

置 \(D_I(v)=\sum_{j\in I}e_q(-jv)\)。
共同频率窗在 \((0,q^2)\) 内，故prefix长度不超过 \(q\)，
完整残类几何和给
\(\sum_{v\bmod q}|D_I(v)|\ll q\log(2q)\)，含 \(v=0\)。
再对慢相位作准确收敛展开
\[
e(-av/q^2)=\sum_{h\ge0}\frac{(-2\pi i)^h}{h!}
 (a/q)^h(v/q)^h.
\]
每一项的z系数平方和至多
\[
(PR/q+1)\frac{q^2}{PR}\log^2(2q).
\]
模q的a-Parseval、乘 \((a/q)^h\) 的范数收缩及整个factorial和，
给任意该共同prefix的真实untwisted能量 \(O(q^2\log^C X)\)。
这没有逐k丢掉j相消，也没有免费删除正负折叠层。

## 2. 原外相位与参数恢复

真实 \(n^{it_\nu}\) 唯一来自
\(V(sn/(qX))\)，其中 \(V(y)=X\nu(2\pi Xy)\)。
原g和C²空间profile只给s、p、r、q、u相位，没有额外n-twist。
对完整周期，\(j+a/q\asymp X/S\)；向量Abel在同一共同prefix上
保留全部外相位，只付 \(1+|t_\nu|\)。
无需为每个a另选参数，也无需把最大prefix逐点取出。

原 \(\nu\) 已有全固定阶导数估计。令 \(h(u)=V(e^u)\)，
\(\|h^{(m)}\|_1\ll\log^{m/2}X\)。
固定四阶分部积分足以给
\(\int(1+|t_\nu|)^2|\widehat V(t_\nu)|dt_\nu\ll\log^C X\)。
其他参数仍只用原C²包络的L1，不提高原profile光滑性，
也不截断Mellin尾。任意固定残类mask只收缩这个正能量。

F的真实加权残类能量为
\(\sum_q b_q^2\sum_a|F_q(a)|^2\ll Q\log^C X\)。
因此原前因子 \(S/(QX)\) 消费为 \(QS/X\)。
原s排除仍在同一准确mask上重新用非负Parseval付款，
全部为 \(O(\sqrt X\log^C X)\)，没有由旧signed全界截取子集。

## 3. 这项进展改变了什么

旧[485](485-original-minor-product-cap-and-point-repairs.md)及
[487](487-original-joint-rational-major-payment.md)已经允许一般
\(Z=X^{12/7-\eta}\) 的完整产品cap；489采用1193/700只是具体配置。
所以本轮的新正能量证明虽准入了实际 \(h=1-w\) 的coherent节省，
其费用仍不能当成新whole产品域或新的方面比付款。
491已付端周期与这里的完整周期也都回到同一 \(QS/X\) 费用。

如果独立H能量将来还能得到
\(Q^3X^{-r}\log^C X\)，完整周期的充分付款门槛变为
\[
r>2(u+w-12/7),\qquad Q=X^u,\ S=X^w.
\]
这不是必要输入或能量下界；直接证明带F权的signed联合预算也可能够用。
此外高产品端周期仍须另付，单独改善H不能覆盖整个准确剩余。

上述证明中的实际系数为
\(B_{q,z,h,I}=\sum_{v<q}C_{q,qz+v}D_I(v)(v/q)^h\)。
现有全q,z平方和为 \(O(Q^2\log^C X)\)。
若该真实量有 \(X^{-r}\) 节省，且所有共同prefix、原参数与Taylor阶数
的常数可合法恢复，就足以给前述更强H能量；这也是充分旁路，
不是所有signed联合方法都必须满足的条件。

## 4. 普通素数前缀直接代入的费用

先在零twist这个有利版本中，额外给出
\(\psi(x)=x+O(x^\theta\log^C x)\)、\(1/2\le\theta<1\)
的ordinary prefix输入。先减去proper powers，其
\(O(P_+^{1/2}\log^C X)\) 误差被 \(\theta\ge1/2\) 吸收。
置 \(N=PR\asymp QS\)，令 \(P_+=\max(P,R)\)、\(P_-=N/P_+\)。
固定较短prime腿并对较长腿作带 \(p^{-1/2}\) 权的部分求和，
一个长度不超过q的真实product-cell累计误差至多
\(\sqrt{P_-}P_+^{\theta-1/2}\log^C X
=\sqrt N P_+^{\theta-1}\log^C X\)。
实际q-prefix和product-cell两端只使每个短腿的长腿区间截短。

对j频率约 \(M=X/S\)、长度 \(O(M)\) 的共同Dirichlet窗，
其总variation为 \(O(M\log^C X)\)，所以这种直接Abel消费的
误差费用相对当前 \(|B_{q,z,0,I}|\ll q/\sqrt N\log^C X\) 是
\[
\frac{\sqrt N P_+^{\theta-1}(X/S)}{q/\sqrt N}
\asymp \frac{X}{P_+^{1-\theta}}\ge X^\theta.
\]
因此仅把ordinary prefix上界代入这个绝对费用表，连这个有利版本
也没有省幂；这不反驳真实prime相关能相消，也不证明该误差饱和。
这里只核算这条消费方式，不准入额外无零前件、非零twist参数矩或尾部合同。

下一轮应消费真实素数乘积系数的相位结构，尝试控制原mask上的
signed协方差或带F权的联合和；继续优化时间权正则性、
单独改变Hölder指数或重新扩大已知产品cap，不会解决目前的高产品瓶颈。
原完整目标和新纪录论文的发布条件保持。
