# 289. 增长阶 resolvent 端点展开与多对数谱局部化

日期：2026-09-06。主线：NCE-8 / B1z；论文归属：Vaughan--Brownian response。

状态：[T/R] 实际 zeta 的增长阶展开、完整谱端点的历史控制，以及同一284
记录序列上的有限深右谱归约；[O] 新有限核的真实有符号四阶预算。
本篇不假设 RH，不使用零密度定理，也不证明 RH、零点比例或完整 Weil 正性。
外部输入仅为282、285已经核验的显式公式与单位高度零点计数。

这里的进展不是把287中的原核直接截到更低高度：先对**全部零点**作增长阶
分部积分，将完整谱共同端点方向独立控制，再对新的余项核进行谱截断。
原 prime、continuum 正通道及其归一化分母始终不变。

## 1. 同一记录序列与主结论

固定 \(0<\sigma<\beta<1/2\)，令
\[
 \delta=\beta-\sigma>0,\qquad d=1/2-\sigma>0,
 \qquad L=\log Y,\qquad
 \ell(Y)=\max(1,\log\log\log Y).
 \tag{1}
\]
沿[284](284-causal-abel-inverse-and-diagonal-record-selection.md)已经构造的
同一整数对角共尾序列 \(N=Y\)，有
\[
 |M|\ge c_*Y^d\ell(Y),\qquad
 P_\beta(N)N^\delta\le C_*|M|,
 \qquad
 P_\beta(N)=\max_{1\le n\le N}\frac{|R(n)|}{n^\beta}\ge1.
 \tag{2}
\]
其中 \(R(x)=\psi(x)-x\) 右连续，所有整数 cutoff 原子取完整权。
下面有限配置的解析恒等式也适用于 \(Y\le N\le2Y\)，但相对结论明确调用(2)，
不声称重新产生记录、得到 dyadic 记录，或输出275原算法。

仍令
\[
 w_Y(x)=x^{-\sigma}e^{-x/Y},\qquad
 f_\xi(x)=w_Y(x)(\cos(\xi\log x)-1),
\]
\[
 M=\sum_{2\le n\le N}\Lambda(n)w_Y(n)-\int_1^Nw_Y(x)\,dx,
\]
\[
 \widehat r(\xi)=\sum_{2\le n\le N}\Lambda(n)f_\xi(n)
                     -\int_1^Nf_\xi(x)\,dx,
 \qquad
 Q_E(v)=\frac1{2\pi}\int_E\frac{|v(\xi)|^4}{\xi^2}\,d\xi.
 \tag{3}
\]
\(Q_E(r)\) 表示把 \(v=\widehat r\) 代入；其他谱函数直接作为 \(v\) 使用。
\(f_\xi\) 中的 \(-1\) 保留完整中心化质量 \(-M\)。

固定 \(A>1/2\) 和 \(0<a<3/8\)，置
\[
 U=\sqrt L,\qquad T=L^A,\qquad
 E=\{\xi:U\le|\xi|\le T\},\qquad
 \theta_Y=\frac12+\frac{a\log L}{L},
\]
\[
 m=\lceil L\rceil,\qquad h=mT,\qquad V=4h.
 \tag{4}
\]
全部断言均在 \(Y\) 充分大时使用，因此 \(m\ge1\)、\(h\ge1\)、
\(\theta_Y\in[1/2,3/4]\)。常数可依赖固定的
\(\sigma,\beta,A,a,c_*,C_*\)，但不依赖 \(Y,N,m,h,\xi\)。

