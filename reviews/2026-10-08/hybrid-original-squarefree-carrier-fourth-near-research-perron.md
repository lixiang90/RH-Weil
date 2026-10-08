# 原 prime/squarefree 四阶：原载体的远相关付款与近相关核心

2026-10-08，perron_reviewer。研究轮3，基线 main cd95587。
只新增本源，不改冻结输入、检查器、输出或 Git。待 root 与不同作者全文审查。

本稿保留原固定 \(\chi\)、离散 floor 和完整正测度 \(\nu\)。
在490的真实 prime/squarefree 主项上，证明原阈值外的全部系数四阶相关
绝对费用为 \(O(X^{2-\sqrt{8\pi}}\log^C X)\)。
这是该准确主项的新远相关付款；425已有一般 \(\Gamma\) 尾是所用工具。
未改善近相关、整个第四矩增长幂、常数预算、比例或无零边界。

## 1. 完整读取、冻结输入与原观察量

本轮 FULL READ 下列四源；453第一次输出截断的正文另逐行补读。
哈希只将 CRLF/lone CR 转 LF，不 trim。

| 输入 | 行数 | canonical LF SHA256 |
| --- | --- | --- |
| [实际载体425](hybrid-whole-fourth-unit-unit-actual-research-whole.md) | 425 | b3f14cf4ee5659f8e23bd51dc9bf71e853e783bd2d55e42ee8846d6e8d1e41dc |
| [原完整周期191](hybrid-original-coherent-period-energy-research-checkpoint-audit.md) | 191 | fe19e50f955c47b7abb22933d0b406a9bc339ac68056d8d115d1f7277be22c5f |
| [固定零点包453](hybrid-original-squarefree-signed-zero-gram-research-perron.md) | 453 | 0b126138c7bf42e9be3c4352b099a6ab37d88cef93af20593593c8e849aa2a17 |
| [490完整配置](../../notes/490-original-weighted-mobius-squarefree-conditional-remainder.md) | 118 | a5bf40493c864774da5f8fbecce8d257bc21176a78b16ff1841c89843d4924ef |

固定 \(X=T/(2\pi)\)、\(L=\log X\)、\(d=\lfloor XL\rfloor\)、
\(\eta=2\pi/L\)、\(s_T=T/\sqrt L\)，原 \(\chi\) 是固定正概率密度，
支撑于 \([3/8,5/8]\)，且
\[
 \Gamma(u)=\int\chi(v)e^{iuv}dv,\qquad
 |\Gamma(u)|\le e^{-\sqrt{|u|}/16}\quad(|u|\ge256).
\]
直接保留425的概率测度
\[
 \nu(t)=\frac1{ds_T}\sum_{k=0}^{d-1}
       \chi((t-T-k\eta)/s_T),\qquad \int\nu=1.                 \tag{1}
\]
其准确支撑两端为 \(T+3s_T/8\)、\(T+(d-1)\eta+5s_T/8\)。
大 \(T\) 时包含在 \(J=[T/4,4T]\)，并且
\[
 0\le\nu(t)\ll_\chi T^{-1}.                                \tag{2}
\]
因为每处非零 \(k\) 数至多 \(O(s_T/\eta+1)\)，且 \(d\eta\asymp T\)。
定义 \(\|f\|_{\nu,p}^p=\int\nu(t)|f(t)|^pdt\)。
没有更改原载体、选择新时间子集或将191的 Mellin 参数误认作原 \(t\)。

## 2. 真实有限系数、对角及准确原时间核

