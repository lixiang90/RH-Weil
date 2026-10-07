# 原高素数 parity 对平方残差的预算：有界 q 下的必要联合约束

2026-10-07。作者 radial_review。新完整推导，待另一作者全文独审。
保留原 Eisenstein / AF 矩阵、所有内部 P、sharp coefficients 与全部高度。
新增的是 high 平方残差的 odd 部分预算和 low 平方残差的 parity 常数。
没有证明 467 的算术前件，也没有新的实际比例、无零边界或 RH/RR 结论。

## 1. 原对象与冻结输入

沿用原 \(X=T/(2\pi)\)、\(\mathcal L=\log X\)、\(d=\lfloor X\mathcal L\rfloor\)、
interval carrier \(E\)、\(P=EE^*\)、\(Q=1-P\)。
\(B_H,B_L\) 为原 high/low genuine-prime 平移和；
\(H=E^*B_HE,L=E^*B_LE\) 为真实 Hermitian finite matrices。
\(J=M_{\operatorname{sgn}u}\)、\(S=E^*JE\)、\(U=\operatorname{sgn}S\)，
零特征值处选 \(+1\)，所以 \(U^*=U,U^2=I\)。
原 \(W=E^*M_wE,V=E^*M_vE\) 是两个非负 bounded diagonals。
置 \(\Gamma=H^2-W,\Delta=L^2-V\)，并保留 467 的 \(q,c\) 定义。

| 完整冻结输入 | canonical LF SHA-256 |
| --- | --- |
| [actual high parity](hybrid-high-parity-gram-and-mobius-completion-research-radial.md) | 3f4c714bb126356389332f3674836d6edf6f110f60935a27af93a58a0e26bbb2 |
| [entire low4](hybrid-low-prime-exact-fourth-path-constant-research.md) | 798947fb9cd13f25b541025f0c180945590341bbab6f55cacbcf6c50e87ee080 |
| [465](../../notes/465-centered-high-square-joint-fourth-budget.md) | a9290d2d847c2a3f7942b26353bd1582a68b391e481acc109c4ac18d3d750464 |
| [466 含 sharp \(4M\)](../../notes/466-high-square-variance-commutator-obstruction.md) | 0b955bdc26b4bf950ce457dec7bf18f635f702d85a73d73c8d6263df969cbbbe |
| [467](../../notes/467-two-residual-schur-and-commutator-budget.md) | 0089fd92c70d5e2b7b48bef0084675707f2fe283833f8a97745766ccf6899cb8 |

这些输入已经支付
\[
 \frac{\|H+UHU\|_2}{\sqrt d}=o(1),\quad
 a_T:=\frac{\operatorname{Tr}H^4}{d}=S_H+q_T+o(1),\quad
 K_T:=\frac{\|[H,W]\|_2^2}{d}\longrightarrow\frac{41}{10080}.
 \tag{1}
\]
flat 下可取 \(0\le W\le M_TI\)、\(M_T\to M=3/8\)。
这里 \(\|\cdot\|_2\) 是 HS norm。
whole low4 已付 \(e_T\to19/240\)、\(S_L=7/240\)、
\(\|\Delta\|_2^2/d\to1/20\)。
整个13、weighted2及底层 [R] 的准确范围仍是 467 所列范围；
本稿不重证其分析内核。以下新增必要界本身不需要新的 [R]。

定义实际 finite parity projections
\[
 \mathcal E_U(A)=\frac{A+UAU}{2},\qquad
 \mathcal O_U(A)=\frac{A-UAU}{2}.
 \tag{2}
\]
它们在 real HS 空间中是正交投影。写
\[
 q_T^{\mathrm e}=\|\mathcal E_U\Gamma\|_2^2/d,\qquad
 r_T=q_T^{\mathrm o}=\|\mathcal O_U\Gamma\|_2^2/d,\qquad
 q_T=q_T^{\mathrm e}+r_T .
 \tag{3}
\]
它们与 466 在 H 特征基中的 \(q_{\rm diag},q_{\rm off}\) 不同。
不能从 (1) 的 H 二范数 parity 免费推出 \(\Gamma\) 的二范数 parity：
fourth tails 仍可能留下非零 \(r_T\)。

