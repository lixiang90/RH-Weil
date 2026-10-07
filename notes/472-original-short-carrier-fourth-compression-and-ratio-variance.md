# 472：原路线的短载波四阶压缩付款与完整比值方差

2026-10-08。基线 2d5621dbc999e0cf313ea224b825d6d56547c45c。

回到原 Eisenstein / AF 路线后的实际进展：在合法的短起点窗口中，
原 high/low 素数算子的全部四阶内部投影误差已经付清；实际 high
平方残差与明确的完整 half-ratio 方差双向一致，并能保留同一个
起点上的全部 16 个有序混合四词。证明没有新的无零前件，也不要求
未知 high fourth 先有界。仍未证明完整比值方差的有用上界，
没有新的实际零点比例、无零边界或需要发表的边界论文。

另有原二阶 rank--trace 证书的谱尾保留式，可以和原三点 Gram
成本同加；它同样尚缺实际正密度收益。这两项分别处理四阶压缩和
二阶谱尾，不能把它们的开放算术输入相互代替。

## 1. 完整推导与审查来源

Markdown canonical 仅统一 CRLF/lone CR 为 LF，不 trim 或改 EOF。

| 本轮完整研究源 | canonical UTF-8 LF SHA256 |
|---|---|
| [短窗口中的原 P leakage 和整个四阶正差](../reviews/2026-10-08/hybrid-anchored-carrier-averaged-fourth-projection-gap-research-radial.md) | c0e874ab9061982c8ef4365c8e9313eeac77eeddb756dc0b455cab3349f99dd8 |
| [完整 half-ratio 方差与四全异目标](../reviews/2026-10-08/hybrid-whole-short-carrier-ratio-and-distinct-criterion-research-twisted.md) | c7ff142ebe15232542626e4feda3c05a1285cbf7bff64f462e734c662dafea53 |
| [可同加二阶谱尾、实际效果对偶与条带量纲](../reviews/2026-10-08/hybrid-second-order-tail-coupling-and-strip-geometry-research-compression.md) | e5c21e3a8bb0cb52e9e3131259a52dbb42051d7eb514ca8a65b083128b88d444 |

root 对三篇完整新源的独立审查见
[全文审查](../reviews/2026-10-08/hybrid-short-carrier-ratio-and-tail-review-root.md)。
有限检查与准确最终 source/review 绑定见
[检查器](../scripts/hybrid_short_carrier_checkpoint.py)、
[输出](../output/hybrid-short-carrier-checkpoint.json)。
这些文件不能把有限数值检查提升为素数渐近证明。

## 2. 原对象不变，起点只在 o(T) 窗口移动

固定原
\[
 X=T/(2\pi),\quad \ell=\log X,\quad d=\lfloor X\ell\rfloor,\quad
 I=[-\ell/2,\ell/2],\quad s=T/\sqrt\ell .
\]
原 even C² taper、normalizer a_ell、sharp prime cutoff、b_p 全部冻结。
令 sigma∈J_T=[T,T+s]，
\[
 E_\sigma e_k=\ell^{-1/2}1_I
 e^{i(\sigma+2\pi k/\ell)u},\quad
 P_\sigma=E_\sigma E_\sigma^*,\quad Q_\sigma=1-P_\sigma .
\]
这是真实零延拓 interval carrier 的共同 modulation。写
\[
 B_R=-\sum_{p\in R}\frac{\log p}{a_\ell\ell\sqrt p}
     M_\phi(R_{\log p}+R_{-\log p})M_\phi,\qquad
 C_{R,\sigma}=E_\sigma^*B_RE_\sigma ,
\]
R=H 为 sqrt X<p≤X，R=L 为 p≤sqrt X。原实线平移未周期化。
下文 avg 是 J_T 上 normalized Lebesgue 平均，tau=Tr/d。

## 3. 新付款：整四阶实际压缩误差趋零

