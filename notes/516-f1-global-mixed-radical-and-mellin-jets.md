# 516. 完整混合根空间、实际源关系与重数jet障碍

2026-10-11。[T/R/N] 接续[405](405-f1-adelic-restriction-moments-and-radical.md)、
[515](515-f1-common-central-mixed-kernels.md)。
本稿严格识别完整算术标量配对的根空间，并比较真实源闭像的更强重数条件。
不构造全局HH₁完成，不认证几何主除子，不证明Weil负性或RH。

## 1. 固定同一空间、源与完整配对

采用405明确的实Fréchet空间
\[
 \mathcal S_{\exp}=\{f\in C^\infty(\mathbb R,\mathbb R):
       p_{N,j}(f)=\sup_t e^{N|t|}|f^{(j)}(t)|<\infty,\ \forall N,j\}.
\]
\(M_f(s)=\int e^{st}f(t)dt\)、\(d(f)=M_f(1)\)、\(c(f)=M_f(0)\)，
\(f^\sharp(t)=e^{-t}f(-t)\)。
B仍是原完整算术配对，全部Euler、Gamma及恒等元项保留：
\[
 2B(f,g)=d(f)c(g)+c(f)d(g)
       -\sum_{\rho}m_\rho M_f(\rho)M_g(1-\rho).                \tag{1}
\]
这里ρ遍历不同的通常非平凡ζ零点，mρ是重数；
不同时重复列ρ又乘mρ。只用无条件的 \(0<\Re\rho<1\)
与标准零点计数，不假设中心线。

定义
\[
 \mathcal R_{\rm val}=
 \{f\in\mathcal S_{\exp}:d(f)=c(f)=0,\ M_f(\rho)=0\ \forall\rho\}.
                                                               \tag{2}
\]
后缀val表示只要求零点处的值，尚无高阶导数条件。

## 2. 全部混合标量检测恰给rad(B)

对实偶紧支ζ令 \(k_\zeta=e^{-t/2}\zeta\)。若f,g紧支，
记 \(k_{fg}=(f*g^\sharp+g*f^\sharp)/2\)、
\(\eta_{fg}(t)=e^{t/2}k_{fg}(t)\)。前者实sharp，后者实偶，
所以515的链输入为 \(\eta_{fg}\)，其算子为 \(C=\Pi A_{\eta_{fg}}\)。
实际有限S中央读出在覆盖合成支集后准确为
\[
 \Omega_{S,\zeta}([t_{S,\eta_{fg}}])
 =2N_S(k_{fg}*k_\zeta)=2B_S(f,g*k_\zeta).
                                                            \tag{3}
\]
因为 \(k_\zeta^\sharp=k_\zeta\)，最后极化恒等式准确成立。
覆盖后的值等于完整 \(2B(f,g*k_\zeta)\)。

在较大空间只定义完整标量检测核
\[
 \mathcal K_{\rm mix}=
 \{f\in\mathcal S_{\exp}:B(f,g*k_\zeta)=0,\
                    \forall g\in C_c^\infty,\ \forall\zeta\in C_{c,\rm even}^\infty\}.
                                                               \tag{4}
\]
这是(1)的连续标量延拓；不冒称非紧支f已有全局实际链。

选偶非负近似单位 \(\zeta_\epsilon(t)=\epsilon^{-1}\zeta_0(t/\epsilon)\)，
\(\int\zeta_0=1\)。则 \(g*k_{\zeta_\epsilon}\to g\) 于 \(\mathcal S_{\exp}\)：
支集统一有界，逐导数一致收敛，且 \(\int k_{\zeta_\epsilon}\to1\)。
紧支测试在 \(\mathcal S_{\exp}\) 中稠密，偶截断证明见405。
B联合连续，故
\[
 \mathcal K_{\rm mix}=\operatorname{rad}B.                    \tag{5}
\]
这也说明(4)包含全部g的量词不可缩成一个固定自配对。

## 3. 通过平移与Laplace留数识别完整根空间

(1)立即给 \(\mathcal R_{\rm val}\subset\operatorname{rad}B\)。
反向取 \(f\in\operatorname{rad}B\)，固定非零非负实紧支κ，写
\(\tau_a\kappa(t)=\kappa(t-a)\)。则对所有实a，
\[
 \begin{aligned}
 0=2e^{-a/2}B(f,\tau_a\kappa)
 ={}&d(f)c(\kappa)e^{-a/2}+c(f)d(\kappa)e^{a/2}\\
 &-\sum_\rho m_\rho M_f(\rho)M_\kappa(1-\rho)
                                    e^{(1/2-\rho)a}.          \tag{6}
 \end{aligned}
\]
Mellin变换在零点带内沿虚轴任意阶快速衰减，
故级数及每阶a导数在紧区间绝对一致收敛。

