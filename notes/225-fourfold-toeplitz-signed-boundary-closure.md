# 225. 四因子 Toeplitz telescoping 与纯素数 finite signed boundary 闭合

日期：2026-09-02

分支：MOM-1 / 路线 A

状态：四因子 finite-section telescoping、crossing trace-norm bound、所有
`3+1`/`4+0` pure-prime finite-to-bulk boundary 的短高度 signed first mean、
完整 pure-prime finite 四词共同高度一侧账本为 [T]；Henriot shifted upper
bound 为 [R]；有限矩阵和指数账本为 [E]；Gamma/continuum mixed words 与最终
中心化正规化为 [O]；从 signed mean 推出 mean absolute value 的逻辑跳跃为 [N]。

## 1. 结论

笔记 224 已闭合 translation-invariant bulk 的 `3+1`、`4+0` signed
first means，但把完整有限 Gabor 四循环与 bulk 的差留作开放边界。本轮证明：
对每个四因子 word，这个差精确分解成三个 cross-boundary Hankel 项，且其
**标量迹**一致满足

\[
 |\delta_{\boldsymbol\varepsilon}(x_1,x_2,x_3,x_4)|
 \ll 1+\log L,
 \qquad L=\log X.
\tag{1}
\]

关键是式 (1) 没有矩阵维数

\[
 d\asymp XL
\]

因子。bulk 主项的迹带 \(d\)，而每个 finite-section crossing 已经越过一次
\(P_d/(I-P_d)\) 边界，其 trace norm 只读取 Fourier crossing energy。

冻结 \(X,L,d\)，令 \(H=X/\sqrt L\)。对任意三个正号、一个负号的循环
次序，有限与 bulk `3+1` words 之差 \(\mathcal E_{31}(t)\) 满足

\[
 \boxed{
 \left|\frac1H\int_I\mathcal E_{31}(t)\,dt\right|
 \ll
 \frac{(1+\log L)(\log L)^4}{\sqrt L}
 +\frac{X(1+\log L)}{L^{7/2}}
 =o(N),}
\tag{2}
\]

其中 \(I=[Y,Y+H]\)、\(Y\asymp X\)、\(N\asymp XL\)。对全正号 word，

\[
 \boxed{
 \left|\frac1H\int_I\mathcal E_{40}(t)\,dt\right|
 \ll\frac{X(1+\log L)}{L^{7/2}}
 =o(N).}
\tag{3}
\]

结合笔记 203--223 已闭合的 finite `2+2` adjacent/alternating 通道和笔记
224 的 bulk signed words，每个长度 \(X/\sqrt L\) 的 interval 都含一个共同
高度，使完整 **finite pure-prime** 四词的非配对 remainder 具有 \(o(N)\) 的
一侧上界。因而在笔记 199 的 paired-diagonal 正规化下，

\[
 \operatorname{tr}P_{X,d}(t)^4
 \le D_{22}(\psi)N+o(N)
\tag{4}
\]

沿相对稠密共同高度成立。这里 \(P_{X,d}\) 只表示 pure-prime response；
式 (4) 尚未包含 \(A^3P,A^2P^2,APAP,AP^3\) 等 Gamma/continuum mixed
words，因此不是完整中心四矩上界，也不产生新的零点比例。

本轮同时修正笔记 224 式 (44) 的目标强度：共同高度的一侧选择只需要

\[
 \left|H^{-1}\int_I\mathcal E_{\partial,4}(t)dt\right|=o(N),
\tag{5}
\]

不需要更强的 \(H^{-1}\int_I|\mathcal E_{\partial,4}(t)|dt=o(N)\)。后者不能
从相位平均推出。

## 2. 一般 finite-section 四因子恒等式

令 \(\mathcal L(f)\) 为圆周 Laurent 算子，\(P=P_d\)、\(Q=I-P\)，并记

\[
 T(f)=P\mathcal L(f)P,
 \qquad
 \mathcal H(f,g)=P\mathcal L(f)Q\mathcal L(g)P.
\tag{6}
\]

### 引理 225-A（left-associated Toeplitz telescoping）[T]

对任意 bounded symbols \(f_1,\ldots,f_r\)，\(r\ge2\)，精确地

