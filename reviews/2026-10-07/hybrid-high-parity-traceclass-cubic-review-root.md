# 原 high parity 的 trace-class cubic：root 独立全文审查

2026-10-07。限定 PASS：核范数界、原窗口/高度接口及条件门槛通过；
当前 7/8 输入没有因此支付绝对背景三次项，也没有新比例或新边界。

审查对象：
[完整研究稿](hybrid-high-parity-traceclass-cubic-research-compression.md)，
canonical UTF-8 LF SHA-256
bf54378214c05f68c6865aeaef7e87ae6a9cf9853cddfd5654174031871eabc9，
6382 bytes、189 lines。逐节完整读取，未改作者稿或既有冻结文档。

## 1. 原有限投影的核范数

原 interval basis 中，外侧 rows 与 finite columns 的 J 矩阵确实是两块
odd-filtered rectangular Hilbert matrix。对无滤波的块，
rank-one 积分核为 1/(r+k+1)；其 integrand 核范数是
sqrt(1-t^(2d))/(1-t²)。在 t≤1-1/d 与剩余区间分别积分，费用为
O(log(2d)) 与 O(1)。这也证明积分在 S1 收敛，不能仅以逐项积分
替代算子核范数付款。odd filter 用两次 unitary sign multiplication
的差表示，故两侧相加仍为 O(log(2d))。

S=E*JE 的谱在 [-1,1]；对 zero eigenvalue 指定 sgn(0)=+1
仍满足 |U-S|=1-|S|≤1-S²。已有
Tr(I-S²)=O(log d) 因而给 ||U-S||_1=O(log d)。
这些均是原 finite carrier 的计算，未换成连续频带投影。

## 2. 背景与 high 的准确恒等式

静态背景 D=E*M_hE 满足 M_h J=J M_h，因此稿中 (5)
来自准确的 P=I-Q 展开，两个交叉项符号正确。
由 ||QM_hE||op≤||h||∞、上节 S1 界及 U-S，可得
||[D,U]||_1=O(||h||∞ log d)。无需 h 为偶函数。

原 raw high shift 每步跨空间两个 half，故 JB_H+B_HJ=0。
稿中 (8) 的 SH+HS 两项同样由 P=I-Q 准确展开。
good-height 算子只用于这两个交叉项的 norm：原 B_H 的
anticommutation 从未错误迁移到 B_g。因此 sharp height 截断破坏
空间支持并不使恒等式失效。

## 3. C² packet 的两种尾费用

原 F=𝓕MφE 的 bad-height HS norm 为 O(T^-1)，所以右作用
B_bad E 的 HS norm为 O(m/T)。将其与 QJE 的 HS norm
O(sqrt(log d)) 配对，给 (9) 的 bad S1 项。

有限 compression 则两端同时在 bad band：
H-H_g=F*D_bad F，S1 norm 至多
m||1_bad F||_2²=O(m/T²)。这项给 finite ||H||op≤q_+；
不能把单侧 HS 尾与这个双侧 S1 尾混为同一个估计。
随后用 U-S 得 (10)，全高度 raw 对象已恢复。

## 4. 非交换三次展开及门槛

取 H'=-UHU、D'=UDU，由 finite cyclic trace 得
Tr D'H'^3=-Tr DH³。稿中三次 telescoping
H³-H'^3=rH²+H'rH+H'^2r 对不交换矩阵准确成立。
S1–op Hölder 给 (11)，没有使用未知 high fourth。

原 [R] fixed-gap sharp prefix 及 low/proper-power absolute subtraction
只在固定 a>max(θ,3/4) 给 band
q≪X^(a-1/2) polylog X。两费用分别具有幂
3a-5/2 和 2a-5/2；第二项在 a<1 小，第一项需 a<5/6。
因而条件 θ<5/6 确实足够，当前 θ=7/8 与既有接近它的引用边界
均不满足。作者没有用这个门槛反向证明新的无零输入。

## 5. 模型和实际研究范围

末节 spike 的 second 质量 q²/d 与 normalized HS parity defect
趋零，而 weighted cubic 可为 d0 q³/d，在 a>5/6 有正幂。
这个例子只检验明确列出的 second/parity/op 信息；没有声称实现
原素数 translations、454 全部 weighted mixed data 或实际 Gamma
有限矩阵。其 scope 限定正确。

本稿的绝对 static cubic bound不支付原 R_T=A-A0 的 cubic。
只凭 ||R_T||op=O(1/L) 与 paid second/op，费用至多 q_+/L，
仍可能增长；实际背景恢复须另行证明。已有相对 fourth 界仍合法。

结论：可保存为原路线的核范数工具与门槛诊断，不可作为当前
7/8 条件下的新零点比例、完整 fourth constant 或正式边界论文。
