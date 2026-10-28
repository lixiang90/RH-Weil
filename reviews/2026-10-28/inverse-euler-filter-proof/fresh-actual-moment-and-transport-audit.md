# C053：actual moment与真实Gram运输的独立fresh审查

2026-10-28；`/root/inverse_euler_final_audit` 当前新审查任务，区别于两proof作者、准入fresh及bump辅助作者。已恢复README／STATE、check→show、Goal／原0c4f、AX、当前C053／前沿和当前总结；实际全文读moment终稿、transport最后12520-byte终稿及root物理前件稿，并对必要旧585共同Sonin、C052 strip／localization和uniformPNT范围作原件核对。未读新primary／PDF／web／来源查询／数值，不改其他proof、STATE、Git或cadence。

**限定PASS，无必须修正的数学断点。** 在本稿绑定的实际版本上，全大n矩lower、growing-n原Gram范数运输、归一化谱逃逸与固定g′测试发散可以合成；不是仅核了一个conditional lemma⇒结论。最终root前件闭合、结算和发布仍另行执行。本审不预590、不消费数学轮、不完成长期Goal。

## 1. 对象、源及旧前件没有换位

合同的arch空间是gap1的raw Mellin实现M；moment证明先在positive-halfline的gap-a空间K_a（a=2）构造原Riesz，再按585的同一dilation/Gevrey模板嵌入M。两projection不能互换。辅助H0=ψhat G2与physical测试g不同；ψ固定δ=log2/4、support[-δ/2,δ/2]，g仍587的du norm1正bump，原du／zeroextension Dlog及第一槽linear保持。

旧共同向量稿确实付任意first-fixed a>1的非零raw评价：不能只由“评价连续”推非零，其已用同Sonin域合法除零补齐。Hermitian Riesz在实点t=0满足G_a(0)=||k_(a,0)||²>0；本证明不冒用复参数bilinear evaluator。旧模板也付H0的Gevrey2 upper、真实双gap余量与全部finite polynomial倍在同M的准入，费用允许随degree增长。C053只用这些membership加明确norm估计，不把fixed-degree Gram结论扩大到growth。

Q_X=sup_(||D_Xh||≤1)|h(t)|²是原G_X=PB_X*B_XP逆下的weighted raw evaluator，ν_X=Q_Xdt/(2π)=ρ_X|D_X|^-2dt。没有把取消外D当取消Gram、把B_X当酉或把P G_X^-1P当正交投影。FiniteX正测度、S_X[g]>0和测试域已旧付；本规则仍在原compact源上定义，不对noncompact filtered source套未准的完整pole恒等式。

必要旧界经原proof核对：C052 upper稿§3的strip证明在real轴确给Q_X≤C(1+t²)全线uniform；localization稿§5–6确给raw Q_X≤exp[(-4+o1)A]于每fixed log^B X频带。旧585只在|t|≤X²给uniform twisted-prime absolute o(A)，而global Euler upper另有全线版本。下文分别按其实际范围使用。Bareν strongS′零极限及Sg/Sg′→0是旧0，不决定其ratio；本次结论不由两个零量相除得到。

## 2. TT*逆给真正projection，奇异幂没有被放进错误的L²域

在H=L²(0,∞)，C为2cos(2πxy)的酉自伴cosine transform。L=1_(0,a)，K=LCL是固定有限区间的compact selfadjoint contraction。若||K||=1，compactness给norm-attaining向量，contraction等号迫v和Cv都compact支撑；entire cosine transform唯一性与酉性使v=0，矛盾。因此||K||<1确实支付I−K²和I±K的bounded inverse，未假定随a一致。

T=(L,LC)满足TT*=[[I,K],[K,I]]，故P_a=I−T*(TT*)^-1T是到kerT=K_a的实际正交投影。对Lh=0，block解为P_a h=h+LKw−CLw，w=(I−K²)^-1LCh；两个sign与head约束核准，不是近似投影。

对实s∈(1/2,3/4]，h_s=1_[a,∞)x^-s在L²；head幂p_s=x^-s仅在L¹使用，经K后才进L²。Cosine power公式

    C(x^-s)=χ(s)x^(s−1),
    χ(s)=2(2π)^(s−1)Γ(1−s)sin(πs/2)

