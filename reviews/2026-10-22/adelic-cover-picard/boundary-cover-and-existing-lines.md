# 实际双位覆盖、已有非平凡线与物理源 clutch：定点比较

2026-10-22。分支独占稿。恢复 G20261014、0c4f 基线、C036/573 已结算和 D20261022G；
不改 STATE/cadence。本稿 §§1–3、5–9 是 409–414/420/553 的准确恢复与源比较；
§4 的此前未有的精确 clutch kernel 已由 root 准入 C037，并另存[独占证明](periodic-clutch-classification.md)。
新旧部分不合并冒作来源0，也不把这项新几何输入说成新 RH／成长预算结论。

## 1. 不能遗忘的强旧资产

- [409](../../../notes/409-f1-boundary-prime-power-kernels-and-heat-defects.md)：原完整 Q× 源纤维的 p 幂核为无穷维，普通有限 Fredholm 指数不存在；非 p 幂虽无核但像不闭。
- [410](../../../notes/410-f1-boundary-kernel-bundles-and-relative-k-classes.md) §§3–5：实际 p^Z 子群胚上有连续秩 a 核丛，周期过渡为循环矩阵，
  `det C_a(z)=(-1)^(a-1) z^(-1)`。其行列式线真正非平凡；秩随 a 变，相位绕数只有一次。
  非平凡性由真实紧单位悬挂上的绕数递推检测，没有虚构悬挂内的周期圆。
- [411](../../../notes/411-f1-full-rational-relative-classes-and-logarithmic-trace.md)：完整 Q× 不变扩张已有真正非零相对 K 类及 `2 a log p` 对数迹；共同轴商中的参数秩零项与 p 无关。
- [413](../../../notes/413-f1-two-place-boundaries-and-virtual-class-collapse.md)：下文真实开覆盖、两个单边 proper Morita 模型、全 O 非 proper、共同 bulk 坐标和连接映射均已证明。
- [414](../../../notes/414-f1-deep-boundary-unitary-and-time-defect.md)：真实源酉的边界为 `-η`，不能在相关代数单位化中提升为可逆元；乘子酉提升存在，二者不同。
- [420](../../../notes/420-f1-source-hardy-index-and-dual-action.md)：从实际源经 Hardy 压缩与稳定化得到真实指数线 `𝓛`，
  `(2π,z,λ) ~ (0,z,zλ)`，指定定向下 `c1(𝓛)=-1`、虚指数秩零。

所以“实际 adelic 方法只有自由线／从未有非平凡线”是错误总结。
目前未付的是任意物理 r 到合适 **可移动且 principal-compatible** 族的实际比较，以及同对象的整性、度量和 RR／mixed 容量。
上述固定线或相对 K 类并未支付这些箭头。

## 2. 使用真实覆盖，而非另造代数覆盖

固定不同素数 p,q，`L=log p`、`M=log q`。取 413 的

\[
T=\mathbf Z\cup\{\infty\},\quad
Y=T^2\times\mathbf R_t,\quad
(a,b)(j,k,t)=(j+a,k+b,t+aL+bM).
\]

删双零层 `D={(∞,∞)}×R` 得 O，两个 Γ 不变开片为

\[
W_p=\{k\in\mathbf Z\},\quad W_q=\{j\in\mathbf Z\},\quad
B=W_p\cap W_q=\mathbf Z^2\times\mathbf R.
\]

共同 bulk 坐标严格为 `x=t-jL-kM`，不是分别选两个独立实线。
Γ=Z² 在 B 上自由 proper，商为 R；在每一 W 边 proper，商为

\[
Z_L=(T\times\mathbf R)/((j,s)\sim(j+1,s+L))
\]

及 Z_M，但在整个 O 上不 proper。Z_L 是实际螺旋
`x↦(exp(x),exp(2πix/L))` 加零端圆；负端趋圆，正端没有附加点。
线对象以下均指这一个 Γ 覆盖上的等变连续复线／其 sheaf clutch；没有把完整非交换 C* 代数的任意 K 类都称为可逆层。

