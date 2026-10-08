# 原高产品次弧：保留素数 s 腿的完整有理子族付款

2026-10-08，high_product_joint。基线 main
`a4e4c8cf3de71450325174028f0ed09dd5ef4dec`。
只新增本研究源，不改旧冻结文件、检查器、输出或 Git。

本稿取得原准确高产品次弧中的一项新实际付款。
旧主弧仍以 \(W=X^{1/10}\) 定义；在其准确 complement 内，
将全部存在
\[
 W<d\le B,\qquad (a,d)=1,\qquad
 |n/q-m-a/d|\le1/S
\]
的原真实频率完整付到 \(O_\phi(B\sqrt X\log^C X)\)。
这里 \(S\) 是原 dyadic scale，\(B=X^{1/5}\) 时费用为 \(X^{7/10}\log^C X\)。
付款保留全部原 \(q,s,p,r,u\)、profile、prime 权和准确 sharp endpoints。
关键是把 \(s\) 素数 Fourier 和保留到同一个有理族的 Cauchy 之后。

它没有证明剩余完整高产品次弧或独立 \(G\) 的目标能量，
没有新的 whole 四矩、中心四阶常数预算、零点比例或无零边界。
新 \(1/S\) 半径与旧 \(W/(dS)\) 定义有区别，本文明确保留两套条件。

## 1. 全文读取的冻结实际输入

哈希按 UTF-8、CRLF/lone CR 转 LF，不 trim、不改变末尾换行。
下列源均已 FULL READ；本次再次全文读487与340行联合大筛源，
并消费原 minor464第6—7节和原 major378第7节的准确对象：

| 源 | 行数／字节 | SHA256 |
| --- | --- | --- |
| [原 actual unit425](hybrid-whole-fourth-unit-unit-actual-research-whole.md) | 425／16428 | b3f14cf4ee5659f8e23bd51dc9bf71e853e783bd2d55e42ee8846d6e8d1e41dc |
| [原 major378](hybrid-original-unit-band-joint-cancellation-research-whole.md) | 378／14896 | 7c95bd2e700c16e0b0e836063f7545e8222a4de4b03d60c3271965252ec744b4 |
| [原 cap／修正464](hybrid-original-unit-band-minor-lift-research-pc8.md) | 464／17560 | b6018e1254049b77dd5d7f73f4d3a7dc7272d5fe5dd3568f3c5ddf8cf73928b4 |
| [联合有理大筛340](hybrid-original-unit-band-joint-rational-large-sieve-research-high-product.md) | 340／14702 | 92989568fd5ffbe25a8f6f47997c9ced10acd96b8d3732c740d2cb8a7563ee7e |
| [已准入487](../../notes/487-original-joint-rational-major-payment.md) | 113／5156 | 1768ac94f1d72b1934fa6b8c7290e78717bd2082214e562fde5586c2d788de7d |

仍取 \(X=T/(2\pi)\)、\(L=\log X\)、
\(b_p=\log p/(a_LL\sqrt p)\)、\(a_L\ge c_\phi>0\)。
所有 genuine primes 在 \((\sqrt X,X]\)，\(q\) 为真实最大素数，
\(s<q\)、\(p,r<q\)。全部原两套 same-u profiles沿 actual425(4)、(5)；
\(p,r\ne s\) 的精确修正保留到第7节。
\(\nu\)、时间 floor、正高度 \(\theta_\pm\)、interior carry间隙与原 \(g\)
都不改变。另两个最大标签位置交换两对后取共轭。

固定真实 dyadic \(Q,S,P,R\)，始终保留 \(PR\asymp QS\)、
\(P,R\ll Q\)、所有 prime dyadic endpoints 与严格 \(q\)-prefix。
令 \(Z=X^{1193/700}\)。当前487的准确未付对象是
\(qs>Z\) 内的旧 minor：不存在 \(1\le d\le W\) 使
\[
 |n/q-m-a/d|\le W/(dS),\qquad (a,d)=1.
\tag{1}
\]
真实外 \(s\) 支撑还保留 \(s<q\)、\(q-s>4q\delta_{\rm near}\)。
因此固定 \(q\) 的 \(s\) 集合是原 dyadic interval 与这些上下阈值的交集。
它是一个真实 prime interval，端点可随 \(q\) 变，且没有 \(n\) 依赖。

