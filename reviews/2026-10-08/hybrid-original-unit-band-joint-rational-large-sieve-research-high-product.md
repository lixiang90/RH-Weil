# 原 unit 主弧：全部有理频率的联合加性大筛付款

2026-10-08，high_product_joint。基线 main
`e51a51e2225c9216b23cc7b12bc97e8fa8cf2ea1`。
只新增本研究源，不改任何旧冻结源、笔记、检查器、输出或 Git。

本稿进一步把原完整主弧费用降为
\[
 \boxed{|\mathfrak L_{F,\mathrm{major}}^g|
       \ll_\phi D^2\sqrt X\,\log^C X.}
\]
它覆盖原参数域 \(1\le D\le X^{1/10}\)，保持真实最大素数、
全部原 prime 权、sharp 前缀、共同空间变量与原正高度载体。
关键是把一个 dyadic 分母族的全部 \((q,d,a,m)\) 有理频率一次送入
普通 additive 大筛，然后在同一个完整族上作外权 Cauchy。

因此原上限 \(D=X^{1/10}\) 已可完整支付到 \(X^{7/10}\log^C X\)。
原高产品次弧仍未付清，没有新的 whole 四矩、中心四阶常数预算、
零点比例或无零边界。本文不扩大冻结源给定的 \(D\le X^{1/10}\) 域。

## 1. 冻结输入与原实际 major

SHA256 按 UTF-8、CRLF/lone CR 转 LF，不 trim、不改变末尾换行。
以下原实际输入已 FULL READ；中间稿的唯一前缀量词澄清也已精确回读：

| 输入 | 行数／字节 | SHA256 |
| --- | --- | --- |
| [原 actual unit 源](hybrid-whole-fourth-unit-unit-actual-research-whole.md) | 425／16428 | b3f14cf4ee5659f8e23bd51dc9bf71e853e783bd2d55e42ee8846d6e8d1e41dc |
| [原共同主弧源](hybrid-original-unit-band-joint-cancellation-research-whole.md) | 378／14896 | 7c95bd2e700c16e0b0e836063f7545e8222a4de4b03d60c3271965252ec744b4 |
| [原产品 cap 与点排除源](hybrid-original-unit-band-minor-lift-research-pc8.md) | 464／17560 | b6018e1254049b77dd5d7f73f4d3a7dc7272d5fe5dd3568f3c5ddf8cf73928b4 |
| [已准入笔记485](../../notes/485-original-minor-product-cap-and-point-repairs.md) | 171／6973 | 4fd6db48a93dcc5ff18840c3f663341096988f3c6b624ee761c90f85108f6eed |
| [本次残类压缩中间稿](hybrid-original-unit-band-major-residue-compression-research-high-product.md) | 334／14509 | 4b85fb921d5767eeb3856a58a93b1e83af34a453be119c2a205e23744513e2f1 |

下文不消费中间稿的 \(D^{5/2}\) 主弧结论；它用直接加性大筛重新证明
更强付款。中间稿保留为另一条 CRT 和固定系数量词的独立推导。

仍取 \(X=T/(2\pi)\)、\(L=\log X\)、
\(b_p=\log p/(a_LL\sqrt p)\)、\(a_L\ge c_\phi>0\)。
所有 genuine primes 满足 \(\sqrt X<p\le X\)。\(q\) 为实际最大素数，
\(s<q\)、\(p,r<q\)，真实 \(p,r\ne s\) 在第5节准确保留。
两套原 \(A_p,B_r\) 完全沿 actual 源(4)、(5)，包括全部原 \(C^2\)
profile 与同一 \(u\)。另外两个最大位置交换两对后取共轭。

原 \(\nu\)、时间 floor、\(\theta_\pm\)、\(\delta_{\rm near}\)、
原 interior \(qs>4X\)、\(q-s>4q\delta_{\rm near}\) 均保持。
以下 \(d\) 是 rational denominator，\(H\) 是它的 dyadic scale。
原完整 \(q\mid n\) 加回、完整 \(n\) 中插入产品窗 \(g\)、chirp、
graph、整数 aliases 继续沿原已付桥消费；不逐频率改写那些 signed 项。

