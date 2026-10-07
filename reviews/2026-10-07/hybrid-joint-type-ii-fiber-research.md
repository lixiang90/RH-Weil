# 联合 Type-II 纤维：共同除数、精确 affine 重排与全部 proper powers 的实际矩阵付款

2026-10-07。type_ii_joint 推导。状态：§1–5 的有限整数恒等式、共同 centering
与 support 限制为 [T]，§4.2的规范 coprime Möbius 估计另有全 Dirichlet
输入 [T/R]；§6 的实际 AF proper-prime-power compression 付款为
[T/R-MV]，只引用经典 Montgomery–Vaughan 均值不等式和已固定的原 AF frame；
§7 的 prime-only 四范数稳定传递有明确前件。没有证明 high-product signed
response 为 o((log X)^4)，没有改进简单临界线零点比例。
除§4.2明确调用既有 θ 输入外，不依赖新的零自由条带。

## 1. 固定实际对象并先落实共同 centering

固定 0<c_1<C_1，Y=X^(3/4)，L=log X，Q=XL，D 为本次实际选定的
整数维数，满足 D=XL+O(1)。每条式子只使用自己的 D；不将 floor 与 round
产生的不同有限核视为同一个核。记

\[
 \xi_k=1+k/Q,\qquad
 K(t)=D^{-1}\sum_{k=0}^{D-1}\cos(2\pi\xi_k t),
 \qquad t(a,b;c,d)=X\log(ad/bc).
 \tag{1}
\]

完整保留 carrier：2πξ_k t=τ_k log(ad/bc)，τ_k=2πX+2πk/L。
沿用238和239预先固定的共同整数 mask

\[
 m(a,b)=\mathbf1_{(a,b)=1}\,m_0(a,b),\qquad 0\le m_0\le1,
 \quad c_1Y\le a,b\le C_1Y.
 \tag{2}
\]

原 factor/aperture cuts 全在 m_0 中；在原 prime-power support 上它等于
distinct-base 的 physical mask。ghost extension 在 cutoff、channel、k
和估计之前已经固定。令

\[
 F_{a,b}(z)=\phi(z+\log(a/b))\phi(z)\phi(\log b-z)^2,\qquad
 W_{a,b;c,d}=\langle F_{a,b},F_{c,d}\rangle_H.
 \tag{3}
\]

H=L²(R/LZ,dz/L)，六窗口实际 overlap 不被常数1替换。

取239所选的共同正半轴 shells J_j=[A_j,B_j]，并使用 even symmetrization。
在配对 shell J_j∪(-J_j) 上，constant-density projection 给的核均值准确是

\[
 \kappa_j=
 \frac1{D(B_j-A_j)}
 \sum_{k=0}^{D-1}
 \frac{\sin(2\pi\xi_k B_j)-\sin(2\pi\xi_k A_j)}
 {2\pi\xi_k}.
 \tag{4}
\]

因此共同 centered multiplier 可以逐 atom 写成

\[
 K^{\rm cent}(t)=
 \sum_j\mathbf1_{\{|t|\in J_j\}}\{K(t)-\kappa_j\}.
 \tag{5}
\]

重叠 shell 端点须按原 partition 的同一约定只计一次。该表达只把
∫K d(σ-P_Jσ)=∫(K-κ_j)dσ 展开，不定义 channel 各自的非线性 reference。
它对 signed σ 线性，先合并 channels、再 centering 与原239完全相容。
原 physical density response 的 O(L) 付款仍取自239-F/236，不由(5)重新推断。

为简记，定义

\[
 {\cal W}^{\rm cent}_{a,b;c,d}
 =\frac{m(a,b)m(c,d)W_{a,b;c,d}}
 {(4\pi^2)^2\sqrt{abcd}}\,
 K^{\rm cent}\bigl(t(a,b;c,d)\bigr).
 \tag{6}
\]

所有变量在各自 fixed balanced cell 中。由于(2)的两对均约化，
ad=bc 当且仅当 (a,b)=(c,d)。故同 atom reference 的删除准确等价于
h=ad-bc≠0；没有删除任何非零 determinant ghost。

