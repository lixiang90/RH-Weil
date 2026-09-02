# 238. Band-energy Bessel 障碍与 exact physical-response Gram

日期：2026-09-03

分支：MOM-1 / 路线 A1r；接口：fixed-power alternating response /
Vaughan--Brownian physical direction

状态：in-band positive modulation 的 bounded exact response、离散 band energy
平方根下界、$\theta=3/4$ 尺度分离及 six-window physical Gram identity 为
[T]；以全 band $L^2$ energy 作为必要输入为 [N]；actual Type-I/II physical
Gram estimate 为 [O]。本笔记不更新 PDF，不改变四矩比例的 [C] 状态。

## 1. 从笔记 237 留下的问题

笔记 237 证明 cumulative discrepancy 会看见 band 以下的慢调制，因而不是
exact $[1,2]$ response 的必要输入。该笔记提出更具频率选择性的充分证书

\[
 {\mathcal B}_{Q,D}(\nu)^2
 =
 \frac1D\sum_{k=0}^{D-1}
 |\widehat\nu(\xi_k)|^2,
 \qquad
 \xi_k=1+\frac{k}{Q},
\tag{1}
\]

并由 Cauchy--Schwarz 得

\[
 \left|
 \frac1D\sum_{k=0}^{D-1}\Re\widehat\nu(\xi_k)
 \right|
 \le {\mathcal B}_{Q,D}(\nu).
\tag{2}
\]

式 (1) 已删除低频盲目性，但仍把实际 all-ones response direction 换成整个
band vector 的欧氏长度。本轮证明这个损失也可以是幂级的：一个很窄的
in-band coherent line 对物理平均只贡献常数，却使式 (1) 达到 $\sqrt M$。

## 2. Exact finite band 与内部调制

令

\[
 Q>0,\qquad D=\operatorname{round}(Q),\qquad
 \xi_k=1+\frac{k}{Q},
\tag{3}
\]

以及

\[
 K_{Q,D}(t)
 =
 \frac1D\sum_{k=0}^{D-1}\cos(2\pi\xi_k t).
\tag{4}
\]

固定 $0<\varepsilon<1$。对偶整数 $M\ge4$ 定义

\[
 \xi_\star=\frac32,\qquad
 d\mu_M(t)
 =
 \left(1+\varepsilon\cos(2\pi\xi_\star t)\right)
 {\bf1}_{[-M,M]}(t)\,dt.
\tag{5}
\]

这是 even positive measure。因为 $\xi_\star M=3M/2$ 为整数，

\[
 \mu_M([-M,M])=2M.
\tag{6}
\]

所以 constant reference 恰为 $dt$，且 centered measure 是

\[
 d\nu_M(t)
 =
 \varepsilon\cos(2\pi\xi_\star t)
 {\bf1}_{[-M,M]}(t)\,dt.
\tag{7}
\]

与笔记 237 不同，调制频率 $\xi_\star$ 位于实际 band 内部。

## 3. 物理 all-ones response 只有常数尺度

置

\[
 I_M(u)
 =
 \int_{-M}^{M}e^{2\pi iut}\,dt
 =
 \begin{cases}
 2M,&u=0,\\
 \dfrac{\sin(2\pi Mu)}{\pi u},&u\ne0.
 \end{cases}
\tag{8}
\]

则

\[
 \widehat\nu_M(\xi)
 =
 \frac{\varepsilon}{2}
 \left(I_M(\xi-\xi_\star)+I_M(\xi+\xi_\star)\right).
\tag{9}
\]

### 引理 238-A（continuous-band response）[T]

若

\[
 K(t)=\int_1^2\cos(2\pi\xi t)\,d\xi,
\tag{10}
\]

则

\[
 \int_{-M}^{M}K(t)\,dt=O(M^{-1}),
\tag{11}
\]

且

\[
 \int_{-M}^{M}K(t)\cos(3\pi t)\,dt
 =
 \frac12+O(M^{-1}).
\tag{12}
\]

#### 证明

式 (11) 是 band endpoints 的一次 Dirichlet integration by parts。由

\[
 K(t)=\frac{\sin(4\pi t)-\sin(2\pi t)}{2\pi t}
\tag{13}
\]

及积化和差，

