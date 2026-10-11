# 第506轮小活跃 radical 引理的独立审查

2026-10-11。审查人：`proportion_research_20261010`。**结论：限定通过 [T/R]。**
这里通过的是原 `μ×plain×plain×once-Q` 卷积的小活跃 radical 子块、它的恢复尺度和有限参数接口。
没有得到完整 signed mixed estimate、全 count saving 或新的无零边界；没有运行 Lean 或 NaNoDa。
原比例证书、正式源、Git 和形式化仓库保持冻结。

审查对象是公开的 `reviews/2026-10-11/active-radical-mixed-cross-research.md` 与
`scripts/hybrid_active_radical_mixed_cross_budget.py`。原稿第7节保留作者临时路径，公开运行方式
以 `reviews/2026-10-11/active-radical-mixed-cross-reproduction.md` 为准。
公开报告与保存的作者稿逐字相同；本审查的文件身份见 `independent-active-radical-audit.json`，
绑定的是公版程序、公版证明及其公版有限收据，不把作者临时程序的 hash 当公版 hash。

实际读取的原 TeX 为
`E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`。
已独立重算 canonical LF SHA256：
`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`，766316 bytes。
重点读原文605–738、1101–1206、4221–4309、4385–4685、12343–12586、14998–15035、
15100–15178，并对照项目450、451及505的实际两 cutoff 覆盖报告。
这些阅读核对本轮使用的原接口，不是重新认证原整篇论文或其全部外部分析输入。

## 1. 无限理想对计数：方向和规模成立

给定非零积分理想 `k,l`，令 `h=gcd(k,l)`。唯一分解为
`k/h=s a^6`、`l/h=t b^6`，其中 `s,t` 六次无幂、互素。原互素性还约束 `a,b`，
但在上界中允许全部删除这些约束。设 `D=rad(st)`，`q_k,q_l≤C N`、`N≥1`。

固定 `s,t,a,b` 后，`q_h≤C N/max(q_s q_a^6,q_t q_b^6)`。
这个上界小于1时没有任何 `h`；不应为每个四元组添加一个独立的 `+1`。
否则，原固定域理想计数 `#(q≤X)=O_K(X)` 给

```
#h ≪ N (q_s q_t)^(-1/2) q_a^(-3) q_b^(-3).
```

因此删除互素和尺寸限制后，两根变量之和是两个收敛的 `ζ_K(3)`。
只需原理想计数作 dyadic 求和，不需要新的 cancellation 或大筛定理。
固定 `s,t` 的总贡献 `≪N(q_s q_t)^(-1/2)`。

固定 squarefree `D`，每个 `p|D` 只能在 `s,t` 中的一侧出现，指数为1至5，恰10种选择。
于是这一 `D` 的贡献至多 `C_K N 10^ω(D)q_D^(-1/2)`。
任给 `ε>0`，大 norm prime 满足 `10≤q_p^ε`，有限小 prime 合并入常数，
所以 `10^ω(D)≪ε q_D^ε`。再由理想计数的 dyadic 求和得到

```
# {(k,l): q_k,q_l≤CN, q_D≤R} ≪K,C,ε N R^(1/2+ε),   R≥1.
```

每一步都是计数集合的上界放宽，未从放宽图反推下界。
单位/primary generator 只有固定 multiplicity：本域为6个单位，理想对至元素对至多固定36倍。
这是本轮无限命题的书面证明；有限程序的局部测试不是该无限命题的证明。

## 2. 活跃性不等于删除自然零

实际方向只有 `eχ=±1`。在 good prime `p` 的单位行上，相关局部相位为
`χ_p(v)^(eχ(v_p(k)−v_p(l)))`。它非平凡恰当指数差不为0模6，局部阶为
`6/gcd(6,v_p(k)−v_p(l))`。gcd 后的六次剥离恰得到 `rad(st)`。
原有限 ray twist 的 conductor 只在固定 `S`，不会取消 good prime 的这个局部相位。

