# 522. 实际源商的最优中心化增长率与RH等价

2026-10-11。[T/R] 接续[520](520-f1-source-quotient-spectrum-and-centered-growth.md)、
[521](521-f1-moving-source-correction-and-uniform-resolvent.md)。
本稿补齐520没有证明的反向条件定理：若RH成立，指定实际商的双向次指数半范数界成立。
这是增长判据强度的识别，不是增长界的独立算术证明，也没有证明RH。

## 1. 原商拓扑及两个不同的完成

仍取
\[
 X=\mathcal S_{\exp,\mathbb C}/I_{\mathbb C},\quad
 I_{\mathbb C}=\mathcal R_{\rm jet,\mathbb C},\quad
 A=-D,\quad B=A-\tfrac12,\quad V_a=e^{-a/2}\tau_a.
\]
先在原空间取递增的合并半范数，再取商：
\[
 P_n(f)=\max_{0\le j\le n}\sup_t e^{n|t|}|f^{(j)}(t)|,
 \qquad \bar P_n([f])=\inf_{h\in I_{\mathbb C}}P_n(f-h).       \tag{1}
\]
\(P_n\)生成原拓扑，\(\bar P_n\)生成原商拓扑。
不能交换inf与max。各\(\bar P_n\)可能有非零核；
令\(E_n\)为\(X/\ker\bar P_n\)的Banach完备化，\(\iota_n:X\to E_n\)为稠密映射。
不假设每个\(\iota_n\)单射，也不把单一\(E_n\)当作整个原Fréchet商。

平移及I不变性给无条件粗界
\[
 \bar P_n(V_a x)\le e^{(n+1/2)|a|}\bar P_n(x).               \tag{2}
\]
因此\(V_a\)延拓为每个\(E_n\)上的Banach强连续群。
稠密像上的连续性来自原群；局部统一的(2)支付完成后的强连续性。
记其闭生成元为\(\mathfrak B_n\)。原商的光滑轨道给
\[
 \iota_n x\in\operatorname{Dom}\mathfrak B_n^k,\qquad
 \mathfrak B_n^k\iota_nx=\iota_n B^kx,\quad k\ge0.           \tag{3}
\]
这是从实际平移得到的生成元，不是从抽象Fréchet谱猜测的群。

## 2. 真实零点的宽度与外侧预解估计

定义未知的真实量
\[
 \beta=\sup_\rho|\Re\rho-\tfrac12|\in[0,\tfrac12].          \tag{4}
\]
函数方程对称给\(\sup\Re\rho=\tfrac12+\beta\)。
不假设上确界被某个零点达到，也没有算出β。

令\(\mathscr R(z)=(z-B)^{-1}\)为520的原商连续预解。
521的移动合法源、整函数\(Z(s)=(s-1)\zeta(s)\)的Harnack估计与实际一阶逆给：
对任意\(b>\beta\)、有限\(c\ge b\)和n，有m、C使
\[
 \bar P_n(\mathscr R(z)x)
 \le\frac{C}{1+|\Im z|}\bar P_m(x),
                    \quad b\le\Re z\le c.                 \tag{5}
\]
完整jets保证原商预解，不要求简单零点或零距下界。
\(\mathscr R(z)x\)在\(\Re z>\beta\)内为原Fréchet商值全纯函数。
可从520的实际尾积分及局部非零校准直接核对；移动源提供(5)的统一成本。

若\(\Re z>n+1/2\)，(3)及预解恒等式给
\[
 \iota_n\mathscr R(z)x
       =(z-\mathfrak B_n)^{-1}\iota_nx.                     \tag{6}
\]
这里右边的Banach群Laplace预解存在，由(2)的指数界支付；
两者满足同一生成元方程，Banach预解的唯一性证明(6)。
**只在这个初始半平面**将两者识别。
下文移线后的(5)不声称目标竖线属于整个\(\mathfrak B_n\)的Banach预解集。

## 3. 在每个合法初始线上支付反演

固定x、n，取\(c>\max(b,n+1/2)\)。预解代数恒等式为
\[
 \mathscr R(z)x
   =\frac{x}{z}+\frac{Bx}{z^2}
                   +\frac{\mathscr R(z)B^2x}{z^2}.          \tag{7}
\]
因为b>β≥0，z=0始终在后续所有竖线左侧。

在\(E_n\)内，(3)及两次实际时间积分给a≥0时
\[
 W_n(a)=\iota_n(V_a x-x-aBx)
        =\int_0^a(a-u)V_u\iota_n B^2x\,du.                 \tag{8}
\]
由(2)，\(e^{-ca}W_n(a)\)在正半线绝对可积；负半线延为零，0处连续。
绝对Fubini、Banach群Laplace积分及(6)给其Fourier变换
\[
 \widehat{e^{-c\cdot}W_n}(T)
       =\frac{\iota_n\mathscr R(c+iT)B^2x}{(c+iT)^2}.        \tag{9}
\]
初始线上Banach预解范数至多\(1/(c-n-1/2)\)，
所以(9)也在T上绝对可积。Banach值Fourier反演合法：
可先乘\(e^{-\epsilon T^2}\)，用Fubini得到Gaussian近似单位，
再由W的连续性及两端L¹支配令ε趋零。
于是对a≥0，
\[
 \iota_nV_ax=\iota_n(x+aBx)+\frac1{2\pi i}
   \int_{c-i\infty}^{c+i\infty}
            e^{za}\frac{\iota_n\mathscr R(z)B^2x}{z^2}\,dz. \tag{10}
\]
这没有要求一条对所有Fréchet半范数同时有效的初始Laplace线。

