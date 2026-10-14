# Full actual prime adjacency 的 cosh–Schur 费用：最强旧与 whole 惯性逆审

2026-10-14；root 临时发现候选后的独立新增审查。只编辑本稿，不改上一已消费 raw 稿、
STATE、Goal、cadence、Git；是否结算由 root 在全部前件闭合后决定。
重新恢复 AGENTS/README/STATE、check/show、同版 Goal/frontier/C021 stopped/最新 AA。
实际工作树有 root 的 553、source reviews 及 STATE/.gitattributes 改动；未作 clean 声明。
固定 0c4f3a3/全部≤538，同 G20261014，最新数学结算仍 549。

## 1. 审查判断

候选实际加权行费用成立：在原 H_L=L²((-L,L),du)，

    ||A_L||≤(1+o(1))e^L， L→∞，                         (1)

覆盖 ALL complex 源和 ALL 成长窗，全部 actual primepowers。
由 actual Γ 与删除 negative pole 的一维费用，得到

    log(1+n_−(Q_L))≤(1+o(1))e^L。                      (2)

本次定向检查没有发现旧仓中已经支付 (1)/(2) 的 whole 定理或同等实际上界。
旧 016 的 cosh 锚、旧 030 的固定边界层、旧 537 的 finite-window Schur 不能免费充当 (1)。
候选并非只把一个弱旧子界优化：它新支付 complete finite-window adjacency 的 uniform row，
并使 whole count certified budget 的 leading exponent 从 2e^L 降到 e^L。
工具 Schur、PNT 和 negative trace 都是旧工具；新的数学内容是这个全实际 row 费用及合成净值，
不主张经典工具新颖或外部首创，也不将此结果直接认作 Goal 完成。

## 2. 同对象 row 与 uniform arithmetic error：独立推导

设 I_L=(-L,L)，L>0，q 是全部 integers≥2，w_q=Λ(q)/sqrt(q)，a_q=log q；
partial T_a^I r(u)=r(u+a)1_(u+a∈I_L)。原 prime 算子为

    A_L=Σ_(q<e^(2L)) w_q(T_aq^I+T_−aq^I)。

这是 bounded symmetric **positive-kernel** 算子，未声称 A_L 为 PSD。
它在原 complex L² 中给 〈r,A_Lr〉=2Σw_q Re∫r(u+a_q)overline(r(u))du。
端点 q=e^(2L) overlap 零；strict 内部 cutoff 与 endpoint convention 不改变算子。

取 auxiliary Schur weight c(u)=cosh(u/2)>0。它不是新的 physical Hilbert norm，
无需以其 similarity 的 condition number 运输原 operatornorm。
直接展开 c(u±log q)，记

    x_−=e^(L−u)， x_+=e^(L+u)，
    ψ_<(x)=Σ_(q<x)Λ(q)， B_<(x)=Σ_(q<x)Λ(q)/q，

得到 ALL u∈I_L 的 exact row

    R_L(u)=(A_Lc)(u)/c(u)
      =[e^(u/2)ψ_<(x_−)+e^(−u/2)ψ_<(x_+)
         +e^(−u/2)B_<(x_−)+e^(u/2)B_<(x_+)]/[2cosh(u/2)]。  (3)

q 的 proper powers 在 ψ 与 B 中保持 Λ(p^j)=log p，绝不改成 j log p。
这是 q^(±1/2) 与 w_q 配对后产生 ψ、B 的真实算术行，不是 generic degree 行。

对每个先固定 ε>0，经典 unconditional PNT 可写成

    ψ(x)≤(1+ε)x+C_ε， ALL x≥1， C_ε≥0 finite。

它的 ALL x 形式由 sufficiently large x 的 PNT 与有限 initial segment 合并；
C_ε 与 ε 有关，不要求 ε=ε(L) 时未给的 uniform rate。
ψ_<≤ψ；Abel 给同一个 uniform majorant

    B_<(x)≤B(x)=ψ(x)/x+∫₁ˣ ψ(t)/t²dt
                ≤(1+ε)(1+log x)+C_ε。                  (4)

这个写法直接支付 B；无需另假设 RH、effective cancellation、未知 zero-free 参数或新的 Mertens 率。
在 (3) 的 ψ 项，leading x 部分恰为

    (1+ε)e^L[e^(−u/2)+e^(u/2)]/[2cosh(u/2)]
       =(1+ε)e^L，

