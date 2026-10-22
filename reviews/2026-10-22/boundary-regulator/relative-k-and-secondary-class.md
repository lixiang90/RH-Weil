# Boundary regulator 的相对 K 类与 secondary 类：实际定义、零化及未付源覆盖

2026-10-22。独占原稿，供 root / fresh 审阅；不改公共状态、合同、cadence 或 Git。
同 G20261014、0c4f 冻结基线。已恢复 README、STATE、check/show、Goal、C035、宏观前沿及上轮 actual relative DGA 报告；本门只作一个可判的 boundary-regulator 准入检验。

## 1. 结论

可以给 407 的每个实际单向箭头复形定义一个**合法的代数 relative K0 triple**；不再停在只为非零对象命名。但该 relative 类是否非零仍未证明，且没有给任意物理源 r 到它的映射。

更便宜、可以闭合的反测是：这些单向箭头在逐 idele 的 trace-norm product topology 中给一条从恒等元出发的可逆路径，故对应的 topological K1 类及其 connecting boundary 都是零。它不否定代数 relative 类，也不否定更强、另有证明的算子场拓扑。

实际 DGA 上另一个自然尝试——先卷积指数化，再取相对 boundary——也能对全 S_exp 源严格定义，但其 boundary 必为零，因为该 unit 已有源中的 invertible lift。这一具体构造同时丢掉 537 非根，不能承担所求源桥。

因此“idele fibre 可缩”并不排除真正的 relative / secondary 数据；本门却没有得到可穿过该可缩性、同时保全主关系、537、原费用及局部 order / RR 容量的实际 regulator。

**强旧扣除不可止于407/408。** 410/411早已构造真实非零 boundary K 类，并在完整有理群作用下给来源明确的 2a log p 迹；414已有实际酉边界，432已有规范相对 HH1 电荷。下面“relative非零未证”仅指 (2) 的特定 Gaussian 单向 ring-map triple，不是对仓库全部 relative K 资产的判断。真正未付的是物理 DGA 到这些较强实际载体的同源比较、闭链/全主关系、过滤及平方容量。

## 2. Primary 的定点核查

本门仅核两条来源链：

