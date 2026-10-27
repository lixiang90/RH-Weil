# 固定c2设施测试：独立fresh审查

2026-10-27；`/root/c2_fresh_audit`独占。恢复已实际读README／STATE、check→show、G20261027、C046结算、D20261027G、宏观前沿及固定pair门；C046预算不恢复。本文只改本审稿，不改STATE／cadence／producer原件。初始状态为producer尚在实施，故下文先付恒等式／消费范围；实际证书未读前不宣布数值PASS。

## 1. 对象和独立恒等式

physical H=L²(R+,dx)，F自伴酉且核2cos(2πxy)。Hcut=1_(1,infinity)，U=U_log2，(Uh)(x)=2^−1/2h(x/2)。本固定real输入仍为h0=1_[1,2]、原F8，f=Bh0。保存的ell*=1_(0,1)(g+p*)由384个精确g项和27个有理even-monomial系数定义；v*=f−Hcut F ell*保完整无限Fourier尾。它不是finite physical grid，也不是quotient标签。

我独立从四项展开核得：令a=Fell*，U Hcut=1_(2,infinity)U，故

\[
\begin{split}
 \langle v_*,Uv_*\rangle={}&\langle f,Uf\rangle
 -\langle\ell_*,F Hcut U^{-1}f\rangle
 -\langle\ell_*,F Hcut U f\rangle\\
 &+\langle\ell_*,U^{-1}\ell_*\rangle
 -\int_0^2 a(x)2^{-1/2}a(x/2)\,dx.
\end{split}
\]

第一cross由< f,UHcut a>=<Hcut U^-1 f,Fell*>转移；第二cross由<Hcut a,Uf>=<ell*,F Hcut Uf>转移。最后一项从<Hcut a,UHcut a>=∫_2^infinity aUa，减去全< a,Ua>的0..2部分；FUF=U^-1给全项<ell*,U^-1ell*>。因此两个负号、U方向、末项负号和边界2均正确；第四项真实支撑是(0,1/2)。这里没有删除物理无限尾，而是用exact Plancherel/cutoff身份运输。

## 2. 输入误差与尚待核的求值误差

原vector消费已限定给δv≥||v−v*||，v=PBh0，δv<1.061·10^−16；窄norm界给||v||<0.389。因此

\[
 |\langle v,Uv\rangle-\langle v_*,Uv_*\rangle|
 \le\delta_v(2\sqrt{\|v\|^2_{hi}}+\delta_v)
 <8.250\cdot10^{-17}.
\]

该运输只用U酉和triangle，不需v*恰在Sonin M。input费不能代替五个finite integrals／steps求值的区间算术、余项和conditioning。接受门为整个c2有理区间**宽**≤1/1024，必须合并上述输入费。两个producer各项宽≤1/16384是充分分账，不是必要条件或一般最优复杂度。

当前需要特别核：g中sin/y在0的可去奇点与Σtau消去；integer/half-integer endpoint的sin=0、cos=±1及Si辅助函数的相位；大频率Laplace finite-geometric remainder的真实符号；small频率Si Taylor/π argument费；p*大单项系数消去／高moments，不以低精度float代证；末项cosine Taylor必须是整个0..2的uniform／L²余项，并为乘积积分另付交叉误差。

## 3. 消费上限与后续准入

固定c2若pass，只证明这个explicit analytic表示实际可读一个bounded mixed pair；不提供Gv、a=<v,Gv>、b=||Gv||²、非零full-G trial/J/true residual，不使q0宽1/16通过，更不提供五源T/E/Hfin或经典RH。旧535/560 trace设施和542+555→557 whole leading4/5负惯性UPPER仍为输入，原du/Dlog、ALLcomplex、全Γ/contact/properpowers/双pole及成长core/coupling责任保持。

whole-G新准入不能只说“c2已算所以把所有prime再做一次”。它需给实际适用的函数类／finite action或pair规则、目标a/b或true residual的完整同对象误差及成本，并说明成功/失败能改变哪个具体选择。仅增加pair数／阶数、重写未知G逆或重复scalar不是新input。若无这类可执行比较，则按原单测试停止，不把设施验证链当作长期数学目标进展。

本次若最终只是旧exact身份的标准有理实现与固定数值验证，数学轮增量为0；不建C047/584，不恢复停止路线，不以代码数/运行次数计轮。新的严格全量词结果如真出现须另按实际范围结算，不能用0标签藏新数学。当前经典关键瓶颈未因恒等式或有限求值改变，Goal完成门仍open。

## 4. 实际代码／证书审查

已全文读两个producer脚本／证明稿、actual JSON及root aggregator。独立in-memory重放mixed.make_record(precision180)及tail.make_record(precision260,N32)，除elapsed_seconds外所有JSON字段exact match。该审查会话19260已terminal exit0，不留后台；没有重跑旧scalar／G。

mixed的半整数辅助式正确。设Q(k)=πk(π/2−Si(πk))、Q(0)=0，则integer k≥80有Q(k)=(-1)^k∫_0^infinity e^-s/[1+(s/(πk))²]ds。这里odd parity的负号不能借旧T(n)的even相位省略。finite geometric remainder真有符号且≤下一factorial项；small-k由real sine Taylor积分余项与π argument差付款，不依赖未证明的渐近无限求和。180位向外算术足够承受small Si的大中间项，接受仍是实际区间宽比较。

