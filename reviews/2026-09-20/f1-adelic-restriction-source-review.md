# 405：独立来源审计

2026-09-20。只读代理Lorentz（01a0bed7-5a42-7cd1-9eae-ed17da799136）。
以下保留首次来源审计返回的内容；它记录当时尚未核验的正规化桥。主线程随后补证及独立数学逆审另行结算。

可以确认：**2007 年原文支持限制映射、原始像上的全混合迹消失，以及不以 RH 为假设的 global nuclear trace formula；它没有把该像识别为真正的 principal divisors。此次也没有认证全测试类上的 \(L(k)=2N(k)\)，该正规化比较须保留开放。**

核验原件：:codex-file-citation{path="H:/codex-build/RH/RH-Weil/literature/f1/ccm-weil-adeles-math-0703392v1.pdf" purpose="source"}。PDF 确为 61 页，SHA256 与给定值完全一致。以下页码均为 PDF 页码，与印刷页码一致。

**(a) 对象、限制映射及闭包的实际范围。**

PDF16–17，(4.1)–(4.6)：对象是作用群胚
\[
G_K=K^\times\ltimes\mathbb A_K,\qquad
s(k,x)=x,\quad r(k,x)=kx,
\]
\[
(k,x)\circ(k',y)=(kk',y)\quad(x=k'y).
\]
代数为 \(C_0(\mathbb A_K)\rtimes K^\times\)，其光滑子代数
\[
S(G_K)=S(\mathbb A_K)\rtimes K^\times
\]
使用有限和 \(\sum_k f_kU_k\)。不能直接替换成商空间上的普通函数代数。

PDF17，(4.8)–(4.10)：
\[
\epsilon_0\!\left(\sum_k f_kU_k\right)=f_1(0),\qquad
\epsilon_1\!\left(\sum_k f_kU_k\right)=\int_{\mathbb A_K}f_1(x)\,dx,
\]
\[
S(G_K)^\natural_0
=\ker\epsilon_0^\natural\cap\ker\epsilon_1^\natural,\qquad
\epsilon_j^\natural(a_0\otimes\cdots\otimes a_n)
=\epsilon_j(a_0\cdots a_n).
\]
这是 **cyclic module 的核交**；原文还说明非含幺代数通过添单位构造 cyclic module。

PDF18–21，(4.12)、(4.16)、Definition4.9–4.10：
\[
\rho(f)=f|_{\mathbb A_K^\times},\qquad
\rho:S(G_K)\longrightarrow C(C_K,\mathcal L^1(H_x)),
\quad H_x=\ell^2(p^{-1}(x)).
\]
idele 拓扑按 \(g\mapsto(g,g^{-1})\) 定义。一般 \(K\) 下 Hilbert 场不能自然平凡化；PDF19 明确要求保留算子值目标与 \(C(C_K)\) 的区别。\(K=\mathbb Q\) 才使用
\(\Delta_{\mathbb Q}=\widehat{\mathbb Z}^{\,\times}\times\mathbb R_+^\times\)
作自然截面。

为区分原文两种 Schwartz 记号，以下将 (4.20) 的较强空间记为
\[
\mathscr S(C_K)=\bigcap_{\beta\in\mathbb R}|\cdot|^\beta S(C_K).
\]
函数域情形采用紧支撑 Schwartz 函数。目标 cyclic submodule 要求：**主对角线限制的 cyclic trace 属于 \(\mathscr S(C_K)\)**，不只是任意连续截面。

PDF20、23，(4.25)、Definition4.14：
\[
S(\mathbb A_K)_0
=\{\xi\in S(\mathbb A_K):\xi(0)=0,\ \int_{\mathbb A_K}\xi=0\},
\]
\[
\mathcal V
=\operatorname{Ran}(\operatorname{Tr}\rho)
=\left\{\Sigma\xi:x\mapsto\sum_{k\in K^\times}\xi(kx),\
\xi\in S(\mathbb A_K)_0\right\}
\subset\mathscr S(C_K).
\]
这里没有 \(|x|^{1/2}\) 因子；1999 的 \(E\) 与此不同，见 PDF15 的 (3.11)。

PDF21 明确规定 cyclic cokernel 要除以**像的闭包**：
\[
\mathcal H^1
=\operatorname{coker}\!\left(
\rho^\natural:S(G_K)^\natural_0
\to\mathscr S^\natural(C_K,\mathcal L^1(H_x))\right),
\qquad
H^1=\operatorname{Tor}(\mathbb C^\natural,\mathcal H^1).
\]
但这些页**没有逐级展开闭包所用的半范数、张量完成等完整拓扑细节**。因此可以确认“取闭像商”的规定，不能据此把它认作仓库任意 \(L^2\)、一致或分布拓扑下的闭包。

**(b) vanishing、closure、sharp 与混合测试。**

PDF24–25，Lemma4.15、Lemma4.17 的实际证明是
\[
\vartheta_m(f)\xi=f\star\xi,\qquad
\mathcal V\star\mathscr S(C_K)\subseteq\mathcal V,
\]
所以
\[
r\in\mathcal V
\ \Longrightarrow\
\vartheta_m(r)|_{H^1}=0. \tag{4.46}
\]
PDF29，Proposition6.4 的证明明确写到
\[
\langle r,h\rangle
:=\operatorname{Tr}\bigl(\vartheta_m(r\star h)|_{H^1}\bigr)=0,
\qquad r\in\mathcal V,\quad h\in\mathscr S(C_K).
\]
**这已经覆盖所有该测试空间内的混合测试，不只覆盖 \(h=r^\sharp\)。** 卷积交换性也给出另一槽的消失。它证明的是 radical 的包含关系，未证明 \(\mathcal V\) 就是全部 radical。

闭包版本需要明确区分“原文陈述”和“连续性推论”：若在上述测试空间拓扑中卷积连续，令
\(J=\overline{\mathcal V}^{\,\mathscr S}\)，则
\[
J\star\mathscr S\subseteq J,
\]
故 \(J\) 在闭像商上的卷积作用仍为零，混合迹消失随之成立。这不需要凭空假设“核迹对任意弱收敛连续”，但**不能推广到未经指定的其他闭包**。

视觉核对 PDF28 后，(6.6)、(6.9) 的正确公式包含共轭：
\[
f^*(g)=\overline{f(g^{-1})},\qquad
f^\sharp(g)=|g|^{-1}\overline{f(g^{-1})}.
\]
JSON 抽取漏掉了横线。所核 Lemma4.17/Prop6.4 **没有单独证明**
\(\mathcal V^\sharp=\mathcal V\)。可以作如下标准补证，但应标成补证而非该引理原句：选全局字符及自对偶 Haar 测度，由 adelic Poisson 公式和两项消失条件，
\[
\Sigma\xi(x)=|x|^{-1}\Sigma\widehat\xi(x^{-1}),\qquad
(\Sigma\xi)^\sharp=\Sigma(\overline{\widehat\xi})\in\mathcal V.
\]
再用 \(\sharp\) 的连续性可得 \(J^\sharp=J\)。在这些条件下，加入 \(r\in J\) 后，自配对的两个混合项均消失。

另须保留 PDF29，Prop6.4(2) 的拓扑边界：
\[
(f+r)\star(f+r)^\sharp(1)
=\int_{C_K}|f(g)+r(g)|^2|g|\,d^*g<\varepsilon
\]
依赖 [10] Appendix I 中 \(\delta=0\) 的满射性。**这个加权 Hilbert 范数逼近，不意味着 \(\mathcal V\) 在 \(\mathscr S\) 中稠密。**

**(c) Theorem6.1 的无 RH 性质及依赖。**

PDF28，Theorem6.1：
\[
T(f):=\operatorname{Tr}(\vartheta_m(f)|_{H^1})
=\widehat f(0)+\widehat f(1)
-(\log|a|)f(1)
-\sum_v I_{v,e_{K_v}}(f), \tag{6.3}
\]
\[
I_{v,\beta}(f)
=\int_{(K_v^\times,\beta)}'
\frac{f(u^{-1})}{|1-u|}\,d^*u.
\]

该页明确说明使用 [32] 的 **nuclear spaces** 版本，并通过 [11] 作上同调表述；它区别于 [10] 的 semi-local Hilbert-space 版本。PDF23、25 又明确说所有零点——包括可能不在临界线上的零点——都按自然重数出现。PDF24 的归一化关系为
\[
\vartheta_m(\gamma)=|\gamma|^{1/2}W(\gamma). \tag{4.41}
\]

因此，**该文将 (6.3) 作为无 RH 假设的定理使用**。RH 等价条件另在 PDF29，Corollary6.3：
\[
T(f\star f^\sharp)\ge0
\quad\forall f\in\mathscr S(C_K).
\]
不能把这个迹恒等式与 1999 特殊 Hilbert 截断下的 RH 等价命题混为一谈。

依赖定位已核：

- PDF60，[10]：Connes，1999，*Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*。
- PDF60，[11]：Connes–Consani–Marcolli，*Noncommutative geometry and motives: the thermodynamics of endomotives*，math.QA/0512138。
- PDF61，[32]：Meyer，*On a representation of the idele class group related to primes and zeros of L-functions*，Duke Math. J. 127 (2005), 519–595。

本次认证的是 **2007 原文的定理陈述及其依赖边界**，没有独立重验 [11]/[32] 的完整解析证明。

对仓库迁移尤其重要的是：若将全局字符正规化的局部总和记为 \(L_\alpha\)，则 (6.4) 给出
\[
T(f)=\widehat f(0)+\widehat f(1)-L_\alpha(f).
\]
因此
\[
L_\alpha(r\star h)
=\widehat r(0)\widehat h(0)+\widehat r(1)\widehat h(1),
\qquad r\in\mathcal V.
\]
**迹 radical 并不自动是局部项 \(L_\alpha\) 的 annihilator。**
这也准确指出额外两个 Mellin 矩条件的作用，而不涉及其子空间构造。

**(d) trivial correspondences 与 principal divisors。**

PDF30，(7.1)–(7.3) 将
\[
Z(f)=\int_{C_K}f(g)Z_g\,d^*g
\]
的 degree/codegree 对应到 \(\widehat f(1)\)、\(\widehat f(0)\)。PDF32 明确把来自 \(\mathcal V\) 的 \(Z(f)\) 视为 **trivial correspondences 的类比**，用来调整 degree。

PDF32–33 的 Fubini 讨论说明：
\[
\int_{\mathbb A_K}\xi=0
\quad\not\Rightarrow\quad
\widehat{\Sigma\xi}(1)=0.
\]
Lemma7.3 宣称 degree 可任意调整；所列证明明确“只处理 \(K=\mathbb Q\)”，而其 Mellin 表达还带有 “up to normalization”。本次未重复该 Gaussian 计算。

PDF33 紧接着把
> “identify the correct notion of principal divisors”

列为继续模拟 Weil 证明所需的重要问题。**这里确实尚未识别真正的 principal divisors；不能把 \(\mathcal V\)、其闭包或其中的矩零部分直接命名为已经建立的 principal-divisor 关系。**

另有复数约定边界：PDF30–31 的 (7.3)、(7.8) 未完整显示反线性 sharp 所需的共轭修正，不能原样当作任意复系数测试的代数恒等式；实值情形没有这一问题。

**(e) 追加的固定主值与 \(\delta_0\) 比较：本次未认证。**

已准确定位并视觉核对 PDF9，Definition2.1、(2.33)–(2.34)：\(\varrho_\beta\) 延拓局部 \(d^*u\)，其正规化由
\[
\widehat{\varrho_\beta}(1)=0
\]
固定，并规定
\[
I_{v,\beta}(f)=\langle\varrho_\beta,g\rangle,\qquad
g(\lambda)=\frac{f((\lambda+1)^{-1})}{|\lambda+1|}.
\]
该处直接讨论紧支撑测试；全 \(\mathscr S\) 类的公式在 Theorem6.1 中通过上游结果使用。

PDF27 固定 \(e_{\mathbb R}(x)=e^{-2\pi ix}\)；PDF28 的 (6.5) 明写正规化变化：
\[
I_{v,\alpha_v}(f)
=(\log|a_v|)f(1)+I_{v,e_{K_v}}(f).
\]
这正是必须追踪单位元支撑项的来源。换成对数坐标，它对应 \(\delta_0\) 项；**sharp 不变本身不能排除这样的项**。

本次没有核读 CC2015 PDF16(14) 的 \(\kappa\) 正规化，也没有核读 1999 Appendix II 或 [11]/[32] 中计算实位常数的原页。因此，尚不能认证题给
\[
N(k)=\sum_n\Lambda(n)k(\log n)
+\int_0^\infty\frac{e^{2x}k(x)-k(0)}{e^{2x}-1}\,dx
+\frac{\log\pi+\gamma}{2}k(0)
\]
与 2007 固定主值满足全测试类上的 \(L(k)=2N(k)\)。**404 的离开 \(0\) 比较不能在本次审计后自动升级；\(\delta_0\) 系数比较仍开放。** 复值测试还须对齐上面的反线性 sharp 约定。

实际核读范围：完整文本核读 PDF17–25、27–33；补读同一原件 PDF8–10、15–16、59–61。视觉核对 PDF9、20、21、24、25、28–33；全文关键词检索只用于定位，不计作其他章节通读。全部渲染在内存中完成；未写文件、未操作 Git、未联网发送，未重做 Gaussian、Mellin 精确常数或双矩零子空间构造。

## 后续正规化闭环

首次来源审计准确保留了当时尚未核读的δ_0常数问题。
主线程随后核读Connes1999固定原件PDF69–74、76–78，整页视觉检查74；
由(36)的log(2π)+γ有限部分直接得到sharp不变实测试的L_∞=2A+(logπ+γ)k(0)，
有限位单位壳按指定正规化为零。405 §3.1记录完整切变量与极限。
Lorentz另行独立核算该新增推导、半因子及测试类延拓，见[数学逆审](f1-adelic-restriction-mathematical-review.md)。
因此指定主值下的L=2N比较现已闭环；本原始来源报告仍保留其初次核查范围。