\[
 \boxed{
 \prod_{j=1}^rT(f_j)
 =T\!\left(\prod_{j=1}^rf_j\right)
 -\sum_{k=1}^{r-1}
 \mathcal H\!\left(\prod_{j=1}^kf_j,f_{k+1}\right)
 \prod_{j=k+2}^rT(f_j).}
\tag{7}
\]

空乘积解释为恒等算子。特别地，四因子差为

\[
 \begin{aligned}
 T(f_1)T(f_2)T(f_3)T(f_4)-T(f_1f_2f_3f_4)
 ={}&-\mathcal H(f_1,f_2)T(f_3)T(f_4)\\
 &-\mathcal H(f_1f_2,f_3)T(f_4)\\
 &-\mathcal H(f_1f_2f_3,f_4).
 \end{aligned}
\tag{8}
\]

#### 证明

二因子恒等式是

\[
 T(f)T(g)=T(fg)-\mathcal H(f,g).
\tag{9}
\]

假设式 (7) 对 \(r\) 成立，右乘 \(T(f_{r+1})\)。对首项再次应用式
(9)，此前的每个 Hankel 项只需右乘 \(T(f_{r+1})\)，即得 \(r+1\) 情形。
归纳完成。\(\square\)

### 引理 225-B（dimension-free crossing trace bound）[T]

定义

\[
 \mathfrak b_d(f)=
 \sum_{n\in\mathbb Z}\min(d,|n|)|\widehat f(n)|^2.
\tag{10}
\]

则

\[
 \|\mathcal H(f,g)\|_1
 \le \mathfrak b_d(f)^{1/2}\mathfrak b_d(\bar g)^{1/2}.
\tag{11}
\]

若 \(\|f_j\|_\infty\le1\)，且每个连续乘积
\(f_1\cdots f_k\) 与 \(f_{k+1}\) 都满足

\[
 \mathfrak b_d(\,cdot\,)\ll 1+\log L,
\tag{12}
\]

那么对任意 unitary \(U\)，

\[
 \left|
 \operatorname{tr}\left[
 \left(\prod_{j=1}^4T(f_j)-T(f_1f_2f_3f_4)\right)U
 \right]\right|
 \ll1+\log L.
\tag{13}
\]

#### 证明

Schatten Hölder 给

\[
 \begin{aligned}
 \|\mathcal H(f,g)\|_1
 &\le
 \|P\mathcal L(f)Q\|_{\rm HS}
 \|Q\mathcal L(g)P\|_{\rm HS}\\
 &=\mathfrak b_d(f)^{1/2}
 \mathfrak b_d(\bar g)^{1/2}.
 \end{aligned}
\]

又 \(\|T(f_j)\|\le\|f_j\|_\infty\le1\)。把式 (8) 的三项分别取
trace norm，再用 

\[
 |\operatorname{tr}(AU)|\le\|A\|_1
\]

即得式 (13)。\(\square\)

## 3. Signed Gabor words 的精确边界

沿用笔记 204、223：

\[
 R_t(x)=\beta_Le^{itx}T_d(q_x)D_d(x),
 \qquad
 q_x(u)=\phi(u)\phi(x-u),
 \qquad
 \beta_L\asymp L^{-1}.
\tag{14}
\]

周期平移记作 \(f^{(s)}(u)=f(u-s\pmod L)\)。对
\(\varepsilon\in\{+1,-1\}\)，置

\[
 f_{+,x}=q_x,
 \qquad
 f_{-,x}=q_x^{(-x)}.
\tag{15}
\]

则精确地

\[
 R_t(x)^{\varepsilon}
 =\beta_Le^{it\varepsilon x}T_d(f_{\varepsilon,x})D_d(\varepsilon x),
\tag{16}
\]

其中负一次幂在这里只表示 adjoint。给定 sign word
\(\boldsymbol\varepsilon=(\varepsilon_1,\ldots,\varepsilon_4)\)，令

\[
 s_0=0,
 \qquad s_j=\sum_{i=1}^j\varepsilon_ix_i,
 \qquad
 g_j=f_{\varepsilon_j,x_j}^{(s_{j-1})}.
\tag{17}
\]

反复使用 modulation covariance 得

