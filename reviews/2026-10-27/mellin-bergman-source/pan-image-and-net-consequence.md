# Mellin–Bergman源：真实Pan同像、mixed根门与强旧净值

2026-10-27；/root/mb_pan独占稿。执行STATE唯一[实际source准入](../arithmetic-theta-section8/next-mellin-bergman-source-admission.md)，不编辑STATE/cadence/Git，不恢复C047预算或预建C048/585。下面的bounded-source前提须与[typed／原费稿](typed-source-and-original-fees.md)按实际最终版本重闭；本稿出稿不代root消费。

## 1. 同一源、同一实际关系及依赖

物理源是复Fréchet空间F=S_exp,C，r(t)=e^(t/2)f_phys(t)，原du范数为L²(R,dt)。记P=C(P_an,C)为405的实际关系空间，C f=e^(t/2)f；它不是事后按当前读出kernel命名的几何principal像。

405的实际正H及其关系为

\[
 p=(D^2-\tfrac14)H\ne0,\qquad p_b(t)=p(t-b)\in P
 \quad(b\in\mathbb R).
\]

每个固定b的全部强源半范数有限，满足
p_(N,k)(p_b)≤e^(N|b|)p_(N,k)(p)；所有有限复线性组合也在P。两pole矩精确为0，完整经典配对对这些关系的mixed项为0。没有crop p_b，也没有把P∩C_c^\infty={0}的空条件当作全关系检验。

[553§§1–2](../../../notes/553-principal-cyclic-closure-and-cofinal-readout-fees.md)已消费

\[
 \overline{\operatorname{span}_{\mathbb C}
   \{p_b:b\in\mathbb R\}}^{\,L^2(du)}=L^2(du). \tag{1}
\]

其实际理由是同一关系p的整Mellin函数不恒零，Fourier限制在竖线上的零集测度0；Fourier唯一性给cyclic密度，不用RH、零点简单性或spacing。(1)是强旧输入，不是本次新的稠密定理。

当前固定holomorphic sector S、κ=3/2、Petersson正交标准基f_j及

\[
 W_j(t)=e^{3t/4}f_j(i e^t),\qquad
 A_r=\sum_j\left(\int_{\mathbb R}r(t)\overline{W_j(t)}dt\right)f_j
 \tag{2}
\]

均沿唯一准入给定。另稿须实际支付W_j∈L²及

\[
 \|A_r\|_{\rm Pet}\le C_B\|r\|_{du},\qquad
 C_B^2=\sum_j\|W_j\|_{du}^2<\infty . \tag{3}
\]

S是fixed model／level的holomorphic子类，有限维；不把源文所有潜在smooth/Maass扩域也纳入这项有限维前提。此处t为physical log-time，modular实部固定0，不与§8的τ=u+iv坐标混同。

## 2. 有界有限像的exact同像：不只是稠密

条件于(3)，A有连续延拓L²(du)→S。令

\[
 V=A(F),\qquad
 U=A\big(\operatorname{span}_{\mathbb C}\{p_b\}\big).
\]

两者是有限维S中的代数线性子空间，所以U闭。任给r∈F，由(1)可取有限Pan线性组合q_n使q_n→r于L²；(3)给A(q_n)→A(r)。U闭遂有A(r)∈U。反向包含显然，因此

\[
 \boxed{U=A(P)=A(F)=V.} \tag{4}
\]

这里image的有限维闭性发生在已明确定义的Petersson空间S中，不是在整个算术Chow群中。(4)没有假设P在原Fréchet中稠密，没有将原强源拓扑换成L²，也没有假设P本身等于它的cyclic子空间。

若要核V=S，也有直接实际检验。设复线性泛函ℓ在A(F)上为0；按(2)，它给某个W_j的固定复线性组合与所有r∈C_c^\infty的L²配对为0。因此该连续函数在全部t上为0。除去非零实因子e^(3t/4)，得到某个holomorphic f_j组合在整条τ=i e^t上为0。holomorphic唯一性及f_j线性独立迫该组合为0，ℓ=0；有限维对偶给V=S。

这一步只检验模输入像，不是经典全源coverage／mixed身份。即使不使用V=S，关系首门已经由(4)完成。S=0的情况自然为V=U=0，不需要另找level以制造非零特例。

也可从(4)选出有限个实际平移p_(b_l)，使其A像构成V的一组基。于是每个r的A像可由一个**有限复线性组合的实际Pan**精确实现。所选b_l、逆矩阵及其条件数均依赖fixed S；本稿没有计算数值b_l、没有给跨model的统一费用，也不把这个存在性basis当新的算术capacity。

## 3. 算术Theta及同数据后处理