## 2. bounded weight 与 U 的渐近交换

原 sharp J 的 Fourier coefficients 给
\(\ell_J:=\|QJE\|_2=O(\sqrt{\log(2d)})\)、
\(\|U-S\|_2\le\ell_J\)。
对 \(w,v\)，465 的 bounded-weight leakage 给
\(\ell_w,\ell_v=O(\sqrt{\log(2+\mathcal L)})\)。
因为真实 \(J\) 与两个乘法函数交换，
\[
 [S,W]=-E^*JQM_wE+E^*M_wQJE .
 \tag{4}
\]
故 \(\|[S,W]\|_2\le\ell_w+\|w\|_\infty\ell_J\)。
加入 \([U-S,W]\) 得 \(\|[U,W]\|_2=o(\sqrt d)\)；
V 完全相同。因此
\[
 \|\mathcal O_UW\|_2/\sqrt d=o(1),\qquad
 \|\mathcal O_UV\|_2/\sqrt d=o(1).
 \tag{5}
\]
这个比较保留原 carrier；没有把 P 当成与 J 交换的投影。

## 3. fixed clip 的严格有限估计

对 fixed \(R>0\)，令 \(f_R(x)=\max(-R,\min(x,R))\)、
\(H_R=f_R(H)\)、\(\Gamma_R=H_R^2-W\)、
\(q_{R,T}=\|\Gamma_R\|_2^2/d\)。
HS Lipschitz 无需外部黑箱：若 A、B 的谱为 \(a_i,b_j\)，谱投影为
\(P_i,Q_j\)，则
\[
 \|f(A)-f(B)\|_2^2
 =\sum_{i,j}|f(a_i)-f(b_j)|^2\operatorname{Tr}(P_iQ_j)
 \le\operatorname{Lip}(f)^2\|A-B\|_2^2 .
 \tag{6}
\]
每个 \(\operatorname{Tr}(P_iQ_j)\ge0\)。
f_R 为 odd、1-Lipschitz，所以
\(\|H_R+UH_RU\|_2\le\|H+UHU\|_2\)。
由 \(\|H_R\|\le R\)，
\[
 e_{R,T}:=\frac{\|\mathcal O_U\Gamma_R\|_2}{\sqrt d}
 \le R\frac{\|H+UHU\|_2}{\sqrt d}
       +\frac{\|\mathcal O_UW\|_2}{\sqrt d}=o_R(1).
 \tag{7}
\]

令 \(D_R=H^2-H_R^2\ge0\)。它只支持 \(|H|>R\)，在该支持上
\(H_R^2=R^2I\)。若 \(R^2\ge M_T\)，准确有
\[
 \frac{\operatorname{Tr}\Gamma_RD_R}{d}
 \ge(R^2-M_T)\frac{\operatorname{Tr}D_R}{d}\ge0,\qquad
 q_T-q_{R,T}
 =\frac{\|D_R\|_2^2+2\operatorname{Tr}\Gamma_RD_R}{d}
 \ge\frac{\|D_R\|_2^2}{d}.
 \tag{8}
\]
因此 \(q_{R,T}\le q_T\)，并且
\[
 r_T\le q_T-q_{R,T}+2e_{R,T}\sqrt{q_T}+e_{R,T}^2 .
 \tag{9}
\]
这是 finite PSD tail 估计，不删除 centering/tail errors。

令 \(K_{R,T}=\|[H_R,W]\|_2^2/d\)。
466 的通用 sharp 界对每个 \(H_R,W\) 直接给
\(q_{R,T}\ge K_{R,T}/(4M_T)\)。
同时
\[
 \frac{\|H-H_R\|_2^2}{d}\le\frac{a_T}{R^2},\qquad
 \left|\sqrt{K_T}-\sqrt{K_{R,T}}\right|
 \le \frac{2M_T\sqrt{a_T}}{R}.
 \tag{10}
\]
将 (9)–(10)合并得到明确 finite 必要式
\[
 r_T\le q_T-
 \frac{(\sqrt{K_T}-2M_T\sqrt{a_T}/R)_+^2}{4M_T}
 +2e_{R,T}\sqrt{q_T}+e_{R,T}^2 .
 \tag{11}
\]
M_T 取正；W=0 的退化情形单独显然成立。

