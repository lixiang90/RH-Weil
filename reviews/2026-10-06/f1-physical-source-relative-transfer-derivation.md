# 原Haar球截止的源边界、完成平均与实际迹极限次序

2026-10-06。独立推导425、429、430、432、433的同一原采样、原源与物理截止。
只写本报告，不改笔记或索引。这里的准入在原Hilbert空间中支付，不由源不变x截止移植。

## 1. 原数据及结论

令L=log p、M=log q，rho_p=p^(-1/2)、rho_q=q^(-1/2)。
沿用原实值光滑紧支平方分割c=d_p、d=d_q，
\[
 \sum_j c(t-jL)^2=\sum_k d(t-kM)^2=1,\quad
 \int c^2=L,\quad\int d^2=M.
\]
完整波形基为w_n=lambda_n w_0；原径向基记为e_n。
除去425的共同时间酉元后，同一固定算子准确为
\[
 A(h)=VU(h)V^*,\qquad
 (V_p\phi)_{j,0}(t)=\mathbf1_{j<0}c(t)\phi(t-jL),\quad
 (V_q\phi)_{0,k}(t)=\mathbf1_{k<0}d(t)\phi(t-kM),
                                                        \tag{1}
\]
其中V=V_p+V_q，U(h)核为h(t-t')，h属于C_c^\infty(R)。
原源幂保持全部时间：
\[
 u^r=1-e+v_r,\qquad
 v_r=\sum_a M_{c(t)c(t-aL-rM)}P_{(a,r)}.                 \tag{2}
\]
固定整数r时只有有限个a有非零系数。e为源投影，与物理径向基e_n区分。

物理截止、源共轭和完成平均记为
\[
 P_K=\mathbf1_{\text{物理 }j\ge-K_p,\ k\ge-K_q}\otimes1_t,\quad
 A_r(h)=u^rA(h)u^{-r},\quad X(h)=FU(h)F^*,\ F=(1-e)V.
\]
置
\[
 f=cd,\quad a_p(x)=\sum_{n<0}c(x+nL)^2,\quad
 I_f=\int f^2,\quad W=M-I_f,\quad
 J_p=\int a_p(x)(1-a_p(x))dx.                            \tag{3}
\]
a_p光滑，充分左端0、充分右端1，故J_p有限；W非负。
完整原轴分布为
\[
 \Pi_p(h)=\sum_a\rho_p^{|a|}h(-aL),\quad
 \Pi_q(h)=\sum_b\rho_q^{|b|}h(-bM),\quad
 \Lambda(h)=L\Pi_p(h)+M\Pi_q(h).                         \tag{4}
\]

独立结果是：固定r、足够深K时有准确等式
\[
 \boxed{\operatorname{Tr}(P_KA_r(h)P_K)
   =(K_pL+K_qM)h(0)+\Lambda(h)-rW h(0).}                 \tag{5}
\]
两个截止阈值允许依r变化，不能说对全部r统一。完成平均的同一物理截止则为
\[
 \boxed{\operatorname{Tr}(P_KX(h)P_K)
          =(K_qW+J_p)h(0)+W\Pi_q(h)}                    \tag{6}
\]
对足够深K准确成立。以下还证明固定K时
\[
 \|P_K(C_N(h)-X(h))P_K\|_1=O_{K,h}(N^{-1}),\quad
 C_N(h)=N^{-1}\sum_{r=1}^NA_r(h).                        \tag{7}
\]
因此不同极限次序的反例可用实际普通压缩迹给出，而不只是形式有限部。

## 2. 物理截止的真实波形矩形和Haar逃逸球

对一位s，令c_s=sqrt(1-rho_s^2)，D_p=L、D_q=M。
球向量b_-K=lambda_-K b_0满足
\[
 b_{-K}=-c_s\sum_{n<-K}\rho_s^{-K-n-1}w_n,\qquad
 H_{K,s}:=\mathbf1_{\text{物理 }j\ge-K}
     =D_{K,s}+P_{b_{-K,s}},\quad
 D_{K,s}=\sum_{n\ge-K}P_{w_n}.                            \tag{8}
\]
这里的正交分解是整个物理半线，并不限于原A的支撑。
证明：n>=-K的w_n全部支撑于物理半线，且与b_-K正交；
n<-K的半线限制准确为
\[
 H_{K,s}w_n=-c_s\rho_s^{-K-n-1}b_{-K,s}.
\]
由完整波形基得到(8)。球系数的ell^1和为c_s/(1-rho_s)，与K无关。

两位P_K是四个正交通道的和：
\[
 D_{K_p,p}\otimes D_{K_q,q},\quad
 P_{b_{-K_p,p}}\otimes D_{K_q,q},\quad
 D_{K_p,p}\otimes P_{b_{-K_q,q}},\quad
 P_{b_{-K_p,p}}\otimes P_{b_{-K_q,q}}.                    \tag{9}
\]
非零周期权重将由中间两通道承担。把物理截止直接改成波形矩形会丢失它们。

## 3. 原Hilbert空间中的迹类准入

这里先支付普通迹，随后才对角求值。对固定r，(2)是有限个径向移位加时间系数。
选较深物理截止P'=P_(K_p+A_r,K_q+B_r)，使所有允许径向位移都满足
\[
                  P_Ku^r=P_Ku^rP'.
\]
时间乘子及时间平移与物理径向投影交换；该式逐有限群项成立。
425已经证明P' A(h)P'属于S_1，于是准确因子分解
\[
 P_KA_r(h)P_K=(P_Ku^rP')\, (P'A(h)P')\,
                                    (P'u^{-r}P_K)       \tag{10}
\]
使每个固定物理压缩属于S_1。全u^r A u^-r通常非紧，(10)并不称它迹类。

同理，1-e为有限源系数和，X=(1-e)A(1-e)，使用较深P'证明
P_KX P_K属于S_1。左、右分别压到不同固定物理截止的交叉压缩也可用同一因子办法。
这足以支付本报告所有A_r、X及有限Cesàro和的准入。

另一个后面使用的直接证明是Fourier秩一积分。实际采样压缩后径向行有限；
逃逸球的无限系数ell^1绝对可和，时间输出系数光滑紧支。
对形式平面波e_xi(t)=exp(i xi t)，定义真实输出向量
v_(K,r)(xi)为P_Ku^rV的明确采样式作用该函数。它属于原Hilbert空间，且
sup_xi ||v_(K,r)(xi)||有限。这里没有将e_xi当作L²输入。
逐光滑时间核比较给
\[
 P_KA_r(h)P_K=\frac1{2\pi}\int\widehat h(\xi)
       |v_{K,r}(\xi)\rangle\langle v_{K,r}(\xi)|\,d\xi.    \tag{11}
\]
hat h属于L¹，故此积分在迹范数中绝对收敛；核相等先在稠密紧支光滑输入上证明，
再由有界性延拓。P_KX P_K有同样表示。完整混合块在(10)、(11)中均保留，
未在准入前删除。

## 4. 原源的准确采样行和局部能量

直接作用(2)得到
\[
 (u^rV\phi)_{j,k}(t)=\eta^{(r)}_{j,k}(t)\phi(t-jL-kM),
\]
\[
\begin{split}
 \eta^{(r)}_{j,k}(t)={}&
 \delta_{k0}c(t)[\mathbf1_{j<0}-a_p(t-jL)]
 +\delta_{kr}c(t)a_p(t-jL-rM)\\
 &+\delta_{j0}\mathbf1_{k<0}d(t)\\
 &+c(t)[\mathbf1_{k<r}f(t-jL-rM)
                          -\mathbf1_{k<0}f(t-jL)] .
\end{split}                                               \tag{12}
\]
r=0准确还原(1)。全部输出时间在supp(c)并supp(d)内。
固定r时，充分负p行只为q=r、系数c(t)；充分负q条带系数为
\[
 D_j^{(r)}(t)=\delta_{j0}d(t)
              +c(t)[f(t-jL-rM)-f(t-jL)].                 \tag{13}
\]
(13)只含有限个p标签。除此之外只有有限角点行，没有双负外角支撑。

在y=t-jL坐标中平方分割给
\[
 \sum_j D_j^{(r)}(y+jL)^2
                  =d(y)^2-f(y)^2+f(y-rM)^2,
 \quad \sum_j\int D_j^{(r)}(t)^2dt=M.                    \tag{14}
\]
证明是完整平方展开：第一交叉项为
2f(y)[f(y-rM)-f(y)]，其余平方项用sum_j c(y+jL)^2=1，
准确合成右侧。(14)同时支付q深条带总归一化和完整混合能量；不是预先要求q周期不变。

## 5. 波形矩形的p、q通量及逃逸球迹

固定r，选择两个K越过(12)的所有有限角点及(13)的有限p宽度，
并使r>=-K_q，且两负截止均进入上述深端。波形矩形的核对角迹为
h(0)乘可见行的总时间能量；r=0给K_pL+K_qM。

可在已选定的物理波形矩形中用忠实坐标x=t-jL-kM换元。
源u逐x酉，全部采样能量点态不变。
p外边j<-K_p的源能量与原能量之差为
\[
 a_p(x-K_pL+rM)-a_p(x-K_pL).
\]
两个无穷外能量不能各自积分相减；差本身紧支可积，且
\[
 \int[a_p(x+rM)-a_p(x)]dx=rM.                            \tag{15}
\]
例如对位移求导、int a_p'=1即证，对负r也成立。
q外边k<-K_q的能量差由(14)为
\[
 \sum_{k<-K_q}[f(x+(k-r)M)^2-f(x+kM)^2],
\]
这是有限望远镜和，积分为-rI_f。双外边无支撑，故可见矩形能量差准确为
\[
                  -rM+rI_f=-rW.                        \tag{16}
\]
这一方法把全部角点混合能量计算在内，不依赖先把通道交叉设为零。

p逃逸球只遇到深p边q=r；取足够深q截止后该标签完全可见。
球几何系数的Fourier自相关为
\[
 \frac{1-\rho_p^2}{|1-\rho_p e^{i\xi L}|^2}
                 =\sum_a\rho_p^{|a|}e^{ia\xi L}.
\]
int c²=L，源r和截止K引入的时间相位在自相关中准确消去，故p球迹为L Pi_p(h)。
q逃逸球只遇到(13)，全部有限p标签可见；同一Poisson展开及(14)给M Pi_q(h)。
这两式含单位项Lh(0)、Mh(0)。双球通道压缩为零，因(12)的双负区为空。
(9)正交，且压缩已S_1，所以通道之间的完整交叉块普通迹为零。
这发生在源混合项全保留并计算之后。

合并矩形的(K_pL+K_qM-rW)h(0)和两球迹证明(5)。
沿425同一体积扣除，准确有限部为
\[
 \operatorname{FP}_{\rm phys}(A_r(h))=\Lambda(h)-rWh(0).
\]
原加权边界的实际物理压缩迹于是为
\[
                 \operatorname{Tr}(P_K[A-uAu^*]P_K)
                                 =Wh(0)                 \tag{17}
\]
对大K成立。p<q时W>=M-L>0，对所有原合法分割有严格非零单位见证。
W含辅助分割重叠I_f，不能自动称作算术不变量。
h(0)=0时该边界的物理压缩迹准确为零；这一族没有新增非零时间或混合长度原子。
全边界仍通常非紧，这个零迹不把它变成S_1或HH₁闭链。
432的源不变x截止对同一边界每次迹为零，两种真实截止的源通量并不相同。

## 6. 完成固定算子X的原物理迹

由(12)的1-e部分，
\[
 (F_p\phi)_{j,0}(t)
   =c(t)[\mathbf1_{j<0}-a_p(t-jL)]\phi(t-jL),
\]
\[
 (F_q\phi)_{j,k}(t)=\mathbf1_{k<0}D_j^F(t)
                         \phi(t-jL-kM),\quad
 D_j^F(t)=\delta_{j0}d(t)-c(t)f(t-jL).                     \tag{18}
\]
F_p和F_q各自只有有限个p波形标签。
全p平方分割给
\[
 \sum_j\int c(t)^2[\mathbf1_{j<0}-a_p(t-jL)]^2dt=J_p,
 \qquad \sum_j\int D_j^F(t)^2dt=W.                       \tag{19}
\]
第一式换元x=t-jL后，平方展开为
a_p(1-a_p)^2+(1-a_p)a_p²=a_p(1-a_p)。
第二式交叉项-2I_f、末平方和+I_f，合计M-I_f。

足够深P_p在这有限p标签上为单位，无p逃逸球贡献。
F_p的q=0与F_q的q<0经物理P_q后仍正交，因为w_0与所有这些波形及球正交。
F_p全部迹为J_p h(0)；F_q波形负块有K_q行、每行总能量W，
q球的几何自相关给W Pi_q(h)。完整交叉算子保留而迹为零。
得到(6)，即
\[
 \operatorname{Tr}(P_KX P_K)
       =(K_qW+J_p+W)h(0)
             +W\sum_{b\ne0}\rho_q^{|b|}h(-bM).            \tag{20}
\]
X是433同一原源平均的范数极限，未按目标读出指定。
它失去原p体积和p周期，原q体积也由M变W；因此将原体积扣除机械用于X
一般不给原联合有限部。以下反例取h(0)=0，完全避开这项归一化问题。

## 7. 固定物理截止下的迹范数收敛

这一节独立补足433未声称的局部迹比较。只考虑r趋正无穷及固定K。
置Z=eV。433的准确分解为u^rV=F+u^rZ；源角行是
\[
 (u^rZ\phi)_{j,k}(t)=
 c(t)\{\delta_{kr}a_p(t-jL-rM)+
                         \mathbf1_{k<r}f(t-jL-rM)\}
                           \phi(t-jL-kM).                \tag{21}
\]
令supp(c)包含于[c_-,c_+]，a_p(x)=0于x<a，supp(f)包含于[f_-,f_+]。
若f恒零则第二项为空，可任取这样的f端点。
(21)非零p标签都满足
\[
 j\le J_r,\qquad
 J_r\le -rM/L+C_0.                                      \tag{22}
\]
确实，第一项要求t-jL-rM>=a；
第二项要求t-jL-rM位于supp(f)，且允许j的数目有统一有限界。
所以r足够大时J_r<-K_p；物理P_p将这些行全部压到唯一球b_-K_p。
其系数的绝对值为
\[
 |\beta_{p,j}|=c_p\rho_p^{-K_p-j-1},
 \quad \sum_{j\le J_r}|\beta_{p,j}|
                              \le C_K e^{-rM/2}.         \tag{23}
\]
指数中的M/2来自rho_p=exp(-L/2)与j约为-rM/L，并非重新取权。

令e_xi(t)=exp(i xi t)，仍仅用于明确输出采样。
经P_p压缩后，k<r行的时间向量为exp(-i xi kM) H_(r,xi)(t)，其中
\[
 H_{r,\xi}(t)=c(t)e^{i\xi t}
       \sum_j\beta_{p,j}f(t-jL-rM)e^{-i\xi jL}.
\]
k=r行时间向量为exp(-i xi rM) J_(r,xi)(t)，其中
\[
 J_{r,\xi}(t)=c(t)e^{i\xi t}
       \sum_j\beta_{p,j}a_p(t-jL-rM)e^{-i\xi jL}.
\]
(23)及光滑紧支、有界系数给一致界
\[
 \sup_\xi(\|H_{r,\xi}\|_2+\|J_{r,\xi}\|_2)
                              \le C_K e^{-rM/2}.         \tag{24}
\]
求和在绝对L²范数中收敛。

接着P_q保留-k次数从-K_q到r-1的r+K_q个波形行，
外加一个q球行，以及k=r的一个行。q球由k<-K_q的几何ell¹系数求和，
其标量绝对值至多c_q/(1-rho_q)。因此实际向量
\[
 b_r(\xi):=P_Ku^rZ e_\xi
\]
满足
\[
 \boxed{\sup_\xi\|b_r(\xi)\|
            \le C_K\sqrt{r+K_q+2}\,e^{-rM/2}.}            \tag{25}
\]
这里r充分大，且K固定。这个界无需把整个Hilbert空间中的u^rZ说成小算子。

同理(18)只有有限p标签，q轴经P_q只剩有限波形行及一个几何球行，给
\[
 a(\xi):=P_KF e_\xi,\qquad \sup_\xi\|a(\xi)\|\le C'_K.    \tag{26}
\]
所有输出时间都位于固定紧区间；无任意平面波L²输入假定。

现在(11)的两个核分别以a+b_r及a给出。秩一迹范数估计
\[
 \||a+b\rangle\langle a+b|-|a\rangle\langle a|\|_1
                                      \le2\|a\|\|b\|+\|b\|²
\]
和hat h属于L¹，得到
\[
 \boxed{\|P_K(A_r(h)-X(h))P_K\|_1
 \le C_{K,h}\{\sqrt{r+K_q+2}\,e^{-rM/2}
                      +(r+K_q+2)e^{-rM}\}.}             \tag{27}
\]
有限个初始r的压缩也已由第3节支付S_1。
(27)对r的右边可求和，故
\[
 \|P_K(C_N(h)-X(h))P_K\|_1
       \le N^{-1}\sum_{r=1}^\infty
                  \|P_K(A_r(h)-X(h))P_K\|_1
       =O_{K,h}(N^{-1}).                                \tag{28}
\]
这证明固定K的普通迹收敛，而非从全算子范数收敛推断迹收敛。
常数依K，特别(23)含物理p截止深度的指数因子；
(28)没有支付对K一致估计，也不能交换下一节的极限。

## 8. 同一实际源平均、同一物理截止的非交换极限

L/M无理，故可取h光滑紧支于-L的小邻域，
h(-L)=1，避开0及两轴其他整数周期。于是
\[
             h(0)=0,\quad \Pi_q(h)=0,\quad
                         \Lambda(h)=L\rho_p\ne0.         \tag{29}
\]
对每个有限N，选K越过所有1<=r<=N的有限阈值后，(5)直接给
\[
                   \operatorname{Tr}(P_K C_N(h)P_K)
                                      =L\rho_p.
\]
因此先物理截止、后源平均的两个实际标量极限为
\[
 \lim_{N\to\infty}\lim_{K_p,K_q\to\infty}
                   \operatorname{Tr}(P_K C_N(h)P_K)
                                      =L\rho_p.          \tag{30}
\]
固定K时(28)给内层N极限等于Tr(P_KX(h)P_K)；
大K时(6)、(29)使该迹准确为0。所以反过来
\[
 \lim_{K_p,K_q\to\infty}\lim_{N\to\infty}
                   \operatorname{Tr}(P_K C_N(h)P_K)
                                      =0.               \tag{31}
\]
两式均是已准入S_1压缩的实际普通迹。
不是把恒零标量列说成非零极限，也无需改一个单位时间常数。
差来自N相关截止阈值及逃逸球：范数平均把原p周期移到任意深物理负端，
固定K的局部迹先看不到它；先取足够深K则每个有限源平均都看得到。

433已经给C_N(h)->X(h)的全算子范数收敛，X属于实际最小源闭理想J。
(30)–(31)进一步说明原物理读出不能只靠该范数完成连续传递。
h(0)不零时由(5)还得有限N原有限部
Lambda(h)-(N+1)W h(0)/2；X的体积系数变更则是另一个明确障碍。

## 9. 有限词、相对循环与规范性范围

432的原链u* tensor uA(h)的Hochschild边界为A-uAu*。
其通常非紧，故在模S_1商中仍非闭；物理压缩迹为0并不改变这一事实。
431的有限轨道边界单射排除了只用有限对角源共轭词的修复。
433的完成固定扇区确实存在，但(30)–(31)说明普通S_1迹、
物理有限部及实际HH₁电荷不能由算子范数平均无条件传递。
若使用无限相对链，必须另指定链拓扑、证明边界收敛，
并证明b(lift)在迹理想拓扑中可读；本报告未完成这一桥。

现在可严格区分三个已证事实：
原物理球对A给原两位周期；原源共轭有真实单位通量Wh(0)；
源不变x截止及完成平均采用不同的可见边界，均不能自行选定物理Lambda。
非零单位通量依原分割，非零时间不连续反例则使用原Haar权重。
两者均不提供不可替代的算术主关系、Weil二次型正性、
实位和全素数比较、RR或RH。这里所得是准入和连续传递的具体障碍及下一步约束，
不是规范相对Chern类已经构成的声明。

交叉参照：本次独立计算与434的全有限源域物理准入、
435的全部固定共轭原迹一致；最强的新局部估计为(27)–(28)，
它将完成读出障碍加强为(30)–(31)的两个实际普通迹极限。
