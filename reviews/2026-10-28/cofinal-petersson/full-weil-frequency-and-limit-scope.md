# 固定未平均Pet覆盖塔：完整Weil高频与逐源极限范围

2026-10-28；/root/pet_gamma独占稿。恢复G20261027、STATE、C047已耗预算、D20261028A及唯一cofinal Pet准入；本稿只核最强旧552§5输入和极限反测。不调level/ray/weight或Pet规范，不读新外部论文，不改STATE/cadence/Git。局部evaluation费用由独占local稿另付；本稿不以其草案存在代前件闭合。

## 1. 原对象、全项与准确规范

物理源r=e^(u/2)f_phys，原du就是Lebesgue du，固定I*=(-17/16,17/16)。记

\[
 F_r(z)=\int r(u)e^{-izu}\,du,\qquad
 h_r(a)=\int r(v+a)\overline{r(v)}\,dv.
\]

已root消费的[537](../../../notes/537-source-exact-weil-window-positive-tail-admission.md)§2及[c009对象审查](../../2026-10-14/c009-tail/object-source-audit.md)§1给全部complex Cc∞(I*)的完整几何侧：

\[
 Q_\zeta(r)=P(r)+\frac1{2\pi}\int_{\mathbb R}
        \Gamma(\tau)|F_r(\tau)|^2\,d\tau
       -\sum_{\substack{n\ge2\\ \log n<17/8}}
          \frac{2\Lambda(n)}{\sqrt n}\operatorname{Re}h_r(\log n),
 \tag{1}
\]
\[
 \Gamma(\tau)=\operatorname{Re}\psi(1/4+i\tau/2)-\log\pi
             =2\theta'(\tau),\qquad
 P(r)=2\operatorname{Re}\!\left[F_r(i/2)
                                  \overline{F_r(-i/2)}\right].
 \tag{2}
\]

此处ψ是digamma；下节的源bump另记χ以免混名。原norm的Plancherel规范是(2π)^−1∫|F_r|²=||r||du²，因而leading系数不会多或少一个2π。式(1)保完整Γ/contact常数，不以half helper替代2θ′。全部非零prime powers恰为2、3、4、5、7、8，Λ(p^j)=log p；不存在只保primes、把Λ(8)改成log8或删proper powers的操作。对更小源支持，某些h_r实际为零，但仍是同一完整式。

双pole不是总非负：若C_r=∫r cosh(u/2)、S_r=∫r sinh(u/2)，则P(r)=2(|C_r|²−|S_r|²)。本稿用完整P而非只保even正腿。所有源均complex，未假定任何ζ-zero ordinate为实。式(1)的几何侧及以下论证不依赖RH。

## 2. 已付高频式的直接核对

固定任意非零χ∈Cc∞(I*;C)，取

\[
       r_R(u)=\chi(u)e^{iRu},\qquad R\to+\infty.
\]

有||r_R||du²=||χ||du²、F_(r_R)(τ)=F_χ(τ−R)，且h_(r_R)(a)=e^(iRa)h_χ(a)。因此式(1)全部prime-power项的绝对值统一不超过

\[
 \left(\sum_{n\in\{2,3,4,5,7,8\}}
       \frac{2\Lambda(n)}{\sqrt n}\right)\|\chi\|_{du}^2.
 \tag{3}
\]

这仅用平移的原L² Cauchy–Schwarz；没有随R扩prime支持或漏全尾。对两个pole矩，e^(±u/2)χ仍为固定smooth compact函数，反复分部积分给

\[
 F_{r_R}(\pm i/2)=O_{A,\chi}(R^{-A})\quad\text{对每个固定 }A>0,
 \tag{4}
\]

故完整P也快速衰减，并非先删pole再调制。

digamma实际乘子满足Γ(τ)=log|τ|−log(2π)+O(1/|τ|)于|τ|→∞，在全部实τ上smooth且|Γ(τ)|≤C+log(2+|τ|)。这是552§5已消费的同一输入；下述只是核其量词/规范。令s=τ−R。对|s|≤R/2，用大参数式和|log|1+s/R||≤log2得到Γ(R+s)−log R一致有界；在补集用F_χ的任意阶Schwartz尾控制，包括R+s接近0的区域，Γ此处本来有界而无对数奇点。于是

\[
 \frac1{2\pi}\int\Gamma(R+s)|F_\chi(s)|^2ds
       =\log R\,\|\chi\|_{du}^2+O_\chi(1).
 \tag{5}
\]

结合(3)–(5)得到最强旧[552§5](../../../notes/552-radial-adelic-green-principal-and-comparison-gate.md)已明示的结论：

\[
 \boxed{Q_\zeta(r_R)=\log R\,\|\chi\|_{du}^2+O_{I_*,\chi}(1),
       \qquad \|r_R\|_{du}^2=\|\chi\|_{du}^2>0.}
 \tag{6}
\]

I*固定，χ也先固定；O常数不声称对所有单位L² bump统一。换R→−∞同理。该式表明完整Q在这个固定窗不是du有界二次型，且高频值趋正无穷；它不是Q负方向或RH反例。自然zero-extension Dlog/Hlog型费用沿调制增长，未称原du有界就自动给强型界。

