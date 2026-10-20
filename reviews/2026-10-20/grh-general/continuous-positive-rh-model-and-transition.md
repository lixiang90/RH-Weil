# 连续正 primitive／g-integer 测度的非空 RH 类及精确相变

2026-10-20，独立原稿，供 root 另行逆审和消费。本稿只写本文件，不更改 Goal、STATE、
cadence 或 Git。按新用户问题，检验的新增内容是**连续正 primitive 与连续 g-integer
分布也可有非空中心线零点**，并与同一正测度族中的离线例直接比较。
不声明文献首创，不把有限零点模型外推为经典 Gamma／实际 ζ 的结果。

已恢复 AGENTS、goals/README、STATE、check/show、G20261014、C024、战略、宏观前沿和
561／root 收据／direct-Fourier 停止范围。旧 C024 已完成，561 中的离线段是输入；
本稿不续其预算、不把恢复和旧结果重复计轮。实际 ζ 的强旧链 542＋555→557 的 whole
4/5 与成长 core／完整 Ξ 缺口均不受本稿改变。

## 1. 对象、量词和结论

固定实参数

\[
 0<c\le\tfrac12,\qquad
 Z_c(s)=1+\frac{c}{s(s-1)},\qquad
 X_c(s)=s(s-1)Z_c(s)=s^2-s+c.
 \tag{1}
\]

在对数坐标 \(u\ge0\) 上构造正局部有限 Borel 测度 \(P_c,\Pi_c,M_c\)，并证明

\[
 \Pi_c=\sum_{k\ge1}\frac1k(T_k)_*P_c,
 \quad T_k(u)=ku,
 \quad M_c=\exp_*\Pi_c,
 \quad \int_0^\infty e^{-su}\,dM_c(u)=Z_c(s)\quad(\Re s>1).
 \tag{2}
\]

这里 \(P_c\) 是 primitive g-prime 测度，\(\Pi_c\) 是完整 prime-power 测度，
\(M_c\) 是含单位原子的 g-integer 测度。重复指标 \(k=1,2,\ldots\) 只编码幂；
未输入普通素数的分布、唯一分解或 \(\log n\) 的特殊位置。
这是正测度型／分布型 generalized Euler 系统；不将连续测度称为经典离散 Beurling
prime 序列。

同一族有如下**精确**分界：

| 参数 | \(Z_c\) 的全部零点 | 完整中心化 Weil 型 |
|---|---|---|
| \(0<c<1/4\) | \(1/2\pm\sqrt{1/4-c}\)，离中心线 | 在原 \(C_c^\infty(\mathbb R)\) 上有严格负方向 |
| \(c=1/4\) | \(s=1/2\) 二重零点 | 正半定，谱迹测度 \(2\delta_0\) |
| \(1/4<c\le1/2\) | \(1/2\pm i\sqrt{c-1/4}\) | 正半定，谱测度 \(\delta_\tau+\delta_{-\tau}\) |

因此本例不是“无零点所以真空成立的 RH”。在正向段，至少有一个非空中心零点对，
或分界点的二重中心零点；primitive 和 integer 两侧的非单位部分始终是连续正密度。

## 2. 真正的 positive primitive：不能把正 \(\Pi\) 免费当作正 \(P\)

令 \(\alpha+\beta=1\)、\(\alpha\beta=c\)，取 \(\beta=\overline\alpha\) 于 \(c\ge1/4\)。设

\[
 A_m=1-\alpha^m-\beta^m\quad(m\ge2),\qquad
 C_m=\sum_{k\ge1}k^{-m-1},\qquad
 p_c(u)=\frac1u\sum_{m\ge2}\frac{A_m u^m}{m!C_m}.
 \tag{3}
\]

\(A_1=0\)。若 \(0<c<1/4\)，则 \(0<\alpha,\beta<1\)，所以 \(0<A_m<1\)。
若 \(1/4\le c\le1/2\)，则 \(|\alpha|^2=|\beta|^2=c\)，于是

\[
 A_2=2c>0,\qquad
 A_m=1-2\Re(\alpha^m)\ge1-2c^{m/2}>0\quad(m\ge3).
 \tag{4}
\]

注意新段的 \(A_m\) 不再都小于 1，例如 \(c=1/2\) 时 \(A_3=3/2\)。统一安全界是
\(0<A_m\le3\)，以及 \(C_m\ge1\)。由此级数局部一致收敛，且

