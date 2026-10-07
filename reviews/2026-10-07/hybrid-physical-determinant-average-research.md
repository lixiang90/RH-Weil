# Physical determinant 联合平均：指定算术主项的完整费用与新增四点条件

2026-10-07。type_ii_joint。从 f76eb72bff841c689ad2de228308720d62d880b7 继续，
起始 worktree clean；未发现仓库及上级 E:/codex-build、E:/ 的 AGENTS.md。
按当前授权只新增本文，math、旧报告、论文和 scripts 未编辑。

状态：§1–6 的有限重排、局部因子、BV/连续体费用为 [T]；
§7 的实际 weighted four-point correlation 是明确 [O] 新输入。
没有取得新的实际 \(o((\log X)^4)\)、四阶常数或零点比例。
本报告给一个具体充分算术条件，不称它必要、最弱或已由无零 package 推出。
指定参考的费用与实际响应的节省是两个不同结论。

## 1. 合并后的原对象：先 pooling，再使用 determinant

保留既有报告的
\[
Y=X^{3/4},\quad L=\log X,\quad N=Y^2,\quad H=N/X,\quad
Q=XL,\quad D=XL+O(1),
\]
\[
K(t)=D^{-1}\sum_{k=0}^{D-1}\cos(2\pi(1+k/Q)t).
\tag{1}
\]
D 是本次原实际整数，不切换到另一个 floor/round 核。
carrier 对应 \(\tau_k=2\pi X+2\pi k/L\)，不删除它。

原 mask 为 \(m(a,b)=\mathbf1_{(a,b)=1}m_0(a,b)\)。
本文只使用已固定的 finite factor-interval / log-ratio aperture cuts；
连续 m0 按这些同一几何公式解释，不把 integer gcd 连续化。
同一 C² 窗口满足 \(0\le\phi\le1,\|\phi''\|_1\ll1\)，
同一 \(H_z=L^2(\mathbb R/L\mathbb Z,dz/L)\) features 是
\[
F_{a,b}(z)=\phi(z+\log(a/b))\phi(z)\phi(\log b-z)^2,\quad
W_{a,b;c,d}=\langle F_{a,b},F_{c,d}\rangle_{H_z}.
\tag{2}
\]
全部变量在一个 fixed balanced cell，范围 \(cY\le a,b,c,d\le CY\)。
凡需要多于这些有限 cuts 的新 ghost mask，不在本报告的 BV 定理内。

保留 236/239 的原 central/dyadic partition：
\[
M=\max(H,Y/H),\quad J_0=[0,M],\quad J_j=[R_j,2R_j],
\quad R_j=2^{j-1}M,
\tag{3}
\]
末段按实际原 partition 覆盖最大 \(|t|=O(X)\)，端点只计一次。
令 \(\kappa_j=|J_j|^{-1}\int_{J_j}K(t)\,dt\)，
\[
K^{\rm cent}(t)=
\sum_j\mathbf1_{\{|t|\in J_j\}}\{K(t)-\kappa_j\}.
\tag{4}
\]
这是同一个原共同线性 projection；没有逐 n、h、channel 自适应选 density。
这里 \(M=H=X^{1/2}\)。若选择另一 usual partition，后文保留 H/M 费用，
不能自动声称同样的小量。

先在每个 physical fiber 合并所有 I/I、I/II、II/II divisor blocks。
既有 completion \(\sum_{r\mid a}\mu(r)B_V(a/r)=\Lambda(a)\) 给精确物理量
\[
\mathcal Q^{\rm cent}=
\sum_{\substack{a,b,c,d\\ad-bc\ne0}}
\frac{\Lambda(a)\Lambda(b)\Lambda(c)\Lambda(d)
m(a,b)m(c,d)W_{a,b;c,d}}
{(4\pi^2)^2\sqrt{abcd}}\,
K^{\rm cent}\!\left(X\log\frac{ad}{bc}\right).
\tag{5}
\]
primitive 两对确保 h=0 恰是原 same-atom reference，准确删除。
proper powers 仍在四个 Λ 中，不能以既有全压缩 Schatten–4 小量
直接删除单 raw cell 的 proper powers。

