# 固定实际 Sonin 投影、压缩逆与 Hilbert 向量 reader

2026-10-27；`/root/tf_projection_reader` 独占建设性预检稿。只执行STATE冻结的五源输入门，不改STATE／cadence／文献库，不建C047，不计算五源T矩阵或其符号。已恢复README／STATE、check→show、G20261027及next-input-admission；535／560已有的迹身份与有限Gram存在性不重计。

主线给**全Hilbert空间上的投影／逆误差证书**，用于兄弟分支的source-HS有限秩夹心；不把finite matrix residual当成Hilbert residual。533已付的低forcing裸求值另给可选的有费point reader，并非实际矩阵计算的必要路线。

## 1. 原物理对象与规范运输

在 \(\mathcal H=L^2((0,\infty),dx)\) 上固定

\[
 (U_t f)(x)=e^{-t/2}f(e^{-t}x),\quad
 (Ff)(x)=2\int_0^\infty\cos(2\pi xy)f(y)dy,
 \quad L=1_{(0,1)},\ H=I-L.
\]

F是self-adjoint unitary involution，\(FU_tF=U_{-t}\)。unitary log map为
\((Vf)(y)=e^{y/2}f(e^y)\)，故VU_tV^−1是translation y→y−t；physical source仍是原r=e^(u/2)f，不再给A_r多乘一个指数。于是

\[
 A_r=\int r(t)U_tdt,\quad \|A_r\|\le\|r\|_1,
 \qquad A_r(x,y)=\frac{r(\log(x/y))}{\sqrt{xy}}.
\]

Fourier约定为r̂(s)=∫r(t)e^(−ist)dt。若引入unitary inversion \((\mathcal Jf)(x)=x^{-1}f(1/x)\)，它在log坐标仅是reflection；F在该坐标不是裸reflection，而带真实Gamma相位

\[
 \widehat{VFf}(s)=m(s)\widehat{Vf}(-s),\quad
 m(s)=\pi^{is}\frac{\Gamma(1/4-is/2)}{\Gamma(1/4+is/2)}.
\]

Sonin载体 \(M=\ker L\cap\ker LF\)，其投影记P。Sonin cutoff1不是source半窗L_source=3/2。

## 2. P的既有公式与实际低区间证书

记 \(C_0=LFL\) 为 \(\mathcal H_0=L^2(0,1)\) 上的cosine compression，\(R_0=(I-C_0^2)^{-1}\)。原532／533已付

\[
 P=H-HFLR_0LFH. \tag{1}
\]

该式来源于 \((HFL)^*(HFL)=I_{\mathcal H_0}-C_0^2\)，不是省略第二边界的Wiener–Hopf代理。定性gap \(\|C_0\|<1\) 已有；本轮root另外给可复现的定量输入 [arch-gap-certificate.json](arch-gap-certificate.json)及[scripts/tf_reader_arch_gap_certificate.py](../../../scripts/tf_reader_arch_gap_certificate.py)。

其数学结构已独立核对。令

\[
 C_N(x,y)=\sum_{n=0}^N c_nx^{2n}y^{2n},\quad
 c_n=\frac{2(-1)^n(2\pi)^{2n}}{(2n)!},\qquad
 \delta_N=\frac{2(2\pi_{hi})^{2N+2}}{(2N+2)!}.
\]

real-variable Taylor remainder给

\[
 \|C_0-C_N\|\le\|C_0-C_N\|_{HS}\le\delta_N. \tag{2}
\]

这既控制整个低方形的kernel，也控制无限维operator residual。令E将系数送到Σa_nx^(2n)，H_N=E*E，其entries为1/(2i+2j+1)，D_N=diag(c_n)，则C_N=ED_NE*。由congruence，\(aH_N^{-1}\pm D_N\succ0\) 等价于 \(\|C_N\|<a\)。root固定N=20证书以Machin arctan有理π enclosure、向外整数interval LDL验证两符号正定，并以(2)运输到真实C0。它给

\[
 \|C_0\|\le\bar\kappa_0<1,\qquad
 1-\bar\kappa_0^2>10^{-6},\quad \|R_0\|<M_0:=10^6. \tag{3}
\]

