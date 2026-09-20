# 414 独立来源审查

2026-09-21。以下是原Laplace完成通知的完整报告，工具会话丢失后从会话原文恢复；[保留的通知JSON](f1-boundary-unitary-source-review.raw.json)不是重新执行审查的返回。原文中的“未保存PDF”指审查者当时状态，主线程随后另行保存原件。

三项来源接口均可支持，但应区分：**标准定理给出的 Morita 比较、截止投影的直接识别，以及主线程仍需完成的指定满角同构和源提升。** 本次未审查 414 主稿的具体构造。

1. **完整两平移交叉积与旋转代数的比较**

   最贴合的来源是 Williams 作者稿 **Version 3.1，2006-09-06**：

   | 定位 | 已核内容 |
   |---|---|
   | Theorem 4.1，印刷 pp.110–111／PDF pp.122–123 | Raeburn 的一般对称 imprimitivity 定理 |
   | Corollary 4.11，印刷 p.126／PDF p.138 | Green 的标量版本及 \(C_c(P)\) 等价双模公式 |
   | Proposition 3.11，印刷 p.87／PDF p.99 | 半直积对应迭代交叉积，包含直积情形 |
   | Theorem 7.13，印刷 p.199／PDF p.211 | amenable 群作用的 full、reduced 交叉积相同 |

   Corollary 4.11 要求两个局部紧群在局部紧 Hausdorff 空间上的左右作用**分别自由、proper，且彼此交换**，结论为
   \[
   C_0(P/H)\rtimes K\ \sim_M\ C_0(K\backslash P)\rtimes H.
   \]
   来源：[Williams 作者原稿](https://math.dartmouth.edu/~dana/cpcsa/draft3.1.pdf)。

   对
   \[
   D=C_0(\mathbb R)\rtimes\Gamma,\qquad
   \Gamma=L_p\mathbb Z+L_q\mathbb Z\cong\mathbb Z^2
   \]
   必须给 \(\Gamma\) **离散拓扑**。以下是定理的直接实例化，并非书中的逐字例子：取
   \[
   P=\mathbb R\times\mathbb Z,\quad K=\mathbb Z^2,\quad H=\mathbb Z,
   \]
   \[
   (m,n)\cdot(t,k)=(t+mL_p+nL_q,k+n),\qquad
   (t,k)\cdot r=(t,k+r).
   \]
   两作用满足上述前提，两个商分别由 \(t\) 和
   \([t-kL_q]_{L_p}\) 识别。因此得到实际 C*-代数的比较
   \[
   \boxed{D\sim_M C(\mathbb R/L_p\mathbb Z)\rtimes\mathbb Z
   \cong A_\theta,\qquad \theta=L_q/L_p.}
   \]
   此处 \(p,q\) 为不同素数，故两长度有理无关。

   为固定符号，若圆上的代数作用为
   \(\alpha_q(f)(t)=f(t-L_q)\)，取圆坐标
   \(V(t)=e^{2\pi it/L_p}\) 和实现酉元 \(W\)，则
   \[
   VW=e^{2\pi i\theta}WV.
   \]
   改换生成元方向时，应同时记录关系的变化。

   **不能直接把完整 \(\Gamma\curvearrowright\mathbb R\) 称为 proper。** 另外，Williams Example 4.14，印刷 pp.126–127／PDF pp.138–139，直接讨论的是两个旋转代数之间的比较，不能单凭该例替代上面的实例化。

   已存 BGR 的 **Theorem 1.1，印刷 pp.350–351／PDF pp.3–4** 给出 linking algebra 中的互补满角；**Theorem 1.2，印刷 pp.351–352／PDF pp.4–5** 在可数近似单位条件下给稳定同构。它们支持
   \[
   D\otimes\mathcal K\cong A_\theta\otimes\mathcal K,
   \]
   **不会自动指定主线程所选 \(e\) 的角同构，也不能未经证明删掉左侧稳定化。**
   原件：:codex-file-citation{path="H:/codex-build/RH/RH-Weil/literature/f1/brown-green-rieffel-morita-1977.pdf" purpose="source"}

2. **非幺扩张、一般非可逆提升及指数自然性**

   本项依据已存 Blackadar：:codex-file-citation{path="H:/codex-build/RH/RH-Weil/literature/f1/blackadar-k-theory-author-book6.pdf" purpose="source"}

   对任意 C*-扩张
   \[
   0\longrightarrow J\longrightarrow B\xrightarrow{\pi}Q\longrightarrow0,
   \]
   准确定位如下：

   - **3.4.2，印刷 p.18／PDF p.32；8.1.1，印刷 p.59／PDF p.73**：非幺 \(K_1\) 使用单位化中标量部分为 \(1_n\) 的可逆元／酉元。
   - **8.1.5，印刷 p.61／PDF p.75**：非幺同态延拓至单位化，诱导 \(K_1\) 映射。
   - **3.4.1、3.4.4–3.4.5，印刷 pp.18–19／PDF pp.32–33**：\(\operatorname{diag}(u,u^{-1})\) 位于恒等连通分支，并可作可逆提升；C* 情形可作酉提升。
   - **8.3.1–8.3.2，印刷 pp.62–63／PDF pp.76–77**：一般指数边界及部分等距特例。
   - **21.1.1、21.1.2(a)，印刷 pp.217–218／PDF pp.231–232**：连接映射对扩张态射自然，适用于普通 C*-K 理论，不要求半分裂。

   具体说，若 \(u\in U_n(Q^+)\)、\(u-1_n\in M_n(Q)\)，取
   \[
   w\in GL_{2n}(B^+),\qquad
   \pi^+(w)=\operatorname{diag}(u,u^{-1}),\qquad
   p_n=\operatorname{diag}(1_n,0_n),
   \]
   则
   \[
   \boxed{\delta_1[u]=[wp_nw^{-1}]-[p_n]\in K_0(J).}
   \]
   可以选 \(w\) 为酉元，此时第一项就是投影。

   **原来的单个提升 \(a\) 不可逆，并不妨碍这个定义。** 但不能因此直接写
   \([1-a^*a]-[1-aa^*]\)：一般这两个算子不是投影。仅在已有部分等距提升 \(v\) 时，8.3.2 才给
   \[
   \delta_1[u]=[1-v^*v]-[1-vv^*].
   \]
   原文也明确指出，商酉元一般未必能提升为部分等距。

   对满角中的酉元 \(v\in eQe\)，进入 \(Q^+\) 的代表应为
   \[
   \widetilde v=1-e+v.
   \]
   这是单位化函子性的直接应用。源提升是否确实属于指定 \(B^+\)、是否满足
   \(\pi^+(a)=\widetilde v\)，仍是主线程具体构造的验证内容。

   对相容扩张图，自然性准确写作
   \[
   (\phi_J)_*\delta_1=\delta'_1(\phi_Q)_*.
   \]
   若比较通过 Morita 等价完成，沿用上一轮确认的相容 linking 扩张即可；独立选择两端 K 群同构不足以识别另一扩张的边界。

3. **截止投影的来源、归一化和“秩一”的含义**

   最直接的原文接口是 Williams **Corollary 4.11 的公式 (4.43)、(4.44)，印刷 p.126／PDF p.138**，以及同页 **Remark 4.12** 的单群作用特例。公式中的复共轭已作目视核对。

   令
   \[
   B_p=C_0(\mathbb R)\rtimes L_p\mathbb Z,\qquad
   C_p=C(\mathbb R/L_p\mathbb Z).
   \]
   使用计数 Haar 测度、约定
   \[
   U_pfU_p^*(t)=f(t-L_p),
   \]
   Green 模 \(C_c(\mathbb R)\) 的内积特化为
   \[
   \langle\xi,\eta\rangle_{C_p}([t])
   =\sum_n\overline{\xi(t-nL_p)}\,\eta(t-nL_p),
   \]
   \[
   {}_{B_p}\langle\xi,\eta\rangle
   =\sum_n\xi(t)\overline{\eta(t-nL_p)}U_p^n.
   \]

   因而你给出的
   \[
   e=\sum_n c(t)c(t-nL_p)U_p^n
   \]
   **在 \(c\) 为实值截止函数时完全匹配原文接口**；通常取 \(c\ge0\)。若允许复值 \(c\)，须保留复共轭，并将归一化写成 \(\sum_n|c(t-nL_p)|^2=1\)。

   在该归一化下，\(\langle c,c\rangle_{C_p}=1\)，所以 \(e\) 对应
   \(\theta_{c,c}\)。由 imprimitivity 恒等式直接得到：它是满投影，其在 \(B_p\) 中的角为 \(C_p\)。这属于**原文内积公式的直接推论**，不是书中逐字出现了本题的 \(p\)-截止公式。

   还应保留三个使用界限：

   - \(c\) 紧支撑保证仅有限个 Fourier 系数非零，因此 \(e\in B_p\)，不只是乘子投影；\(U_p\) 本身通常是乘子酉元。
   - “秩一”指 Hilbert \(C_p\)-模中的秩一，不能直接解释为某个整体 Hilbert 空间表示中的有限秩。
   - 从该 \(e\) 到完整 \(D\) 中指定角 \(eDe\cong A_\theta\)，仍须核准 \(q\) 方向的实现酉元、关系和生成性；不能仅因有 Green 等价就默认 \(eU_qe\) 已是所需酉元。这部分留给主线程。

本次直接用于结论的核读范围：

- **Blackadar**：PDF **32–33、37、45、73、75–77、231–232**；PDF **76–77** 另作内存渲染。
- **BGR**：PDF **3–5**，即印刷 **350–352**。
- **Williams**：版本页及 PDF **79–80、99、122–123、137–138、211–212**；另核读 Lemma 3.54 的作用约定和 Example 4.14 的续文。PDF **122、138** 作内存渲染。未逐页核读整个 imprimitivity 定理证明或全书。

Williams 原稿此前未在本地文献目录找到，本次仅读入内存，未保存文件：**540 页，3,843,628 字节**，SHA256：
`3dbc1fb9e96191a278e0d59feb4981d3bbea4faa4df609d1886c81125bffe9c2`

全程只读，未修改文件，未运行 Git／Lean；未将这些标准输入视为对 414 具体满角、源提升或指数值的认证。
