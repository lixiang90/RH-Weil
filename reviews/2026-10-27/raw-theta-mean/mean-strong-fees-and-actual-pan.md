# 同raw K_g的空间均值：强源费用、精确旧分解与actual Pan渐近

2026-10-28；/root/rm_source独占稿，执行2026-10-27保存的STATE唯一[rawmean/joint首门](../corrected-theta-source/next-raw-mean-joint-source-admission.md)。同G20261027／原0c4f基线，C047预算已耗；不改STATE/cadence/Git，不预C048/585，不调核／模型／ray／weight／阻尼或续paper。出稿不代root消费。本稿付款mean／原域与actual Pan系数；完整联合闭包由独立稿/root另消费。

## 1. 同一实际raw核、两端与精确Mellin分解

沿已root/fresh闭合的项目独立R_g/K_g版本，固定原B/L/M及positive体积测度μ。原literal R/K失域及整体Theta／7.4运输冻结保持。记

\[
 \alpha=\frac34,\qquad
 c=\operatorname{covol}_{B}(L)>0,\qquad
 V_\mu=\int_Md\mu,
\]
\[
 m(t)=e^{\alpha t}V_\mu^{-1}
          \int_M K_g(i e^t,z)d\mu(z),
 \qquad \ell_0(r)=\int_{\mathbb R}r(t)m(t)dt.
 \tag{1}
\]

c是实际B-selfdual测度的格covol，不是空间体积V_μ，亦不设为1。前轮[Poisson原稿](../corrected-theta-source/polynomial-gaussian-poisson-and-zero-modes.md)的(8)/(9)对全空间及全部固定log-v导数成立；取均值并乘e^(αt)给某些fixed模型常数a_±>0：

\[
 \begin{aligned}
 m(t)&=-e^{\alpha t}
       +O\bigl(e^{\alpha t}e^{-a_+e^t}\bigr),&&t\to+\infty,\\
 m(t)&=c^{-1}e^{-\alpha t}
       +O\bigl(e^{-\alpha t}e^{-a_-e^{-t}}\bigr),&&t\to-\infty.
 \end{aligned}
 \tag{2}
\]

每个固定阶t导数也有对应估计，常数依阶数。这里实际大端系数是−1，小端系数是+c^−1；没有将Poisson的负号丢掉，也没有将α改成经典pole的1/2。

关键是先扣一个比“mean无du费用”更强的**精确旧分解**。定义

\[
 \nu(t):=m(t)+e^{\alpha t}-c^{-1}e^{-\alpha t}.
 \tag{3}
\]

由(2)，正端剩−c^−1e^(−αt)加双指数尾，负端剩+e^(αt)加双指数尾；中央compact区间smooth。因此ν及其每个固定阶导数都以O(e^(−α|t|))衰减，特别ν∈L²(R)。这不是把ν冒称为全部指数权的S_exp核。

若M_s(r)=∫e^(st)r(t)dt，则对全部complex r∈F=S_exp有精确等式

\[
 \boxed{\ell_0(r)=-M_\alpha(r)+c^{-1}M_{-\alpha}(r)
                   +B_\nu(r)},\qquad
 B_\nu(r)=\int r(t)\nu(t)dt,
 \quad |B_\nu(r)|\le\|\nu\|_2\|r\|_{du}.
 \tag{4}
\]

所以新增mean腿只是两个固定Mellin矩加一个原du有界读出；不能只因整个ℓ0不延拓为L²泛函便报新独立算术输入或新的whole后果。

## 2. ALLcomplex强源定义、完整raw源及原范数范围

由(2)，|m(t)|≤C e^(α|t|)，故(1)在全部F上绝对收敛并按r复线性。对原强半范数p_(N,0)(r)=sup_t e^(N|t|)|r(t)|，任何N>α都有

\[
 |\ell_0(r)|\le\frac{2C}{N-\alpha}p_{N,0}(r).
 \tag{5}
\]

