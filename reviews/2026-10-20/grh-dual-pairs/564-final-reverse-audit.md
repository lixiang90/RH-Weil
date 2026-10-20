# 564／C027 独立终逆审：PASS（限本文所列完整前件）

2026-10-20；独占终审原稿，不改公共状态、cadence、原证明或 Git。
已恢复 README／STATE／check 后 show、固定 Goal／frontier／C027／最新战略及 D20261020D，
并核实际工作树。审查是 0 轮，不代 root 消费或合同结算。

**结论：当前五个版本通过。** 发现并已要求修正的一处必要范围问题：564 原 §6 的
Dirichlet 完成化函数方程应限于 primitive χ；root 已补“非实 primitive Dirichlet χ”，
本审查复读确认。独立 paired 原稿本已保留该前件。以下 PASS 绑定修正后的版本。

## 1. 按最强结论倒推：同一整数系统的规范反测试确实成立

算术对象始终为普通整数／素数，不以未知经典零点为输入。取 λ=2、A=2^{1/4}：

\[
B(s)=1+A^2/\lambda+A\lambda^{-s}+(A/\lambda)\lambda^s=B(1-s).
\]

三个 Gaussian 的物理核系数全正；Fourier 缩放把第二、第三项精确交换，故
\(\mathcal Fg_B=g_B>0\)，这里使用全实轴 e^{-2πixξ} 的单位酉规范。
Mellin 缩放独立给 G_B=B G_0；不依赖任何形式商构造。
逐项 Poisson 的缺陷恰为 B(0)(x^{-1}−1)/2，未丢原点／极点。

全平面延拓由实际公式

\[
\Psi_B(s)=\int_1^\infty F_B(x)(x^{s-1}+x^{-s})dx
               +\frac{B(0)}{2s(s-1)}
\]

支付。Gaussian 尾给整个积分及闭竖带一致 Riemann–Lebesgue 衰减，F_B 在 0 为 O(x^{-1})，
在无穷快于任意幂；因此这里 HL 的连续性、两端增长、有限极点和竖直衰减全有真实输入。
B(0)>0，所以 Ψ_B 仅有 0、1 两个不消去的简单 pole。Gaussian 积分的
log M(R)=O(R log(R+2)) 给 E_B=s(s−1)Ψ_B 阶≤1。

B 的两个因子分别在 Re s=1/4、3/4 及奇数倍 π/log2 的频率消失；这些点不在 Ψ_0
的两个 pole 上。Ψ_0 若也消失只会加重数，不能取消。因此 E_B 确有离线零点。
而 B 在中心线上为 |1+2^{-1/4}e^{it log2}|²>0；中心线乘子正也不能消去离线除子。

这严格否定的是“允许任意正且 Fourier 自对偶 Mellin 核后，其所有 completed 根仍居中”。
它没有改变普通 ζ，没有反驳经典 RH，也没有给原固定 Γ／pp／pole 的 actual Weil 泛函负方向。
canonical completion 或预先指定 relative divisor 是必要的对象数据，不能后验随零点选 gauge。

## 2. 移位模型的 primitive 正性并非免费倾斜

独立重算了 b=h+1/2>0、Δ=1/4−c∈[−1/4,1/4) 的二项式：

\[
A_m(h)=2\sum_{k=1}^{\lfloor m/2\rfloor}{m\choose2k}
b^{m-2k}[(1/4)^k-\Delta^k]>0\quad(m\ge2).
\]

Δ<0 的偶 k 端点允许括号等于 0，但 k=1 严格正，且 b>0，故所有 m≥2 仍严格正。
四个底数模≤R=h+1，得 A_m≤4R^m；这覆盖原稿的全部 h>−1/2、0<c≤1/2，
不是仅在 h≥0 或 c≤1/4 下的估计。
由此 primitive p_h 真正正且对每个 σ>R 加权可积。

重复幂的 k^{-1} 权和密度 Jacobian 再给一个 k^{-1}，所以系数正好是
Σk^{-m-1}=C_m；Tonelli 支付 q_h=e^{hu}q_c 的完整身份。
直接倾斜 P 会产生 e^{hu/k}，原稿正确禁止该偷换。
加权正卷积指数存在，Laplace 唯一性给
δ_0+c(e^{(h+1)u}−e^{hu})du，以及物理侧 δ_1+c(x^h−x^{h−1})dx。
这里 prime、powers、integers 三层均已付，非仅 Π≥0。

对 |h|<1/2，两个 ±h 系统均在刚核的正范围；反射精确给 Z_h(1−s)=Z_{−h}(s)。
全部真实 pole 是 h,h+1 与 −h,1−h，未偷换成共同 0,1。
各 own-center a_h=h+1/2 由输入的 pole 中点预定，归一化 Weil 核恰退回 W_c。
c≥1/4 的平方和及 c<1/4 的负向测试依赖 562 已付结论，不再次计收益。

新增共同中心测试的系数已核：c=1/4 的两个双根合并给 4cosh(hu)，
g(u)=uφ(u)、φ 非零非负偶 compact 时，Q=−4(∫g sinh(hu))²<0。
因此 positive primitive 乘积及精确自对偶并不保证错误共同中心的 PSD。
两权产品的 c_1=5/16、c_2=13/36 分别给频率 1/4、1/3；四个 pole 与复零点无抵消。
grading 为构造输入，不是从未知根后验拆权；主 N 指数的一半通常确不等于 own-center。

## 3. 配对框架的箭头和域均未扩大

