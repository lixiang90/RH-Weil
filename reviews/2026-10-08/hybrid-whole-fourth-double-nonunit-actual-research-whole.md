# 原 whole 四素数近共振：双非单位频块的实际完成与平方根付款

2026-10-08，whole_mixed4。研究源，待不同作者全文审查。
本稿只写此独立来源，不改旧笔记、检查器、输出或 Git。

新付款是原合法 \(\chi\)-载体平均的完整四全异近共振，
在模最大素数平方的精确完成中，
**整个双非单位 Fourier 频块为 \(O_{\phi,\varepsilon}(X^{1/2+\varepsilon})\)**。
这是该带符号平均的上界，不是逐起点绝对值平均或固定起点的频块上界。
证明覆盖全部最大素数、原共同空间变量、两个 sharp prime endpoints、
乘积进位和零加性频率；没有只取稀疏素数子族。
这不是新的 whole 第四矩上界：同一完成的其余频块仍须付款。

## 1. 实际对象及原投影的使用顺序

沿用 475、479、480 的 \(X=T/(2\pi)\)、\(L=\ell=\log X\)、

\[
 d=\lfloor XL\rfloor,\quad \eta=2\pi/L,\quad s_T=T/\sqrt L,
 \qquad b_p=\frac{\log p}{a_LL\sqrt p},\quad a_L\ge c_\phi>0.
\]

这里 \(s_T\) 是载体长度；下文的 \(s\) 专指一个素数。
所有素数都在原 sharp 区间 \(\sqrt X<p\le X\)。
\(\phi\) 是原 even \(C^2\) taper，\(0\le\phi\le1\)。
不升级其光滑性。

使用已证明的实际 half-ratio 展开
[475 的完整远共振来源](hybrid-whole-ratio-smooth-carrier-far-resonance-research-twisted.md)
及 [472](../../notes/472-original-short-carrier-fourth-compression-and-ratio-variance.md)：

\[
 r_\sigma=\frac1L\int_{I_+}\phi(u)^2
 \sum_{p\ne q,\ p'\ne q'}c_{pq}(u)c_{p'q'}(u)
 e^{i\sigma S}K_d^0(S)\,du,
\]
\[
 c_{pq}(u)=b_pb_q\phi(u-\log p)^2\phi(u+\log(q/p)),\qquad
 S=\log\frac{qp'}{pq'},\qquad
 K_d^0(S)=d^{-1}\sum_{k<d}e^{ik\eta S}.
 \tag{1}
\]

载体仍取 475 的同一个固定正密度 \(\chi\)：
\(\chi\in C_c^\infty((0,1))\)、\(\int\chi=1\)，
\(\operatorname{supp}\chi\subset[3/8,5/8]\)，并且

\[
 \Gamma(z)=\int\chi(v)e^{izv}dv,\qquad
 |\Gamma(z)|\le e^{-\sqrt{|z|}/16}\quad(|z|\ge256).
\]

准确平均核及原 near threshold 为

\[
 \Psi(S)=e^{iTS}\Gamma(s_TS)K_d^0(S),\qquad
 \Delta=1024L^{5/2}/X.
 \tag{2}
\]

来源已支付原 actual 和 physical 四词的整个 far union (o(1))，
并支付整个 word 的平均 absolute (P)-crossing error (o(1))。
本稿按这个顺序使用它们：**先作 whole union 的桥，再作 below 的
prime-variable completion**。不从单个 tuple 中删除内部 (P)。
原 repeated union 和 same-prime center 仍用 456、465 的已付合同；
据此，actual 四全异 whole near 可以在这些已付误差后按 (1) 的完整
四全异 physical near 作算术分解。本文的频块定义属于这一步的分解，
不是原三个有限 (P) 各自的 Fourier 频块。

## 2. 固定真实最大素数：共同 profile 仍准确分离

先将 (1) 限定为四个标签互异。真实最大素数唯一，记为 (q)。
将其四种位置分开；若最大素数在分母，交换两对标签，取共轭，
因为 \(\Psi(-S)=\overline{\Psi(S)}\)。
因此只须付最大素数位于分子的两个位置。固定另一个分子素数 (s<q)，
两个分母素数写成 (p,r<q)。准确有

