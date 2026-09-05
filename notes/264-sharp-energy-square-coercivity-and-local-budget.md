# 264. 最优能量平方强制性与局部单一预算判据

日期：2026-09-05。路线：NCE-8 / B1u。
论文归属：Vaughan--Brownian response；本轮仅保存Markdown。

状态：[T] 紧支撑二阶/四阶能量的最优不等式；
[T] 260局部质量预算的单一四阶能量等价判据；
[T] 用实际二阶能量给出局部障碍的充分证书；
[E] 冻结dyadic全源数值；[O] 实际局部算术估计与全源signed transfer。
最优常数的内部证明不等于已认证文献新颖性；本文不证明RH或零点比例改善。

## 1. 能量平方的最优不等式

令 \(\zeta\) 是质量零的有限复测度，支撑于 \([-H,H]\)，其中 \(H>0\)。
这里的 \(\zeta\) 是discrepancy测度，不是Riemann zeta函数。
定义
\[
 F_\eta(t)=\eta((-\infty,t]),\qquad
 \mathcal E(\eta)=\|F_\eta\|_2^2
 =\frac1{2\pi}\int_{\mathbb R}
          \frac{|\widehat\eta(\xi)|^2}{\xi^2}\,d\xi,
 \tag{1}
\]
其中 \(\widehat\eta(\xi)=\int e^{-i\xi x}d\eta(x)\)，
只对零质量测度使用此式。紧支撑确保这里的primitive及卷积primitive属于 \(L^2\)。
置
\[
 E_1=\mathcal E(\zeta),\qquad E_2=\mathcal E(\zeta*\zeta).
 \tag{2}
\]

### 定理264-A [T]

有最优不等式
\[
 \boxed{E_2\ge E_1^2/H.}
 \tag{3}
\]
常数1可由 \(\zeta=c(\delta_{-H}-\delta_H)\)，\(c\ne0\)，精确取到。

