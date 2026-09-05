# 267. 素数幂碰撞控制、四阶高频尾与全频乘子障碍

日期：2026-09-05。路线：NCE-8 / B1v 至 B1w。
论文归属：Vaughan--Brownian response；本轮仅Markdown。

状态：[T] 实际素数幂乘积系数平方和及加权平方和的一致界；
[T] 精确额外碰撞项及 \(\sigma>1/8\) 时的有界性；
[T/R] 实际四阶高频尾的cutoff无关预算；
[N] 有限实际源的全频乘子小量障碍；
[E] 有限频带探针；[O] 增长但有限的频带中的相对算术预算。
本轮不证明全源mass-only预算、RH/GRH或新的零点比例。

## 1. 对象和需要保留的质量中心项

固定 \(0<\sigma<1/2\)，置 \(a=1-\sigma,\ Y\to\infty,\ L=\log Y\)。
任意有限 \(N\ge Y\) 上实际素数系数为
\[
 a_n=\mathbf1_{n\le N}\Lambda(n)n^{-\sigma}e^{-n/Y}.
 \tag{1}
\]
令 \(F(\xi)=\sum_n a_n n^{-i\xi}\)，
\(C(\xi)=\int_1^N x^{-\sigma-i\xi}e^{-x/Y}dx\)。
完整和窗口源的质量差分别记 \(M=A-B\)、\(M_H=A_H-B_H\)。
沿用265的centered \(r,r_H\)，精确有
\[
 \widehat r(\xi)=\Re F(\xi)-\Re C(\xi)-M .
 \tag{2}
\]
窗口版本完全同型，只将两边共同限制到
\([L-H,L+H]\cap[0,\log N]\)。不管频率多大，都不能删除式(2)的 \(-M\)。

仍以
\[
 A_4=\|F_{(r-r_H)*(r+r_H)}\|_2,\qquad
 B_4=\|F_{r_H*r_H}\|_2
 \tag{3}
\]
表示265的两个四阶量。这里 \(F_\eta\) 是测度primitive，和上面的Dirichlet多项式
\(F(\xi)\) 用参数/下标区分。

以下首先控制真实prime-power系数，而不直接对六阶physical response使用任意系数Bessel界。

## 2. 乘积系数和单素数链 [T]

### 引理267-A：混合乘积纤维界

令 \(x_n,y_n\) 分别为(1)在任意两个prime-power子集上的限制。
设 \(V_x=\sum x_n^2,\ V_y=\sum y_n^2\)。则
\[
 \boxed{\ \sum_m\left(\sum_{uv=m}x_uy_v\right)^2
 \le C_\sigma V_xV_y,\qquad
 C_\sigma=\max\left\{2,\frac{1+2^{-2\sigma}}{1-2^{-2\sigma}}\right\}.\ }
 \tag{4}
\]
此引理本身只要求固定 \(\sigma>0\)；常数不依赖 \(Y,N\) 或所删的项。

证明：不同素数 \(p\ne q\) 的乘积 \(p^jq^k\) 至多有两种有序分解。
用 \((u+v)^2\le2u^2+2v^2\)，它们的贡献至多
\(2\sum_{p\ne q}V_{x,p}V_{y,q}\)。

对同素数链，记 \(x_j=x_{p^j},y_j=y_{p^j}\)，并在未选指数处补零。
每个非零 \(x_j\) 与 \(h\ge1\) 满足
\(x_{j+h}\le p^{-\sigma h}x_j\)，若后项被删除不等式仍成立。
因此
\[
 C_x(h):=\sum_jx_jx_{j+h}\le p^{-\sigma h}V_{x,p}.
 \tag{5}
\]
有限求和的精确自相关恒等式为
\[
 \|x*y\|_{\ell^2}^2
 =V_{x,p}V_{y,p}+2\sum_{h\ge1}C_x(h)C_y(h)
 \le\frac{1+p^{-2\sigma}}{1-p^{-2\sigma}}V_{x,p}V_{y,p}.
 \tag{6}
\]
同、异素数的index pairs彼此不交，合并即得(4)。\(\square\)

### 定理267-B：额外重数的精确账本

对单个限制源写
\[
 Q=\sum_n a_n^2,\quad D_4=\sum_n a_n^4,\quad
 b_m=\sum_{uv=m}a_ua_v .
\]
则
\[
 \boxed{\ \sum_m b_m^2=2Q^2-D_4+\mathcal C,\ }
 \qquad
 \mathcal C=4\sum_p\sum_{h\ge1}\sum_{j<k}
 a_{p^j}a_{p^{j+h}}a_{p^k}a_{p^{k+h}}\ge0 .
 \tag{7}
\]
若 \(R(v)=\sum_{n_1/n_2=v}a_{n_1}a_{n_2}\)，则
\[
 \sum_{v\ne1}R(v)^2=Q^2-D_4+\mathcal C .
 \tag{8}
\]

