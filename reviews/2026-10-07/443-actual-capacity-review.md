# 443 实际 detector capacity 独立审查

2026-10-07。**限定 PASS。** 审查对象为 `notes/443-effective-kappa-and-actual-detector-capacity.md`，canonical LF SHA256（CRLF及单独CR换为LF后UTF-8）：

`79bfb7f8770eb3865ccdfe0da416388b2182383bd425fd57b39f520b3fd59bc6`。

443 对可变槽参数的 actual count 准入符合所列通用 [R] 前件。它没有把 kappa<3/4 代入未覆盖的 plain theorem，没有要求 error slot 存在 lower spike，也没有用缩小到零的 marked width 处理零容量端点。没有发现实质数学错误；PASS 限于有实际共同 presentation witnesses 的非 floor bins 及稿中明确的 no-slot cases，不扩大到 floor、central joint estimate 或最终 continuation。

## 1. 独立读源与版本

只读 OpenAI/math 提交 `adc7f1241b42e322a6451854ab7e4b4c146bf78a` 的
`E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`。
canonical LF SHA256：

`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`。

逐源核查位置：

| 原输入 | 行号 | 关键前件 |
|---|---:|---|
| buffered bins、actual zero ceiling、primitive family | 4250–4321、6821–6829 | 原 mask、非 floor actual L-zero、a<=beta_* |
| detector dyads/witnesses | 4385–4405、4510–4547 | 同 presentation 与相同 twist height；bounded actual lengths；literal height ceiling |
| marked inverse | 9220–9269 | either common sign、两条严格 width、row-independent coefficients |
| sixth-power amplification | 12362–12389、12423–12460 | sixth-power-free actual rows、bounded r、rowwise smooth tests |
| plain moment | 12492–12578 | kappa∈[3/4,1]、beta_*前件、固定Theta系数类、inducing family与uniform mesh |
| original physical amplitudes | 15015–15090 | fixed prime windows/zero extension、实际 upper/lower amplitude bins |
| actual selection/coefficient identity | 15110–15183 | whole positive slots、两份 witness 及全部 slots 的整体共轭 |
| full count proof | 15185–15446 | actual witness saturation、width、zero-capacity/no-slot与count比较 |
| mesh/pool/order | 16238–16287、16312–16432 | fixed finite slot system、单个累计height预算、内部阶数先于外尾阶数 |

另交叉阅读作者的 `hybrid-effective-kappa-and-capacity-admission.md`，canonical LF SHA256为
`69c290f7df660b8cefe72c792a63e3ed67de7d4b1756aee8d174a25fbe586c79`。
以下核验来自原源的实际陈述和证明，未将该作者报告本身增加为新假设。

## 2. Fixed effective kappa 合法且未循环

原 plain lemma 允许 closed range `3/4<=kappa<=1`，在 kappa<1时的前件是非严格 `beta_*<=(1+kappa)/2`。因此

\[
 \kappa_{eff}=\max(3/4,2\beta_*-1),\qquad
 \Delta_{eff}=\max(\beta_*-7/8,0)
\]

同时满足原范围、`kappa_eff=3/4+2Delta_eff`及所需 beta_* 不等式。Part I 全 Hecke 11/12 input给 kappa_eff<=5/6；若另外接受原全 Hecke 7/8 bootstrap，则反证区间 `sigma1<beta_*<=7/8` 中 kappa_eff=3/4、Delta_eff=0准确成立。

这里使用的是原同一全集 primitive finite-order Hecke beta_*，不是 AF 的固定 Dirichlet高度比例、某个单一角色或 derivative-zero比例。未假设待证 sigma1 半平面已经无零。原 family 全局上确界不必达到；a<=beta_*来自 bin中的actual zeros。

signed `beta_*-7/8<0` 不能投入原 positive capacity-loss比较。443对此作了正确区分。Delta1=beta_*-sigma1为正，且一般 Delta_eff<=Delta1；它与容量损失不混用。

## 3. Witness、whole-slot spike 和 coefficient class

actual witnesses给同一 presentation下的 `r+m>=t-o(1)`，分别有 `|M_r|²>>U^{delta r-epsilon}`、`|S_m|²>>U^{delta m-epsilon}`。plain 使用两份同一 S_m，除以的是 |S_m|⁴，因此正容量条件为 `2m+6kappa_eff z<=1`。只除以 |S_m|² 会得到错误的 affine crossing；443没有这个错误。

选定 physical z、amplitude bin、presentation及dyadic pair后，slot指数 g_i固定。positive main slots满足actual lower spike，errors定义 g_i=0，mean q以**全部 slots 的 ell1**为分母。在U基数下的slot长度为 `w_i=ell_i/d`。按g_i排序，fractional最优填充的gain至少qz；删除至多一个fractional slot在平方spike中损失至多 `delta max_i w_i`。若positive slots不足则全取，其gain是 `q ell1/d>=qz`。因此443(9)是真正whole-slot下界，不需要虚构缺失slot，也不从error factor要求lower bound。

请求容量先减nu0还带来至多2qnu0的平方spike损失；两个损失均按所指定small power预算支付。q=0时可选空集，仍合法。

原 physical Q_i相对于共同 presentation `psi=nu bar(chi_bullet(u))` 的prime coefficient准确为

\[
 \bar\nu(p)1_{p\in1_T}=|T|^{-1}\sum_{\theta\in\widehat T}(\bar\nu\theta)(p).
\]

