# 447 独立终审：更大固定槽的连续证书与同源延拓

日期：2026-10-07。独立审查人：radial_review。
结论：**限定 PASS [T/R]**。已全文读取最终 447，独立重算原显示指数，未依赖网格判断正性；安全有理参数和 critical 全族共同 gap 的实际准入及延拓均通过。原外部 [R] 的整链重证、Lean kernel certification、RH/RR 或比例改善不在本次验收范围内。

## 1. 绑定与独立方法

最终主稿 notes/447-larger-slot-discriminant-and-critical-strip.md：
canonical LF SHA256
35d0f11bd822bdf7862dc821f2b02628b3a41778ff9633cb27a9bcbf5d3431b1
（10843 字节）。全文核对后，确认无意外 LaTeX 控制字符。

已全文读取独立输入报告 reviews/2026-10-07/hybrid-next-boundary-certificate-optimization.md，最终 canonical LF SHA256
125feb225c7a8db0ca8e4097f6949d7496ec12d7106c444fe45f8bea53b44fa6
（14029 字节）。

准确外部 [R] 仍是 OpenAI/math 提交 adc7f1241b42e322a6451854ab7e4b4c146bf78a 的
preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex；
本地 canonical LF SHA256
42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3，
766316 字节。该来源只读，未编译、修改或重建形式化。

沿用已读、已绑定的 441–445：

| 稿件 | canonical LF SHA256 |
|---|---|
| 441 | dffcaa1899358d581fe3d6438ee87d075588e5e7e8f41ccd8a629fe5c31be0dd |
| 442 | 87abb4dd86ccae9b8209e030606413ef2b8682631f9c4d9195afdd808ad1b6b7 |
| 443 | 79bfb7f8770eb3865ccdfe0da416388b2182383bd425fd57b39f520b3fd59bc6 |
| 444 | 47686e9b6b28239562e83e9ab5199349458fd19bf9abbe45cca67df8c876957c |
| 445 | 99ac005976c7c22934b5597c25b0d6fc6d7f3f4d9be604f8cbd53e130eae0f2e |

本次从显示的 \(E_t\) 和实际 \(R_*\) 重新展开，用内存中的符号恒等式及 Fraction 核对精确分数。正性结论来自下列全区间代数证明；未调用旧审计、未写数值网格或将有限检查冒充无限分析。

## 2. 从原实际指数重新导出二次式

取
\[
 \ell=1/6+t,\quad l_x=17/48-t/2,\quad
 l_y=23/48-t/2,\quad h=13/16+3t/2,\quad
 \sigma=7/8-t/4.
\]
bootstrap \(\sigma<\beta_*\le7/8\) 给固定 \(\kappa_{\rm eff}=3/4\)、
\(\Delta_{\rm eff}=0\)。实际非 floor bin 的
\(1/50<\delta\le3/4\)，\(q\in[0,\delta/2]\)。
以下正性在更大的 \(0\le\delta\le5/6\) 范围成立，不需物理行同时达到 count 包络的极值。

令 \(x=q/\delta\)、\(y=1/2-x\in[0,1/2]\)，
\[
 D=(37+34y)/18,\qquad P=(7+18y+8y^2)/9,\qquad
 J=(5/6-\delta)D+\delta P,
\]
\[
 R_*=1-\delta+\frac{(5/6-\delta)\delta P}{2J}.
\]
这是 443 准入的 actual row count；不是新造 nominal row 集。
\(D\in[37/18,3]\)、\(P\in[7/9,2]\) 给
\[
 35/54\le J\le5/2.
\]

