# C013：完整实际 Weil 负惯性桥独立逆审

2026-10-14；本代理先恢复 AGENTS、README/STATE、check/show、当前 Goal、
MACRO_FRONTIER、C013 和 D20261014N。起始 HEAD 6657ca4、工作树干净。
本文件只审 actual Fourier 型、闭型域、全源惯性运输及新旧量级的净差异，
不改 STATE/cadence/Git，不生成数值样本。下面的全源桥是已付旧工具的
正确 actual 消费，不独立计为新数学轮；高矩 all-band 费用须另外原证据付款。

## 1. 对象、域与实际规范

令 L>0，H_L=L²((-L,L),du)，所有源零延拓；Ff(t)=∫f(u)e^(-itu)du。
写 X=e^(2L)、w_n=Λ(n)/√n，并严格保留全部实际 prime powers n<X：

    P_L(t)=Σ_(n<X) w_n n^(it)，S_L=Σ_(n<X)w_n，
    Γ(t)=Re ψ(1/4+it/2)−log π=actual 2θ′(t)，
    b_L(t)=Γ(t)−2 Re P_L(t)。

完整型正是

    Q_L(f)=∫_R b_L(t)|Ff(t)|² dt/(2π)
           +2|C(f)|²−2|S(f)|²，
    C(f)=∫_(-L)^L f(u)cosh(u/2)du，
    S(f)=∫_(-L)^L f(u)sinh(u/2)du。

S_L 是算术质量，S(f) 是奇极点锚，二者不能混写。
Plancherel 与 autocorrelation 恒等式给 prime Fourier 规范，
没有删 Γ 尾、proper powers、双 pole、复源或原 L² norm。
n=X 若恰是整数，其位移长度为 2L，重叠为零；本合同已冻结严格 n<X，
测度辅助对象也按这一选择定义，不无声换成另一有限多项式。

自然闭型域是

    Dlog,L={f∈H_L:∫log(2+|t|)|Ff(t)|²dt<∞}。

