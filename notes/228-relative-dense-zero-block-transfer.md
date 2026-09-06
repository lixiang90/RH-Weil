# 228. 相对稠密高度到 AF 零点块的移动端点传递

日期：2026-09-02

分支：MOM-1 / 路线 A1g；接口：显式公式型部分 Weil 配置

状态：移动 Gabor 起点对应的零点块、相对稠密端点传递、中心矩到
rank--trace--inertia 证书的量词桥梁为 [T]；Alpöge--Furman 的零点侧
分解、tail、trace 与二矩定理为 [R]；以笔记 227 的 fourth-trace 上界为
前件得到的比例公式为 [T]；实际新比例仍为 [C]：后续审查已定位
fixed-power high-product 的合并有符号四阶算术预算尚未证明，不只是等待逆向审计。
笔记 203--227 的其他依赖仍需按具体覆盖范围复核。当前中心矩数据不能唯一确定
Christoffel 四矩证书为 [N]。

## 1. 审计结论

笔记 227 对每个长度

\[
 H_T=\frac{T}{\sqrt{\log T}}=o(T)
\tag{1}
\]

的 starting-height interval 给出一个 centered fourth-trace good point。
Alpöge--Furman 的压缩并不统计 \((0,t]\)；它统计由 Gabor grid 覆盖的移动块。
本轮证明这个区别不构成障碍。

令

\[
 L=\log(T/2\pi),\qquad X=e^L=\frac{T}{2\pi},\qquad
 h=\frac{2\pi}{L},\qquad d=\left\lfloor\frac{LT}{2\pi}\right\rfloor,
\tag{2}
\]

并令

\[
 B_T=dh=T+O(L^{-1}).
\tag{3}
\]

把原文的 grid 起点从 \(T\) 平移到 \(u\)：

\[
 \alpha_k(u)=u+kh,\qquad 0\le k<d.
\tag{4}
\]

它对应的主零点块是

\[
 J_u=[u,u+B_T),
\tag{5}
\]

zero-side 分解使用的 padded block 是

\[
 J_u'=[u-\sqrt T,u+B_T+\sqrt T).
\tag{6}
\]

若 \(u\in[T,T+H_T]\)，则

\[
 N(J_u\triangle[T,2T])
 \ll (H_T+1)\log T=o(T\log T)=o(N(T,2T)).
\tag{7}
\]

因此在每个短 interval 中只得到一个 good starting height 已足够把局部比例传回
固定 dyadic block \([T,2T]\)。不需要 pointwise-in-height fourth moment，也不
需要把 good points 先变成一个正密度集合。

## 2. 一手来源中的精确量词 [R]

Alpöge--Furman, arXiv:2608.13637v2 的对应位置是：

1. §2.2：\(\alpha_k=T+2\pi k/L\)、\(d=\lfloor LT/(2\pi)\rfloor\)，
   所以 grid 覆盖 \([T,2T)\)；
