# L_r(j) 的 Fourier 源核、模 Faber 截断与原范数尾界

2026-10-27；执行 STATE 保存的实际截断／lift 比较，本分支只处理解析输入与截断，不改 STATE／cadence／Goal／文献库／合同。G20261027、原0c4f基线和≤582资产保持；运行实例由root实际get_goal核验，本分支不创建实例或认定数学完成。

恢复已读 README／STATE、check→show、Goal、A20261027、D20261027C及宏观前沿。本稿不重做 essential-cusp 或 Baire 并把它计为新信息；目标是给同一实际物理源的 coefficient map、合法模截断与完整解析尾。计轮／root消费由root在与 Green／关系分支对齐后决定。

## 1. 对象、规范与来源

原物理源为 r=e^(u/2)f，Fourier约定 \(\widehat r(t)=\int r(u)e^{-itu}du\)。令

\[
 L_r(z)=\int_{\mathbb R}r(u)e^{zu}du,\qquad
 F_r(\tau)=L_r(j(\tau)),\qquad q=e^{2\pi i\tau}.
 \tag{1}
\]

首先允许全部 \(r\in\mathcal S_{\exp,\mathbb C}\)。此处定义含 \(e^{u j(\tau)}\)，不是此前已否的 arch-only \(F(x+i v e^u)\) transport；对固定 \(\tau\)，\(j(\tau)\) 有限，全部线性指数矩已足以使(1)合法。它不需要一个 \(e^{C e^u}\) 的源尾假设。

