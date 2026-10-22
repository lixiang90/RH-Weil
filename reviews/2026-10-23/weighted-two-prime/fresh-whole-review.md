# 581 双素数有权强完成：独立 fresh 审核

2026-10-23；`/root/weighted_two_prime_fresh_581` 独立核查。仅写此文件，不改 STATE／cadence；本审核不等于 root 消费或宏观完成。已读恢复入口、C044、580的结算范围与三份本轮原证明。主稿写入后的逐项闭合记在末节。

## 1. 审核对象与初步判定

审核以下实际对象，不在它们之间免费运输：

1. fixed-arch 源 `J_w r=φ_*⊗Σ w_n c_n(r)e_n`；有限位径向球基及其 A₁ 强完成。
2. compensated rational orbit 源 `V_w r=Σ w_n c_n(r)Ω_n`，其中 `Ω_n=D_{−a_n}φ_*⊗e_n`；原 Schwartz 域与其全 s transported 输出。
3. 物理坐标的真实 S-unit 群差 `I−T`；加权 frame 坐标中的 `M_w^{-1}(I−T)M_w`。
4. 另定义的反向共轭 `B=M_w(I−T)M_w^{-1}` 及其 Hilbert Koszul 复形。

三分支的数学结论可限定 PASS：算术高度、全源注入与强完成费用成立；真实 routing 留非零 charge，反向共轭则吞掉全部 H₀。它们没有构造成功的 arithmetic primitive 源、同对象二次容量或新的经典 Weil 正性。全原域保留要求在这条具体 recipe 上失败，不能以“强完成合法”替换该要求。

## 2. 算术权、原域与实际范数

固定 `k=Q(√−7)`、split 2与11。`−7≡4 mod11` 且不分歧；2的判别式条件也正确。fractional ideal `I=2^j11^k O` 与 O 的两个真实有限指数给

`H=sqrt([O:I∩O][I:I∩O])=2^{|j|}11^{|k|}`。

此 H 是 symmetric commensurability height，区别于通常有理 projective height；指数2是明示的安全选择，没有从算术独立唯一选出，更没有由 RH 选取。

局部 Gram 两位相乘的 Riesz 上下界确为 `5/18,18/5`。因 `||sech(u/2)||²=4`，实际 `J_w` 的全部 mixed 范数由 `4νμ(18/5)Σw²||r||²_du` 支付。`Σw=61/36`、`Σ(|j|+|k|)w=805/864` 和三分支列出的 `Σw²`、origin／integral 费用数值一致。HS／紧性成立，不能把注入报成统一 frame lower。

全源注入证明闭合：权处处非零；Riesz 唯一性恢复每个 c；双步长集合稠密；`r*sech` 连续且 Fourier 乘子没有实零。它对全 L²、从而全 S_exp 成立。不用 Q／未知零点来定义数据。

原 Bruhat 门的两种证明一致。固定原两位球旗上的 Bruhat 函数是有限 e_{jk} 组合；或由统一局部常值性作双 valuation 差分，迫一整个半平面的 c 样点为零，而该半平面样点仍稠密。因此每个非零源的指定 `J_w` 都不属原 Bruhat 域。更一般地，任何处处非零且使同一球／Riesz 合成合法的权都过不了该门：对固定 annulus，评价向量 `(2^j11^k)_{j≤n,k≤m}` 属 ell²，Cauchy–Schwarz 已保证该处绝对评价与双差分，无需额外偷加 A₁。此结论不排不同基、新完成、额外边界或有费变域。

## 3. A₁ 强完成与双读出阈值

`A_β={Σ a_jk e_jk:Σ|a_jk|H_jk^β<∞}` 对 β≥1 是实际 C₀∩L¹∩L² 函数空间。自对偶 Fourier 的 `e_jk→e_{−j,−k}`、球乘法

`e_j e_l=p^{min(j,l)}e_{max(j,l)}`

及权不等式逐正负象限均正确。故 pointwise product、卷积闭合与相应代数费用成立。`σ>β≥1` 的源费用 `2ΣH^{−(σ−β)}||r||du` 闭合；固定 σ=2、β=1 合法。

