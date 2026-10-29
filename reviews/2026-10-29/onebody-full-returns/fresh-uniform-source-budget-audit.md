# C065 独立审查：whole fixed-I 全返回费用与强旧净后果

2026-10-29；独立审查者 `/root/onebody_uniform_fresh`。同 G20261027、运行 Goal1793085111、冻结基线0c4f。本文件只向 root 提交审查，不修改 STATE、cadence、Goal、文献、Git，不自行计602或formal21。

## 1. 结论与唯一可消费责任

**限定 PASS，未发现必须修复的数学缺口。** 16385-byte主证明和13097-byte交叉证明，在同一实际 Sonin 对象上，支付此前指定旧材料尚未支付的 whole fixed-I 原L²单位球绝对费用。应消费同一证明已经给出的较强系数方向：

    对每个固定有界区间 I，存在 C_I<∞，对所有 p≥pκ，
    ||𝒦_{p,I}−𝒦_{empty,I}||_{L²(I)→L²(I)} ≤ C_I(1+log p)/p。       (A)

pκ只由实位低cutoff压缩的固定谱隙和p≥2要求选定。证明(A)不要求log p>diam I。这里𝒦是560/532的完整source compact误差，保实际全Gram逆；不是整个正迹，也不是删掉proper powers的形式模型。

实际迹差在原Dlog/smooth域内始终为

    t_p(r)−t_empty(r)=−𝒫_p(r)+⟨r,(𝒦_{p,I}−𝒦_{empty,I})r⟩。          (B)

𝒫_p包含该p的全部proper powers及原权。当log p>diam I时，所有相关项才因支撑而exact为0，(A)才直接成为实际迹差的同界。对仍可见的p，不能从(A)删除(B)中的−𝒫_p。1964-byte root方向记录准确，应作为原16385/13097 late-D表述的最强消费补充，原字节无需回填。

因此完整onebody compact误差有

    𝒦_{≤1}(X,I)=𝒦_empty,I+Σ_{p≤X}(𝒦_{p,I}−𝒦_empty,I)，
    ||𝒦_{≤1}(X,I)|| ≤ C_I(1+log X)。                             (C)

只需单独吸收有限p<pκ的旧fixed-I费用，不必把所有p≤exp(diam I)都当未付head。相应完整connected≥2项满足𝒦_J=𝒦_{F_X,I}−𝒦_{≤1}(X,I)，所以这两个whole source算子的差也有(C)的费用。

这是统一所有固定I单位源、所有频高和在该I内随p或X变化的源的定量结论。旧533的每fixed smooth源p^-2及onebody绝对可和、J_r0和所有固定finite-E后果仍属old0。新(A)不是p可和界，也没有支付C_I随I增长、共同signed core/cross、通常Ξ或Goal完成门。若root核准本限定PASS，可作为C065一个完整数学责任统一结算；本审查、两原稿、方向补记和强旧恢复不各计轮。

## 2. 读取与对象审查范围

按恢复要求读AGENTS、goals/README与STATE，运行research_state.py check后show；恢复Goal、C065、D20261029AL及macro frontier。压缩后再次核当前STATE/check/show，确认当前唯一合同仍为C065 reviewing、尚未结算、cadence仍3/history65/latest601/formal20。README/frontier旧4340诊断的冻结由STATE及本目录scope-correction明确覆盖，不能恢复其“fixed smooth强化率未付”的旧归因。

两主稿均在收到terminal路径/字节/hash后读取。13097稿第一次组合输出被截断，随后单独完整读取，未把截断输出当全文。本次又完整读取1964方向记录、old533-root-status-pins及560全文。旧532/533/534/535、c007 trace-domain-proof、c006-uniform source-budget-audit/direct-budget-audit、c006-late direct-increment-audit均完整读取；reverse-audit仅读相关§5–7，不声称全稿重审。另读D20261028L，确认旧决策已经明确533与585的强旧对照。pins只核历史版本/status范围，不把其记录当独立数学认证。

物理空间为H_x=L²((0,∞),dx)，酉log映射为(Wf)(y)=e^(y/2)f(e^y)，source空间为原S_I=L²(I,du)。群积分A_r=∫r(a)U_a da，source系数经此运输仍是同一个r；没有再乘一次半密度。compact source属L¹，故A_r有界。原物理输入g与此r的识别没有改范数或把裸评价k_s当source。

为避免两个K混用，下文C₀=LFL表示物理低cutoff cosine压缩，C_p=LF_pL；𝒦_{p,I}只表示source compact误差。F为核2cos(2πxy)的实自伴酉变换，L=1_(0,1)、H_+=1−L。B_p=I−p^-1/2 U_logp，Π_p=B_pP G_p^-1P B_p*为实际正交投影，全G_p^-1不截断。F_p=B_p F B_p^-1也是实自伴酉；用B_p与B_p*交换及F把dilation反向即可验证，不能把B_p本身当酉。