若 `p|kl` 而指数差为0模6，原 presentation 在 `p|v` 仍是0；在 `p∤v` 才是1。
因此 gcd cancellation 和纯六次幂所留下的 punctures 必须全部留在 `K_H`。
公版稿明确这样做，pair bound 只用角色乘积模长至多1，所以不依赖取消这些零。
`D` 的用途是记录活跃 sextic 相位 support；它不能替代完整 presentation modulus 或 `rad(kl)`。

`R=1` 等价于左右理想各个指数模6相同，也即同六次无幂部分。
`R>1` 的估计还付款给不同部分的 pair，故比504的同部分子块确实扩大了范围。
没有从“局部相位不活跃”得出整行字符值恒为1。

## 3. 实际系数没有被换成任意 plain coefficient

原 inverse 具有 `μ(n)`，两份 plain 的系数为1；选中的整个 `Q` 只出现一次，
underlying prime supports 在 mask 前互不相交。
共同负方向 `ψ=ν0 overline(χ_•(u))` 中，原 prime coefficient 为
`overline(ν0(p))1_(p∈1_T)`，是原固定 `Θ` 的有限展开。
它与原15136–15162的 whole conjugation 一致：换方向时整个 factor、其 profile 和系数一起共轭。
没有把自然零值作除数。真实505 family 的不同 factor 使用同一 `ν0`，额外 finite-ray closure
仅作为固定相位留在系数中。

对固定 `k` 的某个 prime exponent `e`，inverse 只可占0或1次。
没有把该 prime 选进 `Q` 时，两个 plain 的分配数是 `2e+1`；
若选进它唯一可用的 slot 一次，余数分配数是 `max(0,2e−1)`。
因此 `e≥1` 时总数至多 `4e≤(e+1)^2`，`e=0` 时为1。
每槽必须选一个 prime 的全局约束只减少分配数。
`J` 个槽及其原 profile 幅度只给固定常数；`J` 先于 `U` 固定。

于是实际卷积和固定导数 closure 有
`|c(k)|≪C,ε (1+T1)^A(2+N′)^ε`。
这里的 ideal-divisor subpower 也可直接核：大 prime 对所有 `e≥1` 用
`(e+1)^2≤4^e≤q_p^(εe)`，有限小 prime 的
`sup_e (e+1)^2q_p^(−εe)` 并入固定常数。
没有借用原 plain theorem 去支付任意长 Möbius 卷积，也没有使用 μ cancellation。

## 4. 恢复公式、cutoff 和分母均匹配原对象

对固定 amplifier `a`，唯一拆解 squarefree inverse index 为
`n=d n′`，`d|rad(a)`；plain index 为 `b=h b′`，
`h|rad(a)^∞`、`(b′,a)=1`。原 zero extension 给
`ψ_(ua^6)(b′)=ψ_u(b′)1_((b′,a)=1)`，即使 `u,a` 共素因子也成立。
因此每个 plain 的恢复式准确为

```
S_u(X;W)=Σ_(h|rad(a)^∞) ψ_u(h) q_h^(-1/2) S_(ua^6)(X/q_h;W).
```

inverse 的同式另带 `μ(d)`。这由原中央归一化直接得出：
`q_h^(-1/2)(X/q_h)^(-1/2)=X^(-1/2)`。
三个恢复尺度 `D′,X1′,X2′` 相互独立，不能因原两 plain 相同而强制 `X1′=X2′`。
恢复系数总绝对质量为
`∏_(p|a)(1+q_p^(-1/2))(1−q_p^(-1/2))^(-2)≪ε q_a^ε`；
故原 triangle/scale supremum 路线仅有 subpower 费用。
prime supports 外选择 `a` 保证 `Q_(ua^6)=Q_u`；此为先前恢复归约的真实前件，未在本轮删除。
先前 amplification 使用原理想计数/素理想输入取得足够这类 `a`，原 `ua^6` 的单射也保留。

尤其原长 witness profile 是
`W1(y)V≤((D/D*+)y)y^(−σ−iωL)`。
当 `D′=D/q_d`，`y=q_n′/D′`，其 cutoff argument 为
`(D/D*+)y=q_d q_n′/D*+`，准确等于恢复前指数 `n=d n′` 的 cutoff。
改成 `D′/D*+` 会得到不同函数，公版稿没有这样做。

