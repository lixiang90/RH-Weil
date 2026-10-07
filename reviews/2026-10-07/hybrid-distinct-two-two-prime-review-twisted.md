# distinct 22：另一作者的完整独立审查

2026-10-07。被审作者 `mixed_path_check`；审查作者 `twisted_research`。
**限定 PASS，无数学阻断。**结论限于真实物理同号块全异 `o(N)`、
其余已显示的粗界和实际有限投影的准确余额。没有净 actual `O(N)`、
完整四阶常数或新比例结论。

## 1. 绑定与审查方法

被审稿：[hybrid-distinct-two-two-prime-sector-research.md](hybrid-distinct-two-two-prime-sector-research.md)，
canonical LF SHA256
`daca79cd62b61b7bd82a3b4fdf5a1a956ac0f2a1f44f7e63c0ff3f3b912cfc0d`，
18946 UTF-8 bytes，585 行。规范化仅替换 CRLF/lone CR 为 LF，不 trim。

独立重算了 (7)–(47)；先完成下面的原对象、能量、alias 和投影核验，
再读 [radial 独审](hybrid-distinct-two-two-prime-review-radial.md)，未以其
结论代替推导。同步读取冻结 [high 输入](hybrid-high-prime-four-word-response-research.md)
及 [mixed repeated 输入](hybrid-low-high-mixed-four-word-research.md)，
其 SHA 分别为 `988f8669a771e5b913bbc546590ceac540fc1391838e948563e4b4578f8ff666`
和 `71f62b2dd931cfda012e7dad9c4efcfece63f5cf1bb8ff5b466d3e2ac1ae89f9`。

