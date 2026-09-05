# 291. 多项式平方负迹证书：最优阶 S/d 与固定次数障碍

日期：2026-09-06。新周期第1轮的核心近似接口审计。

状态：[T] 显式正核平方证书及有限迹/lag 接口；
[T/N] 所有区间上一致多项式平方证书的 \(S/d\) 阶下界；
[T/N] 实际有限 prime--continuum 符号的宽双侧谱区间及一致证书次数障碍；
[O] 实际算术 signed response 的一致估计。
“最优阶”不表示本文常数最优，也不表示发现了新的 Jackson 逼近方法。
本篇不证明 RH、GRH 或任何零点比例；不更新 PDF。

## 1. 对象、目标与不可隐藏的尺度

令 \(X=X^*\) 属于有限迹代数 \((\mathcal M,\tau)\)，先取
\(\tau(1)=1\)，并有一个已独立验证的谱界
\[
 \|X\|\le S,\qquad S>0.
 \tag{1}
\]
这里 \(S\) 是**同一个目标 current 的谱界**。它可以来自源的总变差上界，
但不能未经证明就等同于254中两正源质量和 \(A+B\)：
若 \(X\) 还含 Gamma、常数、尾部或其他通道，这些项也必须计入(1)。
把 \(X\) 换成 \(X/S\) 后，实际负迹仍是 \(S\tau((X/S)_-)\)，不能漏乘 \(S\)。

对实或复多项式 \(b\)，要求
\[
 \sup_{|x|\le S}|b(x)|\le1,\qquad
 g_b(x)=(-x)_++x|b(x)|^2,\qquad
 E_S(b)=\sup_{|x|\le S}g_b(x).
 \tag{2}
\]
因为 \(b\) 是 contraction，
\[
 g_b(x)=
 \begin{cases}
 |x|(1-|b(x)|^2),&x<0,\\
 x|b(x)|^2,&x\ge0
 \end{cases}
 \quad\hbox{且}\quad 0\le g_b(x)\le S.
 \tag{3}
\]
我们直接控制这个**加权平方缺口**，不先一致逼近
187中的 \(a_\rho(x)=(-x)_+/(( -x)_++\rho)\) 再分别支付软化与逼近误差。

以下将显式构造一个只依赖 \(S,m\) 的实多项式 \(b_{m,S}\)，满足
\[
 0\le b_{m,S}(x)\le1,\qquad
 \deg b_{m,S}\le2m-2,\qquad
 E_S(b_{m,S})\le\frac{3\pi S}{m}.
 \tag{4}
\]
同时证明：对每个 \(d\ge1\)，任何满足(2)、次数至多 \(d\) 的实或复多项式，
\[
 E_S(b)\ge\frac{S}{216d}.
 \tag{5}
\]
所以固定次数的一致绝对代价不能是 \(o(S)\)；改变 \(\rho\) 本身并不能绕过它。
下界量词是“整个区间上有效的统一证书”，不是对每个实际 \(X\) 都宣称必须
支付同样代价。一个特殊 current 的谱分布可能不访问最坏标量点。

## 2. 显式正 Jackson 核及首绝对矩 [T]

圆周积分统一使用 \(dt/(2\pi)\)，主值代表取 \(-\pi\le t\le\pi\)。
对整数 \(m\ge1\)，定义
\[
 D_m(t)=\frac{\sin(mt/2)}{\sin(t/2)},\qquad
 A_m=\frac{2m^3+m}{3},\qquad
 J_m(t)=\frac{D_m(t)^4}{A_m}.
 \tag{6}
\]
在 \(t=0\) 取连续值 \(D_m(0)=m\)；第四次幂是 \(2\pi\)-周期函数。

### 引理291-A

\(J_m\) 是非负、偶的三角多项式，次数至多 \(2m-2\)，并且
\[
 \int_{-\pi}^{\pi}J_m(t)\frac{dt}{2\pi}=1,\qquad
 I_m:=\int_{-\pi}^{\pi}|t|J_m(t)\frac{dt}{2\pi}
       \le\frac{3\pi}{2m}.
 \tag{7}
\]

证明。有限几何和的平方给
\[
 D_m(t)^2
 =\left|\sum_{j=0}^{m-1}e^{ijt}\right|^2
 =\sum_{|j|<m}(m-|j|)e^{ijt}.
 \tag{8}
\]
再平方，第四次幂的常数项为
\[
 m^2+2\sum_{j=1}^{m-1}(m-j)^2
     =m^2+\frac{(m-1)m(2m-1)}3=A_m.
 \tag{9}
\]
这证明次数、正性及归一化。

