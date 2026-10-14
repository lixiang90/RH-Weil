# GY native prime-AP 源审：全移位、直接 a_U 与对数临界总误差

2026-10-14，独立来源审查，零数学轮；不登记 C021，不编辑 STATE/cadence/Git。
恢复 AGENTS/README/STATE、check/show、G20261014、frontier、C020 已停合同、
D20261014V、549 原闭合记录和 physical-row-next-source-screen 后执行。
固定基线仍为 0c4f3a3/全部≤538。现场 HEAD=5e65cc4637fc2d89edd83a85a4e492a5a6cd3608；
恢复时仅 STATE 有 root 运行中的改动；子代理 get_goal=null，不代替 root 的 active 实例。

**结论：** k=2 直接 AP 机制确实能保 native W_U(j)，不需要小移位条件；
a_U 可直接展开，全部实际 prime powers 和非互素 residue 可以支付。
冻结 U=floor(T/log²(e+T)) 的全 j 总误差，已核经典 BV 输入尚不足以给 o(1)。
先固定较大的对数指数、例如 U_10=floor(T/log¹⁰(e+T))，同一机制则合法给这一个
prime/Type-I 混合槽的 o(1) 误差。它不补 actual ΛΛ 槽，也不自动改善完整核心。
不得把第一项来源缺口扩大为“所有允许变 cutoff 的 direct AP 方法失败”。

## 1. 原件、确切输入与声明/推导的区分

