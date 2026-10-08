# 原 unit 主频带 major arcs：不同作者全文独审

2026-10-08，checkpoint_audit。研究作者 whole_mixed4，审查作者不同。
本次只新增本审查文件；不修改研究源、冻结依赖、检查器、输出或 Git。

## 1. 绑定、全文读取与判定范围

全文读取下列固定文件，并独立重推本次新增估计，未以已有 PASS 代替推导。

| 文件 | 行数 | canonical UTF-8 LF bytes | SHA256 |
|---|---:|---:|---|
| [本次研究源](hybrid-original-unit-band-joint-cancellation-research-whole.md) | 378 | 14896 | 7c95bd2e700c16e0b0e836063f7545e8222a4de4b03d60c3271965252ec744b4 |
| [原 unit 频带源](hybrid-whole-fourth-unit-unit-actual-research-whole.md) | 425 | 16428 | b3f14cf4ee5659f8e23bd51dc9bf71e853e783bd2d55e42ee8846d6e8d1e41dc |
| [原 unit 源 root 独审](hybrid-whole-fourth-unit-unit-actual-review-root.md) | 68 | 3984 | 586974acc279ca4a55d9a26d1269e7e78d56f5f50f95f36c934de786d4bca3c9 |

同时只读核对新增工具的作者原文：
[Kedlaya，Chapter 18，Theorem 18.2](https://kskedlaya.org/ant/chapter-18.html)，
其式 (18.2.1) 为固定整数系数的 primitive multiplicative large sieve，
权重 q/φ(q)，费用 Q²+N−1。核读其 Gauss 展开及
|τ(χ)|=√q 的证明。引用该标准定理，不增设素数 AP 分布或 GRH 前件。

判定：研究源 (17) 的完整 major 频率族
Oφ(D³X^(1/2)L^C)，以及 (18) 的实际主项缩约，通过本次独立审查。
这里 1≤D≤X^(1/10)，取 D=X^δ、0<δ<1/14 时
1/2+3δ<5/7。未发现需要阻断这些限定结论的实质缺口。

此判定依赖已冻结 unit 源的原 χ-carrier signed 频带准入。
本次没有重新认证全部更早的 whole-P、重复词或 good-set 桥，
没有取得完整 minor 上界、canonical scalar whole 四矩或新的比例/条带。

## 2. 完整 nn 加回与真实产品窗

源 (1) 保留原 b_p、所有 genuine primes、共同 u、两个分子最大位置，
以及另外两种共轭位置；q 为真实最大素数，s<q，p,r<q 且排除 s。
原 ν、d floor、θ_± 和正高度均未改变。

先加回全部 n=qm，所得 L_F 是完整频带。interior qs>4X，
且 θ_+/(2π)<3X 对大 X 成立，所以 1≤m<q。
模 q 的 m 非零加性矩阵有范数 √q，两腿 L2 均 Oφ(1)。
每个 q,s 的 m 个数 O(X/s)，而
(2πs/q)||ν||∞≪s/(qX)，故该完整 nn 主项每对 q,s 为 Oφ(q^(-1/2))。
外 b_qb_s 全族求和 Oφ(X^(1/2)L^C)，确认 (3)。
这个 argument 本身消费完整 n=qm 块，不由 signed 总量推任意子集范数。

g(pr/(qs)) 必须在完整 n 主项中插入，不能逐 n 或只在 major 中插入。
完成 n 逆变换得到 K0((qs−pr)/(qs)) 及原 mod-q² aliases。
若 g≠1，真实产品离 qs 至少 qs/4；K0 的 χ Fourier 因子为
Γ(s_T v)，其 stretched 尾在此有任意固定省幂。

额外 pr+ℓq² aliases 由 p,r<q 和原 interior q−s>4qδ
保持离 qs 至少 δqs。冻结 whole-line lattice 尾证明适用于 j=m=0 的
K0；ν 主项没有需额外支付的 Taylor 导数。
原四权总质量至多 X²L^C，因此源 (5) 的全族 tiny 误差成立。

此后 dyadic p,r,q,s 从 √X 起，末箱严格按 X 截断。
g 非零推出 PR≍QS，因而真实整数产品系数长度 N≪PR≪Q²。
这个真实长度是大筛的依据；没有以模 q 产品剩余类替代它。

## 3. 完整低产品族与 packet 几何

QS≤64DX 的 boxes 在全部 n 逆变换以后一起支付。
实际 qs≤256DX；near 每对 q,s 有 O(qsδ+1) 个整数产品，
每个整数产品的 factor pairs 至多 τ(a)。
near 中四权为 Oφ(1/(qs))，profile 与共同 u 积分有固定上界。

放大 q,s 到整数：
计数 ≪DX log(2D)，倒数质量 ≪log²(2D)。
乘 δ≪X^(-1)L^C 与任意 subpower divisor 界后，
全低产品族为 Oφ,ε(DX^εL^C)。
near 外和 carry aliases 消费完整 χ 尾，不依赖 n 子集的绝对和。
确认 (6)，没有未知短区间素数输入。

在高产品 QS>64DX boxes，(7) 保留全部 d≤D、全部 reduced a、
包括 d=1,a=0 的表示。重叠用固定次序分配；上界可正计数全部表示。
q>D 为素数，所以 gcd(d,q)=1。

正 support θ_-/(2π)>X、s≤X 保证 n/q>1；
误差 D/(dS)=o(1)，故 c=dm+a≥1。
上 support 给 n/q≤3X/S，继而
c≤4dX/S≤4DX/S<q/16。
因此 b=c d^(-1) mod q 是非零频率。

固定 d,a 时 m 走 O(X/S) 的公共整数范围，
长度小于 q；m↦m+a d^(-1) mod q 注入非零频率。
固定 q,d,a,m 的实际整数 n 个数
K_d≪QD/(dS)+1。
这个 +1 必须保留；后续费用中确实保留了它。
全部 ν support、s<q 和 n<q² 仍为实际 mask，仅在正上界时外包围。

## 4. CRT、统一 Mellin 包络与公共 profile

写 β=n−cq/d，严格分解为
e_(q²)(−npr)=e_(dq)(−cpr)e(−βpr/q²)。
CRT 给
e_(dq)(−cpr)=e_q(−c d^(-1)pr)e_d(−c q^(-1)pr)。
按 p≡i、r≡j mod d 分两腿后，最后因子是模长 1 的常数。
c mod d=a，即使此常数依赖 q，也不改变大筛系数的绝对能量。

令 t=log(pr/(qs))、z=βs/q，则 |z|≤2D/d，
g 和 chirp 正好合为 H_z(t)=g(e^t)e(−ze^t)。
紧支撑固定，L1 有界，二阶导数 L1≪(1+|z|)²。
因此可取所有 q,s,n,m、β 共享的包络
W_d(τ)=C min(1,(1+2D/d)²/(1+|τ|)²)，
且 ∫W_d≪1+D/d。

Mellin 项是 p^(iτ)r^(iτ)(qs)^(-iτ)。
最后因子和 H_z 的 Fourier 系数虽依赖 q,s,n，
但取绝对后由同一 W_d 控制。
所以不是将不同系数序列直接塞入同一 large sieve；
是在每个固定 τ 上筛同一个整数产品序列，再以公共包络积分。

原 unit 源 (4)、(5) 的 p/r 交叉 profile 由 φ、φ² 的
对数变量 Fourier 分解。原 C²、紧支撑长 O(L) 使 Fourier L1
只付 log^C；对共同 u、q/s 的平移只产生单位相位。
纯 q 或 s 的剩余 profile 因子按原 sup 上界控制。
这保持同一 u，没有升级 φ 的微分阶。

每个固定全部 Fourier/Mellin 参数上的基本腿为
b_p p^(it1)、b_r r^(it2)，twists 不依赖 q,m。
q 依赖仅通过真实严格 prefix 和 CRT 频率；
s 的点排除在下一节单独支付。
因此公共包络可放在整 q,m 的 ℓ² 能量之外用 Minkowski，
而无需对每个 q,m 另选不能共享的大筛系数。

## 5. 非主角色归一化、固定系数与 mask

令 C_t 为模 q 的乘法卷积，C_0=0，
M0=Σ_t C_t、μ=M0/(q−1)。
对 units 置 D_t=C_t−μ，并置 D_0=0。
其零加性 Fourier 系数为零；对 b≠0 为 B_b+μ。
加性 Parseval 给 qΣ_(t≠0)|D_t|²，
乘法群 Parseval 给
q/(q−1) Σ_(χ≠χ0)|Σ_pα_pχ(p)|²|Σ_rβ_rχ(r)|²。
确认源 (11) 的符号与 q/(q−1) 归一化。

q 为素数，所有非主 χ modulo q 都 primitive；
principal modulo q 不 primitive，必须另付。
这里的 q/(q−1) 正好与作者定理 q/φ(q) 相同，
没有遗漏或重复一个 √q 的 Gauss 因子。

固定 dyadic boxes、残类、twists 和两个固定整数区间 I,J，取
c_k=Σ_(p∈I,r∈J,pr=k) b_p b_r p^(it1)r^(it2)。
它与 q,m 无关，长度 ≪Q²。
genuine-prime 唯一因子分解使每个 k 至多两个有序 pair；
即使 p=r 也不超过这个上界。
所以 Σ|c_k|²≤2Σ|α_p|²Σ|β_r|²≪φ1。
复权和可能的 ordered-pair 干涉已用 Cauchy 正确支付。

严格 p,r<q 是动态 prefix，不能直接作为固定 c_k。
每条腿以一个固定 binary interval tree 展开任意 prefix，
每次查询 O(L) 块，两腿乘积 Cauchy 付 O(L²)。
在每个固定 level 上，各 prime 坐标只归属一个 interval，
所以所有区间对的产品系数能量和再付 O(L²)。

可先在每个实际 prefix 使用 (11)，再在角色和的两腿作上述展开；
后续正求和允许将所有固定 interval 的 q 族扩到全部 q∼Q。
这避免为不使用的 q 偷换 prefix 或要求 interval 中每个 prime<q。
角色在 prime=q 时自动为零，primitive 大筛仍对固定 c_k 有效。
非主总能量为 Oφ(Q²L^C)。

主角色独立支付：|M0|²≪PR，全部 q,b 的 μ 能量
≪Σ_(q∼Q) PR/q≪Q²L^C。
它未被当作零或免费删除。

恢复 p,r≠s 时，用原未 mask 双腿减去 p=s、r=s，
再加双单点。由于 g≤1、profile 有界，统一于所有 s∼S 的
单点绝对大小分别为 Oφ(√R/√S)、Oφ(√P/√S)，双点 Oφ(1/S)。
整个 q,m 族平方费用分别
≪Q(X/S)R/S、Q(X/S)P/S≪Q²，
因为 S²≥X、P,R≪Q。
双单点更小。这是真实 sup-s 控制，不由 signed 子集范数推断。

d² 残类求和 Cauchy 付 d²。
所有残类的产品系数能量和仍 ≤2 原两腿能量积；
公共 Mellin 的平方费用 (1+D/d)² 将它变为 (d+D)²。
结合 binary prefix、主角色和上述 mask，确有非负 F_(q,m)^(d,a)，
同时控制全部 packet n、s 和共同 u，满足源 (14)。
其 ℓ²(q,m) 费用 Oφ((d+D)²Q²L^C)，不是逐 q 未证的 O(q)。

## 6. 全 packet 与全部 aspects 的预算

原外权给 Σ_q b_q²≪φ1、Σ_s b_s≪φ√S，
而 (2πs/q)ν(2πsn/q)≪S/(QX)。
同一 F 可以覆盖固定 q,m 的全部实际 n，
所以付 K_d 个数而不暗删 multiplicities。

对 q,m 的 Cauchy 因子为 √(X/S)，整族 F 的 L2 为
(d+D)Q L^C。故固定 d,a 的全 box 费用为
(d+D) S K_d/√X L^C，
即 (d+D)(QD/(d√X)+S/√X)L^C。
确认源 (15)，其中第二项完整消费了 K_d 的 +1。

每个 d 至多 d 种 a：
Q 部分为 QD Σ_(d≤D)(d+D)/√X≪QD³/√X，
S 部分为 S Σ_(d≤D)d(d+D)/√X≪SD³/√X。
因此 (16) 没有省略 a、m、n 或 residue 族。

全部 dyadic boxes、全部 q/s aspects、四个最大标签位置和
原 L^(-1)∫φ(u)²du≤1/2 只添固定因子或 log^C。
Q≤X、S≲Q，完整求和为 D³X^(1/2)L^C。
δ<1/14 同时满足最初 D≤X^(1/10)，指数比较成立。

## 7. 实际缩约与消费边界

低产品族先完整支付，高产品族在插入 g 后完整分割 major/minor。
(3)、(5)、(6)、(17) 合成 (18) 合法；
I_D 是保留真实 g、ν、共同 profile 与 conjugate positions 的
高产品 minor complement，不是原 signed whole 的任意正子矩。

所有 n=q m 属于 d=1 major，所以此精确定义的 minor 不含它们。
这不推广为其他任意频率子集的 nn 范数估计。
原 chirp、graph、边界付款仅作为冻结输入合入误差。

源 (19) 仍是一个待证目标。自然整 q² Parseval 能量 Q³，
与拟议 Q²(X/S) 相差实际 resolution 因子 QS/X。
即使这个目标将来成立，还须消费完整 s-mask/profile 及原 whole 桥。
本次没有将有限 Gauss/CRT 浮点恒等式作为该 sup-energy 或无限大筛证明。

最终限定结论：完整 major 付款和真实 minor 缩约通过；
minor、完整 scalar whole 常数预算、比例及 σ_* 均未改进。
此次不运行新的有限实验或旧覆盖，不生成 checkpoint。
全部三个本地链接已只读核对存在；审查只绑定以上最终源。