由阻尼Gamma积分及Dirichlet极限给出，χ(s)χ(1−s)=1、χ(1/2)=1。Tail截断在L²收敛并具有同一逐点振荡积分表达，因而LCh_s=χ(s)p_(1−s)−Kp_s是合法等式。这里p_(1−s)在s>1/2时为L²；极限p_(1/2)不是L²，证明没有越界施inverse。

分离w_s=χ(s)p_(1−s)+r_s之后，r_s的bracket输入在C¹参数连续；bounded resolvent先给L²连续，再由r_s=b_s+K²r_s和K²的平滑性给C¹连续/一致界。这确实控制s↓1/2，未以形式代入替代极限。

## 3. 临界L²极限识别为原Riesz；有限阶边界是新证出的实际性质

把全半线cosine power的两项先相消，tail代表恰为

    F_s(x)=χ(s) C(1_[a,∞)y^(s−1))(x)−C(Lr_s)(x)，x>a。

第一个振荡积分一次分部积分：y^(s−1)在∞趋0，导数y^(s−2)可积且s∈[1/2,3/4]一致；第二项用r_s的uniform C¹及sin在0为0。故|F_s(x)|≤C/x uniform，包含接近临界的参数，不是未证raw G_a(t)=O(1/t)。与head L¹连续性合用给P_a h_s在H中的强极限k_*。

对每fixed v∈K_a，<v,P_a h_s>=∫v(x)x^-s dx在s>1/2绝对收敛；旧raw Mellin解析延拓使其趋冻结的原点评价。强L²极限与Riesz唯一性遂给k_*=k_(a,0)。这是关键的actual识别，未更换一个边界较好的trial；参数实性也给k的real代表，与第一槽linear相容。

端点极限r_0=−(I+K)^-1Kq只将q=x^-1/2按L¹经过K，w_0=q+r_0为compact L¹输入。于是x>a时

    k(x)=x^-1/2−2∫_0^a w_0(y)cos(2πxy)dy。

第二项entire，第一项在positive轴analytic，所以右侧在a附近有analytic延拓。若a处所有jets零，则在(a,∞)恒零，结合gap使k=0，与已付非零评价矛盾。因此存在固定有限m、右邻域和非零real首系数，给统一定号下界c(x−a)^m。没有强迫m=0，也没有将一般entire非零直接当成物理端点lower。

## 4. 原正卷积与Taylor确给所有大n的4nlogn指数

v=Wk=e^(y/2)k(e^y)在b=log a左侧为0，右侧保同一有限阶m。h=g*ψ*v的Fourier正是ghat H0，原Plancherel给J_n^g=||h^(n)||²_du；这里h只是moment辅助函数，不要求它自身仍在M，更不对它应用完整Weil型。

h因compact光滑卷积属于C∞且每阶导数在L²，左端L0=b−1−δ/2以前恒零且各阶flat。在L0+ε的全部非零贡献中，三个端点距离非负且和为ε；ε小于定号邻域时整个积分同号。保留x1,x2∈[ε/4,ε/3]的矩形使第三距离在[ε/3,ε/2]；两个冻结的positive bumps分别有exp(−C/ε)下界，面积~ε²，得到每个小ε的

    |h(L0+ε)|≥c ε^(m+2)exp(−A0/ε)。

这避免了任何振荡独立性/好频点/子列依赖。Taylor积分余项与Cauchy精确给

    ||h^(n)||²≥|h(L0+ε)|² ((n−1)!)²(2n−1)ε^(-2n+1)。

对每个大整数n取ε=1/n，再用elementary factorial lower，得到logJ_n^g≥4nlogn−Cn。固定m、边界常数和normalization只添O(n)或O(logn)，全大n量词成立。新lemma真正付款的是actual临界Riesz/物理边界/卷积/Taylor链；辅助fixed-bump-fourier-lower-support.md未被本审当成任何依赖，亦不因本PASS认证该未使用稿的单独结论。

## 5. 原Gram的growing-n三段与fixed测试消费

对n=ceil(2A/logA)、R=logX，n=O(√X/log²X)、n=o(A)、4nlogn=(8+o1)A。旧H0 upper给J_n≤exp(4nlogn+C_U n)，不反向作lower。每X的t^nH0是合法finite-degree trial，真实单位向量为t^nH0/||D_Xt^nH0||，所以actual Q_X逐点变分下界和S_X[g]≥J_n^g/N_X²保完整G_X逆及dt/(2π)。