外部原文再次浏览：[AF v2 §2](https://arxiv.org/html/2608.13637v2#S2) 的
固定 finite frame 与 [MV Theorem 2](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)
的局部间距 Hilbert 输入。其余用标准 Chebyshev/Mertens 上界；没有
调用新零自由区域或素数 correlation。保留 `d=floor(XL)`、原 carrier、
zero extension 和固定 C² taper，只使用 `d/N(T,2T)->1`。

## 2. 正量与两步 physical 表示

Hermitian H,L 的六种 high/low 位置选择准确给

\[
 A_{22}=\|C_HC_L\|_2^2,\quad
 M_{22}=6A_{22}-\|[C_H,C_L]\|_2^2,\quad
 2A_{22}\le M_{22}\le6A_{22}.
\]

因此 signed commutator 不能单独掩盖远大于 d 的 product norm。
减去 repeated union 后的下界是 signed 下界，不是上界付款。

两步 multiplier 的准确 feature 是
`phi(u) phi(u+sigma log p)^2 phi(u+sigma log p+eta log q)`；
两负号抵消。同号 span 是 `log(pq)`，非空项 `pq<X`；异号 span
是 `log p`。正 high 首步的输出 `u<0`、负首步 `u>0`，所以它们
在 physical product 中正交，经 P 后没有这个免费结论。
报告 (14) 的 HS 内积线性于首因子，与 `K_d(s)` 的相位一致。

## 3. 同号 unique product 与 all-distinct

因为 high/low 范围不交，`n=pq<=X` 唯一分解，且 log n 跨度小于
L/2。局部间距 `delta_n>=1/(2n)`。逐 q 的 Chebyshev 上界给

\[
 E_+(Y)\ll YL^{-3}\log^2(2Y/Z),\quad
 E_+(X)\ll X/L,\quad A_+(X)\ll\sqrt X/L.
\]

normalizer 确为 `a_L^4 L^4`；低于 2Z 时集合为空。
在固定 u 上使用 features `c_n f_n(u)`，拆开真实 finite sine 的
两个 endpoint phases。Hilbert 主项 `(L/d)E_+(X)` 加 csc remainder
`A_+(X)^2/d` 为 `O(1/L)`。因此 (18) 是准确 physical norm 付款。

从总非对角和中扣除 fixed-p 与 fixed-q 子族也合法：其 cutoff
分别为 `q<=min(Z,X/p)`、`p<=X/q`，与另一个变动标签无关。
两种 single-prime weighted energies 为 `O(Z/L)` 与 `O(X/L)`，
再按重复标签的 `sum b_p^2` 或 `sum b_q^2=O(1)` 聚合。
在非对角部分两子族无共同 diagonal。因此 (19) 及镜像为全异
physical `o(d)`，尚不是 actual four-word 的结论。

## 4. 异号 determinant：spacing 与真实 alias

`log(p/q)` 互异。若两频率差小于 1/2，交叉整数最大者小于两倍
`pq'`，整数 determinant 非零遂给 `delta_(p,q)>=1/(2pZ)`；
较远分支直接满足同界。真实整数长度是 XZ，不是 X。

频率跨度接近 L，报告保留了 csc remainder 在端点的奇性。
共同支撑长至多 `L-max(log p,log p')`，而频率差绝对值不超过
`max(log p,log p')`，故积分后的 overlap 抵消 `1/(L-|s|)`。
这只用于 remainder；Hilbert 主项先在完整频率集上计算，没有对
moving pair cut 免费套 Hilbert。

主项 energy 准确为

\[
 Z\sum_p p b_p^2\frac{L-\log p}{L}\sum_q b_q^2
 \ll XZ/L^2.
\]

层积分 `sum(log p)^2(L-log p)<<XL` 支付最后一步。乘 L/d 得
`O(Z/L^2)`，alias remainder 是 `O(Z/L^5)`，diagonal 为 O(1)。
因此 (25) 正确，但 normalized 上界仍增长。fixed-label 非对角
子族按 single-prime Hilbert 扣除，(27) 的 real signed Delta_X 与
其 `O(1+Z/L^2)` 范围均准确。

## 5. triple-composite/prime cross

固定 q' 后使用**单侧** `m=nq'<=2X`，因 q'>=2 不扩大 n<=X。
两个集合为 composite m 与 genuine high prime p'，无碰撞；都落
在 `(Z,2X]`，log span最多 `L/2+log2`。features 分别只依赖各自
变动指标，weighted bilinear Hilbert 准入成立。

\[
 E_m=q'E_+(2X/q')\ll XL^{-3}\log^2(4Z/q'),\qquad
 E_{p'}\ll X/L.
\]

normalized 主项为 `O(log(4Z/q')/L^2)`。再乘 b_q' 并用
`sum b_q' log(4Z/q')<<sqrt Z/L`，得 `O(sqrt Z/L^3)`；
csc remainder 是 `O(L^-3)`。这里逐 q' 费用尚未消去。

far `m>2X` 的位移大于 log 2；实际非空 feature 共同 span>=|S|，
所以原 finite kernel 与 overlap 有 `O(1/X)`，包含 S 接近 L 的
alias。真实三边 l1 mass `O(X sqrt Z/L^3)`，没有遗漏 far。

repeated p=p' 频率为 log(qq')>=log 4，按同一 overlap 得 o(1)。
repeated q=q' 的 near composite pq² 能量为 O(X/L)，按 b_q²
聚合得 O(1/L)，far 也为 o(1)。因此 (34) 保持准确 all-distinct
范围。把所有 q' 合并而删除 prime-side 的 q' feature 依赖不合法；
报告没有这样做。

## 6. physical diagonal 与实际有限 P

diagonal net frequency 为零，全实线积分可作 `v=u+log p` 的
普通平移；结合偶窗，准确给 `2(F_++F_-)=D_HL,L`。这不是一般
带 P trace 的循环交换。continuous middle 权重是 psi²，故
一般 F_+ 不等于 repeated four-corner J。
flat 的 `1/640,1/96,23/960` 与 (37) 相容。

报告的 `V=P B_H B_LP`、`Ecal=P B_HQ B_LP`、
`Lcal=Q B_H B_LP` 满足

\[
 P B_HP B_LP=V-Ecal,\quad
 \|B_HB_LP\|_2^2=\|V\|_2^2+\|Lcal\|_2^2.
\]

这直接推出 (42) 的所有符号。Lcal 须插入 P+Q，得到 (44) 的
两项；其 HS norm 和 Ecal 都仅有 `O(sqrt(XZ ell_0)/L^2)`。
平方除 d 不趋零，cross term也超出 sharp 量级。方向性 +/- 的
同样估计来自冻结输入的**逐 shift** Fourier crossing 证明，不能
仅由完整 B_H/B_L 的 norm 推断。故 (46) 也准确。

`pq>X` 的 physical 同号块为空，actual 中间 P 却可通过 crossing
给非零 product。报告保留了它的 XZ 长度与 alias，未把 (19) 免费
搬到 actual sector。

将这些等式、commutator 和 repeated budget 代入，(47) 的系数为
`2D-8J,12Delta,24ReGamma,-||Kcal||²,-6||Lcal||²,
-12Re<V,Ecal>,+6||Ecal||²`，全部一致。flat `17/480` 只是已知
余额项，不是 distinct 主项。粗界 `M22<<XZ/L` 确实由 physical
norm 与较小 log-factor corrections 得到，其 normalized 增长
`sqrt X/L²` 没有被写成净 saving。

## 7. 验收范围

此稿把 actual distinct 22 归约到同一有限对象的 Delta_X、Gamma_X、
Ecal/Lcal 和 commutator signed 合并，保留原采样、carrier、全
physical Hilbert space及全部 Fourier tails。尚未付的是这些对象的
joint upper budget，不是再补一个重复标签正项。

作者的19个有限模型只作代数 sanity evidence；本次未把它们登记为
分析证明，也未新增同类脚本。结论来自上述逐式解析重算。
**绑定版本完整限定 PASS；actual distinct 22、全四矩和比例仍开。**
