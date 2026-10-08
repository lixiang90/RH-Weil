# 原 whole 四全异 unit 块：真实加性主频带与完整 chirp 付款

2026-10-08，whole_mixed4。独立研究源，待 root 全文审查。
只写本文件；不改旧来源、笔记、检查器或 Git。

本稿取得一个覆盖原全部最大标签位置、共同空间 profile 和真实 carry 的
缩约。联合完成真实产品变量以后，剩余 unit 块的主项是一个明确的
`n asymp qX/s, q not dividing n` 加性频带。原 log 相位的全部有限 Taylor
修正，在同一完整族中为 `O(X^(1/2) log^C X)`；低产品、upper-gate 边界
和 graph 修正另有完整付款。

没有证明主频带的有用 signed 上界，没有新的 canonical scalar whole
四阶幂、简单零点比例、kappa 或无零区域。本稿的频带是**合并真实 a 核
之后的单加性完成**，不是两个 Kloosterman dual 的免费短截断。

## 1. 完整读取并冻结的准入合同

已全文读
[双非单位实际来源](hybrid-whole-fourth-double-nonunit-actual-research-whole.md)，
545 行，canonical UTF-8 LF SHA256
`2d27661262a1e672a9bb93846de68a661e0d17d8f5e0444117ae6a8debac4215`。
同时读 472、456、465、474 的原载体、重复词、same-prime 和 scalar
准入合同。以下不修改或扩大这些来源的结论。

保留
\[
 X=T/(2\pi),\quad L=\log X,\quad d=\lfloor XL\rfloor,
 \quad \eta=2\pi/L,\quad s_T=T/\sqrt L,
 \qquad b_p=\frac{\log p}{a_LL\sqrt p},\quad a_L\ge c_\phi>0.
 \tag{1}
\]
原 genuine primes 都在 `sqrt X<p<=X`，原 even C² taper 不升级光滑性。
载体为原 `sigma in [T,T+s_T]` 的固定正概率密度 chi，且
\[
 \operatorname{supp}\chi\subset[3/8,5/8],\qquad
 \Gamma(z)=\int\chi(v)e^{izv}dv,\qquad
 |\Gamma(z)|\le e^{-\sqrt{|z|}/16}\quad(|z|\ge256).
 \tag{2}
\]
原 near threshold 是 `Delta=1024 L^(5/2)/X`。

使用原 actual 到 physical 的 whole union 桥之后才作以下分解。
不逐 tuple 删除内部 P，不移动到 canonical scalar `J=[T/4,4T]`。
原 half-ratio prefactor 是 `L^(-1) int_(I_+) phi(u)^2 du`，至多 1/2。

## 2. 实际所有词与 exact graph correction

四全异标签的真实最大素数唯一，记 q。若最大素数在分母，交换两对
标签并取共轭；故只须处理最大素数在分子的两个位置，最后恢复全部
四种位置。另一个分子素数 s 满足 `sqrt X<s<q<=X`。
分母为真实素数 `p,r<q`，记
\[
 A=qs,\quad a=pr,\quad h=A-a,\quad S=\log(A/a).
 \tag{3}
\]

第一位置的原共同 profile 是
\[
 A_p=b_p1_{\sqrt X<p<q,p\ne s}
 \phi(u-\log p)^2\phi(u+\log(q/p)),
\]
\[
 B_r=b_r1_{\sqrt X<r<q,r\ne s}
 \phi(u-\log s)^2\phi(u+\log(r/s)).
 \tag{4}
\]
第二位置是
\[
 A_p=b_p1_{\sqrt X<p<q,p\ne s}
 \phi(u-\log p)^2\phi(u+\log(s/p)),
\]
\[
 B_r=b_r1_{\sqrt X<r<q,r\ne s}
 \phi(u-\log q)^2\phi(u+\log(r/q)).
 \tag{5}
\]
始终保留同一个 u。Chebyshev/partial summation 给
\[
 \|A\|_2,\|B\|_2\ll_\phi1,\quad
 \|A\|_1,\|B\|_1\ll_\phi\sqrt q/L,\quad
 \sum_{p\le z}b_p\ll_\phi\sqrt z/L.
 \tag{6}
\]

令 `c=q²`，`e_c(x)=exp(2pi i x/c)`，原 hard-near a 权为
\[
 W_A(a)=1_{1\le a<c}1_{|S|<\Delta}\Psi(S),\qquad
 \Psi(S)=e^{iTS}\Gamma(s_TS)d^{-1}\sum_{k<d}e^{ik\eta S}.
 \tag{7}
\]
原 raw 产品严格满足 `pr<c`；在该 gate 内 `pr=a (mod c)` 才与
真实整数等式 `pr=a` 等价。