置 n=bc、h=ad−bc。定义精确 weighted product count
\[
\mathcal R_X(n,h)=
\sum_{\substack{bc=n,\ ad=n+h\\\text{原实际 cell}}}
\frac{\Lambda(a)\Lambda(b)\Lambda(c)\Lambda(d)
m(a,b)m(c,d)W_{a,b;c,d}}
{(4\pi^2)^2\sqrt{abcd}}.
\tag{6}
\]
则
\[
\mathcal Q^{\rm cent}
=\sum_{n}\sum_{h\ne0}\mathcal R_X(n,h)
K^{\rm cent}\!\left(X\log(1+h/n)\right).
\tag{7}
\]
这是全部 a,b,c,d 先共同 pooling 的实际表达，没有 outer absolute sums。
在旧 ghost 参数中 \(n=gvCb,\ n+h=guAd\)，所以原
h=guAd−gvCb 和全部 g,u,v strata 仍准确存在；只有合并后才用 (6)。
没有把稀疏 affine fiber 的 O(1) 整数替换为连续 PNT。

## 2. 明确指定、尚未证明是实际主项的算术参考

为了提出可检验的新相关输入，先固定其主项而完整付款。
连续四变量权重仅将四个 Λ 换成 1、保留 m0/six-window；
integer primitive gcd 不解释成实变量函数。
在 (a,b,n,h) 坐标
\[
c=n/b,\quad d=(n+h)/a,\quad
da\,db\,dc\,dd=\frac{da\,db\,dn\,dh}{ab}.
\]
因此指定连续 density 是
\[
\rho_X(n,h)=
\frac1{(4\pi^2)^2\sqrt{n(n+h)}}
\int\!\!\int
m_0(a,b)m_0(n/b,(n+h)/a)
W_{a,b;n/b,(n+h)/a}\,\frac{da\,db}{ab}.
\tag{8}
\]
所有四个实变量的原 factor cuts 均在积分中保留。
支撑为 n、n+h 都在固定正 compact 倍数的 N 内；
没有取 W=1 或制造新的可自由调整 profile。

