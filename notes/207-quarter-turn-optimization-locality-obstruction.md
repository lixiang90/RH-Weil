# 207. Boundary quarter-turn 最优化、operator-smallness 与局部化障碍

日期：2026-09-02

分支：MOM-1 / 路线 A，辅助接口 NCE-8 / 路线 B

状态：有限维最优 quarter-turn 公式、operator-smallness 充分条件、自然双边
pairing 的精确缺陷恒等式、band-limited no-go 及实际 Gabor 高对角局部化为
[T]/[N]；实际 von Mangoldt--smooth-window 计算为 [E]；boundary operator
norm 的 little-oh 为 [O]。

## 1. 逆向审计后的结论

笔记 206 把 supercritical adjacent boundary 渐近等价地归约为

\[
 \beta_L^4\|B_XB_X^{\mathsf T}\|_{\mathrm{HS}}^2=o(N),
 \qquad B_X=P_d\mathcal A_X(I-P_d),
\tag{1}
\]

并提出 exterior quarter-turn \(J\) 的充分条件

\[
 \beta_L\|B_XJ-iB_X\|_{\mathrm{op}}=o(1).
\tag{2}
\]

本轮对该分支作逆向审计，得到四点。

第一，对一个固定 finite boundary block，可以精确求出所有实正交
quarter-turn 中的最小 Hilbert--Schmidt defect。若

\[
 H=B^*B=S+iK,
 \qquad S^{\mathsf T}=S,\quad K^{\mathsf T}=-K,
\tag{3}
\]

则

\[
 \boxed{
 \inf_J\|BJ-iB\|_{\mathrm{HS}}^2
 =2\|B\|_{\mathrm{HS}}^2-2\|K\|_{S_1}.}
\tag{4}
\]

所以“事后存在一个好 \(J\)”只是在测量 column covariance 的 imaginary
skew saturation；若不独立构造 \(J\)，它不能被描述为新的算术极化。

第二，笔记 206 的 same-\(BB^*\) no-go 必须作尺度限定。它排除的是：在
one-factor covariance 保持自然非消失尺度时，仅靠 singular data 读取额外
phase cancellation。它**不排除**直接证明

\[
 \boxed{\beta_L\|B_X\|_{\mathrm{op}}=o(1).}
\tag{5}
\]

事实上笔记 206 已有

\[
 \beta_L^2\|B_X\|_{\mathrm{HS}}^2\ll N,
\tag{6}
\]

而式 (5) 与次乘性立即推出式 (1)。这是一个合法、比 arbitrary family
Bessel bound 更具体的 actual-response 路线。

第三，最自然的 lower/upper exterior pairing 在 Hilbert--Schmidt 层面受到
Gabor 局部性的反向约束。对 finite-band Laurent responses，它没有任何
quarter-turn gain；对真实 smooth window，两个 Gabor edges 的交叉 overlap
无条件为 \(O(L/X)\)，因而

\[
 \|B_XJ_0-iB_X\|_{\mathrm{HS}}^2
 =2\|B_X\|_{\mathrm{HS}}^2
 +O\!\left(\frac LX\|B_X\|_{\mathrm{HS}}\right).
\tag{7}
\]

若 \(B_X\) 本身没有小到已经闭合式 (1)，自然 pairing 的 HS defect 就趋于
未极化基准，而不是趋零。

第四，实际 von Mangoldt 权和固定宽度光滑窗的有限实验与式 (7) 一致：自然
pairing 的 normalized HS defect 在三个尺度均为 \(1+O(10^{-6})\)；甚至事后
最优 \(J\) 仍保留 \(0.37\)--\(0.50\) 的 defect。自然 \(J_0\) 的 operator
defect 也比 \(\|B_X\|_{\mathrm{op}}\) 大约 \(1.66\)--\(1.80\) 倍。因此当前
证据支持优先研究式 (5)，而不是继续给 \(J_0\) 增加自由参数。

## 2. 最优 finite quarter-turn 公式

设 \(B\in\mathbb C^{p\times2q}\)，并令

\[
 \mathfrak J_{2q}
 =\{J\in\mathbb R^{2q\times2q}:
 J^{\mathsf T}=-J,\ J^{\mathsf T}J=I\}.
\tag{8}
\]

等价地，每个 \(J\in\mathfrak J_{2q}\) 满足 \(J^2=-I\)。

### 定理 207-A（optimal quarter-turn defect）[T]

若 \(H=B^*B=S+iK\) 如式 (3)，则式 (4) 成立。特别地，

\[
 0\le\|B\|_{mathrm{HS}}^2-\|\operatorname{Im}(B^*B)\|_{S_1}.
\tag{9}
\]

#### 证明

