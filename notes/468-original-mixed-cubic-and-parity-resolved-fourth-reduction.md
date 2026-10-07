# 468：原路线的混合三次项与奇偶残差约束

2026-10-08。回到原 Eisenstein / AF 路线，保持原素数系数、采样窗口、
有限投影和显式公式。本次完成三个具体接口：背景中所有含低素数的
三次项、一个完整截短31子块、以及平方残差的奇偶必要约束。
完整高素数第四矩仍未支付，尚无新的实际零点比例或无零边界。

完整推导保存在：

- [背景混合三次项](../reviews/2026-10-07/hybrid-background-entire-mixed-cubic-research-compression.md)；
- [实际背景的相对恢复](../reviews/2026-10-07/hybrid-background-cubic-relative-actual-recovery-research-compression.md)；
- [非交替31分区](../reviews/2026-10-07/hybrid-three-high-one-low-nonalternating-gate-research.md)及[完整截短31](../reviews/2026-10-07/hybrid-thin-high-short-low-entire-three-one-research.md)；
- [完整截短31的无条件简证](../reviews/2026-10-07/hybrid-thin-high-short-low-unconditional-three-one-research-radial.md)；
- [奇偶残差必要约束](../reviews/2026-10-07/hybrid-parity-resolved-residual-necessary-constraints-radial.md)。

## 1. 同一个原有限矩阵

记 \(\ell=\log X,\ X=T/(2\pi),\ d=\lfloor X\ell\rfloor\)，
\(I=[-\ell/2,\ell/2]\)，原等距嵌入为
\[
 Ee_k=\ell^{-1/2}1_Ie^{i\tau_ku},\qquad
 \tau_k=T+2\pi k/\ell,\quad 0\le k<d,\quad P=EE^*.
 \tag{1}
\]
原偶 C² 窗为 \(\phi\)，\(a_\ell=\|\phi\|_2^2/\ell\)。
genuine-prime high/low 通道分别使用
\[
 b_p=\frac{\log p}{a_\ell\ell\sqrt p},\qquad
 B_R=-\sum_{p\in R}b_pM_\phi
        (R_{\log p}+R_{-\log p})M_\phi,\qquad C_R=E^*B_RE.
 \tag{2}
\]
每次平移按实线零延拓。以下 \(H=C_{(\sqrt X,X]}\)，
\(L=C_{[2,\sqrt X]}\)；字母 \(L\) 指低素数矩阵，日志长度写作 \(\ell\)。
原完整通道 \(C_\Lambda\) 还包含 proper powers。
原显式公式矩阵 \(\mathcal M\) 满足
\(\mathcal M-I=A+C_\Lambda\)，\(A\) 是实际 Gamma/pole 背景。

涉及 [R] 的结论只引用
[446](446-uniform-prime-twists-on-the-original-gabor-frame.md)
明列的 fixed-gap zero-free/logarithmic-control 输入，不重新认证外部证明。

## 2. 实际背景中含 low 的全部三次项

令 \(A_0=E^*M_{h_\ell}E\)，
\(h_\ell=\phi^2/a_\ell-1\)。[454](454-original-background-and-weighted-prime-mixed-traces.md)
已付 \(A=A_0+R_T,\ \|R_T\|_{\mathrm op}=O(1/\ell)\)。
本次不以未知 high fourth 为前件，得到
\[
 \begin{aligned}
 &\operatorname{Tr}(A_0L^3)=o(d),\\
 &\max\{|\operatorname{Tr}(A_0HL^2)|,
        |\operatorname{Tr}(A_0LHL)|,
        |\operatorname{Tr}(A_0L^2H)|\}=o(d),\\
 &\max\{|\operatorname{Tr}(A_0H^2L)|,
        |\operatorname{Tr}(A_0HLH)|,
        |\operatorname{Tr}(A_0LH^2)|\}=o(d).
 \end{aligned}
 \tag{3}
\]
这里每一项分别是 \(o(d)\)。前两类无需 [R]；第三类需固定
\(\theta<a<9/10\)，原 \(\theta=7/8\) 可取 \(a=89/100\)。