取固定标量 \(II_{2,2}\)／weight0 模型，\(j(q)=q^{-1}+744+196884q+\cdots\)。真实输入及 product 角色仍归 [Borcherds 作者稿 §13、Example13.5](https://math.berkeley.edu/~reb/papers/aut/aut.pdf)，本地作者版64页、448471字节，SHA256 `93618b64a0c07f68a085b0b520079b1062a98ff7672159f34f77b1463e0724d2`；本次只延用这一原件和标准 Cauchy／Faber 计算，不串论文。

j 的 q 展开在 \(0<|q|<1\) 全纯。其整数系数也可直接由 \(j=E_4^3/\Delta\)、\(E_4=1+240\sum_{n\ge1}\sigma_3(n)q^n\)、\(\Delta=q\prod_{n\ge1}(1-q^n)^{24}\) 看出。以下的 \(j'(q)\) 始终是 q 导数，不能漏／添 \(2\pi i\)。

定义强源半范数

\[
 p_A(r)=\int|r(u)|e^{A|u|}du,\qquad A\ge0.
 \tag{2}
\]

它在 \(\mathcal S_{\exp}\) 连续：任取整数 \(N>A\)，有
\(p_A(r)\le 2\sup_u e^{N|u|}|r(u)|/(N-A)\)。因此 L_r 为 entire，所有紧集上的换序／求导由相应有限 A 及多项式 u 矩支付。

## 2. 全部 Fourier 系数有同一实际源核

写

\[
 F_r(q)=\sum_{n\in\mathbb Z}a_n(r)q^n.
\]

对任意固定 \(0<s<1\)，令

\[
 K_n(u)=\frac1{2\pi i}\oint_{|q|=s}
       e^{u j(q)}q^{-n-1}dq
 =\frac{s^{-n}}{2\pi}\int_0^{2\pi}
       e^{u j(se^{i\theta})}e^{-in\theta}d\theta.
 \tag{3}
\]

对每个 u，该值与 s 无关；它是 punctured-disc 上的 Laurent 系数。K_n 为 u 的 entire 函数。若记

\[
 A_s=\max_{|q|=s}|\Re j(q)|,\qquad
 M_s=\max_{|q|=s}|j(q)|,
\]

则对实 u 和任意整数 \(\ell\ge0\)

\[
 |K_n^{(\ell)}(u)|\le s^{-n}M_s^{\ell}e^{A_s|u|}.
 \tag{4}
\]

由(2)–(4)绝对换序，全部 \(r\in\mathcal S_{\exp}\) 有精确源公式

\[
 \boxed{\ a_n(r)=\int r(u)K_n(u)du\ },\qquad
 |a_n(r)|\le s^{-n}p_{A_s}(r).
 \tag{5}
\]

在 height \(v=-\log s/(2\pi)\) 的实参数写法是

\[
 a_n(r)=e^{2\pi nv}\int_0^1 F_r(x+iv)e^{-2\pi inx}dx.
\]

特别对负系数 \(b_m(r):=a_{-m}(r)\)，\(m\ge1\)，

\[
 |b_m(r)|\le s^m p_{A_s}(r)\quad(0<s<1).
 \tag{6}
\]

于是每个固定强源的负系数超几何衰减：\(\limsup_m|b_m(r)|^{1/m}=0\)。此结论的常数依赖 s；不能令 s 随 m 趋零而忽略 \(p_{A_s}\) 的增长。对任意固定 s，(6)在 \(p_{A_s}\) 有界的源族上一致。

常数项是 \(a_0(r)=\int rK_0\)，不是可以忽略的 pole moment。其低阶实际数据为

\[
 K_0(0)=1,\quad K_0'(0)=744,\quad
 K_0''(0)=744^2+2\cdot196884=947304.
 \tag{7}
\]

负核有三角首项：\(K_{-m}^{(k)}(0)=0\) 对 \(k<m\)，而 \(K_{-m}^{(m)}(0)=1\)。这是因为 j^k 的最低 q 次数为 −k。所有常数／负系数作为线性泛函各自有非零内容，不能把它们按名称当作自动消去405的边界。

## 3. 固定源窗的原 du／Dlog 费用

对 \(r\in C_c^\infty((-L,L);\mathbb C)\)，(5)在原 \(L^2(-L,L;du)\) 上延拓为线性泛函，其精确 squared dual norm 为

\[
 \|a_n\|_{du,*}^2=\int_{-L}^{L}|K_n(u)|^2du.
 \tag{8}
\]

这里利用 \(C_c^\infty((-L,L))\) 在该 L2 空间中稠密；不把任意有额外几何约束的源子类也称为达到这一 norm。由(4)得到可用的上界

\[
 |a_n(r)|\le s^{-n}C_{L,s}\|r\|_{du},\qquad
 C_{L,s}^2=
 \begin{cases}
 (e^{2A_sL}-1)/A_s,&A_s>0,\\
 2L,&A_s=0.
 \end{cases}
 \tag{9}
\]

粗一些可用 \(C_{L,s}\le\sqrt{2L}e^{A_sL}\)。负系数相应乘 \(s^m\)。沿用[原 zero-extension Dlog 规范](../../../goals/reviews/2026-10-22-source-dependent-divisor-families-and-relative-sections.md#3-原dudlog费用固定窗成功全线全高度另付)，

\[
 \|r\|_{D_{\log}}^2=(2\pi)^{-1}
  \int\log(2+|t|)|\widehat r(t)|^2dt
 \ge(\log2)\|r\|_{du}^2.
\]

所以(9)给 \(s^{-n}C_{L,s}/\sqrt{\log2}\) 的原 Dlog 上界。553的原 Hlog 范数使用 Fourier 权 \(1+\log(2+|t|)\)，相应给 \(s^{-n}C_{L,s}/\sqrt{1+\log2}\) 上界。没有在此报 Hlog／Dlog 的精确 dual norm，也不将它们与 du 等同。

全线 \(\mathcal S_{\exp}\) 的(5)用的是强半范数(2)，不是一个全线 du 或 Hlog uniform 常数。对真实平移 \(r_b(u)=r(u-b)\)，

\[
 L_{r_b}(z)=e^{bz}L_r(z),\quad
 p_A(r_b)\le e^{A|b|}p_A(r),\quad
 |b_m(r_b)|\le s^m e^{A_s|b|}p_{A_s}(r).
 \tag{10}
\]

这些是已付 upper，既不证明必要 height 增长，也不允许把固定 b 的费用宣称全平移统一。

## 4. 整数 Faber 基及真正保持模性的截断

定义多项式 P_m(z) 的 generating function

\[
 G(q,z):=-\frac{qj'(q)}{j(q)-z}
      =1+\sum_{m\ge1}P_m(z)q^m.
 \tag{11}
\]

q=0处奇性可去。对每个 m，P_m 是 monic degree m 的整数多项式；递推来自整数系数的 qj(q)，其逆幂级数和 q 导数都保整数。最初两项是

\[
 P_1(z)=z-744,\quad
 P_2(z)=(z-744)^2-393768.
\]

令 \(J_m(\tau)=P_m(j(\tau))\)。它们的精确 principal part 为

\[
 J_m(q)=q^{-m}+O(q),
 \qquad a_0(J_m)=0.
 \tag{12}
\]

可直接验证(12)：把 \(j(q)-j(p)\) 写成

\[
 \frac{p-q}{pq}H(q,p),\quad
 H(q,p)=1-pq\sum_{n\ge1}c_n
                   \sum_{a=0}^{n-1}q^{n-1-a}p^a.
\]

H−1的每项都含正的 p、q 次数。对 \(q(j(q)-j(p))=(1-q/p)H(q,p)\) 取 −q∂q log，q^m系数即 \(p^{-m}+O(p)\)，没有其他负次或常数。于是每个 J_m 都是整数 principal-part、constant0 的真实 weight0 模输入；不是仅在 cusp 写下的一段 Laurent 多项式。

对实际 r 定义

\[
 F_{r,N}(\tau)=a_0(r)+\sum_{m=1}^N b_m(r)J_m(\tau).
 \tag{13}
\]

它是 weight0 的 weakly holomorphic modular function，精确保留 F_r 的常数及前 N 个负系数。其正系数由完整 J_m 决定，通常不等于 F_r 的逐项正系数截断。普通 \(a_0+\sum_{m\le N}b_mq^{-m}\) 没有这些正系数修正，一般不模；不能拿普通 Laurent tail 代替(13)的模尾。

一般 complex r 的 a0、b_m不是整数，故 F_{r,N}自身不能无说明地直接套原整输入产品定理。合法路径是先对每个整数基 J_m应用原定理，再说明实际 divisor／Green／relative 输出怎样复线性组合；乘积、character或线丛是否相容仍由另外的原几何计算支付。常数a0在(13)对每个N都精确保留，原产品的 c0／2 weight及constant／metric腿不因“截断尾小”而消失。

## 5. 双半径的完整 Faber 重构与可审 tail

在 q=0附近 \(1/j(q)=q+O(q^2)\) 可作局部坐标，因此存在 \(\epsilon>0\)，使充分小 q 圆在 j 下成为绕一个大有界域的简单闭曲线、方向反转。给定任意 compact \(A\subset\mathbb C\)，可取 \(0<R<\epsilon\) 足够小，使 j 的 \(|q|=R\) 曲线包围 A，且 \(j(q)\notin A\) 对 \(0<|q|\le R\)。此时G在 \(|q|\le R,z\in A\) 解析，令

\[
 D_{A,R}=\max_{|q|=R,z\in A}|G(q,z)|<\infty.
\]

Cauchy给

\[
 \sup_{z\in A}|P_m(z)|\le D_{A,R}R^{-m}.
 \tag{14}
\]

对任意 \(0<s<R\)，以 j(|q|=s) 的反向大曲线作 entire L_r 的 Cauchy 积分，并用(11)逐项展开，得到准确重构

\[
 \boxed{\quad L_r(z)=a_0(r)+\sum_{m\ge1}b_m(r)P_m(z)\quad}.
 \tag{15}
\]

这不需要另援引 j(H)=C；只用 cusp 附近的局部反演和 entire L_r。由(6)、(14)，级数绝对且在 A上一致，其全尾满足

\[
 \sup_{z\in A}\left|L_r(z)-a_0(r)
                -\sum_{m\le N}b_m(r)P_m(z)\right|
 \le D_{A,R}p_{A_s}(r)
       \frac{(s/R)^{N+1}}{1-s/R}.
 \tag{16}
\]

固定compact源窗则有原 norm 版本

\[
 \text{左侧}\le D_{A,R}C_{L,s}
       \frac{(s/R)^{N+1}}{1-s/R}\|r\|_{du}.
 \tag{17}
\]

因此(17)是一个真正的 \(L^2(-L,L;du)\to C(A)\) operator tail upper；该窗全部原zero-extension Dlog源的 tail 常数只须再乘 \((\log2)^{-1/2}\)。源族只须满足相同 support L 和共同du界，不是仅一个已选源。全S_exp则由(16)对共同 \(p_{A_s}\) 界的源族一致。

对compact \(B\subset\mathbb H\) 取 \(A=j(B)\)，即给 \(F_{r,N}\to F_r\) 的原 norm compact-open tail。若要求任意固定阶 τ 导数，先把 A增厚一个固定δ，再用 z 的 Cauchy导数估计及 j在B邻域的固定导数界；所得仍是(16)/(17)的几何因子乘明确依赖B、δ、阶数的有限常数。这里不交换N与cusp height／source window的成长。

特别不能把 R、s固定后声称覆盖趋向 cusp 的 B_N：A=j(B_N)随height成长，允许的R、s及A_s、D、C都会变化。Green核、cycle/current norm、arithmetic height、全部 n总尾与完整Γ／pp／pole预算也不由C(A)尾自动支付。

## 6. 完整源可见性与关系的准确位置

所有负系数 \(\{b_m(r)\}_{m\ge1}\) 已共同分离全 \(\mathcal S_{\exp}\)。若它们全零，由(15)知L_r在任意compact上为a0；虚轴L_r(it)是L1源的Fourier变换、趋0，因此a0=0，再由Fourier唯一性r=0。反之，有限N读出仍有限rank，与前轮标准核门一致。

这项可见性同样保留非零405 raw源，而不是自动消去它们。对 \(P=(D^2-1/4)H\)、\(P_b(u)=P(u-b)\)，分部积分和(4)给全部系数的实际公式

\[
 a_n(P_b)=\int H(v)
       [K_n''(v+b)-\tfrac14K_n(v+b)]dv.
 \tag{18}
\]

因为H∈S_exp，该积分及每个固定b、n的强源费用合法；它不等于零的断言，也不认证全部b上principal下降。对537 compact非根 \(r_*=(D^2-1/4)(u\varphi(u))\)，同式把H替为uφ、b=0；负系数族至少一个非零来自共同注入，但特定系数／几何primitive是否可见仍须实际核。

没有把a0等同μ±，没有删常数／weight／character，也没有把raw source注入当正确商的注入。若原几何目标模principal后把全部输入类都杀掉，(15)的解析可见性不能救回537；若relative／Green记录保源，也要另核其405边界和mixed身份。

## 7. 消费范围与待对齐事项

本稿实际给出：(i)全S_exp合法的轮廓系数source核及强半范数；(ii)fixed窗du精确dual norm与可用upper；(iii)整数Faber基、保持常数和负主部的真正模截断；(iv)双半径全部尾的uniform operator上界；(v)负系数完整可见性及actualP_b的准确核公式。

这些是同一给定候选的解析截断设施，区别于重做essential/Baire。是否形成新完整研究迭代，须root结合实际native product／Green／relative运输与strongest-old净值后决定，本稿不自行source0／1结算。没有证明Green extension、primitive mixed RR、经典完整Bζ身份或独立正号。Whole4/5仍负惯性UPPER；actualq/core/coupling/Ξ未改变。

后续只消费已付对象和原费用：fixed source窗、fixed targetcompact及fixed两轮廓；全线强源、成长height、sum_n/arithmeticcurrent与product/cycle域分别付费。任何下游若只用(16)而声称Green/current或cofinal费用已闭，须冻结并重新核前件。
