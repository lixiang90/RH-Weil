# 405：独立数学逆审与异议处理

2026-09-20。只读代理Lorentz（01a0bed7-5a42-7cd1-9eae-ed17da799136）。

**核心数学构造通过逆审。新增 §3.1 的有限部分计算正确，确实消除了原先未认证的 \(\delta_0\) 常数差。** 在采用你已核对的原始主值、有限位正规化和紧支显式公式后，式 (6) 及依赖它的结论通过；仍需收紧 cyclic 商的拓扑标识，并补明式 (14) 的反向映射与分裂类别。

核读版本为 289 行，SHA256：
`1a4b97f3844a61cde0d14d8dca6e45c9e4cca76d01f7f8b5e09b256592a8aec8`。

1. **§3.1：系数、有限部分与延拓均成立，但须明确 sharp 子空间。**

   令 \(k_0=k(0)\)，
   \[
   F_\pm(x)=\frac{k(x)}{1\mp e^{-x}},\quad
   a_\varepsilon=-\log(1-\varepsilon),\quad
   b_\varepsilon=\log(1+\varepsilon).
   \]
   正 \(u\) 的两侧分别给出
   \(\frac12\int_{a_\varepsilon}^\infty F_+\)、
   \(\frac12\int_{b_\varepsilon}^\infty F_+\)；负 \(u\) 的两部分合为
   \(\int_0^\infty F_-\)。三个系数正确。

   因为 \(a_\varepsilon,b_\varepsilon=\varepsilon+O(\varepsilon^2)\)、
   \(F_+(x)=O(x^{-1})\)、\(F_-(x)=O(1)\)，把下限统一为 \(\varepsilon\) 的误差为 \(O(\varepsilon)\)。利用
   \[
   F_+(x)+F_-(x)=\frac{2k(x)}{1-e^{-2x}},
   \]
   截断积分 \(J_\varepsilon\) 满足
   \[
   J_\varepsilon+\log\varepsilon\,k_0
   =2A(k)+k_0\log\frac{\varepsilon}{1-e^{-2\varepsilon}}
     +o(1)
   \longrightarrow2A(k)-(\log2)k_0.
   \]
   因而
   \[
   L_\infty(k)=2A(k)+(\log\pi+\gamma)k_0.
   \]
   **这里没有遗漏 \(1/2\)、符号或额外常数。**

   给定单位壳正规化为零，其余有限位壳确实配成
   \[
   L_p(k)=\log p\sum_{m\ge1}
   \bigl[k(m\log p)+p^{-m}k(-m\log p)\bigr]
   =2\log p\sum_{m\ge1}k(m\log p).
   \]
   \(S_{\exp}\) 的衰减保证对所有素数、幂次绝对求和。结合 \(\mathbb Q\) 的 different 因子，得到指定正规化下的 \(L(k)=2N(k)\)。

   [第159行](H:/codex-build/RH/RH-Weil/notes/405-f1-adelic-restriction-moments-and-radical.md:159) 建议改成：
   > 对满足 \(k^\sharp=k\) 的实 \(k\in S_{\exp}\)，取固定偶函数 \(\chi\in C_c^\infty\)，在 \([-1,1]\) 上等于一，令 \(\chi_R(x)=\chi(x/R)\)。

   这样既保留 sharp，也有
   \[
   p_{N,j}((1-\chi_R)k)
   \le C_j e^{-R}\sum_{\ell\le j}p_{N+1,\ell}(k).
   \]
   还应补明**线性**零点和的连续性：
   \[
   |M_k(\sigma+it)|
   \le C_j(1+|t|)^{-j}
      \sum_{\ell\le j}p_{2,\ell}(k),
   \qquad0\le\sigma\le1.
   \]
   取 \(j=2\)，结合零点计数即足够，不用 RH。

   \(L=2N\) 的适用范围是 sharp 不变子空间；由于 \(k_{f,g}^\sharp=k_{f,g}\)，这足以证明式 (6) 对**任意实 \(f,g\in S_{\exp}\)** 成立。第161行“等式延至 \(S_{\exp}\)”宜按此区分量词。

2. **§2：径向源像、Fréchet 空间和理想构造正确；CCM 拓扑标识仍不可直接认证。**

   给定半范数确实定义完备、可度量的局部凸空间；它与径向的全指数加权 Schwartz 条件一致。Poisson 公式控制负半轴，普通 Schwartz 估计控制正半轴，足以证明 \(E:S_{\mathrm{even},0}\to S_{\exp}\) 连续。

   理想证明可以用以下明确估计补实：
   \[
   q_{a,b}(\eta_g)
   \le q_{a,b}(\eta)
      \int_{\mathbb R}|g(t)|e^{(a-b)t}\,dt,
   \quad q_{a,b}(\eta)=\sup_r|r^a\eta^{(b)}(r)|.
   \]
   两个源条件也保持，因为
   \[
   \eta_g(0)=\eta(0)\int g,\qquad
   \int\eta_g=\left(\int e^tg(t)\,dt\right)\int\eta.
   \]
   所需绝对可积界成立，故此次换序合法。\(J\) 是理想，\(I\) 是闭、sharp 不变理想。

   有限 adele 的径向化描述也正确。建议补一句：若平均后的总源为
   \(\sum_i1_{a_i\widehat{\mathbb Z}}\otimes\eta_i\)，应合并为
   \[
   \eta_*=\sum_i\eta_{i,\mathrm{even}}(a_i\,\cdot).
   \]
   **总源**的两项消失条件给出 \(\eta_*\in S_{\mathrm{even},0}\)，不要求每个张量项分别满足它们。

   [第75行](H:/codex-build/RH/RH-Weil/notes/405-f1-adelic-restriction-moments-and-radical.md:75) 仍建议收紧为：
   > 本稿独立定义分离径向来源商 \(S_{\exp}/I\)。将它进一步识别为 CCM 的径向 cyclic/cohomological 商，还需证明目标拓扑及平均、trace/Morita、闭像操作之间的比较相容性。

   当前径向解析构造不能补上原来源没有明确展开的 cyclic 拓扑。

