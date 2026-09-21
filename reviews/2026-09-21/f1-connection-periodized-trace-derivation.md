# 连接时间的原Γ周期化迹：独立推导全文

2026-09-21。只读独立推导，原始回包见[raw](f1-connection-periodized-trace-derivation.raw.json)。本文仅添加标题和本段，并将本地路径改为仓库相对链接；结论尚须主稿整合及另一次全文审查。

**结论：收敛成立，而且可以给出原周期分布与纠正周期分布的精确系数比较及带误差界的 Dyson 展开。** 全程保留 \(P_gU_sW_s\) 的原次序，不假设 \(U_s^c\) 与 \(P_g\) 交换。

以下沿用 [414](../../notes/414-f1-deep-boundary-unitary-and-time-defect.md)、[416](../../notes/416-f1-split-transfer-and-periodic-coefficients.md) 的表示和截止。未修改文件、未运行 Git 或构建，也不重复实际 \(K\) 的系数推导。

1. **定理及记号。**

写
\[
K=\sum_{n\in F}M_{\kappa_n}P_{(n,0)},\qquad
F\subset\mathbb Z\ \text{有限},\quad
\kappa_n\in C_c^\infty(\mathbb R),\quad K^*=-K.
\]
记
\[
\ell_g=g_1L+g_2M,\qquad
r(g)=\rho_p^{|g_1|}\rho_q^{|g_2|},\qquad
\omega(g)=r(g)^{-1}.
\]
令
\[
W'_s=\beta_{-s}(K)W_s,\quad W_0=1,\qquad
U_s^c=U_sW_s.
\]
\(U^c(h)=\int h(s)U_s^c\,ds\) 首先定义为强算子积分。

则对每个固定 \(N\) 和每个 \(h\in C_c^\infty(\mathbb R)\)，
\[
\boxed{
A_N^c(h):=\sum_{g\in\Gamma}C_NP_gU^c(h)C_N
}
\]
绝对迹范数收敛。更具体地，若
\(\operatorname{supp}h\subset[-S,S]\)、\(S\ge1\)，则存在有限常数
\(B_{N,S,K,d}\)，使
\[
\boxed{
\|C_NP_gU^c(h)C_N\|_1
\le B_{N,S,K,d}\,\|h\|_{C^4}\,r(g).
}
\tag{1}
\]
常数不要求对 \(N\) 或 \(S\) 一致。

下面给出足以核验此结论、所有求和交换及标量比较的估计。

2. **Dyson 系数：群权与四阶导数同时支付。**

可以在带权系数 Banach 代数中构造 \(W_s\)：系数函数及其至四阶导数取有界一致连续函数，范数取
\[
\|a\|_{\omega,4}
=\sum_{g\in\Gamma}\omega(g)
 \sum_{j=0}^4\frac{\|\partial_t^ja_g\|_\infty}{j!}.
\]
交叉积乘法中的时间平移保持各上确界；权满足
\(\omega(g+r)\le\omega(g)\omega(r)\)。Leibniz 公式遂证明此范数次乘性。

实际解只有 \(p\)-次数，写成
\[
W_s=\sum_{n\in\mathbb Z}M_{w_n(s,\cdot)}P_{(n,0)},
\qquad
w_n=\mathbf1_{n=0}+\sum_{r\ge1}w_n^{(r)}.
\]
采用对正负 \(s\) 都有效的固定单纯形
\[
\Delta_r=\{1\ge\theta_1\ge\cdots\ge\theta_r\ge0\},
\qquad |\Delta_r|=\frac1{r!}.
\]
第 \(r\) 阶系数的明确公式为
\[
\boxed{
w_n^{(r)}(s,t)
=s^r
\sum_{\substack{n_1,\ldots,n_r\in F\\n_1+\cdots+n_r=n}}
\int_{\Delta_r}
\prod_{j=1}^r
\kappa_{n_j}\!\left(
t+s\theta_j-L\sum_{i<j}n_i
\right)d\theta .
}
\tag{2}
\]
负 \(s\) 的方向由 \(s^r\) 保留；没有把负时间错误换成正向时间排序。

设
\[
b_n=\max_{0\le j\le4}\|\kappa_n^{(j)}\|_\infty,\qquad
B_4=\sum_{n\in F}\rho_p^{-|n|}b_n,\qquad X=SB_4.
\]
对系数族定义
\[
e_{n,r}
=\max_{a+b\le4}\sup_{\substack{|s|\le S\\t\in\mathbb R}}
|\partial_s^a\partial_t^bw_n^{(r)}(s,t)|.
\]
由 (2) 得
\[
\boxed{
\sum_n\rho_p^{-|n|}e_{n,r}
\le16(r+1)^4\frac{X^r}{r!},
\qquad r\ge1.
}
\tag{3}
\]

