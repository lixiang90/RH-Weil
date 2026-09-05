# 278. 固定正整数源的历史包络与真实中频响应障碍

日期：2026-09-06。路线：NCE-8 / B1z；论文归属：Vaughan--Brownian response。

状态：[T] 一个固定全局正整数权的构造、历史 guard 与 Fourier 峰；
[N] 历史指数包络、平方根级误差及正源一致性不能自动闭合真实中频；
[N] 同源双误差增量对小对数损失的障碍；[O] 实际 von Mangoldt 中频预算。
本篇是模型障碍，不是实际 \(\Lambda\) 的反例，也不预先宣称文献新颖性。
没有数值实验、渐近外推或新研究脚本。

## 1. 结论与准确模型范围

固定 \(0<\sigma<\beta<1/2\)、\(\delta=\beta-\sigma\)，
并把 \(\ell(x)=\max(1,\log\log\log x)\) 在小自变量处连续延伸为正的非减函数。
以下只在充分大自变量使用三重对数。

### 定理278-A [T/N]

存在一个固定的实数列 \(\lambda(n)\in[1/2,3/2]\)（\(n\ge2\)），
不是随着 \(Y\) 更换的源；存在共尾 dyadic
\(Y_j=2^{2^j}\)、共同 cutoff \(N_j=2Y_j\)，使以下性质同时成立。
记
\[
 \psi_\lambda(x)=\sum_{2\le n\le x}\lambda(n),\quad
 R_\lambda(x)=\psi_\lambda(x)-x,\quad
 P_{\beta,\lambda}(N)=\max_{1\le n\le N}\frac{|R_\lambda(n)|}{n^\beta}.
 \tag{1}
\]

首先有真正全局的误差与双向振荡
\[
 R_\lambda(x)=O(\sqrt x\,\ell(x)),\qquad
 R_\lambda(x)=\Omega_\pm(\sqrt x\,\ell(x)).
 \tag{2}
\]
使用与实际问题完全相同的 Abel 权、连续背景和中心化：
\[
 w_Y(x)=x^{-\sigma}e^{-x/Y},\quad
 \alpha_{Y,N}=\sum_{2\le n\le N}\lambda(n)w_Y(n)\delta_{\log n},
 \quad b_{Y,N}=(\log)_*(\mathbf1_{[1,N]}w_Y(x)\,dx),
 \tag{3}
\]
\[
 H_{Y,N}(u)=\sum_{2\le n\le e^u}\lambda(n)w_Y(n)
              -\int_1^{e^u}w_Y(x)\,dx,
 \quad 0\le u\le\log N,\quad M(Y,N)=H_{Y,N}(\log N).
 \tag{4}
\]
沿 \((Y_j,N_j)\)，写 \(L_j=\log Y_j\)、\(M_j=M(Y_j,N_j)\)。有
\[
 M_j\asymp_\sigma Y_j^{1/2-\sigma}\ell(Y_j)
      >Y_j^{1/2-\sigma}\sqrt{\ell(Y_j)},
 \tag{5}
\]
且实际满足 275-B 所指定的严格数值 guard：
\[
 P_{\beta,\lambda}(N_j)N_j^\delta
       <\frac12 C_{\sigma,\beta}M_j,
 \qquad
 C_{\sigma,\beta}=\frac{16e^2 2^\beta}{1-2^{-\beta}}.
 \tag{6}
\]
这里仅断言这些模型点满足该测试，不把它们说成 275 对真实 \(\Lambda\)
所执行的认证程序的输出。相应累计路径不仅有端点大值，而且有
\[
 |H_{Y_j,N_j}(u)|\ll_{\sigma,\beta}M_j e^{\delta(u-\log N_j)},
 \quad \|H_{Y_j,N_j}\|_1\asymp_{\sigma,\beta}M_j,
 \quad \|H_{Y_j,N_j}\|_2^2\asymp_{\sigma,\beta}M_j^2.
 \tag{7}
\]

