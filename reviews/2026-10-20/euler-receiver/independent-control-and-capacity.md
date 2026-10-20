# 实际 Euler 差分 receiver：独立费用与容量边界核查

2026-10-20；独占 producer／independent-control 稿。已恢复 AGENTS、README、STATE、
check/show、G20261014、C034、cycle14 和 571；不改公共 STATE、cadence 或 Git。
冻结基线仍是 0c4f／≤538；strong-old 仍是 542＋555→557 的 whole leading 4/5。
本稿不是 fresh 终审，也不把 producer 出稿记作 root 已消费。

## 1. 准入问题与原对象

cycle14 唯一待核门是：实际有限 Euler 多项式能否先对真实 receiver 作 coherent 合并，
再以原 L²(t>0) 范数支付有限高度尾费，而不是只得到 fixed-F Bohr diagonal。
下面 §§2–4 给出具体 polynomial diagonal 及完整有限高度证明核查。
它付一个明确 θ>2e 的成长范围，因而不只是换名的 unknown-tail 前件。
它仍不付 Sonin 运输、危险核心和完整 Weil 正性。

物理空间 H=L²(R,dy)，U_a f(y)=f(y−a)，

    B_F=∏_(p∈F)(I−p^−1/2 U_logp), D=B_F^−1,
    b_F(R)=∏_(p∈F)(1−p^−1/2 e^−iRlogp),
    P_T=1_(0,T), L_-=1_(-∞,0), H_+=1_(T,∞),
    w_(R,T)=e^iRy 1_(0,T)/sqrt(2π),
    v=L_-D*P_Tw, u=H_+DP_Tw.

这是 571 的同一个完整 D、同一真实受限像。先对任何有限 F 和任何 T>0 写身份；
实际成长消费再严格锁定 T_R=Γ(R)=Re ψ(1/4+iR/2)−logπ。
完整 Γ 不能用 log R 替代定义。w 是物理 carrier，不是 Weil 原源 r 或 Sonin 裸求值 k_R。

## 2. 实际 Euler 差分、原域和无 condition 分母的 diagonal

令 n 遍历 F-smooth 正整数，ω(n) 为不同 prime 数，rad(n) 只取 F 中因子。
直接把有限 bar b 乘到完整 v 上并按最终整数 n 合并，得到

    P_R(t):=sqrt(2π)e^iRt bar b_F(R)v(−t)
           =Σ_n a_(n,T)(t)e^iRlogn,        t>0,
    a_(n,T)(t)=n^−1/2 Σ_(d|rad(n)) μ(d)
                          1_(t<log(n/d)<t+T).                 (1)

每个 a_n 属于原 L²((0,∞),dt)。特别 n=1 时 a_1=0；
其余系数都支撑在 (0,log n)，且由原 band 长度也有

    ||a_n||₂ ≤sqrt(T)·2^ω(n)n^−1/2.                           (2)

先截 D 再乘 bar b 会改变最终 n 的 cutoff；本稿一直先按 (1) 合并，再截 log n。
有限 F 下原 inverse 绝对质量有限，有限差分是有限和，以上重排有原范数合法性。

记 A=supp(n)⊂F、x=log n。将 (1) 在全 t 线上看作 interval 的有限差分，平移不影响范数。
选 A 中最小 prime p；差分 Δ_logp 作用于长度 T 的 indicator 有

    ||Δ_logp 1_(−T,0)||₂²=2 min(T,log p),
    ||Δ_logq||_(L²→L²)≤2.

因此，限制回 t>0 只能减小范数，

    ||a_n||₂² ≤ [2·4^(|A|−1) log p]/n.                      (3)

对固定非空 A，原整数自由因子分解给

    Σ_(supp(n)=A) 1/n =∏_(p∈A)(p−1)^−1.

定义 D_F(T)=Σ_n ||a_(n,T)||₂²。按最小 prime 分组，得到 uniform T 的显式 bound

    D_F(T) ≤ 2 Σ_(p∈F) [log p/(p−1)]
                         ∏_(q∈F,q>p)(1+4/(q−1)).            (4)

这里没有 m^−2、M²/m² 或 Γ-gap 分母。F_L={p<y=e^(2L)} 时，
已付 Mertens 部分积估计给

    ∏_(p<q<y)(1+4/(q−1)) ≤ C (log y/log p)^4.

而 Σ_p log p/[(p−1)(log p)^4]<∞，故

    sup_(T>0) D_(F_L)(T)=O((log y)^4)=O(L^4).                (5)

这是实际 bar b 乘 receiver 后的完整 coherent coefficient diagonal 原 norm 费用。
它比粗 |b|≤M 后的 exponential condition 费用更好，但 diagonal 本身还不是有限高度平均。
单 prime 的完整精确抵消已在 571 支付，不能把 (4) 冒称一个新的 single-prime 结论。

## 3. 完整有限高度尾：独立复核 θ>2e 证明

