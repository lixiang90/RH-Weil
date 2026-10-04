# 四分量相对读出、最小维数与循环障碍的独立推导

2026-10-04。采用422已经核准的实际定义域及其四分量平移；接续423的标准α=σ⁻¹ Hochschild约定。本报告只写本文件，不改旧稿。以下是可核验的线性代数、连续函数域及复形计算，不是完整相对算术桥或RH证明。

## 1. 四分量确实给平移相容的多分量读出

记V=C⁴，列向量为 `d(f)=(λ_pq(f),e_p(f),e_q(f),f_c)`，基分别记t、p、q、c。t是开放普通迹方向。422的实际平移给

`S(a,b)(λ,e_p,e_q,c)=(λ−a e_p−b e_q+ab c,e_p−b c,e_q−a c,c)`。

令N₁、N₂满足

`N₁p=−t, N₁c=−q, N₁t=N₁q=0`，

`N₂q=−t, N₂c=−p, N₂t=N₂p=0`。

则N₁²=N₂²=0，N₁N₂=N₂N₁，N₁N₂c=t，并且

`S(a,b)=1+aN₁+bN₂+abN₁N₂`。

因此S(a,b)S(u,v)=S(a+u,b+v)。d是实际连续Γ-equivariant读出，不需scalar invariant。对开放余项r∈ℓ¹(Z²)，d(r)=(Σr)t，确实保留普通迹。以时间S₁系数取Tr_t后结论相同。

这已经构造一个合法的四分量augmentation：若仅要求平移相容并保留可见的普通迹方向，有限维augmentation不是不可能。其代价是平移表示不半单，有限部坐标不是不变scalar。

## 2. Coinvariant与invariant functional精确杀掉trace方向

Γ-coinvariant为 `V_Γ=V/span{(S(g)−1)v}`。两个生成元的像分别为span{t,q}和span{t,p}，故

`V_Γ≅C·[c]`，且 `[t]=[p]=[q]=0`。

若线性泛函ℓ=(A,B,C,D)在全部S(a,b)下不变，由ℓN₁=ℓN₂=0得A=B=C=0。因此

`(V*)^Γ=C·c*`。

唯一保留的scalar invariant方向是角点，不能读出开放普通迹。选择coinvariant再读scalar得到相同结论。尤其不存在 `λ+u e_p+v e_q+w c` 的固定纯boundary correction，使之成为平移不变且在开放理想上保普通迹。

这个结论无需同时使用两个生成元才能发现。对单个非零γ=(r,s)，设Rγ=S(−r,−s)，则

`ℓ(Rγ−1)=(0,Ar,As,Ars+Bs+Cr)`。

不变性迫使A=0。其余不变泛函满足Bs+Cr=0；虽然固定γ的invariant空间比全Γ大，trace方向仍被杀掉。单个非零扭曲所要求的scalar invariance也不能通过选一个额外不变边方向来保留开放迹。

## 3. 非分裂扩张：boundary correction为何必败

V中Ct是平凡Γ子模。令B=V/Ct，其坐标为(e_p,e_q,c)，作用为

`S_B(a,b)(e_p,e_q,c)=(e_p−b c,e_q−a c,c)`。

短正合列 `0→Ct→V→B→0` 的scalar有限部截面有缺陷

`ζ_(a,b)(e_p,e_q,c)=−a e_p−b e_q+ab c`。

它严格满足扩张的1-cocycle恒等式

`ζ_(g+h)(b)=ζ_g(S_B(h)b)+ζ_h(b)`。

改有限部为λ+χ(B)时，缺陷变为 `ζ_g+χ(S_B(g)b)−χ(b)`。但边向量p在S_B(1,0)下固定，而ζ_(1,0)(p)=−1；对任何χ，此处的coboundary为0。同理q在另一生成元给−1。因此该扩张不能Γ-equivariant分裂。这是“纯boundary correction失败”的精确扩张类见证，而不是缺乏某个合适参数的经验判断。

## 4. 任意维数augmentation的scalar不变读出仍不可能

设W为任意Γ表示，Q:V→W为equivariant线性映射，且L:W→C为Γ-invariant线性泛函。则LQ必为V上的invariant泛函，所以LQ(t)=0。因而任何维数的augmentation，只要最终还要求通过不变scalar方向读出非零普通迹，都不能修复。

同一障碍在实际函数域上更直接，不要求Q因子分解过V，也不要求finite dimension。设Q:E₂→W equivariant，L invariant，且对全部开放r有LQ(r)=Σr。取f=H(j)δ_{k,0}，则

