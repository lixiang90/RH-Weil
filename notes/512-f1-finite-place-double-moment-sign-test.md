# 512. 固定有限 S 的双矩零正值检验与全局化量词

2026-10-11。[T/N] 使用[511](511-f1-semilocal-fourier-inversion-cycle.md)的同一来源闭链。
对每个固定有限 \(S\)，构造实际紧支实测试 \(f_R\)，两个次数矩准确为零，
但 \(N_S(f_R*f_R^\sharp)>0\)（充分大 \(R\)）。
这是固定半局部对象的严格障碍，不是完整 \(N\) 或RH的反例。

## 1. 指定目标方向与实际有限 S 密度

[405](405-f1-adelic-restriction-moments-and-radical.md)的完整公式为
\[
 2W_{\rm pol}(f,g)=M_f(1)M_g(0)+M_f(0)M_g(1)
                          -\sum_\rho M_f(\rho)M_g(1-\rho).
\]
在RH下，对实 \(f=g\) 且 \(M_f(0)=M_f(1)=0\)，右侧为非正平方和。
所以完整Weil型在双矩零空间上的所需方向是 \(W_{\rm pol}(f,f)\le0\)。
这里仅据此固定检验方向，未以RH作构造输入。

511实际闭链密度为
\[
 a_S(\tau)=-b_S(\tau)=\log\pi-\operatorname{Re}\psi(1/4+i\tau/2)
 +2\sum_{p\in S_f}\log p\sum_{n\ge1}p^{-n/2}\cos(n\tau\log p).
                                                               \tag{1}
\]
它实偶连续，固定有限 \(S\) 时为 \(O_S(1+\log(2+|\tau|))\)。
Gamma反射、复制公式的对数导数给
\(\psi(1/4)=-\gamma-\pi/2-3\log2\)，因此
\[
 a_S(0)=\gamma+\pi/2+3\log2+\log\pi
       +2\sum_{p\in S_f}\frac{\log p\,p^{-1/2}}{1-p^{-1/2}}>0. \tag{2}
\]
它由同一实际来源确定，未自由加入正权。

## 2. 两个次数严格消失的紧支测试

取非零实偶 \(\chi\in C_c^\infty((-1,1))\)，\(R\ge1\)，令
\[
 g_R(t)=\chi(t/R),\quad F_R(t)=(\partial_t^2-\tfrac14)g_R(t),
 \quad f_R(t)=e^{-t/2}F_R(t).                              \tag{3}
\]
紧支分部积分对 \(s=0,1\) 给
\[
 M_{f_R}(s)=((s-\tfrac12)^2-\tfrac14)
                      \int e^{(s-1/2)t}g_R(t)dt=0.       \tag{4}
\]
若 \(F_R=0\)，紧支 \(g_R\) 满足 \(g_R''=g_R/4\)，
常微分方程唯一性迫使 \(g_R=0\)，矛盾。故 \(f_R\ne0\)。

令 \(h_R=f_R*f_R^\sharp\)，则
\[
 \eta_R(t)=e^{t/2}h_R(t)=F_R*\widetilde F_R(t),\quad
 \widetilde F_R(t)=F_R(-t),\quad
 \operatorname{supp}h_R\subset[-2R,2R].
\]
用 \(\widehat F(\tau)=\int F(t)e^{-i\tau t}dt\)，有
\[
 \varphi_R(\tau)=|\widehat F_R(\tau)|^2
   =(\tau^2+\tfrac14)^2R^2|\widehat\chi(R\tau)|^2\ge0.      \tag{5}
\]
矩消失为逐 \(R\) 的准确恒等式，未通过浮点调参近似实现。

## 3. 固定有限 S 的正值极限

511的普通电荷、\(v=R\tau\) 换元给
\[
 \frac{\Omega_S(c_{S,h_R})}{R}
 =\frac1{2\pi}\int a_S(v/R)(v^2/R^2+\tfrac14)^2
                               |\widehat\chi(v)|^2dv.    \tag{6}
\]
对 \(R\ge1\)，被积式由
\(C_S(1+\log(2+|v|))(v^2+\tfrac14)^2|\widehat\chi(v)|^2\)
支配，可积性来自Schwartz衰减。
支配收敛与Parseval准确给
\[
 \lim_{R\to\infty}\frac{\Omega_S(c_{S,h_R})}{R}
 =\frac{a_S(0)}{32\pi}\int|\widehat\chi(v)|^2dv
 =\frac{a_S(0)}{16}\|\chi\|_2^2>0,
\]
\[
 \boxed{\lim_{R\to\infty}
 \frac{N_S(f_R*f_R^\sharp)}{R}=\frac{a_S(0)}{32}\|\chi\|_2^2>0.} \tag{7}
\]
所以每个固定有限 \(S\) 均有双矩零正自配对。
仅在一个固定半局部来源上补齐次数字段，无法取得完整目标的非正方向。

