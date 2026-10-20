# F23 的实际物理对象、夹源迹与全部返回的迹类控制

2026-10-20；570 的独立配套原稿。仅本文件为本代理输出，不改状态、节奏或 Git。
输入为 531、532、534、535、560 与既存 `next-joint-error-sign-and-growth-admission.md`。
固定 \(S=\{\infty,2,3\}\)、Sonin cutoff 1、原物理 Hilbert 范数；不增加素数或数值截断。

## 1. F23 与真正物理投影确实属于同一对象

在 \(\mathcal H=L^2((0,\infty),dx)\) 中，令 \(L=1_{(0,1)}\)、\(H=I-L\)，

\[
(U_t f)(x)=e^{-t/2}f(e^{-t}x),\quad F(x,y)=2\cos(2\pi xy),
\quad B=(I-2^{-1/2}U_{\log2})(I-3^{-1/2}U_{\log3}).
\]

这里的 \(L,H\) 是物理乘法投影，不是 source 的支撑投影。
\(F=F^*=F^{-1}\)、\(FU_tF=U_{-t}\)，因而

\[
FBF=B^*,\qquad FW F=W,\qquad W=B^*B.
\]

\(B\) 有界可逆但不酉。仍然有

\[
F_{23}=BFB^{-1}=B(B^*)^{-1}F,
\quad F_{23}^*=F_{23},\quad F_{23}^2=I.
\tag{1}
\]

自伴性可以直接算：\(F_{23}^*=(B^*)^{-1}FB^*=(B^*)^{-1}BF\)，
而 \(B,B^*\) 交换。式 (1) 的酉性来自相位比 \(B(B^*)^{-1}\)，不来自把 \(B\) 当作酉。

实位 Sonin 空间 \(M=\{f:Lf=LFf=0\}\)，其正交投影为 \(P\)。
\(B\) 与 \(B^{-1}\) 都是非负 delay 的绝对算子范数收敛列，故保持高半线。
于是

\[
\{f:Lf=LF_{23}f=0\}=BM.
\tag{2}
\]

取 \(G=(PB^*BP)|_M\)，则真正物理正交投影为

\[
\Pi_{23}=BP G^{-1}PB^*.
\tag{3}
\]

式 (2) 与 (3) 给同一个空间；不存在使用另一个 Fourier 对象替换 full-\(G\) 的问题。
本轮未发现需要冻结 560 既有消费的语义更改。

## 2. 双几何级数的正确模式与实际余项

令 \(\mathcal N=\{2^j3^k:j,k\ge0\}\)。原 Hilbert 空间上

\[
B^{-1}=\sum_{n\in\mathcal N}n^{-1/2}U_{\log n}
\]

绝对算子范数收敛。与有限 \(B\) 相乘可得

\[
F_{23}=\sum_{d\mid6}\sum_{n\in\mathcal N}
 {\mu(d)\over\sqrt{dn}}U_{\log(d/n)}F.
\tag{4}
\]

若截断 \(j,k\le N\)，余项的 operator norm 至多

\[
\Big(\sum_{d\mid6}d^{-1/2}\Big)
\left[{2^{-(N+1)/2}\over(1-2^{-1/2})(1-3^{-1/2})}
 +{3^{-(N+1)/2}\over(1-2^{-1/2})(1-3^{-1/2})}\right].
\tag{5}
\]

式 (4) 对应的分布核为

\[
F_{23}(x,y)=2\sum_{d\mid6}{\mu(d)\over d}
 \sum_{n\in\mathcal N}\cos\bigl(2\pi(n/d)xy\bigr).
\tag{6}
\]

不能在 (6) 中再给每项乘 \(n^{-1/2}\)：这个因子已被 dilation 的核缩放抵消。
将重复尺度合并，写 \(a=\log2,b=\log3\)，真实振幅是

\[
\begin{array}{c|c}
\text{尺度}&\cos\text{ 的振幅}\\ \hline
2^j3^k,\ j,k\ge0&2/3\\
3^k/2,\ k\ge0&-2/3\\
2^j/3,\ j\ge0&-1/3\\
1/6&1/3.
\end{array}
\tag{7}
\]

