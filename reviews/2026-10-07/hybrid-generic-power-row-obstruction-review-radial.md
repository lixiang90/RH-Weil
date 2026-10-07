# 460 独立审查：全行幂次障碍、数域成本和边界转换范围

2026-10-07。审查者 radial_review；全文只读逆审。

结论：**限定 PASS**。460 的一般任意列全行下界、必要指数阈值、
二次 Hecke-family 全行上界及其对换域的解释成立。没有发现阻断性错误。
这个结论不认证 Gaussian 特殊 Möbius raw 合同、不认证完整新域
marked/plain 递归，也不产生新的无零边界。

## 1. 精确绑定及实际审查范围

以下 SHA-256 均对 UTF-8 内容作 CRLF/lone CR→LF 规范化后计算；
没有改动被审笔记、旧审查、math 源码或 Git。

| 证据对象 | canonical LF SHA-256 |
|---|---|
| notes/460-generic-power-row-obstruction-and-field-choice.md | 9625c0d618854769de90edfb3ee3b8d8b89e1d3b2b83d676dffccb927e09d85f |
| notes/457-number-field-choice-and-relative-amplification.md | 75079970955602644a9290709f66e2be331ad6116d2a637ed8fc97fb0dde5791 |
| notes/458-gaussian-all-row-large-sieve-comparison.md | 3ee821601d6e1d5da38c8235586981b28d7ebee5a5f28691a98d869834dcc8ac |
| notes/451-kappa-feedback-cubic-boundary-and-family-continuation.md | 17ce7fea8c881ebd4034657b7039e99897d4ff9532348993ba329c46e3c4d487 |
| pinned math September-30-2026/build/paper.tex | 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 |

460 为 7,891 canonical bytes、195 个正文行。math 对象为
766,316 canonical bytes，固定提交
adc7f1241b42e322a6451854ab7e4b4c146bf78a，绝对位置
E:\codex-build\math\preprints\The-Quasi-Riemann-Hypothesis-September-30-2026\build\paper.tex。
下列源行号均指此对象。

完整读取 460、457 和 458；局部重读原 raw、amplification、
common-mask/slots 和 κ 前件，并核对二次大筛原始定理。
没有逐项重证原 math 全稿、metaplectic reflection 或其中引用的无限
分析定理；本次也没有运行或改写有限脚本。

## 2. 幂次重复行下界的完整准入

460(0) 已显式定义 B_d(U,D)：固定 good/ray conventions 后，
在 norm 至多 U 的全部允许行上，作用于 norm 位于 [D,2D] 的
squarefree good ideal 列、列能量为1的角色矩阵平方算子范数。
不是起始 d-free 行族，也不是特定 μ(n)η(n)W 列的二矩。
新增定义明确把列限制为 good squarefree ideals，与二次 upper bound
前件一致；最终 §2 的 prime columns、r 及计数集合也显式为 good，
避免把固定坏素数处的非允许行计入下界。这些澄清没有改变指数或证明。

Gaussian 情形的以下步骤均合法：

1. 奇 primary generator 对每个奇理想唯一；其乘法仍 primary。
   所以 r↦r^4 的单位歧义被消除：相等四次幂迫使 r 的比值为
   Gaussian unit，primary 条件随即迫使二者相等。
2. 奇 primary r、Nr≤R 的数量为线性数量级。删除固定有限坏素数
   或固定一个允许的有限 ray 子类只改变正的固定密度。
   这里取 R=U^{1/4}；仅这个子族已经给出 ≫R 个不同实际行。
