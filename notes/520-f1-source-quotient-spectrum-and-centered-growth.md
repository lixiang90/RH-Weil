# 520. 实际源商的完整Fréchet谱与中心化增长关口

2026-10-11。[T/R] 接续[519](519-f1-closed-source-image-and-degree-moments.md)。
在明确的实际源商内给连续预解算子和完整Jordan重数。
这完成本模型的Fréchet谱识别；不是正Hilbert自伴实现，也不是全局HH同构。

## 1. 明确对象、算子与谱的含义

复化519的空间与真实源像，取Hausdorff Fréchet商
\[
 X=\mathcal S_{\exp,\mathbb C}/I_{\mathbb C},\qquad
                         I_{\mathbb C}=\mathcal R_{\rm jet,\mathbb C}.
\]
源像在平移及D下不变，故
\[
 A=-D,\qquad M_{Af}(s)=sM_f(s),\qquad
 (\tau_a f)(t)=f(t-a)
\]
下降到X，A连续，平移的生成元为A。
定义本稿使用的连续预解谱
\[
 \sigma_c(A)=\{\lambda\in\mathbb C:
  A-\lambda:X\to X\text{没有连续的双侧线性逆}\}.              \tag{1}
\]
这里没有把Fréchet空间当成Banach或Hilbert空间。

沿用405的实际非零 \(h_0=E\theta_0\in I\)，令
\[
 H_0(s)=M_{h_0}(s)=\xi_{\rm Riemann}(s)/2.
\]
这里ξ是405的整完成函数，H0的零点恰是全部非平凡ζ零点，
阶数恰为mρ；H0(0)=H0(1)=1/4，平凡零点已被Gamma补偿。

## 2. 任意非零点处的连续实际预解