证明：记 \(f=F_\zeta\)，并定义自相关
\[
 C(t)=\int f(u)\overline{f(u-t)}\,du=f*\check{\bar f}(t).
 \tag{4}
\]
这里check表示反射。\(f\) 支撑于 \([-H,H]\)，故
\(C\) 支撑于 \([-2H,2H]\)，且
\[
 C(0)=E_1,\quad C(2H)=0,\quad C(-t)=\overline{C(t)}.
 \tag{5}
\]
连续性来自 \(L^2\) 平移连续性。
分布意义下 \(f'=\zeta\)，所以
\[
 C''=-\zeta*\check{\bar\zeta},\qquad
 C'=-F_{\zeta*\check{\bar\zeta}}.
 \tag{6}
\]
导数 \(C'=\zeta*\check{\bar f}\) 属于 \(L^2\)，
因为有限测度与 \(L^2\) 函数的Young不等式适用。
因此 \(C\) 具有局部绝对连续代表；(6)中的积分常数由紧支撑定为0。

Fourier公式给
\[
 \|C'\|_2^2
 =\mathcal E(\zeta*\check{\bar\zeta})
 =\frac1{2\pi}\int\frac{|\widehat\zeta(\xi)|^4}{\xi^2}d\xi
 =E_2.
 \tag{7}
\]
虽然复测度时 \(C\) 不一定为实偶函数，(5)仍保证 \(|C'|^2\) 为偶函数。
于是
\[
 E_1^2=\left|\int_0^{2H}C'(t)dt\right|^2
 \le2H\int_0^{2H}|C'(t)|^2dt=H E_2.
 \tag{8}
\]
当 \(\zeta=c(\delta_{-H}-\delta_H)\) 时，
\(f=c{\bf1}_{[-H,H]}\)（忽略端点），
\(C(t)=|c|^2(2H-|t|)_+\)，
\(E_1=2H|c|^2,\ E_2=4H|c|^4\)，故取等。\(\square\)

复测度版本只推广这个基础能量引理；下文260的正源响应判据仍限制为实正通道。

### 推论264-B [T]：最优一阶矩证书

记 \(m_1=\int u\,d\zeta(u)\)，则
\[
 \boxed{
 E_1\ge\frac{|m_1|^2}{2H},\qquad
 E_2\ge\frac{|m_1|^4}{4H^3}.}
 \tag{9}
\]
证明：分部积分给 \(m_1=-\int_{-H}^H f(u)du\)，Cauchy给第一个不等式；
再用 (3) 得第二个。上述双端点测度使两式同时取等。\(\square\)

若只把 \(\zeta*\zeta\) 当一般零质量且零一阶矩测度作二次测试，
会得到较弱常数 \(3/16\)。式 (9) 保留了“同一测度自卷积”的结构，
把该常数提高为最优 \(1/4\)。

## 2. 接入260的局部响应

以下严格使用260的局部模型：
\(\alpha,\beta\ge0\) 为 \([-H,H]\) 上的有限实正测度，
\(A,B>0,\ K=A^2+B^2,\ S=A+B,\ M=A-B\ne0,\ 0<H<L/6\)。
physical lag为 \(L+u\)。令
\[
 \zeta=\alpha-(A/B)\beta,\qquad
 x=\frac{E_2}{LM^4},\quad y=\frac{E_1}{LM^2},\quad
 d=\frac D{LK},\quad
 R=\frac{J_{\rm loc}}{(M/S)^4}=\frac{P^2}{M^4D}.
 \tag{10}
\]
所有量均来自同一个局部模型；不能把full-source质量代入。
260的minimum kernel及扰动界给
\[
 \frac5{12}\le d\le\frac7{12},\qquad
 \left(\sqrt{\frac{3x}{8d}}-4\sqrt{\frac{2y}{d}}-4\right)_+^2
 \le R\le
 \left(\sqrt{\frac{11x}{16d}}+4\sqrt{\frac{2y}{d}}+4\right)^2.
 \tag{11}
\]
由264-A，
\[
 y^2\le(H/L)x\le x/6.
 \tag{12}
\]

### 定理264-C [T]：一致仿射比较

在上述全部局部模型中，有
\[
 \boxed{\frac{x}{8}-5500\le R\le100(x+1).}
 \tag{13}
\]
常数与 \(L,H,\alpha,\beta,M\) 无关；不宣称这两个比较常数最优。

证明：取
\[
 a_0=3/\sqrt{14},\quad A_0=\sqrt{33/20},\quad
 b_0=4\sqrt{24/5}\,6^{-1/4}.
\]
式 (11)--(12) 给
\[
 (a_0\sqrt x-b_0x^{1/4}-4)_+^2
 \le R\le(A_0\sqrt x+b_0x^{1/4}+4)^2.
 \tag{14}
\]
注意 \(b_0^2<32\)。上界使用三项平方和以及 \(\sqrt x\le(x+1)/2\)：
\[
 R\le3A_0^2x+96\sqrt x+48\le100(x+1).
 \tag{15}
\]
下界对非负 \(u,v\) 用
\((u-v)_+^2\ge u^2/2-v^2\)，并用 \(a_0^2/2\ge5/16\)，得
\[
 R\ge\frac5{16}x-64\sqrt x-32.
 \tag{16}
\]
再配平方
\[
 64\sqrt x\le\frac3{16}x+\frac{16384}{3},
\]
得到 \(R\ge x/8-16480/3\ge x/8-5500\)。\(\square\)

### 推论264-D [T]：单一四阶能量判据与二阶障碍证书

对任何满足局部假设的非零质量源族，
\[
 \boxed{J_{\rm loc}=O((M/S)^4)
 \quad\Longleftrightarrow\quad E_2=O(LM^4).}
 \tag{17}
\]
两者都自动迫使更强的二阶预算
\[
 E_1=O(M^2\sqrt{LH}),
 \tag{18}
\]
而不是原260中单独要求的 \(O(LM^2)\)。
例如 \(R\le C\) 时，(13)和(3)给
\[
 E_2\le(8C+44000)LM^4,\qquad
 E_1\le\sqrt{8C+44000}\,M^2\sqrt{LH}.
 \tag{19}
\]
又由 (13)，\(R\to\infty\) 当且仅当 \(x\to\infty\)。特别地
\[
 \boxed{\frac{E_1}{M^2\sqrt{LH}}\to\infty
 \quad\Longrightarrow\quad
 \frac{J_{\rm loc}}{(M/S)^4}\to\infty.}
 \tag{20}
\]
因为 (3)给 \(x\ge[E_1/(M^2\sqrt{LH})]^2\)。
二阶预算小并不能反推出四阶预算；(20)只是一个充分障碍证书。

后续266用显式光滑严格正源证明上述不充分性，即使 \(L\to\infty\) 仍成立；
同时给实际局部 \(E_1\ge c_\sigma Y^{-2\sigma}(\log Y)^2\) 的gap下界。
真实full-source signed transfer的无条件绝对改进及保留两份discrepancy的
四阶充分证书见265；它们没有自动闭合(22)的相对算术输入。

这是局部响应条件的严格简化，不是一个不需算术输入的Weil正性定理。
把 (17)命名为公理并不能替代对实际 \(E_2\) 的估计。

## 3. 算术矩接口和全源/局部的区别

固定 \(Y,N,L,H\)，在 \(\sigma\) 微分时冻结窗口及端点。
以physical lag写实际局部源的质量 \(A_H(\sigma),B_H(\sigma)\)，则
\[
 \int u\,d\zeta_H(u)
 =-B_H\,\partial_\sigma(A_H/B_H)
 =-\partial_\sigma M_H+(M_H/B_H)\partial_\sigma B_H.
 \tag{21}
\]
证明：\(-\partial_\sigma A_H=\int\lambda\,d\alpha_H\)，
连续项同理；\(\int d\zeta_H=0\) 消掉从 \(\lambda\) 到 \(u=\lambda-L\) 的平移。
这给一个无需未知零点的实际一阶矩测试，但它可能漏掉大量能量。

应用 (17)--(20) 必须先构造满足 \(L>6H\) 的局部源。
对全cutoff源，support为 \([0,\log N]\)，平移后的半宽至少 \((\log N)/2\)，
不能满足同一carrier分离条件。因此全源 \(E_1\) 数值不能直接代入 (20)。
基础能量不等式 (3)仍可用于全源，取 \(H=(\log N)/2\)，但响应判据不能自动跟随。

263已无条件排除小窗口的正源绝对相对tail证书。
从局部结果到全源的一个明确剩余输入组合为
\[
 E_{2,H}=O(LM_H^4),\qquad |M_H|=O(|M|),\qquad
 \|\mathbf P-\mathbf P_H\|=O(M^2\sqrt D),
 \tag{22}
\]
其中 \(\mathbf P=(F_{r*r*p},F_{r*r*c})\)，\(\mathbf P_H\) 为局部对应向量，
且最后两项用full-source \(M,D\)。
这里局部源须有 \(A_H,B_H>0\)。当 \(M_H\ne0\) 时，由 (17)得
\(\|\mathbf P_H\|=O(M_H^2\sqrt{D_H})\)；
若 \(M_H=0\)，(22)的第一项强迫 \(E_{2,H}=0\)，再由 (3)得
\(E_{1,H}=0\)，即 \(\zeta_H=0\)，于是平衡响应 \(\mathbf P_H=0\)。
正源限制使 \(D_H\le D\)，故 (22)确实推出full \(J_4=O(\mu^4)\)。
它仍是一组开放的实际算术输入 [O]，不因形式等价而成为RH证明。

特别地，在局部预算与质量匹配这两项已经成立时，三角不等式也给逆向蕴含：
若full \(\|\mathbf P\|=O(M^2\sqrt D)\)，则
\(\|\mathbf P-\mathbf P_H\|=O(M^2\sqrt D)\)。
所以剩余signed transfer此时与full预算等价；(22)是把待证估计分开的接口账本，
不是已获得更弱算术输入的证明。真正已完成的简化是局部模型中二阶预算不再独立。

## 4. 冻结dyadic实际数据 [E]

运行 scripts/dyadic_balanced_moment_probe.py，固定
\(\sigma=1/4,Y=2^m,N=\lfloor Y(\log Y)^2\rfloor\)。
这里 \(\zeta\) 为全cutoff的一侧平衡测度，不是上节的局部 \(\zeta_H\)。

| \(m\) | \(M\) | \(\int\lambda\,d\zeta\) | \(E_1/(LM^2)\) | 一阶矩Cauchy下界占 \(E_1\) 的比例 |
|---:|---:|---:|---:|---:|
| 3 | -0.615388 | 0.793421 | 0.387114 | 0.58559 |
| 8 | -0.750241 | 3.122857 | 0.824791 | 0.42229 |
| 12 | -0.754757 | 5.171457 | 1.454858 | 0.30902 |
| 16 | -0.755041 | 7.255253 | 3.112285 | 0.16822 |
| 18 | -0.755055 | 8.300742 | 4.898133 | 0.11285 |

最后一列为 \(|\int\lambda d\zeta|^2/((\log N)E_1)\)。
已检范围内一阶矩能捕捉的能量份额下降，不宣称渐近逃逸或 (20) 的前提成立。
6点/10点Gaussian求积相对差不超过 \(1.4\cdot10^{-13}\)；
本机longdouble仍只有52个显式尾数位，不提供interval认证。
双端点结构例和随机有理测度的精确检查见下一节；两种证据不能混淆。

## 5. 最小假设、删除审计和复算

基本不等式只用零质量、有限测度及已知支撑长度；复测度使用Hermitian自相关。
删除零质量后 \(F_\zeta\) 一般不属于 \(L^2\)；删除有限支撑尺度后，
放大支撑即可使 \(E_2/E_1^2\) 任意小，所以固定系数下界失效。
响应归约另需260的实正通道、同一局部参数与 \(L>6H\)；
删除carrier分离后不能继续引用260的双边估计。
\(M=0\) 时 (10)未定义，须直接使用平衡响应定理，不能约去零质量。

与部分Weil配置的接口仍为256的capture/Schur条件；
基本复测度引理可供Dirichlet/自守模型使用，但未证明它们的正源响应定理。
Gamma-complete和上同调桥梁仍独立开放。
没有以酉性、Weil完全正性或统一负指数作为未经证明的公理。

scripts/brownian_energy_square_audit.py 使用Fraction进行104案例、
1024个自相关斜率区间的独立精确检查：primitive与distance能量、
自卷积与Hermitian自相关能量、直接区间重叠计算的 \(\|C'\|_2^2\) 一致；
16个双端点案例达到等号。也检查 (9)，并有9例 \(m_1=0\) 而能量非零。
该脚本的原子样本为实有理测度；复测度范围由第1节解析证明覆盖，而非由这些样本认证。

独立推导及逆向复核检查最优常数、归一化、(13)的显式常数和局部量词。
自相关与Cauchy技巧是经典工具；本轮不宣称已排除同一不等式的文献先例。
下一轮只继续 (22) 中实际带符号算术输入，不通过扩写局部等价表述替代算术进展。
