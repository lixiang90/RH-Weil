# 原平方自由主项：完整低实部与下端付款后的纯上端 Cauchy 包

2026-10-08，perron_reviewer。研究轮4，基线 main da5f0df。
只新增本研究源，不改冻结来源、输出、检查器或 Git。待不同作者全文审查。

本稿仅在名义普通 \([R_{7/8}]\)、490的 \(Y=X^{5/7}\) 配置中证明：
实际 \(R\) 可改写为一个固定的纯 \(X\) 端点 Cauchy 包加完整误差 \(3/7\)。
低实部的整个两端包费用为 \(1/5\)，高实部的整个 \(Y\) 端点费用为 \(11/35\)。
这些费用直接对相应完整集合证明，不从旧 signed 总范数限制子包。
本稿改变未付主项的结构，没有改善其 \(5/7\) 增长指数或任何零点比例。

## 1. 完整读取与名义固定对象

本轮 FULL READ 453、188原载体源、493，以及184行的完整密度源。
canonical LF SHA256只将CRLF/lone CR转LF，不trim。

| 输入 | 行数 | canonical LF SHA256 |
| --- | --- | --- |
| [453固定零点包](hybrid-original-squarefree-signed-zero-gram-research-perron.md) | 453 | 0b126138c7bf42e9be3c4352b099a6ab37d88cef93af20593593c8e849aa2a17 |
| [188原载体四阶](hybrid-original-squarefree-carrier-fourth-near-research-perron.md) | 188 | 2142645eed724da49a3e6faae7068adb2c8ca907c196a691f09a2b7a7fd6f3ae |
| [184密度全分段](hybrid-ivic-density-and-scalar-fourth-growth-research-twisted.md) | 184 | a21a19e7bd09892ed705fa7883143e49c138ffe112c561be9413edaf44d72a1d |
| [493消费范围](../../notes/493-original-reference-subtraction-and-carrier-near-correlations.md) | 140 | efbefb73a457e1bda079fdb9c003ec4bcf9c50d89a1f1c2053b548153371a67a |

取 \(X=T/(2\pi)\)、\(L=\log X\)、\(N_L=a_LL\ge c_\phi L\)、
\(J=[T/4,4T]\)，固定490名义配置
\[
 U=V=\lfloor X^{1/7}\rfloor,\quad H=V^2,\quad Y=X^{5/7}.
\]
保留其全部真实 prime/squarefree 系数、\(p\mid k\)、负号、方面比及共同乘积两端。
普通全高度 \([R_{7/8}]\) 仅用于既有条件输入，不引入其他零点家族。
沿453固定 \(h_0\in[T/32,T/16]\)、\(h_1\in[5T,6T]\)，准确零点集为
\[
 {\cal Z}_T=\{\rho=\beta-i\gamma:h_0<\gamma<h_1,\ 0<\beta<1\},
 \quad a_\rho=\beta-1/2,\quad m_\rho=\operatorname{mult}(\rho).
\]
它是原负绝对高度的完整有限集合；不添加共轭高度、不移动端点或删除重数。
令 \(x=\lfloor X\rfloor+1/2\)、\(z_0=\lfloor Y\rfloor+1/2\)，
\[
 f_\rho(t)=\frac{x^{a_\rho+i(t-\gamma)}-z_0^{a_\rho+i(t-\gamma)}}
                  {a_\rho+i(t-\gamma)}.
\]
分母零处始终取entire延拓。453的完整函数身份是
\[
 R=Z_T+A+r_T,\qquad Z_T=-N_L^{-1}\sum_{{\cal Z}_T}m_\rho f_\rho,
\]
\[
 {\cal M}_A\ll X^{3/7+\epsilon},\quad
 \sup_J|r_T|\ll X^{-1/2}L^2+Y^{-3/2}L^2,\quad
 {\cal M}_f=T^{-1}\int_J|f|^4dt.                           \tag{1}
\]
原 \(\nu\) 保持188的准确定义、floor与固定 \(\chi\)，且
\(0\le\nu\ll_\chi T^{-1}1_J\)。以下范数界也直接适用于 \(M_{\nu,f}=\int\nu|f|^4\)；
不反向利用单个 \(\nu\) 覆盖canonical窗。

## 2. 全部低实部：保留两端的直接付款

