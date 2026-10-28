# 一次反射双源构造尝试：系数门即旧式

2026-10-28，unit_height 独占 v1。恢复 STATE／G20261027／D20261028U／前沿，check→show 通过；当前 C049 耗尽，cadence0／历史50／latest586。只做一次公式形成与 cheap admission，无外网／数值／新证明，不改管理文件。

**结果：形成了可代入的实际双源有限和，但未形成合格新 input。** 它精确重编码旧 prime 腿，没有独立 signed 净量，不准 C050／587。

## 固定的一次尝试

原物理复源 \(r=e^{u/2}f,s=e^{u/2}g\in\mathcal S_{\exp,\mathbb C}\)；有限和亦定义于全部 du-L²。记
\[
 h_{r,s}(a)=\int_{\mathbb R}r(u+a)\overline{s(u)}\,du .
\]
不先造正空间；把真实整数 Möbius 与余因子 log 放在相反平移腿，取整数 \(N\ge2\)：
\[
 D_N(r,s)=
 \sum_{\substack{d,m\ge1\\dm\le N}}
 \frac{\mu(d)\log m}{\sqrt{dm}}
 \int r(u+\log d)\overline{s(u-\log m)}\,du ,
\]
\[
 C_N(r,s)=D_N(r,s)+\overline{D_N(s,r)}.
 \tag{1}
\]
这是 first-linear 的 scalar Hermitian 型；没有声称 PSD。两源始终独立，有限 cutoff 是 product \(dm\le N\)，不是分别截两腿。

原 du 费用直接为
\[
 |C_N(r,s)|\le2A_N\|r\|_2\|s\|_2,\qquad
 A_N=\sum_{dm\le N}\frac{|\mu(d)|\log m}{\sqrt{dm}}<\infty .
 \tag{2}
\]
原零延拓 Dlog 满足平方范数至少 \(\log2\) 倍 du²，故相应 upper 为 \(2A_N/\log2\)。不把有限 \(N\) 费叫 cofinal uniform 费。

## 最便宜门：一行实际系数塌缩

在每一项取 \(v=u-\log m\)，其积分恰为 \(h_{r,s}(\log(dm))\)。有限换序合法，因而
\[
 D_N(r,s)=\sum_{2\le n\le N}\frac{h_{r,s}(\log n)}{\sqrt n}
       \underbrace{\sum_{d\mid n}\mu(d)\log(n/d)}_{\Lambda(n)},
\]
\[
 \boxed{C_N(r,s)=\sum_{2\le n\le N}
 \frac{\Lambda(n)}{\sqrt n}
 [h_{r,s}(\log n)+h_{r,s}(-\log n)] .}
 \tag{3}
\]
全部 proper powers 留下原权 \(\Lambda(p^k)=\log p\)；复合非幂位置消去。这里的反射源位置是正确的，但它没有改变旧 Dirichlet 系数。

对每先固定 \(r,s\in C_c^\infty((-L,L);\mathbb C)\)，取 \(N\ge e^{2L}\) 后，(3) 已是完整 prime 腿。因此与完整目标的唯一实际连接仍是旧式
\[
 Q_\zeta(r,s)=q_\Gamma(r,s)+
 \mu_+(r)\overline{\mu_-(s)}
 +\mu_-(r)\overline{\mu_+(s)}-C_N(r,s),
\]
其中 \(q_\Gamma\) 保全部 \(2\theta'\)／FP-contact，\(\mu_\pm(r)=\int e^{\pm u/2}r(u)du\)。未新构造这两项，未得到它们与(1)的独立净预算。

同向 Dirichlet 卷积本身不是 Gram；(1)的 Hermitian 化也不是平方。将它当正型需要额外定理，当前没有。不能把“希望 \(\Gamma+\mathrm{pole}-C_N\ge0\)”当作已经给出的独立 input。

## 最强旧与停止

最短扣除就是旧 \(\mu*\log=\Lambda\) 的逐系数恒等式。549／550已有真实 physical 余因子、共同 cross、actual II₂ 原 norm² O(1) 及完整型运输；本改写没有新增其未付的 actual \(\Lambda\Lambda\) near 差。也不把本任意 smooth 源自动套成550的特定方窗源族。

560早有同源完整 identity；fixed \(r\) 的 \(t-K=Q_\zeta-\mathrm{pole}\) 已是常数，585又付 \(t,K\) 的必要共同成长，不能再把该净差写出领作新输入。405／553全 Pan 与537非根、542＋555→557 whole4/5负惯性 UPPER 均未改变。

故本次是**正确旧编码、无合格新 formula／input，0数学**；不是反例或新方法类边界。停止这一尝试，不追加 Gamma 拟合、未知 domination、第二候选或来源链；不预建合同，不结算 cadence，不代 root 消费。