\[
 A=qs,\qquad a=pr,\qquad h=qs-pr,\qquad S=\log(A/a).
 \tag{3}
\]

对最大素数原位于 (1) 第一对的情形，原 profile 权重准确为

\[
 A_p(u;q,s)=b_p1_{\sqrt X<p<q, p\ne s}
       \phi(u-\log p)^2\phi(u+\log(q/p)),
\]
\[
 B_r(u;q,s)=b_r1_{\sqrt X<r<q, r\ne s}
       \phi(u-\log s)^2\phi(u+\log(r/s)).
 \tag{4}
\]

外系数是 (b_qb_s\phi(u)^2/L)。另一分子位置的权重同样是
原两项 (c) 分别归给 (p,r) 后的乘积；具体是

\[
 A_p=b_p1_{\sqrt X<p<q,p\ne s}
       \phi(u-\log p)^2\phi(u+\log(s/p)),
\]
\[
 B_r=b_r1_{\sqrt X<r<q,r\ne s}
       \phi(u-\log q)^2\phi(u+\log(r/q)).
 \tag{5}
\]

两者都保留共同的同一个 (u)，且都满足

\[
 |A_p|,|B_p|\le b_p,\qquad
 \|A\|_2,\|B\|_2\ll_\phi1,\qquad
 \|A\|_1,\|B\|_1\ll_\phi\sqrt q/L.
 \tag{6}
\]

(6) 来自 Chebyshev 和 partial summation：
\(\sum_{p\le z}\log p/\sqrt p\ll\sqrt z\)，
\(\sum_{p\le z}(\log p)^2/p\ll(\log z)^2\)。
它不需要 RH、素数等差数列定理或 Möbius 节省。

余下的四全异条件只有 \(p\ne r\)。将在第8节对其完成的对角项
准确扣除，不以任意矩形代替该 prime graph。

## 3. 模 (q^2) 完成与进位 gate

对固定 (q,s,u)，先考虑尚未扣 (p=r) 的原有限和

\[
 Z_{q,s}(u)=\sum_{p,r}A_pB_r\,
       1_{|\log(A/(pr))|<\Delta}\Psi(\log(A/(pr))).
 \tag{7}
\]

把它准确写为 (a) 的有限和，必须保留

\[
 1\le a<q^2,\qquad a=qs-h.
 \tag{8}
\]

因为真实 (p,r<q)，(pr\in(0,q^2))；在这个 gate 内
\(pr\equiv a\pmod{q^2}\) 与 (pr=a) 等价。
这一步没有把 \(qs-h\) 按 (q^2) 的进位删掉：
不在 (8) 的 (qs-h) 被明确排除。令

\[
 W_A(a)=1_{1\le a<q^2}1_{|\log(A/a)|<\Delta}\Psi(\log(A/a)).
\]

记 (c=q^2)、\(e_c(x)=e^{2\pi ix/c}\)，

\[
 \widehat A(m)=c^{-1/2}\sum_pA_pe_c(-mp),\qquad
 S(m,n;c)=\sum_{x\in(\mathbb Z/c\mathbb Z)^\times}e_c(mx+n\bar x).
\]

由于 raw (p,r) 都是 (q) 的单位，准确完成是

\[
 \sum_{p,r}A_pB_r1_{pr=a}
 =c^{-1}\sum_{m,n\bmod c}S(m,an;c)\widehat A(m)\widehat B(n).
 \tag{9}
\]

在 (8) 外不使用此等式。对 \(q\mid a\)，左侧本来为零；
其后第4节得到的双频块也准确为零，故在计算该块时可以对所有 (a)
统一求和，无需给 (W_A) 添一个会产生额外 Fourier aliases 的删点函数。
最终完整分解仍可以只保留原非零的 (q\nmid a)。

## 4. 双非单位频块的精确 physical 公式

在 (9) 中取 (q\mid m,n)，写 (m=q\mu,n=q\nu)。
没有截断其 dual widths。准确有

\[
 S(q\mu,aq\nu;q^2)=qS(\mu,a\nu;q),\qquad
 \widehat A(q\mu)=q^{-1}\sum_pA_pe_q(-\mu p).
\]

因此这个完整频块是

\[
 \boxed{Z^{\mathrm{nn}}_{q,s}(u)
  =\frac1q\sum_aW_A(a)\sum_{p,r}A_pB_r1_{pr\equiv a\ (q)}.}
 \tag{10}
\]