`β_(1,0)f−f=−δ_(0,0)`。

不变性令左侧读出0，普通迹归一化令右侧读出−1，矛盾。即使额外坐标在trace-zero开放余项上非零，最终invariant scalar仍不能逃过此见证。

若W为有限维完全可约表示，且Q把开放普通迹映为固定非零向量t_W，则该平凡子表示可分裂，有invariant L满足L(t_W)=1，仍矛盾。有限维酉表示是特例；更一般的酉Hilbert表示也有由t_W给出的invariant有界scalar泛函，因此同样不可能。合法augmentation必须保留非半单扩张，或者放弃最终不变scalar迹读出。

这里的最终scalar要求是一个固定L:W→C，本身Γ-invariant。若读出还与随群作用变换的dual coefficient、链或几何数据配对，不再满足这个假设；本命题没有否定这种联合相对机制。能否实现它，须具体构造和比较。

## 5. 四分量线性模型的最小维数恰为4

**命题。** 若Q:V→W为Γ-equivariant线性映射，且Q(t)≠0，则Q单射；因此任何压缩四分量模型但保留trace方向的目标维数至少4。

证明：若v=A t+B p+C q+D c∈kerQ，施N₁N₂得到D Q(t)=0，故D=0。再施N₁得−B Q(t)=0、施N₂得−C Q(t)=0，最后A Q(t)=0。因此v=0。这个证明对W维数无限也成立，且不假定目标表示酉或半单。

等价地，V的每个非零Γ子模都含trace方向Ct。任何equivariant quotient只要丢掉一个非零方向，就同时丢掉有效trace方向；coinvariant是这件事的极端形式。V本身实现维数4的上界。

注意范围：这里只排除对完整Γ作用的equivariant压缩。若仅保留一个固定γ的作用，Jordan块大小可能更小，不能把全Γ的最小4维结论直接移用于一个生成元。

## 6. 实际E₂上的连续finite-dimensional augmentation也至少4维

下面不要求读出先因子分解过四分量；明确假设保留普通迹的方式为“开放理想仅映向一条trace轴”。

**命题。** 设W有限维、U₁,U₂为可逆且可交换的Γ表示算子，Q:E₂→W为连续equivariant线性映射。假定有非零t_W，使对每个r∈ℓ¹(Z²)都有 `Q(r)=(Σr)t_W`。则dimW≥4，且W中包含与上述V同构的四维非分裂Γ子模。

证明如下。开放平移保持全和，故U₁t_W=U₂t_W=t_W。置

`v=Q(H⊗H), x=Q(δ_0⊗H), y=Q(H⊗δ_0)`，

并令Lᵢ=1−Uᵢ。由实际函数等式得

`L₁v=x, L₂v=y, L₁L₂v=t_W`。

与纯四分量模型不同，目前不能直接假定L₁x=L₂y=0，因为Q可能携带额外boundary信息。连续性提供所需控制：所有β_(n,0)(δ_0⊗H)=δ_n⊗H的E₂范数均为1，因此U₁ⁿx在所有整数n上一致有界；同理U₂ⁿy一致有界。

在有限维W中，取U₁在特征值1的广义特征空间谱投影P₁，以及U₂对应P₂；可交换性保证P₁、P₂及全部Uᵢ相互可交换。P=P₁P₂满足Pt_W=t_W。置v₀=Pv、x₀=Px、y₀=Py。于是L₁v₀=x₀、L₂v₀=y₀、L₁L₂v₀=t_W，且L₁、L₂在P W上幂零。

一个unipotent有限维算子的幂作用在向量上有界，当且仅当该向量位于特征空间而非更高广义层：否则最高非零幂给随n增长的非零多项式项。因此U₁ⁿx₀有界迫使L₁x₀=0；U₂ⁿy₀有界迫使L₂y₀=0。即L₁²v₀=L₂²v₀=0。

四个向量t_W、x₀、y₀、v₀线性独立。若线性组合为0，先施L₁L₂得v₀系数0，再施L₁得y₀系数0，再施L₂得x₀系数0，最后t_W系数0。它们的张成空间对U₁、U₂及其逆保持不变，作用恰是V的四分量diamond。因此dimW≥4。

该命题被连续d:E₂→V达到，故界尖锐。不可省略连续性：证明明确用到横向边格点平移的一致E₂范数。也不可把开放条件扩为任意额外坐标后仍照搬本证明；若Q在trace-zero开放余项上另有非零数据，t_W与L₁L₂v的关系需重新核验。无论这些额外数据如何，上一节“最终invariant scalar迹不可能”的结论仍成立。