## 2. 先精确完成 v,w，再使用 determinant 条件

令 U=V=Y^(1/4)，这里只需 V<c_1Y。定义

\[
 B_V(n)=\sum_{\substack{v\mid n\\v>V}}\Lambda(v)
 =\log n-\sum_{\substack{v\mid n\\v\le V}}\Lambda(v).
 \tag{7}
\]

后一个等式来自 Σ_(v|n)Λ(v)=log n，且 B_V(n)=0 当 n≤V。
239的 completion column 恰为

\[
 T_{a,r}=\mathbf1_{r\mid a}B_V(a/r),\qquad
 \sum_{r\mid a}\mu(r)B_V(a/r)=\Lambda(a),\quad a>V.
 \tag{8}
\]

证明：(μ*1)*Λ_(>V)=Λ_(>V)，而 high cell 上 Λ_(≤V)(a)=0。
式(7)已经在每个 actual numerator a 中合并所有 v,w；既没有丢弃
Λ(v)>0 的 completions，也没有对它们分别取绝对值。

所以239的完整 centered physical quotient 准确成为

\[
 {\cal Q}^{\rm cent}
 =\sum_{\substack{a,b,c,d\\ad-bc\ne0}}
 \Lambda(b)\Lambda(d)\,
 {\cal W}^{\rm cent}_{a,b;c,d}
 \sum_{\substack{r\mid a\\s\mid c}}
 \mu(r)\mu(s)B_V(a/r)B_V(c/s).
 \tag{9}
\]

I–I、I–II、II–II 分别只在 r≤U 或 r>U、s≤U 或 s>U 处加 cutoff
indicators。先合并这四个区域使其 indicator 总和为1，才得到(9)。
这一求和顺序保留241规定的每个 actual determinant/frequency fiber 内的
全部 divisor signs。式(9)本身还不是新的 saving。

## 3. 非零 determinant 对共同 Möbius 除数的额外限制

固定 h=ad-bc≠0。在 μ(r)μ(s)≠0 的项中唯一写成

\[
 r=gu,\quad s=gv,\quad g=(r,s),\quad (u,v)=1.
 \tag{10}
\]

r,s 均 squarefree，故 g,u,v 均 squarefree 且两两 coprime，并且

\[
 \boxed{g\mid h,\qquad \mu(r)\mu(s)=\mu(u)\mu(v).}
 \tag{11}
\]

证明：g 同时整除 a,c，故整除 ad-bc。两两 coprime 来自 r,s
squarefree；μ(g)²=1，给出符号等式。注意共同部分 g 的符号平方消失，
并非可继续使用一次 μ(g) 相消。

因此一个非零 determinant core |h|≤H 不含任何 g>H 的共同 divisor
stratum。241的 common-multiple overlap 在 arbitrary response row 上存在，
但不能不加 h 条件地照搬到非零 physical fiber。此处只是实际 support
restriction；不能由 g≤H 推出其余 u,v labels 独立、正交或小量。

令 q=(b,d)。由 mask 有 (gu,b)=(gv,d)=1，故 (g,q)=1，而 q|h。
准确地，

\[
 \boxed{gq\mid h.}
 \tag{12}
\]

对 small nonzero core |h|<c_1Y，denominator 仍保留 Λ(b)Λ(d)，因此

\[
 \boxed{q=1.}
 \tag{13}
\]

若 b,d 不同 prime bases，q=1；若同一 base，它们是同一素数的幂，q 是
min(b,d)≥c_1Y，与 q|h 矛盾。这个推论在合并之前也适用于 numerator ghosts，
因为 denominator 从未作 Vaughan split。

完整 quotient 合并后 numerator 的 Λ(a)Λ(c) 同理说明，small nonzero
core 中 a,c 的 bases 也不同。不排除 a,d 或 b,c 的共同 base；不能把它
误写为“四个 bases 两两不同”。

## 4. gcd / coprime divisor 的精确 affine 纤维

写 b=qb_0、d=qd_0、(b_0,d_0)=1，并取

