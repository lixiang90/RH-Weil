# 原 unit 主弧的产品残类压缩与扩大付款

2026-10-08，high_product_joint。基线 main
`e51a51e2225c9216b23cc7b12bc97e8fa8cf2ea1`。
只新增本研究源；不改旧冻结源、笔记、检查器、输出或 Git。

本稿把原真实主弧费用从 \(D^3\sqrt X\log^C X\) 改为
\(D^{5/2}\sqrt X\log^C X\)。关键是保留整个素数产品系数，
先按 \(q\bmod d\) 分组，而非把两条素数腿分别拆为 \(d^2\) 个残类。
这个压缩适用于原共同 \(u\)、真实最大素数、所有 sharp prefix 与
\(n\) 无关的 \((q,s)\) region。它扩大可以完整支付的有理频率族，
例如 \(D=X^{2/25}\) 的全主弧费用为 \(X^{7/10}\log^C X\)。

剩余高产品次弧仍未付清，没有新的 whole 四矩、常数级中心四阶预算、
简单零点比例或无零边界。本文不把一个有理频率块的付款当成整个主项付款。

## 1. 全文读取的冻结实际对象

SHA256 按 UTF-8、CRLF/lone CR 转 LF，不 trim、不改变末尾换行。
以下输入均已 FULL READ：

| 输入 | 行数／字节 | SHA256 |
| --- | --- | --- |
| [原 actual unit 源](hybrid-whole-fourth-unit-unit-actual-research-whole.md) | 425／16428 | b3f14cf4ee5659f8e23bd51dc9bf71e853e783bd2d55e42ee8846d6e8d1e41dc |
| [原共同主弧源](hybrid-original-unit-band-joint-cancellation-research-whole.md) | 378／14896 | 7c95bd2e700c16e0b0e836063f7545e8222a4de4b03d60c3271965252ec744b4 |
| [产品 cap 与点排除源](hybrid-original-unit-band-minor-lift-research-pc8.md) | 464／17560 | b6018e1254049b77dd5d7f73f4d3a7dc7272d5fe5dd3568f3c5ddf8cf73928b4 |
| [已准入笔记485](../../notes/485-original-minor-product-cap-and-point-repairs.md) | 171／6973 | 4fd6db48a93dcc5ff18840c3f663341096988f3c6b624ee761c90f85108f6eed |

仍取 \(X=T/(2\pi)\)、\(L=\log X\)、
\(b_p=\log p/(a_LL\sqrt p)\)、\(a_L\ge c_\phi>0\)。
所有 genuine primes 满足 \(\sqrt X<p\le X\)；\(q\) 为实际最大素数，
\(s<q\)、\(p,r<q\)。原两套 \(A_p,B_r\) 完全保持 actual 源(4)、(5)，
包括 \(p,r\ne s\) 与全部同一 \(u\) 的原 \(C^2\) profile。
另外两个最大标签位置交换两对后取共轭。

原 \(\nu\)、\(d_{\rm time}=\lfloor XL\rfloor\)、\(\theta_\pm\)、
\(\delta_{\rm near}=65536L^{5/2}/X\) 保持。
以下 \(d\) 总指 rational denominator，不是原时间 floor。
原 interior 是 \(qs>4X\)、\(q-s>4q\delta_{\rm near}\)。
原完整 \(q\mid n\) 加回、产品窗 \(g\)、chirp、graph 与 aliases
都沿冻结源的已付桥使用，不逐频率改写这些 signed 项。

固定真实 dyadic \(Q,S,P,R\)。始终有
\(Q,S,P,R\ge\sqrt X\)、\(P,R\ll Q\)、\(S\ll Q\)、
非零产品窗强制 \(PR\asymp QS\ll Q^2\)。
所有 sharp endpoints 仍由原求和保留。
令 \(1\le D\le X^{1/10}\)，先完整支付 \(QS\le64DX\) 的低产品 boxes。
在其余 boxes，major 的准确定义仍为
\[
 \left|\frac nq-m-\frac ad\right|\le\frac D{dS},
 \qquad 1\le d\le D,\quad 0\le a<d,\quad(a,d)=1.
\tag{1}
\]
包括 \(d=1,a=0\)。这里用 dyadic \(S\)，不改为 individual \(s\)。
重叠按固定顺序分配；后面的非负上界允许按全部 packets 正计数。