\[
 p_c(u)>0\quad(u>0),\qquad
 p_c(u)=\frac{c}{C_2}u+O_c(u^2)\quad(u\downarrow0),\qquad
 p_c(u)\le\frac{3(e^u-1-u)}u.
 \tag{5}
\]

所以 \(dP_c=p_c(u)du\) 在 \([0,\infty)\) 局部有限，且对每个 \(\sigma>1\)，
\(\int e^{-\sigma u}dP_c<\infty\)。没有 \(u=0\) 的 primitive 原子。

推前 \((T_k)_*P_c\) 的密度为 \(k^{-1}p_c(u/k)\)，再乘 Euler 权 \(1/k\)，得到

\[
 \begin{aligned}
 \sum_{k\ge1}\frac1{k^2}p_c(u/k)
 &=\frac1u\sum_{m\ge2}\frac{A_m u^m}{m!C_m}\sum_{k\ge1}k^{-m-1}\\
 &=\frac{e^u+1-e^{\alpha u}-e^{\beta u}}u=:q_c(u).
 \end{aligned}
 \tag{6}
\]

全部项非负，交换由 Tonelli 支付，且式(5)支付局部有限性和右半平面指数权。
因此 \(d\Pi_c=q_c(u)du\) 的全部重复幂确实来自正 \(P_c\)。在正向段也有直接核对：

\[
 q_c(u)=\frac{e^u+1-2e^{u/2}\cos(\tau u)}u>0,
 \qquad \tau=\sqrt{c-1/4},\quad u>0.
 \tag{7}
\]

## 3. Euler／Mellin、计数正则性及连续性全部闭合

对每个 \(\Re s>1\)，有

\[
 \begin{aligned}
 I_c(s)&=\int_0^\infty e^{-su}q_c(u)du\\
 &=\log\frac{(s-\alpha)(s-\beta)}{s(s-1)}=\log Z_c(s).
 \end{aligned}
 \tag{8}
\]

可直接对积分求 \(s\) 导数验证等式，再用实 \(s\to+\infty\) 两边趋零固定常数和分支。
求导及复数延拓由 \(\Re s>1\) 的绝对收敛支付；\(Z_c\) 在此半平面无零极点。

定义正卷积指数

\[
 M_c=\delta_0+\sum_{j\ge1}\frac{\Pi_c^{*j}}{j!}.
 \tag{9}
\]

对每个 \(\sigma>1\)，加权总质量恰为
\(\sum_j(\int e^{-\sigma u}d\Pi_c)^j/j!=\exp I_c(\sigma)<\infty\)。
故式(9)是合法正局部有限测度，而非仅形式级数。其 Laplace 变换由式(8)为 \(Z_c\)。
加权有限测度的 Laplace 唯一性再给

\[
 dM_c(u)=\delta_0+c(e^u-1)du.
 \tag{10}
\]

换回物理变量 \(x=e^u\)：

\[
 d\mathcal N_c(x)=\delta_1+c(1-x^{-1})\mathbf1_{x>1}dx,
 \qquad
 N_c(x)=1+c(x-1-\log x)=cx+O_c(\log x).
 \tag{11}
\]

因此 primitive 在每个 \(u>0\) 的开区间都有正质量，integer 测度除单位原子外也在
每个 \(x>1\) 的开区间有正质量；两者均非 lattice 点列。式(11)的正则性同时存在于
离线段和 RH 段，不能单凭此强计数余项区分零点位置。

## 4. 原测试域、反射、范数和完整极点缺陷

对乘法测试函数 \(f\in C_c^\infty((0,\infty))\)，固定

\[
 (Uf)(t)=e^{t/2}f(e^t),\qquad f^\sharp(x)=x^{-1}\overline{f(x^{-1})}.
 \tag{12}
\]

则 \(U:C_c^\infty((0,\infty))\to C_c^\infty(\mathbb R)\) 双射，且
\(U(f^\sharp)(t)=\overline{Uf(-t)}\)。在 Hilbert 范数上，\(U:L^2(dx)\to L^2(dt)\)
为酉映射。乘法卷积使用 \(dy/y\)，在 \(U\) 下正好变为普通加法卷积；
这只用于固定反射／卷积约定，不声称得到了实际 ζ 的 Weil norm 比较。