sin-product核可由J(c)=∫_0^R(1−cos(cy))/y²dy=(cos(cR)−1)/R+cSi(cR)独立推导。integer／half-integer endpoint使k±=2R|a±b|同parity，cos差精确消失，故

\[
 I_R(a,b)=\min(a,b)+[Q(k_-)-Q(k_+)]/(2\pi^2R).
\]

代码freq key=m意为a=m/2，base_twice及factor1/(2NF²R)均正确。cross_down与cross_up的√2／1/√2、highclip端点max(1,d/2)..d／2d..4d正确。compact项g(2y)的额外1/2及p*(2y)的4^j全部保留；最后乘√2。odd sine-moment的I_n=−R^n cos(πmR)/(πm)−n(n−1)I_(n−2)/(πm)²是实际endpoint递推，j0为Si/π；不是把第四项读成norm。

我另以512个canonical endpoint区间的exact Fraction sweep独立求f(x)f(x/2)积分，核得−3955669/9699690，与producer全pair-overlap组织相同。对k=1,2,39,79,80,81,200,19399380，用220位mpmath Si作不同算法的sanity check，全部值位于outward Q区间；正式认证仍来自上述有理Taylor／Laplace余项。

tail脚本的g零moment用了Σtau=0消常数的exact Si式。其余even moment是integer endpoint的有限integration-by-parts闭式，代码各factorial／inverse-π系数正确。ell*本身L1可直接界为2+Σ|p_j|/(2j+1)，无需用粗R0界；本次约28.6685。N32真实cos Taylor在0≤x≤2给eps≈3.719·10^−19；若A≥sup|Fell*|，乘积积分误差为2/√2·(2Aeps+eps²)，约6.032·10^−17。精确monomial积分的系数2^(2j+1)/(2(j+k)+1)正确，1089项rounding和1/√2根界全部保留。

root aggregator已手工以Fraction重新做五项符号／端点合成，再加减δv(778/1000+δv)，得到与actual JSON完全相同的有理端点和总宽；全部source LF hash与当前文件一致。正式c2区间由JSON有理数定义，向外短显示可写

\[
 c_2\in[-0.039604989843303151,\ -0.039604989843302864],
 \quad\operatorname{width}<2.857\cdot10^{-16}<1/1024.
\]

因此**固定c2设施门限定PASS**。negative c2只是一个unitary dilation的mixed coefficient，既不是Weil/J/T/E型负值，也不是q0负值或Hfin反例。q0=<v,G^-1v>仍有其独立正投影意义；本次没有计算它的窄区间。

本段审到的规范LF版本如下；hash只绑定版本，不替上述证明：

| 文件 | SHA256 |
|---|---|
| scripts/tf_reader_c2_mixed_terms.py | 5e0b9bb4848a3485235a6cd7f87bd756bd7e822510db716192e5e9c5334afad0 |
| mixed-terms.json | 5f55a5b7d7284ccc6dd7e2899129a65e6436b97c7d2a7e2a8e16217250583721 |
| mixed-terms.md | 2f0a2d4f51c193375b5904d5f4f7b0cc8d37e2d0799166ba5afe6c5eb05e782b |
| scripts/tf_reader_c2_tail_term.py | c00ef23129ea699140d66148656dac1e39b28bffda95ae1d251c1193dce44659 |
| tail-term.json | 85c2380c85046dbb601b60fca37c0795449b0a091c17e55a38664d017acd1b7b |
| tail-term.md | a3253cefc240f30abb53c21fe60ebe820b9a6a3908d1f0e80cda83d74e670d07 |
| scripts/tf_reader_fixed_c2_certificate.py | 3da7306faacfa758c4476e6db71c985105bb88844e9cd10a69ed5bae6808b65b |
| fixed-c2-certificate.json | b15e6da48c1c8e8ddf1ffc50cea38266005a05607d2bf7ef5d548e23a0183d3d |

## 5. whole-G再准入：当前不通过，限定失败范围

我独立用exact Fraction枚举W=B*B的乘积

\[
 W=\prod_{p\in F8}[(1+1/p)I-p^{-1/2}(U_{\log p}+U_{-\log p})].
\]

8个exponent∈{−1,0,1}给6561个word，prime唯一分解使ratio全不同，范围[1/9699690,9699690]；central系数准确为165888/46189。绝对系数和是∏(1+p^-1/2)²，即先前u的上界对象。固定ratio2的c2并不覆盖该预算，更不覆盖P W v的projection forcing或b=||Gv||²。

若原样把本次tail的N32 uniform Taylor包络从cutoff2延至maxratio NF，它乘(NF/2)^66，同一充分eps上界约10^422.83，完全无信息。这只否定**原样复用这一个小cutoff证书**，不是必要复杂度lower、整个analytic表示失效或全方法不可能；可保真正有费的远尾／振荡积分／source-adapted／compressed组织。

