# 真实 receiver 的原范数、锁定 Γ 的成长平均与消费边界

2026-10-20；独占 producer 稿，不改公共 STATE/cadence/Git。
已恢复 AGENTS、README/STATE/check/show、同 G20261014/0c4f 冻结基线、
570 结算、560 §§2–6 及 cofinal-causal-tail-and-role-audit。
本文是待 root 消费的证明稿；旧 223/551 的 MV 工具和 560 的概率/PNT 输入归旧。

## 1. 对象与完整实际 receiver

原物理空间 H=L²(R,dy)，U_x f(y)=f(y−x)。先固定 finite F，

    c_x=n^(−1/2), x=log n, n 为 F-smooth（包括 n=1），
    D=Σ_x c_x U_x=B^(−1), m=∏_(p∈F)(1−p^(−1/2)),
    D0=Σ_x c_x=1/m, J0=Σ_x x c_x<∞。

所有逆级数在 operator norm 绝对收敛。T 必须取 actual Γ(R)，
但以下逐 fixed F/T/R 恒等式先对 ALL T>0、ALL real R 成立。

    w_R(y)=e^(iRy)1_[0,T](y)/sqrt(2π), ||w_R||²=T/(2π),
    v_(T,R)=L_-D*H_Tw_R,
    v_(T,R)(−t)=e^(−iRt)/sqrt(2π)
                  ·Σ_(t≤x≤t+T)c_x e^(iRx), t>0。                 (1)

这已是受限像本身，未以任意低半线向量替换输入。令

    ℓ_T(x,z)=[min(x,z)−max(0,x−T,z−T)]_+
            =min(min(x,z),(T−|x−z|)_+)。

Tonelli 的绝对上界由 Σ c_x c_z min(x,z)≤D0 J0 支付，所以

    ||v_(T,R)||²=(2π)^−1Σ_(x,z)c_x c_z e^(iR(x−z))ℓ_T(x,z)。      (2)

这是真实 signed/coherent 双和；各项有相位，不能将其改成正系数概率质量的 lower。
若 X,X′ 独立且 P(X=x)=m c_x，则 exact

    m²||v_(T,R)||²=(2π)^−1E[e^(iR(X−X′))ℓ_T(X,X′)]，
    ||v_(T,R)||²≤min(TD0²,D0J0)/(2π)。                         (3)

第二个 upper 无 T 因子，逐 fixed F 比粗 D-norm upper 更具体；但它由 560 已付
同一个一阶矩可直接推出，不能独立重计为 whole ζ 新费用。
carrier 共轭 C_R f=e^(iRy)f 只给

    C_R* D C_R=Σ_x c_x e^(−iRx)U_x。

因此消去外面的 e^(iRy) 后，R 进入全部 inverse 系数；没有把 phases 消成正算子的酉变换。

## 2. 单 prime 的精确原范数反测

令 F={p}、a=log p、q=p^(−1/2)、β=q e^(iRa)、T=Na+τ，0≤τ<a。
对 t=(j−1)a+s、j≥1、0<s<a，(1) 的内和有 N 或 N+1 项。直接求和得

    ||v_(T,R)||²=
      q²{(a−τ)|1−β^N|²+τ|1−β^(N+1)|²}
      /{2π(1−q²)|1−β|²}。                                   (4)

这在 N=0 时同样正确，第一项为零。锁定 T=Γ(R) 且 R→∞ 时，uniform in phase

    ||v_(Γ(R),R)||²=
       a q²/[2π(1−q²)|1−β|²]+O_p(q^N)，
    |b_p(R)|²||v_(Γ(R),R)||²
       =a q²/[2π(1−q²)]+O_p(q^N)。                            (5)

这里 |b_p(R)|=|1−β|；实际 |b|² 权精确消去单 prime 的相位分母。
该 cancellation 不能逐因子相乘推出 multi-prime receiver 的 lower/upper：
ℓ_T(log n,log m) 将全部 primes 的 delays 耦合，非乘积函数。
单 prime 结果不代模型 signed 差的符号；后者仍须完整逆和两边界协同。

## 3. 两边界协同与 full inverse 的准确费用

