# 实际全源的代数 HH₀ 类：有限交换子精确消失

2026-10-28；unit_height 独占推导稿，供 root/fresh 消费。只核当前 action-cone 的实际 HH₀ 分支；不修改 STATE、cadence、Git，不预分配轮次。本稿不消费另一份高阶 inner-homotopy 或 regulator 推导。

## 1. 结论、对象及原件依赖

固定 430 的明确解析扩大域和实际 Hilbert 表示，而非较小的原始源代数：

\[
 A_c=C^*(A_{\rm src})\subset B(\mathcal H),\qquad
 I_c=A_c\cap\mathcal S_1,\qquad Q_c=A_c/I_c.
\]

430(12)已经把全部 \(\mathcal S_1(\mathcal H)\) 纳入 \(D_{\rm src}\)，因此本域确有
\(\mathbb K(\mathcal H)\subset A_c\)，且 \(I_c=\mathcal S_1(\mathcal H)\)。后一个等式没有把理想改为紧算子。\(Q_c\) 仍是按迹类取的**代数商**，不赋予 Hausdorff C* 商的角色。以下

\[
 HH_0(Q_c)=Q_c/\operatorname{span}_{\rm finite}\{[a,b]:a,b\in Q_c\}
\]

采用未完成的代数 Hochschild 复形，\(b_1(a\otimes b)=[a,b]\)。

**实际结论。** 对每个 \(r\in L^1(\mathbb R;\mathbb C)\)，令

\[
 h(t)=r(-t),\qquad F_r=VU(h)V^*,\qquad f_r=q(F_r).
\]

则存在至多 24 项的实际有限链

\[
 t_r\in A_c\otimes_{\rm alg} A_c,\qquad b_1t_r=F_r. \tag{1}
\]

所以

\[
 \boxed{[f_r]=0\quad\hbox{于 }HH_0(Q_c).} \tag{2}
\]

这覆盖全部 complex \(S_{\exp}\)、实际 noncompact 405/Pan 及 537 的全窗源；不是只留有限退化坐标。事实上 (1) 已在取迹类商之前成立。对每个非零 \(r\in L^1\)，\(F_r\) 仍非紧，故 \(f_r\ne0\) 作为 \(Q_c\) 元素；消失的是其 HH₀ 类，不是 raw 算子。

依赖的短链为：430 纳入全部迹类及实际 \(VBV^*\)；431 §6 单角稳定 C* 符号；573 的 L¹ raw 延拓；本稿 §2 的显式有限交换子恒等式；§3 实际提升及紧误差消去。没有使用无限源指标 Gram 的逆、外部无界乘子、自由 singular trace 或较小 smooth 代数的迹。

## 2. 稳定角内的三个交换子恒等式

先给可以逐项验证的通用构造。令 \(H\) 为可分无限维 Hilbert 空间，\(X\) 为紧空间；取
\(B_X=C(X,\mathbb K(H))\)。本稿分别用 \(X=S^1\) 和单点。

固定一次酉同构

\[
 H\simeq\bigoplus_{w\in\{0,1\}^{<\infty}}H,
\]

右端的空词为树根。令 \(W:H\to H\) 是根 copy 的等距嵌入，所以 \(W^*W=1\)。这里 \(W\) 只是定义有界组合的辅助算子；**不要求裸 \(W\) 属于 \(B_X\)、\(A_c\) 或源代数**。

给定 \(T\in B_X\)、\(T\ge0\)，定义

\[
 X_T=\sqrt T\,W^*,\qquad Y_T=W\sqrt T.
\]

它们属于 \(B_X\)：\(\sqrt T\) 是范数连续的紧算子值函数，乘固定有界算子仍为紧且连续。并且

\[
 [X_T,Y_T]=T-WTW^*. \tag{3}
\]