这里每项成本可以逐一检查：

- 对 \(s^r\) 求 \(i\) 次导数，支付至多 \(r^iS^r\)；
- 对 \(r\) 个系数因子总共求 \(a-i+b\) 次导数，支付至多
  \(r^{a-i+b}\)；
- 对系数中的 \(s\) 求导只产生 \(\theta_j\)，其绝对值不超过 \(1\)；
- 累积群移位 \(L\sum_{i<j}n_i\) 与 \(s,t\) 无关，**不产生群指数因子**；
- 总指数的权由各路径指数权的乘积控制；
- 单纯形体积给出 \(1/r!\)。

因此
\[
e_n:=\max_{a+b\le4}\sup_{|s|\le S,t}
|\partial_s^a\partial_t^bw_n(s,t)|
\]
满足
\[
\boxed{
\sum_n\rho_p^{-|n|}e_n
\le
\mathcal B_4(S):=
1+16\sum_{r\ge1}(r+1)^4\frac{X^r}{r!}<\infty.
}
\tag{4}
\]
对任意更高固定阶数作同样估计，还得到系数的联合 \(C^\infty\) 光滑性。

这些 Dyson 级数在系数代数中求解给定 ODE，表示到 \(M(A)\) 后，由有界算子 ODE 的唯一性就是题设的 \(W_s\)。

3. **时间支集也有明确控制。**

取紧区间 \(J\)，同时包含所有
\[
\operatorname{supp}\kappa_n,\qquad
\operatorname{supp}\kappa_n-nL.
\]
在 (2) 的一个非零路径中，首个因子和末个因子分别要求
\[
t\in J-s\theta_1,\qquad t-nL\in J-s\theta_r.
\]
所以对 \(|s|\le S\)，
\[
t,\ t-nL\in J+[-S,S],\qquad
|n|L\le\operatorname{diam}J+S.
\tag{5}
\]
这说明本题还有一个更强的局部性质：

> 在每个有界 \(s\)-区间，\(W_s-1\) 的时间系数具有共同紧支集，而且群支也包含于一个固定有限集合。

这个有限集合允许随 \(S\) 增长。证明不需要把它当作先验假设；它由 Dyson 路径的两个端点直接得到。估计 (3)–(4) 仍有用，因为它提供了显式导数界和阶数截断误差。

4. **保持原次序后的实际核。**