\[
 a=gu A,\quad c=gv C,\qquad
 m_h=h/(gq).
 \tag{14}
\]

determinant 方程变成

\[
 u d_0 A-v b_0 C=m_h.
 \tag{15}
\]

自然 mask 必须同时保留 (gu A,qb_0)=(gv C,qd_0)=1；其必要前件给
(u,b_0)=(v,d_0)=1。由这些前件以及 (u,v)=(b_0,d_0)=1，逐素数可核得

\[
 (u d_0,v b_0)=1.
 \tag{16}
\]

取唯一的 0≤A_0<vb_0 满足

\[
 u d_0 A_0\equiv m_h\pmod {vb_0},\qquad
 C_0=(u d_0 A_0-m_h)/(vb_0).
 \tag{17}
\]

若 modulus vb_0=1，按 A_0=0 定义。所有整数解且仅有这些解：

\[
 \boxed{
 A=A_0+vb_0\ell,\qquad C=C_0+ud_0\ell,\qquad \ell\in\mathbb Z.}
 \tag{18}
\]

尤其其实际 kernel argument 准确保持为
\[
 t=X\log\frac{uA_\ell d_0}{vb_0C_\ell}
   =X\log\left(1+\frac{h/(gq)}{vb_0C_\ell}\right).
 \tag{18a}
\]
它不是 K(h/g) 或 K(h/(gq))。F 中的 log a、log b 以及全部 original
normalizations 按(14)代入实际值，没有认为缩放后的 W 等于缩放前的 W。

令 ℐ(h,g,q,u,v,b_0,d_0) 为(18)同时满足原 a,c factor cuts、aperture
cuts、两侧完整 natural gcd mask 与 A,C>V 的整数集合。该集合不可改为一个
独立于 labels 的连续平均。在任一 fixed rectangle 中其 enclosing real
interval 长度满足

\[
 |\mathcal I|_{\rm real}\ll \frac q{guv},
 \qquad \#\mathcal I\ll 1+\frac q{guv}.
 \tag{19}
\]

例如 A-range 长度 O(Y/(gu))，而其 progression step vb_0≈vY/q；
C-range 相同。small core 的 q=1 因而每条这样的 ℓ fiber 都只有 O(1) 点。
常数依赖 fixed balanced aspect ratio。不能把短于1的 real interval 长度
直接当作整数点数，也不能由大 guv 单独获得衰减。

把(10)–(18)代入(9)，得到完整、唯一计数的精确表达：

\[
 \begin{split}
 {\cal Q}^{\rm cent}
 =\sum_{h\ne0}\!
 \sum_{\substack{g,q\ge1\\gq\mid h,\ (g,q)=1\\g\ {\rm squarefree}}}
 \sum_{\substack{u,v\ {\rm squarefree}\\
 (u,v)=(g,u)=(g,v)=1}}
 &\mu(u)\mu(v)\\
 {}\times\!
 \sum_{\substack{b_0,d_0\ge1\\(b_0,d_0)=1\\
 (gu,qb_0)=(gv,qd_0)=1}}
 &\Lambda(qb_0)\Lambda(qd_0)
 \sum_{\ell\in\mathcal I}
 B_V(A_\ell)B_V(C_\ell)\,
 {\cal W}^{\rm cent}_{guA_\ell,qb_0;gvC_\ell,qd_0}.
 \end{split}
 \tag{20}
\]

所有 outer ranges 由实际 fixed cell 和 B_V support 截断，故有限。
h 的正负、全部非 core tails、原 carrier、所选 D 和 common-shell
subtractions 均未删除。式(20)可直接按实际 h/shell 分组；对每个组，
所有 g,u,v 之和先保持符号。没有建立各 stratum 的独立 absolute budget。

新限制是 gq|h 和 denominator-weighted small core 的 q=1，加上
canonical completion (7)；它们使未来的 reciprocity / Kloosterman 或联合
Möbius dispersion 必须估计一个具体的 coprime divisor residue average。
单独的 Mertens bound、row-independent Dirichlet PNT 或 label-distance
Schur decay 都没有支付该 average。

