# 296. 临界单极点对的负迹边界层与锐利右移日程

日期：2026-09-06。B1z 新周期第1轮；归属：独立 response 论文的有限完成接口。
状态：[T] 匹配 sharp--Abel 单包的统一负迹渐近、完整均值与背景加法；
[T/N] 中心线整数除子、有限 Poisson 接口与任意日程推理的反例；
[T] 三角 lag 权消除该模型障碍；[O] 实际 zeta 的独立有符号估计。
本篇不证明或否定 RH，不声称文献新颖性，也不完成 Goal 阶段验收。

## 1. 对象、归一化与主定理

所有对数均为自然对数。固定 \(\gamma>0\)，令
\[
 L=\log Y,\qquad \delta\ge0,\qquad q=\delta L,\qquad E_q=e^{-q},
 \qquad d\mu_C(t)=\frac{dt}{\pi(1+t^2)}.
 \tag{1}
\]
本文始终用 \(q\) 表示实日程参数；后面的全纯变量另记为 \(w\)。
可以在全文限制 \(Y=N\) 为整数；证明对所有充分大的实 \(Y\) 同样成立。
对实可积函数定义
\[
 \tau_C f=\int_{\mathbb R} f\,d\mu_C,\qquad
 \kappa_\pm(f)=\tau_C(f_\pm),\qquad
 f_+=\max(f,0),\quad f_-=\max(-f,0).
 \tag{2}
\]
不重新缩放迹，不减去 \(f(0)\)，也不将复 Fourier 模长当作实部负迹。

考虑同一个固定共轭模式经过匹配 sharp--Abel 权后的实符号
\[
 \begin{split}
 R_{\delta,L}(t)
 &=2\Re\int_0^L
       e^{(-\delta+i\gamma)u-e^{u-L}}\cos(tu)\,du\\
 &=C_{\delta,L}(t-\gamma)+C_{\delta,L}(t+\gamma),\\
 C_{\delta,L}(h)&=\int_0^L e^{-\delta u-e^{u-L}}\cos(hu)\,du .
 \end{split}
 \tag{3}
\]
上端是 \(L\)，Abel 因子是 \(e^{-e^{u-L}}\)；二者均完整保留。
这里只研究未中心化的右侧实部，不把它误认成旧中频四阶量
\(\widehat r=P-M\)。

### 定理296-A：统一的负迹渐近 [T]

固定任意 \(A>0\)。当 \(L\to\infty\)，一致于
\[
             0\le q\le A\log\log L,\qquad \delta=q/L,
 \tag{4}
\]
有
\[
 \boxed{\displaystyle
 \kappa_-(R_{\delta,L})
 =K_\gamma E_q\log L+
 O_{\gamma,A}\!\left(E_q[1+q+\log(1+q)]\right),\qquad
 K_\gamma=\frac4{\pi^2(1+\gamma^2)}.}
 \tag{5}
\]
因此误差是主项的统一 \(o(1)\) 倍，**包括主项本身趋于零的日程**。
这不是以 \(O(1)\) 误差代替趋零区间的估计。

另有完整均值
\[
 \tau_C R_{\delta,L}
 =\frac{2(1+\delta)}{(1+\delta)^2+\gamma^2}
       +O(L e^{-L})
 =\frac2{1+\gamma^2}+O_\gamma(\delta+Le^{-L}),
 \tag{6}
\]
以及
\[
 \kappa_+(R_{\delta,L})
 =\kappa_-(R_{\delta,L})
   +\frac{2(1+\delta)}{(1+\delta)^2+\gamma^2}+O(Le^{-L}).
 \tag{7}
\]
尤其不能在负迹趋零时写成正负迹具有同一个趋零渐近。
本定理的常数允许依赖固定 \(\gamma,A\)，不对合并的极点、增长的
\(\gamma\) 或增长的模式数声称一致性。

## 2. 精确矩形核与 Abel 差：没有 \(1/\delta\) 假奇点

充分大 \(L\) 时(4)保证 \(0\le\delta\le1/4\)。
先定义保留相同端点、暂时不带 Abel 因子的矩形核
\[
 \begin{split}
 C^0_{\delta,L}(h)
 &=\int_0^L e^{-\delta u}\cos(hu)\,du\\
 &=\frac{\delta+
      E_q\{h\sin(Lh)-\delta\cos(Lh)\}}{\delta^2+h^2}.
 \end{split}
 \tag{8}
\]
式(8)由一个有限指数积分直接得到。对 \(\delta=0\)，按连续值解释为
\[
 C^0_{0,L}(h)=\frac{\sin(Lh)}h,\qquad C^0_{0,L}(0)=L.
 \tag{9}
\]
没有把上下端拆成各自在 \(\delta=0,h=0\) 发散的积分。

