# 519. 真正源像闭合、完整重数关系与双次数源矩

2026-10-11。[T/R] 接续[518](518-f1-quantitative-mellin-division-and-mobius-source.md)。
在405指定拓扑中完成实际源像识别。Gaussian及谱实现路线有既有文献来源，
不声称首次构造ζ谱；新工作是本仓库明确空间、重数、常数及原映射接口的证明。

## 1. 实际像恰为完整零点jets空间

405的连续线性映射为
\[
 E:\mathscr S_{e,0}\longrightarrow\mathcal S_{\exp},\qquad
 E\theta(t)=2\sum_{n\ge1}\theta(ne^t).
\]
两端快速衰减及连续性已由405的Schwartz估计和Poisson求和证明。
记J为其实际像，I为原Fréchet闭包。

516的必要性与518的实际重建给
\[
 \boxed{J=I=\mathcal R_{\rm jet}
   =\{f:M_f^{(j)}(\rho)=0,\ 0\le j<m_\rho,\ \forall\rho\}.}   \tag{1}
\]
未对目标添加双次数条件。完整jets求值连续，所以该像闭。
E单射：在Re s=2上 \(M_{E\theta}=2\zeta M_+\theta\)，ζ非零；
正实Mellin的Fourier唯一性给θ=0。
因而E是两个明确Fréchet空间之间的连续双射，开映射定理给
\[
 \boxed{E:\mathscr S_{e,0}\simeq\mathcal R_{\rm jet}
       \text{为拓扑实线性同构。}}                           \tag{2}
\]
逆就是518的Möbius源，不是一般无限维商的任选截面。

也可直接核对逆连续性。设
\[
 q_{c,n}(G)=\sup_\tau(1+|\tau|)^n|G(c+i\tau)|,
 \quad c=2,3,\ldots\ \text{或}\ c=-1,-3,\ldots.
\]
这些线避开全部G极。对普通Schwartz半范数
\(Q_{A,j}(\theta)=\sup_r(1+|r|)^A|\theta^{(j)}(r)|\)，
取K满足 \(2K+1\ge j\)，518的两端积分给
\[
 Q_{A,j}(\theta_f)\le C_{A,j,K}\left(
 q_{A+2,j+2}(G_f)+q_{-2K-1,j+2}(G_f)
                              +\sum_{k=1}^K|\alpha_k|\right). \tag{3}
\]
高处q由定量除法控制；这些线的有界高度部分没有非平凡或平凡零点；
α由有限个Mellin求值控制。(3)因此是f的有限个指数半范数界。

## 2. 两个目标次数的真正源表达

令 \(G=M_+\theta=M_f/(2\zeta)\)，f=Eθ。
ζ(0)=−1/2，而ζ在1的留数为1，故
\[
 G(0)=-c(f),\qquad G(1)=0,\qquad G'(1)=d(f)/2.
\]
这给出绝对收敛的实际源积分
\[
 \boxed{c(E\theta)=-\int_0^\infty\theta(r)\frac{dr}{r},\qquad
 d(E\theta)=2\int_0^\infty\theta(r)\log r\,dr.}                \tag{4}
\]
它们与源准入的θ(0)=0、∫θ=0不同。
405实际Gaussian源的G(0)=−1/4、G′(1)=1/8，
准确恢复c=d=1/4，不能把整个源像当成双次数零关系。

于是
\[
 P_{\rm an}=I\cap\ker d\cap\ker c
\]
在实际源侧恰对应四项约束：原准入两项，加上(4)两个积分为零。
518给源原点的每个偶Taylor系数
\[
 \theta_f^{(2k)}(0)
  =(2k)!\frac{M_f(-2k)}{2\zeta'(-2k)}.                        \tag{5}
\]
两次数、非平凡零点重数、平凡零点的源Taylor数据分别有明确职责。

## 3. 来源卷积、平移与Fourier—sharp相容

对 \(g\in\mathcal S_{\exp}\)、\(f=E\theta\)，405真实源作用为
\[
 \theta_g(r)=\int_{\mathbb R}g(t)\theta(e^{-t}r)dt,\qquad
                       E\theta_g=g*f.                       \tag{6}
\]
其Schwartz半范数由
\[
 \sup_r|r^a\theta_g^{(b)}(r)|
 \le\sup_r|r^a\theta^{(b)}(r)|
                         \int|g(t)|e^{(a-b)t}dt
\]
控制；θg保持原点零值和零积分，所有换序已有绝对界。
由E单射，(6)准确等于从 \(g*f\) 重建的唯一源。
完整jets在乘积 \(M_gM_f\) 中保留，故(1)也是闭卷积理想。

平移 \(\tau_a f(t)=f(t-a)\) 对应源
\(\theta_a(r)=\theta(e^{-a}r)\)，原准入仍成立。
405的自对偶Fourier约定给
\[
 (E\theta)^\sharp=E\widehat\theta,\qquad
              \theta_{f^\sharp}=\widehat{\theta_f}.          \tag{7}
\]
偶源上正负Fourier号一致。这里依靠原Poisson恒等式和唯一性，
没有给算术配对添加自由相位。

这些是实际线性及卷积来源的相容；不把它们冒称几何对应的有效复合、
结构层乘法、正则单位商或主除子定理。

## 4. 标量关系空间与源关系空间相等的精确判据

516已经证明
\[
 \operatorname{rad}B=\mathcal R_{\rm val}
  =\ker d\cap\ker c\cap\{f:M_f(\rho)=0,\ \forall\rho\}.
\]
由(1)，
\[
 \boxed{P_{\rm an}=\mathcal R_{\rm jet}\cap\ker d\cap\ker c.} \tag{8}
\]
若所有非平凡零点简单，jets条件就是值条件，所以两者相等。
若存在重零点，516的完整共轭轨道一阶除法给一个
实sharp、双次数零、全部零点值零的函数，却少了一阶必要导数，
故不属于I。于是
\[
 \boxed{P_{\rm an}=\mathcal R_{\rm val}
       \iff\zeta\text{全部非平凡零点简单。}}                   \tag{9}
\]
这是关系空间的等价判据，未证明简单性或RH。
即使两者相等，剩余商上配对的独立Weil非正性仍需证明。

## 5. 与既有Schwartz谱实现的准确比较

[Meyer math/0412277v3](https://arxiv.org/pdf/math/0412277v3)的
Theorem3.3已证明ζ算子像闭且与偶Schwartz源拓扑同构；
Theorem4.1刻画相应Mellin商衰减；Corollary4.2给对偶谱的零点重数。
本轮核读这些陈述及其证明，PDF第5–8页；不以此认证该文后续全部核迹计算。

其所有实指数权的对数Schwartz交空间与405的 \(\mathcal S_{\exp}\)
拓扑相同：多项式对数权由多加一个指数权控制；反向由带权Schwartz上确界控制。
本项目E为其ζ算子的2倍，源两项条件一致。
因此闭像和Fréchet谱属于既有机制。本轮定量除法与Möbius重建
支付本仓库完整jet表述和双次数接口，不主张世界优先权。

下一步已不再是重复证明同一Mellin除法，而是
[520](520-f1-source-quotient-spectrum-and-centered-growth.md)中独立的中心化增长约束。
全局HH完成、几何principal、RR与正Hilbert桥仍未建立。