## 4. 两次极限与真正联合量词

现在明确增加前件 \(q_T=O(1)\)。由 (1) 得 \(a_T=O(1)\)。
先固定任意足够大的 R，再 \(T\to\infty\)，最后 \(R\to\infty\)。
(7)、(10)与 (11)准确推出
\[
 \boxed{\liminf(q_T-r_T)\ge\underline q=\frac{41}{15120}.}
 \tag{12}
\]
等价地 \(\limsup(r_T-q_T)\le-\underline q\)。
更准确的子列陈述是：每个有界共同极限
\((q_T,r_T)\to(q_\infty,r_\infty)\) 都满足
\[
 0\le r_\infty\le q_\infty-\underline q.
 \tag{13}
\]
这里没有把不同子列的两个 limsup 混为一个共同值。
有限估计中的 \(a_T/R^2\) 只有在明列 bounded-q 后才统一趋零；
不能对未知增长的 whole high4 先做此步。

若 467 的 \(Q=1/350\) 前件成立，则
\[
 \boxed{\limsup r_T\le Q-\underline q=\frac{11}{75600}.}
 \tag{14}
\]
这证明已付 commutator 的方差成本至少落在 U-even 残差中。
U-odd fourth tails 仍允许存在，但只能占剩余预算。
它比重新计算总 q 的 sharp \(4M\) 下界多一个真正 parity 必要约束。

## 5. low 平方 parity：保留原 P 的准入

以下独立于 bounded high q，只用整个原 low4 的已付输入。
写 \(y=\|B_L\|\ll X^{1/4}/\mathcal L\)、
\(\ell=\|QB_LE\|_2\ll X^{1/4}\sqrt{\log(2+\mathcal L)}/\mathcal L\)、
\(T_L=B_L^2,A=L^2\)。
准确的 compression difference 为
\[
 A-E^*T_LE=-(QB_LE)^*(QB_LE),\qquad
 \|A-E^*T_LE\|_2\le y\ell=o(\sqrt d).
 \tag{15}
\]
由 \(\|U-S\|_2\le\ell_J\) 以及逐项保留 P、Q 的展开，
\[
 \|UAU-E^*JT_LJE\|_2\le C(y\ell+y^2\ell_J)=o(\sqrt d).
 \tag{16}
\]
例如 \(S(E^*T_LE)S=E^*JP T_LPJE\) 与
\(E^*JT_LJE\) 的差，每项至少含一个 \(QJE\)，费用不超过
\(2y^2\ell_J\)；没有循环物理末端 P。
这里 \(y^2\ell_J/\sqrt d=O(\mathcal L^{-2})\)。

令 \(T_{\rm o}=(T_L-JT_LJ)/2\)。
\(\|QT_LE\|_2\le2y\ell\)，而
\(\|QJT_LJE\|_2\le2y\ell+2y^2\ell_J\)。
所以
\[
 \|QT_{\rm o}E\|_2=o(\sqrt d),\qquad
 \|\mathcal O_U\Delta-E^*T_{\rm o}E\|_2=o(\sqrt d).
 \tag{17}
\]
第二项使用 (5)。由整个 physical low4 bounded 与 (15)–(17)，
\[
 \frac{\|\mathcal O_U\Delta\|_2^2}{d}
 =\frac{\operatorname{Tr}(E^*T_{\rm o}^2E)}{d}+o(1).
 \tag{18}
\]
HS 平方传递合法：两侧 normalized HS norms 先由 low4 给有界。
physical-to-actual gap 恰为 \(\|QT_{\rm o}E\|_2^2\)，已在 (17)支付。