对任意λ，若M_f(λ)=0，516的一阶实际右逆
\[
 R_\lambda f(t)=e^{-\lambda t}\int_{-\infty}^t e^{\lambda u}f(u)du
             =-e^{-\lambda t}\int_t^\infty e^{\lambda u}f(u)du
\]
满足
\[
 (D+\lambda)R_\lambda f=f,\qquad
 M_{R_\lambda f}(s)=\frac{M_f(s)}{\lambda-s}.                 \tag{2}
\]
任意固定λ的两端估计仍成立：取K>N+|Reλ|，
\[
 p_{N,0}(R_\lambda f)\le
                   p_{K,0}(f)/(K-|\Re\lambda|);
\]
导数由 \(g'=f-\lambda g\) 递推。因此(2)是明确闭子空间上的连续线性映射。

当λ不是非平凡零点，H0(λ)≠0。定义
\[
 S_\lambda g=g-\frac{M_g(\lambda)}{H_0(\lambda)}h_0,\qquad
 T_\lambda g=-R_\lambda S_\lambda g.                         \tag{3}
\]
其Mellin变换为
\[
 M_{T_\lambda g}(s)
   =\frac{M_g(s)-M_g(\lambda)H_0(s)/H_0(\lambda)}{s-\lambda}. \tag{4}
\]
分子在λ处为零，目标空间两端条件由(2)支付。
Tλ连续并保持I：g的全部ρ-jets零时，分子仍满足全部jets，
而 \(s-\lambda\) 在每个ρ附近是单位。
故Tλ诱导X上的连续映射，且
\[
 (A-\lambda)T_\lambda[g]=[g].
\]
若 \((A-\lambda)[f]=0\)，则 \((s-\lambda)M_f\) 全部ρ-jets零；
同一个单位论证给f∈I。因此A−λ单射，Tλ是连续双侧逆。
所有非零点，包括0、1及负偶整数，都不属于(1)。

## 3. 每个真实零点的完整Jordan链

固定ρ及真实重数m=mρ。令u0=h0，逐次作合法一阶除法
\[
 u_j=-R_\rho u_{j-1},\qquad
 M_{u_j}(s)=\frac{H_0(s)}{(s-\rho)^j},\quad1\le j\le m.     \tag{5}
\]
在第j步，前一分子的ρ零阶矩仍为零，所以(2)逐次准入。
u_j是真正 \(\mathcal S_{\exp,\mathbb C}\) 函数；
它们通常不在源像I，正是需要保留的商类。
原函数空间已经有
\[
 (A-\rho)u_j=u_{j-1}.
\]
商中 \([u_0]=0\)，故(5)成为长度m的Jordan链。
u_j在ρ的消失阶数恰为m−j，在所有其他零点保持完整jets；
这给 \([u_1],\ldots,[u_m]\) 线性独立，特别是 \([u_1]\ne0\)。
所以每个ρ都是实际点谱，属于(1)。

反向，若 \((A-\rho)^k[f]=0\)，则f在其他零点保持全部jets，
在ρ处至少消失 \(\max(m-k,0)\) 阶。
模I后，该空间单射进入剩余 \(\min(k,m)\) 个ρ-jets；
(5)给恰这么多个独立向量。因此
\[
 \boxed{\sigma_c(A)=\{\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\},\quad
 \dim\ker(A-\rho)^k=\min(k,m_\rho).}                         \tag{6}
\]
广义代数重数恰为mρ，没有假设全部零点简单。
不据(6)声称X拓扑等于全部无约束的零点jet乘积，或具有Hilbert正交谱基。

## 4. 中心化实际平移及重数的多项式因子

令 \(V_a=e^{-a/2}\tau_a\)。在(5)的有限Jordan块上，
\[
 V_a[u_j]=e^{a(\rho-1/2)}
                  \sum_{\ell=0}^{j-1}\frac{a^\ell}{\ell!}[u_{j-\ell}].
                                                               \tag{7}
\]
可由有限维生成元求解，也可将
\(e^{as}-e^{a\rho}\sum_{\ell=0}^{j-1}a^\ell(s-\rho)^\ell/\ell!\)
的j阶消失与H0的m阶消失相乘，直接验证差属于I。

Reρ−1/2决定双向指数增长，重数决定多项式增长。
因此一个保留Jordan信息的独立增长合同可以是：
对X每个连续半范数p及每个ε>0，存在连续半范数q和C，使
\[
 p(V_a x)\le C e^{\epsilon|a|}q(x),
                      \qquad a\in\mathbb R,\ x\in X.        \tag{8}
\]
若(8)有不依赖RH的算术证明，则对非零 \([u_1]\) 选p使其值正，
在a→+∞和a→−∞分别使用(7)，得到
\(|\Re\rho-1/2|\le\epsilon\)。ε任意，故所有ρ都在中心线。

这只证明(8)是充分合同，未证明它与RH等价，也没有从离散谱自动推出(8)。
每个有限中心线Jordan块的多项式因子与任意ε>0的界相容；
无限个块的统一半范数控制仍是实质问题。

## 5. 为什么忠实酉化是更强的要求

若X有正定范数，V_a在其忠实Hilbert实现中成为酉作用，
(7)对u1立即迫使Reρ=1/2。
若某个m≥2，进一步有
\[
 \|V_a[u_2]\|
   =\|[u_2]+a[u_1]\|
   \ge |a|\|[u_1]\|-\|[u_2]\|,
\]
而酉性要求它恒等于 \(\|[u_2]\|\)，矛盾。
故这一忠实酉化目标还会迫使全部零点简单，强于单纯RH。
不能先丢掉高阶jets，再把剩余值模型当成原源商的忠实酉化。

本轮准确付清的是实际Fréchet商的全零点与广义重数，
不是自伴Hilbert–Pólya谱。独立双向次指数增长(8)、算术Hodge/Weil符号、
几何principal及全局HH桥仍未付清。

## 6. 文献与下一合同

[Meyer math/0412277v3](https://arxiv.org/pdf/math/0412277v3)
已经给相应Schwartz商的谱实现及对偶重数，见PDF第6–8页。
本稿在405的符号下显式写出原商的连续预解及Jordan函数；
不主张首次谱实现，也不把本稿的谱定义泛化为所有Fréchet谱概念。

下一步应检验来自真实算术来源的双向增长估计，尤其是(8)所需
统一半范数如何在对应复合、源商和所有零点高度下保持。
单靠已有源Hilbert空间的酉性不能传到这个源余核；
仅将(7)重写成谱公式也不会提供新的增长约束。
