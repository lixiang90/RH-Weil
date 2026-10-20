# 固定 Fourier 到完整 Weil 的直接运输：精确负测试与来源止损

2026-10-20。按 root 指定的唯一下一来源门执行；0 轮，不修改 STATE/cadence/Goal，
不建立新数学合同。本文为独立原稿，root 消费阶段须另行登记。
已恢复 README/STATE、check/show、当前 C024 与新 strategy；实际树中 561 草稿及其他
代理输出正在汇合，不把文件已出视为数学消费。固定 G20261014 文本目标和 0c4f/≤538
基线；现场运行 Goal 的观察沿用 root 的 `get_goal=null`，不冒称 active。

## 1. 本门的确切问题与新输入

561 的正向鉴别已给：正 tempered integer-side 测度、固定 Fourier 自对偶与精确单位 gap
可以不预设离散/整数支撑而恢复单位 comb。该命题识别对象，没有支付 zero-side 正测度。
本门检验最直接的下一箭头：**把固定 Fourier 的自伴性通过原范数的酉坐标直接运输，
能否得到非负二次型？** 这是有明确算子的可判测试，不是再给未知正性命名。

源为正半轴 L²(dx) 上的固定 cosine transform；目标为 log 坐标 L²(du)。
不输入 ζ 的零点，不输入完整 Weil 正性，不选择待证正性的未知内积。

## 2. 原范数、固定核和自伴 involution

在 L²((0,∞),dx) 取

\[
(Cf)(x)=2\int_0^\infty\cos(2\pi xy)f(y)\,dy.
\tag{2.1}
\]

精确定义先在 smooth compact core，再由 L² Fourier 变换延拓。
令 `Jf(x)=f(|x|)/√2`，这是到全线 even L² 的酉同构；全线 Fourier 使用
`Ff(ξ)=∫f(x)e^{-2πixξ}dx`，则 `FJ=JC`。因此

\[
C^*=C,\qquad C^2=I,\qquad \|C\|=1.
\tag{2.2}
\]

指定酉映射（注意是 dx，不是 dx/x）

\[
(Uf)(u)=e^{u/2}f(e^u),\qquad
(U^{-1}h)(x)=x^{-1/2}h(\log x).
\tag{2.3}
\]

换元 `x=e^u` 给 `||Uf||²_{du}=||f||²_{dx}`。于是 `H=UCU^{-1}` 满足

\[
(Hh)(u)=2\int_{\mathbb R}
e^{(u+v)/2}\cos(2\pi e^{u+v})h(v)\,dv,
\quad H^*=H,\ H^2=I,\ \|H\|=1.
\tag{2.4}
\]

核为实对称 Hankel 核，依赖 `u+v`。对 compact h，积分逐 u 有普通意义；对全部
L² 输入则按 (2.3) 的有界算子定义，不能把核当绝对可积 Schur 核或无条件逐项求迹。
自伴性来自上述酉结构，未从核的实对称形式直接跳过定义域。

## 3. 精确 −1 方向，且在 compact 原测试空间保负

设 `g_0(x)=e^{-πx²}`。Gaussian Fourier 恒等式和两次微分给

\[
Cg_0=g_0,\qquad C(x^2g_0)=(1/(2\pi)-x^2)g_0.
\tag{3.1}
\]

故固定非零函数

\[
f_-(x)=\left(x^2-\frac1{4\pi}\right)e^{-\pi x^2}
\quad\text{满足}\quad Cf_-=-f_-.
\tag{3.2}
\]

Gaussian moments 另给

\[
\|f_-\|_2^2=\int_0^\infty
\left(x^2-\frac1{4\pi}\right)^2e^{-2\pi x^2}\,dx
=\frac1{16\sqrt2\,\pi^2}>0.
\tag{3.3}
\]

log 向量

\[
h_-(u)=Uf_-(u)
=e^{u/2}\left(e^{2u}-\frac1{4\pi}\right)e^{-\pi e^{2u}}
\tag{3.4}
\]

属于普通 Schwartz 空间 `S(R)`：正端为 double-exponential 衰减，负端及其导数为
`O(e^{u/2})`。因此 `Hh_-=-h_-` 且

\[
\langle h_-,Hh_-\rangle=-\|h_-\|^2<0.
\tag{3.5}
\]

这里 **h_- 不属于 405 的 S_exp**，因为负端未付任意指数衰减；不能把它默认为那个
全局源空间的元素。需要原 compact 源时可以严密修复，而不改变结论范围。

