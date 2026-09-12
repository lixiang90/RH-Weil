# 387的谱检测、局部化复合与闭理想边界

2026-09-13。McClintock核对来源接口；主线程另读关键页与勘误。
这份报告不替代387直接证明的独立复核。

固定原件：

- [KL1 Foundations v5](../../literature/f1/kl-foundations-1301.0792v5.pdf)，SHA256
  `a6a117423db62aec072442bb15b70e3175bcc3b631bdcd6d74f740e3c6cfd942`。
- [KL2 Imperfect v3](../../literature/f1/kl-imperfect-1602.06899v3.pdf)，
  [固定来源](https://arxiv.org/abs/1602.06899v3)，SHA256
  `97383900492daf1c6778959c37e993f67dd5ad379ac03c31049b870382e5d42c`。

## 已核来源接口

1. KL1 Lemma2.4.13(b) / PDF42不只说开集复合：S的有理子域准确对应原A空间中
   包含在S域内的有理子域。Definition2.4.12 / PDF41的泛性质给对应复合局部化环。
2. KL1 Definition2.8.1(b) / PDF59使uniform环的原范数等价于谱半范数。
   Theorem2.3.10 / PDF35及Remark2.3.11(b) / PDF36给谱半范数等于各谱点取值的最大值。
   因而非零元素g确实有某个谱点取值为正，Definition2.4.6 / PDF40给实际Spa点。
3. 取常数单位λ且|λ|<β(g)，有理域{|λ|≤|g|}非空；
   Lemma2.4.13(a)的闭关系商含gT=λ，所以g可逆。
4. 任意有理局部化S的uniform性由KL1 Theorems3.6.14(c)、3.6.15 / PDF94，
   或KL2 Theorem3.3.18(i)、Corollary3.3.19 / PDF64–65支持。

McClintock明确仅审核上述来源，不重复Singer的自然c_0图、限制映射单射及茎上正则性证明。
本轮代理均无仓库/git修改，也没有启动代理。

## uniform定义的已公布勘误

主线程读KL1 PDF35–36、59及KL2 Appendix A / PDF189。
后者修正KL1 Definition2.8.1：条件(a)–(c)等价并作为uniform定义，
一般(d)“幂有界子环有界”是必要但未必充分；它的反向需要附加规范前提。
387使用(b)，不受该修正影响。382的非uniform证明也保留了谱半径与原范数不等价的直接证据，
而且由必要性反推非uniform并未误用(d)的充分性。

## 闭性缺口不是二维模型特有的问题

主线程另读KL2 Example2.4.2 / PDF35–36。该例使用模曲线的无限p层与Hodge–Tate周期映射，
是来自一维曲线的perfectoid例子；不是本项目已经识别的一变量完美化乘法环域。
它给f在两环中均为非零因子、fA闭但有理局部化后fB不闭。
正文还把找到相应零因子、从而得到非平坦局部化的例子列作另外的问题。
因此不能称该例已经证明非平坦，也不能由单射或一维几何自动推出闭主理想。

本报告不以该例反驳387，也不从387导入一般商的完备性、稳定伪相干或规范重数测度。