三角和上界与 \(\sin(|t|/2)\ge |t|/\pi\) 给
\[
 |D_m(t)|\le\min\{m,\pi/|t|\}\qquad(0<|t|\le\pi).
 \tag{10}
\]
在 \(t=\pi/m\) 分割首矩，精确计算两个初等积分：
\[
 \begin{aligned}
 I_m
 &\le\frac1{\pi A_m}
   \left\{\int_0^{\pi/m}tm^4\,dt
              +\int_{\pi/m}^{\pi}\frac{\pi^4}{t^3}\,dt\right\}\\
 &=\frac{\pi(2m^2-1)}{2A_m}
 \le\frac{3\pi}{2m}.
 \end{aligned}
 \tag{11}
\]
这也包括 \(m=1\)，此时第二个积分为空且 \(J_1=1\)。
所有估计都是整个圆周上的积分，不依赖数值频率截断。\(\square\)

## 3. 阶跃卷积、平方缺口与显式 Chebyshev 系数 [T]

令圆周阶跃
\[
 h(\theta)=\mathbf1_{\{\cos\theta<0\}},
 \tag{12}
\]
在跳点的取值不影响后续积分。置
\[
 B_m(\theta)=\int_{-\pi}^{\pi}J_m(t)h(\theta-t)\frac{dt}{2\pi}.
 \tag{13}
\]
正概率核立即给 \(0\le B_m\le1\)。
两函数均偶且 \(J_m\) 具有有限 Fourier 支撑，所以 \(B_m\) 是偶三角多项式，
次数至多 \(2m-2\)。因此存在唯一实多项式 \(b_{m,S}\)，使
\[
 b_{m,S}(S\cos\theta)=B_m(\theta),\qquad
 \deg b_{m,S}\le2m-2.
 \tag{14}
\]

### 定理291-B（直接加权平方逼近）

对全部 \(|x|\le S\)，
\[
 |x|\,|b_{m,S}(x)-\mathbf1_{\{x<0\}}|\le S I_m,
 \tag{15}
\]
\[
 \boxed{\quad
 0\le g_{b_{m,S}}(x)\le2S I_m\le\frac{3\pi S}{m}.
 \quad}
 \tag{16}
\]

证明。固定 \(x=S\cos\theta\)。若
\(h(\theta-t)\ne h(\theta)\) 且 \(x\ne0\)，两个余弦处于不同符号侧，故
\[
 |\cos\theta|
    \le|\cos\theta-\cos(\theta-t)|\le |t|.
 \tag{17}
\]
在没有符号失配处，阶跃差为零。把(17)乘正核并积分，用三角不等式即得(15)。
在 \(x=0\) 两端均为零，无须给阶跃指定特殊值。

当 \(x<0\)，
\[
 g_b(x)=|x|(1-b(x))(1+b(x))
        \le2|x|(1-b(x))\le2S I_m.
 \]
当 \(x\ge0\)，\(g_b(x)=xb(x)^2\le xb(x)\le S I_m\)。
结合(7)得到(16)。\(\square\)

这个证明不需要在跳点一致逼近阶跃——那本来不可能；
它利用的是缺口中保留的权 \(|x|\)。

### 3.1 可直接计算的系数

置 \(a_{m,j}=(m-|j|)_+\)，并定义有限整数卷积
\[
 A_{m,k}=\sum_{j\in\mathbb Z}a_{m,j}a_{m,k-j},\qquad
 \gamma_{m,k}=A_{m,k}/A_m.
 \tag{18}
\]
这里 \(a_{m,j}=0\) 于 \(|j|\ge m\)，所以和式有限，
\(\gamma_{m,0}=1\)，而 \(\gamma_{m,k}=0\) 于 \(|k|>2m-2\)。
式(8)给 \(J_m(t)=\sum_k\gamma_{m,k}e^{ikt}\)。

阶跃的余弦系数由一次积分给出：
\[
 h(\theta)\ \hbox{的常数项为 }1/2,\qquad
 [\cos(k\theta)]h=-\frac{2}{\pi k}\sin(k\pi/2)
        \quad(k\ge1).
 \tag{19}
\]
因此无需运行逼近优化或读取 \(X\) 的特征向量，就有
\[
 \boxed{\quad
 b_{m,S}(x)=\frac12-\frac2\pi
     \sum_{k=1}^{2m-2}
       \gamma_{m,k}\frac{\sin(k\pi/2)}k\,T_k(x/S).
 \quad}
 \tag{20}
\]
奇偶性给
\[
 b_{m,S}(-x)=1-b_{m,S}(x),\qquad b_{m,S}(0)=1/2.
 \tag{21}
\]
偶数 \(k\) 的项为零，所以 \(m\ge2\) 时实际次数至多 \(2m-3\)；
本文使用较保守的 \(2m-2\) 上界以统一参数账本。
当 \(m=1\)，和式为空，\(b_{1,S}=1/2\)，并且
\[
 E_S(b_{1,S})=3S/4.
 \tag{22}
\]
这说明(16)的小 \(m\) 常数可以很松；不声称 \(3\pi\) 最优。

