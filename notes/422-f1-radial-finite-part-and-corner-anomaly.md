# 422. 双径向有限部、角点异常与原周期算子的实际定义域

2026-09-21。[推导完成；独立全文逆审待完成] 接续[421](421-f1-weighted-hardy-trace-and-atomic-obstruction.md)与[有限任务](../reviews/2026-09-21/f1-radial-finite-part-relative-trace-next-proof-plan.md)。
以下构造的是原419代数中的明确稠密定义域及其非循环有限部。
并不由相对余圈的存在宣称算术主关系消失。

## 1. 固定格点起点的一维系数

仍取 \(T_0=\mathbb Z\cup\{\infty\}\)，有限点孤立，正尾收敛到∞；
向负无穷消失是 \(C_0(T_0)\) 条件。令
\[
 H(j)=\mathbf1_{j\ge0},\quad H(\infty)=1,\qquad
 E_1=\mathbb CH\oplus\ell^1(\mathbb Z),\quad
 \|aH+r\|_{E_1}=|a|+\|r\|_1.                                  \tag{1}
\]
序列 \(r\) 在∞取0。这是实际函数的唯一分解，因为 \(a=f(\infty)\)。
乘法的余项为 \(aHs+bHr+rs\)，故此范数次乘；复共轭等距。
完备性由直和给出。紧支格点函数及H的平移张成在 \(C_0(T_0)\) 一致稠密的子空间：
先用尾部极限减去 \(f(\infty)H\)，再截断所得 \(c_0(\mathbb Z)\) 序列。
所以E₁是原代数的稠密Banach星子代数，而非额外假定的几何对象。

对 \(a\in\mathbb Z\)，\(\beta_af(j)=f(j-a)\)，
\[
 \|\beta_a\|_{E_1\to E_1}\le1+|a|,\qquad
 \lambda(f)=\sum_j(f(j)-f(\infty)H(j)),\quad
 \lambda(\beta_af)=\lambda(f)-af(\infty).                        \tag{2}
\]
确切地，\(\beta_aH-H=-\mathbf1_{[0,a-1]}\) 当a>0；
a<0时等于 \(\mathbf1_{[a,-1]}\)，二者的和都是−a。
对ℓ¹余项则可合法重编号。并且
\[
 \lambda(f)=\lim_{R\to\infty}
 \left(\sum_{j\le R}f(j)-(R+1)f(\infty)\right),\quad R\ge0.       \tag{3}
\]
每个左无限和绝对收敛。此处没有假定有限部平移不变。

## 2. 两位空间、真正的联合截止与反例

定义 \(E_2=E_1\widehat\otimes_\pi E_1\)。由ℓ¹直和及其投影张量性质，
这等同于实际函数
\[
 f(j,k)=aH(j)H(k)+H(j)r_q(k)+r_p(j)H(k)+r_{pq}(j,k),             \tag{4}
\]
范数为 \(|a|+\|r_p\|_1+\|r_q\|_1+\|r_{pq}\|_1\)。
该描述亦可不用张量理论，直接取四分量完备直和：
先取双∞极限，再分别取边极限，即唯一恢复a、r_p、r_q，最后恢复r_pq。
乘法由(1)两次展开，给次乘性；有限分离紧支函数给 \(C_0(T_0^2)\) 中的稠密性。

记
\[
 f_p(k)=f(\infty,k)=aH(k)+r_q(k),\quad
 f_q(j)=f(j,\infty)=aH(j)+r_p(j),\quad f_c=a,
\]
\[
 \lambda_{pq}(f)=\sum_{j,k}r_{pq}(j,k),\quad
 e_p(f)=\lambda(f_p),\quad e_q(f)=\lambda(f_q).
\]
对 \(R,S\ge0\)，令 \(S_Rv=\sum_{j\le R}v(j)\)。真实的有限部是
\[
 \lambda_{pq}(f)=\lim_{\substack{R\to\infty\\S\to\infty}}
 \left[S_RS_Sf-(R+1)S_Sf_p-(S+1)S_Rf_q
                 +(R+1)(S+1)f_c\right].                       \tag{5}
\]
方括号准确等于 \(\sum_{j\le R,k\le S}r_{pq}(j,k)\)，
所以这是任意共尾联合极限，不要求R/S有界。运算顺序和边的标签均固定。

