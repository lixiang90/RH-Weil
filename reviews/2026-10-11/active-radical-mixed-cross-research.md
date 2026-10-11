# 506：实际 mixed cross 的小活跃 radical 付款与完整系数接口

2026-10-11。研究作者：Codex 自动化数学研究代理
`ninth_span_analytic_transport`。只写本轮临时报告和精确检查；未改变冻结 source、
旧笔记、形式化仓库、Git、Goal 或复盘计数。

**新结果 [T/R]：** 原 `M_long S_short^2 Q_selected` 卷积的全部小活跃
radical 交叉项，包括不同六次无幂部分，可以绝对付款
`Oε(H R^(1/2+ε) U^ε)`。这里 R 是左右理想指数差模6的活跃 radical 范数阈值，
不是 `rad(kl)`，也不是被删除零的全部 radical。付款统一于实际两独立高度、
原 cutoff、恢复后的三个独立尺度和有限 Sobolev 导数族。

这是一项新的实际算术筛除；504只有 R=1 的同六次无幂部分付款。
它不证明剩余大活跃 radical 的有符号交叉估计，不登记全 count saving 或新 σ。
全部无限输入仍相对于项目明列的原输入包 **R**，尤其固定数域理想计数、
角色／自然零约定和 smooth calculus。没有声称重新证明整个原 source 或实际 ζ 无零条带。

## 1. 冻结身份和实际对象

实际只读 source：
`E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`，
canonical LF SHA256
`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`。
检查脚本本轮直接读取该文件并重算，不把旧 JSON 的 hash 当原文核对。

公开权威基线是505的 `reviews/2026-10-11/two-cutoff-joint-witness-coverage.md`
和第四周期 review；504研究稿中的“联合 witness gate 未付”已由505的实际五分支
partition 解决，不能继续作为新假设或缺口。不同部分 signed cross 仍未付。

原文定位，行数均指上述冻结文件：

| 原接口 | 位置 | 本报告保留的内容 |
|---|---|---|
| 固定数域及理想计数 | 610–626 | `# ideals(q≤X)=O_K(X)`；元素至理想只有固定有限 unit multiplicity |
| 原 sextic 符号 | 627–642 | `χ_c(v)=∏χ_p(v)^(v_p(c))`；零指数、负指数、6整除指数均保留 nonunit zero |
| M/S 定义 | 705–726 | 原 μ×1 系数、中央平方根归一化、自然零；不同 profile 不改变角色乘法性 |
| smooth calculus | 1101–1204 | 有限参数 Sobolev；固定内部阶先于 τ 与外部 tail order |
| reciprocity/fixed ray | 934–1092 | 固定 ray phases；共素消去不可除以零值 |
| 同 ψ 和实际零 ρ | 4221–4309 | 自然 presentation `νχ_n(u)^±`，primitive inducing 和原 Euler deletion 均保留 |
| detector dyads / saturated proof | 4385–4685 | 先定ρ，再定 `D*=U^t`，每次不同 Fourier maximizer |
| 逆列六次放大 | 12343–12475 | `ua^6` 单射、真实 scale supremum、原 profile 不随 restoration 偷换 |
| plain 与系数 | 12492–12586 | 原 Θ、common puncture、whole supports、两 plain 因子及实际 κ 容量 |
| 原物理 Q_i | 14998–15028 | `P_i^(-1/2) Σ_(p∈1_T) overline(χ_p(u)) W_i(q_p/P_i)(q_p/P_i)^(ζ−1)` |
| whole selection/方向 | 15113–15169 | 一次 whole product，原固定 finite-ray coefficients，witness/physical heights 不同 |
| 全 count 分支 | 15200–15436 | 无槽、r≥1、m≥1/2、固定零容量邻域、strict marked 与 plain 容量 |

## 2. 所有真实 core 参数及高度、ray coefficients

定义 `α=5/6, δ=2a−1, κ=2β*−1, x=q/δ∈[0,1/2]`，并记

```
c=1/(3κ), Dκ=3−(1+2c)x, Pκ=(2−2cx)(1−x)
A=α−δ, J=A Dκ+δPκ, B=δPκ/Dκ
t0=1+δPκ/(2J)
r0=((2−2cx)t0−(1−c)x)/Dκ, m0=t0−r0
R0=1−δ+A(t0−1), I1=δ(1−x), Cm=δ(2−2cx).
```

505为实际 bin 预先指定固定 g>0 的两个 cutoff
`t+=t0+g/B`、`t−=t0−g/A`。真实剩余 core 包含 **全部**

