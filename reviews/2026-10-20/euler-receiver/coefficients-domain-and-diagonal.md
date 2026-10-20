# 实际 finite Euler 乘子、receiver 系数与原域／diagonal 准入

2026-10-20，独占 producer 稿；不改公共 STATE、cadence 或 Git。
已恢复 README／STATE／check／show、同 G20261014／0c4f 冻结基线、
C034、cycle14、D20261020N、MACRO_FRONTIER 及 571／receiver-norm 原件。
这是 cycle14 规定的一次来源准入原稿；root 是否据三稿净后果准入数学合同，另按实际结果决定。
原件出稿不等于 root 消费。

## 0. 三句输入、测试与净后果

输入是 571(9) 的完整真实 receiver 和实际有限 Euler 多项式 bar b_F(R)，
不截 D、不自由选择低半线输入。可判测试是同 delay 合并后的系数、原 L²(t>0) 域、
diagonal 及 MV 所需加权域；最便宜反测是单 prime。
下文证明 cofinal b-weighted diagonal 有 O(L⁴) upper，不付 m/M condition；
同时证明粗整数间距版本的无限 MV 充分域仍不满足。
这不是 finite-height coherent tail、原源容量或实际 Sonin 误差的费用；
更精确的 fixed-F local-gap MV 是合法付费修复，须由另一稿单独核其常数和成长量词。

## 1. 完整实际对象与精确 coherent 系数

H=L²(R,dy)，U_a f(y)=f(y−a)。先固定有限 prime 集 F，

\[
 B_F=\prod_{p\in F}(I-p^{-1/2}U_{\log p}),\qquad D_F=B_F^{-1},
 \quad b_F(R)=\prod_{p\in F}(1-p^{-1/2}e^{-iR\log p}).       \tag{1}
\]

记 N_F 为 F-smooth 正整数集，包含 1；rad(F)=∏_(p∈F)p。
令 P_T=1_(0,T)、L_-=1_(-∞,0)，T>0，
w_(T,R)(y)=e^(iRy)1_(0,T)(y)/√(2π)，
v_(T,R)=L_-D_F*P_Tw_(T,R)。完整 D_F 的绝对 operator-norm 级数给

\[
 v_{T,R}(-t)=\frac{e^{-iRt}}{\sqrt{2\pi}}
       \sum_{m\in N_F}m^{-1/2}e^{iR\log m}
                  1_{\{t<\log m<t+T\}},\qquad t>0.           \tag{2}
\]

将实际 bar b_F(R)=Σ_(d|rad(F)) μ(d)d^(-1/2)e^(iRlog d) 乘入，
按相同 n=dm 的 delay 先 coherent 合并，严格得到

\[
 \boxed{\overline{b_F(R)}v_{T,R}(-t)
  =\frac{e^{-iRt}}{\sqrt{2\pi}}
       \sum_{n\in N_F}a_{n,T}(t)e^{iR\log n},}\qquad
 a_{n,T}(t)=n^{-1/2}\!\sum_{\substack{d\mid\operatorname{rad}(F)\\d\mid n}}
       \mu(d)1_{\{t<\log(n/d)<t+T\}}.                       \tag{3}
\]

这里不是把每个 (d,m) label 的平方分别求和；那样会漏掉 Euler 差分。
a_(1,T)=0。由于 ordinary unique factorization，n 标签与 log n 的不同实际 delay 一一对应。
一般 g-primes 若存在 exact collisions，必须先按实际 log value 再合并，不能沿用本文的 label diagonal。

逐 ALL T>0 的身份最后直接取 T=完整
Γ(R)=Re ψ(1/4+iR/2)−log π>0；没有把 Γ 改成 log，也没有将 T 与 R 独立取平均。

### 1.1 同一个系数里的两边界协同支撑

若 n>1，记 y=log n、h=log rad(n)。所有 divisor delays log(n/d) 落在 [y−h,y]。
当 (t,t+T) 包含整个区间时，完整有限差分的和为 Σ_(d|rad(n))μ(d)=0；
当该窗口与区间不相交时同样为零。因此 exact 地有

\[
 \operatorname{supp}a_{n,T}\subset
 \big([y-h-T,y-T]\cup[y-h,y]\big)\cap[0,\infty).             \tag{3a}
\]

若 T<h 两段可以重叠；本式仍正确，不假设它们总是分离。
这呈现同一 Euler 系数的上下窗口边界协同，不能逐 divisor／逐边界取绝对值后再宣称相同取消。
它也不单独证明 infinite coherent tail 小：系数个数、大小、相位和 finite-height 域仍须支付。

## 2. 原 receiver L² 域与合法换序

本稿系数空间是 V=L²((0,∞),dt)，即 receiver 原物理 dy norm 经 t=−y 的酉坐标；
不是原 Weil 源的 du L²／zeroextension Dlog 范数。
对 fixed F/T，

