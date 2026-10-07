# 438 独立全文审查：来源、物理截止和单窗四矩障碍

日期：2026-10-07。审查者：twisted_research。只读审查主稿、外部原始来源和两份独立推导报告；只新增本报告，未修改 notes 或 math，未构建 Lean。

审查对象：`notes/438-seven-eighths-and-zero-proportion-interfaces.md`，全文 184 行，已复读最终新增静态证据及全局 manifest 范围表述。本次所读 canonical LF SHA256（仅 CRLF→LF、UTF-8）：

`1b5109396c89efab2f1ad0fa2d4281ab2c7e53ba9ed25900e86f29dc83ea3283`。

**数学接口与范围：PASS。** 未发现需要改变 (1)–(3) 或单窗四矩障碍的实质错误。这个 PASS 不是 September-30 全证明的独立认证，也不是 Lean kernel 验收或新的零点比例、无零区域、RH 结论。§1 的本轮静态扫描已附可复核记录；本报告独立核对了全部逐模块哈希、总行数、仓库 HEAD/origin、实际定理入口和范围文档，不把未执行的 kernel 当作通过。

## 1. 所读版本与独立核查

已完整阅读另两份报告，但数学复核不只沿用其结论：

| 文件 | canonical LF SHA256 |
| --- | --- |
| `reviews/2026-10-07/hybrid-proportion-source-audit.md` | `ed4ce3563f306155e7976c8a462b6eee9a2f77328d9f1820bc2ca16dd82ad9a1` |
| `reviews/2026-10-07/hybrid-strip-inertia-derivation.md` | `e93e376ac357549c8db282a0b914b90eea23755cfb3801a1ad17fc2f09cfa7f0` |
| `output/openai-math-nonvanishing-static-closure.json` | `03e715bccb612f2a656be249ca676bd5e528e0f23416363d00fee90c03f95903` |
| `scripts/openai_math_source_closure_audit.py` | `cba2fc4dc3162d7edaf28417237978f99ebf797f485781f09cd87800713458c9` |

本地 math `git rev-parse HEAD` 为 `adc7f1241b42e322a6451854ab7e4b4c146bf78a`，origin 为 `https://github.com/openai/math`，与正文相符。独立读取了：

- September-30 `build/paper.tex` 的定理 106–119、common-signal criterion 400–431、low 8564–8574、principal signal 15650–15659、assembly 16440–16462，并结合此前 detector/endpoint 阅读。
- October-5 `build/paper2.tex` 的引言 61–81。81 行把 11/12 称为通向 7/8 的自然中间步骤；因此正文的版本关系准确。
- `lean/OAI/NumberTheory/DirichletL/Nonvanishing.lean` 全文 33 行：19–24 行调用 unconditional `dirichlet_nonzero`，29–31 行调用 unconditional `zeta_nonzero`。
- `lean/docs/003.md` 10–16 行及 `lean/formalization.yaml` 1662–1663 行。前者声明 ζ、所有正模数 Dirichlet 角色和指定 Hecke 族的 7/8 范围，排除 principal 极点；后者的 `review.status` 确为 `unchecked`。

本次直接浏览的 primary sources：

