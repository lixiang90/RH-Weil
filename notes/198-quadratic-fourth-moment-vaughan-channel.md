# 198. 四矩二次通道、素数共振账本与 Vaughan 接口

日期：2026-09-01

状态：矩阵恒等式与有限 Dirichlet 多项式恒等式为 [T]；平窗常数账本为 [F]；
有限数值实验为 [N]；真实 tapered zeta 四矩估计为 [O]。

## 1. 本轮结论

四矩路线的正确算术对象不是孤立的正量

\[
\frac1T\int_T^{2T}\left|\sum_m
\frac{(\Lambda*\Lambda)(m)}{\sqrt m}m^{it}\right|^2dt,
\]

而是背景、线性素数项与二次素数项组成的三通道 Gram。完整 Gram 保留
2+2、3+1、4+0 resonance families 及背景之间的有符号交叉项；分别取绝对值会
删除要利用的相消。

这一重写没有解决 zeta 四矩估计，但把“改善 67.25%”压成了一个比完整
Hardy--Littlewood 渐近更弱、可明确审计的一侧 Schur/Gram 任务。

## 2. 精确 quadratic-channel 分解 [T]

令中心化有限 Weil 压缩

\[
H=G-I=A+V
\]

为 Hermitian，其中 \(A\) 是 prime-free/Gamma/continuum 背景，\(V\) 是素数
振荡通道。定义

\[
C_0=A^2,\qquad C_1=AV+VA,\qquad C_2=V^2,
\]

\[
K_{ij}=\langle C_i,C_j\rangle_{\rm HS}
=\operatorname{tr}(C_i^*C_j).
\]

### 定理 AEA（quadratic-channel Gram identity）

\[
K=(K_{ij})_{0\le i,j\le2}\succeq0
\]

且

\[
\begin{aligned}
\operatorname{tr}H^4
&=\|H^2\|_{\rm HS}^2\\
&=K_{00}+2\operatorname{Re}K_{01}
+K_{11}+2\operatorname{Re}K_{02}
+2\operatorname{Re}K_{12}+K_{22}.
\end{aligned}
\tag{1}
\]

按 \(V\) 次数分组：

| 次数 | 贡献 |
|---:|---:|
| 0 | \(K_{00}\) |
| 1 | \(2\operatorname{Re}K_{01}\) |
| 2 | \(K_{11}+2\operatorname{Re}K_{02}\) |
| 3 | \(2\operatorname{Re}K_{12}\) |
| 4 | \(K_{22}\) |

证明只是 \(H^2=C_0+C_1+C_2\) 和 Hilbert--Schmidt 范数展开。

### 定理 AEB（quadratic-channel Schur residual）

令

\[
K_{<2}=(K_{ij})_{0\le i,j\le1},\qquad
k=(K_{02},K_{12})^{\mathsf T}.
\]

则

\[
r_2=K_{22}-k^*K_{<2}^{\dagger}k\ge0.
\tag{2}
\]

若 \(\mathcal P\) 是到
\(\operatorname{span}\{C_0,C_1\}\) 的 Hilbert--Schmidt 正交投影，则

\[
r_2=\|(I-\mathcal P)C_2\|_{\rm HS}^2,
\tag{3}
\]

\[
\operatorname{tr}H^4
=\|C_0+C_1+\mathcal PC_2\|_{\rm HS}^2+r_2.
\tag{4}
\]

所以需要控制的是 \(r_2\) 和投影系数
\(K_{<2}^{\dagger}k\)，不是单独控制 \(K_{22}=\|V^2\|_{\rm HS}^2\)。
这与文档 195 的 response-specific Vaughan--Brownian Gram 是同一种原则。

## 3. 2+2、3+1、4+0 符号共振 [T]

令

\[
Q_T(t)=\sum_n c_n n^{it},\qquad
V_T(t)=Q_T(t)+\overline{Q_T(t)}.
\]

以 \(C_r(m)\) 表示 \(Q_T^r\) 的 Dirichlet 系数，并记

\[
M_{r,s}=\frac1T\int_T^{2T}
Q_T(t)^r\overline{Q_T(t)}^{\,s}\,dt.
\]

二项式展开给出精确账本

\[
\frac1T\int_T^{2T}V_T(t)^4dt
=6M_{2,2}+8\operatorname{Re}M_{3,1}
+2\operatorname{Re}M_{4,0}.
\tag{5}
\]

其中

\[
M_{2,2}
=\sum_{m,n}C_2(m)\overline{C_2(n)}
K_T\left(\log\frac mn\right)\ge0,
\tag{6}
\]

\[
K_T(\omega)=\frac1T\int_T^{2T}e^{it\omega}dt
=e^{3iT\omega/2}\operatorname{sinc}\left(\frac{T\omega}{2\pi}\right).
\tag{7}
\]

式 (6) 的 diagonal 是

\[
D_{22}=\sum_m|C_2(m)|^2.
\tag{8}
\]

但其 off-diagonal 没有固定符号；\(M_{3,1}\) 和 \(M_{4,0}\) 也没有固定符号。
当 \(c_n\) 取 \(\Lambda(n)/\sqrt n\) 的主尺度时，

