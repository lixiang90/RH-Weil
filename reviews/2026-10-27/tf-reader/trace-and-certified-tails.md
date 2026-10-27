# 五源 actual t_F：physical HS 夹心、全尾及真实 Hilbert residual

2026-10-27；`/root/tf_trace_tail`独占建设性预检稿，不改STATE／cadence／文献库，不建数学合同，不运行浮点矩阵实验。已恢复README／STATE、check→show、G20261027与冻结的next-input-admission；C046／583、535、560、570均为输入。以下给同一固定F及五源的独立正迹读出，绝不以Q加unknown误差反定义T。

## 1. 原对象与两个真实支撑

物理空间为H=L²(R_+,dx)，

\[
 (U_t f)(x)=e^{-t/2}f(e^{-t}x),\qquad
 (\mathcal Ff)(x)=2\int_0^\infty\cos(2\pi xy)f(y)dy.
\]

F为unitary self-adjoint cosine transform。令P为cutoff1的实际Sonin投影：M=RanP的f与Ff都在(0,1)消失。

本文内部Hilbert记号统一采用conjugate-first：`<f,g>_H=∫bar(f)g`，所以V* A^−1 V等compression／residual矩阵是通常column-Gram。冻结的source表却保原linear-first：N_ij=∫r_i bar(r_j)、T_ij=Tr(A_i Pi A_j*)。若r=Σc_jr_j，source二次型为c^T T bar(c)，不是c* T c；通常column-vector实现必须将全部N／Q／T／E一起transpose。下面(13)通过row coefficients c_(i,alpha,beta)保留这个方向，不能只将某一表共轭。

本轮冻结

\[
 F_0=\{2,3,5,7,11,13,17,19\},\quad
 N_F=\prod_{p\in F_0}p=9699690,
\]
\[
 B=\prod_{p\in F_0}(I-p^{-1/2}U_{\log p}),\quad
 G=(PB^*BP)|_M,\quad \Pi=BP G^{-1}PB^*.
 \tag{1}
\]

这里Pi是实际orthogonal projector onto BM。记m=∏(1−p^−1/2)、M_+=∏(1+p^−1/2)、d=m²、D=M_+²，有dI≤G≤DI。原物理源A_r=∫r(t)U_tdt，五源r_j及其L=3/2参数一律不变。

两个支撑事实支付后面的全部物理尾。首先BM中每个函数在x<1消失，因为B的有限Euler展开只有U_logn，n≥1。其次

\[
 \mathcal F B=B^*\mathcal F
 =\prod_{p\in F_0}(I-p^{-1/2}U_{-\log p})\mathcal F.
\]

故F(BM)在y<b:=N_F^−1消失。B*的最大负平移是−log N_F；不能误把Fourier侧下界仍写成1。此处只有有限Euler numerator；全returns仍在G^−1，未截断。

五源support为[-L,L]、端点flat；A_r把支撑[1,∞)送到[a,∞)，其中a=e^−L。因此

\[
 D_r:=1_{[a,\infty)}A_r\mathcal F1_{[b,\infty)},\qquad
 A_r\Pi=D_r\mathcal F\Pi.
 \tag{2}
\]

这是exact operator identity；两个指标cutoff均来自实际支撑，不是receiver/window模型。

## 2. 显式 Hilbert–Schmidt 核与全部 physical 尾

在x≥a、y≥b上，D_r的核为K_r(xy)，其中

\[
 K_r(z)=2\int_{-L}^{L}r(t)e^{-t/2}\cos(2\pi ze^{-t})dt
       =2\int_{e^{-L}}^{e^L}w_r(v)\cos(2\pi zv)dv,
\quad w_r(v)=r(-\log v)v^{-1/2}.
 \tag{3}
\]

w_r为该闭v区间上端点flat的smooth函数。定义可明确上界的常数

\[
 C_{r,n}=\frac{2\|w_r^{(n)}\|_1}{(2\pi)^n},\qquad
 J_{r,n}=\frac{4\pi\|(v w_r)^{(n)}\|_1}{(2\pi)^n}.
 \tag{4}
\]

