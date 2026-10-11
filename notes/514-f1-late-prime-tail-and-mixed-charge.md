# 514. 远端素数的非可和边界与非零混合电荷

2026-10-11。[T/N] 使用[513](513-f1-single-prime-relative-chain-transfer.md)的实际角、缩放与单位修正闭链。
同一个非零紧支输入在远端素数上有准确零普通电荷，却有非零边界、
不可绝对迹类累计的范数，以及可认证非零HH₁类的中心混合电荷。
这些结果限制指定全局化和主商接法，不否定完整Weil型或RH。

## 1. 精确的两个输出块

沿用实偶非零 \(\eta\in C_c^\infty([-R,R])\)、\(A=A_\eta\)、\(C=\Pi A\)，
\(a=\ell^{-1/2}\)、\(L=\log\ell\)、\(Z_t\psi(u)=\psi(u-t)\)。
由513的真实Euler缩放展开，
\[
 [\Pi,V_\ell]A=
 aM_{(0,L]}Z_LA+
 (1-a^2)\sum_{j\ge1}a^j M_{(-jL,0]}Z_{-jL}A.            \tag{1}
\]
各负移项的迹类范数至多 \(C_\eta(1+jL)\)，几何和绝对可积；
(1)既在算子范数也在迹类范数成立。
\(B_\ell=[\Pi,V_\ell]AV_\ell^*\)。

正输出投影 \(P_+=M_{(0,\infty)}\) 准确抽出
\[
 P_+ B_\ell V_\ell=aM_{(0,L]}Z_LA.                       \tag{2}
\]
这里没有用非负核估计或渐近替代原算子。

## 2. 每个真实边界的迹类范数下界

令I=(0,L]。513已付 \(M_IA\in\mathcal S_1\)。
对任意s，\(M_IAZ_sM_I\)也是迹类，且
\[
 \operatorname{Tr}(M_IAZ_sM_I)=L\eta(-s).                 \tag{3}
\]
直接来源证明：以 \(\varphi(\tau)=\int\eta(t)e^{-i\tau t}\,dt\in L^1\)
写带 \(1/(2\pi)\) 的频率rank-one积分，
两端都由M_I截断，所以两个指数向量属于L²(I)，rank-one范数为L；
乘 \(e^{-i\tau s}\varphi(\tau)/(2\pi)\) 的迹类Bochner积分给(3)。
不使用未截断实轴指数向量。

用迹类理想性质、投影收缩、Z_L及Vℓ的酉性，
\[
 \|B_\ell\|_1
 \ge a\|M_IA\|_1
 \ge a\,|\operatorname{Tr}(M_IAZ_sM_I)|.
\]
对s取上确界得到
\[
 \boxed{\|B_\ell\|_1\ge
       \frac{\log\ell}{\sqrt\ell}\|\eta\|_\infty>0.}      \tag{4}
\]
这个下界对每个新增素数成立，不依赖L>2R。
它与513的 \(O_\eta((1+L)/\sqrt\ell)\) 上界相容，
现在确实控制了实际范数，而非只发现某个上界不可求和。

因非零η固定，移除任意有限S后仍有
\[
 \boxed{\sum_{\ell\notin S_f}\|B_\ell\|_1=\infty.}         \tag{5}
\]
只需Euler的 \(\sum_{\ell\text{ prime}}1/\ell=\infty\)：
对\(\ell\ge3\)，\((\log\ell)/\sqrt\ell\ge1/\ell\)。
这个素数倒数发散可由有限Euler乘积直接证明：
若倒数和有限，则 \(\prod_{\ell\le X}(1-1/\ell)^{-1}\) 有统一上界，
而它至少包含 \(\sum_{n\le X}1/n\)，矛盾；不需PNT。

(5)严格排除直接用这些单素数边界的绝对S₁求和支付无限尾。
范数在实际径向酉运输下保持。
没有据此排除有符号或共轭后的条件求和、算术补偿、不同相对结构或更弱拓扑。

## 3. 电荷已消失时，Hilbert–Schmidt费用仍准确可算

若L>2R，则513的有限电荷公式给
\[
 \Omega_\ell(\widetilde c_{\ell,h})
    =2L\sum_{n\ge1}a^n\eta(nL)=0.                        \tag{6}
\]
但(4)已证明边界算子非零。

还能准确计算HS范数。固定输出u，(1)不同负移j的输入核
\(\eta(u+jL-v)\)的支集彼此相隔L，在L>2R时不交。
正、负输出块也正交；各项HS范数分别为
\(a\sqrt L\,\|\eta\|_2\) 与
\((1-a^2)a^j\sqrt{jL}\,\|\eta\|_2\)。
其HS范数和有限，故核展开和正交求和合法，得到
\[
 \begin{aligned}
 \|B_\ell\|_2^2
 &=L\|\eta\|_2^2
      \left(a^2+(1-a^2)^2\sum_{j\ge1}j a^{2j}\right)\\
 &=\boxed{\frac{2\log\ell}{\ell}\|\eta\|_2^2}.             \tag{7}
 \end{aligned}
\]
右乘Vℓ*保持HS范数。
零普通电荷并不消除实际相对边界费用。
仅由B≠0尚不能推断HH₁类非零，下一节另给真正同调检测。

