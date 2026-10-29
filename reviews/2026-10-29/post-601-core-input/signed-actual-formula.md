# 一份实际 connected-prime 公式：合法提取交互，但没有新增核心估计

2026-10-29；`/root/post601_signed_actual_formula` 独占原稿。这里实际设计并检查一个由真实 finite-Euler 投影组成的 Möbius 差分，不再调秩三 Green 连接或裸 pointwise gauge Gram。**该公式合法，确实隔离同对象的素数交互；本次没有得到此前未付的有利定量比较。** 建议按 exact 强旧／直接代数的0准入停止，不把“隔离了 compact defect”本身当失败，也不禁止有新估计的 connected-prime 路线。

## 1. 实际恢复与冻结问题

已读 AGENTS、README、实际 STATE，执行 `research_state.py check` 后 `show`，读完整 G20261027、停止的 C064、601结算、D20261029AJ、宏观前沿当前因果段及工作流。父线程已现场核同 runtime1793085111 active 与601最终219a7aa发布；本子任务没有独立认证父运行时／远端，不创建 Goal，不修改 STATE／cadence／库／Git。

当前强旧包括560同对象全 finite-Euler identity、570实际两素数 signed 误差、571完整双边界 receiver 组织；596前驱增量、591占据协方差及595同向量物理比较均不重做。本次定向读取560全文、570全文、535全文，571只核§§1–3的模型与真实Sonin区分及后文成长说明，596只读原对象／前驱／严格夹源迹相关段，591读定义和三测试结论。没有另做文献库存或来源章检索。

冻结三句：输入是由已知正交投影本身独立定义的 finite-prime Möbius 差分；首检是全 complex 源的夹源迹域、完整 Γ／primepower／pole 的系数和最强旧 signed 反测；成功必须给该实际交互项相对 t 或原 du／Dlog 的新有利估计，从而严格减少 unpaid core/coupling 的责任。仅给恒等式或写一个未知 domination 不算成功。

## 2. 唯一实际公式

保560物理 H=L²(R,dy)、U_a f(y)=f(y−a)、arch Sonin投影P和M=RanP。对每个先固定有限素数集B，

    B_B=∏_(p∈B)(I−p^(−1/2)U_logp)，
    G_B=(P B_B*B_B P)|M，
    Π_B=B_B P G_B^(−1)P B_B*，Π_empty=P。

G_B的全部逆／returns保留，B_B不是酉。给定非空有限素数集A，定义一个实际 ambient bounded 自伴算子

    C_A=Σ_(B⊆A)(−1)^(|A|−|B|) Π_B。                         (1)

特别

    C_{p,q}=Π_{p,q}−Π_p−Π_q+P。                              (2)

它不是以 K 的定义命名的 counterterm：四个投影都由原 B／P／G 的实物公式给出。也不是591的 source-occupation variance；这里差分的是**素数输入集合**，不对 receiver 乘子做 covariance。没有普通 determinant、det2、未知 ζ 零点、未标记 PSD 或附加 source counterterm。

实际物理源仍为 r，A_r=∫r(u)U_u du；定义

    c_A(r,s)=Tr(A_r C_A A_s*)，c_A(r)=c_A(r,r)。                (3)

源先在同一个固定 I=(−L,L) 的 zero-extension Dlog 内，第一槽linear。r=e^(u/2)f 是原物理源，不换回裸f；r/s 与Π_B所在的H向量不同，不从(1)的ambient operator norm制造原源费用。

## 3. Mixed ordinary trace 已合法，ambient compact 未声称

560逐 fixed B 支付 A_rΠ_B、A_sΠ_B∈S2，故

    A_rΠ_BA_s*=(A_rΠ_B)(A_sΠ_B)*∈S1，
    ||A_rΠ_BA_s*||S1≤sqrt(t_B(r)t_B(s))。

有限和使 (3) 是严格的 ordinary trace，而不是未夹源 Tr(Π M_f M_g*) 的循环缩写。全部 complex r/s 由同一HS乘积或极化处理，不只验证实源。这里可付的有限费用为

    ||A_r C_A A_s*||S1≤Σ_(B⊆A)sqrt(t_B(r)t_B(s))。             (4)

没有在 |A| 成长时把2^|A|个项吞成统一常数。把正负项各自分组，0≤Σ_±Π_B≤2^(|A|−1)I，故ambient norm≤2^(|A|−1)；此直接代数界不等于源→trace范数，也不证明 C_A 在 H 上紧／Schatten。下节紧性只在**固定物理源窗**成立。

## 4. 全系数检查：交互项精确落在旧紧余项中

写560同一I上的第一槽linear identity

    t_B(r,s)=qΓ(r,s)−Σ_(p∈B) P_p(r,s)+K_(B,I)(r,s)，          (5)
    P_p(r,s)=logp Σ_(m≥1)p^(−m/2)
                 [R_(r,s)(m logp)+R_(r,s)(−m logp)]。