这里\(\bar\kappa_0\)使用JSON的actual operator_norm_upper，不将\(\|C_N\|\)直接当实际norm。本轮JSON已含gram_inverse_exact_identity_verified=true，脚本逐entry以exact rational算术验证HHinv=I；LDL的每个正下端是证书，不是浮点eigenvalue。此项为投影输入，不是T_F／Weil矩阵数值试验。

## 3. 任意精度的R0／P全空间近似

以下N可以精度细化，数学source／F／假设均不改变。取N使 \(\kappa_N:=\bar\kappa_0+\delta_N<1\)，定义

\[
 R_N=(I-C_N^2)^{-1},\quad M_N=(1-\kappa_N^2)^{-1},\quad
 \eta_N=M_0M_N\delta_N(\bar\kappa_0+\kappa_N).
\]

resolvent identity与(2)直接给

\[
 \|R_0-R_N\|\le\eta_N. \tag{4}
\]

R_N不是把无穷维inverse换成某个未经检查的有限inverse：它在span{1,x²,…,x^(2N)}的正交补上恰是I，有限rank correction完全显式。若ξ=E*f，则

\[
 R_Nf=f+E (I-D_NH_ND_NH_N)^{-1}D_NH_ND_N\xi.
\]

定义真正全空间bounded operator

\[
 P_N=H-HFLR_NLFH.
\]

因为F/L/H都是contractions，

\[
 \|P-P_N\|\le\eta_N=:e_P,\quad \|P_N\|\le1+e_P. \tag{5}
\]

P_N一般不是正交投影；它只作带误差的reader，不能用其有限矩阵幂等性／positive eigenvalues代替(5)。本式包含真实F的全physical action，没有finite-domain residual偷换。

## 4. 固定8素数的完整Gram逆／Π_F

F_source集合固定为{2,3,5,7,11,13,17,19}，以下为避免与cosine F混名记该集合为\(\mathcal P\)。令

\[
 B=\prod_{p\in\mathcal P}(I-p^{-1/2}U_{\log p}),\quad
 W=B^*B,\quad m=\prod_p(1-p^{-1/2}),\quad M_+=\prod_p(1+p^{-1/2}),
\]
\[
 d=m^2,\quad u=M_+^2,\quad c=(u+d)/2,\quad
 \rho=(u-d)/(u+d)<1,\quad A=I-W/c.
\]

所有积为明确finite数，dI≤W≤uI、||A||≤ρ；B有界可逆而非unitary。actual G=(PWP)|_M，

\[
 \mathcal R=P G^{-1}P
 =c^{-1}\sum_{j\ge0}Q^jP,\quad Q=PAP,\qquad
 \Pi=B\mathcal R B^* . \tag{6}
\]

\(Q^0P=P\)；本式没有把G的inverse无说明扩到range外。\(\|\mathcal R\|\le d^{-1}\)，\(\Pi\)是BM的真实正交投影。

用(5)构造 \(Q_N=P_NAP_N\)，则

\[
 e_Q:=\|Q-Q_N\|\le\rho e_P(2+e_P),\qquad
 \|Q_N\|\le\beta:=\rho(1+e_P)^2.
\]

选择N使β<1总能做到；这是fixed集合的有费条件，不是成长uniform gap。对inverse级数截到J，置

\[
 \mathcal R_{N,J}=c^{-1}\sum_{j=0}^J Q_N^jP_N.
\]

power telescoping给真正global operator bound

\[
 \|\mathcal R-\mathcal R_{N,J}\|\le
 \underbrace{d^{-1}\rho^{J+1}}_{\text{完整逆谱尾}}
 +c^{-1}\left[e_P\sum_{j=0}^J\rho^j
 +(1+e_P)e_Q\sum_{j=1}^Jj\beta^{j-1}\right]
 =:e_{\mathcal R}. \tag{7}
\]

所以

\[
 \|\Pi-B\mathcal R_{N,J}B^*\|\le M_+^2 e_{\mathcal R}. \tag{8}
\]

允许再将右侧近似operator取self-adjoint part，误差不增。近似operator本身不保证正或投影，不能先用“positive T”过滤掉不利的误差。此证书保完整G，未用B P B*、receiver w_R、finite word符号或joint裸核HS假设代替它。

