# 分布化 Beurling–Weil 思路与本项目后续选择

2026-10-27；用户要求结合附件与本项目旧研究思考 Weil 猜想类比路线。本稿是来源纠错、旧资产去重和战略比较，0 数学轮；同 G20261014、冻结 0c4f／≤538，不创建运行 Goal，不重新准入已停止的 C045。附件中的安排是讨论对象，不是用户授权的新指令。原附件不改。

审读原件为 [附件接口核查](../../reviews/2026-10-27/distribution-beurling/document-audit.md)、[独立路线比较](../../reviews/2026-10-27/distribution-beurling/route-comparison.md)；[fresh 修后限定 PASS](../../reviews/2026-10-27/distribution-beurling/fresh-review.md)已由 root 实际核读，三稿的 Deligne 净误差充分条件及连续 primitive 参数范围已对齐。本稿与三独占输出的来源／战略范围前件闭合；这不认证新的经典输入。

## 1. 判断：优先迁移正号的来源，避免重复建立已有解析包络

附件最有价值的贡献是把 Euler／Mellin 对偶／显式公式与独立正性／纯度分层，并把正迹、对应极化和 Deligne 放大分成不同证明接口。这有助于选路，但附件没有提供此前缺失的经典算术输入。

本项目的重点应保留在**同一算术对象上的源、关系、乘法与 mixed 容量**。一般 g-system、对偶、正核例子、紧修正、局部 Weil 稳定域和实际 Green 源已具备较具体的版本。继续扩大这类设施，若不改变其接入经典完整 Weil 型的箭头，不足以推进当前瓶颈。

推荐次序是：

1. 几何主线：实际非零 primitive 载体上的 relative principal／Green cocycle 和物理源比较；随后才是整过滤、截面 lift／乘法、mixed RR 与完整 Weil 身份。
2. 分析备选：独立正对象对完整经典分布的逐测试逼近，或新的正压缩与完整 signed 余项估计。
3. 放大备选：只有出现实际非平凡 tensor 对象及全局 pole 定理时，才启动 Deligne 型路线。

这是投入选择，不是证明第二、三路不可能。当前没有新载体或新公式可付第一步，故本次不预建 C046，也不把写下接口称为研究已经启动。

## 2. 先修正附件三个会改变目标的公式

### 2.1 所有素数幂必须保原权

附件定义 \(\widetilde\pi=\sum_{m\ge1}m^{-1}D_m\pi\)、\(Z=\exp\mathcal L\widetilde\pi\)，则直接求导给

\[
 -Z'/Z=\mathcal L\lambda,\qquad
 \lambda=u\widetilde\pi=\sum_{m\ge1}\frac{u}{m}D_m\pi.
\]

附件的 \(u\sum_mD_m\pi\) 会使 \(p^m\) 的系数成为 \(m\log p\)，而经典目标是 \(\log p\)。不能用该错误测度接入本项目的完整 prime-power 预算。

### 2.2 自相关、Mellin 中心与物理范数须相容

按附件字面 \(h(x)=\int g(xy)\overline{g(y)}dy/y\)、\(\widehat g(s)=\int g(x)x^s dx/x\)，实际是

\[
 \widehat h(s)=\widehat g(s)\overline{\widehat g(-\bar s)},
\]

不是 \(1-\bar s\)。可以保 Haar 自相关而改用中心化 Mellin \(x^{s-1/2}\)，或保原 Mellin 而改成 \(g^*(x)=x^{-1}\overline{g(x^{-1})}\) 的带权对合。主线沿用项目 \(r=e^{u/2}f\)、\(r^*(u)=\overline{r(-u)}\)、原 du 及 zero-extension Dlog，不能无声改 norm。

### 2.3 Frobenius 只能归一化一次，且 H1 零点方向要正确

若 \(\Phi\Phi^\vee=q1\)，则应写 \(P_1(q^{-s})=\det(1-q^{-s}\Phi)\)；若用 \(U=q^{-1/2}\Phi\)，则写 \(\det(1-q^{1/2-s}U)\)。附件把第二式的 U 换成未归一化 Φ，会把奇性移到实部 1。曲线 H1 因子在分子，H0/H2 在分母，取逆不能继续称同一零点因子。[Deligne I §1，式 1.14.3](https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf)给出分次行列式的实际符号。

还须限定：正测度在 0 附近要付对数矩；有限零点组可分离不支付无限尾；一般只能推出半正，严格正需另排核；正则化迹不自动有普通迹的正性。附件 A/B 可修成充分接口，不能据此认证它们的经典实例存在。详细计算和算子域见独立审读稿。

