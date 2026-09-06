# 298. 实际临界窗口、共同端点载波与过快右移障碍

日期：2026-09-06。B1z 亚纯接口周期第2轮；归属：独立 response 论文的有限完成接口。
状态：[T/R] 实际完整端点恒等式与任意载波的负半波下界；[C/RH] 局部共同
载波公式；[T/N] 实际有限完成候选的过快右移日程无条件失败，以及成功日程
的必要下阈值。主证明不使用记录选择或 Littlewood 振荡。
本篇不宣称 RH/GRH、零密度或零点比例改善，也不作为 Goal 阶段完成。

## 1. 实际有限候选、规范迹与完整单包

以下所有截断均匹配：素数幂与连续项使用同一个实端点 \(Y\)，并保留
\(e^{-x/Y}\)。\(\psi(x)=\sum_{n\le x}\Lambda(n)\) 右连续，整数或素数幂
端点取完整权；\(\Lambda(1)=0\)。令
\[
 E(x)=\psi(x)-x+1,\quad E(1)=0,\qquad
 L=\log Y,\quad s=\tfrac12+z,\quad
 w_s(x)=x^{-s}e^{-x/Y}.
 \tag{1}
\]
采用[293 §5](293-poisson-transport-and-right-shifted-record-currents.md)
的实际完成候选
\[
 \begin{split}
 G(s)&=\frac1s-\frac12\log\pi+
                 \frac12\frac{\Gamma'(s/2)}{\Gamma(s/2)},\\
 F_Y^\sharp(z)&=G(s)+\int_1^Y w_s(x)\,dx
                      -\sum_{n\le Y}\Lambda(n)w_s(n).
 \end{split}
 \tag{2}
\]
这里不重复加入 \(1/(s-1)\)，不删除 Gamma 项，不另行归一化实际迹。
写
\[
 z=\delta+it,\quad 0\le\delta\le1/4,\quad q=\delta L,\qquad
 d\mu_C(t)=\frac{dt}{\pi(1+t^2)},
 \quad \kappa_Y(\delta)=\int_{\mathbb R}
       (\Re F_Y^\sharp(\delta+it))_-\,d\mu_C(t).
 \tag{3}
\]
全局正规族接口使用严格的 \(\delta>0\)。\(\delta=0\) 在本篇有限公式中
合法，但不能在引用正规族定理时未经说明地代替严格右移。

后面的局部条件分支固定一个实际临界零点
\(\rho_+=1/2+i\gamma_*\)、\(\gamma_*>0\)，并令
\(\rho_-=\overline{\rho_+}\)、\(m\ge1\) 为各自的完整重数。
在 RH 分支中可任选一个非平凡零点；不用数值高度，也不假定它简单。
定义与[296](296-critical-pole-boundary-layer-and-shift-schedule.md)完全相同的包
\[
 \begin{split}
 F_L(z)&=2\int_0^L e^{-zu-e^{u-L}}\cos(\gamma_*u)\,du\\
       &=\sum_{\rho\in\{\rho_+,\rho_-\}}
                       \int_1^Y x^{\rho-1}w_s(x)\,dx,\\
 R_{\delta,L}(t)&=\Re F_L(\delta+it).
 \end{split}
 \tag{4}
\]
包从 \(x=1\) 起，含匹配 Abel 权及全部上端；不是只保留极限有理函数。
实际联合余项为
\[
 \mathcal B_Y(z)=F_Y^\sharp(z)-mF_L(z).
 \tag{5}
\]
它与296的任意背景函数之间的关系必须另证；不因一个有限极点已被移除就
默认为尺度一致有界。

## 2. 完整端点与 RH 条件局部载波

### 2.1 无条件的实际 Stieltjes 恒等式 [T]

置
\[
 E_*(x)=E(x)+m\sum_{\rho\in\{\rho_+,\rho_-\}}
                         \frac{x^\rho-1}{\rho}.
 \tag{6}
\]
因此 \(E_*(1)=0\)、\(E_*\) 为实函数，且只减去显式公式中这两个零点
贡献的连续模式；实际素数幂跳跃没有改变。由(2)、(4)直接得
\[
 \mathcal B_Y(z)=G(s)-\int_{(1,Y]}w_s(x)\,dE_*(x).
 \tag{7}
\]
右连续 Stieltjes 分部积分给
\[
 \boxed{\quad
 \mathcal B_Y(z)=G(s)-e^{-1}Y^{-s}E_*(Y)
 -\int_1^Y E_*(x)x^{-s-1}e^{-x/Y}(s+x/Y)\,dx.
 \quad}
 \tag{8}
\]
共同端点载波没有额外的 \(s\) 因子；\(s\) 只出现在内部核中。
式(8)对实数及整数 \(Y>1\) 均成立，端点原子取完整权。

### 2.2 只对补偿核使用绝对零点和 [T/R]

为与[285 §2](285-shallow-zero-deletion-and-finite-deep-response.md)精确衔接，
设 \(Y\ge2\)，并记
\[
 C_*=1-\frac{\zeta'(0)}{\zeta(0)}
             -m\sum_{\rho\in\{\rho_+,\rho_-\}}\frac1\rho,
 \qquad T_0(x)=-\tfrac12\log(1-x^{-2}).
 \tag{9}
\]
对其余实际零点，含重数，定义
\[
 I_\rho(s)=\frac1\rho\int_2^Y x^\rho w_s'(x)\,dx.
 \tag{10}
\]
明确的固定早段与补偿项为
\[
 \begin{split}
 D_{12,*}(s)={}&\Lambda(2)w_s(2)-\int_1^2w_s(x)\,dx
       +m\sum_{\rho\in\{\rho_+,\rho_-\}}
                    \int_1^2x^{\rho-1}w_s(x)\,dx,\\
 B_*(s)={}&D_{12,*}(s)-w_s(2)E_*(2)
       -C_*\{w_s(Y)-w_s(2)\}-\int_2^YT_0(x)w_s'(x)\,dx.
 \end{split}
 \tag{11}
\]
则有精确式
\[
 \boxed{\quad
 \mathcal B_Y(z)=G(s)-B_*(s)-e^{-1}Y^{-s}E_*(Y)
                    -\sum_{\rho\notin\{\rho_+,\rho_-\}}I_\rho(s).
 \quad}
 \tag{12}
\]
和式移除该共轭对的全部 \(m\) 重；其余零点仍按重数计。

证明。将(7)拆成 \((1,2]\) 与 \((2,Y]\)，只在第二段的普通积分中使用
285已经审计的半权显式公式。在普通积分内，几乎处处有
\[
 E_*(x)=-\sum_{\rho\notin\{\rho_+,\rho_-\}}\frac{x^\rho}{\rho}
                        +C_*+T_0(x),
 \tag{13}
\]
这里的未积分表达式按对称高度极限解释。先固定 \(Y,s\)，再令高度趋于
无穷；282/285的截断误差支配收敛论证给出(12)。积分后的(10)对固定 \(Y\)
及紧 \(s\) 集绝对可和：实部 majorant \(1\) 和一次振荡分部积分给高处
\(O_{Y,s}(|\gamma|^{-2})\)，再用标准单位高度零点计数。
不曾在原子端点对 \(\sum Y^\rho/\rho\) 取绝对值。

\(n=2\) 的全权原子只在 \(D_{12,*}\) 的首项出现一次。又因
\(T_0'(x)=-1/[x(x^2-1)]\)，再次分部积分
\[
 \int_2^YT_0w_s'=[T_0w_s]_2^Y-\int_2^YT_0'w_s
 \tag{14}
\]
说明 \(B_*(s)=O_{\gamma_*,m}(1)\)，统一于 \(Y\ge2\)、
\(\Re s\in[1/2,3/4]\) 及全部实 \(\Im s\)。在固定紧频窗 \(J\) 上，
\(G(s)=O_J(1)\)，这是 Gamma 对数导数在相应紧集无极点的直接结果。
本节无须 RH；RH 只在下一节控制剩余谱的振幅。\(\square\)

式(12)与[297](297-raw-pole-endpoint-splitting-obstruction.md)一致：
若将 \(I_\rho\) 再拆成原始核和两个端点，原始复核的逐项 Cauchy 绝对和
发散。因此不能先对那些原始核求绝对值，再声称共同载波已经消失。

### 引理298-A：实际局部载波 [C/RH]

假设 RH。令 \(J\) 为固定正宽紧区间，并要求
\[
 \operatorname{dist}\bigl(J,
 \{\Im\rho:\rho\text{ 是未移除的实际零点}\}\bigr)>0.
 \tag{15}
\]
该区间可以包含已经移除的 \(\gamma_*\) 或 \(-\gamma_*\)。则统一于
\(Y\ge4\)、\(0\le\delta\le1/4\)、\(t\in J\)，
\[
 \mathcal B_Y(\delta+it)
                  =-e^{-1}Y^{-1/2-\delta-it}E(Y)+O_J(1),
 \tag{16}
\]
从而
\[
 \boxed{\quad
 \Re F_Y^\sharp(\delta+it)
   =mR_{\delta,L}(t)-a_Y\cos(Lt)+O_J(1),\qquad
 a_Y=e^{-1-q}\frac{E(Y)}{\sqrt Y}\in\mathbb R.
 \quad}
 \tag{17}
\]
常数允许依赖固定的包、\(m\)、窗口及其谱间隔，但不依赖 \(Y,\delta,t\)
或端点幅度 \(E(Y)\)。没有假设 \(a_Y\) 小、有界或具有某一符号。

证明。在 RH 下，每个零点写成 \(1/2+i\gamma\)。换元 \(u=\log x\) 得
\[
 I_\rho(s)=-\frac1\rho\int_{\log2}^{L}
      e^{i(\gamma-t)u}(s+e^{u-L})h(u)\,du,
 \qquad h(u)=e^{-\delta u-e^{u-L}}.
 \tag{18}
\]
\(h\) 在区间内递减，零延拓后的总变差至多2。
\(v=e^{u-L}\in[0,1]\) 单调，\(TV(vh)\le C\)；因 \(s\) 留在固定紧集，
\[
       TV\bigl((s+e^{u-L})h\,\mathbf1_{[\log2,L]}\bigr)\le C_J.
 \tag{19}
\]
因此利用(15)，每个未移除零点满足
\[
 |I_\rho(s)|\le\frac{C_J}{|\rho|\,|\gamma-t|}.
 \tag{20}
\]
有限低零点由(15)控制，高处为 \(O_J(\gamma^{-2})\)。含重数的单位高度
\(O(\log(2+|\gamma|))\) 上界使这些估计绝对可和，于是
\(\sum_{\rm rest}I_\rho(s)=O_J(1)\)，统一于全部所述参数。
再由(6)，\(E_*(Y)-E(Y)=O_{\gamma_*,m}(\sqrt Y)\)，而 \(\delta\ge0\)
使它乘上 \(Y^{-1/2-\delta}\) 后仍为 \(O(1)\)。代入(12)即得(16)--(17)。
\(\square\)

非 RH 情形不能使用(19)：振幅会多出 \(e^{(\Re\rho-1/2)u}\)，固定的
物理高度间隔并不消除其随 \(Y\) 增长的大小。复平面中的单点孤立性也不
自动排除另一个实部不同但高度相同的零点。因此(15)在这里明确属于 RH
条件分支；若需要在任意正宽区间上应用下界，可在该分支内选一个正宽子窗
避开未移除高度，不能将该选择提前当作无条件谱输入。

### 2.3 局部背景与同一记录的诊断 [C/RH]

对满足(15)的 \(J\)，一个有界周期函数原函数的分部积分给
\[
 \int_J|\cos(Lt)|\,d\mu_C(t)
       =\frac2\pi\mu_C(J)+O_J(L^{-1}).
 \tag{21}
\]
由(16)，存在 \(c_J,C_J>0\)，使充分大的 \(Y\) 满足
\[
 c_J|a_Y|-C_J
 \le\int_J|\Re\mathcal B_Y(\delta+it)|\,d\mu_C(t)
 \le C_J(1+|a_Y|).
 \tag{22}
\]
故该局部 \(L^1\) 背景一致有界，当且仅当
\(e^{-q}|E(Y)|/\sqrt Y=O(1)\)。仅仅删掉一个临界包没有证明该条件。

作为短诊断，另固定 \(0<\sigma_0<\beta<1/2\)、\(d=1/2-\sigma_0\)。
[283-D](283-fixed-cutoff-abel-mass-oscillation.md)在 RH 下保留完整端点给
\[
 M_{\sigma_0}(Y,Y)=e^{-1}Y^{-\sigma_0}E(Y)+O_{\sigma_0}(Y^d).
 \tag{23}
\]
该文用 \(\psi-Y\) 写端点；换为 \(E=\psi-Y+1\) 只改变
\(O(Y^{-\sigma_0})\)。其证明是把普通积分中每个零点的 \(1/\rho\)
与正数 \(d\) 下的 BV 衰减合用，并非直接采用 RH 的点态 PNT 上界。
因此在[284](284-causal-abel-inverse-and-diagonal-record-selection.md)
同一记录上，
\[
 a_Y=e^{-q}\frac{M_{\sigma_0}(Y,Y)}{Y^d}+O(e^{-q}),
 \qquad |M_{\sigma_0}(Y,Y)|\ge cY^d\ell(Y),\quad\ell(Y)\to\infty.
 \tag{24}
\]
固定 \(q>0\) 时，(22)在这条记录上发散。这一记录结论严格标为
[C/RH]，不把全尺度与指定子序列的量词互换；后面的主结论不以记录选择
或 Littlewood 振荡为证明输入。

## 3. 完整负半周期消去任意共同载波 [T]

### 引理298-B

固定 \(\gamma>0\)、\(m>0\)、\(0<H<\min(\gamma/3,1/4)\)，令
\[
 J=[\gamma-H,\gamma+H],\qquad p_*=
               \min_{t\in J}\frac1{\pi(1+t^2)}>0.
 \tag{25}
\]
在本节的 \(R_{\delta,L}\) 中用 \(\gamma\) 作模式高度。对充分大的 \(L\)，
统一于 \(0\le q\le\log\log L\)、\(\delta=q/L\) 和所有 \(a\in\mathbb R\)，
\[
 \boxed{\quad
 \int_J[mR_{\delta,L}(t)-a\cos(Lt)]_-\,d\mu_C(t)
 \ge\frac{2p_*m}{\pi}e^{-q}\log\frac{L}{1+q}-C_{\gamma,m,H}.
 \quad}
 \tag{26}
\]
常数不依赖 \(a\)；不假设载波小，也不先付 \(|a|\) 乘以密度导数的误差。

证明。置 \(M_L=\lfloor HL/(2\pi)\rfloor\)、\(X=2\pi M_L\)，取窗口内
关于 \(\gamma\) 对称的完整负正弦半周期
\[
 S_L=\bigcup_{k=0}^{M_L-1}
 \left\{\gamma\pm h:
  \frac{(2k+1)\pi}{L}\le h\le\frac{(2k+2)\pi}{L}\right\}\subset J.
 \tag{27}
\]
关于 \(h=0\) 的对称性消去 \(\sin(L\gamma)\sin(Lh)\)，而每个完整
半周期上 \(\cos(Lh)\) 的积分为零。因此无权 Lebesgue 积分满足
\[
                      \int_{S_L}\cos(Lt)\,dt=0.
 \tag{28}
\]
对 \(f=mR_{\delta,L}-a\cos(Lt)\)，于是有
\[
 \int_J f_-\,d\mu_C\ge p_*\int_{S_L}f_-dt
       \ge-p_*\int_{S_L}fdt
       =-p_*m\int_{S_L}R_{\delta,L}(t)dt.
 \tag{29}
\]
载波精确消失，规范迹并未改变。

296的有限积分计算给矩形核
\[
 C^0_{\delta,L}(h)
 =\frac{\delta+e^{-q}\{h\sin(Lh)-\delta\cos(Lh)\}}
        {\delta^2+h^2};
 \tag{30}
\]
\(\delta=0\) 时按 \(\sin(Lh)/h\) 连续解释。
完整 Abel 双模与两个矩形核之差逐点至多 \(2e^{-q}/(1-\delta)\)，
这是296-(10)的有限权差。在 \(t=\gamma+h\in J\) 上，另一中心的矩形核
\(C^0_{\delta,L}(2\gamma+h)=O_\gamma(\delta+e^{-q})\)。这些项在(29)
只付 \(O_{\gamma,m,H}(1)\)。Poisson 项的全轴普通积分为 \(\pi\)，
余弦校正的绝对积分至多 \(\pi e^{-q}\)；\(\delta=0\) 时两项为零。
所以，令 \(g(y)=(-\sin y)_+\)，有
\[
 -\int_{S_L}R_{\delta,L}(t)dt
 \ge 2e^{-q}\int_0^X g(y)\frac{y}{q^2+y^2}dy-C_{\gamma,H}.
 \tag{31}
\]

\(g\) 在 \([0,\pi]\) 上为零，周期平均为 \(1/\pi\)，去均值原函数有界。
对 \(v_q(y)=y/(q^2+y^2)\)、\(y\ge\pi\)，
\(\sup|v_q|\le1/\pi\)、\(TV(v_q)\le2/\pi\)：其导数至多变号一次，
且 \(v_q(\infty)=0\)。分部积分给，统一于 \(0\le q\le X\)，
\[
 \begin{split}
 \int_0^X g(y)\frac{y}{q^2+y^2}dy
 &=\frac1{2\pi}\log\frac{q^2+X^2}{q^2+\pi^2}+O(1)\\
 &=\frac1\pi\log\frac{X}{1+q}+O(1).
 \end{split}
 \tag{32}
\]
第二个误差一致，因为 \(q/X\le1\)，且
\((1+q)/\sqrt{q^2+\pi^2}\) 留在固定正紧区间。本引理的参数范围保证
最终 \(q\le X\)、\(X\asymp_H L\)、\(\delta\le1/4\)。代入(29)--(31)，
吸收固定的 \(\log H\) 项，得到(26)。\(\square\)

检验集仅用于给负部积分的下界，不是宣称真实负谱投影等于该集合。

## 4. 实际过快日程无条件失败 [T/R/N]

### 4.1 RH 分支的全尺度定量下界 [C]

在 RH 分支内任选实际非平凡零点 \(1/2+i\gamma_*\)，计其全部重数 \(m\)。
零点存在由[297-(10)](297-raw-pole-endpoint-splitting-obstruction.md)所引
经典计数给出，不需要指定数值高度。RH下零点高度离散，故可取
固定 \(H\) 使 \(J=[\gamma_*-H,\gamma_*+H]\) 满足(15)、(25)。
引理298-A、298-B及负部的 \(L^1\)-Lipschitz 性给
\[
 \boxed{\quad
 \kappa_Y(\delta)\ge c_*e^{-q}\log\frac{L}{1+q}-C_*,
 \qquad 0\le q\le\log\log L,
 \quad}
 \tag{33}
\]
其中 \(c_*>0\)，常数与 \(Y,q,E(Y)\) 无关。证明只把(17)中一致
\(O_J(1)\) 余项吸收到常数，并用全轴负迹大于局部负迹；端点振幅可以
任意大。这里没有调用 PNT 振荡、历史 guard 或记录选择。

### 定理298-C：实际候选的必要日程门槛 [T/N]

对(2)的原始匹配 sharp--Abel 完成候选，有以下无条件结论。

1. 对任何 \(Y_j\to\infty\)、\(\delta_j>0\) 的序列，若
   \[
   q_j=\delta_j\log Y_j,\qquad
   q_j-\log\log\log Y_j\longrightarrow-\infty,
   \tag{34}
   \]
   则 \(\kappa_{Y_j}(\delta_j)\to\infty\)。
2. 对任何 \(Y_j\to\infty\)、\(\delta_j>0\to0\) 的序列，若
   \(\sup_j\kappa_{Y_j}(\delta_j)<\infty\)，则必有
   \[
       \delta_j\log Y_j\ge\log\log\log Y_j-O(1).
   \tag{35}
   \]

证明。293-E已经独立验证每个 \(F_Y^\sharp\) 在右半平面全纯、满足
Poisson admissibility，并在 \(\Re z>1/2\) 局部一致收敛到
\(\xi'/\xi(1/2+z)\) 的 Euler 开集 germ。因此
[145定理ZT](145-bounded-defect-normality.md)给
\[
 \left.
 \begin{gathered}
 Y_j\to\infty,\quad\delta_j>0\to0,\\
 \sup_j\kappa_{Y_j}(\delta_j)<\infty
 \end{gathered}
 \right\}\quad\Longrightarrow\quad\mathrm{RH}.
 \tag{36}
\]
这只引用分析定理及实际候选的独立适用性，没有把有界负迹当作已证公理。

若第一条失败，取负迹有界的子序列。(34)保证最终
\(0<q_j\le\log\log L_j\)、\(\delta_j\to0\)，故(36)推出 RH。
在该分支内，对同一子序列用(33)得到
\[
 \kappa_{Y_j}(\delta_j)
 \ge c_*e^{-q_j}\log L_j\,(1-o(1))-C_*
 \longrightarrow\infty,
 \tag{37}
\]
因为 \(\log(1+q_j)=o(\log L_j)\)，且
\(e^{-q_j}\log L_j=\exp(\log\log L_j-q_j)\to\infty\)。矛盾证明第一条。
这里先由假定的有界子序列推出RH，再使用条件性局部公式，没有在无条件
谱和中偷用RH。

对第二条，先用(36)。若 \(q_j>\log\log L_j\)，(35)已成立；其余指标
由(33)及最终 \(\log(L_j/(1+q_j))\ge\tfrac12\log L_j\) 得
\(e^{-q_j}\log L_j=O(1)\)，即(35)。\(\square\)

同一证明允许 \(Y_j\) 全为整数，不需要连续尺度 Mellin 变换或取整。
这是实际源的日程障碍，不只是有限模式的反例。第一条无条件结论只声称
发散；(33)的显式速率仍标为[C/RH]，没有借逻辑二分宣称无条件速率。

固定 \(q>0\) 的 \(\delta=q/\log Y\) 是第一条特例。(35)只是必要下阈值，
不是充分条件，更不声称实际最优日程已经确定。293的RH条件安全日程
\(\delta\log Y=(5/2)\log\log Y\) 仍远大于此门槛。
主定理明确要求 \(\delta_j>0\)，不经未写出的边界 Poisson 步骤加入
\(\delta_j=0\)。

## 5. 固定有限中心模式减法仍不能修复过快日程 [T/N]

固定有限多个 \(\gamma_1,\ldots,\gamma_k>0\) 与实系数
\(c_1,\ldots,c_k\)，均不随 \(Y\) 改变；允许这些高度并非实际零点。
令 \(F_{L,\gamma_r}\) 为(4)在高度 \(\gamma_r\) 的同一有限核，并设
\[
 \widetilde F_Y(z)=F_Y^\sharp(z)-\sum_{r=1}^k c_rF_{L,\gamma_r}(z),
 \qquad
 \widetilde\kappa_Y(\delta)
   =\int(\Re\widetilde F_Y(\delta+it))_-\,d\mu_C(t).
 \tag{38}
\]
定理298-C两条结论对 \(\widetilde\kappa\) 同样成立。

证明。每个新增核在 \(\Re z\ge0\) 的模至多 \(2L\)，且为 entire、
real-type。Gamma项不变，故293-E的Poisson证明仍适用：固定 \(Y,\delta>0\)，
有限部分在右半平面有界，而 \(\Re G\) 在大半圆上一致趋于正无穷。
负边界部连续且最终紧支撑；加回其Poisson积分，对半圆用最小值原理即得
admissibility。这不是把两个Poisson下界直接相减。

新的 Euler 开集 germ 是
\[
 \frac{\xi'}\xi(1/2+z)-Q(z),\qquad
 Q(z)=\sum_{r=1}^k c_r
  \left\{\frac1{z-i\gamma_r}+\frac1{z+i\gamma_r}\right\}.
 \tag{39}
\]
\(Q\) 在整个右半平面全纯。有界负迹子序列由145的分析部分给出这个germ
的全右半平面全纯延拓；加回 \(Q\) 后 \(\xi'/\xi\) 也在此全纯，函数
方程遂给RH。没有把任意实系数 \(c_r\) 解释为新的整数除子。

在RH分支内，经典零点计数允许选一个不在该有限高度列表中的实际零点，
并在其附近取同时避开其余实际高度和上述有限列表的固定窗。
每个减去的有限模式在该窗内一致有界：矩形核
的分母与零分离，296-(10)的Abel差亦为 \(O(1)\)。所以(17)对
\(\widetilde F_Y\) 仍成立，只改变有界余项。298-B给同样的(33)，重复
298-C的反证及阈值推导即可。\(\square\)

本节仅覆盖固定数目、固定高度、固定实系数与同一sharp--Abel核的减法，
不覆盖增长模式包、随尺度改变的任意修正或更换有限权。296的三角权在
单包模型中确能消去边界层，不能被本节排除。

## 6. 依赖、循环性与下一最小输入

- [T/R] 实际源、Gamma及两个完整端点在(1)--(14)保留；只对补偿零点和
  使用绝对求和。经典显式公式和单位高度计数沿用282/285。
- [C/RH] RH仅用于(18)--(20)的一致变差及局部载波，进而用于(33)。
  同一记录的(24)也是条件诊断，不是全局主证明的输入。
- [T] 完整负半周期(27)--(32)消去任意实共同载波，没有要求 \(E(Y)\) 小。
- [T/N] 只有在假定存在有界子序列后，才由293/145推出RH并使用条件下界。
  所排除的是指定实际有限正则化的一类过快日程，不是RH或所有Weil配置。
- [O] 下一最小实际输入是临界或更慢靠线日程的共同载波与全谱联合预算。
  \(q\) 更大意味着 \(\delta=q/L\) 更大，即向中心线靠近得更慢；本篇
  没有证明临界尺度 \(q\asymp\log\log L\) 已充分。

一个下轮候选（本篇未证明）是核验RH条件下的全轴误差能否被
\(e^{-q}|E(Y)|/\sqrt Y+e^{-q}\log(2+1/\delta)+Y^{-1/2-\delta}\)
控制，再检查小端点整数截断是否使临界门槛达到。该候选仍为[O]，不得
引用为本轮定理，也不产生无条件零点比例或零密度改进。

本轮没有新的零自由区、零密度或零点比例，没有上同调构造，也没有将两类
Weil结构认作等价。文献新颖性、外部同行审查与Goal阶段验收仍未完成。

## 7. 计算与独立审计登记

配套有限复算见
[critical_carrier_test_probe.py](../scripts/critical_carrier_test_probe.py)。
它检验完整负半周期的载波消去与有限矩形/Abel积分，输出的是检验集下界
泛函而非完整 \(\kappa\)；负的有限下界也如实保留。所有计算只标[E]，
不用于上述统一证明，也不认证真实零点高度或记录。
九组 MP50 合成参数由脚本作者与主代理各自运行通过；主代理复算的载波
消去残差不超过 \(2.51\cdot10^{-52}\)，矩形原函数与独立 Fubini 积分的
缩放差不超过 \(2.71\cdot10^{-50}\)，Abel 展开误差与已证阶乘尾上界之比
不超过 \(7.99\cdot10^{-4}\)。这些只验证有限恒等式和实现，不承担渐近证明。

全文由主代理、gap_exception_audit 与 midband_compute 分别逆向复核通过。
重点核验了两个完整端点、共同载波的精确消去、统一 \(q\) 范围、
有界子序列推出 RH 后才使用条件下界的逻辑，以及有限模式减法后重新证明
Poisson admissibility 的步骤。内部复核不等于外部同行评审。

仓库布局检查、11项布局回归及77项检查的注册/mock调度核验均通过；
未重跑77项重型计算。本稿保持Markdown，本轮不更新PDF。