给定desired tolerance，先选J令第一项小，再选N令另外两项小，均有明确有限停止准则。ρ靠近1时J可能极大；有限性与实用成本分开，本稿不声称已经高效实现或计算了本五源矩阵。

## 5. Π对有限Hilbert输入确可计算，而非仅抽象operator式

与source-HS分支衔接时，只需Π对有限piecewise-smooth compact向量／log-cell向量的matrix elements。以下步骤给可验证的实际action，而不是输出有限矩阵后声称残余小。

* L/H cutoff、unitary dilation以及finite B/B*具有直接全空间norm控制；每次输入近似误差按相应operator norm运输。
* 对compact piecewise polynomial输入，cosine Fourier积分可用逐区间trigonometric primitives计算。若输入f在各区间C¹、总variation含jumps为V_f，则一次分部积分给 \(|Ff(x)|\le V_f/(\pi x)\)（可把端点项计入V_f），因此外部L²尾≤V_f/(π√X)。这付的是实际Ff尾，不是有限Fourier矩阵residual。
* 有理log-cell输入在正的compact x区间上为已知x^(-1/2)函数。其piecewise polynomial逼近的L²误差可由区间sup导数／mesh上界付款；F的unitarity使输入误差在**整个**输出半线保持。再对polynomial transform付上条tail与compact quadrature误差。
* R_N=I+finite rank correction只需要低区间moments及固定有理／π矩阵线性代数；区间矩阵逆误差、每个moment quadrature误差另记入action ledger。再经(7)–(8)闭合真实operator误差。

有限次数operator复合的误差可用 \(\|T_1\cdots T_k-\widetilde T_1\cdots\widetilde T_k\|\) 的逐位置telescoping，或逐vector norm递推付款。不得只测试当前finite basis上的residual，再当成(7)/(8)的全Hilbert结论。F的严格unitarity和(2)/(4)保证这里每个遗漏项都已有global输入；具体实现仍须写出所选mesh、matrix inverse enclosure及其实际误差值。

## 6. source-HS有限rank路线的support核对

兄弟分支使用 \(D_r=1_{[a,\infty)}A_rF1_{[b,\infty)}\)，其中a=e^(−3/2)、b=1/∏p。其support方向正确：g∈M时g与Fg都在[1,∞)，Bg仍在[1,∞)，而FBg=B*Fg；B*的finite negative delays只会把下端降到b。因此

\[
 1_{[b,\infty)}F\Pi=F\Pi,\qquad
 1_{[a,\infty)}A_r\Pi=A_r\Pi,
 \qquad D_rF\Pi=A_r\Pi. \tag{9}
\]

source矩阵仍按原linear-first定义：T_ij=Tr(A_riΠA_rj*)，组合c的值为c^T T barc。若实现采用column/conjugate-first c*G c，须把T／Q／E／原norm四表同时transpose，不只换一张表。单个self-adjoint quadratic值不受此坐标转置影响。

在source-HS全尾已付后，有限rankD_r近似将T矩阵降为有限个 \(F\Pi F\) 的Hilbert-vector matrix elements；(8)正好支付所需operator误差。由此不需要把非Hilbert plane wave截成一段后凭空声明pointwise density已准，也不需要把A_r本身当HS。

## 7. 可选的实际裸求值reader：低forcing正则化

这一段把533已有实际k_s的构造变成明确尾界，供独立核对，不是另一个数学输入。令

\[
 e_s(x)=x^{-1/2+is}/\sqrt{2\pi},\quad \gamma_s=m(-s),\quad
 r_s=\gamma_sLe_{-s}-C_0Le_s\in L^1(0,1),
 \quad \|r_s\|_1\le R_*:=6/\sqrt{2\pi}.
\]

全e_s并非Hilbert向量，不能直接代P。合法构造为

\[
 z_s=R_0C_0^2r_s=C_0R_0C_0r_s,\quad
 w_s=z_s-C_0Le_s,\quad
 k_s=H[e_s-F(\gamma_sLe_{-s}+w_s)]. \tag{10}
\]

这里C_0r_s∈L²，w_s smooth；使用核row的L²界，对j≥0有