该合并先在 (4) 的绝对算子范数级数进行，再读分布核。
它不是 ambient 逐项取 trace 的授权。

## 3. 实际 joint cutoff 的 Schatten 控制与严格 gap

置 \(K=LF_{23}L\)。式 (4) 中某一 \(d,n\) 项的 operator norm 至多

\[
(dn)^{-1/2},
\]

其低方形上的核振幅为 \(2/d\)，故 HS norm 至多 \(2/d\)。
对任意 \(r>2\)，Schatten 插值给

\[
\left\|{1\over\sqrt{dn}}L U_{\log(d/n)}F L\right\|_{S_r}
\le (2/d)^{2/r}(dn)^{-(1-2/r)/2}.
\tag{8}
\]

对 \(n=2^j3^k\) 求和，右端是两个收敛几何级数的乘积。因此

\[
K\in S_r\quad\text{对全部 }r>2,
\qquad\text{尤其 }K\in S_3.
\tag{9}
\]

证明没有使用 joint 核的点值或 HS 收敛；它允许 \(K\notin S_2\)。
从 (1) 可知 \(K\) 为紧自伴 contraction。令

\[
\eta=(B^*)^{-1}.
\]

\(\eta\) 及其逆都是反向 causal，保持低半线，并且 \(F_{23}\eta=\eta F\)。
若非零 \(f\) 与 \(F_{23}f\) 都低支撑，则 \(g=\eta^{-1}f\) 与 \(Fg\) 都低支撑，
违反实位 Fourier 的紧支唯一性。紧 contraction 若 norm 为 1 会达到等号并产生这种向量，所以

\[
\kappa=\|K\|<1.
\tag{10}
\]

这也有付费的定量运输。设 \(\kappa_0=\|LFL\|<1\)、
\(m=(1-2^{-1/2})(1-3^{-1/2})\)、\(M=(1+2^{-1/2})(1+3^{-1/2})\)。
因 \(\eta^{-1}\) 保持 low，
\(\|H\eta v\|\ge\|Hv\|/\|\eta^{-1}\|\)。对 low \(f=\eta g\) 应用实位 gap 得

\[
1-\kappa^2\ge (m/M)^2(1-\kappa_0^2)>0.
\tag{10a}
\]

这是 cutoff 1、固定 \(S\) 的真实有费 gap；\(m/M\) 在成长素数集下可退化，
没有 uniform 成长结论。

## 4. 光滑 source 支付 joint 裸块的迹类域

对固定 \(g\in C_c^\infty(\mathbb R)\) 置 \(A_g=\int g(t)U_tdt\)。
535 的实际 source 平滑引理，对 \(F_r(x,y)=2\cos(2\pi rxy)\) 给

\[
\|A_g L F_rL\|_1\le C_g{1+\log r\over\sqrt r},\qquad r\ge1.
\tag{11}
\]

\(C_g\) 支付固定 source 支撑及若干导数；不能当作原 source \(L^2\) 或 \(D_{\log}\) 的统一常数。
其已付证明在输出的 log 坐标采用 H1 平滑与深尾 rank-one 展开，仍适用于每个实际 \(r=n/d\)。
少量 \(r<1\) 的项有光滑低核，另付有限常数。

由于

\[
\sum_{j,k\ge0}(1+ja+kb)2^{-j/2}3^{-k/2}<\infty,
\]

(6) 的第一裸核在 \(A_g L(\cdot)L\) 后于 \(S_1\) 中收敛。因此

\[
A_g L K\in S_1,\qquad A_g Lh(K)\in S_1,
\quad h(K)=K(I-K^2)^{-1}.
\tag{12}
\]

反演源和伴随同样成立。此处不把 \(g=g_\eta\) 的导数费当 uniform；
(12) 仅先给每个固定 \(\eta>0\) 的合法普通 trace。

## 5. 全投影、裸块与所有 returns 的合法分离

