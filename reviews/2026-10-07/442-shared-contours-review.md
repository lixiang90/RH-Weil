# 442 独立逆审：同源身份、共享轮廓与主信号

日期：2026-10-07。审查人：radial_review（非主稿和原解析推导报告作者）。
结论：**限定 PASS [T/R]**。已全文检查 442，并读取其需要的原局部定义、完整 tuple、stage-high 合同、principal/whole-bin/outer-row 证明和尾引理。未发现需要阻断本稿结论的错误。

## 1. 文件绑定与准确范围

主稿：notes/442-shared-contours-and-principal-signal-at-the-new-boundary.md。
canonical LF SHA256：
87abb4dd86ccae9b8209e030606413ef2b8682631f9c4d9195afdd808ad1b6b7
（11726 字节）。

外部 [R] 来源：E:\codex-build\math\preprints\The-Quasi-Riemann-Hypothesis-September-30-2026\build\paper.tex。
固定提交 adc7f1241b42e322a6451854ab7e4b4c146bf78a；
canonical LF SHA256：
42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3
（766316 字节）。
本报告的 source 行号均绑定这一源版本。

PASS 仅覆盖主稿所声明的解析/外行接口：同一个物理 finite compensated expression 的 high identity、扩展域全纯性与全高度 majorant、主信号和实际 normalizer、principal contour、whole-bin contour、新小行域及大行控制。没有认证完整 central numerator × error-slot 联合估计、实际 detector counts、全域严格 saving、continuation criterion、新的无零区域、RH/RR 或 Lean 验收。

## 2. 同源有限操作与输入参数顺序

主稿 §1、§3，式 (8)(9) 通过。

- 原 base probe 在 independent positive \(X,Y,Z\) 上定义，只有后续 balanced proposition 才固定 scales（source 3315–3322）。
- fixed ray group \(T\) 可在目标前选择；source 3327–3343 明确目标相关 fixed-numerator characters 无须通过 \(T\)，扩大最终 \(S\) 不改 \(T\)。source 3950–3951 的校准对固定 enlargement 仍 coefficientwise 成立。
- 原补偿是对每个固定 \(Z\) 的有限 physical completed-sum 操作；source stage-high 定义 5597–5604 允许这种 \(Z\)-dependent finite combination，但直接 low estimate 必须仍指向这份 physical expression。
- selected local operation
  \[
  \overline{\eta(p)}Q^{s+z-1}P_p^*-Q^{z-w-1}P_p
  =\frac{1-D}{(1-V)(1-W)}Q^{z-1}G_p
  \]
  是 source 8717–8719 的准确等式，不依赖旧 \(\ell=1/6\)；disjoint underlying slot supports 使每个 selected prime 只操作一次。它不需要除 \(P_p\) 或 \(H_p\)。
- 在绝对起始线 \((3,3,2)\) 上按有限组合整理，可以使用同一个 scalar quotient、physical sixth-power-free \(u\)-support 与 Mellin kernel，得到主稿 (9)，见 source 8714–8729、8774–8790。这确实来自原 physical expression，没有以 high integral 倒定义 low object。

固定几何给 \(h=1-l_x+\ell\)、\(C(s)=s+l_x/2-1+h/6=s-11/16\)；新槽长没有移动标量极点 \(w=1,z=1/6\)。\(S,\xi\) 可依赖固定目标，但同一次应用的 low/high/信号/normalizer 始终使用同一个最终 \(S\)。

## 3. \(D_2^*\) 正常收敛、完整无商 tuple 与全高度界

主稿 §2，式 (3)–(7) 通过。

源完整局部表 4013–4032、定义 4034–4047 和 defect 4139–4146 保留了 \(p\mid u\) 时的 \(D=W=0\)。新域
\[
 \Re s\ge\sigma_1,\quad\Re z\ge33/200,\quad\Re w\ge19/20
 \]
上 good-prime 的关键幂为
\[
 301/100-6\Re s,\quad-\Re s-19/20,\quad-194/100.
 \]
所以可和 margin 正是
\[
 c_b=\min\{6\sigma_1-401/100,\sigma_1-3/50,47/50\}
 =65199/80000.
 \]