### 4.1. 只能在完整 physical quotient 后进行的 core 投影

在 0<|h|<c_1Y 上，完整 Λ(a)Λ(c) support 还满足 (a,c)=1：
若两者同一 prime base，则 (a,c)=min(a,c)≥c_1Y；但 (a,c)|h。
因此将整个 physical core summand 乘以

\[
 \mathbf1_{(a,c)=1}
 \tag{20a}
\]

准确不改变结果，包括共同 density subtraction。该投影对原 I/II 各个
entry 一般会改变它们；可用性仅来自先合并全部 divisor blocks 得到完整
Λ(a)Λ(c)。不能用(20a)证明原独立 Type-II entry 本身小。

在这个合法投影后的 expansion 中，r|a、s|c 强制 (r,s)=1，即 g=1。
故共同 g>1 可在 whole physical core 上精确消去，代价是(20a)对 completion
variables 的交叉约束。写 a=rA、c=sC，它等价于

\[
 (r,s)=(r,C)=(s,A)=(A,C)=1.
 \tag{20b}
\]

这一步是合并后真实 support 的约化，不能只保留 (r,s)=1 而丢掉后三个条件。
尾部 r>U、s>U 也仍按同一个 physical fiber 联合处理。

特别地，在真正 prime a>V 时，canonical I(a)=Λ(a)、II(a)=0。
large-divisor II 的 nonzero prime-free ghost atoms 与 I 的 ghost atoms
在 physical sum 中抵消；把(20a)或 prime support 当作允许独立丢 ghost 的
理由，会使规范系数准入失效。这里没有得到原 II–II/mixed 的 intrinsic 小量。

### 4.2. coprime joint Möbius 的一个真正规范估计及其准入限度

假定446所涉全 Dirichlet 角色 family 在 Re s>θ 无零及相同 uniform
reciprocal-control，θ>1/2。固定 a=θ+δ<1，δ先于长度、角色和高度。
对两个预先固定的 Dirichlet zero extensions χ、ψ，准确有

\[
 \sum_{(r,s)=1}\frac{\mu(r)\mu(s)\chi(r)\psi(s)}{r^z s^w}
 =
 \frac{{\cal H}_{\chi,\psi}(z,w)}{L(z,\chi)L(w,\psi)},
 \tag{20c}
\]
\[
 {\cal H}_{\chi,\psi}(z,w)=
 \prod_p
 \left\{
 1-\frac{\chi(p)\psi(p)p^{-z-w}}
 {(1-\chi(p)p^{-z})(1-\psi(p)p^{-w})}
 \right\}.
 \tag{20d}
\]

Re z,Re w>1 上逐 prime 的 coprime alternative 为
1-χ(p)p^(-z)-ψ(p)p^(-w)，直接验证(20c)。当两实部≥a>1/2，
(20d)的 departures from1 被 C_a p^(-2a) 一致支配，故绝对收敛、
holomorphic 且 |H|≤C_a，uniform in heights/characters。更一般的绝对收敛
区域为 Re z>0、Re w>0、Re z+Re w>1；不扩大到两实部只大于0的区域。
H 的零点不会产生任何 pole；没有使用它的 reciprocal。principal 1/L
在 s=1 是零，此处也没有 principal residue。

对 fixed W∈C_c^∞((1/2,2)^2)，二维 Mellin inversion 及相同 reciprocal
输入，分别移两线到 a，得到

\[
 \left|
 \sum_{(r,s)=1}\mu(r)\mu(s)\chi(r)\psi(s)
 W(r/R,s/S)(r/R)^{it_1}(s/S)^{it_2}
 \right|
 \ll_{W,\delta,\epsilon}
 (RS)^a
 \{q_{\chi,\mathrm{eff}}q_{\psi,\mathrm{eff}}
 (3+|t_1|)^2(3+|t_2|)^2\}^{\epsilon}.
 \tag{20e}
\]

