# Joint oldform tower：实际源、退化规范与全序列反演

2026-10-27；/root/tower_inverse 独占原稿。执行[唯一准入比较](../finite-cover-trace/next-joint-oldform-tower-admission.md)，不恢复 C047 预算，不预建 C048／585。本文不修改 STATE、cadence 或 Git。root 与独立 fresh 消费前，本稿只是待审原件。

净结论是一个**标准坐标比较**：完整 tower 在明确的 rapid-geometric sequence 空间上，恰为583负 Faber 系数的连续可逆重编码。它保 raw 全源信息，但不因此给 Pan 下降、非零 primitive 类、算术整性或 mixed RR。两种商的比较由独立原稿另行处理。

## 1. 固定源及已付输入

固定

\[
 g(\tau)=g_{11}(\tau)=\eta(\tau)^2\eta(11\tau)^2
   =\sum_{k\ge1}c(k)q^k,\qquad q=e^{2\pi i\tau},\quad c(1)=1.
\]

584的[source原稿](../marked-cusp/source-kernel-and-typed-controls.md)已核 \(g\in S_2(\Gamma_0(11))\)、trivial character 和 compact coarse \(X_0(11)\) 上全纯微分 \(\omega_0=g(\tau)d\tau\)。该原稿用 \(g(q)dq/q=2\pi i\,\omega_0\)；这个固定常数不影响下面 pullback 的 \(d\) 因子。

物理源固定全部复 \(F=S_{\exp,\mathbb C}\)，\(r=e^{u/2}f\)，
\(p_{N,j}(r)=\sup_u e^{N|u|}|D^jr(u)|<\infty\) 对所有 \(N,j\)。
沿583§1令

\[
 L_r(z)=\int r(u)e^{uz}du,\qquad
 L_r(j(q))=\sum_{n\in\mathbb Z}a_n(r)q^n,\quad x_m(r)=a_{-m}(r).
\]

对每个 \(0<s<1\)，令
\(A_s=\max_{|q|=s}|\Re j(q)|\)、\(M_s=\max_{|q|=s}|j(q)|\)、
\(P_s(r)=\int|r(u)|e^{A_s|u|}du\)。583已付

\[
 |x_m(r)|\le s^mP_s(r),\qquad
 P_s(r)\le\frac{2p_{N,0}(r)}{N-A_s}\quad(N>A_s).              \tag{1}
\]

“全部半径超几何”不等于统一原范数上界：改变 \(s\) 也改变 \(A_s\) 和源费用。

## 2. 全部d的实际 oldform 与微分规范

对每个整数 \(d\ge1\)，定义 \(\alpha_d\tau=d\tau\)、\(g_d(\tau)=g(d\tau)\)。若
\(\gamma=\left(\begin{smallmatrix}a&b\\c&e\end{smallmatrix}\right)\in\Gamma_0(11d)\)，则

\[
 \alpha_d\gamma\alpha_d^{-1}
 =\begin{pmatrix}a&db\\c/d&e\end{pmatrix}\in\Gamma_0(11).
\]

于是 \(g(d\gamma\tau)=(c\tau+e)^2g(d\tau)\)：\(g_d\) 有 weight2、trivial character 的实际 modularity。

同一 equivariance 给 degeneracy map
\[
 \beta_d:X_0(11d)\longrightarrow X_0(11),\qquad[\tau]\longmapsto[d\tau].
\]

