# 395：连续主商代数核心的独立复核

2026-09-20。只读代理Raman（01a0bcfa-9310-7f50-80c2-1712bf1327e1）。
固定紧Hausdorff载体及389测度性质作为输入；不重审上游几何。
[395正文](../../notes/395-f1-geometric-measure-principal-quotient.md)。

**复核通过。** 对你消息中的 395 核心命题，在固定紧 Hausdorff 空间 \(X\)、全部测度属于 \(M(X)=C(X,\mathbb R)^*\)、并采用相对弱星拓扑的前提下，
\[
\boxed{\overline{P_0}^{\,V_0,w^*}
      =V_0\cap\ker(\mathrm{mass})},
\qquad
\boxed{A=N\oplus\mathbb R1,\quad A/N\cong\mathbb R}.
\]
无需假设 \(V_0\) 闭或完备。G3 排除结论需要保留上述拓扑限定。

1. **量词与良定义。**

   固定一个 \(F\in A\)。对每个 \(w>0,d\in H_p\)，非零截面存在；消去同一指定线丛内的所有截面差，使
   \[
   a_F(w,d)=\langle F,\nu_f\rangle
   \]
   与截面选择无关。非零截面的乘积及测度可加性给出
   \[
   a_F(w+v,d+e)=a_F(w,d)+a_F(v,e).
   \]
   此处确实需要遍历**全部正实权、全部指定扭曲及其全部非零截面**；不能未经证明缩减到某个紧截面族。完全不需要随 \(w\) 连续选择截面。

