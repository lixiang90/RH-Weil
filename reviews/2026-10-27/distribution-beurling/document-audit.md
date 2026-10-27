# 附件独立审读：分布化 Beurling–Weil 的接口、归一化与当前增量

2026-10-27。仅审读用户附件《分布化Beurling–Weil结构与广义黎曼猜想.md》及项目直接相关资产；附件中的研究安排视为待评价内容，不视为新的用户指令。本稿不新开数学合同，不重计旧结果。状态、轮数和root消费由主稿统一处理。

## 1. 可以保留的判断

附件的主要划分正确且有用：正primitive测度／Euler包络、Mellin反射／模对偶、完整显式公式、独立正性／纯度是不同责任。尤其不能由前三者推出第四者。其正迹与对应代数定理可作为**充分接口**，不能据此说经典对象已经进入正性类。

这与项目562–567完全相容：562/563已有同一正continuous primitive族的正负两段；567用同源全Π构造对偶、复合、trace和正的不同图交数，负段的primitive Gram仍失败。真正函数域的负交数来自同一对象上的截面乘法、有效性、surface RR及固定容量，并由完整点数／全周期身份接到Weil型。

附件强调普通测度张量积不构成Deligne放大，也应保留。项目567§6已定位：需要同一tensor族的局部幂迹非负与全局极点预算同时支付；原经典ζ的Euler参数1并不是其全局非平凡零点的纯度。

## 2. 三处必须先改的明确公式

### 2.1 prime-power测度少了1/m

附件§2.1设

\[
\widetilde\pi=\sum_{m\ge1}\frac1mD_m\pi,
\qquad Z(s)=\exp\int e^{-su}d\widetilde\pi(u).
\]

求导直接给

\[
-Z'(s)/Z(s)=\int e^{-su}u\,d\widetilde\pi(u).
\]

所以正确的von Mangoldt测度是

\[
\lambda=u\widetilde\pi=\sum_{m\ge1}\frac{u}{m}D_m\pi,
\]

不是文中的 \(u\sum_mD_m\pi\)。对 \(\pi=\sum_p\delta_{\log p}\)，前式在 \(m\log p\) 的系数是 \(\log p\)，文中定义则是 \(m\log p\)。这会改变所有proper powers，必须在进入显式公式前统一修正。

### 2.2 Haar自相关与中心1/2的Mellin对合未匹配

按附件§4.2的字面定义

\[
h(x)=\int g(xy)\overline{g(y)}\frac{dy}{y},
\qquad \widehat g(s)=\int g(x)x^s\frac{dx}{x},
\]

代换 \(t=xy\) 得到的是

\[
\widehat h(s)=\widehat g(s)\overline{\widehat g(-\bar s)}.
\]

不是文中声称的 \(1-\bar s\)。有两种可行修正，须择一全程固定：

* 用中心化变换 \(\widehat g_c(s)=\int g(x)x^{s-1/2}dx/x\)，保留Haar自相关；此时正确反射是 \(1-\bar s\)。
* 保留文中的 \(x^s\) Mellin变换，把对合改为 \(g^*(x)=x^{-1}\overline{g(x^{-1})}\)，从而 \((g*g^*)(x)=\int g(xy)\overline{g(y)}dy\)。

不能在 \(dy/y\)、\(x^s\) 和中心1/2三者之间无声移位。项目physical \(r=e^{u/2}f\)／原du的费用也必须随实际选择运输。

### 2.3 Frobenius行列式既重复归一化又颠倒零极方向

附件§5.2先设 \(\Phi\Phi^\vee=q1\)，所以未归一化 \(\Phi\) 的谱模是 \(\sqrt q\)。其后又写

\[
\det_{\rm reg}(1-q^{1/2-s}\Phi)^{-1}.
\]

若 \(|\alpha|=\sqrt q\)，该式的奇性满足 \(q^{1/2-\Re s}|\alpha|=1\)，即 \(\Re s=1\)，不是1/2。应二选一：

