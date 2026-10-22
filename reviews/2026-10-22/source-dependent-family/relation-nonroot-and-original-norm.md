# 源依赖族的主关系、非根与原范数：实际构造及强旧扣除

2026-10-22。独占工作稿；不修改共同 STATE／cadence／合同，不执行 Git 写入。
恢复并核读 goals/README、STATE、check/show、G20261014、C035及D20261022A，
随后只消费405、519、520、537、552、553、568及所列原收据。

**结论：固定全部主关系的全线原范数连续类映射必退化，这已是553的旧结论，不能作为新合同。
源依赖的度量族可以明确写出，过单个p及r0并付原L²高度费，但它未消去p的平移。
真正的解析商／相对截面也可写出并过全部关系；其固定窗原范数费用有显式上界，
但其全局增长和谱性质仍属于519–526／553，未独立支付完整Weil容量。**

## 1. 坐标及两个实际见证

本稿的输入是物理源 (r(u)=e^{u/2}f(u))，不是405未中心化的f。
记 (C f=e^{u/2}f)，

\[
 F_r(z)=\int_{\mathbf R}e^{zu}r(u)du
       =M_f(\tfrac12+z),\qquad
 M_\pm(r)=F_r(\pm\tfrac12).
\]

对 (\mathcal A_{\exp}=C\mathcal S_{\exp,\mathbf C}=\mathcal S_{\exp,\mathbf C})，
F为整函数；compact源仅是其中的一个子类。405的实际关系为

\[
 \eta(x)=\pi x^2(\pi x^2-\tfrac32)e^{-\pi x^2},\quad
 h(u)=2\sum_{n\ge1}\eta(ne^u),\quad
 p=(\partial_u^2+\partial_u)h=E\eta_0,
\]

\[
 \eta_0(x)=(4v^4-28v^3+41v^2-9v)e^{-v},\quad v=\pi x^2.
\]

它有 (p\ne0\)、(c(p)=d(p)=0\)、(p\in P_{\rm an}\)，并且

\[
 M_p(s)=\frac{s(s-1)\xi(s)}2,\quad
 P=Cp=(\partial_u^2-\tfrac14)(Ch),\quad
 F_P(z)=\frac{(z^2-\tfrac14)\xi(\tfrac12+z)}2.       \tag{1}
\]

P是实偶非零的非compact关系，不是可直接放进fixed窗的测试函数。
所有普通平移 (\tau_aP\) 仍来自 (P_{\rm an}\)：

\[
 C^{-1}(\tau_aP)=e^{-a/2}\tau_a p\in P_{\rm an}.        \tag{2}
\]

固定非零实偶 (\psi\in C_c^\infty((-17/16,17/16))\)，令

\[
 r_0=(\partial_u^2-\tfrac14)\psi.
\]

分部积分给 (M_\pm(r_0)=0\)，紧支ODE唯一性给 (r_0\ne0\)，537完整源定理给

\[
 Q_W(r_0)\ge2^{-49162}\|r_0\|_2^2>0.                  \tag{3}
\]

由519的实际zero-jets像刻画，(C^{-1}r_0\notin I\)，尤其不在 (P_{\rm an}\)。
这里只使用已验收固定窗定理作非根见证，不用它推成长全源正性。

## 2. 必须先扣除553：全线稠密与非线性退化均已付

采用原零延拓范数

\[
 \|r\|_{D_{\log}}^2=(2\pi)^{-1}
       \int\log(2+|t|)|\widehat r(t)|^2dt.              \tag{4}
\]

553用的 (1+\log(2+|t|)\) 与(4)等价；这不是H¹／导数能量。
553 §2已经逐式消费523，证明

\[
 \overline{\operatorname{span}\{\tau_aP:a\in\mathbf R\}}^{L^2}
 =L^2,\qquad
 \overline{\operatorname{span}\{\tau_aP:a\in\mathbf R\}}^{D_{\log}}
 =D_{\log}.                                           \tag{5}
\]

