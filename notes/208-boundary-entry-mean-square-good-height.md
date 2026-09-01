# 208. Boundary entry 正均方障碍与 exceptional good-height 桥梁

日期：2026-09-02

分支：MOM-1 / 路线 A

状态：首个 lower-boundary prime response 的平核极限、Montgomery--Vaughan
均方渐近、uniform operator-smallness no-go、短区间 bad-height 结论与相对稠密
good-height 的零点比例传递为 [T]/[N]；exceptional operator-smallness 与直接
pseudocovariance cancellation 为 [O]；有限精确积分为 [E]。

## 1. 本轮结论与路线修正

笔记 207 给出合法充分条件

\[
 \beta_L\|B_X(T)\|_{\mathrm{op}}=o(1),
 \qquad B_X(T)=P_d\mathcal A_X(T)(I-P_d),
\tag{1}
\]

并指出它与已知

\[
 \beta_L^2\|B_X(T)\|_{\mathrm{HS}}^2\ll N(T)
\tag{2}
\]

合并后足以闭合 supercritical adjacent boundary。

本轮证明式 (1) **不可能对所有高度一致成立**。原因已经出现在单个 matrix
entry。取第一个 lower exterior column \(\ell=-1\) 与 row \(j=0\)，则

\[
 S_X(T):=(B_X(T))_{0,-1}
 =\sum_{n\le X}b_nc_{\log n}(1)
 n^{i(T-h/2)}.
\tag{3}
\]

对 fixed-width flat-core smooth window，无条件有

\[
 \boxed{
 \frac{\beta_L^2}{X}
 \int_X^{2X}|S_X(T)|^2\,dT
 \longrightarrow\frac1{4\pi^2}.}
\tag{4}
\]

由于 \(\|B_X(T)\|_{op}\ge|S_X(T)|\)，得到

\[
 \liminf_{X\to\infty}
 \sup_{X\le T\le2X}
 \beta_L\|B_X(T)\|_{op}
 \ge\frac1{2\pi}.
\tag{5}
\]

更强地，在任意长度

\[
 H_X\gg X/L
\]

并满足 \(H_XL/X\to\infty\) 的高度区间上，同一 normalized mean square
仍趋于 \(1/(4\pi^2)\)。所以 uniform operator-smallness 不能在任何这种区间
上成立。

这不是 RH 等价障碍；它是 prime-side mean-value theorem。它并不排除：

1. 在每个相对短区间中选择一个 exceptional good height；
2. \(B_X\) 的 operator norm 不小，但无共轭 pseudocovariance
   \(B_XB_X^{\mathsf T}\) 仍因 phase circularity 而小。

本轮另证明一个一般传递定理：若完整零点比例结论能在相对间距
\(o(T)\) 的 good heights 上成立，则 Riemann--von Mangoldt 计数可把它传到
所有高度。因此下一最小引理应改成“相对稠密 exceptional heights”，不能继续
要求式 (1) uniform in height。

## 2. Flat-core window 与第一个 boundary fibre

沿用

\[
 L=\log X,\qquad h=\frac{2\pi}{L},\qquad
 b_n=-\frac1{2\pi}\frac{\Lambda(n)}{\sqrt n}.
\tag{6}
\]

本轮增加实际固定过渡层假设：存在与 \(L\) 无关的 \(C>0\)，使

\[
 0\le\phi_L\le1,
 \qquad \phi_L(u)=1\quad(|u|\le L/2-C),
 \qquad \operatorname{supp}\phi_L\subset[-L/2,L/2].
\tag{7}
\]

Alpöge--Furman 型 fixed smooth cutoff 以及审计脚本使用的 smootherstep window
均满足式 (7)。该假设比笔记 204 的抽象 uniform \(W^{2,1}\) 更具体；本轮的
正极限常数不声称适用于任意非平坦窗口。

令

\[
 q_x(u)=\phi_L(u)\phi_L(x-u),
 \qquad
 c_x(r)=e^{-irhx/2}\widehat q_x(r)\in\mathbb R.
\tag{8}
\]

### 引理 208-A（first centred mode flat limit）[T]

在式 (7) 下，一致于 \(0\le x\le L\)，

\[
 \boxed{
 c_x(1)=\frac{\sin(\pi x/L)}{\pi}+O_C(L^{-1}).}
\tag{9}
\]

