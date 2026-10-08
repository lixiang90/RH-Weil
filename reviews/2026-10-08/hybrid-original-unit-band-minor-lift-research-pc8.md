# 原 unit-lift minor：完整产品族与真实 s 排除修正的付款

2026-10-08，pc8_cover_audit。基线 main fdf86cb。
只新增本研究源，不修改冻结依赖、检查器、输出或 Git。

本稿取得两项实际付款。原主频带中完整产品族 qs≤Z 的真实 minor
满足 O((Z/X+1)L^C+D³X^(1/2)L^C)；取
Z=X^(12/7−η)、D=X^δ，便覆盖指数严格小于5/7的一个完整产品域，
包括全部 q/s≥X^(2/7+η) 的真实非平衡 aspects。
另将全部 s 求和保留到 n 的正能量之后，原 p,r≠s 的三项修正
在整个 minor union 上付到 O(X^(1/2)L^C)。

没有证明原目标(19)，没有付清剩余高产品 minor，也没有新的 whole
四矩、常数预算、零点比例或无零边界。新增结果保持原 carrier、
同一 u、真实最大素数 q 和全部原 profile。

## 1. 全文读取的冻结输入与实际对象

下列三份源已 FULL READ，行数及 SHA256 均按 canonical UTF-8 LF：

| 源 | 行数／字节 | SHA256 |
| --- | --- | --- |
| [major 联合研究](hybrid-original-unit-band-joint-cancellation-research-whole.md) | 378／14896 | 7c95bd2e700c16e0b0e836063f7545e8222a4de4b03d60c3271965252ec744b4 |
| [major 不同作者独审](hybrid-original-unit-band-major-arcs-review-peer.md) | 222／10927 | 9274d9891903471401389db33d8b76441076eeccfe6193f9a0a1ee5219e05899 |
| [原 actual unit 频带](hybrid-whole-fourth-unit-unit-actual-research-whole.md) | 425／16428 | b3f14cf4ee5659f8e23bd51dc9bf71e853e783bd2d55e42ee8846d6e8d1e41dc |

仍取 X=T/(2π)、L=log X、b_p=log p/(a_LL√p)，a_L≥c_φ>0。
所有 genuine primes 在 √X<p≤X。q 为真正的最大素数，√X<s<q，
分母 p,r<q，原 p,r≠s 的限制保留到第6节的精确展开。
共同 u 的两套 A_p、B_r 精确取原 actual 源(4)、(5)，
半比值前因子为 L^(-1)∫_(I_+)φ(u)²du≤1/2。

仍用原 ν、d floor、θ_±、δ_near=64Δ，Δ=1024L^(5/2)/X；
ν≥0、∫ν=1、||ν^(j)||∞≪X^(-j-1)L^(j/2)。
为区分 major 参数，本稿用 δ_near 表示宽 near，用 δ 表示 D=X^δ。
原 interior 是 qs>4X、q−s>4qδ_near。

对每个 dyadic Q,S,P,R，所有 sharp endpoints 原样保留，
仍假设1≤D≤X^(1/10)。
major 按既有源(7)定义：存在1≤d≤D、0≤a<d、
(a,d)=1 与整数 m，使

\[
 \left|n/q-m-a/d\right|\le D/(dS).
\tag{1}
\]

定义取 dyadic S，**不取某个 individual s**。minor 是原高产品
boxes QS>64DX 中的准确 complement；n=q m 全部在 major。
产品窗仍为原 g∈C_c∞((1/2,2))，0≤g≤1、g=1 于[3/4,5/4]。
记完整 n 主项为 L_F^g，真正 minor 为 I_D。
完整产品域 qs≤Z 的限制只加在 q,s 的 n 无关系数上。

## 2. 任意 q,s region 的完整 nn 加回与产品窗

先对任意 n 无关 q,s region R，在原 ν 主项中加回全部 n=q m。
interior 中 ν support 给 1≤m<q、m 个数 O(X/s)。
原 A、B 的 L2 范数均 O_φ(1)，模 q 加性矩阵范数为 √q，因此