3. norm 位于 [D,2D] 的 split prime ideals 有 ≍D/log D 个。
   固定模数素数定理已经足够：p≡1 mod4 各给两支 norm p 的
   Gaussian prime ideals。这一数量级直接由
   [Kedlaya Theorem 5](https://kskedlaya.org/18.785/dirichlet.pdf)
   的固定模数素数定理得到。inert prime ideals 的 norm p² 不减少这个下界。
   若还需有限 ray 分拆，取一个允许的正密度类即可。
4. Nr<D≤Nn 且 n 为 prime ideal，严格迫使 (n,r)=1。
   因而零延拓恒等式 χ_n(r^4)=1_{(n,r)=1} 在所选支持上实际等于1。
   并未把一般非互素 mask 删除。

取 a_n=P_D^{-1/2} 在这些 prime ideal 列上，列能量恰为1；
每个 u=r^4 行的内和等于 √P_D。全行平方和非负，因此只取该子族
便严格得到

\[
 B_4(U,D)\ge c\,U^{1/4}P_D
 \gg \frac{D U^{1/4}}{\log D},\qquad U^{1/4}<D .
\]

共轭 orientation 不改变此计算；完整四次幂也不产生单位补充律相位。
所以 460§2 没有漏掉 units、prime norm convention 或非互素零值。

一般 d 版本的范围也准确：必须已经有 ideal-indexed 角色、
χ_n(r^d)=1_{(n,r)=1}、全部理想幂行、理想幂注入和固定去坏素数后
线性计数。高次域不能未经单位商就用 norm-bounded elements 代替它。
在这些明确前件下完全相同的证明给出 D U^{1/d}/log D。

## 3. 必要阈值及二次上界

在 U=D^{1+c}、1+c<d 时，下界除以 U 的幂恰为

\[
 1+\frac{1+c}{d}-(1+c)
 =\frac{1-(d-1)c}{d}.
\]

若 c<1/(d−1)，选择
ε<[1−(d−1)c]/[d(2+c)] 后，它严格超过
(UD)^ε=D^{(2+c)ε}。对所有任意小 ε 的线性上界因此不成立。
故 460(8) 的必要阈值 d/(d−1) 正确；不是充分性声明，
也不是临界点消去 logarithm 后自动获得的定理。

二次上界 460(9) 有独立支付：
逐 prime valuation 唯一写 u=a r²，a squarefree、r 任意。
a 与 r 可相交；其真实角色仍满足
χ_n(u)=χ_n(a)1_{(n,r)=1}。固定 r 后，mask 进入同一列系数，
列能量不增；squarefree a 的长度为 U/(Nr)²。
[Goldmakher–Louvel Theorem 1.1](https://arxiv.org/html/1112.1642v2)
对满足其固定 reciprocity/primitive-family 前件的平方自由行、列
给出 U/(Nr)²+D。求和 Nr≤√U 时，
Σ_r(Nr)^{-2}<∞、#r=O(√U)，于是

\[
 B_2(U,D)\ll_{K,\varepsilon}
 (U+D\sqrt U)(UD)^\varepsilon .
\]

有限 ray sectors 仅增加固定因子。不能把任意元素符号自动读成该
ideal Hecke family；460 的“满足……前件”已经保留了这个限制。
二次下界 D√U/log D 与上界的指数阈值 D² 匹配。
四次下界仅迫使 U≥D^{4/3}；它没有填补 458 上界到 D² 才线性的
中间区间。460§3 对必要和充分的区分通过。

## 4. 原 source 为什么没有被这个反例否定

原 source 12343–12360 导出的 raw 界实际使用
μ(n)ν(n)W(q_n/D)，且来自其 marked lemma；
12355–12357 完整显示该固定逆列和每个固定 c>0 的 H≥D^{1+c}。
它从未承诺任意列系数都具有同一线性 raw 界。

当前反例把列改为 prime-only positive constant。真实 annular
Möbius 列还含 composite squarefree ideals，且 η、profile 和
自然 mask 都有固定的共同结构。不能保留 prime 项的正下界后，
把真实列中其他项直接删去：内和先有 cancellation，再取平方。
因此反例说明 generic sieve 无法代替原特殊合同，并不反驳该合同。

另一个容易混淆的量词是行限制。原 source 12365–12366 的起始行
为 sixth-power-free；12394–12408 付的是 all-row scale supremum；
12437–12445 才以 (u,a)↦ua^6 注入到该全行终端。
所以把起始行改成 d-free 并不能从终端 raw family 删掉 r^d 行。
460 §3 末段已经准确指出这一点。

## 5. 六次与四次放大的定量比较

457 的相对引理保留以下真实前件：每个固定 c>0 的线性 all-row
raw scale supremum、所有所需 row profiles 的固定 polynomial
height 费用、自然零延拓、正密度 multiplier 计数和 d-free 注入。
精确 divisor transfer 对应原 source 12416–12434；
scale supremum 对应 12394–12408；
行参数 Sobolev/height 费用对应 12457–12465。

在这些全部已经支付的特殊 raw 前件下，H=max(2U,D^{1+c})、
P=(H/U)^{1/d} 给 H/P，从而对 D=U^r 有

\[
 e_d(r)=\max\{1,[1+(d-1)r]/d\}.
\]

这只是一份未加 prime slots 的二矩指数。当前临界长行
r=1.1242271467860845 的比较为：

| 合同 | 未加 slots 的 U 指数 |
|---|---:|
| 原已引用 cubic raw + d=6 放大 | 1.1035226223217371 |
| 假定特殊 quartic raw 已付 + d=4 放大 | 1.0931703600895634 |
| 只用458的已付全行大筛包络 | 1.4575604801194178 |

理想六次与四次之差恰为 (r−1)/12=0.0103522622321737。
458 的全部行上界是 U+(UD)^{2/3}+D U^{1/3}；
当 r>1，其主指数是 r+1/3。沿 ua^4 放大把 H 加大后，
B(H,D)/P 的 H 幂全正，不能凭该上界取得理想四次收益。

这与 460 的新下界相容：较小 d 改善的是特殊 raw 合同下的
放大效率，同时使一般任意列矩阵的完整幂次行更密。
两种合同不同，没有矛盾。

在旧临界 cutoff 上还有一项独立检查：
short detector count 与旧 long count 都为2/3。即使理想四次
合同降低该点的 long count，取二者最大值后 short count 仍为2/3，
所以固定旧 cutoff 的 whole count 没有收益。必须重新选择 crossing
并重做全部预算，不能把上述0.01035直接减在 σ 上。

## 6. 换域仍缺哪些具体接口

Q(√−3) 的指数优势来自源 766–835 的 cubic Gauss signal 与
1789–1793 的 completed cubic reflection（ordinary local branch）；实际 retained j=1
在 7697–7702 反射为 sextic 的二次幂，能使用二次终端大筛。
固定判别式、格密度、有限 units/class sectors 只改变常数。

Gaussian 的 γ_1(c)²=μ(c)α(c) squarefree signal 已有具体证明；
其局部 phase 必须按
[DDHL v5 §3](https://arxiv.org/html/2306.11875v5) 的 supplement
读取。这个信号不等于全 incoming quartic rows 的 completed
reflection，也不自动产生原 Euler reciprocal。

登记新无零半平面以前至少还须分别证明：

- 对实际 μ(n)η(n) 列的近临界 all-row scale supremum，带全部
  required row profiles、导子及 polynomial height；任意列 generic LS
  不能提供它。
- 新 metaplectic completion 与全部 incoming residue sectors、
  Gauss/Euler phases、natural zeros、cusp/pole/residue branches。
  普通有限阶 Hecke FE 不替代这个合同。
- 同一个 marked inverse 列、两个 plain 列和一次 prime slots 的
  递归，保留 common coefficients/masks、Θ exceptions 和 strict widths。
  原 13032–13062 的共同矩形、prime factors 与 masks 有实际用途；
  不是仅 row conductor 大小的抽象合同。
- 新 local Euler tuple、low/whole-bin contours、principal signal 和
  同一 normalizer。ua^6 及 ζ_F(6z) 所产生的原留数/low 几何不能
  在改成四次以后未经证明地保持原式。
- actual κ 和全 finite-order family 的统一量词、bootstrap、
  Mellin continuation 与最后 Dirichlet transfer。
  source 12833–12844 的 prime-slot contour 明确要求
  β_*≤(1+κ)/2；不能使用尚未证明的新域零自由线支付自身 slots。

对于高次 CM 域，普通 conductor 因子仍是 C_K^{1/2-s}；
度数增加的是 Γ(s) 的个数及 height 费用。
[Goldmakher–Louvel (3.1)–(3.2)](https://arxiv.org/html/1112.1642v2)
直接保留这个指数。degree 2r 的有限阶系统有 Γ(s)^r；
r>1 时 unit rank=r−1，所以 norm-bounded element rows 已无限，
必须先选单位商/理想索引及受控 archimedean representatives。
仅扩到包含 μ6 的域不会改变 d=6 的放大幂。

## 7. 最终范围

460 全文限定通过。新证明是 arbitrary-column 全行幂次下界、
必要阈值和有明确 Hecke-family 前件的二次上界；
它增强了数域路线的障碍定位，没有解决 Gaussian Möbius cancellation。

既有引用输入 [R] 范围内已记录的边界
σ_*≈0.874957019420099 不因本次审查改变。
本报告不登记反事实 Gaussian 无零数值，也不把理想 raw 指数、
有限 Gauss 核验或条件 crossing 节省改称新的全族定理。
