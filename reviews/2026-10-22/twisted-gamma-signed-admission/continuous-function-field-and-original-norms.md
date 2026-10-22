# 578后同源双变量核准入：连续／函数域联检与原源费用

2026-10-22；独占分支，供root消费，不自行建合同／计轮。已恢复STATE、Goal、C041、frontier，并运行state check/show。下列是131／132、562、576–578旧资产的具体比较与反测，**未取得独立经典q_R小费，不作为新数学轮或RH输入**。

## 1. 候选核的准确对象、符号和边界

固定去全极点后的canonical entire completion，中心变量z=s−1/2，记
\[
 \Phi(z)=\xi(1/2+z),\quad A(z)=\Phi'(z)/\Phi(z),\qquad
 K(z,w)=\frac{A(z)+\overline{A(w)}}{z+\bar w}.             \tag{1}
\]
这是旧[131(5)、XQ／XR](../../../notes/131-positive-real-boundary-impedance-weil.md)的**同一个核**，不是新的Christoffel–Darboux设施。K在Re z,Re w>0且A无极点的区域Hermitian；分母在该区域不为零。其对角是
\[
 K(z,z)=\frac{\Re A(z)}{\Re z},                          \tag{2}
\]
没有额外2。关于虚轴的奇实型对称给A(it)纯虚（该点非pole时）。法向边界对角极限为
\[
 \lim_{x\downarrow0}K(x+it,x+it)=A'(it)\in\mathbb R.     \tag{3}
\]
它是导数极限，不是把分母直接置0；有zero/pole的边界点不声称有限极限。对任意off-axis zero，A有真实正整数residue的pole，不能先假定(1)在全右半平面全纯。

在classical Euler安全域Re s>1，全部数据给
\[
 A(z)=\frac1s+\frac1{s-1}-\frac12\log\pi
       +\frac12\psi(s/2)-\sum_{n\ge2}\Lambda(n)n^{-s}.    \tag{4}
\]
所有powers、两个pole和完整Γ均在同一个A中；FE只给奇对称，不给K正性。全右半平面holomorphic/passive或所有有限Pick Gram正性的RH等价，131已证明，不能再计新。

### 1.1 核确与完整linear Weil预算相等，但不是自动正平方

取physical半轴源
\[
 r_z(u)=e^{-zu}\mathbf1_{u\ge0},\quad \Re z>1/2,
 \qquad f_z=e^{-u/2}r_z=e^{-su}\mathbf1_{u\ge0}.          \tag{5}
\]
它们属于原du／zero-extension Dlog，通常不属于S_exp。直接卷积
\[
 (r_z*r_w^*)(u)=\frac1{z+\bar w}
 \begin{cases}e^{-zu},&u\ge0,\\e^{\bar w u},&u<0.\end{cases}       \tag{6}
\]
完整偶分布Wζ在这些指数尾／原点Lipschitz测试上有合法延拓：powers与pole由Re z,Re w>1/2绝对收敛，Γ有限部分在原点的差为O(|u|)，可积。实际局部公式给
\[
 \tfrac12 W_\zeta(e^{-z|u|})=A(z),\qquad
 B_{W_\zeta}(r_z,r_w)=K(z,w).                            \tag{7}
\]
具体Γ部分恰为
\[
 \tfrac12\Gamma(0)+\int_0^\infty a(v)(1-e^{-zv})dv
       =\tfrac12\psi((z+1/2)/2)-\tfrac12\log\pi,
 \quad a(v)=e^{-v/2}/(1-e^{-2v}).
\]
H部分给1/(z−1/2)+1/(z+1/2)，P部分给ΣΛ(n)n^(−z−1/2)，故(7)没有省略contact、pole或proper power。它是**已有linear预算在特定Laplace源上的Hermitian表示**；若再宣称此核为positive Gram，就把所需signed比较重新作为前件。

## 2. 连续正负：同一安全两点精确Gram

用562／578已证明真正positive primitive与positive g-integers的同族
\[
 Z_c(s)=1+c/[s(s-1)],\quad E_c(s)=(s-1/2)^2+d,
 \quad d=c-1/4.
\]
它的native Γ=0、全pole为0,1，不外加经典Γ。其A与核是原数据的有理恒等式
\[
 A_d(z)=\frac{2z}{z^2+d},\qquad
 K_d(z,w)=\frac{2(z\bar w+d)}{(z^2+d)(\bar w^2+d)}.       \tag{8}
\]
对任意两不同点z₁,z₂且分母非零，
\[
 \det[K_d(z_j,z_k)]_{j,k=1}^2
 =\frac{4d|z_1-z_2|^2}{|z_1^2+d|^2|z_2^2+d|^2}.         \tag{9}
\]
所以d<0的失败已经发生在同一Euler安全域，并非只有把safe数据继续到中心线才出现。固定z₁=1、z₂=2，即s=3/2、5/2：