- [Alpöge–Furman v2 PDF](https://arxiv.org/pdf/2608.13637v2)，Theorems A/B、(2.8)、Lemma 2.1、Propositions 4.1–4.3、Theorem 5.7 及 Remark 6.1。
- [Lamzouri v2 PDF](https://arxiv.org/pdf/2609.02882v2)，计数定义、Theorem 1.1 和 Proposition 2.1。

未把公开来源的形式化声明当作本次重建结果，也未把本轮以后更高比例研究稿认证为纪录。

静态证据另作了只读交叉检查：输出列出 2,924 个本地模块、486,490 行、251 个外部未扫描模块，missing OAI 与 suspicious 列表均为空；逐个重读全部模块，2,924 个 SHA256 全部匹配，重新合计行数亦一致。阅读扫描脚本后，额外在剥除嵌套注释与字符串的同一本地闭包上搜索更广的 `sorry|admit|sorryAx|axiom` 词面，仍无命中。没有运行脚本的写文件 `main()`，没有改扫描输出或构建 Lean。`formalization.yaml` 的 unchecked 是全局 review 状态，最终正文对此限定正确。

## 2. 7/8 路线及计数口径

438 第 12–16、86–95 行的解释与原稿一致：无零断言是所有导子、所有高度的严格半平面，principal 极点允许；不排除边界线的零。对 ζ 利用函数方程得到闭条带 \([1/8,7/8]\)，而不是所有零均在临界线。

11/12 的稀疏六次幂行验账正确：由均方 \(\sum_{Nu\le H}|A_u|^2\ll D^{1+\epsilon}H\)、约 \(H^{1/6}/\log H\) 个素数六次幂行，以及 \(A_{p^6}-A_1=O(D/H^{1/6})\)，得到

\[
 |A_1|^2\ll D^{1+\epsilon}H^{5/6}+D^2H^{-1/3}.
\]

代入 \(H=D^{1+\theta}\) 后第一项的平方根是 \(D^{11/12+5\theta/12+\epsilon}\)，第二项更小；先依要求固定小 \(\theta\) 再取 \(D\to\infty\) 合法，不需要 \(\theta\to0\) 时一致常数。正文没有把这项均方单独当作全部续延证明。

7/8 的低侧指数 \(3/16\)、信号 \(C(s)=s-11/16\) 及 \(H_\eta\) 的收缩界均准确。它说明了 common-signal 的矛盾机制，仍没有声称本轮重验所有反射、递归和尾部。

438 第 99–110 行的交集、并集和平均严格分开。AF 的 \(C_0\) 计简单且在线，分母包含重数；固定 primitive Dirichlet 推广不提供移动 Hecke 行族的一致估计。Lamzouri 的并集按重数计，平均界是 \((N_s+N_0)/(2N)\)，不是简单在线交集的新下界。对应常数与 [Lamzouri Theorem 1.1](https://arxiv.org/pdf/2609.02882v2) 一致。

## 3. 独立重新证明一般 AF padding 的关键账本

这一部分以明确输入 \(H_\theta\) 为条件，记 \(d=\theta-1/2\in(0,1/2)\)。所有非平凡零都满足 \(|\Im\gamma_\rho|\le d\)，其中 \(\gamma_\rho=(\rho-1/2)/i\)。令

\[
 L=\log(T/(2\pi)),\quad h=2\pi/L,\quad
 \alpha_k=T+kh,\quad D_T=\lfloor LT/(2\pi)\rfloor.
\]

AF 使用 \(\widehat\phi(z)=\int\phi(t)e^{-izt}\,dt\)，与 Lamzouri 的 \(e^{-2\pi izt}\) 不同。正文各自保留尺度，未把两个 Fourier 约定混用。AF 的偶 \(C^2\) 窗支持于 \([-L/2,L/2]\)，归一化为 \(q_L=L\|\phi\|_2^2\asymp L^2\)。准确 Poisson 恒等式是

\[
 \sum_{k\in\mathbb Z}\widehat\phi(z-\alpha_k)^2=q_L,
 \qquad z\in\mathbb C.
 \tag{A}
\]

这里是复平方，不是绝对平方。[AF Lemma 2.1 及 (2.8)](https://arxiv.org/pdf/2608.13637v2) 给所需的恒等式与 \(C^2\) Fourier 衰减；正文正确保留了两者。

从 \(\|\phi^{(j)}\|_1\) 的原统一界可直接得到

\[
 |\widehat\phi(r+iy)|^2
 \ll T^d\min\{L^2,|r|^{-2},|r|^{-4}\},\qquad |y|\le d.
 \tag{B}
\]

全网格以最近格点分组，\(|r|<1\) 用二阶幂衰减，\(|r|\ge1\) 用四阶幂衰减，得到

\[
 \sum_{k\in\mathbb Z}|\widehat\phi(\gamma_\rho-\alpha_k)|^2
 \ll T^dL^2.
 \tag{C}
\]

若一个半侧网格距 \(\Re\gamma_\rho\) 至少 \(R\ge1\)，积分比较给

\[
 \sum_{\rm separated}|\widehat\phi(\gamma_\rho-\alpha_k)|^2
 \ll T^d(R^{-4}+LR^{-3})\ll T^dLR^{-3}.
 \tag{D}
\]

这些估计保留原网格；\(\alpha_{D_T}\) 与 \(2T\) 相差 \(O(h)\)，由距离不足 1 的端点集处理即可。

定义 \(v_\rho=(\widehat\phi(\gamma_\rho-\alpha_k))_{0\le k<D_T}\)，并用全部物理非平凡零定义
\(H=q_L^{-1}\sum m_\rho v_\rho v_\rho^{\mathsf T}\)。固定 \(T\) 的和绝对迹范数收敛。FE 对 \(\rho,1-\bar\rho\) 使两个向量互为共轭，故完整和与按高度截断的和都是实对称矩阵。单项虽用转置，仍有
\(\|v v^{\mathsf T}\|_1=\|v\|_2^2\)；无需把单项伪装为正 Hermitian rank-one 项。

在 \(I_P\) 外，\(R=\operatorname{dist}(\Re\gamma_\rho,I)\ge P\)，(D) 除以 \(q_L\) 后是 \(O(T^dL^{-1}R^{-3})\)。以重数计算的单位高度零数是 \(O(\log(|\gamma|+3))\)。\(|\gamma|\le3T\) 的两侧和为 \(O(L/P^2)\)，更远两尾为 \(O(L/T^2)\)，在 \(P\le T/2\) 时也被前者吸收。因此

\[
 \|E_P\|_1\ll T^dP^{-2}.
 \tag{E}
\]

首迹需要两项不同论证，不能直接把原内侧论证套到 padding 外侧：

- \(\gamma\in I\) 且距端点至少 1：用 (A) 减掉外网格，(D) 控制误差。单位高度求和给 \(O(T^d)\)。
- \(\gamma\in I_P\setminus I\) 且距 \(I\) 至少 1：直接用 (D) 控制**内网格**；同样是 \(O(T^d)\)。
- 距任一端点不足 1 的零共 \(O(L)\) 个；(C) 给每点归一化贡献 \(O(T^d)\)，合为 \(O(T^dL)\)。

故

\[
 |\operatorname{Tr}G_P-N(I)|\ll T^dL,
 \qquad |\operatorname{Tr}G_P-N(I_P)|\ll T^dL+PL.
 \tag{F}
\]

这独立验证了正文 (1)。其中较精细的日志指数来自 (C)，不是未经证明删除原 AF 的 \(L\) 损失。

在 \(\theta=7/8,P=T^{1/4}\) 时，(E) 是 \(O(T^{-1/8})\)，(F) 是正文 (2)。一般 \(P=T^\alpha\) 的迹范数尾 \(o(1)\) 充分条件是 \(\alpha>3/16\)；没有把充分条件声称为必要条件或新的零密度结论。

AF prime-side 控制的是这个相同完整矩阵 \(H\)。改变 \(P\) 只更改零侧截断误差，不更改窗口主常数 \(R(\psi)\)；所以正文第 150–152 行关于“不提升渐近比例”的结论成立。Theorem 5.7 的全矩阵 proof 给对数误差，Remark 6.1 给保守比例率；这两种公开日志账本均比上述归一化幂误差更大。此处不重新认证 AF 全证明。

## 4. Lamzouri 核增长与联合预算

正文保持 Lamzouri 的 \(2\pi\) Fourier 规范。固定实偶 \(\eta\)、\(\operatorname{supp}\eta\subset(-\lambda,\lambda)\)、\(\int\eta^2=1\)，有

\[
 \|\eta(u)e^{-2\pi izu}\|^2
 \le e^{4\pi\lambda|\Im z|},\qquad
 |\widehat{\eta^2}(z)|\le e^{2\pi\lambda|\Im z|}.
\]

实际零点缩放 \(|\Im z_\rho|\le d\log T/(2\pi)\)，差点的界多一倍，于是单向量平方 \(T^{2\lambda d}\)、双点核绝对平方 \(T^{4\lambda d}\) 正确。\(\lambda=1/2,d=3/8\) 时双点核指数确为 \(3/4\)。这没有使单项复平方变为正，也没有把微观条带宽度变为常数。

令 \(p_{\rm off}=1-N_0/N\)、\(p_{\rm mult}=1-N_s/N\)，均按重数计。Lamzouri 平均界给
\(p_{\rm off}+p_{\rm mult}\le1-C_0+o(1)\)。固定条带再给

\[
 \frac1N\sum|\beta-1/2|^k\le(3/8)^k p_{\rm off},
\]

两式相加就是正文 (3)。它没有重复叠加交集与平均信息，没有把 \(p_{\rm off}\) 当成不同零点比例，也没有把原尺度矩当成微观深度矩。

## 5. 单固定窗口四矩反例的独立检查及范围

所引报告选 \(f=\eta^2\)、\(\int f=1\)、\(K=\widehat f\)，固定平滑支持于一个单位区间。Parseval 准确给

\[
 R_{\rm lat}=\sum_{n\in\mathbb Z}|K(n)|^2=\int f^2,
 \quad \delta_f=R_f-R_{\rm lat}
 =2\int_0^1u(f*f)(u)\,du>0.
\]

对 \(m=\log T\to\infty\)、\(M\sim Tm/(2\pi)\)，在连续整数背景上，每隔
\(D=\lceil m^2/\delta_f\rceil\) 放一个重数 \(m\) 的簇，簇数 \(q\sim M/D\)，总重数 \(N=M+q(m-1)\)。重新核算得到：

\[
 M/N\to1,\quad q(m-1)^2/N\to\delta_f,
\]
\[
 \operatorname{Tr}A^2
 =MR_{\rm lat}+O_f(1)+O_f(qm)+q(m-1)^2+o(N).
\]

背景项来自 Schwartz 核差的可求和性；交叉项 \(qm=o(N)\)；不同簇的平方和也为 \(o(N)\)。所以二阶迹/N 精确趋于 \(R_f\)，不是任意宽松预算。簇 Gram 的非对角行和
\(2\sum_{n\ge1}|K(Dn)|=o(1)\)，故至少 \(q\) 个特征值达到 \((m-1)(1-o(1))\)，由此中心四阶迹/N 至少为

\[
 (\delta_f+o(1))m^2\longrightarrow\infty.
\]

原高度每单位区间有 \(O(m)\) 个背景点且至多一簇，因簇间高度距离 \(2\pi D/m\to\infty\)。故局部计数没有超出 \(O(\log T)\)。按位移 \(N^{-6}\) 拆开簇时，实际算子迹范数扰动为 \(O_f(N^{-5})\)；raw 四阶迹变化除以 \(N\) 趋零。补零维数或拆开后维数的中心矩差也不改变发散。因此全部点可以简单且在线。

438 第 172–177 行准确限定了否定范围：**固定条带、单个固定特征窗的二阶主常数及该局部计数尺度，不推出有界中心四阶迹。**反例不满足 ζ 对所有测试函数的完整显式公式，也不认证 Riemann–von Mangoldt 的完整逐高度误差。它没有否定实际四点算术、所有窗口联合约束或额外谱尾输入能够改善比例。

收窗障碍亦正确：若支持宽度 \(\lambda_T=O(1/\log T)\) 且 \(\int\eta_T^2=1\)，则 Cauchy–Schwarz 给 \(\int\eta_T^4\ge1/(2\lambda_T)\gg\log T\)。但这是所述直接缩放策略的障碍，不能泛化成所有可能核的不存在性。正文没有作该泛化。

## 6. 验收界限

数学部分没有请求正文修改。继续研究仍须区分：7/8 原稿/源码的外部声明；显式 \(H_\theta\) 输入下的本项目截止定理；实际新比例或新无零区域。正文已保持这种区分。

本审查不验证最新 67.3% 稿的全部常数证书，也不沿数学仓库的完整依赖重跑 proof kernel。§1 的静态证据已与当前源逐模块核对，但词面扫描是否出现 `sorry`/`axiom` 本身仍不能替代 elaboration、kernel、statement comparison 和外部依赖审查。最终正文已准确保留这些范围限制。