证明：不同素数的乘积无额外有序分解。单素数链由(6)的自相关展开，
在每个 \(C_a(h)^2\) 中分开 \(j=k\) 与 \(j\ne k\)。
前者连同零shift给两个配对的贡献 \(2Q^2-D_4\)，其余恰为(7)。
因 \(uv=xy\) 等价于 \(u/x=y/v\)，product energy等于全部ratio fiber energy；
单位比值的系数是 \(Q\)，删除其平方即得(8)。
中间指数相同的首次额外碰撞 \(p\cdot p^3=p^2\cdot p^2\) 也包括在(7)内。\(\square\)

实际Abel系数给
\[
 \mathcal C\le
 4\sum_p\frac{(\log p)^4p^{-8\sigma}
      e^{-(p+2p^2+p^3)/Y}}
 {(1-p^{-2\sigma})^3(1+p^{-2\sigma})}.
 \tag{9}
\]
证明：每个乘积的指数和是 \(2(j+k+h)\)，置 \(q=p^{-2\sigma}\)；
\(\sum_{h\ge1,j<k}q^{j+k+h}=q^4/((1-q)^3(1+q))\)。
四个Abel指数中的数之和至少为 \(p+2p^2+p^3\)。
若 \(\sigma>1/8\)，去掉指数后与
\(\sum_{n\ge2}(\log n)^4n^{-8\sigma}\) 比较即得
\[
 \boxed{\ \mathcal C=O_\sigma(1)\quad(\sigma>1/8),\ }
 \tag{10}
\]
一致于全部cutoff及所有子集限制。没有宣称 \(\sigma=1/8\) 时仍有这个有界结论。

特别在本轮 \(\sigma=1/4\) 模型，额外精确重数不是一个随 \(Y\) 失控的输入。
但精确相等的product/ratio fibers不控制频率平均中的近碰撞；
不能据(7)直接声称增长短频带已对角化。

## 3. 加权系数预算不需要 \(N^2\) 长度损失 [T]

置
\[
 B_0=\sum_m b_m^2,\quad B_1=\sum_m m b_m^2,\quad
 Q_j=\sum_n n^j a_n^2\quad(j=0,1).
 \tag{11}
\]
初等Chebyshev上界 \(\psi(X)\ll X\) 与 \(\Lambda(n)^2\le\Lambda(n)\log n\) 给
\[
 Q_0\ll_\sigma Y^{1-2\sigma}L,\qquad
 Q_1\ll_\sigma Y^{2-2\sigma}L.
 \tag{12}
\]
可直接对 \(n\asymp X\) 分块：该块至多
\(C_\sigma X^{j+1-2\sigma}\log(2X)e^{-cX/Y}\)。
小于 \(Y\) 的二进块由 \(j+1-2\sigma>0\) 求和，大于 \(Y\) 的块由指数求和。
正项允许延伸到无穷，故常数与 \(N\) 无关。这一步没有使用PNT误差率。

### 引理267-C：加权单素数链的 \(\ell^1/\ell^2\) 界

固定 \(\tau>0\)。对任意素数 \(p\)、\(Y>0\) 和有限连续指数区间，
序列 \(z_j=p^{\tau j}e^{-p^j/Y}\) 满足
\[
 \|z\|_1\le C_\tau\|z\|_2,\qquad
 C_\tau=\frac1{1-2^{-\tau/2}}+4+\frac1{1-2^{-\tau}}.
 \tag{13}
\]

证明：未截断的相邻比为
\[
 z_{j+1}/z_j=p^\tau e^{-x_j},\qquad x_j=(p-1)p^j/Y.
 \tag{14}
\]
在 \(x_j<(\tau/2)\log p\) 的左段，相邻比至少 \(2^{\tau/2}\)；
该段总和由最大项乘第一个几何常数控制。
在 \(x_j>2\tau\log p\) 的右段，相邻比至多 \(2^{-\tau}\)，同理。
中间的 \(x_j\) 只跨因子4，而相邻 \(x_j\) 的比为 \(p\ge2\)，
其项数可放宽为4。各段最大项不超过整段 \(\ell^2\) 范数，得(13)。
有限区间截断不改变段内相邻比。\(\square\)