3. **§4–5：Gaussian 常数、严格正性和非零双矩零元素全部通过。**

   独立复算得到
   \[
   \widehat\eta=\eta,\qquad
   \int_0^\infty\eta(r)r^{s-1}\,dr
   =\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2),
   \]
   因而
   \[
   M_h(s)=\frac{s(s-1)}4\Lambda_{\mathbb Q}(s),\quad
   c(h)=d(h)=\frac14,\quad M_h(2)=\frac{\pi}{12}.
   \]
   对 \(\lambda\ge1\)，每个 \(\eta(n\lambda)>0\)；另一半轴由 Poisson 对称得到。因此 \(h(x)>0\) 对所有实 \(x\) 成立，非紧支结论正确。

   写 \(A=r\partial_r\)、\(z=\pi r^2\)，复算为
   \[
   A\eta=(-2z^3+7z^2-3z)e^{-z},
   \]
   \[
   (A^2+A)\eta=(4z^4-28z^3+41z^2-9z)e^{-z}.
   \]
   Euler 算子保持源条件，且与 \(E\) 的微分交换合法，所以 \(p=E\eta_0\in J\)。分部积分给
   \[
   M_p(s)=s(s-1)M_h(s),\qquad
   c(p)=d(p)=0,\qquad M_p(2)=\frac{\pi}{6}\ne0.
   \]
   非零性没有借用式 (6)。

   新增正规化桥通过后，式 (9) 的
   \[
   B(h,g)=\frac{d(g)+c(g)}8,\qquad B(h,h)=\frac1{16}
   \]
   以及 \(B(p,g)=0\) 都成立。

4. **式 (13) 精确成立，但“谱核”应避免扩大含义。**

   \(w=E(\eta(\cdot/2))\in J\)，所以 \(u_d,u_c\) 确属真实源像，双矩分别为 \((1,0)\)、\((0,1)\)。对 \(r\in I\)，
   \[
   B(r,u_d)=c(r)/2,\qquad B(r,u_c)=d(r)/2,
   \]
   足以证明
   \[
   I\cap\operatorname{rad}(B)=I\cap\ker d\cap\ker c.
   \]
   [第235行](H:/codex-build/RH/RH-Weil/notes/405-f1-adelic-restriction-moments-and-radical.md:235) 的“反向由(5)立即成立”应改为“反向由 **(5)与(6)** 成立”。

   本稿证明的是 \(I\subseteq\operatorname{rad}(T)\)，没有证明两者相等。因此第278行“谱核内”最好写成“**已构造的谱消失闭理想 \(I\) 内**”。这不影响式 (13) 本身。

5. **式 (14) 的三种同构成立；反向证明应补全，内部直和须限定类别。**

   令
   \[
   Qf=f-d(f)u_d-c(f)u_c.
   \]
   [第248行](H:/codex-build/RH/RH-Weil/notes/405-f1-adelic-restriction-moments-and-radical.md:248) 缺少的关键一句是：
   \[
   Q(I)\subseteq P_{\rm an}.
   \]
   因而 \(q_PQ\) 连续下降为
   \[
   \bar Q:S_{\exp}/I\longrightarrow S_{\exp}/P_{\rm an}.
   \]
   连续反向应明确写成
   \[
   (a,b,[f]_I)\longmapsto
   [Qf+a u_d+b u_c]_{P_{\rm an}}.
   \]
   这充分证明拓扑同构，**没有构造或假定**
   \(S_{\exp}/I\to S_{\exp}\) 的连续截面。

   \(d,c\) 都是卷积代数的角色，所以式 (14) 也是代数同构。不过
   \[
   I=P_{\rm an}\oplus\mathbb Ru_d\oplus\mathbb Ru_c
   \]
   只应称为**拓扑向量空间直和**。两个基元素仅模 \(P_{\rm an}\) 满足
   \[
   u_d^2\equiv u_d,\quad u_c^2\equiv u_c,\quad u_du_c\equiv0.
   \]
   它们在 \(I\) 内并非这些幂等元；例如
   \(M_{u_d}(2)=\pi\)，故 \(u_d*u_d\ne u_d\)。

   式 (6) 给出的双曲型与 \(-T/2\) 分解、两部分正交均正确。

没有发现草稿已经误称获得几何 principal divisors；第6、222、237、257–273行保留的边界适当。此次只读核查了草稿及内存中的符号计算，没有重验上游 PDF、运行 Lean、写文件或操作 Git。

## 主线程处理与结算

原审稿行号和SHA256属于补强前的289行版本，不用于定位最终稿。
所有数学异议均已处理：sharp子空间量词、线性零点和的连续界、合并后的总源条件、
CCM完成cyclic商的未证拓扑比较、I仅为谱消失闭理想、(5)+(6)的依赖、
商反向的明确公式及I内部仅为拓扑向量空间直和。
式(6)的原文输入由主线程核对1999 PDF69–74、76–78，74整页视觉核查；
本报告独立复算其有限部分与推广，单位元常数比较现已闭环。
八条代数Lean结果实测通过且无sorryAx；未借此认证Poisson、Gaussian、显式公式或实际主除子。
405只交付真实限制来源上的解析关系及精确配对兼容性；几何主除子、完整τ与RR仍开放。
