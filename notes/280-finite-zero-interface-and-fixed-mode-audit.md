# 280. 晚段的有限零点接口与固定模式删除审计

日期：2026-09-06。路线：NCE-8 / B1z；论文归属：Vaughan--Brownian response。

状态：[T/R] 锐截断晚段的有限高度显式公式与独立统一余项；
[T] 固定有限零点模式的相对删除；[O] 剩余有限零点和的四阶算术预算。
本篇只作为[279](279-record-controlled-arithmetic-prefix-deletion.md)晚段局部化的附属接口，不另开零点侧主线。
双向换表示不计作新的算术 saving，也不证明 RH、GRH 或零点比例结论。

## 1. 对象、端点与外部输入

固定 \(0<\sigma<\beta<1/2\)，令
\[
 L=\log Y,\qquad \ell(Y)=\max(1,\log\log\log Y),\qquad
 Y\le N\le2Y,
 \quad w_Y(x)=x^{-\sigma}e^{-x/Y}.
 \tag{1}
\]
仅在充分大 \(Y\) 使用三重对数；275 中 \(N\) 为整数，以下显式公式也允许
实数 \(N\)。令 \(2\le K<N\)，晚段恰为 \((K,N]\)，不把下端点改成闭区间。
定义
\[
 M_H=\sum_{K<n\le N}\Lambda(n)w_Y(n)-\int_K^N w_Y(x)\,dx,
 \qquad f_\xi(x)=w_Y(x)(\cos(\xi\log x)-1),
 \tag{2}
\]
\[
 \widehat r_H(\xi)=\sum_{K<n\le N}\Lambda(n)f_\xi(n)-\int_K^N f_\xi(x)\,dx.
 \tag{3}
\]
这里 \(r_H\) 是晚段的带符号 lag 源对称化后减去 \(M_H\delta_0\) 所得的
真实中心化误差；\(-1\) 不能删除。
记完整匹配源的净质量为 \(M=M(Y,N)\)。应用时沿275的新序列，
\[
 |M|>Y^{1/2-\sigma}\sqrt{\ell(Y)}.
 \tag{4}
\]
279 的晚段局部化另外提供所需选择下的 \(M_H/M\to1\) 及早段相对删除。
下面有限公式本身不需要历史 guard，也不假设 (4)。

