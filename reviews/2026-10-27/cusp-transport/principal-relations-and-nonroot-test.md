# 完成化模源的实际405关系、537非根与constant-weight门

2026-10-27；C046独占分支原稿，待root消费。仅研究已给出的
\(F_r=L_r(j)\)，不重做essential-cusp／有限维Baire门，也不据本稿结算轮数。

本稿的具体新比较是：对405的真实noncompact Pan及其全部平移，constant项有实际积分公式，且正向大平移上有严格非零／指数增长下界。这一项在每个Faber截断中原样保留。扣除constant则是合法解析修复，但全部负系数仍注入地保留Pan和537，不能据此声称已得正确principal商；native divisor／Green类的消费另见同目录产品分支。

## 1. 固定对象、原范数与已经支付的前件

源固定为physical \(r(u)=e^{u/2}f(u)\)，允许ALLcomplex

\[
 \mathcal S_{\exp}=\{r\in C^\infty(\mathbb R;\mathbb C):
 p_{N,k}(r)=\sup_u e^{N|u|}|r^{(k)}(u)|<\infty\quad\forall N,k\}.
\]

\(L_r(z)=\int r(u)e^{zu}du\)是整函数，\(F_r(\tau)=L_r(j(\tau))\)在H内全纯且weight0模不变。此处的完成化解析源一般不是原Borcherds有限整主部输入；有限原输入先对整数基使用原定理，然后只在divisor／Green数据上复化，不把任意complex系数说成整输入。

原du范数是\(\|r\|_2\)。原zero-extension logarithmic图范数可用553的

\[
 \|r\|_{H\log}^2={1\over2\pi}\int_{\mathbb R}
 [1+\log(2+|t|)]|\widehat r(t)|^2dt
\]

表达；它与原\(D_{\log}\)图范数等价，且全线平移不改变该范数。下文fixed源窗的du上费也由该图范数支付；全线\(\mathcal S_{\exp}\)费另列，不能把二者合并为全源统一原费。

本稿消费的旧结论仅为：405／579的实际

\[
 H=e^{u/2}h>0,\qquad H\in\mathcal S_{\exp},\qquad
 p=(D^2-\tfrac14)H\ne0,
 \qquad B_\zeta(\tau_bp,s)=0\quad
 (b\in\mathbb R,s\in\mathcal S_{\exp}),                 \tag{1}
\]

其中\(\tau_br(u)=r(u-b)\)。全部平移都是physical真实关系的合法非零缩放，不能裁去其noncompact尾。这里physical算子是\(D^2-1/4\)，不是未中心化坐标的\(D^2+D\)。537给固定\(I=(-17/16,17/16)\)内ALLcomplex源

\[
 Q_\zeta(r)\ge2^{-49162}\|r\|_2^2\quad(r\in C_c^\infty(I;\mathbb C)). \tag{2}
\]