\[
 \prod_{j=1}^4R_t(x_j)^{\varepsilon_j}
 =\beta_L^4e^{its_4}
 T(g_1)T(g_2)T(g_3)T(g_4)D_d(s_4).
\tag{18}
\]

相应 bulk word 是把四个 Toeplitz factors 换为一个：

\[
 \beta_L^4e^{its_4}T(g_1g_2g_3g_4)D_d(s_4).
\tag{19}
\]

定义未含 \(\beta_L^4e^{its_4}\) 的 scalar boundary

\[
 \delta_{\boldsymbol\varepsilon}(\mathbf x)
 =\operatorname{tr}\left[
 \{T(g_1)\cdots T(g_4)-T(g_1g_2g_3g_4)\}D_d(s_4)
 \right].
\tag{20}
\]

### 定理 225-C（uniform four-word trace boundary）[T]

在笔记 204 的 uniform \(C^2/W^{2,1}\) 窗口假设下，对所有
\(x_j\in[0,L]\) 和所有 sign words，式 (1) 成立。

#### 证明

每个 \(q_x\) 满足 \(0\le q_x\le1\)，周期平移不改变范数。任意至多三个
这类 symbols 的乘积仍满足一致的

\[
 \|f'\|_1+\|f''\|_1\ll1.
\tag{21}
\]

二阶导数的交叉项用各 \(q_x'\) 的一致 \(L^2\) bound 和
Cauchy--Schwarz 控制。笔记 204 的 Fourier crossing lemma 因而给式
(12)。在引理 225-B 中取 \(U=D_d(s_4)\)，即得式 (1)。\(\square\)

式 (20) 是实际 finite Gabor word 的精确 scalar boundary，不是对任意矩阵
系数施加的 Bessel majorant。与笔记 200 的全局 signed-kernel Schatten gate
相比，本轮只估计 pure-prime 四词所需要的 response-specific traces；因此绕开
了更强且仍开放的全算子差估计。

## 4. `3+1` boundary 的短高度平均 [T]

记

\[
 b_n=-\frac1{2\pi}\frac{\Lambda(n)}{\sqrt n}.
\tag{22}
\]

固定一个三个正号、一个负号的循环次序。重标正号变量为 \(a,b,c\)，负号
变量为 \(d\)，定义

\[
 \mathcal E_{31}(t)
 =\beta_L^4
 \sum_{a,b,c,d\le X}
 b_ab_bb_cb_d\,
 \delta_{31}(a,b,c;d)
 \left(\frac{abc}{d}\right)^{it}.
\tag{23}
\]

不同循环次序只改变式 (20) 的 symbols，不改变式 (1) 或下述算术预算。

### 定理 225-D（finite `3+1` signed boundary mean）[T]

式 (2) 对所有三个正号、一个负号的次序一致成立。

#### 证明

令

\[
 \mathcal A_{3,X}(m)
 =\sum_{\substack{abc=m\\a,b,c\le X}}
 \Lambda(a)\Lambda(b)\Lambda(c)
 \le(\Lambda*\Lambda*\Lambda)(m).
\tag{24}
\]

对 \(m=abc,n=d\) 先处理 comparable dyadic ranges \(m,n\asymp R\)。因为
\(n\le X\)，这里只需 \(R\ll X\)。笔记 224 的 shifted
\(E_3\)-prime bound 与 interval kernel 给

\[
 \sum_{\substack{m,n\asymp R\\m\ne n}}
 \frac{\mathcal A_{3,X}(m)\Lambda(n)}{\sqrt{mn}}
 \left|K_I\!\left(\log\frac mn\right)\right|
 \ll \frac RH L^3(\log L)^4.
\tag{25}
\]

对 \(R\ll X\) 求 dyadic 和，乘式 (1) 与 \(\beta_L^4\ll L^{-4}\)，得到

\[
 \ll
 \frac{1+\log L}{L^4}\frac XH
 L^3(\log L)^4
 =\frac{(1+\log L)(\log L)^4}{\sqrt L}.
\tag{26}
\]

exact diagonal \(m=n\) 由笔记 224 式 (27) 给 \(O((1+\log L)L^{-4})\)。

若 \(m,n\) 不 comparable，则 \(|\log(m/n)|\gg1\)，所以

\[
 |K_I(\log(m/n))|\ll H^{-1}.
\]

这里不需要 compact path support；直接使用

\[
 \sum_{r\le X}\frac{\Lambda(r)}{\sqrt r}\ll\sqrt X
\tag{27}
\]

四次，得到 noncomparable contribution

\[
 \ll
 \beta_L^4(1+\log L)H^{-1}X^2
 \ll\frac{X(1+\log L)}{L^{7/2}}.
\tag{28}
\]

式 (26)--(28) 即为式 (2)，且两项除以 \(N\asymp XL\) 都趋于零。
\(\square\)

## 5. `4+0` boundary 的短高度平均 [T]

定义

\[
 \mathcal E_{40}(t)
 =\beta_L^4
 \sum_{a,b,c,d\le X}
 b_ab_bb_cb_d\,
 \delta_{40}(a,b,c,d)(abcd)^{it}.
\tag{29}
\]

### 定理 225-E（finite `4+0` signed boundary mean）[T]

式 (3) 成立。

#### 证明

因为 \(a,b,c,d\ge2\)，

\[
 \log(abcd)\ge4\log2.
\]

故 interval kernel 一致为 \(O(H^{-1})\)。式 (1)、(27) 和
\(\beta_L^4\ll L^{-4}\) 给

\[
 \left|\frac1H\int_I\mathcal E_{40}(t)dt\right|
 \ll
 \frac{1+\log L}{L^4H}
 \left(\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}\right)^4
 \ll\frac{X(1+\log L)}{L^{7/2}}.
\]

