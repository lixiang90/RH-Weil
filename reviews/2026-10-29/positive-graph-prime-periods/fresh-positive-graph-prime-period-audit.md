# C055：正周期图跨素数通信的独立数学审查

2026-10-29；不同组织的全链数学fresh。**PASS，无必须修项。** 只写本审查，不改STATE、cadence、Goal或Git，不新增来源、辅助任务或数值实验。两原件及root准入／范围草稿均已全文核；下述PASS不代root消费、计轮或发布。

## 1. 三闭词与exact SCC主链成立

在可数有向multigraph中，严格正且有限的edge length/activity、有限word的加法／乘法和primitive cyclic words给出所写正和。每个非空closed edge-word都有primitive cyclic root；其真实贡献是lγ a(W)，不是l(W)a(W)。ν_G在(0,∞)的Radon性是明确前提，不由图可数性或边正性自动推出；本证明的所有下界只取正子和。

对c≥0、a=logp、b=logq、p≠q，若c+a、c+2a、c+a+b全在S，则N、pN、qN全为>1整数素数幂。前两者迫N为p的正幂，第三者矛盾。M=ceil(e^C p max(p,q))、δ=1/(16M)的统一裕量也正确：假三点均距S≤δ，选近邻素数幂N_i后，两整数差N2−pN1、N3−qN1绝对值均≤4Mδ=1/4，故exact0，仍矛盾。不同prime幂倍率p^m、q^n同理。

STA、STAA、SBTA确为同一图内的closed words，活动分别zx、zx²、zxy，无负项可相消。故supportν_G⊂S迫每个cyclic SCC只有一个prime基底；不迫全图无one-way连接，不迫component一维或单cycle。若ν_G=νζ，logp处正atom必有primitive贡献，其长度m logr及repeat k满足p=r^(mk)，迫r=p、m=k=1。各prime的base周期因而存在并落在不同SCC；没有错误升级成唯一orbit或所有全局解析耦合均不存在。

## 2. 高repeat、固定测试与通信sup均闭合

主稿§4正确修复了高重复可能使单个系数很小的问题。设W=γ^k，t=kℓ、w=u^k，d=log2/8。若ℓ≥d/4，原repeat项给≥(d/4)min(1,w)。若ℓ<d/4，落在I=[d,2d]的整数repeat数至少d/(2ℓ)；因t≥log2=8d，所用j<k，所以u^j≥min(1,u^k)。这条阶梯给≥(d/2)min(1,w)，不依赖最小edge长度、word edge数或graph维数。

I与F={t∈[a,L]:dist(t,S)≥δ}均为远离S的compact，存在同一个0≤h_C≤1、在I∪F为1且支撑不交S的光滑compact test。h_C只依固定p/q/C。若marked x,y≥η0∈(0,1]，三个活动均≥zη0²，于是

    ν_G(h_C)≥(log2/32)η0² min(1,z)。

同一个h_C适用于所有本层返回路径，故可取sup而无需达到最大值，也允许sup=∞。所得Z_(G,C)是最佳单条roundtrip activity product的sup，**不是sum、capacity或operator norm**。ν_j(h_C)→νζ(h_C)=0直接迫每firstfixed C的Z_j,C→0。此量词覆盖随层改变和非局部自适应选择的路径，却没有偷补cofinal marked activity下界。

近似长度a_j→logp、b_j→logq的同稿扩展亦成立：三实际length的误差至多δ/2，仍有距S>δ/2的一点；固定区间[log2/2,L+1]仍在2d以上，primitive阶梯常数不变。这里使用固定test的有限裕量，不是moving-source反证。

## 3. 全部fixed复平方到off0正measure的桥成立

本接口正确先假设共同W_j∈D′(R)存在及其off-origin限制为同WΓ+H减ν_j与反射。ν_j仅Radon(0,∞)本身不保证在0可延拓，主稿没有补这个结论。Q_j不必PSD；sesquilinear polarization仍由四个复平方恢复每个fixed r*s#的收敛。