在树分解中，令 \(A_i(T)\)，\(i=0,1\)，把词长 \(n\) 的 copy 向其 child \(wi\) 送出
\(2^{-(n+1)/2}\sqrt T\)，其他矩阵块为零。每个 \(A_i(T)\) 有界，且

\[
 \|A_i(T)\|\le2^{-1/2}\|T\|^{1/2}.
\]

保留 \(n<N\) 的截断只含有限个紧算子块，故属于 \(B_X\)；其余部分满足一致界

\[
 \|A_i(T)-A_i(T)_{<N}\|
 \le2^{-(N+1)/2}\|T\|^{1/2}\longrightarrow0. \tag{4}
\]

这里的 \(\|T\|\) 是 \(X\) 上的 sup operator norm，因此 (4) 同时支付 fiberwise 紧性和 \(X\) 上的一致范数连续性，得 \(A_i(T)\in B_X\)。没有把一个无限重数的未衰减 compact 块当成 compact。

现在直接按树节点核对：词长 \(n\) 节点的总 outgoing 平方权为 \(2^{-n}T\)；若 \(n\ge1\)，其唯一 incoming 平方权也是 \(2^{-n}T\)，精确相消；根只有 outgoing 的 \(T\)。所以作为实际有界算子恒等式，

\[
 [A_0(T)^*,A_0(T)]+[A_1(T)^*,A_1(T)]=WTW^*. \tag{5}
\]

(3)+(5) 给出

\[
 T=[X_T,Y_T]+[A_0(T)^*,A_0(T)]+[A_1(T)^*,A_1(T)]. \tag{6}
\]

这是**三个实际交换子的有限和**。范数极限只用来构造各个合法腿，不是把 \(T\) 判进交换子空间的范数闭包。

任意 \(B\in B_X\) 按

\[
 B=(\Re B)_+-(\Re B)_-+i(\Im B)_+-i(\Im B)_-
\]

分成四个正部；各正部仍在 \(B_X\)，范数至多 \(\|B\|\)。将系数吸进 (6) 的一条腿，得

\[
 B=\sum_{j=1}^{12}[b_j,c_j],\qquad b_j,c_j\in B_X,
 \qquad\sum_j\|b_j\|\|c_j\|\le8\|B\|. \tag{7}
\]

零项可省。每个正部在 (6) 的三项 product-norm 总和至多 \(2\|T\|\)，因此最后常数直接成立。单点情形还证明每个实际紧算子都为至多 12 个紧算子交换子之和。这并不将普通迹延到全部紧算子；(6) 的各个乘积一般不是迹类，不能逐项以普通迹循环换序。

## 3. 431 稳定符号的实际提升：误差先紧，再精确消去

令

\[
 B_0=\overline{G_M}^{\|\cdot\|}
 \cong C(S^1)\otimes\mathbb K(L^2(0,M)),\qquad M=\log q.
\]

这是 431(15) 通过实际胞元分解、有限传播 Laurent 紧块及反向稠密性支付的**单角**完成。\(S^1\) 参数不是原 \(u\) 的谱参数。本稿不需要所有源指标的 C* 完成分类。

定义实际线性提升

\[
 \widehat\rho(B)=\tfrac12 VBV^*\in A_c\qquad(B\in B_0). \tag{8}
\]

在 \(G_M\) 上，(8) 的值已在原域；\(\|V\|^2\le2\) 给
\(\|\widehat\rho(B)\|\le\|B\|\)，故由范数极限得到整个 \(B_0\) 上的实际 \(A_c\) 值提升。这里没有假定裸周期谱乘子或树 shift 本身属于 \(A_c\)。§2 构造出的腿先经 431 同构落在 \(B_0\)，再用 (8) 提升，已支付它们的域。

用 \(\pi_K:A_c\to A_c/\mathbb K\) 表示这一步的辅助 C* 商。由于 \(\mathbb K\subset A_c\)，它与 Calkin 内的相应像一致。431(14) 给等距星同态

