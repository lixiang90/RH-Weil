# 224. Shifted \(E_3\) sieve 与纯素数四阶词的共同短高度闭合

日期：2026-09-02

分支：MOM-1 / 路线 A

状态：精确三素数卷积支撑分解、shifted
\((\Lambda*\Lambda*\Lambda)\)-prime 上界、bulk \(3+1\) 与 \(4+0\)
短高度平均、纯素数四阶词的共同 good-height 选择为 [T]；Henriot 的
discriminant-uniform Nair--Tenenbaum upper bound 为 [R]；完整有限
Gabor 四循环的 signed boundary 与 Gamma/continuum 混合词为 [O]；有限
组合与指数账本检查为 [E]。

> **后续修正（笔记 225）**：本笔记的 bulk 结论保持成立。笔记 225 已把
> finite `3+1,4+0` 与相应 bulk words 的差精确分解为三个 Toeplitz crossing
> traces，并在同一短高度尺度闭合其 signed first mean。因此本笔记式 (44)
> 中把绝对值放在积分内部的目标过强；共同一侧选择只需绝对值放在积分外。
> 完整 finite pure-prime 四词现已闭合，下一输入改为 Gamma/continuum mixed words。

## 1. 结论

笔记 223 已在每个长度

\[
 H_X=\frac{X}{\sqrt L},\qquad L=\log X,
\tag{1}
\]

的高度区间中找到一点，使 adjacent \(2+2\) 的 supercritical boundary
为 \(o(N)\)，其中 \(N\asymp XL\)。完整纯素数四阶账本还含

\[
 8\operatorname{Re}\operatorname{tr}(Z^3Z^*)
 +2\operatorname{Re}\operatorname{tr}(Z^4).
\tag{2}
\]

本轮证明这两个 signed words 的 translation-invariant bulk 版本在同一短区间
上的 **signed first mean 的绝对值**都是 \(o(N)\)。

关键是 compact-support path 对 \(+,+,+,-\) 和 \(+,+,+,+\) 两种次序都
强制前三个正频率满足

\[
 abc\le X.
\tag{3}
\]

对 \(3+1\)，唯一不能被高度核自动分辨的区域是

\[
 |abc-d|\lesssim \frac{X}{H_X}=\sqrt L.
\tag{4}
\]

其算术质量由本轮的新 shifted \(E_3\)-prime 上界控制：

\[
 \boxed{
 \sum_{R<n\le2R}
 \Lambda(n)(\Lambda*\Lambda*\Lambda)(n+h)
 \ll
 \Delta(h)R(\log R)^2(\log\log R)^4
+R(\log R)^2,}
\tag{5}
\]

一致于 \(1\le |h|\le R\)，其中

\[
 \sum_{h\le H}\Delta(h)\ll H,\qquad
 \sum_{h\le H}\frac{\Delta(h)}h\ll\log(2H).
\tag{6}
\]

因此

\[
 \boxed{
 \left|\frac1{H_X}\int_I
 \mathcal W_{31}^{\mathrm{bulk}}(t)\,dt\right|
 \ll
 X\sqrt L(\log L)^4=o(XL),}
\tag{7}
\]

而

\[
 \boxed{
 \left|\frac1{H_X}\int_I
 \mathcal W_{40}^{\mathrm{bulk}}(t)\,dt\right|
 \ll \frac{X}{\sqrt L}=o(XL).}
\tag{8}
\]

笔记 209--222 已对 alternating \(2+2\) primitive support 给出 uniform
\(o(N)\)，笔记 223 又给 adjacent 的非负短高度 defect。把 adjacent defect
与 \(3+1,4+0\) 的**实际带符号组合**先相加再取平均，得到每个式 (1) 的
interval 内存在一个共同高度，使纯素数 bulk 四阶词的全部非配对 remainder
具有 \(o(N)\) 的一侧上界。这里不声称两个 signed words 在该点分别为
\(o(N)\)。

这不是完整四矩定理。尚未闭合的是：

1. 从完整有限 Gabor 四循环到 bulk 的 signed boundary；
2. \(A^3P,A^2P^2,APAP,AP^3\) 等 Gamma/continuum 混合词；
3. 上述各项与最终 \(b_4\) 正规化的共同 finite ledger。

