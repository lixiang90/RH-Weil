# 483. 接入已知 AM 八点全域证书与实际零点计数

2026-10-08。这是接入已有公开方法和固定证书的成果，不是新纪录。
PC8CL 的连续区间语义、全部有限数据及展开式对应现已分别核验。
结合此前已证明的实际谱压力和计数桥，项目采用下界
\[
\boxed{p_{\mathrm{simple,line}}\ge
\frac{118513839290}{175971686899}
=0.6734824299207958688\ldots.}
\]
这里分母是全部非平凡零点数，按重数计。
同一账本另给全部非平凡零点的互异比例
\[
\boxed{p_{\mathrm{distinct}}\ge0.8367412149603979344\ldots.}
\]
这不排除少量线外零点，也不提高无零边界。

## 1. 已有解析装配与本次补齐的证书

此前的
[八点谱压力研究源](../reviews/2026-10-08/hybrid-original-eight-point-sqrt-pressure-research-compression.md)
及其[不同作者审查](../reviews/2026-10-08/hybrid-original-eight-point-sqrt-pressure-review-whole.md)
已经证明八点平方根压力、全部滑动块端项、AM 自身窗二矩，以及304的
实际复矩阵计数桥。它们当时只缺固定 PC8CL 七维全域下界的准入。
本次没有借用上游最终 zeta theorem 代替这些本地解析证明。

