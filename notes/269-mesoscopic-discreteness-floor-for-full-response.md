# 269. 实际全响应的中尺度离散性下界

日期：2026-09-05。路线：NCE-8 / B1w；论文归属：Abel mass obstruction。
状态：[T/R] 全部有限cutoff一致的响应下界；[N] 小质量schedule的障碍；
[E] 所选cutoff的full有限频带实验；[O] dyadic选择预算及新颖性。

本轮不把有限实验晋级为渐近反例，不声称RH或零点比例改进。

## 1. 对象与主结论

固定 \(0<\sigma<1\)，置 \(a=1-\sigma,\ L=\log Y\)。
允许任意充分大实数 \(Y\)，任意有限整数 \(N\ge Y\)，不要求 \(N=O(Y)\)。
使用265的实际匹配Abel源、中心化测度 \(p,c,r=p+c\)，以及
\[
 S=A+B,\quad M=A-B,\quad\mu=M/S,\quad
 D=\|F_p\|_2^2+\|F_c\|_2^2,\quad
 J_4=\frac{\|F_{r*r*p}\|_2^2+\|F_{r*r*c}\|_2^2}{S^4D}.
 \tag{1}
\]
定义
\[
 a_n=\mathbf1_{n\le N}\Lambda(n)n^{-\sigma}e^{-n/Y},\qquad
 F(\xi)=\sum_n a_n n^{-i\xi},\quad
 C(\xi)=\int_1^N x^{-\sigma-i\xi}e^{-x/Y}\,dx ,
 \quad Q=\sum_n a_n^2,\quad Q_1=\sum_n n a_n^2.
 \tag{2}
\]
实际Fourier符号精确为
\[
 \widehat p=\Re F-A,\qquad \widehat c=B-\Re C,\qquad
 \widehat r=\Re F-M-\Re C .
 \tag{3}
\]
质量中心项 \(-M\) 在以下全部平均中保留。

### 定理269-A [T/R]

存在仅依赖 \(\sigma\) 的 \(K_\sigma,c_\sigma,Y_\sigma>0\)，使
对每个 \(Y\ge Y_\sigma\)、每个有限 \(N\ge Y\)，令
\(U=K_\sigma Y,\ I=[U,2U]\)，则实际full响应在这个正频带的贡献满足
\[
 \boxed{
 J_{4,I}\ge c_\sigma\frac{(Q+M^2)^2}{YLS^4}
 \ge c_\sigma\frac{L}{Y^3}.}
 \tag{4}
\]
这里 \(J_{4,I}\) 是(1)的Plancherel积分限制到单侧 \(I\)，不是对称双带；
故 \(J_4\ge J_{4,I}\)。常数一致于所有有限cutoff。

若 \(M\ne0\)，特别有
\[
 \frac{J_4}{\mu^4}
 \ge c_\sigma\frac{(Q+M^2)^2}{YL M^4}
 \ge c_\sigma\frac{Y^{1-4\sigma}L}{M^4}.
 \tag{5}
\]

## 2. 独立算术规模与Brownian分母 [T/R]

只用Chebyshev上界和Abel分块，可得
\[
 A\ll_\sigma Y^a,\quad B\asymp_\sigma Y^a,\quad
 \int\lambda\,d\alpha,\ \int\lambda\,d\beta\ll_\sigma Y^aL .
 \tag{6}
\]
例如prime的第 \(j=0,1\) 阶lag矩，在 \(n\asymp X\) 的贡献至多
\(C_\sigma X^a(\log(2X))^j e^{-cX/Y}\)；
小块用 \(a>0\) 作几何求和，大块用指数衰减。
正项可延伸到无穷作上界，因此(6)不依赖 \(\log N\)。

同样，由 \(\Lambda(n)^2\le\Lambda(n)\log n\) 得
\[
 Q_1\ll_\sigma Y^{2-2\sigma}L .
 \tag{7}
\]
这里所需指数是 \(2-2\sigma>0\)，没有用267中只对
\(\sigma<1/2\) 适用的 \(Q\) 上界或加权卷积链界。

定性PNT [R] 给 \(\vartheta(Y)-\vartheta(Y/2)\asymp Y\)。
仅保留 \(p\in(Y/2,Y]\) 的真正素数，使用
\((\log p)^2\ge(\log(Y/2))\log p\)，得到
\[
 Q\ge c_\sigma Y^{1-2\sigma}L,\qquad Q_1\le C_\sigma YQ .
 \tag{8}
\]
这不需要素数对相关或短区间PNT。

由正源Brownian恒等式
\[
 D=\tfrac12\iint\min(\lambda,\nu)
        \bigl(d\alpha(\lambda)d\alpha(\nu)+d\beta(\lambda)d\beta(\nu)\bigr)
 \tag{9}
\]
及 \(\min(\lambda,\nu)\le\lambda\)，式(6)给 \(D\ll_\sigma Y^{2a}L\)。
只保留连续源在 \([Y/2,Y]\) 的bulk则给反向下界，故
\[
 S\asymp_\sigma Y^a,\qquad D\asymp_\sigma S^2L .
 \tag{10}
\]
即使 \(N\) 远大于任何 \(Y\) 的幂也适用；没有用
\(\log N=O(\log Y)\) 代替所需一致矩界。

