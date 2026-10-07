# 原实线有限 P 的整个四阶压缩差：无零自由前件的共同起点付款

2026-10-08。作者 radial_review。新完整推导，待其他作者独立全文审查。
基线 2d5621dbc999e0cf313ea224b825d6d56547c45c。
不改变原域、prime cutoff、scalar sharp coefficients、taper、normalizer、
载波间距或 finite dimension；全部旧源、论文、输出和 Git 保持冻结。

本轮新付款：固定原 X、ell、d，在合法的短起点区间
[T,T+T/sqrt ell] 中，对真实 raw high/low operators 的 P leakage 作
二矩平均，得到 O(ell)。因此整个 fourth Jensen deficit 的平均为
O(ell^−2)，全部16个有序 high/low 四词的 three-P 差的 mean absolute
也为 O(ell^−2)。存在同一个起点使这些全部差词同时趋零。
证明使用原 whole-height bounded prime multipliers、经典 finite
Montgomery–Vaughan second 与真实 e基；没有 [R] 零自由输入或未知
high fourth bounded 前件，也没有周期化 physical translations。

这是 anchored moving-carrier 上的实际准入定理，不是 original 起点
恰等于 T 的逐点 o(1) 定理。移动起点是 AF 原构造允许的参数，
零块传递范围见第8节。仍未支付同一物理 four-prime long-product
signed upper；因此没有新的实际比例、无零边界或 RH 证明。

## 1. 原对象、合法起点与冻结输入

冻结 X=T/(2π)、ell=log X、d=floor(X ell)、h=2π/ell、
I=[−ell/2,ell/2]、原 even C² taper φ。
φ的 L¹/一阶/二阶导数分别为 O(ell)、O(1)、O(1)，0≤φ≤1，
a_ell=ell^−1‖φ‖2²有固定正下界。
对任意起点 σ，定义真实 interval isometry

\[
 E_\sigma e_k=\ell^{-1/2}1_I e^{i(\sigma+hk)u},
 \quad 0\le k<d,\quad P_\sigma=E_\sigma E_\sigma^*,
 \quad Q_\sigma=1-P_\sigma .                            \tag{1}
\]

它只是同一原网格的共同 modulation。
prime channels 不随平均变量改变：

\[
 \begin{gathered}
 b_p=\frac{\log p}{a_\ell\ell\sqrt p},\quad
 B_R=-\sum_{p\in R}b_p M_\phi
                 (R_{\log p}+R_{-\log p})M_\phi,\\
 R=H:\sqrt X<p\le X,\qquad R=L:p\le\sqrt X,\qquad
 C_{R,\sigma}=E_\sigma^*B_RE_\sigma .
 \end{gathered}                                         \tag{2}
\]

R_s是真正零延拓的实线平移；B_R输出支撑在I。
单个T时这是有限 bounded selfadjoint prime sum。

| 冻结输入及本次使用范围 | canonical UTF-8 LF SHA-256 |
| --- | --- |
| [223-C：interval-uniform weighted MV second](../../notes/223-short-height-hilbert-mv-adjacent-closure.md) | e5a179bdf9c3b64cfb9d62284fcf4ec1206cdded5828c37defc77755e3dece2e |
| [225：旧 signed-first-mean 边界的范围对比](../../notes/225-fourfold-toeplitz-signed-boundary-closure.md) | 7b87d8e53007873edcb19d0cf42651baab71bcd40b21d7a3f3a3cd81eb35ddd0 |
| [228：anchored moving zero blocks](../../notes/228-relative-dense-zero-block-transfer.md) | 2cc8a3f5eb0e66ef0a6306a317a1e2b03c046c62b8284a87ccbee8e8130181ae |
| [原 e基 leakage 与 closed two-crossing](../2026-10-07/hybrid-one-three-finite-band-admission-research.md) | bc6ad6b1a007422c7678cd540b4127b81d2adc168faf5b090a58b6676778e35f |
| [原 fourth 正差、whole physical 与 nearcore](../2026-10-07/hybrid-whole-fourth-compression-upper-research-radial.md) | 0703f66778d49de29e363f7eabede6718ef24fe579e53603ff70db4e6aeacdea |
| [471：当前 long-product 余额](../../notes/471-original-principal-subtraction-and-signed-four-distinct-target.md) | a66dcc18606b59ac0aa1a879f64f6f7dae4a3278981e5fbc2c94190efa3a3ef6 |