令 \(R^0_{\delta,L}(t)=C^0_{\delta,L}(t-\gamma)+
C^0_{\delta,L}(t+\gamma)\)。对全部实 \(t\)，用 \(v=L-u\) 得
\[
 \begin{split}
 |R_{\delta,L}(t)-R^0_{\delta,L}(t)|
 &\le2\int_0^L e^{-\delta u}
               (1-e^{-e^{u-L}})\,du\\
 &\le2E_q\int_0^L e^{-(1-\delta)v}\,dv
 \le \frac{2E_q}{1-\delta}.
 \end{split}
 \tag{10}
\]
这里使用 \(1-e^{-x}\le x\)；故同一界适用于 Cauchy \(L^1\) 范数。
负部是 \(L^1\)-Lipschitz 的，于是
\[
 |\kappa_-(R_{\delta,L})-\kappa_-(R^0_{\delta,L})|
 \le O(E_q).
 \tag{11}
\]
这并非删除一个未控制的无限尾，而是对两个明确有限核给出完整误差。

虽然真正上端处的 Abel 值是 \(e^{-1}\)，(5)的主系数不多乘 \(e^{-1}\)。
原因是负迹对数来自 \(1/L\ll |t\mp\gamma|\ll1\) 的共振环；
末端宽度 \(O(1)\) 的 lag 权改动只贡献(10)的 \(O(E_q)\)。
把非常高频的单个端点系数误用到此共振环，会得到错误常数。

## 3. 实部负半波的加权平均

记
\[
 p(t)=\frac1{\pi(1+t^2)},\qquad
 S_L(h)=\frac{\sin(Lh)}h,\qquad S_L(0)=L.
 \tag{12}
\]
函数 \(g(y)=(-\sin y)_+\) 是 \(2\pi\)-周期函数，平均值为 \(1/\pi\)。
其零均值原函数
\(G(y)=\int_0^y(g(v)-1/\pi)\,dv\) 有界。
对 \(1\le a<b\)，分部积分严格给
\[
 \int_a^b \frac{g(y)}y\,dy
   =\frac1\pi\log\frac ba+O(1/a).
 \tag{13}
\]
这里误差来自 \(G(b)/b-G(a)/a+\int_a^bG(y)y^{-2}dy\)，
与 \(a,b\) 无关。它处理的是负半波本身，不是复模长的平均。

固定
\[
               0<H<\min(\gamma/3,1/4).
 \tag{14}
\]
在 \(|h|\le H\) 内，
\(p(\pm\gamma+h)=p(\gamma)+O_\gamma(|h|)\)。
又 \(S_L\) 是偶函数，\(|S_L(h)|\le\min(L,1/|h|)\)。
所以冻结 Cauchy 密度的误差是 \(O_\gamma(1)\)。
由(13)，对 \(L^{-1}\le a<H\) 有
\[
 \int_{a\le|h|\le H}(S_L(h))_-\,p(\pm\gamma+h)\,dh
 =\frac{2p(\gamma)}\pi\log\frac Ha+O_\gamma(1).
 \tag{15}
\]
在 \(|h|<L^{-1}\) 的积分为 \(O(1)\)，而
\[
 \int_{|h|>H}\frac{p(\pm\gamma+h)}{|h|}\,dh<\infty.
 \tag{16}
\]
因此单个共振中心的全轴负迹满足
\[
 \int_{\mathbb R}(S_L(t\mp\gamma))_-\,d\mu_C(t)
 =\frac{2p(\gamma)}\pi\log L+O_\gamma(1).
 \tag{17}
\]
两个中心分离、每个中心有两侧，再乘负半波平均 \(1/\pi\)，
正是(5)中系数 \(4/[\pi^2(1+\gamma^2)]\) 的来源。

## 4. 定理296-A的负迹证明

### 4.1 全轴上界

