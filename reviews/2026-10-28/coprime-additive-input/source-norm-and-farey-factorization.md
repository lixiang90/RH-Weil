# 同一互素加法规则：原域、端点、grid费用与旧Farey责任

2026-10-28；unit_height独占支持。恢复STATE／D20261028R、同Goal、formal17及[唯一冻结规则](actual-two-source-candidate.md)，check后show通过。只闭该规则，不造第二候选、不改权／中心化／cutoff，不web／PDF／数值，不改STATE／cadence／Git或编号。当前cadence0／历史50／latest586保持；本文不代root消费或计轮。

## 1. 原对象与finite-B费用

原physical \(r=e^{u/2}f,s=e^{u/2}g\) 为complex S_exp或compact smooth；本段可扩大到全L²(du)。内积第一变量线性，
\[
 T_a r(u)=r(u-a),\quad U_x=T_{\log x}-I,\quad
 V_x=T_{\log(1-x)}-I,
\]
\[
 J_x(r,s)=\tfrac12[
 \langle U_xr,V_xs\rangle+\langle V_xr,U_xs\rangle].
\]
所有T为原du酉平移；J是Hermitian sesquilinear scalar，\(J_{1-x}=J_x\)，共同平移不变，未宣称PSD。

取原 \(G_c=(\log c+\ell)J_x\)，\(\ell(x)=\log x+\log(1-x)\)。因为 \(\|U_x\|,\|V_x\|\le2\)，
\[
 |J_x(r,s)|\le4\|r\|_2\|s\|_2. \tag{1}
\]
在a+b=c时 \((a,b)=1\iff(a,c)=1\)，且原三腿权准确为
\(\gamma=\log(ab/c)=\log c+\ell(a/c)\)。
正整数a,b≥1给 \(1/2\le ab/c\le c\)，故 \(|\gamma|\le\log c\)。
又 \(\int_0^1|\ell(x)|dx=2\)。因此root原finite-B上界成立：
\[
 |C_B(r,s)|\le K_B\|r\|_2\|s\|_2,\quad
 K_B=8\sum_{2\le c\le B}\frac{\varphi(c)(1+\log c)}{c^2}
 =O((1+\log B)^2). \tag{2}
\]
两源均用原全线zero-extension Dlog时，右侧常数除以log2。fixed-B的积分及有限点值读出均合法；这里没有对r作point evaluation。

输出是scalar mixed form。经Riesz也可在L²给有界self-adjoint算子，但不是算术cycle／primitive类或既定Weil分布。三腿赋值在系数中只以既定log-linear组合出现；不把它称为已取得新的prime-coupled身份。另一方面x=a/c与分母仍记录实际加法三元组，不能粗说所有整数信息都已消失。

## 2. H¹端点消失与J′的真实mixed费用

令
\[
 R=\|r\|_{H^1},\quad S=\|s\|_{H^1},\qquad
 D=\|r\|_2\|s'\|_2+\|r'\|_2\|s\|_2\le RS.
\]
H¹采用原du和一阶弱导数。对0<x≤1/2，
\[
 \|V_xr\|_2\le|\log(1-x)|\|r'\|_2\le2x\|r'\|_2.
\]
与(1)同法及x↔1−x对称给
\[
 |J_x(r,s)|\le2\min(x,1-x)D. \tag{3}
\]
这是H¹费用，不是全L²源的O(x)结论。

H¹向量的平移在L²中可强微分，故
\[
 U'_xr=-x^{-1}T_{\log x}r',\qquad
 V'_xr=(1-x)^{-1}T_{\log(1-x)}r'.
\]
对J的四项求导，在x≤1/2时，将每个x⁻¹项与另一腿V_x的O(x)配对，得到
\[
 |J'_x(r,s)|\le
 2\|r'\|_2\|s'\|_2+2D\le4RS. \tag{4}
\]
x≥1/2由对称相同。因此J在(0,1)为C¹，延拓到[0,1]是Lipschitz，两个端值均为0，且
\[
 \operatorname{Var}J\le4RS.
\]
没有用H²或pointwise source导数。

## 3. G_c的BV／绝对连续原域