外部输入 [R] 是作者本人公开书稿的
[Kedlaya，*Analytic Number Theory*，第9章，定理9.9](https://kskedlaya.org/ant/chap-von-mangoldt.html)。
其第9.1节采用半权函数
\[
 \psi_0(x)=\sum_{n<x}\Lambda(n)+\tfrac12\Lambda(x),
 \tag{5}
\]
其中对非整数或非素数幂的实数 \(x\)，规定 \(\Lambda(x)=0\)。
对 \(x\ge2,V\ge2\)，该定理给
\[
 \psi_0(x)-x
 =-\sum_{|\Im\rho|<V}\frac{x^\rho}{\rho}
   -\frac{\zeta'(0)}{\zeta(0)}-\frac12\log(1-x^{-2})+E_0(x,V),
 \tag{6}
\]
\[
 E_0(x,V)\ll
 \frac{x\log^2(xV)}V
 +\log x\min\!\left(1,\frac{x}{V\langle x\rangle}\right).
 \tag{7}
\]
\(\langle x\rangle\) 指最近的其他素数幂与 \(x\) 的距离：若 \(x\) 本身为
素数幂，排除其自身。零点按重数计。书稿证明中用有界高度移动避开零点，
再将改变的有限零点项吸收到余项，所以 (6)--(7) 不另要求用户挑选“好高度”。
本篇保守地使用 (7) 的第二项不超过 \(\log x\)，不需要任何素数间距假设。
全部 \(\Re\rho\) 均保留为实际值，未替换成 \(1/2\)。

## 2. 两个锐端点均保留的有限公式 [T/R]

### 定理280-A

定义整个复平面上均合法的有限区间核
\[
 \mathcal K_{Y;K,N}(s)=\int_K^N x^{s-\sigma-1}e^{-x/Y}\,dx,
 \tag{8}
\]
及有限零点和
\[
 Z_V(\xi)=-\sum_{|\Im\rho|<V}
 \left\{\frac{\mathcal K_{Y;K,N}(\rho+i\xi)+
                    \mathcal K_{Y;K,N}(\rho-i\xi)}2
                  -\mathcal K_{Y;K,N}(\rho)\right\}.
 \tag{9}
\]
则对全部实数 \(\xi\) 有
\[
 \boxed{\quad
 \begin{aligned}
 \widehat r_H(\xi)={}&Z_V(\xi)
  -\int_K^N\frac{f_\xi(x)}{x(x^2-1)}\,dx\\
 &+\tfrac12\Lambda(N)f_\xi(N)-\tfrac12\Lambda(K)f_\xi(K)
  +\mathcal E_V(\xi),
 \end{aligned}
 \quad}
 \tag{10}
\]
其中余项既有精确表达，也有统一界：
\[
 \mathcal E_V(\xi)=f_\xi(N)E_0(N,V)-f_\xi(K)E_0(K,V)
                       -\int_K^N E_0(x,V)f'_\xi(x)\,dx,
 \tag{11}
\]
\[
 \boxed{\quad
 |\mathcal E_V(\xi)|\ll_\sigma(1+|\xi|)
 \left\{\frac{Y^{1-\sigma}\log^2(2YV)}V+K^{-\sigma}L\right\}.
 \quad}
 \tag{12}
\]
两个半权端点与平凡零点积分合起来的绝对值为 \(O_\sigma(K^{-\sigma}L)\)，
故 (12) 也控制 \(\widehat r_H-Z_V\)，只需改变隐常数。

证明。令右连续 \(R(x)=\psi(x)-x\)。Stieltjes 分部积分精确给
\[
 \widehat r_H(\xi)=f_\xi(N)R(N)-f_\xi(K)R(K)
                       -\int_K^N R(x)f'_\xi(x)\,dx.
 \tag{13}
\]
在普通积分中 \(\psi\) 与 \(\psi_0\) 几乎处处相同；两个端点却分别相差
\(\Lambda(N)/2\) 和 \(\Lambda(K)/2\)。把 (6) 代入 (13)，
常数 \(-\zeta'(0)/\zeta(0)\) 在端点与积分间恰好抵消。
每个非平凡零点项的导数为 \(-x^{\rho-1}\)，
平凡零点项的导数为 \(-1/[x(x^2-1)]\)，得到 (9)--(11)。
特别地，下端半权带负号，符合排除 \(K\) 而包含 \(N\) 的约定。

为了估计余项，使用
\[
 |f_\xi(x)|\le2w_Y(x),\qquad
 |f'_\xi(x)|\le2|w'_Y(x)|+|\xi|w_Y(x)/x.
 \tag{14}
\]
由于 \(N\le2Y\)，有
\[
 N|f_\xi(N)|+K|f_\xi(K)|+\int_K^N x|f'_\xi(x)|\,dx
       \ll_\sigma(1+|\xi|)Y^{1-\sigma},
 \tag{15}
\]
\[
 |f_\xi(N)|+|f_\xi(K)|+\int_K^N|f'_\xi(x)|\,dx
       \ll_\sigma(1+|\xi|)K^{-\sigma}.
 \tag{16}
\]
例如 \(\int_0^\infty w_Y(x)dx=\Gamma(1-\sigma)Y^{1-\sigma}\)，
\(\int_K^N w_Y(x)dx/x\le K^{-\sigma}/\sigma\)，
且 \(w_Y\) 正而递减，足以逐项证明这两式。
在 (7) 第一项中统一放大 \(\log(xV)\le\log(2YV)\)，
在第二项中用 \(\log x\ll L\)，由 (15)--(16) 即得 (12)。

最后，\(|\Lambda(t)|\le\log t\) 给两个端点的
\(O_\sigma(K^{-\sigma}L)\) 上界；平凡零点积分由
\(K\ge2\) 给 \(O_\sigma(K^{-\sigma-2})\)。
所有公式在 \(\xi=0\) 恰为零；所给上界无需在零频取得最佳消失阶。\(\square\)

## 3. 物理频率与零点高度分别记账 [T]

### 推论280-B：独立小余项的有限高度接口

固定 \(A>1/2\)、\(h>0\)，采用 279 的晚段形状
\[
 K=\lfloor N/L^h\rfloor,\qquad T=L^A,\qquad
 \mathcal B_Y=\{\sqrt L\le|\xi|\le T\},\qquad
 V=\sqrt Y\,L^{A+2}.
 \tag{17}
\]
\(T\) 是物理频率上限，\(V\) 是零点截断高度，两者不能混同。
沿 (4) 的同一真实序列，定义
\[
 Q_E[z]=\frac1{2\pi}\int_E\frac{|\widehat z(\xi)|^4}{\xi^2}\,d\xi,
 \qquad
 Q_E[Z_V]=\frac1{2\pi}\int_E\frac{|Z_V(\xi)|^4}{\xi^2}\,d\xi.
 \tag{18}
\]
则
\[
 \frac1{2\pi}\int_{\mathcal B_Y}
       \frac{|\widehat r_H(\xi)-Z_V(\xi)|^4}{\xi^2}\,d\xi
 \ll_{\sigma,A,h}\frac{M^4}{\ell(Y)^2\sqrt L}
 =o(M^4L).
 \tag{19}
\]
因而
\[
 \boxed{\quad
 Q_{\mathcal B_Y}[r_H]=O(M^4L)
 \quad\Longleftrightarrow\quad
 Q_{\mathcal B_Y}[Z_V]=O(M^4L).
 \quad}
 \tag{20}
\]
当 279 已给 \(M_H/M\to1\) 时，右侧目标中的 \(M\) 也可换成 \(M_H\)，
无需再次假设晚段质量与完整质量可比。

证明：此时 \(\log(2YV)\ll_A L\)，故 (12) 及已记账的其他项给
\[
 \sup_{\xi\in\mathcal B_Y}|\widehat r_H(\xi)-Z_V(\xi)|
 \ll_{\sigma,A,h}
 Y^{1/2-\sigma}+Y^{-\sigma}L^{h\sigma+A+1}
 \ll_{\sigma,A,h}Y^{1/2-\sigma}
 \le\frac{|M|}{\sqrt{\ell(Y)}}.
 \tag{21}
\]
最后一个不等式只使用 (4)。固定的所有对数幂都被 \(Y^{1/2}\) 吸收。
而 \(\int_{\mathcal B_Y}\xi^{-2}d\xi\le2L^{-1/2}\)，得到 (19)。
在测度 \(d\xi/(2\pi\xi^2)\) 上对四次方根用 Minkowski，得到 (20)。
这里没有用 \(\xi=0\) 附近的粗余项去积分一个发散 majorant。\(\square\)

独立零点计数 \(N(V)=O(V\log V)\) 使 (9) 的项数为
\(O_A(\sqrt Y\,L^{A+3})\)；这是有限对象，不是含糊的无限零点和。
该计数可核验于同一作者书稿第9章 Lemma9.4、Remark9.7。
但有限项数变少没有证明四阶有符号相关界；(20) 只是保留真实端点、
真实实部和独立小误差后的等价接口，不能单独晋级成新 saving。

特别地，单位高度的 \(O(\log V)\) 零点计数不控制
\(x^{\Re\rho-\sigma}\) 的大小。把它一律改为
\(x^{1/2-\sigma}\) 会直接加入本任务未证明的零点位置假设。
本篇也不把现代较好余项在有限 \(V,x\) 范围内的定理，未经检查地用于整个 Abel 积分。

## 4. 固定有限零点模式可相对删除，而非固定模板障碍 [T]

### 定理280-C

令 \(\mathcal Z_0\) 为任意固定有限、共轭封闭的非平凡零点多重集合，
且其中每个零点满足 \(\Re\rho\le1/2\)。这里这是对所选有限集合的明确假设，
不是对所有零点或任意增长集合的结论，也不认证某个首零点的数值或重数。

在完整区间 \([1,N]\) 定义实带符号源
\[
 d\nu_{\mathcal Z_0}(x)
   =-\sum_{\rho\in\mathcal Z_0}x^{\rho-1}w_Y(x)\,dx.
 \tag{22}
\]
将它推前到 lag 轴、对称化，再减去其总质量乘 \(\delta_0\)，记为
\(r_{\mathcal Z_0}\)。若先将 (22) 限制到 \((K,N]\) 再作同样中心化，
记为 \(r_{\mathcal Z_0,H}\)。对这两个对象均有
\[
 \|\nu_{\mathcal Z_0}\|_{\rm TV}
       \ll_{\sigma,\mathcal Z_0}Y^{1/2-\sigma},\qquad
 \|r_{\mathcal Z_0}\|_{\rm TV}
       \ll_{\sigma,\mathcal Z_0}Y^{1/2-\sigma},
 \tag{23}
\]
\[
 \boxed{\quad
 Q_{\mathbb R}[r_{\mathcal Z_0}],\qquad
 Q_{\mathbb R}[r_{\mathcal Z_0,H}]
       \ll_{\sigma,\mathcal Z_0}Y^{2-4\sigma}L
       =o(M^4L)
 \quad\text{沿 (4)。}\quad}
 \tag{24}
\]
在 (23) 第一式中，对晚段应用时将 \(\nu\) 理解为其限制，所给上界不变。

证明：记 \(d_0=1/2-\sigma>0\)、\(m=|\mathcal Z_0|\)，按重数计。
由 \(x\ge1\) 和 \(\Re\rho\le1/2\)，
\[
 \|\nu_{\mathcal Z_0}\|_{\rm TV}
 \le\sum_{\rho\in\mathcal Z_0}\int_1^N x^{\Re\rho-\sigma-1}e^{-x/Y}\,dx
 \le m\int_0^\infty x^{d_0-1}e^{-x/Y}\,dx
 =m\Gamma(d_0)Y^{d_0}.
 \tag{25}
\]
限制源不会增大总变差；lag 推前与对称化也不会增大它，
减去中心质量至多再增加一倍，得 (23)。
所有这些中心化测度总质量为零、支撑在 \([-\tau,\tau]\)，
\(\tau=\log N\asymp L\)。因此 \(r_{\mathcal Z_0}*r_{\mathcal Z_0}\)
的总质量为零，支撑在 \([-2\tau,2\tau]\)，且其 primitive 满足
\[
 \|F_{r_{\mathcal Z_0}*r_{\mathcal Z_0}}\|_\infty
 \le\|r_{\mathcal Z_0}\|_{\rm TV}^2.
 \tag{26}
\]
该 primitive 在上述支撑区间外为零。由有限测度 primitive 的 Plancherel 恒等式，
\[
 Q_{\mathbb R}[r_{\mathcal Z_0}]
 =\|F_{r_{\mathcal Z_0}*r_{\mathcal Z_0}}\|_2^2
 \le4\tau\|r_{\mathcal Z_0}\|_{\rm TV}^4
 \ll_{\sigma,\mathcal Z_0}Y^{4d_0}L.
 \tag{27}
\]
晚段同理。由 (4)，\(M^4>Y^{4d_0}\ell(Y)^2\)，
所以 (27) 除以 \(M^4L\) 是 \(O_{\sigma,\mathcal Z_0}(\ell(Y)^{-2})=o(1)\)。
\(\square\)

### 4.1 接回真实响应时保持物理正通道不变

对完整实际源的 \(p,c,S,D,M\) 固定不动，定义任意中心化误差 \(z\) 的响应泛函
\[
 \mathfrak J_E[z]=\frac1{S^4D}\frac1{2\pi}\int_E
    \frac{|\widehat z|^4(|\widehat p|^2+|\widehat c|^2)}{\xi^2}\,d\xi.
 \tag{28}
\]
因此 \(\mathfrak J_E[r]\) 正是原真实响应的该频带贡献。
由已证 \(|\widehat p|^2+|\widehat c|^2\le4S^2\)、\(D\asymp S^2L\)，
及 (24)，
\[
 \mathfrak J_E[r_{\mathcal Z_0}]
 \ll\frac{Q_{\mathbb R}[r_{\mathcal Z_0}]}{S^4L}
 =o(\mu^4),\qquad \mu=M/S.
 \tag{29}
\]
故对同一非负加权测度用 \(L^4\) Minkowski，
\[
 \left|\mathfrak J_E[r]^{1/4}
       -\mathfrak J_E[r-r_{\mathcal Z_0}]^{1/4}\right|=o(|\mu|).
 \tag{30}
\]
同理，以 \(r_H,r_{\mathcal Z_0,H}\) 替换两份误差，晚段也成立。
因此从完整或晚段 discrepancy 中删除所选固定模式，不改变相应
\(O(\mu^4)\) 预算的真假。对 bare \(Q_E\) 的 \(O(M^4L)\) 预算，
同一结论直接由 (24) 和未乘物理通道的 Minkowski 得到。

这里保持原实际正通道和分母，不声称删除零点模式后已构造另一套正源配置。
即使同时记下删除模式后的净质量，其变化也至多
\(\|\nu_{\mathcal Z_0}\|_{\rm TV}=O(|M|/\sqrt\ell)=o(|M|)\)；
对 279 已有 \(M_H/M\to1\) 的晚段也一样。
所以不会暗中用一个不再可比的新质量归一化。

### 4.2 固定与增长集合不能混淆

(24) 的隐常数允许依赖所选固定集合，但不允许它随 \(Y\) 增长。
本篇不删除全部零点、不删除任意增长高度的集合，也不声称已经排除离线零点。
对一个假设位于中心线的固定首零点对、或任何满足(22)--(25)大小约束的固定有限模式，
上述贡献最终相对可忽略；有限窗口中的大响应不能据此升级成最终渐近障碍。
如果人为使模板系数随 \(Y\) 放大，也已超出本定理的固定模式假设。

## 5. 依赖、循环性与停止边界

- 独立输入：(6)--(7) 是已核验的截断显式公式；(4) 来自275，
  早晚段质量关系由279单独负责。没有从有限公式产生缺失的正性。
- 锐截断：两个半权端点、平凡零点积分及总质量中心项全部保留。
  对非整数 \(K\)，半权项依约为零，而不是把 \(K\) 静默取整。
- 固定模式：唯一的零点位置假设只作用于指定 \(\mathcal Z_0\)，
  不用于有限高度和 (9) 中的其他零点。
- 量词：(20) 沿同一实际选定序列和同一物理频带成立；
  不证明所有 cutoff 满足预算，也不改变279的存在性选择问题。
- 晋级边界：新增有限零点和估计、实际乘法相关估计或可严格缩小该输入的定理，
  才是下一步；仅重复 (20) 不算进展。

本篇的固定模式删除是一个独立完成的小结论；有限高度接口提供明确可检验的余项，
但还没有解除剩余四阶算术难题。新颖性、论文级独立审计及一般 \(L\) 函数推广仍开放。

## 6. 有限实验 [E]

主代理独立运行
`python -B scripts/first_zero_midband_template_probe.py`，用 NumPy 2.5.2、
SciPy 1.18.1、mpmath 1.3.0，耗时约6.8秒。该可选探索脚本需要 SciPy，
不加入标准 CI，不写输出文件，也不更新 PDF。

固定 \(\sigma=1/4\)，用 MP50 的 `zetazero(1)` 数值虚部
\(\gamma_1=14.1347251417\ldots\) 定义一个**预先指定、未经拟合的模板参数**：
\[
 z_1(\xi)=-2\int_1^N x^{-\sigma-1/2}e^{-x/Y}
             \cos(\gamma_1\log x)(\cos(\xi\log x)-1)\,dx .
 \tag{31}
\]
这不是零点认证程序，也不是使用(10)后已控制了其他零点的余项。
记反射对称的 \(E=\{L\le|\xi|\le2L\}\)、
\(Z=\{\gamma_1-1.5\le|\xi|\le\gamma_1+1.5\}\)。
分割端点后分别积分 \(E\cap Z,E\setminus Z,Z\)，不重复计数交集。
正频半轴使用 \(1/\pi\)，与完整 \(1/(2\pi)\) 约定一致。

以下各 \(N\) 为271候选集的浮点窗口质量最大者，**不是275的新认证记录点**：

| \(Y\) | \(N\) | \(J_{4,E}/\mu^4\) | \(J_{4,E\setminus Z}/\mu^4\) | \(E\cap Z\)占\(E\)真实响应比例 |
|---:|---:|---:|---:|---:|
| 256 | 346 | 0.0359473 | 0.0359473 | 0 |
| 1024 | 1422 | 0.159672 | 0.0384469 | 75.9213% |
| 4096 | 5380 | 1.89864 | 0.0230868 | 98.7840% |
| 16384 | 19372 | 1.02462 | 0.0184703 | 98.1974% |

另复算每个 \(Y\) 的 \(N=Y,2Y\)，合计12个配置；全部未达到(4)。
分母效应尤其清楚：\(Y=16384,N=Y\) 的 bare \(Q_E=420.921690\)，
而浮点质量最大者的 \(Q_E=421.203320\)，原始能量几乎相同；
但两者 \(J_{4,E}/\mu^4\) 分别约 \(376640.1\) 与 \(1.02462\)。
不能将前一个大比值描述为同等幅度的实际谱能量爆发。

还令 \(v=\widehat r-z_1\)，在**原实际通道权**
\((|\widehat p|^2+|\widehat c|^2)/(\pi\xi^2)\) 下保留五个有符号项
\[
 z_1^4,\quad4z_1^3v,\quad6z_1^2v^2,\quad4z_1v^3,\quad v^4.
 \tag{32}
\]
\(Y=16384,N=19372\) 的 \(Z\) 带中，五项除以完整响应分子约为
\[
 1.1183073,\quad-0.2521898,\quad0.1309379,\quad
 0.00004668,\quad0.00289787 .
\]
它们合计为1。仅用两份四阶范数的 Hölder/Minkowski 上界则约为完整分子的
2.52340倍；保留符号有影响，但本实验没有证明一致的算术交叉 saving。
此分解也不是 Vaughan Type I/II 分解，更不是普通 Bessel 定理的替代输入。

核验细节：

- 全部五项合计与独立累计的 \(\widehat r^4\) 分子相对误差最多
  \(3.695\cdot10^{-16}\)。
- 连续 lag 的10/18阶、物理频率的8/12阶复合 Gauss 比较最大误差
  \(2.319\cdot10^{-13}\)；这不是区间积分证书。
- 用独立复不完全 Gamma 公式作MP50模板及连续项采样校验，
  最大缩放误差分别 \(4.361\cdot10^{-14}\)、\(1.731\cdot10^{-15}\)；
  最小浮点最大者另用独立试除素数幂账本复算真实响应，
  最大缩放误差 \(3.942\cdot10^{-15}\)。

解释边界：固定的 \(Z\) 与移动的 \(E=[L,2L]\)（正半轴）仅在
\((\gamma_1-1.5)/2\le L\le\gamma_1+1.5\) 时可能相交；
\(L\to\infty\) 后它必然离开。因此上表不能证明渐近的“首零点主导中频”。
定理280-C也已说明，若所选固定模式确实满足其有限实部条件，
则沿理论大质量序列其完整相对贡献最终消失。
真正的下一输入仍是279尾部实际算术四阶预算，或增长零点集的统一有符号相关。

内部独立审计：gap_exception_audit重建(10)--(30)完整证明；
主代理完整读取外部定理和本篇证明、独立运行上述脚本；
midband_compute另行逐式逆向复核，并独立核验Kedlaya原章的半权定义、
任意高度余项及有限模式的primitive恒等式，证明通过。
两份审计一致要求将(17)写成整数floor截断、限制§4.2模板范围，现已落实。
这里的内部复核不等于外部同行评审或文献新颖性结论。