令 \(u_0=\log2\)、\(Z=\log N\)、\(D_u=d/du\)，并定义
\[
 \mathcal A_\xi(u)=
 -e^{-e^u/Y}\big\{(\sigma+e^u/Y)(\cos(\xi u)-1)
                                  +\xi\sin(\xi u)\big\}.
 \tag{5}
\]
对每个实际非平凡零点 \(\rho=b+i\gamma\)，记 \(s_\rho=\rho-\sigma\)，
定义新的余项核
\[
 \mathcal R_\rho^{(m,h)}(\xi)
 =\frac{(-1)^m}{\rho(s_\rho+h)^m}
   \int_{u_0}^{Z}e^{s_\rho u}(D_u-h)^m\mathcal A_\xi(u)\,du.
 \tag{6}
\]
最后只保留有限的实际深右零点：
\[
 \mathcal K_Y(\xi)=
 \sum_{\substack{\Re\rho>\theta_Y\\|\Im\rho|\le V}}
                        \mathcal R_\rho^{(m,h)}(\xi).
 \tag{7}
\]
重数、系数和相位均保留原值；集合共轭封闭，故 \(\mathcal K_Y(\xi)\) 为实数。
未假设其中有零点，也未假设其中没有零点。

### 定理289-A [T/R]

沿(2)，有
\[
 \frac{Q_E(\widehat r-\mathcal K_Y)}{M^4L}
 \ll
 L^{-3/2}
 +\frac{L^{4a-3/2}(\log L)^8}{\ell(Y)^4}
 +\frac{Y^{2-4\log4}L^{3A-1}(\log L)^4}{\ell(Y)^4}
 =O(\ell(Y)^{-4}).
 \tag{8}
\]
特别，正确的四次方根比较为
\[
 \boxed{\quad
 \frac{|Q_E(r)^{1/4}-Q_E(\mathcal K_Y)^{1/4}|}
      {|M|L^{1/4}}
 =O(\ell(Y)^{-1})=o(1).
 \quad}
 \tag{9}
\]
所以在该物理带上
\[
 Q_E(r)=O(M^4L)\quad\Longleftrightarrow\quad
 Q_E(\mathcal K_Y)=O(M^4L).
 \tag{10}
\]
这是实际算术归约，不是已经证明右侧预算。特别，(8)不是
\(Q_E(r)=Q_E(\mathcal K_Y)+o(M^4L)\) 的能量加性声明。

## 2. 固定参数的精确全谱恒等式 [T/R]

