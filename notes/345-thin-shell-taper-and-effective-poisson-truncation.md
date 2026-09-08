# 345. 极薄shell平滑与有效的Poisson有限截断

2026-09-08。周期9第4动作的频率尾部分。[T]。
Franklin只读[独立复核通过](../reviews/2026-09-08/345-independent-review.md)。
沿用335–344。本文控制一次有实际算术成本的平滑及远尾；
剩余有限非零频率和仍未估计，不把有限化算作关键高矩突破。

## 1. 固定平滑，先在合并物理和上付费

记H(t)=K_infty(t)-bar K_infty(M)、M=sqrt X，取delta=X^-1/4。
令rho(s)在s<=0时为0、s>=1时为1、中间为3s²-2s³，并设
\[
 \chi_\delta(t)=\rho((M-|t|)/\delta),\qquad
 T_\delta(t)=H(t)\chi_\delta(t).
\]
chi_delta是C1，分段C2，值在[0,1]；在|t|<=M-delta上等于1，在|t|>=M上为0。
R_delta是342合并原物理响应R_infty将H乘上chi_delta后的版本；
prime powers、原mask、W、两个q权、整数X均保持。

两者之差仅支撑M-delta<=|X log(ad/bc)|<=M，此处|H|<<1/M。
固定b,c∈I，令n=ad。每一端帽允许的n落在一个长度
\[
 O(bc\,\delta/X)=O(Y^2\delta/X)=O(X^{1/2}\delta)
\]
的实区间，因此整数n数O(X^(1/2)delta+1)。对每个n~Y²，
有序分解a d=n至多d(n)个；a,d在I时
Lambda(a)Lambda(d)/sqrt(ad)<<L²/Y。取固定eta=1/12，使用
d(n)<<_eta n^eta<<X^(1/8)，于是
\[
\begin{aligned}
 |R_\infty-R_\delta|
 &\ll {1\over M}\,{L^2\over Y}\,
       X^{1/8}(X^{1/2}\delta+1)
       \sum_{b,c\in I}{\Lambda(b)\Lambda(c)\over\sqrt{bc}}\\
 &\ll L^2X^{1/8}(\delta+X^{-1/2})
 \ll X^{-1/8}L^2=o(1).                              \tag{1}
\end{aligned}
\]
两端帽、归一化常数及整数区间的+1均保留。不需要端帽里的素数分布定理。
这里使用合并后的四Lambda权，不声称单个Vaughan通道的平滑误差也满足(1)。

所用除数界可自证：对p>=2^(1/eta)，a+1<=2^a<=p^(eta a)；
其余有限多个p各有sup_(a>=0)(a+1)p^(-eta a)<∞。
乘遍素因子即可得到一个只依赖固定eta的常数，无未证算术输入。

## 2. 平滑后自由变量的函数与导数账本

先做(1)，再按341精确展开Lambda(a)。固定m=rv及b,c,d，写
\[
 g_\delta(w)=(mw)^{-1/2}W(w)T_\delta(X\log(w/w_0))
                       {\bf1}_{[A/m,B/m]}(w),\qquad
 f_\delta(w)=g_\delta(w){\bf1}_{mw\ne b}{\bf1}_{mwd\ne bc}.          \tag{2}
\]
外层系数保持343-(2)，w0=bc/(md)。虽然形式上cell长约Y/m，
T_delta的非零支撑仍仅在w~w0~Y/m的窄shell。