\[
 K(t)\cos(3\pi t)
 =
 \frac{\sin(7\pi t)-\sin(5\pi t)+2\sin(\pi t)}
 {4\pi t}.
\tag{14}
\]

对整条实线积分时，三个 normalized Dirichlet integrals 分别为 $1,1,1$，
所以式 (14) 的积分是 $(1-1+2)/4=1/2$。每个频率都与零相隔固定距离，
截去 $|t|>M$ 的尾由 Dirichlet test 为 $O(M^{-1})$。$\square$

### 引理 238-B（finite-grid quadrature）[T]

令

\[
 G_M(\xi)
 =
 \int_{-M}^{M}
 \left(1+\varepsilon\cos(3\pi t)\right)
 \cos(2\pi\xi t)\,dt.
\tag{15}
\]

则

\[
 \frac1D\sum_{k=0}^{D-1}G_M(\xi_k)
 =
 \int_1^2G_M(\xi)\,d\xi
 +O_\varepsilon\left(\frac{M^2}{Q}+\frac{M}{Q}\right).
\tag{16}
\]

#### 证明

逐项微分式 (15) 给

\[
 \sup_\xi|G_M'(\xi)|
 \le
 2\pi(1+\varepsilon)\int_{-M}^{M}|t|\,dt
 \ll_\varepsilon M^2.
\tag{17}
\]

步长 $1/Q$ 的 rectangle rule 因而有 $O(M^2/Q)$ 误差。又因
$D/Q=1+O(Q^{-1})$，离散区间右端与 $2$ 相差 $O(Q^{-1})$，而
$|G_M|\le2M(1+\varepsilon)$；端点与 normalization 误差合计
$O(M/Q)$。$\square$

### 定理 238-C（bounded physical response）[T]

若 $Q\ge M^2$，则

\[
 \boxed{
 \int K_{Q,D}(t)\,d\mu_M(t)
 =
 \frac{\varepsilon}{2}
 +O_\varepsilon\left(
 \frac1M+\frac{M^2}{Q}
 \right).}
\tag{18}
\]

特别地，在 $Q/M^2\to\infty$ 时 physical response 趋于
$\varepsilon/2$，而不是按 $\sqrt M$ 或 $M$ 增长。

#### 证明

交换式 (4) 与式 (5) 的有限求和、积分，左边等于式 (16) 左边。
引理 238-A 给式 (16) 主项

\[
 O(M^{-1})
 +\varepsilon\left(\frac12+O(M^{-1})\right).
\]

再吸收 $M/Q\le M^2/Q$。$\square$

## 4. 同一测度的 exact discrete band energy

### 定理 238-D（band-energy square-root lower bound）[T]

存在绝对常数 $c_0>0$，使充分大偶整数 $M$ 及
$Q\ge64M$ 时

\[
 \boxed{
 {\mathcal B}_{Q,D}(\nu_M)
 \ge c_0\varepsilon\sqrt M.}
\tag{19}
\]

例如可取 $c_0=1/\sqrt{160}$。

#### 证明

考虑 grid indices

\[
 {\mathcal K}_M
 =
 \left\{0\le k<D:
 |\xi_k-\xi_\star|\le\frac1{8M}\right\}.
\tag{20}
\]

该 interval 的 $k$-长度为 $Q/(4M)$。因 $D=Q+O(1)$ 且
$\xi_\star$ 距 band endpoints 均为 $1/2$，充分大 $M$ 时

\[
 |{\mathcal K}_M|\ge\frac{Q}{8M},
 \qquad
 \frac{|{\mathcal K}_M|}{D}\ge\frac1{10M}.
\tag{21}
\]

若 $|u|\le1/(8M)$，则 $|2\pi Mu|\le\pi/4$。由正弦在该区间的
concavity chord bound，

\[
 I_M(u)\ge M.
\tag{22}
\]

另一方面，对 $k\in{\mathcal K}_M$，

\[
 |I_M(\xi_k+\xi_\star)|
 \le \frac1{\pi(\xi_k+\xi_\star)}
 \le1.
\tag{23}
\]

由式 (9)，充分大 $M$ 时

\[
 |\widehat\nu_M(\xi_k)|
 \ge\frac{\varepsilon M}{4}
 \qquad(k\in{\mathcal K}_M).
\tag{24}
\]

把式 (21)、(24) 代入式 (1)，

