# 237. 累计差异并非带响应的必要输入：慢调制障碍

日期：2026-09-03

分支：MOM-1 / 路线 A1q；接口：fixed-power exact Gabor response

状态：exact positive slow-modulation family、累计差异下界、finite-band
$O(M^{-1})$ 响应及其 $\theta=3/4$ 尺度分离为 [T]/[N]；实际
four-von-Mangoldt response 的 band-selective estimate 为 [O]。本笔记修正
笔记 235--236 中把 cumulative discrepancy 称为“唯一剩余输入”的过强表述。
笔记 235-H 与 236 的充分性结论仍然有效。

## 1. 审计问题

笔记 235-H 对 even positive measure $\mu$ 给出

\[
 \left|\int K_{X,D}\,d\mu\right|
 \ll
 \frac{b_0}{M^2}+E_0\log(2+M)
 +\sum_{j\ge1}\left(\frac{b_j}{R_j^2}+E_j\right).
\tag{1}
\]

笔记 236 已把其中全部 mass-over-radius-squared 项压到 $O(L)$。因而

\[
 E_0\log(2+M)+\sum_{j\ge1}E_j=o(L^4)
\tag{2}
\]

是闭合 power-high response 的一个充分算术条件。问题是：式 (2) 是否也刻画了
带响应真正缺失的算术输入？

答案是否定的。累计差异把零频附近的慢漂移和 $[1,2]$ 中的实际响应频率一视
同仁；Stieltjes 分部积分随后对 $K'$ 取绝对值，丢失了这两个频区的分离。下面
给出 exact finite kernel 上的正测度反例。

## 2. Exact kernel 与慢调制族

置

\[
 Q=XL,\qquad D\in\mathbb N,\qquad
 \lambda=\frac DQ\in[1/2,2],
\tag{3}
\]

并沿用

\[
 K_{Q,D}(t)
 =
 \frac1D\sum_{k=0}^{D-1}
 \cos(2\pi\xi_k t),
 \qquad
 \xi_k=1+\frac{k}{Q}
       =1+\frac{\lambda k}{D}.
\tag{4}
\]

固定 $0<c<1/2$ 与 $0<\varepsilon<1$。对整数 $n\ge2$ 取

\[
 M=n^2,\qquad \omega=M^{-1/2}=n^{-1},
\tag{5}
\]

并假设 $M\le cQ$。定义 even positive measure

\[
 d\mu_M(t)
 =
 \left(1+\varepsilon\cos(2\pi\omega t)\right)
 {\bf 1}_{[-M,M]}(t)\,dt .
\tag{6}
\]

因为 $0<\varepsilon<1$，式 (6) 确为正测度。又因
$\omega M=n$ 为整数，

\[
 \mu_M([-M,M])=2M.
\tag{7}
\]

所以与相同总质量的 constant-density reference 恰好是 Lebesgue measure，
没有通过重新拟合密度隐藏误差。

## 3. 累计差异恰为平方根尺度

### 命题 237-A（exact slow cumulative discrepancy）[T]

令

\[
 F_M(u)
 =
 \mu_M([-M,u])-(u+M),
 \qquad -M\le u\le M.
\tag{8}
\]

则

\[
 F_M(u)
 =
 \frac{\varepsilon}{2\pi\omega}
 \sin(2\pi\omega u),
\qquad
 \boxed{\ \|F_M\|_\infty
 =\frac{\varepsilon}{2\pi}\sqrt M\ }.
\tag{9}
\]

同一等式适用于笔记 235 的 central one-sided discrepancy
$\sup_{0\le u\le M}|\mu_M([0,u])-u|$。

#### 证明

对式 (6) 积分，并用
$\sin(-2\pi\omega M)=\sin(-2\pi n)=0$，得到式 (9) 第一式。
区间 $[-M,M]$ 包含 $\sin(2\pi\omega u)=\pm1$ 的点，所以 supremum
恰好达到。对 $[0,M]$ 从零积分完全相同。$\square$

## 4. Exact finite band 看不见慢调制

### 引理 237-B（shifted consecutive-band Abel bound）[T]

在式 (3)--(5) 下，对任意 $a$ 满足 $|a|\le1/2$ 及 $aM\in\mathbb Z$，

\[
 J_a(M)
 :=
 \frac1D\sum_{k=0}^{D-1}
 \frac{\sin(2\pi(\xi_k+a)M)}
      {\pi(\xi_k+a)}
 \ll_c M^{-1}.
\tag{10}
\]

隐常数对 $Q,D,M,a$ 一致。

#### 证明

因为 $M$ 与 $aM$ 都是整数，

\[
 \sin(2\pi(\xi_k+a)M)
 =
 \Im\exp\left(\frac{2\pi i kM}{Q}\right).
\tag{11}
\]

令

\[
 z=\exp(2\pi iM/Q),\qquad
 w_k=(1+a+k/Q)^{-1}.
\tag{12}
\]

由 $M/Q\le c<1/2$，

\[
 \left|\sum_{k=0}^{r}z^k\right|
 \le\frac{2}{|1-z|}
 \ll_c\frac Q M.
\tag{13}
\]

