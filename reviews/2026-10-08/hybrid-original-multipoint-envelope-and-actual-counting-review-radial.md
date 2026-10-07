# 原多点包络与实际零点计数独立全文审查

2026-10-08。审查者：radial_review。结论：**限定 PASS**。本人 FULL READ compression 最终研究源全部421行，独立核验两条实际桥、有限谱包络、280种分块平均、重数/惯性消元及极限顺序。未发现阻断；所得比例是原解析输入之下的渐近下界，不是 RH 证明、世界纪录或端到端 Lean 认证。

## 1. 最终证据对象与范围

SHA256 的 canonical LF 规则为原 UTF-8 字节 CRLF→LF、孤立 CR→LF，不删 EOF 换行。

| 对象 | canonical LF SHA256 | LF 字节 |
|---|---|---:|
| [被审完整计数研究源](hybrid-original-multipoint-envelope-and-actual-counting-research-compression.md) | 59b399445a3022ce9b5ee6c064660e1602dab6d5641d3793649f16f509fc5efa | 16963 |
| [root 固定来源与数学核读](hybrid-multipoint-spectral-envelope-source-read-root.md) | 2c4a81a9a2d860e3d0882edb8a1a5928cda318679874c9be9b0adf18576b5dc5 | 5933 |
| [本轮有限重放脚本](../../scripts/hybrid_multipoint_cap_replay.py) | 8ac87f18cf928a51771556168e5af07400a3ba0333196b3e410394d8e4c37d05 | 11337 |
| [七点完整运行输出](../../output/hybrid-multipoint-seven-primary-replay.json) | aa6885489c1d0086bca32b72d27fc7a2a5f44a48f78483a057f23a59e5a828e6 | 2108 |
| [纯有理三点输出](../../output/hybrid-multipoint-three-rational-replay.json) | 4ee77471d08503c22a848e47a17713b44bd5f2afb95bfd57d994e878d9192456 | 1989 |
| [精确代数输出](../../output/hybrid-multipoint-cap-exact-algebra.json) | d84077ab71b47d1ea253cad9675fa8c25f9aa4dade775ad73ff53033167625c3 | 3367 |
| [304 完整 Hilbert 接口](../../notes/304-mt-triple-geometry-and-second-moment-stability.md) | 03f21ab1749157ff45bc4d4f62709e2a5482257c7155e7e8e644da0ac4521bc4 | 26598 |

另逐页读归档 AF v2 PDF 第4–7、11–12页的原窗口/列、Poisson–Gabor 恒等式、pull-back 惯性、Trace/Tail 命题、Theorem5.7与原计数闭合。原件 raw SHA 6de3b156342e7b4a802c34f8ef40432567e9dabe006938da04233f19fc4ef444。这里核的是本源调用的确切 [R] 输入及其适用对象；没有把这一局部核读表述成重新证明 AF 全文所有解析前件。

304 的§2、§3、§5已完整重读。固定外部来源、七点 verifier、舍入、精确有理三点和包络的另份审查为 [knownsource review](hybrid-multipoint-spectral-envelope-source-review-radial.md)。本审查不以已有审查代替对新421行实际计数证明的全文阅读。

## 2. 范数至多1的列与有限惯性不等式

被审(4)保留了 trP≤s，而未把近单位对角误当成精确单位列。必要时补零到维数至少 s+b，谱移位 λ_(b+i)(A)≤p_i 对负 A 谱仍有效。函数 F(t)=4t−t² 在 t≤p、p≥0 上的上界恰为
\[
 \phi(p)=2p+1-j(p).
\]
前 b 个谱费用至多4b，后 s 个恰是 G 的全部谱；j(0)=1只在 G 的这 s 个谱中计入，不在环境补零中重复添加。得到
\[
 4\operatorname{tr}A-\|A\|_{\rm HS}^2
 \le4b+2\operatorname{tr}P+s-\operatorname{tr}j(G)
 \le4b+3s-J.
\]
只用标量凸性，没有 operator convexity 前件。

从 s+2b≤N_c 得(5)简单点式，从4b+3s≤N_c+2D_c得不同点式。这两个消元已独算；不同点结论绝不是免费 D≥(N+s)/2。一般高重数配置会否定后一式，本稿没有偷用它。

## 3. 完整 AF 算子、原 S1 尾项与真实归一化

被审§3对象与原 AF v2 §2.2–2.3完全匹配：L=log(T/(2π))、h=2π/L、α_k=T+kh、d=floor(LT/(2π))，固定原 χ 与 MT 窗。φ只在原支撑区间内按平方根公式取值、区间外为0；γρ=(ρ−1/2)/i 的实部为普通高度。简单临界线列是 vρ/√(a_L L²)，全无限格 Poisson 给其有限列范数≤1。

A是 I′=[T−√T,2T+√T)内所有零点的实际实自伴有限算子，不是只含临界线点的 PSD 替代物。离线对 v,bar v 的总块
\[
 2m_\rho(aa^T-bb^T)/(a_L L^2)
\]
保留了正负 signature。重复实点至多贡献一个正方向，离线对至多贡献一个正方向；pull-back 只减正惯性。因此 n_+(Q)≤s_2+p，且重数给 s_1+2(s_2+p)≤N(I′)。不同点恰为 s_1+s_2+2p。原 Weil 正性或 RH 均没有被加入前件。

原 Proposition4.3 的尾合同是**未归一化** ||Etilde||_1=Oχ(T^−1/2)。结合原 trace 和二阶均值，A的 trace=N(I′)+o(N(I))、HS²=(R0+o(1))N(I)。本稿给出的 HS 平方传递费用使用 HS 范数乘真正小的尾范数，量纲正确；没有把 normalized o(N)当成可用的未归一化 o(1)。