\(\tau>0\) 不可在此证明中静默删去：当 \(\tau=0,p=2,Y\to\infty\)，
越来越长的初始链近似为常数，\(\ell^1/\ell^2\) 无一致上界。

### 定理267-D

对任意full或区间限制的实际源，
\[
 \boxed{\ B_0\ll_\sigma Y^{2-4\sigma}L^2,\qquad
 B_1\ll_\sigma Y^{4-4\sigma}L^2.\ }
 \tag{15}
\]
证明：第一式由(4)、(12)给出。
第二式令 \(c_n=\sqrt n\,a_n\)，则
\(\sqrt m\,b_m=(c*c)(m)\)。
异素数贡献至多 \(2Q_1^2\)。同素数链为
\((\log p)p^{\tau j}e^{-p^j/Y}\)，其中 \(\tau=1/2-\sigma>0\)；
由Young与(13)，该链卷积的平方和至多
\(\|c_p\|_1^2\|c_p\|_2^2\le C_\tau^2Q_{1,p}^2\)。
加总并用(12)即得第二式。\(\square\)

任意删除项也可用正系数单调性将其 \(B_1\) 上界为full \(B_1\)，
因此(15)的全局 \(Y\) 上界仍适用；这里不额外声称删项后的
\(B_1\ll Q_{1,\mathrm{subset}}^2\) 是本段已证明结论。

## 4. 加权均值到实际高频四能量 [T/R]

使用经典外部均值上界 [R]：对任意有限Dirichlet多项式
\(P(t)=\sum_m d_m m^{-it}\)，任意实数 \(V\) 和 \(U\ge1\)，
\[
 \int_V^{V+U}|P(t)|^2dt
 \le C_{\rm MV}\sum_m(U+m)|d_m|^2 .
 \tag{16}
\]
这是Montgomery--Vaughan加权均值定理的上界形式；
平移 \(V\) 只改变系数的单位相位。
本轮核验的作者讲义及正式论文书目信息列在第8节；
不使用未经核验的最优Hilbert常数。

对 \(F(t)^2=\sum b_m m^{-it}\)，在 \([2^jT,2^{j+1}T]\) 上用(16)，
乘以 \((2^jT)^{-2}\) 后求和，得到
\[
 \int_{|\xi|>T}\frac{|F(\xi)|^4}{\xi^2}d\xi
 \ll \frac{B_0}{T}+\frac{B_1}{T^2}\qquad(T\ge1).
 \tag{17}
\]
所有序列均有限；在正项高频积分上用可求和的几何majorant。
这不是把有限样本的均值猜测提升为无限频带结论。

连续lag密度 \(g(\lambda)=e^{a\lambda-e^\lambda/Y}\) 单峰，
且 \(\sup g\ll_\sigma Y^a\)。
限制到一个区间后零延拓的总变差至多 \(2\sup g\)，所以
\[
 |C(\xi)|,\ |C_H(\xi)|\le C_\sigma Y^a/|\xi|
 \quad(\xi\ne0).
 \tag{18}
\]
这是BV分部积分，包含区间两端的跳跃；不能删除它们而声称有限cutoff也有纯Gamma指数衰减。

### 定理267-E：cutoff无关的实际高频尾

记
\[
 \mathcal H_T(q)=\frac1{2\pi}
 \int_{|\xi|>T}\frac{|\widehat q(\xi)|^4}{\xi^2}d\xi,
 \qquad q=r\ \hbox{或}\ r_H .
 \tag{19}
\]
对任意有限 \(N\ge Y\)、任意 \(H\ge0\)、\(T\ge1\)，一致有
\[
 \boxed{\ \mathcal H_T(q)\ll_\sigma
 \frac{Y^{2-4\sigma}L^2}{T}
 +\frac{Y^{4-4\sigma}L^2}{T^2}
 +\frac{M_q^4}{T}
 +\frac{Y^{4a}}{T^5}.\ }
 \tag{20}
\]
其中 \(M_q=M\) 或 \(M_H\)，空窗口对应零源。

证明：将(2)代入，使用
\(|u+v+w|^4\le27(|u|^4+|v|^4+|w|^4)\)。
prime项用(15)、(17)，continuum项用(18)及
\(\int_T^\infty \xi^{-6}d\xi=(5T^5)^{-1}\)，
中心项保留 \(\int_T^\infty M_q^4\xi^{-2}d\xi=M_q^4/T\)。\(\square\)

