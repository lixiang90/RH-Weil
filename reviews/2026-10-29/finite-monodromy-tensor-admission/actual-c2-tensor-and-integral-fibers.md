# 固定C₂算术张量：实际整纤维、Artin因子与零点运输准入

2026-10-29；独占原件准入稿，尚未不同fresh／root消费。恢复README／STATE、check→show、同Goal／C053／D20261029A／formal18及宏观前沿；C053耗尽，原 `0/history54/latest590/formal18` 不动。本稿按本次明确授权自含核固定对象，0预算、非C054；无新primary／web／候选／数值／Git，不改STATE、cadence或看板。

**净判断：此普通算术张量给出了真实全n局部因子和可算的全局pole order，但其generic L函数仅为同一ζ与L(χ₋₇)的重数乘积。它没有将经典ζ的全局零点谱送到其n次幂。** 原整模型与正规化在7处的scheme-zeta还确实不同，不能以generic Artin张量因子替代坏纤维。

## 1. 固定代数、整模型与正规化

记 `ω=(1+√−7)/2`，`O=Z[ω]`，其最小多项式 `f(T)=T²−T+2`、判别式−7，Galois群 `G=C₂={1,c}`。令n≥1、`m=2^(n−1)`，
\[
 A_n=K^{\otimes_{\mathbb Q}n},\quad
 R_n=O^{\otimes_{\mathbb Z}n},\quad X_n=\operatorname{Spec}R_n.
\]
`K⊗K≅K×K`由在K中把f分为不同根得到，映射为 `x⊗y↦(xy,x c(y))`。迭代给
\[
 A_n\simeq K^m,\qquad
 x_1\otimes\cdots\otimes x_n\longmapsto
 (x_1\sigma_2(x_2)\cdots\sigma_n(x_n))_{\sigma_i\in G}.
\]
R_n是自由Z模，rank `2^n`，故嵌入其generic代数而为reduced order。A_n中对Z整的元素恰为 `O^m`；这也就是对R_n整的元素。因此正规化为
\[
 \widetilde X_n=\coprod_{1}^{m}\operatorname{Spec}O.
\]
根差 `√−7` 在7外可逆，Chinese remainder分解已在Z[1/7]上成立；R_n与正规化之差只支撑7。作为补充的费用／导子区别，trace Gram张量公式给
\[
 |\operatorname{disc}R_n|=7^{n2^{n-1}},\quad
 |\operatorname{disc}\widetilde R_n|=7^m,\quad
 [\widetilde R_n:R_n]=7^{(n-1)m/2}.
\]
最后指数在n=1为0、n≥2为整数。非极大order的判别式不能自动当作下文generic Artin conductor。

## 2. 所有有限素数的实际scheme局部因子

scheme-zeta按闭点定义，等价于 `Z_p(T)=exp(Σ_{r≥1}#X(F_{p^r})T^r/r)`；nilpotents不改变闭点数。令χ为primitive quadratic character χ₋₇，χ(7)=0。

| 素数 | X_n实际纤维 | 局部scheme-zeta，T=p⁻ˢ |
|---|---|---|
| p≠7，χ(p)=1 | `F_p^{2^n}` | `(1−T)^−2^n` |
| p≠7，χ(p)=−1 | `F_{p²}^{m}` | `(1−T²)^−m` |
| p=7 | `F₇[ε₁,…,ε_n]/(ε₁²,…,ε_n²)`，一个闭点 | `(1−T)^−1` |

good-prime两行亦可由 `#X_n(F_{p^r})=(1+χ(p)^r)^n` 直接得到：split恒为2ⁿ，inert在r奇时0、r偶时2ⁿ；此处包含good prime2。7处 `f(T)=(T−4)² mod7`，每一ε_i映到域都必须为0，故任意r都只有一个F_{7^r}点。