完整经典目标始终含actual \(\Gamma=2\theta'\)／FP-contact、全部proper powers与两个pole；本稿没有用模形式系数\(m\)替代经典\(p^k\)，也没有从native正能量推导(2)。

## 2. constant核、合法换序及实际费用

在任一固定\(0<\rho<1\)的q圈上定义

\[
 K_n(u)={1\over2\pi i}\int_{|q|=\rho}
       e^{u j(q)}q^{-n-1}dq,\qquad
 a_n(r)=\int_{\mathbb R}r(u)K_n(u)du.                 \tag{3}
\]

令\(C_\rho=\max_{|q|=\rho}|j(q)|\)。固定q圈有

\[
 |K_n^{(k)}(u)|\le\rho^{-n}C_\rho^k e^{C_\rho|u|}.    \tag{4}
\]

因此\(N>C_\rho\)时，绝对换序和u微分均由

\[
 |a_n(r)|\le {2\rho^{-n}\over N-C_\rho}p_{N,0}(r)     \tag{5}
\]

支付。任意fixed \(\operatorname{supp}r\subset[-L,L]\)另有真正原du费用

\[
 |a_n(r)|\le\|K_n\|_{L^2(-L,L)}\|r\|_2
 \le\rho^{-n}\sqrt{2L}\,e^{C_\rho L}\|r\|_2.          \tag{6}
\]

第一项是该fixed窗线性泛函的精确du范数，第二项只是方便上界；不能从第二项声称必要高度增长。原\(D_{\log}\)图范数通过其du嵌入支付(6)。各个\(\rho,L,n\)、几何compact和算术height仍是不同参数。

本稿只需\(A(u)=K_0(u)=\operatorname{CT}_q e^{u j(q)}\)，以及

\[
 V(u)=A''(u)-\tfrac14 A(u),\qquad
 |V(u)|\le(C_\rho^2+\tfrac14)e^{C_\rho|u|}.           \tag{7}
\]

\(A,V\)均为实整函数。这些核通常指数增长；553的全线du／Hlog中Pan平移稠密结论**不能**直接用于它们。本稿改用(4)–(7)及下面的实际正尾证明。

## 3. q系数正性给一个确定符号

使用\(q=e^{2\pi i\tau}\)的经典归一化

\[
 j={E_4^3\over\Delta}
   =q^{-1}+744+\sum_{n\ge1}c_nq^n,
 \quad E_4=1+240\sum_{n\ge1}\sigma_3(n)q^n,
 \quad\Delta=q\prod_{n\ge1}(1-q^n)^{24}.              \tag{8}
\]

这些绝对收敛的q恒等式直接给\(c_n\ge0\)：\(E_4^3\)与\(q/\Delta=\prod(1-q^n)^{-24}\)的系数均非负，constant由720+24=744得出。这里只使用该代数事实，不使用模系数渐近或RH。标准归一化及Faber基可另核[Duke–Jenkins作者课程稿](https://www.math.ucla.edu/~wdduke/preprints/notes_Bristol.pdf)，印刷pp.2–3；该出处不承担本稿下列新不等式。

记\(J=j-744\)、\(B(u)=\operatorname{CT}e^{uJ}\)，则
\(A=e^{744u}B\)。每个\(\operatorname{CT}J^k\)非负；在固定q圈用\(|\operatorname{CT}J^k|\le\max|J|^k\)可合法逐项微分其整u级数。因此对全部\(u\ge0\)，

\[
 B(u)\ge1,\quad B'(u),B''(u)\ge0,\qquad
 \boxed{V(u)\ge(744^2-\tfrac14)e^{744u}>0.}            \tag{9}
\]

在\(u<0\)没有免费采用该符号，下一步显式支付此区域的尾。

## 4. 405的实际constant／weight反测及全平移量词

对每个固定\(b\in\mathbb R\)，(1)、(7)允许两次分部积分：H及其导数的任意指数衰减令所有边界为零。所以

\[
 \boxed{a_0(\tau_bp)=\int H(v)V(v+b)dv.}              \tag{10}
\]

这是所有真实平移的同一个公式；不是假定某个未知principal map。取\(b\ge0\)，在\(v\ge-b\)用(9)，其中\(v\in[0,1]\)的贡献至少

\[
 c_H e^{744b},\qquad
 c_H=(744^2-\tfrac14)\int_0^1H(v)e^{744v}dv>0.         \tag{11}
\]

唯一可能负贡献在\(v<-b\)。固定任意\(N>C_\rho\)，用
\(H(v)\le p_{N,0}(H)e^{Nv}\)得

\[
 \begin{aligned}
 \int_{v<-b}H(v)|V(v+b)|dv
 &\le (C_\rho^2+\tfrac14)p_{N,0}(H)e^{-C_\rho b}
          \int_{-\infty}^{-b}e^{(N-C_\rho)v}dv\\
 &= {(C_\rho^2+\tfrac14)p_{N,0}(H)\over N-C_\rho}
       e^{-Nb}=:C_{N,\rho,H}e^{-Nb}.                  \tag{12}
 \end{aligned}
\]

于是严格有

\[
 \boxed{a_0(\tau_bp)\ge c_He^{744b}
             -C_{N,\rho,H}e^{-Nb}>0
       \quad\hbox{对全部充分大的 }b.}                \tag{13}
\]

这里先固定\(\rho,N,H\)再让b增长；阈值不依Faber截断阶数。不要求\(a_0\)对每个负b也非零；(10)是全b公式，(13)已严格否定“消去全部真实Pan平移”的责任。

还有一项实际必要费用：\(\|\tau_bp\|_2\)与全线\(H\log/D_{\log}\)图范数均不随b变，而(13)发散。因此这个constant读出没有全线统一原du或上述平移不变图范数界。这项必要性来自实际Pan源下界，**不是**把(6)的粗上界反向使用。它也不妨碍(5)的强源连续性或每fixed窗(6)。

令\(J_m=q^{-m}+O(q)\)为constant0的整数Faber模函数，有限模截断是

\[
 F_{r,N}=a_0(r)+\sum_{m=1}^{N}a_{-m}(r)J_m.           \tag{14}
\]

这不是直接截断Laurent多项式。每个(14)的constant仍恰是\(a_0(r)\)。因此(13)的非零constant在任意N中保留，不能被“更长principalpart尾”治愈。对原Borcherds有限输入，section权为\(a_0/2\)；complex源只对该权数据复线性延拓。这里确切排除的是忽略该权／character／cusp，直接把每个输出当作weight0的全局principal**函数**的recipe。

非零weight本身不是任意开模型上一切divisor类非principal的定理。必须保实际automorphy line、compactification与character；不能省掉这些再声称已核几何商。

## 5. 同一个537奇非根有实际非零constant读出

在原537窗内取足够小的\(\varepsilon>0\)，选非零、非负、偶
\(\phi\in C_c^\infty((-\varepsilon,\varepsilon))\)，并令

\[
 \psi(u)=u\phi(u),\qquad r_*=(D^2-\tfrac14)\psi.       \tag{15}
\]

它是非零实奇compact源；\(\mu_\pm(r_*)=\int r_*e^{\pm u/2}=0\)由分部积分精确成立。非零性来自非零compact函数不能解\(P\psi=0\)。这是579／582同一类显式奇源，此处只把其支撑取小来核新的constant核；未按Q或零点选择源。

由(8)，

\[
 V'(0)=\operatorname{CT}j^3-\tfrac14\operatorname{CT}j
 =744^3+6\cdot744c_1+3c_2-186>0.                       \tag{16}
\]

故存在固定\(\varepsilon<1\)使\(V(u)-V(-u)>0\)对\(0<u<\varepsilon\)。用(15)两次分部积分，

\[
 \boxed{a_0(r_*)=\int_0^\varepsilon
       u\phi(u)[V(u)-V(-u)]du>0,\qquad
 Q_\zeta(r_*)\ge2^{-49162}\|r_*\|_2^2>0.}            \tag{17}
\]

所以该constant通道读到了这个实际非根，与579的sech单通道奇源漏失不同；但它同时读到了(13)的真实关系，仍不是正确关系商。

任意fixed有限N只保留有限个\(a_0,a_{-1},\ldots,a_{-N}\)。按580的旧finite-rank bump机制，在I内取N+2个不交非零bumps\(\psi_j\)，解这N+1个实际泛函在\(P\psi_j\)上的齐次系统，得非零compact双polezero源全部读数为零，而(2)仍严格正。这里给出实际矩阵\(\int\psi_jPK_n\)，不再把finite-rank重述计作新增结果；加入其他有限个读数只需相应增加bumps。

## 6. 扣constant／ratio的合法修复与准确剩余

解析层可以直接定义

\[
 \widetilde F_r=F_r-a_0(r),\qquad
 \widetilde F_{r,N}=\sum_{m=1}^N a_{-m}(r)J_m.         \tag{18}
\]

该修复精确消除constant及其weight数据，费用为(5)／(6)。有限整数输入上，可在权与character匹配时用原乘积作ratio；任意complex系数下首先是divisor／Green pair的加减，不免费选出全局单值复幂。weight0也仍须检查character。

这一扣除**不把全部源在解析层吞掉**。事实上

\[
 \boxed{r\longmapsto(a_{-1}(r),a_{-2}(r),\ldots)
        \quad\hbox{在全部}\ \mathcal S_{\exp}\ \hbox{上注入}.} \tag{19}
\]

证明：若负系数全零，则\(F_r-a_0(r)\)在唯一cusp的Laurent负部为零，因而延成compact模曲线\(X(1)\)上的全纯函数。它只能是常数，其constant0又迫它为零。于是\(L_r\circ j\)恒常；j非恒定且为开映射，整函数唯一性给\(L_r\)恒常。沿虚轴\(L_r(it)\)是Schwartz源的Fourier变换，趋零，故该常数为零，再由Fourier唯一性给r=0。

因此balanced完成化解析map保留每个非零Pan、上述537源及全部其他非零源。它的全源信息恢复不等于关系下降；finiteN的盲源与全family的注入也不可混为一谈。

若native整数基的divisor／Green pair本来是principal，则每个有限balanced输入在相应native principal类中为零；这与(19)完全相容，丢失发生在**后续类读出**。无限Green/current尾及所选relative quotient是否允许取极限，必须逐项支付；不能以解析注入保证native primitive非零，也不能仅凭各有限principal就未经闭包证明宣布所有完成化类为零。该native闭合责任交同目录实际产品／Green分支和root审查，不在本稿预设。

## 7. 强旧比较、净范围与停止条件

| 已有最强输入 | 本稿消费方式／未升级的范围 |
|---|---|
| 552的完整actualGamma高频机制 | 未改善；模constant读出不等于\(Q_\zeta\)的Hermitian身份，fixed窗上费不是成长whole下界。 |
| 553全Pan平移在du／Hlog稠密 | 未用于指数增长核；(10)–(13)另以强源尾与正q系数给实际关系反测。若未来读出全线bounded且消Pan，553旧全零门仍适用。 |
| 579实际Pan与sech、奇537漏失 | 真实源本身是旧输入；新项限于j-completion的constant核、非零weight及实际必要平移费用。 |
| 580有限通道与无限塔门 | fixedN盲源是旧finite-rank机制；(19)表明这里完整负系数family不同于有限通道，不能用旧单格盲源直接代替。 |
| 582full-local／实际Green、Pan失败与537恢复 | 不重复其源设施；本稿核另一个已给出的模源，仍未得到同对象primitive容量／mixedRR。 |

本稿新增的严格范围为(3)–(7)的该核费用、(10)–(13)的真实关系／必要费用反测、(17)的同类非根具体读出，以及(18)–(19)所界定的合法balanced信息修复。这些不再只是“essential奇性不是honest输入”的标准资格门。原du固定窗、强源、全线不统一与全family注入的量词均已分开。

下游必须保留：actual\(\Gamma\)/contact、properpowers／双pole、全部complex源与noncompact Pan；q-coefficient方向没有被识别为经典signed预算；没有独立primitive/Hodge-RR容量、成长core／coupling／\(\Xi\)或经典正性新结论。strongest-old542+555→557 whole leading4/5仍只是负惯性UPPER，未改善。

这一结果只否定忽略constant的raw principal-function recipe，并保留有费用的balanced完成化／真实relative cocycle／不同非零primitive载体。若实际native balanced类及其闭合把Pan和537一并杀掉，当前recipe到此止；不能继续只增N、改j的仿射constant或把未知relative读出改名。是否取得新整体闭合与本轮计数由root按三个分支实际结果统一判断。