560给原复Dlog的ordinary trace t_p=qΓ−𝒫_p+𝒦_p，Γ为actual2θ′/原contact，full Weil型另保双pole。535完整overlap E_p恰等于𝒦_p的二次型。实位基项、全部proper powers与共同pole的方向由这个身份固定，未借系数transport去构造新投影。

## 3. T自身S₁：全单位球费用的新关键步骤

令W=diam I>0。把source整体平移至[0,W]只使A_h=U_c A_r，故Z=A_r*A_r不变，原source L²范数也不变。这是证明T分解的合法source平移，不是让实际Π_p随source改变。

在log物理坐标中，L是负半线，H_+是正半线，E=1_[0,W]。A_h L输出限于(−∞,W]，A_h H_+输出限于[0,∞)，二者输出重叠只在[0,W]，因此exact地有

    T_r=L A_h* A_h H_+=(E A_h L)*(E A_h H_+)。

两因子分别HS。直接对其卷积核积分得到

    ||E A_h L||₂²=∫₀ᵂ a|h(a)|² da，
    ||E A_h H_+||₂²=∫₀ᵂ(W−a)|h(a)|² da。

所以||T_r||₁≤W||r||²；原稿使用的较松常数足够。这里没有source导数、零矩或平滑边界前件。hard endpoints也已在两个有限长度积分里支付。不是从“某个再乘F的M₀属S₁”倒推T属S₁。

χ_r(t)=∫r(u+t)overline{r(u)}du连续、支撑于[−W,W]，sup|χ_r|≤||r||²。返回物理坐标，T的核是χ_r(log(x/y))/√(xy)，其实际矩形为x∈[e^-W,1]、y∈[1,e^W]。这在固定W下有界连续，端点χ_r(±W)=0。T核不必对x/y可微；以下证明严格避免对χ_r求导。

## 4. 完整ordinary trace与L²延拓没有∞−∞

旧535/c007已经在实Cc∞源上证明各个实际overlap项分别S₁，且

    E_p[r]=2 Re Tr_L[h(C_p) T_r F_p L]， h(C)=C(I−C²)^−1。          (D)

这包括全部往返，并不需要源的pole矩为0。它不是有限angle近似强收敛后交换trace的未经证明公式。新分解使T_r本身在全L²_I上S₁，因此(D)右侧在固定I上有连续二次型意义；但不能据此声称每个L²_I源的qΓ和t_p分别有限。

合法运输顺序是：先在实Cc∞中使用已付ordinary trace身份，证明其差的uniform L²二次型界；560/532已给每个p的有界自伴source compact算子𝒦_{p,I}，故再利用Cc∞在L²_I中的稠密性延拓到整个source空间。Dlog上的实际身份由旧log Fourier core连续性匹配。延拓的是source compact差，不是在全L²中把两项可能无穷的ordinary trace相减。

“535 overlap = source𝒦”与560的(B)相结合，同时解释为什么(A)可覆盖visible p，而实际tdiff只在𝒫_p为0时继承同界。若另要为全L²定义有限trace差，必须明确使用这一bounded source-form延拓，不能把符号D_p混成无条件ordinary trace。

## 5. 全逆Taylor及所有高返回

旧实位C₀为紧算子且κ=||C₀||<1。严格小于1来自norm attainment与不存在同时时间/余弦频率紧支撑的非零向量。置q=p^-1/2、D=F_p−F、N=L D L，有||D||≤2q/(1−q)。取固定pκ，使||C_p||≤(1+κ)/2；所有resolvent统一有界，阈值未用W。

R_σ=(I−σC₀)^−1，σ=±1。h(C)=½[(I−C)^−1−(I+C)^−1]，其一阶项为

    Dh(C₀)[N]=½(R_+ N R_+ + R_- N R_-)。

由两次exact resolvent identity，h(C_p)=h(C₀)+Dh[N]+Q_p，||Q_p||≤Cκq²，而||Dh[N]||≤Cκq。原始resolvent始终保留；没有把Neumann头部当完整inverse。故

    (E_p−E_empty)/2
      =Re Tr(Dh[N] T_r F L)+Re Tr(h(C₀) T_r D L)
       +Oκ(||T_r||₁ q²)。                                         (E)

交叉项Dh[N]T_rD及Q_p T_rF_p都由S₁×bounded合法控制，给C_I q²||r||²。这里正是T自身S₁带来的全单位球余项费用，源导数并未藏进O常数。q²余项包含全部高返回，不是漏掉q级数中较高阶项。