ramified 全五种 \(J_j\) 分支与 strict term 的 margin 可由
\[
 c_r=\min\{\sigma_1-1/20,3\sigma_1-3/2\}
 =65999/80000
 \]
控制。两个值正确且严格为正；\(1-R,1-V,1-D\) 一致离零，\(1-W\) 仅是 polynomial factor。所有 bounds 对 imaginary parts 和目标 unit phases 统一。

采用理想计数与有限 ramified divisor-product bound，good-prime 正 majorant 正常收敛，ramified 部分为 \((Nu)^\epsilon\)。严格 margin 允许实下界略向外移动，所以是在闭域每点邻域全纯，不只是 contour 上的点态存在。原 \(D_1(\epsilon_0)\) 的通用域 source 4054–4055 允许任意固定 \(\epsilon_0>0\)，无需扩其陈述。

完整 correction 必须是 source 8707–8711 的 finite selected tuple sum。主稿 (6) 正确使用该对象：
\[
 \prod_{\rm selected}G_p\ \prod_{\rm unselected}H_p;
 \]
一般 row 从未除以可能为零的 \(H_p\)。
删除 selected primes 只是在每个大于等于一的 positive majorant 中删除因素，不是对 complex product 宣称 support monotonicity。因而 bound 对所选 tuple 一致，不需要任何一般 local nonvanishing。

