# C056：Nyman短窗／完整范数与同χ候选对的独立数学审查

2026-10-29；限定 **PASS，无必须修项**。本审不同于原norm、strongest-old及affine作者；只核当前一个数学迭代，不代root最终消费／计轮，不改任何原稿或状态。

## 1. 冻结输入与审查范围

以下UTF-8规范LF版本已全文读并独立重算：

| 输入 | LF bytes | SHA256 |
|---|---:|---|
| C056-nyman-physical-head-and-affine-residual.md | 4040 | 7301bf48cae763e5111afb78ef390744ad326c74f815481a7738ba88efc878ec |
| 593-nyman-short-head-norm-loss-and-affine-residual-defect.md | 5331 | 93b3fd832798e71dee39438ed283708a1c55f5aeca406779c9a1376ad14242f6 |
| adjacent-source-exact-head-and-full.md | 8380 | e5fd028a679685b29cd567e66ec31900c01fe800163a9fc76715b9499806c43f |
| strongest-old-head-full-scope.md | 8264 | 1ff882489ec6eebd5c378fe1b0e9fb106da45c043a3f2e595c9ab46a10345e10 |
| affine-target-head-small-and-full-defect.md | 7310 | e03f1ba61286ec87bd1046752b80a185cd428daf809234e41a9b7660f7e98cd3 |
| root-integer-cell-and-adjacent-test.md | 5855 | 465986c951e4ad463877e988610f283d9907ece47da772ab5ddf2a0fa5474034 |
| root-affine-pair-draft.md | 3650 | 797bf4a9e9e071ed8f0e3c4f0e828d53d6632396a9310e053f6c411624b4cc13 |

头两件分别在goals/contracts/、notes/，其余在本目录。已恢复README/STATE、check→show、Goal、C056、D20261029L和formal18前沿，并核实际工作树。定点读082、087、088、096、097、099、104、111相关原件及525(6)经典输入；没有借其全部历史推论或093/094已冻结下游。一个只读子核独立确认triple-squarefree域／QT范围，不写文件，不构成另一个数学轮。

## 2. 实际Hilbert域、两项控制与三项主证书：PASS

H=L²((0,∞),dx)，rho_n(x)={1/(nx)}。A(b)=Σb_n/n=0时，y=1/x下U_b(y)=−Σb_n floor(y/n)，在integer cells常数；full能量是∫|U_b|²dy/y²。First-X cells到y=X+1，而旧local region可能只到X，两者不能偷换。

两项g_N=rho_N−(N−1)rho_(N−1)/N只有A=0，Σb=1/N。令n=N−1，P=Nn，首period在[jN,(j+1)n)、[(j+1)n,(j+1)N)取−j/N、(n−j)/N。独立积分得每block能量(n−j)/(N³(j+1))，故首period=(N H_n−n)/N³。Period内取值给|U|≤n/N，后尾≤n/N³；first-N cells精确1/[N(N+1)]。其full=(logN+O1)/N²成立，但不能把此两项源直接当087 tangent。

三项h_N=((N−1)/N)rho_(N−1)−2rho_N+((N+1)/N)rho_(N+1)同时满足A=Σb=0。统一消费N≥6、X=N+2。对k≤K=floor((N−2)/2)，有k(N+1)<(k+1)(N−1)，真实两pulse值为−(N−1)/N、+(N+1)/N，区间[k(N−1),kN)、[kN,k(N+1))；此前其余gap为0。

逐对能量为

    (N−1)/(kN³)+(N+1)/(kN³)=2/(kN²)。

因此至K(N+1)能量=2H_K/N²。全局正coeff和与负coeff绝对和均为2，fractional parts∈[0,1)，故|U_h|≤2，后尾≤4/[K(N+1)]≤16/N²。由K=N/2+O1，full=(2logN+O1)/N²。第二pulse从2(N−1)>N+3开始，first-X cells只含第一对，head精确2/N²。

所以全方向energy支配常数至少logN+O1；这只是必要loss lower，不是最佳常数upper。v_N=N h_N/sqrt(2logN)的full energy→1、head=1/logN→0。Support x≤1/(N−1)及有界fullnorm给对每个fixed f∈H的弱收敛0。这里的两scalar条件与原405全部Pan关系无等同断言。

## 3. 成长与087合法域：PASS，按准确量词消费

若Y_N≥N+3且log(Y_N/N)=o(logN)，令J=ceil(Y_N/(N+1))，则最终J≤K，head≤2H_J/N²=o(logN/N²)。这允许窗口依源／N适应，只要该成长上限实际成立。该结论只对h_N的norm比较；不把后面的affine R_X公式推广到任意大Y_N。Θ(N²)窗口对本witness可留住1−O(1/logN)能量，不给allcoeff统一domination。