I′与I的差为O(√T logT)重数，删除中心格两端 L²个位置单位只删普通高度O(L)、重数O(L²)。两者均o(N)。全 Gram pinching 可把其余块的非负 j 迹丢掉，但没有删原完整 A 的离线 signature。(8)因此继承的是同一完整 trace/HS/inertia 预算。

保留中央列距物理格端至少 D≍L。原实轴 r^−2 尾平方求和除 a_L L² 给 O(1/(LD³))=O(L^−4)，均匀对角为1−o(1)>0。全格 kernel 的 h与2π归一化正好产生
\[
 \widehat{\phi^2}(h(x_i-x_j))/(a_L L)
 \longrightarrow k_0(x_i-x_j).
\]
这里只在固定实跨度使用一致近似，不在增长复带上误用此误差。

## 4. 七点聚合、完整谱包络及实际280点块

有限证书(10)的单窗口压力为1/3000。对 m−6个连续七点窗口求和，每gap至多出现6次，每跨度 r≤6 的pair至多出现7−r次；正系数给
\[
 E_m+\operatorname{span}/500\ge (19/5000)(m-6).
\]
E_m包括全部pairs，额外pairs非负，方向正确。这里1/500来自聚合，不是原 local pressure。没有将三点证书另加到同一 Gram 谱缺陷上。

包络(12)–(13)允许多个大特征值，已独算 Cauchy 分支。g_m连续、递增且1-Lipschitz，E+x≥A推 J+x≥g_m(A)。固定 m280 的 A=2603/2500 与
\[
 C=2603/700000+2\sqrt{726237/700000}-1
\]
逐项与脚本相符。

实际 G_B并非单位对角。小跨度时 D_B G_B D_B才是准确 correlation matrix；固定 m与统一对角近似使 Frobenius 误差o(1)，Hoffman–Wielandt和 j 的2-Lipschitz使谱迹误差o(1)。大跨度分支直接用 j≥0与C≤A，不要求核近似。小跨度阈值应是500A=520.6，本源已正确取固定R521，没有沿用m269的旧500阈值。于是(17)对全部实际满块成立，并且误差统一。

## 5. 原计数的280 offset平均及不同点消元

满块取连续的简单临界线位置。对每种offset，pinching只需标量 Jensen；遗留两端固定至多2(m−1)列。280种offset的满块数平均S°/280+O(1)。每个相邻gap最多在279种offset的span中计入，所有gap总长≤d+O(1)=N(I)+o(N(I))。故
\[
 J^\circ\ge(C/280)S(I)-279N(I)/(500\cdot280)-o(N(I)).
\]
不假设单个gap小，也不要求全部blocks紧跨度。每块统一o(1)乘O(N)块仍是o(N)，m、R、χ均在T之前固定。

记 c=C/280、α=279/(500·280)。从(8)第一式得到
\[
 (1-c)S\ge(C_0-\alpha)N-o(N),
\]
1−c>0。于是 p=(C0−α)/(1−c)。不同点同时使用(8)第二式和同一J下界，再代入已经获得的S≥pN：
\[
 \liminf D/N\ge
 (1+C_0-\alpha+cp)/2=(1+p)/2.
\]
最后等号由 p=C0−α+cp，而非任意矩阵/零点配置的免费计数不等式。全推导没有用待证p自举几何块数。

本人已实际只读 algebra --check PASS，输出给出严格有理包围并确认
\[
 p>673009652279/10^{12}>p_{270}>p_{269}.
\]
m280只是一个明确足够的固定选择，没有未经证明地声称全整数m最优。

## 6. 304的精确单位列桥与两个极限

被审§7正确取每个固定δ的实偶光滑ηδ，fδ=ηδ²在L1及L2趋f0；原304去权用Qδ及其二导数两份固定测试函数，恢复完整双和，含全部非实零点。真实自伴算子trace精确N，HS²=(Rδ+oδ(1))N；简单实点列精确单位，位置范围长度X_T/N→1。

实轴核差≤εδ，两核模≤1，每平方差≤2εδ，故
\[
 |E_\delta-E_0|\le2m(m-1)\varepsilon_\delta=e_\delta.
\]
因这是真正全实轴一致误差，此桥可处理所有span；不需要另设紧跨度cutoff。先固定足够小δ，使A−eδ、C−eδ正；用包络得到块下界C−eδ。有限稳定性、offset平均及重数消元沿用同一实际账本，先T→∞给pδ和(1+pδ)/2，最后δ→0恢复p280。

没有取δ=δ(T)，没有假定未知统一导数预算。另一条由dyadic窗口求前缀的方法也成立：固定充分大低高度起点，低部贡献相对N(T)消失；不把只有单序列的liminf当成任意窗口统一输入。

## 7. 执行归属与最终范围

Compression执行原seven首次完整栈覆盖，并再次完整只读 --check；相应确定字段一致。本人 FULL READ原verifier、runner和输出，并独立执行 rational-three --check 与 algebra --check，两项PASS；没有声称第三次seven执行。代码/浮点舍入/Arb凸证书方法的详细独审见第1节链接。

新结论为：在原明确[R]解析合同与本轮完整有限证书下，简单临界线渐近比例至少p280=0.673009652279136912…，不同零点至少(1+p280)/2=0.836504826139568456…。原norm、原尾、完整复零点的正负signature、实际重数、两极限及所有分块费用已经在本源保留。

限定PASS不表示重新证明AF全文或304所引所有外部解析定理，不表示外部同行评审/Lean闭包已完成。它确实高于项目304三点基准及ainta旧m269装配；更高公开候选和已知Schwarz包络优先权均明确保留。未支付原signed near共振的常数级四矩、未改善无零边界、不宣称世界纪录或RH完成比例。