本文最大区间大筛只支持这种 interval，或固定有限个 intervals 的 union。
**不推广到任意 \(n\) 无关 \((q,s)\) region**；
任意 \(q\)-私有稀疏 \(s\) mask不能凭区间最大大筛免费付款。

## 2. 新有理子族和原准确次弧的关系

取 \(W<B\)，下文最终用 \(B=X^{1/5}\)。
定义 \(\mathfrak J_{W,B,>Z}\) 为旧准确 minor中保留全部满足
\[
 W<d\le B,\quad0\le a<d,\quad(a,d)=1,\quad m\in\mathbb Z,
 \qquad |n/q-m-a/d|\le1/S
\tag{2}
\]
的原真实频率。
它是实际 \(q,n,S\) mask，与 individual \(s\) 无关。
重叠时按固定顺序选一条表示，后面非负上界允许放大到全部 packets。
若 \(d\le W\) 满足 \(1/S\) 条件，它已经满足(1)，所以不会出现在旧 minor。
因此(2)恰是把分母族增大以后新增的那部分原频率。

分母按 \(H<d\le2H\) dyadic分组，并与 \((W,B]\) 相交。
最小相交族有 \(H>W/2\)，末族在 \(B\) 截断。
对每个实际非空 packet置
\[
 c=dm+a,\qquad \beta=n-cq/d,\qquad \alpha=c/(dq),
 \qquad |\beta|\le q/S.
\tag{3}
\]
当前高产品域 \(qs>Z\) 给 \(QS>Z/4\)，\(S>X^{493/700}/2\)、
\(q>X^{1193/1400}\)（真实 \(s\) 与 dyadic \(S\) 要区分固定倍数）。
对 \(B=X^{1/5}\)，充分大 \(X\) 有
\[
 B^2\ll S,\quad B<q,\quad QS>64BX.
\tag{4}
\]
沿原正高度，\(X/(2S)\le n/q\le3X/S\)。
所以 \(c\) 是正整数，且
\(1\le c\le4dX/S<q/16\)。
又 \((c,d)=1\)、\(q\nmid c\)，\(c/(dq)\) 确为 reduced fraction。
分母唯一恢复大于 \(B\) 的 prime \(q\)，再恢复 \(d\)；分子唯一恢复 \(m,a\)。
不同 \((q,d,a,m)\) packets给不同 \(\alpha\)，都在 \((0,1/16)\)。
固定 \(H\) 族的模1 spacing至少 \(1/(16H^2Q^2)\)。
这些是对新的非空实际 packets重推的 guards，未把原 \(D\) 域直接改成 \(B\)。

每个 \(q,d,a\) 的 \(m\) 种数 \(O(M)\)，\(M=X/S\ge1\)，
每个 packet的实际整数 \(n\) 种数为
\[
 K\ll Q/S+1.
\tag{5}
\]
\(+1\) 保留；不假设 packet中始终有多个或均匀分布的整数频率。

## 3. 先用零支撑改到共同 n 窗，再作共同参数分离

置 \(V(y)=X\nu(2\pi Xy)\)。其真实相对支撑在固定正紧区间内，
\(V\) 的前两阶对数导数只损失 \(L^C\)，故 Mellin变换绝对积分为 \(L^C\)。
固定 \(q,S\)，先利用 \(\nu\) 的零支撑，把原各 \(s\) 的频带写在共同
\[
 J_q=\left[\frac{q\theta_-}{4\pi S},
           \frac{q\theta_+}{2\pi S}\right]\cap\mathbb Z,
 \qquad |J_q|\ll qX/S,\quad J_q\subset(0,q^2).
\tag{6}
\]
对各真实 \(s\)，\(V(sn/(qX))\) 仍准确恢复原频带。
分离后不能再保留那个依赖 \((s,n)\) 的旧频带指示函数。
新旧 rational masks则只依赖 \(q,n,S\)，可在 \(s\) 求和外保持原样。

