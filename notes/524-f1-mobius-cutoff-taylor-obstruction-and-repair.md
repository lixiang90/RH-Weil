# 524. Möbius原点切断的Taylor障碍、有限修复与协变族限制

2026-10-12。[T/N] 接续[518](518-f1-quantitative-mellin-division-and-mobius-source.md)、
[519](519-f1-closed-source-image-and-degree-moments.md)和
[522](522-f1-optimal-centered-growth-and-rh-equivalence.md)。
本稿检验明确的实际源修正族，证明两种与离线零点无关的严格失败，并构造合法有限Taylor修复。
它们限制指定的修正方法，没有否定522的合同或证明RH。

## 1. 原空间、实际反演及需要支付的合同

采用同一复空间和全部原半范数：
\[
 F=\mathcal S_{\exp,\mathbb C},\quad
 P_n(f)=\max_{0\le j\le n}\sup_t e^{n|t|}|f^{(j)}(t)|,
 \qquad M_f(s)=\int_{\mathbb R}e^{st}f(t)dt.
\]
合法源空间为偶复Schwartz函数θ，满足θ(0)=0和 \(\int_{\mathbb R}\theta=0\)。
其实际算子 \(E\theta(t)=2\sum_{n\ge1}\theta(ne^t)\) 的像I在F闭，
恰是所有非平凡ζ零点的完整重数jets消失的空间；E到I为拓扑同构。
原中心化作用是 \(V_af(t)=e^{-a/2}f(t-a)\)。

522的实际源修正合同为
\[
 \forall n\ \forall\varepsilon>0\ \exists m,C\ \forall a\in\mathbb R\ \forall f\in F
 \ \exists\theta\text{合法}:\quad
 P_n(V_af-E\theta)\le Ce^{\varepsilon|a|}P_m(f).             \tag{1}
\]
m和C统一于a、f；源可依赖n、ε、a、f，不要求线性或连续选择。
已经证明(1)与RH等价，不能将其当作已有的独立算术估计。

对任何f∈F，不预设f∈I，正r上的实际反演函数是
\[
 T_f(r)=\frac12\sum_{n\ge1}\mu(n)f(\log(nr)).              \tag{2}
\]
在每个正r紧区间，所有Euler导数的和绝对一致收敛；在无穷端普通导数任意快衰减。
正整数双和用足够强的指数衰减绝对换序，除数恒等式给
\[
 2\sum_{m\ge1}T_f(me^t)
 =\sum_{k\ge1}\Big(\sum_{n\mid k}\mu(n)\Big)f(t+\log k)=f(t). \tag{3}
\]
这是逐点重建，尚不表示T在原点已是合法源。另有准确协变式
\[
 T_{V_af}(r)=e^{-a/2}T_f(e^{-a}r).                          \tag{4}
\]
一般T的无条件可积性、零积分及其代价由[525](525-f1-smoothed-mobius-probes-and-arithmetic-strength.md)另证。

## 2. 切断并补偿积分得到合法源，却误删全部偶Taylor数据

固定光滑χ，在r≤1为0，在r≥2为1；固定偶紧支β，支集远离0，
\(\int_{\mathbb R}\beta=1\)。对任意δ>0及g∈F，偶延拓
\(q_{g,\delta}(r)=\chi(|r|/\delta)T_g(|r|)\)，并令
\[
 \theta_{g,\delta}=q_{g,\delta}
             -\Big(\int_{\mathbb R}q_{g,\delta}\Big)\beta.   \tag{5}
\]
q在0邻域为0、在无穷端Schwartz，故积分有限。(5)偶、Schwartz、原点零值且零积分，确为合法源。
但它在原点是flat的：全部导数为0。让δ任意依赖a、f，或用多个原点外profile补偿，
都不能改变这个性质。