固定 \(\eta_0=1/20\)，准确分成
\[
 {\cal L}=\{\rho\in{\cal Z}_T:a_\rho\le\eta_0\},\qquad
 {\cal H}={\cal Z}_T\setminus{\cal L}.
\]
低集合包括全部 \(\beta\le1/2\)、负 \(a_\rho\) 和任意接近 \(a_\rho=0\) 的零点。
对它不分开两个奇异单端。entire积分表示及大 \(|t-\gamma|\) 时的分母给
\[
 |f_\rho(t)|\ll X^{\eta_0}\min(L,|t-\gamma|^{-1})
 \ll \frac{X^{\eta_0}L}{1+L|t-\gamma|}.                    \tag{2}
\]
在 \(t=\gamma\) 以左边的entire值解释。原局部零点计数按重数给
\(\sum_{|\gamma-u|\le1}m_\rho\ll L\)；对完整 \({\cal Z}_T\)、每个 \(t\in J\)，
\[
 \sum_\rho\frac{m_\rho}{1+L|t-\gamma|}
 \ll L+\sum_{1\le j\le CT}\frac{L}{Lj}\ll L.              \tag{3}
\]
因此 \(Z_{\cal L}:=-N_L^{-1}\sum_{\cal L}m_\rho f_\rho\) 点态为 \(O(X^{\eta_0}L)\)，
\[
 \boxed{{\cal M}_{Z_{\cal L}},\ M_{\nu,Z_{\cal L}}
              \ll X^{1/5}L^4.}                          \tag{4}
\]
这是该整个低包的独立positive majorant，不从 \({\cal M}_{Z_T}\) 推子集界。

## 3. 整个高包的下端：完整分段密度费用 \(11/35\)

高集合中 \(a_\rho>\eta_0\)，允许准确分开两端。记其下端为
\[
 C_Y(t)=\frac{e^{it\log z_0}}{N_L}
    \sum_{\rho\in{\cal H}}
        \frac{m_\rho z_0^{a_\rho}e^{-i\gamma\log z_0}}
             {a_\rho+i(t-\gamma)}.                       \tag{5}
\]
令 \(k(u)=(1+|u|)^{-1}\)。固定 \(\eta_0\) 给分母倒数 \(\ll_{\eta_0}k(u)\)，
局部计数给 \(\sum_{{\cal Z}_T}m_\rho k(t-\gamma)\ll L^2\)。
按重数作positive weighted Hölder，直接有
\[
 |C_Y(t)|^4\ll_{\eta_0}N_L^{-4}
 \left(\sum_{\cal H}m_\rho k(t-\gamma)\right)^3
 \sum_{\cal H}m_\rho z_0^{4a_\rho}k(t-\gamma).
\]
对每个 \(\gamma\)，\(T^{-1}\int_J k(t-\gamma)dt\ll L/T\)，原 \(\nu\) 积分也同样。
所以
\[
 {\cal M}_{C_Y},\ M_{\nu,C_Y}
 \ll_{\eta_0} \frac{L^3}{T}\sum_{\rho\in{\cal H}}m_\rho z_0^{4a_\rho}. \tag{6}
\]
重数没有删除；Hölder权为实际 \(m_\rho\)，不要求最小零点间距。

沿已准入184密度源的全部分段，正计数使用
\[
 n(\sigma)=
 \begin{cases}
 3(1-\sigma)/(2-\sigma),&1/2\le\sigma\le3/4,\\
 3(1-\sigma)/(3\sigma-1),&3/4\le\sigma\le4/5,\\
 3(1-\sigma)/(2\sigma),&4/5\le\sigma\le7/8.
 \end{cases}                                             \tag{7}
\]
最后一段的Ivić范围严格从 \(3831/4791<4/5\) 起，固定网格合法。
\([R_{7/8}]\) 给所有 \(\beta\le7/8\)。先固定有限实部网格与密度损失，
再令 \(T\to\infty\)，(6)的费用由
\[
 F_Y(\sigma)=\frac{20}{7}(\sigma-1/2)-1+n(\sigma)
             =\frac{20}{7}\sigma-\frac{17}{7}+n(\sigma)   \tag{8}
\]
控制；半整数 \(z_0\asymp X^{5/7}\) 只付固定常数。