本节对照另一 producer 的 Schur/Gram 恒等式，仅列消费接口。
记 P=H_T、L=L_-、H=H_+、W=B*B、G=PWP，

    u=HDPw_R,
    K=LBD*H : HH→LH,
    J=[[I,K],[K*,I]]，x=(v,u)。

BD* 是 whole unitary，且 bounded invertibility 给 ||K||=κ<1。
反射共轭 (J_T f)(y)=overline(f(T−y)) 满足

    u=e^(iRT)J_Tv, ||u||=||v||。

对真正双边界 S_T=P(DD*−DLD*−D*HD)P，有 exact

    E_win=<w_R,(G^−1−S_T)w_R>=||x||²−<x,J^−1x>。              (6)

因 J 的 spectrum⊂[1−κ,1+κ]，

    −κ/(1−κ)||x||² ≤ E_win ≤ κ/(1+κ)||x||²
                                   =2κ/(1+κ)||v||²≤||v||²。 (7)

所以正向 E_win upper 不需要坏 gap 分母；负向控制一般仍有 (1−κ)^−1。
这是 sign-aware 的实际 receiver upper，但不声称 E_win≥0 或 ≤0。
若要用于实际密度还须乘 |b_F(R)|²，并加回 whole Z/两单边界主项尾和 k_R→w_R 的误差。
在 general finite F 上，(3) 与 |b|≤M=∏(1+q_p) 仅给

    |b_F(R)|²(E_win)_+≤M² D0J0/(2π)。                        (8)

固定 F 后这是有限 upper；cofinal F 下它仍有指数 condition 费用，并非独立 RR 容量。
式 (6)/(7) 的完整证明由 general Schur producer 支付；本文不把一个模型正迹
或 bare residual 的 sign 当 actual Weil sign。

## 4. fixed-F Bohr 平均不能免费升级成长

对先 fixed F/T，(2) 绝对收敛，R 的 Bohr 平均去掉 x≠z，故

    M_R ||v_(T,R)||²=(2π)^−1Σ_n n^−1 min(T,log n)。            (9)

再 T→∞ 得

    (2π)^−1 ∏_(p∈F)(1−1/p)^−1 ·Σ_(p∈F)log p/(p−1)。        (10)

对于 F_L={p<e^(2L)}，(10) 的表达式是 O(L²)（经典 Mertens/Abel）。
但取 fixed-F 平均长度→∞ 然后 L→∞，不支付 R≈exp(θe^L)、T=Γ(R) 的同步成长。
不允许由这里直接声称实际 receiver 的原 norm 仅 O(L) 或其 squared norm 为 O(L²)。

## 5. 一个真正锁定 Γ 的受限像成长平均测试

下述是 (9) 之外的新量词；它只控制明确写出的 m²-normalized norm。
对先 fixed θ>1，选 0<κ0<1、ε>0 使

    1+ε/2<κ0 θ<θ。

令 L→∞、F=F_L、m=m_L，

    R0=exp(θe^L), H0=R0^κ0, I_L=[R0,R0+H0],
    T_R=Γ(R), T0=Γ(R0), A=(2+ε)e^L。

则严格有

    (1/H0)∫_(I_L) m_L²||v_(T_R,R)||²/||w_(T_R,R)||² dR →0。  (11)

可取 upper

    O_(θ,ε,κ0)(L²e^(−L))
      +O(exp(−c e^L)), c>0；                               (12)

只需充分大 L，量词不依赖未付 RH。
其含义是：相对于全 D 最坏放大 m^−1，真实 receiver 在这些实际高度区间的平均占比趋零。
当 1<θ<2 时，它与旧 560 的 m||H_+DL_-||→1 完全共存；
旧达到 norm 的宽低向量并非真实 receiver。

### 证明：原 norm 每笔费用

先固定 T0，将 D 截为 D_A=Σ_(x≤A)c_xU_x（只用于估计，最终 tail 全部加回）。
由 (1)，乘去共同 unit phase e^(−iRt)，向量系数

    f_n(t)=n^(−1/2)1_(0,∞)(t)1_{t≤log n≤t+T0},
    ||f_n||²=n^−1 min(T0,log n)。

