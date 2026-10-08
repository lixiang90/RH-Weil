# 原四全异近共振双非单位块：root 全文审查

2026-10-08。root 独立全文阅读并重推下列定稿；未修改研究源。
接受的范围是合法短载体的带符号平均中一个完整算术频块，
不包含逐起点、平均绝对值、canonical scalar whole 界或新比例。

## 1. 实读来源与绑定

canonical UTF-8 LF 只统一 CRLF/lone CR，不 trim 或改变 EOF。

| 全文实读文件 | 行数 | SHA256 |
|---|---:|---|
| [新完整源](hybrid-whole-fourth-double-nonunit-actual-research-whole.md) | 545 | 2d27661262a1e672a9bb93846de68a661e0d17d8f5e0444117ae6a8debac4215 |
| [原 far / carrier 来源](hybrid-whole-ratio-smooth-carrier-far-resonance-research-twisted.md) | 359 | 9b8c6064731f65eb4449a3e9da353077baa856a4cb27f93fd5063b6f6a578054 |
| [472，完整 P / ratio 桥](../../notes/472-original-short-carrier-fourth-compression-and-ratio-variance.md) | 194 | 9856885e932a892cf7c33ece82f430c2ec13004555eb52da2f1e8b1ec6bb2683 |
| [456，完整 repeated sector](../../notes/456-high-opposite-four-word-vanishing-and-repeated-limit.md) | 270 | 7de855634f93f9d92f6d0cbdd762f9894effaaf40f788b3e02de89f961eadb96 |
| [465，同素数中心](../../notes/465-centered-high-square-joint-fourth-budget.md) | 272 | a9290d2d847c2a3f7942b26353bd1582a68b391e481acc109c4ac18d3d750464 |
| [474，另一观察对象的一侧准入](../../notes/474-original-short-carrier-canonical-scalar-fourth-admission.md) | 121 | 37306c6d403f48c93d5d0f92782088225084e2e4b6b694cd89644a75fe39e99f |

新源依赖 480 的记号，不依赖其新 Type II 估计或矩传递结论。
root 最后核查时已提交基线为 `0161e73f7c4c9392dc8ea97a224c2119830981ac`。

## 2. actual 到 physical 的顺序与频块定义

472 支付的是整个 word 的 mean absolute P error。该结论不能任意
拆给四全异 near 的各 tuple。正确顺序为：先在完整 high word 上使用
这个桥，再减去已付的完整 repeated sector，最后分别移走 actual 和
physical 的整个 far union。475 的正密度被 box 密度的8倍支配，
所以前一误差仍为 o(1)，其直接 actual far 证明保留所有 internal P。

456 的 repeated 证明通过绝对几何核和 endpoint overlap，载体相位
可以统一移动在合法短窗内；465 的同素数中心也统一于这个窗口。
于是 physical 与 actual 的完整四全异 signed 平均相差 o(1)，
physical half-ratio 到 full high 的固定 factor2 保持。新频块定义在
这次完整桥之后，不是对原三个 internal P 逐 tuple 分块。

固定真实最大素数 q，原同一 u 的 profiles 正好按源(4)、(5)分离。
将分母最大的位置取共轭不会重选 u 或改变系数。p,r<q 使原 product
严格小于 q²，因此源(8)的 carry gate 保留后，模 q² 同余才等于原等式。
剩余 p=r 条件须用不同的 diagonal kernel 扣除。

## 3. 完成、归一化与非零加性频率

以 c=q² 的 unitary DFT 展开两 raw arrays，完整核的 prefactor 为 c⁻¹。
取 m=qμ,n=qν 后 Kloosterman lift 给 q 倍的模 q 核，两 DFT 各含 q⁻¹；
再用模 q 两次正交性，得到固定 a 的
q⁻¹ Σ A_p B_r 1_(pr≡a mod q)，即源(10)。继续完成位移 a，
前因子为 q⁻²，不能遗漏这两个 q。

q|a 时 raw 和双非单位块均严格为零，故仅在估计后者时统一添回
这些 a 合法。对于 unit a，x=y+qk 的 lift 因子是
Σ_k e_q(k(m−an y⁻²))；恰一个 dual frequency 为单位时严格为零。
这个消失结论不能套给 p=r 的另一个 diagonal kernel。

