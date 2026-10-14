# C015 原件审查：局部散射、奇偶分次与共同复源

2026-10-14；独立原件审查。仅消费 Burnol 的真实局部定理及直接运输，
不把原件声明、局部正迹或旧 Euler 恒等式登记为新的完整谱强制后果。
不修改 STATE、cadence 或 Git；结算及宏观选择由 root 统一完成。

## 1. 恢复与原件身份

已依次读 AGENTS、README、STATE，执行 research_state.py check/show，
恢复 GOAL.20261014、MACRO_FRONTIER、唯一 C015 和 D20261014P。
check 只证明状态结构。起始实际 HEAD 为
`8cba2c811ca301a17816a8330b40a2a1ef87c5d3`，原工作树无改动。
子代理 get_goal 返回 null，只说明本代理无单独 runtime Goal；
不能据此覆写 root 的 G20261014 active 观察。没有科学 producer 或续跑 session。
已有 543 仅给共尾全源负惯性预算，不支付正性或 Ξ 识别；
C015 的信息价值是查有分次来源是否提供旧 Euler 以外的共同源约束。

实际冻结原件：

- [Burnol v2 PDF](../../../literature/background/burnol-scattering-9901051v2.pdf)，
  源为 [arXiv math/9901051v2](https://arxiv.org/pdf/math/9901051v2)，17 页。
- [按 PDF 页标抽取文本](../../../literature/background/burnol-scattering-9901051v2.txt)。
  抽取器会丢掉部分上横线，因此复共轭符号另对照原 HTML，并由下文代数复核。
- [来源收据](../../../literature/background/burnol-scattering-9901051v2-source.json)。
  PDF SHA256 为
  `353f16b36139650a5221c0c6f6416a0da0bc5a47ff2d08a46c5468b9989d2c49`；
  text SHA256 为
  `4f526b453f9ccdac5733cf318571b980537f409a6e5540fdd60344dbbd1eeab3`。

PDF 页 1 标 arXiv v2，1 Feb 1999，内文 v2 日期 31 Jan 1999。
核读 pp.4–7 的 Haar、I/F、Δ、A/B/H；pp.8–10 的 incoming/outgoing、
S/K；pp.10–11 的 VII/VIII；pp.12–14 的 IX/X 及其 proof。
另核 pp.14–17 的 Connes 截断迹用途。本文只研究非 Archimedean 地方；
其局部定理不覆盖实际实位 Γ、双 pole 或全球源识别。

## 2. Haar、谱变量、核与域必须一并保留

设地方剩余域大小为 q，different 指数为 δ，uniformizer 为 π，
|π|=q^-1。加法测度自对偶，vol(O)=q^-δ/2。
单位群的乘法 d* 测度为 1，d×=(log q)d*，故单位处计量为 log q。
令 b²=q^-δ/2(1−1/q)，则 dx=b²|x|d*x。
从加法空间到乘法空间的酉变换是 φ(x)↦b|x|^1/2φ(x)，
不能漏掉 b 或换成 d× 后仍沿用同一范数。

乘法谱是按单位 character χ 分解的圆，z=q^iτ，圆测度 dθ/(2π)。
原乘法变换使用 ∫g(t)χ(t)|t|^iτd*t 的正号约定。
U(π^-1) 在谱上是乘 z。I 在乘法坐标是 g(t)↦g(t^-1)，
谱上同时反转 character 和圆坐标；F I 是单位模 Γ_local 的乘子。

Δ 是只占有限 χ 分量、每圆上光滑的稠密域。
S₀(K)⊂S(K)⊂Δ，且 S₀(K) 是 H 的 core；Δ 对 A/B/I/F 和 dilations 稳定。
A=log|x| 在谱上为 D=(log q)z∂_z。
原 proof 由 IBI=Γ_local^-1 AΓ_local=A+H，得到 B=−A+H。
因此 conductor H=A+B 的符号来自局部函数方程，而非由目标 Weil 值指定。

写 r=q^-1/2，P_r(z)=(1−r²)/|1−rz|²。
原未分歧符号等价于

    H(1;z)=(δ+1)log q−(log q)P_r(z)，
    H(χ;z)=(e(χ)+δ)log q，χ 非平凡。

Γ_local(1;z)=z^δ(1−rz)/(1−r z̄) 的对数导数直接复核此式：
z∂_z log Γ_local=δ−rz/(1−rz)−r z̄/(1−r z̄)。
恒等式 P_r=1+rz/(1−rz)+r z̄/(1−r z̄) 支付符号。
这里 Γ_local 是 Tate 乘子，不能与完整实位 Γ(t)=2θ′(t) 混称。

原 interacting 空间为 K=L²⊖(D_-⊕D_+)，
D_- 是支持 |x|≤1 且加法积分为零的空间，D_+=F D_-。
积分条件使 Fourier 像避开原低球，付 D_-⊥D_+。
K_χ 维数为 δ+e(χ)−1+2·1_(χ=1)。
其中平凡分量含 ω=1_O，单位范数向量 q^δ/4ω 的圆谱是
sqrt(1−1/q)/(1−r z̄)；它贡献 K 对角的 Poisson 项。
ramified 分量的有限 monomial basis 贡献 e(χ)−1。

## 3. VII、VIII 的 proof 与正性的准确对象

VII 使用 K 为正交投影及圆上光滑核的绝对 Fourier 求和。
对 ξ∈Δ，原轨道和是

    ⟨Tξ,ξ⟩=(log q) Σ_(j∈Z)||K U(π^-j)ξ||²
            =∫_(K×)||K U(t)ξ||²d×t。

有限单位 character 和圆光滑性付收敛，再由核对角得到

    T(1;z)=(log q)(δ+P_r(z))，
    T(χ;z)=(log q)(δ+e(χ)−1)，χ 非平凡。

所以 T 非负，初始 Δ 上本质自伴。
这不是声称 H 非负。VIII 的 proof 是逐谱分量比较：

    T=δlog q+|(δ+1)log q−H|。

平凡分量的绝对值采用 −H+(δ+1)log q；
ramified 分量采用 H−(δ+1)log q。
ζ 的 Q_p 均 δ=0，且需要单位不变、χ=1 分量，故

    a=log p，r=p^-1/2，T_p=a P_r≥0，H_p=aI−T_p。

其 H_p 的精确范围由 Poisson extrema 得到：

    min H_p=−2ar/(1−r)，max H_p=2ar/(1+r)。

换取 ramified 的正 H 分量，会换掉实际 ζ Euler 数据。
原散射 S(1;z)=z^-δ(√q−z)/(√qz−1) 的 phase derivative 给 T，
并非给 H 的正性。它是局部 causal 散射，不是未知 ζ 零点的 global scattering matrix。

## 4. IX、X 的迹域、分次和单位项

用 F 表示迹公式的乘法测试函数，避免把它与源向量 ξ 混同。
原 IX 先取 F 为 K× 上 Schwartz–Bruhat 且支持 |t|≥1。
有限 character/有限 annulus 分解使 Z(F)=∫F(t)Z(t)d×t 有限秩，
不是先假设某个无限 Hilbert 对角可取迹。
在 K_χ 上 Z(π^-1) 的非 ω 部分 nilpotent；
ω 商的 eigenvalue 为 q^-1/2。
proof 由有限维迹得到单位项和几何响应，再以 Cauchy residue 与 T 的 Poisson 符号对齐。
随后 |t|<1 部分按 Z(F)=Z(IF) 扩展，单位层只计算一次。

因此 IX 的测试范围是一般乘法 Schwartz–Bruhat F，
没有要求 F 自相关或 F̂≥0。
T≥0 与 Tr Z(F)=∫F̂ T 并不使任意 F 的迹为正。
若另取 F=ξ * ξ^⋆（中间 * 为卷积，ξ^⋆(t)=overline{ξ(t^-1)}），
则 F̂=|ξ̂|²，正的标量迹才由该额外选择支付。
这一选择可由实际物理 f 实现，见下一节；不是原 X 自动附送的条件。
一般 ramified 情形不据这条标量公式宣称 Z(F) 为正算子。

X 的 grading：span ω 为 odd，正交补为 even。
超维数为 δ+e(χ)−1。其 proof 对平凡分量使用
H+T=(2δ+1)log q 与已付 IX，ramified 分量直接比较常数，
再由 inversion 拓展两侧。所得局部 explicit-formula 项是

    H(F)(1)=sTr Z(F)+F(1)log q。

关键的 ζ specialization 更强于“有正有负”概述：
Q_p、δ=0 的 K_1 维数恰为 1，完全由 odd ω 占据，even 部分为 0。
所以对所有单位不变 F，有

    sTr Z(F)=−Tr Z(F)，
    H(F)(1)=aF(1)−Tr Z(F)。

正的 unramified time-delay trace 进入实际 ζ 局部项时整体带负号。
不能擦掉 grading 或 F(1)a；不能把单位项再留在全式中额外加一次。
原 paper introduction 也只为此 grading 提供实现局部公式的动机，
没有给出独立 global arithmetic polarization。

## 5. 对同一 complex physical 源的 exact 运输可以支付

这一节是直接核算，不依赖未付的 global inequality。
令 f∈Cc∞((-L,L)) 复值并零延拓。固定实际 p，a=log p。
对几乎每个 v∈[0,a)，令 c_k(v)=f(v+ka)，只有限 k 非零。
取单位不变本地乘法向量

    ξ_v(p^-k u)=c_k(v)，u∈Z_p×。

它是有限 annulus Schwartz–Bruhat 向量；本地加法向量为
ξ_v(t)/(sqrt(1−1/p)|t|^1/2)，满足原 Haar 对应。
原正号谱变换为

    ξ̂_v(z)=Z_pf(v,θ)=Σ_k c_k(v)e^(ikθ)。

每个向量的圆 Parseval 和 dv 分解给

    ∫_0^a∫_circle |Z_pf|² dθ/(2π)dv
       =∫_0^aΣ_k|f(v+ka)|²dv=||f||²。

因此 C015 所需共同 physical norm 并不需要新的假设。
每 p 的 Zak 变换是原 Lebesgue L² 的酉分解；v 是连续 fiber，
不能直接用一个 scalar periodization 或 ξ̂_v(1) 代替完整 dv/circle 积分。

取 F_v=ξ_v * ξ_v^⋆，则 F̂_v=|Z_pf|²，且

    F_v(1)=Σ_k|c_k(v)|²，
    F_v(p^-m)=Σ_k c_(k+m)(v)overline{c_k(v)}。

定义 k_f(t)=∫f(u+t)overline{f(u)}du。
积分 dv 后 F_v(p^-m) 正好给 k_f(ma)，反向由共轭给 k_f(−ma)。
于是原 IX/X 对每 fiber 可合法消费，再作有限和/连续 dv 积分：

    E_p(f):=∫_0^a∫_circle aP_r(e^iθ)|Z_pf|² dθ/(2π)dv
            =a||f||²+2aΣ_(m≥1)p^-m/2 Re k_f(ma)，

    ∫_0^a H(F_v)(1)dv
            =a||f||²−E_p(f)
            =−2Σ_(m≥1)(log p)p^-m/2 Re k_f(m log p)。

这里独立核算了 P_r=Σ_(m∈Z)r^|m|e^imθ 的 Fourier 系数，
不是把原 paper 的 trace test 凭名称当物理源平方。
完整 complex 源被保留；没有只取偶/实源，交叉相关靠 Re 和 reflection 成对支付。
所有 m log p≥2L 的相关严格为 0，故有效项恰是 p^m<e^(2L)。
若 equality p^m=e^(2L)，零延拓 L² 源的重叠仍为空，不能凭 cutoff 插入 boundary atom。

Poisson 符号对 fixed p 有界，

    a(1−r)/(1+r)||f||²≤E_p(f)≤a(1+r)/(1−r)||f||²。

因此纤维等式从 smooth 源连续延到整个固定窗 L²，
再与原完整 Γ 的 Dlog 闭型域相交，无本地导数费用。
fixed L 的 actual prime sum 有限，只剩实位 Γ 是无界形式。
这一运输支付源、规范和单位项；它本身没有支付 prime 间的 joint inequality。

## 6. 大 prime 的精确相消与 direct sum 的费用

当 p≥e^(2L)，对每 fiber 支撑最多占一个 lattice 点。
此时所有非零 shift 相关消失，E_p(f)=a||f||²，
整个 H_p 贡献严格为 0。原 positive local trace 并未消失；
它与单位项在每个 p 上恰好相消。

对有限实际 prime 集 S，原 full Weil identity 因而是

    Q_L(f)=(2π)^-1∫ Γ(t)|f̂(t)|²dt
             +2|C(f)|²−2|S_pole(f)|²
             +Σ_(p<e^(2L))[a_p||f||²−E_p(f)]，

Γ(t)=Re ψ(1/4+it/2)−log π=actual 2θ′。
双 pole 的 C/S_pole 与原完整源定义保持；本地原 X 不证明这两全球项。
上述式只是原 actual explicit formula 的同源重写，不生成额外常数或删去任何 pp。

未经重整的 all-prime direct sum 不提供有界共同极化：
每个 Zak 分量范数都为 ||f||，故非零 f 的 Σ_p||Z_pf||²=∞。
同样 Σ_p a_p||f||² 与 Σ_p E_p(f) 各自发散；
后者甚至在所有足够大 p 上等于前者。
合法消费必须先在同源、同 prime 上减掉单位项，才能取无限 prime 表示。
给 finite S 的 direct sum 加任意 isometric normalization，会同步改变系数；
不能再不付费用地沿用原 Weil prime 权。

所需正性形式若写成

    Σ_(p<e^(2L))E_p(f)
       ≤Σ_(p<e^(2L))a_p||f||²
            +(2π)^-1∫Γ|f̂|²+2|C|²−2|S_pole|²

就正好是原 Q_L(f)≥0；局部 T≥0 不蕴含该方向。
把这个 unknown 改名为“global graded domination”不算新的独立输入。
源共同性提供实际约束，但原 VII/VIII/X 没有给它与 Γ/pole 的联合费用。

## 7. 与最强已付资产扣除及可消费结论

已核旧资产：

- 017 的 unitary Euler edge 与正 graph−负常数分解，已明确 global domination 未付；
  本地 Poisson 展开和精确 pp 身份属于同一已付 Euler 数据，不重记新 forcing。
- 510 的实际实位 Fourier/inversion 与完整 Γ 相位/普通相对迹，含单位元；
  原 Burnol paper 没有替代其全实位域证明或给新的 joint 正性。
- 531–535 的真实 canonical ordinary Sonin 正迹、common physical norm、
  compact bridge、晚 prime 子项与无费比较边界，保持各自对象范围。
  本审查的 Lax–Phillips K 不等于 canonical Sonin P_p；不能拿 535 直接排所有 graded 方法，
  也不能取消本 paper grading 后把它伪装成已停止 ordinary 正迹桥。
- 016/028 的 exact degree 与强负迹、543 的共尾 Ce^S 预算是完整谱对照；
  本地 norm/trace identity 尚未给任何超出这些已付后果的新 whole bound。

原 proof 支付：local H/T/K、δ0 符号、odd grading、单位项、有限秩迹域。
直接运输另支付：同一 complex f 的真实本地 autocorrelation 测试、原 L² norm、
strict 全 pp 与 fixed-L Dlog 交域延拓。
缺项仍是成长多 prime 与 actual Γ/双 pole 的共同 signed/core 估计，
或非循环的算术几何极化。世界优先权与新 global theorem 未声称。

准入结论：只有这些定理和运输，C015 的“新 joint 信息”门未通过。
建议 root 不用原局部正迹/旧 Poisson 身份晋级，也不花下一轮微调该重写。
这不是“所有 graded/multi-prime 方法不可能”的定理。
重新准入应有原件中真正跨地方关系、共同源 signed inequality 或新 global geometry，
并同时付实际规范、growth/error 和超最强旧资产的净后果。

本审查为原件核验/旧工具消费，不单独增加数学轮；
宏观瓶颈未因 local 公式和 exact norm 运输而消除。

## 8. root 544 最终 source/scope 消费核验

后续只读核验
[544](../../../notes/544-graded-local-source-admission-without-new-joint-input.md)，
当次消费 raw SHA256 为
`e54479df63ccb7d12301a45e2b0f65eda5f5938d3b1cfb61d9a26f494260fa18`。
已再次恢复 AGENTS/README/STATE/check/show、Goal/frontier/C015/D20261014P、
实际 HEAD 与 cadence。现场原 cadence 仍 2，latest settled 为 543；
当时 STATE 尚为 C015 running，最终入口停止须 root 自己保存，
本补审不据主文措辞提前认证 STATE 或 runtime 终态。

接受 544 §§1–4 的原件消费范围：

- Q_p δ0 的 T_p=aP_r、H_p=aI−T_p，K_1 纯 odd，
  原 X 的一般 Schwartz–Bruhat 测试与另选 ξ*ξ^⋆ 的正标量迹严格分开。
- Haar/Δ 的本地 proof 没有被当 global Γ/pole proof；
  common complex 零延拓源、Zak 原范数、全部 strict pp、log p 权与 Dlog 交域运输准确。
- 共同范数这一定位缺口现已核清，但没有随之产生新的 joint inequality。
  单位项须逐 p 相消，大 p local 正能量并未凭支撑消失。
- physical filter 与 mixed Gram 只是上述局部响应的直接有界平方分解；
  没有由 cross kernel 或 bare all-prime direct sum 宣称新的 global 方法类障碍。
  actual old Euler/graph 和最强 016/028/543 对照仍被扣除。

因此接受 root 对本件的计数判定：**C015 入口停止，零新数学结算轮**。
读取原 proof、完成本地 norm 身份、写出旧 filter/direct sum 消费规则，
均不足以把本件改成“完整新数学失败轮”。保存来源准入记录可以改变下一动作，
而数学 cadence 保持 2、latest settled 保持 543；不能新增 whole forcing 或 Goal 完成声明。
544 并未排所有 graded/multi-prime/scattering/source-adaptive 方案，
535/529 的已付边界与其他暂停路线也没有因此自动复活。

544 §5 只登记 modular Eisenstein 的下一来源准备，并明确 original physical norm 桥未付。
本次 source 终审仅确认该段没有冒充已核 actual-Weil 定理；
它不代替将来 C016 对 Zagier/Garrett 原证明、全 Gram、cutoff/error 与规范的独立审查。
未发现原 VII/VIII/X、grading 或 common physical transport 的误消费。
