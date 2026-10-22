# 实际 adelic character 线族的源、原费用与正反控制

2026-10-22。独占分支，仅消费本轮实际覆盖的指定对象，不改 STATE/cadence，不另开分支合同。
本分支的标准 character 线及源测试按来源准入与405/537/553强旧后果消费；
本轮 C037 的双位 periodic-clutch 精确分类是另一独占证明，由 root 统一结算一轮，本稿不将它降为来源0。
这里不将标准对象换表示计作独立容量或新 RH 后果。

## 1. 本轮对象确实比上一自由图线强

令 X=[A_Q/Q×]、U=[A_Q×/Q×] 为实际变换群胚及其 idele 限制端。
X 使用 A_Q 的加法拓扑，U 使用 ideles 的乘法 restricted-product 拓扑；
idele inclusion 给限制映射，但 U 不是 A_Q 加法拓扑中的开部分，不能当作 open immersion。
对 z∈C 定义 equivariant 线

\[
 L_z=A_Q\times C,\qquad q\cdot(a,v)=(qa,|q|_\infty^zv),
 \quad |q|_\infty^z=\exp(z\log|q|_\infty).                 \tag{1}
\]

这里只固定连续复线/群胚等变范畴；不宣称这是实际 Schwartz DGA 的已给可逆模或 proper 算术模型。
在 a=0 的 Q× 稳定群上，纤维字符是 |q|∞^z。
若 L_z≅L_w，纤维同构迫使 2^(z−w)=3^(z−w)=1。
于是 z−w 同时为 2πi Z/log2 与 2πi Z/log3 的元素，只能为0；否则推出正整数2、3幂相等。
故该指定 full-stack 线族真实非平凡，不能用“底层自由线”否定其等变 Picard 类。

在 U 上有实际不消失的等变截面

\[
 h_z(a)=|a_\infty|^z,\qquad h_z(qa)=|q|_\infty^zh_z(a).
                                                               \tag{2}
\]

故 (L_z,h_z|_U) 给具体的相对线对象，forget 到 X 仍能用0处稳定群区分。
这是本轮可检验的新对象输入，区别于上轮所有 Pic 类恒定的 graph/Koszul 候选。
但 (1) 的 Pic 类非平凡，不等于它已实现函数域的 degree-zero 可移动 Cartier 线或有原范数的物理源比较。
特别 |a∞| 是单个实分量，不是全 idele 模；(2) 不可由 product formula 改写为错误的全模等变权。

## 2. 最便宜的实际物理源映射及全主关系反测

在明确物理域 F_c=e^(u/2)S_exp,C 上取

\[
 \ell_0(r)=\int_R r(u)du,\qquad
 \mathcal L(r)=(L_{\ell_0(r)},h_{\ell_0(r)}|_U).             \tag{3}
\]

这是一个不使用 Ξ 零点、真正有值的映射；加法对应线的 tensor product。
537 可以选 ψ≥0、非零、支撑在固定17/16窗内，r_0=(D²−1/4)ψ。
其 μ±=0、Qζ(r_0)>0，且

\[
 \ell_0(r_0)=-\tfrac14\int\psi\ne0.                     \tag{4}
\]

所以指定非根确实可见，不是把任意 raw 非零值冒充商非根。

然而令 h=Eη_h 为405的实际正函数，H=e^(u/2)h>0，
p=(D²+D)h∈P_an，P=e^(u/2)p=(D²−1/4)H。
这是实际非 compact 全主关系，μ±(P)=0。带权端点费用由405的 S_exp 估计已付，故

\[
 \ell_0(P)=-\tfrac14\int H<0.                            \tag{5}
\]

(1) 的注入性使 L_{ell_0(r+P)} 与 L_{ell_0(r)} 不同。
故 (3) **不消全部405主关系**；这项断点先于局部消失/容量。
旧 boundary 稿已经给 raw periodization 的同一个负平均反测；这里新增的是它在本轮 genuine
full-stack 相对 Picard 对象上的准确后果，不能将这一直接消费再报新定理。
只在 C_c∞ 上检查主关系无效，因为旧553已付 P_an∩C_c∞=0。

把 z 换成 c+ ell_0 或 i ell_0 不修复 (5)。后者对实源给 unitary 字符，但全 principal 的实/复缩放仍使类改变。
只用 μ± 选择 z 会消 Pan，却把 (4) 的537 primitive非根映成0。
实际 DGA 的 η_P 同伦不能自动成为 (1) 中不同稳定群字符间的线同构；0处字符已经否定这种普通等变同构。
允许新 derived relative 层/变化目标，但应另外给真实范畴和 transport，不能把旧 null-homotopy 直接当该线族的 gauge。

