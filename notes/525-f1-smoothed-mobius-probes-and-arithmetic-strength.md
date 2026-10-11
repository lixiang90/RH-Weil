# 525. 平滑Möbius探针、零质量与临界算术强度

2026-10-12。[T/R] 接续[518](518-f1-quantitative-mellin-division-and-mobius-source.md)、
[519](519-f1-closed-source-image-and-degree-moments.md)、
[521](521-f1-moving-source-correction-and-uniform-resolvent.md)与
[522](522-f1-optimal-centered-growth-and-rh-equivalence.md)。
本稿把原Möbius源的原点抵消与实际修正所需的算术强度分开核算：
无条件支付一般反演函数的可积性、零积分和截断质量；
证明全部平滑测试函数的临界估计与RH等价，并保留固定探针取消零点的盲点。
这些是范围和强度的识别，没有取得新的RH证明、无零区域或零点比例。

## 1. 同一原空间上的实际Möbius函数

仍用405的复化空间 \(\mathcal S_{\exp,\mathbb C}\)，记
\[
 P_m(f)=\max_{0\le N,j\le m}\sup_t e^{N|t|}|f^{(j)}(t)|,
 \qquad M_f(s)=\int_{\mathbb R}e^{st}f(t)dt.
\]
对任何f及r>0定义
\[
 T_f(r)=\frac12\sum_{n\ge1}\mu(n)f(\log(nr)),\qquad
 W_f(x)=T_f(1/x)=\frac12\sum_{n\ge1}\mu(n)f(\log(n/x)).       \tag{1}
\]
每个正r上的和及所有Euler导数绝对局部一致收敛。
T在r趋于无穷时连同普通导数均快速衰减；原点处尚不能称为合法Schwartz源。
若f紧支于[-R,R]，则W只对 \(xe^{-R}\le n\le xe^R\) 求和。

