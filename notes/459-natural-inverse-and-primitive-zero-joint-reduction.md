# 459：自然逆列的有限恢复与 primitive 零点联合能量

2026-10-07。沿实际三列研究继续；未得到新的 strict saving 或无零边界。
本笔记把 redundant Euler pseudozeros 从联合观测量的显式极点中移走，
代价为有限、行依赖的 geometric restoration polynomial。所有原自然
零掩码仍通过精确恒等式/定量余项保留，未删除任何单独 Euler residue。

引用输入是原来源 adc7f124 的自然呈现、deleted Euler 界、raw inverse
合同与普通 finite-order Hecke FE；这些仍为 [R]，不是在此重新认证。
原归一化见 source 705–726，FE 1425–1453，positive-half-plane
deleted products 1602–1640，实际 raw fixed-scale moment 12343–12360，
scale supremum 12394–12408。
[三列反射研究](../reviews/2026-10-07/hybrid-three-column-reflection-research.md)
的 negative-line kernel、全部 primitive/natural residues 与 joins作为
已逐式核读的接口；本笔记不把其 covariance 归约误当作已得 saving。

## 1. 同一个实际 inverse 列

在固定原算术数据与非 principal presentation 中，写

\[
 L_v(s)=L(s,\psi_v^*)D_{R_v}(s),\qquad
 D_{R_v}(s)=\prod_{p\mid R_v}(1-a_{p,v}q_p^{-s}),\quad
 a_{p,v}=\psi_v^*(p),\quad |a_{p,v}|=1.
 \tag{1}
\]

R_v 是 primitive conductor 外的 squarefree redundant radical。
令 f(y)=V(y)y^(-sigma-i omega)，V 支撑于固定 [c_0,c_1] subset
(0,infinity)，sigma 位于固定有界范围。实际 inverse cutoff包含于V；
其 untwisted annular seminorm按原 dyadic stratum统一。omega 可以是
原独立长列 height，不与两个 plain heights合并。

定义同一原归一化的两列

\[
 M_v(X;f)=X^{-1/2}\sum_n\mu(n)\psi_v(n)f(q_n/X),\qquad
 P_v(X;f)=X^{-1/2}\sum_n\mu(n)\psi_v^*(n)f(q_n/X).
 \tag{2}
\]

P_v 是同一个 target 的 primitive inverse，未把 target平方或改变
finite character。它不是原自然列；二者的差由以下真实算术因子支付。

## 2. 精确双向恢复与 scale-supremum 比较

由 reciprocal Euler products在 Re s>1 的绝对收敛展开，逐系数有

\[
 M_v(X;f)=\sum_{h\mid R_v^\infty}
 \frac{\psi_v^*(h)}{\sqrt{q_h}}P_v(X/q_h;f),                \tag{3}
\]
\[
 P_v(X;f)=\sum_{d\mid R_v}
 \frac{\mu(d)\psi_v^*(d)}{\sqrt{q_d}}M_v(X/q_d;f).         \tag{4}
\]

(3)在给定X下实际有限：q_h<=c_1X才可能有term。式(4)是有限
inclusion–exclusion。它们也可直接逐 prime核验：自然 inverse的
p局部系数为1，primitive inverse的局部系数为1-a_p t；在(3)乘
geometric (1-a_p t)^(-1)后精确恢复1。所有mask因此已恢复，未用
primitive phase为非零来删除原自然零。

对每个固定 s>0、epsilon>0，有

\[
 \prod_{p\mid R}(1-q_p^{-s})^{-1}\ll_{s,\epsilon}(NR)^\epsilon.
 \tag{5}
\]

证明可把有限小 norm primes单独合入常数；大 primes满足
-log(1-q^(-s))<=epsilon log q。也有同型的有限加号product界。
令 mathfrak M_v(D)=sup_(0<X<=D)|M_v(X;f)|，
mathfrak P_v(D)=sup_(0<X<=D)|P_v(X;f)|。由(3)–(5)，逐行准确有

\[
 \mathfrak M_v(D)\ll_\epsilon (NR_v)^\epsilon\mathfrak P_v(D),
 \qquad
 \mathfrak P_v(D)\ll_\epsilon (NR_v)^\epsilon\mathfrak M_v(D).
 \tag{6}
\]

若 NR_v<=U^K、K固定，则对任何非负真实行权w_v，同样得到
sum w_v mathfrak M_v(D)^2 与 sum w_v mathfrak P_v(D)^2的双向
U^epsilon比较。无需权重或R_v与row独立；但不能据此创造跨行的
共同 separating measure。这里比较的是scale supremum，非固定
scale的等式，profiles始终是同一个f。

## 3. 固定尺度的可忽略恢复尾

取1/2<theta<1，定义真实有限恢复

\[
 P_{v,\theta}(D;f)=
 \sum_{\substack{h\mid R_v^\infty\\q_h\le D^\theta}}
 \frac{\psi_v^*(h)}{\sqrt{q_h}}P_v(D/q_h;f).                \tag{7}
\]

这仍是复值signed和，不把sum换成positive majorant后称同一观测。
本域理想计数O(X)给 |P_v(X;f)|<=C_f sqrt X在所有可能非空尺度
X>=1/c_1成立；常数对omega统一。故对任意固定 0<t<1，由(5)

\[
 |M_v(D;f)-P_{v,\theta}(D;f)|
 \ll_f D^{1/2}\sum_{q_h>D^\theta,h\mid R_v^\infty}q_h^{-1}
 \ll_{t,\epsilon,f}D^{1/2-\theta+\theta t}(NR_v)^\epsilon.
 \tag{8}
\]

在最后一步，q_h^(-1)<=D^(-theta(1-t))q_h^(-t)，先固定足够小
t。因NR_v仅为U的固定幂，可将theta t及product损失统一写成任意
小的幂损失。截断保留的primitive尺度是

