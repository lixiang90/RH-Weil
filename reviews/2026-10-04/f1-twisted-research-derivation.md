# 扭曲相对读出的独立推导：实际有限源与非零混合标签

2026-10-04。独立推导草稿；数学结论的范围以各命题的前提为准。
依赖 [419](../../notes/419-f1-original-time-crossed-product-and-trace-interface.md)、
[420](../../notes/420-f1-source-hardy-index-and-dual-action.md)、
[421](../../notes/421-f1-weighted-hardy-trace-and-atomic-obstruction.md)、
[422](../../notes/422-f1-radial-finite-part-and-corner-anomaly.md)。
这里没有证明算术主关系消失、完整 Weil 比较或 RH。

## 1. 插入、循环方向和统一反例

沿用 422 的实际 Fréchet 代数 \(\mathcal A\)、开放理想 \(\mathcal I\)、
径向乘子 \(z_g\)、平移 \(\beta_g\) 与非循环有限部 \(\tau\)。对固定
\(\gamma\in\mathbb Z^2\)，置
\[
 W=z_{-\gamma}\otimes1,\qquad \sigma=\operatorname{Ad}W,
 \qquad \tau_\gamma(F)=\tau(FW)=\operatorname{Tr}_t\lambda_{pq}(F_\gamma).
\]
这是连续泛函；\(W\) 保持 \(\mathcal A\) 及 \(\mathcal I\)，
且 \(F\in\mathcal I\) 时 \(\tau_\gamma(F)=\operatorname{Tr}(FW)\)。
插入普通迹可由 422 的迹范数绝对收敛矩阵单位展开证明。

定义
\[
 D_\gamma(A,B)=\tau_\gamma(AB-B\sigma(A))
              =\tau([A,BW]).                                    \tag{1}
\]
这里可以允许 \(A\) 为已验证的连续有界乘子，\(B\in\mathcal A\)。
对单项 \(A=fz_g\)、\(B=vz_h\)，只有 \(g+h=\gamma\) 时非零。
置 \(k=\operatorname{Tr}_t(f\beta_gv)\)，\(g=(a,b)\)，则
\[
 D_\gamma(A,B)=-ae_p(k)-be_q(k)-abk_c.                           \tag{2}
\]
证明是在 (1) 中将 \(B W\) 的群标签写为 \(-g\)，直接使用 422 式 (14)；
因此不能另行选择角点符号。

同时必须保留
\[
 \Delta_\gamma\tau_\gamma(F):=
 \tau_\gamma(\sigma(F))-\tau_\gamma(F)
 =\gamma_1\operatorname{Tr}_t e_p(F_\gamma)
  +\gamma_2\operatorname{Tr}_t e_q(F_\gamma)
  +\gamma_1\gamma_2\operatorname{Tr}_t(F_\gamma)_c.                \tag{3}
\]
这是 422 的 \(\beta_{-\gamma}\) 平移律，而非可忽略的余项。
例如 \(F=H(j)\delta_{k0}z_\gamma\otimes P\)，其中 \(P\) 为时间秩一投影，
式 (3) 等于 \(\gamma_1\)；交换两个坐标可见 \(\gamma_2\)。
故每个 \(\gamma\ne0\) 都有不变性失败的实际见证。

由定义直接展开的准确恒等式是
\[
 D_\gamma(AB,C)-D_\gamma(A,BC)-D_\gamma(B,C\sigma(A))=0.          \tag{4}
\]
另有
\[
 D_\gamma(A,B)+D_\gamma(B,\sigma(A))
 =\tau_\gamma(AB)-\tau_\gamma(\sigma(AB)).                       \tag{5}
\]
因此 (4) 不能代替扭曲循环性。

