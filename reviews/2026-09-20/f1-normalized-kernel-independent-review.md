# 399归一化图核：独立周期辅助与全文逆审

2026-09-20。只读代理Einstein，任务标识01a0bd88-a253-7ec3-8ccd-867cd6d60e1e。
主线程保留以下完整汇总；代理未修改文件或提交。这是内部独立复核，不是外部同行评审。
后续主稿中的符号分开：K表示从平方测试函数到基底的算子，P表示第一投影的边缘Markov核；以下原报告沿用其自身记号。

以下汇总已完成的独立报告，供主线程直接归档。**399 §1–6（含新增 (11a)(11b)）及 §7.1 的限定结论通过此次内部逆审；未发现阻断性数学错误。** 周期辅助同时确认：固定层不能下降，高度混合可以真实等变，但一般不保持幂半群。全程只读，未修改文件或提交。

**一、周期、复合与连续 Haar 混合**

沿用已审的完美化环域 \(Y_K\)、实际解析平方 \(Y_K^{(2)}\)、幂映射和高度：
\[
\pi_b^*U^q=U^{bq},\qquad
\phi=\pi_p,\qquad
\Phi=\phi\times\phi,\qquad
h(\pi_bx)=b\,h(x).
\]
其中 \(K\) 完备代数闭，\(b\in\mathbf Z[1/p]_{>0}\)。以下核复合均约定右边先作用。

**相位群及整数层。** 定义
\[
G=\operatorname{Hom}_{\rm Ab}
\bigl(\mathbf Z[1/p],\mu_{p^\infty}(K)\bigr).
\]
给定义域和单位根群离散拓扑，给 \(G\) 逐点收敛拓扑。单位根的离散拓扑也等于其在 \(K\) 中的子空间拓扑：不同 \(p\) 幂单位根的距离至少为
\[
|p|^{1/(p-1)}>0.
\]

对所有整数 \(N\)，定义
\[
T_N=\{\varepsilon\in G:\varepsilon(p^{-N})=1\}.
\]
则
\[
T_{N+1}\subset T_N,\qquad
[T_N:T_{N+1}]=p,\qquad
\bigcup_{N\in\mathbf Z}T_N=G,\qquad
\bigcap_{N\in\mathbf Z}T_N=\{1\}.
\tag{A1}
\]
每个 \(T_N\) 是紧开子群，且
\[
T_N\simeq
\varprojlim_{r\ge0}\mu_{p^r}(K),\qquad
\varepsilon\longmapsto
\bigl(\varepsilon(p^{-N-r})\bigr)_r.
\]
对 \(M\ge N\)，取值于 \(p^{-M}\) 给出
\[
T_N/T_M\simeq\mu_{p^{M-N}}(K).
\tag{A2}
\]

所以 \(G\) 是局部紧群，规范地识别为
\[
G\simeq\mathbf Q_p(1).
\]
选相容本原单位根以后，才得到坐标形式
\[
G\simeq\mathbf Q_p,\qquad T_N\simeq p^N\mathbf Z_p.
\]
**整个 \(G\) 不紧；各 \(T_N\) 才紧。**

负层确实扩大了群：
\[
T_{-r}=\{\varepsilon:\varepsilon(p^r)=1\},
\]
允许 \(\varepsilon(1)\) 是非平凡 \(p^r\) 次单位根。因此不能把负层继续定义为原 \(T_0\) 内的子群。

记 \(H_N\) 为 \(T_N\) 的 Haar 概率测度。第 \(M\ge N\) 层每个柱集质量为 \(p^{-(M-N)}\)。若 \(G\) 上的 Haar 测度归一化为 \(T_0\) 质量 \(1\)，则
\[
d\varepsilon|_{T_N}=p^{-N}H_N.
\tag{A3}
\]
这与有限层根数一致：整数层方程
\[
F_{N,b}=U^{p^{-N}}-V^{bp^{-N}}
\]
在 \(U_M\) 层有 \(p^{M-N}\) 个普通根；每根权 \(p^{-M}\)，总质量为 \(p^{-N}\)。负 \(N\) 时取 \(M\ge\max(0,N)\) 即可。

