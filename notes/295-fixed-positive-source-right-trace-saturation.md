# 295. 固定正整数源、真实前缀记录与右侧迹的包络饱和

日期：2026-09-06。B1z 新周期第4轮；归属：独立 response 论文的边界审计。
状态：[T/N] 一个固定正整数源、完整匹配截断及真正归一化 Abel 前缀记录；
[T/N] 一般平滑次幂 PNT 包络下的右侧正负迹同阶饱和；
[T] 有限 Poisson／Euler 开集接口及模型的非亚纯边界。
本篇不是实际 \(\Lambda\) 的反例，不证明 RH 为假，也不排除所有共尾选择。

## 1. 主张、共同对象与量词

固定
\[
 0<\sigma _0<\beta<1/2,\qquad
 d=\beta-\sigma _0,\qquad \lambda_*=1-\beta .
 \tag{1}
\]
这里 \(\lambda_*\) 是一个实指数，下面的 \(\lambda(n)\) 才是整数源权。
固定函数 \(\omega:[0,\infty)\to[0,\infty)\)，在充分大自变量处为 \(C^1\)，且
\[
 \omega(u)\longrightarrow\infty,\qquad \omega'(u)\longrightarrow0 .
 \tag{2}
\]
小区间上的延伸固定为连续非负函数；不影响任何渐近结论。
(2)蕴含 \(\omega(u)=o(u)\)，但不要求 \(\omega\) 单调。
特别可取 \(\omega(u)=c\sqrt u\)，在零点附近作固定光滑延伸。

### 定理295-A [T/N]

存在一套固定的实权 \(\lambda(n)\in[1/2,3/2]\)，\(n\ge2\)，并且
\(\lambda(n)\to1\)。另置 \(\lambda(1)=0\)，故下文所有 \(n\le Y\)
和式都与从 \(n=2\) 起求和一致。定义
\[
 \psi_\lambda(x)=\sum_{2\le n\le x}\lambda(n),\qquad
 E_\lambda(x)=\psi_\lambda(x)-x+1,\qquad E_\lambda(1)=0 ,
 \tag{3}
\]
\[
 A_{\sigma _0}(Y)=
 \sum_{n\le Y}\lambda(n)n^{-\sigma _0}e^{-n/Y}
       -\int_1^Yx^{-\sigma _0}e^{-x/Y}\,dx,\qquad Y\ge1 .
 \tag{4}
\]
同一个源具有以下性质。

1. 全部实尺度上
   \[
   |E_\lambda(x)|\le Cx e^{-\omega(\log x)}\quad(x\ge1).
   \tag{5}
   \]
   所以它满足定性 PNT 和 Chebyshev 上界；这不是只在所选窗口上的估计。
2. 令 \(X_j=2^{4^j}\)、\(U_j=\log X_j\)、\(Z_j=X_j^2\)。存在固定
   \(c_*>0\) 和真正的整数前缀记录 \(Y_j=N_j\in[c_*Z_j,Z_j]\)，满足
   \[
   |N_j^{-d}A_{\sigma _0}(N_j)|
       =\max_{1\le n\le Z_j,\ n\in\mathbb Z}
                           |n^{-d}A_{\sigma _0}(n)|.
   \tag{6}
   \]
   特别它也是截至 \(N_j\) 的真正前缀最大值。沿这些点，置
   \(M_j=A_{\sigma _0}(Y_j)>0\)、\(L_j=\log Y_j\)，有
   \[
   \begin{split}
   B_j^0&=\exp\{\lambda_*U_j-\omega(U_j)\},\\
   M_j&\asymp B_j^0Y_j^d,\qquad
   \frac{M_j}{Y_j^{1/2-\sigma _0}\ell(Y_j)}\longrightarrow\infty,
   \end{split}
   \tag{7}
   \]
   其中 \(\ell(Y)=\max(1,\log\log\log Y)\)，只在充分大尺度使用。