对K=[u,v]⊂(0,∞)，主稿B=v/4、A=(u+v)/2的两个bump确有不交支撑。其cross-convolution非负，support在[u/2,v+u/2]，且K位于严格正的内部，故存在c_K>0。它在0的邻域恒零，所以任意origin-supported接触修复（包括阶数或系数随j改变者）全部exact0，反射measure亦不贡献。由off0身份与极化得到ν_j(h0)收敛，从而sup_jν_j(K)<∞。

再对任意positive compact support的h用h*k_ε，fixed ε时它就是一对原compact源的卷积；支撑保持away0，接触项仍为0。上述uniform正质量界支付ε→0的一致逼近，给ν_j→νζ于D′((0,∞))及vague。没有借未知factorization定理、near0质量界或du→graph范数。完整Γ/contact、proper powers和indefinite双pole的目标身份依旧由全源收敛前提承担；此桥不能把正prime measure升级成Weil正型、Hodge配对或ordinary trace。

## 4. 两个实际逃逸及commensurable控制已核

**Long-star。** prime≤N各自selfloop加长度N/activity1的双向star确为有限强连通图。任何含star edge的closed primitive或其repeat都至少长2N；固定时间窗最终只见原prime loops/repeats，且所需prime最终全部列入。因此该窗最终exactνζ。同Γ/H的完整signed W_N于是也在每fixed compact源上最终相等，但没有PSD结论。

**Diffuse-star。** 令Q_M=11^T/M、P=e0e0^T。Q_M²=Q_M、P²=P、Tr(Q_MP)=1/M，rank-two计算给

    det(I−uQ_M−vP)=(1−u)(1−v)−uv/M。

更直接，任何含Q/P两种字母的cyclic trace在压缩连续相同字母后化为Tr((QP)^r)=M^(−r)，r≥1；pure traces为1。固定时间窗只涉及有限总edge次数，故全部mixed周期系数O_T(1/M)。这可以在有限图的formal trace-log/primitive word计数中逐系数证明，不用越过收敛域的解析延拓。M=N再附long-star补齐其余primes，便得fullν_N→νζ。所有周期有统一positive下界，完整signed W_N∈D′的构造及fixed平方收敛也合法。

该图在vertex0的p/q loops可取空返回、z=1；但每条长度logq的individual q-loop activity是α_q/M→0，因而不满足marked lower。它确实证明diffuse修复非空，不能把主定理扩大为所有强连通cofinal图均失败，也不能消费成对整个q-sector的rankfree通信norm下界。

**单q控制。** 2×2 rank-one J、B=q^(-1/2)J满足TrB^k=q^(-k/2)。primitive m-edge orbit在k-edge based trace中贡献m个cyclic起点，乘统一delay logq后恰得到原measure的primitive coefficient。因此主稿的单q正mixing对照正确；它不冒称非平凡曲线完整ζ或F5全Hodge实现，也不错误排有限域同一logq时钟。

## 5. 强旧净值、完成门与当前计轮

本审独立核078全文及079 OR/OS/OT、565有限双向Markov、566正jump/heat域、404 actual周期、560/577完整目标的相关原段。078是同一q时钟的有限Ihara/companion机制；079须prime-block及normal/Schatten determinant前件；565须有限维双向保正；566是closed-form/heat边界；404的flow周期不自带edge-word拼接。它们不直接给当前可数正周期图的SCC分类或共同h_C通信下界。这里的净值判断限项目内所比较的已付资产，不宣称世界优先权或逐篇重证全部历史。

本结果改变局部positivegraph如何承担跨prime耦合的选择，没有移除独立算术primitive/Pan下降、principal/sections/mixed、危险signed core/cross或Ξ瓶颈。Whole542+555→557 leading4/5仍仅负惯性UPPER。Long/diffuse已经有实际fullsigned逼近；signed/off0修补、非edge-additive／无限记忆roof、一般flow/higher/Hodge及非normal重整仍有准确未排范围。任意origin-only接触在主稿§6的类型内已经覆盖，不能再列为那一类型的逃逸。