这里也明确核对了 \(q\mid a\) 的情形：raw \(p,r\in\{1,\ldots,q-1\}\)
都是模 \(q\) 单位，故 \(pr\equiv a\pmod q\) 没有解，(10) 严格为零。
(9) 的完整 raw 求和也严格为零，因为 \(pr=a\) 不可能。
因此最终完整完成仅需 \(q\nmid a\)；第5节为估计双频块统一添回
\(q\mid a\) 的权重，不改变这个块。

对 \(q\nmid a\)，原 Kloosterman kernel 的两个 mixed 频块也准确消失。
完整证明如下：写单位 \(x=y+qk\)，其中 \(y\) 遍历模 \(q\) 单位，
\(k\bmod q\)，且
\(\overline{y+qk}\equiv\bar y-qk\bar y^2\pmod{q^2}\)。
对每个 \(y\)，lift 求和因子是
\[
 \sum_{k\bmod q}e_q(k(m-an\bar y^2)).
\]
若恰有一个 \(m,n\) 可被 \(q\) 整除，\(a\) 是单位，
则括号中的系数始终是模 \(q\) 单位，故该几何和严格为零。
于是 kernel (9) 只剩 unit/unit 与 double-nonunit 两块。
第8节的 graph 对角扣除仍保留其完整完成；不把上述 mixed 消失
错误套用于那个不同的 diagonal kernel。

这也验证物理 residue-multiplicity 估计的确应用于实际 raw supports：
每个 mod (q) residue 至多含一个 \(p\) 或 (r)。
固定 (a) 的粗界为 \(q^{-1}\|A\|_2\|B\|_2\)，
但本文不逐 (a) 累加该粗界。

定义

\[
 H_n=\sum_aW_A(a)e_q(-na),\qquad
 B_n=\sum_{p,r}A_pB_re_q(npr).
\]

联合完成真实位移 (h=qs-a)，(10) 准确变为

\[
 Z^{\mathrm{nn}}_{q,s}(u)=q^{-2}\sum_{n\bmod q}H_nB_n.
 \tag{11}
\]

对每个 (n\ne0\pmod q)，加性 Fourier 矩阵的正交性给

\[
 |B_n|\le\sqrt q\,\|A\|_2\|B\|_2.
 \tag{12}
\]

这里用的是素数 modulus (q) 的乘法置换与普通 Fourier 正交性，
不是删掉 prime graph 后引用 bilinear Kloosterman 定理。

## 5. 光滑 near gate 与全部加性 Fourier 质量

使用一个固定正卷积构造的 cutoff \(\rho_\Delta\)，满足

\[
 0\le\rho_\Delta\le1,\quad
 \rho_\Delta=1\ (|u|\le\Delta),\quad
 \rho_\Delta=0\ (|u|\ge2\Delta),
\]
\[
 \operatorname{Var}(\rho_\Delta)\le2,\qquad
 \|\rho_\Delta^{(j)}\|_\infty
       \le(Cj^2/\Delta)^j.
 \tag{13}
\]

例如，将 \(1_{[-3\Delta/2,3\Delta/2]}\) 与一个总支撑宽
\(\Delta\) 的平移缩放版无限 uniform convolution 相卷积。
第 (j) 阶导数对前 (j) 个 uniform 因子各作一次差分，
给 \(\prod_{i\le j}2/a_i\ll C^j(j!)^2\Delta^{-j}\)，
从而得到 (13)。卷积保持上述两个 plateau/support 合同与 total variation。
这是辅助 gate 的光滑性，不改变原 \(\phi\)。

令 \(\widetilde W_A(a)\) 用 \(\rho_\Delta(\log(A/a))\)
代替原 hard near indicator，仍保留 (1\le a<q^2)。
由于改变处 \(|\log(A/a)|\ge\Delta\)，475 给
\(|\Psi|\le X^{-4}\)。故整个双非单位块的改变不超过

\[
 X^{-4}\sum_{q,s<q}b_qb_s\,q\|A\|_2\|B\|_2
 \ll_\phi X^{-2}L^{-2}=o(1).
 \tag{14}
\]

