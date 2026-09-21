# 419. 原时间交叉积、深边界环面与普通迹的接口

2026-09-21。[全文独立逆审通过；范围内结构与障碍] 继续[417–418后的有限准入](../reviews/2026-09-21/f1-original-time-crossed-product-next-proof-plan.md)。
保持原物理时间β；不再用同一个连接迹差完成主补偿。
本稿构造实际交叉积，追踪原源与原算术读出，并定位下一项必须支付的相对比较。

## 1. 固定原作用，直接解耦联合群

沿用[414](414-f1-deep-boundary-unitary-and-time-defect.md)的
\(X=T_0^2,\ T_0=\mathbb Z\cup\{\infty\}\)，\(d=(\infty,\infty)\)，
\(\Gamma=\mathbb Z^2,\ell_g=g_1L+g_2M\)，\(L=\log p,M=\log q\)。
记
\[
 A=C_0(X\times\mathbb R)\rtimes_\alpha\Gamma,\qquad
 \mathfrak B=A\rtimes_\beta\mathbb R .
\]
\(\alpha_gf(y,t)=f(y-g,t-\ell_g)\)，
\(\beta_sf(y,t)=f(y,t-s)\)，且 \(\beta_s(P_g)=P_g\)。
新时间交叉积的规范群乘子记 \(V_s\)，故 \(V_sP_g=P_gV_s\)。

迭代协变表示就是 \(\Gamma\times\mathbb R\) 的协变表示，联合作用为
\[
 \gamma_{(g,s)}f(y,t)=f(y-g,t-\ell_g-s).
\]
作保持 Haar 测度的群同构 \((g,r)\mapsto(g,r-\ell_g)\)，得到分离作用
\[
 \widetilde\gamma_{(g,r)}f(y,t)=f(y-g,t-r).
\]
对应的真实新乘子是
\[
 Z_g=P_gV_{-\ell_g},\quad
 Z_gf(y,t)Z_g^*=f(y-g,t),\quad
 Z_gZ_h=Z_{g+h},\quad Z_gV_s=V_sZ_g,\quad
 P_g=Z_gV_{\ell_g}.                                             \tag{1}
\]
没有额外二阶cocycle。径向协变对与时间协变对彼此交换；
反过来，任意两对这样的交换协变表示经(1)恢复原作用，给出双向普遍性质。

令
\[
 \mathfrak C=C_0(X)\rtimes\Gamma_{\rm rad},\qquad
 \mathbb K_t=\mathbb K(L^2(\mathbb R)).
\]
以下将直接证明
\[
 \Phi:\mathfrak B\xrightarrow{\cong}\mathfrak C\otimes\mathbb K_t. \tag{2}
\]
这不是以Thom的K群同构替代实际代数构造。

## 2. 稠密卷积核及范数完成

稠密核写成
\[
 F=\sum_g\int F_g(s;y,t)P_gV_s\,ds,
\]
其中群支有限，系数连续紧支。原卷积为
\[
 (F*G)_k(s;y,t)
  =\sum_g\int F_g(r;y,t)
       G_{k-g}(s-r;y-g,t-\ell_g-r)\,dr .
\]
定义
\[
 k_g(y;t,t')=F_g(t-t'-\ell_g;y,t).                               \tag{3}
\]
直接换元得到
\[
 (k*l)_k(y;t,t')=\sum_g\int k_g(y;t,u)l_{k-g}(y-g;u,t')\,du,
 \qquad
 (k^*)_g(y;t,t')=\overline{k_{-g}(y-g;t',t)}.                     \tag{4}
\]
群均为 unimodular，变换只涉及平移，没有遗漏模函数或Jacobian。

若 \(k_g(y;t,t')=a(y)\xi(t)\overline{\eta(t')}\)，则
\[
 \Phi(F)=(a z_g)\otimes|\xi\rangle\langle\eta|,
 \qquad
 F_g(s;y,t)=a(y)\xi(t)\overline{\eta(t-\ell_g-s)}.                 \tag{5}
\]
这里 \(z_g\in M(\mathfrak C)\) 是规范径向群乘子；
\(a\in C_c(X)\)、\(\xi,\eta\in C_c(\mathbb R)\) 时逆核确实紧支。
(4)证明(5)保持乘法和伴随。

