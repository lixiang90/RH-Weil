# 202. Archimedean localizer 非构造补全与标量四矩 no-go

日期：2026-09-01

状态：65 维精确反例和 abstract localizing completion 为 [T]；数域 arithmetic
operator system 的统一近正性与 divisor visibility 为 [O]。

## 1. 问题

能否不具体构造数域的 Hilbert--P\'olya 空间，而由每个有限层次的可满足性
非构造地推出一个“类 Weil 结构”存在？

答案分成两部分：

1. 只给标量前四矩，严格不可能推出完整正性；
2. 若让 arithmetic word localizers 随层次增长，并有 Archimedean 一致界，
   则有限可满足性通过紧致性确实推出一个全局 tracial positive representation。

所以非构造路线可行，但正确对象必须是 matrix-valued localizing hierarchy，
而不是一次性的四个标量矩。

## 2. 一个精确的标量四矩 no-go [T]

定义两个概率测度

\[
 \mu_+
 =\frac3{13}\delta_{1/5}
 +\frac9{13}\delta_{3/5}
 +\frac1{13}\delta_1,
\tag{1}
\]

\[
 \mu_-
 =\frac1{65}\delta_{-1/5}
 +\frac8{13}\delta_{2/5}
 +\frac{24}{65}\delta_{4/5}.
\tag{2}
\]

它们分别是两个 \(65\times65\) 对角 Hermitian 矩阵的归一化谱测度；
重数分别为

\[
 (15,45,5),\qquad (1,40,24).
\]

### 定理 AEI（degree-four indistinguishability）

对 \(0\le k\le4\)，

\[
 \int x^k\,d\mu_+(x)=\int x^k\,d\mu_-(x),
\tag{3}
\]

共同矩为

\[
 1,\quad \frac7{13},\quad \frac{109}{325},
 \quad \frac{371}{1625},\quad \frac{1357}{8125}.
\tag{4}
\]

两矩阵维数相同，算子范数分别为 \(1\) 与 \(4/5\)，共同上界为 \(1\)；
第一矩阵正定，第二矩阵有一个负特征值。任取多个直和后，负谱比例仍为 \(1/65\)。
2026-09-06 勘误：旧版“范数同为 1”不成立。

若要求实际范数完全相同，取
\(\widehat H_\pm=H_\pm\oplus[1]\)。这是两个 66 维、范数同为 1 的矩阵，
共同归一化矩为 \(\widehat m_k=(65m_k+1)/66\)，负谱比例为 \(1/66\)。
65 维局部化证书仍针对原测度；66 维中同一多项式仍给严格负值，
但须重新计算归一化积分，不能照搬旧常数。精确验证及影响范围见
[306](306-quartic-boundary-and-equal-norm-corrections.md)。

证明只需检查六点有理恒等式

\[
 -\left(-\frac15\right)^k
 +15\left(\frac15\right)^k
 -40\left(\frac25\right)^k
 +45\left(\frac35\right)^k
 -24\left(\frac45\right)^k
 +5=0
\]

对 \(0\le k\le4\) 成立。

### 推论

任何只依赖维数、统一算子范数和
\(m_0,\ldots,m_4\) 的抽象 extension/compactness 定理，都不能把有限 Gabor
四矩提升为完整 Weil 正性。

甚至一阶 \(h\)-localizer

\[
 M_h^{(1)}=
 \begin{pmatrix}m_1&m_2\\m_2&m_3\end{pmatrix}
\tag{5}
\]

对两者相同且正定，因为

\[
 \det M_h^{(1)}=\frac{1104}{105625}>0.
\]

但二阶 localizer 已能检测 \(\mu_-\)。取

\[
 p(x)=\left(x-\frac25\right)\left(x-\frac45\right),
\]

则

\[
 \int xp(x)^2d\mu_-(x)=-\frac9{8125}<0.
\tag{6}
\]

这清楚说明需要增长的 word/localizer 层次，或额外的 flatness/递推关系。

## 3. Archimedean localizing completion [T]

令 \(\mathcal A_0\) 是具有可数 word 张成集的幺正复 \(*\)-代数，完全由 primes、Gamma、
continuum、shift/window projection 或其他零点无关 correspondences 生成。
令 \(Q\subset\mathcal A_{0,h}\) 为 Archimedean quadratic module：对每个
\(a\in\mathcal A_0\)，存在 \(R_a<\infty\) 使

\[
 R_a^2-a^*a\in Q.
\tag{7}
\]

令 \(h=h^*\in\mathcal A_0\) 为 bounded Hodge current，并令
\(\lambda(e)\) 是在可数 arithmetic word family \(E\) 上预定的 length-side
moments。

### 定理 AEJ（finite satisfiability completion）

假设对每个有限约束集 \(F\)、每个 \(n\ge1\)，都存在定义在包含
\(F\) 所涉全部 words 的有限维 \(*\)-空间上的线性泛函 \(L_{F,n}\)，使：

1. \(L_{F,n}(1)=1\)，所选 \(*\)-关系、迹关系
   \(L(ab)=L(ba)\) 的误差不超过 \(1/n\)；
2. 每个被选中的 Gram 与 \(Q\)-localizing matrix 半正定到误差 \(1/n\)；
3. 对所选 words \(u_1,\ldots,u_r\)，

   \[
   [L_{F,n}(u_i^*hu_j)]_{i,j}
   \succeq-\frac1n[L_{F,n}(u_i^*u_j)]_{i,j};
   \tag{8}
   \]

