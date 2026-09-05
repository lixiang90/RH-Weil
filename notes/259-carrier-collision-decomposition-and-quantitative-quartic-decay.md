# 259. Carrier--collision decomposition 与 quantitative quartic decay

日期：2026-09-04

分支：NCE-8 / 路线 B1；接口：B1q central logarithmic lag window / equal-carrier
signed Gram

状态：actual six-lag Brownian energy 的全变量 logarithmic-window truncation、精确
carrier finite-rank main term、equal-carrier collision remainder及无条件定量界
\(J_4=O(\mu^4+(\log L)/L)\) 为 [T]。真正非线性的 shape information 已缩到一个显式
local collision kernel；但该 absolute \(o(1)\) bound 不给 \(J_4=O(\mu^4)\)，也不证明
normalized actual tilt tightness。Gamma residual未并入，不声称 RH/GRH。

## 1. 从 discrepancy-only 到全部六个 lag variables

沿用笔记 258 的 one-sided measures \(\alpha_m,\beta_m\)，置

\[
 L=L_m=\log Y_m,\qquad S=S_m=A_m+B_m,\qquad
 D=D_m^{\rm raw}.
\tag{1}
\]

给定 fixed \(Q>0\)，取

\[
 H=H_m^{(Q)}=\frac{Q+4}{1-\sigma}\log L.
\tag{2}
\]

用 superscript \(H\) 表示把 one-sided source限制到 \([L-H,L+H]\)；定义

\[
 p^H=\int k_\lambda\,d\alpha^H(\lambda),\qquad
 c^H=-\int k_\lambda\,d\beta^H(\lambda),\qquad
 r^H=p^H+c^H.
\tag{3}
\]

令

\[
 J_4^H=
 \frac{\|F_{r^H*r^H*p^H}\|_2^2+
 \|F_{r^H*r^H*c^H}\|_2^2}{S^4D}.
\tag{4}
\]

注意 denominator仍是 full-source normalization；这使 tail error 与原 \(J_4\) 可直接
比较。

### 引理 259-A（weighted six-variable tail truncation）[T]

对每个 fixed \(Q>0\)，

\[
 \boxed{|J_{4,m}-J_{4,m}^H|=O_{\sigma,Q}(L_m^{-Q}).}
\tag{5}
\]

#### 证明

笔记 258-C 的同一 dyadic argument在 integrand 中多放一个
\(1+\lambda/L\)，给

\[
 \int_{|\lambda-L|>H}
 \left(1+\frac{\lambda}{L}\right)
 d(\alpha_m+\beta_m)(\lambda)
 =O_{\sigma,Q}(SL^{-Q-3}).
\tag{6}
\]

低 lag处 \(\lambda/L\le1\)；高 lag处新增的 logarithm仍被
\(\exp(-e^{\lambda-L})\) 吸收。另一方面，笔记 258-(12) 的 atomic representation给

\[
 |\mathcal B(\lambda,\mu)|
 \le32\left(\lambda_1+\lambda_2+\lambda_3
             +\mu_1+\mu_2+\mu_3\right),
\tag{7}
\]

因为每个 triple kernel 的 coefficient absolute sum为
\((1/2+1+1/2)^3=8\)。在 full sixfold product减 central product 的 telescoping
展开中，每项至少有一个 tail variable；式 (6) 控制该 variable，其余五个 variables
的 total variation至多贡献 \(S^5\)。所以 unnormalized energy difference为
\(O(S^6L^{-Q-2})\)。笔记 255-C 给

\[
 S^4D\asymp LS^6
\tag{8}
\]

这里还须控制 kernel中落在非 tail variable上的 lag。由式 (6)，
\(\int\lambda\,d(\alpha+\beta)\le(L+H)S+
L\int_{I^c}(1+\lambda/L)d(\alpha+\beta)=O(LS)\)，其中 \(I=[L-H,L+H]\)。
因此上述每一项的 first-moment积分也被控制，不能只引用 total variation。
（式 (8)使用 qualitative PNT 使 \(A_m/B_m\to1\)。）
实际得到 \(|J_4-J_4^H|=O(L^{-Q-3})\)，故式 (5)成立。 \(\square\)