冻结来源的 mixed Kloosterman blocks 对 unit a 消失。重新合并其整个
unit/unit raw 核，physical inverse 精确为
\[
 U_a(p,r)=1_{pr=a\ (c)}-q^{-1}1_{pr=a\ (q)}.
 \tag{8}
\]
这是 exact completion 的结果，不是 generic 点态上界。
若
\[
 F_A(n)=\sum_aW_A(a)e_c(na),\qquad
 \mathcal B_n=\sum_{p,r}A_pB_r e_c(-npr),
\]
则 raw unit 为
\[
 Z_U(q,s,u)=c^{-1}\sum_{\substack{n\bmod c\\q\nmid n}}
 F_A(n)\mathcal B_n.                                      \tag{9}
\]
因为完整 `n divisible by q` 子和正是第二项的 mod-q 条件平均。
这里尚包含 `p=r`，其余 repeated 条件已由 (4)、(5) 准确排除。

记原 exact diagonal 为
\[
 D_{\rm actual}=\sum_pA_pB_pW_A(p^2),
\]
双非单位 diagonal 为冻结来源 (24) 的 `D_nn`。原完整未付 remainder
必须是
\[
 Z_U-(D_{\rm actual}-D_{\rm nn}).                         \tag{10}
\]
这个 correction 包含 diagonal kernel 的 mixed 频块，不能在这里套用
raw rectangular kernel 的 mixed 消失。本文先保留 (10)，第 7 节才付款。

## 3. 原时间概率密度与宽 near 迁移

把原 k 与 chi 的概率平均写成真正的平滑密度
\[
 \nu(\theta)=\frac1{d s_T}\sum_{k=0}^{d-1}
 \chi\!\left(\frac{\theta-T-k\eta}{s_T}\right),
 \qquad \int\nu=1.
 \tag{11}
\]
其支撑严格保留原 floor 和窗口：
\[
 \theta_-:=T+3s_T/8,\qquad
 \theta_+:=T+(d-1)\eta+5s_T/8.
 \tag{12}
\]
所以 `Psi(S)=int e^(i theta S) nu(theta)dtheta`。对每个固定 m，
\[
 \|\nu^{(m)}\|_\infty
 \ll_{\chi,m} X^{-m-1}L^{m/2}.                           \tag{13}
\]
证明：每个 theta 处至多 `O(s_T/eta+1)` 个 k 非零，对 chi 求导后
除以 `d s_T^(m+1)`；`d eta asymp X`，`s_T asymp X/sqrt L`。

置
\[
 v=(A-a)/A,\qquad \delta=64\Delta.
 \tag{14}
\]
以后辅助宽 near 为 `|v|<=delta`。大 X 时原 hard near 包含于此。
新增点必有 `|S|>=Delta`，故 (2) 给 `|Psi(S)|<=X^(-4)`。
对 whole raw 四权，`(sum b_p)^4<<X²/L⁴`；对条件平均块，用
每个 a 的 mod-q 置换范数和至多 q² 个 a，得到
`X^(-4) sum_(q,s)b_qb_s q<<X^(-2)log^C X`。
所以将原 (9) 改到宽 near 的整个 union 只付 `O(X^(-2)log^C X)`。
没有把这个迁移当成逐 a 的无费用改变。

## 4. 两个完整边界族的 unit 付款

按顺序先切 `A<=4X`，然后切 `q-s<=4q delta`；余下为 interior。
估计 raw physical 和条件平均的差，正是 (8) 的 unit 块。

### 4.1 全部 A<=4X

此时 `q<=4sqrt X`，`a asymp A>=X`，且 `|h|<=A delta` 只有
`O(L^(5/2))` 个整数。每个整数 a 的真实 factor pairs 至多 `tau(a)`，
两侧原系数乘积至多 `C_phi/A`。放大 q,s 到整数并用
`tau(a)<<epsilon a^epsilon`，整个 raw 四权族为 `O_epsilon(X^epsilon)`。
此处使用真实产品等式，不能用任意矩形 L1 质量代替。

条件平均块每个 `(q,s,u)` 的 absolute 值至多
`C_phi(A delta+1)/q`。这一族的外权质量为 `O(sqrt X/L²)`，
而 q、s 均为 `O(sqrt X)`，故整个条件平均费用仅为 polylog。
所以全部低产品 unit 族是 `O_(phi,epsilon)(X^epsilon)`。

### 4.2 全部 q-s<=4q delta

