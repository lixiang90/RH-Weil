# 412独立来源审查

2026-09-21，Laplace，完整原始返回；仅规范Markdown换行。

**核准：完整截止乘积确为所述正交投影；单位群平均后秩为 \(2N+1\)。其中的 \(+1\) 已计入 Connes 的精确发散项，不能在只扣 \(2N\) 后，将留下的 \(1\) 认作原文有限部分。**

核读本地原件 :codex-file-citation{path="H:/codex-build/RH/RH-Weil/literature/f1/connes-trace-math-9811068v1.pdf" purpose="source"}，88页，519632字节。以下**印刷页与 PDF 页一致**。原件 SHA256：
```text
dfd4e9924d8980f82e3da11fdea861d318fda8f5c7ba57ee659baf8631975053
```
[arXiv v1 原始 PDF](https://arxiv.org/pdf/math/9811068v1)

1. **字符、测度及完整投影**

   Appendix II **p.72，(22)–(24)** 固定加性字符在 \(\mathbb Z_p\) 上平凡、在 \(p^{-1}\mathbb Z_p\) 上非平凡；自对偶加性 Haar 测度满足
   \[
   \operatorname{vol}(\mathbb Z_p)=1,\qquad
   \mathcal F1_{\mathbb Z_p}=1_{\mathbb Z_p}.
   \]
   §V **p.22，(15)(16)** 定义
   \[
   P_\Lambda,\qquad \widehat P_\Lambda=\mathcal FP_\Lambda\mathcal F^{-1},
   \qquad R_\Lambda=\widehat P_\Lambda P_\Lambda.
   \]

   对本题的 **整数 \(N\ge0\)、\(\Lambda=p^N\)**，令
   \(B_N=p^{-N}\mathbb Z_p,\ C_N=p^N\mathbb Z_p\)。由上述 Fourier 约定直接得到
   \[
   \widehat P_Nf(x)=p^N\int_{x+C_N}f(y)\,dy.
   \]
   因 \(C_N\subseteq B_N\)，两投影交换，且
   \[
   R_Nf(x)=1_{B_N}(x)\,p^N\int_{x+C_N}f(y)\,dy.
   \]
   因而它恰是投向
   \[
   \{f:\operatorname{supp}f\subseteq B_N,\
   f\text{ 在每个 }C_N\text{ 加法余类上常值}\}
   \]
   的正交投影，秩为
   \[
   [B_N:C_N]=p^{2N}.
   \]
   这是原文定义在当前字符约定下的直接识别，没有附加径向性或零矩条件。

2. **单位群平均改变重数；最内层是球**

   令
   \[
   M=\int_{\mathbb Z_p^\times}U(a)\,da_{\mathrm{prob}},
   \]
   其中单位群 Haar 测度总质量为1。它与 \(R_N\) 交换，\(R_NM\) 为径向子空间的正交投影。

   其独立方向是
   \[
   1_{p^m\mathbb Z_p^\times}\quad(-N\le m<N),
   \qquad 1_{p^N\mathbb Z_p},
   \]
   故
   \[
   \operatorname{rank}(R_NM)=2N+1.
   \]

   完整投影中，第 \(m\) 个壳有
   \((p-1)p^{N-m-1}\) 个加法余类方向；单位平均把它们压成一个方向。因此裸投影的秩分别增长为 \(p^{2N}\) 和 \(2N+1\)。

   **最后一个方向是整个内球 \(p^N\mathbb Z_p\)，不是球壳 \(p^N\mathbb Z_p^\times\)，也不是原点的点质量。** 在球壳基下，它包含无限尾部；不能仅凭维数相等，把该径向投影识别为估值坐标上的硬截断窗口。

3. **“\(|u|=1\) 测试给零”的准确范围**

   Appendix II **p.69，(9)** 明定
   \[
   \operatorname{Pf}_w
   \int_{\mathbb Q_p^\times}
   \frac{1_{\mathbb Z_p^\times}(u)}{|1-u|}\,d^*u=0.
   \]
   **Lemma 2，pp.72–73，特别是(26)–(29)** 证明：在上述加性字符约定下，这与 Theorem 3 的 Fourier 正规化有限部分相同。

   所以 \(h=1_{\mathbb Z_p^\times}\)，或其常数倍，确实给零。**这不适用于任意仅仅支撑在单位群上的 \(h\)。** 对这样的局部常值测试函数，直接有
   \[
   \operatorname{FP}_\alpha(h)=
   \int_{\mathbb Z_p^\times}
   \frac{h(u^{-1})-h(1)}{|1-u|}\,d^*u,
   \]
   右边为通常收敛积分，一般非零。

   字符约定也不可省略：Appendix II **Lemma 3，pp.76–77** 给出，若
   \(\alpha(x)=\alpha_0(\lambda x)\)，有限部分增加
   \[
   \log|\lambda|\,h(1).
   \]
   这是明确的字符变更公式，不能在保持当前导子与截止不变时任意采用。

4. **为什么扣 \(2N\) 留下的 \(1\) 不是源有限部分**

   §V **p.22，(14)、Theorem 3** 的乘法测度满足
   \[
   d^*(\mathbb Z_p^\times)=\log p,
   \]
   而定理采用
   \[
   2\log'\Lambda
   =\int_{\Lambda^{-1}\le |u|\le\Lambda}d^*u.
   \]
   两端点均包含。因此
   \[
   2\log'(p^N)=(2N+1)\log p.
   \]
   原文 **p.39，(9)之前** 也明确写出此等式；该页处于函数域的 \(S\)-local 讨论，这里仅用来交叉核对端点约定。

   对单位群指示函数，
   \[
   U(1_{\mathbb Z_p^\times})=(\log p)M,
   \]
   从而精确地
   \[
   \operatorname{Tr}\!\left(R_NU(1_{\mathbb Z_p^\times})\right)
   =(2N+1)\log p.
   \]
   若取概率平均对应的测试
   \(h_0=1_{\mathbb Z_p^\times}/\log p\)，则迹为 \(2N+1\)，**原文规定扣除的主项也是 \(2N+1\)**，有限部分为零。

   因此：

   - 秩计数中的 \(+1\) 与原文完全相容。
   - 扣 \(2N\) 后保留 \(1\)，采用了另一种正规化。
   - 对一般测试，把原文扣项换成 \(2h(1)\log(p^N)\)，有限部分就增加 \((\log p)h(1)\)，即增加单位元处的 Dirac 项。

5. **仍须由主线程证明的接口**

   - 实际使用的截止究竟对应 \(R_N\)、\(R_NM\)，还是另有条件的子投影；尤其须识别内球方向。
   - 测试函数、单位平均测度及发散扣项是否同时采用上述正规化。
   - §V **p.21，(13)** 使用 \(U(\lambda)\xi(x)=\xi(\lambda^{-1}x)\)，没有酉化因子。若主线程使用 \(|\lambda|^{-1/2}U(\lambda)\)，须相应替换测试函数；单位群上的结论不受影响。
   - Theorem 3 输入是紧支撑的 Schwartz 测试函数；\(1_{\mathbb Z_p^\times}\) 合法，但产生恒等算子的 Dirac 测试不在该输入类中。因此不能把裸完整投影的 \(p^{2N}\) 迹直接代入其对数发散公式。

实际核读：**pp.19–25、38–41、69–73、76–77、79**；视觉复核 **pp.22、39、72**。未重做悬挂或压缩算子计算，未修改文件、保存新原件或运行 Git／Lean。