\[
 {\mathcal B}_{Q,D}(\nu_M)^2
 \ge
 \frac1{10M}\frac{\varepsilon^2M^2}{16}
 =
 \frac{\varepsilon^2M}{160}.
\]

取平方根即得。$\square$

### 障碍推论 238-E（ordinary band Bessel is not necessary）[N]

在 even positive measures 类上，

\[
 \text{physical response}=o(L^4)
\quad\Longrightarrow\quad
 {\mathcal B}_{Q,D}(\nu)=o(L^4)
\tag{25}
\]

为假。

更具体地，取偶整数 $n\to\infty$ 并置

\[
 X_n=n^4,\qquad L_n=\log X_n,\qquad
 Q_n=X_nL_n,\qquad M_n=n^2.
\tag{26}
\]

则

\[
 \int K_{Q_n,D_n}\,d\mu_{M_n}
 =
 \frac{\varepsilon}{2}+O(L_n^{-1})
 =
 o(L_n^4),
\tag{27}
\]

但

\[
 {\mathcal B}_{Q_n,D_n}(\nu_{M_n})
 \gg\varepsilon n
 \gg L_n^4.
\tag{28}
\]

#### 证明

这里 $Q_n=M_n^2L_n$，故定理 238-C 给式 (27)。定理 238-D 给式
(28)，且 $n/(\log n)^4\to\infty$。$\square$

这个反例与 $\theta=3/4$ 的证明尺度 $M=X^{1/2}$ 完全一致。它不声称 actual
prime determinant measure 具有 narrow spectral line；它严格否定的是把
ordinary full-band energy 当成 response closure 的必要或结构上无损输入。

## 5. Six-window overlap 的 exact physical Gram

普通 band energy 失败后，必须保留实际 all-ones coefficient direction。笔记
216 的 overlap 已自然提供所需 Hilbert 空间。

对一个 fixed factor/aperture cell 的 ratio atoms $i=(a,b)$，置

\[
 s_i=\log(a/b),\qquad b_i=b_ab_b,
\tag{29}
\]

并沿笔记 216-(8) 记窗口函数为 $P_i$。在长度为 $L$ 的圆周上定义

\[
 F_i(v)=P_i(v+s_i),
\qquad
 \langle f,g\rangle_H
 =
 \frac1L\int_{-L/2}^{L/2}f(v)\overline{g(v)}\,dv.
\tag{30}
\]

变量代换 $u=v+s_i$ 给

\[
 \langle F_i,F_j\rangle_H
 =
 \frac1L\int
 P_i(u)P_j(u-(s_i-s_j))\,du
 =
 W_{i,j}.
\tag{31}
\]

令实际 Gabor heights 为

\[
 \tau_k=T+kh_0,
\qquad
 S_k=\sum_i b_i e^{i\tau_ks_i}F_i,
\tag{32}
\]

并置 diagonal reference

\[
 A=\sum_i b_i^2W_{i,i}.
\tag{33}
\]

### 定理 238-F（exact all-ones physical-response Gram）[T]

对该 cell，

\[
 \boxed{
 \frac1D\sum_{k=0}^{D-1}
 \left(\|S_k\|_H^2-A\right)
 =
 \frac1D\sum_{k=0}^{D-1}
 \sum_{i\ne j}
 b_ib_jW_{i,j}e^{i\tau_k(s_i-s_j)}.}
\tag{34}
\]

更一般地，对两个 atom subfamilies $\mathcal U,\mathcal V$，置

\[
 S_{\mathcal U,k}
 =\sum_{i\in\mathcal U}b_i e^{i\tau_ks_i}F_i,
 \qquad
 A_{\mathcal U,\mathcal V}
 =\sum_{i\in\mathcal U\cap\mathcal V}b_i^2W_{i,i}.
\]

则有双线性版本

\[
 \boxed{
 \frac1D\sum_k
 \left(
 \langle S_{\mathcal U,k},S_{\mathcal V,k}\rangle_H
 -A_{\mathcal U,\mathcal V}
 \right)
 =
 \frac1D\sum_k
 \sum_{\substack{i\in\mathcal U,\ j\in\mathcal V\\i\ne j}}
 b_ib_jW_{i,j}e^{i\tau_k(s_i-s_j)}.}
 \tag{34a}
\]