固定一个恢复 tuple 后，`N′=D′X1′X2′∏Y_i`，同一个 whole product 的 Gram 分母是 `1/N′`。
不同 tuple 的交叉需要 `1/sqrt(N′_a N′_b)`，公版稿没有付款给这些交叉。
它先作 triangle/sup，再对每个固定 tuple 的 Gram 付款。

**小尺度的补充解释。** pair lemma 写成 `N≥1`，而恢复后 `N′` 可能小于1。
设固定 annular supports 乘积的上端常数为 `C_J`。
nonempty tuple 有 `1≤q_k≤C_J N′`，因此 `N′≥C_J^(-1)`。
应用 pair lemma 时取 `N=max(1,N′)`，则 `N/N′≤max(1,C_J)`。
这里 `J`、全部 support 和有限导数阶先于 `U` 固定，故这一常数不会隐藏一个额外幂损失。
empty tuple 贡献为0。这补齐公版稿“bounded N′同样成立”的解释，不增加算术前件。

`|K_H(k,l)|≪H` 来自真实 retained indicator（模长≤1）、固定有界径向 majorant 和元素/理想计数。
将上面的 pair bound、系数界及真实分母代入，并将初始 ε 缩小，就得到公版稿的

```
|E_small-active| ≪ε H R^(1/2+ε)(2+N′)^ε(1+T1)^A.
```

这是 signed 子块的绝对上界；子块本身不必非负。
对 bounded-power `N′,R`，额外 subpower 因子可支付为 `U^ε`。
没有用未恢复的总长度 `N` 去代替某个很小的 `N′` 分母。

## 5. 两高度及有限 Sobolev 费用没有遗漏

原 detector proof 先选同一 `ψ,ρ`，再选 cutoff；逐 cutoff 的 Fourier maximizer 可以不同。
因此 `ωL=γ−ν+`、`ωS=γ−ν−` 确为两个独立参数。两份 plain 仍同一 `ωS`。
物理 prime 参数 `ζ` 的虚部另外固定，不能识别为 `ν−`。
固定 dyadic/finite-ray 子类后，卷积系数与 row 无关，才可形成所写 kernel。

对整个 product 作参数 Sobolev，scale derivative 产生 `−W/2−EyW`；
`σ,ωL,ωS,ζ` derivatives 插入 bounded annular `log y`，按 Leibniz 展开有限和。
同一 `ωS` 作用两个 plain 的事实仅增加有限项数。
cutoff 的有限 Euler derivatives 始终作用于原 `(D/D*+)y`，transition 时 argument 有界。
所有结果仍属于相同 μ/two-plain/once-Q coefficient class，support 不扩大。
相位的 Euler derivative 只产生固定 `(1+T1)^A`，其阶先于 `τ` 和 external tail order 固定。
单位参数盒及多项式 scale cover 增加 powers of `log U`；height cover 增加固定 height power。
两个 Fourier maximizer、物理参数和后续 separating variables 分享同一原 `T1/2` 预算。
没有重新给每一步另发一份全额频率预算，也未以 tail order 反向改变已固定的内部高度阶。

未来的大活跃 signed estimate 必须对这整套固定 derivative closure 一致。
只有原中心 profile 的一个结果不能自行给出 scale supremum 或 rowwise height 结论。
公版稿把该要求保留为下一项未付接口。

## 6. 连续 critical 盒：有理付款成立，范围有限

独立程序没有 import 作者代码。它从 `c,D,P` 的连续单调性重新推导端点，
然后用有理区间支付整个
`δ∈[3/8,2/5]`、`x∈[49/100,1/2]`、`κ∈[37/50,3/4]`。
`D` 随 `c,x` 减少；`P_x=−2−2c(1−2x)≤−2`，且 `P_c≤0`。
故使用端点是全盒证明，不是从有限 mesh 或角点采样作外推。

得到的公版界逐项一致：

