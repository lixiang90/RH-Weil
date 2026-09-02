# 229. 四阶素数侧外部输入的逆向审计：行列式公式与判别式一致筛

日期：2026-09-02

分支：MOM-1 / 路线 A1h；接口：critical determinant shell、shifted \(E_j\) correlations

状态：Bettin--Chandee Corollary 1 的参数代入、单序列 Selberg 展开的 level
账本、Henriot 2014 勘误后的线性平移 specialization 及随 \(z_j\to0\) 的统一性为
[T/R]；这两项外部输入没有发现导致笔记 221--227 失效的缺口。完整记录级实例仍为
[C]，因为内部 Toeplitz/箱求和/常数拼装尚未全部完成独立复核。本笔记不更新 PDF。

## 1. 审计结论

本轮从笔记 228 的条件性常数反向检查两个最强的外部算术输入。

1. Bettin--Chandee 的 fixed-determinant Corollary 1 确实允许两个任意系数坐标
   \(n_1,n_2\) 和两个 derivative-controlled smooth 坐标 \(m_1,m_2\)。笔记 221
   的替换
   \[
   a=q_1m_1,\quad c=q_2m_2,\quad n_1=q_2b,\quad n_2=q_1d
   \]
   保持行列式 \(m_1n_2-m_2n_1=h\)，并给出所写的
   \(Y^{39/20+\varepsilon}\) 误差尺度。
2. 笔记 221 不是对两个坐标分别放一套 Selberg 平方权。它对单个带重数序列
   \(n=ac\) 筛 \((n,P(z))=1\)。因此展开只有一个 ordered pair
   \((d_1,d_2)\)，即 \(O(D^{2+\varepsilon})\) 的 remainder cost；把它误读成
   四个独立 divisors 而改成 \(D^4\) 是不正确的。
3. Henriot 原文确有 2014 勘误。上界定理中的 congruence factor 必须由
   \(\widehat\rho_R\) 换成 \(\check\rho_R\)，并在一般非首一多项式中把
   discriminant factor 从 \(D^*\) 换成 \(a^*D^*\)。本项目使用
   \(Q_1(n)=n,Q_2(n)=n+h\)，二者 primitive 且首一，故 \(a^*=1\)；又有
   \(\check\rho_R\le\widehat\rho_R\)，所以笔记 224、227 所需的 upper bound
   保持成立。
4. 权
   \[
   F_{z_1,z_2}(u,v)=z_1^{\Omega(u)}z_2^{\Omega(v)},\qquad0<z_j\le1,
   \]
   可统一放入同一个 \(\mathcal M_2(A,B,\varepsilon)\) 类：固定任意
   \(A,B>1\) 即可，因为新增 coprime factor 只乘不超过 \(1\) 的量。Henriot
   隐常数只依赖固定的 \(g,\alpha,\delta,A,B\)，不依赖 \(z_j\)。因此
   \(z_j\asymp1/\log\log R\) 的选择没有把一个发散常数藏进 \(o(N)\)。

结论是“这两个外部关节通过审计”，不是“整个四迹链已经通过”。

## 2. Bettin--Chandee 参数核对 [R/T]

一手来源为 Bettin--Chandee, *Trilinear Forms with Kloosterman Fractions*,
Corollary 1：

https://arxiv.org/abs/1502.00769

其误差为

\[
 (\eta\mathcal R)^{3/2}\|\alpha\|_2\|\beta\|_2
 (N_1N_2)^{7/20}(N_1+N_2)^{1/4+\varepsilon}
 (M_1M_2)^\varepsilon.
\tag{1}
\]

在 balanced box 中

\[
 M_1\asymp Y/q_1,\quad M_2\asymp Y/q_2,
 \quad N_1\asymp q_2Y,\quad N_2\asymp q_1Y,
\tag{2}
\]

而 arbitrary coefficient norms 满足

\[
 \|\alpha\|_2\|\beta\|_2\ll Y\log Y.
\tag{3}
\]

因此不计 \(q_j\) 的部分是

\[
 Y^{1+7/10+1/4+\varepsilon}\log Y
 =Y^{39/20+\varepsilon}\log Y.
\tag{4}
\]

两个 smooth weights \(w(q_jm_j/Y)\) 的第 \(r\) 阶导数是
\(O_r((Y/q_j)^{-r})\)，所以式 (1) 的 \(\eta\) 可一致取常数；没有随 sieve
level 增长。

此外，当 \(b,d\) 是不同且大于所有 sieve primes 的素数时，

\[
 (q_2b,q_1d)=(q_1,q_2),
\tag{5}
\]

故主项 density 精确为

\[
 \mathbf1_{(q_1,q_2)\mid h}\frac{(q_1,q_2)}{q_1q_2}.
\tag{6}
\]

这一步只在 moderate/balanced 区使用；extreme 区的短因子可能有共同底，已经由
笔记 222 的一参数 affine sieve 另行处理。

## 3. 为什么 remainder cost 是 \(D^2\) 而不是 \(D^4\) [T]

定义带重数的非负序列 \(A_n\)，其中 \(n=ac\)，其余变量和权重全部吸收到
\(A_n\) 中。对该**单序列**使用

\[
 \mathbf1_{(n,P(z))=1}
 \le\left(\sum_{d\mid(n,P(z))}\lambda_d\right)^2.
\tag{7}
\]

展开式 (7) 只有 \((d_1,d_2)\)，并令 \(q=[d_1,d_2]\le D^2\)。条件
\(q\mid ac\) 对每个 \(p\mid q\) 有

