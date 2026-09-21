# 第419稿全文独立逆审

2026-09-21。完整原始回报见 [raw](f1-original-time-crossed-product-full-review.raw.json)。

**419 全文独立逆审通过。**已覆盖全部十一节及公式 **(1)–(22)**，包括新增第7–9节的逐步核验。未发现必须修改的数学错误、实质性条件遗漏或量词越界。第10节的 Hardy/Fredholm family 保持为下一任务，本报告不将其视为已证。

实际读取文件：[419-f1-original-time-crossed-product-and-trace-interface.md](H:/codex-build/RH/RH-Weil/notes/419-f1-original-time-crossed-product-and-trace-interface.md)，16502 字节。读取前后 SHA256 一致，且与指定值相符：

```text
2c68f5bf15a7137228eb4808c73b112d5cab4299db810afa29f7c92312169372
```

以下以 \(T_s\xi(t)=\xi(t-s)\)、\(L=\log p\)、\(M=\log q\)、\(\ell_g=g_1L+g_2M\) 为约定。对414、418已闭合的迹范数收敛结果只作为明确依赖使用；419新增的交叉积、忠实性、迹扩张障碍及源族计算分别核验。

1. **第1节，(1)–(2)：联合群解耦及交叉积同构成立。**

   原联合作用为
   \[
   \gamma_{(g,s)}f(y,t)=f(y-g,t-\ell_g-s).
   \]
   群变量替换
   \[
   (g,r)\longmapsto(g,r-\ell_g)
   \]
   是连续群同构，且保持“计数测度 \(\times\) Lebesgue测度”：对每个固定 \(g\)，只是实变量平移。因而没有额外 Jacobian、模函数或二余圈。

   令 \(Z_g=P_gV_{-\ell_g}\)，直接得到
   \[
   \operatorname{Ad}Z_g(f)(y,t)=f(y-g,t),\qquad
   Z_gZ_h=Z_{g+h},\qquad [Z_g,V_s]=0,
   \]
   以及逆关系 \(P_g=Z_gV_{\ell_g}\)。这同时核对了解耦符号和可逆性。

   两套交换的协变对给出满交叉积的普遍性质同构，故
   \[
   \mathfrak B=A\rtimes_\beta\mathbb R
   \cong
   \mathfrak C\otimes\mathcal K_t,\qquad
   \mathfrak C=C_0(X)\rtimes\Gamma_{\rm rad}.
   \]
   这里是实际代数同构，不是仅凭 Thom 同构或 \(K\) 群相同作出的识别。

