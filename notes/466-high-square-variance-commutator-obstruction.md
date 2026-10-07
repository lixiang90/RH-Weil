# 466：原高素数平方残差的空间交换子正下界

2026-10-07。保留原 Eisenstein / AF finite frame。
本稿证明一个实际结构性下界，排除465中的过小 flat 残差前件；
第5节进一步给出 sharp 通用有限不等式和更强的实际下界。
没有得到新的零点比例或无零区域。

## 1. 同对象输入

沿用 [465](465-centered-high-square-joint-fourth-budget.md) 的
\(X=T/(2\pi)\)、\(\mathcal L=\log X\)、\(d=\lfloor X\mathcal L\rfloor\)、
原实线零延拓、\(E\)、\(P=EE^*\)、\(Q=1-P\)、even taper \(\phi\)。
本稿仅取 flat profile \(\psi=1\)，保留原 endpoint taper。
记原 high prime physical sum 为 \(B_H\)，实际矩阵
\[
 H=E^*B_HE,\qquad W=E^*M_{w_{\mathcal L}}E,\qquad
 \Gamma=H^2-W,\qquad q_T=d^{-1}\|\Gamma\|_{\rm HS}^2.
 \tag{1}
\]
\(w_{\mathcal L}\) 是465(1)的原同素数 high diagonal；
它非负，\(0\le W\le M_T I\)，其中可以选择
\[
 M_T=3/8+o(1)>0.
 \tag{2}
\]
证明(2)时用 \(\phi^2\le1\)、\(a_{\mathcal L}\to1\) 和原 Mertens
partial summation，untapered diagonal 的 uniform 上界趋于
\(\max_{|v|\le1/2}|v|(|v|+1)/2=3/8\)。
endpoint taper 只减少该非负 diagonal；这里不要求它一致趋于硬窗。

[454](454-original-background-and-weighted-prime-mixed-traces.md)
的原加权二矩给
\[
 \mu_T=d^{-1}\operatorname{Tr}\Gamma
 =d^{-1}\operatorname{Tr}H^2-d^{-1}\operatorname{Tr}W=o(1).
 \tag{3}
\]
以下不假定 high fourth 有界，不使用新的无零区域或另一数域角色。

## 2. 一个严格有限 PSD 不等式

**引理。** 对任意 \(d\) 维 Hermitian \(H\)、\(0\le W\le MI\)，
设 \(\Gamma=H^2-W\)、\(q=\operatorname{Tr}\Gamma^2/d\)、
\(\mu=\operatorname{Tr}\Gamma/d\)。则
\[
 K:=d^{-1}\|[H,W]\|_{\rm HS}^2
 \le4Mq+\frac{M^3}{64}+\frac{M^2\mu}{2}.
 \tag{4}
\]

在 \(H\) 的正交特征基中令 \(H_{ii}=\lambda_i\)，
\(w_i=W_{ii}\)、\(\Delta_i=\lambda_i^2-w_i\)、
\(r_i=\sum_{j\ne i}|W_{ij}|^2\)。准确地，
\[
 q=q_{\rm diag}+q_{\rm off},\quad
 q_{\rm diag}=d^{-1}\sum_i\Delta_i^2,\quad
 q_{\rm off}=d^{-1}\sum_i r_i,\quad
 \mu=d^{-1}\sum_i\Delta_i.
 \tag{5}
\]
从 \(W^2\le MW\) 得
\[
 0\le r_i\le w_i(M-w_i)\le M^2/4.
 \tag{6}
\]
同时
\[
 \begin{aligned}
 K&=d^{-1}\sum_{i,j}(\lambda_i-\lambda_j)^2|W_{ij}|^2\\
  &\le4d^{-1}\sum_i\lambda_i^2r_i\\
  &\le4M q_{\rm off}+M^2 d^{-1}\sum_i\Delta_i^+\\
  &\le4M q_{\rm off}+\frac{M^2}{2}\sqrt{q_{\rm diag}}
                    +\frac{M^2\mu}{2}.
 \end{aligned}
 \tag{7}
\]
第三行只将正的 \(\Delta_i\) 配以(6)；没有把 \(\Gamma\) 当成 PSD。
最后一行用 \(\Delta^+=(|\Delta|+\Delta)/2\) 与 scalar Cauchy。
对 \(z=\sqrt{q_{\rm diag}}\ge0\)，完成平方：
\[
 -4Mz^2+\frac{M^2z}{2}
 =-4M(z-M/16)^2+\frac{M^3}{64}.
 \tag{8}
\]
代回(7)即为(4)。所有步骤是严格 finite 代数，无未知增长误差。