沿用[282](282-rh-conditional-endpoint-preserving-response-bound.md)和
[285](285-shallow-zero-deletion-and-finite-deep-response.md)的记号
\[
 C_\zeta=\frac{\zeta'(0)}{\zeta(0)},\qquad
 T_0(x)=-\frac12\log(1-x^{-2}).
 \tag{11}
\]
外部输入为作者公开书稿
[Kedlaya，第9章，Lemma9.4 与 Theorem9.9](https://kskedlaya.org/ant/chap-von-mangoldt.html)：
半权显式公式及单位高度零点计数。282已完整给出固定 \(Y,N,\xi\) 时，
先在普通积分中令截断高度趋于无穷的支配收敛证明；本篇不在原子端点使用
条件收敛的原始零点和。标准临界带 \(0<b<1\) 和
\(|\rho|^{-1}\ll(1+|\gamma|)^{-1}\) 也保持不变。

由285的精确端点拆分，
\[
 \widehat r(\xi)=E_N(\xi)+B_{Y,N}(\xi)+\sum_\rho I_\rho(\xi),
 \tag{12}
\]
\[
 E_N(\xi)=f_\xi(N)R(N),\qquad
 I_\rho(\xi)=\frac1\rho\int_2^Nx^\rho f'_\xi(x)\,dx
            =\frac1\rho\int_{u_0}^{Z}e^{s_\rho u}\mathcal A_\xi(u)\,du,
 \tag{13}
\]
其中完整固定早段为
\[
 \begin{split}
 B_{Y,N}(\xi)={}&\Lambda(2)f_\xi(2)-\int_1^2f_\xi(x)\,dx-f_\xi(2)R(2)\\
 &+C_\zeta(f_\xi(N)-f_\xi(2))
                    -\int_2^NT_0(x)f'_\xi(x)\,dx .
 \end{split}
 \tag{14}
\]
因为 \(T'_0(x)=-1/[x(x^2-1)]\)，最后的积分再次分部积分后是统一的
\(O_\sigma(1)\)。因此
\[
 |B_{Y,N}(\xi)|\ll_\sigma1,\qquad
 |E_N(\xi)|\le2w_Y(N)|R(N)|\ll|M|.
 \tag{15}
\]
\(N\) 的完整原子没有改成半权；\(n=2\) 只在(14)出现一次。
积分后的 \(\sum I_\rho\) 对每个固定频率绝对收敛，282的 \(\vartheta=1\)
majorant 版本即可保证这一点，不假设 RH。

对任意有限整数 \(m\ge1\)、\(h\ge1\)，逐次分部积分精确给
\[
 I_\rho(\xi)
 =\sum_{j=0}^{m-1}\frac{(-1)^j}{\rho(s_\rho+h)^{j+1}}
       [e^{s_\rho u}(D_u-h)^j\mathcal A_\xi(u)]_{u_0}^{Z}
       +\mathcal R_\rho^{(m,h)}(\xi).
 \tag{16}
\]
这是对 \(e^{(s_\rho+h)u}\) 与 \(e^{-hu}\mathcal A_\xi(u)\) 作分部积分，
不是把 \(s_\rho\) 的实部换成中心线。令
\[
 C_{j,h}(x)=\sum_\rho
       \frac{x^{s_\rho}}{\rho(s_\rho+h)^{j+1}},\qquad j\ge0,
\]
\[
 \mathcal E_{m,h}(\xi)=
 \sum_{j=0}^{m-1}(-1)^j
       [(D_u-h)^j\mathcal A_\xi(u)\,C_{j,h}(e^u)]_{u_0}^{Z}.
 \tag{17}
\]
每个 \(C_{j,h}\) 都绝对收敛。对每个固定 \(Y,N,m,h,\xi\)，余项在
大 \(|\gamma|\) 处有 \(O(|\gamma|^{-m-1})\) majorant，故也可绝对求和。
因此(16)可求和为
\[
 \sum_\rho I_\rho=\mathcal E_{m,h}+\sum_\rho\mathcal R_\rho^{(m,h)}.
 \tag{18}
\]
随后才使用(4)中随 \(Y\) 增长的 \(m,h\)；没有把一个不一致的极限交换
当作新的算术估计。

## 3. 全谱 resolvent 系数的历史控制，含全部下端初值 [T/R]

### 引理289-B：统一于阶数的因果积分公式

令 \(\tau=\log(N/2)\)。对全部整数 \(j\ge0\)，有
\[
 \begin{split}
 C_{j,h}(N)={}&e^{-h\tau}
       \sum_{k=0}^{j}\frac{\tau^k}{k!}C_{j-k,h}(2)\\
 &-\frac1{j!}\int_0^\tau e^{-ht}t^j(Ne^{-t})^{-\sigma}
       [R(Ne^{-t})+C_\zeta-T_0(Ne^{-t})]\,dt .
 \end{split}
 \tag{19}
\]
这里普通积分中的半权与右连续 \(R\) 几乎处处相同；不在积分端点将
\(\sum x^\rho/\rho\) 认作绝对收敛值。

证明。把有限高度显式公式乘以 \(x^{h-\sigma-1}\)，在固定 \([2,N]\)
积分并按282的顺序取极限，得
\[
 (D_{\log x}+h)C_{0,h}(x)
       =-x^{-\sigma}[R(x)+C_\zeta-T_0(x)]
 \quad\text{几乎处处}.
 \tag{20}
\]
也可先写(20)的积分形式，从而完全避免逐点求导原零点级数。
对 \(j\ge1\)，一阶导数级数在每个固定的紧 \(x\) 区间上局部一致绝对收敛：
其大 \(|\gamma|\) 项为 \(O(|\gamma|^{-j-1})\)，单位高度计数足以求和。
因此允许逐项求导，并给
\((D_{\log x}+h)C_{j,h}=C_{j-1,h}\)。逐次使用一阶变参数公式即(19)。
有限阶因果卷积产生的系数恰为 \(t^j/j!\)，不能在增长阶数时丢掉这个阶乘。
\(\square\)

下面所有估计的常数都不依赖 \(j\)。在整数历史与实变量之间，
\[
 |R(x)|\le P_\beta(N)x^\beta+1
                  \le2P_\beta(N)x^\beta\qquad(2\le x\le N),
 \tag{21}
\]
因为同一整数 cell 内 \(R(x)=R(\lfloor x\rfloor)-(x-\lfloor x\rfloor)\)。
\(C_\zeta,T_0\) 在本积分区间有界，故(19)的积分部分满足
\[
 \begin{split}
 \left|\frac1{j!}\int_0^\tau\cdots\,dt\right|
 &\le \frac{C P_\beta(N)N^\delta}{j!}
                   \int_0^\infty e^{-(h+\delta)t}t^j\,dt\\
 &=\frac{C P_\beta(N)N^\delta}{(h+\delta)^{j+1}}
 \le\frac{C|M|}{(h+\delta)^{j+1}}.
 \end{split}
 \tag{22}
\]

还必须估计(19)第一行。单位高度计数直接给
\[
 \sum_\rho\frac{2^{b-\sigma}}{|\rho|\,|s_\rho+h|}
                 \ll\frac{\log^2(2h)}h.
 \tag{23}
\]
事实上，\(|\gamma|\le h\) 部分用 \(|s_\rho+h|\ge h-\sigma\asymp h\)
和调和和；\(|\gamma|>h\) 部分用平方倒数尾。每个额外分母均至少
\(h-\sigma\)，所以对**所有**整数 \(r\ge0\)，
\[
 |C_{r,h}(2)|\le
      \frac{C\log^2(2h)}{(h-\sigma)^{r+1}}.
 \tag{24}
\]
这不是带一个未经控制的 \(O_r\) 常数的估计。

记(19)第一行为 \(B_{j,h}(N)\)。由(24)，对 \(j<m\)，
\[
 h^j|B_{j,h}(N)|
 \le\frac{C\log^2(2h)}h
       \left(\frac h{h-\sigma}\right)^{j+1}
       e^{-h\tau}\sum_{k=0}^{j}\frac{((h-\sigma)\tau)^k}{k!}.
 \tag{25}
\]
在(4)下，\(m/h=1/T\to0\)，且 \(\tau=L+O(1)\)。因此
\[
 \left(\frac h{h-\sigma}\right)^m\le e^{O(m/h)}=O(1),
\]
\[
 e^{-h\tau}\sum_{k=0}^{m}\frac{(h\tau)^k}{k!}
 \le\exp\{-h\tau+\log(m+1)+m\log(h\tau)\}
 \le e^{-h\tau/2}.
 \tag{26}
\]
最后一步使用 \(h\tau\asymp L^{A+2}\)，而
\(m\log(h\tau)=O_A(L\log L)\)。完整下端初值因此有明确的一致小量，
并未在令 \(m\) 增长时静默省略。

## 4. 增长阶导数与完整端点方向的删除 [T]

### 引理289-C：\(h=mT\) 下无阶数损失的导数界

对 \(1\le q=|\xi|\le T\)、\(0\le j\le m\)，有
\[
 \sup_{u_0\le u\le Z}|(D_u-h)^j\mathcal A_\xi(u)|
                           \le C qh^j,
 \tag{27}
\]
其中 \(C\) 与 \(m,j,h,Y,N,q\) 无关。

证明。写
\[
 B_0(u)=e^{-e^u/Y},\qquad B_1(u)=(\sigma+e^u/Y)B_0(u).
 \tag{28}
\]
\(\mathcal A_\xi\) 是 \(B_1\)、\(B_1e^{\pm i\xi u}\)、
\(\xi B_0e^{\pm i\xi u}\) 的固定线性组合。
对中心在 \([u_0,Z]\) 的复圆盘取固定半径 \(r_0=1/4\)。因
\(e^u/Y\le2\)，两个 \(B\) 在所有这些圆盘上一致有界，Cauchy 估计给
\[
 |B^{(k)}(u)|\le C k!r_0^{-k}\qquad(k\ge0),
 \tag{29}
\]
常数与 \(k,Y,N\) 无关。对 \(\varepsilon=0,\pm1\)，置
\(H_\varepsilon=|-h+i\varepsilon\xi|\ge h\)。Leibniz 展开给
\[
 \begin{split}
 |(D_u-h)^j(Be^{i\varepsilon\xi u})|
 &\le C H_\varepsilon^j
       \sum_{k=0}^j\frac{j!}{(j-k)!}(r_0H_\varepsilon)^{-k}\\
 &\le C H_\varepsilon^j
       \sum_{k=0}^j\left(\frac{j}{r_0H_\varepsilon}\right)^k
 \le 2C H_\varepsilon^j .
 \end{split}
 \tag{30}
\]
这里 \(j/(r_0H_\varepsilon)\le1/(r_0T)\le1/2\) 对大 \(Y\) 成立。
同时
\[
 H_\varepsilon^j\le h^j
       \exp\left(\frac{j q^2}{2h^2}\right)
       \le e h^j,
 \tag{31}
\]
因为 \(j\le m\)、\(q\le T\)、\(h=mT\)。合并得到(27)。
若改用 \(h\asymp T\) 而仍令 \(m\asymp L\)，(30)--(31)就不能提供这个
一致界；因此不能把两种平移尺度混用。\(\square\)

由(22)、(27)，完整上端历史部分满足
\[
 \sum_{j=0}^{m-1}Cqh^j\frac{|M|}{(h+\delta)^{j+1}}
              \le C|M|\frac{mq}{h}=C|M|\frac qT.
 \tag{32}
\]
由(25)--(27)，上端传播初值的贡献至多
\[
 C\frac{mq}{h}\log^2(2h)e^{O(m/h)}e^{-h\tau/2}.
 \tag{33}
\]
而实际下端 \(u_0\) 的全部端点项由(24)、(27)给
\[
 C\frac{mq}{h}\log^2(2h)e^{O(m/h)}.
 \tag{34}
\]
沿(2)，\(|M|\gg Y^d\ell(Y)\) 足以吸收 \(\log^2(2h)=O_A((\log L)^2)\)。
所以完整端点函数满足
\[
 \boxed{\quad |\mathcal E_{m,h}(\xi)|\le C|M|\frac qT\le C|M|
                  \qquad(\xi\in E).\quad}
 \tag{35}
\]
特别，连同(15)，
\[
 \frac{Q_E(E_N+B_{Y,N}+\mathcal E_{m,h})}{M^4L}
                         \ll\frac1{LU}=L^{-3/2}.
 \tag{36}
\]
这里先求和全部零点再使用历史 guard。没有声称硬截去低零点后，每个
\(C_{j,h,|\gamma|>2T}\) 仍满足(22)。这种硬截谱推论并非本证明所需。

## 5. 新余项的高谱尾：只用零点计数 [T/R]

对全部零点 \(0<b<1\)，由(27)及 \(u\ge\log2>0\)，
\[
 \int_{u_0}^{Z}e^{(b-\sigma)u}
       |(D_u-h)^m\mathcal A_\xi(u)|\,du
 \le C qh^m\int_{u_0}^{Z}e^{(1-\sigma)u}\,du
 \le C qh^mY^{1-\sigma}.
 \tag{37}
\]
因 \(|\rho|\ge|\gamma|\)、\(|s_\rho+h|\ge|\gamma|\)，当 \(|\gamma|>V\) 时
\[
 |\mathcal R_\rho^{(m,h)}(\xi)|
                \le CqY^{1-\sigma}h^m|\gamma|^{-m-1}.
 \tag{38}
\]

为了避免引入不必要的随 \(m\) 精细常数，只使用安全的统一尾和
\[
 \sum_{|\gamma|>V}|\gamma|^{-m-1}
                         \le C\log(2V)V^{-m}
 \qquad(m\ge1,\ V\ge2).
 \tag{39}
\]
证明：单位高度计数给 \(N_{\rm abs}(t)\ll t\log(2t)\)。Stieltjes 分部积分
并丢掉非正下端项后，左侧至多
\[
 C(m+1)\int_V^\infty t^{-m-1}\log(2t)\,dt
 =C(m+1)V^{-m}
       \left(\frac{\log(2V)}m+\frac1{m^2}\right),
\]
即(39)。严格 \(>V\) 的约定与可能位于 \(V\) 的零点原子相容；无需把浮点
高度移到整数，也未使用一个未经验证的 \(1/m\) 改进。

因此对任何实际零点子集，特别对深右部分，
\[
 \left|\sum_{\substack{b>\theta_Y\\|\gamma|>V}}
            \mathcal R_\rho^{(m,h)}(\xi)\right|
 \le CqY^{1-\sigma}\left(\frac hV\right)^m\log(2V)
 =CqY^{1-\sigma}4^{-m}\log(2V).
 \tag{40}
\]
取四次幂后积分实际频率，保留 \(q\) 因子：
\[
 \frac{Q_E\left(\sum_{b>\theta_Y,\,|\gamma|>V}
                   \mathcal R_\rho^{(m,h)}\right)}{M^4L}
 \le C\frac{Y^2 4^{-4m}T^3\log^4(2V)}{\ell(Y)^4L}
 \le C\frac{Y^{2-4\log4}L^{3A-1}(\log L)^4}{\ell(Y)^4}.
 \tag{41}
\]
\(2-4\log4<0\)，所以这是独立的幂次小量。这里没有把 \(Y^b\) 换成
\(Y^{1/2}\)，没有使用零密度或零自由区域。

## 6. 新余项的全部浅层删除 [T/R]

记 \(\mathscr S_Y=\{\rho:\Re\rho\le\theta_Y\}\)，包含无限多个左半、
中心线以及浅右零点。对这个子集，(16)仍可绝对求和：
\[
 \sum_{\rho\in\mathscr S_Y}\mathcal R_\rho^{(m,h)}
     =\sum_{\rho\in\mathscr S_Y}I_\rho
                     -\mathcal E_{m,h,\mathscr S_Y}.
 \tag{42}
\]
不应直接把原核的浅层估计宣称为新核的估计；必须控制这里额外的端点项。

285已经证明，常数对 \(\theta\in[1/2,3/4]\) 统一，
\[
 \left|\sum_{b\le\theta_Y}I_\rho(\xi)\right|
       \le C Y^{\theta_Y-\sigma}\log^2(2+q)
       =C Y^dL^a\log^2(2+q).
 \tag{43}
\]
此处只对浅层零点使用明确的 \(b\le\theta_Y\) majorant，不假设所有零点
满足这个上界。

对浅层系数，直接保留绝对值，(23)--(24)同样给对全部 \(j\ge0\) 统一的
\[
 |C_{j,h,\mathscr S_Y}(N)|
       \le\frac{C Y^{\theta_Y-\sigma}\log^2(2h)}{(h-\sigma)^{j+1}},
 \qquad
 |C_{j,h,\mathscr S_Y}(2)|
       \le\frac{C\log^2(2h)}{(h-\sigma)^{j+1}}.
 \tag{44}
\]
乘以(27)并求和，利用 \((h/(h-\sigma))^m=O(1)\)，得
\[
 |\mathcal E_{m,h,\mathscr S_Y}(\xi)|
       \le C\frac qT Y^{\theta_Y-\sigma}\log^2(2h).
 \tag{45}
\]
结合(42)--(45)，在 \(E\) 上
\[
 \left|\sum_{b\le\theta_Y}\mathcal R_\rho^{(m,h)}(\xi)\right|
                         \le C Y^dL^a(\log L)^2.
 \tag{46}
\]
因此
\[
 \frac{Q_E\left(\sum_{b\le\theta_Y}\mathcal R_\rho^{(m,h)}\right)}{M^4L}
       \le C\frac{L^{4a}(\log L)^8}{\ell(Y)^4LU}
       =C\frac{L^{4a-3/2}(\log L)^8}{\ell(Y)^4}=o(1).
 \tag{47}
\]
严格条件 \(a<3/8\) 在这里使用。没有只删除固定有限个零点，也没有把
所有离线零点预先归入中心线。

## 7. 定理的合并与实际通道接口

由(12)、(18)，有精确分解
\[
 \begin{split}
 \widehat r-\mathcal K_Y={}&E_N+B_{Y,N}+\mathcal E_{m,h}\\
 &+\sum_{b\le\theta_Y}\mathcal R_\rho^{(m,h)}
 +\sum_{\substack{b>\theta_Y\\|\gamma|>V}}\mathcal R_\rho^{(m,h)}.
 \end{split}
 \tag{48}
\]
浅层的高零点只在第一谱和出现；最后一项仅为深右高尾，不重复计数。
由加权 \(L^4\) Minkowski 或有限项四次幂三角上界，(36)、(41)、(47)
给出(8)。因为 \(a<3/8\)，三项均为 \(O(\ell^{-4})\)，且各自趋于零。
再次用同一个加权 \(L^4\) 范数得到(9)，进而得到(10)。

对于[277](277-continuum-channel-coercivity-and-double-discrepancy-interface.md)
的实际正通道，继续使用原 \(p,c,S,D\)，令
\[
 \mathfrak J_E(v)=\frac1{S^4D}\frac1{2\pi}\int_E
       \frac{|v(\xi)|^4(|\widehat p(\xi)|^2+|\widehat c(\xi)|^2)}{\xi^2}
       \,d\xi .
 \tag{49}
\]
其中 \(J_{4,E}=\mathfrak J_E(\widehat r)\)。\(\mathfrak J_E(\mathcal K_Y)\)
只是把同一物理范数作用于有限谱函数，不是重新定义一个正算术源。
沿原配置，\(D\asymp S^2L\)、\(\mu=M/S\)，277给
\[
 \frac{\mathfrak J_E(v)}{\mu^4}\asymp
                  \frac{Q_E(v)}{M^4L}
 \qquad(U\longrightarrow\infty).
 \tag{50}
\]
所以原实际通道中的根误差也有
\[
 |J_{4,E}^{1/4}-\mathfrak J_E(\mathcal K_Y)^{1/4}|
                         \ll |\mu|/\ell(Y).
 \tag{51}
\]
这不要求有限谱函数本身具有非负原子，不把277的正性假设转移给零点和。
真正的正源仍是原 \(\Lambda\) 与连续背景；使用的是它们已经证明的通道界。

## 8. 最小输入、实际缩减与下一最小问题

| 输入 | 本证明中的精确作用 | 删除后不能得到的步骤 |
|---|---|---|
| 实际截断显式公式与标准临界带 [R] | (12)、(19)、(37) 保留真实符号、端点和 \(Y^{1-\sigma}\) majorant | 不能把任意正源的历史写成这些实际 zeta resolvent 系数 |
| 单位高度零点计数 [R] | (23)--(24)、(39)、(44) 的统一绝对和 | 不能保证增长阶初值、浅层和高谱尾的所需界 |
| 同一284历史 guard [T/R] | (22)、(32)、(35) 控制完整谱共同端点 | 仅有质量下界不控制整个历史；硬截谱 guard 也未由此推出 |
| 同一284强质量 [T/R] | 吸收固定早端、将(41)、(47)化为相对小量 | 不能用小误差的绝对规模自动换取 \(M^4L\) 归一化 |
| \(m=\lceil L\rceil\)、\(h=mT\)、\(V=4h\) [T] | 阶数增长产生 \(4^{-m}\)，而平移尺度确保(27)、(35)一致 | 固定阶数不提供这次幂次 saving；\(h\asymp T\)不能沿用本增长阶控制 |
| 原正通道与连续通道下界 [T/R] | (49)--(51) 回到实际 \(J_{4,E}\) | 不可把裸谱四阶直接认作任意别的正性形式 |

首带 \(A=1\) 时，新的有限谱高度为
\[
 V=4\lceil\log Y\rceil\log Y\asymp(\log Y)^2,
 \qquad
 \Re\rho>\frac12+\frac{a\log\log Y}{\log Y}.
 \tag{52}
\]
这比287原核方案的 \(Y^{1/4}(\log Y)^{5/4}\) 高度显著更小，但核已变为(6)。
必须同时保留 \(m,h\) 和全部共同端点删除证明，不能只把287的高度参数改成(52)。
[287](287-zero-density-compression-of-deep-response.md)的原核零密度方案保持有效，
作为使用不同输入的独立备份；本篇没有修改它，也没有把密度输入隐藏在新证明中。

下一最小实际输入为：[O] 沿同一284记录序列，证明首带有限有符号和满足
\[
 \boxed{\quad
 \frac1{2\pi}\int_{\sqrt L\le|\xi|\le L}
       \frac{|\mathcal K_Y(\xi)|^4}{\xi^2}\,d\xi
                       \ll M^4L,
 \quad}
 \tag{53}
\]
其中 \(\mathcal K_Y\) 是(6)--(7)、(52)指定的真实核、实际零点和实际相位。
仅计数这些有限零点、把 \(Y^b\) 替换为 \(Y^{1/2}\)，或要求新核自己对应正源，
都不能代替(53)。没有证明(53)比 RH 已知更弱或与 RH 等价。

本篇只完成固定 \(A>1/2\) 的物理多对数带归约，不将首带预算误称为全部
\(\sqrt L<|\xi|\le T_{\rm diag}\) 已闭合，更不将原 prime--continuum 子系统
误称为完整 Gamma gluing 或上同调 Weil 结构。数值高度有限也不是数值验证了
随 \(Y\) 无界增长的零点集合。本篇没有新增未执行的实验、数值证书或新颖性声明。

## 9. 有限复算与内部独立审计

复算脚本：[polylog_spectral_localization_probe.py](../scripts/polylog_spectral_localization_probe.py)。
只用已安装的 mpmath，运行命令：

```text
python -B scripts/polylog_spectral_localization_probe.py
```

将 \(\mathcal A_\xi=e^{-x}\sum_{\nu=0,\pm\xi}P_\nu(x)e^{i\nu u}\)、
\(x=e^u/Y\) 展开，归一化 jet 的多项式递推为
\[
 \widetilde P_{j+1}
   ={x\over h}\widetilde P_j'
      +\left({i\nu\over h}-1-{x\over h}\right)\widetilde P_j .
\]
脚本用有限区间不完全 Gamma 积分逐单项重算(16)，另用直接积分及低阶微分
独立检查。六例取 \(N=Y=16,64,256\)，含低虚部、共振附近及 \(|\gamma|>4h\)；
这些 \(\rho\) 是合成参数，不冒称实际 zeta 零点。
两端与完整中心化项均保留。MP70恒等式最大缩放误差
\(3.57\cdot10^{-71}\)，独立 jet 微分误差 \(1.59\cdot10^{-70}\)，
首例直接积分误差 \(9.95\cdot10^{-72}\)，全部只记[E]。
有限检查不证明增长阶常数、全谱求和或记录历史界；这些依赖上述解析证明。

主代理与独立代理已完成全文逆向审计，并重新核对外部显式公式的半权约定。
审计重点是：先固定参数再取显式公式高度极限；保留 \(h-\sigma\) 而不产生
\(2^m\) 损失；先分离振荡因子再作Cauchy估计；全部下端初值与阶乘；
全谱端点先合并；浅层原核与浅层端点相减；全高谱尾；原物理通道的四次方根转移。
内部通过不是外部同行评议、新颖性确认、完整中频预算或Goal阶段验收。