**幂作用与 \(p\) 分母。** 定义
\[
\alpha_b(\varepsilon)(q)=\varepsilon(bq).
\]
唯一写成
\[
b=mp^{k_b},\qquad p\nmid m,\qquad k_b=v_p(b)\in\mathbf Z.
\]
即使 \(m^{-1}\notin\mathbf Z[1/p]\)，\(\alpha_m\) 仍可逆，因为取 \(m\) 次幂在 \(\mu_{p^\infty}\) 上可逆。直接得到
\[
\boxed{
\alpha_b(T_N)=T_{N+k_b},\qquad
(\alpha_b)_*H_N=H_{N+k_b}.
}
\tag{A4}
\]
特别地，若 \(b=a/p^r\)，必须使用
\[
k_b=v_p(a)-r.
\]
因此 \(p\) 使层深加一，\(p^{-1}\) 使层深减一，与 \(p\) 互素的整数保持层深。

对未归一化测度：
\[
(\alpha_b)_*(p^{-N}H_N)
=p^{k_b}\,p^{-(N+k_b)}H_{N+k_b}.
\tag{A5}
\]
这里的相位倍率不是幂映射的去 \(p\) 部分有限次数 \(m\)。

**实际图核与周期方向。** 相位作用是实际解析自同构
\[
a_\varepsilon^*U^q=\varepsilon(q)U^q,
\]
并满足
\[
\pi_ba_\varepsilon=a_{\alpha_b\varepsilon}\pi_b.
\tag{A6}
\]
边缘概率核为
\[
K_{N,b}(x)=
\int_{T_N}\delta_{a_\varepsilon\pi_bx}\,dH_N(\varepsilon).
\]

同时应保留真实平方中的图核。定义解析映射
\[
j_{\varepsilon,b}:Y_K\longrightarrow Y_K^{(2)},\qquad
j_{\varepsilon,b}^*(U^qV^r)
=\varepsilon(q)W^{bq+r},
\]
以及
\[
\boldsymbol K_{N,b}(x)
=\int_{T_N}\delta_{j_{\varepsilon,b}(x)}\,dH_N(\varepsilon).
\tag{A7}
\]
其第二投影是 \(\delta_x\)，第一投影才是 \(K_{N,b}(x)\)。这里没有把 Berkovich 纤维积点等同于两个边缘点的普通配对。

由解析态射恒等式
\[
\Phi j_{\varepsilon,b}
=j_{\alpha_p\varepsilon,b}\phi
\]
得到
\[
\boxed{
\Phi_*\boldsymbol K_{N,b}(x)
=\boldsymbol K_{N+1,b}(\phi x),\qquad
\phi_*K_{N,b}(x)=K_{N+1,b}(\phi x).
}
\tag{A8}
\]
这与
\[
\Phi^*F_{N,b}=F_{N-1,b}
\]
一致：**方程拉回减一，零纤维向前推加一。**

令 \(\boldsymbol\mu_{N,b}=p^{-N}\boldsymbol K_{N,b}\)，则
\[
\Phi_*\boldsymbol\mu_{N,b}(x)
=p\,\boldsymbol\mu_{N+1,b}(\phi x).
\tag{A9}
\]
乘源高度后倍率抵消：
\[
\Phi_*\bigl(h(x)\boldsymbol\mu_{N,b}(x)\bigr)
=h(\phi x)\boldsymbol\mu_{N+1,b}(\phi x).
\tag{A10}
\]
这些都是条件核公式，没有引入底测度。

**精确复合。** 完整公式是
\[
\boxed{
K_{N,b}K_{M,c}
=K_{\min(N,M+v_p(b)),\,bc}.
}
\tag{A11}
\]
证明是两次独立取相位后，输出相位变为
\[
\varepsilon\,\alpha_b(\delta),
\]
其分布为
\[
H_N*H_{M+v_p(b)}
=H_{\min(N,M+v_p(b))}.
\]
最后一步使用嵌套紧子群 Haar 概率的卷积公式。

真实图对应也可用实际三变量解析图、独立 Haar 积分及首尾投影证明同一公式，而不是仅拼接边缘点。

若使用未归一化核，令 \(L=\min(N,M+v_p(b))\)，则
\[
\mu_{N,b}\mu_{M,c}
=p^{L-N-M}\mu_{L,bc}.
\tag{A12}
\]

对 \(2,3,6\)，两个方向分别为：

| 素数 | \(K_{N,2}K_{M,3}\) | \(K_{M,3}K_{N,2}\) |
|---|---|---|
| \(p\ne2,3\) | \(K_{\min(N,M),6}\) | \(K_{\min(N,M),6}\) |
| \(p=2\) | \(K_{\min(N,M+1),6}\) | \(K_{\min(M,N),6}\) |
| \(p=3\) | \(K_{\min(N,M),6}\) | \(K_{\min(M,N+1),6}\) |