\[
 \rho=\pi_K\widehat\rho:B_0\longrightarrow A_c/\mathbb K,
 \qquad \|\rho(B)\|=\|B\|. \tag{9}
\]

这仅说 (8) **模紧算子**保持乘法，不说 (8) 在 \(A_c\) 内保持乘法，也不把完成后的乘法误差冒称迹类。

对任意 \(r\in L^1\)，用 \(C_c^\infty\) 在 L¹ 中逼近 \(h=r(-\cdot)\)。Young 界
\(\|U(h-h_n)\|\le\|h-h_n\|_1\) 和 \(U(h_n)\in G_M\) 给

\[
 B=U(h)\in B_0,\qquad F_r=2\widehat\rho(B)\in A_c. \tag{10}
\]

这明确包括 noncompact 源，不需其核仍有限传播。

按 (7) 写 \(B=\sum_{j\le12}[b_j,c_j]\)。则

\[
 E_r=F_r-2\sum_{j\le12}
       [\widehat\rho(b_j),\widehat\rho(c_j)]
       \in\mathbb K(\mathcal H), \tag{11}
\]

因为其 (9) 符号精确为零。\(E_r\) 可以不在 \(\mathcal S_1\)，所以不能此时就在 \(Q_c\) 中删去。将 §2 的单点构造用于这个**实际紧误差**，得到

\[
 E_r=\sum_{j\le12}[e_j,g_j],\qquad e_j,g_j\in\mathbb K\subset A_c. \tag{12}
\]

因此

\[
 t_r=2\sum_{j\le12}\widehat\rho(b_j)\otimes\widehat\rho(c_j)
       +\sum_{j\le12}e_j\otimes g_j \tag{13}
\]

是未完成代数 tensor 中的有限链，满足 (1)。把它沿 \(q\otimes q\) 送入 \(C_1(Q_c)\) 即证明 (2)。整个推导没有把 \(Q_c\) 当作 Calkin；只在 (11) 检出紧误差后，以 (12) 把这个误差重新付清。

此外，由 (9)–(10)，

\[
 \|F_r\|_{\rm ess}=2\|U(h)\|. \tag{14}
\]

Fourier 对角化和 L¹ Fourier 单射表明非零 \(r\) 有 \(U(h)\ne0\)。因此非零源的 \(f_r\) 作为代数商元素仍非零；(2) 不是“所有 raw 算子早已属于迹类”的退化论证。

## 4. 一份有 L¹ 费用的代表，不声称必要费或 canonical lift

(7) 与 (8) 给 (13) 首部分的 projective 代表费至多 \(16\|B\|\)。由 (11)，

\[
 \|E_r\|\le\|F_r\|+4\sum_j\|b_j\|\|c_j\|
 \le34\|B\|.
\]

(12) 的代表费至多 \(8\|E_r\|\)。故在实际 \(A_c\) operator norm 下，所选有限链满足粗界

\[
 \sum\|\hbox{left leg}\|\|\hbox{right leg}\|
 \le288\|B\|\le288\|r\|_1. \tag{15}
\]

这是显式构造的上界，非必要费用、最优常数、canonical 线性 source homotopy 或 \(\Omega\) 连续性。正部和开方使所展示的 \(t_r\) 一般并不依 \(r\) 线性；这不妨碍线性映射 \(r\mapsto[f_r]\) 恒为零。

保留原物理坐标 \(r(u)=e^{u/2}f(u)\) 及 Lebesgue 测度 \(du\)。若 \(\operatorname{supp}r\subset[-L,L]\)，(15) 给

\[
 \|t_r\|_{\pi,\rm rep}\le288\sqrt{2L}\|r\|_{du}
 \le288\sqrt{2L/\log2}\|r\|_{D\log}. \tag{16}
\]

对强 \(S_{\exp}\) 半范数 \(p_{N,0}(r)=\sup e^{N|u|}|r(u)|\)、\(N>0\)，有

