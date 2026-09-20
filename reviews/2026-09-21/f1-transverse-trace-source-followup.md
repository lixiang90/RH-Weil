# 412来源采纳复核

2026-09-21，Laplace，完整返回；仅规范Markdown换行。

§5 的 **(13)–(13c) 来源采纳、酉化方向和正规化正确**。本次以(5)(6)(10)为既有输入，未重审其证明。

- \(\lambda=p^{-a}u\) 时，\(|\lambda|_p=p^a\)，故
  \[
  U_C(\lambda)=p^{a/2}V_aD_{u^{-1}},
  \]
  对应 \(h(s)=e^{s/2}k(s)\)，方向正确。
- \(k\in C_c^\infty(\mathbb R)\) 保证 \(g_k\) 紧支、局部常值，零延拓仍是 Schwartz 函数，属于原定理输入。
- 增加右侧 \(P_N\) 不改变有限秩迹。(13c) 的逐 \(N\) 精确性来自稿内(10)，没有冒称 Connes 原定理本身给出逐 \(N\) 等式。
- 扣项 \((2N+1)Lk(0)\) 及单位壳层有限部分为零均正确。

建议收紧两处措辞，避免范围误读：

- [第168行](H:/codex-build/RH/RH-Weil/notes/412-f1-transverse-compression-and-periodic-traces.md:168)：改为“**对本文径向测试族 \(g_k\)，有限位有限部分已经识别**”。
- [第171行](H:/codex-build/RH/RH-Weil/notes/412-f1-transverse-compression-and-periodic-traces.md:171)：改为“**该正规化保证单位群上的常值测试给零；仅支撑在单位群并不足以保证为零**”。避免“仅对”被理解为零值测试必须为常值。

本次核读 SHA256：
```text
50e48ce99f058b04369c1f397f69d31ffb160ec320938e491f45891e99055513
```
未改文件，未运行 Git／Lean。
