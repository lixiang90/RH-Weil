# 原 unit 主频带：完整 major arcs 的联合乘法大筛付款

2026-10-08，whole_mixed4。基线 main 6149e0a。
只新增本研究源，不修改既有源、笔记、输出、检查器或 Git。

本稿取得一个新的实际联合上界：原主频带中 n/q 接近全部小分母有理数的
major arcs，在全部 q、s、真实 p、r、共同 u 与所有 aspect ratios 上，
费用为 O(D³X^(1/2)log^C X)。它使用整 q 族的 primitive-character 大筛，
不是逐 q 的矩形算子范数。取 D=X^δ、0<δ<1/14，这个完整频率块的
指数严格小于5/7。

完整 minor arcs 仍未付。因此没有新的 canonical whole 四矩界、常数级
signed 预算、简单零点比例、kappa 或无零边界。以下给完整付款和精确剩余。

## 1. 冻结合同与原实际对象

全文读取并保持
[unit425源](hybrid-whole-fourth-unit-unit-actual-research-whole.md)，canonical LF SHA256
`b3f14cf4ee5659f8e23bd51dc9bf71e853e783bd2d55e42ee8846d6e8d1e41dc`，
及[root全文独审](hybrid-whole-fourth-unit-unit-actual-review-root.md)。
当前 RESEARCH_BRANCHES 队列的未付项正是该源(36)的 nu 主项。
原 chirp、graph、整数 aliases 和边界不在本稿重新认领。

仍取 X=T/(2π)、L=log X、b_p=log p/(a_L L√p)，a_L≥cφ>0，
所有 genuine primes 在 √X<p≤X。q 为实际最大素数，√X<s<q。
对最大标签在分子的两个位置，A_p、B_r 精确取冻结源(4)、(5)，
包括 p,r<q、p,r≠s、全部原 phi 因子和共同 u。
另两个位置交换两对后取共轭。

保留同一 nu、d floor、theta_-、theta_+，尤其
nu≥0、∫nu=1、supp nu⊂[theta_-,theta_+]、||nu||∞≪χX^-1。
不改变原空间 C² profile，也不扩大观察窗。

记冻结源 interior 为 C_int，满足 qs>4X、q−s>4q delta。
以 e_c(z)=exp(2πiz/c) 写第一位置的原主项

\[
 \mathfrak L_U=\frac1L\int_{I_+}\phi(u)^2
 \sum_{(q,s)\in\mathcal C_{\rm int}}b_qb_s\frac{2\pi s}{q}
 \sum_{\substack{n\in\mathcal I_{q,s}\\q\nmid n}}
 \nu(2\pi sn/q)e_q(ns)\mathcal B_n(q,s,u)\,du,
\tag{1}
\]

\[
 \mathcal B_n=\sum_{p,r}A_pB_r e_{q^2}(-npr),\qquad
 n\asymp qX/s,\quad0<n<q^2.
\tag{2}
\]

整个原 physical remainder 还带冻结源已付的 O(X^(1/2)L^C)等误差。
本稿只改进(1)的一个完整频率块，不将它当成 canonical J_T 的子块。

## 2. 加回完整 nn 后，真实产品可局部化

先给(1)加回全部 n=q m 的 nu 主项，记所得完整 n 主项为 L_F。
这是整块加回；不从已付 signed nn 总量推出任意频率子集。
在原 interior，1≤m<q且q为素数。模q Fourier 矩形的范数为√q，
原 ||A||2、||B||2≪φ1，故 |B_qm|≪φ√q。
全部 m 个数 O(X/s)，nu 的 sup 为 O(X^-1)，所以每(q,s,u)
的 n=q m 主项为 O(q^-1/2)。原外权完整求和给

\[
 \mathfrak L_F-\mathfrak L_U=O_\phi(X^{1/2}L^C).
\tag{3}
\]

这里仅明确新的频率分解如何消费已经付款的完整块。

