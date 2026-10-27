# 原全z framed holonomy：定义域、范数、两端与gauge闭合

2026-10-28；unit_height独占前件稿。恢复STATE／D20261028M、同G20261027、前沿、[唯一准入](../independent-source-discovery/next-original-framed-holonomy-admission.md)和[低阶意见](../independent-source-discovery/original-holonomy-next-input-opinion.md)，check/show通过。本文只闭原族定义及误差／frames，不重证V₁／V₂或续高阶，不调B／A₀，不web／PDF／下载，不改STATE／cadence／合同／Git或其他稿。原cadence3／历史49／cycle16保持，数学净果及计轮由root统一消费。

## 1. 冻结对象与真实控制量

原physical源为 \(r(u)=e^{u/2}f(u)\)，取复空间

\[
 S_{\exp}=\{r\in C^\infty(\mathbb R;\mathbb C):
 p_{N,k}(r)=\sup_u e^{N|u|}|r^{(k)}(u)|<\infty,\ \forall N,k\in\mathbb N\}.
\]

固定 \(A_0=\mathrm{diag}(1/4,-1/4)\)，及一次先固定的tracefree Hermitian

\[
 B=\begin{pmatrix}a&c\\\bar c&-a\end{pmatrix},\quad a\in\mathbb R,\qquad
 C_B(u)=e^{-uA_0}Be^{uA_0}
 =\begin{pmatrix}a&ce^{-u/2}\\\bar ce^{u/2}&-a\end{pmatrix}.
\]

所有矩阵范数取标准Euclidean operator norm。对原意见的控制量

\[
 w_B(u)=|a|+|c|e^{|u|/2},\quad
 s=s_B(r)=\int_{\mathbb R}|r(u)|w_B(u)\,du,
\]

有 \(\|C_B(u)\|\le w_B(u)\)，故 \(a_B(r)=\int|r|\|C_B\|\le s<\infty\)。这是三角不等式得到的充分真实范数控制，不称最优常数。

定义 \(M_{r,z}(u)=zr(u)C_B(u)\)。其trace为零，且全线L¹；r／z为complex时它不必skew-Hermitian，不能据B的Hermitian条件称运输为unitary或正配对。

原族保持

\[
 Y(u,z)=I+z\int_{-\infty}^u r(v)C_B(v)Y(v,z)\,dv,\qquad
 \mathcal H_B(r)(z)=Y(+\infty,z). \tag{1}
\]

