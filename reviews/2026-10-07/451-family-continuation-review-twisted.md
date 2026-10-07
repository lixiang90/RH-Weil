# 451 全文独立审查：实际 κ 反馈、三次证书与全族 continuation

2026-10-07。审查人 `/root/twisted_research`。结论：**限定 PASS [T/R]**。
本报告重新审查451全文及其真实物理、算术和解析接口，不以450的 lower-κ
审查代替边界结论的审查。在下列准确原输入 [R] 成立的条件下，451的
新纸面推导成立；没有发现阻断该相对推导的数学缺口。这里的 PASS
不是源整篇证明、外部形式化 kernel、RH 或简单临界线比例的独立认证。

## 1. 实际文件、哈希和审查范围

所有 SHA-256 按 UTF-8、CRLF/CR→LF 后计算，不删除其他字节。

| 文件 | canonical LF SHA-256 |
|---|---|
| [451正文](../../notes/451-kappa-feedback-cubic-boundary-and-family-continuation.md) | `17ce7fea8c881ebd4034657b7039e99897d4ff9532348993ba329c46e3c4d487` |
| [450正文](../../notes/450-plain-kappa-extension-and-actual-capacity.md) | `f16807e0f80461e3005b3173e313218b00f5f86abfa860a4ead79e425dd6bee5` |
| [精确脚本](../../scripts/hybrid_kappa_feedback_exact_audit.py) | `e03d6536378fff4b51625ab71fa5eace9fcbf4fe1156ccb6ae048f03bf96bc68` |
| [保存输出](../../output/hybrid-kappa-feedback-exact-audit.json) | `309f275701a1d96c245eb067d49b00598df4af8e380d220944de250fd2e9d7ba` |
| [lower-κ完整推导](hybrid-critical-count-witness-research.md) | `a1a6146b8f5e0b82b0e7e642e323398aece00d0a3488cce3d6f146974332dff8` |
| [本审查人的450全文审查](450-plain-kappa-extension-review-twisted.md) | `0051dcd82296aefc5cfd23d19cce3a8ce0b09c3c8e9370fad933e5ab8581c61a` |
| [449自由b正文](../../notes/449-free-b-compensated-geometry-and-optimal-relative-boundary.md) | `2d4b37628d6f68229fd687d6ac84c2ba03cb7223c412df5e00c07a0ff5e1a3bd` |
| [445明确输入与全族合同](../../notes/445-conditional-strip-improvement-and-family-continuation.md) | `99ac005976c7c22934b5597c25b0d6fc6d7f3f4d9be604f8cbd53e130eae0f2e` |

451正文为10207个 canonical UTF-8字节、244行。精确脚本为10637个
canonical字节。保存输出的原始字节数4630，canonical字节数4414；两种
计数不同源自CRLF，不是输出数据不同。