故不能以已证uniform coupled/marked-visible子类缩小Goal第3门；三项长期数学完成门仍未通过。可将本轮交root统一消费，**本fresh不预先结算592，不重置formal18，不发布或完成Goal**。现场唯一cadence仍1/history55/latest591/formal18，LF SHA为`7ac71ae721e352746db7b172281c1001370cd51063709b68965e3dab5d6840c1`；这是本次观察，不冻结未来合法结算。未独立调用运行Goal工具；STATE的运行观察没有被本审当作实时Goal验证。

## 6. 审查版本与读取范围

两主原件、root准入、root范围草稿、C055合同全文已读；恢复AGENTS、README/STATE、check后show、Goal完成门及当前D20261029G/macro相关责任。旧078全文；079 OR/OS/OT、565 §5、566 §§2/7、404 §1及已定位角色、560 §1、577 §1按必要范围读取；未核它们所引外部论文全文，无web/新primary/PDF/下载/数值。结构check及hash均不认证数学或授权。

规范LF绑定如下；无须把本审不存在的helper或父代理历史读取当本审证据。

| 文件 | LF bytes | SHA256 |
|---|---:|---|
| three-word-and-cofinal-proof.md | 15836 | 47b7c0105f80577561a356731d401d3a00d9b0d782a4d321342666d5c8fcdf0a |
| strongest-old-and-role-audit.md | 15038 | 59d6f0f84ab996e828b5f76f2305d3f31893316d257ff49bbbe2d2bdb6b3042a |
| root-three-word-admission.md | 4917 | 96e6658ddd96d8ca918ab0ef35e528ff0f0127a2537b550f6bafe59f395c4a9f |
| root-consumption-and-goal-scope-draft.md | 4396 | 3ab5608094107e8d000219976412982a213492fed22070a76984cdc24e84be22 |
| goals/contracts/C055-positive-graph-prime-period-communication.md | 5156 | 39eab2f7fb984e2d6acd92db1c3d11fbbc7935358a51eb1857f99f27f993214d |
| goals/GOAL.20261027.md | 9679 | b3d2acb1f962d793f45d79b6a4e67fb87dd072cd4752108a9298204b4cefa1de |
| notes/078-ihara-ramanujan-hodge-structure.md | 7932 | c38f97f987b8a326b508359bba708463798b144afc8ddd6f24a8695ad3ce61bb |
| notes/079-prime-orbit-schatten-normal-limit-no-go.md | 9005 | 74dab279e8ef02306dea15249342a5ff1d9198ddf5db94e92496095bc3834edb |
| notes/565-canonical-completion-graded-identifiability-and-independent-energy.md | 12584 | 3ac5d8f6dbbd3dcfda10e74cd911c803bacfbfa8ac6aaa535b3559e7c374ea89 |
| notes/566-source-closed-forms-and-full-weil-heat-trace-tests.md | 10582 | 004f5438c918373e0ead73c0011ffb3883ef872c4977e356911dd910da177053 |
| notes/404-f1-adelic-periodic-orbits-and-mixed-local-trace.md | 14797 | 43f2c14e97a7fd0b0aa83958d30fccd03ec5f725444139e03c04d9acbf49fb37 |
| notes/560-joint-finite-place-sonin-primepower-cancellation-and-compact-weil-bridge.md | 9263 | 9c2e6cd5a9eae269ad04b332699c21eec7403a230f9557afa8b895c45d4228d3 |
| notes/577-full-gamma-positive-repairs-and-independent-budget-gap.md | 13925 | cf80354ab3bb3c7ca2a2bae7e2aa4083adc47d01da5c984146fb285d7551f55f |
| literature/supplements/2026-10-29-positive-graph-prime-period-scope.md | 1189 | 2878982f15c2ccc9f5bf3ad68cb5480bffd7b082842256cf74747e9c37ae7668 |

前四项短文件名相对本审目录；其余相对仓根。最终root收据和结算可以引用这些冻结版本，本审不替其未来执行作预确认。
