# 原高产品次弧：真实素数腿的点值、联合有理平均接口与费用门槛

2026-10-08，checkpoint_audit。当前基线 main a4e4c8c。
只新增本研究源；不修改冻结对象、既有文件、输出或 Git。

本稿证明两条真实 F 腿输入。普通 Vaughan 次弧点值即使完整恢复
原 C² 公共参数，与已知 G 的 Q³ 能量相配仍不产生当前余项的
5/7 以下付款。另一条输入保留 F 在有理数上的完整平方平均：
当 H²≪S 时，真实 q-dependent 区间的 maximal additive 大筛
仅付 S log^C。这能与联合 G packet 能量相配，提供具体新机制。
本稿不把后一条 G 前件当成已经证明的新付款。

## 1. 原对象、冻结输入与准确剩余

全文核读了 [原 actual unit425](hybrid-whole-fourth-unit-unit-actual-research-whole.md)、
[原 major378](hybrid-original-unit-band-joint-cancellation-research-whole.md)、
[产品 cap/minor464 的第6—7节](hybrid-original-unit-band-minor-lift-research-pc8.md)、
[联合 rational-major340](hybrid-original-unit-band-joint-rational-large-sieve-research-high-product.md)
及 [487](../../notes/487-original-joint-rational-major-payment.md)。
固定 canonical UTF-8 LF SHA256 如下：

- unit425：b3f14cf4ee5659f8e23bd51dc9bf71e853e783bd2d55e42ee8846d6e8d1e41dc；
- major378：7c95bd2e700c16e0b0e836063f7545e8222a4de4b03d60c3271965252ec744b4；
- minor464：b6018e1254049b77dd5d7f73f4d3a7dc7272d5fe5dd3568f3c5ddf8cf73928b4；
- joint340：92989568fd5ffbe25a8f6f47997c9ced10acd96b8d3732c740d2cb8a7563ee7e；
- note487：1768ac94f1d72b1934fa6b8c7290e78717bd2082214e562fde5586c2d788de7d。

X=T/(2π)，L=log X，D=X^(1/10)，Z=X^(1193/700)。
所有 dyads 从 √X 开始，终点按 X sharp 截断；q 是实际最大
genuine prime，s<q，p,r<q。原 b_p=log p/(a_L L√p)，a_L≥c_φ>0。
既付原整 nn、chirp、graph、integer aliases、carry boundaries 和
整个 minor 的 p=s、r=s 修正保持原范围；不能由完整 signed 上界
推出任意频率子集付款。

当前剩余是原同一 χ-carrier signed 平均中的 qs>Z interior unit
minor。对固定 q 和 S dyad，真实 s 支持为一个整数区间的 prime 子集：
下端含 max{dyad 起点,√X,Z/q}，上端含
min{dyad 终点,X,q(1−4δ_near)}，所有 strict endpoints 精确保留。
它不依赖 n。这里不推广到任意 s 区域。

先利用原 ν 的零支撑恢复共同 J_q，再分离 ν 和各原 C² profile，
可在每个共同 Fourier/Mellin 参数上写

\[
 F_{q,n}(t)=\sum_{s\in S_q}b_s(s/S)s^{it}e(ns/q),\qquad
 G_{q,n}=\sum_{p,r<q}b_pb_rp^{it_1}r^{it_2}e(-npr/q^2).
 \tag{1}
\]

产品窗 g(pr/(qs)) 也通过共同 Mellin 参数保留；固定参数后
PR≍QS≲Q²。ν 的精确前因子为
(2πs/q)ν(2πsn/q)=(2πS/(QX))·(Q/q)·(s/S)·V(sn/(qX))，
V(y)=Xν(2πXy)。实际 |J_q|≪qX/S 且 J_q⊂(0,q²)。
外共同参数包络的 L1 仅付 L^C，原空间积分仍是同一个 u。

## 2. 真正 minor 的 Dirichlet approximant

原 minor 排除了所有 reduced a/d、1≤d≤D 与整数平移 m，使
|n/q−m−a/d|≤D/(dS)。包括 d=1,a=0，故 minor 上 q∤n。
令 K=ceil(S/D)。对 α=n/q mod 1 使用 Dirichlet 逼近，可选

\[
 (a,d)=1,\quad 1\le d\le K,\quad
 |\alpha-a/d|\le1/(dK)\le D/(dS),\qquad
 |\alpha-a/d|\le1/d^2.
 \tag{2}
\]

整数平移在 mod 1 逼近时保留。若 d≤D，(2)违反真实 minor，
所以 D<d≤K≤2S/D。ceil 保证第二个不等式，不能误用 floor
然后免费丢掉边界窄环。此处未假设任一 Dirichlet L 函数的 RH。