将(3)按频率正交切分为 \(A_{4,\le T}^2+A_{4,>T}^2\) 等，有
\[
 A_{4,>T}^2+B_{4,>T}^2
 \le2\mathcal H_T(r)+3\mathcal H_T(r_H).
 \tag{21}
\]
所以(20)也控制这两个实际四阶尾，只需把中心项换成
\((M^4+M_H^4)/T\)。

对 \(\sigma=1/4\)，除中心项外的余项为
\[
 \mathscr R(Y,T)=\frac{YL^2}{T}+\frac{Y^3L^2}{T^2}+\frac{Y^3}{T^5}.
 \tag{22}
\]
任意固定 \(\varepsilon>0\) 下，\(T=Y^{3/2+\varepsilon}\) 使 \(\mathscr R\to0\)。
但不能据此声称完整实际高频能量无条件趋于0，质量项仍在。
仅用 \(|M|,|M_H|\ll Y^{3/4}\)，选 \(T=Y^{3+\varepsilon}\) 才可直接得到
\[
 A_{4,>T}^2+B_{4,>T}^2=O_\varepsilon(Y^{-\varepsilon}).
 \tag{23}
\]
这是平方能量；相应范数为 \(O(Y^{-\varepsilon/2})\)。

## 5. 精确的finite-band接口与未闭合部分 [T/O]

本节示例仍取 \(\sigma=1/4\)；连接265的signed截断结论时，
另继承其 \(0\le H\le k\sqrt L\)（固定 \(k\)）范围。
一般 \(\sigma\) 应将下文 \(\mathscr R\) 换成(20)中的非质量余项。
这不缩小高频定理267-E本身对任意 \(H\ge0\) 的适用范围。

若在同一schedule上已有 \(|M_H|\le C_0|M|\)、\(M\ne0\)，则除以 \(M^4L\) 后，
中心项仅为 \(O_{C_0}(1/(TL))\)。
其余项仍含 \(M^{-4}\)，不能从绝对小量自动变为相对小量。

例如，一个可审计的充分组合是
\[
 \begin{aligned}
 &|M_H|=O(|M|),\qquad
 \mathscr R(Y,T)=o(M^4L),\qquad T\to\infty,\\
 &A_{4,\le T}+e^{-aH}B_{4,\le T}=O(M^2\sqrt L).
 \end{aligned}
 \tag{24}
\]
(21)表明高频尾在目标范数下为 \(o(1)\)，故(24)推出265-(24)。
局部 \(E_{2,H}=O(LM_H^4)\) 仍须另外证明，才能接到264的full预算及256的Schur接口。

这是真正去掉无穷高频尾的证明，但不是自动闭合中频：
区间 \([0,T(Y)]\) 随 \(Y\) 增长，不能用fixed-frequency PNT替代其统一四阶控制。
仅将其再写成大矩阵或换partition不算晋级。

## 6. 实际有限源的全频乘子障碍 [N]

### 定理267-F

对任一固定有限实际源，或任何有 \(B_H>0\) 的局部窗口，存在 \(\xi_j\to\infty\)，使
\[
 \widehat r(\xi_j)\longrightarrow B
 \quad\hbox{或}\quad \widehat r_H(\xi_j)\longrightarrow B_H.
 \tag{25}
\]

证明：有限个非零原子的相位可同时返回到1。
具体对其有限频率 \(\lambda_i/(2\pi)\) 使用抽屉原理：
将 \(Q^s+1\) 个整数倍向量放入单位立方体的 \(Q^s\) 个小格，
得到整数 \(1\le q\le Q^s\) 使全部 \(\|q\lambda_i/(2\pi)\|\le1/Q\)。
若这些 \(q\) 随 \(Q\) 无界，取子列；
若有有界子列，则存在一个固定非零 \(q_0\) 使全部相位精确为1，
其整数倍亦给无界序列。
因此 \(\Re F(\xi_j)\to A\)。由(18)连续项趋于0，再用(2)得 \(A-M=B\)。
空prime源时同样成立，任选 \(\xi_j\to\infty\)。\(\square\)

在以 \(\|F_\eta\|_2\) 完备化的零质量测度空间上，
卷积 \(r\) 的算子范数为 \(\|\widehat r\|_\infty\)，因primitive与卷积交换且
紧支撑光滑primitive在 \(L^2\) 中稠密。因此
\[
 \boxed{\ \|\eta\mapsto r*\eta\|_{\rm op}\ge B.\ }
 \tag{26}
\]
实际full源满足 \(B\asymp S\)，故不可能通过
\(\|\widehat r\|_\infty=o(S)\) 获得第二份saving。
局部结论在 \(B_H\asymp S_H\) 时同理。
这是实际有限源而非外生振荡源的障碍，但只排除全频算子范数路线：
返回频率可以极高，(25)不提供正比例积分能量，也不否定(20)、(24)或response-specific抵消。

