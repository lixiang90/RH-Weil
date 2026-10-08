# Yang–Yang 79.62%：无穷解析引擎的独立审查

日期：2026-10-08。审查对象是原有限 Weil 矩阵的矩极限如何抵达
四、五、六阶模型常数；此文件不重新认证有限有理证书，也不执行外部代码。

结论：固定版本的解析论证尚不足以把 79.62% 当作已经证明的零点比例。
两个首要缺口是原 cell 权到 log-modulus 截断的换量，以及真正
`N_4(k,j)` 方差到 FFT 自相关卷积的带权传递。后者可以用独立代数检查
证明不存在文面暗示的通用等式。这里没有证明整个几何定理为假；缺口可能
由新的专门桥填补，但当前原文、公开代码和有限 faces 没有提供该桥。

## 1. 固定来源与核对范围

GitHub 固定提交为
[`d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`](https://github.com/JoshuaHKU/zeta-0.7947-reproduction/tree/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8)，
提交时间 2026-08-18 01:30:39 UTC。以下行号均指这个提交的
[`paper.tex`](https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/paper.tex)。
该文件按末尾换行计为 2893 行。

已读 §5 cell-mass/truncation、§7 Lemma D 的 frame/Parseval 和三个 arc
leaves、§8 product/W1–W3 与高阶传递、§9 consumption、§11 verification、
Appendix A comb，以及相关原矩阵和第三、第四矩定义。

固定提交的 `paper.pdf` 与
[Zenodo 21975237 的英文 PDF](https://zenodo.org/records/21975237)
均为 598532 bytes，内存只读比对的 MD5 均为
`0811e74faaffe8ef7b216cc004481eb5`，所以本审查针对同一英文稿件。
未执行未知 Lean/Python/GPU pipeline；数值诊断仅用自己编写的有限求和。

作者在 paper.tex 2067–2076、2096–2106、2210–2229 明确把解析层标为
pre-Lean/pre-review 的 certified-candidate，并把 external review 留在记录
准入条件中。这个自我分级是正确的阅读边界；本审查不借 GitHub issue 的
判断代替逐式核查。

## 2. 原对象的 cell 权与截断合同

原第四矩残差 `R` 在 760–766 行是

\[
 N_1=b_1m_1\ne N_2=b_2m_2,\qquad
 \frac{\Lambda(b_1)\Lambda(m_1)\Lambda(b_2)\Lambda(m_2)}
 {\sqrt{N_1N_2}}\,
 \widehat W\!\left(\log\frac{N_1}{N_2}\right)O_4,
\]

最后除以 `d ell_1^4`，其中 327–328 行已经定义
`ell_1=log(T/(2pi))+2log2-1`。这是对所有 cells 共同的全局高度归一化。
1074–1075 行写出的 continuum outer weight 则为

\[
 \frac{\Lambda(b_1)\Lambda(b_2)}{b_1b_2}F_\infty(b_1,b_2).
\]

公开计算也直接保留这个外权：
[`scripts/g1_ledger.py`](https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/scripts/g1_ledger.py)
354–355 行；196 行的实际带账本权是 `norm*Lambda(b1)*Lambda(b2)*Q/N`。
[`scripts/babs_mean.py`](https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/scripts/babs_mean.py)
89–116、219–247 行也直接从原四腿权和核生成 cells。

与此相比，1127–1182 行的 truncation 证明使用

\[
 \ell^{-k}\cdot\ell\cdot\ell^\varepsilon,
 \qquad \sum_{\ell>P}\ell^{-k+1+\varepsilon}
 \ll P^{-(k-2)+\varepsilon}.
\]

这里没有定义一个独立于全局 `ell_1` 的 cell 参数，也没有给出从原
`(b_1,b_2,m_1,m_2,j)` 到这个参数、权、体积和 multiplicity 的公式。
因此有两种均未完成的解释：

* 若 `ell_1` 仍按 327 行的定义，`ell_1<=P` 是全局高度条件，不能选择
  小模数 cells；共同除以 `ell_1^k` 不能带来 cell 尾部衰减。
* 若这里另指 lcm/product 等 cell 参数，必须重新定义并证明换权。
  例如 coprime `b_1,b_2` 的 lcm 是 `b_1b_2`，原外权只含其倒数，
  不能直接改成其负四次方。若参数是 `max(b_1,b_2)`，固定大素数最大值
  仍允许大量第二条素数腿，所谓 divisor-bounded multiplicity 也不自动成立。

这不是符号修正即可完成的证明：还要保留所有 sharp cutoffs、prime-power
腿限制、row/column overlap、原 finite-P 核以及剩余 deviation。
1172–1179 行的另一个 D1 singular-series 尾估计不能自动替代原素数权的
这个截断；两种截断对应的变量和对象本来就不同。

### 2.1 必要诊断：bare moduli 质量并不集中在 polylog 范围

令

\[
 M(X)=\sum_{b\le X}\frac{\Lambda(b)}b=\log X+O(1).
\]

独立、有序的裸外权总质量是 `M(X)^2`。若保留
`b_1,b_2 <= P=(log X)^B`，其质量仅为
`M(P)^2=O_B((loglog X)^2)`，保留份额趋于零。无序、同腿修正不改变
主阶，因为 `sum Lambda(b)^2/b^2` 收敛。只要求 `b<=X^delta` 时同样有
主阶 `delta^2(log X)^2`，所以这不是仅由最顶端极稀疏模数造成的现象。

自写筛法计入所有 prime powers，取 `B=2`，得到：

| X | floor((log X)^2) | M(X) | M(P) | 保留裸外权份额 |
| ---: | ---: | ---: | ---: | ---: |
| 1000 | 47 | 6.32875144 | 3.32239280 | 0.27559154 |
| 10000 | 84 | 8.63463931 | 3.88802841 | 0.20275448 |
| 100000 | 132 | 10.93626215 | 4.31832909 | 0.15591706 |
| 1000000 | 190 | 13.23789253 | 4.65331960 | 0.12356289 |

这仅反驳裸权的“trivial tail”解释；它不是整个带核、带几何、有符号定理
的反例。一个有效证明仍可能由几何或联合 cancellation 取得小尾，但必须
对该完整对象证明，不能把裸外权当作归一化概率质量。

### 2.2 overlap 支持没有排除全部大腿

公开 `o4_block` 的三个 overlap 项，在四腿对数均为 `alpha L` 时给出

\[
 \frac{O_4}{L}=(1-\alpha)+2(1-2\alpha)_+.
\]

例如 `alpha=0.6,0.8` 时分别为 `0.4,0.2`。微扰到非等产品的连续几何邻域
仍有正 overlap；所有腿也都满足原 sharp `n<=X`。
因此原几何并没有一个“所有大模数 cell 均消失”的支持性质。
这个连续支持检查没有声称特定算术近共振族有正下界，也没有测量其净残差。

所谓 `P^{-(k-2)}` 即使得到证明，取 `P=(log X)^B` 后也是 log saving。
它可以支付常数矩极限所需的某些 `o(1)`，但不是本项目 whole 指数所需的
`X^{-delta}` 省幂；必须说明最后消费归一化再作比较。

## 3. 三个不同的锁对象

547–566 行定义的真正四点锁数为

\[
 N_4(k,j)=\sum_{m,n}
 f(m)f(m-rk)g(n)g(n-qk)
 \mathbf1_{b_1n-b_2m=j},
\]

其中实际 `f,g` 是各自窗口内的 von Mangoldt 序列。
固定 `k,j` 后，若 `gcd(b_1,b_2)|j`，全部解可写为

\[
 m=m_0+r t,\qquad n=n_0+q t.
\]

所以未归一化的共同窗口体积是一维的 `t`-长度，至多
`min(Y_m/r,Y_n/q)`。563、1140 行的 `Y^2/(rq ell_1)` 若指另一种
consumption-normalized volume，必须给出这层换量，不能直接把它当成
原固定 `(k,j)` 的几何计数。

1265–1277 行的 FFT 对象却是

\[
 \rho(\tau)=\sum_t A_f(t)A_g(t-\tau),
 \qquad A_f(t)=\sum_x f(x)f(x+t)
\]

（实际须把 `f,g` 放在 `b_2 m,b_1 n` 的 position lattices）。
设两点 lock density `B(j)=sum_{b_1n-b_2m=j} f(m)g(n)`，则
`rho` 自然是 `B` 的自相关；这是一个自由的“两个 lock 差为 tau”对象。
在完整 shift 范围中，`sum_k N_4(k,j)=B(j)^2`。
这给出 `sum_{k,j}N_4(k,j)=rho(0)`，并不给出
`sum_{k,j}N_4(k,j)^2=sum_tau rho(tau)^2`。

1445–1456 行的 product identity 另有合法范围：对四条位置链，全部三个
lock 坐标自由求和时，平方范数为 `sum_t A_f(t)^2 A_g(t)^2`。
“全部 lock 自由”与原 `k,j` 的共享 affine 约束并非相同索引集合。

### 3.1 独立有限代数核

取 `b_1=b_2=r=q=1`，`f=g=1_{ {0,1} }`；完全枚举整数 `k,j,t,tau`：

\[
 \sum_{k,j}N_4(k,j)^2=8,
 \qquad
 \sum_\tau\rho(\tau)^2=70,
 \qquad
 \sum_tA_f(t)^2A_g(t)^2=18.
\]

第一项由 `k=0` 的 `6` 和 `k=+-1` 的各 `1` 组成；仅取 `k>0` 时为 `1`。
`A=(1,2,1)`，`rho=(1,4,6,4,1)`，所以每个数都能手算复核。
这是对通用恒等式的反证，不是对 von Mangoldt 带权几何定理的反例。
若原文的 “carried by” 指非平凡 inequality 或专门受限迁移，需要写出该
inequality、主模型、常数及每项损失，并保持原 masks。

### 3.2 原 local law 也显示模型不能直接混用

固定 `b_1=b_2=1,k=2,j=4`，原四个共享形式的偏移是
`{0,-2,4,2}`，模 3 覆盖全部三个 forbidden residues，所以四点 all-unit
local density 为零。两个独立 shift-2 twin 链，各自却仍有一个 allowed
residue，局部密度乘积为正。

因此 Appendix A 的 twin-product tau-comb 可以是其自身自由相关对象的
正确模型，却不能直接取代原 fixed `(k,j)` 的四共享形式 singular series。
这一点需要实际 lock 分解，不能仅靠 CRT 正交或 local mean-one 解决。

## 4. 公开 faces 验证了什么

[`pipeline/face_parseval.py`](https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/pipeline/face_parseval.py)
21–28 行先定义 `rho=irfft(dens)`，再比较其平方范数与同一个 `dens` 的
Parseval 范数。这是正确 FFT 恒等式；代码没有生成 `N_4(k,j)`，也没有
验证它到 `rho` 的桥。

[`pipeline/face_dispersion.py`](https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/pipeline/face_dispersion.py)
26–71 行构造自由 tau-profile 和 two-twin CRT model；74–87 行测量有限
高度 profile tracking。该 face 与其自己的数学对象匹配，却不是原 theorem
1369–1372 行的 fixed `(k,j)` residual variance。

[`pipeline/face_arcs.py`](https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/pipeline/face_arcs.py)
70–100 行的 measured mixed mass 和 budget 针对 `am2*an2`，而 Lemma D
谱平方距离需要 `(am2*an2)^2` 及 model subtraction。
所以其 24–31 倍 tightness 不能认证所需高次 L2 stratum budget。

[`certification/writeouts_verification.py`](https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/certification/writeouts_verification.py)
的 W1（92–132 行）实际只构造三条序列，111–117 行检验一维 Parseval，
并检查 `x,z` 同在 `b_1` lattice 时的 `t_2` CRT support contrast。
这不是 1624–1643 行所消费的完整 `(b-1)` 维残差 comb 方差。
W2 的 55–56 行在左右两边重写同一 `pair*mass` 算式；这验证可分离 toy
对象的 Fubini，不验证 actual finite-P trace ledger 的 free-slot 迁移。
W3 测量四组三个固定 twin sums 的乘积，没有原 joint geometry 的 remainder。

[`pipeline/face_b5_frame.py`](https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/pipeline/face_b5_frame.py)
54–58 行与
[`pipeline/face_b6_frame.py`](https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/pipeline/face_b6_frame.py)
92–97 行都把相同的 exact zero-shift diagonal 加到 empirical/model 中。
其 relative tracking 可能被该共同 diagonal 稀释，因而必须另报告 off-diagonal
误差预算；现代码不能据此单独认证 connected residual 的极限。

这些 faces 本身不是坏测试。问题在于将它们的有限对象/有限精度范围升级
为另一完整解析对象的证明。作者在 2056–2062 行也正确承认 faces 不能
验证渐近式。

## 5. SW/Vaughan leaves 与 glue 的最小缺项

对真正长窗口 `Y asymp X`，小模数 major arcs 的单素数和
Siegel–Walfisz + partial summation，以及 Vaughan 的 minor pointwise
估计，都是可用的经典输入。但单因子的正确估计不等于原 joint lock
方差已完成。

1322–1345、1378–1394 行没有写出在所需 squared spectral measure 下的
stratum cardinalities、image spacing 损失、各 `Y,b_i,N` 次幂与 model
误差总和。公开 `face_arcs` 如上测量的是较低次对象。
要填补这一项，至少需要明确证明完整 model-subtracted L2 预算，并把
`K J V^2` 的归一化准确还原到原残差消费。

1366–1367 行还把窗口扩展到 `Y=X^vartheta, vartheta>1/2`。
普通长区间 SW 的误差是以起点尺度 `X` 计量；换成短窗口差分，并不自动
给出相对于 `Y` 的任意 log saving。普通 Vaughan 全前缀估计含
`X^(4/5)` 项，也不能直接支付所有 `vartheta>1/2` 的 `Y`-归一化。
如果只保留 `Y asymp X` 可以避开这项额外扩大，但不能修补 cell/lock 桥。
若保留全 stated range，必须给出适用该长度的原定理与参数匹配。

1016–1020 行的实际 glue 为
`w_k(n)=sum_{m in I(n)} Lambda(m)Lambda(m-rk)`。
这个权含 prime correlations，且端点由共同 lock/strip 决定。
“Abel summation against the glue”需要实际总变差或相应加权范数估计；
“exact factorization of main terms”只处理模型项，不能抹掉与 prime errors
的 covariance。原正文没有完整 remainder 公式及跨完整 family 的预算。

最小可审阅补充不是再列单素数 SW，而是：保留 `w_k(n)`、所有 shared
cutoffs 和原 local model，给出一个带权 joint deviation lemma，证明其
在原 `R` 归一化后为 `o(1)`。若用 smoothing，必须另外支付 sharp collar
和整个 family 的损失。

## 6. m3–m6 到原有限矩阵的传递

原有限矩阵使用 `0<=k<d`（385–398 行）；Poisson identity 却对全部
`k in Z` 成立（400–413 行）。三阶证明 701–738 行直接在 collapse 后
开始类账本，非标准 locality/calibration 和 tail adaptation 的细节指向
`V1_completion.md`。固定公开树没有该 memo，也没有原 D1/consumer/glue
完整 write-outs。这个公开可审阅范围缺失须记录，不能自动断言未公开证明
不存在。

一般原 trace 需要保留

\[
 K_d(\tau,\tau')=
 \sum_{0\le j<d}\widehat\phi(\tau-\tau_j)
 \widehat\phi(\tau'-\tau_j),
 \qquad
 K_\infty=L\Phi(\tau-\tau').
\]

用 `K_infty` 替代每个 `K_d` 后，必须在实际 prime-side measure 和产品
kernel 下，逐项支付 boundary/error；二阶校准不自行认证高阶 near-product
或 finite-P carry。高阶 operator 插入还须有合适的 Schatten/trace 控制。

1460–1465、1624–1643 行把四阶谱法 factor by factor 传到 k=5,6，
但仍消费未完成的 truncated actual-ledger 合同和锁映射。
1478–1503 行的 Bell/anchor assembly 与 1660–1704 行的 rational polytope
积分可以正确计算模型常数，却不能自行证明原算术 trace 具有这些常数。
尤其 “odd-block classes vanish by the local law”需要实际 connected-class
identity；1200–1209 行的 positive coincidence density/mean-one 本身并不
给出奇阶 connected residual 消失。模型网格上 `{3,3}=0` 也不能代替这一桥。

必要的终端合同可以写成：对原 finite matrix，在明确极限顺序和全部 masks
下，证明 `mu3=2+o(1), mu4=13/4+o(1), mu5>=101/18-o(1),
mu6<=12809/1260+o(1)`，且每个 `o(1)` 是带已支付 family norm 的 bound。
获得这个合同之后，有理平方多项式证书的消费才合法。此次解析审查不认证
证书层本身，也不把这些未付前件当成已知输入。

### 6.1 69.16% 单侧路线须独立判定

884–910 行的 `0.691615/0.845807` 路线先于 §5 truncation 和 §7 Lemma D，
且 875–882 行明确说逻辑独立。因此不能把 Proposition 5.3 的证明缺口直接
当成这一单侧路线的反证。

该路线自身仍有明确未付的数值到渐近桥：1063–1068 行的有限高度
`tail<=0.0111`、`core(2400/4800)`，以及 1070–1109 行的 continuum
convergence/universality 和保守 `core<=-0.0055+0.0010` charge，最后在
1114–1122 行被消费成 `limsup R<=0.0066`。
1100–1106 行承认常数 bands 不是 certified enclosures，quadrature
certification 是 named open item。有限网格的递减/追踪不能独自证明该
保守 bound 对所有充分大 T 成立。还须公开完整 glue/consumer estimates，
并给出可审阅的 convergence rate、统一 tail bound 与最终上界。
这是一条独立的 certified-candidate 路线；当前材料同样不足以把其较小
比例当作已经建立的纪录，但本审查没有证明其比例命题为假。

## 7. 对 RH-Weil 原路线的可用启发与准入边界

可以借用的结构是：按实际 affine locks 做精确有限身份、先扣共同
diagonals、分别认证模型 polytope 常数和算术 remainder，再用符号正确的
高阶矩证书消费。所有 faces 应同时给出原对象与变换对象的独立计算，
而不只从同一 FFT 或已因子化公式重建左右两边。

不能借用为已付接口的是：把原 `Lambda(b1)Lambda(b2)/(b1b2)` 外权当成
带负四次幂的 log-truncatable cell 概率；把 free-lock tau-comb 当作
fixed `(k,j)` 方差；用模型 connected 常数的 exact-rational 认证替代
whole prime-family signed deviation。

本项目当前已付的是实际 chi-carrier signed double-nonunit 块，未付的是
完整 unit/unit physical block、其 q² carry、四 distinct graph 扣除和共同
profile 下的 joint union。Yang 解析层没有提供可覆盖这类完整大模数
unit family 的新上界，SW 的 polylog 模数范围也不会从裸外权自动扩展。
因此本审查不改变 whole `5/7` 基线、不改善简单比例、不代入 kappa，
也不把其 79.62% 算作本项目可调用的公开同口径已证纪录。

最先值得推进的实质工作是一个实际带权截断或 true-lock bridge。
如果只能证明模型/自由锁对象，该结果应保留在这一范围；若能证明完整
signed remainder 省幂，才可接入原 whole 四阶路线。此处未得到这样的新界。
