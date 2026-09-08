# 343. 自由整数变量的Poisson公式及总零频率

2026-09-08。周期9第2–3动作。[T]。
Gibbs只读[独立复核通过](../reviews/2026-09-08/343-independent-review.md)。
先按342将合并原响应换为连续频带，总付一次O(1)，再精确展开一个分子Lambda。
此处不把其他素数权当作平滑权，也不把双分子四通道的和换成单一通道。

## 1. 固定外层与真实分段函数

沿用341，写m=rv，v>V、m<=B，A=ceil(.70Y)、B=floor(1.30Y)，
U=V=max(2,round(Y^(1/4)))，epsilon=X^-1/2。
b,c,d为I内prime powers且c!=d；Type I取r<=U，Type II取r>U。
令a0=bc/d、w0=a0/m，并定义
\[
 J=[u_-,u_+]
 =[A/m,B/m]\cap[w_0e^{-\epsilon},w_0e^\epsilon].
\]
J为空时以下积分与和为零。对正实w，以a=mw代入335的区间端点和周期重叠，
记实际重叠为W(w)，Delta=log(w/w0)。区间端点取实数只是自由变量的连续延拓；
在所有整数w处与既定物理mask和窗口一致。

设
\[
 g(w)=(mw)^{-1/2}W(w)
 \{K_\infty(X\log(w/w_0))-\bar K_\infty(M)\}{\bf1}_J(w),
\]
\[
 f(w)=g(w){\bf1}_{w\ne b/m}{\bf1}_{w\ne w_0}.           \tag{1}
\]
闭区间J保留原端点值；两个指定点删除对应a=b与ad=bc。
若两点重合，删除一次。J为单点的情形也按(1)定义。
w无Lambda或mu权；外层仍保留
\[
 {\mu(r)\Lambda(v)\Lambda(b)\Lambda(c)\Lambda(d)
        \over16\pi^4\sqrt{bcd}}.                       \tag{2}
\]
一个分子展开后两通道之和已经恢复R_X^infty；
若随后展开c才得到I/I、I/II、II/I、II/II四通道。

## 2. 带端点与删除点修正的准确求和

令
\[
 \widehat g(k)=\int_J(mw)^{-1/2}W(w)
 \{K_\infty(X\log(w/w_0))-\bar K_\infty(M)\}e(-kw)\,dw,
 \quad e(x)=e^{2\pi ix}.
\]
有限个点的删除不改变此积分。准确恒等式为
\[
 \boxed{\sum_{n\in\mathbb Z}f(n)
 =\lim_{R\to\infty}\sum_{|k|\le R}\widehat g(k)+E_{\rm pt},}
 \quad
 E_{\rm pt}=\sum_{n\in\mathbb Z}
 \left(f(n)-{f(n-)+f(n+)\over2}\right).                \tag{3}
\]
E_pt只可能来自整数端点、两个被删除的整数点或退化为整数单点的J。
当J非退化时，未删除的整数端点补半个原g值；
区间内部被删除的整数点减整个原g值。重合点以(3)计算，不能重复计数。
逐外层有|E_pt|<<Y^-1/2，但这个界尚不能在巨大外层和中直接丢掉。

证明：g在紧支撑内分段C1，只有有限个值跳跃和斜率转折，因而具有逐点有界变差。
其周期化P(x)=sum_n g(x+n)在每周期只有有限项，Fourier系数恰为g_hat(k)。
Dirichlet–Jordan收敛在x=0给P左右极限的平均。
减去和加入原整数点实际值即得(3)，包含孤立删除点和退化J。
这也是Miller–Schmid原文第1页(1.2)的中值求和口径；
不使用只对Schwartz函数陈述的无端点版。

对每个固定X，外层r,v,b,c,d是有限集合，故可先合并外层，再取同一个R极限。
这里没有证明某个有限R(X)截断有统一小误差；也不声称Fourier和绝对收敛。

## 3. 所得到的核与非零频率范围

对sigma=+1或-1、1<=xi<=2，定义
\[
 I_\sigma(k,\xi)=\int_J(mw)^{-1/2}W(w)
 e\{\sigma\xi X\log(w/w_0)-kw\}\,dw,
 \quad I_0(k)=\int_J(mw)^{-1/2}W(w)e(-kw)\,dw.
\]
那么精确地
\[
 \widehat g(k)=\frac12\int_1^2
       \{I_+(k,\xi)+I_-(k,\xi)\}\,d\xi
                       -\bar K_\infty(M)I_0(k).        \tag{4}
\]
对数相位的w导数是sigma xi X/w-k。
所以若J非退化，振荡项可能的驻点仅在相同符号的k，且
\[
 X/u_+\le |k|\le2X/u_-,
\quad |k|\asymp X/w_0\asymp Xm/Y=X^{1/4}m.            \tag{5}
\]
“可能”不意味每个整数k都有驻点，也不包括中心项I_0的频率判断。
这个频率尺度不是原自由区间长Y/m，更不是模数平方根长度。
对固定xi，若驻点存在，其准确位置w_*=xi X/|k|，
相位须保留log(w_*/w0)；不能未经误差分析替换成线性相位。

