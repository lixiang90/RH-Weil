# 456 第二独立全文审查：高素数 opposite 四词与重复极限

2026-10-07。作者：radial_review。完整读取 456 及其已冻 high/mixed 真正输入，
独立重算三个内部 \(P\) 的删除、物理支撑、近对角整数计数与全部 dyadic
费用；不以有限模型代替分析。只新增本报告，不编辑被审稿、旧稿、脚本、
输出、math 或 Git。

**限定 PASS，无数学阻断。**在原 fixed AF frame、原 carrier、真实
zero-extended translations 与全高度表示中，
\(T_{\rm opp}=o(N)\) 的证明完整。既有 exact partition、\(T_0/T_{22}\)
相同主项与这次付款严格给高素数重复标签并集
\(S_{\rm rep,H}/N\to2S_\psi\)，无需先假设完整 \(\Tr C_H^4=O(N)\)。
此结论不支付四 distinct、完整 high/low 混合或 \(AC^3\)，没有新比例。

## 1. canonical LF 证据绑定与输入边界

canonical LF：CRLF 和 lone CR 均转 LF，再按 UTF-8 哈希。本轮实读：

| 对象 | canonical LF SHA256 | bytes / 行 |
|---|---|---:|
| [456 最终稿](../../notes/456-high-opposite-four-word-vanishing-and-repeated-limit.md) | 7de855634f93f9d92f6d0cbdd762f9894effaaf40f788b3e02de89f961eadb96 | 8936 / 270 |
| [冻结 high 报告](hybrid-high-prime-four-word-response-research.md) | 988f8669a771e5b913bbc546590ceac540fc1391838e948563e4b4578f8ff666 | 19170 / 572 |
| [冻结 mixed 报告](hybrid-low-high-mixed-four-word-research.md) | 71f62b2dd931cfda012e7dad9c4efcfece63f5cf1bb8ff5b466d3e2ac1ae89f9 | 22126 / 589 |
| [新有限脚本](../../scripts/hybrid_high_opposite_exact_audit.py) | 731d8dacae09726610b9958d04fc97d6a8b99e5e112fe21fc567026f83981574 | 3984 / 89 |
| [已有输出](../../output/hybrid-high-opposite-exact-audit.json) | 3bef191084595e821d3e6f892405d9a6dab6471b8bdfe02d858e5ea18e07e466 | 1801 / 81 |

第一次全文实审 456 的 SHA 为
40a8cb259116ad804a3db66122c3d73a78a3a5cd4ca2c74f64388eb3583ac560。
最终稿只更新状态、修复 (17) 的 substack row separator、追加有限 evidence
范围。下文审核的是最终稿；这三项编辑性更新没有改变主数学证明或引入新合同。

前置 bounds 实际来自 high 报告 §2–§5：\(\sum b_p^2=O(1)\)、
\(\sum b_p\ll\sqrt X/L\)、单 prime 高步 norm \(\le b_p\)、crossing
\(l_p\ll b_p\sqrt{\ell_0}\)、\(l_Y\ll\sqrt{X\ell_0}/L\)，以及
\(Y_2=\|BP\|_{\rm HS}=O(\sqrt d)\)，\(\ell_0=\log(2+L)\)。
最后一个由实际 finite-carrier weighted 二矩已付，绝非四矩假设。
mixed 报告 §5 只是删除引理的来源；本报告重新检查其每个差额。

