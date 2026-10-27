# 固定ell11门：独立域／分支／关系逆审

2026-10-27；`/root/ell11_fresh`独占审稿。已恢复AGENTS、README／STATE、check→show、G20261027、D20261027I及当前唯一门，随后核到新C047一轮合同。本文不改STATE/cadence，不自行计轮或发布。初稿时producer说明／Pan稿与root584尚待出现，不能以本独立推导代替它们的最终版本消费。

## 1. 当前对象及强旧

固定q=e^(2πiτ)、j=q^-1+744+…、g11=η(τ)²η(11τ)²，selected∞读出K(u)=CT(e^(u j)g11)、ell(r)=∫rK。source是ALLcomplex S_exp，原physical r=e^(u/2)f；fixedcompact du／zero-extensionDlog与全线强费用分开。该C值rank1泛函不是actual Maass input、原Weilρ运输、relativePic、primitive class或完整Hermitian Weil型。

583已给全source raw Faber/current像，不能由其注入性推一个selected scalar必不消Pan；553原du/Hlog连续稠密不能直接套指数增长的K。旧a0核的q系数非负也不能运给带符号g11。新关系若闭合，只否定当前fixedsinglecusp recipe，不否定全部harmonic/relative或算术来源；strongold542+555→557 whole leading4/5负惯性UPPER及classic core/coupling未变。

## 2. source代码实际独立重放

已全文读`ell11_source_controls.py`，独立in-memory调用build_record，所存source-controls.json所有字段exact match。另手工重构前三个非零jet：g的c1=1,c2=−2,c3=−1给

