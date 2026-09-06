# 反向大值定理的原始范围与下一路线准入

2026-09-07。主线程原始条款核查及自含推导候选，独立审查待完成。
本记录不认证整个ANTEDB，也不修改外部原件。

## 来源与实际核读

- Matomäki–Teräväinen，arXiv:2403.13157v1，16页；
  [版本](https://arxiv.org/abs/2403.13157v1)，
  [本地原件](../../literature/background/matomaki-teravainen-density-to-large-values-2403.13157v1.pdf)。
  2026-09-07版本页只列v1。SHA-256为43b9a4dfe32437909ac948d2146ac4b3aa787a3155a5cba1c77abeddb1453d49。
  主线程读第1–9页，重点Theorem1.2、Remark1.3、Lemmas2.1–2.6、4.1及原始量词；
  第10–16页和所引全部分析证明尚未核读。
- ANTEDB，2026-09-05封面、2026-09-06取得的190页快照，
  [原件](../../literature/background/antedb-blueprint-20260906.pdf)。
  本次核对PDF第38、45–47、83–84、104页的定义、反射、Lemma11.6与比较表。
  [当前网页](https://teorth.github.io/expdb/blueprint/zero-density-chapter.html)2026-09-07仍将Lemma11.6写为tau>0。
- TTY v1第17–18、27、29–31页复读。其Theorem51的局部补证见[328](../../notes/328-tty-thm51-proof-repair-and-scope.md)。

## 1. 原定理控制的是短多项式的测度

Matomäki–Teräväinen Theorem1.2（第2页）对0<=nu<=1/2、epsilon>0，
控制所有|t|<=T中，存在M in [T^epsilon,T^(1/2)/2]、
M<M'<=2M使
|sum_{M<n<=M'}n^(-1-it)|>=M^-nu的t集合的Lebesgue测度，界为
\[
 T^\varepsilon\max_{1-\nu-\varepsilon\le\alpha\le1}
 T^{(\alpha-(1-\nu))/2}N(\alpha,C_\varepsilon T)
 +T^{\nu/2+\varepsilon}.                               \tag{1}
\]
N按原始零点重数计数。测度含全部可能M和端点的并集。
不能直接称为任意长度、任意系数、任意一分离集合的定理。
Remark1.3对prime/Möbius多项式的讨论还引入T^(2nu+2epsilon)项，
而且须完成Heath-Brown分解及短因子的账本，不能免费保留(1)的nu/2余项。

## 2. 一分离点到测度的无幂损失桥梁

固定1/2<sigma<1、tau>=2。取zeta大值pattern：
T=N^(tau+o(1))，I subset [N,2N]为一个固定区间，
W subset [T,2T]一分离，且每个t_r in W有
|sum_{n in I}n^-it_r|>=N^(sigma-o(1))。

将端点单位项吸收后，写I=(M,M']，M asymp N、M'<=2M。
分部求和给某端点u<=M'满足
|sum_{M<n<=u}n^(-1-it_r)|>=N^(sigma-1-o(1))。
若|h|<=1/4，再对n^-ih作分部求和，有
\[
 \left|\sum_{M<n\le u}n^{-1-it_r}\right|
 \le(1+|h|\log2)
       \max_{M<v\le u}\left|\sum_{M<n\le v}n^{-1-i(t_r+h)}\right|. \tag{2}
\]
允许变化端点正是(1)所控制的事件。对任意小固定delta>0，
nu=1-sigma+delta<1/2，充分大N时每个[t_r-1/4,t_r+1/4]
都在阈值M^-nu事件中；这些区间不交，总测度为|W|/2。

取T'=16max(T,N²)，则T'=N^(tau+o(1))、|t_r+h|<=T'、
M<=sqrt(T')/2；对充分小固定epsilon，M>=(T')^epsilon。
因此(1)适用于T'。先N趋无穷，再令delta、epsilon趋零，不损失T的固定幂。
这证明短多项式事件到一分离pattern的桥梁，未把任意系数偷偷改成1。

例如，若一个固定连续函数f在[sigma-delta_0,1]上为实际零计数提供
N(alpha,T)<<_{alpha,epsilon}T^(f(alpha)+epsilon)，
则有限网格加N对alpha单调性与f的一致连续性给
\[
 {\mathrm{LV}_\zeta(\sigma,\tau)\over\tau}
 \le\max\left({1-\sigma\over2},
       \sup_{\sigma\le\alpha\le1}
            \{f(\alpha)+(\alpha-\sigma)/2\}\right),
 \qquad \tau\ge2.                                      \tag{3}
\]
网格常数有限，所有端点都固定在T极限前；不假定逐alpha渐近自动一致。
(3)只是原定理的明确推论，不宣称新大值原理。

## 3. ANTEDB的“所有tau>0”不能按字面使用

快照Lemma11.6写
LV_zeta(sigma,tau)/tau<=max(1/2,sup_{sigma<=alpha<=1}
{A(alpha)(1-alpha)+(alpha-sigma)/2})，并列tau>0。
Definition7.1和8.1确实允许全部tau>=0，没有隐藏tau>=2。

下面给该全范围版本的反例，针对实际纯系数Dirichlet多项式，不是合成零点模型。
取整数N->infinity、T=N^(1/8)、I=(N,2N]。
一阶积分比较一致于T<=t<=2T给
\[
 \sum_{N<n\le2N}n^{-it}
 =N^{1-it}{2^{1-it}-1\over1-it}+O(1+t).
\]
误差由端点和integral |(x^-it)'| dx<=t log2得到。
因|2^(1-it)-1|>=1，主项绝对值>=N/sqrt(1+4T²)，
而T²/N->0，故充分大N时整个和至少N/(4T)。
取W=Z intersect [T,2T]，V=N/(4T)=N^(7/8+o(1))，
得到合法zeta大值pattern，|W| asymp T。
结合平凡上界，LV_zeta(7/8,1/8)=1/8，其与tau之比为1。

另一方面，用已采用的Huxley实际密度界
f(alpha)=3(1-alpha)/(3alpha-1)，alpha>=7/8。
f(alpha)+(alpha-7/8)/2严格递减，因为导数
-6/(3alpha-1)²+1/2<0。故上述sup至多f(7/8)=3/13，
印刷右端为1/2，小于1，矛盾。

因此**Lemma11.6的全tau范围按所列定义不成立**。
这不是对Matomäki–Teräväinen Theorem1.2的反例：这里N远大于sqrt(T)，
正好违反其长度范围。也不否定tau>=2的合法推论。
1<tau<2若要使用反射，须保留Definition8.3(iv)中的sup和阈值损失；
不能直接把脚注所称“morally”简式当作精确定理。

## 4. 两项不应继续寻优的直接拼接

**仅重新优化TTY五项中的alpha。** 记其五项为F1,...,F5。
对任意alpha1,alpha2>=0，两个非负凸组合给
\[
 {F_2\over2}+{F_3\over4}+{F_4\over4}
 ={3\tau\over4}+5-7\sigma,
\]
\[
 {2F_4\over3}+{F_5\over3}
 \ge {2\tau\over3}+9-12\sigma,
\]
第二式只用max(1,2tau-2)>=1。
所以若在tau=tau0用这五项的最大值认证LV<=3-3sigma，
必有tau0<=min(8(2sigma-1)/3,9(3sigma-2)/2)。
这正是328已恢复的端点。换alpha不能让这套端点认证超过它。
这不限制改用其他大值定理、不同检测器或非此端点的归约。

**仅将同一零密度界反向反馈。** (3)的sup包含alpha=sigma，
所以其右端>=f(sigma)。单靠f -> (3) -> 常规大值上界拼接不会自动产生
比f(sigma)更小的数；需要另外的独立信息。
这是此直接代入账本的判定，不排除与其他有效不等式组合产生改进。

## 5. 对MOM的准入结论

当前balanced factor长度N=X^(3/4)、平均高度尺度X对应tau=4/3，
没有直接进入(1)的短长度范围。实际系数为von Mangoldt及六窗乘积，
也不是原定理的纯系数区间和。
即使先证明某个大值上界，仍须控制238的完整有符号、
已减去对角项的物理响应；正能量上界本身不能替代该差。

所以目前不把该来源当作MOM缺口已补齐，也不因“反向”二字重启纯反馈寻优。
下一有限问题若沿此方向，必须明确并证明新的长度转换、实际系数转换或新的带符号输入。
当前文件是文献辅助及准入审计；未产生新零密度值，不触发整个GOAL完成。