若写回背景坐标 \(F(u,z)=e^{uA_0}Y(u,z)\)，准确方程为
\(F'=(A_0+zr(u)B)F\)。z是整个coupling参数，不省成另一个源或固定z读出。

## 2. Volterra存在、唯一及整个z族

令 \(K(u)=r(u)C_B(u)\)，定义

\[
 V_n(u)=
 \int_{u>t_1>\cdots>t_n}
 K(t_1)\cdots K(t_n)\,dt_1\cdots dt_n,\quad V_0=I.
\]

积分绝对收敛。写
\(s_-(u)=\int_{-\infty}^u|r|w_B\)、\(s_+(u)=s-s_-(u)\)，有

\[
 \|V_n(u)\|\le \frac{s_-(u)^n}{n!}\le\frac{s^n}{n!}. \tag{2}
\]

理由是矩阵乘积范数被标量乘积支配，标量对称积分在有序simplex上占 \(1/n!\)。因此

\[
 Y(u,z)=\sum_{n\ge0}z^nV_n(u)
\]

对所有u和任意 \(|z|\le R<\infty\) 一致绝对收敛，\(\|Y(u,z)\|\le e^{Rs_-(u)}\)。由绝对Fubini代回(1)；原K连续，故Y对u为C¹并满足原ODE。对z局部一致收敛给entire矩阵函数。任意固定 \(R>0\) 还可逐项得
\(\sup_{u,|z|\le R}\|\partial_zY(u,z)\|\le se^{Rs}\)；这里不计算新的高阶有序系数。

若Z是另一个locally absolutely continuous解且 \(Z(u,z)\to I\) 于负端，对每个固定z及有限u，从有限左端v应用Gronwall得

\[
 \|Z(u,z)-Y(u,z)\|
 \le e^{|z|\int_v^u|r|w_B}\|Z(v,z)-Y(v,z)\|.
\]

令 \(v\to-\infty\) 即零。因此该负端归一解唯一；无需额外假设全局L²或unitarity。此证明也覆盖按有限左端初值I取极限的定义。

## 3. 两端、SL₂与截断误差

由(2)直接有

\[
 \sup_{|z|\le R}\|Y(u,z)-I\|
 \le e^{Rs_-(u)}-1\longrightarrow0\quad(u\to-\infty). \tag{3}
\]

全线有序积分 \(V_n=V_n(+\infty)\) 满足相同阶乘界，故

\[
 \mathcal H_B(r)(z)=I+\sum_{n\ge1}z^nV_n
 \in\mathcal O(\mathbb C,M_2(\mathbb C)).
\]

由积分方程及 \(\|Y\|\le e^{Rs}\)，

\[
 \sup_{|z|\le R}\|\mathcal H_B(r)(z)-Y(u,z)\|
 \le R e^{Rs}s_+(u)\longrightarrow0\quad(u\to+\infty). \tag{4}
\]

所以两端极限均在每个z-disk上局部一致，非仅逐个z存在。

对有限初值区间的基本解，trace \(M_{r,z}=0\) 给det恒1；向负无穷的上述局部一致极限保持det。因此对全部u、z，

\[
 \det Y(u,z)=\det\mathcal H_B(r)(z)=1,\qquad
 \mathcal H_B(r)\in\mathcal O(\mathbb C,SL_2(\mathbb C)).
\]

有限基本解的逆满足反向方程及相同Gronwall范数界；取极限给

\[
 \|Y(u,z)^{-1}\|\le e^{|z|s_-(u)},\qquad
 \|\mathcal H_B(r)(z)^{\pm1}\|\le e^{|z|s}. \tag{5}
\]

逆的两端极限亦局部一致，因矩阵取逆在此由adjugate和det1给出。右端归一的同一ODE基本矩阵可记 \(Y_+(u,z)=Y(u,z)\mathcal H_B(r)(z)^{-1}\)；其正端为I、负端为 \(\mathcal H_B(r)^{-1}\)。这只是同一运输的另一端基，不把它当允许自由更换的两端frames。

令 \(\Phi(T,-T;z)\) 是原系数在有限区间、左初值I的基本解，\(\delta_T=\int_{|u|>T}|r|w_B\)。有序积分中至少一变量在区间外的部分给

\[
 \sup_{|z|\le R}\|\mathcal H_B(r)(z)-\Phi(T,-T;z)\|
 \le e^{Rs}-e^{R(s-\delta_T)}
 \le R e^{Rs}\delta_T. \tag{6}
\]

故不存在条件积分或双端取极限顺序的歧义；同样适用于不对称左右端截断，以两端积分尾之和替代δ_T。这是全source积分的误差核算，不把裁掉Pan尾后的源当成关系测试。

## 4. 强源、fixed窗du与zero-extension Dlog费用

对任一 \(N>1/2\)，用原 \(p_{N,0}\) 可付

\[
 s_B(r)\le
 2\left(\frac{|a|}{N}+\frac{|c|}{N-1/2}\right)p_{N,0}(r), \tag{7}
\]
\[
 \delta_T\le2p_{N,0}(r)
 \left(\frac{|a|e^{-NT}}N+
       \frac{|c|e^{-(N-1/2)T}}{N-1/2}\right),\quad T\ge0. \tag{8}
\]

S_exp的整数N可取任意N≥1。故(1)是原强源上的连续定义，全部极限／误差有明确强半范数费用，而非只有形式存在。

另先fixed \(\operatorname{supp}r\subset[-L,L]\)、\(L>0\)，原意见的充分常数为

\[
 K_{B,L}=\sqrt{2L}(|a|+|c|e^{L/2}),\qquad
 s_B(r)\le K_{B,L}\|r\|_{du}.
\]

采用原全线zero extension及 \(\widehat r(t)=\int r(u)e^{-itu}du\)，

\[
 \|r\|_{D\log}^2=\frac1{2\pi}\int
 \log(2+|t|)|\widehat r(t)|^2dt
 \ge\log2\,\|r\|_{du}^2,
\]

故 \(s_B(r)\le K_{B,L}(\log2)^{-1/2}\|r\|_{D\log}\)。代入(2)–(6)即得同一fixed窗的全z-disk误差；没有换范数或额外2π。

原族还满足实际连续性误差：对两个同域源r、q，Duhamel和有限／无限端基本解界给

\[
 \sup_{|z|\le R}\|\mathcal H_B(r)(z)-\mathcal H_B(q)(z)\|
 \le R e^{R(s_B(r)+s_B(q))}s_B(r-q). \tag{9}
\]

其积分式保原乘法顺序：
\(z\int\Phi_r(+\infty,u)(r-q)(u)C_B(u)\Phi_q(u,-\infty)\,du\)。
于是强 \(p_{N,0}\) bounded集合或同fixed窗du bounded集合上得到局部Lipschitz上界。全线weighted L¹与globaldu／Dlog不能混同；这里没有声称整个非线性全z族有globaldu统一有界费用，亦不由一个充分upper反向证明任何必要lower。

## 5. z-disk尾如何消费已有非zero系数

对任意积分截断阶m，纯定义层尾界为

\[
 \sup_{|z|\le R}\left\|
 \mathcal H_B(r)(z)-\sum_{j=0}^{m}z^jV_j\right\|
 \le e^{Rs}\frac{(Rs)^{m+1}}{(m+1)!}. \tag{10}
\]

这不是新计算高阶系数。仅就已有意见拟消费的 \(m=1\) 或2：若前面系数零、\(\kappa=\|V_m\|>0\)，则s>0，取

\[
 0<\rho\le\min\left\{1,\frac{\kappa(m+1)!}{2e^s s^{m+1}}\right\}.
\]

对全部 \(0<|z|\le\rho\)，(10)以R=|z|给

\[
 \|\mathcal H_B(r)(z)-I\|
 \ge |z|^m\kappa-
       e^{|z|s}\frac{(|z|s)^{m+1}}{(m+1)!}
 \ge\tfrac12\kappa|z|^m>0. \tag{11}
\]

因此一份经独立核准的非zero一／二阶系数确实排除整个z族恒I；不可能由未算的全尾对所有z抵消。ρ依实际源／B／系数，未给ε、平移或成长上的uniform半径，也不宣称每个远处非零z都非I。本文不认证低阶意见中的系数值／号或其strongest-old分类。

## 6. 允许gauge与原坐标的必要限定

冻结的frames是在interaction坐标 \(Y=e^{-uA_0}F\) 中。精确允许的framed gauge是：局部绝对连续可逆矩阵 \(h(u,z)\in SL_2(\mathbb C)\)，在该坐标满足

\[
 h(u,z)\longrightarrow I\quad(u\to-\infty,+\infty).
 \tag{12}
\]

对整个解析族，可取h在z上entire、(12)在每个disk局部一致；这保证同一全z frames。若继续将gauge后的连接放在全线L¹系数类别内，还须其变换系数在该类；例如局部一致L¹的h′是充分条件。这一导数域责任与端frame条件分开，不把仅有端极限当成所有导数可积。

采用左作用 \(\widetilde Y=hY\)，变换系数为

\[
 \widetilde M=h'h^{-1}+hMh^{-1}.
\]

由(12)，\(\widetilde Y(-\infty)=I\)、\(\widetilde Y(+\infty)=\mathcal H_B(r)\)；故允许gauge逐z保整个H族。一般端值为h_±时，则变成 \(h_+\mathcal H_B(r)h_-^{-1}\)。不得自由丢掉这一左右端信息。特别，形式选h=Y⁻¹虽然可消ODE系数，其正端通常为H⁻¹，非允许的双端I gauge。

**背景坐标的g→I不等于(12)。** 若背景F变为gF，interaction gauge是

\[
 h=e^{-uA_0}g e^{uA_0}
 =\begin{pmatrix}
 g_{11}&e^{-u/2}g_{12}\\e^{u/2}g_{21}&g_{22}
 \end{pmatrix}. \tag{13}
\]

所以确切加权条件是diag趋1，且两个off-diagonal在(13)的加权后分别趋0；非酉背景在正端放大21项，在负端放大12项。

一个只检端frame、与source无关的反控制：取光滑χ在u≤0恒0、u≥1恒1，置

\[
 g(u)=I+\chi(u)e^{-u/2}E_{21}\in SL_2(\mathbb C).
\]

背景两端均有g→I，但 \(h(u)=I+\chi(u)E_{21}\) 的右端为I+E₂₁，改变运输为 \((I+E_{21})H\)。这没有改A₀／B／r，而是证明两个gauge条件不同；不能用background-only条件消掉已算系数，再声称保留原frames。

**消费限定／可能补正：** 原gate已用interaction Volterra与双端frames定义H，本文按这个对象把“gauge两端I”精确读为(12)。若此前措辞实际想允许所有仅在背景坐标趋I的g，则那是另一等价关系，原H未必为其不变量；必须由root明示纠正／重新闭合frame语义后，才可消费非identity作为framed反测。本文不静默将两类gauge互换，也不改变physical源或端frames来修复候选。

## 7. 原Pan域与本支消费边界

405及其既有physical字典给 \(H=e^{u/2}h\in S_{\exp}\)，故
\(p=(D^2-\tfrac14)H\) 及每个固定 \(\varepsilon p_b\)（ε complex、\(p_b=\tau_bp\)）均在本原域。导数、乘固定指数与固定平移保持S_exp；例如
\(p_{N,0}(\varepsilon\tau_bp)\le|\varepsilon|e^{N|b|}p_{N,0}(p)\)。
因此(1)–(11)对真实noncompact Pan及其全部固定倍数／平移适用，不用crop代替。这里仅核域，不重证Pan来源、矩或V₁／V₂。

root可消费的本支完整前件是：原强源全尾／fixed窗du-Dlog费用；全z解析唯一运输、两端局部一致极限和SL₂；明确的范数／截断／Taylor误差；以及interaction双端I的framed gauge不变性。全部z是候选数据，不将一个矩阵元素、det或有限probe当整个source carrier。

这仍只是实际矩阵连接／相对运输对象，不自动获得Pic、HH、算术primitive、整线丛、section乘法或mixedRR。完整Γ／contact、properpowers、双pole及经典whole/core责任未由此付款。低阶Pan是否构成strongest-old直接结论或新的strict反测、实际轮数与合同结算，均留root和其他独占分支对齐后决定。