这里 `s asymp q`，每个 q 的整数候选 s 有 `O(q delta+1)` 个。
宽 near 和 `p,r<q` 同时强制
`q-Cq delta<p,r<q`，故真实 raw 项数至多
`O((q delta+1)^2)`，四权至多 `C_phi/q²`。
整个 raw 边界为
\[
 \ll_\phi\sum_{\sqrt X<q\le X}\frac{(q\delta+1)^3}{q^2}
 \ll_\phi X^{-1/2}L^C                                  \tag{15}
\]
（最后仅按全部整数 q 求和）。

条件平均块固定 a 的内和是模 q 的加权置换，范数至多 `C_phi`。
其边界 union 因而至多
\[
 C_\phi\sum_{\sqrt X<q\le X}\frac{(q\delta+1)^2}{q}
 \ll_\phi L^C.                                         \tag{16}
\]
这是完整 upper carry 边界付款，未假设短素数间隔。

## 5. Interior 的有限 log-chirp 展开及 whole-line 迁移

以下只在
\[
 A>4X,\qquad q-s>4q\delta                              \tag{17}
\]
使用 Poisson。宽 near `A(1-delta)<=a<=A(1+delta)` 严格位于
`1<a<q²`；原 carry gate 在该支撑中没有截断。

定义
\[
 g(v)=-\log(1-v)-v,\qquad P(v)=\sum_{m=2}^{8}v^m/m.
 \tag{18}
\]
`|theta g(v)|<<X delta²=o(1)`。保留而非丢弃全部 0 到 3 阶：
\[
 e^{i\theta[-\log(1-v)]}
 =e^{i\theta v}\sum_{j=0}^{3}\frac{(i\theta)^jP(v)^j}{j!}
 +O\bigl((X\delta^2)^4+X\delta^9\bigr).
 \tag{19}
\]
Taylor remainder 和 `g-P=O(delta^9)` 分别给两项。
按全部四权质量和全部条件平均 raw norm 聚合，(19) 的整个 union 误差为
`O(X^(-2)L^C)`。只取线性主项不能用这个付款，因为其一阶误差大得多。

写固定有理系数
\[
 c_{jm}=\frac1{j!}[v^m]P(v)^j,
 \qquad c_{00}=1,\quad 2j\le m\le8j\ (1\le j\le3).
 \tag{20}
\]
令
\[
 K(v)=\sum_{j,m}c_{jm}v^m\int(i\theta)^j e^{i\theta v}
 \nu(\theta)d\theta.                                  \tag{21}
\]
这是 Schwartz 函数；chi 光滑，而原 phi 完全未被求导。

还要支付把宽 near K 扩到整条 a lattice 的尾，不能只说 nonstationary。
从 (2) 可推出固定 `0<=r<=3` 的
\[
 |\Gamma^{(r)}(z)|\ll_r e^{-\sqrt{|z|}/32}\quad(|z|\text{大}).
 \tag{22}
\]
一个自足证明是取 8 阶局部插值差分。所有高阶导数的 sup 至多 1
（chi 是支撑于 [0,1] 的概率密度），区间 `[z-1,z+1]` 的函数值至多
`E=exp(-sqrt(|z|-1)/16)`；步长 `E^(1/8)` 给第 r 阶导数
`O_r(E^(1-r/8))`，再弱化成 (22)。对实部、虚部分别应用同一差分。

每个 (21) 的 theta-moment 是 `exp(i(T+k eta)v)` 与
`Gamma^(r)(s_T v), r<=j<=3` 的有限线性组合，其系数为 `O(X^j)`。
在 `|v|>=delta`，
\[
 \frac{\sqrt{s_T\delta}}{32}
 =\frac{\sqrt{64\cdot2048\pi}}{32}L>20L.                 \tag{23}
\]
固定最高次数 m=24 的多项式尾因此足够支付这里需要的固定省幂：
逐点可取 `O(X^(-17)L^C)`，沿 `a` 间距 1 的尾和可取
`O(X^(-16)L^C)`。后一项由正 envelope 的积分加最大值给出，
尺度因子为 `1+A/s_T<<X log^C X`。

对完整 raw products，`a=pr+ell q²` 的额外 aliases 都离 A 至少
delta A；对条件平均块直接用上述全 lattice 尾和与 `q^(-1)`。
两者连同外 q,s 权聚合后的费用为 `O(X^(-10)L^C)`。
这一步完整付清 gate 外整数 aliases；原 near 可以用 whole-line (21)
替换，仅留下 (19) 的 `O(X^(-2)L^C)` 误差。

## 6. 精确单加性频带与全族 chirp 付款

