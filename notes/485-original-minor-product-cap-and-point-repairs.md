# 485. 原真实次弧的产品域付款与全部 s 排除修正

2026-10-08。基线 main `fdf86cb439a6c5df8ca0a8e8a526b2b9d177d286`。
本笔记继续同一个原数域、原 carrier 和同一空间变量，记录两项完整实际付款。

第一项是原 unit 主频带中全部 \(qs\le Z\) 产品族的次弧：
\[
\boxed{|\mathfrak I_D(qs\le Z)|\ll
 (Z/X+1)\log^C X+D^3\sqrt X\log^C X.}
\]
第二项是整个实际次弧上的 \(p,r\ne s\) 三项容斥修正：
\[
\boxed{|\text{全部 }s\text{ 排除修正}|\ll\sqrt X\log^C X.}
\]
后者也覆盖 \(qs>Z\) 的剩余，解决此前目标(19)的一个真实前件。
完整高产品次弧仍未得到新的上界，不能从这两项费用推断整个四阶矩、
常数级中心四阶预算、零点比例或无零边界。

连续证明、全部原权及参考工具范围见
[研究源](../reviews/2026-10-08/hybrid-original-unit-band-minor-lift-research-pc8.md)，
不同作者的完整复核见
[独立审查](../reviews/2026-10-08/hybrid-original-unit-band-minor-lift-review-peer.md)。

## 1. 同一个主项与准确次弧

保持 \(X=T/(2\pi)\)、\(L=\log X\)、
\(b_p=\log p/(a_LL\sqrt p)\)、\(a_L\ge c_\phi>0\)。
所有 genuine primes 在 \(\sqrt X<p\le X\)；\(q\) 为真实最大素数，
\(s<q\)、\(p,r<q\)，两套 profile沿原 unit 源(4)、(5)，始终保留同一 \(u\)。

原 \(\nu\) 是正概率密度，具有真实正高度支撑和固定相对范围。
主项的相位是
\[
e_q(ns)e_{q^2}(-npr),\qquad n\asymp qX/s.
\]
先加回完整 \(q\mid n\) 块，再在完整 \(n\) 中插入原产品窗
\(g(pr/(qs))\)；这些步骤有各自的完整付款。
先完整支付 \(QS\le64DX\) 的低产品 boxes；
\(\mathfrak I_D\) 只在 \(QS>64DX\) 的高产品 boxes 中定义。
在这些 dyadic \(Q,S\) boxes 中，以
\[
\left|n/q-m-a/d\right|\le D/(dS),\quad
1\le d\le D,\quad (a,d)=1
\]
定义 major，其准确 complement为 minor。
这里 \(S\) 是固定 dyadic scale，不能随 individual \(s\) 改定义。

## 2. 完整产品域不能通过删频率获得

对任意 \(n\) 无关的 \((q,s)\) region，完整 \(q\mid n\) 加回费用
可逐 pair 使用模 \(q\) 矩形范数 \(\sqrt q\) 直接支付；
产品窗和 aliases也有正绝对包络。没有从 signed 总范数推子集范数。

只有在完成整个 \(n\) 后，Poisson 才恢复真实物理核
\(K_0((qs-pr)/(qs))\) 及所有整数 aliases。
原 interior的 carry间隙和 \(\chi\) 尾支付非零 aliases及宽 near之外。
剩余每个 \((q,s)\) 只有
\(O(qs\delta_{\rm near}+1)\) 个整数产品；
\(\delta_{\rm near}\ll X^{-1}L^{5/2}\)，每项四权为 \(O(1/(qs))\)。

这里两腿是 genuine primes，因此每个整数产品 \(a=pr\) 至多有两个
有序 factor pairs。这一步不需要一般 divisor界的 \(X^\epsilon\) 损失，
不能照搬到任意 composite Vaughan系数。
放大 \(q,s\) 到整数后，产品 cap给
\[
\#\{(q,s):qs\le Z\}\ll ZL,\qquad
\sum_{q,s>\sqrt X}(qs)^{-1}\ll L^2.
\]
因此完整 \(n\) 产品族费用为 \((Z/X+1)L^C\)。

major在这个 region中的费用须重新使用原非负共同包络，
仍为 \(D^3\sqrt X L^C\)。两完整项相减，才得到开头的实际 minor付款。
这个推导没有把 individual minor频率说成只在物理 near有支撑。

## 3. 新的完整剩余域

固定 \(0<\eta<3/14\)、\(0<\delta<1/14\)，取
\[
Z=X^{12/7-\eta},\qquad D=X^\delta.
\]
原完整 unit主项准确缩约为
\[
\mathfrak L_U=\mathfrak I_{D,>Z}
 +O(X^{5/7-\eta}L^C)+O(X^{1/2+3\delta}L^C),
\]
其中原 chirp、graph、边界及其他已付项仍按原证明合并。
例如 \(\eta=\delta=1/100\)，两项指数为
\(493/700\) 与 \(53/100\)，均严格小于 \(5/7\)。