其中R_(r,s)(a)=∫r(u+a)overline(s(u))du。qΓ使用 actual Γ=2θ′及完整FP/contact、原1/(2π)，proper powers无截断。对 |A|≥2，有限组合系数给

    Σ_(B⊆A)(−1)^(|A|−|B|)=0，
    Σ_(B⊆A,p∈B)(−1)^(|A|−|B|)=0（p∈A）。

所以准确得到

    c_A(r,s)=Σ_(B⊆A)(−1)^(|A|−|B|)K_(B,I)(r,s)。             (6)

等价地，其全线 multiplier 为 ε_A^conn=Σ_B(−1)^(|A|−|B|)ε_B∈C0；源压缩算子

    K_A^conn=Σ_B(−1)^(|A|−|B|)K_(B,I)

逐 fixed A／I 自伴紧。它是旧560的有限线性组合，没有新 uniform norm、符号或成长容量。

双pole没有藏进 t_B：原部分式 (5)本来未含pole。若给每个B统一加入完整 Lorentz pole型

    P∞(r,s)=2M_c(r)overline(M_c(s))−2M_s(r)overline(M_s(s))，

这里M_c(r)=∫r(u)cosh(u/2)du、M_s(r)=∫r(u)sinh(u/2)du。该pole型也因第一项组合系数为0而抵消。故不能把 c_A 独自改名 full Weil 型；但这**不否定其研究价值**——若能对 (1)独立给新的有利估计，仍可真实推进 K 的 coherent 责任。本次只是没有取得该估计。

## 5. 对实际候选的反向检查和最强旧

有限 Möbius 反演给精确 ambient identity

    Π_F=Σ_(A⊆F) C_A，C_empty=P，C_{p}=Π_p−P。                (7)

所有源夹迹因此同样反演。删除所有 |A|≥2 的交互后得到

    t_F(r,s)−Σ_(A⊆F,|A|≥2)c_A(r,s)
      =Σ_(p∈F)t_p(r,s)−(|F|−1)t_empty(r,s)
      =qΓ−P_F+K_≤1，
    K_≤1=Σ_(p∈F)K_p−(|F|−1)K_empty。                         (8)

右侧为 signed sum，不因每个 t_p≥0 自动为正。它保完整算术主项，但仍有实际 compact error K_≤1。把删除项重新加回只恢复旧 K_F；另减 K_≤1 则需要支付原未付比较，不能把“写得出来的全部旧误差”当新正性来源。另一方面，(8)并不证明所有更有结构的部分交互补偿或 joint signed 修复不可能。

最便宜的强旧反测取570原样数据：d=log(3/2)、固定双patch，源 g_η^± 各patch均双pole-zero，支持直径 W<log2，L1质量一致有界。旧570已付

    E_{23}(g_η^±)=±C23 log²(1/η)+O(log(1/η))，
    C23=1/(9 sqrt6 log2 log3)>0。                             (9)

不能只读 (9)就不核所减三项。在本源差支持 [−W,W]，fixed p=2、3 的single-prime裸核无 logp共振；535的实际核和完整returns分离已支付以下直接界：

    E_2(g_η^±)=O(1)，E_3(g_η^±)=O(1)，E_empty(g_η^±)=O(1)。   (10)

具体扣除：single-prime尺度 r=p^j（及一个fixed p^(−1)项）的非同尺度pair，在 0≤t≤W<logp 上有 |r−e^t s|≥c_(p,W)max(r,s)，535/570同一Si两端点界给绝对可和的 O(max(r,s)^(−2))。同尺度项给 C min(t,p^(−j))，求和为 O(t(1+log(1/t)))，在t=0附近仍有界。故裸源核在[−W,W]有界；完整return为ambient S1，源kernel Tr(Dret U_t)连续有界，其值≤||g_η||1²||Dret||1。empty case只有一个裸尺度，return亦为同一有界核情形。这里没有忽略returns、替换ambient裸核迹或假C0 multiplier本身有bounded inverse Fourier kernel。

由 (6)、(9)、(10)立即读回强旧已蕴含的

    c_{2,3}(g_η^±)=±C23 log²(1/η)+O(log(1/η))。               (11)

此为旧完整核的 direct consequence，不能再报一个新 signed 方法类定理或新增数学轮。它说明(2)不是自动非负／非正，也没有因source矩条件而消失；**不**排除把这个实际 signed interaction 与其它项共同组织后得到有利比较。

## 6. 原费用、成长和覆盖仍是什么

旧570已经给 ||g_η||du²=Cφ/η+O(1)，||g_η||Dlog²=(Cφ/η)log(1/η)+O(η^(−1))。因此 (11) 的原du单位源值仅为

    ±(C23/Cφ)ηlog²(1/η)+O(ηlog(1/η))→0，

Dlog单位值亦趋0。不能把L1质量有界但du范数成长的 log² 说成 norm1 发散或危险core lower；它与源compact一致。该旧双patch完整Q本身在η小时为正，537早已覆盖这个小窗，未给RH反例。