沿精确(4)可用另一个显式充分upper：

\[
 |\ell_0(r)|
 \le\left[(1+c^{-1})\frac{2N}{N^2-\alpha^2}
                   +\frac{\|\nu\|_2}{\sqrt N}\right]p_{N,0}(r),
 \quad N>\alpha.
 \tag{6}
\]

其中∫e^(±αt−N|t|)dt=2N/(N²−α²)，且||r||du≤p_(N,0)/√N。N按原半范数可取整数≥1；这不是跨N／模型的统一价格，也不是sharp operator norm／necessary lower。

前轮已付T r=∫r(t)e^(αt)P0K_g(i e^t)dt的||Tr||Hm≤C_m||r||du。于是未投影的同一个raw源确可在F定义为

\[
 R_{\rm raw}r=\int r(t)e^{\alpha t}K_g(i e^t,\cdot)dt
             =Tr+\ell_0(r)\mathbf1.
 \tag{7}
\]

该式在每个H^m和C^k中是绝对Bochner积分：第一项用前轮实际L²核费，第二项用(5)/(6)及constant函数。空间导数／时间积分／空间均值交换因此都有majorant；无crop、分布delta或隐含正则化。按原spectral H^m规范，||1||Hm=√V_μ，所以

\[
 \|R_{\rm raw}r\|_{H^m}
 \le C_m\|r\|_{du}+\sqrt{V_\mu}|\ell_0(r)|.
 \tag{8}
\]

这支付全部complex强源r的真实C∞ raw函数；real r先得real F∞不变函数再复化，沿同一已核scalar实结构。physical r=e^(t/2)f_phys、原du=dt不改；没有把此强费称为原du、Dlog、Hlog或自然height费。

## 3. 同一个actual Pan：系数、方向与o(1)误差

405／553的非零实际physical关系记

\[
 H(t)=e^{t/2}h(t)>0,\qquad
 p=(D^2-\tfrac14)H,\qquad p_b(t)=p(t-b).
 \tag{9}
\]

H,p∈F。405原h^sharp=h使H偶；所有p_b及其有限复线性组合仍是actual physical Pan。这里用的是553的纯physical平移，不把Cτ_b p_an=e^(b/2)τ_b(Cp_an)的缩放遗漏；Pan为线性空间，纯p_b均合法。

强衰减许可每个实s的带权分部积分，给

\[
 P(s):=\int p(t)e^{st}dt
       =(s^2-\tfrac14)\int H(t)e^{st}dt.
 \tag{10}
\]

在s=±α，α²−1/4=5/16，因此

\[
 A_\pm:=P(\pm\alpha)
       =\frac5{16}\int H(t)e^{\pm3t/4}dt>0.
 \tag{11}
\]

两者相等，因为H偶。若按405的原M_h(s)=∫e^(st)h(t)dt=ξ_Riemann(s)/2写同一系数，则

\[
 A_+=A_-=:A=\frac5{32}\xi_{\rm Riemann}(5/4)>0.
 \tag{12}
\]

负端也可写5ξ_Riemann(−1/4)/32，405原functional equation／H偶给其同值；不用RH、零点简单性或spacing。式(11)的严格正性已经足够，不需要额外ξ数值。

代入精确(4)得到对每个b的全公式

\[
 \ell_0(p_b)
 =-A_+e^{\alpha b}+c^{-1}A_-e^{-\alpha b}
       +\epsilon(b),\qquad
 \epsilon(b)=\int p(u)\nu(u+b)du.
 \tag{13}
\]

由p,ν∈L²，|ε(b)|≤||p||₂||ν||₂；还确有ε(b)→0于b→±∞。一个不用额外Fourier约定的证明是先以compact支撑L²函数近似p和ν：近似项在充分大的平移下支撑不交而积分为0；Cauchy–Schwarz使其余误差对b一致可小。故

