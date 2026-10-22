# C036 实际相对理想闭链与 regulator 电荷的独立范围逆审

2026-10-22。独占审阅；不改公共 STATE/cadence/Git。同 G20261014、冻结基线 0c4f。
本审阅已读 C036、573 全文与三份独占原件，并重读 405、424、427、430–432、537、553 的必要定义和证明。
**最终结论：限定 PASS，无剩余 P1/P2。** 本审阅独立重推有限 Γ、胞元源、−4 迹及闭理想识别，
未将新外部文献背景当本命题的未证明前件。
不把原件出稿当 root 消费，不由本审阅完成宏观 Goal。

## 1. 有限 Γ 隔离：左右腿顺序准确

在实际 430 的解析扩大代数 \(A=\operatorname{alg}(1,u,u^*,D_{\rm src})\) 中，
取 \(X=(V,uV)\)、\(\Gamma=[\gamma_{k-j}]_{j,k=0,1}\succeq I_2\)。
430 的有限传播光滑核证明给实际乘法模 \(I=\mathcal S_1\) 为 \(B\star C=B\Gamma C\)。
对于原件所写

\[
 L_{0i}=C M_{(\Gamma^{-1})_{0i}},\qquad
 R_{j0}=M_{(\Gamma^{-1})_{j0}}D,
\]

逐腿相乘得到 \((L\Gamma)_{0k}=\delta_{0k}C\)、\((\Gamma R)_{k0}=\delta_{k0}D\)。
故 \(L\Gamma(E_{00}U(h)-E_{11}U(h))\Gamma R=E_{00}CU(h)D\)。
没有把 C、D 与周期乘子交换，也没有使用无界或未定义的无限 Γ 逆。
\(\Gamma^{-1}\) 是实际光滑周期有限矩阵；乘子夹在光滑核旁保持 \(G_M\) 准入。
每次从周期符号回实际算子的差均为旧 430 已证明的迹类余项；因 I 已是生成理想的一部分，
所得 \(VCU(h)DV^*\) 是实际理想元素，不只是商中同类。

## 2. 实际非根源与有限秩 trace −4

令 \(0<L_0<\min(M/2,17/16)\)，胞元函数 \(\phi\) 取实非负、单位 L² 范数，
支撑于 \((0,M)\) 内宽度小于 ε 的紧区间；χ 为实偶光滑紧支函数，
支撑于 \((-L_0,L_0)\)，在 \([-2\epsilon,2\epsilon]\) 恒为 1。
记 \(c=(\int\phi)^{-2}\)，则

\[
 r_*(u)=h_0(-u)=h_0(u)=c(\chi-4\chi'')
             =(D^2-1/4)(-4c\chi).
\]

分部积分严格给 \(\mu_\pm(r_*)=0\)。它非零且严格落在 537 正窗，
故完整 \(Q_W(r_*)>0\)，不是 Pan 关系或 Weil 根方向。
同胞元差集上的平台值及不同胞元差集与 h₀ 支撑不交，准确给 \(PU(h_0)P=P\)。
胞元周期秩一投影 P 与双边胞元移位 B 都是 \(G_M\) 的真实光滑有限传播核，范数为 1。
有限 Γ 隔离因此把 \(VPV^*\)、\(T=VBV^*\)、\(T^*=VB^*V^*\) 放进
\(J_*=\langle I,F_{r_*}-uF_{r_*}u^*\rangle_A\)。

独立重算 \(\xi_n=V\phi_n\)、\(a_n=\|\xi_n\|^2\)：
\(T\xi_n=a_n\xi_{n+1}\)、\(T^*\xi_n=a_n\xi_{n-1}\)。
在实际归一化向量上，移位权为 \(\sqrt{a_na_{n+1}}\)，
交换子本征值为 \(a_n(a_{n-1}-a_{n+1})\)。
原 m 的端点 0→2 保证充分左端 aₙ=0、充分右端 aₙ=2，无须单调性。
所以交换子严格有限秩，且

\[
 \operatorname{Tr}[T,T^*]
 =\sum_{n=-N}^Na_n(a_{n-1}-a_{n+1})
 =a_{-N-1}a_{-N}-a_Na_{N+1}=-4.
\]

aₙ=0 的项自行为零，未对零向量归一化。正交补上的 T 与 T* 都为零。
故匹配 I 普通迹的循环标量 \(\tau:J_*\to\mathbf C\) 不存在，甚至不要求连续或正。
另一方面 \(q_I(T)\otimes q_I(T^*)\) 是旧商的一循环，旧 Ω 值 −4，
在新商 \(A/J_*\) 的链像却为零；因此旧 Ω 不可能沿自然 HH₁ 商映射因式分解。
这不是声称 \(HH_1(A/J_*)\) 本身为零，也不是所有新 relative regulator 都不存在。

## 3. 范数闭理想的范围与尾费

