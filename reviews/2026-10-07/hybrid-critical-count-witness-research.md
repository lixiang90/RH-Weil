# 临界 count witness：真实振幅域、lower-kappa plain 重证及 amplification 的可核结论

2026-10-07。独立研究。主要结果：**原 generic plain proof 可从其明确底层 [R] 输入重证到 \(\kappa\in[37/50,1]\)**，保留全部系数、mask、effective conductor 和高度统一性；不是在原 lemma 声明域外直接引用它。由此能合法改善临界 count，排除旧 envelope 的唯一等号点。实际 characters/witness 的额外联合可行域尚未缩小；六次幂带槽 amplification 的自然扩展合法，但不能改善临界长支。

本报告仅新增，不改 notes 449、正式论文、旧报告、脚本或 math 源。未构建外部项目。

## 1. 固定输入与全文准入范围

固定源：
E:\codex-build\math\preprints\The-Quasi-Riemann-Hypothesis-September-30-2026\build\paper.tex。

- commit：adc7f1241b42e322a6451854ab7e4b4c146bf78a。
- canonical LF SHA-256：42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3。
- 已交付 free-b 论文最终 canonical LF SHA：5df2b6ad687572229e2c4d41292bee6cf81b57a13b762173d26732169f1688db。
- 旧临界边界
  \[
   \theta_0=(1507-2\sqrt{921})/1653,\quad
   e_0=(33+8\sqrt{921})/1653,\quad
   b_0=(2185e_0-213)/1228,
  \]
  \[
   \delta_0=(49-\sqrt{921})/48,\quad x_0=1/2,\quad y_0=0.
  \]

此次逐段读取了 actual bins/witnesses 4220–4685、marked 9220–9269、amplification 12362–12475、**完整 generic plain proof 12492–14974**、physical \(Q_i\)/amplitude/capacities/counts 14985–15446，以及 adaptive cutoff 15920–15992。对 plain proof 的全部 \(\kappa\)、\(2M/9\)、\(M/21\)、\(7/2\)、old-eq:3.6 和 affine-budget 引用同时进行了文本依赖定位；下述重证不只检查 theorem 的显示公式。

保留的底层 [R] 是原 finite Gauss/full-correlation/complete-support identities、reciprocity 与 zero extensions、smooth/kernel calculus、global logarithmic control、primitive functional equations/growth、fixed-field ideal/prime counts。原 unrestricted zero-slot induction 与 positive-slot induction一起按下面的范围重做；不将原 \(\kappa\ge3/4\) theorem 本身当作新范围的输入。不声称重新认证这些底层证明核。

## 2. 为什么 actual amplitude 上端尚不能直接排除

源 bins **向下舍入**：
\[
 a\le M_i(u)<a+e,\qquad a\le\sigma<a+e
\]
（4298–4303），不是把实际零点严格夹在 \(a\) 左侧。所有 \(\mathcal X_u\) 的 conductor/deleted radical 仍为 \(O_{\mathcal A}(q_u)\)（4244–4257），有限群 \(\Theta\) 和双方 common presentation 不变。

原 physical main slots 为
\[
 Q_i(u;z_{\rm phys})=P_i^{-1/2}
 \sum_{p\in\mathcal P_i(Z)}
 \overline{\chi_p(u)}W_i(q_p/P_i)(q_p/P_i)^{z_{\rm phys}-1}.
 \tag{1}
\]
所有 slots 使用同一 varying row character、原 ray coefficients、原自然零延拓和外部 physical height。prime upper bound 在 \(a+8e\) 的缓冲线上推导，实际结论为
\[
 |Q_i|\ll U^{\epsilon_1}P_i^{a-1/2+O(e)}
 \tag{2}
\]
（15015–15061）。它不含严格的 fixed-power gap。

幅度定义直接允许 endpoint：
\[
 g_i=\min\{\delta/2,\max(0,\vartheta
       \lfloor\log|Q_i|/(\vartheta\log P_i)\rfloor)\},\quad
 q=\ell^{-1}\sum_i\ell_i g_i .
 \tag{3}
\]
所以 \(y=0\) 在该分箱中等价于每个正长度 slot 都是 main、非零且 \(g_i=\delta/2\)；error/zero slot 必有 \(g_i=0\)（15064–15090）。这是一个准确可核的联合条件，但单由 (2) 不能证明其不存在。即使某个更精细显式公式有 \(1/\log P_i\) 因子，它也只是 subpower，不能直接变成全局统一的正指数缺口；原 buffer/clipping 还允许超过 \(\delta/2\) 的小固定幂。

