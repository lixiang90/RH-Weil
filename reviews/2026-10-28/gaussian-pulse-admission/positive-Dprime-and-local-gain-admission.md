# 正型D′收敛、谱vague运输与同密度local gain必要费

2026-10-28；`/root/rational_first_gate`当前独立root-premise任务，非旧polyfresh／phase几何续算。已恢复README／STATE、check→show、Goal／原0c4f／AS／macro frontier／当前执行及实际工作树。读当前root3548-byte规则与两terminal稿，回核589已根闭合的actual fixedδ／B=1 kernel接口。本稿不web／PDF／下载／数值，不改STATE／Git／cadence，不建新Goal／合同或第二候选。

**限定PASS：拟议更强必要费成立，未找到反例；关键positive-type D′→S′／谱vague桥在下文实际证明，不先假定为已付。** 对任意共同、source-independent、nonnegative measurable w_X，使ν_X=w_Xρ_Xdt为正tempered谱测度，若其physical分布真趋完整Wζ于D′，则有一个fixed compact band J远离0及c,C>0，使全部大X有

\[
 \boxed{\operatorname*{ess\,sup}_{t\in J}w_X(t)
          \ge C\exp\!\left(c\frac{\sqrt X}{\log X}\right).} \tag{G}
\]

esssup按Lebesgue测度，允许为∞。这不需要degree／项数／内部组织的上限，不排具有该费用或更大费用的规则，也不提供同阶upper或sharp结论。最强旧分类为589 actual局部化＋标准正型分布连续性的直接组合0。

## 1. 前件、原规范与待证拓扑桥

Fourier固定为`fhat(t)=∫f(u)e^(−itu)du`，physical定义为

\[
 \mathfrak W_X(f)=\int\widehat f(t)d\nu_X(t),\qquad
 \nu_X=w_X\rho_Xdt\ge0.
\]

各ν_X先假定为正tempered Radon测度，因此𝔚_X∈S′，对compact smooth卷积平方为正。若s*(u)=overline(s(−u))，则`𝔚_X(r*s*)=∫rhat overline(shat)dν_X`，原第一槽linear／第二槽conjugate与ρ内部的2π规范保持。没有把target Wζ预先放进S′，也没有从单个pole项的增长判定完整target的temperateness。

先证明一项通用命题：若一列这样的𝔚_n在D′中收敛到W，则W有唯一tempered延拓，ν_n趋某个positive tempered Radon测度μ于weak S′及vague。这里不需要ν_n=w_nρ_n的额外结构。下文的N／常数允许依这条sequence；一般实cutoff族的全量词在第3节另闭。

## 2. 当前实际证明：固定compact UBP→统一谱polynomial moment

取一次fixed ψ∈Cc∞，使`∫ψ≠0`，置`q=ψ*ψ*`（末尾星号为involution）。选fixed compact interval K包含supp q。`qhat=|ψhat|²`在原点严格正，故存在a,r>0使`|ψhat(t)|²≥a`于|t|≤r。

对Fréchet空间D_K={f∈Cc∞:supp f⊂K}，D′收敛给每个f的`sup_n|𝔚_n(f)|<∞`。Uniform boundedness于是给某整数N及C，使

\[
 \sup_n|\mathfrak W_n(f)|
 \le C\max_{0\le j\le N}\|f^{(j)}\|_\infty
 \quad(f\in\mathcal D_K).                              \tag{1}
\]

这是对一个fixed support的共同有限order；不声称整个D空间有同一global order。

对任意real y，令`q_y(u)=e^(iyu)q(u)`。它仍在同D_K，且

\[
 \widehat q_y(t)=|\widehat\psi(t-y)|^2,\qquad
 \max_{j\le N}\|q_y^{(j)}\|_\infty
 \le C_{q,N}(1+|y|)^N.
\]

谱正性与(1)给**对全部n及全部y**

\[
 a\,\nu_n([y-r,y+r])
 \le\mathfrak W_n(q_y)
 \le C'(1+|y|)^N.                                    \tag{2}
\]

左式利用完整nonnegative Fourier test；无需限制积分到该interval，也没有从signed测度得到这个不成立的推论。q_y本身也是ψ的调制所生成的卷积平方。

用中心kr、k∈Z的这些interval覆盖实线，且其上`1+|t|`与`1+|k|`相差fixed倍。取L=N+2，(2)逐interval求和给

\[
 \sup_n\int(1+|t|)^{-L}d\nu_n(t)<\infty.             \tag{3}
\]

