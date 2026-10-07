# 原完整比值方差：合法光滑载体消去全部远共振

2026-10-08，twisted_research。父任务报告的新轮基线为 46106dc；
本稿只新增研究源，不改 Git、math、旧笔记、脚本、输出或论文。
状态：完整新推导，待另一作者全文审查。

本轮实际支付的是整个原素数范围、所有标签和原内部 P 保留的
远共振 signed union。根节点提出在合法短载体窗口内使用固定
正光滑密度；本稿独立核验原对象，并构造一个明确的固定密度，
将剩余频率带收窄到 polylog(X)/X。完整近共振上界仍未证明。

## 1. 冻结的原对象和实际使用的输入

canonical UTF-8 LF 只统一 CRLF/lone CR，不 trim 或改变 EOF。

| 输入及范围 | canonical LF SHA-256 |
|---|---|
| [472 原全部四阶 P 与 ratio 桥](../../notes/472-original-short-carrier-fourth-compression-and-ratio-variance.md) | 9856885e932a892cf7c33ece82f430c2ec13004555eb52da2f1e8b1ec6bb2683 |
| [原完整 half-ratio 及同一 good carrier](hybrid-whole-short-carrier-ratio-and-distinct-criterion-research-twisted.md) | c7ff142ebe15232542626e4feda3c05a1285cbf7bff64f462e734c662dafea53 |
| [原 raw short-carrier leakage](hybrid-anchored-carrier-averaged-fourth-projection-gap-research-radial.md) | c0e874ab9061982c8ef4365c8e9313eeac77eeddb756dc0b455cab3349f99dd8 |
| [474 完整 scalar 单侧准入](../../notes/474-original-short-carrier-canonical-scalar-fourth-admission.md) | 37306c6d403f48c93d5d0f92782088225084e2e4b6b694cd89644a75fe39e99f |
| [228 移动零点块合同](../../notes/228-relative-dense-zero-block-transfer.md) | 2cc8a3f5eb0e66ef0a6306a317a1e2b03c046c62b8284a87ccbee8e8130181ae |

沿用
\[
 X=T/(2\pi),\quad L=\log X,\quad d=\lfloor XL\rfloor,\quad
 \eta=2\pi/L,\quad s=T/\sqrt L,\quad I=[-L/2,L/2],
\]
\[
 E_\sigma e_k=L^{-1/2}1_Ie^{i(\sigma+k\eta)u},
 \qquad \sigma\in J_T=[T,T+s],\qquad 0\le k<d.
 \tag{1}
\]
原 even C² taper \(\phi\)、finite \(a_L=\|\phi\|_2^2/L\ge c>0\)、
sharp high primes \(\sqrt X<p\le X\) 与
\[
 b_p=\frac{\log p}{a_LL\sqrt p},\qquad
 m_H=\sum_{\sqrt X<p\le X}b_p\ll_\phi \frac{\sqrt X}{L}
 \tag{2}
\]
共同冻结。Chebyshev 与 partial summation 即给 (2)。
平移仍是实线零延拓 \(R_tf(u)=f(u+t)\)，没有周期化。

写
\[
 A=-\sum_pb_pM_\phi R_{\log p}M_\phi,\quad G=A^*A,\quad
 D_+=\sum_pA_p^*A_p,\quad R_+=G-D_+,
 \qquad r_\sigma=d^{-1}\|R_+E_\sigma\|_{\rm HS}^2.
 \tag{3}
\]
以下远区付款不使用 [R]、新的零自由输入、full fourth boundedness
或未知 Möbius saving；也不需要先调用 474 的 BV/L⁴ upper。

## 2. 同一个 u 的半区间支撑，及准确 carrier 特征函数