σ>1 时 origin 和 integral 两条真实读出均有原 du 统一费用。σ≤1 的反向证明不是粗上界：固定 compact `ψ≥0`，`r_T=(D²−1/4)ψ(·−T)` 保双 pole-zero 与平移不变的原 du／Dlog；origin 的各项同负，约 T 个正象限点给 `T exp((1−σ)T/2)` 的实际费用。反射得到 integral 反测。每个固定 S_exp 源即使 σ≤1 仍可有绝对读出；失败的是全线原范数统一费用，不能写成逐源不存在。

A₁ 的 Fourier＋dilation＋乘法并不证明 full Weil group 稳定。unipotent chirp 一般离开这条球旗。分支最后新增的每个先固定 local g 的 λ 评价可延拓：matrix 的 c=0 时由 origin 费控制，c≠0 时由含相位的积分及 L¹费控制，给 `|λF(g₂,g₁₁)|≤C_g||F||Aβ`。该结论合法，常数依赖 g；它既不证明 ω(g)F 仍在 A₁，也不外推全 adelic g／Eisenstein 求和的统一控制。E′、Green、cycles 与相对 DGA 的全域连续性仍必须另证。

## 4. 全预算运输与 compensated 轨道

独立核了 finite-only 的 right-transport 规范：bare 球的 family 是 `d^{-1}Φ₀(g t_d,s)`，native classical 导数因 `v^{-1/2}d^{-1}=(d²v)^{-1/2}` 变成 `φ₀(d²τ)`；单位化 e 的输出为 `dφ₀(d²τ)`。所以完整去 constant Mellin 系数为 `d^{1−2z}`。这同时保正／负 Fourier 项、两条 constant 腿与 Γ。标准延拓导数仍需明确 local log-Iwasawa cocycle，不能因 s=0 初值相同忽略它。

σ2 下 `B_r(z)=Σw c d^{1−2z}` 的 du 正常收敛带是 `−1/2<Re z<3/2`。S_exp 的真实指数尾可扩大带，扩大费使用强源 seminorm，不能伪报 du。其输出在中心线上是有限复原子测度的 Fourier 变换，因原子位置各异，完整解析像仍全源注入。B 是数据决定的 source-dependent signed 乘子，既不是任意完成化选择，也没有自动无零、正逆或 Weil quadratic 身份。

compensated `Ω_n=ω(m(d^{-1}))Φ_*` 的规范不同。对 imaginary axis `g_v`，rational diagonal 与其交换，automorphy 精确给所有 s 的 `E₀(g_vm(d^{-1}),s)=E₀(g_v,s)`。constant-term 积分的换元 `b→d²b` 在全 adele quotient 上模长为1，故两腿也相同。这个结论只在指定 imaginary-axis 预算读出成立；一般 τ 不自动相同。因此完整 Mellin 预算为 `C_w(r)ℳ₀`，不能把 fixed-arch 的全源解析注入挪到此 scalar 读出。