并且

\[
 a_L:=L^{-1}\|\phi_L\|_2^2=1+O_C(L^{-1}),
 \qquad
 \beta_L=\frac{2\pi}{L}\left(1+O_C(L^{-1})\right).
\tag{10}
\]

#### 证明

平窗 \(\mathbf1_{[-L/2,L/2]}\) 对应的 \(q_x\) 是以 \(x/2\) 为中心、长度
\(L-x\) 的 indicator。因此其 centred first coefficient 为

\[
 \frac1L\int_{-(L-x)/2}^{(L-x)/2}e^{ihv}\,dv
 =\frac{\sin(\pi(1-x/L))}{\pi}
 =\frac{\sin(\pi x/L)}{\pi}.
\tag{11}
\]

式 (7) 的真实 \(q_x\) 与该 indicator 只在至多四个总长度
\(O(C)\) 的 transition pieces 上不同，且振幅至多 \(1\)。所以其 normalized
Fourier coefficient 相差 \(O(C/L)\)，得到式 (9)。同理，
\(\phi_L^2\) 与平窗 indicator 的 \(L^1\) 差为 \(O(C)\)，得到式
(10)。\(\square\)

笔记 206 的 exact physical-fibre identity 给

\[
 (\mathcal A_X(T))_{j\ell}
 =\sum_{n\le X}b_nc_{\log n}(j-\ell)
 n^{i[T+h(j+\ell)/2]}.
\]

取 \((j,\ell)=(0,-1)\) 即为式 (3)。

## 3. Arithmetic coefficient mass

定义

\[
 a_{n,X}=b_nc_{\log n}(1)n^{-ih/2}.
\tag{12}
\]

相位不改变绝对值。笔记 203 已经从

\[
 \sum_{n\le y}\frac{\Lambda(n)^2}{n}
 =\frac12(\log y)^2+O(\log y)
\tag{13}
\]

证明测度收敛

\[
 L^{-2}\sum_{n\le X}\frac{\Lambda(n)^2}{n}
 \delta_{\log n/L}
 \Longrightarrow r\,dr.
\tag{14}
\]

### 引理 208-B（first-fibre coefficient mass）[T]

\[
 \boxed{
 L^{-2}\sum_{n\le X}|a_{n,X}|^2
 \longrightarrow\frac1{16\pi^4}.}
\tag{15}
\]

#### 证明

由式 (6)、式 (9) 和式 (14)，

\[
 \begin{aligned}
 L^{-2}\sum_{n\le X}|a_{n,X}|^2
 &\longrightarrow
 \frac1{4\pi^2}
 \int_0^1r\left(\frac{\sin(\pi r)}{\pi}\right)^2dr.
 \end{aligned}
\]

函数 \(\sin^2(\pi r)\) 关于 \(1/2\) 对称，所以

\[
 \int_0^1r\sin^2(\pi r)dr
 =\frac12\int_0^1\sin^2(\pi r)dr
 =\frac14.
\]

这给式 (15)。式 (9) 的 \(O(L^{-1})\) 误差乘式 (13) 后仅贡献
\(O(L)\)，除以 \(L^2\) 消失。\(\square\)

## 4. Positive mean-square theorem

### 定理 208-C（first boundary entry positive mean square）[T]

在式 (7) 下，式 (4) 成立。更一般地，设

\[
 I_X=[Y_X,Y_X+H_X],\qquad Y_X\asymp X,
\]

且

\[
 \frac{H_XL}{X}\longrightarrow\infty.
\tag{16}
\]

则

\[
 \boxed{
 \frac{\beta_L^2}{H_X}\int_{I_X}|S_X(T)|^2dT
 \longrightarrow\frac1{4\pi^2}.}
\tag{17}
\]

#### 证明

Montgomery--Vaughan Dirichlet-polynomial mean-value theorem [R] 给任意长度
\(H_X\) 的 interval

\[
 \int_{I_X}\left|\sum_{n\le X}a_{n,X}n^{iT}\right|^2dT
 =H_X\sum_{n\le X}|a_{n,X}|^2
 +O\!\left(\sum_{n\le X}n|a_{n,X}|^2\right).
\tag{18}
\]