## 2. 固定 q 残类后只扭动整个产品系数

固定 \(d,a\)，写
\[
 c=dm+a,\qquad \beta=n-cq/d,\qquad
 |\beta|\le qD/(dS).
\tag{2}
\]
沿原正高度频带，\(n/q\le3X/S\) 对充分大 \(X\) 成立。
高产品 \(QS>64DX\) 保证
\(1\le c\le4dX/S<q/16\)。因此 \(q\nmid c\)。
又 \(d\le D\le X^{1/10}<q\)，\(q\) 为素数，故 \((q,d)=1\)。
这些 guards 使下面 CRT 逆元存在，并使模 \(q\) 频率非零。
每个 \(q,d,a\) 的实际 \(m\) 种数为 \(O(M)\)，\(M=X/S\ge1\)；
整个允许 \(m\) 范围长度小于 \(q\)，所以其模 \(q\) 映射是注入。
每个 packet 中实际整数 \(n\) 的种数满足
\[
 K_d\ll QD/(dS)+1.
\tag{3}
\]
保留这里的 \(+1\)，不假设 packet 中总有连续密集的整数频率。

精确相位为
\[
 e_{q^2}(-npr)
 =e_{dq}(-cpr)e(-\beta pr/q^2),
\]
\[
 e_{dq}(-cpr)
 =e_q(-c\bar d\,pr)e_d(-c\bar q\,pr).
\tag{4}
\]
对 \(d=1\)，最后因子按1解释。
因为 \(c\equiv a\pmod d\)，固定可逆剩余类
\(j=q\bmod d\) 后，最后因子恰为
\[
 e_d(-a\bar j\,pr).
\tag{5}
\]
它与 \(m\) 无关。第一因子的频率
\(b=c\bar d\equiv m+a\bar d\pmod q\) 非零，随实际 \(m\) 注入。
因此无需把 \(p,r\) 分成各 \(d\) 个残类。

对暂不排除 \(p=s,r=s\) 的两腿，原公共 Mellin/Fourier 分离后，
固定参数的基本权仍为
\(\alpha_p=b_pp^{it_1}\)、\(\beta_r=b_rr^{it_2}\)。
定义真实整数产品系数
\[
 C_k=\sum_{pr=k}\alpha_p\beta_r,
 \qquad C_k^{(j)}=C_k e_d(-a\bar j\,k).
\tag{6}
\]
腿保持原 prime dyadic supports；sharp \(p,r<q\) 在第4节付最大前缀。
因为两腿是 genuine primes，每个 \(k\) 最多有两个有序 factor pairs，
所以固定区间对和固定 twists 都满足
\[
 \sum_k|C_k^{(j)}|^2=\sum_k|C_k|^2
 \le2\sum_p|\alpha_p|^2\sum_r|\beta_r|^2\ll_\phi1.
\tag{7}
\]
产品长度 \(N\ll PR\ll Q^2\)。一般 composite Vaughan 系数不享有此两对因子界。

## 3. 有限 Parseval 不要求扭动后系数继续分离

先取一对与 \(q\) 无关的固定 binary 区间。
对两区间都包含于原严格两腿前缀的实际 \(q\equiv j\pmod d\)，
这些 \(p,r<q\) 都是模 \(q\) 单位。置
\[
 C_t^{[q]}=\sum_{k\equiv t\ (q)}C_k^{(j)},\qquad
 B_b=\sum_{t\in(\mathbb Z/q\mathbb Z)^*}C_t^{[q]}e_q(-bt),
 \qquad M_0=\sum_t C_t^{[q]}.
\]
有限群 Parseval 准确给
\[
 \sum_{b=1}^{q-1}
 \left|B_b+\frac{M_0}{q-1}\right|^2
 =\frac q{q-1}\sum_{\chi\ne\chi_0\ (q)}
 \left|\sum_k C_k^{(j)}\chi(k)\right|^2.
\tag{8}
\]
证明：把 \(C_t^{[q]}\) 减去群平均 \(M_0/(q-1)\) 后，
模 \(q\) 的零加性系数为0；全加性 Parseval 给 \(q\) 倍群方差，
再作 \(q-1\) 元乘法群 Parseval 即得(8)。
主角色对应每个非零加性频率上的 \(-M_0/(q-1)\)，符号保留。