ψ 的 C_ε 部分恰不超过 C_ε。B 部分由 (4) 不超过

    (1+ε)[1+L+u tanh(u/2)]+C_ε
       ≤(1+ε)(1+2L)+C_ε。

故可消费的显式 ALL L、ALL u 账本是

    R_L(u)≤M_ε(L):=(1+ε)e^L+(1+ε)(1+2L)+2C_ε。          (5)

对每条 symmetric edge 用 complex Young 的带权式

    2|r(u)||r(v)|≤|r(u)|²c(v)/c(u)+|r(v)|²c(u)/c(v)，

完整求和得 |〈r,A_Lr〉|≤∫R_L(u)|r(u)|²du≤M_ε(L)||r||²。
因此 ||A_L||≤M_ε(L)，ALL original L² complex r，无 finite/profile/common-source 限制。
先让 L→∞、再让先固定 ε↓0，得到 (1) 的 limsup 形式；不能把 C_ε 省掉或声称无根据的 rate。

## 3. actual Γ、全部 pole 与 whole count：独立合成

完整 Q_L=Γ_I−A_L+2|C|²−2|S|²，
Γ(t)=Re ψ_digamma(1/4+it/2)−logπ=actual 2θ′，
C(r)=∫r cosh(u/2)，S(r)=∫r sinh(u/2)。原域为 zeroextension Dlog，源可 complex。

ker S 的 complex codimension 至多 1。在该子域上 positive even pole 保留，故

    Q_L|_(ker S)≥(Γ_I−M_ε(L)I)|_(ker S)。

严格 negative subspace 与 ker S 的交至少只损失一维，因此

    n_−(Q_L)≤1+n_−(Γ_I−M_ε(L)I)。                      (6)

不以 odd pole operatornorm 再加 e^L scalar；它的一维费用准确为 +1。
prime adjacency 可能 indefinite 无妨，因为只用已核 A_L≤M_ε I。

对 scalar Γ，旧 028/543 的 negative-trace/Bessel 证明应用于 Γ−(M+1)；
每个 Γ−M 的 strictly negative eigenvalue 在 Γ−(M+1) 的 negative trace 中至少贡献 1。
actual Γ 的已付渐近给

    ∫[a−Γ(t)]_+dt=4πe^a+O(a+1)， a→∞。

原半窗长为 2L，所以 trace budget 至多 C L exp(M+1)。有限初值可放大 C。
它是 actual Γ，不使用 016 旧 half multiplier 的历史常数。
由 (5)/(6)，对每个先固定 ε>0，ALL sufficiently large L（亦可放大常数覆盖 L≥1），

    n_−(Q_L)≤1+C L exp[(1+ε)e^L+(1+ε)(1+2L)+2C_ε]。     (7)

取 log，先 L→∞ 再 ε↓0，得到 (2)。这是 ALL L 的 complete complex-domain upper budget，
不要求 head PSD、mixed Schur 或未知 G2，也不产生 actual negative eigenvalue 下界。
strict negative eigenvalue counting 与 finite matrix sign 是不同对象。

## 4. 最强旧查找与净值

检索覆盖 notes、reviews、scripts 的 Schur/cosh/ψ/PNT/prime-operatornorm/adjacency/
negative-count 相关表达；定向读原 016/017/022/023/027/028/030、542/543、537 的 source 逆审、
546 的 weighted divisor row、319 的另一谱矩阵 Schur 和 523/526 当前消费范围。
这不是宣称逐字重读全部历史，也不是外部 novelty 全文检索。

