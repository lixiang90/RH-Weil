# 真 Γ 层的关系、原费用与连续／函数域控制

2026-10-22；独占分支，供 root 消费。只核 root 提出的具体候选，不更新 STATE／cadence。物理源始终 (r=e^{u/2}f)，全部 complex 源；原全线 zero-extension (du)／(D_{\log}) 不换成周期范数。取等价图范数
\(\|r\|_{H_{\log}}^2=(2\pi)^{-1}\int[1+\log(2+|t|)]|\hat r(t)|^2dt\)，其域正是原 (D_{\log})；下文常数1针对这个明确规范。以下标准消费与新候选的增量由 root 统一结算。

## 1. 固定对象与候选

令
\[
 W_\zeta=W_\Gamma+M,\qquad
 M=2\cosh(u/2)\,du-
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
       (\delta_{\log n}+\delta_{-\log n}).                 \tag{1}
\]
\(\Lambda(n)\) 是全部素数幂，完整 Γ 包含指定 contact，完整双极点已在 (2\cosh(u/2)) 内。Fourier 约定为 \(\hat r(t)=\int r(u)e^{-itu}du\)，
\[
 Q_{W_\Gamma}(r)=(2\pi)^{-1}\int\Gamma(t)|\hat r(t)|^2dt,
 \quad \Gamma(t)=\Re\psi(1/4+it/2)-\log\pi
               =\log|t|+O(1).
\]

取实偶 (\phi\in C_c^\infty\) 为 normalized autocorrelation，(\phi(0)=1)、\(\operatorname{supp}\phi\subset[-1,1]\)，令 (\phi_R(u)=\phi(u/R))，支撑为 ([-R,R])。可从支撑在 ([-1/2,1/2]) 的非负实 bump 的自相关选取，因而同时有 (0\le\phi\le1)、正型；以下费用只需实偶、(\phi(0)=1) 及有界二阶导数。fixed 原源窗仍以 ([-L,L]) 标记。定义
\[
 V_R^0=W_\Gamma+\phi_RM,\qquad
 a_R(t)=\Gamma(t)+\widehat{\phi_RM}(t),\qquad
 c_R=(-\inf_{t\in\mathbb R}a_R(t))_+,\quad
 V_R=V_R^0+c_R\delta_0.                                  \tag{2}
\]
因为 \(\phi_RM\) 是 compact finite measure，其 Fourier 变换有界且实偶；(a_R(t)\to+\infty)，故下确界有限、可在某个有限区间达到。(c_R\ge0) 的定义不读任何未知零点。它给正型层 (V_R)，但 (c_R\to0) 尚未付款。正层存在与缺陷消失必须分开。

## 2. 405 的实际关系：不是 compact 交集的空测试

405 给实际 adele 限制关系
\[
 p=(D^2+D)h\in P_{\rm an},\qquad r_p=e^{u/2}p
   =(D^2-1/4)H,\quad H=e^{u/2}h>0,
\]
其中 (p,r_p\in S_{\exp}\) 均非 compact。其完整变换为
\[
 \hat r_p(t)=s(s-1)\xi(s)/2,\qquad s=1/2-it.              \tag{3}
\]
全部平移仍是实际解析关系，且双 pole 矩严格为零。由完整显式公式，不用 RH，目标满足
\[
 B_\zeta(r_p,s)=0\quad(s\in S_{\exp,\mathbb C}),
 \qquad Q_\zeta(r_p)=0.                                  \tag{4}
\]
405 的 (h) 有双 degree (1/4,1/4)，不能把整个像 (I) 当成同时保双 degree 的 (P_{\rm an})。本分支不认证这些解析关系为几何 principal。

553 已证明 (I\cap C_c^\infty=0)，且 
\(\operatorname{span}\{\tau_a r_p:a\in\mathbb R\}\) 在原全线 (du) 和 (H_{\log}) 都稠密。因此只检验“compact 主关系”没有内容；一个全域 bounded 原范数源映射若精确消掉全部这些平移，就全零，失去537非根。换一个随 R 增长的全域有限 bound 并不避开该逻辑。合法逃逸是 varying compact domain、(S_{\exp}) 更强拓扑，或明确付费的 cofinal／source-adapted family。

