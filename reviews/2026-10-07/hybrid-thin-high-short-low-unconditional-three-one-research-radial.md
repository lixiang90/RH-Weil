# 原 thin-high / short-low entire31 的无条件原载波简证

2026-10-08。作者 radial_review。新完整推导，待另一作者全文独审。
不修改冻结来源、notes、三篇论文、math、旧 output 或 Git。
本稿保留原 coefficients、window、全部高度和 finite P：
\[
 \boxed{\operatorname{Tr}(C_t^3C_s)=o(d)}
 \tag{1}
\]
在下述固定 caps 下不需要 [R]、canonical prime cancellation、
good-height 截断或 unknown high fourth bounded。
这是一整个原 signed capped31 子块，不是整个 high/low 范围的31。

## 1. 原对象与固定范围

记 \(X=T/(2\pi),\ell=\log X,d=\lfloor X\ell\rfloor\)、
\(I=[-\ell/2,\ell/2]\)，
\[
 Ee_k=\ell^{-1/2}1_Ie^{i\tau_ku},\quad
 \tau_k=T+2\pi k/\ell,\quad 0\le k<d,\quad P=EE^*,\ Q=1-P.
 \tag{2}
\]
原 fixed-profile even C2 taper \(\phi\) 零延拓到实线；
其 sup、\(\|\phi'\|_1+\|\phi''\|_1\) 一致有界，
\(a_\ell=\|\phi\|_2^2/\ell\) 有固定正下界。
原 shifts 为 \(R_sf(u)=f(u+s)\)。置
\[
 b_p=\frac{\log p}{a_\ell\ell\sqrt p},\quad
 B_R^\epsilon=-\sum_{p\in R}b_pM_\phi R_{\epsilon\log p}M_\phi,\quad
 C_R^\epsilon=E^*B_R^\epsilon E,\quad C_R=C_R^++C_R^- .
 \tag{3}
\]
所以 \((B_R^\epsilon)^*=B_R^{-\epsilon}\)；单向 factor 通常非自伴。
本稿只取
\[
 R_t=(X^{1/2},X^{11/20}]\cap\mathbb P,\qquad
 R_s=[2,X^{1/3}]\cap\mathbb P.
 \tag{4}
\]
Chebyshev 与正 partial summation 给
\[
 m_R:=\sum_{p\in R}b_p,\qquad
 \|B_R^\epsilon\|\ll m_R,\quad
 m_t\ll X^{11/40}/\ell,\quad m_s\ll X^{1/6}/\ell .
 \tag{5}
\]
这些是全高度 absolute bounds，不调用无零区。
以下符号展开始终包含全部 genuine-prime 标签与重复标签。

两份既有同对象来源供比较，但本稿逐式重证所需 raw bridge：

| 冻结来源 | canonical LF SHA-256 |
| --- | --- |
| [nonalternating gate](hybrid-three-high-one-low-nonalternating-gate-research.md) | ce1e000572fc2eecb0fe99211c3120ac0b901fb42dd973064b8b041adc3174bd |
| [原 capped31 的 stronger [R] bound](hybrid-thin-high-short-low-entire-three-one-research.md) | c720b48c6e481d3c1b2f67ec36f8dd26b541e2f006eddd9022307fe9474a7128 |

## 2. 原单向 translation 的双方 raw leakage

对任意原 step \(s=\epsilon\log p\)，写
\(g_s(u)=\phi(u)\phi(u+s)\)，是支撑于 I 的 C2 函数。
产品求导给
\(\|g_s\|_\infty+\|g_s'\|_1+\|g_s''\|_1\le C\)，uniform 于所有真实 s。
交叉导数项可用 \(\|\phi'\|_\infty\|\phi'\|_1\)；
\(\|\phi'\|_\infty\le\|\phi''\|_1\)，来自真实 compact C2 零延拓。
因此不因 step 接近窗口端点损失 derivative 界。

I 上完整原 Fourier basis 取同一 \(\tau_j=T+2\pi j/\ell,\ j\in\mathbb Z\)。
定义
\[
 c_n(g_s)=\ell^{-1}\int_I g_s(u)e^{-2\pi inu/\ell}\,du.
 \tag{6}
\]
两次 integration by parts 均无边界项，故
\[
 |c_n(g_s)|\le C\min(1,|n|^{-1},\ell|n|^{-2}),\quad n\ne0.
 \tag{7}
\]
准确矩阵核为
\[
 (B_p^\epsilon)_{jk}
 =-b_pe^{i\tau_ks}\,c_{j-k}(g_s).
 \tag{8}
\]
输出因左端 \(\phi\) 支撑于 I，所以 Q 只需计算
\(j\notin[0,d-1]\)，没有漏掉 \(I^c\) 分量。
固定差 n 的 outside pairs 数量恰为 \(\min(d,|n|)\)，从而
\[
 \|QB_p^\epsilon E\|_2^2
 =b_p^2\sum_{n\ne0}\min(d,|n|)|c_n(g_s)|^2
 \le Cb_p^2\log(2+\ell).
 \tag{9}
\]
最后一步在 \(|n|\le\ell\) 用 harmonic sum，
在 \(|n|>\ell\) 用 \(\ell^2\sum n^{-3}=O(1)\)。
伴随为反向 step，(7)–(9) 完全同样成立。
Minkowski 对实际 prime sum 给，记 \(\ell_0=\log(2+\ell)\)，
\[
 \boxed{\lambda_R:=\|QB_R^\epsilon P\|_2\ll m_R\sqrt{\ell_0},
 \qquad
 \lambda_R^*:=\|Q(B_R^\epsilon)^*P\|_2\ll m_R\sqrt{\ell_0}.}
 \tag{10}
\]
左右 crossing 各用正确方向；没有套用只适用于 selfadjoint 的恒等式。

## 3. 非自伴四词：准确六项 two-crossing

令 \(V_i\) 任意 bounded operators，
\(y_i=\|V_i\|,\lambda_i=\|QV_iP\|_2,\lambda_i^*=\|QV_i^*P\|_2\)。
P 有限 rank，全部 trace 定义合法。逐个插入三个内部 P，差准确为
\[
 \begin{aligned}
 \mathfrak D={}&\operatorname{Tr}(PV_1QV_2V_3V_4P)\\
 &+\operatorname{Tr}(PV_1PV_2QV_3V_4P)
 +\operatorname{Tr}(PV_1PV_2PV_3QV_4P).
 \end{aligned}
 \tag{11}
\]
右侧递归插入 \(P+Q\) 给
\[
 \|QV_2V_3V_4P\|_2
 \le\lambda_2y_3y_4+y_2\lambda_3y_4+y_2y_3\lambda_4,
 \quad
 \|QV_3V_4P\|_2\le\lambda_3y_4+y_3\lambda_4.
 \tag{12}
\]
左 factors 的 HS norms 分别至多
\(\lambda_1^*,y_1\lambda_2^*,y_1y_2\lambda_3^*\)。
HS–HS 配对因此给准确六项上界
\[
 |\mathfrak D|
 \le\sum_{1\le i<j\le4}\lambda_i^*\lambda_j
                      \prod_{k\ne i,j}y_k .
 \tag{13}
\]
应用 (5)、(10)，对三个 thin-high 与一个 short-low 的每个方向，
\[
 \frac{|\mathfrak D|}{d}
 \ll \frac{\ell_0 m_t^3m_s}{d}
 \ll X^{-1/120}\ell^{-5}\ell_0=o(1).
 \tag{14}
\]
这里 \(3(11/40)+1/6=119/120<1\)，
或 cap 总和 \(3(11/20)+1/3=119/60<2\)。
这是直接 raw finite/physical 比较，不更换 P 或高度观测。

## 4. 全16种物理 signs 与准确 netgap

先在实际有限词中将 low 放在末位。
对 high labels \(p,q,r\in R_t\)、low \(h\in R_s\)，
\(s_i=\epsilon_i\log p_i,\ S_j=\sum_{i\le j}s_i,\ S=S_4\)。
若 \(\epsilon_1=\epsilon_2\) 或 \(\epsilon_2=\epsilon_3\)，
相邻两个同向 high steps 的和严格超过 \(\ell\)。
原 interval 三个位置不可能同时在 I 内，相关 physical operator product 准确为0。
16个 signatures 中十二个属于这类，不取正 majorant 去代替零。

余下四个 high signatures 为 \((+,-,+,\pm)\)、\((-,+,-,\pm)\)。
对前一 high 方向，
\[
 \begin{array}{ll}
 \epsilon_4=-1:&7\ell/60<S<3\ell/5-\log2,\\
 \epsilon_4=+1:&9\ell/20+\log2<S<14\ell/15.
 \end{array}
 \tag{15}
\]
反转全部 signs 给另外两条负区间。因此每个原 tuple 准确满足
\[
 7/60<|S|/\ell<14/15.
 \tag{16}
\]
这在应用任何 cancellation 前成立；内部路径窗还保留全部其他支持限制。

原 physical normalized trace 的准确形式为
\[
 \left(\prod_i b_{p_i}\right)K_d(S)\,\ell^{-1}
 \int\phi(u)\phi(u+S)\prod_{j=1}^3\phi(u+S_j)^2\,du,
 \tag{17}
\]
\[
 K_d(S)=\frac{e^{i[T+(2d-1)\pi/\ell]S}-e^{i[T-\pi/\ell]S}}
                   {2id\sin(\pi S/\ell)} .
 \tag{18}
\]
四个负号的乘积为正。由 (16)，\(|\sin(\pi S/\ell)|\ge c>0\)，
故 \(|K_d(S)|\le C/d\)，含原 floor d 与所有原 finite heights。
normalized 窗口积分的绝对值 uniformly bounded。
对所有 tuple 作真实 positive coefficient mass upper，只在这里舍去 oscillation，
得到每个剩余 physical signature
\[
 \frac{|\operatorname{Tr}(E^*B_t^{\epsilon_1}B_t^{\epsilon_2}
                                  B_t^{\epsilon_3}B_s^{\epsilon_4}E)|}{d}
 \ll \frac{m_t^3m_s}{d}
 \ll X^{-1/120}\ell^{-5}=o(1).
 \tag{19}
\]
没有 near、\(\pm\ell\) alias 或其他未付 height dyad，因为 (16)已有固定间隔；
也没有 canonical phase 分离、[R] 或 Fourier ghost 替换。

## 5. 回到整个 capped31 与准确剩余范围

将十二个 physical 零项、四个 (19)和每一项的原 P bridge (14)相加，
\[
 \boxed{\frac{|\operatorname{Tr}(C_t^3C_s)|}{d}
 \ll X^{-1/120}\ell^{-5}\log(2+\ell)=o(1).}
 \tag{20}
\]
全部16种符号、重复与 distinct labels、原 normalizer、finite carrier 与内部 P
同时在 (20)内。其他 low placements只在 actual finite trace 中循环，
不对带末端 P 的物理 trace免费循环。

先固定原 profile、(4)的 caps及所有常数，然后 \(T\to\infty\)。
本稿只用原 Chebyshev–Mertens / taper / exact finite algebra，不需要无零输入。
既有 [R] 版本的 \(X^{-739/3000}\ell^4\) 是另一个更强幂界；
本稿无需它即可付款同一 capped31 观测量。
high 的 \((X^{11/20},X]\)、low 的 \((X^{1/3},X^{1/2}]\) 仍在 whole31；
没有支付完整 high4、22、467 的实际 q/k 前件或新比例。
扩 caps 后 (14)的 raw mass 节省或 (16)的 netgap 可消失，必须重新证明。