原因是 (\widehat P(t)=F_P(-it)\) 为非零整函数在实轴上的限制，零集离散，
不需RH、简单性或间距。对所有平移正交时，带log权的乘积在L¹，Fourier唯一性迫其为零。
553 §4及旧cofinal-fees稿已明确包括以下**非线性**版本：若

\[
 T:\mathcal A_{\exp}\to Y
\]

值于Hausdorff空间，按同一个全线原norm连续，并且对所有关系平移及其有限线性组合q有

\[
 T(r+q)=T(r),
\]

则(5)使T常值。源依赖除子／metric并不凭“非线性”三个字绕过这个精确前提；
但以下情形不在其中：只按原Fréchet拓扑连续、只在各compact输入窗付C_L、
domain随L改变、输出是未分离的群胚／相对对象，或只有matched cocycle而非类不变。
不先给这些对象的拓扑，不能套(5)。

有显式逼近也不改变新旧归属：对compact smooth目标r，先选smooth频率cutoffχ_K，令

\[
 \widehat g_{K,\delta}(t)=
  \chi_K(t)\widehat r(t)\overline{\widehat P(t)}
       /(|\widehat P(t)|^2+\delta).
\]

它为compact smooth频率函数，g为Schwartz。先K增大再δ减小给
P*g→r于(4)。再将g乘compact cutoffχ_R，有

\[
 \|P*(g-\chi_Rg)\|_{D_{\log}}
 \le\|P\|_{D_{\log}}\|g-\chi_Rg\|_1\longrightarrow0.
\]

每个 (P*(\chi_Rg)=C(p*(e^{-u/2}\chi_Rg))\) 都在实际physical (P_{\rm an}\)。
逼近关系的支撑／Fréchet半范数不受同一个fixed窗口控制；不能据此说537矛盾。
这是旧(5)的显式实现，不能记新数学轮或新全对象后果。

## 3. 确实存在的源依赖metric族：单p测试通过，平移关系失败

以下对象区别于568的 (J_W=W*r\)，不读取未知零点。
先对实源定义原L²正交投影

\[
 A_Pr=r-\frac{\langle r,P\rangle_2}{\|P\|_2^2}P,
 \qquad
 \kappa_a(u)=(2\pi a)^{-1/2}e^{-u^2/(2a)},\quad a>0,
\]

\[
 \phi_r=\kappa_a*A_Pr,\quad
 c_r=\|\kappa_a\|_2\|A_Pr\|_2,\quad
 \Phi_r=c_r+\phi_r.                                   \tag{6}
\]

在 (X=\mathbf P^1_{\mathbf Q}\) 的底层线丛O上，有限位用标准metric，实位用

\[
 \|1\|_{r,\infty}(z)=e^{-\Phi_r(\log|z|)}.             \tag{7}
\]

对compact r与它们加P有限组合，Gaussian卷积使φ在 (u\to\pm\infty\) 比任意指数衰减，
故(7)在 (z=0,\infty\) 光滑延拓。它是conjugation-invariant smooth adelic metric，
按552 §3的固定曲率界证明逐源integrable；不是从Q反造的metric。
复源明确用Re r、Im r的两个有序metric，不把实metric暗当复线性几何。

实际原费用为

\[
 \|\phi_r\|_\infty\le c_r\le C_a\|r\|_2,
 \quad C_a=\|\kappa_a\|_2=(2\sqrt\pi\sqrt a)^{-1/2},
\]

\[
 \|\phi'_r\|_2^2\le(ae)^{-1}\|r\|_2^2,
 \quad 0\le\Phi_r\le2C_a\|r\|_2.                     \tag{8}
\]

因此原sup-height及Dirichlet energy由原du norm支付，亦由(4)支付。
逐源compactification曲率／nef-difference的费用不能称为同一uniform常数：
当supp r⊂[-L,L]，加权Gaussian导数估计只给

\[
 \sup_u\cosh^2u\,|\phi_r''(u)|
       \le C_{a,P}(1+e^{2L})\|r\|_2.                  \tag{9}
\]

这足以解释每源smooth/integrability，未把成长费用消去。

