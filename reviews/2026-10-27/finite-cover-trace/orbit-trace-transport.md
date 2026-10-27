# Whole-cusp orbit trace：有限 modular cover 的标准运输核查

2026-10-27；`/root/cover_trace` 独占原稿。执行 [唯一准入比较](../marked-cusp/next-finite-cover-trace-admission.md)，不恢复 C047 预算、不预建 C048。本稿给出 584 的 slit-Cauchy 论证与标准有限覆盖 trace 的逐项合成；计轮建议为 **0 数学轮的旧推论／准入核查**，须 root 比较后决定，文件存在不代 root 消费。

## 1. 实际对象与 coarse 曲线约定

令 Γ 为 SL2(Z) 的任意有限指数子群，先取其在 PSL2(Z) 中的像 Γbar。以下 XΓ 指紧化的 **coarse** 复曲线 Γbar\H*，π=j:XΓ→X(1)=P1 是实际有限非恒定映射。不要求 congruence、torsion-free 或 Γ 含 −I。所有 cusp width w 都按 Γbar 对 T 的局部轨道定义；不用 SL2 的 lift-order 冒充 coarse width。若改用 orbifold／stack 微分，须先另给到本 coarse 全纯微分的映射，不在本稿中自动识别。

输入 ω∈H0(XΓ,Ω1) 是全局全纯微分；可为 0、可为复微分，不要求实结构或任何 q 系数正性。每个 cusp c∈π^−1(∞) 取一个固定复数 λc，权重作用于 **whole cusp**，不能在其 w 个 sheet 中再任意分别加权。对 ALLcomplex 物理源 r=e^(u/2)f∈S_exp，所有 p_(N,k)(r)=sup exp(N|u|)|D^k r(u)| 有限，定义

\[
 L_r(z)=\int_{\mathbb R}r(u)e^{uz}du,\qquad
 R_c(r)=\operatorname{Res}_c\big(L_r(\pi)\omega\big),\qquad
 R_\lambda(r)=\sum_c\lambda_cR_c(r). \tag{1}
\]

Lr 是 entire；c 处允许 isolated essential，residue 是实际 Laurent 系数。对一个固定小 cusp 圈，π 有有限上界 M，all-S_exp 给 ∫|r|exp(M|u|)du<∞，所以 (1) 的 contour 与 u 积分可绝对互换。源域没有裁成 compact，特别不会删去 405 的 noncompact Pan。

π 在 H 中的有限 branch values 只能是 0、a=1728。0 上 coarse ramification e 为 1 或 3；a 上为 1 或 2，因为它们分别由 PSL2 的 order3/order2 stabilizer 与 Γbar-stabilizer 的商给出。除此以外 π unramified。下面只用 e∈{1,2,3} 与 branch-values 的实际位置。

## 2. 一个 whole cusp 的 trace 与全部系数

固定 cusp c。选 rational cusp 的 SL2(Z) 变换作局部坐标，令 t=q_c，width 为 w，则

\[
 x=t^w,\quad z=J(x)=x^{-1}+744+196884x+\cdots,
 \qquad \omega=\sum_{n\ge1}a_n t^{n-1}dt. \tag{2}
\]

n≥1 来自 **coarse 全纯** ω；没有 a0 dt/t。z 在该 cusp 的 pole-order 为 w。设 h=ω/dπ，其单 sheet 分支是

