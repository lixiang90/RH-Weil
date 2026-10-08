# 原 unit 主弧联合有理频率大筛：不同作者全文审查

2026-10-08，perron_reviewer。不同作者独立 FULL READ 与数学重推。
只新增本审查；没有修改作者源、冻结依赖、输出、检查器或 Git。

**限定 PASS。** 最终 340 行源的完整原主弧费用
\(D^2\sqrt X\log^C X\) 在原 \(1\le D\le X^{1/10}\) 域内成立。
它的任意 \(n\) 无关 \((q,s)\) region 版本、产品 cap 的真实 minor
缩约及最后的指数实例均可按文中证明消费。334 行中间源的
\(D^{5/2}\sqrt X\log^C X\) 也作为较弱中间付款通过。
[root 汇总笔记487](../../notes/487-original-joint-rational-major-payment.md)
经独立全文核对，也在同一限定范围内通过。

没有准入完整高产品 minor 的 signed 界、原目标的 restricted-band
能量、canonical whole 四矩、中心四阶常数预算、零点比例或无零边界。
新源的直接证明不依赖中间源的 \(D^{5/2}\) 结论。

## 1. 冻结版本与全文读取范围

哈希按 UTF-8 字节、CRLF/lone CR 转 LF；不 trim，保留原末尾换行。
下表全部源及笔记均 FULL READ；结论不由摘要、旧 peer 或有限枚举代替。

| 输入 | 行数／LF 字节 | SHA256 |
| --- | --- | --- |
| [本次最终联合有理频率源](hybrid-original-unit-band-joint-rational-large-sieve-research-high-product.md) | 340／14702 | 92989568fd5ffbe25a8f6f47997c9ced10acd96b8d3732c740d2cb8a7563ee7e |
| [原 actual unit 源](hybrid-whole-fourth-unit-unit-actual-research-whole.md) | 425／16428 | b3f14cf4ee5659f8e23bd51dc9bf71e853e783bd2d55e42ee8846d6e8d1e41dc |
| [原共同 major 源](hybrid-original-unit-band-joint-cancellation-research-whole.md) | 378／14896 | 7c95bd2e700c16e0b0e836063f7545e8222a4de4b03d60c3271965252ec744b4 |
| [完整产品 cap 与点排除源](hybrid-original-unit-band-minor-lift-research-pc8.md) | 464／17560 | b6018e1254049b77dd5d7f73f4d3a7dc7272d5fe5dd3568f3c5ddf8cf73928b4 |
| [已准入笔记485](../../notes/485-original-minor-product-cap-and-point-repairs.md) | 171／6973 | 4fd6db48a93dcc5ff18840c3f663341096988f3c6b624ee761c90f85108f6eed |
| [残类压缩中间源](hybrid-original-unit-band-major-residue-compression-research-high-product.md) | 334／14509 | 4b85fb921d5767eeb3856a58a93b1e83af34a453be119c2a205e23744513e2f1 |
| [root 汇总笔记487](../../notes/487-original-joint-rational-major-payment.md) | 113／5156 | 1768ac94f1d72b1934fa6b8c7290e78717bd2082214e562fde5586c2d788de7d |

