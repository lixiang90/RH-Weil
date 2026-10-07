# 可变 slot 总长度的 compensated low estimate：完整条件准入推导

日期：2026-10-07。状态：**条件推导完成；相对于下列确切外部通用引理，low estimate 准入通过**。这不是对外部论文全部算术前件的独立重证，也不是新无零半平面、RH 或 Weil/RR 桥梁的证明。

## 1. 输入绑定与条件命题

只读输入为 E:\codex-build\math\preprints\The-Quasi-Riemann-Hypothesis-September-30-2026\build\paper.tex。
其 canonical LF SHA256 为
42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3
（766316 字节）。下文行号均绑定这一源文件。

外部原文的固定 geometry 是 6857–6866 行，compensated probe 的**原有限表达式**是 6894–6903 行；本报告保留后者的全部系数、原 slot 窗口、mark、排除集和零延拓，仅另取固定几何参数
\[
 e=\frac1{20000},\quad
 \ell=\frac16+e=\frac{10003}{60000},\quad b=\frac18,\quad
 M=1-\ell,\quad l_x=\frac{M-b}{2},\quad l_y=l_x+b,\quad
 h=1+\ell-l_x.                                                   \tag{1}
\]
因此
\[
 M=\frac{49997}{60000},\quad
 l_x=\frac{42497}{120000},\quad l_y=\frac{57497}{120000},\quad
 h=\frac{32503}{40000},\quad M+\ell=1.                             \tag{2}
\]

**条件命题。** 固定一个符合原文 6846–6851、6868–6883 行全部条件的算术 datum、目标 \(\eta\)、有限 slot 系统和 smooth tests；slot 长度正且总和为 (1) 的 \(\ell\)，原底层素数窗口互不相交。以 \(X=Z^{l_x},Y=Z^{l_y}\) 代入同一个原 finite compensated probe。条件于 §2 列出的源引理，有
\[
 \forall\epsilon>0,\qquad
 |I_{\eta,\mathrm{modified}}(Z)|
 \ll_{\mathrm{fixed},\epsilon}
 Z^{\,l_x/2+b/12+\epsilon}
 =Z^{14999/80000+\epsilon}.                                      \tag{3}
\]
常数、有限导数阶和 \(Z\) 下阈值可依赖已固定 datum、目标、slot 系统、测试函数和 \(\epsilon\)，但不依赖移动素数标签、当前 row 或 rescaled tuple。指数不依赖 slot mesh。**没有断言**常数在 \(K\to\infty\)、slot 长度趋零或测试支持任意变化的系统间统一。

## 2. 确切通用前件

本证明以源中的以下结果为条件输入，而不把原固定 geometry 的 lem:probe-row-norm 或 prop:probe-low 直接改参使用。

| 源结果 | 行号 | 本证明需要的实际范围 |
|---|---:|---|
| eq:low-separated | 3456–3479 | 任意正 \(X,Y,Z\)，同原 corrected row、ray 分解和 \(m\ne0\) 支持 |
| lem:smooth-calculus | 1123–1209；共同密度的 Minkowski 证明 1222–1229 | 固定 compact logarithmic box、固定 norm monomial；一个密度同时用于所有 rows |
| lem:gaussian-annular | 1288–1315，导数证明 1320–1339 | 任意固定 annular 分解、阶数和正 tail cutoff；不要求 \(\ell=1/6\) |
| lem:reflection-row-sectors | 2470–2506 | 所有非零 element rows，包括 meeting \(S\) 的 rows；每个共享 good-prime 零均保留 |
| prop:completed-reflection 及 lem:reflection-common-profile | 通用 kernel 界 1852–1880；2540–2566 | 固定 joint profile 和任意正 block scale；有限 smooth seminorm、norm-twist polynomial cost |
| eq:reflection-common-minkowski | 2580–2609 | 先从共同密度提取 homogeneous 小标量，再平方；仅随后扩大 separated positive row norm |
| cor:marked-reflection 与精确 phase separation | 7361–7415；7443–7483 | product-form whole-index marks、分开的 full \(M_{\rm ref}^2\) row/tuple sectors、原零掩码 |
| lem:reflected-energy | 7747–7804 | 固定 bounded log-length ranges；product-form slots；固定 row restrictions 与 active slots/dual variables 独立，显式 row-mark mask 除外 |
| prop:probe-gram | 8340–8361 | \(Q,Y'\ge1,\ P_a=Y'^2/Q\ge1\)，固定 polynomial scale ranges；只允许原 fixed-ray 系数及固定有限线性组合 |