\[
 h(t)=\frac{1}{w xJ'(x)}\sum_{n\ge1}a_n t^n. \tag{3}
\]

在 ∞ 附近 x=x(z) 是 J 的唯一小逆分支；c 的 w 个 sheets 对应 t_k=ζ_w^k x^(1/w)。对这一个完整 orbit 求和，得到实际恒等式

\[
 \boxed{T_c(J(x))=\sum_{k=0}^{w-1}h(t_k)
 =\frac{\sum_{m\ge1}a_{mw}x^m}{xJ'(x)}.} \tag{4}
\]

这同时核清了两项：w∤n 的全部系数被 roots-of-unity 求和消去；单 branch 的 1/w 被 orbit 大小 w 抵消，whole trace **不再有额外 1/w**。因此

\[
 T_c(z)=-a_wz^{-2}+O(z^{-3})=O(z^{-2}). \tag{5}
\]

若 a_w=0，可衰减更快；不假定非零或给每个 reader 相同 leading term。原 a_n 的全系数筛选由 (4) 给出，不是把 q_c 当成 width1 的 q。

也可选 exact local parameter v=(1/π)^(1/w)=t·unit(t^w)，使 π=v^−w，ω=Σ_(n≥1)b_n v^(n−1)dv。则

\[
 h=-\frac1w\sum_{n\ge1}b_nv^{n+w},\quad
 T_c(z)=-\sum_{m\ge1}b_{mw}z^{-m-1},\quad
 \operatorname{Res}_c(e^{u\pi}\omega)
 =\sum_{m\ge1}b_{mw}\frac{u^m}{m!}. \tag{6}
\]

(6) 的最后一式只作 local entire-kernel 的 coefficient check；小圈上 e^(uπ) 正常收敛，Cauchy 系数估计给每个固定 u 的合法 residue。b_n 与 (2) 的 a_n 分属不同 local parameter，不将其全序列混同。

## 3. 不是假设 simply-connected 的单值延拓

令 Ω=C\[0,a]。Ω 的 π1≅Z，其 generator 是绕整个 cut 的环，等价于 ∞ monodromy 的反向。这个 monodromy 在 c 的 w 个 sheets 上恰为一个 w-cycle，并保持该 **整个 orbit 集合**。ω 是 XΓ 上全局单值微分，故延拓 h 只按同一 sheet permutation 改排；(4) 的和在 generator 下不变。

于是 Tc 从 ∞ 小邻域唯一延成 Ω 上单值 holomorphic function。这里不要求任意单 sheet 单值，也不要求整个 cover 的 monodromy 平凡。允许 w>1；whole cusp 权重不破坏 orbit invariance。

在有限 branch point z0∈{0,a} 的任一 preimage，选 coarse local coordinate v，使 z−z0=v^e，ω=A(v)dv 且 A holomorphic。则

\[
 h=\frac{A(v)}{e v^{e-1}}
 =O(|z-z_0|^{-1+1/e}). \tag{7}
\]

Tc 的各项均满足这个 subpole 界。0 处最坏 O(|z|^−2/3)，a 处最坏 O(|z−a|^−1/2)，e=1 项 bounded。即使所选 orbit 在有限点的局部 monodromy 下不封闭，各 bank 的分支仍满足这些有限项 bounds，足以完成下一步。没有 other finite poles，也没有 endpoint simple pole。

## 4. 复 jump、Cauchy 方向和实际 residue

在 0<t<a 定义两个解析 bank boundary values Tc,±(t) 及

\[
 \nu_c(t)=\frac{T_{c,+}(t)-T_{c,-}(t)}{2\pi i}. \tag{8}
\]

(7) 给 νc∈L1((0,a);C)。**不取 Im Tc,+/π**：一般复 ω 没有 Schwarz reflection，后者通常是错公式。固定 λ 的 νλ=Σλcνc 仍为 complex L1。

对 Ω 的 keyhole contour 使用 Cauchy：端点小圆由 exponent<1 消失；大圆由 (5) 消失。正向 domain 的内边界 upper bank 从 0 到 a、lower bank 从 a 到 0，于是

\[
 \boxed{T_c(z)=-\int_0^a\frac{\nu_c(t)}{z-t}dt.} \tag{9}
\]

这与 584 的号相同。是直接 contour 恒等式，不先假设 endpoints 可去；(7) 已排除额外 endpoint 原子，(5) 排除 polynomial／constant 项。∞ 的 z^−1 系数还给 ∫νc=0。

从正向 t 小圈到 z=π(t) 的像，z 绕 ∞ **顺时针 w 次**，每次遍历恰读取 orbit 的下一 sheet。合在一起正好是一个顺时针 z 圈上的完整 trace，因此对任意 entire F，

\[
 \operatorname{Res}_c(F(\pi)\omega)
 =-\frac1{2\pi i}\oint_{|z|=R,\,CCW}F(z)T_c(z)dz
 =\int_0^aF(t)\nu_c(t)dt, \tag{10}
\]

其中 R>a 足够大；没有再除 w。也可直接在 (6) 中核 F=z^m：左边为 b_mw，右边等于 −coeff(z^−1) of z^mTc，恰为 b_mw。这排除了把 essential residue 错当普通 meromorphic degree 或反转系数方向。

取 F=e^(uz) 或 F=Lr，得到全源实际表示

\[
 K_c(u):=\operatorname{Res}_c(e^{u\pi}\omega)
 =\int_0^a e^{tu}\nu_c(t)dt\quad(u\in C),
 \qquad R_\lambda(r)=\int_{\mathbb R}r(u)K_\lambda(u)du
 =\int_0^aL_r(t)\nu_\lambda(t)dt. \tag{11}
\]

(11) 的第二重互换由 t 支撑固定 compact、νλ∈L1 与 all-S_exp 付清。所有 source 非 compact 尾保留。

## 5. 已付费用与未付 uniformity

记 Cλ=||νλ||1，N>a。对实 u 和每个固定 k，

\[
 |K_\lambda^{(k)}(u)|\le a^kC_\lambda e^{a u_+},\quad
 |R_\lambda(r)|\le C_\lambda\left(\frac1N+\frac1{N-a}\right)p_{(N,0)}(r). \tag{12}
\]

源域为 all-S_exp，这付的是强半范数费用。若 supp r⊂[−L,L] 且 L>0，则原物理 du=L2(du) 的费用更明确为

\[
 |R_\lambda(r)|\le C_\lambda
 \left[L+\frac{e^{2aL}-1}{2a}\right]^{1/2}\|r\|_{du}
 \le C_\lambda\sqrt{2L}e^{aL}\|r\|_{du}. \tag{13}
\]

对同一个 zero-extension 源，原 Dlog²=(2π)^−1∫log(2+|ξ|)|rhat(ξ)|²dξ≥log2·||r||du²，故 (13) 的原 Dlog 费用乘 (log2)^−1/2。Hlog 多一个 1，不改称完全同一范数。

Cλ 是固定 (Γ,ω,λ) 的有限常数；本稿不提供 Γ、ω、λ 变化时的统一上界、数值值或 arithmetic norm transport。指数 upper a=1728 对本 fixed-cut class 成立，但**不把 C047 的非零正端点、e^(1728b)/√b 必要增长复制到每个 reader**：其复 jump 可 cancellation、endpoint 可更高阶消失，也可能整个 reader 为 0。fixed-window 原费用不升级为全线 du/Dlog uniform boundedness。

全部 cusps 的等权总和为 0：全 trace π_*ω 在 P1 上全纯，因而为 0；或直接对 compact XΓ 去 cusp discs 用 Stokes。故 ΣcTc=0、Σcνc=0 和 ΣcRc(r)=0 一致。它是边界记录的线性约束，不是 primitive／RR 容量。

## 6. 强旧扣除、准确净范围和停止

现在 (11) 把当前整个 **fixed whole-cusp residue class** 运输进了 584 §5 已必须扣除的 compact-real complex measure reader。405 给实际 H>0、H∈S_exp、p=(D²−1/4)H 及全部 pb=τbp∈Pan；对实 t，MH(t)=∫Hexp(tu)>0。于是

\[
 R_\lambda(p_b)=\int_0^a e^{bt}(t^2-1/4)M_H(t)\nu_\lambda(t)dt. \tag{14}
\]

若 (14) 对全部实 b 为 0，旧 compact-Laplace uniqueness 立即给 (t²−1/4)MH(t)νλ(t)=0 a.e.；非零 multiplier 只可能在 t=1/2 消失，L1 不能集中于一点，所以 νλ=0。因而 Rλ 在 **全部 S_exp** 上为 0。反之 zero reader 当然消关系。此结论不依赖 RH、数值 b、原norm全线连续性或任何未经给出的 height／shadow。

所核的信息是：whole orbit trace 不因 width>1、多 cusp、复 ω、coarse elliptic point 而逃出旧 real-cut reader 门。证明只用标准 roots-of-unity trace、cover local ramification 与 584 的同一个 Cauchy contour；(14) 则是强旧现成 lemma。没有新的独立算术输入、经典全源正性、primitive 整过滤、mixed RR、growth/core/coupling/Ξ 或 whole4/5 UPPER 改善。因此建议按 **标准旧推论准入审查0轮** 保存，停止从本 class 自动换 level、cusp、basis 或 fixed masks 寻找非零 exact-Pan-descending reader。

本稿不覆盖 meromorphic ω 的额外 poles、非 whole-orbit 的 branch 数据、非 fixed/source-adaptive masks、非局部或额外 relative 数据、complex/unbounded spectrum、非 residue source map。family 每个 fixed member 在 exact descent 下为零，也不等于未逐层消 Pan 的 D′ 正逼近失败；本稿未给这类逼近的 defect budget 或 joint signed 极限。legal trace representation 不代全源 coverage，不等于所有 modular／Maass／Pic／算术Chow 方法不可能，更不能单独完成长期 Goal。

## 7. 消费前件简表

| 项目 | 本稿实际范围 |
|---|---|
| 对象／domain-range | coarse finite modular cover；全纯 ω；whole cusp 固定复权；all-S_exp→C 实际 residue |
| relation／商／physical 角色 | physical r=e^(u/2)f；reader 未先商；405 全 noncompact 平移实际进入域，消去关系则 reader=0 |
| 量词与源成长 | 每给定 Γ/ω/λ 全 S_exp、全部实 b；固定 N>1728 的强费；不报跨 Γ 统一常数 |
| 符号／系数 | 单branch1/w、whole trace无额外1/w；w∤n全滤；Cauchy负号与residue反向相抵；complex jump |
| 误差／依赖 | exact analytic identities；端点 subpole 小圆→0、∞O(z^-2)；无需浮点或新外部论文 |
| coverage／coupling | finite scalar boundary数据；不付 primitive/RR/完整ζ/growth/core/coupling/Ξ |
| 最强旧净值 | 584 slit-Cauchy＋标准trace→compact-real reader→405旧唯一性；数学净增量建议0轮 |
| 停止与合法修复 | 停当前 whole-cusp residue class；保额外实际数据／不同source-map／有费非局部与未逐层下降的D′ family |

本稿只编辑此独占文件。STATE、cadence、root消费、统一结算与Git发布由 root 按实际版本另行处理。