## 3. 如需精确双polezero，也能保同一式

本次所拟逐compact源极限本来包括全部Cc∞，所以(6)已够反测，无须添加polezero约束。若另需展示两个pole矩精确为零的合法测试，也可只用两个**固定**模板；这不是逐层消noncompact Pan。

令M_±(r)=∫r(u)e^(±u/2)du。取非零、非负、even η∈Cc∞(I*)，令

\[
 b_0=\frac{\eta}{\int\eta\cosh(u/2)du},\qquad
 b_1=\frac{u\eta}{\int u\eta\sinh(u/2)du},\qquad
 \eta_\pm=(b_0\pm b_1)/2.
\]

两个分母严格为正，M_σ(η_τ)=δ_(στ)。所以

\[
 \widetilde r_R=r_R-M_+(r_R)\eta_+-M_-(r_R)\eta_-
 \quad\text{满足 } M_\pm(\widetilde r_R)=0.
 \tag{7}
\]

M_±(r_R)均为O_(A,χ)(R^−A)，故修正在全部固定源半范数及Dlog型norm均快速小。不能仅因L²修正小就假设不连续的Q自动近；准确运输为：在fixed窗，Γ与log(2+|τ|)可比，prime/pole为du有界扰动，因此Q的极化对zero-extension Hlog型norm连续。调制源的该norm为O_χ(sqrt(log R))，固定模板norm有限，故

\[
 Q_\zeta(\widetilde r_R)-Q_\zeta(r_R)=o(1),\qquad
 \|\widetilde r_R\|_{du}^2\to\|\chi\|_{du}^2.
 \tag{8}
\]

于是Qζ(tilde r_R)/||tilde r_R||du²→∞同样成立。polezero不是Pan成员身份；没有将Cc∞中的非零函数宣称成完整405关系。这里完全是552所给固定模板修正的显式核对，不是新费用定理。

## 4. 与独占local费用的消费接口：先固定源，再取level极限

冻结准入中的Γ_n=Γ(N0 n!)、κ3/2 restricted automorphy、原未平均Pet规范和实际A_n/G_n。下面只需另稿/root实际闭合的单一前件：存在有限C_(I*)，独立n与r，使

\[
        G_n(r,r)\le C_{I_*}\|r\|_{du}^2
        \quad(n\ge1,\ r\in C_c^\infty(I_*;\mathbb C)).
 \tag{9}
\]

设(9)已按同一源map/norm闭合。如果对每个固定compactcomplex源都有G_n(r,r)→Qζ(r)，则逐源取极限直接给Qζ(r)≤C_(I*)||r||du²。由(6)，先选一个充分大但**有限、固定**的R0，使

\[
 Q_\zeta(r_{R_0})>(C_{I_*}+1)\|r_{R_0}\|_{du}^2.
\]

这个选择与n无关；之后对所有n都有一个相同源上的完整signed缺陷：

\[
 Q_\zeta(r_{R_0})-G_n(r_{R_0},r_{R_0})
       >\|r_{R_0}\|_{du}^2>0.
 \tag{10}
\]

所以该源上的逐n收敛失败，更不可能对全部Cc∞有所拟极限。可用(7)的精确polezero源替代，但并无必要。没有用依n变化的r_n否定逐源收敛，也不交换高频与level的两个极限。

Gram的complex极化定义清楚，若曾有全部diagonal源极限便能传mixed；(10)已经在diagonal否定它，无需额外交换polarization或拓扑。逐层G_n没有被要求消noncompact Pan；本门只用(9)与完整Q高频，不借旧fixed A精确Pan像结论，也不从“PSD”单独推出失败。没有ordinary trace或算术height前件。

## 5. 强旧净值、停止与未排范围

高频式(6)及固定模板费用已由552/536/537付清，本稿恢复准确对象、全项和顺序。若local费用只是标准嵌入圆盘/holomorphic均值/Riesz evaluation，则(9)+(6)的反测为**标准最强旧直接合成0数学轮**，止这个固定、原未平均Pet正Gram覆盖塔的逐compact源极限recipe。并非新classic正号、whole预算或实质全方法类边界。

若local(9)未闭合，本稿反测仍为准确conditional接口，不能以某个上界证明失败推断极限成立；root须定位实际缺费。体积平均norm、发散level Gram权、非局部或source适应读出、不同实际arithheight/relative载体均会改变(9)的前件或源map，不受本稿自动排除，也不能默改当前family来宣称它逃过检验。各修复须另有实物、原norm及完整signed误差。

经典primitive桥/整过滤/截面乘法/mixedRR、完整signedgrowth/actualq/core/coupling/Ξ瓶颈未变；542＋555→557仍只是whole leading4/5负惯性UPPER，537固定窗正性不升级成长。原literal theta源及整体7.4/modularity/算术Theta身份冻结保持，不借任何新论文或新cited输入。无新下载/网页/PDF阅读，本稿只写本独占路径；出稿不代root消费，Goal完整门仍open。