\[
 |\mathcal B_{qm}(q,s,u)|\ll_\phi\sqrt q,\qquad
 \frac{2\pi s}{q}\sum_m
 \nu(2\pi sm)|\mathcal B_{qm}|
 \ll_\phi q^{-1/2}.
\tag{2}
\]

这是一条逐 pair 的 absolute 上界。故任意 R 的 nn 加回成本至多

\[
 \sum_q b_q q^{-1/2}\sum_{\sqrt X<s<q}b_s
 \ll_\phi X^{1/2}L^C.
\tag{3}
\]

不能从一个已付 signed nn 总量推出任意 n 子集；(2)直接控制
该 region 内的完整 multiples，并保持同一 u。

随后才在完整 n 中插入 g。原证明的 χ-tail 和整数 aliases
均使用 absolute 全族包络；R 的限制只缩小这些正包络。
所以完整 R 仍有

\[
 L_F(R)=L_F^g(R)+O_\phi(X^{-2}L^C).
\tag{4}
\]

第3节也会直接控制带 g 的逆变换，因此本次不需要把(4)错误地
推广到 individual n 或任意频率子集。

## 3. 完整 n 逆变换后支付全部 qs≤Z

令 A=qs、c=q²、K_0(v)=∫ν(θ)e^(iθv)dθ。
对所有原系数、profile、g 完成整个 n 后，Poisson 精确给

\[
 \frac{2\pi A}{c}
 \sum_{n\in\mathbb Z}\nu(2\pi An/c)e_c(n(A-pr))
 =\sum_{\ell\in\mathbb Z}
 K_0((A-pr+\ell c)/A).
\tag{5}
\]

interior 使 θ_+<2πA，故左边只有原实际 band
0<n<c 上的 ν support。这里同时保留 e_q(ns) 和全部 s，
没有先对外 s Fourier 取 absolute 后制造“正交”。

非零 aliases 的距离有完整控制。因 pr<q²，ℓ≥1 时
|A−pr+ℓq²|≥A；ℓ≤−1 时最近的距离至少 q²−A，
而(q²−A)/A=(q−s)/s>4δ_near。
其余 aliases 的 v 步长为 q/s≥1。主 ℓ=0 项在
|A−pr|>δ_near A 时也位于原已付 χ-tail。

ν 是原 χ 及 k 的概率平均，所以
|K_0(v)|≤|Γ(s_Tv)|。原 stretched 尾在
|v|≥δ_near 处具有远超过本稿所需的固定省幂；
沿所有 lattice aliases 用原 source 的积分加最大值包络，
整个原四权质量 O(X²L^C) 后尾仍为 O(X^(-2)L^C)。
任意 R 仅减少这个 absolute 尾和。没有删除 gate 外 aliases。

在剩余真实整数 near 中，|K_0|≤1，
pr∈[A(1−δ_near),A(1+δ_near)]。全部四权及原有界
profile 的绝对值至多 C_φ/A；同-u 积分只添固定因子。
每个整数 a=pr 的有序 genuine-prime factor pairs 至多2个：
不同 prime 因子的唯一分解只允许交换两腿，p=r 时只有1个。
所以这里不必使用旧低产品证明的 τ(a) 或 X^ε 损失。near 的 a 个数
O(δ_near A+1)，故每个 q,s 的完整费用至多

\[
 C_\phi
 \left(\delta_{\rm near}+\frac1{qs}\right).
\tag{6}
\]

q 最大性、s 排除、prime supports、g≤1 只减少此正计数。
对全部 √X<s<q≤X、qs≤Z 扩到整数后，

\[
 \#\{(q,s):qs\le Z\}\ll ZL,\qquad
 \sum_{q,s>\sqrt X}\frac1{qs}\ll L^2.
\tag{7}
\]