对任意 \(J\in\mathfrak J_{2q}\)，展开得

\[
 \begin{aligned}
 \|BJ-iB\|_{\mathrm{HS}}^2
 &=2\operatorname{tr}H+2i\operatorname{tr}(JH)\\
 &=2\operatorname{tr}H-2\operatorname{tr}(JK),
 \end{aligned}
\tag{10}
\]

因为 \(\operatorname{tr}(JS)=0\)。实反对称矩阵有正交标准形

\[
 U^{\mathsf T}KU
 =\bigoplus_{a=1}^q
 \begin{pmatrix}0&\kappa_a\\-\kappa_a&0\end{pmatrix},
 \qquad \kappa_a\ge0.
\tag{11}
\]

在式 (11) 的基底中，第 \(a\) 个 block 对
\(\operatorname{tr}(JK)\) 的贡献绝对值至多 \(2\kappa_a\)，因为正交矩阵
的每个 entry 绝对值至多 \(1\)。所以

\[
 \operatorname{tr}(JK)\le\|K\|_{S_1}=2\sum_a\kappa_a.
\tag{12}
\]

在每个 \(2\times2\) block 上选择与 \(K\) 极性相反的标准 quarter-turn，
便同时达到式 (12) 的等号。代入式 (10) 得式 (4)。式 (9) 来自左侧非负。
\(\square\)

### 删除与循环性审计

- 式 (4) 是 finite linear algebra，不包含 zeta zeros。
- 若 \(J\) 由 \(K\) 的正交标准形事后选取，它读取了完整 actual boundary
  covariance；该最优 \(J\) 只用于诊断，不能冒充独立构造的 Weil polarization。
- 一个可进入证明链的 \(J\) 必须预先由 Gabor incidence、Vaughan channels、
  Gamma/continuum correspondence 或函数域 Frobenius pairing 指定。

## 3. Covariance no-go 的精确边界与 operator-smallness 路线

### 命题 207-B（one-factor operator-smallness certificate）[T]

对任意 Hilbert--Schmidt \(B\)，

\[
 \|BB^{\mathsf T}\|_{\mathrm{HS}}
 \le\|B\|_{\mathrm{HS}}\|B\|_{\mathrm{op}}.
\tag{13}
\]

因此式 (5)--(6) 推出式 (1)，从而推出 supercritical boundary lemma。

#### 证明

式 (13) 是

\[
 \|UV\|_{\mathrm{HS}}
 \le\|U\|_{\mathrm{HS}}\|V\|_{\mathrm{op}}
\]

应用于 \(U=B\)、\(V=B^{\mathsf T}\)，并用
\(\|B^{\mathsf T}\|_{\mathrm{op}}=\|B\|_{\mathrm{op}}\)。故

\[
 \begin{aligned}
 \beta_L^4\|BB^{\mathsf T}\|_{\mathrm{HS}}^2
 &\le
 \left(\beta_L^2\|B\|_{\mathrm{HS}}^2\right)
 \left(\beta_L^2\|B\|_{\mathrm{op}}^2\right)\\
 &=o(N).
 \end{aligned}
\]

再用笔记 206 定理 206-C。\(\square\)

笔记 206 定理 206-G 的矩阵对仍然是 sharp：在固定相同 \(BB^*\) 时，
singular data 不区分 \(BB^{\mathsf T}=0\) 与最大 coherence。但该反例的
\(\|B\|_{\mathrm{op}}\) 固定为 \(1\)，所以它不反驳式 (5)。正确结论是：

> natural-scale covariance data 不产生 phase cancellation；vanishing
> one-factor operator norm 则通过缩小整个 boundary block 而合法闭合目标。

这两种机制必须分开记录。

## 4. 自然 lower/upper pairing 的局部化 no-go

把 exterior space 分成

\[
 Q_-=\mathbf1_{\{\ell<0\}},
 \qquad Q_+=\mathbf1_{\{\ell\ge d\}},
\tag{14}
\]

并按 pairs

\[
 -r\longleftrightarrow d-1+r,
 \qquad r=1,2,\ldots
\tag{15}
\]

定义自然 quarter-turn

\[
 J_0=
 \begin{pmatrix}0&-I\\I&0\end{pmatrix}.
\tag{16}
\]

写

\[
 B=[B_-\ B_+],
 \qquad B_-=P\mathcal A Q_-,\quad B_+=P\mathcal A Q_+,
\tag{17}
\]

其中两块 columns 按式 (15) 排列。

### 引理 207-C（natural-pairing defect identity）[T]

精确地

\[
 \boxed{
 \|BJ_0-iB\|_{\mathrm{HS}}^2
 =2\|B\|_{\mathrm{HS}}^2
 -4\operatorname{Im}\langle B_-,B_+\rangle_{\mathrm{HS}}.}
\tag{18}
\]

