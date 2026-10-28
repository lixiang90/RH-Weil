# 一次marked-HNF两源尝试：中心化完整格theta缺陷

2026-10-28；G20261027/runtime1793085111/原0c4f。执行冻结的next-marked-hnf-formula-formation唯一一次形成与便宜自筛；无新source/web、proof合同、数值或参数搜索。原件恢复README/STATE/check→show、Goal/C049/D20261028Y/当前next、HNF前置与root/fresh限定。只写本独占稿，不改STATE/cadence/Git；draft不是root消费结果。

## 1. 唯一规则先冻结（本段落盘时检验pending）

固定原H_B={H=[[a,b],[0,d]]:a,d≥1,0≤b<a,ad≤B}，n=ad，G_H=HᵀH。所有content、Smith与prime valuations按原数据保留，b=0包括；没有GL₂ invariant或极化主张。索引字典同583，而本次检验的是下面marked Euclidean热reader，不凭raw旧一概拒绝它。

对T>0定义**完整**格theta

\[
 \Theta_H(T)=\sum_{(m,k)\in\mathbb Z^2}
       \exp\{-\pi T[(am+bk)^2+d^2k^2]\}.
\]

以T=e^(2v)进入长度对数坐标，冻结中心化prefactor与两个主项为

\[
 \boxed{K_H(v)=\sqrt T\,[\Theta_H(T)-1-(nT)^{-1}]
     =e^v[\Theta_H(e^{2v})-1-n^{-1}e^{-2v}].} \tag{F1}
\]

**√T已在规则中，不是未加权缺陷失败后的修补。** 它是二维长度Mellin反射中心的标准half-density：Poisson的T^−1经长度坐标有权2，中心化权为1。未采用Θ_H(T)−1−1/(nT)的无权版本；后者没有下文所需uniform界。

仅作Hermitian偶化及固定计数概率平均：

\[
 \kappa_H(v)=[K_H(v)+K_H(-v)]/2,\qquad
 \kappa_B(v)=\frac1{|H_B|}\sum_{H\in H_B}\kappa_H(v).
                                                        \tag{F2}
\]

两个独立complex physical源r=e^(u/2)f、s以原自相关进入：

\[
 h_{r,s}(v)=\int_\mathbb R r(x+v)\overline{s(x)}dx,\quad
 \boxed{C_B(r,s)=\int_\mathbb R\kappa_B(v)h_{r,s}(v)dv.} \tag{F3}
\]

不先取PSD Gram。C_B第一槽线性、第二槽共轭线性；κ_B real/even使其Hermitian。原cutoff为ad≤B、原等权1/|H_B|；后文不得改权、窗口、heat变量、norm、source域或level再试。

## 2. 完整经典目标承担项（尚未认证）

此尝试的动机是：同一有限指数格有零向量、covolume、完整非零格点与Poisson dual，(F1)先扣两端主项，再保marked shape的signed热波动。希望借该actual双源读出承担完整Weil式中的signed **H−P**，而非另造positive metric再列unknown identity。

实际候选全型仅为

\[
 B_B(r,s)=q_\Gamma(r,s)+C_B(r,s),\qquad
 B_\zeta(r,s)=q_\Gamma(r,s)+(H-P)(h_{r,s}),
\]

\[
 H=2\cosh(v/2)dv,\quad
 P=\sum_{p,j\ge1}\frac{\log p}{p^{j/2}}
           [\delta_{j\log p}+\delta_{-j\log p}].
\]

Γ=Reψ(1/4+it/2)−logπ、原FP/contact与dt/(2π)外腿准确复用。H含两pole的mixed平衡，不删odd负方向；P含全部proper powers原权。**未声称F1的二维零／volume项已经等于经典双pole，也未认证C_B→H−P。** 这正是下文最便宜actual target门，不将未知完成身份算作输入。

本段落盘时仅冻结(F1)–(F3)和目标角色；检验与最终分类待追加，不能将此稿当新已proved结果。