原前因子精确为
\[
 \frac{2\pi s}{q}\nu(2\pi sn/q)
 =\frac{2\pi S}{QX}\frac Qq\frac sS\,V(sn/(qX)).
\tag{7}
\]
\(Q/q\) 有固定上界。\(V\) Mellin分离把 \(s^{it}\) 放进 \(F\)，
\(n^{it}(qX)^{-it}\) 留在外面，模长1。
原 \(g(pr/(qs))\) **单独** 作固定 Mellin分离；
全部 \(C^2\) profiles沿原同 \(u\) Fourier包络分离，绝对积分只有 \(L^C\)。
它们只把固定 twists放进 \(s,p,r\)，或在外乘单位 \(q,u\) 相位。

现在同时保留两个相位的 residual：
\[
 e_q(ns)=e(a s/d)e(\beta s/q),\qquad e(ms)=1,
\]
\[
 e_{q^2}(-npr)=e(-\alpha pr)e(-\beta pr/q^2).
\tag{8}
\]
选择固定光滑窗 \(h_F=1\) 于 \([1,2]\)，支撑在 \((1/2,3)\)；
\(h_G=1\) 于 \([1,4]\)，支撑在 \((1/2,8)\)。
原 dyadic supports使 \(h_F(s/S)\)、\(h_G(pr/(PR))\) 准确等于1。
两套 residual窗分别为
\[
 h_F(e^t)e(\zeta_Fe^t),\quad \zeta_F=\beta S/q,\quad |\zeta_F|\le1,
\]
\[
 h_G(e^t)e(-\zeta_Ge^t),\quad \zeta_G=\beta PR/q^2,
 \quad |\zeta_G|\ll PR/(QS)\ll1.
\tag{9}
\]
每套共同 Mellin包络均可取 \(C/(1+|t|)^2\)，绝对积分 \(O(1)\)。
第二套使用固定 \(PR\)，与 \(s\) 无关。
不能把旧 \(H_z(pr/(qs))\)、\(z=\beta s/q\) 的 \(s\)-依赖绝对包络
直接配上一个已经保留 cancellation的 \(F\)；那会破坏下面的因子化。

因此对每组**固定且共同**参数 \(\lambda\)，基本两腿准确是
\[
 F_{q,d,a}(\lambda)=
 \sum_{s\in\mathcal S_q} b_s(s/S)s^{it_s}e(a s/d),
\]
\[
 G_{q,d,a,m}(\lambda)=
 \sum_{\substack{p,r\ \mathrm{actual}\\p,r<q}}
 b_pb_rp^{it_p}r^{it_r}e(-\alpha pr).
\tag{10}
\]
这里 \(\mathcal S_q\) 是第1节的真实 prime interval，全部原 \(u\) 同一。
原联合主项是这些 \(F G\) 的共同参数积分。
每个 packet内不同 \(n\) 的 residual Mellin系数可以不同，
但都被同一个可积正包络控制；在(10)中固定系数不随 \(q,m,n\) 私下改变。
\(s,p,r\) twists可能共享某些公共参数，所有以下界对参数大小一致，
所以也允许它们共享参数，而不需要人为独立化。

## 4. 真正 s 素数区间的 rational平均与最大前缀