令 \(\xi_{pq}=\log(q/p)\)，并置
\[
 c_{pq}(u)=b_pb_q\phi(u-\log p)^2\phi(u+\xi_{pq}),\qquad p\ne q.
\]
冻结源给准确式
\[
 r_\sigma=\frac1L\int_{I_+}\phi(u)^2
       \sum_{\substack{p\ne q\\p'\ne q'}}
 c_{pq}(u)c_{p'q'}(u)
 e^{i\sigma S}K_d^0(S)\,du,
 \quad
 S=\xi_{pq}-\xi_{p'q'},\quad
 K_d^0(S)=\frac1d\sum_{k=0}^{d-1}e^{ik\eta S}.
 \tag{4}
\]
该式是展开完整平方，所有 repeated/distinct 标签自然保留。
两个 \(c\) 共用同一 u；没有独立重选窗口或 prime phases。

若 \(c_{pq}(u)\ne0\)，则 \(z=u-\log p\in I\)，并且
\[
 v=u+\xi_{pq}=z+\log q\le L/2,\qquad
 v\ge -L/2+\log q>0.
\]
故 \(v\in I_+=(0,L/2]\)。同时 \(u\in I_+\)。两个非零项于是满足
\[
 S=v-v',\qquad |S|\le L/2.                         \tag{5}
\]
这准确消除 half-ratio 平方中的 \(\pm L\) alias；不能仅由两个
terminal \(\phi\) 各自支撑于 I 推出 (5)，必须同时使用 q、q' 为 high。

取任一固定非负密度 \(\chi\in C_c^\infty((0,1))\)，\(\int\chi=1\)，
定义同一合法载体窗口的概率平均
\[
 \langle F\rangle_\chi=
 \frac1s\int_T^{T+s}\chi((\sigma-T)/s)F(\sigma)\,d\sigma,
 \qquad
 \Gamma_\chi(z)=\int_0^1\chi(v)e^{izv}\,dv.          \tag{6}
\]
这里 \(\Gamma_\chi\) 是正号特征函数；若 Fourier transform 定义为
\(\widehat\chi(z)=\int\chi(v)e^{-izv}dv\)，则
\(\Gamma_\chi(z)=\widehat\chi(-z)\)。准确平均核为
\[
 \Psi_\chi(S)=e^{iTS}\Gamma_\chi(sS)K_d^0(S).
 \tag{7}
\]
特别地 \(|K_d^0(S)|\le1\)，没有以 positive kernel 替换其相位。

对 (4) 的任意 tuple 子集 \(\mathcal A\)，令
\(\mathcal R_{\mathcal A}\) 为该子集在同一积分中的 signed contribution。
因为 \(0\le\phi\le1\)，全标签绝对质量准确有
\[
 \frac1L\int_{I_+}\phi^2
   \sum_{\substack{p\ne q\\p'\ne q'}}c_{pq}(u)c_{p'q'}(u)\,du
 \le \frac12 m_H^4.
 \tag{8}
\]
所以任何 \(\Delta>0\) 均有
\[
 \left|\langle\mathcal R_{\mathcal A\cap\{|S|\ge\Delta\}}
                  \rangle_\chi\right|
 \le \frac12m_H^4
       \sup_{|z|\ge s\Delta}|\Gamma_\chi(z)|.
 \tag{9}
\]
不必把 repeated 与 four-distinct 分别用新的算术假设估计。

## 3. 同一短窗口的固定正 C∞ 密度：可核验的 stretched-exponential 衰减

给出 (6) 的一个具体固定选择。令
\[
 a_n=\frac1{4n(n+1)},\qquad
 U_n\text{ 为 }[-a_n/2,a_n/2]\text{ 上的 uniform probability density}.
\]
将有限卷积 \(U_1*\cdots*U_N\) 平移至中心 \(1/2\)，记为 \(\chi_N\)。
由于 \(\sum_na_n=1/4\)，所有 \(\chi_N\) 支撑于 \([3/8,5/8]\)，
非负、积分一，且第一因子 \(a_1=1/8\) 给
\[
 \|\chi_N\|_\infty\le8,\qquad
 \Gamma_N(z)=e^{iz/2}\prod_{n=1}^N
      \operatorname{sinc}\!\left(\frac{z}{8n(n+1)}\right),
 \quad \operatorname{sinc}x=\frac{\sin x}{x}.       \tag{10}
\]

