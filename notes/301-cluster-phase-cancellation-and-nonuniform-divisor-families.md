# 301. 临界簇的相位抵消与除子族的非一致性

日期：2026-09-06。B1z 亚纯接口周期第4轮。
状态：[T] 固定有限簇的精确合尾、相位主项及一致误差；
[N] 两个随尺度靠近的中心极点对消掉单包对数主项。
本文验证[300-(50)](300-endpoint-separated-global-error-and-critical-schedule.md)
的有限模型猜测。所有移动高度都是明确给定的模型参数，不是实际
Riemann zeta 零点的假设，不以此推翻300的固定实际谱结论。

## 1. 固定参数、完整 Abel 核与待估计量

固定正整数 \(J\)、实数 \(h_1,\ldots,h_J\)、非负实权
\(m_1,\ldots,m_J\) 及 \(\gamma>0\)。记
\[
 M=\sum_{j=1}^Jm_j,\qquad
 H=\max_j|h_j|,\qquad H_1=\sum_{j=1}^Jm_j|h_j|,
 \qquad B=\sum_{j=1}^Jm_je^{-ih_j}.
 \tag{1}
\]
允许零权；若 \(M=0\)，以下结论均为平凡恒等式。
固定簇指 \(J,h_j,m_j,\gamma\) 均不随 \(L\) 改变；
真正的极点高度为
\[
 Y=e^L,\qquad \omega_j(L)=\gamma+h_j/L,\qquad
 \delta>0,\quad q=\delta L,\quad \varepsilon=e^{-q}.
 \tag{2}
\]
当 \(L\) 充分大时，全部 \(\omega_j(L)>0\)。重复高度允许合并其权。
采用与[296](296-critical-pole-boundary-layer-and-shift-schedule.md)
相同的完整下端 \(u=0\)、sharp 上端 \(u=L\) 及 Abel 权：
\[
 \begin{split}
 C_{\delta,L}^{A}(v)
   &=\int_0^L e^{-\delta u-e^{u-L}}\cos(vu)\,du,\\
 R_{\omega,\delta,L}(t)
   &=2\int_0^L e^{-\delta u-e^{u-L}}\cos(\omega u)\cos(tu)\,du\\
   &=C_{\delta,L}^{A}(t-\omega)+C_{\delta,L}^{A}(t+\omega),\\
 \mathcal R_L(t)&=\sum_{j=1}^Jm_jR_{\omega_j(L),\delta,L}(t).
 \end{split}
 \tag{3}
\]
这是整个有限核的实部：
\[
 F_{L,\omega}(z)=2\int_0^L e^{-zu-e^{u-L}}\cos(\omega u)\,du,
 \qquad R_{\omega,\delta,L}(t)=\Re F_{L,\omega}(\delta+it).
 \tag{4}
\]
不切去 \([0,\log2]\)，不添减另一个背景，也不改变 Cauchy 迹：
\[
 p(t)=\frac1{\pi(1+t^2)},\qquad d\mu_C(t)=p(t)\,dt,\qquad
 \tau_C|f|=\int_{\mathbb R}|f|\,d\mu_C,\qquad
 \kappa_-(f)=\int_{\mathbb R}f_-\,d\mu_C .
 \tag{5}
\]
第2节的精确界适用于 \(0<\delta\le1/4,\ q\ge1\)；
第3节另固定 \(A>0\)，研究
\(1\le q\le A\log\log L\) 的统一渐近。后一区间在充分大 \(L\)
时自动满足 \(\delta=q/L\le1/4\)。

权的非负性用于保留非负 Poisson 背景。若要把 \(m_j\) 称为整函数
零点的重数，还须要求 \(m_j\) 为非负整数；正实非整数权只是正残数
核的权，不自动对应一个单值整函数除子。

## 2. 精确矩形分解、合尾与零相位和

### 2.1 Abel 与矩形的比较 [T]