下述算术因子由一个有限计算唯一指定。
对 prime p，在四个 unit variables 上计数 \(ad-bc=h\bmod p\)：
\[
\#_p(h)=
\begin{cases}
(p-1)^3,&p\mid h,\\
(p-1)^2(p-2),&p\nmid h .
\end{cases}
\]
若 h≠0 mod p，任选 a 与 b,c，除 bc=−h 外，d 唯一且非零；
若 h=0，三个 unit variables 后 d 唯一。故
\[
\mathfrak S_p(h)=\frac{p\,\#_p(h)}{(p-1)^4}
=\begin{cases}
p/(p-1),&p\mid h,\\
p(p-2)/(p-1)^2,&p\nmid h .
\end{cases}
\tag{9}
\]
对非零整数 h，定义
\[
\mathfrak S(h)=2C_2\,\mathbf1_{2\mid h}
\prod_{\substack{p\mid h\\p>2}}\frac{p-1}{p-2},\qquad
C_2=\prod_{p>2}\left(1-\frac1{(p-1)^2}\right)>0.
\tag{10}
\]
有限坏素数由给定 h 的除数准确保留，不假定它们随机。

指定参考 response 为
\[
\mathcal Q_{\rm loc}^{\rm cent}
=\sum_n\sum_{h\ne0}\mathfrak S(h)\rho_X(n,h)
K^{\rm cent}\!\left(X\log(1+h/n)\right).
\tag{11}
\]
这不是已证明的 prime-pair asymptotic 或新的外部输入。
把 \(\mathcal R_X\) 与 \(\mathfrak S\rho_X\) 联系起来，
包括原 gcd mask、四个 Λ、proper powers 和所有 repeated sectors，
正是 §7 的未付四点条件；局部 residue count 本身没有完成它。
没有定义 \(\mathfrak S(0)\)，h=0 全部按原 reference 删除。

## 3. 算术因子的全前缀平均：O(log²) 而非逐 h 绝对值

令 α(d) 为 odd squarefree d 上的 \(\prod_{p\mid d}(p-2)^{-1}\)，
其余 d 上为 0，α(1)=1。Euler products 给
\[
\mathfrak S(h)=2C_2\mathbf1_{2\mid h}\sum_{\substack{d\mid h\\d\ {\rm odd}}}\alpha(d),
\qquad \sum_{d\ge1}\frac{\alpha(d)}d=C_2^{-1}.
\tag{12}
\]
绝对收敛由 α(d)/d 的 prime departures \(1/[p(p-2)]\) 可和。
又 \(\alpha(d)\le3\tau(d)/d\)，因为 p≥5 时 p/(p−2)≤2，
只有 p=3 需要一个固定额外常数。因此
\[
\sum_{d\le T}\alpha(d)\ll\log^2(2T),\qquad
\sum_{d>T}\frac{\alpha(d)}d\ll\frac{\log(2T)}T.
\tag{13}
\]
第一式由双 harmonic sum，第二式由
\(\sum_{d\le u}\tau(d)\ll u\log(2u)\) 的 Abel 求和。
现在
\[
\sum_{1\le h\le T}\mathfrak S(h)
=2C_2\sum_{d\le T/2}\alpha(d)\left\lfloor\frac T{2d}\right\rfloor
=T+O(\log^2(2T)).
\tag{14}
\]
负 h 用 evenness。故对任意 compact BV 函数 f，支撑 \(|h|\le C N\)，
\[
\left|\sum_{h\ne0}(\mathfrak S(h)-1)f(h)\right|
\ll L^2\{\|f\|_\infty+\operatorname{Var}f\}.
\tag{15}
\]
这是保留 arithmetic divisor structure 的联合平均。
若先对每个 h 取 \(|\mathfrak S(h)-1|\)，将失去 (14) 的付款。

## 4. 原有限 carrier 的 BV 和均值费用

fixed cell 的 atoms 和最后 shell 的 endpoints 均有
\(|t|\le C_0X<Q/2\)（充分大 L），故无 grid alias。
准确 geometric sum 为
\[
\mathcal K(t)=D^{-1}\sum_k e^{2\pi i(1+k/Q)t}
=e^{i\pi(2+(D-1)/Q)t}
\frac{\sin(\pi Dt/Q)}{D\sin(\pi t/Q)},\quad K=\Re\mathcal K.
\tag{16}
\]
在 \(|t|\le1\)，直接有限求和给 K、K′ 一致有界；
在 \(1\le|t|\le C_0X\)，分母 \(\asymp|t|\)，对上式求导给
\[
|K(t)|\ll |t|^{-1},\qquad |K'(t)|\ll |t|^{-1}.
\tag{17}
\]
carrier 的导数必须保留，它正贡献 O(1/|t|)，不是 O(1/t²)。

原 κ 的较强均值也可保留有限整数 D 严格证明。
对 endpoint T，weight \(1/(1+k/Q)\) 的总 variation 有界；
对精确 geometric sum 作 discrete Abel，
\[
\left|D^{-1}\sum_k\frac{e^{2\pi i(1+k/Q)T}}{1+k/Q}\right|
\ll\min(1,1/|T|).
\]
应用 κ 的原 sine antiderivative，得到
\[
|\kappa_0|\ll M^{-2},\qquad |\kappa_j|\ll R_j^{-2}\quad(j\ge1).
\tag{18}
\]
中央的 0 endpoint 的 sine 准确为零。
因此 shellwise 常数的总跳跃有界，并且
\[
\|K^{\rm cent}\|_\infty\ll1,\quad
\operatorname{Var}_{[-C_0X,C_0X]}K^{\rm cent}\ll L,\quad
\int_{-C_0X}^{C_0X}|K^{\rm cent}(t)|dt\ll L.
\tag{19}
\]
这些全是实际 finite carrier 的费用；没有改成连续频段或删尾部。

## 5. 原权重的 BV 与 lattice / continuum 交换费用

由原 finite factor/aperture cuts 及 C² 窗口，
\[
0\le\rho_X(n,h)\ll N^{-1},\qquad
\operatorname{Var}_h\rho_X(n,\cdot)\ll N^{-1}.
\tag{20}
\]
证明：固定 n,a,b 时 c 固定、d=(n+h)/a 随 h 单调；
每个 factor/aperture cut 只经过固定数目的 edges。
各 window 的 h-derivative为 O(1/N)，prefactor也在该正 compact 域中有
O(1/N) 总 BV。积分 \(da\,db/(ab)\) 在 fixed log rectangle 上总质量 O(1)，
normalized dz/L 不增加 L。由周期性
\(\|\phi'\|_\infty\le\|\phi''\|_1\ll1\)，故 uniform 常数合法。

结合 (19)，
\[
f_n(h)=\rho_X(n,h)K^{\rm cent}(X\log(1+h/n))
\]
的 sup 为 O(1/N)、BV 为 O(L/N)。
单变量 BV lattice summation 于是给
\[
\sum_n\left|\sum_h f_n(h)-\int f_n(h)\,dh\right|\ll L.
\tag{21}
\]
这里只对一个已显式证明小量的 reference quadrature error 求绝对值，
没有对实际 prime-product error 作 outer absolute estimate。
删除 h=0 reference 的总费用为 O(1)。

还须支付 n 的离散化，不能默认为 n 已经连续。
令 t=X log(1+h/n)，则
\[
\gamma_n(t)=\frac{ne^{t/X}}X\rho_X(n,n(e^{t/X}-1))
=\frac{e^{t/(2X)}}{(4\pi^2)^2X}
\int\!\!\int m_0(a,b)m_0(n/b,ne^{t/X}/a)
W_{a,b;n/b,ne^{t/X}/a}\frac{da\,db}{ab}.
\tag{22}
\]
固定 t 时 c,d 都随 n 成比例，c/d=a/(be^{t/X}) 不依赖 n；
factor cuts 和 log d windows 给
\(\operatorname{Var}_n\gamma_n(t)\ll1/X\)。
故由 (19) 和 BV quadrature，
\[
\left|\sum_n\int f_n(h)dh-\int\!\!\int f_n(h)dh\,dn\right|
\ll L/X.
\tag{23}
\]
所有 sharp shell endpoint 仍取原 convention，BV 控制包括其 jumps。
没有对 curved determinant mask 宣称 old straight-ratio Mellin 准入。

## 6. 指定算术参考的完整 fixed-cell 付款

连续 uniform term 的 raw response 有真实 Gram 形式。置
\[
P_z(\tau)=\frac1{4\pi^2}\int\!\!\int
\frac{m_0(a,b)F_{a,b}(z)}{\sqrt{ab}}e^{i\tau\log(a/b)}\,da\,db .
\]
连续原 K response 准确为 \(D^{-1}\sum_k\int|P_z(\tau_k)|^2dz/L\)。
固定 b，a-slice 的有限 edges 和 window 导数允许一次 integration by parts；
每个 a integral 的费用 \(\ll\sqrt Y/|\tau|\)，再对 b 积分给
\[
|P_z(\tau_k)|\ll Y/X,\qquad
|\mathcal Q_{\rm unif,cont}^{\rm raw}|\ll N/X^2.
\tag{24}
\]
这是指定连续体积分的 oscillatory estimate，不是两条 sparse prime forms 的 PNT。

由 (22) 积分 n，连续 log-frequency density
\(\Gamma_X(t)=\int\gamma_n(t)dn\ll N/X=H\)。
共同 κ subtraction 的中央质量至多 O(HM)、dyadic 质量 O(HR_j)；
(18) 给全部费用 O(H/M)。结合 (21)–(24)，
\[
|\mathcal Q_{\rm unif,lattice}^{\rm cent}|
\ll L+N/X^2+H/M.
\tag{25}
\]
再用 (15)、(20)、(19)，对每个 n 的算术项费用 O(L³/N)，
实际 n 数量 O(N)，得到
\[
\boxed{\ |\mathcal Q_{\rm loc}^{\rm cent}|
\ll L^3+N/X^2+H/M.\ }
\tag{26}
\]
原 M=H，因此指定主项是 \(O(L^3)=o(L^4)\)。
全部 h 正负、|h|达到 O(N) 的 tails、原 masks/windows、finite carrier、
same-atom 删除和 common density 项已在该 reference 付款中保留。
它不是实际 \(\mathcal Q^{\rm cent}\) 的无条件界。

## 7. 不取 outer absolute values 的具体新增算术条件

将 (6) 和 (11) 的两种 weights 以
\(T_{n,h}=|X\log(1+h/n)|\) push forward，分别记 \(\nu_X,\nu_{\rm loc,X}\)。
actual ν 包括原四 Λ、两个 primitive masks 和所有 physical quadruples；
reference ν 的主项按 (8)–(10) 预先固定。
这两个 measure 都不依赖 k、D 或 carrier。重复 ratios 按真实质量相加。

对每个原 J_j=[A_j,B_j]，先令
\[
\mathcal D_j(T)=
\nu_X(J_j\cap[A_j,T])-\nu_{\rm loc,X}(J_j\cap[A_j,T]),
\]
再用原同一个 linear shell projection 定义
\[
\mathcal E_j(T)=\mathcal D_j(T)
-\frac{T-A_j}{B_j-A_j}\mathcal D_j(B_j),\quad
A_j\le T\le B_j,\qquad
e_j=\sup_T|\mathcal E_j(T)|.
\tag{27}
\]
端点严格/inclusive convention 与原整数 partition 一致。
原 P_J 是固定的线性 operator；这里只对 actual-minus-reference 用它，
没有另选 n-dependent 或 channel-dependent projection。
特别 \(\mathcal E_j(B_j)=0\)；不要求实际 shell 总质量与参考相差 O(L²)，
因为这种额外强条件对共同 centered response 没有必要。
条件涉及实际正计数的差异，不是原 oscillatory response 的换名：
它对该 shell 内所有前缀要求 uniform bound，且不含原 kernel/carrier。
曲线 cutoff 在原变量就是
\(|\log(ad/bc)|\le T/X\)，不把它改成 fixed h interval 或直线 u/v mask。

一个明确充分的新 four-point correlation 输入是
\[
\boxed{\quad e_0\log(2M)+\sum_{j\ge1}e_j=o(L^4).\quad}
\tag{28}
\]
更强但易陈述的具体目标为 \(e_j\ll L^2\) uniformly，
因为原 shell 数 O(L)，则左边 O(L³)。
与此前 flat-density certificate 不同，这里先显式扣除原几何的
非恒定 continuous density 和完整 arithmetic divisor main，
并由 (26) 直接支付其 response；没有把其曲率或奇偶/divisor波动误记为
prime-correlation error。原 common centering 始终不变。

证明条件如何接入：对 signed δν=ν−νloc，原 constant-density part 满足
\(\int_J(K-\kappa_j)dP_J\delta\nu=0\)。
因此在每个 J 的 Stieltjes partial summation 给
\[
\int_{J_j}(K-\kappa_j)d\delta\nu
=-\int_{A_j}^{B_j}K'(t)\mathcal E_j(t)\,dt .
\]
中央费用 O(e0 log(2M))，dyadic 各 O(ej)，由 (17)–(18)。
因此实际、严格的条件估计为
\[
\boxed{\ |\mathcal Q^{\rm cent}|
\ll L^3+N/X^2+H/M+
e_0\log(2M)+\sum_{j\ge1}e_j.\ }
\tag{29}
\]
这先合并全部 a,b,c,d 及 divisor signs，再估计共同累计差；
没有 Σ_A,C,b,d absolute PNT error，也没有逐 h 绝对累计局部因子。
若 (28) 被真实证明，则 fixed cell 满足 \(o(L^4)\)，
条件界确实强于当前无条件 \(X^{1/2+\eps}\) 基线。
本轮没有证明 (28)，所以不登记实际节省。

既有 θ<1 的 [R] 能处理已准入的 canonical μ/Λ twists，
但没有证明四 Λ 的 (27)。本报告未调用新的 [R]。
若尝试用 Mellin/Fourier 来证明 (28)，必须单独支付这些 exact curved prefix 的
endpoints、moving seminorm 和全高度费用；旧 straight log-shell 准入不自动覆盖。
上述接入证明只用 finite carrier 的 BV，不藏未付的无限高度积分。

## 8. 逐 n 的 uncentered absolute error 有实际 support 障碍

这个错误有实际 support 障碍。假设普通 cell 的连续 density 在某个
固定 scaled rectangle \(n/N\in I,\ h/N\in J\) 内严格正。
这是窗口和 cuts 有非空重叠 interior 的情形。
对 n≡0 mod 3，actual Λ(b)Λ(c)≠0 要求至少一因子是
位于 balanced range 的 \(3^k\)；这样的 k 只有 O(1)，对应 n 总数仅 O(Y)。
因此 I 内正比例的 n 完全没有 actual product support。

而对这些 n，(8) 的 \(\rho_X\ge c/N\) 在一段长度 cN 的 h 区间上；
偶数 h 的 \(\mathfrak S(h)\ge2C_2>0\)，其 reference prefix mass至少一个固定正数。
若对每个 n 单独比较并取 uncentered absolute prefix error，再把 n 求和，
则该费用 \(\gg N\)。不能以全导子 one-point PNT 修补这个 support 空洞。
这否定的是该 uncentered per-n 替代方案，不能据此否定所有 centered per-n
估计。这里应优先研究 (27) 那样的 product-base 与 determinant 联合平均。
这是实际 support 的有限/渐近计数，不是自拟 random-sign 模型。
它不排除其它 genuine joint estimates，也不声称 (28) 不可能。

## 9. 防错证据、余额及下一动作

stdout-only 的有限 Fraction 枚举在 p=2,3,5,7,11,13 上核对
四 unit variables 的 determinant residues，共 41 个 residue 检查全部满足 (9)。
有限 Euler product 在完整 period 30030 上的因子总和准确为 30030；
所有运算有理，无浮点、无文件写入。
这只验证局部恒等式与 finite mean-one，不证明 actual prime correlations。
(13)–(29) 的无限量词证明在正文，不以 finite period 外推。

仍未完成：

- 真实四点相关 (27)–(28)，包括原自然 masks、proper powers、repeated sectors；
- all-cells / 跨cell alias、其他 signed words 与背景及原四阶常数；
- 从 fixed-cell 条件估计向完整 AF finite-frame 比例链的 uniform 总账。

这里 fixed-cell 无 alias 来自其 O(1) log-ratio跨度，不能扩大到整条 L-period。
原已付 low-prime / proper-power 全压缩费用继续按原证据使用，
不重复算为本轮的比例节省。

下一有效动作是直接研究 (27) 中 pooled product correlations：
在 h-average 中保留 prime-denominator incidence 和 all-divisor completion，
或给整个 cumulative error 一个真正共同的 dispersion 估计。
证明一个 kernel-free \(O(L^2)\) uniform 累计余量比再做 fixed-W 准入更具体；
但其强度是一个尚未取得的新算术结论。
若不能在该方向取得新前向不等式，应报告缺口并换实际机制，
不将 (26) 的 reference 付款当成实际费用已经闭合。

依赖：[原 joint affine/completion](hybrid-joint-type-ii-fiber-research.md)、
[已付 moving-shell 与 centered 基线](hybrid-residue-averaged-type-ii-research.md)、
[236 mass ledger](../../notes/236-elementary-power-high-mass-ledger-closure.md)、
[239 quotient-first centering](../../notes/239-vaughan-quotient-first-centering-and-divisor-kernel.md)、
[241 physical-fiber-first](../../notes/241-divisor-scale-separation-no-go.md)。
Goal 仍 active，论文交付、指定主项付款或一个充分条件均不构成完整目标完成。