\[
 \sum_{n\in N_F}\|a_{n,T}\|_V
  \le 2^{|F|}\sqrt T\sum_{n\in N_F}n^{-1/2}
  =2^{|F|}\sqrt T\prod_{p\in F}(1-p^{-1/2})^{-1}<\infty.      \tag{4}
\]

因此 (3) 是 V 中绝对、对 R 一致收敛的级数，允许全部有限 Euler 重排及
Bohr 平均；对每个 R 其右侧确是原 receiver，而不是新的概率模型。
由外面的 t-modulation 酉性，

\[
 |b_F(R)|^2\|v_{T,R}\|^2=\frac1{2\pi}
       \left\|\sum_{n\in N_F}a_{n,T}e^{iR\log n}\right\|_V^2. \tag{5}
\]

固定 F/T 后的 Bohr 均值为

\[
 \lim_{H\to\infty}\frac1H\int_A^{A+H}|b_F(R)|^2\|v_{T,R}\|^2dR
       =\frac{\mathcal D_F(T)}{2\pi},\qquad
 \mathcal D_F(T)=\sum_{n\in N_F}\|a_{n,T}\|_V^2.             \tag{6}
\]

极限对起点 A 一致，但它的 fixed-F/T 量词不支付 F、T=Γ(R)、高度窗同步成长。
下面的 diagonal upper uniform in T，也不能自行删除有限高度 off-diagonal。

## 3. support／radical 分组及无 condition 的多项式 diagonal

对非空 S⊂F 记 r_S=∏_(p∈S)p，A_p=log p；令

\[
 H_S(T)=\left\|\prod_{p\in S}(I-\tau_{A_p})1_{(0,T)}\right\|_{L^2(R)}^2,
       \qquad (\tau_a f)(x)=f(x-a).                          \tag{7}
\]

原半线 diagonal 本身还可精确写成

\[
 \|a_{n,T}\|_V^2=n^{-1}
 \sum_{d,e\mid\operatorname{rad}(n)}\mu(d)\mu(e)
     \ell_T(\log(n/d),\log(n/e)),
 \quad\ell_T(x,z)=\min\{\min(x,z),(T-|x-z|)_+\}.             \tag{7a}
\]

相同 delay 的 Euler 取消在这个 signed 双和内，不能在平方前丢掉。
若 supp(n)=S，(3) 的有限差分在整线只差平移／反射，所以限制 t>0 后有

\[
 \|a_{n,T}\|_V^2\le n^{-1}H_S(T),\qquad
 \sum_{\operatorname{supp}(n)=S}\frac1n
       =\prod_{p\in S}\frac1{p-1}.                          \tag{8}
\]

每个 τ_a 是整线酉算子。选 S 中最小 prime p；先做该差分，其 exact norm² 为
2min(T,log p)，其余 |S|−1 个差分每次最多乘 norm² 因子 4。因此

\[
 H_S(T)\le2\,4^{|S|-1}\min(T,\log p).                      \tag{9}
\]

按最小 prime 组合同一 S 的全贡献，由 (8)–(9) 得

\[
 \boxed{\mathcal D_F(T)\le
 2\sum_{p\in F}\frac{\min(T,\log p)}{p-1}
     \prod_{\substack{q\in F\\q>p}}\left(1+\frac4{q-1}\right).} \tag{10}
\]

这是完整无限 n 的 diagonal，没有 D-tail 截断、没有 m^−1 或 M。
对 X≥3、F⊂{p<X}，

\[
 1+\frac4{q-1}\le(1-1/q)^{-4},\qquad
 \prod_{p<q<X}(1-1/q)^{-4}
       \le C\left(\frac{\log X}{\log p}\right)^4.             \tag{11}
\]

后一式是旧 Mertens product 上下界的直接比值，非新外部输入。
代入 min(T,log p)≤log p，且
Σ_p[(p−1)(log p)³]^−1<∞（甚至全整数对应级数已收敛），得到

\[
 \boxed{\sup_{T>0}\mathcal D_F(T)\le C(\log X)^4.}          \tag{12}
\]

特别 F_L={p<e^(2L)} 时 D_(F_L)(T)=O(L⁴)，uniform ALL T>0。
常数绝对，使用 classical Mertens（571 已付经典 Mertens／Abel 来源），不使用 ζ 未知零点。
这个 upper 不宣称最优；无须再扩参数／优化次数才能作本次准入决定。

净内容是实际 |b|² 权的 fixed-F diagonal 不必付粗 M²/m² 指数 condition。
它比“用 M² 乘旧 receiver diagonal”更具体，却不是 finite-height 结论；
off-diagonal／tail 若未付，(12) 不能报告为原范数 O(L⁴) 的同步高度平均。

## 4. 单 prime 原域负对照：有限差分未进入粗整数 gap 的无限 MV 充分域

取 p∈F，n=p^k。由于 supp(n)={p}，其它 primes 不进入 (3)：