非零加性 n 的矩阵 e_q(npr) 是完整 Fourier 矩阵的置换，算子范数√q。
这是对子数组合法的范数界，未要求 prime 等差数列分布。
同一 near 权重先解调线性相位，余相位变差 O(XΔ²)=o(1)；
sharp gate 至多两个 jumps。整个 n 网格的 Fourier l¹ 费用为
O(AΔ+q log q)=O(q L^(5/2))，不需要短 dual cutoff。
含原外权重 b_qb_s 的完整求和为 O(√X L^(1/2))。

## 4. 零频与阶数随 X 增长的估计

连续零频不能仅依靠 fixed-order IBP。这里 Γ 是正号 Fourier
变换，χ 的逆变换支撑在正区间；正载体 θ 下，所有固定次数
u^j e^(iθu)Γ(s_Tu) 的全实轴积分严格为零。
七次 Taylor 多项式因此准确消去，八阶余项支付 AΔ⁸/s_T。
尾部以 z=s_Tu 改元，s_TΔ=2048πL²，显式 stretched exponential
得到 X⁻⁴ times polylog 的积分费用；这是真幂节省。

辅助 cutoff 的无限 uniform convolution 给固定 Gevrey2 常数 C。
复合 log 的 j 阶导数也可直接以第一类 Stirling 系数验证：
Σ_k c(j,k)y^k=y(y+1)…(y+j−1)≤(y+j)^j，
取 y=Cj²/Δ 并使用 x≈A，得到源(21)的 cutoff 部分。
Mellin monomial 的 rising product 至多 (θ+N)^r；Leibniz 合成后
bracket 是两个导数尺度之和，外面没有遗漏 N!。

在 A>4X 的完整内区，N 为超过20L的最小偶数，
bracket/(2π)≤1/2+o(1)+O(L^(−1/2))，最终统一≤3/4。
Euler–Maclaurin 的 compact-support 余项只含
2ζ(N)/(2π)^N ∫|f^(N)|；所有边界导数为零。
因为 (3/4)^(20L)=X^(−20 log(4/3))，20 log(4/3)>5，
乘以 O(X L^(5/2)) 的支撑长度仍为 O(X⁻⁴)。
同一结论不可套在 A≤4X 的 aliases 或 upper sharp gate 边界。

这两个完整边界族单列：A≤4X 强制 q≤4√X；
q−s≤4qΔ 每 q 只有 O(qΔ+1) 个整数候选。
源7.1、7.2的带原 b_qb_s q⁻² 权重计数分别不超过
O(L^(1/2))、O(L³)。其余族整个 bump 在 (1,q²) 内。
覆盖完整，未使用小素数间隔猜想。

## 5. graph 扣除、有限检查与结论

双频投影在 physical 变量是 residue average：每模 q residue
至多一个 raw p，所以取值为 A_(x mod q)/q。
diagonal kernel 因此恰为源(24)的 q⁻² unit-square-root sum。
每 a 至多两根，max b_p²≪X^(−1/2)；全部 q,s,a 的原权重费用为
O(X^(−1/2) polylog X)，包含 hard / smooth 迁移。

root 另外用直接模 q² unit lifts、unitary DFT 和所有 unit square
roots 进行14732项浮点核检查，q=5,7,11：nn 最大误差
3.35·10⁻¹⁶，diagonal 最大误差7.16·10⁻¹⁸；q=5,7 的完整
unit a / unit m / n=qν mixed 核最大误差5.94·10⁻¹⁵。
这些只核查有限归一化，不能认证上述无限解析界；未运行外部 Lean。

接受源(26)在其明确范围内的完整付款：
|D_nn|≪_(φ,ε) X^(1/2+ε)。它属于合法 χ-carrier 的 signed 平均，
不是平均绝对块、固定σ上界或 canonical J 上的 scalar 子块。
总 near 的 unit/unit 全宽块及 diagonal kernel 的其他频块仍在余额中。
same good point 仍须总 near 上界和概率分母，未获得新四阶常数、
零点比例、Hecke全族深度或无零边界。未发现所述局部付款的数学阻断。
