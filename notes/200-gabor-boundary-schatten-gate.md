# 200. Gabor 边界的本征 Schatten 门与二矩提升 no-go

日期：2026-09-01

状态：Poisson--Gabor 核审计、算子范数界、zero-side tail 的四矩消去、
本征 Schatten 门和秩一 no-go 为 [T]；weighted boundary Hilbert--Schmidt
估计为 [O]。

## 1. 本轮结论

Alpöge--Furman 的临界密度 Poisson--Gabor 公式是精确恒等式。四矩的
finite-to-bulk 障碍不是 aliasing，也不是远端零点矩阵
\(\widetilde E\)，而是两个不同的边界：

1. 有限指标集 \(0\le k<d\) 相对于全格点的 \(K_{\rm out}\)；
2. \(\tau\)-积分由全线截到 \(I=[T,2T]\)。

本轮无条件证明 \(\widetilde E\) 对四次迹为 \(o(N)\)，并把剩余边界压成
一个本征的 signed-kernel Schatten--4 逼近。再结合可证的算子范数尺度，
得到具体的充分目标

\[
 \|J_T-J_{\infty,T}\|_{\rm HS}^{2}
 =o\!\left(\frac{L^3}{(1+\log L)^2}\right).
\tag{1}
\]

原论文的二矩标量误差不能推出式 (1)；一个秩一族给出严格逻辑反例。

## 2. 精确 Poisson 核与误差来源 [R/T]

沿用一手来源
https://arxiv.org/html/2608.13637v2
的记号：

\[
 L=\log(T/2\pi),\quad h=\frac{2\pi}{L},\quad
 \alpha_k=T+kh,
\]

\[
 f_k(\tau)=\widehat\phi(\tau-\alpha_k),\qquad
 \Phi=\widehat{\phi^2}.
\]

由于 \(\operatorname{supp}(\phi*\phi)\subset[-L,L]\)，Poisson 对偶格点
为 \(L\mathbb Z\)，端点项连续消失，故精确地

