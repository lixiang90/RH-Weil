# 507. 有限真源域的规范周期相位与仍然存在的共轭通量

2026-10-11。接续[历史复盘](../goals/reviews/2026-10-11-weil-f1-retrospective.md)选择的相位合同。
这是历史复盘后第一轮 Weil／F₁ 研究，与508合计一次研究迭代；总节奏计数由1推进到2。

本轮完成固定素数对 \(p=2,q=5\) 的小分母付款，并从434完整矩阵计算得到430整个**有限源域**的相位读出。
得到的是两个体积系数、零均值周期相位和常数，具有实际表示无关性、线性及伴随相容性。
它没有成为循环迹：新的加权共轭公式及一个零单位输入的有限词反例仍给非零源通量。
原437的线性有限部反例保留；范数完成、辅助分割独立下降、实位、闭链、正性及RR没有由本轮实现。

## 1. 固定实际对象与独立小分母输入

保留[430](430-f1-source-stable-periodic-smoothing-algebra.md)的原 Hilbert 空间、原酉源 \(u\)、采样 \(V\)、平方分割 \(c,d\) 及
[434](434-f1-haar-physical-cutoff-on-the-source-domain.md)的原双物理投影 \(P_{K_p,K_q}\)。置

\[
 L=\log2,\quad M=\log5,\quad f=cd,\qquad
 F_{r,s}(B)=u^rVBV^*u^{-s},
\]
\[
 D_{\rm src}=\operatorname{span}_{\rm finite}
 \{F_{r,s}(B):r,s\in\mathbb Z,\ B\in G_M\}+\mathcal S_1.
 \tag{1}
\]

\(G_M\) 是原来光滑、联合 \(M\)-周期、有限传播的实际核类。430已证明(1)是星代数、\(u,u^*\) 为双侧乘子。
有限原源词在此域中，但不将它等同于最小源理想的全部范数完成。