又因 $|a|\le1/2$，$w_k$ 为正单调序列，且

\[
 |w_0|+\sum_{k=0}^{D-2}|w_{k+1}-w_k|\ll1.
\tag{14}
\]

离散 Abel 求和给

\[
 \left|\sum_{k=0}^{D-1}w_kz^k\right|
 \ll_c\frac Q M.
\tag{15}
\]

除以 $D$，再用 $Q/D=\lambda^{-1}\le2$，取虚部并除以 $\pi$，得到式
(10)。$\square$

### 定理 237-C（large discrepancy / tiny exact response）[T]

对式 (6) 的正测度族，

\[
 \boxed{
 \left|\int_{-M}^{M}K_{Q,D}(t)\,d\mu_M(t)\right|
 \ll_{c,\varepsilon}M^{-1},}
\tag{16}
\]

而其累计差异由式 (9) 按 $\sqrt M$ 增长。

因此，在 even positive measures 类上，下列逆向命题均为假 [N]：

1. small exact band response 推出 small cumulative discrepancy；
2. response 的 $o(L^4)$ closure 必须经由式 (2)；
3. 笔记 235-H 的 cumulative-discrepancy 右端在数量级上刻画响应。

#### 证明

constant part 的响应是

\[
 \int_{-M}^{M}K_{Q,D}(t)\,dt=J_0(M).
\tag{17}
\]

积化和差给 modulation part

\[
 \int_{-M}^{M}K_{Q,D}(t)\cos(2\pi\omega t)\,dt
 =
 \frac12\left(J_{-\omega}(M)+J_{\omega}(M)\right).
\tag{18}
\]

这里 $\omega\le1/2$ 且 $(\pm\omega)M=\pm n$ 为整数。分别对
$a=0,\pm\omega$ 应用引理 237-B，即得式 (16)。结合命题 237-A，
response 趋零而 discrepancy 发散，故三个逆向命题均失败。$\square$

## 5. $\theta=3/4$ 应用尺度上的严格分离

### 推论 237-D（$L^4$ gate 不要求 cumulative gate）[N]

取

\[
 X_n=n^4,\qquad L_n=\log X_n,\qquad
 Q_n=X_nL_n,\qquad D_n=\operatorname{round}(Q_n),
 \qquad M_n=X_n^{1/2}=n^2.
\tag{19}
\]

则充分大 $n$ 时式 (3)--(5) 成立，而且

\[
 \left|\int K_{Q_n,D_n}\,d\mu_{M_n}\right|
 =O(n^{-2})=o(L_n^4),
\tag{20}
\]

但

\[
 E_{M_n}\log(2+M_n)
 \asymp n\log n
 \gg(\log n)^4\asymp L_n^4.
\tag{21}
\]

因此即使在笔记 236 为 $\theta=3/4$ 选出的同一证明尺度
$M=X^{1/2}$，式 (2) 也不是 exact response closure 的必要条件。

#### 证明

$D_n/Q_n\to1$ 且 $M_n/Q_n\to0$，故定理 237-C 可用。式 (20) 来自
式 (16)，式 (21) 来自式 (9) 以及 $M_n=n^2$、$L_n=4\log n$。$\square$

注意：本推论只否定一个证明 schema 的必要性。测度 (6) 不是 prime determinant
measure，因此不否定实际 prime measure 可能满足式 (2)，也不提供四矩渐近。

## 6. 为什么原充分定理仍然正确

定理 235-H 只声称

\[
 \text{small cumulative budget}
\Longrightarrow
\text{small band response}.
\tag{22}
\]

定理 237-C 否定的是反方向。其机制可从分部积分看得很清楚：

\[
 \int K\,d(\mu-dt)
 =
 [KF]_{\partial I}-\int F(t)K'(t)\,dt.
\tag{23}
\]

以 $\|F\|_\infty\int|K'|$ 控制式 (23) 时，低频 $F$ 与带通 $K'$ 的正交性
被绝对值抹掉。故：

- 笔记 235-H 仍是完全有效的 arithmetic sufficient certificate；
- 笔记 236 对其 mass ledger 的 $O(L)$ 闭合仍有效；
- 只能删除“cumulative discrepancy 是唯一剩余输入”这一 necessity 表述。

## 7. 更弱而非同义反复的 band-selective 证书

令 $\nu=\mu-c\,dt$ 是一个 cell 中去除 constant reference 后的 signed
measure，并置

\[
 \widehat\nu(\xi)=\int e^{2\pi i\xi t}\,d\nu(t).
\tag{24}
\]

定义 exact discrete band energy

\[
 {\mathcal B}_{Q,D}(\nu)^2
 =
 \frac1D\sum_{k=0}^{D-1}
 |\widehat\nu(\xi_k)|^2.
\tag{25}
\]

### 命题 237-E（band-energy sufficient certificate）[T]

\[
 \left|
 \frac1D\sum_{k=0}^{D-1}\Re\widehat\nu(\xi_k)
 \right|
 \le {\mathcal B}_{Q,D}(\nu).
\tag{26}
\]

#### 证明