## 2. 精化的 discriminant-uniform 输入

记

\[
 \mathbf e_j(n)=\mathbf 1_{\Omega(n)=j},
\tag{9}
\]

其中 \(\Omega\) 按重数计算素因子。

### 外部定理 224-A（Henriot specialized shifted bound）[R]

存在非负函数 \(\Delta(h)\)，满足式 (6)，使对任意
\(0<z_1,z_3\le1\)，一致于 \(1\le|h|\le R\)，

\[
 \begin{aligned}
 &\sum_{R<n\le2R}
 z_1^{\Omega(n)}z_3^{\Omega(n+h)}\\
 &\qquad\ll
 \Delta(h)\frac{R}{(\log R)^2}
 \prod_{p\le3R}
 \left(1+\frac{z_1}{p}\right)
 \left(1+\frac{z_3}{p}\right).
 \end{aligned}
\tag{10}
\]

这里的常数可对 \(z_1,z_3\in(0,1]\) 一致选择。

这是 Henriot 的 discriminant-uniform Nair--Tenenbaum theorem 对
\(Q_1(n)=n,Q_2(n)=n+h\) 和

\[
 F(u,v)=z_1^{\Omega(u)}z_3^{\Omega(v)}
\]

的 specialization。原论文在介绍中明确指出：相对于 Holowinsky 的
\(\tau(h)(\log R)^\varepsilon\) 版本，精化项 \(\Delta(h)\) 具有平均值
一，并删除 \(\varepsilon\) 损失。Henriot 的 2014 erratum 保留 upper bound，
但正式应用必须把 \(\widehat\rho_R\) 换成修正的 \(\check\rho_R\)，并在一般
多项式中把坏素数因子写成 \(a^*D^*\)。这里的 \(X,X+h\) primitive 且 monic，
所以 \(a^*=1\)，而 \(\check\rho_R\le\widehat\rho_R\)；笔记 229 已独立核验
本 specialization 及 \(z_j\to0\) 时隐常数的统一性。

由 Theorem 3 的显式 local discriminant factor，在
\(z_1,z_3\le1\) 时可用

\[
 \prod_{p\mid h}\left(1+\frac Cp\right)
\tag{11}
\]

一致支配 \(\Delta(h)\)。式 (6) 的第一式也可由该 Euler product 和
divisor expansion 直接推出；第二式再由 Abel summation 得到。

### 引理 224-B（one-prime/three-prime support correlation）[T]

一致于 \(1\le|h|\le R\)，

\[
 \boxed{
 \sum_{R<n\le2R}
 \mathbf e_1(n)\mathbf e_3(n+h)
 \ll
 \Delta(h)\frac{R(\log\log R)^4}{(\log R)^2}.}
\tag{12}
\]

#### 证明

置 \(\ell=\log R\)，并取

\[
 z_1=\frac1{\log\ell},\qquad
 z_3=\frac3{\log\ell}.
\tag{13}
\]

对充分大 \(R\)，二者都位于 \((0,1]\)。逐点有

\[
 \mathbf e_1(n)\le z_1^{-1}z_1^{\Omega(n)},\qquad
 \mathbf e_3(m)\le z_3^{-3}z_3^{\Omega(m)}.
\tag{14}
\]

Mertens 上界给

\[
 \begin{aligned}
 \prod_{p\le3R}
 \left(1+\frac{z_1}{p}\right)
 \left(1+\frac{z_3}{p}\right)
 &\ll
 \exp((z_1+z_3)\log\ell+O(1))\\
 &\ll1,
 \end{aligned}
\tag{15}
\]

而

\[
 z_1^{-1}z_3^{-3}\asymp(\log\ell)^4.
\]

代入式 (10) 即得式 (12)。\(\square\)

## 3. 三重 von Mangoldt 卷积的误差分解

置

\[
 \mathcal A_3=\Lambda*\Lambda*\Lambda.
\tag{16}
\]

令 \(\Lambda_1(n)=\Lambda(n)\mathbf1_{n\ {\rm prime}}\)，并写

\[
 \Lambda=\Lambda_1+\mathcal E_1.
\tag{17}
\]