3. 对相同的 Abel 参数和完整 cutoff，令
   \[
   H_j(u)=\sum_{n\le e^u}\lambda(n)n^{-\sigma _0}e^{-n/Y_j}
                    -\int_1^{e^u}x^{-\sigma _0}e^{-x/Y_j}\,dx .
   \]
   有尺度无关的常数
   \[
   |H_j(u)|\le C M_j e^{-d(L_j-u)},\qquad
   \|H_j\|_1+\|H_j\|_2\le C M_j
          \quad(0\le u\le L_j).
   \tag{8}
   \]
   同时 \(P_{\beta,\lambda}(Y_j)Y_j^d\le C M_j\)，这里
   \(P_{\beta,\lambda}(Y)=\max_{n\le Y}|\psi_\lambda(n)-n|/n^\beta\)。
4. 对全部 \(\sigma'\in[1/2,3/4]\)，使用原 Cauchy 概率迹
   \(d\mu_C(t)=dt/[\pi(1+t^2)]\)，定义
   \[
   P_{\sigma',j}(t)=
     \sum_{n\le Y_j}\lambda(n)n^{-\sigma'}e^{-n/Y_j}\cos(t\log n)
       -\int_1^{Y_j}x^{-\sigma'}e^{-x/Y_j}\cos(t\log x)\,dx .
   \tag{9}
   \]
   这是同一未中心化源的指数右移，不删去 \(P_{\sigma',j}(0)\)。
   令
   \[
   B_j=M_jY_j^{-d}\asymp B_j^0,\qquad
   \lambda_* V_j-\omega(V_j)=\log B_j ,
   \tag{10}
   \]
   其中 \(V_j\) 为充分大区域中的唯一解，再置
   \[
   b=\sigma'-\beta,\qquad
   T_j(\sigma')=B_j e^{-bV_j}.
   \tag{11}
   \]
   则一致地有
   \[
   \boxed{\quad
   \tau_C((P_{\sigma',j})_-)
    \asymp\tau_C((P_{\sigma',j})_+)
    \asymp\tau_C|P_{\sigma',j}|
    \asymp T_j(\sigma')\longrightarrow\infty .
   \quad}
   \tag{12}
   \]
   加入293的固定完成项 \(g_{\sigma'}\) 后，
   \(\tau_C((g_{\sigma'}-P_{\sigma',j})_-)\asymp T_j(\sigma')\) 亦成立。

所有常数允许依赖固定 \(\sigma _0,\beta,\omega\) 和下面一次选定的光滑函数，
但与 \(j,\sigma'\) 无关。特别，(12)允许任意共同日程
\(\sigma'_j=1/2+\delta_j\)、\(\delta_j>0\to0\)。

这些记录确实来自固定源的前缀最大值，不是每轮重新指定的两个原子。
但它们不是实际 \(\Lambda\) 的284记录。本定理也不声称该模型的每个合格
cutoff 或每条共尾序列都失败；它排除的是从(5)、(6)、(8)及有限接口
对所有此类输入普遍推出更小迹预算的推理。

## 2. 单一全局源：先选常数，再开始块序列

固定 \(h=1/8\) 及非负非零函数
\(\phi\in C_c^\infty((-h,h))\)。
下面只使用其固定有限范数，不需数值调参。记
\[
 \mathcal W(v)=
        \exp\{-\sigma _0(v-1)-e^{v-1}\},\qquad
 c_\phi=-\int\mathcal W'(v)\phi(v)\,dv>0 ,
 \tag{13}
\]
因为 \(-\mathcal W'=(\sigma _0+e^{v-1})\mathcal W>0\)。
为了保证最终选到真正晚段记录，预先取
\[
 C_{\rm early}=e^{\beta h}\|\phi\|_\infty,\quad
 C_{\rm Abel}=1+\frac{\sigma _0+1}{d},\quad
 C_{\rm pre}=(C_{\rm early}+3)C_{\rm Abel},
 \qquad
 K>\max\{1,4C_{\rm pre}/c_\phi\}.
 \tag{14}
\]
\(K\) 从此固定，不随 \(j\) 或 \(\sigma'\) 改变。

写
\[
 A_j=e^{U_j-\omega(U_j)},\qquad
 D_j=B_j^0 Z_j^\beta=e^{(1+\beta)U_j-\omega(U_j)} .
 \tag{15}
\]
从一个充分大的固定 \(j_0\) 起定义
\[
 \mathcal R(x)=\sum_{j\ge j_0}
   \left\{
      A_j\phi(\log x-U_j)
       +K D_j\phi(\log x-(2U_j-1))
   \right\}.
 \tag{16}
\]
每对块分别支撑在 \(x\asymp X_j\) 和 \(x\asymp Z_j\)，第二块完全在
\(Z_j\) 之前。各块互不相交、局部有限；下一对块在 \(Z_j\) 之后。
因此 \(\mathcal R\) 光滑、非负，在1附近恒零。

早块和晚块导数的上界分别为
\[
 C_\phi e^{-\omega(U_j)},\qquad
 C_{\phi,K} e^{-(1-\beta)U_j-\omega(U_j)} .
 \tag{17}
\]
由(2)均趋于零。选足够大的 \(j_0\) 使
\(\|\mathcal R'\|_\infty\le1/2\)，然后**一次性**定义
\[
 q(x)=1+\mathcal R'(x)\in[1/2,3/2],\qquad
 \lambda(n)=\int_{n-1}^n q(x)\,dx
           =1+\mathcal R(n)-\mathcal R(n-1).
 \tag{18}
\]
所有以后出现的 cutoff 都使用这同一数列。由(17)，还有
\(\lambda(n)\to1\)。

令
\[
 \epsilon(x)=
  \psi_\lambda(x)-\int_1^x q(v)\,dv .
 \tag{19}
\]
在整数点 \(n\ge1\) 有 \(\epsilon(n)=0\)；对 \(n\le x<n+1\)，
\(\epsilon(x)=-\int_n^x q(v)dv\)，所以 \(|\epsilon(x)|\le3/2\)。
于是全实轴的准确关系为
\[
 E_\lambda(x)=\mathcal R(x)+\epsilon(x),\qquad
 \psi_\lambda(n)-n=\mathcal R(n)-1 .
 \tag{20}
\]
这里保留了从 \(n=2\) 开始求和带来的常数 \(-1\)，没有把两种累计误差混同。

## 3. 全局 PNT、离散化及全部旧块

### 3.1 相同的 \(\omega\) 不在拼接中损失

由 \(\omega'=o(1)\)，固定有界 \(v\) 上有
\(\omega(U_j+v)-\omega(U_j)=o(1)\)，一致于 \(v\in[-h,h]\)。
故早块上
\[
 \mathcal R(x)\ll x e^{-\omega(\log x)} .
 \tag{21}
\]
晚块与此包络的比值至多为常数倍
\[
 \exp\{-(1-\beta)U_j+
       \omega(2U_j-1+v)-\omega(U_j)\}
       =\exp\{-(1-\beta)U_j+o(U_j)\}\longrightarrow0 .
 \tag{22}
\]
块外 \(\mathcal R=0\)。又 \(x e^{-\omega(\log x)}\to\infty\)，固定小区间
和(20)中的有界误差均可吸收，得到(5)。特别没有把 \(\omega\) 换成较小常数。

### 3.2 每个有限 cutoff 的加权离散化

对整数 \(N\) 及绝对连续函数 \(g\)，逐个单位区间比较给
\[
 \left|\sum_{n=2}^N\lambda(n)g(n)-\int_1^N q(x)g(x)dx\right|
 \le\frac32\int_1^N|g'(x)|dx .
 \tag{23}
\]
因此取 \(g=x^{-\sigma _0}e^{-x/Y}\) 时误差为 \(O(1)\)，一致于整数
\(1\le N\le Y\)。取
\(g=x^{-\sigma'}e^{-x/Y}\cos(t\log x)\) 时，误差为
\[
 O(1+|t|)\qquad(\sigma'\in[1/2,3/4]),
 \tag{24}
\]
因为递减权的总变差不超过1，且
\(\int_1^\infty x^{-\sigma'-1}e^{-x/Y}dx\le1/\sigma'\le2\)。
(24)只在固定频率窗口用于下界；不会将它直接积到整个 Cauchy 频轴。

### 3.3 旧块不能只按净质量忽略

对任意当前 cutoff \(Y\asymp Z_j\)，全部 \(k<j\) 块均完整包含在内。
在右移范围 \(\sigma'\in[1/2,3/4]\)，它们的**加权总变差**之和至多
\[
 C_K\sum_{k<j}
  \left\{ e^{(1-\sigma')U_k-\omega(U_k)}
       +e^{(1+\beta-2\sigma')U_k-\omega(U_k)}\right\}
 \le C_K j e^{U_{j-1}/2}.
 \tag{25}
\]
此处 \(e^{-x/Y}\le1\)，而有限支撑的 \(\phi'\) 只贡献固定常数。
由于 \(U_j=4U_{j-1}\) 以及 \(\omega(U_j)=o(U_j)\)，相对于
\[
 Q_j(\sigma')=e^{(1-\sigma')U_j-\omega(U_j)}
 \tag{26}
\]
有
\[
 \frac{j e^{U_{j-1}/2}}{\inf_{\sigma'\in[1/2,3/4]}Q_j(\sigma')}
 \le j\exp\{-U_j/8+\omega(U_j)\}\longrightarrow0.
 \tag{27}
\]
因此旧块的 Fourier 误差是统一的 \(o(Q_j)\)，不只是总质量很小。

## 4. 从两个尺度升级到真正的归一化 Abel 记录

令 \(b_0(y)=y^{-d}A_{\sigma _0}(y)\)，整数 \(y=1\) 时 \(b_0(1)=0\)。
取
\[
 c_* =e^{-1-h}.
 \tag{28}
\]
在 \(x\le Z_j\) 上，每个早块的 \(\mathcal R(x)/x^\beta\) 至多
\(C_{\rm early}B_k^0\)，晚块至多
\(K e^{\beta(1+h)}\|\phi\|_\infty B_k^0\)。
由(2)，\(\lambda_*u-\omega(u)\) 最终严格递增，且
\(B_{j-1}^0/B_j^0\to0\)。
故对固定 \(K\) 和充分大的 \(j\)，在当前晚块尚未开始的全部前缀
\(1\le x\le c_*Z_j\)，(20)给
\[
 |E_\lambda(x)|\le(C_{\rm early}+3)B_j^0x^\beta .
 \tag{29}
\]
常数3吸收全部旧块与 \(\epsilon\)。这里“充分大”允许依赖一次选定的 \(K\)，
并没有让 \(K\) 随 \(j\) 增长。

对任意 \(y\le c_*Z_j\)，精确分部积分为
\[
 A_{\sigma _0}(y)
  =w_y(y)E_\lambda(y)+
       \int_1^y E_\lambda(x)(-w_y'(x))dx,\qquad
 w_y(x)=x^{-\sigma _0}e^{-x/y}.
 \tag{30}
\]
利用 \(-w_y'(x)\le(\sigma _0+1)x^{-\sigma _0-1}\)，(29)蕴含
\[
 |b_0(y)|\le C_{\rm pre}B_j^0
                     \quad(1\le y\le c_*Z_j).
 \tag{31}
\]
所有原子完整，\(E_\lambda(1)=0\)，所以没有下端常数遗漏。

在 \(y=Z_j\)，连续模型的当前晚块净质量恰为
\[
 \int_1^{Z_j}w_{Z_j}(x)\,
       d\{K D_j\phi(\log x-(2U_j-1))\}
   =K c_\phi B_j^0 Z_j^d .
 \tag{32}
\]
因 \(\mathcal R\ge0\)，每个已经完整包含的块对递减权的净质量均非负。
由(23)，因此
\[
 b_0(Z_j)\ge K c_\phi B_j^0-O(Z_j^{-d})
                   >3C_{\rm pre}B_j^0
 \tag{33}
\]
于充分大 \(j\) 成立。

现在在有限集合 \(1\le n\le Z_j\) 上取 \(|b_0(n)|\) 的任一最大者 \(N_j\)，
并令 \(Y_j=N_j\)。由(31)--(33)，\(N_j>c_*Z_j\)。
在任意整数 cutoff \(y\)，连续模型还有
\[
 \int_1^y w_y\,d\mathcal R
       =w_y(y)\mathcal R(y)+\int_1^y(-w_y')\mathcal R\ge0 .
 \tag{34}
\]
(23)故使 \(A_{\sigma _0}(y)\ge-O(1)\)。最大者的绝对值趋于无穷，
不可能由负值取得，故 \(M_j=A_{\sigma _0}(N_j)>0\)。
这样得到(6)，且 \(Y_j\to\infty\)；事实上相邻区间
\([c_*Z_j,Z_j]\) 最终互不相交。

在全部 \(x\le Z_j\) 上，同一块估计给
\(|E_\lambda(x)|\le C_K B_j^0x^\beta\)。
再次应用(30)得
\[
 c B_j^0\le B_j=N_j^{-d}M_j\le C_K B_j^0 .
 \tag{35}
\]
因为 \(L_j=2U_j+O(1)\)，(35)给
\[
 \log\frac{M_j}{Y_j^{1/2-\sigma _0}}
       =\beta U_j-\omega(U_j)+O(1)\longrightarrow\infty
       \quad\hbox{以线性于 \(U_j\) 的速率}.
 \tag{36}
\]
三重对数因子不会改变此结论，证明(7)的强质量。

最后，对固定 Abel 参数 \(Y_j\) 和任意 \(1\le x\le Y_j\)，
把(30)中的 \(w_y\) 换成 \(w_{Y_j}\)，同样得到
\[
 |H_j(\log x)|\le C_K B_j^0x^d
      \le C M_j(x/Y_j)^d .
 \tag{37}
\]
这证明(8)及其两个范数界。又
\(\psi_\lambda(n)-n=E_\lambda(n)-1\)，故有定理中的 \(P_{\beta,\lambda}\) guard。
本证明没有借用实际 \(\Lambda\) 的振荡，也没有把无界搜索当作有效数值算法。

## 5. 同一记录上，右侧负迹确实达到交点尺度

### 5.1 实际质量定义的交点与构造尺度相容

由(2)，函数 \(F(u)=\lambda_*u-\omega(u)\) 在充分大区域有
\(F'(u)\ge\lambda_*/2>0\)，且趋于无穷。
因而(10)的充分大根唯一。由(35)，
\[
 F(V_j)-F(U_j)=\log(B_j/B_j^0)=O(1),
 \qquad V_j=U_j+O(1).
 \tag{38}
\]
这里的 \(O(1)\) 与 \(\sigma'\) 无关。由 \(b\) 位于固定紧正区间，得到
\[
 T_j(\sigma')\asymp B_j^0e^{-bU_j}
                  =Q_j(\sigma') .
 \tag{39}
\]
不能先用构造中的 \(B_j^0\) 替代实际 \(M_jY_j^{-d}\) 而省略(38)。

### 5.2 小而固定的频率窗口已经给双侧下界

当前早块在所有 \(Y_j\in[c_*Z_j,Z_j]\) 之前完整包含。
代入 \(x=X_je^v\)，它的连续右移符号为
\[
 Q_j(\sigma')\,
 \Re\left[
 e^{itU_j}\int e^{(-\sigma'+it)v}
       e^{-X_je^v/Y_j}\phi'(v)\,dv
 \right].
 \tag{40}
\]
定义
\[
 Q_{\sigma'}(t)=\int e^{(-\sigma'+it)v}\phi'(v)\,dv,\qquad
 Q_{\sigma'}(0)=\sigma'\int e^{-\sigma'v}\phi(v)\,dv>0 .
 \tag{41}
\]
\(\sigma'\in[1/2,3/4]\) 上后者有统一正下界，且 \(Q_{\sigma'}'\) 在有界
\(t\) 区间统一有界。可固定 \(t_0>0\)，使
\[
 |Q_{\sigma'}(t)-Q_{\sigma'}(0)|
        \le Q_{\sigma'}(0)/8
                  \quad(|t|\le t_0)
 \tag{42}
\]
对全部该 \(\sigma'\) 成立。
因 \(X_j/Y_j=O(X_j^{-1})\)，(40)把 Abel 因子替换成1的误差为
\(O(Q_j/X_j)\)，一致于全部实 \(t\)。

当前晚块即便被所选 \(N_j\) 部分截断，其加权总变差仍为
\[
 O_K(D_j Z_j^{-\sigma'})
    =O_K\!\left(Q_j(\sigma')e^{-(\sigma'-\beta)U_j}\right)
    =o(Q_j(\sigma')) .
 \tag{43}
\]
这里没有用“晚块已完整”代替部分 cutoff；总变差界直接覆盖两种情形。
全部旧块由(25)--(27)为 \(o(Q_j)\)，离散化在固定窗口由(24)为 \(O(1)\)。
又 \(\inf_{\sigma'}Q_j\to\infty\)，所以真实整数源满足
\[
 P_{\sigma',j}(t)=Q_j(\sigma')
      \Re(e^{itU_j}Q_{\sigma'}(t))+o(Q_j(\sigma'))
               \quad(|t|\le t_0),
 \tag{44}
\]
其误差对 \(t,\sigma'\) 一致。

对两个符号，\([-t_0,t_0]\) 内
\(\cos(U_jt)\ge1/2\) 和 \(\cos(U_jt)\le-1/2\) 的集合均占固定正长度；
删去至多两个不完整周期即可直接证明。
结合(41)--(44)，每个集合分别提供至少 \(cQ_j\) 的正井或负井。
Cauchy 密度在该固定窗口有统一正下界，故
\[
 \tau_C((P_{\sigma',j})_\pm)\ge cQ_j(\sigma')
                           \asymp T_j(\sigma').
 \tag{45}
\]
这是真实实部的积分下界，不是单一复 Fourier 峰或有限采样。

### 5.3 全轴上界不积分 \(O(1+|t|)\) 误差

由(5)、(37)，可以直接使用
[294](294-pnt-envelope-gain-and-fixed-source-saturation.md)
的匹配 PNT 前缀／历史交点分析。为使一般 \(\omega\) 的适用性在本篇自足，
所需的一般化只列明如下。

因 \(\omega'=o(1)\)，对 \(A\) 位于固定正紧区间，充分大 \(u\) 有
\((Au-\omega(u))'\ge A/2\)。固定低区间的积分可由常数控制，因此
\[
 \int_0^U e^{p(ru-\omega(u))}du
       \le C e^{p(rU-\omega(U))}\quad(p=1,2)
 \tag{46}
\]
对充分大 \(U\) 一致于 \(r=1-\sigma'\in[1/4,1/2]\)。
对固定低段的吸收合法，因为
\(rU-\omega(U)\ge U/4-o(U)\to\infty\) 一致成立。
同一论证与完整 Stieltjes 公式先给
\[
 |H_j(u)|\le C e^{(1-\sigma _0)u-\omega(u)}
                  \quad(0\le u\le L_j),
 \tag{47}
\]
其中固定低段也吸收到有限常数；(5)中的 \(\omega\) 不变。
将其与(8)相交，得到
\[
 |e^{-au}H_j(u)|
  \le C\min\{e^{ru-\omega(u)},B_je^{-bu}\},\qquad a=\sigma'-\sigma _0 .
 \tag{48}
\]
在充分大根 \(V_j\) 左侧，最终第一项较小；固定低区间亦如此，因为
\(B_j\to\infty\)。右侧则第二项较小。
由(46)及指数尾，(48)的一、二次范数和上确界均为 \(O(T_j)\)。
固定小区间的贡献仍由 \(T_j\to\infty\) 吸收，不能默认包络在零点附近递增。
端点 \(|M_j|e^{-aL_j}\) 就是该路径在 \(L_j\) 的绝对值，同样被控制，
不需假设 \(V_j\le L_j\)。

最后应用293的完整端点公式及其全轴 Plancherel 界
\[
 \tau_C|P_{\sigma',j}|
   \le M_je^{-aL_j}
       +a\|e^{-a\cdot}H_j\|_1
       +\|e^{-a\cdot}H_j\|_2/\sqrt2
   \ll T_j .
 \tag{49}
\]
这覆盖整个频轴。结合(45)和(39)，证明(12)。

当 \(\omega(u)=c\sqrt u\) 时，(10)中恰是294-C的较大根
\[
 V_j=\left[
    \frac{c+\sqrt{c^2+4\lambda_*\log B_j}}{2\lambda_*}
       \right]^2 .
 \tag{50}
\]
所以294给出的 \(B^\theta\) 乘根指数节省可以被一个固定正整数源同阶达到。
更一般，本篇饱和的是明确给定的光滑次幂包络；不排除使用比(5)更强的
独立算术信息继续节省。

## 6. 有限 Poisson／Euler 开集接口确实一致

定义 \(D_\lambda(s)=\sum_{n\ge2}\lambda(n)n^{-s}\)，在 \(\Re s>1\) 绝对收敛。
由 \(\lambda(n)\le3/2\)，同一匹配有限候选
\[
 F^\sharp_{\lambda,Y}(z)
   =G(s)+\int_1^Yx^{-s}e^{-x/Y}dx
           -\sum_{n\le Y}\lambda(n)n^{-s}e^{-n/Y},
 \quad s=1/2+z ,
 \tag{51}
\]
其中 \(G(s)=1/s-\tfrac12\log\pi+\tfrac12\psi(s/2)\)，在右半平面全纯、
real-type。其有限部分是同一固定源的 Laplace 变换。
有限总变差给精确 Poisson 右移；加入 \(G\) 后，293-E的大半圆最小值证明
逐字适用，给相同的 Poisson admissibility。
这里不需要任何未知零点或随尺度更换的源。

在 Euler 开集 \(\Re s>1\)，有限和及积分局部一致收敛，故
\[
 F^\sharp_{\lambda,Y}(z)\longrightarrow
     G(s)+\frac1{s-1}-D_\lambda(s).
 \tag{52}
\]
这只是一条明确的 Euler 开集 germ；不是声称它等于真实 \(\xi'/\xi\)。
对 \(\sigma'\in[1/2,3/4]\)，293的 Gamma 估计和 Cauchy 均值恒等式还给
\[
 \tau_C|g_{\sigma'}|=O(1),\qquad
 \tau_C(P_{\sigma',j})
  =\sum_{n\le Y_j}\lambda(n)n^{-1-\sigma'}e^{-n/Y_j}
       -\int_1^{Y_j}x^{-1-\sigma'}e^{-x/Y_j}dx=O(1).
 \tag{53}
\]
因此
\[
 \tau_C((g_{\sigma'}-P_{\sigma',j})_-)
     =\tfrac12\tau_C|P_{\sigma',j}|+O(1)
     \asymp T_j(\sigma') .
 \tag{54}
\]
此处的 \(O(1)\) 对全部 \(\sigma'\) 一致，故右移日程可趋近 \(1/2\)。
没有将 Gamma 从非线性响应或 Gram 中删除。

## 7. 实际 zeta 已有而本模型缺失的解析性质 [N]

本模型不仅没有证明全局亚纯除数；下面直接核验(52)在 \(s=1\) 非亚纯。
这是适用边界，不把模型伪装成新的 \(L\) 函数。

令
\[
 f(u)=e^{-u}\mathcal R(e^u)\ge0,\qquad
 \mathcal L_f(q)=\int_0^\infty f(u)e^{-qu}du\quad(\Re q>0).
 \tag{55}
\]
由(5)的连续模型版本，\(f(u)\to0\)，且有界。
每个早块在 \(u=U_j+v\)、\(v\in(-h,h)\) 的贡献恰为
\(e^{-\omega(U_j)}e^{-v}\phi(v)\)。
所以对任意 \(\varepsilon>0\)，
\[
 \int_0^\infty e^{\varepsilon u}f(u)du=\infty ,
 \tag{56}
\]
因为各早块的正积分是正固定常数倍
\(e^{\varepsilon U_j-\omega(U_j)}\to\infty\)。
同时，对实 \(q\downarrow0\)，有
\[
 q\mathcal L_f(q)\longrightarrow0 .
 \tag{57}
\]
证明只需先截固定前缀，再用 \(f\) 的尾部上确界趋零。

若 \(\mathcal L_f\) 在0亚纯，(57)排除任何非零整数阶极点，故它应全纯。
此时对每个整数 \(k\ge0\)，从 \(q>0\) 的导数公式及正项单调收敛得
\[
 (-1)^k\mathcal L_f^{(k)}(0)
                 =\int_0^\infty u^k f(u)du<\infty .
 \tag{58}
\]
在一个半径 \(r>0\) 的解析圆盘上，Cauchy 估计给这些矩除以 \(k!\)
不超过 \(C r^{-k}\)。对任意 \(0<\varepsilon<r\) 用正项 Tonelli 求和，
便得到 \(\int e^{\varepsilon u}f(u)du<\infty\)，与(56)矛盾。
所以 \(\mathcal L_f\) 在0非亚纯；这一论证不引用未验证的谱假设。

另一方面，(19)中的 \(\epsilon\) 有界，故
\[
 J_\epsilon(s)=s\int_1^\infty \epsilon(x)x^{-s-1}dx
       \quad\hbox{在 }\Re s>0\hbox{ 全纯}.
 \tag{59}
\]
在 \(\Re s>1\) 对(20)分部积分，有精确恒等式
\[
 D_\lambda(s)=\frac1{s-1}
                +s\mathcal L_f(s-1)+J_\epsilon(s).
 \tag{60}
\]
因此(52)等于
\(G(s)-s\mathcal L_f(s-1)-J_\epsilon(s)\)，在 \(s=1\) 非亚纯。
主项 \(1/(s-1)\) 已精确抵消；非亚纯性不是遗漏连续极点造成的。

真实 \(\zeta'/\zeta\) 的亚纯延拓已独立排除此模型。
因此(12)不能升级成“亚纯 completed divisor 也无法改善上界”的结论；
更不能升级为整个 Weil 结构、所有选择原理或实际 RH 的障碍。

## 8. 与旧模型的区别和停止条件

| 保留的输入 | 本篇的核验 | 没有获得的额外结构 |
|---|---|---|
| 固定正整数源、所有有限截断一致 | (16)--(20)、(51)--(52) | 真实素数幂支撑、Euler 乘积 |
| 任意给定的平滑次幂 PNT 包络 | (21)--(22)，相同 \(\omega\) | 真实 \(\Lambda\) 的局部相关与更强算术抵消 |
| 真正整数归一化 Abel 前缀记录 | (31)--(38)，固定 \(K\) 后选点 | 实际 \(\Lambda\) 的284输出、所有共尾点失败 |
| 同一历史 guard 与原始迹 | (37)、(45)、(49) | 把归一化矩当成绝对有界迹 |
| 有限完成项及 Poisson／Euler germ | (51)--(54) | 全局亚纯、整数除数、函数方程 |
| 新鲜未中心化右侧目标 | (9)、(12) | 旧固定左侧四阶响应的自动迁移 |

278已有固定正整数源及中频四阶包络障碍；本篇不重新登记其拼接、
整数化或“固定源”思想。本篇不同的可证伪结论是：在真正前缀记录和
原右侧 Cauchy 迹上，294的 PNT／历史交点上界可达到同阶。
278的平方根级误差更强，但其目标是另一中频四阶量，不能互相替换。
288的有限 Euler 多项式正性障碍没有应用到本模型；
290使用离散极点背景，本篇始终使用数域风格的连续 \(dx\) 背景。
这些模型的不同公理不能拼在一起，冒充同一个反例具有全部结构。

下一最小输入若只重复固定源一致性、PNT 包络、前缀记录及历史 soft norm，
不能普遍改进(12)到 \(o(T_j)\)。可继续的输入必须使用模型未保留的
算术或解析限制，并对实际 \(\Lambda\) 给出独立有符号估计。
本篇不排除选取另一条模型子序列成功，也不排除由更多已知算术信息改善界。
文献新颖性、发表价值、外部同行审查和 Goal 阶段验收仍未完成。
没有新增实验；所有全尺度断言来自上述证明，不来自有限采样。

## 9. 完整证明的独立内部复核

gap_exception_audit写出正文并自审；主代理、carrier_audit、
midband_compute各自完整读取落盘证明并逆向核算，均PASS。
复核覆盖固定 \(K\) 后的真正前缀选点、所有旧块总变差、部分晚块截断、
两种迹的实部下界、全 \(\sigma'\) 统一性、全轴上界和非亚纯germ的完整证明。
审稿期间补清了 \(\lambda(1)=0\)，并将(34)前调用离散化的cutoff明确限定为整数。
这些文字修正已落盘后再经核对；没有将固定窗误差积到无限频轴。
两篇笔记和仓库检查的共同记录见294第5节。
内部复核不证明文献新颖性，不替代外部同行审查，也不构成RH/GRH的阶段验收。