原源实际读取于
`E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`，
commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`。重新计算其 canonical
LF SHA-256 为
`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`，
766316字节，与451绑定一致。没有编辑或构建该源。

本轮重新全文读取451、450、449和445，并直接回核源375–505、
4010–4180、6810–6940、7663–7804、8340–8364、8654–8835、
15520–15684、15684–15920、16375–16463。450的原 plain proof
12532–15015及实际计数15105–15475已在本轮先前完整独审，绑定上述
新450报告；本报告另外检查其对451实际参数的应用，而非仅援引其结论。
已对照原 shared-contour、联合error-slot和自由b推导的完整相关章节。

准确 [R] 仍是445 §1展开的输入包：

1. 原 coefficientwise physical probe、Poisson、finite compensation、
   完整局部算术表和 ray 校准；不是任意另造的探针身份。
2. smooth calculus、Gaussian annuli、实际 row sectors、通用 reflected
   energy 和 quantitative additive Gram，包括第三项和全部原 masks。
3. global、fixed-bin及buffered reciprocal、Hecke增长、functional
   equation及完整外尾合同。本文重核新实参数前件，不直接套用旧
   `sigma>=7/8` 的 shared-interface statement。
4. actual witnesses、marked/inverse/recursive moments、sixth-power
   amplification及固定系数类；positive-slot plain原证明的κ范围扩展
   由450重证，仍需这些底层输入。
5. **整个 primitive finite-order Hecke family 的7/8结论**，仅用作
   `beta_*<=7/8` bootstrap。
6. fixed-ray prime asymptotic、有限Euler删除和原二次Dirichlet transfer。

目标族是源中的 `F=Q(sqrt(-3))` finite-order Hecke族；Dirichlet及zeta
结论经所列transfer得到。没有把单个Dirichlet L的零比例当作该Hecke族
的统一坏行计数输入，也没有导数零/L零的互换。

## 2. 三次根、一般 b 最优化和连续证书

我独立以符号展开验证了端点身份、一般 `b` 优化及其极大值，而不只
复跑脚本已有的有限点。

写 `e=ell_*`、`k=kappa_*`，

\[
 c=1/(3k),\quad D=5/2-c+(1+2c)y,
 \quad P=1-c/2+2y+2cy^2,
\]
\[
 J=(5/6-\delta)D+\delta P,\quad
 h=(1+3e+b)/2,\quad K=-1/4+5e/4+b/6,
 \quad W=1/2+3e/2-ey.
\]

对

\[
 R=1-\delta+(5/6-\delta)\delta P/(2J),\qquad
 E=K+W\delta-h(1-R)
\]

逐式清分母，得到451的

\[
 -2JE=A\delta^2-B\delta+C,
\]
\[
 A=-2(P-D)(W-h)+hP,
\quad B=2K(P-D)+\tfrac53D(W-h)+\tfrac56hP,
\quad C=-\tfrac53DK.
\]

这里 `W delta=(1/2+e)delta+e delta x`，`x=1/2-y`；没有丢失
whole-slot mean或第三项，也没有将 `q ell` 误写成 `d q ell`。

独立求 `Q0=4A(0)C(0)-B(0)^2` 的 `b` 极大点，恰得451 §1的
一般有理式。其二阶导数为

\[
 \partial_b^2Q_0=-\frac{3312k^2-936k+67}{864k^2}<0.
\]

分子二次式的判别式为 `-11520`，首项系数正，故这是实际κ范围
内唯一极大点。将该极大点代入得到451显示的 `Q0max`，进一步代入
`k=5/6-e/2`，其中方括号准确成为

\[
 -657e^3+954e^2-21e-20=-p(e).
\]

`p(LO)>0>p(HI)`；在 `[1/6,167/1000]` 上其导数严格负。
故451的有理隔离区间确定唯一指定根。以 `sigma=11/12-e/4`
消元准确给显示的三次边界方程。`b` 在三次商域中的简化式也一致。
旧二次根的有理区间严格在新 `e` 左侧，所以 `sigma_*<sigma_0`；
**旧 sigma_0仅用于这个数值比较，没有作为新反证的analytic bootstrap**。

脚本的商域乘法逐项按
`e^3=(-20-21e+954e^2)/657`约简，逆元由有理线性方程求得；
模7三次无根保证所用商是域。隔离实嵌入的区间Horner包含真实值。
我核对这些运算与输出中的完整有理系数，确认 `A0..A3>0`、
`C0,C1>0`、`Q0=0`、`Q1..Q4>0`。

因此对所有 `y>=0`，`A(y)>0`、`Q(y)>=0`，精确平方完成

\[
 F(y,\delta)=A(y)(\delta-B(y)/(2A(y)))^2+Q(y)/(4A(y))\ge0
\]

证明连续域，实际 `0<=x<=1/2`、`1/50<=delta<=3/4` 上
`J>0`使 `E<=0`。451的“任意实delta”在清分母多项式 `F` 上
成立；外部 `J=0` 点的原有理 `R/E` 未定义，不能赋值，但从未用于
实际rectangle。

等号只能是 `y=0` 和

\[
 \delta_*=(5-9e)/(6+18e)=B(0)/(2A(0)),\qquad R=2/3.
\]

其严格位置在 `(1/50,3/4)`，约0.38858335。临界点确在真实
rectangle内；没有借删去该点取得假严格余量。

脚本复跑149项全部通过，所打印JSON与已保存JSON解析后逐项一致。
49个direct endpoint models是附加恒等式检查；全域结论来自上述
正系数与平方完成，不来自49点采样。

## 3. 实际 κ 的前提和完整 high 反馈

源375–398的上确界定义是整个 primitive Hecke族的实际L零，包含
`1/2`、不包含principal pole；由定义 `Re s>beta_*` 全族零自由。
在反证 `beta_*>sigma_*` 中设共同 `Delta=beta_*-sigma_*>0`。
唯一用到的已证明旧边界是 [R] 的 `beta_*<=7/8`，所以

\[
 k_{\rm act}=2\beta_*-1\in(k_*,3/4]\subset[37/50,1],
 \qquad k_{\rm act}-k_*=2\Delta.
\]

450的positive-slot条件 `beta_*<=(1+k)/2` 对 `k_act` 精确成立。
对 `k_*` 未成立，451没有调用它的analytic moment。因此reference
参数与actual参数的分离是实质性且正确的。

独立微分一般计数包络得到

\[
 \partial_kR_{*,k}=
 \frac{\delta(5/6-\delta)^2x(1-x)^2}{3k^2J_k^2}\ge0.
\]

由 `J_k>=(5/6-delta)D_k`、`D_k>=2`、`delta<=3/4`、
`k>=37/50` 和 `x(1-x)^2<=4/27`，上界为
`625/36963<1/50`，统一于整个actual rectangle。因此

\[
 0\le R_{*,k_{\rm act}}-R_{*,k_*}<\Delta/25.
\]

相对于 **同一个 `C_b(beta_*)`**，端点准确为

\[
 E_{\beta_*}(h)=E_*(h)-\Delta+h(R_{\rm act}-R_*)
 \le-24\Delta/25,
\]

因为 `h<1`。这里没有再扣一次 `7/8-sigma_*`，也没有把带符号
`beta_*-7/8`作为旧原count statement的正容量损失。

直接回核源15726–15840的unfactored exponent、局部error-slot×numerator
联合估计并代入新几何，得到451的全selected范围表达

\[
 E_{\beta_*}(d)=K_{\beta_*}+(1/2+e)\delta+eq-h(1-R)
 +(d-h)(R+\delta/2-17/50).
\]

此处 `q` 是全部物理槽的length-weighted mean；error槽赋 `g_i=0`，
不能重新对positive槽归一化。所有strict ramified labels共用一次
实际numerator conductor deficit，不重复消除同一b-dependent error。
只在whole-bin global/local轮廓完成后作pointwise amplitude/witness分箱，
不会把依赖轮廓的子集合另行延拓。

由 `R>=1-delta`，selected `[1/2,h]` 的 `d` 斜率至少 `57/200`，
最大值在端点。`zeta=Delta/32` 和保守斜率上界2使 `[h,h+zeta]`
最多花 `Delta/16`，保留 `359Delta/400`。中央其他总loss取小于
`Delta/4`之后，仍至少留下 `259Delta/400`，足够最终 `m0/4`。

## 4. 同一物理探针、low与所有非selected行

源6894–6912的物理操作完整保留：

\[
 I_{\eta,\rm mod}=\sum_{(p_i)}\prod_iW_i(q_{p_i}/P_i)
 \sum_J(-1)^{|J|}q_{p_J}^{-3/2}\overline\eta(p_{J^c})
 I_{\eta;p_{J^c}}(X/q_{p_J},Y/q_{p_J},Zq_{p_{J^c}}).
\]

underlying windows在ray/S限制前disjoint；补偿操作不改变其他槽的
原尺度，marking保持原零掩码。有限的是slot tuple/subsets，不是原
completed `c n^3` sums。451使用这一个身份，未添加另一算术信号。

对rescaled subset `d_J`，`M'=M-2d_J`、`ell'=e-d_J`，
`M'+ell'-1=-3d_J`。所有actual tuple norm ratios在固定正紧区间。
相应长度为正，`P_a=Y'^2/Q`随 `Z^b`增长，最终满足Gram前件。
actual residual-row dyads使 `T_d<=H-3d_J+small`；不能用虚拟
`H=M-O`等式替代原不等式。共同Gaussian profile在kernel saving、
平方与正sieve enlargement前固定，保留empty marks和shared primes。