## 4. 实际移线及统一半范数

在固定矩形\(b\le\Re z\le c\)内，(5)使(10)的水平边为
\(O(e^{ca}|T|^{-3}\bar P_m(B^2x))\)，对每个固定a趋零；
两条竖边绝对可积。商值全纯性在\(E_n\)中保留，因此Banach值Cauchy定理给
\[
 \iota_nV_ax=\iota_n(x+aBx)+\frac1{2\pi i}
   \int_{b-i\infty}^{b+i\infty}
            e^{za}\frac{\iota_n\mathscr R(z)B^2x}{z^2}\,dz. \tag{11}
\]
没有跨越实际零点，也没有跨越正则化的极点0。
竖线积分满足
\[
 \left\|\frac1{2\pi i}\int_{b-i\infty}^{b+i\infty}\cdots dz\right\|_{E_n}
 \le C_{n,b}e^{ba}\bar P_m(B^2x),                           \tag{12}
\]
因为\(\int_{\mathbb R}(1+|T|)^{-1}|b+iT|^{-2}dT<\infty\)。
\(B=-D-1/2\)的连续性给\(\bar P_m(B^2x)\le C_m\bar P_{m+2}(x)\)。
修正项\(x+aBx\)也由\(C_be^{ba}\bar P_{n+1}(x)\)控制。
取一个更大的统一索引，得到
\[
 \boxed{\forall n,\ b>\beta,\ \exists m,C:
   \bar P_n(V_ax)\le Ce^{ba}\bar P_m(x),\quad a\ge0.}       \tag{13}
\]
m、C依赖n、b；不依赖a、x、零点或零点高度。

sharp是原商的连续复线性反演，并满足
\[
 f^\sharp(t)=e^{-t}f(-t),\qquad
 \sharp V_a=V_{-a}\sharp,
 \qquad\bar P_n(x^\sharp)\le C_n\bar P_{n+1}(x).
\]
把(13)应用于\(x^\sharp\)，再次应用sharp，便得所有a∈R的同一类界。
全过程保留全部Jordan块，没有先半单化。

## 5. 最优指数包络与520判据的反向

定义\(\omega_X\)为下列可容许指数b≥0的下确界：
\[
 \forall n\ \exists m,C\ \forall a\in\mathbb R,x\in X:
             \bar P_n(V_ax)\le Ce^{b|a|}\bar P_m(x).         \tag{14}
\]
521–(13)证明每个b>β都可容许。
反向，520每个真实零点的非零首Jordan向量u1给
\(V_a[u_1]=e^{a(\rho-1/2)}[u_1]\)。
选能检测它的\(\bar P_n\)，分别令a趋于正、负无穷，
任何可容许b必须满足\(|\Re\rho-1/2|\le b\)。取上确界便得
\[
 \boxed{\omega_X=\beta.}                                   \tag{15}
\]
未证明端点指数β本身可容许；只确定下确界。
不推出b=0的有界性或忠实酉化，重零点的多项式增长仍被保留。

任意连续商半范数由一个\(\bar P_n\)控制，所以(14)与520的半范数量词一致。
结合520已付的逆向，现在可以准确写成
\[
 \boxed{\text{RH}\iff
  \forall p,\epsilon>0\ \exists q,C\ \forall a,x:
       p(V_ax)\le Ce^{\epsilon|a|}q(x).}                    \tag{16}
\]
已无条件付清的是β≤1/2下的每个\(1/2+\epsilon\)指数界，
不是将未知β改小，也不是新的无零条带。
需要独立算术来源的正是β=0所对应的界，而非这条条件等价的解析反向。

## 6. 实际源修正版本和研究边界

由(1)及I=E源，(16)的增长合同也等价于：
\[
 \forall n,\epsilon>0\ \exists m,C\ \forall a,f\ \exists\theta\in\mathscr S_{e,0,\mathbb C}:
 P_n(V_af-E\theta)\le Ce^{\epsilon|a|}P_m(f).                \tag{17}
\]
增长界到(17)可选接近下确界的源，将常数放大；
若f=0直接取θ=0。反向先对代表f使用(17)，再对f−Eψ使用并取ψ下确界。
源像在V下不变，故同一商类被正确比较。
θ可以依赖n、ε、a、f；不要求原商具有连续线性截面。
如果在商下确界为零而输入P_m(f)>0，任意小的近似误差仍足以选择源。

521的源校准与本稿的完成／移线证明补齐解析增长桥。
[523](523-f1-natural-hilbert-collapse-and-growth-gap.md)说明自然酉Hilbert完成为何会丢掉整个商。
本轮不声称这种谱与增长关系具有世界优先权。
独立算术增长、Weil负性、几何principal及全局HH桥仍开放。
