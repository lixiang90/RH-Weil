# 明确R_g核：实际Gaussian、Poisson符号与全部零模

2026-10-27；/root/kg_poisson独占原稿。执行STATE唯一[修补核准入](../negative-plane-green/next-corrected-kernel-source-admission.md)，恢复D20261027P、独立singlex证书与原literal冻结。本稿只处理同一fixed division模型的明确R_g/K_g；不改STATE/cadence/Git，不预C048/585，不借作者modularity/7.4、自然height或后章证明。出稿不代root消费。

## 1. 独立版本、实际格与Fourier测度

固定V_R的实双线性B、Q=B(x,x)/2及签名(1,2)，D=C\R。令x=x_++x_-为z对应的正一维／负二维B正交分解，定义

\[
 R_g(x,z)=-B(x_-,x_-),\qquad
 H_z(x)=B(x,x)+2R_g(x,z)
        =B(x_+,x_+)-B(x_-,x_-)>0\quad(x\ne0).
\]

当前actual系数为

\[
 \varphi_z(x):=\varphi_g^0(x,z)e^{-2\pi Q(x)}
 =[4\pi(R_g(x,z)+2Q(x))-1]e^{-\pi H_z(x)}.
 \tag{1}
\]

这里R_g+2Q=B(x_+,x_+)。这是已经明写的2R_print版本，不能写回原literal规范。式(1)对全部实x（包括x=0）直接定义smooth scalar，不靠singlex Green在Q=0处的current解释；\(\varphi_z(0)=-1\)。

采用B-selfdual Lebesgue测度dX，以及

\[
 (\mathcal F_Bf)(y)=\int_{V_R}f(x)e^{-2\pi iB(x,y)}dX(x).
 \tag{2}
\]

具体说，在任一B-orthonormal实坐标X=(X_1,X_2,X_3)、B=diag(−1,−1,+1)中，dX为普通三维Lebesgue测度。原矩阵坐标x=[[a,u+d],[u-d,−a]]在z=i时可取X=√2(a,u,d)，所以dX=2√2 da du dd；不是把这组未缩放坐标的普通测度误当selfdual。

actual L=O_B∩V是fullrank3格，记

\[
 c_L=\operatorname{vol}_{dX}(V_R/L)>0,\qquad
 L^\#=\{y\in V_R:B(y,L)\subset\mathbf Z\}.
\]

L^#仍为fullrank格，c_(L#)=c_L^−1。c_L按固定B与L定义，不依z；没有将L假设为selfdual或把c_L设为1。换L基时c_L等于该基B-Gram行列式绝对值的平方根。

## 2. Fourier特征值是−1，不是+1

在z适配的B-orthonormal坐标中，R_g=X_1²+X_2²、2Q=X_3²−X_1²−X_2²，故(1)恰为

\[
 \varphi_z(X)=(4\pi X_3^2-1)e^{-\pi|X|^2}.
 \tag{3}
\]

设G=e^(−π|X|²)。标准Gaussian积分直接给\(\mathcal F_BG=G\)；B的两个负号只改变Fourier自变量的对应符号。第三坐标为正，且

\[
 \mathcal F_B(X_3^2G)
 =-\frac1{4\pi^2}\partial_{Y_3}^2G(Y)
 =\left(\frac1{2\pi}-Y_3^2\right)G(Y).
\]

所以

\[
 \boxed{\mathcal F_B\varphi_z=-\varphi_z},\qquad
 \int\varphi_z\,dX=1,\qquad\varphi_z(0)=-1.
 \tag{4}
\]

任意两个适配坐标由B-isometry连接，其Jacobian绝对值为1、保(2)的测度与pairing，因此(4)对每个z成立；不需在全D选择一个全局frame，也没有用theta的模变换定理。

## 3. actual K_g是通常smooth格点和，且有Γ不变性

令τ=u+iv，v>0。把e^(−2πvQ)并入(1)，得到原拟式的相同表达

\[
 K_g(u+iv,z)=\sum_{x\in L}
               \varphi_z(\sqrt v x)e^{2\pi iuQ(x)}.
 \tag{5}
\]