因为余下是`Σ_k(1+|k|)^(N−L)=Σ_k(1+|k|)^−2`。因此对全部φ∈S

\[
 |\nu_n(\phi)|\le C_L p_L(\phi),\quad
 p_L(\phi)=\sup_t(1+|t|)^L|\phi(t)|.                 \tag{4}
\]

Fourier在S连续，故`|𝔚_n(f)|≤C_L p_L(fhat)`给𝔚_n在S上的共同连续半范数界。这份uniform temperateness是**由positive D′收敛证明出来**的，未从每层单独tempered免费升级。

Cc∞在S稠密：fixed χ∈Cc∞、χ=1于原点邻域时`χ(u/R)f(u)→f`于S。对任意f∈S先用该近似，(4)同时控制全部n的余项，D′收敛控制compact近似上的差。因此𝔚_n(f)为Cauchy，并定义S上连续linear极限，限制到D正是W。S′延拓唯一，且𝔚_n→W于weak S′。

置`μ(φ)=W(F^−1φ)`，其中F^−1为原Fourier的逆；于是ν_n(φ)→μ(φ)对所有φ∈S。μ对nonnegative Cc∞测试为正。对任何compact J，取χ_J∈Cc∞、χ_J≥1于J，正性给`|μ(f)|≤||f||∞ μ(χ_J)`于supp f⊂J的smooth real测试；局部supnorm延拓和正泛函的Radon表示遂给一个positive Radon测度μ。式(4)也给它tempered。ν_n在compact上的质量由smooth majorant统一有界，故将continuous compact测试uniform近似为smooth测试，又得通常的vague收敛。

主证明只需weak S′／vague。若使用strong dual S′，同一sequence的共同S′半范数界与S的Montel性质也足够：S有界集的闭包compact，取有限半范数近似网，pointwise收敛加equicontinuity便对每个有界集一致。此增强不另需谱moment或target前件，但(G)并不依赖它。

## 3. 实cutoff X的全量词：不误套任意net

给定实际real cutoff X→∞，假设𝔚_X→W于D′。先任选一列X_n→∞，第2节构造W的唯一tempered延拓及μ。对**任何另一列**Y_n→∞，同一证明仍适用，虽然N、L及常数可变；其tempered延拓限制到D仍是同一个W，所以由D在S稠密而唯一，spectral μ也相同。

于是对每个fixed χ∈Cc∞，ν_X(χ)→μ(χ)为全部real X的极限：若失败，存在ε>0及X_n≥n使偏差≥ε，和上述每条cofinal sequence收敛矛盾。positive compact majorant再将它扩到vague所需的Cc测试。这里没有要求w_X随X连续、有限X区间上的family有界，亦没有直接对未控制的整个tail family使用UBP。实∞的countable cofinal basis允许这条sequence反证；不把它推广成任意directed net都有cofinal subsequence。

## 4. 完整target迫一个fixed away0正质量，再付local gain

若W=完整Wζ，沿原g′卷积平方的已付目标有