## 3. 最便宜actual norm门：该冻结prefactor确实给uniform有界密度

以下仅检验(F1)–(F3)，没有替换其热参数或权。冻结前段为3067 bytes，LF SHA b2aba545690c4e3fb3c0cdacb1941950e85c350a0d528ee75cdbcabfaa8c5260。

先记一维平移Gaussian和。间距a的点在[−R,R]中至多1+2R/a个，故layer-cake直接给，对所有实z、T>0，

\[
 \sum_{m\in\mathbb Z}e^{-\pi T(am+z)^2}
 \le\int_0^\infty2\pi TR e^{-\pi TR^2}(1+2R/a)dR
 =1+\frac1{a\sqrt T}.                                    \tag{T1}
\]

对完整Θ_H先在m行使用该uniform-shift界，再对k使用同式，得

\[
 \Theta_H(T)\le(1+(a\sqrt T)^{-1})(1+(d\sqrt T)^{-1}).       \tag{T2}
\]

b未被删去或换成0，(T1)恰好对z=bk统一。另一方面，零向量给Θ_H(T)≥1；完整二维Gaussian Poisson以covolume n给

\[
 \Theta_H(T)=(nT)^{-1}\Theta_{H^{-T}\mathbb Z^2}(1/T)
 \ge(nT)^{-1}.                                            \tag{T3}
\]

因而对实际中心化K_H，(T2)给

\[
 K_H(v)\le a^{-1}+d^{-1}\le2.
\]

分别用(T3)的两个lower，得K_H(v)≥−√T及K_H(v)≥−1/(n√T)，合并为

\[
 K_H(v)\ge-\min(\sqrt T,(n\sqrt T)^{-1})\ge-n^{-1/2}\ge-1.
\]

所以是**ALL H／ALL实v／ALL B**的actual界

\[
 -1\le\kappa_H(v),\kappa_B(v)\le2,\qquad
 \|\kappa_B\|_\infty\le2.                                \tag{T4}
\]

这里未用未加权缺陷的错误uniform界。H=diag(1,n)、T=1/n并不反驳(T4)：未加权量可为√n阶，而本冻结式中√T已是n^−1/2。没有在得知失败后添加该因子。

对全部complex r,s∈L¹∩L²，Young/Fubini给‖h_rs‖₁≤‖r‖₁‖s‖₁，故

\[
 |C_B(r,s)|\le2\|r\|_1\|s\|_1.                           \tag{T5}
\]

这覆盖全S_exp与Cc∞。若r,s支持I_L=(−L,L)，则

\[
 |C_B(r,s)|\le4L\|r\|_{du}\|s\|_{du}
 \le\frac{4L}{\log2}\|r\|_{Dlog}\|s\|_{Dlog}.              \tag{T6}
\]

原Dlog为zero-extension后log(2+|t|)的Fourier型norm，故最后一步只用其既定L²下界。B和L、频高始终不同量词；(T5)不是全线L²有界声明，也没有要求逐层exact消Pan。有限H索引亦未被错误当作physical有限rank。

## 4. 一个固定两源反测，明确排本规则的cofinal完整身份

这不是从finite-B一个系数不同跳到极限不可能。由(T4)可对**所有B同用一对fixed源**。

取任意实非负ψ∈Cc∞((−1,1))且‖ψ‖₂=1，冻结ε=1/256、α=log2，令

\[
 s_\epsilon(u)=\epsilon^{-1/2}\psi(u/\epsilon),\qquad
 r_\epsilon(u)=s_\epsilon(u-\alpha).
\]

两者都是原complex空间中的合法实源，原du norm为1、原Dlog norm固定有限，支持均在I_1中；不随B变化。其自相关h=h_(rε,sε)满足

\[
 h\ge0,\quad\operatorname{supp}h\subset
 [\alpha-2\epsilon,\alpha+2\epsilon],\quad h(\alpha)=1,
 \quad\|h\|_1=\epsilon\|\psi\|_1^2\le2\epsilon.
\]

