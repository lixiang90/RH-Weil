# Joint Type-II 纤维与 proper-power 全压缩独立审查

日期：2026-10-07。结论：**限定 PASS**。准确范围为有限物理重排与 support 恒等式 [T]、指定零自由/reciprocal 输入下的规范 coprime 二维 Mellin 估计 [T/R]、经典 mean-square 输入下的 proper-power 全有限矩阵估计 [T/R-MV]，以及有限整数/形式系数审计。实际 reciprocal-residue joint signed average、原 Type-II 尾部节省和新的四矩常数仍未支付。

## 1. 冻结版本与独立核验

全文被审报告：`reviews/2026-10-07/hybrid-joint-type-ii-fiber-research.md`，511 行，17846 个 canonical LF UTF-8 字节。

- 报告 SHA-256：`238fd374cad6da451fd186c6f3766d79d869ff8ae92ed6441e0ca516e1398473`。
- 完整读取的新脚本 `scripts/hybrid_joint_type_ii_fiber_audit.py`，205 行，8048 字节，SHA-256：`885130779ee38b9ce86933233ca4d323abc0a8ff4170be05247d7308d2d9fe9e`。
- 原 coefficient/centering note 239 SHA-256：`b35398ecdfbe65ce2ea04856a5e66f6676d61cc109b3de48e855b514db0cfa20`。
- 原有限 Gabor frame note 446 SHA-256：`08060477a6ea806d559fd67533d9e6d3b96483a755842cca9a048b6ab5e110cf`。

仅将 CRLF/孤立 CR 转为 LF。报告、脚本及旧文件均未编辑；独立执行这个新脚本只向 stdout 打印 JSON，没有写文件或覆盖旧审计。

## 2. 原物理对象、canonical completion 和 affine 重排

报告 §1 保留实际整数行数 \(D\)、carrier、双自然 gcd mask、原六窗口、共同正轴 shell 和 atomwise common centering。primitive 两侧的 \(ad-bc=0\) 当且仅当 \((a,b)=(c,d)\)，所以 exact diagonal deletion 合法。centering 是各 channel 上同一个线性操作；没有在合并前为各 ghost channel 建立不相容的 absolute 主项预算。

\[
 B_V(n)=\sum_{v\mid n,\ v>V}\Lambda(v),\qquad
 \sum_{r\mid a}\mu(r)B_V(a/r)=\Lambda(a)
 \quad(a>V)
\]

由 \(\mu*1*\Lambda_{>V}=\Lambda_{>V}\) 严格推出。原 \(I/II\) ranges 的合并与 ordered numerator tensor 重构正确，不是替换成任意有界 coefficient。

取 \(r=gu,s=gv\)。非零 Möbius 项使 \(g,u,v\) 两两互素且 squarefree，\(\mu(r)\mu(s)=\mu(u)\mu(v)\)。自然 mask 给 \((g,q)=1\)，其中 \(q=(b,d)\)；故 \(gq\mid h\) 而非仅分别的 divisibility。primitive mask 还保证 \((ud_0,vb_0)=1\)，因此公式 (17)–(18) 的唯一 residue representative 和全部整数 affine 解正确，包括 modulus 为 1 的约定。

实际 kernel argument 在公式 (18a) 保留

\[
 X\log\frac{uA_\ell d_0}{vb_0C_\ell}
 =X\log\left(1+\frac{h/(gq)}{vb_0C_\ell}\right).
\]

没有将其错误变成只依赖 determinant 的 \(K(h/g)\)。因 \(b_0,d_0\asymp Y/q\)，\(A\)-range 长度与 progression step 的比给 real interval \(O(q/(guv))\)，整数点数必须另带 \(1\)。公式 (20) 的全部交叉 natural masks、有限 ranges、原窗口和正负/noncore shells 保留；这是精确重排，不提供每条 sparse fiber 的 cancellation。

## 3. Core coprime 投影只对合并后的完整物理和可用

§3 的 denominator core \(q=1\) 使用真正 \(\Lambda(b)\Lambda(d)\) support：若两者同 prime base，\((b,d)=\min(b,d)\ge c_1Y\)，而此 gcd 整除非零 \(h\)，与 \(|h|<c_1Y\) 矛盾。

§4.1 对 numerator 的同一论证只有在各 divisor blocks 合并为完整 \(\Lambda(a)\Lambda(c)\) 后成立。于是完整 core 可乘 \(1_{(a,c)=1}\)，包括 atomwise 线性 common-density subtraction；不能先对一个独立 II–II 或 mixed entry 使用此投影。展开后它准确等价于

\[
 (r,s)=(r,C)=(s,A)=(A,C)=1.
\]

后三项不可删除。报告没有借此在原 Type-II entry 中单独丢 ghost atoms，也没有将 whole-core 的 \(g>1\) 精确消去冒充独立 Type-II 小量。

## 4. 规范 coprime 二维 Mellin 估计的真前件

§4.2 的局部 identity 可直接由 coprime alternative
\(1-\chi(p)p^{-z}-\psi(p)p^{-w}\) 核验。显示 Euler correction 的 departures 为 \(O_a(p^{-2a})\)，对 \(\Re z,\Re w\ge a>1/2\) 高度、角色一致；一般的局部正常收敛域还要求两实部均正且和大于 1。没有误用 correction reciprocal，也不要求其无零。principal \(1/L\) 在 1 为零，不产生 residue。