则

\[
 \sum_{n\le R}\mathcal E_1(n)\ll\sqrt R\log R,
\qquad
 \sum_{n\ge1}\frac{\mathcal E_1(n)}n<\infty.
\tag{18}
\]

定义

\[
 \mathcal A_{3,0}=\Lambda_1*\Lambda_1*\Lambda_1,\qquad
 \mathcal E_3=\mathcal A_3-\mathcal A_{3,0}\ge0.
\tag{19}
\]

### 引理 224-C（proper-power mass and pointwise bound）[T]

在固定倍区间内，

\[
 \sum_{n\le R}\mathcal E_3(n)\ll R\log R,
\tag{20}
\]

并且

\[
 0\le\mathcal A_3(n)\ll(\log(2n))^6.
\tag{21}
\]

此外

\[
 \mathcal A_{3,0}(n)
 \le6(\log(2n))^3\mathbf e_3(n).
\tag{22}
\]

#### 证明

式 (18) 来自 proper prime powers \(p^k,k\ge2\) 的直接求和。对
\(\mathcal E_3\)，至少一个 convolution factor 来自 \(\mathcal E_1\)。
Chebyshev 上界给

\[
 \sum_{bc\le y}\Lambda(b)\Lambda(c)\ll y\log(2y).
\tag{23}
\]

因此把 exceptional factor 固定为 \(a\) 后，总质量至多

\[
 R\log(2R)\sum_a\frac{\mathcal E_1(a)}a\ll R\log R.
\]

三个位置求和只改变常数，得到式 (20)。

若 \(\mathcal A_3(n)\ne0\)，每个 convolution factor 必为一个整除 \(n\)
的 prime power。这样的 prime-power divisors 总数不超过
\(\Omega(n)\ll\log(2n)\)，故 ordered triples 至多 \(O((\log(2n))^3)\)；
每个权重乘积至多 \(O((\log(2n))^3)\)，得到式 (21)。

最后，三个 prime factors 的 ordered permutations 至多六个，且
\(\Omega(n)=3\)，得到式 (22)。\(\square\)

### 定理 224-D（shifted \(E_3\)-prime correlation）[T]

式 (5) 对正、负 shifts 都成立。

#### 证明

先考虑 \(\mathcal A_{3,0}(n+h)\Lambda_1(n)\)。由式 (22)、
\(\Lambda_1(n)\le\log(3R)\) 和引理 224-B，

\[
 \sum_{R<n\le2R}
 \mathcal A_{3,0}(n+h)\Lambda_1(n)
 \ll
 \Delta(h)R(\log R)^2(\log\log R)^4.
\tag{24}
\]

含 \(\mathcal E_3\) 的项由式 (20) 和
\(\Lambda(n)\le\log(3R)\) 控制为 \(O(R(\log R)^2)\)。

含 \(\mathcal E_1(n)\) 的项只在 proper prime powers 上出现。这样的
\(n\) 在 \([R,2R]\) 中有 \(O(\sqrt R\log R)\) 个；式 (21) 给其总贡献

\[
 O(\sqrt R(\log R)^8)=o(R(\log R)^2).
\tag{25}
\]

交换两个 shifted variables处理负 \(h\)。\(\square\)

### 对角退化 [T]

当 \(h=0\) 且 \(\Lambda(n)\ne0\) 时，\(n=p^k\)。精确地

\[
 \mathcal A_3(p^k)
 =\binom{k-1}{2}(\log p)^3,\qquad k\ge3.
\tag{26}
\]

所以

\[
 \sum_{n\ge1}\frac{\Lambda(n)\mathcal A_3(n)}n
 =
 \sum_p\sum_{k\ge3}
 \binom{k-1}{2}\frac{(\log p)^4}{p^k}
 <\infty.
\tag{27}
\]

该 exact resonance 在第四矩尺度上为 \(o(N)\)。

## 4. Bulk path words

令 \(w_{a,b,c;d}^{31}\)、\(w_{a,b,c;d}^{40}\) 是固定偶窗口产生的
translation-invariant four-cycle path weights。只需使用两个性质：