当前尚无实际whole-G a/b/action规则和全ratio费用／true残差预算，所以whole-G再准入**不通过**。不得据fixed c2 pass自动续6561 ratio、扩Krylov或另一个源模式。下一行动必须重新给具体actual input/test/net，或按既有连续非核心触发作战略取舍；本段枚举和充分包络对照是标准成本审查，0数学轮，不建立新方法类边界或改变classic关键瓶颈。

## 6. 新实际c2之后的一次便宜预算比较：准入限定

root随后提出只用已产n=||v||²和c2，再作一次整个G残差包络的有理预算比较，不执行G、其他ratio或Krylov。该候选有具体实际input和能改变选择的test，可作下一准入，但必须先扣下列更强旧exact后果。

令W2=(3/2)I−2^-1/2(U+U*)，则实际

\[
 a_2=\langle v,W_2v\rangle=(3/2)n-\sqrt2\,c_2.
\]

rest七个prime的正可逆因子相互交换，drest I≤Wrest≤urest I。因W2亦与之交换，drest·a2≤a=<v,Gv>=<v,Wv>≤urest·a2。这里G没有与每个dilation交换的假设，v∈RanP足够；被比较的是whole uncompressed W的二次型再用v的物理角色运输。

**更强旧lower**：v=PBh0及||h0||=1给

\[
 n=\langle v,PBh_0\rangle=\langle B^*v,h_0\rangle,
 \quad a=\|Bv\|^2=\|B^*v\|^2\ge n^2.
\]

B的normal性来自有限commuting-unitary dilation乘积。也可由旧q0≤1和Cauchy n²≤a q0得相同后果。这一lower约0.02266，比drest·a2约0.000517强，因此新比较必须取a_lo=max(n_lo²,drest·a2_lo)，不能改善一个较弱lower就声称whole残差净改善。p2的upper仍可能影响fixed a/J/q0下界，不能反向泛称c2没有任何固定数值作用。

对同一z=t v，实际r²=n−2ta+t²b，b=||Gv||²≤u_hi·a。若0≤t≤2/u_hi，则

\[
 r^2\le n_{hi}-(2t-u_{hi}t^2)a_{lo}.
\]

这是有相关性的包络，不能把a/b作无关rectangle多付误差。该已冻结包络关于t最优是t=1/u_hi，因此一项cheap exact比较即可判断其上界n_hi−a_lo/u_hi能否付原d_lo/32门，不应继续调t／prime／degree。若a_hi<u_hi(n_lo−target)，甚至免费知道exact a时，该同一b≤u_hi a包络仍不足；这时缺的是更紧的b/a或actual残差信息，而不是再改善弱a_lower。

此处只接受下一次有理预算比较的研究准入，尚未执行其新数值证书；用户权限仍来自原始直接研究请求。若不足，停止此input／包络的自动续算。它不声称actual r²的下界，不否定一般trial、真正b费用、source-adapted／compressed路线，也不因一个scalar-envelope边界完成长期Goal。标准旧不等式加固定数值预算对照为0数学轮，若有新实质全量词结果则须重新按实际范围结算。

## 7. root消费稿审查

已全文核root实际`tf-reader-execution/fixed-c2-execution.md`、`tf-reader-c2/root-consumption-scope.json` draft及`next-one-trial-budget-admission.md`。收据绑定的16个规范LF版本全部与现场一致，含旧vector/norm/gap及三新脚本／分项／root实际证书；没有以未出现的稿件代消费。root对当前fixed real/physical对象、源成长范围、关系／quotient角色、全部误差／方向、coverage-coupling／strongest-old净值的叙述均与本审查一致。

root主稿准确区分固定c2负值与Weil/J/T/E/q0符号，fixed-c2全宽通过与full-G／原五源尚未执行，standard建设性0数学轮与长期Goal open。当前whole-G action不自动准入；下一项只作一份cheap correlated-budget比较，已经扣强旧a≥n²，a上界与下界均取新旧交集。第6节的a2/rest七prime Loewner、b≤u_hi a的相关消费、冻结t=1/u_hi包络最优、n_lo−a_hi/u_hi所诊断的对象和单次停止均在实际next稿中明确。未发现符号／方向、系数、原norm或量词缺口。

本段审到root主稿LF SHA为`2da19cdbc007d0105d8e2a648a21b8ea1642392cc52e3c7703f2fc2c6848bf73`，下一准入稿为`30de9f34356f5720a32644402f046662a7313ce26d7ab66dad1e50d4a002dafc`，root收据draft（status=root-draft-awaiting-final-fresh）为`8c6b7822a0ee4adf2a88f4d8d6592c1745f9388183f684e8e236e3afa63fd18e`。填最终状态／fresh hash之后该收据hash自然变化，不递归要求审稿绑定自己的hash。

最终限定结论为**PASS**：消费本次固定c2实际数值与表示求值能力，并准入一次已冻结预算比较；该下一比较的数值尚未运行，不预填其结果。数学范围不包括actual Gv、一般trial不可能性、RH／成长signed或独立primitiveRR。root仅填写收据的最终状态／fresh审核hash而不改变数学内容时，本审查继续适用；若语义／依赖改变须重新审。