令 \(P_n=P_{(n,0)}\)。直接作用于函数，而不交换 \(U_s^c\) 与 \(P_g\)，得到
\[
(P_gU_sW_s\psi)_x(t)
=\sum_n w_n(s,t-\ell_g-s)
 \psi_{x-g-(n,0)}(t-\ell_g-nL-s).
\]
置
\[
k=g+(n,0),\qquad
\sigma=t-t'-\ell_k.
\]
于是积分后的第 \(n\) 项时间核是
\[
\boxed{
h(\sigma)\,w_n(\sigma,t'+nL).
}
\tag{6}
\]
右侧的 \(t'+nL\) 至关重要，不能替换为 \(t'\)，也不能把 \(W_s\) 当作与 \(P_g\) 交换。

展开
\[
C_N=\sum_{\alpha\in\{p,q\}}E_\alpha\otimes M_{d_\alpha}.
\]
若记横向移位为
\[
V(k)=V_{p,-k_1}\otimes V_{q,-k_2},
\]
则第 \((\alpha,\beta,g,n)\) 块恰为张量积
\[
E_\alpha V(k)E_\beta\ \otimes\ Q^{\alpha\beta}_{g,n},
\]
其中时间核为
\[
q^{\alpha\beta}_{g,n}(t,t')
=d_\alpha(t)d_\beta(t')h(\sigma)
 w_n(\sigma,t'+nL).
\tag{7}
\]

本题能作这个张量分解，是因为 \(K,W_s\) 的系数只依赖时间，不依赖横向坐标。

取固定紧区间 \(I\)，使两个 \(d_\alpha\) 的支集严格位于其内部。核 (7) 在 \(I^2\) 边界附近为零。对中间函数，微分对应
\[
\partial_t=\partial_\sigma,\qquad
\partial_{t'}=-\partial_\sigma+\partial_y,
\quad y=t'+nL.
\]
因此在 \(t,t'\) 各求至多两次导数，只需 (4) 中总阶数至四的导数，并得到
\[
\max_{i,j\le2}
\|\partial_t^i\partial_{t'}^jq^{\alpha\beta}_{g,n}\|_\infty
\le C_{I,d}\|h\|_{C^4}e_n.
\tag{8}
\]
这里没有遗漏移位后的系数参数：\(e_n\) 对全部 \(y\in\mathbb R\) 取上确界；只有 \(\sigma\) 被 \(h\) 限制于 \([-S,S]\)。

将核向周期圆光滑延拓，在两个变量各分部积分两次，Fourier 矩阵元满足
\[
|\widehat q^{\alpha\beta}_{g,n}(m,l)|
\le
\frac{C_{I,d}\|h\|_{C^4}e_n}
{(1+m^2)(1+l^2)}.
\]
时间秩一展开因此给出
\[
\boxed{
\|Q^{\alpha\beta}_{g,n}\|_1
\le C'_{I,d}\|h\|_{C^4}e_n.
}
\tag{9}
\]
迹类性来自这个核估计，并非来自 \(U_s^c\) 有界或酉。

5. **支付横向求和，完成绝对迹范数收敛。**

取
\[
R=R_{N_p+1,p}\otimes R_{N_q+1,q},
\qquad E_\alpha\le R.
\]
414 的有限非负坐标基矩阵元估计给
\[
\|E_\alpha V(k)E_\beta\|_1
\le\|RV(k)R\|_1
\le A_Nr(k).
\tag{10}
\]
具体地，若 \(R\) 的基为 \(\{\zeta_\mu\}_{\mu=1}^{D_N'}\)，则先估计
\[
\sum_{\mu,\nu}
|\langle\zeta_\mu,V(k)\zeta_\nu\rangle|
\le A_Nr(k),
\]
再作有限秩一展开。\(A_N\) 已包含有限基底求和的成本；未把壳层有符号基当成非负基。

结合 (9)–(10)，四个块求和后，
\[
\|\text{第 }(g,n)\text{ 项}\|_1
\le C_{N,I,d}\|h\|_{C^4}e_n\,r(g+(n,0)).
\]
利用
\[
r(g+(n,0))\le r(g)\rho_p^{-|n|},
\]
再用 (4)，便得到定理中的 (1)。进一步，
\[
\boxed{
\sum_g\|C_NP_gU^c(h)C_N\|_1
\le C_{N,I,d}\|h\|_{C^4}\mathcal B_4(S)
\frac{1+\rho_p}{1-\rho_p}
\frac{1+\rho_q}{1-\rho_q}.
}
\tag{11}
\]
相同估计实际上控制了 \(g,n,\alpha,\beta\) 的联合绝对求和，故后续重排和逐项取迹均合法。

此外，若 \(A_N^{(r)}(h)\) 表示用 \(W_s^{(r)}\) 代替 \(W_s\) 得到的周期化，则
\[
A_N^c(h)=A_N(h)+\sum_{r\ge1}A_N^{(r)}(h)
\]
在迹范数中绝对收敛，并有可计算余项界
\[
\boxed{
\left\|A_N^c(h)-A_N(h)-\sum_{r=1}^{R}A_N^{(r)}(h)\right\|_1
\le
16C_{N,I,d}\|h\|_{C^4}\mathcal R_\rho
\sum_{r>R}(r+1)^4\frac{X^r}{r!},
}
\tag{12}
\]
其中
\[
\mathcal R_\rho=
\frac{1+\rho_p}{1-\rho_p}
\frac{1+\rho_q}{1-\rho_q}.
\]

6. **纠正周期分布的精确系数公式。**

定义实际系数函数
\[
\boxed{
F_c(s,t)=\sum_{n\in\mathbb Z}w_n(s,t+nL),
\qquad
J_\alpha(s)=\int_{\mathbb R}d_\alpha(t)^2F_c(s,t)\,dt.
}
\tag{13}
\]
由 (4)，此和及其任意固定阶导数在有界 \(s\)-区间一致绝对收敛。它只是明确的系数求和，不是交叉积上的增广同态。

因为 \(W_0=1\)，
\[
F_c(0,t)=1,\qquad J_p(0)=L,\quad J_q(0)=M.
\tag{14}
\]

现在对 (7) 取迹。交叉块的横向迹为零：
\[
\operatorname{Tr}(E_\alpha V(k)E_\beta)=0
\quad(\alpha\ne\beta).
\]
对角块的时间迹为
\[
h(-\ell_k)\int d_\alpha(t)^2
 w_n(-\ell_k,t+nL)\,dt.
\]
在已证绝对收敛后重排 \(k=g+(n,0)\)，得到
\[
\operatorname{Tr}A_N^c(h)
=
\sum_{k\in\Gamma}h(-\ell_k)
\sum_{\alpha=p,q}
\operatorname{Tr}(E_\alpha V(k)E_\alpha)\,J_\alpha(-\ell_k).
\tag{15}
\]

这里消失的是**重排后总指数 \(k\)** 的混合项，不能在开始时删除原指数 \(g\) 的混合项。

由原壳层精确迹公式，
\[
\operatorname{Tr}(E_pV(a,b)E_p)
=2\mathbf1_{b=0}
\begin{cases}
2N_p+1,&a=0,\\
\rho_p^{|a|},&a\ne0,
\end{cases}
\]
且 \(E_q\) 对称。因此，对每个固定合法 \(N\)，有精确式
\[
\boxed{
\begin{aligned}
\frac12\operatorname{Tr}A_N^c(h)
={}&D_Nh(0)\\
&+\sum_{a\ne0}\rho_p^{|a|}
 J_p(-aL)h(-aL)\\
&+\sum_{b\ne0}\rho_q^{|b|}
 J_q(-bM)h(-bM),
\end{aligned}}
\tag{16}
\]
其中原来的
\[
D_N=(2N_p+1)L+(2N_q+1)M
\]
保持不变。

与 414 原分布比较，得到
\[
\boxed{
\begin{aligned}
\frac12\operatorname{Tr}\bigl(A_N^c(h)-A_N(h)\bigr)
={}&\sum_{a\ne0}\rho_p^{|a|}
 [J_p(-aL)-L]h(-aL)\\
&+\sum_{b\ne0}\rho_q^{|b|}
 [J_q(-bM)-M]h(-bM).
\end{aligned}}
\tag{17}
\]
特别地，纠正项没有恒等时间原子。对紧支 \(h\)，(16)–(17) 中实际出现的周期点只有有限多个；这是完成原 \(\Gamma\) 求和与迹计算后的结果。

7. **比较系数的有限积分算法及误差界。**

将 (2) 代入 (13)，写
\[
J_\alpha(s)=l_\alpha+\sum_{r\ge1}J_\alpha^{(r)}(s),
\qquad l_p=L,\ l_q=M.
\]
各阶具有完全明确的有限积分公式：
\[
\boxed{
\begin{aligned}
J_\alpha^{(r)}(s)
={}&s^r\int_{\mathbb R}d_\alpha(t)^2
\int_{\Delta_r}
\sum_{n_1,\ldots,n_r\in F}\\
&\qquad\prod_{j=1}^r
\kappa_{n_j}\!\left(
t+s\theta_j+L\sum_{i=j}^rn_i
\right)d\theta\,dt.
\end{aligned}}
\tag{18}
\]
群指标只有有限集合 \(F^r\)，时间积分受 \(d_\alpha\) 的固定紧支限制。

第一阶特别为
\[
\boxed{
J_\alpha^{(1)}(s)
=
\int d_\alpha(t)^2
 \int_0^s\sum_{n\in F}\kappa_n(t+nL+r)\,dr\,dt.
}
\tag{19}
\]
负 \(s\) 仍使用有向积分。

设
\[
B_0=\sum_{n\in F}\|\kappa_n\|_\infty.
\]
不需要导数时有更简洁的余项界：
\[
|J_\alpha^{(r)}(s)|
\le l_\alpha\frac{(|s|B_0)^r}{r!},
\]
故
\[
\boxed{
\left|J_\alpha(s)-l_\alpha
-\sum_{r=1}^{R}J_\alpha^{(r)}(s)\right|
\le l_\alpha\sum_{r>R}\frac{(|s|B_0)^r}{r!}.
}
\tag{20}
\]
所以 (17) 的每个实际周期系数都能由有限阶有限积分计算，并附上显式截断误差。这里没有把某个目标算术周期差作为定义输入。

8. **Duhamel 比较成立，但须先时间平滑再取迹。**

由 \(W_s\) 的积分方程及
\[
U_s\beta_{-r}(K)W_r
=U_{s-r}K\,U_r^c,
\]
直接得到保持次序的恒等式
\[
\boxed{
U_s^c-U_s=\int_0^s U_{s-r}K\,U_r^c\,dr.
}
\tag{21}
\]
因此令
\[
\mathcal D(h)=
\int_{\mathbb R}h(s)
 \left(\int_0^s U_{s-r}K\,U_r^c\,dr\right)ds
\]
为强算子积分，则
\[
\boxed{
A_N^c(h)-A_N(h)
=\sum_g C_NP_g\,\mathcal D(h)\,C_N
}
\tag{22}
\]
在迹范数中绝对收敛。其合法性由上面针对 \(W_s-1\) 的核估计证明。

这里的顺序要求不能省略：**先完成 \(h\) 平滑，再双压缩、求和和取迹。** 不能据此声称每个固定 \((s,r)\) 的
\[
C_NP_gU_{s-r}K\,U_r^cC_N
\]
都是迹类，也不能未经证明把普通迹移入这两个时间积分。需要逐阶计算时，(12)、(18) 提供了已经在迹类空间闭合的替代步骤。

以上结论仅涉及题设的原 \(\Gamma\) 周期化迹、其连接纠正和明确比较；不涉及 \(N\) 极限、规范算术读出或相对 Chern 特征。
