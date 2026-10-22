# 实际 adelic restriction 的相对链载体：源作用、主关系同伦和外平方的范围

2026-10-22。独占原稿；供 root 与 fresh 审查消费，未自行结算数学轮次、状态或 Git。
恢复：同 G20261014、冻结 0c4f；已读 README、STATE、check/show、Goal、C035、frontier、D20261022B、最新 family 报告以及 405/519/520/553。目标不改为构造任何表示；本门只检查一个不以完成零除子作 base 的实际相对链载体，是否另付平方容量。

## 1. 原件与范围

定点核读 [CCM2007 固定 v1 HTML](https://arxiv.org/html/math/0703392v1)，§4.2–4.5、§6.4、§7.1–7.2。所消费内容限定为：restriction 的 trace-class 矩阵模型、闭像 cyclic cokernel、缩放等变和卷积作用、源像作用消失、degree 调整。没有把其关于 RR 的类比升级为定理。未重新阅读其他来源。

实际 base 是群胚对

\[
 \mathbb Q^\times\ltimes\mathbb A_\mathbb Q^\times
 \longrightarrow\mathbb Q^\times\ltimes\mathbb A_\mathbb Q,
\]

而不是某个预给的零点 scheme。CCM Prop.4.5–4.8 的 restriction 在基本域上有矩阵
\(M_b(x,y)=\xi_{xy^{-1}}(xb)\)，次数零 trace 对径向源给 405 的
\(E\eta(t)=2\sum_{n\ge1}\eta(ne^t)\)。Def.4.10 的分离余核使用闭像，Lemma4.15/4.17 付卷积作用及像关系消失。本文下面只对这个**明确径向两项复形**做构造；不声称它等于所有 cyclic 次数的映射锥、Tor 或 completed tensor 的导出对象。

## 2. 正确中心化及保 degree 的实际两项复形

记 \(F=\mathcal S_{\exp,\mathbb C}\)，\(C f(u)=e^{u/2}f(u)\)，\(F_c=CF\)，\(S=\mathscr S_{e,0,\mathbb C}(\mathbb R)\)。\(F_c=F\) 作为函数集合，但物理 norm 和作用必须按 C 运输。设

\[
 E_c=CE:S\to F_c,\qquad
 \mu_+(r)=\int e^{u/2}r(u)du=d(C^{-1}r),\quad
 \mu_-(r)=\int e^{-u/2}r(u)du=c(C^{-1}r).
 \tag{1}
\]

这些目标 degree **不是**源准入的 \(\eta(0)=\int\eta=0\)。405 的 h 是最便宜反测：\(E\eta_h=h\) 而 \(c(h)=d(h)=1/4\)。若只取 \([S\xrightarrow{E_c}F_c]\)，h 及其两个 degree 都被杀掉。

一个保 degree 的实际修补是以下复形，次数为 \((-1,0)\)：

\[
 \mathcal C^\bullet=\left[
 S\xrightarrow{\partial}F_c\oplus\mathbb C_+\oplus\mathbb C_-
 \right],\qquad
 \partial\eta=(E_c\eta,-\mu_+(E_c\eta),-\mu_-(E_c\eta)).
 \tag{2}
\]

它只使用实际源、restriction 和两个绝对收敛矩。519(4) 给对应源积分，因此没有用 \(\Xi\) 回填差分或 base。实际 source-to-relative-class map 为

\[
 j(r)=[(r,0,0)]\in H^0(\mathcal C^\bullet).
 \tag{3}
\]

直接由 (2) 得

\[
 \ker j=C P_{\rm an},\qquad
 H^0(\mathcal C^\bullet)\simeq F_c/(CI)\oplus\mathbb C^2,
 \quad[(g,a,b)]\mapsto([g],a+\mu_+(g),b+\mu_-(g)).
 \tag{4}
\]

405/519 已付 E 的连续单射与像闭性；故 \(H^{-1}=0\)，(4) 是明确 Fréchet 分离商，非任意选截面。普通两项复形的同调又恰是旧源商加 degree；**独立算术定义成立，并不等于获得独立容量**。它不同于以前的 V(H) base 定义，但取同调后不是新的谱约束。也未将 (3) 称为某个 algebraic line bundle 的 regular global section。

类型必须保留：(2) 是下面 \(F_c\)-卷积作用下的 module complex，未自动成为 differential graded algebra。B 上若裸用逐分量乘法，\(\partial S\) 一般不是其 ideal，不能将该乘法下降。405 的两 degree 源基使 j 满射，因而可以从旧 \(F_c/(CP_{\rm an})\) 运输卷积代数到 \(H^0\)；那是旧商的乘法，并不证明 (2) 自身已有结构层或 divisor 的乘法。

## 3. 实际源上的卷积 chain map、复合与 null-homotopy

对物理源 r 定义

\[
 (U_r\eta)(x)=\int_{\mathbb R}e^{-t/2}r(t)\eta(e^{-t}x)dt,
\]
\[
 T_r^{-1}=U_r,\qquad
 T_r^0(g,a,b)=(r*g,\mu_+(r)a,\mu_-(r)b).
 \tag{5}
\]

405/519 的实际 dilation lift 给 \(E_c U_r\eta=r*E_c\eta\)。矩是卷积字符，所以 \(\partial T_r^{-1}=T_r^0\partial\)。此外

\[
 U_rU_s=U_{r*s},\qquad T_rT_s=T_{r*s}.
 \tag{6}
\]

这些是有原源 lift 的实际复合；(5) 中的 \(e^{-t/2}\) 不能删掉。未 centered 的 f 与物理 r 用同一个裸 dilation 核会错移两个 degree 权。

405 的实际 p 是 \(p=E\eta_0=(D^2+D)h\)，\(\eta_0(x)=(4z^4-28z^3+41z^2-9z)e^{-z}\)，\(z=\pi x^2\)。设 \(r_p=Cp\)。给出一个可直接检查的 chain-homotopy：

\[
 K_p^0(g,a,b)=U_g\eta_0\in S,\qquad K_p^{-1}=0.
 \tag{7}
\]

因为 \(\mu_\pm(r_p)=0\)，

\[
 \partial K_p^0(g,a,b)=(r_p*g,0,0)=T_{r_p}^0(g,a,b).
\]

另一方面 \(E_cK_p^0\partial\eta=r_p*E_c\eta=E_cU_{r_p}\eta\)，E 单射给 \(K_p^0\partial\eta=U_{r_p}\eta\)。所以

\[
 \boxed{\ T_{r_p}=\partial K_p+K_p\partial.\ }
 \tag{8}
\]

所有实际 \(r_q=CE\eta_q\) 且 \(\mu_\pm(r_q)=0\) 同理；闭像 519 让此处覆盖整个 \(CP_{\rm an}\)，不止单个 p。链同伦所需的是实际源 \(\eta_q\)，不是在任意整函数环中把 A/H 形式相除。

对 h 不能照抄 (8)：\(T_{r_h}\) 在两个 degree summand 上各为 1/4，不能 null-homotopic。事实上 \(j(r_h)=[(0,1/4,1/4)]\)。这正是避免把全 I 误称405 principal 的检查。最小 Weil Q 根又与 405 B 根不同：完整 Q 在 h 上为零，所以以后不能要求 j 上的忠实正 norm 等于 Q。

### 3.1 显式 DGA 修补：可以补完，不能误作平方容量

root 提出以下具体乘法；本稿逐项核查后成立。保留§2对**裸逐分量乘法**的失败判断，但这不排除用 degree cocycle 修补。在 \(B=F_c\oplus\mathbb C^2\) 上定义

\[
 \begin{aligned}
 (g,a,b)\star(h,c,d)=\big(&g*h,\;
 ac+a\mu_+(h)+c\mu_+(g),\\
 &bd+b\mu_-(h)+d\mu_-(g)\big).
 \end{aligned}
 \tag{8a}
\]

令 \(\Phi(g,a,b)=(g,a+\mu_+(g),b+\mu_-(g))\)。因为 \(\mu_\pm(g*h)=\mu_\pm(g)\mu_\pm(h)\)，直接展开即得 \(\Phi\) 为 (8a) 到 \(F_c\times\mathbb C^2\) 逐分量代数的拓扑代数同构。\(\Phi(\partial\eta)=(E_c\eta,0,0)\)，所以 \(\partial S\) 现在确为 ideal。

h 给出具体相消检查：裸逐分量乘法下 \((0,1,0)\partial\eta_h=(0,-1/4,0)\) 不在像中，因为 E_c 单射；改用 (8a) 后同一乘积变零。这个修复没有删除 degree，而是用正确 cocycle 协同运输它。

将 B 对次数 −1 的 S 的作用定义为 \((g,a,b)\eta=U_g\eta\)，并令 \(S^{-1}\cdot S^{-1}=0\)。则 (2)、(8a) 成为交换的非正次数 DGA。完整核查如下：

1. 结合律与次数零交换性由 \(\Phi\) 给出；module 结合律由 \(U_gU_h=U_{g*h}\) 给出。
2. 混合次数的 Leibniz 为 \(\partial(U_g\eta)=(g,a,b)\star\partial\eta\)，两端 degree 分量同为 \(-\mu_\pm(g)\mu_\pm(E_c\eta)\)；(8a) 中的 a、b 额外项恰好相消。
3. 两个次数 −1 元素的 Leibniz 要求 \(U_{E_c\eta_1}\eta_2=U_{E_c\eta_2}\eta_1\)。对 E_c 作用后两边同为 \((E_c\eta_1)*(E_c\eta_2)\)，由 E_c 单射即得；这正是 Peiffer 恒等式。
4. 原 Fréchet 拓扑下，B 乘法由卷积／连续矩联合连续，B×S 的作用由 (9) 的带权 L1 界联合连续。没有另取一个能免费支付原 du/Dlog 的 completion。

该 DGA **非 unital**：F_c 内没有卷积恒等元。\((0,1,0)\)、\((0,0,1)\) 是 degree 局部幂等且杀 S，但不能成为整个 DGA 的 unit。若需 unit，须另行 unitization 并跟踪其附加常数；这里未将分布 \(\delta_0\) 冒充原 F_c 中的函数。

\(j_0:r\mapsto(r,0,0)\in B\) 现在为真正代数 map，其左乘在 B 上恰为 (5) 的 \(T_r^0\)，在 S 上恰为 \(U_r\)。因此链上乘法、作用与 principal 同伦可同时兼容，不必因未写乘法而停在 module complex。E_c 单射及闭像说明 canonical DGA projection

\[
 \mathcal C^\bullet\longrightarrow H^0(\mathcal C^\bullet)
 \simeq F_c/(CP_{\rm an})
 \tag{8b}
\]

为 quasi-isomorphism：次数 −1 同调零；次数零识别由 j 与405两 degree 源基给出。这个 algebraic／Fréchet 意义的 quasi-isomorphism 未声称是原 L2/Dlog 正 Hilbert 的等距实现，也未声称等于全 cyclic complex。

故 (8a) 是可明确补完的一项代数设施，不能把“非自动 DGA”误写成“无法构造 DGA”。与此同时，它由原矩及旧实际 restriction 完全给出，且 quasi-isomorphic 的仍是旧405源商；没有新增结构 sheaf、Cartier 有效性、极化、算术平方的 RR Euler-characteristic 或独立容量。

## 4. 537 非根与原 du/Dlog 费用

取537的 \(r_0=(D^2-1/4)\psi\)，\(0\ne\psi\in C_c^\infty((-17/16,17/16))\)。分部积分给 \(\mu_\pm(r_0)=0\)。若 \(j(r_0)=0\)，则由 (4) 得 \(r_0\in CP_{\rm an}\subset CI\)，405 的完整显式公式给 \(Q_W(r_0)=0\)，违反537 \(Q_W(r_0)>0\)。因此 (3) 保非根。这里用旧固定窗全源结论作见证，不预设零点位置，也不把主关系商的存在当正性。

还可以核实际对应作用本身不把该见证杀掉。若 \(T_{r_0}\) 在 \(H^0\) 上全零，则对所有 g 有 \(j(r_0*g)=T_{r_0}j(g)=0\)。取归一化紧支 smooth approximate identity \(g_\epsilon\)，有 \(r_0*g_\epsilon\to r_0\) 于原指数 Fréchet 拓扑；\(CP_{\rm an}\) 闭，遂得 \(r_0\in CP_{\rm an}\)，矛盾。故 \(T_{r_0}\) 的同调作用非零，特别不是 null-homotopic。这里用了真实 approximate identity，没有给无单位卷积代数凭空添一个 F 内的恒等元。

原源作用有以下逐项付费。对 \(q_{a,b}(\eta)=\sup_x|x^a\eta^{(b)}(x)|\)，\(a,b\ge0\) 整数，

\[
 q_{a,b}(U_r\eta)\le q_{a,b}(\eta)
       \int|r(t)|e^{(a-b-1/2)t}dt.
 \tag{9}
\]

这同时保证源仍为 Schwartz、原点零值／零积分，以及 (5)–(8) 的换序。全部 r 在 F_c 上有有限带权 L1 费用；不是一个全线原 L2 bound。若 \(\operatorname{supp}r\subset[-L,L]\)，令 \(\kappa=a-b-1/2\ne0\)，则

\[
 q_{a,b}(U_r\eta)\le q_{a,b}(\eta)
 \left(\frac{\sinh(2\kappa L)}{\kappa}\right)^{1/2}\|r\|_{du}.
 \tag{10}
\]

目标卷积在原 L2 及 zero-extension Dlog 上的乘子费皆 \(\le\|r\|_1\le\sqrt{2L}\|r\|_{du}\)；两个 degree 的 dual norm 则皆为 \(\sqrt{2\sinh L}\)。用 \(\|r\|_{Dlog}^2=(2\pi)^{-1}\int\log(2+|t|)|\widehat r(t)|^2dt\) 时，(10) 也可除以 \(\sqrt{\log2}\) 改写为 Dlog 上界。不能把这些 fixed-window 费用合称全域 uniform quotient 费用，也不能把上界当必要增长下界。

553 的强旧反测仍适用：全部物理 \(r_p\) 的平移在全线 L2/Dlog 稠密。因此把 (3) 再送入任何 Hausdorff positive completion，若要求精确消全部关系且全线原 norm 连续，就只能给零类。保留 Fréchet、固定窗／变域或付 cofinal 范数是合法逃逸；(9) 正保存这份费用，并未免费绕过553。

## 5. 外平方确实存在，却不产生 RR 二次容量

至少在代数 tensor 范畴，\(\mathcal C\otimes_\mathbb C\mathcal C\) 是明确三项复形：

\[
 S\otimes S\longrightarrow
 (S\otimes B)\oplus(B\otimes S)\longrightarrow B\otimes B,
 \quad B=F_c\oplus\mathbb C^2,
 \tag{11}
\]

差分按 Koszul 符号；\(T_r\otimes T_s\) 是实际 chain map。\(T_{r_p}\otimes T_s\) 的同伦由 \(K_p\otimes T_s\) 给出。此处没有自动声称 completed projective tensor 精确、cyclic Eilenberg–Zilber 或同一 sheaf square 的 Künneth；这些比较须另给拓扑及范畴证明。

即使付了 tensor 精确性，代数 Künneth 仅给 \(H^0\simeq H^0(\mathcal C)\otimes H^0(\mathcal C)\)。有限截断维数 m 的平方变 m²，**不是** \(h^0(nD)\) 随 n 的 RR 二次主项，更不是具有符号的 \(D^2/2\)。它没有定义可复合的有效 Cartier 对应、principal rational functions、局部消失过滤及同一有界 global section 空间。

最便宜的可判反测：设 A=diag(1,-1)，则

\[
 \operatorname{Tr}(A\otimes A)=\operatorname{Tr}(A)^2=0,
 \qquad\operatorname{Tr}(A\circ A)=2.
 \tag{12}
\]

所以 external tensor trace 与 Weil 所需 composition trace 不是一个预算。把 \(T_rT_{r^*}\) 的 Hilbert 原 L2 正性用作修复也无免费收益：其 ordinary convolution trace 通常无限；若改到分离余核，原 norm 下降遭553；若做有限部分／相对 trace，正性必须重新证明，不能继承被减去两个无穷量之前的 positivity。

在实际 adelic restriction 的输入中，Schwartz 值和 trace-class 矩阵为 complex-valued；restriction 本身没有给评价 minor 的整性格或 p-adic 消失阶。一般复源不必本身是整数 divisor——函数域也先有统一几何再复线性扩张——但必须先独立构造那个统一几何／filtered global module。此处不能把每个 complex coefficient 事后宣称有一份算术 valuation。

## 6. 完整经典项、验证要求与净结论

405 完整显式公式已付 Γ finite-part/contact、全部 prime powers、两 pole/degree 的相同正规化；(1)–(8) 不删任何项。这里只是把旧 primitive trace 和两 degree 账本安置在实际 relative complex 中。没有证明 Γ 是同一 square 的 arch 容量，没有证明 prime powers 是其评价 minor 整除阶，也没有证明 poles 是其 RR Euler-characteristic 缺陷。

函数域的 adelic restriction/相对复形同样存在；已知正性另用 C×C 的真正 divisor／principal／有效性及平方 RR/Hodge，不能由 (11) 替代。连续正反模型中，可在同一有限代数 \(\mathbb C[z]/(z^2+d)\) 上保全部乘法、composition、tensor 和非退化评价，而 \(z^\dagger=-z\) 的 regular trace 为 \(2|A|^2+2d|B|^2\)，d 正负给相反号。这个旧568/上一轮反测说明：链层复合及局部评价本身不决定极化。

本稿实际付出：**不以 Ξ 零除子为 base 的 source-defined relative 两项链载体及显式非 unital DGA 修补；正确物理权；保两 degree 的修补；全部405解析 principal 的实际源同伦；537非根及原 fixed-window 费用；外平方与 composition 的明确区别。** 这是405/519/553的直接、可核查链层实现，不是新的独立 RR 容量或经典正性。

最小未付箭头仍为：由这份相对链数据得到同一算术 square 上的可限制／可复合 global sections 和消失过滤，独立给 \(n^2 D^2/2\) 的有符号容量项与所有误差，再把同一预算逐项识别为完整 Weil 型。仅规定该项等于 Q 且容量非负，会重新陈述 Weil 正性。没有这份新输入时，应在本源门停止，不继续提高 tensor 次数、加标签或重命名 ordinary cokernel。