取 real `χ∈C_c^∞(R)`，`0≤χ≤1`，`χ=1` 于 `[-1,1]`，并令
`h_R(u)=χ(u/R)h_-(u)`。则 `h_R∈C_c^∞⊂Dlog`，且
`δ_R=||h_R-h_-||₂→0`。由 `||H||=1`，

\[
\left|\langle h_R,Hh_R\rangle-
\langle h_-,Hh_-\rangle\right|
\le 2\|h_-\|\delta_R+\delta_R^2.
\tag{3.6}
\]

选充分大但固定 R 使 `δ_R≤||h_-||/4`，即得完全解析的负上界

\[
\langle h_R,Hh_R\rangle\le-\frac7{16}\|h_-\|^2,
\qquad
\frac{\langle h_R,Hh_R\rangle}{\|h_R\|^2}\le-\frac7{25}<0.
\tag{3.7}
\]

后一式用 `||h_R||≤5||h_-||/4`。没有扩大频率截断或依赖有限浮点采样。
所以即便把测试限制在原 smooth compact 源类，直接原范数酉运输的自伴 Fourier
二次型也不是 PSD。任何继续的酉坐标变化都保留该负方向；自伴性本身不强迫非负。

## 4. 该负方向不属于 actual Q 的负性结论

`H=UCU^{-1}` 是本门固定 Fourier involution；它不是 560 的 actual Γ 载波/primepower
Weil operator，也不是 Sonin positive projection，更不是 ζ 零点谱算子。
`h_R` 虽在 actual Q 的合法测试域，(3.7) 只算 `q_H(h_R)`，没有任何已付恒等式把它
识别成 `Q(h_R)`。因此本门不声称 actual Q 有负向量、RH 为假或 Goal 方法类门完成。

同样，`(I+C)/2` 确是正投影；以它代 C 是合法而不同的算子。它会丢掉 −1 eigenspace，
若要识别完整 Q，必须支付实际 source range、补空间、signed pole 与费用。
Sonin 条件、联合有限位、非局部 signed 比较、paid infinite-rank/compact 修复均未被
(3.7) 排除。本门仅停止“正 integer-side 自对偶 ⇒ 直接酉运输的 Fourier 型 PSD”捷径。

## 5. 原件核对：405 的关系与 554 的完整正跳已经到哪里

已读原件：

- [405](../../notes/405-f1-adelic-restriction-moments-and-radical.md) §§3–6：
  Gaussian/Poisson actual 源、恒等元常数、真实 Mellin 与双矩。
- [554](../../notes/554-theta-joint-positive-jump-and-adaptive-domain-scope.md)：
  root 原消费范围；其[完整正跳原推导](../2026-10-14/theta-joint-source/positive-jump-calibration-and-domain-gate.md)
  §§1–3、5、7–9；[最强旧与准入审查](../2026-10-14/theta-joint-source/strong-old-and-next-admission.md)。

405 使用

\[
\eta(x)=\pi x^2(\pi x^2-3/2)e^{-\pi x^2},\quad
h=E\eta,\quad g(u)=e^{u/2}h(u)>0,
\]

`g` real-even，`A_±(g)=1/4`，完整 `Q(g,r)=0`。原 h/g 是有非零 pole 矩的关系；
双 pole 零的 principal 为 `(D²−1/4)g`，二者不可互换。该正 g 不是 §3 的 −1 方向。

554 已保 actual `Γ=2θ′`、全部 proper prime powers、原 `du` norm 与 complex cross，
得到所有 `f∈C_c^∞(R;C)` 的 exact identity

\[
Q(gf)=E_g(f)-\int\mu_g|f|^2
+2\Re\{A_+(gf)\overline{A_-(gf)}\},
\quad \mu_g=\tfrac12\cosh(u/2)g>0.
\tag{5.1}
\]

`E_g≥0` 同时包含 actual Γ 的正跳与全部 primepower 的正跳；compact r 的有限相关
不能删除该能量的外窗 degree tail。令 `dπ=8μ_g du`、`b(u)=tanh(u/2)`，则

\[
Q(gf)=E_g(f)-\frac18\left(
\operatorname{Var}_\pi f+|\mathbb E_\pi(bf)|^2\right).
\tag{5.2}
\]

由于 g 在每个 compact 支持上严格正，`r↔f=r/g` 覆盖全部 compact 源；
所以要求 RHS 非负，仍然就是原 full Weil 正性。未付的是有准确阈值的 modified
Poincaré 不等式，而不是正跳能量或 Gaussian 关系的合法性。