\[
 \|w_s^{(j)}\|_\infty\le
 \frac{4(2\pi)^jM_0R_*}{\sqrt{2j+1}}
 +\frac{2(2\pi)^j}{\sqrt{2\pi}(j+1/2)}=:W_j. \tag{11}
\]

homogeneous Fourier identity Fe_−s=γ_−s e_s精确取消power腿。对剩余高半线power积分和低区间smooth积分各作一次IBP，得到对全部real s、x≥1的可用粗界

\[
 |k_s(x)|\le\frac{C_s}{x},\quad
 C_s=\frac{1+2\sqrt{1/4+s^2}}{\pi\sqrt{2\pi}}+\frac{W_0+W_1}{\pi},
 \quad \|k_s\|\le C_s,\quad
 \|1_{(X,\infty)}k_s\|\le C_s/\sqrt X. \tag{12}
\]

这是点求值的**特定Riesz向量**，不是任意Sonin L²向量的point bound。它不使用高频Γ载波替换低频，亦不丢掉s=0附近。

若 z_s以 \(z_{s,N}=R_NC_N^2r_s\) 近似，利用L¹→L²的uniformkernel remainder及(4)，有

\[
 \|z_s-z_{s,N}\|_2
 \le R_*\left[2\eta_N+M_N\delta_N(2+\kappa_N)\right]=:e_k.
 \tag{13}
\]

以(10)替换z后给global Hilbert误差≤e_k；这是因为差仅为HFL(z−z_N)，不是比较两个非Hilbert power。全部forcing moments可直接算：

\[
 \int_0^1 t^{2n}r_s(t)dt
 =\frac{\gamma_s}{\sqrt{2\pi}(2n+1/2-is)}
 -\frac1{\sqrt{2\pi}}\sum_{j\ge0}
 \frac{c_j}{(2n+2j+1)(2j+1/2+is)}.
\]

级数绝对factorial收敛，可用与(2)同一Taylor remainder付款；不需要在t=0对oscillatory singular power作未经估计的quadrature。Γ相位区间误差及有限线性代数误差仍须加到e_k，不能由本式自动省略。

真实density为 \(\rho_{\mathcal P}(s)=|b_{\mathcal P}(s)|^2\langle k_s,\mathcal R k_s\rangle\)。若k近似误差≤e_k、\(K=\|k_s\|\le C_s\)、\(K_N\le C_s+e_k\)，用(7)的reader可付

\[
 |\rho_{\mathcal P}(s)-|b_{\mathcal P}(s)|^2
       \langle k_{s,N},\mathcal R_{N,J}k_{s,N}\rangle|
 \le M_+^2\left[e_{\mathcal R}K_N^2+d^{-1}(K+K_N)e_k\right].
\]

同时 \(0\le\rho_{\mathcal P}(s)\le(M_+^2/d)C_s^2\)，是明确至多quadratic的全球upper，足够结合固定C∞源的高阶Fourier尾作有费积分。它比已付sharp Γ/log高频界粗，不作新whole改善。

## 8. root消费范围／strongest-old净值

主对象是fixed cutoff1的真实cosine P、fixed8-prime B/G/Π及有限Hilbert输入；原source通过V/A_r保持同一physical normalization。全space残差由cosTaylor kernel／resolvent和full spectral tail给出，physical Fourier action用unitarity与有端点尾的输入逼近付款。没有ambientjoint裸核HS假设，也没有有限残差偷换。

532／533已给P和正则化k_s、535已闭ordinary smooth source trace、560已给全fixed窗正迹及C0紧误差，这些不重计。新增用途限把本次被冻结输入的reader与实际误差路线落实；是否形成完整新研究迭代由root对齐source-HS／矩阵误差后判断，本稿不自行计轮。

没有计算本次5×5 T/E、没有认证Hfin、没有经典正性／cofinal core或coupling结论。固定集合的d、ρ、M0／MN及J成本全部保留，不能升级成长uniform读出；全Γ/contact、properpowers／双pole仍由原完整Q与兄弟分支的同源比较承担。无新primitive／mixedRR或whole leading4/5后果，Goal完成门不因此通过。
