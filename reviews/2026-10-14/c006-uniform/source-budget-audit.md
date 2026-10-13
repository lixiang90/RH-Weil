# C006 uniform预算：实际joint负对照与局部高return乘积

2026-10-14；起始HEAD `44337d2e1492c093dcb263f5ecf57c4676eed3e6`。
恢复AGENTS/README/STATE/check/show、Goal、C006、D20261014B、533后执行。
只写本来源/反例审查，不改STATE/cadence，不独立计研究轮；没有数值扩展或零点拟合。

## 消费对象和结论等级

冻结源U、逐patch两矩零闭域V沿533；源相关跨度
`W=log√6<log3`。实际p≥3的所有primepower源相关严格0。研究的是
`D_p=T_p−T∞`在V上的完整source-L²范数，不重新追已排除的norm首项渐近。

本审查没有取得actual joint carrier norm的反例，也没有证明完整
`Σ_p||D_p||<∞`。已付的新partial是：**完整resolvent的三阶及以上δK余项
H3_p与局部源边界乘积M_p满足TC范数O(p^-3/2)||g||²，整个冻结L²单位球上统一。**
这只支付局部ordinary trace候选的可求和预算；将它识别为实际E_p的高return尾，
还缺source夹心的迹类域及成对cutoff联合极限。不能据此把actual剩余范围缩为0..2阶，
也不能按单个M2正trace补费用。

2026-10-14同轮scope纠正：先前开头和第2、5节将局部TC乘积直接消费为actual高尾，
该消费过强，现明确降级。Schatten/finite-band估计保持；本纠正不计新研究轮。