## 3. 原 finite 交换子的完整二矩

在同一原 carrier 上，
\[
 \boxed{\lim_{T\to\infty}d^{-1}\|[H,W]\|_{\rm HS}^2
       =\frac{41}{10080}.}
 \tag{9}
\]

先支付内部投影。置 \(C_{\rm phys}=[B_H,M_w]\)，
\(C_{\rm fin}=E^*C_{\rm phys}E\)，其中 \(w=w_{\mathcal L}\)。
准确展开给
\[
 [H,W]-C_{\rm fin}
 =-E^*B_HQM_wE+E^*M_wQB_HE .
 \tag{10}
\]
465和454的原泄漏给
\[
 \ell_w=\|QM_wE\|_{\rm HS}\ll\sqrt{\log(2+\mathcal L)},\quad
 \ell_H=\|QB_HE\|_{\rm HS}
       \ll m_H\sqrt{\log(2+\mathcal L)},\quad
 m_H\ll\sqrt X/\mathcal L.
\]
故(10)的 HS 范数为
\(O(m_H\sqrt{\log(2+\mathcal L)})=o(\sqrt d)\)。

对每个 \(\pm\log p\)，\(C_{\rm phys}\) 的 coefficient 是原 prime
weight 乘以
\[
 \phi(u)\phi(u\pm\log p)[w(u\pm\log p)-w(u)].
 \tag{11}
\]
这是454允许的 bounded shift coefficient：\(w\) 的 sup 与一二阶
derivative \(L^1\) bounds 统一有界，两端及导数为零。
454的原 Fourier leakage 因而还给
\(\|QC_{\rm phys}E\|_{\rm HS}\ll
m_H\sqrt{\log(2+\mathcal L)}=o(\sqrt d)\)。
于是
\[
 \|C_{\rm fin}\|_{\rm HS}^2
 =\|C_{\rm phys}E\|_{\rm HS}^2-\|QC_{\rm phys}E\|_{\rm HS}^2.
 \tag{12}
\]
物理右式的二矩仍使用454全部差频 Hilbert 项、endpoint remainder
与和频 overlap-alias；它们对(11)的 bounded masks 同样是 \(o(d)\)。
同素数对角由 Mertens 与 dominated convergence 支付，给
\(\|C_{\rm phys}E\|_{\rm HS}^2/d=O(1)\)，因此(10)–(12)
确实将 actual finite norm 与该物理对角连接到 \(o(1)\) 精度。
未删除 \(P\)，未假设 high4 bounded。

令 \(D(t)=t(t+1)/2\)，\(0\le t\le1/2\)。
极限中 high 平移 \(x\in[1/2,1]\) 将负半区的 \(-t\)
移到正半区 \(x-t\)，两种 signs 贡献相同。因此
\[
 K_1=2\int_{1/2}^1x\int_{x-1/2}^{1/2}
                  [D(t)-D(x-t)]^2\,dt\,dx.
 \tag{13}
\]
\(D(t)-D(x-t)=(x+1)(t-x/2)\)，故
\[
 K_1=\frac16\int_{1/2}^1x(x+1)^2(1-x)^3\,dx
     =41/10080 .
 \tag{14}
\]
这是完整原交换子二矩，非受限的正子和。

## 4. 排除过小残差与粗预算的适用限制