下文直接在完整 \(C_c^\infty(\mathbb R)\) 上写 \(g^*(t)=\overline{g(-t)}\)，定义线性
平衡泛函和二次型

\[
 \begin{aligned}
 W_c(h)&=\int_\mathbb R
 \left[2\cosh(t/2)-|t|e^{-|t|/2}q_c(|t|)\right]h(t)dt,\\
 Q_c(g)&=W_c(g*g^*).
 \end{aligned}
 \tag{13}
\]

\(t=0\) 处按连续延拓。两项分别是完整 \(s=0,1\) 极点背景与完整 prime-power 项；
没有丢 proper powers，也没有丢 pole。此模型的 archimedean Gamma 项为零，
**不能替换成经典 \(\pi^{-s/2}\Gamma(s/2)\)**。极点背景是两个 Mellin 评价，有限秩；
代入式(6)给出精确相消

\[
 W_c(h)=
 \begin{cases}
 \displaystyle\int_\mathbb R 2\cosh(rt)h(t)dt,&0<c<1/4,\quad r=\sqrt{1/4-c},\\
 \displaystyle\int_\mathbb R 2h(t)dt,&c=1/4,\\
 \displaystyle\int_\mathbb R 2\cos(\tau t)h(t)dt,&1/4<c\le1/2.
 \end{cases}
 \tag{14}
\]

这里正性是 \(W_c(g*g^*)\ge0\)，不是要求线性 \(W_c(h)\) 对所有复 \(h\) 非负。

## 5. 非空连续 RH 类的独立平方和及自伴实现

固定 Fourier 约定 \(\widehat g(\xi)=\int g(t)e^{-i\xi t}dt\)。由式(14)，
对每个 \(g\in C_c^\infty(\mathbb R)\) 和 \(1/4<c\le1/2\)，

\[
 Q_c(g)=|\widehat g(\tau)|^2+|\widehat g(-\tau)|^2
 =\int|\widehat g(\xi)|^2d\sigma_c(\xi),
 \quad \sigma_c=\delta_\tau+\delta_{-\tau}.
 \tag{15}
\]

这直接来自完整 arithmetic／pole 相消式，域为全 \(C_c^\infty\)，没有有限样本推全域。
\(c=1/4\) 时同一公式成为 \(Q_c(g)=2|\widehat g(0)|^2\)，\(\sigma_c=2\delta_0\)。
对离线段，取实奇函数 \(g(t)=t\phi(t)\)，其中非零非负偶 \(\phi\in C_c^\infty\)。
若 \(F_g(z)=\int g(t)e^{zt}dt\)，则

\[
 Q_c(g)=2\Re\{F_g(r)\overline{F_g(-r)}\}
 =-2F_g(r)^2<0.
 \tag{16}
\]

所以在本族上 \(Q_c\ge0\) **当且仅当** \(c\ge1/4\)，正是零点进入中心线的阈值。
值得区分：离线段 \(W_c\) 的物理密度 \(2\cosh(rt)\) 处处为正却不正定；
RH 段 \(2\cos(\tau t)\) 可取负值却卷积正定。普通测度正性与 Weil 正性不是一件事。

当 \(\tau>0\)，取 \(\mathcal H_c=\mathbb C^2\)、\(D_c=\operatorname{diag}(\tau,-\tau)\)，
在通常正内积上为有界自伴算子，且

\[
 X_c(1/2+iz)=\tau^2-z^2=-\det(zI-D_c),
 \qquad
 X_c(1/2+iz)=\tau^2
 \prod_{\gamma=\pm\tau}(1-z/\gamma)e^{z/\gamma}.
 \tag{17}
\]

没有隐藏零点、没有额外非消失的未知因子；谱权、零点重数、常数和指数因子都已固定。
\(\int(1+\xi^2)^{-1}d\sigma_c(\xi)<\infty\) 显然成立。

\(c=1/4\) 时应取 \(D_c=0\) 作用于 \(\mathbb C^2\)，此时
\(X_c(1/2+iz)=-z^2=-\det(zI-D_c)\)。必须显式列出零点因子 \(z^2\)，
因为原 canonical product 中的 \(1-z/\gamma\) 在 \(\gamma=0\) 无定义。

