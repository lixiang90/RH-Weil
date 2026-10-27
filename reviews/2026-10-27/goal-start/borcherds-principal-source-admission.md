# 启动首门：Borcherds §13 产品、principal 与物理源准入

2026-10-27。只核一个原始章节：[Borcherds，Automorphic forms with singularities on Grassmannians，§13，Theorem 13.3、Lemma 13.1、Example 13.5](https://math.berkeley.edu/~reb/papers/aut/aut.pdf)。作者版 PDF 共64页，定理位于PDF第47–49页，例13.5在第50页；对照 [arXiv alg-geom/9609022v2](https://arxiv.org/pdf/alg-geom/9609022v2)，不以摘要代公式。此次不串 Bruinier 或新的论文。

文献库已另由负责分支保存作者原件 `literature/local/2026-10-27-weil/borcherds-automorphic-products-1998-author.pdf`，本分支实际核 SHA256=`93618b64a0c07f68a085b0b520079b1062a98ff7672159f34f77b1463e0724d2`、448471 bytes。首页日期为1996-09-29／corrected1997-05-29；1998是刊年，不能改写为此PDF修订日。来源和本地原件版本匹配，hash只认证版本。

root 已通知 G20261027 运行实例建立并核 active（createdAt 1793085111）；该通知后本分支在 07:12:53 UTC 继续实际核读作者版 §13 的 line/section 与定理公式。子代理自己的 get_goal=null 属于子代理上下文，不能冒充 root 运行实例状态；STATE 的运行事实由 root 独占维护。

恢复所读：AGENTS、README/STATE、check→show、G20261014 的完成门与基线、C045、MACRO_FRONTIER顶部、D20261027A、10-27战略主稿及582实际Green/Pan/537的相关段。C045已止；本文是新Goal的首个来源／实物准入门，不建立C046。工作树的并行Goal/board/library修改属各负责人，本分支只写本文件。

## 1. 结论与真正的信息差

**该章节确实给正维算术群商上的实际 automorphic section 和可计算除子／log Green 身份，但没有给本项目的任意物理源映射，也没有自动给 principal 下降。** 它比“存在某种Green/对应”具体，值得一次首门；核完应停，当前不准入C046。

这里可改变判断的具体比较有三项：

1. 产品带 weight 和可能非平凡 character；“产品的除子自动 principal”在 quotient 上不是定理的字面后果。
2. 实际输入是有指定模变换、有限principal part与整系数约束的weakly holomorphic模形式。不能把582已有的全源Gaussian/Green输入直接当成此输入。
3. 对直接照搬582 arch-only transport的字面候选，一个非零Fourier模态的Cauchy–Riemann缺陷已足以拒绝其holomorphic输入资格；537 compact非根也不例外。该检验只消费旧Laplace唯一性和初等整性逻辑，未给新的全域方法边界。

## 2. 原件的输入、输出及全部角色

固定偶格M、signature(2,b−)，其正2-plane域D为complex维b−的Hermitian域，P→D为C*主丛。输入F属于ρ_M型、weight 1−b−/2，H上holomorphic、cusp处meromorphic，m≤0的Fourier系数为整数。输出Ψ在P上亚纯、homogeneous degree −k，k=c0(0)/2；在合适算术子群Γ上带unitary projective character χ。其负norm超平面阶数由相应negative Fourier系数给出。产品仅在指定cusp/Weyl chamber邻域得到收敛展开；定理的global延拓不是任意域uniform产品界。

符号取作者版Theorem13.3(3)，在原section/frame中

\[
 \Phi_M(Z,1,F)=-4\log|\Psi_M(Z,F)|
 -2c_0(0)\{\log|Y_M|+\Gamma'(1)/2+\log\sqrt{2\pi}\}.
 \tag{1}
\]

该式是regularized theta integral与log norm的身份，不是经典Hermitian二次型Qζ的身份。weight项、constant和frame变换不能删。本文不把它改称完整Γ(t)=2θ′、proper powers或经典双pole已运输。

原件给的是复解析算术群商上的automorphic几何。整模型、finite-place vertical除子、所有bad primes的metrics与算术Chow身份不由本章自动支付。正维也不自动保证指定primitive部分非零；本门没有选出并证实承担经典源的非零primitive载体。

## 3. Section 不等于 quotient 上的 principal function

由P的定义，Ψ(aZ)=a^(−k)Ψ(Z)，在Γ下另有χ。因此Ψ一般是automorphic line的meromorphic section；其除子表示该line的类，不能单由“存在Ψ”宣布该除子在base上principal。式(1)的log|Y|项正是不能丢掉的metric/frame责任之一。

确有一个合法且更精确的principal机制：在**同一base与group/frame**上，若两个输出s1、s2已具有同一个line及character，则s1/s2是meromorphic function，div(s1)−div(s2)=div(s1/s2)。相同weight只消齐次因子，character的相同比较仍需支付；也不能未经证明将所有unitary character说成finite order而任意取幂消掉。若是零weight且character实际trivial，则单个Ψ可直接降为函数。

这个ratio机制给出要寻找的actualrelative候选类型，却不付 r→(F1(r),F2(r))。特别是：两产品的line相同、除子差principal，不表示同一个非根源的primitive输出必然非零；把所有源都送进principal差可能再次全吞。537测试与完整mixed pairing必须单独核。

同章Example13.5给一个确实可检查的低维控制：F=J=j−744=q^(−1)+196884q+…、M=II_(2,2)，相应函数本质上是j(σ)−j(τ)，在有限点holomorphic而在cusp有极点。它确认正维上的actualprincipal relation存在，并提醒不得删cusp预算；它自身没有把经典物理r送进输入F，也不能认证所需primitive容量。本文不将此已知例子计为新正性。

## 4. 两个直接输入检验

### 4.1 ALLcomplex源不能字面线性送进整数principal part

若要求J:r↦F_r为复线性，而且对于每个r∈S_exp,C都直接满足本定理的整数条件，则每个m≤0的系数泛函a_m(r)都满足

\[
 a_m(\alpha r)=\alpha a_m(r)\in\mathbb Z\qquad(\alpha\in\mathbb C).
\]

取α=i即知a_m(r)=0。因而这种字面recipe没有非零的negative-part除子阶数或constant weight。这里甚至不用uniform norm假设。

这只拒绝“所有complex源的输出本身都是整principal part”的直接要求，不拒绝从实际整数／有理源出发、先证明几何关系后在divisor／current／Hermitian配对上复化；也不说无divisor就所有Green读出为零。任何修复仍要交付可实现源子类、连续延拓和原费用，而非把complex核加权自动当整线丛。

### 4.2 把582的arch-only transport直接套模输入，失holomorphic

取本章实际weight0输入F=J和任意r∈C_c^∞(R;C)，字面照搬582的源积分

\[
 (\mathcal T_rF)(x+iv)
   =\int r(u)e^{u/2}F(x+i v e^u)\,du.
 \tag{2}
\]

固定紧源、v>0，F的Fourier展开及所需导数在积分的compact height区间可合法逐项处理。n=1模态的Cauchy–Riemann缺陷为

\[
 [e^{2\pi ix}]\,\bar\partial\mathcal T_rF
 =i\pi\,196884\int r(u)e^{u/2}(1-e^u)
                         e^{-2\pi v e^u}\,du.
 \tag{3}
\]

若(2)在全部x、v上holomorphic，(3)须对全部v>0为零。t=e^u后，这是compact支持密度

\[
 r(\log t)t^{-1/2}(1-t)\,dt
\]

的Laplace变换。旧582已用的唯一性给r(u)(1−e^u)=0；smooth r只能为0。全Fourier项不能对所有x取消n=1系数。故(2)对任何非零compact smooth r均未成为本定理的weakly holomorphic输入；尚未谈S变换，已经在CR门失败。

把582明确的537奇非根r_*=(D²−1/4)(uφ(u))代入即可：φ≥0偶compact、support⊂(−17/16,17/16)，r_*非零且双pole矩零、Qζ(r_*)>0是旧输入；上面的同一测试说明其字面输入(2)不holomorphic。**这里不是把r_*映为0，而是根本未取得合法Borcherds输入，不能消费Ψ(F_{r_*})来声称“保非根”。**

405真实Pan是noncompact S_exp源。本章未给(2)对此全族的换序/收敛/模输入资格。J的negative Fourier模态在u→+∞带e^(2πv e^u)增长；S_exp的全部线性指数矩本身不能提供这一double-exponential的统一domination。本文不声称每个实际Pan积分都发散，只记录其合法性尚未付，不能用空的compact Pan交来替代全族测试。

式(3)是旧Laplace设施对一个明确字面候选的标准微分比较；不是新算术正性，也不排新的genuine modular intertwiner、不同lift域、relative transgression或有费非局部修复。若未来先以别的操作把r送入合法F，不能直接套此反测否定该新操作。

## 5. 原norm、mixed预算与可见性的位置

本门只在compact r下为(2)/(3)给逐fixed-height的合法微分；它没有获得r到合法modular-input空间的du／zero-extension Dlog有界映射，因而也没有到automorphic section、Green norm或算术height的原费。Theorem13.3的cusp产品收敛不等于所有r/height/level的共同费用。

式(1)线性依赖F，却不等于Bζ(r,s)。来自不同F的divisor、line及metric要形成同一mixed pairing，仍需解释两个源的乘法和完整误差；所有proper powers、Γ/contact、双pole及constant jet须在同一身份出现。不能将式(1)中的Γ′(1)常数视为经典Γ(t)全乘子已经匹配。

因此本门不给Qζ新的正号、whole负惯性预算或growth/core/coupling/Ξ后果。强旧542+555→557的leading4/5负惯性UPPER、537固定窗正性与582设施全部保持原范围。

## 6. 消费范围、停止及重新准入

| 前件 | 本门状态 |
|---|---|
| 正维automorphic domain、真实section／除子及log lift | cited：本章原定理已给，准确保weight、character、constant、cusp |
| quotient上的principal | conditional：零weight/trivial character或同line+character ratio可给；不能从任意产品直接领取 |
| 指定载体的非零primitive部分 | open：positive dimension不代此证据 |
| physical r→合法F | 字面整值复线性／arch-only transport未准入；不同新map仍open |
| 全Pan actualprincipal／537可见 | 未有合法同域输入，不作成功或普遍不可能声明 |
| 原du/Dlog费用、完整mixed身份／RR | open；本门没有付款 |
| 本轮净后果 | 来源域／principal角色的具体纠正与选择信息，无新经典数学后果 |

**停于本章，不建C046，不自动转Bruinier／harmonic-Maass／下一个level或paper。** 重新准入至少要：在指定确有非零primitive部分的carrier上，给出一个区别于(2)的实际物理源映射或整／有理可实现源体系；逐项证明modular输入条件、weight/character/constant及全Pan cocycle，并保537与全源coverage；再付原norm和完整mixed身份。这样的新实物若到位，再与正D′逼近／actualcore备选比较。

本门分类为source review／标准旧推论比较，0数学轮；不是证明Borcherds类方法总体无效，不产生新的全域严格方法边界。单cadence及最终root结算由root维护，本稿不触碰STATE／Goal／board／library。