一级物理接口仍为[CCM2310.18423v2](https://arxiv.org/html/2310.18423v2)
实际θ/η及F_p，2021实位Sonin trace；原版本/字节和核读见既有receipt。
以下Schatten和finite-boundary推导为独立新分析，不把它引为原文定理。

## 1. 合法joint source和便宜模型反例审查

任取非零实χ∈Cc∞(−b,b)，b=log(3/2)/4，置

    h_R=D(D+1/2)[χ(t)cos(Rt)] / ||D(D+1/2)[χ cos(Rt)]||₂.

每个R都严格满足ℓ₀=ℓ₁/₂=0。用原patch移位形成`U(h_R,±h_R)`，
carrier可选R=c p或c p²；全部actual晚prime相关仍为0。不能把
`cos(logp·s)`的bare multiplier在频率点的大小当作这些合法源的Rayleigh值。

由532的实际Γ窗口近似，当a=logp且a<T<2a时，窗口模型的
`C_T=1_[0,T](U_a+U_-a)1_[0,T]`对同carrier向量w有

    M1_model=2cos(as)(T−a)/(2π),
    M2_model=2(T−a)/(2π),
    M2_model−2cos(as)M1_model
       =−2(T−a)cos(2as)/(2π).

因此q²return的零次harmonic精确取消。只取q²M2会伪造一个1/p质量反例。
更一般地，每fiber上B把n个格点送到n+1维中的rank n空间；它的projection
phase周期平均trace与原n点完全相同。因此完整窗口差的零次harmonic在所有q阶都为0。
R≈p²的较长chain也一样，不能凭增加return words恢复该假质量项。

532的sharp-window误差在R≈p或p²时仍远大于目标p^-2；这说明该已有误差
不足以认证joint Rayleigh，并不是actual反例。尤其交接T≈a、2a附近，
不得把hard-window的corner当作真实Sonin密度的已付stationary特征。

## 2. 角组织候选与有限boundary域

physical空间为L²((0,∞),dx)，L=1_(0,1)、H=I−L。
`F_p=B F B^(-1)`、`K_p=L F_p L`，K₀=LFL。
令`Z=A_g*A_g`，冻结real source时Z与F_p交换。有限秩角截断经循环迹得到的
合并候选为

    E_p(g) ?= 2Re paired-Tr_low[h(K_p) M_p],
    h(K)=K(I−K²)^(-1), M_p=L Z H F_p L.

问号是未付的无限维trace身份，不是记号省略。531/532支付完整实际source trace；
这本身不保证任意正负角成对截断的trace收敛，也不保证h(K_p)M_p为TC。
`paired-Tr`只有在额外证明source-cutoff联合极限后才能用于消费实际E_p。
以下只对明确属于TC的局部H3_p M_p乘积单独取ordinary trace，不预设它是actual高尾。

physical Z的核为`R_g(log(y/x))/√(xy)`。由于自相关支持跨度W，
LZH只连接有限rectangle

    x∈[e^(-W),1], y∈[1,e^W].

记H_band=1_[1,e^W]，则LZH=LZH_band，并且对所有g∈L²(U)

    ||LZH_band||HS²=∫_0^W t|R_g(t)|²dt
                   ≤W²/2 ||g||₂⁴.

没有low区间延伸到0的infrared费用。complex source可经实自伴型polarization处理；
原冻结矩条件与上述范数界均保持。

## 3. 实际lacunary cutoff的Schatten控制

置q=p^-1/2。完整actual Fourier有operator-norm身份

    F_p=(1−q²)Σ_(n≥0)q^n U_(-n logp)F−qU_logp F.

在low square中，第n项`L q^n U_(-n logp)F L`的核恰为
`2cos(2πp^nxy)`，HS范数≤2，而operator范数≤q^n。
它不是一串HS范数衰减的核；531的nonHS结论保持。

对r>2，Schatten插值给

    ||L q^n U_(-n logp)F L||S_r
      ≤2^(2/r) q^(n(1−2/r)).

因此δ_p=K_p−K₀满足，对足够late p有

    ||δ_p||op≤q/(1−q)+2q²=O(q),
    ||δ_p||S6=O(q^(2/3)),
    ||δ_p||S8=O(q^(3/4)).

这里low项`−q²K₀`和`−qLU_logpFL`都是O(q²)的HS核；后者kernel
`−2q²cos(2πxy/p)`，不能仅用U unitary的粗O(q)估计。

κ₀=||K₀||<1已付；选择finite p₀使δ的operator norm≤(1−κ₀)/2，
则||K_p||≤(1+κ₀)/2，所有`(I±K_p)^(-1)`共同有界。
这是fixed ambient Sonin cutoff1的统一late-p gap，不是成长cutoff或成长S的gap。

## 4. 完整三return余项的局部TC乘积预算

令`R_(σ,p)=(I−σK_p)^(-1)`、`R_(σ,0)=(I−σK₀)^(-1)`，σ=±1。
精确resolvent展开而非截断假设为

    R_(σ,p)=Σ_(j=0)^2 σ^j(R_(σ,0)δ_p)^jR_(σ,0)
              +σ³(R_(σ,0)δ_p)^3R_(σ,p).

因为`h(K)=½[(I−K)^(-1)−(I+K)^(-1)]`，完整高尾为

    H3_p=½[(R_(+,0)δ_p)^3R_(+,p)
                    +(R_(-,0)δ_p)^3R_(-,p)].

两个尾是加号：σ³的负号被h的差反转。全部actual逆保留在最后一因子。
由上一节op/S6界及Schatten Hölder，

    ||H3_p||op≤Cq³,
    ||H3_p||HS≤C||δ_p||S6³≤Cq².

再写`M_p=M₀+M_δ`。实位有限band核光滑且

    ||H_band F L||HS≤2√(e^W−1),
    ||M₀||1≤√2 W√(e^W−1)||g||².

所以M₀是source boundary HS×HS的**真正TC**。同时

    ||F_p−F||op≤2q/(1−q),
    ||M_δ||HS≤C_U q||g||².

由op×TC及HS×HS两个合法组织，

    ||H3_p M_p||1
       ≤||H3_p||op||M₀||1+||H3_p||HS||M_δ||HS
       ≤C_U q³||g||²=C_U p^-3/2||g||².

故局部候选的source quadratic ordinary trace满足

    |2ReTr(H3_p M_p)|≤C_U p^-3/2||g||²,

并且这个局部候选的源L²算子norm可对actual primes绝对求和。不需要source导数、carrier上界，
所以包括所有joint R≈p、p²和更高合法源。
原先以S8支付四δ尾也成立，但本组织借实位M₀的TC性将可控尾改进到三δ。
本节没有证明实际E_p的对应高尾等于这个ordinary trace。

## 5. 未付的实际trace域及低阶消费

实际E_p和局部scalar `2ReTr(H3_p M_p)`可各自定义，因此二者之差只是一个合法scalar。
没有第2节的trace身份，不能称这个差为实际0、1、2阶δ_p的paired aggregate，
也不能称被减的scalar为实际高尾。尤其H3_p一般不与K_p交换，不能把其resolvent
word直接当作K_p的一个成对谱角cutoff。

具体未付接口是ambient角映射

    Φ_p(T)=L T L F_p H + F_p L T L F_p H F_p.

有限秩T的source夹心经合法循环迹可与局部 `2ReTr(T M_p)`对应；
但对一般HS T，Φ_p(T)目前仅有HS控制，`A_g Φ_p(T) A_g*`未证TC。
有限秩T趋于H3_p的S2极限只给相应HS极限，不给trace-norm收敛；
完整 `A_g R_p A_g*` 为TC亦不补这个缺口。fixed smooth源即使给LZH的进一步平滑/TC，
仍不能自动推出ambient source夹心trace等于局部循环trace。

需要的新输入是共同source/角cutoff下的trace-norm收敛或等效commutator/核域证明，
特别要支付H3_p的非交换分离。未得该输入前，本节全部actual低阶分离保持conditional。

若该trace身份后来支付，仍须审三个低阶的signed kernel消去、stationary交接及source-L²绝对界。
M2的positive return、bare cosine项、low O(1/p)修正和fast lacunary mode不能逐块取绝对值
后仍声称此前p^-2取消保留。533的fixed-g endpoint theorem与它的compact norm渐近边界
都不支付这个低aggregate的uniform范数。

direct审查已另支付fulltrace大移位子项的source核O(p^-3/2)，乘q后O(p^-2)；
它是正确actualpartial，但尚未控制本节全部return/cross。
本审查没有发现可升级的actualjoint Rayleigh lower大于p^-2，也没有用crude误差或
hard-window corner假装反例。

## 唯一下一动作与宏观范围

finite-boundary域、S6插值和完整H3_p M_p局部TC预算已通过主/逆审核；
actual高尾身份及source-cutoff joint limit没有支付，也没有严谨短证明可补。
按C006第二且最后一轮止损，保存该消费缺口；这份辅助报告不新增轮数。
重新准入须先给实际source-cutoff共同迹类/收敛输入，再付完整joint signed低阶费用，
或给绕过角分离的actual整体源核统一界；不能以局部预算或泛norm改名替代。

低域完整Weil符号、base S={∞,2}/growingS运输和实际lowest仍未付。
本文件不是完整D_p预算或Goal完成证书。无本辅助下载/计算进程。