这是有限 Hilbert-valued Dirichlet polynomial，旧 223-C/MV Corollary 2 给

    (2π/H0)∫_(I_L)||v_A(T0,R)||²dR
      ≤ Σ_(n smooth)n^−1 log n
         +(C/H0)Σ_(log n≤A)min(T0,log n)
      ≤ C L²+C A Ψ(e^A,e^(2L))/H0。                        (13)

MV 常数绝对，起点 R0 不改变它。local real log-spacing 是
δ_n≥log(1+1/n)≥1/(2n)，所以其 error 正是 O(Σ n||f_n||²)；
不是把无限 smooth 级数直接放进一个不满足 weighted ℓ² 的定理。
Rankin 的有限和 positive upper 仅用 D0：

    Ψ(e^A,e^(2L))≤e^(A/2)Σ_(n smooth)n^−1/2=e^(A/2)/m。

乘 m²/T0，(13) 的第二项≤C m(A/T0)e^(A/2)/H0
≤C exp[−(κ0θ−1−ε/2)e^L]，第一项 O(m²L²/e^L)。

全部 inverse tail 的费用不用 MV。D−D_A 的 operator norm 为其正系数质量，

    ||v−v_A||≤sqrt(T0/(2π))m^−1 μ_L(X>A)。

560 的 paid EX=2e^L+o(e^L)、VarX≤C_V L e^L 给

    μ_L(X>A)≤C_ε L e^(−L)，
    (2πm²/T0)||v−v_A||²≤C_ε L²e^(−2L)。                    (14)

这保留全部 prime powers/returns 的 tail，没有宣称截断 carrier 本身是实际输入。
actual Γ 光滑渐近 Γ(R)=log(R/(2π))+O(R^−2)、Γ′(R)=R^−1+O(R^−3) 给
Δ_T=sup_(I_L)|T_R−T0|≤C H0/R0。原 w 的 hard endpoint 差确为

    ||w_(T_R,R)−w_(T0,R)||²=|T_R−T0|/(2π)，
    ||v_(T_R,R)−v_(T0,R)||²≤m^−2 Δ_T/(2π)。                (15)

故 m²/T0 归一后该费用为 O(H0/(R0T0))，趋零；T_R/T0→1。
用 ||a+b+c||²≤3Σ||·||² 合并 (13)–(15) 得 (11)/(12)。

真实新范围是同步成长、短相对高度区间、actual receiver 像的 normalized average。
旧 223/551 外部均值工具、560 的概率浓缩和原 Γ clipping 归旧，合成不称新外部定理。
无需自由配准 R log p；R 在指定区间平均，T 始终跟随 Γ(R)。

## 6. 为何该平均仍不给独立容量或原范数小费

式 (13)–(15) 还原原 norm 的已付 upper 是

    average ||v_(T_R,R)||²
      ≤C{L² + A e^(A/2)/(mH0)
             +T0 m^−2 μ_L(X>A)² +m^−2 Δ_T}。              (16)

其中 tail/cutoff 两项必须保留，不能由 (11) 删除 m^−2。
旧 PNT 给 log m^−2=(2+o(1))e^L/L，因此即使 μ≤CL e^−L，
T0m^−2μ² 的现有 upper 也不趋零，远不能改写为 O(L²)。
式 (16) 的大 upper 不是实际 receiver 的 lower；它只说明当前证书不支付更强结论。

相同问题影响 (7)：粗 |b|≤M 使

    average [|b(R)|²(E_win)_+/T_R]
       ≤C(M²/m²)·average [m²||v||²/||w||²]。

log(M²/m²)=(4+o(1))e^L/L；将 (12) 代入仍不给小费。
需要实际 |b(R)|² 与 receiver/coherent tail 的相关估计，不能以单 prime (5) 代。
负向 absolute 控制还须 κ/gap，完整 actual 比较另外有下一节费用。
因此 (11) 是真实受限像信息及旧 lower 误用的反测，非 whole Γ-relative 容量。

## 7. source、k_R、w_R 与完整 Weil 预算仍分开

w_R 是原物理 H 中的 carrier，||w_R||²=T/(2π)，不是原 Weil 源 r∈L²((-L,L),du)。
原 source Dlog norm 为

    ||r||²_Dlog=(2π)^−1∫log(2+|s|)|hat r(s)|²ds。