\[
 |w_{a,b,c;d}^{31}|+|w_{a,b,c;d}^{40}|\ll_\psi1,
\tag{28}
\]

以及笔记 201 的 path-support identity

\[
 w_{a,b,c;d}^{31}=w_{a,b,c;d}^{40}=0
 \quad\text{unless }abc\le X.
\tag{29}
\]

第二式来自部分和

\[
 0,\quad \frac{\log a}{L},\quad
 \frac{\log ab}{L},\quad\frac{\log abc}{L}.
\tag{30}
\]

记

\[
 \gamma_X=\beta_L^4d_G\asymp\frac X{L^3}.
\tag{31}
\]

忽略固定的 \((2\pi)^{-4}\) 后，定义

\[
 \begin{aligned}
 \mathcal W_{31}^{\rm bulk}(t)
 &=
 \gamma_X
 \sum_{\substack{a,b,c,d\le X\\abc\le X}}
 \frac{\Lambda(a)\Lambda(b)\Lambda(c)\Lambda(d)}
 {\sqrt{abcd}}\,
 w_{a,b,c;d}^{31}
 \left(\frac{abc}{d}\right)^{it},\\
 \mathcal W_{40}^{\rm bulk}(t)
 &=
 \gamma_X
 \sum_{\substack{a,b,c,d\le X\\abc\le X}}
 \frac{\Lambda(a)\Lambda(b)\Lambda(c)\Lambda(d)}
 {\sqrt{abcd}}\,
 w_{a,b,c;d}^{40}
 (abcd)^{it}.
 \end{aligned}
\tag{32}
\]

这正是 \(\operatorname{tr}(Z^3Z^*)\) 和
\(\operatorname{tr}(Z^4)\) 的 bulk scalar form，差别只在固定循环
combinatorial constants。

对长度 \(H\) 的 interval \(I\)，置

\[
 K_I(u)=\frac1H\int_Ie^{itu}\,dt.
\tag{33}
\]

则

\[
 |K_I(u)|\le\min\left(1,\frac2{H|u|}\right).
\tag{34}
\]

## 5. \(3+1\) 的短高度平均 [T]

### 定理 224-E

对 \(H=H_X\) 和任意 \(I=[Y,Y+H]\)、\(Y\asymp X\)，式 (7) 成立。

#### 证明

按

\[
 m=abc,\qquad n=d
\]

聚类。删除 path weights 的符号后，系数由
\(\mathcal A_3(m)\Lambda(n)/\sqrt{mn}\) 控制。

先取 \(m,n\asymp R\)。若 \(m=n+h\ne n\)，则

\[
 \left|\log\frac mn\right|\gg\frac{|h|}{R},
\]

故式 (34) 给

\[
 |K_I(\log(m/n))|
 \ll\min\left(1,\frac{R}{H|h|}\right).
\tag{35}
\]

由式 (5)--(6) 与 Abel summation，

\[
 \sum_{1\le|h|\le R}
 \Delta(h)\min\left(1,\frac{R}{H|h|}\right)
 \ll\frac RH\log(2R),
\tag{36}
\]

同样

\[
 \sum_{1\le|h|\le R}
 \min\left(1,\frac{R}{H|h|}\right)
 \ll\frac RH\log(2R).
\tag{37}
\]

这里 \(R/H\le X/H=\sqrt L\)。当 \(R>H\) 时，
\(|h|\le R/H\) 的 unresolved core 中 kernel 可以等于一；式 (36) 先用
\(\sum_{h\le U}\Delta(h)\ll U\) 处理该 core，再对其余 shifts 作 harmonic
summation，因而已经包含这一情形。

式 (5)、(35)--(37) 说明该 dyadic range 在乘 \(\gamma_X\) 前至多

\[
 \frac RH L^3(\log L)^4.
\tag{38}
\]

对 \(R\le X\) 求 dyadic 和是 geometric sum。再乘式 (31)，得到

\[
 \left|\frac1H\int_I\mathcal W_{31}^{\rm bulk}(t)dt\right|
 \ll
 \frac X{L^3}\frac XH L^3(\log L)^4
+o(N)
 =
 X\sqrt L(\log L)^4+o(N).
\tag{39}
\]

式 (27) 处理 \(m=n\)。

