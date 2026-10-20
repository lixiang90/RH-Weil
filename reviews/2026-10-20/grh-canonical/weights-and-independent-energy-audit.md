# 分次权的可识别性与独立能量输入：同一计数数据的反测试

2026-10-20，565独立原稿。已恢复README／STATE／check/show、Goal、frontier、C027、最新策略；
核读001、002、290、307、563、564及其有限域原稿。只写本文件，不改公共状态、cadence或Git。
固定G20261014／0c4f≤538；本稿不是经典RH或一般数域正极化的证明。

## 1. 首先分开三种可识别性

裸positive primitive P给全部repeat powers Π及M=exp_*Π；在收敛半平面内它确定Z。
在已证明延拓的共同域，解析延拓也唯一。但这不同时确定：

1. 允许乘什么Mellin核G来定义完成对象；564的同一整数Gaussian正核反例已严格否定此项。
2. 用哪些分次空间和F_j实现同一superdeterminant；净零极点只看交错重数。
3. 指定原F_j的Jordan结构、正内积与相容极化；普通迹和行列式看不到Jordan块。

因此，应把“补充一种规范使问题有确定对象”与“从这个对象推出纯性”分开核验。
这不否定在已知标准Gamma／数域类内由同一Dirichlet级数推出完成化唯一性；
同轮完成化来源审查另核该类唯一性。不能据本稿泛称同一数域ideal-norm ζ有任意signature自由。
这里缺少的是一般g-distribution自动属于该类的存在性，以及几何grading／正能量来源。
原始对偶的总反射权w只给两伙伴的权之和。它没有一般规则把多权对象分成各个次数。
若输入已经声明“单一非空自对偶分量”，则a=w/2无需看零点即可固定；
这个单权声明不能由整个多权对象的函数方程免费得出。

## 2. 完整点数和positive Euler也看不到相邻次数的虚消包

以下是精确有限反测试，不使用任何未知零点。先取真实P²/F_q，q>1为素数幂。
其计数N_n=1+q^n+q^{2n}、positive closed-point Euler及

\[
 Z(T)=\frac1{(1-T)(1-qT)(1-q^2T)}
\]

都固定。通常分次实现为H⁰,H²,H⁴各一维，F分别为1,q,q²。
任取λ∈C×，另加如下分次向量空间及作用：

\[
 K^1=C_\lambda,\quad K^2=C_\lambda\oplus C_{q^2/\lambda},
 \quad K^3=C_{q^2/\lambda}.                              \tag{1}
\]

这里C_r表示一维空间上F乘r。给K¹×K³标准非退化配对；K²上给
矩阵[[0,1],[1,0]]的双线性型。每个互补次数的配对都精确满足
B(Fv,Fz)=q²B(v,z)。奇次数反向配对取负号，与分次符号相容。
然而所有n≥1都有

\[
 \sum_j(-1)^j\operatorname{Tr}(F^n|K^j)=0,\qquad
 \prod_j\det(1-TF|K^j)^{(-1)^{j+1}}=1.                  \tag{2}
\]

故把K加在原实现上，不改变一个点数、不改变一个Euler系数、不改变完整Z或其FE，
却改变Betti数、分次谱与可否在所宣称权上纯。λ可任意，原计数数据完全看不到它。
这也说明：“净zeta已无额外B因子”尚不足以排除谱实现中的隐藏相消。