这是有限维 Cauchy--Schwarz。取
$z_k=\widehat\nu(\xi_k)$ 即得。$\square$

式 (25) 仍是比 signed response 更强的充分条件，但与 cumulative discrepancy
不同，它只查看实际 band，并且可展开为正的二重算术 Gram：

\[
 {\mathcal B}_{Q,D}(\nu)^2
 =
 \iint
 \left(\frac1D\sum_{k=0}^{D-1}
 e^{2\pi i\xi_k(t-s)}\right)
 d\nu(t)\,d\overline{\nu}(s).
\tag{27}
\]

所以它不是把所求 signed average 原样改名；它要求整个实际 band 上的
mean-square 控制。另一方面它可能仍过强，因为式 (26) 丢失不同 $k$ 间的
物理响应 cancellation。任何晋级都必须先检查 actual four-von-Mangoldt
factorization 后的 Gram，而不能把普通 arbitrary-coefficient Bessel bound
冒充 response-specific estimate。

## 8. 修正后的下一最小引理 237-F [O]

固定 $\theta=3/4$ 与一个 balanced factor/aperture cell，取
$M=X^{1/2}$。对笔记 234-(16) 的实际 four-von-Mangoldt、six-window
determinant measure $\mu_q$，完成以下二择一：

1. **band-energy 路线**：去除笔记 236 已闭合的 constant-density mass terms
   后，证明
   \[
   {\mathcal B}_{Q,D}(\nu_q)=o(L^4)
   \tag{28}
   \]
   uniformly over the fixed cell parameters，并把式 (28) 的 actual
   factorized Gram 归约为 response-specific Type-I/II bound；
2. **direct physical-response 路线**：把
   $D^{-1}\sum_k\Re\widehat\nu_q(\xi_k)$ 保持为一个整体，在不假设
   RH/四素数渐近的前提下证明 raw $o(L^4)$，同时给出比目标本身更具体、
   可独立验证的 determinant correlation 输入。

只写“证明 exact response 为 $o(L^4)$”是目标的改写，不能作为新结构定理。
式 (25) 虽为可检验的充分输入，也必须接受 overstrength audit：若 actual
finite data 中 band energy 不降而 signed response 降，则转向第二路线。

全 cells 的 global ledger 只在 single-cell estimate 明确其 aperture 与
factor-width uniformity 后处理；per-cell little-oh 不能直接求和。

## 9. 最小公理、删除审计与循环性

定理 237-C 使用且只使用：

1. **频谱间隙**：$\xi_k\ge1$，使 $\xi_k-\omega\ge1/2$，从而 shifted weights
   有一致 bounded variation；
2. **consecutive arithmetic grid**：给式 (13) 的同一几何和控制；
3. **pre-alias 条件**：$M/Q\le c<1/2$，使 $|1-z|$ 有 $M/Q$ 下界；
4. **integral alignment**：$M=n^2$、$\omega=1/n$，消除端点基相位；
5. **positivity**：$0<\varepsilon<1$，保证反例位于笔记 235 的正测度类。

删除审计：

- 删除频谱间隙并让 band 包含 $\omega$，慢调制可产生 $\asymp M$ 响应；
- 删除 consecutive grid，不能用单一几何和证明 uniform $O(M^{-1})$；
- 接近 alias $M/Q=1$ 时式 (13) 失效；
- 删除 alignment 仍可得到沿适当子列的分离，但不再有本文的 exact 简式；
- 删除 positivity 会得到更容易却更弱的 signed-measure 反例。

非同义反复审计：式 (9) 与式 (16) 是对同一显式正测度族分别作实空间和
频带计算；没有把“响应小”作为公理。命题 237-E 是明确标注的充分
Cauchy--Schwarz certificate，不被表述为必要条件或新 RH 等价。

循环性审计：全部 [T]/[N] 结论只用 finite trigonometric identities、
geometric sums、Abel summation 与 elementary asymptotics；不调用 RH/GRH、
Hardy--Littlewood、Weil positivity、谱酉性或 bounded negative index。

## 10. 模型范围与 Weil 接口

- **Riemann zeta**：直接纠正 fixed-power alternating response 的输入看板；
  不对 actual primes 作渐近断言。
- **Dirichlet/Dedekind/automorphic L**：只要 Gabor frequencies 有统一
  nonzero gap，同一 geometry no-go 成立；角色权会使 actual measure signed，
  但正测度反例已足以否定一般 necessity。
- **函数域**：degree lattice 可能与 $\omega$ 或 band alias；必须重新检查式
  (13)，不能自动移植。
- **一般谱 zeta 模型**：任何只凭 cumulative primitive 的 variation bound
  控制非零带响应的方案都会面临同一 low-frequency blindness。
- **上同调型 Weil 结构**：本文不构造上同调对象，也不声称显式公式 band
  energy 等价于极化或 Hard Lefschetz；两类结构之间仍无桥梁定理。

本轮的严格结论是一个结构性障碍：累计差异是可用但过强的实空间证书，不能被
提升为 fixed-power Weil response 的必要或“唯一”算术输入。下一步应在 actual
factorized response 的非零频带内寻找算术估计。