## 3. Mellin 标签修补会在哪里回到旧商

更一般的有限 Mellin 标签取

\[
 \ell_z(r)=\int e^{zu}r(u)du.
\]

对实际 P，有405的完整恒等式

\[
 \ell_z(P)=M_p(\tfrac12+z)
   =\tfrac12(z²-\tfrac14)\xi(\tfrac12+z).                 \tag{6}
\]

因此单个 evaluation 标签若消所有 Pan，必要条件已经是 z=±1/2 或 ξ(1/2+z)=0。
反向也由 μ±消失和405的实际 E 像 Mellin vanishing 成立。
前者只保 degree；后者就是旧谱 evaluation，不是从覆盖独立恢复的自然坐标。
有限线性组合和更大目标可能有消去/协同，不由 (6) 一概否定；必须给具体系数及全平移关系检验。
若直接把所有零点/必要 jets 当标签，旧519/520已给忠实商，不应以非平凡 character 线重新申报它为新源桥。

更强的全域原范数责任来自553：physical Pan 的全平移 span 在全线 du 和 Dlog 中稠密。
故任何在其中全域连续、消全部 coset、值于固定 Hausdorff Pic/moduli 目标的类映射恒定。
不能把这个 Hausdorff 前件直接用于本轮新双位 absolute 参数商 C/iΛ。
对[双位实际分类](periodic-clutch-classification.md)的复线性标签 ℓ，正确次序是：
全 Pan 兼容先给 ℓ(Pan)⊂iΛ；Pan 对所有复标量闭合，而 iΛ 可数，故每个 ℓ(q)=0。
此后若 ℓ 本身在原全线 du/Dlog 连续，才由稠密性得到 ℓ=0。
这不需要把 C/iΛ 冒充 Hausdorff，也不先假定其 quotient 类映射有可分离连续目标。
full-stack (1) 的稳定群注入及双边界保frame版本则直接要求 ℓ(Pan)=0。
这些是该强旧结果在各指定目标上的准确条件消费，不是所有 Fréchet/变域/有费 cofinal 源桥不存在。

## 4. 原 du/Dlog 的源费与 cover/frame 费须分开

原 norm 固定为

\[
 \|r\|_{du}²=\int|r|²du,\quad
 \|r\|_{Dlog}²=(2\pi)^{-1}\int\log(2+|t|)|\widehat r(t)|²dt.
\]

对 supp r⊂[−L,L]，Cc∞ 稠密近似给精确 du dual norm

\[
 \|\ell_0\|_{du}=\sqrt{2L},\qquad
 |\ell_0(r)|\le\sqrt{2L/\log2}\,\|r\|_{Dlog}.            \tag{7}
\]

第二项只是合法 upper，不称 restricted Dlog 精确 dual norm。
一般 z=α+iβ 的 du squared fee 为

\[
 \int_{-L}^L e^{2αu}du=
 \begin{cases}2L,&α=0,\\ \sinh(2αL)/α,&α\ne0.\end{cases}  \tag{8}
\]

全线没有统一有限的同类 du/Dlog 泛函费用；Fréchet F_c 上仍连续。
若采用 (6) 的真实谱标签，准确 fixed/cofinal/critical/offcritical 与 joint 责任归553，不能删去其成长。

另一方面，在 cover 上另指定 |log|a∞||≤B 后，(2) 才有

\[
 \|h_z\|_\infty,\ \|h_z^{-1}\|_\infty
 \le e^{B|Re\,z|},\qquad
 |\partial_{u∞}^j h_z|\le |z|^j e^{B|Re\,z|}.           \tag{9}
\]

有限箭头集合 Q_0 及 C=max_{q∈Q_0}|log|q|∞| 仅给该有限集合的

\[
 |\chi_z(q)|,|\chi_z(q)^{-1}|\le e^{C|Re\,z|}.           \tag{10}
\]

将 (7) 代入 (9) 是一个选定 source/cover 双窗充分 upper；B、Q_0、source L 不同。
它不是全 adelic norm 或全箭头/cofinal容量，也不是其他实际 lift 的必要 lower。
若想对全 X 给 invariant 正纤维 metric，0处必须满足 |q|^(2Re z)=1，故 Re z=0。
纯虚 z 的标准纤维 metric确实 invariant，但 unitary isotropy 与 Weil 正极化/局部整性消失不同。
本分支不从 invariant metric 推正容量，也不将其缺失推广成所有有奇异 metric/相对范畴的不可行性。