原 witness 是同一个零点/presentation下的 \(M_r,S_m\)，满足
\[
 r\le t+o(1),\quad r+m\ge t-o(1),\quad
 0\le m\le1/2+o(1),\quad r\ge t-1/2-o(1),
 \tag{4}
\]
以及各自饱和 spike（4510–4547）。但源 15163–15167 明说 witness heights 与 physical heights 不必相等；它们的统一性由参数 Sobolev、共同 Fourier allowance支付。不能由“同一 row character”推断它们具有同一 phase、同一主 residue 或一个额外 Hölder 节省。

命题对每个 \(t\) 给存在 witness，未给不同 \(t\) 的选中 dyads/profile之间的定量相容条件。仅对数值合同 (2)–(4) 而言，short branch 可以在 \(r=r_*(t),m=t-r_*(t)\) 取最坏点，long branch 可以在 \(r=t,m=0\) 取最坏点；这只是合同的可行参数，不是实际 prime sums 或 actual rows 的构造。若要凭多 \(t\) witnesses进一步缩小域，需支付它们共同 profile/height的 mixed moment或 detector dyad 连续性约束；原两种单独 moments尚未给这个新输入。

## 3. Lower-kappa 的可审命题

**命题 [T/R]。** 将源 lem:plain 的首句范围改为
\[
 37/50\le\kappa\le1.
 \tag{5}
\]
其余全部声明保持原状：rows \(q_k\ll Z^m\)、fixed twist \(\tau\) 的完整 displayed moving radical \(Z^q\)、effective width \(M=m+q\)、同一 polynomial-size fixed extra mask、原有限 \(\Theta\) coefficient lists、disjoint underlying prime supports、原 natural row zeros与 \(\mathcal R_z\)。对 positive slots 仍要求
\[
 n_1+n_2+6\kappa z\le M,\qquad
 \beta_*\le(1+\kappa)/2 \quad(\kappa<1).
 \tag{6}
\]
zero-slot 保持全部 bounded nonnegative plain lengths；仍只在 nonprincipal inducing rows 上使用它。则原结论
\[
 \sum_{k\in\mathcal R_z}|S_{\psi_k}(n_1)S_{\psi_k}(n_2)Q|^2
 \ll Z^{M+\epsilon}
 \tag{7}
\]
成立，并有相同的固定、与 slot count 无关的 mesh 和有限 seminorm/polynomial-height 顺序，统一于 (5)。

### 3.1 全高度 prime bound 与系数前件

源 12833–12900 的 global prime estimate只要求 \(s_\kappa=(1+\kappa)/2\ge\beta_*\)，在固定 \(e>0\) 右移后使用 global logarithmic control；其解析路径在 (5) 上位于固定紧实 real strip \(s_\kappa\ge87/100\)。非 principal slot来自同一个 \(\Theta\) expansion和 inducing-family 排除，原 deleted radicals仍计入 conductor。重做这一段给
\[
 |Q_{\boldsymbol\omega}|^2\le
 C Z^{\kappa z+\epsilon_1}p_j(\boldsymbol W)^b
                    (1+|\boldsymbol\omega|)^h .
 \tag{8}
\]
\(\kappa=1\) 仍用 absolute prime count。uniformity只把固定紧区间下端换成 \(37/50\)；contour displacement仍为 \(2ez\)，derivative/height orders不进入 \(Z\)-指数。每次 weighted Fourier use保留这个固定高度因子。没有新 principal residue或一般局部 quotient。

### 3.2 Terminal width 的冗余数字

源 12925–12938 用 (6) 得
\[
 z\le M/(6\kappa),\qquad \kappa z\le M/6 .
\]
原额外展示 \(z\le2M/9\) 确实依赖 \(\kappa\ge3/4\)，但该段真正的 terminal cost仅为 \(\kappa z\le\rho/6\)。old-eq:3.6 的 \(2M/9\) 在其余 proof 没有被继续引用。新范围可以如实展示 \(z\le25M/111\)，保留同一个 terminal error \(T_{\rm term}\)。

### 3.3 同带 comparison 的真正门槛