该引理截断 \(\alpha,\beta\) 的全部六个 copies，而不只截断笔记 258-E 的两个
discrepancy factors；因此下面每个 lag都可写成 \(L+\) small offset。

## 2. Carrier index 的精确有限枚举

置

\[
 \mathcal E=\{-1,0,1\}^3,\qquad
 w(-1)=w(1)=\frac12,\qquad w(0)=-1,
\]

\[
 \omega(e)=\prod_{j=1}^3w(e_j),\qquad q(e)=e_1+e_2+e_3.
\tag{9}
\]

若 \(\lambda_j=L+u_j\)，则

\[
 K_\lambda=\sum_{e\in\mathcal E}
 \omega(e)\delta_{q(e)L+e\cdot u}.
\tag{10}
\]

carrier-sector masses \(c_q=\sum_{q(e)=q}\omega(e)\) 为

\[
 (c_{-3},c_{-2},c_{-1},c_0,c_1,c_2,c_3)
 =\left(\frac18,-\frac34,\frac{15}8,-\frac52,
          \frac{15}8,-\frac34,\frac18\right).
\tag{11}
\]

### 定理 259-B（exact carrier--collision kernel decomposition）[T]

若 \(|u_j|,|v_j|\le H\) 且 \(6H<L\)，则

\[
 \boxed{
 \mathcal B_L(u,v)
 =\frac{63}{16}L
 +\frac{21}{32}\left(\sum_{j=1}^3u_j+\sum_{j=1}^3v_j\right)
 +\mathcal C(u,v),}
\tag{12}
\]

其中唯一的 nonlinear collision kernel 是

\[
 \boxed{
 \mathcal C(u,v)=
 -\frac12
 \sum_{\substack{e,f\in\mathcal E\\q(e)=q(f)}}
 \omega(e)\omega(f)|e\cdot u-f\cdot v|.}
\tag{13}
\]

并且

\[
 \boxed{|\mathcal C(u,v)|\le192H.}
\tag{14}
\]

#### 证明

由式 (10) 与 Brownian distance identity，

\[
 \mathcal B_L(u,v)=-\frac12
 \sum_{e,f}\omega(e)\omega(f)
 |(q(e)-q(f))L+e\cdot u-f\cdot v|.
\]

当 \(q(e)\ne q(f)\) 时，\(|e\cdot u-f\cdot v|\le6H<L\)，绝对值的 sign由
\(q(e)-q(f)\) 固定，故该项对 \(L,u,v\) 完全线性。相同 carrier项正是式 (13)。

由式 (11) 直接有限求和，

\[
 -\frac12\sum_{q,r=-3}^3c_qc_r|q-r|=\frac{63}{16}.
\tag{15}
\]

三个 coordinates 的 permutation symmetry与
\(\mathcal B_L(u,v)=\mathcal B_L(v,u)\) 使六个 offset coefficients相等；把
\(u_1=u_2=u_3=v_1=v_2=v_3=h\) 时 kernel按 common scaling变成
\((L+h)63/16\)，故每个 coefficient为 \((63/16)/6=21/32\)。这证明式 (12)。

最后 \(\sum_e|\omega(e)|=8\)，而 equal-carrier项仍满足
\(|e\cdot u-f\cdot v|\le6H\)；故式 (13) 的 absolute sum至多
\((1/2)8^2(6H)=192H\)。 \(\square\)

## 3. 有限秩 main term 与 local signed collision Gram

记 central masses

\[
 A_H=\alpha^H(\mathbb R),\qquad
 B_H=\beta^H(\mathbb R),\qquad M_H=A_H-B_H,
\tag{16}
\]

以及 centered first lag moments

\[
 a_1=\int(\lambda-L)d\alpha^H(\lambda),\qquad
 b_1=\int(\lambda-L)d\beta^H(\lambda),\qquad
 d_1=a_1-b_1.
\tag{17}
\]

令
\(\Gamma_p^H=(\alpha^H-\beta^H)\otimes(\alpha^H-\beta^H)\otimes\alpha^H\)，
并以 \(\beta^H\) 替换最后一项定义 \(\Gamma_c^H\)。