标准“末因子移到首位”约定应取 \(\alpha=\sigma^{-1}\)。真正的标准
Hochschild 余边界为
\[
 E_\gamma(A,B):=(b_\alpha\tau_\gamma)(A,B)
 =\tau_\gamma(AB-\sigma^{-1}(B)A)
 =D_\gamma(A,B)
  +\Delta_\gamma\tau_\gamma(\sigma^{-1}(B)A).                   \tag{6}
\]
于是 \(b_\alpha E_\gamma=0\) 是结合律恒等式，但仍不能省略循环及不变性条件。
若直接将 \(D_\gamma\) 代入标准 \(b_\alpha\)，结果为
\[
 (b_\alpha D_\gamma)(A,B,C)
 =\tau_\gamma(\sigma^{-1}(C)AB-C\sigma(A)\sigma(B)),             \tag{7}
\]
一般不为零。原文约定见 Rennie–Sitarz–Yamashita 作者稿 Definition 2.1，
[PDF 第 2 页](https://rennieillawarramath.com/website-pdfs/JournalArticles/2013RSY-Prepub.pdf)。
此处公式均由展开直接核验；没有引用一般理论来宣布新余圈成立。

还有一个对所有 \(\gamma\) 同时成立的较强停止见证。令
\(e=(1,0)\)、\(s(j,k)=H(j)\delta_{k0}\)，取
\[
 A=sz_e\otimes P,\qquad B=sz_{\gamma-e}\otimes P.
\]
两者属于 \(\mathcal A\)，且
\[
 (AB-B\sigma(A))W=[A,BW]
 =\bigl(H(j-1)-H(j)\bigr)\delta_{k0}\otimes P
 =-\delta_{(0,0)}\otimes P.                                   \tag{8}
\]
故 \(D_\gamma(A,B)=-1\)。其原缺陷 \(AB-B\sigma(A)\) 本身属于 \(\mathcal I\)。
因而不存在同时匹配开放理想插入普通迹、并在完整 \(\mathcal A\) 上满足
\(\rho(AB)=\rho(B\sigma(A))\) 的标量泛函 \(\rho\)。
这不排除携带边界数据的相对对象。

## 2. 原源固定，原提升仍有边界条带

保持原系数
\[
 f_{(n,0)}(t)=-c(t)c(t-nL),\qquad
 f_{(n,1)}(t)=c(t)c(t-nL-M),
\]
其他 \(f_g=0\)，并令有限集 \(F\) 包含所有非零系数标签及 \(0\)。
原平方分割为 \(\sum_n c(t-nL)^2=1\)。置
\[
 b_g(t)=\delta_{g0}+f_g(t),\quad
 q_g(j,k)=H(j-\max(0,g_1))H(k-\max(0,g_2)),\quad Q=q_0.
\]
于是
\[
 u=1+\sum_{g\in F}z_g\otimes M_{f_g}\mathsf T_{\ell_g},\qquad
 T=1+\sum_{g\in F}q_gz_g\otimes M_{f_g}\mathsf T_{\ell_g}.
\]
\(\sigma(u)=u\)，因为其径向系数恒为 1。相反
\[
 \sigma(T)-T=\sum_g(\beta_{-\gamma}q_g-q_g)z_g
                    \otimes M_{f_g}\mathsf T_{\ell_g}.          \tag{9}
\]
每个差在双无穷角点为零，但不必在两条边界同时为零。
对 \(\gamma\ne0\)，零群系数含
\((\beta_{-\gamma}Q-Q)\otimes M_{-c^2}\)，其某条边界非零，故 (9)
不是开放径向理想中的修正。实际 \(T\) 未满足通常要求的固定提升条件。
下节求得的是合法乘子域上的实际数值，尚未登记为扭曲循环 K 理论配对。

## 3. 原 \(T^*\)、\(TK_h\) 的全部标签公式

取实 \(d\in C_c^\infty(\mathbb R)\)、\(h\in C_c^\infty(\mathbb R)\)，
\[
 K_h=Q\otimes M_dU(h)M_d\in\mathcal A.
\]
422 的连续乘子准入证明所有下述乘积合法。
对 \(g\ne0\)，
\[
 (T^*)_g=q_g\otimes
 M_{\overline{f_{-g}(t-\ell_g)}}\mathsf T_{\ell_g},\qquad
 (TK_h)_s=q_s\otimes M_{b_s}\mathsf T_{\ell_s}M_dU(h)M_d.
\]
第二式对 \(s=0\) 也成立，完整保留 \(TK_h\) 的独立单位贡献。
\((T^*)_0=1+Q\otimes M_{\overline{f_0}}\) 也保留；它在 (2) 中因 \(g=0\)
不贡献交换异常，而不是因删掉了单位元。

固定 \(\gamma\)，写 \(s=\gamma-g\) 及
\[
 r_i=\max(0,g_i,\gamma_i),\qquad
 C_\gamma(g)=g_1r_2+g_2r_1-g_1g_2,                             \tag{10}
\]
\[
 J_\gamma(g)=\int_{\mathbb R}
 \overline{f_{-g}(x)}b_{\gamma-g}(x)
 d(x-\ell_{\gamma-g})d(x+\ell_g)\,dx.                          \tag{11}
\]
准确公式是
\[
 \boxed{D_\gamma(T^*,TK_h)
       =h(-\ell_\gamma)\sum_{g\ne0}C_\gamma(g)J_\gamma(g).}      \tag{12}
\]
和实际有限；其可能非零的标签包含在 \(F-F\) 中。

证明：径向乘积为
\[
 q_g\beta_gq_{\gamma-g}=H(j-r_1)H(k-r_2).
\]
此函数的两边有限部是 \(-r_2,-r_1\)，角点为 1，故 (2) 给 (10)。
时间算子为
\[
 M_{\overline{f_{-g}(t-\ell_g)}b_{\gamma-g}(t-\ell_g)}
 \mathsf T_{\ell_\gamma}M_dU(h)M_d.
\]
核的对角值是 \(h(-\ell_\gamma)\) 乘相应紧支乘法系数；
令 \(x=t-\ell_g\) 得 (11)。求迹可按 422 的 Fourier 秩一积分核验，
不需要循环两个非迹类因子，也不预设目标周期原子。

式 (12) 是 \(D_\gamma\) 的式子，不能原封不动用作 (6) 的标准
\(E_\gamma\) 读出。例如 \(g\ne0\) 时，\(\sigma^{-1}(TK_h)_s(T^*)_g\)
的径向阈值是
\[
 R_i=\max(\gamma_i,\gamma_i+s_i,s_i)
    =\max(\gamma_i,2\gamma_i-g_i,\gamma_i-g_i).
\]
其时间普通迹与第一乘积相同，所以相应 \(E_\gamma\) 权重为
\(r_1r_2-R_1R_2\)。在 \(g=0\) 时，原独立单位项及 \(f_0\) 项还需分别保留，
不能再由“交换标签为零”将它们删除。

## 4. 非零混合标签确实出现，但权重取决于原分割

取 \(\gamma=(a,1)\)。仅 \(g=(-n,0)\) 可贡献；
\(C_\gamma(g)=-n\)，而 \(f_{(n,0)}f_{(n+a,1)}\) 有一个负号。
令 \(y=x-nL\) 及 \(s=\ell_\gamma=aL+M\)，得到
\[
 D_{(a,1)}(T^*,TK_h)=h(-s)\int
 m_c(y)c(y)c(y-s)d(y)d(y-s)\,dy,                               \tag{13}
\]
\[
 m_c(y)=\sum_{n\in\mathbb Z}n\,c(y+nL)^2.
\]
这个整数一阶矩来自实际群标签及平方分割，而不是外加的周期权重。
对每个固定 \(y\) 和紧支积分域，该和只有有限项。

以下给出严格正的非零混合见证。取 421 的近锐分割 \(c_\varepsilon\)，
并让过渡函数 \(\theta\) 在 \((0,1)\) 内严格处于 \((0,1)\)。置
\[
 a=-\lceil M/L\rceil,\qquad s=aL+M\in(-L,0),\qquad r=-s\in(0,L).
\]
不同素数使 \(M/L\notin\mathbb Z\)。取
\(0<\varepsilon<\min(r,L-r)/4\)。在 \(0<y<\varepsilon\) 上，
\[
 c_\varepsilon(y)>0,\quad
 m_{c_\varepsilon}(y)=c_\varepsilon(y+L)^2
 =\cos^2\bigl(\pi\theta(y/\varepsilon)/2\bigr)>0,
\]
而 \(c_\varepsilon(y+r)=1\)。

选非零非负 \(\eta\in C_c^\infty((0,\varepsilon))\)，并置
\(d(t)=\eta(t)+\eta(t-r)\)。两峰分别位于下过渡及其向右平移 \(r\) 的位置。
选择足够窄的 \(\eta\) 支集时，\(d(y)d(y+r)\) 的支集准确位于第一峰，
在那里等于 \(\eta(y)^2\)。故 (13) 中积分严格正。
取 \(h\) 在 \(r\) 附近紧支且 \(h(r)>0\)，即可得到
\[
 D_{(a,1)}(T^*,TK_h)>0.                                      \tag{14}
\]
此周期是 \(r=-aL-M\)。它既不是任何非零整数倍 \(L\)，也不是任何非零整数倍 \(M\)，
否则素数幂唯一分解将迫使不同素数的非零幂相等。
因此可把 \(h\) 支集缩在 \(r\) 附近，避开 414 的全部纯 \(p\)、纯 \(q\) 周期及 0。
原 414 周期分布在该测试上为 0，而 (14) 为正。
这给明确的混合标签不匹配，反驳“所有非零标签均消失”，也反驳此直接读出已等于原周期分布。

该见证使用实际允许的 \(c_\varepsilon,d\)。若取 \(d\) 的支集使
\(d(y)d(y+r)\equiv0\)，同一标签读出变为零；缩放 \(d\) 又使值二次缩放。
故目前没有独立于分割和时间截止的算术权重比较。

## 5. 有限支持与原全群算子的边界

对固定 \(c\)，(12) 只有有限个非零 \(\gamma\)。任何测试无关的有限标签组合
仍只有有限时间支撑，不能与 414 的无限纯素数周期分布作为完整测试空间上的分布相等。
可在一个未进入 \(\ell(F-F)\) 的纯 \(p\) 周期处缩窄测试，给出非零差值。
这不排除更高链、实际无限全群传递或携带新的奇异输入的相对正则化。

原 \(A_N(h)\) 已由 422 证明属于 \(\mathcal I\)。对合法有界乘子 \(B\)，
\[
 D_\gamma(B,A_N(h))=\operatorname{Tr}[B,A_N(h)W]=0.
\]
标准 \(E_\gamma\) 在任一因子属于 \(\mathcal I\) 时也为零：
插入普通迹及 \(W^{-1}BW=\sigma^{-1}(B)\) 给合法迹循环。
所以将原有限壳层截止重新塞进这两个边界异常，并不自动恢复非零全群周期桥。

目前严格获得：插入普通迹的实际定义域；全标签交换异常公式；标准方向修复与循环失败；
原有限源的全部标签时间读出；一个实际严格正的混合周期反例。
尚缺的是固定提升或携带条带异常的合法相对链、所有标签的相容性、原壳层权重比较及主关系消失。

## 6. 标准 Hochschild 修复的完整源公式，含零标签两种单位项

本节继续计算 (6)，不再把 (12) 的结果直接移植过去。
定义 \(m_i=\max(0,\gamma_i)\) 及
\[
 U_\gamma=m_1m_2-(\gamma_1+m_1)(\gamma_2+m_2),
\]
\[
 J^u_\gamma=\int b_\gamma(t)d(t-\ell_\gamma)d(t)\,dt,\qquad
 J^f_\gamma=\int\overline{f_0(t)}b_\gamma(t)
                         d(t-\ell_\gamma)d(t)\,dt.
\]
对于 \(g\ne0\)，仍用 (10) 的 \(r_i\)、(11) 的 \(J_\gamma(g)\)，并置
\(R_i=\max(\gamma_i,2\gamma_i-g_i,\gamma_i-g_i)\)。则
\[
 \boxed{
 E_\gamma(T^*,TK_h)=h(-\ell_\gamma)
 \left[U_\gamma(J^u_\gamma+J^f_\gamma)
      +\sum_{g\ne0}(r_1r_2-R_1R_2)J_\gamma(g)\right].}          \tag{15}
\]

证明：\(\lambda_{pq}(H(j-u)H(k-v))=uv\) 对所有整数 \(u,v\) 成立，
因为两个一维有限部各为 \(-u,-v\)。对于非零 \(g\)，第一乘积阈值为 \(r_i\)，
第二乘积 \(\sigma^{-1}(TK_h)_{\gamma-g}(T^*)_g\) 阈值为 \(R_i\)。
两个时间迹相同，因为其中一个时间因子迹类，另一因子有界。
故给出求和部分；不使用径向有限部的循环性。

对 \(g=0\)，\((T^*)_0=1+Q\otimes M_{\overline{f_0}}\) 必须分成两项。
独立单位项的两个径向阈值分别是 \(m_i\) 与 \(\gamma_i+m_i\)，给 \(U_\gamma\)。
\(Q f_0\) 项的第一乘积是 \(Qq_\gamma=q_\gamma\)。第二乘积必须使用
交叉积法则对右侧 \(Q\) 作 \(\beta_\gamma\) 平移，因此它是
\[
 (\beta_\gamma q_\gamma)(\beta_\gamma Q)
 =\beta_\gamma(q_\gamma Q)=\beta_\gamma q_\gamma.
\]
它的两个阈值也分别是 \(m_i\) 与 \(\gamma_i+m_i\)，给同一个 \(U_\gamma\)。
它们的时间核对角积分准确是 \(J^u_\gamma,J^f_\gamma\)。
两项可合并为
\[
 U_\gamma\int(1-c(t)^2)b_\gamma(t)
                         d(t-\ell_\gamma)d(t)\,dt.
\]
特别地 \(\gamma=0\) 时两种零标签贡献均为零，(15) 回到普通交换异常。

标准修复也有同一个严格正的实际混合见证。
沿 §4 取 \(\gamma=(a,1)\)、\(a=-\lceil M/L\rceil\le-1\)、\(r=-\ell_\gamma\)，
以及下过渡双峰 \(d(t)=\eta(t)+\eta(t-r)\)。此时 \(m_1=0,m_2=1\)，
\(U_\gamma=-2a\)。
在下过渡的时间支撑上，非零群标签只有 \(g=(-1,0)\) 可贡献；
其径向权重是 \(-2a-2\)，时间积分的源乘积为
\(-c_\varepsilon(y+L)^2c_\varepsilon(y)c_\varepsilon(y+r)\eta(y)^2\)。
零标签的两项合为
\(-2a(1-c_\varepsilon(y)^2)c_\varepsilon(y)c_\varepsilon(y+r)\eta(y)^2\)。
利用 \(1-c_\varepsilon(y)^2=c_\varepsilon(y+L)^2\) 与非零群标签相加，得到
\[
 E_{(a,1)}(T^*,TK_h)=2h(r)\int
 c_\varepsilon(y+L)^2c_\varepsilon(y)c_\varepsilon(y+r)
 \eta(y)^2\,dy
 =2D_{(a,1)}(T^*,TK_h)>0\quad\text{若 }h(r)>0.                 \tag{16}
\]
这里使用 \(c_\varepsilon(y)^2+c_\varepsilon(y+L)^2=1\)，且
\(c_\varepsilon(y+r)=1\)。因此准确修复 Hochschild 方向本身也没有消去该混合原子。
原 414 分布在同一离轴测试上仍严格为零。
这排除把裸 (15) 当作原周期分布的直接读出；尚不排除同时补入 (3)、(9)
边／角相对链后的组合机制。

作为修正式 (15) 的另一个直接检验，取平台双峰。
取小区间 \(I\subset(\varepsilon,L-r)\)，让 \(\eta\ge0\) 非零支撑于 \(I\)，
且区间足够窄以使双峰乘积仅在 \(I\) 非零；仍置
\(d(t)=\eta(t)+\eta(t-r)\)。两峰现在都位于 \(c_\varepsilon=1\) 的平台。
在时间积分支撑上，仅 \(n=0\) 的 \(c_\varepsilon(y+nL)\) 非零，
故所有 \(g\ne0\) 项消失，而 \(b_\gamma(y)=1\)。
零标签单位与 \(f_0=-c_\varepsilon^2=-1\) 项完全抵消，故准确得到
\[
 D_{(a,1)}(T^*,TK_h)=0,\qquad
 E_{(a,1)}(T^*,TK_h)=0.                                      \tag{17}
\]
选固定 \(I,\eta\) 后，只要 \(\varepsilon\) 足够小，两种零值对整个近锐族保持。
平台不提供非零混合见证；本报告的严格正混合见证限定为上面的下过渡情形。

## 7. 对 423 的独立对照

已对照 [423 初稿](../../notes/423-f1-twisted-radial-readout-and-mixed-period-obstruction.md)
的 §1–10：插入方向、全部平移符号、统一有限秩见证、\(D_\gamma\) 原源式、
混合正见证及固定 \(N\) 开放理想消失均与本报告独立推导一致。
423 明确没有把 \(D_\gamma\) 源公式直接推广给 \(E_\gamma\)，此限制准确。
本报告 (15)–(17) 为随后的独立计算，须按下述修正记录使用。

## 8. 零标签乘法错误的修正记录

本报告 §6 初稿错误地将第二乘积的零标签右侧 \(Q\) 保持为未平移的 \(Q\)，
遗漏了交叉积乘法中的 \(\beta_h\)；此处 \(g=0,h=\gamma\)，所以实际右侧是
\(\beta_\gamma Q\)。这导致误写 \(f_0\) 权重为 \(-3m_1m_2\)，并产生错误的
平台严格正结论。两者均已撤销。

经主审新增实际格点乘法审计及径向独立复核指出后，本报告重新逐项核验
\((\beta_\gamma q_\gamma)(\beta_\gamma Q)=\beta_\gamma q_\gamma\)，
并对照 [实际格点脚本](../../scripts/twisted_radial_witness_audit.py) 中两个零标签
乘积的独立断言及 [审计结果](f1-twisted-radial-witness-audit.json)；
该结果登记 600 项非零标签、50 项零标签修正源核验。有限枚举辅助核验符号，
不替代上述任意 \(\gamma\) 的交叉积乘法证明。
修正 (15) 为两个零标签同权 \(U_\gamma\)，修正 (16) 为下过渡
\(E_\gamma=2D_\gamma>0\)，修正 (17) 为平台 \(E_\gamma=D_\gamma=0\)。
非零 \(g\) 的阈值 \(R_i\)、§1–5 的全部 \(D_\gamma\) 公式及下过渡正见证未受影响。
本报告此前发送的“平台严格正且固定截止保持非零”结论无效；其哈希快照不可再作当前依据。
