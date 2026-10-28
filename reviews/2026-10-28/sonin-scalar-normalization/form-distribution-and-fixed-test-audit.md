# Scalar归一化actual Sonin：正型分布及固定导数test准入

2026-10-28；`/root/rational_first_gate` 当前独占具体审稿。已恢复README／STATE、check→show、同G20261027/runtime1793085111/原0c4f、AI、frontier／summary，并读[root新规则稿](root-formula-and-relative-test-admission.md)。C051／588 completed，cadence2/history52/latest588/formal17；本稿不续C051，不改STATE／共享文件／Git／cadence，不准新合同或计轮，不web／下载／证明新upper／读6.4proof。只核这一scalar rule及r₀′固定test。

**裁决：规则合法且非空，确为stationary tempered正型分布；有限分母严格正，原2π规范可闭。必要比值是实际同一T_X的 `T_X[r₀′]/T_X[r₀]→q₁/q₀>0`。当前已付旧lower／553／587／588没有足够前件直接判该比值，不能将两个lower相除。** 精确未付量是r₁的relative upper／同源渐近；当前原件已定位的Th6.3 zero-mean little-o是足够而更短的接口，尚未在本审认证其proof。

## 1. Actual规则、源域与有限分母

使用587同一literal实偶bump

\[
 r_0(u)=c\exp[-1/(1-u^2)]\quad(|u|<1),\qquad r_0=0\text{ elsewhere},
 \quad\|r_0\|_{du}=1,
\]

以及560／585同一actual Π_X／完整有限Euler Gram inverse／returns。源为physical `r=e^(u/2)f`，Fourier `rhat(t)=∫r(u)e^(−itu)du`。finite-X ordinary迹为

\[
 T_X[r,s]=\operatorname{Tr}(A_r\Pi_XA_s^*)
 =\int\widehat r(t)\overline{\widehat s(t)}\rho_X(t)dt.
\]

第一槽线性、第二槽共轭；rho已含原求值规范，不另加除2π。ALLcompact smooth complex源合法；在每fixed bounded J上，natural closed form域为zero-extension Dlog(J)，见560 §4及[588 §3](../../../notes/588-common-support-sonin-weak-coercivity-and-local-anchor-barrier.md)。仅L²不自动支付ordinary trace。

令 `q₀=Q_W[r₀]`。537原完整型给 `q₀≥κ=2^-49162>0`，且q₀有限。每个finite X，ρ_X≥0并在充分高频与log(2+|t|)相当，非零compact r₀的Fourier entire不能在实区间恒零，故

\[
 0<T_X[r_0]<\infty.
\]

因此题定唯一规则

\[
 \alpha_X=\frac{q_0}{T_X[r_0]}>0,\qquad
 W_X(r,s)=\alpha_XT_X(r,s)\tag{1}
\]

在每层都可代入，并有 `W_X[r₀]=q₀` exact。585的fixed r₀ lower给T_X[r₀]→∞，所以α_X→0。没有通过全局Q正号、未知K谱或按完整target误差反定义alpha；只用了已经独立证明正性的一个局部常数。

## 2. Tempered正型分布、stationarity及2π

560的fixed finite-F密度有 `0≤ρ_X(t)≤C_X[1+log(2+|t|)]`。这是逐X常数，不声称X一致；足以使ρ_X(t)dt为positive tempered spectral measure。

对φ∈Schwartz空间，明确以complex-linear分布作用定义

\[
 \mathscr W_X[\phi]
 =\alpha_X\int\rho_X(t)\widehat\phi(t)dt.\tag{2}
\]

绝对可积性及Schwartz seminorm界使 `𝒲_X∈S′⊂D′`。令 `tilde s(u)=overline{s(−u)}`，则 `widehat(r*tilde s)=rhat·overline(shat)`，故

\[
 \mathscr W_X[r*\widetilde s]=W_X(r,s),\qquad
 \mathscr W_X[r*\widetilde r]\ge0.
\]

这里是**positive type／正型**，不是声称物理u侧𝒲_X为正Radon测度。其source form对共同平移stationary，因为Fourier相位在rhat·overline(shat)中相消；与前个nonstationary anchor-projection form不同。

在当前 `hatφ(t)=∫e^(−itu)φ(u)du` 约定下，(2)的Fourier transform为 `2π alpha_X ρ_X(−t)dt`。旧actual实结构给ρ_X偶，故

\[
 \widehat{\mathscr W_X}=2\pi\alpha_X\rho_X(t)dt.
\]

不是alphaρ而遗漏2π；也不能在(2)或actual T积分中再除2π。原Plancherel dt/(2π)属于physical／trial Hilbert norm，rho已按560吸收相应系数。

目标是D′意义的**完整**Weil distribution／相应ALLfixed compact complex source form。每层tempered不等于已付uniform S′界或S′极限，也没有在这里先假设完整目标已是tempered正型（那会偷用所求全局正号）。至少逐fixed卷积平方的收敛仍是该目标的必要条件。

## 3. r₁固定test与完整q₁

唯一不同fixed test取 `r₁=r₀′`，非零且support仍为[-1,1]；不是moving source／frequency／window。其原du／Dlog norm有限固定，`rhat₁(t)=it rhat₀(t)`，且

\[
 \int r_1=0,\quad\widehat r_1(0)=0,
 \qquad q_1=Q_W[r_1]\ge\kappa\|r_1\|_{du}^2>0.
\]