此外直接打开核读 [Kedlaya 作者讲义 Theorem 17.5 及其证明](https://kskedlaya.org/ant/chapter-17.html)。
它对模1分离的有限频率族和一个固定整数区间的任意复系数适用；
作者源使用的较弱费用 \(\rho^{-1}+N\) 与该处实际证明一致。
没有将平方模大筛的 \(Q^3\) 费用更名为 \(Q^2\)，也不需要素数 AP 分布。

## 2. 原对象与 packets 的确切范围

实际观察对象仍为原正高度 \(\nu\) 载体的 unit 主频带。
\(q\) 是真实最大素数，\(s<q\)、\(p,r<q\)，原两套 actual
profile(4)、(5)、共同 \(u\) 及 \(p,r\ne s\) 均保留。
另外两个最大位置由交换两对后取共轭恢复。

完整 \(q\mid n\) 加回和完整 \(n\) 中插入 \(g\) 在旧源各有付款；
新源没有把这两个 signed 操作逐个 minor/major 频率使用。
低产品 \(QS\le64DX\) 先作为完整 boxes 支付。
高产品族保持 \(Q,S,P,R\ge\sqrt X\)、\(P,R\ll Q\)、\(S\ll Q\)
与 \(PR\asymp QS\ll Q^2\)；这是产品系数真正的大筛长度。

major 使用固定 dyadic \(S\)：
\[
 |n/q-m-a/d|\le D/(dS),\quad d\le D,\quad(a,d)=1,
 \quad0\le a<d.
\]
它不随 individual \(s\) 改变。重叠按固定顺序分配是合法的；
此后所有 packets 可以在正包络中重复计数。
只为至少有一个原实际 \((s,n)\) 的 packet 建立频率集合，不假定
一个外包围 packet 必然非空。

## 3. reduced 频率、唯一性与圆周间距

从原 \(\theta_\pm\) 支撑独立得到
\(X/(2S)\le n/q\le3X/S\)，充分大 \(X\) 时均成立。
令 \(c=dm+a\)、\(\beta=n-cq/d\)。误差最多 \(D/(dS)\)，
故 \(c>0\)，且
\[
 c\le 3dX/S+D/S\le4dX/S<q/16.
\]
末项使用 \(QS>64DX\)、\(d\le D\)、\(q>Q\)。
\(q>D\) 为素数，\((c,d)=(a,d)=1\)，且 \(q\nmid c\)，
因此 \(c/(dq)\) 完全约分，包括通常约定下的 \(d=1,a=0\)。

若两个频率相等，约分分母相等。分母 \(dq\) 唯一的大于 \(D\)
的素因子就是 \(q\)，因为全部其他因子来自 \(d\le D\)。
于是 \(q,d,c\) 相同，再由欧几里得除法唯一恢复 \(m,a\)。
这里的全 \((q,d,a,m)\) 集合确实没有频率重数。

对 \(H<d\le2H\)、\(Q<q\le2Q\)，约分分母至多 \(4HQ\)。
两个不同分数差的分子为非零整数，实数间距至少
\((16H^2Q^2)^{-1}\)。又所有频率都在 \((0,1/16)\)，
所以同一界控制模1距离，不存在整数1附近绕回的更短距离。
\(d=1\) 单列族取 \(H=1\) 与相同较弱常数。

这些论证是全参数证明；不依赖有限频率样本。

## 4. 固定产品系数与动态前缀

先固定两个与 \(q\) 无关的 binary 区间和共同 twists。
真实整数产品系数
\(C_k=\sum_{pr=k}b_pb_rp^{it_1}r^{it_2}\)
支撑于长度 \(O(PR)=O(Q^2)\) 的整数区间。
每个 \(k\) 至多有两个有序 genuine-prime factor pairs，故
\[
 \sum_k|C_k|^2\le2\sum_p b_p^2\sum_r b_r^2\ll_\phi1.
\]
同一个系数序列送入全部分离频率，直接大筛能量为
\(O_\phi(H^2Q^2)\)。twists 模长1，常数与参数大小无关。
产品系数不必是两条乘法角色和的积。
原 principal 或 mod \(d\) 残类从未被删去，已包含于该加性和。

恢复严格 \(p,r<q\) 时，每条前缀精确分成 \(O(L)\) 个 binary 块。
前缀的两块乘积后 Cauchy 支付 \(O(L^2)\)。
对每个固定区间对，只在正平方和中将选择该区间的合法 \(q\)
扩到完整频率族，再用固定系数大筛。
所有区间对的能量和至多增加 \(O(L^2)\)，因为每个 prime
坐标在每层至多出现一次。
额外区间含 \(p=q\) 等数时，加性大筛仍适用任意整数系数；
这没有把真实前缀改成非严格前缀。

## 5. 同一 profile、完整 chirp 与所有点修正

精确相位分解为
\[
 e_{q^2}(-npr)=e(-cpr/(dq))e(-\beta pr/q^2).
\]
置 \(t=\log(pr/(qs))\)、\(z=\beta s/q\)，有
\(|z|\le2D/d\le2D/H\)。产品窗和 residual chirp 正好是
\(g(e^t)e(-ze^t)\)。固定紧支撑上其 \(L^1\) 范数为常数，
二阶导数范数为 \(O((1+D/H)^2)\)，所以共同非负 Fourier
包络的积分为 \(O(1+D/H)\)。这是完整 chirp 付款，不是截断展开。

原 actual(4)、(5) 中每个 \(\phi\) 或 \(\phi^2\) 的自变量，
都是 \(u,\log q,\log s,\log p,\log r\) 的线性组合。
其原 \(C^2\) 紧支撑 Fourier 包络仅损失 \(L^C\)；
\(u,q,s\) 平移变成单位相位，\(p,r\) 变成共同 twists。
外部有界 profile 也可直接取绝对值。没有升级光滑性或拆成不同 \(u\)。

同一 packet 的各 \((s,n)\) 可有不同 Fourier 系数，
但其模长被同一 \(W_H\) 支配；先在每个固定参数使用统一大筛，
再对这个共同可积包络作 Minkowski。不能逐频率另选大筛系数。

真实 \(p,r\ne s\) 用精确容斥恢复。两个单点和双单点的直接
绝对包络为 \(C_\phi(\sqrt{R/S}+\sqrt{P/S}+S^{-1})\)。
\(H\) 族有 \(O(H^2)\) 对 \((d,a)\)，每个 \((q,d,a)\)
只有 \(O(X/S)\) 个 \(m\)。因此全族修正平方能量最多
\[
 H^2Q(X/S)(R/S+P/S+S^{-2})\ll_\phi H^2Q^2L^C,
\]
使用 \(S^2\ge X\)、\(P,R\ll Q\)。
这是对所有实际 \(s,n\) 的 sup 修正，不从 signed 子集范数推断。

因而确有对完整 \(H\) 族、全部 \(s,n\) 共用的正包络 \(F\)，
\[
 |\mathcal B_n^g|\le F_{q,d,a,m}(u),\qquad
 \sum_{\mathcal A_H}F_{q,d,a,m}(u)^2
 \ll_\phi(H+D)^2Q^2L^C.
\]

## 6. 在完整 H 族恢复全部外权

不先分别支付每个 \((d,a)\)。原外权另一 Cauchy 因子满足
\[
 \sum_{\mathcal A_H}b_q^2\ll H^2(X/S)\sum_qb_q^2
 \ll_\phi H^2X/S.
\]
故 \(\sum_{\mathcal A_H}b_qF\ll H(H+D)Q\sqrt{X/S}L^C\)。
同一 packet 的实际整数 \(n\) 个数至多 \(QD/(HS)+1\)；
\(+1\) 不可删除。原 \(s\) 正质量 \(O(\sqrt S)\) 和
原 \((2\pi s/q)\nu\) 点态权 \(O(S/(QX))\) 给
\[
 \sqrt S\frac S{QX}\left(\frac{QD}{HS}+1\right)
 H(H+D)Q\sqrt{X/S}
 \ll\frac{(H+D)(QD+HS)}{\sqrt X}L^C.
\]
\(H\le D\) 后即 \(D^2(Q+S)L^C/\sqrt X\)。
全部 \(H\) 和 \(d=1\) 单列只添对数，全部 \(Q,S,P,R\)
boxes、共同 \(u\)、四种真实最大位置同样只添原固定因子或对数。
因此完整原主弧确为 \(O_\phi(D^2\sqrt X L^C)\)。

## 7. Region、产品 cap 和剩余的准入范围

任意 \(n\) 无关 \((q,s)\) region 都可以在上述正包络证明中重新限制
\(q\) 子族及 \(s\) 正质量。频率集合的子族不会破坏分离性。
所以 region 主弧得到同一个界，无须由 signed 全域界推其子域。
实际 \(qs\le Z\) 可横切 dyadic box，不发生阈值固定倍数泄漏。

旧 cap 源已在完整 \(n\) 逆变换后支付 \((Z/X+1)L^C\)，
含非零整数 aliases、真实 near 产品和所有原权。
完整 cap 减去按本证明重新支付的 region major，合法给
\[
 |\mathfrak I_D(qs\le Z)|\ll (Z/X+1)L^C+D^2\sqrt X L^C.
\]
完整 \(q\mid n\)、低产品、chirp、graph 和边界付款仍保留。
旧全 minor 的 \(s\) 点排除证明只要求 \(n\) mask 依赖 \(q,n,S\)，
新 major 的 complement 满足该条件；它只在正平方和中扩到全 period。

独立 Fraction 算式核对 \(\eta=1/100,\delta=1/10\)：
\[
 12/7-\eta=1193/700,\quad5/7-\eta=493/700,
 \quad1/2+2\delta=7/10,
 \quad5/7-7/10=1/70>0.
\]
旧 \(D^3\) 与中间 \(D^{5/2}\) 指数分别为 \(4/5\)、\(3/4\)。
这只核算有理数，不认证任何连续或无限解析输入。
低产品费用可取固定 \(\epsilon\) 使 \(\delta+\epsilon<1/2\)。
\(Z\gg DX\) 保证最终 \(qs>Z\) 的 boxes 全为新高产品 boxes；
扩大 major 后的准确 complement 没有漏掉未付款的低产品频率子集。

## 8. 中间334行源与最终限制

中间源也已独推：CRT 的模 \(d\) 因子可合到产品系数中，
固定 \(q\bmod d\) 后系数与 \(q\) 无关，非主角色的有限 Parseval
和 primitive 大筛给 \(dQ^2\) 能量；principal 单独保留。
直接打开核读的 [Kedlaya Theorem 18.2 及证明](https://kskedlaya.org/ant/chapter-18.html)
确认只求 primitive 角色、外带 \(q/\varphi(q)\) 权；实际素数 \(q\)
的全部非主角色满足它的前件。
其动态前缀必须先固定 binary 区间对，再在正能量中扩 \(q\) 族。
中间源121—123行明确先取与 \(q\) 无关的固定区间对，153—157行
只对该固定序列扩展正角色能量；177—186行才恢复实际前缀。
这项量词澄清与最终334行哈希绑定，未把 \(q\)-相关序列直接送入大筛。
chirp 后固定 \((d,a)\) 能量为 \(d(1+D/d)^2Q^2L^C\)，
外权费用为
\((d+D)d^{-1/2}(QD/(d\sqrt X)+S/\sqrt X)L^C\)。
按全部至多 \(d\) 个 \(a\) 及 \(d\le D\) 求和确给
\(D^{5/2}(Q+S)L^C/\sqrt X\)。这个较弱中间结果不存在发现的阻断。

笔记487全文保持源的真实 \(p,r,q,s\)、同一 \(u\)、全部最大位置、
正载体及 sharp endpoints；其第2节的能量和外权均是固定 \(H\) 族。
第3节的产品 cap、准确 complement 和全部旧付款与本审查一致。
对 \(Z=X^{1193/700}\)，直接由 \(q\le X\)、\(s<q\)、\(qs>Z\)
得到 \(q>X^{1193/1400}\)、\(s>X^{493/700}\)、
\(q/s<X^{207/700}\)；\(g\ne0\) 与 \(p,r<q\) 给 \(p,r>s/2\)。
该支撑收缩没有被当成剩余能量上界。笔记开头与末尾明确保持
项目已知比例、引用输入下的既有边界和完整四矩基线。

最终不同作者审查没有发现新340行证明的实质缺口。
PASS 绑定表中两份研究源及笔记487的最终哈希；不能移植到未读的新版本。
没有执行 heavy pipeline、有限素数采样或外部计算程序来代替数学证明。
准确未付款项仍为高产品域内原 \(F\cdot G\) 的完整 signed minor union。
原 \(n/q^2\) minor 频率不属于本次 rational approximant 大筛集合。
本审查只准入已明确证明的主弧/region/cap 缩约，所有 whole、比例与 strip
消费仍须另有完整证明，不能从该局部付款直接宣布。