\[
 \mathbf1_{p\mid ac}
 =\mathbf1_{p\mid a}+\mathbf1_{p\mid c}
  -\mathbf1_{p\mid a,\,p\mid c}.
\tag{8}
\]

所以给定 \(q\) 只产生 \(3^{\omega(q)}\ll_\varepsilon q^\varepsilon\) 个
二坐标 divisibility sums，不会再产生另一对 Selberg divisors。由
\(q_1,q_2\le D^2\)，式 (1) 的 level cost 是

\[
 (q_1q_2)^{7/20}(q_1+q_2)^{1/4+\varepsilon}
 \ll D^{19/10+\varepsilon}.
\tag{9}
\]

与 ordered pair 数 \(D^{2+\varepsilon}\) 合并得到

\[
 D^{39/10+\varepsilon}.
\tag{10}
\]

故 \(D=Y^\kappa\)、\(\kappa<1/78\) 时，relative exponent

\[
 -\frac1{20}+\frac{39}{10}\kappa<0
\tag{11}
\]

严格闭合。这验证的是 level ledger；Bettin--Chandee 定理本身仍是外部输入。

## 4. Henriot 勘误后的 specialization [R/T]

一手来源：Henriot, *Nair--Tenenbaum bounds uniform with respect to the
discriminant*，以及 2014 erratum：

- https://arxiv.org/abs/1102.1643
- https://doi.org/10.1017/S0305004114000280

勘误明确说明：原 Theorem 5 的 upper bound 仍有效，但应以满足额外交叉
congruence 条件的 \(\check\rho_R\) 替换 \(\widehat\rho_R\)；一般多项式还要把
坏素数集合扩大到 leading coefficient \(a^*\) 的素因子。对于

\[
 Q_1(X)=X,\qquad Q_2(X)=X+h,
\tag{12}
\]

有 \(a^*=1\)，且两个多项式 primitive。修正后的局部因子由旧局部因子支配，
于是存在一个与 \(z_1,z_2\) 无关的常数 \(C\)，使

\[
 \Delta_{z_1,z_2}(h)
 \le \Delta_0(h):=\prod_{p\mid h}\left(1+\frac Cp\right).
\tag{13}
\]

展开正 Euler product 得

\[
 \Delta_0(h)=\sum_{d\mid h}\frac{C^{\omega(d)}}d
 \quad(d\text{ squarefree}),
\tag{14}
\]

从而

\[
 \sum_{h\le H}\Delta_0(h)
 \le H\sum_{d\ge1\atop d\text{ squarefree}}
 \frac{C^{\omega(d)}}{d^2}\ll_C H.
\tag{15}
\]

Abel summation再给

\[
 \sum_{h\le H}\frac{\Delta_0(h)}h\ll_C\log(2H).
\tag{16}
\]

因此笔记 224、227 使用的 shift average 仍成立。严格说，后续文档中的
\(\Delta(h)\) 应理解为式 (13) 的统一 majorant，而不是依赖 \(z_j\) 的原始
local factor。

## 5. 删除审计与剩余开放项

1. 删除 Bettin--Chandee 的 \(1/20\) saving，式 (11) 失去负幂，balanced 与
   moderate critical shell 不再由现有外筛闭合。
2. 若真对 \(a,c\) 分别放独立平方 Selberg 权，则 remainder ledger 会变成四
   divisor 展开；笔记 221 的证明依赖单序列 \(n=ac\) 的组织方式。
3. 删除 Henriot 的 discriminant uniformity，\(|h|\) 依赖可能在式 (15)--(16)
   前产生不可平均的常数，mixed \(3+1\) 与 \(E_j\)-prime 通道中断。
4. 删除 \(0<z_j\le1\) 的共同函数类控制，随 \(R\) 变化的参数可能使隐常数发散；
   本轮已明确排除此漏洞。
5. 本轮没有复核：笔记 209--220 的全部 local-energy 到 factor-box 组合、笔记
   224--227 的每个 Toeplitz cyclic orientation、以及 MT 窗口积分的独立高精度
   重算。因此 \(0.7569026\ldots\) 仍不得标为无条件纪录。

下一最小引理 A1i [O]：对笔记 199 的 paired-diagonal 常数和笔记 224--227 的
cyclic multiplicities做一次从原始 \((S_L+P)^4\) 展开出发的独立符号重建；要求
不调用已有常数拆分，最后再与 \(D_0,D_{\rm mix},D_{22}\) 比较。若出现系数或
orientation 重数差异，立即下调记录级实例。

## 6. 可复现检查 [E]

`scripts/external_input_reverse_audit.py` 检查：

1. local survival factor 在 \(p\nmid h\) 与 \(p\mid h\) 时分别为
   \(1-2/p\)、\(1-1/p\)；
2. 单序列 inclusion--exclusion 的三态恒等式；
3. \(39/20\)、\(19/10\)、\(39/10\) 与 \(1/78\) 的精确有理指数账本；
4. 有限截断上式 (14)--(15) 的 divisor expansion。

这些检查不实现 Bettin--Chandee 或 Henriot 定理，也不构成 RH 证据。

## 7. 后续推进（笔记 230）

笔记 230 已完成本笔记提出的 A1i：从六个 `2+2` sign words 与两种 pairing
枚举十二条 raw paths，独立恢复 `4A_++4A_-+4B`；从六个 mixed placements
恢复 `8C_1+4C_2`，并直接重算 MT 总常数 `0.252508968714...`。下一任务改为
A1j：内部 Fejer cone、factor-box 求和、finite crossing 与 frozen grid 的统一
原子集合审计。