## 6. 两个trace的单坐标C¹与正确IBP方向

R_σ=I+S_σ，其中S_σ=σC₀+C₀R_σC₀；这是exact identity。低cutoff cosine核光滑，第二项两边均有C₀，故S_σ在闭低方形上的两个坐标导数都由固定κ费用控制。

B_r=T_r F L的核为

    B_r(x,z)=∫₁^(e^W) T_r(x,y)2cos(2πyz)dy。

它对输入z有C¹界，sup(|B_r|+|∂_zB_r|)≤C_W||r||²；不要求对输出x求导。C_σ=R_σ B_r R_σ仍属S₁，展开(I+S_σ)B_r(I+S_σ)后，每个输入导数只落在B_r的输入或右S_σ上，故仍有同样的input-C¹界，输出只需有界/连续。

循环trace把第一项写为Tr_L(N C_σ)。对一个有限fast-scale核F_λ，核配对为

    Tr(L F_λ L C_σ)=∫₀¹∫₀¹2cos(2πλxy) C_σ(y,x) dxdy。

积分分部在x上进行；x是C_σ的输入坐标，恰是已经支付的导数方向。不能按未转置核误对粗糙输出求导。y≤1/λ的窄条直接估计，其余y用一次x分部得到1/(λy)；积分y于是给C_W||r||²(1+logλ)/λ。边界项也只需同一input-C¹上界。

第二项令V_r=h(C₀)T_r。h(C₀)=½(S_+−S_−)光滑，故V_r核对输出x有C¹界，输入y仍在[1,e^W]。Tr(V_rF_λL)中phase为λxy，这次在输出x上分部，费用1/(λy)，y≥1，所以为C_W||r||²/λ，无原点log。两个trace使用不同的已付坐标，未把它们混同。

## 7. F_p核级数、低scale与极限

若F_λ表示核2cos(2πλxy)，全物理空间||F_λ||=λ^-1/2。由实际B_p代数得exact的operator-norm收敛式

    D=−p^-1 F_1+(1−p^-1)Σ_{n≥1}F_(p^n)−p^-1 F_(1/p)。            (F)

高scale项没有另一个隐含q^n系数；其opnorm本身为q^n，故(F)绝对opnorm收敛。对已付S₁的C_σ、V_r作trace测试，有限部分和的trace连续趋于全D测试。每个有限核项先用有界矩形上的HS×HS配对得到上节核积分，未把无逐点收敛保证的无限振荡核直接塞进积分。

低scale F_1与F_(1/p)在实际有限矩形上核绝对值≤2；其前系数p^-1给C_W||r||²/p。若错用F_(1/p)全空间opnorm√p，会损失这个界，但不是原稿采用的局部估计。高scale统一和为

    Σ_{n≥1}(1+n log p)/p^n ≤ C(1+log p)/p。

与(E)及q²余项合并，即得对所有实smooth r的(A)二次型界。整个论证中W仅进入固定矩形/核导数常数，没有使用log p>W。这独立确认root 1964方向补记比原late-D消费更强，且无需变更证明。

## 8. 复源、极化及onebody总和

不能直接对一般复r假设Z_r与F_p交换。应先用实r证明上述公式，再用原实结构延拓。Π_p、A_a和所有实位/finite-prime源型是实算子；实源a,b的交叉ordinary trace实值，adjoint/cyclicity使两个交叉值相等，故t_p(a+ib)=t_p(a)+t_p(b)。qΓ和𝒫_p同样分解，已付source𝒦为实自伴。由此(A)二次型界对全部复r成立，费用乘||a||²+||b||²=||r||²。也可用旧real-even symbol密度；两种方式均保原complex源，并不额外限制零矩。

自伴source算子的全复二次型界给真正operator norm，因而同时控制任意两源的mixed配对及固定I内任何X/p适应源，无需另借finite-E常数。注意这只是该source compact差的norm控制，不能把它改名为新的算术mixed RR输入。

有限head p<pκ由旧每fixed-p有界source compact算子付清；Σ_{p≤X}(1+log p)/p=O(1+log X)，例如Chebyshev上界加partial summation已经足够。因此(C)在原范数上成立；无需对source频高截断，也无需将visible primes全部放入head。𝒫_p的全proper powers仍原样保留在(B)及560 joint比较中；没有被onebody误差求和消去。

## 9. 最强旧比较：哪些已付，哪些确实新增

533的真实对象、同一physical g=r、all compact smooth量词、全Gram逆返回与边界square均已付：每fixed smooth源D_p=p^-2A[r]+O_r(p^-5/2)，并有绝对onebody可和。其常数含source Sobolev费用。534只降级whole-L²的低cycle/trace/norm消费，不能回滚533的固定smooth完整结论。不同12150稿恢复的较弱q阶式也不能在这条旧结论之前领新功。