4. 对所选 \(e\in E\)，
   \(|L_{F,n}(e)-\lambda(e)|\le1/n\)。

则存在一个全局 tracial state \(L\) 和 GNS 表示
\((\pi,H,\Omega)\)，满足

\[
 L(e)=\lambda(e)\quad(e\in E),\qquad \pi(h)\succeq0.
\tag{9}
\]

### 证明

2026-09-06 独立审查修正：有限近似泛函不能直接使用精确界。
固定一个可数线性基。对任意有限基坐标集 \(K\)，加入每个坐标 \(a\) 的 \(\{1,a\}\) Gram 及
\(R_a^2-a^*a\in Q\) 的标量约束与所涉 words。矩阵不等式取 Hermitian part；
先将泛函换为 \(\widetilde L(x)=(L(x)+\overline{L(x^*)})/2\)，不改变趋零误差。
对 \(\epsilon=1/n\le1\)，有
\[
|\widetilde L(a)|^2\le(1+\epsilon)(\widetilde L(a^*a)+\epsilon)
\le(1+\epsilon)(R_a^2+2\epsilon)\le2(R_a^2+2).
\]
不能由可数 word 张成推断 \(Q\) 的约束集可数。因此使用有向网，
按三元组 \((K,F,n)\) 索引：\(K\) 是有限基坐标集，\(F\) 是任意有限约束集，
\(K\) 包含 \(F\) 涉及的全部基坐标，按包含关系及 \(n\) 的大小排序。
在调用有限可满足性时另加入 \(K\) 的上述坐标界及其辅助 words。
只记录 \(K\) 中已获界的坐标，其他坐标补零；不要求所有辅助 words 同时已获界。
这些点都在固定紧圆盘的可数乘积中，紧致性给收敛子网。
每条固定约束都在原网中最终包含，误差趋零；收敛子网保留这一性质。
每个约束只依赖有限坐标且闭，故极限满足全部精确约束，包括不可数的 \(Q\)。
此时才恢复精确界 \(|L(a)|\le R_a\)。

Gram 与 \(Q\)-localizer 的正性在极限下保持，所以 \(L\) 是 tracial positive
functional。GNS 构造给

\[
 \langle\pi(h)\pi(p)\Omega,\pi(p)\Omega\rangle
 =L(p^*hp)\ge0
\]

对所有 \(p\in\mathcal A_0\) 成立。由 quadratic module 对 \(p^*(\cdot)p\) 封闭，式 (7) 给 \(L(p^*a^*ap)\le R_a^2L(p^*p)\)，保证各 \(\pi(a)\) 有界，故
\(\pi(h)\succeq0\)。预定 arithmetic moments 也由闭性保留。

该结论与 truncated tracial moment/flat-extension 理论方向一致；参见
Burgdorf--Klep, arXiv:1001.3679，以及 Mourrain--Schm\"udgen,
arXiv:1406.4975。这里使用的是直接的 Archimedean 紧致性，而不是假定低阶
flat extension。

## 4. 失败时的有限证书 [T]

若全局交为空，紧致性反面说明已有某个有限 word level 不可满足。该层是有限维
带坐标界的凸可行性问题；分离定理给有限分离证据。若要求可计算的 SDP/SOS 证书，仍须给该层编码、对偶性和精度条件，不能仅由紧致性声称已有可运行证书。因此该路线具有二分性：

- 可满足：非构造地产生全局 tracial representation；
- 不可满足：在有限层产生明确的 arithmetic obstruction。

这比“假设存在所需 Hilbert 空间”更可审计，因为每次失败都必须落在有限 mixed
moment identity 上。

## 5. 与 RH 的非循环接口 [C/O]

定理 AEJ 只产生 abstract positive representation。要成为数域上的完整 Weil
配置，还必须另证：

1. \(\mathcal A_0,Q,h\) 及所有 moments 只由 length side 构造，不能用 zeros；
2. 用 bounded resolvent 或 Cayley-transform moments 编码 divisor visibility；
3. 这些 resolvent constraints 在紧致极限中保持；
4. word family 的闭包确实看见每个可能的负 divisor direction；
5. 得到的 tracial determinant/Weierstrass product 恢复目标 Gamma--Euler
   divisor。

若把“全部 Weil tests 已正”直接列入有限约束，前提仍与 RH 等价，紧致性没有
降低难度。真正可能较弱的新输入是：找到一个小而代数闭合的 arithmetic
operator system，使其 mixed localizer 正性可由 Type I/II、Gamma 与 continuum
恒等式推出，而闭包自动给 divisor visibility。

## 6. 下一步有限实验

在 finite Gabor coefficient space 上选择零点无关生成元

\[
 \{\text{shift},\ \text{window projection},\
 \ \text{prime incidence},\ \text{Gamma/continuum response}\},
\]

并计算

\[
 G_{T,r}=[\tau_T(u_i^*u_j)],\qquad
 H_{T,r}=[\tau_T(u_i^*h_Tu_j)].
\tag{10}
\]

优先检查是否有与 \(T\) 无关的 flatness/递推；若没有，则目标改成

\[
 H_{T,r}\succeq-\varepsilon_rG_{T,r},
 \qquad \varepsilon_r\to0,
\tag{11}
\]

并逐层记录 SDP dual separator 是否仍落在可估计的 Type I/II word cone。

审计脚本 scripts/operator_fourth_localizer_audit.py 用精确有理数验证
式 (3)--(6)。
