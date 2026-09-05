# 293. Poisson 右移、实际记录的相对缩减与独立有限完成候选

日期：2026-09-06。B1z 新周期第3轮；归属：独立 response 论文的 Weil 接口审计。
状态：[T] 同一实际有限源的右移、记录上界及同阶抵消；
[T/R] 有限完成候选的独立 Poisson/germ 核验；
[C] RH条件下全轴实部误差及明确日程；
[O] 无条件右侧绝对负迹预算。本文不证明 RH，也不声称新 Poisson 半群方法。

## 1. 同一记录、参数与准确目标

固定 \(0<\sigma_0<\beta<1/2\)，置 \(d=\beta-\sigma_0>0\)。
沿[284-D](284-causal-abel-inverse-and-diagonal-record-selection.md)同一整数记录
\(Y=N\to\infty\)，令 \(L=\log Y\)，并沿用292的有限实 lag 测度
\[
 \nu_Y=\sum_{n\le Y}\Lambda(n)n^{-\sigma_0}e^{-n/Y}\delta_{\log n}
       -(\log)_*(x^{-\sigma_0}e^{-x/Y}dx|_{[1,Y]}),\quad
 H(u)=\nu_Y([0,u]),\quad M=H(L).
 \tag{1}
\]
原子端点完整保留，\(H(0)=0\)。所用独立实际输入恰为
\[
 |M|\gg Y^{1/2-\sigma_0}\ell(Y),\qquad
 |H(u)|\le C_e|M|e^{-d(L-u)},\quad
 \|H\|_1+\|H\|_2\ll |M| ,
 \tag{2}
\]
其中 \(\ell(Y)=\max(1,\log\log\log Y)\)，只在充分大尺度使用。
记录不预设质量符号；本篇不改变记录、不新增有效高度或认证算法。
另用经典 Chebyshev 上界 \(\psi(x)\ll x\)，不使用 RH 级误差。

