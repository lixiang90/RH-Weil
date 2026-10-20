# 连续 arithmetic 与连续 spectral 混合：C4 的严格边界测试

2026-10-20，按 root 单独任务逆审。仅写本文件，不改 562、STATE、cadence，不提交 Git。
已读 README/STATE、check/show、G20261014、C025、当前战略与前沿，并核对连续模型原稿。
本稿是已付正族的概率对数混合直接推论，属于同一 C025 迭代，非另一数学轮。

**裁决：在下列范围限定和分支规范下 PASS。** 混合同时给连续正 primitive／integer
分布与连续正谱测度、自伴乘法算子；其完成对象有分支端点，不能作为标准整个零除子。
故这是较宽的 **spectral-positive RH-like 系统**，不是一个“整函数有连续中心线零点”的例子，
也不是满足完整 C1 后仍违反 C4 的反例：它在严格全域亚纯／整个规范下同时失败 C1。
本稿不付实际 ζ 的独立完整正性、成长 K/core 或 Ξ 识别。

## 1. 固定对象、测度与统一权界

固定

\[
 0<a<b\le\tfrac12,\qquad d=b-a,\qquad
 d\nu(\tau)=d^{-1}\mathbf1_{[a,b]}(\tau)d\tau,
 \quad c_\tau=\tfrac14+\tau^2\in(\tfrac14,\tfrac12].
\]

引用已自证的连续正族原稿中的精确对象

\[
 Z_\tau(s)=\frac{(s-\tfrac12)^2+\tau^2}{s(s-1)},\qquad
 dP_\tau(u)=p_\tau(u)du,\quad d\Pi_\tau(u)=q_\tau(u)du,
\]

\[
 \Pi_\tau=\sum_{k\ge1}\frac1k(T_k)_*P_\tau,\quad T_k(u)=ku,
 \qquad
 q_\tau(u)=\frac{e^u+1-2e^{u/2}\cos(\tau u)}u>0\quad(u>0).
 \tag{1}
\]

原稿的正系数构造给 **同一个** 统一界

\[
 0<p_\tau(u),q_\tau(u)\le\frac{3(e^u-1-u)}u,
 \quad p_\tau(u),q_\tau(u)=O(u)\quad(u\downarrow0),
 \tag{2}
\]

其中原点界对全部 \(\tau\in[a,b]\) 一致。具体级数中
\(A_m=1-2\Re(\tfrac12+i\tau)^m\) 满足 \(0<A_m\le3\)，
\(C_m=\sum_{k\ge1}k^{-m-1}\ge1\)；这同时证明参数可测性与局部一致收敛。
对每个 \(\sigma>1\)，在原测度 norm

\[
 \|\mu\|_\sigma:=\int_0^\infty e^{-\sigma u}d|\mu|(u)
\]

上，式(2)给

\[
 \|P_\tau\|_\sigma,\|\Pi_\tau\|_\sigma
 \le B_\sigma:=3\left(\log\frac\sigma{\sigma-1}-\frac1\sigma\right)<\infty.
 \tag{3}
\]

定义正 Borel 测度

\[
 P_\nu=\int P_\tau d\nu(\tau),\qquad
 \Pi_\nu=\int\Pi_\tau d\nu(\tau).
\]

Tonelli 与 (3) 支付局部有限性、每个指数权 norm 及所有参数积分／重复幂交换，故

\[
 \Pi_\nu=\sum_{k\ge1}\frac1k(T_k)_*P_\nu.
 \tag{4}
\]

特别地，正 \(\Pi_\nu\) 不是未经 primitive 审计的输入；(4) 保留全部 proper powers
及推前 Jacobian。\(P_\nu,\Pi_\nu\) 都是严格正的连续密度，不含原点原子。

定义

\[
 M_\nu=\exp_*\Pi_\nu
 =\delta_0+\sum_{j\ge1}\frac{\Pi_\nu^{*j}}{j!}.
 \tag{5}
\]

加权总质量精确为

\[
 \|M_\nu\|_\sigma
 =\exp\|\Pi_\nu\|_\sigma\le e^{B_\sigma}.
 \tag{6}
\]

所以 (5) 是真正的正局部有限测度，非形式卷积级数。每项 \(j\ge1\) 绝对连续，
且其密度级数在每个有限区间的 \(L^1\) 中收敛；故
\(M_\nu=\delta_0+m_\nu(u)du\)，\(m_\nu>0\) 几乎处处。
由于 \(q_\nu\) 自身在 \(u>0\) 严格正，这个结论不是空支持结果。
换回 \(x=e^u\) 后，非单位 integer 分布仍绝对连续。