1. [CCM2007 固定 v1](https://arxiv.org/html/math/0703392v1)，§8 Definition 8.2、Proposition 8.10 及其证明：在 adele 的 v 分量为零的闭子群胚上有真实限制同态 rho_v；局部动力学在其 kernel 上由 log|x_v| 的乘子实现为 inner。这里的 Xi_K 是原文的 periodic-classical locus，**不是**黎曼 Xi 函数的零除子。
2. [Weibel K-book Chapter II](https://www.math.rutgers.edu/~weibel/Kbook/Kbook.II.pdf)，Definition 2.10、Exercise 2.17；[Chapter IV](https://www.math.rutgers.edu/~weibel/Kbook/Kbook.IV.pdf)，1.11.1、Exercises 1.15–1.16：一般环同态的 relative triple、connecting map 与 homotopy-fibre 定义相容。没有把任意核范畴自动认同为该 homotopy fibre。

第二条适用于 407 的非交换单位化环；不能直接套仅对交换环给出的 relative Pic / gamma-filtration 结论。CCM 的 inner-kernel 证明也不是一个算术 Cartier divisor、K-localization、regulator 或 RR 定理。下面的简单路径和指数化结论由实际定义推导，不归作来源新定理。

## 3. 407 复形真正给出的 relative K 类

沿 407 取

\[
 R=(\mathcal S(\mathbb A_\mathbb Q)\rtimes_{\rm alg}\mathbb Q^\times)^+,
 \quad a=1_{\widehat{\mathbb Z}}\otimes\eta,
 \quad v=1-z aU_q,
\]

q 为素数，z 非零，eta 是 405 的明确偶 Gaussian 多项式，eta(0)=integral eta=0。R 只有有限箭头和。对 idele 轨道 b，令

\[
 B_b=\mathbb C I+\mathcal L^1(H_b),\qquad
 f_b=\rho_b:R\longrightarrow B_b.
\]

这是实际单位环同态；整个 R 的非单位部分在每个指定 b 上确为 trace class。407 给 v 在 R 中不是 unit，且两侧正则，而 f_b(v) 在 B_b 中可逆。

固定一个集合的 b 代表，代数乘积也合法：

\[
 B_{\rm id}=\prod_b B_b,\qquad
 f_{\rm id}:R\longrightarrow B_{\rm id}.
 \tag{1}
\]

这里只允许逐坐标数据，不要求共同 trace norm 上界，不将它冒称 CCM 的连续核算子场。对 f=f_b 或 f_id，已有明确类

\[
 \kappa_{q,z}(f)=[R,\ L_{f(v)},\ R]\in K_0(f),
 \qquad
 \kappa_{q,z}(f)=\partial[f(v)].
 \tag{2}
\]

模块取右模，L 为左乘，类型与 407 一致。其忘却像是 [R]-[R]=0。若改用 differential 的逆约定，只改变 (2) 的整体符号，不改变本门判断。

必须区别三个断言：

- K=[R --L_v--> R] 在 Perf(R) 非零：407 已证 H0=R/vR 非零。
- K0(R) 中 Euler class 为零：两项自由模直接给出。
- (2) 在 K0(f) 中非零：**仍未证明**。它是一个实际已定义的类，非零性不能由前两条推出，也不能由 determinant=1 推翻。

407 的 C_id 是所有 idele derived base-change 的共同核厚子范畴，但尚未证明 Perf(R)/C_id 等于 Perf(B_id)。所以不得直接将 K0(C_id) 与 K0(f_id) 等同，或把 (2) 与某个已证非零的 support K 类等同。定义 ring-map homotopy fibre 不要求 f 为 localization；认同“support category K theory”才须另付 localization / quotient 比较。

这一步补全了一个合法类型，未给新的 positive capacity，也未把 q,z 的有限族变成任意 r 的 source coverage。

## 4. Topological 分支：实际可逆路径使这一 boundary 为零

给每个 B_b 范数 |lambda|+trace-norm(T)，给 B_id 逐 b 的 product topology。固定 q,z 后

\[
 v_b(t)=1-tz\rho_b(aU_q),\qquad 0\le t\le1
 \tag{3}
\]

在每个 b 上 trace-norm 连续。407 的无闭合词证明适用于所有复参数 tz，给 det_F(v_b(t))=1，因此 v_b(t) 始终可逆，逆仍在 B_b 中。乘积拓扑下 (v_b(t))_b 也是 GL1(B_id) 的连续路径。

所以，在由稳定 GL 路径或相容 topological K-spectrum 定义的 K1_top 中，

\[
 [f_b(v)]_{\rm top}=0,\qquad
 [f_{\rm id}(v)]_{\rm top}=0.
 \tag{4}
\]

若使用 relative topological K 的 homotopy-fibre connecting map，其 boundary 同样为零。这比“一个 determinant 标量看不到”更明确，但范围仅是 (3) 的单向族、这一拓扑及这一 connecting 构造。

连续 t 不是代数 K 理论的等价关系，不能由 (4) 推出 (2)=0。也没有证明 (3) 在共同 uniform trace-norm、带增长约束的连续算子场等未指定目标中为路径。不得将逐 fibre 路径免费提升为后者。

## 5. 真实 DGA 的 quasi-isomorphism 与 regulator 能记住什么

上轮的非 unital DGA C=[S --partial--> B] 定义在实际 E_c 及两矩上，B=F_c+complex^2，degree cocycle 乘法已核。它有 canonical quasi-isomorphism

\[
 \mathcal C\longrightarrow H^0(\mathcal C)
 \simeq F_c/(CP_{\rm an}).
 \tag{5}
\]

E_c 单射付 H^-1=0；405/519 付闭像、两个 degree 和该商的识别。因此，对**只依赖该 DGA 的 quasi-isomorphism / derived-Morita 类型**的 ordinary regulator，(5) 使结果仍由旧解析商决定。用 K、Chern、determinant 给旧商换记号不产生新的算术容量。

这不排除给 pair(C→D)、integral model、filtration、metric、指定 boundary trivialization 或 cutoff family 增加真正新结构。Secondary analytic torsion 也可以依赖 differential 和 metric，未必只依赖 ordinary cohomology。例如有限复形 [complex --a--> complex] 虽可缩，固定两端 metric 后的 log torsion 可含 log|a|。这种数据并非 ordinary cohomology 中的非零类；须证明其选择依赖、变换律及实际源费用。不能一面用 quasi-isomorphism 消除全部结构，一面又称 torsion 免费记住了它。

## 6. 一个全源可定义、却必零的 boundary：卷积指数化

令 F_c=S_exp,C，卷积作为乘法，F_c^+ 为真正单位化；delta 只记新增 unit，不声称 delta 属于原 F_c。对整数 N,m>=0 定义

\[
 p_{N,m}(r)=\int e^{N|u|}|D^m r(u)|\,du.
\]

这些半范数与 S_exp 的指数加权 sup 半范数给相同拓扑：一个方向用更强指数权积分，另一个方向用加权 W^{1,1} 的 sup 估计。Young 不等式及将全部导数放在一个因子上给

\[
 p_{N,m}(r^{*n})\le p_{N,m}(r)\,p_{N,0}(r)^{n-1},
 \qquad n\ge1.
 \tag{6}
\]

故全源均可定义

\[
 \exp_*r=\delta+\sum_{n\ge1}\frac{r^{*n}}{n!}\in F_c^+,
 \quad (\exp_*r)^{-1}=\exp_*(-r).
 \tag{7}
\]

每一半范数绝对收敛，Cauchy 积合法；t→exp_*(tr) 在原 Fréchet 拓扑连续。单位化后的 j0:F_c^+→B^+ 把它送为 exp_B(j0r)。这不是从 F_c 到 407 交叉积 R 的同态；那条桥尚未构造。

对任意已给的单位环同态 f:A→D，只要把物理源先送为 A 中的上述 unit，relative exactness 立即给

\[
 \partial\,[f(\exp_*r)]=0\quad\hbox{in }K_0(f).
 \tag{8}
\]

特别 A=F_c^+ 或 B^+、D=H0(C)^+ 等真实已给卷积商均适用。这里不用拓扑路径：其在源中已是 unit，所以**代数** boundary 也为零。用 1+epsilon j(r)、epsilon^2=0 的一阶替代同理：有源 unit lift 时 connecting class 仍零。

因此这一自然 boundary-regulator 候选通过“消主关系”只是因为它消所有源；537 非根 r0 也被消掉。若改保 absolute K1 unit，在旧商里 generic 小参数 exp(tj(r0)) 可以非平凡，但它仍只记录 (5)，未获得 local arithmetic order 或 RR。

原费用也能明确给出，不能用零化掩盖它。对 supp r⊂[-L,L]，

\[
 \|r\|_1\le\sqrt{2L}\|r\|_{du},\qquad
 p_{N,0}(r)\le e^{NL}\sqrt{2L}\|r\|_{du}.
\]

 Fourier 端 |exp(hatr)-1|<=exp(||hatr||infinity)|hatr|，所以

\[
 \|\exp_*r-\delta\|_{Dlog}
 \le e^{\|\widehat r\|_\infty}\|r\|_{Dlog}
 \le e^{\sqrt{2L}\|r\|_{du}}\|r\|_{Dlog}.
 \tag{9}
\]

同式对 du 成立。高导数的 Fréchet 费用依赖 p_N,m，不能全由 du 控制。无界窗仍受 553 的全 Pan 稠密限制；这里既未付全域商 norm，也未产生 arithmetic sections 的 norm。

## 7. Fredholm torsion、真实边界与非零源覆盖的断点

407 的单向族 det_F(1-z rho_b(aUq)) 恒 1，因此用该标量或其 z 对数导数读出的 torsion 全零。它不是“所有 secondary invariant 都是 1”的定理：允许反向箭头后 407 的 mixed 二阶迹非零，辅助 t 平面的 Fredholm determinant 已能区分 q。但那不是 local divisor order、log q 的 primitive orbit 权重或完整 Weil 交数。

408 又给实际界限：Gaussian 零端点族在每个有限 p 的有限箭头边界 R_p 中非零，在所指定 ell1 completion B_(1,p) 中可逆而可缩；finite-p 非零性支撑是所有有限 p，不能直接叫“位于 q 的素数除子”。实原点值非零的不同族可以在该 completion 保留非零对象，却检测到共同原点字符，未有 q-selective local order。

更早的断点是任意物理 r 并没有给 407 的 adelic Schwartz 系数或有限箭头矩阵。Pan 源 q=E eta 才有实际 eta lift；537 r0 不在像中，正是非根见证。因此 r→K_(q,z) 或 r→kappa_(q,z) 目前**未定义**。不能给 q,z 的命名对象配一个任意 probe 系数后，就称之为 actual source coverage。外部 real idele scaling 的积分 U_r 亦不等于内部有理箭头的有限和。

单有 fixed-window 卷积费用也不能定义 Fredholm determinant：在全线 L2 上，非零 smooth compact 源的卷积是 Fourier 乘子 hatr；乘子在非原子谱空间非零便非 compact，更不属于 trace class。压缩、局部化或正则化可以另行定义，但必须给实际 domain、核项、费用和两个边界的协同；不得把 (9) 当 trace-ideal 许可。

## 8. 必须先扣除的更强旧 boundary 资产

本稿出稿后按 root 指定，已实际补读
[410](../../../notes/410-f1-boundary-kernel-bundles-and-relative-k-classes.md)、
[411](../../../notes/411-f1-full-rational-relative-classes-and-logarithmic-trace.md)、
[413](../../../notes/413-f1-two-place-boundaries-and-virtual-class-collapse.md)、
[414](../../../notes/414-f1-deep-boundary-unitary-and-time-defect.md)、
[432](../../../notes/432-f1-relative-cycle-charge-and-source-invariant-cutoff.md)、
[437](../../../notes/437-f1-finite-source-word-without-a-linear-physical-finite-part.md)
的定义与关键证明。不能用本门较弱的407 triple，重新提出仓库已解决过的“是否存在非零 boundary 类”。以下准确范围作为本门 baseline：

1. **410/411 的实际非零类。** 410 在真实 p^Z 子群胚扩张中给核丛 L_a，rank=a，而 determinant clutch 仅绕一次。411 改用完整 Q^times 不变实零层，定义
   \[
    \Omega_{p,a}=\delta_p[1-zU_p^a]
      =a\kappa_p^{src}+\beta_p^{src}\ne0.
   \]
   其共同实轴商上的半有限迹给固定参数配对 2a log p，log p 来自实际平移基本长度；参数混合项在该商中不再区分 p。该对数/幂次是加性 K 量，不是显式公式迭代权 log p；仍没有完整测试核及 principal/RR 身份。它与407的 Gaussian eta(0)=0、单向 determinant1 的 ring-map triple **不是同一对象或同一 boundary map**。
2. **413 的同源粘合与忘却。** 实际两位径向扩张给 boundary 秩映射 (r_p,r_q)→−(r_p+r_q)，故只允许有符号等秩对提升，普通 K0(I) 由 eta=(1,−1) 生成。该虚类及带参数提升在完整两位 A 的普通 K 中忘却为零；却不能由此称为405主关系，因为原周期读出对 eta 的局部测试非零。这里的 A 包含两有限位各零层、实坐标始终非零，并非全部 adele 空间。
3. **414 的实际 boundary unit。** 原分割函数 c（不是本题物理源 r）给 Green 投影及修正 q 箭头，构造 u∈A_D^~ 和实际一般提升 T∈A^~，两侧指数分别 −1、+1，得到 partial_D[u]=−eta。它没有可逆的 A^~ 提升，尽管在 multiplier M(A) 中有酉提升。因此§6的“已在源单位化有 unit lift 则 boundary0”**不适用于此 u**；不能把 multiplier lift 当作单位化 lift。414还在同一表示中给两位完整周期和的共同截断迹，但没有证明该读出消此 boundary 或下降为K类函数。
4. **432 的已定义规范相对电荷。** 在实际有界代数 A_src、Q_src=A_src/S1 上，商中闭的一链 c=sum a_i tensor b_i 的提升满足 sum[A_i,B_i]∈S1，普通迹给
   \[
    \Omega:HH_1(Q_{src})\to\mathbb C,
    \qquad\Omega(c)=\operatorname{Tr}\sum_i[A_i,B_i].
   \]
   它对提升、边界和源内共轭不变，并保留旧角点电荷 −4 integral s h(s)k(−s)ds。不能再把“任意相对电荷尚未定义”作为缺口。真正的原加权链 q(u*) tensor q(uF) 却有 boundary q(F−uFu*)；431/432证明非 trace-class F 的实际源上该差非紧，且有限个原 u 轨道修补不能闭合。这里 h,k 是旧时间平滑参数，与原分割 c、物理 r 分别保类型。
5. **437 的更强有限部停止。** 在最小真实源理想已经有合法有限词 Y=A(h)uA(k)，每次原物理压缩 trace class，却在任何线性体积扣除后没有共尾 finite part。它是合法 p=2,q=5 及特定原分割的存在性反例，不是全部分割/全部源词的普遍否定；保 phase、新边、受限域、自然平均、非线性重整化等另付来源的逃逸。故“将相对源闭包后原有限部自动延拓”不能作为新输入。

一个更具体、但仍失败的 raw-source 测试可以避免泛称所有映射都未定义：对 r∈C_c^infty，**明确另定义** h_r(s)=r(−s)，则旧实际 V、U(h) 给 F_r=A(h_r)=VU(h_r)V*，有
\[
 \|F_r\|\le\|V\|^2\|h_r\|_1
 \le\|V\|^2\sqrt{2L}\|r\|_{du}
 \quad(\operatorname{supp}r\subset[-L,L]).
\]
原 Dlog 右端可再用 ||r||du<=||r||Dlog/sqrt(log2) 运输；这里控制原有界算子 map，未控制一个尚未合法的闭链 regulator。
这只是一个合法原算子 map，未声称它已具有完整 Weil 的正确测试运输。对非零 r（包括537见证），432(8)的单项情形说明 F_r−uF_ru* 非紧，故自然加权一链仍不是 HH1 的源。该 recipe 有原 norm 上界，却没有进入 regulator 的 domain；它并不支付 local-order 或容量。要覆盖全 CP_an 还须合法延拓到原 Fréchet 域并证明其关系，而不是只在紧支域测试；553表明紧支域与主关系的交为零，紧支测试本身不能证明全主关系消失。

以上强旧内容说明，本门精确瓶颈不是“没有非零 boundary / regulator”，而是**已有实际非零类、电荷、原读出之间缺同一物理源的闭链/比较及容量**。新增§3–6的合法类型与零化仅解释两种最直接的 recipe 为什么不补这条箭头；不重计旧410–437为新成果。

## 9. 正反例及完整 Weil 责任

函数域给出精确正对照：在真实曲线的 generic field 上，rational function 是 unit，而在整模型有零极点；localization boundary 读出 valuations。其可能非零正是因为该 unit **不能**在有关整模型中 invertibly lift。principal relation、局部 order、真实截面乘法和 C×C 的 RR/Hodge index 是不同的已证设施。K boundary 的存在本身不推出平方容量或极化。

连续正反例则拒绝形式推论：对旧 R_d=C[z]/(z^2+d)、z-dagger=-z，d=+1/16 与 -1/16 都允许同样的指数化 / relative formalism，而 Q_d(A+Bz)=2|A|^2+2d|B|^2 符号不同。(8) 在两者都零，不能挑出正例。这里没有冒称任意连续 g 系统自动有加法 adeles 或真实 local arithmetic rings。

本门始终保 568 完整 Q_W 的 real Gamma/contact、所有 p^k proper powers、两 pole/degree；CCM rho_v 的存在与某个 inner cocycle 不证明这些项是同一 relative determinant line / arithmetic section 的 local order 与 arch capacity。若要求 regulator 有正极化，且其 pairing 被**定义**为 Q_W，就重新写了 Weil 正性。独立输入必须从实际整模型/截面/有效性证明该 pairing 身份与容量上界，而非将所求正号放进定义。

## 10. 可消费范围与停止

实际得到的是：合法 ring-map relative triple；ordinary Euler、relative 非零与 fibre 可缩的严格区分；逐 fibre topological boundary 的明确零化；全 S_exp 卷积指数及其原费用；unit-lift boundary 候选的全源失败。这些是 405/407/408/519/553 的直接后果与具体候选测试，不是新经典独立容量、Weil 正性或 whole 预算。

仍合法但尚未付的逃逸为：保 integral / filtered / metrized pair 的 secondary regulator；具有不可逆整 lift 的实际 source-dependent relative unit；保真 local support 的 algebraic localization；有原 norm / 成长费用的 boundary gluing 或非平凡双向箭头类。准入时须同时写出 r 的真实映射、全 CP_an 的等价/同伦、537 非根、local-order filtration、same-object primitive RR 及完整 Gamma/pp/pole 的预算比较。

在这些新数据出现前，继续给旧 quotient 取 Chern 名称或给单向 det=1 族增加样本不能改变选择。strong-old 542+555→557 的 whole leading 4/5 上预算及实际 core/coupling/Xi 缺口均未变。
