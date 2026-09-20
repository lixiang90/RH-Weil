# 413独立来源审查

2026-09-21，Laplace；完整返回，仅规范Markdown换行。

本次来源接口可以核准。需要保留两项限定：**Morita 比较若要识别另一扩张的边界，必须具有扩张层面的相容性；圆参数分裂应先保留悬挂边界，不能省略 Bott 识别后直接断言两个分量同号。** 新增的零维空间及悬挂 K 群公式有标准依据，不需要一般 Künneth 定理。

核查对象为本地 [Blackadar book6](H:/codex-build/RH/RH-Weil/literature/f1/blackadar-k-theory-author-book6.pdf)，314 页；以下 PDF 页码均从 1 起算，正文对应“印刷页＋14”。

SHA256：
`a20e676e9d400ebcd0cd07c13fbdbe1fac759a30c739fab23d6161ecfb1a23fb`

作者原版：[book6.pdf](https://bruceblackadar.com/Mathematics/book6.pdf)。

1. **\(K_0\to K_1\) 指数边界：正号已经核准。**

   Blackadar **9.3.1–9.3.2，印刷 pp.67–68／PDF pp.81–82**。对于
   \[
   \mathcal E:\quad0\longrightarrow J\longrightarrow B\xrightarrow{\pi}Q\longrightarrow0,
   \]
   在标准单位化画面中，取投影 \(e\in M_n(Q^+)\)，其标量部分为 \(p_r\)，以及自伴提升 \(h\in M_n(B^+)\)，则
   \[
   \boxed{\delta_0^{\mathcal E}([e]-[p_r])
          =[\exp(2\pi i h)]\in K_1(J).}
   \]
   因为 \(\pi^+(\exp(2\pi ih))=1\)，该酉元属于 \(1+M_n(J)\)。自伴提升即可，**无需投影提升**；若确实存在投影提升，边界为零。

   这适用于非幺扩张，不要求半分裂。商有幺不能据此认定商单位的边界为零。书中另一方向的约定为 **8.3.2，印刷 p.63／PDF p.77**：
   \[
   \delta_1([u])=[1-v^*v]-[1-vv^*],
   \]
   即核减余核的 Fredholm 指数约定。

2. **\(K_1(C_0(\mathbb R))\) 的正向生成元可以明确固定。**

   **9.1.1，印刷 p.64／PDF p.78** 定义
   \[
   \beta_D([e]-[p_r])=[f_e f_{p_r}^{-1}],
   \qquad f_e(z)=ze+(1-e).
   \]
   **9.2.1，印刷 p.65／PDF p.79** 证明它是同构。因此 \(\beta_{\mathbb C}([1])\) 对应正向圈 \(z=e^{2\pi it}\)。

   若实坐标正向取 \(x:-\infty\to+\infty\)，可明确选
   \[
   \chi(x)=\frac12+\frac1\pi\arctan x,\qquad
   u_+(x)=e^{2\pi i\chi(x)}=\frac{x-i}{x+i}.
   \]
   则 \(u_+-1\in C_0(\mathbb R)\)，绕数为 \(+1\)；逆元绕数为 \(-1\)。这是上述 Bott 定义的直接坐标化。

   一个确实存在的定向区别：**19.3.4(a)，印刷 p.191／PDF p.205** 在解释 Thom 元时采用 \(+\infty\mapsto0,\ -\infty\mapsto1\)。不能未经换向，把该处 Thom 生成元直接当作这里“实坐标递增”的正生成元。

3. **Morita 对理想、商及边界的相容性成立，但应说明所用比较。**

   书中直接定位：

   - **13.6.2，印刷 p.112／PDF p.126**：Hilbert 模稳定化定理。
   - **13.7.1(b)(c)，印刷 p.113／PDF p.127**：满遗传子代数的强 Morita 等价，以及 \(\sigma\)-幺情形的稳定同构；这里是**习题中的标准结论**。
   - **21.1.1、21.1.2(a)，印刷 pp.217–218／PDF pp.231–232**：普通 K 理论的连接映射对短正合列态射自然，且 K 理论稳定。

   为补足书中未集中陈述的 linking algebra 接口，核读了 Brown–Green–Rieffel 原文 **Theorem 1.1，印刷 pp.350–351／出版社 PDF pp.3–4**；它将强 Morita 等价实现为同一代数中的互补满角。**Theorem 1.2，印刷 pp.351–352／PDF pp.4–5** 给出可数近似单位条件下的稳定同构。原始链接：[出版社 PDF](https://msp.org/pjm/1977/71-2/pjm-v71-n2-p06-s.pdf)。仅在线读取，未保存文件。

   具体的理想与边界相容性可由该构造直接推出：若 \({}_A E_B\) 为 imprimitivity bimodule，\(J_A\triangleleft A\)，令
   \[
   E_J=\overline{J_AE},\qquad
   J_B=\overline{\operatorname{span}}\langle E,J_AE\rangle_B.
   \]
   则 \(E_J\) 比较两个理想，\(E/E_J\) 比较两个商。它们组成同一个 linking algebra 扩张的角，因而诱导
   \[
   \mu_J\circ\delta_A=\delta_B\circ\mu_Q.
   \]
   这里的理想／商／边界结论是**linking 构造加边界自然性的直接推论**，不是把 BGR Theorem 1.1 误称为已经逐项陈述这些结论。

   对 413 的使用界限是：单独指定 \(J\sim_M C_0(\mathbb R)\)、\(A_p\sim_M C(S^1_{\log p})\) 等，可以运输原扩张的 K 群与边界；**它们本身不会识别出另一模型扩张的边界**。若要作后一种比较，须给出相容扩张图、linking 扩张或相应的稳定化图。

4. **圆参数分裂不需要一般 Künneth；边界相容性有一个无歧义写法。**

   令 \(\Omega D=C(S^1)\otimes D\)，以 \(1\in S^1\) 为基点：
   \[
   0\longrightarrow SD\xrightarrow{j}\Omega D
   \xrightarrow{\mathrm{ev}_1}D\longrightarrow0.
   \]
   常值函数给出 \(*\)-同态截面 \(c\)。依据 **8.3.6，印刷 p.64／PDF p.78**，
   \[
   K_i(\Omega D)\cong K_i(D)\oplus K_i(SD),
   \quad(a,b)\longmapsto c_*(a)+j_*(b).
   \]
   再用 **8.2.2，印刷 pp.61–62／PDF pp.75–76** 和上述 Bott 定理，得到
   \[
   K_i(C(S^1)\otimes D)\cong K_i(D)\oplus K_{i+1}(D).
   \]
   **9.4.1，印刷 p.68／PDF p.82** 正是这项计算的习题，不是一般 Künneth 假设。

   圆参数化原扩张仍然正合：这里 \(C(S^1)\) 为核代数，见 **15.8.2，印刷 p.130／PDF p.144**；也可在连续代数值函数的画面中直接验证。

   **在尚未消去悬挂的分裂下，准确公式为**
   \[
   \boxed{\delta_i^{\Omega\mathcal E}
      =\delta_i^{\mathcal E}\oplus\delta_i^{S\mathcal E}.}
   \]
   常值截面和悬挂理想包含均给出扩张态射，因此此式直接来自自然性，没有混合分量。

   如需写成 \(K_i(D)\oplus K_{i+1}(D)\)，固定
   \[
   s_{0,D}=\theta_D:K_1(D)\to K_0(SD),\qquad
   s_{1,D}=\beta_D:K_0(D)\to K_1(SD),
   \]
   则第二分量准确地是
   \[
   s_{i-1,J}^{-1}\,
   \delta_i^{S\mathcal E}\,
   s_{i,Q}.
   \]
   **本次核准到这一明确公式；9.4.1 本身不足以支持把它未经说明改写为另一份同号的 \(\delta\)。** 这保留了全部边界相容性，并明确标出了坐标、悬挂及 Bott 约定的入口。

5. **新增零维空间与悬挂公式：标准依据充分。**

   对局部紧 Hausdorff、零维、第二可数空间 \(X\)：

   - **7.1.2，印刷 p.48／PDF p.62** 明列 \(C_0(X)\) 为 AF 代数。
   - **8.1.2(a)，印刷 pp.59–60／PDF pp.73–74** 给出 AF 代数的 \(K_1=0\)。
   - **5.2.4，印刷 p.29／PDF p.43**，以及 **5.5，印刷 p.31／PDF p.45**，给出所需的归纳极限连续性及非幺 K₀ 画面。

   由有限紧开分割形成的有限维子代数及其秩函数，直接得到自然同构
   \[
   \boxed{K_0(C_0(X))\cong C_c(X,\mathbb Z),\qquad K_1(C_0(X))=0.}
   \]
   此处 \(C_c(X,\mathbb Z)\) 指**连续、紧支撑的整数值函数**。完整公式是上述书中结论的直接推论，不应伪引为 7.1.2 的逐字陈述。

   利用 \(C_0(X\times\mathbb R)\cong S C_0(X)\) 及两项悬挂同构：
   \[
   \boxed{K_0(C_0(X\times\mathbb R))=0,\qquad
          K_1(C_0(X\times\mathbb R))\cong C_c(X,\mathbb Z).}
   \]
   实变量平移由点范数连续的平移同伦连接到恒等，故在 K 群上作用为恒等；K₀ 同伦不变性的明确定位为 **5.2.2，印刷 p.29／PDF p.43**。

   两次 PV 的标准入口为 **10.2.1，印刷 p.73／PDF p.87**，对任意 C*-代数及其自同构适用，书中横箭头写作 \(1-\alpha_*\)。这核准了计算工具；**没有代替主线程核准紧开上尾矩形基、乘 \(X,Y\) 的实际作用、第二次诱导作用或最终模计算**。

本报告直接使用并逐页核读的 Blackadar 范围为：PDF **42–43、45、62、73–82、87、126–127、143–144、203、205、231–234**；其中 PDF **78、82** 另作内存渲染核对。BGR 核读范围为印刷 **349–352／出版社 PDF 2–5**。未审查 413 的商拓扑、实际边界值或理想计算，未运行 Git／Lean，未修改或新增文件。