\[
 K(0)=0,\quad K'(0)=1,\quad K''(0)=1486,\quad
 K'''(0)=2246795.
\]

q_times_j的有限乘积截断足以给每阶CT j^n g；没有以sample拟合代替exact系数。程序对左商Γ0(11)\SL2(Z)的12个代表与S/T及inverse给48个Schreier过渡；bottomrow projective mod11确实判Γ0左乘轨道，随后SL2在此商集合上右乘，word=rep_i·generator·rep_j^-1在Γ0(11)。矩阵±正规化不改变weight2变换。

fresh独立打开官方[DLMF23.18.5–7](https://dlmf.nist.gov/23.18)正文，核principal sqrt(−i(cτ+d))、epsilon和c>0的Dedekind sum。两份平方η相乘，phase恰是

\[
 (a+d)/c-s(d,c)-s(d,c/11)-1/2\pmod{\mathbb Z};
\]

T腿phase=b。全部48个有理phase均为整数，足以从Schreier生成性得到fullΓ0(11)的trivial character。DLMF已纠正sum只需r=1,…,c−1，无coprime限制；代码确实求全部r。这里只核三式／域／erratum，未审整章或另下TeX。

infinity与0 cusp阶均1；Fricke的规范slash为g|2W11=−g，直接由η(−1/τ)变换得到。η在H无零，故g有限点不为零。它是scalar S2(Γ0(11))数据，不自动是原II2,2／trivialρ的S2输入。

source费用也独立核过：σ3(n)≤n⁴，−log(1−R^n)≤R^n/(1−R^n)，再用exp x≤1/(1−x)给程序的有理j_R/g_R上界。s=1/1024、R=1/512、s<R支付series换序；direct contour也给强指数矩费。p_A=∫|r|e^(A|u|)有限可由任意N>A的S_exp半范数付，不领取全线uniform du。fixed源窗的sqrt(2L)exp(AL)du费合法，Dlog仅使用原du嵌入。

## 3. 537控制角色的必要纠正

537是fixed17/16窗ALLcomplex正性定理，未固定唯一数值波形；583 relation(15)是small-evenφ族。不能把某个新选φ叫作“已评唯一旧sample”。当前共同族

\[
 r_\phi=(D^2-1/4)(u\phi),\quad
 \phi\ge0\text{非零偶},\quad\operatorname{supp}\phi\subset(-2^{-20},2^{-20})
\]

是旧583同一族中的共同选择。设W=K''−K/4，独立jet给W'(0)=8987179/4>0。代码用mean value及真实contour四阶上界核

\[
 |W'(u)-W'(0)|\le g_R\varepsilon
  (j_R^4+j_R^2/4)/(1-j_R\varepsilon),\quad |u|\le\varepsilon.
\]

其数值摘要约17741，对W'(0)约2246795有余量；同一ε的旧a0核variation约9.048e6小于旧V'(0)约1.3552e9。全部接受是有理比较，不是这些打印小数。因此同一个r_phi有ell(r_phi)>0、旧a0(r_phi)>0、双polezero且由537为真非根。573另一个固定evenχ源没有被本证书评价。

## 4. 独立重构的Borel／cut分支链

以下是fresh对root提出候选链的独立重构，最终仍须对齐producer实际稿及版本。

令a=1728、h(z)=g11(q(z))/(q j_q(q(z)))，选∞width1 sheet。h作为X0(11)上的weight0函数meromorphic；j-cover的有限branch值只有0、a，原∞branch的h(z)=−z^-2+O(z^-3)。注意D=C\[0,a]并非simply connected，而是π1=Z；围全cut的monodromy等于围∞，width1使该选sheet固定，故h确实单值holomorphic于D。不能用错误的simple-connectivity论证跳过这一步。

Γ0(11)无order2/3椭圆点。j=0的ramification3使h=O(z^-2/3)，j=a的ramification2使h=O((z−a)^-1/2)，都局部L1。g finite nonzero，不会产生更坏极点；cut内部无其他branch/pole。real q系数和real∞branch给Schwarz对称。于是

\[
 \rho(t)=(h(t+i0)-h(t-i0))/(2\pi i)\in L^1(0,a;\mathbb R),
 \qquad h(z)=-\int_0^a\frac{\rho(t)}{z-t}dt.
\]

正负号可由Cauchy contour沿cut的方向重构，亦由h~−z^-2及K'(0)=1检验。端点小圈费用为O(ε^(1−2/3))／O(ε^(1−1/2))而趋0，无隐含pointmass。∫ρ=0不表示ρ=0；该density必有符号，不是ζ谱的正测度。

在z>a选τ=iy、y>1，g(iy)>0且qj_q<0。y→1+时j−a=C(y−1)²+…，C>0，所以

\[
 h(z)=-A(z-a)^{-1/2}+O(1),\quad A>0,
 \qquad \rho(a-x)=A/(\pi\sqrt x)+O(1).
\]

该endpoint sign与旧a0 positivity无关；取上侧sqrt(−x+i0)=i√x，得到h+≈+iA/√x，jump方向正确。

将原q圈变形为∞支的large-j圈（orientation反转），给

\[
 K(u)=-\frac1{2\pi i}\oint e^{uz}h(z)dz
      =\int_0^a\rho(t)e^{ut}dt .
\]

这对所有complex u成立，且K^(k)的费用由a^k||ρ||1 exp(a(Reu)_+)付。Cauchy强费此前已有明确有理上界，故此表示不依赖一个未证数值||ρ||1来合法化源积分。

## 5. 真Pan／必要费用及两腿商角色

已回读405的真实η(r)=πr²(πr²−3/2)e^-πr²、h=Eη，以及579/583的physical H=e^(u/2)h>0、H∈S_exp、p=(D²−1/4)H≠0的Pan身份。全部固定平移p_b均在同一强域；没有裁noncompact尾或只用两个pole矩冒充全关系。

强衰减与ρ∈L1许可Fubini及分部积分：

\[
 \ell(p_b)=\int_0^a\rho(t)(t^2-1/4)L_H(t)e^{bt}dt,
 \quad L_H(t)=\int H(v)e^{tv}dv>0\quad(t\in\mathbb R).
\]

right endpoint因此给Watson渐近

\[
 \ell(p_b)\sim \frac{A}{\sqrt\pi}(a^2-1/4)L_H(a)
                e^{ab}/\sqrt b>0\quad(b\to+\infty).
\]

这正是否定全部Pan下降的一个实际关系轨道；不是对每个b都为正的声称。du与原Dlog图范数平移不变，所以该实物增长给全线uniform原norm费用不可能的必要结论，不是反用Cauchy upper。strong S_exp费用仍合法。新全源Borel/Pan/费用信息不能由583 raw注入或553原Hilbert连续直接推出，应按C047实际一数学轮消费，不以source0隐藏。

若fullboundary读出确为B(r)=(ell(r),−ell(r))，则任一真实Pan的非零像已张成整个source range那条C线。任何杀Pan的固定complexlinear两腿readout／线性商必杀所有source及上述r_phi。更强且无需新前件：所有complex倍数仍是真Pan，所以B(Pan)=B(S_exp)=C·(1,−1)。任何只依同B数据的source-independent postmap若把全部Pan像送同一base，即使非线性也在全部source像上常值；不能仅在同B后换非线性当逃逸。未判的是带额外实际数据或不同source-map的非线性／source-adapted修复。

这些只限制当前局部residue-map，不能升级为全部Maass、relativePic或算术Chow失败。fullresidue theorem对两cusp的essential源仍合法：去掉固定小disc后是compact Stokes，原finiteprincipal H_k域不被借用。两腿constant不应混成fullΓ/contact或经典两pole。

## 6. 实际producer限定审查

已全文核source/typed稿与`pan-relation-test.md`稳定稿。source已将陪集术语写成无歧义作用描述：Γ0以左乘作用的轨道、随后SL2右乘。fresh最初口头要求“右陪集应改左陪集”不严谨，常用Hg称右陪集时原称法并无数学错误；最终只澄清作用方向。代码与Schreier方向本来正确，不影响数值。48phase、两cusp规范、Cauchy/原norm费用、共同ε与537控制角色均通过，改稿仅更新文字版本。

Pan实际稿的(1)–(14)与上述独立重构一致。h=Eη、physical H及M_H(t)=ξ_Riemann(t+1/2)/2的规范已回到405原定义核对；正号来自H>0而非RH。q_i处j_qq>0由S固定点和正q系数支付，不误混q／τ二阶导数。式(13)的显式threshold条件也正确：b≥1/δ使√b exp(−δb)递减，故任何满足条件的整数b0之后，整个actualPan轨道都给正值。稿件没有假装实际算出b0数值；它给出的严格全b公式/充分大正b反例已足以否定当前下降责任。

两cusp essential residue与固定complexlinear quotient推论范围准确，只限同一boundary map，不冒领Maass/arithPic。符号、域、极限次序及强旧扣除未发现数学缺口。新全源signed-cut/Pan/必要费用是本轮C047数学实物，不能由旧scalar positivity或raw注入推出，宜按一数学轮而非source0消费；标准typed/Cauchy/finite-rank及linear corollary不另加轮。

目前核到的producer稳定规范LF版本如下；hash仅绑定版本，不替上述证明：

| 文件 | SHA256 |
|---|---|
| scripts/ell11_source_controls.py | 1e628c47378e2c789c45d2ca34684da13b2d7cae4604f0b33e744be3060b0f24 |
| source-controls.json | 8d8495f4aad1b5f6be4a02b27b958a82391e7cf96291b1479306d74679406cf1 |
| source-kernel-and-typed-controls.md | 2f539af310fdef071a019c6942d9e7cc5b44fd09496eb643af07143be650ff0d |
| pan-relation-test.md | 6a68cf1bfd7861cabb80dd0bdd41e09756293e9071ef870a2ff1715463874367 |

root584／前件收据尚待出现，以上producer限定PASS不代root最终消费或长期Goal验收。最终精确版本另补，未把未出现的稿件当作已审。

## 7. compact-real旧直接推论须现在扣除

已定点回读519§1/§4与553§2–4。519给原S_exp全jets／Pan理想及双degree背景；553的全线du/Hlog bounded读出稠密不能直接作用于非零real指数核。更直接的compact-real support诊断已经是405实际正H与标准compact Laplace唯一性的立即推论：固定compact-real有限complex measure μ定义ell_mu，全部p_b消去迫(t²−1/4)M_H(t)μ=0；M_H(t)>0于real，故μ仅能支持±1/2，对doublepolezero源读0。当前ν∈L1且非零，不能符合该责任。

这项旧合成应在本轮strong-old消费中扣除，不把已能立即证明的lemma伪留作“下一未执行研究”，不另计轮或建general数学合同。C047新本体仍是实际K属于该类的全局Borel/L1身份、endpoint符号与1728真实Pan必要增长；一般support lemma和两腿线性代数不再计新轮。compact-real、fixed source-independent finite measure及原强域必须保留，不能改称所有curve/harmonic/lift边界。

## 8. 唯一后续family transport比较的准入范围

root另提出一个不换level参数序列／paper的实际类比较：任意实际finite-index modular cover j:X_Gamma→P1、holomorphic ω∈H0Ω、每cusp固定的complex mask，读取res L_r(j)ω。该输入和source公式具体存在，能检验这类residue是否总落已经扣除的compact-real L1读出类，不是unknown map。

可判的新增transport责任应是：width>1时不能选单一inverse sheet，而要取该cusp的完整∞monodromy orbit trace Σh_j；绕整cut固定该orbit总和。local q_c中j~q_c^-w、holomorphic ω的首阶≥dq_c，trace的integer部分最早z^-2、无z^-1，须保完整width和residue规范。有限branch端点e∈{1,2,3}给subpole型。若ω／mask非real，所获是complex L1 density，不能偷写成real density或直接领取右端正号。

这足以限定准入一次family transport/strong-old比较；尚不是该general family已消费的数学合同。先检它是否只是C047 proof与标准finite-cover trace的直接合成，若是按0轮旧推论收口，不预建C048；若确有新的完整类边界／量词净信息，再按实质准入和计轮。不得将per-cusp mask换成任意sheet-mask，亦不得将holomorphic ω换成有额外极点的meromorphic输入而省掉额外atoms/complex supports。

complex spectral supports、unbounded／不同拓扑、带新数据的relative、非线性/source-adapted或非residue源都不由这个准入排除。正D′各中间层不必消Pan，不能强加逐层关系责任。当前仍先完成584/root的实际版本消费；下一正式稿未出现前不预填family通过或长期Goal完成门。

## 9. root实际版本最终限定PASS

本节替代上面§6、§8的阶段性“root稿／下一稿尚未出现”状态。恢复后重新读取同一Goal／C047／D20261027J与当前STATE，执行research_state check→show，检查实际工作树；当前仍是C047 reviewing，cadence为1，尚未结算584，没有借C046旧预算或把draft当已消费。

已全文核实际584、结算、root前件收据、next-finite-cover-trace-admission，以及Pan最终(15)与scope追加。对root收据中全部12个规范LF绑定逐一从实际文件复算，12项完全相符。最终审核绑定如下：

| 文件 | 规范LF SHA256 |
|---|---|
| notes/584-marked-cusp-borel-kernel-and-pan-residue-collapse.md | 63a2a438666cc859d543503715a16bb7c58c2de80e0a5bd8a22e2a36997c96a0 |
| goals/reviews/2026-10-27-marked-cusp-584-settlement.md | 4d2a7bda90a7275f77b8e309892b9140cda0ec38b96183134485b81c3e5af08f |
| reviews/2026-10-27/marked-cusp/root-consumption-scope.json（最终审前draft） | 1d387f28346666d9e08ede21b448e1931648e07894336e035a3f6605ce3cc23e |
| reviews/2026-10-27/marked-cusp/next-finite-cover-trace-admission.md | c2363abf8a080164cc06f6804df844bab881e0e8b6aa2651494e270cc7f1d40a |

**限定PASS。** 584把object/domain/norm、物理源与selected residue角色、typed输入、所选sheet的monodromy、两次负号、endpoint符号、全部noncompact Pan平移及强费用放在同一闭链，没有把独立producer片段自动升级。共同epsilon控制只消费583同一small-evenφ族；原537全窗定理保持，573固定χ没有冒评。完整两腿由真实essential residue定理给出，Pan的complex倍数扫满同一B的全部源像，所以同B上的任意source-independent后处理若把全部Pan送同一base便全像常值；新Pan稿与root三个消费文件已同步这个更强范围，不再保留“仅把同B改成非线性”的伪逃逸。

584§5及root strongest-old字段已经**现在**扣除405正H加compact Laplace唯一性的全fixed finite complex measure／compact-real support lemma。它不是新的待证下一门，也不另计数学轮；553原全线bounded读出门没有被错误套在指数强费核。新净实物仍是本K11的完整signed-cut Borel身份、右端1728定量实际Pan及必要增长。C047可统一消费一完整数学轮；typed／exactq／Cauchy、一般support lemma、finite rank、两腿线性代数及same-B像集后果不分别加轮。

next文件已给actual finite modular cover、holomorphic differential及whole-cusp固定mask的明确源公式与orbittrace测试，故足以作为唯一**准入比较**。当前没有消费该general family定理；须先判断只是本轮加标准trace的旧直接合成还是有实质新类信息，前者0轮收口、后者另按实际净范围准入，不预建C048。不能把width>1单sheet、meromorphic额外pole、complex/unbounded谱或不同relative数据混入现有闭合；D′中间层也不需逐层消Pan。

结算末“拟统一一轮”准确反映当前draft阶段；实际root结算、唯一cadence1→2／历史47→48、看板／文献库及GitHub同步由root后续执行一次，本审计没有修改它们。584改变的是固定source模型的关系／强费用门，经典whole leading4/5仍为负惯性UPPER，actualq/core/coupling、primitive RR与完整signedζ主瓶颈未改变，长期Goal不因此complete。

本PASS允许root随后只填收据status／本fresh版本与管理状态，保持以上数学文件及12项输入绑定不变；若数学语义或输入绑定再变须重审。上述收据SHA标明所审draft，不伪称后续metadata变化后的JSON仍有同一SHA。
