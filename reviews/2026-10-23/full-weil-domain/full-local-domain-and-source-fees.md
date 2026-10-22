# 从 A1 到完整局部 Weil 强域：实际原子、精确群费用与物理源门

2026-10-23；分支 `/root/full_weil_domain_582`，独占此稿，不改 STATE／cadence。接 [581](../../../notes/581-arithmetic-weighted-two-prime-completion-and-relative-capacity-gap.md) 的实际 split 2、11、native Q／字符／Haar／Gaussian。以下是直接计算，不从 Q 或未知零点选择范数或标签。此稿建立完整局部作用的解析强域；没有把它称作算术循环／Green／regulator 的延拓。

## 1. 已付输入和准确新责任

581 的实际 finite 源为

\[
 F_w(r)=\sum_{j,k\in\mathbb Z}H_{jk}^{-2}c_{a_{jk}}(r)e_{jk},
 \quad H_{jk}=2^{|j|}11^{|k|},\quad
 a_{jk}=2j\log2+2k\log11,
\]
\[
 c_a(r)=\int r(u)\operatorname{sech}((u-a)/2)du,\qquad
 e_{jk}=e_j^{(2)}\otimes e_k^{(11)},\quad
 e_j^{(p)}=p^j\mathbf1_{p^jL_p}.
 \tag{1}
\]

物理源是 ALLcomplex \(r=e^{u/2}f\in S_{\exp}\)，原范数 du 和 zero-extension Dlog。A1 是这些径向球向量的 H 加权系数 ℓ1 空间；它保 partial Fourier、乘法和双读出，但 chirp 一般离开径向基。新责任是给包含 A1 的**具体实际函数空间**，支付完整 \(SL_2(\mathbb Q_p)\) 的 Weil 作用，不能只把群轨道的抽象包络换名。

下文在 \(p=2,11\) 使用 split 坐标

\[
 V_p=\mathbb Q_p^2,\quad L_p=\mathbb Z_p^2,\quad
 Q(x)=-x_1x_2,\quad
 B(x,y)=Q(x+y)-Q(x)-Q(y)=-x_1y_2-x_2y_1.
 \tag{2}
\]

字符 ψ 的 conductor 是 \(\mathbb Z_p\)，Haar 使 L 自对偶、体积1。式(2)保留原二次型的极化；在 p=2 **不写**未经支付的 \(B(x,x)/2\) 或除2的矩阵公式。

## 2. 具体 S0：STFT 范数正好等于一个可见原子 ℓ1 范数

取 \(g=\mathbf1_L\)，定义

\[
 V_gF(a,\xi)=\int_{V_p}F(x)\overline{g(x-a)}
                 \psi(-B(x,\xi))dx,\quad
 \|F\|_{S_0,p}=\int_{V_p\times V_p}|V_gF(a,\xi)|da\,d\xi.
 \tag{3}
\]

