# C001 独立有符号来源审查

2026-10-13；相对基线 `3a72930e9f9f554b03b41d17d8c8002f1813ca82`。
本文件是独立推导／反例审查，主代理须复核后消费；不改 STATE、cadence 或主代码。
已按 AGENTS 恢复 README、STATE、check/show、当前 Goal、C001 与 D20261013，
核对恢复时工作树为空。没有启动研究后台进程，没有计算 ζ 零点或扩大 N。

对象严格限定为 `scripts/qw_matrix.py` 的实周期 Fourier 核，
`L=log(mu)>0`，正整数指标 `n,m>=1`，`xi_n=2pi n/L`。
本文件的符号不是对完整 Weil 型的符号结论。

## 1. 反向指标核的来源符号

写 `W=P+A+R`，其中 `P=w02`、`A=-w_real`、`R=-w_primes`。
同源定义 `H_s(n,m)=W_s(n,-m)`、`d_s(n)=W_s(n,0)`。
由代码的 off-diagonal 分支（这里 `n!=-m` 且 `n!=0`），

\[
q_{n,-m}(x)=-\frac{\sin(\xi_nx)+\sin(\xi_mx)}{\pi(n+m)},
\quad q_{n,0}(x)=-\frac{\sin(\xi_nx)}{\pi n}.
\]

**极点来源 [proved, 辅助核]。** 设 `t=1/2`、
`gamma=8sinh²(L/4)/L>0`，则精确地

\[
H_P(n,m)=\gamma\frac{t^2+\xi_n\xi_m}
 {(t^2+\xi_n^2)(t^2+\xi_m^2)},\qquad
d_P(n)=\frac{\gamma}{t^2+\xi_n^2}.
\]

令 `r_n=t/(t²+xi_n²)`、`s_n=xi_n/(t²+xi_n²)`，
`H_P=gamma(rr^T+ss^T)>=0`，所有有限截面成立。
这与004的奇极点负平方相容：正指标奇块极点是 `-2gamma ss^T`；
反向块正性不能替代完整极点正性。

**无穷位来源 [proved, 辅助核]。** 对以上 off-diagonal 指标，
`omega0=0`，因而 `w_real` 中的常数项及 subtraction 全消失。令

\[
\rho(x)=\frac{e^{x/2}}{e^x-e^{-x}}
 =\sum_{j=0}^\infty e^{-t_jx},\qquad t_j=2j+\tfrac12.
\]

周期条件 `xi_n L=2pi n` 给出

\[
\int_0^L e^{-tx}\sin(\xi_nx)dx
 =\frac{\xi_n(1-e^{-tL})}{t^2+\xi_n^2}.
\]

所以

\[
H_A(n,m)=\frac2L\sum_{j\ge0}(1-e^{-t_jL})
 \frac{t_j^2+\xi_n\xi_m}
 {(t_j^2+\xi_n^2)(t_j^2+\xi_m^2)},
\quad
d_A(n)=\frac2L\sum_{j\ge0}\frac{1-e^{-t_jL}}{t_j^2+\xi_n^2}.
\tag{1}
\]

每个 H 求和项是正 rank≤2 Gram；级数各项为 `O_L(j^-2)`。
交换积分与级数合法：固定有限 n,m，近零的 sine 是 `O(x)`，
`rho(x)=O(1/x)`，绝对可积；远离零常规几何收敛。
故任意 N、任意实有限向量 v 都有 `v^T H_A v>=0`。
事实上非零有限 v 时严格大于零：若平方和为零，
`sum_n v_n t/(t²+xi_n²)` 在所有正 t_j 为零；
其有限有理函数分子有无限零，恒零后各异极点留数强制所有 v_n=0。
`d_A(n)>0` 也成立，但 `d_A^T v` 对有符号 v 不必为正。

**素数来源 [proved, 辅助核]。** 对单原子 `(a,w)`，`w>0`，