实际 Γ 的部分分式与渐近见 [NIST DLMF 5.7.6](https://dlmf.nist.gov/5.7#E6)
及 [5.11.2](https://dlmf.nist.gov/5.11#E2)。部分分式直接给

    Γ(t)−Γ(0)=Σ_(n≥0) (t²/4)/[(n+1/4)((n+1/4)²+t²/4)]≥0，
    Γ(0)=−γ−π/2−3log2−logπ。

Γ 是实偶连续函数、t>0 严格递增，且 Γ(t)=log|t|+O(1) 当 |t|→∞。
故 Γ 加合适常数后的 positive form 与 Dlog 范数等价；finite prime 和 pole
是 fixed L 的 L² bounded form 扰动，Q_L 因而是半有界 closed form。
这与已付 [537 §5](../../../notes/537-source-exact-weil-window-positive-tail-admission.md)
的缩支撑/weighted dilation/mollifier core、
[538 §3](../../../notes/538-actual-weil-geometric-upper-and-full-inertia-gates.md)
的 compact-resolvent 接口一致，但此处没有消费其 fixed L 正性作为 growth 正性。

compact resolvent 可独立看清：Dlog 单位球在 Fourier |t|>R 的 L² 质量为
O(1/log R)；固定 |t|≤R 的 zero-extension Fourier 限制算子是 Hilbert–Schmidt。
先逼近有限频窗，再让 R→∞，得到 Dlog→H_L 的紧嵌入。负惯性因此等于
完整自伴闭型算子的负本征值总重数，亦等于所有复线性严格负子空间维数的上确界。
以下结论适用于整个 Dlog，不只 Cc∞ 或有限 trial frame。

## 2. 精确有限测度与 trace 桥

令 B_L=2S_L−Γ(0)>0，E_1={t∈R:b_L(t)<1}。
因为 |P_L|≤S_L，b_L≥−B_L；又 Γ→∞，E_1 为有界开集。
无需把 E_1 近似成有限矩阵、忽略边界或先假设 PSD。

令 J_E:H_L→L²(E_1,dt/(2π))，J_E f=Ff|_(E_1)，K_E=J_E*J_E。
它是 positive trace-class contraction；Hilbert–Schmidt kernel 的平方范数给

    Tr K_E=||J_E||_HS²=(2L)|E_1|/(2π)=L|E_1|/π。

在 E_1 外 b_L≥1，在 E_1 内 b_L≥−B_L，所以全闭型域上

    Q_L(f)+2|S(f)|²
    ≥||f||²−(1+B_L)⟨K_E f,f⟩+2|C(f)|²
    ≥||f||²−(1+B_L)⟨K_E f,f⟩。                 (1)

取任一 m 维严格负子空间 V⊂Dlog。V∩ker S 的维数至少 m−1。
在此交空间中任一单位源满足 ⟨K_E f,f⟩>1/(1+B_L)，因为其 Q_L<0。
若 m≥2，选 m−1 个 H_L 正交单位源并求和；trace 上界给

    m−1<(1+B_L)L|E_1|/π。

若 m≤1 下列界已自动成立，所以安全的整数界为

    n_−(Q_L)≤floor[(1+2S_L−Γ(0))L|E_1|/π]+1。   (2)

若右侧 trace 比例恰是正整数，上面的严格符号还能略改整数端点；(2) 已是
本合同要求且对全部参数安全。+1 只来自 negative odd pole 的 rank-one；
positive even pole 被保留为非负项，没有付错第二个 +1。

反射保 Dlog 且所有项奇偶相容。在 even 块 S(f)=0，不需要 +1；odd 块
有 rank-one +1。直接对 whole E_1 使用 (2) 比分别用两个 full trace 更省，
不因 pairs/重数或把复域当实域漏掉方向。若另做非自对偶 paired 数据，
须逐分量相加；本合同对象只是实际 ζ 的这一 full complex Q_L。

## 3. All-band 测度给 whole 惯性的真实后果

以下消费门依赖尚须独立付款的实际 all-band 算术命题：

    log(1+|E_1|)≤(1+o(1))S_L，L→∞。             (3)

一旦 (3) 已由完整原 ledger 证明，(2) 立即给

    log(1+n_−(Q_L))≤(1+o(1))S_L。               (4)

理由是正因子 (1+B_L)L/π 的对数为 O(log S_L+log(1+L))=o(S_L)。
旧 291 的双边 Chebyshev 或本轮独立 binomial 证明已给 c e^L≤S_L≤C e^L，
明确使该费用为 O(L)，无需 PNT。
从 (2) 取 log 时须用 1+|E_1|，所以 E_1 很小或空都不产生 log 端点漏洞。
positive C 锚及 negative S 锚并不改变 leading exponent。

若还用 PNT，仅在这一另列渐近消费下才能把 (4) 写成

    log(1+n_−(Q_L))≤(2+o(1))e^L。

不把 PNT 记为未知 ζ 零点位置输入；但原 (2) 是每个 fixed L 的完全有限
actual 算术和，即使不写此 PNT 归一化也成立。

## 4. 旧 degree-profile 给出的更强 whole 谱反事实

已全文核 [018](../../../notes/018-prime-resonance-density.md) 和
[027](../../../notes/027-phase-volume-hodge-index.md)，并定向核 016/023/024/150。
旧 027 的 trace 桥及 odd pole +1 是旧资产；旧 018 给全部 prime powers
二矩和相对密度、中心井/finite prolate removal，明确没有得到 high-k actual
Γ-threshold 的完整绝对测度成长界。其原 half Γ 常数须按 016 的实际规范
纠正后才能比较，不能拿历史 numeric shift 直接消费。

若只用 Fourier |P_L|≤S_L，坏集被含于 Γ(t)<2S_L+1，terminal 频率为
exp(2S_L+O(1))；固定 k=1 的 Chebyshev 因子只删除 polynomial(S_L,L)，
仍为 2S_L+o(S_L) 的粗指数。(3) 确实严格改进这个特定 Fourier 粗测度界。
但是这并非 baseline 的全部 whole 谱资产，不能把它当最强旧界。

[016 §§1、5](../../../notes/016-prime-graph-hodge-inequality.md) 已付 exact
positive prime-graph energy 减 degree potential 以及实际空间 degree profile：

    D_L(u)=A(e^(L−u))+A(e^(L+u))，a.e. |u|≤L，
    A(Y)=Σ_(n<Y)Λ(n)/√n。

两 thresholds 的较小者不超过 e^L，较大者不超过 e^(2L)。故对 a.e. u，
只用正权和的单调性就有完全有限、保留全部 proper powers 的上界

    D_L(u)≤R_L:=A(e^(2L))+A(e^L)=S_L+S_(L/2)。    (5)

原指标端点的 ≤/< 差异只发生在有限个 u 上；乘法 form 与 essential sup 不变。
此处明确写 a.e.，避免恰 e^L 是 prime power 的 singleton 被 strict A 记号漏算。

完整 Q 的旧 exact 图分解保留正 energy 与 even pole，所以同一 Dlog 上

    Q_L(f)+2|S(f)|²≥∫Γ(t)|Ff(t)|²dt/(2π)−R_L||f||²。

令 E^Γ_R={t:Γ(t)<R_L+1}，重用 §2 的 trace 证明得到

    n_−(Q_L)≤floor[(1+R_L−Γ(0))L|E^Γ_R|/π]+1。    (6)

实际 Γ 的 uniform lower Γ(t)≥log t−G（t≥1，G 绝对常数）已由 Binet 支付，
故 E^Γ_R⊂(−exp(R_L+G+1),exp(R_L+G+1))，
log(1+|E^Γ_R|)≤R_L+O(1)。
双边 Chebyshev 已给 S_(L/2)=O(e^(L/2))=o(S_L)，
从 (5)/(6) 已给

    log(1+n_−(Q_L))≤S_L+O(e^(L/2)+L)
                     =(1+o(1))S_L。                (7)

父代理另指出可以只在单列 PNT 消费下加强这一旧反事实：若较小 threshold<2，
其 A 和为零，D≤S；若较小 threshold≥2，则较大 threshold≤X/2，
而较小 threshold≤√X，所以 D≤A(X/2)+A(√X)<A(X)=S 对充分大 L 成立，
因为比值趋向 1/√2。结合 u→L 的 endpoint degree 极限，
ess sup D_L=S_L 对所有充分大 L。这里等号点仍按 a.e. 规范。
因此 (7) 的旧 upper 还可写 S_L+O(L)，但没有把 PNT eventual 声明免费用于
每个有限 L；此加强并非 high-k 新 independent forcing，不另计轮。

这一证明只组合已付 016 exact 图分解/degree profile、027 trace、正确 actual Γ；
甚至不需要 PNT，因为 (5) 为每个参数的直接 finite 上界，双边 Chebyshev 足够。
half Γ 的历史 scalar 错误不影响图分解 (5)，此处全部 Γ 重按 actual 运输。

因此 (4) 尚未严格改善 baseline 可立即消费的 whole 谱界 (7)。
若 high-k all-band ledger 只有 leading S_L，其谱净值条件没有通过，
不能用比一个更弱 2S_L 子界好就登记“比旧 whole 谱界严格强”。
通常的 high-k 误差 O(S_L log L/L) 还大于旧 (7) 的 O(e^(L/2)+L)。
实际 b_L 坏集的测度命题仍可能是不同对象的新算术估计；但它不自动满足
C013 已冻结的 strict whole-inertia 净后果，也不能因这次新定位旧消费链再计新轮。
本段是对象相关定向旧件范围审查，不是 ≤538 全文或世界优先权审查。

宏观门必须保持准确：exp((1+o(1))S_L) 仍允许非常多负方向，
既未证明 Q_L≥0，也未付款最后 finite core 的 PSD、真最低支/Ξ 的识别、
cofinal near-PSD 或 RH。因而若 C013 本轮只取得 (3)/(4)，whole 新净值仍须
与 (7) 比较，不能据此结算成功；即使以后取得真 strict 新 whole 后果，
也须独立核稳定 Goal 第 2 项要求的
“消除关键瓶颈/严格削弱关键前件”的全部责任，更不满足第 1 项或第 3 项。
不得用数值巨大但 strict 的指数改善自动标记宏观 Goal complete。

实际瓶颈变化是新定位了 baseline 已蕴含的 S_L whole 指数界，
从而纠正 C013 的对照门；full signed positivity 与最后危险源几何仍未付。
下一次晋级需要严格越过 (7) 的同对象谱预算，或有限 core/signed 联合输入；
不能继续以 2S_L 为唯一旧对照。

## 5. 审查状态

§§1–2、旧 graph 反事实 §§4 已独立验证；§3 的 (3) 本身另核了
[独立 all-band 推导](growing-measure-derivation.md) §§3–6：
Binet 的 G=log(2π)+46/15、所有 proper powers 的 R=O(L)、V=O(L²)，
Y=2S+G+1 终端和 H=max(L³,4D,4L,4M) 的完整低 head 正确。
k=floor(y/(2L)) 使 X^k≤T，ceil(X^k)≤T+1 已付 (1+4π)T；
floor 误差保留为 +log(y/M)，F′ 在 [H,Y] 最终统一为正，
J=O(S) 的总 band 对数费 O(L)，negative frequencies 精确乘 2。
因此该 candidate actual E 测度上界有原证明，whole 运输也真；但仍不越过旧 (7)。
它严格改 k=1 的同对象 certified upper ledger，不是 E 下界、最优性或新 whole 突破。
父代理最终 note 若改变对象/threshold/schedule，须再次核其消费范围。
没有数学 producer/session；本代理文件及 source browsing 不是研究轮。

## 6. 028 negative trace 的更强旧对照（补审，零轮）

父代理要求补核最强旧 scalar Γ 消费，已原读
[028 §1 定理 DI](../../../notes/028-core-renormalized-negative-trace.md)。
旧 DI 不只有 phase-volume 计数：它控制完整 closed-form 负谱迹。
令 M≥ess sup D_L，H_M=Γ_I−M I（仍在全 complex Dlog 上），
图分解给 Q_L≥H_M−2|S(f)|²，positive even pole/prime graph energy 保留后可下界为零。
负子空间与 ker S 相交直接给

    n_−(Q_L)≤1+N_−(H_M)。

H_M 的每个 negative 本征值 λ<0 在 H_M−I 的 negative trace 中贡献 1−λ>1。
因此不用任何有限矩阵或谱估计误差就有

    N_−(H_M)≤Tr[(H_M−I)_-]
      ≤(L/π)∫_R [M+1−Γ(t)]_+ dt。                  (8)

第二不等式就是原 DI 的 actual 消费：取原非负 multiplier Γ−Γ(0)、
scalar a=M+1−Γ(0)>0，r=0。原 Γ、L² norm、closed domain 未换对象。

保留前面已核 uniform Γ lower Γ(t)≥log t−G 于 t≥1，
G=log(2π)+46/15；设 a=M+1+G>0。负频偶性精确乘 2，head |t|≤1
用 Γ≥Γ(0) 付款，外部尾在 t≥e^a 空。因此

    ∫[M+1−Γ(t)]_+dt
      ≤2(M+1−Γ(0))+2∫_1^(e^a)(a−log t)dt
      =2(M+1−Γ(0))+2(e^a−a−1)
      ≤C e^M+O(1+M)。                              (9)

其中 ∫_1^(e^a)(a−log t)dt=e^a−a−1，未把深度 M 免费乘到整宽 e^M。
因 M≥0，(1+M)≤e^M，可扩大绝对常数进一步写整式 ≤C' e^M。
故 strongest 已付 scalar Γ/degree-profile 对照是

    n_−(Q_L)≤1+C' L e^M，
    log(1+n_−(Q_L))≤M+log(1+L)+O(1)。              (10)

无 PNT 时可取有限 M=S_L+A(e^L)，得到

    log(1+n_−(Q_L))≤S_L+A(e^L)+O(log(1+L))。

单列 PNT eventual 消费 ess sup D_L=S_L 后，则旧 whole bound 为

    n_−(Q_L)≤1+C' L e^(S_L)，
    log(1+n_−(Q_L))≤S_L+O(log L)。                 (11)

因此 §§3–4 的普通 phase-volume 前因子 L S_L 还不是最强旧计数账本；
C014 heat/Golden–Thompson 必须超过 (10)/(11)，不能只改善较弱的 L S_L e^S。
本补审只是恢复 0c4f/≤538 已付 016+028 原件的直接强后果，
不登记新 arithmetic input/forcing，也不另消费 cadence。

## 7. Root 542 最终消费范围复核（一次只读，补审零轮）

已一次全文读取
[542 最终稿](../../../notes/542-actual-prime-high-moments-and-strong-baseline-audit.md)，
没有重新展开来源册或改父代理数学版本。最终 §3 的 M=4V/L、
H=max(L³,4D,4L,4M)、G=log(2π)+46/15、完整 pp/strict cutoff、
J/floor/ceil/negative-frequency 费用与已审独立 all-band 证明相同。
因此其 (3)/(4) 的 actual 全 E_L 测度估计消费准确；
其 whole Fourier 惯性整数门也与本件 §2 相同。

最终 §4 准确扣除强旧 graph profile：D_L≤S_L+A_<(e^L) a.e.，
并使用旧 028 negative trace 而非较弱 phase-volume 深度乘整宽。
其 (5) 为 n_−Q≤1+C L exp(S_L+A_<(e^L))、
log(1+n_−Q)≤S_L+A_<(e^L)+log(1+L)+O(1)，与补审 §6 一致。
另列 PNT eventual ess sup D_L=S_L 的 proof 及 endpoint 小条带正测度正确，
没有把此 eventual 声明免费用于每个有限参数。

最终判定准确：新 actual all-band 估计是一个完整准入动作，
generic MV/factorial/trace 及强旧资产恢复不各自计轮；
其 whole 净门失败，C013 一轮即止损，不据此完成宏观 Goal。
计数结算由 root 维护唯一 cadence，本代理没有修改它。
C014 killed Γ heat/record 只保存待付 target，不是 542 已证明的独立正性，
其将来晋级仍须超过最强旧 (5)/(11)、支付所有新前件，并另核稳定 Goal。
