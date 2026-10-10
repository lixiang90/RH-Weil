# 三次 κ 反馈界的精确接口障碍，以及整数化能否改善指数

2026-10-10。研究草稿；未改正式论文、公开形式化源或其他仓库。

本轮没有取得新的无零半平面。新增结果是一个可精确复核的参数障碍：
在当前 balanced 补偿几何、已有 low majorant 与完整 inverse/plain/
sixth-power count 包络不变的情况下，三次反馈界
`sigmaStar = 0.874957019420098946...` 已经是最优参数界。
另一个更一般的命题允许 M 与总槽长独立，但明确以前述三条仿射约束为前件。
两者均不是实际坏行或零点的存在性结论，也不是一切算术方法的最优性。

## 1. 已有结果的准确层级

已交付论文中的 eStar 是

\[
p(e)=657e^3-954e^2+21e+20
\]

在 `(1/6,167/1000)` 中的唯一根，
`sigmaStar=11/12-eStar/4`。其 written theorem 相对于明列输入包 R，
包括全 Hecke 7/8 bootstrap、实际相关/反射/矩估计及素数渐近。

只读检查 `RH-Zero-Free-Formalization/docs/proof-status.md` 确认：
`ArithmeticProbeObligation` 尚无已证明 inhabitant；完整 four-field Moments、
实际 reflected probe low 与全部 raw-high 组装仍有缺口。
通用 HighData 或最终 Mellin 蕴涵不能充当这些缺口已闭合的证据。

下述检查只用现有的显式有理 count 和指数表达式。
它没有补齐 R 的形式化，也没有证明新的 Hecke 非零定理。

## 2. 在真正的 count 矩形内移动临界点

令 `alpha=5/6`，`37/50 <= kappa <= 1`，固定 `x=1/2`，并写

\[
D=5/2-1/(3\kappa),\quad P=1-1/(6\kappa),\quad
J=(\alpha-\delta)D+\delta P,
\]
\[
R_\kappa(\delta)=1-\delta+
\frac{(\alpha-\delta)\delta P}{2J}.
\tag{1}
\]

这里 `D >= 455/222 > 2`、`P >= 86/111 > 0`，
且对 `1/50 <= delta <= 3/4`，`alpha-delta >= 1/12`，故 J 严格正。
该区间没有 floor witness 或零容量边界的偷换。

R 对 delta 严格下降。一个不需要导数的证明是设

\[
H(\delta)=\frac{(\alpha-\delta)P}{2J},\qquad
R=1-\delta+\delta H(\delta).
\]

对 `delta2 > delta1`，

\[
H(\delta_2)-H(\delta_1)=
-\frac{\alpha P^2(\delta_2-\delta_1)}{2J_1J_2}<0,
\tag{2}
\]

并有 `0 <= H(delta) <= P/(2D) < 1/3`。
代回 `R(delta2)-R(delta1)` 得严格负号，甚至不超过
`-2(delta2-delta1)/3`。

R 对 kappa 非减。精确有限差分为

\[
R_{k_2}(\delta)-R_{k_1}(\delta)
=\frac{3\delta(6\delta-5)^2(k_2-k_1)}
 {2Q_1Q_2},\quad
Q_i=54\delta k_i-6\delta-75k_i+10.
\tag{3}
\]

每个 `Q_i=-36 k_i J_i < 0`，所以分母为正。
这不把参考 kappa 误用成实际 prime-bound 前件。

在 admissible kappa 全区间，

\[
R_\kappa(3/8)-2/3\ge1961/157272>0,
\quad
R_\kappa(1/2)-2/3=-\frac{15\kappa-2}{3(48\kappa-7)}<0.
\]

因此有唯一 `delta_kappa in (3/8,1/2)` 使 `R=2/3`。
它总在真正的矩形内部，而且 `delta_kappa < 1/2 < 37/50 <= kappa`。
相应的 bin 实部在 `(11/16,3/4)` 内，远离 `51/100` floor。

无供给上限的 (1) 是既有 moment/count 方法最乐观的指数。
减少 available slots、要求 strict decrement 或仅允许整数 whole slots
不能把这个最乐观指数变得更小。若另外证明新的 count 不等式，
则属于改变接口，不在本障碍的结论内。

## 3. 当前 balanced 几何的完整参数障碍

保留 `M=1-e`、`h=(1+3e+b)/2`，当前 low majorant 至少含

\[
L_0=(1-e)/4-b/6,
\qquad C_b(B)=B-2/3-b/6.
\]

所以以边界 B 比较时，必有 `e >= 11/3-4B`。
在已经重放的 `1/6 <= e <= 1/5` 域内，`B<13/15` 已被 low 排除。
任何额外的 Gram/reflected-energy 分支只会增加这个 majorant。