然而存在固定 \(t_0>0\)，在单侧中频区间
\[
 I_j=[L_j-t_0,L_j+t_0]
 \tag{8}
\]
上，使用 269、275、277 的真实两个正通道定义 \(J_{4,I_j}\)，有
\[
 \boxed{\quad
 \frac{J_{4,I_j}}{\mu_j^4}\asymp_{\sigma,\beta}L_j\longrightarrow\infty,
 \qquad \mu_j=M_j/S_j.
 \quad}
 \tag{9}
\]
这里的量词是同一固定 \(\lambda\) 存在一条满足 (5)--(7) 的失败共尾序列。
没有证明该源的所有合格 cutoff 或所有共尾选择都失败；
不排除另选序列取得成功，也不由此否定原有的存在性任务。
\(I_j\) 最终包含在 275 的剩余频带
\(\{\sqrt{L_j}<|\xi|\le Y_j\sqrt{\log(2L_j)/L_j}\}\) 中。
因此 \(T^2\) 损失在这些带有历史指数包络的正源模型中可同阶达到，
纯包络方法不能自动从 \(\sqrt{\log Y}\) 扩展到 \(\log Y\) 并保持质量四阶预算。
本结论不把任意整数权当作素数幂权、Beurling 素数系统或具有 Euler 乘积的
\(L\) 函数；这些额外算术结构均没有由 (1)--(7) 给出。

## 2. 单一全局权的构造：没有随尺度更换数据

记
\[
 W(v)=e^{-\sigma v-e^v},\qquad
 Y_j=2^{2^j},\quad U_j=L_j=\log Y_j,\quad
 A_j=\sqrt{Y_j}\ell(Y_j),\quad a_j=A_jY_j^{-\sigma}.
 \tag{10}
\]
取一个非负、非零、偶的光滑函数
\(\phi\in C_c^\infty((-1/10,1/10))\)。把它缩放得足够小，使
\[
 \chi(v)=\frac{\phi(v+1)}{W(v)}\quad\text{满足}\quad0\le\chi\le1.
 \tag{11}
\]
另取 \(0\le f\le1\)，
\[
 f\in C_c^\infty((-3/4,-1/20)),\qquad
 f=1\quad\text{于}\quad[-13/20,-3/20].
 \tag{12}
\]
两者支撑互不相交。这些函数固定后不随 \(j\) 变化；也可选为可计算光滑函数。