canonical 只统一 CRLF、lone CR为LF，不 trim或改变EOF。
旧225的 signed first mean 及其其他算术闭合不作本稿前件；
本稿不从 signed average 推出 mean absolute。
从223只读取 finite scalar weighted MV；从228只读取零侧移动端点接口，
不读取其旧 fourth-trace 算术前件或比例数值。

## 2. 整条高度轴上的 prime second：统一于每个平移区间

原 unitary Fourier 下

\[
 B_R=M_\phi\mathcal F^{-1}M_{D_R}\mathcal F M_\phi,
 \quad D_R(t)=-\sum_{p\in R}b_p(p^{it}+p^{-it}).
 \tag{3}
\]

Chebyshev、partial summation 给

\[
 y_H:=\|B_H\|\le\|D_H\|_\infty\ll\sqrt X/\ell,\quad
 y_L\ll X^{1/4}/\ell,\quad
 \sum_{p\in R}b_p^2\ll1,\quad
 \sum_{p\in R}p b_p^2\ll X/\ell .                       \tag{4}
\]

最后两式可直接检查：
∑(log p)²/p≤ell ∑(log p)/p=O(ell²)，
∑(log p)²≤ell ∑log p=O(X ell)。
所有normalizer仍是原(a_ell ell)²。

finite Montgomery–Vaughan输入是，对任意实区间[β,β+s]，

\[
 \int_\beta^{\beta+s}\left|\sum_n a_n n^{it}\right|^2dt
 \le s\sum_n|a_n|^2+C\sum_n n|a_n|^2,\qquad s>0.
 \tag{5}
\]

常数不依赖β；也可将起点吸收到unit phases中。
对(3)的两个相反符号用
|P(t)+P(−t)|²≤2|P(t)|²+2|P(−t)|²，得到全部高度的一致量

\[
 M_{2,R}(s):=\sup_\beta\frac1s
                \int_\beta^{\beta+s}|D_R(t)|^2dt
       \ll1+\frac{X}{\ell s}.                          \tag{6}
\]

没有对t≈0使用Perron或删掉 coherent peak。
平均时X、ell、d、φ与所有prime coefficients都冻结；只移动σ。

## 3. 原 QP leakage 的 e基公式与 shifted lattice 能量

定义
\(\lambda_R(\sigma)=\|Q_\sigma B_RE_\sigma\|_{\rm HS}\)。
由于输出在I，Q的相关部分准确是全interval Fourier basis中
j∉[0,d−1]的那些向量，不漏掉 I^c。
非unitary hatφ使用实线积分归一化。原 entry 为

\[
 (B_R)_{jk}^{(\sigma)}
  =\frac1{2\pi\ell}\int_{\mathbb R}
      \overline{\widehat\phi(\xi-h(j-k))}
      D_R(\sigma+hk+\xi)\widehat\phi(\xi)\,d\xi .
 \tag{7}
\]

这仍是全高度 bounded multiplier 的准确式，不取good band。
每个n=j−k，对outside j，允许k数准确为min(d,|n|)。
定义

\[
 W_\ell(\xi)=\ell^{-2}\sum_{n\in\mathbb Z}
      \min(d,|n|)|\widehat\phi(hn-\xi)|^2 .
 \tag{8}
\]

对所有实ξ一致，

\[
 \ell^{-2}\sum_n|\widehat\phi(hn-\xi)|^2\ll1,\qquad
 W_\ell(\xi)\ll1+\log(2+\ell)+\ell|\xi| .                \tag{9}
\]

自证：取ν=ξ/h，|n|≤|n−ν|+|ν|。
|n−ν|≤1的项用|hatφ|≤C ell；
1<|n−ν|≤ell用|hatφ|≤C ell/|n−ν|；
更远用|hatφ|≤C ell²/|n−ν|²。
weighted sum依次为O(1)、O(log ell)、O(1)，unweighted为O(1)。
第二项 |ν|乘unweighted bound给O(ell|ξ|)。
这个证明包含ν任意接近整数，不将ξ偷偷离散化。

原C² bounds又严格给