若 \(m,n\) 不在相邻 dyadic ranges，则
\(|\log(m/n)|\gg1\)。利用 Chebyshev convolution bounds 和 partial
summation，

\[
 \sum_{m\le X}\frac{\mathcal A_3(m)}{\sqrt m}
 \ll\sqrt X L^2,\qquad
 \sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}\ll\sqrt X.
\tag{40}
\]

因此 noncomparable ranges 的总贡献至多

\[
 \gamma_XH^{-1}XL^2
 \ll\frac X{\sqrt L}=o(N).
\tag{41}
\]

最后

\[
 \frac{X\sqrt L(\log L)^4}{XL}
 =\frac{(\log L)^4}{\sqrt L}\longrightarrow0.
\]

这证明式 (7)。\(\square\)

## 6. \(4+0\) 的短高度平均 [T]

### 定理 224-F

在同一 \(H,I\) 上，式 (8) 成立。

#### 证明

所有 \(a,b,c,d\ge2\)，故

\[
 \log(abcd)\ge4\log2.
\]

式 (34) 因而一致给 \(O(H^{-1})\)。由式 (40) 与第二个
Chebyshev bound，

\[
 \begin{aligned}
 &\sum_{\substack{a,b,c,d\le X\\abc\le X}}
 \frac{\Lambda(a)\Lambda(b)\Lambda(c)\Lambda(d)}
 {\sqrt{abcd}}\\
 &\qquad\le
 \left(\sum_{m\le X}\frac{\mathcal A_3(m)}{\sqrt m}\right)
 \left(\sum_{d\le X}\frac{\Lambda(d)}{\sqrt d}\right)
 \ll XL^2.
 \end{aligned}
\tag{42}
\]

所以 signed first mean 的绝对值至多

\[
 \gamma_XH^{-1}XL^2
 \ll\frac X{\sqrt L}=o(N).
\]

\(\square\)

## 7. 共同 good height [T]

### 推论 224-G（pure-prime bulk common-height closure）

在笔记 209--223 的假设与结论下，每个
\(I=[Y,Y+H_X]\)、\(Y\asymp X\) 都含一点 \(t_I\)，使：

1. adjacent \(2+2\) 的 supercritical finite aggregate 为 \(o(N)\)；
2. alternating \(2+2\) 的完整 primitive off-diagonal 为 \(o(N)\)；
3. adjacent defect 与 bulk \(3+1,4+0\) 的实际带符号组合具有
   \(o(N)\) 的一侧上界。

#### 证明

令 \(\mathcal D_{\rm adj}(t)\ge0\) 为笔记 223 的 supercritical
Hilbert--Schmidt defect，并置实际四阶系数组合

\[
 \mathcal R_X(t)=
 \mathcal D_{\rm adj}(t)
+8\operatorname{Re}\mathcal W_{31}^{\rm bulk}(t)
+2\operatorname{Re}\mathcal W_{40}^{\rm bulk}(t).
\tag{43}
\]

笔记 223 与定理 224-E--F 给

\[
 \frac1{H_X}\int_I\mathcal R_X(t)dt=o(N).
\]

任意实可积函数的最小值不超过其平均，故区间内至少一点满足
\(\mathcal R_X(t_I)\le o(N)\)。alternating 结论由笔记 209--222
uniform in height 地成立，可在同一点加入。
\(\square\)

该选择没有把几个 exceptional sets 事后相交；它先形成完整的一侧 signed
remainder，再只选择一个高度。由于目标是四矩上界而非逐 word 绝对值，
负的 \(3+1\) 或 \(4+0\) 贡献可以保留，不能再取绝对值删除。

## 8. 最小公理、删除审计与 no-go

1. **compact path support**：把 \(m=abc\) 限制到 \(X\)。删除后
   \(3+1\) 的 numerator 可达 \(X^3\)，式 (39) 完全失去尺度。
2. **Henriot refined discriminant factor**：其 bounded mean 把
   \(\sum\Delta(h)/h\) 控制为 \(O(L)\)。若只用
   \(\tau(h)\)，则 harmonic sum 为 \(O(L^2)\)，式 (39) 会停在
   \(N\sqrt L\) 附近而不能闭合。
