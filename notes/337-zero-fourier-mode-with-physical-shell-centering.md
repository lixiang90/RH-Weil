# 337. 有限域完成中零Fourier模的物理中心化

2026-09-07。周期8第3动作的中心项核算。[T，内部独立复核通过]。
沿用336固定的离纤维延拓；不自由改变shell平均或实际六窗。

## 1. 目标与范围

336将335同一平窗cell写成R_X=M0+E_Kl。
本篇证明其真正的零Fourier模无条件满足
\[
 \boxed{|{\cal M}_0|\ll \log X=o((\log X)^4).}            \tag{1}
\]
常数只依固定cell比例及窗，充分大X的范围统一。
不是对E_Kl的估计，也不是全体factor/aperture cell的总账本。
这与235–239的共同常密度中心项小量原则一致，
不把再次控制常密度项宣称为四素数相关瓶颈的解决。

以下固定一个支持内的(a,b,c,d)，记z=bc asymp Y²=X^3/2，
W(delta)=Wcal_ab;cd(delta)，K=K_X、bar K=bar K_X(M)、M=X^1/2。
需要一致控制
\[
 S_{a,b,c,d}:=\sum_{\substack{h\in\mathbb Z,\ h\ne0\\
                    |X\log(1+h/z)|\le M}}
 W(\log(1+h/z))\{K(X\log(1+h/z))-\bar K\}.              \tag{2}
\]
只有1+h/z>0的h进入定义，其余置0。
这些h全在336的[-H,H]中。

## 2. 有限Gabor核的大小与全变差

Q=XL、D=round(Q)，xi_k=1+k/Q。精确式给
\[
 \bar K={1\over D}\sum_{k=0}^{D-1}
                 {\sin(2\pi\xi_k M)\over2\pi\xi_k M},
 \qquad |\bar K|\le{1\over2\pi M}.                        \tag{3}
\]
因此没有把bar K按绝对积分粗估成log(M)/M。
对|t|<=M，充分大X有M/Q<1/2，
\[
 |K(t)|+|K'(t)|\ll(1+|t|)^{-1}.                          \tag{4}
\]
证明：|t|<=1用有限平均及xi_k<=3。1<=|t|<=M时用精确几何和
K(t)=A_D(t)cos(Phi_D(t))，其中
A_D=sin(D pi t/Q)/(D sin(pi t/Q))，
Phi_D=2pi t+(D-1)pi t/Q。
分母绝对值>=2|t|/Q，D/Q asymp1，直接微分得
|A_D|<<1/|t|、|A_D'|<<1/|t|+1/t²、|Phi_D'|<<1。
这给(4)，没有对一个未控制的渐近误差求导。
从而
\[
 \int_{-M}^{M}|K'(t)|dt\ll\log(2+M),\qquad
 \int_{-M}^{M}|t|\,|K(t)-\bar K|dt\ll M.                \tag{5}
\]

两个周期区间的重叠满足0<=W<=1，以及
|W(delta)-W(delta')|<=2|delta-delta'|/L，
由一个区间与其平移的对称差长度给出。故
V(t)=W(t/X)在[-M,M]上Lipschitz，常数<=2/(XL)。
函数psi(t)=V(t)(K(t)-bar K)1_{[-M,M]}(t)连同端点跳跃满足
\[
 \|\psi\|_\infty\ll1,\qquad
 \operatorname{Var}(\psi)\ll\log(2+M).                   \tag{6}
\]
这里保留真实分段线性重叠，不需要额外光滑化。

## 3. 整数h求和与连续主项

将psi与单调变量t(h)=X log(1+h/z)复合并在其紧支持外置0，
全变差不增加。逐单位区间比较，任一紧支撑BV函数f满足
|sum_{h in Z}f(h)-integral_R f(u)du|<<Var(f)+||f||infty。
这里Var使用包含实际点值与端点跳跃的逐点全变差，不能只按几乎处处等价类
忽略整数点的特殊取值。
该形式包括非整数端点和按原定义取值的端点原子。
去掉h=0只再付O(1)。所以(2)等于
\[
 {z\over X}\int_{-M}^{M}
       W(t/X)(K(t)-\bar K)e^{t/X}dt+O(\log(2+M)).        \tag{7}
\]
令G(t)=W(t/X)e^{t/X}。因M/X=X^-1/2且L>=1，
|G(t)-G(0)|<<|t|/X。
共同平均的定义精确给
integral_-M^M(K(t)-bar K)dt=0。
因此(7)中的积分主项绝对值至多
\[
 {Cz\over X^2}\int_{-M}^{M}|t|\,|K(t)-\bar K|dt
 \ll {zM\over X^2}\ll1.                                 \tag{8}
\]
于是S_abcd=O(L)，统一于全部支持四元组。
这里h=0、Jacobian e^(t/X)、六窗变化和整数求和误差均已记入。
不能省略Jacobian后宣称主项精确为零；真正结果是(8)的有界误差。

## 4. 全部实际系数的质量

Chebyshev输入psi(U)=sum_{n<=U}Lambda(n)<<U，
同236的原始质量账本，给
\[
 \sum_{n\in I_X}{\Lambda(n)\over\sqrt n}\ll\sqrt Y,\qquad
 \sum_{a,b,c,d}C(a,b,c,d)\ll Y^2.                        \tag{9}
\]
C非负，distinct-base mask只减少总质量；不改变实际有符号核。
由336，M0=(p^-1-p^-3)sum_{a,b,c,d}C(a,b,c,d)S_abcd，
而p asymp Y²。用(8)之后的S=O(L)及(9)即得(1)。
只对已完成共同中心化的S取绝对值，未跨物理通道拆开相消。

## 5. 真正剩余问题

因此对这个固定实际cell，证明R_X=o(L4)等价于证明336的
E_Kl=o(L4)，因为已证M0=O(L)。
这个等价关系不提供E_Kl的新上界，也不自动把A(h,n)化成可分离系数。
目前未消除全模数频率、determinant合并以及原始四Lambda系数的相关困难。
下一动作必须改善这一真实余项的结构或净估计；
重新定义一个名为“Kloosterman预算”的同一开放量不算进展。