[Hilberdink–Lapidus Theorem 3.2](https://arxiv.org/pdf/math/0410270)要求具体的两端衰减、带内有限极点及一致竖向趋零；单说多项式增长不能直接援引。该定理对离散系统的结论也不是对任意连续测度的无前件函子定理。函数域须另保周期型解析类别、全部 endpoint 副本与 aliases。

## 3. 扣除已有资产后，真正剩什么

| 附件任务 | 本项目已付 | 当前剩余责任 |
|---|---|---|
| 找连续非经典正核实例 | 562／563 已有正 continuous primitive 族、完整分布 ODE 与守恒正能量证书；同族另有负段 | 新玩具正例不能代经典完整源身份 |
| 把固定窗写成正部减紧算子 | 560 已有所有 fixed 窗、全部 complex 原域的真实正迹减紧误差及双 pole；570 有实际 joint signed 比较 | cofinal 低频／符号／共同原费与 coupling |
| 构造对应、transpose、复合和 trace | 567 对真函数域恢复 RR→Hodge→完整 mixed Gram；continuous ± 也有形式对应而符号不同 | 同一经典源对应的独立容量／有效性 |
| 正对象逼近经典 | 576 真函数域正原料生成与原 alias 费用；577 真 Γ/contact 正修补与完整费用 | 从经典原数据独立构造趋零的完整 signed 缺陷 |
| 大局部作用域／更多 Green 信息 | 581／582 有实际强域、完整局部作用、全源可见的额外 native Green family | 405 全关系尚非 principal；q7 fixed coarse native primitive 为零；全局几何与混合身份未付 |
| 找自伴生成元／普通热迹 | 562–566 已区分正型分布、GNS、带重数 trace 与 determinant；函数域全 time／全 winding 身份已核 | 经典独立能量、原源身份、全谱可见性／重数及尾部运输 |

最强实际经典后果仍是 [542＋555→557](../../notes/557-joint-row-norm-and-gamma-arithmetic-moment-budget.md) 的 whole 负惯性上预算：其对数主项系数至多 4/5；这是仍允许巨大负谱维数的上界，不能写成 4/5 的正性比例、负谱下界或 RH。

与它并存的 [560](../../notes/560-joint-finite-place-sonin-primepower-cancellation-and-compact-weil-bridge.md) 给每个先固定 L 的完整

\[
 Q_L=t_{F_L}-\langle r,K_{F_L,I_L}r\rangle+\mathrm{Pole}(r),
 \qquad t_{F_L}\ge0,
\]

但 fixed-L 紧性并不支付成长 K 的 sign／norm。高频安全层已有强旧合成，当前缺口是完整低频／核心及补空间的共同比较。附件的“正部减紧修正”应从这里起步，不能从零建立同名表示。

## 4. 几何主线：把“平方”收缩为一个可否定的同对象任务

函数域最可迁移的证明片段是：真实截面的乘法与有限容量，结合 RR 的二次项和有效性的 degree 约束，排除 primitive 正自交；再由图交数身份得到全部 mixed Weil 正性。这个正号的来源可从 [Milne Thm 1.2／1.5](https://jmilne.org/math/xnotes/pRH.pdf)和 [567 §§2–3](../../notes/567-function-field-positivity-origins-and-generalized-correspondence-tests.md)逐步核查。它不要求先建立经典 ζ 的整套高维上同调。

候选载体须有实际非零 primitive 方向。582 中 fixed q7 coarse native CH1 的 degreezero 部分为零，不能继续在该商中寻找隐藏 primitive；relative／family／higher 载体仍合法。正维 family 或真实相对 Picard／regulator 是候选类型，其具体成员和物理源映射目前未给出。

最小准入材料是一个**独立定义的源公式** \(\mathcal J:r\mapsto\mathcal D_r\)，并同时交付：

* **关系。** 全部 405 物理关系及其真实平移，在该对象中有实际 principal、Green transgression 或相应 exact 同伦；由算术映射证明，不能把 Pan 的像另命名为 boundary 来强行消去。
* **可见性。** 537 的明确双 polezero 非根仍非零；说明何种测试分离全部目标非根。仅这个正例通过不等于 coverage。也不要求错误的 \(\ker\mathcal J=\mathrm{Pan}\)：已知完整 trace radical 与分次 degree 类必须分开。
* **费用。** 用原 r 坐标核 du／zero-extension Dlog、支撑 L、height 与局部 level 的依赖，包含 Γ/contact、全部 proper powers、双 pole、constant jet、std／transported 差和所有尾。允许 Fréchet 强源、有费无界或源适应比较，但不能报原 norm 全线统一。

这三项没有实际公式时，只保留一个章节定位的来源门并在此停止，不继续 word、orbit、level 或论文串联。附件本身未提供这个公式。

进入容量阶段后，第一份值得审的对象应是**两个独立源的混合配对**。在实际整对象上先核局部消失阶、section lift 和乘法，再延到有理／实系数和 Hermitian 复化。任意 complex 核加权 cycle 不是自动的整线丛。要算 \(\mathcal D_r\) 与 \(\mathcal D_s\) 的全位配对，保 r+s、r+is 所需的 mixed 项；单条对角高度或 native degree 不能代全 Gram。

582 已给一个具体理由：Fourier 交换点乘和卷积，chirp 对乘积与逐因子作用差相位。因此可考虑实际的分次 tensor／line cocycle／双线性配对，检验相位在 tensor 后的真实相容性。这是一个有失败标准的结构建议；尚未构造相应算术 line 或容量定理，不能把“biextension／determinant line”名称作为输入。

最终应尝试关闭旧的量化充分接口。对每个固定原 compact 源 r，在实际 cutoff j 上给 primitive \(D_j(r)\)、真实交数和截面容量，使

\[
 I_j(D_j(r),D_j(r))=-Q_\zeta(r)+e_j(r),\qquad e_j(r)\to0,
\]

并独立支付

\[
 l_j(K_j\pm nD_j)\ge\tfrac12 n^2 I_j(D_j,D_j)-n b_j-a_j,
 \quad c_j=l_j(2K_j)<\infty.
\]

截面乘法给

\[
 I_j(D_j,D_j)\le\frac{2(c_j+a_j)}{n^2}+\frac{2b_j}{n}.
\]

这里先使用 surface 的 \(l_j=\dim H^0\) 型接口。若改为算术 small sections 的 \(\log\#\)，须另证同一 metric 下的乘法与容量比较，并计入相应 norm／边界误差；不能把维数论证原样套上。

若能选合法整数尺度 \(n_j\) 使右边和 \(e_j(r)\) 都趋零，就得到 Qζ(r)≥0。必须从实际 integral／rational 可实现源出发、支付延拓；身份须包括完整两 degree／endpoint 的正确平衡，不能只在双 polezero 子空间证明后声称覆盖全部 Q。所有 mixed 项和全 complex 源随后依真实连续性闭合。

这些是 [567](../../notes/567-function-field-positivity-origins-and-generalized-correspondence-tests.md) 与 [10-22 存在性稿](2026-10-22-weil-structures-and-existence-space.md) 的旧充分接口，本次未证明新实例。其价值是把“有二次容量”改成同一源、同一交数和实际误差的可审目标；别处 P1_Z 的 n² 容量本身不能付款。

## 5. 分析备选：保留较弱、却已足以传正性的 D′ 目标

为证明经典 RH，并不必先得到 ordinary trace、谱重数与 determinant。若从独立正对象直接构造正型分布 \(W_j\)，并证明

\[
 W_j\longrightarrow W_\zeta\quad\hbox{于 }\mathcal D'(\mathbb R),
\]

则对每个 compact complex r，卷积平方仍 compact，故 \(W_j(r*r^*)\to Q_\zeta(r)\ge0\)。完整经典显式公式和其 Weil 判据已是输入；此处不需额外的零点收敛定理。这是旧 562／576 已核的传递接口。

**不应把几何主线的要求强加给这条路。** 中间层不必逐层精确消 405 非 compact 关系；D′ 本身也不提供它们的全尾控制。若只为 compact 正性，原 norm 的统一算子小误差、trace norm 和行列式识别也不是必要条件。只有声称同一几何商、原 norm uniform 或完整 trace 层时才另付这些责任。

真正尚欠的是逼近序列的独立构造。576 的未标记正混合闭包已经等于全部实偶正型锥；只说经典 W 在该闭包，仍等于付目标正性。577 虽保真 Γ/contact 并构成逐层正修补，但完整修补的实际缺陷消失尚无独立证明。不能再用“平滑、弱极限、紧性”命名它。

这条备选升为主攻的证据应是：从经典 prime／dual 数据给出新的非负生成规则，或在具体 r 上可核的完整 signed 余项机制；同时通过 continuous 正负两段控制。若正负两段都通过而结论应只对正段成立，该规则不足。直接追完整 D′ 身份可比 uniform norm 目标更弱，值得保留，但本附件没有新序列可执行。

对于压缩迹路线，[Connes–Consani](https://arxiv.org/abs/2006.13771)确实研究了 archimedean Sonin 压缩及其与 Weil 分布之差；这里必须接本项目 560／570 的实际全逆、joint 费用和 signed 核，不能把局部设施直接提升为经典全局正性。

## 6. Deligne 放大：保作更强备选，先区分局部参数和全局零点

经典 ζ 的局部 Euler 参数都是 1；对这些参数普通 tensor 不会自动把 ζ 的非平凡零点张量化。必须先有承载全局临界谱的对象，并有保持源与 trace／pole 的非平凡族运算。普通 \(\pi^{\otimes k}\) 或 ζ(s)^k 不支付这件事。

[Deligne I §3，Thm 3.2 与 Lemmas 3.3–3.7](https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf)同时使用偶次 tensor 的局部非负性和同一层族的全局 pole 控制；[Katz 对原证明的说明](https://web.math.princeton.edu/~nmk/old/katzWorkofPDicm1978.pdf)也明确区分两项。它们不是从一般 Euler 正测度或函数方程免费得到的。

若最终有 \(|\alpha|^k\le C_kq^{kw/2+A_k}\)，一组便于核验的充分条件是 \(\log C_k=o(k)\)、\(A_k=o(k)\)。更一般，只须合并净误差 \((\log C_k+A_k\log q)/k\) 沿某个无界允许阶数子列的上极限不大于 0；两个误差可以抵消，不能将它们分别次线性说成必要条件。固定误差当然够，但未经控制的 rank／conductor／pole 重数增长可能使该极限失效。先提交可算的 k=2／4 真对象和全族定理来源；通过低阶只准入，不能代替全 k 证明。当前无此输入，故排序后于已有实际源与 Green 设施的几何主线。

## 7. 下一动作、反事实与停止

唯一下一研究动作保持为：**验收一个同一非零 primitive 实际载体上的 relative principal／Green cocycle 及物理源公式，先核全 405／537／全源非根与原费用，再决定是否建立一轮合同。**

这一选择胜于继续扩 S0，是因为 582 已证明域扩大和全源可见仍可与 principal 失败同时存在；胜于直接做 tensor，是因为后者连低阶非平凡对象与全局 pole 控制也尚未到位。

改变排序的证据有两种：实际构造了完整 Wζ 的独立正分布逼近及 signed 缺陷消失；或出现真 tensor 族和可检验的全局 pole 定理。另一个新局部范数、非零 metric、abstract positive trace 标签或只对固定正例成立的比较，不改变排序。

若候选载体 primitive 零、Pan 非 principal、537 失真或费用只在未覆盖子域合法，停止该 recipe；保留它确实给出的局部设施和其余合法修复。失败不排所有 relative／higher、付费无界、源适应或非局部路线。

## 8. Root 消费范围与本次结算

本稿只消费标准纠错、已结算结果和条件接口的逻辑。输入／输出为固定经典完整 \(W_\zeta\)、原物理源及其范数；有限域、continuous 正负模型和 KRY native 对象的角色各自保留。外部论文只支撑所指原机制，不给新经典身份。附件不是独立算术输入，也不赋予发布或新 Goal 授权。

已闭合的是附件三处字面公式的纠正、任务去重与路线责任比较。未闭合的是 \(\mathcal J\)、同对象 primitive mixed RR／完整 signed 运输、正逼近缺陷消失以及 tensor 全族。上述箭头仍 conditional／open；数个已付局部片段不能合成新整体定理。

强旧 whole4/5 是负惯性 UPPER；fixed17/16 正性不外推成长；actual q、成长 core／coupling／Ξ 未改。实际主瓶颈未改变。统一计 0 数学轮，单 cadence 保持 5、历史 46、formal cycle15；不建立新合同、不重置预算、不 complete 长期目标。

现场恢复：工作树起初 main 与 origin/main 同步且 clean；本轮 get_goal=null。Get-Process 未见列举的数学运行程序，CIM 命令行查询不可用，因此不声明全系统无进程。两独占审读与后续 fresh 的实际 handle／状态在各转换同步 STATE；最终 checkpoint 记录已完成输出及唯一下一动作。本次仅本地保存，未执行 GitHub 发布。