由 \(|c_x(1)|\le1\)，

\[
 \sum_{n\le X}n|a_{n,X}|^2
 \ll\sum_{n\le X}\Lambda(n)^2.
\tag{19}
\]

对式 (13) 作 Abel summation 得

\[
 \sum_{n\le X}\Lambda(n)^2\ll XL.
\tag{20}
\]

所以式 (18) 除以 \(H_X\) 并乘 \(\beta_L^2\) 后，error 为

\[
 O\!\left(\frac{X}{H_XL}\right)=o(1).
\]

主项由式 (10)、式 (15) 给

\[
 \beta_L^2\sum|a_{n,X}|^2
 \longrightarrow
 4\pi^2\cdot\frac1{16\pi^4}
 =\frac1{4\pi^2}.
\]

这证明式 (17)，取 \(Y_X=X,H_X=X\) 即得式 (4)。\(\square\)

外部输入 [R] 只是 Montgomery--Vaughan mean value；它不使用 zeros、RH、
素数对猜想或四阶矩。

## 5. Uniform operator-smallness no-go

### 推论 208-D（uniform A1c-op obstruction）[N]

式 (5) 成立。因此不存在

\[
 \sup_{X\le T\le2X}
 \beta_L\|B_X(T)\|_{op}=o(1).
\tag{21}
\]

更一般地，在满足式 (16) 的任意 intervals \(I_X\) 上，不可能有

\[
 \sup_{T\in I_X}\beta_L\|B_X(T)\|_{op}=o(1).
\tag{22}
\]

#### 证明

因为 operator norm 支配每个 entry，

\[
 \beta_L^2\|B_X(T)\|_{op}^2
 \ge\beta_L^2|S_X(T)|^2.
\]

区间 supremum 的平方至少为右侧区间平均。应用定理 208-C 并开方得到式
(5)、式 (21)--(22)。\(\square\)

该障碍排除的是 all-height 或 interval-uniform smallness。它没有证明每个高度都
bad，也没有给 good heights 的密度下界；均方正值允许 isolated 或稀疏 small
values。

## 6. Exceptional good heights 如何仍能服务零点比例

设 \(N(T)\) 为总非平凡零点计数，\(S(T)\) 为某个单调的目标零点计数，例如
简单且位于临界线的零点数。

### 定理 208-E（relative-dense good-height transfer）[T]

设 \(0\le c\le1\)。若存在 good-height 集合 \(\mathcal G\) 与函数
\(H(T)=o(T)\)，使每个充分大的 \(T\) 都存在

\[
 T\le T'\le T+H(T),\qquad T'\in\mathcal G,
\tag{23}
\]