例如，交上 Γ 不变函数 `g(x)∈C(R,C×)` 可把 Wp、Wq 上两条平凡等变线粘为 L(g)。
若 g 是一个单边上延拓的无零函数，便是这个 Čech 覆盖的 coboundary；若额外规定边界 frame，还须核该延拓在边界是否为 1。

## 3. 一个原范数可付的实际源映射，仍精确平凡

物理源仍是 `r(u)=exp(u/2) f(u)`、`r∈S_exp,C`。固定实际 `κ∈Cc∞(R)`，令

\[
a_r=\kappa*r,\qquad g_r(x)=\exp(a_r(x)),\qquad r\longmapsto L(g_r).
\tag{1}
\]

这是在真实 B 上的实际 Γ 不变 transition，不依赖 Ξ 零点；复源也合法，未将实源结果冒作 complex-linear Picard 映射。
注意 (1) 是源到几何 clutch 的 map，不声称物理卷积到 pointwise 单位群是代数同态。

因 `a_r∈S_exp`，其负端趋 0；故 g_r 在 Z_L 和 Z_M 的零端圆均连续延拓为 **1**。
正端也趋 1，因此每边 `g_r-1∈C0(Z_ℓ)`，g_r 及其逆是实际单位化单位。
把 g_r 作为 Wp 的 gauge、Wq 取 1，即显式消去 transition。
该 gauge 在两个闭边界均为 1，因而同时保留所定边界 frames。此候选连这种相对带 frame 类也平凡。

设 `Dlog` 采用原全线 Fourier norm：

\[
\|r\|_{D\log}^2=(2\pi)^{-1}\int\log(2+|t|)|\widehat r(t)|^2dt.
\]

实际代表费对全源已有

\[
M_r:=\|a_r\|_\infty\le\|\kappa\|_2\|r\|_{du}
\le {\|\kappa\|_2\over\sqrt{\log2}}\|r\|_{D\log},
\]
\[
\|g_r^{\pm1}\|_\infty\le e^{M_r},\qquad
\|g_r-1\|_\infty\le e^{M_r}-1,
\]
\[
\|g_r-g_s\|_\infty\le
e^{\max(M_r,M_s)}\|\kappa\|_2\|r-s\|_{du}.
\tag{2}
\]

a_r 的导数由 `||κ^(j)||2 ||r||du` 支付；g_r 导数再用有限 Faà di Bruno 多项式及 e^Mr 上界。
这是所选 source→coefficient norm 的 upper fee，
不是任何算术截面、RR 格高度或非平凡线移动的必要费用。
若不平滑直接 `g=exp(r)`，原 du／Dlog 不控制 `||r||∞`，不得抄用 (2)。

全 physical Pan 关系对 (1) 的 Pic 类当然均消失，但 **每一个源** 的 Pic 类都消失。
537 的双 pole-zero 非根 r0 也映到平凡类，失败的正是 nonroot 可见性；不能以“关系已过”报告成功。
若把 gauge／frame 参数保留为标记，它只是实际原源的额外数据，尚不是非平凡 Picard 移动。

## 4. 覆盖本身确实允许非平凡 character clutch，不能泛称 Pic=0

对 `λ∈R` 取

\[
g_\lambda(x)=e^{i\lambda x},\qquad L_\lambda=L(g_\lambda),\qquad
\Lambda_{L,M}={2\pi\over L}\mathbf Z+{2\pi\over M}\mathbf Z.
\tag{3}
\]

在这个 **特定 character 子族** 内，

\[
L_\lambda\simeq L_\nu\iff\lambda-\nu\in\Lambda_{L,M}.
\tag{4}
\]

充分性：频率 `2πm/L`、`2πn/M` 的相位分别延拓为两边零端圆上的周期单位，所以是两个 side gauge 的乘积／比。