分部积分没有endpoint remainder，对任意z>0，

\[
 |K_r(z)|\le\min(C_{r,0},C_{r,n}z^{-n}),\qquad
 |K_r'(z)|\le\min(J_{r,0},J_{r,n}z^{-n}).
 \tag{5}
\]

这些不是待定unknown norms：w及导数由冻结的chi、j显式给出，可用源稿的全导数majorant直接上界。具体地，若R_k≥||r^(k)||∞，且a_(n,k)为∏_(ell=0)^(n−1)(X+ell+1/2)的系数，则

\[
 \|w^{(n)}\|_1\le(e^L-e^{-L})e^{(n+1/2)L}
                    \sum_{k=0}^n a_{n,k}R_k.
 \tag{6}
\]

这是w^(n)=(-1)^n v^(-n−1/2)∏(D_t+ell+1/2)r(t)的直接链式法则。对v w使用∏(X+ell−1/2)的系数绝对值及保守因子e^((n+1/2)L)，给J的同样显式上界。只需有限阶n=2即可付下述尾，增加阶数不是新source或新数学合同。

令c=ab。变元z=xy给exact HS norm

\[
 \|D_r\|_{S_2}^2
 =\int_c^\infty |K_r(z)|^2\log(z/c)dz<\infty.
 \tag{7}
\]

本冻结c<1时，一个可用的完整上界是

\[
 H_r^2:=C_{r,0}^2[\log(1/c)-1+c]
         +C_{r,1}^2[1+\log(1/c)].
 \tag{8}
\]

没有把A_r本身说成HS；HS的是含真实双支撑的D_r。故后续opnorm projection误差可以合法夹在HS两边，避开“opnorm误差乘非HS A_r便给trace误差”的漏洞。

截断到[a,X]×[b,Y]，只要Xb≥1且aY≥1，遗漏HS²由行／列tail的union bound给

\[
 \delta_{r,\mathrm{tail}}^2
 \le\frac{C_{r,n}^2}{(2n-1)^2}
       [(Xb)^{1-2n}+(aY)^{1-2n}],\qquad n\ge1.
 \tag{9}
\]

因为∫_h^∞z^(-2n)log(z/h)dz=h^(1−2n)/(2n−1)²。也可在unitary log coordinates xi=log x、eta=log y中取矩形

\[
 -L\le\xi\le\log N_F+R,\qquad
 -\log N_F\le\eta\le L+R,
\]

使两个h都为e^R，tail²≤2C_(r,n)²e^(-(2n−1)R)/(2n−1)²。无unbounded physical interval被默默删掉。

## 3. 有限 rank 近似：mesh 和系数误差也明确付款

log-unitary kernel是

\[
 \widetilde K_r(\xi,\eta)=e^{(\xi+\eta)/2}K_r(e^{\xi+\eta}).
\]

它只依赖s=xi+eta。由(5)，两个偏导在全R²有统一上界

\[
 M_r=\max\{C_{r,0}/2+J_{r,0},\ C_{r,2}/2+J_{r,2}\}.
 \tag{10}
\]

s≤0用第一个界，s≥0用n=2衰减。取上述log矩形上orthonormal normalized cell indicators g_alpha(xi)、h_beta(eta)，mesh宽≤h_xi、h_eta；cell midpoint核值给一个真实有限rank D_r^(h)。若每个kernel coefficient再有pointwise误差≤epsilon_r，面积记A_R，则

\[
 \|D_r-D_r^{(h)}\|_{S_2}
 \le\delta_{r,\mathrm{tail}}
    +\sqrt{A_R}[M_r(h_\xi+h_\eta)+\epsilon_r]
 =:\delta_r.
 \tag{11}
\]

这是核在真实Hilbert空间的S2误差，不是一个离散matrix residual。K_r的pointwise系数可用(3)的有限v区间积分和已付w导数进行带界quadrature。必要时先用(5)在大z处取含0的绝对小enclosure；不要求解析所有巨大oscillation。每项均有显式趋0参数。