\[
P_1(q^{-s})=\det(1-q^{-s}\Phi),
\quad\text{或}\quad
P_1(q^{-s})=\det(1-q^{1/2-s}U),\ U=q^{-1/2}\Phi.
\]

曲线的H1因子在zeta分子，H0/H2在分母。若取逆，行列式零点成为该因子的极点；必须用真实分次行列式保留零／极及重数。这里只作公式核对，不对未定义的无限维正则化行列式授予存在性。

## 3. 还需补齐的量词和算子域

1. **近零质量。** “有指数可积性”若仅指 \(\int e^{-\sigma u}d\pi<\infty\)，不足以定义 \(\widetilde\pi\) 的Laplace积分。正测度情况下可直接要求某 \(\sigma>0\) 有
   \[
   \int-\log(1-e^{-\sigma u})d\pi(u)<\infty.
   \]
   因为近零需对数矩。例 \(d\pi=du/[u(\log(1/u))^2]\) 于 \((0,e^{-1})\) 的总质量有限，但对数矩发散。带权正测度空间中的卷积指数可精确处理；“必要时放进某个分布空间”不能代替存在证明。
2. **测试分离。** 能对有限零点四点组插值不足以单独支付无限尾控制。广义Weil判据必须保整个测试域、增长、对称求和以及其余除子的可控贡献。项目562/563已给带前件版本，不必重新创建未经闭合的最一般类。
3. **一般只能半正。** 非零测试可处于正型分布的核；例如有限频率正分布可有非零测试的Fourier变换在其支持全为零。不能从有限组分离直接升级为“所有非零测试严格正”。
4. **定理A。** 修正对合后，普通迹正性是合法充分接口。应明确 \(U\) 是同一测试代数的有界 * 表示，产品和迹循环是否合法。若 \(B=U(g)\)，\(U(g*g^*)=BB^*\)，安全的正平方是 \(\operatorname{Tr}(S^{1/2}BB^*S^{1/2})=\|B^*S^{1/2}\|_{\rm HS}^2\)，须支付其Hilbert–Schmidt域及与原迹的身份。文中 \(\operatorname{Tr}(BSB^*)\) 的顺序在一般非交换代数不能直接代入；此处乘法群测试代数交换，\(B\) normal，加上足够迹类／循环前件可以修复。另一种办法是固定 \(g^**g\) 的顺序并全程相容。一般正则化迹无正性和循环性保障，不能替代普通迹。
5. **定理B。** 对正trace的GNS先商去零理想。\(q^{-1/2}\Phi\) 的左右逆及trace性保证该左作用在此特定元素上有界且酉；这并不自动让整个抽象代数都有有界表示。更重要的是，GNS只见trace可见商，必须另证完整目标谱／重数的行列式识别。有限维cyclic Gram商不能冒充H1的全部普通trace重数。
6. **Deligne量词。** 若估计写作 \(|\alpha|^k\le C_kq^{kw/2+A_k}\)，\(\log C_k=o(k)\) 且 \(A_k=o(k)\) 是便于核验的充分条件；固定C、A当然足够。更一般，合并净误差 \((\log C_k+A_k\log q)/k\) 沿无界允许阶数子列的上极限不大于0即可；不能把分别次线性说成必要条件，因为误差可能抵消。局部张量幂、整体几何族、全局pole预算和对偶同对象性缺一不可。只假设所需均匀极点界是条件接口，不是新来源。
7. **函数域类型。** §4.1的“紧垂直带只有有限个极点”若指实部有界、高度无界，会排除函数域zeta的全部周期端点pole。可改为每个紧集局部有限，另给增长／周期pole预算，或明确连续生成元型与离散Frobenius型两种解析类别。§7.2虽已指出这一差异，前面的统一公理还须相应修改；全周期aliases不能只取一个基本带。

## 4. 附件建议与项目已付内容的去重