不能把(5)中的边截断随意换成其完整有限部。
例如 \(f(j,k)=H(j)r(k)\)，其中
\(r(k)=1/((k+1)(k+2))\) 对k≥0，其他为0，则 \(\sum r=1\)。
若仅从 \(S_RS_Sf\) 减去 \((R+1)\sum r\)，剩余
\[
                  -\frac{R+1}{S+2}.                            \tag{6}
\]
沿R=S趋于−1，沿R=S²发散，而(5)恒为0。
准确边截止防止另一方向的截止放大未控制尾部。

## 3. 完整平移、起点与角点项

由(2)对两坐标分别应用，得到
\[
\begin{aligned}
 \lambda_{pq}(\beta_{(a,b)}f)
   &=\lambda_{pq}(f)-ae_p(f)-be_q(f)+abf_c,\\
 e_p(\beta_{(a,b)}f)&=e_p(f)-bf_c,\\
 e_q(\beta_{(a,b)}f)&=e_q(f)-af_c,\qquad
 (\beta_{(a,b)}f)_c=f_c.                                        \tag{7}
\end{aligned}
\]
范数界为 \((1+|a|)(1+|b|)\)。角点项不是可选择的补偿：
它由先后两次减去边界的实际计数强制产生。
(7)的四分量变换严格满足平移复合律。

若参考正尾改为 \(H(j-u),H(k-v)\)，新的有限部为
\[
 \lambda^{u,v}_{pq}(f)=\lambda_{pq}(f)+ue_p(f)+ve_q(f)+uvf_c.     \tag{8}
\]
这是更换扣除起点，不是把f平移。本文始终采用原赋值起点u=v=0；
(8)仅给依赖性，不能为消去某个算术目标而调参。

## 4. 时间迹类与快速衰减群代数

令 \(\mathcal S_1=\mathcal S_1(L^2(\mathbb R_t))\)。
以S₁值替代(4)各分量，定义
\(E_2(\mathcal S_1)=E_2\widehat\otimes_\pi\mathcal S_1\)。
四分量在迹范数中唯一确定；乘法有
\(\|AB\|_1\le\|A\|_1\|B\|_1\)，故同一证明给Banach星代数。
这里边界极限是迹范数极限。

在419的分离坐标中，\(z_g\)只平移径向变量，原
\(P_g=z_g\otimes\mathsf T_{\ell_g}\)，\(\ell_g=g_1L+g_2M\)。
定义
\[
 \mathcal A=\left\{F=\sum_{g\in\mathbb Z^2}F_gz_g:
 p_k(F):=\sum_g(1+|g|_1)^k\|F_g\|_{E_2(\mathcal S_1)}<\infty
 \text{ for every }k\ge0\right\}.                              \tag{9}
\]
乘法、伴随沿419实际核公式：
\[
 (FG)_v=\sum_gF_g\beta_g(G_{v-g}),\qquad
 (F^*)_g=\beta_g(F_{-g}^*).
\]
所有级数在给定范数中收敛，且
\[
 p_k(FG)\le p_{k+2}(F)p_k(G),\qquad
 p_k(F^*)\le p_{k+2}(F).                                      \tag{10}
\]
权的次乘性及(7)的二次增长给这两式。
加权ℓ¹的可数交给完备Fréchet空间，因此这是明确的完成星代数。
由 \(\|\sigma(F)\|\le p_0(F)\) 及Fourier系数唯一性，它忠实嵌入
\(\mathfrak C\otimes\mathbb K_t\)；有限径向／群系数及时间有限秩核证明其C*稠密性。

设 \(\mathcal I\) 是(9)中每个 \(F_g\in\ell^1(\mathbb Z^2,\mathcal S_1)\) 的闭理想，
使用所有相同加权ℓ¹范数。它准确是两条边界限制同时为0的核。
边界像可以直接定义为两个实际限制代数的匹配对：
它们在双∞处的快速衰减S₁值群系数相同。
线性截面
\[
 (f_p,f_q)\longmapsto H(j)f_p(k)+H(k)f_q(j)-H(j)H(k)f_c           \tag{11}
\]
连续并逐系数适用，所以 \(\mathcal A/\mathcal I\) 是这个明确的边界代数。
此处没有把它与任意更大的C*商中的光滑逆封闭代数混同。

## 5. 有限部泛函确实来自普通截止迹

定义
\[
 \tau(F)=\operatorname{Tr}_t\lambda_{pq}(F_0),\qquad
                         |\tau(F)|\le p_0(F).                  \tag{12}
\]
这里0是新代数的群Fourier标签，不是把原外部Γ求和只留下g=0。