\[
 \|t_r\|_{\pi,\rm rep}\le\frac{576}{N}p_{N,0}(r). \tag{17}
\]

这些都是 raw lift/代表的付费上界。没有给全线 du 或 Dlog 的统一代表费；也不从这个构造反推所有可能代表都不可能有更好费用。树与 C* 完成只在明确扩大域中支付，不把腿悄悄搬回原 \(A_{\rm src}\) 的有限传播/光滑域。采用 C* 域得到 (2)，并不等于免费获得同一算术整模型、可解截面、极化或成长控制。

## 5. actual 405/Pan、双次数及 537 控制

405 的 \(S_{\exp}\) 先为实空间，本稿取其 complexification；其全部元素均在 L¹，乘 \(C:f\mapsto e^{u/2}f\) 仍保持 \(S_{\exp}\)。原 405 实际解析关系是

\[
 P_{\rm an}=I\cap\ker d\cap\ker c,
 \quad I=\overline{E(S_{\rm even,0})}^{S_{\exp}},
 \quad d(f)=\int e^u f(u)du,\quad c(f)=\int f(u)du.
\]

对应物理关系为 \(C(P_{\rm an}\otimes\mathbb C)\)。对于全部这些 noncompact 关系，(2) 无条件给零；没有用 compact crop 替换 Pan。具体的非零实际源

\[
 \eta(s)=\pi s^2(\pi s^2-3/2)e^{-\pi s^2},\quad
 h_{405}=E\eta,\quad p=(D^2+D)h_{405},\quad P=Cp
\]

满足 405 的真实像准入及 \(d(p)=c(p)=0\)、\(M_p(2)=\pi/6\ne0\)。因此 \(P\ne0\)，由 (14) \(f_P\ne0\)，却 \([f_P]=0\)。这一测试实际覆盖 noncompact 源，而不只覆盖 573 所选 compact 非根。

同一消失也杀掉所有非关系方向。例如 405 的 \(h_{405}\) 有 \(d(h_{405})=c(h_{405})=1/4\)；相应物理 \(Ch_{405}\) 的两 pole 矩为
\(\mu_+=d(h_{405})\)、\(\mu_-=c(h_{405})\)，它的 HH₀ 类也为零。405 明确的两个独立次数方向 \(Cu_d,Cu_c\) 同样为零。因此这里并未留下可保双次数的有限 HH₀ 坐标。

537 已消费的同对象结论为：对每个
\(0\ne r\in C_c^\infty((-17/16,17/16);\mathbb C)\)，

\[
 Q_W(r)\ge2^{-49162}\|r\|_{du}^2>0. \tag{18}
\]

特别包括 573 的双 pole 零实际 \(r_*\)。但这些非根全有 \(f_r\ne0\)、\([f_r]=0\)。所以 HH₀ 并非只消去算术关系后保留正非根；本扩大域的这个 raw HH₀ source map 是全零。任何只依赖这份 HH₀ 类的泛函或二次读出也必全零，不能与 (18) 相等，亦不能由此得到非零 primitive 运输。

这是同一固定 source map 的完整反测，不声称所有不同相对 pair、较小域、额外边数据或不同 regulator 都失败；后一类对象须独立实际构造。这里不加自由 functional 来补回已被杀掉的源。

## 6. 与 strongest old 的净差及 root 消费边界

431 已有单角 \(B_0=C(S^1)\otimes K\) 的符号和 finite-word 加权边界单射；432 已有非零 HH₁ 电荷与源保持 cutoff 的有限读出。573 已有单一 actual \(r_*\) 的最小理想电荷障碍、**闭 ideal** 吞全 L¹ raw 源，以及旧 mapping-fibre 保 \(-4\) 类。这些都不等于
\(F_r\in[A_c,A_c]\)，因为闭 ideal、代数交换子空间和 HH₀ 是不同对象；原件亦未给 (6)、(11)–(13) 的有限交换子链。