这就是式 (3)。\(\square\)

## 6. 完整 pure-prime finite common height [T]

### 推论 225-F（finite pure-prime one-sided closure）

在笔记 199、203--224 的定理链下，每个
\(I=[Y,Y+X/\sqrt L]\)、\(Y\asymp X\) 都含一点 \(t_I\)，使完整有限 Gabor
pure-prime fourth-word ledger 满足式 (4)。

#### 证明

笔记 203--223 已把 paired `2+2` main term转移到有限响应，并将 adjacent
与 alternating 的非配对 finite remainder 闭合为 \(o(N)\)。笔记 224 把
bulk `3+1,4+0` 按真实系数

\[
 8\operatorname{Re}W_{31}+2\operatorname{Re}W_{40}
\]

与 adjacent defect 合并，证明其短区间平均为 \(o(N)\)。定理 225-D--E
说明 finite/bulk signed boundary 的同一线性组合平均仍为 \(o(N)\)。因此把
这些项在取平均前全部相加，只作一次“最小值不超过平均值”的选择，即得共同
\(t_I\)。uniform alternating estimate可在同一点加入。\(\square\)

这一步没有相交多个 exceptional sets，也没有要求每个 signed word 在
\(t_I\) 分别为 \(o(N)\)。结论恰好是四矩上界需要的一侧组合。

## 7. Signed mean 与 mean absolute value 的 no-go [N]

取任意 \(A>0,\omega\ne0\)，令

\[
 E(t)=Ae^{i\omega t}.
\]

则

\[
 \frac1H\int_I|E(t)|dt=A,
\]

而

\[
 \left|\frac1H\int_IE(t)dt\right|
 \le\frac{2A}{H|\omega|}.
\tag{30}
\]

所以相位核可以使 signed first mean 任意小，却完全不减 mean absolute value。
笔记 224 式 (44) 的绝对值放在积分内部是一个严格更强、且当前共同高度选择不需要
的目标。这里不是宣称实际 zeta boundary 等于单频模型；式 (30) 排除的是从本轮
相位平均论证自动推出该强目标的逻辑步骤。

## 8. 最小公理、删除审计与循环性

1. **临界 Gabor 密度与 modulation covariance**：产生式 (18) 的单一总相位。
   删除后，四因子不能化为固定 coefficient 的指数和。
2. **uniform crossing energy**：把每个 Hankel trace norm 压到
   \(O(1+\log L)\)。只有 operator norm 而无 Fourier crossing budget 时，迹可带
   \(d\) 因子，式 (2)--(3) 失效。
3. **left-associated exact telescoping**：保留真实物理 response；没有把四个
   factors 分别取绝对值后施加任意系数 Bessel 界。