q₁包含完整Γ/FP-contact、全部Λ(p^k)=logp和双pole。mean zero不是双pole矩零；由IBP，`μ_±(r₀′)=∓(1/2)μ_±(r₀)`，odd负pole仍须保留。不能因F₁(0)=0而删除pole项或把q₁换成arch-only型。

若(1)的完整目标成立，则在同一fixed `h₁=r₁*tilde r₁` 上必须有

\[
 \boxed{R_X:=\frac{T_X[r_1]}{T_X[r_0]}
 \longrightarrow\frac{q_1}{q_0}>0.}\tag{N}
\]

所有分子／分母／target都是同一actual规范。等价地，令

\[
 d\nu_X(t)=\frac{|\widehat r_0(t)|^2\rho_X(t)dt}{T_X[r_0]},
 \qquad \nu_X(\mathbb R)=1,
\]

则R_X就是这份**actual**加权spectral probability的t² moment。这是(1)的必要relative量，不是另一生成规则或从Gaussian trial measure读出的moment。

(N)若失败就停止这份固定scalar rule；若通过也仅是一项必要test，不能据两源匹配推出ALLsource／D′收敛或RH。所有r₀平移的对角已因stationarity自动匹配，因此固定r₀′确实提供不同信息，而不是重验归一化等式。

## 4. 最强旧为何尚未直接判R_X

* **585。** 已付 `T_X[r₀]≥c₀√X/log²X`，也付r₁自己的lower。两个lower不能相除得到R_X的upper／极限。特别不能写 `R_X≤C/log²X`；此式需要numerator upper而非lower。
* **587。** actual fixed-degree Gram共同lower是lower／cross费用，未给本test所需fixed-source upper或r₁/r₀相对渐近。alpha_X乘同一Gram后没有可免费消费的denominator upper。
* **588。** commoncompact弱非零源迫unscaled T_X发散、fixed-anchor正分解的迹系数有统一正lower；当前alpha_X→0正好不满足该类的trace-weight前件。两个发散量的比值不由weak coercivity或strong resolvent0决定。
* **553。** 其退化门须有全域fixed有限Hlog／有限Sobolev读出界，并正确杀全405 noncompact Pan关系。这里每层虽有finite-X Hlog费用，但其常数 `alpha_X C_X` 没有uniform证书，逐层Pan下降也未给；D′compact-source中间层本不要求逐层精确杀Pan。不能因它是positive Hilbert／tempered分布而免费套553。

此外，finite-X Γ符号的系数被alpha缩小不等于完整目标的Γ可删：成长prime／ε项可能在极限承担非trivial分布，尚未有合法逐项极限。对每个fixed compact r，仅在可见prime已全覆盖后，旧完整字典准确给

\[
 W_X[r]-Q_W[r]
 =(\alpha_X-1)Q_W[r]-\alpha_XP_{pole}[r]
                  +\alpha_XK_X[r].
\]

本式没有证明所需normalized K净信息；它只保完整target，不能将未付项删掉制造反证。当前没有足够已付exact前件直接排(1)，也没有因这些合法逃逸自动证明该rule成功。

## 5. 精确未付接口：只需zero-mean upper

足以拒绝(N)的一项最短同源输入是

\[
 T_X[r_1]=o(\sqrt X/\log^2X).\tag{U1}
\]

配585已付r₀ lower即得 `R_X→0`、`W_X[r₁]=q₀R_X→0`，与完整q₁>0冲突。这里没有证明(U1)，也不声称更强matching-order upper／sharp常数；(U1)只是准确标出未付估计。

Root另支给出的exact locator已按其指定范围核到现存固定v2 Markdown的[lines802–809／Th6.3 (6.11)](../../../literature/local/2026-10-28-core-source-location/bramble-trace-rstation-2-v2.md)：原陈述为

\[
 \limsup_{X\to\infty}\frac{(\log X)^2}{\sqrt X}\,\mathcal T_X(f)
 \le4|F(0)|^2,
\]

并明确注明F(0)=0时为little-o。若其**同一actual T字典、合法源域及证明**经另门闭合，则physical r₁满足F₁(0)=0，正好给(U1)。当前仅核这8行statement接口；未读／认证Th6.3 proof，未读6.4 sharp proof，未以作者标签／已定位／“未审”当成新定理或续章授权。

该接口不要求6.4sharp下界；r₀ denominator lower已经paid，q₁的完整正性也已paid。精确定位不等于数学消费，是否冻结这一命题的来源／证明门只由root另判，本稿不准新合同。

## 6. 当前准入结论与停止

实际input是(1)的唯一alpha及actual正密度，test是fixed r₁的(N)，未付net是同一T的relative upper；成功证明(U1)会拒绝这份scalar归一化族的完整逼近，而非普遍排所有消失迹权。没有泛库存／新载体／归一化或source参数形成任务。

本稿准确终态为：**规则／域／stationary正型S′类型通过；旧直接排除前件不足；必要比值未判；已有精确Th6.3 zero-mean接口，proof尚未消费。** 不将两个lower相除，不把未读upper当已证，不修改alpha／r₀／r₁／窗口去追匹配，不续C051或预C052／新轮数。

完整Weil正号、primitive/principal/mixed、signed/core/Xi与whole542＋555→557 leading4/5负惯性UPPER不因本准入改变；同实例Goal保持active/open/noteligible。cadence2/history52/latest588/formal17保持，STATE／Git／共享文件均未动。
