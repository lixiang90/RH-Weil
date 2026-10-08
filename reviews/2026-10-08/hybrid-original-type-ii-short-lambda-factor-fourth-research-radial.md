# 原Vaughan Type II：短Λ因子17/24与全部squarefull-k的1/2付款

2026-10-08。作者：radial。基线为已发布478后的权威main5d508871。
只新增本源；477/478、原数学源、检查器、论文与Git均不修改。

**状态：完整子族推导，待不同作者独审。** 对冻结 \(U=V=\lfloor X^{1/8}\rfloor\)、\(Y=X^{5/6}\) 的同一个实际 \(C_4\)，严格支付所有 \(U<m\le\lfloor X^{1/4}\rfloor\) 和全部允许 \(k\) 的四矩：
\[
 \mathcal M_{\mathrm{short}}\ll_\varepsilon X^{17/24+\varepsilon},
 \qquad \frac57-\frac{17}{24}=\frac1{168}>0.
 \tag{1}
\]
另外支付全部squarefull-k子族及large-m proper-prime-power子族的1/2四矩，并把原Type I四矩强化至7/12。原 \(b_V(k)\) 的精确零项强制非零squarefull-k满足 \(k>V^2\)。按short-m、large-m properpowers、large-prime-m/squarefull-k顺序分区，不重复付款。最终真实剩余为所有genuine prime \(m>\lfloor X^{1/4}\rfloor,\ k>V\) 且k非squarefull、\(Y<mk\le X\)。**没有证明whole四矩为17/24、常数级预算或新比例。**

## 1. 原对象、固定输入与量词

保持原
\[
 X=\frac{T}{2\pi},\quad \ell=\log X,\quad
 J_T=[T/4,4T],\quad a_\ell\ge c_\phi>0,\quad
 \|F\|_{p,T}=\left(\frac1T\int_{J_T}|F(t)|^pdt\right)^{1/p}.
 \tag{2}
\]
原genuine高素数scalar为
\[
 P_H(t)=\frac1{a_\ell\ell}
 \sum_{\sqrt X<p\le X}\frac{\log p}{\sqrt p}p^{it}.
\]
冻结原系数为
\[
 b_V(k)=\sum_{\substack{d\mid k\\d\le V}}\mu(d),\qquad
 C_4(t)=-\frac1{a_\ell\ell}
 \sum_{\substack{m>U,\ k>V\\Y<mk\le X}}
 \frac{\Lambda(m)b_V(k)}{\sqrt{mk}}(mk)^{it}.
 \tag{3}
\]
此处 \(\Lambda(m)\) 保留所有prime powers，\(b_V\) 保留原truncated divisor系数与符号。正高度、normalizer、两sharp endpoints均未替换。

| 冻结输入 | canonical LF SHA256 |
|---|---|
| [477完整Vaughan付款与实际系数](hybrid-original-vaughan-type-i-and-type-ii-reduction-research-radial.md) | cf58086aeb9eee63832ccd06f5499110ea236b4bd94396893757b62e75bdb9d4 |
| [其独立全文审查](hybrid-original-vaughan-type-i-and-type-ii-reduction-review-twisted.md) | 576a0841b5a5ad9bf8fbda74561bb83ca3d16654a0c2faac5f4aa80269fb296f |
| [原scalar/proper-power准入](hybrid-short-carrier-canonical-scalar-fourth-admission-research-radial.md) | f04279a9de54303d772859b2ee5e05010567404c53143c928a14e905eb51a0d7 |
| [476原增长上界](../../notes/476-original-fourth-growth-five-sevenths-with-ivic-density.md) | 179829dd25f92ff187359f73455aafad9f957d714df13cf871db47a76e9408b6 |