正规化在7处不是reduced：其纤维是m份 `F₇[ε]/ε²`，因此有m个闭点、局部因子 `(1−7⁻ˢ)^−m`。7外与X_n相同。于是先在Re s>1的绝对收敛域，继而由右边给亚纯延拓，准确有
\[
 \zeta_{\widetilde X_n}(s)=\zeta_K(s)^m,
 \qquad
 \boxed{\zeta_{X_n}(s)=\zeta_K(s)^m(1-7^{-s})^{m-1}.}
\]
这不是可无声省略的nilpotent修正：差异来自正规化分开了闭点分支，而非nilpotent长度直接作为Euler指数。

## 3. generic Artin张量与坏素模型不可混同

嵌入置换表示 `V=H⁰(Spec K_Qbar,Q_l)=1⊕χ`，张量按同一个G的diagonal作用。任一非平凡c的trace为0，恒等元trace为2，因此
\[
 V^{\otimes n}=m\,1\oplus m\,\chi.
\]
good prime的Frobenius特征值积给
\[
 L_p(V^{\otimes n},s)
 =(1-p^{-s})^{-m}(1-\chi(p)p^{-s})^{-m},
\]
恰为§2两种good因子。7处惯性映满G，`(V⊗n)^I`是m维平凡部分，Frobenius在其上为1，所以Artin因子为 `(1−7⁻ˢ)^−m`。χ的ramified局部因子为1，不能把χ(7)=0当作完整表示仍有2m个未分歧特征值。

由各prime因子逐项乘起，
\[
 \boxed{L(V^{\otimes n},s)=\zeta(s)^mL(s,\chi)^m=\zeta_K(s)^m.}
\]
它对应正规化generic Artin对象，不等于n>1时raw X_n的闭点zeta。若“cohomological因子”指实际特殊纤维的trace，则7处H⁰只有一条常数线，仍应恢复raw因子；若指generic Artin表示的惯性不变空间，则有m条。virtual Artin表达又容许负重数。三种角色不能凭“上同调／张量”名称同一化。

## 4. arch Γ、conductor与pole order

固定 `Γ_R(s)=π^(−s/2)Γ(s/2)`、`Γ_C(s)=2(2π)^−sΓ(s)`；duplication公式给
`Γ_R(s)Γ_R(s+1)=Γ_C(s)`。χ是odd，conductor7，故取Artin规范
\[
 \Lambda_K(s)=7^{s/2}\Gamma_C(s)\zeta(s)L(s,\chi),
 \qquad
 \Lambda_n(s)=7^{ms/2}\Gamma_R(s)^m\Gamma_R(s+1)^m
                 \zeta(s)^mL(s,\chi)^m=\Lambda_K(s)^m.
\]
generic conductor为 `7^m`；不是R_n的判别式 `7^{nm}`。通常Dirichlet completion写 `(7/π)^((s+1)/2)Γ((s+1)/2)L(s,χ)`，比此χ的Artin规范仅多常数√7，不改变任何pole／zero order。

解析只用项目既有ζ和primitive Dirichlet L的延拓／Poisson功能方程。χ在1,…,6取值 `1,1,−1,1,−1,−1`，非零性在本例也可直接核：
\[
 L(1,\chi)=\int_0^1
 \frac{1+x-x^2+x^3-x^4-x^5}{1-x^7}\,dx>0,
\]
因为分子是 `(1−x)(1+2x+x²+2x³+x⁴)`。故ζ_K在s=1恰simple pole。其completed功能方程对称s↔1−s，Λ_K在0、1均simple pole（odd χ的Gauss root number为1）；因而Λ_n在0、1恰有m阶pole。无n无关的pole-order界出现，且m随n指数增长。

raw scheme-zeta在1处仍为m阶pole，因为修正因子在1非零。若用相同generic arch/conductor补齐raw函数，得到
\[
 \Lambda_n^{raw}(s)=\Lambda_K(s)^m(1-7^{-s})^{m-1}.
\]
在0处修正有m−1阶零，故此completion在0仅simple pole，在1为m阶。这里仅固定generic arch／Artin conductor作比较，**没有声称非normal order存在该canonical selfdual completion**。换成order判别式只再乘非零指数因子 `7^((n−1)ms/2)`，不改变pole阶；n>1的0阶1／1阶m不对称不能由此修复，也不能搬用正规化的常数根数对称功能方程。n=1无此差异。不判其它带dual-order／额外局部数据的公式不存在。

