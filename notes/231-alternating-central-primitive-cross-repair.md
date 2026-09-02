# 231. Alternating 中心块交叉缺口与短高度修复

日期：2026-09-02

分支：MOM-1 / 路线 A1j；接口：pure-prime (2+2) alternating Gram

状态：笔记 209--225 的旧拼接未控制中心 ratio block 与 primitive hard core
交叉项为 [N]；该交叉项的任意短区间 signed mean 由已审计 shifted prime-pair
上界闭合为 [T/R]。本笔记只修复 central--noncentral component；笔记 232 证明
完整 primitive ledger 仍缺 `ab>XL^2` 高乘积 off-diagonal [O]。
本笔记不更新 PDF，也不把记录级比例从 [C] 晋级。

## 1. 逆审计结论

令

\[
 b_n=-\frac1{2\pi}\frac{\Lambda(n)}{\sqrt n},
 \qquad
 R_t(n)=\beta_L e^{it\log n}T_d(q_{\log n})D_d(\log n),
\tag{1}
\]

其中 (L=\log X)、(d\asymp XL)、
(\beta_L\asymp L^{-1})。alternating response 按 ratio 聚类为

\[
 F_\rho(t)=
 \sum_{a/b=\rho}b_ab_bR_t(a)R_t(b)^*.
\tag{2}
\]

笔记 209 的 prime-power multiplicity classification 把 clusters 分成：

1. 中心块 (F_1)，由全部 ((n,n)) 组成；
2. 非中心同素数底 chains；
3. 不同素数底的 primitive singleton clusters。

旧拼接把笔记 210--222 解释为闭合第三类内部的全部 off-diagonal，笔记 209-C
使第二类 aggregate 为 (o(N))。笔记 232 后来证明前一解释实际只覆盖
`ab<=XL^2`；但无论 primitive 内部是否已闭合，完整 alternating Gram 还含

\[
 \left\|F_1+F_{\rm ch}+F_{\rm pr}\right\|_{\rm HS}^2
\tag{3}
\]

还含

\[
 \boxed{
 C_{1,\ne1}(t)=
 2\operatorname{Re}
 \left\langle F_1(t),F_{\rm ch}(t)+F_{\rm pr}(t)\right\rangle_{\rm HS}.}
\tag{4}
\]

笔记 209 第 1 节明确把 central--primitive cross response 列为开放项；后续
笔记没有给式 (4) 的估计。把“central 与 same-prime 由独立预算处理”解释成
式 (4) 已闭合是不成立的：分别控制两个向量的平方范数只给 (O(N)) 的
Cauchy 上界。

本轮先把这个遗漏标为严格拼接缺口 [N]，再证明它事实上可由项目已有的
prime-pair 输入修复。

## 2. 旧预算不蕴含中心交叉小量 [N]

### 障碍命题 231-A（separate block budgets do not control the cross）

下列信息本身不推出
(2\operatorname{Re}\langle F_1,F_{\rm pr}\rangle=o(N))：

\[
 \|F_1\|^2=O(N),\qquad
 \|F_{\rm pr}\|^2=
 \sum_{\rho\in\mathcal P}\|F_\rho\|^2+o(N),
 \qquad
 \sum_{\rho\in\mathcal P}\|F_\rho\|^2=O(N).
\tag{5}
\]

#### 证明

取二维 Hilbert 空间与 (N=M^2)。令 (F_1=Me_1)，并令 primitive family
只有一个 atom。若该 atom 为 (Me_1)，则式 (5) 全部成立，而交叉项为
(2N)；若该 atom 为 (Me_2)，同样的所有 separate budgets 成立，而交叉项
为零。故式 (5) 不决定交叉项，更不推出 little-oh。\(\square\)

该反例不是 zeta 的 lower bound；它只证明旧拼接的逻辑输入不足。

## 3. 中心块的精确相位结构

由式 (1)，中心块的 carrier phase 完全消失：

\[
 F_1(t)=F_1=
 \sum_{n\le X}b_n^2R_0(n)R_0(n)^*,
\tag{6}
\]

这里 (R_0(n)) 表示删去 scalar (e^{it\log n}) 后的矩阵。对任意
(a\ne b)，

\[
 b_ab_bR_t(a)R_t(b)^*
 =e^{it\log(a/b)}C_{a,b},
\tag{7}
\]

其中 (C_{a,b}) 在冻结 (X,L,d) 后与 (t) 无关。因此式 (4) 是一个
ratio Dirichlet polynomial 的实部，而不是任意 Hilbert-space cross term。

对长度 (H) 的 interval (I)，记

\[
 K_I(u)=\frac1H\int_Ie^{itu}\,dt,
 \qquad
 |K_I(u)|\le\min\left(1,\frac2{H|u|}\right).
\tag{8}
\]

每个 (R_0(n)) 满足

\[
 \|R_0(n)\|_{\rm op}\le\beta_L,
\tag{9}
\]

所以