固定原真实 dyadic \(Q,S,P,R\)，有
\(Q,S,P,R\ge\sqrt X\)、\(P,R\ll Q\)、\(S\ll Q\)，
产品窗 \(g(pr/(qs))\ne0\) 强制 \(PR\asymp QS\ll Q^2\)。
所有 sharp endpoints 保留。取 \(1\le D\le X^{1/10}\)，
先完整支付 \(QS\le64DX\) 的低产品 boxes。
其余 boxes 的 major 精确定义仍为
\[
 \left|\frac nq-m-\frac ad\right|\le\frac D{dS},
 \quad 1\le d\le D,\quad0\le a<d,\quad(a,d)=1.
\tag{1}
\]
包括 \(d=1,a=0\)。这里使用 dyadic \(S\)，不使用 individual \(s\)。
重叠可以按固定顺序分配；全部 packets 的正包络允许重复上界。

## 2. 真正不同的 reduced rational frequencies

写
\[
 c=dm+a,\qquad \beta=n-cq/d,\qquad
 |\beta|\le qD/(dS),\qquad
 \alpha_{q,d,a,m}=\frac{c}{dq}.
\tag{2}
\]
只列出原实际频带中非空的 packets；即至少有一个真实 \(s,n\)
满足原 supports 和(1)。沿原正高度频带，\(n/q\le3X/S\)，
且 \(n/q\ge X/(2S)\)。充分大 \(X\) 时 \(D/S=o(1)\)，
因此非空 packet 的 \(c\) 是正整数，并满足
\[
 1\le c\le4dX/S<q/16.
\tag{3}
\]
最后一步用 \(QS>64DX\)、\(d\le D\)、\(q>Q\)。
又 \(q>\sqrt X>D\ge d\)，\(q\) 为素数，故 \((q,d)=1\)；
由 \(c\equiv a\pmod d\) 与 \((a,d)=1\)，有 \((c,d)=1\)。
(3)给 \(q\nmid c\)。所以 \(c/(dq)\) 已经约分，并且
\[
 0<\alpha_{q,d,a,m}<1/(16d)\le1/16.
\tag{4}
\]
\(d=1,a=0\) 时 \((a,d)=1\) 按通常约定成立，\(c=m\)，结论不变。

**相同有理数只能来自同一个 packet。**
约分后分母是 \(dq\)。它唯一确定那个大于 \(D\) 的素因子 \(q\)：
其他因子都包含于 \(d\le D\)。因此相同分母强制相同 \(q,d\)。
相同约分分子再强制相同 \(c\)；欧几里得除法 \(c=dm+a\)、
\(0\le a<d\) 唯一恢复 \(m,a\)。不同 \((q,d,a,m)\) 因而给不同频率。
这消除了把重复频率免费当成 separated set 的风险。

单列 \(d=1\)；其余分成 \(H<d\le2H\) 的完整 dyadic 族，
最后一个族在 \(D\) 处截断。令 \(\mathcal A_H\) 为该族的所有真实非空
\((q,d,a,m)\) packets。对它们，约分分母至多 \(4HQ\)。
不同有理数的差值分子是非零整数，故
\[
 \|\alpha_{q,d,a,m}-\alpha_{q',d',a',m'}\|
 \ge\frac1{16H^2Q^2}.
\tag{5}
\]
这里 \(\|\cdot\|\) 是到整数的距离。(4)保证两数之差小于 \(1/16\)，
不会经由整数1绕回产生更小距离。
\(d=1\) 的单列族用 \(H=1\) 和相同较弱常数即可。

## 3. 全部 q,d,a,m 的固定产品系数能量