时间因子 \(C_0(\mathbb R)\rtimes_{\rm trans}\mathbb R\) 的Schrödinger表示
将核 \(F(s;t)\) 送为 \(F(t-t';t)\)。
任意紧支连续核可在固定紧矩形上由有限分离核一致逼近；
逆变换后，\(L^1(ds;\|\cdot\|_\infty)\) 误差由有限时间区间长度乘一致误差控制。
所以这些秩一核在普遍交叉积范数中稠密。
每个有限秩矩阵角的C*范数唯一，且Schrödinger表示在该角非零，
故这个完成恰为 \(\mathbb K_t\)。

第1节的普遍性质先给
\(\mathfrak B\cong\mathfrak C\otimes_{\max}\mathbb K_t\)；
紧算子的有限矩阵角使最大与最小张量范数相同。
因此(2)是等距满射，(3)–(5)就是其实际核公式。
若使用约化交叉积，\(\Gamma,\mathbb R\) 可和，结论相同。

## 3. 乘子、理想与深边界图

记 \(\mathsf T_s\psi(t)=\psi(t-s)\)。同构的非退化乘子延拓满足
\[
\begin{aligned}
 \overline\Phi(a(y)b(t))&=i_X(a)\otimes M_b,\\
 \overline\Phi(P_g)&=z_g\otimes\mathsf T_{\ell_g},\\
 \overline\Phi(V_s)&=1\otimes\mathsf T_s,\\
 \overline\Phi(Z_g)&=z_g\otimes1.                                \tag{6}
\end{aligned}
\]
这些是乘子公式：例如非零乘法算子 \(M_b\) 通常不紧。
原 \(A\) 的规范像首先在 \(M(\mathfrak B)\) 中，不是默认包含于 \(\mathfrak B\)。

记 \(X_0=\mathbb Z^2,\ X_I=X\setminus\{d\}\)，
\[
 \mathfrak J=C_0(X_0)\rtimes\Gamma_{\rm rad},\qquad
 \mathfrak I=C_0(X_I)\rtimes\Gamma_{\rm rad}.
\]
核变换完全不改 \(y\)，所以
\[
 J\rtimes_\beta\mathbb R\cong\mathfrak J\otimes\mathbb K_t,\quad
 I\rtimes_\beta\mathbb R\cong\mathfrak I\otimes\mathbb K_t,\quad
 A_D\rtimes_\beta\mathbb R\cong C(\mathbb T^2)\otimes\mathbb K_t.    \tag{7}
\]
最后的商映射是令 \(y=d\)；该点的径向作用平凡。
这些同构逐项交换 \(J\subset I\subset A\) 的理想及商图。

开放层中的
\(e_{mn}=\mathbf1_{\{m\}}z_{m-n}\) 是实际矩阵单位，故
\[
 \mathfrak J=\mathbb K(\ell^2\Gamma).
\]
两边层的商是
\[
 \mathfrak I/\mathfrak J
 \cong
 \bigl(C(\mathbb T_p)\otimes\mathbb K(\ell^2\mathbb Z_q)\bigr)
 \oplus
 \bigl(\mathbb K(\ell^2\mathbb Z_p)\otimes C(\mathbb T_q)\bigr).    \tag{8}
\]
它们的时间交叉积就是再张量 \(\mathbb K_t\)。
这里完整保留两个边方向与深边界环面，没有先取普通K群再选抽象生成元。

## 4. 原414积分表示仍然忠实

按原径向坐标基识别 \(\mathcal H_{\rm rad}=\ell^2\Gamma\)，414的表示为
\[
 (\pi(f)\psi)_m(t)=f(m,t)\psi_m(t),\quad
 \pi(P_g)=\lambda_g\otimes\mathsf T_{\ell_g},\quad
 U_s=1\otimes\mathsf T_s ,
\]
其中 \((\lambda_g\xi)(m)=\xi(m-g)\)。
因此在(2)下，积分表示 \(\Pi=\pi\rtimes U\) 是
\[
 \Pi=(\sigma\otimes{\rm id})\Phi,\qquad
 \sigma(a)\xi(m)=a(m)\xi(m),\quad \sigma(z_g)=\lambda_g.           \tag{9}
\]

需要另证 \(\sigma\) 忠实。对规范 \(\mathbb T^2\) 作用平均得到
\(E:\mathfrak C\to C_0(X)\)。
平均忠实：若正元素平均为0，对任意正泛函得到连续非负函数的积分为0，
该函数在单位点也为0。固定点代数为 \(C_0(X)\)，可由有限群多项式逼近核准。
对每个 \(b\in\mathfrak C\)，同样由有限多项式逼近，
\[
 \langle\delta_m,\sigma(b^*b)\delta_m\rangle=E(b^*b)(m).
\]
若 \(\sigma(b)=0\)，右侧在 \(\mathbb Z^2\) 恒零；
此集合在 \(T_0^2\) 稠密，连续性给 \(E(b^*b)=0\)，遂有 \(b=0\)。
所以
\[
 \ker\Pi=0,\qquad
 \Pi(J\rtimes\mathbb R)=\mathbb K(\ell^2\Gamma\otimes L^2\mathbb R). \tag{10}
\]
没有从原 \(\pi\) 忠实直接推出时间交叉积表示忠实。

联合Fourier表示中，原乘子可写为
\[
 P_p=\zeta_p e^{-iL\xi},\quad
 P_q=\zeta_q e^{-iM\xi},\quad
 V_s=e^{-is\xi},
\]
其中 \((\zeta_p,\zeta_q)\in\mathbb T^2\) 与 \(\xi\in\mathbb R\) 独立。
于是 \(Z_p=\zeta_p,Z_q=\zeta_q\) 保留完整联合谱。

## 5. 完整代数未被开放层的紧化吞掉

换坐标 \(x=t-\ell_m\) 的酉变换满足
\[
 P_g\mapsto\lambda_g\otimes1,\quad
 V_s\mapsto1\otimes\mathsf T_s,\quad
 Z_g\mapsto\lambda_g\otimes\mathsf T_{-\ell_g},\quad
 f(m,t)\mapsto f(m,x+\ell_m).                                   \tag{11}
\]
因此原 \(J=C_0(\mathbb R_x)\otimes\mathbb K(\ell^2\Gamma)\)
经时间交叉积成为全空间紧算子；但一般 \(f(m,x+\ell_m)\) 没有统一消失，
不能将结论套到整个 \(A\)。

例如 \(Q(y)=H(j)H(k)\in C_c(X)\)，取时间单位向量
\(\xi_0\in C_c^\infty(\mathbb R)\)、\(k_0=|\xi_0\rangle\langle\xi_0|\)。
则 \(Q\otimes k_0\in\mathfrak C\otimes\mathbb K_t\)，深边界商为
\(1\otimes k_0\ne0\)。它固定无穷正交向量
\(\delta_{(n,0)}\otimes\xi_0\)，所以不紧。
在 \(x\) 坐标下只是非零块范数始终为1的秩一直和，时间支撑移动不使范数趋零。
\((Qz_g)\otimes k_0\) 的商为 \(\chi_g\otimes k_0\)，故全部环面Fourier模式都有实际原像。

还须避免把 \(V_s,Z_g\) 倒放进原 \(M(A)\)。
原 \(M(A)\) 限制到 \(M(J)=M(C_0(\mathbb R_x)\otimes\mathbb K)\)
后与中心乘子 \(M_{\varphi(x)}\) 交换；
(11)中的非零时间平移不交换，故 \(s\ne0\) 时 \(V_s\notin\pi(M(A))\)。
同理，\(g\ne0\) 时 \(\ell_g\ne0\)，\(Z_g\notin\pi(M(A))\)。
它们是新交叉积的乘子，这不妨碍(1)–(7)成立。

## 6. 仅时间的边界表示确实丢失参数

深边界商、径向常值系数的乘子副本以及原完整表示是不同对象。
原 \(\Pi\) 在 \(I\rtimes\mathbb R\) 非零，不能直接下降到深边界商。
但是乘子中存在忠实嵌入
\[
 C(\mathbb T^2)\otimes\mathbb K_t\longrightarrow M(\mathfrak B),
 \qquad \chi_g\otimes k\longmapsto z_g\otimes k;                 \tag{12}
\]
其原表示含径向正则表示，完整保留 \(\mathbb T^2\)。

另选仅在 \(L^2(\mathbb R)\) 上的边界协变表示
\[
 f\mapsto M_f,\quad P_g\mapsto\mathsf T_{\ell_g},\quad
 V_s\mapsto\mathsf T_s
\]
时，\(Z_g\mapsto1\)。
其积分表示准确为 \({\rm ev}_{(1,1)}\otimes{\rm id}\)，核是
\[
 C_0(\mathbb T^2\setminus\{(1,1)\})\otimes\mathbb K_t.             \tag{13}
\]
联合谱被限制为
\((P_p,P_q,\xi)=(e^{-iL\xi},e^{-iM\xi},\xi)\)。
前两坐标的投影虽稠密，带频率的联合谱仍只是一个真闭图像；
不能以这种投影稠密性推断时间交叉积表示忠实。

## 7. 原算术周期算子位于开放理想

追踪414的原 \(C_N=E_p\otimes M_c+E_q\otimes M_{d_q}\)。
每个 \(E_\alpha\) 是径向有限秩投影，故属于
\(\mathfrak J=\mathbb K(\ell^2\Gamma)\)，而时间乘法是 \(\mathbb K_t\) 的乘子。
因此 \(C_N\in M(\mathfrak B)\)，并不是把它误认为新代数内的投影。

按(6)，原次序的单项压缩给
\[
 C_NP_gU(h)C_N
 =\sum_{\alpha,\beta}
 E_\alpha\lambda_g E_\beta
 \otimes M_{d_\alpha}\mathsf T_{\ell_g}U(h)M_{d_\beta}.           \tag{14}
\]
时间核为 \(d_\alpha(t)h(t-t'-\ell_g)d_\beta(t')\)，是光滑紧支核。
每项因此在 \(\mathfrak J\otimes\mathbb K_t\) 中。
414的全Γ迹范数收敛于是给
\[
 A_N(h)\in J\rtimes\mathbb R .
\]
418的纠正算子同样满足
\[
 A_N^c(h)\in J\rtimes\mathbb R.                                 \tag{15}
\]
可由其实际核逐项证明，也可直接用(10)：418已证明它是原Hilbert空间上的迹类算子，
而(10)将全部紧算子识别为这个理想，故有唯一原像。

因此两个算子在两边商和深边界商中的普通像都为0。
它们的普通迹却不因此为0：选择 \(h(-L)=1\)，支集靠近 \(-L\)，
避开0、其余p周期及全部q周期，414给
\[
 \tfrac12\operatorname{Tr}A_N(h)=L\rho_p\ne0
 \quad\text{对所有 }N_p,N_q\ge0.                               \tag{16}
\]
所以不能通过“先取这些算子的普通边界商像，再施加线性泛函”恢复这个周期读出。
这没有否定相对类、边界传递或非连续的重整化过程；
它明确指出这些额外步骤尚未被(2)的代数同构提供。

## 8. 规范普通迹不能有限地扩张到所需边投影

在径向代数中，置
\[
 E=H(j)\mathbf1_{\{k=0\}},\qquad
 S=E z_{(1,0)} E,\qquad r=\mathbf1_{\{(0,0)\}}.
\]
它们属于 \(\mathfrak I\)，在忠实轨道表示中是非负p链上的单边移位及端点，
因此
\[
 S^*S=E,\qquad SS^*=E-r.                                       \tag{17}
\]
张量前述时间秩一投影 \(k_0\)，记
\(\widetilde E=E\otimes k_0,\widetilde S=S\otimes k_0,\widetilde r=r\otimes k_0\)。
同一关系仍成立，且 \(\widetilde r\) 是原全Hilbert空间上的秩一投影。

若一个有限值线性泛函 \(\tau\) 的定义域含这些元素及乘积，
满足循环性并扩张原紧算子迹，则
\[
 \tau(\widetilde E)
 =\tau(\widetilde S^*\widetilde S)
 =\tau(\widetilde S\widetilde S^*)
 =\tau(\widetilde E)-1,
\]
矛盾。等价地，
\[
 \operatorname{Tr}[\widetilde S^*,\widetilde S]=1,                \tag{18}
\]
其中交换子确在紧算子理想；不能把普通迹的循环性应用于两个不迹类的因子。

同样，若迹权的有限正值锥在 \(\mathfrak B_+\) 中范数稠密且其在开放理想上等于普通迹，
选正有限值 \(a\) 使 \(\|a-\widetilde E\|<1/2\)。
有 \(\widetilde E a\widetilde E\ge\frac12\widetilde E\)，且迹性质给
\[
 \tau(\widetilde E a\widetilde E)
 =\tau(a^{1/2}\widetilde E a^{1/2})\le\tau(a)<\infty .
\]
于是 \(\tau(\widetilde E)<\infty\)，再次与(17)及 \(\tau(\widetilde r)=1\) 冲突。
这里明确要求范数稠密的有限正值锥；没有否认在 \(B(\mathcal H)\) 上取值无穷的普通算子迹。
那个普通迹在本例的 \(\widetilde E\) 上为无穷，不能直接当作所需有限边界泛函。

所以若继续从原迹走向相对循环特征，必须携带(18)的实际迹缺陷，
不能宣布有限部分“仍然循环”。这一限制只针对保留原紧算子归一化的此类扩张。

## 9. 原源酉元在深边界中仍只是乘子族

在深边界(7)中取参数 \(\zeta=(\zeta_p,\zeta_q)\in\mathbb T^2\)。
原实际对象的乘子像是
\[
\begin{aligned}
 e_\zeta&=\sum_n\zeta_p^n
   M_{c(t)c(t-nL)}\mathsf T_{nL},\\
 v_\zeta&=\sum_n\zeta_p^n\zeta_q
   M_{c(t)c(t-nL-M)}\mathsf T_{nL+M},\\
 u_\zeta&=1-e_\zeta+v_\zeta .                                  \tag{19}
\end{aligned}
\]
有限和给范数连续的参数族，仍满足原投影／角内酉关系。
但它们不能直接冒充 \(C(\mathbb T^2)\otimes\mathbb K_t\) 或其单位化中的原K类代表。

具体地，将 \(L^2(\mathbb R)\) 按 \(t=s+jL,\ 0\le s<L\) 分解。
\(e_\zeta\) 的纤维矩阵为
\[
 (e_\zeta(s))_{jk}
 =\zeta_p^{j-k}c(s+jL)c(s+kL)
 =a_\zeta(s)_j\overline{a_\zeta(s)_k},\quad
 a_\zeta(s)_j=\zeta_p^j c(s+jL).
\]
\(\|a_\zeta(s)\|_2=1\)，所以
\[
 (\mathcal G_\zeta f)(s+jL)=\zeta_p^j c(s+jL)f(s)
\]
是 \(L^2([0,L))\) 到 \(e_\zeta L^2(\mathbb R)\) 的满等距映射。
故 \(e_\zeta\) 是无限秩投影，不紧。

写 \(s-M=r+kL,\ 0\le r<L\)。
将(19)逐项作用到 \(\mathcal G_\zeta f\)，平方分割给
\[
 (\mathcal G_\zeta^*v_\zeta\mathcal G_\zeta f)(s)
       =\zeta_q\zeta_p^k f(r).                                 \tag{20}
\]
固定一个实参数 \(\theta_p\) 使 \(\zeta_p=e^{i\theta_p}\)；
这是单个参数点的选择，不是声称环面上存在全局连续辐角。
正交基
\[
 f_m(s)=L^{-1/2}e^{i(\theta_p+2\pi m)s/L},\qquad m\in\mathbb Z
\]
由(20)给特征值
\[
 v_\zeta:\quad
 \lambda_m=\zeta_q e^{-i(\theta_p+2\pi m)M/L}.                    \tag{21}
\]
由于 \(M/L\) 无理，这些特征值在单位圆稠密。
故 \(u_\zeta-1\) 在正交序列 \(\mathcal G_\zeta f_m\) 上有无穷多个模长离0有界的特征值，
所以不紧。在 \(1-e_\zeta\) 的无限维像上 \(u_\zeta=1\)，
因此也不能通过改用另一个标量 \(\lambda1\) 使 \(u_\zeta-\lambda1\) 紧。
结论为
\[
 u_\zeta\notin\mathbb C1+\mathbb K_t
 \quad\text{对每个 }\zeta.                                     \tag{22}
\]

原 \(u\in A_D^\sim\) 没有消失；它是新交叉积的合法乘子。
若要将 \([u]\in K_1(A_D)\) 沿时间交叉积送成实际 \(K_0\) 对象，
还须构造真正的Thom／Fredholm代表并核准原源及定向，不能把(19)本身当成该构造。

## 10. 当前交付与下一有限命题

本稿完成实际代数同构、全部层图、原积分表示忠实性、原周期算子的开放理想位置，
以及保留普通迹归一化的有限循环扩张限制；还给出源乘子族及其非紧性的精确谱计算。
这些结构保留了完整环面参数，但尚未提供所需算术主消失。

下一步以(19)的实际族为输入，固定时间Fourier约定，
检验正频率投影 \(P_+\) 与 \(u_\zeta\) 的交换子是否形成连续紧算子族，
从而构造 \(P_+u_\zeta P_+\) 的实际Fredholm族。
随后计算其指数丛、点指数和过渡数据，核准Thom/Bott符号；
即使得到整数或Bott类，仍须另证与原周期函数式的比较。
不按预期选择某个抽象生成元代替原源，也不把一个新的K群表示当作F₁存在性证明。

## 11. 来源、独立推导与形式化范围

[原时间交叉积的独立构造全文](../reviews/2026-09-21/f1-original-time-crossed-product-derivation.md)
及[原始回包](../reviews/2026-09-21/f1-original-time-crossed-product-derivation.raw.json)
覆盖第1–6节的基础构造。
本稿另外追踪原周期算子、有限迹扩张与原源的实际非紧谱；全文另作独立逆审。

[作者原文增量核读](../reviews/2026-09-21/f1-original-time-crossed-product-source-read.md)
记录Williams的迭代交叉积、内作用比较、可和性，
以及Blackadar的Thom定义、自然性与实线平移基例。
本稿直接给出具体同构，未使用这些一般结果省略原表示或算术比较。
时间交叉积、无限维迹权及完整F₁结构未被现有Lean代数记录形式化。

## 12. 全文验收与Lean边界

[全文独立逆审](../reviews/2026-09-21/f1-original-time-crossed-product-full-review.md)及[原始回报](../reviews/2026-09-21/f1-original-time-crossed-product-full-review.raw.json)
覆盖原十一节及(1)–(22)，没有必要数学改正；审稿时SHA256为
2c68f5bf15a7137228eb4808c73b112d5cab4299db810afa29f7c92312169372。
正文第1–11节保持该审稿版本；第10节的下一任务随后见[420](420-f1-source-hardy-index-and-dual-action.md)，不能倒算为419的已证内容。

第8节有限值障碍实际只需与有限秩的普通迹归一化相符，不要求所有紧算子有有限迹。
[ShiftTraceObstruction.lean](../formal/F1/Analysis/ShiftTraceObstruction.lean)把三个代数步骤形式化：
移位交换子等于端点缺陷、循环加性泛函消去缺陷、非零端点读出与循环性冲突。
[内核报告](../formal/checks/shift-trace-obstruction-verification.json)由固定Lean4.32.2通过，无sorryAx；
报告SHA256为a06d4dad8aa043574dd05657a7dc3fa9d477004deda79d194078a396d9cd6bc8。
实际交叉积、无限维算子实现、无穷值迹权和范数稠密性分析仍不在这些Lean引理的范围。