本审核重新打开了 [KRY1999 作者版](https://www.math.uni-bonn.de/people/rapoport/myalggeom/preprints/tinynew.pdf)，核 §1 的 λ／标准 extension／Eisenstein 定义与引言、§4对应的完整 Mellin式。该原件没有支付这里无限 weighted Schwartz／Green／算术 cycle 扩张。负 level 的实际解析 family 与重新标记的 quasi-endomorphism 模态问题不等于无限同一整模型、共同 level 或 principal 比较。

## 5. 相对边界、反向共轭及 405／537

物理系数 `z=w c` 中的真实 unitary group difference 是 I−T。转到 `E_n=w_nΩ_n` 的 frame 后为 `M_w^{-1}(I−T)M_w`；相反方向不是同一个算术边界。

实际第一矩 routing 给

`∂b=z−C_wδ₀`，`||b||₁≤(805/432)||r||du`。

这里 finite-height 全尾已付；不能泛称没有费用可付。405 的每个平移均有 `c_n(τ_bP)<0`，故 `C_w(τ_bP)<0`，真实 charge 不消。另一方面正偶 K_w 的 scalar 读出漏掉 537 窗内的奇双 pole-zero 非根。全 family 注入与该 readout 丢失并不冲突。

另定义 `B_p=M_w(I−T_p)M_w^{-1}` 后，分支给出的 R_p 在正负半轴递推都满足 `B_pR_p=I`。ell² norm 上界4/3，经全部 finite Gram 的 condition 数换算为24/5，数值正确。全 Ω Gram 是有限 Gram 与归一化 arch Gram 的 Schur product，后者对角1；同样的上下界保留，所以该原费用亦正确。

Koszul 的 `H₀=H₁=0,H₂=span{w}` 证明闭合。该合法 Hilbert 修复会吞全部 H₀，因而不能付 primitive coverage。形式无权 charge 发散只说明这个 primitive 离开保 charge 的强域，不能反过来否认其实际 ell² 右逆。H₂ 的 coefficient-ell² 投影不能冒充非正交 Gram 投影；一维 scalar 也不生成同对象 RR。

常数 S-unit 的真实 Arakelov principal divisor 仅在2、11及 arch处支撑，不可能等于 n=1 的 level-cycle 差在 char7 的非零分量。这个反测只排常数unit最便宜桥，不排真实 isogeny／modular function／额外相对 regulator。

## 6. 首门强化、完整高频费用与对照

另独立核 root 提出的强化：在537窗取 `ψ≥0` 非零 compact，`r=(D²−1/4)ψ`。它双 pole-zero，全部 `c_a(r)<0`，且

`c_a(r)=−4d^{−3}∫ψ(u)e^{3u/2}du+O(d^{−5})`，`a=2log d→+∞`。

finite origin 的 Ω 振幅中 e_n 的 d 与 arch dilation 的 d^{-1} 抵消。沿 k=0、j→+∞、`y=d=2^j`，权 d^{-2} 使单项为固定负号的 d^{-5} 级，所有其余项同号。因此该明确537双pole-zero非根的 compensated Ω 和也不是原 arch Schwartz；不只是非负、带pole源的较弱反测。这一结论仍限于指定 σ2 轨道 recipe。

R_A 的源恒等式 `R_A*s=4πexp(−π²−πA)e^{-u²}sin(Au)` 与归一化因子一致。新 dense family 确实看见旧 alias 源，却只有指数小能量；完整经典 Γ 给 `log A` 费用，全部 prime powers 的 Gaussian 尾一致可和，双 pole 在该源上精确为零。没有用零点或预设 Weil 正性。故 bounded-energy 容量比较失败，但不能将这项旧 Gaussian smoothing 机制重数为新的独立正号，也不排独立算术来源的无界 height。

continuous ±1/16 的同一奇源对相同局部 Gram 有完整 Weil 异号；这是 distribution-sensitive quadratic 身份缺失的对照，未建立 continuous→CM 运输，不能说它反驳 KRY。函数域两个 finite norm 步长均为整数倍 log Q，必相称；不能移植数域的 dense-grid 覆盖结论。567 的同对象 primitive mixed 交数、实际截面乘法和 RR/Hodge 提供其正号；compact 源用统一 j₀保证非负 Frobenius，完整源依已证 Toeplitz 完成，不造负 Frobenius。局部权 Gram 与该由点数给出的 primitive Gram 不是同一对象。

## 7. root 主稿闭合状态

已实际通读 `notes/581-arithmetic-weighted-two-prime-completion-and-relative-capacity-gap.md` 全稿并与三个分支逐项核查，给出**限定 PASS**。主稿准确区分 fixed-arch A₁源、compensated Ω源、两方向共轭及真实 arithmetic principal；原 du／zero-extension Hlog 费用与固定窗／全线／强源量词一致，保全部 Γ／prime powers／双 poles，未升级独立容量。root 拟加入的 fixed-g λ 句已按上一节核准。唯一小记号修正是将 Koszul 的 `H₂=Cw` 明写 `H₂=ℂ·w`，避免与真实 charge `C_w(r)` 混淆；这不改变其证明。

扣旧后确认本轮新消费是实际算术权／A₁代数和双读出阈值、全非零源 Bruhat 门、完整解析像及真实边界／routing 的准确方向与费用。旧553 bounded商障碍、552／579 Gaussian高频和567 RR来源均已按输入处理，不能再次计作本轮独立正性。即使这些局部件均闭合，它们也没有覆盖同一整模型上的局部消失过滤、primitive截面lift／乘法和 mixed RR容量。

宏观结论固定：本轮局部有权完成／原域／边界门可有真正新输入，但 classic 独立 mixed 容量、actual q／成长 core／coupling／Ξ未付；强旧542＋555→557 whole leading4/5是负惯性 UPPER且未改善。root 前件闭合、统一结算与 GitHub 同步另行执行，不由本审核代办。
