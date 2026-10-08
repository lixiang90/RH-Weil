# 原高产品次弧有理切片：不同作者全文审查

2026-10-08，perron_reviewer。不同作者独立 FULL READ 与逐段数学重推。
只新增本审查，不修改作者源、冻结输入、输出、检查器或 Git。

**限定 PASS。** 在原 \(qs>Z=X^{1193/700}\) 高产品域、原
\(W=X^{1/10}\) major 的准确 complement 中，新源定义的
\(W<d\le B\)、半径 \(1/S\) 完整真实有理频率子族满足
\[
 |\mathfrak J_{W,B,>Z}|\ll_\phi B\sqrt X\log^C X.
\]
\(B=X^{1/5}\) 的 \(7/10\) 费用、全部原 \(s\) 排除修正和新
complement 缩约均在该限定范围内通过。
没有准入剩余高产品 minor、独立 \(G\) 的目标能量、whole 四矩、
常数级中心四阶预算、零点比例或无零边界。

## 1. 冻结身份与全文读取

canonical 哈希仅将 CRLF/lone CR 转 LF，不 trim，保持 EOF。
下表全部输入已经独立 FULL READ；不能由旧结论或有限采样代替。

| 输入 | 行数／LF字节 | SHA256 |
| --- | --- | --- |
| [新高产品有理切片源](hybrid-original-high-product-minor-rational-slice-research-high-product.md) | 337／14790 | 56219e9f136c0f0666c5b1ce028ec4d7d93ad33f5ebd43d5e4a5e34c399677a8 |
| [原actual unit425](hybrid-whole-fourth-unit-unit-actual-research-whole.md) | 425／16428 | b3f14cf4ee5659f8e23bd51dc9bf71e853e783bd2d55e42ee8846d6e8d1e41dc |
| [原major378](hybrid-original-unit-band-joint-cancellation-research-whole.md) | 378／14896 | 7c95bd2e700c16e0b0e836063f7545e8222a4de4b03d60c3271965252ec744b4 |
| [原cap/修正464](hybrid-original-unit-band-minor-lift-research-pc8.md) | 464／17560 | b6018e1254049b77dd5d7f73f4d3a7dc7272d5fe5dd3568f3c5ddf8cf73928b4 |
| [联合有理大筛340](hybrid-original-unit-band-joint-rational-large-sieve-research-high-product.md) | 340／14702 | 92989568fd5ffbe25a8f6f47997c9ced10acd96b8d3732c740d2cb8a7563ee7e |
| [487](../../notes/487-original-joint-rational-major-payment.md) | 113／5156 | 1768ac94f1d72b1934fa6b8c7290e78717bd2082214e562fde5586c2d788de7d |

