# 67.25% 比例、坏行密度与可变几何 endpoint：有限推导

日期：2026-10-07。独立推导；只读数学仓库，未构建，未修改旧稿。本报告不认证整个 7/8 主稿，不宣称新的无零半平面或 RH。

分析对象：`E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`。下文行号均指该文件。本次读取的 canonical LF SHA256（CRLF→LF，UTF-8）：

`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`。

结论分为三层：AF 的高度平均比例不能直接降低本稿的坏行幂指数；可以准确写出所缺的 hybrid row-density 输入；可变槽长度的低、高账本和局部 Euler 解析域存在具体可核验的延伸，但把这些组合成新无零区域仍需逐项验收同一实际源。

## 1. 比例和 detector 实际计数不同

采用用户指定的 [Alpöge–Furman arXiv:2608.13637v2](https://arxiv.org/pdf/2608.13637v2)，而非另换版本或更强比例。其 Theorem A 的分母是按重数计的高度窗口零数，分子是简单且在临界线的零点数；Theorem B 是每个固定本原 Dirichlet 字符的同类断言。Montgomery–Taylor 窗给

\[
 c_{\rm AF}=\frac32-\frac1{\sqrt2}\cot\frac1{\sqrt2}
 =0.6725007036794116\ldots.
 \tag{1}
\]

这不是本稿随行导子移动的全部 Hecke 字符族的一致定理。该文关于 \(\xi'\) 的另一比例也不能当作原 \(L\) 的零数。原文 §1.4 明确其输入不能排除 \(o(N)\) 个离线零；该说明与下面的计数障碍一致。

本稿 4223–4254 的实际族为

\[
 \mathcal X_u=\{\psi_{u,\nu,\varsigma}(n)
  =\nu(n)\chi_n(u)^{\varsigma}:\nu\in\Theta,\varsigma=\pm1\},
 \quad q_u\asymp U=Z^d,\quad Q_{\psi^*}\ll_{\mathcal A}q_u.
 \tag{2}
\]

它保留原零延拓、删除 Euler 因子以及诱导到本原字符的步骤。4260–4268 的有限 principal 例外由源本身分类，而不是由比例选掉。4270–4304 的检测高度为 \(T_1=Z^\tau\)，且 \(\tau\ll d\)。每个动态 bin 用 \(|\Im\rho|\le3iT_1\) 内的一枚实际 \(L(\rho,\psi^*)=0\) 作为 witness；若 \(a>51/100\)，则

\[
 a\le\Re\rho<a+e,\qquad \delta=2a-1>1/50.
 \tag{3}
\]

所以 detector 的坏行数 \(\#\mathcal C\) 计的是**至少有一枚这样的零的导子行**。它不计每个固定函数在 \(T\to\infty\) 时的平均好零比例。

严格的非蕴含有三个层次。

1. 固定字符的渐近常数不能自动用于 \(U\to\infty\) 的移动 Hecke 族，尤其检测高度只有 \(Z^\tau\)，远小于行导子尺度 \(Z^d\)。
2. 即使额外假设比例在此全族一致，仍可能每行各有一个孤立离线零而所有行均坏。形式反模型可给每行放一对 \(\beta+i\gamma,1-\beta+i\gamma\)（及共轭族所需的对称零），再放满足所需高度增长的无限多个简单临界线零；好零比例趋于 1，而每行仍被 (3) 检出。取 \(1/2<\beta<7/8\) 不冲突于拟用的 7/8 bootstrap。这只是零点多重集的逻辑反模型，**不声称构造满足 Euler 乘积的真实 L 函数**。
3. 即使真的得到 \(\#\mathcal C\le(1-c_{\rm AF})U^R\)，也只改变乘法常数：\(\log_U(1-c_{\rm AF})\to0\)。不能把 \(0.6725\) 或 \(0.3275\) 当作 \(R\) 的幂次节省。

## 2. 最小明确 hybrid 输入及其灵敏度

设 \(\mathcal C\) 是 15712–15724 的实际点态行子集：每一保留的外部 Mellin 参数、error-slot 子集、amplitude class 以及 witness subdivision 都须覆盖。写

\[
 x=q/\delta\in[0,1/2],\quad
 D_x=3-17x/9,\quad P_x=(2-8x/9)(1-x),\quad \alpha=5/6,
\]
\[
 J=(\alpha-\delta)D_x+\delta P_x,\qquad
 R_*=1-\delta+\frac{(\alpha-\delta)\delta P_x}{2J}.
 \tag{4}
\]

本稿 15949–15992 的平衡 exponent 是 (4)；原 \(\Delta=\beta_*-7/8\ge0\) 容量变动产生额外 \(\Delta/4\)。最小有用的新假设是：对所有以上实际 \(\mathcal C\)，存在固定 \(\eta>0\)，统一有

\[
 ({\rm HD}_\eta)\qquad
 \#\mathcal C\ll_{\mathcal A,\epsilon}
 U^{R_*+\Delta/4-\eta+\epsilon}(1+T_1)^A.
 \tag{5}
\]

它比 AF 增加的是**移动行族中的幂次稀疏性**。不要求重新定义字符族、替换源或按目标零点重选权重。高度指数 \(A\) 必须有限、统一且在选择 \(\tau\) 前确定；在底数 \(U\) 下，其成本是 \(A\tau/d\)，必须从真正的 \(\eta\) 余量中支付。

一项更强但清楚的充分假设是给实际检测零总数

\[
 Z_{\mathcal C}(a,T_1)=
 \sum_{u\in\mathcal C}\sum_{\psi^*\in\mathcal X_u}
 \sum_{\substack{L(\rho,\psi^*)=0\\
          \Re\rho\ge a,\ |\Im\rho|\le3IT_1}}m_\rho
 \tag{6}
\]

同样的幂次上界。因为每坏行至少有一枚 witness，\(\#\mathcal C\le Z_{\mathcal C}\)。单独的高度比例没有给出 (6) 在导子族中的幂次上界。

15726–15734 精确给出

\[
 \frac{\partial E(d)}{\partial R}=d,qquad
 h=13/16,qquad c_*=49/440640.
 \tag{7}
\]

因此 (5) 在 endpoint 节省 \(13\eta/16\)。在主稿**已分析的** \(\Delta\ge0\) 范围，16085–16109 变为

\[
 E(h)-\Delta\le-c_*-\frac{51}{64}\Delta
 -\frac{13}{16}\eta+\epsilon_{\rm total}.
 \tag{8}
\]

若另付出有符号 \(\Delta<0\) 的全部统一接口，且同一个 (5) 仍成立，则候选改善 \(\varepsilon=7/8-\sigma\) 的**仅高侧**必要验账形式为

\[
 \varepsilon<\frac{64}{51}c_*+\frac{52}{51}\eta
 \quad\text{（还须留出所有误差）。}
 \tag{9}
\]

例如右端在 \(\eta=0,0.001,0.005\) 时分别约为
\(0.0001395475,0.0011591553,0.0052375867\)。这只是敏感度，不是新边界：固定 geometry 的 low 仍在 \(7/8\) 与信号相交，而且 (5) 也不是 AF 的结果。若不拟作有符号 \(\Delta\) 延伸，应改假设为 \(R\le R_*-\eta\)，不能直接沿用旧稿的正 \(\Delta\) 扰动项。

## 3. 可变 geometry：low、信号与固定留数

6857–6867、8564–8575 明确只验收
\(b=1/8,\ell=1/6,h=13/16\) 的 geometry。为了检查相同有限补偿源的可变账本，设

\[
 M+\ell=1,\quad l_y-l_x=b,\quad h=1-l_x+\ell,
\]
\[
 l_x=\frac{1-\ell-b}{2},\quad l_y=\frac{1-\ell+b}{2},
 \quad h=\frac{1+3\ell+b}{2}.
 \tag{10}
\]

5584–5589、6269–6276 的 principal 留数固定为 \(w=1,z=1/6\)，故

\[
 C_b(s)=s+l_x/2-1+h/6=s-2/3-b/6.
 \tag{11}
\]

这里 \(1/6\) 是 \(\zeta_F(6z)\) 的极点位置，**不能随总槽长度 \(\ell\) 改变**。

原 low 为 \(l_x/2+b/12\)，不是 \(1/6+b/6\)。在 (10) 下它是

\[
 A_0=\frac{1-\ell}{4}-\frac b6.
 \tag{12}
\]

还必须保留完成行的 clipping 项。8073–8081 对 rescaled 子集记 \(d=\sum_{i\in J}\ell_i\)、\(M'=M-2d\)、\(\ell'=\ell-d\)。一般 reflected-energy 7747–7803 明确在固定有界 log-length 集上统一。8306 的第二能量分支，在 (10) 中为

\[
 M'+\frac{1+3\ell'-2M'-2\Delta_H}{4}
 =M'+\frac{5\ell-1+d-2\Delta_H}{4}.
 \tag{13}
\]

第一分支为 \(M'-\Delta_H\)。故在同一完成行 reduction 可应用该通用引理的前提下，行平方范数成本是
\((5\ell-1+d)_+/4\)。Cauchy 的成本减半，而 8626–8632 的子集权重、tuple 数以及 \(X'^{1/2}\) 一起产生 \(-d\)。准确的代数最大值为

\[
 \max_{0\le d\le\ell}
 \left\{-d+\frac{(5\ell-1+d)_+}{8}\right\}
 =\frac{(5\ell-1)_+}{8}.
 \tag{14}
\]

因此相同低侧证法的延伸账本应为

\[
 A_{\rm low}(\ell,b)=\frac{1-\ell}{4}-\frac b6
                   +\frac{(5\ell-1)_+}{8},
\]
\[
 \sigma_{\rm low}(\ell)=\frac{11}{12}-\frac\ell4
                         +\frac{(5\ell-1)_+}{8}.
 \tag{15}
\]

固定 \(\ell=1/6\) 时，\(b\) 完全从交点消失；单独减 \(b\) 不能把 low 边界移到 \(7/8\) 左侧。\(\ell\le1/5\) 时交点斜率为 \(-1/4\)；\(\ell>1/5\) 后斜率反成 \(3/8\)。低账本的形式最优是 \(\ell=1/5,\sigma=13/15\)，但高侧远未准许这个幅度。

8340–8360 的 additive Gram 命题本身给多项式范围的 \(Q,Y'\) 及 \(P_a=Y'^2/Q\ge1\)。在可变 geometry 中 \(P_a\asymp Z^b\)，一个方便的严格充分长度域是

\[
 b>0,\quad 1-3\ell>0,\quad 3\ell+b<1,
 \quad 9\ell+8b<3.
 \tag{16}
\]

最后一项正是最坏子集 \(d=\ell\) 的
\(l_y-d-11b/6>0\)，保证 \(P_a^2/Y'\ll P_a^{1/6}\)。在此域，(13)–(15) 是保留所有原项后的低侧推导，仍须核验通用行引理在新槽系统上的同源准入，不能只引用原固定 geometry 的 Proposition low 充当新命题。

## 4. 一般 high 常数的独立修正

6090–6091 是一般 high 账本，15729 是其固定实例。把 \(g=q\ell\) 及 \(\sigma_\ell=11/12-\ell/4\)（此节限 \(\ell\le1/5\)）代入，准确得到

\[
 E_{\sigma_\ell}(h)
 =K(\ell,b)+(1/2+\ell)\delta+\ell q-h(1-R),
\]
\[
 K(\ell,b)=-\frac14+\frac{5\ell}{4}+\frac b6,
 \tag{17}
\]
\[
 E(d)=E(h)+(d-h)(R+\delta/2-17/50).
 \tag{18}
\]

直接验算：在 \(d=h\) 时原式为
\(a-\sigma_\ell-a l_y-\ell/2+q\ell-h/6+hR+h\delta/2\)。常数是
\((1-l_y)/2-\sigma_\ell-\ell/2-h/6+h\)，即 (17)。若误把 \(-h/6\) 替成 \(-h\ell\)，会得到带 \(\ell^2,b\ell\) 的错误常数；两者差恰为 \(h(1/6-\ell)\)。本报告采用固定 \(z\)-留数后的 (17)。

可变几何的局部敏感度为

\[
 \partial_bE(h)=R/2-1/3,\qquad
 \partial_\ell E(h)=-1/4+\delta+q+3R/2.
 \tag{19}
\]

减 \(b\) 是否改善 high 取决于具体 \(R\)，不能只凭低账本判断。当 \(R<2/3\) 时减 \(b\) 反会增加 \(E\)；\(R>2/3\) 时才降低 \(E\)。

## 5. 一个保留全部 clipping 的小扰动证书

本节是**名义账本的有理数证书**，假设可以把原稿的 \(\beta_*\le7/8\) 作为已验收 bootstrap，并在新源上支付 §8 的统一接口。采用保守 \(\kappa=3/4\) 以及 \(\delta\le3/4\)，而不是把 \(\beta_*\) 减去新候选边界所得的量塞入旧 \(\Delta\) 容量公式。原 moment 的 \(\kappa\in[3/4,1]\) 统一域在 16238–16242 明确包含这个端点。

令 \(b=1/8\)，\(\ell=1/6+t\)，沿用 (4) 的 \(\Delta=0\) 容量。因

\[
 3P_x\le2D_x\quad(0\le x\le1/2),
 \qquad R_*\le1-2\delta/3,
\]

有精确线性扰动

\[
 E_t(h_t)-E_0(h_0)
 =t(-1/4+\delta+q+3R_*/2)
 \le(5/3)t.
 \tag{20}
\]

这里用 \(q\le\delta/2\)；保守地允许 \(\delta\le5/6\) 仍足够。\(3P\le2D\) 可直接展开：
\(2D-3P=x(44-24x)/9\ge0\)。

原 16039–16069 的 endpoint completed-square 证书给 \(E_0\le-c_*\)。取

\[
 t=1/20000,\quad
 \ell=10003/60000,\quad h=32503/40000,
 \quad \sigma_\ell=69999/80000=0.8749875,
\]
\[
 c_*-(5/3)t=\frac{307}{11016000}>0.
 \tag{21}
\]

其他可直接核算的名义余量如下。

- Floor bin 15843–15850：\(\delta_0=1/50,R=1,q\le\delta_0/2\)，故
  \(E_t(h_t)\le-7/1200+(32/25)t=-4327/750000<0\)。
- 固定 \(d\) 时由 (18) 或一般原式直接得
  \(\partial_\ell E(d)=13/50+\delta/4+q\le177/200\)。所以 16146–16165 的 intermediate 余量在此扰动后至少为
  \(49/14400-177/4000000=120907/36000000>0\)。
- \(\ell/h\) 随 \(\ell\) 严格增加，因为
  \(\partial_\ell(\ell/h)=(1+b)/(2h^2)>0\)。故原实际槽供给 \(8/39>1/5>7/37\) 的 margin 得以保留；固定 mesh 可以再细分，不能通过替换 prime 集实现。
- (16) 在 \(t=1/20000\) 仍有严格正余量，而且 \(\ell<1/5\)，(15) 的 clipping 不提高最终 low。\(\ell\) 的增加不是任意忽略 clipping。
- 当 \(R\ge1-\delta\) 时，frequency slope
  \(R+\delta/2-17/50\ge33/50-\delta/2>0\)。\(d\) 稍越 \(h_t\) 的成本仍可由一小段 \(\zeta>0\) 支付，且 source supply 更宽。

这些有理数等式已用 Python `fractions.Fraction` 核验；没有浮点数参与正性结论。(21) 的数值不是新无零区域，只是说明一个具体且很小的 geometry 扰动没有立即被 low/floor/intermediate/adaptive 的原始指数账本否决。

## 6. 可直接证明的 principal Euler 解析扩域

这一项不需要假设 AF、零密度或新的无零结论。它从原稿的准确局部恒等式推得，不依赖“每个有限 Euler 因子非零所以无限乘积非零”的错误推断。

3859–3871 定义
\(V=Q^{-6z}\)、\(R=a_p^2Q^{4-6s-6z}\)，所有单位相位模为 1。4034–4039 定义 \(D,W,H_p\)。令 \(\mathcal E_p=P_p^*+D\)，4139–4142 的准确式是

\[
 H_p-1=
 \frac{D(V+W-VW)-VW+(1-V)(1-W)\mathcal E_p}{1-D}.
 \tag{22}
\]

它没有 \((1-W)^{-1}\) 分母。对于 \(p\nmid u\)，4150–4152 的 \(j=0\) 行（在 \(\Re w>0\)）给

\[
 |\mathcal E_p|\ll
 Q^{4-6\sigma-6z_r}+Q^{1-\sigma-w_r-6z_r}.
 \tag{23}
\]

这里可直接核对新域，而非把旧域的结论形式套出域。4015–4025 的 \(j=0\) 准确展开是

\[
 \mathcal E_p=
 \frac{R\{(1-Q^{-1})/(1-V)+W-D\}
 -\eta(p)(Q-1)Q^{-s-w}V/(1-V)}{1-R}.
 \tag{23a}
\]

只要 \(\sigma,w_r,z_r>0\) 且 \(|R|<1\) 有固定余量，(23) 便由这个式子直接得到。后面的新域都满足这些条件。

先在 principal 点 \(u=1,w=1,z=1/6\) 上，由 (22)–(23) 得

\[
 |H_p-1|\ll Q^{3-6\sigma}+Q^{-1-\sigma}+Q^{-2}.
 \tag{24}
\]

所以每个固定 \(\sigma_0>2/3\)，这个实际 \(H_\eta(s)\) 在 \(\Re s\ge\sigma_0\) 正常收敛，并以
\(c_0=\min(6\sigma_0-4,\sigma_0,1)>0\) 给出 prime tail
\(O(P_0^{-c_0})\)。选择固定且与目标单位相位无关的 \(P_0\)，可使

\[
 \sup_{\Re s\ge\sigma_0}|H_\eta(s)-1|\le1/2.
 \tag{25}
\]

故整个乘积也非零。这里加大 \(S\) 只采用原稿 5533–5537 已允许的 coefficientwise 校准操作。

更强地，保留原 principal contour 的 \(w_r\ge19/20,z_r\ge33/200\)，并令

\[
 \sigma\ge\sigma_0>401/600.
 \tag{26}
\]

则 (22) 中 good-prime 的各项模至多是常数乘

\[
 Q^{-\sigma-99/100},\quad Q^{-\sigma-19/20},
 \quad Q^{-97/50},\quad Q^{301/100-6\sigma},
 \quad Q^{-\sigma-47/50}.
 \tag{27}
\]

因此

\[
 H_p-1=O(Q^{-1-c}),\qquad
 c=\min\{6\sigma_0-401/100,\sigma_0-3/50,47/50\}>0.
 \tag{28}
\]

\(1-D,1-V,1-R\) 在此域统一离开 0，因为各相应模严格小于 1；有严格余量，故也有点的开邻域。prime/ideal count 给正常收敛及整个 good tail 的目标一致小量。在原 \(\sigma_0=7/8\) 处，(28) 的最小值是 \(163/200\)，恰好复现 4183–4185 的原尾指数。

对于 \(p\mid u\)，原零延拓使 \(D=W=0\)，故 (22) 化为 \((1-V)\mathcal E_p\)。4015–4031 的完整六行给出统一的衰减指数可取

\[
 r=\min\{\sigma_0-1/20,\ 3\sigma_0-3/2,
 3\sigma_0-21/20,\ 4\sigma_0-2,
 4\sigma_0-31/20,\ 6\sigma_0-3,
 6\sigma_0-301/100\}>0.
 \tag{29}
\]

故 \(H_p-1=O(Q^{-r})\)。\(p\mid u\) 只有有限个，标准 divisor-product bound 给 \(\prod_{p\mid u}|H_p|\ll_\epsilon q_u^\epsilon\)。这个上界不冒称 ramified \(H_p\) 非零；主项 nonvanishing 只在 \(u=1\) 使用。\(\sigma_0=7/8\) 时 (29) 的最小值为 \(33/40\)，与 4174 完全匹配。

9052–9074 的实际 principal slot quotient \(\mathcal B_p=G_p/H_p\) 在此新域亦可定义，因为 principal \(H_p\) 由 (25)/(28) 统一离开零。原准确 error exponents 是

\[
 -\sigma,\quad-6z_r,\quad4-5\sigma-6z_r,
 \quad1-w_r-6z_r.
 \tag{30}
\]

其衰减率为
\(r_B=\min(\sigma_0,99/100,5\sigma_0-301/100,47/50)\)。特别当
\(301/400<\sigma_0\le47/50\) 时可取 \(r_B=\sigma_0\)，并得到

\[
 \mathcal B_p=-1+O(Q^{-\sigma_0}),\quad
 |\rho_i(s)|\ll P_i^{-\sigma_0},\quad
 0<\mu<\sigma_0\min_i\ell_i.
 \tag{31}
\]

这保留原 principal normalization，而只是改变局部余量。\(\sigma_0=69999/80000\) 明确位于这个范围。固定 \(z\)-留数及 \(A_T\asymp(\log Z)^{-K}\) 的真实源因子不需要改变。

因此共享 \(H\) 的旧 \(\Re s>7/8\) 写法不是一个结构性的循环前提；(22) 给出可以本地证明的左侧解析扩域。但是这仍不等于已经验证全部 generalized probe 的闭合估计。

## 7. 与 Weil 路线的具体接口

AF 的正指数/秩证书给的是有限测试空间的高度平均零点信息。要给本稿产生 (5)，应研究与实际 \(u\)-行和短高度 \(T_1\) 匹配的 source-weighted 检测压缩：每个坏行的 witness 是否贡献一个不可被其它行抵消的定量 charge，以及其 prime-side 总量能否给 \(U^{-\eta}\) 的节省。仅有归一化 trace、Hilbert–Schmidt norm 和全局好零比例不足以支付此 charge。

本次 geometry 改善与 AF 比例没有建立这样的桥。它是一条独立的源参数账本路径；不能将其包装成“67.25% 已改善无零边界”。若继续走 hybrid 路线，目标应是 (5)/(6) 的实际行族一致估计，而不是重复提高单函数的平均比例。

## 8. 从本报告到新边界仍需支付的项目

1. **同源可变 geometry 准入。**把 6894–6906 的同一有限补偿 probe、Gaussian annulus、zero mask、ray calibration 和原物理槽窗口，在 \(\ell=1/6+t\) 中准确重跑；不能仅把原固定命题的参数替掉。(13)–(16) 给出应保留的完整 low 成本。
2. **高表示与全局解析接口。**把 5582–5656、6021–6155、6174–6298 中明写 \(\sigma_0\ge7/8\) 的接口重新表述并逐步验收。(22)–(31) 支付了局部 Euler 收敛和 principal 余因子这一部分，不能代替全部 contour joins、完整 correction、外部高度坐标及积分尾的核查。
3. **Detector 统一范围。**确认以已验收 7/8 bootstrap 取 \(\kappa=3/4\) 时，现有 moment、capacity、mesh、amplitude/witness partition 对新源的同一行子集统一；不使用负的旧 \(\Delta\)，不偷偷改成其它字符平均。保留 floor 与全部小/大行范围。
4. **参数顺序及真实 margin。**用 (21) 的小正余量重新分配 moment、bin、rounding、retention、height、\(\zeta\)、principal approximation 等全部成本。每个 height order 必须先固定，\(\tau\) 后选择；有限积分尾只可由同一既有 source expression 控制。
5. **若要使用 AF 的新增贡献。**另证明 (5) 或明确更强的 (6)。本报告没有从 (1) 推出任何 \(\eta>0\)，也没有将另一 \(\xi'\) 比例或角色平均定理转移到此行族。

本报告的确定产出是：比例到行数的逻辑障碍、最小 hybrid 假设、正确的 clipping/geometry/固定留数账本、小有理扰动的有限指数验算，以及从实际局部恒等式证明的 Euler 解析扩域。新无零结论仍须完成上述同源统一验收。