令
\[
 C_{\delta,L}^{0}(v)=\int_0^L e^{-\delta u}\cos(vu)\,du
 =\frac{\delta}{\delta^2+v^2}
    -\varepsilon\Re\frac{e^{iLv}}{\delta-iv}.
 \tag{6}
\]
这是精确恒等式；右边第二项等于
\(\varepsilon\{v\sin(Lv)-\delta\cos(Lv)\}/(\delta^2+v^2)\)。
由 \(0\le1-e^{-x}\le x\)，对全部实 \(v\) 有
\[
 |C_{\delta,L}^{A}(v)-C_{\delta,L}^{0}(v)|
 \le\int_0^L e^{-\delta u}e^{u-L}\,du
 =\frac{\varepsilon-e^{-L}}{1-\delta}
 \le\frac{\varepsilon}{1-\delta}.
 \tag{7}
\]
用 \(C^0\) 替换(3)中的 \(C^A\)，所得完整簇记为
\(\mathcal R_L^0\)。于是既有全轴点态界，也有 Cauchy 界
\[
 |\mathcal R_L-\mathcal R_L^0|
 \le\frac{2M\varepsilon}{1-\delta},\qquad
 |\kappa_-(\mathcal R_L)-\kappa_-(\mathcal R_L^0)|
 \le\frac{2M\varepsilon}{1-\delta}.
 \tag{8}
\]
最后一步用负部的 \(L^1\)-Lipschitz 性和 \(\mu_C(\mathbb R)=1\)。
这里比较的两个积分都从0开始、都包含全部上端；没有把 Abel 权在
上端的值替换成1后宣称误差为零。

### 2.2 两个中心的振荡尾必须先相加 [T]

在 \(+\gamma\) 中心令 \(y=L(t-\gamma)\)，定义
\[
 c_j=m_je^{-ih_j},\qquad
 S_+(y)=\sum_{j=1}^J\frac{c_j}{q-i(y-h_j)}.
 \tag{9}
\]
由(6)，这个中心所对应的 \(J\) 项精确等于
\[
 L\sum_{j=1}^J\frac{m_jq}{q^2+(y-h_j)^2}
              -\varepsilon L\,\Re\{e^{iy}S_+(y)\}.
 \tag{10}
\]
第一项非负。另一中心令 \(y=L(t+\gamma)\)；只需同时替换
\(h_j\mapsto-h_j\)、\(c_j\mapsto\overline{c_j}\)，得到同一公式，
其相位和为 \(\overline B\)。因此两侧的主振荡幅度都为 \(|B|\)，
不是两组独立的 \(\sum m_j\)。

共同分母的合尾恒等式为
\[
 S_+(y)=\frac{B}{q-iy}+Z_+(y),\qquad
 Z_+(y)=\sum_{j=1}^J
       \frac{-ih_jc_j}{(q-iy)\{q-i(y-h_j)\}} .
 \tag{11}
\]
由 Cauchy--Schwarz 和平移不变性，
\[
 \begin{split}
 \int_{\mathbb R}|Z_+(y)|\,dy
 &\le \sum_jm_j|h_j|
 \left(\int_{\mathbb R}\frac{dy}{q^2+y^2}\right)^{1/2}
 \left(\int_{\mathbb R}\frac{dy}{q^2+(y-h_j)^2}\right)^{1/2}\\
 &=\frac{\pi H_1}{q}.
 \end{split}
 \tag{12}
\]
负中心的 \(Z_-\) 同界。设 \(W_L\) 是两个 \(Z\) 项对完整实簇的贡献；
变元 \(dt=dy/L\) 给
\[
 \int_{\mathbb R}|W_L(t)|\,dt\le\frac{2\pi\varepsilon H_1}{q},
 \qquad
 \tau_C|W_L|\le\frac{2\varepsilon H_1}{q}.
 \tag{13}
\]
第二式只用 \(p(t)\le1/\pi\)，不要求两个中心相隔很远，也不依赖
任何“任意系数 Bessel 界”。这是所定义的两个振荡尾相加后的精确差核估计。

为后文记号方便，令
\[
 T_{\alpha,b}(t)
   =-\varepsilon L\Re\frac{b\,e^{iL(t-\alpha)}}
                                  {q-iL(t-\alpha)}.
 \tag{14}
\]
则全实轴有精确分解
\[
 \mathcal R_L^0(t)=P_L(t)
             +T_{\gamma,B}(t)+T_{-\gamma,\overline B}(t)+W_L(t),
 \quad
 P_L(t)=\sum_jm_j
  \left\{\frac{\delta}{\delta^2+(t-\omega_j)^2}
             +\frac{\delta}{\delta^2+(t+\omega_j)^2}\right\}\ge0.
 \tag{15}
\]
式(13)控制的是 \(W_L\)，不是单独丢弃原簇中的各个振荡尾。