固定公开源为
[d272437 的 Solution.lean](https://github.com/josusanmartin/riemann/blob/d272437e7ebeb17b87c8c3d7cece592aa23785ab/submissions/dani-bound-2026/proof/Solution.lean)，
1,675,641 bytes，19,049 行，原始 SHA256
`012c6ac5f9282158a686500dc0c967bf0a9b00e1a6192734d8f237bb23dd2d5f`。

本次新增三类证据：

1. [连续语义独审](../reviews/2026-10-08/hybrid-original-am-eight-point-full-certificate-audit-pc8.md)：
   有向区间、导数包络、切线外推、Farkas、closure、非紧空间覆盖和逆序对称。
   该文冻结时仍待数值复演，不能单独看其早期状态判断最终准入。
2. [持久复演器](../scripts/am_pc8_finite_replay.py)和
   [全项输出](../output/am-pc8-finite-replay.json)：
   240项精确整数编译求值、7项全量有限结构检查，最终 Lean 退出码为0。
3. [结构桥](../formal/certificates/AMPC8StructuralBridge.lean)和
   [叶节点桥](../formal/certificates/AMPC8MinorantBridge.lean)：
   28种分裂、初始收紧与优化 minorant 判据的30个通用符号桥，
   另有5个执行适配器等价守卫，均由核心 Lean 检查。
   30个主桥的传递公理输出只有标准 `propext`。

240项使用 `#eval` 的任意精度整数求值，不能称为240个内核 `decide` 证明。
本次也没有重新构建整个外部 Lean / mathlib / zeta 工程。
有限检查与连续数学证明合并，才支持以下全域下界；输出文件自身明确
不单独证明解析定理或零点比例。

## 2. 实际全域下界

AM13 窗取
\[
v(u)=\cos(\sqrt2u)+\sum_{j=1}^{12}c_j\cos(2\pi ju),
\quad |u|\le1/2,\qquad f=v/Z_0,
\]
\[
Z_0=\sqrt2\sin(1/\sqrt2)>0,
\]
系数 \(10^9c_j\) 为
\[
(12310798,-15041681,3867664,6489926,-992327,5580097,
-6846472,3781297,-5670353,3355089,-450523,-218483).
\]
\(\sum|c_j|=0.06460471\)，故 \(v\) 为正；归一化核平方为
\[
w(x)=\left|\int_{-1/2}^{1/2}f(u)e^{2\pi ixu}\,du\right|^2.
\]
保持公开的26个非零 pair 权重及
\[
10^8(b_0,\ldots,b_6)=(28898,57272,75526,80958,75526,57272,28898).
\]
完整复演所支持的连续命题是
\[
g\in\mathbb R_{\ge0}^7\quad\Longrightarrow\quad
F_W(g)=\sum b_rg_r+\sum_{i<j}a_{ij}
 w\!\left(\sum_{r=i}^{j-1}g_r\right)\ge c,
\quad c=\frac{805003}{10^8}.
\]
pair 权重每个 span length 的质量不超过2，
\(B_0=\sum b_r=404350/10^8\)。

全项复演包括：值表512块与顶部、导数表512块与顶部、192个点列表、
全部凸区间链、小 gap 窗16区间、7份外层覆盖及32棵根树的精确消费位置。
gap 为连续实数，不能把这些检查理解成仅在网格点上的采样。
树上优化展开式已通过通用符号桥接到有连续语义的 `cupd` 和 `mcheckGZ`。

## 3. 平方根压力、二矩与全部端项

令 \(q=7\)、\(m=152\)、\(\tau=8/7\)，并取
\[
F=f_\tau(c(m-q))=2\sqrt{\tau c(m-q)}-\tau<m.
\]
已证明的全链端项给
\[
J\ge\frac Fm s-\frac{B_0(m-q)}m\,\mathrm{span}
          -\frac{F(m-1)}m.
\]
其中所有 \(m\)-offset 和压力端项均保留。
经固定平滑及304的同一实际计数桥，极限比例为
\[
p\ge\frac{2-R_{AM}-B_0(m-q)/m}{1-F/m}.
\]
使用 AM 自身二矩，不能把 MT 的常数直接补入新窗：
\[
R_{AM}=R_{MT}+\sum_{j=1}^{12}
\frac{c_j^2(1/2-1/(4\pi^2j^2))}{2\sin^2(1/\sqrt2)}.
\]
此前研究源的严格有理包络给
\[
2-R_{AM}>\frac{67216841}{10^8},\qquad
F>\frac{4084939303}{3500000000}.
\]
把这两个保守下界代入，精确得到本笔记开头的有理比例。
这些余量的计算已在原研究源中核验；本次补齐的是全域证书，
没有把有限数据当作实际渐近二矩的替代。

互异比例使用304的另一条实际惯性账本
\[
2D\ge3N-\mathrm{HS}^2+J+o(N).
\]
配合上面的同一个压力和简单零点下界，它给 \(2p_D\ge1+p\)。
这个结论来自该账本，不能以一个一般的简单/互异计数不等式代替。

## 4. 比较与研究范围

项目简单临界线下界从67.3058110282…%提高到67.3482429920796…%，
提高约0.04243196388个百分点。已知公开登记值写为67.34824%；
其参数和未取整消费公式与本次采用的方法相同。
多保留的小数位不构成超越已有最优的新纪录，因此没有触发
以刷新纪录为目的的论文发布。

[79.62%候选审查](../literature/supplements/2026-10-08-yang-7962-deep-audit.md)
的两个解析缺口仍然存在。本次改进来自另一份已有八点证书，
没有准入该候选的高阶矩常数。
[482](482-original-conditional-mobius-perron-remainder.md)的条件误差改进
及原 unit 主频带 major arcs 付款也不提供常数级四阶输入。
下一研究目标仍是原实际 minor arcs / signed 四阶预算和联合算术反馈。

## 5. 复现与冻结身份

将上述固定公开源保存为 `tmp/pc8-am-admission/Solution.lean`，
安装 `leanprover/lean4:v4.34.1` 后，在仓库根目录运行：

```powershell
python -B scripts/am_pc8_finite_replay.py --check
```

若 elan 路径不同，使用 `--lean` 指定。复演器只接收具有固定长度和
SHA256的源码，不运行上游脚本；重建忽略目录中的纯数值文件，
同时核验本仓库两份符号桥，最后比较保存的完整输出。
使用 Python `-O` 会被显式拒绝；失败、缺项、重项或任何 false 都不准入。

| 产物 | canonical LF SHA256 |
|---|---|
| 持久复演器 | `2db626d7c3fbcc1f6ced7580d0fe847fff743b1039aa58797392e9e05845600f` |
| 全项输出 | `48c29521994321837b60ea39661b93f87c28560b5f19932c583ad8b29f5dd549` |
| 结构桥 | `98771eceea94a14f3a1be38c1e9c7ab48fffbb0d1c77bbfde636d21358b9ba9f` |
| 叶节点桥 | `f3947ca27750760322481a87ed5da4a5a8702a92bdf4570a6a4727f957fee114` |

独立提取和重放的最终范围见
[抽取审查](../reviews/2026-10-08/hybrid-original-am-eight-point-numerical-extraction-review-pc8.md)。
早期失败只涉及执行栈和编译求值路由性能；最终检查保持同一数学定义、
全部固定数据及原根等式。本笔记的比例准入依赖完整证据组合，
没有将编译成功、30个符号桥或任一单独 JSON 当成整个 RH 的形式化证明。