\[
 \left|
 \operatorname{tr}{R_0(n)R_0(n)^*C_{a,b}^*\}
 \right|
 \le d\beta_L^4|b_ab_b|.
\tag{10}
\]

将式 (10) 对中心系数求和，只需

\[
 \sum_{n\le X}|b_n|^2\ll L^2.
\tag{11}
\]

## 4. Ratio kernel 的 shifted-prime 预算 [T/R]

定义

\[
 \mathcal P_H(X)=
 \sum_{\substack{a,b\le X\\a\ne b}}
 \frac{\Lambda(a)\Lambda(b)}{\sqrt{ab}}
 \left|K_I\!\left(\log\frac ab\right)\right|.
\tag{12}
\]

### 引理 231-B（short-height prime-ratio kernel）

若 (H=X/\sqrt L)，则

\[
 \boxed{
 \mathcal P_H(X)
 \ll L^{3/2}(\log L)^2.}
\tag{13}
\]

#### 证明

先取 (a,b\asymp R)。写 (a=b+h\ne b)。由 mean-value theorem 与
式 (8)，

\[
 \left|K_I\!\left(\log\frac ab\right)\right|
 \ll\min\left(1,\frac{R}{H|h|}\right).
\tag{14}
\]

笔记 227-E 已由 Henriot 的 discriminant-uniform upper-bound sieve [R]
证明，一致于 (1\le|h|\le R)，

\[
 \sum_{R<n\le2R}\Lambda(n)\Lambda(n+h)
 \ll \Delta(h)R(\log\log R)^2+R,
\tag{15}
\]

并且

\[
 \sum_{h\le U}\Delta(h)\ll U,
 \qquad
 \sum_{h\le U}\frac{\Delta(h)}h\ll\log(2U).
\tag{16}
\]

在 (a,b\asymp R) 上有 ((ab)^{-1/2}\asymp R^{-1})。将式 (15)
乘式 (14)，再用式 (16) 分别处理
(|h|\le R/H) 与 harmonic tail，得到该 dyadic range 的贡献

\[
 \ll \frac RH\log(2R)(\log\log(3R))^2.
\tag{17}
\]

对 (R\le X) 求 dyadic 和是 geometric sum，故 comparable ranges 总计

\[
 \ll \frac XH L(\log L)^2
 =L^{3/2}(\log L)^2.
\tag{18}
\]

若两个 dyadic ranges 不相邻，则
(|\log(a/b)|\gg1)，式 (8) 一致给 (O(H^{-1}))。Chebyshev partial
summation 给

\[
 \sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}\ll\sqrt X,
\tag{19}
\]

所以 noncomparable contribution 为 (O(X/H)=O(\sqrt L))，被式 (18)
吸收。这证明式 (13)。\(\square\)

式 (15) 已包含 proper prime powers；因此本引理同时控制 central 与
noncentral same-base chains 的交叉，不需要另删 exceptional bases。

## 5. 中心--非中心交叉闭合 [T]

### 定理 231-C（central/noncentral short-height evacuation）

令

\[
 F_{\ne1}(t)=\sum_{a\ne b}b_ab_bR_t(a)R_t(b)^*.
\tag{20}
\]

对任意 (I=[Y,Y+H])、(Y\asymp X)、(H=X/\sqrt L)，一致有

\[
 \boxed{
 \left|
 \frac1H\int_I
 2\operatorname{Re}\langle F_1,F_{\ne1}(t)\rangle_{\rm HS},dt
 \right|
 \ll X\sqrt L(\log L)^2=o(XL).}
\tag{21}
\]

#### 证明

展开 Hilbert--Schmidt inner product，使用式 (8)--(12)，得到左侧至多

\[
 C d\beta_L^4
 \left(\sum_{n\le X}\frac{\Lambda(n)^2}{n}\right)
 \mathcal P_H(X).
\tag{22}
\]

由 (d\asymp XL)、(\beta_L\asymp L^{-1})、式 (11) 与引理 231-B，

\[
 \text{式 (22)}
 \ll
 \frac{X}{L^3}\,L^2\,L^{3/2}(\log L)^2
 =X\sqrt L(\log L)^2.
\tag{23}
\]

除以 (N\asymp XL) 后为

\[
 \frac{(\log L)^2}{\sqrt L}\longrightarrow0.
\tag{24}
\]

故式 (21) 成立。\(\square\)

本证明直接使用完整 finite responses 的 operator-norm bound，没有调用 bulk
替换，也没有改变 frozen grid；因此不产生新的 finite-to-bulk 边界。

## 6. 修复后的 covered alternating ledger [T]

令 (F_{\rm ch}) 为全部非中心 same-base chains 的 aggregate，令
(F_{\rm pr}^{\le}) 为 `ab<=XL^2` 的 different-base primitive atoms，并令
(F_{\rm pr}^{>}) 为其余高乘积 atoms。已有结论给

