# 固定 Tate 双源规则的解析源、原范数与首门核查

2026-10-28；unit_height 独占咨询稿。已恢复 AGENTS、README、STATE、G20261027、D20261028S、前沿顶部及当前已耗尽的 C049，实际运行 check→show 通过；formal17 后 cadence0／历史50／latest586 保持。按 root 本轮冻结的 [actual-source-rule](actual-source-rule.md) 核查，不再选择 evaluation、period 或新源族。不 web／PDF／数值，不改管理文件，不展开 Poincaré metric 或高度。

**结论：固定源确实有合法强域和真实整数 Cartier 线，但全 Pan principal 门已经失败；只依赖同一点数据的完整 Weil 读出也有旧正窗 kernel 障碍。两项均由最强旧直接决定，按前置强旧0止，不准继任数学合同。** 这不是全部 Tate／Poincaré／额外 relative 数据的方法类边界。

## 1. 同一实际对象与两种不同的连续性

使用旧 [371](../../../notes/371-f1-tate-curve-frobenius-weight.md) 的
\[
 E=\mathbb C/\Lambda,\qquad
 \Lambda=(\log2)\mathbb Z+2\pi i\mathbb Z,\qquad O=[0].
\]
源为全部复物理函数 \(r=e^{u/2}f\in\mathcal S_{\exp,\mathbb C}\)，固定
\[
 \ell(r)=\int_{\mathbb R}e^u r(u)\,du,\qquad
 P_r=[\ell(r)],\qquad J_r=\mathcal O_E([P_r]-[O]).
 \tag{1}
\]
每个除子的系数确为整数 \(+1,-1\)，degree 为0；复源只决定点的位置，不冒充复权 Cartier 系数。曲线是实际紧复椭圆曲线，但没有在本门新增一个整算术模型。

记 \(p_{N,0}(r)=\sup_u e^{N|u|}|r(u)|\)。绝对积分直接给
\[
 |\ell(r)|\le p_{2,0}(r)
 \left(\int_0^\infty e^{-u}\,du+\int_{-\infty}^0e^{3u}\,du\right)
 =\frac43p_{2,0}(r).
 \tag{2}
\]
因此 (1) 对原强源拓扑连续。每先固定 \(A>0\)、支撑在 \([-A,A]\)，原 du 上的精确 dual norm 是
\[
 \|\ell\|_{L^2([-A,A])^*}^2
 =\int_{-A}^{A}e^{2u}\,du=\sinh(2A).
 \tag{3}
\]
在严格 compact smooth 子域上的 supremum 相同，由其在该 L² 空间稠密得到；不要求 extremizer 本身严格 compact。以全线零延拓的原 Dlog 范数，已有 \(\|r\|_{D\log}^2\ge\log2\,\|r\|_{du}^2\)，故
\[
 |\ell(r)|\le\sqrt{\sinh(2A)/\log2}\,\|r\|_{D\log}.
 \tag{4}
\]
(4) 只是 upper，不是 Dlog 的精确 dual norm。\(A\) 是物理支撑，不能改叫算术 height，亦不支付线族 metric／截面的任何范数。

对固定 compact smooth \(v\) 满足 \(\ell(v)\ne0\)，物理平移 \(T_bv(u)=v(u-b)\) 保持每个固定全局有限 Sobolev 范数、du 及平移不变的 Dlog／Hlog 范数，却有
\[
 \ell(T_bv)=e^b\ell(v).
 \tag{5}
\]
所以不存在这些原全局范数到 \(\ell\) 的统一 bound。商到 compact \(E\) 也不会自动恢复该连续性：固定 \(t=\frac12\log2\)，令
\[
 r_b=\frac{t}{\ell(v)}e^{-b}T_bv .
\]
则 \(r_b\to0\) 于每个固定有限 Sobolev 范数，而 \(P_{r_b}=[t]\ne O=P_0\)。这是同一源规则的范数检验，不是增加新候选。

## 2. 553 的最强旧责任及其不适用前件

[553 §2、§4](../../../notes/553-principal-cyclic-closure-and-cofinal-readout-fees.md) 已付：405 的一条实际非 compact physical Pan 的平移线性包，在全线 du、Hlog 和每个固定有限 Sobolev 完成中稠密。这里的 H¹ 等版本是原件明确论证的结果，不从 L² 密度无声升级。