线性 Mellin 对偶 E_1(s)=εE_2(w−s) 只搬运跨对象除子。给定 a_1+a_2=w 后，
两成员右半平面分别无零 ⇔ 两条互补纯线，证明的反向确需同时核两成员，不能只核一边。
非空单权自对偶或同规范共轭兼容才把 a_1=a_2=w/2 强制出来；多权 whole 不受此推理。
反线性反射 2a−bar s 与线性 w−s 在正文和原稿中分清了。

有限维正极化命题中，B(U_1v,U_2η)=B(v,η)、U_2C=CU_1、
h(v,z)=B(v,Cz)>0 精确推出 h(U_1v,U_1z)=h(v,z)。
两个 U_j 均可酉化，因而原 F_j 也半单；这条强结论正确依赖输入正定性及兼容 C。
若只知纯模，则不能反灌原 Frobenius 半单／既有正内积，正文已明确保留。
有限 determinant FE 的 q^{-ns} 前因子和以 q^{ns/2} 完成化的零自由规范亦核正确。

packet G(z)=E_1(a_1+z)E_2(a_2+z) 为偶；real-type 或共轭 packet 后才调用实偶热接口。
它的除子为正重数并集，没有 quotient cancellation，才能由 packet 居中推出每成员纯。
非实偶单成员丢弃奇频信息的 Gaussian 热量不充分，δ_1−δ_{−1} 反测试正确。
off-diagonal 自伴块的负方向和 dilation 只读奇异值的反测试均正确，不制造 faithful 原谱。

无限维部分未将形式反对称升级为自伴：须独立给群、稠密域、闭性和最大反自伴性；
普通 trace／determinant 还须完整身份、整数维重数、中心零点因子、计数及零自由规范。
连续谱不自动具有普通 trace；562 的分支／连续谱边界没有被覆盖。

## 4. 原始来源与算术适用层级复核

本审查独立在线复核 [HL arXiv v1](https://arxiv.org/html/math/0410270)，
§3.2 Theorem3.2 式(3.5)–(3.6)：原件确以已给两连续 F 为输入，
0 端 O(x^{-1−ε}) 对每个 ε>0、∞ 端 O(x^{-β_r})、β_r>1；相应条带及有限 pole 条件
与独立来源稿一致。v1 确有重复 §3.2，以及核增长指数冲突；原稿采用实际 Mellin 可积条件，
不照抄冲突指数，是准确修正。其引言的普适 fractal-membrane dual 图景为 conjectural，
Remark 所引后续为 in preparation；本次未取到证明，正文没有冒称任意 positive arithmetic dual 已得。

作者原始 D↔1−D／self-dual⇒D=1/2 是维数固定点；固定 D 逆谱命题与
“所有 D≠1/2”总体 RH 量词没有混同。
[Kedlaya 第6章](https://kskedlaya.org/ant/chap-funceq2.html)确在 primitive 前件下给共轭 Dirichlet FE；
修正后的564与原稿一致。复 twisted 权不被误称正 primitive 计数。
[Milne Theorem5.1](https://jmilne.org/math/xnotes/pRH.pdf)给 H^j 纯模 q^{j/2}，
Poincaré 对偶权和为 d，因此两中心 j/2 与 d−j/2 一般不同。
曲线 H0/H2 在 0/1、H1 在1/2，以及整个 ζ 的 superdeterminant 区分均正确。

## 5. 净后果、旧资产扣除与结算边界

已复读001/002相关正极化／同权 packet，以及290正整数 Euler＋分次对偶离线模型。
564 末段准确扣除了这些强旧蕴含。正极化→纯权的标准定理、562/563 的判据／证书、
对偶本身不足的旧反例均不应在本轮重计为新数学收益。
当前完整 C027 的具体新检验范围是同一整数系统的实际正 Fourier 自对偶 Mellin gauge，
以及真正正 primitive 的 ±h 不同权 pair／共同中心负测试；由 root 统一消费至多一轮。

actual ζ 的强旧542＋555→557 whole leading4/5不变；560成长 K/core/coupling、
原 du/Dlog 域的独立完整 Γ／全部 proper powers／pole 正性，以及 faithful Ξ 未付。
本 PASS 不表示 root 已消费、不 complete 长 Goal、不 authorize 新合同；审查自身 0 轮。

## 6. 最终规范 LF 版本绑定

以下 SHA-256 仅识别本审查实际读过的最终 UTF-8／LF 字节，不作为证明或前件替代。

| 文件 | LF bytes | LF SHA-256 |
|---|---:|---|
| notes/564-dual-pair-rh-weighted-purity-and-mellin-gauge.md | 11145 | 5dd191f630c4fa615274d96d767d939d0332e6e8c56c4f1c47793ee961f47157 |
| reviews/2026-10-20/grh-dual-pairs/hilberdink-lapidus-primary-source-audit.md | 6322 | e580fea89efb0ff62ee9718059f856a53d5ee691160d076d72d6f45b08e4302d |
| reviews/2026-10-20/grh-dual-pairs/paired-duality-polarization-and-purity.md | 15672 | 6c779f701469caf1ad50c10fd565747abe74ccc44379fa6fca969f37800c2e23 |
| reviews/2026-10-20/grh-dual-pairs/positive-mellin-gauge-obstruction.md | 6000 | b6a93d67aab25ec24d3e9152c1da82f004bb170e86ef781a8a5149b3a5025f37 |
| reviews/2026-10-20/grh-dual-pairs/positive-shifted-beurling-pairs-and-weight-test.md | 5594 | 8e343b13d5739e26524a41bac02456946821ef65719a16fa062f096833b5fe52 |
