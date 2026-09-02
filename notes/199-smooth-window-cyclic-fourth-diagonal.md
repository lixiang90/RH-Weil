# 199. 光滑窗四循环、配对对角泛函与窗口再优化

日期：2026-09-01

状态：有限 Gabor 四循环与非交换 word ledger 为 [T]；理想 bulk 的配对
2+2 对角泛函为 [T]；Montgomery--Taylor 与余弦窗数值为 [E]；把真实有限
压缩归约到 bulk 以及未配对共振估计为 [O]。

## 1. 本轮修正与新结论

文档 198 正确记录了平窗配对对角总量 \(4/15\)，但对六个符号词的文字分配有误。
正确分配是：

\[
\text{两个 alternating words 合计 }\frac15,\qquad
\text{四个 adjacent words 合计 }\frac1{15}.
\]

不是每个 word 分别给 \(1/5\) 或 \(1/15\)。

更重要的是，\(4/15\) 不是任意窗口的常数。本轮得到一个显式窗口泛函
\(D_{22}(\psi)\)。它对 Montgomery--Taylor 窗约为

\[
D_{22}(\psi_{\rm MT})=0.244589382034\ldots,
\]

比平窗 \(0.266666\ldots\) 更低，并给其余通道约
\(0.082909914286\) 的净预算来严格改善当前比例。

## 2. 与 Alpöge--Furman 正规化的精确对接 [R]

采用原论文 arXiv:2608.13637v2 的记号：

\[
L=\log(T/2\pi),\quad X=e^L,\quad
\alpha_k=T+\frac{2\pi k}{L},
\]

\[
f_k(\tau)=\widehat\phi(\tau-\alpha_k),\qquad
a=L^{-1}\|\phi\|_2^2,
\]

