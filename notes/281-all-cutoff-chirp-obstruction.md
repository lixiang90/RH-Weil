# 281. 全部 cutoff 的固定 chirp 正源障碍

日期：2026-09-06。路线：NCE-8 / B1z；论文归属：Vaughan--Brownian response。

状态：[T/N] 一个固定正整数源在所有充分大尺度和全部匹配 cutoff 上的反例；
[T] 指定历史 guard、质量与统一实部频带下界；
[N] 模型系数 Dirichlet 级数在 \(s=1/2\) 的非亚纯奇点；
[O] 实际 von Mangoldt 中频上界和解析结构的充分性。
本篇不证明 RH/GRH，不把任意正整数权当作素数幂权或 \(L\) 函数，
也不预先宣称文献新颖性。没有使用数值实验。

## 1. 与278不同的量词

278 构造了同一固定源的一条合格失败共尾序列，但仍允许跳过其坏尺度。
本篇用一个遍布大尺度、瞬时 log 频率增长的光滑振荡替代稀疏块，
使换 cutoff 和跳过尺度两种选择都不能在该模型中修复预算。
这不排除实际 \(\Lambda\) 利用本模型没有的解析或乘法结构。

### 定理281-A [T/N]

存在一个固定数列 \(\lambda(n)\in[1/2,3/2]\)、\(n\ge2\)，使对每个固定
\(0<\sigma<\beta<1/2\)，以下结论对所有充分大的实数 \(Y\)
及全部整数 \(N\in[Y,2Y]\) 一致成立。
记
\[
 d=\tfrac12-\sigma>0,\quad\delta=\beta-\sigma>0,\quad
 L=\log Y,\quad a_Y=Y^d\ell(Y),\quad
 \ell(x)=\max(1,\log\log\log x)
 \tag{1}
\]
（小自变量处作下述固定光滑延伸），并令
\[
 \psi_\lambda(x)=\sum_{2\le n\le x}\lambda(n),\quad
 R_\lambda(x)=\psi_\lambda(x)-x,\quad
 P_{\beta,\lambda}(N)=\max_{1\le n\le N}\frac{|R_\lambda(n)|}{n^\beta}.
 \tag{2}
\]
这个源满足全局误差及双向振荡
\[
 R_\lambda(x)=O(\sqrt x\ell(x)),\qquad
 R_\lambda(x)=\Omega_\pm(\sqrt x\ell(x)).
 \tag{3}
\]

在同一 Abel 权 \(w_Y(x)=x^{-\sigma}e^{-x/Y}\)、实际连续背景
\(w_Y(x)\,dx\) 和共同 cutoff 下，记
\[
 H_{Y,N}(u)=\sum_{2\le n\le e^u}\lambda(n)w_Y(n)-\int_1^{e^u}w_Y(x)\,dx,
 \quad0\le u\le\tau=\log N,
 \qquad M=H_{Y,N}(\tau).
 \tag{4}
\]
则
\[
 M\asymp_\sigma a_Y>Y^{1/2-\sigma}\sqrt{\ell(Y)},\qquad M>0,
 \tag{5}
\]
并满足275-B预先指定的严格历史门槛，且有固定余量：
\[
 P_{\beta,\lambda}(N)N^\delta
 <\tfrac12C_{\sigma,\beta}M,
 \qquad C_{\sigma,\beta}=\frac{16e^2 2^\beta}{1-2^{-\beta}}.
 \tag{6}
\]
特别地，有真正的指数历史包络和双边范数规模
\[
 |H_{Y,N}(u)|\ll_{\sigma,\beta}M e^{\delta(u-\tau)},\qquad
 \|H_{Y,N}\|_1\asymp_{\sigma,\beta}M,\qquad
 \|H_{Y,N}\|_2^2\asymp_{\sigma,\beta}M^2.
 \tag{7}
\]
然而对固定宽度单侧频带
\[
 I_Y=[L-2,L-1]
 \tag{8}
\]
有真实正通道响应的统一双边界
\[
 \boxed{\quad
 \frac{J_{4,I_Y}}{\mu^4}\asymp_{\sigma,\beta}L\longrightarrow\infty,
 \qquad \mu=M/S.
 \quad}
 \tag{9}
\]
这里 \(p,c,r,S,D,J_4\) 使用与275、277完全相同的定义，只把素数源系数
替换为这一个固定 \(\lambda(n)\)。频带 \(I_Y\) 最终位于
\(\sqrt L<\xi\le L\)，是279真正未闭合的中频，而非最高尾壳。