在 `x=1/2`、`R=2/3`，已有完整高 endpoint 的 b 系数精确消失：

\[
E_B(h)=1/2+e/2-B+(1/2+3e/2)\delta.
\tag{4}
\]

假设 `13/15 <= B < sigmaStar`，令

\[
a=11/3-4B\in(eStar,1/5],\quad
k_0=2B-1=5/6-a/2,\quad
d_0=\frac{5-9a}{6+18a}.
\]

`d0 in [1/3,7/18]`，位于合法 delta 矩形内。
直接有理恒等式给

\[
R_{k_0}(d_0)-2/3
=\frac{p(a)}{2(3a+1)(153a^2-201a-20)}>0.
\tag{5}
\]

确实，p 在 `[1/6,1/5]` 严格下降：
`p'(a) <= -5454/25 < 0`，所以 `a>eStar` 时 p(a)<0；
另有 `153a²-201a-20 <= -2369/50 < 0`。
分母、分子同为负。

所有合法 actual 参数满足 `kappa >= max(37/50,2B-1)`。
(1) 可在 `k0>=11/15` 的更宽代数区间计算；这里仅把它作为
actual count 的乐观下限，并未调用范围外的 plain theorem。
由 (3)，`R_kappa(d0)>2/3`，由 (2)，临界 `delta_kappa>d0`。
(4) 对 e 严格增加，而在 `e=a,delta=d0` 时恰为零。
因此在真正的临界点，`E_B(h)>0`，不存在全矩形的非正证书。

这包括改变 b、重新选 total prime length、把实际 kappa 提高、
任意精确 whole-slot 选择，且不只证明根的一个数值邻域。
它仅排除这里定义的参数证书。若探测器把实际可出现的幅度/见证
限制到更小集合，或证明新的 low/count saving，本障碍可被绕开。

## 4. 显式三约束下，允许 M 与 e 独立的对偶障碍

