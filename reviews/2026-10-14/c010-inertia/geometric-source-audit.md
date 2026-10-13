# C010：独立raw源重组、尺度负对照及实际geometric上界

2026-10-14；起始HEAD `35609baea2fb3a4456b5ab9250648b198a9a4130`。
先恢复AGENTS/README/STATE/check/show、当前Goal、C010、D20261014I及537。
只写本辅助audit与私有named脚本/数据，不改STATE/cadence/git，不运行原外部code或联系作者。
参数先存[source-preregistration.json](source-preregistration.json)，六个16/32/64每sector
80digits压缩只ordinary探索；没有扩N、提升digits或用ζ零点。

## 1. bytes、原norm及正确压缩

原新source数据来自`tmp/c009-liu/fresh-b-20261014/certificates/`，本辅助实际重核：

- source-matrices.json SHA256 `4bce98228442805bc5ae16e9c26c8df88e85c35ab7ec8deffdd808adbf1217ac`；
- tail-columns.json SHA256 `2a88894c7405e01a37cbdef8671e9d628ddc60ae9cdb335fa2636fe49b6666a2`。

与537 fresh收据一致。只读取A/J₀ raw dyadic intervals及两raw tail列，不导入原候选或PASS。
L=17/16，p_n(u)=P_n(u/L)，Γ_nn=2L/(2n+1)。matrix midpoint=(lo+hi)/2^257，
tail midpoint=(lo+hi)/2^641。正确orthonormal R压缩为

    Γ^-1/2 [A_raw+J0_raw+(648/17)(r0 r0^T+r1 r1^T)] Γ^-1/2.

J₀ raw已经包含L² change-of-variables；不能再乘L²。
U的648/17来自81/Γ₀₀=27/Γ₁₁，不是把两column当等norm source。
归一化后当前source operator误差为

    εA+εH+σ=2^-204+2·2^-220+9·2^-512≈3.88950324e−62.

real/complex Hermitian pole已在J₀包含，odd负pole不删；A保留完整prime powers2,3,4,5,7,8。
Legendrebasis本身没有中心exponentialbasis的(-1)^n换相问题；odd/even分别取1,3,...与0,2,...。
这里不把basis normalization变成form缩放。

## 2. 80digits诊断及源尺度负对照

[sonin_source_reconstruct.py](sonin_source_reconstruct.py)是本辅助自行写的重组脚本，
结果为[sonin-source-reconstruction.json](sonin-source-reconstruction.json)。正确R的最低值普通探索为：

| 每sector维数 | even最低值 | odd最低值 |
|---|---:|---:|
| 16 | 6.15163809699e−22 | 2.10908173533e−19 |
| 32 | 3.40642117357e−30 | 1.09548401563e−28 |
| 64 | 5.05309697584e−35 | 1.84024104271e−31 |

残差约1e−80，仅ordinary mp residual，不是interval eigenvalue认证或全源inertia。
未触发actual严格负方向；不能仅因有限最低值positive宣布全R或Q的排序。
A+J₀（无U）的finite最低值亦positive但略小，这不授权删除全域tail supplier。

多乘一个L²到J₀的错误对象在六个截面都出现O(1)负底，约even−0.531/odd−0.633。
更便宜的exact rational source-scale控制由
[sonin_source_scale_control.py](sonin_source_scale_control.py)及
[sonin-source-scale-control.json](sonin-source-scale-control.json)给出：
同一constant规范化Legendre source，paid source errors后正确R Rayleigh>1/32，
错误A+L²J₀+U的Rayleigh<−1/8。
这是精确显示额外L²会改变实际对象；该负值绝不消费成原R、Q或C009的反例。

## 3. 固定even64源的actual Q上界：不能用R Rayleigh替代

主代理进一步授权只取既定even64试探、raw系数规范到50 significant decimal digits，
不改变N或80digits。该源先冻结为
[sonin-even64-rational-source.json](sonin-even64-rational-source.json)：

    f(u)=1_(-L,L)(u) Σ_(n=0,2,...,126)c_n P_n(u/L),
    c_n为明确exact rational，N_f=Σ c_n²Γ_nn.

zero-extension可能端点不光滑，但piecewise polynomial Fourier为O(1/t)，
所以f∈closed logarithmic form域D_log,L。Cc∞ core沿537已付，
故这个Rayleigh值合法给真正even全源infimum的upper，亦可由合法smooth逼近。
试探系数生成是否精确逼近R底不影响upper有效性：冻结后是一个确切有理source。