### 2.3 零相位和的全轴显式界 [T]

**命题301-A。** 若 \(B=0\)，则
\[
 \boxed{\quad
 \kappa_-(\mathcal R_L)
       \le\frac{2\varepsilon H_1}{q}
                         +\frac{2M\varepsilon}{1-\delta},
 \qquad 0<\delta\le\tfrac14,\quad q=\delta L\ge1 .
 \quad}
 \tag{16}
\]
本界事实上允许任意实 \(\gamma\)，无需中心分离，也不要求
\(q\le A\log\log L\)。

证明。此时(15)中的两个 \(T\) 项恰好为零。由于 \(P_L\ge0\)，
\((P_L+W_L)_-\le|W_L|\)。积分后用(13)，再用(8)，即得(16)。
\(\square\)

所以 \(B=0\) 时有真正的 \(O_{\mathbf h,\mathbf m}(\varepsilon)\)
负迹，而不是仅由第3节带有 \(q\) 的误差推出这一加强。
本证明保留了全部正 Poisson 项，只在上界中合法地利用它们。

## 3. 一般相位和的完整主项 [T]

### 定理301-B

固定第1节的参数与 \(A>0\)。当 \(L\to\infty\)，一致于
\(1\le q\le A\log\log L,\ \delta=q/L\)，有
\[
 \boxed{\quad
 \kappa_-(\mathcal R_L)
 =\frac4{\pi^2(1+\gamma^2)}|B|\,
                   e^{-q}\log L
  +O_{\gamma,J,\mathbf h,\mathbf m,A}
       \bigl(e^{-q}[1+q+\log(1+q)]\bigr).
 \quad}
 \tag{17}
\]
尤其除以 \(e^{-q}\log L\) 后，统一极限为
\(4|B|/[\pi^2(1+\gamma^2)]\)。当 \(B=0\) 时，(16)更强。
不把(17)写成对任意增长个数或增长 \(h_j,m_j\) 的一致估计。

### 3.1 相位平均与单个共同振荡尾

对任意实相位 \(\theta\)，周期函数
\((\pm\sin(y+\theta))_+\) 的平均值均为 \(1/\pi\)，
减去均值后的原函数可一致选为有界。因此分部积分给
\[
 \int_r^R\frac{(\pm\sin(y+\theta))_+}{y}\,dy
       =\frac1\pi\log\frac Rr+O(r^{-1}),
           \qquad R\ge r\ge1,
 \tag{18}
\]
隐常数与相位、正负号无关。这里不要求相位固定为0，也不只选取一个
宽度 \(O(L^{-1})\) 的峰。

写 \(y=L(t-\alpha)\)。对(14)直接展开：
\[
 T_{\alpha,b}(t)
 =\varepsilon L
 \frac{y\,\Im(be^{iy})-q\,\Re(be^{iy})}{q^2+y^2}.
 \tag{19}
\]
在 \(|y|\le q\) 内，
\(\int |T_{\alpha,b}|\,dt\le C\varepsilon|b|\)。
在 \(|y|\ge r\ge q\) 上，将(19)换为
\(\varepsilon L\,\Im(be^{iy})/y\)，其普通 \(L^1(dt)\) 误差至多
\[
 2\varepsilon|b|\int_r^\infty
 \left\{\frac q{q^2+y^2}
       +\frac{q^2}{y(q^2+y^2)}\right\}dy
       \le C\varepsilon|b|.
 \tag{20}
\]
所有分母误差已包含在内；没有把 \(q\) 直接设为0。

