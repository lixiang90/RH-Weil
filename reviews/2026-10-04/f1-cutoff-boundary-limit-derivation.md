# 原壳层截止的边界极限、统一算子界与正角有限部

2026-10-04。独立推导，依据[412](../../notes/412-f1-transverse-compression-and-periodic-traces.md)、[414](../../notes/414-f1-deep-boundary-unitary-and-time-defect.md)、[419](../../notes/419-f1-original-time-crossed-product-and-trace-interface.md)、[422](../../notes/422-f1-radial-finite-part-and-corner-anomaly.md)、[423](../../notes/423-f1-twisted-radial-readout-and-mixed-period-obstruction.md)。仅研究实际算子与拓扑，不把零交换异常的数值序列解释成非零极限。以下直接证明可复用估计与比较；未形式化，尚需独立验收。

## 1. 显式投影、壳层与Fréchet增长

对任意一位r，记D=log r、ρ=r^(-1/2)、c=(1−ρ²)^(1/2)，令λ_a e_j=e_(j+a)。414原物理群表示使用此λ方向；412的V_a对应λ_(−a)。

\[
b_N=c\sum_{m\ge0}\rho^m e_{N+m},\qquad
R_N=\sum_{j=-N}^{N-1}|e_j\rangle\langle e_j|+|b_N\rangle\langle b_N|.
\tag{1}
\]

由b_N=ce_N+ρb_(N+1)，置

\[
w_N=\rho e_N-cb_{N+1},\qquad
S_N=|e_{-N-1}\rangle\langle e_{-N-1}|+|w_N\rangle\langle w_N|.
\tag{2}
\]

这准确等于R_(N+1)−R_N：两个新增方向正交，w_N与b_N正交；w_N=λ_Nw_0，支撑j≥N。

对径向矩阵设W_k(F)=Σ_(m,n)(1+|m−n|)^k|F_(mn)|。固定差m−n先求几何和得

\[
W_k(R_N)=2N+B_k(\rho),\qquad
B_k(\rho)=1+2\sum_{d\ge1}(1+d)^k\rho^d.
\tag{3}
\]

特别地B_0=(1+ρ)/(1−ρ)。S_N的W_k与N无关，因为两个投影支集不交且w_N仅平移；尤其

\[
\|w_0\|_{\ell^1}=1+2\rho,\qquad
W_0(S_N)=1+(1+2\rho)^2=:S(\rho).
\tag{4}
\]

两位E_p=R_(N_p,p)⊗S_(N_q,q)、E_q=S_(N_p,p)⊗R_(N_q,q)，原C_N=E_p⊗M_(d_p)+E_q⊗M_(d_q)。E_pE_q=0，故

\[
\|C_N\|=\max(\|d_p\|_\infty,\|d_q\|_\infty).
\tag{5}
\]

对422中B(L²_t)值乘子Fréchet半范数记m_k，则

\[
\begin{split}
m_0(C_N)&\le\|d_p\|_\infty(2N_p+B_0(\rho_p))S(\rho_q)\\
&\quad+\|d_q\|_\infty S(\rho_p)(2N_q+B_0(\rho_q)),\\
m_0(C_N)&\ge2\max\{(2N_p+1)\|d_p\|_\infty,\,
                         (2N_q+1)\|d_q\|_\infty\}.
\end{split}\tag{6}
\]

下界只用零径向Fourier系数：每个C_N(m,m)是正时间乘法算子，Σ_m(E_p)_(mm)=2(2N_p+1)，在同一时间点取d_p接近上确界，q同理。上界由绝对矩阵和给出；更高m_k也有线性N上界，常数依赖k,p,q及固定分割，用(1+x+y)^k≤(1+x)^k(1+y)^k分解张量权即可。

所以原截止算子范数统一，但原Fréchet预算确实发散。裸C_N不在422的S₁时间代数𝓐中。

## 2. 原未重心截止没有非零边界极限

每个固定e_j最终被S_N严格消去，故C_N及C_N*在原Hilbert空间强趋于0。Π_N亦强趋于0。各固定N的普通边界像为0，不能从这条零数值序列声称非零极限。

在开放理想𝔍⊗K_t的乘子代数B(ℋ)中，统一有界的strong*收敛给strict收敛到0：对有限秩算子先验证，再逼近任意紧算子。

在完整原时间交叉积𝔅=𝔠⊗K_t的乘子拓扑中，C_N却不strict趋于0。取原Q=H(j)H(k)及时间秩一投影P_ξ，||ξ||=1、M_(d_p)ξ≠0。b_(N_p,p)⊗w_(N_q,q)在Q及E_p像内，被E_q消去，因此

