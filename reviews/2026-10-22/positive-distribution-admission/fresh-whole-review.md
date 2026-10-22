# 576／C039 独立整稿逆审：限定 PASS

2026-10-22。独立复核主稿、合同及三个分支的实际版本；另对 Euler／Γ 归一化作独立交叉核对。只写本文件，不改主稿、STATE 或轮数。结论是**限定 PASS，无阻断本稿已限定命题的问题**；hash 只绑定版本，不代替证明。

## 1. 通过的准确命题

1. 固定真实曲线 \(E/\mathbb F_5:y^2=x^3+x+1\) 的已付全次数点数递推与正 (H)，经过实际 base change 和整个 completed 对象的 centered dilation，确能保全部 returns／aliases、完整 powers 与双 pole，并以独立选择的相位小回归逼近任意预定 \(2\cos(\gamma u)du\)。这里没有读取经典零点。
2. 对 \(m\ge2,0<a\le1\)，Möbius 反演确给非负实权 primitive，而不只给正 log-Euler 系数；全 \(n\ge2\) 的 \(b_n\ge53A^n/(100n)\) 成立。
3. 允许有限非负实权混合后，未标记完整分布的 (D') 闭包恰为全部实偶正型分布。它不表示固定经典完成化／pole／weight 纤维已非空，也不表示普通整数重数 determinant 的极限身份已付。
4. 在每个固定物理源窗的原全线 zero-extension \(H_{\log}\simeq D_{\log}\) 域上，完整 aliases 相对目标 cosine 的正误差有统一 \(O_R(1/\log\Delta)\) 上界。双 pole-zero 的实际调制源给匹配阶 lower，且排除原 (du) operator 误差为 (o(1))。这是全源 operator 费的匹配检验，不是每个源的必要费用。

## 2. 独立算核

**完整缩放和 Euler。**写 \(w=\tfrac12+a(s-\tfrac12)\)、\(Q=5^m\)、\(h=a\log Q\)，则 \(Q^{-w}=Cx\)、\(x=e^{-hs}\)，其中 \(A=QC=Q^{(1+a)/2}\)、\(B=\sqrt Q C=Q^{a/2}\)、\(C=Q^{-(1-a)/2}\)，并有 \(AC=B^2\)。因此主稿 (6) 的分子／分母、全部 \(c_n\) 和 poles \(\tfrac12\pm(2a)^{-1}+2\pi ik/h\) 均正确；不能固定原 0/1 pole 后只移动 comb。

由 \(A\ge5,B/A\le1/5,C\le1\)，有 \(c_n\ge23A^n/25\)（\(n\ge2\)）、\(c_k\le7A^k/5+1\)。全部 proper-divisor 指数在 \(1,\ldots,K=\lfloor n/2\rfloor\)，其和至多

\[
 (7/4)A^K+K\le(39/20)A^K\le(39/100)A^n.
\]

扣除最不利 Möbius 项即得所报 (53/100)；没有把有限数表外推为全部次数。实权 primitive、正 convolution exponential 和右半平面绝对收敛也与该归一相容。非整数权混合仍可能产生 branch，正文已明确降到分布证书层。

**相位与闭包。**若 \(e^{i\theta}\) 为 root of unity，则 \(2\cos\theta=-3/\sqrt5\) 为代数整数，平方 (9/5) 仍应为代数整数，矛盾。故可独立选 \(m_j\to\infty\) 使相位余量 \(\delta_j\to0\)，再取 \(h_j=\delta_j/\gamma\)；全部 comb 的逐 cell 误差正是 (10)。\(\gamma=0\) 的 \(h_j=\sqrt{\delta_j}\) 也合法。闭包反向包含由标准 Bochner–Schwartz 谱截断／正求积及闭凸锥完成，不把有限头当全谱，也不依赖未经连续性控制的可数测试对角化。

新增 (11a) 的**经典整数混合闭包 membership iff RH**同样通过：在 RH 前件下，完整显式公式以整数重数的实零点对给出 \(\sum_{\gamma>0}m_\gamma2\cos(\gamma u)\)；零点计数的多项式增长支付 (S') 截断，任一有限整数和可由 (9) 逼近。另一向由正型锥闭与 Weil 判据。这只是在 RH 前件下消费旧完整零点表示，不是独立近似规则；也未证明整数混合闭包等于全部正型锥。一般“偶完成化”处仅消费中心零点偶重数的偶函数情形。

**Poisson 和原 norm。**主稿 (4)、(12) 中 spectral measure 没有多余 \(2\pi\)：实际是 \(\widehat W=2\pi\sigma\)，而 \(Q=\int|\widehat r|^2d\sigma\)。两支 aliases 重合时仍按两次计重。由 \(\chi r=r\) 的卷积公式、weighted Cauchy–Schwarz，主稿 (13) 的首括号确为 \(O_\chi(1/w(\lambda))\)；每支格点分别 separated 就足以给余括号求和的 uniform packing 上界，不需两支相互分离。Tonelli 合法，留下的固定 Fourier 常数已吸入 \(C_R\)。这是 \(Q_{h,\gamma}-Q_{\cos}=R\ge0\) 的正确方向。

固定窗 core 延拓和正残差 Cauchy–Schwarz 支付全部 complex 源及 mixed 误差；没有换成 periodic 或 regional 域。式 (14) 的两矩修正严格为零，修正系数和原 \(H_{\log}\) 费为任意负幂。主要调制源的 \(H_{\log}\) 费渐近为 \(\log\Delta\|\eta\|_2^2\)，同时一个真实 alias 读出趋非零，所以 sharp 阶及原 \(du\) 反测都成立。该 lower 作用于真实源，不是辅助全空间 norm；没有声称可直接支付经典 Sonin／core 费用。

## 3. Γ 预算与允许修复

\(|\operatorname{Tr}U^n|\le2g\) 给 \(|W_{C,a}|([-R,R])\le2g(2R+h)\)。因此所列两项 genus／weight 预算一致有界时，极限必为 locally finite Radon 测度；经典完整 Γ 的穿孔核为 \(-e^{-|u|/2}/(1-e^{-2|u|})\sim-1/(2|u|)\)，而 pole 背景平滑且首 prime atom 离零，故同一完整目标不在该有界 TV 类。这里扣除了旧非 Radon 事实，不把新组合上界夸大为排除所有缩放逼近。

发散预算修复确实合法：digamma 级数直接给

\[
 \Gamma(t)-\Gamma(0)
 =\sum_{k\ge0}\frac{(t/2)^2}
 {(k+1/4)\((k+1/4)^2+(t/2)^2\)}\ge0.
\]

故 \(W_\Gamma-\Gamma(0)\delta_0\) 是独立正型且非 Radon 的分布，可由已证明的宽闭包逼近。这说明 TV 门仅排有界预算子类。恢复经典目标必须补回原 contact，并同源处理所有 \(p^k\) 和两 pole；正文没有从这一正修补偷渡完整 signed 组合的正号。

新增主稿 (17a)–(17b) 也通过：对每个固定 locally finite Radon \(V\)，\(|Q_V(r)|\le |V|([-2R,2R])\|r\|_2^2\) 是 autocorrelation 的实际原 \(du\) 上界。用同窗高频调制并严格修正双 pole 矩后，Γ 的首项给 \(Q_\zeta(r_t)\sim\log t\|\eta\|_2^2\)，而 fixed 窗只含有限 prime-power shifts，贡献 \(O_R(\|r_t\|_2^2)\)；\(Q_V(r_t)\) 亦仅 \(O_V(\|r_t\|_2^2)\)。因此两者分别除以原 \(\|r_t\|_{H_{\log}}^2\sim\log t\|\eta\|_2^2\) 的极限为 1 和 0，确得每个 \(V\) 的全部双 pole-zero 源上 norm 误差至少 1。允许每层 TV 任意发散也不能越过该门，因为对每层先固定 \(V_j\) 再选更高频率。常数 1 仅对应所给 Γ／\(H_{\log}\) 首项归一；不是等价 \(D_{\log}\) 范数中的不变数值。这是旧 Γ 首项责任的精确消费，不影响 \(D'\)／逐源逼近。保留真 Γ 奇性、较强范数或源适应截断均为未排修复，(13) 的 finite cosine alias 误差未被误作完整 Γ 的 norm 逼近。

## 4. 源、关系和控制的消费范围

405 实际 noncompact \(p=(D^2-1/4)H\) 有 \(\int p=-\tfrac14\int H\ne0\)，常数极限的 \(Q_0(p)>0\)。全线 \(L^1\) 导数版 Riemann 和适用于该快速衰减源，故这是实际关系失败，不是只检查 compact 交空。逐层精确消 405 会迫使正谱支撑位于该关系变换的实零集；其源坐标责任不能由“正证书”名字消掉。

另一方面，完整 \(D'\) 逼近仅为证明 compact 源正性时，不要求每层先消经典 noncompact Pan；额外全源商／截面 lift／ordinary trace 身份另需尾费。537 非根由真正完整极限才能保证最终可见，任意单个原料无此保证。准确 dilation 范数及原 pole 矩变换也通过：\(a\le1\) 的 \(H_{\log}\) contraction 不支付扩大的 native 源窗、容量或 trace 尾。

连续正 cosine 与连续负 cosh 的完整双 pole-zero mixed 控制有效；Gaussian 卷积与 Gaussian 乘窗未被混同。粗固定乘窗能掩盖负谱的 signed 例子也被保留，未把某负例扩成一般不可能定理。函数域独立正性仍归旧 \(H\)、完整递推和几何 RR；本轮没有重新证明 Weil 猜想。

## 5. 新旧归属、轮次与停止

可限定结算一完整合成数学轮：**固定真实曲线的实际全 base change／缩放接通已有解析正锥，付全次数 primitive 正号，并新增全部 aliases 的原 \(H_{\log}\) uniform sharp 费用。**这不应只因使用标准旋转、Poisson 和 Schur 工具就一概记为来源整理零轮。反过来，continuous cosine、Bochner 闭锥、原有限 \(H\)、Γ 非 Radon及未缩放 gap 均是旧资产／标准工具，不可重复计功。历史去重只支持本仓有界检索判断，不支持世界优先权。

它改变的是局部正模型覆盖及固定窗原费设施；**没有改变独立经典 membership／mixed RR 容量、strong-old 542＋555→557 的 whole leading 4/5 负惯性上预算，亦未改变 actual 成长 core／coupling／Ξ。**原费用是 fixed \(R\)、对全部 complex 源的结论；总权、频率及源窗成长仍须共同支付。宏观 Goal 门保持 open。

本轮止于该宽类的精确覆盖与费用，不续调相位、尺度、抹平或以未知闭包 membership 换名 RH。下一准入须有从完整经典 Γ/contact、全部 prime powers 与 pole 直接生成非负近似的独立规则和同步误差，或同对象实际源→截面／RR 容量；更刚性的 marking、整数 trace、共同尺度或其他独立修补均未被排除。由 root 完成前件消费与统一计轮；本文件不自行结算。

## 6. 最终复核版本（LF SHA-256）

| 文件 | LF SHA-256 |
|---|---|
| `notes/576-fixed-elliptic-positive-cone-and-original-alias-cost.md` | `cbf32034c1e63518ef124ba89e1a46093b55da1086868532d8e5a1e0576595bd` |
| `goals/contracts/C039-function-field-positive-cone-and-original-norm-transport.md` | `c1be0e5225627a72481758148ba4f219d0b9360a9a1b1230c91fda9937eaa52f` |
| `reviews/2026-10-22/positive-distribution-admission/function-field-approximation-and-scaling.md` | `94081c58c66041bb00e5f8fd0fe6b9e1303f39950e4d0ba2fa0556649c32bea5` |
| `reviews/2026-10-22/positive-distribution-admission/history-and-independent-input-audit.md` | `e15195f2e788548333bfc919e05497192799f8565d53746e516e7a070e87774b` |
| `reviews/2026-10-22/positive-distribution-admission/smoothing-and-positive-certificate-tests.md` | `2978e4102d0046577e3262f1e644e7890f5b355e8913cd5c5af06eeeb3493648` |

上述版本若发生实质修改，对应消费须重新闭合。本审未修改任何被审文件。