这是固定Theta有限组合，独立于当前row。对plain的positive common orientation，必须将两个witnesses、全部selected factors及其profiles整体共轭，系数成为 `nu(p)1_T`；443保留了这个操作。所有 masks、disjoint underlying supports与 inducing-family判别保持。不能只共轭 witness，不能令prime系数随后跟随rowwise witness参数变化。

原 source在固定physical参数/selected indices后才对rowwise witness参数作 smooth Sobolev；这只加入logarithmic profile weights和固定height cost。no-slot amplification的实际base profile `W_1(y)V_le(Dy/D_*)`同样有统一固定logarithmic seminorm，纯twist另计height。443的“通用smooth成本”在这些源范围内适用。

## 4. 两条严格 width、群例外及零容量

原 crossing给 `r_*(t)>=23/37`、`1/3<=t-r_*(t)<=1/2`。inverse side请求 `z<=z_M(r)-nu0` 后，

\[
 1-r-2z\ge2\nu_0,qquad
 3-2r-8z=4(1-r-2z)+(2r-1)
 \ge8\nu_0+9/37-O(\epsilon).
\]

第二条 width有独立正余量，并非仅因第一条为正就自动成立。plain side有 `m>=1/3-O(epsilon)`，请求 `z<=z_P(m)-nu0` 后
`1-2m-6kappa_eff z >=(9/2)nu0`。实际 annular ratios只在这些正余量之后由threshold吸收。

positive-slot plain case排除的是primitive inducing character属于Theta，而不是零延拓 presentation字面相同。sixth-power-free physical row在S外的j=1,…,5局部order为6/gcd(6,j)>1，固定Theta无法消去此ramification。因此large rows满足family排除条件；其余fixed S-supported exceptional rows有限。selected U>=Z^{1/2}后不再出现这些例外，但完整物理表达式中的bounded rows仍须由outer接口处理，不能删去。

四种例外处理准确：r>=1用sixth-power amplification；m>=1/2用zero-slot plain；small z_M用 `1-delta r<=1-delta+2delta nu0`；small z_P用 `1-2delta m<=1-delta+6delta nu0`。这些是 upper bounds，不是 exact count identities。

amplification在bounded r中的loss选择统一，包括r接近1：e(r)=max{1,(1+5r)/6}两支连续。delta=alpha时t=3/2给actual r>=1-O(epsilon)，两支均产生 `1-delta+O(epsilon)`。所以端点不调用shrinking marked width；更强7/8 bootstrap下它本来不会实际出现。

## 5. Actual supply、affine count 和 no-slot 结论

独立有理核验了新 supply：

\[
 \ell_1/h_1=20006/97509,
 \quad \ell_1/h_1-7/37=57659/3607833>0,
 \quad5\ell_1-h_1=2521/120000.
\]

选zeta小于最后值，实际 available `ell1/(h1+zeta)>1/5`，比最大inverse需求7/37仍大2/185。plain需求最多2/27+small，更小。只在d>=1/2使用selected primes，所以 `w_i<=2ell_i`；不能以d_min压缩此处mesh条件。

在 fixed count-loss、nu0及rounding预算之后选有限even K，可令2ell1/K低于uniformmesh和supplygap的一半。原I_i⊂(1,2)构造使physicalunderlyingwindows在ray/masks之前disjoint。内部plainpool从 `U^{sigma_width/3}/2` 开始，而physicalslots至多 `2U^{mesh}`、mesh<sigma_width/6，故固定exponentgap保证最终分离。

短count两式的crossing和weightedaverage直接给443(4)–(5)。plain实际capacity减少的cost为

\[
 \frac{24q(1-2m)\Delta_{eff}}{(9/2)(9/2+12\Delta_{eff})}
 \le\Delta_{eff}/4+O(\epsilon).
\]

它始终非负，bootstrap下准确为零。actual witnesses、selected whole-slot spikes和相应moment条件支付后，443(12)是真正pointwise actual count，不是仅由available长度猜测的count。

adaptive T的J有固定上下界，crossing `R_short(T)=L(T)=R_*`，所以443(14)实际成立。其r/m/witness subdivisions、rowwisesmoothsuprema和heightcost都仍计在右边。no-slot t=1时 selectiongain为零，两shortcounts交叉给 `1-2delta/3`，longcount为 `1-delta`，不需要prime-supply前件。floor始终不被该witness count覆盖。

独立BigInt有理计算9项断言通过：ratio、gap、extension、1/5−7/37、D_x/P_x端点、r_*(1)下界、inverse c2余量及相应plain length。有限核验只检查数值，不替代moments的通用分析。

## 6. 量词及最终范围

443量词顺序正确：bootstrap/geometry/boundedactualranges和requestedloss先固定；capacitydecrements、moments/mesh/rounding后固定K与physicalwindows；amplitude及prime-bin preliminaryloss在positive minell_i已知后选。原 `U^epsilon1` 可因d/ell_i有界转入每槽bin allowance。

target确定后才固定Theta和arithmeticdatum、internalSobolev/heightorders。所有retainedvariables用一个累计T1/2预算。tau随后取足够小，使原literaldetectorheightceilings在全moderaterange成立；externaltailorder与threshold最后选。提高externalorder不能改变此前internalheightorders、momentloss或mesh。

443没有超出这些量词去要求movingtarget、K趋无穷或slotmesh趋零时的统一常数。底层marked/plain/witness/amplification仍是明确[R]输入；不是本项目对所有外部来源的重新认证。

在上述绑定版本与范围内，结论为PASS。centralerror-slot×numerator、全frequencyhigh、principalcomparison和continuation必须独立合并；本审查没有从actualcount单项宣布新的无零区域，也未构建或认证Lean/RH。