由 \(\gamma_0=2\)，实际三重乘法给
\(F_{i,0}(C)(VPV^*)F_{0,j}(D)=4F_{i,j}(CPD)+I\)。
胞元错位的光滑秩一核 \(CPD\) 产生 Laurent 单项式乘胞元秩一块；
其线性 span 在旧 431 已计算的
\(\overline{G_M}=C(S^1)\otimes\mathbb K(L^2(0,M))\) 中范数稠密。
有限 \(F_{i,j}\) 的实际算子范数连续性因此给

\[
 \overline{J_*}^{\,C^*(A)}=\overline{D_{\rm src}}.
\]

反向包含使用 \(D_{\rm src}\) 为 A 双侧理想，生成元已在其中。
这仅是范数闭包相等；没有证明代数 \(J_*=D_{\rm src}\)，也不声称纯 u 商一并消失。
对 raw \(r\in L^1\) 的延拓只用
\(\|F_r-F_{r_n}\|\le2\|r-r_n\|_1\)。
S_exp cutoff 的尾费明确为 \(2\|(1-\chi_R)r\|_1\to0\)。
这使 C* quotient 消去全 raw S_exp，包含全 Pan，但同时杀掉 537 非根。
它不是 HH₁/迹类准入的扩域定理，也没有全线原 du/Dlog 统一尾费。

## 4. 原费用、其他新边与全关系检验

原源 \(\operatorname{supp}r\subset[-L,L]\) 的实际费用
\(\|F_r\|\le2\sqrt{2L}\|r\|_{du}\le2\sqrt{2L/\log2}\|r\|_{Dlog}\) 正确。
所选 r* 的 c、χ 及导数费用有限但可能随胞元收缩增长；没有宣称统一无费。
测试 P、B、有限 Γ 逆是合法额外代数边，不冒称它们是物理 raw 源或原源的必要费用。
430 trace-norm 余项还需核半范数；单一 du 范数没有被偷偷用于支付该全域费用。

新边稿的对称修补严格满足提升层面的交换子和零，因此 Ω=0；
它是旧 424 身份的真实源实例，并非新非零 regulator。
任意另一修补与之相差一循环，故闭性本身留下 HH₁-cycle 的自由度。
旧角点循环电荷
\(4\int uk(u)r(u)du\) 对固定 k 有精确 du/Dlog dual 费用；
取 \(k=u\overline{r_0}\) 可见 537，非零固定 k 却由 553 稠密性必失败某个真实 405 平移。
源依赖 kᵣ 同样给正数 \(4\|ur\|_2^2\)，但其对非零 Pan 标量延拓也正。
这里严格区分 compact 链准入与 S_exp 标量延拓；未将 crop 认成主关系。

代表链的 projective 费用不自动证明 Ω 在某完成中连续。
S₁ 在整个 B(H) 中算子范数不闭，本身也不证明其在 A 中的相对闭性或商不分离；
旧 431 恰已给 \(D_{\rm src}\cap\mathbb K=S_1\)。
三稿消费的是实际代表上界与独立计算的标量 dual 费用，不能偷换成新的 Hilbert 商正性。

## 5. 整模型、正反控制与完整目标