\[
 \int|\widehat\phi(\xi)|\,d\xi\ll1+\log(2+\ell),\quad
 \int|\xi|^{1/2}|\widehat\phi(\xi)|\,d\xi\ll1,
\]
\[
 \int|\widehat\phi(\xi)|\sqrt{W_\ell(\xi)}\,d\xi
       \ll\sqrt\ell .                                 \tag{10}
\]

前两式用min(ell,C/|ξ|,C/ξ²)在1/ell、1处分段。
最后由(9)给O((1+log ell)^(3/2)+sqrt ell)=O(sqrt ell)。
不能改用∫|ξ||hatφ|；在只有C²输入时该积分的粗界会发散。

## 4. 新准入：σ、j、k 联合 L² 中的 Minkowski

任取起点区间 \(\mathcal I_s=[\sigma_0,\sigma_0+s]\)。
把(7)视为
L²(dσ/s;ℓ²{(j,k):j outside,0≤k<d})中的向量积分。
Minkowski、(6)、准确outside count给

\[
 \begin{aligned}
 \left(\frac1s\int_{\mathcal I_s}\lambda_R(\sigma)^2d\sigma
                  \right)^{1/2}
 &\le\frac1{2\pi\ell}\int|\widehat\phi(\xi)|
  \left(\sum_{\substack{k,j\\j\ {\rm outside}}}
    |\widehat\phi(\xi-h(j-k))|^2
    \frac1s\int_{\mathcal I_s}
                |D_R(\sigma+hk+\xi)|^2d\sigma\right)^{1/2}d\xi\\
 &\ll\sqrt{M_{2,R}(s)}
          \int|\widehat\phi(\xi)|\sqrt{W_\ell(\xi)}\,d\xi .
 \end{aligned}                                         \tag{11}
\]

每个(k,ξ)只是对σ区间作实平移，(6)对全部平移统一，故可以在求和前用。
无穷entry求和及积分由(10)的可积majorant控制；
也可先finite截断，再单调收敛。没有假定不同prime leakage正交。

因此新增实际估计为

\[
 \boxed{\frac1s\int_{\mathcal I_s}\lambda_R(\sigma)^2d\sigma
               \ll\ell+\frac Xs .}                    \tag{12}
\]

对两个真实channels可先相加。取
\[
 s=H_T=T/\sqrt\ell,\qquad\mathcal I_s=[T,T+H_T],
 \tag{13}
\]
则平均 \(\lambda_H^2+\lambda_L^2=O(\ell)\)。
Markov给一个Lebesgue measure至少H_T/2的共同集合
\(\mathcal G_T\subset[T,T+H_T]\)，在其上

\[
 \lambda_H(\sigma)^2+\lambda_L(\sigma)^2\le C\ell .
 \tag{14}
\]

C与T、σ无关，只依赖原固定profile。
这不是先挑high与low两个不同起点。

## 5. 整个 fourth Jensen deficit：raw 全高度且无 H4 前件

对任一bounded selfadjoint B和finite isometry E，按P⊕Q写
B=[[A,C*],[C,D]]，C=QBP、A=PBP、D=QBQ。
K=C*C≥0。严格finite乘法给

\[
 \begin{aligned}
 \operatorname{Tr}(E^*B^4E)-\operatorname{Tr}A^4
 &=2\operatorname{Tr}(A^2K)+\operatorname{Tr}K^2
                    +\|CA+DC\|_{\rm HS}^2\\
 &\ge0,\qquad
 \operatorname{Tr}(E^*B^4E)-\operatorname{Tr}A^4
       \le7\|B\|^2\|C\|_{\rm HS}^2 .
 \end{aligned}                                         \tag{15}
\]

最后三个upper分别是2y²λ²、y²λ²、4y²λ²。
这个一般恒等式已有冻结来源；新增付款是把真实raw λ的(12)代入，
而不是重命名未知gap。
令
\[
 a_\sigma=d^{-1}\operatorname{Tr}C_{H,\sigma}^4,\quad
 \Phi_\sigma=d^{-1}\operatorname{Tr}(E_\sigma^*B_H^4E_\sigma).
\]
原whole raw y_H²=O(X/ell²)、d∼X ell，因此

\[
 \boxed{0\le\frac1s\int_{\mathcal I_s}(\Phi_\sigma-a_\sigma)d\sigma
 \ll\frac1{\ell^2}+\frac{X}{s\ell^3}.}                 \tag{16}
\]