\[
 \sum_{k\in\mathbb Z}f_k(\tau)f_k(\tau')
 =L\Phi(\tau-\tau').
\tag{2}
\]

所以

\[
 K(\tau,\tau')
 =\sum_{0\le k<d}f_k(\tau)f_k(\tau')
 =L\Phi(\tau-\tau')-K_{\rm out}(\tau,\tau')
\tag{3}
\]

中的差异只来自有限指标截断。原文命题 4.3 的
\(\|\widetilde E\|_1\ll T^{-1/2}\) 是零点集合 \(I'\) 外的 zero-side
tail，不能与式 (3) 的 \(K_{\rm out}\) 混同。

## 3. 全显式公式矩阵的算子范数 [T]

记

\[
 \mathcal B_T=\widetilde G+\widetilde E,qquad
 B_0=L+4\sqrt X,quad X=e^L=\frac{T}{2\pi}.
\]

### 定理 AEF

对固定窗口 \(\psi\) 和固定平滑 \(\chi\)，

\[
 \|\mathcal B_T\|
 \ll_{\psi,\chi}\frac{B_0(1+\log L)}{L}
 \ll_{\psi,\chi}\frac{\sqrt T(1+\log L)}{L}.
\tag{4}
\]

### 证明

对 \(x\in\mathbb C^d\) 令

\[
 g_x(\tau)=\sum_{0\le k<d}x_k\widehat\phi(\tau-\alpha_k),
 \qquad
 p_x(u)=\sum_{0\le k<d}x_ke^{i\alpha_ku}.
\]

则 \(g_x=\widehat{\phi p_x}\)。由于
\(\alpha_k-\alpha_j=2\pi(k-j)/L\)，指数函数在长度 \(L\) 的区间上
精确正交，故

\[
 \int_{\mathbb R}|g_x(\tau)|^2d\tau
 =2\pi\int_{-L/2}^{L/2}\phi(u)^2|p_x(u)|^2du
 \le 2\pi L\|x\|^2.
\tag{5}
\]

又 \(a=\|\phi\|_2^2/L\ge a_0(\psi)>0\)。在 \(I\) 内用
\(|\nu_X|\le B_0\)，式 (5) 给正规化二次型 \(O(B_0/L)\)。

在 \(I\) 外使用原文的包络

\[
 \vartheta(r)=\min\!\left(L,\frac2{|r|},\frac{C_\chi}{r^2}\right),
\]

以及

\[
 \int\vartheta^2=O(L),\qquad
 \int |r|\vartheta(r)^2dr=O_\chi(1+\log L).
\]

对正包络取迹并按 \(\Delta=\operatorname{dist}(\tau,I)\) 求和，可得
未正规化界 \(O(B_0L(1+\log L))\)；除以 \(aL^2\) 即得式 (4)。

## 4. zero-side tail 对四矩无害 [T]

### 推论 AEG

\[
 \left|
 \operatorname{tr}(\widetilde G+\widetilde E)^4
 -\operatorname{tr}\widetilde G^4
 \right|
 \ll_{\psi,\chi}
 \frac{T(1+\log L)^3}{L^3}
 =o(N(T,2T)).
\tag{6}
\]

证明：对 \(A=\widetilde G+\widetilde E\)、\(G=\widetilde G\) 作非交换
telescoping，并用

\[
 |\operatorname{tr}(EX)|\le\|E\|_1\|X\|.
\]

原文给 \(\|\widetilde E\|_1\ll T^{-1/2}\)，式 (4) 也控制
\(\|G\|\)，所以差至多为
\(T^{-1/2}O((\sqrt T(1+\log L)/L)^3)\)。

因此论文 199 中“有限四循环到 bulk”的开放项可以进一步缩小：零点远端
tail 已闭合，剩余只是 \(K_{\rm out}\) 与 \(\tau\)-domain 边界。

## 5. signed kernel 的本征实现 [T]

在 \(H=L^2(\mathbb R,d\tau)\) 上定义

\[
 (U_Tx)(\tau)
 =\frac{|\nu_X(\tau)|^{1/2}}{\sqrt aL}
   \sum_{0\le k<d}x_kf_k(\tau),
 \qquad S=M_{\operatorname{sgn}\nu_X},
\]

\[
 C_T=U_TU_T^*\succeq0,qquad
 J_T=C_T^{1/2}SC_T^{1/2}.
\tag{7}
\]

这里 \(C_T\) 的核为

\[
 \frac{|\nu_X(\tau)|^{1/2}K(\tau,\tau')
 |\nu_X(\tau')|^{1/2}}{aL^2}.
\]

有限矩阵满足 \(\mathcal B_T=U_T^*SU_T\)。先比较
\(U_T^*SU_T\) 与 \(C_TS\)，再比较 \(C_TS\) 与
\(C_T^{1/2}SC_T^{1/2}\)；两次使用 \(AB\) 与 \(BA\) 的非零谱
（含代数重数）一致，得到

\[
 \operatorname{tr}\mathcal B_T^r=\operatorname{tr}J_T^r
 \quad(r\ge1),qquad
 \operatorname{tr}\mathcal B_T^4=\|J_T\|_{\mathcal S_4}^4.
\tag{8}
\]

把核换成 \(L\Phi\) 并乘
\(\mathbf1_I(\tau)\mathbf1_I(\tau')\)，同样定义
\(C_{\infty,T},J_{\infty,T}\)。则

\[
 \operatorname{tr}J_{\infty,T}^4=\mathcal C_4(\nu_X).
\tag{9}
\]

### 定理 AEH（intrinsic finite-to-bulk gate）

若

\[
 \mathcal C_4(\nu_X)=O(N),qquad
 \|J_T-J_{\infty,T}\|_{\mathcal S_4}=o(N^{1/4}),
\tag{10}
\]

则

\[
 \operatorname{tr}\mathcal B_T^4-\mathcal C_4(\nu_X)=o(N).
\tag{11}
\]

这是论文 199 中正包络 gate 的本征修订：只比较真正编码有符号谱的
Hermitian operators \(J_T,J_{\infty,T}\)，不要求更强的正包络差。

## 6. 一个具体 Hilbert--Schmidt 充分目标 [T/O]

令

\[
 m_L=1+\log L,qquad q_T=\frac{\sqrt Tm_L}{L}.
\]

式 (4) 与 bulk Schur 界给

\[
 \|J_T\|+\|J_{\infty,T}\|=O(q_T),qquad
 \|J_T-J_{\infty,T}\|=O(q_T).
\tag{12}
\]

若式 (1) 成立，则插值

\[
 \|\Delta J\|_4^4
 \le\|\Delta J\|^2\|\Delta J\|_{\rm HS}^2
 =o\!\left(q_T^2\frac{L^3}{m_L^2}\right)
 =o(TL)=o(N)
\]

给出式 (10)。所以新的边界最小任务不是模糊的“四个核共同定位”，而是明确的
weighted boundary Hilbert--Schmidt/Carleson 估计 (1)，再加 bulk 四矩
\(O(N)\)。

## 7. 二矩误差不能自动提升 [T]

取秩一投影 \(P\)，令

\[
 A_T=q_TP,qquad B_T=0.
\]

则 \(\|A_T\|=q_T\)，且二矩差

\[
 q_T^2=\frac{Tm_L^2}{L^2}
\]

小于原文二矩边界证明可保守读出的 \(O(Tm_L)\) 量级；但是

\[
 \frac{|\operatorname{tr}(A_T^4-B_T^4)|}{N}
 \asymp\frac{Tm_L^4}{L^5}\longrightarrow\infty.
\tag{13}
\]

这不声称 zeta 核出现该秩一行为；它严格证明“二矩标量误差加现有算子范数”
在逻辑上不足以推出四矩稳定。

## 8. 对原文二矩 rate 的证据边界 [R]

按 v2 第 5.2 节当前展示的计算，\(\mathcal E_2\) 最后一行是 raw
\(O(L^3B_0^2l\log L)\)。文中 \(l=L\)、\(B_0^2\ll T\)，直接除以
\((aL^2)^2\) 得

\[
 O(T\log L)=O\!\left(\frac{N\log L}{L}\right),
\]

而命题 5.2 写成 \(O(N\log L/L^2)\)。这里仅记录为 proof-display
discrepancy：可能是展示证明省略了一步改进，也可能是陈述或中间式的排印差异；
不据此断言论文结论错误。较弱界仍为 \(o(N)\)，足以支持其主二矩渐近，
但不能用来声称四矩 Schatten 控制。

## 9. 下一步

式 (1) 可能需要至少一种额外机制：

1. 对 Gabor 指标使用 smooth taper 或 guard band；
2. 对区间平移或高度 \(T\) 作平均，避免固定边缘集中；
3. 不取 \(|\nu_X|\) 的粗绝对值，保留 prime phases 作专门四线性边界估计。

审计脚本 scripts/operator_fourth_localizer_audit.py 验证本征谱实现、Schatten
插值尺度和秩一 no-go。它不证明式 (1)。

## 10. 后续推进（笔记 225）

笔记 225 绕开而非证明了式 (1)：对 pure-prime 四词，left-associated Toeplitz telescoping 只产生三个具体 crossing-Hankel traces，每个 nuclear norm 为 `O(1+log L)`；结合 prime-side高度相位即可闭合 signed boundary。因此本笔记的 intrinsic Schatten gate 仍是 all-word 充分条件和二矩提升 no-go，但不再是 pure-prime `P^4` 的必要中间目标。Gamma/continuum mixed symbols 是否也允许这种 response-specific 绕行仍开放。

## 11. 后续推进（笔记 226）

笔记 226 对 Archimedean/pole-absorption 背景给出比本笔记全局正包络更精确的 response-specific 绕行：在正高度 Gabor centers 上，背景是零频 Toeplitz 主部加 `O(1/L)` 算子余项，后者经 Schatten--4 telescoping 只产生 `O(N/L)`。因此 all-word intrinsic gate 仍是一般充分条件和 no-go 基准，但 zeta 四矩主线无需再用它控制 Gamma 余项；剩余困难是确定性 `S_L` 与 prime responses 的非零 mixed frequencies。