对a≥0作单边Laplace变换，\(\Re z>1/2\) 时得到
\[
 G_{f,\kappa}(z)=
 \frac{d(f)c(\kappa)}{z+1/2}+\frac{c(f)d(\kappa)}{z-1/2}
 -\sum_\rho\frac{m_\rho M_f(\rho)M_\kappa(1-\rho)}
                       {z-(1/2-\rho)}=0.                    \tag{7}
\]
换序由 \(\sum m_\rho|M_f(\rho)M_\kappa(1-\rho)|<\infty\)
及 \(\Re z-1/2>0\) 支付。
在避开离散极点的任何紧集，大高度项分母与 \(|\Im\rho|\) 同阶，
快速系数衰减给局部正常收敛。因此(7)是全平面亚纯函数。

亚纯恒等定理使全部留数为零。
±1/2处留数及 \(c(\kappa),d(\kappa)>0\) 给 \(d(f)=c(f)=0\)。
对每个固定ρ，另选足够窄的正κ，使支集上
\(\cos(\Im\rho\,t)>0\)，则 \(\Re M_\kappa(1-\rho)>0\)。
零点极的留数迫使 \(M_f(\rho)=0\)。
零点极不与次数极相撞，因为ρ≠0、1。遂有
\[
 \boxed{\mathcal K_{\rm mix}=\operatorname{rad}B=\mathcal R_{\rm val}.} \tag{8}
\]
这是完整标量根空间，未识别为任何几何principal像。

## 4. sharp中央核的直接读出

对 \(h^\sharp=h\in\mathcal S_{\exp}\)，
\(M_h(s)=M_h(1-s)\)、\(d=M_h(0)=M_h(1)\)。
完整线性显式公式给
\[
 D_h(\zeta):=2N(h*k_\zeta)=\int K_h(t)\zeta(t)dt,
\]
\[
 K_h(t)=2d\cosh(t/2)
        -\sum_\rho m_\rho M_h(\rho)e^{(\rho-1/2)t}.            \tag{9}
\]
K实偶光滑；每阶导数在紧t区间绝对一致收敛。
全部实偶紧支ζ消失等价于K=0。
其单边Laplace变换为
\[
 \frac{d}{z-1/2}+\frac{d}{z+1/2}
       -\sum_\rho\frac{m_\rho M_h(\rho)}{z-(\rho-1/2)}.        \tag{10}
\]
同样的正常收敛与留数证明给
\[
 \boxed{\forall\zeta,\ D_h(\zeta)=0
       \iff h\in\mathcal R_{\rm val},\quad h^\sharp=h.}        \tag{11}
\]
这里是完整标量中央核，不是未构造的全局HH₁核。

## 5. 真实非零源关系与405的准确交

405的实际源
\[
 \theta(r)=\pi r^2(\pi r^2-\tfrac32)e^{-\pi r^2},\quad
 h_0=E\theta,\quad p=(D^2+D)h_0
\]
满足
\[
 M_{h_0}(s)=\xi(s)/2,\quad
 M_p(s)=s(s-1)\xi(s)/2,\quad M_p(2)=\pi/6\ne0.                \tag{12}
\]
p实sharp、非零、属于实际像J和 \(\mathcal S_{\exp}\)，
其两个次数和全部零点值为零。因此p确实属于(8)、(11)的核。

若I是405的实际像闭包，则其原有证明与(8)给
\[
 \boxed{I\cap\mathcal R_{\rm val}=P_{\rm an}
                         =I\cap\ker d\cap\ker c.}             \tag{13}
\]
不由此断言 \(I=\mathcal R_{\rm val}\) 或所有解析关系都是几何主关系。

## 6. 紧支域中的核为零：明确使用经典不同零点输入

若非零 \(f\in C_c^\infty([-R,R])\)，则
\[
 |M_f(s)|\le\|f\|_1e^{R|\Re s|}.
\]
选 \(M_f(s_0)\ne0\)，Jensen公式在以s₀为中心的圆盘给
其零点数 \(n_f(T)=O_f(T)\)：半径2T上的对数最大模为O(T)，
而半径T的每个零点至少贡献log2。
这计数当然也控制不同零点。