\[
\|C_N(Q\otimes P_\xi)\|\ge\|M_{d_p}\xi\|>0.
\tag{7}
\]

这是完整源上的具体非一致性，与强极限0相容。任何完整源strict极限都必须在非退化表示中强趋于同一个0，故原C_N没有另一完整源strict极限。

单独R_N强趋于1，而普通边界像为0，展示商映射不保持表示强拓扑；它不能倒换成含强趋零壳层的原C_N极限。

## 3. 实际采样因子给全部N的统一算子界

先仅作形式记号

\[
(\Omega\phi)_{j,k}(t)=\phi(t-jL-kM),\qquad L=\log p,\ M=\log q.
\]

Ω本身没有被定义为到全Hilbert空间的有界算子。压缩后的K_N=C_NΩ却有独立的有界定义：在E_p、E_q的有限正交基上，逐个取ℓ¹基向量的时间平移卷积，再乘时间分割。每个级数由Minkowski不等式在L²中收敛。

壳层w_N的卷积是平移乘下列Blaschke酉元：

\[
\mathcal W_r=\frac{\rho_r-\mathsf T_{\log r}}
                   {1-\rho_r\mathsf T_{\log r}},\qquad
\|\mathcal W_r\phi\|_2=\|\phi\|_2.
\tag{8}
\]

逆分母由算子范数收敛的几何级数定义；Fourier乘子的模恒为1，直接证明酉性。球b_N卷积为平移乘c_r(1−ρ_r𝕋_(log r))^(-1)，范数至多√B_0(ρ_r)。

E_p的环带基e_j由真实平方分割给

\[
\sum_j\int d_p(t)^2|\psi(t-jL-a)|^2dt\le\|\psi\|_2^2,
\tag{9}
\]

求和可取任意子集、a任意。球方向用d_p上确界及球卷积范数。q壳层的两个正交方向各给相同界；E_q同理，两个通道再正交相加，得

\[
\boxed{\ \|K_N\|^2\le C_*
=4+2\|d_p\|_\infty^2B_0(\rho_p)+2\|d_q\|_\infty^2B_0(\rho_q).\ }
\tag{10}
\]

这是与N无关的真实采样界；平方分割还给各d上确界≤1。没有给稠密Γ时间长度虚构共同基本区间。

矩阵核比较给

\[
A_N(h)=K_NU(h)K_N^*,\qquad \|A_N(h)\|\le C_*\|h\|_1.
\tag{11}
\]

先在有限径向、紧支时间输入上核对：ΩU(h)Ω*形式核为h(t−t′−ℓ_m+ℓ_n)，恰为每个径向矩阵元唯一g=m−n的原Γ项。C_N基向量ℓ¹与时间紧截止保证压缩核展开合法；414的绝对迹范数和确认它就是既有A_N，再以(10)延拓。

原未重心A_N(h)因此实际也strong*趋于0。有限径向输入最终被C_N消去，故A_N在这些输入上最终严格为0；(11)将它扩张到全空间。伴随使用h*(s)=overline(h(−s))。

它一般不在算子范数中趋零。对N_p≥2，将输入、输出分别压到
\(e_{0,p}\otimes w_{N_q,q}\)、\(e_{1,p}\otimes w_{N_q,q}\)的时间副本。
q波形的全部平移内积为δ_(b=0)，p环带矩阵元强制a=1，E_q的输入为0，故这一实际块准确为
\[
M_{d_p}\mathsf T_LU(h)M_{d_p}.
\tag{11a}
\]
其迹为Lh(−L)。若h(−L)≠0，则块非零，给与N无关的正算子范数下界。

这准确展示强拓扑不保持迹：h支集靠近−L、h(−L)=1、h(0)=0时，A_N(h)strong*趋于0，而(1/2)TrA_N(h)=Lρ_p恒定非零。非零的是不同算子的既有迹读出，不是零标量序列的极限。

## 4. 双正重心的真实正角

令Z_N=λ_(−N_p,p)⊗λ_(−N_q,q)⊗1。它是419新交叉积的真实乘子酉元，与P_g、U(h)交换。设

\[
R_r^-=\mathbf1_{j<0}+|b_{0,r}\rangle\langle b_{0,r}|,\quad
R_{K,r}^-=\sum_{j=-K}^{-1}|e_j\rangle\langle e_j|
                         +|b_{0,r}\rangle\langle b_{0,r}|,\quad
W_r=|w_{0,r}\rangle\langle w_{0,r}|.
\tag{12}
\]