定义原始及右移后的未中心化符号
\[
 P_0(t)=\int\cos(tu)d\nu_Y(u),\qquad
 P_a(t)=\int e^{-au}\cos(tu)d\nu_Y(u)\quad(a>0).
 \tag{3}
\]
\(P_a\) 精确是相同 \(Y,N=Y\) 的 \(\sigma'=\sigma_0+a\) prime--continuum 符号，
不是将中心化 \(\widehat r=P_0-M\) 直接改参数。
令
\[
 \Pi_b(t)=\frac{b}{\pi(b^2+t^2)},\quad
 d\mu_b(t)=\Pi_b(t)dt,\quad
 \tau_b(f)=\int f\,d\mu_b,\quad \kappa_b(P)=\tau_b(P_-).
 \tag{4}
\]
原规范 Cauchy 迹始终为 \(\tau_1=\tau_C\)；下标 \(1+a\) 只在中间恒等式出现。

## 2. 精确 Poisson 迁移及其单独使用的限制 [T]

**引理293-A。** 对有限实非负 lag 源和(3)，有
\[
 P_a=\Pi_a*P_0,\qquad \Pi_1*\Pi_a=\Pi_{1+a},
 \tag{5}
\]
\[
 \kappa_1(P_a)\le\kappa_{1+a}(P_0)
 \le(1+a)\kappa_1(P_0),\qquad
 \kappa_{1+a}(P_0)\ge\frac{\kappa_1(P_0)}{1+a}.
 \tag{6}
\]
这里“非负 lag”仅指支撑位置 \(u\ge0\)，不要求测度为正。

证明。Cauchy 核的 Fourier 变换为 \(e^{-a|u|}\)，可对两个半轴分别作
单极点积分得到。对有限总变差源用 Fubini，得到(5)第一式；两个
\(L^1\) 核的变换相乘及 Fourier 唯一性给第二式。
凸性给 \((\Pi_a*P_0)_-\le\Pi_a*(P_0)_-\)，再与 \(\mu_1\) 积分。
最后
\[
 \frac{d\mu_{1+a}}{d\mu_1}(t)
 =\frac{(1+a)(1+t^2)}{(1+a)^2+t^2}
 \in[(1+a)^{-1},1+a]
 \tag{7}
\]
给两侧比较。所有被卷积符号均有界，故这里的积分合法。\(\square\)

(5)是292-(29)的半群写法，(6)是标准正核后果，不单独登记为新结构。
由292的 \(\kappa_1(P_0)\asymp|M|\)，只使用(6)仍仅得 \(O(|M|)\)；
它并未控制需要的绝对 \(O(1)\) 预算。

## 3. 记录历史给出的真正相对缩减 [T]

**定理293-B。** 若 \(a>d\)，则
\[
 \tau_1|P_a|\le |M|e^{-aL}
 +C_e|M|e^{-dL}
   \left(\frac{a}{a-d}+\frac1{2\sqrt{a-d}}\right).
 \tag{8}
\]
因此对任意日程 \(0<\delta_Y\le1/4,\ \delta_Y\to0\)，置
\[
 \sigma'_Y=\tfrac12+\delta_Y,\qquad a_Y=\sigma'_Y-\sigma_0,
 \tag{9}
\]
沿同一284记录统一有
\[
 \tau_1|P_{a_Y}|\ll_{\sigma_0,\beta}|M|Y^{-d}=o(|M|).
 \tag{10}
\]

证明。置 \(W_a(u)=e^{-au}H(u)\)。Stieltjes 分部积分精确给
\[
 P_a(t)=Me^{-aL}\cos Lt
       +a\int_0^LW_a(u)\cos tu\,du
       +t\int_0^LW_a(u)\sin tu\,du.
 \tag{11}
\]
这里右移后的总质量是 \(P_a(0)=Me^{-aL}+a\int W_a\)，并非仅端点项。
292-(11)的奇延拓/Plancherel 计算对 \(W_a\) 同样给
\[
 \tau_1|P_a|
 \le |M|e^{-aL}+a\|W_a\|_1+\|W_a\|_2/\sqrt2.
 \tag{12}
\]
由(2)，\(|W_a(u)|\le C_e|M|e^{-dL}e^{-(a-d)u}\)。
积分得 \(\|W_a\|_1\le C_e|M|e^{-dL}/(a-d)\)、
\(\|W_a\|_2\le C_e|M|e^{-dL}/\sqrt{2(a-d)}\)，故有(8)。
在(9)中 \(a_Y-d\ge1/2-\beta>0\)，且 \(a_Y\) 一致有界，故(10)成立。\(\square\)

### 3.1 再利用真实小前缀的 Chebyshev 界

**定理293-C。** 置
\[
 B=\max(1,|M|Y^{-d}),\qquad
 \theta(\sigma')=\frac{1-\sigma'}{1-\beta}.
 \tag{13}
\]
对全部 \(\sigma'\in[1/2,3/4]\)、\(a=\sigma'-\sigma_0\)，一致有
\[
 \boxed{\quad \tau_1|P_a|\ll_{\sigma_0,\beta} B^{\theta(\sigma')}.\quad}
 \tag{14}
\]
这里 \(0<\theta<1\)，是对(10)中 \(O(B)\) 的实际上界增强，不是负迹有界结论。

证明。由 \(\psi(x)\ll x\) 对递减幂权部分求和，以及连续项的初等积分，
\[
 |H(u)|\le
 \sum_{n\le e^u}\Lambda(n)n^{-\sigma_0}
 +\int_1^{e^u}x^{-\sigma_0}dx
 \ll_{\sigma_0}e^{(1-\sigma_0)u}.
 \tag{15}
\]
与(2)合用，令 \(r=1-\sigma'\)、\(b=\sigma'-\beta\)，得到
\[
 |W_a(u)|\le C\min(e^{ru},B e^{-bu}),\quad
 r\ge1/4,\quad b\ge1/2-\beta,\quad r+b=1-\beta.
 \tag{16}
\]
这两个包络的交点是 \(u_*=\log B/(r+b)\ge0\)。将积分区间扩大到
\([0,\infty)\)，在 \(u_*\) 分割，直接得到
\[
 \|W_a\|_1\le C(1/r+1/b)B^\theta,\qquad
 \|W_a\|_2\le C(1/(2r)+1/(2b))^{1/2}B^\theta.
 \tag{17}
\]
同一最小值在全部 \(u\ge0\) 上至多 \(B^\theta\)，所以由(16)在端点取值，
\(|M|e^{-aL}=|W_a(L)|\le CB^\theta\)，不要求 \(u_*\le L\)。
代入(12)，并用 \(a,r^{-1},b^{-1}\) 的统一界，得(14)。\(\square\)

不能由(14)宣称绝对有界：记录只保证
\(B\gg Y^{1/2-\beta}\ell(Y)\to\infty\)，没有给 \(B^\theta=O(1)\)。
一个上界表达式发散也不证明实际右移符号发散。改变 \(\beta\) 随 \(Y\)
逼近 \(1/2\) 会改变记录、逆核和常数；不在本篇固定参数量词内。

## 4. 修正和 Jensen 抵消确实具有质量同阶 [T]

**推论293-D。** 对(9)的同一实际序列，
\[
 \tau_1|P_{a_Y}-P_0|\asymp |M|.
 \tag{18}
\]
若定义正核的 Jensen 缺口
\[
 D_a(P_0)=\kappa_{1+a}(P_0)-\kappa_1(P_a),
 \tag{19}
\]
则
\[
 D_{a_Y}(P_0)
 =\int\min\{\Pi_{a_Y}*(P_0)_+,\Pi_{a_Y}*(P_0)_-\}\,d\mu_1
 \asymp |M|.
 \tag{20}
\]
证明。292给 \(\tau_1|P_0|\asymp|M|\)，与(10)及正反三角不等式合用得(18)。
对两个非负函数 \(U,V\)，有 \((U-V)_-=V-\min(U,V)\)。
取 \(U=\Pi_a*(P_0)_+,V=\Pi_a*(P_0)_-\)，积分即得(20)的等式。
再由(7)、292和(10)，(19)的第一项为 \(\Theta(|M|)\)，第二项为 \(o(|M|)\)。
\(a_Y\) 位于固定紧区间，比较常数统一。\(\square\)

所以右移不是把迹改小；中间迹在(7)中始终与原迹双边可比。
它实际混合原来的正负载波，并支付292所要求的非微扰补偿。
这仍只清除了原来的 \(|M|\) 尺度障碍，没有估计绝对剩余量至 \(O(1)\)。

## 5. 有限完成候选可以独立接入145，而非假定尾部很小 [T/R/C]

令 \(s=1/2+z\)，使用132的真实完成项
\[
 G(s)=1/s-\tfrac12\log\pi+\tfrac12\psi(s/2),\qquad
 F_Y^\sharp(z)=G(s)+\int_1^Yx^{-s}e^{-x/Y}dx
                    -\sum_{n\le Y}\Lambda(n)n^{-s}e^{-n/Y}.
 \tag{21}
\]
\(G\) 中不再加回已经由连续项处理的 \(1/(s-1)\)。
这是另一个正确定义的 regularization，不宣称等于132的完整 Abel 候选。

**命题293-E。** 每个 \(F_Y^\sharp\) 在 \(\Re z>0\) 全纯、real-type，并满足
136的 Poisson admissibility；当 \(Y\to\infty\) 时，在 \(\Re z>1/2\)
局部一致收敛到 \(\xi'/\xi(1/2+z)\) 的 Euler germ。

证明。有限 lag 部分为整函数，\(G\) 在 \(\Re s>1/2\) 全纯。
在每个固定 \(\varepsilon>0\) 的闭半平面 \(\Re z\ge\varepsilon\)，
固定 \(Y\) 的有限源有一致绝对界，而
\(\Re G(1/2+z)\to+\infty\) 沿大半圆一致成立。
这个常用 Gamma 事实也可直接由
[DLMF 5.7.6](https://dlmf.nist.gov/5.7.E6)的部分分式式重建：
写 \(w=A+iB,\ A\ge1/4,\ R=|w|\ge2,\ J=\lfloor R\rfloor\)。
当 \(A\ge R/2\)，\(\sum_{n\le J}\Re(n+w)^{-1}\le O(1)\)；
当 \(A<R/2\)，\(|B|\ge\sqrt3R/2\)，同一和仍为 \(O(1)\)。
尾项的实部在 \(A\ge1\) 时非负；\(1/4\le A<1\) 时负部至多
\((1-A)/((n+1)(n+A))\)，其和一致有界。
因此 \(\Re\psi(w)\ge\log R-O(1)\)，足以证明所需增长。

令 \(W(t)=[-\Re F_Y^\sharp(\varepsilon+it)]_+\)。
它连续且紧支撑。Poisson 积分 \(\mathcal P_\varepsilon W\) 非负，
边界值为 \(W\)。对
\(\Re F_Y^\sharp+\mathcal P_\varepsilon W\) 在右侧大半圆使用最小值原理，
再令半径趋于无穷，即得136-(17)；不假设 \(W\) 一致有界。
最后，在 \(\Re s>1\) 的紧集上由 \(\Lambda(n)\le\log n\) 绝对支配收敛，
有限和与积分分别趋于 \(-\zeta'/\zeta(s)\)、\(1/(s-1)\)。
与真实完成恒等式合用，极限为 \(\xi'/\xi(s)\)。\(\square\)

对(9)，定义真正的有限右侧预算
\[
 \kappa^\sharp_Y
 =\tau_1\bigl((\Re F_Y^\sharp(\delta_Y+it))_-\bigr)
 =\tau_1((g_{\sigma'_Y}-P_{a_Y})_-).
 \tag{22}
\]
292的 Gamma 部分分式估计对 \(\sigma'\in[1/2,3/4]\) 一致，故
\(\tau_1|g_{\sigma'}|\le C\)。Cauchy 特征函数又给
\(\tau_1(P_a)=\sum_{n\le Y}\Lambda(n)n^{-1-\sigma'}e^{-n/Y}
-\int_1^Yx^{-1-\sigma'}e^{-x/Y}dx=O(1)\)，一致于该区间。
负部的 \(L^1\)-Lipschitz 性及 Jordan 分解于是给
\[
 \kappa^\sharp_Y=\tfrac12\tau_1|P_{a_Y}|+O(1)
 \ll_{\sigma_0,\beta}1+B^{\theta(\sigma'_Y)}.
 \tag{23}
\]
特别地，在这些参数的任意共同日程上，
\[
 \kappa^\sharp_Y=O(1)
 \iff\tau_1((P_{a_Y})_+)=O(1)
 \iff\tau_1((P_{a_Y})_-)=O(1)
 \iff\tau_1|P_{a_Y}|=O(1).
 \tag{24}
\]
首个等价使用 \(\tau_1|g_{\sigma'_Y}|=O(1)\)，中间等价使用
\(\tau_1P_{a_Y}=O(1)\)。这只允许在**标量有界负迹目标**中去掉 Gamma；
它不允许从非线性多项式、卷积响应或 Gram 中直接删除该通道。
若能独立证明沿此日程 \(\sup_Y\kappa^\sharp_Y<\infty\)，则由命题293-E
和145-ZT推出 RH [C]。这是一个准确的条件接口，不声称预算已知或弱于 RH。
本篇不使用未知零点来构造 \(F_Y^\sharp\) 或证明其 admissibility。

已有143-ZL早已证明另一日程 \(N=\lceil Y\log^2Y\rceil\) 等全部有限化误差
\(o(1)\)；“完整 Abel 能否有限化”不是新开放问题。
131也已构造不带Abel因子的sharp候选；本节只为(1)保留的匹配Abel权
单独核验所需接口，不把有限候选的一般想法记作新发明。
若坚持与132原完整 Abel 族比较，\(N=Y\) 之外的联合尾仍须估计。
这里不隐藏该尾，而是由命题293-E独立验证一个合法有限候选，故145接口
不要求先证明两个 regularization 相近。不能将此事实写成原尾部已经很小。

## 6. 公理作用、停止边界与下一最小输入

| 输入 | 确切作用 | 删除后的失效或范围 |
|---|---|---|
| 同一有限实源、非负 lag 和匹配权 | (3)、(5)、(11)保持源和端点 | 不匹配 cutoff、复原始符号需重建 |
| 284独立强记录与指数历史 | (8)--(10)、292下界及(18)--(20) | Poisson 收缩本身只有 \(O(|M|)\) |
| 实际 Chebyshev 上界 | (15)--(17)增强至 \(B^\theta\) | 仅历史包络没有这个小前缀控制 |
| 固定 \(\sigma_0<\beta<1/2\) | 右移与历史指数有统一正间隔 | 改成随尺度参数须重审全部常数 |
| 固定 Cauchy 迹、正核 | Jensen 和真实绝对归一化 | 不能删去(7)或把归一化响应当实际迹 |
| 完成项、Euler germ、Poisson | 命题293-E与145的相容性 | 任意修正即便变小也未必保留 divisor |
| 独立绝对预算 | 唯一尚未成立的中心线输入 | 选择/半群/完备化均不产生它 |

本轮可晋级的有限结果是(10)、(14)、(18)--(20)，不是经典半群公式本身。
292停止的是固定左侧原始绝对目标；(10)证明右移可以通过其质量尺度障碍，
却未恢复一个已经闭合的数域 Weil 配置。
下一最小算术输入必须针对明确 \(\delta_Y>0\to0\) 的(22)：
\(\kappa^\sharp_Y=O(1)\)，或真正降低(23)剩余项的独立有符号估计。
由(23)，只把同一量改写成右移后的绝对 \(L^1\) 范数不算输入缩减。
289的固定左侧中心化四阶预算不自动转成此量；只写新 Gram 或一般矩表示则停止扩写。
本篇只处理 Riemann 实源；其他 \(L\) 函数须重建实性、记录与完成项，
也没有建立上同调型极化。新颖性、发表价值和外部审查仍 [O]。

## 7. 全轴实部误差与明确右侧日程：仅为RH条件基准 [C]

本节不使用284记录，允许全部整数 \(Y\to\infty\)。
假设RH。令 \(E(x)=\psi(x)-x+1\)，仍为右连续完整原子约定，故 \(E(1)=0\)。
经典条件估计为
\[
 |E(x)|\le C\sqrt{x}\log^2(2x)\quad(x\ge1).
 \tag{25}
\]
这里可由已核验的[Kedlaya第9章](https://kskedlaya.org/ant/chap-von-mangoldt.html)
显式公式及单位高度计数直接重建：在RH下取高度 \(V=x\)，零点贡献
不超过 \(\sqrt{x}\sum_{|\gamma|\le x}|\rho|^{-1}
\ll\sqrt{x}\log^2(2x)\)，截断余项及半权到完整原子的差均被吸收。
没有用未证零密度、零点简单性或数值验证高度。(25)不能在本篇无条件部分使用。

**定理293-F [C]。** 置 \(L=\log Y,\ \sigma=1/2+\delta\)。
对 \(0<\delta\le1/4,\ \delta L\ge1\)，RH蕴含一致的全轴估计
\[
 \boxed{\quad
 \tau_C\left|\Re F_Y^\sharp(\delta+it)
       -\Re\frac{\xi'}{\xi}(\sigma+it)\right|
 \ll \frac{Y^{-\delta}L^2}{\sqrt\delta}.
 \quad}
 \tag{26}
\]
本式是**实部差**的 \(L^1(\mu_C)\) 估计；不声称全复函数的该范数、
未加权范数或整个current的二阶矩一致有界。

证明。写 \(D_Y(s)=\sum_{n\le Y}\Lambda(n)n^{-s}e^{-n/Y}
-\int_1^Yx^{-s}e^{-x/Y}dx\)。精确分部积分给
\[
 D_Y(s)=e^{-1}Y^{-s}E(Y)
       +\int_1^Y E(x)x^{-s-1}e^{-x/Y}(s+x/Y)\,dx .
 \tag{27}
\]
另一方面，(25)使
\[
 D_\infty(s)=s\int_1^\infty E(x)x^{-s-1}dx
      =-\frac{\zeta'(s)}{\zeta(s)}-\frac1{s-1}
 \tag{28}
\]
在 \(\Re s>1/2\) 全纯。等式先在Euler域由Stieltjes公式证明，再用解析
延拓；\(s=1\) 的极点恰好相消。端点 \(E(1)=0\) 不额外留下常数。
真实完成恒等式为 \(\xi'/\xi=G-D_\infty\)，所以
\(F_Y^\sharp-\xi'/\xi=D_\infty-D_Y\)。

在 \(u\ge0\) 置
\[
 h(u)=E(e^u)e^{-\sigma u},\quad
 k(u)=h(u)\{1-e^{-e^u/Y}\mathbf1_{u\le L}\},\quad
 q(u)=Y^{-1}e^u h(u)e^{-e^u/Y}\mathbf1_{u\le L}.
 \tag{29}
\]
对实半轴函数 \(v\)，记 \(C_v(t)=\int_0^\infty v(u)\cos(tu)du\)、
\(S_v(t)=\int_0^\infty v(u)\sin(tu)du\)。
将(27)--(28)直接作 \(x=e^u\) 换元并取实部，得到
\[
 \Re(F_Y^\sharp-\xi'/\xi)
 =-e^{-1}Y^{-\sigma}E(Y)\cos Lt
          +\sigma C_k(t)+tS_k(t)-C_q(t).
 \tag{30}
\]
左侧按(26)的不同自变量评价。正弦项为**正号**，来自
\(\Re[(\sigma+it)(C_k-iS_k)]=\sigma C_k+tS_k\)。
未再次分部积分，也未丢掉 \(u=L\) 的跳跃或完整原子。

由(25)，\(|h(u)|\le C e^{-\delta u}(1+u)^2\)。
在 \(u\le L\) 上用 \(1-e^{-e^u/Y}\le e^u/Y\)，得
\[
 \int_0^L|k(u)|^2du
 \le C Y^{-2}\int_0^L e^{2(1-\delta)u}(1+u)^4du
 \le C Y^{-2\delta}(1+L)^4 .
 \tag{31}
\]
在 \(u>L\) 上，直接积分展开多项式得
\[
 \int_L^\infty|k(u)|^2du
 \le C Y^{-2\delta}\sum_{j=0}^4
   \binom4j(1+L)^{4-j}\frac{j!}{(2\delta)^{j+1}}
 \le C Y^{-2\delta}\frac{(1+L)^4}{\delta}.
 \tag{32}
\]
最后一步用 \(\delta(1+L)\ge1\)；所有常数与 \(\delta,Y\) 无关。
同样有
\[
 \|q\|_1+e^{-1}Y^{-\sigma}|E(Y)|\le C Y^{-\delta}L^2,
 \qquad \|k\|_2\le C Y^{-\delta}L^2/\sqrt\delta .
 \tag{33}
\]
这里 \(\delta L\ge1,\delta\le1/4\) 已保证 \(L\ge4\)。
每个固定 \(\delta>0\) 时 \(k\in L^1\cap L^2\)，所以(30)积分有意义；
统一界来自(31)--(33)，不是交换一个非一致的 \(\delta\to0\) 极限。

余弦/正弦延拓的Plancherel公式给
\(\int C_k^2dt=\int S_k^2dt=\pi\|k\|_2^2\)。
而
\[
 \int_{\mathbb R}\frac{dt}{\pi^2(1+t^2)^2}
 =\int_{\mathbb R}\frac{t^2dt}{\pi^2(1+t^2)^2}
 =\frac1{2\pi}.
 \tag{34}
\]
因而 \(\tau_C|\sigma C_k+tS_k|\le(\sigma+1)\|k\|_2/\sqrt2\)；
另有 \(\tau_C|C_q|\le\|q\|_1\)。
代回(30)、(33)得(26)，覆盖**整个实轴**，无需频率截断。\(\square\)

### 7.1 条件日程与循环性检查

在充分大 \(Y\) 上选定
\[
 \delta_Y=\frac{5\log L}{2L},\qquad L=\log Y .
 \tag{35}
\]
则 \(\delta_Y\to0\)、\(\delta_Y L\ge1\)，且(26)右侧为
\(O((\log L)^{-1/2})\to0\)。
RH下由[131-XQ](131-positive-real-boundary-impedance-weil.md)的成对Hadamard
展开，\(\Re(\xi'/\xi)(1/2+\delta+it)\ge0\)；
每个临界零点的成对倒数实部为正，成对和局部一致收敛。
因此
\[
 \mathrm{RH}\quad\Longrightarrow\quad
 \kappa_Y^\sharp=O((\log L)^{-1/2})\longrightarrow0 .
 \tag{36}
\]
更慢的143日程 \(\delta_Y=1/(4+\sqrt L)\) 也可用，(26)给
\(O(e^{-L/(4+\sqrt L)}L^{9/4})\to0\)。
常数 \(5/2\) 只是此粗RH误差所给的**安全日程常数**，未证明最优，
也不是新的无条件零自由区域。

反向，沿任意 \(Y_j\to\infty,\delta_{Y_j}\to0\) 若
\(\kappa_{Y_j}^\sharp\) 有界，命题293-E及145即推出RH。
所以对明确日程(35)，RH、有界 \(\kappa^\sharp\)、趋零 \(\kappa^\sharp\)
是等价条件。由(24)，有界右移实部 \(L^1\) 也等价。
**这个等价只作循环性审计，不记作将RH削弱成新算术假设。**
尤其不能把(25)或未知 \(\xi'/\xi\) 的正实部当成无条件已构造背景。
本节与147全二阶矩发散障碍相容，不能将实部差的 \(L^1\) 改成全current的 \(L^2\)。

## 8. 有限计算与落盘审计

[poisson_record_transport_probe.py](../scripts/poisson_record_transport_probe.py)
只用mpmath MP50，模型为 \(L=12,24\)、\(d=1/8,a=1/2\)、
\(C=e^{-dL}\) 下的
\(\nu=-C\delta_1+2C\delta_2+(1-C)\delta_L\)，以及其反号。
这是合成的混合原子BV路径，**不是**实际von Mangoldt或认证记录。

~~~text
python -B scripts/poisson_record_transport_probe.py
~~~

整数lag允许使用完整周期化Poisson/Cauchy核，不截去频率尾。
脚本作者及主代理独立复跑通过；主代理约14秒。
Poisson直接卷积与逐原子倾斜的最大差约 \(1.50\cdot10^{-51}\)，
完整加权分部积分差约 \(3.34\cdot10^{-52}\)。
两个模型的全轴 \(L^1\) 前后值为约
\(0.531867\to0.0937745\)、\(0.606395\to0.0209626\)；
对应精确路径上界约0.232957、0.051556。
加权Jensen缺口约0.222189、0.292838；脚本未做(20)的嵌套min双积分，
该恒等式由正文证明，不将缺口的一种算法冒称独立验证了另一算法。
全部计算仅[E]，不是区间认证、渐近定理或RH条件的数值验证。

第7节候选由主代理重建；carrier_audit与gap_exception_audit各自完整读取
最终落盘全文并独立逆向复核，均PASS、无必要修正。核验包括Gamma下界、
有限候选的Poisson/germ条件、全部端点、正弦正号、\(\delta\)统一常数、
全轴范数和明确日程的RH等价量词；README与看板摘要也未扩大结论。

仓库布局检查及11项布局回归测试通过；检查清单覆盖测试通过
（core=75、B1h=1、B1i=1，共77项仅作注册及mock调度核验，
不是77项重计算）。本轮未运行heavy全套，也未更新PDF。
内部证明不代表文献新颖性、外部同行评审或Goal阶段验收。