因此同层时，对所有素数均有
\[
K_{N,2}K_{N,3}=K_{N,3}K_{N,2}=K_{N,6}.
\tag{A13}
\]
固定层对正整数幂闭合，但 \(K_{N,1}\) 是平均投影，不是恒等核。

含 \(p\) 分母时：
\[
\boxed{
K_{N,p^{-1}}K_{N,p}=K_{N-1,1},\qquad
K_{N,p}K_{N,p^{-1}}=K_{N,1}.
}
\tag{A14}
\]
若 \(D_b(x)=\delta_{\pi_bx}\) 是确定性幂核，则
\[
D_bK_{N,c}=K_{N+v_p(b),bc},\qquad
K_{N,c}D_b=K_{N,bc}.
\tag{A15}
\]

**固定层不能下降。** 等变下降要求
\[
K_{N,b}(\phi x)=\phi_*K_{N,b}(x),
\]
而右边实际上是 \(K_{N+1,b}(\phi x)\)。在完整几何相位纤维上，
\[
H_N(T_{N+1})=\frac1p,\qquad H_{N+1}(T_{N+1})=1.
\]
两者不同，标量重权或平坦线丛字符不能修复这一支集差异。某些 Gauss 点的边缘相位作用可能不可见，不影响整体不下降的结论。

更强地，高度无关的相位概率若满足
\[
(\alpha_p)_*\lambda=\lambda,
\]
则只能是 \(\delta_1\)：所有 \(\lambda(T_N)\) 相等；向负层取并得该值为 \(1\)，向正层取交便得 \(\lambda(\{1\})=1\)。

**连续高度混合。** 固定 \(h_*>0\)，令
\[
t(x)=\log_p(h(x)/h_*).
\]
对 \(t=n+\theta\)、\(n=\lfloor t\rfloor\)、\(0\le\theta<1\)，置
\[
\lambda_t=(1-\theta)H_n+\theta H_{n+1}.
\tag{A16}
\]
它在整数接缝连续，事实上在总变差范数下连续，并满足
\[
(\alpha_b)_*\lambda_t=\lambda_{t+v_p(b)}.
\tag{A17}
\]
定义
\[
\boldsymbol{\mathcal R}_b(x)
=\int_G\delta_{j_{\varepsilon,b}(x)}\,d\lambda_{t(x)}(\varepsilon).
\tag{A18}
\]
因为 \(t(\phi x)=t(x)+1\)，实际测度恒等式为
\[
\boxed{
\Phi_*\boldsymbol{\mathcal R}_b(x)
=\boldsymbol{\mathcal R}_b(\phi x).
}
\tag{A19}
\]
例如对连续测试函数 \(F\)，左边的积分为
\[
\int F(j_{\alpha_p\varepsilon,b}(\phi x))\,d\lambda_{t(x)}(\varepsilon)
=
\int F(j_{\eta,b}(\phi x))\,d\lambda_{t(x)+1}(\eta),
\]
正是右边。这个论证核对的是实际平方上的概率测度。

因此
\[
\overline{\boldsymbol{\mathcal R}}_b([x])
=(q_\Delta)_*\boldsymbol{\mathcal R}_b(x)
\]
与提升无关，且
\[
(p_2)_*\overline{\boldsymbol{\mathcal R}}_b([x])=\delta_{[x]},
\qquad
\operatorname{supp}\overline{\boldsymbol{\mathcal R}}_b([x])
\subset\{\rho=b\}.
\tag{A20}
\]
没有选择底测度来构造“规范平方总测度”。

连续性由实际相位作用的联合连续性及局部有限混合得到。399 对非负层证明的 Feller 性也延伸到负层，因为
\[
\boldsymbol K_{N,b}(x)
=(\Phi^N)_*\boldsymbol K_{0,b}(\phi^{-N}x).
\]
其原 \(C\) 上版本再由 399 §4 下降。

整数负层不能省略：若整个周期覆盖上的相位概率都支撑在 \(T_0\)，又要求周期等变，则其支撑必须同时落在所有 \(T_r\)，最终只能得到 \(\delta_1\)。

**混合的复合边界。** 记 \(t=t(x)\)，则边缘混合核满足
\[
\boxed{
(\mathcal R_b\mathcal R_c)(x)
=
\int_G\delta_{a_\varepsilon\pi_{bc}x}\,
d\bigl(\lambda_{t+\log_pc}*\lambda_{t+v_p(b)}\bigr)(\varepsilon).
}
\tag{A21}
\]
第一个移位来自中间点高度，第二个来自外层幂对相位的作用，不能混同。

