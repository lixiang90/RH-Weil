# 模型基准独立复核（Descartes）

日期：2026-09-06。以下保留修订前独立报告；异议处理见笔记 307 第八节。

**审查结论：数学主体通过，限于已列明的经典几何输入；未发现循环论证、错误的全扩域公式或 PLF 实例化失败。** 有一处局部缺前提应补明，另有几处建议展开的说明。本次未修改文件，也未执行 commit/push。

1. **307 第 7 节遗漏了局部前提 \(\kappa>0\)。**  
   [第 137 行](F:/codex-build/RH/RH-Weil/notes/307-odd-polarization-and-elliptic-degree-benchmark.md:137) 单独声称权函数可积，须补上这一条件；例如 \(\kappa=0,r=1,f(t)=1\) 时，积分在原点发散。结构论文和 163 已明确要求 \(\kappa>0\)，因此不影响它们的相关结论。建议同时写明指数和具有实频率。合并重复频率后，
   \[
   \int_{-R}^{R}\left|\sum_j a_je^{i\lambda_jt}\right|^2dt
   =2R\sum_j|a_j|^2+O(1),
   \]
   故非零指数和在 \(r=0\) 时确实发散。055 的变化阶数条件确为 \(r_X\ge2\)。

2. **次数到二维模型的依赖链成立，没有预设纯谱。**  
   [307 第 51 行起](F:/codex-build/RH/RH-Weil/notes/307-odd-polarization-and-elliptic-degree-benchmark.md:51) 的点数、交叉项符号、判别式均正确。建议明确
   \[
   V=\mathbb Q[\pi]\subset\operatorname{End}_{\mathbb F_5}(E)\otimes_{\mathbb Z}\mathbb Q,
   \qquad Q(\alpha/m)=\deg(\alpha)/m^2.
   \]
   二次同态关系确实能在引入二维表示之前推出：令
   \(\gamma=\pi^2+2\pi,\ k=2m-m^2\)，则次数乘法性给出
   \[
   \deg(\gamma+[k])
   =\deg((\pi+[m])(\pi+[2-m]))=(5-k)^2.
   \]
   两边都是 \(k\) 的二次多项式，并在无限多个整数上相等，故可取 \(k=5\)，得到
   \(\deg(\pi^2+2\pi+[5])=0\)，从而该同态为零。这正是所引 Milne II.6.2 的论证机制，无须 Hasse 界。[Milne 原文](https://www.jmilne.org/math/Books/EC2.pdf)

   随后由不可约多项式 \(T^2+2T+5\) 得到基 \(1,\pi\)，再由
   \(Q(a+b\pi)=(a-b)^2+4b^2\) 得到实正定性，顺序没有倒置。

3. **修订 PLF 的一般证明与具体模型均成立。**  
   [论文定义及证明](F:/codex-build/RH/RH-Weil/papers/rh-weil-structure-paper.tex:159) 中，\(F\) 保持 primitive 子空间；在 \(L^rP^a\) 上比较缩放因子 \(q^r\) 与 \(q^{d-a-r}\)，确实得到
   \[
   S_nF=q^{n-d}FS_n,\qquad h_n(Fx,Fy)=q^nh_n(x,y).
   \]
   建议将“允许的 \((a,r)\)”显式写成 \(0\le a\le d,\ 0\le r\le d-a\)，并约定范围外分次为零。这是定义精确化，不是发现反例。

   我逐项核验了这个模型对六条公理的满足：

   | 公理 | 核验结果 |
   |---|---|
   | 分次交换代数、保分次实结构 | 外代数及有理基上的系数共轭满足要求 |
   | 顶次迹与非退化配对 | \(H^0\times H^2\) 配对为 \(1\)，\(H^1\) 配对矩阵为可逆的 \(\Omega\) |
   | 实 Lefschetz 元、Hard Lefschetz | \(L:H^0\to H^2\) 为同构，\(H^1\) 上对应恒等映射 |
   | \(F\) 的乘法、共轭及缩放相容性 | 外幂延拓给 \(F(L)=5L\)、\(\tau F=5\tau\) |
   | primitive 分解 | \(P^0=H^0,\ P^1=H^1,\ H^2=LP^0\) |
   | \(J,S,h\) 极化公理 | 可逆性、相容性、Hermite 对称及正定性全部成立 |

4. **\(J\)、正定性和常数没有符号或倍数错误。**  
   [307 第 84 行起](F:/codex-build/RH/RH-Weil/notes/307-odd-polarization-and-elliptic-degree-benchmark.md:84) 中
   \[
   J_1=\frac{F+I}{2},\quad J_1^2=-I,\quad 2\Omega J_1=H.
   \]
   因而它既是实矩阵，又与 \(F\) 交换。所选常数给出
   \[
   h_1(x,x)=|x_0-x_1|^2+4|x_1|^2>0\quad(x\ne0).
   \]
   \(H^0,H^2\) 上均为标准绝对值平方，三个次数的缩放分别是 \(1,5,25\)。虽然 \(S_1^2=-4I\)，修订定义并未要求通常 Hodge star 的平方归一化，故不构成错误。

5. **全部 \(n\) 的点数与 zeta 识别是真正的推导。**  
   [第 106 行](F:/codex-build/RH/RH-Weil/notes/307-odd-polarization-and-elliptic-degree-benchmark.md:106) 建议补上这一个显式等式，以消除“次数等于范数”只是宣称的疑虑：
   \[
   M_{a+b\pi}=
   \begin{pmatrix}a&-5b\\b&a-2b\end{pmatrix},
   \qquad \det M_{a+b\pi}=a^2-2ab+5b^2=Q(a+b\pi).
   \]
   因为每个 \(\pi^n\in\mathbb Z[\pi]\)，结合每个 \(n\ge1\) 的可分核计数，就得到
   \[
   N_n=\det(I-F^n)=1+5^n-\operatorname{tr}(F^n).
   \]
   形式幂级数恒等式随后给出的 zeta 分式、分子根模 \(5^{-1/2}\) 和中心线均正确。Milne AV §19 的证明也明确先建立全部幂的核计数，再处理纯性，二者可以分开引用。[Milne AV 原文](https://www.jmilne.org/math/xnotes/AVs.pdf)

6. **没有发现将模型冒称为通常 étale 上同调实结构的断言。**  
   这里的共轭是
   \[
   \overline{a+b\pi}=\bar a+\bar b\,\pi,
   \]
   它固定有理向量 \(\pi\)；它与二次域的共轭／Rosati 对合
   \(\pi^\dagger=-2-\pi\) 是不同操作。建议在 [第 102 行](F:/codex-build/RH/RH-Weil/notes/307-odd-polarization-and-elliptic-degree-benchmark.md:102) 更明确地写：“本构造未建立与该曲线通常 étale 上同调的有理形式、实结构及杯积的比较同构。”论文“不能自动实例化”的提醒与本笔记逐项构造后实例化并不冲突。

[基准脚本](F:/codex-build/RH/RH-Weil/scripts/elliptic_degree_benchmark.py:31) 用 `python -B` 执行通过；有限域运算及所有断言正确。我另在内存中独立检查了完整四维外代数的乘法、配对和全部缩放关系，并额外枚举得到 \(N_3=104,N_4=640\)。这些额外检查仍只是有限验证，全 \(n\) 结论依靠上述证明。

**通过范围**是 307 的全部数学论证、该脚本及论文修订 PLF 定义与直接推论。外部的次数二次性、同态次数理论、可分态射核计数，以及一般 Rosati 交数正性的几何基础，已核对引用及依赖方向，未全部从头重证；也未审查整篇论文其余数域论证或认证其 RH 研究状态。核对的本地原始文献为 :codex-file-citation{path="F:/codex-build/RH/RH-Weil/literature/background/milne-elliptic-curves-second-edition.pdf" purpose="source"} 和 :codex-file-citation{path="F:/codex-build/RH/RH-Weil/literature/background/milne-abelian-varieties.pdf" purpose="source"}。