取(13)，右边O(ell^−2)。
对每个共同good σ∈G_T，直接有

\[
 \boxed{0\le\Phi_\sigma-a_\sigma=O(\ell^{-2})=o(1).}    \tag{17}
\]

全prime B_H+B_L同样成立，因其leak≤λ_H+λ_L，
op≤y_H+y_L。证明始终whole raw，全高度没有删掉乘子或packet；
因此没有追加463/[R]准入，也无未知四矩尾的统一可积性前件。

一般(16)说明s≫X/ell³已足以使本估计趋零。
但一个网格周期的微移s=2π/ell没有由此付款：
该MV合同只给O(X/ell²)的粗费用，不是o(1)。
本稿不声称微移不足的方法不可能性，只明确本次平均长度。

## 6. 全16个有序四词的 mean absolute three-P 差

对任意四个selfadjoint bounded factors B_i，
闭合trace的三个内部P逐一删除，每项至少两次crossing。
令λ_i=‖Q B_iP‖HS、y_i=‖B_i‖，严格有

\[
 \left|\operatorname{Tr}E^*B_1B_2B_3B_4E
       -\operatorname{Tr}(E^*B_1E\cdots E^*B_4E)\right|
 \le C\sum_{i<j}\lambda_i\lambda_j
                         \prod_{k\ne i,j}y_k .         \tag{18}
\]

具体three-P telescoping的第一项用B_1的cross与右triple，
第二项用左B_2与右pair，第三项用B_3、B_4；
product commutator expansion把每个右pair/triple cross
界为对应λ的线性和，给全部六个pair。
使用原P而非continuous Fourier projection。

平均(18)时用Cauchy
avg(λ_iλ_j)≤sqrt(avgλ_i² avgλ_j²)，没有从signed mean取绝对值。
对每个R_i∈{H,L}、原raw B_R，(4)、(12)给

\[
 \boxed{\frac1s\int_{\mathcal I_s}
  \frac1d\left|\operatorname{Tr}E_\sigma^*B_{R_1}B_{R_2}B_{R_3}B_{R_4}E_\sigma
       -\operatorname{Tr}\prod_{i=1}^4C_{R_i,\sigma}\right|d\sigma
 \ll\ell^{-2}+\frac{X}{s\ell^3}.}                      \tag{19}
\]

在(14)的同一集合，每个有序四词的差均O(ell^−2)。
故全部16 words，包括whole31与whole22，所有重复/distinct/signs
聚合后，同时有完整actual/physical差o(d)。
这是总channel算子乘积结论，不是逐tuple删P。
各physical placement仍按其自身顺序保留；没有用未许可的物理cyclic rotation。
没有由此证明physical词本身有界或付清four-distinct算术。

## 7. 原same-prime W下的平方 residual 比较

对high，保持其实际same-prime rowdiagonal压缩
W_σ=E_σ*M_w E_σ，0≤W_σ≤MI、M=O(1)；
该乘法压缩事实上不随共同σ modulation改变。
取 K_σ=(Q_σB_HE_σ)*(Q_σB_HE_σ)，准确有

\[
 E_\sigma^*B_H^2E_\sigma=C_{H,\sigma}^2+K_\sigma,\quad
 K_\sigma\ge0,\quad \operatorname{Tr}K_\sigma=\lambda_H(\sigma)^2 .
 \tag{20}
\]

定义实际q与two-step physical compression covariance：

\[
 q_\sigma=\|C_{H,\sigma}^2-W_\sigma\|_{2,d}^2,\quad
 q_{{\rm sq},\sigma}=
       \|E_\sigma^*B_H^2E_\sigma-W_\sigma\|_{2,d}^2 .
 \tag{21}
\]

这三个对象必须区别：q_σ是原actual residual；q_sq是先压缩
physical two-step再平方，仍在两个two-step之间保留一个P；
Φ_σ是没有W扣除的完整physical fourth。q_sq不是Φ_σ，
也不是完整实线residual ‖(B_H²−M_w)E_σ‖HS²/d。
本节不声称后一实线residual的比较；那还需要支付M_w的QP leakage。
不删除q_sq平方中的剩余投影。finite展开为

