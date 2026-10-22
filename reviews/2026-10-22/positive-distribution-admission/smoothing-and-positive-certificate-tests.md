# 完整正分布逼近的准入：Gaussian、正型乘窗与有限原子证书

2026-10-22。独占来源／候选检验，不改 STATE 或自行计轮。输入为上一轮固定纤维路线及 405、537、553、562–566；§1–7 是标准运算及旧分离论证的具体消费。执行中另收到实际函数域 basechange／dilation 家族，§8 对其补付全部固定窗原 Hlog 源的 alias 费用；这不是经典 RH 新证明。

## 1. 要逼近的对象和最便宜的有效证书

固定 Fourier 约定 \(\widehat r(t)=\int r(u)e^{-itu}du\)，\(r^*(u)=\overline{r(-u)}\)。目标是同一个完整 \(W_\zeta\)，而非 prime 项或 Γ 项单独的近似。令 \(\Gamma(t)=\Re\psi(1/4+it/2)-\log\pi=2\theta'(t)\)，\(a_n=\Lambda(n)/\sqrt n\)，则对 compact 测试 \(h\)
\[
 W_\zeta(h)=\int 2\cosh(u/2)h(u)du
 +\frac1{2\pi}\int\Gamma(t)\widehat h(t)dt
 -\sum_{n\ge2}a_n\{h(\log n)+h(-\log n)\}.                 \tag{1}
\]
这是 562–566 的完整线性平衡；Γ 的 Fourier 配对包含既定 finite part/contact，求和保 \(n=p^k\) 的每个 k，第一项保两极点。非偶 complex h 也按本式消费。

最简独立正分布证书为实际给定的实数 \(t_{jk}\) 和非负实数 \(a_{jk}\)：
\[
 \sigma_j=\sum_{k=1}^{m_j}a_{jk}\delta_{t_{jk}},\qquad
 V_j(u)=\sum_{k=1}^{m_j}a_{jk}e^{-it_{jk}u}.                \tag{2}
\]
于是 \(V_j(r*r^*)=\sum a_{jk}|\widehat r(t_{jk})|^2\ge0\)，符号不借零点位置。可用有限维自伴矩阵及正向量写同一证书；其普通 trace 重数与此向量谱质量仍是不同数据。若要求实偶目标，可以对 \(\sigma_j\) 关于 t↦−t 对称化。

真正的准入门是从原数据、且不从未知正性挑选参数，证明
\[
 \sum_k a_{jk}\widehat h(t_{jk})\longrightarrow W_\zeta(h)
 \quad(\forall h\in C_c^\infty(\mathbb R)),                 \tag{3}
\]
或给覆盖所有源的已付双侧误差。逐 h 的 (3) 就足够传正性，无需先构造极限 scheme 或普通 determinant。独立正测度已有时，截断和正求积确可产生 (2)；对未知正性的 W 直接声称“取其正谱求积”则循环。

如果只在可数测试上证明收敛，还须给共同分布阶／局部连续上界才能延到全部测试。例：统一
\(\int(1+t^2)^{-M}d\sigma_j(t)\le C\)
提供 \(|V_j(h)|\le C\sup_t(1+t^2)^M|\widehat h(t)|\) 的连续性。它不是自动获得的原 du／Dlog 容量，也不自动给 ordinary trace 的重数或热迹尾紧。

## 2. 两种 Gaussian 操作不能混同

取 \(k_s(u)=(4\pi s)^{-1/2}e^{-u^2/(4s)}\)，s>0。

**卷积平滑**为 \(W_s=W*k_s\)。在有限指数阶域，Gaussian 尾支付非 compact 配对，并有
\[
 Q_{W_s}(r)=Q_W(k_{s/2}*r).                                \tag{4}
\]
它把已有正性传到平滑对象；并不使一个未知 signed W 自动正。对完整经典对象，(1) 精确给
\[
\begin{aligned}
 W_{\zeta,s}(v)={}&2e^{s/4}\cosh(v/2)
 +\frac1{2\pi}\int e^{-st^2}\Gamma(t)e^{itv}dt\\
 &-\sum_{n\ge2}a_n\{k_s(v-\log n)+k_s(v+\log n)\}.         \tag{5}
\end{aligned}
\]
每个固定 s、compact v 及有限阶导数的尾由 Gaussian 和 \(\Lambda(n)\le\log n\) 控制。(5) 已使 Γ 奇性及 prime atoms 光滑，却没有给它的正型证书。尤其不能删第一项或把负 prime 波包改成正 jump。

**正型乘窗**为 \(\widetilde W_\varepsilon=e^{-\varepsilon u^2}W\)。如果 W 已正型，乘窗由 Schur 乘积／正谱卷积保正。这个方向不能倒用；它和 (4) 不是同一操作。乘窗改变 pole 项及每个 \(a_n\) 为 \(a_ne^{-\varepsilon(\log n)^2}\)，并使 Γ 的完整 distribution 同乘该窗；保留 φ(0)=1 不意味着 Γ 的 finite part 未变。

更一般的 smooth compact 正型窗可由非负 \(\eta\in C_c^\infty\) 的自相关缩放、按 φ_R(0)=1 归一化得到，且 φ_R→1 于每个 compact 的全部导数。若所有 cofinal R 的 \(\phi_RW\) 已独立正型，则闭锥给 W 正型；“有这样的全尺度正窗证书”目前仍承担全部正性责任。

这些操作通常不自动给一个新的正 g-prime 系统。比如仅把 primitive 权重乘 m(u)，其第 k 幂权重是 m(u)，而 Gaussian 乘窗要求 m(ku)=\(e^{-\varepsilon k^2u^2}\)；k=1 已固定 m，k=2 一般矛盾。可以另作 Möbius 反演或换证书类型，但 primitive 非负性及完成化身份须重证。作为纯正分布证书不要求中间对象是 g-system；不能把这项选择说成已得到自然 g-system 对偶。

## 3. 连续负例给出两个实际比较

562 的真正正 primitive／integer 连续族保 Γ=0、全部 powers 和双 pole，完整负段为
\(W_-(u)=2\cosh(a u)\)，例如 a=1/4。则
\[
 (W_-*k_s)(u)=2e^{sa^2}\cosh(a u).                         \tag{6}
\]
离线指数没有消失；任意 s>0 的平滑对象仍失败完整正性。取旧双 pole-zero 源 \(r_1=(D^2-1/4)\eta\)、\(r_2=\tau_hr_1\)，\(\eta\ge0\) 偶且 compact，其 2×2 Gram 只是旧 (15) 乘正数 \(e^{sa^2}\)，h≠0 时 determinant 仍负。

Gaussian 乘窗也不能救此族：普通 Fourier 变换精确为
\[
 \widehat{\,2e^{-\varepsilon u^2}\cosh(a u)\,}(t)
 =2\sqrt{\pi/\varepsilon}\,
   e^{(a^2-t^2)/(4\varepsilon)}
       \cos\!\left(\frac{at}{2\varepsilon}\right).          \tag{7}
\]
每个 ε>0 都有正负区间，所以该平滑实偶 Schwartz 核非正型。这是同一个正 g-system 负对照，不把“smooth／Gaussian／正 primitive”当正性的来源。

另一方面，不能从 (7) 推广成“所有 signed 核在每个固定 Gaussian 尺度都失败”。实际 bounded signed 控制为
\(V(u)=2\cos u-1\)，其谱是 \(\delta_{-1}+\delta_1-\delta_0\)，原 V 非正型。但
\[
 \widehat{e^{-\varepsilon u^2}V(u)}(t)
 =\sqrt{\pi/\varepsilon}\,e^{-t^2/(4\varepsilon)}
  \{2e^{-1/(4\varepsilon)}\cosh(t/(2\varepsilon))-1\}
                                                               \tag{8}
\]
在 \(\varepsilon\ge1/(4\log2)\) 全非负。故**粗尺度正型乘窗可以掩盖负谱**；它不可能沿 ε↓0 一直正型，因为正锥闭。此控制只检验滤波逻辑，不冒称 V 来自 562 的 positive primitive 类。

连续正段 \(W_+(u)=2\cos(\tau u)\) 则在 (4) 得 \(2e^{-s\tau^2}\cos(\tau u)\)，乘窗 Fourier 为两个正 Gaussian。正、负段因同源参数阈值 d=c−1/4 的独立证书区分；不是平滑本身区分了符号。

## 4. 固定热平滑在整个阶／完整除子类里也没有免费弱化

在 562 §3 的同一整个阶≤1、竖带、完整反射除子类，固定 s>0 后，要求 \(W*k_s\) 对**全部源**正型仍与原 Weil 正性等强。正向由 (4)。反向若有离线 pair，旧分离证明用
\(F(z)=e^{b z^2}G(z)L(z)\)
隔离该 pair 并给负二次值；其中 b>0 可任取，G 为清除该 pair 后的整个因子，线性 L 独立插值所需两值。取 b>s/2，则
\(e^{-(s/2)z^2}F(z)\)
仍在每条固定竖带 Gaussian 下降，其逆变换 r∈S_exp，且 \(F\) 是 \(k_{s/2}*r\) 的中心 Laplace 变换。于是 (4) 给负值。连续性和 compact 截断再给 compact 负源。

这里 z 是中心 Laplace 变量，热乘子 \(e^{(s/2)z^2}\) 在实 Fourier 线上才是 \(e^{-(s/2)t^2}\)。不得把它在离线指数处误当零；Gaussian 整函数从不为零。该反向是旧 562 分离法在合法热像上的直接应用，**不是从原数据证明正性的新输入**。它不声明任意分布的任意固定滤波都可逆保正，(8) 已说明另一操作的反例。

## 5. 函数域通过的是独立 unitary 证书，不是滤波魔法

旧 563／566 的真 \(E/\mathbb F_5:y^2=x^3+x+1\) 由点数、RR 有理性及全递推给
\[
 F=\begin{pmatrix}0&-5\\1&-3\end{pmatrix},\quad
 H=\begin{pmatrix}1&-3/2\\-3/2&5\end{pmatrix}>0,
 \quad F^THF=5H.
\]
令 U=F/√5、L=log5，完整 \(W_E=L\sum_{n\in\mathbb Z}\operatorname{Tr}(U^n)\delta_{nL}\) 已有全周期平方和。以 H-inner-product 的 unitary 特征相位为 \(e^{i\theta_\ell}\)，其正实线谱为
\[
 \sigma_E=\sum_{\ell=1}^{2}\sum_{m\in\mathbb Z}
     \delta_{(\theta_\ell+2\pi m)/L}.                       \tag{9}
\]
符号及所有 n 来自先前 H 和全递推，不由先假设相位实。有限频率截断 (9) 给实际 (2)，对 compact 测试的 Schwartz Fourier 尾给 (3)。Gaussian 热平滑只是再乘非负 \(e^{-st^2}\) 谱权；正型乘窗只是与正 Gaussian 测度卷积。全部周期 pole 及 aliases 仍由原完整 W 身份保存。

式 (9) 没有额外 2π：\(\sum_m e^{2\pi imu/L}=L\sum_n\delta_{nL}\)。本例相位多重集关于取负对称，故两种指数符号给同一 W，且 \(\widehat W_E=2\pi\sigma_E\)；不把 Fourier transform measure 与 (2) 的表示 measure 混同。有限 unitary 证书在频率圆周有限，在实线上必须保无限 aliases；只保一个 strip 不足。

## 6. 原 du／Dlog、405 全关系及 537 的运输

对有限原子证书，物理源映射为
\(J_jr=(\sqrt{a_{jk}}\widehat r(t_{jk}))_k\)。对 \(\operatorname{supp}r\subset[-L,L]\)
\[
 \|J_jr\|^2\le2L\Big(\sum_k a_{jk}\Big)\|r\|_{du}^2.      \tag{11}
\]
L≥1 时旧 553 单点评价 Hlog 费另给粗 upper
\(C L\sum_k a_{jk}/[1+\log(2+|t_{jk}|)]\)。它是逐坐标相加的充分上界，**不是**共同 Gram 的必要下界；全高度最优共同费用须另算。完整 Γ 的原 Hlog／zero-extension Dlog 费不能被某个有限 j 的 (11) 永久替掉。热源平滑在原全线 du 和 Hlog 上都是 contraction，但输出非 compact，因此不能直接套固定支撑的 537 窗定理或原 C_L 窗费。

若要求每个有限证书精确消去405实际 \(r_p\) 及全平移，则
\[
 0=\|J_jr_p\|^2=\sum_k a_{jk}|\widehat r_p(t_{jk})|^2,
 \qquad a_{jk}>0\Rightarrow\widehat r_p(t_{jk})=0.           \tag{12}
\]
而旧 405／553 已给 \(\widehat r_p(t)=s(s-1)\xi(s)/2\)，s=1/2−it。故**逐层精确 annihilation 把原子频率强制放到实际临界线零坐标**。按这些坐标选原子可有合法部分正谱，但已是旧谱商／坐标证书；尚无完整目标收敛，不能算独立算术来源。全 Pan 还要求全部必要 jets 等关系，(12) 仅是最便宜必要门。

若只要求 D′ 完整逼近，compact 源的正性已够 Weil 判据；不必逐层精确消 Pan。可是405是实际 noncompact S_exp 关系，D′ 收敛**不自动**给 \(Q_{V_j}(r_p)\to0\)，更不能宣称已有实际 source quotient map。需另付 S_exp 测试尾或明确只在 compact 域作存在性证明。553 的全线 bounded 消 Pan⇒零结论也不能套到仅窗上有费的 (11)。

537 的明确 compact r0 满足 \(Q_\zeta(r_0)>0\)。若 (3) 真已付，\(\|J_jr_0\|^2\to Q_\zeta(r_0)>0\)，故最终保留非根；若先给任意有限原子，则必须实际检查，不能由“a≥0”保证 r0 可见。热平滑保持 Pan 零 jets／pole 矩，因为 Mellin 变换只乘无零 Gaussian；它也保留553 cyclic density的旧障碍，不制造 globally bounded 非零关系商。

## 7. 频率裁剪及停止决定

有限频率裁剪从已知 \(\sigma\ge0\) 得正证书，是合法后处理。对未知 W，没有正谱测度前不能直接做这个操作。先用 physical Gaussian 乘窗使 Fourier 有合法 signed 函数，再取其正部，也能人为制造正分布；此时必须控制被删除负部对**所有** \(\widehat{r*r^*}\) 的贡献趋零。该负部消失正是所欠的完整比较，不能按定义置零。Γ 的高频余量也不能只在有限头里计算后忽略全部补空间；537 的成功依赖真实非有限秩 tail，而非有限 PSD 本身。

本候选门的具体信息差是：(6)–(7) 在实际 continuous 负 g-system 上拒绝两种 Gaussian 自动正性，(8) 又排除了从固定粗乘窗反推目标的错误方向；(12) 给出逐层精确消405时不可隐去的谱标签责任。因而不应启动“先平滑再任取有限正谱”合同。

目前没有从经典 prime／Gamma／pole 独立产出 (2)–(3) 的参数或带费用误差。仅自动平滑、正部裁剪、取未知谱求积、全尺度未知 Gram 可行性在本门停止，不扩 ε、频率或网格。可改变这个决定的输入是：**一项源侧、带完整误差和共同原费用的正原子／unitary 构造**，或可独立支付的正余量＋完整 signed 残差支配。保其他非局部、变域、几何和无限维能量证书；本门不排它们。尤其下面实际 unitary lattice 的新费用不在此停域。强旧 542＋555→557 whole leading4/5负惯性上预算、成长 core／coupling／Ξ 与独立容量瓶颈均未改变。

## 8. 实际 unitary lattice 的新 all-source 原费：alias 尾恰为 1/log

这是执行期间收到实际函数域 basechange／dilation 家族后的补核。其几何合法性及其从真曲线的构造由另稿负责；本节独立核物理分布及原范数，不从未知 ζ 谱选点。固定实 γ，令 Δ=2π/h，
\[
 W_{h,\gamma}=h\sum_{n\in\mathbb Z}2\cos(\gamma nh)\delta_{nh}.
                                                               \tag{13}
\]
Poisson（先在 Schwartz 源）给完整、带全部 aliases 的正谱公式
\[
 Q_{h,\gamma}(r)=\sum_{k\in\mathbb Z}
 \{|\widehat r(\gamma+k\Delta)|^2+
                  |\widehat r(-\gamma+k\Delta)|^2\}.
                                                               \tag{14}
\]
对应两支相位的重合项也按 multiplicity 相加。k=0 是 \(2\cos(\gamma u)\) 的完整 Gram，余项 \(R_{h,\gamma}(r)\ge0\)。没有 2π 或 h 的额外归一化；(13) 中 h 恰抵 Poisson 的 1/h。

**固定窗统一上界。**固定 R>0，令 \(\operatorname{supp}r\subset[-R,R]\)，使用原全线 zero-extension Hlog 范数，取固定 \(\chi\in C_c^\infty\) 在该窗等于1。写 q=|hatχ|、w(t)=1+log(2+|t|)。由 χr=r，
\[
 |\widehat r(\lambda)|^2\le\frac{A_\lambda}{(2\pi)^2}
       \int q(\lambda-t)w(t)|\widehat r(t)|^2dt,
 \qquad A_\lambda=\int\frac{q(\lambda-t)}{w(t)}dt.            \tag{15}
\]
当 |λ|≥2，把积分分为 |t−λ|≤|λ|/2 和其补集。前者 w(t)≥c w(λ)，后者 q 的 Schwartz 尾给任意负幂；有界 λ 用 q∈L1。因此存在只依赖 χ 的 C，
\[
 A_\lambda\le C_\chi/w(\lambda)\quad(\lambda\in\mathbb R).
                                                               \tag{16}
\]
取 Δ≥max(2,4|γ|)，则所有 k≠0 的 \(\lambda_{\pm,k}=\pm\gamma+k\Delta\) 满足 |λ|≥3Δ/4。每一支是 Δ-separated；由 \(q(x)\le C(1+|x|)^{-2}\)，选最近格点并估计其余点，得
\[
 \sup_t\sum_{\pm}\sum_{k\ne0}q(\lambda_{\pm,k}-t)\le C_\chi.
                                                               \tag{17}
\]
两支可能重合时上界只多固定因子2，不使用相互 separation。把 (16)–(17) 代回 (15)，Tonelli 对非负 integrand 合法，得
\[
 \boxed{\quad0\le R_{h,\gamma}(r)
   \le\frac{C_R}{\log(2+\Delta)}\|r\|_{H_{\log}}^2.\quad}  \tag{18}
\]
C_R 只依赖所选 χ，特别在 Δ≥max(2,4|γ|) 范围对 γ 一致。式 (15) 的 \((2π)^{-2}\) 与 \(\int w|\hat r|^2=2π\|r\|_{Hlog}^2\) 留一个固定 \((2π)^{-1}\)，已吸收进 C_R。

首先对 compact smooth r 证明；固定窗 Dlog 的旧 form core、(18) 及固定 h 时 (13) 有限个 autocorrelation 取值的 du 连续性，把 (14)–(18) 延到整个 zero-extension Dlog 窗域。这里没有把全线 Dlog 改成 periodic／regional 域。对多个固定 γ 的非负有限组合，费用按其正权相加；γ 和权随 j 增长时必须同步使对应 Δ 足够大，并显式支付 \(\sum a_j C_R/\log\Delta_j\)。不把单 atom 固定窗结论扩成任意成长 family。

**同阶 lower 与 du 反测。**固定非零 \(\eta\in C_c^\infty((-R,R))\)，\(\int\eta\ne0\)。可固定 \(b_+,b_-\in C_c^\infty((-R,R))\) 使 \(\mu_i b_j=\delta_{ij}\)：两实指数在任意开窗上线性独立，故两个 moment functional 满秩。取 \(\lambda_h=\gamma+\Delta\)，定义
\[
 r_h(u)=e^{i\lambda_hu}\eta(u)
       -\sum_{j\in\{+,-\}}\mu_j(e^{i\lambda_h\cdot}\eta)b_j(u).
                                                               \tag{19}
\]
这样两 pole 矩严格为0，修正系数因 compact 光滑积分分部积分为任意负幂 O_N(|λ_h|−N)，不是只近似消 pole。故
\[
 \|r_h\|_{du}^2\to\|\eta\|_2^2,\qquad
 R_{h,\gamma}(r_h)\ge|\widehat r_h(\lambda_h)|^2
                 \to|\textstyle\int\eta|^2>0.              \tag{20}
\]
所以不存在全固定窗源的 uniform du 误差 o(1)。同时 Fourier 平移和 dominated convergence 给
\[
 \|r_h\|_{H_{\log}}^2\sim\log\Delta\,\|\eta\|_2^2.
                                                               \tag{21}
\]
支配可用 \(w(\lambda+x)\le C\{w(\lambda)+w(x)\}\) 及 \(\widehat\eta\) 的快速下降，修正项的 Hlog 费仍为任意负幂。因此 (18) 的 1/logΔ 阶在本原域上为 sharp order，且负对照已限制在双 pole-zero 子域。它不声称每个源都付此 lower；它是 operator 全源 upper 的匹配 test。

这个输入确实比逐测试 Poisson／D′ 收敛更强：给了完整正 carrier 到目标 cosine Gram 的**所有固定窗物理源统一原 Hlog 费用**，并准确说明原 du 为何不能有同样小费。它不消405全 Pan：单个 cosine／lattice carrier 一般不满足 (12)，也不包含经典完整 Γ／prime powers／pole 身份。可将其作为正模型逼近的已付模块；把多个这样的模型组成 Wζ 的目标收敛仍欠独立权重／频率生成与全误差。本节不因模型费用已付而宣称经典 RH、独立容量或成长 core 已改变；是否结算新一轮由 root 在合并实际 family 来源与强旧对照后决定。