反射能量的底层 norm 输入是 lem:hybrid-energy（7510–7540），不是新的任意 pair-mask sieve。它允许 \(n,b\) 的原 source \(S\)-支撑，并要求 tuple 与 dual 系数分别独立于当前 row；其两个 moving masks 由自身证明处理。反射 tail 使用 lem:lattice-kernel-tail（2618–2628）及 7892–7914 行的 whole-dyad 删除。以上通用陈述均没有 \(\ell=1/6\) 或 \(M=5/6\) 的限制。

本报告检验这些通用陈述对本次参数的适用性，以及以它们为前提的新指数证明；没有重新认证 DR theta 变换、GL/HB sieve 或完整 additive-correlation 证明。

## 3. 原物理 probe、row masks 与 joint-profile 准入

固定 \(J\subseteq\{1,\ldots,K\}\)，把 rescaled tuple \(p_J\) 固定。记
\[
 d=\sum_{i\in J}\ell_i,\quad
 M'=M-2d,\quad \ell'=\ell-d,\quad
 r_J=q_{p_J}/Z^d,\quad 0\le d\le\ell.                             \tag{4}
\]
原 annular 支持给 \(0<c_J\le r_J\le C_J\)，常数对当前移动 tuple 统一。保持
\[
 X'=\frac{Z^{l_x-d}}{r_J},\qquad
 Y'=\frac{Z^{l_y-d}}{r_J},\qquad
 Q=q_{b_*}X'Y'=\frac{q_{b_*}Z^{M'}}{r_J^2}.                        \tag{5}
\]
原 8094–8109 行的 \(B^J_{m,\sigma}\) 不变：surviving slots 是 \(J^c\)，其系数仍为单个素数函数的乘积；固定 \(p_J\) 只进入 \(X',Y',Q\)，不进入其 marked completed coefficient。这是原 finite probe 的逐 \(J\) 精确重写，不是另造目标 row。

以下支持条件必须保留。

1. 原低分离中的 \(m=0\) 由 \(W_0\) 的 annular 支持精确消失（3476 行）。\(\xi(m)\) 的 \(S\)-零掩码仍在原低分离；Cauchy 上界仅使用 \(|\xi(m)|\le1\)。为界 \(B^J\) 可以求和所有 \(m\ne0\)，不能把新的 \((m,S)=1\) 掩码塞进其反射系数。源 8199–8202 行正是使用覆盖全部非零 rows 的 sector lemma。
2. primal completed ideals 避免原 \(S\)，squarefree/cube ideals 允许共享素数（8089–8093、7325–7326 行）。marked prime 若与 base local prime 碰撞，原 primal 项为零，先按 7413–7414 行精确删除；此后只保留明确的 \(1_{(P,R)=1}\) mask。
3. 冻结 powerful row part、supported squarefree part 及全部非 residual local factors。特别不能平均移动 \(j=4\) non-slot 因子，否则 7451–7455 行的 residual-row/mark phase 消去不成立。
4. \(R\) 与 active mark product \(P\) 各自固定 full \(M_{\rm ref}^2\) class（7461–7467 行），不是只固定乘积。于是剩余 scalar 为 row-only、tuple-only 或 frozen factor；dual coefficient 是 full extracted dual index 的函数。active moving columns 原样为
   \[
   \chi_R(nb^3)^3=\chi_R(nb)^3,\qquad
   \chi_P(nb^3)^{-2}=\chi_P(n)^{-2}1_{(P,b)=1},
   \]
   两式含全部零（7469–7483 行）。没有引入 \((n,b)=1\)。
5. dual ideals 必须保持源 old-eq:4.3 的完整支撑，包括 permitted \(S\)-primes 和 \(h_\lambda\ge-4\)；不得复制 primal \(S\)-mask 到 dual side（7731–7735、8255–8258 行）。

对 surviving tuples 的 Gaussian 并不逐 tuple 选密度。按照 8125–8145 行，令 \(r=q_A/Z^{1+\ell'}\)，在 \(r=e^kx\) 的固定 translate annulus 保持一个 profile
\[
 w_{k,J}(x,\boldsymbol\varrho)
 =\chi(\log x)\,
 W_{\mathrm G}\!\left(e^kx/\prod_{i\notin J}\varrho_i\right)
 \prod_{i\notin J}W_i(\varrho_i),\qquad
 \varrho_i=q_{p_i}/Z^{\ell_i}.                                    \tag{6}
\]
所有 logarithmic coordinates 有固定 compact 支持。Gaussian 参数的 logarithm 是 \(k+O_{\rm fixed}(1)\)，故每个固定阶 \(j\) 的 homogeneous \(p_j(w_{k,J})\) 满足 8155–8161 行的可和及超多项式 tail 界。固定 elementary row/slot/ideal polynomial count 后，先删 whole Gaussian annuli；不会删一部分 tuple 以获得虚假的小 seminorm。

对 retained annuli，smooth calculus 对 (6) 一次性 Fourier inversion；slot ratios 是变量，不是分别选取 measure 的标签。因此当前全部 rows 和 active tuples 共用一个密度，separated slot coefficients 仍 bounded、product-form 且 row-independent。完成尺度为
\[
 N_*=1+\ell'+\theta_N,\qquad
 |\theta_N|\le\kappa_{\mathrm G}+O_{\rm fixed}(1/\log Z).             \tag{7}
\]
尺度重心只变化 smooth test；原 \(q_c^{-1/2}q_n^{-1}\) normalization 不变，不能多添一个 \(e^k\) 幂（8195–8197 行）。weighted separation norms 对 \(k\) 可和，并支付固定 norm-twist height cost。

这样得到的 row ball \(q_m\ll Q\) 只依赖固定 rescaled tuple，独立于 surviving active tuples 和 dual variables；(5) 的比较常数统一。反射能量的系数独立性、实际 annuli 和 bounded-length 条件全部成立。

## 4. 变量 \(\ell\) 的 completed-row 范数证明

取 \(f=\rho=1\)。反射 dyad 使用源的 \(O,H,A_0,S_0,N_0,B_0,z_a,v,\ell_b,e_\lambda\)，以 \(\varepsilon_Z=O_{\rm fixed}(1/\log Z)\) 收集固定 annular/conductor offsets。源的实际 norm 比较逐字给出
\[
 H\le M'-O+\varepsilon_Z,\qquad
 \Delta_H=M'-O-H\ge-\varepsilon_Z,\qquad
 2A_0\le O+\varepsilon_Z,\quad N_0\le A_0,\quad z_a\le\ell'.          \tag{8}
\]
这里没有把 \(H\) 设为 \(M'-O\)；supported row part 可以有正长度。

通用反射 lemma 的 retained length 和 energy 是
\[
\begin{split}
 T_d&=2H+2A_0+2z_a-1-\ell'-\theta_N-N_0-3B_0,\\
 E_{\rm ref}
 &=O/2+\max(H,v+\ell_b)-S_0-B_0+z_a-s_{\rm hyb}
   -\ell_b-\frac{2e_\lambda}{3}
   -\frac12(T_d-y)_+,\\
 s_{\rm hyb}&=\min\{v,z_a,(v+z_a)/3\},\qquad
 y=v+3\ell_b+e_\lambda\le T_d+\tau_{\rm ref}.                       \tag{9}
\end{split}
\]
它包括一次 powerful-part 数量 \(Z^{O/2+o(1)}\)；不可再计该因子。负的 \(e_\lambda\) 仅 \(O(1/\log Z)\)，subunit \(n,b\) ranges 为空或 bounded boundary；所有 unit dyads 被保留。

关键的 \(M+\ell=1\) 推论没有使用 \(\ell=1/6\)：
\[
 M'+\ell'-1=-3d,
\]
\[
\begin{split}
 T_d-(H-3d)
 &=H-M'+2A_0+2(z_a-\ell')-N_0-3B_0-\theta_N\\
 &\le 2\varepsilon_Z+|\theta_N|.                                 \tag{10}
\end{split}
\]
这就是源 8246–8250 行在一般 \(\ell\) 下的正确版本。对 retained dyads，(9)(10) 及 unit lower bounds 给
\[
 \max(H,v+\ell_b)=H+
 O(\tau_{\rm ref}+\kappa_{\mathrm G}+\varepsilon_Z).                \tag{11}
\]
whole-dual-dyad tail 仍先在原未 separated sum 由 lattice-kernel-tail 去除（7892–7914 行）。对 retained dyads，kernel 实际坐标的 multiplicative identity（7864–7868 行）不变；common-profile 先提取
\(\min\{1,Z^{(y-T_d)/4}\}\)，经 Minkowski 才平方成
\(Z^{-(T_d-y)_+/2}\)。仅此之后把 positive separated row norm 扩为 ball。不能在扩大得到的 shorter rows 重算 kernel scale（7916–7926、8226–8233 行）。

记全部预先规定的 small losses 为
\(\varepsilon_* = O(\tau_{\rm ref}+\kappa_{\mathrm G}+\varepsilon_Z)\)。
对 (9) 分两支。

**第一支：\(s_{\rm hyb}=z_a\)。** 消去 \(+z_a-s_{\rm hyb}\)，drop 非正项；unit lower bounds 支付可能的 \(e_\lambda<0\)。由 (11)
\[
 E_{\rm ref}\le O/2+H+\varepsilon_*
 =M'-O/2-\Delta_H+\varepsilon_*
 \le M'+\varepsilon_*.                                          \tag{12}
\]

**第二支：\(s_{\rm hyb}\ne z_a\)。** 同源 8281–8289 行，
\[
 s_{\rm hyb}+\ell_b+\frac{2e_\lambda}{3}
  +\frac{(T_d-y)_+}{2}
 \ge\frac y4+\frac{(T_d-y)_+}{2}-O(\varepsilon_Z)
 \ge\frac{T_d}{4}-O(\varepsilon_Z).
                                                                    \tag{13}
\]
两种 \(y\le T_d,y\ge T_d\) 都成立；没有要求 \(T_d\ge0\)。精确 saving identity 为
\[
\begin{split}
 O/2+\Delta_H+S_0+B_0+T_d/4
 ={}&\frac{2M'+2z_a-1-\ell'+2\Delta_H-\theta_N}{4}\\
 &+\frac{2A_0-N_0+B_0+4S_0}{4}.                                  \tag{14}
\end{split}
\]
第二行非负。用 \(z_a\le\ell'\) 得
\[
\begin{split}
 E_{\rm ref}
 &\le M'+\frac{1+3\ell'-2M'-2\Delta_H+\theta_N}{4}
      +\varepsilon_*\\
 &=M'+\frac{5\ell-1+d-2\Delta_H+\theta_N}{4}
      +\varepsilon_*.
                                                                    \tag{15}
\end{split}
\]
**这里才是原 proof 的实质性改动：** 源 8308 行的 \(d-1/6\) 必须改为 \(5\ell-1+d\)。固定 \(\ell=1/6\) 的原 row norm statement，不能作为本次参数的直接前件。

结合 (12)(15)，处理 \(\Delta_H\ge-\varepsilon_Z\)、unit offsets，并用 Gaussian 的共同 weighted density、Minkowski、dyadic summation，得新的有效结论
\[
 \sum_{0<q_m\ll Q}|B^J_{m,\sigma}(Z)|^2
 \ll Z^{M'+R_\ell(d)+\epsilon},\qquad
 R_\ell(d)=\frac14(5\ell-1+d)_+.                                  \tag{16}
\]
选择顺序是：先固定最终 \(\epsilon\)，再选 \(\tau_{\rm ref},\kappa_{\mathrm G}\) 和 component losses，最后增大 \(Z\) 阈值使 \(\varepsilon_Z\) 可吸收；固定 Fourier height 阶数由有限 seminorm 支付。输出幂不依赖 surviving-slot mesh。

### 空 marks 与 empty endpoint

若 \(J^c=\varnothing\)，实际 endpoint 是 \(d=\ell\)，不是 \(d=1/6\)。此时 \(z_a=0\)，非负 nominal dual centers 使 \(s_{\rm hyb}=0=z_a\)，属于 (12) 的第一支；bounded negative unit offsets仅改变 \(\varepsilon_Z\)。因此空列表实际上有更强的
\[
 \sum |B^J|^2\ll Z^{M'+\epsilon}.                                \tag{17}
\]
反射的 empty active radical、unit annulus 与 source dual support 均被原通用前件允许；没有除以 active length 或要求存在 active prime。

也可直接用源 lem:unmarked-completed-moment（3138–3168），其一般 \(M,N\) 范围给 Gaussian 尺度 \(Z\) 的
\[
 O/2+\max\{M'-O,\,2M'-O-1\}\le M'
\]
因为 \(M'=1-3\ell<1\)。这独立确认 (17)。即使对空 endpoint 只用较粗的 (16)，最终 low 支付仍成立；不需要声称每个 \(J\) 都有原来的无损 \(M'\) row bound。

若 surviving lists 非空但某个反射分支的 active 列表为空，其 \(z_a=0\) 同样落在第一支；inactive-list mass 由 \(\sum q_p^{-1}\ll Z^\epsilon\)（7807–7816 行）支付，不能额外计 active tuples。

## 5. Additive Gram、Cauchy 与所有 rescaled subsets 的支付

由 (5)
\[
 P_a=\frac{Y'^2}{Q}=q_{b_*}^{-1}Z^b.                             \tag{18}
\]
当前参数对所有 \(0\le d\le\ell\) 有严格、固定的正下界
\[
\begin{gathered}
 M'\ge M-2\ell=\frac{9997}{20000}>0,\\
 l_x-d\ge\frac{7497}{40000}>0,\qquad
 l_y-d\ge\frac{12497}{40000}>0,\\
 l_y-d-\frac{11b}{6}
 \ge\frac{9991}{120000}>0.                                      \tag{19}
\end{gathered}
\]
故可选一个 fixed-data 阈值，使 \(Q,Y',P_a\ge1\) 对全部 moving tuples 统一。特别 \(P_a\ge1\) 只需 \(Z\ge q_{b_*}^8\)。最后一个余量给
\[
 \frac{Y'}{P_a^{11/6}}
 =q_{b_*}^{11/6}r_J^{-1}
   Z^{l_y-d-11b/6}\longrightarrow\infty
\]
统一成立，因而 \(P_a^2/Y'\ll P_a^{1/6}\)。

原 \(A_{m,\sigma,v}(Y')\) 的 coefficient 恰是 prop:probe-gram 允许的固定 ray 系数；没有由 completed side 传进任意 row-dependent coefficient。用该 proposition：
\[
 \sum_{q_m\ll Q}|A_{m,\sigma,v}(Y')|^2
 \ll (1+|v|)^{J_{\rm Gr}}(Q/Y')P_a^{1/6}Z^\epsilon.               \tag{20}
\]
原 low separation 中 \(\Omega(q_m/Q)\)、\(\xi(m)\) 与 norm phase bounded；Cauchy 与 (16)(20) 及
\(\int(1+|v|)^{J_{\rm Gr}/2}|\widehat W_0(iv)|\,dv<\infty\)
给每个固定 rescaled tuple 的未乘外系数表达式
\[
 \ll Q^{-1/2}[(Q/Y')P_a^{1/6}]^{1/2}
 Z^{(M'+R_\ell(d))/2+\epsilon}
 \ll Z^{(l_x-d)/2+b/12+R_\ell(d)/2+\epsilon}.                    \tag{21}
\]
这一步共同 completed profile 的 Fourier 变量与 outer \(v\) 的高度都由已固定 smooth seminorm 支付；原 row coefficient 不因频率分离而失去独立性。

对 \(J\) 的 rescaled tuples，elementary ideal count 为 \(O(Z^{d+\epsilon})\)，原外系数 \(q_{p_J}^{-3/2}=O(Z^{-3d/2})\)。所以总幂相对于 \(l_x/2+b/12\) 增加
\[
 F_\ell(d)=-d+\frac18(5\ell-1+d)_+.                             \tag{22}
\]
本次 \(\ell<1/5\)，故 \(5\ell-1<0\)，对 \(d\ge0\)
\[
 (5\ell-1+d)_+\le d,\qquad
 F_\ell(d)\le-\frac78d\le0.                                     \tag{23}
\]
所有可能的正 row loss 因此由**原 rescaled coefficient、tuple count 与 \(X'\) 变短三项**完整支付，既不是被忽略，也不是另设原无损 row theorem。\(d=0\) 的原全 marked summand 决定最终指数；空 surviving endpoint 更有 (17)。

给各 component losses 分配最终 \(\epsilon\)，将 finitely many \(J,\sigma,\theta\)、实际 row/dual dyads 及共同 Gaussian separation densities 求和，得到 (3)。这完成新 geometry 的 compensated low proof，条件依赖仅是 §2 的确切通用结果。

## 6. 下一接口及不能转移的内容

新 low exponent 精确为
\[
 l_x/2+b/12=\frac3{16}-\frac1{80000}.                             \tag{24}
\]
若在**另行支付 high representation 和全部 error estimates**之后，同一 probe 的 principal normalization 仍为其几何公式
\[
 C_\ell(s)=l_x/2+s-1+h/6,
\]
则 (1) 给
\[
 C_\ell(s)=s-\frac{11}{16},\qquad
 C_\ell\!\left(\frac78-\frac1{80000}\right)
 =\frac{14999}{80000}.                                          \tag{25}
\]
这里 (25) 只是精确 geometry/algebra 接口；本报告没有由 low estimate 推出新的 \(L\)-函数无零区域。

原文参数未覆盖的位置已经明确：8079 行写 \(d\le\ell=1/6\)；8111–8121 行的 row lemma 及 8564–8575 行的 low proposition 都以固定 geometry 为陈述范围；8308、8325–8327 行使用 \(d-1/6\) 和原 empty endpoint；8593–8597 行列举旧的具体正余量。新证明必须使用 (16)、(17)、(19)、(22)，不能把这些固定陈述静默改参。

已经支付：\(M+\ell=1\) 的一般代数、\(T_d\le H-3d+o(1)\)、actual residual dyads、原全部 zero masks、empty marks 与 unit ranges、Gaussian whole-annulus tails、joint common density、完整 rescaled tuple loss以及 additive Gram 的全部尺度条件。

仍须另付：新的 high-side 主信号与局部 compensation、plain/inverse moment 的新几何准入、全部误差族的统一 margin、continuation criterion 的同一个物理 probe 合同，以及与 Weil 正性/几何来源的实际比较。有限 Fraction 参数核对只认证本报告的有理代数，不认证这些无限分析前件。本任务没有修改外部论文、主稿或旧脚本，也没有构建外部论文。