此处按所有 (a<q^2) 粗估，已包括全部进位 gate 边界。
从此节至第7节的 (H_n) 均用 \(\widetilde W_A\)。

它支撑在 (a\asymp A=qs) 的一个实区间，长度

\[
 N_A\ll A\Delta+1\ll qL^{5/2}.
 \tag{15}
\]

由 (2)，该权重是 \(\rho_\Delta(\log(A/a))(A/a)^{i\theta}\)
对 \(k<d\)、\(v\in\operatorname{supp}\chi\) 的概率平均，其中

\[
 \theta=T+k\eta+s_Tv,\qquad
 T\le\theta\le2T+s_T.
 \tag{16}
\]

对每一个这样的 \(\theta\)，乘以 \(e^{i\theta(a-A)/A}\) 解调。
余相位的 total variation 在 (15) 上至多

\[
 C\theta\Delta^2\ll XL^5/X^2=o(1).
\]

sharp (a<q^2) 最多再加两个 jumps。故解调后的 amplitude 有统一
bounded variation；普通几何和与 Abel 求和给

\[
 |H_n^{(\theta)}|\ll
 \min\{N_A,\|n/q+\theta/(2\pi A)\|_{\mathbb R/\mathbb Z}^{-1}\}.
\]

在整条 (n\bmod q) 网格上求和，至多一个最近点付 (N_A)，
其余以距离 (j/q) 累加，得到

\[
 \boxed{\sum_{n\bmod q}|H_n|\ll_\phi N_A+q\log(2q)
       \ll_\phi qL^{5/2}.}
 \tag{17}
\]

概率平均使用 triangle，保持 (17)。没有令 \(H_0=0\)，
也没有把 \(n\) 限定为人为选出的短 dual interval。

## 6. 非零加性频率：整个最大素数范围付 (X^{1/2+\varepsilon})

由 (6)、(11)、(12)、(17)，

\[
 |Z^{\mathrm{nn},\ne0}_{q,s}(u)|
       \ll_\phi q^{-1/2}L^{5/2}.
\]

原 \(u\) 积分有 \(L^{-1}\int_{I_+}\phi^2\le1/2\)。
全部 \(q,s\) 的外权重准确保留，故

\[
 \sum_q\frac{b_q}{\sqrt q}\sum_{\sqrt X<s<q}b_s
 \ll_\phi L^{-1}\sum_qb_q
 \ll_\phi\sqrt X/L^2.
\]

因此四种最大标签位置的整个非零频率 union 满足

\[
 \boxed{|\mathcal D_{\mathrm{nn},\ne0}|\ll_\phi
       X^{1/2}L^{1/2}.}
 \tag{18}
\]

\(\mathcal D\) 在这里表示原 physical half-ratio 四全异 near 的该频块；
乘以 whole actual/half-ratio 桥的固定因子2不改变幂。

## 7. 零加性频率：内区消去与所有 sharp 边界付款

不能用 (17) 的粗界来付 \(H_0B_0\)。分成下列完整覆盖。

### 7.1 \(A=qs\le4X\)

因 \(s>\sqrt X\)，此时 \(q\le4\sqrt X\)。
\(|H_0|\ll A\Delta+1\ll L^{5/2}\)，
\(|B_0|\le\|A\|_1\|B\|_1\ll q/L^2\)。
全部外权重质量至多 \(C\sqrt X/L^2\)，
而 \(q^{-1}\le X^{-1/2}\)，所以 (11) 的该整个族为 \(O_\phi(L^{1/2})\)
（保守 polylog bound 已足够）。

### 7.2 \(q-s\le4q\Delta\)

这完整支付 upper gate \(a<q^2\) 可能切到 near bump 的全部边界。
每个 \(q\) 至多有 \(O(q\Delta+1)=O(L^{5/2})\) 个整数候选 \(s\)，
且 \(s\asymp q\)。利用 \(b_qb_s\ll1/q\)，每对的零频绝对贡献至多

\[
 C_\phi(\Delta+q^{-2})/L^2.
\]

全部 \(q\le X\) 直接按整数计数，得到 \(O_\phi(L^3)\)。
无需猜测短素数间隔；也不删除这个 sharp 边界。

### 7.3 \(A>4X\) 且 \(q-s>4q\Delta\)