必要性只用真实 Z_L 拓扑。若 `e^(iλx)=a(x)/b(x)` 是 side gauges，
它们负端分别一致逼近无零 L 周期 A(x) 和 M 周期 B(x)。于是
`e^(iλx)-A(x)/B(x)→0` 当 x→−∞。
三频率 `(λ,2π/L,2π/M)` 有同时近回到单位元的无界负移位：可由紧环面上的有限网格 pigeonhole 得到；
若已为有限周期，取周期倍数即可。沿该负移位把渐近恒等式传回任意固定 x，得到
`e^(iλx)=A(x)/B(x)` 处处成立。
写周期单位的绕数分解

\[
A(x)=e^{2\pi imx/L}e^{a_0(x)},\qquad
B(x)=e^{2\pi inx/M}e^{b_0(x)},
\]

其中 a0、b0 是有界连续周期 logarithm。
提升相位后，`i(λ-2πm/L+2πn/M)x-(a0-b0)` 是连续的 `2πi Z` 值函数，故常值。
有界性迫线性频率为零，得必要性。
对两个 λ 相减给 (4)。

例如 `λ0=π/L` 不在 Λ：若 `1/2=m+nL/M`，无理性 L/M 迫 n=0，又与整数 m 矛盾。
因此 **真实覆盖上有具体非平凡等变线** L_(π/L)，不是先挑抽象 K 生成元。
这是从 413 拓扑给出的本次新精确子族分类，不主张外部首创；没有构造整性局部环或 RR 容量。
完整复指数、relative frames 与 metric 范围见[独占证明](periodic-clutch-classification.md)。

还须保留一个重要区别：Λ 稠密，因此这个 character 子族的自然参数商 R/Λ 的 quotient topology 是 indiscrete。
这是 character family 的商描述，不是对整个 Picard stack、全部相对拓扑或代数 Pic 的分类。
它恰说明保留 λ、holonomy、frame／微分数据与只保抽象线类有不同信息，不能把这个商直接当成已付 Hausdorff 正能量空间。

## 5. 将 (3) 真正接物理源：两种最便宜实际选择分别失败不同门

选 real-linear `λ(r)=Re µ_+r`，或者乘任意固定实常数。
405 全 Pan 的 µ+、µ− 均零，因此 `L_(λ(r+q))=L_(λ(r))` 对每个 q∈Pan。
但 537 r0 的两矩也是零，所以其像等于 0 源的线。只借 pole 字符能保两 degree，却不能保 nonroot。
405 的 h 两矩各 1/4，不能将其当 Pan；degree 数据仍需单独保留。

选 `λ(r)=Re ∫r du` 则固定窗费更小，却不消全 Pan。旧 405 具体物理关系

\[
P=(D^2-\tfrac14)H\in P_c,\quad H=e^{u/2}h>0,
\qquad\int P=-\tfrac14\int H<0
\]

由全部衰减严格成立。缩放该同一个真实主关系，使 `λ(P_scaled)=π/L`，
便将零商类送到第4节证明非平凡的 L_(π/L)。这是明确 principal 反例，而不是只检验一个自选 relation。
累计 primitive phase 的端点费用若只读 ∫r，也有同一个失败；加两 pole degree 不修复双矩已经零的 P。

两种读出的 **实际 fixed 窗原 norm upper fee** 为

\[
|\mu_\pm r|\le\sqrt{2\sinh A}\|r\|_{du},\qquad
\left|\int r\right|\le\sqrt{2A}\|r\|_{du}
\quad(\operatorname{supp}r\subset[-A,A]),
\tag{5}
\]

转 Dlog 时除 `sqrt(log2)`。这不是全线 uniform bound；405 P 的全线反例不因 compact 窗 Pan 空交而消失。
在 `|x|≤X` 上 `||g_λ-g_ν||∞≤X|λ-ν|`，但在整个 R 上不同频率的 uniform norm 距离是 2。
所以 character family 仅按 compact-open 参数连续，不能把 (5) 说成全 bulk 乘子算子范数的 Lipschitz 费。