近核把 semiprime 与 prime 按真实整数产品联合分组，
保留全部八种方向、重复标签和每个 placement。远核先分离共同路径窗，
再应用原 sharp prefix；二高一低的主幂为
\[
 X^{(5/2)a-9/4}\operatorname{polylog}X=o(1).
 \tag{4}
\]
接近 \(S=\pm\ell\) 的位置由原 endpoint overlap与正素数乘积质量
单独支付。实际有限矩阵与物理词之间通过 good-height 两次 crossing
比较，三个内部 \(P\) 全保留；低高度 principal 峰由原 C² 尾恢复。

## 3. 非平窗口的背景附加费用可条件移除

另外明确增加前件
\[
       \limsup\operatorname{Tr}H^4/d<\infty.
 \tag{5}
\]
既有 [high cubic 相对界](../reviews/2026-10-07/hybrid-parity-weighted-high-cubic-research.md)
此时给 \(\operatorname{Tr}A_0H^3=o(d)\)。
结合 (3)、entire low4 与 Schatten Minkowski，prime 通道第四矩有界。
这之后才可用 \(\|R_T\|_{\mathrm op}=O(1/\ell)\) 恢复实际背景，
并用 [455](455-whole-proper-power-fourth-norm-and-prime-equivalence.md) 恢复全部 proper powers，
严格得到
\[
                \operatorname{Tr}(A C_\Lambda^3)/d\longrightarrow0.
 \tag{6}
\]
于是 454 的实际中心四迹在该前件下改进为
\[
 \frac{\operatorname{Tr}(\mathcal M-I)^4}{N}
 =\frac{\operatorname{Tr}C_\Lambda^4}{N}
       +6Z_\psi-J_\psi+V_\psi+o(1),\qquad N=N(T,2T)\sim d.
 \tag{7}
\]
非平窗口不再需要此前 Cauchy 上界产生的
\(4\sqrt{Z_\psi F}\) 附加费用。没有额外 high fourth 控制时不能直接使用 (6)–(7)；
本次没有独立证明 (5)，也未把这条条件桥写成实际比例改进。

进一步用已付 prime 二矩恢复 \(R_T\)，并逐项
支付全部七个非交换 proper-power cubic，得到无有界 fourth 前件的
相对预算：
\[
 \boxed{\left|\frac{\operatorname{Tr}(A C_\Lambda^3)}d\right|
       \ll\frac{\sqrt{a_T}+1}{\ell}+o(1),
       \qquad a_T=\operatorname{Tr}H^4/d.}
 \tag{7a}
\]
因此更弱的 \(a_T=o(\ell^2)\) 已足以使 (6) 成立，并得到 (7)
的渐近等式；用于比例改进的常数第四矩预算仍需另行取得。

## 4. 一个整个有符号的实际31子块

保持同一个 \(E,\phi,P,b_p\)，只把原标签按两个固定 sharp 范围分组：
\[
 R_t=(X^{1/2},X^{11/20}]\cap\mathbb P,\qquad
 R_s=[2,X^{1/3}]\cap\mathbb P,\qquad C_t=C_{R_t},\ C_s=C_{R_s}.
 \tag{8}
\]
本次证明，无需 [R] 或未知 high fourth 有界，
\[
                \boxed{\operatorname{Tr}(C_t^3C_s)=o(d).}
 \tag{9}
\]
包括全部16种符号、重复与不同素数、所有内部 \(P\)、原 carrier 和高度。
十二种物理方向有相邻同向 high 步，准确为空；
剩下四种的每一个 tuple 都有
\(7/60<|S|/\ell<14/15\)，与近核和采样周期保持固定间隔。
直接使用原全高度系数质量及复数算子的双方 crossing 给
\[
 \frac{|\operatorname{Tr}(C_t^3C_s)|}{d}
 \ll X^{-1/120}\ell^{-5}\log(2+\ell)=o(1).
 \tag{10}
\]
这里 \(m_t^3m_s\ll X^{119/120}/\ell^4\)，实际投影误差只有
\(O(\log(2+\ell)m_t^3m_s)\)。原 [R] \(\theta=7/8\) 下另可取
\(a=22/25\)，通过共同 Fourier 分离得到更强的
\(O(X^{-739/3000}\ell^4)\) 主幂及两个严格小尾；
它是额外定量加强，(9) 的小量结论不需要该输入。
原更大的 high 或 low 范围仍留在 whole31 中，未由 (9) 支付。
在同一 [R] 合同下，另一个较大的已付分区是：low≤\(\sqrt X\)，三个 high 中至多一个
超过 \(X^{11/20}\) 时，十二种非交替方向实际合计为 \(o(d)\)；
该分区仍留下四种交替方向。

