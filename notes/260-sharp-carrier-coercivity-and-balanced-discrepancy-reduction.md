# 260. 七扇区 sharp coercivity 与平衡 discrepancy 归约

日期：2026-09-05

路线：NCE-8 / B1r。论文归属：Vaughan--Brownian response。

状态：[T] 七扇区卷积公式；[T] 精确平衡时的双边最优常数 \(3/8,11/16\)；
[T] 非平衡响应到二阶、四阶平衡 discrepancy 能量的显式归约；
[N] 固定宽度局部正源的 mass-only budget障碍。
真实 von Mangoldt系数上的相对能量估计仍为 [O]。不声称 RH/GRH、零点比例纪录
或文献意义上的新颖性已经确认。

## 1. 局部模型与能量

令 \(\alpha,\beta\) 是 offset区间 \([-H,H]\) 上有限实正测度，
\(A=\alpha(\mathbb R)>0,\ B=\beta(\mathbb R)>0\)，并置
\[
 M=A-B,\quad S=A+B,\quad K=A^2+B^2,\quad \mu=M/S,\quad L>6H.
\tag{1}
\]
本笔记所有 source变量都是 offset \(u\)；其 physical lag为 \(L+u\)。
记反射测度为 \(\check\eta\)，\(k_\lambda=(\delta_\lambda+\delta_{-\lambda})/2-\delta_0\)，
\[
 r_\eta=\int k_{L+u}\,d\eta(u),\quad
 p=r_\alpha,\quad c=-r_\beta,\quad r=p+c,\quad \rho=\alpha-\beta.
\tag{2}
\]
定义
\[
 D=\|F_p\|_2^2+\|F_c\|_2^2,\quad
 P^2=\|F_{r*r*p}\|_2^2+\|F_{r*r*c}\|_2^2,\quad
 J_4=\frac{P^2}{S^4D}.
\tag{3}
\]
这里 \(F_\eta(x)=\eta((-\infty,x])\)，只对零总质量测度直接使用其全轴 \(L^2\) 范数。