2. §2.3：主块 \(I=[T,2T)\)，padded block
   \(I'=[T-\sqrt T,2T+\sqrt T)\)，并定义
   \(\widetilde G\)、zero-side tail \(\widetilde E\)；
3. Proposition 4.1：on-line zeros 给正 rank-one 项，off-line pairs 的
   positive index 至多为 pair 数；
4. Propositions 4.2--4.3：
   \(\operatorname{tr}\widetilde G=N(I')+o(N)\) 与
   \(\|\widetilde E\|_1=o(1)\)；
5. Corollary 4.5：把 padded counts 换回 \(I\)，损失
   \(O(\sqrt T\log T)=o(N)\)；
6. Theorem 5.7：\(\|\widetilde G\|_{\rm HS}^2=R(\psi)N(T,2T)+o(N)\)；
7. §6：有限 rank--trace inequality 在同一个 block 内产生 simple/distinct
   counts；累计版本最后才由 dyadic summation 得到。

一手链接：

https://arxiv.org/html/2608.13637v2

把起点换成式 (4) 不改变 Poisson--Gabor identity，因为只给所有 grid modes
乘共同 modulation。prime-side 的 Montgomery--Vaughan bounds 也只改变单位
模 phase。Archimedean 项在 \(u\asymp T\) 上由 Stirling 一致；笔记 226 已对
更长的冻结区间证明这一点。因此上述零点侧与二矩误差对
\(u\in[T,T+H_T]\) 一致。

## 3. 移动块传递定理 [T]

对 interval \(J\)，记 \(N(J)\) 为按重数计的零点数，\(S(J)\) 为简单且位于
中心线的零点数，\(D(J)\) 为不同零点数。

### 定理 228-A（moving-start zero-block transfer）

设 \(H_T=o(T)\)。若每个充分大的 \(T\) 都存在
\(u_T\in[T,T+H_T]\)，使

\[
 S(J_{u_T})\ge (c-o(1))N(J_{u_T}),
\tag{8}
\]

则

\[
 \boxed{S(T,2T)\ge(c-o(1))N(T,2T).}
\tag{9}
\]

同一结论对 \(D\) 成立。

#### 证明

由 \(B_T=T+O(L^{-1})\) 与 \(0\le u_T-T\le H_T\)，

\[
 |J_{u_T}\triangle[T,2T]|\le 2H_T+O(L^{-1}).
\tag{10}
\]

标准局部计数 \(N(y,y+1)\ll\log(y+2)\) 给

\[
 N(J_{u_T}\triangle[T,2T])
 \ll(H_T+1)L=o(TL)=o(N(T,2T)).
\tag{11}
\]

目标计数在两个 interval 上的差的绝对值至多为式 (11)，总计数也同样。因此

\[
 \begin{aligned}
 S(T,2T)
 &\ge S(J_{u_T})-o(N(T,2T))\\
 &\ge cN(J_{u_T})-o(N(T,2T))\\
 &=cN(T,2T)-o(N(T,2T)).
 \end{aligned}
\]

不同零点计数的证明相同。\(\square\)

### 推论 228-B（cumulative transfer）[T]

式 (9) 若对每个充分大的 dyadic base height 成立，则

\[
 S(0,T)\ge(c-o(1))N(0,T),
\tag{12}
\]

且 \(D\) 同样成立。

证明：固定 \(\varepsilon>0\)，对所有高于统一阈值的 dyadic blocks 使用
\(c-\varepsilon\)，低端有限块贡献为 \(o(N(0,T))\)，再令
\(\varepsilon\downarrow0\)。\(\square\)

这比笔记 208-E 更贴合实际矩阵：208-E 传递的是 cumulative endpoint；本定理
传递的是 AF construction 真正使用的 moving block。

## 4. Good point 上的矩正规化 [T/R]

令

\[
 \mathcal B_u=\widetilde G_u+\widetilde E_u,
 \qquad \mathcal C_u=\mathcal B_u-I_d.
\tag{13}
\]

笔记 200 的 tail theorem 与笔记 227 在 good point 给出的
\(\|\mathcal C_u\|_4=O(N^{1/4})\) 蕴含

\[
 \operatorname{tr}(\widetilde G_u-I_d)^4
 =\operatorname{tr}\mathcal C_u^4+o(N).
\tag{14}
\]

另一方面，AF 的 trace、dimension 与二矩定理一致给

\[
 \frac d{N(J_u)}=1+o(1),\qquad
 \frac{\operatorname{tr}\widetilde G_u}{N(J_u)}=1+o(1),
\tag{15}
\]

\[
 \frac1{N(J_u)}\operatorname{tr}(\widetilde G_u-I_d)^2
 =b_2(\psi)+o(1),
 \qquad b_2(\psi)=R(\psi)-1.
\tag{16}
\]

式 (16) 只是恒等式

\[
 \operatorname{tr}(G-I)^2=\operatorname{tr}G^2-2\operatorname{tr}G+d
\tag{17}
\]

与式 (15) 的组合。所有量都属于同一个 \(J_u\)，不存在用 base block 的
零点计数正规化 shifted matrix 的混用。

## 5. 中心四矩到比例的量词桥梁 [T]

设在 good point 上

\[
 \frac1{N(J_u)}\operatorname{tr}(\widetilde G_u-I_d)^4
 \le B_4+o(1).
\tag{18}
\]

2026-09-06 补齐前提：采用 [306](306-quartic-boundary-and-equal-norm-corrections.md)
与论文中的含误差证书。除式 (15) 的维数和迹归一化外，必须有同一配置的
\(E_{1,u}=o(N(J_u))\)，并且对选点范围一致。AF padded block 的重数账本
在 padded count 下给 \(s+2b\le N(J_u')\)；换回 \(J_u\) 所付
\(N(J_u'\setminus J_u)=O(\sqrt T\log T)=o(N)\) 正是这项边界误差。
须先把证书应用于 padded 配置的 \(s=S(J_u')\)、\(D=D(J_u')\)，再用
\[
|S(J_u')-S(J_u)|,\ |D(J_u')-D(J_u)|\le N(J_u'\setminus J_u)=o(N).
\]
有限层的分子损失也必须支付，不能只调整 \(E_1\) 就把 padded 计数改名为主块计数。
若另行修改配置或截断规则，必须重新核查，不能仅凭四矩数据删除该项。

置 \(v=b_2(\psi)\)，要求 \(0\le v<1\)。笔记 197 的一侧 quartic 证书给

\[
 \boxed{
 \frac{S(J_u)}{N(J_u)}
 \ge \kappa_4(v,B_4)-o(1),
 \qquad
 \kappa_4(v,B_4)=\frac{(1-v)^2}{1-2v+B_4},}
\tag{19}
\]

以及

\[
 \boxed{
 \frac{D(J_u)}{N(J_u)}
 \ge\frac{1+\kappa_4(v,B_4)}2-o(1),}
\tag{20}
\]

只要

\[
 1-2v+B_4>0,
 \qquad \frac{v-B_4}{1-v}<\frac34.
\tag{21}
\]

这里允许的是 fourth-moment upper bound，不要求等号：在 quartic dual 中把
实际中心四矩替换为较大的 \(B_4\) 只会放松右侧。结合定理 228-A，式
(19)--(20) 自动传到固定 \([T,2T]\)，再由推论 228-B 传到累计计数。

二矩 rank--trace 常数是

\[
 \kappa_2(v)=1-v.
\tag{22}
\]

若 \(B_4<v<1\)，则

\[
 \kappa_4(v,B_4)>\kappa_2(v),
\tag{23}
\]

因为式 (23) 精确等价于 \(v>B_4\)。所以改进判据在中心矩记号下只是
“中心四矩严格小于中心二矩”，并非必须匹配完整 sine-kernel 四矩。

## 6. Montgomery--Taylor 实例化 [C]

对 Montgomery--Taylor 窗，AF 的无条件二矩给

\[
 v_{\rm MT}
 =-\frac12+\frac1{\sqrt2}\cot\frac1{\sqrt2}
 =0.327499296320588\ldots.
\tag{24}
\]

笔记 227 的 fourth-trace 前件是

\[
 B_{\rm MT}=0.252508968713594\ldots.
\tag{25}
\]

于是

\[
 \sigma_* =\frac{v_{\rm MT}-B_{\rm MT}}{1-v_{\rm MT}}
 =0.111509664148609\ldots<\frac34,
\tag{26}
\]

\[
 \boxed{
 \kappa_4(v_{\rm MT},B_{\rm MT})
 =0.756902665727919\ldots,}
\tag{27}
\]

\[
 \boxed{
 \frac{1+\kappa_4}2
 =0.878451332863959\ldots.}
\tag{28}
\]

逻辑状态必须分两层：

1. “若笔记 227-I 的 uniform relative-dense fourth-trace bound 成立，则
   式 (27)--(28) 的 local 与 cumulative 比例成立”是本轮完整证明的 [T]；
2. 把式 (27) 宣布为新的无条件 zeta 纪录仍标 [C]。原因不是 zero-block
   coverage；本轮已经闭合该接口。2026-09-06 修订：实际合并有符号的
   fixed-power high-product fourth-trace 预算仍是未证数学输入；
   pure-prime、Henriot specialization、finite-to-bulk 和尺度求和的
   其他已核查部分不能填补它。

在该复核完成前，不在摘要、README 或论文标题中写“改进纪录”。

## 7. 为什么当前数据不能直接声称 \(13/18\) [N]

AF §7.2(d) 的 degree-two Christoffel function 使用完整 raw moments

\[
 (m_0,m_1,m_2,m_3,m_4).
\tag{29}
\]

当前得到的是 \(m_1=1+o(1)\)、中心二矩 \(v\) 和中心四矩 upper bound
\(B_4\)。它没有给中心三矩或 raw \(m_3\)，因此不能把 sine-kernel 的
\(\Lambda_2(0)=5/36\) 直接代入。

这个信息缺口是严格的。令

\[
 q=\frac{v^2}{B_4},\qquad a=\sqrt{\frac{B_4}{v}}.
\tag{30}
\]

概率测度

\[
 \mu_{\rm sym}=(1-q)\delta_1+\frac q2\delta_{1-a}
 +\frac q2\delta_{1+a}
\tag{31}
\]

具有均值 \(1\)、中心二矩 \(v\)、中心四矩 \(B_4\)，中心三矩为零。
另一方面，取 \(p\in(0,1/2)\) 使

\[
 \frac{B_4}{v^2}
 =\frac{(1-p)^2}{p}+\frac{p^2}{1-p},
\tag{32}
\]

并令

\[
 A=\sqrt{\frac{v(1-p)}p},\qquad
 C=\sqrt{\frac{vp}{1-p}},
\tag{33}
\]

则

\[
 \mu_{\rm skew}=p\delta_{1+A}+(1-p)\delta_{1-C}
\tag{34}
\]

有同样的均值、中心二矩和中心四矩，但中心三矩非零。对 MT 数值，

\[
 p=0.2485379985\ldots,qquad
 \int(x-1)^3d\mu_{\rm skew}=0.2181061992\ldots.
\tag{35}
\]

两组 raw \(m_3\) 不同，degree-two moment matrix 和
\(\Lambda_2(0)\) 因而不同。特别地，\(\mu_{\rm skew}\) 只有两个不含零的
support points，存在 degree-two polynomial 在 support 上为零而在 \(0\) 为
一，所以其 \(\Lambda_2(0)=0\)；而三点测度 \(\mu_{\rm sym}\) 的对应值为
\(0.1395279987\ldots\)。

所以当前中心偶矩数据不决定 AF 的 \(13/18\) Christoffel 数值。可用的正确
接口是式 (19) 的 rank--trace--inertia certificate，而不是补写一个未证明的
第三矩渐近。

## 8. 最小公理与删除审计

1. **移动 grid 的精确定义**：把 good height 解释为 starting point。
   删除它就无法知道矩阵统计哪个零点块。
2. **局部零点计数 \(N(y,y+1)\ll\log y\)**：把长度 \(o(T)\) 的 endpoint
   displacement 变成 \(o(N)\)。删除后 relative-dense points 不自动覆盖固定块。
3. **同一矩阵上的 trace、二矩、四矩**：quartic certificate 不能把不同高度
   或不同 grid 的 moments 拼在一起。
4. **zero-side tail 的 Schatten 稳定**：把 full explicit-formula matrix 的
   fourth trace 传给 finite zero matrix。删除后 prime-side good point 不一定
   控制惯性矩阵。
5. **rank--trace--inertia quartic dual**：只使用中心二、四矩和 zero-side block
   账本；它不假装拥有缺失的第三矩。

## 9. 循环性与模型范围

- moving-block transfer 只用零点局部计数，不使用 RH、零密度或零自由区域。
- quartic finite certificate 是线性代数，不把正性作为公理；off-line pairs 仍由
  函数方程的 \((1,1)\) 惯性块处理。
- 固定本原 Dirichlet \(L\) 函数具有相同的 block transfer，局部计数和 Gamma
  shift 的常数只依赖固定 conductor。
- Dedekind/automorphic 情形需要对应的 local zero count、functional-equation
  pairing 与 uniform moving-grid moment estimates。
- 本轮只连接显式公式型配置，不建立到上同调型 Weil 结构的桥梁。

## 10. 下一最小引理 [O]

路线 A1h：从最终常数反向审计笔记 203--227。按依赖的逆序逐式检查：

1. 227-I 的 whole-trace averaging 是否确实得到同一 \(u_T\)；
2. 225 的 pure-prime finite fourth bound 是否对 anchored moving grid 一致；
3. 224 的 signed first means 是否在所有 dyadic ranges 有可求和的 uniform error；
4. 223 的 Hilbert-valued mean value 是否保持 \(H=T/\sqrt L\) 的常数；
5. 221--222 对 critical determinant shell 的 box summation 是否漏失
   logarithmic multiplicity；
6. 217 的 Henriot 参数族、判别式因子与 bounded-mean 常数是否对随
   \(L\) 变化的 \(z_j\) 真正一致。

任一处若只能给 \(O(N)\) 而非 \(o(N)\)，立即把式 (27)--(28) 降为开放并记录
最小缺失估计；只有整条链通过独立复核后才晋级为无条件比例定理。

## 11. 可复现检查 [E]

脚本 `scripts/relative_dense_zero_block_audit.py` 检查：

1. AF grid length \(dh=T+O(1/L)\)；
2. endpoint displacement 相对 \(N\asymp TL\) 为 \(O(H/T)=o(1)\)；
3. raw-to-centered second/fourth trace identities；
4. MT 的 \(v\)、\(B_4\)、\(\sigma_*\)、simple/distinct constants；
5. 式 (31)、(34) 的相同偶中心矩与不同三阶矩；
6. 两个 moment sequences 的 Christoffel 数据确实不同。

脚本不证明笔记 227-I，也不执行零点计算；它只审计本轮的量词桥梁和有限代数。

## 13. 后续 prime-side 漏区修正（笔记 232）

moving-block transfer 与 quartic inertia implication 保持 [T]。笔记 232 证明其
prime-side 输入链仍缺 `ab>XL^2` alternating primitive off-diagonal；所以本笔记
给出的 simple/distinct 数值仍严格标为 [C]，不能据当前链宣称无条件纪录。
