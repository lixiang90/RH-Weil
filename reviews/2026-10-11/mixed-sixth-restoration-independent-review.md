# 独立数学审查：mixed sixth-power restoration、same6 付款及剩余 count gates

2026-10-11。审查者：feedback_formalization（独立于研究稿作者）。
发布补充：审查者最后复查修订稿时确认全部实质gate已纳入，并修正原意见中的措辞：
δν₀及δ max wᵢ是保证下尖峰的预留预算，不能称实际损失必然“至少”如此。
严格raw指数为t+η+1−R−λ=t+1−R−χ+η/6。公开修订稿已采用这两项修正，
下文初稿审查保留原记录。
只读审查研究稿、预算 Python/JSON、冻结 written source 及既有 witness/status 文档。
没有运行 Lean，没有改主研究稿、形式化仓库或 Git，没有登记任何新无零区域。

本审查读取版本的 canonical LF SHA-256：
research.md `44dd0e18a1cc9342065c2a1ce433b5e3004e7359f30e85ff5e41d3853b3a3951`；
budget.py `45da1831dd277d50e09e94ed8eaee7bd3adf24adb29ac4d64cef939ca4bcff97`；
budget.json `ac517eb95c5d19d3058fa7781e15bdab3c3b0749aed9428d5ba0f6c4d5043d0a`。
审查意见涉及研究稿随后修订时，应保留初稿和修订稿身份区别。

## 结论

研究稿的**条件性代数归约**成立：在明示共同 zero-extended presentation、
同向 χ、固定 masks、实际有限 profiles/slots 之下，可以同时恢复一份 long inverse、
两份 short plain、一次 selected whole-slot product，并得到真实 convolution/Gram。
完整 same-sixth-free-ideal-part block 的绝对付款 O(H U^ε) 也成立，
包含不同 ideal columns、自然零和固定 ray phases；没有误把它证明为完整 resonance locus。

不同 sixth-free part 的 signed cross estimate 仍完全未付。
此外，raw mixed 上界到**全部 detector count**之间还有一个独立 gate：
原 detector 不自动保证同一行同时存在指定 long-M 和指定 short-S 的大尖峰。
目前只能消费明示 simultaneous-large core 的 spike。
因此这些归约及有限 checks 都不能登记 count decrement 或新条带。

## 1. Restoration 的实质与适用范围

在所有列上使用
ψ_u(n)=ν(n)χ_n(u)^εχ，εχ∈{−1,1}，
ν 是固定有限 ray character，所有固定排除、自然 zero extensions、允许的共同
row-independent coprimality puncture 已包含在 ψ。这样的 puncture 是乘法性的。

χ_n(a^6)=𝟙_{(n,a)=1} 给 ψ_(ua^6)(n)=ψ_u(n)𝟙_{(n,a)=1}，
不要求 (u,a)=1。这与 source 12409–12475 的 exact identity 完全一致。
对 inverse n 的 squarefree decomposition n=d m（d|rad(a), (m,a)=1），
μ(n)=μ(d)μ(m)，产生 q_d^(−1/2) 和原 μ(d)ψ_u(d)。
对 plain b 则必须取所有 a-supported valuations h，不可只取 squarefree h，
产生 q_h^(−1/2)。研究稿 (2)–(4) 正确使用了这两个不同分解。

两份 plain 恢复后的 scales X_1/q_(h1)、X_2/q_(h2) 可不同；
故未来 raw bound 必须覆盖这两个独立 restored scales，不能仅覆盖原同尺度 S^2。
实际选中 slots 与 a 的底层支持互素时 Q_(ua^6)=Q_u；Q 出现一次，
没有用一份 |Q|^2 替代原 product 的平方，也没有增加额外一份 Q。

local absolute mass
∏_(p|a)(1+q_p^(−1/2))(1−q_p^(−1/2))^(−2)
≪_ε q_a^ε 的证明正确。对小素数付款固定常数，对其余素数以
log(local factor)≤ε log q_p；平方时先减半 ε。
这里只是 divisor/absolute cost，没有 Euler cancellation saving。
预算脚本的 truncated local-polynomial checks 只核有限形式系数，
不能称作实际 Hecke-row restoration 的机器证明。

## 2. 放大、族与 masks

(u,a)↦ua^6 对原 sixth-power-free ideal valuations≤5 的 element rows 是单射：
valuation mod 6 恢复 (u)，商恢复 (a)，primary generator 恢复 u 的 unit。
这不需要 u 与 a 互素。q_v≪UP^6≪H，P=(H/U)^(1/6)。