由连续频带显式式，j=0,1,2时
|K_infty^(j)(t)|<<1/(1+|t|)，且|bar K_infty|<<1/M。
平滑端帽内|H|+|H'|<<1/M，故
\[
 \|T_\delta\|_\infty+\|T_\delta'\|_\infty\ll1,\qquad
 \int_{\mathbb R}(|T_\delta'|+|T_\delta''|)\,dt
 \ll L+(M\delta)^{-1}\ll L.                                      \tag{3}
\]
T_delta''为分段普通导数；T_delta'连续，端帽交界无额外点质量。
例如chi_delta'' H的积分为O(1/(M delta))，不能遗漏该项。
另有integral |T_delta|dt<<L。

置A_0(w)=(mw)^-1/2 W(w)、lambda=Xm/Y。
W由固定数量的区间min/max组成，在shell上分成O(1)个光滑片；
每片及斜率跳跃满足
\[
 |A_0^{(j)}(w)|\ll Y^{-1/2}w_0^{-j}\ (j=0,1,2),\qquad
 \sum |\operatorname{jump} A_0'|\ll Y^{-1/2}/w_0.                 \tag{4}
\]
这是实际原窗口的分段导数界，常数独立于m,b,c,d；
不将有Lambda的外层函数当作光滑函数。
由于t'=X/w~lambda、|t''|=X/w²，
以dt=t'dw在每片积分乘积的二阶导数，用(3)(4)并补入斜率转折和cell两端，
得到
\[
 \operatorname{TV}(g'_{\delta,\mathrm{reg}})
 \ll Y^{-1/2}\lambda L={XmL\over Y^{3/2}}.                        \tag{5}
\]
g'_(delta,reg)是每片普通导数，在cell外延为0；
cell端的导数跳跃计入TV，但g_delta本身的值跳跃另在下节计入。
具体积分项依次由
Y^-1/2(lambda/X²)integral|T_delta|、
Y^-1/2(lambda/X)integral|T_delta'|、
Y^-1/2 lambda integral|T_delta''|控制；
边界和(4)转折项也不超过(5)。

## 3. 只剩有理cell跳跃，统一控制对称远尾

g_delta连续越过shell端（那里函数及一阶导数均为0），
故其值跳跃仅可能在x_-=A/m、x_+=B/m，记跳量J_-,J_+。
各|J_j|<<Y^-1/2。按分布导数分部积分，对k!=0有
\[
 \widehat g_\delta(k)
 ={J_-e(-kx_-)+J_+e(-kx_+)\over2\pi i k}+\mathcal E_k,
 \qquad
 |\mathcal E_k|\le{\operatorname{TV}(g'_{\delta,\mathrm{reg}})
                              \over4\pi^2 k^2}.                 \tag{6}
\]
W的连续斜率转折进入后一TV，不产生1/k值跳跃项。

对有理x=A/m或B/m，若x整数，对称k与-k的跳跃项准确相消；
否则||x||>=1/m，几何和及分部求和给
\[
 \left|\lim_{S\to\infty}
 \sum_{R<|k|\le S}{e(-kx)\over2\pi i k}\right|
 \ll{1\over R\|x\|}\le {m\over R}.                               \tag{7}
\]
R>=1，不假设无穷和绝对收敛。结合(5)–(7)，每个固定外层
\[
 \left|\lim_{S\to\infty}\sum_{R<|k|\le S}\widehat g_\delta(k)\right|
 \ll {mY^{-1/2}+XmL/Y^{3/2}\over R}
 \ll {XmL\over Y^{3/2}R}.                                       \tag{8}
\]
极薄shell平滑避免了对原非有理shell端到整数的距离作任何定量假设。

全部其余三Lambda平方根权的质量O(Y^(3/2))。
再由Chebyshev分部求和
\[
 \sum_{\substack{r\ge1,v>V\\rv\le B}}|\mu(r)|\Lambda(v)\,rv
 \le\sum_{r\le B/V}r\sum_{v\le B/r}v\Lambda(v)
 \ll B^2\sum_{r\le B/V}{1\over r}\ll Y^2L,
\]
得到完整外层远尾
\[
 \boxed{\text{总对称远尾}\ll{XY^2L^2\over R}
                           ={X^{5/2}L^2\over R}.}               \tag{9}
\]
这里可以对外层系数取绝对值，完整I/II总成本已计算。
取R=ceil(X³)，远尾为O(X^-1/2 L²)，真正给出随X的有效有限截断。

## 4. 中心、点修正与最终仍需证明的量

中心常数仍是原bar K_infty(M)，没有随平滑重新选取中心。
相对343的每个零频积分，(2)的变化至多
C sqrt(Y) delta/(m X M)，因为只有总长度O(delta)的t端帽且|H|<<1/M。
对全部外层合计为
\[
 O\left({Y^2\delta\over XM}
       \sum_{rv\le B}{|\mu(r)|\Lambda(v)\over rv}\right)
 =O(\delta L^2).                                                \tag{10}
\]
因此若343零频结论成立，平滑版本的总零频仍O(L³)。

点修正准确满足P_delta(a)=chi_delta(X log(a/a0))P(a)，
因为乘子连续且不依赖a=rvw的分解；没有点值Jacobian。
因此按344-(1)–(3)在完整I+II合并后恢复Lambda(a)。
两cell端及两种删除点的界只用|H chi_delta|<=|H|，
故344的O(L²)照常；平滑后的shell端函数值为0，本版本不再需要其指数无理性条款。
这只是平滑版本的依赖缩减，未否定344对原硬端点的处理。

定义有限的实际余项
\[
 \mathcal N_{X,R}^{\delta}=
 \sum_{\substack{r\ge1,v>V,rv\le B\\b,c,d\in I,\ c\ne d}}
 {\mu(r)\Lambda(v)\Lambda(b)\Lambda(c)\Lambda(d)
                       \over16\pi^4\sqrt{bcd}}
 \sum_{0<|k|\le R}\widehat g_{\delta,rv,b,c,d}(k).
\]
343–345现已分别通过独立审查。对R=ceil(X³)
\[
 \boxed{R_X=\mathcal N_{X,R}^{\delta}+O(L^3),\qquad
 R_X=o(L^4)\ \Longleftrightarrow\
                 \mathcal N_{X,R}^{\delta}=o(L^4).}              \tag{11}
\]
这是有明确误差的有限求和接口，没有声称所有|k|<=R都是驻点频率。
343的原振荡相位仍仅可能在|k|~Xm/Y驻定；chi_delta引入的端帽导数已经计费。
实际有符号有限和及其外层相关仍是主缺口。仅有限化和去端点不满足GOAL第十节C。
