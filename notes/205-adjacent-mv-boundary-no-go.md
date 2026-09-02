# 205. Adjacent interior 的 Montgomery--Vaughan 闭合与 Hankel family no-go

日期：2026-09-01

分支：MOM-1 / 路线 A

状态：Toeplitz bulk 的离散 diagonal-fibre 分解、对数乘积频率的圆周间距、
\(m\le X\) adjacent family 的渐近对角化为 [T]；所用圆周 Hilbert
不等式为 [R]；仅由 direct-sum Hankel 预算推出 family-frame 控制的不可能性为
[N]；真实 \(m>X\) supercritical Hankel aggregate 的算术估计为 [O]；
有限矩阵检查为 [E]。

## 1. 本轮结论

笔记 204 已经证明 product clusters 的 direct-sum transfer

\[
 \sum_m
 \|F_m^{\mathrm{fin}}-F_m^{\mathrm{bulk}}\|_{\mathrm{HS}}^2
 \ll 1+\log L.
\tag{1}
\]

该结论本身不能控制 \(\|\sum_mF_m\|_{\mathrm{HS}}\)。本轮把缺口精确分成
一个正向定理和一个障碍定理。

第一，Toeplitz bulk 的每一条矩阵对角线都给出同一组频率
\(\log m/L\) 上的离散指数和。Montgomery--Vaughan 圆周 Hilbert
不等式逐 diagonal 应用后，得到

\[
 \left|
 \left\|\sum_{m\in\mathcal M}F_m^{\mathrm{bulk}}\right\|_{\mathrm{HS}}^2
 -
 \sum_{m\in\mathcal M}\|F_m^{\mathrm{bulk}}\|_{\mathrm{HS}}^2
 \right|
 \ll
 \beta_L^4LM\,\mathscr S_0(\mathcal M),
\tag{2}
\]

其中 \(\mathcal M\subset[4,M]\)、\(M\le X\)，而

\[
 \mathscr S_0(\mathcal M)
 =
 \sum_{m\in\mathcal M}\sum_{r\in\mathbb Z}
 |\widehat Q_m(r)|^2
 =
 \frac1L\sum_{m\in\mathcal M}\int_{-L/2}^{L/2}|Q_m(u)|^2\,du.
\tag{3}
\]

无条件算术预算给 \(\mathscr S_0([4,X])=O(L^4)\)。笔记 203 的 endpoint
tightness 又给

\[
 \mathscr S_0((X^{1-\delta},X])
 \ll
 L^4\delta^{2\kappa+2}+o(L^4).
\tag{4}
\]