取实部后，式 (34a) 正是笔记 216-A 的 normalized cross-cell response；
取 $\mathcal U=\mathcal V$ 则退化为式 (34) 与笔记 234-D 的正测度版本。

#### 证明

展开式 (32) 的平方范数并用式 (31)：

\[
 \|S_k\|_H^2
 =
 \sum_{i,j}
 b_ib_j e^{i\tau_k(s_i-s_j)}W_{i,j}.
\]

$i=j$ 部分恰为式 (33)，移项并对 $k$ 平均。$\square$

对式 (34a) 分别展开两个 synthesis 完全相同；共同 atoms 的 $i=j$ 部分
恰为 $A_{\mathcal U,\mathcal V}$。若两 families 不交，则没有 diagonal
reference，且不能把 cross inner product 单独称为正能量。

式 (34) 有三点重要区别：

1. coefficient vector 固定为真实 $b_i e^{i\tau_ks_i}$，不是任意系数；
2. six-window cross terms 全部保留在同一个 Hilbert norm 中；
3. 所需 cancellation 是平均物理能量与其 diagonal reference 之间的差，
   不能由 $\sum_k\|S_k\|^2$ 的单独上界推出。

对不同 cells，第二点应读成同一 Hilbert 空间中的 physical cross inner
product；只有同 cell specialization 才是 norm square。

因此定理 238-F 是显式公式型 Weil Gram 的合法接口，但它本身只是 finite
identity，不是 RH 或四矩定理。

## 6. Exact one-factor Vaughan lift 与 ghost gauge

ratio atom $i=(a,b)$ 含两个 von Mangoldt factors。若同时分解二者，自然得到
$2\times2=4$ 个 tensor channels，而不是两个。为了获得真正的二通道且保持
exactness，本节只分解 numerator variable $a$，denominator $\Lambda(b)$
保持完整。

固定 cutoffs $U,V$，置

\[
 a_U=\mu_{\le U}*1,\qquad
 \Lambda_{\le V}=\Lambda{\bf1}_{n\le V},\qquad
 \Lambda_{>V}=\Lambda-\Lambda_{\le V},
\tag{35}
\]

以及 canonical coefficients

\[
 I_{U,V}=a_U*\Lambda_{>V}+\Lambda_{\le V},
 \qquad
 II_{U,V}=\Lambda-I_{U,V}.
\tag{36}
\]

由 $\mu*1=\delta_1$（Dirichlet convolution unit）或直接展开 Vaughan
identity，逐整数有

\[
 \boxed{\Lambda=I_{U,V}+II_{U,V}.}
\tag{37}
\]

现在固定一个与 channels 无关的 integer-pair mask $m_{\mathcal C}(a,b)$：
它在 original prime-power support 上等于 actual factor/aperture 与
distinct-base mask；在 $\Lambda(a)=0$ 的 composite points 上也必须预先固定，
不得随 $U,V$ 或估计目标改变。定义

\[
 \gamma_{a,b}^{(r)}
 =
 m_{\mathcal C}(a,b)
 \frac{r_{U,V}(a)\Lambda(b)}
 {4\pi^2\sqrt{ab}},
 \qquad r\in\{I,II\},
\tag{38}
\]

以及

\[
 S_k^{(r)}
 =
 \sum_{a,b}
 \gamma_{a,b}^{(r)}
 e^{i\tau_k\log(a/b)}F_{a,b}.
\tag{39}
\]

### 定理 238-G（exact one-factor physical Vaughan quotient）[T]

对每个 $k$，

\[
 \boxed{S_k=S_k^{(I)}+S_k^{(II)}.}
\tag{40}
\]

令

\[
 G_{rs}
 =
 \frac1D\sum_k
 \langle S_k^{(r)},S_k^{(s)}\rangle_H,
\tag{41}
\]

并令同原子 reference matrix 为

\[
 A_{rs}^{\rm diag}
 =
 \sum_{a,b}
 \gamma_{a,b}^{(r)}
 \overline{\gamma_{a,b}^{(s)}}W_{a,b;a,b}.
\tag{42}
\]

若 $e=(1,1)$，则

\[
 \boxed{
 e(G-A^{\rm diag})e^*
 =
 \frac1D\sum_k\left(\|S_k\|_H^2-A\right),}
\qquad
 A=eA^{\rm diag}e^*.
\tag{43}
\]