同一 \(\mathbf P^1_{\mathbf Z}\) 的真整数 jets、乘法过滤及
\(\log\#\widehat H^0=a n(n+1)+O_a(n\log n)\) 二次容量继续有效。
有限非零角点 probe 作复系数坐标可以有费且保 r₀，却既不消全 Pan，也不自动给整数系数/局部整除。
connecting boundary 是局部数据的拼接障碍，须证明其消失并给实际 metric lift；
已有整数容量不支付 raw HH₁ source→同一算术截面的比较。
没有把坏 singular value 的全空间 worst-case 费用当 actual source 必要费用。

连续正反控制确来自旧 562/567 的正 continuous P/Π/M 族
\(Z_c=1+c/[s(s-1)]\)、\(d=c-1/4=\pm1/16\)。
有限代数 \(R_d=\mathbf C[z]/(z^2+d)\)、\(z^\dagger=-z\) 的 regular trace 为
\(2|A|^2+2d|B|^2\)，独立算出两种 primitive 号。
同样的 length-two resolution/闭链和形式 tensor 设施不会选择 d>0。
这不是声称 d<0 的 † 已是正 Hilbert adjoint，也不把 430 的具体经典 source 表示外推给所有 g 分布。
函数域另有真实 \(C\times C\) 上 effective sections、signed 对应、局部交数与 RR/Hodge，
全 Frobenius periods 及 H⁰/H² 两 pole 同对象身份才承担符号。

完整经典目标保留 Γ/contact、全部 prime powers、双 pole 与 complex mixed；
−4 普通迹异常不是这些片的完整同源预算。
指定修补电荷等于 Q 且正仍为旧 Weil 等价/充分包，并未取得独立容量。

## 6. 扣最强旧后的净后果与停止范围

424 已有同 lift 对称修补的抵消；427 已有整个 D 上的 trace-extension 障碍；
431/432 已有有限 source orbit 的非闭性与 Ω。
这些强旧没有给出本轮的实际单 generator：
**一个 537 正窗双矩零非根的 defect，借有限 Γ 隔离已迫使新代数理想含 −4 普通迹循环，
其 C* 闭包更准确等于全部原源闭理想。**
这是一项新增具体数学准入反测，可与本合同统一结算一轮；
新边/probe/连续模型及算术容量分别属旧直接合成或已有正控制，不另计轮。
既不能把这项新具体 proof 隐藏为来源0，也不能冒称新增经典正性或宏观方法边界完成。

范围限于固定 430 的扩大 A、共同 ideal 包含 I 与该 defect、并要求旧 Ω 自然因式分解/保 ordinary trace。
额外 P/B 未知全由原 E/u 最小域生成，故不能排较小原始代数。
新非标量 transgression、不同 regulator/relative pair、源依赖目标、强拓扑/合法无限 transfer、
filtered integral 数据均未被一般排除，须另给旧电荷去向、全 Pan/537/双 degree、原费与同对象 RR。
最强实际 ζ 仍为 542+555→557 whole leading4/5 上预算，非实际负谱 lower；
core/coupling/Ξ 与长期 Goal open/not-eligible 未变。

## 7. 最终版本绑定

审阅发现的两项表述风险已在最终稿消除：代表链费用不代 Ω 完成连续性；
ambient S₁ 非闭不判商分离。主稿 §§1、10 另已明确扩大 A 与较小原始源域的区别。
这些修订未改变独立重推的命题、−4 符号或闭包范围。

以下为本次实际文件字节 SHA256；hash 仅绑定审阅版本，不认证数学。

| 文件 | SHA256 |
|---|---|
| notes/573-relative-ideal-chain-closure-and-regulator-loss.md | da5ed121715fa71ce3e83c61aef7160825778ce0beeca8df39d4ae55fbb4cd93 |
| reviews/2026-10-22/relative-chain-closure/enlarged-ideal-and-trace-descent.md | 3c35ad285bc976e482f4810c083b2503489f5b5af894cdf5f3225dba1c3a12d0 |
| reviews/2026-10-22/relative-chain-closure/new-edges-and-regulator-charge.md | 60f35bad2c3f54d3709e38deb747c1b84e6f50fe17b46f5723e38ace6804ec1b |
| reviews/2026-10-22/relative-chain-closure/closed-charge-source-and-arithmetic-tests.md | d06679670d0b1d2c7be381e5b382e3ea8bfc800e6ecf38e8ca2022f0f8542ad4 |

正文或上述独占稿语义改变须重闭受影响前件。本稿未自行更新 cadence 或结算公共状态。
建议 C036 的实际 ideal 新反测统一结算一数学轮，停止固定 A 下保旧 Ω 的共同理想扩大；
保留已经列明的新相对/二层数据逃逸，不用本局部结果完成 G20261014。

## 8. 主稿 §10 实际相对 pair 的补充审阅

对新增的实际商映射 \(\pi:Q=A/I\to Q_J=A/J_*\)，取原代数 Hochschild 链及

\[
 R_n=C_n(Q)\oplus C_{n+1}(Q_J),\qquad
 d(x,y)=(bx,\pi x-by).
\]

这是所给链映射的实际 mapping fibre 复形：
\(d^2(x,y)=(0,\pi bx-b\pi x)=0\)。若 \((x,y)\) 为一循环，首分量满足 bx=0，
故 \(\Omega_{\rm rel}[(x,y)]=\Omega([x])\) 有定义。
若改变相对代表一个边界 \(d(a,b)\)，首分量只改变 ba，旧 432 已证明 \(\Omega(ba)=0\)，
所以该读出严格下降到 \(H_1(R)\)。这里不需把非 unital 新 ideal 的 naive 复形与 R 识别，
亦不需 H-unitality 或 excision。

旧 \(\zeta=q_I(T)\otimes q_I(T^*)\) 满足 bζ=0、πζ=0（后者在张量链层面已严格为零），
所以 \((\zeta,0)\) 是真实相对一循环，电荷为 −4。
若它为 R 中边界，其首分量 ζ 必为 Q 中的 Hochschild 边界，与 Ωζ=−4 矛盾。
因此**本 pair 的确保留单商所丢的电荷**，而非仅把它列作未知可能性。

与此同时，\((c_r,y)\) 成为 R 的一循环仍须 \(bc_r=0\)；第二腿仅修复 πcᵣ 的边界条件，
不能消掉首腿原有的非零 \(q_I(\delta F_r)\)。
所以该真实非零相对类不提供 raw 物理源的闭链比较，也不支付 Pan 同伦、537 同源保留、
filtered 算术截面 lift 或平方 RR。代表 T/T* 的有限链费与任意源比较费仍是不同责任。

新增控制限定 PASS，无 P1/P2。它准确缩窄 no-go：失败的是旧 Ω 沿单 quotient 的因式分解，
不是新的相对 pair 本身必失电荷。此标准 cone 控制不另增研究轮；C036 仍只统一一轮。
表中主稿 hash 已更新，三份独占原件 hash 未变；此前没有被改变的前件继续成立。