对z在D的任一compact集，正定H_z与任取固定Euclidean norm一致等价，且所有固定阶z导数的二次型系数有界。因此任意固定阶空间／u／v导数，在v的compact正区间中由多项式×正定Gaussian逐项可和控制。式(5)及这些导数绝对、正常收敛，给通常C∞函数。实u的phase绝对值为1；这里的存在性不声称下面small-v零模对任意u仍相同。

Γ=O_B^×按共轭保L、B、Q，且R_g(γx,γz)=R_g(x,z)。换格点变量给K_g(τ,γz)=K_g(τ,z)。它因而下降到当前M(C)=Γ\D的smooth scalar；Γ稳定子的普通orbifold局部函数条件已足，不把这一步称为算术Chow／height身份。

本模型D(B)>1，M(C) compact。取有限orbifold charts，每个有在D中compact闭包的lift；这些lift的并集足以估全局C^k norm，不假设某个未构造的fundamental polygon在坐标中compact。有限charts上H_z的统一正定下界、所有系数导数界及固定格的Gaussian壳数给下文全空间估计。L^#也受Γ保留，故相同框架可用于dual和。

## 4. Poisson公式、covol与small-v主项

当前原范数门只用冻结ray u=0。写

\[
 K_L(v,z)=\sum_{x\in L}\varphi_z(\sqrt v x).
\]

对Schwartz函数(1)应用普通格点Poisson公式；测度和dual按(2)固定。缩放给

\[
 \mathcal F_B[\varphi_z(\sqrt v\,\cdot)](y)
 =v^{-3/2}(\mathcal F_B\varphi_z)(y/\sqrt v)
 =-v^{-3/2}\varphi_z(y/\sqrt v).
\]

因此准确公式是