为避免把形式 infinite product 直接当成 smooth density，逐项证明：
对每个固定 z，尾部 sinc 为 \(1+O_z(a_n^2)\)，
\(\sum a_n^2<\infty\)，所以 \(\Gamma_N\) 有点态极限 \(\Gamma\)。
对每个固定整数 m，先固定 \(k>m+1\)，前 k 个因子给
\[
 |z|^m|\Gamma_N(z)|
 \le C_k|z|^m(1+|z|)^{-k},\qquad N\ge k.
 \tag{11}
\]
右边可积。Fourier inversion 与 dominated convergence 于是使
\(\chi_N\) 在每个 C^m norm 中收敛到同一个 \(\chi\)。
故 \(\chi\in C_c^\infty((0,1))\)、\(\chi\ge0\)、\(\int\chi=1\)、
\(\operatorname{supp}\chi\subset[3/8,5/8]\)、\(\|\chi\|_\infty\le8\)。
积分一来自共同 compact support 上的 uniform convergence。
这个构造没有扩大合法 \(\sigma\) 窗口。

若 \(|z|\ge256\)，取 \(N_0=\lfloor\sqrt{|z|}/8\rfloor\)。
对 \(n\le N_0\)，有 \(8n(n+1)\le16N_0^2\le|z|/4\)，
所以对应 sinc 因子的模至多 \(1/4\)。又
\(N_0\ge\sqrt{|z|}/16\)，因此无限乘积严格满足
\[
 |\Gamma_\chi(z)|\le4^{-N_0}
   \le \exp(-\sqrt{|z|}/16),\qquad |z|\ge256.
 \tag{12}
\]
仅使用 \(\log4>1\) 作了保守放松；没有 finite mock 或数值拟合。

## 4. 整个远区的小量：近带只剩 polylog(X)/X

取明确的确定阈值
\[
 \Delta_T=\frac{1024L^{5/2}}X.                     \tag{13}
\]
它趋零，且
\[
 s\Delta_T=2048\pi L^2\ge4096L^2.
\]
当 L 足够大，(12) 给
\[
 \sup_{|S|\ge\Delta_T}|\Gamma_\chi(sS)|
 \le e^{-4L}=X^{-4}.
 \tag{14}
\]
由 (2)、(9) 得到整个 high 范围的实际新付款
\[
 \boxed{\left|\langle\mathcal R_{\mathcal A\cap
                 \{|S|\ge\Delta_T\}}\rangle_\chi\right|
       \ll_\phi X^{-2}L^{-4}=o(1).}               \tag{15}
\]
该 bound 对任意 tuple 子集统一，包括完整四全异与完整 repeated，
没有限定 prime dyadic cap、固定窗口中的少数标签、或改变系数。
hard frequency indicator 可直接使用，因为求和本身有限；
这里不必 Fourier 展开该 indicator，不会留下新的 gate tail。
原 \(\phi\) 仍只有 C²，没有被改为 Schwartz 或 analytic。

若只取一般固定正 C∞ 密度，逐次分部积分也给
\(|\Gamma_\chi(z)|\le C_A(1+|z|)^{-A}\)。
因此任意 fixed \(\varepsilon>0\) 的
\(\Delta=X^{-1+\varepsilon}\) 远区可由 \(A>3/\varepsilon\) 支付。
(10) 的固定显式密度进一步把这个幂次 near 改为 (13) 的 polylog near。

作为对比，对原 box carrier 平均，
\[
 \Psi_{\rm box}(S)=e^{i(T+s/2)S}
        \operatorname{sinc}(sS/2)K_d^0(S).
 \tag{16}
\]
(5) 使 \(|K_d^0(S)|\ll (X|S|)^{-1}\)，故
\[
 |\langle\mathcal R_{\{|S|\ge\Delta\}}\rangle_{\rm box}|
 \ll \frac{m_H^4}{Xs\Delta^2}
 \ll L^{-7/2}\Delta^{-2}.
 \tag{17}
\]
取 \(\Delta=L^{-1}\) 仅给 \(O(L^{-3/2})\)。
(15) 的加强来自合法 carrier 密度的高阶光滑性，不来自把 box kernel
的 fixed-order 衰减免费升级。

