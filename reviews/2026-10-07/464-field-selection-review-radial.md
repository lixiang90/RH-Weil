# 464 辅助数域选择与共轭障碍的独立全文审查

2026-10-07。radial_review。结论：限定 PASS。
独立全文读取464，并重新核对457、458、460、既存定量审查及固定 math
关键原定义、Gauss identities、反射、二次大筛、实际 \(ua^6\) 放大。
两个新增有限代数结论均成立；没有得到新域的 raw 合同或无零边界。
本次只新增本审查文件，不修改464、旧稿、math、脚本或 Git。

## 1. 证据对象与引用范围

[464](../../notes/464-field-selection-decision-and-conjugation-obstruction.md)
最终 canonical LF SHA-256：
c534076d26fbc9612ea67946b9ab8e247bd8b13acb2d4415ba60b52501f3ae2d。
CRLF及 lone CR 统一成 LF 后计算：9100 UTF-8 bytes，181行。

依赖的既定 canonical hashes：

| 输入 | SHA-256 |
| --- | --- |
| 457 | 75079970955602644a9290709f66e2be331ad6116d2a637ed8fc97fb0dde5791 |
| 458 | 3ee821601d6e1d5da38c8235586981b28d7ebee5a5f28691a98d869834dcc8ac |
| 460 | 9625c0d618854769de90edfb3ee3b8d8b89e1d3b2b83d676dffccb927e09d85f |
| 451 | 17ce7fea8c881ebd4034657b7039e99897d4ff9532348993ba329c46e3c4d487 |
| 固定 math source | 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 |

固定 math 是 September-30-2026 build/paper.tex、commit adc7f124。
本次直接核568–625、705–726、766–835、1425–1453、
1789–1793、2640–2672、7697–7702、12362–12416行。
底层 [R] 整篇分析不是本次重证对象，也没有把原 [R] 自动迁移给 Gaussian。

## 2. 原机制、single-shift 最小值与数域次数

§1 的分工准确：primary normalization及有限单位负责实际 arithmetic
indexing；cubic prime identity及其 squarefree CRT给目标 phase；
ordinary completed branch把 actual residual \(j=1\) 送到 quadratic
\(\chi_6^{-3}\)，才能在合法 conductor/reciprocity sectors中使用线性大筛。
源1789–1793还含其它特殊分支，464没有声称所有 \(j\) 都降成二次。
源12362–12408的指数 \(1/6\) 来自 sixth-power averaging及 raw
row-scale supremum，不是除去六个单位造成的系数。

§2 限定条件是必要的：row阶 \(d=2m\)、retained \(j=1\)、
single shift \(\rho\)，且 shift本身来自 \(\chi^\rho\) 的 theta角色。
要使 \(\chi^{-1-\rho}\) 为唯一 order2幂 \(\chi^m\)，准确有
\(\rho\equiv m-1\pmod{2m}\)。又
\[
 \gcd(2m,m-1)=\gcd(2,m-1),
\]
所以 \(m\) 为奇时 theta阶是 \(m\)，偶时是 \(2m\)。
在 \(m\ge2\) 中，偶数给至少4，奇数给至少3；
等号3只能是 \(m=3,d=6\)。\(m=1,d=2\) 给平凡角色，被明确排除。
这是真正全整数论证，不依赖有限枚举；它没有排除改变 retained row、
多重 shift或其它 probe设计。

在所声明的 Kummer构造需要 \(\mu_d\subset K\) 时，
\(\mathbb Q(\zeta_d)\subset K\) 及
\([K:\mathbb Q]\ge\varphi(d)\) 成立。Degree2只允许
\(\varphi(d)\le2\)，即 \(d=1,2,3,4,6\)；对 even row阶留下2、4、6。
其中 \(\mathbb Q(\zeta_6)=\mathbb Q(\sqrt{-3})\)，
\(\mathbb Q(\zeta_4)=\mathbb Q(i)\)，故464的虚二次分类准确。
其它虚二次域上的高阶有限 Hecke characters并未被这条包含关系排除。

固定域的判别式、有限类数及 lattice covolume只改变常数与有限数据，
不能单独改善 fixed-field ideal counting 的一次幂。
非PID仍须重建 primary/representative乘法与 conductor接口；
这不是把有限类群步骤免费删除。域随主参数增长时也不再是固定常数。

## 3. Gaussian signal与定量条件的独立复算