一条线移动时另一条仍在2，(20d)仍绝对收敛；双线到 a 后 fixed-profile
Mellin rapid decay 支付全部 vertical/horizontal tails。deleted Euler
radicals 计在 q_eff 中。cutoff、fixed profile seminorms、gap 和 Mellin
orders 先于 moving q,t 固定；不是任意 row-dependent bounded coefficients。
固定的除数 coprimality 如 (r,C)=1 可用对应 natural zero extension 准入，
但另需明确其 q_eff 和 full weight 变化。

这给真正 coprime μ⊗μ 的规范幂节省，不能直接付(20)或(20a)：
actual residue fiber 使用 moving congruence (17)、B_V(A_ell)B_V(C_ell)、
sharp integer incidence 和原 mask，尚未得到与 R,S 无关的 fixed W
或相应 weighted Mellin seminorm 预算。nonseparable smooth W 获准，并不意味着
这个随 reciprocal residue 变化的稀疏 weight 获准。对 r>U、s>U 尾部，
§4.2只完成可估计的规范 coupled factor，而没有证明实际 tail 的净 saving。
这精确定位下一输入为(20b)和 residue-dependent profile 的共同付款，
不是换一个 kernel 名字或把任意系数 large sieve 加入公理。

## 5. 有限整数审计与准确作用范围

2026-10-07 在全部 a,b,c,d∈{12,…,22}、两侧 primitive gcd mask、
V=3 上穷举。4290 个非零 determinant quadruples、37000 个 nonzero
Möbius divisor terms 全部满足(11)(12)(16)(18)。78 个
0<|h|<12 且 Λ(b)Λ(d)≠0 的 denominator core rows 全部 q=1。
初次浮点 orientation 的式(8)最大残差为 1.1102230246251565e-16；
交付审计另以 log(p) 为形式 basis、integer coefficients 精确验证整个
convolution，以及(9)在每个 primitive quadruple 中的 numerator tensor
coefficient 重构。divisibility、gcd、Möbius signs、affine reconstruction
和全部形式系数均只用整数断言。可复现入口为仓库根目录运行

~~~powershell
python scripts/hybrid_joint_type_ii_fiber_audit.py
~~~

脚本只输出 JSON，不写文件，绑定本报告最终 canonical LF hash。

这是有限 identity 的防错证据，不是 asymptotic cancellation 证书。
本报告的完整数学证明不以这个小范围穷举代替量词。

## 6. 全部 proper prime powers 在原有限 AF compression 中的统一付款

这节处理原完整矩阵，而非(20)某个独立 raw cell。定义 sharp
proper-prime-power polynomial

\[
 R_X(t)=\sum_{\substack{p^j\le X\\j\ge2}}
 \frac{\log p}{p^{j/2}}e^{it\log(p^j)}.
 \tag{21}
\]

两个无条件 elementary 估计为

\[
 \|R_X\|_\infty\ll L,\qquad
 \sum_{\substack{p^j\le X\\j\ge2}}\frac{(\log p)^2}{p^j}\ll1.
 \tag{22}
\]

第一式 j=2 用 Chebyshev 加 Abel 给 Σ_(p≤sqrt X)log p/p≪log X；
j≥3 的和绝对收敛。第二式连同所有 j≥2 的无限和也绝对收敛。

对原 enlarged height interval J=[T/2,3T]，X≈T，经典
[Montgomery–Vaughan Corollary 3](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)
的 Dirichlet-polynomial mean-square inequality 给

\[
 \int_J|R_X(t)|^2dt\ll X.
 \tag{23}
\]

每个起点平移只给 coefficients 单位相位。使用 length≤X 的有限 polynomial
和(22)，其 remainder 至多 O(X)；无需任何素数对输入或新的零自由区。

保留446的原 U_F、f_k(t)=hat φ(t-α_k)、a_L=||φ||²/L 以及 finite d≈XL≈N。
令 F=U_F/sqrt(2πL)，则 F*F≤1，finite critical Parseval 给
Σ_(0≤k<d)|f_k(t)|²≤a_L L²。原 proper-power channel 准确是

