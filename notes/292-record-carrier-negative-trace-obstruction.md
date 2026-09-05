# 292. 实际记录载波的同阶负迹与非微扰补偿障碍

日期：2026-09-06。B1z 新周期第2轮；归属：独立 Vaughan--Brownian
response 论文的适用边界，不另开一篇 RH 框架论文。

状态：[T] 有限带符号源的载波下界、全轴上界及定量平均；
[T/R] 284实际整数记录上的正负 Cauchy 迹同阶增长；
[N] 同一原始符号的小补偿与绝对有界证书路线失败。
全尺度定性结论另用145既有正规族机制，不声称新的正规族方法。

**这里的固定参数是 \(0<\sigma<1/2\)，不是完整 Weil 判据中的
\(s=1/2+\delta_Y+it,\ \delta_Y>0\to0\)。**
结论不否定 RH，不否定中心化四阶矩预算，也没有解决完整配置存在性。
它把一个原被列为开放的原始符号绝对预算改判为不可能目标。

## 1. 同一对象与独立算术输入

固定 \(0<\sigma<\beta<1/2\)，记 \(\delta=\beta-\sigma\)。
取[284-D](284-causal-abel-inverse-and-diagonal-record-selection.md)
给出的同一共尾整数序列 \(Y=N\)，令 \(L=\log Y\)、
\(w_Y(x)=x^{-\sigma}e^{-x/Y}\)。定义实 lag 测度
\[
 \nu_Y=\sum_{2\le n\le Y}\Lambda(n)w_Y(n)\delta_{\log n}
       -(\log)_*(w_Y(x)\,dx|_{[1,Y]}),
 \qquad M=\nu_Y([0,L]).
 \tag{1}
\]
所有原子端点均取完整权。\(H_Y(u)=\nu_Y([0,u])=M(Y,e^u)\)，
\(H_Y(0)=0,\ H_Y(L)=M\)。未中心化原始符号是
\[
 P_Y(t)=\int_{[0,L]}\cos(tu)\,d\nu_Y(u)
 =\sum_{n\le Y}\Lambda(n)w_Y(n)\cos(t\log n)
       -\int_1^Yw_Y(x)\cos(t\log x)\,dx .
 \tag{2}
\]
因此 \(P_Y(0)=M\)，而旧中心化符号是 \(\widehat r=P_Y-M\)，二者不可互换。
固定概率迹
\[
 d\mu_C(t)=\frac{dt}{\pi(1+t^2)},\qquad
 \tau_C(f)=\int_{\mathbb R}f\,d\mu_C,\qquad f_-=\max(-f,0).
 \tag{3}
\]
对每个有限 \(Y\)，\(P_Y\) 有界；这是一项真实的标量乘法算子有限迹。

284已独立证明，沿所选记录，有尺度无关的 \(C_0,C_2,C_e<\infty\)：
\[
 |M|\gg Y^{1/2-\sigma}\ell(Y),\quad
 \|H_Y\|_1\le C_0|M|,\quad \|H_Y\|_2\le C_2|M|,
 \quad |H_Y(u)|\le C_e|M|e^{-\delta(L-u)} ,
 \tag{4}
\]
其中 \(\ell(Y)=\max(1,\log\log\log Y)\)，只在充分大尺度使用。
产生记录的算术输入是283已核验的无条件质量振荡及284的因果历史转移；
不是由本篇的迹估计产生记录，不预设负质量记录或 RH。
本篇不提供这些记录的有效高度或认证数值 guard。

## 2. 有限源的实际双侧迹定理 [T]

### 定理292-A

设 \(\nu\) 是支撑在 \([0,L]\) 的有限实带符号测度，\(\nu(\{0\})=0\)，
\(H(u)=\nu([0,u])\)，\(M=\nu([0,L])\ne0\)，且
\(\|H\|_1\le C_0|M|\)。置
\[
 a=\frac1{4(C_0+1)},\qquad
 c_0=\frac{a}{12\pi(1+a^2)} .
 \tag{5}
\]
若 \(L\ge4\pi/a\)，对两个符号 \(\varepsilon=\pm1\)，都有
\[
 \boxed{\quad
 \tau_C((\varepsilon P)_-)\ge c_0|M|,\qquad
 P(t)=\int\cos(tu)\,d\nu(u).
 \quad}
 \tag{6}
\]
事实上下界已经来自固定窗口 \([-a,a]\)。
另有不要求该 \(L\) 门槛的全轴上界
\[
 \boxed{\quad \tau_C(|P|)
       \le |M|+\frac{\|H\|_2}{\sqrt2}.\quad}
 \tag{7}
\]
有限测度的累计路径有界，故(7)右侧总有意义；要取得统一 \(O(|M|)\)
上界，才额外需要 \(\|H\|_2=O(|M|)\)。