固定辅助 g∈C_c∞((1/2,2))，0≤g≤1，且 g=1于[3/4,5/4]。
在 L_F 中把 B_n 换为

\[
 \mathcal B_n^g=\sum_{p,r}A_pB_r g(pr/(qs))e_{q^2}(-npr).
\tag{4}
\]

这一步在完整 n 求和以后才有 tiny 误差，不能逐 n 声称等价。
Poisson/inversion恢复的真实核为
K0((qs−pr)/(qs))=∫exp(i theta(qs−pr)/(qs))nu(theta)dtheta。
若 g≠1，真实 |(qs−pr)/(qs)|≥1/4，原 chi 的 stretched Fourier
尾给任意固定省幂。其额外 modq² aliases 在原 carry interior 仍由
冻结源整 lattice 尾支付。原四权质量至多 O(X²L^C)，故

\[
 \mathfrak L_F=\mathfrak L_F^g+O_\phi(X^{-2}L^C).
\tag{5}
\]

在(4)中分 p∼P、r∼R、q∼Q、s∼S的全部 dyadic boxes。
四条 dyadic grids均从√X开始，最后一箱按X截断，故P,R,Q,S≥√X。
有 √X≲S≤2Q≤2X，P,R≲Q，且非零 boxes满足 PR≍QS。
全部 sharp endpoints仍留在各和中；只为上界添加这个辅助产品窗。
产品系数长度 O(PR)=O(QS)=O(Q²)，是下述大筛的实际长度。

## 3. 低产品全族与 major/minor 的准确分割

令 1≤D≤X^(1/10)，大X时D<q。
先按 dyadic Q,S 分区：QS≤64DX 的整个 boxes列为低产品族，
其实际 qs≤256DX。此族不再作 n 的任意子集分割。

完整 n 逆变换后，宽 near |h|≲qs delta 内每个(q,s)只有
O(qs delta+1)个整数产品 a=pr，每个 a 有至多tau(a)个真实 factor pairs。
四权至多 Cφ/(qs)，全部 phi 因子和原同-u prefactor至多常数。
放大 q,s 到整数并求和，

\[
 \sum_{q,s>\sqrt X,\ qs\le256DX}1\ll DX\log(2D),
 \qquad\sum_{q,s>\sqrt X,\ qs\le256DX}\frac1{qs}\ll\log^2(2D).
\]

tau(a)≪εX^ε且 delta≪X^-1L^C，所以整个低产品 raw 主项为

\[
 O_{\phi,\varepsilon}(DX^\varepsilon L^C).
\tag{6}
\]

宽 near 外还是完整 chi Fourier 尾。此付款保留真实产品等式，
没有把任意 n 子集的绝对和说成低产品付款。

以后固定一个 QS>64DX 的 box。称 n 是 major，若存在

\[
 1\le d\le D,\quad0\le a<d,\quad(a,d)=1,\quad m\in\mathbb Z,
 \left|\frac nq-m-\frac ad\right|\le\frac D{dS}.
\tag{7}
\]

包括 d=1,a=0。重叠时按任意固定顺序选一个表示；上界允许全 packet
正计数，因此无需用不相交性制造节省。minor 是真实频带中的其余 n。
全部 q整除n都属于 d=1 的 major。

设 c=dm+a、beta=n−cq/d。正频带给 n/q≤3X/S，大X时 D≤X，
所以 1≤c≤4dX/S<q/16；因此 q不整除c。
每个 q、d、a 的 m只有 O(M)种，M=X/S≥1；对固定 m，整数 n只有

\[
 K_d\ll QD/(dS)+1
\tag{8}
\]

种。实际 s∈(S,2S]和 n 的 nu support仍由原求和保留，
这里只为 absolute 上界作保守外包围。

## 4. Major phase的CRT与原profile的共同Mellin包络

准确有

\[
 e_{q^2}(-npr)=e_{dq}(-cpr)e(-beta pr/q^2),
\]