\[
H_{R,a}(n,m)=w\frac{\sin(\xi_na)+\sin(\xi_ma)}{\pi(n+m)},
\qquad d_{R,a}(n)=w\frac{\sin(\xi_na)}{\pi n}.
\tag{2}
\]

真实来源在 `a=log k,w=Lambda(k)/sqrt(k)` 求和。
这是一般有符号 sine 核，不是正 Gram。
因此 `h=v^T H v<0` 若在真实核中成立，必由素数来源承担：
`h_R<-(h_P+h_A)<=0`。反向不成立；实际底向量 h 未在这里认证为负。
当 `a0>o` 且 D<0 但 h>=0 时，排序则依赖全来源常数模耦合，
不能归因于某一个负 h 源。

## 2. 实际 p=2 的两维反例：移动不是 Loewner 单调

只动 `a=log2`、权 `w=log2/sqrt2` 不变，则

\[
H'_{R,a}(n,m)=\frac{2w}L
 \frac{n\cos(\xi_na)+m\cos(\xi_ma)}{n+m},
\qquad d'_{R,a}(n)=\frac{2w}L\cos(\xi_na).
\tag{3}
\]

在 `L=log13`，令 `theta=2pi log2/log13`。
`2^4>13>2^3` 严格给 `pi/2<theta<2pi/3`。
于是 `c1=cos(theta)` 在 `(-1/2,0)`，
`c2=cos(2theta)=2c1²-1` 在 `(-1,-1/2)`。
导数的 n=1,2 主块，除正因子 `2w/L` 后为

\[
\begin{pmatrix}c_1&(c_1+2c_2)/3\\(c_1+2c_2)/3&c_2\end{pmatrix},
\quad\det=-\frac{(c_1-c_2)(c_1-4c_2)}9<0.
\tag{4}
\]

因此对所有 N>=2，该导数是不定型：存在正、负方向。
这排除实际原位置附近单靠移动方向推出 H 的统一 Loewner 单调，
即使两条 diagonal 导数都负。权、偶原子对、反演和自伴保持不提供该单调。
同一原子的 H 本身也不定：`sin(theta)>0`，`sin(2theta)<0`，
故 n=1,2 diagonal 一正一负。
这只是指定反向核的严格边界，不排除全核的其他联合估计。

## 3. 固定向量与移动底向量不可混用

令 v 是原核真实有限奇底单位向量。对冻结 v 定义
`o(delta)=v^T O_delta v`、`h(delta)=v^T H_delta v`、
`beta(delta)=sqrt2 d_delta^T v`、`A(delta)=a0(delta)-o(delta)`。
固定 v 时