### 定理 259-C（exact finite-rank main plus collision ledger）[T]

有

\[
 \boxed{S^4D J_4^H=\mathcal Q_{\rm car}+\mathcal Q_{\rm coll},}
\tag{18}
\]

其中

\[
\boxed{
\begin{aligned}
 \mathcal Q_{\rm car}=\frac{63}{16}\bigg[{}
 &L M_H^4(A_H^2+B_H^2)\\
 &+\frac23M_H^3(A_H^2+B_H^2)d_1\\
 &+\frac13M_H^4(A_Ha_1+B_Hb_1)
 \bigg],
\end{aligned}}
\tag{19}
\]

而

\[
\boxed{
\begin{aligned}
 \mathcal Q_{\rm coll}={}&
 \iint\mathcal C(u,v)d\Gamma_p^H(u)d\Gamma_p^H(v)\\
 &+\iint\mathcal C(u,v)d\Gamma_c^H(u)d\Gamma_c^H(v).
\end{aligned}}
\tag{20}
\]

#### 证明

\(\Gamma_p^H\) 的 total mass与 total offset sum分别为

\[
 g_{p,0}=M_H^2A_H,\qquad
 g_{p,1}=2M_HA_Hd_1+M_H^2a_1.
\tag{21}
\]

所以式 (12) 的 carrier部分在
\(\Gamma_p^H\otimes\Gamma_p^H\) 下积分为

\[
 \frac{63}{16}\left(Lg_{p,0}^2+\frac13g_{p,0}g_{p,1}\right).
\]

以 \(B_H,b_1\) 替换 \(A_H,a_1\) 得 continuum channel。两式相加并展开，得到
式 (19)；equal-carrier项按定义给式 (20)。 \(\square\)

式 (19) 只依赖 mass与 first lag moments，是 finite-rank carrier block；全部 higher
shape information只存在于式 (20)。

### 推论 259-D（collision budget 与 unconditional quartic rate）[T]

有

\[
 \boxed{|\mathcal Q_{\rm coll}|\le
 192H S^4(A_m^2+B_m^2).}
\tag{22}
\]

进而

\[
 \boxed{
 J_{4,m}=O_{\sigma,Q}\left(\mu_m^4+\frac{\log L_m}{L_m}\right).}
\tag{23}
\]

特别地，由 qualitative PNT 的 \(\mu_m\to0\)，

\[
 \boxed{
 J_{4,m}=O_\sigma\left(\mu_m^4+\frac{\log L_m}{L_m}\right)=o(1).}
\tag{24}
\]

#### 证明

\(\|\alpha^H-\beta^H\|_{\rm TV}\le S\)，所以

\[
 \|\Gamma_p^H\|_{\rm TV}\le S^2A_m,\qquad
 \|\Gamma_c^H\|_{\rm TV}\le S^2B_m.
\]

式 (14) 给式 (22)。又由 tail bound，
\(M_H/S=\mu_m+O(L^{-Q-3})\)，并且

\[
 |a_1|\le HA_m,\qquad |b_1|\le HB_m,\qquad |d_1|\le HS.
\tag{25}
\]

把式 (19)、(22)、(25)除以式 (8)，再用引理 259-A，得到

\[
 J_{4,m}=O\left(
 \mu_m^4+|\mu_m|^3\frac HL+\frac HL+L^{-Q-3}\right).
\]

因为 \(|\mu_m|\le1\)、\(H\asymp\log L\)，得到式 (23)--(24)。 \(\square\)

## 4. Main constant 的 normalization check

若两个 sources 的所有 lag都恰等于 \(L\)，则
\(a_1=b_1=d_1=0\)、collision term为零，且

\[
 D=\frac L2(A^2+B^2).
\]

式 (18)--(19) 因而给

\[
 \boxed{J_4=\frac{63}{8}\mu^4.}
\tag{26}
\]