显式恒等式为

\[
\lambda_{-N}R_N\lambda_N=R_{2N}^-,\qquad
\lambda_{-N}S_N\lambda_N=|e_{-2N-1}\rangle\langle e_{-2N-1}|+W.
\tag{13}
\]

R_K^- strong*趋于R^-，重心壳层strong*趋于W，且R^-W=0。故Z_NC_NZ_N*分成两个实际正交通道，其中正角为

\[
C_N^+=R_{2N_p,p}^-\otimes W_q\otimes M_{d_p}
                  +W_p\otimes R_{2N_q,q}^-\otimes M_{d_q}.
\tag{14}
\]

另一左逃逸角C_N^left把相应W换成e_(−2N−1)的单原子投影。两角正交。正角实际极限为

\[
C_\infty=R_p^-\otimes W_q\otimes M_{d_p}
                         +W_p\otimes R_q^-\otimes M_{d_q}.
\tag{15}
\]

这由原壳层的正交通道产生，不是按目标周期系数添加补偿。

C_∞不在422原E₂(S₁)域：时间乘法非S₁，负端常数不在E₁。径向系数却属于D₁=ℂ1+E₁的双端乘子类别，因1_(j<0)=1−H(j)，球／波形外积又有快速ℓ¹系数。原正端商不能把负端值认成正端边界。若使用负端有限部，必须明确改变定义域与来源入口。

## 5. 正角的强极限与完整重心的可控加强

分别定义K_N^+=C_N^+Ω、K_∞=C_∞Ω，同一采样估计给统一界。K_∞的实际采样公式可以完整写出。令
\(\mathcal B_r=c_r(1-\rho_r\mathsf T_{\log r})^{-1}\)，则

\[
\begin{split}
(K_\infty\phi)(t)
={}&d_p(t)\left\{\sum_{j<0}e_{j,p}\otimes w_{0,q}
              (\mathcal W_q\phi)(t-jL)
       +b_{0,p}\otimes w_{0,q}
              (\mathcal B_p\mathcal W_q\phi)(t)\right\}\\
&+d_q(t)\left\{\sum_{k<0}w_{0,p}\otimes e_{k,q}
              (\mathcal W_p\phi)(t-kM)
       +w_{0,p}\otimes b_{0,q}
              (\mathcal B_q\mathcal W_p\phi)(t)\right\}.
\end{split}\tag{15a}
\]

两个大通道正交；每个级数由(9)在整体Hilbert范数中收敛。与形式Ω记号不同，(15a)是直接的有界算子定义，且
\(\|K_\infty\|^2\le2+\|d_p\|_\infty^2B_0(\rho_p)+\|d_q\|_\infty^2B_0(\rho_q)\)。

令
\[
\mathsf P_N=\mathbf1_{j\ge-2N_p,\,k\ge-2N_q}\otimes1.
\]
因b_0、w_0全部支撑非负坐标，且\(\mathsf P_NR^-=R_{2N}^-\)，有严格算子恒等式
\[
C_N^+=\mathsf P_NC_\infty=C_\infty\mathsf P_N,\quad
K_N^+=\mathsf P_NK_\infty,\quad
A_N^+(h)=\mathsf P_NA_\infty(h)\mathsf P_N.
\tag{15b}
\]
后两式由(15a)与有界因子分解直接证明，不交换任何未压缩Γ和。
\(\mathsf P_N\)强趋于1，(15b)立即给正角的strong*极限；下面的尾界另量化其非一致性。

固定T包含d_p支集时，负p尾有准确估计

\[
\begin{split}
&\|((R_p^--R_{2N_p,p}^-)\otimes W_q\otimes M_{d_p})\Omega\phi\|^2\\
&=\sum_{j<-2N_p}\int d_p(t)^2|\mathcal W_q\phi(t-jL)|^2dt\\
&\le\int_{x\ge2N_pL-T}|\mathcal W_q\phi(x)|^2dx.
\end{split}\tag{16}
\]

q同理。故K_N^+→K_∞强收敛。在有限径向输入上，(K_N^+)*最终准确等于K_∞*；统一界给伴随强收敛。因此

\[
A_N^+(h)=\sum_gC_N^+P_gU(h)C_N^+
=K_N^+U(h)(K_N^+)^*
\xrightarrow{\mathrm{strong*}}A_\infty(h):=K_\infty U(h)K_\infty^*.
\tag{17}
\]