第一式来自按 s 求 min(X,Z/s)，第二式是完整整数调和和。
于是对于任意该产品域内的 n 无关 region R，

\[
 \boxed{|L_F^g(R)|\ll_\phi
       (Z/X+1)L^C.}
\tag{8}
\]

本式覆盖整个 products union，而非一个固定 q,s 或 dyadic 点。
在单个 Q,S box 中同一论证给 O((QS/X+1)L^C)；
全族(8)直接按 q,s 求和，避免把全部 P,R boxes 重复计数。

## 4. Region major 必须重新使用非负公共包络

不能由 signed major 的全域上界推其 qs≤Z 子域。
所幸既有 major 证明给出逐 q,m 的非负公共包络
F_(q,m)^(d,a)(u)，同时控制该 packet 的全部 s,n，且

\[
 \sum_{q\sim Q}\sum_m F_{q,m}^{(d,a)}(u)^2
 \ll_\phi(d+D)^2Q^2L^C,\qquad
 K_d\ll QD/(dS)+1 .
\tag{9}
\]

R 仅限制 q 和 s 的 n 无关支持；取 absolute 后，
Σ_(s in R(q))b_s≤Σ_(s∼S)b_s≪√S。
同一包络、完整 m 范围与 K_d 因此重新给固定 d,a 的费用

\[
 (d+D)\left(\frac{QD}{d\sqrt X}+
                       \frac S{\sqrt X}\right)L^C .
\tag{10}
\]

这里 principal character、所有 residual classes、动态 q-prefix
和 +1 均沿原证明保留。按全部 a、d、boxes 及四个最大位置，
得到 region major 的真实 absolute 付款

\[
 |L_{F,\mathrm{major}}^g(R)|\ll_\phi D^3X^{1/2}L^C.
\tag{11}
\]

该推导允许 qs≤Z 横切一个 dyadic box，不把其放大边界当成
严格 Z。若用整个 boxes 包围，则 dyadic (Q,2Q]、(S,2S]
只带 qs≤4QS 的固定因子；直接使用 R 的原 qs≤Z 系数
无需此泄漏。P,R 的 g 支撑 PR≍QS 与 sharp endpoints 未变。

以 R 取原 high boxes 内的所有 qs≤Z，完整 n 等于 major 加
minor，因而由(8)、(11)

\[
 \boxed{|I_D(qs\le Z)|\ll_\phi
 (Z/X+1)L^C+D^3X^{1/2}L^C.}
\tag{12}
\]

这一步先支付完整 n，再减去已经按正包络重新支付的完整 major。
它不声称某个 individual minor n 的逆变换只在 physical near。

## 5. 完整非平衡付款与新的剩余域

固定 0<η<3/14，取

\[
 Z=X^{12/7-\eta},\qquad D=X^\delta,\qquad0<\delta<1/14 .
\tag{13}
\]

于是(12)的指数为
max(5/7−η,1/2+3δ)，严格小于5/7。
例如 η=δ=1/100，产品族主指数为493/700，
major 指数为53/100；产品族付款本身没有 ε 损失。

因为 q≤X，实际 q/s≥X^(2/7+η) 强制
qs=q²/(q/s)≤Z。因此所有这些真实非平衡 aspects 的完整
minor union，包括全部 p/r aspects、u 和四最大位置，都由(12)支付。
使用 dyadic Q/S 的版本若要避免 factor 2 泄漏，可以取
Q/S≥2X^(2/7+η)，或直接保留实际 q/s 阈值；
仅改变固定常数阈值也不改变幂。

令 I_(D,>Z) 为原实际 minor 中保留 qs>Z 的完整剩余。
与既有 major/low-product 缩约合并，

\[
 \boxed{\mathfrak L_U=I_{D,>Z}
 +O_\phi(X^{5/7-\eta}L^C)
 +O_\phi(X^{1/2+3\delta}L^C).}
\tag{14}
\]

