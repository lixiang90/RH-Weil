# 411 PV、归纳极限与对数迹来源审计

2026-09-21。只读agent Laplace返回全文，raw.json保留原始记录。
主线程已采纳P3核心/理想措辞及全域迹性补强，未把指定来源页核读称为全文认证。

**来源审计通过所需 PV／归纳极限比较，以及真正半有限迹的构造与 \(\log p\) 规范化。** 对411定向核读发现一处需改写：§6第179行的“稠密理想”应改为“稠密 \(*\)-子代数”，并补足全代数上的迹性论证。其 \(K_0\) 定义域补充有效。

本次核读 [411正文](H:/codex-build/RH/RH-Weil/notes/411-f1-full-rational-relative-classes-and-logarithmic-trace.md:136) 的快照 SHA256：
```text
946f3d59c4b2e4fd7af91ab5c54f4156508f5830e2454cf6d5d6d44a80ead878
```

1. **标准来源与准确页码**

   主要依据已存 Blackadar 作者版 :codex-file-citation{path="H:/codex-build/RH/RH-Weil/literature/f1/blackadar-k-theory-author-book6.pdf" purpose="source"}，SHA256：
   ```text
   a20e676e9d400ebcd0cd07c13fbdbe1fac759a30c739fab23d6161ecfb1a23fb
   ```

   | 所需事实 | Blackadar 条款 | 印刷页／PDF页 |
   |---|---|---|
   | 交叉积、point-norm 连续作用、amenable 时 full=reduced | §10.1 | 71／85 |
   | 同伦不变性及非幺 \(K_0\) 定义 | §5.2.2、§5.5 | 29、31／43、45 |
   | \(K_0\) 与归纳极限交换 | §5.2.4 连同 §5.5 | 29、31／43、45 |
   | \(K_1\) 与归纳极限交换 | §8.1.5 | 61／75 |
   | PV 六项正合列 | Theorem 10.2.1 | 73／87 |
   | stably unital 时 \(K_{00}(A)\cong K_0(A)\) | Proposition 5.5.5 | 31／45 |
   | 参数圆的自然分裂及 K 群计算 | Exercise 9.4.1 | 68／82 |

   [Blackadar 作者原件 PDF](https://bruceblackadar.com/Mathematics/book6.pdf)

   另已视觉核准 PV 原文 **Theorem 2.4，印刷 p.103／PDF p.11**；**Remark 2.7，印刷 p.104／PDF p.12** 明确通过单位化及分裂扩张处理非幺代数。原图写 \(1-(\alpha^{-1})_*\)，与 Blackadar 的约定不同；本题这两个箭头均为零，单射结论不受影响。[出版社原始 PDF](https://jot.theta.ro/jot/archive/1980-004-001/1980-004-001-005.pdf)

2. **§5 的 PV 单射与无限阶段适用性成立**

   必须给 \(H_F=\bigoplus_{\ell\in F}\mathbb Z\log\ell\) **离散拓扑**。设
   \[
   \beta_s(f)(t)=f(t-s),\qquad \beta_s(u_h)=u_h.
   \]
   这里 \(u_h\) 是交叉积的**乘子酉元**。平移与原作用交换，因此这些公式定义 \(A_F\) 的自同构。

   对有限和有
   \[
   \left\|\beta_s\!\left(\sum_h f_hu_h\right)-\sum_hf_hu_h\right\|
   \leq\sum_h\|f_h(\,\cdot-s)-f_h\|_\infty.
   \]
   由稠密性得到 point-norm 连续实流。故
   \(\alpha_q=\beta_{\log q}\) 经 \(\beta_{s\log q}\)、\(0\le s\le1\)，同伦于恒等，两个 K 群上的作用均为恒等。

   协变表示的泛性质给出
   \[
   A_{F\cup\{q\}}\cong A_F\rtimes_{\alpha_q}\mathbb Z.
   \]
   PV 因而给出
   \[
   0\longrightarrow K_i(A_F)
   \longrightarrow K_i(A_{F\cup\{q\}})
   \longrightarrow K_{1-i}(A_F)\longrightarrow0.
   \]
   **中间的第一箭头就是稿中实际包含诱导的箭头。**

   子群包含在交叉积上等距：规范包含与 identity 系数条件期望相容，而这些 amenable 群的条件期望忠实。全部有限标签和均落在某个有限阶段，故
   \[
   A_H=\overline{\bigcup_F A_F}=\varinjlim_F A_F.
   \]
   再用上述 K 连续性，每个有限阶段的两个 K 群均单射进入极限。

   参数圆也成立：对 \(C(\mathbb T)\otimes A_F\) 使用
   \(\mathrm{id}\otimes\beta_s\) 重复 PV；并且
   \[
   C(\mathbb T)\otimes A_H
   =\varinjlim_F\bigl(C(\mathbb T)\otimes A_F\bigr).
   \]
   后一个等式也可直接用连续函数的紧像及有限分割统一逼近证明，不需额外假设。

   对不同素数 \(p,q\)，\(\log p/\log q\) 无理，因此当 \(|F|\ge2\) 时该平移作用**确实不 proper**。以上论证没有使用 properness。

3. **§6 的规范权确为忠实、下半连续、稠密定义的半有限迹**

   规范忠实条件期望的准确出处为 Sims **Proposition 4.2.6，印刷 p.33／PDF p.37**，本地原件 :codex-file-citation{path="H:/codex-build/RH/RH-Weil/literature/f1/sims-hausdorff-etale-groupoids-2017.pdf" purpose="source"}。[作者 PDF](https://aidansims.com/papers/Sims2017.pdf)

   定义
   \[
   \tau(a)=\int_{\mathbb R}E_H(a)(t)\,dt,\qquad a\ge0.
   \]
   全代数上的迹性可直接验证。对任意 \(x\in A_H\)，写 Fourier 系数
   \(f_h=E_H(xu_h^*)\)。正则表示对应的平方可和系数展开给出
   \[
   E_H(x^*x)=\sum_h\beta_{-h}(|f_h|^2),\qquad
   E_H(xx^*)=\sum_h|f_h|^2.
   \]
   正项和在系数代数范数中收敛。由 Lebesgue 平移不变性与 Tonelli，
   \[
   \tau(x^*x)=\sum_h\|f_h\|_2^2=\tau(xx^*),
   \]
   允许双方为 \(+\infty\)。

   下半连续性来自积分权的下半连续性及 \(E_H\) 的连续性；忠实性来自 \(E_H\) 忠实及 Lebesgue 测度满支撑。有限标签、紧支系数的代数包含于
   \[
   \mathfrak n_\tau=\{x:\tau(x^*x)<\infty\},
   \]
   因而定义域稠密。

   半有限性也可明确补证：取 \(0\le e_n\le1\) 的紧支系数近似单位，则
   \[
   a_n=a^{1/2}e_na^{1/2}\le a,\qquad
   \tau(a_n)\le\|a\|\int e_n(t)\,dt<\infty,
   \]
   且 \(a_n\to a\)，由下半连续性得到所需逼近。

   **[P3] [第179–180行](H:/codex-build/RH/RH-Weil/notes/411-f1-full-rational-relative-classes-and-logarithmic-trace.md:179) 建议替换为上述全域论证。** 有限标签、紧支系数构成稠密 \(*\)-子代数，通常不是整个 C* 代数的双边理想；仅有稠密核心上的循环恒等式，也不应省略延至全域的步骤。此处修正不改变迹存在的结论。

4. **实际投影有限迹及 \(K_0\) 定义域补充有效**

   第182–184行的谱截断论证正确：近似选取 \(b\in\mathfrak n_\tau\)，使 \(b^*b\) 足够接近投影 \(P\)，则
   \[
   Q=1_{(1/2,\infty)}(b^*b)\sim P,\qquad
   \tau(Q)\le2\tau(b^*b)<\infty.
   \]
   矩阵放大后同样成立。

   第185–188行也成立：单周期代数
   \(A_L\cong C(\mathbb R/L\mathbb Z)\otimes\mathcal K\)
   有投影近似单位；其进入 \(A_H\) 的包含非退化，因为共同的 \(C_0(\mathbb R)\) 已非退化。故该近似单位继续适用于 \(A_H\)。

   因此可应用 Blackadar **Proposition 5.5.5**，把 \(K_0(A_H)\) 写成实际矩阵投影差。迹在这些投影上有限、对等价不变并对直和可加，确实给出有限值同态
   \[
   \tau_*:K_0(A_H)\longrightarrow\mathbb R.
   \]
   这一步解决了非幺代数中不能直接对单位化投影差做“无穷减无穷”的问题。

5. **秩一值为 \(\log p\)；保迹同伦的范围须明确**

   令 \(L=\log p\)。选取 \(\xi\in C_c(\mathbb R)\) 满足
   \(\sum_{n\in\mathbb Z}|\xi(t-nL)|^2=1\)。相应秩一投影可写为
   \[
   e=\sum_n\xi(t)\overline{\xi(t-nL)}\,u_{nL}.
   \]
   这是有限标签和，且 \(E_L(e)=|\xi|^2\)，故
   \[
   \tau(e)=\int_{\mathbb R}|\xi(t)|^2dt
   =\int_0^L1\,dt=L=\log p.
   \]
   稿中(17)的纤维对角和给出一般秩 \(d\) 的值 \(dL\)；矩阵放大时使用未归一化矩阵迹。子群包含保持条件期望，所以该投影进入 \(A_H\) 后仍取值 \(\log p\)。这里的秩一属于单周期紧算子模型。

   固定 \(A_F\) 上的实平移流确实逐点保迹：
   \[
   E_H\beta_s=\beta_sE_H,\qquad \tau\beta_s=\tau.
   \]
   **这不推广成任意作用变形所得的 K 群比较都保迹。** 例如把单生成平移长度由 \(L\) 连续改为 \(2L\)，各自基本圈秩一投影的 Lebesgue 迹就由 \(L\) 改为 \(2L\)。本题新增素数过程中，来自既有 \(A_F\) 的元素则因包含保持条件期望而保持迹值。

实际核准的是 §5第138–155行及 §6第172–197行的标准比较和定义域。第156–167行调用的核类非零、矩阵兼容，以及(18)中的因子2和具体类识别，均留给 Euler；新增端点可逆性分类亦未审核。

原文核读包括上述 Blackadar 条款及相关证明页、Sims PDF pp.35–37；PV 原件视觉核读 PDF pp.1–4、9–12，未通读整篇。未保存新文件，未修改仓库，未运行 Git 或 Lean。
