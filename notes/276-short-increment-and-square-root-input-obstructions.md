# 276. 真实短增量与平方根二阶矩输入的两项障碍审计

日期：2026-09-06。路线：Vaughan--Brownian response 的中频预算。
论文归属：response-specific 算术输入与循环性审计；本轮仅保存 Markdown。

状态：[T] 真实 von Mangoldt 加权短增量的 bulk 二阶下界；
[N] 单误差质量相对 Lipschitz 输入在指定短尺度一致失败；
[T] 固定比例区间的全尺度平方根二阶矩输入推出 RH 的 Mellin 重建；
[O] 双误差卷积和实际联合 response 的中频预算。
两项审计均不预先宣称新颖性、可发表性或新的零点结论。

本笔记不依赖 275 的新 record 选择证明。第一项对全部
\(Y\le N\le2Y\) 一致，因而也适用于任何满足此范围的后续 record schedule；
它不把新 schedule 的前缀包络结论回填到 271 原有的选择序列。

## 1. 单误差短增量：真实素数正对角造成的障碍

### 1.1 对象、端点和独立输入

固定 \(0<\sigma<1/2\)，令 \(Y\to\infty\)、\(Y\le N\le2Y\)，其中
\(N\) 可为整数或实数。记
\[
 L=\log Y,\qquad W=\log(2L),\qquad
 w_Y(x)=x^{-\sigma}e^{-x/Y},\qquad Z=\log N,
 \tag{1}
\]
\[
 M(Y,t)=\sum_{2\le n\le t}\Lambda(n)w_Y(n)-\int_1^t w_Y(x)\,dx,
 \qquad H_Y(u)=M(Y,e^u)\quad(0\le u\le Z),
 \qquad M=M(Y,N).
 \tag{2}
\]
\(\psi\) 和 \(H_Y\) 采用右连续约定；求和包含上端点。
连续项与素数项在同一 cutoff 匹配，且 \(H_Y(0)=0\)。

