# 579／C042 整稿独立 fresh：实际 KRY 源接口与 native primitive 首门

2026-10-23；独立于三分支的整稿检查。只编辑本文件，不结算 STATE、cadence 或合同。结论是**限定 PASS**：允许消费一个具体实际源候选的完整解析接口和精确失败门；不允许消费相对 primitive 循环构造、独立正性、二次容量或成长经典 ζ 后果。

核读对象为 [579](../../../notes/579-kry-physical-gaussian-source-and-native-primitive-obstruction.md)、[C042](../../../goals/contracts/C042-kry-gaussian-source-and-relative-primitive-gate.md)及本目录三个原稿。405、537、545、552、553和上轮来源审查作为已消费输入；其原先 paid/open 意义不改变。现场结构 check/show 通过只说明状态结构，不能认证本数学判断。

## 1. 原件和 native 规范确实对齐

对唯一外部 [KRY1999 作者版](https://www.math.uni-bonn.de/people/rapoport/myalggeom/preprints/tinynew.pdf)，独立核了 §1(1.4)、§2 native Schwartz/正定无穷位、Lemma 2.1(ii)、Theorem 1/3 和 Proposition 5.1／§6(6.8)附近实际对象。该原件确给 weight 1 Gaussian、局部表示到诱导 section 的映射，以及 CM 有限循环的线性 degree 身份。正指标 n=1、q=7 的 degree 由其公式为 2 log 7。CM 底空间 generic dimension 0；不存在本稿已构造 C×C 型 primitive mixed 自交的事实。

579 采用同一实际 φ* 的二维 unitary dilation，并保 ν=||φ*||²；没有把 raw Lebesgue 宽度 1 的 ν₀=1/2 擅移到原件 Haar。只要 φ* 是固定实正定 Gaussian，直接积分与伸缩给

\[
 \langle D_u\phi_*,D_v\phi_*\rangle
  =\nu\,\operatorname{sech}((u-v)/2),\qquad
 \|T_*r\|^2={1\over2\pi}\int
 2\pi\nu\,\operatorname{sech}(\pi t)|\widehat r(t)|^2dt.
\]

因此 squared operator norm 为 2πν、注入性成立；raw ν₀=1/2 时恰恢复 π。最低 Gaussian 线的正交投影系数是 c(r)=∫r(u)sech(u/2)du，不多一个 ν；||c||²=4，fixed 窗版本为 4 tanh(L/2)。这些常数及 Fourier 的 2π 因子已独立复算。ν 不是完成化 B(s) 的自由度。

## 2. 原域、section 与真实费用

逐导数缩放给半范数权 e^{(1+|β|−|α|)u/2}；S_exp 的双端任意指数衰减支付全部加权绝对积分。所以 T*:S_exp,C→radial Schwartz 连续是真正原域结论，不靠 L² 延拓冒充 Schwartz。fixed 支撑 [−L,L] 的 √(2L)e^{|1+|β|−|α||L/2} 费用也正确，常数随阶和 L，不能说成长统一有界。

原 du 到 Gaussian Hilbert 像的全线 upper 合法；zero-extension Dlog/Hlog 更强，仍可付此 upper。双 pole 矩分别变成 T*r 的原点值及积分，乘固定非零常数。它们不能代全部 section 关系或算术 height 费。

λ_C 在径向像上注入的证明成立：有限腿取 identity，所有 arch wn(b) 评价是半轴径向剖面的一维 Fourier transform。若全 b 为零，Fourier 唯一性先杀径向 Schwartz，再由 T* 注入杀 r。只看 identity 和 w 两点远远不够。

section 的全线 norm 反测也用的是实际源族。raw 读出 F_b 满足 F_{e^a b}(τ_a r)=e^{−a/2}F_b(r)；双 pole-zero 和原 du/Hlog 随 τ_a 保持，而 b→0 的同一固定 compact 上 sup 无界。每 fixed 源／fixed 窗的 Fréchet 费用依然存在。本反测没有把全空间 inverse norm 当个别源必要费用。

## 3. 405 全主关系与 537 非根都经过实际检验

405 的 h=Eη>0、H=e^{u/2}h>0 在 S_exp 中，p=(D²−1/4)H 非零且是完整真实 Pan；不得裁成 compact。s₀=sech(u/2) 满足 (D²−1/4)s₀=−s₀³/2。带权分部积分没有边界，所以对全部实 a

\[
 c(\tau_ap)=-\tfrac12\int H(v)s_0(v+a)^3dv<0.
\]

这精确证明 native 线不消任何这个实际关系轨道；raw T* 和 λ_CT* 注入也保留它。没有依靠 RH、零点或 Q 值选源。

根稿新选的奇源更简明，核算正确。取非零非负偶 φ∈Cc∞((−1,1))，ψ=uφ，r*=(D²−1/4)ψ。r* 非零实奇、compact；两 pole 矩为零，c(r*)=0 因奇偶。原 537 full-complex 窗定理给 Qζ(r*)≥2^{−49162}||r*||²>0。因此实际非根被 native 标量入口杀掉。另一个非负 ψ 给 c<0 只说明某些非根可保，不能推全源 coverage；主稿没有混淆它们。

## 4. 实际循环、principal 与 fixed relative 的准确范围

严格投回 native Gaussian 线后，已证全 theta derivative 只乘 c(r)。于是 c(r)Z(n) 是实／复系数循环的实际接入，尚非一般整系数线丛。q=7,n=1 的有限循环配上零 arch 分量有正 degree，故 c(p)Z(1) degree 非零；它不是 principal Arakelov divisor。principal 必须同时带同一函数的有限与 arch 分量、总 degree 零，此处没有遗漏这项。

若 Π 对选定实／复系数字段线性且固定，Φ(r)=c(r)ΠZ(1) 的二择直接成立：ΠZ(1) 非零则 p 不消，ΠZ(1) 零则全家族为零、也杀 r*。对所有指标及 arch/constant 项统一做 fixed coefficient-linear 操作，仍因同一 c 因子而失败。这不是未知正性推论，不需要 Hausdorff 性或 boundedness。

若讨论复杂源上仅实线性的 Π，字面复数提出须改成两实坐标；但用 p 与 ip 两个完整主关系后也会杀整个复标量家族。根稿已修为同字段线性，并显式给出仅实线性时的两个坐标；本审再次核读修订，结论正确。它没有偷扩为所有非线性／源依赖 relative 构造。源依赖 frames、变化 finite Schwartz、高 K-types、非标量边界和非有界 height 未被排除。

## 5. 高频费、polar 与 finite Euler 都没有越界

固定 compact 高频源减两固定 dual 模板可精确消 pole；修正 O_N(τ^{−N}) 正确。Gaussian 像能量对每 N 为 O_N(τ^{−N})，原 Hlog 及完整 Qζ 的主项为 (log τ)||h||²。fixed 支撑的全部 prime-power shifts 是原 du bounded form，pole 精确零，Γ 的 log 高频项保留。因此 bounded Gaussian energy 加 O(||r||²) 不可能等同完整型；不排 genuinely unbounded arithmetic height。不能加强 Gaussian 像为指数小，主稿已明确没有这样做。

先 K^{-1/2} 输入的 cosh 指数 Fourier domain 排非零 compact，证明成立；但 direct polar U=TK^{-1/2} 的组合延拓是合法酉映射，亦成立。Γ(1/2−it) 的无零及 dense range 付清 onto radial L²。U 未被证明回 Schwartz/cycles，仍不消 Pan；再接全域 du/Hlog bounded Hausdorff 读出消所有 Pan，旧 553 密度才给全零。这里准确保留 545 的 direct normalization 逃逸，没有重新报告旧 no-go 为新定理。

有限 Euler 真实源操作是所有 shifts 的有符号和，Fourier 乘子 B_F(σ+it) 与 T* 后的乘子权 2πν sech(πt)|B_F|² 正确。它完整保所有 mixed 项、支持安全范围 I+[0,2Σ_F log p] 和双 pole-zero。每个位 degree≤2 的逆多项式是完整 Euler 因子的精确逆，并非漏 proper powers。根稿已补明：这只是给定 Mellin 乘子在实际 source／Schwartz 像的实现，未给 KRY relative cycle inverse functor／height，也未给全 (20)→Qζ 运输；此新增范围修订已再次核读通过。

全线 operator norm 可由有限 log p 的 torus 稠密取到 supremum；要成为 actual 源费，必须另选随 F 变化的长 packet 和 phase。分支给出这层限定，σ>1 一致绝对费不移到中心，σ=1/2 operator 大也不冒充固定 r 或 q_R necessary lower，均正确。

579 的新增有限 F 轨道断言可独立闭合。设 g=A_{F,σ}p、J(a)=c(τ_ag)，则

\[
 \widehat J(t)=2\pi\operatorname{sech}(\pi t)
 B_F(\sigma-it)\widehat p(-t).
\]

非零有限 Dirichlet polynomial 在实 t 上至多有离散零点；p≠0、p∈L²，故右式不可能 a.e. 为零，J 不恒零。因此任何有限 F 不能把整个真实 Pan 轨道消掉。仅证明“至少某个 a 非零”，没有声称每 a 同号或全 F 无限极限不可能。有限 A 既保 Pan 又不能修 native 全关系，这一反测不支付或否定其他 infinite signed 接口。

## 6. 连续和函数域对照

独立复算了 (23)。d>0 时 ψ 的 Fourier 正弦系数是 −i√d B，r* 的乘子为 −(d+1/4)，故 Q_d(r*)=2d(d+1/4)²B²>0。d<0 时 odd ψ 的两 Laplace 矩互为相反数，(D²−1/4) 给同一 (−d−1/4) 因子，得到同式且为负。d=±1/16，u∈(0,1) 的 sin/sinh 因子均正，B>0；没有负号或 √d 漏失。

同一 r* 的 c=0 而 Gaussian 能量正，确实反测“通用外加正能量／单 scalar 无独立身份即可成为 native Weil 型”。continuous 背景 Γ=0 不能冒充经典 Γ；未给 continuous→CM 几何 map，也不能声称它满足或反驳 KRY 定理。

真函数域保 C×C 的双 degree primitive、全 mixed 交数、RR/有效性或 Rosati 独立符号；保 H⁰/H² 与全 returns/aliases。CM generic-dim0 的 degree 不是该二次链。主稿只消费旧 567/576 对照，没有声称本轮付 FF→CM 运输或新的函数域定理。

## 7. 新旧、消费结论和停止

相对上轮 source0，本轮实际执行了一个先前未给公式的具体接口：全 S_exp 的 KRY Schwartz 轨道、exact 原 norm、native c(r)Z(n) 的真实循环接入、405 非principal 与 537 coverage 双失败，并核 finite Euler 实际像和合法 polar。它们能作为**同一个候选接口的完整一轮检验**，不能逐公式／分支各计轮。405 Gaussian 关系、545 direct 补偿、552 高频比较、553 密度及上轮 signed 差/商责任均为旧输入，已扣除。是否结算一次由 root 一次执行，本文件不增加计数。

限定 PASS 的可消费净值是：从“物理源接口尚未算出”推进到“实际解析／标量循环接口存在，但指定 native／fixed relative recipe 在容量之前精确失败”。它不是一个成功的相对 primitive lift，更不是新的独立经典正性或容量。

strongest-old 542+555→557 whole leading 4/5 仍为负惯性**上预算**，无改进；actual q、同对象 primitive 二次容量、成长 core/coupling/Ξ 未付，宏观完成门不通过。完整 Γ/FP-contact、所有 prime powers、双 pole 与 fixed／强源／D′／成长／全线量词均保持。

停止本 native 标量／fixed relative、raw bounded-energy 与无费预逆入口。不自动续 Gaussian 宽度、有限 F、K-type 阶、q/level 或下一 paper。下一只有新的实际非标量源/边界公式，先付 405 全 principal 同构与 537 非零和原费用，再核同对象过滤、截面乘法、二次容量及完整 signed 身份；强拓扑、非有界 height、源适应、变域及有费无限完成仍保留，但名称本身不是新输入。

本次最终复核的 579 LF SHA-256 为 `8d56791706d8acc6fce54d4d774c1589fba4584b4a0f2e3b4e0cec39c8a767b8`。若对象、系数字段、映射范围或费用意义再变，须由 root 重新闭合相应消费；hash 仅绑定版本，不替代上述证明。
