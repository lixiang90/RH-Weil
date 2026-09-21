# 原物理时间交叉积：独立实际构造全文

2026-09-21。原始回包见[raw](f1-original-time-crossed-product-derivation.raw.json)。只增加标题和本段，并将本地路径改为相对链接；未将本侧题视为完整算术比较。

**两个实际代数同构都成立。414 的原 \(\beta\)-协变表示积分后仍然忠实，但这需要另证。** 加入时间交叉积后，开放层 \(J\) 确实成为整个 Hilbert 空间上的紧算子理想；完整代数并不会因此变成紧算子代数，也没有自动丢掉深边界。

确实存在会丢失深边界环面参数的“仅时间坐标”表示，但它不同于 414 保留径向因子的原表示。下面给出构造、范数完成和两种表示的区别。

已只读核对[指定计划第 1 节](f1-original-time-crossed-product-next-proof-plan.md)及 [414](../../notes/414-f1-deep-boundary-unitary-and-time-defect.md)。未写文件、运行 Git 或构建。

1. **联合群作用及消去时间位移的真实变换。**

记
\[
X=T_0^2,\quad d=(\infty,\infty),\quad
\ell_g=g_1L+g_2M,
\]
\[
A=C_0(X\times\mathbb R)\rtimes_\alpha\Gamma,\qquad
\mathcal B=A\rtimes_\beta\mathbb R.
\]
原作用为
\[
\alpha_gf(y,t)=f(y-g,t-\ell_g),\qquad
\beta_sf(y,t)=f(y,t-s),\qquad \beta_s(P_g)=P_g.
\]

在 \(\mathcal B\) 的乘子代数中，
\[
V_sP_g=P_gV_s.
\]
因此迭代交叉积的协变表示恰对应于联合群
\(\Gamma\times\mathbb R\) 的协变表示，其作用为
\[
\gamma_{(g,s)}f(y,t)=f(y-g,t-\ell_g-s).
\tag{1}
\]

作保持 Haar 测度的群同构
\[
(g,r)\longmapsto(g,r-\ell_g).
\]
联合作用随即变成
\[
\widetilde\gamma_{(g,r)}f(y,t)=f(y-g,t-r).
\tag{2}
\]
对应的新规范群乘子正是
\[
\boxed{Z_g=P_gV_{-\ell_g}.}
\tag{3}
\]
直接验证：
\[
Z_gf(y,t)Z_g^*=f(y-g,t),\qquad
Z_gZ_h=Z_{g+h},\qquad Z_gV_s=V_sZ_g.
\]
没有额外的二阶 cocycle。逆变换为
\[
\boxed{P_g=Z_gV_{\ell_g}.}
\tag{4}
\]

由此，径向协变对与时间协变对彼此交换：
\[
(C_0(X),Z_g),\qquad(C_0(\mathbb R),V_s).
\]
反过来，任何这样一对交换的协变表示，通过 (4) 都恢复原联合协变表示。这给出范数层面的双向普遍性质，而不只是形式上的群元换名。

2. **稠密核上的同构及乘法。**

取真实稠密卷积代数中的元素
\[
F=\sum_{g\in\Gamma}\int_{\mathbb R}
F_g(s;y,t)P_gV_s\,ds,
\tag{5}
\]
其中仅有限多个 \(g\) 非零，各 \(F_g\) 连续并具有紧支集。