本次已打开核读的唯一外部标准输入为
[Kedlaya作者讲义，Theorem 17.5](https://kskedlaya.org/ant/chapter-17.html)：
模1距离至少 \(\rho\) 的有限频率族，对固定长度 \(N\) 的系数，
其 additive 大筛平方和费用至多 \(\rho^{-1}+N\)。
这里只使用这个稍弱版本，不需要最优的 \(-1\)。

先取两条与 \(q\) 无关的固定 binary 区间及固定共同 twists，定义
\[
 C_k=\sum_{pr=k}b_pb_rp^{it_1}r^{it_2}.
\tag{6}
\]
腿保留原 genuine-prime dyadic supports 与这两个固定区间。
产品长度 \(N\ll PR\ll Q^2\)；每个 \(k\) 至多有两个有序素数 factor pairs，
故
\[
 \sum_k|C_k|^2\le2\sum_p b_p^2\sum_r b_r^2\ll_\phi1.
\tag{7}
\]
固定系数满足(5)，直接 additive 大筛给
\[
 \sum_{(q,d,a,m)\in\mathcal A_H}
 \left|\sum_k C_ke(-\alpha_{q,d,a,m}k)\right|^2
 \ll_\phi H^2Q^2\sum_k|C_k|^2.
\tag{8}
\]
无需展开成模 \(q\) 或模 \(dq\) 的乘法角色；
原 principal contribution、所有 mod \(d\) 残类已包含在这个完整加性和中。
它也不要求扭动后的产品系数继续分成两条角色和。

原真实两腿前缀 \(p,r<q\) 依赖 \(q\)，不能直接把它们送入(8)。
每条前缀用最多 \(O(L)\) 个 binary intervals 精确展开，
两腿乘积后的 Cauchy 付 \(O(L^2)\)。
对每个固定区间对，实际 \(q\) 仅选择其中合法的区间，
在非负平方和中可放大到完整 \(\mathcal A_H\)，再使用(8)。
所有层上，每个 prime 坐标各出现 \(O(L)\) 次，因此所有区间对的(7)
能量之和仅再付 \(O(L^2)\)。恢复所有 strict \(q\)-prefix 后仍有
\[
 \sum_{\mathcal A_H}
 \left|\sum_{\substack{p,r\ \mathrm{actual}\\p,r<q}}
 b_pb_rp^{it_1}r^{it_2}e(-\alpha_{q,d,a,m}pr)\right|^2
 \ll_\phi H^2Q^2L^C.
\tag{9}
\]
大筛的额外区间若包含 \(p=q\) 等数也不成问题：
加性大筛对任意整数系数成立，不需要额外区间的单位条件。
真实前缀依然严格保留，不把原最大素数假设改掉。

## 4. 完整 chirp 和原 profile 的共同可积包络

原相位精确为
\[
 e_{q^2}(-npr)
 =e(-\alpha_{q,d,a,m}pr)e(-\beta pr/q^2).
\tag{10}
\]
保留产品窗后，剩余 chirp 与窗合成
\[
 H_z(t)=g(e^t)e(-ze^t),\qquad
 z=\beta s/q,\qquad |z|\le2D/d\le2D/H.
\tag{11}
\]
沿原共同主弧源(10)的固定紧支撑与二导数证明，一个同时控制整个
\(\mathcal A_H\)、全部真实 \(s,n\) 的非负包络可取
\[
 |\widehat H_z(\tau)|\le
 C\min\{1,(1+2D/H)^2/(1+|\tau|)^2\}=:W_H(\tau),
 \qquad\int W_H(\tau)d\tau\ll1+D/H.
\tag{12}
\]
Mellin 分离只把 \(p^{i\tau}r^{i\tau}\) 放进(6)，
\((qs)^{-i\tau}\) 是模长1的外因子。
每个不同 packet 的 \(\widehat H_z\) 可以不同，但其模长都被同一个
\(W_H\) 控制；没有对各频率私下选一组新的固定大筛系数。

原两套 \(C^2\) profile、profile平方，用原同一 \(O_\phi(L^C)\)
Fourier包络分离。\(u,q,s\) 平移只乘单位相位。
没有把 \(\phi\) 改成更光滑的函数，没有分裂空间变量。
固定公共参数时(9)的常数与 twists 大小无关，
共同参数积分用 Minkowski 与(12)，得到真正可积的统一正包络。

## 5. 原全部 s 单点排除及整个 H 族的正包络

真实 \(p,r\ne s\) 用精确容斥保留。
在原同 \(u\) profile、\(g\le1\) 和原相位中直接取绝对值，
两个单点与双单点对全部 \(s,n\) 的统一上界为
\[
 C_\phi\bigl(\sqrt{R/S}+\sqrt{P/S}+S^{-1}\bigr).
\tag{13}
\]
例如 \(p=s\) 的原系数是 \(b_s\sum_{r\sim R}b_r\)，
若 \(s\) 不在 \(P\) 的实际 support，该项本来是0。
这只是主弧共同包络所需的 sup 修正；
全次弧的平方根点修正仍沿冻结产品 cap 源第6节，不重新认领。

整个 \(H\) 族有 \(O(H^2)\) 对 \((d,a)\)，
每个 \(q,d,a\) 有 \(O(M)\) 个 \(m\)，\(M=X/S\ge1\)。
故(13)在全部 \(\mathcal A_H\) 上的平方能量为
\[
 \ll H^2 Q(X/S)(R/S+P/S+S^{-2})\ll_\phi H^2Q^2L^C,
\tag{14}
\]
因为 \(S^2\ge X\)、\(P,R\ll Q\)。
这个 sup bound 不需要把 signed 全族范数推成任意 \(s\) 或 \(n\) 子集范数。

把(9)、原 profile包络、(12)、(14)合并，得到非负
\(F_{q,d,a,m}(u)\)，对每个实际 packet 的全部真实 \(s,n\) 满足
\[
 |\mathcal B_n^g(q,s,u)|\le F_{q,d,a,m}(u),
 \qquad
 \sum_{\mathcal A_H}F_{q,d,a,m}(u)^2
 \ll_\phi(H+D)^2Q^2L^C.
\tag{15}
\]
这是整个 \((q,d,a,m)\) 族的一次付款。
若此时先对每个 \(d,a\) 取 absolute 再求和，会重新丢掉本稿的节省。
\(d=1\) 的单列族由同一论证取 \(H=1\)，没有主角色或零频率删除。

## 6. 全部外权也在同一个 H 族作 Cauchy

原正密度满足 \(\|\nu\|_\infty\ll X^{-1}\)，
原频带内外前因子为
\((2\pi s/q)\nu(2\pi sn/q)\ll S/(QX)\)。
仍保留 \(\sum_{q\sim Q}b_q^2\ll1\)、\(\sum_{s\sim S}b_s\ll\sqrt S\)。
每个 \(H<d\le2H\) 的 packet 中实际整数 \(n\) 个数至多
\[
 K_H\ll QD/(HS)+1.
\tag{16}
\]
原 \(\nu\) support 和所有 sharp \(s,n\) endpoints 没有改变；
(16)只用于实际 packet 的 absolute 上界，\(+1\) 保留。

全部 \(\mathcal A_H\) 上的另一 Cauchy 因子是
\[
 \sum_{\mathcal A_H}b_q^2
 \ll H^2(X/S)\sum_qb_q^2\ll_\phi H^2X/S.
\tag{17}
\]
这里用的是每个 \(q\) 的 \(O(H^2X/S)\) 个真实 packet 计数。
它不假设全部这些 packet 都非空；准确非空子族只会减少该正计数。
于是(15)、(17)给
\[
 \sum_{\mathcal A_H}b_q F_{q,d,a,m}(u)
 \ll_\phi H(H+D)Q\sqrt{X/S}\,L^C.
\tag{18}
\]
将全部真实 \(n\) 用(16)、全部真实 \(s\) 用原正质量、原 \(\nu\)
用点态上界支付，整个 \(H\) 族的 box费用为
\[
 \sqrt S\frac S{QX}K_H\,
 H(H+D)Q\sqrt{X/S}\,L^C
 \ll_\phi\frac{(H+D)(QD+HS)}{\sqrt X}L^C.
\tag{19}
\]
因为 \(H\le D\)，(19)至多 \(D^2(Q+S)L^C/\sqrt X\)。
按全部 dyadic \(H\) 族和 \(d=1\) 求和，只再损失 \(O(\log(2D))\)，
可被 \(L^C\) 吸收。得到
\[
 |\mathfrak L_{F,\mathrm{major}}^g(Q,S,P,R)|
 \ll_\phi\frac{D^2(Q+S)}{\sqrt X}L^C.
\tag{20}
\]
恢复所有原 boxes、半比值同 \(u\) 前因子、两种分子最大位置与另外
两种共轭位置，\(Q\le X\)、\(S\ll Q\)，因此
\[
 \boxed{|\mathfrak L_{F,\mathrm{major}}^g|
       \ll_\phi D^2\sqrt X\,L^C.}
\tag{21}
\]
这个付款覆盖完整原 rational union，既没有丢掉 \(K_H\) 的 \(+1\)，
也没有用一个固定 \(q\) 的矩形范数代替真实全部 \(q\) 族。

## 7. 原 n 无关产品 region 与准确剩余

对任意 \(n\) 无关的 \((q,s)\) region \(\mathcal R\)，
先在(18)保留真实 \(q\) 子族，在恢复 \(s\) 时用
\(\sum_{s\in\mathcal R(q)}b_s\le\sum_{s\sim S}b_s\)。
同一个(15)的共同非负包络重新证明该 region 的(21)。
这是原系数上的重推，不是由 signed 全域上界删掉一个 region。
可取实际 \(qs\le Z\)，允许它横切 dyadic boxes，无产品阈值固定倍数泄漏。

冻结 cap 源的完整 \(n\) 产品费用 \((Z/X+1)L^C\) 保持。
完整 cap 减去已按正包络重新支付的 region major，得到
\[
 \boxed{|\mathfrak I_D(qs\le Z)|\ll_\phi
       (Z/X+1)L^C+D^2\sqrt X\,L^C.}
\tag{22}
\]
随后与原 \(q\mid n\) 加回、低产品完整族、chirp、graph 和边界付款
合并，原 unit主项准确缩约为
\[
 \mathfrak L_U=\mathfrak I_{D,>Z}
 +O_\phi((Z/X+1)L^C+D^2\sqrt X\,L^C)
 +O_{\phi,\epsilon}(DX^\epsilon L^C).
\tag{23}
\]
原全部 \(s\) 排除修正的全 minor 平方根付款仍保持；
major定义只依赖 \(q,n,S\)，任何准确 complement 都可沿那个正平方和付款。

在原参数域取 \(Z=X^{12/7-\eta}\)、\(0<\eta<3/14\)，
\(D=X^\delta\)、\(0<\delta\le1/10\)。
则两项主要费用指数为 \(5/7-\eta\) 和 \(1/2+2\delta\le7/10<5/7\)。
可固定 \(\epsilon\) 使 \(\delta+\epsilon<1/2\)，吸收全部旧低产品费用。
例如 \(\eta=1/100\)、\(D=X^{1/10}\)，得到
\[
 \boxed{\mathfrak L_U
 =\mathfrak I_{X^{1/10},>X^{1193/700}}
 +O_\phi(X^{493/700}L^C)+O_\phi(X^{7/10}L^C).}
\tag{24}
\]
旧 \(D^3\) 费用在这个 \(D\) 为 \(X^{4/5}\)，中间 \(D^{5/2}\)
费用为 \(X^{3/4}\)，都不能直接消费为低于 \(5/7\) 的误差。
本稿使原完整 \(D\le X^{1/10}\) 有理族均可支付。

major随 \(D\) 单调扩大。最终 \(qs>Z\) 的所有相关 boxes，对充分大
\(X\) 都因 \(Z\gg DX\) 处于新的高产品区；准确剩余是扩大的 major
在该原 region 内的真正 complement，没有漏掉未经完整支付的低产品子集。
剩余几何支撑仍为 \(q>X^{6/7-\eta/2}\)、\(s>X^{5/7-\eta}\)、
\(q/s<X^{2/7+\eta}\)，产品窗和原 \(p,r<q\) 的真实限制不变。

仍未证明这个剩余 \(F\cdot G\) signed union 小于 \(5/7\)，
也未准入实际 \(G\) 的 \(Q^2(X/S)\) restricted-band能量。
本次纯解析付款不增加新的 \(\zeta\) 或 Dirichlet \(L\) 无零假设，
也没有将一般平方模大筛的 \(Q^3\) 费用误读成 \(Q^2\)。
这里的加性大筛只处理已准确建立并带共同 residual chirp 包络的
rational approximant族，真正 minor的原 \(n/q^2\) 频率不在(8)中。

本稿没有 finite采样或外部 pipeline。上述无限界仍需 root 全文独推和
不同作者全文审查后准入。当前比例、已有无零边界与完整四矩基线均保持。