\[
 D^{1-\theta}\le D/q_h\le D.                              \tag{9}
\]

式(8)没有用新Möbius cancellation，仅用Geometric support稀疏与
trivial primitive inverse bound。它不声称原pseudozero residues逐项小。

## 4. 只含 primitive L 极点的具体观测量

对同一psi_v^*和f，选一条无零boundary的rectangle，contours
[-r,c]、r=1/20、c>1，height center omega、H_v asymp U^tau。
对一个row的所有(9)尺度采用同一H_v；primitive zeros集合不随尺度变。
定义Z_v^*(X;f)为其全部primitive reciprocal residues加指定horizontal
joins，multiplicities和可能的primitive trivial zeros全部保留。
原三列报告的 R=1 负线计算给

\[
 P_v(X;f)=Z_v^*(X;f)
 +O(C_v^{-3/2}X^{-3/2})+O(U^{-A}),                         \tag{10}
\]

在(9)大尺度一致成立。先固定profiles、contours、长度范围及有限
内部orders，再取tau与external tail order；没有以height tail order
消灭horizontal inverse。其joins依然是未付的实际积分。

定义

\[
 Z_{v,\theta}(D;f)=
 \sum_{\substack{h\mid R_v^\infty\\q_h\le D^\theta}}
 \frac{\psi_v^*(h)}{\sqrt{q_h}}Z_v^*(D/q_h;f),              \tag{11}
\]
\[
 G_{v,\theta}(s)=
 \sum_{\substack{h\mid R_v^\infty\\q_h\le D^\theta}}
 \psi_v^*(h)q_h^{-s}.                                    \tag{12}
\]

Z_(v,theta)准确是对integrand
fhat(s) D^(s-1/2) G_(v,theta)(s)/L(s,psi_v^*)的全部residues加
同一horizontal joins。G是有限Dirichlet polynomial，entire；因此
本表示没有redundant Euler pseudozero poles。R_v依赖、primitive
phases以及相应natural masks仍在G及(8)余项内，未删除。

恢复(10)的负线余项由

\[
 \sum_{q_h\le D^\theta}q_h^{-1/2}
 C_v^{-3/2}(D/q_h)^{-3/2}
 \ll_{t,\epsilon}C_v^{-3/2}D^{-3/2+\theta(1+t)}(NR_v)^\epsilon
 \tag{13}
\]

控制；它比(8)更小，因为theta<1。vertical tails乘geometric
coefficient mass仍只付任意小幂。于是

\[
 \boxed{M_v(D;f)=Z_{v,\theta}(D;f)
 +O_\epsilon(D^{1/2-\theta+\epsilon}U^\epsilon)+O(U^{-A}).}
 \tag{14}
\]

所有constants依赖固定量词；primitive C_v有固定正下界，可吸入
此界，不需声称它数值上>=1。这里的epsilon可先缩小再吸收NR_v。

对simple primitive zero rho，Z_(v,theta)的residue为

\[
 \frac{\widehat f(\rho)D^{\rho-1/2}G_{v,\theta}(\rho)}
 {L'(\rho,\psi_v^*)}.                                    \tag{15}
\]

未假设零点simple；(15)只是该情况的例式。若Re rho>=beta_0>0，
(5)还给G_(v,theta)(rho)=D_Rv(rho)^(-1)+
O(D^(-theta(beta_0-t))(NR_v)^epsilon)，0<t<beta_0。
所以正实部primitive spike仍然存在，不能把移走pseudozero poles
说成得到新的primitive cancellation或L'下界。

## 5. 对 actual mixed strict saving 的定量等价

取原whole amplification的结构rows，#rows<=U^eta，NR_v<=U^K，
D=U^ell。保持同一原two plain及once-prime slot乘积
B_v=S_(1,v)S_(2,v)Q_v，所有heights、系数和natural zeros不变。
设既有pointwise预算 |B_v|^2<=U^(b+epsilon)；reference b=1/3，
实际小邻域使用其真实b，不免费替换为selected amplitude。
(14)逐行给

\[
 \sum_v|(M_v-Z_{v,\theta})B_v|^2
 \ll U^{\eta+b-\ell(2\theta-1)+\epsilon}+O(U^{-A}).         \tag{16}
\]

令Gamma_tail=ell(2theta-1)>0。对任意固定0<chi<Gamma_tail，
Hilbert norm triangle证明以下两个上界互相蕴含（允许任意小幂损失）：

\[
 \sum_v|M_vB_v|^2\ll U^{\eta+b-\chi+\epsilon}
 \quad\Longleftrightarrow\quad
 \sum_v|Z_{v,\theta}B_v|^2\ll U^{\eta+b-\chi+\epsilon}.
 \tag{17}
\]

同样可对原plain峰集E_chi使用权w_v=1_(v in E_chi)：unweighted
inverse能量的strict saving等价于Z_(v,theta)的restricted能量saving。
原scale-sup raw inverse及(6)也保留其总能量预算。没有根据所需
结论重新定义row family或选择prime coefficients。

例如theta=3/4时，primitive尺度只需覆盖[D^(1/4),D]，
Gamma_tail=ell/2≈0.5621135734。这个数是**近似误差的允许saving范围**，
不是已得到chi=0.5621；(17)两侧的实际joint bound仍需证明。

新归约的价值是将下一输入定位为primitive residues/joins乘有限G的
同对象联合能量，而非另行估计natural Euler poles。G依赖row、含
实际primitive phase，不可从q_R^epsilon mass推出generic separating
measure或独立Gauss phases。L'、multiple residues、horizontal
joins及原unequal-height plain峰的相关性仍是明确未付费用。
没有新比例、边界或正式边界论文；Goal保持原完整目标。