## 4. 有限迹证书与非归一化迹 [T]

### 定理291-C（polynomial-square negative-trace certificate）

在(1)及 \(\tau(1)=1\) 下，
\[
 \boxed{\quad
 -\tau\!\left[Xb_{m,S}(X)^2\right]
 \le\tau(X_-)
 \le-\tau\!\left[Xb_{m,S}(X)^2\right]+\frac{3\pi S}{m}.
 \quad}
 \tag{23}
\]
更准确的误差可取 \(2S I_m\)；或者直接使用
\(\min\{S,3\pi S/m\}\)。

证明。\(b_{m,S}\) 是实多项式且在目标谱区间取值于 \([0,1]\)，
所以 \(b_{m,S}(X)^2\) 是正 contraction，且与 \(X\) 对易。
标量恒等式(3)经 functional calculus 给
\[
 \tau(X_-)+\tau[Xb_{m,S}(X)^2]
        =\tau(g_{b_{m,S}}(X)).
 \tag{24}
\]
用(16)和正迹即得(23)。这不要求整个代数交换；
只使用单个自伴 \(X\) 生成的交换函数演算。\(\square\)

若改用任意满足(2)的复多项式，则(24)应写成
\[
 \tau(X_-)+\tau[Xb(X)^*b(X)]=\tau(g_b(X)).
 \tag{25}
\]
复值时不能把 \(b^*b\) 偷换成 \(b^2\)；二者的区别在下界定理中同样保留。

若 \(\tau(1)=t_0<\infty\) 而不归一化，(23)的加性误差必须是
\[
 \frac{3\pi S}{m}\,t_0.
 \tag{26}
\]
例如普通 \(n\times n\) 矩阵迹给 \(t_0=n\)，不能漏掉该维数。
\(t_0=0\) 的正迹情形平凡；以下必要性讨论取 \(t_0>0\)。
只有已知归一化 \(\tau(1)=1\) 时才可直接使用(23)。

## 5. 自包含的次数下界：代价 S/d 的阶不可改善 [T/N]

### 引理291-D（区间内部的多项式导数界）

若复多项式 \(p\) 满足 \(\deg p\le d\)、\(d\ge1\)、
\(\sup_{[-1,1]}|p|\le1\)，则
\[
 |p'(x)|\le9d\qquad(|x|\le1/2).
 \tag{27}
\]

证明。置
\[
 P(z)=z^d p((z+z^{-1})/2).
 \tag{28}
\]
展开后负幂被 \(z^d\) 消去，故 \(P\) 是次数至多 \(2d\) 的普通多项式。
在单位圆上，\(|P(e^{i\theta})|=|p(\cos\theta)|\le1\)。
最大模原理同时作用于 \(P(z)\) 和多项式 \(w^{2d}P(1/w)\)，给
\[
 |P(z)|\le
 \begin{cases}
 1,&|z|\le1,\\
 |z|^{2d},&|z|\ge1.
 \end{cases}
 \tag{29}
\]
对任意 \(|z_0|=1\)，半径 \(r=1/(2d)\) 的圆盘上有
\[
 |P(z)|\le(1+1/(2d))^{2d}<3.
 \]