这属于 Feichtinger 空间的标准具体 realization；[Enstad–Jakobsen–Luef 的原研究论文 §3](https://comptes-rendus.academie-sciences.fr/mathematique/item/10.1016/j.crma.2018.12.004.pdf)给 p-adic／adelic 的 coset 上绝对 Fourier 级数及 tensor 描述。这里所需二维 split 范数、群费用和源费用由下面逐项证明，引用不代付这些计算。

选 \(V_p/L\) 的代表集 A、Ξ，令

\[
 h_{a,\xi}(x)=\psi(B(x,\xi))\mathbf1_{a+L}(x),\quad
                     (a,\xi)\in A\times\Xi.
 \tag{4}
\]

不同 a 的支撑不交；在每个 a+L，Ξ 恰给 L 的完整正交字符。因此这些 h 是 L2 的正交标准基。若 \(b_{a,\xi}=\langle F,h_{a,\xi}\rangle\)，则 STFT 的绝对值在每个 \((a+L)\times(\xi+L)\) 上等于 \(|b_{a,\xi}|\)：改 a 的 L 内代表不改支撑，改 ξ 的 L 内代表只乘支撑上的常相位。每块体积1，故精确地

\[
 F=\sum_{a,\xi}b_{a,\xi}h_{a,\xi},\qquad
 \boxed{\ \|F\|_{S_0,p}=\sum_{a,\xi}|b_{a,\xi}|\ }.          \tag{5}
\]

式(5)既给 Banach 完备性，也给实际函数身份：每个原子 L1、L∞、L2 范数均为1，所以 ℓ1 合成在 C0 和 L1 一致收敛，并在 L2 收敛。特别

\[
 \|F\|_1,\ \|F\|_\infty,\ \|F\|_2,
 \ |F(0)|,\ \left|\int F\right|\le\|F\|_{S_0,p}.
 \tag{6}
\]

有限原子和是 Bruhat–Schwartz；反之每个 Bruhat 函数有有限个 coset、每个 coset 有有限 Fourier 系数，故属于有限原子和。它在 S0 稠密，但 S0 包含非局部常值的实际函数，不能把这称为恢复原 Bruhat 域。

平移、调制只排列(4)并乘单位相位，因而是等距作用。Fourier_B 也把原子送到一个原子乘单位相位，所以是等距。两原子相乘时，支撑 coset 不同给0，相同则仍是一个原子乘单位相位，因此

\[
 \|FG\|_{S_0,p}\le\|F\|_{S_0,p}\|G\|_{S_0,p},\qquad
 \|F*G\|_{S_0,p}\le\|F\|_{S_0,p}\|G\|_{S_0,p}.
 \tag{7}
\]

第二式由 Fourier 等距及第一式得到。这是真函数乘法／卷积，不是算术截面乘法。

## 3. 球向量的精确费用：算术指数恰是 S0 第一矩

若 j≥0，\(e_j=p^j1_{p^jL}\) 的 STFT 支撑为 \(a\in L,\xi\in p^{-j}L\)，绝对值为 \(p^{-j}\)。若 j<0，支撑为 \(a\in p^jL,\xi\in L\)，绝对值为 \(p^j\)。积分给

\[
 \boxed{\ \|e_j^{(p)}\|_{S_0,p}=p^{|j|}\ },\qquad
 \|e_{jk}\|_{S_0,2\times11}=H_{jk}.                    \tag{8}
\]

两位空间可直接按产品原子定义，等同于 \(S_0(V_2)\widehat\otimes_\pi S_0(V_{11})\)：ℓ1 基的 projective tensor 仍是乘积指标 ℓ1。由(8)，581 的 A1 连续嵌入它，嵌入范数≤1；一般 F 的 S0 范数不必等于其径向 A1 范数，不能误报等距。

因 \(\|\operatorname{sech}(u/2)\|_2=2\)，ALLcomplex 全 L2 源有

\[
 \boxed{\ \|F_w(r)\|_{S_0,2\times11}
 \le2\sum_{j,k}H_{jk}^{-1}\|r\|_{du}
 ={36\over5}\|r\|_{du}\ }.                            \tag{9}
\]

这里 \(\sum H^{-1}=3\cdot6/5=18/5\)。Dlog 也支付(9)。源的所有 mixed 项都已由实际函数合成处理，没有以全空间逆范数下界冒充源费用。原 native L2 中 \(\nu=\|\phi_*\|_2^2\) 与其余 finite 腿因子 μ 仍按581固定；(9)不重定 Haar 或把 ν 设成 raw Gaussian 数值。

因此选择 H^-2 不再仅有形式上的算术来源：H 本身就是该强域中这条格轨道的精确范数。指数2仍只是安全可和幅度，未被唯一强迫，也不构成正极化的 canonical 选择。

## 4. 完整局部 Weil 作用：chirp、dilation、Fourier 和精确 Cartan 范数

在上述 split 模型，Weil 的标准生成作用为

\[
 N_bF(x)=\psi(bQ(x))F(x),\quad
 M_aF(x)=\chi_V(a)|a|_pF(ax),\quad
 W F=\gamma_V\mathcal F_BF,
 \tag{10}
\]

其中 \(|\chi_V(a)|=|\gamma_V|=1\)；split 情形可以取相应标准单位相位。相位与精确范数无关。若采用 metaplectic lift，其中央因子同样模1，不影响下列结论。

先算 chirp window \(N_bg\)。当 \(|b|_p\le1\)，它就是 g。若 \(|b|_p=p^m>1\)，它在 L 上的 Fourier 系数为

\[
 \int_{\mathbb Z_p^2}\psi(-b x_1x_2+x_1\xi_2+x_2\xi_1)dx_1dx_2.
 \tag{11}
\]

对 x1 先积分，非零恰要求 \(\xi\in bL\) modulo L；此时系数绝对值 \(|b|_p^{-1}\)。一共有 \(|b|_p^2\) 个 ξ coset，故

\[
                 \|N_bg\|_{S_0,p}=\max(1,|b|_p).
 \tag{12}
\]

这是在 p=2 仍合法的实际有限 Gauss 计算。由 \(Q(x)=Q(x-a)+B(x-a,a)+Q(a)\)，N_b 把任一原子送成 \(N_bg\) 的平移／调制乘单位相位，所以(5)给上界；在 g 上取到下界。dilation 同理，由其与平移／调制的共轭关系以及 \(M_ag=\text{phase}\cdot e_{-v_p(a)}\)，得到

\[
 \|N_b\|_{S_0\to S_0}=\max(1,|b|_p),\quad
 \|M_a\|_{S_0\to S_0}=\max(|a|_p,|a|_p^{-1}),\quad
 \|W\|_{S_0\to S_0}=1.                              \tag{13}
\]

这已经支付任意有限 Bruhat word。还有更准确、不依赖分解的全群公式。置

\[
 \theta_p(g)=\max_{i,l}|g_{il}|_p\ge1,
 \qquad g\in SL_2(\mathbb Q_p).
\]

K=SL2(Zp) 的 elementary unipotents 以及 W 均为等距，其逆也等距，故每个 K 元素等距。Cartan 分解给 \(g=k_1m(p^n)k_2\)、n≥0，且 \(\theta_p(g)=p^n\)。上界由(13)，下界在范数1的实际测试向量 \(\omega(k_2)^{-1}\mathbf1_L\) 上取到。于是

\[
 \boxed{\ \|\omega(g)\|_{\mathcal B(S_0,p)}=\theta_p(g)\ }. \tag{14}
\]

没有宣称对所有 g 统一有界。每个有限原子和是 smooth Weil vector：原 Bruhat 公式给一个开紧 stabilizer。有限原子稠密，且 θ 在每个群紧集上有界，所以 \(g\mapsto\omega(g)F\) 对每个 F∈S0 强连续；结合局部有界性得到联合连续作用。不声称算子范数拓扑下连续，也不把所有 S0 向量称为 smooth。

两位实际源在每个先固定 \(g_2,g_{11}\) 上满足

\[
 \|\omega(g_2,g_{11})F_w(r)\|_{S_0,2\times11}
 \le {36\over5}\theta_2(g_2)\theta_{11}(g_{11})\|r\|_{du}.
 \tag{15}
\]

矩阵 entry height 是独立局部数据。它和格高度的(8)相容，但还没有 arithmetic height／RR 身份。

## 5. λ、全 finite 位积与 arch 端：哪些费用确实延拓

由(6)、(14)，

\[
 \lambda(F)(g)=(\omega(g)F)(0),\qquad
 |\lambda(F)(g)|\le\theta_p(g)\|F\|_{S_0,p}.            \tag{16}
\]

它在每个固定 g 上连续；parabolic transformation identity 从稠密的 Bruhat 子空间和(16)继承。identity／Fourier 两条读出都保留，λ 不是手添的 abstract boundary。标准 section 的每 fixed-g s 导数可保留实际 \(\log|a(g)|\) 因子，但(16)不支付全 adelic Eisenstein 总和、全高度的一致误差或 arithmetic theta 定理。

在其余 finite 位可以保原 Bruhat 空间：对每个先固定 finite S，取两位 S0 与 S\{2,11} 上 Bruhat 的 tensor，再对有限 S 作 restricted inductive tensor。每个 adelic g 只有有限个非 K 的腿；good 位的原格向量被 K 固定，bad7及新受作用位的原 Bruhat 域在 Fourier／chirp／dilation 下仍稳定。因此这给含(1)的实际全 finite Weil 域；并非声称原 ramified7腿被 Fourier 固定。

也可以把其余 finite 位一起完成为 S0 的 adelic projective tensor。一般 bad 位不使用(14)的 split 精确常数：选固定 compact-open window，chirp 在其支撑上局部常值，故有有限原子和；Fourier 把 compact-open 格送其真实对偶格，二者 commensurable，仍为有限原子和。上述 covariance 给每个固定 bad 位 g 的有限常数。almost-all good 位常数1，所以每个 fixed adelic g 的乘积常数有限。这个构造不把 bad 位的 Haar／dual lattice 修改成 split 数据；精确 \(36/5\) 和 θ 只属于2／11两位费用。

arch 端可保 Schwartz(V∞)，与上述 finite 域作 projective tensor；原 fixed Gaussian 的全部 arch 半范数只是固定因子，完整实 Weil 作用保 Schwartz。若希望一个 Banach 强域，可改用真实 Gaussian window 定义的 S0(V∞)，再与 finite S0 作 projective tensor。real metaplectic covariance 将 STFT 的相空间作保体积线性变换；\(\omega(g_\infty)g_\infty^0\) 是实际 chirped Gaussian，其 STFT 有有限 Gaussian 积分，故每个 fixed g∞ 连续作用。常数依赖 g∞，不宣称全群统一。

因此 **fixedarch \(\phi_*\otimes F_w(r)\)** 进入完整 local／adelic Weil 强域的原 du 费用仍由(9)乘固定 arch 和其余 finite 常数支付，原 Dlog 亦支付。全源注入仍由581的 Riesz／dense samples 原证明给出；扩空间并不改变这条实际向量的 kernel。405 的全部 \(\tau_bP\) 依然有非零向量像，537 非根依然保留。full-group 稳定没有把405自动变 principal，也未给新的相对边界。

## 6. 读取额外原源的 raw arch 接口：逐源合法，但不能冒称原 du 统一费

579 的实际 raw arch map

\[
 T^*r=\int r(u)D_u\phi_*\,du,\qquad
 D_u\phi(x)=e^{u/2}\phi(e^{u/2}x)
 \tag{17}
\]

读取全部原源，且在 S_exp 上注入。选 \(g_\infty^0=\phi_*/\sqrt\nu\) 为 L2-unit Gaussian window，沿 native Gaussian 坐标直接做 STFT Gaussian 积分，在真实维数2有

\[
 \|D_u\phi_*\|_{S_0,\infty}=4\sqrt\nu\cosh(u/2),\qquad
 \|T^*r\|_{S_0,\infty}
       \le4\sqrt\nu\int |r(u)|\cosh(u/2)du.             \tag{18}
\]

这里 S0 的 STFT 范数按 L2-unit window 定义；若选另一个 fixed Gaussian／字符坐标，只改变固定等价常数，不能改 u 的指数费用。S_exp 支付该实际 Bochner 积分。它不是全线原 du 费用：取537窗内非零 compact 双pole-zero \(r_0=(D^2-1/4)\psi\)，令 \(r_T=\tau_Tr_0\)。原 du、全线 Dlog 范数及双pole-zero不变，而

\[
 T^*r_T=D_TT^*r_0,\qquad
 \|T^*r_T\|_\infty=e^{T/2}\|T^*r_0\|_\infty>0.
 \tag{19}
\]

最后严格正来自579实际 T* 的注入；双polezero使该函数在 x=0 为零，不能靠 origin 值错误证明(19)，这里用的是全 L∞ 范数。STFT reconstruction 给 \(\|F\|_\infty\le\|g_\infty^0\|_\infty\|F\|_{S_0,\infty}\)，故(19)是每个实际源的强费用下界，排除这个 raw 接口的全线 du／Dlog 统一上界。它不排 fixed-window 费用、带权物理范数、源相关非有界 height 或另一个 actual map。

这一区分正是本轮额外源责任：\(\phi_*\otimes F_w(r)\) 的全源可见性和(9)原费已付；把另一个独立 raw 物理腿 \(T^*r\) 接到 arithmetic regulator 时，不能借用前一个 map 的费用。若 tensor 两个 r-dependent 腿，所得 map 一般二次，不应继续称为线性源。

## 7. 完整经典预算、对照和停止范围

本域保留原 Q、ψ、Haar、arch Gaussian 及 genuine λ，所以没有截去完整 Γ／FP-contact、素数幂或极点。但它本身还不证明新的 Γ 预算恒等式：581 在 right-transported 球族上已核完整 Mellin 输出 \(B_r\mathscr M_0\)，该实际源未变；一般 S0 向量上的无限 Eisenstein 导数、cycle 和 Green 延拓尚需同域定理。标准／transported 导数之间580的实际局部 δ 修正不能因 full-group 稳定而删去。特别 finite local positivity 或一个正 S0 范数不能自动支付

\[
 Q_\zeta(r)=\mathcal A_\Gamma(r*r^\sharp)
             -\mathcal P_{\text{all powers}}(r*r^\sharp)
             +\mathcal H_{\text{both poles}}(r*r^\sharp).
\]

continuous ±1/16 对照保同一个 source map、强域和正局部范数，而完整 native Weil 型在同一合法源上异号。它检出“局部 Weil representation＋正强域⇒正的完整 Weil预算”这一遗漏；没有 continuous→CM 运输，不能称其为 arithmetic KRY 的反例。

函数域的相同局部 S0／Weil 设施可以定义，但两 place 的 lognorm 步长相称；不能偷取数域2／11的 dense-grid 注入。真正正号仍来自同一 \(C\times C\) 的 degree-zero primitive 对应、有效截面／乘法和 RR／Hodge index，包含完整 returns、aliases 以及 H0／H2 极点。S0 的实际点乘(7)不是其截面乘法；强域本身没有给局部消失过滤、integral lattice、same-object Green pairing 或 primitive quadratic RR。

新付的实际输入是：(5)非抽象强域，(8)算术格范数恒等式，(12)包括2-adic的 chirp 有限Gauss费用，(14)全局部群的精确 entry-height作用范数，(9)/(15)/(16)全源原 du/Dlog 与 genuine λ 费用，及(18)/(19)额外 raw arch 源的准确强费用边界。没有新 RH 正号、同对象容量、actual q 消失或 whole 后果。542+555→557 的 strongest-old 仍只是 leading4/5 负惯性 UPPER，未改变。

停止把“full Weil 稳定强域”本身当作下一容量证明。下一独立输入必须是这个同域上的 actual arithmetic principal／regulator／cycle／Green 公式，读取额外源却先核405全主关系、537非根、原范数与全部误差，再给同对象局部消失过滤／截面lift／primitive mixed RR。若只按定义把405像作边界、或从 \(Q_\zeta\) 拉回 height，仍是旧商／等价改写。