| 量 | 独立严格有理界 |
|---|---|
| `D` | `[455/222,1867/900]` |
| `P` | `[86/111,1496/1875]` |
| `J` lower bound | `785/666` |
| `t0` upper bound | `2785237/2453125` |
| 未扣 support error 的 `r_L` 解析端点 upper bound | `34503220411/30379500000`，约1.1357402331 |
| 相应 varying-long `L(r_L)` upper bound | `501053424521/729108000000`，约.6872142735 |
| 未扣 support error 的 plain core 端点 | 保守包含于 `(.3980259596,.4181404567)` |
| requested plain capacity | 保守包含于 `(.0363820192,.0459342525)` |

固定 `g=1/20000` 时，两 cutoff 在 `(1,3/2)`，短 inverse cutoff 距1和 plain cutoff 距1/2
均有固定 margin；独立检查也给出可用的 near-one/near-half 无槽 buffers `1/10000`。
原 whole-slot 供给 `ell/d>1/5` 足够，所请求的 marked capacities 始终严格。
实际 dyad/support 的 `o(1)` 和 mesh、height、slot rounding 仍须从这些严格 margin 中另行支付。

对 **设计中、尚未证明全 cross** 的 raw saving `λ=3/10000`，全盒选择 `R=U^(31/50)` 有

```
1−L_max−31/100−3/10000
  =1812363079/729108000000 >1/500.
```

因此全盒小活跃子块确可从该未来预算中删除。
在单个 target label `δ=19429/50000,κ=7499/10000,x=1/2` 可用的 `R=U^.665`
只在该 label 的全部实际长范围有效，不能推广到整个盒。

**κ 记账。** 原 paper 的 generic plain lemma 在12531写明 `κ≥3/4`。
本次 `κ<3/4` 的 capacity/coverage 必须消费项目450从底层 [R] 重证的
`κ∈[37/50,1]` 版本及其完整前件，不能直接区间外引用原声明。
本审查已核对450和独审记录；这里把它作为既有相对输入，并未重新审完其整个无限归纳。
实际调用 `κ=2β*−1`，不能替换成 target κ。原7/8 bootstrap 给
`β*>.87495 ⇒ κ∈(.7499,.75]`，完全落入上面 κ 区间。
引用451的较紧上界同样是相对包R的结论，不是本轮新增的无条件 ζ 输入。

**δ/x 记账。** 全盒 N 不覆盖所有物理 bins。450/451的旧全域 count 与 continuation
是旧相对边界的记录，不能自动供应更小目标在 N 外所需的新余量。
公版稿第6节准确保留这项未来 high accounting；未把单个 critical label 当全域。
一般 variable-threshold 小活跃引理在外部 bins 仍成立，但固定 `.62` 数值例不替代全域比较。

## 7. 仍未付的接口及实际复验

所需 all-branch coverage multiplier 仍为 `8209647083/1500842361≈5.47002623`。
必要 target count decrement 经这项 tax 后的 raw gate 是
`467366968772963/2251263541500000000≈.0002076020689`，另需其他费用。
固定 `g=.00005` 的设计要求 raw saving 至少 `.0002735013115+5η/6`，再加全部真实费用。
小活跃子块的付款不抹去这些税，也不证明所需 full signed estimate。

真正剩余的是保持原 Möbius 系数、once-Q、natural punctures、恢复尺度和整个有限 closure 的
大活跃 radical signed 聚合。除非这项估计、N 外真实 high accounting 和完整原 probe/continuation
一并闭合，本轮成果不能登记为全 count 或 σ 提升。

本审查的独立运行：

```
C:/Python312/python.exe -B -X utf8 tmp/research-round506-20261011/zero-free-independent/independent_active_radical_audit.py
```

实际 exit 0，3367项检查 PASS，包括原源身份、局部 valuation 重建、自然零、实际 factorization
计数、全连续盒、严格 capacities、cubic interval 和公版核心数据逐项对照。
另实际执行公版 `--check --source <frozen-paper.tex>`，exit 0、1349项有限核心加3项 source 检查，
共1352项，`source_matched=true`。所有公版输入在复验前后未改变。
这是有限代数和源身份复验；无限 pair 计数的审查依据是第1节书面证明。
收据与公版程序 hash 见本目录 JSON；没有把有限 PASS 命名成无限分析、Lean 或实际 ζ 证明。