本稿补出的准确新输入是：在当前声明的完成域中，全 L¹ 源（含全 noncompact Pan、双次数和全窗正非根）都有 **24 项以内的实际代数边界**，并有 (15) 的 L¹ 代表费；中间紧误差经实际紧腿消去，未删去 \(\mathcal S_1\) 外的误差。这比旧“norm-closed ideal 内全源消失”强，不能仅因宏观 RH 净果仍为零就把这份完整反例藏为来源摘要。

§2 的树构造本身是标准稳定代数的显式交换子机制；不主张世界新颖性。其与 431 的实际单角、(8) 的 lift、真实紧误差及 all-source/Pan/537 的完整比较是本次实际执行的消失测试，尚需 fresh/root 核验后决定统一数学迭代消费。此处不分配 C048/585，也不为树、提升和控制分别计轮。

它与旧 \(-4\) HH₁ 类没有矛盾：HH₀ 源消失不等于 HH₁ regulator 消失。若试图对 (6) 的非迹类乘积逐项施普通迹，反而会破坏使用域。高阶 inner-homotopy、源在 action-cone 分裂后的另一腿、原 \(\Omega\) 的实际延拓及 \(J_r\) 是否成为边界由另一独占稿核验；本稿不代为消费。单凭 (2) 尚不能把所有 source cone 类宣布为零。

宏观瓶颈仍是同一经典物理源到非零同对象 primitive/整过滤/截面/mixed RR 的桥及完整 signed 成长/core/coupling/Ξ；原 whole 4/5 负惯性 UPPER 预算未改变。这个 HH₀ 分支已实际判完，不能再保留“全源 HH₀ 标签未知”作为同一 canonical recipe 的未付希望。

## 7. 实际读入及可核字节

恢复已读 goals/README、STATE、当前准入稿，并运行 research_state.py check/show（均通过）；本稿数学实际读入如下。以下为 CRLF→LF 后 SHA-256；没有新取论文、未读额外证明，也没有以数值有限截断验证代替树的有界算子恒等式。

| 原件 | 实际范围 | LF SHA-256 |
|---|---|---|
| notes/430-f1-source-stable-periodic-smoothing-algebra.md | 全文；本次回核 V、D_src(12) | 86e7d443e8b88dc00345d959c8256c92e3addebf14344cebc083cb56d3a029b6 |
| notes/431-f1-source-orbit-essential-symbol-and-boundary-injectivity.md | 全文；本次回核 §6 全部同构和符号 | 352adafebc2a6bbe3b0dc935ccb1f4155a4792e912adec5193630f7813bdf2c5 |
| notes/432-f1-relative-cycle-charge-and-source-invariant-cutoff.md | 全文，比较 HH₁/截止范围 | da952ffa06cf918818ad8c994f14fc4740bd541d7dd1e7268718a3e09549d48b |
| notes/573-relative-ideal-chain-closure-and-regulator-loss.md | 全文，特别 §6–8、§10 | da5ed121715fa71ce3e83c61aef7160825778ce0beeca8df39d4ae55fbb4cd93 |
| notes/405-f1-adelic-restriction-moments-and-radical.md | 全文，消费 §2、§4–6 | fe5ee4b574954e51a69c6bbbaa772bb75a1a510c91c837ba02eed8ac406cbb7d |
| notes/537-source-exact-weil-window-positive-tail-admission.md | 全文，消费已验收 §2/§4 结论，不重跑来源 | 269a500556d37fc04a4e44efd2f0899414787743e529506dbbe7395a34eea9f8 |
| reviews/2026-10-28/unitary-premise/next-action-cone-hh0-admission.md | 全文，固定本次对象和停止范围 | a58676d1772619f6e6f9b32b3889a140cdda4abc589cfa9c4637312522ad8e4f |

无 pending process。所出为推导稿，不是 root-consumed 收据；唯一后续是独立核 §2–3 的域/恒等式并与另一分支合并，不自行续参数或新对象。