对 lambda_R(sigma)=||Q_sigma B_R E_sigma||HS，完整原 Fourier
entry、outside count min(d,|n|)、C² shifted-lattice 能量与
interval-uniform finite Montgomery--Vaughan 二矩一起给
\[
 \boxed{\operatorname{avg}\lambda_R^2
 \ll\ell+X/s=O(\ell).}                                      \tag{1}
\]
本估计是 raw whole-height 的付款，无 [R]、无 good-height 截断，
也没有不同素数 leakage 正交的假设。

一般 Hermitian B 的准确正差为
\[
 \Tr(E^*B^4E)-\Tr((E^*BE)^4)
 =\|QB^2E\|_{\rm HS}^2+2\Tr(A^2K)+\Tr K^2
 \le7\|B\|^2\|QBE\|_{\rm HS}^2 ,
\]
A=E*BE，K=(QBE)*(QBE)。结合 raw ||B_H||²≪X/ell² 与 d∼Xell，
对 high 或 full B_H+B_L 均有
\[
 \boxed{0\le\operatorname{avg}
 \left[\tau(E_\sigma^*B_H^4E_\sigma)-\tau C_{H,\sigma}^4\right]
 \ll\ell^{-2}.}                                            \tag{2}
\]
正差恒等式本身是既有结果；新增的是原算子实际平均能量的支付。

对每个 ordered (R_1,R_2,R_3,R_4)∈{H,L}⁴，准确 three-P
展开的七条非平凡路径均至少两次 crossing，故
\[
 \boxed{\operatorname{avg}\left|
 \tau(E_\sigma^*B_{R_1}B_{R_2}B_{R_3}B_{R_4}E_\sigma)
 -\tau\prod_{i=1}^4 C_{R_i,\sigma}\right|\ll\ell^{-2}.}       \tag{3}
\]
这是 mean absolute，不是 signed average。它包含全部 prime signs、
重复标签与全异标签的聚合；并非逐 tuple 的投影删除。
可以一次 Markov 选出 measure≥s/2 的集合，使全部 16 词同一
sigma 的误差 O(ell^(-2))；也可用较弱 o(1) 阈值得到
relative measure 1−o(1) 的共同 good set。
固定原起点 sigma=T 的逐点误差未因此被证明。

原零点块 J_sigma=[sigma,sigma+2πd/ell) 对 [T,2T] 的对称差计数为
O((s+1)log T)=o(N)。所以这个选点范围与
[228 的移动零块传递](228-relative-dense-zero-block-transfer.md)相容。
必须先在同一个 good set 内取得后续算术估计；不同高度的好点
不能直接拼成同一个零点证书。

## 4. 已付桥之后的真实算术目标

保持原 same-prime 乘法中心 w_T 与 W=E_sigma*M_wT E_sigma。
它不随共同 modulation 改变。定义
\[
 q_\sigma=\tau(C_{H,\sigma}^2-W)^2,\quad
 a_\sigma=\tau C_{H,\sigma}^4,\quad
 S_T=\ell^{-1}\int_I w_T^2\longrightarrow S_\psi .
\]
[465 的实际加权二矩](465-centered-high-square-joint-fourth-budget.md)
对短窗口 uniform 给 q_sigma=a_sigma−S_T+o(1)，其误差不乘未知
a 或 q。令 D_sigma 为
[471](471-original-principal-subtraction-and-signed-four-distinct-target.md)
定义的整个四全异 signed union，则
D_sigma=a_sigma−2S_psi+o(1)。