| 实部区间 | 连续费用的严格核算 | supremum |
| --- | --- | --- |
| \([1/2,3/4]\) | \(F_Y'=20/7-3/(2-\sigma)^2\ge164/175>0\) | \(F_Y(3/4)=11/35\) |
| \([3/4,4/5]\) | \(F_Y''=36/(3\sigma-1)^3>0\)，比较两端 | \(\max(11/35,2/7)=11/35\) |
| \([4/5,7/8]\) | \(F_Y''=3/\sigma^3>0\)，比较两端 | \(\max(13/56,2/7)=2/7\) |

网格、日志和密度损失先分配进最终 \(\epsilon\)，得到
\[
 \boxed{{\cal M}_{C_Y},\ M_{\nu,C_Y}\ll X^{11/35+\epsilon}.} \tag{9}
\]
这里只对名义 \(y=5/7,\theta=7/8\) 核算；不泛化到其他 \(\theta\) 配置。
这不是从原signed包删出下端；(6)直接对全部实际高集合证明。

## 4. 完整主项化成固定纯上端 Cauchy 包

定义
\[
 \boxed{C_X(t)=-\frac{e^{it\log x}}{N_L}
  \sum_{\rho\in{\cal H}}
   \frac{m_\rho x^{a_\rho}e^{-i\gamma\log x}}
        {a_\rho+i(t-\gamma)}.}                           \tag{10}
\]
每个分母实部严格大于 \(1/20\)，不存在近 \(a_\rho=0\) 的分拆奇点。
原完整固定包准确为 \(Z_T=Z_{\cal L}+C_X+C_Y\)，所以
\[
 \boxed{R=C_X+E_C,\qquad E_C=A+r_T+Z_{\cal L}+C_Y.}        \tag{11}
\]
由(1)、(4)、(9)和 \(L^4\) 三角不等式，
\[
 \boxed{{\cal M}_{E_C},\ M_{\nu,E_C}\ll X^{3/7+\epsilon},}
 \qquad \max(3/7,1/5,11/35)=3/7.                         \tag{12}
\]
因此对任何固定 \(B\ge3/7\)，同一canonical或原 \(\nu\) 的 \(R\) 与 \(C_X\)
第四矩上界 \(O(X^{B+\epsilon})\) 双向互通；只运输完整函数差。
以(6)的方法将 \(z_0\) 换成 \(x\)，184的全实部费用仍给
\({\cal M}_{C_X},M_{\nu,C_X}\ll X^{5/7+\epsilon}\)。
这仅核既有增长基线；它没有支付 \(B<5/7\)。
已有 \(5/7\) 下，四次方差的Hölder费用仍为
\[
 {\cal M}_R={\cal M}_{C_X}+O(X^{9/14+\epsilon}),
 \quad M_{\nu,R}=M_{\nu,C_X}+O(X^{9/14+\epsilon}).         \tag{13}
\]
主项结构变得简单，误差与传递指数均没有改变。

## 5. 仍须消费的真正联合相位

置 \(d_\rho=m_\rho x^{a_\rho}e^{-i\gamma\log x}\)，则完整canonical核心准确是
\[
 {\cal M}_{C_X}=\frac1{TN_L^4}
 \sum_{{\cal H}^4}d_{\rho_1}d_{\rho_2}\overline{d_{\rho_3}d_{\rho_4}}
 \int_J\frac{dt}
 {(a_1+i(t-\gamma_1))(a_2+i(t-\gamma_2))
  (a_3-i(t-\gamma_3))(a_4-i(t-\gamma_4))}.                \tag{14}
\]
原 \(\nu\) 版本只把 \(dt/T\) 换成 \(\nu(t)dt\)，不改变这个固定集合。
局部计数或ordinary Hilbert型估计控制的是叠加常数、对角费用及日志，
没有交付(14)的真实四零点相位省幂。
对 \(\gamma\in[T/2,3T]\) 的内部零点，单个Cauchy核自项量级仍为
\(X^{4(\beta-1/2)}/T\)；全固定包只用这一uniform上界费用。
这是密度付款预算，不断言内部高实部零点存在或达到预算；名义费用仍为 \(5/7\)。
要改进，须证明完整(14)或准确的原平方自由近相关一侧界，
或证明相关实际高零点计数比已准入密度包络更小；不能把交叉项设零。

本稿所有零点分拆只在原 \(J\) 及原 \(\nu\) 上使用453的固定公式。
不将其搬到支撑超出 \(J\) 的辅助平移载体，不重选一个更大零点包。
没有新的whole增长、中心常数、比例、无零边界、外部文献输入或检查器。