\(q/s\ge X^{2/7+\eta}\) 且 \(q\le X\) 强制 \(qs\le Z\)，
所以相应全部真实非平衡 aspects已付。剩余保留 \(qs>Z\)，自动满足
\[
q>X^{6/7-\eta/2},\quad s>X^{5/7-\eta},
\quad q/s<X^{2/7+\eta}.
\]
\(g\ne0\) 和 \(p,r<q\) 还强制
\[
p,r>s/2,
\quad\max(p,r)>X^{6/7-\eta/2}/\sqrt2,
\quad\max(p,r)/\min(p,r)<2q/s.
\]
这些是真实剩余的支撑收缩，不能当成其能量上界。
dyadic表述须保留相应固定倍数。

## 4. 全部 s 求和后的平方根排除修正

不排除 \(p=s,r=s\) 的双腿，减去两个单点项，再加回双单点，
是原系数的精确容斥。对于 \(p=s\)，原相位合为
\[
e_{q^2}\bigl(n\,s(q-r)\bigr).
\]
先利用 \(\nu\) 的零支撑，将各 \(s\) 的频带改写在共同
\[
J_q=\left[\frac{q\theta_-}{4\pi S},
          \frac{q\theta_+}{2\pi S}\right]\cap\mathbb Z,
\qquad |J_q|\ll qX/S.
\]
随后只对 \(V(y)=X\nu(2\pi Xy)\) 作共同 Mellin分离。
其 Fourier绝对积分为 \(L^C\)。分离后不能再保留依赖 \((s,n)\)
的原频带指示函数；全部原同 \(u\) profile和 \(g(r/q)\) 则直接保留
为 \(n\) 无关的有界系数，不提高 \(\phi\) 的光滑性。

固定 Mellin参数后，置 \(h=s(q-r)\)。\(0<h<q^2\le X^2\)，
每个 \(h\) 至多有三个不同的素因子 \(s>\sqrt X\)，每个 \(s\) 确定唯一 \(r\)。
真实外 \(s\) 权与置为 \(p=s\) 的第二条权合在同一系数中，因此
\[
\sum_h|c_{q,h}|^2\ll
\sum_{s,r}|b_s(s/S)b_s b_rR_{q,s,r}(u)|^2\ll S^{-1}.
\]
这个系数节省来自先保留全部 \(s\)，不来自任意频率的“免费正交”。
完整 \(q^2\) Parseval和正平方和给
\[
\sum_{q\sim Q}\sum_{n\in J_q\ \mathrm{minor}}
 |H_{q,n}|^2\ll Q^3/S.
\]
原外权和前因子随后给
\[
\frac S{QX}\sqrt{\frac{QX}{S}}\sqrt{\frac{Q^3}{S}}
 =\frac Q{\sqrt X}.
\]
\(r=s\) 对称；双单点的 \(h=s(q-s)\) 至多二对一，费用更小。
恢复全部 boxes、原最大标签位置、同 \(u\) 和共同 Mellin包络，
得到完整 \(O(\sqrt X L^C)\) 修正。任意 minor mask只在正平方和中放大。

## 5. 仍需真实 prime-product 或联合抵消

剥离已付修正后，原共同 Fourier/Mellin参数上的主项可写为
\[
F_{q,n}=\sum_{s\in S_q}b_s(s/S)s^{it_3}e_q(ns),\qquad
G_{q,n}=\sum_{p,r<q}b_pb_rp^{it_1}r^{it_2}e_{q^2}(-npr).
\]
\(S_q\) 保留 \(s<q\)、interior和 \(qs>Z\) 的真实 \(n\) 无关域。
原 \(g\)、profiles及严格 \(q\)-prefix须以共同包络恢复。
素数 \(s\) 的完整 period Parseval已给
\[
\sum_qb_q^2\sum_{n\in J_q}|F_{q,n}|^2\ll QX/S\,L^C.
\]
下一能量目标仍是实际 minor中的
\[
\sum_{q\sim Q}\sum_{n\in J_q\ \mathrm{minor}}|G_{q,n}|^2
 \ll Q^2(X/S)X^\epsilon,
\]
并要求常数在原共同参数包络中一致或可积。
自然 \(q^2\) 费用为 \(Q^3\)；普通平方模大筛没有提供所缺的
\(QS/X\) resolution省因子。
研究源还给出任意整数系数的窄频带过采样诊断；它不反驳真正的
genuine-prime两腿目标，不能用那个模型代替本主项。

本轮未以有限素数采样认证任何无限界，也未调用无逆元适用桥的
Kloosterman定理。原 canonical完整四矩、已知比例和引用输入下的
无零边界保持。下一任务已收缩到上述高产品域内保留原轮廓的实际联合均值。