frequency side也给相同结果：\(\Delta=\mu(1-\cos(L\xi))\)，而 \(\nu\) 的 density
多一个 \((1-\cos)^2\)；比例正是 Brownian integrals of \((1-\cos)^6\) 与
\((1-\cos)^2\) 的比。这个 check独立确认 \(63/16\) 的 carrier常数与
even-centering factor。

## 5. 已缩小的开放算术输入

推论 259-D 比笔记 255 的 qualitative \(J_4\to0\) 给出显式 unconditional rate，但通常

\[
 \frac{\log L}{L}\ne O(\mu_m^4).
\]

因此它不闭合笔记 256 的 mass-relative criterion。真正剩余的对象不是 arbitrary
sixfold moment，而是式 (20) 的 equal-carrier signed Gram。要恢复
\(J_4=O(\mu^4)\)，截断模型的一个充分 response-specific input 是

\[
\boxed{
|\mathcal Q_{\rm coll}|
 +|M_H|^3(A_H^2+B_H^2)|d_1|
 +|M_H|^4|A_Ha_1+B_Hb_1|
\ll L M_H^4(A_H^2+B_H^2).}
\tag{27}
\]

该条件为 [O]，只控制 \(J_4^H\) 与 \((M_H/S)^4\)。要推出 full-source
\(J_4=O(\mu^4)\)，还须下述质量相对 tail条件；任意固定幂次 absolute tail
估计本身不够。逐项 absolute bound只重现式 (22) 的 \(H/L\) ceiling。

### 2026-09-05 独立审计修正：relative tail transfer [T/N]

令 \(\tau=\alpha+\beta\)，并记
\[
 t=\frac{\tau(I^c)}S,\qquad
 \ell=\frac{\int_{I^c}\lambda\,d\tau}{LS}.
\]
若 \(D\ge cLS^2\)，则
\[
 \left|\sqrt{J_4}-\sqrt{J_4^H}\right|
 \le8t+4\sqrt{\frac{t\ell}{2c}}\le C_c(t+\ell).
\]
证明：两通道组成 Hilbert空间中的向量。在各通道中写
\[
 r*r*p-r^H*r^H*p^H
 =(r-r^H)*(r+r^H)*p+r^H*r^H*(p-p^H).
\]
第一项用 Young不等式及
\(\|r-r^H\|_{\rm TV}\le2St,\ \|r+r^H\|_{\rm TV}\le4S\)，
归一化后贡献至多 \(8t\)。第二项贡献至多
\(4\sqrt{D_{\rm tail}/D}\)，这里
\(D_{\rm tail}=\|F_{p-p^H}\|_2^2+\|F_{c-c^H}\|_2^2\)。
由正源的 minimum-of-two identity，
\[
 D_{\rm tail}\le\frac12
 \sum_{\gamma=\alpha,\beta}\gamma(I^c)
               \int_{I^c}\lambda\,d\gamma
 \le\frac12 LS^2t\ell.
\]
两通道求和及三角不等式给结论。

因此 (27) 加上 \(t+\ell=O(\mu^2)\) 是 full-source充分条件。
它同时给 \(|M_H/S-\mu|\le t=O(\mu^2)\)。
若另有 \(|\mu|\ge c_0L^{-r}\)，可选固定 \(Q+3\ge2r\) 闭合此条件；
当前未证明这种质量差下界。

后续263已在实际matched Abel系数上证明更强的停止结论：
定量PNT给 \(\mu=O_K(L^{-K})\) 对每个固定 \(K\) 成立，而
任意 \(H=O(\log L)\) 窗口的正连续尾迫使
\(\mu^2/(t+\ell)\to0\)，一致覆盖所有 \(N\ge Y\)。
因此上述对数幂质量下界在实际族中不成立，固定 \(Q\) 的
\(t+\ell=O(\mu^2)\) 证书不能闭合。
原relative upper bound及absolute decay定理保持有效；
下一输入改为带符号响应差本身，不能从证书失败推断实际响应转移失败。