444 的同源行指数在 \(d=h\) 为
\[
 E=K_\sigma+(1/2+\ell)\delta+\ell q-h(1-R_*),
 \qquad K_\sigma=-1/48+5t/4.
\]
代入 \(q=\delta(1/2-y)\) 后准确合并为
\[
 E_t=-1/48+5t/4-(1/16+y/6+ty)\delta
 +(13/32+3t/4)(5/6-\delta)\delta P/J.
\]
这里已经相对 \(C(\sigma)\)；\(-\sigma'\) 的贡献已算入，不能再扣 \(t/4\)。

直接展开
\[
 p_t=10368J(-E_t)=A_t(y)\delta^2+B_t(y)\delta+C_t(y)
\]
得到
\[
\begin{aligned}
 A_t={}&2448+6288y+4512y^2+1536y^3\\
       &+t(6048+2304y+8064y^2+9216y^3),\\
 B_t={}&-1896-3016y-208y^2+t(11520+3360y-960y^2),\\
 C_t={}&370+340y-t(22200+20400y).
\end{aligned}
\]
每一系数均与输入报告匹配。独立计算的
\(Q_t=4A_tC_t-B_t^2\) 五系数如下：

| y 次数 | 系数 |
|---|---|
| 0 | \(28224-164747520t-669772800t^2\) |
| 1 | \(1198848-664266240t-775526400t^2\) |
| 2 | \(5344448-877278720t-893260800t^2\) |
| 3 | \(7154944-484362240t-1469952000t^2\) |
| 4 | \(2045696-113203200t-752947200t^2\) |

注意 \(p_t>0\) 可以覆盖 \(\delta\in\mathbb R\)，但从 \(p_t\) 返回 \(-E_t\) 时必须另用实际域的 \(J>0\)。本报告不把任意 \(\delta\) 上的 polynomial 正性误当作任意 \(J\) 的指数正性。

## 3. t=1/5900 的显示连续证书

令 \(N=5900\)、\(A_N=NA_t\)、\(B_N=NB_t\)、\(C_N=NC_t\)。独立整数系数为
\[
 A_N=14449248+37101504y+26628864y^2+9071616y^3,
\]
\[
 B_N=-11174880-17791040y-1228160y^2,\qquad
 C_N=2160800+1985600y.
\]
相反判别式 \(Q_N=4A_NC_N-B_N^2\) 的五系数为
\[
 (9797299200,\ 37811952537600,\ 180863397171200,\
 246204393472000,\ 70542025932800).
\]
全部严格正，故 \(Q_N(y)>0\) 对全部 \(y\ge0\) 成立。与此同时 \(A_N(y)>0\)，完成平方合法。

仅用 \(Q_N(y)\ge Q_N(0)\) 还不能在分母中擅自把 \(A_N(y)\) 换成 \(A_N(0)\)。必须先证明 ratio inequality。独立展开
\(A_N(0)Q_N(y)-Q_N(0)A_N(y)\) 给系数
\[
\begin{aligned}
(&0,\ 545990785044553728000,\
2613079188901203148800,\\
&3557379462630329548800,\
1019279227125458534400).
\end{aligned}
\]
全部非负、非零次项严格正。因此
\[
 p_t=
 \frac{A_N}{N}\left(\delta+\frac{B_N}{2A_N}\right)^2
 +\frac{Q_N}{4NA_N}
 \ge\frac{Q_N(0)}{4NA_N(0)}
 =\frac{85046}{2960089}.
\]
在 \(y=0,\delta=116405/301026\) 实际达到这个 polynomial 下界；
\(1/50<\delta<3/4\)。这不是说物理 bad rows 达到了 count 包络。

结合 \(J\le5/2\)，得到
\[
 -E_t\ge\frac{42523}{38362753440}
 >\frac1{1000000}.
\]
两个分数的精确正差为
\[
 \frac{26001541}{239767209000000}>0.
\]
所以可固定统一 \(m_{\rm ad}=10^{-6}\)。这个界覆盖连续 \(y,\delta\) 矩形；证明不以样点或网格密度为依据。

## 4. 所有频率、外行与 supply

新几何的全部精确分数独核一致：
\[
 \ell=2953/17700,\quad l_x=25069/70800,\quad
 l_y=33919/70800,\quad h=19181/23600,\quad
 \sigma=20649/23600.
\]

主双留数仍是 \(w=1,z=1/6\)。不是把 Euler pole 改到 \(z=\ell\)。
\[
 l_x/2-1+h/6=-11/16,\qquad
 C(s)=s-11/16,\qquad C(\sigma)=553/2950.
\]
441 的完整 low exponent
\((1-\ell)/4-b/6\)
同样恰为 \(553/2950\)，因为 \(b=1/8\)。441 所核的
\(\ell\in[1/6,1/5]\) general reflected-energy、empty marks、actual \(T_d/H\)、joint profile、masks、Gram 和 tuple 亏损继续适用；没有照引原固定 low proposition。

selected 非 floor \(d\in[1/2,h]\) 的 slope 为
\[
 R_*+\delta/2-17/50\ge33/50-\delta/2>0,
\]
故 endpoint 控制全部实际频率。
floor 用自己的 \(R=1,\delta_0=1/50,q\le1/100\)，得
\[
 E(h)\le-7/1200+(32/25)t=-9941/1770000<0.
\]
中间 \(d_{\min}\le d\le1/2\) 的共同 no-slot 包络
\(R=76/75-2\delta/3\)
覆盖 floor 与 nonfloor，slope 为 \(101/150-\delta/6>0\)。几何导数界 \(177/200\) 给
\[
 E(d)\le-49/14400+(177/200)t=-1171/360000<0.
\]
no-slot 只是不用 physical prime factor 做 row moment；不能删去 full tuple 的 prime slots。

固定
\(\zeta=m_{\rm ad}/32=1/32000000\)；
上端 extension 成本最多 \(2\zeta=m_{\rm ad}/16\)，所以全部 moderate 行至少留
\(15m_{\rm ad}/16=3/3200000\)
在 real losses 之前。
实际供给由
\[
 5\ell-h=1517/70800>\zeta,\quad h+\zeta<1,\quad
 \ell/h-7/37=34243/2129091>0
\]
支付。更具体
\[
 \ell/(h+\zeta)-1/5=121359823/23017200885>0.
\]
因此固定 even \(K\)、actual whole-slot rounding、strict marked/plain widths 和 centered pool 隔离仍可照 443 的 general proof 选择；只有 \(d\ge1/2\) 才选 primes，\(w_i\le2\ell_i\)，不偷用小行的名义总供给。

完整小行的相对 \(C(\beta_*)\) 指数为
\[
 h(13/75)-l_y/2+(63/50)d_{\min}
 =-20311/236000<0.
\]
若用更粗 \(2d_{\min}\)，也仍为 \(-92823/1180000\)。
该参考幂不能静默换成 \(C(\sigma)\)；bootstrap 只允许多花至多 \(t/4\)，仍不影响负余量。
大行在固定 \(\zeta\) 后选固定 \(z_\infty\)，
\[
 B_0=l_x/2+1+l_y=78169/47200
\]
而 \(-\zeta z_\infty\) 可支付任何预定 fixed margin。即使所需 \(z_\infty\) 很大，也是固定 real box 与 finite seminorm orders，不随 Z 或 moving rows 变化。

## 5. 同源解析与全族 continuation 的再次准入

局部 identity、无商 full tuple、dynamic main/error 分解和 strict labels 共用一次 numerator conductor 的推导均不依赖 \(\ell=1/6\) 的固定数值；只有槽的 fixed finite count 与 fixed profile 改变。原完成尺度的 compensation 和 zero-on-nonunit masks必须保持，不能改为某个单独易估计的 high integral。

新的 D2 下界 \(\sigma=20649/23600\) 给
\[
 c_b=\min(6\sigma-401/100,\sigma-3/50,47/50)
 =19233/23600>0,
\]
\[
 c_r=\min(\sigma-1/20,3\sigma-3/2)
 =19469/23600>0.
\]
所以 full unselected positive majorant、ramified divisor product、neighborhood holomorphy 和 all-height tuple bound 仍支付。主行的四错误指数中最大值仍是 \(-\sigma\)，故 \(B_p=-1+O(Q^{-\sigma})\)，相对主槽误差可取任意
\(0<\mu<\sigma\min_i\ell_i\)。
\(\sigma+1/2>1+1/3\)，小行 D1(1/3) 修补仍有严格余量。

principal 两个轮廓 margin 为
\[
 m_w=33919/1416000,\qquad m_z=19181/14160000,
\]
都严格正。fixed ray normalizer 最终非零，inverse 为 subpower；target 后 fixed S enlargement继续缩小同一个 product-error majorant。所有表达式及 normalization必须使用同一最终 \(S,c_S,A_T,H_\eta\)。

general plain mesh 的原量词只依赖 bounded lengths 与 requested loss。故先固定 \(m_{\rm ad}\)、count/capacity losses、mesh、rounding，再选 even \(K\) 和 actual disjoint windows；K 固定后才取
\(\mu=\sigma\ell/(2K)\)。
principal 与 central 分别支付自己的小损失，不用依赖 K 的 \(\mu\) 倒选 mesh。

取
\[
 m_0=\min\{m_{\rm ad},m_w,m_z,\mu,20311/236000\}>0,\qquad
 m=m_0/4.
\]
central extension 后 \(15m_{\rm ad}/16\)，再扣 \(m_{\rm ad}/4\) real budget仍大于 \(m_{\rm ad}/2\ge m_0/2\)。principal、小行和大行也可留 \(m_0/2\)，最后共同 \(m\) 不倒转参数次序。

目标后固定 arithmetic datum、最终 S、finite internal moment/Sobolev/height orders，得到 N-independent \(A_\eta,B_\eta\) 和 literal detector ceiling。全部 retained variables 使用原 single cumulative buffer；之后选 \(\tau_\eta\)，再选 external tail order并提高阈值。\(J_\eta,f_\eta\) 不含 \(T_1\)。445 的 late-height proof因此给共同
\(\sigma_{\rm hi}=m_0/8>0\)；
低侧共同 \(\omega=(\beta_*-\sigma)/2\)。
同一个 Mellin endpoint/Fourier inversion/supremum 未达到的反证可重放，未跨目标零点或假设待证新半平面已无零。

此节认证的是上述 general [R] 之后的再准入，不是重证原 source 的全部矩或其形式化。AF 比例没有进入 count 节省。

## 6. 包络临界与失败见证的准确含义

另独核输入报告的 family threshold：
\[
 Q_0(t)=28224-164747520t-669772800t^2.
\]
它的唯一正根 \(t_c\) 的显示 closed form 正确。对 \(0\le t<1/5000\)，A 的 coefficient comparison 及其他 \(Q_i\) 的强正下界使同一个 ratio argument 生效。因此 \(t<t_c\) 给正 continuous polynomial margin，\(t=t_c\) 的附加 margin 为零。这里仅是相对 \(C(\sigma)\) 严格负指数证书的极限，不能误写成 actual high 或 continuation 无法启动的极限。

critical 时 \(Q_0=0\)、其余 \(Q_i>0\)、\(A_t>0\)，故 \(E_\sigma\le0\)。唯一等号点 \(y=0,\delta=(1896-11520t_c)/(4896+12096t_c)\) 仍在实际允许矩形内。即使相对 \(C(\sigma)\) 没有额外负 margin，反证中共同 \(\Delta_{\rm new}=\beta_*-\sigma(t_c)>0\) 仍在目标前固定，所以相对 \(C(\beta_*)\) 有 \(E_\beta\le-\Delta_{\rm new}\)。可取 \(\zeta\le\Delta_{\rm new}/32\)、real loss 小于 \(\Delta_{\rm new}/4\)，先选 count/capacity/mesh/rounding，再 K/windows、\(\mu\)、小 e，仍留至少 \(\Delta_{\rm new}/2\) central saving。principal/outer margins 照常保留，随后取它们与 \(\Delta_{\rm new}\) 的正最小值作共同 high margin，late-height 与全族 Mellin 量词不变。原 source 的目标无关选择允许依赖这个共同反证 gap。因而 critical 也可支付 continuation，不能把额外 margin 为零误作阻断。

在 \(t=1/5800,y=0,\delta=57215/147963,q=\delta/2\) 独立精确代入，得到
\[
 J=2164165/1775556,\quad
 p_t=-29297/1430309,\quad E_t=29297/18075106080>0.
\]
点位于真实允许的 \((\delta,q)\) 矩形，但不证明物理 bad rows 同时达到 upper envelope，也不证明存在相应 L 零点。它说明相对 \(C(\sigma)\) 的负证书在该点失效；对任意小共同反证 gap，不能仅靠减小 error epsilon抵消这个固定正指数。它不排除另行利用更大的实际 gap、更强 count/gain 关联或新 high 估计。

## 7. 最终 447 全文与 critical 证明验收

447 §1–§3 的代数根、主留数、显示指数、A/B/C/Q 系数、ratio argument 和安全有理 margin 与以上独立推导一致。critical 的 irrational fixed geometry 不触发原一般引理的额外限制：所有槽长度和 scale exponents本来就是固定实数；小数只作定位。精确有理夹逼给 \(1/5842<t_c<1/5841\)，证明没有以 rounded decimal 判定符号。

447 §4 的核心比较
\[
 E_{\beta_*}(d)=E_{\sigma_c}(d)-\Delta
\]
准确。selected 的正 frequency slope使 \(E_{\sigma_c}(d)\le0\) 控制全部 \(1/2\le d\le h\)；floor 与中间独立 count 仍为实际包络，不借 critical 等号点赋予 floor witness。用 \(t_c<1/5800\) 独核三项 strict coarse bounds：
\[
 -7/1200+(32/25)(1/5800)=-4883/870000<-1/200,
\]
\[
 -49/14400+(177/200)(1/5800)=-8483/2610000<-2/625,
\]
\[
 -79/800+(51/100)(1/5800)+63/5000=-12479/145000<-2/25.
\]
实际 \(t_c\) 的指数更小。

最终主稿正确允许 bootstrap endpoint 的等号：
\(\zeta=\Delta/32\le t_c/128<1/(5800\cdot128)\)。
若 \(\beta_*=7/8\)，第一项可以取等号；它不影响供给、\(h+\zeta<1\) 或上端 cost \(2\zeta=\Delta/16\)。selected critical high 先留 \(15\Delta/16\)，而 floor/mid/small保留显示的独立余量。所有 moderate/outer/principal rows都由同一原 physical expression 的合同覆盖。

447 §5 重放新 D2、D1(1/3)、full tuple、same-source local identities 与 actual detector hypotheses 合法。其简化域界 \(c_b=\sigma_c-3/50>81/100\)、\(c_r=\sigma_c-1/20>82/100\) 都由实际 min branches推出，不是任意选更强 decay。\(B_p\) 的最弱 error exponent仍为 \(-\sigma_c\)，主槽误差依 fixed \(\ell_i>0\) 支付。principal nonvanishing使用 Euler product-tail majorant，不使用待证的新无零半平面。fixed ray、normalizer 和所有 probe/signal项均使用目标的同一最终 S。

447 §6 的 target-independent 顺序严格可行：反证先固定共同 \(\Delta>0\)，以它请求 count/moment/capacity/rounding losses与 mesh；再选 finite even K/windows；此后才取 \(\mu=\sigma_c\ell/(2K)\) 与 amplitude/prime/e losses。没有用 \(\mu\) 倒选 K 或 mesh。critical 的预算允许依共同 \(\Delta\) 变小，原 source 16219–16324 正是这种先共同 gap 后 target 的量词。原 plain lemma 12572–12578 的 mesh 独立于 arithmetic datum 和 K，故全族范围没有退化为逐目标改 slot geometry。

把 central real costs压至 \(\Delta/4\) 后仍余至少 \(\Delta/2\)。取主稿显示的
\[
 m_0=\min\{\Delta,m_w,m_z,\mu,1/200,2/625,2/25\},\qquad m=m_0/4
\]
不会要求重选内部 mesh；common high saving为 \(m_0/8>0\)。target 后固定 arithmetic data、internal orders、N-independent \(A_\eta,B_\eta\) 和 literal height ceiling，之后才 \(\tau_\eta\)、external \(N_\eta\)、threshold。所有 Fourier variables保留 single cumulative budget，函数 J/f不含 cutoff。因此 source late-height 6521–6579 的每个前件和 continuation criterion 400–501 的全部量词满足。

low 的 \(\omega=\Delta/2\) 与 high 的 \(m_0/8\) 都在目标前固定；共同 \(\epsilon_*=\min(\Delta/2,m_0/8)>0\) 才允许从全族 supremum选出产生矛盾的某个目标。不同目标的 constants、S、cutoff和阈值可以不同，不能把它们与共同 exponent混同。小 Z 向右移线、Mellin/Fourier识别、H非零、finite Euler deletion和quadratic transfer与445相同，均无需跨目标零点或令supremum被达到。

最终没有未解决的本稿数学返修项。PASS仅表示：接受确切 source generic [R] 和全族旧7/8 bootstrap后，447的新安全有理/critical参数证明完整成立。没有认证原[R]整链、形式化或实际四点算术的独立正确性；447末段也没有把232–240的开放响应预算冒称闭合。本轮只新增并完成本报告，没有修改任何旧稿或外部 math。