右边是定理 238-F 的 actual same-cell physical response。对两个 cells，
把 norm square 换成式 (34a) 的 cross inner product，结论同型成立。

#### 证明

式 (40) 由式 (37) 逐 $a$ 代入式 (38)--(39) 及 synthesis 的线性性。
展开 $\|S_k^{(I)}+S_k^{(II)}\|^2$ 给
$eGe^*$；同原子项同样按式 (37) 给 $A=eA^{\rm diag}e^*$。相减即得式
(43)。$\square$

这里不能只在 $\Lambda(a)\ne0$ 的 prime-power support 上计算两个 channels。
当 $\Lambda(a)=0$ 而 $I(a)=-II(a)\ne0$ 时，两项是必须保留的
**composite ghost atoms**；它们在式 (40) 中逐 feature cancel，但分别进入
$G_{I,I}$、$G_{I,II}$ 与 $G_{II,II}$。

### 障碍命题 238-H（ghost-gauge Gram no-go）[N]

二通道完整 Gram 不是 physical response 的内在对象。抽象地，若
$S=S_I+S_{II}$，则对任意 $h\in H$ 与 $R>0$，

\[
 S_I'=S_I+Rh,\qquad S_{II}'=S_{II}-Rh
\tag{44}
\]

保持 $S_I'+S_{II}'=S$，但只要 $h\ne0$，对应 $2\times2$ Gram 的 operator
norm 可按 $R^2\|h\|^2$ 增长。特别地，任何只依赖 full Gram norm、而不固定
off-support feature extension或不投影到 physical vector $e=(1,1)$ 的
estimate，都不是 intrinsic response estimate。

#### 证明

物理和在式 (44) 中逐项不变。Gram 的 $R^2$ leading block 是

\[
 R^2\|h\|^2
 \begin{pmatrix}1&-1\\-1&1\end{pmatrix},
\]

其非零 eigenvalue 为 $2R^2\|h\|^2$，而该 block annihilates
$e=(1,1)$。$\square$

这不是否定固定 Vaughan convolution的价值；它要求证明中明确固定
$m_{\mathcal C}$ 与 ghost features，并只把 physical quadratic form 或一个
已证明 gauge-invariant 的 Schur quantity接入 Weil 结论。

## 7. Actual finite channel evidence [E]

脚本 `scripts/power_high_physical_vaughan_channel_audit.py` 使用 flat
six-window overlap，把 numerator channel扩展到全部 integer factors，保留
composite ghost atoms，并逐 pair验证

\[
 \Delta_{I,I}+2\Delta_{I,II}+\Delta_{II,II}
 =
 \text{direct physical response}.
\tag{45}
\]

记右边绝对值除以四个 matrix entries 的 $\ell^1$ 和为 $r_{\rm phys}$。
结果为：

| $X$ | cutoff exponent $\kappa$ | $r_{\rm phys}$ |
|---:|---:|---:|
| 400 | $1/4$ | 1.0000 |
| 800 | $1/4$ | 0.2633 |
| 1,600 | $1/4$ | 0.0772 |
| 3,200 | $1/4$ | 0.0169 |
| 6,400 | $1/4$ | 0.0665 |
| 1,600 | $1/3$ | 0.0959 |
| 3,200 | $1/3$ | 0.0351 |
| 6,400 | $1/3$ | 0.1194 |
| 1,600 | $1/2$ | 0.7777 |
| 3,200 | $1/2$ | 0.4578 |
| 6,400 | $1/2$ | 0.9304 |

小 cutoff 确实暴露 substantial cross cancellation；$\kappa=1/2$ 常退化成
几乎纯 Type I。但序列不单调，且不同 gauges/cutoffs 的 entry budgets不是
intrinsic quantities，所以这些数据不能升级为渐近 saving。

## 8. 修正后的下一最小引理 238-I [O]

固定 $\theta=3/4$、$\kappa=1/4$、$U=V=Y^\kappa$ 与一个明确的
channel-independent integer-pair mask。把式 (41)--(42) 的三个独立 entries
逐一展开成含

\[
 I(a)=(a_U*\Lambda_{>V})(a)+\Lambda_{\le V}(a),
 \qquad
 II(a)=((\mu-\mu_{\le U})*\Lambda_{>V}*1)(a)
\tag{46}
\]