范围限制必须保留：(1)是抽象分次／对偶实现，不声称来自P²的实际几何上同调，
不声称有杯积代数或Hard Lefschetz。若额外给出标准上同调函子或严格的最小性，
可能排掉该包；这些是新增结构输入，不是(2)中的计数信息。
Milne的[étale讲义§25–29](https://www.jmilne.org/math/CourseNotes/LEC.pdf)先给独立定义的H^j，
再以Lefschetz迹公式得到Z的交错行列式；这条方向不应反写成Z自动恢复全部H^j。

即使另付minimal determinant维数，Jordan仍不可识别。令

\[
 F_0=rI_2,\qquad F_J=r\begin{pmatrix}1&1\\0&1\end{pmatrix},\quad r>0.
\]

两者所有正负幂迹均为2r^n、行列式同为(1-rT)²，普通trace维数同为2。
二者都有模r的纯谱；但F_J不可能满足F_J*HF_J=r²H、H>0：
否则U=F_J/r酉，所有U^n范数有界，与非零Jordan块线性增长矛盾。
所以“纯性”比“指定原作用的正极化／半单”弱。选择cyclic companion也不是无害的唯一性规范：
它在重根处可能恰好选择Jordan作用，不能用来免费保证正极化。

## 3. 独立权数据在真正函数域中来自哪里

光滑射影V/F_q的degree j在构造上同调时已给出；Tate twist及
F L=qLF规定次数变化的缩放。这些不依赖先查看复零点。
Poincaré对偶给j与2d−j的总缩放q^d；欲证的纯性仍是|α|=q^{j/2}。
按实际零点模把因子分为q^{j/2}各组，只有在纯性已付后才是合法恢复方法，不能拿它证明纯性。
标准有理性／FE与纯性是不同输入；[Milne Theorem5.1及§5](https://jmilne.org/math/xnotes/pRH.pdf)
明确把一般纯性作为定理证明，而非仅由对偶搬运得到。

几何次数可先于零点给正性。椭圆曲线上deg(m−nπ)是实际映射的非负次数，
为二次型m²−tmn+qn²；因此t²≤4q。这是独立几何不等式，
不是“所有复根模sqrt(q)”的改写式被当成公理；二次型非负须由映射／有效性证明。
本仓307已为y²=x³−x/F5完整重建此机制，不重复登记新定理。

565应消费的去重结论是：裸分布到degree或正极化之间仍需函子／映射／能量的独立来源。
001已经证明PLF正性到纯权；290更强地给了positive integer closed points、精确FE、
分次外代数、Poincaré对偶及代数Hard Lefschetz同时成立的离线模型。
因此给候选包加上“对偶／分次／Lefschetz”几个名称，仍不足以代替正极化。

## 4. finite energy是可执行证书；其存在性本身不是自动新输入

对曲线型二次多项式P(T)=1−tT+qT²，从全部点数递推直接给

\[
 A=\begin{pmatrix}0&-q\\1&t\end{pmatrix},\quad
 H=\begin{pmatrix}1&t/2\\t/2&q\end{pmatrix},\quad
 A^THA=qH,\quad\det H=q-t²/4.                           \tag{3}
\]

矩阵恒等式无需算根；H>0恰在|t|<2sqrt(q)。563的F5曲线y²=x³+x+1给t=−3，
detH=11/4>0；完整有理性／FE给全部递推，遂给全部周期Weil平方和。
290取t=q、q≥5时，同一形式的detH=q−q²/4<0，正Euler及代数对偶并不修复它。
这是两个源侧精确测试，不能把“总存在某个正H”当成一般正分布的已证事实。
边界|t|=2sqrt(q)时，半正H的商会丢普通迹重数；原companion还可能有Jordan块。
已知P=(1∓sqrt(q)T)²可以另造±sqrt(q)I₂的trace实现，但它不等于证明指定原作用酉化。
严格正H与此二阶源的strict Hasse不等式等强，不能宣称它是逻辑上比该有限域RH更弱的新前件。
严格H失败于边界也不等于RH失败：边界的行列式仍纯，而指定companion不半单。
连续族c=1/4同样有C=[[0,1],[0,0]]、G=diag(0,1)，G商仅一维而源为常数2；
它给正型但不自动给二重零点的ordinary trace。另选零生成元于C²可保trace2，
仍须与原作用分账。F5严格H、有限精确点数和全递推构成已知实例的认证，
没有从一个N1计算普遍推得所有曲线Hasse界。

对于有限输入，若H和全递推由精确算术独立给出，检查主子式、(3)和全源身份
的确是不先读零点的证书；与结论有逻辑等价关系不使这种具体证明自动循环。
循环发生在“由于应该RH，故断言存在H”或先从未知居中本征基定义H，随后再称证明RH。
这一区别已在001/002/563支付，本稿仅固定565的消费规则。

## 5. 双向收缩和Markov详细平衡：一个准确可行的蕴含及其过强版本

设预定中心a_j、已知正Hilbert范数和实际对偶识别把U₂对应到(U₁*)⁻¹。
若能从输入独立证明||U₁||≤1、||U₂||≤1，则||U₁⁻¹||≤1，故

\[
 ||U₁v||\le||v||=||U₁^{-1}U₁v||\le||U₁v||.
\]

于是U₁酉，给纯性和原作用半单。有限矩阵可核两条LMI；强连续双向群版本
还须全部t及共同合法域。073早已有更弱的双向subexponential增长推出纯性、
一致有界平均重建极化；因此本蕴含不登记为新机制。
关键未付项是：分布怎样独立产生同一个正范数，且dual真是该范数中的adjoint inverse。

单向Markov详细平衡不够。若P是行随机矩阵，π>0平稳，Jensen给
Σπ_i|(Pf)_i|²≤Σπ_i|f_i|²；详细平衡另给P自伴。
例如P=[[3/4,1/4],[1/4,3/4]]是正、可逆、详细平衡的Markov矩阵，
却有1、1/2两个特征值，归一化F=q^aP不纯。精确双线性dual可形式定义为
q^{w-a}(P^t)⁻¹，但它没有第二个收缩界。
此例只反驳算子条件本身，不冒称已构造相同条件的全部positive g-integer系统。

更强的“P和P⁻¹都逐项非负且行随机”反而过窄。由(PP⁻¹)_{ij}=0(i≠j)，
若P_{ik}>0，则P⁻¹的第k行仅能在第i列支撑。两行P若共用同一正支撑会迫使该行全零，
与可逆矛盾；n个非空互不交支撑分配n列，所以每行恰一个正项，行和1迫使P为permutation。
其特征值全是单位根，迹为整数。这一版本甚至不能包含563的F5正例：
归一化U=A/sqrt(5)的迹=−3/sqrt(5)非整数，不可能与有限permutation相似。
因此有限Markov的双向可逆保正不能充当覆盖一般函数域的自然极化机制。
允许unitary而不要求逐项保正、允许无限空间或只用正时间heat semigroup，是合法逃逸。

## 6. 一种真正可用但尚待算术身份的分析证书：正闭形式的heat trace

应区分两类semigroup：选择archimedean Gaussian核的物理空间扩散，
与完整Weil分布的谱heat trace。前者即使规范唯一，也没有自动证明后者。

给一个在不读取零点情况下由P／dual及已固定背景构造的正稠密闭形式\(\mathfrak e\)，
其表示算子K≥0自伴。若对每个t>0，e⁻ᵗᴷ普通trace-class，并能独立证明**同一完整源**

\[
 \Theta_W(t)=W(k_t)=\operatorname{Tr}(e^{-tK})\quad(t>0),\tag{4}
\]

则Θ完全单调。确实λ^n e⁻ᵗλ≤C_{n,t}e⁻ᵗλ/²，trace-class保证逐阶微分合法，
于是(−1)^nΘ^(n)=Tr(K^n e⁻ᵗᴷ)≥0。
若W是563规定的实偶、有限指数阶完整分布，563热定理随即给全部complex compact Weil正性。
适用其entire／零带／完整除子前件时，再推出预定权上的RH纯性。

正闭形式可用显式非负跳跃项和killing项认证，例如

\[
 \mathfrak e[f]=\frac12\iint|f(x)-f(y)|²J(dx,dy)+\int|f|²V,d\mu,
 \quad J\ge0\text{ 对称},\quad V\ge0,                  \tag{5}
\]

但必须另证稠密性／闭性或closability及所取闭包；形式表达本身不付这些域责任。
若具Dirichlet截断性质，则关联semigroup为symmetric sub-Markov；这项标准分析接口核
[Baudoin本人讲义](https://fabricebaudoin.blog/2019/02/11/lecture-5-dirichlet-forms/)。
推出CM只需K≥0和trace身份，Markov性是可核构造机制之一，不是必要条件。
保守Markov要求常数态不衰减，可能无端强迫零频谱；允许killing更自然。

连续Z_c正段直接以K=τ²I₂给Θ=2e⁻ᵗτ²，重数正确；负段Θ=2e^{r²t}递增，
不可能是任何K≥0的这种heat trace。混合连续谱可改用正state／半有限trace，
但ordinary determinant与分支边界须另外付，不能偷换(4)中的ordinary trace。

这里的独立输入必须是**具体闭形式及从同一源推得(4)**，不是泛称“存在某个K”。
若只从未知零点定义K并宣布(4)，那仍是RH等价包装。
经典ζ的Θ源式在563已含完整Γ、全部proper powers及双pole；
尚未得到由这些源独立构造的(5)及(4)。prime atoms带负号，不能逐项当J≥0；
Gamma Gaussian的Markov性也不能抹掉完整源中负算术贡献。

## 7. 数域与函数域检验给出的选择结果

| 候选输入 | 连续正反例 | 真函数域 | 数域／经典ζ | 本轮分类 |
|---|---|---|---|---|
| 正P／N、精确dual、有限缺陷 | 正反段均有 | 290同样有正Euler与代数HL而离线 | 已知数据不付全正性 | 旧严格不足 |
| 唯一核／完成规范 | 可固定各模型Gamma=0 | 几何类已固定背景和degree | archimedean local datum可固定常用Gamma | 对象责任，非正性来源 |
| 点数Z唯一推出grading | 对多权分解无一般唯一性 | (1)–(2)给净迹不可见包 | 同样不能从净divisor恢复Jordan／取消块 | 565具体可识别性反测试 |
| 全递推＋已算出H>0 | 563精确区分两段 | F5证书通过，290失败 | 无覆盖完整源的已给H | 有限真证书；存在性非免费 |
| 单Markov detailed balance | 单算子反测已失败 | 不给Frobenius模约束 | 不能由此宣称RH | 不足 |
| 有限P与P⁻¹都Markov | 只允许permutation型 | 排除已知F5正例 | 过窄，不能作一般要求 | 565准确适用边界 |
| 具体正闭形式＋同源全heat trace | 正段通过、负段不能 | 可在已纯／已证H后实现；不重计已知纯性 | (4)的独立算术推导仍未付 | 合法充分证书接口；非已得classic input |

最强旧净后果：001/002/073/307/563已经支付极化／双向增长／heat-CM到纯性的标准蕴含，
290已有positive Euler和HL不足；这些不重计。本稿新增可消费的信息仅是明确的
dual-compatible虚消包、Jordan不可识别测试及有限双向Markov排除真实F5正例的边界。
没有新增actualζ whole预算、成长K/core/coupling或faithfulΞ信息；542+555→557的4/5不变。
若下一轮只有未知H、未知heat identity或未知canonical grading改名，不能按新输入准入。
值得继续的具体证据是从实际分布／对偶构造可关闭的正形式，并独立支付同一完整源的(4)，
或给出一个严格更弱、仍排290并包含真实函数域且不靠已知零点的源侧不等式。