对 \(\delta>0\)，把(8)写成
\[
 C^0_{\delta,L}(h)=P_\delta(h)+
 E_q\left\{\frac{h\sin(Lh)}{\delta^2+h^2}
           -\frac{\delta\cos(Lh)}{\delta^2+h^2}\right\},
 \qquad P_\delta(h)=\frac{\delta}{\delta^2+h^2}\ge0.
 \tag{18}
\]
对 \(\delta=0\) 直接用(9)，并在此记 \(P_0=0\)；这不是把
\(P_\delta\) 的测度极限当作零。
非负的两个 \(P_\delta\) 只会减少负部，可以在上界中丢去。
又
\[
 \left(\frac{h\sin(Lh)}{\delta^2+h^2}\right)_-
 \le (S_L(h))_-,\qquad
 \int_{\mathbb R}
   \frac{\delta}{\delta^2+(t\mp\gamma)^2}\,d\mu_C(t)\le1.
 \tag{19}
\]
第二式用 \(p\le1/\pi\)；当 \(\delta=0\) 时对应校正项为零。
负部的次可加性、(17)--(19)给
\[
 \kappa_-(R^0_{\delta,L})
 \le K_\gamma E_q\log L+O_\gamma(E_q).
 \tag{20}
\]
这里没有先把正 Poisson 质量取绝对值，从而没有引入不允许的 \(O(1)\) 误差。

### 4.2 四个环上的下界

令
\[
 h_0=\frac{\max(1,q e^q)}L.
 \tag{21}
\]
在(4)下，\(h_0\to0\) 一致成立，故充分大 \(L\) 时 \(h_0<H\)。
两个集合 \(h_0\le |t-\gamma|\le H\) 和
\(h_0\le |t+\gamma|\le H\) 互不相交。
当 \(\delta>0\)，定义(21)保证
\[
 \frac{\delta}{h_0}\le E_q,\qquad
 \delta\le H E_q.
 \tag{22}
\]
确切地，若 \(q e^q\ge1\)，第一个比值等于 \(E_q\)；
否则该比值为 \(q<E_q\)。

在每个本中心环上，将 \(C^0_{\delta,L}(h)\) 与 \(E_q S_L(h)\) 比较。
由(18)，两者差的普通 \(L^1\) 范数至多
\[
 O\!\left(
     \frac{\delta}{h_0}
     +E_q\frac{\delta^2}{h_0^2}
     +E_q\frac{\delta}{h_0}\right)=O(E_q).
 \tag{23}
\]
三项依次来自 \(P_\delta\)、分母
\(h^{-1}-h/(\delta^2+h^2)\) 和余弦校正。
例如第二项用
\(\delta^2/[|h|(\delta^2+h^2)]\le\delta^2/|h|^3\)；
所有积分均从 \(h_0>0\) 开始。
当 \(\delta=0\)，上述差恒为零。

另一共振中心距本环至少 \(\gamma\)，故其矩形核逐点为
\(O_\gamma(\delta+E_q)=O_\gamma(E_q)\)，其中使用(22)。
Cauchy 密度有界，环长固定，再由(10)，这些扰动总计仍为 \(O_\gamma(E_q)\)。
对任意实 \(f,g\)，有 \((f+g)_-\ge f_- -|g|\)。
在四个环上应用该式和(15)，于是
\[
 \begin{split}
 \kappa_-(R_{\delta,L})
 &\ge K_\gamma E_q
       \{\log L-\log(Lh_0)\}-O_\gamma(E_q),\\
 0\le\log(Lh_0)
 &=\log\max(1,q e^q)
 \le q+\log(1+q).
 \end{split}
 \tag{24}
\]
结合(11)、(20)便得(5)。由于
\((1+q+\log(1+q))/\log L\to0\) 在(4)下一致成立，
也得到主定理所说的统一相对误差。证明覆盖 \(q=0\)，未使用 \(1/q\) 界。
\(\square\)

## 5. 均值、正迹及日程阈值

### 5.1 均值不能略去

初等 Cauchy Fourier 恒等式为
\[
              \int_{\mathbb R}\cos(tu)\,d\mu_C(t)=e^{-|u|}.
 \tag{25}
\]
对 \(u>0\)，闭合上半平面围道并取极点 \(i\) 的留数即得；
\(u<0\) 用偶性，\(u=0\) 用概率归一化。
有限 lag 积分有绝对支配，故 Fubini 给精确公式
\[
 \tau_C R_{\delta,L}
       =2\int_0^L e^{-(1+\delta)u-e^{u-L}}\cos(\gamma u)\,du.
 \tag{26}
\]
去掉 Abel 因子的误差至多
\(2e^{-L}\int_0^L e^{-\delta u}du\le2Le^{-L}\)。
补回 \(u>L\) 的指数尾只付 \(O(e^{-L})\)。
而
\(\int_0^\infty e^{-(1+\delta)u}\cos(\gamma u)du
=(1+\delta)/[(1+\delta)^2+\gamma^2]\)。
这证明(6)。恒等式 \(f_+-f_-=f\) 随即给(7)。

### 推论296-B：临界日程 [T]

