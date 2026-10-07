# 445 独立逆审：同源合同、参数顺序与全角色族延拓

日期：2026-10-07。审查人：radial_review（非 445 作者）。
结论：**限定 PASS [T/R]**。全文核对 445，并重新检查其所需 441–444 的对象、参数范围、正余量和原来源的实际量词。未发现阻断本稿引用证明的错误。

这是相对于准确列出的原通用结果和原全 Hecke 7/8 结论的纸面证明。没有独立重证原论文的全部算术、递归矩估计或外部依赖；没有执行原论文编译、Lean elaboration、kernel check 或 Comparator，也不是 RH/RR 证明。

## 1. 文件绑定

全部哈希按字节 CRLF→LF 后 SHA256；不作其他空白或 Unicode 规范化。

| 文件 | canonical LF SHA256 | LF 字节 |
|---|---|---:|
| notes/445-conditional-strip-improvement-and-family-continuation.md | 99ac005976c7c22934b5597c25b0d6fc6d7f3f4d9be604f8cbd53e130eae0f2e | 9869 |
| notes/441-variable-slot-low-bound-on-the-original-probe.md | dffcaa1899358d581fe3d6438ee87d075588e5e7e8f41ccd8a629fe5c31be0dd | 8643 |
| notes/442-shared-contours-and-principal-signal-at-the-new-boundary.md | 87abb4dd86ccae9b8209e030606413ef2b8682631f9c4d9195afdd808ad1b6b7 | 11726 |
| notes/443-effective-kappa-and-actual-detector-capacity.md | 79bfb7f8770eb3865ccdfe0da416388b2182383bd425fd57b39f520b3fd59bc6 | 10122 |
| notes/444-joint-error-slots-and-uniform-central-high-saving.md | 47686e9b6b28239562e83e9ab5199349458fd19bf9abbe45cca67df8c876957c | 10069 |

原 [R] 来源：
E:\codex-build\math\preprints\The-Quasi-Riemann-Hypothesis-September-30-2026\build\paper.tex。
固定 Git 提交 adc7f1241b42e322a6451854ab7e4b4c146bf78a；
canonical LF SHA256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3（766316 字节）。
下文 source 行号绑定此文件，不指向漂移的 main。

## 2. bootstrap、全族量词与同一对象

445 §1–§2 通过。

source 373–398 定义的 \(\beta_*\) 是全部 primitive finite-order Hecke characters 在 \(F=\mathbb Q(\sqrt{-3})\) 上零实部的共同上确界，包含 \(1/2\)，不包含极点。接受 source 16455–16463 的全族 7/8 结论后，反证范围准确为
\[
 \sigma_1<\beta_*\le7/8,\qquad
 0<\Delta_1=\beta_*-\sigma_1\le1/80000.
\]
这里允许 \(\beta_*\) 不被任何角色达到。bootstrap 是已明确引用的旧边界，没有把待证新边界作为 reciprocal 或 plain moment 的输入。

source stage-high definition 5584–5649 明确要求 physical expression 独立给定，并要求 direct low estimate 指向这份表达式；高积分不能反过来定义它。441 保留原 completed sums 的 finite compensation 与所有 masks；442 用原 coefficientwise high identity 和 selected local operation 重放恒等式。445 采用的
\[
 J_\eta=I_{\eta,\mathrm{modified}}/(c_S A_T),\qquad
 f_\eta=\frac1{2\pi i}\int_{(2)}
 Z^{s-11/16}e^{(s-5/6)^2}
 \frac{H_\eta(s)}{L_F^S(s,\eta)}\,ds
\]
确实是同一 expression 和同一 principal 双留数，均没有 \(T_1\)。

目标前固定 ray group 和 slot system；目标后可把 conductor、动态误差估计需要的固定 primes 加入最终 \(S\)。source 3327–3343、3950–3951 与 16336–16341 允许这种次序，且扩大 \(S\) 缩小原 positive product-tail majorant。442 最终稿已经准确写出
\[
 \exp\!\left(C\sum_{Q>P_0}Q^{-1-c_b}\right)-1\le1/2.
\]
因此同一个 \(H_\eta\) 在 \(\Re s>\sigma_1\) 全纯且 \(\sup|H_\eta-1|\le1/2\)，所有 physical terms、\(c_S\)、\(A_T\)、principal extraction 和 \(f_\eta\) 均使用目标的同一个最终 \(S\)。没有把一般行的 local zeros 除掉。