generic reflected energy和第三项Gram组合后，tuple数、原
`q_(p_J)^(-3/2)`及 `X'`缩短共同贡献 `-d_J`。451的

\[
 F(d)=-d+\tfrac12(11b/6-l_y+d)_+
              +\tfrac18(5e-1+d)_+
\]

斜率确实最多 `-3/8`；强all-J gap `l_y-e-11b/6>2/25`
保证所用第一low分支。low exponent为 `(1-e)/4-b/6`，
与 `C_b(sigma_*)`完全相同。它不含κ，故450扩域不会改变low证明。

我核对新参数的有理区间证书：all-J Gram gap、supply gap、floor、
middle和small的各不等式均有严格余量；脚本列出的approx数仅用于
方向说明，判断使用隔离区间上的有理符号。

| 物理范围 | 实际估计和保留的前件 |
|---|---|
| `u=1` | 同一principal双留数及同一normalizer，见下一节 |
| `d<1/100`、bounded非平凡units | 全tuple、D1(1/3)，`E_small<-2/25`；不使用witness |
| floor `a=51/100` | `delta=1/50,R=1`理想数，`E_floor<-1/200`；不虚构actual零见证 |
| `1/100<=d<=1/2` | 原no-slot `R=76/75-2delta/3`，`E_middle<-1/50` |
| selected `1/2<=d<=h+zeta` | actual `k_act` 的count，统一Delta余量如上 |
| `d>h+zeta` | 全绝对tuple和预先固定 `z_infty`，不靠中央count |