\[
 q_{{\rm sq},\sigma}-q_\sigma
  =2\tau(C_{H,\sigma}^2K_\sigma)-2\tau(W_\sigma K_\sigma)
                              +\tau K_\sigma^2 .
\]

所有非W项均非负，且是(15)正差的一部分，所以严格夹住未知增长：

\[
 -2M\lambda_H(\sigma)^2/d
 \le q_{{\rm sq},\sigma}-q_\sigma
 \le\Phi_\sigma-a_\sigma .                             \tag{22}
\]

没有粗暴乘未知Γ norm与o(1)，也不假定q bounded。
在共同good carrier上，(14)、(17)给

\[
 |q_{{\rm sq},\sigma}-q_\sigma|
       =O(\ell^{-2})+O(X^{-1})=o(1).                   \tag{23}
\]

这准确减少actual平方里一次P的成本。
q_sq仍含整个physical two-prime ratio covariance；
(23)只是已付桥，没有供给它的long-product signed upper。
不会把原W改成目标选择的center。

## 8. 零块接口、原fixed起点范围及旧材料的区别

H_T=T/sqrt ell=oT，d、ell、prime cutoff保持冻结。
E_σ对应的零点块为J_σ=[σ,σ+dh)，
padded block在两端再加sqrt T。
228的moving-start接口给
N(J_σ triangle [T,2T])=O((H_T+1)log T)=o(N)。
Poisson–Gabor identity只改共同modulation，原norm/inertia账本不变；
Archimedean与二矩须使用该来源的uniform moving-grid版本。
本稿不读取228旧fourth arithmetic前件，也不重证AF零侧分析内核。

因此可以在未来的同一zero-block证书中使用(14)的共同good载波；
但另一独立算术good point未必落在G_T。
若需同时选择，必须在选择前汇合相应非负defect或证明good-set交集，
不能先选arithmetic point，再声称它也满足(17)–(19)。
当前不存在已付的新whole arithmetic upper可以直接完成该最后一步。

旧223使用Hilbert-valued product-cluster的short signed/second averages；
本稿只读取其scalar MV定理，以真实raw summed prime multiplier
支付原outside-carrier leakage。
旧225的主要结论是某些Toeplitz boundary的signed first means，
其文本明确不从中推出mean absolute。
本稿(19)则直接给全部原raw high/low四词的mean absolute three-P差，
不使用其Henriot或旧product-cluster闭合。
与旧一般Jensen正差相比，本稿新增了实际平均能量付款，不主张重新发现(15)。

对原起点恰为σ=T，仍不能据平均免费推出(17)。
可用旧准确[Perron R]在固定good band的 y≪X^(a−1/2)ell、
真实leak≤y sqrt ell及463双侧高度，另得
0≤Φ_T−a_T≪_a X^(4a−3)ell⁴+O(X^−1 ell^−5)，
只在其既定a>max(θ,3/4)、a<1范围使用。
这个较小幂仍不是constant upper；本稿主结论(12)–(23)完全不用它。

## 9. 正 nearcore、真实进展与剩余付款

对原flat/MT endpoint-positive taper，旧restricted nearcore计数
在σ∈[T,T+H_T]仍统一成立：所有carrier频率≤5πX，
固定小δ使Re K_{d,σ}(log(pr/qs))≥1/2，
zero-extended五点窗口、原子权重和tuple计数均不改变。
所以其paired positive子和仍≫X/ell⁵。
这是restricted sum，永远不是wholephysical fourth的下界。

在本稿selected carrier上净positive compression gap为o(1)，
不能用它独立吞掉上述leading positive子和。
如果未来证明同一carrier的actual高四矩O(1)，(17)严格迫使整个
physical高四矩也O(1)：补集必须完成相应的净signed相消。
现有R早已证明大量physical补集相消，这不是本轮新算术结果。
新增的是全部内部P的whole absolute平均误差与合法共同good carrier准入。

剩余问题仍是471的atomic high two-product，pr/qs可长至X²，
以及相关31/22 long-product全signed预算。本稿不把(17)的
actual/physical接近本身当成这些未知量的上界，不提出小cap或数值Q。

在内存中另用rational selfadjoint 4×4 B与rank2 P核对(15)的SOS
和(22)的W夹界，精确通过。这个有限核对仅验证代数；
没有运行旧audit、改写输出或用有限模型认证素数渐近。
