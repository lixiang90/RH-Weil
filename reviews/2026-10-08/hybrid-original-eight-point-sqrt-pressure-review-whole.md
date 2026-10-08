# 原八点平方根压力、全 offset 与 AM 实际计数的独立审查

2026-10-08。审查作者：whole。只新增本审查，不修改研究源、笔记、
证书、脚本、输出或 Git。

结论：在项目已经接受的304固定函数相关公式与原计数合同下，
研究源的有限平方根对偶、全部 offset 压力、AM 自身二矩和条件比例装配
均通过本轮独立数学审查。两段自写有限代码已独立重跑并通过。
外部 PC8CL 全域证书未运行，未逐叶和逐依赖审完，故其式(16)继续未准入；
本审查没有新增项目实际简单比例。

## 1. 冻结对象、全文范围与执行范围

全文审查对象为
[419行研究源](hybrid-original-eight-point-sqrt-pressure-research-compression.md)，
canonical LF SHA256：

~~~text
94dcf6cde41a78dad81a5ed4d7a1513478bbc09746603a2397b677548fdd4161
~~~

同时完整阅读304、477作者源和477–479笔记，核对当前 canonical LF hashes：

| 输入 | SHA256 |
|---|---|
| [304](../../notes/304-mt-triple-geometry-and-second-moment-stability.md) | 03f21ab1749157ff45bc4d4f62709e2a5482257c7155e7e8e644da0ac4521bc4 |
| [477作者源](hybrid-original-multipoint-envelope-and-actual-counting-research-compression.md) | 59b399445a3022ce9b5ee6c064660e1602dab6d5641d3793649f16f509fc5efa |
| [477](../../notes/477-original-vaughan-reduction-and-replayed-multipoint-proportion.md) | 9c2da25b665070fe5496b9b02cbe382208cd3b60dc793af1ae018ede395bd6b5 |
| [478](../../notes/478-original-mt-six-neighbor-dual-and-whole-chain-proportion.md) | 6ab8384289cf7470b7ee448e381f5e9afdd268b13852f95322c98c1a62dd5c54 |
| [479](../../notes/479-original-type-ii-factor-reduction-and-diagonal-gauge.md) | 6b6e15f8a3a83d62e1d472cbeaa86a894c9e01740ccd682fc79ec99c2ec5a559 |
| [前沿记录](../../literature/supplements/2026-10-08-proportion-frontier-audit.md) | a84e418e5540dc4694740515680bc8b8287f05d94bbf9a90eccd80721abedabd |
| [C0有理输出](../../output/hybrid-multipoint-cap-exact-algebra.json) | d84077ab71b47d1ea253cad9675fa8c25f9aa4dade775ad73ff53033167625c3 |