actual equality为

    Q(f)=<f,(M+K)f>+π^-1∫_256^∞ [A(t)−7/2]|F_f(t)|²dt.

不是R=M+K+U的eigenvalue，也不是只删除正tail。
head用A_raw+J₀_raw midpoint作exact Fraction quadratic，并支付
εA+εH=2^-204+2·2^-220；U不属于这个head，不能重复加。

### 完整Γ高尾的无ζ有理上界

even polynomial的endpoint derivatives是exact rational：

    d_k=f^(k)(L)=L^-k Σ_(n≥k)c_n (n+k)!/[2^k k!(n−k)!].

反复integration by parts到degree126结束，没有剩余integral；Fourier精确为

    F_f(t)=2[sin(Lt) S(t)+cos(Lt) C(t)],
    S(t)=Σ_(j=0)^63 (−1)^j d_(2j)t^(-2j−1),
    C(t)=Σ_(j=0)^62 (−1)^j d_(2j+1)t^(-2j−2).

因此|F|²≤8(S²+C²)。保持两个signed series内的所有cross项，
不用Σ|d_k|作绝对化，否则会浪费许多数量级。
令S²+C²=Σ b_m t^-m，对q=0,1,2及Ω=256有exact rational积分

    I_q=Σ b_m Ω^(1−m−q)/(m+q−1)=∫_Ω^∞t^-q(S²+C²)dt≥0,
    J=Σ b_m Ω^(1−m)/(m−1)²=∫_Ω^∞log(t/Ω)(S²+C²)dt≥0.

Γ上包络由同一Binet规范独立推导：z=5/4+it/2，
|2·Binet integral|≤1/(15t)，两个real reciprocal项为非负，
Re logz≤log(t/2)+25/(8t²)，所以

    A(t)−7/2≤log(t/(2π))−7/2+1/(15t)+25/(8t²).

该上界在t≥256为positive。保留全部Γ尾，得到

    T_tail(f)≤(8/π){[log(Ω/(2π))−7/2]I₀+J+I₁/15+(25/8)I₂}.

π用Machin160-term alternating fractions上下包围，log用160-term atanh series加完整geometric
remainder，再round outward到256-bit dyadics。I_q/J与head全部Fraction精确计算，
因此ordinary80 eigenproposal不会使最终upper失去严格误差预算。
该解析流程不是ζzero数据、拟合或盲增有限N。

[sonin_source_geometric_upper.py](sonin_source_geometric_upper.py)及
[sonin-even64-geometric-upper.json](sonin-even64-geometric-upper.json)给：

| 项目（除以exact N_f） | 值 |
|---|---:|
| A+J₀ midpoint Rayleigh | 5.0515879616663e−35 |
| 完整Γ tail upper | 1.8177582965117e−35 |
| paid head norm error | 约3.8895e−62 |
| outward actual Q upper | 6.8693462581781e−35 |

final upper保存为exact dyadic numerator/denominator，并严格比较通过

    Q(f)/||f||² < 7·10^-35.                            (1)

这是本辅助新的实际geometric upper候选；应由主/不同组织逆审公式、因子2/π、constants
及向量exact norm后消费。每次源改动才需重新评估，不在结果通过后机械扩大计算。

## 4. 对whole-ground合同的消费范围

(1)只给真正even λ₁的upper。537的coercivity仍给全部complex窗bottom≥τ，
两者本身不付simple/even，因为odd底或第二even底可能位于区间内。
64阶ordinary odd约1.84e−31与第二even约3.17e−28不是whole lower bounds。
必须由M−sI的完整source-error/complement/Schur或合法frame inertia给真实lower门，
不能用这两个finite值与(1)直接比较宣称simple。

原C001 μ13窗更大，535无费桥不复活，C008不等待；没有RH/成长域/prolate最低态声明。
实际瓶颈局部变化：actual Q的无ζ几何upper已构造，whole odd/second-even lower仍未付。
唯一下一动作：主/逆审先确认(1)的exact bound，再决定现有448-source全域inertia费用是否
能提供严格大于该upper的两个lower；若只剩finite排序或条件归约，依C010止损。
辅助脚本均已exit0，无pending process；不改STATE/cadence/git，不另计研究轮。