因此，若一个全域线性 energy 读出有上述某个固定 global bound，消去全部真实 Pan，并进入已定义的 Hausdorff closed-base quotient，则它在该 quotient 全零。对全域连续标量 mixed 型，同样先固定另一腿，关系根条件使该腿全零。非线性类映射须有实际全 Pan coset 不变性，才可由这种密度推出常值；仅 raw 值非线性、仅强源连续或 varying domain，不在该命题中。

当前 \(\ell\) 因 (5) 不满足 global finite-Sobolev 前件，故不能用“553 密度”直接宣布它为零。若另用某个复线性标签降到离散周期格，要求所有 Pan 点等于 \(O\)，则复标量闭合首先迫使标签在 Pan 上**精确为零**：一条非零复直线不能包含于 \(\Lambda\)。只有标签再有 global 有限 Sobolev 连续性时，才继续由553迫全标签为零。这是 [574 §5](../../../notes/574-actual-adelic-cover-relative-picard-and-source-transport.md) 已有的“先标签、后密度”责任。

最初咨询中的“非实 Mellin evaluation”不是本次冻结公式：当前 \(z=1\)，通常 Mellin 变量 \(s=\frac12+z=\frac32\) 仍是实数，且不在临界线上。解析 evaluation 的强连续性与 Pan 消去是两项责任；旧405／553在实际零点及必要 jets 的 evaluation 坐标，属于已知谱商标签，不能作为新的独立正性或容量输入。这里不换 evaluation 点，也不生成新的参数族。

## 3. 405 的真实 Pan 值：系数、正号与非主除子

用 [405](../../../notes/405-f1-adelic-restriction-moments-and-radical.md) 与574§4–5的固定 Gaussian／全整数规范，记
\[
 H(u)=e^{u/2}h(u),\qquad
 p=(D^2-\tfrac14)H\in P_{\mathrm{phys}}.
\]
这是实际 adele 限制给出的非 compact 关系；所有复倍数和物理平移仍是关系。旧式
\[
 \int e^{zu}H(u)\,du=\frac12\xi(\tfrac12+z)
\]
与强衰减下两次分部积分，给
\[
 \ell_z(p)=\frac12(z^2-\tfrac14)\xi(\tfrac12+z).
 \tag{6}
\]
物理变量的导数 \(D\) 在该积分中变为 \(-z\)，平方后系数为 \(z^2-\frac14\)；没有额外 \(e^{u/2}\) 或 Fourier 因子。代入唯一固定 \(z=1\)：
\[
 c:=\ell(p)=\frac38\xi(\tfrac32)>0.
 \tag{7}
\]
正号可由 \(\xi(\frac32)\) 的实正 Gamma／Euler 数据，或 \(\ell(p)=\frac34\int e^uH(u)\,du>0\) 核对；不用 RH 或零点假设。

取 root 已固定的合法实数倍
\[
 a=\frac{\log2}{2c}.
\]
则 \(ap\in P_{\mathrm{phys}}\)，但
\[
 P_{ap}=[\tfrac12\log2]\ne O.
 \tag{8}
\]
若 \([P_{ap}]-[O]\) 为主除子，就存在非恒定亚纯函数仅在 \(O\) 有至多一阶极点。旧371属一 RR 给
\[
 h^0(E,\mathcal O_E([O]))=1,
\]
只能是常数，矛盾。这里使用的是 **degree1 除子线 \(\mathcal O_E([O])\)** 的截面维数，不是只引用结构层 \(\mathcal O_E\) 的 \(h^0=1\)。故 \(J_{ap}\) 确非平凡 Pic⁰ 类，未成为所需 principal。

这已经结束首门。由于 \(\ell(p)\ne0\) 且全复倍数合法，该单标签的 Pan 点像甚至扫满 \(E\)；这只说明当前标签丢失了所需商区分，不把 Pan 集合等同于全部源。不裁成 compact Pan，不把拓扑闭包改叫 exact 成员，也不需要再展开 metric 或高度。

## 4. 同一个537正窗内的遗漏方向

