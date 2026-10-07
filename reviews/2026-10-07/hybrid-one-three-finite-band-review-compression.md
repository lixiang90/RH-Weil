# 原 actual13 有限 band 桥独审：compression_bridge

2026-10-07。独审人 compression_bridge。结论：**PASS，相对于同一 [R] 与原窗前件**。
只新增本独审，不改被审稿、旧 notes、论文、math、脚本、output、Goal 或 Git。

全文核对对象为
[finite-band 桥](hybrid-one-three-finite-band-admission-research.md)，canonical LF SHA256
`bc6ad6b1a007422c7678cd540b4127b81d2adc168faf5b090a58b6676778e35f`，
10800 bytes / 274 lines。其物理前件为
[physical13](hybrid-signed-one-three-physical-resonance-research.md)，canonical LF SHA256
`0f7c0146e984c49d84fc057394aed1ab9ace658ae5b775b931bfd359a4c47bac`，
16387 bytes / 389 lines。LF hash 仅将 CRLF 与 lone CR 换成 LF。

本次独立复算 band 桥全部六节、精确 Fourier entries、两种全高度替换、
outside carrier 计数、two-crossing trace ideal 及最终幂次。
另已向 radial_review 发送物理前件 §3–4 的逐项 PASS；本报告记录其关键接口。
未把本研究所引用的外部 [R] 重新认证为无条件定理。

## 1. 最小前件与同对象检查

取原 `X=T/(2pi)`、`L=log X`、`Z=sqrt X`、`d=floor XL`，
原 zero-extended interval carrier
`Ee_k=L^(-1/2)1_I exp(i tau_k u)`，`tau_k=T+2pi k/L`，`P=EE*`。
原 phi 支撑 I，0<=phi<=1，a_L 有固定正下界，且对 phi 与 phi² 有
一、二阶导数 L¹ uniformly bounded。因此两者都满足

\[
 |\widehat f(\xi)|\ll\min(L,|\xi|^{-1},|\xi|^{-2}),
 \qquad f=\phi,\phi^2.
\]

只需同一 446 sharp-prime 输入在固定 high-height band 给

\[
 q_H\ll_a X^{a-1/2}L,\qquad
 q_L\ll_a Z^{a-1/2}L,\qquad \theta<a<9/10.
\]

theta=7/8 时 a=89/100 合法。全高度另只用 Chebyshev
`m_H<<sqrt X/L`、`m_L<<sqrt Z/L`。
全部 prime sums 为原 genuine-prime sharp prefixes；没有输入 arbitrary
row-dependent coefficients 的 canonical 小量，也不需 whole fourth budget。

Fourier 取 unitary e^(-itu) convention。原 B_R 的 multiplier
`D_R=-(Q_R(t)+Q_R(-t))/(a_L L)` real even，且
`B_R=M_phi F^(-1)D_R F M_phi` 准确等于原平移算子有限和。
所有 B_R bounded selfadjoint。`D_R 1_J` 仍 real，故 B_R^g 也 selfadjoint；
J=[T/2,3T] 无需关于 0 对称。截频仅用于辅助比较，最终回到原 B_R。
所有含 P 的 traces 因 P 有限 rank 定义，HS 配对也是 trace ideal 合法操作。

## 2. 两种全高度替换均付款

置 `F_0=F M_phi E`。每列为 `(2pi L)^(-1/2)hat phi(t-tau_k)`，
原 tau_k 在 [T,2T)。因此

\[
 \|1_{J^c}F_0\|_2^2
 \ll\frac dL T^{-3}\ll T^{-2},\qquad
 \|F_0\|\le1,\quad\|F_0\|_2\le\sqrt d.
\]

由 `C_R-C_R^g=F_0*D_R1_Jc F_0` 得 HS 差 `O(m_R/T)`。
有限四词 telescoping，每项将该差与另三因子的 HS norm 配对，后者至多
`sqrt d product m_remaining`。于是原 compressed 13 与 good compressed 13
之差为 `O(sqrt d m_H m_L³/T)`，normalized 为

\[
 \frac{m_Hm_L^3}{T\sqrt d}\ll X^{-1/4}L^{-9/2}=o(1).
\]

原 physical 四词准确为
`Tr(F_0* D_1 K D_2 K D_3 K D_4 F_0)`，其中
`K=F M_phi² F^(-1)`，kernel `(2pi)^(-1)hat(phi²)(t-s)`。
按 |t-s|<=T/100 分 near/far，二阶尾给