固定 \(0<a<1\)。在 \(|t-\alpha|\le a\) 上，
\(p(t)=p(\alpha)+O_{\alpha,a}(|t-\alpha|)\)。
这一权差作用于
\(\varepsilon\,\Im(be^{iL(t-\alpha)})/(t-\alpha)\)
的 Cauchy 积分仅为 \(O_{\alpha,a}(\varepsilon|b|)\)。
结合(18)--(20)，对 \(aL\ge r\ge q\ge1\)，两个环段满足
\[
 \int_{r/L\le|t-\alpha|\le a}(T_{\alpha,b}(t))_-\,d\mu_C(t)
 =\frac{2p(\alpha)|b|}{\pi}\,
          \varepsilon\log\frac{aL}{r}
            +O_{\alpha,a}(\varepsilon|b|).
 \tag{21}
\]
两侧的相位和符号可能不同，但(18)给相同平均值。
此外，在 \(|t-\alpha|\ge a\) 上，
\[
 |T_{\alpha,b}(t)|\le
       \frac{\varepsilon|b|}{|t-\alpha|},\qquad
 \int_{|t-\alpha|\ge a}|T_{\alpha,b}|\,d\mu_C
                 \le C_{\alpha,a}\varepsilon|b|.
 \tag{22}
\]
取 \(r=q\)，加回核心及外侧，得到在 \(q\le aL\) 时
\[
 \kappa_-(T_{\alpha,b})
 =\frac{2p(\alpha)|b|}{\pi}\,
            \varepsilon\log(L/q)+O_{\alpha,a}(\varepsilon|b|).
 \tag{23}
\]
式(21)将用于下界；式(23)只估计单个共同振荡尾，不等于已经控制
整个含正背景的簇。

### 3.2 全轴上界

在(15)中利用 \(P_L\ge0\)，再用负部次可加性、(8)、(13)、(23)，得
\[
 \begin{split}
 \kappa_-(\mathcal R_L)
 &\le \kappa_-(T_{\gamma,B})
      +\kappa_-(T_{-\gamma,\overline B})
      +O_{\mathbf h,\mathbf m}(\varepsilon)\\
 &\le \frac{4|B|}{\pi^2(1+\gamma^2)}
                  \varepsilon\log L+O_{\rm fixed}(\varepsilon).
 \end{split}
 \tag{24}
\]
这里 \(q\ge1\)、\(\delta\le1/4\)，且在所述渐近参数范围内
\(q\le aL\) 最终成立。两个中心的 Cauchy 密度相同，
\(p(\gamma)=p(-\gamma)=1/[\pi(1+\gamma^2)]\)。
上界没有把两个模式簇的负部强行相加成等式。

### 3.3 下界：在正背景可支付的环段内积分

取
\[
 a=\min(\gamma/4,\,1/4),\qquad
 C_H=4(1+H),\qquad Q=C_H(1+q)e^q .
 \tag{25}
\]
令 \(\mathcal W_\pm=\{|t\mp\gamma|\le a\}\)，
\(\mathcal A_\pm=\{Q/L\le|t\mp\gamma|\le a\}\)。
两个窗不相交。对整个 \(q\) 范围一致有
\[
 Q\ge\max(q,2H,1),\qquad
 \frac QL\le
 \frac{C_H(1+A\log\log L)(\log L)^A}{L}\longrightarrow0,\qquad
 \frac{\delta}{\varepsilon}
 =\frac{qe^q}{L}\longrightarrow0 .
 \tag{26}
\]
所以充分大 \(L\) 时环段非空；最后一个极限允许下面将
\(O(\delta)\) 吸收到 \(O(\varepsilon)\)，且不漏掉任何 \(q\) 子区。

在 \(\mathcal A_+\) 上取 \(y=L(t-\gamma)\)。自己的正 Poisson 簇
在这些环段的普通积分满足
\[
 \begin{split}
 \int_{\mathcal A_+}
       \sum_j\frac{m_j\delta}
                 {\delta^2+(t-\gamma-h_j/L)^2}\,dt
 &=\sum_jm_j\int_{Q\le|y|\le aL}
                 \frac q{q^2+(y-h_j)^2}\,dy\\
 &\le \frac{8Mq}{Q}=O_{\mathbf h,\mathbf m}(\varepsilon).
 \end{split}
 \tag{27}
\]
用到 \(|y-h_j|\ge|y|/2\)。Cauchy 积分至多再乘 \(1/\pi\)。
另一中心的正 Poisson 簇在整个 \(\mathcal W_+\) 为
\(O_{\gamma,\mathbf h,\mathbf m}(\delta)\)，因为对充分大 \(L\)，
\(|t+\gamma+h_j/L|\ge\gamma\)；另一共同振荡尾则由(22)的点态式为
\(O_{\gamma,B}(\varepsilon)\)。
对 \(\mathcal A_-\) 同理。