核读 [Montgomery–Vaughan Vol II 原作者 PDF](https://personal.science.psu.edu/rcv4/Vol2/Vol2.pdf)
Theorem 17.1 及其完整证明（印刷69—70页，PDF79—80页）：
对 (2) 的逼近，Λ 的所有实数 sharp prefix N 有
|Σ_{j≤N}Λ(j)e(αj)|≪(N/√d+N^(4/5)+√(Nd))log^C(2N)。
代 N≤2S 并使用 (2)，得到

\[
 \sup_{N\le2S}\left|\sum_{j\le N}\Lambda(j)e(\alpha j)\right|
 \ll (S/\sqrt D+S^{4/5})L^C.
 \tag{3}
\]

全 Λ 和与真正 prime 的 log-weight 和之差是 proper powers，
逐项绝对和≪√S L²；这是明确支付的 mask 差。
在真实区间 S<s≤2S 上对
√s\,s^(it)/(a_L L S) 作 Abel，sup 与总变差
≪S^(-1/2)(1+|t|)L^C。因此对所有真实 S_q，

\[
 |F_{q,n}(t)|\ll L^C\min\{A,(1+|t|)B\},\quad
 A=\sqrt S,\quad B=\sqrt{S/D}+S^{3/10}+1.
 \tag{4}
\]

任意 fixed interval 可由两条 prefix 的差表示，包含 q-dependent
moving endpoints。这里 A 来自真实系数 ℓ1，而非另一个函数。

## 3. C² 公共参数恢复的真正费用

不能直接积分 (4) 中的 1+|t|：C² Fourier 包络通常只有
(1+|τ|)^(-2)，其一阶绝对矩未必收敛。保留 trivial cap A 后，
对 A≥B 有

\[
 \int_{\mathbb R}\min\{A,(1+|\tau|)B\}
       (1+|\tau|)^{-2}\,d\tau
 \ll B[1+\log(2+A/B)].
 \tag{5}
\]

按 |τ|≈A/B 分开积分即可；A<B 时直接付 A。
实际 t 是有限多个共同 Fourier/Mellin 参数的线性组合。
用 1+|Σ_jτ_j|≤Σ_j(1+|τ_j|) 和
min(A,Σ_jx_j)≤Σ_jmin(A,x_j)，逐参数应用 (5)，其余包络作 L1。
因为 A/B≤√D，结果仅添 L^C。g 的公共 Mellin 包络有更快衰减。
故 (4) 的 B 是真实同-u 恢复后的可积上界，不是隐藏不可积
twist 常数的 X^ε。所有原 2π、ν support 和 sharp J_q 均保留。

## 4. 单独点值与已知能量配对：精确费用 no-go

真实 s<q 使 s residues mod q 不重复。完整 q-period Parseval 后
按 J_q 的长度付款，原 minor464(24)给

\[
 E_F=\sum_qb_q^2\sum_{n\in J_q}|F_{q,n}|^2
       \ll QX/S\,L^C.
 \tag{6}
\]

原 product multiplicity≤2，完整 q²-period 的 G 能量为
E_G≪Q³L^C；普通 Q³+PR 大筛也不改此费用。非负能量可限制到
minor；不得将完整 signed block 换成其 signed 子集。
原 S/(QX) 前因子与 (6) 给 box 成本

\[
 Q\sqrt{S/X}\,L^C.
 \tag{7}
\]

改用 (4)—(5) 的点值再 Cauchy，则成本为
Q√(S/X) B L^C。当前 S≳X^(493/700)，因此 √(S/D)
支配另外两项，得到 Q S/√(DX)L^C。这比 (7)更差。

写 Q=X^u、S=X^w 仅为费用指数表示，dyadic 固定倍数不计为新 saving。
真实残域有 u≥w、u+w≥1193/700（端点只损失 O(1/L)）。
(7) 的最小指数为

\[
 u+w/2-1/2\ \ge\ 2179/2800-O(1/L)
  =5/7+179/2800-O(1/L).
 \tag{8}
\]

点值路线最低指数为 u+w−11/20≥202/175−O(1/L)；balanced Q,S≈X 时
(7)为 X，点值路线为 X^(29/20)。这些是已证上界的费用，
不是实际 F·G 的下界，也不是对所有未来 joint 方法的不可能性结论。

若未来真实正能量能证明
E_F≪(QX/S)X^(-f)L^C、E_G≪Q³X^(-g)L^C，则要在该 box
付到 5/7 以下，充分条件是

\[
 f+g>2u+w-17/7.
 \tag{9}
\]

本 CS 费用达到严格目标必须跨过同一阈值。残域最容易处的阈值
至少179/1400−O(1/L)，balanced 处为4/7。旧目标 E_G≪Q²X/S
相当于 g=u+w−1，比 (9) 所需高出 10/7−u≥3/7；
因此全旧目标是强的充分输入，并非所有 whole 改进的必要输入。
普通 ζ 的 [R_θ] 仅控制普通 ζ；从它直接给 additive/AP 的
Dirichlet L 全族无零输入不成立。本稿没有假装消费该额外输入。

## 5. 新 F 接口：保留 rational average 的 maximal interval 大筛

取 B_*=X^(1/5)，完整 denominator dyads D≤H<d≤2H≤2B_*，
最后一箱在 B_* 截断。对固定共同 twist t，
c_s=b_s(s/S)s^(it) 是所有 rational a/d 共享的原 prime 系数；
nonprimes置零。令 R_(d,a) 为所有整数区间 I⊂原 S dyad 上
|Σ_{s∈I}c_s e(as/d)| 的最大值。

已打开核读 [Kedlaya 作者讲义 Theorem 17.5 及其证明](https://kskedlaya.org/ant/chapter-17.html)：
ρ-separated additive 频率族对 fixed 长度 N 的系数付 ρ^(-1)+N。
本 reduced a/d 族的 mod 1 间距≥1/(4H²)。每个 I 精确分成
O(log S) 个 binary intervals，Cauchy 付 log S；每个 level 的
intervals 不交。对每个 fixed binary block 作 additive 大筛，
然后完整求和所有 blocks 和 levels，给

\[
 \sum_{\substack{H<d\le2H\\(a,d)=1}}R_{d,a}^2
 \ll(H^2+S)L^C\sum_{s\in{\rm actual\ dyad}}|c_s|^2
 \ll S L^C.
 \tag{10}
\]

最后用 B_*²≪S 和 Σ|c_s|²≪L^C。dyad/grid/floor 可先置零
padding 到固定 binary 整数区间，未移动任何真实 endpoint。
所有 fixed twists 的模长为1，故 (10) 常数与 t 大小无关。
原 S_q 的 q-dependent interval 可在最大值中合法消费；
任意 s 集合、任意 n-dependent s mask 不在此结论内。

考虑真实 rational shell |n/q−m−a/d|≤1/S。
δ=n/q−m−a/d 满足 |δ|S≤1，而 e(ns/q)=e(as/d)e(δs)。
选择固定 smooth 窗在 s/S∈[1,2]为1、紧支撑于(1/2,3)。
窗乘 e((δS)y) 的 Mellin transform 有与 δ,q,m,n 无关的
共同正 L1 包络：其前两 log 导数在 |δ|S≤1 时一致有界。
Mellin 后只把 fixed s^(iτ) 加入 c_s。变量 δ 留在包络外，
不能让大筛内部的 fixed coefficients 随 q,m,n 变化。
ν、g、原 C² profile 也沿第1节共同参数精确恢复，同一个 u 不分裂。
这证明 (10) 是原 shell 中真实 F 腿的可积接口。

## 6. 与 G 联合接口的条件消费及结论边界

若在同一组共同参数上，真实 (q,d,a,m) packets 的 G 有正包络
A_(q,d,a,m)，且 ΣA²≪H²Q²L^C，则 (10) 可以直接配对。
每个 q,d,a 的 m 只有 O(X/S) 种，整数 n 数≤C(Q/S+1)；
保留这个 +1，不假设每个 packet 必有整数 n。
F 的 weighted packet 因子至多
(X/S)(Q/S+1)ΣR²≪X(Q/S+1)L^C，
G 因子至多 (Q/S+1)H²Q²L^C。准确前因子给

\[
 \frac S{QX}\sqrt{X(Q/S+1)}\sqrt{(Q/S+1)H^2Q^2}
 \ll H(Q+S)/\sqrt X\,L^C.
 \tag{11}
\]

完整 H≤B_* union 条件成本为 B_*√X L^C=X^(7/10)L^C< X^(5/7)。
这是明确的 F·G 同 packet Cauchy 接口，保留 genuine-prime
F cancellation；它没有把单独点值改善冒充这个平均改善。
G 必须用独立于 s 的 fixed pr/(PR) residual-chirp 窗、原 g
单独 Mellin、全部 q-dependent p/r prefixes 和 packet uniqueness
证明上述统一包络。冻结 joint340 的范围 H≤D 不能仅凭本算术
延伸为全部 H≤B_*；对应扩展须另作完整证明。本稿不预先认证它。

新 shell 的整个 p=s、r=s 修正可沿 minor464 第6节的非负
q²-period 能量证明限制到此频率 mask；该 proof 本来允许任意
minor mask，并非由 signed 全 minor 上界免费限制而来。
所有 aliases、physical carrier scope 和同-u 恢复仍以冻结源为准。

本次完成了 (4)—(5) 的实际可积点值、(8)—(9) 的费用门槛，以及
(10) 的真实固定系数 rational-average F 接口。没有证明当前完整
余项的新 whole 界，没有新常数级 signed 预算、比例、κ 或 strip。
没有进行有限数值实验，也没有将有限 checker 当作无限解析证明。