### 证明：端点、固定负井与全轴尾

Stieltjes 分部积分保留完整端点，给出精确恒等式
\[
 P(t)=M\cos(Lt)+tS_H(t),\qquad
 S_H(t)=\int_0^L H(u)\sin(tu)\,du .
 \tag{8}
\]
没有丢掉中心质量；(8)也正是284-(37)加回 \(M\)。
在 \(|t|\le a\) 上，
\[
 |tS_H(t)|\le a\|H\|_1\le |M|/4 .
 \tag{9}
\]
令
\[
 E_L^\varepsilon=
 \{t\in[-a,a]:\varepsilon\operatorname{sgn}(M)\cos(Lt)\le-1/2\}.
 \tag{10}
\]
每个长度 \(T=2\pi/L\) 的完整周期中，此集合占 \(T/3\)。
在 \([-a,a]\) 中删去至多两个不完整周期，留下总长度至少 \(2a-2T\)。
当 \(T\le a/2\) 时，故 \(|E_L^\varepsilon|\ge a/3\)。
在该集合上 \(\varepsilon P\le-|M|/4\)，而 Cauchy 密度至少为
\(1/[\pi(1+a^2)]\)。积分得到(6)，对 \(M\) 两种符号均成立。

为估计整个实轴，作 \(H\) 的奇零延拓 \(H_o\)。取 Fourier 约定
\(\widehat f(t)=\int f(u)e^{-itu}\,du\)，则
\(\widehat H_o=-2iS_H\)。Plancherel 因而给
\[
 \int_{\mathbb R}|S_H(t)|^2dt=\pi\|H\|_2^2,\qquad
 \int_{\mathbb R}\frac{t^2}{\pi^2(1+t^2)^2}dt=\frac1{2\pi}.
 \tag{11}
\]
Cauchy--Schwarz 得 \(\tau_C(|tS_H|)\le\|H\|_2/\sqrt2\)。
再以 \(\tau_C(|\cos Lt|)\le1\) 作用于(8)，即得(7)。
这里估计覆盖无限频率尾，不将有限窗口实验替代全轴上界。\(\square\)

### 推论292-B：同一实际记录 [T/R]

对(1)--(4)的实际 von Mangoldt 源，
\[
 \boxed{\quad
 \tau_C((P_Y)_-)\asymp |M|,\qquad
 \tau_C((P_Y)_+)\asymp |M|,\qquad
 \tau_C(|P_Y|)\asymp |M|.
 \quad}
 \tag{12}
\]
比较常数只依固定参数和284 guard，沿同一序列
\[
 \tau_C((\pm P_Y)_-)\gg Y^{1/2-\sigma}\ell(Y)\longrightarrow\infty .
 \tag{13}
\]
证明就是将(4)代入292-A。没有使用右侧离线零点存在性，也不要求
284的绝对值记录同时出现两个质量符号。\(\square\)

