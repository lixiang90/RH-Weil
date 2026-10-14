# 实际完整 prime 邻接：cosh 加权 Schur、全源费用与 sharpness

2026-10-14；root 指派独立 full-prime 费用门。不改前一 theta raw、不改 STATE/cadence/Git。
新任务后重新恢复 AGENTS/README/STATE/check-show、同 Goal/frontier/C021 stopped/D20261014AA/战略，
固定 0c4f/≤538。入口 HEAD `1d48bd538cd176091dbec90eeca46253a1473d70`；公共文件正有 root 编辑。
前一 theta gate 源恢复/修复费用没有 independent balanced positivity；本稿是不同的可判全源范数费用。
数学结算/合同准入仍由 root 对 strongest-old net 审核；本稿不自行计轮或建合同。

必要原件：016 的原 partial translations/degree/pole；030 的 actual endpoint PNT rank-two 通道；
028 的独立 negative-trace 接口；543 的 actual Γ 与 strongest old cofinal budget。
经典 PNT 已是旧输入，另核作者 [Tao 246B Notes 4，Theorem 6](https://terrytao.wordpress.com/2021/02/12/246b-notes-4-the-riemann-zeta-function-and-the-prime-number-theorem/)
（2021-02-12，2026-10-14 web 现场读 theorem body，不消费 comments）：ψ_≤(x)/x→1。
没有新增/优化 zero-free region，没有使用 RH 或实际零点位置。

## 1. 原对象、量词和 strict cutoff

ALL L>0，I_L=(−L,L)，H_L=L²(I_L,du;C)，r 在 I 外零延拓。
原 Fourier `hat r(t)=∫r(u)e^(−itu)du`；actual Γ=Reψ(1/4+it/2)−logπ=2θ′。
定义 full symmetric prime adjacency

    A_L r(u)=Σ_(q<e^(2L)) w_q[r(u+logq)+r(u−logq)],
    w_q=Λ(q)/sqrtq,
    Λ(q)=logp if q=p^k, k≥1; otherwise 0.

保留全部 proper prime powers；boundary q=e^(2L) 没有正长度 overlap，严格排除。
每项 partial shift 有 norm≤1，有限和给 A_L bounded selfadjoint。
它的 kernel 是非负测度，order-preserving；**不是**声称 quadratic form A_L≥0。
ALL complex r∈H_L 有 exact

    ⟨r,A_Lr⟩=2Σq w_q Re∫_(−L)^(L−logq)bar r(u)r(u+logq)du.

完整实际 Weil 型在原 Dlog 为

    Q_L(r)=qΓ,I(r)−⟨r,A_Lr⟩+2|C(r)|²−2|S(r)|²,
    C(r)=∫r(u)cosh(u/2)du,
    S(r)=∫r(u)sinh(u/2)du.

这里 A 的 factor2 已由 ± shifts 包含；不能在 Schur bound 后再乘 2。
本稿 prime bound 对全部 H_L，不只 smooth、bandlimited、even、principal 或 theta profiles；
消费到完整 Q 时仍须保原 Γ/Dlog/两个 pole 与独立惯性证明。

## 2. 加权 Schur 的 exact ψ/B 原账本

取 W(u)=cosh(u/2)>0 on I_L，外置0；这只是测试 kernel 的 Schur 权，没有改原 H_L norm。
定义

    ψ_<(x)=Σ_(q<x)Λ(q),   B_<(x)=Σ_(q<x)Λ(q)/q,   x≥1,
    x_−=e^(L−u),         x_+=e^(L+u).

ALL interior u，完整 exact ratio 是

    F_L(u)=A_LW(u)/W(u)
      ={e^(u/2)[ψ_<(x_−)+B_<(x_+)]+
         e^(−u/2)[B_<(x_−)+ψ_<(x_+)]}
           /(e^(u/2)+e^(−u/2)).                           (1)

验证：positive shift admissible q<x_−，其 w_q W(u+logq)
=Λ(q)[e^(u/2)+e^(−u/2)/q]/2；negative shift q<x_+，其值
=Λ(q)[e^(u/2)/q+e^(−u/2)]/2。除 W 后得 (1)。
cutoff jumping u 只有有限点，定义其值不影响型/norm；ψ_≤不能暗换 strict ψ_<。

令 β_L=ess sup_(u∈I_L)F_L(u)，则 ALL complex r

    |⟨r,A_Lr⟩|≤β_L||r||²,   ||A_L||≤β_L.                (2)

自含证明：对每条 u,v=u+logq edge，weighted AM–GM 给

    2|r(u)r(v)|≤|r(u)|² W(v)/W(u)+|r(v)|² W(u)/W(v).

乘实际 w_q、对 overlap 积分，再汇集两个方向，即得到 ∫F_L|r|²。
取 absolute Re 后不限制 complex phases；selfadjoint A 的 norm 等于 absolute Rayleigh sup。
没有使用同源系数丢失的 label norm、未知共同谱、Mellin density 或等价 Hilbert 酉化。

β_L 可用有限实际 primepower 表直接计算/认证：分割点为 ±(L−logq)，q<e^(2L)。
每个开 cell 上 ψ/B 均常数，F_L=(ae^u+b)/(e^u+1)，其导数符号固定；
故 sup 只须检查实际端点的两侧限及整个 I 的端限。不是无限 source sampling 或普通矩阵通过。
该算法说明 finite-L certificate 的真实性；本稿不运行浮点数值或将可算性代替全L证明。

## 3. PNT 必须做成 ALL x envelope，不能只取中心点渐近

PNT 给：对每个 fixed ε>0，存在 finite X_ε，使 ψ_≤(x)≤(1+ε)x 对 x≥X_ε。
令

    C_ε=max(0,sup_(1≤x≤X_ε)[ψ_≤(x)−(1+ε)x])<∞.

于是真正 simultaneous ALL x≥1 envelope 是

    ψ_<(x)≤(1+ε)x+C_ε.                                  (3)

没有把依赖 u/L 的 small argument x_− 当大参数；C_ε fixed，不能按源选择。
对于 B，用旧542/543 binomial Chebyshev 全 x≥1 bound ψ_≤(x)≤Cψ x，Cψ=4log2。
Stieltjes partial summation 保下端 ψ(1)=0 给

    B_≤(x)=ψ_≤(x)/x+∫_1^x ψ_≤(t)t^(−2)dt
          ≤Cψ(1+logx),
    B_<(x)≤Cψ(1+logx).                                  (4)

含 proper powers的 ψ 与 B 全保留。strict/closed difference ≤logx/q 或 ≤logx，
不用这个粗差去破坏 exact (1)，只用于通常 asymptotic一致性。

代 (3) 入 (1)，ψ 的主项精确消成

    [e^(u/2)e^(L−u)+e^(−u/2)e^(L+u)]
       /(e^(u/2)+e^(−u/2))=e^L.

C_ε 项恰≤C_ε；B 两项是 positive convex combination，且 logx±≤2L。
因此 ALL L>0、ALL complex original source 的统一可付证书为

    ||A_L||≤β_L≤(1+ε)e^L+C_ε+Cψ(1+2L),   ALL ε>0.        (5)

量词先 fixed ε 再 ALL L；没有声明已提供 effective ε(L) 费或高精度 threshold。
(5) 特别给

    limsup_(L→∞) e^(−L)||A_L||≤1,
    limsup_(L→∞) e^(−L)β_L≤1.                           (6)

这是真 ALL source operator bound，不用 Gaussian ground/μ transport。
原 Schur 权可能随 L 的 minimum/maximum变化，但 (2) 的原 L² norm 没有隐藏这些费用。

## 4. 原 actual endpoint 源的 sharp lower：先 fixed profile，再 L→∞

此部分是旧030 endpoint PNT 通道的直接消费，不能再次计独立新增下界。
为审 ALL prime norm 是否真有改常数的余地，仍完整核回原 source 和 factor。
固定 M>0、real nonnegative φ∈Cc∞((0,M))、||φ||²₂=1。
L>M 时，左右端点 profile source 为

    r_L^+(−L+x)=φ(x)/sqrt2,
    r_L^+(L−y)=φ(y)/sqrt2,  0<x,y<M,

其余0。两支不交，||r_L^+||²=1。r_L^− 把右支改成−φ/sqrt2，同 norm。
源皆属于 Cc∞(I_L)，actual full Γ operator domain；没有随着 L 拟合 ζ ordinate。
令 k(v)=∫φ(x)φ(v−x)dx（zeroextend φ），support k⊂(0,2M)，
ℓ_φ=∫_0^M e^(−x/2)φ(x)dx。
q 的跨端位移给 v=2L−logq，exact cross correlation 是 ±k(v)/2。
同端相关只来自 logq<M 的 finite q，其 contribution fixed O_φ(1)。
所以

    ⟨r_L^±,A_Lr_L^±⟩
      =±Σq w_q k(2L−logq)+O_φ(1).                       (7)

对 X=e^(2L)，PNT/030 weighted endpoint lemma 给

    e^(−L)Σ_(q<X)Λ(q)/sqrtq k(log(X/q))
      →∫_0^(2M)e^(−v/2)k(v)dv=ℓ_φ².                   (8)

独立组织验证：(8) 为 ∫t^(−1/2)k(log(X/t))dψ(t)/sqrtX；
其实际区间 t∈[Xe^(−2M),X]。先 fixed M/φ，在此整个 multiplicative window 上
ψ(t)=t+o(X) uniform；Stieltjes parts boundary+derivative error都是 o(sqrtX)，
主项换元 v=log(X/t) 得右侧；Λ properpowers及 strictendpoint齐全。
k 在0附近零，故 q=X possible atom甚至不影响本源，但仍采用原 strict convention。

用 Fubini 分解 convolution 后得到 ℓ_φ²。Cauchy–Schwarz 给 ℓ_φ²≤1−e^(−M)；
取 smooth φ approximating normalized e^(−x/2)1_(0,M)，则 ℓ_φ² 可逼近1−e^(−M)。
因此对每个 δ>0，先选 fixed M、fixed φ 使 ℓ_φ²>1−δ，再令 L→∞；由 (7)/(8)

    liminf e^(−L) supSpec A_L≥1,
    liminf e^(−L)[−infSpec A_L]≥1.                       (9)

这里的 liminf 写法表示让 δ↓0 后的 conclusion，不混成 profile 与 L 的未核 joint limit。
结合 (6) 得 actual all-source sharp leading scale

    ||A_L||=(1+o(1))e^L,
    supSpec A_L=(1+o(1))e^L,
    infSpec A_L=−(1+o(1))e^L,
    β_L=(1+o(1))e^L.                                    (10)

最后 β 下界来自 β≥||A||，不需估 actual step envelope 的更强 uniform remainder。

## 5. prime sharpness 不推出 full Q 负：双 pole 在同一源 leading相消

对上面固定 profile source，actual pole moments给

    2|C(r_L^±)|²−2|S(r_L^±)|²
       =±e^L ℓ_φ²+o(e^L).

这恰与 (7)/(8) 同 factor/sign；Q 中 prime是减号，所以两者 leading cancel。
actual Γ 2θ′ 的 absolute form O_φ(1)：两fixed profiles平移只乘 unit phases，
||hat r_L||² weighted log由两 profiles weighted norm支付，independent L。
故 Q_L(r_L^±)=o(e^L)，是旧030 DU的同对象结果；没有得到 Q negative、PSD、RH 或 Ξ。
这些源不是一个 finite matrix特殊样本，恰是全源 norm下界的合法 actual witness；
但 lower只约束 pure-prime scalar norm账本，signed prime/pole/fullΓ修复完全保留。

## 6. strongest-old net 与下游消费隔离

016/542 的旧 unweighted degree scalar main fee是 S_L=Σq<e^(2L)Λ(q)/sqrtq∼2e^L，
degree sup≥S_L；543 record full-source count已有 cofinal 1+C exp(S_L)。
(5)/(10) 的目标是 raw actual symmetric adjacency在 original norm 的 leading constant1，
不是把旧degree或单source的2改写成不同norm，ALL complex profiles与成长L都已付款。
但 full repository strongest-old review由root/另一代理负责；不能仅凭定向搜索未命中宣称新颖性或结算。
旧030已完整蕴含本稿 lower/cancellation；不得让这些 parts重复计功。

仅消费 (5) 可写确定的原型下界

    Q_L(r)≥qΓ,I(r)−β_L||r||²−2|S(r)|²,  ALL Dlog.

此句保正 evenpole舍去及 oddpole真实rank1，不省 Γ0。
若要推出严格优于543的 whole negative-count budget，须另外付 Γ lower/trace、
rank-one minmax、任意δ的028 count转换及与 strongest old exact split的比较。
这些不能由 pure-prime norm asymptotic自动升级；本稿没有自行声明新的完成/轮数。
同样，全source Γ-relative/polylog费用、dangerouscore、joint PSD、Ξ都未被 (10) 支付。
范数 leading1 仍指数危险规模；不能把 pure-prime sharpness当所有joint方法的 Goal3 边界。

root 消费记录：actual A_L/H_L(originaldu)；ALL L>0/ALL complex L²；full proper powers/strictcutoff/±factor；
旧PNT+Chebyshev被准确归属，ALL x envelope及weightedSchur费用已付；
actual方向完整r，不需labelmass；sharp lower是旧030；fullΓ/polecount/strong-old net另核；
无新独立正性/ζ位置假设；source与预算强度结算由root决定，公共cadence未变。