4. **Henriot shifted \(E_3\)-prime upper bound**：只用于 `3+1` comparable
   ranges。删除它后，
   \(|abc-d|\lesssim X/H\) 的 resolution core 仍不可由相位消去。
5. **Chebyshev weighted \(L^1\) bound**：只处理 noncomparable `3+1` 与全部
   `4+0`。它不含素数对或 RH 信息。
6. **signed one-sided selection**：允许负 remainder 保留。改成逐 word absolute
   smallness 会引入式 (30) 所示的不必要障碍。

全部新证明位于 prime-side finite Gabor 代数、上界筛和高度积分；没有使用零点
位置、RH、Weil positivity 或 Hardy--Littlewood asymptotic。式 (4) 是部分 Weil
配置的 pure-prime fourth-trace 输入，不是完整 Weil 正性的改写。

模型范围：Riemann zeta 直接适用；固定本原 Dirichlet \(L\) 的 character phases
不增 absolute arithmetic bounds；Dedekind/automorphic 情形需要 degree-three
coefficient shifted sieve；函数域需要离散 Frobenius-orbit averaging；只有函数
方程而无 Euler-product sparsity的模型缺少定理 225-D 的算术输入。

## 9. 与全局 Schatten gate 的关系

笔记 200 的

\[
 \|J_T-J_{\infty,T}\|_{\mathcal S_4}=o(N^{1/4})
\]

仍是控制**全部 signed kernel**的充分条件。本轮没有证明它，而是证明纯素数
四词只需三个具体 Hankel trace 的 response estimate。两者关系是

\[
 \text{global Schatten gate}
 \Longrightarrow \text{all-word boundary control},
\]

而本轮只建立

\[
 \text{crossing energy + prime phases}
 \Longrightarrow \text{pure-prime signed boundary control}.
\]

不得反向声称 pure-prime closure 推出全局 Schatten approximation。mixed
Gamma/continuum symbols 的系数几何不同，尚未进入本轮算术和迹范数预算。

## 10. 下一最小引理 [O]

路线 A 的开放输入现缩为 **mixed-word common-height Schur ledger**：对

\[
 4\operatorname{tr}(A^3P)
 +4\operatorname{tr}(A^2P^2)
 +2\operatorname{tr}(APAP)
 +4\operatorname{tr}(AP^3)
\tag{31}
\]

提取 Gamma/continuum 背景 \(A\) 的实际 Toeplitz symbols 和 coefficient
measures，并证明其 finite/bulk boundary 与 bulk mixed remainder 的真实带符号
组合，在每个长度 \(X/\sqrt L\) interval 上具有 \(o(N)\) 的一侧均值，或归约为
一个明确的 response-specific Schur defect。

第一步应是写出 \(A\) 的原子/连续测度总变差、\(L^2\) 能量与 crossing energy
三张独立账本。若其总变差在四词 telescoping 中必然产生主尺度且没有可保留的
符号交叉项，则形成 mixed-boundary obstruction；不能退回全局正包络并把缺失
的抵消称为已证。

## 11. 可复现检查 [E]

脚本 `scripts/fourfold_toeplitz_boundary_audit.py` 检查：

1. band-limited Laurent symbols 的式 (7)--(8)；
2. adjoint response 的 modulation/translation 符号；
3. 四因子 scalar boundary 的 nuclear crossing bound；
4. 式 (2)--(3) 的指数账本；
5. signed mean 与 mean absolute value 的单频分离。

脚本不实现 Henriot 定理、不证明 prime asymptotics，也不包含 RH 数值证据。

## 12. 后续推进（笔记 226）

笔记 226 完成了本笔记第 10 节所要求的第一步，但结果比“三张正包络账本”更强：显式公式的 Gamma/pole-absorption 背景可直接写为确定性零频 Toeplitz 主部 `S_L=T_d(phi^2/a-1)` 加 `O(1/L)` 算子余项；后者利用本笔记已证的 `tr P^4=O(N)` 在第四迹中为 `O(N/L)=o(N)`。因此新的最小引理不再包含 continuum/Gamma boundary，而是 `tr(S_L+P)^4` 中 one-prime、two-prime off-diagonal 与 three-prime signed frequencies 的共同短高度 evacuation。