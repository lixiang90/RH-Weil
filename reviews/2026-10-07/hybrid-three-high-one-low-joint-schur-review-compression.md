# whole31 joint Schur：独立 compression 审查

2026-10-07。全文只读独审；只新增本文件，旧数学、源、Goal、Git 未改。

结论：限定 PASS。源稿的 finite Gram、Schur complement、整个 22 消元、
sharp constant 与 one-sided envelope 均成立。新收益是 already-paid
entire13 对 31/22 联合预算的常数改进；没有由此支付 whole high4、
整个第四矩或任何新的比例/无零边界。

## 1. 完整快照绑定

源：reviews/2026-10-07/hybrid-three-high-one-low-joint-schur-budget-research.md。
canonical UTF-8 LF SHA-256：
`d48a20606a81c88b5b466339c95ee6049b26d50ebc7b23209c936980dcd131b1`，
13091 bytes / 354 lines。只把 CRLF/lone CR 统一为 LF，不 trim。

源稿列出的同对象前件 461、462、463 对应 final hashes
f9fdf0b7…8170b、868adfeb…f680、6554ebc8…7d90。
本审查沿用此前独审，不把 repeated high 常数当作 whole high4。
源的 H=C_H、L=C_L 始终是原同维 actual finite matrices。
它没有循环带末端 P 的 physical trace，没有替换 carrier，也未删除
三个内部 P。因此本次后续有限代数的 cyclic traces 全合法。

## 2. finite HS Gram 与 Schur complement

写 a=Tr H⁴/d、e=Tr L⁴/d、b=Tr H³L/d、η=Tr HL³/d、
c=Tr H²L²/d、s=Tr HLHL/d。Hermitian cyclic trace 保证 b、η、s 为实数。
c=||HL||HS²/d≥0；|s|≤c；k=||[H,L]||HS²/d=2(c−s)。
entire22 w=4c+2s=6c−k，因此 2c≤w≤6c，c²≤ae。

三个真实 HS vectors H²、L²、S=HL+LH 的 Gram entries 正确：

\[
 \begin{pmatrix}a&c&2b\\c&e&2\eta\\2b&2\eta&2(c+s)\end{pmatrix}\succeq0.
 \tag{R1}
\]

对 e>0，分别减去 (c/e)L²、(2η/e)L²。归一化平方范数为
a−c²/e 与 2(c+s)−4η²/e，inner product 为 2b−2cη/e。
Cauchy 后准确给

\[
 |b-c\eta/e|^2\le(a-c^2/e)\{(c+s)/2-\eta^2/e\}.
 \tag{R2}
\]

两个因子非负，不能在负余量上取平方根。源稿已保留这一点。
e=0 时 L=0，所有 mixed quantities 为零；实际 e_T→e_0>0，
足够大 T 的 e>0 前件合法。一般原正 profile 的 low4 正性证明也成立。

## 3. entire22 消元与未知增长的 η 误差

给定 a,e,w，准确 admissible 区间为 w/6≤c≤min(w/2,sqrt(ae))，
(c+s)/2=w/4−c/2。删去 −η²/e 后的 radicand
f(c)=(a−c²/e)(w/2−c)/2，有
f'(c)=(3c²−wc−ae)/(2e)≤(2c²−wc)/(2e)≤0。
所以 f 在 c=w/6 处最大，值 aw/6−w³/(216e)。
同时 c|η|/e≤w|η|/(2e)，得到源 (12) 的 finite bound。

radicand 的非负性由 w≤6sqrt(ae) 保证；w=0 时 c=s=b=η=0。
源稿正确保留 w|η|/(2e)，没有在 whole a,w 未知增长时称它 o(1)。
signed η 的 exact one-sided 式 (13) 更强，也没有倒置预算方向。

## 4. 0.620403… 常数、联合 envelope 与极限

不依赖 w，最大化 ac−c³/e 于 0≤c≤sqrt(ae)，临界点
c=sqrt(ae/3)，最大值 2a^(3/2)e^(1/2)/(3sqrt3)。
因此源 (15) 的 K=sqrt(2/(3sqrt3)) 与 finite error sqrt(a/e)|η| 正确。
要把它变成 (16) 的 o(1)，确实需要 a_T 有界；源明确写出该前件。

whole prime fourth 的 cyclic expansion a+e+w+4b+4η 正确。
源 (18) 保留 actual e_T；a,w bounded 后 η 的误差才能一致趋零。
以 w=6sqrt(ae)v、0≤v≤1 代入 gives

\[
 \Phi(a,e)=a+e+\max_{0\le v\le1}
 \{6\sqrt{ae}v+4a^{3/4}e^{1/4}\sqrt{v-v^3}\}.
 \tag{R3}
\]

固定 e>0 时每个 objective 关于 a 单调；compact v 上连续。
所以 limsup a_T≤A_0、e_T→e_0 的 envelope 传递合法，包括 A_0=0。
额外 whole22 上界必须限制 maximization 域，不能把 radical 单独
在 w=W_0 处代入；源 (20) 已正确说明该非单调性。

v−v³ 在 (0,1) 严格凹且正，平方根单调凹，故 objective 严格凹。
两端导数 ±∞ 给唯一最大点，位于 (1/sqrt3,1)。stationary equation
(3v²−1)²=9sqrt(e/a)(v−v³) 正确；区间条件排除平方引入的错误根。

## 5. sharpness 模型与实际范围

源 (22) 的 roots 满足 t²=βt+c/e，按所列 p± 有 Et=0、Et²=c/e，
Et³=βc/e、Et⁴=(c/e)²+β²c/e。取 d=2、L±⁴=2ep±、H±=t±L±，
即可逐项得到 prescribed a,e,c、η=0、s=c、w=6c、b=βc。
故 b²=ac−c³/e=aw/6−w³/(216e) 准确取等。
端点 β=0、w=6sqrt(ae) 也合法；w=0 可另取 disjoint supports。
重复 block 可以放大维数，不要求 p± 为有理，因为其权重编码于 L±。

因此 K 对这些所列 fourth trace 条件 sharp；对每个 w 的 equality
也证明 R3 是这种信息松弛下的 sharp envelope。其 first/second 或
prime geometry 并未匹配，源稿没有声称对更多真实数据也 sharp。
exact example (a,c,b,η,w)=(6,2,2,0,12) gives F=27，代数一致。

这些都是数据模型，不是实际 AF prime matrix 的反例。它们不证明
实际31不为小量，也不排除额外 arithmetic、parity、background joint
信息带来的改善。整个 actual high4 仍未支付；bounded high4 若成立，
普通 Hölder 本来就给31/22 bounded，新成果是严格常数与联合 Schur saving。

本审查没有发现阻断问题。源稿可以按以上限定范围接受。
