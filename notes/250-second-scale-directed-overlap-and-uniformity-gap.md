# 250. 第二尺度 directed overlap 与 uniformity gap

日期：2026-09-04

分支：NCE-8 / 路线 B1；接口：B1h second finite ratio / physical
prime--continuum Schur gain

状态：预注册实例 `(Y,N,J,h)=(16,15,4,1/200)` 的 intended Brownian
分母、directed whole-cell 分子、固定比值与 physical overlap 为 [T]；第一、第二
尺度的数值比较为 [E]；任何尺度一致下界、归一化稳定 core 或 RH/GRH 结论仍为 [O]。
本轮只更新 Markdown，不更新 PDF。

## 1. 第二尺度主定理

沿用笔记 244--249 的 two-sided prime/continuum measures、degree-two divided
difference multiplier 与 Brownian spectral measure。令

\[
 D_{16}=P_{16}+C_{16}
 =\int_{\mathbb R}(W_{p,16}^2+W_{c,16}^2)\,d\omega_{R,16}
\tag{1}
\]

为完整 intended finite diagonal，并令

\[
 G_{16}=\left\{\xi:\frac14\le
 \frac{W_{p,16}(\xi)}{W_{c,16}(\xi)}\le4\right\}.
\tag{2}
\]

### 定理 250-A（second intended ratio certificate）[T]

对

\[
 (Y,N,J,h)=(16,15,4,1/200),\qquad |\xi|\le256,
\tag{3}
\]

完整 intended diagonal 满足

\[
 \boxed{D_{16}\le
 0.001025620093083457466797381202.}
\tag{4}
\]

存在 10,065 个经 outward rational intervals 验证的 positive-frequency cells，
其正频率总宽度为 `10065/200=50.325`，且

\[
 \mathcal N_{16}:=
 \int_{G_{16,\mathrm{verified}}}
 (W_{p,16}^2+W_{c,16}^2)\,d\omega_{R,16}
 \ge0.000163944504546660552689839988.
\tag{5}
\]

因此

\[
 \boxed{
 \frac{\mathcal N_{16}}{D_{16}}
 \ge0.159849154333328712>\frac3{20}.}
\tag{6}
\]

这里式 (6) 使用脚本内部未十进制截断的 exact rational quotient；显示值向下舍入。
未验证 cells 与 `|xi|>256` 的能量全部丢弃。

### 推论 250-B（second finite physical Schur gain）[T]

在式 (2) 的 band 上逐点有

\[
 \frac{W_{p,16}W_{c,16}}
 {W_{p,16}^2+W_{c,16}^2}\ge\frac4{17}.
\tag{7}
\]

由笔记 244 的符号恒等式 `z_16=<u_p,u_c><=0` 与式 (6)，

\[
 \boxed{-z_{16}>\frac3{85}(P_{16}+C_{16}).}
\tag{8}
\]

故 full physical energy 满足

\[
 \|u_{p,16}+u_{c,16}\|^2
 =D_{16}+2z_{16}<\frac{79}{85}D_{16},
\tag{9}
\]

以及

\[
 \boxed{
 \frac{D_{16}}{\|u_{p,16}+u_{c,16}\|^2}
 >\frac{85}{79}=1.0759493670\ldots .}
\tag{10}
\]

式 (8)--(10) 只属于这个 fixed physical response，不是任意系数 Bessel bound，
也不是随尺度一致的 Schur gain。

## 2. Intended base data

prime-power support 扩为

\[
 n\in\{2,3,4,5,7,8,9,11,13\},
\qquad
 w_n=(\log p)n^{-3/5}e^{-n/16}.
\tag{11}
\]

continuum density 改为

\[
 f_{16}(x)=\exp\left(\frac{2x}{5}-\frac{e^x}{16}\right),
\qquad 0\le x\le2,
\tag{12}
\]

而 small cell `[0,3/100]`、四个 uniform cells 及其中点保持与笔记 248
相同。对 `Y=16` 仍有 `f<3, |g'|<1, e^x/Y<1`，故笔记 248 的保守界
`|f''''|<45` 与 eight-panel Simpson remainder 原样有效。所有 `log, exp,
sqrt(3)` 仍由 rational series 或整数平方根 enclosure。