\[
 \int t^2|\widehat g(t)|^2d\mu(t)
 =Q_W[g']\ge2^{-49162}\|g'\|_{du}^2=:q_1>0.         \tag{5}
\]

等号合法，因为g′是compact smooth，𝔚_X在D′上的原收敛与S′延拓一致。若μ只支持{0}，positive Radon性迫μ=cδ₀，左式为0，矛盾；不能容许δ导数来逃逸，因为μ是positive measure。

所以存在一个fixed compact band J⊂R\{0}，及`0≤χ∈Cc∞`、suppχ⊂J，使`μ(χ)>0`。取m=μ(χ)/2，谱vague给全部大X有ν_X(χ)≥m。χ、J在此一次选定，不能随X移动。

令`δ=(min_(t∈J)|t|)/2>0`，R=max_J|t|固定。589实际full-Gram kernel的first-fixedδ／B=1界，在ℓ=logX≥R的大X上给

\[
 \rho_X(t)\le C_\delta e^{-c_\delta A}
 \quad(t\in J),\qquad A=\sqrt X/\log X.             \tag{6}
\]

由ν_X=w_Xρ_Xdt，若esssup_J w_X有限，则

\[
 m\le\nu_X(\chi)
 \le(\operatorname*{ess\,sup}_J w_X)C_\delta e^{-c_\delta A}\int\chi(t)dt.
\]

若esssup_J w_X=∞，下界本就成立。综上得到(G)，例如取`c=c_δ`、`C=m/[C_δ∫χ]`。全部常数可依所需完整target及一次fixed band，独立X、degree、项数及filter系数。这不是增长窗／moving频带估计，也没把trial kernel lower倒作actual upper。

等价的子类结论：若每个fixed away0 band上的`log⁺esssup w_X=o(A)`，而physical D′极限存在，则其谱μ在所有away0 band均无质量，只能是cδ₀，physical极限为constant。它因(5)不能是完整Wζ。该必要费不涉及无穷尾的先验uniform估计；谱尾所需的uniform temperateness由第2节的正型收敛前件迫出。

## 5. 当前Gaussian TV例、exact ratio强旧对照与边界

对当前已terminal的fixedσ TV构造，不必再用第2节：chosenσ的g′配对为q₁>0，故可直接选fixed away0 χ使`∫χσ>0`。TV(ν_X−σdt)→0便给ν_X(χ)≥m，与(6)直接推出同一(G)。Gaussian乘子

\[
 h_X(t)=e^{-t^2/2}p_X(t),\qquad w_X=|h_X|^2
\]

每层是bounded Fourier multiplier，原L²(du) operatornorm为`||h_X||∞=sqrt(esssup_R w_X)`，故至少有`C^(1/2)exp(cA/2)`费用。这里是原source multiplier的norm，不是receiver projection norm、外层Gram条件数或项数M的下界；没有相应upper／最优性／有效算法结论。

最强旧exact对照不能漏：当前已付ρ_X>0 a.e.后，给定任意非负density σ，只要σdt为所需正tempered测度，可在满测集合直接取

\[
 w_X(t)=\sigma(t)/\rho_X(t)
\]

（零测异常点任意定义），就有`w_Xρ_Xdt=σdt` **exactly**。它可unbounded，不一定属于有限Gaussian-pulse synthesis；对unrestricted measurable multipliers的whole-output可达性却强于TV。故“同ρ正锥可达”不是新的独立输入。有限Gaussian稿的内容是特殊finite-Schwartz filter的实现／TV与数学残差规则，不能被exact ratio抹成不存在，也不能冒classic target已选。

(G)对这个exact ratio同样适用：它是paid localization要求的必要反向放大，不是同scale可达或sharp threshold。更一般的正谱若含atoms，不能直接用density ratio精确表示，但已有positive smooth逼近／同一条件运输仍须扣576正锥membership责任。没有由此独立确定完整经典正谱。

覆盖任意degree／有限项数的成长、非局部或内部signed组织，**只要最后仍是同一source-independent positive谱density w_Xρ_X**。不覆盖任意source-dependent nonlinear且不定义共同分布的规则、独立其它carrier或不具此ac形式的每层singular谱；不排exponential／superexponential gain，当前finite Gaussian的actual非constant TV例亦保持合法。Fixedσ的全X primeatom缺陷另由当前oldtarget稿给出，不能把它扩大为整个允许质量成长的Gaussian-pulse class失败。

## 6. 净分类、版本及停止

第2–3节是本次实际核闭的标准positive D′连续性证明，不依未读论文或先验target temperateness；第4节唯一算术kernel输入为589早付actual fixedδ／B=1。相对最强旧应记**直接组合0**，不是新C053／590、C052续算或principal／mixed新输入。它说明必要local amplification，未给完整signed缺陷消失、K不利正部／cross、primitive／principal／mixed／Ξ或whole4/5负惯性UPPER改善。Goal完成门open；cadence3/history53/latest589/formal17不动。

当前版本绑定：

| 原件 | bytes | LF SHA256 |
|---|---:|---|
| [AS冻结规则](root-actual-gaussian-pulse-rule.md) | 3548 | `963e55eaa5a4ea943e847c61199f964d7c4250eb50fdf86a82fa972387266387` |
| [actual Galerkin／TV终稿](actual-galerkin-and-tv-proof.md) | 15246 | `6d6102832a6942165de6df27ddb56b91f155741fff973195ce69ab7811e52920` |
| [old target／atom终稿](strongest-old-target-and-atom-test.md) | 11659 | `7bffb78b25b2046789d447a594617fa2adf10e91d9ac4f49b2744bd53f1a055a` |
| [589 localization原核§6](../sonin-scalar-normalization/source-localization-proof-audit.md) | 11459 | `809bc7ffc6f1fbf4dd24af0d710af05fb7ca1bc259992430c3fd6760912ffcb1` |

已实际读上述当前对象及必要旧定位；本稿不重复整份Galerkin证明，不重审旧PDF，不以current lemma的推导名义扩来源／参数／第二候选。它是供root消费的独占前件核证，不代root解除draft条件、结算或发布。