严格逻辑反例：取 \(L>6H>0,\ \epsilon=e^{-L}\)，
\[
 \alpha=\delta_L+\epsilon\delta_{L-2H},\qquad
 \beta=\delta_L+\epsilon\delta_{L-3H}.
\]
此时 \(\mu=M_H=0\)，central sources完全相同，所以 (27)成立；
tails小于任意固定负幂。然而
\(r=\epsilon(k_{L-2H}-k_{L-3H})\ne0\)，且 \(p\ne0\)。
其 Fourier transforms为非零解析函数，乘积 \(\widehat r^{\,2}\widehat p\)
不恒为零，故 \(J_4>0\)。这否定了旧版未附 relative tail条件的推论。
反例属于一般正源模型，不是 actual von Mangoldt源反例。

另一方面，如果 \(\mathcal Q_{\rm coll}\) 有远大于 carrier main 的 positive lower，
并且其 physical 频率集中于 \(|t|\ge m/\log L\)，则应转向 actual escape theorem，
而不是继续追求 mass-relative bound。当前没有证明这两个方向中的任一个。

## 6. 最小输入、删除与循环性审计

最小输入：

1. [T] actual centered triple coefficient ledger（笔记 258）；产生 27-state carrier
   representation；
2. [T] Abel lag-tail envelope；允许全部六 variables进入 \(O(\log L)\) 窗；
3. [T] separation \(6H<L\)；使 unequal carriers 的 absolute-value kernel精确线性；
4. [T] 27-state finite sum；给 \(63/16\)、\(21/32\) 与 collision kernel；
5. [R] qualitative PNT；只用于 raw normalization (8) 与 \(\mu_m\to0\)；
6. [T] total-variation bound；只给 collision 的 absolute \(H/L\) ceiling。

删除审计：

- 删除 full six-variable truncation，third source factor可能跨 carrier cells，式 (12)
  不可统一使用；
- 删除 \(6H<L\)，unequal-carrier absolute values也会产生 nonlinear collisions；
- 删除 equal-carrier block，错误地只保留 finite-rank main，会把全部 shape
  discrepancy 抹掉；
- 对 signed collision逐项取 absolute value，只得到式 (22)，不能达到式 (27)；
- 把 \(J_4=o(1)\) 当 \(J_4=O(\mu^4)\)，在 \(\mu\) 很小时量词错误；
- 把 absolute energy rate (24) 当 normalized probability tightness，仍缺 denominator
  lower；
- 把 two-channel collision ledger称为 Gamma-complete response，缺少独立 bridge。

非同义反复：carrier constants来自 actual 27-state centered atoms 的精确 finite sum；
collision block由相同 carrier indices强制产生，并可被具体 short-interval coefficients
检验。公理中没有包含 desired capture、\(J_4=O(\mu^4)\) 或 collision cancellation。

循环性审计：已证结论只用 qualitative PNT、Abel tails、有限 signed convolution、
absolute-value Brownian kernel与 elementary TV bounds；不使用 zeros、RH/GRH、PNT
平方根误差、Weil positivity、谱酉性、bounded negative index、四矩猜想或紧性完备化。

## 7. 模型范围与下一最小引理 B1r

- Riemann zeta：全部公式直接适用于 matched sign-pure subsystem；
- Dedekind zeta：carrier algebra不变，raw normalization需 prime-ideal theorem；
- Dirichlet/automorphic L：carrier decomposition保留，但 collision measures成为
  phase/matrix-valued；
- 函数域：degree lattice使 carrier sectors离散且可能进一步 exact orthogonalize；
- 一般 spectral models：只要 lag envelope使 \(H=o(L)\)，259-B--C 纯几何保留；
- 论文归属：与笔记 242--258 同属 Vaughan--Brownian response论文，是从 global
  sixfold integral到唯一 local arithmetic Gram 的核心结构节。

B1q 已把 central six-lag kernel精确拆成 finite-rank carrier main 与 local collision。
后续笔记260已完成 B1r：式 (20) 的七扇区全部展开，精确平衡时得到
与四阶 discrepancy卷积能量之间的双边最优常数 \(3/8,11/16\)，并给非平衡扰动界。
下一最小引理 B1s 是实际二阶/四阶 discrepancy能量与质量差的统一比较，
同时控制本笔记修正后的相对tails。不得把式 (27)作为未经证明的 positivity axiom。
