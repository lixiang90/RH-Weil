# 472：原短载波全四阶压缩与比值方差总结的独立审查

2026-10-08。radial_review。结论：**限定 PASS**。
全文读取最终笔记194行，并逐式与三篇完整研究源比较；
另外独立执行新检查器的finite()，32个命名检查组全部通过。
只写本审查，不修改笔记、作者源、旧审查、math、输出或Git。

被审笔记：
[472-original-short-carrier-fourth-compression-and-ratio-variance.md](../../notes/472-original-short-carrier-fourth-compression-and-ratio-variance.md)，
canonical UTF-8 LF SHA-256
**9856885e932a892cf7c33ece82f430c2ec13004555eb52da2f1e8b1ec6bb2683**，
9037 bytes，194行。只统一CRLF/lone CR为LF，不trim或改变EOF。
最后相对4cb98稿只将显示记号改为Tr((E*BE)^4)，明确矩阵四次幂的迹；
没有改动数学命题或费用。

## 1. 实读输入及审查对象

| 输入 | canonical LF SHA-256 |
| --- | --- |
| [raw whole-P平均源](hybrid-anchored-carrier-averaged-fourth-projection-gap-research-radial.md) | c0e874ab9061982c8ef4365c8e9313eeac77eeddb756dc0b455cab3349f99dd8 |
| [half-ratio / 四全异criterion源](hybrid-whole-short-carrier-ratio-and-distinct-criterion-research-twisted.md) | c7ff142ebe15232542626e4feda3c05a1285cbf7bff64f462e734c662dafea53 |
| [二阶tail完整源](hybrid-second-order-tail-coupling-and-strip-geometry-research-compression.md) | e5c21e3a8bb0cb52e9e3131259a52dbb42051d7eb514ca8a65b083128b88d444 |
| [465真实weighted second](../../notes/465-centered-high-square-joint-fourth-budget.md) | a9290d2d847c2a3f7942b26353bd1582a68b391e481acc109c4ac18d3d750464 |
| [456完整repeated union](../../notes/456-high-opposite-four-word-vanishing-and-repeated-limit.md) | 7de855634f93f9d92f6d0cbdd762f9894effaaf40f788b3e02de89f961eadb96 |
| [新有限检查器](../../scripts/hybrid_short_carrier_checkpoint.py) | f66dd8cf3d6f67e2c7ec323bc7eed841144cd7bfa4d0cafdec428fec04c8365d |

本次summary作者为root。raw carrier研究源由本审查者提出；
其另外作者独审单独登记，本审查只认证root总结的对应对象、
全量量词与作用域，不将自己源的作者复算登记为另一作者独审。
criterion全文独审另见
[ratio审查](hybrid-whole-short-carrier-ratio-and-distinct-criterion-review-radial.md)。
tail源已实际完整读取292行，并在下文重新给出(6)的有限证明。

原197、304的计数及Schur--Jensen接口和228的移动零块范围
按既有冻结输入使用。本审查没有重新认证AF零侧分析内核，
也没有使用228旧的未付四矩上界或其条件性比例常数。

## 2. §2–3：raw whole-height平均及全部16词

X=T/(2pi)、ell、floor d、phi、a_ell、sharp b_p在整个窗口冻结。
E_sigma只作共同modulation，physical shift保留原实线零延拓。
全interval Fourier outside basis的entry计算保留min(d,|n|)
准确pair count，没有将真实P改成全局Fourier guard。

任意实平移区间上的weighted MV给
avg|D_R|²≪1+X/(ell s)；原C² shifted-lattice与Minkowski于是给
avg lambda_R²≪ell+X/s。
在s=T/sqrt ell下为O(ell)，原raw op²≪X/ell²及d∼Xell给
normalized四阶费用O(ell^−2)。
这个推导是整个高度轴的finite multiplier计算，不使用zero-free [R]、
bad-height删截、different-prime leakage正交或未知H4 bounded。

