# 577后 prime／pole signed 预算：历史去重与 Selberg 单来源门

2026-10-22；独占分支原稿。冻结 G20261014／0c4f，未修改 STATE、cadence 或主稿。恢复时 C040/577 已完成，cycle15 后 cadence=0；本分支不自行结算轮数。查找只作相关族代表核读，不声明重证全部笔记或全球新颖性。

**结论。** Selberg 1949 §2 的对称公式提供真正独立的乘法卷积预算；它不是577实际线性符号的 Hermitian 正型估计。完整补回 prime powers 后误差仍可付，但现有量词和权不能使实际 q_R 消失。更具体地，562已有的连续正反两段均满足同样的 Selberg 型二次总量主项及 O(X) 误差。因此“该总量＋PNT＋正 primitive＋自对偶”不可能单独选择正号；这只排所述粗数据包，不排完整精细卷积身份、twist、同源 Γ 协同或独立容量的新用法。没有以未知零点选系数。

## 1. 恢复的对象及最强已付后果

物理源始终为 r=e^{u/2}f，hat r(t)=∫r(u)e^{-itu}du，du 为原范数；全 complex、原 zero-extension Dlog、完整 Γ/contact/FP、Λ(p^k)=log p 及双 pole 均保留。577 的对象为

\[
 G_R=W_\Gamma+\phi_R(H-P),\quad
 g_R=\widehat G_R,\quad q_R=(-g_R)_+,\quad
 c_R=\|q_R\|_\infty,\quad m_R=(2\pi)^{-1}\|q_R\|_1.
\]

每层连续正谱证书已由 q_R 构造；未付的是实际 c_R／m_R／K_R 的消失。Γ 协同 μ_R 的原 du 与 Fourier-L¹ 均为 O(R⁻²)，这不能向 q_R 自动运输。fixed 源窗 [-L,L] 的完整误差为

\[
 D_L/R^2+\min(c_R,2Lm_R),\qquad
 D_L\ll(1+L^2)e^L.
\]

必须分别保留 fixed L、L=L(R) 成长和全部支撑量词。完整目标已在 D′ 被 G_R 逼近；正修补消失仍是577已核的 Weil 正性／RH 等价条件。

历史检索后直接核读的最强相关资产：

| 已有原件 | 可消费结论 | 不能升级为 |
|---|---|---|
| [036 §4–5](../../../notes/036-max-kernel-prime-square.md) | Selberg 的乘积卷积与 discrepancy 的 max-kernel 平方逐系数不同；n=6 即有实际反测。subpower PNT 包络不跨固定临界幂门 | 用“平方”一词把乘法卷积当全 Weil Gram |
| [169 §1–3](../../../notes/169-selberg-profile-rh-equivalence-resonance-wedge.md) | 独立微窗 incidence 及平方根外 wedge；所需 polylog 乘法 Selberg profile 已是 RH 强度 | 已知无条件的全部尺度 prime-pair 小量 |
| [294 §1–2](../../../notes/294-pnt-envelope-gain-and-fixed-source-saturation.md) | 完整原子／匹配连续端点，PNT 后 Abel 包络真有 stretched-exponential 节省 | 临界加权实际 signed 小费；本轮不重做来源常数 |
| [299 §1](../../../notes/299-local-one-sided-budget-mellin-strength-audit.md) | 特定完整匹配候选的 fixed 频窗一侧 polylog 预算仍等价 RH | 任意“只是局部一侧估计”即低于 RH；也不直接移植其结论到不同 φ_R |
| [548 §1–4](../../../notes/548-canonical-weil-mixed-response-and-critical-input-boundary.md) | actual canonical mixed 响应与临界 Chebyshev 场只差原 norm O(1)，其 subpower／polylog 目标仍 RH | 独立新算术界或任意 head 的共同 Γ 费用 |
| [550 §2–5](../../../notes/550-physical-row-mixed-source-admission-and-strong-old-aggregate.md) | 完整 AP/prefix 与筛/Haar 正 Gram 已付 actual topband O(1)，优于弱 log 预算 | ΛΛ near 差、全部 height、全部算术尺度或全源 Gram |
| [555 §1–4](../../../notes/555-actual-prime-weighted-schur-and-growing-weil-inertia.md) | ALL L、ALL 原 complex 源的实际 prime 行 norm~e^L | signed 负部小量；非负 kernel 不等于 PSD |
| [557 §1–4](../../../notes/557-joint-row-norm-and-gamma-arithmetic-moment-budget.md) | 542＋555 的 strongest-old whole leading 4/5 负惯性上预算 | 负谱 lower、core／coupling／Ξ 或正性 |