由(3)，x logx趋0给
\[
 G_c(0)=G_c(1)=0.
\]
在开区间
\[
 G'_c=\ell'J+(\log c+\ell)J',\qquad
 \ell'=1/x-1/(1-x).
\]
利用(3)，可粗取 \(\int|\ell'J|\le4D\)；(4)与 \(\int|\ell|=2\) 给
\[
 \operatorname{Var}(G_c)
 \le4D+(\log c+2)\|J'\|_\infty
 \le(4\log c+12)RS. \tag{5}
\]
各导数项L¹、端值存在，因此G_c实际属于 \(W^{1,1}(0,1)\)，并绝对连续延到闭区间。这支付了原log端点，而非把singularity略掉。

同样
\[
 \operatorname{Var}(\ell J)\le12RS,\qquad
 \operatorname{Var}J\le4RS, \tag{6}
\]
两者端值均为0。S_exp当然在此域；对N>0有
\[
 \|r\|_{H^1}\le N^{-1/2}
       \bigl(p_{N,0}(r)^2+p_{N,1}(r)^2\bigr)^{1/2}.
\]
这是真strong-source费用。fixed源窗并不把一阶H¹范数降成du／Dlog，不能作该偷换。

## 4. Möbius-grid精确式及q=1

对F定义原
\[
 E_c(F)=\sum_{\substack{1\le a<c\\\gcd(a,c)=1}}F(a/c)
                 -\varphi(c)\int_0^1F,\qquad
 R_q(F)=\sum_{1\le k<q}F(k/q)-q\int_0^1F.
\]
用 \(1_{(a,c)=1}=\sum_{d\mid(a,c)}\mu(d)\) 和
\(\varphi(c)=\sum_{d\mid c}\mu(d)c/d\)，有限重排准确给
\[
 \boxed{E_c(F)=\sum_{d\mid c}\mu(d)R_{c/d}(F).} \tag{7}
\]
这里q=1项恰为 \(R_1(F)=-\int F\)，必须保留；公式不要求先有cofinal收敛。

若F∈W¹,¹且F(1)=0，右端Riemann和给
\[
 R_q(F)=q\sum_{k=1}^q\int_{(k-1)/q}^{k/q}
                  [F(k/q)-F(x)]dx,
\qquad |R_q(F)|\le\operatorname{Var}F. \tag{8}
\]
证明只用区间内积分F′，每个导数点的系数≤1。q=1也成立；若端值未付，就不能无声省去F(1)。

由(5)、(7)、(8)，
\[
 |E_c(G_c)|\le\tau(c)(4\log c+12)RS. \tag{9}
\]
故冻结的整份C_B在全局H¹×H¹上有绝对收敛极限C_∞，且
\[
 |C_\infty(r,s)-C_B(r,s)|
 \le C RS\sum_{c>B}\frac{\tau(c)(1+\log c)}{c^2}
 \le C'RS\,\frac{(1+\log B)^2}{B}. \tag{10}
\]
后一界由
\(\sum_{c\le y}\tau(c)\le y(1+\log y)\)
和分部求和直接得到；所有常数与B、r、s无关。于是这是H¹ sesquilinear form norm收敛，不只逐点形式极限。

供同规则coefficient支持重排所需的更细界也实际付清：
\[
 \sum_{q\ge1}\frac{(1+\log q)|R_q(J)|
                         +|R_q(\ell J)|}{q^2}
 \le\left[4\sum_{q\ge1}\frac{1+\log q}{q^2}
                       +12\zeta(2)\right]RS<\infty. \tag{11}
\]
再乘 \(\sum|\mu(d)|(1+\log d)d^{-2}<\infty\) 仍绝对。因此同一product cutoff dq≤B下，可合法拆 \(\log(dq)=\log d+\log q\)，并显式处理排除dq=1的corner；不许可在尚未付域时先做Dirichlet级数重排。

## 5. 与旧080–096的精确对象／责任区别

本次实际读取080／081／085／089必要定义，082–084、086–088、090–096的原对象、摘要及责任段落定位；不重审整条旧路线proof，不恢复暂停的比例／zero-free优化。

| 旧对象 | 真正相同的设施 | 本规则没有因此取得的结论 |
|---|---|---|
| 080 divisibility incidence \(C_a(n,d)=a(n/d)1_{d\mid n}\)、μ逆矩阵 | 整除fiber／Möbius反演确能在同一个式子连接复合整数；(7)属这一基本设施 | finite acyclic／det1及inverse标签不产生新primitive或Weil号 |
| 081–084 Nyman–Beurling fractional-part features、log-mollifier | 实际source features／Dirichlet反演与完整低除数重排已有 | 新写一个mixed后处理不继承RH距离消失或其未知边界控制 |
| 085 reduced Farey \(h/r\)、\(S_N(r)=\sum_{r\mid n}b_n/n\) | primitive分母分层与coprime sieve已存在；当前(7)也是primitive grid→ordinary grid | 旧h/r是sawtooth的Fourier频率，当前a/c是进入log平移核的实参数，两者不是同一变量。旧Parseval正对角不等于当前J正性 |
| 086–089 mean-zero capacity、local/parabolic/far分块、跨conductor determinant | finite Gram／响应与不同分母collision必须同对象核，不能只看capacity | 当前fixed H¹下绝对可和的grid误差没有支付旧Nyman \(1/\log N\) parabolic leakage；亦未支付当前完整Γ相消 |
| 090–093 determinant方程、cotangent reciprocity、shared-gcd sieve、DFT／短sector | finite gcd／primitive-residue合并、符号与非主mode责任均是旧算术设施 | 当前γ已按log-linear收缩；没有用到旧Kloosterman／Type-I-II新抵消，不能因三腿含素因子就报新prime净方向 |
| 094–096 endpoint Riesz稳定、response leverage与Loewner shortening | 原norm及方向性稳定必须追踪，positive capacity不够 | 本(3)–(11)只是固定test function的端点／BV费用，未给那些cofinal response／leakage预算 |

所以(7)和definition费用属于标准／旧基础重排；当前G_c和J_x是具体的新test function写法，不宜假称逐式等于旧085的某个未付Gram。另一方面，经(7)/(11)消去coprime筛后，系数腿可将算术部分化为经典ζ(2)、ζ′(2)常数乘ordinary-grid泛函；这些grid泛函仍依赖r,s，并非C_∞只由两个常数决定。没有从这个表示推出新经典signed预算。

## 6. 553在极限层的适用范围；552不能被偷用

(10)只付global H¹，不付B统一du／Dlog；旧552的fixed-window高频log增长**不能**仅凭这个H¹上界直接反测cofinal规则。finite层ratio原子也不直接否定D′极限。必须另找实际极限责任。

这里可用的更强旧是553 §2的**H¹**密度：它不只是L²结论。原523的Gaussian／Mellin唯一性给每fixed整数Sobolev的cyclic密度；553明确代入405双moment-zero关系，并给 \(h_c\) 的H³密度经 \(D^2-1/4:H^3\to H^1\) 的链。因此真实physical Pan有限平移span在H¹中稠密，不是本稿从L²密度自行升级。

若把本冻结规则的cofinal极限当作完整经典mixed身份，假设先只在compact smooth两源有
\[
 C_B(r,s)\longrightarrow B_\zeta(r,s),
\]
则(10)给 \(C_\infty=B_\zeta\) 在该域。若先声称对应分布D′趋完整Wζ，compact卷积平方／极化同样给这项compact mixed身份。该身份还可向全S_exp共同compact cutoff延伸：C_∞经H¹连续，完整Bζ按405／568的原S_exp拓扑连续，且χ_Rr→r于两种拓扑。因此在全noncompact Pan与S_exp第二腿上有C_∞(p,s)=0。

固定s后，C_∞第一腿H¹连续，553的真实Pan H¹密度迫C_∞(r,s)=0对全部r∈H¹。特别在537非零compact正窗源上为零，与 \(B_\zeta(r,r)>0\) 矛盾。

所以**若作为完整Weil mixed极限，这份冻结规则已在旧553责任前失败**。论证只要求极限身份，不要求每个finite B杀Pan；没有以spurious ratio atom或未经共同cutoff的noncompact测试否定D′。若从单源平方开始，Hermitian极化先给同一compact mixed身份，结论相同。

这不排本C作为某个其他表达式的一项有界H¹补正；但原规则并未给出那份额外结构、完整Γ／pole身份或独立净费用。不能在失败后自动添背景／改变中心化成为第二候选。

## 7. 可消费结论与分类边界

实际已闭：fixed-B全complex du／Dlog费；H¹端点O(x)、J′ mixed费、G_c的AC／BV；含q=1的exact Möbius-grid；固定H¹及S_exp强域的cofinal绝对收敛与(10)/(11)；原Farey的对象区别及limit层553门。

这些是对同一已给公式的definition／标准整除与已付密度去重，没有新增primitive、独立positiveD′规则或完整净signed/corecross箭头。建议按构造前置0消费本规则，不建数学合同，不改参数、另造theta／PSD或顺读paper。具体coefficient符号／finite atom方向由另一独占支持核；本稿不替该分支领新结果。

完整Γ／FP-contact、proper powers、双pole、原physical norm与fixed／成长量词保持；没有全Farey／非局部／强费用方法类no-go，whole4/5UPPER与长期Goal门未变。
