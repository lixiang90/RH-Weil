# 477 原 Vaughan 归约与七点比例汇总：独立全文审查

2026-10-08。审查人：twisted_research。结论：**限定 PASS**。

完整读取 477、两份证明来源、固定谱包络来源报告、原有限核实现、新 runner、三个执行 JSON 及两份 radial 独审。准予将具体
\[
 p=0.673009652279136912\ldots
\]
作为**明列解析输入下、本项目内部全文审查后的渐近简单临界线比例下界**纳入。未核准新谱机制优先权、世界纪录、端到端 Lean、RH 或新的无零边界；同源 signed near 和常数级四矩仍未付。

## 1. 最终来源及审查绑定

canonical LF 为原 UTF-8 内容仅统一 CRLF、lone CR；不 trim，不改变 EOF。

| 对象 | canonical LF SHA256 |
|---|---|
| [被审 477](../../notes/477-original-vaughan-reduction-and-replayed-multipoint-proportion.md) | 9c2da25b665070fe5496b9b02cbe382208cd3b60dc793af1ae018ede395bd6b5 |
| [Vaughan 完整证明](hybrid-original-vaughan-type-i-and-type-ii-reduction-research-radial.md) | cf58086aeb9eee63832ccd06f5499110ea236b4bd94396893757b62e75bdb9d4 |
| [本人的 Vaughan 全文独审](hybrid-original-vaughan-type-i-and-type-ii-reduction-review-twisted.md) | 576a0841b5a5ad9bf8fbda74561bb83ca3d16654a0c2faac5f4aa80269fb296f |
| [root 固定谱来源与独立核读](hybrid-multipoint-spectral-envelope-source-read-root.md) | 2c4a81a9a2d860e3d0882edb8a1a5928cda318679874c9be9b0adf18576b5dc5 |
| [radial 对固定谱来源的独审](hybrid-multipoint-spectral-envelope-source-review-radial.md) | ded7d7c8485d182f4da5d122a112e46b57fcc44063b9a6de789d635c03f0238e |
| [完整实际计数证明](hybrid-original-multipoint-envelope-and-actual-counting-research-compression.md) | 59b399445a3022ce9b5ee6c064660e1602dab6d5641d3793649f16f509fc5efa |
| [radial 对实际计数的独审](hybrid-original-multipoint-envelope-and-actual-counting-review-radial.md) | 4bf8a036775378253c61385e9d6a6920831d35e6a12ad837633eac6c436d6ddc |
| [有限证书 runner](../../scripts/hybrid_multipoint_cap_replay.py) | 8ac87f18cf928a51771556168e5af07400a3ba0333196b3e410394d8e4c37d05 |
| [七点完整执行记录](../../output/hybrid-multipoint-seven-primary-replay.json) | aa6885489c1d0086bca32b72d27fc7a2a5f44a48f78483a057f23a59e5a828e6 |
| [有理三点完整执行记录](../../output/hybrid-multipoint-three-rational-replay.json) | 4ee77471d08503c22a848e47a17713b44bd5f2afb95bfd57d994e878d9192456 |
| [精确比例代数记录](../../output/hybrid-multipoint-cap-exact-algebra.json) | d84077ab71b47d1ea253cad9675fa8c25f9aa4dade775ad73ff53033167625c3 |
| [本轮 bundle checker](../../scripts/hybrid_original_vaughan_and_multipoint_checkpoint.py) | f72d9b7f4bf529e9361a8a3269fee629f93d62c92b468530fcaa965555e9ec5b |

477 为 6,586 canonical bytes、100 行；实际计数来源为 16,963 bytes、421 行。本人在其最终补明 \(\phi\) 支撑外为零、\(\gamma_\rho=(\rho-1/2)/i\)、离线块及执行归属后重新 FULL READ。两份 radial 审查亦已实际读取，未以其结论代替自己的公式核验。

