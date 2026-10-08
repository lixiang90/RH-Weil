# 482. 原路线保留 Möbius 相消的条件完整误差改进

2026-10-08。基线 main `6149e0ac2d9c247b316fd81829185b211275b25c`。

本笔记在原引用输入 \([R_{7/8}]\) 下，把同一真实素数函数的
Type II 合成误差第四矩从481的无条件 \(13/21\) 改为条件 \(49/81\)。
其完整第四矩传递误差相应从 \(29/42\) 降到 \(779/1134\)。
剩余主项的整体 \(5/7\) 上界、零点比例和无零边界没有由此改变。

完整证明及其全部输入在
[研究源](../reviews/2026-10-08/hybrid-original-optimized-type-ii-remainder-research-checkpoint-audit.md)，
不同作者的逐项复核在
[独立审查](../reviews/2026-10-08/hybrid-original-conditional-perron-remainder-review-peer.md)。
本笔记不重新认证 \([R_{7/8}]\) 本身。

## 1. 同一函数和真实截断

沿用481的 \(X=T/(2\pi)\)、\(L=\log X\)、\(J_T=[T/4,4T]\)、
\(a_L\ge c_\phi>0\)，定义
\[
P_H(t)=\frac1{a_LL}\sum_{\sqrt X<p\le X}
       \frac{\log p}{\sqrt p}p^{it},\qquad
\mathcal M_F=T^{-1}\int_{J_T}|F(t)|^4dt.
\]
一般引用前件 \([R_\theta]\) 是普通 zeta 在整个
\(\Re s>\theta\) 无零，\(1/2\le\theta<1\)。先固定
\[
0<v<a,\quad v<1/4,\quad \max(1/2,a+v)<y<1,
\]
\[
U=V=\lfloor X^v\rfloor,\quad A=\lfloor X^a\rfloor,
\quad Y=X^y,\quad H=V^2,
\quad b_V(k)=\sum_{d\mid k,d\le V}\mu(d).
\]
原短 \(m\) 子项为
\[
S_A(t)=-\frac1{a_LL}
\sum_{\substack{U<m\le A,\ k>V\\Y<mk\le X}}
\frac{\Lambda(m)b_V(k)}{\sqrt{mk}}(mk)^{it}.
\]
所有 Möbius 符号和共同乘积边界保留。

## 2. 有限 Perron 先于取绝对值

令 \(N=\lfloor X\rfloor\)，展开有限乘积
\[
\left(\sum_{U<m\le A}\Lambda(m)m^{-z}\right)
\left(\sum_{d\le V}\mu(d)d^{-z}\right)
\left(\sum_{j\le N}j^{-z}\right).
\]
其长度 \(Z=AVN<X^2\)，归一化系数为
\(O_\phi(\tau_3(n)/\sqrt n)\)。对半整数
\(x^\sharp=\lfloor X\rfloor+1/2\)、
\(y^\sharp=\lfloor Y\rfloor+1/2\)，在
\(c=1/L\)、\(|\Im z|\le T/8\) 上施有限截断 Perron。
它恰好保留 \(Y<n\le X\)；外层移位高度始终在
\([T/8,33T/8]\)。

两个端点的全部误差，包括矩形展开中的所有 \(n>X\)，一致为
\[
O_{\phi,\eta}\left(X^{2\eta}
\left(\frac{\sqrt Z}{T}+\frac{\sqrt X\log(2X)}T\right)\right).
\]
由于 \(a+v<1\)，预先取充分小的 \(\eta\) 后仍有负幂。
没有在取绝对值后补用已消失的 Möbius 相消。

原 \([R_\theta]\) 下的短 Möbius 准入及全 prefix Abel 给
\[
\left|\sum_{d\le V}\mu(d)d^{-1/2-c+i\tau}\right|
\ll V^{\theta-1/2+\delta}X^\rho.
\]
内部 Möbius Perron 使用 \(O(T^2)\) 高度，与外层 Perron 分开。
其截断误差为 \(O(W^{1/2}T^{-2}\log^2T)\)，水平线须保留
\(O(W^{1/2}T^{-2+\rho})\)，不能将次幂费用写成固定对数费用。

同一正高度 guard 上，无权因子的 Weyl 上界为
\(X^{1/6}\log^C X\)，短 \(\Lambda\) 因子为 \(\sqrt A\log X\)。
再结合真实截断子项的二矩 \(\|S_A\|_{2,T}^2\ll X^\epsilon\)，得
\[
\boxed{\mathcal M_{S_A}\ll
 X^{1/3+a+(2\theta-1)v+\epsilon}}.
\]
所有 buffer 和次幂损失先按最终 \(\epsilon\) 分配。

## 3. 完整费用和限定最优参数

保留481的低段、Type I、proper prime powers 及完整平方丰满尾证明，
合成误差成本为
\[
\max\{2y-1,\ 1/3+2v,\ 1/3+a+(2\theta-1)v,
        \ 1-2a,\ 1-4v,\ 0\}.
\]
这个费用族的最小值为
\[
c_\theta=\frac{6\theta+7}{6\theta+15},\qquad
v=\frac2{6\theta+15},\quad a=2v,\quad
y=\frac{6\theta+11}{6\theta+15}.
\]
下界由 \(a\ge(1-c)/2\)、\(v\ge(1-c)/4\) 和短项成本直接推出；
这是该费用族的最优性，不是所有算术方法的最优性。

\(\theta=7/8\) 时，精确取
\[
U=V=\lfloor X^{8/81}\rfloor,\quad
A=\lfloor X^{16/81}\rfloor,\quad Y=X^{65/81},\quad H=V^2.
\]
剩余项保持真实系数及所有原截断：
\[
R_\mu(t)=-\frac1{a_LL}
\sum_{\substack{m>A,\ m\ \mathrm{prime}\\k>V,\ r(k)\le H\\Y<mk\le X}}
\frac{\Lambda(m)b_V(k)}{\sqrt{mk}}(mk)^{it},
\]
其中 \(r(k)=\prod_{v_p(k)\ge2}p^{v_p(k)}\)。于是
\[
P_H=R_\mu+E_\mu,\qquad
\boxed{\mathcal M_{E_\mu}\ll X^{49/81+\epsilon}}.
\]
它与481的不同参数余项不能互当子族。

## 4. 完整传递及尚未完成的主项

476在同一引用输入下给 \(\mathcal M_{P_H}\ll X^{5/7+\epsilon}\)。
先以范数差得到 \(R_\mu\) 的同幂上界，再用四矩 Hölder 差，得
\[
\boxed{\mathcal M_{P_H}=\mathcal M_{R_\mu}
       +O(X^{779/1134+\epsilon})},\qquad
\frac57-\frac{779}{1134}=\frac{31}{1134}.
\]
相对481，误差第四矩指数节省 \(8/567\)，传递指数节省 \(2/567\)。
这没有给出相对未知主项的渐近等价，也没有给出常数级四阶矩。

研究源另外保留481全部参数，将真实 genuine-prime \(m\) 带支付到
\(A_1=\lfloor X^{3/14}\rfloor\)，误差仍为 \(13/21\)。
这个结论先付全 \(k\) 带、再直接付其 \(r>H\) 尾，避免从有符号整体
范数推断子集范数。

剩余 \(r=1\) 的 balanced genuine-prime / squarefree 块仍开放，
生成函数的实际零点留数仍为 \(-m_\rho\)。本笔记不改善整体 \(5/7\)、
简单临界线比例或引用输入下的无零边界，未触发新纪录论文发布。