在固定 real box 内，完整局部 rational formulas 给 \(|G_p|\ll Q^B\)；modulus 只依赖实部，local phases 和 norm twists 对 imaginary parts 的 modulus 为一。每槽 \(O(P_i)\) 个理想、\(Q_i\asymp P_i\)，故
\[
 |\mathfrak H_{\eta,u,Z}|
 \ll (Nu)^\epsilon\prod_i P_i^{\Re z+B}
 \ll (Nu)^\epsilon Z^{B'}.
 \]
对 \(Nu\le Z^D\)，这支付 source 5614–5623 的 all-height requirement，确实可取 height exponent \(J=0\)。\(B'\) 由固定 real box、slot system 和 \(D\) 決定，独立于稍后 external integration-by-parts order。这没有给 central joint numerator bound。

## 4. 主行非零、\(B_p\) 指数与实际 normalizer

主稿 §4，式 (10)(11) 通过。

source 的 unique principal numerator row 是 \(u=1\)。对该行，选 cutoff 的可审实际条件是
\[
 \sum_{p\notin S}|H_p-1|\le C P_0^{-c_b},\qquad
 \exp(CP_0^{-c_b})-1\le1/2.
 \]
此条件同时给每个 local factor 非零、整个 product 非零以及
\(|\mathcal H_{\eta,1}-1|\le1/2\)。最终稿 §4 已明确写成 \(\exp(C\sum_{Q>P_0}Q^{-1-c_b})-1\le1/2\)，正确表达此 product-error majorant；这一唯一措辞澄清不产生新问题。源校准保证目标确定后增加排除集仍缩小同一个 positive majorant，且不改变 \(T\)。因此该固定 \(P_0\) 可在目标前选择，不需目标 uniform prime asymptotic。

主行 local quotient \(B_p=G_p/H_p\) 此时合法。source 8808–8827 的精确抵消与 9066–9077 的局部比较，在新 \(D_2^*\) 给四个最大 error exponents
\[
 -69999/80000,\quad-99/100,\quad-21839/16000,\quad-47/50.
 \]
因此 \(B_p=-1+O(Q^{-\sigma_1})\) 准确；不能保持旧的 \(Q^{-7/8}\) uniform exponent。此界和 positive unselected product 也给 principal correction 的
\(Z^{\ell\Re z}\) 全高度 bound，无需 height 截断。

固定 positive slot windows 的 ray-prime asymptotic 为明确 [R] 输入。由于各 \(\ell_i>0\) 固定，\(S_i(Z)>0\) 最终成立，\(A_T=(-1)^K Z^{-\ell/6}\prod S_i\) 最终非零且 inverse 仅是 logarithmic power。奇偶号不影响非零性或 complex normalization。

在 \(w=1,z=1/6\)，主行可因子化为
\(\mathcal H_{\eta,1}\prod_i \mathcal B_i\)。
非负 \(W_i\) 允许逐槽相对 error：
\[
 \left|\sum_p W_i(Q/P_i)Q^{-5/6}(B_p+1)\right|
 \ll P_i^{-\sigma_1}S_i(Z).
 \]
固定 finite \(K\) 后，任意预先给定
\(0<\mu<\sigma_1\min_i\ell_i\)
支付主稿 (11)，包括整条 global \(s\)-line 的 imaginary parts。这里的 relative error 不要求对目标 varying conductor 作统一 prime theorem；最终阈值可依赖固定目标的有限 \(S\)。
\(c_S>0\) 的来源及 \(1/6\) residue factor 与 source 5520–5543 完全一致。

## 5. Principal 轮廓、actual remainders 与高度顺序

主稿 §5，式 (12)(13) 通过。

源 principal proof 6224–6301 的几何无关步骤均已在扩展域获得前件：

1. 把 principal row 隔离后，在 global \(s=\beta_*+e\) 上移至 \(w=1+e,z=1/6+e\)。
2. 移 \(w\) 至 \(19/20\)，只跨 \(w=1\)；在其 residue 中移 \(z\) 至 \(33/200=1/6-1/600\)，只跨 \(z=1/6\)。unresidued \(w\) 部分保持 \(z=1/6+e\)。
3. 整个过程在 \(D_2^*\)；reciprocal 始终 global。每个 extended vertical scalar axis 严格位于相关 pole 一侧，horizontal joins 在非零大高度，没有把未去的标量 pole 放进 arithmetic majorant。
4. w-residue 后使用实际 two-dimensional kernel，其余部分使用 triple kernel。Gaussian 在 \(s+z\) 方向、\(M(z)\) 与 \(\widehat W_1(w)\) 在另两方向的 rapid decay，经固定可逆变换控制原 heights；不能以一条轴的 bound 替代 joint bound。
5. relative residue error 只在 global line 上估计；只有无误差的 main integral 右移到 \(s=2\)。principal denominator 的 pole 对 reciprocal 是零，不增加 residue；本次不用新 \(\sigma_1\) 零自由性。

raw power 为 \(l_x/2+\Re s-1+h\Re z+l_y(\Re w-1)\)，故三项 remainders 准确为
\[
 C(\beta_*)+(1+h)e-l_y/20+\epsilon,\quad
 C(\beta_*)+e-h/600+\epsilon,\quad
 C(\beta_*)+e-\mu+\epsilon.
 \]
新 \(l_y/20=57497/2400000\)、\(h/600=32503/24000000\) 均为正，数值正确。
normalizer inverse 的小幂只需分配到总 \(\epsilon\) 一次。
应先固定 slots、\(\mu\) 和所有 positive real margins，再选 \(e\) 与 component losses；目标相关的 finite arithmetic height orders在 external tail order 之前确定。这一顺序与主稿要求一致。

## 6. Whole-bin 轮廓与 conditional central bookkeeping

主稿 §6，式 (14) 通过。

源 fixed-bin theorem 的陈述 5811 行确有限制 \(\sigma_0\ge7/8\)；本次不能直接援引该 statement。
但其证明 5838–5896 只需要 \(a\le\beta_*\)、原 \(D_1\)、full correction holomorphy/majorant 和 global/buffered reciprocal：

- **先固定整个 bin** 和 finite original row set，不以 contour-dependent amplitude/detector labels 预切再移线。
- \(z\to17/50,\ s\to\beta_*+20e,\ w\to1-a-6e\) 时有
  \(\Re(s+w)\ge1+14e\)、\(w\ge-6e>-1/100\)，full correction 在 \(D_1(10e)\) 合法。
- 先在 global \(s\) 线上丢弃**原三个 heights 的同一个 box**外的 tails，再移动 retained \(s\)-segment 至 \(a+16e\)。源的固定 box constants \(c_s,c_w,c_z\le1/2\) 和 cumulative frequency allocation继续保留；reciprocal argument 的 real part \(>a+6e\)，其 height严格落在原 buffered rectangle。
- \(s\)-joins 的 denominator 只依赖 \(s\)，所以可扩 \(w,z\) 轴来取 joint trace bound；没有在别的 join 上扩一个已移动进仅 buffered 区域的 \(s\)-axis。

source 5672–5728 的 external integrated/trace tails 用固定 \(Z^B(1+|\boldsymbol t|)^J\) majorant 与任意阶 rapidly decreasing test kernel；在所有所需 axes/joins 上 \(B,J\) 先固定，再选 tail order。这给主稿的 \(O_{\eta,N}(Z^{B_\eta}T_1^{-N})\)，没有隐藏的 \(N\)-dependent arithmetic exponent。

主稿 (14) 由源 6142–6152 的 outside powers 与**尚待证明**的 joint central bound直接记账，代入 \(h=1-l_x+\ell\) 和参考幂 \(C(\sigma_1)\) 无误。附加 losses
\((16-6l_y)e+(1+d)\epsilon_c+d\epsilon_d+\epsilon_p\)
准确。它没有证明实际 \(R,g\)；主稿 258–259 行和 §8 明确保留这个条件范围，没有把 nominal \(R_*\) 偷换为 actual counts。

## 7. \(D_1(1/3)\) 小行修补及大行

主稿 §7，式 (15)–(17) 通过。

原 small-row proof 的 \(D_1(3/8)\) 不再统一包含 \(\beta_*\) 刚超过 \(\sigma_1\) 的情形；主稿明确修为 \(D_1(1/3)\)，因为
\[
 \sigma_1+1/2>1+1/3.
 \]
这保留原域所有条件和 \(\epsilon_H=1/50\)，没有新增零自由假设。

small-line good selected \(G_p\) 的四 errors 全负。ramified 使用 \(D=W=0\) 后，全 \(j=1,\ldots,5\) boundary exponents为主稿所列值，乘 \(Q^s\) 后均不超过 \(1/2\)；strict term 为 \(1-w=1/2\)，common \(R\) term更小，几何比例 \(|R|,|V|<1\) 且一致离一。因此 \(G_p\ll Q^{1/2}\) 合法，包括 \(H_p\) 零点。
局部 threshold \(x\ge1/2\) 并不代替完整 Euler 域的 \(x\ge51/100\) 等条件；本次 actual line 已由 \(x\ge\sigma_1\) 满足全部条件。

每槽 nonramified \(O(P_i)\) ideal count 与 ramified divisor-many count，结合 uniformly deleted positive product，支付主稿的 full tuple
\(U^\epsilon Z^{17\ell/50}\)，而不先丢掉 selected \(G_p\)。
原 nonprincipal numerator conductor/strip bound 给 \(U^{3/5+\epsilon}\)，行数 \(O(U)\) 和 \(q_u^{-17/50}\) 给 \(U^{63/50+\epsilon}\)。
精确 new small margin
\[
 h(13/75)-l_y/2+(63/50)/100=-172249/2000000
 \]
正确；用粗 \(2/100\) 为 \(-157449/2000000\) 也正确。它独立控制 outer small rows，不依赖中间行 detector。

大行 final lines \((2,2,z_\infty)\) 上完整 selected \(G_p=O(1)\)、unselected positive product统一；新
\[
 B_0=l_x/2+1+l_y=264994/160000
 \]
以及 dyadic tail exponent
\[
 B_0+(h+\zeta)(1+\epsilon)-\zeta z_\infty+\epsilon
 \]
均正确。先固定 \(\zeta>0\)、再取 fixed \(z_\infty\) 足够大，可以获得指定 power saving。
证明 fixed-dyad contour identity 用到的暂时常数可依赖该 dyad，但 final estimate 使用统一 absolute tuple bound；不能让此暂时依赖污染 summed tail。

## 8. 限定验收

当前稿可以作为新边界的解析和 outer-row [T/R] 输入。
明确保留的 [R] 是原 coefficientwise probe/Poisson、完整局部 identity 与 source support、ray-prime asymptotic、Hecke growth、global/buffered reciprocal/zero bins，以及 finite-order test/tail calculus。本审查没有逐项重证外部全部算术或 recursive moments。

没有需要主稿数学修订的阻断点。全部结论均受主稿 §8 的边界限制：actual central counts、error gains、全 \(d\) saving 和完整 continuation 仍须后稿支付。
审查只新建本报告；未改主稿、旧文件、外部 math 仓库，也未编译外部项目。