## 5. flat 情形的奇偶残差必要约束

以下常数只取 flat profile。沿用
[465](465-centered-high-square-joint-fourth-budget.md)至
[467](467-two-residual-schur-and-commutator-budget.md)：
\[
 \Gamma=H^2-W,\quad\Delta=L^2-V,\quad
 q_T=\|\Gamma\|_{\mathrm{HS}}^2/d,\quad
 c_T=\operatorname{Tr}H^2L^2/d.
 \tag{11}
\]
原 \(J=M_{\operatorname{sgn}u}\)，
\(U=\operatorname{sgn}(E^*JE)\)，零特征值处取 \(+1\)。
对任意矩阵定义
\(\mathcal E_U B=(B+UBU)/2,\ \mathcal O_U B=(B-UBU)/2\)，
并令 \(r_T=\|\mathcal O_U\Gamma\|_{\mathrm{HS}}^2/d\)。

在明确的有界 \(q_T\) 前件下，新证明给
\[
 \boxed{\liminf(q_T-r_T)\ge\underline q=\frac{41}{15120}.}
 \tag{12}
\]
证明先把 \(H\) 固定截断到 \([-R,R]\)，保留 PSD 平方尾；
先 \(T\to\infty\)，再 \(R\to\infty\)。它没有把二范数 high parity
直接升级成平方残差的 parity。
整个低素数平方通过所有 \(P\) 及 sharp \(J\) 准入，另给
\[
 \frac{\|\mathcal O_U\Delta\|_{\mathrm{HS}}^2}{d}\to\frac{13}{480},
 \qquad
 \frac{\|\mathcal E_U\Delta\|_{\mathrm{HS}}^2}{d}\to\frac{11}{480}.
 \tag{13}
\]
因此每个有界共同极限 \((q_T,r_T,c_T)\to(q,r,c)\) 必须满足
\[
 0\le r\le q-\underline q,\qquad
 \left|c-\frac{23}{960}\right|
 \le\sqrt{(q-r)\frac{11}{480}}+\sqrt{r\frac{13}{480}}.
 \tag{14}
\]
若未来证明 467 尚未支付的 \(q_T\le1/350+o(1)\)，则进一步必须有
\[
 \limsup r_T\le\frac{11}{75600},\qquad
 \limsup\left|c_T-\frac{23}{960}\right|<\frac1{100}.
 \tag{15}
\]
这收紧该候选的必要区间；没有排除或实现候选，
也没有证明另一项算术前件 \(\liminf\|[H,L]\|_{\mathrm{HS}}^2/d\ge1/40\)。

## 6. 剩余工作与交付范围

真正的剩余任务仍是同对象的完整 signed high fourth，以及更大标签范围
的31、22联合预算。上述实际小块不能与重复标签常数相加成完整四矩。
本次 (6) 减少了获得有界第四矩后非平窗口的背景恢复费用，
(14) 则提供应当保留的实际方差分配约束。

新结果相对于已明列 [R] 输入；既有
\(\sigma_*\approx0.874957019420099\) 与实际已验证零点比例均未改变。
没有确认新全边界，因此不触发另写正式边界论文的交付条件。
