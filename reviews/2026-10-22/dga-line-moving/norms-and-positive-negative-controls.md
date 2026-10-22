# 实际 DGA 模块的原费用、连续正反与函数域控制

2026-10-22。独占分支稿；服务本轮 actual adelic DGA 的 line/moving 准入。
不改 STATE/cadence，不开 C037/574。下列为已有实际 DGA 的有限代数操作、旧原范数后果和固定控制；
不申报新的经典 Weil 正性、独立 RR 容量或宏观净后果。

## 1. 先区分三种真实对象

输入为[实际 DGA 主稿](../../../goals/reviews/2026-10-22-adelic-restriction-relative-square-and-quadratic-capacity.md)§§3–5：
物理源 \(r=e^{u/2}f\)，\(F=\mathcal S_{\exp,\mathbf C}\)，负次数源为偶 Schwartz 的

\[
 S=\{\eta:\eta(0)=\textstyle\int\eta=0\},\quad
 E_c\eta(u)=e^{u/2}2\sum_{n\geq1}\eta(ne^u),\quad
 \mu_\pm(r)=\int e^{\pm u/2}r(u)du.
\]

令 \(\mathcal A\) 为该非 unital DGA 的单位化。这里只添加正式卷积单位，
不把 \(\delta_0\) 冒称原 \(F\) 的函数。次数零在原文的 \(\Phi\) 坐标中精确为

\[
 A^0\simeq F^+\times\mathbf C^2,
 \qquad A^{-1}=S,\qquad d\eta=(E_c\eta,0,0),             \tag{1}
\]

其中 \(F^+=\mathbf C\mathbf1\oplus F\)；物理源的实际嵌入是

\[
 a_r=j(r)=(r,\mu_+(r),\mu_-(r)),                         \tag{2}
\]

而不是只取首分量。负次数作用使用

\[
 U_r\eta(x)=\int e^{-t/2}r(t)\eta(e^{-t}x)dt.            \tag{3}
\]

原文已付 \(U_rU_s=U_{r*s}\)、\(E_cU_r=r*E_c\) 和 Peiffer；此处不另行计功。
记 \(R=H^0(\mathcal A)\)。同调上的 \(R\) 仍为保两 degree 的旧 405 商之单位化，
没有因加上单位而得到新的算术结构层。

后面必须分别记录：

1. \(\mathcal A\) 上真实有限自由 DG 模块及其 DG 变基；
2. \(A^0\) 在原 Hilbert 空间上的代表元作用；
3. \(R\) 上消全部 Pan 的对象。

第二项不是第三项的正表示：对实际非零 principal \(q\)，原卷积算子 \(T_q\) 可非零，
它的 DG 零同伦并没有在下面单独选取的 Hilbert 空间里实现。

## 2. 有费的 graph line 确实存在，但其 Picard 类恒定

对任意实际 \(r\in F\)，令

\[
 \mathcal L_r=\mathcal A\,(1,a_r)\subset\mathcal A^2,
 \qquad v_r=(1,a_r),\quad s_r=a_rv_r.                  \tag{4}
\]

这是具体的 rank-one DG 模块及其实际物理源映射；第一坐标投影给逆，故

\[
 \mathcal L_r\simeq\mathcal A,\quad
 \mathcal A^2/\mathcal L_r\simeq\mathcal A,\quad
 e_r=\begin{pmatrix}1&0\\a_r&0\end{pmatrix},\quad e_r^2=e_r. \tag{5}
\]

