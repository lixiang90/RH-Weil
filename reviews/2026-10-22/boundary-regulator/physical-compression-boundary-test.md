# 物理半线压缩的次级边界量：原费用可付，全principal失败

2026-10-22。root直接核算，供独立逆审。此候选是物理卷积表示的半线边界，
未证明等于CCM的素数boundary restriction或其relative regulator；不能以同名boundary拼接。
只做一个明确候选的准入，不声称新的Weil正性或方法类边界。

## 1. 合法算子与exact乘法缺陷

固定物理r=e^(u/2)f∈S_exp,C，原H=L²(R,du)。令L_r为卷积，P_±为正/负半线投影，
W_r=P_+L_rP_+，H_r=P_+L_rP_-，G_r=P_-L_rP_+。
直接用卷积结合律与P_++P_-=1得

\[
 W_rW_s-W_{r*s}=-H_rG_s. \tag{1}
\]

H_r、G_r均为Hilbert–Schmidt：核r(x−y)分别限制x>0>y、x<0<y。换元v=x−y给

\[
 \|H_r\|_{HS}^2=\int_0^\infty v|r(v)|^2dv,
 \qquad\|G_r\|_{HS}^2=\int_{-\infty}^0|v||r(v)|^2dv. \tag{2}
\]

因此(1)右边迹类；在原S_exp域，核积分绝对收敛，迹为

\[
 \operatorname{Tr}(H_rG_s)=\int_0^\infty v\,r(v)s(-v)dv. \tag{3}
\]

这正是Wiener–Hopf/Hankel乘法缺陷的标准机制。primary背景仅定点核
[Basor–Ehrhardt 2005 v1 §3.1](https://arxiv.org/html/math/0502039v1)的乘法恒等式；
本文(1)–(3)直接从空间核证明，不调用其特殊symbol渐近或任何强Szegő定理。
算子符号r在这里是卷积核，和文献中的Fourier symbol不能同名互换。

保真实adjoint时L_r*=L_(r*)，r*(u)=overline(r(−u))，G_(r*)=H_r*。
于是单边缺陷与双边总量为

\[
 A_+(r)=\operatorname{Tr}(H_rH_r^*)\ge0,\qquad
 A_{\partial}(r)=\|H_r\|_{HS}^2+\|G_r\|_{HS}^2
 =\int|v||r(v)|^2dv. \tag{4}
\]

注意交换子trace为(3)的反对称化；不是(4)的正平方和。
具体Tr([W_r,W_s])=−∫_0∞v[r(v)s(−v)−s(v)r(−v)]dv。
不把antisymmetric cocycle、positive Hessian和完整Weil型混为一个量。

## 2. 真Fredholm行列式存在，不自动给平方RR

对每个真实源定义

\[
 D_r(t)=\det_F(I+t^2H_rH_r^*)\det_F(I+t^2G_rG_r^*),\quad t\in\mathbf R. \tag{5}
\]

两个positive trace-class因子使D_r(t)>0；由本征值展开，

\[
 0\le\log D_r(t)\le t^2 A_\partial(r),\qquad
 \log D_r(t)=t^2 A_\partial(r)+O(t^4\|H_rH_r^*\|_1^2+t^4\|G_rG_r^*\|_1^2)
\]

在t→0成立。n替t的large-scale leading项并未由小t展开给出；
更没有算术截面格、局部消失阶或RR的signed n²D²系数。这份正determinant是实际对象，
但不能把它的正性或Taylor二次项直接命名为平方容量。

## 3. 原du/Dlog费用与关系测试

对supp r⊂[−L,L]，(4)给

\[
 A_\partial(r)\le L\|r\|_{du}^2
 \le\frac L{\log2}\|r\|_{Dlog}^2. \tag{6}
\]

这是实际源费，未由全空间inverse下界代替。一般S_exp只需weighted L²有限，
不能删去L或宣称全线du统一界。相应HS map在每fixedL有明确连续费。

全principal测试已失败：405实际P=Cp非零且光滑，故

\[
 A_\partial(P)>0,\quad D_P(t)>1\quad(t\ne0). \tag{7}
\]

若两HS算子都零，(2)强迫P在非零点a.e.为零，连续性又给P=0，矛盾。
因此(4)/(5)均不消去p，更不消Pan全族。取537任意非零r_0同样得到正量，
所以非根通过不能补偿关系失败。P本身在S_exp而非compact域，(7)用实际weighted L²；
不将其强行放入固定紧窗测试。

加入任意fixed finite-rank正修补不能消去(7)的正项。
这句话只约束非负相加；允许signed counterterm、真实链supertrace、family/变域修复，另付身份及原费。
553已付全线连续coset-invariant positive quotient的更强稠密障碍，本文不重计。

## 4. 与actual DGA及完整项的关系

上轮T_P=∂K+K∂是实际链关系，而r→L_r、再压缩到P_+，只使用次数0代表元。
压缩不保乘法，正缺陷(4)恰未由任何degree−1 regulator抵消。故(7)不推DGA有矛盾，
只说明该裸secondary readout不下降。若有真实链supertrace/局部补偿可修，必须构造它；
仅把结果指定为完整Q，则正号仍承担Weil正性本身。

该物理边界没有内置素数、Γ/contact或双pole；它不能代替经典完整Q的这些项。
连续正反例都能作同样物理压缩，故它的positive square不选择正确Weil极化。
函数域真square RR另有同对象整性、有效性与局部对应，不能由(1)的compression anomaly替代。

消费：原费用可付且determinant真实存在的候选，仍在405关系门被否定；
这是标准边界设施的直接测试，不给新的classic容量或全源不等式。
停止该裸压缩入口，不续投影位置、Hankel次数或small-t参数。保真实相对链补偿与算术filtered提升为未排逃逸。