本轮消费独立的已证超越数论定理。[Bugeaud–Mignotte–Siksek原刊](https://annals.math.princeton.edu/wp-content/uploads/annals-v163-n3-p05.pdf)
§9.1、Theorem9.4，pp.988–989，给实代数数乘积减1的明确下界，文中由Matveev2000 Cor.2.3推出。
固定高度 \(h(2)=L,h(5)=M\)、数域 \(\mathbb Q\)、两个整数系数，令

\[
 \kappa=1.4\,30^5\,2^{9/2}LM\approx858754405.997,
 \qquad c_*={4e^{-\kappa}\over M\sqrt5}>0.
\]

对 \(n\ge2\)，取 \(m\) 为 \(nL/M\) 最近整数；有 \(1\le m\le n\)、
\(\xi=nL-mM\ne0\)、\(|\xi|\le M/2\)。定理先给

\[
 |2^n5^{-m}-1|>e^{-\kappa}n^{-\kappa}.
\]

这里的对象是乘积减1，尚不是加法对数。再用
\(|e^\xi-1|\le\sqrt5|\xi|\) 及 \(\sin(\pi t)\ge2t\)（\(0\le t\le1/2\)）才得到

\[
 z_n=e^{2\pi inL/M},\qquad |z_n-1|>c_*|n|^{-\kappa}\quad(n\ne0).
 \tag{2}
\]

\(n=1\) 由 (1/3<L/M<1/2) 直接付款，负频用共轭。这里只需要有限的多项式次数，不优化巨大常数。
另已核读Matveev1998原文Theorem2.2作为加法形式备份；准确来源、假设和核读限制见
[小分母审查](../reviews/2026-10-11/f1-phase-small-divisor-review.md)。没有声称重证上述经典定理或取得Matveev2000全文。

**相位引理。** 每个 \(P\in C^\infty(\mathbb R/M\mathbb Z)\) 都有唯一零Haar均值的光滑解

\[
 G(\theta+L)-G(\theta)=P(\theta+L)-\overline P,
 \qquad \overline P=M^{-1}\int_0^M P.
 \tag{3}
\]

采用频率 \(2\pi n/M\)，令

\[
 \widehat G(0)=0,\qquad
 \widehat G(n)={z_n\over z_n-1}\widehat P(n)\quad(n\ne0).
 \tag{4}
\]

(2)只造成固定多项式增长，光滑 \(P\) 的Fourier系数快速下降，故(4)及任意阶微分绝对一致收敛。
逐系数得到(3)，非零小分母及零均值给唯一性。定义
\(\|F\|_{H^s_n}^2=\sum_n(1+n^2)^s|\widehat F(n)|^2\)，则

\[
 \|G\|_{H^s_n}\le c_*^{-1}\|P-\overline P\|_{H^{s+\kappa}_n}.
 \tag{5}
\]

因此得到 \(C^\infty\to C^\infty\) 连续线性算子，并与平移、微分及复共轭相容。
这不是相同有限正则性阶的有界性，也不是乘法同态。仅用 (L/M) 无理不能证明这项存在性。

## 2. 全有限源指标的完整物理迹

设

\[
 C_B(x)=K_B(x,x),\quad P_B(\theta)=\int c(t)^2C_B(t+\theta)dt,
 \quad a_B=\overline P_B=L\overline C_B.
 \tag{6}
\]

最后等式来自原平方分割的 \(\int c^2=L\)。每个核导数在基本条带有界，故这些实际函数光滑且 \(M\)-周期。

434已逐截止证明压缩迹类。本节在其完整核迹上计算四个正交块；不在计算前删除源混合项。
对固定 \(r,s,B\)，两截止超过有限阈值后，深 \(p\) 边的原行只有
\(b^{(r)}_{j,k}(t)=\delta_{k,r}c(t)\)。可见矩形的每个新增 \(p\) 层因而贡献
\(\delta_{rs}P_B(nL)\)：核的共同 \(rM\) 平移准确由周期性消掉。

深 \(q\) 条带为

\[
 d_j^{(r)}(t)=\delta_{j0}d(t)+c(t)\{f(t-jL-rM)-f(t-jL)\}.
\]

令 \(y=t-jL\)，完整交叉能量的平方分割展开给

\[
 D_{rs}(y):=\sum_jd_j^{(r)}(y+jL)d_j^{(s)}(y+jL)
 =d(y)^2-f(y)^2+f(y-rM)f(y-sM).
 \tag{7}
\]

具体地，\(j=0\) 的交叉项为 \(f(f_r+f_s-2f)\)，其余乘积和为
\((f_r-f)(f_s-f)\sum_jc(y+jL)^2\)，与 \(d^2\) 相加恰得(7)。每个新增 \(q\) 层贡献

\[
 \mu_{rs}(B)=\int D_{rs}(y)C_B(y)dy
 =\int_0^M[1-\alpha(x)+\beta_{s-r}(x)]C_B(x)dx,
 \tag{8}
\]
\[
 \alpha(x)=\sum_kf(x+kM)^2,\qquad
 \beta_\ell(x)=\sum_kf(x+kM)f(x+(k-\ell)M).
\]

特别 \(\mu_{rr}(B)=M\overline C_B\)。由深边逐层增量，可见矩形迹准确为

\[
 \delta_{rs}\sum_{n=1}^{K_p}P_B(nL)+K_q\mu_{rs}(B)+E_{rs}(B).
 \tag{9}
\]

\(E_{rs}\) 可在任一足够深、已经迹类的有限矩形中按(9)求出；逐层公式证明它不再依赖截止。
这是实际有限角贡献，没有相减未准入的无穷总迹。

**两个逃逸球。** 令 \(\rho_p=2^{-1/2},\rho_q=5^{-1/2}\)，完整 \(p\) 球函数为

\[
 H_B(\theta)=(1-\rho_p^2)\sum_{a,b\ge1}\rho_p^{a+b-2}
 \int c(t)^2K_B(t+\theta+aL,t+\theta+bL)dt.
 \tag{10}
\]

球内 \(a\ne b\) 的相关全部保留。系数绝对可和、核各阶导数一致有界，故(10)在全部光滑范数中收敛。
球中固定 \(q=r,s\) 标签已可见，原 \(Q_q(r,s)=\delta_{rs}\)，因此贡献是
\(\delta_{rs}H_B(K_pL)\)。不需要短传播假设。

\(q\) 球的全部有限 \(p\) 标签同样可见，其贡献为固定常数

\[
 J_{rs}(B)=(1-\rho_q^2)\sum_{a,b\ge1}\rho_q^{a+b-2}
 \int D_{rs}(y)K_B(y+aM,y+bM)dy.
 \tag{11}
\]

共同 \(K_qM\) 平移由核周期性消掉。双球最终严格为零，因为源支撑只有固定水平边、有限宽负条带及有限角区。
四个正交块之间的交叉迹在434准入后为零。于是得到**准确式**

\[
 \operatorname{Tr}(P F_{r,s}(B)P)
 =\delta_{rs}\left\{\sum_{n=1}^{K_p}P_B(nL)+H_B(K_pL)\right\}
 +K_q\mu_{rs}(B)+E_{rs}(B)+J_{rs}(B).
 \tag{12}
\]

若核传播小于 \(L\)，(10)只有 \(a=b\)，还原437几何尾。
若 \(B=U(h)\)，(10)恒为 \(L\sum_{a\in\mathbb Z}\rho_p^{|a|}h(-aL)\)，还原435的完整球周期，并非仅 \(Lh(0)\)。

## 3. 规范相位读出及其表示无关性

对(6)的每个 \(P_B\) 应用(3)，得到零均值 \(G_B\)。必须对**完整**相位归一化：

\[
 \Phi_B=G_B+H_B-\overline H_B,\qquad \overline\Phi_B=0.
 \tag{13}
\]

一般不能把 \(G_B+H_B\) 本身叫作零均值。由望远镜和，(12)成为

\[
 \operatorname{Tr}(P F_{r,s}(B)P)
 =K_p\delta_{rs}a_B+K_q\mu_{rs}(B)
 +\delta_{rs}\Phi_B(K_pL)+R_{rs}(B),
 \tag{14}
\]
\[
 R_{rs}(B)=E_{rs}(B)+J_{rs}(B)
 +\delta_{rs}(\overline H_B-G_B(0)).
\]

对实际算子 \(Y=\sum_i F_{r_i,s_i}(B_i)+S\)、\(S\in\mathcal S_1\)，有限相加并加入 \(\operatorname{Tr}S\) 得

\[
 \operatorname{Tr}(PYP)=K_pv_p(Y)+K_qv_q(Y)
 +\Phi_Y(K_pL)+R(Y)+o(1),\qquad\overline\Phi_Y=0.
 \tag{15}
\]

只有迹类余项产生 \(o(1)\)；\(P\to1\) 强收敛使它沿任意独立双截止共尾路径趋于零。
体积、相位及常数均从实际源核算出，没有按期望Weil值选择减项。

**唯一性。** 两种有限表示之差是零算子，故
\(aK_p+bK_q+\Phi(K_pL)+c+o(1)=0\)。取 \(K_q=K_p\) 和 \(K_q=2K_p\)，有界相位使 \(a=b=0\)。
然后稠密无理转动及连续性使 \(\Phi\equiv-c\)，零均值给 \(\Phi=c=0\)。因此(15)四项是实际算子数据。
有限相加及伴随的真实压缩迹再给线性和
\(R(Y^*)=\overline{R(Y)}\)，另外三项同样星相容。

所以规范常数也可定义为

\[
 R(Y)=\lim_{K_p,K_q\to\infty}
 \{\operatorname{Tr}(PYP)-K_pv_p(Y)-K_qv_q(Y)-\Phi_Y(K_pL)\}.
 \tag{16}
\]

沿完整整数 \(K_p\) 的Cesàro平均，零均值相位给同一常数；这不等于任意子列选择或原线性共尾有限部。
单纯圆周坐标改名须同时移动物理轨道的初始相位，才保持常数；只移动符号却重新从0出发改变了实际数据。
规范性限于固定来源、分割、截止和零均值规则，没有证明辅助分割变化的独立下降。

## 4. 共轭相位不变，但新的加权边电荷不消失

源内共轭给 \(u^tF_{r,s}(B)u^{-t}=F_{r+t,s+t}(B)\)。两体积、相位及 \(q\) 球均保持：
(8)只依赖 \(s-r\)，(10)不依赖这些指标，(11)的 \(f_rf_s\) 同时平移 \(tM\) 后积分相同。

剩下的有限角变化须保留。逐 \(x\) 的全部源交叉能量在共同酉共轭下不变，故计算两外边的可积过渡差即可。

- \(p\) 外边只在 \(r=s\) 出现；共同 \(tM\) 移动给
  \(\delta_{rs}\int[a_p(x+tM)-a_p(x)]C_B(x)dx=t\delta_{rs}\int_0^M C_B\)。
  等式由 \(a_p\) 两端0、1及周期分块望远镜给出，负整数 \(t\) 同样成立。
- \(q\) 外边由(7)的 \(f_rf_s\) 移动给
  \(-t\int f(y-rM)f(y-sM)C_B(y)dy\)。

内部变化为外部变化的负数，得到全有限源共轭公式

\[
 R(F_{r+t,s+t}(B))-R(F_{r,s}(B))=-t\,\mathcal W_{s-r}(B),
 \tag{17}
\]
\[
 \mathcal W_\ell(B)=\int_0^M[\delta_{\ell0}-\beta_\ell(x)]C_B(x)dx.
 \tag{18}
\]

这些是紧过渡差的积分，没有相减无穷总能量。迹类余项的共轭缺陷零，因此(17)有限相加定义

\[
 \mathcal W(Y)=R(Y-uYu^*),\qquad
 R(u^tYu^{-t})=R(Y)-t\mathcal W(Y).
 \tag{19}
\]

表示无关性由(15)保证。对 \(r=s,B=U(h)\)，(18)为 \((M-I_f)h(0)\)，还原435；一般周期核则有非恒定权。
因此相位修复没有消去源通量。它也不消去427的旧迹类交换子电荷：\(R\) 在 \(\mathcal S_1\) 上仍是普通迹。

## 5. 零边电荷线性域不是乘法域

使用437的原合法分割 (L<D<M/2)，此时 \(\beta_1=0\)、\(\gamma_1=1-\alpha\ge0\)，且
\(\int_0^M\gamma_1\ge M-L>0\)。取非零、实、偶、非负的光滑 \(h\)，支撑在零附近两个小区间并令 \(h(0)=0\)。
可同时满足437原短传播条件。原实际有限词

\[
 Y=A(h)uA(h)=F_{0,0}(B)+S,
 \quad B=U(h)M_{\gamma_1}U(h)\ge0,\quad S\in\mathcal S_1
\]

有

\[
 C_B(x)=\int h(s)^2\gamma_1(x-s)ds,
\]
\[
 \mathcal W(Y)=\int h(s)^2
 \left\{\int_0^M\gamma_1(x)\gamma_1(x-s)dx\right\}ds>0.
 \tag{20}
\]

严格正性来自自相关在0为 \(\int\gamma_1^2>0\)，故其在零附近保持正，选择 \(h\) 支撑于该邻域即可。
另一方面，\(\mathcal W(A(h))=0\)，且 \(uA(h)=F_{1,0}(U(h))\) 的对角核为 \(h(0)=0\)，故边电荷也为零。
这两个零电荷元素的乘积却是(20)。

由(19)，\(\ker\mathcal W\) 是星线性、共轭稳定且 \(R\) 在其中源不变的最大线性域；(20)证明它**不是子代数**。
因而“先删除单位输入”或“只取零边电荷”都不能自动得到乘法稳定的无通量源域。
这个障碍已经在实际有限词中，不依赖任意新增周期核或范数完成。

## 6. 本轮付款与下一合同

本轮完成的是规范周期相位及430全部有限源域的实际读出，扩大并明确了原435的共轭缺陷。
尚未消除标量循环迹障碍，也未把非紧 \(Y-uYu^*\) 变成合法HH₁循环；431的有限边界单射性仍有效。
不继续优化这里的巨大Diophantine常数；下一合同转到[508](508-f1-prime-gap-archimedean-mixed-test.md)的实位间隙测试和真实相对闭链。

三个子任务独立核读小分母、全源物理矩阵及adelic比较；根线程另推导、交叉核对并合并。
完整范围见[域与通量审查](../reviews/2026-10-11/f1-phase-domain-independent-review.md)及
[桥接审查](../reviews/2026-10-11/f1-phase-adelic-bridge-review.md)。
[精确检查脚本](../scripts/source_phase_trace_exact_audit.py)通过1,364项有理断言：直接源矩阵的交叉能量、非恒定及有符号周期权的层增量、加权共轭通量，以及保留球尾的Fourier望远镜式。
[检查记录](../reviews/2026-10-11/f1-source-phase-exact-audit.json)明确区分整数周期离散模型与本稿光滑素数对数分析；这些检查没有代替无限证明或Lean形式化。
整轮逆审、来源核对和原数学文件保留情况见[整轮核对记录](../reviews/2026-10-11/f1-phase-round-verification.json)。