沿490取 \(1/2<\theta<1\)、
\[
 v=1/(8\theta),\quad y=1-1/(4\theta),\quad
 U=V=\lfloor X^v\rfloor,\quad Y=X^y,\quad N_L=a_LL,\ a_L\ge c_\phi>0.
\]
真实主项始终是453的
\[
 R(t)=\sum_{Y<n\le X}r_n n^{it},\quad
 r_n=-\frac1{N_L\sqrt n}
 \sum_{\substack{p\mid n,\ p>U\ {\rm prime}\\
 n/p>V,\ n/p\ {\rm squarefree}}}(\log p)b_V(n/p),\quad
 b_V(k)=\sum_{d\mid k,\ d\le V}\mu(d).                       \tag{3}
\]
保留 \(p\mid n/p\)、全部方面比、负号及共同乘积两端；系数均为实数。
\(|b_V(k)|\le\tau(k)\) 和 \(\sum_{p\mid n}\log p\le\log n\) 给
\[
 |r_n|\ll_\phi\tau(n)/\sqrt n,\qquad
 \sum_{Y<n\le X}|r_n|\ll_\phi\sqrt X L.                    \tag{4}
\]
后一界来自 \(\sum_{ab\le X}(ab)^{-1/2}\ll\sqrt X\sum_{a\le X}a^{-1}\)。
准确平方写成
\[
 R(t)^2=\sum_\ell g_\ell\ell^{it},\qquad
 g_\ell=\sum_{\substack{n_1n_2=\ell\\Y<n_1,n_2\le X}}r_{n_1}r_{n_2}.
\]
故 \(Y^2<\ell\le X^2\)，且
\[
 \sum_\ell|g_\ell|\ll X L^2,\quad
 |g_\ell|\ll\tau_4(\ell)/\sqrt\ell,\quad
 D_\nu:=\sum_\ell g_\ell^2\ll L^{16}.                       \tag{5}
\]
最后一步用453证明的 \(\tau_4^2\le\tau_{16}\) 和 harmonic product 和。
这个对角仅为已有 polylog 付款，不是常数级准确值。