## 5. 连续正反控制：同一个 line 标签会漏掉两段的真实 primitive 向量

沿既有真实连续正测度系统 Z_c(s)=1+c/[s(s−1)]，d=c−1/4=±1/16。
primitive 实现 R_d=C[w]/(w²+d)、w†=−w，a_r=∫r(u)e^(uw)du，完整型为

\[
 Q_c(r)=Tr(a_ra_r†)=2|A_r|²+2d|B_r|².                   \tag{11}
\]

取 φ≥0、非零、偶、光滑 compact、supp φ⊂(−1,1)，g=uφ，r=(D²−1/4)g。
r 是奇函数且 μ±(r)=0，因此 ell_0(r)=0；(3) 总给相对平凡线。
另一方面 A_g=0，B_g>0：d>0 时由 u sin(sqrt(d)u)/sqrt(d)>0，d<0 时由对应 sinh 式。
分部积分给 a_r=−(d+1/4)a_g，从而

\[
 Q_c(r)=2d(d+1/4)²B_g²
\]

在两段分别严格正/负。正段的非根与负段的危险方向都可被同一零标签漏掉。
这比只查一个537 even probe 更能揭示标量标签覆盖不足。
它仍是旧完整连续模型的具体源测试，不宣称该模型具有经典 A_Q 的算术实现。
若把 (1) 作为与 g 系统无关的外加 carrier，线/metric 设施本身无权区分这两个符号。
模型背景 Γ=0 是其指定完成化；没有从经典 ζ 删除 Γ 来制造该例。

## 6. 函数域控制与需要真正新增的输入

函数域正控制保持上一真实 C/F5:y²=x⁵−x+1，P=(0,1)、Q=(1,1)。
L_0=O(P+Q−2∞) 不是平凡线：canonical 评价矩阵 det1 给 H0(K−P−Q)=0，RR给
h0(K⊗L_0)=1，而 h0(K)=2。该有效化后的 cohomology 变化不可能由全局 frame 或字符标签计数替代。
这是旧实际曲线控制的再次消费，不报新证明。

Milne 的 Picard functor先模去从参数底拉回的线；degree-zero family、刚性化和下降数据共同确定相对对象。
其 §7.6 用真正 degree-zero twist 进入好有效图，再以 Picard 平移校正局部图；并非任意局部过渡单位就给这种移动。
[primary: Milne JVs §§1、7.6](https://www.jmilne.org/math/xnotes/JVs.pdf)。

本轮 (1) 已独立给非平凡相对等变线；下一未付责任不能再泛称“无任何 Pic 对象”。
但指定源 map (3) 在全 Pan 上失败；Mellin 谱修补只恢复旧 source quotient。
还需至少一个实际新源桥，同时给：全主关系上的线/relative同构、537及更强 primitive 覆盖、
同一整模型的 Cartier/valuative 消失过滤、可付的原 du/Dlog 与 arch metric lift，
以及 independent effective/RR/ample mixed 容量。

完整经典目标始终是

\[
\begin{aligned}
 Q_\zeta(r)={}&2Re(\mu_+r\,\overline{\mu_-r})
 +[\psi(1/4)-\log\pi]\|r\|²\\
 &+\tfrac12\int_0^\infty\frac{2e^{-v/2}}{1-e^{-2v}}
       \|\tau_vr-r\|²dv
 -2\sum_{p,k\ge1}(\log p)p^{-k/2}Re(r*r^*)(k\log p).
\end{aligned}                                                   \tag{12}
\]

405已付的全位抵消不能用单个稳定群字符或底层 unitary metric 替代。
还未证明 (12) 的 Γ/contact、每个 p^k 消失与双 pole 缺陷来自上述同一线族的预算。
(12) 已逐项回核568的(13)–(14)：差分前的1/2恰使 Fourier multiplier为
\(\int_0^\infty w(v)(1-\cos tv)dv=\Gamma(t)-\Gamma_0\)，
两方向 prime shifts 给−2，两个 pole rank-one项给2Re；未额外乘或除2。
据用户止损：停止 (3) 及仅谱坐标修补，不继续调 character/probe 数；保真正不同 relative family 与有费源桥为重准入条件。
本分支无 independent capacity、经典新 Weil 正性、whole/core 或宏观瓶颈变化。