由 Cauchy 导数公式，\(|P'(z_0)|\le3/r=6d\)。
对 \(p(\cos\theta)=e^{-id\theta}P(e^{i\theta})\) 求导，得到
\[
 \left|\frac{d}{d\theta}p(\cos\theta)\right|\le7d.
 \]
当 \(|\cos\theta|\le1/2\)，\(|\sin\theta|\ge\sqrt3/2\)，故
\[
 |p'(\cos\theta)|\le\frac{14}{\sqrt3}d<9d.
 \]
证明不引用外部 Bernstein/Markov 近似定理。\(\square\)

### 定理291-E（所有 contraction 平方证书的下界）

设 \(S>0,d\ge1\)，\(b\) 为次数至多 \(d\) 的实或复多项式，
\(\sup_{[-S,S]}|b|\le1\)。则
\[
 \boxed{\qquad E_S(b)\ge S/(216d).\qquad}
 \tag{30}
\]

证明。归一化 \(p(x)=b(Sx)\)，令 \(\varepsilon=E_S(b)/S\)。
\(\varepsilon=0\) 不可能：正半区会迫使 \(p=0\)，由多项式恒等性
在负半区也为零，与缺口为零矛盾。
若 \(\varepsilon\ge1/8\)，(30)立即成立。
否则取 \(t=4\varepsilon\in(0,1/2)\)。
在 \(x=t\) 和 \(x=-t\) 使用缺口上界，分别得到
\[
 |p(t)|^2\le1/4,\qquad |p(-t)|^2\ge3/4.
 \tag{31}
\]
所以反三角不等式给
\[
 |p(-t)-p(t)|\ge |p(-t)|-|p(t)|
             \ge(\sqrt3-1)/2>1/3.
 \tag{32}
\]
另一方面，复多项式也可沿实区间积分导数。由引理291-D，
\[
 |p(-t)-p(t)|
    \le\int_{-t}^{t}|p'(u)|\,du
    \le18dt=72d\varepsilon.
 \tag{33}
\]
于是 \(\varepsilon\ge1/(216d)\)，得证。\(\square\)

### 5.1 零次、小次数及最优阶的准确意义

当 \(d=0\)，令 \(|b|^2=v\in[0,1]\)，则
\[
 E_S(b)=S\max\{v,1-v\},\qquad
 \inf_{\deg b=0,\ |b|\le1}E_S(b)=S/2,
 \tag{34}
\]
在 \(b=1/\sqrt2\) 处达到。这与(22)不矛盾：
本篇的 \(m=1\) kernel 构造不是零次极小化解。

对任意 \(d\ge1\)，取 \(m=\lfloor d/2\rfloor+1\)，则(14)给
\(\deg b_{m,S}\le d\)，且 \(m\ge(d+1)/2\)。
因此无论极小化类取所有复 contraction、所有实 contraction，
还是更小的 \(0\le b\le1\) 实多项式，都有
\[
 \frac{S}{216d}
 \le\inf_b E_S(b)
 \le\min\left\{S,\frac{6\pi S}{d+1}\right\}.
 \tag{35}
\]
这就是本文的 \(\Theta(S/d)\)；未优化常数，也未确定最优多项式。

下界还直接作用于有限迹的**通用绝对证书**：
若一个预先给定的 \(b\) 声称对全部 \(\|X\|\le S\) 有
\[
 \tau(X_-)\le-\tau[Xb(X)^*b(X)]+C,
 \tag{36}
\]
取一维 \(X=xI\) 就要求 \(C\ge E_S(b)\)。
对 \(\tau(1)=t_0\)，则要求 \(C\ge t_0 E_S(b)\)。
因此固定绝对 \(C\) 的 uniform interval 方法必须有
\[
 d\ge \frac{S\,t_0}{216C}.
 \tag{37}
\]
这不是“每个实际 zeta current 都需要此次数”的断言：
若允许独立利用实际谱分布或其他算术信息而不要求全区间缺口界，
本下界并未排除改进。反之，用未知负谱量直接决定系数或缺口预算，
也不能称为已经独立获得的算术输入。

## 6. 与187软化上界的准确比较

187现有的证明路线给
\[
 \tau(X_-)\le-\tau[Xb(X)^2]
       +2\rho+5\epsilon\,\tau(|X|),\qquad
 \epsilon\le C_J\frac{S}{\rho d}.
 \tag{38}
\]
在这里只使用 \(\tau(1)=1,\|X\|\le S\)，于是
\(\tau(|X|)\le S\)；把该 Jackson 上界代入，其已展示的误差账本为
\[
 2\rho+\frac{5C_JS^2}{\rho d}.
 \tag{39}
\]
当次数足够大以使相关误差条件满足时，优化这个**上界表达式**，
取 \(\rho=S\sqrt{5C_J/(2d)}\)，得到
\[
 2\sqrt{10C_J}\,\frac{S}{\sqrt d}.
 \tag{40}
\]
因此本篇(35)把这套已给出的 worst-case 上界从 \(S/\sqrt d\) 改为 \(S/d\)。
它不是对所有可能软化核或所有旧方法最优性的下界；
若实际 \(\tau(|X|)\ll S\) 或另有更好的逼近误差，应另作比较。

本篇不支付 \(2\rho\)，但并未令代价消失。
为了只靠 universal polynomial square 给归一化迹 \(O(1)\) 的加性误差，
充分可取 \(m\asymp S\)，而(37)证明同阶次数在通用区间方法中必要。
固定二阶的困难因而不是只选错了 \(\rho=S/3\)，
而是整个固定次数 uniform square 方法具有尺度代价。

## 7. 同一 current 的 Chebyshev/lag 接口 [T/C/O]

### 7.1 不沿用旧 degree-two multiplier

定义新的实响应多项式
\[
 F_{m,S}(z)=-z\,b_{m,S}(z)^2.
 \tag{41}
\]
其次数至多 \(4m-3\)。对 \(m=1\)，\(F_{1,S}(z)=-z/4\)；
一般由(21)仍有
\[
 F_{m,S}'(0)=-1/4.
 \tag{42}
\]
它不是194–256旧的
\(-c_2^2z^3(z-\alpha S)^2\)。
特别，旧 multiplier 在平衡点的二阶退化、旧
\(q_\kappa(\mu,\Delta)\)、固定四阶预算和256 capture 估计，
都不能直接替换变量后复用。

### 7.2 Canonical 有限 lag 递推

设当前已被精确或带可控误差实现为有限 Hermitian lag 测度
\[
 d=\sum_j d_j,\qquad
 P(t)=\widehat d(t)\in\mathbb R,\qquad
 |P(t)|\le S,\qquad M=d(\mathbb R).
 \tag{43}
\]
每个 \(d_j\) 是有限总变差、紧支撑的复 Borel 测度；
总和满足 Hermitian 反射关系。
足够的谱界是 \(S\ge\|d\|_{\rm TV}\)，但可以使用另经证明的更紧界。
频率零点 \(M=P(0)\) 因而也在 \([-S,S]\)。

在卷积代数中取
\[
 C_0=\delta_0,\qquad C_1=d/S,\qquad
 C_{k+1}=2(d/S)*C_k-C_{k-1}.
 \tag{44}
\]
则 \(\widehat C_k(t)=T_k(P(t)/S)\)。
用(20)的明确系数形成
\[
 b_{m,S}(d)=\frac12\delta_0-\frac2\pi
   \sum_{k=1}^{2m-2}
       \gamma_{m,k}\frac{\sin(k\pi/2)}k\,C_k,
 \qquad
 q_{m,S}=F_{m,S}(d)=-d*b_{m,S}(d)*b_{m,S}(d).
 \tag{45}
\]
这给 \(\widehat q_{m,S}(t)=F_{m,S}(P(t))\)，不读取目标零点或特征向量。
当 \(m\) 随 \(S\) 增长时，卷积阶和系数条件数的代价必须真实登记；
本篇没有证明这些高阶算术和式便于估计。

对每个 component 置 \(M_j=d_j(\mathbb R)\)，并定义普通多项式
\[
 R_{m,S,M}(z)=\frac{F_{m,S}(z)-F_{m,S}(M)}{z-M}.
 \tag{46}
\]
在 \(z=M\) 取导数值；它的次数至多 \(4m-4\)。
有限卷积恒等式给
\[
 q_j^\circ=(d_j-M_j\delta_0)*R_{m,S,M}(d),\qquad
 \sum_jq_j^\circ=q_{m,S}-F_{m,S}(M)\delta_0 .
 \tag{47}
\]
令 \(U_j\) 为 \(q_j^\circ\) 的零质量 primitive，
\(G_{ij}=\langle U_i,U_j\rangle\)。紧支撑与有限总变差保证
\(U_j\in L^2\)，从而
\[
 G\succeq0,\qquad
 \mathcal E_B(q_{m,S})=\mathbf1^*G\mathbf1.
 \tag{48}
\]
这是195的 polynomial divided-difference 证明对新 \(F\) 的直接有限应用；
必须保持完整 current 对各通道使用**同一个新 multiplier**。
不能只在旧 prime/continuum 分量末尾追加 Gamma 而不改变(46)。

### 7.3 Direct Cauchy 证书及尚未证明的算术输入

若 \(\tau_C\) 是 stationary symbol 的规范 Cauchy 迹，
\(d\mu_C(t)=dt/(\pi(1+t^2))\)，则其 characteristic function 为
\(e^{-|u|}\)，故
\[
 -\tau_C[P\,b_{m,S}(P)^2]
       =\int e^{-|u|}\,dq_{m,S}(u).
 \tag{49}
\]
对任意有限紧支撑 \(q\)，置 \(T_q=q(\mathbb R)\)、
\(DA_q=q-T_q\delta_0\)，取紧支撑 primitive。分部积分直接给
\[
 \int e^{-|u|}\,dq(u)
   =T_q-\int (e^{-|u|})'A_q(u)\,du,
 \qquad
 \left|\int e^{-|u|}\,dq(u)\right|
       \le|T_q|+\|A_q\|_2,
 \tag{50}
\]
因为 \(\|(e^{-|u|})'\|_2=1\)。
结合(23)、(48)，得到同一个完整有限 current 的新充分账本
\[
 \boxed{\quad
 \tau_C(P_-)
 \le |F_{m,S}(M)|+\sqrt{\mathbf1^*G\mathbf1}
                         +\frac{3\pi S}{m}.
 \quad}
 \tag{51}
\]
因此若另有完整 Weil/显式公式识别误差 \(\eta_n\)，一个明确的条件输入为
\[
 \sup_n\left\{
 |F_{m_n,S_n}(M_n)|+\sqrt{\mathbf1^*G_n\mathbf1}
       +3\pi S_n/m_n+\eta_n
 \right\}<\infty .
 \tag{52}
\]
在194所依赖的完整 divisor、有限迹、Poisson 和共尾识别条件均已成立时，
(52)才可接到原 bounded-negative-trace 中心线定理。
本篇没有证明实际 zeta 的(52)，也没有重建或自动满足那些解析条件。

本篇真正缩小的是**通用近似误差账本**：
把两个独立参数 \(\rho,\epsilon\) 的粗组合替换为明确的 \(3\pi S/m\)，
并证明其次数阶的最优性。新的高阶 signed arithmetic response 仍[O]。
不能仅因已经能选 \(m_n\asymp S_n\)，就声称正性或有界负迹由选择产生。

### 7.4 实际素数符号的谱区间并非粗 TV 界的假象 [T/N]

本节回到真实 von Mangoldt 系数，但只处理**未加入 Gamma** 的原有限
prime--continuum 符号。固定 \(0<\sigma<1/2\)，整数 \(Y=N\ge2\)，置
\[
 w_Y(x)=x^{-\sigma}e^{-x/Y},\qquad
 P_Y(t)=\sum_{2\le n\le Y}\Lambda(n)w_Y(n)\cos(t\log n)
               -\int_1^Yw_Y(x)\cos(t\log x)\,dx,
 \tag{53}
\]
\[
 A_Y=\sum_{2\le n\le Y}\Lambda(n)w_Y(n),\quad
 B_Y=\int_1^Yw_Y(x)\,dx,\quad S_Y^{\rm src}=A_Y+B_Y,
 \qquad
 A_Y^{\rm even}=\sum_{p^{2k}\le Y}(\log p)w_Y(p^{2k}).
 \tag{54}
\]
式(53)保留全部原子、连续项及原质量 \(P_Y(0)=A_Y-B_Y\)；
没有把它换成居中 \(\widehat r\) 或完整 Weil current。
考虑 \(P_Y\) 在 \(L^2(\mathbb R,dt/(\pi(1+t^2)))\) 上的乘法算子。

**定理291-F。** 对每个这样的固定 \(Y\)，其本质谱包含
\[
 [-A_Y+2A_Y^{\rm even},\,A_Y].
 \tag{55}
\]
当 \(Y\to\infty\) 时，
\[
 A_Y\asymp_\sigma B_Y\asymp_\sigma Y^{1-\sigma},\qquad
 A_Y^{\rm even}\ll_\sigma Y^{1/2-\sigma}=o(A_Y).
 \tag{56}
\]
所以充分大时本质谱包含 \([-A_Y/2,A_Y/2]\)，而
\(\|P_Y\|_\infty\asymp_\sigma S_Y^{\rm src}\)。
若次数至多 \(d\ge1\) 的多项式 \(b\) 在实际整个谱上满足 \(|b|\le1\)，
则该实际全谱上的**一致标量缺口**必满足
\[
 \sup_{x\in\operatorname{spec}(P_Y)}
       \{(-x)_++x|b(x)|^2\}\ \ge\ \frac{A_Y}{432d}.
 \tag{57}
\]

证明。先固定 \(Y\)，枚举其中有限多个素数 \(p_1,\ldots,p_r\)。
唯一分解给
\(\sum_j k_j\log p_j\ne0\) 对所有非零 \(k\in\mathbb Z^r\) 成立。
故对任意非零 \(k\)，
\[
 \lim_{T\to\infty}\frac1T\int_0^T
       e^{it\sum_jk_j\log p_j}\,dt=0.
\]
任给素数相位 torus 上的一个开盒，取支撑于盒内、积分严格正的非负光滑
周期 bump。其 Fourier 系数绝对可和，所以上式允许逐项取时间平均，
平均值恰为正的常数 Fourier 系数。于是轨道
\((t\log p_j\bmod2\pi)_j\) 在任意大的 \(t\) 命中此开盒：
如果只在某有限初段命中，长期平均只能为零。
这也直接证明本节所需的相位逼近，不调用未知素数或零点分布。

连续部分经 \(u=\log x\) 变成有限区间上
\(e^{(1-\sigma)u-e^u/Y}\) 的余弦变换，积分分部给 \(O_Y(1/|t|)\)；
所以当 \(|t|\to\infty\) 时消失。
依次缩小全零相位和全 \(\pi\) 相位的盒，分别选取趋于无穷的频率。
前一种使每个素数幂余弦趋于1，后一种使
\(\cos(t\log p^k)\to(-1)^k\)。因此 \(P_Y\) 的值域闭包包含两个端点
\[
 A_Y,\qquad -A_Y+2A_Y^{\rm even}.
 \tag{58}
\]
对每个固定 \(Y\) 取相位极限后才令 \(Y\) 增长；本证明没有统一的命中高度。

\(P_Y\) 是连续实函数，所以值域闭包是区间，包含(55)。
而 Cauchy 密度在整个实轴严格为正：每个达到的值的任意邻域之原像，
都含非空开区间并有正测度。因此本质值域恰等于值域闭包，
乘法算子的谱就是这个集合，证明(55)。

这里只需初等双边 Chebyshev 估计 \(\psi(x)\asymp x\)。
为完整起见，\(\prod_{n<p\le2n}p\) 整除 \(\binom{2n}{n}\)，所以
\(\vartheta(2n)-\vartheta(n)\le2n\log2\)；在二的幂处求和及单调性
给 \(\vartheta(x)\ll x\)。于是
\(\psi(x)=\sum_{k\le\log_2x}\vartheta(x^{1/k})
 \ll x+\sqrt x\log x\ll x\)。
反向，每个 \(p^k\le2n\) 对 \(\log\binom{2n}{n}\) 的系数
\(\lfloor2n/p^k\rfloor-2\lfloor n/p^k\rfloor\) 是0或1，故
\(\psi(2n)\ge\log\binom{2n}{n}
 \ge2n\log2-\log(2n+1)\)；
再取 \(n=\lfloor x/2\rfloor\) 得下界。
这个估计给 \(A_Y\) 的两侧界：
下界用 \(w_Y(n)\ge e^{-1}Y^{-\sigma}\)，上界对递减幂权积分分部；
连续积分直接给 \(B_Y\asymp Y^{1-\sigma}\)。
这里不需要 RH 级误差或定量 PNT。
偶次幂与普通 prime-power 变量之间有精确的一一对应，
\[
 A_Y^{\rm even}
   =\sum_{n\le\sqrt Y}\Lambda(n)n^{-2\sigma}e^{-n^2/Y}
   \le\sum_{n\le\sqrt Y}\Lambda(n)n^{-2\sigma}
   \ll_\sigma Y^{(1-2\sigma)/2}.
 \tag{59}
\]
最后一步只用 \(\psi(x)\ll x\) 和 \(2\sigma<1\) 的部分求和，
得到(56)。充分大时 \(A_Y^{\rm even}\le A_Y/4\)，故有对称子区间；
在其上用291-E、取谱半径参数 \(S=A_Y/2\)，得到(57)。
上界 \(\|P_Y\|_\infty\le S_Y^{\rm src}\) 与端点 \(A_Y\) 则给范数同阶。
\(\square\)

这个加强排除了对(53)仅靠更紧的**全频一致谱界**来把固定次数的
绝对缺口变成 \(O(1)\)：次数仍至少与 \(S_Y^{\rm src}\) 同阶。
它不排除对实际谱分布积分后取得更好的误差；
命中极值的频率可以很大，Cauchy 质量可以随 \(Y\) 极小。
尤其不能把(57)的 supremum 下界换成
\(\tau_C(g_b(P_Y))\) 的同样下界，更不能断言实际负迹发散。
有限维压缩、加入 Gamma、复相位的 Dirichlet \(L\) 源以及其他迹权
也都需要分别核对，不能自动移植本节的双侧谱结论。

## 8. 最小公理、删除审计与循环性

| 公理或步骤 | 证明中的具体作用 | 删除后的失效 |
|---|---|---|
| 有界自伴 \(X\) 与实际谱界 \(S\) | functional calculus 和整区间 contraction | 谱跑出区间时 \(b(X)\) 未必是 contraction，(3)可失效 |
| 正且归一化的圆周核 | 保持 \(0\le b\le1\) | 一般 Fourier 截断会有 Gibbs 超调，不能直接用平方正效应 |
| 加权阶跃误差 \(|x||b-h|\) | 跳点附近的误差以 \(|x|\) 支付 | 无权阶跃的一致误差不趋零；不能误称普通 uniform convergence |
| 同一个多项式的平方 | 给(24)的合法正 contraction response | 复多项式必须用 \(b^*b\)，不能用 \(b^2\) |
| 正有限迹及明确的 \(\tau(1)\) | 把标量缺口界积分为绝对迹界 | 普通矩阵迹若漏维数，会得到虚假的尺度收益 |
| 固定次数并在整个区间控制 \(|b|\) | Cauchy 导数界与(30) | 若只在未知实际谱点约束 \(b\)，本下界不自动适用 |
| 同一完整 lag current | (45)--(51)的 exact response 身份 | 改 source、参数、Gamma 后沿用旧 multiplier 会破坏等式 |
| 真实素数幂支撑、正权及有限 cutoff | (58)中全0/全π相位给两个算术端点 | 一般复相位L函数不能沿用这些端点 |
| 连续背景的有限 lag 变换衰减 | 使极大频率的背景消失 | 另一个离散背景可能保留与素数同相的贡献 |
| Cauchy权的全实轴正支撑 | 值域闭包成为实际本质谱 | 截断高度上的谱不必包含这些远频率极值 |

删除 contraction 的具体例子是常数 \(b=2\)：在负 \(x\) 上
\(g_b(x)=-3|x|<0\)，不再有(23)的下侧不等式。
删除自伴性时，实轴逐点正性不构成非正规算子的正效应证书。
删除迹归一化时，取 \(X=-SI_n\) 就看出任何点态缺口都必须乘 \(n\)。
允许次数随 \(S\) 增长后，(16)说明固定次数障碍可以被克服，
但算术 convolution 阶数也同时增长。

非循环性：\(J_m,\gamma_{m,k},b_{m,S}\) 全部由 \(m,S\) 显式产生；
未使用零点位置、未知负谱投影或 GNS/紧性来产生算术预算。
阶跃只作为一个已知的**标量目标函数**用于构造通用多项式，
最终响应仍是(45)中的有限算术 polynomial。
通用下界是有限标量反例；7.4进一步给实际子系统的一致证书障碍，
但两者都不是 RH 反例，也不提供实际积分负迹下界。

## 9. 文献定位、下一最小问题和审计

正核保持正性、Chebyshev 滤波和 Jackson 的 \(1/d\) 分辨率是经典机制。
已核对的一手定位为 Weiße–Wellein–Alvermann–Fehske,
“The Kernel Polynomial Method”, Rev. Mod. Phys. 78 (2006), 275–306，
[作者预印本的 §II.3.2–II.3.3](https://arxiv.org/html/cond-mat/0504627v2) [R]。
该文式(71)的优化 KPM Jackson 系数不是本篇(6)的正弦四次卷积核；
本篇没有混用两个核的系数或把(16)、(30)的具体常数归给该文。
本篇所需核、迹平方误差和次数下界均在正文独立证明。
未取得正文的其他检索材料不进入结论链。

本篇不宣称新的 Jackson 方法、最优常数或已确认的论文新颖性。
当前可审计的结果是(16)、(23)、(30)、同一 current 的(51)，以及
真实有限 prime--continuum 子系统的(55)--(57)。
下一算术输入只能是新次数下的实际 signed response，或独立有效的
实际谱分布加权误差；对(53)仅缩小全频谱界已被7.4排除。
不再仅通过调小 \(\rho\)、重新归一化或把旧 \(J_4\) 改名晋级。
若高次数强迫恢复完整已知 RH 等价矩预算，须如实登记并停止该捷径。

本轮先记录完整证明，不写新模型或 PDF。
正文由 carrier_audit 完整读取187/194/195后重建，主代理完整读取并复核；
gap_exception_audit 与 midband_compute 另行完成全文独立检查，核心证明通过。
7.4由主代理补入，其候选全证明已经两路独立核验；
gap_exception_audit 又完成最终落盘逐式检查，结果通过。
内部复核不代替外部同行评审、新颖性核验或Goal阶段验收。

### 9.1 可复现有限计算 [E]

[jackson_negative_trace_probe.py](../scripts/jackson_negative_trace_probe.py)
只使用标准库与 mpmath，不写文件、不用网络：

```text
python -B scripts/jackson_negative_trace_probe.py
```

主代理及两名独立代理复跑通过，约9--10秒。
核系数以整数卷积核验，另对 \(m\le8\) 从两套不同有限几何和展开交叉检查。
MP60计算把Chebyshev多项式与原阶跃所在半圆的直接积分比较，
最大误差约 \(1.56\cdot10^{-61}\)。
在 \(m=1,2,3,4,8,16,32\) 的有限网格，\(m\) 乘样本最大缺口分别约为
\(0.75,0.51802,0.51767,0.50841,0.50432,0.50319,0.50290\)；
这些不是连续 supremum、最优常数或渐近极限证书。

另一分支使用明确的合成符号
\(P(t)=-1/5+(9/10)\cos t+(3/10)\cos2t\)，已认证
\(\|P\|_\infty\le S=7/5\)，原质量 \(M=P(0)=1\)。
它不是实际 von Mangoldt、连续背景或 Gamma 配置。
利用完整周期化 Cauchy 密度
\(\sinh(1)/(2\pi(\cosh(1)-\cos t))\)，直接积分与完整 lag 卷积
\(\sum_\omega q_\omega e^{-|\omega|}\) 的最大差约为 \(1.41\cdot10^{-60}\)。
真实保留的合成谱负迹为约 \(0.241643359863\)，在 \(m=2,4,8\)
的带符号平方响应分别为
\(0.0967529784403,0.186168349741,0.230574262974\)。
脚本不删除正谱贡献或常数质量，不截断未周期化的 Cauchy 频率尾。
这批MP实验仍不是区间认证；全次数、全谱结论来自正文证明。

提交前目录/TeX引用检查和11项目录回归通过，77项注册覆盖及模拟分发检查通过。
没有据此声称运行了77项重型数学计算或本轮完整远程CI。