\[
 \boxed{\ell_0(p_b)=-A_+e^{3b/4}+c^{-1}A_-e^{-3b/4}+o(1)}
 \quad (|b|\to\infty).
 \tag{14}
\]

于是b→+∞时ℓ0(p_b)∼−A_+e^(3b/4)<0，b→−∞时ℓ0(p_b)∼+c^−1A_-e^(−3b/4)>0。保留了方向、covol及actual系数；不是某个数值b的单点检验。所有关系仍noncompact，未把裁剪后的p_b冒称Pan。

## 4. 无原全线统一费、固定窗价格及给联合稿的输入

pure translations p_b在原L²du、zero-extension Dlog及Hlog的范数均不随b改变；它们有限，因为p∈F。因此(14)证明ℓ0对这三个同一global源域均无finite uniform upper。这里直接用了实际双pole-zero Pan，不是只用任意compact探针；这也没有说joint source的全部下降已失败。

若只看固定compact源窗(−L,L)上的原du标量读出，准确的squared operator fee为∫_(−L)^L|m(t)|²dt（在Cc∞窗上以L²密度取同一sup）。由(2)与分段主项m0(t)=−e^(αt)于t≥0、c^−1e^(−αt)于t<0，m²−m0²在R可积，故

\[
 \|\ell_0\|^2_{du,(-L,L)}
 =\frac{1+c^{-2}}{2\alpha}e^{2\alpha L}+O(1)
 =\frac23(1+c^{-2})e^{3L/2}+O(1),\qquad L\to\infty.
 \tag{15}
\]

这是full compact窗标量费，不假称其在双polezero子域仍为同一精确norm，也不提供Hlog窗sharp常数或任何classic whole预算。

给联合闭包稿的实际输入可取b→+∞并令q_b=p_b/ℓ0(p_b)。对充分大b它有定义，q_b仍是actual Pan，且

\[
 \ell_0(q_b)=1,\qquad
 \|q_b\|_{du}=\frac{\|p\|_{du}}{|\ell_0(p_b)|}\to0,
 \qquad
 \|Tq_b\|_{H^m}\le
 \frac{C_m\|p\|_{du}}{|\ell_0(p_b)|}\to0.
 \tag{16}
\]

同一q_b对每个m都给收敛，从而Tq_b→0于C∞。式(16)是实际关系像逼近(1,0)的输入；任意完整joint closure、连续mixed或后处理后果由独占联合稿/root另闭，不把这个单列sequence说成exact全像。

## 5. 角色、最强旧与净值

已付的是同一raw核的F强源定义、精确Mellin±3/4加bounded余项、actual Pan全b公式及两个方向leading、原全线费失败和明确固定窗标量费。没有更改R/B/L/ray/weight或添加未知scalar。±3/4是固定核的零模指数，与classic physical双pole±1/2不同；实际p在±1/2的矩恰零，却在±3/4有(11)的非零矩，不能把后者叫作已识别的classic pole。

natural metric height不见空间常数是旧ddc常数为零的事实，不把它作为新正号。当前mean无du上界也不自动给primitive或escape；精确(4)已将它扣回固定Mellin泛函＋L²有界读出的标准类，(13)/(16)只是结合已付真实关系与平移。建议标准／强旧合成0数学轮，不预新合同或经典whole结果。联合对象能否下降仍应按同一actual S_raw、目标拓扑与continuous pairing核，不能仅凭scalar非零作结论。

未支付作者7.4/modularity／整体算术Theta、primitive整过滤/截面/mixedRR、完整Γ/contact/properpowers/双poleWeil身份、537同源coverage或growth/core/coupling/Ξ；strongest-old wholeleading4/5仍为负惯性UPPER，经典主瓶颈及长期Goal完成门未变。原literal源冻结和既有语义纠正保持。本稿只编辑此独占路径，没有新文献下载／网页／后章或引文原proof阅读。