在 \(\ell^2(\mathbb Z^2)\otimes L^2(\mathbb R)\) 上，用
\(P_{R,S}=\mathbf1_{j\le R,k\le S}\otimes1\) 压缩。
对固定R,S，压缩F的各系数有绝对可和的S₁值矩阵元；
其迹范数和由常数 \(C_{R,S}p_0(F)\) 控制，故压缩后的实际算子迹类。
非零群标签无对角矩阵元，于是
\[
 \operatorname{Tr}(P_{R,S}FP_{R,S})
     =\sum_{j\le R,k\le S}\operatorname{Tr}_t F_0(j,k).
\]
按(5)同步减去两条边的零Fourier系数截止迹，再加回角点，
其联合极限正是(12)。没有交换一个未控制的无穷迹和极限。

对 \(F\in\mathcal I\)，矩阵单位展开绝对迹范数收敛，
\[
 \|F\|_1\le\sum_g\sum_m\|F_g(m)\|_1,\qquad
 \tau(F)=\operatorname{Tr}F.                                  \tag{13}
\]
因此这是原实际普通迹的确定扩张，但一般不循环，也不声称正性。

## 6. 精确交换异常与相对循环数据

先取单项 \(F=fz_g,\ G=vz_{-g}\)，\(g=(a,b)\)。
定义标量系数 \(k(m)=\operatorname{Tr}_t(f(m)v(m-g))\in E_2\)。
每个时间乘积迹类，时间普通迹可循环；于是
\[
 \tau([F,G])=\lambda_{pq}(k)-\lambda_{pq}(\beta_{-g}k)
             =-ae_p(k)-be_q(k)-abk_c.                         \tag{14}
\]
注意角点符号为−ab；这是(7)中平移−g后再相减。
两项群标签之和非0时有限部为0。由(10)，一般情形是(14)对全部g的绝对收敛和，
其中 \(k_g=\operatorname{Tr}_t(F_g\beta_gG_{-g})\)。
这一公式完整包含两边及角点，并非只取一个Toeplitz方向。

令 \(\Psi(F,G)=\tau([F,G])\)。若任一因子属于 \(\mathcal I\)，
(13)与普通迹的有界因子循环性给 \(\Psi=0\)。
所以它下降为 \(\mathcal A/\mathcal I\) 上的连续双线性泛函 \(\bar\Psi\)，满足
\[
 \bar\Psi(x,y)=-\bar\Psi(y,x),\qquad
 \bar\Psi(xy,z)-\bar\Psi(x,yz)+\bar\Psi(zx,y)=0.                 \tag{15}
\]
第二式是展开后用结合律抵消，不额外假定τ循环。
以 \(b\tau(F,G)=\tau(FG-GF)\) 为约定，得到
\(b\tau=q^*\bar\Psi,\ b\bar\Psi=0\) 的实际相对余圈数据。
更换起点时，τ的差由(8)的边界泛函给出，故 \(\bar\Psi\) 的差是相应余边界。
这说明起点依赖受控；没有因此识别算术主关系、K理论配对或全局Chern比较。

## 7. 原源与截止都是连续乘子

取 \(D_1=\mathbb C1+E_1\)，范数
\(\|s1+aH+r\|=|s|+|a|+\|r\|_1\)。
向负无穷及正无穷的极限保证唯一性。E₁是D₁的理想。
令 \(D_2=D_1\widehat\otimes_\pi D_1\)，并以
\(D_2\widehat\otimes_\pi B(L^2\mathbb R)\) 的快速衰减Γ系数定义 \(\mathcal M\)。
它由实际有界乘子组成，(10)的证明给对 \(\mathcal A\) 及 \(\mathcal I\) 的连续左右作用。
S₁的理想性质在这里不可省略。

414的 \(u=1-e+v\) 只有有限个原Γ系数；
它们的径向系数为1，时间算子为 \(M_f\mathsf T_{\ell_g}\)，所以 \(u\in\mathcal M\)。
\(Q=H(j)H(k)\otimes1\) 也在 \(\mathcal M\)，从而
\[
                  T=1-Q+QuQ\in\mathcal M.                      \tag{16}
\]
这不是宣称u或T在S₁时间代数本身中。