```
r_L ∈ (t0−g/A, t0+g/B+o(1)]
m ∈ [m0−g/A−g/I1−o(1), m0+g/Cm)
z_request(m)=(1−2m)/(6κ)−ν0,
```

并使用 greedy 选择的一次 whole 原 physical Q product，实际选中总长度
`z_selected≤z_request`；其尖峰仍按 requested length 付款，损失
`2qν0+δ max_i w_i`。不得把 actual z_selected 当 requested value 的恒等替代。
上面不是只取 crossing 的单个 r/m 或把 dyadic r 换成 t0。

两次 proof 使用相同已选 `ψ_u(n)=ν0(n)χ_n(u)^eχ` 和同一实际零
`ρ=σ+iγ`。本轮真实505 family 中 ray twist ν0 和方向 eχ 相同；
**Fourier extraction** 的 `ν+`、`ν−` 则可以不同：

```
ωL=γ−ν+,     ωS=γ−ν−,
WL(y)=W1(y)V≤((D/D*+)y)y^(−σ−iωL),
WS(y)=W2(y)y^(−σ−iωS),     D*+=U^t+.
```

两个 plain 是同一 WS 的两份，不把 ωL 和 ωS 识别，也不把
`n^(−iωL)b1^(−iωS)b2^(−iωS)` 改成单个 product frequency。
physical `ζ=z_phys` 另行固定；其 imaginary coordinate 不是 ν−。
有限 cutoff 调用、physical parameters 和所有后续 separating variables
共同分享原 `T1/2`，并按505先固定频率分配再缩小 τ。

把各 witness 的整个 factor 按需要共轭到原 Q 的负方向，取共同
`ψ=ν0 overline(χ_•(u))` 时，原 selected prime coefficient **准确为**

```
ai(p)=overline(ν0(p)) 1_(p∈1_T)
     =|T|^(-1) Σ_(θ∈T^) (overline(ν0)θ)(p).
Wi^phys(y)=Wi(y)y^(ζ−1).
```

它是固定 finite Θ list，固定于 row sum，原 underlying supports 在 mask 前互不相交。
若整体再共轭为正方向，系数变为 `ν0(p)1_T(p)`，所有 profiles 一同共轭。
Q出现一次；没有复制成 Q² 或让 selected slot 与自己发生支撑碰撞。

为兼容504已列的有限 ray closure，可以在 baseline ν0 下保留各因子的
`θL(n)=νL(n)conj(ν0(n))`、`θj(bj)=νj(bj)conj(ν0(bj))`；
这里各 νj∈Θ 固定、以相位乘入系数，而不是通过角色零值相除。
真实505同 ψ tuple 中这些 θj=1。原固定 exclusions、同一准入 polynomial-size
row-independent puncture 及各列的自然 zero extension 全部保留。
原 row mask随u固定成ψ的一部分，不能另选一个“有利 mask”。

## 3. Restoration、实际卷积及有限导数 closure

先按504正确的 triangle/scale supremum 处理 restoration，不把不同恢复 tuple
直接交叉展开。固定 amplifier a 和 tuple `(d,h1,h2)` 后

```
D'=D/q_d, X1'=U^m/q_h1, X2'=U^m/q_h2,
d|rad(a), μ(d)≠0, h1,h2|rad(a)^∞,
N'=D' X1' X2' ∏_(i∈I)Y_i.
```

三尺度各自可下降至 bounded/empty range；两 plain 的 restored scale 独立。
原 WL 整个保留，特别 `D/D*+` 仍是恢复前 parameter；不是 `D'/D*+`。
每个 nonempty annular tuple 的 `q_k≍N'`，原 fixed support 只影响固定常数。

对固定参数和尺度，写真实系数

```
c(k)=Σ_(n b1 b2 ∏pi=k) μ(n) θL(n)θ1(b1)θ2(b2)
      WL(q_n/D') W1S(q_b1/X1') W2S(q_b2/X2')
      ∏i ai(pi)Wi^phys(q_pi/Y_i),
Π_v=N'^(-1/2)Σ_k c(k)ψ_v(k).
```

对 actual retained family 的 indicator A(v)，原非负 radial majorant wH(v) 定义

```
K_H(k,l)=Σ_v A(v)wH(v)ψ_v(k)conj(ψ_v(l)),
E_raw=N'^(-1)Σ_(k,l)c(k)conj(c(l))K_H(k,l),    |K_H(k,l)|≪H.
```