用到的经典外部引理是[Montgomery–Vaughan作者书Volume II](https://personal.science.psu.edu/rcv4/Vol2/Vol2.pdf) Theorem16.7及Lemma16.8，分别为PDF第18页（印刷第8页）与PDF第21页（印刷第11页）。本轮已实读原文陈述及证明。下面逐式自证本次实际对数相位的差分、三个长度区间与sharp权，不把generic exponent-pair名称当未写出的合同。

对任何最终固定 \(\varepsilon>0\)，先分配更小固定divisor损失，再令 \(T\to\infty\)。常数可依赖 \(\phi,\varepsilon\) 和§6的固定参数，不能把移动cut参数带入未声明统一估计。没有使用[Rθ]、新零点密度、RH、twistedζ四矩或短因子Watt定理。

## 2. 无权sharp对数和的统一Weyl界 [T/R]

**引理。** 固定 \(C>0\)。当 \(t\in J_T,\ 1\le R\le CT\) 时，对每个真实子区间 \(A\subset[R,2R]\)，
\[
 \left|\sum_{n\in A}n^{it}\right|
 \ll_C T^{1/6}R^{1/2}.
 \tag{4}
\]
这里 \(A\) 按其整数交集求和，可含任意实数sharp endpoints；常数与这些endpoints无关。

### 2.1. 小长度与长长度

若 \(R\le T^{1/3}\)，trivial项数给 \(O(R)\le O(T^{1/6}R^{1/2})\)。当 \(R\) 有界时同式以固定常数成立。

若 \(R\ge T^{2/3}\)，对 \(f(x)=t\log x/(2\pi)\)，在整个dyadic区间有
\[
 |f''(x)|\asymp_C T/R^2.
\]
Theorem16.7适用于任意partial endpoints，给
\[
 \left|\sum_{n\in A}n^{it}\right|
 \ll_C \sqrt T+\frac R{\sqrt T}.
\]
在 \(T^{2/3}\le R\le CT\) 上，每项均至多固定倍
\(T^{1/6}R^{1/2}\)。此分支无需主项或functional equation。

### 2.2. 中间长度的一次实际差分

现在 \(T^{1/3}<R<T^{2/3}\)。把 \(n^{it}1_A(n)\) 填零到一个长度 \(N\asymp R\) 的整数数组。对任意 \(1\le H\le N\)，Lemma16.8给
\[
 |S|^2\ll \frac{R^2}{H}
       +\frac RH\sum_{1\le h<H}|S_h|,\qquad
 S_h=\sum_{\substack{n,n+h\in A}}e(f(n+h)-f(n)).
 \tag{5}
\]
该不等式也可直接由移位填零数组自证：将 \(HS\) 写成H个平移之和，Cauchy后展开，差 \(h\) 恰出现 \(H-|h|\) 次；对角能量至多 \(R\)。因此实际短partial interval不会丢一个未付boundary项。

对 \(1\le h<H\le R\)，交集仍是一个整数区间，并且
\[
 f_h''(x)=\frac{t}{2\pi}
          \left(\frac1{x^2}-\frac1{(x+h)^2}\right)
         =\frac{th(2x+h)}{2\pi x^2(x+h)^2}
         \asymp \frac{hT}{R^3}.
 \tag{6}
\]
只在 \(x,x+h\in[R,2R]\) 使用此式，故符号固定、上下常数统一。Theorem16.7的真实前件由(6)支付，得到
\[
 |S_h|\ll \sqrt{\frac{hT}{R}}
                  +\frac{R^{3/2}}{\sqrt{hT}}.
\]
代入(5)，用 \(\sum_{h<H}\sqrt h\ll H^{3/2}\)、
\(\sum_{h<H}h^{-1/2}\ll H^{1/2}\)，得
\[
 |S|^2\ll
 \frac{R^2}{H}+\sqrt{TRH}
                  +\frac{R^{5/2}}{\sqrt{TH}}.
 \tag{7}
\]
取 \(H=\max(1,\lfloor R/T^{1/3}\rfloor)\)。它合法且
\(H\asymp R/T^{1/3}\)，当H=1时(5)的空差分和给同样预算。于是
\[
 |S|^2\ll R T^{1/3}+\frac{R^2}{T^{1/3}}
             \ll R T^{1/3},
\]
最后不等式用 \(R\le T^{2/3}\)。与另外两个分支合并，证明(4)。

## 3. sharp临界权与完整斜乘积掩码 [T]

对任意真实子区间 \(A\subset[R,2R]\)，权
\(w_j(r)=r^{-1/2}(\log r)^j\)，\(j=0,1\)，其sup加总变差
\[
 \|w_j\|_\infty+\operatorname{Var}_{[R,2R]}w_j
 \ll R^{-1/2}(\log(2R))^j.
\]
逐式partial summation用(4)对全部partial endpoints，给
\[
 \left|\sum_{r\in A}
      r^{-1/2}(\log r)^j r^{it}\right|
 \ll T^{1/6}(\log(2R))^j.
 \tag{8}
\]
一般区间 \((A_0,B_0]\subset[1,CX]\) 切成O(logX)个dyadic子区间。因此
\[
 \left|\sum_{A_0<r\le B_0}
      r^{-1/2}(\log r)^j r^{it}\right|
 \ll T^{1/6}(\log(2X))^{j+1}.
 \tag{9}
\]
这是实际sharp求和，不要求先以可分离rectangle取代斜的 \(mk\) 边界。

取 \(M=\lfloor X^{1/4}\rfloor\)，定义原C4的完整子族
\[
 S_M(t)=-\frac1{a_\ell\ell}
 \sum_{\substack{U<m\le M,\ k>V\\Y<mk\le X}}
 \frac{\Lambda(m)b_V(k)}{\sqrt{mk}}(mk)^{it}.
 \tag{10}
\]
当T足够大时 \(Y/M>V\)，所以子族中的 \(k>V\) 已由原 \(Y<mk\) 强制；它没有被丢弃为另一函数。展开有限原divisor和，精确得到
\[
 S_M(t)=-\frac1{a_\ell\ell}
 \sum_{U<m\le M}\frac{\Lambda(m)m^{it}}{\sqrt m}
 \sum_{d\le V}\frac{\mu(d)d^{it}}{\sqrt d}
 \sum_{Y/(md)<r\le X/(md)}\frac{r^{it}}{\sqrt r}.
 \tag{11}
\]
所有三个和有限，重排无收敛假设。r的sharp endpoints随m,d变化，(9)正是对这些endpoints统一的界。两端不增加边界多项式。其下端至少 \(X^{11/24}\)，上端不超过X，均在已证明的实际长度域。

由(9)及初等 \(\Lambda(m)\le\log m,\ |\mu(d)|\le1\)，
\[
 \sum_{m\le M}\frac{\Lambda(m)}{\sqrt m}
       \ll \sqrt M\log(2M),\qquad
 \sum_{d\le V}\frac{|\mu(d)|}{\sqrt d}\ll\sqrt V,
\]
得到
\[
 \sup_{t\in J_T}|S_M(t)|
 \ll_\phi X^{1/6}\sqrt{MV}(\log(2X))^C
 \ll_{\phi,\varepsilon}X^{17/48+\varepsilon}.
 \tag{12}
\]
(11)先保留了全部真实系数、cutoff与μ符号，再为子族upper取绝对值；未将positive sector当成whole norm下界。

## 4. 原子族的实际二矩与17/24 [T]

(10)作为一个长度至多X的有限Dirichlet polynomial，其n系数为
\[
 \alpha_n=-\frac{1_{Y<n\le X}}{a_\ell\ell\sqrt n}
 \sum_{\substack{m\mid n\\U<m\le M\\n/m>V}}
       \Lambda(m)b_V(n/m).
\]
逐项有
\[
 |\alpha_n|\ll_\phi \frac{\tau_3(n)}{\sqrt n}.
 \tag{13}
\]
因为 \(|b_V(k)|\le\tau(k)\)、
\(\sum_{m\mid n}\tau(n/m)=\tau_3(n)\)，并且 \(\log n\le\ell\)；没有把系数换成任意μ(n)。

为支付二矩，任意长度O(T)时间窗对
\(F(t)=\sum_{n\le Z}\alpha_n n^{it}\) 有
\[
 \frac1T\int_J|F(t)|^2dt
 \ll \left(1+\frac{Z\log(2Z)}T\right)\sum_n|\alpha_n|^2.
 \tag{14}
\]
自证是展开积分：非对角积分模至多 \(2/|\log(n/m)|\)，
\(\log(n/m)\ge(n-m)/Z\)，再以
\(2|\alpha_m\alpha_n|\le|\alpha_m|^2+|\alpha_n|^2\)
及harmonic sum支付。此式与J的正高度起点无关，原J_T完全覆盖。

对先固定的 \(\delta>0\)，\(\tau_3(n)\ll_\delta n^\delta\)。由(13)，
\[
 \sum_n|\alpha_n|^2\ll_{\phi,\delta}X^{2\delta}\log(2X).
\]
在(14)取Z=X、T=2πX，并在最终ε中分配δ与日志，得到实际
\[
 \|S_M\|_{2,T}^2\ll_{\phi,\varepsilon}X^\varepsilon.
 \tag{15}
\]
二矩不被当成免费条件，也不需要prime第四矩输入。

结合(12)、(15)，先分配更小ε，严格有
\[
 \boxed{\quad
 \mathcal M_{S_M}=\|S_M\|_{4,T}^4
 \le\|S_M\|_\infty^2\|S_M\|_{2,T}^2
 \ll_{\phi,\varepsilon}X^{17/24+\varepsilon}.
 \quad}
 \tag{16}
\]
要使显示上界仍严格低于5/7，可固定 \(\varepsilon<1/168\)。没有声称一个带ε式在任意ε下都低于5/7。

### 4.1. 同一Weyl引理支付原Type I至7/12

保留477同一 \(I_2,I_3\)、\(Y=X^{5/6}\) 和 \(U=V=\lfloor X^{1/8}\rfloor\)。
令 \(D=UV\)，其真实outer系数满足
\[
 |g_{U,V}(d)|\le\tau(d)\log(2d),\qquad
 \sum_{d\le D}\frac{|g_{U,V}(d)|}{\sqrt d}
 \ll_\delta D^{1/2+\delta}\log(2D).
\]
对原inner区间 \(Y/d<r\le X/d\) 用(9)的j0/j1两个版本，
并对 \(I_3\) 用 \(\sum_{d\le V}d^{-1/2}\ll\sqrt V\)，得到
\[
 \sup_{J_T}|I_2+I_3|
 \ll_{\phi,\varepsilon}T^{1/6}D^{1/2}X^\varepsilon
 \ll_{\phi,\varepsilon}X^{7/24+\varepsilon}.
 \tag{16a}
\]
这里两个outer都保留原g与μ系数，并未取掉共同sharp下端。
原n系数仍至多 \(\tau_3(n)\log(2n)+\tau(n)\log(2n)\)，
长度至多X；用(14)与固定divisor损失重新支付
\(\|I_2+I_3\|_{2,T}^2\ll X^\varepsilon\)。
因而
\[
 \|I_2+I_3\|_{4,T}^4
 \ll_{\phi,\varepsilon}X^{7/12+\varepsilon}.
 \tag{16b}
\]
冻结Y下，lower block仍为2/3，所以返回 \(P_H-C_4\) 的整体范数费用仍为1/6。
这是旧Type I的实际强化，不把7/12说成whole费用。

若另先固定 \(a>0\) 后重新定义 \(U=V=\lfloor X^a\rfloor\)，
同一实际证明给Type I四矩 \(X^{1/3+2a+\varepsilon}\)。
可合法另选 \(y=2/3+a<1\) 平衡lower费用 \(2y-1\)，但此时原C4的
共同lower cutoff必须相应改为 \(X^y\)，不能把新费用直接移到旧余项。
主结论(1)、(16)及以下ledger均保持冻结Y，不依赖该改cut优化。

## 5. 完整原对象的第一层账本：norm而非additive等同

定义真实剩余
\[
 R_M(t)=-\frac1{a_\ell\ell}
 \sum_{\substack{m>M,\ k>V\\Y<mk\le X}}
 \frac{\Lambda(m)b_V(k)}{\sqrt{mk}}(mk)^{it}.
 \tag{17}
\]
它没有丢任何允许aspect ratio或原prime powers。精确有限恒等式为
\(C_4=S_M+R_M\)，所以Minkowski及
\((u+v)^4\le8(u^4+v^4)\) 分别给
\[
 \mathcal M_{C_4}\le8\mathcal M_{R_M}
                  +C_{\phi,\varepsilon}X^{17/24+\varepsilon},
 \qquad
 \mathcal M_{R_M}\le8\mathcal M_{C_4}
                  +C_{\phi,\varepsilon}X^{17/24+\varepsilon}.
 \tag{18}
\]
第二式使用 \(R_M=C_4-S_M\)，并非把两第四矩误认为additive相差小量。

冻结477已付原lower block及Type I的2/3，连同原proper-power完整
\(\|\widehat P_H-P_H\|_{4,T}=O(X^{-1/12})\)，给
\[
 \|P_H-C_4\|_{4,T}\ll_{\phi,\varepsilon}X^{1/6+\varepsilon}.
\]
由于 \(17/96>1/6\)，(16)与范数三角严格得到
\[
 \|P_H-R_M\|_{4,T}
 \ll_{\phi,\varepsilon}X^{17/96+\varepsilon}.
\]
再分配ε，得到原genuine对象的两向coupling
\[
 \boxed{\quad
 \mathcal M_T\le8\mathcal M_{R_M}
                    +C_{\phi,\varepsilon}X^{17/24+\varepsilon},
 \qquad
 \mathcal M_{R_M}\le8\mathcal M_T
                    +C_{\phi,\varepsilon}X^{17/24+\varepsilon}.
 \quad}
 \tag{19}
\]
负号、prime/composite cancellation在原 \(\Lambda(m)b_V(k)\) 中保持；本轮只支付真实short-m子族的upper。没有从其upper、其系数符号或coupling推得 \(R_M\) 的upper。

式(19)是第一层真实ledger。§8进一步支付 \(R_M\) 中的全部squarefull-k子族，
最后只剩large-m/non-squarefull-k；原whole增长结果仍为476。
新支付不能用来认领whole exponent17/24、fixedcarrier第四常数、RH或新增无零区域。

## 6. 固定参数的可审成本前沿

不修改冻结a1/8对象，也可对另一个先固定的 \(a,b,y\) 给同样自证。置
\[
 U=V=\lfloor X^a\rfloor,\quad
 M=\lfloor X^b\rfloor,\quad Y=X^y,\quad
 0<a<b,\quad a+b<y<1.
\]
原C4重新按这些精确整数cut定义；不是把不同bV当成同一个函数。(11)仍合法，因为 \(Y/M>V\)。完全相同的actual系数二矩和sharp内层证明给
\[
 \mathcal M_{S_M}
       \ll_{\phi,a,b,y,\varepsilon}X^{1/3+a+b+\varepsilon}.
 \tag{20}
\]
因此付款严格低于5/7的条件是
\[
 a+b<\frac8{21},\qquad
 a<b<\frac8{21}-a.
 \tag{21}
\]
这是子族成本前沿，不是whole最优无零边界。对冻结 \(a=1/8\)，允许
\(1/8<b<43/168\)；本稿的 \(b=1/4\) 留下确切1/168幂余量。
每个b先固定，接近该前沿时最后ε必须相应缩小。

例如先固定 \(a=1/16,b=5/16,y=3/4\)，同样付17/24；原477固定a tradeoff的lower/Type I费用为1/2，故可把对应genuine对象归约到全部 \(m>X^{5/16},k>X^{1/16}\) 的真实余项。这个改变一方面提高m阈值，另一方面降低k阈值；没有得到对冻结a1/8剩余的免费统一改进。

## 7. 短Λ付款的实际意义

新增的是对同一旧C4的完整short-Λ因子子族实际L4付款：全部 \(U<m\le X^{1/4}\)、全部 \(k>V\)、原斜 \(Y<mk\le X\) 和全正高度窗。一次内层差分不是对退化的Type-II乘积相位假用非零m导数；它仅在展开原有限divisor后，对真正无权r和施用(6)。

没有再次发布短μ准入或原zero留数障碍。下一节只支付(17)的另一个完整原系数子族；
balanced prime×prime等非squarefull-k signed sector仍在最终余项。不能把一个positive rectangle的结果代替它。

## 8. 疏外因子与完整共同cutoff：最大prefix四矩 [T]

本节的squarefull-k初步路线由compression在同轮独立快研提示；radial核出并证明原 \(b_V\) 的完整零域。根线程进一步提示large-m proper-power子族，下面用同一最大prefix引理独立付款。它们不是对原n整体的proper-power替换，而是原C4内部不同因子的真实子族。

**最大prefix引理。** 设 \(A\ge1,\ A\ll X\)，
\(q(n)\) 为实际有限系数，并对每个固定 \(\delta>0\) 有
\(|q(n)|\ll_\delta X^\delta\)。这允许 \(q=\Lambda\) 或 \(q=b_V\)；
后者的常数对所有V统一，因为 \(|b_V(n)|\le\tau(n)\)。
在dyadic区间 \(A<n\le2A\) 上定义
\[
 B_q(t;u)=\sum_{A<n\le u}\frac{q(n)}{\sqrt n}n^{it},
 \qquad A\le u\le2A.
\]
则在原整个正高度窗上
\[
 \frac1T\int_{J_T}
       \max_{A\le u\le2A}|B_q(t;u)|^4dt
 \ll_\varepsilon X^\varepsilon(1+A^2/X).
 \tag{22}
\]
区间若还加任意固定lower/upper mask，只须在数组中填零，同式仍成立。

证明：把这些整数排列成长度 \(N\asymp A\) 的2幂数组，空位置填零。
第j层的 \(2^j\) 个不交binary blocks各含至多
\(O(A2^{-j})\) 项，\(0\le j\le\log_2N\)。对每block I，
\[
 Q_I(t)=\sum_{n\in I}\frac{q(n)}{\sqrt n}n^{it},
 \qquad
 \sum_{n\in I}\frac{|q(n)|^2}{n}
       \ll_\delta X^{2\delta}2^{-j}.
\]
平方后的实际product系数满足divisor Cauchy
\[
 \sum_v\left|
     \sum_{\substack{n_1n_2=v\\n_1,n_2\in I}}
       \frac{q(n_1)q(n_2)}{\sqrt{n_1n_2}}
          \right|^2
 \le \max_{v\le4A^2}\tau(v)
       \left(\sum_{n\in I}\frac{|q(n)|^2}{n}\right)^2.
\]
\(\tau(v)\ll_\delta X^{2\delta}\)，固定log损失由最终ε支付。
对 \(Q_I^2\) 用(14)，其**实际product长度**至多4A²，得到
\[
 \sum_{I\text{在第j层}}\|Q_I\|_{4,T}^4
 \ll_\varepsilon X^\varepsilon(1+A^2/X)2^{-j}.
\]
没有将product support误改为A或假设完整ζ四矩。

每个prefix可写成每层至多一个binary block；对所有prefix逐t，
\[
 \max_u|B_q(t;u)|
 \le\sum_j\left(\sum_{I\text{在第j层}}|Q_I(t)|^4\right)^{1/4}.
\]
L4 Minkowski和收敛的 \(\sum_j2^{-j/4}\) 证明(22)。
任意sharp区间 \((u_1,u_2]\) 是两个prefix之差，其逐t模至多
两倍最大prefix。此步骤保留原斜cutoff随外因子移动，不要求rectangle分离。

### 8.1. 原squarefull-k的精确自然零项

squarefull指每个prime divisor的valuation至少2。若
\(1<k\le V^2\) 且k squarefull，则
\[
 \operatorname{rad}(k)\le\sqrt k\le V,\qquad
 b_V(k)=\sum_{d\mid\operatorname{rad}(k)}\mu(d)=0.
 \tag{23}
\]
第一个不等式来自 \(\operatorname{rad}(k)^2\mid k\)；
所有非零μ-divisor均为rad(k)的divisor，所以第二式是全部真实divisor和。
原 \(k>V\ge2\) 已排除k1。故实际C4中非零squarefull-k一定满足
\(k>V^2\)，未新增人工zero mask。

平方满数均可唯一写成 \(k=a^2b^3\)，b squarefree：
even valuation放入a²，odd valuation≥3放一个b³。
因此
\[
 \#\{K<k\le2K:k\ {\rm squarefull}\}
 \le\sum_{b\le(2K)^{1/3}}\sqrt{2K}\,b^{-3/2}
 \ll\sqrt K.
\]
不用prime density或平均μ符号；由 \(|b_V(k)|\le\tau(k)\)，得到
\[
 \sum_{\substack{K<k\le2K\\k\ {\rm squarefull}}}
       \frac{|b_V(k)|}{\sqrt k}\ll_\delta X^\delta
 \quad(K\le X).
 \tag{24}
\]

为先证明完整子族，可取任意 \(m_0\ge U\)；在m、k上分别dyadic分块。
对一个非空 \((M,2M]\times(K,2K]\)，共同 \(Y<mk\le X\)
给每个固定k的真实m区间
\((\max(M,m_0,Y/k),\min(2M,X/k)]\)。
以两个Λ-prefix差保留这个区间，再对外k求绝对值，得
\[
 |C_{\rm sf,M,K}(t)|
 \ll_\phi X^\delta
       \max_{M\le u\le2M}|B_\Lambda(t;u)|.
\]
(22)遂给其第四均值
\(\ll X^\varepsilon(1+M^2/X)\)。
非空块有 \(MK<X\)，并可从 \(K=V^2\) 开始dyadic覆盖；
所以 \(M<X/K\le X/V^2\)。最后对O(log²X)个真实块用L4 Minkowski，
全部日志在ε中分配，得到
\[
 \boxed{\quad
 \mathcal M_{\rm squarefull\text{-}k,\ m>m_0}
 \ll_{\phi,\varepsilon}X^\varepsilon(1+X/V^4)
 \ll_{\phi,\varepsilon}X^{1/2+\varepsilon}.
 \quad}
 \tag{25}
\]
这同时覆盖 \(m_0=U\) 的整个原squarefull-k子族，
以及不重叠ledger所需 \(m_0=M\)。
所有m可以为prime或prime power；原bV和共同sharp乘积掩码均保持。

### 8.2. large-m proper-prime-power全部k

设 \(M_0=\lfloor X^{1/4}\rfloor\)。这里proper prime power指
\(m=p^j,\ j\ge2\)，不含prime本身。对每个dyadic \((M,2M]\)，
\[
 \sum_{\substack{M<m\le2M\\m=p^j,\ j\ge2}}
       \frac{\Lambda(m)}{\sqrt m}
 \ll(\log(2X))^2.
 \tag{26}
\]
直接验证：j2至多O(√M)个base，每项≤log(2M)/√M；
j≥3至多O(logM)种exponent，每种至多O(M^{1/3})个base，
合计 \(O(M^{-1/6}(\log(2M))^2)\)。
只用整数项数，保留所有prime powers和Λ(p^j)=logp。

固定每个这样的m，原k区间
\((\max(K,V,Y/m),\min(2K,X/m)]\)
是两个真实bV-prefix之差。以(26)作稀疏外L1权、
以(22)对实际 \(q=b_V\) 作内层最大prefix四矩，得到
\[
 \mathcal M_{\rm pp,M,K}\ll_\varepsilon X^\varepsilon(1+K^2/X).
\]
对全部 \(m>M_0\) 的非空块有 \(K<X/M_0\)；
O(log²X)个块的L4 Minkowski给
\[
 \boxed{\quad
 \mathcal M_{\rm large\text{-}m\ properpower}
 \ll_{\phi,\varepsilon}
        X^\varepsilon(1+X/M_0^2)
 \ll_{\phi,\varepsilon}X^{1/2+\varepsilon}.
 \quad}
 \tag{27}
\]
这里k不限squarefull或prime，不调用bV的FE、零自由pointwise界或假设μ随机。

## 9. 最终不重叠实际ledger与尚未付款的genuine sector

现在分成三个已付子项及一个真实剩余：
\[
 C_4=S_{M_0}+P_{\rm pp}+P_{\rm sf}+R_{\rm gp,nsf}.
 \tag{28}
\]
其中：

- \(S_{M_0}\)：全部 \(U<m\le M_0\)，全部k；四矩17/24。
- \(P_{\rm pp}\)：\(m>M_0\) 为proper prime power，全部k；四矩1/2。
- \(P_{\rm sf}\)：\(m>M_0\) 为genuine prime，k squarefull；四矩1/2。
- \(R_{\rm gp,nsf}\)：\(m>M_0\) 为genuine prime，\(k>V\) 非squarefull。

每项均带同一个 \(Y<mk\le X\)、原normalizer及原负系数。
Λ为零的m不贡献，故(28)是精确finite partition；SF付款(25)对其prime-m子集可直接用同一prefix证明，不能由一个复杂signed全函数norm直接推出任意子集norm。

三已付项的合成L4范数由Minkowski至多
\(C_{\phi,\varepsilon}X^{17/96+\varepsilon}\)。
再加入原lower block2/3、实际Type I7/12、完整proper-power迁移，
整体误差函数 \(E=P_H-R_{\rm gp,nsf}\) 满足相同范数界。
以一个余项加一个误差函数的两向三角，得到
\[
 \boxed{\quad
 \mathcal M_T\le8\mathcal M_{\rm gp,nsf}
                      +C_{\phi,\varepsilon}X^{17/24+\varepsilon},
 \qquad
 \mathcal M_{\rm gp,nsf}\le8\mathcal M_T
                      +C_{\phi,\varepsilon}X^{17/24+\varepsilon}.
 \quad}
 \tag{29}
\]
没有把各次triangle的常数8相乘后误写成8：先合成误差函数，再只应用一次
\((u+v)^4\le8(u^4+v^4)\)。日志/ε先按有限子项数量分配。

本轮完整支付了两种原系数疏族，并提高了原Type I付款；留下的已是genuine-prime m的大因子与non-squarefull-k共同mixed4。其balanced prime×prime sector仍存在，μ截断的真实符号与全部cutoff仍保留，尚无whole小于5/7的upper。不能用本轮成本前沿、疏因子计数或这份精确ledger替代该最后算术付款。

