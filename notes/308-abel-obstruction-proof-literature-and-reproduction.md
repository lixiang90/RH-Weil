# 308. Abel 质量障碍稿：证明收敛、文献比较与复现

日期：2026-09-06。对应 GOAL 第五节与第十节第 3、4 项。
成果归类：指定响应的内部复核／技术重建 [T/N]，使用明确的经典外部输入 [R]。
不主张组合的文献优先权，不作为新零点比例或 RH 证明。

## 1. 固定对象与准确结论

完整定义和证明见 [论文源稿](../papers/abel-mass-obstruction-paper.tex)。
固定 \(0<\sigma<1\)，对实际 von Mangoldt 系数及同一截断的连续源定义
\[
\alpha=\sum_{2\le n\le N}\Lambda(n)n^{-\sigma}e^{-n/Y}\delta_{\log n},\qquad
d\beta(\lambda)=\mathbf1_{[0,\log N]}e^{(1-\sigma)\lambda-e^\lambda/Y}d\lambda.
\]
令 \(A=\alpha(\mathbb R),B=\beta(\mathbb R),S=A+B,M=A-B,\mu=M/S\)，
并取偶对称化后的零质量通道 \(p=\alpha^{\rm ev}-A\delta_0\)、
\(c=B\delta_0-\beta^{\rm ev}\)、\(r=p+c\)。若 \(F_\eta(t)=\eta(({-\infty},t])\)，
则使用唯一的归一化
\[
D=\|F_p\|_2^2+\|F_c\|_2^2,\qquad
J_4=\frac{\|F_{r*r*p}\|_2^2+\|F_{r*r*c}\|_2^2}{S^4D}.
\]

已通过独立审查的主结论为：

1. 对固定 \(\sigma\)、所有充分大实 \(Y\)、每个有限整数 \(N\ge Y\)，
   \(J_4(Y,N)\gg_\sigma Y^{-3}\log Y\)。常数统一于全部此类 \(N\)，没有隐藏 \(N\ll Y^2\) 上限。
2. 若存在非实零点 \(\rho\) 满足 \(\Re\rho>\sigma\)，则无截断质量 \(M_\infty(Y)\)
   在任意远处取正值和负值，因而有趋于无穷的零点序列。
3. 设 \(N(Y)=\lfloor\Phi(Y)\rfloor\)，\(\Phi\) 最终连续非减。固定 \(\kappa>0\)，
   在第 2 项的零点前提及
   \[
   N/Y\ge(3/\kappa)\log Y-b\sqrt{\log Y},\quad 0\le b<0.8476836
   \]
   下，\(J_4=O(|\mu|^\kappa)\) 不能统一成立于所有充分大实尺度的非零质量点。
   四次预算特别覆盖 \(N=\lfloor cY\log Y\rfloor,c\ge3/4\)；
   正则超对数截断 \(N/(Y\log Y)\to\infty\) 排除每个正幂质量预算。

\(0<\sigma<1/2\) 时临界线零点存在性使第 2、3 项无条件。
中心参数 \(\sigma=1/2\) 的全实尺度预算蕴含 RH；未证明反向蕴含。
这里并未否定每条 dyadic 序列、任意选定共尾序列或完整 Weil 型正性。
Gamma 通道及通向整个算术显式公式的桥梁独立开放。

## 2. 从定义到主结论的依赖链

| 步骤 | 完整证明位置／输入 | 已检查的关键点 |
|---|---|---|
| Brownian／Fourier 能量恒等式 | 论文 §2，直接积分 | \(-1/2\) 距离系数、\(1/(2\pi)\) Fourier 归一化、两个通道采用同一截断 |
| Mellin 与质量振荡 | §3；Euler 恒等式、zeta 延拓；Landau 引理在稿中自证 | 初始收敛域 \(\Re s>1-\sigma\)，实极点抵消，零点留数非零；不假设最右零点存在 |
| 初等多项式下界 | §§4–6；Bertrand 定理 | 孤立素数原子及乘积中的三次估值；有限截断端点和质量根附近扰动 |
| 中尺度响应下界 | §7；MV 局部间距均值、定性 PNT | 保留 \(-M\) 的零频项；时间尺度 \(U\asymp Y\)，不以最大截断 \(N\) 粗代替局部间距；连续源 BV 端点完整 |
| 对数截断扩展 | §8；FKS Corollary 1.4 | 带符号尾项含 \(e^{-d\sqrt{\log Y}}\)；取 \(b<d<0.8476836\)；处理 floor 截断和非零质量 |

有限算例不是以上任何渐近步骤的前提。原子下界是较弱但更初等的独立基线；
中尺度下界和有符号尾给出更强的已证范围。

## 3. 原始文献比较与新颖性分级