还须验证含无限壳层尾的 \(C_N\)。在原径向坐标，
每个 \(R_{K,p}\) 的有限维像由
\(e_{-K},\ldots,e_{K-1},b_K\) 张成，
\(b_K(j)=\sqrt{1-\rho_p^2}\rho_p^{j-K}\mathbf1_{j\ge K}\)。
这些向量在所有多项式加权ℓ¹中；q方向相同。
故每个 \(E_\alpha\) 的实际矩阵满足
\[
 W_k(E_\alpha):=\sum_{m,n}(1+|m-n|_1)^k|(E_\alpha)_{mn}|<\infty.
                                                                    \tag{17}
\]
这是原有限秩展开与指数尾的结果，不能由有限秩一般推得。
其群系数是 \( (E_\alpha)_d(m)=(E_\alpha)_{m,m-d}\)，
在(9)的开放径向ℓ¹类中快速衰减。
因此 \(C_N=\sum_\alpha E_\alpha\otimes M_{d_\alpha}\in\mathcal M\)，
且其两条径向边界都为0；时间乘法本身通常不紧。

## 8. 原全部Γ周期算子在新定义域中收敛

原外部求和标签记g，新代数的径向Fourier标签记d，两者不得混用。
对原
\[
 A_N(h)=\sum_{g\in\Gamma}C_NP_gU(h)C_N
       =\sum_{g,\alpha,\beta}E_\alpha\lambda_gE_\beta
            \otimes K_{\alpha\beta,g}(h),
\]
\[
 K_{\alpha\beta,g}(h)
 =M_{d_\alpha}\mathsf T_{\ell_g}U(h)M_{d_\beta},
\]
Fourier秩一积分给
\[
 \|K_{\alpha\beta,g}(h)\|_1
 \le \frac{\|\widehat h\|_1}{2\pi}\|d_\alpha\|_2\|d_\beta\|_2,
                       \quad h\in C_c^\infty(\mathbb R).       \tag{18}
\]
414的有限基向量平移系数界与(17)共同给，对每个k，
\[
 W_k(E_\alpha\lambda_gE_\beta)
 \le C_{N,k}\rho_p^{|g_1|}\rho_q^{|g_2|}.                       \tag{19}
\]
证明是先在两个固定有限基之间展开，平移只进入中间矩阵系数；
每个固定外积的W_k有限，中间系数按两个素数各自几何衰减。
常数可依赖N,k，不能声称对N一致。

由(18)–(19)，外部全部Γ和在 \(\mathcal I\) 的每个Fréchet范数中绝对收敛。
这是比旧迹范数收敛更强且单独证明的准入结论。
(13)和414的实际横向迹式因此给
\[
 \frac12\tau(A_N(h))=\frac12\operatorname{Tr}A_N(h)
 =D_Nh(0)+L\sum_{a\ne0}\rho_p^{|a|}h(-aL)
                  +M\sum_{b\ne0}\rho_q^{|b|}h(-bM),            \tag{20}
\]
\(D_N=(2N_p+1)L+(2N_q+1)M\)。
混合项由真实壳层迹为零；并未删除混合外部g。
所有N依赖和半迹因子均保留，没有再把这一个1/2与有限位半迹的另一个1/2混同。

这也说明新泛函确实容纳所需原子，但不是421中一个固定S₁算子B与U(h)的配对。
准入控制的是 \(\|\widehat h\|_1\)，局部缩窄测试时它可保持量级不变，
不能将其偷换成趋零的 \(\|h\|_1\) 或 \(\|h\|_2\)。

## 9. 原提升的实际相对异常：只支撑在单位时间

取任意实 \(d\in C_c^\infty(\mathbb R)\)，定义
\[
 K_h=Q\otimes M_dU(h)M_d\in\mathcal A.
\]
这里Q只指径向H⊗H。由§7的乘子准入，\(T^*TK_h,TK_hT^*\) 都属于 \(\mathcal A\)。
故可以定义实际数值
\[
             \Psi(T^*,TK_h):=\tau(T^*TK_h-TK_hT^*).             \tag{21}
\]
这只是已定义乘子的交换异常，不是默认的K理论配对。

