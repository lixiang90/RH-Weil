# 486. 原有限 Perron 的长因子四矩与完整误差改进

2026-10-08。继续原数域和同一个真实素数函数，基线 main
`e51a51e2225c9216b23cc7b12bc97e8fa8cf2ea1`。

普通 zeta 在整个 \(\Re s>7/8\) 无零这一引用前件下，
本轮得到原完整误差第四矩
\[
\boxed{\mathcal M_E\ll X^{9/17+\epsilon},\qquad P_H=R+E,}
\]
以及原完整第四矩的传递
\[
\boxed{\mathcal M_{P_H}=\mathcal M_R+O(X^{159/238+\epsilon}).}
\]
相对484的 \(43/75\)、\(713/1050\)，分别节省
\(56/1275\)、\(14/1275\) 的指数。
同一长因子方法还无条件支付一套完整误差 \(3/5\)，
但剩余主项的完整四矩仍未改善。没有常数级中心四阶预算、
新零点比例或新无零边界。

连续证明和全部前件见
[长因子研究源](../reviews/2026-10-08/hybrid-original-extended-inner-zeta-fourth-perron-research-perron.md)，
不同作者全文复核见
[独立审查](../reviews/2026-10-08/hybrid-original-extended-inner-zeta-fourth-perron-review-peer.md)。
本笔记不把有限算术检查当作这些无限估计的证明。

## 1. 保持原函数，延长一个有限因子

保持 \(X=T/(2\pi)\)、\(L=\log X\)、\(J_T=[T/4,4T]\)、
\(a_L\ge c_\phi>0\)，以及
\[
P_H(t)=\frac1{a_LL}\sum_{\sqrt X<p\le X}
 \frac{\log p}{\sqrt p}p^{it},\qquad
\mathcal M_F=T^{-1}\int_{J_T}|F(t)|^4dt.
\]
外 Perron 仍取 \(c=1/L\)、高度 \(T/8\)，全部移位
\(t-\omega\in[T/8,33T/8]\) 保持正。

将无权有限因子从 \(j\le\lfloor X\rfloor\) 延长到
\(j\le N=\lfloor10T\rfloor\)。新增的 \(j>X\) 在二因子或三因子
产品中都产生 \(n>X\)，所以不改变原 \(Y<n\le X\) 的任何系数。
这些新增系数仍要完整支付：先保留有限矩形，再对两个半整数端点施
Perron，绝对误差为
\[
O\left(X^{2\eta}
 \{\sqrt Z/T+\sqrt X\,T^{-1}\log(2X)\}\right),\qquad Z<X^{2-\xi}.
\]
\(Z\) 是该有限产品的完整长度；\(\xi>0\) 先固定。
误差包含全部 \(n>X\)、近端项及远尾，不替换为无限 Dirichlet 乘积。

## 2. 长因子的真实正高度第四均值

对 \(W_N(s)=\sum_{j\le N}j^{-s}\)，整数端点 Euler 公式保留
主极点项、半端点和整个 \(\psi\) 积分。
先对 \(\psi\) 作 Abel Fourier 正则化，再逐非零频率积分分部：
\(N\ge9T\) 排除所有驻点，完整尾以 \(\sum h^{-2}\) 绝对求和。
因此在所需正高度及固定实部域统一得到
\[
W_N(s)=\zeta(s)+O(T^{-\Re s}).
\]
同一个固定 \(N\) 上以半径 \(c/2\) 作 Cauchy，另得
\[
W_{\log,N}(s)=\sum_{j\le N}(\log j)j^{-s}
 =-\zeta'(s)+O(T^{-\Re s}L).
\]