外部只读核对固定
[Solution.lean，d272437](https://github.com/josusanmartin/riemann/blob/d272437e7ebeb17b87c8c3d7cece592aa23785ab/submissions/dani-bound-2026/proof/Solution.lean)
的窗/核定义、WCert以及PC8CL最终入口与参数。
其 `kfunAM` 按积分质量 `KfunAM 0` 归一化，与本稿 AM 概率密度相同；
WCert 的 span capacity 和非均匀压力也对应研究源的式(5)–(6)。
这里没有以外部定理名称替代证书执行，也没有将其末尾 `N0star` 导出
当作本项目的简单计数证明。

实际执行仅为研究源两段已逐行审读的自写 Python：
第一段用 Fraction 做精确有理比较，第二段用 bundled python-flint 的
Arb160 包围固定有理点。运行通过标准输入，使用 `-B`，没有写文件。
未执行外部 Lean、nanoda、PC8CL、证书生成器或网络下载代码。

## 2. 有限带色平方根对偶通过

令带矩阵 K 保留 Hermitian G 的条目
0<|r_i-r_j|≤q，且 rank 是整数的注入标号。
由于 K Hermitian，E=Tr K²=Σ|Kij|²；这不是任意非 Hermitian 矩阵的平方迹。

对单位 v，Cauchy 给

\[
 |v^*Kv|^2\le E\sum_{0<|r_i-r_j|\le q}|v_i|^2|v_j|^2.
\]

按 rank mod(q+1) 着色。同色不同 rank 差至少 q+1，故没有同色带边。
设各颜色质量为 p_a，则带边和至多 1−Σp_a²≤q/(q+1)。
所以原行序上的有限矩阵满足

\[
 \|K\|_{\rm op}\le\sqrt{E/\tau},\qquad \tau=(q+1)/q.
\]

此处既没有把实际标号周期化，也没有要求 G 的对角等于1。
Hermitian 条件保证绝对 Rayleigh 商确实控制完整算子范数。

对任意 Hermitian B≤I，在 G 的谱基下有 b_ii≤1，且
Tr B²≥Σb_ii²。因此

\[
 2\operatorname{Tr}B(G-I)-\operatorname{Tr}B^2
 \le\sum_i\sup_{b\le1}\{2b(t_i-1)-b^2\}
 =\operatorname{Tr}j(G).
\]

当 0≤t≤2，最大值在 b=t−1；当 t≥2，最大值在 b=1。
恰给研究源的 j，而非对所有实数误用同一凸支。

由于 K 对角为0且只在所保留条目上非零，
Tr K(G−I)=Σ保留条目|Gij|²=E。
取 B=αK，α=min(1,√(τ/E))，上述范数界使 B≤I。
故 J≥(2α−α²)E，分别得到 E 与 2√(τE)−τ。
E=0 单独用 J≥0，消除除以 E 的例外。

fτ 两支在 E=τ 处连续且导数为1；大支导数 √(τ/E)≤1。
因此它递增、1-Lipschitz且不超过 E，后续压力迁移合法。
这份证明与研究源式(1)–(4)一致，没有遗漏对角条件。

## 3. 非均匀压力与全部 m 个 offset 通过

在 m 个排序点 y 上累加 m−q 个局部 q+1 点窗口。
对距离 h≤q 的固定全局无向边，其总系数是局部
a_i,i+h 的一个子和；全部权非负且完整 span mass≤2，
所以该边总贡献不超过2|k|²。正好由有向带能量 E_q 支付。

压力的精确恒等式为

\[
 \sum_{t=0}^{m-q-1}\sum_{r=0}^{q-1}b_r
 (y_{t+r+1}-y_{t+r})
 =\sum_{r=0}^{q-1}b_r(y_{m-q+r}-y_r)=P_m.
\]

故 A=c(m−q)≤E_q+P_m。
若 P_m≤A，单调性及1-Lipschitz给
fτ(A)≤fτ(E_q)+P_m；若 P_m>A，J≥0且 F=fτ(A)≤A<P_m。
所以两种情况均有 J(G_y)+P_m≥F。

对长度 s 的完整点链，用 m 个 offset 的连续满块分割。
每个起点 t=0,…,s−m 在这些分割中恰出现一次，
而每个分割的块本征基加端块本征基构成完整正交基。
标量 Jensen 后求和，给 J(G)≥各满块 J 之和；
端块 j 的迹非负，可以丢弃。这里没有重叠块直接相加或 operator convexity。

固定 r 时，某个全局 gap 被 P_m 的区间
[t+r,t+m−q+r) 覆盖至多 m−q 次。
全部起点压力因此至多 B0(m−q)span。
所以

\[
 mJ(G)\ge F(s-m+1)_+-B_0(m-q)\operatorname{span}.
\]

以 (s−m+1)_+≥s−m+1 得研究源式(9)。
s<m、s=0和s=1均合法；空列/单点的 span 按0计。
最后常数 F(m−1)/m 是一次完整链端费，未按簇重复收费。
Gram 内部零特征值仍计算 j(0)=1，环境补零不新增这个余项。

## 4. 304固定平滑桥与计数闭合通过

这里的解析前件仍是304引用的固定函数全零点相关公式，
本审查没有重新证明 BGST 或 Lamzouri 的原解析定理。
在该已接受合同下，本次更换正偶密度没有新增解析尾前件。

每个固定 δ，令 fδ=ηδ²，Qδ=fδ*fδ。
Qδ与Qδ''均为固定实偶光滑紧支撑函数，满足304式(33)的范围。
其 Fourier 恒等式与相关权精确相消：

\[
 \widehat{Q_\delta''}(z)=-4\pi^2z^2k_\delta(z)^2,
 \quad z=i(\rho-\rho')\log T/(2\pi).
\]

因此304式(34)只需两份固定函数合同，而非 δ(T) 的统一导数估计。
所得原自伴 A 的 Tr A=N 与 HS²=(Rδ+oδ(1))N
保留全部离线共轭对和其正负 rank1 块；不要求 A 半正定。
简单临界线特征精确单位，Gram 精确为 kδ 的实位置核。

当 fδ→f 于 L1∩L2，实轴 sup|kδ−k|≤εδ。
两核模≤1，故每平方差≤2εδ。
每 m 点块有向带边至多2qm，所以能量误差至多4qmεδ。
在同一 sparse band 预算上，Jδ+P≥F−4qmεδ。
固定小 δ 后应用全部 offset，只损失斜率4qεδ；
不需要对增长维度稠密 Gram 做扰动估计。

这里一般 f 的接口须存在所陈述的 L1∩L2 实偶平方根平滑序列，
因此已经隐含 f∈L2。不能从“实偶概率密度”一句扩展到任意奇异密度。
第5节的具体 AM 正光滑内窗满足全部这些前件，不存在此范围问题。

原 multiplicity/inertia 给 N≥s+2b、D≥s+b；
谱移位给 4N−HS²≤4b+3s−J。
第一计数式由 4b+3s≤2N+s 得到。
不同点式则用 4b+3s≤N+2D，直接得到

\[
 s\ge2N-\mathrm{HS}^2+J,\qquad
 2D\ge3N-\mathrm{HS}^2+J.
\]

上述第二步没有调用错误的一般不等式 D≥(N+s)/2。
X_T/N→1、先固定 δ 再 T→∞最后 δ→0，给式(13)。
F<m保证分母为正；分子为正时，同一 J 与 s 下界使
不同点下界化简为(1+p)/2。

该结论是实际前缀合同；本稿没有支付任意新窗的 AF 未归一化 S1 尾，
也没有将这个前缀接口说成 canonical J 上原四阶的新费用。

## 5. AM窗质量、正性与自身 R 通过

精确系数绝对和为0.06460471<13/200；
cos(√2u)≥1−u²≥3/4于 I=[−1/2,1/2]，
因此 v≥137/200。整数余弦积分为0，故 ∫v=Z0=√2 sinβ。
fAM=v/Z0确为正偶概率密度；MAM=5/4不进入归一化后的核与 R。
√v 在 I 的邻域光滑，配固定偶 cutoff 并按真实平方质量归一化，
给所需 ηδ 和 L1∩L2 收敛。

对自伴 T=I+|u−v|积分算子，Tf0 的二阶导数为0且函数为偶，
所以 Tf0为常数。h=fAM−f0积分为0，故 R 的交叉项消失。
对整数余弦，二阶导数计算给

\[
 T\cos(2\pi ju)=
 \left(1-\frac1{2\pi^2j^2}\right)\cos(2\pi ju)+\text{常数}.
\]

整数余弦正交且平方积分为1/2，所以研究源式(15)的损失 D_AM
准确包含 Z0²=2sin²β；没有将 AM 窗与 MT 的 C0 免费拼接。
R0由 Tf0在端点的值为1/2+βcotβ，亦与304一致。

全部八点 span capacities、压力 B0与反射对称均逐项精确核对。
这些仅支付权表准入，不能证明 AM 核的全七维最低值。

## 6. 独立有限重跑与条件算术通过

研究源两段代码原样重跑，第一段输出：

~~~text
finite rational checks PASS; global AM8 certificate not checked
~~~

Machin 第一 atan 部分和给上界，第二 atan 部分和给下界，
因此它们给 π 的上界。cos√2 至第6项给上界，
因而 1−cos√2 的严格正下界也正确。
损失分子随 π 增大，分母使用严格正下界，确实得到 D_AM 的上界。
冻结 C0 下端与此独立上界给 2−R_AM>67216841/10^8。

A=1.16725435>τ=8/7，所以使用平方根大支正确。
所给 sr²<τA使 Flo=2sr−τ严格小于 F，且 Flo≤A<m。
正分子下，较小 Flo给较大的分母，故条件比例取它仍为保守下界。

精确重算得到

\[
 p_- =\frac{118513839290}{175971686899}
      =0.673482429920795868\ldots,
\]

\[
 p_- -\frac{6734824}{10^7}
 =\frac{6581516153}{219964608623750000}>0.
\]

差显示约2.9920795869×10^-8，百分数口径差约2.9920795869×10^-6百分点。
这是研究源自身预算的条件下端，不是用该数值倒证全域证书。

第二段 Arb160 重现

~~~text
[0.007257968549711223120650248019034694683813725332 +/- 6.95e-49]
~~~

并严格验证 FW<726/10^5<805003/10^8。
全部给定相邻 gap均>1，故所有 pair距离>1，MT 闭式的分母远离可去点。
这份有限反例只排除把 AM 证书常数直接给 MT 核，
不能排除 MT 的较低全域常数或其它权表/块长仍有用。
约0.0068758的探索阈值和 m316显示均没有被当作认证最优值。

## 7. 仍未准入的精确前件与最终范围

剩余目标是同一真实归一化 AM 核、同一八点权表，对全部非负 gaps：

\[
 \sum_{r=0}^6b_rg_r+
 \sum_{0\le i<j\le7}a_{ij}k_{\rm AM}(x_j-x_i)^2
 \ge805003/10^8.
\]

正压力支付任一 g_r≥c/b_r，剩余可限于有限根盒；
反射对称可缩为 g6≥g0。两者均不支付根盒内的七维完整覆盖。
必须核验 PC8CL 的全部依赖、区间核和导数表、闭 cell 包围、
根覆盖与反射分支、叶检查以及对应实际核的最终传递。
本轮只读最终入口且没有执行它，故该条件保持 [O]。

本轮没有发现必须修改冻结研究源的数学错误。
“唯一剩余前件”只相对于本项目已经接受的304解析合同和该固定路线成立，
不表示这次审查重新认证了所有外部解析论文或外部形式化库。
有限证明与条件数值可保留；实际采用式(18)仍需完整有限证书准入。
当前项目 p_dg、whole 四矩、无零边界与发布状态均不由本审查改变。