### 2.1 每个 (2) 都不可能精确消去非零 405 关系

在 (2) 中，(a_R(t)+c_R\ge0)，并在所有充分大的 (|t|) 严格为正。(r_p\ne0)，其整个 Fourier 变换不恒零，实零集离散；故
\[
 Q_{V_R}(r_p)=(2\pi)^{-1}\int(a_R+c_R)|\hat r_p|^2dt>0.   \tag{5}
\]
同样适用于任一非零 (S_{\exp}) 源。于是“每层保真 Γ＋compact Radon 修正＋有限 (\delta_0) 补偿”可给严格正层，却不能给逐层 source-exact 的405商。此结论只排这个层类型的逐层 exact 要求，不排 D′ 正逼近。

更一般，若正谱证书满足 (Q_j(r)=\int|\hat r|^2d\sigma_j)，且精确 (Q_j(r_p)=0)，则
\[
 \operatorname{supp}\sigma_j\subset\{t:\hat r_p(t)=0\}
   =\{t:\xi(1/2-it)=0\}.                                 \tag{6}
\]
这把实际 critical-line 零标签重新放入谱支持约束。它不单独证明所有零点在这条线上，也不迫使所有这些点均有谱质量；完整 trace／重数身份还要另付。其正确用途是标明：不能一边用连续正密度保 Γ 主项，一边宣称已经精确消去405。

### 2.2 全线 normalized 主关系与逐个固定关系不同

任一固定 R 的 (V_R) 及下面 (\widetilde V_R) 都在原全线 (H_{\log}) 上给 bounded 正 form：Γ 仅为 log-growth，compact measure 和 smooth spectral correction 则是 (du)-bounded。另一方面，对固定非零 compact (\eta)，高频 (r_t=e^{itu}\eta) 给
\[
 \frac{Q_{V_R}(r_t)}{\|r_t\|_{H_{\log}}^2}\to1,
 \qquad
 \frac{Q_{\widetilde V_R}(r_t)}{\|r_t\|_{H_{\log}}^2}\to1.
\]
由553的真实 (P_{\rm an}) 全线 (H_{\log}) 稠密性及各层 form 连续性，对每个固定 R 有
\[
 \sup_{0\ne p\in C(P_{\rm an})}
 \frac{Q_{V_R}(p)}{\|p\|_{H_{\log}}^2}\ge1,\qquad
 \sup_{0\ne p\in C(P_{\rm an})}
 \frac{Q_{\widetilde V_R}(p)}{\|p\|_{H_{\log}}^2}\ge1.     \tag{6a}
\]
其中 (C(P_{\rm an})=e^{u/2}P_{\rm an}) 是实际物理关系空间，而非任意 raw 源。每个高频 compact 测试可先在 (H_{\log}) 用有限个真实平移关系逼近，再令频率增长。原全线 (du) 上相应 supremum 甚至无限，因各层 Γ 的 log 高频主项不 bounded。这是旧553与本层真 Γ 的直接消费，不是新的 classic 负性／容量结论。

因此，哪怕最终逐个固定 (p) 的费用都趋0，也绝不意味着全部 normalized noncompact 主关系的统一费用趋0；(6a) 与 fixed compact 窗的 (9) 不矛盾，compact 窗没有非零完整主关系。它不排付更强指数半范数、growing domain 或实际 source-adapted 费用。

## 3. 不抹平 Γ 后，原 (du/D_{\log}) 误差可以逐窗付清