对任意bounded Hermitian B，A=E*BE、
K=(QBE)*(QBE)≥0，exact block展开为
\[
 \operatorname{Tr}(E^*B^4E)-\operatorname{Tr}A^4
 =\|QB^2E\|_{\rm HS}^2+2\operatorname{Tr}(A^2K)
                          +\operatorname{Tr}K^2\ge0.
\]
三个项的费用之和至多7||B||²||QBE||HS²。
笔记最终trace括号已准确，(2)对high及full high+low均相符。

三个内部P的八条闭合路径中，除全P路径外的七条均至少两次crossing。
six-pair bound及共同sigma上的Cauchy给每个ordered H/L词的
mean absolute费用O(ell^−2)。因此(3)包括全部16词及聚合后的
prime signs、重复与全异标签；没有逐tuple免费删P。

笔记保留两种共同集合：以固定倍数阈值得到measure至少s/2及
逐点O(ell^−2)；以较弱趋零阈值得到relative measure1−o(1)。
这两种选择均合法，不能将它们的不同速率自动混同。
另一算术good point须在选择前与这同一defect账本结合。

moving zero block的长度2pi d/ell=T+O(ell^−1)；
其相对于[T,2T]的端点移动O(s)，标准局部计数界给
O((s+1)log T)=o(N)。与228的同配置接口相容。
这不证明原sigma=T处逐点误差，也不自己完成零侧证书。

## 3. §4：实际q、压缩平方及完整实线ratio互不混同

原same-prime multiplication w_T与有限W保持原配置；
共同modulation与该乘法交换。465的two-crossing weighted second
及Hilbert/alias费用对sigma uniform，误差为additive o(1)，
不乘未知q或a。因此
\[
 q_\sigma=a_\sigma-S_T+o(1)
\]
在整个短窗口成立，无H4 bounded前件。

456的完整repeated partition与其near/far费用也uniform：
phase只改变prime端点unit factors或|K_d|之外的单位模量。
因此D_sigma=a_sigma−2S_psi+o(1)仍是原actual四全异union。

physical high步长大于ell/2，准确有A=Pi_- A Pi_+及A²=0。
K=CJ逐个固定E_sigma e_k，两个physical half块的输出正交、
HS norm相等；finite E*A E没有被错误称为nilpotent。
已付diagonal--ratio cross uniform O(ell^−1)给
\[
 \Phi_\sigma=S_T+2r_\sigma+O(\ell^{-1}),\qquad
 r_\sigma=\|R_+E_\sigma\|_{\rm HS}^2/d\ge0.
\]
这里2r等于完整实线(B_H²−M_wT)E_sigma的平方范数；
q_sq是另一种仍有内部P的压缩两步平方，Phi则是不扣W的
完整physical fourth。笔记136–138行明确区分，未借PSD错误平方排序。

由whole-P平均桥，|q−2r|与|D−(2r−S_psi)|的窗口L¹都趋零。
误差界不乘r、q或H4，故(4)具有增长统一性。
(5)用nonnegative r与高相对measure共同集合选点；
若B_T增长，必须保留1/(1−eta_T)的损失，笔记已明确。

本轮新成果是双向L¹及全部16词共同载波准入。
旧Jensen早已给r upper至q upper的单侧蕴含，笔记没有重复报为突破。
实际natural short-window r upper没有由这些恒等式支付。
ratio/products的X²长度、long-width消频与原o(T)移动区间的
不相容范围均准确；没有从long mean0推出(5)的目标。
470原qstar及旧Q=1/350的排除也未被撤销。

## 4. §5(6)：同一槽位上可加的二阶尾

这一节的A是原有限零点矩阵，P=VV*、Q是其零点计数分解；
它与前节high算子的block记号是不同配置，不能将未知四矩
或单个未压缩离线pair的谱直接代入本节账本。

