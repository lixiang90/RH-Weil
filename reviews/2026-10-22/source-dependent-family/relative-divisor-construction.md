# 源依赖除子族：实际 graph/section 的两种构造与准确停止点

2026-10-22。子任务独占稿；不修改公共 STATE/cadence、不建立合同，不将本稿当作已被 root 消费的结果。
已恢复 README/STATE、check/show、同 G20261014/0c4f Goal、MACRO_FRONTIER、C035 与 D20261022A；
本稿直接消费 405、519、520、537（经 552/568 指定坐标）和 553 的已付资产。
本轮不是新证 RH，不把以下相对化重新计为新的独立谱实现。

**结论先行。** 真实的源依赖 divisor/section 族可以写出，因而“仍没有任何实际映射”过强。
有两种必须分开的成功范围：

1. 有界平滑探针给 ​P¹ 上 moving graph，原 du/Dlog 费用便宜；它甚至可同时杀指定 p/h、保 r0，
   但不能杀全部解析主关系。只测一两个关系会误判。
2. 用旧 Mellin 关系理想作非约化解析底空间，可给**全部关系相容**的实际 global section 与相对 graph。
   它不经过完整 J_W，但把旧谱商本身放进底空间；因此不是独立算术容量，也没有缩减 Weil 正性的责任。

## 1. 固定坐标、关系与非根

所有源先用物理坐标

\[
 r(u)=e^{u/2}f(u),\qquad
 A_r(z)=\int_{\mathbf R}e^{zu}r(u)du=M_f(1/2+z).
 \tag{1}
\]

对 \(r\in S_{\exp,\mathbf C}\)，A_r 为整函数；compact 源是其子域。
旧 405 的 Gaussian h 与 p=(D²+D)h 有

\[
 M_h(s)=\xi(s)/2,\qquad M_p(s)=s(s-1)\xi(s)/2.
\]

写 \(r_h=e^{u/2}h\)、\(r_p=e^{u/2}p\)，于是

\[
 \Xi(z)=\xi(1/2+z),\qquad
 A_{r_h}=\Xi/2,\qquad A_{r_p}=(z^2-1/4)\Xi/2.       \tag{2}
\]

这是完整、自然完成化的 ξ；不以未知零点位置定义它。
537 的实际非根为

\[
 r_0=(D^2-1/4)\psi\ne0,\qquad
 \psi\in C_c^\infty((-17/16,17/16)),\qquad Q_W(r_0)>0.
 \tag{3}
\]

两个 pole 矩为零，且 \(A_{r_0}(z)=(z^2-1/4)A_\psi(z)\)。
非零 ψ 不可能使 r0=0（否则紧支 ψ 解齐次 ODE）。
必须分开：405 的 B 商消 \(P_{an}\) 并保 h 的两次数；完整 Q 商消整个 I，故 h 也为 Q 零类。

## 2. 不含 J_W 的原范数有界 moving graph

取固定非零实 \(\zeta\in C_c^\infty(I)\)，定义复线性读出

\[
 a(r)=\ell_\zeta(r)=\int r(u)\zeta(u)du.                \tag{4}
\]

普适族在 \(\mathbf P^1_{\mathbf C}\times\mathbf A^1_{\mathbf C}\) 上为

\[
 s_t=X-tY\in\Gamma(\mathcal O(1)),\quad
 \Gamma_t=Z(s_t),\quad
 \Gamma_t-\Gamma_0=\operatorname{div}\frac{X-tY}{X}.     \tag{5}
\]

把 t 拉回为 a(r)，得到实际 source-dependent divisor 和 marked section。
仿射图 Y≠0 时方程 z−t 为 monic，故是非零因子；另一图同理。
每纤维 Γ_t 为有效 Cartier 除子，实际全局截面是 s_t，非零源部分可取
\(s_{a(r)}-s_0=-a(r)Y\)。
这不是“把向量命名为截面”：P¹、O(1)、截面及零子概形均已给公式。
但其三个不同角色不能合并：