**归一化重点：** 左右列是同一 whole Π_v 的系数，均有 N'，故确实是1/N'。
X1'与X2'不同不造成左右 Gram 的两个 N。不同 restoration tuples 之间不在本式内
交叉；若另研究这类交叉，就必须保留 `1/sqrt(N'_a N'_b)`，不能直接借本付款。
本报告逐 tuple 付款，随后与 scale supremum/Sobolev所需的其他 tuple estimates 一起消费。

新 raw cross 必须对整个 Π 的参数 Sobolev closure 统一。可以使用固定维数的参数
`(log D',log X1',log X2',σ,ωL,ωS,Re ζ,Im ζ)`（physical ζ若已固定则不需
在此重复 cover）。实际 Π对每坐标的一次 mixed derivatives 展开成有限个相同形状的
μ×plain×plain×whole-Q卷积：

- restored scale derivative将对应 W换为 `−W/2−Ey W`；这里 `Ey=y∂y`；
- σ derivative乘入各 witness 的 `−log y`，共用 σ时按 Leibniz 取有限和；
- ωL、ωS derivatives各在自己的 factor插入 `−i log y`，ωS作用两 plain；
- physical ζ derivatives在 prime factors插入 `log y` 或 `i log y`；
- 为记录 uniformly smooth cutoff，可允许固定有限次 `∂log(D/D*+)`，产生
  `(Ey^j V≤)((D/D*+)y)`。原 cutoff仍固定，不由 restore scale重新定义。

因此 closure具体为有限线性组合
`(log y)^b Ey^a[W_base(y)V≤(c_cut y)y^(−σ−iωL)]`、
`(log y)^b Ey^a[W2(y)y^(−σ−iωS)]`、
`(log y)^b Ey^a[Wi(y)y^(ζ−1)]`，a,b取由固定参数维数预定的有限范围。
底层 μ、ray phases、mask和prime coefficient list不变。
annular log y有界，Ey导数的height费用为固定 `(1+T1)^A`。
先固定这些阶及有限 tuples，再选 τ 和external Fourier tail order。

### 实际系数的更具体 divisor bound

原 μ(n)只允许每个prime在n中出现0或1次。固定k的p-adic exponent e时，
不把p选到Q的 inverse/two-plain factorization数为 `2e+1`；
若p属于一个 selected underlying support，还可把它选到该 **唯一** slot一次，
余数 factorization数为 `max(0,2e−1)`。全局“每槽恰选一个prime”的约束只删项。
因此e≥1时总数至多 `4e≤(e+1)^2`，e=0时为1。

固定J个slots只令profile/finite-ray幅度常数乘一个固定常数（例如 `C^J`），
不会产生一个随Z增长的额外slot数。于是完整实际系数及固定导数closure满足

```
|c(k)| ≤ C_closure (1+T1)^A d_K(k)^2 ≪ε (1+T1)^A(2+N')^ε.
```

没有使用 μ cancellation，也没有把它当 arbitrary coefficient 的原 plain theorem。
此处的subpower界来自原固定数域divisor约定；disjoint supports和Q只出现一次是关键。

## 4. 新引理：小活跃 radical 的全部理想对

令k,l为非零积分理想，`q_k,q_l≤C N`，N≥1。
设 `h=gcd(k,l)`，写互素quotients

```
k/h=s a^6,     l/h=t b^6,
s,t sixth-power-free, gcd(s,t)=1,
D_act=rad(st).
```

则对任意R≥1，

\[
 \#\{(k,l):q_k,q_l\le CN,\ q_{D_{act}}\le R\}
 \ll_{K,C,\epsilon} N R^{1/2+\epsilon}.                 \tag{1}
\]

**完整证明。** 固定s,t,a,b。可能的h满足
`q_h≤CN/max(q_s q_a^6,q_t q_b^6)`，由原固定数域理想计数，数量至多常数乘此上界；
右端小于1时没有h，故不需要另加一个未经付款的boundary常数。
利用max(A,B)≥sqrt(AB)，此数量≤

\[
 C_K N(q_s q_t)^{-1/2}q_a^{-3}q_b^{-3}.
\]

删除所有coprimality和尺寸限制以作上界，再对a,b求和，两个series均为
绝对收敛的`ζ_K(3)`。这是理想计数 `#(q≤X)=O_K(X)` 加dyadic summation的直接后果。
因此对固定s,t，可能的pairs总数 `≪_K N(q_s q_t)^(-1/2)`。