有一个重要的独立归一化核验。由 Cauchy 特征函数
\(\int\cos(tu)d\mu_C=e^{-|u|}\)，有限测度 Fubini 给
\[
 \tau_C(P_Y)=\sum_{n\le Y}\Lambda(n)n^{-1-\sigma}e^{-n/Y}
          -\int_1^Yx^{-1-\sigma}e^{-x/Y}\,dx
 \longrightarrow -\frac{\zeta'(1+\sigma)}{\zeta(1+\sigma)}-\frac1\sigma .
 \tag{14}
\]
级数由 \(\Lambda(n)\le\log n\) 绝对支配，积分同理。
因此 \(M=P_Y(0)\) **不是** Cauchy 均值；正负迹的差有界而各自发散。
特别由 \(\tau_C(P_+)-\tau_C(P_-)=O_\sigma(1)\)，两者之比趋于1。

## 3. 真正的载波平均与明确误差 [T]

292-A的下界只需历史 \(L^1\) 界；以下较精确公式另用晚段一阶历史矩。
置 \(g(v)=H(L-v)\)（\(0\le v\le L\)，区间外为零），
\[
 A(t)=M-it\int_0^L g(v)e^{-itv}\,dv .
 \tag{15}
\]
直接在(8)换元，得到
\[
 P(t)=\Re(e^{iLt}A(t)),\qquad A(0)=M .
 \tag{16}
\]
若 \(\int|g|\le C_0|M|\)、\(\int v|g(v)|dv\le C_1|M|\)，则
\[
 |A(t)-M|\le |t|C_0|M|,\qquad
 |A'(t)|\le(C_0+|t|C_1)|M|.
 \tag{17}
\]
(4)足够，分别可取 \(C_0=C_e/\delta,\ C_1=C_e/\delta^2\)。

### 引理292-C

对任意有限区间 \(I\)、复值 \(B\in W^{1,1}(I)\) 及 \(L>0\)，
\[
 \left|\int_I[-\Re(e^{iLt}B(t))]_+dt
                    -\frac1\pi\int_I|B(t)|dt\right|
 \le\frac{2\pi+2}{L}
          \bigl(\|B'\|_{L^1(I)}+\|B\|_{L^\infty(I)}\bigr).
 \tag{18}
\]
证明。自区间左端起划分长度 \(T=2\pi/L\) 的完整周期及一个长度小于 \(T\)
的余段。在每个完整周期起点冻结 \(B\)。固定复数 \(b\) 时一个周期内
负部积分精确为 \(T|b|/\pi\)，不依赖起始相位。
负部和复模都是1-Lipschitz，因此完整单元内两次替换的误差至多
\((1+1/\pi)T\int_{\rm cell}|B'|\)。
余段直接以 \((1+1/\pi)T\|B\|_\infty\) 控制，求和即(18)。\(\square\)

以 \(B(t)=A(t)/[\pi(1+t^2)]\) 代入，在固定 \(I\) 上由(17)得到
\[
 \tau_{C,I}((\pm P)_-)
 =\frac1\pi\int_I|A(t)|\,d\mu_C(t)+O_I(|M|/L).
 \tag{19}
\]
小窗口中 \(|A|\ge|M|/2\)，再次得到(6)型下界。
一般载波平均早已在[144-ZP2](144-abel-zero-wave-obstruction.md)
使用；这里不声称发明平均原理。区别是其对**完整实际有限源**的应用、
明确误差和无需离线残量主导的记录输入。
不把固定窗口(19)外推成全轴渐近；全轴只用已证(7)、(12)。

## 4. 补偿必须在真实负井上支付质量代价 [N]

对任意实 \(C_Y\in L^1(\mu_C)\)，由
\((f+g)_-\ge f_--g_+\)，有
\[
 \tau_C((\varepsilon P_Y+C_Y)_-)
 \ge c_0|M|-\tau_C((C_Y)_+)
 \ge c_0|M|-\tau_C(|C_Y|),\qquad \varepsilon=\pm1 .
 \tag{20}
\]
特别，任何 \(\tau_C(|C_Y|)=o(|M|)\) 的修正仍使负迹发散。
更精确，若修正后负迹不超过 \(K\)，把同一逐点不等式只积在(10)上即得
\[
 \boxed{\quad
 \int_{E_L^\varepsilon}(C_Y)_+\,d\mu_C
       \ge c_0|M|-K .\quad}
 \tag{21}
\]
这是非微扰补偿的**必要条件**，不是充分条件。
补偿不必变号；足够大的正背景也可能付出这种代价，但不能称作小 gluing
误差。固定窗口中具有统一正下界密度的其他迹，同样保留这个下界；
任意变更迹或除以 \(|M|\) 则必须另证原归一化、divisor 可见性和 germ 保持。

### 4.1 真实固定参数 Gamma 项，而非假定小误差 [T/R/N]

[132-(15)](132-shifted-passivity-abel-resonance.md)中的实际 archimedean 项为
\[
 g_\sigma(t)=\Re\!\left\{\frac1{\sigma+it}-\frac12\log\pi
              +\frac12\psi\!\left(\frac{\sigma+it}{2}\right)\right\}.
 \tag{22}
\]
这里不额外放回132已吸收入连续项的 \(1/(s-1)\)。
对固定 \(\sigma>0\)，
\[
 \tau_C(|g_\sigma|)=O_\sigma(1).
 \tag{23}
\]
为核验统一性，使用 [NIST DLMF 5.7.6](https://dlmf.nist.gov/5.7.E6) [R]
的部分分式公式
\[
 \psi(z)=-\gamma+\sum_{n\ge0}
                  \left(\frac1{n+1}-\frac1{n+z}\right).
 \tag{24}
\]
取 \(z=\sigma/2+it/2\)，\(J=\lceil2(|z|+1)\rceil\)。
\(n\le J\) 的两部分绝对和由 \(|n+z|\ge n+\sigma/2\) 为
\(O_\sigma(\log(J+2))\)；\(n>J\) 合并为
\((z-1)/[(n+1)(n+z)]\)，尾和为 \(O(1)\)。
故 \(|\psi(z)|\ll_\sigma\log(2+|t|)\)，再与 Cauchy 密度积分即得(23)。
因而同一有限截断的 \(g_\sigma-P_Y\) 仍有
\[
 \tau_C((g_\sigma-P_Y)_-)\asymp |M|\longrightarrow\infty .
 \tag{25}
\]
这一步没有估计 \(n>Y\) 与 \(x>Y\) 的联合 Abel 尾，也没有移动 \(\sigma\)。

### 4.2 291平方证书：真实响应本身不能有界 [N]

对同一 \(P_Y\)，用实际正源质量 \(S=A_{\rm prime}+B_{\rm cont}\) 作谱界。
令 \(b=b_{m,S}\) 为[291](291-sharp-polynomial-square-negative-trace-certificates.md)
的显式多项式，\(F(x)=-xb(x)^2\)。291的两侧证书给
\[
 \tau_C((P_Y)_-)-3\pi S/m
       \le\tau_C(F(P_Y))\le\tau_C((P_Y)_-).
 \tag{26}
\]
因此若 \(S/m=O(1)\)，则
\[
 \tau_C(F(P_Y))\ge c_0|M|-O(1)\longrightarrow\infty .
 \tag{27}
\]
更一般，只要 \(S/m=o(|M|)\) 亦然。故增加次数虽然减小逼近误差，
却不可能把这个实际带符号响应变成 \(O(1)\)。
291中的 \(|F(M)|+\sqrt{\mathbf1^*G\mathbf1}\) 是它的合法绝对上界，
因此也不可能一致有界。此处不需要猜测 \(F(M)\) 与 Gram 哪一项发散。
对反号原始符号重做同一证书亦成立。

“逼近误差足够小”的限定不可删除：291取 \(m=1\) 时 \(b=1/2\)，
\(F(P_Y)=-P_Y/4\)，由(14)其迹恰为 \(O_\sigma(1)\)；
此时误差预算却与 \(S\) 同阶，不能控制实际负迹。

这是实际积分量的障碍，强于291的区间 supremum 逼近下界；
但不否定291作为一般有限迹工具的正确性。

## 5. 全尺度定性发散：既有正规族方法的应用 [T/R/N]

本节不使用284记录或 Littlewood 振幅。对所有整数 \(Y\to\infty\)，定义
\[
 f_Y(z)=\sum_{n\le Y}\Lambda(n)n^{-\sigma-z}e^{-n/Y}
            -\int_1^Y x^{-\sigma-z}e^{-x/Y}\,dx,\qquad \Re z>0 .
 \tag{28}
\]
每个 \(f_Y\) entire，边界实部正好为 \(P_Y(t)\)。
有限 lag 测度支撑非负半轴，因此对 \(x>0\)，有精确 Poisson 公式
\[
 \Re f_Y(x+iy)=\frac1\pi\int_{\mathbb R}
                 \frac{xP_Y(t)}{x^2+(y-t)^2}\,dt .
 \tag{29}
\]
证明可逐个 \(\cos(tu)\) 积分得到 \(e^{-xu}\cos(yu)\)，再用有限 TV 的 Fubini。
不需要待证的正性或高度截断。

在开集 \(\Re z>1-\sigma\)，绝对支配收敛局部一致给
\[
 f_Y(z)\longrightarrow
 f_{\rm ar}(z)=-\frac{\zeta'(\sigma+z)}{\zeta(\sigma+z)}
                          -\frac1{\sigma+z-1}.
 \tag{30}
\]
若存在 \(Y_j\to\infty\) 使 \(\tau_C((P_{Y_j})_-)\) 一致有界，(29)及
Poisson 核在任意右半平面紧集上被常数倍 \((1+t^2)^{-1}\) 控制，
便给 \(\Re f_{Y_j}\) 的局部统一下界。
同时 \(f_{Y_j}(1)\) 由(14)有界。
[145-ZT1](145-bounded-defect-normality.md)的单点 Carathéodory 圆盘链
引理给正规性；(30)及恒等定理迫使 \(f_{\rm ar}\) 在整个 \(\Re z>0\)
有全纯延拓。这也可直接视为145-ZT的固定边界版本；这里只需其分析部分。

经典无条件事实 [R]：zeta 有非平凡零点（[Kedlaya Remark9.7](https://kskedlaya.org/ant/chap-von-mangoldt.html)
给出更强的计数渐近），[完成函数方程](https://kskedlaya.org/ant/chap-funceq.html)
及实性将其按
\(\rho\mapsto1-\overline\rho\) 配对，故至少一个满足 \(\Re\rho\ge1/2>\sigma\)。
于是(30)在 \(z=\rho-\sigma\) 有留数为负重数的不可消极点；
连续项仅在 \(\sigma+z=1\) 有极点，不能消掉此零点。
这与全纯延拓矛盾。故
\[
 \tau_C((P_Y)_-)\longrightarrow\infty
                  \quad\text{对所有整数 }Y\to\infty .
 \tag{31}
\]
再用(14)，反号负迹也发散；(23)说明加固定 \(g_\sigma\) 仍然发散。
因此换成另一条共尾整数子序列不能使这个固定参数原始目标有界。
**(31)没有全尺度增长率**；(12)--(13)的同阶尺度只沿284记录成立。
存在一个临界带零点不是“存在 RH 离线零点”的假设：固定竖线
\(\Re s=\sigma<1/2\) 本来就位于至少一些零点左侧。

## 6. 最小假设、删项与循环性审计

| 输入 | 确切作用 | 删除后的反例或失效位置 |
|---|---|---|
| 同一有限实 lag 测度、完整端点 | (8)给 Hermitian 原始符号 | 改成 \(P-M\) 引入同阶常数，(9)--(10)的负井结论不能照搬 |
| \(\|H\|_1\le C_0|M|\)、固定 \(C_0\) | 固定窗口中余项小于载波 | 取 \(\nu_L=M_L\delta_{1/L}\)、\(M_L=\sqrt L\)，有大质量但负迹 \(O(M_L/L)\to0\)，历史比为 \(L-1/L\) |
| \(L\to\infty\) | 固定窗口容纳足够完整周期 | 有界 \(L\) 未必达到(5)--(6)门槛；仅端点公式不足以给指定窗口下界 |
| \(\|H\|_2\le C_2|M|\) | (11)控制全轴上界 | (6)下界不需要；缺此界不能从(7)宣称统一 \(O(|M|)\) |
| \(|M|\to\infty\) | 从比例下界得到发散 | 有界 \(M\) 只得有界尺度结论 |
| 固定迹，低频密度统一正下界 | 负井得到非零迹质量 | 移动集中到 \(t=0\) 的迹可隐藏负部，不能再冒称原 Cauchy 迹 |
| 283振荡与284记录转移 [T/R] | 实际源满足(4)的同一序列 | 一般 BV 路径不自动产生算术记录；选择/完备化不制造此输入 |
| 非负 lag 支撑、Poisson、Euler开集及一个已知零点 | (28)--(31)的全尺度定性排除 | 仅记录证明不排除其他序列；无已知极点的 germ 可正常全纯延拓 |

表中 \(\delta_{1/L}\) 例的负部只可能在 \(|t|\ge\pi L/2\)，
且被 \(M_L\) 控制，Cauchy 尾质量 \(O(1/L)\)，故反例界严格成立。
若去掉固定窗口密度，用概率测度 \(\delta_0\) 且 \(M>0\)，则
\(\int P_-\,d\delta_0=0\)。
这些例子只审计一般分析定理，不冒充素数反例。

上同调分次、极化、酉性、全 Weil 正性和统一负指数都未作为公理；
因此结论不是 RH 的同义重述。一般定理292-A适用于有限实 lag 模型；
函数域若满足相同历史条件也可用，但本篇没有验证其实际满足。
Dirichlet、Dedekind 或一般自守情形需分别重建实性/完成项、记录输入和
Poisson--germ 识别，不能从 zeta 例自动推广。

## 7. 决策：原始绝对目标停止，中心化矩线门槛式保留

完整判据132/145/149使用
\[
 s=1/2+\delta_Y+it,\quad \delta_Y>0\to0,\qquad
 \Re\{1/s-\tfrac12\log\pi+\tfrac12\psi(s/2)+I_Y(s)-S_Y(s)\},
 \tag{32}
\]
其中 \(I_Y,S_Y\) 在 \([1,\infty)\) 与全部素数幂上作完整 Abel 平滑。
(2)则固定在中心线左侧，并于 \(Y=N\) 锐截断。
反号和(22)可以精确核验，但**参数迁移和联合尾项尚无小误差定理**。
本篇恰说明不能未经证明把它们叫作微扰。

- [N/停止] 对固定 \(\sigma<1/2\) 的同一原始 \(P_Y\)、反号及仅加固定
  archimedean 项，继续寻找绝对 \(O(1)\) 负迹或合法总上界账本。
  对原始 \(P_Y\)，逼近误差 \(O(1)\)（更一般 \(o(|M|)\)）的平方响应
  也不可能有界；不否定低次数但误差发散的有界响应。
- [O/门槛式保留] 289-(53)中心化四阶预算仍是独立有意义的响应问题，
  292未证明它失败。但在完整接口未通过前，不继续把它标作 RH 存在性的直接推进。
- [O/下一最小任务] 固定一条明确的右侧参数日程
  \(\delta_Y>0,\ \delta_Y\to0\) 及完整 Abel 截断迁移方案，
  先给实际差值的精确分解和292负井上的量化补偿；必须保留原 Cauchy 迹、
  divisor germ、Poisson 条件和全部尾。只把同阶修正重新命名不晋级。
- 晋级条件是独立证明某个此前未控的迁移误差/有符号抵消，或新的严格障碍；
  若仍只有质量相对范数与等价换表示，则暂停289扩写，不恢复已排除的目标。

290的模型非识别和291的通用逼近障碍仍正确；292新增的是**实际源的负迹
定量下界及原始接口的明确止损**。它不否定整个 Weil 纲领。
文献新颖性、发表价值、外部同行评审及 Goal 阶段验收仍 [O]。

## 8. 有限复算与独立审计记录

本轮以 Markdown 为主，不更新 PDF，不启动 DL-AUDIT。

[record_carrier_trace_probe.py](../scripts/record_carrier_trace_probe.py) 使用
mpmath MP50，模型明确为
\[
 H(u)=M\frac{e^{\delta u}-1}{e^{\delta L}-1},\qquad
 \delta=1/8,\quad L=16,32,64,128,256,\quad M=\pm1 .
\]
它是合成 BV 路径，不是实际素数、zeta 零点或认证算术记录。
复算命令为

~~~text
python -B scripts/record_carrier_trace_probe.py
~~~

- 10个有限配置核验 \(A=M-it\widehat g\)、原 \(dH\) 的 cosine transform
  及独立路径积分；最大归一化差约 \(2.76\cdot10^{-51}\)。
- 在 \([-1,1]\) 上按符号变点分段积分，两种质量符号都检验(18)。
  所列 \(L|\text{负迹}-\text{平均主项}|/|M|\) 最大约0.210313，
  对应已证明的有限误差上界常数约38.405981。
  \(L=256\) 两个负迹为约0.0619449146933、0.0619330775999，
  平均主项约0.0619366935751；这些数值不是渐近常数或最优界证书。
- 全轴 Cauchy 均值及二阶矩由精确特征核
  \(e^{-|u-v|}\)、\(e^{-u-v}\) 计算，再独立以 lag 积分复算，
  最大差约 \(1.07\cdot10^{-50}\)；未用有限频率截断冒充全轴。
  此处二阶矩是 \(\tau_C(P^2)\)，不与负迹混同。

脚本作者与主代理各独立运行通过，主代理运行约13秒。
carrier_audit另完整只读审计脚本，核验特征核公式和变点分割。
全部计算只标[E]，不包含浮点区间认证，也不参与
(6)、(12)、(20)、(31)的证明。

主代理重建并审阅全文；carrier_audit、gap_exception_audit 均完整读取
落盘正文并独立逐式逆向复核。已特别核验端点、双质量符号、全轴
Plancherel常数、平均误差、全整数量词、Gamma及原Weil接口。
审计识别并修复了“任意平方响应都不能有界”的过强措辞，
以第4.2节的 \(m=1\) 反例明确保留逼近误差条件。

目录/TeX引用检查及11项目录回归通过；77项注册覆盖和模拟分发检查通过，
不表示重跑了77项重型数学计算。本轮没有据此宣称远程CI已完成。
内部独立复核不替代外部同行评审、文献新颖性或正式Goal阶段验收。