例如原 norm1、频率集中 R 的合法平滑源有该 norm squared 约 log R≈T，
而 carrier 的 T/2π 不能视作未经运输的 source 费用。
固定 F 时 560 已付 ||k_R−w_R||≤C R^−1/4、全部有限 words 及全 inverse 误差 (3)。
cofinal 时必须保留 m/M/ρ/Ω/d 的全部 prefactors：

    log(M²/m²)=(4+o(1))e^L/L, Ω→3,
    1−ρ≈2m²/M²。

在 log R~θe^L，word 误差要求 N=O(e^L)，而要使谱尾 ρ^N 小，
该证书需要 N 至少量级 M²/m²=exp((4+o(1))e^L/L)，二者不兼容。
这是原充分证书的成长缺口，不是 actual clipping error 下界。
无新 carrier/fullinverse 组织时，(11) 不可直接运输成 actual ε_(F_L) 的平均界。

完整 actual source 身份仍为 560：

    Q_W(r)=t_(F_L)(r)−<r,K_(F_L,I_L)r>
             +2|<r,cosh(u/2)>|²−2|<r,sinh(u/2)>|²，
    2πρ_F(R)=Γ(R)
        −2Σ_(p∈F,k≥1)log p p^(−k/2)cos(kRlog p)+ε_F(R)。

本文 Γ 是完整 actual Γ，未替为裸 log；全部 proper powers、双 pole 仍在定义。
除非具体原 source 另付 exact 双矩/相关零条件，不将任何一项设置为零。
receiver 高度平均不覆盖 ALL complex source、低频/core、source coupling 或整个 Fourier 权。

## 8. 一般 g-integer 的适用前件

(1)–(3) 只需有限正 delay、0<q_j<1 及完整 causal inverse 的绝对收敛；
相同 delay 的 coefficient 必须先 coherent 合并。Gram identity 另需 B bounded invertible。
但 (11) 非一般 duality 的自动后果，它额外使用：

1. ordinary integer n 的 log-spacing δ_n≥1/(2n)，以及相应 dimension-free MV error；
2. cofinal geometric probability EX~2e^L、VarX=O(Le^L)；
3. diagonal Σ c_n² log n=O(L²)、Rankin count Ψ≤e^(A/2)/m；
4. actual Γ derivative 及 T_R~θe^L 的原 norm endpoint 运输。

一般 g 分布可分别重新证明这些前件，不能从 functional duality/positive density 推出。
若 g-values 有 exact collisions，先合并后的 diagonal 不是自由乘法 label 的 Σ c²；
若相近 logg 没有 spacing 下界，MV error 可大。连续分布需要另一 Fourier/Plancherel 输入。

## 9. 净消费与来源

新增可消费：真实 receiver 的 exact coherent 原 norm (2)，以及 actual T=Γ(R)
同步成长时的 (11)，它在 1<θ<2 的范围内严格区分受限像与旧 full-H norm 饱和。
单 prime (4)/(5) 是最便宜 nonzero phase 对照；没有抽掉 full inverse 的 signed 比较。
仍欠：乘实际 |b|² 后的原 norm/coherent tail、full carrier inverse 运输、ALL source/成长 core。
strongest-old 542+555→557 whole leading 4/5 无改善，独立经典容量/Weil 正性未付。
全源同对象有利 domination 若只是另写假设，仍承担原 RH 等价责任。

MV 原件：Montgomery–Vaughan, *Hilbert's Inequality*, JLMS (2)8(1974),73–82，
[作者托管 PDF](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)，
印刷 pp74–75 Corollary 2/3。
本轮读已保存原 text §1–4 定位及完整 [551 来源审计](../../2026-10-14/c021-mv-source/primary-hilbert-formulas-and-domain-audit.md)，
原 PDF/公式视觉核由该已有审计支付；当前 publisher 网页只返回 metadata/abstract，
不冒称此次重读全文图像或重证 MV 全部 lemma。
Hilbert-valued finite扩张用旧 223-C，证明只是逐有限系数 span 正交坐标相加。
无后台数值、下载或执行 pending；原件出稿不等于 root 消费。
