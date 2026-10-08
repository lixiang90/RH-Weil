# 原平方丰满尾与 Euler 留数接口：主线程独立审查

2026-10-08，root。研究源作者为 checkpoint_audit，审查者另为 root。
本审查针对完整原系数、完整乘积截断和完整正高度窗口。

## 1. 全文与冻结输入

全文读取401行研究源
[平方丰满尾源](hybrid-original-type-ii-large-single-prime-part-research-checkpoint-audit.md)，
canonical UTF-8 LF SHA256：
`66c35eb3ed43cec836ff1d10ed01322f115684c44b771d3db7364637994c3cab`。
还全文读取477 Vaughan、479 short-Lambda/max-prefix、480原分区及476原whole输入。
这些旧源的冻结哈希列在[481精确检查器](../../scripts/hybrid_optimized_type_ii_checkpoint.py)。
没有以摘要、固定数值抽样或脚本输出替代解析证明。

## 2. 全部平方丰满尾的真实四矩

按每个素因子指数是否恰为1，将 k 唯一写成互素 s r，s平方自由、r平方丰满。
它不同于指数奇偶的平方自由核。固定r后合并 n=m s；真实系数为源(6)的
`L^(-1) sum_(ms=n) Lambda(m)b_V(sr)`，m为大 genuine prime，s平方自由，
保留 `(s,r)=1,sr>V`。对所有r和实际V、M一致，绝对值不超过
`tau(r)tau_3(n)`；使用subpower界只放大有限系数，不改变原符号。

真实 inner 区间恰为 `Y/r<n<=X/r`。479的最大prefix引理适用于一致
subpower系数数组；允许它依赖r、X及截断参数。先将每个sharp区间写成
两个原prefix之差，再以该引理支付，不能把斜乘积域当成矩形。

平方丰满r在(K,2K]的个数为O(sqrt K)：唯一表示r=a²b³、b平方自由，
以 `sum_b b^(-3/2)<infinity` 求和即可。故其r^(-1/2)加权质量为O(1)。
这一步对外r作Minkowski，对全部非空dyads K>=H求和，得到
`M_(Q_>H) << X^epsilon(1+X/H²)`。余下日志和一致subpower幂可预先分配
到最终任意固定epsilon。此证明覆盖全部s>=1和全部aspect ratios；原规范
`a_L L`、符号、乘积端点和J_T均保留。

H=V²时，若s=1而k<=H、k>V，则平方丰满k满足rad(k)<=sqrt k<=V，
全部非零Möbius除数已被截断包括，故b_V(k)=0。因此所有非零平方丰满k
都在已控尾中。对新481的floors还有H<=M，genuine prime m>M自动与r互素。
无需另外从一个较大signed函数的范数推出子集范数。

判定：完整尾界通过。它确实扩大已控制子族；它没有控制余下r<=V²的
genuine-prime/squarefree balanced族，也没有直接证明新whole幂。

## 3. small-r 生成函数与零点留数

对每个固定有限V,H>=1，绝对收敛半平面Re z>1上，small-r系数序列准确为
`B_(V,H)(z)=zeta(z)/zeta(2z) C_(V,H)(z)-1`。
有限C中q是rad(r)的除数；它来自固定r的Möbius除数，因此没有q^(-z)权。
另一个除数a进入平方自由s，才有a^(-z)及局部`(1+p^(-z))^(-1)`。
逐项核对互素限制和有限q、a端点后，Euler乘积恒等式成立。

减1不可删：b_V(1)=1；2<=k<=V的b_V(k)=0；r(1)=1<=H。
C是有限和，局部分母在Re z>0非零。Re z>1/2时zeta(2z)绝对收敛非零，
所以B在该域解析，且在zeta零点rho处B(rho)=-1。

真实大prime因子
`A_M(z)=sum_(p>M) log(p)p^(-z)`，以`-zeta'/zeta`减去proper powers和
有限prime段续拓到Re z>1/2。proper-power级数在此局部一致绝对收敛。
在重数m_rho的零点rho处，Res A_M=-m_rho，故Res(-A_M B)=-m_rho。
移除有限低乘积段只改整函数，不改留数。

判定：局部续拓与留数接口通过。该接口说明余项保留原零点障碍；
它没有支付全Perron换线、增长零点和或混合四矩，不是路线不可能性定理。

## 4. 准入范围

本文通过的是研究源的解析尾界和局部Euler接口。
[481](../../notes/481-original-type-ii-squarefull-tail-and-optimized-moment-transfer.md)
另把已证费用联合优化为完整误差13/21；其独立审查和有限重放分别另存。
有限精确系数/Euler重放只检查有限恒等式，不能证明本审查的无穷估计。
原零点比例、whole5/7及引用输入下的sigma_*均保持。