该区间正且只含一个经典prime-power位置log2：log3−log2=log(3/2)≥1/3>4ε，其他正powers更远，所有负位置也在支撑外。因此全部P的实际配对精确是

\[
 P(h)=\frac{\log2}{\sqrt2}\ge\frac14.                     \tag{T7}
\]

不是删除proper powers：其他所有项是这对fixed源的support使其exact0。H的双pole配对仍完整保留，并有0≤H(h)≤4‖h‖₁，因为支撑上|v|<2且cosh(v/2)<2。结合(T5)，ALL B≥1均有

\[
 \begin{split}
 |C_B(r_\epsilon,s_\epsilon)-(H-P)(h)|
 &\ge P(h)-|C_B(r_\epsilon,s_\epsilon)|-H(h)\\
 &\ge\frac14-6\|h\|_1
 \ge\frac14-12\epsilon=\frac{13}{64}>0.                  \tag{T8}
 \end{split}
\]

完整B_B与Bζ的Γ外腿在同一对actual源上精确相消，故(T8)也是其真实mixed差的lower。一个固定B不符没有被冒作cofinal证据；这里是同一对fixed源、全部B的统一分离，因此任何B→∞子列都不能给完整mixed身份，κ_Bdu也不能D′趋于H−P。

若验收只列全部compact卷积平方，Hermitian极化把同一mixed差写成rε±sε、rε±isε四个fixed源的平方差组合。若四个全部趋0，则本mixed差必须趋0，矛盾(T8)。所以也不能凭只写quadratic版本逃过此门；不需要要求有限B层消全部noncompact405。

## 5. 强旧扣除与实际停止

583已经使用同一完整HNF/Hecke raw族及gcd/square aliases、native产品／norm／Green全尾。本规则没有把G、Smith或ambient标记报成新raw，也没有借det/count σ₁或ζ(s)ζ(s−1)的较弱对照领资格；所有H，包括noncyclic与b=0，都在原cutoff内。κ_H的shape dependence是一个实际不同的marked functional，不能仅由“索引同583”就拒绝；此处的拒绝依据是已写出的(T1)–(T8)及原完整目标。

读出没有声称经583的L_r(j)/principal商因子化，也不依赖其非闭base宽读；故未套用不具前件的closed-base结论。548–550的canonical/cofactor／samephysical行族费用亦没有被强套到此theta源。555／578所付的完整prime-power平移与双pole角色正是(T7)／H(h)的强旧目标，不能用p+1的Hecke degree代替logp。标准Gaussian Poisson／一维计数及旧原子目标的这项便宜比较已经决定本候选，不需再付principal、mixedRR、正PSD谱或全高阶completion设施。

**形成结果与责任断点。** 已形成唯一可代入的same-HNF、两独立原源signed规则，包含实际prefactor、cutoff、线性／共轭与全B原费；但它未能承担Γ外完整H−P。最早断点是(T4)所迫的uniform bounded ac读出无法支付一个固定原prime原子；不是后来不知道怎样证明未知positive height。二维零／volume主项并没有被认证为经典两pole，完整目标门已直接失败。

建议按标准工具＋最强旧target的前置自筛0止这一规则，不预C050/587，不试第二formula、不改√T/平均权/B cutoff/norm/source域/level或Γ外腿角色再造。它不是RH反例、一般marked-HNF no-go、全theta或正D′方法边界；允许不同实际signed/joint／relative对象的修复，但本稿没有该新实物，也不把“可能改权”当后继输入。

本次自筛没有新增经典Weil正号、primitive/mixed或actualcore/coupling预算，whole leading4/5负惯性UPPER不变，长期Goal门仍open。所有推导均是本次当前稿，尚待root另行强旧审稿和实际消费；不由本稿自动结算计轮、发布或完成Goal。