2. **第2节，(3)–(5)：核参数、乘法、伴随及满范数完成均闭合。**

   对
   \[
   F=\sum_g\int F_g(s;y,t)P_gV_s\,ds,
   \]
   核变量必须取
   \[
   k_g(y;t,t')=F_g(t-t'-\ell_g;y,t).
   \]
   将这一替换代入交叉积卷积，取 \(u=t-\ell_g-r\)，确实得到
   \[
   (k*l)_k(y;t,t')
   =\sum_g\int k_g(y;t,u)\,
       l_{k-g}(y-g;u,t')\,du.
   \]
   伴随为
   \[
   (k^*)_g(y;t,t')
   =\overline{k_{-g}(y-g;t',t)}.
   \]
   群指标、径向平移与时间端点全部一致，没有漏掉 \(\ell_g\)。

   分离核
   \[
   a(y)\xi(t)\overline{\eta(t')}
   \]
   对应 \((az_g)\otimes|\xi\rangle\langle\eta|\)，其逆像为
   \[
   F_g(s;y,t)=a(y)\xi(t)
       \overline{\eta(t-\ell_g-s)}.
   \]
   当 \(\xi,\eta\) 紧支时，逆像也有紧的时间参数支撑。

   满范数完成的论证足够：固定紧矩形上的连续核可由有限分离核一致逼近；变回交叉积系数后，误差受到
   \(\int\sup_t|F(s,t)|\,ds\) 控制，因而控制满交叉积范数。有限秩核落在有限矩阵角中，其 \(C^*\) 范数唯一。因此时间交叉积的完成确为 \(\mathcal K_t\)，没有仅在某一表示下消失而未排除的额外核。随后 \(\mathcal K_t\) 的核性消除最大与最小张量积的差别。

3. **第3节，(6)–(8)：乘子位置及全部理想、商图正确。**

   乘子对应关系
   \[
   P_g\mapsto z_g\otimes T_{\ell_g},\quad
   V_s\mapsto1\otimes T_s,\quad
   Z_g\mapsto z_g\otimes1
   \]
   与第1–2节一致。时间乘法算子 \(M_b\) 通常不紧，因此原 \(A\) 的自然位置是 \(M(\mathfrak B)\)，不能据此改称 \(A\subset\mathfrak B\)。正文保留了这个区别。

   核同构不改变径向变量 \(y\)，故对开不变子空间限制及边界取值均自然兼容：
   \[
   J\rtimes\mathbb R\cong\mathfrak j\otimes\mathcal K_t,\qquad
   I\rtimes\mathbb R\cong\mathfrak i\otimes\mathcal K_t,
   \]
   \[
   A_D\rtimes\mathbb R
   \cong C(\mathbb T^2)\otimes\mathcal K_t.
   \]
   开轨道中的
   \[
   e_{mn}=1_{\{m\}}z_{m-n}
   \]
   满足矩阵单位关系，所以
   \(\mathfrak j\cong\mathcal K(\ell^2\Gamma)\)。

   两条侧边分别有一个稳定子方向和一个自由平移方向，得到(8)的两个直和分量。对应的时间商公式准确写作
   \[
   (I/J)\rtimes_\beta\mathbb R
   \cong(\mathfrak i/\mathfrak j)\otimes\mathcal K_t.
   \]
   满交叉积的正合性及张量 \(\mathcal K_t\) 后的正合性支持所用图；若改用约化版本，本文各作用群的可和性也满足要求。

4. **第4节，(9)–(10)：原414积分表示的忠实性得到独立证明。**

   原表示满足
   \[
   \pi(P_g)=\lambda_g\otimes T_{\ell_g},\qquad
   U_s=1\otimes T_s,
   \]
   因而
   \[
   \Pi=\pi\rtimes U=(\sigma\otimes\mathrm{id})\Phi,
   \qquad
   \sigma(z_g)=\lambda_g.
   \]
   这一步没有把“原系数表示忠实”直接当成“积分表示忠实”。

   对径向交叉积，规范环面作用的平均给出忠实期望
   \(E:\mathfrak C\to C_0(X)\)。有限群多项式计算并由范数逼近延拓，给出
   \[
   \langle\delta_m,\sigma(b^*b)\delta_m\rangle
   =E(b^*b)(m).
   \]
   若 \(\sigma(b)=0\)，右端在所有 \(m\in\mathbb Z^2\) 上为零；由于该开轨道在 \(X\) 中稠密，连续性推出 \(E(b^*b)=0\)，再由期望忠实性推出 \(b=0\)。

   因此
   \[
   \ker\Pi=0,\qquad
   \Pi(J\rtimes\mathbb R)
   =\mathcal K(\ell^2\Gamma\otimes L^2\mathbb R).
   \]
   后一个等式是“像等于全部紧算子”，不只是包含某些紧核。它是第7节唯一原像论证的关键。

   联合 Fourier 变量中
   \[
   P_p=\zeta_p e^{-iL\xi},\qquad
   P_q=\zeta_q e^{-iM\xi},\qquad
   V_s=e^{-is\xi}.
   \]
   原表示保留了独立的 \(\zeta_p,\zeta_q,\xi\)，没有把环面自由度压缩为一条时间轨道。

5. **第5节，(11)：坐标变换、非紧元及新旧乘子区别成立。**

   在
   \[
   (\mathcal U\psi)_m(x)=\psi_m(x+\ell_m)
   \]
   下，直接计算得到
   \[
   P_g\mapsto\lambda_g\otimes1,\quad
   V_s\mapsto1\otimes T_s,\quad
   Z_g\mapsto\lambda_g\otimes T_{-\ell_g}.
   \]
   原 \(J\) 因而具有 \(C_0(\mathbb R_x)\otimes\mathcal K_{\rm rad}\) 的形式；加入时间交叉积才得到全部紧算子。这不能推广成整个 \(A\) 或 \(\mathfrak B\) 都是紧算子代数。

   \(Q\otimes k_0\) 在 \(\mathfrak B\) 内，深边界像为非零的 \(1\otimes k_0\)。它固定无穷多个互相正交的径向向量乘同一个时间向量，所以非紧。坐标变换后的时间支撑漂移不会改变这一结论，各块仍有范数一。

   关于 \(V_s,Z_g\) 不属于旧表示的乘子像，正文使用的判据有效：旧 \(M(A)\) 限制到 \(M(J)\) 后必须与中央乘法算子 \(M_\varphi(x)\) 交换，而非零时间平移不满足这一条件。不同素数保证 \(\ell_g=0\) 仅在 \(g=0\) 时发生，故所述非平凡情形没有遗漏例外。

6. **第6节，(12)–(13)：原表示与仅时间边界表示的核区分准确。**

   原 \(\Pi\) 在 \(J\rtimes\mathbb R\) 上已经非零且忠实，所以不能通过深边界商因子化。

   (12)的
   \[
   \chi_g\otimes k\longmapsto z_g\otimes k
   \]
   是进入 \(M(\mathfrak B)\) 的忠实嵌入：\(\lambda_\Gamma\) 保留完整环面谱。此嵌入与“对径向变量取深边界”的商映射是不同的映射，正文没有混同。

   仅时间边界表示中
   \[
   P_g\mapsto T_{\ell_g},\qquad V_s\mapsto T_s,
   \]
   因而 \(Z_g\mapsto1\)。在解耦后的边界代数上，它恰为
   \[
   \operatorname{ev}_{(1,1)}\otimes\mathrm{id}_{\mathcal K_t},
   \]
   故准确核是
   \[
   C_0\!\left(\mathbb T^2\setminus\{(1,1)\}\right)
   \otimes\mathcal K_t,
   \]
   像为 \(\mathcal K_t\)。

   曲线 \((e^{-iL\xi},e^{-iM\xi})\) 在环面稠密，不能消除这个核：把时间谱变量一并保留后，
   \[
   (e^{-iL\xi},e^{-iM\xi},\xi)
   \]
   是乘积空间中的闭图，并不是全部联合谱。正文对此区分正确。

7. **第7节，(14)–(16)：\(C_N\) 的完整乘子位置、全群迹算子的唯一原像及边界失迹结论成立。**

   \(C_N\in M(\mathfrak B)\) 的依据不能只说它属于
   \(M(J\rtimes\mathbb R)\)；后者本身并不足够。本稿给出的张量结构可以证明更强的位置。

   具体说，\(E_\alpha\in\mathfrak j\subset\mathfrak C\)，
   \(M_{d_\alpha}\in B(L^2\mathbb R)=M(\mathcal K_t)\)。对稠密初等张量，
   \[
   (E_\alpha\otimes M_{d_\alpha})(a\otimes k)
   =E_\alpha a\otimes M_{d_\alpha}k
   \in\mathfrak j\otimes\mathcal K_t,
   \]
   右乘也同样成立，且有统一算子范数界。因此这些算子确实定义整个 \(\mathfrak B\) 的乘子，(14)的压缩合法。这里不需要把 \(C_N\) 称为投影，也不需要宣称它属于 \(\mathfrak B\) 本身。

   单项时间核为
   \[
   d_\alpha(t)\,
   h(t-t'-\ell_g)\,
   d_\beta(t'),
   \]
   是光滑紧支核；径向因子 \(E_\alpha\lambda_gE_\beta\) 有限秩。因此每个未修正单项属于 \(\mathfrak j\otimes\mathcal K_t\)。414的绝对迹范数收敛蕴含算子范数收敛，再由忠实同构的等距性及理想闭性，得到全 \(\Gamma\) 和的理想归属。

   对 \(A_N^c\)，418已证明其全群和为迹类。结合(10)“开理想的像等于全部紧算子”，立即得到它在 \(J\rtimes\mathbb R\) 中的存在且唯一原像。原 \(A_N\) 同理。这个论证没有擅自把任意 \(B(\mathcal H)\) 算子当作交叉积元素。

   两者在侧边界商及深边界商中均为零。另一方面，取 \(h\) 支撑在 \(-L\) 的足够小邻域，使
   \[
   h(-L)=1,\qquad h(0)=0
   \]
   并避开其余相关素数周期，414公式给出
   \[
   \frac12\operatorname{Tr}A_N(h)=L\rho_p\ne0.
   \]
   因此普通边界商不可能通过其上的线性读出来恢复这个原迹。

   此非零例证针对原 \(A_N\)，不要求对所有分割、所有修正族的 \(A_N^c\) 都在同一测试函数上非零。结论也没有排除依赖提升的相对类、传递或另行定义的重整化读出。

8. **第8节，(17)–(18)：单边移位及两类迹扩张矛盾均成立，排除范围恰当。**

   \[
   E=H_p\,\delta_{k0}
   \]
   的支撑是带端点的正向 \(p\) 尾、固定 \(q\) 坐标，属于侧理想对应的紧开部分；并不碰到深角 \(d\)。令
   \[
   S=Ez_pE,\qquad r=1_{\{(0,0)\}}.
   \]
   在开轨道上，
   \[
   S\delta_{(j,0)}=\delta_{(j+1,0)}\quad(j\ge0),
   \]
   因而
   \[
   S^*S=E,\qquad SS^*=E-r.
   \]
   第4节的忠实性把这些表示中的关系提升为实际代数关系。

   张量时间秩一投影 \(k_0\) 后，\(\widetilde r=r\otimes k_0\) 是整个表示空间上的秩一投影。对有限值循环线性泛函，只需它满足
   \(\tau(\widetilde r)=1\)，便有
   \[
   \tau(\widetilde E)
   =\tau(\widetilde S^*\widetilde S)
   =\tau(\widetilde S\widetilde S^*)
   =\tau(\widetilde E)-1,
   \]
   矛盾。此处甚至不需要连续性或正性。准确的归一化需求只是与有限秩上的通常迹相符；无需假定所有紧算子都有有限通常迹。

   对允许无穷值的迹权，正文额外使用“有限正值锥范数稠密”，这一步不可省略，而稿中没有省略。选取正元 \(a\)，满足
   \[
   \tau(a)<\infty,\qquad
   \|a-\widetilde E\|<\tfrac12.
   \]
   则
   \[
   \widetilde Ea\widetilde E\ge\tfrac12\widetilde E,
   \]
   且由迹权的 \(x^*x/xx^*\) 等值性质，
   \[
   \tau(\widetilde Ea\widetilde E)
   =\tau(a^{1/2}\widetilde Ea^{1/2})
   \le\tau(a)<\infty.
   \]
   所以 \(\tau(\widetilde E)<\infty\)，此时才可对移位关系使用有限值加减，得到矛盾。

   **这不排除 \(B(\mathcal H)\) 上通常的扩展迹 \(\operatorname{Tr}\)。**在那里 \(\operatorname{Tr}(\widetilde E)=\infty\)，而有限迹正元的范数闭包只能落在紧算子中，不能逼近这个非紧投影。本稿没有使用无效的“\(\infty=\infty-1\)”推理。

   同理，(18)中
   \[
   \operatorname{Tr}[\widetilde S^*,\widetilde S]=1
   \]
   合法，因为交换子是秩一；不能因此对两个各自非迹类的乘积强行套通常迹的循环性。

9. **第9节，(19)–(22)：实际源族、Green 等距、Floquet 相位及全部特征值符号正确。**

   从(6)逐项取深边界参数 \(\zeta=(\zeta_p,\zeta_q)\)，得到(19)：
   \[
   e_\zeta=\sum_n\zeta_p^n
     M_{c(t)c(t-nL)}T_{nL},
   \]
   \[
   v_\zeta=\sum_n\zeta_p^n\zeta_q
     M_{c(t)c(t-nL-M)}T_{nL+M},
   \qquad
   u_\zeta=1-e_\zeta+v_\zeta.
   \]
   紧支性使所需 \(n\) 集合有限，故得到范数连续的乘子族。它们不能因此被误认成紧算子值族。

   写 \(t=s+jL\)，\(0\le s<L\)。则
   \[
   e_\zeta(s)_{jk}
   =\zeta_p^{j-k}c(s+jL)c(s+kL)
   =a_j(s)\overline{a_k(s)},
   \]
   其中 \(a_j(s)=\zeta_p^jc(s+jL)\)。分割恒等式给出
   \(\sum_j|a_j(s)|^2=1\)，所以
   \[
   (G_\zeta f)(s+jL)=a_j(s)f(s)
   \]
   是到 \(e_\zeta\mathcal H\) 的满等距映射。于是每个纤维虽为秩一，整个 \(e_\zeta\) 仍是无限秩投影；不能把“逐纤维秩一”当作时间 Hilbert 空间上的紧性。

   对 \(s-M=r+kL\)、\(0\le r<L\)，逐项代入后相位相乘为
   \[
   \zeta_p^n\zeta_p^{j-n+k}=\zeta_p^{j+k},
   \]
   因而
   \[
   G_\zeta^*v_\zeta G_\zeta f(s)
   =\zeta_q\zeta_p^k f(r).
   \]
   所以(20)确实是 **\(\zeta_p^k\)**，不是其逆；负 \(k\) 也被同一计算覆盖。

   固定一点选 \(\zeta_p=e^{i\theta_p}\)，取正交基
   \[
   f_m(s)=L^{-1/2}
      e^{i(\theta_p+2\pi m)s/L}.
   \]
   由于 \(r=s-M-kL\)，代入上式并消去
   \(\zeta_p^k e^{-i\theta_pk}\)，得到(21)
   \[
   \lambda_m
   =\zeta_q
     e^{-i(\theta_p+2\pi m)M/L}.
   \]
   指数的**负号正确**。更换 \(\theta_p\) 的分支只会重编号 \(m\)，不会改变谱。

   这些是 \(v_\zeta\) 在 \(e_\zeta\mathcal H\) 上的完整特征值；在全空间上，\(v_\zeta\) 还在补空间取零，\(u_\zeta\) 则在补空间取一。由于 \(M/L\) 无理，\(\lambda_m\) 在单位圆稠密，因此有无穷多个正交本征向量满足
   \[
   \|(u_\zeta-1)G_\zeta f_m\|
   =|\lambda_m-1|\ge\delta>0.
   \]
   所以 \(u_\zeta-1\) 非紧。

   另一方面，\(e_\zeta\) 的值域支撑在 \(\operatorname{supp}c\) 内，故补空间包含一个无限维的 \(L^2\) 子空间。对任意标量 \(a\ne1\)，\(u_\zeta-a1\) 在该子空间上等于 \((1-a)1\)，仍非紧。因此对**每个** \(\zeta\)，
   \[
   u_\zeta\notin\mathbb C1+\mathcal K_t.
   \]
   (22)不仅排除“减去一后紧”，也排除了减去任意标量后的紧性，没有遗漏特殊参数。

10. **第10节：下一任务的范围准确，未被本文提前使用。**

   Hardy 投影交换子的紧性与参数连续性、Toeplitz/Fredholm family、指标丛、局部指标及过渡函数、Bott/Thom 方向，均仍须另证。

   第9节逐点选择 \(\theta_p\) 的谱计算并不自动构成全环面上的连续本征基，也不自动给出所需指标丛。正文把这些列为后续工作是准确的。即使未来完成 Fredholm family，算术迹比较仍需独立桥接，本文没有越过这一界限。

11. **第11节：依赖、来源及形式化范围表述适当。**

   已交叉核读所附独立交叉积推导、来源阅读说明及下一步证明计划，并核对414、418中本稿实际使用的定义和结论。

   第1–6节有核层面、满范数完成及表示忠实性的直接论证，不能简化成“教材有相关定理所以成立”；本次通过依据是这些具体论证与计算。来源说明所列教材页码不等于本次重新逐页审计了整部教材。

   本稿也没有把既有 Lean 簿记当成交叉积分析、迹权障碍或后续 Fredholm family 的机器认证。

**必要改正：无。**可保留的结论包括交叉积实际同构、原积分表示忠实性、所有所列理想与表示核、全群迹算子的唯一开理想原像、所限定的迹扩张障碍，以及源族的 Floquet 谱和非紧性结论。仍开放的是第10节所列 family 构造及其后续算术迹连接。

全程只读；未写文件、未构建、未运行 Git 或 Lean、未提交，也未重启任何进程。