\[
 e_{dq}(-cpr)=e_q(-c\bar d\,pr)e_d(-c\bar q\,pr),
\tag{9}
\]

其中逆元分别模q、模d。d=1时第二因子为1。
两腿按真实 p≡i、r≡j(mod d)分开，第二因子就是单位模长常数。
第一个因子的频率 b=c bar d(mod q)非零。
固定 q、d、a时，m↦b是平移 m↦m+a bar d；m范围长 O(X/S)<q，
可注入模q非零频率。正是这个完整 m族可进入有限 Parseval。

另有 |beta|≤qD/(dS)。设 t=log(pr/(qs))和 z=beta s/q，则
|z|≤2D/d，而产品窗和 chirp 合为

\[
 H_z(t)=g(e^t)e(-ze^t),\qquad
 |\widehat H_z(\tau)|\le C\min\{1,(1+2D/d)^2/(1+|\tau|)^2\}=:W_d(\tau),
\]

\[
 \int W_d(\tau)d\tau\ll1+D/d.
\tag{10}
\]

证明只用 H_z 的固定紧支撑、L1界与二导数 O((1+|z|)²)。
这个共同包络对所有 q,s,n、beta有效，不使用 exp(D) 的 Taylor 费用。
Mellin inversion将 H_z 分解为 p^(iτ)r^(iτ)(qs)^(-iτ)。
beta和s只进入被(10)统一包围的系数。

原 phi、phi²在对数变量上C²、紧支撑长 O(L)，
其 Fourier绝对积分为 Oφ(L^C)：由 L1、二导数L1界分别控制小/大频率。
每个共同-u、q/s平移只乘 Fourier系数以单位模长的相位。
因而冻结源(4)、(5)的全部交叉profile可用同一 Oφ(L^C)包络分离；
没有求导升级原phi，也没有把s或u换成独立坐标。

在每个固定 Mellin/Fourier参数上，实际基本腿仍是
α_p=b_p p^(it1)、β_r=b_r r^(it2)，真实prime dyadic support，
加 q 的严格prefix与mod d残类。所有参数模长不改变 L2能量。

## 5. 整q、m族的非主角色能量