当 \(X\) 足够大，\(\rho_\Delta(\log(A/x))\) 的整个支撑
严格位于 \(1<x<q^2\)；原两端 gate 在此不截断它。
令

\[
 f(x)=\rho_\Delta(\log(A/x))\Psi(\log(A/x)),\quad x>0,
\]

在支撑外置零。这是辅助变量 \(x\) 的 \(C_c^\infty\) 函数。
先对其连续积分支付零频。改用 \(u=\log(A/x)\) 得

\[
 \int f(x)dx=A\int\rho_\Delta(u)e^{-u}e^{iTu}
       \Gamma(s_Tu)K_d^0(u)du.
 \tag{19}
\]

对每个 \(\theta>0\) 及每个固定 \(j\ge0\)，

\[
 \int_{\mathbb R}u^je^{i\theta u}\Gamma(s_Tu)du=0.
 \tag{20}
\]

这是 Fourier inversion：右侧是 \(\chi\) 在负点
\(-\theta/s_T\) 的导数；\(\chi\) 支撑于正区间。
\(\Gamma\) 为 Schwartz，故积分和参数求导均合法。
在 (19) 中用 \(e^{-u}\) 的次数为7的 Taylor 多项式，
各多项式的 whole-line 积分由 (20) 消失。
内区 Taylor remainder 至多 \(C A\Delta^8/s_T\)。
把多项式的 tail 补到 whole line 时，stretched-exponential bound 给

\[
 A\int_{|u|\ge\Delta}(1+|u|^8)|\Gamma(s_Tu)|du
       \ll A s_T^{-1}X^{-4}L^C\ll X^{-3}L^C.
\]

因 \(A\le X^2\)，连续零频故为 \(O(X^{-3}L^C)\)。

还必须支付整数采样 aliases。对此使用完整高阶 Euler–Maclaurin，
而非只取一阶误差。由 (13) 与 log 的导数，

\[
 \left\|\frac{d^j}{dx^j}\rho_\Delta(\log(A/x))\right\|_\infty
        \le(Cj^2/(A\Delta))^j.
\]

对固定 \(\theta\)，Mellin monomial 的准确导数满足

\[
 |D^r(A/x)^{i\theta}|
       \le[(\theta+r)/(Ae^{-2\Delta})]^r.
\]

Leibniz 后，对每个 even \(N\) 有

\[
 \|f^{(N)}\|_\infty\le
 \left[\frac{2T+s_T+N}{Ae^{-2\Delta}}
               +\frac{CN^2}{A\Delta}\right]^N.
 \tag{21}
\]

这是概率平均的导数界；不涉及 prime/profile 的导数。
compact support 的 Euler–Maclaurin remainder 是

\[
 \left|\sum_{a\in\mathbb Z}f(a)-\int f(x)dx\right|
 \le\frac{2\zeta(N)}{(2\pi)^N}\int|f^{(N)}(x)|dx.
 \tag{22}
\]

取 \(N\) 为超过 \(20L\) 的最小偶数。因 \(A>4X\)，
\((2T+s_T)/(2\pi A)\le1/2+o(1)\)，而
\(N^2/(A\Delta)=O(L^{-1/2})\)。
所以 (21) 的 bracket 除以 \(2\pi\) 最终不超过 \(3/4\)。
支撑长度 \(O(A\Delta)\le O(XL^{5/2})\)，(22) 为 \(O(X^{-4})\)。
连同 (19)，得到这个完整内区

\[
 \boxed{|H_0|\ll X^{-3}L^C.}
 \tag{23}
\]

没有把小 \(A\) 时的整数 aliases 或 \(a=q^2\) 边界套进 (23)。
它们已经由7.1、7.2支付。重叠族可以先指定顺序分割，绝对上界保持。
因此全部零加性频率贡献为 \(O_{\phi,\varepsilon}(X^\varepsilon)\)。

## 8. 四全异 graph 的最后对角扣除

(4)、(5) 已准确排除 \(p=s,r=s\)；\(q\) 的最大性排除其他重复。
剩下 \(p=r\) 在原 mod \(q^2\) 完成中用 kernel

\[
 D_a(x,y)=1_{x=y\in(\mathbb Z/q^2\mathbb Z)^\times}1_{x^2=a}
\]