原 [AF v2 §2](https://arxiv.org/html/2608.13637v2#S2) frame、fixed C² taper、
Chebyshev/Mertens 与
[MV weighted Hilbert 输入](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)
仍是范围明确的 classical inputs。456 新 near 付款不调用 prime-pair/triple
猜想、无零半平面、RH 或完整 fourth theorem。

## 2. 三个内部 \(P\) 删除：右 projection 确实保留

写 \(A=B_p=A^*, Y=B=Y^*\)，\(a=\|A\|\le b_p\)，
\(y=\|Y\|\)，\(l_A=\|QAP\|_2\)，
\(l_Y=\|QYP\|_2\)，\(Y_2=\|YP\|_2\)。
原 finite trace 对应
\[
 \Tr(PAPYPAPYP),\qquad
 \text{physical trace 为 }\Tr(PAYAYP).
 \tag{R1}
\]
从左到右逐个删内部 \(P\)，三项差额的绝对 trace 分别由
\[
 PAQYPAPYP,\qquad PAYQAPYP,\qquad PAYAQYP
 \tag{R2}
\]
付款。符号在绝对界中无关；有限 rank \(P\) 使这些 traces 全部合法。

第一项把 \(PAQYP\) 与 \(PAPYP\) 作两 HS 因子，
费用 \(\le a^2 l_YY_2\)。第二项用 \(QAP\) 与 \(Y P A Y Q\)，
费用 \(\le a y l_AY_2\)。第三项以 \(QYP\) 配
\(PAYAQ\)，后者 HS norm 至多 \(a\|YAP\|_2\)。
准确恒等式
\[
 YAP=YPAP+YQAP,\qquad
 \|YAP\|_2\le aY_2+yl_A
 \tag{R3}
\]
才给第三项 \(l_Y(a^2Y_2+a y l_A)\)。
这核准 456(6)；没有把 \(YAP\) 误认成 \(YP A\) 并漏掉右 \(P\)。

按 \(\sum_p b_p^2=O(1)\)、\(\sum_p b_p l_p=O(\sqrt{\ell_0})\)
聚合，再代入真实 \(d=\lfloor XL\rfloor\)，总费
\[
 O\!\left(Y_2l_Y+yY_2\sqrt{\ell_0}
                +yl_Y\sqrt{\ell_0}\right)
 =O\!\left(X\sqrt{\ell_0/L}+X\ell_0/L^2\right)=o(d).
 \tag{R4}
\]
这是平方可求和的 repeated label 付款。若改用四 distinct 的四个
\(\ell^1\) prime sums，此估计不成立；456 没有这样外推。

## 3. 四个大步、五点支撑与原 alias 排除

原物理 product 展开后，(8) 中每个 word 的四个 endpoints 给
\[
 d\,b_p^2b_qb_rK_d(S_4)\langle W\rangle,\quad
 W(u)=\phi(u)\phi(u+S_4)\prod_{j=1}^3\phi(u+S_j)^2.
 \tag{R5}
\]
此式直接来自原 finite-k phase
\(e^{i\tau_k S_4}\)，没有删除 carrier 或 internal \(P\) 而不付费；
后者已经在 §2 单独付过。

每步长度 \(>L/2\)，两相邻同号的位移超过 \(L\)，故相应两个物理点
不可能同在 \(I\)。全部16 signs 只有两个 alternating patterns 可非零。
取 \(+\,-\,+\,-\)，\(a=\log p,b=\log q,c=\log r\)，五个位置为
\[
 0,\ a,\ a-b,\ 2a-b,\ S=2a-b-c.
 \tag{R6}
\]
如果 \(S\ge L/2\)，则 \(S_3=S+c>L\)，与位置0不相容；
如果 \(S\le-L/2\)，则 \(S_1-S=a-S>L\)，与位置 \(S\) 不相容。
反射的 pattern 也同样。因此任何非零实际 path 严格有
\[
 |S|<L/2.
 \tag{R7}
\]
原几何核的潜在 \(\pm L\) alias 是由真实支撑排除，不是被估计者忽略。
在 (R7) 下，
\[
 |K_d(S)|\ll\min\{1,L/(d|S|)\}\ll1/(X|S|),\quad S\ne0.
 \tag{R8}
\]
floor \(d\) 只影响统一常数。两个位置0、\(a\) 的共同区间长度
至多 \(L-a\)，且 \(0\le\phi\le1\)，所以
\[
 0\le\langle W\rangle\le(L-a)/L=\log(X/p)/L.
 \tag{R9}
\]
这个 endpoint factor 在 top dyadic bins 是决定性支付，不能改成1。

## 4. diagonal、far 与精确 near 项费用

\(S=0\) 即 \(p^2=qr\)。三个 labels 都是 genuine primes，唯一分解强制
\(q=r=p\)；两个 patterns 的总 normalized 费用至多
\(2\sum_p b_p^4=O(L^{-4})\)。
这是 diagonal 绝对界，不拿它冒充整个 repeated 主项。

ratio \(p^2/(qr)\notin[1/2,2]\) 时 \(|S|\ge\log2\)；
只有实际 path 非零才使用 (R8)，空 path 正好为零。
far 聚合 normalized bound
\[
 O\!\left(X^{-1}\sum_pb_p^2(\sum_qb_q)^2\right)=O(L^{-2})
 \tag{R10}
\]
支付全部这些 paths 与两个 orientations。

near 非diagonal时 \(\Delta=p^2-qr\ne0\)，\(qr\asymp p^2\)。
因 \(\log p,\log q,\log r\le L\)、\(a_L\) 离零，
\(b_p^2b_qb_r\ll p^{-2}\)；又
\(|\log(p^2/(qr))|\gg|\Delta|/p^2\)。
(R8) 与 (R9) 一起给实际单项 majorant
\[
 O\!\left(\frac{\log(X/p)}{XL|p^2-qr|}\right).
 \tag{R11}
\]
该界即使对极小 \(|\Delta|\) 较粗，仍是合法单侧上界；随后由 §5
对整组做计数。它没有假定 near-prime products 独立或稀疏。

## 5. prime-modulus 二根计数与 \(\ell\mid p\) 分支

456(13) 的 integer lemma 统一成立。固定奇 prime \(\ell\le X\)，
让这里的 \(p\) 遍历 \([P,2P]\) 中全部 positive integers、\(P\ge1\)。
当 \(\ell\nmid p\)，\(\delta_\ell(p)=\operatorname{dist}(p^2,\ell\mathbf Z)>0\)。
沿 spacing \(\ell\) 的 q-progression，单列至多两个最近项，其余按距离
编号，得到
\[
 \sum_{1\le q\le X}|p^2-\ell q|^{-1}
 \ll \log(2X)/\ell+\delta_\ell(p)^{-1}.
 \tag{R12}
\]
中心可以在 q-range 内或外；最近项的距离不小于 residue distance，
余项的 harmonic sum 同样至多 \(O(\log(2X)/\ell)\)。

每个 mod-\(\ell\) 完整 block，任何非零 square residue 至多两个根。
所以
\[
 \sum_{\substack{p\ {\rm in\ one\ block}\\\ell\nmid p}}
 \delta_\ell(p)^{-1}
 \le2\sum_{a=1}^{\ell-1}\frac1{\min(a,\ell-a)}
 =O(\log(2\ell)).
 \tag{R13}
\]
残 block 只减小这个正和；block 数 \(O(P/\ell+1)\)。
再加 (R12) 第一项，由 \(\ell\le X\) 得 nonzero-residue 部分 (13)。

若 \(\ell\mid p\)，\(q_0=p^2/\ell\) 是整数。剔除真正零分母后，
\[
 \sum_{\substack{1\le q\le X\\q\ne q_0}}
 \frac1{|p^2-\ell q|}
 =\ell^{-1}
 \sum_{\substack{1\le q\le X\\q\ne q_0}}\frac1{|q-q_0|}
 \ll\log(2X)/\ell.
 \tag{R14}
\]
包括 \(q_0>X\) 的情形。这样的 \(p\) 只有 \(O(P/\ell+1)\) 个，
也被 (13) 吸收。actual prime \(p=\ell\) 已在此分支；只剔除其
\(q=\ell\) 真 diagonal，不删除 \(q\ne\ell\) 项，也不假赋
\(\delta_\ell(p)\ge1\)。这是本轮重点核准的量词。

## 6. dyadic 聚合与共同 endpoint 的最后费用

取 \(p\in[P,2P]\)、\(P=X/2^{j+1}\)，只留与 \(p>\sqrt X\) 相交的 bins。
设 \(q_s=\min(q,r),q_l=\max(q,r)\)。仅在共同 positive majorant (R11)
中排序，至多因子2；没有交换物理 operators 或免费 cyclic rotation。
near 条件使
\[
 \max(\sqrt X,P^2/(2X))<q_s\le2\sqrt2P.
 \tag{R15}
\]
因此相关 dyadic \(Q\) 满足
\(Q\asymp q_s,\ Q\le CP,\ Q\ge c\max(\sqrt X,P^2/X)\)。
\(\log Q\asymp L\)，Chebyshev 给 genuine prime \(q_s\) 的个数
\(O(Q/L)\)。对每个这样的 modulus，按 §5 把重复 \(p\) 和 \(q_l\)
放大成整数正 majorant，得
\[
 O\!\left(\frac QL(P/Q+1)L\right)=O(P+Q)=O(P).
 \tag{R16}
\]
扩大 q-range 时所有零分母均剔除；这仍覆盖 actual 非diagonal subset。

记 \(\lambda_P=\log(X/P)=(j+1)\log2\)。相关 \(Q\) bins 的数量
是 \(O(1+\lambda_P)\)：当 \(P\le X^{3/4}\)，
\(\log(P/\sqrt X)\le\log(X/P)\)；当 \(P\ge X^{3/4}\)，
lower \(P^2/X\) 给同一上界。部分 boundary bins 只增加固定常数。
由 (R11)、(R16) 及 \(\log(X/p)\le\lambda_P\)，near 总费
\[
 \ll\frac1L\sum_P\frac PX\lambda_P(1+\lambda_P)
 \ll\frac1L\sum_{j\ge0}2^{-j}(j+1)^2=O(1/L).
 \tag{R17}
\]
即使最低 bin 部分超出 high range，此整数上界只增大费用。
若不用真实 endpoint 而令 \(W\le1\)，top bins 在这条 proof 中只得
\(O(1)\)，故不能删除它。456 对这一步的说明准确。

## 7. 原有限重复并集的极限与全高度范围

§2–§6 给
\[
 |T_{\rm opp}|/d\ll
 L^{-1}+\sqrt{\ell_0}L^{-3/2}+\ell_0L^{-3}=o(1).
 \tag{R18}
\]
所有 Fourier/physical 表示本来就在整条 height 轴上进行，
未先截去低高度、负高度或 \(J^c\)，所以无未支付的 height tail。
物理支撑只排除对应 path，finite \(P\) 的三项误差另付；
不是把 spectral integral 分区后的矩阵四次 cross terms 删除。

冻结 high 报告的 exact partition 为
\[
 S_{\rm rep,H}=4T_0+2T_{\rm opp}-2T_{22}-T_\times-8T_3+6T_4.
 \tag{R19}
\]
该报告已用实际 second moment、平方乘法符号与 crossing bounds 给
\(T_0/N\to S_\psi\)、\(T_{22}/N\to S_\psi\)；\(T_\times,T_3,T_4=o(N)\)
也没有 full fourth 前提。特别是 \(T_3\) 只用
\(\Tr|C_H|=O(d)\) 与 \(\sum_p b_p^3=O(L^{-3})\)。
本次 (R18) 因而把 (R19) 精确变为
\[
 S_{\rm rep,H}/N\to(4-2)S_\psi=2S_\psi.
 \tag{R20}
\]
这是 signed repeated union，不能解释成所有单词非负。

flat 的 \(d_{H,\psi}(v)=(|v|+v^2)/2\) 给
\[
 S_\psi=\frac12\int_0^{1/2}(v+v^2)^2\,dv=\frac{19}{480},
 \quad2S_\psi=\frac{19}{240}.
 \tag{R21}
\]
MT 系数仍是冻结报告定义的严格积分 \(2\int d_{\rm MT}^2\)，
显示小数 \(0.0620202440072\ldots\) 没有被误当新 rational 比例证书。
量词是 fixed \(\chi,\psi\)，任意 \(\varepsilon>0\) 后存在统一 \(X_0\)，
所有 \(X\ge X_0\) 的 normalized error 小于 \(\varepsilon\)；
不提供有限 numerical height threshold。

## 8. 最终 editorial 与新有限 audit 的准确范围

初审发现 (17) substack 中少一个反斜杠，已修为真正 row separator；
这是纯显示修复。最终另外更新状态与追加 evidence 说明，主数学不变。
本报告已只读最终末段和完整新脚本/JSON，未运行脚本、未覆写输出。

六个 cyclic-label 模型通过 ordered-word enumeration 与 coefficient
Counter 直接比较 (R19)；不是构造待证右边作为唯一 target。
1134 是指定25个 odd-prime moduli 的 nonzero-residue 输入数；
脚本实际构造 squares、核每个 fiber 至多2，并用 Fraction 比较
reciprocal-distance 正和与 harmonic majorant。
225 zero-progression cases 是25个 moduli ×3个 divisible \(p\) ×3个
中心内/外 cutoff，直接比较零分母剔除后的两边。这覆盖有限模型中的
\(\ell\mid p\) 支付，但不证明任意参数的 asymptotic theorem。
flat \(19/480,19/240\) 的 rational integral 与 (R21) 相符。

JSON 的 note/script SHA 与最终实读文件一致。其 not-certified 项准确：
没有认证无限 prime harmonic estimates、dyadic sum、物理支撑或 projection
删除；这些步骤由本报告的全文数学审核支付。无新增 kernel/whole-chain
认证，没有 full fourth 常数或零点比例结论。

最终验收：**456 指定最终 SHA 的全文限定 PASS，无数学阻断。**
实质付款是 \(T_{\rm opp}\) 的 actual \(o(N)\) 与 high repeated 的实际
\(2S_\psi\) 极限；四 distinct、完整 mixed 与背景协方差仍须单独证明。