因此，对这个模型的任何共尾 \((Y_m,N_m)\)、\(N_m\in[Y_m,2Y_m]\)，
全部充分大的数据点都已满足质量和历史条件，同时
\(J_4/\mu^4\to\infty\)。不存在靠另选这样的 cutoff 或共尾尺度成功的例外。
这个量词仍只针对已明确构造的正整数模型，不针对实际 \(\Lambda\) 或所有
具有 Euler 乘积、函数方程、亚纯对数导数的模型。

## 2. 一个固定全局源及完全一致的离散化

取 \(b=3/4\)。把 \(\ell\) 在小自变量处延伸成固定正的光滑非减函数，
使它在足够大 \(x\) 恰等于 \(\log\log\log x\)。
选一个足够大的固定 \(u_0\)，取光滑函数 \(\chi\) 满足
\[
 0\le\chi\le1,\qquad\chi(u)=0\ (u\le u_0),\qquad
 \chi(u)=1\ (u\ge u_0+1),
 \tag{10}
\]
其过渡形状固定，导数一致有界。定义
\[
 \mathcal R(x)=\chi(\log x)\sqrt x\ell(x)
                   \left[b+\cos\!\left(\frac{(\log x)^2}{2}\right)\right].
 \tag{11}
\]
这是同一个全局函数，没有在选择 \(Y,N\) 后修改源。
其导数满足
\[
 |\mathcal R'(x)|\ll x^{-1/2}\ell(x)(1+\log x)+x^{1/2}|\ell'(x)|
 \longrightarrow0
 \tag{12}
\]
于高段成立；过渡区的导数也受同一趋零量控制。
先把 \(u_0\) 取足够大，可保证 \(|\mathcal R'|\le1/2\) 处处成立。
于是固定定义
\[
 \mathfrak q(x)=1+\mathcal R'(x)\in[1/2,3/2],\qquad
 \lambda(n)=1+\mathcal R(n)-\mathcal R(n-1)
           =\int_{n-1}^n\mathfrak q(x)\,dx.
 \tag{13}
\]
这证明要求的正性与系数界。

因为 \(\mathcal R(1)=0\)，对整数 \(n\) 精确有
\(R_\lambda(n)=\mathcal R(n)-1\)；实数端点仅另有小于1的线性漂移。
因此得到 (3) 的全局上界。在任意大的
\((\log x)^2/2=2\pi k\) 与 \((2k+1)\pi\) 点，
\(b+\cos((\log x)^2/2)\) 分别为 \(7/4\) 与 \(-1/4\)。
移到相邻整数改变 \(\mathcal R\) 至多 \(1/2\)，故两种符号均保留
\(\sqrt x\ell(x)\) 量级，得到 (3) 的 \(\Omega_\pm\)。

对任意整数 \(N\) 及绝对连续 \(g\)，单位区间比较给
\[
 \left|\sum_{n=2}^N\lambda(n)g(n)-\int_1^N\mathfrak q(x)g(x)\,dx\right|
 \le\frac32\int_1^N|g'(x)|\,dx.
 \tag{14}
\]
取 \(g=w_Y\) 时误差为 \(O_\sigma(1)\)。取
\(g=w_Y(x)(\cos(\xi\log x)-1)\) 时，由
\[
 |g'(x)|\le2|w'_Y(x)|+|\xi|w_Y(x)/x,\quad
 \int_1^\infty|w'_Y(x)|dx\le1,\quad
 \int_1^\infty w_Y(x)dx/x\le1/\sigma,
 \tag{15}
\]
误差为 \(O_\sigma(1+|\xi|)\)，一致于全部 \(Y,N\)。
所以它既不会随 cutoff 积累，也没有删除 \(-M\) 中心项。

## 3. 一个统一的慢变振幅引理

写 \(z=N/Y\in[1,2]\)，\(L=\log Y\)。在整条 \(v\) 轴上定义
\[
 B_Y(v)=e^{dv-e^v}\chi(L+v)\frac{\ell(Ye^v)}{\ell(Y)},
 \qquad B(v)=e^{dv-e^v}.
 \tag{16}
\]
在 \(v\le\log2\) 上，充分大 \(Y\) 时有 \(0\le B_Y(v)\le2B(v)\)，
因为 \(\ell\) 非减且 \(\ell(2Y)/\ell(Y)\to1\)。每个固定 \(v\) 上又有
\(B_Y(v)\to B(v)\)。由于 \(d>0\)，函数
\((1+|v|)^mB(v)\) 在 \(( -\infty,\log2]\) 对每个固定 \(m\) 可积。
故 dominated convergence 给
\[
 \int_{-\infty}^{\log2}|B_Y(v)-B(v)|\,dv\longrightarrow0.
 \tag{17}
\]
乘以 \(\sigma+e^v\) 后同样成立。
这是一致于 \(z\in[1,2]\) 的截断积分控制，而不是在
\(v\to-\infty\) 处声称慢变比值逐点一致趋于1。

还将反复使用下列初等 Fourier 界：若 \(G\) 局部绝对连续且
\(G,G'\in L^1(-\infty,\log2]\)，
且 \(G\) 在该区间有一致有界端点值，则
\[
 \sup_{a\le\log2}\left|\int_{-\infty}^a G(v)e^{i\omega v}\,dv\right|
       \ll_G(1+|\omega|)^{-1}.
 \tag{18}
\]
对大 \(|\omega|\) 这是一次分部积分，小频率用 \(L^1\) 上界。
下文所用 \(G\) 均为 \(B(v)\)、\((\sigma+e^v)B(v)e^{iv^2/2}\)
或 \(B(v)e^{iv^2/2}\)，其导数可积由指数衰减直接保证。
因此不需要对一个随 \(Y\) 变化的振幅偷用统一导数界。

## 4. 全部 cutoff 的质量及历史 guard

### 引理281-B [T]

以 \(\gamma(d,z)=\int_0^z t^{d-1}e^{-t}\,dt\) 记下不完全 Gamma 积分。
对所有 \(z=N/Y\in[1,2]\)，有一致渐近式
\[
 \boxed{\quad
 \frac{M(Y,N)}{a_Y}
 =\frac b2\gamma(d,z)
   +z^de^{-z}\cos\!\left(\frac{(L+\log z)^2}{2}\right)+o_\sigma(1).
 \quad}
 \tag{19}
\]

证明。由 (14) 及 \(\mathcal R(1)=0\)，
\[
 M(Y,N)=w_Y(N)\mathcal R(N)
          +\int_1^N(-w'_Y(x))\mathcal R(x)\,dx+O_\sigma(1).
 \tag{20}
\]
除以 \(a_Y\) 后，端点的慢变比值 \(\ell(N)/\ell(Y)\) 对 \(z\in[1,2]\)
一致趋于1。积分部分变为
\[
 \int_{-\infty}^{\log z}(\sigma+e^v)B_Y(v)
       [b+\cos((L+v)^2/2)]\,dv.
 \tag{21}
\]
由 (17)，先把 \(B_Y\) 换成 \(B\)，误差一致为 \(o(1)\)。
振荡部分在提出相位 \(e^{iL^2/2}\) 后具有频率 \(L\)，由 (18) 为
\(O_\sigma(L^{-1})\)。慢部分与端点相加，利用精确恒等式
\[
 z^de^{-z}+\int_0^z(\sigma+t)t^{d-1}e^{-t}dt
       =(d+\sigma)\gamma(d,z)=\tfrac12\gamma(d,z),
 \tag{22}
\]
即得 (19)。整个证明没有假设端点振荡相位收敛。\(\square\)

由于 \(0<d<1/2\)、\(z\ge1\)，
\[
 \gamma(d,z)\ge\int_0^1 t^{d-1}(1-t)dt
       =\frac1{d(d+1)}\ge\frac43,
 \qquad z^de^{-z}\le e^{-1}\quad(1\le z\le2).
 \tag{23}
\]
故令 \(b_0=1/2-e^{-1}>0\)，(19) 给
\[
 b_0+o(1)\le M/a_Y\ll_\sigma1
 \tag{24}
\]
对所有 cutoff 一致，证明 (5)。这正是慢偏置选择 \(b=3/4\) 的用途：
它使 Abel 净质量不会被端点相位选成零，但仍保留 \(b-1<0\) 的全局负振荡。

由 \(|\mathcal R(n)|\le(7/4)\sqrt n\ell(n)\)、\(1/2-\beta>0\)，有
\[
 P_{\beta,\lambda}(N)
 \le1+\tfrac74 N^{1/2-\beta}\ell(N).
 \tag{25}
\]
因此一致地
\[
 \frac{P_{\beta,\lambda}(N)N^\delta}{M}
 \le\frac{(7/4)2^d+o(1)}{b_0+o(1)}<32
 \quad\text{于充分大的 }Y.
 \tag{26}
\]
例如 \(e^{-1}<3/8\) 给 \(b_0>1/8\)，从而极限上界小于
\(14\sqrt2<20\)。另一方面
\(C_{\sigma,\beta}/2=8e^2 2^\beta/(1-2^{-\beta})>8e^2>32\)，
故 (26) 严格蕴含 (6)，不是只满足某个未与275比较的模型常数。

275-C 的解析历史引理只用单位区间线性漂移、Abel 权和 \(P_\beta\)；
它对当前 \(R_\lambda\) 同样成立。因此 (6) 给 (7) 的点态包络和两个范数上界。
为了补足反向范数界，注意 (19) 的证明也一致适用于任意固定紧区间
\(z\in[z_0,2]\)、\(z_0>0\)。这里也允许实数累计端点：
将(14)先应用到其整数部分，再补最后不足一个单位区间，其额外误差为
\(O_\sigma(1)\)，仍被 \(a_Y\to\infty\) 吸收。函数
\(b\gamma(d,z)/2-z^de^{-z}\) 在 \(z=1\) 为正，故由连续性存在固定
\(z_0<1\)，使 \(H_{Y,N}(\log(Yz))\gg_\sigma a_Y\) 于 \(z\in[z_0,1]\)。
该 lag 区间固定长且对全部 \(N\ge Y\) 都在累计路径内。
由 (24) 得两个范数的反向下界，完成 (7)。

## 5. 统一共振公式：保留真实实部而非复模峰

### 引理281-C [T]

对 \(t\in[-2,-1]\)、\(z\in[1,2]\)，定义显式核
\[
 F_z(t)=\int_{-\infty}^{\log z}
             e^{dv-e^v}e^{-iv^2/2+itv}\,dv.
 \tag{27}
\]
则对全部 \(N\in[Y,2Y]\)，一致有
\[
 \boxed{\quad
 \frac{\widehat r_{Y,N}(L+t)}{a_Y L}
 =\frac12\Im\!\left[e^{i(L^2/2+tL)}F_z(t)\right]+o_\sigma(1).
 \quad}
 \tag{28}
\]
\(r_{Y,N}\) 是正源 (13) 与实际 Abel 连续源的完整中心化差异。
一致小量不要求 \(z\) 固定、不要求端点相位有极限。

证明。写 \(f_\xi(x)=w_Y(x)(\cos(\xi\log x)-1)\)。
连续替代响应与真实整数源的差由 (14)--(15) 为 \(O_\sigma(1+|\xi|)\)。
对连续部分分部积分，精确得到
\[
 \begin{aligned}
 \widehat r^{\rm sm}_{Y,N}(\xi)
 ={}&f_\xi(N)\mathcal R(N)
       -\int_1^N\mathcal R(x)w'_Y(x)(\cos(\xi\log x)-1)\,dx\\
    &+\xi\int_1^N\mathcal R(x)w_Y(x)\sin(\xi\log x)\,\frac{dx}{x}.
 \end{aligned}
 \tag{29}
\]
第一行是 \(O_\sigma(a_Y)\)，一致于全部 \(\xi,N\)，
因为其绝对值由 \(a_Y\) 乘 \(B_Y\) 的固定加权 \(L^1\) 范数控制。
这行包含真实净质量中心化与端点，不能先删除后再宣称等价。

第二行除以 \(a_Y\xi\)，在 \(u=L+v\) 坐标下为
\[
 \int_{-\infty}^{\log z}B_Y(v)
     [b+\cos((L+v)^2/2)]\sin(\xi(L+v))\,dv.
 \tag{30}
\]
由 (17)，可以一致地把 \(B_Y\) 换成 \(B\)，误差 \(o(1)\)。
慢项 \(b\) 由 (18) 为 \(O_\sigma(L^{-1})\)。
取 \(\xi=L+t\)，将乘积展开成两份正弦：共振相位为
\[
 \xi(L+v)-(L+v)^2/2=L^2/2+tL+tv-v^2/2,
 \tag{31}
\]
另一相位为
\(3L^2/2+tL+(2L+t)v+v^2/2\)。
后者把 \(B(v)e^{iv^2/2}\) 作为固定振幅，由 (18) 为
\(O_\sigma(L^{-1})\)，一致于 \(z,t\)。
这也明确处理了很负的 \(v\)：固定振幅及其导数均可积，
没有在无限负区间上误称原始相位导数一致接近 \(2L\)。
共振项恰为 (28) 的右侧主项。最后 \(\xi/L\to1\) 一致，
第一行的 \(O(a_Y)\) 和离散化 \(O(L)\) 除以 \(a_Y L\) 后趋于零，
因为 \(a_Y\to\infty\)。\(\square\)

### 引理281-D [T]：核的正下界与快速相位平均均对 cutoff 一致

有仅依赖 \(\sigma\) 的正数 \(c,C\)，使
\[
 c\le\int_{-2}^{-1}|F_z(t)|^4dt\le C\qquad(1\le z\le2).
 \tag{32}
\]
并且
\[
 \int_{-2}^{-1}
   \left|\Im[e^{i(L^2/2+tL)}F_z(t)]\right|^4dt
 =\frac38\int_{-2}^{-1}|F_z(t)|^4dt+O_\sigma(L^{-1})
 \tag{33}
\]
一致成立。

证明：(27) 对复变量 \(t\) 在半平面 \(\Im t<d\) 全纯，
因为在负无穷端可用 \(e^{(d-\Im t)v}\) 控制，所有紧集上的导数也可积。
如果某个 \(z\) 使 (32) 中的积分为零，连续性迫使 \(F_z\) 在整个
实区间 \([-2,-1]\) 为零。解析唯一性继而使其在该半平面恒为零。
对实轴应用 \(L^1\) Fourier 唯一性，这会迫使非零函数
\(\mathbf1_{v\le\log z}B(v)e^{-iv^2/2}\) 几乎处处为零，矛盾。

所以每个固定 \(z\) 的积分严格正。另一方面，(27) 对 \((z,t)\)
在紧集 \([1,2]\times[-2,-1]\) 连续，因而积分关于 \(z\) 连续。
紧性给 (32) 的统一正下界；上界直接由 \(\|B\|_1\) 给出。
这里的紧性只把已经独立证明为正的显式有限参数核取最小值，
没有用它产生任何未知算术正性。

令 \(\Theta=L^2/2+tL\)。代数恒等式为
\[
 |\Im(e^{i\Theta}F)|^4
 =\frac38|F|^4-\frac12\Re(e^{2i\Theta}F^2|F|^2)
                     +\frac18\Re(e^{4i\Theta}F^4).
 \tag{34}
\]
由 \(\int(1+|v|)B(v)dv<\infty\)，\(F_z\) 与 \(\partial_tF_z\)
在所用紧集上一致有界。对 (34) 后两项各作一次 \(t\) 分部积分，
边界及导数均一致有界，得到 (33)。
因此使用的是固定宽度的真实实部平均，不是一个长度 \(1/L\) 的复模峰窗口。
\(\square\)

## 6. 所有选择的真实响应都失败

由 (28)、(32)--(33) 和 \(L^4\) 反三角不等式，
\[
 \int_{L-2}^{L-1}|\widehat r_{Y,N}(\xi)|^4d\xi
       \asymp_\sigma a_Y^4L^4
 \tag{35}
\]
对全部 \(N\in[Y,2Y]\) 一致成立。\(\xi\asymp L\) 与 (24) 于是给
\[
 Q_{I_Y}:=\frac1{2\pi}\int_{I_Y}
                  \frac{|\widehat r_{Y,N}(\xi)|^4}{\xi^2}\,d\xi
       \asymp_\sigma M^4L^2.
 \tag{36}
\]

由固定正系数界 (13)，正原子源质量 \(A\ll_\sigma Y^{1-\sigma}\)，
而背景仍是未经修改的实际 Abel 连续源。因此277-A的一般正源比较适用：
在 \(I_Y\) 上，充分大时
\[
 |\widehat p|^2+|\widehat c|^2\asymp_\sigma S^2,
 \qquad D\asymp_\sigma S^2L,
 \qquad
 \frac{J_{4,I_Y}}{\mu^4}\asymp_\sigma\frac{Q_{I_Y}}{M^4L}.
 \tag{37}
\]
下界仍来自 \(\widehat c=B-\Re C\ge B/2\)，
不是任意系数 Bessel 估计，也不是只证明 bare 充分证书失败。
(36)--(37) 证明 (9)，而 \(J_4\ge J_{4,I_Y}\) 排除所有共尾选择。

同一模型已经满足 (6)--(7)，故275的解析低频上界
\(Q_{|\xi|\le T}\ll M^4(L+T^2)\) 仍适用。
在 \(T=L\) 时 (36) 同阶达到 \(M^4T^2\)，
所以这里没有违反已证的低频定理；失败恰发生在把其 \(T^2\) 项无条件省掉的步骤。

## 7. 一个已知真实解析结构确实排除此模型 [T/N]

### 定理281-E：系数 Dirichlet 级数不能在 \(1/2\) 附近亚纯延拓

令
\[
 \mathcal D_\lambda(s)=\sum_{n\ge2}\lambda(n)n^{-s}\qquad(\Re s>1).
 \tag{38}
\]
它可亚纯延拓到 \(\Re s>1/2\)，但不能进一步亚纯延拓到 \(1/2\) 的任何邻域。
精确地，对实数 \(q\downarrow0\)，
\[
 \boxed{\quad
 \mathcal D_\lambda(1/2+q)
 \sim\frac{3}{8q}\log\log\frac1q .
 \quad} \tag{39}
\]
特别地，它不能在该邻域等于某个非零亚纯函数的对数导数。

证明。由(13)的望远镜求和，\(\Re s>1\) 时
\[
 \mathcal D_\lambda(s)=\zeta(s)-1+
             s\int_1^\infty\mathcal R(\lfloor x\rfloor)x^{-s-1}\,dx .
 \tag{40}
\]
\(\mathcal R(1)=0\) 使下端没有额外常数。因为
\(|\mathcal R'|\le1/2\)，差
\(\mathcal R(\lfloor x\rfloor)-\mathcal R(x)\) 一致有界。
其 Mellin 积分在 \(\Re s>0\) 全纯：每个紧子集及每阶参数导数
均由 \(x^{-1-\varepsilon}(1+\log^k x)\) 控制。
连续 \(\mathcal R\) 的积分在 \(\Re s>1/2\) 绝对收敛，故(40)给出所称延拓。

令 \(u_1>e\) 足够大，使 \(u\ge u_1\) 时
\(\chi(u)=1,\ell(e^u)=\log\log u\)。把固定低段、离散化误差和
\(\zeta(s)-1\) 并入 \(s=1/2\) 附近有界的全纯项。置 \(g(u)=\log\log u\)，
\(s=1/2+q\)，剩余部分为
\[
 s\left[\frac34J(q)+I(q)\right],\quad
 J(q)=\int_{u_1}^\infty e^{-qu}g(u)\,du,\quad
 I(q)=\int_{u_1}^\infty e^{-qu}g(u)\cos(u^2/2)\,du .
 \tag{41}
\]
慢项作代换 \(v=qu,z=1/q\) 得
\[
 \frac{qJ(q)}{\log\log z}
 =\int_{u_1/z}^\infty e^{-v}
          \frac{\log\log(zv)}{\log\log z}\,dv\longrightarrow1.
 \tag{42}
\]
这是可直接核验的支配收敛：把下端之外延为零；对固定 \(v>0\) 比值趋于1，
\(v\le1\) 时它不超过1，\(v\ge1\) 且 \(z\) 充分大时不超过 \(1+\log v\)。
后者乘 \(e^{-v}\) 可积。

振荡项使用
\(\cos(u^2/2)=u^{-1}(d/du)\sin(u^2/2)\) 分部积分。
除固定下端外，其绝对值受
\[
 \int_{u_1}^\infty e^{-qu}
       \left(\frac{|g'(u)|}{u}+\frac{g(u)}{u^2}
                          +\frac{qg(u)}{u}\right)du
 \tag{43}
\]
控制。前两项可积，而
\(q e^{-qu}\le1/(eu)\) 也把第三项控制于可积的 \(g(u)/(eu^2)\)。
所以 \(I(q)=O(1)\)，一致于 \(q\downarrow0\)。
把(42)--(43)代入(41)，得到(39)。

若存在所称亚纯延拓，则 \(1/2\) 只能是可去奇点或有限阶极点。
但(39)给
\[
 q\mathcal D_\lambda(1/2+q)\to+\infty,\qquad
 q^m\mathcal D_\lambda(1/2+q)\to0\quad(m\ge2),
 \tag{44}
\]
排除全部可能。非零亚纯函数的对数导数仍为亚纯函数，故最后一句随之成立。
固定低端的任何修改只增添全纯项，不影响此障碍。\(\square\)

这里的 \(\mathcal D_\lambda\) 是**系数级数**，不是声称构造了一个以
\(\lambda(n)\) 为 Euler 系数的 zeta 函数。对于实际 \(\Lambda\)，相应级数是
\(-\zeta'/\zeta\)，其亚纯性不依赖 RH；基本恒等式与对数导数极点见
[Kedlaya 第9章，(9.1.1)及§9.2](https://kskedlaya.org/ant/chap-von-mangoldt.html)。
所以一个已知、非循环的解析性质已经排除此处反例。
但“排除这个模型”不等于“该性质足以证明真实中频上界”，后者仍须另证。
尤其不能给本模型添上“具有亚纯对数导数、Euler乘积、函数方程”的标签，
然后据它否定相应更强结构类。

## 8. 依赖、量词与下一输入

| 已保留条件 | 验证 | 尚未因此获得的性质 |
|---|---|---|
| 固定全局正整数源与一致有限截断 | (10)--(15) | 素数幂乘法结构或 \(L\) 函数实现 |
| 全局平方根级误差及 \(\Omega_\pm\) | (3)、(11)--(13) | 实际零点分布或有限高度显式公式 |
| 全部 \(Y,N\) 的大质量与指定历史 guard | (19)--(26) | 中频平滑性与双误差抵消 |
| 指数历史包络及双边范数 | (7) | 可省掉 \(T^2\) 损失的更强估计 |
| 实际连续背景、匹配端点、中心项 | (14)--(15)、(29)、(37) | 可让第三正通道自动隐藏坏频带 |

慢偏置在保持双向 \(R_\lambda\) 振荡的同时，保证全部匹配质量远离零；
chirp 的增长瞬时频率使共振跟随每个尺度，而不是只在一组可跳过的稀疏窗口出现。
若删去其中任一部分，本篇的全部 cutoff 结论均不能直接沿用。
\(d>0\) 用于负 lag 端可积和范数界；\(\beta<1/2\) 用于历史最大值的单调尺度界。
本证明不覆盖 \(\sigma=1/2\)。

量词提升仅排除：对所有满足已列正性、大小、历史和一致性条件的模型，
总能选出成功共尾数据的普遍命题。它不排除使用额外解析/算术条件的选择方法、
所有非构造性方法或真实 Riemann zeta 的路线。
实际 \(\Lambda\) 在279晚段中频的无条件相对预算仍为 [O]。
下一步必须说明新输入如何使用本模型没有的结构，而不能继续重复已被它满足的
soft norm 或记录条件。新颖性比对、论文级证明复核与一般 \(L\) 函数范围仍须单独完成。

内部独立审计：gap_exception_audit完成构造和完整证明；
主代理独立重算质量、严格guard、共振公式及全cutoff相位平均，并补定理281-E；
midband_compute独立复核281-E后又逐段反向审计落盘全文，全部通过。
实累计端点相对于整数端点的不足单位区间误差已显式补入。
本篇的统一下界来自解析证明，不依赖有限频率采样或渐近数值拟合。
内部[T/N]不等于已完成文献新颖性比对、外部同行评审或Goal的论文级阶段验收。