且沿 \(T'\in\mathcal G\)

\[
 S(T')\ge cN(T')+o(N(T')),
\tag{24}
\]

则对所有实高度

\[
 \boxed{S(T)\ge cN(T)+o(N(T)).}
\tag{25}
\]

#### 证明

Riemann--von Mangoldt 公式 [R] 给

\[
 N(T')-N(T)
 =O\!\left((T'-T)\log T+\log T\right)
 =o(T\log T)=o(N(T)).
\tag{26}
\]

单调性给

\[
 S(T)\ge S(T')-[N(T')-N(T)].
\]

把式 (24)、式 (26) 代入，并用 \(N(T')=N(T)+o(N(T))\)，得到式
(25)。\(\square\)

该传递说明不需要在每个实高度直接验证完整四矩证书；相对 gaps 为 \(o(T)\)
的 good endpoints 已足够。但所有通道估计必须在同一组 good heights 上同时成立。

## 7. 修正后的下一最小引理

### A1c-good-height [O]

证明存在集合 \(\mathcal G\)，relative gaps 为 \(o(T)\)，且沿
\(T\in\mathcal G\)

\[
 \beta_L\|B_X(T)\|_{op}=o(1),
\tag{27}
\]

或者直接证明

\[
 \beta_L^4\|B_X(T)B_X(T)^{\mathsf T}\|_{HS}^2=o(N(T)).
\tag{28}
\]

式 (27) 比 uniform A1c-op 弱，且由定理 208-E 保留零点比例接口。它仍十分
强：必须同时压小全部 boundary directions，而单个 entry 的均方是正常数。

### 止损条件

1. uniform operator-smallness 路线由推论 208-D 停止；
2. 不得把有限样本中很小的 \(|S_X(T)|\) 升级为 good-height existence；
3. 若式 (27) 的 relative-density 蕴含一个已知 RH-strength critical-line prime
   polynomial bound，则把该等价写成障碍并转回 direct pseudocovariance；
4. good heights 必须对 adjacent、alternating、\(3+1\)、\(4+0\) 和背景项共同
   可用，不能为每个通道分别选择不同 endpoints。

## 8. 最小公理、删除审计与模型范围

1. **flat core / fixed transition**：只负责显式常数 \(1/(4\pi^2)\)。删除后
   仍可由窗口 profile 得到
   \(a_\infty^{-2}\int_0^1r|c(r)|^2dr\) 型常数；若 first mode
   profile 恒零，本 no-go 需换另一个 mode。
2. **von Mangoldt square measure**：给式 (15) 的正质量。它是无条件
   prime-side input。
3. **Montgomery--Vaughan mean value**：只消去 height-average 的
   off-diagonal；没有读取 zeta zeros。
4. **operator norm dominates an entry**：把 scalar 正均方传到 matrix no-go。
   删除 matrix all-direction 要求、改估实际 \(BB^{\mathsf T}\)，该障碍不再适用。
5. **Riemann--von Mangoldt counting**：只用于 good-height 到 all-height 的
   结论传递，不制造 good heights。

适用范围：

- Riemann zeta 满足全部算术输入。
- 固定本原 Dirichlet \(L\) 函数的单 entry 含角色相位；diagonal square mass
  不变，Montgomery--Vaughan error 仍适用，所以同型正均方 no-go 成立。
- Dedekind/automorphic 情形需要相应 coefficient square-measure 极限；若
  Rankin--Selberg residue 为正，得到相应正常数。
- 函数域有限 Fourier 模型中 height averaging 的含义不同，不能自动套用；应直接
  检查 Frobenius orbit 上的 discrete mean square。

## 9. 有限精确均方审计 [E]

脚本 `scripts/boundary_entry_mean_square_audit.py`：

1. 使用全部 prime powers 的实际 \(\Lambda(n)/\sqrt n\) 权；
2. 数值积分 fixed-width smootherstep window 的 \(c_{\log n}(1)\)；
3. 以 finite exponential kernel 精确计算 \([X,2X]\) 均方，而非 Monte Carlo；
4. 比较 diagonal mass、exact mean 与极限 \(1/(4\pi^2)\)；
5. 另采样 entry 的 min/median/max，只作诊断。

结果：

\[
\begin{array}{c|c|c|c|c|c}
X&\beta^2D_X&\beta^2M_X&\beta^2(M_X-D_X)
&\operatorname{median}|\beta S_X|&\max|\beta S_X|\\ \hline
128&0.0215532&0.0210031&-0.0005502&0.13132&0.26812\\
256&0.0222233&0.0221595&-0.0000638&0.13761&0.32301\\
512&0.0227929&0.0226690&-0.0001239&0.13321&0.32947\\
1024&0.0232680&0.0232685& 0.0000005&0.13610&0.35087
\end{array}
\tag{29}
\]

极限常数为

\[
 \frac1{4\pi^2}=0.0253302959\ldots.
\]

finite off-diagonal 已显著小于 diagonal，且 normalized RMS 接近
\(1/(2\pi)\)。样本 minimum 很小，说明 exceptional scalar cancellations 在有限
尺度存在；它不证明完整 operator norm 可同时变小，也不证明 relative-dense
good heights。

## 10. RH/GRH 循环性与结论边界

- 本轮没有闭合 supercritical boundary，也没有改善零点比例。
- 推论 208-D 是 uniform operator-smallness 路线的严格 no-go，不是 RH no-go。
- 定理 208-E 只说明 good heights 若存在时如何传递；它不构造这些 heights。
- 式 (28) 仍是实际无共轭 prime-response 输入，不是 Weil positivity 的改写。
- 自然 quarter-turn 已由笔记 207 在 HS 层面停止；本轮又停止 uniform
  operator-smallness。下一轮必须研究 exceptional-height joint response 或直接
  pseudocovariance，不能继续扩写同一个 uniform norm criterion。