的 determinant-layer sums，完整保留 six-window weight 与 exact
$K_{Q,D}(X\log(ad/bc))$。下一有限目标是：

1. 给出三个 entries 的 exact divisor-range formula及共同 diagonal removal；
2. 隔离 smooth/constant-density main terms，并检查它们在 physical
   combination (45) 中是否先代数相消；
3. 只有相消后剩余的 response-specific Type I/II correlation才允许使用
   sieve、large sieve 或 Schur estimate。

若 leading main terms在 (45) 中不相消，或所需 bound只能通过 full Gram
operator norm给出，则停止该 cutoff。若相消是 exact algebraic identity，则
开放输入将严格缩成三个明确 divisor ranges 上的 oscillatory determinant
errors，而不是原始 four-prime response。

只把式 (43) 改写为“证明 physical response 小”没有价值；可晋级的内容必须
是式 (46) 的 divisor ranges、固定 ghost extension 与可独立验证的 correlation
estimate。

## 9. 最小公理、删除审计与循环性

定理 238-C--D 使用：

1. **band interior line**：$\xi_\star=3/2$ 距两端固定正距离；
2. **consecutive frequency grid**：允许 Riemann quadrature 与窗口内点计数；
3. **fine-grid relation**：$Q\ge M^2$ 控制 physical quadrature error；
4. **positive modulation**：$0<\varepsilon<1$ 保证反例仍是正测度；
5. **constant reference matching**：偶整数 $M$ 使 total modulation mass 为零。

删除审计：

- 把 $\xi_\star$ 移出 band，退化为笔记 237 的 slow-modulation 障碍；
- 把 $\xi_\star$ 放在 band endpoint，continuous response 常数改变且窗口点计数
  只剩半边，但平方根障碍仍可修改后保留；
- 删除 fine grid，只能得到 $O(\log M)$ envelope，仍足以作尺度 no-go，但失去
  式 (18) 的精确极限；
- 删除 positivity 会得到更容易的 signed model，不能审计正测度证书；
- 对 physical direction 使用 arbitrary coefficients 会恰好重新引入式 (2)
  的 Cauchy 损失。
- 删除共同 linear synthesis、只在 prime support上分解，会漏掉
  $I=-II$ 的 composite ghost atoms，得到退化而非共同 synthesis Vaughan
  Gram。
- 不固定 off-support mask 会触发命题 238-H 的 gauge inflation。

非同义反复审计：反例的 response 与 band energy 都由显式正密度独立计算；
没有把“小响应”作为公理。定理 238-F--G 是 exact finite Gram/quotient
identities；笔记 238-I 中式 (46) 后的 determinant correlation estimate
仍明确标为开放。

循环性审计：全部 [T]/[N] 结论只使用 finite Fourier sums、Riemann quadrature、
Dirichlet integrals、窗口变量代换与 Hilbert norm expansion；不调用 RH/GRH、
Hardy--Littlewood、Weil positivity、谱酉性或 bounded negative index。

## 10. 模型范围与 Weil 接口

- **Riemann zeta**：推论 238-E 直接约束 fixed-power four-moment proof
  strategy；定理 238-F 使用 actual von Mangoldt/six-window coefficients。
- **primitive Dirichlet L**：角色相位使 $b_i$ 复化；physical Gram identity
  保持，但 diagonal reference 与 conjugation 必须重算。
- **Dedekind/automorphic L**：fixed-degree local coefficients可进入同一
  Hilbert synthesis；Ramanujan/temperedness 不得暗中作为无条件输入。
- **函数域**：frequency grid 与 degree lattice可能 alias；连续 interior-line
  model 不能未经检查直接移植。
- **一般谱 zeta 模型**：任何用全 spectral-band $L^2$ norm 控制一个固定 trace
  direction 的方法都可能支付同一 narrow-line square-root tax。
- **上同调型 Weil 结构**：定理 238-F 只属于显式公式/Hilbert Gram侧；没有
  建立其与极化、Hard Lefschetz 或 Frobenius weights 的桥梁。

本轮的严格结论是：频率选择正确仍不够；若忽略实际 coefficient direction，
ordinary Bessel/Parseval certificate 会产生幂级 overstrength。MOM-1 与
Vaughan--Brownian 接口必须估计式 (34) 的实际物理方向及其 Type I/II cross
cancellation。