\[
 \|F_{\rm ch}\|_{\rm HS}^2=o(N),
 \qquad
 \|F_{\rm pr}^{\le}\|_{\rm HS}^2
 =\sum_{\rho\in\mathcal P_{\le}}\|F_\rho\|_{\rm HS}^2+o(N)=O(N),
\tag{25}
\]

并且中心 paired block 与 chain paired diagonals 满足

\[
 \|F_1\|_{\rm HS}^2=O(N),
 \qquad
 \sum_{\rho\in\mathcal C}\|F_\rho\|_{\rm HS}^2=o(N).
\tag{26}
\]

由 Cauchy--Schwarz，所有含 (F_{\rm ch}) 的 cross terms 为 (o(N))。
定理 231-C 给中心与全部
(F_{\rm ch}+F_{\rm pr}^{\le}+F_{\rm pr}^{>}) 的 signed short-height mean
为 (o(N))。因此，把这一项加入 one-sided average 后，已覆盖部分满足

\[
 \boxed{
 \|F_1+F_{\rm ch}+F_{\rm pr}^{\le}\|_{\rm HS}^2
 =\|F_1\|_{\rm HS}^2
 +\sum_{\rho\in\mathcal C\cup\mathcal P_{\le}}
  \|F_\rho\|_{\rm HS}^2+o(N)}.
\tag{27}
\]

central--noncentral 的量词仍是每个短 interval 上 signed mean 为 (o(N))，
所以必须在完整 one-sided remainder 中一次选点；它不声称 pointwise 小。
对完整 primitive family，定理 231-C 已经处理 central 与
(F_{\rm pr}^{>}) 的 cross，但
(F_{\rm pr}^{>}) 内部及其与 covered primitive 区的 cross 仍须由笔记 232-E
闭合。因此式 (27) 不能外推到全部 (F_{\rm pr})。

## 7. 对旧结论的修正

1. 笔记 222-B 的 primitive critical-shell theorem 本身不变；其中“central
   由笔记 209 独立处理”不足以推出完整 alternating ledger，必须补入定理
   231-C。
2. 笔记 225-F 的共同高度证明应在 `2+2` remainder 中加入式 (21)。加入后仍是
   同一个 signed first mean，只选择一次高度；不存在 good-set 交集问题。
3. 笔记 227-I 依赖修复后的 225-F。定理 231-C 不改变 paired constant
   (D_{22})，故数值 (0.252508968714\ldots) 不变。
4. 本轮只修复一个此前漏列的 pure-prime cross。笔记 218--222 的
   Fejer/factor-box/frozen-grid 内部求和仍需继续逆审计；记录级比例继续为 [C]。

## 8. 最小公理、删除审计与模型范围

1. **中心 carrier cancellation**：给式 (6)。删除后中心块也随高度振荡，
   式 (12) 不再是单一 ratio kernel。
2. **finite operator bound**：
   (|R_0(n)|_{\rm op}\le\beta_L) 把四矩阵 trace 直接压到
   (d\beta_L^4)。删除后需要 response-specific Schatten 输入。
3. **shifted prime-pair upper bound**：闭合 near-diagonal (a\approx b)。只有
   Chebyshev mass 时 unresolved core 可达主尺度。
4. **短高度 (H=X/\sqrt L)**：使 harmonic kernel 提供
   (X/H=\sqrt L)，而式 (24) 仍趋零。
5. **不使用 RH**：全部输入在 prime side；没有使用零点位置、pair correlation
   猜想或完整 Weil 正性。
6. **模型范围**：固定本原 Dirichlet (L) 函数只需相应带角色系数的绝对值
   majorant；Dedekind/automorphic 情形需要本地系数的 shifted two-point upper
   bound，不能由函数方程单独推出。

## 9. 可复现检查 [E]

`scripts/alternating_central_cross_audit.py` 检查：

1. central/chain/primitive Gram 的精确分拆恒等式；
2. 障碍命题 231-A 的平行/正交两模型；
3. 式 (23)--(24) 的 (L)-指数账本；
4. 有限 von Mangoldt 样本上的 ratio-kernel majorant 量级。

脚本不实现 Henriot 定理，也不证明渐近；算术输入仍是笔记 227-E 的已引用
上界。

## 10. 下一最小引理 A1k [O]

对笔记 218-E 到 222-B 作 line-by-line box-cover audit：构造一个全局 atom ID
ledger，验证每个 primitive ordered pair 恰落入 central/same-base、subcritical、
transition 或 critical 中的一类，并核对 Fejer arcs 与 factor boxes 使用同一个
冻结的 (X,L,d)。若出现 overlap，只允许在显式 half-open convention 下分配；
若出现遗漏，立即写成新的边界通道而不以 (O(N)) 吸收。

## 11. 与高乘积漏区的关系（笔记 232）

本笔记的 central--all-noncentral short-height estimate 已包含高乘积 atoms，因而
不受笔记 232 的 cutoff 修正影响。新开放项只是在 primitive--primitive Gram 内部
控制 `ab>XL^2` 的 off-diagonal aggregate；两项必须分开记账。