因此在这两个环段中，用
\((f+g)_-\ge f_--|g|\)，对正项也可减去其积分；
再用(8)、(13)、(26)--(27)，得到
\[
 \kappa_-(\mathcal R_L)
 \ge\int_{\mathcal A_+}(T_{\gamma,B})_-\,d\mu_C
       +\int_{\mathcal A_-}(T_{-\gamma,\overline B})_-\,d\mu_C
                                      -O_{\rm fixed}(\varepsilon).
 \tag{28}
\]
这一步只在环段中支付正背景，不把它的全轴 \(O(1)\) 质量当成
足够小的误差；后者在主量趋零时会破坏结论。

由(21)取 \(r=Q\)，右侧两项之和为
\[
 \frac{4|B|}{\pi^2(1+\gamma^2)}
                  \varepsilon\log(aL/Q)+O_{\rm fixed}(\varepsilon).
 \tag{29}
\]
而
\(\log Q=q+\log(1+q)+\log C_H\)。
所以(28)--(29)与上界(24)合用，恰得(17)的完整误差。
常数可依赖固定簇及 \(A\)，但不依赖 \(L,q\)；不存在未控制的
“先令 \(q\) 固定再令 \(L\) 增长”步骤。 \(\square\)

## 4. 两包抵消、重数与严格适用边界

### 推论301-C：验证300的双包猜测 [T/N]

取
\[
 J=2,\quad (h_1,h_2)=(0,\pi),\quad (m_1,m_2)=(1,1).
 \tag{30}
\]
则 \(B=1+e^{-i\pi}=0,\ M=2,\ H_1=\pi\)。
命题301-A直接给
\[
 \boxed{\quad
 \kappa_-\!\left(R_{\gamma,\delta,L}
                  +R_{\gamma+\pi/L,\delta,L}\right)
       \le \frac{2\pi e^{-q}}q+\frac{4e^{-q}}{1-\delta}
       \le(2\pi+16/3)e^{-q},
 \quad 0<\delta\le\tfrac14,\ q\ge1 .
 \quad}
 \tag{31}
\]
于是对每个固定 \(A>0\)，一致于 \(1\le q\le A\log\log L\)，
\[
 \frac{\kappa_-(R_{\gamma,\delta,L}
                       +R_{\gamma+\pi/L,\delta,L})}
                          {e^{-q}\log L}\longrightarrow0.
 \tag{32}
\]
这完整验证300-(50)，而不是只在有限数值尺度观察到抵消。
两项各自的单包对数负迹不能在该移动簇中直接相加。

所有权均为整数时，可以给出真正的有限中心线除子：
\[
 \Phi_L(w)=\prod_{j=1}^J
                  \{w^2+\omega_j(L)^2\}^{m_j}.
 \tag{33}
\]
对充分大 \(L\)，它是 real-type、偶、单值的整多项式，
其零点为 \(\pm i\omega_j(L)\)，完整重数为 \(m_j\)
（碰合的因子须合并重数）。所有零点恰在中心线上。
这不要求零点简单；(30)的两个不同正高度各具有单位重数。
如果 \(m_j\) 只是非负实权而非整数，分析结论仍成立，但不能把(33)
的形式实幂默认当作单值整函数。

本篇没有把合成 \(h_j/L\) 间隔说成实际 zeta 的零点间隔。
300先固定有限实际谱包、再让尺度趋于无穷、最后让谱包增大；
本篇从一开始就改变除子族，间隔常数随 \(L\) 退化。
因此(31)--(32)阻止的是不带簇相位控制的**一致外推**，
不是固定实际谱的渐近，也不是某个实际数域 \(L\) 函数的RH反例。

非负权在(15)、(16)、(24)中实质使用。允许负权时，
Poisson 背景本身可能产生不带 \(e^{-q}\) 的负质量，不能一般地沿用该上界；
仅有函数方程或中心线位置并不能替代这条符号条件。
另一方面，(31)只是负迹上界，不声称 Abel 簇逐点非负或其负迹恒为零。
整个构造继续保留 sharp 截断与 Abel 权，并未调用296的三角 taper。

## 5. 同一固定解析 germ 不识别临界边界预算 [T/N]

### 5.1 有限候选、精确 Poisson 相容性及局部一致极限