仍在(4)的范围内，记
\[
                        b_L=q-\log\log L.
 \tag{27}
\]
则
\[
               \kappa_-(R_{\delta,L})
                   =K_\gamma e^{-b_L}(1+o(1)),
 \tag{28}
\]
其中相对误差统一。具体地：

- 若 \(b_L\to c\in\mathbb R\)，负迹趋于
  \(K_\gamma e^{-c}\)，正迹趋于 \(K_\gamma e^{-c}+2/(1+\gamma^2)\)。
- 若 \(b_L\to+\infty\)，负迹趋于零，正迹趋于 \(2/(1+\gamma^2)\)。
- 若 \(b_L\to-\infty\)，正负迹均发散，且两者之比趋于1。

更一般，在此参数范围内，负迹一致有界当且仅当
\(q\ge\log\log L-O(1)\)；负迹趋零当且仅当 \(b_L\to+\infty\)。
例如，固定 \(q=c>0\) 已有 \(\delta=c/L>0\to0\)，但负迹仍按
\(K_\gamma e^{-c}\log L\) 发散。
固定 \(q=0\) 也包含在定理中，但不是严格右移的日程。

请注意三个层级：
\[
 L=\log Y,\qquad
 \log L=\log\log Y,\qquad
 \log\log L=\log\log\log Y.
 \tag{29}
\]
本模型的临界乘积 \(\delta\log Y\) 是最后一个量级。
本文不把它说成实际 zeta 的最优日程。

## 6. 真正的中心线除子与有限 Poisson 接口

### 命题296-C：正实极限并不控制任意有限右移日程 [T/N]

定义
\[
 \Phi(w)=w^2+\gamma^2,\qquad
 F_L(w)=2\int_0^L e^{-wu-e^{u-L}}\cos(\gamma u)\,du .
 \tag{30}
\]
这是同一固定连续源的各个有限匹配截断，不是每轮新选的原子。
有以下全部性质。

1. \(\Phi\) 是 real-type 的整函数，阶至多一，满足
   \(\Phi(-w)=\Phi(w)\)。两个零点恰为 \(\pm i\gamma\)，均为单零点；
   对数导数在两个极点处的留数都为整数1。
2. 每个 \(F_L\) 都是 entire、real-type，并且
   \(|F_L(w)|\le2L\) 于 \(\Re w\ge0\)。
3. 对 \(a>0,\delta\ge0\)，有精确有限 Poisson 恒等式
   \[
   \Re F_L(\delta+a+it)
      =\Pi_a*\Re F_L(\delta+i\,\cdot)(t),\qquad
   \Pi_a(t)=\frac a{\pi(a^2+t^2)} .
   \tag{31}
   \]