式(4)目前是实振荡积分核，没有直接生成完整有限域S或Kl2。
硬端点在大频率尾部一般只给1/|k|型衰减；
无驻点本身并不保证靠近驻点频率范围边缘时有统一的这种界。
不能对全部k取绝对值后仍假设无穷尾和有限。
后续必须处理端点、频率相消和外层算术关系。

## 4. 所有外层合计的Poisson零频率可控

定义Z_X为将(2)乘g_hat(0)，再对全部r,v,b,c,d求和的量，
即两通道的零频率总量。以下甚至对外层系数取绝对值，也得到
\[
 \boxed{|Z_X|\ll L^3=o(L^4).}                         \tag{6}
\]
它不包含E_pt或任何非零k。

换元t=X log(w/w0)，有
\[
 \widehat g(0)={\sqrt{a_0}\over mX}
 \int_{\mathcal T} \widetilde W(t)e^{t/(2X)}
       \{K_\infty(t)-\bar K_\infty(M)\}\,dt,            \tag{7}
\]
其中T=[-M,M]与Xlog(A/a0)<=t<=Xlog(B/a0)的交，
Wtilde是原a=a0 exp(t/X)及Delta=t/X的重叠。
该重叠满足0<=Wtilde<=1、Lip(Wtilde)<<1/(XL)：
移动a的支持端点与移动Delta均只按log a或Delta作Lipschitz平移，
min和max不增加阶数，周期化重叠用区间对称差界控制。
因此G(t)=Wtilde(t)exp(t/(2X))有|G(t)-G(0)|<<|t|/X。
G不含T的截断或删点mask，G(0)使用第1节固定的连续延拓。
在边界情形a0可略在cell外；非空shell保证所需延拓仍在固定比例的扩大cell内，
上述变化常数一致。不能因整数w0被删除而将G(0)设为零。

若完整shell都在cell内，即a0 e^(-epsilon)>=A且a0 e^epsilon<=B，
则T=[-M,M]。准确中心平均使integral_(−M)^M(K_infty-bar)=0，
且integral_(−M)^M |t| |K_infty-bar|dt<<M，所以
\[
 |\widehat g(0)|\ll{\sqrt Y M\over mX^2}.              \tag{8}
\]
若J非空但shell被cell边界截断，则a0位于
[A e^-epsilon,A e^epsilon]或[B e^-epsilon,B e^epsilon]。
对任何子区间T⊂[-M,M]，
|integral_T K_infty(t)dt|<<1
（逐xi积分sin/(2pi xi)），而|bar K_infty||T|<<1。
以G(0)为常数并用上面的变化估计，得到
\[
 |\widehat g(0)|\ll{\sqrt Y\over mX}.                  \tag{9}
\]

完整shell的其余三Lambda权总质量O(Y^(3/2))。
边界三元组固定b,c后，d落在O(1)个长度O(Yepsilon)的区间；
单项Lambda(d)/sqrt(d)<<L/sqrt(Y)，故这部分质量
O(L sqrt(Y)(Yepsilon+1))。
乘(8)(9)后，分别为
O(Y²M/(mX²))=O(1/m)，以及
O(LY(Yepsilon+1)/(mX))=O(L/m)。

最后由Chebyshev分部求和，
\[
 \sum_{\substack{r\ge1,v>V\\rv\le B}}
       {|\mu(r)|\Lambda(v)\over rv}
 \le\sum_{r\le B/V}{1\over r}
       \sum_{v\le B/r}{\Lambda(v)\over v}
 \ll L^2,
\]
得到(6)。U切分只是这个总和的子集，故零频率绝对外层界也分别适用于两通道。
没有以逐通道的核替换误差冒充342合并后的O(1)。

## 5. 净状态与来源

结合342与(3)，当前同一物理响应精确化为：一次O(1)核替换误差、
已控O(L³)的Poisson零频率、尚待合计的E_pt，以及全部非零k的有符号外层和。
后两项必须实际控制，才能得到o(L^4)。
长纤维局部积分可写不等于整个四阶相关完成；Type II多外层共同求和也未被否定。

原始背景：
[Miller–Schmid, math/0304187v1](../literature/background/miller-schmid-summation-0304187v1.pdf)，
第1页(1.1)–(1.2)及左右极限口径已核读；第2–3页只作范围比较，
未导入其GL3公式或认证全证。
[Sutherland, Lecture16](../literature/background/sutherland-poisson-lecture16-20151105.pdf)
第1–2页提供Schwartz版及周期化证明，本篇端点处理另有上述自含说明。