不需 \(1+a_r^\dagger a_r\) 可逆，更没有假定 \(\dagger\) 已正。
任意 DG 基变 \(\mathcal A\to\mathcal A'\) 都将此有限自由模块变为同样的 graph line；
这一步的代数 derived base change 没有未付 Tor。它不等于某个新 proper family 的
pushforward/cohomology base-change 定理，更不自动给完成 Fréchet 范畴的所有 tensor 比较。

这里 \(v_r\) 是生成 frame，\(s_r\) 才是根 section。537 非根 \(r_0\) 在 \(a_{r_0}\)
及 \(s_{r_0}\) 的同调 marking 中非零；忘掉 embedding 及根 section 后，底线连同生成 frame
\((\mathcal L_r,v_r)\) 对每个 \(r\) 都是同一自由 pair。
所以“有实际 line 对象”与“degree-zero Picard 类实际移动”不同。
如果把源信息只放在标记上，再宣称底 line 的 degree 已编码完整 Weil 型，尚无计算依据。

真实可逆的 unitriangular 变基也存在：若 \(N^2=0\) 是固定二阶矩阵，

\[
 G_r=I+a_rN,\qquad G_r^{-1}=I-a_rN.                    \tag{6}
\]

不能把所有这类操作说成不存在。但 (6) 不产生 rank-one Picard 类。
在额外添加的 \(\mathbf P^1_{\mathcal A}\) 上，rank-one 平方零 clutch

\[
 1+\varepsilon a_rz^{-1},\qquad \varepsilon^2=0,
\]

本身延拓为无穷 chart \(w=z^{-1}\) 上的单位 \(1+\varepsilon a_rw\)，故是 coboundary。
这是该具体 clutch 的精确失败，非所有相对/derived Picard 操作的不可能性定理。
在真实高亏格曲线上，非零 \(H^1(\mathcal O)\) 可支持不同的平方零变形；该曲线和 cocycle
若另行加入，须支付它与实际源的比较，不能由 (1) 自动获得。

## 3. 全 principal 可以严格处理，但最强有限对象仍是旧商的 derived 实现

原文的全 principal 同伦为：对实际 \(q=E_c\eta_q\in C P_{\rm an}\)，

\[
 a_q=d\eta_q,\quad
 T_q=dK_q+K_qd,\qquad
 K_q(\lambda\mathbf1+(g,\alpha,\beta))
       =\lambda\eta_q+U_g\eta_q.                     \tag{7}
\]

经 frame \(v_r\) 识别，根 section \(s_r\) 为 \(a_r\)；
对 \(r+q\) 与 \(r\)，它们只在 DG 同伦意义下相差 exact 项。不能把它说成
原 \(A^0\) 中逐点相等，也不能直接说任何普通单位 clutch 已严格下降。

有一个有限 semi-free 对象可以把这个同伦写成真正的协调变基：

\[
 \mathcal K_r=\mathcal A[\epsilon_r],\quad
 |\epsilon_r|=-1,\quad d\epsilon_r=a_r,\quad\epsilon_r^2=0. \tag{8}
\]

它是单元 Koszul DG 对象，底层是一个零次和一个负一次自由生成元。
对整个实际 Pan，

\[
 \mathcal K_{r+q}\xrightarrow{\sim}\mathcal K_r,
 \qquad\epsilon_{r+q}\longmapsto\epsilon_r+\eta_q       \tag{9}
\]

是严格 DG 同构：微分给 \(a_r+d\eta_q=a_{r+q}\)，奇次数交换性给平方为零，
逆为减去 \(\eta_q\)。实际 \(E_c\) 单射使 \(\eta_{q_1+q_2}=\eta_{q_1}+\eta_{q_2}\)，
所以这些变基满足严格可加的 overlap 协同。此处不是凭形式标签宣布下降。
有限 semi-free 性也给任意代数 DG 基变下的同一公式。
普通 Koszul 与 Čech 定义可对照 [Stacks 36.9](https://stacks.math.columbia.edu/tag/08CX)；
(8)–(9)在本实际 DGA 中由上面直接验证负责。

对 537 实际 \(r_0\)，\(\bar a_{r_0}\ne0\in R\)，所以

\[
 H^0(\mathcal K_{r_0})=R/(\bar a_{r_0}),\qquad
 H^0(\mathcal K_0)=R.                                  \tag{10}
\]

它们不能作为 \(R\)-模相同：前者的 annihilator 是非零理想 \((\bar a_{r_0})\)，后者为零。
因此这确实保留非根对象；但其有限自由 determinant presentation 为

\[
 \det(\mathcal A)\otimes\det(\mathcal A)^{-1}\simeq\mathcal A, \tag{11}
\]

类恒定。同源信息在 derived zero-locus/微分中，不在新 Picard 移动或独立正容量中。
(8)没有为 (1) 增加新的算术主关系或 \(RR\) 二次系数；只是把旧 \(R\) 的 multiplication cone
写成实际可协调对象。不能将这一合法实现重复申报为新独立正性。

## 4. 原 du/Dlog 费用：只付代表元，不伪造正商范数

令

\[
 \|r\|_{D_{\log}}^2=(2\pi)^{-1}\int\log(2+|t|)|\widehat r(t)|^2dt,
 \qquad\|r\|_{du}^2=\int|r|^2du.
\]

暂以 \(X=H\oplus\mathbf C^2\) 作次数零代数的一个表示，
其中 \(H=L^2(du)\) 或原 \(D_{\log}\)；两有限 degree 暂取标准欧氏范数。
这只是明示的外部代表元 norm，未认证为 canonical 算术 metric。令

\[
 T_r=\operatorname{diag}(r*\cdot,\mu_+(r),\mu_-(r)).    \tag{12}
\]

对 \(\operatorname{supp}r\subset[-L,L]\)，Young/Fourier multiplier 及 Cauchy 给

\[
 \|r*\cdot\|_{H\to H}\le\|r\|_1\le\sqrt{2L}\|r\|_{du},
 \qquad |\mu_\pm(r)|\le\sqrt{2\sinh L}\|r\|_{du}.      \tag{13}
\]

于是

\[
 \|T_r\|\le C_L\|r\|_{du},\qquad C_L=\sqrt{2\sinh L}. \tag{14}
\]

若 \(\mu_\pm(r)=0\)，可取 \(C_L=\sqrt{2L}\)。以 \(\|r\|_{D_{\log}}\) 计源费时，
所有右侧常数再除 \(\sqrt{\log2}\) 即给合法上界，未称 sharp。
graph 的代表元投影及 unipotent 满足

\[
 \|e_r\|=\sqrt{1+\|T_r\|^2},\quad
 \|e_r-e_s\|=\|T_{r-s}\|,\qquad
 \|I\pm T_rN\|\le1+\|T_r\|\|N\|.                     \tag{15}
\]

这些不是全空间 worst-case 下界，更不是必要实际源的最小 lift 费。
它们只是具体 chosen representative 的上界；Pan 的卷积作用在 \(X\) 中通常不为零，
所以 (12) 不是 \(R\) 的正表示，也不能把 (15) 当作已经下降的正商 norm。

整个 DG 对象还须付负次数源。对实际 Schwartz 半范数

\[
 q_{a,b}(\eta)=\sup_x|x^a\eta^{(b)}(x)|,\quad\kappa=a-b-\tfrac12,
\]

(3)给精确权预算

\[
 q_{a,b}(U_r\eta)\le q_{a,b}(\eta)\int|r(t)|e^{\kappa t}dt
 \le q_{a,b}(\eta)
 \sqrt{\frac{\sinh(2\kappa L)}\kappa}\,\|r\|_{du}.     \tag{16}
\]

\(\kappa=0\) 取极限 \(\sqrt{2L}\)；这里整数 \(a,b\) 实际无零值。
对全 \(F\) 则保第一项的带权 \(L^1\) 费用，不压成全线统一 \(du\) 常数。
(9)的变基成本含 \(\eta_q\) 的半范数，不能从 (15) 擅自删去。

可用整个实际 405 平移族直接看其量词：令 \(r_p=E_c\eta_p\ne0\)，

\[
 r_{p,v}=\tau_vr_p,
 \qquad\eta_{p,v}(x)=e^{-v/2}\eta_p(e^{-v}x),
 \qquad E_c\eta_{p,v}=r_{p,v}.                        \tag{17}
\]

原 \(du/Dlog\) 源 norm 对平移不变，而

\[
 q_{a,b}(\eta_{p,v})=e^{(a-b-1/2)v}q_{a,b}(\eta_p).    \tag{18}
\]

在该固定半范数及实际单射源 lift 中，这是等式；不声称所有可能的新几何 lift 都有同一必要费用。
它准确说明：全 Pan 的实际 DG 协同虽有公式，却没有因此得到以全线 \(du/Dlog\) 控制的统一源费用。

更强的旧 [553](../../../notes/553-principal-cyclic-closure-and-cofinal-readout-fees.md) 已证明：
全 physical Pan 在全线 \(du/Dlog\) 稠密。因此任何对此 norm 全域连续、
消去全部 principal coset、值于一个共同 Hausdorff 目标的类映射都恒定；
不论目标称 Hilbert、Picard 或 nonlinear moduli。
此结论不排 \(F\)-拓扑、真正变域、源依赖非共同目标、只在 compact 域有费或 cofinal 付费的逃逸。
尤其 \(P_{\rm an}\cap C_c^\infty=0\)：compact 域上“检查全部 compact principal”是空条件，
不能取代 (7)、(9) 对非 compact 实际源的检验。

## 5. 裸 principal section、单位与 localization 的真实边界

对 537 双 pole-zero \(r_0\)，在 (1) 中

\[
 a_{r_0}=(r_0,0,0),\qquad a_{r_0}e_+=a_{r_0}e_-=0.    \tag{19}
\]

两个 degree idempotent 在 \(R\) 中仍非零，且 \(\bar a_{r_0}\ne0\)。
所以这个裸标量 section 在原 \(A^0\) 及 \(R\) 中都为 zero divisor；
不能直接命名为 regular Cartier section 并照搬 effective Cartier exact sequence。
剔除两个 degree component、改用矩阵 determinant/相对 section、或经另一 geometric base 实现是合法修复，
但必须重新核双 pole 与同一预算；(19)并不排除这些修复。

“改成 \(1+t a_r\)”也不能无条件宣布为原代数的 unit。取

\[
 r_0=(D^2-\tfrac14)\psi,\quad0\ne\psi\ge0,
 \quad\psi\in C_c^\infty((-17/16,17/16)),\quad
 t_*=4/\!\int\psi.
\]

积分 character \(\ell(\lambda\mathbf1+r)=\lambda+\int r\) 在原 \(F^+\) 乘法下合法，
且 \(\ell(1+t_*r_0)=0\)。所以 \(1+t_*a_{r_0}\) 在原 \(A^0\) 非 unit。
这里只消费原 \(A^0/F^+\)；该积分 character 没有证明消全部 Pan，
不据此声称它在 \(R=H^0(\mathcal A)\) 也非 unit。

在 \(L^1\) Banach 完成中，小 \(t\) 的 Neumann inverse 与 operator 界

\[
 \|(I+t\,r*)^{-1}\|\le(1-|t|\|r\|_1)^{-1}
 \quad (|t|\|r\|_1<1)                                \tag{20}
\]

是真的，但未由此证明逆属于全指数 \(F^+\)，也未使其变成 \(R\) 的表示。
若选择代数 localization \(\mathcal A[(1+t a_r)^{-1}]\)，这是合法变 base；
源依赖 cover \(D(a_r)\cup D(1+t a_r)\) 也由 unit ideal 关系覆盖。
仅用 \(a_r\) 和 \(1+t a_r\) 各自幂构造的 transition 延拓到各 chart，仍为 coboundary。
更复杂 Picard cocycle 未被排除；其独立选择、原拓扑 inverse/overlap 费用和容量仍待给出。
不能把一个坏 chart 的发散当所有实际源的必要费用，也不能将变 base 后失掉的 source 当已保存。

## 6. 连续正反例：同一模块设施不决定完整 mixed 号

沿 562–568 的真实 positive primitive/g-integer 连续族

\[
 Z_c(s)=1+\frac c{s(s-1)},\quad0<c\le\tfrac12,
 \qquad d=c-\tfrac14,
 \qquad R_d=\mathbf C[z]/(z^2+d),\quad z^\dagger=-z.   \tag{21}
\]

其 complete 对象是 \(s(s-1)Z_c=s^2-s+c\)，本例真实 \(\Gamma=0\)，
0、1 两 pole 与全部 \(\Pi_c\) 项均保留；不将它假装成经典的 adelic DGA。
分布侧 ODE 给实际 convolution map

\[
 x_r=\int r(u)e^{uz}du=A_r+B_rz,\quad
 x_{r*s}=x_rx_s,\quad x_{r^*}=x_r^\dagger,
 \quad Q_d(r)=\operatorname{Tr}(x_rx_r^\dagger)
             =2|A_r|^2+2d|B_r|^2.                   \tag{22}
\]

这个完整 trace 身份来自已给分布的 ODE/显式公式，不是按根位置另选正 metric。
对 \(d=1/16\)，\(e^{uz}=\cos(u/4)+4\sin(u/4)z\)；
对 \(d=-1/16\)，为 \(\cosh(u/4)+4\sinh(u/4)z\)。
两个同为 reduced、非退化二维代数，graph free line、unitriangular 变基、
Koszul/basechange/有限局部化都同样存在。

可以连双 pole-zero 源也固定为同一种实际 recipe：取偶非负 \(\phi\in C_c^\infty((-1,1))\)，
非零，令 \(g(u)=u\phi(u)\)，\(r=(D^2-1/4)g\)。则 \(\mu_\pm(r)=0\)，
奇偶给 \(A_g=0\)，两例的 \(B_g>0\)，且分部积分给

\[
 x_r=-(d+\tfrac14)x_g=-c x_g,
 \qquad Q_d(r)=2d\,c^2|B_g|^2.                       \tag{23}
\]

因此同样良定义、有原费用的模块操作在 \(d=+1/16\) 给正，在 \(d=-1/16\) 给负。
graph/Picard/局部 jets 的代数存在不推出所需号。
这只反驳“以上设施自身已够”，不反驳能独立区分两例的更强有效性、极化或 mixed 容量。

该比较也说明：不能为了让负例转正而用普通 Hilbert–Schmidt adjoint 取代原 \(\dagger\)；
那会改变 (22) 的完整 Weil 型。一般 \(g\) 不自动有加法 adeles，
连续控制只检验可自然移植的有限代数设施，不声称把经典 \(E_c\) 原封不动搬给它们。

## 7. 函数域正控制：真实 degree-zero line 与 mixed 容量另有来源

取已付真例 \(E/\mathbf F_5:y^2=x^3+x+1\)，\(P=(0,1)\)，无穷点 \(O\)。

\[
 L=\mathcal O_E(P-O)                                  \tag{24}
\]

是真 degree-zero 非平凡 line：若 \(P-O\) 为 principal，函数将给 \(E\to\mathbf P^1\)
的 degree-one map，违反 genus-one。它与恒 free 的 (4) 不同；
其 \(h^0=h^1=0\)，而 \(L(O)=\mathcal O_E(P)\) 具有 \(h^0=1,h^1=0\)。
参数 \(T\in E\) 的 \(\mathcal O_E(T-O)\) 是实际 Picard 族，
在 \(E\times E\) 上的规范 Poincaré line 给跨 chart 的同一对象；
这种 family、proper pushforward 和有效 divisor 不是单给一个 coefficient DGA 即可恢复。
函数域的真正 base-change 定理需 flat/proper/finite-presentation 等几何前件，
可对照 [Stacks 36.30](https://stacks.math.columbia.edu/tag/0A1G)；
不把 graph 的有限自由基变偷换为该定理的全部前件已付。

作为所需 mixed 正号的精确已付控制，旧 563 给

\[
 A=\begin{pmatrix}0&-5\\1&-3\end{pmatrix},\quad
 A^\dagger=-3I-A=5A^{-1},\quad
 \operatorname{Tr}((aI+bA)(aI+bA)^\dagger)
 =2|a|^2-6\Re(a\bar b)+10|b|^2,                      \tag{25}
\]

其 Hermitian Gram determinant 为 11，故全 mixed 正。
这里正号的独立几何来源是 Jacobian 的 ample 极化/有效 mixed intersection，
不是模块自由性或 determinant 标量；详见前轮
[Rosati 原件消费](../roadmap-after-573/positive-realization-admission.md)。
全 period aliases 及 \(H^0/H^2\) poles 仍消费旧完整 trace 身份，不以单次有限矩阵替代。

另外，固定 \(\mathbf F_5\) 上的 \(\operatorname{Pic}^0(E)(\mathbf F_5)\) 是有限群；
复向量源的加法群是 divisible，因此到该有限群的群同态只能为零。
这不是反对函数域策略，而是阻止错误的目标类型：需要几何参数族、相对 formal base，
或先做整数/有理对应再 complexification，不能要求物理复源字面线性地映入固定有限 Picard 点集。

## 8. 完整经典目标与止损结论

经典仍保持

\[
\begin{aligned}
 Q_\zeta(r)={}&2\Re(\mu_+\overline{\mu_-})
 +[\psi(1/4)-\log\pi]\|r\|_{du}^2\\
 &+\frac12\int_0^\infty\frac{2e^{-v/2}}{1-e^{-2v}}
             \|\tau_vr-r\|_{du}^2dv\\
 &-2\sum_{p,k\ge1}(\log p)p^{-k/2}
             \Re(r*r^*)(k\log p).
\end{aligned}                                                    \tag{26}
\]

本分支没有把完整 \(\Gamma/contact\)、任一 proper prime power 或 signed 两 pole 删除。
只是证明：有限 module/free graph/Koszul 操作确实存在、全 Pan 可做实际协调、原费用可列；
它们还未提供新的 degree-zero Picard 移动，也未独立支付 (26) 的 mixed 正号。

仍缺的独立输入必须在同一个实际对象上给出：

* 真实物理源到可移动相对 line/correspondence 族，且全 principal 的变换、非根及两 degree 同时可见；
* chart/overlap、局部消失过滤与截面 lift 的原域 metric 费用，不只一个 free representative；
* 独立有效性/ample 极化或 RR mixed 二次容量，其正号能拒绝 (23) 的负段；
* 同一容量预算与 (26) 的完整 \(\Gamma\)、全部 \(p^k\)、两 poles 的 coefficient/finite-part 身份。

若只把 (26) 指定为容量二次系数并假定其非负，仍是 Weil 正性等价/充分条件改写。
目前这些实际有限操作最终回到旧 \(R\) 及其 multiplication cone，
所以本入口应来源 0 停止，不继续调 unipotent 参数、Koszul 长度、额外 projective base 或坏 chart。
合法的新几何族、强拓扑/变域/源依赖 cofinal 费用、非标量对应和独立 mixed 容量仍未排除。
最强旧 whole \(4/5\) 上预算、实际 core/coupling/\(\Xi\) 与宏观完成门均不变。