本节复核另稿 weighted-tail-and-height-cost.md 的 after-Euler 完整尾。
令 F=F_L、R0=exp(θe^L)、H0=R0^β、0<β<1，T0=Γ(R0)。
只为估计，将 (1) 按最终 coherent n 分成 log n≤A 与 log n>A，A=c e^L。
令

    S_L(A)=Σ_(n F-smooth,logn>A) 2^ω(n)n^−1/2,
    Z_j(s)=∏_(p<e^(2L))(1+j/(p^s−1)).

(2) 的向量三角不等式逐 R 给完整尾的原 norm 费用

    ||Σ_(logn>A) a_(n,T0)e^iRlogn||₂² ≤ T0 S_L(A)².          (6)

它是 full inverse 尾，不是把实际对象改成 finite polynomial。
对 α>0、1/2−α>0，正项 Rankin 仅作估计：

    S_L(A) ≤e^−αA Z_2(1/2−α).                               (7)

固定 k>0，取 α=k/(2L)。PNT 部分求和在 s=1/2−O(1/L) 的紧邻域内 uniform，给

    log Z_2(1/2−α)=(2e^k+o(1))e^L/L.

可直接核其常数：Σ_(p<e2L)p^−s~e^(L+k)/(L+k)；
log(1+2/(p^s−1))=2p^−s+O(p^−2s)，后者总和 O_k(L)，是低阶项。
若 c>4e，取 k=log(c/4)>1，则

    log S_L(c e^L)
      ≤−[d(c)+o(1)]e^L/L,
    d(c)=c/2·[log(c/4)−1]>0.                               (8)

故 T0 S_L(A)²→0；T0~θe^L 的 prefactor 没有被省掉。

有限 head 对频率 log n 使用 ordinary integer gap δ_n≥1/(2n)。
MV 的有限 Hilbert-valued 形式给

    average_(R0,R0+H0) ||Σ_(logn≤A)a_(n,T0)e^iRlogn||₂²
       ≤ D_F(T0)+(C/H0)Σ_(logn≤A)n||a_(n,T0)||₂².           (9)

这里不对无限和直接套 Corollary 3。由 log n≤A、support t∈(0,log n)，

    Σ_(logn≤A)n||a_n||₂²
       ≤ A Σ_(logn≤A)4^ω(n)
       ≤ A e^(A/2) Z_4(1/2),
    log Z_4(1/2)=(4+o(1))e^L/L.                            (10)

因此只要 c<2βθ，head MV error 也趋零。存在

    4e<c<2βθ,  0<β<1

当且仅当该 certificate 的 θ>2e。取任何固定 θ>2e 后再固定 β,c，
由 (5)–(10) 与已保留的 1/sqrt(2π) 归一，得到

    average |b_F(R)|² ||v_(T0,R)||₂² =O_(θ,β,c)(L^4)+o(1).  (11)

用于 upper 时可用 ||head+tail||²≤2||head||²+2||tail||²；
若要 asymptotic diagonal，cross 由 Cauchy–Schwarz 付 O(L² sqrt(T0)S_L(A))→0。
没有对 tail 作随机相位假设，也没有应用 fixed-F Bohr 平均后交换 F→∞。

### 3.1 Γ 变窗的原 norm 费用

严格 T_R=Γ(R)；原 hard endpoint 费用是

    ||w_(T_R,R)−w_(T0,R)||₂²=|T_R−T0|/(2π),
    ||bar b_F(R)(v_(T_R,R)−v_(T0,R))||₂²
       ≤(M_F/m_F)² |T_R−T0|/(2π).                           (12)

Γ′(R)=R^−1+O(R^−3) 给 Δ_T≤C H0/R0。
log(M_F²/m_F²)=(4+o(1))e^L/L，而 log(H0/R0)=−(1−β)θe^L；
所以 (12) 在任意固定 θ>0、β<1 已趋零。对 (11) 的 weighted norm difference
仍用 Cauchy–Schwarz 或 triangle 支付；终值是真正 T_R，不是自由 T/R 平均。
由 ||w_(T_R,R)||²=T_R/(2π)~θe^L/(2π)，还可消费

    average [|b_F(R)|²||v_(T_R,R)||₂² / ||w_(T_R,R)||₂²]
       =O(L^4e^−L)→0.                                     (13)

这是原物理 dy 范数的成长结果，确实强于只控制 m²||v||² 的不同加权结论。
其范围 θ>2e 较窄且高于旧 θ>1；两者的量和量词不能互换。

## 4. 两边界相位与完整 returns 必须协同变换

571 已付 δ_win=||v||²+||u||²−<(v,u),J^−1(v,u)>，

    K=L_- B_F D* H_+, J=[[I,K],[K*,I]], ||K||<1,
    δ_win≤min(||v||²,||u||²).