为与 [Liu v1 §25](https://arxiv.org/html/2610.12234v1#S25) 作精确比较，
再研究一个前件显式的仿射问题。该文证明固定 kappa>=3/4 的三约束障碍；
以下把临界 delta 随真实 kappa 移动，所得固定点为我们的三次根。
这里不宣称全部 actual source 参数已经被证明满足三约束。

对任意实数 M、e，假设比较边界 B 满足

\[
 B\ge L_0:=5/6+M/12-e/6,
\quad B\ge L_K:=1/3+7M/12+e/3,
\]
\[
B\ge H_\delta:=1+\delta-(1+\delta)M/2+\delta e,
\quad \delta=\delta_\kappa,
\quad 37/50\le\kappa\le1,
\quad \kappa\ge2B-1.
\tag{6}
\]

前两项来自 general reflected majorant 的 `0`、`M+e-1`
两分支和 Gram 的 `b/12` 项；最后一项是 `h>0` 时在
`R=2/3,x=1/2,d=h` 的完整高表达式。若研究实际 general geometry，
仍须另外验证 majorant、完整 high estimate 及所有算术准入。

**命题（纯代数）。** (6) 蕴含 `B>=sigmaStar`，与 M、e、b 无关。

证明：取正权重

\[
(w_0,w_K,w_H)=\frac{(4+18\delta,2,3)}{9+18\delta}.
\]

它们和为 1，精确消去 M、e，故

\[
B\ge G(\delta):=\frac{18\delta+7}{18\delta+9}.
\tag{7}
\]

G 严格增加，`G'(delta)=36/(18delta+9)²`。
由 `delta>3/8`，(7) 先强制 `B>55/63>87/100`。
若 `B<sigmaStar`，则
`a=11/3-4B in (eStar,14/75)`；(5) 完全落在已核对的符号域。
仍有 `delta_kappa>d0`，且直接恒等式 `G(d0)=B`，于是
`B>=G(delta_kappa)>G(d0)=B`，矛盾。
该论证覆盖任意实数 B、M、e，不依赖 finite grid。

在 `B=sigmaStar`、`kappa=2sigmaStar-1`、`M=1-eStar`，
三项同时等于 B；现有正式论文另有完整连续证书与 strict side margins。
因此它既是三约束的准确下界，也是该 reduced model 可达到的界。
关于 actual source 的整个参数系统，本报告只登记“前件为三约束的
最优性”，不沿用“整个系统最优”这一未完全证明的更广表述。

## 5. 精确整数化为什么不给固定指数节省

1. **固定 K 的 whole slots。** 所允许的 subset 总长是连续容量集合的子集。
   在均一幅度 `g_i=delta/2` 这个允许的标签上，spike savings 对所选
   总长单调增加。`floor(capacity/slot_length)` 最多达到连续容量；
   没有在连续最乐观包络以下的新 count 指数。不得把 fractional slot
   免费填满或在 prime factors 里重复同一 support。
2. **dyadic witness 长度。** r、m 的格距是 `O(1/log U)`。
   更精确地定位 crossing 改变光滑指数至多同阶，
   `U^(O(1/log U))=O(1)`；切点处可能更小。单独的格点定位不能给
   `U^(-chi)` 的固定 chi>0。实际 saturation 可能受到额外约束，
   但要前向证明它，不能仅由 dyadic 格点推断。
3. **整数行数。** floor/ceil 只改变常数级数量。R≈2/3 的行数 upper
   没有借此变成 `U^(2/3-chi)`。任何实际 family 的稀疏性仍需算术证明。
4. **有限 compensation subsets。** K 在 Z 之前固定，精确 binomial
   multiplicities 是常数；prime asymptotic 的 log factors 是 subpower。
   empty subset 的 exponent 未因此减少。若令 K 随 Z 增长，则原 uniform
   coefficient/profile/height 合同不自动适用，须另付定量 uniformity。

这些排除的是“保持既有合同，仅做精确舍入”的固定指数收益，
不是整数结构或短见证联合相关性的普遍不可能性。

## 6. 真正可能改变下一边界的输入

临界 `deltaStar≈0.388583354266`，相应 bin 实部约 0.694291677133，
而非接近 Hecke family supremum 的 0.875。此前更强 raw zero-density
在这里仍大于 2/3，直接取 min 无效。
合法 mixed plain 的 count 是重复较大 plain witness 的平均，仍无固定收益。

需要的新输入应直接减少临界邻域的原 count 或原 low exponent：
同一 presentation 与原物理 Qi 上的 long-inverse / short-plain covariance
saving，或对真正原 reflected probe 的 signed saving。
已定位的 mixed 对象为
`sum_core |M_long|² |S_short|⁴ |Q_selected|²`；
新增估计必须保留不同实际 Fourier heights、natural zero masks、
原 moving radicals、一次 Qi 及目标前选择的有限高度阶。
没有在本报告把这些尚未证明的估计标成成果。

## 7. 下一具体数值目标的必要预算

把 `Btarget=17499/20000=0.87495` 作为尚未取得的研究目标。
取实际矩形内的有理检验点
`delta=19429/50000=0.38858`、`x=1/2`，最乐观的
`kappa=2Btarget-1=7499/10000`。精确有

\[
 R_\kappa(\delta)-2/3=
 \frac{1875081893}{615723531225000}>0,
\quad
G(\delta)-Btarget=\frac{52361}{7997220000}>0.
\]

若保持原 low 两项，新的实际 count 在这个标签上减少 chi，
完整高 endpoint 相应少 `h*chi`。正权对偶强制

\[
\chi\ge R_\kappa(\delta)-2/3+
\frac{G(\delta)-Btarget}{w_Hh}.
\tag{8}
\]

在当前 `h<1` 的几何中，右侧严格大于

\[
\frac{1875081893}{615723531225000}
+\frac{52361}{1500000000}
=0.0000379526642292785\ldots.
\tag{9}
\]

这只是需要寻找的 count 指数节省，不是已经证明的节省；
实际 h 约 0.811 时必要费用更大，而且临界邻域以外与全部物理侧条件
仍须完整支付。若另有真实 low 费用减少 mu0、muK，则对应必要预算是
`w0*mu0+wK*muK+wH*h*(chi-(R-2/3)) >= G-Btarget`。
因此下一步可以把新原算术估计与一个明确的精确目标比较，
而不再靠参数搜索重复生成无法越过界的数值。

## 8. 重放与范围

交付检查器 [kappa_feedback_interface_barrier.py](../../scripts/kappa_feedback_interface_barrier.py) 默认 `--check` 只读，
只用 Python 标准库实现稀疏有理多项式与交叉相乘的精确恒等式检查，
不用浮点、随机代入或 CAS。38 项包括根的有理隔离、显示符号、
输入文件 raw hashes 与 mixed sharpness 所用 long inverse 指数身份。
只有显式传入 `--output PATH` 才保存 JSON。
先前的 `feedback_interface_audit.py`/SymPy 输出只保留为 scratch 探索。
所有连续符号论证在正文给出，未从样本推断全域。
它不编译 Lean、不认证 R、不构造 ArithmeticProbeObligation、
不推导实际素数行的新矩估计，也不宣称新无零区域。

运行：`python scripts/kappa_feedback_interface_barrier.py --check`（从仓库根目录）。
另一个完全自包含的有限族论证在 `mixed-budget-sharpness.md`；
其中 rLong 是以 U 计的长逆列长度，绝非物理总槽长 e。