若试用某个其他 λ(r) 消全 Pan 且看见 r0：
若 λ 是到 Hausdorff metric target 的全 du／Dlog 连续 coset map，则旧 [553](../../../notes/553-principal-cyclic-closure-and-cofinal-readout-fees.md) 的 Pan 稠密性迫其常值。
若改用 S_exp Fréchet 上的全部 Mellin／zero-jet 读出，非平凡类可以标记旧商，但这是旧谱商输入，并未产生独立容量。
这不排除 stronger topology、带费用的变域、actual sheaf 额外 regularity 或新的非谱 source bridge。

还有一个更强、必须承认的旧包装控制：完整既定解析 Q 本身就给 **实际** nonlinear 源映射

\[
z(r)=i c Q_\zeta(r),\qquad r\longmapsto\mathscr L_{z(r)}.
\tag{6}
\]

405 的完整 identity 给 Pan 是 Q 的 radical，所以 (6) 消全部真实 Pan coset；537 给 Q(r0)>0，
选固定 `c=π/(L Q(r0))`，便把 r0 送到 §4 的真实非平凡线 `𝓛_(iπ/L)`。
定义 (6) 直接使用完整 Γ、prime powers、双 pole 的分布公式，不预设未知零点位置；
不能因它是旧包装就否认这个实际 map 的存在。
但其 Pic 坐标直接装入欲比较的原 Q 值，连续正反模型对正／负 Q 都有同样 unitary metric，
因而没有独立正号，不能将这个 fiber metric 再称为 Q 正性的证明。
它也不是 physical addition 到 tensor product 的同态：令 `a=r0/√2`，
则 `z(2a)=i2π/L` 给 absolute 平凡线，而 `2z(a)=iπ/L` 给严格非平凡线。
一般 mixed 差由原 Q 的交叉项决定，不能从 marker 拼接新得到同源 correspondence composition。

对每个先 fixed 窗 A，旧完整 Γ form 界、555 的完整 prime operator 界及 pole rank2 界给
`|Q(r)|≤C_A||r||Dlog²`，同窗 mixed 界还给
`|Q(r)-Q(s)|≤C_A(||r||Dlog+||s||Dlog)||r-s||Dlog`。
这是 (6) 的 **原 Dlog fixed 窗** 坐标 upper fee，不是全线 uniform quotient fee；
完整 Γ 在 du 上无同级 bounded form，因此不能报告纯 du 有同一界。
在每个 `|x|≤X` 的 transition 费还要乘 X，全球 multiplier norm 仍不可据此付。
本控制明确消全关系且保 nonroot，但按用户“若只是旧商包装就停止”的规则收口，
不命名为新的 source-to-capacity bridge。
在连续正反模型上直接用各自完整 `Q_c` 作同样标签，两号值均生成纯虚参数且都允许同一个 unitary fiber metric；
因此“全 Pan 已消、r0 已见、fiber metric 正”三门合在一起也不独立推出完整 Weil 符号。

## 6. 旧非平凡指数线接源后的信息边界

把任何 L(g_r) tensor 410／420 的固定非平凡线，只给同一个固定 Pic 类；
前面的 decaying gauge 可消掉，不能借“tensor 后非平凡”偷换成 source-dependent 移动。
若把 420 的对偶平移参数 ν 取成源标量，其 ordinary K 类仍同秩零、同 Chern=-1；
420 已明确保留整个 marked 双作用和 cutoff 才能保时间频率，不能以 ordinary index 替代完整周期测试。
这不排除该增强数据有用；缺的是实际从 r 得出的全 Pan 同伦／相对比较及原费用，而非再算一次固定 Chern 数。

同理，413 可提升虚对 `(1,-1)` 并不自动是算术主除子；414 用真实局部周期测试已给非零残差。
线 transition、boundary K class、relative triple、determinant line 是不同层次，不应由名称互相等同。

## 7. 函数域与连续正反控制，及保留的完整目标