Low段上界包含R^(2n)这一费用，2nlogR=o(A)，故仍exp[(4+o1)A]。Middle只在R≤|t|≤X²用585的uniform式，得到exp[o(A)]J_n，未将PNT外推全线。Outer改y=√|t|≥X，因logy/y递减且4nlogX/X→0，对全部该段统一吸收growing power至Gevrey半指数；余下exp[(4+o1)A]可由exp(−cX)吸收。因此N_X²≤exp(4nlogn+C_U n+o(A))，并非fixed-n尾偷换。

与新全大n lower合并给S_X[g]≥exp[−o(A)]，适用于全部充分大real X；与旧S_X[g]→0无冲突。Actual probability π_X=|ghat|²Q_Xdt/(2πS_X[g])对每first-fixed K有π_X([-K,K])≤exp[(-4+o1)A]→0。故每fixedK给liminf∫t²dπ_X≥K²；K任意即S_X[g′]/S_X[g]→∞。每finiteX该矩有限由旧全线poly/Schwartz支付，不使用uniform integrability或moving K。

最后，任意共同positive scalar β_X若β_XS_X[g]→q0>0，则β_XS_X[g′]→∞。固定compact卷积平方g′*(g′)*因此不能趋任何有限分布值，特别不能趋原完整finite q1。g／g′都在原537 fixed窗口内；q0/q1保全部Γ/contact、Λ(p^k)=logp及双pole，g′没有被称为polefree。没有从正滤波发散推出Q负值或RH反例。

## 6. 消费范围、完成门和版本

结论仅拒本fixed full-prime inverseEuler/commonweight及positive matching-g scalar族，已允许其growing F和nonlocal source inverse；不覆盖其它frequency weights、高gain生成规则、signed/joint、非线性source适应或primitive几何。它不移除完整signed corecross／非零primitive/principal/mixed/Ξ瓶颈，不改善542+555→557的whole4/5负惯性UPPER，更不通过长期Goal完成门。

裸零极限、旧upper/domain/PNT不另计；是否统一结算C053及消费原cadence由root另执行。本审现场观察cadence仍3/history53/latest589/formal17，Goal文件LF SHA仍b3d2acb1…；这是观察，不把将来的合法计轮变动当数学版本失配。无新来源、PDF页、数值或公开全文变更。

实际全文核的冻结版本：

| 原件 | LF bytes | LF SHA256 |
|---|---:|---|
| C053合同 | 5773 | 94a8d147ba05067678d56b691799ee3fac54f7bda8e719d272ce0c6c082de8d1 |
| actual-sonin-gevrey-moment-lower.md | 13693 | 96339651615d5ccf10b999fea7dd3ec3c6f91961be0594433e94de307ef3044a |
| growing-trial-transport-and-fixed-test.md | 12520 | 791ce6cc943de3cc94b8a89de8d3afc5be5b07d939cc545801c703f19667d38b |
| root-physical-boundary-premise-draft.md | 4827 | 8046a3d9542c5580b5d09b2b481af71fb9bfe7cfb378c378a037c19f5e249597 |
| fixed-test-lower/common-sonin-vector-and-polynomial-domain.md | 16348 | dcdf8e91b408423e3647f116f8bd72e040feaf24cf80f9b92db30d776398af85 |
| sonin-scalar-normalization/source-upper-and-tail-proof-audit.md | 10211 | bab769113b4ce8c858dfd4b7a83dea6abd8808436a599d2206ea9a9bf0915fff |
| sonin-scalar-normalization/source-localization-proof-audit.md | 11459 | 809bc7ffc6f1fbf4dd24af0d710af05fb7ca1bc259992430c3fd6760912ffcb1 |
| notes/585-cofinal-sonin-fixed-source-trace-lower-and-core-error-fee.md | 7857 | 5dca916d978eef599587ff4c6ce34144f814ddec0567a4c1b2314dcd71cd01af |

本审仅写当前独占fresh文件，不改绑定原稿或共享状态。**审查terminal／限定PASS，无必须修项；不同fresh出稿仍不代root的最终前件消费和结算。**
