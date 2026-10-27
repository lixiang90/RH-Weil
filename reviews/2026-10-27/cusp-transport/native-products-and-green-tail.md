# II₂,₂ 的实际 Faber 产品、全边界与 Green/current 尾

2026-10-27；C046 独占分支。只消费同一 (F_r=L_r(j)) 及整数 Faber 截断，不改 STATE／cadence／Goal／文献库／合同，不自行计轮。恢复已读当前执行状态及 C046；研究轮、whole-budget 净值和宏观审视由 root 消费后判定。

本稿证明一个特定的解析完成化接口：先逐个整数 (J_m) 应用原 Borcherds 定理，再在 divisor／Green 数据上复线性组合，最后证明全尾。这里的粗模空间是固定的 (X=\mathbf P^1_{\mathbb C}\times\mathbf P^1_{\mathbb C})，不是算术整模型。已付 global norm 的无限输出是 balanced (G(r)) 的 (L^1) 函数和 (Z(r)) 的有限质量 current；(a_0(r)\Phi_0) 另保其原 line／metric／character 标签。一般不能把这些无限 current 视为 locally finite 的解析除子或一个普通亚纯函数。

## 1. 输入与原文中实际可用的定理

沿用 [Fourier／Faber 分支](fourier-kernels-and-faber-tails.md) 的规范：

\[
 F_r(\tau)=L_r(j(\tau)),\qquad L_r(z)=\int r(u)e^{zu}du,\qquad
 J_m=q^{-m}+O(q),\quad a_0(J_m)=0,
\]
\[
 b_m(r)=a_{-m}(r),\qquad
 F_{r,N}=a_0(r)\,1+\sum_{m=1}^{N}b_m(r)J_m.                 \tag{1}
\]

全部 (r\in\mathcal S_{\exp,\mathbb C}) 满足，对每个固定 (0<s<1)，

\[
 |b_m(r)|\le s^m p_{A_s}(r),\quad |a_0(r)|\le p_{A_s}(r),\qquad
 p_A(r)=\int|r(u)|e^{A|u|}du,\quad
 A_s=\max_{|q|=s}|\Re j(q)|.                              \tag{2}
\]

对固定源窗 ([-L,L])，同一右端可替为 (s^m C_{L,s}\|r\|_{du})，其中
\(C_{L,s}^2=(e^{2A_sL}-1)/A_s\)，(A_s=0) 时连续解释为 (2L)。这只是 fixed-window 原 du 费用；全线用强半范数，不能混为全线 du 一致性。Dlog 版本保留原 zero-extension norm 比较常数。