令F(t)=4t−t²。对lambda≤p、p≥0，直接分lambda<0、
0≤lambda≤2、lambda>2三段，有
\[
 F(\lambda)+\kappa_2(\lambda)\le
 \phi(p),\qquad
 \phi(p)=\begin{cases}4p-p^2,&p\le2,\\4,&p\ge2,\end{cases}
        =2p+1-j(p).
\]
min-max从n_+(Q)≤b给lambda_(i+b)(A)≤p_i(P)。
前b槽位的F+κ₂至多4；随后s槽位使用上式；
剩余lambda≤0，F+κ₂准确为0。
G=V*V的s个特征值包括必要的零值，因此求和严格得到
\[
 4\operatorname{Tr}A-\operatorname{Tr}A^2
 \le4b+2p+s-\operatorname{Tr}j(G)-\operatorname{Tr}\kappa_2(A).
\]
故笔记(6)同时保留两项成本，没有重复计算同一j(G)余量。
代入原p+2b≤N+E_0即给其后显示的s下界。

κ₂的noncommuting PSD/contraction变分式由谱基逐对角完成平方
证明；非对角条目只增加square成本，最优变量为实际谱正负parts。
恢复使用Hoffman--Wielandt及
|κ₂(x)−κ₂(y)|≤(4+2|x|+2|y|)|x−y|，
只需normalized second及同配置S2小误差，不需full fourth。
原三点j(G)成本可同加，但实际正密度κ₂收益仍未付。

7/8条带换成标准化坐标后仍为3log T/(16pi)增长宽度，
不能提升simple实轴三点核或约束其真实间距。
单对off-axis负谱不能在finite compression及其他pair相互作用后
逐项相加。笔记的几何限制与tail完整源相符。

## 5. 新检查器的方法与独立实跑

检查器当前canonical LF SHA
f66dd8cf3d6f67e2c7ec323bc7eed841144cd7bfa4d0cafdec428fec04c8365d，
10476 bytes，221行，已全文读取。

实际运行用Python -B及runpy.run_path的非main名称，只调用finite()。
不执行build()，没有生成或覆盖JSON、旧输出、cache或Git。
返回32个命名检查组全部PASS：

- 3组符号指数及short-window端点费用；
- 5组complex Hermitian finite block正差、非负性、
  Frobenius原始范数费用、same-W residual恒等式及夹界；
- 全部16 ordered H/L词各7条非平凡P/Q路径的exact trace展开；
- 3组反线性fixed-carrier有限模型的half/full factor2与diagonal展开；
- 5组rank-trace scalar槽位、tail变分最优值、
  low效果正负平方形式及完整distinct常数偏移。

script的finite七倍费用使用Frobenius范数作为operator norm上界，
这是有限模型的合法粗测试；不声称数值核验了原prime op。
scalar槽位和效果取有限有理样本，完整任意参数范围由tail源的
分段证明支付。程序不把有限assert当成MV、Minkowski、
真实carrierFourier、素数渐近或ratio算术upper的证明。

checkpoint build另核现行source/review哈希及文件链接；
它没有独立重证这些分析输入。
最终script只新增self-output链接的首次生成例外：解析路径恰等于
OUTPUT.resolve()时，由main写入或--check读取核验该输出的存在，
其余链接仍必须存在。把这唯一guard及两行注释还原后，精确恢复
已实跑finite()版本f0777ac65e0a7924efe8026aaabb2df536c76413f8c188c5aa733b88369ff60f。
因此32组有限数学没有变化；该修复只解开首次生成的文件存在性循环。
本审查在生成最终output之前完成；最终output与全--check
由root生成后另作只读验收，不在这里预报已经执行。

## 6. 最终结论

**限定 PASS**：472准确保留原whole-height短carrier准入、
all16共同选点、增长统一q/full-ratio判据及可同加二阶尾的前件。
32组有限检查已独立实跑通过；全部分析结论仍由完整源证明承担。

完整短窗ratio upper与实际正密度tail收益均未付。
没有新的实际simple-critical-line比例、无零区域或RH证明。