## 4. 量词不能移到完整 N

511的全 \(N\) 比较对支集 \([-M,M]\) 要求包含全部 \(p\le e^M\)。
(3)的 \(R\) 趋大时支集增长，固定 \(S_f\) 没有满足此覆盖合同。
每个 \(R\) 虽然都有有限差
\[
 N(h_R)-N_S(h_R)=\sum_{p\notin S_f}\log p\sum_{n\ge1}h_R(n\log p),
\]
该差的符号或小量界尚未支付。
\(\varphi_R\ge0\) 不意味着 \(h_R(t)\ge0\)，不能假设补进更多素数只增加自配对。

因此(7)只排除指定固定 \(S\) 的符号方案，未否定完整Weil型负性，
没有得到实际线外零点。“固定 \(S\) 后取宽测试极限”与“随测试扩大 \(S\)”
是不同量词；(6)的支配常数也明确依赖 \(S\)。

## 5. 自然扩大 S 的 Fourier 缺陷不是迹类修正

令 \(\ell\notin S_f\)，\(S'=S\cup\{\ell\}\)。
真实源 \(F\mapsto F\otimes\mathbf1_{\mathbb Z_\ell^\times}\) 给自然等距嵌入
\[
 j_{S,S'}:L^2(C_S,|c|d^\times c)
        \longrightarrow L^2(C_{S'},|c|d^\times c).
\]
在基本域上，新单位壳层使新S-unit的 \(\ell\)-valuation必须为0，
所以周期化像准确为旧像在新紧群变量上的常函数。
新紧群概率Haar证明等距性；反演与模长红外投影也与 \(j\) 交织。
径向对数坐标中 \(j\) 是恒等嵌入，511的共同来源计算给
\[
 (\mathcal F_{S'}j-j\mathcal F_S)|_{\rm radial}
   =M_{(m_\ell-1)m_S}J_\tau,\quad
 m_\ell-1=\frac{2i\ell^{-1/2}\sin(\tau\log\ell)}
                       {1-\ell^{-1/2}e^{i\tau\log\ell}}. \tag{8}
\]
这是非零连续乘子，故在一个正测度谱集合上模长有正下界。
对应无限维 \(L^2\) 子空间的单位正交序列证明其非紧；更不属于迹类。
写 \(a=\ell^{-1/2}\)、\(z=\cos(\tau\log\ell)\)，
\[
 |m_\ell-1|^2=\frac{4a^2(1-z^2)}{1+a^2-2az}\le4a^2,
\]
因为分母减去 \(1-z^2\) 恰为 \((z-a)^2\)。
在 \(z=a\) 取到上界，所以径向缺陷的算子范数准确为 \(2/\sqrt\ell\)。
小算子范数与非紧性可以同时成立。

因此给这个自然嵌入添加迹类小修正，不能消去其共同Fourier的非紧缺陷。
本结论只针对这个 \(j\) 及这些实际Fourier；
允许另一来源intertwiner或已经支付准入的加权相对边界传递。
新增有限位普通电荷由511准确给
\(2\log\ell\sum_{n\ge1}h(n\log\ell)\)，是下一传递必须解释的费用。
不因这项对某个固定 \(h\) 恰为零就声称两个来源算子已相同。

## 6. 下一任务

511提供真实半局部非局部混合读出，本稿给便宜的目标符号检验。
下一阶段应攻随 \(S\) 的来源相容、遗漏素数的共同控制及真实主关系进入
[405](405-f1-adelic-restriction-moments-and-radical.md)完整双矩零混合根空间的同一主商。
若新的正性定理覆盖这些 \(f_R\)，必须指出并证明它额外使用的真实算术条件。
进一步固定 \(S\) 的谱重写不能消除(7)。
下一项便宜合同是明确(8)的来源传递及测试加权迹类边界，再检验主商；
暂不将半局部闭链晋级为RR或RH。