源 12947–12980 对 \(A>5M/6\) 用
\[
 (6\kappa-1)z\le M-A<M/6 .
\]
在 (5) 上 \(6\kappa-1\ge86/25\)，所以
\[
 z<25M/516<M/20 .
 \tag{9}
\]
用 (9) 代替旧的 \(z<M/21\)，原全部后续 comparison bounds逐项保留：
\[
 A_{\rm comp}\le3M/2-A+2z+\xi
                  \le23M/30+\xi ,
\]
\[
 A_{\rm comp}+(6\kappa-1)z
 \le5M/2-2A+2z+\xi
 \le14M/15+\xi .
 \tag{10}
\]
因此两个边界至少有原 \(M/15\) margin；\(\xi\le\rho/30\) 仍足够。\(L=M/4\)、四个 plain lengths和 equal-product comparison也不变。此门槛只是需要 \(z<M/20\)，不是精确的 \(3/4\)。

### 3.4 两变换和真实 child 不隐藏另一下限

源 13095–13875 的 aggregate support boxes、whole-dyad tails、first complete extraction、two Möbius indicators、common characters/masks、pool \(p^6\) amplification、second correlation和 child width
\[
 M'=M+J-g-g_2+t_2\le M-\sigma
\]
均不依赖新的 \(\kappa\) 下限。pool仍由 \(\ell_*=\sigma/3,\eta<\sigma/6\) 分离；固定 data 先于 moving labels，所有归一化、相位和6-divisible natural zeros保留。