## 2. Euler 变换、完成化及完整 pole 背景

在 \(\Re s>1\)，使用由实 \(s\to+\infty\) 时趋零固定的 log 分支，有

\[
 I_\nu(s)=\int e^{-su}d\Pi_\nu(u)
 =\int\log Z_\tau(s)d\nu(\tau),\qquad
 Z_\nu(s)=\int e^{-su}dM_\nu(u)=e^{I_\nu(s)}.
 \tag{7}
\]

交换由 (3) 绝对收敛支付，复全纯性由每个更小闭半平面的同界支付。
注意
\(M_\nu\ne\int M_\tau d\nu\) 一般成立；(7) 是 \(Z\) 的几何平均，不能写成算术平均。

在最初半平面固定

\[
 E_\nu(s):=s(s-1)Z_\nu(s)
 =\exp\int\log\big((s-\tfrac12)^2+\tau^2\big)d\nu(\tau).
 \tag{8}
\]

概率总质量恰为 1，因而分母 \(s(s-1)\) 的幂恰为 1。沿实 \(s\) 轴，
所有分子均正，(8) 有自然非零解析延拓至 \(s=0,1\) 的邻域；其值都是

\[
 C_\nu=\exp\int\log c_\tau d\nu(\tau)>0.
\]

所以可达分支上的 \(Z_\nu\) 在 0、1 确有简单极点，系数分别为 \(-C_\nu,C_\nu\)；
乘上 \(s(s-1)\) 正好去除它们，没有制造额外零点。其 Gamma 背景为 0，不能换作经典 Gamma。
在下述 slit 域，\(E_\nu(1-s)=E_\nu(s)\) 可精确成立；这种 slit-domain 反射
不等于整个完成函数的 FE 公理。

令 \(h\in C_c^\infty(\mathbb R)\)，完整线性平衡泛函为

\[
 W_\nu(h)=\int_{\mathbb R}
 \left[2\cosh(u/2)-|u|e^{-|u|/2}q_\nu(|u|)\right]h(u)du,
 \quad q_\nu=\int q_\tau d\nu.
 \tag{9}
\]

在 \(u=0\) 连续延拓。compact 域上的交换由 (2) 支付；完整极点背景仍是两个评价，
并未随连续参数变成连续 pole 缺陷。代入 (1) 精确得到

\[
 W_\nu(h)=\int_{\mathbb R}\left(2\int_a^b\cos(\tau u)d\nu(\tau)\right)h(u)du.
 \tag{10}
\]

因此所有 prime powers、双 pole 以及符号均已保留，未靠只看谱端反推未知正性。

## 3. 连续正谱、自伴域与普通 trace 的限制

对全部 complex \(g\in C_c^\infty(\mathbb R)\)，设
\(g^*(u)=\overline{g(-u)}\)、\(\widehat g(t)=\int g(u)e^{-itu}du\)。式(10)给

\[
 Q_\nu(g):=W_\nu(g*g^*)
 =\int_a^b\big(|\widehat g(\tau)|^2+|\widehat g(-\tau)|^2\big)d\nu(\tau)
 =\int|\widehat g(t)|^2d\sigma_\nu(t)\ge0,
 \tag{11}
\]

\[
 d\sigma_\nu(t)=d^{-1}
 \mathbf1_{[-b,-a]\cup[a,b]}(t)dt,
 \qquad \sigma_\nu(\mathbb R)=2.
 \tag{12}
\]

每一段的密度为 \(1/d\)，不是 \(1/(2d)\)。特别
\(\int(1+t^2)^{-1}d\sigma_\nu(t)<2\)。这是连续正谱，而非零除子计数测度。

在 \(\mathcal H=L^2(\sigma_\nu)\) 上，

\[
 (Dg)(t)=tg(t),\qquad \operatorname{Dom}D=\mathcal H,
 \quad D=D^*,\quad\|D\|=b.
 \tag{13}
\]

全部测试的 Fourier 像在 \(\mathcal H\) 稠密：若 \(v\) 与其正交，
有限复测度 \(\overline v\sigma_\nu\) 的逆 Fourier 分布杀掉全部 compact 测试，
故该测度为零。因 \(D\) 有界，这也是其 graph norm 稠密域。
它的谱是两闭区间，且没有本征值：单点的 \(\sigma_\nu\) 质量为 0。