\[
 \|K_{far}\|=O(T^{-1}),\quad\|K_{near}\|\le2,\quad
 \|K_{far}1_{J'}\|_2=O(T^{-1})
\]

对 length O(T) 的源 interval J' 一致。最后一界确实来自平方核积分：
`|J'| int_|v|>T/100 |hat(phi²)(v)|² dv=O(T^-2)`。
只用 far 的 op norm 会损失本次付款，不能替代此 HS 计算。

把右 input 限于 J_0=[.9T,2.1T]，三个 near 卷积只把频带扩到
[.87T,2.13T]，仍在 J 中。因此 all-near 子词逐个 D 换成 D1_J 完全相等。
其余七词从右取首个 far：此前 near 与 diagonal multipliers 保证源仍在某个
length O(T) 的固定 interval，故该 far 因子以 HS O(T^-1) 付款；其余算子
均 bounded。左 F_0* 以 HS sqrt d 配对。右 J_0c input 的 HS 尾也是 O(T^-1)。
raw/good 两组都可照此控制，故 physical replacement 也是
`O(sqrt d m_H m_L³/T)=o(d)`。没有在中间坏 height 偷用 canonical q_R。

## 3. 原 interval P 的 crossing：无需交换或周期化

一般 `D_R1_J` 不与 P 交换，本证明没有该假设。
B_R^g 的输出支撑 I，故 Q crossing 全由 I 上完整 basis
`e_j=L^(-1/2)1_I exp(i[T+2pi j/L]u)` 中 j 不在 [0,d-1] 的系数表示；
实线 I^c 输出为零。直接全直线 Fourier 计算给

\[
 (B_R^g)_{jk}=\frac1{2\pi L}\int
 \overline{\hat\phi(\xi-2\pi(j-k)/L)}
 D_R^g(\tau_k+\xi)\hat\phi(\xi)\,d\xi.
\]

没有把 D_R^g 周期延拓，也没有把 P 改成全局连续频带投影。
固定 n=j-k，outside j 对应 k 的数量恰为 min(d,|n|)。Minkowski 后可先用
真实 global sup |D_R^g|<=q_R；即使该 factor 依 k，亦合法被统一 sup 控制。

置

\[
 W_L(\xi)=L^{-2}\sum_n\min(d,|n|)
              |\hat\phi(2\pi n/L-\xi)|^2.
\]

无权和还可直接由 interval Parseval 得精确恒等式
`L^-2 sum_n |hat phi(2pi n/L-xi)|²=a_L<=1`，对任意 xi 一致。
加权部分置 nu=Lxi/(2pi)，用 |n|<=|n-nu|+|nu|。
原三段 envelope 对 z=n-nu 给
`|hat phi(2pi z/L)|/L<<min(1,1/|z|,L/|z|²)`。
最近格点 O(1)、1<|z|<=L 的 weighted square 为 harmonic O(log L)、
|z|>L 的 weighted square 为 O(1)。故

\[
 W_L(\xi)\ll\log(2+L)+L|\xi|.
\]

此估计包含 nu 任意接近整数的情况。并且
`int sqrt|xi| |hat phi(xi)| dxi=O(1)`，分 0<|xi|<1/L、
1/L<|xi|<1、|xi|>1 直接可证。故

\[
 l_R^g=\|QB_R^gP\|_2
 \ll q_R\{\log(2+L)^{3/2}+\sqrt L\}
 \ll\sqrt L q_R.
\]

sharp band J 的边界不要求光滑；这一 crossing proof 只用 multiplier sup。

## 4. 三个内部 P 需要两次 crossing

对 bounded selfadjoint V_i，令 y_i=||V_i||、l_i=||QV_iP||_2。
physical-minus-compressed 的三项 telescoping 正是被审稿 (17)。
`||[P,V_i]||_2=sqrt2 l_i`，product commutator expansion 给

\[
 \|QV_{i_1}\cdots V_{i_r}P\|_2
 \le\sqrt2\sum_j l_{i_j}\prod_{k\ne j}y_{i_k}.
\]

每个 telescoping 项先取其左 crossing，再以此界取右 product crossing，
HS–HS 配对产生六对 i<j：

\[
 |\Delta|\ll\sum_{i<j}l_i l_j\prod_{k\ne i,j}y_k.
\]

对 one H、three L 的任何顺序，y_R<=q_R 与 l_R<=sqrt L q_R 给
`|Delta|<<L q_H q_L³`。确切归一化是

\[
 d^{-1}|\Delta|\ll X^{(5/2)a-9/4}L^4.
\]

a=.89 时指数 -1/40；不是以 whole fourth 小量反向估计 crossing。
所有四 placements 都在此引理内，finite matrix 循环用于最后合并。

## 5. 与物理前件接口、最终结论及范围

物理前件 §3 的合法顺序为先用原 chi(S) 支持作乘积截断，再 Fourier 分离
chi 与四个 shifted windows。固定 coordinates 后，同乘积聚合真实 coefficients；
单侧 cutoff 与另一侧 prime 无关。k=3 union 从 min n=8 到 max 2X，跨度
L-log4；k=2 union 从 min 4 到 max 2X，跨度 L-log2。HL 因 h>Z>=r 唯一分解，
且与 LL integer products disjoint。union log spacing 的 Hilbert 费用合法。
这些条件不依 high placement，原 shared windows 仅改变 unit phases。

§4 的全部 alias 计数也合法：k=2 positive alias 最终为空，negative alias
保留 pq<=e²r 及原 physical h<=Xpq/r，给 O(X/L³) mass；k=3 positive alias
只需 h<=e²Z，给 O(X/L⁴) mass，negative alias 因 min n=8>e² 为空。
不能在 far 删除 n>2X，该前件确实留给 joint canonical 部分。
§5 将 middle-far kernel 与四个 windows 同时 Fourier 分离，不另加 tuple
product cutoff；主 height 是原 endpoint 加至多五个 coordinates，ghost 由
原 C² L¹ tail 付款。finite band 桥不会取消这项物理前件的责任。

接受同一物理 o(d) 后，logical order 为：physical raw -> physical good，
再 two-crossing -> compressed good，最后 packet tail -> compressed raw。
每步误差均 o(d)，所以原 `Tr(C_H C_L³)=o(d)`，包括重复与 distinct 标签；
四 placements 的 actual 13 coefficient 为 `4Tr(C_H C_L³)=o(d)`。

结论保持原 phi、E、sharp genuine primes 与全高度 operator。
在已固定 profiles、a 与 [R] 后令 T 趋无穷，没有移动 gap 或目标后选窗。
这是整个 actual13 sector 的新付款；31、distinct22 与 high all-distinct
signed 余额仍未闭合。31 的相同 crossing 指数是 (7/2)a-11/4，当前为正。
本独审不推出 whole fourth 主常数、新零点比例、新无零区域或 RH。

## 6. 正式笔记 461 的最终 hash-bound 全文独审

追加于 2026-10-07。全文核对
[461](../../notes/461-original-one-high-three-low-fourth-trace.md)，canonical LF SHA256
`f9fdf0b721c76a5cc4c4e4821748007e62975286417e6bec9700e39b6778170b`，
6799 bytes / 194 lines。结论 **PASS，相对于其明列的 [R]**。
该追加不改 461，也不改变前五节所绑定的两个研究报告版本。

461 保持原 E、phi、a_L、C_H、C_L 与 genuine-prime cutoff。
Fourier multiplier (5) 与原 translation operator (2) 一致，所有 B_R
bounded selfadjoint，band 仅为估计辅助。一般 theta<9/10 时先固定
theta<a<9/10；只有原 theta=7/8 配 a=.89 时明确记录指数 -1/40。
crossing (7)–(9) 与 height replacement (10) 完整沿用已复算的同对象桥。
`d/N(T,2T)->1` 足够，没有假定不成立的 O(L) 差值。

特别独立核对 461 最终第四矩展开。对有限 Hermitian H,L，置
`A=Tr(H²L²)=||HL||_HS²`、`B=Tr(HLHL)`。六个 22 words 的 trace 和为
`4A+2B`，且

\[
 \|[H,L]\|_{\rm HS}^2=2A-2B,
 \qquad4A+2B=6\|HL\|_{\rm HS}^2-\|[H,L]\|_{\rm HS}^2.
\]

四个 31 words 循环后为 `4Tr(H³L)`，四个 13 words 为
`4Tr(HL³)=o(d)`。所以 461 (11) 的系数、commutator 负号及 o(d)
均准确。这里是在原 finite matrices 中合法循环，没有循环删除 physical P。

461 只移除整个 13 sector。其开放项仍包括 31、22 的 joint product norm
和 commutator、high 全异四词及背景 `Tr(AC³)`。没有把 partial repeated
子常数与 low upper bound 累加成完整主常数，也没有由 459 的恢复等价
直接得到 strict saving。最后保留原边界的陈述是引用状态，不是本独审
对外部无零输入的新认证。
