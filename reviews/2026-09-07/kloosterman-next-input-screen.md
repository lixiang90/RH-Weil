# 新算术来源筛查：Kloosterman估计与MOM接合要求

2026-09-07。主线程原始条款核读后已完成[独立条款复核](kloosterman-source-independent-review.md)；
实际双线性映射未完成。
这是周期7之后的候选准入准备，不开启第二条并行数学主线。

## 固定原件与核读范围

- Pascadi，arXiv:2511.08445v2，2026-06-21，54页。
  本次核读PDF第1–5页，尤其Theorem1.1、1.2、Example1.3；
  独立复核另定位第36页Thm7.1和41–42页Thm7.8陈述，没有审查技术证明或54页全证。
- Milićević–Qin–Wu，arXiv:2511.07550v1，2025-11-10，37页。
  本次核读PDF第1–4页，尤其Theorem1.1与归一化定义；
  没有认证后续完整证明。
- Choi–Kumchev，arXiv:math/0412227v1，上传日期2004-12-12，20页。
  PDF第一页自身标“Draft from September 26, 2018”，两种日期分别保留；
  arXiv给期刊版本Acta Arith.123 (2006),125–142。本次只核读PDF第1–2页。
  PDF draft日期本身不证明2018年出现实质修订。

另存Pascadi 2026-08-21在线发表的GAFA版70页PDF，DOI
10.1007/s00039-026-00746-0；主线程初核期刊HTML主条款，尚未逐条比较PDF或认证全证。
上面的独立复核仍针对arXiv v2，范围不自动扩展。

原件、下载直链、SHA、字节数和取得时间均已加入[文献索引](../../literature/README.md)及manifest。
网页摘要不覆盖PDF的范围和日期事实。

## 1. 两个Kloosterman界的规范不能混用

Pascadi用未归一化
S(m,n;c)=sum_{x mod c,(x,c)=1}exp(2pi i(mx+n xbar)/c)。
Theorem1.1的系数支撑为初始区间[1,M],[1,N]，
在M,N<<c^(1/2+o(1))、a为单位、(m,n,c)=1时给
sum alpha_m beta_n S(am,n;c)<<||alpha||2||beta||2 c^(1-1/700+o(1))。
另一条|alpha|<=1结论在(n,c)=1时给sqrt(M)||beta||2 c^(1-1/276+o(1))；
不能把sqrt(M)自由换成||alpha||2。
Theorem1.2允许任意整数区间，长度至多c^(1/2+o(1))，
含模数分解c=dd'e、d'|d、(d,e)=1，f=max{r:r²|cd}；
界为||alpha||2||beta||2 c^(1+o(1))(f/min(c,d²))^(1/6)。
若c/d平方自由则f=d。Example1.3的p²或平衡pq给c^(11/12+o)乘系数范数。
这里c^-1/12是相对norm乘c的节省；只有M,N约sqrt(c)时，
它才也是相对组合平凡界norm乘sqrt(MNc)的节省。
短长度相对因子为c^(5/12)/sqrt(MN)，不能统一声称1/12。
Thm7.1的较宽平衡长度[c^(5/12+epsilon),c^(5/8-epsilon)]另依赖三项式；
Thm7.8仍是初始区间，不是平移版本。

MQW用Kl2(a;q)=q^-1/2 S(a,1;q)。Theorem1.1使用初始区间[1,M],[1,N]
上的任意复系数，没有gcd(mn,q)或gcd(m,n,q)限制。在
1<=M<=N q^1/4、M^(7/5)N<q^3/2、MN<=q^5/4，以及(c,q)=1时给
\[
 \left|\sum_{m\le M,n\le N}\alpha_m\beta_n
             {\rm Kl}_2(cmn;q)\right|
 \ll q^\epsilon\|\alpha\|_2\|\beta\|_2(MN)^{1/2}
 \{M^{-1/2}q^{1/6}+M^{-3/25}N^{-3/10}q^{1/5}
                         +(MN)^{-3/16}q^{11/64}\}.
\]
在M=N=q^1/2，括号三项幂为-1/12、-1/100、-1/64，
故最弱节省为q^-1/100（另留epsilon）。
这与Pascadi特殊模数的更强节省不矛盾。
常数依epsilon，其余参数统一。平移短区间零延拓必须用其右端点，
不能直接以长度替代M,N；第4页Thm2.1的dyadic版本还有另列s|q条件。
两种核在(a,q)=1、(m,n,q)=1时可由局部单位替换和CRT接合：
S(am,n;q)=S(amn,1;q)=sqrt(q)Kl2(amn;q)。
这里m,n不必各自都为单位；但不能删除联合互素条件，
例如S(2,2;4)=2，S(4,1;4)=0。
这里使用arXiv原始声明作为[R]候选，未称已独立认证全部解析证明。

## 2. 素数多项式的L1均值不是四阶中心响应

Choi–Kumchev Theorem1.1控制字符族上的
sum_chi integral_-T^T |sum_{N<n<=2N}Lambda(n)chi(n)n^-it|dt，
上界为(N+H N^(11/20))log^C(HN)，H=m r^-1 Q² T，C为绝对常数。
准确参数为m,r>=1、Q>=r、T,N>=2；
chi=xi psi mod mq，xi为mod m任意字符，psi为mod q本原字符，
r<=q<=Q、r|q、(q,m)=1。这是未除以字符数或时间长度的总和。
C可取1100，权是Lambda而非任意系数。
它是L1平均；不能直接称为带六窗、去对角的四素数中心相关。
第一页和Remark2清楚区分无条件定理与GRH改良。
GRH界NL+H N^.5 L²（L=log(HN)）中的NL仅在主字符出现时需要；
不能因此从无条件定理删除N项。
本来源只进入背景，不直接恢复241已停止的MOM坐标路线。

## 3. 实际映射必须先证明

现有240–241要求同一determinant/frequency fiber内先合并物理方向，
实际包含ad-bc、四个von Mangoldt权、共同六窗、精确Gabor乘子及共同中心项。
上述外部定理有独立算术内容，因此可以进入下一有限准入核查；
但目前没有把这个实际和写成满足其范围的Kloosterman双线性式。

特别地，“b,d是素数，所以取q=bd并用c^-1/12”尚不是论证。
固定互素b,d时，ad-bc=h只先给a≡h dbar (mod b)及c=(ad-h)/b；
这一步本身不产生完整Kloosterman和，不把素数权变成可自由Poisson求和的平滑权。
Vaughan分解还必须保留所有通道和ghost项的共同物理方向。

下一有限任务若被正式采用，至少需：

1. 固定一个实际factor/aperture区间，给determinant和的精确变换及所有互素分层。
2. 确认变换所得是否真有S或Kl2核，写明每个模数、长度及alpha/beta范数。
3. 保留所有变换尾项、零频率、对角和连续中心项，比较最终误差与所需o(log^4 X)。
4. 若只有自由系数范数或不匹配长度，按确切失配停止；不凭外部小幂节省宣布四矩完成。

这条候选与“重新命名Möbius矩阵预算”不同；是否能接入实际问题仍待证明。
332–334已结算；当前唯一数学主周期为周期8的实际determinant映射。
336给完整有限域核的精确候选公式，337处理该固定扩展的零频项；
系数与长度是否满足这里任一双线性定理仍是未证的下一接口。