## 3. Surrogate Brownian 分母的独立证书

生产 factorization 在第二尺度产生更大的 formal supports。本脚本先按 rational
continuum grid 精确商掉全部 grid relations，再将每个 binary64 coefficient 视为
exact dyadic rational，并在零点精确重新居中。prime 与 continuum response 分别得到
64,547 和 56,713 个 canonical nonzero atoms。

每个位置 `log(ratio)+shift` 用 96 项正项 atanh series enclosure；允许的 smooth
primes 为 `2,3,5,7,11,13`。全部 position intervals 经排序后均为 singleton
clusters，故 `maximum_cluster_size=1`。笔记 247 的 cluster-safe primitive theorem给

\[
 \widetilde D_{p,16}
 \le0.000825555045593615937494173316,
\tag{13}
\]

\[
 \widetilde D_{c,16}
 \le0.000171309003407826754442854097.
\tag{14}
\]

这一步完全由 rational atom ordering 与 cumulative masses完成，不把 NumPy Gram
或数值积分当作上界证明。

## 4. Intended-to-surrogate 误差账本

base coefficient intervals与 production binary64 maps之间的 TV errors为

\[
 \delta_{p,16}
 \le2.36479612535922\times10^{-16},
\qquad
 \delta_{c,16}
 \le7.109388396055982101423644\times10^{-6}.
\tag{15}
\]

对 quartic divided difference使用笔记 248 的 Banach convolution ledger，并逐操作
重放 production pruning/roundoff。这里出现一个第一尺度未暴露的实现边界：外围
spectral ledger与 production factorization对同一 total mass 的累加顺序可相差一个
ulp。正确的 coefficient replay必须取 production factorization实际消费的
`total_mass, level, polynomial_factor`；用外围副本会使逐系数 equality 断言失败。
修正对象来源后仍保留强断言

\[
 Q_{\rm replay}=Q_{\rm production}
\quad\text{coefficient by coefficient}.
\tag{16}
\]

最终误差预算为

\[
 \|Q(d)-\widetilde Q(\widetilde d)\|_{TV}
 \le0.017313400595649776151360832637,
\tag{17}
\]

\[
 |s-\widetilde s|
 \le0.000000001684114744824453423914,
\tag{18}
\]

\[
 \varepsilon_{p,16}
 \le0.000053158286316685701138100090,
\qquad
 \varepsilon_{c,16}
 \le0.000058091822381093785945445447.
\tag{19}
\]

因 `log 15<3`，centered component 与 quartic response 的共同 support length仍可取
`L=30`。分别以 `tau=1/100` 应用

\[
 D_j\le(1+\tau)\widetilde D_j
 +(1+\tau^{-1})L\varepsilon_j^2
\tag{20}
\]

并相加，得到式 (4)。

## 5. Directed whole-cell numerator

对 `i=1,...,51199` 使用

\[
 I_i=[i/200,(i+1)/200],\qquad t_i=(i+1/2)/200.
\tag{21}
\]

在每个 midpoint上，Machin `pi` interval、degree-44 cosine Taylor interval和
`10^-60` outward fixed-point arithmetic同时 enclosure `W_p,W_c,d-hat,Q(d-hat)`。
加入 exact first-moment Lipschitz radii后，只保留整格满足

\[
 p_i^-,c_i^-,q_i^->0,qquad
 4p_i^-\ge c_i^+,qquad p_i^+\le4c_i^-.
\tag{22}
\]

每个通过格按右端点给 Brownian density 的一侧下界，再以 fixed-point downward
products求和。冻结输出为：

- verified cell count：`10065`；
- index SHA-256：
  `6ee45ac6e3d3908bb2b0fa464f98672065d9a6718f46e44d79d06a19bf6efdc9`；
- `(index, fixed lower)` SHA-256：
  `52c87473889013e920172f3a1eb80831540bbba61d388561b9e5256d77c1ce40`；
- numerator lower：式 (5)；
- ratio lower：式 (6)。

脚本会在 denominator、numerator、count、任一 hash 或 `ratio>3/20` 失效时退出非零。