| 完整模型 | K₁₁ | K₂₂ | K₁₂=K₂₁ | det K |
|---|---:|---:|---:|---:|
| c₊=5/16，d=1/16 | 32/17 | 32/65 | 1056/1105 | 16384/1221025>0 |
| c₋=3/16，d=−1/16 | 32/15 | 32/63 | 992/945 | −16384/893025<0 |

负例两个diagonal仍为正；scalar实部正不是所有有限Gram正。其边界对角为
\[
 A'_d(it)=2(d+t^2)/(d-t^2)^2,
\]
在d<0、|t|<√(−d)为负，亦直接交叉核(3)。正例(8)的显式feature系数为diag(1,d)，与562完整Weil核2cos(√d u)的已知相变同构；这项2×2计算是旧结论的具体消费，**不是新独立正性或新迭代**。

两模型完整prime-power Laplace测度都为正，故由它造的
\[
 L(s,w)=\int_0^\infty e^{-su}\overline{e^{-wu}}d\Psi(u)
\]
在收敛域一定正；但负模型(9)证明L不是同一K。若用L或|U(s)|²来替代K，必须另给带完整Γ／pole的signed余项与原费用，不能因两者都叫Gram而视作同源identity。

## 3. 真函数域：完整periodic对象与同两点正号

固定已付真实E/F₅，P(T)=1+3T+5T²，ℓ=log5；563／576的具体H>0及FᵀHF=5H是独立输入。**去除全部periodic poles**后，用精确self-dual规范
\[
 \Phi_E(z)=e^{\ell z}P(5^{-1/2}e^{-\ell z})
     =2\cosh(\ell z)+3/\sqrt5,
 \quad \alpha=3/(2\sqrt5),
\]
\[
 A_E(z)=\ell\frac{\sinh(\ell z)}{\cosh(\ell z)+\alpha}.   \tag{10}
\]
漏掉e^(ℓz)会把A减去ℓ，把K减去2ℓ/(z+bar w)，因此这个completion规范不可省略。这里Γ是模型自身的0，并无经典Γ的局部因子。

由旧实际H给unitary U及cosθ=−α，全部alias频率
\(\gamma_{\pm,k}=(\pm\theta+2\pi k)/\ell\)均保留。配对partial fractions给
\[
 K_E(z,w)=\sum_{\pm,k\in\mathbb Z}
 \frac1{(z-i\gamma_{\pm,k})(\bar w+i\gamma_{\pm,k})}.      \tag{11}
\]
右侧局部绝对收敛；这是由已付同对象H／RR保证的正resolvent Gram，而不是只保fundamental strip的两个零点。完整物理
\(W_E=\ell\sum_n2\cos(n\theta)\delta_{n\ell}\)
和(5)直接给B_W=K_E，无剩余square；这里之所以正，是已有独立H而不是closed-place coefficients非负。

同样取z₁=1、z₂=2，设
\[
 a=13+5\alpha,\quad b=313+25\alpha,
 \quad A_1=12\ell/a,\quad A_2=312\ell/b.
\]
完整Gram为
\[
 \begin{pmatrix}A_1&(A_1+A_2)/3\\(A_1+A_2)/3&A_2/2\end{pmatrix},
\quad
 \det=\frac{\ell^2(836352+309120\alpha-150400\alpha^2)}{a^2b^2}
      =\frac{\ell^2(768672+309120\alpha)}{a^2b^2}>0.       \tag{12}
\]
交叉数值仅作转录检查：K₁₁≈1.18094255，K₂₂≈0.76135466，K₁₂≈0.90121729，det≈0.08692351；证明为(11)或(12)精确式。函数域所有periodic poles已在完成化中清除，全部returns及aliases仍在原W／(11)，没有以finite-rank双pole模型替代它们。

## 4. 安全shift的正对象多出什么

旧[132 XU／XV](../../../notes/132-shifted-passivity-abel-resonance.md)有无条件外层positive package：对a足以覆盖已知zero-strip，
\[
 A_a(z)=A(z+a),\quad
 K_a(z,w)=\frac{A(z+a)+\overline{A(w+a)}}{z+\bar w}\ge0.  \tag{13}
\]
经典可取a=1/2。但原安全点Z=z+a、W=w+a的中心核分母为Z+bar W，(13)分母则是Z+bar W−2a。两者不同，不能把已知outer passivity当原中心核在安全域的正性。