a 只须避开固定 S 与实际 selected supports。若另有 polynomial-size moving
puncture，不能额外要求 a 避开其所有素数后仍无证明地宣称 ≫P amplifiers；
它的零值已在列中，restoration 本身不需要这个额外排除。

selected-support 排除的 union bound 正确，但需明示固定正长度下
# {a:q_a≤P,p|a}≪P/q_p（q_p≤P）和
Σ_(p in slot i)1/q_p≪1/log Y_i，slot count 已固定。
正长度 annuli 的 min length 要在所用真实 row-bin 紧范围内一致大于 0；
zero-length/bounded slots 的有限支持应并入固定排除，保持正密度 constant。
其 constant 不能依赖随后变化的 row。

乘以 a^6 只增 zero extension，不改变 primitive inducing character，
故原 outside-Θ/nonprincipal 分类保持。fixed masks 应保持原定义。
新 kernel 应明确写
K_H(k,l)=Σ_v A(v)w_H(v)ψ_v(k)overline(ψ_v(l))，
其中 A(v) 是包含全部 injective images 的实际 retained-family indicator。
可删除 A 来取得更大的非负 raw energy，但这只是更强的新目标；
不能把原 plain theorem 的 outside-Θ 前件一并删除再声称得到 (13)。
当前文字“retained condition may be kept”数学上允许，正式 memo 宜把这个 gate 写进公式。

## 3. 不同高度与不同 ν 的 convolution

同一 ν 的现有 (8)–(9) 正确，**前提是 W_L,W_1,W_2 已是实际 complex profiles**。
例如 source inverse profile含
W_L^0(y)V_≤(D y/D_*) y^(−σ_L−iω_L)，
short profiles 分别含 W_j^0(y)y^(−σ_j−iω_j)。
不同高度留在不同变量 n、b_1、b_2 的因子中：
不能把 n^(-iω_L)b_1^(-iω_S)b_2^(-iω_S)
简化为 k^(-iω)，除非真的相同。

restoration 改变 scale 时必须保持**原整个 W_L**，含原 D/D_* cutoff 参数；
不可把 cutoff 里的 D 自动改成 restored D' 后仍称 exact。
每个 fixed tuple 的 coefficient 仍 row-independent。
Sobolev 应先对整个乘积求导、积分，固定 derivative closure 后再使用 raw estimate；
任何“finite A”必须在选择 τ 与 external tail order 之前固定。

若 long/short witnesses 具有不同 ν_L、ν_S∈Θ，则当前裸 (8) 不能直接沿用。
在所有 indices 已排除固定 S 的前提下，可选 fixed baseline ν_0，
把 θ_j=ν_j overline(ν_0)∈Θ 的相位吸入**各自** short coefficient：
c(k) 中必须增加 θ_1(b_1)θ_2(b_2)（long baseline 若不同也增加 θ_L(n)）。
自然 zero masks应逐列保留，不能通过除以 zero character value 处理。
这保留 single ψ_v(k) 与 row-independent coefficient，因为 outside S 上
|ν_0|=1；可用 conjugation 而不用除法。
若 χ orientation 不同，先共轭相应整个 factor/profile/coefficients，
绝对平方不变，再固定 orientation；不能只共轭 character 漏掉 profile。

此推广的 restoration 使用各 factor 的 fixed ray character，仍成立；
但它扩大了待证明 mixed raw coefficient class。原 marked/common-ν 或原 plain
statement 均不会自动给这个新的 mixed estimate。不同 t 下 witness twists/heights
的有限标签 subdivision 与统一 derivative constants 仍要明确付账。

## 4. same6 付款正确，未证明完整 resonance