\[
 E_{\rm pp}=\frac{2\pi}{a_LL}F^*M_{\rm pp}F,\qquad
 M_{\rm pp}(t)=-\pi^{-1}\Re R_X(t).
 \tag{24}
\]

因此(22)直接给 ||E_pp||_op≪1。对 Hermitian scalar multiplier M，
F contraction 给

\[
 \operatorname{Tr}(F^*MF)^2\le\operatorname{Tr}(F^*M^2F).
 \tag{25}
\]

可由 F F*≤1 和 Hilbert–Schmidt norm 直接证明；不调用 x^4
operator convexity，也不把实际 frame 改成平均投影。

J 内由(23)和 finite Parseval，

\[
 L^{-2}\operatorname{Tr}(F^*\mathbf1_JM_{\rm pp}^2F)
 \ll L^{-3}(a_LL^2)\int_J|R_X|^2
 \ll X/L.
 \tag{26}
\]

J 外保留真实全高度上界 |R_X|≪L，按原 C² Fourier tail
Σ_k∫_(Jc)|f_k|²≪dX^(-3)≪L/X²，给

\[
 L^{-2}\operatorname{Tr}(F^*\mathbf1_{J^c}M_{\rm pp}^2F)
 \ll X^{-2}.
 \tag{27}
\]

这包括低绝对高度，不静默删除它。合并(24)–(27)，得到

\[
 \boxed{
 \|E_{\rm pp}\|_{\rm op}\ll1,\qquad
 \|E_{\rm pp}\|_2^2\ll N/L^2,\qquad
 \operatorname{Tr}E_{\rm pp}^4\ll N/L^2=o(N).}
 \tag{28}
\]

最后用 Hermitian eigenvalues 的 λ^4≤||E_pp||_op²λ²；
从而 ||E_pp||_4≪N^(1/4)L^(-1/2)。

历史221-C等已在某些 critical boxes 用 incidence 删除 proper powers；
(28)的范围是原完整 AF finite compression 中同时付款所有 p^j≤X、j≥2。
其证明机制是经典 mean-square 加 compression，不宣称公开文献的新纪录。
它没有在高-product 单一 raw cell 上证明同样的 o(L^4)。

## 7. prime-only 完整四迹问题的合法稳定约化及尚缺输入

令 H_full 为原完整 centered Hermitian AF response，背景及其它原修正均保留，
并定义 H_pr=H_full-E_pp（prime multiplier 只留真正 primes）。
Schatten triangle 及(28)说明

\[
 \|H_{\rm full}\|_4=O(N^{1/4})
 \quad\Longleftrightarrow\quad
 \|H_{\rm pr}\|_4=O(N^{1/4}).
 \tag{29}
\]

在任一侧确有这个 finite-constant 前件时，非交换 telescoping 加
Schatten Hölder 准确给

\[
 |\operatorname{Tr}H_{\rm full}^4-
   \operatorname{Tr}H_{\rm pr}^4|
 \ll N L^{-1/2}=o(N).
 \tag{30}
\]

这联合保留背景和所有一、二、三次 E_pp mixed words，不逐 word
假设 independence。原446的 growing-power 四迹弱界没有证明(29)的
finite-constant 前件；因此不得直接凭(28)宣布完整四迹已付或比例提高。

真正的余额是(20)在完整 physical direction 上的 reciprocal-residue/
Möbius joint signed average，以及跨 cells、alias 与其它 signed words 的共同账本。
small core 的 modulus vb_0 可比其 A-length 大很多，ℓ 只有 O(1) 点；
全导子单一 canonical AP PNT 不能把另一个 B_V(C_ell) 和物理权重当成
固定 character coefficients 后获得一次独立节省。无零 package [R] 仍可用于
经证明准入的规范因子，却没有在本报告中支付这个新的 joint average。

本轮实质新增的准确范围：完整 determinant fiber 的 gq|h support 约束和
coprime affine 重排；全部 proper powers 的原矩阵四范数小量。开放接口仍是
实际 signed high-prime response。没有将接口失败表述为任何方法的不可能性。