准确相减。令 \(P_q\) 取 dual frequencies divisible by \(q\)。
raw support 每 residue 至多一个，故
\((\mathcal F^{-1}P_q\mathcal F A)(x)=q^{-1}A_{x\bmod q}\)。
因此其完整双频块准确是

\[
 q^{-2}\sum_{x\in(\mathbb Z/q^2\mathbb Z)^\times, x^2=a}
       A_{x\bmod q}B_{x\bmod q}.
 \tag{24}
\]

大 \(X\) 时 \(q\) 为奇素数；每个 \(a\) 至多两个 unit square roots，
且 \(\max_p b_p^2\ll_\phi X^{-1/2}\)。
near bump 的 \(a\) 项数 \(O(qs\Delta+1)\)，故 (24) 的 whole 付款至多

\[
 C_\phi X^{-1/2}\sum_{q,s<q}b_qb_s
          \frac{qs\Delta+1}{q^2}
       \ll_{\phi,\varepsilon}X^{-1/2+\varepsilon}.
 \tag{25}
\]

其中 \(\sum_q(b_q/q)\sum_{s<q}s b_s\ll X/L^2\)，
另一项更小。原 hard/smooth gate 的差仍由 far decay 支付。
故这里没有把重复 prime label 默默留在 four-distinct 图里。

## 9. 新实际付款与仍需闭合的部分

把 (14)、(18)、第7节及 (25) 合成，所有最大标签位置及原同-\(u\)
profile 都在同一预算中，得到

\[
 \boxed{|\mathcal D_{\mathrm{nn}}|
        \ll_{\phi,\varepsilon}X^{1/2+\varepsilon}.}
 \tag{26}
\]

这是 mod \(q^2\) exact completion 的**整个双非单位块**，包括其
零频、全部 \(q,s\)、sharp gate、actual carry 和四全异 graph 扣除。
whole actual 到 physical 的既有 union error 只在第1节使用，
原内部 \(P\) 没有被逐 tuple 删除。normalizer、floor、正高度窗及
\(\chi\) 都保持；不新增零自由或密度前件。

\(1/2<5/7\) 这里只作严格指数比较。本文观察对象是
\(\sigma\in[T,T+s_T]\) 的原 \(\chi\)-carrier signed 平均与 half-ratio
near union；476、480 的 canonical scalar \(\mathcal M_{P_H}\) 使用
\(J=[T/4,4T]\)。二者对象和观察窗不同，不能将 (26) 直接称为
canonical \(\mathcal M_{P_H}\) 的某个已付子块或新的 whole 上界。

原 unit/unit 双频块仍是全宽的原 prime graph；本文没有对其应用
一个不存在的短 dual cutoff，也没有完成它的净带符号上界。
因此 (26) 不降低 476、480 的 whole 第四矩幂，
不推出 \(D_T\) 的净负常数，不更新 \(p_{\rm dg}\)、\(\kappa\)
或引用输入下的 \(\sigma_*\)。

同一合法 good point 仍须一个覆盖剩余完整 near union 的总预算。
若将来得到该总 signed 平均上界 \(B_T\)，475 的既有合同才给
\[
 q_{\sigma_T}\le\frac{2(B_T+o(1))}{\mu_\chi(G_T)}+o(1),\qquad
 \mu_\chi(G_T)=1-O(L^{-1}).
\]
当 \(B_T\) 增长时须保留此概率分母；(26) 单独没有供应这个 \(B_T\)。
本文也不证明 \(\langle|\mathcal D_{\mathrm{nn}}(\sigma)|\rangle\)
或逐 \(\sigma\) 的上界。

可继续工作的具体前件是：在同一个 (9) 完成中，支付未付频块的
完整 \(q,s,a,u\) union，并与本稿已付的双非单位块合成。
此前只有固定 \(a\) 的 residue-multiplicity 粗界；本稿的新步骤是
联合位移完成、原正高度零频消去及全部实际端点付款。

有限归一化自检在 \(q=5,7\) 的全部 \(1\le a<q^2\) 上核对 (10)，
复数浮点误差不超过 \(6\cdot10^{-15}\)，并检查单位 \(a\) 的 mixed
Kloosterman 块消失。它只检查有限核恒等式，不认证以上无限解析估计，
也没有执行外部 Lean 工程；解析结论以本源证明和不同作者审查为准。
