# 342. 原物理cell中连续频带替换的总误差

2026-09-08。周期9第2动作的核准备。[T]。
Gibbs只读[独立复核通过](../reviews/2026-09-08/342-independent-review.md)。
保持335的规范化响应、原prime-power权、六窗和原shell；
给出一次有误差账本的近似，不把有限核与连续核直接认作相等。

## 1. 结论

写Q=X log X、D=round(Q)、M=X^(1/2)，335的有限核为K_X。
定义连续频带核
\[
 K_\infty(t)=\int_1^2\cos(2\pi\xi t)\,d\xi
 ={ \sin(4\pi t)-\sin(2\pi t)\over2\pi t},
 \quad K_\infty(0)=1,
\qquad
 \bar K_\infty(M)={1\over M}\int_0^M K_\infty(t)\,dt.
\]
令R_X^infty只把335式(3)的K_X及其共同平均替换为上述两者，
其余支持、mask、W及所有权重完全保留。则充分大X时
\[
 \boxed{R_X=R_X^\infty+O(1).}                          \tag{1}
\]
因此对这个固定规范化cell，R_X=o(log^4X)当且仅当R_X^infty=o(log^4X)。
这是便于实际求和的等价近似，尚未证明任一方的小量。

## 2. 全shell上的统一核误差

需要比粗Riemann误差O(|t|/Q)更强的界：
\[
 \sup_{|t|\le M}|K_X(t)-K_\infty(t)|\ll Q^{-1}.         \tag{2}
\]
|t|<=1时，对Lipschitz函数cos(2pi xi t)做有限Riemann比较，
同时计入|D/Q-1|<=1/(2Q)，直接得O(1/Q)。

1<=|t|<=M时，用337的精确几何和：
\[
 K_X(t)=A(t)\cos\Phi(t),\qquad
 A(t)={\sin(\pi Dt/Q)\over D\sin(\pi t/Q)},\quad
 \Phi(t)=2\pi t+(D-1)\pi t/Q.
\]
连续核是B(t)cos(3pi t)，B(t)=sin(pi t)/(pi t)。
令c=D/Q、x=pi t/Q，则
\[
 A(t)={1\over c}{x\over\sin x}{\sin(\pi ct)\over\pi t}.
\]
因|c-1|<=1/(2Q)、|x|<=pi M/Q=o(1)，有
\[
 \left|{1\over c}{x\over\sin x}-1\right|
 \ll Q^{-1}+t^2/Q^2,\qquad
 \left|{\sin(\pi ct)-\sin(\pi t)\over\pi t}\right|
 \le |c-1|\ll Q^{-1}.
\]
再用|sin(pi ct)/(pi t)|<=1/(pi|t|)，得到
|A-B|<<Q^-1+|t|/Q²<<Q^-1。
而|Phi-3pi t|<<|t|/Q，乘|B|<<1/|t|给O(Q^-1)。
三角函数的Lipschitz界遂证明(2)，不对渐近误差求导。

同一区间平均因此满足
|bar K_X(M)-bar K_infty(M)|<<Q^-1，
所以两个中心化核之差仍统一O(Q^-1)。

## 3. 同一实际shell的正质量

令epsilon=M/X=X^-1/2，保留335的原权q_ab q_cd。
因为0<=W<=1，去掉mask和h=0限制只会增加下列非负质量上界。
固定b,c,d in I，shell对a的条件是
bc/d e^-epsilon<=a<=bc/d e^epsilon。
其与I的交集包含O(Y epsilon+1)个整数。
用Lambda(a)<=C log X和a约Y，固定b,c,d的a权和至多
\[
 \sum_{\substack{a\in I\\|\log(ad/bc)|\le\epsilon}}
       {\Lambda(a)\over\sqrt a}
 \ll {L\over\sqrt Y}(Y\epsilon+1).
\]
其余三个prime-power权用Chebyshev
sum_(n in I) Lambda(n)/sqrt(n)<<sqrt Y，得
\[
 \sum_{\text{原shell}}q_{ab}q_{cd}W_{ab;cd}
 \ll L Y(Y\epsilon+1)
 =L(X+X^{3/4})\ll XL=Q.                              \tag{3}
\]
这只用全局Chebyshev和单项Lambda上界，没有假设短区间素数分布。
所有素数幂、四个Lambda权及两个4pi²归一化因子按335定义保留。
由(2)(3)得到(1)。

## 4. 使用范围

335没有ordinary完整cross_main_term另置的beta^4 D；
若恢复该因子，(1)的误差也须乘它，不能跨规范化称为O(1)。
本估计只对这个固定cell的合并四Lambda权证明，
不自动覆盖增长个数的cell或各个Vaughan通道的逐项绝对权。

后续可以先在原物理响应中做(1)，再对R_X^infty精确使用341的恒等式，
所有通道共用同一K_infty-bar K_infty和固定整数mask。
这样总替换误差只付一次O(1)，不需要为每个ghost通道另声称同一个上界。

没有将对数相位X log(ad/bc)线性化；它在整个M=X^1/2 shell内的二次修正
不能仅凭局部核极限丢弃。下一动作保留准确对数相位，写自由变量的Poisson公式、
端点修正和非零频率范围。