时间系数模型可先限制到一个固定时间秩一投影P（TrP=1）上的标量E₂副本，故同样的最小维数必要条件适用。这里只为continuous finite-dimensional读出给必要条件，不将其称为完整相对循环系数理论。

## 7. 标准Hochschild修复及剩余循环缺陷的精确层级

固定γ=(r,s)，按423记φ=τγ、σ=Ad Wγ、α=σ⁻¹，G为共链上同时施σ于全部输入。σ与α可交换，故G与bα可交换。置

`κ=(G−1)φ=Δφ`， `E=bαφ`。

423实际边界式给 `E=D+κ(α(B)A)` 及bαE=0。额外两项缺陷可以独立展开为

`E(σA,σB)−E(A,B)=(bακ)(A,B)`，

`E(A,B)+E(α(B),A)=κ(α(AB))`。

第一式说E的不变性缺陷是κ的Hochschild边界；第二式是标准α方向的循环缺陷。只做E=bαφ这一修复消除了Hochschild缺陷，尚未消除不变性和循环性。κ来自实际边与角，不能自由改为目标周期分布。

四分量还给异常的有限层级：Rγ=S(−r,−s)，于是

`κ(F)=r Tr_t e_p(Fγ)+s Tr_t e_q(Fγ)+rs Tr_t(Fγ)_c`，

`(G−1)κ(F)=2rs Tr_t(Fγ)_c`，

`(G−1)³φ=0`。

若rs≠0，只有“两个边”而漏角点的补偿会漏掉明确的二阶异常。若γ在单轴，二阶异常为0，但一阶边异常和普通迹障碍仍存在。有限层级意味着修正数据可以有限排列，不意味着已有合法循环配对。

## 8. 两种实际mapping cone，能修到何处

**相对Hochschild cone。** E在任一开放理想因子上为0，κ在I上为0，所以分别下降为边界共链bar E、bar κ。若q:A→A/I是商映射，则

`bαφ=q*bar E, bα bar E=0`。

因此(φ,bar E)是明确的相对Hochschild cone cocycle；取差分 `(bαφ−q*bar E,−bαbar E)` 即得0。这一构造确实把非循环有限部与边界异常放在同一复形，而非把有限部强行宣布循环。

**不变性cone。** 在Hochschild共链复形上令Δ=G−1。取degree n的对为(x,y)，其中x为n余链、y为n−1余链，定义

`d_cone(x,y)=(bαx, Δx−bαy)`。

因Δbα=bαΔ，d_cone²=0。上面的实际对(E,κ)满足

`d_cone(E,κ)=(0,0)`。

在完整A上它等于d_cone(φ,0)，是exact；在边界A/I上，φ本身不下降，但bar E、bar κ下降，仍给cone cocycle。这里没有证明边界cone类非零，也没有把exact的完整代数类当成新算术不变量。

这些cone可严格修复“相对Hochschild闭性”及“不变性up to Hochschild homotopy”。它们尚不能单凭公式变成标准扭曲循环复形，因为上一节的标准循环缺陷 `κ(αAB)` 仍须有对应的实际循环transgression。若采用带系数或paracyclic构造，应明确给cyclic operator、monodromy及相容微分；仅写“V-valued”或“cone”不能替代这些数据。本报告未声称已给这种完整循环修复。

## 9. 可用于下一有限问题的结论

已得到四项可直接核验的输入：

1. 四分量V是合法translation-equivariant、保普通迹的非半单读出；scalar invariant和coinvariant只能读角点。
2. boundary correction不能拆开trace线与boundary模的非分裂扩张；任何维数的最终invariant scalar有效迹方向仍不可能。
3. 压缩四分量且保trace方向必须单射；甚至实际E₂上的continuous finite-dimensional augmentation、若开放余项仅映trace轴，也至少4维，并包含同一个四维非分裂子模。
4. E修复只解决Hochschild闭性；κ和2rs corner明确记录剩余不变性／循环异常，可组织成上述两种cone，但完整cyclic、算术源链和周期比较仍开放。

所以不能把“finite-dimensional augmentation”一概否定；四分量本身就是合法反例。可严格否定的是把这样的augmentation再压为保普通迹的invariant scalar／coinvariant读出，或者在指定连续性和开放trace轴条件下声称少于4维足够。下一步若拟采用真正的系数循环或相对传递，必须保留这个非半单扩张，并证明实际链的循环条件、source变换、cutoff极限及周期比较，而不是先投到会杀trace的coinvariant。