定义一个**不依赖 A** 的有限微分组合
\[
 \mathcal V(\theta)=\sum_{j,m}c_{jm}i^m
 \frac{d^m}{d\theta^m}\bigl[(i\theta)^j\nu(\theta)\bigr]
 =\nu(\theta)+\mathcal V_{\rm corr}(\theta).
 \tag{24}
\]
Poisson summation 与 Fourier inversion 准确给
\[
 \sum_{a\in\mathbb Z}K((A-a)/A)e_c(na)
 =2\pi A\sum_{\ell\in\mathbb Z}e^{i\xi_\ell}
 \mathcal V(\xi_\ell),\quad
 \xi_\ell=2\pi A(n/c-\ell).                             \tag{25}
\]
公式的符号可直接核：`int v^m e^(i(theta-xi)v)dv` 配对光滑密度后给
`2pi i^m D^m`，再乘 Jacobian A 和 `exp(i xi)`。

`0<theta_-<theta_+<2pi A` 由 (17) 与原 (12) 成立。
对代表元 `0<=n<c`，(25) 只可能有 `ell=0`；所以
\[
 F_A(n)=2\pi A e_q(ns)\mathcal V(2\pi sn/q),             \tag{26}
\]
且严格支撑于
\[
 \mathcal I_{q,s}:=
 \left[\frac{q\theta_-}{2\pi s},\frac{q\theta_+}{2\pi s}\right]
 \cap\mathbb Z\subset(0,q^2),\qquad
 n\asymp qX/s,\quad |\mathcal I_{q,s}|\ll qX/s.
 \tag{27}
\]
原 d 的 floor、chi smoothing、正高度均包含在 nu 中。
这里没有扩大观察窗，也没有截去任意 Kloosterman dual。

由 (13)，固定 `j>=1,m>=2j` 给
\[
 \|D^m[(i\theta)^j\nu]\|_\infty
 \ll X^{j-m-1}L^{m/2},\qquad
 \|\mathcal V_{\rm corr}\|_\infty\ll X^{-2}L^{12}.
 \tag{28}
\]
例如最先的 correction 是 `-(i/2) D²(theta nu)`；该项不能直接删掉。

为整个 correction 付款，使用准确带宽中的加性矩阵。若
`alpha=n/q²` 满足 (27)，则
`alpha asymp X/(qs), q alpha asymp X/s>=1, alpha^(-1)<<q`。
对 raw q 行 q 列矩阵 `E_alpha(p,r)=e(-alpha pr)`，TT* 和几何和给
\[
 \|E_\alpha\|_{\rm op}^2
 \ll(q^2\alpha+q+\alpha^{-1})\log(2q)
 \ll(qX/s)\log(2q).                                    \tag{29}
\]
完整证明：Gram 的第 h 条差线至多
`min(q,(2||alpha h||)^(-1))`。把 `alpha h` 的实区间切为整数单位
区间，至多 `O(q alpha+1)` 段；每段是步长 alpha 的点列，靠各整数的
最近点付 O(q)，其余按距离求和付 `O(alpha^(-1)log(2q))`。
Schur row sum 给 `(q alpha+1)(q+alpha^(-1)log(2q))`，即 (29)。
small-denominator coherence 没有被排除：它已经计入 `q alpha~X/s`；
当 alpha 接近 1/4 时，该界可以退化到自然 q 范数。
限制真实 prime graph 的行列 support 后算子范数只会减小，故由 (6)
\[
 |\mathcal B_n|\ll_\phi\sqrt{qX/s}\,\log(2q)^{1/2}.      \tag{30}
\]

将 (26) 的 correction 放入 (9)，`(A/c)*|I_(q,s)|<<X`，得每个
`(q,s,u)` 的 correction 至多 `X^(-1)L^C sqrt(qX/s)`。
所有 q,s 的实际外权完整保留：
\[
 \sum_qb_q\sum_{\sqrt X<s<q}b_s\sqrt{qX/s}
 \ll_\phi\frac{\sqrt X}{L^2}
 \sum_{q\le X}\log q\sum_{\sqrt X<s<q}\frac{\log s}{s}
 \ll_\phi X^{3/2}/L.                                  \tag{31}
\]
因此四个最大标签位置、原同-u 积分的**整个有限 chirp correction union**
满足
\[
 |\mathcal U_{\rm corr}|\ll_\phi X^{1/2}L^C.
 \tag{32}
\]
这是真实块付款。只对每个固定 a 或单个短 prime family 估计，不会得到
本式所需的完整 normalization。

## 7. Graph correction 的完整付款