## 6. 两尺度比较：证据与不能推出的结论

| quantity | `(8,10,4)` | `(16,15,4)` | status |
|---|---:|---:|---|
| rigorous `N_lower/D_upper` | `>0.1912349009` | `>0.1598491543` | [T], finite |
| verified positive width | `63.925` | `50.325` | [T], finite |
| floating raw wide-band/exact diagonal | `0.58489` | `0.70255` | [E] |
| floating Lipschitz lower/exact diagonal | `0.19987` | `0.16448` | [E] |

第二尺度的 raw wide-band fraction上升，而粗 global-Lipschitz certificate fraction下降。
因此当前两点不支持“频谱质量逃离宽 ratio band”的解释；更像是 whole-cell
resolution与增大的 prime first moment造成证书损失 [E]。这只是诊断，不是对所有尺度
的定理。特别地：

- 两个正的 finite ratios不推出统一正下界；
- verified widths没有在任何自然归一化下证明共同 core；
- 第二尺度常数较小，不能用第一尺度的 `19/425` overlap常数；
- 不得从 raw floating capture取代式 (5) 的 outward lower。

## 7. 最小输入、删除与循环性审计

最小输入：九个显式 prime powers、五个 finite continuum integrals、rational
transcendental enclosures、exact lag quotient、cluster-safe Brownian energy、IEEE
binary64逐操作误差、production operand provenance、whole-cell Lipschitz theorem及
fixed-point numerator sum。

删除审计：

- 删除 exact canonical quotient或 position enclosure，式 (13)--(14)只剩数值能量；
- 删除重新居中，Brownian primitive可能带未结算常数模；
- 删除 production operand provenance，第二尺度逐系数 replay实际失败；
- 删除 base/polynomial/scalar/roundoff任一误差，surrogate不能转到 intended response；
- 删除 Lipschitz radii，midpoint good不推出 whole-cell good；
- 删除 denominator upper，finite numerator不能形成 capture fraction；
- 删除 ratio band，cross/diagonal factor可趋零；
- 将两个 finite points外推为 uniform B1a，结论无依据。

非同义反复审计：输入没有包含式 (5)、式 (6)或 physical cross gain；全部三者均可在
预注册第二实例失败。第一次严格运行确实在独立 replay invariant处失败，说明断言不是
装饰性公理。

循环性审计：未使用 zeros、RH/GRH、Weil positivity、unitarity、PNT error、Mertens
平方根界、bounded negative index或任何渐近 prime discrepancy。prime side只枚举
`n<=15` 的九个 von Mangoldt atoms。

## 8. 模型范围与下一最小引理 B1i [O]

- 当前 Riemann-zeta finite Abel model：定理 250-A--B直接适用；
- Dedekind positive-coefficient finite models：schema可迁移，但需重做 ideal weights、
  lag quotient与 Archimedean channels；
- primitive Dirichlet/automorphic models：complex phases破坏 scalar sign cones，不能引用
  式 (7)--(8)；
- 函数域：degree lags离散，position enclosure更容易，但 coefficient field另行处理；
- 本结果仍是显式公式型 Weil response，不构造上同调极化或 Hard Lefschetz bridge。

B1h 的第二有限证书已闭合。下一最小引理 B1i 是预注册自然相位坐标

\[
 \theta=\xi\log Y
\tag{23}
\]

并以 rational `log 8,log 16` intervals把两组 verified cells推到 theta 轴，证明一个
正长度的共同 whole-cell core，或给出该归一化下共同 core不足以携带固定 response
energy的严格障碍。只有在共同 core同时获得尺度中性的 density lower后，才允许提出
第三尺度；否则停止继续堆叠 finite实例，转向把 loss归约为 smoothed prime
first-moment/discrepancy estimate。

后续：笔记 251 已在 `t=theta/log2` 上闭合 B1i。两尺度 verified ledgers具有
18-component、总宽 `29.655` 的 exact common core；它分别携带 `>5.329%` 与
`>11.327%` 的完整 diagonal，并给共享 finite gain `-z>D/85` [T]。当前进入 B1j
cofinal schedule与 dyadic normalized-symbol transfer；不得从两个尺度外推 uniformity。