## 5. 直接 actual 四词证明：所有 internal P 原样保留

远区不必依赖逐 tuple 的 P 删除。令
\[
 E_0e_k=L^{-1/2}1_Ie^{ik\eta u},\qquad
 E_\sigma=M_{e^{i\sigma u}}E_0.
\]
对任一 prime direction \(\epsilon=\pm1\)，准确有
\[
 C_{p,\epsilon}(\sigma)
 :=E_\sigma^*[-b_pM_\phi R_{\epsilon\log p}M_\phi]E_\sigma
 =e^{i\sigma\epsilon\log p}\widetilde C_{p,\epsilon},
 \qquad \|\widetilde C_{p,\epsilon}\|\le b_p.       \tag{18}
\]
原 \(E_0\) 是 interval zero-extension carrier；这个 modulation
恒等式不让 P 与 real-line Fourier guard 交换。

任一有序 actual 四 tuple 准确等于
\[
 \tau\prod_{j=1}^4 C_{p_j,\epsilon_j}(\sigma)
 =e^{i\sigma S}\tau\prod_{j=1}^4\widetilde C_{p_j,\epsilon_j},
 \quad S=\sum_j\epsilon_j\log p_j,\quad
 \left|\tau\prod_j\widetilde C_{p_j,\epsilon_j}\right|
 \le\prod_jb_{p_j}.                               \tag{19}
\]
每个 \(\widetilde C\) 都保留原压缩；所有三个 internal P 仍在实际乘积里。
归一化 \(|\operatorname{Tr}M|/d\le\|M\|\) 给最后一个 bound，
没有 free cyclic physical trace。

对任何 four-label/sign 子集及任意 ordered H/L word，(6)、(14)、(19)
于是直接给
\[
 \left|\left\langle
   \sum_{\substack{\text{该子集}\\|S|\ge\Delta_T}}
       \tau\prod_j C_{p_j,\epsilon_j}(\sigma)
                 \right\rangle_\chi\right|
 \le X^{-4}\prod_jm_{R_j}
 \ll_\phi X^{-2}L^{-4}.
 \tag{20}
\]
有向 signs 的有限总数至多 16，只改变常数。每一 \(m_R\) 均由
\(C_\phi\sqrt X/L\) 上界；low 更有 \(m_L\ll X^{1/4}/L\)。
这里不需要先证明 \(m_L\le m_H\) 的精确次序。
同样的证明覆盖 physical 四词：其 tuple normalized coefficient
的模由 \(\prod b_{p_j}\) 控制，额外 \(K_d^0\) 与空间 overlap 均至多一。
即使某个其他 physical word 有 alias，(20) 也不需要其无 alias 前件。

## 6. 原 whole-P 桥、same-prime 中心和同一合法 good point

新概率平均被原 box 平均统一支配：
\[
 \langle F\rangle_\chi\le8\langle F\rangle_{\rm box}
 \quad(F\ge0).                                   \tag{21}
\]
所以 472 已付的 raw leakage 二矩与全部 16 个 whole ordered H/L
四词的 mean absolute P error 仍为 \(O(L^{-2})\)。
此处引用的是整个 word 的误差；没有把该误差任意拆给 near 的单个标签。

例如，令 \(\epsilon_w(\sigma)\) 为原 physical/actual whole-word 差，
一次 weighted Markov 便得到
\[
 \mu_\chi(G_T)\ge1-O(L^{-1}),\qquad
 \sup_{\sigma\in G_T}\sum_w|\epsilon_w(\sigma)|\le L^{-1}.
 \tag{22}
\]
uniform weighted HH centering、456 repeated union、half/full factor2
均对每个合法 \(\sigma\) 成立，故不因换正密度而改变。
特别地，仍有 growth-uniform 的 whole 平均
\[
 \langle|q_\sigma-2r_\sigma|\rangle_\chi=o(1),\qquad
 \langle|D_\sigma-(2r_\sigma-S_\psi)|\rangle_\chi=o(1).
 \tag{23}
\]
这些结论没有以未知 \(q\) 或 high fourth boundedness 作前件。
原 same-prime 项的 \(S=0\) 没有被光滑平均消掉；中心 \(D_+\) 仍是 (3)。