等价地，置 \(w_N(t)=\max(1-|t-N|,0)\)，有
\[
(\mathcal R_b\mathcal R_c)(x)
=
\sum_{N,M}w_N(t+\log_pc)w_M(t)
K_{\min(N,M+v_p(b)),bc}(x).
\tag{A22}
\]
这里只是有限和。

混合一般不保持半群。甚至
\[
\lambda_{n+\theta}*\lambda_{n+\theta}
=(1-\theta^2)H_n+\theta^2H_{n+1}
\ne\lambda_{n+\theta}\quad(0<\theta<1).
\tag{A23}
\]
对 \(2,3\)，两个次序分别使用
\[
\lambda_{t+\log_p3}*\lambda_{t+v_p(2)},\qquad
\lambda_{t+\log_p2}*\lambda_{t+v_p(3)},
\]
而 \(\mathcal R_6\) 使用 \(\lambda_t\)。例如：

- \(p=2,t=0\)：两个复合分别使用 \(H_1,H_0\)。
- \(p=3,t=0\)：分别使用 \(H_0,\lambda_{\log_3 2}\)。
- \(p>3\)，取 \(0<t=\theta<1-\log_p3\)：两个复合中 \(H_1\) 的系数分别为 \(\theta(\theta+\log_p3)\)、\(\theta(\theta+\log_p2)\)，而直接核的系数为 \(\theta\)。

选择依赖如下：

- \(G,T_N,H_N,\alpha_b\) 不依赖本原单位根坐标，也不依赖 \(b=a/p^r\) 的表示。
- 相容扩域与 Galois 作用保持这些群和 Haar 测度。
- 中心是实际幂图 \(\pi_b\)，不是任意选取的根；任意改变中心相位不一定保持核。
- 高度参考值 \(h_*\)、采用源高度、插值权重是实质选择。可以改用其他连续非负局部有限权重，只要
  \[
  \sum_Nw_N(t)=1,\qquad w_N(t+1)=w_{N-1}(t),
  \]
  仍然等变，但一般得到不同核。

新增的是实际可下降的连续概率对应。它没有新增 Cartier 性、全局主等价、算术双次数、交叉或 \(\tau\)，也没有恢复严格幂半群。

**二、399 §1–6 的独立逆审**

审核对象是 [399](../../notes/399-f1-normalized-cartier-kernels-and-principal-topology.md) 含新增 (11a)(11b) 的版本。以下结论均限于文中明确指定的空间、核与主子空间。

**§1–2：全部 Berkovich 基点的纤维与质量——通过。**

对任意基点 \(x\) 和位于其上的平方点 \(z\)，有规范等距嵌入
\[
\mathcal H(x)\hookrightarrow\mathcal H(z).
\]
由于 \(K\subset\mathcal H(x)\)，有限层多项式已在 \(\mathcal H(x)\) 内分裂：
\[
U_M^{p^{M-N}}-w_N
=\prod_{\zeta\in\mu_{p^{M-N}}}(U_M-\zeta w_M).
\]
在域 \(\mathcal H(z)\) 中，\(U_M\) 必等于其中一个根。各层的相容选择恰为 \(T_N\)。

所有 Laurent 单项式的值由这些选择和基点半范数决定；稠密性与有界完成再唯一确定整个平方点。因此没有遗漏非经典基点上的额外秩一零分支。

不同相位由
\[
U^q-\varepsilon(q)V^{bq}
\]
区分，紧性及 Hausdorff 性给出实际零纤维与 \(T_N\) 的同胚。这里确实没有要求 \(x\) 为 \(K\) 有理点。

第 \(M\) 层的 \(p^{M-N}\) 个简单根各赋质量 \(p^{-M}\)，故
\[
\mu_{F_N,x}=p^{-N}\kappa_{N,b}(x).
\]
层间柱集相容、扩域相容及 Galois 相容均正确。

**§3：Feller 与紧基底一致弱收敛——通过。**

有限 Laurent 多项式只读有限个相位坐标。共同紧环域上的一致逼近给
\[
T_0\times B_I\longrightarrow Q_I,\qquad
(\varepsilon,x)\longmapsto j_b(\varepsilon,x)
\]
连续。

