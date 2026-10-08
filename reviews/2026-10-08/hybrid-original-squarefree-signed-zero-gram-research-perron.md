# 原 prime/squarefree 主项：固定零点包、带符号 Gram 与二阶障碍

2026-10-08，perron_reviewer。研究基线 main \(\texttt{3afd193}\)。
只新增本研究源，不改冻结输入、检查器、输出或 Git。
**状态：结构推导待不同作者全文审查；没有新的 whole 四矩增长幂。**

本轮不再调整490的误差参数。得到的是三个准确接口：
原平方自由生成函数的全部零点极点来自同一个 \(-\zeta'/\zeta\)；
原共同两端 entire Perron 核可写为一个对全部正高度窗固定的有限零点包；
该包的二阶 Gram 与四阶 Gram 都有保留相位的精确表达式。
二阶平均已有无条件 polylog 控制，但它不能削弱当前顶端 \(5/7\)
的第四矩密度费用。真正未付的是明确的四零点带符号相关，
或真实 prime/squarefree 卷积的完整移位相关。

## 1. 冻结输入、固定参数与实际对象

本轮 FULL READ 395、419、490、476及475/476的完整作者源。
哈希只将 CRLF/lone CR 转 LF，不 trim。

| 输入 | canonical LF SHA256 |
| --- | --- |
| [395原平方自由 Euler/Perron](hybrid-original-squarefree-core-euler-perron-research-perron.md) | 2f25a678b0c38c95a40469c41a757506c6f1fe64343bed327c7effe298e980c0 |
| [419带权 Möbius 条件源](hybrid-original-weighted-mobius-squarefree-perron-research-high-product.md) | 426e0e72e9234e6a9eccbe9a82e3055e7bbbc1669956ae78b9c4a6f82e9799b6 |
| [490已准入配置](../../notes/490-original-weighted-mobius-squarefree-conditional-remainder.md) | a5bf40493c864774da5f8fbecce8d257bc21176a78b16ff1841c89843d4924ef |
| [475完整原零点包源](hybrid-positive-height-zero-packet-fourth-upper-research-radial.md) | 8bcbd27da46d922d9e6e741fcf9a87012d565052f8d97b3ad12e99b3edbc2481 |
| [476密度迁移完整源](hybrid-ivic-density-and-scalar-fourth-growth-research-twisted.md) | a21a19e7bd09892ed705fa7883143e49c138ffe112c561be9413edaf44d72a1d |
| [476现有整个实部包络](../../notes/476-original-fourth-growth-five-sevenths-with-ivic-density.md) | 179829dd25f92ff187359f73455aafad9f957d714df13cf871db47a76e9408b6 |

固定 \(X=T/(2\pi)\)、\(L=\log X\)、\(J=[T/4,4T]\)，
\(N_L=a_LL\)、\(a_L\ge c_\phi>0\)。保留490配置
\[
 v=\frac1{8\theta},\quad y=1-\frac1{4\theta},\quad
 U=V=\lfloor X^v\rfloor,\quad H=V^2,\quad Y=X^y,
 \qquad \frac12<\theta<1.
 \tag{1}
\]
普通整个半平面前件仍是 \([R_\theta]\)；具体名义输入为 \(\theta=7/8\)。
本文不重新证明或扩大该前件。原未付函数严格为
\[
 R(t)=-\frac1{N_L}
 \sum_{\substack{p>U\ {\rm prime},\ k>V\ {\rm squarefree}\\Y<pk\le X}}
       \frac{(\log p)b_V(k)}{\sqrt{pk}}(pk)^{it},\qquad
 b_V(k)=\sum_{d\mid k,\ d\le V}\mu(d).
 \tag{2}
\]
\(p\mid k\) 仍允许；全部 aspect ratios 和共同乘积窗口都保留。

## 2. 全部未知零点极点的准确剥离

先在 \(\Re w>1\) 的绝对收敛区定义
\[
 F_V(w)=F_{V,1}(w),\quad C_V(w)=\frac{F_V(w)}{\zeta(2w)},\quad
 D_U(w)=Q_{\rm pp}(w)+F_U^{\rm prime}(w).
\]
这里 \(Q_{\rm pp}\) 含全部 proper powers，\(F_U^{\rm prime}\)
只含 \(p\le U\)。395的准确身份给
\[
 A_U=-\frac{\zeta'}{\zeta}-D_U,\qquad
 B_{\rm sf}=\zeta C_V-1.
\]
故未归一化的实际无限系数生成函数为
\[
 \boxed{-A_UB_{\rm sf}
 = C_V\zeta'+D_U\zeta C_V-D_U-\frac{\zeta'}{\zeta}.}
 \tag{3}
\]
前三项记为 \(G_{U,V}(w)\)。在 \(\Re w>1/2\) 且非零高度，
它们全纯：有限局部因子 \(1+p^{-w}\) 的零点在 \(\Re w=0\)，
\(1/\zeta(2w)\) 的绝对 Euler 级数合法，proper-power 级数绝对收敛，
\(\zeta,\zeta'\) 的 pole1只在零高度。
因此未知普通零点的全部极点严格集中于最后一个 \(-\zeta'/\zeta\)。
每个零点的留数仍为 \(-m_\rho\)，没有 \(V\) 权重或留数减幅。

定义原共同窗口的 von Mangoldt polynomial
\[
 L_{Y,X}(t)=\frac1{N_L}\sum_{Y<n\le X}\frac{\Lambda(n)}{\sqrt n}n^{it}.
\]
在初线逐系数比较(3)，有精确有限多项式身份
\[
 \boxed{R=L_{Y,X}+A_{U,V;Y,X}},\qquad
 A_{U,V;Y,X}=\frac1{N_L}
                  \sum_{Y<n\le X}[n^{-w}]G_{U,V}(w)\ n^{-1/2+it}.
 \tag{4}
\]
这里 \([n^{-w}]\) 表示初线 Dirichlet 系数，不是将全纯函数截成任意
独立矩形；(4)保持(2)全部真实有限 masks。

419的 \(r=1\) 带权 prefix 和 prime prefix 给左线
\[
 |C_V(1/2+c-i\tau)|\ll V^\alpha T^\rho L^C,\quad
 |D_U(1/2+c-i\tau)|\ll U^\alpha T^\rho L^C,\quad
 \alpha=\theta-1/2+\delta,\quad c=1/L.
\]
395的无限初线、共同两端截断及无条件水平线逐式适用于 \(G_{U,V}\)。
其系数由实际(3)或(4)比较得
\(|[n^{-w}]G_{U,V}|\ll \tau(n)\log(2n)\)，所以远尾仍用准确
\(n^{-1-c}\) 级数，近端才用有限 divisor 幂界。
外水平线继续使用无条件局部界，不把上面的条件 prefix 放到整条横线。
共同核的 Minkowski 与已付 \(\zeta^4,(\zeta')^4\) 给
\[
 \mathcal M_{A_{U,V;Y,X}}\ll X^{4(2\theta-1)v+\epsilon}
                           =X^{c_\theta+\epsilon}.
 \tag{5}
\]
这是旧 \(c_\theta\) 费用的一个准确解释，**不是新的预算改进**。
它说明平方自由结构把解析修正移到小费用，仍留下原
von Mangoldt 函数的全部零点包。

## 3. 固定绝对负高度、原两端 entire 核的有限零点包

下面只对 \(L_{Y,X}\) 作显式公式，不把 \(G_{U,V}\) 移过
\(\Re w=1/2\)，也不遗漏 \(\zeta(2w)\) 的其它奇点。
取半整数
\[
 x=\lfloor X\rfloor+\tfrac12,\quad z_0=\lfloor Y\rfloor+\tfrac12,\quad
 F_{x,z_0}(z)=\frac{x^z-z_0^z}{z}
             =\int_{\log z_0}^{\log x}e^{zu}\,du.
 \tag{6}
\]
这个函数 entire，在 \(z=0\) 的值是 \(\log(x/z_0)\)；
两端在移线前合并，保留原整数集合。

475所证明并采用的普通 zeta 局部输入是
\[
 \#\{\rho:|\Im\rho-u|\le1\}\ll\log(2+|u|),\qquad
 \frac{\zeta'}{\zeta}(\sigma+iu)
 =\sum_{|\Im\rho-u|<1}\frac{m_\rho}{\sigma+iu-\rho}+O(\log |u|).
 \tag{7}
\]
重数保留；在所用固定实部区间，远零部分由 Hadamard 差式绝对支付。
本轮实际核读一手
[Fesenko–Ricotta–Suzuki, Appendix A, Proposition A.1 及(A.6)](https://www.numdam.org/article/AIF_2012__62_5_1819_0.pdf)
的证明；这里只消费其普通 zeta 特例，不消费 mean-periodicity 结论。

由(7)，分别可固定选择
\[
 h_0\in[T/32,T/16],\qquad h_1\in[5T,6T],
 \tag{8}
\]
使 \(-h_0,-h_1\) 距所有零点 ordinate 至少 \(c_0/L\)。
证明是删去总计 \(O(TL)\) 个 ordinate 的半径 \(c_0/L\)
小邻域；先令固定 \(c_0>0\) 足够小，每个候选区间仍有剩余。
这两个绝对高度对全部 \(t\in J\) 同时固定。

置 \(s_0=1/2-it\)、\(\kappa=1/2+c\)。
初始相对竖线 \(z=\kappa+i\omega\) 的端点取
\(\omega_-=t-h_1\)、\(\omega_+=t-h_0\)。
它们异号，离零分别至少 \(T\)、\(3T/16\)，且绝对值 \(O(T)\)。
非对称截断 Perron 由两个振荡尾分别分部积分给通常的
\(\min\{1,C/(T|\log(x/n)|)\}\) 误差。
对两半整数端点，近端 harmonic 和及远端
\(\sum\Lambda(n)n^{-1-c}=-\zeta'/\zeta(1+c)\ll L\)
给总误差 \(O(X^{-1/2}L^2)\)。完整 \(n>X\) 无限尾没有删除。

将该矩形左线移至 \(\Re z=-3/2\)，即 \(\Re(s_0+z)=-1\)。
上下横线始终是绝对 zeta 高度 \(-h_1,-h_0\)；
由(7)及避零距离，整个横线 \(D=-\zeta'/\zeta\) 为 \(O(L^2)\)。
核在横线上为 \(O(\sqrt X/T)\)，横线总费用 \(O(X^{-1/2}L^2)\)。
左线上 functional equation 与 \(\Re=2\) 的绝对级数给
\(|D(-1-iu)|\ll L\)，所以左积分
\[
 \ll z_0^{-3/2}L^2.
 \tag{9}
\]
矩形所有绝对高度都为负且 \(\asymp T\)；pole1不在矩形内，
也未跨 \(-2,-4,\ldots\) 的 trivial zeros。
若某个零点落在相对 \(z=0\)，(6) entire，仍准确计算其真实留数。

记固定有限集
\[
 \mathcal Z_T=\{\rho=\beta-i\gamma:\ h_0<\gamma<h_1,\quad0<\beta<1\},
 \qquad a_\rho=\beta-\tfrac12.
\]
对 distinct zeros 保留重数 \(m_\rho\)，得到对所有 \(t\in J\) 的公式
\[
 \boxed{L_{Y,X}(t)=Z_T(t)+r_T(t),\quad
 Z_T(t)=-\frac1{N_L}\sum_{\rho\in\mathcal Z_T}
               m_\rho F_{x,z_0}(a_\rho+i(t-\gamma)),}
 \tag{10}
\]
\[
 \sup_{t\in J}|r_T(t)|
 \ll_\phi X^{-1/2}L^2+Y^{-3/2}L^2.
 \tag{11}
\]
有限零点集独立于 \(t\)，没有 row-dependent 高度 mask，
没有扩大零点集合以后再把额外 signed 尾当成小项。
结合(4)，\(R=Z_T+A_{U,V;Y,X}+r_T\)。

## 4. 精确二阶 Gram：PSD 不表示每个交叉项非负

令 \(f_\rho(t)=F_{x,z_0}(a_\rho+i(t-\gamma))\)，则
\[
 \mathcal M_{2,Z}:=\frac1T\int_J|Z_T(t)|^2dt
 =\frac1{N_L^2}\sum_{\rho,\sigma\in\mathcal Z_T}
                       m_\rho m_\sigma K_J(\rho,\sigma),
 \quad K_J=\frac1T\int_J f_\rho\overline{f_\sigma}\,dt.
 \tag{12}
\]
这是有限和，交换无需无限收敛论证。其 Gram 矩阵半正定，
且 \(K_J(\sigma,\rho)=\overline{K_J(\rho,\sigma)}\)；
单个非对角实部则可变号。

对 \(a,b>0\) 的单端正载波先记
\[
 f_{\rho,x}(t)=x^a e^{i(t-\gamma)\log x}/(a+i(t-\gamma)).
\]
共同 \(x^{it}\) 消掉以后，设 \(\Delta=\gamma-\gamma'\)，
\[
 G_J(a,\gamma;b,\gamma')=\frac1T\int_J
       \frac{dt}{(a+i(t-\gamma))(b-i(t-\gamma'))}.
 \tag{13}
\]
设 \(A=a-i\gamma,B=b+i\gamma'\)，精确原函数为
\[
 G_J=\left.\frac{\log(A+it)-\log(B-it)}
                  {iT(A+B)}\right|_{T/4}^{4T}.
 \tag{14}
\]
两分母实部正，principal log 沿该段连续。
被积函数的实部是
\[
 \frac{ab+(t-\gamma)(t-\gamma')}
      {(a^2+(t-\gamma)^2)(b^2+(t-\gamma')^2)}.
 \tag{15}
\]
例如取 \(\gamma=T/8,\gamma'=9T/2\) 和固定 \(0<a,b<1/2\)，
在整个 \(J\) 上(15)为负（大 \(T\)）。
这个例子说明核的数学符号，不声称这些位置存在实际离线 zeta 零点。

完整实轴的对照核可由 Laplace 积分或留数直接得
\[
 \int_{\mathbb R}
       \frac{dt}{(a+i(t-\gamma))(b-i(t-\gamma'))}
 =\frac{2\pi}{a+b-i\Delta}.
 \tag{16}
\]
但真实单端 Gram 还乘相位 \(x^{a+b}e^{-i\Delta\log x}\)。
其完整实轴实部正比于
\[
 (a+b)\cos(\Delta\log x)+\Delta\sin(\Delta\log x),
 \tag{17}
\]
仍可为负。因此“共同正载波”没有把实际交叉项变成非负。
原两端核还必须保留 \(xx,z_0z_0,xz_0,z_0x\) 四组 Gram；
在 \(a=0\) 或 \(b=0\) 时不单独使用奇异单端式，
始终以(6)、(12)的 entire 合并核解释。

## 5. 无条件二阶付款及其对第四阶的严格限制

有限 polynomial 长度为 \(X\asymp T\)。无需新的均值外部定理：
对任意 \(Q(t)=\sum_{n\le X}q_n n^{it}\)，直接积分和
\(|\log(n/m)|\ge|n-m|/X\)，再用 \(2|q_nq_m|\le|q_n|^2+|q_m|^2\)，给
\[
 \frac1T\int_J|Q(t)|^2dt
 \ll (1+XL/T)\sum_{n\le X}|q_n|^2
 \ll L\sum|q_n|^2.
 \tag{18}
\]
对 \(L_{Y,X}\)，粗界 \(\Lambda(n)\le L\)、\(a_L\ge c_\phi\)
直接给 \(\sum|q_n|^2\ll\sum_{n\le X}1/n\ll L\)。
由(10)—(11)，已经无条件证明明确的带符号零点 Gram 统计量
\[
 \boxed{\frac1{N_L^2}\sum_{\rho,\sigma}
       m_\rho m_\sigma K_J(\rho,\sigma)
       =\mathcal M_{2,Z}\ll_\phi L^2.}
 \tag{19}
\]
这是实际 signed 二阶估计；不是由密度逐项取绝对值得出的结论。
它仍不能反向限制各个 \(\beta\) 子包的范数，或删去其交叉项。

准确的主项系数记为
\[
 q_V(n)=-\sum_{\substack{p\mid n,\ p>U\ {\rm prime}\\
                         n/p>V,\ n/p\ {\rm squarefree}}}
                   (\log p)b_V(n/p),\quad
 R(t)=\sum_{Y<n\le X}r_n n^{it},\quad
 r_n=q_V(n)/(N_L\sqrt n).
 \tag{20}
\]
其支持只含 squarefree \(n\)，或一个 prime 的 valuation恰为2、
其它 prime valuation至多1的 \(n\)；后者没有删掉 \(p\mid k\)。
由于 \(\sum_{p\mid n}\log p\le\log n\)，
\(|q_V(n)|\le\tau(n)\log n\)。于是
\[
 \sum|r_n|^2\ll\sum_{n\le X}\tau(n)^2/n\ll L^4,\qquad
 \mathcal M_{2,R}\ll L^5.
 \tag{21}
\]
最后一界可直接由 coefficientwise \(\tau^2\le\tau_4\) 及
\(\sum_{n\le X}\tau_4(n)/n\le(\sum_{n\le X}1/n)^4\) 得到。
这些仅是二阶付款，不是新的第四矩 whole 界。

二阶不足的顶端障碍可以精确量化。固定 \(a_\rho\ge\eta>0\)，
且 \(\gamma\in[T/2,3T]\)。由于
\(z_0^{a_\rho}/x^{a_\rho}\to0\) 统一成立，(6)给
\[
 \frac1T\int_J|f_\rho|^2dt\asymp_\eta \frac{x^{2a_\rho}}T,\qquad
 \frac1T\int_J|f_\rho|^4dt\asymp_\eta \frac{x^{4a_\rho}}T.
 \tag{22}
\]
分母积分分别是 \(\pi/a_\rho\)、\(\pi/(2a_\rho^3)\) 的固定常数级量。
若只使用某个固定实部 bin 的密度指数 \(n(\sigma)\)，
其二阶、四阶对角费用的幂分别为
\[
 2\sigma-2+n(\sigma),\qquad4\sigma-3+n(\sigma).
 \tag{23}
\]
重数的额外固定幂由(7)的 \(m_\rho\ll L\) 支付，不改变这里的幂。
如476，先固定实部 bin 宽，再分配到最终 \(\epsilon\)；
下面数值是顶端包络值，不要求 moving-\(\sigma\) 密度常数一致。
476顶端 \(\sigma=7/8\) 采用 \(n_I=3/14\)，所以
\[
 \boxed{2(7/8)-2+3/14=-1/28,\quad
        4(7/8)-3+3/14=5/7.}
 \tag{24}
\]
这是密度上界的费用比较，不是假设实际零点饱和该上界。
它说明现有输入容许顶端包的二阶对角贡献很小而四阶贡献仍增长。
因此(19)甚至理想的二阶近正交，都不自动给严格小于 \(5/7\) 的第四矩。

## 6. 尚缺的四零点 signed 统计量

固定有限包的准确第四矩是
\[
 \boxed{\mathcal M_{Z}
 =\frac1{N_L^4}
   \sum_{\rho_1,\rho_2,\rho_3,\rho_4\in\mathcal Z_T}
    m_{\rho_1}m_{\rho_2}m_{\rho_3}m_{\rho_4}
    H_J(\rho_1,\rho_2;\rho_3,\rho_4),}
 \tag{25}
\]
\[
 H_J=\frac1T\int_J
       f_{\rho_1}f_{\rho_2}\overline{f_{\rho_3}f_{\rho_4}}\,dt.
 \tag{26}
\]
对 pair indices，它也是 Gram；半正定仍不意味着每个条目非负。
令 \(\mathfrak D_4\) 只含
\(\{\rho_1,\rho_2\}=\{\rho_3,\rho_4\}\) 的 pairing diagonal，
其贡献均为非负；令 \(\mathfrak C_4\) 为全部其余项的真实和。
则 \(\mathcal M_Z=\mathfrak D_4+\mathfrak C_4\)，
其中自对角 \(\rho_1=\rho_2=\rho_3=\rho_4\) 已具有(22)—(24)的费用。

475的绝对值与加权 Jensen 最终保留
\(L^3T^{-1}\sum_\rho X^{4(\beta-1/2)_+}\)；
对本固定集合和新下端 \(Y\)，同一直接核界
\(|F|\ll X^{(\beta-1/2)_+}L/(1+L|t-\gamma|)\) 仍逐式适用；
因此原密度费用在这里合法，未搬用不同 signed 子族的范数。
476据此得到 \(5/7\)。仅把其中 off-diagonal 设为0或节省日志，
并不消除该四阶自对角费用。
若要在同一密度输入下严格改善，还必须证明实际
\(\mathfrak C_4\) 的负相消足以抵消相应 diagonal，
或另证实际零点分布使该 diagonal 小于目前密度上界。

一个精确的新增长目标是：固定某个 \(0<\delta_0<2/7\)，证明(25)的完整
signed 四重和为 \(O(X^{5/7-\delta_0+\epsilon})\)，或直接为常数级。
它必须保留 \(x,z_0\) 两端、全部重数、原 \(J\)、全部交叉项。
由于(5)、(11)，一旦得到该目标，便推出
\[
 \mathcal M_R\ll X^{\max(5/7-\delta_0,\ 3/7)+\epsilon}
 \quad(\theta=7/8).
 \tag{27}
\]
这里的主项预算收益是真实的；本文**没有证明该新目标**。
对增长幂 \(B\ge c_\theta\)，零点包与准确主项的预算由(5)和
\(L^4\) 三角不等式双向互通。若零点包本身为常数级，(27)仍只给
\(R\) 的 \(3/7\) 界；常数级 \(R\) 还须处理真实全纯修正的增长。
这不是一个关于一般无权 \(\gamma\)-pair correlation 的替代猜想：
所需核含 \(\beta\) 权、重数、\(\log x,\log z_0\) 相位及四阶乘积。

还可由(6)给出准确 Fourier 形式。令
\[
 S_T(u)=\sum_{\rho\in\mathcal Z_T}
         m_\rho e^{(\beta-1/2)u}e^{-i\gamma u},\qquad
 I=[\log z_0,\log x].
\]
则 \(Z_T=-N_L^{-1}\int_I e^{itu}S_T(u)\,du\)。
原有限 \(J\) 的四阶统计仍是(25)；若使用完整实轴 Plancherel，
得到的是 \(2\pi N_L^{-4}\| (1_IS_T)*(1_IS_T)\|_2^2\)，
它只是原窗的正上界，不能未经付款将原窗和完整实轴互换。

## 7. 真实系数移位相关及已付 diagonal

准确平方 polynomial 写为
\[
 R(t)^2=\sum_\ell g_\ell\ell^{it},\qquad
 g_\ell=\sum_{\substack{n_1n_2=\ell\\Y<n_1,n_2\le X}}r_{n_1}r_{n_2}.
 \tag{28}
\]
各 \(r_n\) 始终是(20)的真实 prime/squarefree masks；没有改变
\(Y<p_i k_i\le X\) 为独立矩形。
直接原高度窗积分给
\[
 \mathcal M_R=\sum_{\ell,\ell'}g_\ell g_{\ell'}\Phi_T(\log(\ell/\ell')),
 \quad
 \Phi_T(u)=\frac{15}{4}e^{17iTu/8}
                  \operatorname{sinc}(15Tu/8).
 \tag{29}
\]
其中 \(g_\ell\) 为实数，最终和取真实共轭配对后的实数值；
\(\operatorname{sinc}(0)=1\)。这不是每条相关可取绝对值的正核。

由(21)的 coefficient 上界，
\[
 |g_\ell|\ll\tau_4(\ell)/\sqrt\ell,\qquad
 \sum_{\ell\le X^2}|g_\ell|^2\ll L^{16}.
 \tag{30}
\]
一般 coefficientwise \(\tau_k^2\le\tau_{k^2}\) 可由整数矩阵
的 row/column marginals 证明：任意两个 composition 都有非负整数
矩阵实现该组 marginals；故 \(k^2\) 格 composition 到二组
\(k\) 格 composition 的映射满射。最后再用 harmonic product 求和。
所以真实算术乘积 diagonal 已无条件付款至 polylog。
仍未付的是(29)的全部非对角带符号相关。
若目标是常数级，必须保留这个 diagonal 的准确值；
仅将它粗付为 polylog 后证明 off-diagonal 为 \(O(1)\) 并不足够。

写 \(\ell'=\ell+h\)，其真实目标为
\[
 \operatorname{Re}\sum_{h\ne0}\sum_\ell
       g_\ell g_{\ell+h}\Phi_T(\log(\ell/(\ell+h)))
       \ll X^{5/7-\delta_0+\epsilon},
 \tag{31}
\]
并保留全部实际支持。近共振尺度为 \(|h|\lesssim\ell/T\)，
顶端 \(\ell\asymp X^2\) 时为 \(|h|\lesssim X\)。
仅证明该近区还不足够：其它 \(h\) 也须对同一真实 \(g\) 付款；
本文没有由原 \(P_H\) 的 far 界对其 signed 子族作单调推断。

平方自由系数还有精确 complementary-divisor 身份
\[
 b_V(k)=-\mu(k)\sum_{\substack{e\mid k\\e<k/V}}\mu(e)
 \qquad(k>V,\ k\ {\rm squarefree}).
 \tag{32}
\]
它来自 \(\sum_{d\mid k}\mu(d)=0\)、\(d>V\Leftrightarrow e=k/d<k/V\)。
严格端点和实际共同乘积窗口必须保留。
例如不同 \(p,q>V\) 的 semiprime \(n=pq\) 有
\(q_V(n)=-\log n\)，而 \(n=p^2,p>V\) 有 \(q_V(n)=-\log p\)。
这些身份确实固定了 signed 算术；它们本身没有给(31)相消。

## 8. 本轮结论

本轮建立了固定有限零点包和精确 signed Gram 接口，
并证明全包二阶 polylog、真实乘积 diagonal polylog。
顶端的 \(-1/28\) 与 \(5/7\) 费用差明确解释了为何仅加强二阶
或删去逐包绝对值的交叉项，不自动改善完整第四矩。
新的研究靶点是(25)保相位的四零点相关或(31)准确移位卷积；
留数仍为 \(-m_\rho\)，平方自由结构没有将其消掉。

没有得到新的 whole 幂、中心四阶常数预算、比例或无零边界。
没有数值零点采样，没有有限枚举替代解析证明，也没有参数重新优化。
