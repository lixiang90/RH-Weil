# C013：MV 原件、实际成长账本与旧范围独立审查

2026-10-14；审查者 c013_source_scope。恢复 AGENTS、README/STATE、check/show、
新 Goal、MACRO_FRONTIER、C013 和 D20261014N 后执行。
现场起点 HEAD 为 6657ca447bba75a03c8a7e947f244806de64d7ec，工作树当时干净。
root 的运行 Goal 身份以 root 现场查询为准；本辅助不查询或修改另一层运行态。
只写本审查件，不改 STATE/cadence/Git，不运行科学 producer、数字拟合或矩阵扫描。
本次审查本身零研究轮，是否结算新命题由 root 的完整证据负责。

## 1. 审查结论及准确来源

原 MV finite mean、multinomial k! 与 time-band trace 桥均为已有工具。
本轮核对其原常数、所有 k 的量词和实际成长参数，未见阻断下列消费的漏洞：

    log(1+|E_L|), log(1+n_-(Q_L))
        ≤ S_L + O(S_L log L/L),  L→∞。

这里 S_L 为真实全部 primepowers 的正绝对质量，E_L 是实际 Γ−2ReP<1 的
全实频坏集，Q_L 为完整 actual Weil 型。但 root/另一逆审指出必须恢复旧 016
exact degree profile。再次原件核算后确认：旧 graph 分解与旧 027 直接组合，
在 actual 规范下已经给出更强的

    log(1+n_-(Q_L))≤S_L+A(e^L)+O(L)， A(e^L)=O(e^(L/2))。

所以仅与弱 Fourier absolute 的 2S_L 比较，会制造错误的新净后果。
高矩全坏集 upper 可以成立，不能据此登记新的完整 Q 谱改善。
初稿未读 016 §5 时作出的净改善判断现已撤回；第 7 节记录复核及准确 endpoint。
以下 source/growth 推导只核候选公式真实性，不付 whole PSD、成长正性或 Ξ 识别。