[Montgomery–Vaughan 原书 Theorem 26.23](https://personal.science.psu.edu/rcv4/Vol3/Vol3.pdf)
给 \(|\sigma-1/2|\le2/\log(5T)\) 的统一第四均值。
它覆盖本次 \(1/2+c\) 及全部 Cauchy 圈，得到
\[
\sup_{|\omega|\le T/8}\|W_N(1/2+c-i(t-\omega))\|_{4,T}\ll L,
\]
\[
\sup_{|\omega|\le T/8}\|W_{\log,N}(1/2+c-i(t-\omega))\|_{4,T}\ll L^2.
\]
这个接口不使用无零假设；\(\zeta'\) 的第四均值由 Cauchy 和上述
\(\zeta\) 第四均值推出，不能用 \(|\zeta\zeta'|^2\) 代替。

## 3. 同一短项与原 Type I

固定 \([R_\theta]\)：普通 zeta 在整个 \(\Re s>\theta\) 无零，
\(1/2\le\theta<1\)，令 \(\beta=2\theta-1\)。
\(U=V=\lfloor X^v\rfloor\)、\(A=\lfloor X^a\rfloor\)、\(Y=X^y\)，
满足 \(0<v<a\)、\(v<1/4\)、\(\max(1/2,a+v)<y<1\)。

在同一短项 \(S_{B,A,q}\) 中，保留真实 \(\Lambda\)、\(\mu\) 和
\(Y<mk\le X\)，先恢复掩码，再以484的全部 prefixes、极点和 prime mask
合同控制 \(F_\Lambda,G_V\) 的点值；只有长 \(W_N\) 使用第四均值。
共享 \(\omega\) 的一次 Minkowski 得
\[
\mathcal M_{S_{B,A,q}}\ll X^{2\beta(a+v)+\epsilon}.
\]
\(\Lambda\) 主极点和其余内部尾均保持负幂费用。
这条估计不在所有更长的 \(A\) 上优于旧 Weyl 费用。

原 Type I 保留两个真实对象
\[
I_2=\frac1{a_LL}\sum_{d\le UV}\frac{g_{U,V}(d)}{\sqrt d}d^{it}
          \sum_{Y/d<j\le X/d}j^{-1/2+it},
\]
\[
I_3=\frac1{a_LL}\sum_{d\le V}\frac{\mu(d)}{\sqrt d}d^{it}
          \sum_{Y/d<j\le X/d}(\log j)j^{-1/2+it},
\qquad g_{U,V}=-\Lambda_{\le U}*\mu_{\le V}.
\]
其外权绝对质量分别为 \(O(X^vL)\)、\(O(X^{v/2})\)。
同一有限 Perron 与长因子第四均值直接给
\[
\mathcal M_{I_2+I_3}\ll X^{4v+\epsilon}.
\]
这项不认领新的 Möbius 相消，也不依赖 \([R_\theta]\)。

## 4. 完整分区及 \(9/17\)

\(H=V^2\)，原低段、大 proper powers、完整平方丰满 \(r>H\) 尾
保持已有证明。合成费用为
\[
C=\max\{2y-1,4v,2\beta(a+v),1-2a,1-4v,0\}.
\]
在所列费用族内，最优值是
\[
c_\theta=\max\left\{\frac12,\frac{6\theta-3}{6\theta-1}\right\}.
\]
这不是所有算术方法的最优性。
\(\theta=7/8\) 取
\[
U=V=\lfloor X^{2/17}\rfloor,\quad A=\lfloor X^{4/17}\rfloor,
\quad H=V^2,\quad Y=X^{13/17}.
\]
五项费用是 \((9/17,8/17,9/17,9/17,9/17)\)。
完整余项仍为
\[
R=-\frac1{a_LL}
\sum_{\substack{m>A,\ m\ {\rm prime}\\k>V,\ r(k)\le H\\Y<mk\le X}}
\frac{\Lambda(m)b_V(k)}{\sqrt{mk}}(mk)^{it},
\]
\[
b_V(k)=\sum_{d\mid k,d\le V}\mu(d),\qquad
r(k)=\prod_{v_p(k)\ge2}p^{v_p(k)}.
\]
全部 floors、负号、原正高度及共同乘积端点保留；非零 core 的一次
素因子部分仍至少为2。此配置与484不同，不能免费互当子族。

先合成 \(E=P_H-R\)，再用476使 \(R\) 继承原完整 \(5/7\) 上界，
最后以 Hölder 差得到 \((3(5/7)+9/17)/4=159/238\)。
距该增长基线节省 \(11/238\)，仍不能视作常数级 \(o(1)\)。

## 5. 无条件付款与既有边界应用

若不使用 \([R_\theta]\)，短 \(F_\Lambda,G_V\) 直接以其真实绝对质量
\(O(\sqrt{AV}L^C)\) 控制，短项费用变为 \(2(a+v)\)。
取 \((v,a,y)=(1/10,1/5,4/5)\)，同一完整分区的五项费用为
\((3/5,2/5,3/5,3/5,3/5)\)。因此无条件有
\(\mathcal M_E\ll X^{3/5+\epsilon}\)，这只改进完整误差。

另接受451已经交付的 \(\theta_* =11/12-e_*/4\) 及其全部引用依赖，
\(657e_*^3-954e_*^2+21e_*+20=0\)，得
\[
c_* =\frac{5-3e_*}{9-3e_*},\quad
v_* =\frac1{9-3e_*},\quad a_*=2v_*,\quad
y_* =\frac{7-3e_*}{9-3e_*}.
\]
消费476的 \(B_I(\theta)=4\theta-3+3(1-\theta)/(2\theta)\)，
完整传递指数为 \(\gamma_*=(3B_I(\theta_*)+c_*)/4\)，严格包围
\[
0.5293832084010138<c_*<0.5293832084010156,
\quad 0.6679943043150209<\gamma_*<0.6679943043150252.
\]
这是既有边界的应用，不能把451的全族前件缩减为普通 zeta 的单条
\([R_{7/8}]\)，更没有得到新无零边界。

## 6. 固定旧对象的扩大截断与下一主项

保持484全部 \(V,H,Y,b_V\)，其真实素数 \(m\) 截断可从
\(X^{16/75}\) 扩到 \(X^{62/225}\)，完整误差仍为 \(43/75\)。
保持482全部配置时，可扩到 \(X^{74/243}\)，误差仍为 \(49/81\)。
每一带均先付全部 \(k\)，再直接付同一 \(m\) 掩码的 \(r>H\) 尾，
两个完整函数之差才支付真实 \(r\le H\) 带，不使用子集范数单调性。

原完整生成函数的零点留数仍为 \(-m_\rho\)。长因子方法没有供应
balanced prime/squarefree 的联合四阶相消；项目已准入的
简单临界线比例67.3482429920796…%、既有无零边界及完整增长界保持。
下一任务仍为该真实余项与高产品次弧的完整联合预算。

## 7. 有限检查的准确范围

[检查脚本](../scripts/hybrid_padded_perron_checkpoint.py)和
[保存输出](../output/hybrid-padded-perron-checkpoint.json)绑定最终研究源、
不同作者审查、本笔记及451/476输入的 canonical LF 身份。
使用 `python -B scripts/hybrid_padded_perron_checkpoint.py --check` 只读复核。
它只检查费用有理数、参数分支、已有三次根区间和严格指数包围，
不证明长截断、无限 Perron、实际相消、无零前件、零点比例或 RH。
连续分析依据仍是所链接的完整证明和独立审查。