此处使用既有的Conrey1989简单临界线零点定理：
简单零点数在高度T以下至少为 \(cT\log T\)，某个c>0。
原文定义与Theorem1见
[作者论文PDF](https://aimath.org/~kaur/publications/24.pdf)，PDF第1、3、4页
（第3页定义简单零点计数，第4页给Theorem1）。
这里只消费其已证的正比例和通常Riemann–von Mangoldt计数，
不重新证明该定理，不消费本项目近期比例证书，不取得新比例。

若f属于 \(\mathcal R_{\rm val}\)，这些不同的简单ζ零点都是M_f的零点，
与 \(O_f(T)\) 矛盾。因此
\[
 \boxed{\mathcal R_{\rm val}\cap C_c^\infty(\mathbb R)=\{0\}.}  \tag{14}
\]
不能只用含重数的 \(N(T)\asymp T\log T\) 跳过不同零点问题。
p的非紧支性与(14)完全相容。

## 7. 实际源闭像保留的高重数jets

对于405实际偶Schwartz源θ，θ(0)=0使θ(r)=O(r²)于0，
\[
 M_{E\theta}(s)=2\zeta(s)\int_0^\infty\theta(r)r^{s-1}dr.
\]
右端Mellin因子在 \(\Re s>-2\) 全纯，故每个重数mρ的零点满足
\[
 M_{E\theta}^{(j)}(\rho)=0,\qquad 0\le j<m_\rho.              \tag{15}
\]
每个Mellin导数求值在 \(\mathcal S_{\exp}\) 连续：
\(\int |t|^j e^{\Re\rho\,t}|f(t)|dt\) 由较大指数半范数控制。
所以闭像I也满足(15)。

(8)、(11)只迫使零阶值为零；mρ只是标量留数的系数。
它们不检测高阶jets，不能直接识别保留全部广义谱信息的源商。

## 8. 若有重零点，两个关系空间严格不同

这是条件性结论，不声称ζ实际存在重零点。
假设某个非平凡ρ的重数m≥2。
取其共轭与 \(s\mapsto1-s\) 的不同点轨道O，
令 \(Q(s)=\prod_{\lambda\in O}(\lambda-s)\)。
通常ζ在实区间(0,1)无零点，故轨道含2或4点；
Q实系数且 \(Q(1-s)=Q(s)\)。

若 \(M_f(\lambda)=0\)，一阶算子的右逆
\[
 g(t)=e^{-\lambda t}\int_{-\infty}^t e^{\lambda u}f(u)du
     =-e^{-\lambda t}\int_t^\infty e^{\lambda u}f(u)du        \tag{16}
\]
满足 \((D+\lambda)g=f\)、\(M_g(s)=M_f(s)/(\lambda-s)\)。
两式分别控制两端。取 \(K>N+|\Re\lambda|\)，
\[
 p_{N,0}(g)\le\frac{p_{K,0}(f)}{K-|\Re\lambda|};
\]
导数由 \(g'=f-\lambda g\) 递推，同样在 \(\mathcal S_{\exp}\) 内。
复值中间函数采用其自然复化。

从p出发，对轨道各点依次用(16)一次，得到
\[
 M_{g_O}(s)=\frac{s(s-1)\xi(s)}{2Q(s)}.                       \tag{17}
\]
每次的零矩条件均仍成立。Mellin唯一性及Q的对称性给gO实sharp；
它双次数零，全部零点值零，但轨道零点仅消失m−1阶，
违反I所需的m阶jet。因此
\[
 \boxed{\exists\rho,\ m_\rho\ge2
      \ \Longrightarrow\ P_{\rm an}\subsetneq\mathcal R_{\rm val}.} \tag{18}
\]
即使全部零点简单，等号仍需真实Mellin除法、像闭包和谱综合证明；
(18)不是简单零点定理，更不是RH证明。

## 9. 下一合同

完整标量混合核现已确定；真正源关系保留的信息还多一层。
下一步须比较 \(\mathcal R_{\rm val}\)、满足全部jets的空间与实际闭像I，
并核对它们对真实对应复合及正则单位的意义。
任何全局谱模型还须解释重数和广义模式，不能只读取标量迹后称为忠实谱。
弱读出极限与保双次数的源截断在[517](517-f1-weak-observable-limit-and-source-cutoffs.md)处理。