沿已审§8来源陈述，Theta:S→hatCH¹(M)按模输入复线性；其定义和height前提仍为cited，不是本次重证。设J=Theta∘A，E=J(F)。由(4)直接有

\[
 \boxed{J(P)=J(F)=E.} \tag{5}
\]

E作为代数向量空间至多dim S维。结论不要求ambient算术Chow群Hausdorff、height正定、Theta某个MW分量非零，或整个arithmetic对象已完成一个Hilbert拓扑。有限像的辅助坐标仅用于线性代数，不能冒充原算术norm。

如果要求J本身将全部Pan送零，(5)迫J全源为0。更一般，任何仅依这同一J数据的source-independent postmap T:E→Y，若
T(Jp)=y0对**全部p∈P**成立，就必在E上为常值y0。实际coset下降
T(J(r+p))=T(Jr)也有相同后果。此处不需要T线性、连续或Y有norm。

多坐标非线性情况必须保留“全部Pan／所有有限复线性组合”的条件。仅逐点测试孤立p_b使T(Jp_b)=y0，不能自动推出T在其线性span上恒值。相反，若J自己是线性且对每个p_b值零，则它当然已杀span，(4)适用。

任何通过同一有限A或J作source-adaptive选择的后处理仍属于这个同数据结论。真正保留A/J以外源数据的source-adaptive、relative或非线性map不在(5)的消费范围；名称不自动赋予其域、原费或完整配对。

## 4. 不误要求literal principal：mixed配对根已足够否定exact Gram

正确的Weil比较可能只要求Pan在一个mixed配对中成为根，而不要求对象map Jp=0。本门不添加ker J=P这样的强要求。

设h是定义在E上的任意固定sesquilinear/Hermitian配对，可退化、可不定。若实际提出的完整比较要求

\[
 h(Jp,Jr)=0\qquad(p\in P,\ r\in F), \tag{6}
\]

则(5)使(6)等价于h(x,y)=0对全部x,y∈E。所以

\[
 h(Jr,Js)=0\qquad(r,s\in F). \tag{7}
\]

这**不**强迫J作为对象map为0：它可以有非零而完全isotropic的像。但任何这种exact relation-consistent height pullback已经全零，不能再匹配537已消费的真实双polezero非根r0的Qζ(r0)>0。该矛盾不需要数值计算A(r0)、确定Theta(r0)非零、或者假设arithmetic height有严格符号。

只有在已给出完整经典Hermitian身份时才作这个exact比较；§8本身没有这样的身份。完整Γ/contact、所有proper powers和双pole没有被删除，本门也没有把原Weil型换成任意PSD坐标和。

一个有限的条件旁注也应扣除：若G(r,s)=g(Jr,Js)是PSD固定Hermitian pullback，且另有在**全部同一global F**成立的下界G(r,r)≤Qζ(r)，则对p∈P有0≤G(p,p)≤0。PSD的Cauchy–Schwarz使P成为G的mixed根，再用(5)得G全零。这只排除这个同一全域表式提供非零PSD下界；G=0时仍须独立证明Qζ≥0。它不排除fixed-window、变域、不同source、带signed误差或非逐层下降的lower策略。

## 5. 家族／极限与原norm范围

每个fixed sector各有自己的C_B。(4)不需要跨B/level统一C_B，但也没有支付这种统一性。

若一族fixed finite maps每个成员都仍定义于全部global F、均有有限du bound，并且每个成员精确下降全部Pan，则各成员在同一实际像上已退化。zero线性成员的pointwise极限仍为zero；constant postmap成员即使具有极限也仍与source无关，不能产生非平凡源信息。它们的base常数可以非零，不能仅用“非零极限”来判定修复；令C_B发散本身不改变这些memberwise事实。

这不覆盖以下合法责任：

* source domain随窗口改变、只对compact restrictions付费，或采用不能延拓为同一global bounded reader的拓扑；
* nonholomorphic无限输入或额外实际relative对象，尚未由本holomorphic固定S的有限像编码；
* 中间层不精确消Pan的独立正D′逼近。完整Weil分布的逐compact卷积平方极限不要求每层先消noncompact Pan；
* 真正新增的source-adaptive数据、非局部／unbounded map，或者一个有实际误差预算的joint signed比较。

对这些域不能借(1)无声延拓测试。尤其不能用P∩C_c^\infty={0}让关系测试空过，也不能将crop p_b当成仍在P，或未付uniform tail就通过极限。

原du与zero-extension Dlog的费用由另稿按同一physical r支付；Hlog多一个1，不改称同一范数。额外source强半范数、global arithmetic Green/vertical尾和成长量词不能由一份finite Petersson norm自动获得。

## 6. 最强旧净值、停止与计轮建议