若只乘共同 scalar bar b，完整 Gram 直接不变，故

    |b|²(δ_win)_+≤|b|²||v||².                              (14)

欲在两边界都用 clean Euler coefficients，应令

    V=bar b v, U=b u, η=bar b/b, A_phase=diag(I,ηI).

b(R) 从不为零，所以 η well-defined 且 |η|=1。
实际 u=e^iRT R_Tv 的 R_T 是 antiunitary 反射共轭；它给

    U=e^iRT R_TV,
    bar b(v,u)=A_phase(V,U).

因此正确的完整协同 Gram 是

    J_b=A_phase* J A_phase=[[I,ηK],[barηK*,I]],
    |b|²δ_win=||V||²+||U||²−<(V,U),J_b^−1(V,U)>.            (15)

不能独立净化两侧 phase 后仍字面保原 K；这会改掉 signed cross。
J_b 只是 unitary conjugate，故完整 inverse、全部 returns、gap 和 (14) 均保留。
(11)–(13) 因而给 weighted positive model residual 的同一上界，
却不给负部、absolute residual 或 uniform sign；负向仍有原 gap／returns 费用。

## 5. 成长核心、独立容量和 actual Sonin 的边界

本轮付的是一个同步成长、有限高度区间、实际 b 权、原 dy norm 的受限 receiver upper。
这是真实费用输入，外部 PNT/Mertens/MV 来源归旧，finiteEuler 合并与 tail 合成不冒称新的外部定理。
它不能被升级为以下任何结论：

1. θ≤2e 的必要费用 lower。4e<c<2βθ 失败只说明本证书的 tail/MV budget 不相容，
   不排 signed tail、不同分解、source-adapted 或更强 spacing 输入。
2. 危险 core 的改善。Γ(R)~θe^L、θ>2e 明显在 555 已有利的高频大小层；
   Γ约≤e^L 的 core、低频、ALL complex 源与 source coupling 尚未覆盖。
3. actual ε_F 的 signed/absolute 费用。δ_win 是 window model；
   Sonin k_R→w_R、完整 inverse word/clipping 的 cofinal 运输仍另付。
   571/560 中 N=O(e^L) 与 spectral tail 所需 M²/m² 的充分 certificate 缺口未由 (13) 解除。
4. Weil 原 du / zeroextension Dlog norm 的自动费用。物理 carrier 不是原源；
   必须给同源 map、完整 Γ/contact、所有 prime powers、双 pole 以及合法 source-domain transport。
5. 独立 RR／Weil 容量。正的 J 来自正 W 的普通 Schur Gram，减法后可两号；
   完整 mixed Weil Gram PSD 仍是 Weil 正性的等价要求，不能由 (15) 的 Gram 正性代替。

完整 actual 身份保持 560：

    2πρ_F(R)=Γ(R)−2Σ_(p∈F,k≥1)(log p)p^−k/2 cos(kRlog p)+ε_F(R),
    Q_W(r)=t_F(r)−<r,K_(F,I)r>
           +2|<r,cosh(u/2)>|²−2|<r,sinh(u/2)>|².

本稿没有删除 Γ、proper powers 或 poles，也没有无条件令它们在源上为零。
strong-old whole leading 4/5、危险核心、Ξ 及 Goal 完成门均未改善。

## 6. 一般 g-integer 的独立输入责任

有限因果 Euler filter、完整绝对逆及正确原域能给 (1) 的对应版本；
若 generalized values 有 exact collisions，必须先 coherent 合并，
不能沿用 ordinary unique factorization 给 (4) 的 free-label diagonal。
成长尾另用了具体 ordinary-prime PNT（Z₂、Z₄ 的常数 2、4）、integer log gap 与 Mertens。
这些不是 distribution/duality 的形式自动后果。
一般离散 g 系统须独立给替代计数、间距和 tail；连续分布须用真实 Fourier/Plancherel 设施，
不能把 discrete MV gap 原样继承。

fixed finite ordinary F 另可用 Matveev/BMS 的 polynomial(log n) gap 来支付无限 MV 域，
但这不是本稿 θ>2e proof 的依赖，且成长维数常数不能忽略。
不以该粗证书巨大推断实际原费用 lower，也不把两个合法 fixed-F 片段拼成 cofinal core 正性。

## 7. 独立核查的净消费

通过：实际 coherent 系数／原域；uniform-T polynomial diagonal；
after-Euler full tail 及 θ>2e 高度窗口；Γ endpoint 原费；两边界 phase 协同和 full J inverse。
局部原 receiver 成长费用从只付 m² 归一推进到明确范围的 actual |b|² 原 norm。
未通过：actual Sonin/source 运输、θ≤1 危险核心、ALL-source capacity、完整 Weil 正性。
因此可作为一次具体费用研究的输入，不可贴宏观突破或 RH 证明标签。

无后台 numeric/shell 生产过程；本文只保存证明与范围，最终由 root 对齐三稿并 fresh 终审。