对任意紧支撑实 signed measure定义距离二次型
\[
 \mathcal E(\eta)=-\frac12\iint|x-y|\,d\eta(x)d\eta(y).
\tag{4}
\]
若 \(\eta(\mathbb R)=0\)，则
\[
 \mathcal E(\eta)=\|F_\eta\|_2^2
 =\frac1{2\pi}\int_{\mathbb R}\frac{|\widehat\eta(\xi)|^2}{\xi^2}\,d\xi\ge0.
\tag{5}
\]
证明：\(|x-y|\) 是两个半直线 indicator之差的平方积分；展开后利用
\(\int d\eta=0\) 消掉两个单变量项，得第一个等式。
分布导数 \(F_\eta'=\eta\) 与 Plancherel给第二个等式。
非零质量时 (4)仍有意义，但 (5)一般不成立。

两个将反复使用的 elementary identities为
\[
 \mathcal E(\rho*\check\rho)=\mathcal E(\rho*\rho),\qquad
 \|F_{\eta*\tau}\|_2\le T\|F_\eta\|_2,
\tag{6}
\]
其中第一个等式要求 \(\rho\) 实且质量为零，第二个要求 \(\eta\) 质量为零、
\(\tau\ge0,\ \tau(\mathbb R)=T\)。前者由 (5) 两边同为
\((2\pi)^{-1}\int|\widehat\rho|^4/\xi^2\)；
后者由 \(F_{\eta*\tau}(x)=\int F_\eta(x-y)d\tau(y)\) 与 Cauchy--Schwarz证明。

## 2. 七个 carrier测度的精确公式 [T]

对 \(\tau=\alpha\) 或 \(\beta\)，记 \(T=\tau(\mathbb R)\)。在以卷积为乘法的
测度代数中展开 Laurent polynomial
\[
 \left(\frac z2\rho-M\delta_0+\frac{z^{-1}}2\check\rho\right)^2
 *
 \left(\frac z2\tau-T\delta_0+\frac{z^{-1}}2\check\tau\right)
 =\sum_{q=-3}^3z^q\nu_{q,\tau}.
\tag{7}
\]
逐项相乘给
\[
\begin{aligned}
 \nu_3={}&\tfrac18\rho*\rho*\tau,\\
 \nu_2={}&-\tfrac T4\rho*\rho-\tfrac M2\rho*\tau,\\
 \nu_1={}&\tfrac18\rho*\rho*\check\tau+MT\rho+
                \tfrac{M^2}2\tau+\tfrac14\rho*\check\rho*\tau,\\
 \nu_0={}&-\tfrac M2(\rho*\check\tau+\check\rho*\tau)
              -TM^2\delta_0-\tfrac T2\rho*\check\rho,
 \qquad \nu_{-q}=\check\nu_q.
\end{aligned}
\tag{8}
\]
例如 \(q=1\) 来自 \((1,0,0),(0,1,0),(0,0,1)\) 与
\((1,1,-1),(1,-1,1),(-1,1,1)\) 六种 choices；
其余 \(q\) 同理。这是 27个 centered-atom choices的完整分组。

\(\nu_q\) 支撑在 \([-3H,3H]\)，质量为 \(c_qM^2T\)，其中
\[
 (c_{-3},\ldots,c_3)=(1/8,-3/4,15/8,-5/2,15/8,-3/4,1/8).
\]
用 \(\mathsf T_a\) 表示平移，则
\(r*r*r_\tau=\sum_q\mathsf T_{qL}\nu_{q,\tau}\)。
因 \(L>6H\)，不同 carrier支撑不交。笔记259中的 remainder精确为
\[
 Q_{\rm coll}=\sum_{\tau=\alpha,\beta}\sum_{q=-3}^3\mathcal E(\nu_{q,\tau}).
\tag{9}
\]
式 (9)由 (4)、(7) 的有限展开得到；当 \(M\ne0\) 时不得将每一项称为非负能量。

## 3. 平衡 coercivity与最优常数 [T]

### 定理260-A

若 \(M=0\)，则
\[
 \boxed{\frac38 K\,\mathcal E(\rho*\rho)
 \le P^2=Q_{\rm coll}
 \le\frac{11}{16}K\,\mathcal E(\rho*\rho).}
\tag{10}
\]
两常数在有限实正源、固定 offset支撑区间的类中均最优。
更一般地，式 (10) 对任何支撑在 \([-H,H]\) 的有限实质量零测度 \(\rho\) 及两个独立正通道
\(\alpha,\beta\) 成立，只须把 \(P\) 中的 \(r\) 换为 \(r_\rho\)；
不要求此时 \(\rho=\alpha-\beta\)。

证明：\(M=0\) 时所有 \(\nu_q\) 质量为零。不同 carrier的 primitives支撑不交，
故 \(P^2\) 是 (9) 的正和；同样可从259的 \(Q_{\rm car}=0\) 得到。
置 \(\sigma_2=\rho*\rho,\ \sigma_{1,1}=\rho*\check\rho\)。
对每个通道，\(q=0,\pm2\) 的能量之和精确为
\[
 \frac{T^2}{4}\mathcal E(\sigma_{1,1})
 +\frac{T^2}{8}\mathcal E(\sigma_2)
 =\frac38T^2\mathcal E(\sigma_2).
\tag{11}
\]
其余四个 sector给恒等式
\[
 Q_\tau=\frac38T^2\mathcal E(\sigma_2)
 +2\mathcal E\!\left(\tfrac18\sigma_2*\check\tau+
                         \tfrac14\sigma_{1,1}*\tau\right)
 +2\mathcal E\!\left(\tfrac18\sigma_2*\tau\right).
\tag{12}
\]
非负性给下界。由 (6) 两个剩余 primitive的范数分别不超过
\((3T/8)\sqrt{\mathcal E(\sigma_2)}\) 与
\((T/8)\sqrt{\mathcal E(\sigma_2)}\)。
所以常数为 \(3/8+2(9/64+1/64)=11/16\)。两通道相加即 (10)。

下界最优性：取 \(u=\frac12{\bf1}_{[-1,1]}dx,\ h=1/n,\ n\ge2\)，
\[
 \alpha_n=\delta_h+nu,\qquad \beta_n=\delta_{-h}+nu.
\tag{13}
\]
此时 \(A=B=n+1,\ \rho=\delta_h-\delta_{-h}\)，
\(\sigma_2=\delta_{2h}-2\delta_0+\delta_{-2h}\)，且
\[
 \mathcal E(\sigma_2)=4h,\qquad
 \mathcal E(\sigma_2*u)=\frac83h^3.
\tag{14}
\]
后一式可以直接积分：\(F_{\sigma_2}\) 是
\({\bf1}_{[-2h,0)}-{\bf1}_{[0,2h)}\)；与 \(u\) 卷积后在 \(\pm1\) 处形成两个
底宽 \(4h\)、高度 \(h\) 的三角形，平方积分各为 \(4h^3/3\)。
又有 \(\sigma_{1,1}=-\sigma_2\)。由 (12)、三角不等式及 (14)，
剩余四个 sector总能量是 \(O(h+n^2h^3)=O(1/n)\)，
而 \(K\mathcal E(\sigma_2)=8(n+1)^2/n\)。
故比值趋于 \(3/8\)。全部 offsets仍在 \([-1,1]\)，可以固定 \(L>6\)。

上界最优性：固定 \(0<h\le1\)，取
\[
 \alpha_n=n\delta_0+\delta_h+\delta_{-h},\qquad
 \beta_n=(n+2)\delta_0.
\tag{15}
\]
\(\rho=\delta_h+\delta_{-h}-2\delta_0\) 为非零偶测度，因而
\(\sigma_{1,1}=\sigma_2\)。\(\beta\) 通道在 (12) 中精确达到 \(11/16\)。
\(\alpha_n/(n+2)\to\delta_0\) 于 total variation；
式 (6) 的 signed-TV版本使两个剩余 primitive在归一化后收敛，
故 \(\alpha\) 通道也趋于该常数。最优性得到证明。
两组例子均可同时缩放 \(\alpha,\beta\) 使 \(A=B=1\)，比值不变。 \(\square\)

### 推论260-B：局部 mass-only budget障碍 [T/N]

在精确平衡的非零正源模型中，\(P=0\) 当且仅当 \(\alpha=\beta\)。
确实，由 (10)，\(P=0\) 蕴含 \(\mathcal E(\rho*\rho)=0\)；
式 (5)给 \(\widehat\rho^{\,2}=0\)，Fourier唯一性给 \(\rho=0\)。

具体地，\(\alpha=\delta_h,\ \beta=\delta_{-h},\ 0<h\le H\) 时，
每个通道的 \((q=0,1,2,3)\) 能量为
\((h,7h/16,h/4,h/16)\)，所以
\[
 P^2=5h,\quad D=\tfrac12(L+h)+\tfrac12(L-h)=L,\quad
 J_4=\frac{5h}{16L},\quad \mu=0.
\tag{16}
\]
因此即使固定 \(h\)、所有 lags都在固定宽窗口内，正源与质量匹配也不能推出
\(J_4=O(\mu^4)\)。它同时说明仅靠局部支撑几何不能把 absolute \(O(H/L)\)
ceiling改为 \(o(H/L)\)。
这是正源结构障碍；它并未证明未经重标定的 von Mangoldt源满足相同下界。

## 4. 非平衡响应的二阶/四阶 discrepancy归约 [T]

定义真正质量零的 offset discrepancy
\[
 \zeta=\alpha-\frac AB\beta,\qquad
 E_1=\mathcal E(\zeta),\quad E_2=\mathcal E(\zeta*\zeta).
\tag{17}
\]
两个量都直接由 source coefficients定义：
\[
\begin{aligned}
 E_1&=\frac1{2\pi}\int\frac{|\widehat\zeta(\xi)|^2}{\xi^2}\,d\xi,\\
 E_2&=\frac1{2\pi}\int\frac{|\widehat\zeta(\xi)|^4}{\xi^2}\,d\xi
 =-\frac12\int |u_1+u_2-v_1-v_2|\,
        d\zeta(u_1)d\zeta(u_2)d\zeta(v_1)d\zeta(v_2).
\end{aligned}
\tag{18}
\]
令 \(P_0\) 为 (3) 中仅将 \(r\) 换成 \(r_\zeta\) 所得向量范数，
仍保留原来的 \(p,c\) 通道和 \(D\)。

### 定理260-C

有
\[
 \sqrt{3KE_2/8}\le P_0\le\sqrt{11KE_2/16},\qquad
 \boxed{|P-P_0|\le4\sqrt2\,|M|\sqrt{KE_1}+4M^2\sqrt D.}
\tag{19}
\]
证明：第一部分是260-A的一般版本。
又 \(r=r_\zeta+(M/B)r_\beta\)。\(r_\zeta\) 的两个平移测度质量均为零且支撑不交，
故 \(\|F_{r_\zeta}\|_2^2=E_1/2\)。
展开
\[
 r*r-r_\zeta*r_\zeta
 =2(M/B)r_\zeta*r_\beta+(M/B)^2r_\beta*r_\beta.
\]
对两个通道一起应用 Young不等式。
第一项使用 \(\|r_\beta\|_{\rm TV}\le2B\) 及通道TV向量范数至多 \(2\sqrt K\)，
得到 \(2|M|B^{-1}(2B)(2\sqrt K)\sqrt{E_1/2}=4\sqrt2|M|\sqrt{KE_1}\)。
第二项把 \(r_\beta*r_\beta\) 当卷积测度，得到
\((M/B)^2(2B)^2\sqrt D=4M^2\sqrt D\)。
向量范数三角不等式给 (19)。 \(\square\)

若 \(M\ne0\)，置
\[
 d=\frac D{LK},\qquad x=\frac{E_2}{LM^4},\qquad y=\frac{E_1}{LM^2}.
\tag{20}
\]
由 minimum-of-two identity，
\((L-H)K/2\le D\le(L+H)K/2\)，所以 \(d\) 一致远离零。
除以 \(M^2\sqrt D\)，得到完全显式的界
\[
 \boxed{
 \left(\sqrt{\frac{3x}{8d}}-4\sqrt{\frac{2y}{d}}-4\right)_+^2
 \le\frac{J_4}{\mu^4}\le
 \left(\sqrt{\frac{11x}{16d}}+4\sqrt{\frac{2y}{d}}+4\right)^2.}
\tag{21}
\]

因此对于任何这样的紧支撑源族：

- [C] 若 \(E_1=O(LM^2),\ E_2=O(LM^4)\)，则 \(J_4=O(\mu^4)\)；
- [C/N] 若 \(E_2/(M^2E_1+LM^4)\to\infty\)，则 \(J_4/\mu^4\to\infty\)。
  证明是 (21) 中 \(x/(y+1)\to\infty\)，故下界趋于无穷。

这里只把条件性应用标作 [C]；两条 implication本身已由 (21) 完整证明。
没有声称 \(x,y\) 有界是必要条件，也没有忽略 \(M=0\) 的单独情形。

## 5. 算术接口、截断误差与下一最小引理

将笔记258的实际 \(\alpha_m,\beta_m\) 限制到 \([L-H,L+H]\) 后平移到
\([-H,H]\)，即可使用以上定理。所有 \(A,B,M,D\) 此时均为这个局部模型的量，
不能与 full-source mass自动混用。实际新对象是
\[
 \widehat\zeta_m(\xi)=
 \int e^{-i\xi(\lambda-L)}d\alpha_m^H(\lambda)
 -\frac{A_H}{B_H}\int e^{-i\xi(\lambda-L)}d\beta_m^H(\lambda).
\tag{22}
\]
它是可核查的 weighted von Mangoldt sum减连续积分。
式 (18) 将六份源的响应积分压缩到两份及四份 discrepancy copies，
并消去了第三个 source通道的细节，只留下 \(K\) 和显式扰动。

为明确区分分母，令本笔记在截断源上计算的量为
\[
 J_{\rm loc}=\frac{P_H^2}{S_H^4D_H},\qquad
 J_4^H=\frac{P_H^2}{S^4D}
      =\left(\frac{S_H}{S}\right)^4\frac{D_H}{D}\,J_{\rm loc}.
\]
其中 \(S_H=A_H+B_H,\ D_H\) 是局部raw分母，而 \(S,D\) 为 full-source量。
正源的 minimum kernel给 \(D_H\le D\)，所以
\(J_{\rm loc}=O((M_H/S_H)^4)\) 蕴含 \(J_4^H=O((M_H/S)^4)\)。

Full-source转移还须笔记259的2026-09-05修正：
若 normalized tail mass/first moment之和是 \(t+\ell\)，则
\(|\sqrt{J_4}-\sqrt{J_4^H}|\le C(t+\ell)\)。
要从局部 \(O((M_H/S_H)^4)\) 推出 full-source \(O(\mu^4)\)，需要
\(t+\ell=O(\mu^2)\) 或直接的相对响应误差估计。
任意固定 \(O(L^{-Q})\) 误差不能覆盖任意小的 \(\mu\)。

B1r 晋级：七个 sectors与双边最优常数已经闭合，跨 sector抵消在精确平衡时
被 (12) 排除。下一最小引理 **B1s**：
对实际 (22) 证明 \(E_2\) 相对 \(M_H^2E_1+LM_H^4\) 的一个统一比较，
同时按 full \(\mu_m^2\) 量级核对 tail budget。
可以先证明明确尺度或子族上的 lower以停止 mass-only方案，
也可以通过独立算术界控制 \(x,y\)。只有 fixed-frequency PNT或正源TV界不算晋级。

## 6. 最小假设、删除审计与模型范围

最小输入及作用：

1. 紧支撑有限实测度：保证所有距离积分可交换、反射的 Fourier共轭公式成立；
2. \(L>6H\)：分离 carrier primitives，使平衡响应精确等于 sector能量和；
3. 质量零：将 (4) 变成非负 (5)，这是显式可计算的线性等式；
4. 通道正性：给 (6) 的质量 \(T\) 范数预算；
5. \(B>0\)：定义 (17)；无非构造性完备化假设。

删除时的失效点：非零sector质量不能应用 (5)；
支撑重叠时全物理能量包含跨sector项；复数 \(\rho\) 时必须重新建立 Hermitian版本；
signed通道的 total variation可远大于其质量，(10) 的上界证明失效。
若 \(\rho=0\)，所有能量为零，定理包括此退化情形；
若 \(M=0\)，(21)不定义，须用260-A--B。

循环性：上述 [T/N] 完全不使用零点、函数方程、RH、PNT误差、
完整 Weil正性或负指数一致有界。正性是 (5) 的 elementary identity，
不是针对 Weil显式公式的假定。与广义 Weil配置的接口只在笔记256的条件
capture/Schur归约；从本响应子系统到 Gamma-complete显式公式仍是独立开放桥梁。

模型范围：Riemann与 Dedekind系数若给实正局部源，则代数定理直接适用；
算术估计须各自证明。函数域的 degree-lattice源同样适用离散版本；
Dirichlet/一般自守复系数尚需 Hermitian推广。
固定窗口反例只排除“质量匹配+局部支撑+正源”这一普遍推理，
未排除实际 zeta结构存在性。

## 7. 复算与文献边界

运行 scripts/carrier_sector_coercivity_audit.py。它用 Fraction精确比较
physical centered convolution、27-state枚举、七扇区闭式、primitive积分及四重距离积分。
有限计算仅为 [E] 交叉核验；渐近最优性由第3节的解析证明给出。
两次独立证明复核分别检查七扇区/常数/扰动界，以及259的全源截断量词。

Brownian距离与负型几何属于既有理论背景。相关已发表论文入口为
[Székely--Rizzo, Brownian distance covariance](https://arxiv.org/abs/1010.0297)
及 [Lyons, Distance covariance in metric spaces](https://arxiv.org/abs/1106.5758)；
后者 v5附两篇已发表勘误。本笔记使用的1维恒等式已在上文独立重建，
不把经典条件负型性质作为新结果。本轮只核对上述书目信息；
七扇区双边常数的文献优先权尚未完成全面检索。
