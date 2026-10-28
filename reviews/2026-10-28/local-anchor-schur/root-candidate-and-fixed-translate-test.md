# 固定anchor的正Schur族：actual规则、平移test与新弱源门

2026-10-28；同G20261027/runtime1793085111/原0c4f。C050/587已完成且不续degree/rank/log优化。本稿形成不同的actual growingrank正form规则并执行最便宜目标比较，当前仅准入草稿，未预C051/588或新source预算。

## 一份非空且不依赖K的正form候选

T_X(r,s)=Tr(A_rΠ_XA_s*)取560/585同一实际Sonin正迹，ρ与原du/Dlog/Fourier规范不改。固定I₀=(-17/16,17/16)、587的r₀及其导数。537已付完整Q_W在Dlog(I₀)的coercivity

\[
 Q_W[q]\ge\tau\|q\|_{du}^2,\quad\tau=2^{-49162}.
\]

令m_X=⌊logX⌋、E_X=span{r₀,…,r₀^(m_X)}。每finite X，T_X的有限Gram正定：原ρ_X在充分高频为log型正值，非零compact源的entire Fourier不能在该区恒零。P_X为到E_X的T_X-orthogonal源投影，由原Gram全逆定义，即T_X(P_Xr,e)=T_X(r,e)对所有e∈E_X。这里不是receiver projection；其系数可大，不宣称du norm有界。

定义共同Hermitian正form

\[
 W_X(r,s)=T_X((I-P_X)r,(I-P_X)s)+Q_W(P_Xr,P_Xs).\tag{1}
\]

每层有限源域合法，两个对角项均非负；对r∈E_X精确有W_X[r]=Q_W[r]。这一规则用actual T与已知local Q，不按未知K反定义补偿，source校正维数可成长，因而587的固定rank上限结论不能单独判它。

一般W_X只是源上的正Hermitian form，有限层不自动translation invariant，不能冒称单变量正D′分布。仍可合法检验更弱但充分的目标：对全部fixed compact complex源W_X[r]→完整Q_W[r]。若成立，极限的正性足以进入完整Weil标准；有限层的stationarity未付不能当作已付。

## 固定平移是实际目标控制

取a=4、r_a(u)=r₀(u−4)，support[3,5]与I₀分离。它是一个先fixed的原physical源，不是a_X moving test。完整autocorrelation不变，双pole Lorentz差也精确平移不变，故537/完整字典给

\[
 Q_W[r_a]=Q_W[r_0]>0
\]

为已知固定有限数；Γ/FP-contact、全部properpowers与双pole均未删。正迹T_X同样translation invariant，所以bare T_X[r_a]也等于T_X[r₀]并发散，但这本身不能直接判含growingrank source projection的(1)。

若(1)在这个fixed r_a上有一条有界子列，记q_X=P_Xr_a，正分解及τ强制

\[
 \|q_X\|_{du}\le C,\qquad T_X[r_a-q_X]\le C.
\]

所有q_X支持共同I₀，弱紧子列给q_X⇀q∈L²(I₀)。因此f_X=r_a−q_X支持共同fixed J、du有界且弱极限r_a−q≠0。这里需要的**新门**是：actual Sonin正迹是否对这种moving源仍必趋∞？不能把585逐fixed源或587的fixed derivative空间下界直接套到f_X。

## 可核查的新弱源比较

若f_n在共同fixed compact J内du有界并弱收敛到f≠0，则F_n=Fourier(f_n)由共同support形成normal family，弱收敛给locally uniform entire极限F。令k=ord₀F有限，选一次fixed小complex圆盘，F在其中只有0处k重零。Rouché给F_n恰k根并都趋0；提出monic P_n后，G_n=F_n/P_n在更小fixed core有统一正模lower。

若这一因子化/源域链核闭，就能在587的actual frame运输中以|F_n|≥c|P_n|替代固定hP；degree k先fixed、P_n monic所以coeff norm≥1，得到T_(X_n)[f_n]≥c√X_n/log^(3k+2)→∞。δ与c_δ只作由非零弱极限决定的一次性receiver proof witness，不改变候选m_X/P_X/r_a规则，也不声称d_X成长或全du单位球uniform。

这会对(1)给一个真正的fixed-source发散反测，而非只说projection合法/正性等价。更强的同链scope不要求q_X线性、幂等或T正交：对任何q_X(r_a)支持共同I₀的合法选择，正分解T_X[r_a−q_X]+Q_W[q_X]若有界都受同一矛盾。因此可涵盖任意growing/infinite局部range及source-adaptive选择，但只在两项非负、residual系数固定1和共同compact anchor的明示类内。

当前两独占准入审将核actual公式、537原coercivity、最强旧覆盖、normal family/Rouché/core参数与ordinary trace域。尚不把新弱源lemma或类边界标proved；若旧已直接覆盖则0止。Growing/unbounded anchor、另缩放T、添加有符号cross/counterterm、不同actual正族不由本题排除，其标签也不自动成为后继输入。原Goal/基线及cadence1/history51/latest587/formal17在根结算前不动。

## 根准入

两当前具体终稿12027b/2a9a3678与12081b/d31a65b5已root全文核。actual formula/κ du/固定a=4目标与new weak-source运输前件对齐，原件已包含可逆审证明链；仅准C051一次完整闭合/逆审，不因改名重推，不续587参数或source。positive form与Dprime类型分开；候选finite Gram正定/全逆/域已付，弱源lemma及fixed-anchor强scope待当前root/fresh最终消费。准入0，原cadence1/history51/formal17保持。
