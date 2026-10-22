# 闭 HH₁ 角点电荷、全主关系与同一算术截面的准入检验

2026-10-22。独占分支；同 G20261014、0c4f 冻结基线。恢复 README/STATE、check/show、Goal、宏观前沿及 D20261022D；不改公共 STATE/cadence/Git。本稿消费 427/430/432 的实际算子、405/519 的关系、537 非根及 553 的原范数结论，未重证这些旧资产。结论限于下面写出的具体链、费用与测试，不排新的 filtered relative 比较。

## 1. 最小真正闭链已经存在，但不是自然 weighted 链的闭合证明

沿 430/432 的实际代数

\[
 A_{\rm src}=\operatorname{alg}(1,u,u^*,D_{\rm src}),\quad
 Q_{\rm src}=A_{\rm src}/\mathcal S_1,\quad
 A(h)=VU(h)V^*,\quad V^*V=M_m,
\]

其中 \(0\le m\le2\)、两端分别为 0 和 2，\(\|V\|^2=2\)。对 \(r,k\in C_c^\infty(\mathbb R)\)，置 \(h_r(s)=r(-s)\)。427 的实际迹类乘法缺陷说明

\[
 z_{r,k}=q(A(h_r))\otimes q(A(k))\in Z_1(Q_{\rm src}),
 \qquad
 \Omega(z_{r,k})=-4\int s h_r(s)k(-s)ds
              =4\int u r(u)k(u)du. \tag{1}
\]

这确实进入 432 的规范普通迹 regulator，不需把非闭链硬送入 \(\Omega\)。但它尚未将

\[
 c_r=q(u^*)\otimes q(uF_r),\quad F_r=A(h_r),\quad
 b_1c_r=q(F_r-uF_ru^*)\ne0 \tag{2}
\]

变成闭链。由 (1) 替换 (2)，须另证这种替换是所要求的 relative comparison，不能只因两者都含 \(F_r\) 就认同。

427/432 的实际闭链证明目前以 compact \(h,k\) 为原域。以下式 (1) 的标量泛函可直接延至全线 \(L^2\)，不等于已经证明 \(A(h)\) 在所有 \(S_{\exp}\) 输入仍有相同迹类链准入。若用 crop 进入实际 compact 域，要保留该区别。

## 2. 原 du/Dlog 费用：固定 probe 可全线支付，因而不能下降而非零

固定 \(k\in C_c^\infty\)，定义

\[
 \ell_k(r)=4\int u r(u)k(u)du.
\]

在全线原 du 上的精确 dual norm 是 \(4\|uk\|_2\)。对 supp \(r\subset[-L,L]\) 的原 du 源，其精确费用是

\[
 \|\ell_k\|_{(L^2[-L,L])^*}=4\|\mathbf1_{[-L,L]}uk\|_2. \tag{3}
\]

以 \(\widehat r(t)=\int r(u)e^{-itu}du\)、\(w(t)=\log(2+|t|)\) 固定原 \(D_{\log}\) 范数，则在全线的精确平方 dual norm 为

\[
 \|\ell_k\|_{D_{\log}^*}^2
   =\frac{16}{2\pi}\int\frac{|\widehat{uk}(t)|^2}{w(t)}dt
   \le\frac{16}{\log2}\|uk\|_2^2. \tag{4}
\]

若采用 553 的 \(1+w\) 等价图范数，式中仅以 \(1+w\) 换 \(w\)。固定窗口原域的 exact Dlog 费用不是简单把 (4) 截断；(4) 给合法上界，(3) 是该 du 原域的精确式。

实际 \(F_r\) 也有已知原窗费用

\[
 \|F_r\|\le2\|r\|_1\le2\sqrt{2L}\|r\|_{du}.
\]

对固定 \(k\)，若在代数商上暂取 operator quotient **半范数**、再取 projective 代表半范数，费用满足