该映射在 cusps 也 holomorphic：若 \(\sigma,\sigma'\) 对应两个 rational cusps，则
\(\sigma'^{-1}\alpha_d\sigma\) 是有理 upper-triangular 正行列式矩阵，其局部作用为 \(z\mapsto Az+B\)、\(A>0\)。取两边 coarse cusp width 的局部q坐标后，equivariance 使
\(q_{\rm target}=\zeta q_{\rm source}^{e_c}\)，其中 \(e_c\) 为正整数。因此 \(\beta_d\) 延到 compact coarse 曲线。这里群含 \(-I\)，而 \(\Gamma_0(11d)\subset\Gamma_0(11)\)，不把 SL lift-order 另当 coarse width。

实际微分为
\[
 \beta_d^*\omega_0=d\,g(d\tau)d\tau.
\]

全纯微分的 pullback 全纯，除以 \(d\) 后仍全纯，故 \(g_d\in S_2(\Gamma_0(11d))\) 在**所有**cusps都是 cusp form。本文读出用

\[
 \omega_d=g(q^d)\frac{dq}{q}
       =\frac1d\,\beta_d^*\left(g(q)\frac{dq}{q}\right).         \tag{2}
\]

所以读出**没有额外d**；若用未除d的 pullback，第d坐标必须乘d。\(\infty\) 的 coarse width 为1，以下正向q圈就是实际 residue 圈。

## 3. Source／contour／coefficients的全域恒等式

固定 \(0<\rho<1\)，令
\[
 C_\rho=\max_{|q|=\rho}|g(q)|,\quad C=\max\{1,C_\rho\},\quad A=\rho^{-1}.
\]
Cauchy 对全部k给同一指数上界
\[
 |c(k)|\le C\rho^{-k}=CA^k.                                  \tag{3}
\]
对任意 \(0<s<\rho\) 及全部 \(d\ge1\)，
\[
 \sum_{k\ge1}|c(k)|s^{dk}\le C\frac{s^d}{\rho-s^d}.             \tag{4}
\]
定义
\[
 K_d(u)=\frac1{2\pi i}\oint_{|q|=s}e^{uj(q)}g(q^d)\frac{dq}{q},
 \quad B_\infty(r)_d=\operatorname{CT}_q\big(L_r(j(q))g(q^d)\big).
\]
固定圈上j有界，r有全部指数矩，(4)保证u积分与contour绝对可换。Laurent expansion 正常收敛，且
\(\sum_k|c(k)x_{dk}(r)|\le CP_s(r)s^d/(\rho-s^d)\)。
因此对全部r、全部d有同一个准确恒等式

\[
 \boxed{B_\infty(r)_d=\int r(u)K_d(u)du
                   =\sum_{k\ge1}c(k)x_{dk}(r).}               \tag{5}
\]

源没有裁为compact，也未先取Pan商。它就是
\(\operatorname{Res}_\infty(L_r(j)\omega_d)\)，负系数/倍数方向及微分规范与(2)一致。
每个固定导数阶j还满足

\[
 |K_d^{(j)}(u)|\le C\frac{s^d}{\rho-s^d}M_s^j e^{A_s|u|},
 \qquad |B_\infty(r)_d|\le C\frac{s^d}{\rho-s^d}P_s(r).         \tag{6}
\]

一个固定s即可同时控制全部d；要求更强的序列半范数时可以选更小s，但源费用随之改变。

## 4. 明确的rapid-geometric空间及原费

令
\[
 E=\{x=(x_m)_{m\ge1}:\|x\|_R:=\sup_{m\ge1}R^m|x_m|<\infty
                           \text{ for every }R\ge1\}.
\]
整数R定义同一Fréchet topology；这是加权 \(\ell^\infty\) 空间的可数交，故complete，不是仅逐坐标product topology。
对coordinate cutoff \(\Pi_M\)、任意 \(Q>R\)，
\[
 \|x-\Pi_Mx\|_R\le\|x\|_Q(R/Q)^{M+1}.                        \tag{7}
\]
所以有限序列在E稠密。由(1)，若 \(s<1/R\)，则
\(\|x(r)\|_R\le P_s(r)\)，原系数映射F→E连续。由(6)，
\[
 \|B_\infty(r)\|_R\le\frac{C}{\rho-s}P_s(r)
        \quad(0<s<\min\{\rho,1/R\}).                          \tag{8}
\]
这是每目标半范数同时全d的强源费。

若 \(\operatorname{supp}r\subset[-L,L]\)，原du满足
\[
 P_s(r)\le C_{L,s}\|r\|_{du},\quad
 C_{L,s}^2=
 \begin{cases}
 (e^{2A_sL}-1)/A_s,&A_s>0,\\
 2L,&A_s=0.
 \end{cases}                                                 \tag{9}
\]
因此(8)给完整tower每个固定E半范数的一份原fixed-window上费。
原zero-extension
\(\|D_{\log}r\|^2=(2\pi)^{-1}\int\log(2+|t|)|\widehat r(t)|^2dt
\ge\log2\,\|r\|_{du}^2\)，故该费用再乘 \(1/\sqrt{\log2}\)。
不与另加1的Hlog混同；不报一个控制全部R、L的单一原norm常数，也不声称E可有界反演回物理du。

## 5. Dirichlet逆的实际指数上界

在全部x∈E上定义multiples-transform
\[
 (Tx)_d=\sum_{k\ge1}c(k)x_{dk}.                               \tag{10}
\]
因c(1)=1，有限Dirichlet convolution唯一给逆系数
\[
 v(1)=1,\qquad v(n)=-\sum_{\substack{k\mid n\\k\ge2}}c(k)v(n/k).
                                                                    \tag{11}
\]
形式存在性以外，取 \(D=(4CA)^2\)，则
\[
 \boxed{|v(n)|\le D^n\quad(n\ge1).}                           \tag{12}
\]
强归纳证明：n=1显然；n≥2的每个k≥2满足n/k≤n/2，项数≤n且A^k≤A^n，故
\[
 |v(n)|\le nCA^nD^{n/2}
       =D^n\,\frac{nC}{(4C)^n}\le D^n,
\]
最后一步用C≥1、n≥2。这不是数值截断猜测。采用584既有
\(\rho=1/512,C_\rho<1\) 证书时可取 \(C=1,A=512,D=2^{22}\)，但一般证明无需再次消费该数值特例。

## 6. 双和绝对性与连续自同构

定义
\[
 (Sy)_d=\sum_{k\ge1}v(k)y_{dk}.                               \tag{13}
\]
先给通用连续界。若 \(|h(k)|\le C_0A_0^k\)，且
\(Q\ge\max\{2A_0,R\}\)，则
\[
 \begin{aligned}
 \sup_dR^d\sum_k|h(k)x_{dk}|
 &\le C_0\|x\|_Q\sup_d\frac{A_0(R/Q)^d}{1-A_0Q^{-d}}\\
 &\le2C_0A_0\|x\|_Q.                                       \tag{14}
 \end{aligned}
\]
它证明每坐标绝对收敛、输出属于E，且
\[
 \|Tx\|_R\le2CA\|x\|_Q\ (Q\ge\max\{2A,R\}),\qquad
 \|Sy\|_R\le2D\|y\|_Q\ (Q\ge\max\{2D,R\}).                   \tag{15}
\]
计算复合时，任选 \(Q\ge4\max\{D^2,A^2\}\)。由 \(2kl\ge k+l\)，全部d≥1有
\[
 \begin{aligned}
 \sum_{k,l\ge1}|v(k)c(l)x_{dkl}|
 &\le C\|x\|_Q\sum_{k,l\ge1}D^kA^lQ^{-dkl}\\
 &\le C\|x\|_Q
       \left(\sum_{k\ge1}(D/\sqrt Q)^k\right)
       \left(\sum_{l\ge1}(A/\sqrt Q)^l\right)<\infty.           \tag{16}
 \end{aligned}
\]
故可按n=kl分组；Dirichlet convolution给
\[
 (STx)_d=\sum_{n\ge1}\left(\sum_{k\mid n}v(k)c(n/k)\right)x_{dn}
          =x_d.
\]
交换c、v用同一绝对界得TS=I。因此不是形式逆或仅有限矩阵，而是
\[
 \boxed{T:E\overset{\sim}{\longrightarrow}E,\qquad T^{-1}=S
        \text{ 连续线性自同构}.}                             \tag{17}
\]
结合(5)，完整 \(B_\infty=T\circ x\) 与583负系数包含相同raw信息。旧583的
\(x(r)=0\Rightarrow r=0\)立即给raw联合注入；这是旧注入的运输，不能重领一次全源可见性或primitive输入。

## 7. 实际截断尾及两种截断

令T_K、S_K只保(10)、(13)的k≤K。按同一几何级数：
\[
 \|(T-T_K)x\|_R\le2CA\|x\|_Q(A/Q)^K
       \quad(Q\ge\max\{2A,R\}),                              \tag{18}
\]
\[
 \|(S-S_K)y\|_R\le2D\|y\|_Q(D/Q)^K
       \quad(Q\ge\max\{2D,R\}).                              \tag{19}
\]
这里K≥0，K=0时有限和为0；尾的证明保留
\(R^dQ^{-d(K+1)}\le Q^{-K}\)，没有从有限逆矩阵推断全tower。

另一截断是583有限principal coefficient vector \(x^{[M]}=\Pi_Mx\)。
由(7)、(15)，
\[
 T(\Pi_Mx)\to Tx,\qquad S(\Pi_My)\to Sy\quad\text{in }E.       \tag{20}
\]
\(T(\Pi_Mx)\) 也是有限序列（d>M时为0），但一般不等于
\(\Pi_M(Tx)\)：后者的前M项仍含dk>M的贡献。finite principal截断应先在原x上做再运输；不能删alias/tail后称exact同源。

583的 finite Faber principal data 在native Green/current拓扑中的闭包是另一项几何比较。
(20)既不把finite principal inputs冒充物理r∈F，也不把honest principal闭包等同actual Pan在强目标中的闭包。

## 8. 净值、前件范围与停止

| 消费项 | 本稿实际范围 |
|---|---|
| 对象／domain-range | 全d实际g(dτ)、coarse X0(11d)、ω_d=(1/d)β_d*ω0；F→E真实contour/constant term |
| 源与成长 | 全complex S_exp；固定ρ,s对全d；每目标R独立付强源或fixed窗原du-Dlog费用 |
| 系数方向 | B_d=Σc(k)a_-dk，无漏d；原principal截断与直接截tower坐标不同 |
| 依赖／误差 | 583全半径Cauchy与Faber注入；584 typed g；(12)/(16)/(18)/(19)付逆增长、双和与全尾，无新外部论文/数值实验 |
| 关系／商／physical | raw自同构尚未取Pan或principal商；F、E、native几何完成化及各关系闭包分开 |
| 强旧净值 | 标准Dirichlet反演使tower恰为583 raw坐标重编码；新独立算术输入、经典whole净后果均为0 |
| 未付 | 算术整模型、非零primitive、整过滤／截面乘法／mixed RR、完整signed与growth/core/coupling/Ξ |

建议按**标准旧坐标比较0数学轮**消费；root结合独立两商原稿及fresh最终决定。本文不推出infinite Pan exact像等式，不以finite-prefix/product稠密证明强商全零，不把全线Hilbert bounded-reader定理套到强费指数核。

止于该完整tower坐标比较，不再挑d、换seed、加period、变source规范或顺读paper。
保真正不同的relative数据、实际合法强拓扑及未逐层消Pan的D′修复，但它们须另有实物和净后果；raw注入或大常数inverse不提供这些前提。经典542+555→557 whole leading4/5负惯性UPPER未改善，长期Goal完成门仍open。