原卷积为
\[
(F*G)_k(s;y,t)
=\sum_g\int_{\mathbb R}
F_g(r;y,t)\,
G_{k-g}(s-r;y-g,t-\ell_g-r)\,dr.
\tag{6}
\]
定义时间核
\[
\boxed{
k_g(y;t,t')=F_g(t-t'-\ell_g;y,t).
}
\tag{7}
\]
则直接换元得到
\[
(k*l)_k(y;t,t')
=\sum_g\int_{\mathbb R}
k_g(y;t,u)\,
l_{k-g}(y-g;u,t')\,du,
\tag{8}
\]
以及
\[
\boxed{
(k^*)_g(y;t,t')
=\overline{k_{-g}(y-g;t',t)}.
}
\tag{9}
\]
这是径向交叉积乘法与时间积分核乘法的准确组合。

令
\[
\mathcal C=C_0(X)\rtimes\Gamma_{\rm rad},\qquad
\mathbb K_t=\mathbb K(L^2(\mathbb R)).
\]
其规范径向群乘子记为 \(z_g\)。对分离核
\[
k_g(y;t,t')=a(y)\xi(t)\overline{\eta(t')},
\]
定义
\[
\boxed{
\Phi(F)=(a z_g)\otimes|\xi\rangle\langle\eta|.
}
\tag{10}
\]
对应的明确逆核是
\[
\boxed{
F_g(s;y,t)
=a(y)\xi(t)\overline{\eta(t-\ell_g-s)}.
}
\tag{11}
\]
这里 \(a\in C_c(X)\)、\(\xi,\eta\in C_c(\mathbb R)\)，故 (11) 确实属于 (5) 的稠密代数。

式 (8)–(9) 直接证明 (10) 保持乘法和伴随。没有遗漏 Jacobian 或模函数：所用群均为 unimodular，时间变量的变换只是平移。

3. **为何范数完成恰为所要求的张量积。**

先单独处理时间因子。对
\[
C_0(\mathbb R)\rtimes_{\rm trans}\mathbb R,
\]
规范 Schrödinger 表示为
\[
f\mapsto M_f,\qquad V_s\mapsto\mathsf T_s,\qquad
(\mathsf T_s\xi)(t)=\xi(t-s).
\]
积分元素的核是
\[
k(t,t')=F(t-t';t).
\]
其中
\[
F(s;t)=\xi(t)\overline{\eta(t-s)}
\]
准确对应秩一算子 \(|\xi\rangle\langle\eta|\)。

这些秩一核在交叉积范数中稠密：可在固定紧矩形上用有限分离核一致逼近任意紧支连续核；逆变换后的误差由固定有限时间区间长度乘一致误差控制，因此也在交叉积的 \(L^1\) 范数、进而在普遍范数中趋零。

有限秩代数的 \(C^*\) 范数由其有限矩阵角唯一决定。因此这里得到的是实际同构
\[
C_0(\mathbb R)\rtimes\mathbb R
\cong\mathbb K_t,
\tag{12}
\]
不是仅有 Morita 等价或 \(K\) 群同构。

第 1 步的双向普遍性质随后给出
\[
\mathcal B\cong
\mathcal C\otimes_{\max}\mathbb K_t.
\]
紧算子因子的有限矩阵角保证最大、最小张量范数一致，故
\[
\boxed{
\Phi:A\rtimes_\beta\mathbb R
\xrightarrow{\;\cong\;}
\bigl(C_0(T_0^2)\rtimes\Gamma_{\rm rad}\bigr)
\otimes\mathbb K(L^2\mathbb R).
}
\tag{13}
\]

这也说明 (7)–(11) 的稠密核同构确实延伸为等距满射。若原记号采用约化交叉积，\(\Gamma\) 与 \(\mathbb R\) 可和，所得同构相同。

4. **规范乘子的位置及同构中的像。**

令 \(\overline\Phi\) 表示 (13) 对乘子代数的延拓。其准确公式为
\[
\begin{aligned}
\overline\Phi(a(y)b(t))
 &=i_X(a)\otimes M_b,\\
\overline\Phi(P_g)
 &=z_g\otimes\mathsf T_{\ell_g},\\
\overline\Phi(V_s)
 &=1\otimes\mathsf T_s,\\
\overline\Phi(Z_g)
 &=z_g\otimes1.
\end{aligned}
\tag{14}
\]

须区分以下位置：

| 对象 | 规范位置 |
|---|---|
| \(P_g\) | 原 \(M(A)\)，并经非退化规范映射进入 \(M(\mathcal B)\) |
| \(V_s\) | 新时间交叉积的 \(M(\mathcal B)\) |
| \(Z_g=P_gV_{-\ell_g}\) | \(M(\mathcal B)\) |
| \(z_g\) | \(M(\mathcal C)\) |
| 积分紧支核 (5) | \(\mathcal B\) 本身 |

这些规范群酉元不能当作非幺代数 \(\mathcal B\) 的元素。原 \(A\) 的规范像也首先位于 \(M(\mathcal B)\)，不是默认作为 \(\mathcal B\) 的子代数包含。

例如 \(M_b\) 通常不紧，所以 (14) 的第一行本来就是乘子公式；加入时间积分核后才产生 \(\mathbb K_t\) 因子。

5. **\(I/J/D\) 图逐核相容。**

设
\[
X_0=\mathbb Z^2,\qquad X_I=X\setminus\{d\},
\]
\[
\mathcal J=C_0(X_0)\rtimes\Gamma_{\rm rad},\qquad
\mathcal I=C_0(X_I)\rtimes\Gamma_{\rm rad}.
\]
核变换 (7) 完全不改变径向变量 \(y\)。所以它同时给出
\[
\boxed{
J\rtimes_\beta\mathbb R\cong\mathcal J\otimes\mathbb K_t,
\qquad
I\rtimes_\beta\mathbb R\cong\mathcal I\otimes\mathbb K_t.
}
\tag{15}
\]

对深边界，限制 \(y=d\) 后径向作用平凡，故
\[
\mathcal C/\mathcal I\cong C^*(\Gamma).
\]
因此
\[
\boxed{
A_D\rtimes_\beta\mathbb R
\cong C^*(\Gamma)\otimes\mathbb K_t
\cong C(\mathbb T^2)\otimes\mathbb K_t.
}
\tag{16}
\]

下列两条正合列由 \(\Phi\) 逐项对应，所有箭头交换：
\[
0\longrightarrow I\rtimes\mathbb R
\longrightarrow A\rtimes\mathbb R
\longrightarrow A_D\rtimes\mathbb R
\longrightarrow0,
\]
\[
0\longrightarrow\mathcal I\otimes\mathbb K_t
\longrightarrow\mathcal C\otimes\mathbb K_t
\longrightarrow C(\mathbb T^2)\otimes\mathbb K_t
\longrightarrow0.
\tag{17}
\]
商映射就是核系数 \(k_g(y;t,t')\) 在 \(y=d\) 的限制。

开放层也能直接计算。对 \(m,n\in\Gamma\)，
\[
e_{mn}=\mathbf1_{\{m\}}z_{m-n}
\]
满足矩阵单位关系。因此
\[
\mathcal J\cong\mathbb K(\ell^2\Gamma),
\]
从而
\[
\boxed{
J\rtimes\mathbb R
\cong
\mathbb K(\ell^2\Gamma)\otimes\mathbb K_t.
}
\tag{18}
\]

中间两边的商同样相容：
\[
\mathcal I/\mathcal J
\cong
\bigl(C(\mathbb T_p)\otimes\mathbb K(\ell^2\mathbb Z_q)\bigr)
\oplus
\bigl(\mathbb K(\ell^2\mathbb Z_p)\otimes C(\mathbb T_q)\bigr).
\tag{19}
\]
这里 \(\{\infty\}\times\mathbb Z\) 的稳定子是 \(p\)-方向，另一边对称。于是 \(J\subset I\subset A\) 的整个相关图，经时间交叉积后与上述径向图张量 \(\mathbb K_t\) 相容。

6. **414 原表示积分后确实忠实：独立证明。**

把径向 Hilbert 空间按其坐标基识别为 \(\ell^2(\Gamma)\)。414 的表示准确为
\[
\begin{aligned}
(\pi(f)\psi)_m(t)&=f(m,t)\psi_m(t),\\
\pi(P_g)&=\lambda_g\otimes\mathsf T_{\ell_g},\\
U_s&=1\otimes\mathsf T_s,
\end{aligned}
\tag{20}
\]
其中 \((\lambda_g\xi)(m)=\xi(m-g)\)。

因此积分表示 \(\Pi=\pi\rtimes U\) 在 (13) 下恰为
\[
\boxed{\Pi=(\sigma\otimes{\rm id}_{\mathbb K_t})\circ\Phi,}
\tag{21}
\]
其中
\[
\sigma(a)\xi(m)=a(m)\xi(m),\qquad
\sigma(z_g)=\lambda_g.
\tag{22}
\]

现在证明 \(\sigma\) 忠实，不能略过此步。

在 \(\mathcal C\) 上对规范 \(\mathbb T^2\) 作用平均，得到忠实条件期望
\[
E:\mathcal C\to C_0(X).
\]
其忠实性可直接由紧群平均看出：若正元素的平均为零，对任意正泛函所得连续非负函数积分为零，故在单位点也为零。

对任意 \(b\in\mathcal C\)，由有限群多项式逼近，
\[
\langle\delta_m,\sigma(b^*b)\delta_m\rangle
=E(b^*b)(m).
\tag{23}
\]
若 \(\sigma(b)=0\)，则右侧在全部 \(m\in\mathbb Z^2\) 为零。由于 \(\mathbb Z^2\) 在 \(T_0^2\) 稠密，连续性给出
\[
E(b^*b)=0.
\]
由期望忠实性，\(b=0\)。因此 \(\sigma\) 忠实，进而
\[
\boxed{\ker(\pi\rtimes U)=0.}
\tag{24}
\]

这不是从“\(\pi\) 忠实”自动推出的，而是通过新交叉积的具体分解和径向轨道表示重新证明的。

联合谱也没有隐藏约束。对径向和时间分别作 Fourier 变换，可写
\[
P_p=z_p e^{-iL\xi},\qquad
P_q=z_q e^{-iM\xi},\qquad
V_s=e^{-is\xi},
\]
其中 \((z_p,z_q)\in\mathbb T^2\) 与 \(\xi\in\mathbb R\) 独立。因此
\[
Z_p=z_p,\qquad Z_q=z_q,
\]
保留整个 \(\mathbb T^2\) 参数。

7. **换成 \(x=t-jL-kM\) 后，只有开放层成为紧算子。**

定义酉变换
\[
(\mathcal U\psi)_m(x)=\psi_m(x+\ell_m).
\]
直接计算：
\[
\begin{aligned}
\mathcal U P_g\mathcal U^*&=\lambda_g\otimes1,\\
\mathcal U V_s\mathcal U^*&=1\otimes\mathsf T_s,\\
\mathcal U Z_g\mathcal U^*
 &=\lambda_g\otimes\mathsf T_{-\ell_g},\\
\mathcal U M_f\mathcal U^*
 &=M_{f(m,x+\ell_m)}.
\end{aligned}
\tag{25}
\]

在开放层，
\[
J\cong C_0(\mathbb R_x)\otimes\mathbb K(\ell^2\Gamma),
\]
且 \(\beta\) 只平移 \(x\)。所以加入 \(V_s\) 后，确实得到
\[
J\rtimes\mathbb R
\cong\mathbb K(L^2\mathbb R_x)\otimes
\mathbb K(\ell^2\Gamma).
\tag{26}
\]
但最后一行 (25) 阻止了把这个结论套到整个 \(A\)：一般的
\(f(m,x+\ell_m)\) 不满足所需的统一消失条件。

有一个完全具体的非紧见证。令
\[
Q(y)=H(j)H(k)\in C_c(X),
\]
取 \(\xi\in C_c(\mathbb R)\)、\(\|\xi\|_2=1\)，并令
\[
k_0=|\xi\rangle\langle\xi|.
\]
则
\[
Q\otimes k_0\in\mathcal C\otimes\mathbb K_t
\tag{27}
\]
对应真实稠密核
\[
F_0(s;y,t)=Q(y)\xi(t)\overline{\xi(t-s)}.
\]
其深边界商是
\[
1_{C(\mathbb T^2)}\otimes k_0\ne0.
\]

在原表示中，(27) 固定无穷正交单位向量
\[
\delta_{(n,0)}\otimes\xi,\qquad n\ge0,
\]
故不是紧算子。

在 \(x\) 坐标中，它成为
\[
\bigoplus_{m\in\Gamma}
Q(m)\,
|\mathsf T_{-\ell_m}\xi\rangle
\langle\mathsf T_{-\ell_m}\xi|.
\tag{28}
\]
每块虽为秩一，但非零块的范数始终是 \(1\)；直和仍不紧。时间支撑移动到远处不等于块范数趋零。

更一般，
\[
(Qz_g)\otimes k_0
\]
的深边界商为
\[
\chi_g\otimes k_0,
\]
所以全部环面 Fourier 模式都由实际商保留，并未被开放层的紧化吞掉。

式 (25) 也精确解释了乘子位置：当 \(s\ne0\)，此 \(V_s\) 不属于原 \(\pi(M(A))\)。因为原 \(M(A)\) 限制到
\[
M(J)=M(C_0(\mathbb R_x)\otimes\mathbb K)
\]
后必须与中心乘子 \(M_{\varphi(x)}\) 交换，而非零时间平移不满足这一点。相应地，当 \(g\ne0\) 时，\(\ell_g\ne0\)，\(Z_g\) 也不是原 \(A\) 的乘子；它是新交叉积中的乘子。

8. **真正会丢掉环面信息的表示及其准确核。**

须区分三件事：

- 414 的完整积分表示 \(\Pi\)，已由 (24) 证明忠实；
- 深边界商 \(A_D\rtimes\mathbb R\)；
- 通过径向常值系数得到的深边界代数乘子副本。

414 的表示并不因“取深边界”而自动成为商代数的表示：它在 \(I\rtimes\mathbb R\) 上非零，不能直接下降到该商。

其乘子中的深边界副本，在分解后是
\[
C^*(\Gamma)\otimes\mathbb K_t
\longrightarrow M(\mathcal C\otimes\mathbb K_t),
\qquad
\chi_g\otimes k\longmapsto z_g\otimes k.
\tag{29}
\]
414 的表示在这个副本上也是忠实的，因为 \(\lambda_p,\lambda_q\) 具有完整联合谱 \(\mathbb T^2\)。但 (29) 是乘子嵌入，不能与深边界商映射混同。

另一方面，若在深边界另选**只有时间坐标**的协变表示
\[
f(t)\mapsto M_f,\qquad
P_g\mapsto\mathsf T_{\ell_g},\qquad
V_s\mapsto\mathsf T_s
\quad\text{于 }L^2(\mathbb R),
\tag{30}
\]
则
\[
Z_g\mapsto1.
\]
因此其积分表示在 (16) 下正是
\[
{\rm ev}_{(1,1)}\otimes{\rm id}_{\mathbb K_t}.
\]
准确核为
\[
\boxed{
\{F\in C(\mathbb T^2,\mathbb K_t):F(1,1)=0\}
=
C_0(\mathbb T^2\setminus\{(1,1)\})\otimes\mathbb K_t.
}
\tag{31}
\]
其像确实只有 \(\mathbb K_t\)。

此时联合谱受到约束：
\[
(P_p,P_q,\xi)
=
(e^{-iL\xi},e^{-iM\xi},\xi).
\tag{32}
\]
虽然前两坐标的投影在 \(\mathbb T^2\) 稠密，但连同时间频率后，它只是
\(\mathbb T^2\times\mathbb R\) 中的一个真闭图像；独立环面变量已经消失。不能用该投影的稠密性推断时间交叉积表示忠实。

所以本侧题的准确结果是：**所要求的实际代数同构及理想图成立；414 原完整积分表示忠实；开放层紧化不等于完整代数紧化；仅时间的深边界表示则确实把环面压到一个点。** 全部结论来自原作用、卷积核和范数完成，未使用 Thom 的 \(K\) 群同构替代实际构造，也未进入源类定向或算术迹计算。