sharp J 的路径计算可严格按固定 smooth \(J_\epsilon\) 先付款。
选择 odd contraction \(j_\epsilon(u/\mathcal L)\)，在
\(|u|\ge\epsilon\mathcal L\) 等于 sign u。
固定 \(\epsilon>0\)，将这些 C2 函数插入原 low4 的各路径窗：
near 联合 Fourier/Hilbert只是增加有限个窗因子，
费用为 \(O_\epsilon((\log(2+\mathcal L))^m/\mathcal L^2)=o(1)\)；
entire far 的 support 和 alias不变，bounded 窗仍用原 absolute mass付款。
所有 zero labels 仍是原三配对，all-repeat correction仍 \(O(\mathcal L^{-4})\)。
weighted finite-to-physical 费用至多
\[
 C_\epsilon(y^2\ell^2+y^3\ell\ell_g+y^4\ell_g^2)=o(d),
 \tag{19}
\]
其中 \(\ell_g=O_\epsilon(\sqrt{\log(2+\mathcal L)})\)；
这是 closed finite word 的两次 crossing 展开，不删除单个内部 P。

为了最后 \(\epsilon\downarrow0\)，取 fixed smooth
\(g_\epsilon\ge|J-J_\epsilon|^2\)，支撑在
\(|u|\le2\epsilon\mathcal L\)，且 \(0\le g_\epsilon\le4\)。
weighted low4 的 zero-path 主项在每条路径只积分一个宽
\(4\epsilon\) 的 translated strip，所以
\(\operatorname{Tr}((E^*M_{g_\epsilon}E)L^4)/d=O(\epsilon)+o_\epsilon(1)\)。
令 \(S_\epsilon=E^*J_\epsilon E\)，compression Schwarz 给
\[
 (S-S_\epsilon)^2\le E^*|J-J_\epsilon|^2E
 \le E^*M_{g_\epsilon}E.
 \tag{20}
\]
因此 \(\|(U-S_\epsilon)A\|_2/\sqrt d
=O(\sqrt\epsilon)+o_\epsilon(1)\)：
U-S 部分用 \(y^2\ell_J=o(\sqrt d)\)，另一部分用 (20)和正 weighted low4。
这也控制 \(UAU-S_\epsilon A S_\epsilon\)，再由 (16)的 smooth 版本
传到 physical 路径。故 sharp J 极限遵守
固定 \(\epsilon\)、先 T 后 \(\epsilon\) 的顺序，不依赖未知 high4。

## 6. 原 low zero atoms 的完整 parity 常数

仅本节取 flat profile，令 \(x=\log p/\mathcal L,y=\log q/\mathcal L\)，
\(0\le x,y\le1/2\)，row 坐标为 \(t\in[-1/2,1/2]\)。
在 \(T_{\rm o}^2\) 的准确四词展开中，net zero 的系数是
\(\frac12[1-\operatorname{sgn}t\operatorname{sgn}(t+S_2)]\)，
即 middle-after-two 与起点处于不同半轴的指示函数。
非零原子已由第5节整体付款，不能只计算配对积分代替全四词。

entire low4 原三配对为
\[
 A:(p_\sigma,p_{-\sigma},q_\eta,q_{-\eta}),\quad
 A':(p_\sigma,q_\eta,q_{-\eta},p_{-\sigma}),\quad
 O:(p_\sigma,q_\eta,p_{-\sigma},q_{-\eta}).
 \tag{21}
\]
A 在两步后准确回到起点，odd 主项为0。
A'、O 两步净位移均 \(\sigma x+\eta y\)。
两者的每个 intermediate position 仍在原 interval 内。
若 \(\sigma=\eta\)，crossing strip 的长度为
\(\min(x+y,1-x-y)\)，两种同号 orientation 相同；
若 \(\sigma=-\eta\)，长度为 \(|x-y|\)，两种异号 orientation 相同。
后一条可直接在 \(x\ge y\) 上检查：
crossing \(t\in(-(x-y),0)\)，且 \(x,y\le1/2\) 保证两条路径的其他点仍在 I；
交换 x、y 付另一半。保持原 orientations和 ordered primes，没有移走 P。