本次核读的唯一外部工具仍是
[Kedlaya，Theorem17.5](https://kskedlaya.org/ant/chapter-17.html)
的 ordinary additive大筛，费用 \(\rho^{-1}+N\)。
真实 reduced \(a/d\)、\(H<d\le2H\) 的模1 spacing至少 \(1/(4H^2)\)。
固定共同 \(t_s\)，置
\[
 R_{d,a}(\lambda)=
 \max_{I\subset(S,2S]}\left|
 \sum_{\substack{s\in I\\s\ \mathrm{prime}}}
 b_s(s/S)s^{it_s}e(a s/d)\right|,
\tag{11}
\]
最大值只取整数端点的 intervals。
实际 \(q\)-相关 \(\mathcal S_q\) 均为其中一个 interval，故
\(|F_{q,d,a}(\lambda)|\le R_{d,a}(\lambda)\) 对全部实际 \(q\) 同时成立。

固定区间先用大筛，整数长度 \(O(S)\)，系数能量
\(\sum_s|b_s(s/S)s^{it_s}|^2\ll1\)。
为了恢复全部不同 \(q\) 的端点，每个前缀作完整 binary展开，
逐频率 Cauchy付 \(O(L)\)，再对所有固定 binary块使用同一大筛。
各层块彼此不相交；块能量之和每层至多原全系数能量。
因此最大前缀及两端点之差只添 \(L^C\)，得到
\[
 \sum_{\substack{H<d\le2H\\W<d\le B}}
 \sum_{(a,d)=1}R_{d,a}(\lambda)^2
 \ll_\phi(H^2+S)L^C\ll_\phi SL^C.
\tag{12}
\]
最后一步用(4)，不是假设每个频率都有小点值。
这是一条完整频率族上的正平方能量；不能给每个 \(q,d,a\)
另选任意 \(q\)-私有的素数权，或将最大interval替换成任意subset。
固定有限个 intervals的 union可再作有限次 Cauchy。

## 5. G的完整 approximant族能量

令 \(\mathcal A_H\) 为当前新子族中所有非空 \((q,d,a,m)\) packets。
第2节的 reduced fractions spacing为 \(1/(16H^2Q^2)\)。
先固定与 \(q\) 无关的两条 binary区间及共同 \(t_p,t_r\)，合并
\(C_k=\sum_{pr=k}b_pb_rp^{it_p}r^{it_r}\)。
真实素数乘积每个整数只有至多两个有序 factor pairs，故 \(\sum_k|C_k|^2\ll1\)；
产品长度 \(O(PR)\ll Q^2\)。
普通 additive大筛支付整个 \(\mathcal A_H\) 的平方能量 \(O(H^2Q^2)\)。
随后完整 binary展开恢复实际两腿 \(p,r<q\)，只添 \(L^C\)。
原 principal与所有残类包含在完整加性和中，不免费删除。因此
\[
 \sum_{\mathcal A_H}|G_{q,d,a,m}(\lambda)|^2
 \ll_\phi H^2Q^2L^C.
\tag{13}
\]
本式对(10)的共同参数一致。
它处理已经分离并完整支付 bounded residuals的 rational approximants，
不是对真正剩余 \(n/q^2\) 次弧免费引用某个改进平方模大筛。

## 6. F与G在同一个 q,d,a,m族相乘

保持 \(\sum_qb_q^2\ll1\)。
每个 \(q,d,a\) 的 \(m\) 种数 \(O(M)\)、\(M=X/S\)，所以(12)给
\[
 \sum_{\mathcal A_H}b_q^2R_{d,a}(\lambda)^2
 \ll_\phi M\sum_{d,a}R_{d,a}(\lambda)^2
 \ll_\phi XL^C.
\tag{14}
\]
同一个 \(R_{d,a}\) 支配全部实际 \(q\)-intervals；这正是不能先按
\(q\) 私下换系数、也不能先取整个 \(s\) 的 \(L^1\) 的原因。
由(13)、(14)，完整共同族 Cauchy得到
\[
 \sum_{\mathcal A_H}b_qR_{d,a}|G_{q,d,a,m}|
 \ll_\phi HQ\sqrt X\,L^C.
\tag{15}
\]
原前因子(7)为 \(O(S/(QX))\)，全部packet整数 \(n\) 用(5)付款。
原共同参数积分的正包络绝对积分为 \(L^C\)，由(15)对每组参数一致，
整个 \(H\) 子族的实际费用为
\[
 \frac S{QX}(Q/S+1)\,HQ\sqrt X\,L^C
 \ll_\phi\frac{H(Q+S)}{\sqrt X}L^C.
\tag{16}
\]
恢复全部 \(H\le B\)，\(\sum H\ll B\)，得到一个完整真实box费用
\[
 \ll_\phi\frac{B(Q+S)}{\sqrt X}L^C.
\tag{17}
\]
全部原 boxes、两个分子最大位置及两个共轭位置、原同 \(u\)
半比值前因子再恢复，\(Q\le X\)、\(S\ll Q\)，全新子族为
\[
 \boxed{|\mathfrak J^{\rm unmasked}_{W,B,>Z}|
       \ll_\phi B\sqrt X\,L^C.}
\tag{18}
\]
当前这条推导暂未排除 \(p=s,r=s\)，但保持 \(p,r<q\)；下一节精确恢复。

## 7. 精确 s排除修正适用于本次真正 n mask

原 \(p,r\ne s\) 用减两个单点、加双单点的精确容斥恢复。
新子族mask只依赖 \(q,n,S\)，与 individual \(s\) 无关，
所以可重新应用冻结464第6节的完整正能量付款，而非从 signed
全 minor 的一个总量推任意频率子集。

简要重推：\(p=s\) 时原相位为 \(e_{q^2}(n s(q-r))\)。
只对 \(\nu\) 作第3节的共同 Mellin分离，原 \(g(r/q)\)、同 \(u\)
profile直接保留为 bounded \(n\) 无关系数。
置 \(h=s(q-r)\in(0,q^2)\)。每个 \(h\le X^2\) 至多有三个不同
prime factors \(s>\sqrt X\)，每个 \(s\) 唯一确定 \(r\)。
原外 \(b_s\) 与单点原 \(b_s\) 合并，系数正能量 \(\sum_h|c_{q,h}|^2\ll1/S\)。
\(q^2\) 完整Parseval对任意 \(n\in J_q\) 子mask给
\(\sum_{q,n}|H_{q,n}|^2\ll Q^3/S\)。
另一正因子 \(\sum_qb_q^2|J_q|\ll QX/S\)，
原 \(S/(QX)\) 前因子遂给 \(Q/\sqrt X\)。
\(r=s\) 对称；\(p=r=s\) 的 map \(h=s(q-s)\) 至多二对一，能量更小。
全部原boxes和same-u恢复后，真正新子族的三项修正为
\(O_\phi(\sqrt X L^C)\)。
这个证明直接消费其准确 \(q,n,S\) mask，未按重叠packets复制 signed修正。
因此(18)严格升级为
\[
 \boxed{|\mathfrak J_{W,B,>Z}|\ll_\phi B\sqrt X\,L^C.}
\tag{19}
\]

## 8. 扩大的已付频率域与准确未付 complement

定义 \(\mathfrak K_{W,B,>Z}\) 为旧准确 \(qs>Z\) minor中再删除(2)
这个已经完整付过的新子族。逐原tuple和原频率mask精确有
\[
 \mathfrak I_{W,>Z}=\mathfrak J_{W,B,>Z}+\mathfrak K_{W,B,>Z}.
\tag{20}
\]
新剩余同时不存在旧 \(d\le W\)、半径 \(W/(dS)\) 的表示，
也不存在 \(W<d\le B\)、半径 \(1/S\) 的表示。
不能把后者改写成另一个 \(B/(dS)\) 主弧合同。

与487已有完整cap、旧主弧、全部原误差合并，
\[
 \mathfrak L_U=\mathfrak K_{W,B,>Z}
 +O_\phi((Z/X+1)L^C+(W^2+B)\sqrt X L^C).
\tag{21}
\]
旧低产品 \(WX^\epsilon\) 可固定小 \(\epsilon\) 后吸收入 \(\sqrt X L^C\)。
取 \(W=X^{1/10}\)、\(B=X^{1/5}\)、\(Z=X^{1193/700}\)，则
\[
 \boxed{\mathfrak L_U=\mathfrak K_{X^{1/10},X^{1/5},>X^{1193/700}}
 +O_\phi(X^{493/700}L^C)+O_\phi(X^{7/10}L^C).}
\tag{22}
\]
误差指数仍低于 \(5/7\)，但真实已付 rational分母族扩到 \(X^{1/5}\)，
而非此前 \(X^{1/10}\)。本次没有改掉旧冻结文件的参数域。

同一新 proof也允许 \(B=X^\kappa\)、\(1/10<\kappa<3/14\)：
当前高产品支撑仍保证 \(B^2\ll S\)、\(QS\gg BX\)、\(q>B\)，
且 \(B\sqrt X\) 的指数严格小于 \(5/7\)。
取 \(B=X^{1/5}\) 是保留现有误差 \(7/10\) 的一个便利具体值。

剩余仍在 \(qs>Z\)，保持全部原prime-product、aspect、profile、same-u与
准确正高度。其独立 \(G\) restricted-band能量和完整 \(F G\) signed预算
仍未付，当前完整四矩、零点比例与已有无零边界均保持。
本次没有有限采样、额外无零假设或外部pipeline。
新无限付款仍需 root全文独推和不同作者全文审查后准入。