| 原始文献 | 其定理的对象与本文使用 | 与本稿结论的区别 |
|---|---|---|
| [Hardy 1914](https://gallica.bnf.fr/ark:/12148/bpt6k3111d/f1014)，158:1012–1014 | 临界线上无穷多个零点；这里只用存在一个 | 不陈述本文响应或质量预算；BnF 获取 403，书目与原文转录核对，实际图像落页待核 |
| [Erdős 1932](../literature/background/erdos-1932-bertrand.pdf) | Bertrand 素数存在性，服务于初等原子选择 | 不给截断响应估计 |
| [Mahatab–Mukhopadhyay v4](../literature/background/mahatab-mukhopadhyay-oscillations-v4.pdf)，Theorem 3.1 | Mellin–Landau 定号与收敛障碍；比较振荡论证 | 本文自证所需 Landau 引理，不声称创造此机制 |
| [Montgomery–Vaughan 1974](../literature/background/montgomery-vaughan-hilbert-1974.pdf)，Theorem 2、Corollary 2 | 一般有限指数和的局部间距均值公式 | 本文仍需针对实际源、中心项及 BV 背景证明截断一致下界 |
| [Fiori–Kadiri–Swidinsky v3](../literature/background/fiori-kadiri-swidinsky-psi-v3.pdf)，Corollary 1.4 | \(|\psi(x)-x|<9.22022x(\log x)^{3/2}e^{-0.8476836\sqrt{\log x}}\)，\(x>2\) | 上界经带符号分部积分转为 Abel 质量尾；不单独等于响应障碍 |

FKS 使用已验证的有限高度零点数据及独立零自由区域，不是假定全 RH。
v3 的 Remark 1.5(2) 明确采用修正后的次凸常数 0.77；本稿使用其已陈述的 9.22022，
不挪用文中讨论的潜在改进 8.99284。定性 PNT 由此推出，
结合 \(\psi-\vartheta=O(\sqrt x\log^2x)\) 得所需素数区间质量。

2026-09-06 检索了本稿特定术语 “Abel mass discrepancy Brownian zeta”、
“mass-only Abel Brownian” 及 Mellin–Landau／指数平滑振荡相关组合；
主张核对回到上述原始文献。检索没有建立组合的优先权，更不是排除了所有先行成果。
所核读定理未直接陈述同一归一化响应的完整结论，但这不能证明新颖性。
因此本阶段按**可审读的技术重建与内部复核成果**收敛，不按已确认原创论文晋级。

## 4. 独立复核及异议处理

[首轮全文报告](../reviews/2026-09-06/abel-proof-review.md)核读全部源稿、
原有 10 页 PDF 及直接数学依赖，并复跑两份脚本；
[修订闭环报告](../reviews/2026-09-06/abel-followup.md)检查变更及上下文。

| 异议 | 修订 | 处理状态 |
|---|---|---|
| massfloor 推论缺明确截断范围 | 固定 \(\sigma\)，序列 \(Y_j\to\infty\)，有限整数 \(N_j\ge Y_j\)，非零质量、固定预算常数 | 关闭；固定 \(N=2\) 反例不再落入假设 |
| 摘要整数／正则截断未写齐 | 明确 \(N\in\mathbb N\) 及最终连续非减的 \(\Phi\) | 关闭 |
| 局部可微不能直接推出解析 | 在 \(z=1/Y,\Re z>0\) 上证明局部一致支配及全纯 | 关闭 |
| 48 样本未写截断 | 补命令、\(N=40Y\)、软件版本及浮点误差边界 | 关闭 |
| 临界线存在性仅引手册 | 添加 Hardy 原始引用；FKS 明确为定性 PNT 来源 | 关闭；原 PDF 的获取失败单列 |

子代理闭环仅代表所列范围的独立内部推理；不是外部同行评审。
后续 263–268、271–303 各种不同截断／记录模型未并入本稿，不能用本次全文通过为其背书。

## 5. 可复现证据

在仓库根目录运行：

```powershell
python scripts/abel_prime_atom_audit.py
python scripts/abel_mass_discrepancy_probe.py --tail-factor 40 --skip-e1
```

首命令由独立审查者和主代理分别运行：24 个有限情形、126 个原子系数、567180 个有理间距不等式全部 PASS。
第二命令由独立审查者本轮复跑：\(\sigma=1/4,1/2,3/4\)，\(Y=2^3,\ldots,2^{18}\)，共 48 个质量样本为负。
使用 Python 3.14、numpy 2.5.2、mpmath 1.3.0；本机 longdouble 只有 52 位显式尾数。
这些不是认证区间数值，尾 majorant 不包含浮点系数／求和误差，不能推首次振荡高度或渐近预算。
prime_jump_full_response_probe.py 的旧 50 位小例仅保留历史记录，本轮不冒称重新运行。

论文编译、PDF 哈希和版面核查单独记录于 [papers/README](../papers/README.md) 及本轮审计目录。
文献获取、解析与哈希见 [文献索引](../literature/README.md) 和 manifest.json。