\[
 a_{p^k,T}(t)=p^{-k/2}
 \big[1_{(k\log p-T,k\log p)}(t)
      -1_{((k-1)\log p-T,(k-1)\log p)}(t)\big]1_{(0,\infty)}(t).
                                                                    \tag{13}
\]

当 (k−1)log p>T 时，两 interval 均在正半线，故严格

\[
 p^k\|a_{p^k,T}\|_V^2=2\min(T,\log p)>0,
 \qquad \sum_{n\in N_F}n\|a_{n,T}\|_V^2=\infty.            \tag{14}
\]

所以“有限 Euler 差分已经使完整级数满足 δ_n≥1/(2n) 所给
Σ n||a_n||²<∞ 充分域”的说法为假。有限截断 Y 下此成本至少按 log Y 长大，
但这不意味着实际 finite-height error 必须如此，亦不是 receiver 能量 lower。

**合法逃逸必须保留：** (14) 仅否定该粗间距版本的无限域。
单 prime 的真实频率 gap 为 log p，故 Σδ_n^−1||a_n||²<∞，
可合法用 MV Corollary 2 的 uniform-gap 版本。
一般 fixed finite F 的多 log Diophantine 下界也可能给
δ_n≥C_F(1+log n)^−M_F，再由 fixed-F 几何系数衰减支付相应域。
这些是合法 paid 修复，不能由 (14) 排除；其真实 C_F、M_F、finite-height 费用和
cofinal 成长责任留在本次另一独立来源稿，不把“存在 fixed-F 常数”吞成 uniform O(1)。

## 5. Γ、两边界与实际 Sonin 的消费限制

所有 (3)、(10)、(12)、(14) 均对 ALL T>0 成立，因此可直接用完整 T=Γ(R)。
但对随 R 变化的 T_R，系数本身也变化；固定 T 的 MV 或 Bohr 身份不能不付
endpoint／变窗费用就应用。式 (12) uniform in T 只处理 diagonal，不处理这个问题。

571 的同一真实 pair v=L_-D*Pw、u=H_+DPw 和 full inverse J^−1 始终保留，

\[
 \delta_{\rm win}=\|v\|^2+\|u\|^2-
        \langle(v,u),J^{-1}(v,u)\rangle,
 \qquad(\delta_{\rm win})_+\le\|v\|^2.                       \tag{15}
\]

对 carrier 反射给 ||u||=||v||，乘同一实际 |b|² 后两边界的 norm 消费相同；
(15) 仍包含全部 returns。本稿有限 Euler 计算只处理该 receiver norm，
未将 J^−1 截为首个 cross，也没有宣称由 norm diagonal 得到 signed 有利比较。
负向控制、κ/gap 以及 actual k_R／Sonin G_F 全逆的运输另外支付。

模型 δ_win 不等于实际 ε_F 或 570 的 E_F。完整 source 身份仍是 560：

\[
 2\pi\rho_F(R)=\Gamma(R)
 -2\sum_{p\in F,k\ge1}(\log p)p^{-k/2}\cos(kR\log p)+\epsilon_F(R),
\]
\[
 Q_W(r)=t_F(r)-\langle r,K_{F,I}r\rangle
   +2|\langle r,\cosh(u/2)\rangle|^2
   -2|\langle r,\sinh(u/2)\rangle|^2.                        \tag{16}
\]

Γ/contact、所有 prime powers 与两个 pole 均保留；没有给具体 r 的消失条件，
不能把它们置零。原 du L²／zeroextension Dlog 与本文 receiver dy norm 继续分角色。

## 6. 准入判定、最强旧扣除与一般 g 范围

已证明：(3) exact coherent 系数及原域；(10) support 分组；(12) cofinal poly diagonal；
(14) 粗整数 gap 无限域失败，同时保留更精确 local-gap 的合法修复。
未证明：同步 finite-height 的 weighted coherent tail 小费、原 unweighted receiver norm 小费、
负向 signed 比较、actual Sonin 完整逆运输、危险 core 或 ALL complex 源容量。
即便另一稿支付 weighted mean，不能免费除实际 |b(R)|² 得原 unweighted norm，
也不能跳过 k_R→w_R／全逆成长期误差。

最强旧 whole 后果仍是 542+555→557 leading 4/5；本稿不改该预算，
亦不声称独立 RR／有效对应容量。要求完整 mixed Weil Gram PSD 仍是等价改写，
本稿的独立输入只是 ordinary multiplicative finite difference、L² 域和已知 Mertens。

一般 free finite g-primes 若 q_j、正 delay 可逆因果，(3) 的乘法 label 版本可照写；
exact collision 必须先 coherent 合并，随后 (8)/(11) 的 ordinary prime 因子与 Mertens 不再自动成立。
一般 duality 本身不付 bounded inverse、真实 local gap、有限高度域或正极化。
连续 g 分布需自身的 Fourier／Plancherel 设施，不能继承离散 label diagonal。

本稿无后台数值／下载进程；最终消费以 root 对齐本稿与 tail／full inverse 稿后独立终审为准。