\[
 \boxed{K_L(v,z)
 =-c_L^{-1}v^{-3/2}K_{L^\#}(1/v,z).}
 \tag{6}
\]

ordinary Poisson可通过一组L基化为Z³的公式，换元Jacobian恰为c_L；这里没有缺失discriminant／finite-lattice体积。dual零格点取值−1，故small-v主项为**正**c_L^−1v^−3/2。大v原零格点主项为−1。两者都是整个空间上的同一常数，非仅某个cusp或某条空间ray上的常数。

## 5. 所有固定阶空间与log-v导数的双端尾

记D_v=v∂_v。对任意固定k,j≥0，有限compact lifts上任意相应空间导数及D_v^j作用于一个非零格点项，所得是(v与x的有限次多项式)×e^(−πvH_z(x))。更精确可由

\[
 C_{k,j}(1+v|x|^2)^{m_{k,j}}e^{-a v|x|^2}
 \tag{7}
\]

控制，a>0依固定有限lifts，常数依k,j/model/L。若只需粗界，允许另乘固定的(1+|x|)^m，仍可由Gaussian吸收。

L无非零格点趋0；结合格点壳数O((1+R)^3)，把(7)中的多项式和一半指数吸收，v≥1有

\[
 \boxed{\|D_v^j(K_L(v,\cdot)+1)\|_{C^k(M)}
          \le C_{k,j}e^{-a_Lv}.}
 \tag{8}
\]

对j>0，D_v已杀常数；对j=0，先显式加1再估。式(8)也用于固定dual格L^#，可取另一个正a_#。由(6)令w=1/v，

\[
 K_L(v)-c_L^{-1}v^{-3/2}
 =-c_L^{-1}v^{-3/2}(K_{L^\#}(w)+1),
\]

且D_v在右侧相当于v^−3/2(−3/2−D_w)。于是0<v≤1时每个固定k,j有

\[
 \boxed{\left\|D_v^j
    \bigl(K_L(v,\cdot)-c_L^{-1}v^{-3/2}\bigr)
        \right\|_{C^k(M)}
       \le C'_{k,j}v^{-3/2}e^{-a_\#/v}.}
 \tag{9}
\]

这些是全actual格／dual格和全部固定阶空间导数，不是只核literal x=0项。它们对当前fixed model/level成立；没有跨B、level、quotient或source-window成长的统一常数。

## 6. P0确实消两主项；不偷空间微分交换

按当前positive hyperbolic orbifold体积测度定义

\[
 P_0f=f-\operatorname{vol}_\mu(M)^{-1}\int_M f\,d\mu.
\]

M compact且体积有限，P0在任意固定C^k范数有界（若取usual sup-derivative最大范数，可用常数2）。因此

\[
 P_0K_L(v)=P_0(K_L(v)+1)
           =P_0(K_L(v)-c_L^{-1}v^{-3/2}).
\]

P0与D_v^j可交换，因为格点和及v导数在compact v区间正常收敛、空间积分有限；端点尾另由(8)/(9)控制。于是

\[
 \|D_v^jP_0K_L(v)\|_{C^k}
 \le\begin{cases}
    C_{k,j}e^{-a_Lv},&v\ge1,\\
    C'_{k,j}v^{-3/2}e^{-a_\#/v},&0<v\le1.
   \end{cases}
 \tag{10}
\]

这里没有声称P0与任意空间向量场或任意微分算子逐项交换。对杀常数的正阶空间导数，D_z(P0f)=D_zf，但P0(D_zf)一般不同；本证明只用P0的C^k有界性处理空间norm。后续用spectral Sobolev时可另按Δ与常数投影的实际相容性处理。

令

\[
 W_L(t,z)=e^{3t/4}P_0K_L(e^t,z).
\]

由(10)及∂_t=D_v，对所有固定k,j，

\[
 \|\partial_t^jW_L(t)\|_{C^k}
 \le\begin{cases}
 C_{k,j}e^{3t/4}e^{-a_Le^t},&t\ge0,\\
 C'_{k,j}e^{-3t/4}e^{-a_\#e^{-t}},&t\le0.
 \end{cases}
 \tag{11}
\]

因此对所有N,k,j≥0，sup_t e^(N|t|)||∂_t^jW_L(t)||_(C^k)<∞。W_L是C∞(M)-valued的S_exp核，特别在L²(dt;C^k)及每个fixed Sobolev阶中平方可积。这里只付款核本身的实际两端性质；r→Phi的原du/Dlog、能量和553消费由另一稿与root对齐。

## 7. 共轭、F∞与连通组件

w(barz)=overline(w(z))且x/B实，故R_g(x,barz)=R_g(x,z)。在u=0，(5)为实数并满足K_L(v,barz)=K_L(v,z)。共轭c:z↦barz与所有实Γ分式作用交换，因而下降到M；它是positive hyperbolic测度的保测等距映射。要区分：作为有向(1,1)形式的pullback，反全纯c满足c*μ=−μ；这里说的是用于正体积积分的measure保持，不是声称有向形式不变。

当前Γ\D至多两个连通组件。若Γ有交换两半平面的元素，则M连通；若无，则两个组件被c交换，体积相等，且K在两边按c相同，因此两个组件的平均值相同，等于全局平均。于是对当前actual K，P0K在每个组件分别mean-zero。这是本fixed模型及c对称性的额外实际核对，不是一般“globalmean-zero自动去除所有component常数”的错误规则；保留H¹或locally-constant closed base也始终合法。

P0及W保同一scalar共轭对称性。未来对实r积分时可得到实、c不变的smooth函数，复杂r应先从实空间作C线性复化；不能把实结构条件和对complex coefficient逐点再取共轭混成另一非线性条件。本稿不因此支付arithmetic a-map的height／7.4身份。

## 8. 归属、最强旧净值与停止

本稿是对明示R_g版本的explicit polynomialGaussian计算、普通Schwartz Poisson及compact finite-chart估计。没有新的外部论文／PDF下载或原作者定理proof消费；公式输入和模型恢复自当前项目的singlex/字面冻结记录。原literal R/K不能使用(4)–(11)，其失域反测及旧hash保持。

当前完整零模／核空间费用首门被标准Gaussian/Poisson直接支付，没有额外未知谱假设或新经典signed设施。建议标准准入0数学轮；后续若553按实际原du费用直接迫mixed退化，应按强旧合成结算并停止这个fixed recipe，不由本稿预建C048/585。

尚未给K_g modularity、作者Th7.4／自然height、arithmetic quotient的完整cycle/current身份、非零primitive容量、405关系消去、537同源非根、整过滤／截面乘法／mixedRR或完整经典Γ/contact/properpowers/双pole。最强经典whole leading4/5仍是负惯性UPPER，core/coupling/Ξ与长期Goal完成门未改。本稿不选择新candidate，不调ray/B/level/weight/阻尼或续后章；准入净值及停止由root统一消费。