从一个充分大的固定 \(j_0\) 起，定义
\[
 \mathcal R_j(x)=A_j\left[
      \chi\!\left(\log\frac{x}{Y_j}\right)
             \cos\!\left(U_j\log\frac{x}{Y_j}\right)
      +f\!\left(\log\frac{x}{Y_j}\right)\right],
 \qquad \mathcal R(x)=\sum_{j\ge j_0}\mathcal R_j(x).
 \tag{13}
\]
每块支撑在 \((e^{-11/10}Y_j,e^{-1/20}Y_j)\)，
各块互不相交且局部有限；下一块在 \(2Y_j\) 之后。
所以 \(\mathcal R\) 是 \((0,\infty)\) 上的光滑函数，且 \(\mathcal R(1)=0\)。
由于
\[
 \|\mathcal R'_j\|_\infty
 \ll_\sigma \frac{A_j(1+U_j)}{Y_j}
 =Y_j^{-1/2}\ell(Y_j)(1+L_j)\longrightarrow0,
 \tag{14}
\]
可选 \(j_0\) 使 \(|\mathcal R'|\le1/2\) 处处成立。于是固定定义
\[
 \mathfrak q(x)=1+\mathcal R'(x)\in[1/2,3/2],\qquad
 \lambda(n)=1+\mathcal R(n)-\mathcal R(n-1)
            =\int_{n-1}^n\mathfrak q(x)\,dx\in[1/2,3/2].
 \tag{15}
\]
这是一套全局权，而非先对每个 \(Y\) 独立造有限配置后再声称有一致极限。

整数端点精确满足
\[
 R_\lambda(n)=\mathcal R(n)-1.
 \tag{16}
\]
在非整数 \(x\) 处，再增加一个绝对值小于 1 的线性漂移。
块内 \(x\asymp Y_j\)、\(|\mathcal R_j|\le A_j\)，块外 \(\mathcal R=0\)，
因此得到 (2) 的全局上界。\(\phi\) 在某个内区间上有正下界，
随着 \(U_j\to\infty\)，该区间内有 \(\cos(U_jv)=1\) 与 \(-1\) 的点；
那里 \(f=0\)，而 \(\chi\) 有固定正下界。取相邻整数只改变
\(\mathcal R\) 至多 \(1/2\)，(16) 另有固定误差，故两种符号都给出
\(\Omega(A_j)\)，证明 (2)。

## 3. 离散化、Abel 质量及指定历史 guard

### 3.1 完全一致的整数化误差 [T]

对任意整数 \(N\) 及任意绝对连续函数 \(g\)，由 (15) 逐个单位区间比较，
\[
 \left|\sum_{n=2}^N\lambda(n)g(n)-\int_1^N\mathfrak q(x)g(x)\,dx\right|
 \le\frac32\sum_{n=2}^N\int_{n-1}^n\int_x^n|g'(t)|\,dt\,dx
 \le\frac32\int_1^N|g'(t)|\,dt.
 \tag{17}
\]
因此取 \(g=w_Y\) 时质量误差是 \(O_\sigma(1)\)，一致于 \(Y,N\)。
取
\(g_\xi(x)=w_Y(x)(\cos(\xi\log x)-1)\) 时，
\[
 |g'_\xi(x)|\le2|w'_Y(x)|+|\xi|w_Y(x)/x,
 \quad \int_1^\infty |w'_Y(x)|\,dx\le1,
 \quad \int_1^\infty w_Y(x)/x\,dx\le1/\sigma.
 \tag{18}
\]
故完整中心化 Fourier 误差为 \(O_\sigma(1+|\xi|)\)。
这里控制的是加权相位导数，不能用无权总变差粗界代替；
\(-1\) 中心项也已包含在 \(g_\xi\) 中。

### 3.2 当前块产生质量，所有旧块都有记账 [T]

记
\[
 c_f=-\int f(v)W'(v)\,dv>0.
 \tag{19}
\]
由于 \(-W'=(\sigma+e^v)e^{-\sigma v-e^v}\ge e^{-2}\) 于 \([-1,0]\)，
且 (12) 的平台长度为 \(1/2\)，有
\(c_f\ge e^{-2}/2\)。
在 \((Y_j,N_j)\) 处，当前块的连续加权差异质量精确为
\[
 \int w_{Y_j}(x)\mathcal R'_j(x)\,dx
 =-a_j\int W'(v)[\chi(v)\cos(U_jv)+f(v)]\,dv
 =a_j\{c_f+O_\sigma(U_j^{-2})\}.
 \tag{20}
\]
第二式使用紧支撑分部积分，没有 cutoff 边界项；最后的振荡项可作两次
分部积分。当前块完全位于 \(Y_j\) 之前。

旧块 \(k<j\) 的质量满足
\[
 \left|\int w_{Y_j}(x)\mathcal R'_k(x)\,dx\right|
 =\left|\int w'_{Y_j}(x)\mathcal R_k(x)\,dx\right|
 \ll_\sigma A_kY_k^{-\sigma}=a_k.
 \tag{21}
\]
所用的是旧块上 \(|w'_{Y_j}(x)|\ll_\sigma x^{-\sigma-1}\)，
因为这些 \(x<Y_j\)。另一方面，\(Y_j=Y_{j-1}^2\) 和 \(1/2-\sigma>0\) 保证
\[
 \sum_{k<j}a_k(1+U_k)=o(a_j),\qquad
 U_j=o(a_j).
 \tag{22}
\]
例如第一比值可由
\(j a_{j-1}(1+L_{j-1})/a_j\) 控制，其中负幂
\(Y_j^{-(1/2-\sigma)/2}\) 吸收全部对数因子。
结合 (17)、(20)--(22)，得到
\[
 M_j=c_fa_j+o(a_j),\qquad M_j\ge\frac14e^{-2}a_j>0
 \quad\text{于充分大的 }j.
 \tag{23}
\]
这证明 (5)。以后固定使用同一 \(\lambda\)，没有为调整质量再改动任何旧块。

### 3.3 全历史而非单窗口的 guard [T]

若 \(n\le N_j\) 在某块 \(k\le j\) 中，则
\(n\ge e^{-11/10}Y_k\)、\(|\mathcal R_k(n)|\le A_k\)；
块外误差仅为 \(-1\)。由于 \(A_kY_k^{-\beta}\) 随 \(k\) 增长，(16) 给
\[
 P_{\beta,\lambda}(N_j)
 \le1+e^{11\beta/10}A_jY_j^{-\beta}
 \le2e^{11\beta/10}A_jY_j^{-\beta}.
 \tag{24}
\]
于是由 (23)，
\[
 \frac{P_{\beta,\lambda}(N_j)N_j^\delta}{M_j}
 \le8e^2e^{11\beta/10}2^\delta.
 \tag{25}
\]
275-B 的常数化简后正是 (6) 中的 \(C_{\sigma,\beta}\)。两常数之比为
\[
 \frac{8e^2e^{11\beta/10}2^\delta}{C_{\sigma,\beta}}
 =\frac12e^{11\beta/10}2^{-\sigma}(1-2^{-\beta})<\frac12,
 \tag{26}
\]
因为 \(\beta<1/2\)、\(e^{11/20}<2\)、\(1-2^{-\beta}<1/2\)。
因此得到了指定严格 guard 的固定余量，非仅某个未比较的模型常数。

275-C 的证明只用单位区间漂移、历史最大值和正 Abel 权，
故对 (16) 逐字成立；由 (6) 得到 (7) 的点态包络及两个范数上界。
为了证明双边范数，在 \(u\in[L_j,L_j+\log2]\) 上，所有 \(k\le j\) 的
连续块已经结束，且下一块尚未进入，因此连续累计差异恒等于其端点质量。
(17) 以及实 cutoff 的不足一个单位区间误差给
\(H_{Y_j,N_j}(u)=M_j+O_\sigma(1)\) 一致成立。
这个固定长度区间提供 (7) 两个范数的反向下界。

## 4. 在真正未控中频构造 Fourier 峰

记 \(r_j\) 为 (3) 的带符号差异对称化并减去 \(M_j\delta_0\) 所得中心化测度。
它与 277 中 \(r=p+c\) 的定义完全相同。连续替代 \(\mathfrak q\) 的符号为
\[
 \widehat r^{\,\mathrm{sm}}_j(\xi)
 =\int_1^{N_j}w_{Y_j}(x)(\cos(\xi\log x)-1)\mathcal R'(x)\,dx,
 \quad
 \widehat r_j(\xi)=\widehat r^{\,\mathrm{sm}}_j(\xi)+O_\sigma(1+|\xi|).
 \tag{27}
\]
由 (17)--(18)，该公式保留全部离散化、连续项、中心项与匹配端点。
每个旧块在 (27) 中的贡献绝对值至多
\[
 2\int w_{Y_j}(x)|\mathcal R'_k(x)|\,dx
 \ll_\sigma a_k(1+U_k).
 \tag{28}
\]
故所有旧块的 Fourier 贡献是 \(o(a_j)\)，不是仅其总质量很小。

写 \(Y=Y_j,L=L_j,U=U_j,a=a_j\)，并置
\(F_j(v)=\chi(v)\cos(Uv)+f(v)\)。当前块分部积分精确给
\[
 \begin{aligned}
 \widehat r^{\,\mathrm{cur}}_j(\xi)
 ={}&-a\int F_j(v)W'(v)[\cos(\xi(L+v))-1]\,dv\\
    &+a\xi\int F_j(v)W(v)\sin(\xi(L+v))\,dv.
 \end{aligned}
 \tag{29}
\]
第一行一致为 \(O_\sigma(a)\)。第二行中 \(fW\) 光滑紧支撑，
一次分部积分给 \(O_\sigma(a)\)。只剩 \(W\chi=\phi(v+1)\) 的振荡主项。

令
\[
 \Phi(t)=\int\phi(s)\cos(ts)\,ds.
 \tag{30}
\]
这是实偶函数。因 \(\Phi(0)>0\)，可固定 \(0<t_0<1\)，使
\(\Phi(t)\ge\Phi(0)/2\) 于 \(|t|\le t_0\)。对 \(\xi=U+t\)，三角恒等式给
\[
 \begin{aligned}
 &\int \phi(v+1)\cos(Uv)\sin(\xi(L+v))\,dv\\
 &\quad=\frac12\Phi(t)\sin(UL+t(L-1))
       +\frac12\Phi(2U+t)\sin(\xi L-(2U+t)).
 \end{aligned}
 \tag{31}
\]
\(\Phi(2U+t)=O(U^{-2})\) 一致成立。使用 (22)、(27)--(31)，
对全部 \(|t|\le t_0\) 得最终、真实整数源的公式
\[
 \boxed{\quad
 \widehat r_j(U_j+t)
 =\frac{a_j(U_j+t)}2\Phi(t)
          \sin(U_jL_j+t(L_j-1))+O_\sigma(a_j).
 \quad}
 \tag{32}
\]
整数化的 \(O(1+U_j)\) 已由 \(U_j=o(a_j)\) 吸收。

不能仅在一个频点声称该正弦因子有下界。实际使用的是固定宽度积分：
\[
 \int_{-t_0}^{t_0}\sin^4(U_jL_j+t(L_j-1))\,dt
 =\frac34t_0+O(L_j^{-1})\gg1.
 \tag{33}
\]
这是将 \(\sin^4 z=(3-4\cos2z+\cos4z)/8\) 逐项积分所得，
对相位 \(U_jL_j\) 完全一致。由 \(L^4\) 反三角不等式及 (32)，
\[
 \int_{I_j}|\widehat r_j(\xi)|^4\,d\xi\asymp_\sigma a_j^4U_j^4,
 \qquad
 Q_{I_j}:=\frac1{2\pi}\int_{I_j}\frac{|\widehat r_j(\xi)|^4}{\xi^2}\,d\xi
       \asymp_\sigma M_j^4U_j^2.
 \tag{34}
\]
上下界都属于有限源的连续频率积分，不是有限采样或纯数值峰。

## 5. 真实正通道和双误差对象均不能消除该模型峰

### 5.1 实际物理响应的下界 [T/N]

(15) 给 \(A=\alpha_{Y_j,N_j}(\mathbb R)\ll_\sigma Y_j^{1-\sigma}\)；
更精确地，\(A=B+M_j\)、\(M_j=o(B)\)、\(B\asymp_\sigma Y_j^{1-\sigma}\)。
故满足 [277-A](277-continuum-channel-coercivity-and-double-discrepancy-interface.md)
的一般正源假设。因为 \(I_j\) 最终全部位于固定 \(K_\sigma\) 以上，
该定理给
\[
 |\widehat p_j|^2+|\widehat c_j|^2\asymp_\sigma S_j^2,
 \quad D_j\asymp_\sigma S_j^2L_j,
 \quad
 \frac{J_{4,I_j}}{\mu_j^4}\asymp_\sigma\frac{Q_{I_j}}{M_j^4L_j}.
 \tag{35}
\]
其下界来自实际连续 Abel 方向
\(\widehat c_j=B-\Re C_j\ge B/2\)，不是由任意系数 Bessel 界提供。
将 (34) 及 \(U_j=L_j\) 代入 (35)，得到 (9)。

同时 275-(27) 对本模型的路径适用，给
\(Q_{\{|\xi|\le T\}}\ll M_j^4(L_j+T^2)\)。在 \(T=U_j+t_0\) 时，
(34) 给同阶反向下界 \(\gg M_j^4U_j^2\)。因此这里确实达到了该
\(T^2\) 项的规模，而不是只发现一个弱于原上界的模型异常。

### 推论278-B [T/N]：同源双误差增量的有限损失障碍

令 \(G_j\) 为 (4) 的奇延拓，再在 \([-\log N_j,\log N_j]\) 外置零，
并令 \(q_j=G_j*G_j\)。记
\[
 W_j^*=\log(2L_j),\quad
 T_j^*=Y_j\sqrt{W_j^*/L_j},\quad h_j^*=(T_j^*)^{-1},
 \qquad \Delta_h q(u)=q(u+h)-q(u).
 \tag{36}
\]
则在同一个固定源、同一 schedule 上有
\[
 \boxed{\quad
 \|\Delta_{h_j^*}q_j\|_2^2
       \gg_\sigma (h_j^*)^2M_j^4L_j^2.
 \quad}
 \tag{37}
\]
所以不能单由这些模型假设推出
\(\|\Delta_{h_j^*}q_j\|_2^2=O((h_j^*)^2M_j^4L_j^A)\)
的任意固定 \(A<2\)。本推论不排除 \(A\ge2\)，不能说成排除任意对数损失。

证明：保留精确端点恒等式
\[
 \widehat r_j(\xi)=M_j(\cos(\xi\log N_j)-1)+\xi S_j^H(\xi),
 \quad S_j^H(\xi)=\int_0^{\log N_j}H_{Y_j,N_j}(u)\sin(\xi u)\,du,
 \quad\widehat G_j=-2iS_j^H.
 \tag{38}
\]
在 (32) 中除以 \(\xi\)，端点项仅产生 \(O(M_j/U_j)=O(a_j/U_j)\)
的误差。因此与 (33) 相同的论证给
\[
 \int_{I_j}|\widehat G_j(\xi)|^4\,d\xi\gg_\sigma M_j^4.
 \tag{39}
\]
由于 \(h_j^*U_j\to0\)，在 \(I_j\) 上
\(|e^{ih_j^*\xi}-1|\gg h_j^*U_j\)。Plancherel、
\(\widehat q_j=\widehat G_j^2\) 及保留该频带给
\[
 \|\Delta_{h_j^*}q_j\|_2^2
 =\frac1{2\pi}\int_{\mathbb R}|e^{ih_j^*\xi}-1|^2|\widehat G_j(\xi)|^4\,d\xi
 \gg_\sigma (h_j^*)^2U_j^2M_j^4,
 \tag{40}
\]
即 (37)。所有卷积都是有限 cutoff 下的 \(L^1\cap L^2\) 函数，
没有无限能量或未记账的零延拓端点。\(\square\)

此处的坏频率是 \(U_j=\log Y_j\)，不是 \(T_j^*\) 附近的最高频壳。
全局增量在很小的 \(h_j^*\) 处仍测到较低频率，故不能由 (37) 宣称最高壳失败。
对实际 \(\Lambda\)，274 的固定倍数高频尾已经闭合该最高壳；
本模型既不能继承未经核验的算术高频定理，也不与它矛盾。

## 6. 依赖、删除审计和研究停止边界

本构造全部由显式光滑拼接、单位区间离散化、分部积分及 Plancherel 证明。
历史包络调用 275-C 的解析引理；真实方向比较调用 277-A 的一般正源定理。
没有调用实际零点假设或外部未证明的算术相关估计。

| 保留的结构 | 本构造中的验证 | 不能因此增加的结构 |
|---|---|---|
| 单一固定正整数源 | (13)--(16)，所有尺度使用同一 \(\lambda(n)\) | 实际素数幂支撑、Euler 乘积或 Beurling 素数公理 |
| 比定性 PNT 更强的全局误差与振荡 | (2) 的 \(O\) 及 \(\Omega_\pm\) 均已证明 | 实际 \(\Lambda\) 的短区间/乘积四点抵消 |
| 指定历史 guard 和大质量 | (23)--(26)，含275预定常数比较 | 真实认证算法输出等于本模型点 |
| 指数路径包络及两种 soft norm | (7)，并有双边量级 | 高频导数、局部增量或双误差预算 |
| 实际连续 Abel 正背景 | (3)、(35) | 可以靠第三正通道隐藏中频峰 |
| 匹配 cutoff、完整中心化 | (17)--(18)、(27)、(38) | 删除 \(-M\)、连续端点或零延拓跳跃 |

若删去当前块的振荡部分，(32) 的增长频率峰不再由本证明产生；
若删去慢 bump，净质量可能太小而不能保留 guard；
若不采用足够稀疏的固定块，(22) 的旧块误差必须重新估计；
若去掉连续 Abel 方向，则 (34) 不再自动给真实响应的双边比较。
这些是具体使用位置，而不是对所有替代模型的分类定理。

本结果比 275-D 更强：它保留历史 guard、指数路径包络、大质量、固定全局源，
且直接否定该模型上的真实中频预算；不是只否定一个单误差充分证书。
它仍然不是 Riemann zeta 的反例，也不提供任何零点比例或 RH/GRH 结论。
本篇不宣称 \(\lambda\) 定义了广义素数系统；更强乘法模型中的已知反例与
本文专门的 response/guard 障碍有何关系，属于待完成的文献新颖性比对 [O]。
例如初步检索发现 Broucke--Debruyne--Vindas 的
[Beurling integers with RH and large oscillation](https://arxiv.org/abs/2004.11501)
（[正式出版记录](https://doi.org/10.1016/j.aim.2020.107240)）。
本轮只核验其摘要与书目信息，研究对象和待估计余项不同；
不将该文的结论直接套用到本模型，也没有完成优先权比对。

下一最小输入 [O] 必须使用本模型未保留的实际算术限制，在真正未闭合的增长中频
（如 \(|\xi|\asymp\log Y\)）控制两份误差的相互作用。
仅重复已经由本模型满足的历史包络、soft norm、全局误差上界及固定源一致性条件，
不能普遍推出该预算。这里没有排除任意更强的算术输入、所有非构造性方法或所有
选择路线；排除的只是由已列这些性质对每条合格数据作普遍蕴含的推理。
内部独立复核：carrier_audit 另行重建固定全局源、加权离散化、严格guard和实部峰；
midband_compute 完整逐段复核本篇及277-A，特别核对旧块总变差、固定宽度相位平均、
双误差增量和选择量词；主代理独立复核(1)--(40)及最终修订。三份复核均通过。
这些是内部证明审计，不替代文献新颖性比对或外部同行评审；论文级晋级仍未完成。