| 最强旧 | 真正已付 | 为什么不覆盖 (1)/(2) |
|---|---|---|
| 016 §§1–5 | pp graph 减 degree；D_L(u)=A(e^(L−u))+A(e^(L+u))；fixed-interior cosh 轮廓；pole 锚范数/图能量 | degree sup 在端点 S_L∼2e^L；没有 c-weighted adjacency exact ψ/B row 或 all-u upper |
| 017/022–028 | 正 graph multiplier、scalar defect、finite core/negative trace 与条件 Feshbach | 旧 scalar 多为 2P 或 degree upper，Γ-trace 是可复用接口；不预付本次 M_ε |
| 030 | 任意 fixed Cc¹ 左右边界剖面的 prime/pole common rank channel，full Q=o(e^L) | fixed profiles 的 weak/Rayleigh limit 不给 ALL L² operatornorm upper，不付 whole count |
| 537 | 固定 L=17/16、primepowers 至8的 polynomial auxiliary weight 和完整 Q 证书 | 固定窗的有限 row bound 无 cofinal arithmetic row 量词，不能继承为 (1) |
| 542/543 | actual allsource degree/Γ 预算，record窗 n_−≤1+C e^(S_L)，S_L∼2e^L；同 native thermal账本优化仍 leading S | 当时实际采用 degree 势；本次是更强原 adjacency 上界，不是重调同 thermal温度 |
| 546 | 薄 integer comb 的 fullprofile prime divisor-matrix row≤log N+O(1) | 非 complete physical L²；其补空间承载全部 fixed responsibility，不能充当 A_L 全源 norm |
| 548/C021 | 条件 polylog Γ-relative / whole quasi-poly count | 关键 independent premise 未付，不能把 conditional 预算当已有 unconditional 最强结果 |
| 319及其他 Schur | 经典加权检验，特定 actual ζ-window 背景列 | 对象/权/方向不同，无当前 physical pp adjacency 费用 |

“旧 016 already 有 cosh，旧仓 already 有 PNT 和 Schur”不意味着新 row 费用已证明。
否则任何以旧一般工具作出的新估计都被形式上否定；两层去重应扣已经付清的同对象后果，
不能把未曾求出的 uniform arithmetic row 当作一行免费标签继承。
本次新费用确实从旧明确算术输入独立推导，且无需猜测 complete sign 或未知 ζ 位置。

旧 030 还说明 coefficient 1 对未修复、完整 A_L 本身是 sharp：
取 fixed 左右 edge profiles 逼近 e^(−v/2)1_(v>0)，各 squared norm→1、各 Laplace moment→1，
030 的 prime quadratic /e^L→2，而 total norm→2。
先固定 profile 再 L→∞、再扩大其 fixed support，得 liminf ||A_L||/e^L≥1。
这只是 old lower 的直接消费，与 (1) upper 合并给 norm asymptotic；不重计 lower，也不排 full-Q
prime/pole cancellation、finitecodim/source-adapted 或 Γ-relative repair。

沿旧543同一 record窗 X=e^(2L)=n→∞，S_L=(2+o(1))e^L。令 U_new 为 (7) 的某统一
ε(L)→0 diagonalized certificate、U_old=C e^(S_L)。其 log 比较为

    log U_new=(1+o(1))e^L， log U_old=(2+o(1))e^L，
    U_new/U_old=exp[−(1+o(1))e^L]→0。                  (8)

不用 diagonalization 也可先冻结任何 ε<1，例如 ε=1/2，直接给严格指数净改善；
接着 ε任意才报 leading coefficient 1。这里比较两个 certified upper budgets，
绝不把 U_old 称作 actual n_− lower，也不把 (8) 当 actual count ratio。

## 5. 宏观准入和停止范围

本候选已有三句实质准入：actual auxiliary c 与 (3)/(5) 是新共同 row 费用；
测试门能由 ALL u/ALL L arithmetic error 与 complex Schur 自含闭合；
成功会严格降低整个 growth negative-count budget 的 leading exponent，而非只改一个弱子界。
这与 previous theta identity / unknown Poincaré 来源0结论并不冲突：root 在该 source gate
发现了另一个可核费用，应以新范围收据消费，不静默改写旧稿。

仍未付：n_−=0、Γ-relative sublinear/polylog fee、complete principal-compatible geometry、
最低支/Ξ同对象识别与 RH。coefficient 1 的 count 仍 exp(e^L) 量级；其强制力有限，
不能仅因出现新的 whole budget 就自动通过整个 Goal 第二/第三完整门。
PNT 属经典独立输入，不是新 prime-count 定理；新权不重启被暂停的无零区域/比例优化，
Schur auxiliary weight 也不复活等价 quotient unitarization 或 whole standard-cone Perron。

本稿已核候选语义和强旧净值；root 需另位对 row/Γ/count 作不同组织逆审，
保存最终原证明/root消费记录，才决定数学结算与主动作。无本人待跑进程。