**重数接口不能省略。** 标量 \(L^2(\mathbb R,2\delta_0)\) 只有一维；其乘法算子通常
行列式只有一阶零点。原子权 2 在标量 \(L^2\) 中不自动成为本征值重数 2。
若要式(17)的行列式，必须使用带重数的谱空间 \(\bigoplus_\gamma\mathbb C^{m_\gamma}\)
或等价的 multiplicity 纤维直积分，并以谱迹测度 \(\operatorname{Tr}E_D=\sum m_\gamma
\delta_\gamma\) 对接零点重数。C3 的 GNS 实现和 C4 的谱行列式之间不能靠一句谱定理跳过此步。

## 6. 对 C1–C5 的确切检验价值

1. C1 与 C2 在整个 \(0<c\le1/2\) 成立：\(X_c\) 是 genus 0 实型自对偶多项式，
   \(X_c(1-s)=X_c(s)\)，所有零点在 \(0<\Re s<1\)，原 \(Z_c\) 只有两个有限极点。
   它们不区分两段。此处的有限零点 completion 不能支付经典 Gamma 或 \(T\log T\) 计数。
2. 修正为卷积二次型后的 C3 在本族恰于 \(c\ge1/4\) 成立，并有式(15)的全域平方和。
   因而该条件确能容纳具有非空 RH 类性质的连续 g-integer／primitive 测度。
3. C4 在正向段有精确有限维行列式实现；应补原子整数重数、中心零点因子和 multiplicity
   空间。离线段无法由自伴 \(D\) 产生同一零点；任意别的自伴算子不满足对象识别。
4. C5 的“最小本征值最终简单”等条件不是本族 RH 的必要条件：式(15)的 Gram 型在任意
   维数大于 3 的测试子空间上，零特征值重数至少为 \(\dim V-2\)。正性和 exact determinant
   可成立而此类简单性失败。若 C5 指另一个截断算子，须先给出该算子、域和 determinant
   对接；不能把有限截断的自伴性自动升级为式(17)。

“连续还是离散”须至少分两侧回答。本例的 arithmetic 侧 \(P_c,M_c\) 连续，而已识别的
零点谱为纯点。若坚持 C4 的全纯 canonical product 且非恒零，零点在有限区域只能离散，
其带重数计数测度自然纯点；连续 arithmetic 侧毫无矛盾。若要**谱侧**连续谱，必须另给
相对／正则化 determinant 或谱位移接口；普通整函数零点积不能把连续谱支持逐点当作零点。

## 7. 本稿的前件闭合和净后果

- **对象／域／norm：** \(P,\Pi,M\) 是 \([0,\infty)\) 正局部有限 Borel 测度，
  对每个 \(\sigma>1\) 有有限指数权总质量；\(Q_c\) 在全 \(C_c^\infty(\mathbb R)\) 上。
  \(U\) 的 domain/range 与 \(L^2(dx)\to L^2(dt)\) 范数在式(12)固定；不是 actual ζ 源费。
- **角色／符号：** \(P\to\Pi\) 包含真实 Jacobian \(k^{-2}\)，\(\Pi\to M\) 正卷积指数；
  pole 减完整 prime-power 的符号在式(13)固定；\(\sigma\) 是 zero-side，不能与 \(P,\Pi,M\) 混同。
- **源与成长量词：** 每个固定 \(0<c\le1/2\)、每个 \(u>0\)、每个 \(x\ge1\)、每个
  \(\Re s>1\)、全部复测试 \(g\in C_c^\infty\)。没有采样替全域或待付误差，且无成长逼近宣称。
- **付清依赖／误差：** 式(3)–(10)的正系数、Tonelli、指数权卷积质量、Laplace 唯一性；
  式(13)–(17)的完整 pole/prime-power 恒等式、平方和、全部零点与重数。均为自包含精确恒等式。
- **最强旧对照：** 561 已付 \(0<c<1/4\) 离线段。新增是同一合法连续正 primitive 族上
  \(1/4\le c\le1/2\) 的非空 RH 段、全域 Weil 平方和、谱行列式和精确分界；
  不是把旧离线结果重新标新，也不是只有空零点系统的形式存在性。
- **实际后果与限制：** 本稿排除“类 RH 必须普通整数梳／必须离散 arithmetic 分布”的必要性。
  它不给实际 ζ 新算术输入、经典 Gamma 平方和、成长 core／Ξ 识别，whole 强旧 4/5 不变。
  没有因此通过 G20261014 宏观完成门，也不声称此族外 \(c>1/2\) 的 primitive 符号已分类。