* Γ_t 是 moving effective divisor，所有纤维线丛类同为 O(1)。
* Γ_t−Γ_0 是实际 principal divisor，因此 Picard 类恒为零。
* marked section s_t 保留 a(r)；其源部分是否为零取决于 a(r)，不是 Picard 类。

上述 effective Cartier divisor/regular section 的区别与
[Stacks Lemma 31.15.10](https://stacks.math.columbia.edu/tag/01X0)一致；
实际非零因子检查已在本稿直接做出，不借一条未读的几何正性定理。
仅浏览该 lemma 与 [31.14 的定义](https://stacks.math.columbia.edu/tag/01WQ)，不声称其余章节已核读。

### 2.1 费用与同对象局部核确实可付

原 du 与 568 的 zero-extension Dlog 范数给

\[
 |a(r)|\le\|\zeta\|_2\|r\|_2
 \le (\log2)^{-1/2}\|\zeta\|_2\|r\|_{Dlog}.             \tag{6}
\]

P¹ 上给 O(1) 以固定 Fubini–Study metric，截面 X−aY 的 sup 范数恰为
\(\sqrt{1+|a|^2}\)。因此

\[
 \log\|s_{a(r)}\|_{sup}
 =\tfrac12\log(1+|a(r)|^2)
 \le\tfrac12\log(1+\|\zeta\|_2^2\|r\|_2^2).          \tag{7}
\]

对同一纤维、\(V_n=\mathbf C[z]_{\le n}=H^0(\mathbf P^1,\mathcal O(n))\)，
实际 k-jet 评价为

\[
 e_{a,k}:V_n\to\mathbf C[z]/(z-a)^k,\quad
 \ker e_{a,k}=(z-a)^k V_{n-k},\quad
 \operatorname{rank}e_{a,k}=\min(k,n+1).                \tag{8}
\]

约定 n−k<0 时核为零；(8)由欧几里得除法直接证明。
有序消失可乘，\((z-a)^kV_{n-k}\,(z-a)^lV_{m-l}\subset (z-a)^{k+l}V_{n+m-k-l}\)。
全局容量 \(\dim V_n=n+1\) 与 a 无关，且已在同一对象内得到。
这是真实的 kernel/乘法/容量成功范围，但它是曲线的一次容量，不是 primitive signed 对应的二次 RR。

### 2.2 同时通过 p/h/r0 仍可明确失败

甚至不用 J_W，也可让(4)同时杀两条指定关系、保非根。
取开区间 J 使 supp ψ⊂J、\(\overline J\subset I\)，再取 χ∈Cc∞(I)，
χ>0 于 J、χ 在 J 外为零（端点平坦）；令 v1=r_h、v2=r_p，

\[
 G_{ij}=\int\chi v_i v_j,\quad b_i=\int\chi v_i r_0,
 \quad c=G^{-1}b,\quad
 \zeta=\chi\left(r_0-\sum_{i=1}^2c_iv_i\right).        \tag{9}
\]

Γ/Poisson Gaussian 求和给 v_i 实解析；二者不成比例，因为(2)的多项式因子非常数。
故 G 正定。若 r0 在 J 上等于二者的线性组合，其在 ψ 支撑之外的开区间为零，
解析延拓迫该组合全零，继而 r0=0，矛盾。因此

\[
 \ell_\zeta(r_h)=\ell_\zeta(r_p)=0,
 \qquad\ell_\zeta(r_0)
 =\int\chi\left|r_0-\sum c_iv_i\right|^2>0.            \tag{10}
\]

但(10)不等于消去全部 \(P_{an}\)。553 已付每个 \(\tau_a r_p\) 仍是 physical 主关系，
且其 Fourier 变换为非零整函数在竖线上的限制，非零 a.e.。
若(4)对所有这些平移为零，则相关的 Fourier 变换
\(\widehat\zeta\,\overline{\widehat r_p}\) 为零；Fourier 唯一性迫 ζ=0，违反(10)。
故存在实 a，使

\[
 \ell_\zeta(\tau_a r_p)\ne0,\qquad
 e^{a/2}\tau_a r_p=e^{u/2}(\tau_a p)\in e^{u/2}P_{an}. \tag{11}
\]

这给实际可判假的 cheap 反例。不是只说“某个关系也许失败”。
若把(5)仅作为 Picard 类，它又杀了包括 r0 在内的所有源；保 marked section 才出现(11)。
不能在前者利用“principal 已下降”，再在后者利用“r0 非零”，拼成一个不存在的 map。

### 2.3 全位与连续反测试

普适式(5)可先在 Z[t] 上写出；但给定一般 complex a(r) 的 actual 纤维是 C 基变换。
Spec C→Spec Z 不保留非零特征纤维；不能据普适族有 p-fibres，宣称实际 complex 源已有同源 p-adic 消失。
强令 a(r)∈Q 会改变全复源域；自然拓扑下连续非恒定 source→Q 读出也不存在。
允许更复杂的 adelic family、非线性或相对 base，并未被此反例排除。

这个图族、(6)–(8)完全不使用 g-integer 分布，因此 562/568 的连续正、负两段都有同一构造。
它们的完整 Weil Gram 符号相反，而图族的 dim V_n 和 fixed FS 度量均相同。
故这些已付前端不可能单独推出完整 Weil 号。该判断不将一般类 RH 强制成离散整数格。

## 3. 全关系相容的实际 relative section：成功，但归旧谱商

上面的失败不代表 family 逃逸全部失败。下面给一个确实消全部关系的解析族。
令

\[
 H(z)=(z^2-1/4)\Xi(z),\quad
 Z_H=(V(H),(\mathcal O_{\mathbf C}/H\mathcal O_{\mathbf C})|_{V(H)}),
 \qquad \pi:\mathbf P^1_{Z_H}\to Z_H.                   \tag{12}
\]

Z_H 是含完整重数的离散非约化解析空间，通常有无穷多个点；不是固定有限 projective arithmetic scheme。
可不枚举其点，直接以整个 H 的 cokernel sheaf 定义(12)。
以 [A_r] 为其 global section，定义

\[
 \sigma_r=-[A_r]Y\in\Gamma(\mathbf P^1_{Z_H},\mathcal O(1)),\quad
 s_r=X-[A_r]Y,\quad \Gamma_r=Z(s_r).                    \tag{13}
\]

全局源→σ 是复线性，Γ 是真正的源依赖 relative graph。
仿射图上 z−[A_r] 为 monic，即使 base 非约化也仍是非零因子。
故每个 Γ_r→Z_H 是同构，且 Γ_r 为 relative effective Cartier divisor。
有 \(\Gamma_r-\Gamma_0=\operatorname{div}(s_r/X)\)：相对 Picard 类仍恒定，marked section 才保存源。
既不声称任意 global section 都来自源，也不把整个 jet 乘积当成原 Fréchet 商。

### 3.1 405 与 537 的实际像

(2)给 \(A_{r_p}=H/2\)，所以

\[
 \sigma_{r_p}=0.                                      \tag{14}
\]

Ξ(±1/2)=ξ(0)=ξ(1)=1/2，故两个 degree 点与 Z_Ξ 不交；CRT 给底空间分解

\[
 Z_H=Z_\Xi\ \sqcup\ \{+1/2\}\ \sqcup\ \{-1/2\}.       \tag{15}
\]

h 的 spectral component 为零，degree 坐标均 1/4：

\[
 [A_{r_h}]\leftrightarrow(0,1/4,1/4).                  \tag{16}
\]

对 r0，两 degree 坐标为零；若 spectral component 也为零，则其全部 ξ-zero values 均为零，
完整显式公式给 Q_W(r0)=0，违反(3)。因此

\[
 [A_{r_0}]\leftrightarrow([A_{r_0}]_{\Xi},0,0),\quad
 [A_{r_0}]_{\Xi}\ne0.                                \tag{17}
\]

旧519的像识别精确给

\[
 \ker(r\mapsto[A_r]_{H})=e^{u/2}P_{an};\quad
 \ker(r\mapsto[A_r]_{\Xi})=e^{u/2}I.                  \tag{18}
\]

证明分两步，不能把整函数除法直接叫作 Schwartz membership：
首先，对**已给定 r∈S_exp**，除以 H 整当且仅当在全部非平凡零点保所需重数 jets，且 ±1/2 两值零。
其次，519 的(1)–(3)使用518两端 Mellin 除法/Möbius 重建与原 S_exp 全部带内快速衰减，
才将前者识别为实际像 E(S_even,0)=闭像 I；后者是双次数。
原函数域已经支付所需增长条件；这里不声称任意整函数商自动属于同一 Mellin 源空间，
也不新增不受控整函数为源。没有假设 RH 或简单性。
后一个去掉degree，保留承载完整Q的jet谱商；前一个另保405 B的degree双曲平面。
(18)不将完整 Q 的全部 radical 等同于 I；有重零点时 value radical 与 jet ideal 的差别仍保留。

具体地，若 ξ 在 ρ 的阶数为 m，则局部环为 C[ε]/(ε^m)，marked section 保留
\(A_r(\rho),A_r'(\rho),\ldots,A_r^{(m-1)}(\rho)/(m-1)!\) 全部 jets。
但 multiplication operator 的普通 trace 只有 \(mA_r(\rho)\)；nilpotent ideal (ε) 对 trace pairing
完全为零。因此“section 非零”不能一般推出“完整 Weil pairing 非零”；(17)是反向使用已付 Q(r0)>0，合法。
本构造不借 trace 抹去 Jordan 重数后再声称仍忠实，也不把分离 Fréchet jet 商与普通 trace 的半单商混为一谈。

这是一个实际、全关系相容、非 J_W 复合的 global-section map。
但其核与目标信息由旧519–520谱商直接给定，故精确归类为**旧谱商的相对几何实现**。
不能把“未显式枚举零点”误读为“没有以 completed divisor 为输入”，更不能把(12)称为独立算术平方。

### 3.2 原范数与局部消失：只有受控成功范围

对 fixed compact I=(-L,L)、每个 z=α+iγ 与 j≥0，(1)给原 du 的精确读出费

\[
 |\partial_z^j A_r(z)|^2
 \le\left(\int_{-L}^L u^{2j}e^{2\alpha u}du\right)\|r\|_2^2.
 \tag{19}
\]

该积分是 Cc∞(I) 上 L² 读出的 squared operator norm（以光滑逼近极向量取到上确界）；
Dlog 可由(6)得上界，不能把它叫 restricted Dlog 精确 Gram。
共中心 α=0 时是 \(2L^{2j+1}/(2j+1)\)，每 fixed α≠0 时成长是指数型。
553 已给相应 Dlog sharp 费用及合法 cofinal 范围，本稿不重计。

全线、全 S_exp 上没有一个 finite global du/Dlog bound 能同时保持全部关系非零读出：
553 cyclic density 阻止这种固定 Hausdorff norm 目标的降商 map。
(12)–(13)使用解析局部/Fréchet 拓扑与 fixed-window 费，不假称违背此结果。
原高度或 section metric 如要对所有源、窗、重数/高度有统一 joint 控制，仍必须另付。

还有一个必须避免的不同构造：\(A_r/H\)可作带规定极点的亚纯截面，但 affine 方程
\(H(z)w=A_r(z)\)不是(13)。在 H=0、A_r≠0 处其纤维为空；在两者均零处纤维为整条 A¹。
projective closure 仅把前一情形变成无穷远点，后一情形仍为整个 P¹，故不能据它取得 uniform flat jets。
本稿的相对图是已在 Z_H 上取系数的 monic \(X-[A_r]Y\)，不偷换成这个退化的亚纯图。

同一 relative P¹ 上的 jets 为 coefficient-ring 版本的(8)，核、乘法均成立。
源端的自然乘法仍是卷积：\(A_{r*s}=A_rA_s\)；不是源的 pointwise product。
σ_r 是 O(1) 截面，σ_rσ_s 是 O(2) 截面，而 σ_(r*s) 又在 O(1)，
两者不能不加分次/固定 Y 因子就宣称同一个映射。
可以明确放进 \(\bigoplus_n\mathcal O(n)\) 并加入形式次数来记录这个乘法，
但那是 graded coefficient-ring 包装，不产生实际算术对应的 degree/有效性。
但 base coefficients 本来就是旧谱 jets；局部化点长 m_ρ 是 completed divisor 的输入，
不是从有限素位 reduction 获得的 \(\log p\,p^{-k/2}\) 消失预算。
P¹ 的 module rank n+1 不给底空间总点长、原 norm 联合费用或平方 RR 容量；无穷底的普通总容量还会发散。

## 4. 完整 Γ、素数幂、极点与 Weil 责任

本稿始终保持旧实际 Q_W，不替换为(13)截面的正 FS 范数。
在物理源上它为

\[
\begin{aligned}
 Q_W(r)={}&2\Re(M_+(r)\overline{M_-(r)})+\Gamma_0\|r\|_2^2\\
 &+\tfrac12\int_0^\infty\frac{2e^{-v/2}}{1-e^{-2v}}
       \|\tau_vr-r\|_2^2dv
 -2\sum_{p,k\ge1}\frac{\log p}{p^{k/2}}
       \Re(r*r^*)(k\log p),\qquad
 \Gamma_0=\psi(1/4)-\log\pi.                           \tag{20}
\end{aligned}
\]

ξ 在(12)中的存在保留已校准完成化/重数信息，但不把(20)变成同一 section 的 arch height−finite divisibility。
特别：

* (15)两新增点是 degree 坐标，不是 ξ 的新零点；其配对须是405的双曲配对，不能给普通正点数 trace。
  完整 Q 只取 primitive ξ 部分并消全部 I；405 的 B 另保 degree 双曲项。
  特别 σ_h 的 degree 部分非零而 Q(r_h)=0，所以给全 H-base section 一个忠实正范数，
  再宣称它就是 Q，连在假定 RH 时也不成立；须作正确 degree quotient 或同源 signed cancellation。
* 任意正范数 \(\|[A_r]\|^2\)不自动等于 spectral partner \(1-\bar\rho\) 的 Weil 配对。
* 若要求所有(13)的 Gram 正且其 Gram 恰等于(20)，这仍是完整 Weil 正性的等价重写。
* 若另给不读 Q 符号的 same-object 非零评价 det、有限整除与原 arch 高度上界，再证明净差身份，才会增加独立输入。

连续正反段上同一 construction 可以以各自 completed entire F 代 ξ；全部 formal kernels/graphs 继续成立。
所以谱商本身不鉴别正负；需要独立极化/容量。
函数域真曲线有同样谱商包装，但其独立输入是实际曲线平方、局部有效对应与 RR/Hodge；
不能用此包装反向宣称已经从谱商恢复那些输入。

## 5. 可消费判断与下一条实际测试

本稿真正可消费的是两个明确构造/精确范围：

* bounded moving graph：cheap 原 norm + 同对象 kernel/线性容量，p/h/r0 有限测试可通过但全部主关系必失败；
* relative completed-divisor graph：全部主关系/非根与 degree 角色可正确通过，代价是旧谱商作为 base，
  没有独立的全位容量/预算号。

它们不是“所有 family 不可能”的边界，也不是 classic ζ 的独立新正性。
相对零点空间的 graph 仍是合法的原型/接口；原型本身不配再开未知容量合同。
下一次真正改变选择的输入应是：在不以 Ξ 商为唯一 coefficient base 的 adelic/relative 对象上，
给出实际 r→section（含原范数和全部关系），以及至少一条不按 Q 定义的本素消失/原高度估计，
再在**同一** det 上校验(20)的预算身份。
full all-complex/增长 coverage、mixed coupling 和整个 Goal 门仍未改；strong-old4/5预算不变。

来源阅读范围：本稿精读405 §§1–6、519 §§1–5、520 §§1–4、552 §§1–7、553 §§1–5、568 §§5–6；
537 非根正性作为已审基线消费，没有重算其巨大常数。外部仅上述两个 Stacks 条目，未续 paper 链。