## 4. 实际中心测试给合法的混合电荷

对任意实偶 \(\zeta\in C_c^\infty(\mathbb R)\)，取真实源卷积 \(A_\zeta\)。
它属于513的角代数：
源函数 \(h_\zeta(t)=e^{-t/2}\zeta(t)\) 实、sharp不变且紧支。

qAζ在角商Q_E中央。逐生成元核对：
它与全部径向卷积交换；ζ偶使其与反演J、共同Fourier \(M_mJ\) 交换。
\([\Pi,A_\zeta]\)的核为
\((\mathbf1_{u\le0}-\mathbf1_{v\le0})\zeta(u-v)\)。
ζ紧支使两个跨半线块的u、v都落在有限窗口；
两端压缩的频率rank-one积分或光滑核展开支付S₁。
它与任意S₁元的交换子也属S₁。
故上述交换性质覆盖运输后的旧角与新来源的全部生成元；
不只检查Vℓ一个算子。

中央元乘Hochschild链的首张量因子是链映射：
\[
 \delta_\zeta(a_0\otimes\cdots\otimes a_n)
       =(qA_\zeta)a_0\otimes\cdots\otimes a_n,\qquad
 b\delta_\zeta=\delta_\zeta b.
\]
由普通电荷Ω已在HH₁上良定义，获得
\[
 \Omega_\zeta([z])=\Omega(\delta_\zeta[z]).                \tag{8}
\]
这是实际商上的同调泛函，不以零点位置作输入。
不将它未经核对地改写成 \(\operatorname{Tr}(A_\zeta B)\)；
首因子提升另有交换项，单位修正必须保留。

在下式全部张量中取q，E为角单位。直接展开给
\[
 \begin{aligned}
 \delta_\zeta\widetilde c(V,C)
       -\widetilde c(V,CA_\zeta)
  ={}&b_2(V^{-1}\otimes VC\otimes A_\zeta)\\
     &-b_2(E\otimes C\otimes A_\zeta).                    \tag{9}
 \end{aligned}
\]
因为qAζ中央，(9)准确支付中心乘法与改测试的比较。
\(CA_\zeta=\Pi A_{\eta*\zeta}\)，新输入仍实偶紧支；
513的准入、电荷定理于是给
\[
 \boxed{\Omega_\zeta([\widetilde c_{\ell,h}])
       =2L\sum_{n\ge1}a^n(\eta*\zeta)(nL).}               \tag{10}
\]

## 5. 原电荷为零的远端类仍是非零HH₁类

固定L>2R，令
\[
 \zeta_\ell(t)=\tfrac12\bigl(\eta(t-L)+\eta(t+L)\bigr).
\]
它是实际允许的实偶紧支源测试。
\[
 (\eta*\zeta_\ell)(L)=\tfrac12\|\eta\|_2^2,\qquad
 (\eta*\zeta_\ell)(nL)=0\quad(n\ge2),
\]
因为 \(\eta*\eta\) 支集在[-2R,2R]。
因此(10)给
\[
 \boxed{\Omega_{\zeta_\ell}
       ([\widetilde c_{\ell,h}])
     =\frac{\log\ell}{\sqrt\ell}\|\eta\|_2^2>0.}           \tag{11}
\]
(6)与(11)同时成立：
远端单位修正类在同一个普通HH₁中确实非零，
虽然原单一普通电荷已经为零。
这否定“原电荷为零就等于HH边界”的接法；
非零性来自一个合法同调泛函，不是从非零边界算子猜测。

这里的ζ随ℓ变化，支集也随L增长。
它检验全部允许紧支混合测试，未宣称固定支集上的电荷尾不稳定；
511按固定支集选择有限S的标量比较仍成立。

## 6. 对真实主商的具体启示与限制

若h来自原极化 \(h=(f*g^\sharp+g*f^\sharp)/2\)，
令 \(k_\zeta=e^{-t/2}\zeta(t)\)，则新的h就是 \(h*k_\zeta\)，
准确对应仍紧支的 \(f,\ g*k_\zeta\)。
若g的两个次数矩为零，这次卷积也保持它们：
\(M_{g*k_\zeta}(s)=M_g(s)M_{k_\zeta}(s)\) 在s=0、1消失。
混合检测没有通过引入非紧支函数或舍掉原次数条件取得。

本稿排除的是把单一kerΩ全部当成HH边界，
或把它全部商掉而又要求这些实际中心作用与混合电荷下降的方案。
未构造[405](405-f1-adelic-restriction-moments-and-radical.md)的几何主除子；
也未证明Ωζ与405所需全部混合配对在一个已完成几何商上同一。
若将某个类认证为真正principal，仍需证明两次数、
完整混合根空间、对应复合和本轮中心作用的下降条件。

下一步应从真实源关系识别哪些类同时消掉这些混合检测，
并解释无绝对S₁尾时采用哪种有源相容结构；
不能按单一电荷的数值零直接删掉远端素数。
完整Weil非正性、独立算术Hodge约束、RR和RH仍开放。