\[
\mathcal B_{kk'}
=\frac1{aL^2}\int_{\mathbb R}
f_k(\tau)f_{k'}(\tau)\nu_X(\tau)\,d\tau.
\tag{1}
\]

这里 \(\mathcal B=\widetilde G+\widetilde E\)，且

\[
K(\tau,\tau')=\sum_{0\le k<d}f_k(\tau)f_k(\tau')
=L\Phi(\tau-\tau')-K_{\rm out}(\tau,\tau'),
\quad
\Phi=\widehat{\phi^2}.
\tag{2}
\]

一手来源：

https://arxiv.org/html/2608.13637v2

## 3. 有限 Gabor 四循环恒等式 [T]

### 定理 AEC

令 \(\tau_5=\tau_1\)。则精确地

\[
\operatorname{tr}\mathcal B^4
=\frac1{a^4L^8}
\int_{\mathbb R^4}
\prod_{j=1}^4K(\tau_j,\tau_{j+1})
\prod_{j=1}^4\nu_X(\tau_j)\,d\tau_1\cdots d\tau_4.
\tag{3}
\]

证明：把式 (1) 代入
\(\sum_{k_1,\ldots,k_4}
\mathcal B_{k_1k_2}\mathcal B_{k_2k_3}
\mathcal B_{k_3k_4}\mathcal B_{k_4k_1}\)，每个 \(k_j\) 和产生一个式 (2) 的
核。

形式上把四个 \(K\) 换成 \(K_\infty=L\Phi\)，并限制
\(\tau_j\in I=[T,2T]\)，得到 bulk 泛函

\[
\mathcal C_4(\nu_X)
=\frac1{a^4L^4}\int_{I^4}
\prod_{j=1}^4\Phi(\tau_j-\tau_{j+1})
\prod_{j=1}^4\nu_X(\tau_j)\,d\tau_1\cdots d\tau_4.
\tag{4}
\]

式 (3) 是精确恒等式；证明

\[
\operatorname{tr}\mathcal B^4-\mathcal C_4(\nu_X)=o(N)
\tag{5}
\]

仍是开放的第四矩边界归约。二矩论文对 \(K^2-K_\infty^2\) 的估计不能不经修改
直接用于四个核的乘积。

### 定理 AED（Schatten--4 finite-to-bulk gate）

令 \(\mathscr A_T,\mathscr A_{\infty,T}\) 为式 (3)、(4) 对应的归一化
signed weighted kernel operators。若

\[
\|\mathscr A_T\|_{\mathcal S_4}
+\|\mathscr A_{\infty,T}\|_{\mathcal S_4}
=O(N^{1/4}),
\tag{6}
\]

\[
\|\mathscr A_T-\mathscr A_{\infty,T}\|_{\mathcal S_4}
=o(N^{1/4}),
\tag{7}
\]

则式 (5) 成立。

证明来自非交换 telescoping 与 Schatten Hölder：

\[
\begin{aligned}
|\operatorname{tr}A^4-\operatorname{tr}B^4|
\le{}&\|A-B\|_{\mathcal S_4}
\bigl(
\|A\|_{\mathcal S_4}^3
+\|B\|_{\mathcal S_4}\|A\|_{\mathcal S_4}^2\\
&+\|B\|_{\mathcal S_4}^2\|A\|_{\mathcal S_4}
+\|B\|_{\mathcal S_4}^3
\bigr).
\end{aligned}
\tag{8}
\]

这把边界问题从过强的 operator-norm 目标降成与四循环正好匹配的
\(\mathcal S_4\) 逼近。条件 (6)--(7) 仍未从二矩 tail lemma 得到。

## 4. 非交换循环 word ledger [T]

若把中心符号写成 \(A+P\)，则

\[
\begin{aligned}
\operatorname{tr}(A+P)^4
={}&\operatorname{tr}A^4
+4\operatorname{tr}(A^3P)
+4\operatorname{tr}(A^2P^2)\\
&+2\operatorname{tr}(APAP)
+4\operatorname{tr}(AP^3)
+\operatorname{tr}P^4.
\end{aligned}
\tag{9}
\]

两个 \(P\) 的六个 words 分成：

- 四个 adjacent words，对应 \(\operatorname{tr}(A^2P^2)\)；
- 两个 alternating words，对应 \(\operatorname{tr}(APAP)\)。

脚本对随机 Hermitian \(A,P\) 逐次验证式 (9)。

## 5. 任意偶窗口的配对对角泛函 [T]

把 \(\psi\) 以零延拓到全线，设

\[
a=\int_{-1/2}^{1/2}\psi(u)\,du.
\]

定义

\[
A_+(r,s)=\int\psi(u)^2\psi(u+r)\psi(u+s)\,du,
\tag{10}
\]

\[
A_-(r,s)=\int\psi(u)^2\psi(u+r)\psi(u-s)\,du,
\tag{11}
\]

\[
B(r,s)=\int\psi(u)\psi(u+r)\psi(u+s)\psi(u+r+s)\,du.
\tag{12}
\]

### 定理 AEE（paired \(2+2\) window functional）

理想 bulk 的纯素数 \(P_X^4\) 项中，两两匹配乘法频率的归一化对角为

\[
D_{22}(\psi)
=\frac4{a^4}\int_0^1\int_0^1
rs\,[A_+(r,s)+A_-(r,s)+B(r,s)]\,dr\,ds.
\tag{13}
\]

其中

\[
D_{\rm alt}(\psi)=\frac4{a^4}\iint rsA_+(r,s)\,dr\,ds,
\tag{14}
\]

\[
D_{\rm adj}(\psi)=\frac4{a^4}\iint
rs[A_-(r,s)+B(r,s)]\,dr\,ds.
\tag{15}
\]

### 证明

写

\[
P_X(\tau)=-\frac1{2\pi}
\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}
\bigl(n^{i\tau}+n^{-i\tau}\bigr).
\]

四个符号中只有 \(2+\)、\(2-\) 能产生两两配对。对
\(\lambda_1+\cdots+\lambda_4=0\)，三个差变量的 Fourier 反演给

\[
(2\pi)^3T\int
q(u)q(u+\lambda_1)q(u+\lambda_1+\lambda_2)
q(u+\lambda_1+\lambda_2+\lambda_3)\,du,
\quad q=\phi^2,
\tag{16}
\]

加窗口边界项。另一方面

\[
L^{-2}\sum_{n\le e^L}\frac{\Lambda(n)^2}{n}
\delta_{\log n/L}\Longrightarrow r\,dr.
\tag{17}
\]

枚举三个 pair partitions 和四个 orientations，式 (16) 分别化为
\(A_+,A_-,B\)。不同 pairing 同时成立的退化单素数幂项在 \(L^{-4}\)
正规化下消失。

## 6. 平窗常数的正确账本 [T]

对 \(\psi_0=\mathbf1_{[-1/2,1/2]}\)，

\[
\iint rsA_+=\frac1{20},\qquad
\iint rsA_-=\frac1{120},\qquad
\iint rsB=\frac1{120}.
\tag{18}
\]

所以

\[
D_{\rm alt}=\frac15,\quad
D_{\rm adj}=\frac1{15},\quad
D_{22}=\frac4{15}.
\tag{19}
\]

这也解释了先前文字错误：\(1/5,1/15\) 是两个 families 的总量。

## 7. Montgomery--Taylor 窗 [E]

对

\[
\psi_{\rm MT}(u)=\cos(\sqrt2u)\mathbf1_{|u|\le1/2},
\quad
a=\sqrt2\sin(1/\sqrt2),
\]

Gauss--Legendre 积分在阶数 \(12,20,28,36,52\) 下稳定到十二位：

\[
\iint rsA_+=0.0317311854355663\ldots,
\]

\[
\iint rsA_-=0.00592010039974290\ldots,
\]

\[
\iint rsB=0.00591198151035655\ldots.
\]

因此

\[
D_{\rm alt}=0.178157229927730\ldots,
\]

\[
D_{\rm adj}=0.0664321521066960\ldots,
\]

\[
D_{22}=0.244589382034426\ldots.
\tag{20}
\]

其二阶中心矩为

\[
b_2=R(\psi_{\rm MT})-1
=0.327499296320588\ldots.
\]

若

\[
b_4=D_{22}+\mathcal R_{\rm net},
\]

则严格改善同一窗口的二矩证书只需

\[
\mathcal R_{\rm net}
<b_2-D_{22}
=0.082909914286163\ldots.
\tag{21}
\]

这比平窗为击败当前纪录所允许的
\(0.060883240736\ldots\) 更宽。

## 8. 应重新优化的目标泛函

设当前无条件简单比例为

\[
\kappa=0.672500703679\ldots.
\]

对任意给定 \(b_2\)，精确四矩证书超过 \(\kappa\) 的阈值是

\[
B_\kappa(b_2)
=\frac{(1-b_2)^2}{\kappa}-1+2b_2.
\tag{22}
\]

所以在尚未估计 remainder 前，窗口筛选应最大化

\[
\mathcal M_\kappa(\psi)
=B_\kappa(b_2(\psi))-D_{22}(\psi),
\tag{23}
\]

而不是只最小化二矩 \(R(\psi)\)。

对余弦族

\[
\psi_c(u)=\cos(cu)\mathbf1_{|u|\le1/2},\qquad 0<c<\pi,
\]

二矩可由闭式

\[
a_c=\frac{2\sin(c/2)}c,\qquad
I_{2,c}=\frac12+\frac{\sin c}{2c},
\]

\[
J_c=\frac{2\sin^2(c/2)}{c^2}
+\frac{2\sin c}{c^3}-\frac{2I_{2,c}}{c^2},
\qquad
R(\psi_c)=\frac{I_{2,c}+J_c}{a_c^2}
\tag{24}
\]

计算。有限扫描得到：

| \(c\) | \(R(\psi_c)\) | \(D_{22}(\psi_c)\) | \(\mathcal M_\kappa(\psi_c)\) |
|---:|---:|---:|---:|
| \(\sqrt2\) | 1.3274992963 | 0.2445893820 | 0.0829099143 |
| 3.0 | 1.4444055747 | 0.1730616620 | 0.1747604056 |
| 3.1 | 1.4711357292 | 0.1677138996 | 0.1904640632 |
| \(\pi\)（形式端点） | 1.4837005501 | 0.1655130420 | 0.1982670070 |

\(c=\pi\) 在端点为零，不满足原论文闭区间严格正条件，但可由
\(c\uparrow\pi\) 逼近。表只说明 paired diagonal 的预算改善；未配对 remainder
可能随 \(c\) 恶化，不能据此宣称比例已经改善。

## 9. 新的首要障碍

本轮把旧目标“证明 \(D_{22}\le4/15\)”完成并推广了。新的最小任务是：

1. 证明式 (6)--(7) 的 weighted-kernel Schatten--4 bounds；
2. 把 \(P_X^4\) 中未配对但近共振的
   \(n_1n_2\approx n_3n_4\) 写成带窗口 \(A_\pm,B\) 的正/有符号 Gram；
3. 同时估计 \(3+1,4+0\) 与 \(A^jP^{4-j}\) 背景 words；
4. 在余弦窗族中联合优化 remainder，而不是只优化显式对角。

一个重要 no-go 是：二矩尾的迹范数 \(o(1)\) 本身不足以自动推出四次迹稳定；
一般需要

\[
|\operatorname{tr}(B^4-G^4)|
\le \|B-G\|_1\,
(\|B\|^3+\|B\|^2\|G\|+\|B\|\|G\|^2+\|G\|^3),
\]

所以还需要压缩算子范数或直接四循环边界估计。不能把二矩 tail lemma 原样提升。

审计脚本 scripts/smooth_fourth_window_audit.py 验证：

- 有限 feature-kernel 四循环恒等式；
- Schatten--4 四次迹稳定不等式；
- 非交换 cyclic word 组合系数；
- 平窗三个有理 overlap 与正确 family 账本；
- Montgomery--Taylor 窗的多阶 Gauss 收敛和预算；
- 余弦端点窗的二矩闭式、配对对角与阈值裕量。

这些检查不估计真实 zeta remainder。

## 10. 后续推进（笔记 200--201）

笔记 200 已无条件证明 zero-side tail 对四次迹为 (o(N))，并把真正边界缩成
signed-kernel 的本征目标

\[
\|J_T-J_{\infty,T}\|_{\rm HS}^2
=o\!\left(\frac{L^3}{(1+\log L)^2}\right).
\]

笔记 201 又把完整 (2+2) family 精确分成 adjacent product Gram 与
alternating ratio Gram；compact-support path 强制前者 (ab\le X)，真正的
(X^2) Farey 障碍只剩后者。因此本笔记第 9 节的第 1--2 项已被进一步量化，
但 weighted boundary estimate 与 alternating response Schur bound 仍开放。

## 11. 后续推进（笔记 202--224）

笔记 209--222 已闭合 alternating/Farey primitive support，笔记 223 闭合 adjacent supercritical boundary 的相对稠密 good heights。笔记 224 使用 shifted `E_3` sieve 与固定频率间隙，进一步闭合 pure-prime bulk `3+1,4+0` 的共同一侧账本。这里仍不能把式 (6)--(7) 的 finite-to-bulk Schatten 边界视为已证：当前开放输入已精确缩为 signed fourth-cycle boundary、Gamma/continuum mixed words 和最终正规化。

## 12. 后续推进（笔记 225）

笔记 225 没有证明本笔记定理 AED 的全局 Schatten--4 gate；它证明了对 pure-prime 四词更弱但足够的 response-specific 结论：四个 finite Toeplitz factors 与 bulk symbol 的 scalar trace 差由三个 crossing-Hankel nuclear norms 控制，再由真实 prime phases 作 signed height averaging。由此 pure-prime `P^4` 的 finite-to-bulk 边界已闭合；全局 gate 仍只在需要一次控制所有 signed kernels 时开放，当前四矩主线转向 Gamma/continuum mixed words。