有限求和与(1)直接交换，得到
\[
 M_{\nu,R}:=\|R\|_{\nu,4}^4
   =\sum_{\ell,\ell'}g_\ell g_{\ell'}\Psi_T(\log(\ell/\ell')),
\]
\[
 \Psi_T(u)=e^{iTu}\Gamma(s_Tu)\frac1d\sum_{k=0}^{d-1}e^{ik\eta u}.
                                                                    \tag{6}
\]
\(\Psi_T(0)=1\)、\(\Psi_T(-u)=\overline{\Psi_T(u)}\)。
此正测度的 Gram 半正定，单个非对角实部仍可变号。
原相位和有限几何核都在(6)；没有先绝对 Mellin 再借回时间相消。

## 3. 原阈值外的全部远相关付款

准确使用425原阈值
\[
 \Delta=1024L^{5/2}/X,\qquad \kappa=\sqrt{8\pi}>5.          \tag{7}
\]
大 \(X\) 时 \(s_T\Delta=2048\pi L^2\ge256\)，所以
\[
 |u|\ge\Delta\ \Longrightarrow\quad
 |\Psi_T(u)|\le|\Gamma(s_Tu)|
 \le e^{-\sqrt{2048\pi}L/16}=X^{-\kappa}.                 \tag{8}
\]
这里完整几何因子模长至多1，不删除其零点、aliases或 floor。
按全部实际 \((\ell,\ell')\) 定义 \(F_\nu\) 为(6)中
\(|\log(\ell/\ell')|\ge\Delta\) 的整个和，则(5)给
\[
 \boxed{|F_\nu|\le
 \sum_{\rm far}|g_\ell g_{\ell'}\Psi_T(\log(\ell/\ell'))|
 \ll X^{2-\sqrt{8\pi}}L^4.}                              \tag{9}
\]
这是 absolute 全族上界，不从另一个 signed 总量截取子族。
约 \(2-\sqrt{8\pi}=-3.013\)，没有有限采样或零点枚举。

令 \(C_{\nu,\rm near}\) 是其余 \(\ell\ne\ell'\)、\(|\log(\ell/\ell')|<\Delta\)
的完整实数和，准确有
\[
 \boxed{M_{\nu,R}=D_\nu+C_{\nu,\rm near}+F_\nu.}           \tag{10}
\]
近区要求 \(|\ell-\ell'|\ll\ell\Delta\)；顶端 \(\ell\asymp X^2\)
仍允许 \(|\ell-\ell'|\ll X L^{5/2}\)，没有免费移位正交。
对任何固定 \(B\ge0\)，若真实一侧近和上界为 \(O(X^{B+\epsilon})\)，
则(5)、(9)给该原载体的 \(M_{\nu,R}\ll X^{B+\epsilon}\)。
这只是尚未付的新近相关目标；本稿没有证明 \(B<5/7\)。

## 4. 同一有限零点包的原载体四阶核

保持453的两个固定绝对负高度和有限零点集合 \(\mathcal Z_T\)，
不重新选择随 \(t\) 移动的零点 mask。置
\[
 x=\lfloor X\rfloor+1/2,\quad z_0=\lfloor Y\rfloor+1/2,\quad
 I=[\log z_0,\log x],\quad
 S_T(u)=\sum_{\rho=\beta-i\gamma\in\mathcal Z_T}
       m_\rho e^{(\beta-1/2)u-i\gamma u}.
\]
记 \(a_\rho=\beta-1/2\) 及
\(f_\rho(t)=(x^{a_\rho+i(t-\gamma)}-z_0^{a_\rho+i(t-\gamma)})
/(a_\rho+i(t-\gamma))\)，在分母零处取 entire 延拓。
453的整个两端函数给 \(Z_T(t)=-N_L^{-1}\int_I e^{itu}S_T(u)du\)。
因此同一原正测度下准确地
\[
 \boxed{M_{\nu,Z}=N_L^{-4}\int_{I^4}
 S_T(u_1)S_T(u_2)\overline{S_T(u_3)S_T(u_4)}
 \Psi_T(u_1+u_2-u_3-u_4)\,d\boldsymbol u.}                \tag{11}
\]
零点有限、积分紧，所以交换全部合法。等价地是
\(\sum m_{\rho_1}\cdots m_{\rho_4}\int\nu f_{\rho_1}f_{\rho_2}
\overline{f_{\rho_3}f_{\rho_4}}/N_L^4\)，两端及重数全保留。
不从(9)反推某个零点四重和子域也有同一远费用。

原 \(\nu\) 在固定内部区间 \([6T/5,9T/5]\) 满足 \(\nu\asymp1/T\)。
证明：步长 \(h=\eta/s_T\to0\) 时，完整离散 Riemann 和
\(h\sum_k\chi(a-kh)=1+O(h\|\chi'\|_1)\)；该区间内全部支撑
均落在原 \(0\le k<d\) 中，故 \(\nu=(d\eta)^{-1}(1+O_\chi(h))\)。
对固定 \(a_\rho=\beta-1/2\ge\eta_0>0\)、
\(\gamma\in[5T/4,7T/4]\)，两端核在 \(|t-\gamma|\le1\) 的
下端与上端比 \(O((z_0/x)^{\eta_0})=o(1)\)；结合(2)及分母积分，
\[
 \int\nu(t)|f_\rho(t)|^4dt\asymp_{\eta_0} X^{4a_\rho}/T. \tag{12}
\]
所以现有密度指数 \(n(\sigma)\) 的单包四阶费用仍为
\(4\sigma-3+n(\sigma)\)；名义 \(\sigma=7/8,n_I=3/14\) 仍给 \(5/7\)。
这是上界费用比较，不声称实际零点或密度饱和；\(\nu\) 不自动消除自对角。

## 5. 已有误差运输与严格消费范围

由(2)，对任何真实函数
\(\|f\|_{\nu,4}^4\ll T^{-1}\int_J|f|^4\)。
453准确给 \(R=Z_T+A_{U,V;Y,X}+r_T\)，普通全高度 \([R_\theta]\)
下 \(\mathcal M_A\ll X^{c_\theta+\epsilon}\)、
\(c_\theta=1-1/(2\theta)\)，且
\(\sup_J|r_T|\ll X^{-1/2}L^2+Y^{-3/2}L^2\)。
故这些完整函数差合法运输到同一 \(\nu\)，名义修正仍为 \(3/7\)。
任何 \(B\ge c_\theta\) 的 \(M_{\nu,R},M_{\nu,Z}\ll X^{B+\epsilon}\)
由加权 \(L^4\) 三角不等式双向互通，不能运输某个 signed 子包。

490的完整 \(P_H-R=E_\theta\) 也运输为
\(\|E_\theta\|_{\nu,4}^4\ll X^{c_\theta+\epsilon}\)。
名义 \(\theta=7/8\) 在已有 \(5/7\) 合同下，原载体的第四矩差仍为 \(O(X^{9/14+\epsilon})\)；
这是已有费用的运输，不是新的误差或传递指数。

本稿仅证明原 \(\nu\) 的(9)及准确(10)、(11)。没有从原载体的第四矩
反推任意 canonical \(J\) 四矩、原 physical unit 频率子族或191的 \(E_H\)。
若将来改善(10)，消费 canonical whole 仍须另付统一覆盖合同；
不能借(2)的单向不等式逆向宣布 whole、比例或新无零区域。
没有检查器，没有外部文献新输入；普通零点留数仍为 \(-m_\rho\)。
