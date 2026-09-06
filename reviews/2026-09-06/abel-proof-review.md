# 独立复核：Abel 质量预算障碍稿

审查者：只读子代理 Lagrange；日期：2026-09-06。以下保留返回报告，包含实际版本与复跑范围；整改处理另记。

复核结论：**主证明链可接收，当前稿件应作小修后作为 GOAL 第十节的先行材料。** 在明确的截断范围与“所有充分大实尺度”量词下，未发现推翻定理 1.1、6.1–6.2、7.2、8.2 的计算错误或 RH 循环依赖。发现一处需要补足的推论假设，以及摘要、解析性说明和复现记录的几处不足。本次不认证新颖性，也不代表整个 GOAL 第十节已经完成。

审查日期：2026-09-06。审查对象为[论文源稿](F:/codex-build/RH/RH-Weil/papers/abel-mass-obstruction-paper.tex)全部 833 行；页码对应现存 10 页 PDF：:codex-file-citation{path="F:/codex-build/RH/RH-Weil/output/pdf/abel-mass-obstruction-paper.pdf" purpose="source"}。读取了 notes261–264、283，以及下述脚本；没有把 README、状态标签或旧审查结论作为正确性前提。

版本记录如下，源稿和 PDF 的首尾哈希一致：

```text
仓库 HEAD：
483ded56401cd174252ef630ed22dd4ab86956ad

源稿 SHA-256：
77DDE8ED47E62119D5173ED0B0ED749E727FBAB0CF97E25D5F1FA3FBE16794CF

现存 PDF SHA-256：
3B2AF9045C6AD23FE3457918EE44CCBFD133F01BE7D917FB73C44EE52897FEC4
```

**证明与依赖核对结果如下。**