174 的正锥投影、576的正型闭包及577的取负部均不重计为 prime-side 来源。上述旧资产已经覆盖本分支能直接消费的粗预算；不得以弱逐项 Λ≤log n 界制造净值。

## 2. 唯一外部章节：Selberg 1949 §2，式(2.8)

已浏览原始论文扫描：Atle Selberg，*An Elementary Proof of the Prime-Number Theorem*，Annals 50 (1949), 305–313，[原件 PDF](https://www.math.lsu.edu/~mahlburg/teaching/handouts/2014-7230/Selberg-ElemPNT1949.pdf)。核读范围仅 §2／印页307–310，特别印页309的(2.8)及(2.9)，并核前页定义和 prime-power 误差位置；没有连续串下一 paper。网页 OCR 的数学下标不完整，公式按原文结构与相邻等式核对。

原式是

\[
 \sum_{p\le X}(\log p)^2
 +\sum_{pq\le X}\log p\log q
 =2X\log X+O(X),                                      \tag{S}
\]

第二项为有序 prime 产品，含 p=q。其证据类型是独立算术总量恒等式，不是 square-integrability 或 Hermitian 正性定理。原文从 Möbius 除数展开推出此式；这里不把原文结论扩展到任意 Beurling 系统。

### 2.1 完整 Λ 版的补幂费用

为和本项目目标同对象，必须补回全部 powers，不能直接以 θ 代 ψ。设 a(n)=log p 当 n=p，其余为0，b=Λ−a。由旧 Chebyshev 及初等幂计数，

\[
 \sum_{n\le X}b(n)\log n=O(\sqrt X\log^3(2X))=O(X).
\]

卷积差非负，且

\[
 0\le\sum_{mn\le X}[\Lambda(m)\Lambda(n)-a(m)a(n)]
 \le2\sum_{p^k\le X,\ k\ge2}\log p\,\psi(X/p^k)
 \ll X\sum_p\sum_{k\ge2}\frac{\log p}{p^k}\ll X.
\]

最后级数由 Σ_{n≥2}log n/[n(n−1)] 收敛控制；所有端点原子均为全权。所以(S)可合法消费成

\[
 S_\Lambda(X):=\sum_{n\le X}\Lambda(n)\log n
            +\sum_{mn\le X}\Lambda(m)\Lambda(n)
 =2X\log X+O(X).                                      \tag{SΛ}
\]

这只是标准补幂／原件范围运输，未缩小577的实际补偿。

### 2.2 它控制了什么，尚未控制什么

在绝对收敛 Re s>1 内，D(s)=ΣΛ(n)n⁻ˢ 满足

\[
 -D'(s)+D(s)^2=\zeta''(s)/\zeta(s).
\]

这里的平方是 holomorphic 乘法平方；复频率上 Re(D²)=(Re D)²−(Im D)²，没有 Hermitian 正号。它也不是577的 Γ＋两 pole−对称 prime 线性符号。将正 Dirichlet 系数当成 Fourier 正谱，类型已变。

即使将(SΛ)的 remainder 用577的完整权 x⁻¹ᐟ²φ(log x/R)cos(t log x)进行 Stieltjes 测试，直接 Abel 绝对估计也只给 O((1+|t|)e^{R/2}) 的粗包络：对 U(X)=SΛ(X)−2Xlog X，U=O(X)，上下端匹配，∫w dU=−∫U w′。该包络既不是趋零，也没有给 g_R 的有符号方向。此处宽支撑 R 的粗量级只是上界，不是实际必要费用。

额外责任有三项：从微分／卷积组合回到实际线性 g_R 的同源比较；全部 twist/window/边界的 signed 误差；以及与完整 Γ/contact、双 pole、全部 powers 的预算协同。若把这三项简写成 g_R≥−ε_R 或 ||q_R||₁→0，即返回577已核的等价责任。

## 3. 连续正反例对(SΛ)粗数据包的实际检验

不是只说“正数据不能推出正性”。取[562 §2](../../../notes/562-generalized-rh-continuous-g-integers-and-spectral-multiplicity.md)已付的 genuine positive primitive／g-integer 族，模型自身 Γ=0、两 poles 全保。α+β=1、αβ=c，全部 prime powers 的 log-Chebyshev 密度为

\[
 \lambda_c(u)=u q_c(u)=e^u+1-e^{\alpha u}-e^{\beta u}\quad(u\ge0).
\]

取577的两个具体 native 对照：c=3/16 时 α=3/4、β=1/4，W_−=2cosh(u/4)；c=5/16 时 α=1/2+i/4、β=1/2−i/4，W_+=2cos(u/4)。二者 λ≥0：前者等于(e^{3u/4}−1)(e^{u/4}−1)，后者由 cos≤1 及 e^u+1≥2e^{u/2}给出。positive primitive 的全 Euler 反演则引用562原证明，不只验证 λ≥0。

令 d(u)=1−e^{αu}−e^{βu}。有 |d(u)|≤Ce^{bu}，b=max(Re α,Re β)<1。普通半线卷积直接给

\[
 \begin{split}
 u\lambda_c(u)+(\lambda_c*\lambda_c)(u)
 &=2u e^u+2e^u\int_0^u e^{-v}d(v)dv
       +u d(u)+(d*d)(u)\\
 &=2u e^u+O_c(e^u)+O_c(u e^{bu}).
 \end{split}
\]

因此对全部 X≥1，

\[
 \boxed{\int_0^{\log X}[u\lambda_c(u)+(\lambda_c*\lambda_c)(u)]du
             =2X\log X+O_c(X).}                         \tag{C}
\]

同时 Ψ_c(X)=∫₀^{log X}λ_c(u)du=X+O_c(X^b+log X)，所以两段均有真正 PNT。式(C)是(SΛ)的同类型二次总量，不声称是经典整数的 Möbius 除数恒等式在所有细节上的几何实现。

两模型对相同粗数据包给相反结论：正段 q_R=0；负段577已有实际 compact 双 pole-zero 源 r_−，Q_−(r_−)<0，故补偿在该实际源上的 liminf≥−Q_−(r_−)>0。因此“正 primitive＋PNT＋自对偶＋(C)的 O(X) 总量”不能支付 q_R 消失。

这个连续反测只排所列 sufficient package；它不排独立获得比(SΛ)更精细的 twisted／source-adapted 同源信息。若root把它消费为新增完整准入反例，须按仓库规则判断研究轮；本分支不因它属于来源审查就预先固定为0轮。

## 4. 函数域与405／537的责任

真函数域原料应保全部 n returns、周期 poles、全部 aliases 和 native contact。已有 positive H／RR 给全周期 W_C 正型，故其577同型 hard 修补为0。即使有同类正系数乘积总量，其正号来源仍是已付同对象几何极化，不能归给(S)粗主项。不能加经典 Γ 改模型后宣称源身份未变；ordinary trace／几何 lift也另有责任。

405实际关系是非 compact 的全 Pan 族及其所有平移，位于原 S_exp 强拓扑；Bζ(p,s)=0 无条件。577每层保真Γ的连续高频正谱却给所有非零 Pan 的 Q_V(p)>0，所以逐层不下降该商。固定强源可按577(17)另付 O(R⁻²) 裸层尾；正修补还须按实际 c_R 或 m_R 计费。Selberg总量不自动覆盖此全族，更不能用 compact 交集空洞地检查关系。

537原 L₀=17/16 fullcomplex du／Dlog 正窗无条件最终保留，因为 Q_K≥0 与裸层 signed 误差足够；这不先要求补偿消失。它保非根可见性，不证明任意成长窗正号。553的 Pan 全线 Hlog 稠密障碍仍在：固定源强拓扑收敛、D′、fixed窗全部原源统一、成长共同预算和全线 Hlog operator统一绝不能合并。

## 5. root消费建议与停止

独立来源已核：Selberg §2(S)，补幂O(X)运输；具体连续双符号(C)对该粗package的反测。未付：实际 q_R 的任何独立 signed 小量预算，没有新 prime-pole／Γ同源平方和、RR容量或 source-map。

最强旧净后果仍542＋555→557 whole leading4/5负惯性上预算；本分支不改变actual core、coupling、Ξ或完整Weil符号。不能把将来所需的 g_R≥−o(1)、小negativepart、positive limit membership 或“容量差”登记为本次新输入。

建议结束这个(S)章节来源门。root已经选定把本次新执行的“连续双符号完整Selberg联检＋实际补偿费用反测”作为 C041／578 的一轮具体准入检验统一结算；本来源子稿不另计轮，也不把(S)本身晋级成新的正性输入。没有新增精细 twisted 身份及可核原费用前，不再串 Selberg、Brun、Bombieri 或 Connes paper制造下一来源。允许将来的真实同对象 signed 估计／primitive RR作为重新准入实物，等价性本身不禁止独立证明。局部反测和选择信息可更新，宏观独立容量瓶颈未改变。