因此
\[
K_{N,b}:C(Q_I)\to C(B_I)
\]
是正、保常数、范数 \(1\) 的算子。对固定测试函数 \(F\)，在紧集 \(\{1\}\times B_I\) 上取有限乘积邻域覆盖，得到对全部 \(x\) 统一的相位邻域，从而
\[
\|K_{N,b}F-G_bF\|_\infty\to0.
\]
证明不需要基底可度量，也没有把点态收敛误当成一致收敛。

未归一化核的算子范数为 \(p^{-N}\)，归一化核则按强算子拓扑趋于图核；两种陈述相容。

**§4：有限 Galois 谱纤维、完备逆极限及原 \(C\) 下降——通过。**

关键连接处均可成立：

1. 对有限 Galois 扩张 \(L/C\)，有限维标量扩张 \(R_L=R\otimes_C L\) 已完备，其拓扑与相应加权 \(c_0\) 系数拓扑等价。

2. 点 \(x\in M(R)\) 上的谱纤维对应
   \[
   \mathcal H(x)\otimes_C L=\prod_iE_i
   \]
   的有限域因子及各自唯一延拓范数。有限维范数等价保证得到的半范数在 \(R_L\) 上有界；反向由剩余域嵌入恢复该因子。因此没有遗漏谱点，也不需要 Noetherian 假设。

3. Galois 群在因子上可迁。否则一个轨道的原始幂等元之和会在
   \[
   (\mathcal H(x)\otimes_C L)^{\operatorname{Gal}(L/C)}
   =\mathcal H(x)
   \]
   中产生非平凡幂等元，矛盾。唯一延拓范数保证代数因子的搬移同时搬移谱点。

4. 完备逆极限步骤不存在不统一的有界常数问题。每个谱半范数自动满足
   \[
   |f|_{x_L}\le\|f\|_{R_L}.
   \]
   即使先只知道带常数的有界性，对 \(f^n\) 应用后取 \(n\) 次根也得到此式。于是相容半范数在保范数稠密并上统一受控，唯一延拓到 \(R_K\)。

5. 有限交性质给相容提升；对两个提升，有限层可迁性及绝对 Galois 群紧性给一个同时搬移所有层的元素。因此限制映射满射，纤维恰为 Galois 轨道，确是紧 Hausdorff 商映射。

故 §4.2 的定义
\[
\kappa^C_{N,b}(x_C)
=r_{\rm square*}\kappa_{N,b}(x_K)
\]
与提升无关。连续测试积分通过商映射下降，Feller 性和紧基底一致收敛均随之下降。这不是单靠一句“Galois 相容”跳过构造。

外部输入的来源状态准确：归档讲义 Thm 4 陈述有限维范数等价，Thm 6 陈述有限扩张绝对值的存在唯一性；该处只证明唯一性，存在性作为标准 [R] 输入。已核对相关完整页面：[归档讲义](../../literature/background/kedlaya-absolute-values-2007.pdf)。

**§5：总变差及算子范数恰为 \(2\)——通过。**

在 \(K\) 上，零纤维同胚与 Haar 无原子性给
\[
\kappa_{N,b}(x)(\{\gamma_b(x)\})=0.
\]
下降到 \(C\) 后，非单位相位仍被某个 \(C\) 系数方程 \(F_M\) 检出，不可能映到完整图点。因此图点质量仍为零，并有
\[
\|\kappa_{N,b}(x)-\delta_{\gamma_b(x)}\|_{\rm TV}=2.
\]

新增的统一测试函数计算也完全正确。对 \(M\ge\max(1,N)\)，
\[
|F_M(j_b(\varepsilon,x))|
=|\varepsilon(p^{-M})-1|e^{-bh(x)/p^M}.
\]
在 \(T_M\) 上为零；在 \(T_N\setminus T_M\) 上至少为
\[
d_Me^{-bA/p^M}=\delta_M.
\]
因此
\[
B_M=\max(0,1-|F_M|/\delta_M)
\]
是整个 \(C\) 平方上的连续函数，在指定相位纤维上恰为 \(1_{T_M}\)。于是对全部基点同时有
\[
K_{N,b}B_M=p^{N-M},\qquad
M_{N,b}B_M=p^{-M},\qquad
G_bB_M=1.
\tag{B1}
\]
用 \(2B_M-1\) 测试得到
\[
\|K_{N,b}-G_b\|_{\rm op}
\ge2(1-p^{N-M})\longrightarrow2.
\]
结合上界 \(2\)，即得等号。它在 \(C\) 下降版本同样成立，不依赖下降后的全局无原子性。