在所述全角色无零及 uniform reciprocal 前件下，先固定 gap、profile 与 seminorm orders，分别将二维线移到 \(a=\theta+\delta<1\)，即可得到公式 (20e)。\(q_{\rm eff}\) 必须包括 deleted Euler radicals；附加 coprime zero extension 也必须重计其 effective modulus。这里的统一性仅覆盖固定平滑二维 profile 及其已付 seminorms。

报告 354–361 行准确说明这尚不能支付真实 affine residue fiber：moving congruence、\(B_V(A_\ell)B_V(C_\ell)\)、sharp integer incidence 和全 masks 未准入为尺度独立的 smooth profile。规范 coprime \(\mu\otimes\mu\) 的节省不能直接搬到实际 high-prime tail。此限制是结论范围的一部分，不是证明缺口被隐藏。

## 5. 全 proper powers 的原 AF compression 估计

§6 的两个 coefficient bounds 正确。平方项用 Chebyshev 加 Abel 给 \(\sum_{p\le\sqrt X}\log p/p\ll\log X\)；\(j\ge3\) 的绝对和收敛，而所有 \(j\ge2\) 的平方 coefficient 总和一致有界。

所需 mean-square 输入是作者原论文 [Montgomery–Vaughan, *Hilbert's Inequality*, Corollary 3, p.75](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)。对于本有限 polynomial，其标准 remainder 被 \(X\) 乘 coefficient 平方和控制；起点平移只乘单位相位，\(|J|\asymp X\)，故 \(\int_J|R_X|^2\ll X\)。无需 prime-pair 输入或改进无零区；这个经典输入并未由有限 audit 证明。

与 note 446 原 normalization 对照，\(F=U/\sqrt{2\pi L}\) 是 contraction，且

\[
 E_{\rm pp}=(2\pi/(a_LL))F^*M_{\rm pp}F
            =(a_LL^2)^{-1}U^*M_{\rm pp}U.
\]

实际 finite Parseval 给 \(\sum_k|f_k(t)|^2\le a_LL^2\)。\(a_L\) 最终离零、\(d\asymp XL\asymp N\)、原 taper 支撑/二阶 Fourier tail 的前件保留；不需要更强的 \(d=N+O(L)\)。

对真实 Hermitian multiplier，

\[
 \|F^*MF\|_{\rm HS}^2\le\operatorname{Tr}(F^*M^2F)
\]

直接来自 \(FF^*\le1\)。因此 \(J\) 内贡献为 \(O(X/L)\)。\(J^c\) 上使用全高度 \(|R_X|\ll L\)，同时原 \(C^2\) tail 给 \(\sum_k\int_{J^c}|f_k|^2\ll dX^{-3}\)，从而规范贡献为 \(O(X^{-2})\)。低绝对高度没有遗漏。

合并即得

\[
 \|E_{\rm pp}\|_{\rm op}\ll1,\quad
 \|E_{\rm pp}\|_{\rm HS}^2\ll N/L^2,\quad
 \operatorname{Tr}E_{\rm pp}^4\ll N/L^2=o(N).
\]

最后一步用 Hermitian eigenvalues 的 \(\lambda^4\le\|E\|_{\rm op}^2\lambda^2\)，没有调用错误的 \(x^4\) operator convexity。这支付全部 \(p^j\le X,j\ge2\) 的原有限矩阵，而不是高-product 某个独立 raw cell。

## 6. 四矩约化的条件范围

§7 的 \(H_{\rm pr}=H_{\rm full}-E_{\rm pp}\) 保留原背景和其他 corrections。Schatten triangle 给 finite-constant \(O(N^{1/4})\) 前件的双向等价。只有确实取得这个前件以后，非交换 telescoping 及四因子 Schatten Hölder 才给

\[
 |\operatorname{Tr}H_{\rm full}^4-\operatorname{Tr}H_{\rm pr}^4|
 \ll N L^{-1/2}=o(N).
\]

这保留全部 mixed words，无独立性假设。note 446 的 growing fourth bound 不满足这个前件；报告明确保留 actual joint high-prime average、cross-cell/alias 账本及有限四矩常数为开放任务。没有据 proper-power 小量推出新临界线比例。

## 7. 新脚本独立执行和范围

本轮从仓库根目录运行 `python scripts/hybrid_joint_type_ii_fiber_audit.py`，退出码 0，打印 PASS，并检查冻结报告哈希。输出计数：

- primitive nonzero-determinant quadruples：4290；
- nonzero Möbius divisor pairs：37000，其中 shared-divisor pairs 3928；
- denominator prime-power core rows：78；
- complete physical prime-power core rows：4。

检查包括 canonical completion、ordered \(\log p\otimes\log q\) 整数 coefficient 重构、primitive diagonal、\(gq\mid h\)、Möbius common sign square、affine 解和实际 ratio 的整数交叉乘法、core coprimality。37000 表示 Möbius factor 非零的 divisor pairs，不声称各个 \(B_V\)-加权项都非零。形式 log basis 的整数验证没有依赖浮点 residual。

脚本只检验 \(a,b,c,d\in\{12,\ldots,22\},V=3\) 的有限代数；不检验窗函数分析、Gaussian/Fourier 无限尾、prime asymptotics、条件 reciprocal estimate、mean-square 定理、Type-II cancellation 或新的零点比例。报告对这些范围的区分准确。因此给出上述限定 PASS，没有需要作者修正的阻断点。
