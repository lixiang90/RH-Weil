# 固定零点包与 signed Gram：不同作者全文审查

2026-10-08，checkpoint_audit。只新增本审查，不修改研究源、冻结输入或Git。
结论：下述限定解析与恒等式范围 PASS；没有新的 whole 第四矩增长界。

## 1. 全文读取与固定身份

主源 [453行研究](hybrid-original-squarefree-signed-zero-gram-research-perron.md)
已独立 FULL READ 全部453行，18782 canonical UTF-8 LF bytes，SHA256
0b126138c7bf42e9be3c4352b099a6ab37d88cef93af20593593c8e849aa2a17。
本轮还全文重读419、490、475完整源332行、476完整源184行；
395和476笔记沿连续独审的既有 FULL READ 使用。六个输入均重新核hash：

| 输入 | canonical LF SHA256 |
| --- | --- |
| [395 Euler/Perron源](hybrid-original-squarefree-core-euler-perron-research-perron.md) | 2f25a678b0c38c95a40469c41a757506c6f1fe64343bed327c7effe298e980c0 |
| [419带权前缀源](hybrid-original-weighted-mobius-squarefree-perron-research-high-product.md) | 426e0e72e9234e6a9eccbe9a82e3055e7bbbc1669956ae78b9c4a6f82e9799b6 |
| [490配置](../../notes/490-original-weighted-mobius-squarefree-conditional-remainder.md) | a5bf40493c864774da5f8fbecce8d257bc21176a78b16ff1841c89843d4924ef |
| [475零点包源](hybrid-positive-height-zero-packet-fourth-upper-research-radial.md) | 8bcbd27da46d922d9e6e741fcf9a87012d565052f8d97b3ad12e99b3edbc2481 |
| [476密度迁移源](hybrid-ivic-density-and-scalar-fourth-growth-research-twisted.md) | a21a19e7bd09892ed705fa7883143e49c138ffe112c561be9413edaf44d72a1d |
| [476笔记](../../notes/476-original-fourth-growth-five-sevenths-with-ivic-density.md) | 179829dd25f92ff187359f73455aafad9f957d714df13cf871db47a76e9408b6 |