533极化固定finite smooth基底即给onebody Gram收敛；结合585/589已有j_X=t_X+O_r(1)、比值1，以及587的固定E共同lower、每fixed j正谱/秩后果。这些连同D20261028L已明确的533-versus585对照均属old0。原4340和后续审查对“同fixed r强化率未付/相关scalar净值新”的诊断必须保持冻结，本PASS不修复那种归因。

直接比较534及两份c006-uniform审查：旧材料已支付J_a的O(p^-2)等whole子项、M₀=LZH_+FL的S₁、Mδ的HS以及H3部分M_p的O(p^-3/2) S₁费用；它们明确保留完整angletrace/high-tail/aggregate缺口。M₀属S₁并不推出没有F的T=LZH_+属S₁；旧完整535身份仍在smooth源以导数费用闭合。未在这些最强旧exact分解中找到已闭合的全单位球C_I log p/p完整source误差界。

此次新增的短依赖链为：

    T自身的whole-L² HS*HS → source无导数S₁余项；
    535已付完整overlap身份 + C₀固定谱隙 → fullresolvent Taylor；
    两条不同坐标的C¹ trace估计 + F_p opnorm级数 → (A)；
    560已付source compact身份/稠密延拓 + prime求和 → (C)。

若只报告“fixed源更快/更好”会被533强旧完全覆盖；此次只对不同的whole source单位球责任给予新结论。不声称世界优先权，也不从某次rg未命中推出整个项目不存在旧证。审查针对root指定的532–535、560、两套原始审查及现有强旧精确分解进行了实际比较。

## 10. 不可升级的范围与结算意见

(A)是上界，不是actual误差下界；Σlog p/p的上界不可和不证明actual误差或其norm和发散。C_I可能随W很差，现有证明的大充分常数不是必要下界；既不能直接支付growing I_L/通常Ξ，也不能仅看X=e^(2L)就宣判全部visible primes被本结论排除。pκ独立I与C_I增长未付是两个不同事实。

(C)没有给𝒦_{F_X,I}的有利符号或危险core/cross控制，也没有删去onebody后就自动给𝒦_J正号。无新principal、sections或算术mixed机制；whole leading4/5仍是旧负惯性UPPER，并未改善为正性。旧安全高频receiver范围和fixed17/16正性也不因此扩大。Goal三数学门保持open，不能因whole标签或一个合同结算complete长期Goal。

建议root完整核本稿及1964方向记录后，以(A)/(C)为C065的最强有限新后果统一结算。实际数学计轮、STATE/cadence/看板、GitHub同步及达到4轮后的宏观21均由root按当前唯一状态办理。我没有执行这些变更，也没有进行新source、外部论文、PDF或数值实验。

## 11. 本次终稿输入原字节绑定

以下为本次完整读取并在写审查前重新核对的当前文件；SHA均对原始字节，不做换行归一化。旧材料详见读取范围，不把root pins当本人全文阅读证明。

| 文件（本目录，另注除外） | bytes | SHA256 |
|---|---:|---|
| cosine-return-large-delay.md | 16385 | 670c91b0d06bde3255ffb7aa43fa250f2f9c0f6ba728b8e7e78d9f9f8373f9b7 |
| uniform-traceclass-cross-check.md | 13097 | 709df9ed1bad8f08cb71b15d6c63d685ad78c17a9ae86e3bbc1a5815eddcbe7a |
| operator-first-variation.md（只作旧恢复） | 12150 | 1c1f5ed54b9030e866c886fae819091413e81090698f17ce9517ebd4c0f13599 |
| 533-fixed-source-scope-correction.md | 3417 | 9141d264aa9c24fa2829ea5997deeb99b775141496f518e2f4ebfe24167ee45e |
| whole-window-onebody-readmission.md | 3499 | b4f8a8f913c76e8d5ca3fe60d4382151d4068d0d4c5920afd81aaf4d9399c2ff |
| compact-error-versus-trace-direction.md | 1964 | 13d70ac72dc578d7987f68829e8a5d801e72a69c55a6a7654656e997189e174f |
| goals/contracts/C065-whole-window-onebody-return-budget.md | 1510 | 278597785ba4de1a6d1fdacb7134dd172f246a6797db0d50a5f133b3d0b6eea0 |
| notes/560-joint-finite-place-sonin-primepower-cancellation-and-compact-weil-bridge.md | 9263 | 9c2e6cd5a9eae269ad04b332699c21eec7403a230f9557afa8b895c45d4228d3 |

本文为终稿，等待root消费；本地通过审查不等于root已消费或已发布。