用 \(|S|<\Delta_T\) 定义相应的 signed near contribution
\(\mathcal R_{\rm near}\)。它本身未被称为非负 norm。
(15) 准确给
\[
 \langle r_\sigma\rangle_\chi
       =\langle\mathcal R_{\rm near}\rangle_\chi
          +O(X^{-2}L^{-4}).                        \tag{24}
\]
若未来支付 near upper \(B_T\)，则原非负 r 与 (22) 才允许选择
同一个 \(\sigma_T\in G_T\)，得到
\[
 q_{\sigma_T}\le
 \frac{2(B_T+O(X^{-2}L^{-4}))}{\mu_\chi(G_T)}+o(1).
 \tag{25}
\]
当 \(B_T\) 可能增长时必须保留该分母；这里没有付款任何 \(B_T\)。
选择点始终在 \([T,T+s]\)，因此与 228 的移动零点块合同相容。
不需要把这个 density 的 support 宣称为全区间 Lebesgue measure \(1-o(1)\)。

## 7. 剩余近共振的真实算术长度

对于 half-ratio 中的 four-distinct 标签，
\[
 S=\log\frac{qp'}{pq'},\qquad
 A=qp',\ B=pq',\quad X<A,B\le X^2.
\]
由于 \(\Delta_T\to0\)，\(|S|<\Delta_T\) 只推出
\[
 0<|A-B|\le2\Delta_T\max(A,B)
 \le2048XL^{5/2}.                                 \tag{26}
\]
所以目前已付的 far 确实把整个四全异问题压到 near-natural
determinant 宽度 \(O(XL^{5/2})\)，但 product 长度仍然是 \(X^2\)，
phase \(e^{iTS}\)、\(K_d^0(S)\)、\(\Gamma_\chi(sS)\) 和同-u profiles
在这个完整 near 带中全部保留。没有获得长度 X 的免费 mean value。
actual 四全异 near 同样由 (20) 保留，原 internal P 没有丢失。

特别地，此选择不能消去 \(|S|=c/X\) 的真正自然 near：
\[
 sS=2\pi c/\sqrt L\longrightarrow0,\qquad
 \Gamma_\chi(sS)\longrightarrow1.
 \tag{27}
\]
这个明确计算阻止把 (15) 称为 complete signed cancellation、
新的 \(O(1)\) ratio upper 或新的负四全异常数。
仍须使用特殊 prime-product arithmetic 对 (26) 的所有近标签
保留共同相位证明净上界；近带逐 tuple absolute counting 不够。

## 8. 旧路线查重和本次完成范围

实读/定位旧 226、228、239、240、472：
226 的对应付款是零频 Archimedean background；
228 支付移动起点的零点块传递，不含四素数 far union；
239 §4 删除的是各 shell 的 common constant-density 项，
240 是实际 Möbius/divisor pullback 与 adjacent-block 接口；
472 的新增付款是 whole-P mean absolute error 与 ratio 双向桥，
其 §4 明确仍留下 short-window ratio upper。
这些冻结结论没有提供 (10)–(15)、(18)–(20) 的合法短载体全标签 far 证书。
本稿没有把旧 common-density shell cancellation 重新命名为新成果。

本次的新实际付款是：
固定正光滑载体的明确构造及衰减；原同-u half-ratio 的无 alias 证明；
完整 prime 范围及所有标签的 far \(o(1)\)；
直接 actual tuple phase 证明，保留全部 internal P；
以及原同一合法载体 good-point 合同的无增长前件继承。
原完整 near upper、实际新比例、无零区域与 RH 均未完成。