在 \(\Re s>1\)，绝对换序给
\[
 \boxed{\int_0^\infty W_f(x)x^{-s-1}dx
       =\int_0^\infty T_f(r)r^{s-1}dr
       =\frac{M_f(s)}{2\zeta(s)}=:G_f(s).}                 \tag{2}
\]
实际Dirichlet系数及原换序范围见
[NIST DLMF 27.4.5](https://dlmf.nist.gov/27.4.E5)。
一般反演类型见[NIST DLMF 27.5.7](https://dlmf.nist.gov/27.5.E7)；
本仓库518另已支付(1)的因子2、正实局部收敛与逐点双和重建。

中心化平移 \(V_af(t)=e^{-a/2}f(t-a)\) 在此实际算子上满足
\[
 T_{V_af}(r)=e^{-a/2}T_f(e^{-a}r),\qquad
 W_{V_af}(x)=e^{-a/2}W_f(e^ax).                              \tag{3}
\]
这些恒等式不预设T已经进入原合法源空间。
对 \(f\in I=E(\mathscr S_{e,0})\)，518–519才进一步证明T为唯一合法源；
准入等价于Mf在每个非平凡零点ρ处消去全部 \(m_\rho\) 阶jets。

## 2. 无条件全族界与实际零积分

直接对(1)取绝对值，分n≤x与n>x，得到对x≥1、j≥0
\[
 |(x\partial_x)^jW_f(x)|\le C_jxP_{\max(2,j)}(f).           \tag{4}
\]
这里使用 \(|f^{(j)}(\log(n/x))|\le p_{2,j}(f)
\min((n/x)^2,(n/x)^{-2})\)。此界尚没有利用Möbius的符号抵消。

令 \(M(u)=\sum_{n\le u}\mu(n)\)。Stieltjes分部积分严格给
\[
 W_f(x)=-\frac12\int_1^\infty M(u)f'(\log(u/x))\frac{du}{u}.\tag{5}
\]
起点取第一个跳点之前，M(1−)=0；大端边界由f的指数衰减为零。
积分绝对收敛，没有遗漏常数项。

[NIST DLMF 27.11.12](https://dlmf.nist.gov/27.11.E12)给无条件经典界
\[
 M(u)=O\bigl(u e^{-c\sqrt{\log u}}\bigr),\qquad c>0.        \tag{6}
\]
这里仅采用此已核对的界，不将其称为当前最优界。
在(5)令 \(t=\log(u/x)\)。对x≥2，中段
\(|t|\le\frac12\log x\) 有 \(u\ge\sqrt x\)，所以
\(|M(u)|/u\le C e^{-c\sqrt{\log x}/\sqrt2}\)；
\(\int e^t|f'(t)|dt\) 由 \(p_{2,1}\) 控制。
两尾改用 \(|M(u)|\le u\) 和 \(|f'|\le p_{2,1}e^{-2|t|}\)，
总贡献至多 \(Cp_{2,1}x^{1/2}\)。缩小正数c、调整常数后，得到
\[
 \boxed{|(x\partial_x)^jW_f(x)|
 \le C_jx e^{-c_1\sqrt{\log x}}P_{\max(2,j+1)}(f),
 \quad j\ge0,\quad x\ge2.}                                \tag{7}
\]
常数不依赖f或x。高阶使用
\((x\partial_x)^jW_f=(-1)^jW_{D^jf}\)，并对 \(f^{(j+1)}\) 重复(5)。

取j=0及r=1/x，(7)给
\[
 |T_f(r)|\le Cr^{-1}e^{-c_1\sqrt{\log(1/r)}}P_2(f),
 \qquad 0<r\le1/2.                                       \tag{8}
\]
该界在原点可积，无穷端已有快速衰减，故一般T属于 \(L^1(0,\infty)\)。
在(2)令实s从右趋于1，原点用(8)、大端用Schwartz界支配收敛，得
\[
 \boxed{\int_0^\infty T_f(r)dr=G_f(1)=0.}                  \tag{9}
\]
ζ在1的极使G在1为零；没有在s=1交换原Möbius和与积分。
那个绝对双和通常因 \(\sum 1/n\) 发散。零积分也不等于原点平滑准入。

## 3. 截断质量可以补偿，但不自动支付目标误差

固定光滑χ，在0邻域为0、在[1,∞)为1，并令 \(\chi_\delta(r)=\chi(r/\delta)\)。
由(8)，对充分小的δ>0有
\[
 \left|\int_0^\infty(1-\chi_\delta(r))T_f(r)dr\right|
 \le CP_2(f)(1+\sqrt{\log(1/\delta)})
                   e^{-c_2\sqrt{\log(1/\delta)}}.          \tag{10}
\]
这是 \(\int_Y^\infty e^{-c\sqrt u}du
 =2e^{-c\sqrt Y}(\sqrt Y/c+1/c^2)\) 的直接应用。
将切断函数偶延拓，再用一个固定、远离0且实积分非零的偶紧支函数补偿质量，
可得到原空间 \(\mathscr S_{e,0}\) 中的真实源。

若另有全族估计 \(|T_f(r)|\le CP_m(f)r^{-c}\)、c<1，
相应质量损失为 \(CP_m(f)\delta^{1-c}\)。
例如临界 \(c=1/2+\varepsilon<1\) 给 \(\delta^{1/2-\varepsilon}\)，
但其算术前提要按下一节核对。
质量系数已支付，E作用后的 \(P_n\) 残差还需保留cutoff导数成本和联合相消；
不可从(10)直接宣称完成522的SC合同。
原点flat切断族的严格无条件障碍与有限Taylor修复，见
[524](524-f1-mobius-cutoff-taylor-obstruction-and-repair.md)。

## 4. 全平滑族的临界估计与RH等价

设 \(b=\sup_\rho\Re\rho\in[1/2,1]\)，固定c>b及j≥0。
521的Euler锚点和无零Harnack链，给固定实部条带上1/ζ的全高度多项式界。
此界常数依赖离零点边界的固定间隙，不对c=b声称同样结果。
Mf在每个固定实部条带沿虚轴任意阶快速衰减，其常数由f的有限个 \(P_m\) 控制。
具体地，选定固定初始实部 \(\sigma_0>\max(c,1)\)。
若在 \(c\le\sigma\le\sigma_0\) 带内
\(|1/\zeta(\sigma+iT)|\le C(1+|T|)^L\)，
先取整数 \(q>L+j+2\)，再取
\(m\ge\max(q,\lceil\sigma_0\rceil+1,2)\)。
分部积分在整带内统一给
\(|M_f(\sigma+iT)|\le C_q(1+|T|)^{-q}P_m(f)\)，
所以插入s的j次幂后，积分由 \((1+|T|)^{L+j-q}\) 支配并绝对收敛。
从初始实部σ0将(2)的逆Mellin线移到c，即得
\[
 W_f(x)=\frac1{2\pi i}\int_{c-i\infty}^{c+i\infty}G_f(s)x^sds.
                                                                    \tag{11}
\]
固定带内的界支付水平边；ζ在1的极只是1/ζ的零，没有经过新的极。
插入s的j次幂，仍可由选择充分高的分部积分阶数保持绝对收敛。
因此存在固定m及C，使
\[
 |(x\partial_x)^jW_f(x)|\le Cx^cP_m(f),
 \quad \forall f\in\mathcal S_{\exp,\mathbb C},\quad x\ge1.\tag{12}
\]
m、C依赖c与j，不能随f或x变化。

反向直接使用(2)的原积分。若给定σ，对全部紧支光滑f有
\(W_f(x)=O_f(x^\sigma)\)，则x→0端任意快，大x端满足该界，
故原积分在 \(\Re s>\sigma\) 全纯。
若该半平面有ζ零点ρ，则Mf必须消掉其完整 \(m_\rho\) 阶。
但对任何指定ρ，足够窄的非负紧支f满足Mf(ρ)≠0，产生矛盾。
因此全部非平凡零点满足Reρ≤σ。这一步甚至不需要全族统一常数。

结合正向(12)和函数方程对称，得到明确合同
\[
 \boxed{\mathrm{RH}\iff
 \forall\varepsilon>0\ \forall j\in\mathbb N_0\ \exists m\in\mathbb N,C>0\quad
 \forall f\in\mathcal S_{\exp,\mathbb C}\ \forall x\ge1:
 |(x\partial_x)^jW_f(x)|\le Cx^{1/2+\varepsilon}P_m(f).}     \tag{13}
\]
反向j=0足够。固定 \(P_m\) 的量词是实际修正路线所需的统一控制。
这个等价没有证明右侧的独立算术估计，也没有用不加权Mertens的unsmoothing。
由(3)，正时间的相应中心化指数为 \(b-1/2\)；
负时间还必须保留Fourier—sharp与原点Taylor数据，不能只计算正时间质量。

(5)另给带范围的转移：如果已知 \(|M(u)|\le Cu^c\)、c>0，
则 \(|W_f(x)|\le C'x^c\int e^{ct}|f'(t)|dt\)，
其常数由任意固定N>c的 \(p_{N,1}\) 控制。
若将f改成随x变尖的阶跃近似，导数半范数也会增加；
忽略这一成本就不能把(12)当作同样的不加权Mertens估计。

## 5. 固定非负紧支探针仍可取消完整零点重数

对单个f，令 \(\nu_\rho=\operatorname{ord}_\rho M_f\)。
G在ρ处实际剩余极阶是
\[
 \max(m_\rho-\nu_\rho,0).                                  \tag{14}
\]
只要它大于0，任何σ<Reρ的 \(W_f=O(x^\sigma)\) 都不可能，
否则上一节的原积分全纯性与该极冲突。
但若Mf已消掉完整mρ阶，这个探针对ρ没有相同的检测能力。

非负性不能排除这种盲点。给定非实ρ=β+iγ，选择足够窄的非负紧支g，
使其支集内 \(\cos(\gamma t)>0\)，从而Mg(ρ)≠0。
设 \(a=\pi/|\gamma|\)、\(c=e^{-a\beta}>0\)，定义
\[
 f=\sum_{j=0}^{m_\rho}\binom{m_\rho}{j}c^j\tau_{ja}g,
 \qquad M_f(s)=M_g(s)(1+ce^{as})^{m_\rho}.                 \tag{15}
\]
f仍实非负且紧支。括号在ρ及其共轭处为简单零点，导数为−a，
因此(15)恰好取消这两个零点的全部mρ阶。
这是对任何待检测零点的条件构造，不声称离线零点已经存在。
不能仅从“一个固定非负bump”的有限观测推出它不会隐藏离线零点。

相应的一手文献范围可见
[Báez-Duarte, *Möbius-convolutions and the Riemann hypothesis*, arXiv:math/0504402v1](https://arxiv.org/pdf/math/0504402)，
PDF6–7 Theorem3.1：固定探针的反向要保留Mellin取消条件，增加非消失准入才成为RH判据。
其算子是 \(\sum_{n\le x}\mu(n)/n\) 的卷积，本稿未将它与(1)混为同一算子。
式(14)–(15)在我们固定空间中独立支付完整重数。

## 6. 单个Gaussian目标的无盲点判据

取目标函数
\[
 f_G(t)=e^{-t^2},\qquad M_{f_G}(s)=\sqrt\pi e^{s^2/4}\ne0.  \tag{16}
\]
它属于Sexp，并在每个ζ零点处均无Mellin取消。
于是对这个单个f，已经有
\[
 \boxed{\mathrm{RH}\iff
 \forall\varepsilon>0\ \exists C_\varepsilon\ \forall x\ge1:
 |W_{f_G}(x)|\le C_\varepsilon x^{1/2+\varepsilon}.}        \tag{17}
\]
反向由(2)原积分在 \(\Re s>1/2\) 的全纯延拓排除右侧零点，
再由函数方程排除左侧零点。
正向用521的固定gap多项式倒数界，结合
\(|M_{f_G}(\sigma+iT)|=\sqrt\pi e^{(\sigma^2-T^2)/4}\)，
即可将逆Mellin轮廓移到 \(\sigma=1/2+\varepsilon\)。
跨过ζ在1的极只遇到G的零，不产生留数。

端点不能与(17)混同。如果进一步有 \(W_{f_G}(x)=O(x^{1/2})\)，
则在 \(s=1/2+\eta+i\gamma\)、η→0+，(2)的大x积分至多 \(O(1/\eta)\)，
小x积分局部有界。因此G在临界线上的极最多简单，
这个端点前提蕴含RH及所有非平凡零点简单。
本稿没有证明端点界，也不把“RH加简单性”声称为这个端点界的充分条件。
一手文献亦将类似端点与简单性另列于Báez-Duarte PDF7 Theorem4.1。

## 7. 实际Gaussian源与目标Gaussian的区别

405的真实Gaussian源为
\[
 \theta_0(r)=\pi r^2(\pi r^2-3/2)e^{-\pi r^2},\qquad
 h_0=E\theta_0,\qquad M_{h_0}(s)=\xi(s)/2.
\]
它和(16)是不同目标。h0已消掉全部非平凡零点jets，所以518严格给
\[
 T_{h_0}(r)=\theta_0(r)=-\frac{3\pi}{2}r^2+O(r^4),\qquad
 W_{h_0}(x)=-\frac{3\pi}{2}x^{-2}+O(x^{-4}).                \tag{18}
\]
这是无条件的实际源重建，不能为一般f的临界Möbius抵消提供证据。
其centered scaling第2k个Taylor系数准确乘 \(e^{-(2k+1/2)a}\)。
负时间不能删掉这些数据，只因原点质量可以补偿就把源改成flat。
相关负时间反例及修复范围已由[524](524-f1-mobius-cutoff-taylor-obstruction-and-repair.md)单独支付。

## 8. 已付清的范围

(7)–(10)给一般原始T的无条件全族半范数界、真实零积分与截断质量成本。
(13)、(17)识别临界输入的RH强度，(15)保留固定紧支探针的全重数盲点。
合法质量补偿之后的实际E残差、原点Taylor修复和独立算术符号，仍须另外证明。
有限Möbius求和或Gaussian积分测试可以核对公式和截尾，
不能证明全x、全部f和固定m的量词，也不能认证新无零区域或RH。