每个 ideal k 唯一分解 k=s a^6，s sixth-power-free。
q_k,q_l≍N' 时给定 s 的 a,b pairs 数≪(N'/q_s)^(1/3)。
fixed-field A(X)≪X 的 dyadic counting 给
Σ_(q_s≤C N')q_s^(−1/3)≪N'^(2/3)，
所以所有 same-s pairs 数为 O(N')。
fixed-slot divisor bound |c(k)|≪_ε N'^ε、|K_H(k,l)|≪H，再除以 N'，
确给 O(H N'^ε)；因原 scales 的 bounded length ranges，改写为 O(H U^ε)。
bounded/empty restored scales可用 (2+N')^ε 并入 fixed constants。

finite units/primary/ray representatives只贡献固定 multiplicity。
此证明没有使用 ψ_v(a^6)=1，因该值可含 ν(a)^6 与 natural mask。
“same6”应称 sixth-free ideal **part** grouping，不是 ideal class group，
更不是全部 phase-resonant locus。不同 s 也可能有相位退化；
它们没有被这笔 O(H U^ε) 自动付款。

## 5. simultaneous-large core 是单独未付的 count gate

可明确设真实 subset C 满足，统一 preliminary losses L_M,L_S,L_Q≥0：

|M_long,u(U^t)|² ≥ U^(δt−L_M),
|S_short,u(U^m)|² ≥ U^(δm−L_S),
|Q_selected,u|² ≥ U^(2qz−L_Q),

其中 q=δ/2；fixed presentation、允许的 rowwise profile heights、
real selected-slot subcollection 和原自然 masks 均同时存在于同一 u。
则乘积 lower spike 为
U^(δt+2δm+δz−L_M−2L_S−L_Q)，
有 mixed upper U^(1+δt−χ+ε)(1+T1)^A 才能推出
#C≪U^(R−χ+ε+L_M+2L_S+L_Q)(1+T1)^A。

source detector对一个 t 给一对 r,m，r+m≥t−o(1)、r≤t+o(1)；
原 long branch 可以取 r=t,m=0，short branch 可取 r=r_*(t),m=t−r_*(t)。
这不推出同一行的 M_long(t) 和 S_short(.40859...) 两尖峰同时成立。
即使跨多个 t 调用 detector，每次 dyads/twists/profile可能不同，
仍需 joint-witness 构造与其余行的完整覆盖/计数。
研究稿应把“real lower spike”改为“explicit simultaneous-large core 下的 lower spike”。
目前 raw cross saving 和此 core/coverage gate 均未证明，不能登记全 count saving。

## 6. 精确复算、normalizer 和损失

作者脚本的 73 assertions 全部实际重放成功；
采用只执行、不覆盖 JSON 的方式，结果与原 JSON 完全一致。
另以独立 Fraction 公式重算 20 项标量恒等式/有理数，全部通过。

关键结果：

- t=9229494722/8209647083，
  r=5875092361/8209647083，
  m=3354402361/8209647083，
  z=333565000/8209647083；
- R=136828076410631/205241177075000；
- t+2m+z=1479260404/746331553；
- t+1−R=299150468714369/205241177075000；
- R+δt=(1+5t)/6，2δm+δz=1−R；
- λ=1/20000、η=1/1000000 的**假设** net saving
  χ=59/1200000；
- 必要 decrement=467366968772963/12314470624500000000；
- 假设余量 χ−必要值
  =46031501199429/4104823541500000000
  ≈0.000011214002437388087；
- 旧 marked-only 带槽放大 cost 的正斜率
  5/3−δ=191713/150000>0。

raw profile-fixed upper 的 exponent 若为 B+1−R−λ，
乘以 P^(−1)=U^(-(B−1)/6)，B=t+η，所得恰是
(1+5(t+η))/6+1−R−λ
=1+δt−(λ−5η/6)。
所以 strict-width cost **5η/6** 保留正确，没有凭空消失。

Pi 的归一化是 N^(−1/2)，Gram 是 N'^(−1)，
restoration 的各 q_d,q_h 权重已付款。
这只是 detector mixed-product normalization；
它没有证明完整 compensated probe J 或 principal slot normalizer的 source assembly。
原 Z^(−e/6)、principal residue常数与 adaptive inverse-normalizer costs不能由这73 checks补齐。

剩余损失必须从上述假设余量逐项扣除：
strict selected decrement ν0 在 q=δ/2 下至少扣 δν0；
whole-slot mesh扣 δ max w_i；witness/bin/Sobolev profile与原均值clipping的幂损失；
triangle/divisor/scale-dyad U^ε；以及 T1=Z^τ 时
(1+T1)^A 变成 U^(Aτ/d)（U=Z^d），不能当固定常数。
须先固定统一 A、选所有小损失，再选 τ 和 external N。
一条 rational label仅给必要测试；actual κ=2β*−1 的连续 admitted bins、
其余 floor/middle/small/outer、low/principal/continuation均仍另需完整证明。

## 判定

- 已给正确相对证明：mixed restoration、absolute amplifier reduction到scale supremum、
  actual convolution Gram、same-sixth-free-part 绝对 block 付款。
- 仍未付：实际不同-part signed cross 上界；不同 witnesses 的共同 core/coverage；
  原实际族及 height/masks/normalizer 的完整新 count/probe assembly。
- 没有新 count decrement，没有新无零区域，没有新增 Lean theorem。