唯一所用原论文为 [Borcherds 作者稿 §13，Theorem 13.3、Example 13.5](https://math.berkeley.edu/~reb/papers/aut/aut.pdf)。本地文件为 [作者稿 PDF](../../../literature/local/2026-10-27-weil/borcherds-automorphic-products-1998-author.pdf)，64 页、448471 字节，SHA256 `93618b64a0c07f68a085b0b520079b1062a98ff7672159f34f77b1463e0724d2`。正文印刷页 47–50 给出以下实际内容：

* 原输入须在上半平面全纯、在 cusp 亚纯，并且 (n\le0) 的系数为整数。(J_m) 逐个满足。
* 对 (M=II_{2,2})，输入 weight0，产品 weight 为 (c_0(0)/2)，有 unitary projective character。
* 负向量的除子阶数为 \(\sum_{x>0,\,x\lambda\in M'}c_{x\lambda}(x^2\lambda^2/2)\)。不能删去向量的非本原倍数。
* 其准确 log 身份是

\[
 \Phi_M(Z,1,F)=-4\log|\Psi_M(Z,F)|
       -2c_0(0)\bigl(\log|Y_M|+\Gamma'(1)/2+\log\sqrt{2\pi}\bigr).
                                                               \tag{3}
\]

* product 的前常数的绝对值是原文写出的有限 discriminant 因子；在本 unimodular、level-one cusp 情形该有限乘积为空，故余下前常数绝对值为 1。Weyl exponential 必须保留。

Example 13.5 只将 (J_1=j-744) 的产品说成 essentially (j(z_1)-j(z_2))，并强调 split dimension4 中 cusp 可以有极点。原文 Problem 16.5 没有替本稿证明一般 Hecke 等变；以下用这个特例的 divisor、character、cusp 及规范直接识别每个 (J_m)，不将该 problem 当定理引用。

## 2. 全 Hecke norm 的整数实物与全部边界

记 (D_m=\sigma_1(m)=\sum_{d\mid m}d)，定义

\[
 R_m(X,j(\tau))=
  \prod_{\substack{ad=m\\a,d>0}}\ \prod_{0\le b<d}
       \left(X-j\!\left(\frac{a\tau+b}{d}\right)\right).
                                                               \tag{4}
\]

这里是 determinant-(m) 的全部 integral isogeny representatives，含非 cyclic 者。因子数是 (D_m)，(R_m) 对 X monic。右边在 \(\tau\mapsto\gamma\tau\) 下由 determinant-(m) 左陪集置换而不变；其系数是有限处全纯、cusp 只有有限极点的标量模函数，因此为 (j(\tau)) 的多项式。

整数性也可在这个实物上检查：各 Fourier 系数先为 roots of unity 中的代数整数；Galois 自同构置换每个 (b\bmod d)，故系数为有理整数。周期性消去分数 q 次幂，再以 j 的 monic (q^{-1}) 三角展开递减消去各极点，得

\[
                 R_m\in\mathbb Z[X,Y].                         \tag{5}
\]

这是无需 Borcherds–Hecke 等变的独立 norm 多项式。类似地，未归一化 Hecke 和满足

\[
 \sum_{ad=m}\sum_{b\bmod d}
 J_1\!\left(\frac{a\tau+b}{d}\right)=J_m(\tau).                \tag{6}
\]

确实，(J_1) 的唯一负项在 b 求和后只对 (d=1,a=m) 留下 (q^{-m})，所有常数仍为零；由该 principal part 的唯一性即得(6)。如采用带 (1/m) 的 Hecke 规范，右边为 (mT_mJ_1)；本稿始终使用(6)的显式规范。

在 (X=j(z_1),Y=j(z_2)) 上，令 (T_m) 为(4)的零除子，令 \(\overline T_m\) 为其在 X 中的闭包；以下不将空间 X 与多项式第一变量混淆。两个 boundary curves 为

\[
 B_1=\{X=\infty\},\quad B_2=\{Y=\infty\},\quad B=B_1+B_2.
\]

固定 (z_2) 时，(R_m(j(z_1),j(z_2))\sim q_1^{-D_m})。反过来，对一个 (ad=m) block，

\[
 \prod_{b\bmod d}\left(X-j\!\left(\frac{az_2+b}{d}\right)\right)
       \sim -q_2^{-a}.
\]

其中符号来自 \((-1)^d\prod_b e^{-2\pi ib/d}=-1\)。因此第二方向总 leading 为 \((-1)^{\tau(m)}q_2^{-D_m}\)，与固定有限 X 无关。故 (R_m) 的 bidegree 为 ((D_m,D_m))，并且

\[
 Z_m:=\operatorname{div}_X R_m
       =\overline T_m-D_mB.                                   \tag{7}
\]

这付清逐个有限输入的 cusp poles，而不是只在开曲面上宣称其 principal。

全 isogeny 与 primitive cyclic correspondence 的准确关系是

\[
        T_m=\sum_{k^2\mid m}T_{m/k^2}^{\rm prim}.               \tag{8}
\]

证明可逐个 integral matrix 取 entries 的最大公因数 k：\(\gamma=k\gamma_0\)，\(\det\gamma_0=m/k^2\)，且二者定义同一 Möbius graph。primitive integral matrix 给 cyclic isogeny；一般无 CM 的点处每个分量重数为一，特殊交点不产生新的 divisor 分量。因而不能把每个 m 的 (T_m) 当作互不重复的 primitive support。

## 3. 原 (\Psi(J_m)) 与 (R_m) 的逐 m、保规范识别

在 (II_{2,2}\simeq(\operatorname{Mat}_2(\mathbb Z),-\det)) 的有序 domain \(\mathbb H^2\) 上取 \(\Gamma=SL_2(\mathbb Z)\times SL_2(\mathbb Z)\) 的像。负 primitive vector 对应 determinant-N primitive matrix；其正交除子是同一 determinant-N Möbius graph。原定理的 \(\lambda=k\lambda_0\) 给出 \(m=Nk^2\)，阶数为一，恰为(8)。所以原 \(\Psi_m:=\Psi_M(\cdot,J_m)\) 的有限零除子与(4)完全相同，无有限极点。

还须排除商掉 finite divisor 后残留的非代数 unit，以及未付的正实 normalization constant。这里可用以下特例证明，而无需一般 Hecke 相容性。

1. 因 (c_0(J_m)=0)，weight 为零。在 cone 上的 homogeneous degree0 函数降为 domain 上的函数，故其在有序 \(\Gamma\) 上的 multiplier 是实际 unitary character。每个 (SL_2(\mathbb Z)\) 的 abelianization 由标准生成元关系 (S^4=1,(ST)^3=S^2) 给 exponent12；所以 \(\Psi_m^{12}\) 是 \(\Gamma\)-invariant。这里不宣称含交换两因子等全正交群上的 character 已平凡。
2. 取原 product 的 chamber (y_1>m y_2)，并令 (y_1\to\infty)，(z_2) 在固定有限紧集。在 (II_{1,1}) product coordinates 中，正向因子的第一指数均正；第一指数为零的所有项的 exponent 都是 (c_0(J_m)=0)。负 Fourier 支持只有 (-m)，所以没有第一指数为负而仍在该 chamber 为正的因子。原收敛 product 在此给

\[
 \Psi_m=\varepsilon_m q_1^{\rho_{m,1}}q_2^{\rho_{m,2}}
                      (1+o(1)),\qquad |\varepsilon_m|=1.       \tag{9}
\]

原 cusp product 的收敛邻域允许固定 (y_2>0) 后使 (y_1y_2) 足够大；product 中第一指数正的因子在 (q_1\to0) 时整体趋1，局部对 (z_2) 一致。这是有限 cusp order，而不是使用此 split 情形不成立的 Koecher holomorphy。由周期性，12 倍的第一 Weyl exponent 为整数。交换两方向，同样得到另一个 generic boundary 上的有限阶。

这里的“整体趋1”还可直接支付 normal convergence：对 fixed m，(J_m) 是 j 的次数 m 多项式；在 height v 的水平线上，modular reduction 给 \(\log^+|J_m|\le C_m(1+1/v)\)（取 (v\le1\)）。对正 Fourier 系数用 q-circle Cauchy 界并取 (v\asymp n^{-1/2}\)，得 \(|c_m(n)|\le C_m e^{C_m\sqrt n}\)。于是正指数 a,b 的 product log 的绝对 majorant 由 \(e^{C_m\sqrt{ab}-2\pi(ay_1+by_2)}\) 控制，在 (y_1y_2) 充分大时可和，并在 (q_1\to0\) 时由一个固定的大 (y_1\) majorant 支配。负 ab 仅等于 (-m)，相应 a>0 的因子只有有限个；ab=0 的 exponents 为零。这使(9)在 generic boundary 的有限阶和 uniform leading 真正成立，而非将逐项极限代成乘积极限。
3. 因而 \(\Psi_m^{12}\) 在两个 generic boundary 上亚纯，并降到 ((j(z_1),j(z_2))\in\mathbb C^2)；椭圆点由有限商的不变亚纯函数下降处理。剩余 corner 为 codimension2，亚纯 Hartogs 延拓给整个 \(\mathbf P^1\times\mathbf P^1\) 上的亚纯函数，故为有理函数。
4. \(\Psi_m^{12}/R_m^{12}\) 是有理函数，且在 affine \(\mathbb A^2\) 无零／极除子。\(\mathbb C[X,Y]\) 是 UFD，故这是常数。连通的 \(\mathbb H^2\) 上 \(\Psi_m/R_m\) 本身遂为一个常数 (C_m\)。此处亦得 ordered subgroup 上实际 character 平凡。
5. 再与 monic (q_1^{-D_m}) leading 比较(9)。对一个开集内全部固定 (z_2)，常数性强迫

\[
 \rho_{m,1}=-D_m,\qquad\rho_{m,2}=0,\qquad
 \Psi_m=C_m R_m,\quad |C_m|=1.                              \tag{10}
\]

这是从原 unimodular prefactor 和 cusp leading 推导 Weyl／normalization；没有暗删随 m 变化的实常数。交换 chamber 的 Weyl vector 可以不同，不能将(10)中的 Weyl vector搬到其他 chamber。

结合(3)、(c_0(J_m)=0\)，得到真正可消费的、逐 m 无加法常数的等式

\[
                 \Phi_m:=\Phi(J_m)=-4\log|R_m|.                \tag{11}
\]

常数输入 (1) 不适用 (c_0=0) 的简化：其 lift weight 为 (1/2)，character／automorphy line 和(3)中的 \(\log|Y_M|+\Gamma'(1)/2+\log\sqrt{2\pi}\) 必须保存。记这一个固定输出为 \(\Phi_0=\Phi(1)\)，不将其改成 weight0 rational-function log。

## 4. Poincaré–Lelong 的尺度和 finite complexification

固定顺序与规范

\[
 dd^c:=\frac{i}{2\pi}\,\partial\bar\partial,
 \qquad dd^c\log|f|^2=[\operatorname{div}f].                 \tag{12}
\]

ordinary principal Green pair 是 \((Z_m,g_m)\)，其中

\[
 g_m=-\log|R_m|^2,\quad [Z_m]+dd^cg_m=0.
\]

原 native Green 的实际尺度为 \(\Phi_m=2g_m\)。因此正确的 principal pair 为

\[
           (Z_m,g_m)\quad\hbox{或}\quad(2Z_m,\Phi_m),         \tag{13}
\]

不能把 \((Z_m,\Phi_m)\) 称为 principal。对开集 \(U=\mathbb A^1\times\mathbb A^1\) 有 \(dd^c\Phi_m=-2[T_m]\)；对全 X 则

\[
 dd^c\Phi_m=-2[\overline T_m]+2D_m[B].                       \tag{14}
\]

原定理先分别作用于整数基 (1,J_1,J_2,\ldots\)，再定义复线性的 finite Green 数据

\[
 \Phi_N(r)=a_0(r)\Phi_0-4\sum_{m\le N}b_m(r)\log|R_m|.       \tag{15}
\]

这不是将一般 complex (F_{r,N}) 说成原定理的整数输入；一般也不存在 \(\prod_m R_m^{b_m(r)}\) 这个单值亚纯函数。若整数 exponents 才可直接取 meromorphic product；此处合法对象是复化后的 divisor／Green pair。

finite tail 的准确 compactified principal pair 是

\[
 \left(2\sum_{m\le N}b_m\,[\overline T_m-D_mB],\;
              -4\sum_{m\le N}b_m\log|R_m|\right).            \tag{16}
\]

如果只记录 \(2\sum b_m\overline T_m\)，就明确留下 \(2\sum b_mD_m B\) 的 boundary 腿，不能同时把它删除又声称是 native principal pair。(a_0(r)\Phi_0\) 及其 weight／metric／character 线另保；尾小不会把它消掉。

## 5. 实际全 Green 尾：先 local log，再另付 global coefficient height

### 5.1 固定 interior compact 的直接 log 费用

取 \(K\subset\mathbb H^2\) compact，包在 \(K_1\times K_2\)。对(4)的一个 Hecke root
\(\alpha=j((az_2+b)/d)\)，其 preimage 的虚部 v 在 \([c_K/m,C_Km]\)。任一 modular reduction 满足

\[
 \Im\gamma w=\frac{v}{|cw+d|^2}\le
 \begin{cases}v,&c=0,\\1/v,&c\ne0,\end{cases}
\]

故 reduced height 至多 (C_Km)。由基本 j cusp 展开在标准 fundamental domain 上的界，

\[
       \log(1+|\alpha|)\le C_Km.                            \tag{17}
\]

负部不能用 sup 控制。其 uniform (L^1) 性可直接证明：对每个 (z_0\in K_1\)，取一个小 chart 使 \(j(z)-j(z_0)=h(z)^e\)，h 在该 chart 单叶。对任意 \(\alpha\in\mathbb C\) 分解 \(h^e-(\alpha-j(z_0))=\prod_{\nu=1}^e(h-\beta_\nu)\)。变元 h 的 Jacobian 在缩小 chart 上有界，而且
\(\int_{|v-\beta|<1}-\log|v-\beta|\,dA(v)=\pi/2\)，与 \(\beta\) 无关。有限个 chart 覆盖给

\[
 \sup_{\alpha\in\mathbb C}\int_{K_1}\log^-|j(z)-\alpha|dA(z)
                 \le C_{K_1}.                              \tag{18}
\]

(17)–(18)逐因子求和即可得

\[
       \|\log|R_m|\|_{L^1(K)}\le C_KmD_m.                  \tag{19}
\]

允许 Hecke divisors 穿过同一 compact；不存在跨全部零点的有限 log supnorm。

### 5.2 固定 coarse compactification 上独立支付的 height／L1 费用

为了把边界也一起取极限，不能仅将(19)称为全 X 上的界。以下另付所需 coefficient height。

在固定 torus \(|X|=|Y|=1\) 上，所有 Y 可取 H 中一个共同 compact 的 reduced j-preimages：有限 Y 禁止 height 趋无穷，而 reduced fundamental domain 的 height 有统一下界。对这些 preimages 使用(17)，有 \(\log(1+|\alpha|)\le Cm\)。由(4)

\[
 \sup_{|X|=|Y|=1}|R_m(X,Y)|\le e^{CmD_m}.
\]

R_m 的 bidegree 已由(7)证明；二维 Cauchy 估计遂给每一个 polynomial coefficient

\[
 R_m=\sum_{0\le i,j\le D_m}c_{ij}^{(m)}X^iY^j,\qquad
                  |c_{ij}^{(m)}|\le e^{CmD_m}.               \tag{20}
\]

这里的 C 是固定的通用常数，不含 r、m 或 source window。取 \(\mu\) 为 \(\mathbf P^1\) 上总质量1的 Fubini–Study measure，affine chart 的 density 为 \(\pi^{-1}(1+|X|^2)^{-2}\)。在 product probability volume \(\mu\times\mu\) 下，(20)给

\[
 \log^+|R_m(X,Y)|\le CmD_m+2\log(D_m+1)
                        +D_m\log^+|X|+D_m\log^+|Y|.         \tag{21}
\]

后两项在 \(\mu\) 下有固定有限积分。另一方面，对每个有限 Y，R_m 对 X 始终 monic degree (D_m)，故

\[
 \int\log^-|R_m(X,Y)|\,d\mu(X)
 \le\sum_{\nu=1}^{D_m}\int\log^-|X-\alpha_\nu(Y)|d\mu(X)
 \le D_m/2.                                                 \tag{22}
\]

最后一步只用 \(d\mu\le\pi^{-1}dA\) 与负部支在 \(|X-\alpha|<1\)。对 Y 再积分，即有真正的全 coarse X 费用

\[
 \boxed{\quad\|\log|R_m|\|_{L^1(X,\mu\times\mu)}
                      \le C_XmD_m.\quad}                   \tag{23}
\]

在 boundary 处 R_m 是有理函数，log 的 poles 仍为 (L^1)；(21)–(23)已经包含这部分，而非假设 cusp away。这是 fixed complex-coarse metric-volume 的结论，不是算术 Faltings／Arakelov height 的比较，也不是所有成长几何／源规范的一致界。

### 5.3 Green 和 current 的 operator 尾

因 \(D_m=m\sum_{d\mid m}d^{-1}\le m(1+\log m)\)，对任意 (0<s<t<1\) 有有限常数 \(C_{s,t}\) 使 \(mD_ms^m\le C_{s,t}t^m\)。由(2)、(23)，

\[
 \left\|\sum_{m>N}b_m(r)\log|R_m|\right\|_{L^1(X)}
 \le C_XC_{s,t}p_{A_s}(r)\frac{t^{N+1}}{1-t}.              \tag{24}
\]

native Green 尾是同界乘4。相同 right side 将 \(p_{A_s}(r)\) 替为 \(C_{L,s}\|r\|_{du}\)，就得到 fixed source-window 的原 du 到这个 fixed global (L^1_X\) norm 的 operator tail；不能去掉 (C_{L,s}\) 的 L／s 依赖。全 \(\mathcal S_{\exp}\) 则在同一强半范数有界的源集上一致。

再取 \(\omega=\pi_1^*\omega_{FS}+\pi_2^*\omega_{FS}\)。由 effective \(\overline T_m\) 的 bidegree，

\[
 \operatorname{mass}_{\omega}(\overline T_m)=2D_m,\quad
 \operatorname{mass}_{\omega}(B)=2,\quad
 \operatorname{mass}_{\omega}(Z_m)\le4D_m.                  \tag{25}
\]

因此 \(\sum b_m[\overline T_m]\)、\(\sum b_m[Z_m]\) 均在全 X 的 current mass norm 下绝对收敛，尾由 \(C'_{s,t}p_{A_s}(r)t^{N+1}/(1-t)\) 控制。特别

\[
 D(r):=\sum_{m\ge1}b_m(r)D_m                              \tag{26}
\]

绝对收敛，boundary current 尾也已支付。设

\[
 Z(r)=\sum_{m\ge1}b_m(r)([\overline T_m]-D_m[B]),\quad
 G(r)=-4\sum_{m\ge1}b_m(r)\log|R_m|.
\]

由全 (L^1\) 对 distributional (dd^c\) 的连续性以及(12)，得全尾精确身份

\[
 \boxed{\quad dd^cG(r)=-2Z(r),\qquad
 \Phi_\infty(r)=a_0(r)\Phi_0+G(r).\quad}                    \tag{27}
\]

固定 \(\Phi_0\) 原有的 automorphy／metric 腿一直保留；对 tail 的(24)不需要重新估计它。(27)的 full \(\Phi_\infty\) 是“该固定标签腿＋已付 global (L^1) 的 G”，本稿不将 full \(\Phi_\infty\) 一并纳入(24)的 operator norm 断言。若只在 \(\mathbb H^2\) 局部消费，则(19)本身已足够；若在 coarse X 消费 balanced G／Z，则必须连(20)–(25)一起引用。

各零支持的并可稠密；(25)仍使其成为合法的 order0 current。通常不能把 (Z(r)\) 叫作 ordinary divisor、把 G 叫作 smooth Green，或把它们叫作某一个实际 meromorphic function 的 principal pair。这里也没有创建一个广义输入定理并声称原定理已覆盖 essential cusp；这是整数基数据的实际 (L^1\)／mass completion。

## 6. 重复支撑的平方 Möbius 反演须用全尾

由(8)、(25)的绝对质量可合法重排，

\[
 \sum_{m\ge1}b_m[T_m]=\sum_{N\ge1}A_N[T_N^{\rm prim}],
 \qquad A_N=\sum_{k\ge1}b_{Nk^2}.                          \tag{28}
\]

各 generic primitive component 的真正系数是 (A_N\)，不是 (b_N\)。由(2)
\(|A_N|\le p_{A_s}(r)s^N/(1-s^{3N})\)，故仍超几何。绝对收敛同时允许平方 Möbius 反演

\[
       b_N=\sum_{k\ge1}\mu(k)A_{Nk^2}.                     \tag{29}
\]

展开右端后，(b_{Nh^2}\) 的 coefficient 为 \(\sum_{k\mid h}\mu(k)\)，仅 h=1 留下。双和的绝对性由 \(\sum_h d(h)s^{Nh^2}<\infty\) 支付。因而“全部 primitive coefficients 为零”确能推出全部负系数为零；有限 m 的逐项独立断言则不成立。

即使 supports 稠密，(28)的 coefficient 可在一个 generic primitive curve 上、避开其与其余可数 curves 的离散交点后按 measure restriction 识别：其余有效 divisor measures 在该曲线上给零质量，绝对质量和保留该性质。这只识别 raw current，不自动给 quotient 上的 primitive 几何非退化。

## 7. principal／relative／primitive 的净后果

有三个不同的可消费对象，必须逐项标注。

1. **Raw logarithms／currents。** (24)–(29)闭合全 (\mathcal S_{\exp}\) 的实际尾，保留非零负系数和 primitive cyclic raw current 的信息。它们没有自动消去405及其平移；关系下降仍须 actual coefficient kernels／(a_0\)／boundary 测试。
2. **正确尺度的 full principal pair quotient。** 每个 finite pair(16)都是复化的 principal pair。若采用对本稿 (L^1\times\)current-mass topology 连续的完成化 quotient，则其极限 \((2Z(r),G(r))\) 的像也是零。这是指定连续 quotient 中的结论，不是说无限 pair 本身来自普通单值有理函数，也不是未经定义就把 ordinary arithmetic Chow quotient 换成完成化 quotient。
3. **不扣 boundary 的 relative 记录／degree primitive 投影。** 只保 \(2\sum b_m\overline T_m\) 时，额外留下明确的 \(2D(r)B\)；还保有 (a_0(r)\) 的 constant-input weight／metric 线。若“primitive”按相同 bidegree 扣 boundary／degree line，即 \(\overline T_m-D_mB\)，则每个 m 的 primitive pair 全部 principal，故其连续完成化 primitive 类也全零。于是537即使 raw current 非零，也不会在这个标准 primitive quotient 中幸存；405和537会被同一个 principal 机制吞掉。只保 relative 数值 (a_0,D\) 时须再实测405，它们不天然构成正确下降。

这就是本特例的明确门：raw completion 合法且有完整尾，不等于构造出同时消405并保537的几何 quotient。有限 m 的 \(\overline T_m\) cycle 在 coarse compactification 中的 divisor／degree 身份已付；有限位原生 special-cycle 模型、bad-prime multiplicities／vertical corrections、原 arithmetic principal 关系及全部 mixed RR 的对应，均不由本复解析论文或 \(R_m\in\mathbb Z[X,Y]\) 自动给出。后者只提供一个实际 rational-function 的整多项式模型，不能代替模型间的识别。

## 8. root 消费的 premise-closure 记录

* 对象／域／norm：全 complex \(\mathcal S_{\exp}\) 源；先 integer (J_m\) lift、后 complexification。fixed (X=\mathbf P^1\times\mathbf P^1\)、product FS (L^1\) 和 divisor current mass；也给任意 fixed interior K 的独立 local 界。
* 源与增长量词：每个 fixed (0<s<t<1\) 用一个实际 (p_{A_s}\)；fixed-window 原 du 支付 (C_{L,s}\)。(mD_m\) 的 polynomial growth 已与 supergeometric tail 合并，Hecke degree、重复支持和 boundary 全尾没有省略。
* paid dependencies／errors：原13.3 的 integer-input product、weight／character／Weyl；special-case divisor＋character12次＋finite-cusp 延拓证明(10)；monic norm 的全 coefficient height(20)支付 coarse compactification 而非只靠 local 界。无数值误差，tail 为(24)的显式几何 upper。
* 实际 coefficient 方向：(r\mapsto b_m\) 来自同一 (L_r(j)\)；完整 cyclic coefficient 为 (A_N=\sum_k b_{Nk^2}\)。原 native Green 是 ordinary principal Green 的2倍，(13)固定尺度。
* 未付 coverage／coupling：未识别 arithmetic integral-model current、原特殊 cycles 的有限位长度、classical full (B_\zeta\)、mixed RR、positive Hermitian pairing、cofinal height 和 actualq/core/coupling/Ξ。不能将 m 当经典 prime-power 指标。
* strongest-old 比较／实际净值：旧 finite-rank、essential-cusp 域失败以及 scalar rational-function 的有限 principal 结论不因本稿而改变；新支付的是该同一无限实际源对 native product 的 special-case normalization、global (L^1\)/mass 全尾及含 cusp 的 current 身份。其 geometric primitive quotient 仍全 principal，独立 Weil 正号和 whole4/5 的实际 bottleneck 未解除。是否足以消费 C046 的一个数学轮由 root 连同 source／relation／fresh 三稿统一判定。

不得从“完成化 Green 合法”继续无期限改 N、radius、j affine 常数或换 level；若405下降／537 primitive／native mixed 门未过，应按 C046 止于已付范围，回到宏观选择。