沿 root 原稿的一份 two-bump 构造，不另加微分 kernel 或测试。令
\[
 I=(-17/16,17/16)
\]
为 [537](../../../notes/537-source-exact-weil-window-positive-tail-admission.md) 的物理 \(u\) 窗；它不是 log 尺度的另一个窗。在 \(I\) 内取支撑不交的两个非零非负 smooth bumps \(v_1,v_2\)，则 \(\ell(v_i)>0\)。定义
\[
 r_* =v_1-\frac{\ell(v_1)}{\ell(v_2)}v_2\ne0,\qquad \ell(r_*)=0.
 \tag{9}
\]
源是合法 complex 域中的实元素，原 du／零延拓 Dlog 费用有限；系数不由 \(Q_\zeta\) 或未知零点选择。537对**全部**该窗内非零 complex 源给
\[
 Q_\zeta(r_*)\ge 2^{-49162}\|r_*\|_{du}^2>0.
 \tag{10}
\]
但 \(P_{r_*}=O\)，\(J_{r_*}\) 是 unit；与零源有相同点数据。root 的混合线族在这条 source 方向落到同一指定 rigidified axis。因此，任何仅依赖这些点／线族和固定 axes 数据、在 unit 处与零源取同值的完整 mixed scalar 读出，不能等于完整 \(Q_\zeta\)：其对角在 \(r_*\) 与0上相同，而(10)不同。

这是旧有限通道全源 coverage 责任；没有要求 \(\ker J=P_{\mathrm{phys}}\)，也没有声称单个 fiber 的抽象一维性使整个 family 平凡。只作某个组件、单边估计，或另带实际原源、相对 frame、transgression 的规则，不由此自动排除；本固定定义没有这些额外数据。

## 5. 线值 mixed 对象与数值高度的类型界限

root 的对象固定为
\[
 \mathcal P=\mathcal O_{E\times E}
   (\Delta-E\times\{O\}-\{O\}\times E),\qquad
 \mathcal B(r,s)=(P_r,P_{\bar s})^*\mathcal P.
 \tag{11}
\]
覆盖 \(dw\) 用于两轴的相容常数线刚性化。(11) 是随两源变化的 line-valued family；一处 fiber 是一维复向量空间，不能直接称为实高度或 Hermitian 数值。因为 \(e^u\) 实，\(\ell(\bar s)=\overline{\ell(s)}\)，第二腿的方向与候选反线性意图相容，但尚未给 sesquilinearity、quadratic scaling 或正号。\(E\) 是加法群而非复向量空间，任意 complex 源缩放也没有自动成为椭圆曲线上的 intrinsic scalar multiplication。

固定 axes rigidification 没有提供全局 metric／section／数值 trivialization；real local height 亦不能不经定义变成 fullcomplex Hermitian Weil 型。局部 principal symbol 可有 evaluation 项，不能仅凭“主除子”字样断言任意 local Néron pairing 为零；全局补偿及算术定义域是另项付款。当前只有复曲线与复点，没有共同全局数域／整模型等数据，不能援引全局 Néron–Tate 正性替代这些责任。本稿不选择 metric、不计算 Green 高度，也不借这些未定义后段否定 line family 本身。

## 6. 实际 input／test／net 与停止

本门的 input 是已经冻结的 \((E_2,\ell_1,J_r,\mathcal B)\)；最便宜 test 是(7)–(8)的真实 noncompact Pan principal 检查，(9)–(10)仅核同一标签的完整读出 coverage。二者由旧405／574精确值、371实际 RR、537全源正窗及旧有限通道责任直接蕴含。当前新写的公式／费用记录没有改变这条 strongest-old 后果，也没有付出独立 signed／corecross、primitive mixed、整过滤容量或成长净身份。

因此按**标准／最强旧前置0**收讫，停止这个 fixed source；不建 C050／587，不换 evaluation／period，不追加 metric、frames 或 Green 拟合续预算。不把这次停止拼成长期 Goal 完成门，不泛排所有双扩张／强拓扑／源适应或非逐层 Pan 的 D′ 构造。Whole4/5 仍仅负惯性 UPPER；关键瓶颈未改。本稿为独占支持，不代 root 消费或自行结算 cadence。
