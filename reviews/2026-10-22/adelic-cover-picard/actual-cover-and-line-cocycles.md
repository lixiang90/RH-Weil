# 实际 adelic atlas、等变线 cocycle 与相对 Picard 候选

2026-10-22，独占来源/候选准入稿。服务本轮实际覆盖与非平凡相对 Picard 门；不修改 STATE、cadence 或主稿。
已恢复 README/STATE、check/show、G20261014、C036、D20261022G、frontier 与上一模块门；固定 0c4f/同长期 Goal。
下述 groupoid descent 是标准直接构造，不宣称分类全部 Picard，也不把一个真实非平凡类当作独立 RR 容量。

## 1. 先固定真正的覆盖与两个拓扑

令 \(X=\mathbb A_{\mathbb Q}\)、\(G=\mathbb Q^\times\ltimes X\)，箭头 \((q,a):a\to qa\)。
实际 continuous quotient stack 的 atlas 是 \(X\to[X/\mathbb Q^\times]\)；其二重交叠为
\(\mathbb Q^\times\times X\)，三重交叠记录有理数乘法。这是以下 line descent 使用的对象。
只在这个 continuous 等变线范畴中工作，不把非交换 Schwartz crossed product 当交换结构环。

idele \(X^\times=\mathbb A_{\mathbb Q}^\times\) 使用自己的 restricted-product 乘法拓扑。
CCM2007 v1 §4.2–4.3、Prop.4.5/Lemma4.6 给 free/proper action、
\(\Delta_{\mathbb Q}=\widehat{\mathbb Z}^{\times}\times\mathbb R_{>0}\) 的连续截面及 pair-groupoid 模型；
这些输入只用于 idele 端的显式平凡化。[原件](https://arxiv.org/html/math/0703392v1)

**\(X^\times\) 不是 additive adeles \(X\) 中的开子集，不能把 idele restriction 叫作两片 Zariski/open cover。**
例如取不同素数 \(p_n\to\infty\)，令 \(a^{(n)}_\infty=1\)、\(a^{(n)}_{p_n}=p_n\)，其他有限分量为 1。
它们在 additive restricted-product 拓扑中趋于 1，却不在 idele 拓扑中趋于 1：后者一个基本邻域要求几乎所有有限分量都是单位。
任何 additive 基本邻域亦允许在一个未受限制的新素数处分量取零，因而不包含于 ideles。

每个 idele 有唯一分解 \(a=q(a)b(a)\)，其中 \(q(a)\in\mathbb Q^\times\)、\(b(a)\in\Delta_{\mathbb Q}\)。
其有理数部分由有限处 valuations 和实位符号确定；在 idele 拓扑中连续。
不从这个截面推出 full adelic stack 的 Picard 平凡，更不推出一般 global field 的截面存在。

## 2. 一份真正非平凡的相对 line 数据

对任意 character \(\chi:\mathbb Q^\times\to\mathbb C^\times\)，定义 underlying continuous line

\[
 L_\chi=X\times\mathbb C,
 \qquad q\cdot(a,v)=(qa,\chi(q)v).                 \tag{1}
\]

atlas 上的 transition 为 \(c(q,a)=\chi(q)\)，且
\(c(q,pa)c(p,a)=c(qp,a)\)。故这是实际 groupoid descent line，不是给某个自由 A 模换一个 frame。

若 \(\chi\ne1\)，其 full-stack line 非平凡。证明只看 \(0\in X\)：稳定群是整个 \(\mathbb Q^\times\)，
line fiber 为一维表示 \(\chi\)。到 trivial character line 的等变同构在 0 处必须是非零标量且 intertwine 两个 character，矛盾。
更一般，\(L_\chi\simeq L_{\chi'}\) 迫 \(\chi=\chi'\)。这里 underlying line on the atlas 虽自由，**下降后的等变 line 并非自由等变对象**。

在 idele 端却有明确 nowhere-zero 等变截面

\[
 s_\chi(a)=\chi(q(a)),\qquad
 s_\chi(qa)=\chi(q)s_\chi(a).                     \tag{2}
\]

因此 \((L_\chi,s_\chi|_{X^\times})\) 是实际 relative line with trivialization。
非平凡证据来自 full stack，不是从未知 zeta 零除子选择底空间，也不是上一轮 graph/Koszul 的恒 Pic 类。
这份设施确实存在；因此本门不应以“实际 adeles 没有任何非平凡 relative line”收口。

但非平凡证据当前仅由 0-isotropy 检出。\(\mathbb Q^\times\) 在 \(X\setminus\{0\}\) 上自由：
一个非零 place 分量即迫 \(q=1\)。这不证明 punctured action proper，也不证明该 line 在 punctured stack 上平凡；
只说明 0-isotropy 的论证没有证明 primitive 部分仍有非平凡 class。
实际源又满足原点消失，故不能把这个 boundary 见证直接当成消双 degree 后的 moving。

## 3. 带参数的真实族、base change 与 arch 图表

取 \(z\in\mathbb C\)，用

\[
 \chi_z(q)=|q|_\infty^z=\exp(z\log|q|_\infty).     \tag{3}
\]

则 (1) 在 \(X\times\mathbb C_z\) 给一族 continuous 等变 line，参数依赖 holomorphic。
这是“参数 holomorphic”，不是把 \(X\) 改造成 complex analytic variety。
任意连续/holomorphic 参数换底 \(T'\to\mathbb C\) 后，action 和所有 overlap identities 直接拉回；无新的 flatness 假设。

该族 faithful：若 \(\chi_z=\chi_w\)，则 \(2^{z-w}=3^{z-w}=1\)。实部先为零；
若虚部不零，便有 \(\log2/\log3\in\mathbb Q\)，与唯一分解 \(2^m\ne3^n\) 矛盾，故 \(z=w\)。

真正 invariant additive-open 图表
\(U_\infty=\{a:a_\infty\ne0\}\) 上已有截面

\[
 h_z(a)=|a_\infty|^z,\qquad h_z(qa)=\chi_z(q)h_z(a).\tag{4}
\]

它在 idele 端同样给合法平凡化；与 (2) 的比值是 \(\Delta\) 上 nowhere-zero 函数 \(b_\infty^z\)。
所以 full-stack 非平凡性不意味着所有实际 arch 图表都缺少 frame，更不意味着有非零有效除子。
对更一般固定素数 \(p\)，也可用参数 \(t\in\mathbb C^\times\)、character \(\chi_t(q)=t^{v_p(q)}\)，
idele frame 为 \(t^{v_p(q(a))}\)。此为标准 Laurent 参数族；不独自指定 degree-zero 或极化。

## 4. 实际物理源 map：能保非根的裸候选失败全关系

物理源仍为 \(r=e^{u/2}f\in F_c=\mathcal S_{\exp,\mathbb C}\)。
具体候选 \(r\mapsto(L_{\ell_0(r)},h_{\ell_0(r)})\)，其中

\[
 \ell_0(r)=\int_{\mathbb R}r(u)\,du.               \tag{5}
\]

不预设零点位置；实际定义在全源，族参数和 frame 都有公式。
537 的 \(r_0=(D^2-1/4)\psi\)、\(0\ne\psi\ge0\) compact，满足
\(\ell_0(r_0)=-\frac14\int\psi\ne0\)，故 (3) 的非平凡性保住此见证。

但 405 的全主关系门失败，且有准确非零见证。记原 405 函数 \(p_0=(D^2+D)h\)，\(P=e^{u/2}p_0\)。
旧 Gaussian Mellin identity 直接给

\[
 M_{p_0}(s)=\frac{s^2(s-1)^2}{4}\pi^{-s/2}\Gamma(s/2)\zeta(s),
\quad
 \ell_0(P)=M_{p_0}(1/2)
  =\frac{\pi^{-1/4}\Gamma(1/4)\zeta(1/2)}{64}<0.   \tag{6}
\]

负号不需要 RH：\(\eta(1/2)=\sum(-1)^{n-1}n^{-1/2}>0\)，而
\(\zeta(1/2)=\eta(1/2)/(1-\sqrt2)<0\)。因此 \(L_{\ell_0(P)}\) 非平凡；
来源上的真实主关系没有变成 trivial line。compact 域内主关系空交不能修复这个全源反测。

若改用 \(\ell=\mu_+\) 或 \(\mu_-\)，虽消全部 physical Pan，却使 double-pole-zero 的 537 \(r_0\) 也变为 trivial。
405 的 \(h\) 两 degree 仍为 \((1/4,1/4)\)，不能把全 \(I_c=E_cS\) 误称 principal 而删两 pole。
若用真正逐位平迹 \(\mathcal L_p\) 给 (3) 或 \(t^{v_p}\) 参数，旧 boundary 门已给
\(\mathcal L_p(P)>0\) 对每个有限素数成立；依然失败全主关系，不可只测所选窄支撑源。

## 5. 何种修补只回到旧商，何种仍合法

对任何线性 \(\ell:F_c\to\mathbb C\)，要求
\(L_{\ell(r+q)}\simeq L_{\ell(r)}\) 对全部 \(q\in P_c\)，由 (3) faithful 即迫
\(\ell(P_c)=0\)。因而 \(\ell\) 必须经过旧 \(F_c/P_c\)。
这不是说所有非平凡 relative lines 都是旧源商；而是说**本 character-parameter recipe 的全关系兼容参数必因式分解旧商**。
选已有 Mellin/谱泛函使其保 \(r_0\) 是合法数学对象，却没有增加独立的 effective/filtered/metric 数据。

原全线 \(du/Dlog\) 拓扑若要求 \(\ell\) 连续，旧 553 的 Pan 稠密性迫 \(\ell=0\)。
更一般共同 Hausdorff 模空间中的连续、全 Pan-coset 不变 map 也退化为常值。
Fréchet 拓扑、变域、非共同 target、fixed-window/cofinal 有费族并未排除；
本稿未分类这些修复，也不以一次裸参数失败否定所有 source-adapted Picard family。

这里 ordinary “base change 和 triple overlap”已经有实际公式；新缺口不应继续写成抽象无拼接。
尚未给出的，是区别于旧 quotient parameter 的 arithmetic/local Cartier moving、
以及相同对象上关系保持的原 metric section lift。

## 6. 原 du/Dlog 费用与不能免费消费的地方

若 \(\operatorname{supp}r\subset[-L,L]\)，则

\[
 |\ell_0(r)|\le\sqrt{2L}\|r\|_{du}
 \le\sqrt{2L/\log2}\|r\|_{Dlog}.                  \tag{7}
\]

在 arch 代表 \(a_\infty=e^u\)、\(|u|\le R\) 上，(4) 及其逆满足

\[
 \max(|h_z|,|h_z|^{-1})\le e^{R|\Re z|},
\]

所以将 \(z=\ell_0(r)\) 代入得到显式 fixed-window/fixed-chart fee。
有理箭头 \(|\log|q||\le H\) 上同理得 \(e^{H|\Re z|}\)。
当 \(\Re z\ne0\)，没有所有 idele/所有 rational arrow 的统一此类上界。
这是本指定 frame 的实际费用，不是每种可能 Picard lift 的必要下界。
全 \(F_c\) 的 (5) 连续于原 Fréchet 拓扑，但不在全线 du/Dlog 上有界。

若限制 \(z\in i\mathbb R\)，(1) 有真正 invariant positive fiber metric，(4) 模长 1；
这给 flat unitary character line，却仍不通过上述全 Pan/537 双门，也没有有效消失过滤。
若 \(\Re z\ne0\)，在 0 处不存在非退化 invariant positive fiber metric：
isotropy 要求 \(|\chi_z(q)|=1\)，取 \(q=2\) 即矛盾。
这不是 RH 条件，而是当前 character line 的 elementary metric gate。
有一份正 fiber metric 亦不同于 primitive intersection/RR 正性。

## 7. 函数域与连续正反控制应如何消费

函数域真正的 degree-zero line 来自局部 DVR frames 的除子：
idele \(a=(a_v)\) 给 \(\sum_v v(a_v)[v]\)，乘 global rational function 改变 principal divisor，
乘 local units 不改线类；degree 是 \(\sum_v v(a_v)\deg v\)。
这与“\(K^\times\) 在 additive 0-isotropy 上的任意复 character”是不同对象。
前者还有 proper 曲线及其 Picard functor，degree-zero family 模 base line 后由 Jacobian 控制。
具体 proper/base-change/Picard 规范参见 [Milne JVs §1/§7](https://www.jmilne.org/math/xnotes/JVs.pdf)。
旧 genus-two \(L_0=O(P+Q-2\infty)\) 的非平凡 twist 改变有效化后的 \(h^0\)，
不靠 additive 原点的 isotropy；本 character family 尚未给相应 DVR、valuation 或 section space。
因此不能把在 idele 端被显式平凡化的 \(L_\chi\) 与 \(\operatorname{Pic}^0(C)\) 直接认同。

连续正反模型 \(Z_c=1+c/[s(s-1)]\)、\(d=c-1/4=\pm1/16\) 仍有既定两 pole/完整 prime 分布、真实 \(\Gamma=0\)。
共同的物理源 probe (5) 和普通参数 line 操作不使用 \(d\) 的正号信息，
故不能由它们推出 \(Q_c=2|A|^2+2d|B|^2\) 的 mixed 正性。
没有给这些模型伪造经典 adelic base；控制只说明源积分、character/fiber positivity 或 formal overlap 不含区分符号的输入。

## 8. 完整经典预算、净后果与止损

本候选没有改变旧 405 的完整 normalized explicit formula：
arch \(\Gamma/contact\)、全部 \(p^k\) 和双 pole 必须共同保留。
(6) 与 \(\mathcal L_p(P)>0\) 说明局部/裸参数不消关系；补偿不是可删除误差。
尚无同一 line 的 arch capacity 等于完整 \(\Gamma\)、finite valuation multiplicities 等于所有 proper-power 权、
以及 RR degree defects 等于双 pole 的 identity。

实际新增决策信息是：在真正 adelic atlas 上，非平凡相对 character lines 与所有参数交叠可明确给出；
所以 free-graph 恒类并未排除这些设施。最便宜的全源 map 仍失败 405；degree-only 修补又失败 537；
强制全关系的连续参数则回旧商/553。这是标准设施与旧反测的具体准入核查，不冒称新数学轮或容量定理。

按用户 stop rule，本 character-source recipe 在此停止，不调 character、probe 或 chart。
可重新准入的数据应为：源依赖实际 local Cartier/idele module 的非平凡 moving，
全 Pan 的真实 rational/local-unit relations，保 537/双 degree，原域 metric/overlap 费用，
以及至少一项独立 valuation/effectivity/proper section-budget 输入。
仅把一个旧 quotient functional 写进非平凡 line 的参数不够；整个一般 Picard/相对方法并未被排除。
经典独立容量、whole leading4/5/core/coupling/Ξ 及宏观 Goal 门均未改变。
