# C004 primary Sonin source audit

2026-10-13；独立来源审查。未修改STATE/cadence，不单独计研究轮。

## 原件与核读范围

- [出版社页面](https://link.springer.com/article/10.1007/s00029-021-00689-4)：Selecta Math.27, article77 (2021)，DOI 10.1007/s00029-021-00689-4；主体订阅内容未取得，故不把下面作者稿页码冒充70页journal排版。
- [作者托管PDF](https://alainconnes.org/wp-content/uploads/Selecta.pdf)：55页，下载到`tmp/pdfs/c004/Selecta-author.pdf`，SHA256 `8a95ede70dd5343c220fbe3d5d1018cb81df7cf32274adc393dc8e40c3b8775e`。视觉核印页2、24、45；相关公式另逐页文本核读。
- [arXiv2006.13771v1](https://arxiv.org/abs/2006.13771v1)：唯一登记版本，2020-06-24，57页。该稿对应trace恒等式编号4.7、(87)–(88)；作者55页稿是4.6、(84)–(85)，不能混号。
- [2026综述v1 §7.2](https://arxiv.org/html/2602.04022v1#S7.SS2)：Theorem7.1。

作者稿Theorem1（印页2）与综述7.1给小支持窗`[2^(-1/2),2^(1/2)]`、`ĝ(i/2)=ĝ(0)=0`下的无误差Sonin下界。作者稿Theorem6.11（印页45）则写`ĝ(-i/2)=0`及误差`-c|ĝ(0)|²`，`c=4γ/log2, γ≈2.94355`；不能读成正号已印改。反演对称可将该负号版用于正号条件：实函数反演把两号互换，并保留W∞及Sonin trace。AppendixC讨论有限消失条件不改变全域RH判据，并不删除小支持限制或证明大窗正性。

## 可消费的独立输入

以下是作者稿Theorem4.6的对象接口；该**恒等式及Sonin trace正性**对所有`f∈C_c^∞(R_+^*)`成立，没有小支持假设。受小支持约束的是`W∞≥Sonin trace`的**差的符号**。

令`U_t=ϑ(exp t)`，`S`为`L²(R)_ev`上函数及Fourier变换都在`[-1,1]`消失的Sonin空间正交投影；`S`不是semi-local的投影乘积。写`f_m(u)=f_a(log u)`，则

    T(f_m):=Tr(ϑ(f_m)S)=W∞(f_m)+E(f_m),
    E(f_m)=∫ f_m(ρ^(-1)) ε(ρ) d*ρ.

`ε(ρ)=ε(ρ^(-1))`且对`ρ≥1`，

    ε(ρ)=Σ_n λ_n / sqrt(1-λ_n²) <ξ_n,ϑ(ρ^(-1))ζ_n>,
    ξ_n=P1 φ_n/||P1 φ_n||,
    ζ_n=(1-P1)F ξ_n/sqrt(1-λ_n²).

这里`λ_n`是even prolate有限Fourier特征值，可带符号；不是本合同`λ=√μ`。正trace的含义是`T(g*g*)=Tr(ϑ(g)Sϑ(g)*)≥0`，不是把单个scaling限制为Sonin空间上的unitary表示。作者稿印页2已明确scaling不保持Sonin空间。

作者稿AppendixB (154)–(155)及出版社可见AppendixB同样给

    K(t)=2θ'(t)=Re ψ(1/4+it/2)-logπ.

故本输入能与actual完整Γ项同规范消费，不能换成旧half helper。

## 两patch账本（本审查独立推导）

采用`ĝ(t)=∫g(y)e^(-ity)dy`及实Hilbert型。令`h(y)=g(y)`，`h_1(y)=h(y+a/2),h_2(y)=h(y-a/2)`，`A=ϑ(h_m)`。由卷积表示

    A1=U_(-a/2)A, A2=U_(a/2)A.

这是源移位的精确关系，不假设`U_t S U_t*=S`。`AS`为Hilbert–Schmidt；交叉产品为trace class。合法的循环trace因此给

    T_ij=Tr(A_i S A_j*)=[[s0,sa],[sa,s0]],
    s0=Tr(AS A*), sa=Tr(U_a AS A*), s0≥|sa|.

`sa`为实数，来自W∞及E的实反演对称。源内相同trace不是Sonin投影scale不变。

设`e(x)=ε(exp|x|)`，定义

    e0(h)=∫∫ h(x)h(y)e(x-y) dxdy,
    ea(h)=∫∫ h(x)h(y)e(x-y+a) dxdy.

两者皆实；`E_ij=[[e0,ea],[ea,e0]]`，由交换x、y和e偶性，与a换成−a等价。所有交叉可用原4.6恒等式；不把两个小窗对角不等式极化。

本合同`a=log2,b=log(3/2)/4,μ=13/5`满足`a>2b`和`a+2b<log3`。源支持在`[-a/2-b,a/2+b]⊂[-logμ/2,logμ/2]`；两个源内相关支持在`(-2b,2b)`，联合相关的真实primepower仅`2`。取`h=D(D+1/2)η`保留`∫h=∫e^(y/2)h=0`，每个patch及任意两patch线性组合的所有pole配对为0。

直接相关计算给真实prime账本

    P_11=P_22=0, P_12=P_21=-(log2/√2)||h||².

因此与完整实际Weil型的差是

    Δ(h):=QW_ij-T_ij
          =[[-e0, -ea-c2||h||²],[-ea-c2||h||²,-e0]],
    c2=log2/√2.

没有缺失的Γ因子、pole或其他primepowers。这里Δ的负方向不等于QW的负方向。

## 统一无费用消费的反例候选及完整证明

这一节是独立推导，不是对原文定理的重新陈述。结论应由主审及不同组织逆审后消费。

`e`在任意有限区间上连续有界：上面的表示系数级数一致绝对收敛。有限Fourier算子`P1FP1`在紧区间有smooth核，故其特征值绝对值快速下降；`|λ_n|<1`，所以`Σ|λ_n|/√(1-λ_n²)<∞`。单位向量的scaling系数连续、绝对值≤1。并且`e(0)=ε(1)=0`，来自ξ与ζ的互相正交。只需连续性，不消费数值或导数cusp的近似。

因而`(-b,b)²`上的两个核`e(x-y)`和`e(x-y+a)`皆Hilbert–Schmidt，定义compact算子。选择任意固定非零实`χ∈C_c^∞(-b,b)`，令

    η_N(x)=χ(x)cos(Nx),
    h_N=D(D+1/2)η_N / ||D(D+1/2)η_N||.

分母渐近`N²||χ||/√2`；`h_N=-(√2/||χ||)χcos(Nx)+o_L²(1)`，故`||h_N||=1`且`h_N⇀0`。每个h_N严格满足两项消失，不是近似满足。compact性给`e0(h_N)→0,ea(h_N)→0`，所以

    Δ(h_N)→[[0,-c2],[-c2,0]],
    (1,1) Δ(h_N) (1,1)^T→-2c2<0.

因此存在有限N及合法smooth generator，严格否定全η、全coeff的`QW≥T_S1`无费用拼接。无需算某个N、增加C001样本或拟合ζ零点。该极限固定真实p2权重与支持，只有source内oscillation增加。它不否定完整W半正定；高频Γ能量仍可大于该固定差。

允许误差`QW≥T_S1-C||source||²`时，此族必要`C≥c2`（因为`||h_1+h_2||²=2`）；支付这样的质量费仍未证明所有η上的比较，更未取得低谱或增长支持预算。

## 判定与下一动作

原trace身份比摘要窗更广，可合法写完整两patch差；原文没有提供使其prime交叉免费非负的来源。统一无费用Sonin桥在冻结真实prime域失败。stop针对该桥；重新准入须独立signed质量/prime费用或不同算术投影，不能以source正性、finite vanishing的RH等价或semi-local非正projection复活。宏观完整Weil正性瓶颈未变。

来源任务的唯一下一动作：主审核本文件Δ的权重、归一化和compact弱零反例，并与独立数学审查对账。不改STATE/cadence，下载已结束，无后台process。

主代理结算收据：原始PDF已按同一SHA保留于
`literature/background/connes-consani-sonin-selecta-author.pdf`（本地忽略），
追踪[source-receipt.json](source-receipt.json)记录来源/版本/核读范围。
本轮完成后下一动作由STATE的C005指定，不从本历史审查恢复旧任务。