每个有限N正角仍在原开放理想，完整Γ和有与414相同的几何迹范数收敛。

这个限定正角结论已经足够。另有可核查加强：K_N^left=C_N^leftΩ也强趋于0。其环带部分只有j∈[−2N_p,−1]、k=−2N_q−1，采样x=t−jL−kM统一向正无穷，(9)以φ的L²远尾控制。球部分是

\[
b_{0,p}\otimes e_{-2N_q-1,q}\otimes
M_{d_p}\mathsf T_{-(2N_q+1)M}c_p(1-\rho_p\mathsf T_L)^{-1}\phi.
\tag{18}
\]

固定有界卷积的L²函数被平移到固定d_p支集外，故范数趋零；另一通道同理，不需N_p/N_q比值限制。伴随在有限径向输入上最终为0。采用此加强时，完整Z_NA_N(h)Z_N*也strong*趋于(17)的A_∞。

单坐标重心不能照抄(18)：另一长环带还跨正负两侧，左壳层的大时间位移可能被正环带抵消；所以裸C_N强极限不自动给全Γ强极限。双正重心使逃逸环带的两个坐标均为负，是上述尾界成立的具体原因。

## 6. 完整极限和的域：Schur强和而非一般Fréchet绝对和

w_n=λ_nw_0为完整正交基：其Fourier乘子为(ρ−z)/(1−ρz)，模恒1，是标准e_n基的实际酉卷积像。直接比较得

\[
R^-=\sum_{n<0}|w_n\rangle\langle w_n|,\qquad W=|w_0\rangle\langle w_0|.
\tag{19}
\]

极限正角的对角Γ块只保留b=0的p轴与a=0的q轴；交叉块E_p^∞λ_(a,b)E_q^∞仅在a<0,b>0非零，反向仅在a>0,b<0非零。在w基中它们是实际矩阵单位，范数1。

时间块K_(rs,g)=M_(d_r)𝕋_(ℓ_g)U(h)M_(d_s)若非零，ℓ_g必须属于固定有界区间J。对固定a，相应b至多1+|J|/M个；对固定b，相应a至多1+|J|/L个。时间块范数统一≤||d_r||∞||d_s||∞||h||₁。算子值Schur估计给任意有限交叉部分和统一范数界，并在有限w基输入上最终稳定；完整Γ和以strong*收敛。它与(17)由相同矩阵元识别。

一般不能认作双端D₁⊗D₁加权ℓ¹的绝对Fréchet和。若K_(pq,0)≠0，由L/M无理可取a_n<0,b_n>0、a_nL+b_nM→0；相应时间块范数趋向正数，径向块范数恒1，故这些项甚至不趋零。实际例子可取h(0)≠0、∫d_pd_q≠0，因TrK_(pq,0)=h(0)∫d_pd_q非零。未满足此重叠条件的分割需另检验一个非零时间块，不能宣称每个h都失败。

Blaschke基变换及其逆有快速ℓ¹群系数，保持自然双端快速域；在w基中，共振交叉矩阵单位的群Fourier系数有不趋零的S₁范数。因此此例的A_∞本身也不满足该域的p₀，不只是所写外部Γ表达式缺少绝对性。完整A_∞应采用本节明确的Schur强和域，不能直接写422的τ值。

## 7. 普通对角的绝对可控性与真实负端压缩

完整算子和不绝对，但物理e基对角有独立更强估计：

\[
(R^-\lambda_aR^-)_{jj}
=\mathbf1_{j<0}\mathbf1_{a=0}+|b_0(j)|^2\rho^{|a|},\qquad
(W\lambda_bW)_{kk}=|w_0(k)|^2\mathbf1_{b=0}.
\tag{20}
\]

交叉对角只在正象限。a=−n<0时

\[
\sum_j|w_{-n}(j)\overline{w_0(j)}|
=2(1-\rho^2)\rho^n,\qquad
\sum_jw_{-n}(j)\overline{w_0(j)}=0.
\tag{21}
\]

第一式的j=0与j≥1两部分各为(1−ρ²)ρ^n；第二式来自正交性。两位混合交叉对角绝对和为

\[
4(1-\rho_p^2)(1-\rho_q^2)\rho_p^{|a|}\rho_q^{|b|}.
\tag{22}
\]

时间迹范数由422(18)统一控制，故完整Γ混合对角绝对求和且总迹为0。这是对角域证明，不能替代第6节完整算子域证明。