450的actual inverse/plain crossing保留 `r>=3/5`、第二inverse
width至少 `1/5`、`m>=1/3`及全部供给 `z_M,z_P<1/5`。
新geometry的 `e/(h+zeta)>1/5`严格满足供给。
选槽仍只在 `d>=1/2`，故 `w_i=ell_i/d<=2ell_i`；fixed mesh和
rounding预算先选，even K后选。actual物理槽与plain内部amplifier
pool分离，没有供给加倍。finite Θ coefficients、同一个presentation、
自然零延拓、whole-product conjugation及inducing-Θ exceptions均保持。
zero capacity、`r>=1`、`m>=1/2`仍走no-slot版本；S-supported
exceptional physical rows在固定目标后有限，留在small/outer处理中。

## 5. Euler、principal和global outer的重新核对

基础local因子不含几何 `b`。由源4013–4145的完整表与defect式

\[
 H_p-1=\frac{D(V+W-VW)-VW+(1-V)(1-W)(P_p^*+D)}{1-D}
\]

在 `D2*(sigma_*)`，good-prime defect为
`O(Q^(-1-c_good))`，其中

\[
 c_{\rm good}=\min\{6\sigma_*-401/100,\sigma_*-3/50,47/50\}
 =\sigma_*-3/50>81/100.
\]

ramified defect为 `O(Q^(-c_ram))`，

\[
 c_{\rm ram}=\min\{\sigma_*-1/20,3\sigma_*-3/2\}
 =\sigma_*-1/20>82/100.
\]