2. **torsion 消除正确，而且在 \(P_0\) 内已经精确成立。**

   令 \(m=p-1\)。按 [392 的单项式同构公式](https://github.com/lixiang90/RH-Weil/blob/main/notes/392-f1-eigensections-and-weighted-banach-space.md)，
   \[
   U^q:H(w,d)\longrightarrow H(w,d+mq).
   \]
   对 \(f\in H(w,d)\setminus\{0\}\)、\(g\in H(w,e)\setminus\{0\}\)，取
   \[
   h=U^{d-e}g^m\in H(mw,md)\setminus\{0\}.
   \]
   因而
   \[
   m(\nu_f-\nu_g)=\nu_{f^m}-\nu_h\in P_0.
   \]
   \(P_0\) 是实线性空间且 \(m\ge1\)，所以
   \[
   \nu_f-\nu_g\in P_0.
   \]
   因此 \(a_F(w,d)\) 只依赖 \(w\)。\(p=2\) 时 \(m=1\)，同样成立；没有遗漏边界情形。

3. **Cauchy 有界性足够，且直接给出 Lipschitz 连续性。**

   正性和总质量公式共同给出
   \[
   |a_F(w)|\le \|F\|_\infty w.
   \]
   对 \(v>w>0\)，由加性，
   \[
   |a_F(v)-a_F(w)|
   =|a_F(v-w)|
   \le\|F\|_\infty(v-w).
   \]
   因而 \(a_F\) 连续。又对正有理数 \(r\)，
   \(a_F(r)=r\,a_F(1)\)，取有理逼近即得
   \[
   a_F(w)=c_Fw,\qquad c_F=a_F(1).
   \]
   对生成元作有限实线性组合便得到
   \[
   \langle F,\mu\rangle=c_F\,\mathrm{mass}(\mu)
   \quad(\mu\in V_0).
   \]
   常数 \(c_F\) 依赖 \(F\)，但不依赖权、扭曲或截面。

4. **弱星子空间连续泛函确实可以延拓。**

   设 \(\ell:V_0\to\mathbb R\) 对相对弱星拓扑连续。连续性保证存在有限个
   \(F_1,\ldots,F_n\in C(X,\mathbb R)\)，使
   \[
   \bigcap_i\ker\langle F_i,\cdot\rangle\big|_{V_0}
   \subseteq\ker\ell.
   \]
   理由是：左侧元素的任意实倍数都落在相应基本零邻域中，故其 \(\ell\) 值必须为零。

   所以 \(\ell\) 经由
   \[
   T:V_0\to\mathbb R^n,\qquad
   T(\mu)=(\langle F_i,\mu\rangle)_i
   \]
   因子化。将 \(T(V_0)\) 上的线性泛函延拓到有限维空间 \(\mathbb R^n\)，得到
   \[
   \ell(\mu)=\sum_i b_i\langle F_i,\mu\rangle
            =\langle F,\mu\rangle,\qquad F=\sum_i b_iF_i.
   \]
   这就是所需弱星连续延拓；不涉及完备性、闭子空间条件或自反性。

5. **相对闭包等式成立。**

   每个 \(P_0\) 生成元质量为零，而质量由常函数 \(1\) 表示，故
   \[
   K:=\overline{P_0}^{\,V_0,w^*}
   \subseteq V_0\cap\ker(\mathrm{mass}).
   \]
   若存在质量为零的 \(\mu\in V_0\setminus K\)，局部凸 Hahn–Banach 分离给出连续线性泛函 \(\ell\)，满足
   \[
   \ell|_K=0,\qquad \ell(\mu)\ne0.
   \]
   第 4 步将其表示为某个 \(F\) 的积分；因为它消去 \(P_0\)，第 3 步又给
   \(\ell=c_F\,\mathrm{mass}\)，矛盾。

   相应的**环境空间闭包**准确写作
   \[
   \overline{P_0}^{\,M(X),w^*}
   =\overline{V_0}^{\,M(X),w^*}\cap\ker(\mathrm{mass}),
   \]
   不能省掉右侧的 \(\overline{V_0}\)。

6. **有效观察空间确为一维，非恒定湮灭函数不构成新次数。**

   第 3 步恰好说明 \(F-c_F1\in N\)，故
   \(A=N+\mathbb R1\)。由于存在质量为 \(1\) 的生成测度，非零常函数不属于 \(N\)，此和为直和。

   若 \(\sigma\) 在 \(X\) 上连续且保持所有 \(\nu_f\)，则
   \[
   \psi-\psi\circ\sigma\in N.
   \]
   该函数是否非零取决于实际作用及 \(\psi\)；即使非零，其在 \(A/N\) 中仍为零。你的区别完全正确。

最后，**G3 障碍的准确表述**是：若完整 \(V=V_0\)，主关系 \(P\supseteq P_0\)，且双次数对上述相对弱星拓扑连续并消去 \(P\)，那么
\[
\deg=c_1\,\mathrm{mass},\qquad
\operatorname{codeg}=c_2\,\mathrm{mass}.
\]
在 \(\Psi_1\) 上二者均为 \(1\)，迫使 \(c_1=c_2\)；这与任何 \(\lambda\ne1\) 时所需的双次数 \((\lambda,1)\) 矛盾。

[现行条件包](https://github.com/lixiang90/RH-Weil/blob/main/formal/blueprint/geometric-realization.md)的 G4 要求次数连续，但没有强制选择弱星拓扑。因此，本证明排除的是上述拓扑接法；不能直接断言代数商 \(V_0/P_0\) 一维，也不能据此排除任意更强拓扑、真正平方或加入新周期后的几何。

本次仅作 connector 只读核对；未重审紧商构造及已接受的上游输入，未修改文件或 Git，未开启 agent。

## 补充定点复核

**三点均确认通过。** ②沿用 \(B\) 是实双线性形式的既定假设。

1. **商范数恰为 \(|c_F|\)。**

   对任意 \(n\in N\)，有 \(c_{F+n}=c_F\)，因此
   \[
   |c_F|\le\|F+n\|_\infty.
   \]
   另一方面，\(F-c_F1\in N\)，所以同一陪集有常函数代表 \(c_F1\)。于是
   \[
   \boxed{\|F+N\|_{A/N}
   =\inf_{n\in N}\|F+n\|_\infty=|c_F|}.
   \]
   因而 \(A/N\cong\mathbb R\) 还是等距同构。

2. **分别弱连续的配对必然退化为质量乘积。**

   取 \(\eta\in V_0\) 满足 \(\mathrm{mass}(\eta)=1\)。固定 \(\nu\)，对第一变量应用已证结论：
   \[
   B(\mu,\nu)=\mathrm{mass}(\mu)\,B(\eta,\nu).
   \]
   再对第二变量应用结论：
   \[
   B(\eta,\nu)=B(\eta,\eta)\,\mathrm{mass}(\nu).
   \]
   故
   \[
   \boxed{B(\mu,\nu)=k\,\mathrm{mass}(\mu)\mathrm{mass}(\nu)},
   \qquad k=B(\eta,\eta).
   \]
   若定义域为 \(S=\overline{V_0}^{\,w^*}\)，每个连续线性切片在稠密子空间 \(V_0\) 上确定，故同样成立。无需联合连续性，也无需预设对称性。

3. **有限评价投影可以完全替代这里的 Hahn–Banach 分离。**

   准确写法是：由 \(\mu\notin\overline{P_0}\)，**存在一组有限评价**
   \[
   T(\xi)=(\langle F_1,\xi\rangle,\ldots,\langle F_n,\xi\rangle)
   \]
   给出的基本邻域与 \(P_0\) 不交，因此 \(T\mu\notin T(P_0)\)。这里不是任意选取 \(T\)。

   \(T(P_0)\subset\mathbb R^n\) 是闭线性子空间；有限维线性代数给出 \(b\in\mathbb R^n\)，使
   \[
   b\cdot T(P_0)=0,\qquad b\cdot T\mu\ne0.
   \]
   令 \(F=\sum_i b_iF_i\)，即得到消去 \(P_0\) 而不消去 \(\mu\) 的连续评价。若 \(\mathrm{mass}(\mu)=0\)，便与已证的质量倍数结论矛盾。这一证明对 \(V_0\) 和 \(S\) 均适用。