物理上(13)是Abel-damped完整分布e^(−a|u|)W在半轴源(5)上的Gram。对一个实际pole r=ρ−a、Re r≤0，逐项精确恒等式为
\[
 \frac{(z-r)^{-1}+(\bar w-\bar r)^{-1}}{z+\bar w}
 =\frac1{(z-r)(\bar w-\bar r)}
 +\frac{-2\Re r}{(z-r)(\bar w-\bar r)(z+\bar w)}.        \tag{14}
\]
第二项是正Szegő square，表示dissipation。a>0的外层正对象能容纳off-center pairs；未付的是去damping／去dissipation的比较。把余项删去或把分母改回中心值，正号没有合法运输。此处(14)只说明同源预算差，不能用未知ρ选本轮coefficients；证明与旧132(8)完全相同，不重报新输入。

## 5. 原du／Dlog、截断与成长的实际费用

(5)令z=a+ib，a>0，则
\[
 \|r_z\|_{du}^2=1/(2a),\qquad
 \|r_z\|_{H_{\log}}^2=(2\pi)^{-1}\int
 \frac{1+\log(2+|t|)}{a^2+(t+b)^2}dt<\infty.             \tag{15}
\]
对a在任意预先固定的正compact区间，后者与(1+log(2+|b|))/(2a)同阶，常数依该区间；没有把Laplace参数范数当physical du范数。a↓0时du费用已经发散，不能拿safe σ>1的统一对象直接到临界源。

hard截断r_z到[0,L]是原Dlog合法源，其尾**准确**满足
\[
 \|\mathbf1_{u\ge L}r_z\|_{du}^2=e^{-2aL}/(2a),\quad
 \|\mathbf1_{u\ge L}r_z\|_{H_{\log}}^2
       =e^{-2aL}\|r_z\|_{H_{\log}}^2,                  \tag{16}
\]
由translation invariance直接给。若需C_c∞ core，还须另做合法原Dlog端点平滑，不能以这些step源误称S_exp。

从safe Laplace衰减去掉固定a的damping涉及乘法r(u)↦e^(au)r(u)。在[0,L]上du operator norm恰e^(aL)，平方费e^(2aL)；靠L端point的bump达到sup。固定a>0，用宽度1的平滑cutoff扩展乘子，weighted Fourier Young界与H²乘子预算给Hlog upper C_a e^(aL)，故平方费用至多C_a²e^(2aL)。这只是固定窗合法运输，非小费用。

在全线du／Hlog该乘子无界：固定compact bump的平移保原两范数，乘法后费用按e^(aL)增长。物理r=e^(u/2)f本身的固定窗du平方权e^u必须按原坐标保留；若f使用天然L²(e^u du)则这是等距坐标变换，不另虚收一笔费。真正未付的是从safe weighted probe控制去掉额外a权后的全源控制。

固定(5)的尾小不等于全部原du／Dlog源有统一尾小；也不等于577实际q_R multiplier c_R或mass m_R变小。要付fixed-L误差仍只能用577已有
\[
 D_L/R^2+\min(c_R,2Lm_R),\qquad D_L\ll(1+L^2)e^L,        \tag{17}
\]
成长L=L(R)须共同付这些项及任何去shift费用。原safe域normal-family控制到全半平面已是131 XT／132 XW的RH等价，不是独立紧性结论。

## 6. 405、537及本门结论

405是actual noncompact Pan p=(D²−1/4)H₀、其全部固定平移和全mixed配对Bζ(p,s)=0，不是“两个pole矩为零”就足够，也不是(5)指数尾probe本身。完整linear身份(7)不改变405。任何把safe正Gram偷当完整Weil的map仍须核全Pan；577真Γ正层高频谱严格正，故每层Q_V(p)>0的exact失败照旧。固定强源裸层O(R⁻²)费用与修补另费、553全线稠密障碍都未被(13)修复。

537原17/16固定窗全部complex源非根见证仍保：577已给Q_V≥(τ−D_L₀/R²)||r||²，无需先付q_R。这里的连续负例不反驳这个经典旧固定窗结论。函数域的零repair来自旧同对象H／RR，连续正例零repair来自562显式cos平方和；连续负例实际双pole-zero源迫repair不消的旧578原费lower保持。

**本门净消费：**一个同源核可精确写出完整linear Weil在safe Laplace源上的配对，但其全Gram正性并未独立取得；safe正Laplace测度Gram、outer-shift正Gram和中心K是三个不同对象。明确两安全点的正／负det及FF全alias对照可阻止误运输，全部是131／132／562既有结论的直接检验。没有新独立q_R消失、全源成长费或whole/core后果。按用户停损在此停止该Pick／shift候选，不调更多点／shift或把RH等价正性另命名为新容量。