外部算术输入 [R] 是无条件定量 PNT。Fiori--Kadiri--Swidinsky 的
Corollary 1.4 给出
\[
 |\psi(x)-x|\ll x(\log x)^{3/2}e^{-c_*\sqrt{\log x}},
 \qquad c_*=0.8476836.
 \tag{3}
\]
已直接核验[正式预印本 v3 的 Corollary 1.4 及其证明](https://arxiv.org/pdf/2204.02588v3)
（正文第 2 页及第 18 页）；这里只用存在的隐常数及指数常数，
不将其有限高度零点验证误写为假设完整 RH，也不宣称该常数最新。
下述素数正对角只需定性 PNT，连续交叉项只需 Chebyshev 上界。

质量上界精确调用已经证明的 **263-C**，而非 265 的转引：
对每个固定 \(0<d<c_*\)，
\[
 \sup_{N\ge Y}|M(Y,N)|
 \le C_{\sigma,d}Y^{1-\sigma}e^{-d\sqrt L}.
 \tag{4}
\]
见 [263，第 3 节，定理 263-C](263-positive-tail-certificate-obstruction.md)。
该定理由 (3) 作 Abel 转移，并明确保留 \(x=1\) 的边界项；
本笔记不重新假设一项与 RH 等价的平方根误差界。

### 定理 276-A [T]：bulk 短增量下界

存在仅依赖 \(\sigma\) 的正数 \(c_0,c_1\)，使对全部充分大的 \(Y\)、
全部 \(Y\le N\le2Y\) 及全部
\[
 0<h\le c_0\frac{L}{Y},\qquad
 I_Y=[\log(Y/3),\log(5Y/6)],
 \tag{5}
\]
有
\[
 \boxed{\quad
 V_Y(h):=\int_{I_Y}|H_Y(u+h)-H_Y(u)|^2\,du
 \ge c_1 hY^{1-2\sigma}L.
 \quad}
 \tag{6}
\]
这里 \(V_Y(h)\) 在该 bulk 中实际上不依赖 \(N\)。
尤其不要求 \(h\) 小于任意实际素数间距。

证明：对充分大的 \(Y\)，(5) 保证
\(h<\min\{\log(3/2),\log(6/5)\}\)。因此对所有 \(u\in I_Y\)，
\[
 1<Y/3\le e^u<e^{u+h}\le Y\le N.
 \tag{7}
\]
没有窗口跨过 cutoff。精确增量为
\[
 H_Y(u+h)-H_Y(u)=P_h(u)-C_h(u),
 \tag{8}
\]
\[
 P_h(u)=\sum_{e^u<n\le e^{u+h}}\Lambda(n)w_Y(n)\ge0,
 \qquad C_h(u)=\int_{e^u}^{e^{u+h}}w_Y(x)\,dx\ge0.
 \tag{9}
\]

首先保留真实素数的正对角。对每个 \(Y/2<p\le2Y/3\)，
使该素数进入 (9) 的 \(u\) 集合为
\([\log p-h,\log p)\)，全包含于 \(I_Y\)，长度恰为 \(h\)。
所有素数及素数幂的系数均非负，故逐点展开平方后可丢掉其他非负项：
\[
 \int_{I_Y}P_h(u)^2\,du
 \ge h\sum_{Y/2<p\le2Y/3}(\log p)^2p^{-2\sigma}e^{-2p/Y}
 \gg_\sigma hY^{1-2\sigma}L.
 \tag{10}
\]
最后一步由
\(\theta(2Y/3)-\theta(Y/2)\sim Y/6\)、\(\log p\asymp L\) 及
\(p^{-2\sigma}e^{-2p/Y}\asymp_\sigma Y^{-2\sigma}\) 给出。
(3) 蕴含这里的 \(\theta\) 渐近：由 Chebyshev 上界，
\(\psi(x)-\theta(x)=O(\sqrt x\log x)=o(x)\)。
特别地，(10) 没有使用素数对相关或把离散平方替换成连续平方。

其次单独记账与连续项的负交叉。由 (7)，
\[
 \sup_{u\in I_Y}C_h(u)\ll_\sigma hY^{1-\sigma}.
 \tag{11}
\]
Fubini 及 Chebyshev 给
\[
 \int_{I_Y}P_h(u)\,du
 \le h\sum_{Y/3<n\le Y}\Lambda(n)w_Y(n)
 \ll_\sigma hY^{1-\sigma}.
 \tag{12}
\]
每个整数在积分中的出现长度至多 \(h\)，这是 (12) 的全部窗口误差。
在 \((P_h-C_h)^2\) 中丢掉正项 \(C_h^2\)，由 (10)--(12) 得
\[
 V_Y(h)\ge c_\sigma hY^{1-2\sigma}L
                  -C_\sigma h^2Y^{2-2\sigma}.
 \tag{13}
\]
选 \(c_0\) 足够小，第二项在 (5) 的全部范围内被第一项的一半吸收。
所有常数均与 \(N,h,Y\) 无关，得到 (6)。\(\square\)

### 推论 276-B [N]：次线性频率尾边界处的失败比值

采用 274 的已定义尺度
\[
 T_*=Y\sqrt{W/L},\qquad
 h_*:=T_*^{-1}=Y^{-1}\sqrt{L/W}.
 \tag{14}
\]
对每个固定 \(A\ge0\)、\(0<d<c_*\)，当 \(M\ne0\) 时一致有
\[
 \boxed{\quad
 \frac{V_Y(h_*)}{M^2h_*^2L^A}
 \gg_{\sigma,d}
 e^{2d\sqrt L}\frac{\sqrt{LW}}{L^A}
 \longrightarrow\infty,
 \qquad Y\le N\le2Y.
 \quad}
 \tag{15}
\]
因此不存在固定的对数损失 \(L^A\)，能使任何这样的 cofinal schedule 满足
\[
 V_Y(h_*)=O(M(Y,N)^2h_*^2L^A).
 \tag{16}
\]

证明：\(h_*Y/L=1/\sqrt{LW}\to0\)，故可用 (6)。将 (4) 平方后代入，得
\[
 \frac{V_Y(h_*)}{M^2h_*^2L^A}
 \gg_{\sigma,d}
 e^{2d\sqrt L}\frac{L^{1-A}}{h_*Y},
 \tag{17}
\]
即 (15)。若 \(M=0\)，(6) 给 \(V_Y(h_*)>0\)，而 (16) 右侧为零，
故同样失败。更精确地，对每个固定 \(A\ge0\) 及 \(K>0\)，
当 \(Y\) 足够大时，对全部 \(Y\le N\le2Y\) 都有
\(V_Y(h_*)>K M(Y,N)^2h_*^2L^A\)。
将 \(h_*\) 换成任意固定正倍数，结论只改变常数。\(\square\)

### 1.2 与实际 response 的接口和禁止扩大的结论

令 \(G\) 为 \(H_Y\) 在 \([-Z,Z]\) 上的奇延拓，再在其外置零。
取 \(\widehat f(\xi)=\int f(u)e^{-i\xi u}\,du\)，并记
\[
 S_H(\xi)=\int_0^Z H_Y(u)\sin(\xi u)\,du,
 \qquad \widehat G(\xi)=-2iS_H(\xi).
 \tag{18}
\]
若 \(r\) 是 (2) 的带符号 lag 测度先对称化、再减去 \(M\delta_0\)
所得中心化误差，则 Stieltjes 分部积分精确给
\[
 \widehat r(\xi)=M(\cos(\xi Z)-1)+\xi S_H(\xi).
 \tag{19}
\]
这里 \(-M\)、连续项和 \(N\) 端点都被保留，且 \(H_Y(0)=0\)。

对 \(U>0\)、\(h=1/U\)，令 \(\Delta_h f(u)=f(u+h)-f(u)\)。
在 \(U\le|\xi|\le2U\) 上，
\(|e^{ih\xi}-1|\ge2\sin(1/2)>0\)。Plancherel 与 Young 给出完全解析的
充分估计
\[
 \frac1{2\pi}\int_{U\le|\xi|\le2U}\xi^2|S_H(\xi)|^4\,d\xi
 \ll U^2\|\Delta_h(G*G)\|_2^2
 \le U^2\|G\|_1^2\|\Delta_hG\|_2^2.
 \tag{20}
\]
其最后一步使用精确恒等式 \(\Delta_h(G*G)=G*(\Delta_hG)\)。
若另有 \(\|G\|_1\ll|M|\)，一种诱人的后续输入会是
\[
 \|\Delta_hG\|_2^2\ll M^2h^2L^A.
 \tag{21}
\]
但由 (7) 在 bulk 内无延拓边界，
\(\|\Delta_hG\|_2^2\ge V_Y(h)\)。所以 (15) 排除 (21) 在
\(h\asymp h_*\) 处成立；这也覆盖顶端中频壳
\([T_*/2,T_*]\) 对应的 \(h=2h_*\)。

这不是 (20) 中 Young 上界的反向不等式，也不是实际 response 的下界。
具体而言，本笔记**不**推出下列任何否定：

- \(\Delta_h(G*G)\) 的双误差交叉抵消或更细的 response-specific 估计；
- \(r*r\) 的短区间二阶预算，或保留物理响应方向后的联合四阶预算；
- 新 schedule 上的低频包络方法、274 的高频尾结论，或 RH 本身。

本结果只排除 (21) 这一指定的单误差正则性输入，即使允许任何固定对数损失。
不能据此宣称所有 Gallagher、短区间或 Young 方法都已失败；
也不能把 \(\|G\|_1\ll|M|\) 这一上界反用成下界。
剩余最小算术输入 [O] 必须直接利用双误差/真实 response 的交叉抵消，
而不能再次要求已被 (15) 排除的单误差 Lipschitz 预算。

## 2. 全尺度平方根二阶矩输入已经隐含 RH：Mellin 循环性审计

这一节独立于第 1 节、\(\sigma\)、cutoff 及 record schedule。
“Selberg 型”在这里仅指区间误差的二阶积分；区间是固定比例
\([x,ax]\)，不能误读为固定加法长度 \([x,x+h]\)。

### 定理 276-C [T]：一个固定比例的全尺度输入足够推出 RH

固定一个实数 \(a>1\)，定义
\[
 E_a(x)=\psi(ax)-\psi(x)-(a-1)x,\qquad x\ge1.
 \tag{22}
\]
如果存在固定 \(C\ge0\)，使对全部充分大的实数 \(X\) 有
\[
 \int_X^{2X}|E_a(x)|^2\,dx\ll_{a,C}X^2(\log X)^C,
 \tag{23}
\]
则 Riemann zeta 函数满足 RH。
这是条件蕴含的完整证明，不是声称 (23) 已无条件成立，也不预先声称新颖性。

证明第一步：在 \(\Re s=b>1/2\) 定义 Mellin 积分
\[
 \mathscr M_a(s)=\int_1^\infty E_a(x)x^{-s-1}\,dx.
 \tag{24}
\]
由 Cauchy--Schwarz，(23) 对每个足够大的 dyadic 块给出
\[
 \int_X^{2X}|E_a(x)x^{-s-1}|\,dx
 \le
 \left(\int_X^{2X}|E_a(x)|^2\,dx\right)^{1/2}
 \left(\int_X^{2X}x^{-2b-2}\,dx\right)^{1/2}
 \ll_{a,C,b}X^{1/2-b}(\log X)^{C/2}.
 \tag{25}
\]
对 \(X=2^jX_0\) 求和收敛，并在半平面 \(\Re s>1/2\) 的每个紧集上
局部一致收敛；加入任意固定次幂的 \(\log x\) 仍收敛。
起始有限区间 \([1,X_0]\) 上 \(E_a\) 局部有界，其 Mellin 积分是整函数。
因此 (24) 是 \(\Re s>1/2\) 上的全纯函数，且可以在紧集上一致逐项求导。

第二步：在 \(\Re s>1\) 内，由绝对收敛的 Euler 乘积对数导数及 Fubini，
\[
 \int_1^\infty\psi(x)x^{-s-1}\,dx
 =\frac1s\sum_{n\ge2}\frac{\Lambda(n)}{n^s}
 =-\frac1s\frac{\zeta'(s)}{\zeta(s)}.
 \tag{26}
\]
在 \(\psi(ax)\) 那一项换元 \(u=ax\)，必须减去 \([1,a]\) 的有限初段。
精确公式为
\[
 \boxed{\quad
 \mathscr M_a(s)
 =-\frac{a^s-1}{s}\frac{\zeta'(s)}{\zeta(s)}
  -a^s\int_1^a\psi(u)u^{-s-1}\,du
  -\frac{a-1}{s-1}.
 \quad}
 \tag{27}
\]
其中 \(a^s=\exp(s\log a)\)，实数 \(\log a>0\) 固定。
有限初段积分及其与 \(a^s\) 的乘积均为整函数；
\(a\) 是否整数不影响普通 Lebesgue 积分的端点约定。

第三步：标准外部事实 [R] 是 \(\zeta\) 的亚纯延拓、在 \(s=1\) 的单极点
及其函数方程。可核验
[DLMF §25.2](https://dlmf.nist.gov/25.2)、
[§25.4，式 25.4.3--25.4.4](https://dlmf.nist.gov/25.4)
以及[§25.10(i) 的非平凡零点对称性](https://dlmf.nist.gov/25.10#i)。
这些是经典基础事实，不涉及零点是否全部在中心线。
于是 (27) 右侧在 \(\Re s>1/2\) 亚纯延拓，并因与全纯的 (24)
在 \(\Re s>1\) 相等而必须具有可去的全部表面极点。

先显式检查 \(s=1\)：
\(\zeta'/\zeta=-1/(s-1)+O(1)\)。
(27) 第一项的留数为 \(a-1\)，恰与最后一项的留数 \(-(a-1)\) 抵消。
这是已扣除主项 \((a-1)x\) 所产生的消极点，不是额外零点假设。

若 \(\rho\) 是 \(\Re\rho>1/2\) 中重数为 \(m\ge1\) 的零点，
则 \(\zeta'/\zeta\) 在 \(\rho\) 的留数为 \(m\)，从而 (27) 在该点的留数为
\[
 -m\frac{a^\rho-1}{\rho}.
 \tag{28}
\]
\(\rho\ne0,1\)，有限初段整函数与最后一项均不能抵消此留数。
关键是乘子没有在目标半平面隐藏零点：
\[
 |a^\rho|=a^{\Re\rho}>1,
 \qquad\text{故}\quad a^\rho-1\ne0.
 \tag{29}
\]
实际上 \(a^s-1\) 的所有零点都在 \(\Re s=0\)。
故 (28) 非零，与 (24) 的全纯性矛盾。
这排除了全部 \(\Re\rho>1/2\) 的零点；再由函数方程对非平凡零点的反射，
也排除 \(0<\Re\rho<1/2\)，即得到 RH。\(\square\)

### 2.1 量词、失效位置与项目中的用途

- 全尺度要求是证明的真实输入：(25) 需要覆盖全部足够大的 dyadic 块。
  仅某个稀疏 cofinal schedule 上的 (23) 不能自动提供这种覆盖，
  本定理没有排除那种更弱的选择性预算。
- 固定 \(a>1\) 保证 (29)。如果取 \(a=1\)，则 \(E_a\equiv0\)，
  假设无内容且乘子恒为零；不能把此退化情形纳入结论。
- 有限初段不能从恒等式 (27) 丢掉，但它是整函数，故不造成新的零点障碍。
  主项也不能遗漏，否则 \(s=1\) 的极点不会按上述方式抵消。
- (23) 是实算术输入，不是由函数方程、有限维压缩、GNS 或紧性自动产生。
  如果某条配置存在性证明把它列为未解释的“常规平方根预算”，
  则该证明已经放入了足以推出 RH 的主要难点。

本节不给 (23) 的无条件证明，也不主张已经证明它与 RH 的双向等价。
它与第 1 节的结论不同：第 1 节无条件否定一个指定的单误差输入；
第 2 节则证明另一个全尺度输入已足够强到推出 RH。
两者均不把 cohomological Weil 结构与显式公式型结构默认等同。

## 3. 依赖与停止边界

独立算术输入只有 (3) 及其定性后果；(4) 由已证明的 263-C 提供。
本笔记没有以数值实验、任意系数 Bessel 界、完整 Weil 正性或有限到无限的
未经控制极限代替真实算术估计，也不新增研究脚本。

主线下一最小引理 [O]：在明确选定的 schedule 上，直接控制双误差卷积或
真实物理 response 的中频贡献，且不调用 (21) 或全尺度 (23) 为未经解释的输入。
当前停止条件是仅重写 Fourier/短区间恒等式，却没有缩小该实际交叉抵消任务。
本文仅为一项实际正对角障碍及一项循环性审计的内部完整证明；
gap_exception_audit 独立构造并逐段检查，主代理另行逆向复核 bulk 范围、
连续负交叉、(15)的量词与指数、(20)的充分性及完整 Mellin 留数，均通过。
这是内部独立复核；新颖性比对、外部同行审查与论文晋级仍须分别完成。