一级原件为 Goldston–Yıldırım 的
[math/0111212v1](https://arxiv.org/abs/math/0111212v1)，核读
[固定版本 HTML](https://arxiv.org/html/math/0111212v1) 的 §1 (1.27)–(1.32)、
§4 (4.1)–(4.17)、§5 (5.7)。这里未冻结新 PDF/hash，HTML 自动生成日期不是论文修订日期。
其 (1.30) 只按固定幂距 q≤x^(θ−ε) 陈述 BV；无条件 θ=1/2。
(4.3) 的 k=2 主项正是下节 W_U(j)。原 Theorem 1.3/1.4、pure 对比及
singular-series 近似有各自移位/截断条件，不能免费用于本题。
(4.6) 仍用固定幂距，证明末尾还按小移位吸收 n=1 特例；本稿改用原 AP 展开，
保留 native 有限和并重新支付全部误差，而非声称已扩大原定理。

对数临界误差使用作者一级原件 R. C. Vaughan，
[The Bombieri–Vinogradov theorem](https://personal.science.psu.edu/rcv4/Bombieri.pdf)，
§1 第3页未编号公式及第4–6页证明。它给完整 Λ、最大 residue 和最大前缀的输入：

    Δ(X,Q) := Σ_(d≤Q) max_(a,d)=1 sup_(0≤v≤X)
                         |ψ(v;d,a)−v/φ(d)|
    Δ(X,Q) ≪_A X(log X)^(-A)+sqrt(X) Q(log(XQ))^6,  Q≤sqrt(X).       (BV)

每个 A>0 先固定；常数及足够大阈值可依 A，经典 Siegel–Walfisz 依赖保留，
不是有效数值证书，也未假设 RH/GRH。只调用已知定理，不重启暂停的无零区域优化。
本审不追最小对数指数。(BV) 是精确消费输入；下节是独立有限和推导。

## 2. 全 prefix 的 native 算术主项；a_U 直接展开

Y→∞，sqrt(Y)≤T≤2sqrt(Y)，h=1/T，|τ|≤T，U≥1。
当前冻结 U=U_2=floor(T/log²(e+T))；足够大 Y 时 U≥1。
所有 j 是整数，|j|≤C Y/T，C 先固定，故 (Y,2Y] 中 n+j>0。
定义原有限除数和

    Λ_U(m)=Σ_(d|m,d≤U) μ(d)log(U/d),
    a_U(m)=Σ_(d|m,d≤U) μ(d),
    I_U(m)=Λ_U(m)+log(m/U)a_U(m).                                (1)

对每个 s,z∈[Y,2Y]、s≤z，有逐项恒等式

    Σ_(s<n≤z) Λ(n)Λ_U(n+j)
      =Σ_(d≤U) μ(d)log(U/d)[ψ(z;d,−j)−ψ(s;d,−j)],               (2)
    Σ_(s<n≤z) Λ(n)a_U(n+j)
      =Σ_(d≤U) μ(d)[ψ(z;d,−j)−ψ(s;d,−j)].                       (3)

因此定义 native 有限算术系数

    W_U(j)=Σ_(d≤U,(d,j)=1) μ(d)log(U/d)/φ(d),
    A_U(j)=Σ_(d≤U,(d,j)=1) μ(d)/φ(d).                            (4)

互素部分分别给 (z−s)W_U(j)、(z−s)A_U(j)，误差至多
2 log U·Δ(2Y,U) 与 2Δ(2Y,U)。这里 AP 的 residue 最大值允许 −j 任意；
没有 j≤sqrt(U) 或 j≤U^ε 需求，也没有把 W_U 改成 singular series。
这是保 native 主项后的真实合法逃逸。

(3) 是直接以 μ(d) 为系数展开，完全未对 big-O 相关公式求 U 导数。
因所有求和都有限、cutoff 相同，(1) 亦逐整数成立。
n=1 的 Λ_N(1) 特例在本 block 根本不出现。

## 3. 非互素 residue 与全部实际 prime powers

若 (d,j)>1 且 n≡−j mod d，Λ(n)≠0 则 n=p^k，k≥1，且 p|(d,j)。
这是实际 Λ 的 support，不是把 proper powers 删除后套素数定理。
对每个这样的 d，不论正负 j 或 j=0，

    0≤ψ(2Y;d,−j)≤Σ_(p|d) Σ_(p^k≤2Y)log p
                   ≤ω(d)log(2Y)≤log d·log(2Y)/log 2.             (5)

μ(d)≠0 的 squarefree 限制只会减少费用。由
Σ_(d≤U)log(U/d)≤U、log d≤log U，得到坏 residue 的统一界

    B_Λ ≤U log U·log(2Y)/log 2,
    B_a ≤U log U·log(2Y)/log 2.                                 (6)

所以对全部 j、全部 prefix，(2)/(3) 的实际误差分别满足

    E_Λ ≤2 log U·Δ(2Y,U)+O(U log²Y),
    E_a ≤2Δ(2Y,U)+O(U log²Y).                                  (7)

这也解释不能直接把 GY (4.17) 的 all-residue E 最大值无声视为 (1.30) 的
coprime 最大值；此处 (5)/(6) 明付其差额。
j=0 时 W_U(0)=log U、A_U(0)=1，公式仍有直接证明，但不以此重付旧167 diagonal；
原 §4 非零移位假设没有被伪称为原文覆盖零移位。

## 4. 原 du triangular 核：全部 shift 的 Abel 总费用

使用 source-screen 的原 Hilbert norm L²(R,du)、同一个 incidence feature，
内积对第一变量线性。全部 joint pair 的权恰为

    w_j(n)=[n(n+j)]^(-1/2) exp[−(2n+j)/Y]
           exp[−iτ log(n/(n+j))]
           [h−|log(n/(n+j))|]_+,
    Y<n,n+j≤2Y.                                                 (8)

其支撑给 |j|≤2Yh；允许固定 C 只是统一上界。
在 clipped interval a_j=max(Y,Y−j)、b_j=min(2Y,2Y−j) 上，
|w_j|+TV(w_j)≤C h/Y，包括两个端点和 positive-part kink。
具体 phase 导数费用为

    |τ| |d/dn log(n/(n+j))|=|τj|/[n(n+j)]≤C/Y.

故总 phase 变化 O(1)，不是删掉 phase 或扩大到 all height。
令 ℓ_j(n)=log((n+j)/U)，则 sup|ℓ_j|≤C logY，TV(ℓ_j)≤C，
从而 |ℓ_jw_j|+TV(ℓ_jw_j)≤C logY·h/Y。
clipped interval 的任意 prefix 是 (2)/(3) 的两个 prefix 之差；不用 pointwise AP 代 uniform prefix。

将 (7) 用于 Stieltjes/Abel 求和，原 mixed 槽保主项为

    Σ_(Y<n,n+j≤2Y) Λ(n)I_U(n+j)w_j(n)
       =W_U(j)∫_(a_j)^(b_j) w_j(v)dv
        +A_U(j)∫_(a_j)^(b_j) ℓ_j(v)w_j(v)dv+error_j.              (9)

所有正、负 j 共同保留。反向槽可换 m=n+j、j→−j，并取相应共轭权；
仍在同一 clipped block，无额外 shift 限制。
全 shift 的个数 O(Y/T)，因此误差总额为

    Σ_j |error_j|
       ≤C[T^(-2)] [logY·Δ(2Y,U)+U log³Y].                       (10)

这是原 du 配对中的总费用，不是另换 weighted norm；只覆盖这里实际 Λ/Type-I
的系数方向及有限 τ 家族，不是全部 Weil L² 源的正性命题。
prime powers 已在 (2)/(3)/(5) 全保；没有凭其“少”无估计删去。

## 5. 冻结 log² cutoff 的缺口与固定 log¹⁰ 的合法逃逸

写 L=logY。对冻结 U_2，(BV) 仅保证

    Δ(2Y,U_2)≪_A Y L^(-A)+Y L^4,
    RHS(10)≪_A L^(1−A)+L^5+L/sqrt(Y).                          (11)

所以这个来源输入不支付所需总 o(1)；一个足够的未付条件是
Δ(2Y,U_2)=o(Y/logY)。这不是断言真实误差增长，也不是证明 BV 或其他 signed
方法不能更强；O(L^5) 是已核输入给出的上界。
特别不能把 GY 固定 ε 换成 ε(Y) 来假造原 (1.30) 的 uniform 常数。

允许先固定 B 后改变截断为 U_B=floor(T/log^B(e+T))，直接 (2)–(10) 全部继续成立。
(BV) 给

    RHS(10)≪_(A,B) L^(1−A)+L^(7−B)+Y^(-1/2)L^(3−B).            (12)

例如先固定 A=4、B=10，则全部 j/prefix 的实际混合误差为

    O(L^(-3))+O(Y^(-1/2)L^(-7))=o(1).                          (13)

没有 B(Y)，不追最佳 B，不假设未知 ζ/Dirichlet 零点位置。
这一不同 cutoff 的 AP 误差付款是合法的来源范围，不能因 paper 声明 miss 而删除。
但它仍保 (9) 的两个 native 主项；不宣称这些主项已相消或得到 ΛΛ 渐近。
旧164的 cutoff 守恒要求同时换 I/II：Λ=I_(U_B)+II_(U_B)。
不能把 U_B 的公式只插进冻结 U_2 的一个槽而丢失 shell/companion。
允许完整 exact 重组是一条未排逃逸；改变 cutoff 本身没有删除 prime current 或 core。

## 6. 消费范围与数学准入判定

| 项目 | 本审已付 | conditional/open 或旧责任 |
|---|---|---|
| 原 GY 到 k=2 native AP | (2)/(4)、全 j、全 block prefix，直接 a_U，正确 residue 量词 | 原 Thm1.3/1.4 不被宣称扩展；不免费 singular-series 替换 |
| 实际 arithmetic/原 du 费用 | 完整 Λ(p^k)、非互素差额、triangular BV/phase、正负 j 和端点 | 固定 U_2 的总误差 o(1) 没有由所核输入支付 |
| 允许变 cutoff | 每先固定充分大 B，具体 A4/B10 的该混合槽 o(1) 误差 | 仍须保 native 主项、I/II 守恒和完整 coupling；不回填 U_2 |
| 实际完整 row/Weil | 没有把来源声明或有限矩阵作为全源定理 | actual ΛΛ、continuum/cross/full Γ-pole-prime/core/Ξ 未由本审支付 |
| 相对强旧的净后果 | 显式原 AP 微观范围与误差分账，可供 root 跨表示核对 | root 正在核旧 Euler-grid/μ-PNT 的更强 aggregate；本审不凭微观新表示计新 whole 结果 |

来源筛选本身零轮。大 B 分支是可核、独立的经典 AP 输入应用，不是未知 bound
改名；但目前没有相对最强旧资产、削弱实际完整 core 的三句净后果准入。
因此本审不请求新 C021、不计轮，不把 U_2 的一个 proof gap 升级成实质方法类边界。
下一动作由 root 合并完整核和强旧 aggregate 原审后唯一登记；本子任务没有待跑进程。

本稿只定位来源与付款范围。原恒等式、BV 本身和旧 diagonal 不计新增；
特殊混合槽成功不代完整成长 signed/core 后果，也不完成宏观 Goal。