唯一新增的标准解析工具是
[Kedlaya作者讲义，Theorem18.2](https://kskedlaya.org/ant/chapter-18.html)：
对长度N的固定系数，primitive multiplicative large sieve 的费用为
Q²+N。以下并不假设所有模数上的素数分布。

先固定两腿残类 i,j、twists及prefix，记

\[
 C_t=\sum_{pr\equiv t\ (q)}\alpha_p\beta_r,
 \quad B_b=\sum_tC_te_q(-bt),\quad M_0=\sum_tC_t.
\]

真实 p,r<q都为模q单位。有限加性/乘法 Parseval准确给

\[
 \sum_{b=1}^{q-1}\left|B_b+\frac{M_0}{q-1}\right|^2
 =\frac q{q-1}\sum_{\chi\ne\chi_0\ (q)}
 \left|\sum_p\alpha_p\chi(p)\right|^2
 \left|\sum_r\beta_r\chi(r)\right|^2.
\tag{11}
\]

证明：减去群上的平均 M0/(q−1)，加性 b=0系数为0；
全q加性Parseval给q倍残类方差。
再对(q−1)元乘法群Parseval，乘法卷积的变换是两腿角色和的积。
主角色在每个 b≠0的加性值为−M0/(q−1)，所以符号和归一化如(11)。

q为素数，因此(11)中所有非主角色确为primitive。
两腿积合成真实整数产品系数 c_k=Σpr=k α_pβ_r，长度 O(PR)≤CQ²。
genuine-prime factorization使每个k只有至多两个有序prime pairs，故

\[
 \sum_k|c_k|^2\le2\sum_p|\alpha_p|^2\sum_r|\beta_r|^2\ll_\phi1.
\tag{12}
\]

twists、残类和任意固定区间均不增加这个上界。
把(11)全部q∼Q的非主角色送入primitive大筛，费用因此为 Oφ(Q²L^C)。
主角色另有全部 q、b的费用
Σq |M0|²/q≪Σq PR/q≪Q²L^C，不能免费删掉。

q相关sharp prefix不能直接当作固定大筛系数。
对每条腿用dyadic binary intervals表示所有prefix：每个prefix最多O(L)块，
两腿乘积后Cauchy付O(L²)。随后对全部区间对用同一大筛。
每个原prime坐标在每层最多一次，故所有区间对的(12)能量和仅再付O(L²)。
因此maximal两腿prefix也只损失log^C，保留严格p,r<q。

最后必须保留 p,r≠s。若p=s，单点改变量的absolute至多
Cφ√R/√S，且只有P≈S的box才出现；r=s同理，双单点项为Oφ(1/S)。
在全部q,m上，前两项的平方能量至多

\[
 O(Q\cdot(X/S)\cdot R/S)\ll Q^2,
\tag{13}
\]

因为S²≥X、R≲Q。另一个腿同理，双单点更小。
这直接控制所有s的sup单点改变量；没有从全角色signed范数推出任意子集范数。
原profile经共同包络分离后仍满足同一L1腿界。

按mod d两腿分残类，d²项的Cauchy付d²。
所有残类的(12)能量和至多原全产品能量，主角色亦可正控制。
加上(10)的共同Mellin包络，得到一个对全部s与packet n有效的非负包络
F_qm^(d,a)，满足

\[
 |\mathcal B_n^g(q,s,u)|\le F_{q,m}^{(d,a)}(u),\qquad
 \sum_{q\sim Q}\sum_m|F_{q,m}^{(d,a)}(u)|^2
 \ll_\phi(d+D)^2Q^2L^C.
\tag{14}
\]

这里m只走(7)的完整范围；q prime、q最大性、共同u和真实权没有被换走。
(14)是整q族能量，而不是每个q都有O(q)的未证分布结论。

## 6. 全部外权与频率packet的完整费用

有 Σq∼Q b_q²≪φ1、Σs∼S b_s≪φ√S，且
(2πs/q)nu(2πsn/q)≪χ S/(QX)。
对固定d,a，保留全部实际n后用(8)、(14)和q,m Cauchy：

\[
 \sum_qb_q\sum_mF_{q,m}^{(d,a)}
 \le\left(M\sum_qb_q^2\right)^{1/2}
      \left(\sum_{q,m}F_{q,m}^2\right)^{1/2}
 \ll_\phi(d+D)Q\sqrt{X/S}\,L^C.
\]

因此这个(d,a)的实际box费用至多

\[
 \sqrt S\frac S{QX}K_d\,(d+D)Q\sqrt{X/S}\,L^C
 \ll_\phi(d+D)\left(\frac{QD}{d\sqrt X}+\frac S{\sqrt X}\right)L^C.
\tag{15}
\]

所有外权和nu均来自原(1)。未扔掉实际 q/s∼任意幂的aspects，
未以单a、单m或逐sigma付款替代whole union。
e_q(ns)仅在这份major上界中取absolute；节省来自共同q大筛。

对每个d有至多d种a，故由(15)

\[
 |\mathfrak L_{F,\rm major}^{g}(Q,S,P,R)|
 \ll_\phi\frac{D^3(Q+S)}{\sqrt X}L^C.
\tag{16}
\]

恢复全部dyadic Q,S,P,R、原两种分子最大位置和另两种共轭位置。
同-u prefactor L^-1∫I+phi(u)²du≤1/2，且Q≤X、S≲Q，
全部几何求和与box数只损失log^C。于是

\[
 \boxed{|\mathfrak L_{F,\rm major}^{g}|\ll_\phi D^3X^{1/2}L^C.}
\tag{17}
\]

这不是只筛一条稀疏prime腿：它覆盖原全部genuine-prime腿、最大标签位置、
所有产品aspects、sharp endpoints及同-u union中的整个定义(7)频率族。

## 7. 新的完整剩余与未付输入

令 I_D为QS>64DX的所有boxes，在(4)中只保留(7)的complement，
nu、两种原profile及所有conjugate位置均保持。
minor不含q整除n，因为那些频率已全部位于d=1 major。
由(3)、(5)、(6)、(17)，原unit主项准确缩约为

\[
 \boxed{\mathfrak L_U=\mathfrak I_D+
 O_\phi(D^3X^{1/2}L^C)+O_{\phi,\varepsilon}(DX^\varepsilon L^C).}
\tag{18}
\]

这里从完整raw频带加回nn，再消费完整nn付款，
不能把(18)的误差说成对任意n/q子集都成立的nn范数。
冻结源的全部chirp/graph/边界付款可合入同一O(X^(1/2)L^C)。

取D=X^δ、0<δ<1/14，1/2+3δ<5/7。
例如δ=1/100给已付完整major块指数53/100。
这只是严格指数比较；完整I_D尚未上界为小于5/7，更未证明常数级预算。

剩余mechanism比原点态矩形问题具体：在major，n/q²的phase经有界chirp
变成模q的非零加性频率，完整q族只需要prime-product长度PR≤Q²的
primitive-character大筛。minor保留真正模q²的unit lift oscillation；
其角色具有conductorq²，不能继续用同一Q²费用。
对真实raw products作单q完整q² Parseval，只给q²乘产品能量，
整q族为O(Q³L^C)，没有(14)的Q²联合节省。
这指出缺的是实际unit-lift restricted-band能量或与真实s prime Fourier的
联合抵消，而不是又一次pointwise sqrtq主张。

一个明确的下一能量目标，在共同Mellin参数与sharp q-prefix下，是
对PR≈QS的真实prime-product和G_qn，证明全部minor n≈qX/S的

\[
 \sum_{q\sim Q}\sum_{n\ \rm minor}|G_{q,n}|^2
 \ll_\varepsilon Q^2(X/S)X^\varepsilon.
\tag{19}
\]

这里在每个固定Mellin参数上可明确取
G_qn=Σp,r b_p b_r p^(it1)r^(it2)e_q²(−npr)，两腿仍在其真实dyadic
prime supports并满足p,r<q；产品g和原phi由上述共同包络分离。
与之配对的可分离s腿为
F_qn=Σs∼S,s<q b_s(s/S)s^(it3)e_q(ns)。
将Xnu(2πXy)对y=sn/(qX)作Mellin分离，只付log^C，
因为其固定相对支撑与原nu二导数界给同样的L1 Fourier包络。
自然完整Parseval为Q³；(19)需要节省QS/X这一真实resolution因子。
在可分离的两腿部分，真实s additive Fourier的完整period Parseval给
Σq b_q²Σn|F_qn|²≪QX/S·L^C，(19)会给O(√QX^ε)的joint bound。
要消费为整个minor证明，还须同时保留原排除s的单点项和共同profile的
完整分离/求和；本文没有声称(19)成立或这些minor前件已付。
即使只争取小于5/7，平衡Q=S=X处也需要这种能量比Q³有真省幂。

本稿没有用外部素数AP分布、短区间下界或有限采样支付这些前件。
所得(17)是新真实联合付款，(18)是新实际缩约；完整short-carrier signed
预算仍由I_D决定。以后还需消费原whole桥及共同good-set概率分母，
不得从此频率块付款宣布canonical whole四矩、条带或比例改进。

## 8. 有限归一化检查的范围

自写标准库复数求和只读运行，在q=5,7,11,13,17核对(11)的Gauss能量
归一化及(9)的CRT符号，最大浮点差2.9068×10^-12。
该检查使用真实小prime腿和任意复杂权，未执行外部pipeline、未写文件。
它只检验有限恒等式，不认证primitive大筛、profile包络或任何ζ渐近界。