## 5. 完整fixed-C₂表示环、tensor与Adams

任意特征0有限维C₂表示都写成 `W=(a,b)=a·1⊕b·χ`，a,b≥0。令 `d=a+b,e=a−b`，则
\[
 (a,b)\otimes(c,d')=(ac+bd',ad'+bc),\qquad
 W^{\otimes n}=\left(\frac{d^n+e^n}{2},\frac{d^n-e^n}{2}\right).
\]
n=0另为(1,0)，不使用0⁰约定。对不等输入W_i，unit／χ数分别为
`[∏(a_i+b_i) ± ∏(a_i−b_i)]/2`。由c的±1 eigenspaces分解或字符相乘即证，重数为非负整数。

对任何(a,b)，实际Artin数据为
\[
 L(W,s)=\zeta(s)^aL(s,\chi)^b,\quad
 N(W)=7^b,\quad
 \Lambda(W,s)=7^{bs/2}\Gamma_R(s)^a\Gamma_R(s+1)^bL(W,s).
\]
good局部为 `(1−T)^−a(1−χ(p)T)^−b`，7处为 `(1−T)^−a`；s=1及completed s=0的pole order均为a（a=0无pole）。这些公式也可在表示环延为a,b∈Z的virtual比值，但负重数不是实际有效对象或正容量。

Adams以 `char ψ^kW(g)=char W(g^k)` 定义，因此
\[
 \psi^k(a+b\chi)=
 \begin{cases}a+b\chi,&k\text{ odd},\\(a+b)1,&k\text{ even}.\end{cases}
\]
它保持rank，并非rank为d^k的tensor power。even Adams须重新计算ramification：χ²=1已变unramified，7因子为 `(1−7⁻ˢ)^−(a+b)`；不能先取原W的惯性不变部分，再只把其Frobenius升幂。即使在good primes，升局部特征值与把全局变量s换ks也不同。

任意rank-growing或逐步adaptive选择，只要仍在**同一个fixed-C₂范畴**内，每个有限阶段仍只有这两种irreducibles和这两个L因子。子表示、直和、tensor或virtual操作可以改重数／取消因子，不能据此新生全局零点位置。无限阶段另须付归一化、收敛和目标身份；此计算不预判所有此类极限。

## 6. 这没有支付“全局ζ零点谱幂”

在0<Re z<1，generic completion的Γ与conductor无零极点，所以精确有
\[
 \operatorname{ord}_z L(W,s)
 =a\operatorname{ord}_z\zeta(s)
   +b\operatorname{ord}_z L(s,\chi).
\]
对V⊗n两重数均为m：原零点只被重复，可能与另一基L函数同点相加。没有 `ρ↦ρ^n` 或其它全局谱参数运输；raw X_n的额外因子也只是7的固定局部修正，不是ζ零点tensor谱。Adams的parity公式同样直接显示其局部升幂不产生所需全局运输。

因而“已有实际整数tensor模型＋alln pole order”在这个例子成立，却仍不是Deligne所需的非平凡全局零点谱tensor／放大定理。此对象是finite-monodromy weight0的H⁰；它没有给同非零arithmetic primitive的physical源、Pan／537下降、整截面mixed RR或完整经典Γ／properpowers／双pole的两源identity，也无原du/Dlog成长净预算。局部±1的Satake乘积不能补这些箭头。

本稿只停止把**这个普通fixed-C₂算术tensor／Adams计算**当作已经支付该全局桥的消费，不否定通用Deligne路线、其它monodromy／高阶上同调或独立global pole theorem。它不通过Goal任一完成门，不改善whole4/5 UPPER，不预591或计数学轮。原件提交fresh/root后才决定准入分类；没有参数优化／新候选／来源后继授权。
