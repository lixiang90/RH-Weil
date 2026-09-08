# 348. 偶窗口集合的相邻边谱势不能突破 MT 基线

2026-09-08。[T/N]，Franklin只读[独立复核通过](../reviews/2026-09-08/348-independent-review.md)。
这是347所选相邻边下界的解析适用边界，不是全部多窗口方法的上限。
没有新的实际零点比例，也不触发GOAL第十节的较远期验收。

## 1. 陈述与准确范围

令I=[-1/2,1/2]，取任意有限个实偶函数p_j∈L²(I)，
p_j>=0、integral p_j=1，以及theta_j>=0、sum theta_j=1。
设k_j(x)=integral_I p_j(u)exp(ixu)du，沿用347式(3)的相邻边势V。
本篇基线明确为
\[
 Q(p)=\int_I p^2+\iint_{I^2}|u-v|p(u)p(v)\,du\,dv,\qquad
 P_{\rm mix}=2-\sum_j\theta_jQ(p_j).
\]
取304的MT极小窗口
\[
 p_0(u)={\cos(\sqrt2u)\over\sqrt2\sin(1/\sqrt2)},\qquad
 C_0=2-Q(p_0)={3\over2}-{\cot(1/\sqrt2)\over\sqrt2}.
\]
304–305的解析包络给67/100<C0<17/25；C0约为0.6725007036794，
是此基线的历史常数，不是对最新研究比例的重新定级。
也可自含核验粗界：令s=sin(beta)/beta、c=cos(beta)、beta=1/sqrt2，
交错Taylor界给11/12<s<147/160、4379/5760<c<73/96，
故67/100<59/88<C0<3559/5292<17/25。
令E=sum_j theta_j Q(p_j-p0)。若347式(5)对所有非负gap成立，
参数0<=alpha<1、eta>=0，h有界，那么
\[
 \boxed{{P_{\rm mix}-\eta\over1-\alpha}-C_0
          \le-{4E\over25(1-\alpha)}\le0.}                         \tag{1}
\]
同一必要上界适用于任意有限记忆的望远镜修正，
只要它在常间距序列上的相邻状态相同且定义良好。
正权窗口中只要有一个不等于p0几乎处处，就有E>0。
不加窗口扰动，取alpha=eta=0、h=0，由V>=0可达C0。
所以此证书家族的基线输出上确界正好为C0。

## 2. 窗口基线损失的精确恒等式

记(Ap)(u)=p(u)+integral_I |u-v|p(v)dv。
由于(Ap0)''=p0''+2p0=0，且Ap0为偶函数，它在I上是常数。
任意实偶q∈L²(I)、integral q=0因而满足Q(p0,q)=integral q Ap0=0。
所以
\[
 Q(p_0+q)=Q(p_0)+Q(q),\qquad P_{\rm mix}=C_0-E.                  \tag{2}
\]
这里Q(p0,q)表示对称双线性形式。令F(u)=integral_(-1/2)^u q(v)dv；
它是奇函数，F(-1/2)=F(1/2)=0。分部积分给
\[
 \iint|u-v|q(u)q(v)\,du\,dv=-2\int F^2.
\]
在偶零均值空间的完整余弦基中写q=sum_(n>=1) a_n cos(2pi n u)，得到
\[
 Q(q)=\sum_{n\ge1}a_n^2\left({1\over2}-{1\over4\pi^2n^2}\right)
 \ge\left(1-{1\over2\pi^2}\right)\|q\|_2^2
 \ge {17\over18}\|q\|_2^2.                                      \tag{3}
\]
最后只用pi>3。先对有限余弦和计算，再由L²收敛及有界积分核连续性推广。
这也证明Q(q)>0当q非零；偶性是(3)所选谱间隙的必要假设。