已有的 nn、graph、chirp、边界和 low-product 成本均在此误差内。
对旧来源的任意 ε 型误差，可固定 ε=1/100；
δ<1/14 时 DX^ε 的指数小于1/2，直接被上述误差吸收。
原实际对象、同-u 和全部 carrier 没有改变。

剩余的每个真实 pair 自动满足

\[
 q>X^{6/7-\eta/2},\qquad
 s>X^{5/7-\eta},\qquad q/s<X^{2/7+\eta}.
\tag{15}
\]

g≠0 又给 pr>qs/2，p,r<q，因此
p,r>s/2>X^(5/7−η)/2，且
max(p,r)>X^(6/7−η/2)/√2、max(p,r)/min(p,r)<2q/s。
dyadic scales Q,S,P,R 有相应固定 factor 2 或 4 外包围，
不能把这些固定常数删掉后冒称 exact support。
这些是精确剩余域收缩，不是对其尚未证明的能量界。

## 6. 保留全部 s 后，整个 minor 的点排除修正已付

下面结果覆盖全部原 minor，包括 qs>Z；不依赖(12)的产品 cap。
也适用于任意 n 无关 q,s region，例如 cap 或动态 interior。

固定 Q,S box 及共同 u。令 R_(q,s) 是原有界 profile 与
g 等 n 无关系数。先写不排除 p=s,r=s 的双腿，真实双腿严格等于
未排除和减 p=s 和减 r=s，再加 p=r=s；这是精确容斥。
对于 p=s 项，外相位与内相位精确合成

\[
 e_q(ns)e_{q^2}(-nsr)=e_{q^2}(n\,s(q-r)),\qquad
 g(pr/(qs))=g(r/q).
\tag{16}
\]

所有原 profile 保持同一 u，并直接保留为 bounded n 无关系数；
无需把 φ 换成更光滑的函数。
minor(1)只依赖 q,n,dyadic S，所以可在 n mask 外完整求和全部 s。
若错误地用 individual s 定义 major，这一步不能成立。

令 V(y)=Xν(2πXy)。其相对 support 位于固定紧区间，
对 log y 的前两导数只损失 log^C；Mellin inversion 有

\[
 V(y)=\frac1{2\pi}\int\widehat V(t)y^{it}dt,\qquad
 \int|\widehat V(t)|dt\ll_\chi L^C .
\tag{17}
\]

必须先用 V 的零支撑，把原各 s 的 I_(q,s) 改成共同

\[
 J_q=\left[\frac{q\theta_-}{4\pi S},
           \frac{q\theta_+}{2\pi S}\right]\cap\mathbb Z,
 \qquad |J_q|\ll qX/S .
\tag{17a}
\]

高产品 QS>64DX 保证大 X 时 J_q⊂(0,q²)。
在 J_q 中，V 对每个 s 的原零支撑仍精确表示 actual band；
**分离后的系数不能再保留依赖 s,n 的 I_(q,s) indicator**。
然后才使用(17)。这没有 Mellin 截断或支持泄漏误差，也不能
把有支撑的 V 换成单一 twist 后让 n 无界求和。

原 prefactor 精确为
(2πs/q)ν(2πsn/q)=[2πS/(QX)](Q/q)(s/S)V(sn/(qX))。
固定 t 时，n^it(qX)^(-it) 是模长1的外因子；
s^it 放入系数。把(Q/q)也按其固定上界吸入外 q 权，
固定 2π 因子纳入 C_φ，p=s 项在 S/(QX) 前因子下变为

\[
 H_{q,n}=\sum_h c_{q,h}e_{q^2}(nh),\qquad
 c_{q,h}=\sum_{\substack{s,r\\s(q-r)=h}}
 b_s(s/S)\,b_s b_r\,R_{q,s,r}(u)\,s^{it}.
\tag{18}
\]

第一 b_s 是原外 s 权，第二 b_s 是被置为 p=s 的原 p 权。
所有 genuine-prime、p=s 属于 P box、r 属于 R box、s<q、
interior 和 region masks 均留在 c_(q,h)。
|R|≪_φ1，包含原 g(r/q) 和实际同-u profile。