**标量谱权仍不是普通 Hilbert trace。** 任一 \(\sigma_\nu(B)>0\) 的 Borel 子集
给无限维 \(L^2(B,\sigma_\nu)\)，故普通 \(\operatorname{Tr}E_D(B)=\infty\)，
不能与有限的 \(\sigma_\nu(B)\) 相等。\(D^{-1}\) 有界但非 compact，当然也非
Hilbert–Schmidt，故这里不存在通常 C4 所需的 compact-resolvent／det2 零除子实现。
可另行声明交换代数上的有限 trace \(\tau(\phi(D))=\int\phi(t)d\sigma_\nu(t)\)，
并在其下定义局部 log determinant；这是一项不同的 trace 数据，不能称为普通算子 trace。

## 4. log determinant 的分支规范与不可亚纯性

在 \(z\in\mathbb C_+\) 取各 \(\operatorname{Log}(z-t)\) 的上半平面标准分支，定义

\[
 L_\nu(z)=\frac1d\int_a^b
 \big(\operatorname{Log}(z-\tau)+\operatorname{Log}(z+\tau)\big)d\tau,
 \qquad F_\nu(z)=e^{L_\nu(z)}.
 \tag{14}
\]

这才是严格的 \(\exp\int\log(z^2-\tau^2)d\nu\) 规范；
不应先把 \(z^2-\tau^2\) 投入一个会碰负实轴的全局 principal Log。
此时 \(F_\nu(z)/z^2\to1\) 于虚轴无穷远。
经 Schwarz 反射／相位匹配，可将 \(F_\nu\) 定义于
\(\mathbb C\setminus([-b,-a]\cup[a,b])\)，在那里非零，且为 even、real-type。
中心化的相位明确为

\[
 E_\nu(\tfrac12+iz)=-F_\nu(z).
 \tag{15}
\]

例如 \(z=iy\) 时右边为正；这固定了相位。原 \(\Re s>1\) 映到
\(\Im z<-1/2\)，所以 (15) 的原 Euler branch 必须先从下半平面核对，
再用反射写上半平面版本，不能忽略这个符号方向。

对 (14) 逐项求导，得到

\[
 M_\nu(z):=-\frac{F_\nu'(z)}{F_\nu(z)}
 =\int\frac{d\sigma_\nu(t)}{t-z}
 =\frac1d\left[
 \operatorname{Log}(z-b)+\operatorname{Log}(z+a)
 -\operatorname{Log}(z-a)-\operatorname{Log}(z+b)\right].
 \tag{16}
\]

分支在整个 \(\mathbb C_+\) 由左边唯一固定。对 \(z=x+iy\)、\(y>0\)，

\[
 \Im M_\nu(z)=\int\frac{y}{(t-x)^2+y^2}d\sigma_\nu(t)>0.
 \tag{17}
\]

这独立验证 Pick／Herglotz 正性，而非援引不存在的 entire 零点。
其自然上下边值在两个开区间上满足
\(M_{\nu,+}(x)-M_{\nu,-}(x)=2\pi i/d\)，在区间外差为 0。
但 **cut 的内点不是自然边界**：上分支可局部延拓到另一 sheet。
要排除单值全局亚纯实现，应使用端点而非错误的自然边界断言。

一个不依赖边值术语的排除证明是

\[
 M_\nu'(z)=\frac1d\left[
 \frac1{z-b}+\frac1{z+a}-\frac1{z-a}-\frac1{z+b}\right].
 \tag{18}
\]