519把源Taylor数据准确转换成负偶整数的目标Mellin值：
\[
 M_{E\theta}(-2k)=2\zeta'(-2k)a_k(\theta),\qquad
 a_k(\theta)=\frac{\theta^{(2k)}(0)}{(2k)!},\quad k\ge1.    \tag{6}
\]
这里ζ'(-2k)非零，来自函数方程；不能把平凡零点处的可去值忽略。
所以实际flat源的像是
\[
 I_{\rm flat}=I\cap\bigcap_{k\ge1}\ker M(-2k).             \tag{7}
\]
正向由(6)；反向用E的唯一源、(6)、偶性及θ(0)=0，得到全部Taylor数据为零。
M(-2k)在F连续，因此(7)在F闭。

原点邻域恒0的合法源在原Schwartz拓扑中的闭包恰是合法flat源。
一边来自连续的原点导数求值；另一边对任意flat θ用χ(|r|/δ)切断，
再按(5)补偿积分。flat性使切断产生的每阶导数误差为任意高次δ小量，
质量误差也为任意高次小量，故δ→0时在每个Schwartz半范数收敛。
由E的拓扑同构，这些目标的F闭包正是(7)，并非整个I。

## 3. 任意截断尺度的严格原点障碍

405的实际非零源及目标是
\[
 \theta_0(r)=\pi r^2(\pi r^2-3/2)e^{-\pi r^2},\quad
 h_0=E\theta_0\in I,\quad M_{h_0}(s)=\xi(s)/2.
\]
其二阶源系数为−3π/2。由
[ζ函数方程](https://dlmf.nist.gov/25.4#E2)，
\(\zeta'(-2)=-\zeta(3)/(4\pi^2)\)，所以
\[
 M_{h_0}(-2)=\frac{3\zeta(3)}{4\pi}>0.                    \tag{8}
\]
这也证明(7)是I的真子空间。

对任意u∈F，Cauchy的直接积分估计给
\[
 |M_u(-2)|\le p_{3,0}(u)\int e^{-2t-3|t|}dt
            =\frac65p_{3,0}(u)\le\frac65P_3(u).             \tag{9}
\]
对全部a≤0和全部合法flat源θ_a，(6)、(8)与平移给
\[
 \boxed{P_3(V_ah_0-E\theta_a)
       \ge\frac{5\zeta(3)}{8\pi}e^{(5/2)|a|}.}             \tag{10}
\]
因此任何ε<5/2时，这一族都不能满足(1)，无论δ(a)缩得多快，也无论如何补偿普通积分。
这不依赖RH、离线零点或简单性。h0的原商类本来是零；其实际伸缩源
\(e^{-a/2}\theta_0(e^{-a}r)\) 可以使残差恰为0。
错误来自把合法来源额外缩小到flat子空间。

一般k及整数n>2k时，有
\[
 |M_u(-2k)|\le\left(\frac1{n-2k}+\frac1{n+2k}\right)P_n(u).
                                                               \tag{11}
\]
遗漏一个非零的此类矩，会产生负时间指数2k+1/2的同类下界。
n=2k时上述积分发散，本稿不以(11)声称这一端点连续估计。

## 4. 有限Taylor修复保持实际源和完整非平凡jets

固定偶 \(\kappa\in C_c^\infty\)，在0邻域为1，仍用上述β。令
\[
 u_k(r)=r^{2k}\kappa(r)-b_k\beta(r),\quad
 b_k=\int_{\mathbb R}r^{2k}\kappa(r)dr,\qquad v_k=Eu_k.    \tag{12}
\]
每个u_k均合法，原点附近准确为r^{2k}，而不是只到有限阶的形式多项式。
故对所有j≥1，
\[
 M_{v_k}(-2j)=2\zeta'(-2j)\delta_{jk}.                    \tag{13}
\]
同时v_k在全部非平凡零点处的完整jets消失，因为它来自实际E。
对固定K，定义
\[
 \Theta_K(f)=\sum_{k=1}^K
          \frac{M_f(-2k)}{2\zeta'(-2k)}u_k,\qquad Q_Kf=E\Theta_K(f).
                                                               \tag{14}
\]
这是到合法源／I的连续有限秩算子，Q_K²=Q_K，秩为K。
取一个固定m>2K，(11)给每个系数的 \(C_KP_m(f)\) 界；
E连续及有限个固定u_k于是给每个n的 \(P_n(Q_Kf)\le C_{n,K}P_m(f)\)。
f−Q_Kf的前K个负偶矩为0，非平凡完整jets仍与f相同。

因此(5)可以改为 \(\theta_{V_af,\delta}+\Theta_K(V_af)\)，
准确修复前K个遗漏矩，零积分不受影响。
要注意系数为
\[
 \frac{M_{V_af}(-2k)}{2\zeta'(-2k)}
 =e^{-(2k+1/2)a}\frac{M_f(-2k)}{2\zeta'(-2k)}.             \tag{15}
\]
负时间时它们可以指数巨大。(1)允许大的源，约束的是联合相消后的残差；
把补偿源和误差分别取三角上界会丢掉必要消去，不能用(15)单独宣布修复失败。

固定K还不能覆盖所有输出半范数。θ0的第2k系数
\(a_k=(-1)^k\pi^k(k+1/2)/(k-1)!\) 对每个k≥1非零。
flat源加前K项修复仍遗漏h0的第K+1项，(11)在任何n>2(K+1)给严格下界。
但(1)允许K随输出n选择；这一事实不否定可变K的修复方案。
至少所有2k<n的矩需要处理，这只是该检测方法给出的必要范围，不是充分误差估计。

普通源积分为0也不等于目标的双次数为0。519给准确接口
\[
 c(Eu_k)=-\int_0^\infty u_k(r)\frac{dr}{r},\qquad
 d(Eu_k)=2\int_0^\infty u_k(r)\log r\,dr.                 \tag{16}
\]
它们一般非零。本构造没有免费加入 \(c=d=0\) 关系。

## 5. 一次选定后只作协变伸缩的源族也严格失败

还有一个独立于flat性的障碍。若给每个f一次选定合法源θ(f)，随后只取
\[
 \theta_a(f)(r)=e^{-a/2}\theta(f)(e^{-a}r),                \tag{17}
\]
则 \(E\theta_a(f)=V_aE\theta(f)\)。残差为 \(V_ar_f\)，
其中 \(r_f=f-E\theta(f)\) 是固定函数。
若r_f非零，选 \(r_f(t_0)\ne0\)，在t=t0+a处求值，得到对a≤0
\[
 P_n(V_ar_f)\ge e^{-n|t_0|}|r_f(t_0)|e^{(n+1/2)|a|}.     \tag{18}
\]
这用 \(|t_0+a|\ge|a|-|t_0|\)，没有忽略中心化的1/2。
任取ε<n+1/2，固定的m、C不可能吸收(18)。对f∉I，每个合法θ(f)都留下非零r_f，
所以任何这样的全输入协变族都失败。

(1)允许逐a重新选择源，(17)额外限制了这种选择；两者不是同一合同。
即使能无条件建立一个不错的固定代表，直接输运这个代表也不能证明商的次指数增长。

## 6. 已付与下一步

本轮付清指定flat族及一次协变族的严格失败，以及实际有限Taylor修复的准入、
连续性和全部重数接口。剩余工作是对可随时间重新选择的修复族，
估计E作用后的整体残差，保留切断导数、质量补偿和Taylor修复的相消，
用一个固定P_m统一全部a、f。

[525](525-f1-smoothed-mobius-probes-and-arithmetic-strength.md)核对能无条件支付的质量成本，
并揭示临界Möbius估计的RH强度；
[526](526-f1-faithful-two-weight-hilbert-quotient-and-defect.md)检验双端完成能否补足正定酉性。
这里没有新零点比例、无零条带、RH证明、几何principal或Weil符号证明。