4. 在整个 \(\Re w>0\) 上局部一致地，
   \[
   F_L(w)\longrightarrow
   F_\infty(w)=\frac{\Phi'(w)}{\Phi(w)}
       =\frac1{w-i\gamma}+\frac1{w+i\gamma}.
   \tag{32}
   \]
   该极限满足 \(\Re F_\infty(w)>0\) 于 \(\Re w>0\)。
5. 有 \(\Re F_L(\delta+it)=R_{\delta,L}(t)\)，所以
   取 \(L=\log N\)、\(\delta=c/L\)、固定 \(c>0\) 时，
   所有上述性质同时成立，有限负迹却趋于无穷。

证明。前两条由多项式及有限积分直接验证，有限积分的全部复导数均可逐项取。
式(25)经尺度变换给 \(\widehat\Pi_a(u)=e^{-a|u|}\)。
对(30)的有限 lag 积分使用 Fubini，得到(31)；
因此还独立满足
\[
 \Re F_L(\delta+a+it)\ge
 -\Pi_a*\bigl(\Re F_L(\delta+i\,\cdot)\bigr)_-(t).
 \tag{33}
\]
这是145需要的 Poisson admissibility，不假设负迹一致有界。

对任意紧集 \(K\subset\{\Re w>0\}\)，取
\(\varepsilon=\inf_K\Re w>0\)。
有限截断被 \(2e^{-\varepsilon u}\) 支配，权
\(\mathbf1_{u\le L}e^{-e^{u-L}}\) 逐点趋于1。
于是局部一致支配收敛给
\(F_L(w)\to2\int_0^\infty e^{-wu}\cos(\gamma u)du\)，
计算积分即(32)。若 \(w=x+it,x>0\)，则
\[
 \Re F_\infty(x+it)
   =\frac{x}{x^2+(t-\gamma)^2}
     +\frac{x}{x^2+(t+\gamma)^2}>0.
 \tag{34}
\]
最后一条来自(3)、(5)。\(\square\)

### 6.1 固定 Mellin 源及其没有保留的算术性质

若写 \(\rho_\pm=1/2\pm i\gamma\)，则固定实源
\[
 dE_\gamma(x)=-
       \{x^{\rho_+-1}+x^{\rho_--1}\}\,dx
 \tag{35}
\]
满足
\[
 -\int_1^Y x^{-1/2-\delta}e^{-x/Y}
                   \cos(t\log x)\,dE_\gamma(x)=R_{\delta,L}(t).
 \tag{36}
\]
负号与一个零点在显式公式误差中的系数相容；完成后的对数导数留数为正1。
源从 \(x=1\) 起累计，故 \(E_\gamma(1)=0\)，无下端遗漏。
它的累计量为
\(-2\Re[(x^{1/2+i\gamma}-1)/(1/2+i\gamma)]\)，
因而是 \(O_\gamma(\sqrt x)\)。

但是，这只是一个连续的有限 Mellin 模式，不是 von Mangoldt 源，
也没有素数幂支撑、算术 Euler 乘积或正整数对数系数。
它也没有284的强质量记录：对固定 \(\sigma_0<1/2\)，其加权质量至多
\[
 2\int_1^Y x^{-1/2-\sigma_0}dx
          =O_{\sigma_0}(Y^{1/2-\sigma_0}),
 \tag{37}
\]
不能满足额外发散因子 \(\ell(Y)\) 的质量下界。
不能把本模型的亚纯除子与295模型的正整数源、强记录拼成同一个反例。

## 7. 更换有限权可消除此障碍：一个必要的范围检验 [T]

本节不改回(3)的物理权；它另造一个明确的有限候选，
以检查本篇障碍是否被误读为“所有有限配置均失败”。
令
\[
 \begin{split}
 F_L^{\triangle,0}(w)
   &=2\int_0^L (1-u/L)e^{-wu}\cos(\gamma u)\,du,\\
 F_L^{\triangle,A}(w)
   &=2\int_0^L (1-u/L)e^{-wu-e^{u-L}}\cos(\gamma u)\,du .
 \end{split}
 \tag{38}
\]
三角权下，在 \(\delta=0\) 的单个中心有
\[
 \int_0^L(1-u/L)\cos(hu)\,du
      =\frac{1-\cos(Lh)}{Lh^2}\ge0,
 \tag{39}
\]
其中 \(h=0\) 的连续值是 \(L/2\)。
两个中心相加后仍非负。相同的有限 Poisson 恒等式因此给
\[
                   \Re F_L^{\triangle,0}(\delta+it)\ge0
                       \quad(\delta\ge0,\ t\in\mathbb R).
 \tag{40}
\]
这不是由对数导数的极限正性反推有限正性，而是(39)的精确公式。

保留匹配 Abel 因子后，用 \(v=L-u\) 得全轴逐点界
\[
 \begin{split}
 |F_L^{\triangle,A}(\delta+it)-F_L^{\triangle,0}(\delta+it)|
 &\le2\int_0^L(1-u/L)e^{-\delta u}e^{u-L}\,du\\
 &\le\frac{2E_q}{L(1-\delta)^2}
 \le\frac{8E_q}{L}\qquad(0\le\delta\le1/2).
 \end{split}
 \tag{41}
\]
故
\[
       \kappa_-\!\left(\Re F_L^{\triangle,A}(\delta+i\,\cdot)\right)
                        \le8E_q/L\le8/L.
 \tag{42}
\]
两种三角候选都满足同一有限 Poisson 结构，并在 \(\Re w>0\)
局部一致趋于 \(\Phi'/\Phi\)：直接使用(32)的支配收敛即可。
因此对任意 \(\delta_L\ge0,\delta_L\to0\)，(42)都趋于零。

(42)仅说明可以为这个明确模型改变有限权来移除 sharp-window 边界层。
它没有证明实际 zeta 的三角 prime--continuum--Gamma 候选有(40)；
更没有通过正核、选择或完备化产生缺失的算术正性。
由此也可见，(5)只是一类给定有限 regularization 的锐利障碍，
不是对所有有限 Weil 型配置的障碍。

## 8. 与既有接口的关系、最小假设及循环性

本文的所有新不等式均由有限积分、负部的 Lipschitz 性及初等周期平均证明，
不使用 RH、零密度、真实零点数值高度或未知的完整 Weil 正性。
以下已有笔记只用于解释接口，不作为(5)的隐含算术输入。

- [145](145-bounded-defect-normality.md)的有界缺陷正规族定理是一个
  **充分条件**：Poisson、germ 与有界缺陷可推出右半平面全纯延拓。
  本模型本来已有中心线除子与全纯右半平面极限。
  (5)否定的是把该定理倒过来，声称给定的所有有限日程也必有有界缺陷。
  它不否定145，亦不否定存在一条成功日程。
- [293](293-poisson-transport-and-right-shifted-record-currents.md)
  第7节对实际 zeta 的 sharp 完成给出 RH 条件充分日程
  \(\delta L=(5/2)\log L\)。
  该日程远在(4)的临界尺度之外；本篇没有改进它，也没有证明其常数最优。
  293无条件的实际 Poisson/germ 核验与其尚缺的绝对预算保持原状态。
- [294](294-pnt-envelope-gain-and-fixed-source-saturation.md)
  给实际 PNT／历史交点的节省；
  [295](295-fixed-positive-source-right-trace-saturation.md)
  用固定正整数源饱和其一般次幂包络，但其 germ 非亚纯。
  本篇确实使用亚纯对数导数、整数留数及中心反射，却不保留295的算术源
  和强记录；所以只推进“有限近似靠近临界极点时需要日程控制”这一条接口。

### 8.1 假设作用与删除后的反例或失效位置

| 输入 | 在证明中的精确作用 | 删除或修改后的失效 |
|---|---|---|
| 固定非零共轭对 \(\pm\gamma\)，实部取值及单位振幅 | 两个分离中心、实负半波平均及 \(K_\gamma\) | 任意复模长没有相同正负惯性；振幅取零即无下界；增长 \(\gamma\) 未获统一常数 |
| 给定的匹配 sharp cutoff 与 Abel 权 | 精确式(8)、小 Abel 差(10)及四个对数环 | 三角权(38)--(42)直接消除本模型障碍，故不能推广为所有有限权 |
| \(q=\delta L\) 的统一范围(4) | \(h_0=o(1)\)、相对误差趋零，以及背景附录的窗口分割 | 更大的 \(q\) 不可沿用这段统一误差；本篇不外推到任意参数平面 |
| 固定 Cauchy 概率迹 | 在 \(\pm\gamma\) 处冻结正密度，给出精确系数 | 若换成支撑远离共振点的迹，只有 \(O_\gamma(E_q+\delta)\) 而没有该对数项 |
| 有限非负 lag、实源与独立 germ | (31)--(33)把模型接入145的候选类别 | 任意边界函数的负井不自动具有合法的全纯或 divisor 接口 |
| 中心线整数除子与正实极限 | 明确说明发散不是 off-center zero 所致 | 这不是(5)的假设改写，而是(30)--(34)独立核验的反例附加性质 |
| 沿趋边界直线的定量近似控制 | 本模型由(5)给出准确门槛 | 紧集局部一致收敛不控制 \(\Re w=\delta_L\to0\) 的边界层 |

“支撑远离共振点”的一行指例如紧支撑于
\(\{|t-\gamma|\ge H,\ |t+\gamma|\ge H\}\) 的固定有限正测度，
其上(8)、(10)逐点为 \(O_\gamma(E_q+\delta)\)。
这仅说明迹的支撑位置不可在该下界中省略，未建议改变实际物理迹。

### 8.2 精确 [N] 范围

被排除的普遍推理是：

> 有限 real-type Poisson 候选的 germ 已来自中心线整数除子，并且
> 在右半平面局部一致收敛到正实函数，所以对任意
> \(L\to\infty,\delta_L>0\to0\)，同一 sharp--Abel 候选的 Cauchy 负迹有界。

命题296-C加上固定 \(q>0\) 的(5)是一个完整反例。
本篇**不**排除合适右移日程；在同一 moderate 范围内可取
\(q=2\log\log L\)，使负迹趋零。
它也不排除更换有限权、额外算术约束、其他成功共尾选择、
实际 \(\Lambda\) 的记录估计或任何完整上同调型结构。
这里没有构造上同调、Frobenius、极化或 Hard Lefschetz，
也没有声称两类 Weil 结构等价。

### 8.3 下一最小输入与止损

本轮有限任务止于一个可证伪的边界层定理，而不再将每种核或日程扩写成新框架。
下一步若继续实际右侧路线，必须先为选定的真实有限权给出可审计的、
在移动直线上的有符号误差界；单独重复“germ 亚纯、留数为整数、
极限正实或紧集收敛”不晋级，因为本模型已同时满足这些性质。

一个最小的模型到算术接口检查是：在真正的
\(F_Y^\sharp\) 中，能否把有限个临界模式与其余完整通道分开，并对后者
在这些固定共振邻域取得尺度一致的实部界。
下节证明说明这样的局部界究竟足以转移什么，也说明若只知一个 \(O(1)\)
全轴扰动，就不能保留负迹趋零时的锐利量级。
对实际 zeta，未指定的无限剩余谱、Gamma 和端点不能被默认为这样的有界背景。
该局部控制目前 [O]，不假设所有实际零点都位于中心线。

若只能再次写出单模式表示、对任意背景使用三角不等式，或者把未知的
全局绝对预算当作结构公理，则停止本支线。
本篇没有减少实际 RH 等价输入至一个已证明较弱的条件。

## 9. 附录：固定局部有界背景的正确加法规则 [T]

本节给完整证明，特别处理任意 signed 背景的自身负迹。
允许背景随 \(L,q\) 改变。设实函数 \(B=B_{L,q}\in L^1(\mu_C)\)，且存在
固定的 \(H\) 如(14)及 \(K<\infty\)，使
\[
 |B(t)|\le K\quad\text{几乎处处于 }
       \{|t-\gamma|\le H\}\cup\{|t+\gamma|\le H\}.
 \tag{43}
\]
不要求其全轴 \(L^1\) 范数对尺度一致有界。

### 命题296-D [T]

在(4)的范围内，对 \(\epsilon=1\) 或 \(-1\)，统一有
\[
 \boxed{\displaystyle
 \kappa_-(B+\epsilon R_{\delta,L})
 =\kappa_-(B)+\kappa_-(\epsilon R_{\delta,L})
       +O_{\gamma,A,K}\!\left(E_q(1+q)\right).}
 \tag{44}
\]
因此
\[
 \kappa_-(B+R_{\delta,L})
 =\kappa_-(B)+K_\gamma E_q\log L
       +O_{\gamma,A,K}\!\left(E_q[1+q+\log(1+q)]\right).
 \tag{45}
\]
若为 \(B-R_{\delta,L}\)，(44)中的第二项是
\(\kappa_+(R_{\delta,L})\)，必须使用(7)保留 Poisson 质量。

证明。取
\[
 H_q=\frac{H E_q}{1+K},\qquad
 \Omega_q=\{|t-\gamma|\le H_q\}\cup\{|t+\gamma|\le H_q\}.
 \tag{46}
\]
则 \(\tau_C(\mathbf1_{\Omega_q}|B|)=O_\gamma(E_q)\)。
在补集，每个共振变量 \(h=t\mp\gamma\) 均有 \(|h|\ge H_q\)。
从(18)与 Cauchy 权的无穷端衰减可得
\[
 \begin{split}
 \tau_C(\mathbf1_{\Omega_q^c}|R^0_{\delta,L}|)
 &\ll_\gamma
    \frac{\delta}{H_q}
       +E_q\{1+\log(1/H_q)\}
       +E_q\frac{\delta}{H_q}\\
 &\ll_{\gamma,A,K} E_q(1+q).
 \end{split}
 \tag{47}
\]
第二行使用
\[
 \frac{\delta}{E_q^2}
      =\frac{q e^{2q}}L
      \le\frac{A\log\log L\,(\log L)^{2A}}L\longrightarrow0
 \tag{48}
\]
的一致性，以及 \(\log(1/H_q)=q+\log((1+K)/H)\)。
当 \(\delta=0\)，Poisson 和余弦校正项直接为零。
再由(10)，(47)对 \(R_{\delta,L}\) 也成立。

对实 \(b,r\)，负部的 Lipschitz 性给
\[
 \begin{split}
 |(b+r)_--r_--b_-|&\le2|b|,\\
 |(b+r)_--b_--r_-|&\le2|r|.
 \end{split}
 \tag{49}
\]
第一式在 \(\Omega_q\) 积分，第二式在其补集积分，
并令 \(r=\epsilon R_{\delta,L}\)，即得(44)。
代入(5)得(45)。全部使用实部符号，且未将有界背景替代为有符号谱和。
\(\square\)

若 \(B\ge0\)，其自身负迹为零，(45)保留裸核的完整渐近。
若 \(B\) 为任意 signed 背景，则必须保留 \(\kappa_-(B)\)：
例如 \(B(t)\equiv-1\) 时，\(b_L\to+\infty\) 给
\(\kappa_-(B+R_{\delta,L})\to1\)，不是趋零。
因此“任意局部有界背景都不改变全轴负迹趋零结论”是错误命题。
当裸核负迹发散、背景的全轴 \(L^1\) 范数一致有界时，
当然也可用较弱的 \(O(1)\) 扰动保留发散主项；
但这不足以证明本附录所覆盖的临界和趋零日程。

## 10. 审计与实验状态

本文没有调用外部零点高度、RH 级估计或数值结论；
所有主张的完整证明均已写出。主代理独立重建证明，并与 carrier_audit
分别完整读取最终落盘稿、逐式逆向复核，均 PASS。midband_compute
另独立核验了系数、趋零量级、Abel差与均值。审计包含(21)--(24)的
统一性、(44)中背景自身负迹、三角Abel近正性及模型与真实源的边界。
README中“阈值”的表述已明确为有界下阈值，而非排除更大的 \(q\)。

### 10.1 有限核验 [E]，不认证渐近

复现脚本：
[critical_pole_boundary_probe.py](../scripts/critical_pole_boundary_probe.py)。

~~~text
python -B scripts/critical_pole_boundary_probe.py
~~~

固定合成 \(\gamma=2\)、窗口半径 \(\varepsilon=1/4\)，以 MP50
计算 \(L=64,256,1024\) 和 \(q=0,\log\log L,2\log\log L\) 的9组有限例。
代码中的变量 `z` 对应本文的 \(q\)，不是全纯变量 \(w\)。
它只计算两个窗口中各自**主矩形极点**的负部：
\[
 \kappa_{\mathrm{loc}}
 =\int_{|t-\gamma|\le\varepsilon}(C^0_{\delta,L}(t-\gamma))_-\,d\mu_C(t)
 +\int_{|t+\gamma|\le\varepsilon}(C^0_{\delta,L}(t+\gamma))_-\,d\mu_C(t).
\]
这不是共轭和的全轴负迹，更不是完整Abel负迹。另一极点、窗外负部、
Abel差分别给安全解析比较预算；没有进行全轴振荡数值积分。
也不把 \(\kappa_{\mathrm{loc}}+\tau_C R\) 冒称真实正迹。

根分割使用 \(y=L|t\mp\gamma|\) 下的精确分子
\[
 N_q(y)=y\sin y+q(e^q-\cos y).
\]
在负半周期的前半段 \(N_q'<0\)，后半段
\(N_q''=(2+q)\cos y-y\sin y>0\)，所以只有一个谷底，
负部至多由两根围成；正半周期没有负部。脚本先夹逼谷底再分根积分。
无负根的分支在两组有限例中实际触发；全部根运算仍是浮点核验而非区间认证。

6个独立原积分点检采用 \(L=4\)，包含 \(\delta=0,t=\gamma\) 的可去点
及其邻域。矩形闭式最大 scaled 误差约 \(5.02\cdot10^{-51}\)，
有限上下端 incomplete-gamma 表达式的最大误差约 \(1.44\cdot10^{-51}\)；
均值的两种计算误差约 \(1.43\cdot10^{-51}\)。
Abel全轴差的lag积分majorant与预算之比最大约0.800919，
根的最大 scaled 残差约 \(6.20\cdot10^{-44}\)。
脚本作者与主代理分别执行通过；主代理运行约7.3秒。
gap_exception_audit另完整读取脚本，独立核验了根分割、漂移预算以及
局部量与全轴负迹的比较预算，PASS。二分迭代上限随工作精度调整；
MP100单根回归亦通过，不将其说成9组MP100复算。

在临界规则 \(q=\log\log L\) 下，形式渐近主项为固定的
\(K_2=4/(5\pi^2)\approx0.08105695\)，但以下局部有限值并不接近它：

| \(L\) | \(\kappa_{\mathrm{loc}}\) | 局部值／形式主项 |
|---|---|---|
| 64 | 0.00341400742 | 0.04212 |
| 256 | 0.01236892158 | 0.15260 |
| 1024 | 0.02032701987 | 0.25077 |

这些数据只检查公式、符号和预算，没有以“比例接近1”作为断言；
有限比较预算也很宽。统一渐近由§2--§4的证明成立，不能由这9例推出。
均值另行输出，例如 \(L=1024,q=\log\log L\) 时约0.400453，
与其极限0.4相区分。

目录与TeX引用检查、11项布局回归、77项检查注册及mock分发核验通过；
本轮未执行77项重型计算，也未更新PDF。本文与
[297](297-raw-pole-endpoint-splitting-obstruction.md)分别处理实部单包和原始复核，
不可把两者的绝对值、无限谱量词或误差预算互换。
文献新颖性、发表价值和外部同行评审仍待独立检验。