一级原件为 [Montgomery–Vaughan 1974, Hilbert's Inequality](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)。
核读原文 p.74–75 的 Theorem 2 / Corollaries 2–3，尤其 (1.6)、(1.8)–(1.11)；
文本提取漏公式，另用 Poppler 渲染并视觉复核完整相关页。
本地原 PDF 为 `literature/background/montgomery-vaughan-hilbert-1974.pdf`，SHA256
`0dbcddf24bc41c65d1920c59aafe7fe85f13a7519b0edf9be9164c84d1cc6db4`。
未宣称本次重新证明原作者 Hilbert 不等式或世界优先权。

## 2. 2π、区间平移与任意 k 的正确消费

原 Theorem 2 (1.6) 给 distinct real λ_r、最小正间距 δ 的 Hilbert 二次和
绝对值 ≤πδ^-1 Σ|a_r|²。展开时间积分有两个 endpoint；
Corollary 2 (1.8) 的精确形式为

    ∫_0^T |Σ a_r e^(iλ_r t)|²dt
       = (T+2πθ_1 δ^-1) Σ|a_r|²， |θ_1|≤1。

Corollary 2 (1.9) 的局部间距版本是 3π，不是 2π；
Corollary 3 (1.11) 使用绝对 O(n)，并没有单独声明 2π 的加权常数。
本消费只用 (1.8) 的 minimum-spacing 版本，故明确常数 2π 有原件依据。
长度 T>0 的任意左端点 A∈R，只把 a_n 换成 a_n n^(iA)，模不变。
若 integer support n≤N，log n 相邻间距 ≥1/N；support 只有一项时直接积分即可。
因此 finite Dirichlet polynomial 满足

    ∫_A^(A+T)|Σ_(n≤N)c_n n^(it)|²dt
       ≤(T+2πN)Σ|c_n|²。

设 X=e^(2L)，a_p=(log p)/√p、P_1=Σ_(p<X)a_p p^(it)、V=Σ_(p<X)a_p²。
对任意整数 k≥1，unique factorization 使 product n 的 prime exponent vector α
唯一，Σα_p=k，系数 c_α=(k!/∏α_p!)∏a_p^α_p。
逐项 m_α²≤k!m_α，再用 multinomial theorem，准确得到

    Σ_n |coeff(P_1^k;n)|² ≤ k! V^k。

重复 prime 已包括，不要求 squarefree，也没有固定 k 的隐含常数。
所有整数 product n<X^k，因此安全长度可取 N=ceil(X^k)，
得 (T+2πceil(X^k))k!V^k；任意 k、L、T 均有效。
若要 X^k≤T 后简化，注意 ceil(X^k)≤T+1，而非 literal ≤T。
T≥1 时可用 (1+4π)T；也可直接选 N=ceil(X^k)−1≤X^k≤T，
得到 (1+2π)T。任何一种全程一致的常数都足以付下述成长结论。

## 3. 实际算术库存：Chebyshev 足够，proper powers 不可删

这里原 Λ(p^j)=log p，不换成 log(p^j)。置

    S=Σ_(p^j<X)log p / p^(j/2)，
    D=Σ_(p^j<X,j≥2)log p / p^(j/2)，
    V=Σ_(p<X)(log p)²/p。

旧 [291 §7](../../../notes/291-sharp-polynomial-square-negative-trace-certificates.md)
已给自含双边 Chebyshev 证明，本次亦逐步核算：
∏_(n<p≤2n)p 整除 C(2n,n)，故 θ(2n)−θ(n)≤2n log2。
二的幂处求和和单调性给 θ(x)≤4(log2)x（x≥2）。
ψ(x)=Σ_(j≤log_2 x)θ(x^(1/j))≤C x。
另一方面，每个 prime power 对 log C(2n,n) 的 Legendre coefficient 为 0 或 1，
故 ψ(2n)≥log C(2n,n)≥2n log2−log(2n+1)。
取 n=floor(x/2) 得 ψ(x)≥c x 于充分大 x；常数与 x 无关。

partial summation 给 Σ_(p≤y)log p/p≤4log2·(1+log y)；
平方项对应 y=√X=e^L，完整贡献为 O(1+L)。
三次以上的项保留全高度绝对界

    Σ_p Σ_(j≥3)log p/p^(j/2)
      ≤(1−2^-1/2)^-1 Σ_(n≥2)log n/n^(3/2)<∞。

所以 D≤C_D(1+L)，并非 O(1)。
例如无需导数符号处理，用
V≤log X·Σ_(p<X)log p/p≤C_V(1+L)²，足够且合法。
对全部 ψ 的相同分部求和，上界 S≤C e^L；
下界 S≥X^-1/2 ψ(X^-)≥c e^L 于充分大 L。
严格 cutoff 的至多一个边界 Λ(X)≤log X 不改变此下界。
于是

    c e^L≤S≤C e^L， log S=L+O(1)。

这不读取 ζ 零点，不用 PNT 误差、PNT 渐近或暂停的零自由输入。
旧 [455 §2](../../../notes/455-whole-proper-power-fourth-norm-and-prime-equivalence.md)
的同一完整 proper-power O(log X) 上界可作为已付资产，不能登记为新结果。

## 4. 完整 Γ 下界的原式、余项与端点

实际 Γ(t)=Reψ_digamma(1/4+it/2)−logπ=2θ′(t)。
用 [NIST Binet digamma 原式](https://dlmf.nist.gov/5.9#E15)，
z=5/4+it/2、z_0=z−1，ψ(z_0)=ψ(z)−1/z_0。
对 t>0，|u²+z²|≥|Im z²|=5t/4，
而 ∫_0∞u/(e^(2πu)−1)du=1/24，完整 remainder 绝对值 ≤1/(15t)。
Re log z≥log(t/2)，两项被减 reciprocal 的实部满足

    Re(1/(2z))≤5/(2t²)， Re(1/z_0)≤1/t²。

所以全 t>0 的准确 lower 为

    Γ(t)≥log(t/(2π))−1/(15t)−7/(2t²)。

t≥15/4 时后两费 ≤1/t；这与旧 537 原来源的下界及 541 的完整渐近相容。
原 Γ 单调/偶性亦由旧 digamma 差式逐项支付，不把 half helper 代入阈值。
在 T≥15/4 的 band [T,2T] 上，令 R=log T，则

    u_T=(Γ(T)−1)/2−D
       ≥R/2−D−(1+log(2π)+1/T)/2。

u_T≤0 的 band 必须付全长，不能取其平方分母继续套小坏集公式。
真实 P=P_1+P_pp，|P_pp|≤D；故 b=Γ−2ReP<1 确实蕴含 |P_1|>u_T
（u_T>0）。Γ tail、所有 primepowers、原 norm 均在这一步保留。

## 5. 候选全 band 成长率的独立核算

令 E={t:b(t)<1}。选择 terminal

    T_*=2π exp(2S+2)， R_*=log T_*=2S+O(1)。

由上节 Γ lower 和 |P|≤S，充分大 L 时 |t|≥T_* 有 b(t)≥1，
故 E 精确在该高度外为空。取 head T_0=exp(L³)，负频由 even b 精确翻倍。
head 的绝对长 ≤2T_0，log head=L³+O(1)=o(S)。

其余取 [T_j,2T_j]，T_j=2^jT_0、T_j<T_*，最后一块允许超出 terminal。
固定真实 X,L,S,D,V；不能随积分变量改变 sharp polynomial。
令 R_j=log T_j、k_j=floor(R_j/(2L))≥1。
R_j≥L³，D=O(L) 给 u_j≥R_j/3 于充分大 L，统一于所有这些 bands。
上节 finite mean、k!≤k^k 以及 V≤C L² 给

    |E∩[T_j,2T_j]|
       ≤C T_j (C_1 L/R_j)^(k_j)。

在 C_1 L/R<1 的范围，用 k≥R/(2L)−1，得到

    log band upper ≤f_L(R)+O(1)，
    f_L(R)=R−[R/(2L)]log(R/(C_1 L))+log(R/(C_1 L))。

f_L′(R)=1−[log(R/(C_1L))+1]/(2L)+1/R。
因 R≤R_*=2S+O(1)、log S=L+O(1)，其导数最终 ≥1/3，
所以所有 band upper 都由 f_L(R_*) 支配。
准确计算给 f_L(R_*)=S+O(S log L/L)+O(L)。
band 数为 O(S)，额外 log 费用 O(log S)=O(L)；加 head、负频和 1 后，

    log(1+|E|)≤S+O(S log L/L)。

这条推导没有先求最优 k，没有要求 T_j≥X^k 后丢 ceil 误差，
也没有把相对 density 当成 absolute measure。
固定二矩/纯 Fourier absolute cutoff 的同一账本只给 log scale 2S+o(S)。
因此该候选改善这份特定弱频率 ledger；能否给新的 whole 谱后果还须扣除
所有可消费旧分析桥，不能从这一 weak comparison 登记新增突破。

## 6. 完整 Q / 旧运输桥的范围

Fourier convention Ff=∫f(u)e^-itu du、I=(-L,L)，Lebesgue L²。
完整 Q 是 (2π)^-1∫b|Ff|² +2|C(f)|²−2|S_pole(f)|²。
b≥−B、B=2S−Γ(0)>0，E 外 b≥1。time-band B_E 为 positive trace class，
Tr B_E=L|E|/π。删除本征值 >1/(1+B) 的有限空间，补空间 multiplier form 非负；
再删除唯一 sinh(u/2) 锚方向，odd negative pole 才被支付，positive even pole 保留。
旧 [027 §2](../../../notes/027-phase-volume-hodge-index.md) 的此分析桥因此给

    n_-(Q_L)≤1+(1+B)L|E|/π。

这对全部 complex Dlog 闭型域/重数成立，不要求 finite matrix PSD；
Q 的闭型域与 smooth form core 可消费旧 537 的已付桥。
prefactor 的 log=O(L+log L)=o(S)，故上节测度式确实传到

    log(1+n_-(Q_L))≤S+O(S log L/L)。

若更严地写 floor，只会改善 integer 上界。本审查不把此旧 trace 定理算为新增。
中心井、任意 source 的实际 Fourier concentration 和可能负 core 没有消失。
原 027 pure phase-volume→RH 障碍继续有效；候选结论只是允许负惯性的 upper。

## 7. 更强旧基线与 ≤538 资产的定向扣除

root 和独立 whole 逆审指出未读的旧
[016 §§1、5](../../../notes/016-prime-graph-hodge-inequality.md)，本审查随后全文核至 §5，
并核 [actual normalization erratum](../../2026-10-13/c003-full-source/normalization-erratum.md)。
旧文记 ell=log λ、总区间长度为 2ell，本合同 half-window L=ell。
取 A_<(x)=Σ_(n<x)Λ(n)/√n，严格 cutoff 的 S=A_<(e^(2L))。
每个 a=log n<2L 的 partial graph 完成平方精确为

    −2Re h_f(a)=E_a(f)−∫d_a(u)|f(u)|²du， E_a≥0。

d_a 为两个可重叠子区间指示函数。degree 的正确 a.e. profile 是

    D_L(u)=A_<(e^(L−u))+A_<(e^(L+u))。

旧原文在 (25) 定义 A_< 却在证明写 ≤ cutoff；等号发生于有限多个 u。
在这些零测集采用 closed-indicator convention 有 boundary-atom 差，
不改变 graph 型积分、a.e. profile 或 essential operator norm。
若 u≥0，第一项 ≤A_<(e^L)，第二项 ≤S；u≤0 时交换两项。因此

    d_*:=||D_L||_∞≤S+A_<(e^L)。

全部 primepowers 权仍为 Λ(n)，不只 genuine primes。
丢 graph 的正项而保完整 actual Γ 与双 pole，给所有 complex smooth / Dlog 源

    Q_L≥Γ-form−d_*||f||²+2|C(f)|²−2|S_pole(f)|²。

Γ-only 坏集 E_*={Γ<d_*+1} 由第 4 节 paid lower 支付
|E_*|≤4π exp(d_*+2)。multiplier ≥Γ(0)−d_*，outside E_* ≥1，
所以第 6 节旧 trace/pole 桥给

    n_-(Q_L)≤1+[1+d_*−Γ(0)]L|E_*|/π，
    log(1+n_-(Q_L))≤d_*+O(L)≤S+A_<(e^L)+O(L)。

partial summation 的旧 Chebyshev upper 给 A_<(e^L)=O(e^(L/2))。
这只是准确组合 ≤538 旧 graph/Γ/trace 资产，不认证旧 half 数字，
不是新的算术定理，也没有用旧 erroneous m_half 作实际谱底。

第 5 节具体 high-k majorant 的 terminal exponent 为
S+S(log L)/L+O(S/L)，远大于旧 graph 的 S+O(e^(L/2)+L)。
即便只保 O 表示，所谓“从 2S 改到 S”的 whole 主阶结论已被旧资产覆盖。
不能为保持合同成功而舍弃更强旧基线，或把同主阶不同弱对象当新的宏观谱约束。

本次全文核 018、150、223、455 与 027；核 267 §§1–4、8；
核 hybrid signed physical 13 原稿 §§1–3 及独立 radial 审查对应范围；
又核 016 §§1–5/actual erratum；另作 notes/reviews 相关关键词定向检索。
结论限这些已读对象，不声称全文库/全球查重。

| 旧件 | 已付范围 | 此次不能重登；未覆盖的区别 |
|---|---|---|
| 016 | actual partial-graph identity、完整 degree profile 与 essential sup | 已给强 whole 参考 S+A(e^L)；仅比弱 Fourier2S 无效 |
| 018 | actual full-primepower 二矩、固定 θS strong density、中心井及 prolate | 不重登均值；未给 growing arbitrary-k 与 actual Γ moving threshold 的全 absolute badset→whole index 成长率 |
| 150 | arbitrary-p barrier-capacity 与 MV/Abel Cauchy weighted trace，square-root core | 形式 p-moment 旧有；不是 sharp Q_L 原 L²、unweighted 全 E 与 growing-k 净 index |
| 223 | arbitrary-shift Hilbert-valued MV 与 fixed finite frame product k=2 good heights | 不重登平移/有限 mean；不能移植其有限 frame 到全部 Q_L Dlog |
| 267 | actual Abel σ-权 primepower 四矩碰撞及 weighted 高频尾 | k=2、另一源/归一化；未付 arbitrary-k sharp prime polynomial 的 Γ allband |
| 455 | complete sharp properpowers 全-height O(log X)、原 AF S4-small | D=O(L) 已有；不能用 finite S4 转成此全 complex Q 的 PSD |
| hybrid physical 13 | unique factor k!、fixed k=2,3 product energies、实际物理 signed placements | factorial 思想旧有，其零自由前件/有限 frame 不消费到本轮；此处不恢复暂停比例路线 |
| 027 | time-band trace、whole inertia/pole+1 一般桥；中心井 pure volume 障碍 | 全运输定理旧有；新 measure 仍须严格超越强 graph 基线才有谱净值 |
| 291 | 自含 ψ(x)≍x 与 sharp/Abel 两端规模 | 双边 Chebyshev 非新结果；此处只核其 actual S_L 成长账本 |

上述已读旧件的准确组合已经给更强 S_L+o(S_L) 的同对象全惯性上界。
高 k 随 L/T 成长、实际 Γ moving threshold 与全 badset 的联合账本有不同中间对象，
但当前运输后的 whole 后果弱于基线，不满足合同的新谱准入成功门。
不能宣称新的 MV、factorial、Chebyshev 或 concentration 定理。
若 root 最终稿改变阈值、support、范数或高矩 schedule，必须重新核运输。

## 8. 宏观限定与继续责任

本审查改变的是 C013 成功判断：原候选高矩公式通过，但新 whole 净后果不通过。
实际瓶颈仍是联合 graph/degree/Γ/pole/source 的成长责任；
固定高 k factorial 工具及 pure measure 运输没有削弱它。
不能以这次公式审查、止损或旧基线组合完成 Goal。
建议按合同止损；重准入须来源适应或实际 joint 算术信息，给严格优于
S+A(e^L)+O(L) 的同对象 net，或实际付款一个尚未解决的正性/识别关键前件。
不得仅优化 k、增 N/精度，或把弱 reference 当新基线以维持合同成功。
没有待续科学 handle。审查原件和本辅助文件足以恢复本次消费范围。