\[
 \|q(F_r)\otimes q(A(k))\|_{\pi}
 \le4\sqrt{2L}\|k\|_1\|r\|_{du}. \tag{5}
\]

这里 \(\mathcal S_1\) 在整个 \(B(\mathcal H)\) 的 operator norm 下不闭；这本身不判定其在 \(A_{\rm src}\) 中的相对闭性，也不证明本商不分离。431已付 \(D_{\rm src}\cap\mathbb K=\mathcal S_1\)。式(5)仅给代表/链的候选有界费用，未宣称该完成下432的 \(\Omega\) 连续。因此 regulator 的实际费用应使用已计算的 (3)–(4)，不能从 (5) 自动推出。

这类固定 probe 的预算便宜，但 553 已决定其全关系命运：若 \(\ell_k\) 消去所有 physical \(P_{an}\)，则它在 du/Dlog 稠密子空间上零，由连续性必全零，故 \(uk=0\)。光滑 compact \(k\) 因而为零。任何非零固定 probe 都不可能同时满足全主关系及保非根。

## 3. 405 全平移上的实际失败与 537 非根的实际成功

令 \(P=Cp\ne0\) 为 405 实际主关系的物理中心化，\(p=(D^2+D)h=E\eta_0\)。全部 \(\tau_aP\) 仍是 physical 主关系，尺度因子 \(e^{a/2}\) 不影响零值测试。对任意非零固定 \(k\in C_c^\infty\)，实际见证族为

\[
 F_k(a)=\ell_k(\tau_aP)
      =4\int u k(u)P(u-a)du. \tag{6}
\]

这个连续函数不恒零。若恒零，其 Fourier 变换给
\(\widehat{uk}(t)\widehat P(-t)=0\)；405 的 Mellin 整函数不恒零，所以固定竖线上的 \(\widehat P\) 非零 a.e.，得到 \(uk=0\)，矛盾。因此**必有实际平移 \(a\)** 使全关系测试失败。这是全真实平移族上的证明，不是只调参数使 named \(p\) 通过，也不依赖 RH 或零点简单性。

该关系输入非 compact。若 \(\chi_R=1\) 于 supp \(k\)，则 \(\chi_R\tau_aP\) 是实际 compact 链允许的源，并且
\(\ell_k(\chi_R\tau_aP)=\ell_k(\tau_aP)\) 已精确相等。crop 不是主关系；这说明：任何保持 (1) 的原标量极限/延拓都不能消去真正 \(\tau_aP\)，而非声称 crop 已在主关系内。若新 relative edge 改变 regulator 的延拓，须支付新的 transgression，不能继续引用裸式 (1) 为答案。

反之，537 的 \(r_0=(D^2-1/4)\psi\ne0\)、\(\psi\in C_c^\infty((-17/16,17/16))\) 双极点矩为零且 \(Q_W(r_0)>0\)。取**固定于此见证**的

\[
 k_0(u)=u\overline{r_0(u)},\qquad
 \Omega(z_{r_0,k_0})=4\int u^2|r_0(u)|^2du>0. \tag{7}
\]

所有输入都在 432 compact 原域，非零性严格。与此同时，(6) 保证该 \(k_0\) 对某个真实 405 平移非零。故“能看见 r₀”已可实现，缺的不是这项单独可见性，而是与全 Pan 同时相容。

把第二因子改成源依赖 \(k_r=u\overline r\) 可给真 compact 闭循环，且

\[
 J(r)=\Omega(z_{r,k_r})=4\|ur\|_2^2
 \le4L^2\|r\|_{du}^2
 \le\frac{4L^2}{\log2}\|r\|_{Dlog}^2 \quad (\operatorname{supp}r\subset[-L,L]). \tag{8}
\]