若存在全平面单值亚纯 \(\widetilde F\not\equiv0\) 与 (14) 在 \(\mathbb C_+\)
一致，则 \(-\widetilde F'/\widetilde F\) 是单值亚纯延拓，其导数仍须等于 (18)。
然而任一单值亚纯函数的导数在所有有限点的 residue 均为 0；(18) 在 \(b\) 的 residue
为 \(1/d\ne0\)，矛盾。故 \(F_\nu\) 没有这种亚纯延拓，尤其不能是非零整个函数。

还可把 monodromy 显写出来。令 \(\phi(w)=w\operatorname{Log}w-w\)，则

\[
 L_\nu(z)=d^{-1}
 [\phi(z-a)-\phi(z-b)+\phi(z+b)-\phi(z+a)].
 \tag{19}
\]

在 \(b\) 附近，\(L_\nu=A(z)-d^{-1}(z-b)\operatorname{Log}(z-b)\)，
其中 \(A\) 局部全纯。绕 \(b\) 一周后

\[
 F_\nu(z)\longmapsto
 F_\nu(z)\exp[-2\pi i(z-b)/d],
 \tag{20}
\]

乘子并非恒等 1。\(F_\nu\) 趋近端点时有有限非零极限，也不消除这个分支。
这排除把端点称作通常零点／极点；整个零除子的局部整数重数结构已经不存在。

## 5. 可消费后果与停止范围

- **存在性与正性：** 全 \(a,b\) 范围、每个 \(\sigma>1\)、全 complex compact 测试；
  无数值采样、截断误差或未付极限。正 \(P\to\Pi\to M\) 与完整 pole 背景分别闭合。
- **实现角色：** \(P,\Pi,M\) 是 arithmetic 侧；\(\sigma_\nu\) 是正型泛函的连续谱侧；
  \(D\) 是指定正 Hilbert 空间的乘法算子。后两者不冒称 entire 除子／普通 trace。
- **C3/C4 边界：** 连续 arithmetic 可有标准中心线离散零点，已由原连续正族支付；
  进一步的连续 spectral 也可有全域正型和自伴实现，但此混合只能给 slit-domain
  log determinant，其连续谱不能逐点放入 usual entire canonical product。
- **C1 限制：** 分支端点位于 \(s=1/2\pm ia,1/2\pm ib\)，故任何包含整条中心线的
  开带都不能给该完成函数全域亚纯延拓。此例不满足标准 C1；不能把它消费成
  “C1+C2+C3 仍不推出中心线”的反例，更不能说一个非零整个函数有连续零集。
- **最强旧与净值：** 这是原正族的凸 log 混合直接结果，所新增的解释是连续谱边界，
  不另结算轮次，不宣称额外实际 ζ whole 改善。原 542＋555→557 whole4/5、成长 K/core/Ξ
  未变。标准 C4 的纯点整数 trace-divisor 责任与更广义连续谱责任从此明确分开。

本文件无 pending producer、数值进程或待用 agent 输出。root 消费前宜只核主稿新增段
是否保持 (12)、(15)、C1 失败及“非自然边界”四项限定，不必扩造另一玩具族。

## 6. 562 新增 §4.1 及 §6 澄清的定向复核

已按 root 交付，仅核 562 新 §4.1（式(14)–(16)）及 §6 新增两项澄清；
不重复终审原主体，也不改其余文件。**复核 PASS。**

1. 主稿的混合是 \(\Pi\)／primitive 线性混合、\(M\) 卷积指数、\(Z\) log 混合，
   未误写成平均 \(M_c\)；(3) 的统一 \(A_m\le3\) 界足以支付其声明的全部指数权与 Tonelli。
2. \(\sigma_\nu\) 两段密度 \(1/(b-a)\)、总质量 2、乘法算子有界自伴且无点谱，
   与本稿 (11)–(13) 完全一致；保持 arithmetic 与 spectral 两侧的区别。
3. \(F_\nu=-E_\nu(1/2+iz)\) 的相位正确；主稿明确原 Euler 域映到
   \(\Im z<-1/2\)，上半平面标准支由本稿 (14)–(15) 的 real-conjugate 规范匹配，
   没有误将右收敛半平面当作 \(\mathbb C_+\)。
4. 主稿的 Cauchy 变换及其导数符号正确，\(b\) 点 residue 为 \(1/(b-a)\ne0\)，
   从而不能有全平面单值亚纯 \(F_\nu\)。明确区分端点分支与 cut 内点局部换 sheet，
   并明说 strict C1 也失败，没有将此例当作 C1+C3 的反例。
5. 主稿保留 finite commutative trace 与普通 Hilbert projection trace 的区别，
   不把连续 \(\sigma\) 冒称 entire 计数除子。其“更宽类 RH”明确限于正型／自伴层。
6. §6 的两项新增判断正确：唯一性分类不付一个候选对象的正性锥成员资格；
   物理 \(x\) 上的加性整数梳与 \(\{\log n\}\) 不同，后者相邻间距趋 0，
   不能满足通常 Delone 的 uniform separation，更不能免费运输 theta／Poisson
   正性为 log 坐标的完整 Weil 正性。

本定向复核仍属于同 C025；无另计轮次、STATE/cadence 修改或 Git 操作。