重新查阅
[DDHL v5](https://arxiv.org/html/2306.11875v5) 的 §3、§4.5及Lemma9.2。
应采用2026-01-30的v5含 supplement的 (3.11)。
457已正确区分 Jacobi signal与Gauss平方，并处理split、inert及
coprime-primary CRT，squarefree \(\gamma_1(c)^2=\mu(c)\alpha(c)\) 在其
additive/residue convention内成立。464没有将它冒充新的线性 theta
coefficient完成；quartic prime-core coefficient仍未全部确定的文献范围
也准确。已证 square-numerator Voronoi不是任意原 \(\eta\)、moving row
和 all masks的统一 completed reflection。

本次从451指定的代数根重新算显示值：
\[
 e_*=0.16683858898627088215\ldots,\qquad
 t_*=(1+3e_*)/(8e_*)=1.12422714678608452984\ldots .
\]
代数根及其有理隔离是既存451证据；本次高精度算术只检查464的显示数值，
不重新用浮点代替连续证书。逐项一致：

| 数值 | 独立复算 |
| --- | --- |
| \(e_6(t_*)\) | 1.10352262232173710820… |
| \(e_4(t_*)\) | 1.09317036008956339738… |
| \(e_6-e_4\) | 0.01035226223217371082… |
| \(e_6-e_2\) | 0.04140904892869484328… |
| 条件 cutoff重平衡 count收益 | 0.00299361956172998467… |
| 458全行 LS exponent | 1.45756048011941786317… |
| LS exponent减原 \(e_6\) | 0.35403785779768075497… |

重平衡数值另从实际显示函数
\(s=\delta P/D\)、
\(R_\alpha=1-\delta+(\alpha-\delta)s/[2(\alpha-\delta+s)]\)
独立计算，\(\alpha_6=5/6,\alpha_4=3/4\)。
在旧 cutoff仍有 short exponent \(2/3\)，故只降 long分支总count收益为零。
只有额外保留整套 short合同并合法重选 cutoff，才能得到表中反事实值；
464明确引用这些额外前件，没有登记Gaussian count theorem或新 \(\sigma\)。

458的实际全行界和fixed-profile scale-sup范围保持不变。
[BGL Theorem1.3](https://arxiv.org/html/1112.1650v1) 的 squarefree
高阶宽度含 \((UD)^{2/3}\)，不是特殊 Möbius全行线性合同。
460的幂次行下界属于任意 unit-energy列的 operator norm；
464没有将它当成原固定 \(\mu\eta W\) 的反例。

## 4. 原方向 quartic 行的有限共轭反例

取 \(\pi=-1+2i,\nu=3+2i,\bar\nu=3-2i\)。
Norms为5、13、13，因这些是 rational primes，三个元分别生成素理想。
Primary条件可直接核：
\[
 (\pi-1)/(-2+2i)=1,\quad
 (\nu-1)/(-2+2i)=-i,\quad
 (\bar\nu-1)/(-2+2i)=-1 .
\]
这里 \(-2+2i=\lambda^3\)。它们都是odd primary；
分母norm13与numeratornorm5互素，在§4的 \(\eta=1\) 及odd约定下
所有相关 natural masks确为1。

模 \(\nu\) 的 residue field识别使 \(i=-3/2=5\bmod13\)：
\(\pi=9\)，\(9^3=1\bmod13\)，故 \((\pi/\nu)_4=1\)。
模 \(\bar\nu\) 使 \(i=3/2=8\bmod13\)：
\(\pi=2\)，\(2^3=8=i\bmod13\)，故 \((\pi/\bar\nu)_4=i\)。
本次以整数 modular power独立算这两项，没有使用待证角色值产生结果。
共轭 convention给 \(1,-i\)，仍不相同。

真实row正是458的 \(\psi_\pi(n)=(\pi/n)_4\)，不是偷偷换成
\((n/\pi)_4\) 后忽略 reciprocal supplementary factor。
任意 norm pullback \(\chi\circ N\) 在这两个good ideal上值必相等；
finite Euler删除不会改变这些good值。因而该row并非norm base-change，
primitive inducing character也不能由这种有限删除免费取得它的全局无零条带。
更强的有限检查是 \(\nu-\bar\nu=4i\)，两个分母属于同一个基本mod4 sector。

当然可按包含row导子的更细有限ray群分拆一个固定角色的系数。
那只把同一全局角色写成局部数据或partial sums，不会使其普通
Hecke L函数变成一个Dirichlet norm-base-change L函数；
moving \(\pi\) 的导子也不能被固定2-part sectors免费吸收。
464对此作的是“不自动获得前件”的判断，没有声称任何sector方法不可能。
单支split conductor不共轭不变与上述好理想值测试相符。

第四幂子族报告仍合法：\(\chi_n(r^4)=1_{(n,r)=1}\)，
只控制明列固定目标及其 reciprocal前件，没有覆盖此变化primitive quartic族。

## 5. 更宽候选、普通完成与最窄待付项

对finite-order CM characters，complex infinite type平凡，
degree \(2r\) 的 ordinary completion含 \(\Gamma(s)^r\)。
Conductor反射指数仍为 \(1/2-s\)，次数增加的是gamma个数与height成本。
这与
[GL (3.1)–(3.2)](https://arxiv.org/html/1112.1642v2) 及
[Watkins §3.6](https://magma.maths.usyd.edu.au/~watkins/papers/hecke.pdf)
一致。实二次还需 real sign/parity gamma和无限单位；
高CM unit rank \(r-1\)，未经商去units的norm-bounded element rows确实无限。
Ideal counting仍linear并不自动支付代表、profile及多place预算。

§5 的候选表和“不是不可能性结论”范围准确。
最窄下一输入是同一目标、同一Gaussian row族、保留全部natural zeros、
fixed profile及height范围的 special Möbius近线性 all-row scale-sup。
普通任意列大筛不能给每个 \(c>0\) 的 \(H\ge D^{1+c}\) 合同，
必须证明实际特殊系数的cancellation或等价primitive联合能量。
它本身也还没有支付 completed reflection、once-prime slots、
marked/plain、same normalizer及whole-family continuation。

限定PASS覆盖464的两个新有限代数判断、定量显示、原机制归属与全部scope。
项目既有 [R] 下的 \(\sigma_*=0.874957019420098946\ldots\) 未变；
没有新Gaussian/实二次/高CM无零定理、RH/RR或比例提升登记。

## 6. 新精确审计脚本的方法范围

只读核查
[hybrid_field_decision_exact_audit.py](../../scripts/hybrid_field_decision_exact_audit.py)
全文。其 canonical LF SHA-256：
36da2a5b99a8d7864d4c285d4fdfd05ff5fe92efe822bf1c537308ca21ff105b；
6481 UTF-8 bytes，157行。方法限定PASS，本次没有运行
\(\mathrm{build}()\)、检查点程序或写入审计JSON。

quartic函数直接识别两个norm13 residue fields中的 \(i\)，由
\(\pi^{(13-1)/4}\) 计算角色值，随后识别四个根；没有把笔记的
结论用作输入。Primary及good条件的整数断言与§4计算一致。
50个even \(d\le100\) 的 single-shift样本准确检验阶数公式，
但全 \(m\) 的唯一性仍由§2的gcd证明支付。

根的两端有理符号、150次二分、所有预算用Fraction运算；
\(e_6-e_4=(t-1)/12\) 和 \(e_6-e_2=(t-1)/3\) 是精确断言。
脚本在有理中点检查 \(e_6=2/3+\delta t\) 的误差小于
\(10^{-50}\)，这是近似根上的有限一致性检查，不能替代451的
代数根隔离与连续证书。60位Decimal仅显示数值，输出也明确标为
非analytic bound。458包络中最大项 \(t+1/3\) 的选择核查正确。

build函数先以 -B 和 --check 调用既存checkpoint，核验已保存
source、旧论文及证据绑定；此调用不重新生成旧输出。
新JSON记录输入、新笔记、两份审查及脚本的canonical hashes，
并核查审查包含最终464 hash、控制字符和本地链接。
正常模式只写新审计JSON，--check模式只作比较。
这些metadata检查证明文件绑定与有限运算的一致性，不能证明底层
[R]、所有Gaussian Gauss phases、角色族的统一反射、实际特殊
Möbius cancellation或新的marked/plain合同。脚本的
not_certified与464及本审查的限定范围相符。

末次只读复核确认exact_conjugation_example的三个元及两个角色值
由tuple显式转成list，使内存结果与JSON读回数组一致。
此序列化修复不改变任何数学计算、有限断言或464正文。