它对非零 \(P\) 的标量延拓严格正，不能消关系。其全线费用需要 \(ur\) 的额外权，并非全球统一 du/Dlog bound。更一般的源依赖配对没有被一概排除：若最终 class map 对每个 Pan coset 不变且全线原范数连续，553 已证其常值；若只对 raw Pan 值零、只在 compact 域有费、采用 Fréchet 或变域，则该定理不适用，仍须分别测试 mixed/coset、尾费及真正关系延拓。

## 4. 新 relative 边的闭合自由度不能由“已闭”选定

假定已在一个明确的实际扩张链复形中给 \(e_r\)，满足 \(b e_r=-b c_r\)，并有可用的 regulator 延拓。另一修补 \(e'_r\) 与之相差真一循环：

\[
 e'_r-e_r\in Z_1,
 \qquad \Omega(c_r+e'_r)-\Omega(c_r+e_r)=\Omega(e'_r-e_r). \tag{9}
\]

旧角点已有非零 \(z_*\in Z_1\) 及 \(\Omega(z_*)\ne0\)；对任意源函数 \(\alpha(r)\)，\(e_r+\alpha(r)z_*\) 的边界相同，电荷却加 \(\alpha(r)\Omega(z_*)\)。当 \(\alpha\) 是固定 bounded probe，这种自由度本身也可以有有限原费。因此“原费可付＋链闭合”不足以选择算术读出，更不足以自动恢复完整 Weil 量。

这里没有否定 432 regulator 的规范性：**\(\Omega\) 对已定 HH₁ 类规范，未定的是从物理源选哪一个 HH₁ 类。** 几何/相对理想若独立限定允许的新边及 exact 等价，可消除部分自由；必须写出该限制和源 homotopy 的相容性。若只把 \(\alpha(r)\) 按期望 prime/Gamma/\(Q_W\) 选定，就仍是旧 probe/谱商包装。反之，一个实际 filtered chain map 即使底层必须经旧 H⁰ 商，也可能新增独立整性/容量；“经旧商”不是一般否决。

## 5. 真算术模型已存在；有限角点坐标仍未把同一源接进去

沿上轮真实正控制取

\[
 L_n=H^0(\mathbf P^1_{\mathbf Z},O(n))=\mathbf Z[X,Y]_n.
\]

同一个 \(L_n\) 有 \(p^k,z^m\) jets、实际满射评价、kernel 及乘法过滤；固定 toric metric/arch twist \(a>0\) 有

\[
 \log\#\{P\in L_n:\|P\|_{\sup}\le e^{an}\}
 =a n(n+1)+O_a(n\log n). \tag{10}
\]

系数 metric 的 determinant degree 也真为 \(a n(n+1)\)。这些是实际整数截面和二次容量，不应重新称不存在。

一种具体最廉价的 source bridge 是用有限闭角点 charge 作多项式系数：

\[
 s_{n,r}(z)=\sum_{j=0}^n\ell_{k_j}(r)z^j\in L_n\otimes\mathbf C. \tag{11}
\]

它在固定系数 metric 有直接 du bound，精确平方 operator fee 是 Gram 矩阵
\(16[\int u^2 k_i(u)\overline{k_j(u)}du]\) 的最大特征值（转置/共轭约定不影响特征值）。但只要 (11) 消去**全部** physical Pan，每个固定坐标即由 553 为零，故所有 \(k_j=0\)。让 n 增长、各层费用变大仍不绕过这个结论：每层若定义在全线且消全部关系，逐层已零。

非零式 (11) 可保 r₀，也给一个复杂截面；它没有真实整数系数，不能直接给原有限位消失阶/整除预算。把固定整数截面乘一个 charge 给的是复系数线，不会自动产生 rank n+1 的整数 section 库。换离散 orders、真 family/degeneracy、先整 cycles 后 complexification 都是合法方向，但须新增实际源/关系/整性资料，不从数值 charge 推出。

即使得局部 jets，也须先证明其 connecting obstruction 消失，才能给原 metric 的 global lift。真曲线精确序列
\(L(D)\to J_{D,E}\xrightarrow\delta H^1(O(D-E))\) 及 \(\mathbf P^1\) 的 \(O(-2)\to O(-1)\) 例已经表明非零 boundary 可以恰是无 lift 的障碍。当前没有从修补后的实际 HH₁ 类到这个整模型的 filtered map，因此没有同对象 local-order/lift/RR 预算可消费。坏 singular value 不得当 actual source 必要费用；真实源若已经给 lift，则直接 lift 费用优先。

## 6. 连续正反例、函数域与完整经典目标

连续控制 \(R_d=\mathbf C[z]/(z^2+d)\)、\(z^\dagger=-z\)、\(d=\pm1/16\) 都有有效 length-two boundary resolution。它们同时具有 local orders、张量/闭链设施，但 regular trace 型为

\[
 \operatorname{Tr}_{reg}(aa^\dagger)=2|A|^2+2d|B|^2,
 \quad a=A+Bz. \tag{12}
\]

闭角点设施也可与有限代数 \(R_d\) 张量，用 \(\operatorname{Tr}\otimes\operatorname{Tr}_{reg}\) 作相对迹；相同闭合计算的 charge 乘上 \(\operatorname{Tr}_{reg}(ab)\)。因此闭链/非零 regulator 本身不会排 d<0 的负 primitive 方向。换一个正 Hilbert trace 可使量正，却须另证它仍等于目标完整 Weil 型。

函数域成功所用的不只是一个 HH₁ 数：是真 \(C\times C\) 上的 signed 对应、全 Frobenius periods/转置/复合、effective 截面乘法与 RR/Hodge 的同对象容量，再扩全 complex Gram。\(H^0,H^2\) 的 pole 项须保留。原角点 charge 只由 \(m(-\infty)=0,m(+\infty)=2\) 决定，427 已明确不含所选纯周期权；不能由原 u/源准入本身推出算术周期。

经典目标仍严格保 568 的全源物理规范：

\[
\begin{aligned}
 Q_W(r)={}&2\Re(\mu_+(r)\overline{\mu_-(r)})
 +[\psi(1/4)-\log\pi]\|r\|_{du}^2\\
 &+\frac12\int_0^\infty\frac{2e^{-v/2}}{1-e^{-2v}}
            \|\tau_vr-r\|_{du}^2dv\\
 &-2\sum_{p,k\ge1}(\log p)p^{-k/2}
       \Re(r*r^*)(k\log p).
\end{aligned} \tag{13}
\]

完整 Γ/contact、全部 proper powers、双 pole/mixed 都未删。式 (1)/(8) 没有这些全部项，不把局部角点的正数解释成其容量。405 全关系恰要求 arch/finite/pole 的协同抵消；指定修补电荷等于 (13) 并要求正，只是 Weil 的等价/充分包，非独立输入。

## 7. 可消费结果与唯一缺口

已付的具体检验：真 compact 闭角点 source 可有原费且看见 r₀；任何固定非零角点 probe 必失败某个真实 405 平移；source-dependent 正角点亦不消关系；repair 的 HH₁-cycle 自由度与 regulator 规范性准确分开；同一 P¹_Z 的真实整数过滤/二次容量仍有效，有限 bounded probe 坐标不能完成 bridge。

上述均属旧 427/432/553 的直接使用及标准正反控制，没有新的 classic 独立容量/成长 whole 结论。最强旧 542+555→557 的 whole leading4/5 上预算、core/coupling/Ξ 均未变。

真正可改变选择的独立资料须同时给：实际扩张/理想中的新边而非任意加 cycle；全 Pan source homotopy 到 exact/principal 变换；537 与双 degree 的保留；原 du/Dlog 与 Fréchet/cofinal 费用；到**同一**整模型 local filters 的可解数据及 actual metric lift；最后同 square 的 primitive RR/full-Γpppole 身份。只给新的 closed charge、probe 或 HH₁ 标签，在此门停止。