对x>=2pi，q为偶函数且均值零，故可从cos(xu)中扣去其均值。
Cauchy–Schwarz及(3)给
\[
 |\widehat q(x)|^2\le\|q\|_2^2
 \left\{{1\over2}+{\sin x\over2x}
             -\left({2\sin(x/2)\over x}\right)^2\right\}
 \le {7\over12}\|q\|_2^2\le {21\over34}Q(q).                    \tag{4}
\]
这里hat采用exp(ixu)，不含额外2pi因子；x>=2pi>6足以给中间粗界。

## 3. 两个可解析定位的基线核零点

记a=sqrt2、beta=1/sqrt2。直接积分得
\[
 k_0(x)={a x\cot\beta\sin(x/2)-2\cos(x/2)\over x^2-2}.          \tag{5}
\]
在x=+-sqrt2处按连续延拓取值；以下根区间均远离这两个可去奇点。
对n=1,2，x=2pi n处的符号为(-1)^(n+1)。
在x=2pi(n+1/10)处，提出(-1)^n后分子严格为正：
cos beta>=3/4、sin beta<=beta给a cot beta>=3/2；
x>6且sin(pi/10)>sin(3/10)>29/100，
于是a x cot beta sin(pi/10)>2，而2cos(pi/10)<=2。
上述正弦界由pi>3、pi<4及sin t>=t-t³/6得到。
连续性给两个零点
\[
 g_1\in(2\pi,11\pi/5),\qquad g_2\in(4\pi,21\pi/5).
\]
无需证明其唯一性。写z_l=g_l/(2pi)，则1<z1<1.1、2<z2<2.1。
定义
\[
 w_1={C_0z_2-1\over z_2-z_1},\qquad
 w_2={1-C_0z_1\over z_2-z_1}.                                   \tag{6}
\]
由C0的粗界，两个权重均为正，且
w1+w2=C0、w1 z1+w2 z2=1。
这是为证书必要条件构造的对偶权重，不是零点间距的概率分布。

## 4. 常间距序列给统一上限

在347式(5)中取u=v=w=g_l，h的差严格抵消，故
alpha<=V(g_l,g_l,g_l)+eta z_l。
相邻边度的系数2/d-1/d²在d>=1时至多1，于是
\[
 \mathcal V(g_l,g_l,g_l)
 \le 2\sum_j\theta_j|k_j(g_l)|^2
 =2\sum_j\theta_j|\widehat{(p_j-p_0)}(g_l)|^2.                  \tag{7}
\]
末式使用k0(g_l)=0，是本证明限于相邻边的关键。
将必要条件乘w_l并相加，再用(4)、(6)，得到
\[
 C_0\alpha-\eta
 \le2\sum_j\theta_j\sum_{l=1}^2w_l|\widehat{(p_j-p_0)}(g_l)|^2
 \le{21C_0\over17}E\le{21\over25}E.                            \tag{8}
\]
把(2)代入输出，恰有
(P_mix-eta)/(1-alpha)-C0=(C0 alpha-eta-E)/(1-alpha)；
因1-alpha>0，(8)即得(1)。没有小扰动假设或数值网格误差。
实际固定分块的端点成本不会提高正的候选输出，不能解除此上界。

## 5. 对当前路线的影响

347的有限矩阵下界仍正确；(1)表明只保留相邻边时，
即使允许任意有限偶窗口集合及任意有限记忆的有界修正，
其精确基线损失已超过可能回收的局部谱收益。
先前八个扰动参数的浮点预筛只属[E]；本篇给出的范围更大且不依赖那份计算。

本篇不排除含第二邻点或更远边的347式(2)：
k0(g_l)=0通常不迫使k0(2g_l)=0，(7)的消失条件随即失效。
也不排除不同试探矩阵、非偶窗口、其他基线或新算术输入。
尤其没有证明Devine五行证书或304三点机制无效。
下一动作应检查含第二邻点的完整度归一化势及其净值，
而不继续在本篇已覆盖的相邻边家族内寻优。