\[
D=2Ah-\beta^2,\qquad
D'=2A'h+2Ah'-2\beta\beta',
\tag{5}
\]
\[
D''=2A''h+4A'h'+2Ah''-2(\beta')^2-2\beta\beta''.
\tag{6}
\]

移动单原子时 `a0'=2w/L`、`a0''=0`。
`o'` 应用实际 O 导数，不能只应用 H 导数；特别地，

\[
O'_{nn}=2w(1-a/L)\xi_n\sin(\xi_na),
\]
\[
O'_{nm}=\frac{4wnm}L
 \frac{\cos(\xi_na)-\cos(\xi_ma)}{n^2-m^2}\quad(n\ne m).
\tag{7}
\]

不要把第二式用连续指标极限填 diagonal：原 q 的 diagonal 分支
还包含重叠区间的长度，非整数指标极限没有该分支的 `2cos` 项。
只在 delta=0，冻结 v 的 o 等于奇底；离开0后它只是奇 Rayleigh 值。
因此不能将冻结 v 的 D<0 消费成移动后全偶底低于全奇底的证书。

若逐 delta 重求 `v_delta`，必须先保证奇底单重、有隔离 gap，
固定规范 `v^T v'=0`；此时 Hellmann–Feynman 给 `o'=v^T O'v`，
但 `h'=v^T H'v+2(v')^T Hv`，
`beta'=sqrt2[(d')^T v+d^T v']`。
`v'=-(O-o)^{-1}_{v^perp}(O'-o')v`；没有可控相对 gap，
不能忽略该旋转。014已明确低簇与单条最低直线不同。

## 4. 全部 beta² 与 D 混合项

对同一个 v，写 `a_s,o_s,h_s,beta_s` 为三源投影。
准确账本为

\[
D=\sum_s[2(a_s-o_s)h_s-\beta_s^2]
 +2\sum_{s<t}[(a_s-o_s)h_t+(a_t-o_t)h_s-\beta_s\beta_t].
\tag{8}
\]

这包括三条 beta 自平方与三条双源 beta 交叉；
`beta²=sum beta_s²` 是错误的。全 D 还包含极点/无穷位/素数
在 a−o 与 h 中的交叉，故不能将源内三个 D_s 的和称为全 D。
移动试验要同时报告(5)与重求向量结果，并报告这些混合变化；
只观测 h_R 改变量也不能支付 D 的符号。

## 5. 非循环的背景混合耦合估计

主代理提出检查的背景是 `BG=P+A`；对其可给严格全有限截面混合估计。
设 `c_j=1-e^{-t_jL}`，则

\[
\alpha_A=\frac2L\sum_{j\ge0}\frac{c_j}{t_j^2}<\infty,
\qquad \alpha_P=\frac\gamma{(1/2)^2}=4\gamma=a_{0,P}.
\tag{9}
\]

令 `r_j(n)=t_j/(t_j²+xi_n²)`、`s_j(n)=xi_n/(t_j²+xi_n²)`。
`d_A^T v=(2/L)sum_j c_j(r_j^T v)/t_j`，而
`h_A=(2/L)sum_j c_j[(r_j^T v)²+(s_j^T v)²]`。
对正加权序列 Cauchy–Schwarz 即得

\[
|d_A^T v|^2\le\alpha_A h_A,
\quad |d_P^T v|^2\le\alpha_P h_P.
\]

将极点 rank2通道与全部拱位通道放在同一个直和 Gram 中、一次使用
Cauchy（等价于两项 triangle 再 weighted Cauchy）得

\[
|(d_P+d_A)^T v|^2
 \le(\alpha_P+\alpha_A)(h_P+h_A).
\tag{10}
\]

等价地，`[[alphaBG,dBG^T],[dBG,HBG]]>=0`，
且 `betaBG²<=2alphaBG hBG`。对每个 `L>0`、每个有限 N、
所有实 v 成立，不要求 v 是底向量，不读任何 ζ 零点。
`alphaA` 的收敛仅来自 `sum t_j^-2`，不是新增的算术抵消。
若非有限向量使该 Gram 能量有限，同样可通过直和空间内的 Cauchy取得
其耦合定义；这仍不是完整 Weil 连续型或全补空间的证书。

在 `L=log13`，用 trigamma 的
`sum_j t_j^-2=polygamma(1,1/4)/4` 及60项指数修正转录计算，
`alphaP≈5.87271282561324976823`、
`alphaA≈2.48712032150856991227`、
`alphaBG≈8.35983314712181968050`。[experiment，仅常数转录]

**费用限制：** `alphaBG` 不是实际 `a0` 或实际 `a0-o`。
实际常数模还包括无穷位 diagonal 的重整常数和素数项，奇能量也包括
素数项。尤其(10)不约束 `h_R` 或 `d_R^T v`。
粗略合并完整 beta 只能得到

\[
\beta^2\le2\left(\sqrt{\alpha_{BG}h_{BG}}+|d_R^T v|\right)^2,
\]

仍需支付真实 prime cross term；而 beta² 的上界本身给 D 的下界方向，
不能免费认证 C001 所需 `D<0`。故(10)是可消费的背景费用账本，
不等于实际完整 H/W 的支配，不改变宏观瓶颈。

主代理追加指定 `v=(1,-1)` 的实际 H 反例核查时，本审查确认其背景能量为

\[
h_A=\frac2L\sum_j c_j
\frac{t_j^2(\xi_2^2-\xi_1^2)^2
 +(\xi_1-\xi_2)^2(t_j^2-\xi_1\xi_2)^2}
 {(t_j^2+\xi_1^2)^2(t_j^2+\xi_2^2)^2}.
\tag{11}
\]

尾部 j>=J 可严格上包为
`(2/L)[(xi2²−xi1²)² sum t_j^-6+(xi1+xi2)² sum t_j^-4]`，
其中 `sum_{j>=J}t_j^-p<=t_J^-p+t_J^(1-p)/(2(p-1))`。
理由是 `|r1−r2|<=|xi2²−xi1²|t^-3`，
`|s1−s2|<= (xi1+xi2)t^-2`，及步长2积分比较。
本文件确认该解析公式／尾部，不认证主代理另行保存的完整实际 h 负号区间。
此 v 未正规化；检验 H 符号无需正规化，若消费 o/D 必须先除 `sqrt2`。

## 6. 非重复性、检查范围与晋级门槛

- **旧结果不重记：** 004已有偶奇块公式、极点符号、变分/尾部证书；
  006已有候选残差与加权尾；014已有簇内不能识别直线；
  016已有完整 P−V 恒等式与指定逐块范数线性损失。
  C001的二维 D 判据和位移 divided-difference 也不重记。
- **本次局部新增：** 对实际正指标反向核，(1)把无穷位明确写为
  全有限截面严格正 Gram；(4)给真实 p=2 位置的精确不定移动导数；
  (10)给背景常数模与反向核的统一耦合费用，仍不包含素数交叉。
  来源对象与旧完整 P−V不同。这是辅助核的来源符号与指定单调路线边界，
  不达到长期 Goal 的实质方法类边界。
- **检索限制：** 阅读指定004/006/014/016及原函数，另用反向核、Hankel、
  Loewner等关键词检索现有 notes，未发现本式；没有重新全文审计全部526笔记，
  不声明世界首次，也不声明其外部文献新颖。
- **转录检查 [experiment]：** 用50位 mpmath，在同一 mu=13 的 n,m=1,2，
  以 digamma 求 `sum_j 1/(t_j²+xi²)`、指数修正求和60项，
  独立核对(1)的 H,d 与原 `w_real`，核对(3)与 `mp.diff(q_nm)`；
  最大误差 `8.35238971903811e-52`。导数二维 determinant 约
  `-0.051107161829385853785`；严格负号由(4)，不由小数。
  未 directed rounding，未重放全部12矩阵。
- **未付前件：** 真正奇底 v 的有符号 h_R、全 beta 混合的稳定来源估计；
  从有限正指标系数到连续 form domain 的闭合与量词；
  全补空间和增长 L 的统一费用；非算术移动不是新 Euler 积。
  (1)只约束辅助 H，未证明完整 W 或完整 O 正性。
- **停止：** 若来源实验只验证(1)与不定(4)，或只改变小数而不能给
  在完整对象上的连续范围与费用，不扩大 N，不以一般 sine 敏感性冒充算术机制。
- **重新准入：** 需要实际素数位置的独立有符号求和定理，能对真实奇低谱空间
  控制 h_R 及 beta 交叉，并支付稳定底空间/连续补空间费用；
  或另一算术身份直接比较完整联合能量。提高精度与重拟合不够。

唯一建议下一动作：主代理用同一冻结 mu,N 的保存原核 v，复核(1)/(4)，
然后按(8)查看真实源与两方向负对照的来源变化；若没有上述重新准入输入，
将 C001 的数值扩展停止，保留该局部符号结构作为新机制的准入条件。
实际宏观瓶颈没有改变：仍缺独立约束完整 Weil 正性的来源定理。