把(2)、(3)、(9)代入严格有限(4)，不需要 \(q_T\) bounded，得到
\[
 \boxed{\liminf q_T\ge
 \frac{41/10080-(3/8)^3/64}{4(3/8)}
 =\frac{33479}{15482880}
 \approx0.00216232380539.}
 \tag{15}
\]
若 \(q_T\) 的 liminf 无穷，结论自然成立；否则沿达到 liminf 的
有界子列取极限即可。尤其(15)严格大于 \(1/1600\)。
465的 finite 联合预算仍正确，但其(17)/(21)的前件不可能在
本 flat 原矩阵上成立，不能将反事实的67.5%称作实际进展。

还可用纯有理数检查粗预算的局限。置 \(q_0=33479/15482880\)。
有
\[
 q_0>1/500,\quad \sqrt{q_0(19/240)}>1/80,\quad
 23/960+1/80=7/192,\quad
 4\sqrt{q_0(7/192)}>17/500.
 \tag{16}
\]
因此465的 monotone bound 满足
\[
 \mathcal B_1(q_0)>
 21/80+1/500+6/80+17/500
 =747/2000>1/3.
 \tag{17}
\]
所以单靠给 \(q_T\) 一个上界，再套465的 scalar 三角/Cauchy预算，
不能认证优于 flat 二矩的比例。它仍可作为其他联合估计的有限接口。

这不排除改进原路线：465舍去了 high/low平方残差之间的协方差、
entire13 的正交信息和22的负 commutator 项。继续研究应支付这些
实际联合量或原零侧 feature 几何。已有比例和明确 [R] 下的
\(\sigma_*=0.874957019420098946\ldots\) 均未因此提高。

## 5. 更强的通用有限常数与实际下界

上述实际交换子付款不变。有限 PSD 估计还可加强为
\[
 \boxed{\|[H,W]\|_{\rm HS}^2/d
 \le Mq_{\rm diag}+4Mq_{\rm off}\le4Mq.}
 \tag{18}
\]
它不需要 \(\mu=0\)，并且总 \(q\) 前的系数4对一般有限矩阵最优。

仍在 \(H\) 的特征基中，Young 平方给
\[
 \Delta_i r_i\le M\Delta_i^2/4+r_i^2/M.
 \tag{19}
\]
由(6)，
\[
 w_i r_i+r_i^2/M
 \le(2w_i-w_i^2/M)r_i\le Mr_i .
 \tag{20}
\]
这里 \(0\le w_i\le M\)，所以最后一步准确；
负 \(\Delta_i\) 也满足(19)，无需正部或迹条件。
把(19)–(20)代回
\(K\le4d^{-1}\sum_i(w_i+\Delta_i)r_i\) 即为(18)。

为证一般 sharpness，取 \(d=2\)、\(0<\varepsilon<M/2\)，
\[
 W=\begin{pmatrix}M-\varepsilon&\varepsilon\\
                  \varepsilon&M-\varepsilon\end{pmatrix},\quad
 H=\begin{pmatrix}\sqrt{M-\varepsilon}&0\\
                 0&-\sqrt{M-\varepsilon}\end{pmatrix}.
 \tag{21}
\]
\(W\) 的特征值为 \(M,M-2\varepsilon\)，因此 \(0\le W\le MI\)。
准确地，\(q_{\rm diag}=0\)、\(q_{\rm off}=q=\varepsilon^2\)、
\(K=4(M-\varepsilon)\varepsilon^2\)。
令 \(\varepsilon\downarrow0\)，\(K/(Mq)\to4\)。
这只是有限常数的等号极限，不是 actual prime matrix 的实现。

现在(2)、(9)、(18)直接给更强的原 flat 结论
\[
 \boxed{\liminf q_T\ge\frac{41/10080}{4(3/8)}
          =\frac{41}{15120}\approx0.00271164021164.}
 \tag{22}
\]
无需先假定 fourth bounded。它严格大于 \(1/400\)，
因而这个更宽松的小残差前件也已被排除。
第4节的旧下界和粗预算阻断仍成立，现应以(22)作为已付最强下界。
后续联合条件若同时约束 \(q\) 和 high/low commutator，
必须先与(22)相容，再证明其实际算术前件；
有限模型或单变量预算不会自动支付它们。