本节任意中间 source 上，E23 先指 560 的 overlap／ε23 型
T23−qΓ+P_(2,3)，不含完整 Q 的 pole 预算。只有最终双 pole-zero 且全部 pp 相关零的源，
才识别为 E23=T23−完整Q。这允许对 φη、固定 β 等非 pole-zero 单项合法极化。

设 \(F_*=F_{23}\)。由真正双 cutoff 的 block 计算，完整 overlap 为

\[
O=\Pi_{23}+L+F_*LF_*-I=\Phi(h(K)),
\quad \Phi(T)=LTLF_*H+F_*LTLF_*HF_*.
\tag{13}
\]

这是 bounded operator 身份，保留全部 \((I-K^2)^{-1}\)，没有 finite-angle/return 截断。
例如在 low/high block 中 \(F_*={\small\begin{pmatrix}K&A\\ A^*&D\end{pmatrix}}\)，
\(AA^*=I-K^2\)、\(KA+AD=0\)，两边可直接逐块验证。

对实 source \(g\)，\(Z=A_g^*A_g\) 与 \(F_*\) 交换，且 \(F_*A_g^*=A_gF_*\)。
(12) 支付 (13) 两半夹源项各自 \(S_1\)，故

\[
E_{23}(g)=\operatorname{Tr}(A_gOA_g^*)
=2\Re\operatorname{Tr}_{L}\bigl[h(K)LZH F_*L\bigr].
\tag{14}
\]

复 source 先用实际 ε 密度实偶，将 r=u+iv 写成实/虚部：奇的 Fourier 混合项积分为0，
故 E(r)=E(u)+E(v)，再作 Hermitian 极化。式 (14) 不从完整 TC 反推任意角截断迹收敛。
令

\[
C=h(K)-K=K^3(I-K^2)^{-1}.
\]

(9)、(10) 给真正 ambient 迹类，并有明确固定对象费用

\[
\|C\|_1\le{\|K\|_{S_3}^3\over1-\kappa^2},\qquad
D_{\rm ret}=\Phi(C)\in S_1,
\quad \|D_{\rm ret}\|_1\le{2\|K\|_{S_3}^3\over1-\kappa^2}.
\tag{15}
\]

因此

\[
E_{23}(g)=\operatorname{Tr}(A_g\Phi(K)A_g^*)
          +\operatorname{Tr}(A_gD_{\rm ret}A_g^*)
\tag{16}
\]

是合法 ordinary trace 分离，而不是只对 full inverse 的形式拆分。
对任何 \(L^1\) 一致有界的窄源族，所有 returns 同时满足

\[
|\operatorname{Tr}(A_gD_{\rm ret}A_g^*)|
\le\|g\|_1^2\|D_{\rm ret}\|_1=O(1).
\tag{17}
\]

完整 return 的源核是 \(\operatorname{Tr}(D_{\rm ret}U_t)\)，连续有界。
在固定 source 窗 \(U\) 上其源 operator 还属于 \(S_1\)，trace norm 至多
\(|U|\|D_{\rm ret}\|_1\)。这些费用是 fixed \(S\) 的，未证 cofinal \(S_L\) 控制。

## 6. 裸双尺度核如何合法消费，哪里仍须另付

在 (16) 第一半中，第一 Fourier 因子可用 (11) 在 \(S_1\) 截断，
第二因子可用 (4) 在 operator norm 截断。TC 乘 bounded 的连续性给 joint trace 极限。
每个有限 pair 可按真实 source boundary 的矩形作普通核积分，之后才取极限。
这个组织说明 actual bare 的分布极限是什么，不预先宣称其 pair 核绝对 \(L^1\) 可和。

固定正 \(t\)，振幅为 1 的 pair 块为

\[
I_{r,s}(t)=e^{t/2}\int_{e^{-t}}^1\int_0^1
\cos(2\pi r xz)\cos(2\pi s e^t xz)\,dz\,dx.
\tag{18}
\]

差相位块有统一界

\[
|I_{r,s}(t)|\le C_J\{(1+|r-e^ts|^2)^{-1}
                       +(1+|r+e^ts|^2)^{-1}\},\quad t\in J\Subset(0,\infty).
\tag{19}
\]