取真实下截止P_K=1_(j,k≥−K)⊗1，K≥0，不作上截止。它压缩C_∞后的径向像有限秩，且

\[
P_KC_\infty=C_\infty P_K=C_{K,\mathrm{finite}}
:=R_{K,p}^-\otimes W_q\otimes M_{d_p}
                         +W_p\otimes R_{K,q}^-\otimes M_{d_q}.
\tag{23}
\]

有限基为e_(-K),…,e_(-1),b_0,w_0，均在全部多项式加权ℓ¹中。固定K原Γ压缩系数有几何衰减，沿414的有限基证明完整Γ迹范数绝对收敛。因此P_KA_∞(h)P_K是真正迹类算子，非仅形式对角。

R_K^-秩K+1，W秩1，R_K^-W=0。(20)–(22)及∫d_p²=L、∫d_q²=M给精确式

\[
\boxed{\ \operatorname{Tr}(P_KA_\infty(h)P_K)
=(K+1)(L+M)h(0)+\mathcal P_{p,q}(h).\ }
\tag{24}
\]

于是实际负端有限部为

\[
\lim_{K\to\infty}
\{\operatorname{Tr}(P_KA_\infty(h)P_K)-K(L+M)h(0)\}
=(L+M)h(0)+\mathcal P_{p,q}(h).
\tag{25}
\]

它由原重心正角、实际压缩、分割和球几何尾产生，没有按目标指定ρ或周期原子。更改负端扣除起点会改变单位时间常数，必须显式保留此依赖。

## 8. 原半迹与正角负端有限部的精确比较

固定N的正角迹为

\[
\operatorname{Tr}A_N^+(h)=D_Nh(0)+\mathcal P_{p,q}(h),\qquad
D_N=(2N_p+1)L+(2N_q+1)M.
\tag{26}
\]

左逃逸角的迹相同：单原子与w_N的全部缩放迭代迹均为δ_(a=0)。两角交叉项径向正交，绝对迹范数收敛后合法循环给迹0。因此

\[
\operatorname{Tr}A_N^+(h)=\tfrac12\operatorname{Tr}A_N(h).
\tag{27}
\]

这一个1/2来自真实壳层的两个正交通道，不能与有限位半迹所需的另一个1/2混同。将(25)与(26)比较得

\[
\boxed{\ \operatorname{FP}_{-}\operatorname{Tr}A_\infty(h)
=\tfrac12\operatorname{Tr}A_N(h)-(2N_pL+2N_qM)h(0)
=(L+M)h(0)+\mathcal P_{p,q}(h).\ }
\tag{28}
\]

扣除全部单位项时，两边均为原周期分布：

\[
\tfrac12\operatorname{Tr}A_N(h)-D_Nh(0)
=\lim_K\{\operatorname{Tr}(P_KA_\infty(h)P_K)
                            -(K+1)(L+M)h(0)\}
=\mathcal P_{p,q}(h).
\tag{29}
\]

左边对每个N已经精确与N无关。其分布极限是同一个周期分布，不能说成由连续边界商制造的新原子。新比较是(17)、(24)把它绑定到原实际通道产生、域与拓扑明确的负端有限部对象。

在固定紧测试支集内，周期原子只有有限多个，所以(29)是通常LF测试拓扑上的连续分布。完整N依赖仅在δ₀扣项。分割形状不影响(24)–(29)，但实际A_∞仍可能随分割变化。

## 9. 尚缺的相对／算术比较

(28)–(29)给实际正角与原有限位周期半迹的精确比较，不是G5主关系定理。422/423每个固定N的普通或扭曲交换异常仍为0，原T的混合异常仍须实际相对链修复；不同域有限部的存在不会自动改变这些事实。

若要接到主除子／相对交叉，还需：

1. Schur强和、负端压缩与边／角相对链之间的确定映射、定义域及测试兼容；证明原T在链中合法，不能只把(29)附在旧余圈后。
2. 新负端、正端与角点异常的完整计算，并证明所选主关系被修正配对消去；零标量交换异常不提供传递项。
3. 分割改变下相对类／配对不变、混合项及双次数的共同兼容；标量分割独立不足以替代。
4. 完整Weil型的Gamma／无穷位与全素数控制。本稿是两个固定有限位的比较，未给RR截面、算术正性或RH。

原Fréchet域之外的极限是精确识别的非一致性位置。强／Schur拓扑容纳实际对象，但原τ没有自动连续延拓；采用新域时必须重新证明相对配对，不能从已有数值比较宣布完整主消失。