式(8)对任意单位产品系数成立。\(C_k^{(j)}\) 的乘法变换
未必能写成两个角色和的积，本证明没有作那个无根据的因子化。
这里使用的是已经合成的真实整数产品系数。

本次核读的外部标准输入仍只有
[Kedlaya作者讲义，Theorem 18.2](https://kskedlaya.org/ant/chapter-18.html)：
固定长度 \(N\) 系数的 primitive multiplicative large sieve 费用为
\(Q^2+N-1\)，外带 \(q/\varphi(q)\) 权。
当前 \(q\) 为素数，故(8)的全部非主角色都是 primitive，
且 \(q/(q-1)=q/\varphi(q)\) 正是该权。

对固定 \(j\)，把 \(q\equiv j\pmod d\) 的非负角色能量放大到
全部 \(q\sim Q\) 后，大筛与(7)给 \(O_\phi(Q^2L^C)\)。
这里 coefficients \(C_k^{(j)}\) 对同一个 \(j\) 的全部 \(q\) 固定。
本节不直接把实际 \(q\)-相关前缀系数送入固定系数的大筛；
第4节再从完整固定区间族恢复所有实际前缀。
随后才合并至多 \(\varphi(d)\le d\) 个类，得到
\[
 \sum_j\sum_{\substack{q\sim Q\\q\equiv j\ (d)}}
 \sum_m|B_{b(q,m)}+M_0/(q-1)|^2
 \ll_\phi dQ^2L^C.
\tag{9}
\]
每个 \(m\) 只走一个注入的非零频率子族，有限 Parseval 的放大
只用于非负平方和。没有从 signed 主弧总量推任意子族范数。

主角色另付。对所有实际前缀、twists 和 \(j\)，
\(|M_0|\le\sum_p b_p\sum_r b_r\ll_\phi\sqrt{PR}\)。
每个 \(q\) 放大到全部非零 \(b\) 后其能量至多 \(O(PR/q)\)。
故整个 \(q\sim Q\) 主角色族费用 \(O(PRL^C)\ll O(Q^2L^C)\)，
不需另付 \(d\)，也没有删去它。
合并正平方和后，固定 \(d,a\) 的基本两腿能量因此为 \(O(dQ^2L^C)\)。

## 4. Sharp q 前缀、真实 s 排除与共同轮廓

\(q\)-相关两腿前缀不能直接当作固定大筛系数。
按原主弧源的 binary intervals 对每条前缀作精确展开：
每个前缀最多 \(O(L)\) 个不相交块，两条腿相乘后 Cauchy 付 \(O(L^2)\)。
对每个固定区间对、固定 \(j\)，其 \(C_k^{(j)}\) 对整个大筛族固定。
原 \(q\) 只选择自己合法的区间对；在非负角色能量中可放大到全部 \(q\)。
每个原素数坐标在每层仅出现一次，所以所有区间对的(7)能量之和
只再付 \(O(L^2)\)。这个做法保留原 strict \(p,r<q\)，
仍只有 \(dQ^2L^C\) 的全参数能量。
扩展大筛时若某个额外 \(q\) 整除某个 \(k\)，角色自动在该项取0；
(8)只用于原合法前缀，不要求额外前缀也满足单位条件。

原真实 \(p=s\)、\(r=s\) 和双单点修正没有删除。
直接在原 \(g\)、同 \(u\) bounded profiles 与原相位中取绝对值，
它们统一小于
\[
 C_\phi\bigl(\sqrt{R/S}+\sqrt{P/S}+1/S\bigr).
\tag{10}
\]
例如 \(p=s\) 给 \(b_s\sum_{r\sim R}b_r\ll\sqrt{R/S}\)；
若 \(s\) 不在该 \(P\) box，真实项是0。
每个 \(q\) 的 packet \(m\) 个数 \(O(X/S)\)，所以在完整 \(q,m\) 族中，
这个对所有 \(s,n\) 有效的 sup 修正具有平方能量
\[
 \ll Q(X/S)(R/S+P/S+S^{-2})\ll Q^2L^C,
\tag{11}
\]
因为 \(S^2\ge X\)、\(P,R\ll Q\)。
该付款没有把一个 signed 全族免费限制到 \(s\) 或 \(n\) 子集。
全次弧的更强点修正仍可沿冻结产品 cap 源第6节使用；
本节只证明主弧共同正包络所需的 sup 修正，不重复认领其平方根全局结论。

共同产品窗与 residual chirp 仍为
\[
 H_z(t)=g(e^t)e(-ze^t),\qquad
 z=\beta s/q,\qquad |z|\le2D/d.
\]
沿原主弧源(10)的二导数论证，有一个对全部 packet、\(q,s\) 统一的
非负 Mellin 包络 \(W_d(\tau)\)，满足
\[
 |\widehat H_z(\tau)|\le W_d(\tau),\qquad
 \int W_d(\tau)d\tau\ll1+D/d.
\tag{12}
\]
原 \(C^2\) profile 与 profile平方用同一个 \(O_\phi(L^C)\) Fourier
包络分离；\(u,q,s\) 的平移只乘单位相位，\(\phi\) 光滑性未升级。
固定参数后的基本两腿权为原 genuine-prime 权的 twists，
(7)、(9)不依赖 twists 的大小；共同积分用 Minkowski，常数可积。
(10)也可直接加入同一个非负包络，不需对 profile 再求导。

于是固定 \(d,a\)，对所有实际 \(s\) 与 packet \(n\) 有效的
非负 \(F_{q,m}^{(d,a)}(u)\) 满足
\[
 |\mathcal B_n^g(q,s,u)|\le F_{q,m}^{(d,a)}(u),\qquad
 \sum_{q\sim Q}\sum_m F_{q,m}^{(d,a)}(u)^2
 \ll_\phi d(1+D/d)^2Q^2L^C.
\tag{13}
\]
这取代旧主弧源(14)的 \((d+D)^2Q^2\)，省下一个 \(d\)。
不是逐 \(q\) 的未证素数分布，也不是任意参数各挑一组新系数。

## 5. 全外权与全部有理 packets 的费用

保持 \(\sum_{q\sim Q}b_q^2\ll1\)、\(\sum_{s\sim S}b_s\ll\sqrt S\)，
原 \((2\pi s/q)\nu(2\pi sn/q)\ll S/(QX)\)。
对固定 \(d,a\)，完整 \(q,m\) Cauchy 与(13)给
\[
 \sum_q b_q\sum_m F_{q,m}^{(d,a)}(u)
 \ll_\phi \sqrt d(1+D/d)Q\sqrt{X/S}\,L^C.
\tag{14}
\]
逐 packet 中的全部真实 \(n\) 用(3)付款，全部 \(s\) 用其原正质量付款，
固定 \(d,a\) 的完整 box 费用为
\[
 \ll_\phi\frac{d+D}{\sqrt d}
 \left(\frac{QD}{d\sqrt X}+\frac S{\sqrt X}\right)L^C.
\tag{15}
\]
\(K_d\) 的 \(+1\) 正是第二项，没有在 \(S\asymp Q\) 时删除。

每个 \(d\) 的 \(a\) 数量至多 \(d\)。由
\(\sum_{d\le D}\sqrt d\ll D^{3/2}\)、
\(\sum_{d\le D}d^{-1/2}\ll D^{1/2}\)、
\(\sum_{d\le D}d^{3/2}\ll D^{5/2}\)，全部 \(d,a\) 给
\[
 |\mathfrak L_{F,\mathrm{major}}^g(Q,S,P,R)|
 \ll_\phi\frac{D^{5/2}(Q+S)}{\sqrt X}L^C.
\tag{16}
\]
恢复所有 boxes、原同 \(u\) 的半比值前因子、两种分子最大位置及
另外两种共轭位置，\(Q\le X\)、\(S\ll Q\)，得到
\[
 \boxed{|\mathfrak L_{F,\mathrm{major}}^g|
   \ll_\phi D^{5/2}\sqrt X\,L^C.}
\tag{17}
\]
这里可支付完整原真实 rational union，保留真实 \(q\)-最大性、全部
\(p/r\)、\(q/s\) aspects、原 sharp endpoints、同一 \(u\) 和正高度频带。

## 6. n 无关 region 与扩大后的准确剩余

对任意 \(n\) 无关的 \((q,s)\) region \(\mathcal R\)，在(14)前保留
\(q\) 的真实子族，并对 \(s\in\mathcal R(q)\) 取原正绝对质量，
它不超过完整 \(\sum_{s\sim S}b_s\)。因此同一个(13)的非负包络
重新证明该 region 的(17)，不从 signed 全域结果推出它。
特别可取实际 \(qs\le Z\)，也允许它横切 dyadic boxes。

冻结产品 cap 源的完整 \(n\) 费用 \((Z/X+1)L^C\) 没有改动。
完整 \(n\) cap 减去已重新付过的 region major 后，得到新的实际付款
\[
 \boxed{|\mathfrak I_D(qs\le Z)|\ll_\phi
 (Z/X+1)L^C+D^{5/2}\sqrt X\,L^C.}
\tag{18}
\]
原低产品费用 \(DX^\epsilon L^C\)、nn/chirp/graph/边界等沿冻结源
保留。所以原 unit 主项的完整缩约变成
\[
 \mathfrak L_U=\mathfrak I_{D,>Z}
 +O_\phi((Z/X+1)L^C+D^{5/2}\sqrt X\,L^C)
 +O_{\phi,\epsilon}(DX^\epsilon L^C).
\tag{19}
\]
所有原点排除修正的全 minor 平方根付款仍成立；minor 定义只依赖
\(q,n,S\)，其任意准确 complement 都可在原正平方和中放大。

取 \(Z=X^{12/7-\eta}\)、\(0<\eta<3/14\)，允许
\[
 D=X^\delta,\qquad 0<\delta<3/35.
\tag{20}
\]
这是 \(1/2+(5/2)\delta<5/7\) 的严格范围，且 \(3/35<1/10\)
满足原 guards。可固定充分小 \(\epsilon\)，使 \(\delta+\epsilon<1/2\)。
于是(19)的两项主要指数为 \(5/7-\eta\) 与 \(1/2+(5/2)\delta\)。

例如 \(\eta=1/100\)、\(\delta=2/25\)，得到
\[
 \mathfrak L_U=\mathfrak I_{X^{2/25},>X^{1193/700}}
 +O_\phi(X^{493/700}L^C)+O_\phi(X^{7/10}L^C).
\tag{21}
\]
旧 \(D^3\) 付款在这个 \(D\) 的指数为 \(37/50>5/7\)，
因此这个参数点此前不能由旧主弧付款直接消费。
现在整个扩大后的主弧确实已付，minor 为其准确 complement；
没有将某个频率子族的任意移除冒称已付。
与较小 \(D\) 相比，major 定义随 \(D\) 单调扩大，低产品族也完整扩大。
在 \(qs>Z\) 的最终剩余中，因 \(Z\gg DX\)，所有原相关 boxes
对充分大 \(X\) 都处于新的高产品区，所以剩余准确是扩大后 major 的
高产品 complement，不含未经付款的低产品任意频率子集。

剩余真实支撑仍有 \(q>X^{6/7-\eta/2}\)、\(s>X^{5/7-\eta}\)、
\(q/s<X^{2/7+\eta}\)，以及产品窗强制的原 \(p,r\) 支撑。
本次把已付频率域扩大，不声称改变剩余域的这些几何指数。
当前尚未证明其 \(F\cdot G\) signed union 小于 \(5/7\)，
也没有准入 \(Q^2(X/S)\) 的实际 restricted-band \(G\) 能量。
上述数学付款不需要新的 \(\zeta\) 或 Dirichlet \(L\) 无零假设；
它只是让原路线可继续使用的准确主弧参数范围增大。

未以有限采样认证上述无限界，也未使用新的外部 pipeline。
新源仍需 root 全文独推和不同作者全文审查后准入。