量词始终是先fixed finite A、I，再取所有原complex Dlog源；(11)只是先fixed A={2,3}后的旧η族。F_L增长时，所有压缩逆和子集费用、同源误差、higher interactions及其相互抵消仍须独立控制。没有证明cofinal cluster可和、pairwise dominance、uniform-|A|界、原du全源coupling、普通Ξ或全405 noncompact Pan识别。不能以compact源cropping冒称验证405全实际关系。

571的模型δ／真实receiver／Sonin误差有不同角色；它的signed完成平方和有利高层均值不是本 C_A 的未付全源费。596对 J_p h 的 ΔK_p 也不是本 (2) 的同源四角cofinal控制，本稿未移植该速率或再累加。595同物理向量的强旧 Llow／fullQpoint／gap 已由 STATE 的原链支付，没有重算或领取其弱子界。Whole542+555→557仍为leading4/5负惯性UPPER。

## 7. 裁决和精确停止

这次交付的是一份具体、独立指定、可合法夹迹的 connected-prime 算子及实际首检。它不因“只提取compactdefect”而失去资格；若对它出现新的同对象有利量化估计，root可以据真实input/test/net重新准入。但本次仅得到 (4)、(6)、(7)这些旧560直接恒等式，以及旧535/570已经蕴含的 (11)，没有独立新bound/符号/coverage。

故**当前不形成新核心输入，建议0准入止**，无C065/602，不以pairwise表示、kernel短证、有限Möbius反演、代理或文件另计轮。此理由是扣最强旧后净增为空，不是“没证明RH”或“公式不是fullWeil所以一概无用”。关键principal/mixed/危险corecross/成长Ξ与whole4/5UPPER不变，长期Goal三门open。

停止这次automatic subtraction／旧核反测，不继续pair样本、第三prime、interaction阶数、cofinal cluster或未知domination续批。保有新独立估计的真正connected机制、额外actualdata／不同source-domain／独立D′未排且无自动预算。下一仅root完整消费当前匹配原稿，再比较是否另有 actual input；本子任务不选择新paper／章节继任。

## 8. 执行与版本边界

没有web、新paper／PDF页、数值、证书重放或新source。一次 Windows wildcard路径检索失败后改用 `--glob '5*.md'`，失败不作无旧资产的证据。只读子任务 `/root/post601_signed_actual_formula/mobius_projection_algebra_check` 已terminal、无文件，独立核 finite Möbius coefficients／mixed S1／反演与role，并核535/570实际核支持(10)，不能从C0本身推boundedkernel。本稿不修改共同状态。后附指纹只认证实际版本；不把hash表冒称重审全部nested旧proof。

| 实际输入 | 实读／使用范围 | bytes | raw SHA256 |
|---|---|---:|---|
| `goals/GOAL.20261027.md` | 全文，完成门与原source/norm/当前运行约束 | 9679 | `b3d2acb1f962d793f45d79b6a4e67fb87dd072cd4752108a9298204b4cefa1de` |
| `goals/contracts/C064-haran-integer-affine-fold.md` | 全文，已停止预算，不复活 | 2047 | `765aa6546b77297a475a0003ce6c4a362736915ae36eb014874d3f3d21971399` |
| `goals/reviews/2026-10-29-haran-affine-601-settlement.md` | 全文，当前实际停止与新input-test-net | 2744 | `664b7acc27bd7a2599a440b9472c20054ad9996357abcb10da9b46c37f84d71e` |
| `notes/560-joint-finite-place-sonin-primepower-cancellation-and-compact-weil-bridge.md` | 全文；同对象/全逆/全complex夹源域/finite-F量词 | 9263 | `9c2e6cd5a9eae269ad04b332699c21eec7403a230f9557afa8b895c45d4228d3` |
| `notes/535-actual-first-prime-sonin-log-resonance-and-indefinite-error.md` | 全文；singleprime真实核/returns/phasegap及历史范围 | 9910 | `e83c3e080d19c2534425fb3c0e469367012f6c566a470b3baba703fb6def146f` |
| `notes/570-actual-joint-sonin-signed-mixed-and-narrow-source-cost.md` | 全文；actual双prime核/oldg±/原norm/完整Q | 12411 | `6c787848770f78a9f535e381ba512352d46e84eb365f49b29d10097c00ff3315` |
| `notes/571-actual-receiver-two-boundary-signed-comparison-and-growth.md` | §§1-3精读模型与receiver；其它返回文本只用于原norm/cofinal范围说明，不消费其新证明 | 12528 | `c7f0cf4712bdbb9429c4356c3974098b9c39b2eba4486b91c800fb7653cf109e` |
| `notes/591-connected-occupation-covariance-three-fixed-test-barrier.md` | 定义/三测试/actualtail段；不重审nested | 5974 | `5a6d6e221369a1a9bce668d56c9fe574aeca0a295fdb7d0ccd31e4fcd03eaa7c` |
| `notes/596-critical-prime-sonin-covariance-and-signed-increment.md` | 原对象/量词/前驱/严格夹源trace与stop段；不重审全部nested | 9094 | `b609b8e5a820ca259c1a02fce134ca5b788d4c3373b933b6e1d2c3094cc4a782` |