#### 证明

由式 (16)，

\[
 BJ_0-iB
 =[B_+-iB_-\ ,\ -B_--iB_+].
\]

分别展开两个 block 的平方范数即得式 (18)。\(\square\)

### 定理 207-D（finite-band natural quarter-turn no-go）[N]

设 \(\mathcal A\) 是任意 complex matrix，满足

\[
 \mathcal A_{jk}=0\qquad(|j-k|>w),
\tag{19}
\]

且 \(d>2w\)。则由式 (14)--(17) 得到的非零 boundary blocks 满足

\[
 \langle B_-,B_+\rangle_{\mathrm{HS}}=0,
\tag{20}
\]

从而

\[
 \boxed{
 \|BJ_0-iB\|_{\mathrm{HS}}^2=2\|B\|_{\mathrm{HS}}^2.}
\tag{21}
\]

#### 证明

对 lower column \(\ell=-r\)，式 (19) 强制其非零 rows 满足

\[
 0\le j\le w-r<w.
\]

对 paired upper column \(\ell=d-1+r\)，非零 rows 满足

\[
 d-w\le j\le d-1.
\]

因 \(d>2w\)，两组 row supports 不交，所以式 (20) 成立。再用式 (18)。
\(\square\)

该 no-go 不要求 \(\mathcal A\) self-adjoint 或 complex symmetric；它只读取
Gabor/Laurent diagonal locality。自然 pairing 把两个空间上分离的 edge
responses 配在一起，不能产生 \(B_+\approx iB_-\) 所需的同向 row geometry。

## 5. 实际 smooth response 的 two-edge tunnelling bound

令 \(R_-\) 投影到 rows \(0\le j<d/2\)，\(R_+=I-R_-\)，并定义

\[
 \tau_X^2
 =\|R_+B_-\|_{\mathrm{HS}}^2
 +\|R_-B_+\|_{\mathrm{HS}}^2.
\tag{22}
\]

### 定理 207-E（actual two-edge overlap suppression）[T]

在笔记 204 的统一 \(W^{2,1}\) 窗口正则性、\(d\asymp XL\) 下，

\[
 \boxed{\tau_X^2\ll\frac{L^2}{X^2}.}
\tag{23}
\]

并且式 (7) 成立。

#### 证明

式 (22) 中每个 matrix entry 的 Fourier difference 都满足
\(|j-\ell|\ge d/2\)。沿用笔记 206 定理 206-D 的 diagonal-fibre
Montgomery--Vaughan 分解，但只对 \(|r|\ge d/2\) 求和。统一二阶导数界给

\[
 |\widehat q_x(r)|\ll\frac{L}{r^2}.
\tag{24}
\]

因此 diagonal part 对每个 \(q_x\) 的 tail 为

\[
 \sum_{|r|\ge d/2}\min(d,|r|)|\widehat q_x(r)|^2
 \ll\frac{L^2}{d^2},
\tag{25}
\]

而 Montgomery--Vaughan remainder 所需的无权 tail 为

\[
 \sum_{|r|\ge d/2}|\widehat q_x(r)|^2
 \ll\frac{L^2}{d^3}.
\tag{26}
\]

再用

\[
 \sum_{n\le X}|b_n|^2\ll L^2,
 \qquad \Delta^{-1}\ll LX,
\]

得到

\[
 \tau_X^2
 \ll\frac{L^4}{d^2}
 +LX\frac{L^4}{d^3}
 \ll\frac{L^2}{X^2},
\]

即式 (23)。另一方面，按 \(R_-+R_+=I\) 分解 Frobenius inner product，
Cauchy--Schwarz 给

\[
 |\langle B_-,B_+\rangle_{\mathrm{HS}}|
 \le\|B\|_{\mathrm{HS}}\tau_X.
\tag{27}
\]

把式 (23)、式 (27) 代入式 (18)，得到式 (7)。\(\square\)

### 推论 207-F（natural HS-polarization dichotomy）[N]

若沿某尺度列

\[
 \frac{L}{X}=o\!\left(\|B_X\|_{\mathrm{HS}}\right),
\]

则

\[
 \frac{\|B_XJ_0-iB_X\|_{\mathrm{HS}}^2}
 {2\|B_X\|_{\mathrm{HS}}^2}\longrightarrow1.
\tag{28}
\]

反之，若 \(\|B_X\|_{\mathrm{HS}}=O(L/X)\)，则

\[
 \beta_L^4\|B_XB_X^{\mathsf T}\|_{\mathrm{HS}}^2
 \le\beta_L^4\|B_X\|_{\mathrm{HS}}^4
 =O(X^{-4})=o(N),
\]