| 位置 | 核对结果 |
|---|---|
| §1–2，页1–3：定义与 Brownian 能量 | 两源在同一端点截断，偶对称的半权与中心质量一致；\(p,c,r\) 均为零质量测度。固定 \(Y\) 时源具有所需绝对对数矩，卷积能量有限。距离核的 \(-1/2\)、Fourier 的 \(1/(2\pi)\)、minimum kernel 的 \(1/2\) 均正确。连续通道保证 \(D>0\)。 |
| §3，页3–4：Mellin 恒等式 | 初始绝对收敛域 \(\Re s>1-\sigma\) 正确；连续源从 \(1\) 开始，恰产生 \(1/(\sigma+s-1)\)。zeta 在 \(1\) 的主部抵消，正实轴无零点；非实零点对应留数 \(-m_\rho\Gamma(\rho-\sigma)\ne0\)，没有漏掉重数或 Gamma 抵消。 |
| §3，页3–4：Landau 振荡 | 删除有限初始区间得到整函数修正。假定最终同号后，非实极点迫使收敛横坐标 \(c\ge\Re\rho-\sigma>0\)，与实点 \(c\) 全纯矛盾。Taylor–Tonelli 论证成立，不要求存在最右零点。由连续性得到无界质量零点序列。 |
| §4、6，页4–6：孤立素数原子 | Bertrand 的整数形式在 \(\lfloor Y\rfloor\)、\(\lfloor Y/2\rfloor\) 的使用有效。\(N<q^2\) 排除了 \(q^2\) 等因子；总 \(q\)-赋值为3强迫三个正向 \(q\)，中心项及负向项不能抵消。原子系数确为 \(a_q^3/8\)。 |
| 同上：间距与连续背景 | 对其他位置 \(\log(u/v)\)，确有 \(\min(u,vq^3)\le N^3\)，故间距下界有效。密度界、隔离长度和跳跃能量给出 \(J_4\gg Y^{-9}L^{-7}\)，以及 \(J_4\gg Y^{-6}N^{-3}L^{-1}\)；各指数核算一致。后者的常数和起点独立于允许范围内的 \(N\)。 |
| §5–6，页5–6：有限截断尾与微扰 | 递减尾积分比较有效。未截断根处的有限质量由遗漏尾控制。连续非减 \(\Phi\) 保证 \(\lfloor\Phi\rfloor\) 在每一点右侧有常值区间，包括整数阈值；可在该区间内任意小地避开固定 \(N\) 的孤立质量零点。无需任何统一的区间宽度下界，也没有偷用响应的截断连续性。 |
| §7，页7：统一矩估计 | \(S\asymp Y^{1-\sigma}\)、\(D\asymp LS^2\)、\(Q_1\ll Y^{2-2\sigma}L\)、\(Q\gg Y^{1-2\sigma}L\) 及 \(Q_1\ll YQ\) 成立，统一于有限 \(N\ge Y\)。包括 \(\sigma\ge1/2\)；证明未错误假设 \(Q\) 必须由大素数占主导。 |
| §7，页7–8：局部间距均值 | 频率集确为 \(\{0,\pm\log n\}\)，相应系数为 \(-M,a_n/2,a_n/2\)。因此主项是 \(U(M^2+Q/2)\)，误差为 \(O(Q_1+M^2)\)。\(U=K_\sigma Y\) 可统一吸收误差；不需要 \(U\gg N\)。 |
| 同上：连续项及响应下界 | 连续 lag 密度截断后零延拓的总变差至多为其最大值的两倍，包含两端跳跃。因此 \(\int_I|C|^2\ll Y^{2-2\sigma}/U=o(UQ)\)。保留连续物理通道与质量中心项后，得到 \(J_{4,I}\gg (Q+M^2)^2/(YLS^4)\gg L/Y^3\)。 |
| §8，页8–9：有符号尾与对数截断 | \(-w(N)R(N)-\int_N^\infty Rw'\) 的符号及右连续端点正确；尾是严格 \(n>N\)。对 \(h=N/Y\ge1\)，得到 \(Y^{1-\sigma}h^{1-\sigma}e^{-h-d\sqrt L}\)。\(h^{1-\sigma}e^{-h}\) 的单调性允许任意大有限 \(N\)，没有暗加上界。 |
| 同上：定理8.2的边界 | 选择 \(b<d<c_*\) 后，最终比值下界为 \(L^{1-(1-\sigma)\kappa}e^{\kappa(d-b)\sqrt L}\to\infty\)。\(c=3/4,\kappa=4\) 时用固定 \(b>0\) 吸收取整误差的说明正确；不能直接使用 \(b=0\)。 |

**具体问题与修复建议：**

1. **推论7.3应显式补上 \(N\ge Y\) 和渐近尺度假设。**  
   位置：页8，[源稿631行起](F:/codex-build/RH/RH-Weil/papers/abel-mass-obstruction-paper.tex:631)。

   “On any actual schedule”若脱离前一定理独立理解，范围过宽。取 \(\sigma=1/4,\ N(Y)\equiv2\)，则
   \[
   M(Y,2)\longrightarrow
   (\log2)2^{-1/4}-\int_1^2x^{-1/4}\,dx<0.
   \]
   因而质量趋于非零常数。另一方面，Young 不等式给
   \[
   J_4\le \left(\frac{\|r\|_{\rm TV}}S\right)^4\le16,
   \]
   所以某个最终预算 \(J_4\le C\mu^4\) 成立；但推论要求 \(|M|\gg(\log Y)^{1/4}\)，不成立。

   这不否定按上下文继承 \(N\ge Y\) 后的推论。建议改为明确的序列表述：固定 \(\sigma\)，令 \(Y_j\to\infty\)、有限整数 \(N_j\ge Y_j\)、\(M_j\ne0\)，再陈述必要下界及其逆否后果。

2. **摘要应统一截断对象及其正则性。**  
   位置：页1，[源稿28–54行](F:/codex-build/RH/RH-Weil/papers/abel-mass-obstruction-paper.tex:28)。

   当前“continuous nondecreasing cutoff functions”与紧接着的取整截断容易混淆。应明确写成
   \[
   N(Y)=\lfloor\Phi(Y)\rfloor,\qquad
   \Phi\text{ 最终连续、非减}.
   \]
   同时，摘要的“每个有限 cutoff”比定理7.2的“有限整数 cutoff”字面范围更宽。可以统一限制为整数；也可以明确把定理7.2扩至实 \(N\ge Y\)，其现有证明实际上同样适用。摘要的无上界超对数截断结论由定理8.2支持，应明确引用，避免误认为仅由带 \(N\le Y^2/8\) 的定理6.2推出。

3. **实解析性的理由可以补成明确的复解析论证。**  
   位置：页4，[源稿278行](F:/codex-build/RH/RH-Weil/papers/abel-mass-obstruction-paper.tex:278)，以及页5的固定截断微扰。

   “局部支配逐阶微分”本身首先说明光滑性。这里补证明很容易：令 \(z=1/Y\)，在 \(\Re z>0\) 的紧子集上，相关和与积分由 \(e^{-cn}\)、\(e^{-cx}\) 支配，故定义全纯函数；复合后得到 \(Y>0\) 上的实解析性。固定 \(N\) 更直接。此处是可立即补齐的说明，不是新的算术缺口。

4. **数值复现说明缺少截断参数。**  
   位置：页10，[源稿774行起](F:/codex-build/RH/RH-Weil/papers/abel-mass-obstruction-paper.tex:774)。

   文稿列出 \(\sigma,Y\) 和“全部为负”，却未写具体 \(N\)。本次重现的是 \(N=40Y\)；脚本默认值则是 \(25Y\)，均不是主定理的 \(\lfloor Y(\log Y)^2\rfloor\)。建议在正文补全命令、截断参数、软件版本和样本数，并保持目前已有的浮点误差边界声明。

5. **一手引用及审查记录应补齐，但不应标成未证数学假设。**  
   位置：页2、9–10，[源稿132行](F:/codex-build/RH/RH-Weil/papers/abel-mass-obstruction-paper.tex:132)、[764行](F:/codex-build/RH/RH-Weil/papers/abel-mass-obstruction-paper.tex:764)。

   临界线零点存在性目前仅引 DLMF。它是可靠手册入口，但并非原始证明；若按 GOAL 的一手材料标准验收，应增加 Hardy 原文。Lemma7.1 的 Chebyshev 上界及定性 PNT 也宜给准确入口。页10笼统的“独立审查已检查”应附版本、范围及实际复跑记录。

**外部文献的实际核查范围：**

| 输入 | 本次核查范围与结论 |
|---|---|
| Montgomery–Vaughan，*Hilbert’s inequality* | 核对印刷页74的 Theorem2、Corollary2式(1.9)，视觉读取公式；核对页75的 \(|\theta_2|\le1\) 和页82由两个双线性形式导出的说明。误差确可取 \(3\pi\sum |d_j|^2/\delta_j\)，允许任意有限互异实频率和复系数；平移只改变相位。没有重做其全部 Hilbert 不等式证明。[作者存档](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf) |
| Mahatab–Mukhopadhyay v4 | 核读 Theorem3.1 的最终同号、分段连续、初始绝对收敛及实轴解析延拓条件。稿件使用的是自行证明的 Landau 机制，没有借用该文更强的振荡测度结论。[固定版本正文](https://arxiv.org/html/1512.03144v4) |
| Fiori–Kadiri–Swidinsky v3，2023-05-17 | 核对页1–3的 \(\psi\) 定义、Corollary1.4、Remark1.5，以及页17–18相关分段覆盖与推论证明。原界为 \(9.22022x(\log x)^{3/2}e^{-0.8476836\sqrt{\log x}}\)，适用于 \(x>2\)；取严格 \(d<c_*\) 吸收对数因子正确。其上游包含已验证的有限高度 RH 数据及数值计算；本次未复跑这些证书，也未逐页比对期刊终版。[v3原文](https://arxiv.org/pdf/2204.02588v3) |
| Erdős，1932 | 核对原文页194及197–198的整数 Bertrand 结论，确认稿件的实 \(Y\) 取整应用满足范围；未重新认证原文全部有限素数清单。[原文](https://www.renyi.hu/~p_erdos/1932-01.pdf) |
| Hardy，1914 | 核对原文页1012的定理声明转录，确认其给出临界线上无穷多个零点，强于本文所需的存在性；未重做全文证明。[原文页转录](https://fr.wikisource.org/wiki/Page:Comptes_rendus_hebdomadaires_des_s%C3%A9ances_de_l%E2%80%99Acad%C3%A9mie_des_sciences,_tome_158,_1914.djvu/1014) |

循环性方面，零点假设仅用于产生质量振荡；响应下界及 PNT 尾估计均独立于该假设。FKS 使用已证明的有限高度验证，不等于假设完整 RH。固定 \(0<\sigma<1/2\) 时障碍无条件；\(\sigma=1/2\) 时所得是“指定连续尺度预算蕴含 RH”，没有逆命题。所有常数允许依赖先固定的 \(\sigma,\kappa,b,d\)，没有证明趋近参数边界时的一致性。

notes263 的正源绝对尾证书障碍、notes264 的局部能量比较、notes283 的固定比例截断振荡，**均不是本文主链必需依赖**。本文也没有把它们混合使用：特别是 note283 的 \(M(Y,Y)\) 有算术跳跃，其正负值不能直接通过介值定理变成本文所需的未截断质量根；该笔记的显式公式上游及 Littlewood 输入不在本次完整认证范围内。

**复跑记录：**

- 运行 `abel_prime_atom_audit.py`：24 个案例、126 个原子系数、567180 个有理间距检查全部通过。它核对有限支撑和有理权重的代数结构，不认证渐近密度估计。
- 运行 `abel_mass_discrepancy_probe.py --tail-factor 40 --skip-e1`：48 个样本全部为负；\(\sigma=1/4,1/2,3/4\)，\(Y=2^3,\ldots,2^{18}\)，\(N=40Y\)。使用 `C:\Python314\python.exe`、NumPy 2.5.2、mpmath 1.3.0；longdouble 的显式尾数为52位。捆绑 Python 缺少 mpmath，改用现有系统环境成功复跑。
- 阅读了 `prime_jump_full_response_probe.py` 的源代码及归一化；未重跑其频率积分和50位小案例。未运行 note283 的全整数扫描，未重编 PDF。以上数值结果均不参与渐近证明。

就 [GOAL 第十节](F:/codex-build/RH/RH-Weil/goals/GOAL.20260906.md:204)而言，本报告可作为第4项“关键证明独立复核”的记录；完成上述小修、文献比较和复现记录后，该稿可承担第3项先行材料。其独立贡献与优先权仍待主代理判定，函数域模型、其他纠错项、归档及远程同步不在本次验收范围内。

本次未修改任何仓库文件，未 commit、未 push。