\[
C_2(m)=\frac{(\Lambda*\Lambda)(m)}{\sqrt m}.
\tag{9}
\]

因此“2+2 是正均值”并不允许把 3+1、4+0 或 2+2 off-diagonal 删除。

## 4. 改善当前无条件比例的预算 [T/F/O]

文档 197 的精确四矩 rank--trace--inertia 证书在
\(b_2=1/3\) 时给

\[
R=\frac4{9(b_4+1/3)}.
\]

当前无条件简单零点比例为

\[
\kappa=0.672500703679\ldots.
\]

所以严格改善只需

\[
b_4<\frac4{9\kappa}-\frac13
=0.327549907402\ldots.
\tag{10}
\]

在形式平窗 word ledger 中，两个 alternating 2+2 words 各给 \(1/5\)，
四个 adjacent words 各给 \(1/15\)，合计

\[
D_{22}^{\rm formal}=\frac4{15}=0.266666666667\ldots.
\tag{11}
\]

于是其余所有项的净预算为

\[
\Delta_*=
\left(\frac4{9\kappa}-\frac13\right)-\frac4{15}
=0.060883240736\ldots.
\tag{12}
\]

sine 预测 \(b_4=1/4\) 对应

\[
b_4-D_{22}^{\rm formal}=-\frac1{60}.
\tag{13}
\]

注意 (11) 目前只是平窗形式账本。真实 Gabor/tapered 压缩还需要证明：

1. \(D_{22}\le 4/15+\delta_D+o(1)\)；
2. 2+2 off-diagonal、3+1、4+0 与背景/taper/Gamma 余项的总和不超过
   \(0.060883240736-\delta_D-\epsilon\)；
3. 所有正规化都与压缩 Weil 矩阵的 \(b_4=N^{-1}\operatorname{tr}(G-I)^4\)
   完全一致。

这是一侧估计，不要求得到 \(b_4=1/4+o(1)\) 的完整渐近。

## 5. 有限无权实验 [N]

脚本 scripts/fourth_moment_channel_audit.py 做两类检查：

1. 对随机 Hermitian \(A,V\) 验证式 (1)--(4)；
2. 对无权、无 taper 的
   \(Q(t)=\sum_{p^j\le X}\Lambda(p^j)(p^j)^{-1/2+it}\)
   精确使用 interval kernel 计算式 (5)--(8)，并用数值积分交叉核对。

代表性输出为：

| \(X=T\) | 2+2 full/diagonal | 2+2 contribution | 3+1 | 4+0 |
|---:|---:|---:|---:|---:|
| 24 | 0.797677 | 179.1374 | -7.7704 | 0.0153 |
| 48 | 0.665864 | 348.7178 | -23.1682 | 0.0558 |
| 72 | 0.719169 | 562.4718 | -30.8240 | -0.0089 |

表中明显存在有符号相消；但模型缺少真正的 Gabor kernel、窗口循环权重、Gamma
背景和 zeta 截断正规化，数值不用于支持任何渐近猜想，更不构成比例改善证据。

## 6. Vaughan--Brownian 接口 [O]

应把 Vaughan identity 应用于 quadratic coefficient map

\[
(c,c)\longmapsto C_2=c*_{\rm mult}c,
\]

再把 Type I/II 输出放入三通道 Gram，而不是先对 \(C_2\) 取绝对值。候选步骤：

1. 推导真实压缩的四重循环核

   \[
   \frac1{a^4L^4}\int_{I^4}
   \prod_{j=1}^4\Phi(\tau_j-\tau_{j+1})
   \prod_{j=1}^4\nu_X(\tau_j)\,d\tau_1\cdots d\tau_4,
   \quad \tau_5=\tau_1;
   \]

2. 展开 \(\nu_X=A+P\) 的非交换循环 word：

   \[
   A^4+4A^3P+4A^2P^2+2APAP+4AP^3+P^4;
   \]

3. 将 \(P^4\) 的符号词逐项映射到 2+2、3+1、4+0；
4. 对 quadratic Vaughan components 构造 Brownian primitive Gram；
5. 只短接对目标 response 正交的方向，保留
   \(K_{<2}^{\dagger}k\)；
6. 用统一 dyadic/taper/boundary 估计封闭式 (12) 的净预算。

## 7. 结构性结论与 no-go

本轮得到的“广义结构”不是新的 RH 充分公理，而是部分 Weil 配置的四矩算术接口：

- algebraic layer：三通道 Gram 和 Schur residual；
- analytic layer：循环 taper kernel 与背景通道；
- arithmetic layer：\(\Lambda*\Lambda\) 的 response-specific Vaughan Gram；
- spectral layer：由 \(b_2,b_4\) 通过精确 rank--inertia 证书得到零点比例。

明确的 no-go 是：若把 \(K_{01},K_{02},K_{12}\) 或 2+2 off-diagonal、
3+1、4+0 分别取绝对值，则会丢失预测所需的负修正，且普通
Montgomery--Vaughan 长多项式误差在有效长度 \(T^2\) 上不闭合。

下一步最小可验证目标是：先对一个固定光滑窗推导完全正规的 cyclic word ledger，
证明 2+2 diagonal 上界，再将剩余项压成一个明确的 finite response Gram。