Triple-squarefree域可由elementary计数付清。限N≡2(mod4)，排除oddp平方的三个坏类，AP中候选数K_T~T/4时bad≤3K_TΣ_(p odd)p^-2+O(√T)。而Σ_(p odd)p^-2≤π²/8−1，故合法数≥K_T(4−3π²/8)−O(√T)。本审消费**正下密度**至少1−3π²/32>0及cofinal，不额外要求自然密度极限存在；这已足够此处源域。

在这些N上，三点都在2≤n<X且µ(n)≠0，087 QT的非零行缩放／full-rank Vandermonde确能表示h_N；Σb=0使其属该affine条件的homogeneous tangent。它不支付fixedR、bounded jet coordinates或插值费用。原始h_N的Dirichlet coefficients有界，而unit归一化v_N的coefficients成长，二者量词已区分；不借091错误generalδ筛。

## 4. 同χ的actual affine残差：PASS

525(6)的旧经典Mertens界给M(t)/t²绝对可积。Partial summation给m1(X)=M(X)/X+∫₁^X M(t)/t²；σ>1的Euler inverse积分在σ↓1可由2|M(t)|/t²支配，ζ的pole使完整积分为0。因此m1(X)→0，且所给subexponential尾界成立。这不是RH临界Mertens估计或暂停路线的优化。

对a_n=µ(n)−X m1(X)1_(n=X)、R_X=χ+Σa_n rho_n，A(a)=0。Σ_(n≤X)µ(n)floor(m/n)=1（m≤X）使R_X在head中仅lastcell[X,X+1)为X m1(X)，故head=X/(X+1)|m1(X)|²。

v_N的head只在[N−1,N+1)，与R_X的[N+2,N+3)严格分开。因此F_N^±=R_X±v_N是同χ的两个明确finite residual，head精确相等且

    head(F_N^±)=X/(X+1)|m1(X)|²+1/logN→0。

完整basecross无需假小：parallelogram精确给平均full energy=||R_X||²+||v_N||²≥||v_N||²→1。所以liminf max(full±)≥1；有限sign集合还给至少一fixed sign的limsup energy≥1。它不保证预定sign的liminf≥1，也不保证两列都失败。Head共同趋0后，漏在x<1/(X+1)的tail有同样max liminf下界。

Base一般Σa=M(X)−X m1(X)不等−2，且a_X一般不为0／不受Möbius support约束；不把affine pair偷归087 prescribedmean或endpoint域。v_N只保持base既有mean。此pair不需exact sign判定或selector，未声称运行Gram数值、付出其费用或在bounded coefficient球内仍有unit defect。

## 5. 最强旧、target与最终消费方向：PASS

独立核082：PL是coefficient Euclidean norm相对full的log节点小谱，不是physicalhead/full必要loss。其PI确给<h_N,χ>=N^-1log(1−N^-2)，故generic坏方向几乎正交裸target，原稿没有据此判optimizer失败。

088的三block身份和actual easy-optimizer leakage需保同candidate的hard能量；096的η证书是conditional上界，§5明确finite diagnostics；097的exact integerwindow公式本身未输出此moving triple的调和渐近。099保全y≤X² spatial区。111保全部N² cell means，仅截后续variance corrections；把其polylog variance cutoff当成physical窗口会越域，本稿没有如此消费。104的fixed nodes／fixedR coercivity亦不覆盖这里moving full-rank域。

在所核最强旧范围中，新的实际内容是同域log必要loss、双约束合法unit defect及同χ affine候选对的head-small/full-non-small证书；不是首次发现targetalignment责任，不主张世界优先权，也不是新carrier／RH等价重命名。足以限定为一轮自含数学比较，而非来源0的重复组织；计轮仍只由root统一一次执行。

这个结果只否定短physicalhead的无费norm-only运输／对某列candidate的普遍验收。NB最优distance可能趋0、087 actual affineoptimizer、095/098 response/targetalignment、fullparabolic/allmeans及paidgrowth修复都未被排除；未给它们成功证书。Parallelogram处理本pair的joint basecross，不是所有optimizer的coupling定理。

原完整Γ/contact/properpowers/双pole、du/Dlog与sameprimitive/principal/sections/mixed、dangerous corecross/成长Ξ没有由此获得新正性输入。Whole4/5负惯性UPPER和关键瓶颈未改，本局部边界不满足原Goal完整方法类验收。C056一次结算后止，不续head-rate、degree、selector或来源队列。

本审仅写此文件，无web／新primary／PDF／下载／数值。观察单cadence仍2/history56/latest592/formal18，manifest仍132；旧093/094语义冻结保持。原稿中的pending/root未消费字样为其阶段记录，不由本审文件存在代替root消费。