## 7. 冻结有限频带实验 [E]

脚本 `scripts/quartic_signed_frequency_probe.py` 固定
\[
 \sigma=\tfrac14,\quad Y=2^m,\quad N=\lfloor YL^2\rfloor,\quad
 H=\min(\log L,L/8).
 \tag{27}
\]
运行 `python -B scripts/quartic_signed_frequency_probe.py --max-m 10`。
以 \(T=1,8,32,128\) 分频带，全部只计算 \(A_{4,\le T},B_{4,\le T}\)。
在 \(T=128\) 得：

| \(m\) | \(A_{4,\le T}/(M^2\sqrt L)\) | \(e^{-aH}B_{4,\le T}/(M^2\sqrt L)\) |
|---:|---:|---:|
| 4 | 0.535003 | 0.244206 |
| 6 | 1.087592 | 0.131090 |
| 8 | 2.664836 | 0.246001 |
| 10 | 5.924380 | 1.327855 |

本表不是total能量或认证下界，不推出渐近发散，也不否定某个未知统一常数的存在。
中心化使用 \(\cos x-1=-2\sin^2(x/2)\)；
lag Gaussian 10/18阶、frequency Gaussian 8/12阶的粗细相对差不超过
\(4.9\cdot10^{-14}\)。48个连续项独立complex incomplete-gamma抽样的scaled误差
不超过 \(3.6\cdot10^{-15}\)；这些均不是interval包络。
在 \(m=8\) 中 \(8\)--\(32\) 带贡献较大，但 \(m=10\) 的低频部分也已增长，
不将全部趋势归因于单一频带或某个零点。

## 8. 依赖、循环性审计与文献边界

独立输入及作用：

1. prime-power支撑与唯一分解给(4)、(7)，不是任意系数Bessel替代；
2. Abel权的几何/单峰链结构给(5)、(13)，消去粗 \(N^2B_0\) 长度预算；
3. Chebyshev上界给(12)，不调用RH或PNT平方根误差；
4. 外部加权均值(16)只控制高频积分；未据此声称中频渐近对角化；
5. 有限cutoff与区间连续源给(18)、(25)，局部空源可直接处理；
6. 未决实际质量及有限增长频带预算只在(24)出现，不作为已证的正性公理。

删除prime-power支撑后，general product fibers可有大量额外分解；
若允许任意链权，(13)的统一 \(\ell^1/\ell^2\) 控制不再保证：
越来越长的常数块即为反例。只删除Abel指数截断而保留
\(p^{\tau j}\) 的几何权，并不会使该链范数界失效，但会失去统一的 \(Y\) 规模预算。
\(\sigma=1/2\) 时本轮weighted链证明不适用，不能静默保留(15)常数。
删除有限原子性后，相位同步的(25)证明不适用。
不同源模型的算术输入必须另证；Dirichlet/自守相位系数、Gamma-complete及上同调桥梁
没有从这些正源结果自动得到。

[R] H. L. Montgomery and R. C. Vaughan, *Hilbert's Inequality*,
J. London Math. Soc. (2) 8 (1974), 73--82，
[正式论文DOI](https://doi.org/10.1112/jlms/s2-8.1.73)。
本轮核验期刊书目、[作者存档原文的Corollary3](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)，并在
[Vaughan作者讲义，Chapter26，Theorem26.A](https://personal.science.psu.edu/rcv4/597-5f25/Class597-26.pdf)
核对(16)的加权上界形式；不声称已重新证明原论文的Hilbert不等式或最佳常数。

额外碰撞的有限恒等式及初等求和在本文完整重建，相关文献优先权仍[O]。
运行 `python -B scripts/prime_power_product_fiber_audit.py` 可独立复算product/ratio
聚合与单素数链碰撞账本；该脚本的有理权模型检查代数恒等式与几何链界，
不是将实际对数/Abel系数假装成有理数。有理有限检查仅为[E]，不替代任何渐近证明。
268进一步用实际素数跳跃选择自由cutoff，独立闭合full \(J_4\) 在
\(|\xi|>Y^2\) 的相对高频尾，而不需要本节局部质量匹配。
当前主线晋级为268的所选schedule增长频带预算，原(24)保留为局部辅助接口；
全频乘子范数路线按267-F止损。