固定squarefree D=rad(st)。每个p|D恰有10个选择：把p放在s或t，指数1,…,5。
且 `q_s q_t≥q_D`。于是该D的贡献≤`C_K N 10^ω(D) q_D^(-1/2)`。
对每个ε>0，固定数域下 `10^ω(D)≪_(K,ε)q_D^ε`：大norm prime逐一用
10≤q_p^ε，有限小norm primes并入常数。最后原理想计数和dyadic求和给
`Σ_(q_D≤R)q_D^(-1/2+ε)≪_(K,ε)R^(1/2+ε)`，证明(1)。

全过程只放宽pair数；没有通过删coprimality获得一个反向下界。
有限unit/primary代表只贡献固定multiplicity（本数域至多6 units），并入常数。
这不是把理想数量当整数divisors数量；明确使用的无限输入只有既有linear ideal count。

### 活跃 radical 的真实角色意义与保留的 puncture

在p∉S且v为p-unit时，kernel中localphase为
`χ_p(v)^(eχ(v_p(k)−v_p(l)))`。它非平凡当且仅当该差不为0模6；
该local character的order为 `6/gcd(6,v_p(k)−v_p(l))`。
gcd quotients的sixth-free decomposition恰给这一prime集合D_act。
故它是 **活跃 sextic residue radical**；outside固定S的primitive conductor support
由此记录，不能与全部presentation modulus或`rad(kl)`混为一谈。

若p|kl而差为0模6，local值是 `1_(p∤v)`，不是1；gcd cancelled primes和纯sixth-power
quotient primes也都仍使v的值在nonunits为0。这些punctures以及全部固定ray phases留在
`K_H`中。(1)及以下付款只用 `|ψ_v(k)conjψ_v(l)|≤1`，完全不要求消掉任何puncture。
即使需要额外fixedS conductor或retained-family indicator，kernel的H上界仍成立。
不存在通过primitive化把零延拓抹去的步骤。

R=1恰给k,l相同sixth-free ideal part；R>1严格包含不同部分的pair。
例如两个不同good primesp,q，k=p,l=q有D_act=pq≠1，可在阈值内被本引理付款。
因此本引理不只是504同part lemma的重命名。

## 5. 可直接消费的 raw 筛除与全部恢复尺度

在第3节每个固定tuple自己的N'上，把(1)和实际系数界代入真实Gram，得