实偶性给 (\phi'(0)=0)。存在有限 (C_\phi) 使
\[
 |1-\phi_R(u)|\le C_\phi u^2/R^2\qquad(u\in\mathbb R).   \tag{7}
\]
固定原源窗 ([-L,L])，设
\[
 T_L=8\sinh L+2\sum_{2\le n\le e^{2L}}
             \frac{\Lambda(n)}{\sqrt n},\qquad
 \delta_{R,L}=C_\phi(2L)^2T_L/R^2.                        \tag{8}
\]
由 \(\|r*s^*\|_\infty\le\|r\|_2\|s\|_2\) 和 
\(|M|([-2L,2L])\le T_L\)，对全部 complex 窗源有
\[
 |B_{V_R^0-W_\zeta}(r,s)|
 \le\delta_{R,L}\|r\|_2\|s\|_2.                          \tag{9}
\]
Γ 的奇性与 contact 在此精确相消，未作有限高度截断；所有本窗会实际出现的素数幂均保留。端点上自相关为零与否可按原源域处理，不以删项改公式。

因此
\[
 |Q_{V_R-W_\zeta}(r)|
 \le(c_R+\delta_{R,L})\|r\|_2^2
 \le(c_R+\delta_{R,L})\|r\|_{H_{\log}}^2.                 \tag{10}
\]
这绕过576逐层 Radon 的高频 obstruction：本层真 Γ 没被有限测度替代。它并未证明 (c_R\to0)。裸 signed 层 (V_R^0\to W_\zeta) 在每个 fixed 窗的原 (du)-bounded perturbation norm 收敛，是独立成立的；其是否正型承担剩余责任。

采用旧555已付的 Chebyshev 部分求和预算 
\(\sum_{n\le x}\Lambda(n)/\sqrt n\ll\sqrt x\)，有 (T_L\ll e^L)；不以较弱的 \(\Lambda(n)\le\log n\) 逐项界作为新前沿。从而成长窗上足够条件为
\[
 L^2e^L/R^2\to0\quad\text{及}\quad c_R\to0.              \tag{11}
\]
这只是给定 recipe 的充分上界，不是必要原源费用，也不代表最大可达成长率。没有 (11) 或更强实际 cancellation，不把 fixed-L 结论写成全源／全尺度统一小误差。

### 3.1 全 (S_{\exp}) 的逐源关系误差

取 (N>1/2)。(M) 的加权二阶矩
\[
 A_N=\int u^2e^{-N|u|}\,d|M|(u)<\infty
\]
由 pole 指数增长及 
\(\sum\Lambda(n)(\log n)^2n^{-N-1/2}<\infty\) 得到。若 (h=r*s^*\in S_{\exp})，则 (7) 直接给
\[
 |(V_R^0-W_\zeta)(h)|
 \le C_\phi A_NR^{-2}\sup_u e^{N|u|}|h(u)|.              \tag{12}
\]
卷积半范数可由 (r,s) 的固定更强指数半范数控制。因此这不是仅靠 D′ 猜出的 noncompact 尾；(12) 实际支付每个 (S_{\exp}) 源及固定半范数有界族。对405特别有
\[
 Q_{V_R}(r_p)=c_R\|r_p\|_2^2+O_{r_p,\phi}(R^{-2}).       \tag{13}
\]
若 (c_R\to0)，近似消去全 (P_{\rm an}) 中每个固定关系及每个固定平移成立。全部平移量 (a\to\infty) 的指数半范数增长须另付；(12) 不给原全线 (du/H_{\log}) 统一关系商。

因为 (V_R^0\to W_\zeta) 已在 D′ 成立，(V_R\to W_\zeta) 于 D′ 当且仅当 (c_R\to0)。其必要性只需取一个 (h(0)\ne0) 的 compact 测试；充分性由 (7)。若这一缺陷消失独立获证，正锥闭给完整 Weil 正性。反向是否对这个特定 cutoff family 自动成立，由 root 的完整 budget 分支核验；本分支不假设它。

### 3.2 更强的 contact-preserving smooth 修补

scalar (c_R\delta_0) 只是上界模型，会改变原 contact；不能把它说成固定经典完成化的逐层对象。root 提出的较强修补是
\[
 q_R(t)=(a_R(t))_-\ge0,\qquad
 K_R(u)=(2\pi)^{-1}\int e^{itu}q_R(t)dt,\qquad
 \widetilde V_R=V_R^0+K_R(u)du.                           \tag{13a}
\]
由于 (a_R\to+\infty)，(q_R) 连续且 compact supported。它不必 (C^\infty)，但 compact (L^1) 已使 (K_R) 为 entire smooth 函数（每阶导数由有限频率矩控制）。因此原 Γ 穿孔核和 contact 均原样保留；新增的是 smooth 全局 correction。谱密度恰为 ((a_R)_+\ge0)。这是一种真实更强的正层，不能因 scalar 修补改变 contact 就一起排掉。

对原全线 (du) 源及 fixed 窗源分别有
\[
 Q_{K_R}(r)=(2\pi)^{-1}\int q_R|\hat r|^2dt
 \le c_R\|r\|_2^2,
\]
\[
 0\le Q_{K_R}(r)\le\kappa_{R,L}\|r\|_2^2,\qquad
 \kappa_{R,L}=\min\{c_R,(L/\pi)\|q_R\|_1\},
 \quad\operatorname{supp}r\subset[-L,L].                 \tag{13b}
\]
第二式来自 \(|\hat r(t)|^2\le2L\|r\|_2^2\)；两式都没有误加 (1/(2\pi)) 到 Plancherel 后的 (c_R\) 系数。cross 费用由正 form 的 Cauchy–Schwarz 支付。用 (13b) 代替 (10) 中的 (c_R)，可得 (\widetilde V_R-W_\zeta) 的 fixed 窗 (du/D_{\log}) bound (\delta_{R,L}+\kappa_{R,L})。对 noncompact 固定 (r\in S_{\exp})，亦可用
\[
 Q_{K_R}(r)\le\min\{c_R\|r\|_2^2,
       (2\pi)^{-1}\|q_R\|_1\|r\|_1^2\}.                \tag{13c}
\]

对一般这种 smooth 修补，单从拓扑出发 (c_R\to0) 只是充分条件，不能当作 D′ 收敛的必要条件；当前特定 family 的额外等价见下段。
\(\|q_R\|_1\to0\) 也是足够条件；更一般应检验实际原源费用 
\((2\pi)^{-1}\int q_R|\hat r|^2\to0\) 或直接 (K_R\to0) 的完整分布 pairing，不把频谱负峰的高度、总质量及逐源加权质量混为一谈。负质量可能集中／逃到高频，其 fixed 窗 (H_{\log}) 价格还可能较小，必须在实际源上计算，不能从全空间 (c_R) 下界直接声称本源费用。

每层 \((a_R)_+\) 在高频严格为正，(5) 的同一论证给 
\(Q_{\widetilde V_R}(r_p)>0\)。但若 correction 在原逐源费用上趋0，则
\[
 Q_{\widetilde V_R}(r_p)=Q_{K_R}(r_p)+O_{r_p,\phi}(R^{-2})\to0.
\]
这清楚区分真 Γ／contact 保留、逐层 exact 关系与极限近似关系。若 (K_R\to0) 于 D′ 独立获证，正锥闭仍能传完整 Weil 正性；这一缺陷的独立 budget 不是由 spectral clipping 本身支付。

**具体 family 的额外链，交 root 合并后消费。**以上“不是必要条件”指一般正密度 smooth 修补，不是断言当前特定 family 不可能另证等价。root 的独占 Γ budget 分支正在核另一条身份：
\[
 V_R^0=\phi_RW_\zeta-\nu_R,\quad
 \nu_R=(1-\phi_R)\frac{e^{-|u|/2}}{1-e^{-2|u|}}\,du,
\]
以及 \(\|\nu_R\|_{\rm TV},\|\widehat\nu_R\|_1=O(R^{-2})\)。若此完整 identity／contact／二阶 TV 费用被 root 验收，在 **RH 前件** 下正型 \(\phi_RW_\zeta\) 可推出 
\(c_R,\|q_R\|_1=O(R^{-2})\)。反向 (K_R\to0\) 于 D′ 通过完整正锥闭推出 RH。这样才可为这个特定 family 得到 
\(K_R\to0\) 于 D′、(c_R\to0\)、(\|q_R\|_1\to0\)、RH 之间的等价；必要性来自额外 target identity，不是来自“D′ 控制 supremum”这一错误一般原则。本分支未独立重审该二阶 TV bound，不以它支付无条件缺陷消失。

## 4. 537 非根保留，但它不能支付成长缺陷

537 给同一实际 (Q_\zeta) 在半窗 (L_0=17/16) 上
\[
 Q_\zeta(r)\ge\tau\|r\|_2^2,
 \qquad\tau=2^{-49162},
\]
适用于全部 complex 原 (D_{\log}) 窗域。取实际非根
\(r_0=(D^2-1/4)\psi\ne0\) 于此窗，双 pole 矩零。由 (9)，
\[
 Q_{V_R}(r_0)\ge(\tau+c_R-\delta_{R,L_0})\|r_0\|_2^2>0
\]
最终成立，而且可对同窗所有源一起成立。这是原范数的非根检验；无需借未知零点，也无需先证明 (c_R\to0)。但它只付一个已知固定窗，不能反推所有 R 的全谱密度或成长窗正性。未知 (c_R) 可能来自越来越大的源窗／pole 区域。

对 smooth 修补，正 (K_R) 同样给
\(Q_{\widetilde V_R}(r_0)\ge(\tau-\delta_{R,L_0})\|r_0\|_2^2>0\)；它也不提供未知 correction 的上界。

## 5. 连续正反例：同一修补必须保留缺陷差别

采用562／563真正正 primitive、全部 Euler powers、双 pole 的连续族，native Γ 为0。

### 5.1 正段

对 (c=5/16)，完整平衡先由源公式相消给
\[
 W_+(u)=2\cos(u/4)\,du.
\]
实际整个模型的 (2) 变成 (V_R^0=\phi_RW_+)。正型分布的乘积仍正型；更具体，Fourier 密度为
\[
 \widehat{\phi_RW_+}(t)
   =\hat\phi_R(t-1/4)+\hat\phi_R(t+1/4)\ge0.
\]
所以 (c_R=0) 对所有 R，完整正逼近及 fixed 窗原 (du/D_{\log}) 费用独立成立。它的每层连续谱也通常不精确消去极限的非零 relation：例如 
\((D^2+1/16)\eta\) 在极限正型中为零，却在连续密度层有正范数。这说明逐层关系失败不应被误当 D′ 逼近失败。

### 5.2 负段

对 (c=3/16)，同样的实际全源相消给
\[
 W_-(u)=2\cosh(u/4)\,du.
\]
取实偶非负非零小支撑 (\eta\)，
\(r_1=(D^2-1/4)\eta\)，(r_2=\tau_h r_1\)（(h>0)）；二者双 pole 矩严格为零。令 
\(A=\int\eta(u)\cosh(u/4)du>0\)、(d=3/16\)。完整 Gram 为
\[
 2d^2A^2
 \begin{pmatrix}1&\cosh(h/4)\\\cosh(h/4)&1\end{pmatrix}.
\]
故 (r_-=r_1-r_2) 有 
\[
 Q_-(r_-)=4d^2A^2(1-\cosh(h/4))<0.                       \tag{14}
\]
这个负测试是 compact、双 pole-zero 的原物理源，不是全空间范数反测。任何修补后的正层均要求
\[
 c_R\ge-\frac{Q_{\phi_RW_-}(r_-)}{\|r_-\|_2^2},\qquad
 \liminf_{R\to\infty}c_R\ge
 \frac{4d^2A^2(\cosh(h/4)-1)}{\|r_-\|_2^2}>0.            \tag{15}
\]
所以此 recipe 不能从正 primitive／全 powers／裸对偶自动得到缺陷消失。有限 R 补偿当然能造正层；其正性不能代替逼近原负目标。正反两段均保原双 pole 后再相消，未通过删除 poles 制造差别。

同一 compact 负见证对更强 smooth 修补给
\[
 Q_{K_R}(r_-)\ge-Q_{\phi_RW_-}(r_-),\qquad
 \liminf_R Q_{K_R}(r_-)\ge-Q_-(r_-)>0.                   \tag{15a}
\]
所以在这个实际源上 correction 不能消失，且它也不可能 D′ 趋0。这里排的是实际源费用而非只引用 \(\|q_R\|_\infty\) 的全空间下界。正段和函数域的 (q_R=0) 则使两种修补都精确无费。

## 6. 真函数域：全部 period aliases 给 (c_R=0)

取已付真实曲线 (E/\mathbb F_5:y^2=x^3+x+1)，(\ell=\log5)，全点数递推与正能量矩阵给
\[
 W_E=\ell\sum_{n\in\mathbb Z}a_n\delta_{n\ell},
 \quad a_n=\operatorname{Tr}U^n,\quad a_0=2,
 \quad U^*HU=H>0.                                      \tag{16}
\]
这是包含所有 periodic poles／returns／prime powers 后的完整对象，且 
\(\hat W_E=2\pi\sigma_E\) 为全部实线 aliases 的正谱。native conductor／contact 是原点质量，(\phi_R(0)=1)，故保原 contact、只 window 其余完整 signed 平衡，与直接 (\phi_RW_E) 相同。由正型乘积，
\[
 V_{E,R}^0=\phi_RW_E\ge_{\rm type}0,\qquad c_{E,R}=0.     \tag{17}
\]
Fourier 一侧是 (\sigma_E\) 与非负 Schwartz 核卷积，必须保每条 alias，不能只算一个 fundamental interval。由于 (|a_n|\le2)，full (W_E) 在任一 fixed 窗的 TV 有线性窗包络；(7) 给完整 fixed 窗原 (du/D_{\log}) 误差 (O_L(R^{-2}))。这里用的是已付全递推后的真实 cancellation；分别估 H／P 的指数 TV 会给较粗但合法上界。

函数域存在独立同对象 RR／正 H 证书，才可无条件给 (17)。这个正例说明 cutoff recipe 没破坏已有独立正性，不说明经典缺陷也会消失。原全线范数仍不能按 fixed 窗结论统一：极限谱有 Dirac 原子，某个原子上的 Fourier 读出对全线 (du/H_{\log}) 不 bounded。让源支撑成长可检出此费用。把源周期化或改 norm 会换掉原任务。

## 7. 净结论和停止条件

具体增量接口是：每层真 Γ 可避免576的逐层 Radon 高频门，且裸 signed 层有 (9)／(12) 的原费用；独立选择的 smooth 补偿 (13a) 总能造正层并精确保原 contact。405 明确迫使这些连续谱层只有近似关系，537 在固定窗可见。continuous± 与真 FF 正好分别检验 correction 为零、实际负源上的 correction 不消失、全 aliases 下 correction 为零。

剩余关键输入仍是从经典 full Γ/contact、全部 Λ(p^k)、双 pole 同源预算独立证明实际 correction 消失，例如 smooth 修补的 (K_R\to0\) 于 D′，或更强 (\kappa_{R,L}\to0\)／(c_R\to0\)（或另一个实际非负 coefficient recipe 的完整 signed 误差）。这些条件强弱不可混写。仅把这个极限写成“capacity”“正层存在”“自然完成化”不支付它。全源统一 norm、D′ 收敛、每个固定 (S_{\exp}) 关系及逐层 exact 几何商是四种不同要求。若当前只能重述未知缺陷消失，停止此 recipe 的扩大，不继续调 cutoff／contact 或用未知零点选非负权。

最强旧 whole 结论仍542＋555→557的 leading4/5负惯性上预算；本分支不提供 actual 成长 core／coupling／Ξ 或独立算术 RR 容量。