q 最大性给 0<h=s(q−r)<q²≤X²。每个 h 的
prime divisors s>√X 至多3个：四个不同此类 prime 的乘积已>X²。
给定 s 后 r=q−h/s 唯一。故逐 h Cauchy 和真实权给

\[
 \sum_h|c_{q,h}|^2
 \le3\sum_{s,r}|b_s(s/S)b_s b_rR|^2
 \ll_\phi S^{-1}.
\tag{19}
\]

这里只用 Σ_(s∼S)b_s^4≪1/S 和 Σ_rb_r²≪1；
twist、profile、动态 s mask 均不增范数。这个真实 1/S
正是先保留全部 s 后才得到的系数能量节省。
因 h 严格在(0,q²)，完整 q² Parseval 没有 products aliases：

\[
 \sum_{q\sim Q}\sum_{\substack{n\in J_q\\n\ {\rm minor}}}
 |H_{q,n}|^2
 \le\sum_{q\sim Q}q^2\sum_h|c_{q,h}|^2
 \ll_\phi Q^3/S .
\tag{20}
\]

放大到完整 period 只发生在非负平方和，任意 minor mask 合法。
这不是将 signed 完整 n 块免费限制为一个子集。

外 q、n 的另一 Cauchy 因子为
Σ_q b_q²|J_q|≪QX/S，故实际原 prefactor 给

\[
 \frac S{QX}
 \left(\frac{QX}{S}\right)^{1/2}
 \left(\frac{Q^3}{S}\right)^{1/2}
 \ll_\phi\frac Q{\sqrt X}.
\tag{21}
\]

以(17)的共同包络 Minkowski 积分只添 log^C。
r=s 项完全相同。

双单点项 h=s(q−s) 的 map 至多2对1，
三个原 prime 权给系数能量≪1/S²；同样推导的费用为
O(Q/√(XS)L^C)，更小。它不是免费删掉的 diagonal。
所有 Q≤X、S≥√X boxes、两个分子最大位置及两个共轭位置
再取原同-u 积分后，

\[
 \boxed{\text{原 }p,r\ne s\text{ 与未排除双腿之差，在整个 minor 上}
       \ll_\phi X^{1/2}L^C.}
\tag{22}
\]

g 和 φ 未作任何整体 smoothness 升级，ν 是唯一需要共同 Mellin
分离的权。该付款直接消除了旧目标(19)后“尚须支付 s 排除”的
前件；它没有同时证明未排除双腿的 restricted-band 能量。

## 7. 整 s Fourier 的核心能量仍缺什么

对(22)已付的修正剥离后，在每个原共同 Fourier/Mellin 参数上，
主项可写成 F_(q,n)G_(q,n)。令 S_q(R) 为 S box 中保持
s<q、interior 及 n 无关 region R 的原真实 s 集合，则

\[
 F_{q,n}=\sum_{s\in S_q(R)}b_s(s/S)s^{it_3}e_q(ns),\qquad
 G_{q,n}=\sum_{p,r<q}b_pb_rp^{it_1}r^{it_2}e_{q^2}(-npr).
\tag{23}
\]

原 g、φ 用冻结公共包络恢复，动态 q-prefix 和原
n-independent s region 必须保留，不能将系数私下换成无 mask 的
另一范数。对实际 s prefix，模 q additive Parseval 和
|J_q|/q≪X/S 给

\[
 \sum_q b_q^2\sum_{n\in J_q}|F_{q,n}|^2
 \ll_\phi QX/S\,L^C.
\tag{24}
\]

若真正证明旧研究源(19)，即 J_q 中全部 minor 的 G 能量
≪Q²(X/S)X^ε，且参数常数对原公共包络一致或可积，
则(24)与原 S/(QX) 前因子给
O(√QX^εL^C)，且(22)已可恢复原 s 排除。
不能对每个 q,n 另选不同的 Mellin 系数，或把依赖 twists 的
不可积常数藏入 ε。当前(19)及其公共参数控制仍未付；
本稿没有把这条条件推论当作实际全 minor 付款。