| 附件建议 | 项目中最接近的已付资产 | 当前不能重计的内容／尚欠 |
|---|---|---|
| 首个非经典非有限域正迹实例 | 562/563的 \(Z_c=1+c/[s(s-1)]\)、\(1/4\le c\le1/2\)，由全分布ODE和正守恒能量给全源平方和 | 在此范围已有正continuous primitive、规范完成化和全部双pole；不将能量矩阵在更宽参数的正性升级为primitive测度已付，也不重开玩具族作为新路线 |
| 全分布正性判别 | 563的全分布证书、实偶指数阶下heat-CM接口 | CM仍可等价；经典需要独立全源身份／源证书 |
| 正闭形式与ordinary heat trace | 566函数域unitary bundle、完整all-time/all-winding热迹 | 新经典载体、完整原源身份仍欠；不能从GNS matrix coefficient自动得普通重数trace |
| \(A_\Lambda-K_\Lambda\) 紧修正 | 560完整fixed窗表示；570实际signed联合比较 | 已知紧性不付cofinal符号或原费用，不能以更大有限窗代全域 |
| 平方、正trace、primitive交数 | 567的真正RR→Hodge链及continuous±反测试 | 缺同一经典源到实际sections/乘法/有效性/容量的桥，形式对应不付正号 |
| 正系统分布逼近经典 | 576真实FF正锥生成、577完整Gamma修补 | 未标记membership仍承担Weil责任；正型锥在D'闭不提供逼近序列的独立存在性 |
| 增强局部Weil域／Green源 | 581/582已付实际S0强域、full-local费用及额外native Green family | 405全关系仍非principal，fixedcoarse primitive零；增加表示域未付独立primitive容量 |

最强classic实际后果仍须按STATE保留为542+555→557的whole leading4/5负惯性**上界**，不能由上述接口提升为正性或下界。当前source/Green设施有实质内容，但没有闭合同对象primitive容量或actualq/core/coupling/Ξ。

## 5. 对后续选择真正有用的信息

附件贡献主要是把候选分成可比的证明核，而非给出此前缺失的算术输入。现在宜把候选压缩成**一条可被405／537和同域费用否定的源身份**：

* 几何路线须给同一非零primitive载体的实际relative principal／Green cocycle及物理源映射；先消全405关系且保537／全源非根，再接整过滤、截面lift乘法与mixed RR。
* 分析正trace路线只有在提交新的实际正对象、并给完整 \(W_\zeta\) 的同域身份或完整signed余项估计时重新准入；抽象 \(W=\operatorname{Tr}(US)\) 目标不算输入。
* Deligne路线作为备选，先要一个可计算低阶非平凡tensor对象及全局pole定理；当前附件没有，不能据此串入一个unknown族合同。

这两条首选接口仍是独立证明等价命题的合法方式；其“等价”不构成禁止理由，缺少的是独立可执行输入。当前附件未改变根本瓶颈，只增加了归一化核对与任务去重依据。成功重准入需出现实物或足以改变选择的具体比较；失败后应停止该候选，而不是扩大术语。

## 6. 核验与来源边界

以上三处公式修正由附件字面定义直接计算；它们是审读纠错，不是新的RH数学后果。项目消费只据已结算资产的原范围，不宣称重证全部历史。

本次核看原始来源：[Hilberdink–Lapidus](https://arxiv.org/abs/math/0410270)研究适当假设下的解析性质与广义函数方程；其Theorem 3.2要求相应带内有限pole及 \(|\operatorname{Im}s|\to\infty\) 时的一致趋零等具体前件，不能只凭多项式竖向增长就援引，更不能无条件覆盖连续测度推广。[Connes–Consani](https://arxiv.org/abs/2006.13771)明确聚焦单archimedean地方，并讨论Weil分布与Sonin压缩trace之差；[Katz原文](https://web.math.princeton.edu/~nmk/old/DeligneRHOverview.pdf)为Weil/Deligne证明背景。[Milne PDF](https://jmilne.org/math/xnotes/pRH.pdf)使用无www域名已由root本轮成功抓取；函数域完整链仍归项目567及旧原件，不把重复获取记作新定理。上述来源均不能替代经典同源身份；本稿为来源审读0数学轮。