## 3. 保留零频中心项的均值下界 [T/R]

使用Montgomery--Vaughan的局部间距均值公式 [R]：
若 \(\lambda_j\) 是有限个互异实频率，
\(\delta_j=\min_{k\ne j}|\lambda_j-\lambda_k|>0\)，则
\[
 \int_V^{V+U}\left|\sum_j d_j e^{i\lambda_j t}\right|^2dt
 =U\sum_j|d_j|^2+
 O\left(\sum_j\frac{|d_j|^2}{\delta_j}\right).
 \tag{11}
\]
隐常数绝对，任意区间平移 \(V\) 只改变系数相位。
这里需要双侧误差公式，不能从267仅引用的均值上界推出。
出处为原论文Corollary2的(1.9)；本轮不需要最优Hilbert常数。

将(11)用于
\[
 f(\xi)=\Re F(\xi)-M
       =-M+\tfrac12\sum_n a_n(e^{i\xi\log n}+e^{-i\xi\log n}) .
 \tag{12}
\]
频率集是 \(\{0\}\cup\{\pm\log n:a_n>0\}\)。
同号不同整数的间距满足
\(\delta_{\pm\log n}\ge1/(n+1)\ge1/(2n)\)；
异号间距更大，而 \(\delta_0=\log2\)。
即使 \(M=0\)，也可保留零系数的0频率，估计不变。
于是
\[
 \int_U^{2U}f(\xi)^2d\xi
 =U(M^2+Q/2)+O(Q_1+M^2).
 \tag{13}
\]
这是针对实际系数的有限平均，不对任何未知零点作假设。

由(8)，先选择 \(K_\sigma\) 充分大，再取 \(Y\) 充分大，
当 \(U=K_\sigma Y\) 时可将误差吸收，得到
\[
 \int_U^{2U}f(\xi)^2d\xi\ge cU(Q+M^2).
 \tag{14}
\]
局部间距版是去掉cutoff长度 \(N\) 的关键；若只用全局最小间距，
误差会是 \(O(N(Q+M^2))\)，不能覆盖全部 \(N\ge Y\)。

连续lag密度 \(e^{a\lambda-e^\lambda/Y}\) 单峰且极大值 \(O_\sigma(Y^a)\)。
在 \([0,\log N]\) 限制后零延拓，BV总变差至多两倍极大值，故
\[
 |C(\xi)|\le C_\sigma Y^a/|\xi|,\qquad
 \int_U^{2U}|C(\xi)|^2d\xi\ll_\sigma Y^{2a}/U.
 \tag{15}
\]
两端跳跃均包含在该界内。由(8)，
\[
 \frac{Y^{2a}/U}{UQ}\ll_\sigma\frac1{YL}\longrightarrow0.
 \tag{16}
\]
对 \(f-\Re C=\widehat r\) 使用 \(L^2\) 反三角不等式，得
\[
 \int_U^{2U}|\widehat r(\xi)|^2d\xi\ge c_\sigma U(Q+M^2).
 \tag{17}
\]
与此同时，\(B\asymp Y^a\) 与(15)保证
\(\widehat c(\xi)=B-\Re C(\xi)\ge B/2\) 于整个 \(I\)，最终一致成立。

## 4. 转回实际第四响应 [T]

Cauchy给
\[
 \int_U^{2U}|\widehat r|^4d\xi
 \ge U^{-1}\left(\int_U^{2U}|\widehat r|^2d\xi\right)^2
 \ge c_\sigma U(Q+M^2)^2 .
 \tag{18}
\]
保留最终continuum物理方向，得到
\[
 \begin{aligned}
 J_{4,I}
 &=\frac1{S^4D}\frac1{2\pi}\int_I
    \frac{|\widehat r|^4(|\widehat p|^2+|\widehat c|^2)}{\xi^2}d\xi\\
 &\ge \frac{B^2}{32\pi U^2S^4D}\int_I|\widehat r|^4d\xi
 \ge c_\sigma\frac{(Q+M^2)^2}{YLS^4}.
 \end{aligned}
 \tag{19}
\]
最后用(8)、(10)，所得幂次是
\(Y^{2-4\sigma}L^2/(Y\cdot L\cdot Y^{4-4\sigma})=L/Y^3\)。
除以 \(\mu^4=M^4/S^4\) 即得(5)。\(\square\)

这里没有用任意系数Bessel上界声称物理增益。
均值公式只证明真实离散项无法消失；BV控制真实连续项，
而最后continuum方向提供实际响应下界。

## 5. 对当前自由cutoff路线的必要门槛 [N/O]