因此整个 \(m\le X\) 的 bulk family 渐近对角化。再结合式 (1) 和
\(\#\{m\le X\}\le X\)，得到真实有限 family 的定理

\[
 \boxed{
 \left\|\sum_{m\le X}F_m^{\mathrm{fin}}\right\|_{\mathrm{HS}}^2
 =
 \sum_{m\le X}\|F_m^{\mathrm{fin}}\|_{\mathrm{HS}}^2+o(N).}
\tag{5}
\]

所以 adjacent interior near-resonance 与 subcritical endpoint 已闭合；
它们不再是 MOM-1 的开放算术输入。

第二，\(m>X\) 的 finite Hankel leakage 仍不能由式 (1) 自动求和。本轮给出
sharp no-go：即使每个误差都具有精确 Toeplitz--Hankel defect 形式、符号具有
一致 \(W^{2,1}\) 正则性、频率互异且 direct-sum 能量为 \(B\)，aggregate
能量仍可等于 \(KB\)，达到 Cauchy 上界。故普通 vector-valued
Montgomery--Vaughan 不能直接作用于任意 Hankel boundary matrices。

经典 zeta 的 adjacent 通道因而被严格缩成唯一的新输入

\[
 \boxed{
 \left\|
 \sum_{m>X}
 F_m^{\mathrm{fin}}
 \right\|_{\mathrm{HS}}^2=o(N).}
\tag{6}
\]

式 (6) 是 actual arithmetic supercritical response 的估计，不是 RH、
Weil 正性或零点位置的改写。

## 2. 记号与 exact diagonal fibres

沿用笔记 204：

\[
 L=\log X,\qquad h=\frac{2\pi}{L},\qquad
 d\asymp TL,\qquad \beta_L=\frac{2\pi}{a_LL},
\tag{7}
\]

并令

\[
 F_m^{\mathrm{bulk}}
 =
 \beta_L^2e^{iTx_m}T_d(Q_m)D_d(x_m),
 \qquad x_m=\log m.
\tag{8}
\]

这里

\[
 T_d(Q_m)_{jk}=\widehat Q_m(j-k),\qquad
 D_d(x_m)_{kk}=e^{ikhx_m}.
\]

因此逐元素精确地

\[
 (F_m^{\mathrm{bulk}})_{jk}
 =
 \beta_L^2\widehat Q_m(j-k)
 e^{i(T+kh)x_m}.
\tag{9}
\]

对 \(|r|<d\)，置

\[
 I_r=\{k:0\le k<d,\ 0\le k+r<d\},
 \qquad |I_r|=d-|r|.
\tag{10}
\]

### 命题 205-A（diagonal-fibre identity）[T]

对任意有限乘积集合 \(\mathcal M\subset[4,X]\)，

\[
 \boxed{
 \left\|\sum_{m\in\mathcal M}F_m^{\mathrm{bulk}}\right\|_{\mathrm{HS}}^2
 =
 \beta_L^4
 \sum_{|r|<d}\sum_{k\in I_r}
 \left|
 \sum_{m\in\mathcal M}
 \widehat Q_m(r)e^{i(T+kh)x_m}
 \right|^2.}
\tag{11}
\]

同时

\[
 \sum_{m\in\mathcal M}\|F_m^{\mathrm{bulk}}\|_{\mathrm{HS}}^2
 =
 \beta_L^4
 \sum_{|r|<d}(d-|r|)
 \sum_{m\in\mathcal M}|\widehat Q_m(r)|^2.
\tag{12}
\]

#### 证明

在式 (9) 中固定 \(r=j-k\)。合法的列指标恰为 \(I_r\)；先对 \(m\)
求和，再对所有矩阵元素取平方，即得式 (11)。只保留 \(m=n\) 的对角项即得
式 (12)。没有使用无限 Toeplitz 极限。\(\square\)

## 3. 离散 Montgomery--Vaughan 输入

### 定理 205-B（圆周 Hilbert mean square）[R]

设 \(y_1,\ldots,y_J\in\mathbb R/\mathbb Z\) 的圆周间距至少为
\(\Delta>0\)。对任意连续整数区间 \(I\) 和复数 \(c_j\)，

\[
 \left|
 \sum_{k\in I}\left|\sum_jc_je^{2\pi iky_j}\right|^2
 -
 |I|\sum_j|c_j|^2
 \right|
 \le C_{\mathrm{MV}}\Delta^{-1}\sum_j|c_j|^2.
\tag{13}
\]

Montgomery--Vaughan 1974 的 Theorem 1 给圆周 cosecant Hilbert
不等式；展开左侧非对角项并把有限几何和写成两个 cosecant/cotangent
双线性型，即得式 (13)。这里只使用某个绝对常数
\(C_{\mathrm{MV}}\)，不需要最优常数。

文献：

- H. L. Montgomery and R. C. Vaughan,
  [Hilbert's Inequality](https://doi.org/10.1112/jlms/s2-8.1.73),
  J. London Math. Soc. (2) 8 (1974), 73--82。
- 作者公开的
  [论文 PDF](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)。

从 [R] 的 Hilbert 不等式到式 (13) 的有限展开属于 [T]；它不使用任何
zeta 零点信息。

### 引理 205-C（log-product circular spacing）[T]

若 \(4\le m<n\le M\le X\)，则点

\[
 y_m=\frac{\log m}{L}\pmod1
\]

满足

\[
 \|y_m-y_n\|_{\mathbb R/\mathbb Z}
 \ge \frac{c}{LM}
\tag{14}
\]

其中 \(c>0\) 为绝对常数。

#### 证明

直接距离满足

\[
 \frac{\log n-\log m}{L}
 \ge
 \frac{\log(1+1/M)}{L}
 \ge\frac1{2LM}.
\]

绕圆另一侧的距离为

\[
 1-\frac{\log n-\log m}{L}
 =
 \frac{\log(Xm/n)}L
 \ge\frac{\log4}{L},
\]

因为 \(n\le X\) 且 \(m\ge4\)。后者更大，故式 (14) 成立。\(\square\)

### 定理 205-D（bulk family Montgomery--Vaughan bound）[T]

对任意 \(\mathcal M\subset[4,M]\)、\(M\le X\)，式 (2) 成立。

#### 证明

在式 (11) 中固定 \(r\)，对连续区间 \(I_r\) 应用式 (13)，取

\[
 c_m=e^{iTx_m}\widehat Q_m(r),
 \qquad y_m=\frac{x_m}{L}.
\]

式 (14) 给 \(\Delta^{-1}\ll LM\)。对 \(r\) 求和并乘
\(\beta_L^4\) 得

\[
 \left|
 \left\|\sum_{m\in\mathcal M}F_m^{\mathrm{bulk}}\right\|_{\mathrm{HS}}^2
 -
 \sum_{m\in\mathcal M}\|F_m^{\mathrm{bulk}}\|_{\mathrm{HS}}^2
 \right|
 \ll
 \beta_L^4LM
 \sum_{m\in\mathcal M}\sum_{|r|<d}|\widehat Q_m(r)|^2.
\]

把有限 \(r\) 和放大到全体整数即为式 (2)。\(\square\)

注意这里没有使用任意 matrix-valued coefficients 的 Bessel 界。
Toeplitz 平移不变性先把矩阵精确拆成 scalar diagonal fibres；这是定理成立的
关键结构。

## 4. 算术 symbol energy

沿用

\[
 b_n=-\frac1{2\pi}\frac{\Lambda(n)}{\sqrt n},
\qquad
 Q_m(u)=\sum_{ab=m}b_ab_bq_{x_a}(u)q_{x_b}^{(x_a)}(u).
\tag{15}
\]

### 引理 205-E（全区间与 endpoint symbol budget）[T]

在笔记 204 的窗口正则性下，

\[
 \mathscr S_0([4,X])\ll L^4.
\tag{16}
\]

若 \(\phi_L(Lu)^2\) 具有笔记 203 的一致 endpoint envelope，消失阶为
\(\kappa\ge0\)，则对 \(p=2\kappa+2\)，

\[
 \limsup_{T\to\infty}
 L^{-4}\mathscr S_0((X^{1-\delta},X])
 \ll_\phi\delta^p.
\tag{17}
\]

#### 证明

由 Parseval 和 \(0\le q_x\le1\)，

\[
 \mathscr S_0([4,X])
 \le
 \sum_{m\le X}
 \left(\sum_{ab=m}|b_ab_b|\right)^2.
\tag{18}
\]

若 \(m\) 含两个不同素数底，只有交换次序产生的两个 ordered
factorizations；Cauchy--Schwarz 和

\[
 \sum_{n\le X}\frac{\Lambda(n)^2}{n}\ll L^2
\]

把这部分控制为 \(O(L^4)\)。若 \(m=p^k\)，其贡献由收敛级数

\[
 \sum_{p,k\ge2}
 \frac{(k-1)^2(\log p)^4}{p^k}
\]

控制。这证明式 (16)。

对式 (3) 展开 \(|Q_m|^2\) 后，恰得到笔记 203 的 adjacent
exact-product path overlap，其中窗口为
\(\psi_L(u)=\phi_L(Lu)^2\)。定理 AEM 的证明只使用一致 endpoint envelope
和无条件 Mertens 二次权渐近，故给出式 (17)。\(\square\)

## 5. 整个 \(m\le X\) family 的闭合

定义

\[
 A_{\le X}^{\mathrm{bulk}}
 =\sum_{m\le X}F_m^{\mathrm{bulk}},
\qquad
 D_{\le X}^{\mathrm{bulk}}
 =\sum_{m\le X}\|F_m^{\mathrm{bulk}}\|_{\mathrm{HS}}^2.
\tag{19}
\]

### 定理 205-F（subcritical adjacent family diagonalization）[T]

在 \(T\asymp X\)、\(N\asymp TL\) 下，

\[
 \|A_{\le X}^{\mathrm{bulk}}\|_{\mathrm{HS}}^2
 =
 D_{\le X}^{\mathrm{bulk}}+o(N).
\tag{20}
\]

真实有限 clusters 也满足式 (5)。

#### 证明

固定 \(\delta>0\)，令 \(M=X^{1-\delta}\)，并分成 interior 与 edge。

对 interior，式 (2)、式 (16) 和 \(\beta_L\asymp L^{-1}\) 给

\[
 \left|
 \left\|\sum_{m\le M}F_m^{\mathrm{bulk}}\right\|_{\mathrm{HS}}^2
 -
 \sum_{m\le M}\|F_m^{\mathrm{bulk}}\|_{\mathrm{HS}}^2
 \right|
 \ll
 LX^{1-\delta}
 =
 o(N).
\tag{21}
\]

对 edge，式 (2) 只需取 \(M=X\)。由式 (12)、式 (17) 和
\(d\asymp TL\)，

\[
 \sum_{X^{1-\delta}<m\le X}
 \|F_m^{\mathrm{bulk}}\|_{\mathrm{HS}}^2
 \le
 \beta_L^4d\,\mathscr S_0((X^{1-\delta},X])
 \ll N\delta^p+o(N),
\tag{22}
\]

而 Montgomery--Vaughan remainder 同样满足

\[
 \beta_L^4LX\,\mathscr S_0((X^{1-\delta},X])
 \ll N\delta^p+o(N).
\tag{23}
\]

所以 edge aggregate 的平方范数为 \(O(N\delta^p)+o(N)\)。interior
平方范数为 \(O(N)\)，故两块交叉项由 Cauchy--Schwarz 控制为

\[
 O(N\delta^{p/2})+o(N).
\tag{24}
\]

先令 \(T\to\infty\)，再令 \(\delta\downarrow0\)，得到式 (20)。

最后置

\[
 E_m=F_m^{\mathrm{fin}}-F_m^{\mathrm{bulk}}.
\]

笔记 204 给 \(\sum_m\|E_m\|_{\mathrm{HS}}^2\ll1+\log L\)。因此

\[
 \left\|\sum_{m\le X}E_m\right\|_{\mathrm{HS}}^2
 \le
 X\sum_{m\le X}\|E_m\|_{\mathrm{HS}}^2
 \ll X\log L=o(N).
\tag{25}
\]

式 (1) 也说明 finite 与 bulk 的 diagonal sums 相差 \(o(N)\)。
由式 (20)、式 (25) 和
\(\|A_{\le X}^{\mathrm{bulk}}\|_{\mathrm{HS}}=O(\sqrt N)\)，得到式
(5)。\(\square\)

式 (25) 使用的是 \(m\le X\) 的基数上界；若把它不加修改地用于
\(m\le X^2\)，会损失一个 \(X\) 因子。这正是下一节的障碍。

## 6. Hankel boundary 的 sharp no-go

### 定理 205-G（direct-sum-to-family no-go）[N]

仅由下列四条信息：

1. \(E_j\) 具有
   \(e^{iTx_j}\mathcal H_d(f_j,g_j)D_d(x_j)\) 形式；
2. \(f_j,g_j\) 具有一致 \(W^{2,1}\) 正则性；
3. \(x_j\) 两两不同；
4. \(\sum_{j=1}^K\|E_j\|_{\mathrm{HS}}^2=B\)；

不能推出优于 Cauchy 的 aggregate bound。事实上对任意 \(B>0\) 和
\(K\) 都可实现

\[
 \left\|\sum_{j=1}^KE_j\right\|_{\mathrm{HS}}^2=KB.
\tag{26}
\]

#### 证明

在长度 \(L\) 的圆上令

\[
 f_L(u)=e^{-ihu},\qquad g_L(u)=e^{ihu},
 \qquad h=\frac{2\pi}{L}.
\tag{27}
\]

按笔记 204 的 Fourier 约定，

\[
 \widehat f_L(1)=1,\qquad \widehat g_L(-1)=1.
\]

若 \(P_d\) 投影到 \(0,\ldots,d-1\)，则直接计算得

\[
 \mathcal H_d(f_L,g_L)
 =
 P_d\mathcal L(f_L)(I-P_d)\mathcal L(g_L)P_d
 =
 |e_0\rangle\langle e_0|.
\tag{28}
\]

正则性一致，因为

\[
 \|f_L'\|_1=2\pi,\qquad
 \|f_L'\|_2=\frac{2\pi}{\sqrt L},\qquad
 \|f_L''\|_1=\frac{4\pi^2}{L},
\tag{29}
\]

\(g_L\) 同理。

取两两不同的 \(x_j=2\pi n_j/T\)。由于
\(e^{iTx_j}=1\)，且

\[
 |e_0\rangle\langle e_0|D_d(x_j)
 =
 |e_0\rangle\langle e_0|,
\]

令

\[
 E_j=\sqrt{\frac BK}\,
 e^{iTx_j}\mathcal H_d(f_L,g_L)D_d(x_j)
\]

便有所有 \(E_j\) 完全同向。于是 direct-sum 能量为 \(B\)，aggregate
能量为 \(KB\)。这达到 Cauchy 上界。\(\square\)

该反例的符号不是 zeta 的非负 compact-support \(q_x\)，频率也不是
\(\log(ab)\)。所以它不反驳式 (6)；它严格排除的是如下证明模板：

\[
 \text{uniform symbol regularity}
 +\text{Hankel form}
 +\text{direct-sum }O(\log L)
 \Longrightarrow
 \text{aggregate }o(N).
\]

任何成功证明必须使用被反例删除的 actual arithmetic structure。

## 7. 剩余 supercritical 算术输入

由笔记 204 的周期 support 审计，\(m>X\) 时 bulk symbol 为零，故

\[
 G_{>,T}
 :=
 \sum_{m>X}F_m^{\mathrm{fin}}
 =
 -\beta_L^2
 \sum_{\substack{a,b\le X\\ab>X}}
 b_ab_b e^{iT(x_a+x_b)}
 \mathcal H_d(q_{x_a},q_{x_b}^{(x_a)})
 D_d(x_a+x_b).
\tag{30}
\]

### 开放引理 205-H（supercritical boundary coherence）[O]

证明

\[
 \|G_{>,T}\|_{\mathrm{HS}}^2=o(N).
\tag{31}
\]

这是 complete adjacent channel 所需且当前唯一剩余的 finite boundary
输入。它应通过实际 factorized response 估计，而不是把 \(ab\) 当成长度
\(X^2\) 的任意 Dirichlet coefficients。

一个仍非循环的 one-factor boundary 目标如下。笔记 206 进一步证明：在本文
已经得到的 subcritical defect aggregate 为 \(o(\sqrt N)\) 的前提下，该目标
与式 (31) 渐近等价，而不只是更强的充分条件。令

\[
 \mathcal A_X
 =
 \sum_{n\le X}
 b_ne^{iTx_n}\mathcal L(q_{x_n})D_\infty(x_n).
\tag{32}
\]

不带 \(ab>X\) cutoff 的总 product boundary 精确为

\[
 -\beta_L^2
 P_d\mathcal A_X(I-P_d)\mathcal A_XP_d.
\tag{33}
\]

因此 response-specific Schatten 估计

\[
 \beta_L^4
 \|P_d\mathcal A_X(I-P_d)\mathcal A_XP_d\|_{\mathrm{HS}}^2
 =o(N)
\tag{34}
\]

足以推出式 (31)。式 (34) 保留两个 prime sums、外部 Gabor index 和
实际物理响应方向；它不是普通 arbitrary-coefficient Bessel bound。

若式 (34) 太强，下一步应对 \(x_a+x_b-L\) 使用 Fejer 型正定分层，并在每层
保留 \(a,b\) 的 factorization，寻找 overshoot 与 boundary depth 的联合增益。
硬 band mask 不应直接插入 PSD Gram。

## 8. 最小公理、删除审计与适用范围

### 正向定理 205-F

1. **Toeplitz diagonal covariance**：产生式 (11) 的长指数和。
   删除后，定理 205-G 的单列集中使 large sieve 完全失效。
2. **critical Gabor density \(d\asymp TL\)**：确定主尺度
   \(N\asymp TL\)。若 \(d\ll TL\)，edge 与 interior 的归一化改变。
3. **log-product spacing**：只负责式 (14)，不包含素数相关猜想。
4. **von Mangoldt square budget**：给式 (16)，是无条件 prime-side 输入。
5. **endpoint envelope**：只控制 edge 的 \(\delta\) 速率；删除后无法从
   interior 推到全部 \(m\le X\)。
6. **finite direct-sum transfer**：只在式 (25) 中使用。它没有被误写成
   family-frame estimate。

### 障碍定理 205-G

- 删除 Toeplitz covariance、actual compact support 和 arithmetic
  factorization 后，现有抽象预算允许 sharp coherence。
- 该定理说明缺失公理必须具有响应方向内容；增加一个未经解释的
  “uniform negative index”或“boundary family Bessel bound”只会把目标藏入
  公理。

### 模型范围

- 对 Riemann zeta，式 (5) 无条件适用。
- 对固定本原 Dirichlet \(L\) 函数，系数只增加单位模相位，式
  (16)--(17) 的绝对 majorant 不变，因此同型结论适用。
- Dedekind 与自守 \(L\) 函数需要相应 Rankin--Selberg 二次系数预算以及
  local product multiplicity 审计；不能自动声称适用。
- 函数域模型具有有限 Fourier/Frobenius 结构，可用式 (11) 检查
  finite-section 与 exact cohomological trace 的接口。
- 定理 205-G 适用于一般谱 zeta finite sections，作为抽象 Hankel
  completion 的负向测试。

## 9. RH/GRH 循环性与结论边界

- 定理 205-F 只用 finite Toeplitz identity、Montgomery--Vaughan
  Hilbert inequality、Mertens 二次权和 endpoint support；没有读取零点。
- 式 (5) 只闭合纯素数 \(2+2\) adjacent family 的 \(m\le X\) 部分。
- 式 (31) 仍是 [O]，所以尚未得到完整 adjacent 四矩，更没有得到新的简单零点
  比例。
- alternating/Farey ratio Gram、\(3+1\)、\(4+0\)、Gamma/continuum
  cross terms 仍分别开放。
- \(13/18\) 与 \(16/21\) 仍是条件性矩信息结论，本轮没有改变其状态。
- 式 (34) 是具体算术 Schatten 估计，不等价于完整 Weil positivity；但在证明
  前不得把它称作已构造的正极化。

## 10. 可复现检查 [E]

脚本

scripts/adjacent_mv_boundary_no_go_audit.py

检查：

1. 式 (11) 的 finite diagonal-fibre identity；
2. \(4\le m\le X\) 的圆周间距尺度 \(1/(LX)\)；
3. 式 (28) 的 rank-one Hankel defect；
4. direct-sum \(B\) 与 aggregate \(KB\) 的 sharp coherence。

有限实验只核对代数、索引和尺度，不证明式 (20)、式 (31) 或任何 zeta
渐近。

## 11. 后续更新（笔记 223）

笔记 223 已关闭本笔记式 (6) 的 relative-dense good-height 版本。关键不是对任意 Hankel family 建立被定理 205-G 排除的 frame bound，而是保留实际 product phase，写成 Hilbert--Schmidt 值 Dirichlet 多项式

\[
 \sum_{X<m\le X^2}m^{it}C_m,
 \qquad \sum_{m>X}\|C_m\|_{HS}^2\ll1+\log L.
\]

Montgomery--Vaughan 高度均值在每个长度 \(X/\sqrt L=o(X)\) 的 interval 中产生一点，使 aggregate 平方为 \(o(N)\)。因此本笔记的 abstract Hankel-family no-go 仍然成立，但 actual zeta family 通过其高度相位绕过该障碍。完整四矩仍需其余通道共享同一 good-height ledger。