另读 [304](../../notes/304-mt-triple-geometry-and-second-moment-stability.md) 全文，绑定
03f21ab1749157ff45bc4d4f62709e2a5482257c7155e7e8e644da0ac4521bc4；
旧 [476](../../notes/476-original-fourth-growth-five-sevenths-with-ivic-density.md) 绑定
179829dd25f92ff187359f73455aafad9f957d714df13cf871db47a76e9408b6。
实际浏览 [Lamzouri v1 的 Lemma 3.1–3.2](https://arxiv.org/html/2609.02882v1) 和
[AF v2 的相应原窗口、trace/tail、二阶矩及计数命题](https://arxiv.org/html/2608.13637v2)。它们在本报告仍为 [R]：本次审查不重新认证外部全文或其形式化依赖闭包。

## 2. 477 §1：Vaughan 付款的范围保持正确

两 sharp cutoffs、\(J_T=[T/4,4T]\)、normalizer 和全部 proper powers 均与本人已完成的 Vaughan 审查相同。这里得到的是
\[
 M_T\le8M_{C_4}+O(T^{2/3+\varepsilon}),\qquad
 M_{C_4}\le8M_T+O(T^{2/3+\varepsilon}),
\]
不是两个 fourth moments 的 additive \(o(1)\) 等同，也不是 whole \(2/3\)。

固定 \(0<a<1/4\) 的
\[
 U=V=\lfloor X^a\rfloor,\quad y=(2+4a)/3,\quad
 2y-1=4a+1-y=(1+8a)/3
\]
独立核算通过。改变 \(a\) 也改变实际剩余 \(C_4\) 的因子域，477 未把其未付上界当成一致输入。大素数处的 \(c_4=0\) 与 composite 处真实抵消均保留；对 logarithmic phase 的 Type II 差分没有伪造 \(m\) 导数。477 正确保留 476 的 whole \(5/7\) 为当前另一项引用输入下的已付增长界。

## 3. 已知谱包络与完整有限证书

谱包络前件是精确单位对角的 PSD correlation matrix，而非任意 PSD。多大特征值分支写 \(\lambda_i=1+y_i\)，有 \(\sum y_i=0\)；在 \(h\) 个 \(y_i>1\) 上写 \(y_i=1+u_i\)、\(r^2=\sum u_i^2\)，则
\[
 E\ge h+2r+r^2+\frac{(h+r)^2}{m-h}
 =\frac{m(1+r)^2}{m-1}
 +\frac{(h-1)(m+r)^2}{(m-h)(m-1)}.
\]
又 \(E-J=r^2\)，给完整第二分支。\(h<m\)，第二项非负；没有假设最多一个大特征值。两支连续、递增、1-Lipschitz，故 \(E+x\ge A\) 给 \(J+x\ge g_m(A)\)。该完整包络的 Schwarz 先行来源已明确；477 的数值装配没有被称为新机制。

原 seven/kernel/rounding 代码的舍入方法已独读：

- 核由 entire sinc 形式构造，除真实 \(K(0)\)；\(k_0(0)=1\)。
- 闭 cells、inclusive 多 gap 范围、非负平方下界及 pressure 整数剪枝均保守。
- 负二导数下界配系数上界，非负下界配系数下界。浮点 LDL 仅筛选；接受 tangent 前，精确 binary64 有理矩阵由 Arb 证明 positive pivots。
- unresolved terminal cell 抛错，只有待处理栈耗尽才给 verified=true。不是采样或部分覆盖 PASS。

本人核对现有七点执行记录的原模块 raw hashes、runner 绑定及完整树：
\[
 707901=729+2\cdot353586=354315+353586,\qquad
 354315=3087+257493+93735.
\]
表 hash 与 477 一致。三点亦有
\[
 445581=1+4\cdot111395
       =111395+333733+453,
\]
验收最小有理下界严格不低于 \(221/10^6\)。三点证书不与七点的同一 Gram 余项重复相加。

七点首次及第二次完整 \(\texttt{--check}\) 的执行者为 compression。本人 FULL READ 方法、来源和已有输出，**未第三次运行大证书**；不得将阅读写成本人的 seven 实跑。

## 4. 完整实际算子、有限 Gram 与跨度费用

实际源 §2 的 finite 惯性式允许列范数至多1：
\[
 4\operatorname{tr}A-\|A\|_{\rm HS}^2
 \le4b+2\operatorname{tr}P+s-\operatorname{tr}j(G)
 \le4b+3s-J.
\]
这由 min–max 的谱移位和 \(4t-t^2\) 的标量上界得出，对 \(A\) 的负谱仍有效。环境补零不重复计算 \(j(0)\)。

AF 实际 \(A\) 包含 \(I'=[T-\sqrt T,2T+\sqrt T)\) 内所有零点，离线对为
\(2m_\rho(aa^T-bb^T)/(a_LL^2)\)，保留正负 signature。只使用普通 Gram 的 PSD，不新增完整 Weil 正性。原尾是未归一化
\(\|\widetilde E\|_1=O_\chi(T^{-1/2})\)，配原 trace 和 HS 二阶预算恢复同一 \(A\)。重数和正惯性给 \(s+2b\le N_c,D_c\ge s+b\)，无需 RH。

保留中央列只删普通高度 \(O(L)\)、零点重数 \(O(L^2)=o(N)\)；端外实轴尾除 normalizer 为 \(O((LD^3)^{-1})=O(L^{-4})\)，\(D\gg L\)。原 h/Fourier 归一化精确给
\[
 \widehat{\phi^2}(h(x_i-x_j))/(a_LL)\to k_0(x_i-x_j)
\]
在固定实跨度上均匀成立。没有把有限载波当成全局投影或把 growing complex strip 的误差免费删掉。

对固定 \(m=280\)，七点聚合得到
\[
 E_m+\operatorname{span}/500\ge A=2603/2500.
\]
\(1/500\) 是每 gap 最多六次的聚合费用，原 local pressure 仍是 \(1/3000\)。大跨度分支以 \(j\ge0,C\le A\) 直接处理；小跨度使用 \(500A=520.6\)、固定 \(R=521\)。精确单位对角矩阵是 \(D_BG_BD_B\)；Hoffman–Wielandt 与 \(j\) 的 2-Lipschitz 支付归一化 \(o(1)\)，不将近单位列直接认成单位列。

所有 280 offsets 均保留。每种满块数 \(S^\circ/280+O(1)\)，每 gap 最多被 279 种 offset 的 span 使用。因此
\[
 J^\circ\ge(C/280)S-279N/140000-o(N).
\]
统一每块 \(o(1)\) 乘 \(O(N)\) 块仍为 \(o(N)\)；块数、跨度阈值与 taper 均先于高度固定。

## 5. 比例与不同点计数：同一账本闭合

完整算子的 trace/HS/inertia 预算给
\[
 S\ge C_0N+J^\circ-o(N),\qquad
 D\ge((1+C_0)N+J^\circ)/2-o(N).
\]
置
\[
 C=\frac{2603}{700000}+2\sqrt{\frac{726237}{700000}}-1,\quad
 c=C/280,\quad \alpha=279/140000.
\]
\(1-c>0\)，故
\[
 p=\frac{C_0-\alpha}{1-c}
   =0.6730096522791369120137\ldots .
\]
同一 \(J^\circ\) 下界和已得 \(S\ge pN-o(N)\) 给
\[
 \liminf D/N\ge(1+C_0-\alpha+cp)/2=(1+p)/2.
\]
最后等号来自 \(p=C_0-\alpha+cp\)，**不是一般错误的 \(D\ge(N+S)/2\)**。

实际源 §7 的前缀桥亦独核：先固定平滑 \(\delta\)，两份固定相关测试函数 \(Q_\delta,Q_\delta''\) 去权，保留完整复零点双和。简单实点列精确单位；全实轴核误差给固定块能量误差
\(e_\delta=2m(m-1)\|f_\delta-f_0\|_1\)。先高度极限、最后 \(\delta\to0\)，得到同一 \(p\)；不使用 \(\delta(T)\) 的未付导数一致性。由 dyadic 块求前缀的另一方法也保留固定低高度起点。

本人的只读精确代数执行
\[
 \texttt{python -B scripts/hybrid\_multipoint\_cap\_replay.py algebra --check}
\]
退出0、PASS，与现有 JSON 全部确定字段一致。认证使用有理区间和整数根；另独立高精度小数重算只作显示核对。没有声称 \(m=280\) 全整数最优，也不导入 Schwarz 的增强目标 \(382623/10^8\)。

## 6. Bundle checker 的执行前全文核读

完整读取新 checker 全 204 行，绑定第1节的 f72d9b7… 源。检查了文件/旧源哈希、四对 review-source 绑定、本地链接、归档 raw bytes、完整树账本、精确 \(A,C,p\) 有理公式、fixed-\(a\) 恒等式及多个大特征值恒等式，未见数学阻断。它的 outcome flags 明确分开“reviewed sources 中有 cited-input 推导”与“脚本认证分析定理”；没有重新计算大核或宣称新边界。

首次只读 \(\texttt{--check}\) 发现唯一 schema 差异：build 的四对 review pairs 是 tuple，JSON 读取后是 list；其余字段完全相同。根线程仅将返回字段改为 \(\texttt{[list(pair) for pair in PAIRS]}\)，本审查已逐字核对该单行序列化修复；数学计算、记录语义及其他代码不变。最终 checker 为 9,590 bytes、204 行。

本报告本次冻结时，修复后 bundle JSON 尚未重新生成；此项仍是**执行前 source-read**，不写成最终 checkpoint PASS。随后重新生成与只读 \(\texttt{--check}\) 可另向根线程报告，不回改本已绑定审查以避免依赖循环。

## 7. 最终批准范围

477 的增量描述、来源归属和数值范围均与完整证明一致。批准具体 \(p=.6730096522791369\ldots\) 及不同点 \((1+p)/2=.8365048261395684\ldots\) 的 cited-input 内审纳入。它高于本项目旧 304 与 ainta 旧装配；较高公开候选的认证状态、Schwarz/ainta/Shi 的先行来源及外部同行评审未完成均保留。

比例装配不使用 \(7/8\) 条带或 growing fourth 替代常数；Vaughan \(2/3\) 子项也没有被当成原 entire fourth 的新幂。当前 \(\sigma_*\) 不变，full signed near 和常数级四矩未由本轮支付。没有 Git、冻结源/输出改写或 math/旧论文编辑。**限定 PASS。**