本次净链是另稿标准cuspidality付款(3)＋553已消费真实cyclic密度(1)＋有限维像闭合。它准确判断了**这个**实际Mellin–Bergman公式：若后续要求全Pan literal下降或完整mixed根兼容，则相应class／height读出退化，不能保完整537正非根。

这不是第一次发现bounded-reader障碍，也没有新的完整Weil预算、独立primitive整模型、截面乘法／mixed RR或growth/core/coupling/Ξ后果。其实际source公式虽已给出，关系消费仍是最强旧的直接合成。建议按**标准actual-source／强旧准入0数学轮**保存，不预C048/585，不以“candidate失败”名称领取新实质全方法边界。

最强经典后果仍542+555→557 whole leading4/5负惯性UPPER。停止该fixed ray／fixed holomorphic source：不换basis/ray/level/B/阻尼或再跑probe延长预算。源文的真实算术Theta设施仍存在；本门不证明所有arithmetic theta、primitive或D′方法不可能。

## 7. 后续信息差：具体设施、准确缺口，不另造授权

当前候选不提供下一数学合同。缺口已能具体定位：§8的实际算术Theta从模输入开始；本formula给出的原global L²有界finite桥受553覆盖。若要继续该设施，必须给真正不同且合法的source/target及完整Weil比较，而不是对(2)改权或换level。

一个可向root提交、**本稿未执行source运输也未自动准入**的实际不同数据候选，是本次§8审查已定位的Theorem7.4中的classical theta kernel。为使下一输入可核，本分支按root追加指示只定位了该kernel的定义／原式，没有展开证明或后章：

* 作者PDF21，(5.3)及Prop5.1给
\[
 R(x,z)=|(x,w(z))|^2\,|(w(z),\overline{w(z)})|^{-1},\qquad
 \varphi_\infty^0(x,z)=
 [4\pi(R(x,z)+2Q(x))-1]e^{-2\pi R(x,z)}.
\]
  同页的μ=(1/(2π))(i/2)dz∧dbarz/(Im z)²是所用体积形式。本分支目视该页核了系数及两个Q的方向。
* PDF22，(5.7)/(5.8)明确majorant
  (x,x)_z=(x,x)+2R(x,z)，**Schwartz函数是**
  \(\varphi_\infty(x,z)=\varphi_\infty^0(x,z)e^{-2\pi Q(x)}\)；
  不能将没有这额外Q因子的varphi0叫作普通Gaussian／Schwartz。
* PDF29，(7.22)给实际
\[
 K(\tau,z)=
 \sum_{x\in O_B\cap V}
     \varphi_\infty^0(\sqrt v\,x,z)\,q^{Q(x)},
 \qquad q=e^{2\pi i\tau}.
\]
  这里不另插v^(3/4)。PDF29(7.23)与PDF30 Th7.4的高度配对系数为1/2。当前只核定义／陈述，未证明此kernel的两端／空间Sobolev运输。

对同一compact M(C)，可先写均值零空间投影

\[
 P_0^z K(\tau,z)
 =K(\tau,z)-\operatorname{vol}(M)^{-1}
   \int_{M(\mathbb C)}K(\tau,w)d\mu(w),
\]

并提出

\[
 \phi_r(z)=\int_{\mathbb R}r(t)e^{3t/4}
                 P_0^zK(i e^t,z)\,dt,\qquad r\longmapsto a(\phi_r).
\]

这个目标保留a(C∞_0)的nonholomorphic／infinite analytic Green数据，和当前finite holomorphic A不同；它不是把ray、B或level作为修补参数。新source中的e^(3t/4)仍是本候选另列的评价框架，不属于上式K的native定义。literal x=0项由varphi0(0,z)=−1为常数，P0杀掉它；这不等于已经付清全部small-v Poisson主项、其余格点尾或空间导数。首门须按上述**实际polynomial-Gaussian／K-type规范**付款t两端、空间导数、mean-zero、Dirichlet energy及全Pan测试。若实际仍全du bounded到分离energy，则553依旧先行；目前没有该实际费用或非零性结果，不能凭Poisson直觉宣布成功／失败，也不应跳到§9–11或新paper。root只有在其actual input/test/净比较真实清楚时才可选择这一个门。

若没有这个或其他真正新实物，最有价值的执行是保存并核验准确准入账：r→模／metric源的公式与domain，Pan如何实际成为base／mixed根，537同源非根，原norm／完整Green尾，以及完整Γ/contact/properpowers/双pole signed身份。参照本次§8root收据、553原费门、582实际source/Green收据和560/577完整signed责任；不存在的箭头不能用“新几何”“去读下一paper”代替。已有559的Pan crop、012的near-radical/operator-gap区别也不能重开作新core输入。

以上只是有依据的候选／缺口定位，不是第二STATE或给root的新授权。本任务只编辑这一独占稿。