现在要求 \(m_j\) 为非负整数，且 \(M>0\)。令
\[
 \mathcal F_{L,\mathbf h}(z)=\sum_jm_jF_{L,\omega_j(L)}(z),
 \qquad
 \Phi(z)=(z^2+\gamma^2)^M.
 \tag{34}
\]
式(33)的 \(\Phi_L\) 系数逐项趋于 \(\Phi\)，因而在整个复平面局部
一致收敛。所有 \(\Phi_L\) 的零点都在中心轴；重数均为真实整数。
另一方面，\(\mathcal F_{L,\mathbf h}\) 是有限 lag 积分，故为
real-type 整函数，并在闭右半平面满足
\[
 |\mathcal F_{L,\mathbf h}(z)|\le2ML,\qquad \Re z\ge0.
 \tag{35}
\]
这里的界依赖 \(L\)，没有声称该族在靠近边界时一致有界。

定义 \(\Pi_b(t)=b/[\pi(b^2+t^2)]\)。由于
\(\Pi_b*\cos(u\,\cdot)=e^{-bu}\cos(u\,\cdot)\) 对 \(u\ge0\) 成立，
有限积分的 Fubini 定理给出对所有 \(b>0,\delta\ge0\) 的精确等式
\[
 \Pi_b*\Re\mathcal F_{L,\mathbf h}(\delta+i\,\cdot)(t)
       =\Re\mathcal F_{L,\mathbf h}(\delta+b+it).
 \tag{36}
\]
绝对换序由 \(\|\Pi_b\|_1=1\) 和有限 lag 积分保证。
因此这里不是把 Poisson 相容性作为待证正性的替代假设；
它确实由每个有限候选独立满足。