554 还已支付原 norm `∫g²|f|²` 与 `μ_g` norm 的区别、global cutoff、合法正 mixtures，
包括 source/window-adapted 与 nonlinear source-adapted 修复。
固定单个 g 的域失败/巨费不能排除这些修复；单靠新写一次 (5.1)/(5.2) 没有新净后果。

## 6. 560 的更强同对象分解必须一并扣除

[560](../../notes/560-joint-finite-place-sonin-primepower-cancellation-and-compact-weil-bridge.md)
§§1、4、6 已给每个先固定 finite F 的完整 actual ε_F∈C₀、ordinary positive trace，
以及原 L²(I,du) 自伴紧误差。每 fixed L 取 F_L 覆盖所有 base primes `p<e^(2L)`，
全部 complex 原 zero-extension Dlog 源满足

\[
Q_L(r)=t_{F_L}(r)-\langle r,K_{F_L,I_L}r\rangle
+2|\langle r,\cosh(u/2)\rangle|^2
-2|\langle r,\sinh(u/2)\rangle|^2,
\quad t_{F_L}(r)\ge0.
\tag{6.1}
\]

本门没有给新的 `K_L` sign/norm/Γ-relative/cofinal/growth/coupling 费用，
也没有改 `∀L逐fixed` 为成长统一性。若从固定 Fourier 识别后只能重新到达 (6.1)，
其正迹是已付资产，未知 signed 紧误差仍是原瓶颈；不能以“终于有正算子”标签计新轮。
最强实际 ζ whole 对照保持 `542+555→557` 的 leading 4/5；§3 的辅助负性不改变它。

## 7. 来源判定、停止与重新准入

**Test 结论：** direct 原范数 selfadjoint Fourier 运输不 PSD；一个精确 Hermite/Gaussian
−1 态及其 compact 负近似已经闭合。这个具体结果纠正“自对偶对象会自动产生正型”的
下一步推理，比仅列“正性尚未知”有可判信息。

**Root 可消费范围：** 不再允许直接把 Fourier 自伴性当作完整 Weil 正性来源；
保留 (5.1)/(5.2)、Sonin positive trace、paid/非局部/signed/adaptive 修复。
本结果是 canonical involution 的既有 Hermite 机制，不是新实际算术输入，
不登记为新的数学合同或新的成长 whole 进展。本文与 561 的对象识别共同说明：
恢复整数可以做成严格纯分析分类；识别后的完整正性责任没有因此消失。

**停止：** 已执行唯一来源门，扣最强旧后，只剩 554 modified Poincaré 或 560 `K_L`
signed 责任，故来源入口在此 0 轮关闭。不能继续新建“Gaussian positivity”合同，
不能只换 remainder/transport 名称串行展开。无待跑 producer/数值进程。

**重新准入需至少一项具体新证据：** 独立于未知零点的 full-source 不等式，确切实际
receiver/range 上的新 signed 费用，或允许 paid/source-adapted/非局部修复后仍成立的
严格必要费/覆盖反例。届时先冻结原对象、norm、全部 pole/pp、成长量词及扣 4/5 后
净后果；当前未有这些证据，不预建下一 math contract。

## 8. 根消费的短前件记录

| 项目 | 已闭合/未付 |
|---|---|
| map | `U:L²(dx)→L²(du)` 酉；`C` even Fourier；`H=UCU⁻¹` 有界自伴 involution |
| source/domain | `f_-∈L²(0,∞)`；`h_-∈S(R)` 但非 S_exp；`χ_Rh_-∈C_c∞⊂Dlog` |
| signs | `Ch_-` 不使用（域不同）；正确为 `Cf_-=-f_-` 与 `Hh_-=-h_-`；compact q_H 严格负 |
| actual coefficient | H 核 `2e^{(u+v)/2}cos(2πe^{u+v})`；Gaussian 常数 `1/(4π)`；负 norm `−1/(16√2π²)` |
| errors | compact L² tail `δ_R→0`；有界 H 给显式 `2mδ+δ²`，无需高频/零点数据 |
| coverage | q_H 负测试覆盖本门 H；无 `H=Q` 或 q_H→q_Q 比较，不能消费 actual Q 负性 |
| strongest-old | 405/554 已有关系与正跳完整式，560 已有正迹−紧误差；whole 4/5/core/Ξ 均未变 |
| stage/cadence | 独立来源原稿；root 另审；0 轮止损，无公共状态写入 |