单p关系由A_PP=0严格消去；r0不能是P的标量倍（否则违(3)），Gaussian卷积又单射，
故φ_{r0}非零。其vertical交数为 (-\|\phi'_{r0}\|_2^2<0\)，不是base常数类。
于是这个实际族通过**指定单p／r0**的前端测试。

可是任意a≠0有 (A_P(\tau_aP)\ne0\)：非零L²函数不能是非零平移的特征向量，
Fourier侧仅离散频率支撑也证明这一点。因此(7)把另一个实际principal关系(2)送到非零能量类。
这不是主关系下降，不经全部 (P_{\rm an}\) 的商；只验一个generator不足。

此族仍有真实全局section 1：底层integral (H^0(O)=\mathbf Z\)。令

\[
 d(r)=\inf_{X(\mathbf C)}\Phi_r=c_r+\inf_u\phi_r,
 \quad0\le d(r)\le c_r.
\]

其sup小截面精确为 (|m|\le e^{d(r)}\)，有限闭处N的restriction核仍为N Z，
存在非零消失小截面 iff (\log N\le d(r)\)。这是同一对象的预算，但d是外加的原metric高度，
section 1在有限位消失量全零；没有从r独立产生完整prime-power消失阶。
它既不等于Q，也未区别连续正反例；加入r依赖N再用c_r支付只是人为编码。

## 4. 全部关系可过的实际解析截面／相对对象

另稿采用

\[
 \Xi(z)=\xi(\tfrac12+z),\quad
 H(z)=(z^2-\tfrac14)\Xi(z),\quad D=\operatorname{div}H.
\]

这是复平面上局部有限的analytic Cartier divisor，含全部通常零点及重数和两个degree点±1/2。
不要求其支撑在虚轴，也不是fixed projective finite Cartier divisor。
有actual global meromorphic section

\[
 r\longmapsto s_r=F_r/H\in\Gamma(\mathbf C,O(D)),
\]

及其除去entire sections的类，等价于

\[
 T(r)=F_r\bmod H\in\Gamma(\mathbf C,O/(H)).            \tag{10}
\]

由519，kerT恰为physical (P_{\rm an}\)，不是仅值消失商，也不是Q根商。
因此(1)的p过关，(3)的r0非零；±1/2的两个点保留405的degree数据。
这是合法解析商的几何包装；局部jets／零除子由完成函数H定义，不能冒称新算术容量。

这个商也**不是Q的最小非退化商**。405的 (r_h=Ch\) 有
F_{r_h}(±1/2)=1/4，故(10)中的类非零，但完整Q(r_h)=0，因为h∈I。
给全部(10)类一个faithful正metric然后声称其energy恰为Q，已经被这个旧见证排除。
保留degree plane时必须同时保signed degree配对／matched pole cocycle；
若改用Xi商消去全I，则两个degree方向需由另一同源预算协同恢复，不能静默删去。

**类型检查：** underlying O(D)由固定H决定；源变的是marked section，而不是其line-bundle class。
去掉marked section时每个r落到同一line-bundle class，r0可见性便丢失。
literal affine方程 (H(z)w=F_r(z)\) 在H=0、F_r≠0处fiber空，common zeros处整条A¹；
不能未经紧化、饱和及base-change检查把它当作全局section、flat或finite correspondence。
正确无歧义对象是上述O(D)截面或torsion restriction类。

## 5. (10)的fixed窗原du／Dlog费用：哪一项exact

对 (r\in C_c^\infty((-L,L))\)、k≥0及z=σ+iγ，

\[
 F_r^{(k)}(z)=\int_{-L}^L u^k e^{zu}r(u)du,
 \quad
 \|F_{(\cdot)}^{(k)}(z)\|_{L^2(-L,L)^*}^2
       =\int_{-L}^L u^{2k}e^{2\sigma u}du.             \tag{11}
\]

这是原L²的精确squared fee，利用compact smooth在L²稠密取得operatornorm。
在compact base |Re z|≤A上直接有

\[
 |F_r^{(k)}(z)|\le\sqrt{2L}\,L^k e^{AL}\|r\|_2.       \tag{12}
\]

没有假定经典零点实部。z在D上时可无RH用0<Reρ<1及degree点取A=1/2。
这给每fixed窗到局部jets的真实连续性，费用随窗增长，不能代全线uniform norm。
原Fréchet的全局源到compact-open analytic sheaf拓扑连续亦成立；两个拓扑不可混同。

**Dlog不是(11)的同一精确积分。** 设 (g_{z,k,L}(u)=1_{[-L,L]}u^k e^{\bar z u}\)，
将其延成全线dual element，只可直接消费

\[
 \|F_{(\cdot)}^{(k)}(z)\|_{D_{\log},(-L,L)^*}^2
 \le(2\pi)^{-1}\int
       |\widehat g_{z,k,L}(t)|^2/\log(2+|t|)\,dt.     \tag{13}
\]

右边是指定全线dual extension的费；restricted subspace的最小dual extension可能更省。
hard-window有端点尾，但(13)合法，不把它改成periodic／regional范数。
553已经独立证明，对L≥1、ALL γ及固定k，临界线jet的实际restricted dual费满足

\[
 \|F_{(\cdot)}^{(k)}(i\gamma)\|^2
       \asymp_k\frac{L^{2k+1}}{1+\log(2+|\gamma|)}.    \tag{14}
\]

对每先fixed σ≠0、γ及k，则

\[
 \|F_{(\cdot)}^{(k)}(\sigma+i\gamma)\|^2
       \asymp_{\sigma,\gamma,k}L^{2k}e^{2|\sigma|L}
       \quad(L\to\infty).                            \tag{15}
\]

σ→0不可偷换一致渐近；fixed k也不能代全部未知multiplicity jets的uniform共同Gram。
即使所有对角费用都付，全高度、全jets、联合operatornorm仍需独立比较。

O/(H)中以F的Taylor coefficients定义的局部jet范数，与F/H的principal-part系数范数不同：
后者含H的leading derivative之倒数及高阶unit展开。对任意已固定的有限个点它们等价，
但该等价常数不能免费uniform于高度、重数或相邻零点间距。未把这些新选择叫自然正metric。

## 6. 完整Weil责任及本稿净消费

完整目标保持568的原Q，含

\[
 \Gamma_0=\psi(1/4)-\log\pi,\quad
 w(v)=2e^{-v/2}/(1-e^{-2v}),\quad
 a_{p^k}=\log p\,p^{-k/2},\quad M_\pm(r)=F_r(\pm1/2).
\]

Γ有限部分及contact、全部proper powers、两pole的mixed配对均未删除。
它们在旧显式公式下与完成化谱相等，不表示(6)的positive height或(10)的analytic局部长度
已独立给出相同的Weil预算差。真实新输入应是**同一个实际截面／相对对象**的
局部消失整除与原高度／容量，独立有利符号及全复杂组合误差控制；仅重新令其差等于Q仍等价改写。

本稿给出具体候选、原费用及失败位置，未产生新的经典正性或whole预算。
553的稠密／nonlinear常值、519/520的analytic quotient及553的窗口jet费用均明确归旧。
强旧542＋555→557 whole leading4/5上预算、actual成长core/coupling/Ξ未改变。
保留合法Fréchet／cofinal／relative-cocycle／非局部／source-dependent几何修复；
本次不以旧结论开C036，不计573，不扩大相同metric参数寻找虚假增量。

### 核读的最强旧短链

- 405 §§4–6：p、两degree及指定实际解析关系；不是几何principal定理。
- 519 §§1–4：实际像=完整zero-jets，Pan另有两个degree条件。
- 552 §§3–5：naive metric真实存在但不下降，H¹费用不代log-Γ。
- 553 §§1–5及reviews/2026-10-14/principal-quotient-norm：原norm稠密、nonlinear／cofinal精确范围，(14)–(15)。
- 537 §2／4：r0的完整Q固定窗严格正，包含Γ／pp／pole和Dlog core。
- 568 §§5–6：J_W的旧signed实现、point费用／smooth修复和预算身份的等价责任。

没有新增外部文献定理，以上纯解析／metric推导基于已列原件，未声称重读全部仓库。
