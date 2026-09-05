# 261. 实际 Abel 质量振荡、孤立素数原子与 mass-only 障碍

日期：2026-09-05。路线：NCE-8 / B1s 至 B1t。论文归属：独立 Abel mass obstruction。

状态：[T] 实际未截断 Abel质量的 Mellin恒等式与振荡归约；
[T] 实际有限截断响应的多项式下界；
[N] \(0<\sigma<1/2\) 时连续尺度上的统一 mass-only预算不成立；
[T] \(\sigma=1/2\) 时该连续尺度预算至少蕴含 RH。
这里明确扩大尺度参数为连续 \(Y\)，原笔记258的固定 \(Y_m=2^m\) 结论仍为 [O]。
没有给出 RH证明、首次变号的有效高度或新颖性认证。
后续262将响应下界扩为 \(Y\le N\le Y^2/8\) 的统一双参数定理，
并覆盖一类 \(N/(Y\log Y)\to\infty\) 的连续截断规则；本笔记的特殊实例保持有效。

## 1. 对象与本轮量词

固定 \(0<\sigma<1,\ a=1-\sigma\)。对 \(Y>0\)，先定义未截断质量
\[
 A_\infty(Y)=\sum_{n\ge2}\Lambda(n)n^{-\sigma}e^{-n/Y},\qquad
 B_\infty(Y)=\int_1^\infty x^{-\sigma}e^{-x/Y}\,dx,\qquad
 M_\infty=A_\infty-B_\infty.
\tag{1}
\]
有限源则在同一个 \(N\) 截断两边：
\[
 d\alpha_{Y,N}=\sum_{2\le n\le N}\Lambda(n)n^{-\sigma}e^{-n/Y}\delta_{\log n},
 \qquad
 d\beta_{Y,N}={\bf1}_{[0,\log N]}(\lambda)
              e^{a\lambda-e^\lambda/Y}\,d\lambda.
\tag{2}
\]
它们就是笔记258的实际系数；仅将 \(Y=2^m\) 扩为实参数。
记 \(A,B,M=A-B,S=A+B,\mu=M/S\)，将 \(\alpha,\beta\) even symmetrize为
\(\alpha^{\rm ev},\beta^{\rm ev}\)，并置
\[
 p=\alpha^{\rm ev}-A\delta_0,\quad
 c=B\delta_0-\beta^{\rm ev},\quad r=p+c,
 \qquad D=\|F_p\|_2^2+\|F_c\|_2^2,
\]
\[
 P^2=\|F_{r*r*p}\|_2^2+\|F_{r*r*c}\|_2^2,\qquad
 J_4(Y,N)=P^2/(S^4D).
\tag{3}
\]
对 \(N=\infty\) 同样定义。所有固定 \(Y\) 的源具有任意对数矩；
零质量测度的 Brownian能量恒等式保证这些量有限；当 \(1<N\le\infty\) 时 \(S,D>0\)。
这里 \(F_\eta(t)=\eta((-\infty,t])\)，Fourier约定为
\(\widehat\eta(\xi)=\int e^{-i\xi x}\,d\eta(x)\)。

本轮排除的命题具有共同常数及共同起点：
\[
 \exists C,Y_0\quad\forall\,Y\ge Y_0:\qquad
 J_4(Y,N(Y))\le C|\mu(Y,N(Y))|^4.
\tag{4}
\]
证明不把“所有充分大的实数 \(Y\)”替换成预先固定的二进格点。

## 2. Mellin恒等式与 Landau正性引理 [T]

### 引理261-A