这里没有收敛量词冲突：强收敛固定测试函数再令 \(N\to\infty\)；范数下界允许测试函数随层变化。

**§6：强闭包、代数不包含及算子范数距离 \(1\)——通过。**

固定
\[
V_I=\mathcal L(C(Q_I,\mathbf R),C(B_I,\mathbf R)),\qquad
P_I=\operatorname{span}_{\mathbf R}\{M_{N,b}:N\ge0\}.
\]
因为
\[
K_{N,b}=p^NM_{N,b}\in P_I
\]
且强收敛到 \(G_b\)，所以
\[
G_b\in\overline{P_I}^{\,\rm strong}.
\tag{B2}
\]

另一方面，对任意固定有限和
\[
T=\sum_{N\le N_0}c_NM_{N,b},
\]
由 (B1) 得
\[
TB_M=p^{-M}\sum c_N\to0,\qquad G_bB_M=1.
\]
所以 \(G_b\notin P_I\)，并且
\[
\|G_b-T\|_{\rm op}\ge1.
\]
取 \(T=0\) 给反向界，故
\[
\boxed{
\operatorname{dist}_{\rm op}(G_b,P_I)
=\operatorname{dist}_{\rm op}(G_b,\overline{P_I}^{\,\rm op})
=1.
}
\tag{B3}
\]
图类在这个指定的算子范数闭商中确定非零，且商范数为 \(1\)。

若强连续线性映射 \(\tau:V_I\to E\) 的目标 Hausdorff，并杀掉全部 \(M_{N,b}\)，则必有
\[
\tau(G_b)=0.
\]
这个结论来自明确的强收敛序列，不是把图类为零写进定义。

排除范围也正确：这里检验的是明确的覆盖／局部主核模型，不是已经建立的全局 Chow 群，也不排除仅使用真正下降的全局主关系并保留过渡数据的理论。

**三、§7.1 快审及应保留的修订说明**

§7.1 的引理也通过：紧 Hausdorff 空间间互有 Feller 概率核逆的两核，必来自互逆同胚。

固定 \(x\)，取 \(y\in\operatorname{supp}P_x\)。对每个连续 \(f\ge0\)、\(f(x)=0\)，
\[
\int Q_y(f)\,dP_x(y)=0.
\]
被积函数连续非负，故在整个支撑上为零，不涉及不可数满测度集的交。对任意 \(g\in C(X,\mathbf R)\)，取 \(f=|g-g(x)|\)，得到 \(Q_y=\delta_x\)。另一复合恒等式给
\[
P_x=(P\circ Q)_y=\delta_y.
\]
Feller 性给点映射连续，双侧恒等式给互逆。证明不要求可度量。

因此严格保 Dirac 单位及 \(p,1/p\) 的两侧逆，迫使作为概率核的 \(p\) 箭头确定性。该限制不排除近似核，也不单凭边缘核的确定性排除额外平方关系或几何字段。

需要在归档时明确的修订与边界如下；**其中没有推翻 §1–6 主结论的阻断性修订**：

- 负层必须在完整 \(G\) 中定义，不能仍限制在原 \(T_0\) 内。
- 周期必须区分方程拉回减层与测度向前推加层；复合必须加入外层 \(v_p(b)\)，包括其负值。
- 实际平方点应由解析图态射定义，不能仅凭两个 Berkovich 边缘点的标签定义。
- §4 完备化可补明“谱半范数自动收缩”的一句证明，以显式展示跨层统一有界性；现有论证可以补全，无阻断缺口。
- §6 的“有限组合无原子”在当前 \(K\) 版本正确。延伸到 \(C\) 时使用图点质量为零或 (11b)，不能仅从推前推出无原子。
- §6“图类可非零”应精确写为：在已指定的算子范数闭主商中，图类非零且范数恰为 \(1\)。
- 高度混合不自动属于 \(P_I\)：它带有随底点变化的连续系数，而 \(P_I\) 只是实线性张成。除非另证主子空间对这些乘法封闭，不能直接把该混合判为主核。不过既有事实 \(G_b\in\overline{P_I}^{\,\rm strong}\) 不因此改变。
- 高度混合的真实等变性不等于严格幂半群；其复合必须使用 (A21)，不得沿用固定层的 \(2,3,6\) 同层公式。

这些结论完成了本次有限辅助与限定逆审，没有构造或证明 RH、循环 \(\tau\)、全局交叉或长期目标接口。