定义正平移半块及其真正 ratio remainder：
\[
 A=-\sum_{\sqrt X<p\le X}b_pM_\phi R_{\log p}M_\phi,\quad
 G=A^*A,\quad D_+=\sum_p A_p^*A_p,\quad R_+=G-D_+,\quad
 r_\sigma=d^{-1}\|R_+E_\sigma\|_{\rm HS}^2\ge0 .
\]
A=Π_-AΠ_+，所以 physical A²=0；有限 E*AE 未被称为 nilpotent。
反射加复共轭的反线性 K=CJ 准确固定每个 E_sigma e_k，
两半块能量相等。原 diagonal--ratio cross uniform 为 O(1/ell)，故
\[
 \tau(E_\sigma^*B_H^4E_\sigma)=S_T+2r_\sigma+O(\ell^{-1}).
\]
结合 (2)，新双向结论是
\[
 \boxed{\operatorname{avg}|q_\sigma-2r_\sigma|=o(1),\qquad
 \operatorname{avg}|D_\sigma-(2r_\sigma-S_\psi)|=o(1).}       \tag{4}
\]
full physical ratio B_H²−M_wT 的能量是 2r；q_sq=
||E*B_H²E−W||²_(2,d) 是仍保留一个内部 P 的另一种量。
这些对象均没有被混同。

如果将来确实证明 avg r_sigma≤B_T，共同 good set 的相对测度
1−eta_T 给同一个 sigma_T：
\[
 q_{\sigma_T}\le\frac{2B_T}{1-\eta_T}+o(1),\qquad
 D_{\sigma_T}\le\frac{2B_T}{1-\eta_T}-S_\psi+o(1).             \tag{5}
\]
只有 B_T=O(1) 时，分母的选择损失才是 additive o(1)。
本篇未提供任何 B_T 或小 Q 数值。
旧 scalar Jensen 已使 r upper 成为 q upper 的单侧充分条件；
本轮新增的是双向 L¹ 一致及全部 16 词的共同选点付款。

待估的 r 仍是原共同窗内两素数比值列的完整平方，products 可长至
X²，ratio 对数间距仅按 X^(-2) 控制，观察高度仅 O(X)。
把高度平均扩大到 X² 可消去 D 的全部非零频率，却不属原
o(T) 零块传递范围。这个 long mean=0 不是 (5) 的短窗口上界。

flat 时 S_psi=19/480，已有
[470 的必要下界](470-centered-spectral-variance-excludes-small-high-residual.md)
qstar=(sqrt(104899)−275)/15120≈0.00323288。
它排除旧 Q=1/350；本轮没有将一个不可能的目标重新作为证书。

## 5. 原二阶证书可以保留什么

对实际零点有限矩阵 A=P+Q，P=VV*≥0、V 有 s 列、
p=Tr P、n_+(Q)≤b，令 G=V*V，
\[
 j(t)=(t-1)^2-(t-2)_+^2,\qquad
 \kappa_2(t)=t_-^2+4t_-+(t-2)_+^2 .
\]
同一个 Weyl 槽位证明给
\[
 4\Tr A-\Tr A^2
 \le4b+2p+s-\Tr j(G)-\Tr\kappa_2(A).                        \tag{6}
\]
原账本 p+2b≤N+E_0 推出
s≥4Tr A−Tr A²−2N−2E_0+Tr j(G)+Tr κ₂(A)。
因此 simple Gram 的既有三点成本与完整负尾/超过 2 的正尾可以同加。
κ₂ 的准确 PSD/contraction 效果对偶与恢复只需二矩，见完整源。
仍须证实际 liminf Tr κ₂(A_T)/N(T)>0 才有额外比例增益。
目前实际 low-only、固定正 row 权重效果的主项收益方向不支持该增益。

原 7/8 条带在标准化零坐标中的宽度为 3log T/(16π)，不会趋零，
没有约束 simple on-line 的实间距，也不提高原三点核常数。
单个未压缩 off-axis pair 的负特征值不能直接相加成完整配置的谱尾。

## 6. 完成范围

本轮付清合法短窗口中的全四阶压缩修正，得到真实 ratio 方差的
双向归约，并核实可同加的二阶谱尾接口。有限检查覆盖指数费用、
非交换块恒等式、全部 16 词的七路径、half-ratio factor2 与尾对偶。

继续研究的实际目标为：在同一个短窗口支付完整 r 的有用上界，
或构造原 carrier 中具有可证正密度收益的谱尾效果。两项均未证。
数域选择保持原 Q(sqrt(-3))；既有比例、边界与论文不因本轮接口
结果改变，也没有把条件性判据写成新纪录。