3. **\(\Omega=1/3\) 双参数优化**：选择 \(z_1,z_3\) 分别匹配一个和三个
   prime factors。固定 \(z\) 会损失固定 log power。
4. **proper-power ledger**：防止把 \(\Lambda\) 或 \(\mathcal A_3\)
   错当 multiplicative functions；它只支付式 (20)、(25) 的低阶误差。
5. **signed first height moment**：\(3+1,4+0\) 是 signed scalar
   words，不需要 Hilbert mean square。高度核只控制
   \(\left|\int W\right|\)，不控制 \(\int|W|\)；后者若被误用会造成错误
   的逐 word 小性结论。
6. **single one-sided selection ledger**：保证所有通道共享同一高度。
   分别证明各自存在 good points 不足以推出共同交非空。

一个 sharp resolution no-go 是：若没有式 (5) 型 actual arithmetic density，
任意系数都可集中在 \(m=n+1\)。在长度 \(H=o(X)\) 的 interval 上，
\((1+1/n)^{it}\) 相位变化为 \(o(1)\)，所以普通短高度 averaging 不会
消除该方向。新结果真正使用的是 \(E_3\)-prime 支撑稀疏性，不是形式相位。

## 9. 循环性、模型范围与 Weil 接口

- 全部新估计只使用 prime-side convolution、上界筛、window path support
  和高度积分；没有读取 zeros、RH、Weil positivity 或 Hardy--Littlewood
  asymptotic。
- 对固定本原 Dirichlet \(L\) 函数，absolute bounds 删除 character
  phases；若其 Gabor path normalization 相同，bulk 结论保留。
- Dedekind/automorphic \(L\) 函数需要相应的 degree-three coefficient
  support sieve；Rankin--Selberg 二矩本身不推出式 (5)。
- 函数域需要把连续高度核换成 Frobenius orbit 上的离散 character
  orthogonality。
- 对只有函数方程而无 Euler-product sparsity的负向模型，式 (12) 不存在；
  因而本结论不是函数方程或中心线的同义改写。

在显式公式型部分 Weil 配置中，本轮闭合了 bulk pure-prime fourth-word
negative/excess budget 的共同高度选择。它没有建立上同调极化，也不声称
上同调型与显式公式型配置等价。

## 10. 下一最小引理 [O]

路线 A 的下一输入缩为 **common-height signed fourth-cycle boundary**：
证明完整有限 Gabor pure-prime fourth words 与本轮 bulk words 的差在每个
长度 \(H_X\) 的 interval 上满足

\[
 \frac1{H_X}\int_I
 |\mathcal E_{\partial,4}(t)|\,dt=o(N),
\tag{44}
\]

并把 Gamma/continuum mixed words 的剩余非负 Schur defect加入同一平均。

如果有限边界含有效 conductor 超过 \(X^2\) 且没有 analog of
Toeplitz--Hankel direct-sum energy，则应形成严格 boundary obstruction，
而不是把式 (44) 当作“技术误差”略去。

## 11. 可复现检查 [E]

脚本 scripts/short_height_31_40_audit.py 检查：

1. \(\mathcal A_3(p^k)=\binom{k-1}{2}(\log p)^3\)；
2. \(+,+,+,\pm\) path span 强制 \(abc\le X\)；
3. exact interval kernel 与式 (34)；
4. bounded-mean discriminant majorant 的 harmonic sum；
5. \((\log L)^4/\sqrt L\to0\) 的指数账本。

脚本不实现 Henriot 定理，不证明 prime asymptotics，也不是 RH 数值证据。

## 12. 后续推进（笔记 225）

笔记 225 证明 finite four-Toeplitz product 减去 bulk product 精确等于三个 crossing-Hankel 项，且每项的 scalar trace 为 `O(1+log L)` 而不带 Gabor 维数。把本笔记的 shifted `E_3` bound 重新用于 comparable `3+1` ranges，并对其余频率用短高度核，得到 finite `3+1,4+0` boundary 的 signed first means 为 `o(N)`。因此 pure-prime finite ledger 已完成 single-selection；下一最小引理只剩 Gamma/continuum mixed-word Schur ledger与最终正规化。