源 13876–14310 的实际 clipping与 mask erasure只需要 \(6\kappa-1\ge0\)，保证缩短/删槽不增加原 affine budget。真实 child defect仍为
\[
 F_{\rm act}=
 (A_{\rm act}-M'_{\rm act}+(6\kappa-1)z_{\rm act})_+
 \le6(w+\ell)+\delta_{{\rm fr},1}+2\theta_N .
\]
移除 whole slots的准确比例为
\[
 \kappa d_z\le F_{\rm act}/6+\kappa\eta
             \le\Delta_{\rm child}
                   +\delta_{{\rm fr},1}/6+\theta_N/3+\eta .
 \tag{11}
\]
因 \(0<\kappa\le1\)，原固定 edge allowance没有增加。不同实际 rectangles分别 clipping、paired coefficient shell、原 \(\mathcal R_z\) family和原 coefficient class均不变；没有在扩域时忽略 moving-conductor或boundary defects。

### 3.5 Exceptional、centering、finite induction 与顺序

源 14312–14777 的 inducing-\(\Theta\) exceptional count仍由 sixth-power form支付；其 \(F_1,F_2\)、common masked equal-product cancellation及 \(A-5M/6-2v/3-(L-v)_+\) 不含 \(\kappa\)。positive-slot条件仍蕴含 \(A\le M\)，所以原 exceptional terminal loss保留。padded zero-slot和 reflection不变。

源 14779–14974 的 numerical Lipschitz bound只用
\[
 0\le6\kappa-1\le5,
\]
它在 (5) 上成立。原 width floor/bands、depth \(D\)、strict drop \(\sigma/2\)、同带先 uncentered 后 centered、先全部 zero-slot再 positive-slot均保留。原 \(\rho,\sigma,\delta,\xi,\eta,\epsilon_0\) 选择可使用同样数界，uniform于 (5)，先于 fixed slot count。随后固定 profile boxes、aggregate support threshold，反向选择有限内部 seminorm/height orders；后来的 external Fourier-tail order不能改内部 height order。原 arbitrary moving-modulus bookkeeping、自然零延拓和全部群例外没有变化。

这逐段完成 (7) 的相对重证；未将“略微小于 \(3/4\)”仅作为连续性口号。

## 4. 新域下 actual counts 的精确公式与 strict widths

设
\[
 c=(3\kappa)^{-1},\quad
 D_\kappa=3-(1+2c)x,\quad
 P_\kappa=(2-2cx)(1-x),\quad x=q/\delta .
 \tag{12}
\]
原 marked input不改。新的 plain容量精确为
\[
 z_P=(1-2m)/(6\kappa),\qquad z_M=(1-r)/2 .
\]
同一个物理槽 spike与两份 plain witness给
\[
 A_I(r)=1-\delta\{x+(1-x)r\},
\]
\[
 S_t(r)=1-\delta\{cx+(2-2cx)(t-r)\}.
 \tag{13}
\]
不先与 \(3/4\) baseline作非必要的容量折损。crossing为
\[
 r_{*,\kappa}(t)=
 \frac{(2-2cx)t-(1-c)x}{D_\kappa},
\]
\[
 R_{{\rm short},\kappa}(t)
 =1-\delta+\frac{\delta P_\kappa}{D_\kappa}(3/2-t).
 \tag{14}
\]
long slope \(\alpha=5/6\) 保持不变：
\[
 L(t)=1-\delta+(\alpha-\delta)(t-1).
\]
因此
\[
 J_\kappa=(\alpha-\delta)D_\kappa+\delta P_\kappa,\quad
 t_\kappa=1+\frac{\delta P_\kappa}{2J_\kappa},\quad
 R_{*,\kappa}=L(t_\kappa).
 \tag{15}
\]

在 (5)、\(x\in[0,1/2]\) 上，
\[
 1/3\le c\le50/111,\quad D_\kappa>2,\quad P_\kappa>3/4,
\]
\[
 r_{*,\kappa}(1)\ge8/13>3/5,\quad
 r_{*,\kappa}(3/2)=1,\quad
 1/3\le t-r_{*,\kappa}(t)\le1/2.
 \tag{16}
\]
故可用更保守的固定 inverse supply bound \(z_M<1/5\)，而
\[
 z_P\le1/(18\kappa)\le25/333<1/5 .
 \tag{17}
\]
新应用只需供给 \(\ell/d>1/5\) 的固定正 margin。具体 crossing 的最大 inverse容量其实不超过 \(5/26\)，但 (17) 的简化足够。

marked请求先减固定 \(\nu_0>0\)，其两个原 width均实付：
\[
 1-r-2z\ge2\nu_0,\qquad
 3-2r-8z=4(1-r-2z)+(2r-1)
                    \ge8\nu_0+1/5-o(1).
\]
plain请求 \(z\le z_P-\nu_0\)，给
\[
 1-2m-6\kappa z\ge6\kappa\nu_0>0.
\]
\(r\ge1\)、\(m\ge1/2\)、small capacity neighborhoods和 \(\delta=\alpha\)仍用原 no-slot/amplified endpoints，不把 shrinking width充当 marked fixed margin。

有限群系数分解与 whole-product conjugation仍是15136–15170的原形式；全部 positive whole slots按同一 \(g_i\) bin、原 windows和自然零延拓选择。原 cumulative \(T_1/2\)、inducing exceptions和 smooth rowwise profiles保持不变。先 losses/decrement/mesh，后 fixed \(K\)，再 amplitude/bin losses与目标内部 height orders；\(U^{O(\epsilon)}(1+T_1)^A\) 由之后固定的 detector ceiling支付。新的 count公式因此具有原 actual、而非 nominal-only，准入范围。

## 5. 严格改善临界 count 和反馈 kappa 的量词

对旧已证全族 \(\beta_*\le\theta_0\)，可先于目标固定
\[
 \bar\kappa=2\theta_0-1
 =(1361-4\sqrt{921})/1653 .
\]
它满足 \(37/50<\bar\kappa<3/4\)，故第3节 lemma合法使用，而 \(c>4/9\)。

直接微分：
\[
 \frac{\partial}{\partial c}\frac{P_\kappa}{D_\kappa}
 =-\frac{2x(1-x)^2}{D_\kappa^2}<0\quad(x>0).
 \tag{18}
\]
\(R_{*,\kappa}\) 随这个比值严格增加，故降低 \(\kappa\) 严格改进每个 \(x>0,\ 0<\delta<\alpha\) 的 actual count envelope。在旧 critical geometry，
\[
 E_{\theta_0,\bar\kappa}
 =E_{\theta_0,3/4}
                  +h_0(R_{*,\bar\kappa}-R_{*,3/4}).
\]
旧连续证书唯一等号在 \(x=1/2,\delta=\delta_0\)，那里 (18) 给严格负值；\(x=0\) 的旧证书已经严格负。于是整个紧矩形 \(\delta\in[1/50,3/4],x\in[0,1/2]\) 有共同严格负 margin。这是可证的新输入，不是只改变 \(b\) 或假设实际 amplitudes不存在。

若优化使用候选边界 \(\sigma_*\) 与 \(\kappa_*=2\sigma_*-1\)，不能在反证 \(\beta_*>\sigma_*\) 中直接调用 \(\kappa_*\) lemma。必须使用
\[
 \kappa_{\rm act}=2\beta_*-1,\qquad
 \kappa_{\rm act}-\kappa_*=2\Delta,\quad
 \Delta=\beta_*-\sigma_*>0 .
\]
在 \(\delta\le3/4,\kappa\ge37/50,D_\kappa>2\) 上，
\[
 \partial_\kappa R_{*,\kappa}
 =\frac{(\alpha-\delta)^2\delta x(1-x)^2}
             {3\kappa^2J_\kappa^2}
 \le\frac{625}{36963}<\frac1{50}.
 \tag{19}
\]
用 \(J_\kappa\ge(\alpha-\delta)D_\kappa\)、\(x(1-x)^2\le4/27\)即可证明这一纯有理界。若 \(h<1\)，反馈费用至多 \(2\Delta/50\)，而与 \(C_b(\beta_*)\) 比较本来提供 \(-\Delta\)。因此至少保留 \(24\Delta/25\) 的共同 central margin，先于目标支付 real losses。新候选的连续多项式证书及全部 geometry/Euler/principal/outer/continuation另由主研究构造，不由本报告仅靠 compactness认证其显示最优数值。

## 6. 一个合法但不改善临界长支的带槽 amplification

第3节是本轮优先突破；以下记录另一已准入路径，防止将它误作降低 \(\alpha\) 的理由。

对固定有限 physical positive slots，设其总 \(U\)-长度为 \(z\)。选择原 amplifier \(a\) 同时避开这些 slot 的 underlying primes。若放大尺度 \(P=U^{(B-1)/6}\)，primary ideals \(q_a\le P\) 有 \(\gg_{\mathcal A}P\) 个，而被 slot primes排除的至多
\[
 O_{\mathcal A}\left(P\sum_{p\in\cup_i\mathcal P_i}q_p^{-1}\right)
 =o(P).
\]
固定有限 annuli中 \(\sum q_p^{-1}\ll\sum_i1/\log P_i=o(1)\)；大于 \(P\) 的 primes不除任何非单位 amplifier。可保留 \(\gg P\) 个 eligible \(a\)，独立于 varying row。

由完整自然零延拓，\(Q_{ua^6}=Q_u\)准确成立。原 inverse column identity（12416–12435）可乘这个同一 \(Q\)。对
\[
 B_0=\max\{1,r+2z,(2r+8z)/3\}
\]
取 \(B=B_0+\eta\)、\(H\asymp U^B\)，两个 marked widths有固定正 margin。scale Sobolev、source marked lemma和 injective map \((u,a)\mapsto ua^6\) 给相对定理
\[
 \sum_{\substack{q_u\asymp U\\u\ {\rm sixth\!-\!power\!-\!free}}}
 |M_u(U^r)Q_u|^2
 \ll U^{1/6+(5/6)B_0+\epsilon}(1+T_1)^A .
 \tag{20}
\]
有限 ray-coefficient expansion、pure twists和 rowwise inverse profiles依原参数 Sobolev支付；不允许新增 row-dependent prime coefficients。

但在临界 long branch \(r\ge1,\ z\le\ell/d<1/2\) 中 \(r\ge2z\)，所以 \(B_0=r+2z\)。除以 spikes后的 exponent为
\[
 1/6+(5/6-\delta)r+(5/3-2q)z .
\]
因为 \(q\le\delta/2\le3/8\)，最后斜率至少 \(11/12>0\)。故这条合法强化仍在 \(z=0\) 最优；它没有降低原 long \(\alpha=5/6\)。

直接换成 \(ua^4\) 或更低幂不保留相位：在 genuine order-six 的 residue character 上，\(\chi_n(a^4)\) 一般不是1。CRT可选择 permitted good prime和 primitive sextic unit展示这个失败。必须额外支付 moving factor \(\chi_n(a)^4\)、其 conductor/zero mask，且原 sixth-power-free valuation对 mod4不再保证 injectivity。此处只排除“原 exact column identity不改便降幂”的捷径，不排除另外的合法新 amplification方法。

## 7. 可审结论与尚未支付事项

本报告支付：

1. 全部 physical \(Q_i\)、actual witness、coefficient/height/conductor合同的定位，以及 \(y=0\) 尚不能靠原上界排除的精确原因。
2. 从指定底层 [R]重证的 \([37/50,1]\) uniform plain lemma。
3. 同一 actual slots/moments下新的 \(D_\kappa,P_\kappa\) crossing、strict widths、供给及群/频率准入。
4. 旧临界 count的严格改善，以及反馈 \(\kappa_{\rm act}\) 的 target-independent \(\Delta\)费用。
5. 带槽 sixth-power amplification的相对估计与其临界长支的正 cost。

尚未在本报告中认证新的显示最优边界、连续 root/discriminant certificate、所有 physical high/error-slot/principal/outer接口或新的正式论文。亦未取得 multiple-\(t\) detector的 joint mixed moment、fixed-power amplitude deficit、低于六次幂的实际 phase-compatible amplification、RH/RR或新的简单临界线比例。所有 [R] 无限分析前件仍需独立 proof-kernel验证。
