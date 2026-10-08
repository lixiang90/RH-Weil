# Knausgård arXiv:2610.08965v1：解析链独立审查

日期：2026-10-08。审查者：perron_reviewer；与论文作者及父任务的 Lean 审查分开。
结论：**限定解析 PASS，未发现主计数链的实质缺口；不是完整形式验证或大规模计算复演 PASS。**

## 1. 固定版本与实际阅读范围

- [论文固定 v1 全文](https://arxiv.org/html/2610.08965v1)：全文 §§1–8、附录 A、方法上限的证明与信任声明均已读；主链证明另以原 TeX 逐式核对。
- [BGST 作者主文](https://catalog.lib.kyushu-u.ac.jp/opac_download_md/7377443/7377443.pdf)：读 Theorem 1、§§2–3 的 Lemmas 1–5 及相应证明；使用的是无条件全零点配对公式，不使用其薄带或密度推论。该载体包含作者 arXiv:2306.04799v1，不冒称已逐页审读后来刊本全部页码。
- 本地 [483](../../notes/483-admission-of-known-am-eight-point-proportion.md) 全文读回；附录三个表文件全文读回，并独立核有理预算。
- 未独立重建约 102,000 行底层形式库，未执行三个庞大搜索；以下计算公理说明依据论文 §8，代码级依赖由另项审查承担。

| 实际读回输入 | 行数 / canonical LF bytes | SHA256 |
|---|---:|---|
| tmp/pdfs/knausgard-2610-08965-v1/knausgard839.tex | 2584 / 137960 | 7384ba0e91228026ca861deca551734a417e8c13365803f725a93a6dde2e0bca |
| notes/483-admission-of-known-am-eight-point-proportion.md | 166 / 7342 | 3ab82cdb257a8555b206f90e59c18fb73f68fe9be0a2de5117bb573056efdb7e |

LF 身份只统一行尾、不删除文件末尾换行。父任务下载包的 archive SHA 为
60fb628fb12bdc1ca28d6e849ce9180e9fbcc8b482021bb62d2c92b7827ac3cb；
此包身份不等同于本审查独立运行其计算。

## 2. 无条件能量与离线零点：重推结果

令 \(L=\log T\)、\(z_\rho=i(\rho-\tfrac12)L/(2\pi)\)。
平滑窗 \(f_\epsilon=\eta_\epsilon^2\) 先固定；零点按重数计入。
反射 \(\rho\mapsto1-\bar\rho\) 将 \(z\) 变为 \(\bar z\)，故
\[
A=\sum_z\nu_z F_z\langle F_{\bar z},\,\cdot\,\rangle,\qquad
\operatorname{tr}A=N,\quad
\operatorname{tr}A^2=\sum_{z,w}\nu_z\nu_wK_\epsilon(z-w)^2
\]
是 Hermitian 有限秩算子。离线时单个 \(K_\epsilon(z-w)^2\) 可以为复数；
这里使用整项的迹，未将各项强行当作正能量。

独立核对去权恒等式：若 \(R_\epsilon=f_\epsilon*f_\epsilon\)，则
\[
\widehat{R_\epsilon-R_\epsilon''/(4L^2)}(x)
=(1+\pi^2x^2/L^2)K_\epsilon(x)^2.
\]
代入 \(x=i(\rho-\rho')L/(2\pi)\) 后，此因子恰为 BGST 权
\(w(\rho-\rho')=4/(4-(\rho-\rho')^2)\) 的倒数。
BGST Lemma 5 允许符号变化的实偶测试；分别消费两个**固定**测试
\(R_\epsilon,R_\epsilon''\)，导数项仅 \(O_\epsilon(N/L^2)\)。
因此无需针对随 \(T\) 变化的测试误用统一误差，且没有假设 RH。
极限必须先 \(T\to\infty\)，再 \(\epsilon\to0\)；原文遵守此顺序。

## 3. 阈值、分离与重数：未见不合法删项

我重推了 Lemmas 2.1–2.4：
阈值式的余量归结为 \(\operatorname{tr}(X_+-Z)^2\ge0\)；
pinching 只须标量凸性加谱测度 Jensen，不须错误的算子凸性。
大筛只用于临界线实频率：\(0\le w\le g\) 且
\(\widehat g(y_i-y_j)=0\) 时，积分平方直接给 Gram 上界 \(\Lambda I\)。
它没有用于复频率离线零点。

极大不相交近对剥离后，剩余集合确实分离；对每个近对以固定和的特征值凸性比较。
标签 \(d=1,2\) 的分离块满足 \(G\le(c/2)D\le cI\)，因而无 clipping 损失。
平滑误差通过 \(O(d_\epsilon\,\#Y)\) 付款；严格主项参数留出余量。

离线反射对写为
\(\nu(vw^*+wv^*)=\frac{\nu}{2}((v+w)(v+w)^*-(v-w)(v-w)^*)\)，
故每对至多一个正特征值，重数增加迹但不增加这个正秩上界。
高重临界线零点各贡献一个正秩。相应 \(Q\) 的正惯性界保留了全部零点。
distinct 链的检查量为
\[
\mu=1.960733,\quad \nu=3.684917,\quad
r_h=1.792984,\quad r_k=0.0688,
\]
均严格正；\(j\nu+\mu-c^2\) 与 \(2j\nu+2\mu-c^2\)
分别在 \(j=3,1\) 取最坏值，故没有遗漏更大重数。
simple-critical 链中 \(N-n\ge2p\) 精确覆盖每个多重线零点及离线对。

## 4. 七／八点转移与边界

对标签固定的实际点对，滑窗总权重受每个 index-distance 的预算约束；
独立整数检查三个附录表的全部 21 / 28 / 21 个点对均通过。
首窗预算分别不超过 \(2,4,8\)，后二窗均不超过 \(2\)；
奖励和与两条 headline 的 Fraction 算式也通过。

关键 storage 不是逐窗丢弃：逐式重推后，当前相邻标签随滑窗移位保持，
\(\sum_rB_r^{dd'}=0\) 给当前状态 \(\Phi\) 减下一状态 \(\Phi\)。
整个序列只有一次端点振幅损失 \(\Omega\)，没有乘窗数。
独立以分段函数的极值预算核得三窗 \(\Omega\) 上界
0.015882、0.003882、0.075420；传播长度费用分别为 \(6\alpha,7\alpha,6\alpha\)。
近对、空集及点数不足一窗的情况均已付款。

连续证明的高度跨度 \(\le T\log T/(2\pi)=N+o(N)\)；
固定端点常数除以 \(N\) 后消失，容差损失先为 \(O_\epsilon(N)\)。
形式版本另用 bandwidth \(\lambda<1\) 与 dyadic 高度段：
能量 \(A/\lambda+\lambda B\) 在 \(\lambda\to1^-\) 回到 \(C(f)\)，严格常数余量允许选择 \(\lambda\)。
端点 \(\sqrt T\) 区间的零点数按重数为 \(O(\sqrt T\log T)=o(N)\)，
搬进 \(Q\) 的逐零点费用有限；这足以解释该边界改写的解析量级，
不替代实际库中每个形式引理的重建。

## 5. 数值证书与可信性限制

表格覆盖的是连续 gap 域：区间上的核下界由 Taylor 余项与
\(|K'|\le\pi, |K''|\le\pi^2\) 控制；长跨度由正 spread 费用直接付款。
分枝盒上的下界与标签联合最小化方向正确，不能把最小 slack 的浮点搜索当作证明。
解析上，若各全域搜索确实返回 true，局部证书到全零点比例的桥已闭合。

[论文 §8 的信任声明](https://arxiv.org/html/2610.08965v1#S8) 明确：三个 native_decide 大搜索各引入一个计算公理；每个主结果依赖其中相应的一次。
它们不是只依赖 propext、Classical.choice、Quot.sound 的纯 kernel 全域归约。
搜索 soundness 与成功执行是不同命题；本审查核前者的解析消费，
没有复演后者或据表格箱数认定完整形式认证。

## 6. 与 483 及本项目的关系

分母均为全部非平凡零点的重数计数。新 simple-critical 下界
\(1669159/2478195=0.673538200181987\ldots\)；
483 为 \(118513839290/175971686899=0.673482429920795\ldots\)，
差为 \(24320973366391/436092154614667305\)，即 **0.00557702611914 个百分点**。
新 distinct-allstrip 下界是 \(1645064/1960733=0.839004596750296\ldots\)，
不能称为 83.9% 在临界线；\(2q-1\) 是 simple-allstrip，也不能称为 simple-critical。
两者均为外部成果，本审查不将其认领为项目新纪录。

可借鉴的实际机制是保留标签的近对／分离转移、storage 端点收费与窗口联合优化。
这些是二阶计数输入，未证明原 signed squarefree 包的四阶近相关减少。
既有普通 \(\zeta\) 的 \(7/8\) 边界只限制实部在固定宽带；
\(|\beta-\tfrac12|\log T\) 仍可增长，不能变成 BGST 的 \(1/\log T\) 薄带，
也未自动减少离线正惯性计数或提高上述比例。
故本次结论是新论文解析链可信度得到支持，完整数值／形式可信度仍须另行核验；
没有免费新零点比例、全主项四阶上界或零点自由条带。