固定非负非零 \(W_i\) 的 fixed-ray asymptotic 给 \(A_T\) 最终非零、逆为 logarithmic power。其 lower threshold 可依赖最终 \(S\)；subpower exponent 可先于目标指定。常数不必对全部角色统一。这个区分正是 source continuation criterion 408–431 所允许的量词。

## 3. 441–444 的实际输入没有偷换

### 3.1 完整 low

441 使用原一般 reflected-energy、smooth calculus、Gaussian annuli、row sectors 和 additive Gram 的明确 [R]，不调用仅为 \(\ell=1/6\) 声明的 fixed-geometry low proposition。

其关键重新计算是
\[
 M'+\ell'-1=-3d_J,\qquad
 T_d-(H-3d_J)\le2\epsilon_Z+|\theta_N|,
\]
以及未删掉的正 row loss
\[
 \sum|B_m^J|^2\ll
 Z^{M'+((5\ell-1+d_J)/4)_++\epsilon}.
\]
同一 tuple 的原系数、tuple 数和 \(X'\) 亏损给
\[
 -d_J+(5\ell-1+d_J)_+/8\le-7d_J/8\le0.
\]
empty surviving slots 使用 \(z_a=0\) 的第一分支，没有假设必须存在正标记。所有 actual residual dyads、共同 joint profile、原 row masks、shared primes、Gaussian tails 和 ray/Gauss coefficients 在上述一般引理的适用范围内。新参数给
\[
 |I_{\mathrm{modified}}|\ll
 Z^{14999/80000+\epsilon},\qquad
 C(\sigma_1)=14999/80000.
\]
445 将低侧 loss 和 normalizer loss 合计取至 \(\Delta_1/2\)，所得 \(\omega=\Delta_1/2\) 是 target-independent 且严格小于 \(\Delta_1\)。依赖假定反证中的共同 \(\beta_*\) 是合法的前目标选择，不是参数循环。

### 3.2 完整 high 的全行覆盖

442 的 full selected/unselected tuple 无商、正常收敛、全虚部 bound 满足 source 5606–5623 的 stage majorant；其 degree 在 external order 之前固定。whole-bin 先在 global \(s\) 线上支付整个外部尾，再移动 retained \(s\) 段；因此后来的 pointwise amplitude/witness sets 没有被拿去独立移动轮廓。

445 §4 四类恰覆盖所有原 physical rows：

- \(u=1\)：同一个 principal normalizer 和三个 remainder；
- \(U\le Z^{d_{\min}}\) 且 \(u\ne1\)：full tuple 绝对小行 bound；在 \(\beta_*>\sigma_1\) 下 \(D_1(1/3)\) 有严格域余量，旧 \(D_1(3/8)\) 不被误引；
- \(Z^{d_{\min}}<U\le Z^{h_1+\zeta}\)：floor 独立 count、中间 no-slot count 和 selected actual counts；
- \(U>Z^{h_1+\zeta}\)：完整绝对大行 bound，在固定 \(z_\infty\) 上求和。

bounded nontrivial units 属于小行；floor 不被强行赋予实际 zero witness。small/absolute large rows 不调用 buffered detector hypothesis。

443 正确固定 \(\kappa_{\rm eff}=3/4\)。source 12532 的 \(\kappa\) 域是 \([3/4,1]\)，12564–12578 的额外条件 \(\beta_*\le(1+\kappa)/2\) 此时由 bootstrap 支付；没有把小于 \(3/4\) 的 \(2\beta_*-1\) 插入原 plain lemma。sixth-power amplification、whole positive-slot spike、实际 coefficient class、共同 orientations、primitive inducing-family exceptions、两个 marked strict widths 和 plain strict width 均保留。

444 的所有 strict ramified error labels 是互异的 selected primes，只对整个 \(J_0\) 分配一次 source 9005–9039 的 conductor deficit；没有为每槽重复获得完整 numerator saving。其 reflected numerator 与 denominator 使用同一个 bin 和 cumulative height buffer。full error/main 分解只用于 retained points，未用于 contour joins。

### 3.3 连续余量

本次另在内存中作精确 Fraction 和符号核对，没有运行或覆盖旧审计：

\[
 C(s)=s-11/16,\quad
 m_{\rm ad}=49/440640-\tfrac53(1/20000)
 =307/11016000>0,
\]
\[
 \zeta=m_{\rm ad}/32=307/352512000,\quad
 m_{\rm ad}-2\zeta=307/11750400.
\]
\(5\ell_1-h_1-\zeta>0\) 且 \(1-h_1-\zeta>0\)，所以 actual prime supply 与 bounded buffered range 同时成立。

还核对了 444(9) 的完整完成平方恒等式和沿
\(\sigma(\ell)=11/12-\ell/4\) 的准确导数
\[
 \partial_\ell E_\sigma(h)
 =-1/4+\delta+q+3R_*/2.
\]
这是 continuous algebra identity；没有将离散网格通过当作区间证明，也没有在改 reference 后重复扣 \(1/80000\)。selected endpoint、正 frequency slopes、floor 和中间 d 的负余量给全部 moderate dyads 的统一包络。这里的 symbol audit 仅核有限代数，不认证所引用的无限分析。

## 4. real choices 的次序无循环

445 §3 的关键次序通过。

source plain lemma 12547–12578 明确说 mesh 只依赖 bounded real lengths 和 prescribed loss，uniform in \(\kappa\in[3/4,1]\)；arithmetic datum 和固定 slot count 只影响其后 finite seminorm/height orders。source 16238–16278 的原应用也先 mesh/rounding 后 \(K\)。因此可先按 fixed \(m_{\rm ad}\) 的小份支付 count/moment/capacity losses，再选 mesh、rounding、fixed even \(K\) 和 \(W_i\)。

随后
\[
 \mu=\frac{\sigma_1\ell_1}{2K}
 <\sigma_1\min_i\ell_i
\]
才定义。没有用这个可能很小的 \(\mu\) 反过来要求更小的 mesh，故不会形成 \(K\to\mu\to\mathrm{mesh}\to K\) 循环。amplitude powers 可在 slot minimum 已固定后选择。

445 的 central budget 只需小于 \(m_{\rm ad}/4\)。principal budget 另将
\((1+h_1)e+\epsilon_{\rm pr}\)、\(e+\epsilon_{\rm pr}\)
分别压至 \(m_w/4,m_z/4,\mu/4\)。继续减小 \(e\) 不改变已经固定的 moment mesh、\(K\) 或供给；source detector-dyads 4398–4404 的 \(e_0\) 只依赖 prescribed loss 和 bounded length ranges。

先选择 \(\zeta\) 与固定 \(z_\infty\) 后再选小 preliminary powers，也符合大行绝对求和。normalizer 的任意小幂按合同分配一次，不额外加第二遍。

因此
\[
 m_0=\min\{m_{\rm ad},m_w,m_z,\mu,172249/2000000\}>0,
 \qquad m=m_0/4
\]
在目标前固定。central 剩余大于 \(m_{\rm ad}/2\ge m_0/2\)，principal、小行和大行也保留至少 \(m_0/2\)；在最后取更小共同 \(m\) 不会要求重选 mesh。指数可很小，但严格正且对目标共同。

## 5. literal height ceiling 到 late closure

445 §4–§5 与 source 6521–6579、15473–15493、16374–16451 的量词一致。

目标及最终 arithmetic datum 固定后，所有 internal moment、Sobolev 和 seminorm orders 才固定。它们只需有限，不需对全部目标共同。取有限 \(A_\eta\) 支配全部 retained height factors；full-tuple/global/absolute majorants 给有限 \(B_\eta\)，且两者都在 external order \(N\) 之前固定。source external-contour-tails 5672–5728 的条件正是这种 fixed \(B,J\)：增加 external kernel order 可使外尾达到任意 \(T_1^{-N}\)，不会增加 arithmetic scale degree。

全部 physical \(\Im z\)、witness 和 prime frequencies 共用单一 cumulative \(T_1/2\) allocation；不能逐次重置 buffer。auxiliary 外部尾阶可在 \(\tau\) 后提高，但不会重新把 externally differentiated profile 交给内部矩定理。

设 \(\epsilon_{\rm ht}\) 为已选 detector allowances 的最小值，固定
\[
 \tau_{0,\eta}=\frac{d_{\min}\epsilon_{\rm ht}}
 {20(1+A_{\rm ht,\eta})}>0.
\]
对 \(T_1=Z^\tau\)、\(0<\tau\le\min(d_{\min}/100,\tau_{0,\eta})\)：
\[
 T_1\le U^{1/100},\qquad
 (1+T_1)^{A_{\rm ht,\eta}}
 \le2^{A_{\rm ht,\eta}}Z^{d_{\min}\epsilon_{\rm ht}/20}
 \le U^{\epsilon_{\rm ht}/10}
\]
在 sufficiently large \(Z\) 成立。因此每个 literal detector height condition 和
\(U^{-189/100+o(1)}T_1^2\to0\)
均被支付；这里的阈值可以依赖目标和 \(\tau\)。

由全部 physical ranges 得到的完整合同是
\[
 |J_\eta-f_\eta|
 \ll_{\eta,N}Z^{C(\beta_*)-m}(1+T_1)^{A_\eta}
 +Z^{B_\eta}T_1^{-N}.
\]
这是全原物理表达式合同，不是选出主项后遗留无限未估计行。随后选择
\[
 \tau_\eta\le m/[4(A_\eta+1)],
 \qquad B_\eta-N_\eta\tau_\eta<C(\beta_*)-m/2
\]
给 high saving \(\sigma_{\rm hi}=m/2>0\)。\(\tau_\eta,N_\eta\)、常数和阈值可依赖目标；\(\omega,\sigma_{\rm hi}\) 必须对全部目标共同，445 保留了这一区别。改变目标的 analysis cutoff 不改变 \(J_\eta\) 或 \(f_\eta\)。

## 6. Mellin 全族反证与转移

445 §6 是 source 400–501 对新 \(\sigma_1\) 的合法实例。

共同
\[
 \epsilon_*=\min(\Delta_1-\omega,\sigma_{\rm hi})>0,
 \qquad \epsilon_*<\Delta_1
\]
给每个 primitive 目标
\(|f_\eta(Z)|\ll_\eta Z^{C(\beta_*)-\epsilon_*}\) 于大 \(Z\)。
小 \(Z\) 向右移至任意固定 \(B>2\)，只用有界 \(H_\eta\)、绝对 reciprocal Euler product 和 Gaussian；没有跨目标零点。中间有限 Z 区间由原积分连续性控制。

因此 Mellin transform 在 \(\Re s>\beta_*-\epsilon_*\) 局部一致收敛并全纯。source 476–488 的普通 Fourier inversion 在 \(\Re s=2\) 上识别它；两个 endpoint bounds 保证所需 integrability，然后 identity theorem 在 \(\Re s>1\) 识别 reciprocal。这个识别没有假设 \(\Re s>\sigma_1\) 已经无零。

由于
\[
 \beta_*-\epsilon_*>\sigma_1,\qquad |H_\eta|\ge1/2,
\]
得到 \(1/L_F^S(s,\eta)\) 在上述半平面的 holomorphic continuation。共同 \(\epsilon_*\) 与上确界定义才允许在此时选出有零
\(\Re\rho>\beta_*-\epsilon_*\)
的某个目标；不需其阈值、cutoff 或常数统一，也不需 \(\beta_*\) 被达到。有限 deleted factors 在 \(\Re s>0\) 非零，故不能移除该 reciprocal pole。反证闭合。

445 §7 的 primitive→imprimitive 和 quadratic transfer 与 source 6705–6781 完全一致：split/inert local factors 给
\[
 L_F^S(s,\chi\circ N)=L^S(s,\chi)L^S(s,\chi\chi_{-3});
\]
\(0<\Re s<1\) 两 Dirichlet 因子全纯；\(s=1+it,t\ne0\) 无极点；唯一 \(s=1\) 的 potential cancellation 用
\(L(1,\chi_{-3})=\pi/(3\sqrt3)>0\)
排除。finite Euler factors 非零于该区域。结论是严格半平面，principal pole 允许；没有推出边界线上无零。

## 7. 准确验收范围

本次 PASS 覆盖：在主稿列明的外部通用 [R] 及旧全族 7/8 结论成立时，441–444 已支付的新对象合同、target-independent 正指数、不可循环的顺序、late-height closure 和全族 Mellin 反证足以推出 445(1)，并转移到 Dirichlet L。

未发现需要返修的数学缺口。明确未验收的部分是原 [R] 本身的完整重证与形式化，而不是把它们暗作本项目自证结果。AF 的简单临界线比例未进入任何坏行 count 或此反证，也没有将有限有理审计冒称无限分析/kernel certification。此次只新增本报告，未修改 math、441–445 或任何旧审计。