继续保持 exact (10)，不把其 mixed diagonal 默默归为零。
冻结来源 (24)–(25) 已给整个 `D_nn` union 为
`O_(phi,epsilon)(X^(-1/2+epsilon))`。

对 `D_actual`，可直接使用 456 的**positive majorant 证明**，而不是
从一个 signed 总量的上界推断任意 subset。在 (4)、(5) 中令 `r=p`，
两种共同 profile 均含 `phi(u)^2 phi(u-log p)^2`，所以
\[
 L^{-1}\int_{I_+}\phi(u)^2|A_pB_p|du
 \le b_p^2\frac{\log(X/p)}L.                            \tag{33}
\]
其余 phi 因子至多 1。原 near 内 `S=log(qs/p²)` 非零：
`p²=qs` 与 genuine primes、`s<q,p<q` 矛盾。有限几何核给
`|Psi(S)|<=|K_d^0(S)|<<p²/(X|p²-qs|)`，原四权在 near 中至多
`C_phi/p²`。故每项 absolute 费用至多
\[
 \frac{C_\phi\log(X/p)}{XL|p^2-qs|}.                    \tag{34}
\]
这正是 456 (15) 的已证 positive endpoint majorant。按 p、较小的
q/s 腿作其 (13)、(17)、(18) 的 dyadic 求和，完整族为 `O_phi(1/L)`。
最大性、`p!=s` 等限制只减少这个正 majorant；无需 physical cyclic rotation。
交换两对的另外两个最大标签位置取共轭，absolute 证明不变。

因此整个 actual graph correction，包括其 mixed frequency 部分，已付
\[
 |\mathcal D_{\rm actual}-\mathcal D_{\rm nn}|=o(1).
 \tag{35}
\]
该付款是原 shared-profile union 上的 positive estimate，不是单 q/s
graph 上免费套用 signed trace 结果。

## 8. 最终完整缩约与未付的精确主项

令 `C_int` 是 (17) 的全部 q,s。对 (4)、(5) 分别定义
\[
 \mathfrak L_T^{(\ell)}=
 \frac1L\int_{I_+}\phi(u)^2
 \sum_{(q,s)\in\mathcal C_{\rm int}}b_qb_s\frac{2\pi s}{q}
 \sum_{\substack{n\in\mathcal I_{q,s}\\q\nmid n}}
 \nu(2\pi sn/q)e_q(ns)
 \sum_{p,r}A_p^{(\ell)}B_r^{(\ell)}e_{q^2}(-npr)\,du.
 \tag{36}
\]
真实 p,r primes、q 最大性、s 排除、共同 u 和两个 sharp prime endpoints
全部保留。再恢复原两种 conjugate 最大标签位置，得到 `mathfrak L_T`。
以原 physical half-ratio 的四全异近共振减去冻结来源已付的完整 distinct-nn 块来定义
`mathcal U_T`，则
\[
 \boxed{\mathcal U_T=\mathfrak L_T+O_\phi(X^{1/2}L^C)
                         +O_{\phi,\varepsilon}(X^\varepsilon)+o(1).}
 \tag{37}
\]
wide-near、Taylor、整数 aliases 的误差另为 `O(X^(-2)L^C)`，已包含。
这一步覆盖完整 q,s,a,u union；a 与 q² carry 通过 (17)、(23)–(26)
严格消化，而非从实际数据中删除。

未付任务现在准确是 (36) 的完整 signed union。其正 carrier weight nu
不能令外 `e_q(ns)` 或原 prime bilinear sum 自动正交。即使用 (30)，
本稿点态矩形界聚合仅给 `O(X^(3/2)log^C X)`，所以本文没有用点态
TT* 对主项宣称新 whole 节省。小分母 aliases 与全部 s/profile 权仍在
(36) 中，后续必须利用联合 cancellation 或实际 prime 输入。

本稿观察对象仍为原 chi-carrier signed 平均，不是每个 sigma、平均绝对
块或 canonical scalar `M_T` 的子块。若将来对 (36) 得到有用预算，必须
和冻结 distinct-nn 块、全部已付桥及共同 good-set 的概率分母一起消费。
本次仅有新的完整主频带缩约与 chirp/边界/graph 付款，whole 5/7 基线
和现有比例、引用输入下的 sigma_* 均保持原状。

原 actual whole 四全异量通过已付桥有 half-ratio 的固定因子 2；这不改变
上述幂，但没有令两个观察对象或频块定义直接相同。
自写有限复数求和核对 (8)–(9) 在 q=5,7,11 的归一化和 Fourier 符号，
最大浮点误差为 2.3e-13；它只检验有限恒等式，不认证解析尾、graph
付款或新 whole 上界，也未执行外部 pipeline。