在D1仍保留负 `w` 的 `theta=(-Re w)_+`；乘上 `1-W`的额外费用
也保留。原 `epsilon_H=min(epsilon_0,1/50)`不能改为任意
`epsilon_0`。positive product majorant给正常收敛、所有高度统一
及任意小row幂，删selected factors只删正majorant的因子。

全局continuation的selected因子是原系数式

\[
 G_p=\frac{(\overline\eta(p)Q^s-Q^{-w})(1-V)(1-W)P_p^*
                     -Q^{-w}(1-VW)}{1-D}.
\]

完整tuple在 `H_p`、`P_p`零点仍全纯；不能用quotient给一般轮廓
定义。只有principal或已证明近1的dynamic域可使用 `G_p/H_p`。
all-height scale degree在任何外尾阶N之前固定。

small线 `(beta_*+epsilon,1/2,17/50)`满足
`sigma_*+1/2>4/3`，所以可重证D1(1/3)，未非法套D1(3/8)。
完整off-row `G_p=O(1)`、ramified `G_p=O(Q^1/2)`给
`|full tuple|<<U^epsilon Z^(17e/50)`；原row幂 `63/50`
给451精确small式。large线 `(2,2,z_infty)` 的每个 `G_p=O(1)`
给总幂

\[
 B_0+(h+\zeta)(1+\epsilon)-\zeta z_\infty+\epsilon,
 \qquad B_0=7/4-3e/4+b/4.
\]

先固定 `zeta>0`，再目标前选足够大固定 `z_infty`，最后小epsilon，
即可任意降低该幂。没有把degree反向依赖后选N。

principal correction使用同一个最终S：

\[
 H_\eta(s)=\prod_{p\notin S}H_p(s,1,1/6).
\]

good majorant的相位统一常数使目标前P0可给
`sup_(Re s>sigma_*)|H_eta-1|<=1/2`；目标后扩大S只改善同一个
正majorant。非消失性来自局部表，不来自待证新零自由域。

四个principal local error指数准确是
`-s,-6z,4-5s-6z,1-w-6z`；新域的最弱正衰减为 `sigma_*`。
所以原 `7/8 min ell_i` 必须换成新 `sigma_* min ell_i`，451以
`mu=sigma_* e/(2K)`正确支付。fixed-ray渐近给

\[
 S_i=\sum_{p\in\mathcal P_i}W_i(q_p/P_i)q_p^{-5/6},\qquad
 A_T=(-1)^K Z^{-e/6}\prod_iS_i\asymp(\log Z)^{-K}.
\]

threshold可依赖目标的最终S；不需要moving conductor统一PNT。
`A_T`最终非零、逆为任意小幂。low/high都用
`J_eta=I_(eta,mod)/(c_S A_T)`，`c_S>0`来自同一测试与同一S，
未替换为自由可选标量。

主轮廓先留在global `s=beta_*+epsilon`，跨 `w=1,z=1/6`
的标量极点，再只将主留数s线向右移至2；保留三种真实误差
`m_w=l_y/20`、`m_z=h/600`、`mu`。没有移动reciprocal跨目标零点。
在尚未提取principal tuple的kernel中，z系数是 `1-l_x=h-e`；
principal tuple恰为 `H_eta Z^(e/6) A_T(1+error)`。因此除以同一
`A_T`后的Mellin幂准确为

\[
 s+l_x/2-1+(h-e)/6+e/6=s-2/3-b/6=C_b(s),
\]

最后的 `e/6`来自该exact principal tuple；若采用已经合并tuple的
`h/6`记账，不得再加一次。`A_T`本身只有最终logarithmic大小。

## 6. 统一量词、late height与全族反证

451的次序可实际实现：

1. 目标前固定精确geometry、whole-family bootstrap、反证的共同
   `Delta`和 `k_act`；给中央预算、moment/count losses、strict
   capacity decrement、mesh与rounding。
2. 再选fixed even K及disjoint windows；随后才选
   `mu=sigma_* e/(2K)`、amplitude widths、prime/bin preliminary losses。
   不用依赖K的mu回选mesh。