写原有限源为 \(u=1+\sum_g f_g(t)P_g\)，其中
\[
 f_{(n,0)}(t)=-c(t)c(t-nL),\qquad
 f_{(n,1)}(t)=c(t)c(t-nL-M).
\]
零函数可留在有限标签集。置
\(q_g(j,k)=H(j-\max(0,g_1))H(k-\max(0,g_2))\)，则
\(T=1+\sum_g q_g z_g\otimes M_{f_g}\mathsf T_{\ell_g}\)。
对g≠0，
\[
 (T^*)_g=q_g\otimes
    M_{\overline{f_{-g}(t-\ell_g)}}\mathsf T_{\ell_g},
 \quad
 (TK_h)_{-g}=q_{-g}\otimes
    M_{f_{-g}}\mathsf T_{-\ell_g}M_dU(h)M_d .
\]
\(\beta_gq_{-g}=q_g\)，时间净移位为0，所以(14)中相应标量函数为
\[
 q_g(j,k)\,h(0)\int |f_{-g}(t-\ell_g)|^2d(t)^2\,dt.             \tag{22}
\]
时间迹公式可由(18)的秩一积分直接核验，未循环两个非迹类时间因子。
g=0的项包括单位及f₀，其交换异常严格为0。

若g=(a,b)，\(e_p(q_g)=-\max(0,b)\)，\(e_q(q_g)=-\max(0,a)\)，
\((q_g)_c=1\)。故(14)的完整径向系数为
\(a\max(0,b)+b\max(0,a)-ab\)。
p方向b=0全部消失；v方向g=(−n,−1)时该系数为 \(-\max(0,n)\)。
由此得到精确的原源公式
\[
 \boxed{\ \Psi(T^*,TK_h)
  =-h(0)\sum_{n>0}n\int
          c(t)^2c(t+nL+M)^2d(t)^2\,dt.\ }                     \tag{23}
\]
因c紧支，和实际有限。特别地，此读出只有单位元支撑。
在421的近锐族中若支集长度L+ε且ε<M，所有这些重叠都消失，(23)为0。
这一附加消失不用于证明任意截止下的主关系。

更一般地，对有限个原Γ标签、时间分量均为
\(M_{f_g}\mathsf T_{\ell_g}\) 的乘子A,B，及上面零Γ标签的K_h，
\(\tau([A,BK_h])\) 中只有相反标签相乘。
\(\ell_g+\ell_{-g}=0\) 强制时间普通迹为h(0)乘一个与h无关的常数。
因而这一明确的相对异常类不能消去414在非零时间的素数周期见证。
此结论只覆盖所述有限标签／测试位置，不排除更高相对链、热演化或不同几何比较。

## 10. 为什么重新插入原截止也没有直接补上桥梁

§8已经证明 \(A_N(h)\in\mathcal I\)，而§7给其两条径向边界为0。
对任意 \(B\in\mathcal M\)，其与 \(A_N(h)\) 的乘积仍在 \(\mathcal I\)，且
\[
                 \tau([B,A_N(h)])=\operatorname{Tr}[B,A_N(h)]=0. \tag{24}
\]
同理，在已定义的乘积域中，任一含C_N的因子经过时间迹类平滑后落入开放理想，
其由(14)给出的边界异常为0。
裸C_N不在 \(\mathcal A\)，故不能对未平滑的它直接写τ值。

(20)的普通迹本身当然可非零；(24)说的是交换异常。
因此既不能把(23)的单位项当作完整周期补偿，
也不能把(20)原子值任意添加到(15)后称为几何传递。
本稿获得实际定义域、相对余圈及原源上的精确比较，并定位这一直接版本的失败。
完整主除子根空间、两次数、固定B、截面与RR仍开放；没有RH或比例改进。

## 11. 原始文献与形式化范围

有限部及边界异常作为一般机制已有先行理论。
Albin–Melrose作者稿PDF24、30的(3.13)、(3.26)明确区分重整化迹与循环迹；
Loya–Melrose作者稿PDF18–21的Definition3.3、Proposition3.5及Theorem3.7给角流形的b迹与各余维边界贡献。
本文的离散ℓ¹域、联合截止、原C_N的快速衰减准入及(23)均直接证明，
没有先声称原F₁来源属于这些微分算子演算。
原PDF与[核读记录](../reviews/2026-09-21/f1-radial-finite-part-source-read.md)保存；不声称新的普遍b迹理论。

[RadialFinitePart.lean](../formal/F1/Analysis/RadialFinitePart.lean)形式化六个可复用代数步骤：
四分量平移的单位／复合／逆、双截止包含排除、反向平移交换异常及(23)的整数角点系数。
[内核报告](../formal/checks/radial-finite-part-verification.json)已在固定Lean4.32.2通过；
依赖仅propext、Quot.sound，无sorryAx。
实际ℓ¹／S₁完成、无穷迹、Fréchet收敛、相对循环下降及RH均不在这些形式化证明的范围。