固定非空紧集 \(K\Subset\{\Re z>0\}\)，记
\(a=\min(\inf_K\Re z,1/2)>0\)。先对每个实频率 \(\omega\) 比较
有限 Abel 积分与无限无权积分，得到
\[
 \begin{split}
 \left|F_{L,\omega}(z)
   -\left\{\frac1{z-i\omega}+\frac1{z+i\omega}\right\}\right|
 &\le 2e^{-L}\int_0^L e^{(1-a)u}\,du
                  +2\int_L^\infty e^{-au}\,du\\
 &\le(4+2/a)e^{-aL},\qquad z\in K.
 \end{split}
 \tag{37}
\]
分母实部至少为 \(a\)，所以频移差的倒数恒等式另给
\[
 \sup_{z\in K}
 \left|\mathcal F_{L,\mathbf h}(z)
             -\frac{\Phi'(z)}{\Phi(z)}\right|
 \le \frac{2H_1}{a^2L}+M(4+2/a)e^{-aL}.
 \tag{38}
\]
极限为
\[
 \frac{\Phi'}{\Phi}(z)
      =M\left\{\frac1{z-i\gamma}+\frac1{z+i\gamma}\right\}.
 \tag{39}
\]
它在右半平面具有正实部；(38)却只控制固定内部紧集，
不控制变化直线 \(\Re z=q/L\)。
这是同一个**解析 germ**，不是 Euler germ：模型没有素数 Euler 数据、
Gamma 完成项或数域算术系数，不能据此声称满足真实 zeta 的全部接口。

### 5.2 同 germ、同极限除子、相反的负迹行为

**定理301-D。** 存在两族满足(33)--(39)的有限实 lag 候选，
极限除子相同、解析 germ 相同且均具有上述定量局部收敛率，
但沿同一右移日程一族负迹趋零、另一族负迹趋于无穷。

证明。固定 \(\gamma>0\)，均取 \(M=2\)，比较
\[
 \mathbf h^{\rm coh}=(0,0),\qquad
 \mathbf h^{\rm can}=(0,\pi),\qquad m_1=m_2=1,
 \qquad q=\tfrac12\log\log L,\quad\delta=q/L .
 \tag{40}
\]
当 \(L\) 充分大时 \(q\ge1\)。两族的 \(B\) 分别为2和0，
共同极限除子为 \((z^2+\gamma^2)^2\)。
令 \(K_\gamma=4/[\pi^2(1+\gamma^2)]\)。定理301-B与(31)分别给
\[
 \begin{split}
 \kappa_-^{\rm coh}
  &=2K_\gamma\sqrt{\log L}
        +O_\gamma\left(\frac{1+\log\log L}{\sqrt{\log L}}\right)
       \longrightarrow\infty,\\
 0\le\kappa_-^{\rm can}
  &\le\frac{2\pi+16/3}{\sqrt{\log L}}\longrightarrow0.
 \end{split}
 \tag{41}
\]
所有有限候选及极限均已在5.1独立构造并核验，故结论不是把所需
负迹行为直接写成结构公理。 \(\square\)

这还给出两个精确推论。
第一，若改取 \(q=\log\log L+c\)，固定 \(c\in\mathbb R\)，则
\[
 \kappa_-^{\rm coh}\longrightarrow2K_\gamma e^{-c}>0,
       \qquad \kappa_-^{\rm can}\longrightarrow0.
 \tag{42}
\]
第二，分别对 \((J,h_1,m_1)=(1,0,1)\) 与 \((1,\pi,1)\) 使用
定理301-B；两次相位和的模均为1。因此在其整个统一参数带内
\[
 \frac{\kappa_-(R_{\gamma,\delta,L}+R_{\gamma+\pi/L,\delta,L})}
      {\kappa_-(R_{\gamma,\delta,L})+
             \kappa_-(R_{\gamma+\pi/L,\delta,L})}
          =O_\gamma(1/\log L)\longrightarrow0.
 \tag{43}
\]
分母的统一主项为 \(2K_\gamma e^{-q}\log L>0\)，误差的相对值趋零；
这里没有默认296的固定高度误差自动对移动高度一致。

故单包负迹的可见性、正整数重数、固定正实极限和 Poisson 相容性，
均不能单独提供合包后负迹的固定比例下界。
仅知道一个固定开集上的定量收敛，紧性或完备化也不能决定(41)哪种
边界行为发生。此障碍只排除**仅依赖这些已列数据**的统一推论，
不排除额外统一算术输入，更不排除数域 Weil 配置的存在。

## 6. 最小条件、删除审计及与原路线的接口

本篇是一条显式公式型接口的有限模型边界定理，不是完整 Weil 配置
存在性定理。其独立输入只有所给 lag 核、正权和初等积分恒等式；
没有新增关于实际素数或实际零点的算术估计。

- **完整核、固定 Cauchy 迹。** (6)--(8)依赖指定 sharp 上端及 Abel 权。
  改变权会改变端点尾；296的三角权已有不同负迹尺度，不能沿用(17)。
  分离的是有限上端尾，不是声称整个单边复变换都获得 \(1/t^2\) 衰减。
- **非负权。** 用于(15)、(24)、(27)。若取单包权 \(-1\)、
  \(q=2\log\log L\)，由 Cauchy 余弦积分及支配收敛，
  \(\int R_{\gamma,\delta,L}\,d\mu_C\to2/(1+\gamma^2)>0\)。
  所以 \(\kappa_-(-R_{\gamma,\delta,L})\) 有正下界，
  而硬套(17)的右侧趋零，给出严格反例。
- **固定正的极限高度。** \(\gamma>0\)保证第3节两个窗不交。
  删除它也会改变常数：取 \(\gamma=0,J=1,h_1=\pi/2,m_1=1\)，
  则 \(B=-i\)，(15)中两个同中心 \(T\) 项恰相消。
  (8)、(13)仍给 \(\kappa_-=O(e^{-q})\)，而机械沿用(17)
  会预言非零的 \(e^{-q}\log L\) 主项。
- **固定有限簇与参数带。** (26)及误差常数依赖固定 \(h_j,m_j,J,A\)。
  不对增长簇声称(17)一致；零相位和的显式(16)则可以逐族使用其已显示
  的 \(M,H_1\) 预算。去掉 \(q\le A\log\log L\) 后下界环段可能消失，
  当前证明不支持原渐近；(16)不受此上界限制。
- **整数重数。** 只在(33)--(39)的整函数除子实现中使用。
  非整数权的解析核定理保持，但不能自动产生单值整函数。

因此删项失效已经在证明或反例中定位，不能将这些定理当作
“全 Weil 正性”的另一种写法。模型的所有零点本来就在中心轴，
所研究的是有限截断的负迹，而不是从模型证明真实 RH。
有限域曲线、Dirichlet/Dedekind/自守 \(L\) 函数及真实 zeta 是否拥有
可应用的统一簇算术控制，仍各自为[O]；本篇没有构造上同调或极化，
也没有建立上同调型与显式公式型结构之间的新桥梁。

### 四轮周期决策

296--297：识别固定中心极点模型的硬截断边界层及原始双端点分拆风险。
298--299：将过快日程障碍传给真实候选，审计全尺度局部强输入。
300：闭合端点分离的真实全谱 RH 条件临界渐近。
301：验证300-(50)，用显式相位和给出移动有限谱簇的非一致性障碍。

**决策：本条件日程校准周期收束，不继续扩写 RH 等价预算。**
301晋级为内部模型定理与范围障碍，不称新算术定理或已具发表价值。
主线下一准入任务只回查已经缩小的289-(53)：
固定 \(A=1,a=1/4\) 的实际深右有限谱包四阶预算，
限一轮检查能否找到适用的实际带符号相关输入及完整参数匹配。
若只能重写有限表示、用正的计数上界或改动合成窗，则继续保留观察，
不登记为该实际预算的推进。需要真正缩小开放输入才启动下一周期。
不把本篇的移动模型当作实际间距资料来强行启动族估计。

本篇归独立的有限迹／配置接口障碍材料，先保留 Markdown。
DL-AUDIT 仍仅登记、未启动；不从本结果推断其数域存在性前景。
RH/GRH、零点比例和零密度均未改善；Goal阶段验收条件尚未满足。

## 7. 可复现检查、独立审计与文献边界

### 有限检查 [E]

运行：

```text
python -B scripts/cluster_phase_cancellation_probe.py
```

固定 \(\gamma=2\)，MP50计算 \(L=32,64,128\)，各取
\(q=1,\log\log L\)，共六例。检查四个原始复尾与合并倒数差恒等式、
非负四Poisson分解、独立原 lag 积分和完整 Abel 误差。
完整的非振荡尾范数用 \(t=\tan\theta\) 计算全轴，
CS乘积积分用中心化平移缩放的同类变换；没有截去数值尾巴。
这仍是普通高精度求积，不是区间认证，返回误差仅为数值诊断。

作者代理与主代理分别复跑通过。主代理记录：
最大缩放恒等式误差 \(7.53\cdot10^{-50}\)，
原 lag 独立积分误差 \(2.83\cdot10^{-50}\)，
实测 Abel 差与正 lag 上界之比不超过0.027481，
正 lag 上界与 \(4e^{-q}/(1-\delta)\) 之比不超过0.800355；
单侧完整合尾范数与 \(\pi e^{-q}/q\) 之比不超过0.167008，
归一化CS积分与 \(\pi\) 之比不超过0.835862。
有限相位和 \((0,0),(0,\pi),(0,2\pi)\) 分别核验为2、0、2。
**没有计算完整负迹、实际 zeta 零点或任何渐近极限。**

### 证明与依赖审计

第2--4节由主代理及 gap_exception_audit 独立推导并全文复核；
双包显式界另由 carrier_audit、midband_compute 独立重建。
第5节由主代理构造，carrier_audit 独立核验局部收敛常数、
Poisson等式和同日程两族对照。
最终全文另经 gap_exception_audit、midband_compute 只读复核通过；
carrier_audit 对第5--7节及删项反例再审通过，均无必须修改项。
目录/TeX链接检查、11项目录回归、77项注册覆盖与模拟分发检查通过，
未重跑77项重型数学计算，未以此宣称新提交的远程CI已通过。
证明不依赖有限数值误差、RH、标准猜想或文献窗口最优性。
这些内部交叉复核不等于外部同行审查。

### 经典机制与尚未核验的新颖性 [R/O]

Fredric J. Harris，*On the Use of Windows for Harmonic Analysis with the
Discrete Fourier Transform*，Proceedings of the IEEE 66(1) (1978), 51--83，
[DOI](https://doi.org/10.1109/PROC.1978.10837)、
[原文扫描](https://web.mit.edu/xiphmont/Public/windows.pdf)。
本轮阅读§III p.52、§V.C p.60及pp.60--62的相关讨论：
端点平滑、余弦窗和移位谱核相消是经典机制，不能作为新方法宣称。
本篇的正背景分离、Cauchy负部估计及同 germ 对照在上文独立证明；
不调用该文的旁瓣最优数值。有限检索尚未核验这些具体结果的优先权，
不因没有命中相同表述就称为新定理发表成果。