证明是先积分 \(z\)，再用两端点 Si 差；小相位直接有界，大相位的两端点
\(\pi/2\) 先抵消，再给二阶衰减。不能把单个 Si 的常数尾留作 \(1/|r-e^ts|\) 费用。

\(r/s\) 的 joint 比例稠密，故 single-prime 的统一 nonresonant phase gap 不再适用。
仅识别 \(r/s=3/2\) 的 exact 子列不足以给 actual signed 渐近；其余所有 pair 仍须控制。
可用 507 已核一手定理的固定 \(2,3\) 参数化，给

\[
|(j-j'+1)\log2+(k-k'-1)\log3|
\ge c(1+H)^{-C}\quad\text{非 exact},
\tag{20}
\]

\(H\) 为 pair 的最大非负 exponent height，边界负指数只改变常数。
参数化责任、平滑极限与返回原 norm 由 mixed 配套稿另行核，不从 (19) 跳过。

一种可消费的平均控制策略是：对宽度 \(\eta\)、\(L^1=O(1)\)、
\(L^\infty=O(\eta^{-1})\) 的物理平滑核，先切 \(H\le\eta^{-\epsilon}\)，
\(\epsilon C<1\)，用 (20) 保留 phase separation；大 height 用 (19) 的积分界
\(O((\eta s)^{-1})\)。近 \(t=\log(3/2)\) 的 comparable pair 有 \(s\ge e^{cH}\)，
每个高度只有多项式个 pair，所以高 height 的费用小于
\(C\eta^{-1}\sum_{H>\eta^{-\epsilon}}(1+H)^3e^{-cH}\)。
此处的 Matveev/Baker 独立输入是有限位真实 \(2,3\) 的定量算术，不依赖 ζ 零点；
推广任意 g-integer 时不能免费继承。

## 7. 原范数、全部源项及净后果边界

560 已付的恒等式为 \(E_{23}=T_{23}-Q_W\) 在本双 pole-zero、
支撑直径小于 \(\log2\) 的实际源上成立：完整 Γ 始终保留；
两 pole 矩按 exact 方程消去；全部实际 prime powers 因相关支撑严格为 0，未删项近似。
本稿的 (17) 是 \(L^1\) 质量费用，不是窄源 original norm 1 费用。

若另稿付出 unnormalized \(\log^2(1/\eta)\) signed 项，因

\[
\|g_\eta\|_2^2\asymp\eta^{-1},\qquad
\|g_\eta\|_{D_{\log}}^2\asymp\eta^{-1}\log(1/\eta),
\]

换回原 \(L^2\) norm 后尺度为 \(\eta\log^2(1/\eta)\to0\)，
按 \(D_{\log}\) 能量规范化则为 \(\eta\log(1/\eta)\to0\)。
这与 fixed-window compact 不矛盾，也不推出 \(Q_W\) 负值。

本稿真实新输入是将 single-prime 已付平滑/迹类机制，按明确费用核到 actual joint
对象与全部 returns；评价了旧准入中可能的语义风险并排除了错对象。
它本身尚未支付 mixed signed 主系数，不声称完整 Weil 正性、独立 RR 容量、
成长 \(K_L\) 费用或 actual whole 4/5 的改善。宏观 Goal 保持 open。

### 依赖与消费清单

- 对象/角色：物理 \(L^2(dx)\) 的 \(F_{23},K,\Pi\)；source 是 log 变量的 \(g\)，两者不混。
- 原 norm/域：每 fixed smooth compact \(g\) 合法 trace；560 扩张的原 zero-extension \(D_{\log}\) 不改。
- 量词：fixed \(S=\{\infty,2,3\}\)、cutoff1、先 fixed \(\eta>0\) 付 trace，再考虑窄源极限。
- 已付：same physical projection、source \(S_1\) 收敛、joint \(S_r\)、严格 cutoff gap、full returns \(O(1)\)。
- 未付/另稿：所有 nonexact dense ratio 平滑控制、mixed 主系数与符号；global 成长费用无运输。
- 最强旧对照：560 fixed-window compact/全部 prime powers 与 542+555→557 leading4/5 保持，不把本稿换表示当新 whole 界。
