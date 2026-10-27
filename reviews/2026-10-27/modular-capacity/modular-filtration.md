# 固定 Borcherds 模输入的有限主部过滤与实际拓扑

2026-10-27；按 STATE 的唯一下一比较，只核固定格／weight／Weil 表示的 honest weakly holomorphic 输入空间。恢复已读 AGENTS、README／STATE、check→show、G20261027、A20261027、D20261027B 与前沿；不改 STATE／Goal／cadence，不开 C046。本稿给主代理消费的标准基础证明，不自行结算数学轮。

## 1. 固定对象与来源

唯一数学原件为 [Borcherds 作者 PDF](https://math.berkeley.edu/~reb/papers/aut/aut.pdf)，本地 `literature/local/2026-10-27-weil/borcherds-automorphic-products-1998-author.pdf`，SHA256 `93618b64a0c07f68a085b0b520079b1062a98ff7672159f34f77b1463e0724d2`，448471字节、64页。实际用 pdftotext 重读 §2（PDF8–9页）、§4 的表示定义／有限商（PDF13页）以及 §13 Thm13.3、Example13.5（PDF47–50页），并对照作者URL的PDF文本；不串论文。

版本必须分层：1998是刊年，首页标1996-09-29／corrected1997-05-29；但本次同一字节文件在PDF25页含 `Remark added 2018-2-23`，限定 §6 中 h± 非零的多项式陈述，且注明不影响 §13／14。因此首页日期不是整个文件最后改动时间。这个内部注记不改变本稿所用 §4 有限表示或 §13 输入定义。

固定偶格 M，signature(2,b−)，V=C[M′/M]，d=dimV，ρ=ρ_M，k=1−b−/2。ρ 是原 metaplectic group Mp2(Z) 的表示；k 可为半整数，必须保原平方根 automorphy factor。作者 §4 明确：ρ 经一个有限群分解，偶维为 SL2(Z/NZ)，奇维为其 double cover。这支付了本次需要的 finite-image／有限阶 ρ(T)，不是对所有抽象 multiplier 的假设。

令 E=M_k^!(ρ) 是所有满足该固定 automorphy law、在 H 内全纯、只在 cusp 处亚纯的 V 值形式。先取**复线性包络**，不强加 Thm13.3 的 m≤0 系数整性。实际整输入只形成其中一个加法子集；它本身不能被不加说明地当成复向量空间。

输入 F 在 H 内全纯；输出 Ψ 的 rational quadratic divisors 是另一对象的奇性。不能把输出允许亚纯反向搬入输入 E。

## 2. 精确的有限主部过滤

由于 ρ(T) 有限阶，可在固定 V 基底中写

\[
 \rho(T)e_\lambda=e^{2\pi i\alpha_\lambda}e_\lambda,
 \qquad 0\le\alpha_\lambda<1,
 \quad\alpha_\lambda\in\mathbb Q.
\]

于是

\[
 F_\lambda(\tau)=q^{\alpha_\lambda}
       \sum_{n\in\mathbb Z}a_\lambda(n)q^n,
 \qquad q=e^{2\pi i\tau}.
\]

在 H 全纯和 cusp 亚纯正是每个分量只有有限多个负指数项。有限个分量使所有负阶可由一个整数界住。定义

\[
 E_N=\{F\in E:a_\lambda(n)=0\ \text{for all }\lambda,\ n<-N\},
 \qquad N=0,1,2,\ldots .
 \tag{1}
\]

则 E_0⊂E_1⊂⋯，E=⋃_N E_N。等价地，每个全 exponent m=αλ+n 满足 m≥−N；没有把有理 exponent 当整数删除。若改在某个固定有限指数 subgroup 的各 cusp 写局部参数，只有有限个 cusp／固定宽度，可取所有局部极阶的共同整数上界。原文 §2 Example2.2 已把这些 cusp 数据纳入一个有限维 induced representation；本稿本来就在 full-group vector-valued 模型中，不能忽略其分量。

“每个 F 有一个有限极阶”不表示“整个 E 已先固定同一个 N”。后者若由 Baire 获得，是源映射的额外结论。

## 3. E_N 有限维：不先借新的算术 RR

先证明每个固定 weight w 和 fixed ρ 的 holomorphic-cusp 空间 M_w(ρ) 有限维。下面是常规复分析证明，避开半整数权线丛紧化的额外记号。

取标准 SL2(Z) fundamental domain 和固定 Y>1。其 y≤Y 部分 K 是 H 中紧集。对 holomorphic-cusp F，写 Fλ=q^αλ hλ(q)，其中 hλ 在 q=0 全纯。最大模原理给 y≥Y 时

\[
 |F_\lambda(x+iy)|\le
 e^{-2\pi\alpha_\lambda(y-Y)}
 \sup_{x\bmod1}|F_\lambda(x+iY)|
 \le \sup_{x\bmod1}|F_\lambda(x+iY)|.
 \tag{2}
\]

因此 fundamental domain 上的 sup 是有限值，并由 K 上 sup 控制。记该 supnorm 为 p(F)；它是一个真正的 norm，F 在含内点的 K 上为零即在 H 全零。

对任意 H 内紧集 K′，只有有限个 fundamental-domain translates 参与覆盖；固定 automorphy factor 和有限个 ρ 矩阵给 K′ 上的局部一致界。故 p 单位球是 normal family。Montel 给紧开收敛子列，模变换等式在极限保留。各 hλ 在 |q|=e^(−2πY) 的一致收敛配合最大模原理，给整个 cusp disc 的一致收敛及 cusp 全纯性；并使该子列在 p-norm 收敛。于是 p 单位闭球在 p-norm 中紧，由无限维赋范空间单位球不紧的标准结论，M_w(ρ) 有限维。

该论证保留原 Mp automorphy，不把半整数权擅自当成整数权 scalar form。若中心相容条件令某些分量必为零，先取其允许子空间，只会减小维数。

现在用经典 discriminant cusp form Δ：它在 H 无零点、weight12、q 展开首项 q，在唯一 full-group cusp 简单消失。对每个 N，乘法

\[
 E_N\longrightarrow M_{k+12N}(\rho),\qquad F\longmapsto\Delta^NF
 \tag{3}
\]

是线性单射，且消去 (1) 中全部负项；故 dim E_N<∞。这里 Δ 是普通 modular-form 背景设施，乘法与有限维论证不是经典 ζ 的新算术容量。若采用多 cusp subgroup 表述，Δ 在各 cusp 的消失阶等于其宽度，仍可用足够整数幂同时消极阶；无需假造只有一个 cusp。

等价几何解释是：fixed automorphy data 在紧化 modular curve／metaplectic orbifold 上给固定有限秩 coherent automorphy sheaf；加 fixed cusp pole divisor ND 后 H0 有限维。半权和有限 isotropy 由局部有限群 invariants 处理，不能略掉它们就宣称 ordinary scalar line。式(2)–(3)已直接支付本稿需要的有限维，不要求先构造数域 Weil RR。

## 4. 真正需要的目标拓扑与闭层

给 Hol(H,V) 其紧开拓扑，即 p_K(F)=sup_{τ∈K}||F(τ)||，其中 K 遍历 H 内紧集；这是 Hausdorff locally convex 空间。给 E 其子空间拓扑，不在此声称 E 完备。

每个有限维 E_N 在这个 Hausdorff TVS 中闭。因此 E 是一个**可数递增的闭有限维层之并**。还可直接核闭性：在固定 height 横截线上作有限区间 Fourier 积分，每个 aλ(n) 是连续线性泛函；E_N 由全部 n<−N 的这些泛函为0定义。Full automorphy law 也是点值等式的闭条件。

也可以给 E strict locally convex inductive-limit 拓扑 lim→E_N，视为 countable finite-dimensional LF 型空间；各层仍闭。此拓扑通常强于紧开子空间拓扑，不能把二者直接等同。对后续 Baire 比较，紧开拓扑已足：源映射若连续到更强 LF，自然也连续到紧开 E。真正需要的是各层逆像闭，不是声称目标 E 自己是 Baire 或 Fréchet。

每个 fixed E_N 内范数等价并不提供 N-uniform 原 du／Dlog 常数，也不提供 r→F 的连续性。这里没有实际源映射；若将来只给代数 map、逐系数 map 或未说明的 completed target，不能自动消费当前结论。逐系数连续若系数族确实分离且 E_N 由连续负系数约束为0，也可单独支付所需闭逆像，但仍需实际证明。

## 5. 实际 scalar 控制：II_(2,2) 与 C[j]

在原文 Example13.5 的 even unimodular signature(2,2) 模型，ρ 为平凡表示、k=0。令 J=j−744=q^−1+196884q+⋯，原例用的是真正 H 内全纯、只在 cusp 有一个简单极点的 elliptic modular function。

对任意 F∈E_N，用其 q^−N 系数减去相应倍数的 J^N，再逐阶减 J^(N−1),…,J，消掉全部负项。余项为 H 上及 cusp 上全纯的 weight0 modular function，降到 compactified modular curve 的全纯函数，故为常数。反之每个 J^m 都是允许输入。由不同 leading pole q^−m 线性独立，得到

\[
 E_N=\operatorname{span}_{\mathbb C}\{1,J,\ldots,J^N\},
 \quad \dim E_N=N+1,
 \qquad E=\mathbb C[J]=\mathbb C[j].
 \tag{4}
\]

这个证明不先借 j 是全函数域生成元或 genus0 的更强命题；只用原例的简单 cusp pole、holomorphy 与紧化上的 maximum principle。M=II_(2,2) 不是说输出乘积的 divisor/line/character 或数域 primitive 容量已解决。

Thm13.3 还对 m≤0 系数要求整数。应先在这个真实整数输入类上应用产品定理，再说明何种 divisor/current／Hermitian pairing 可以复化；不能把 (4) 的任意 complex polynomial 本身说成 theorem13.3 的 integral input。有限维复杂包络 E_N 仅提供一个包含真实输入的容量上界。

## 6. 必须保留的范围与逃逸

* 若允许输入 F 在 H 内任意移动的点有极点，E_N 会失去上述有限维性质。例如 distinct generic a 的 1/(j−a) 在 cusp 无极点，却有不同 interior poles 并线性独立。它们是合法亚纯 modular functions，但不属本次 Thm13.3 的 H-holomorphic 输入。
* 若允许 cusp essential singularities，e^j 等函数仍在 H 全纯，却不在有限 principal-part 并 E 中。旧 theorem13.3 的 product/regularization 不能直接扩域；不把这个 analytic escape 当成已付算术 lift。
* 若 lattice／weight／representation、边界类型或输入 sheaf 随源变化，当前 fixed-data 空间不是其自动共同目标。若先构成确实 Hausdorff 的 countable finite-layer direct sum，则可另做同类比较；不能凭“有可数标签”跳过实际拓扑、闭层及 source 比较。
* 非线性源 map、先实际整数／有理源几何后复化、完成化输入、relative complex 或直接 Green 配对未被本稿排除。输出 Ψ 非线性也不能只由 input 有限维自动推出其所有可能后处理有限 rank；必须核目标 mixed 型是否真正经一个线性源 map 因子化、并核零输入的几何读出。

本稿严格闭合 fixed-data honest weakly holomorphic 输入的 finite-dimensional filtration／closed layers／countable union，以及 scalar C[j] 控制。它未构造 r→F，未付 physical 原 du/Dlog 连续性、全405 principal、537可见性、完整 Bζ identity 或 RR。Strong-old whole4/5 负惯性 UPPER、actual q/core/coupling/Ξ 状态完全不变。与580／552／553相比的净约束和是否形成新完整数学迭代，须由root在全部分支对齐后判断，不能由本稿文件数量或标准基础引理自行升级。