**普通平方模大筛不能凭 band 或 minor 自动给该输入。**
已核读 [Baier–Zhao，Theorem 1，原论文](https://arxiv.org/pdf/math/0512271v3)：
任意长度 N 系数的全平方模 additive 大筛费用为
(QN)^ε[Q³+N+min(N√Q,√N Q²)]。
实际 N≍PR≍QS≲Q²，代入仍为 Q³X^ε，不是 Q²X/S。
更换全部 q 为 prime 子族、固定 twists 或 binary prefix
都没有从此定理产生所缺 resolution 因子 QS/X。

这还可由 restricted-band 的实际局部密度解释。令 M=X/S、
N≍QS。频率 α=n/q² 分布在长度 O(M/Q) 的窄区间；
每个分辨区间长1/N，对一个 q 的 n 窗长 q²/N≍Q/S≥1。
取 q 的 prime dyadic 族，总采样个数为 ≍Q²M/log Q，
仅有 O(NM/Q)=O(X) 个此分辨区间。

major 点数对每 q 至多
O(MD²(Q/S+1))：按全部 d,a,m 计数 K_d，
包括 K_d 的 +1。它相对 n 总数 QM 的比例为 O(D²/S)=o(1)。
所以仅仅删除 major 也不能消除这种过采样局部密度。
对任意整数系数的大筛，pigeonhole 仍给一个短区间内
至少 cQ²/(S log Q) 个 minor 采样点。
取该区间中心 α_0，构造单位 L2 的长度 N 系数
a_k=N^(-1/2)e(−α_0k)，并把分辨区间常数缩小到1/(20N)，
则其 Fourier 值在该区间有平方≳N，联合能量≳Q³/log Q。

因此在 QS/X 为真幂的域，目标 Q²X/S 对任意产品整数系数
的大筛事实上不成立。这个例子不是 genuine-prime 两腿，
所以**不反驳原(19)**；它说明未来付款必须消费 prime-product
结构或 F 与 G 的真实联合抵消，不能只引用更细的平方模采样大筛。
实际 ν support 比窄 band 更准确；此密度论证仅诊断该一般大筛
路线，并未把外包围采样当成原 signed 主项。

已核读 [Baier 的新版原论文摘要](https://arxiv.org/pdf/2503.18009v4)；
其改进使用 modular square roots 的高阶能量假设，本稿未引入
这些假设作为免费输入。
[Bettin–Chandee 的原论文](https://arxiv.org/abs/1502.00769)
处理的是 e(a·inverse(m)/n) 型 trilinear Kloosterman fractions。
本实际 phase 是 e(−npr/q²)，没有 inverse variable。
把它完成为 Kloosterman 后还必须证明所有 n、prime 权、
conductor q²、共同 profile 的完整变换和 tails。
本稿未得到这条适用桥，所以没有据此宣布异 q 节省。

## 8. 最终付款与未付款清单

本次新增的实际付款是：

1. 全 qs≤Z 产品 union 的完整 minor 成本(12)，进而(14)的新缩约；
2. 全部真实 q/s≥X^(2/7+η) 非平衡 aspects，而非单 box 或
   individual frequency 的付款；
3. 整个 minor 上全部 s 排除修正的 O(X^(1/2)L^C) 付款(22)。

剩余准确是(15)域内的完整原 unit-lift minor，
去掉 s 排除只付已经证明的(22)，原共同 g/profile 与 sharp
prefix 仍在。没有证明其 G restricted-band 能量或 F·G
signed union 小于5/7，更没有常数预算。
本稿没有进行有限浮点实验或外部 pipeline；有限 sampled q
不能认证上述无限参数界。是否准入新付款还需 root 的全文独推，
后续 whole 与 good-set 消费边界均沿冻结输入保留。