函数域成功对照是 `Pic^0(C)` 的 **regular-unit sheaf** 和真实局部 DVR：
degree-zero 的 `O(P-Q)` 可以非平凡，交叠 rational transition 在允许局部环内不能被任意连续无零 gauge 消去。
这与本稿 (1) 在实际连续 C0 模型里有 side unit 延拓有实质差别。
已有 genus2 真例 `L0=O(P+Q-2∞)`、`h0(K)=2` 到 `h0(K⊗L0)=1` 的证明与 base change 已保存在上一门，
本稿不再计一次；非平凡 algebraic Pic0 也不能凭其底层 topological Chern 类识别。
regular sheaf、整性／消失过滤、proper pushforward 与极化都是额外实际设施，不是把连续单位改名即可恢复。

连续正反两段仍使用上一门同一个完整 Π／双 pole 模型，Γ=0 是模型本身的既定背景；
clutch (1)/(3)、其费用和 side 延拓不读取 Π，因此同样存在于两个相反 Weil 符号的系统。
本稿没有把该模型伪称经典 adele geometry；只检验“覆盖／线族本身足以独立强迫正号”的推理。

经典目标始终为同一个物理 r 的

\[
\begin{aligned}
Q_\zeta(r)={}&2\Re(\mu_+r\,\overline{\mu_-r})+
[\psi(1/4)-\log\pi]\|r\|_2^2\\
&+\tfrac12\int_0^\infty{2e^{-v/2}\over1-e^{-2v}}
\|\tau_vr-r\|_2^2dv\\
&-2\sum_{p,k\ge1}\log p\,p^{-k/2}
\Re(r*r^*)(k\log p).
\end{aligned}
\]

全部 Γ/contact、所有 proper powers、双 pole 及 complex mixed 责任未删。
本稿的局部 cover／clutch 不给它们任何一项的新预算身份。

## 8. 停止／未排范围与独立新输入

本次 source gate 得到更准确的区分：真实覆盖有非平凡 character 线、旧核线／指数线也非平凡；
但自然 decaying source clutch 是严格 coboundary，degree-only character 杀 r0，mass character 失败全 Pan。
能全局消 Pan 并保 nonroot 的 old spectral coordinate 重新标记，不通过用户本次“非旧商包装”的停止门。
这些检查不改变 strong-old 542+555→557 whole leading 4/5 的 issued upper budget，也不给 actual 负谱 lower／core／Ξ／RH。

仍缺独立输入应具体交付为：

1. 一个来自实际 adeles／对应的 **额外 regular-unit／相对层结构**，其允许 gauges、overlaps 与任意 source 的 map 可写且不按 Ξ 定义；或另一真实非谱 moving family。
2. 全 Pan 在该相同层结构内的 actual coboundary／lift，同对象保 r0 和两个 degree；strong／cofinal 费用与原 du／Dlog 明确比较。
3. 同一层上的整数格／局部消失过滤、实际截面 multiplication 与 paid pushforward；局部函数 locally constant 或 transition 非零本身不提供 DVR jets。
4. 独立有效性／ample mixed 交数或 RR 容量，并将该同源预算与完整上式比较。不能先按 Q 定义正 metric 再把其正性作为输入。

没有上述新数据，不续固定指数／单 character scalar／source gauge 参数。保非自由／非仿射／非标量相对 Pic、Fréchet 或变域付费修复，不作全 Pic=0 或所有 adelic geometry 无效结论。

## 9. 原始来源的准确消费

- [CCM2007 v1](https://arxiv.org/html/math/0703392v1) §§4、8：实际 adelic restriction／边界与 covering 背景。本文 Wp/Wq、拓扑及具体线的直接证明消费的是已审 413/410，不把 CCM 当作本稿所有 clutch 命题的现成定理。
- [Milne, Jacobian Varieties](https://www.jmilne.org/math/xnotes/JVs.pdf) §1：`Pic=H1(O×)`、相对 degree-zero 线族模掉从 base 拉回的线；这区分真实 relative Picard family 与固定线乘源标量。本文未声称原件已为经典 adeles 构造 Jacobian。

以上区分旧资产恢复、原范数／源比较及 C037 新精确子族分类；不认证整篇原件，
也不把该新几何分类作为新的经典正性定理。