另直接读取 [Fesenko–Ricotta–Suzuki原论文](https://www.numdam.org/article/AIF_2012__62_5_1819_0.pdf)
Appendix A，印刷1880–1883页：Proposition A.1完整假设、结论及证明，
和(A.6)从圆盘零点和改成ordinate窗口的说明。
消费的是普通ζ的局部零点计数及log derivative公式，不使用mean-periodicity结论。
本文不重认证476所引全部密度文献或451旧覆盖。

## 2. 实际算术身份和全纯修正

源(3)的符号独立展开为
−(−ζ′/ζ−D)(ζC−1)=Cζ′+DζC−D−ζ′/ζ。
在初线逐系数得到R=L+A，保留p|k、原b_V、k>V、p>U、共同Y<pk≤X。
没有把真实函数改成独立矩形；D的全部proper powers与p≤U有限prime项不双扣。

G=Cζ′+DζC−D在Re w>1/2、非零高度解析；局部1+p^(−w)
在该域不为零，1/ζ(2w)和proper-power级数绝对合法。
全部普通ζ零点留数仍来自−ζ′/ζ，为−m_ρ，没有V减幅。

419的r=1带权prefix和实际prime prefix在共享左线给C、D各V^α。
G最贵DζC为V^(2α)，结合既有ζ4均值、共同核Minkowski得
第四矩指数8αv；先分配δ、ρ及日志损失，恰回到4(2θ−1)v=c_θ。
ζ′C和−D费用更小。外水平边界仍用395无条件界；
初线无限远尾用τ(n)log(2n)n^(−1−c)的收敛级数，不能用n^ε替换。
因此源(5)是原条件误差费用的合法解释，未产生新的saving。

## 3. 固定有限零点集与完整移线

x=floor X+1/2、z0=floor Y+1/2精确保留整数窗口。
F=(x^z−z0^z)/z=∫exp(zu)du entire，F(0)=log(x/z0)。
不能拆开单端核后漏掉核原点，或删掉恰在z=0的真实零点留数。

局部重数计数O(L)给候选height区间内O(TL)个ordinate。
删半径c0/L的小邻域后，可一次固定h0∈[T/32,T/16]、h1∈[5T,6T]。
所有t∈[T/4,4T]的相对上下截断为t−h1、t−h0，分别≤−T和≥3T/16。
两截断端均为T量级，可分别对振荡尾分部积分。

初线Re w=1+c的无限远系数和为−ζ′/ζ(1+c)=O(L)；
半整数近端harmonic和给O(X^(−1/2)L²)，完整n>X远尾已计。
左移到Re w=−1；两横边的绝对height始终−h1、−h0。
避零距与局部公式给D=O(L²)，横边核O(√X/T)，费用O(X^(−1/2)L²)。
左边functional equation给D=O(L)，核绝对积分给O(Y^(−3/2)L²)。
归一化N_L≥c_φL只会降低这些粗界。

矩形全在负height、T量级：pole1和trivial zeros均不在其中。
所跨普通零点集合h0<γ<h1、ρ=β−iγ严格独立于t，重数保留。
故源(10)–(11)成立，没有row-dependent零点扩充后的signed尾偷换。

## 4. Gram、二阶付款与真正未付四阶

有限包允许直接换和与积分。K_J和pair-index H_J都是Hermitian PSD Gram，
这只控制完整二次型，不保证单个交叉项非负，也不允许删某个β子包。
独立对正实部单端核分式分解得到源(14)；完整实轴核为
2π/(a+b−iΔ)，乘实际载波相位后实部含(a+b)cos(Δlogx)+Δsin(Δlogx)。
源给的跨J两端位置例子确使未乘相位核实部为负；没有声称存在相应ζ零点。
临界线a=0时始终用合并entire核；原双端四组Gram均保留。

长度X≍T有限polynomial直接积分和harmonic差分给M2≤LΣ|q_n|²。
Λ≤L及N_L≥c_φL给L窗口M2≪L²，r_T为负幂，故实际全零包M2≪L²。
真实R系数满足|r_n|≪τ(n)/√n，τ²≤τ4给M2_R≪L⁵。
这些是无条件二阶估计，不是各零点实部子包的范数上界。

固定a≥η且γ在J内部，x^a端统一压过z0^a端，
单零点M2和M4尺度分别x^(2a)/T、x^(4a)/T。
结合既有476固定网格密度输入，顶端σ=7/8、n_I=3/14的费用
确为−1/28与5/7。它们是密度upper的费用，不能视为实际零点饱和。
因此二阶polylog或理想二阶近正交均不自动消除第四阶自对角费用。

源(25)保留全部signed四零点，pairing diagonal非负；
其它项合计可有负相消，尚未证明其抵消或更强实际密度。
源(27)仅是取得完整新零点四阶目标后的条件推论，原c_θ修正仍需支付。
完整实轴Plancherel的2π convolution范数只是原J的正上界。

真实R²系数g_ℓ及原J积分的Φ_T相位、15/4长度因子均正确。
|g_ℓ|≤Cτ4(ℓ)/√ℓ、τ4²≤τ16给乘积算术diagonal≪L¹⁶。
全部非对角signed移位相关、远h与近h仍未付；不能从P_H far界限制子族。
补除数公式中e<k/V是严格端点；semiprime和prime-square例子保留p|k。

限定PASS覆盖实际身份、固定有限零点包、完整截断费用、Gram接口、
二阶与算术diagonal付款及明确的未付目标。没有认领(25)/(31)新四阶上界，
没有新whole幂、中心常数预算、比例、κ或无零边界。
本审查没有数值零点采样或finite checker；哈希只固定审查对象，不能认证无限解析。