因此全原子及全部 placements 的总结果为
\[
 \delta_{\mathrm o}
 :=\lim\|\mathcal O_U\Delta\|_2^2/d
 =4\int_0^{1/2}\!\int_0^{1/2}
 xy\{\min(x+y,1-x-y)+|x-y|\}\,dx\,dy.
 \tag{22}
\]
由原 prime measure \(x\,dx\)、bounded translations及第5节准入得到此式。
all-repeat overlap correction仍趋0，未另减或漏掉其六种 signs。
三个分区多项式积分准确为
\[
 \int xy|x-y|=\frac1{480},\quad
 \int_{x+y\le1/2}xy(x+y)=\frac1{960},\quad
 \int_{x+y\ge1/2}xy(1-x-y)=\frac7{1920}.
 \tag{23}
\]
所以
\[
 \boxed{\delta_{\mathrm o}=\frac{13}{480},\qquad
 \delta_{\mathrm e}:=\lim\|\mathcal E_U\Delta\|_2^2/d
 =\frac1{20}-\frac{13}{480}=\frac{11}{480}.}
 \tag{24}
\]
V 的 U-odd 部分由 (5)为零极限，不能将 V 当成另一个 arbitrary low矩阵。

## 7. 新实际必要 covariance 区间及候选的准确状态

467 的准确 finite 内积
\(\langle\Gamma,\Delta\rangle=c_T-\chi_T,\ \chi_T\to C=23/960\)。
orthogonal parity 分解和两次 HS Cauchy给
\[
 |c_T-\chi_T|
 \le\sqrt{(q_T-r_T)\delta^{\mathrm e}_T}
       +\sqrt{r_T\delta^{\mathrm o}_T}.
 \tag{25}
\]
对每个共同有界极限 \((q_\infty,r_\infty,c_\infty)\)，由 (13)、(24)
\[
 \boxed{|c_\infty-C|
 \le\sqrt{(q_\infty-r_\infty)11/480}
       +\sqrt{r_\infty13/480},\quad
 0\le r_\infty\le q_\infty-\underline q.}
 \tag{26}
\]
这是 actual 原结构上的必要条件，较 467 的
\(|c-C|\le\sqrt{q/20}\) 更细。未把 H 二范数 parity 偷升级成 fourth parity。

在尚未证明的 \(q_T\le Q+o(1),Q=1/350\) 前件下，
右侧先随 q 增大而增大。
取 q=Q 后，它随 r 增大至 \(r=Q(13/480)/(1/20)=13/8400\)；
允许的 \(r\le11/75600\) 全在该单调区间内。
因此
\[
 \limsup|c_T-C|
 \le\sqrt{\frac{451}{7257600}}
      +\sqrt{\frac{143}{36288000}}<\frac1{100}.
 \tag{27}
\]
最后一个严格比较有纯有理平方证书。记两个根号内数为 A、B，则
\[
 \frac1{10000}-A-B=\frac{3077}{90720000}>0,\qquad
 \left(\frac1{10000}-A-B\right)^2-4AB
 =\frac{4883}{28576800000000}>0.
 \tag{28}
\]
故候选必须满足更窄区间
\[
 \boxed{\liminf c_T\ge\frac{67}{4800},\qquad
        \limsup c_T\le\frac{163}{4800}.}
 \tag{29}
\]
实际上端点有 (27) 的严格余量。这比原 \(C+3/250\) 的外包络小。

本稿没有仅凭这些必要条件排除或实现
\(q\le1/350,k\ge1/40\)；
没有构造满足全部实际 high transition kernel 的有限 prime model。
两份算术合同仍未付。特别是 \(\Delta\perp Z\) 的整体信息不能未经新证明
拆成每个 parity 分量各自正交；本稿没有如此使用 entire13。
继续付款可利用这里准确分配的 even/odd 方差、真实 weighted transition
和 signed high covariance。原 RH、实际比例及既定无零边界均保持开放状态。