3. `zeta=Delta/32`、足够大 `z_infty`及全部实参数在目标前固定。
   principal三项分别支付独立预算，floor/middle/small保留一半
   固定余量，中央其他总费用小于 `Delta/4`。
4. 共同 `m0=min(Delta,m_w,m_z,mu,1/200,1/50,2/25)>0`，
   `m=m0/4`目标前固定。目标η后才固定最终arithmetic data和同一S、
   内部moment/Sobolev/seminorm阶，得有限 `A_eta,B_eta`及actual
   detector ceiling。这些degree不随后选external N变化。
5. 保留唯一原frequency matrix的 cumulative `T1/2` allocation，
   包括physical `Im z`、witness及prime coordinates；不能按估计更新
   allowance。目标后取 `tau_eta`不超过实际ceiling及
   `m/[4(A_eta+1)]`，再选足够大N，最后阈值。

于是同一 `J_eta` 和主信号 `f_eta` 都不含 `T1`，给实际合同

\[
 |J_\eta-f_\eta|\ll_{\eta,N}
 Z^{C_b(\beta_*)-m}(1+T_1)^{A_\eta}+Z^{B_\eta}T_1^{-N}.
\]

取 `T1=Z^tau_eta`后，第一项保留至少 `3m/4`，第二项可取小于
`Z^(C_b(beta_*)-m/2)`；故共同 `sigma_hi=m/2=m0/8`成立。
target-dependent的tau、N、常数和threshold不改变两个函数定义，
也不改变目标前的共同saving。low与逆normalizer总费取
`omega=Delta/2`，严格小于Delta。

Mellin闭合不是跨目标零点移线。定义

\[
 f_\eta(Z)=\frac1{2\pi i}\int_{(2)}
 Z^{C_b(s)}e^{(s-5/6)^2}H_\eta(s)/L_F^S(s,\eta)\,ds.
\]

`J_eta`只需足够大Z定义；小Z任意快幂衰减只证明给该 `f_eta`，
通过将其线2向右移至任意固定B得到。large-Z low/high合同、
`C_b`斜率1给 `epsilon_*=min(Delta/2,m0/8)>0`，从而

\[
 \int_0^\infty f_\eta(Z)Z^{-C_b(s)}\,dZ/Z
\]

在 `Re s>beta_*-epsilon_*`局部一致收敛。用 `Z=exp(u)`的
Fourier inversion在初始线2识别transform，再在 `Re s>1`
由identity theorem识别；`|H_eta|>=1/2`排除numerator取消。
这给reciprocal的全纯延拓。

共同epsilon不依赖目标，故全族supremum定义提供某个实际目标零
`Re rho>beta_*-epsilon_*`，无需supremum达到。Euler删除不改变
`Re s>0`的零，形成矛盾，推出条件下 `beta_*<=sigma_*`。

原二次transfer
`L_F^S(s,chi o Norm)=L^S(s,chi)L^S(s,chi chi_(-3))`
及finite deletions给全部Dirichlet同一严格半平面。`s=1`可能的
pole-zero cancellation按原输入处理，`L(1,chi_(-3))`非零；principal
pole允许。451没有断言边界线本身无零。

## 7. 范围结论和继续研究的未付项

新内容是准确的lower-κ实际计数准入、其对reference cubic envelope的
反馈，以及保留全部物理行和同一normalizer后的条件全族continuation。
不是仅调一次端点数值，也不是在κ*处非法假定待证零自由前件。
完整重新核算后，451显示的新严格边界在所列[R]下成立。

上述条件范围之外的工作没有被本次PASS关闭：原输入包整体独立认证、
形式化kernel验收、原AF Hermitian whole-response的有限常数四迹、
moving residue weights、全部cross-cell/alias以及更高简单临界线比例。
未完成的high-prime repeated-sector/alternating-path推导也不在本报告
列为已付输入。旧69999与自由b论文源未编辑。