\[
 \left|N'^{-1}\!\sum_{q_{D_{act}}\le R}
 c(k)\overline{c(l)}K_H(k,l)\right|
 \ll_\epsilon H R^{1/2+\epsilon}(2+N')^\epsilon(1+T1)^A. \tag{2}
\]

每个restored nonempty N'≤原product的bounded-power U范围；将preliminaryε缩小后，
`(2+N')^ε`和`R^ε`都可付作U^ε。bounded N'同样成立，empty tuple为零。
这是固定tuple内整个signed subblock的绝对上界；不需要这个subblock非负。

对full mixed core取原放大width `H=U^(r_L+η)`，η>0固定。
若未来要证明 varying-long raw reference

```
E_raw≪H U^(1−L(r_L)−λ+ε)(1+T1)^A,
L(r)=1/6+(5/6−δ)r,
```

则本轮已付该目标中的全部
`q_Dact≤U^(2(1−L(r_L)−λ−b))`，其中b>0为任意固定额外reserve，
只要该指数非负。需要的新signed estimate可以等价地只针对其complement，
保持每tuple自己的normalization、原系数、原mask和kernel。
这是可消费降维，不是已经证明full reference或新的count。

本引理本身对所有bounded r_L,m、actual κ、restored独立scales统一，不以crossing点
或单个critical bin为前件。下面固定数值阈值只是uniform exponent的明确实例。

### 连续critical盒的严格数值实例

此前源证明已准入的连续有理盒

```
N: δ∈[3/8,2/5], x∈[49/100,1/2], κ∈[37/50,3/4]
```

上，取505的g=1/20000。原450/critical-neighborhood proof给
`c∈[4/9,50/111]`, `Dκ∈[455/222,1867/900]`,
`Pκ∈[86/111,1496/1875]`；从独立端点有理算术得

```
Jmin=785/666,
t0≤2785237/2453125,
r_L≤34503220411/30379500000≈1.13574023308481,
L(r_L)≤501053424521/729108000000≈.687214273497205.
```

取R=U^(31/50)=U^.62，本轮付款指数是H U^.31。
相对于设计λ=3/10000（**全cross尚未证明**）的reference，uniform额外余量为

\[
 1-L_{max}-.31-.0003
 =\frac{2031095479}{729108000000}-\frac3{10000}>\frac1{500}.
\]

所有实际r_L、m的core上下界及positive strict capacities在该完整连续盒严格成立，
检查采用区间端点而不是网格。small log-dyad/support errors及其reserve应在固定闭盒中
先付；不能把上述unbuffered端点当有限U的无误差恒等式。

在505单个target-label `δ=19429/50000,κ=7499/10000,x=1/2` 的整个actual r_L range上，
可进一步取R=U^(133/200)=U^.665，并且相对于同λ=.0003仍留额外raw exponent>.0003。
这是该label上的更大筛除，不把它推广成全盒阈值。

## 6. κ窗、非critical counts及剩余缺口核对

若仅用原whole-family7/8 bootstrap，在反证β*>.87495时
`κ_act∈(.7499,.75]`，已完整包含在上面连续κ区间。
若消费项目已写成451的**相对包R边界**σ*，则更紧地

```
κ_act∈(.7499,2σ*−1]⊂(.7499,.749915),
σ*≈.874957019420099.
```

本轮checker直接用已审三次根的有理interval证明该包含；未把`κ_target=.7499`
当真正positive-slot调用参数。调用仍必须用κ_act及其`β*=(1+κ_act)/2`前件。
因此同κ方向的uniformity不是遗漏一个moving feedback bin。

旧 **全count／物理覆盖** 的范围是：450的adaptiveinverse/plain计数覆盖
`δ∈[1/50,3/4],x∈[0,1/2]`，包括r≥1、m≥1/2、δ边界和zero capacity。
451的连续square-completion高侧证书覆盖整个δ/x rectangle，而非仅N；
源之外的floor、`1/100≤d≤1/2` middle、small/boundedS-supported rows、outer、
Euler/principal和familycontinuation均在那里逐项保留。505的五个ordered complement
在其准入critical邻域穷尽所有非core detector rows；不能再丢掉long-only或接近capacity0行。

**范围区别：** 这些文档是旧σ*的包R全局覆盖。505对于更小目标的实际mixed partition
给了局部完整core和coverage tax，但没有提供已付款的大active-radical raw estimate。
也没有由本轮单个label/盒断言更小目标的全部criticalδ/x bins都落在N。
将来targetgeometry改变后，仍须用实际continuoushigh accounting证明N之外的旧count余量
足以付新目标，或对额外near-critical bins使用(2)的一般variable-threshold版本。
小radical lemma在这些额外bins上本身仍无缺口；固定`.62`实例不替代这一global比较。
这保留原source的physical low/rawhigh/normalizer和全`ArithmeticProbeObligation`的范围。

目标`.87495`的必要all-branch count saving仍为

\[
 \frac{467366968772963}{12314470624500000000}\approx3.7952664\cdot10^{-5},
\]

505的coverage multiplier仍为
`8209647083/1500842361≈5.4700262308`，相应limiting varying-long raw λ约
`.0002076020689`，另加width、height、mesh、whole-slot、profile及实际bin损失。
g=1/20000的设计需要rawλ≥`.0002735013115+5η/6`；原假设λ=1/20000不能满足。
本轮不能以筛除费用低于目标为理由抹掉coverage税。

剩余新最小算术目标是 **大活跃radical、原μ×1×1×once-Q系数的有符号聚合**。
现在它可以明示删除(2)已付的全部low-active pairs，且对每个parameter tuple和scale
一致保留两height、完整punctures和finiteclosure。generic `H+N'`或逐pair绝对估计
仍不足以供应所需fullraw预算；本轮没有提出一个未经证实的新large-sieve定理作为成果。

## 7. 复现与证据层级

运行

```
C:/Python312/python.exe -B -X utf8 tmp/research-round506-20261011/zero-free/active-radical-mixed-cross-check.py --output tmp/research-round506-20261011/zero-free/active-radical-mixed-cross-check.json
```

1352项exact检查PASS：实际source身份、gcd quotients剥六次后的localmod6活跃差和zero约定、
inverse/two-plain/once-Q的localfactorization数、完整连续盒的strictthresholds、
κ bootstrap interval、原coverage税和rawλ门槛。本脚本只写指定新输出。
它不从有限localchecks推断无限Hecke估计；无限pair计数是第4节的书面证明。

独立于研究作者的`checkpoint_audit`自动化审查已初步逐步重推(1)，确认overcount方向、
两个ζ_K(3)、10choices和理想计数；它特别要求保留primitive/puncture区别及实际normalization，
本报告已纳入。该初审不是人类同行评议，也不是独立内核证明。

付清的是actual small-active-radical block；全signedcross、fullcount和更小σ均未付。
原论文、记录及版本保持原样。