本轮直接核读的 [Kedlaya Theorem17.5及证明](https://kskedlaya.org/ant/chapter-17.html)
支持所需的普通加性大筛 \(\rho^{-1}+N\) 弱版本。
不需要新的素数 AP 输入、无零假设或平方模大筛改进。

## 2. 原准确频率 mask 与真实 s interval

原 major 仍为 \(d\le W\)、半径 \(W/(dS)\)。新付款只发生在它的
准确 complement 内，并另外要求 \(W<d\le B\)、半径 \(1/S\)。
两套半径没有互换；新剩余也不能直接改叫 \(B/(dS)\) 主弧的 complement。
若 \(d\le W\) 满足 \(1/S\) 半径，它已经属于旧 major。
重叠表示按固定顺序分配即可，正上界允许所有 packets 重复计数。

固定 \(q,S\) 后，实际 \(s\) 属于原 dyadic 区间与
\(s<q\)、\(s<q(1-4\delta_{\rm near})\)、\(s>Z/q\) 等上下阈值的交集。
因此它是一个与 \(n\) 无关的真实 prime interval，端点可依赖 \(q\)。
原 profiles 经共同 Fourier 分离后产生 twists，而不产生一个任意
\(q\)-私有稀疏 prime mask。
源57—59行对 interval、固定有限 interval union 与任意 region 作了准确限制。
本审查不把这个最大区间大筛扩大到任意 \(n\) 无关 region。

## 3. 新分母域的 guards 与所有频率

由实际 \(qs>Z\)、\(q\le X\) 得 \(s>X^{493/700}\)，
故 dyadic \(S>X^{493/700}/2\)；又 \(QS>Z/4\)、\(q>X^{1193/1400}\)。
\(B=X^{1/5}\) 时充分大 \(X\) 确有
\(B^2\ll S\)、\(QS>64BX\)、\(q>B\)。
这些 guards 是在新高产品域重推，未把旧340源的参数域直接改成 \(B\)。

非空 packet 中 \(|\beta|=|n-cq/d|\le q/S\)，\(c=dm+a\)。
原正 \(\theta_\pm\) 频带给 \(X/(2S)\le n/q\le3X/S\)，
从而 \(c\) 为正整数，且 \(c\le4dX/S<q/16\)。
\((c,d)=1\)、\(q\nmid c\)、\(q>d\)，所以 \(c/(dq)\) 完全约分。
分母唯一恢复大于 \(B\) 的 prime \(q\) 及 \(d\)，分子再唯一恢复 \(m,a\)。
不同实际 \((q,d,a,m)\) 因而给不同 approximants。

固定 \(H<d\le2H\)，分母最多 \(4HQ\)，频率都在 \((0,1/16)\)，
模1 spacing至少 \((16H^2Q^2)^{-1}\)。
对 \(s\) 腿，所有 reduced \(a/d\) 在模1上的 spacing至少
\((4H^2)^{-1}\)，同样包含靠近0、1的圆周间距。
全部每个 \((q,d,a)\) 的 \(m\) 数为 \(O(X/S)\)，每个 packet 的
整数 \(n\) 数为 \(O(Q/S+1)\)。不可删除其中 \(+1\)。

## 4. 共同 n 窗与 s 无关的残余相位

必须先用 \(V(y)=X\nu(2\pi Xy)\) 的零支撑，把各 \(s\) 的频带
精确放进共同 \(J_q\)；分离后旧 \((s,n)\) 指示函数不能再保留。
源(6)保留原 \(\theta_\pm\)、\(|J_q|\ll qX/S\) 及 \(J_q\subset(0,q^2)\)。
新旧 rational masks 只依赖 \(q,n,S\)，仍准确放在外层。

精确原前因子为 \(2\pi S/(QX)\cdot(Q/q)(s/S)V(sn/(qX))\)。
\(V\)、原 \(g(pr/(qs))\) 及所有原 \(C^2\) profiles 分别作共同
Mellin/Fourier 分离，只添可积 \(L^C\) 包络。
原 actual(4)、(5) 的自变量都是 \(u\) 与 prime 对数的线性组合，
所以分离后只产生共享 twists 和外部单位相位，始终是同一 \(u\)。

原相位准确分为
\[
 e_q(ns)=e(as/d)e(\beta s/q),\qquad
 e_{q^2}(-npr)=e(-cpr/(dq))e(-\beta pr/q^2).
\]
在固定 \(s/S\) 窗与固定 \(pr/(PR)\) 窗上，两 residual 参数为
\(\beta S/q\) 和 \(\beta PR/q^2\)，均为 \(O(1)\)，且均与 individual \(s\) 无关。
各固定紧支撑窗的二导数给共同 \((1+|t|)^{-2}\) Fourier 包络。
这与单独 \(g\) 分离一起合法恢复原完整 residual；不是删除 chirp。
不能使用旧 \(z=\beta s/q\) 的 \(s\)-依赖包络后，仍假称 \(F\) 已经因子化。
新稿在155—158行正好明确排除了该错误消费。

于是固定同一参数组 \(\lambda\) 后，真正基本两腿是源(10)的
\(F_{q,d,a}(\lambda)\)、\(G_{q,d,a,m}(\lambda)\)。
不同 \(n\) 可有不同变换系数，但全部被同一可积正包络控制；
不能逐个 packet 另选私有系数。下面每个界均对 twists 大小一致。

## 5. s 最大区间大筛与产品 G 大筛

对 \(s\) 腿，定义源(11)的 \(R_{d,a}\) 为所有整数端点区间的最大值。
它同时支配全部实际 \(q\)-相关 intervals。
固定 binary 块的整数长度 \(O(S)\)、系数能量 \(O(1)\)；
普通加性大筛给 \((H^2+S)\) 能量。
最大前缀逐频率分成 \(O(L)\) 块，Cauchy只添日志；
逐层所有块的能量和不超过全系数能量。
两端点之差恢复最大 interval，故
\[
 \sum_{d,a}R_{d,a}^2\ll(H^2+S)L^C\ll SL^C.
\]
末项使用真实高产品 guard \(B^2\ll S\)，没有宣称每个频率的点值都小。

对 \(G\)，先固定与 \(q\) 无关的两条 binary 区间，合成真实 prime
产品系数 \(C_k\)。每个整数至多有两个有序 prime factor pairs，
所以 \(\sum|C_k|^2\ll1\)，实际长度 \(O(PR)\ll Q^2\)。
整个 reduced approximant 族的直接大筛给 \(H^2Q^2\) 能量。
随后通过完整 binary 展开恢复全部严格 \(p,r<q\)，只添日志。
原 principal及模 \(d\) 残类均包含于完整加性和，没有删去。

## 6. 真实联合族的 Cauchy 与全部点排除

每个 \((q,d,a)\) 有 \(O(M)\)、\(M=X/S\) 个 \(m\)，
\(R_{d,a}\) 又不依赖 \(q\)，因此
\[
 \sum_{\mathcal A_H}b_q^2R_{d,a}^2
 \ll M\Bigl(\sum_qb_q^2\Bigr)\sum_{d,a}R_{d,a}^2\ll XL^C.
\]
与全 \(G\) 能量同族 Cauchy 得 \(HQ\sqrt X L^C\)。
原前因子及 packet 全部 \(n\) 支付为
\[
 \frac S{QX}(Q/S+1)HQ\sqrt X L^C
 \ll H(Q+S)L^C/\sqrt X.
\]
全部 \(H\) 族 \(\sum H\ll B\)，恢复全部原 boxes、同一 \(u\) 和
四个真实最大位置，得到 unmasked 新子族的 \(B\sqrt X L^C\) 费用。

真实 \(p,r\ne s\) 三项容斥不在重叠 packets 中复制。
直接对原准确 \(q,n,S\) 子mask重新证明旧464源第6节的正能量付款。
\(p=s\) 时相位为 \(e_{q^2}(ns(q-r))\)，\(h=s(q-r)\in(0,q^2)\)。
给定 \(h\le X^2\) 至多三个 \(s>\sqrt X\) prime divisors，每个唯一恢复 \(r\)。
两个原 \(b_s\) 使真实合并系数平方能量 \(O(1/S)\)，
完整 \(q^2\) Parseval在正平方和中给 \(Q^3/S\)。
另一因子为 \(QX/S\)，原前因子给 \(Q/\sqrt X\)。
\(r=s\) 对称，双单点的二对一 map更小；全部 boxes 的修正为 \(\sqrt X L^C\)。
这一重推保留原有界 profile、\(g(r/q)\)、真正 \(s\) 支撑与同一 \(u\)。
新mask只依赖 \(q,n,S\)，所以任意该子mask的正平方扩展合法；
并非由一个 signed 全 minor 总界对子集作单调推断。

## 7. 精确剩余与准入限制

原旧 \(qs>Z\) minor精确分成 \(\mathfrak J+\mathfrak K\)。
\(\mathfrak K\) 同时排除旧小分母宽半径和新大分母 \(1/S\) 半径，
所有原 tuple、endpoint、profile和 signed 外相位仍在。
它没有被换成另一个 \(B/(dS)\) 的主弧合同。
与487的完整 cap、旧主弧及全部旧付款合并后，源(21)严格为
\[
 \mathfrak L_U=\mathfrak K_{W,B,>Z}
   +O_\phi((Z/X+1)L^C+(W^2+B)\sqrt X L^C).
\]
\(W=X^{1/10},B=X^{1/5}\) 的两 rational费用同为 \(7/10\)，
cap费用为 \(493/700\)，均严格低于 \(5/7\)。
低产品旧费用可用固定 \(\epsilon<2/5\) 吸收。
对声明的 \(1/10<\kappa<3/14\)，\(B=X^\kappa\) 仍满足全部高产品
guards，且 \(1/2+\kappa<5/7\)，一般参数版本也无发现的缺口。

PASS仅绑定表中新337行最终源。没有 finite采样或 heavy pipeline
代替数学证明；没有修改作者源或冻结依赖。
最大区间大筛的 interval 前件、共同参数和完整点修正是准入条件，不能删除。
准确高产品剩余仍未证明其独立 \(G\) 能量或完整 \(F\cdot G\) signed预算。
本付款扩大原次弧中已付的真实有理子族，不改善整个 whole、比例或 strip。