## 4. 原正迹降成有限 compression，不以Q反定义

令R_P=F Pi F，是positive contraction／orthogonal projector。由(2)，全部五源有

\[
 T_{ij}=\operatorname{Tr}(A_{r_i}\Pi A_{r_j}^*)
       =\operatorname{Tr}(D_i R_P D_j^*).
 \tag{12}
\]

有限rank近似可共用输出cell和输入cell：D_i^(h)=Σ_(alpha,beta)c_(i,alpha,beta)|g_alpha><h_beta|。因此只须读有限compression

\[
 Q_{\beta\gamma}^{\Pi}
   =\langle h_\beta,R_P h_\gamma\rangle,\qquad
 T_{ij}^{(h)}=\sum_{\alpha,\beta,\gamma}
 c_{i,\alpha\beta}\overline{c_{j,\alpha\gamma}}
 Q_{\beta\gamma}^{\Pi}.
 \tag{13}
\]

这里Q^Pi_beta,gamma采用本稿内部conjugate-first Hilbert约定，与source表不同；(13)的c_i Q^Pi bar(c_j)使最终T仍linear in r_i、conjugate-linear in r_j。若实现改换约定须将全部源表及坐标transport一起处理。HSideal估计给

\[
 |T_{ij}-T_{ij}^{(h)}|
 \le\delta_i H_j+(H_i+\delta_i)\delta_j.
 \tag{14}
\]

若compression还有opnorm误差delta_Q，则再加
||(c_i)||_F||(c_j)||_F delta_Q，其中Frobenius norms正是有限rank的S2 norms。通过operatornorm=1的R_P付款，不需虚构ρ_F的uniform频段上界。

这里没有对source作Fourier截断，所有source frequency尾均已精确编码在(3)的compact物理积分中。正迹侧因此没有未计的“低模式其实有高频”误差。若root改用点密度bandreader，则必须另消费源稿的rhat高频界，不能将本方案的无frequency截断拿来免除另一方案的频尾。Q／Dlog的独立Fourier quadrature仍由源稿单独付款。

## 5. full inverse 的真实 Hilbert residual，而非finite matrix residual

在整个H上置

\[
 \mathcal A=P B^*B P+(I-P),\qquad dI\le\mathcal A\le DI,
 \quad v_\beta=P B^*\mathcal Fh_\beta.
 \tag{15}
\]

这里d=m²<1、D=M_+²>1，因此无需在未知M上选择数值basis；A在M上是G，在M正交补上是I。exact compression为

\[
 Q_{\beta\gamma}^{\Pi}
 =\langle v_\beta,\mathcal A^{-1}v_\gamma\rangle.
 \tag{16}
\]

令V为这些列，Z为任何实际Hilbert trial列，R_res=V−A Z。定义Hermitian variational matrix

\[
 J(Z)=V^*Z+Z^*V-Z^*\mathcal A Z.
\]

有exact、含全部returns的证书

\[
 Q^\Pi-J(Z)=R_{res}^*\mathcal A^{-1}R_{res},\qquad
 0\le Q^\Pi-J(Z)\le d^{-1}R_{res}^*R_{res}.
 \tag{17}
\]

所以一列真实residual的Hilbert norm界eta_beta给entry误差≤d^−1 eta_beta eta_gamma，全矩阵opnorm误差≤d^−1Σ eta_beta²，再加J本身的integration／rounding enclosure。不得将finite-section残差替换为这里的R_res。

## 6. 为什么这些全空间向量／residual能有效计算

所需不是裸的density argument，而是下述带误差的closure：

1. **Dense trial vectors。** 有限physical step functions以已知L2误差逼近输入。logcell h_beta在physical坐标为normalized x^−1/2 1_[u,v]，u>0、v<∞；其导数有明确有界，有限mesh给可认证L2逼近，不把它原样误称physical step。
2. **实际cosine transform。** 对v=Σc_l 1_[a_l,b_l]，