在 \(\Re s>1-\sigma\) 上，
\[
 \boxed{\int_0^\infty M_\infty(Y)Y^{-s-1}\,dY
 =\Gamma(s)\left[-\frac{\zeta'}{\zeta}(\sigma+s)
                         -\frac1{\sigma+s-1}\right].}
\tag{5}
\]
证明：\(\Lambda(n)\le\log n\) 给
\(A_\infty+B_\infty=O_\sigma(Y^a(1+\log Y))\) 于 \(Y\ge2\)，
而 \(Y\downarrow0\) 时质量按 \(O_\sigma(e^{-c/Y})\) 衰减。
在指定半平面绝对收敛，代换 \(t=x/Y\) 给
\(\int_0^\infty e^{-x/Y}Y^{-s-1}dY=\Gamma(s)x^{-s}\)。
对素数和用 Euler乘积的 logarithmic derivative，对连续项积分
\(\int_1^\infty x^{-\sigma-s}dx\)，即得 (5)。 \(\square\)

右侧在每个正实点 \(s\) 附近全纯。
对实 \(w>1\)，Euler乘积排除零点；对 \(0<w<1\)，交错级数
\(\eta(w)=\sum_{n\ge1}(-1)^{n-1}n^{-w}>0\)，且
\(\zeta(w)=\eta(w)/(1-2^{1-w})<0\)。
在 \(w=1\)，\(-\zeta'/\zeta(w)\) 与 \(1/(w-1)\) 的主部抵消。
\(\Gamma(s)\) 在正实轴无极点。

若 \(\rho\) 是非实 zeta零点且 \(\Re\rho>\sigma\)，则 (5) 的右侧在
\[
 s_\rho=\rho-\sigma,\qquad
 \operatorname*{Res}_{s=s_\rho}
 =-m_\rho\Gamma(\rho-\sigma)\ne0
\tag{6}
\]
有真极点。Gamma函数没有零点；连续项在此没有极点可供抵消。

### 引理261-B：非负尾 Mellin变换的实边界奇点

设 \(f(Y)\ge0\) 于 \(Y\ge Y_0\ge1\)，且
\(G(s)=\int_{Y_0}^\infty f(Y)Y^{-s-1}dY\) 的收敛横坐标 \(c\) 有限。
则 \(G\) 不可能在实点 \(c\) 全纯延拓。

证明：若可延拓，取足够小的 \(\varepsilon>0\)，使 \(b=c+\varepsilon\)
处 Taylor圆盘半径大于 \(\varepsilon\)。这是因为延拓在 \(c\) 的某个圆盘内存在，
而右半平面本来全纯；可取 \(b\) 足够靠近 \(c\)。
各阶导数可在积分下计算，
\[
 (-1)^kG^{(k)}(b)
 =\int_{Y_0}^\infty f(Y)(\log Y)^kY^{-b-1}dY\ge0.
\]
选 \(\varepsilon<h\) 小于该 Taylor半径。由 Taylor收敛及 Tonelli，
\[
 \sum_{k\ge0}\frac{h^k}{k!}(-1)^kG^{(k)}(b)
 =\int_{Y_0}^\infty f(Y)Y^{-(b-h)-1}dY<\infty.
\]
但 \(b-h<c\)，矛盾。 \(\square\)
这是经典 Landau机制的内部重建，不作为新定理优先权主张。

## 3. 实际质量振荡与连续未截断障碍 [T/N]

### 定理261-C

若 zeta有非实零点 \(\rho\) 满足 \(\Re\rho>\sigma\)，则
\(M_\infty(Y)\) 在任意远处都有严格正值和严格负值。
因而有无界的实尺度序列 \(Y_j\) 满足 \(M_\infty(Y_j)=0\)。
特别地，对每个 \(0<\sigma<1/2\)，结论无条件成立。

证明：假设 \(M_\infty\) 最终非负，其非负尾 Mellin变换的收敛横坐标
\(c\le a\)。被删掉的 \(0<Y<Y_0\) 积分是整函数。
若 \(c<\Re(\rho-\sigma)\)，则尾积分在 \(s_\rho\) 附近全纯，
与 (5)--(6) 的亚纯延拓及恒等定理矛盾。因此
\[
 c\ge\Re\rho-\sigma>0.
\tag{7}
\]
引理261-B要求 \(c\) 是奇点，但 (5)在正实点 \(c\) 全纯，矛盾。
对 \(-M_\infty\) 同理。局部对 \(Y\) 微分的 dominated convergence说明
\(M_\infty\) 实解析，介值定理给无界零点序列。
最后使用 [R] 临界线上存在非实零点（例如 Hardy定理），得到
\(\sigma<1/2\) 的无条件结论。 \(\square\)

### 推论261-D

对每个 \(Y>0\)，\(J_4(Y,\infty)>0\)，并且它连续依赖 \(Y\)。
在261-C的假设下，任意 \(Y_0\) 都有
\[
 \sup_{\substack{Y\ge Y_0\\M_\infty(Y)\ne0}}
 \frac{J_4(Y,\infty)}{|\mu(Y,\infty)|^4}=\infty.
\tag{8}
\]
证明：\(r\) 在 \(\log2\) 处有非零原子，而连续项在该点无原子，故 \(r\ne0\)。
Fourier唯一性给某个 \(\xi\ne0\) 满足 \(\widehat r(\xi)\ne0\)。
另一方面，
\[
 \widehat c(\xi)=\int_1^\infty x^{-\sigma}e^{-x/Y}
          (1-\cos(\xi\log x))dx>0\qquad(\xi\ne0).
\tag{9}
\]
所以 \(r*r*c\ne0\)，其 Brownian能量严格为正。
带一阶绝对对数矩的 total variation范数在局部 \(Y\) 区间连续；
卷积及距离积分于是连续。每个 \(M_\infty\) 零点附近，
\(J_4\) 有正下界而 \(\mu\to0\)，即得 (8)。
质量函数不恒为零，例如在充分小的 \(Y\) 处连续项支配且质量差为负；
实解析性保证可从非零质量点趋近其零点。 \(\square\)

## 4. 有限截断的孤立素数原子与多项式响应下界 [T]

此节对所有 \(0<\sigma<1\) 成立，不要求261-C的零点假设。
置
\[
 L=\log Y,\qquad N(Y)=\lfloor YL^2\rfloor.
\tag{10}
\]

### 定理261-E

存在 \(c_\sigma>0,Y_\sigma\)，使所有实数 \(Y\ge Y_\sigma\) 均满足
\[
 \boxed{J_4(Y,N(Y))\ge c_\sigma Y^{-9}L^{-7}.}
\tag{11}
\]

证明分五步。首先由 [R] Bertrand定理可选素数 \(q\in(Y,2Y)\)。
对充分大的 \(Y\)，有 \(q\le N<q^2\)。
置 \(d=\alpha^{\rm ev}-M\delta_0,\ b=\beta^{\rm ev}\)，则 \(r=d-b\)。
测度 \(\eta=r*r*p\) 的原子部分为 \(d*d*p\)；其余部分
\(-2d*b*p+b*b*p\) 绝对连续。

其次，在 \(x_0=3\log q\) 处，\(\eta\) 的原子系数精确为
\[
 w=\frac18\bigl((\log q)q^{-\sigma}e^{-q/Y}\bigr)^3
   \ge c_\sigma L^3Y^{-3\sigma}>0.
\tag{12}
\]
确实，每个原子项由至多三个 signed prime-power lags及中心项组成。
由于 \(q^2>N\)，每个 lag的 \(q\)-valuation至多为1。
达到总 valuation 3必须使用三个正号、各自 valuation 1的项，
于是三因子只能都是 \(q\)。任何中心项或负号都不能产生该位置。
这排除了所有原子抵消；绝对连续项不能改变原子系数。

第三，每个原子位置可写成 \(\log(u/v)\)，其中正整数 \(u,v\le N^3\)。
若 \(u/v\ne q^3\)，两个整数 \(u,vq^3\) 不同，而且其较小者至多为 \(N^3\)。
因此
\[
 |\log(u/v)-3\log q|
 \ge\log(1+N^{-3})\ge(2N^3)^{-1}.
\tag{13}
\]
取 \(\delta=(8N^3)^{-1}\)。两个相邻长度 \(\delta\) 区间内没有其他原子。

第四，初等积分比较给
\[
 S\le C_\sigma Y^aL,\qquad
 \left\|\frac{db}{dx}\right\|_\infty\le C_\sigma Y^a.
\tag{14}
\]
第二式中的 \(x\) 是 additive lag变量，不是原整数变量。
利用 \(\|d\|_{\rm TV}\le2S,\ \|p\|_{\rm TV}\le2A,\ \|b\|_{\rm TV}=B\)，
绝对连续余项的密度 \(g\) 满足
\[
 \|g\|_\infty\le10S^2\left\|\frac{db}{dx}\right\|_\infty
 \le C_\sigma Y^{3a}L^2.
\tag{15}
\]
由 (12)及 \(N\asymp YL^2\)，
\(\delta\|g\|_\infty/w=O_\sigma(L^{-7})\)，最终小于 \(1/4\)。
\(F_\eta\) 在 \(x_0\) 有跳跃 \(w\)，故左右极限至少一个的绝对值不小于 \(w/2\)。
在该侧长度 \(\delta\) 的区间上，连续变化至多 \(w/4\)。
所以
\[
 P^2\ge\|F_\eta\|_2^2\ge\delta w^2/16
 \ge c_\sigma Y^{-6\sigma-3}.
\tag{16}
\]

最后，minimum kernel给
\[
 D\le\tfrac12(\log N)(A^2+B^2),\qquad
 S^4D\le C_\sigma Y^{6a}L^7.
\tag{17}
\]
将 (16)除以 (17)即得 (11)，因为 \(6\sigma+6a=6\)。 \(\square\)

本证明直接作用于有限实际系数，允许 \(N(Y)\) 的跳跃。
它不依赖 compact carrier分离、相对tail transfer、PNT或四矩猜想。
指数9只是本证明的可审计值，不声称最优。

## 5. 从未截断质量零点到实际有限源 no-go [T/N]

### 定理261-F

若存在 zeta零点 \(\rho\) 满足 \(\Re\rho>\sigma\)，则 (4)对
\(N(Y)=\lfloor Y(\log Y)^2\rfloor\) 不成立，即使只要求在 \(\mu\ne0\) 的尺度上成立。
更一般地，任意固定正指数 \(\kappa\) 都不能使
\(J_4(Y,N(Y))=O(|\mu(Y,N(Y))|^\kappa)\) 于所有充分大实数 \(Y\) 成立。

证明：取261-C给出的 \(M_\infty(Y_j)=0,\ Y_j\to\infty\)。
两源共同截断后，\(|M(Y_j,N_j)|\) 至多为被删掉的正源总质量。
由 \(\Lambda(n)\le\log n\) 及 \(N/Y\asymp L^2\)，
\[
 |M(Y_j,N_j)|\le C_\sigma Y_j^a L_j^2e^{-L_j^2/2}.
\tag{18}
\]
例如将递减的 \((\log x)x^{-\sigma}e^{-x/Y}\) 的尾和用从 \(N\) 起的积分控制，
代换 \(x=Yu\)，再用 \(\log u\le u,\ u^{-\sigma}\le1\)（\(u\ge1\)）。
得到 \(C Y^a(L+N/Y+1)e^{-N/Y}\)，这蕴含 (18)；floor误差可吸收到常数。
连续源同样满足该界，且
\(B(Y,N)\ge c_\sigma Y^a\) 来自 \(x\in[Y/2,Y]\)。
所以
\[
 |\mu(Y_j,N_j)|\le C_\sigma L_j^2e^{-L_j^2/2}.
\tag{19}
\]
为同时覆盖笔记256排除零质量点的版本，必要时把每个 \(Y_j\) 向右作任意小扰动。
函数 \(Y\mapsto Y(\log Y)^2\) 最终严格递增，因此在 \(Y_j\) 右侧有一个
保持 \(N(Y)=N_j\) 的区间，连 \(Y_j\) 恰为 cutoff threshold时也如此。
固定 \(N_j\) 后，\(M(Y,N_j)\) 是 \(Y>0\) 上不恒为零的实解析函数：
充分小的 \(Y\) 处连续积分从 \(x=1\) 起，其大小支配从 \(n=2\) 起的素数和。
所以其零点孤立。可选 \(Y'_j\) 满足
\(0<Y'_j-Y_j<Y_j^{-1}\)、\(M(Y'_j,N_j)\ne0\)，并由连续性使质量变化小于
(18)的右侧。于是 (19)在 \(Y'_j\) 仍成立，常数至多改变一个固定因子。

定理261-E直接给这个有限源的响应下界，无须将未截断响应转移过来。
由于 \(Y'_j/Y_j\to1\)，得到非零质量点上的
\[
 \boxed{\frac{J_4(Y'_j,N_j)}{|\mu(Y'_j,N_j)|^4}
 \ge c_\sigma e^{\,2L_j^2-9L_j}L_j^{-15}\longrightarrow\infty.}
\tag{20}
\]
对任意 \(\kappa>0\)，同样得到指数因子
\(e^{\kappa L_j^2/2-9L_j}\) 支配所有对数幂，故广义结论成立。 \(\square\)

### 推论261-G：预算强度与停止边界

- [N] 对每个 \(0<\sigma<1/2\)，连续实际 Abel尺度上的 (4) 无条件失败。
- [T] 对任意 \(0<\sigma<1\)，若 (4)成立，则 zeta在 \(\Re s>\sigma\) 无非平凡零点。
- [T] 特别地，\(\sigma=1/2\) 时 (4)蕴含 RH。没有证明逆命题。

这识别了预算的必要强度：它虽然只由算术 source定义，但在中心参数的
连续统一版本中不能被当作比 RH明显弱的输入。上述推论通过反证使用一个可能的
离线零点，不预设 RH真假。

## 6. 固定格点、配置接口与下一最小引理

若要求对 \(Y=\theta2^m,\ 1\le\theta<2\) 有同一个 \(C\) 和同一个
最终起点 \(m_0\)，则它涵盖所有充分大实数 \(Y\)，故也被261-F排除或受到261-G限制。
若 \(C,m_0\) 依赖 \(\theta\)，上述结论不能直接调用。
特别是原笔记258的固定 \(\theta=1\) 序列尚未被排除。

与部分 Weil配置的接口是笔记256的 mass-relative capture/Schur充分判据。
本轮只排除这条判据的连续统一输入；既没有排除 cofinal选点上的增益，
也没有排除 Gamma-complete配置存在性、其他响应归一化或 RH本身。
不能用新 no-go反向宣称实际 dyadic响应没有增益。

B1s量词审计已完成：笔记255固定 \(Y_m=2^m\)，笔记256的 B1o-q4
询问沿某条 cofinal matched schedule存在统一常数，并只在 \(\mu_m\ne0\) 处要求预算。
256-C另外要求最终 \(\mu_m\ne0\)。其 Schur结论沿同一所选 schedule成立，
没有要求所有实尺度或全部phase。251中的 \(\theta=\xi\log Y\) 是频率坐标，
不是这里的尺度phase。因此本轮不否定原来的存在性目标。

B1s分流：停止在 \(0<\sigma<1/2\) 连续族上寻求 mass-only预算；
\(\sigma=1/2\) 的连续版本标记为 RH-hard必要条件，禁止当作软公理。
**B1t** 保留所选 dyadic cutoff的实际 \(E_1,E_2\) 估计及质量差下界。
对于特定 \(N_m=\lfloor Y_mL_m^2\rfloor\)，(11)说明质量相对预算至少要求
\(|\mu_m|\ge cY_m^{-9/4}L_m^{-7/4}\) 于所检验的非零质量点；
若沿子序列该比值趋零，就得到这个 schedule的 no-go。
目前未证明这种 dyadic接近，也未证明对所有可选 cutoff的统一障碍。
若抽取 cofinal子序列 \(m_j\)，频率归一化必须保留 \(t=m_j\xi\)，不能换成 \(j\xi\)。

## 7. 假设删除、模型范围与依赖审计

最小输入及用途：

1. [T] exponential Abel权与 Euler logarithmic derivative：给 (5)及快速截断尾；
2. [R/T] zeta亚纯延拓、实正轴无零点、极点主部：排除正实 Mellin奇点；
3. [R] 某个 \(\Re\rho>\sigma\) 的非实零点：提供 Landau所需真极点；
   \(\sigma<1/2\) 时可引用 Hardy的经典存在性，\(\sigma\ge1/2\) 时是反证假设；
4. [T] 正源及实际 prime-power支撑、[R] Bertrand：构造无抵消原子；
5. [T] 全实数尺度量词：使质量零点序列可被测试；
6. [T] 两源共同 cutoff及同一 \(J_4,\mu\) 归一化：使 (18)--(20)对应同一对象。

删除审计：若 Mellin变换在正实轴存在主导极点，非实极点未必迫使质量变号；
若没有右侧非实零点，本证明不给质量零点；若允许重新调整连续源质量，
则研究对象已变；若只看固定离散尺度，介值定理不足；
若忘记 prime-power valuation或把原子混入密度，就不能使用跳跃下界。
数值中所有已检样本为负并不反驳最终振荡定理。

Riemann源已给实际无条件实例。Dedekind及实 L系数若有正实零点，
必须重新检查 Landau前提，不能直接套用；一般复 Dirichlet/自守系数
没有本证明使用的实符号与正源结构。函数域的固定 degree格点也不受连续介值论证覆盖。
这一范围限制保留了 cohomological Weil结构与本显式响应模型的区别。

## 8. 复算、实验与文献边界

[E] scripts/abel_prime_atom_audit.py 用精确有理数乘法卷积核验独立原子系数、
中心/负号抵消的排除及整数间距；渐近下界仍由第4节证明。
独立复核分别审计 Landau、有限cutoff下界以及两者的全源/有限源拼接。

[E] scripts/abel_mass_discrepancy_probe.py 使用 numpy/mpmath，
在 \(\sigma=1/4,1/2,3/4,\ Y=2^3,\ldots,2^{18}\) 上计算实际有限质量。
全部48个样本均为负。取 \(N=40Y,\ Y=262144\)，约为：

| \(\sigma\) | \(M(Y,N)\) | (5) 在 \(s=0\) 的留数 \(C_\sigma\) |
|---|---:|---:|
| \(1/4\) | -0.755055201996584 | -0.755059939377137 |
| \(1/2\) | -0.686087630934026 | -0.686091709612833 |
| \(3/4\) | -0.627578884515700 | -0.627582469359427 |

这里 \(C_\sigma=-\zeta'(\sigma)/\zeta(\sigma)+1/(1-\sigma)\)；
表格不宣称 \(M(Y)\to C_\sigma\)。浮点求和、数值微分及积分不构成认证包围，
也没有定位首个质量零点。实验只是说明可计算小尺度未看到渐近振荡。
本机 numpy.longdouble 与 float64 均只有52个显式尾数位；脚本打印的
tail majorant只评估被截断的数学尾项，不包含浮点系数、数值微分和求和误差。

[R] 临界线上非实零点的经典存在性及 zeta零点对称性可核查
[NIST DLMF §25.10](https://dlmf.nist.gov/25.10)。
[R] Bertrand定理使用 Erdős发表于1932年的原文
[Beweis eines Satzes von Tschebyschef](https://users.renyi.hu/~p_erdos/1932-01.pdf)，
卷页为 Acta 5, 194--198；[出版机构档案](https://acta.bibl.u-szeged.hu/13396/)
核对题名、年份及页码。Landau机制已完整重建。
本文主张组合后的内部定理与实际模型障碍，尚未完成全面文献优先权检索。