supercritical boundary 已经闭合。

因此在尚未解决的 regime，自然 lower/upper pairing 不可能在 HS 层面提供
polarization gain。该结论不自动否定式 (2) 的 operator-norm 版本；HS defect
可以分散在很多小奇异方向。operator route 必须由式 (5) 或直接谱估计单独审计。

## 6. 实际 von Mangoldt finite audit [E]

脚本 `scripts/boundary_quarter_turn_audit.py` 使用：

1. \(b_n=-(2\pi)^{-1}\Lambda(n)n^{-1/2}\) 的全部 prime powers；
2. 两端固定宽度 smootherstep transition 的实偶 compact window；
3. \(T=X\)、\(h=2\pi/L\)、\(d=\operatorname{round}(TL/(2\pi))\)；
4. 完整 \(w=d\) lower/upper exterior 截断。

结果为：

\[
\begin{array}{c|c|c|c|c|c}
X&d&\beta\|B\|_{op}&\beta\|BJ_0-iB\|_{op}
&\|BJ_0-iB\|_{HS}^2/(2\|B\|_{HS}^2)&\text{optimal HS fraction}\\ \hline
64&42&0.205870&0.366014&0.99999973&0.421592\\
128&99&0.199070&0.358097&1.00000075&0.495394\\
256&226&0.152361&0.252894&0.99999999&0.372035
\end{array}
\tag{29}
\]

此外

\[
 \frac{\|BJ_0-iB\|_{op}}{\|B\|_{op}}
 =1.7779,\ 1.7988,\ 1.6598,
\tag{30}
\]

而

\[
 \frac{\|BB^{\mathsf T}\|_{HS}}{\|BB^*\|_{HS}}
 =0.7793,\ 0.8433,\ 0.7793.
\tag{31}
\]

有限数据没有显示 natural circularity；natural quarter-turn 反而比直接
operator block 更差。\(\beta\|B\|_{op}\) 在这些尺度下降，值得继续检验
式 (5)，但三个有限点不能升级为 little-oh。

## 7. 下一最小引理与止损条件

路线 A1c 现在分成有严格先后次序的两个目标。

### A1c-op（优先）[O]

对 actual boundary synthesis 证明

\[
 \boxed{
 \|P_d\mathcal A_X(I-P_d)\|_{op}=o(L).}
\tag{32}
\]

这应从式 (18) 的 prime fibres 出发，使用 response-specific Vaughan Type I/II
operator Gram；不得把 \(b_n\) 换成任意系数的 all-direction Bessel family。

### A1c-phase（仅在 A1c-op 失败后）[O]

若存在无条件 lower bound 证明 \(\beta\|B_X\|_{op}\not\to0\)，再直接估计
\(B_XB_X^{\mathsf T}\) 的无共轭 phase cancellation，或寻找一个不是简单
lower/upper pairing 的 arithmetic \(J\)。

### 止损

- 自然 \(J_0\) 的 HS-polarization 路线由定理 207-D--F 停止。
- 不允许用事后最优 \(J\) 的存在性冒充极化构造；式 (4) 显示那只是完整
  covariance 的重新编码。
- 若式 (32) 被证明等价蕴含当前未知的 full Selberg/RH-strength bound，则停止
  operator-smallness 路线，并把该等价写成障碍定理。

## 8. Weil 型结构接口与适用范围

- 定理 207-A 是 finite polarization diagnostic，不构造上同调型 Weil
  polarization。
- 定理 207-B 属于显式公式型部分配置的 finite-boundary bridge；其唯一未知量
  是实际 prime response operator norm。
- 定理 207-D--F 说明“把两个 Gabor edges 形式配对”不等于 Hodge--Riemann
  极化；局部性甚至使该形式 pairing 正交。
- 固定本原 Dirichlet \(L\) 函数保留式 (18)、式 (23) 的绝对 majorant，但
  式 (32) 必须保留角色相位重新证明。
- 函数域模型若有真正的 Frobenius dual boundary states，应检查其 pairing 是否
  在同一 row-response space 内作用；简单复制数域 lower/upper Gabor pairing
  会落入定理 207-D 的 no-go。

## 9. 结论边界

- 本轮没有证明式 (32)，没有闭合 supercritical adjacent channel。
- 没有得到四矩改进、零点比例改进或 RH/GRH。
- `[E]` 表中下降趋势不作为渐近证据。
- 已完成的是：修正 covariance no-go 的适用边界；给出一个新的无条件
  operator-smallness 充分归约；精确求解 finite quarter-turn 最优化；并排除
  natural lower/upper HS-polarization 这一大类局部化证明路线。