若某条实际schedule满足 \(J_4\le C\mu^4\)、\(M\ne0\)，则必须
\[
 |M|\ge c_{\sigma,C}Y^{1/4-\sigma}L^{1/4}.
 \tag{20}
\]
特别任何满足 \(M=o(Y^{1/4-\sigma}L^{1/4})\) 且 \(M\ne0\) 的cofinal序列均使
\(J_4/\mu^4\to\infty\)。
此为实际源的严格障碍条件，不是已经证明存在这样的dyadic序列。

268的两端选择只保证 \(|M|\gg Y^{-\sigma}L\)，其保证尺度与(20)之比为
\[
 \frac{Y^{-\sigma}L}{Y^{1/4-\sigma}L^{1/4}}
 =Y^{-1/4}L^{3/4}\longrightarrow0 .
 \tag{21}
\]
两个下界之间的差距不等于实际质量违反(20)：
268没有给所选质量的同阶上界，故不能据(21)直接停止该schedule。
本轮 \(\sigma=1/4\) 的必要条件为 \(|M|\gg L^{1/4}\)。

当 \(Y\) 充分大，\(I=[K_\sigma Y,2K_\sigma Y]\subset[0,Y^2]\)。
因此本轮下界确实作用于268剩余频带，不与其已闭合的高频尾冲突。
262的孤立单原子证明在 \(N\asymp Y\) 只给 \(Y^{-9}L^{-1}\) 级下界；
本轮通过实际bulk离散项提高到 \(Y^{-3}L\)，并删除了cutoff上界。
该改进依赖额外的均值公式与bulk PNT，不将其描述为旧证明的无成本加强。

## 6. 所选实际cutoff的full有限频带实验 [E]

运行 `python -B scripts/prime_jump_full_response_probe.py --max-m 12`。
\(\sigma=1/4\)，沿268两个端点的浮点最大绝对质量选择：

| \(m\) | \(N\) | \(M\) | \(D/(LS^2)\) | \(J_{4,\le128}/\mu^4\) |
|---:|---:|---:|---:|---:|
| 4 | 16 | -0.807611 | 0.119502 | 0.696582 |
| 6 | 66 | -0.969307 | 0.136548 | 1.600928 |
| 8 | 256 | -1.010156 | 0.152532 | 6.742319 |
| 10 | 1030 | -0.986281 | 0.167300 | 27.816065 |
| 12 | 4098 | -0.271022 | 0.179088 | 24429.067048 |

\(D\) 独立用prime min-kernel排序公式与连续尾平方积分计算，
不是用同一有限频带来近似完整分母。
中心化使用 \(\cos x-1=-2\sin^2(x/2)\)，先合并 \(p+c\) 再取四次方。
粗细Gaussian相对差不超过 \(1.69\cdot10^{-13}\)，30个连续项特殊函数抽样
的scaled误差不超过 \(1.75\cdot10^{-15}\)。
最小例 \(m=4,T=1\) 另用50位独立直接系数和自适应完整积分复算，
相对差 \(1.78\cdot10^{-14}\)。
这些不是认证区间；\(m=12\) 的大比值受到小质量分母影响，
不证明渐近无界，也不是定理(4)的数值认证。

## 7. 依赖、删除与文献

- \(0<\sigma<1\)：用于质量/lag矩及 \(Q_1\) 的幂级求和；\(\sigma=1\) 不由本证明覆盖。
- 真实prime bulk：[R] 定性PNT给(8)，只用单素数质量，不需要素数对猜想。
- 原子频率与局部间距：[R/T] 给(13)；一般密集谱若无加权间距预算，证明失效。
- 连续源正bulk与BV：分别给最后方向的下界及(16)；若背景具有同样的原子，
  如取完全相同的正原子源 \(\beta=\alpha\)，则 \(r=0\)，不能保留(4)。
- 中心项：保留为0频率的系数 \(-M\)；删除它会估计错误的物理对象。
- \(N<\infty\)：外部均值应用始终有限；虽常数一致，没有在本篇自动宣称无限源版本。
- 条件性mass-only接口仍是256；Gamma-complete、一般复L系数与上同调桥梁另证。

[R] H. L. Montgomery and R. C. Vaughan, *Hilbert's Inequality*,
J. London Math. Soc. (2) 8 (1974), 73--82，
[正式论文DOI](https://doi.org/10.1112/jlms/s2-8.1.73)、
[作者存档原文，Theorem2/Corollary2](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)。
本轮核验局部间距公式(1.9)而非仅普通Dirichlet多项式上界；不主张新的均值定理。
定性PNT使用263已核验来源。新颖性与外部同行评审仍[O]。

内部复核记录：两份独立只读审计重建并通过加权局部间距、
所有有限 \(N\) 的矩界、BV端点、单带 \(32\pi\) 因子及260--268的物理归一化。
已补明(20)后取商的cofinal序列必须为非零质量项。
新增full响应探针另以50位小例复核；有限大比值不作为渐近停止证书。