\[
 (\mathcal Fv)(x)=\sum_l c_l
 \frac{\sin(2\pi b_lx)-\sin(2\pi a_lx)}{\pi x}.
\]

若C=sum|c_l|、M=sum|c_l|(b_l−a_l)，则x≥X的L2 tail²≤4C²/(π²X)，x≤delta的tail²≤4M²delta。在[delta,X]上显式导数界加mesh付款；sin／pi有向舍入。由于F unitary，输入step近似误差原样运输，不产生未知tail。
3. **Cutoff与dilation。** L=1_(0,1)、H=I−L为contraction，可精确切分step端点。U_logn及其adjoint只缩放端点、乘代数幅度，有限B／B*的误差由∏(1+p^−1/2)付款。对于带有向enclosure的端点，另外以interval对称差长度支付L2误差。
4. **实际Sonin P。** 使用投影分支的原双cutoff公式P=H−H F L R0 L F H，R0=(I−K0²)^−1、K0=L F L。root现有 `arch-gap-certificate.json` 与脚本给固定cutoff1的d0=1−||K0||²>10^−6、||R0||<10^6的operator证书。R0用Σ_(ell=0)^N K0^(2ell)的尾≤(1−d0)^(N+1)/d0；其余各因子norm≤1。有限词上的向量误差逐算子传播，故P作用的真实全H误差可任意缩小。gap证书是独立输入，不是本稿重新认证它的区间运算实现。
5. **全G逆与returns。** 对c_A=(D+d)/2、rho=(D−d)/(D+d)<1，有

\[
 \left\|\mathcal A^{-1}-\frac1{c_A}
 \sum_{\ell=0}^N(I-\mathcal A/c_A)^\ell\right\|
 \le\rho^{N+1}/d.
 \tag{18}
\]

也可使用任意较好的trial Z，再由(17)直接验收。实际A Z运算按前四项在全H中产生带L2误差的step enclosure；若残差近似r_h的误差≤epsilon，则真实norm≤||r_h||+epsilon。故(17)不是“求解一个有限matrix所以residual小”。所有returns由(18)的全operator尾或真实residual覆盖，未引入有限word代理等式。

这些操作的误差输入均显式、可合并、可趋0，给一个有限但可能昂贵的计算流程。d很小和d0保守会导致巨大成本；证明存在收敛证书不等于已实现一个现实成本的5×5数值表。本稿未运算该表，未断言Hfin的符号。

## 7. 总账、覆盖与strongest-old净值

对每对源，用(11)、(14)与(17)合并即可给Tentry的明确误差：physical无限行列尾、logcell有限rank／scalar quadrature、全部F/P/global inverse向量误差、variational J rounding及true residual。没有sourcefrequency clipping；若选另一band方案则另付频尾。正迹矩阵本身与Q无关，仅比较E=T−Q时才使用源稿的完整Γ/contact、全部q<e³ properpowers和pole-zero的准确公式；不能把primenum、Γ渐近或pole删除用于定义T。

原du／Dlog Gram和crossblock的坐标transport由源稿保；这里有限输入cell dimension与最终5源dimension不同，不把cell Euclidean metric当原r norm。最终Hermitian E的normalized spectral误差还须包含N误差／condition；本稿只提供T侧。

fixed F8、fixed L3/2及冻结5源是全部量词。不能从可任意精度求这个表外推ALLsource／成长L、相应补空间／coupling、独立primitive RR或经典正性。全Γ/powers/poles仍在目标；Σd0／d成本不是actual signed error的必要增长下界。

与最强旧比较：535／560已付trace域与abstract finite Gram；(2)–(18)给一个具体source-adapted可计算的physical HS／true-residual证书，但不改善whole leading4/5负惯性UPPER，也不移除actualq/core/coupling/Ξ或mixedRR瓶颈。它是否仅作标准旧设施的建设性0轮实现、或因root后续实际消耗产生新数学迭代，由root按共同原稿净值统一判断；本稿不以文件／证书数量强行计轮，不建C047。
