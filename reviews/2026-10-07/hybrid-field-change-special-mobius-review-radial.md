# 换域特殊 Möbius 报告的独立全文审查

2026-10-07。radial_review。结论：限定 PASS。独立完整读取被审153行报告，
并重新核对458的实际对象、459的双向恢复与误差、460的反例范围。
该结果是固定目标下第四幂子族的条件节省，以及全行问题的具体归约；
它没有证明 Gaussian 全 raw、marked/plain 合同或新的无零边界。

## 1. 最终证据对象与引用边界

被审
[报告](hybrid-field-change-special-mobius-next-research.md)
canonical LF SHA-256：
1afe4d0b2393f0c67997c2f83680f0e9ed46ae12e0f84f7b337e2a6e0fdb23db；
7711 bytes，153行。CRLF及 lone CR 均统一为 LF 后计算。
全文复读最终版；最终前件明确 subpower 控制及
\(1/2\le\theta_0<1\)。更强零自由线可统一用 \(\theta_0=1/2\)，
以保证所选 \(a>\theta_0\) 自动大于 \(1/2\)。
式 (3)–(8) 和同对象论证未改。

本次核对的冻结依赖为：

| 文件 | canonical LF SHA-256 |
| --- | --- |
| 457 | 75079970955602644a9290709f66e2be331ad6116d2a637ed8fc97fb0dde5791 |
| 458 | 3ee821601d6e1d5da38c8235586981b28d7ebee5a5f28691a98d869834dcc8ac |
| 459 | fe6046154965fb8e833e0a96adf0801f9aa4fd4b2ea8b27397748c79193477b6 |
| 460 | 9625c0d618854769de90edfb3ee3b8d8b89e1d3b2b83d676dffccb927e09d85f |

原 math September-30 build/paper.tex 的 canonical LF SHA-256 为
42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3。
直接重读其1531–1599行 logarithmic control，以及12343–12408行
原 raw fixed-scale / scale-sup 合同。底层零自由论文 [R] 未在本审查逐项重证；
对 Gaussian 新目标的普通 FE 也不能由原 Eisenstein target 名称自动替代。

## 2. 同一个固定列与第四幂行

报告 (1) 与458的 normalization一致：平方范数中的列能量为
\(O_W(1)\)，不是把 \(n^{-1/2}\) 改成另一组任意系数。
\(\eta\) 为同一个固定有限阶目标；可有另外固定的 norm imaginary
phase，原窗口、原高度和全部零延拓继续保留。

对 odd primary \(u=r^4\)，在 \((n,r)=1\) 时 quartic symbol 的
\(\epsilon=\pm1\) 次幂准确为1；不互素时仍为零。因此 (2) 是准确的
带 mask Möbius 和。没有扩大到所有 unit 或 lambda sectors；
这些 sectors 会产生新的固定列角色，不能默认具有原 \(\eta\) 的解析控制。
不同 primary \(r\) 的第四幂注入，且 \(Nr\le U^{1/4}\) 的数量为
\(O(U^{1/4})\)，没有单位或理想重复造成额外幂次。

## 3. 正线估计的必要前件与完整指数核算

[Z_eta] 中 fixed-gap reciprocal control 已按原来源明确写成 subpower 形式：
对每个固定 \(\delta>0,\varepsilon>0\)，在
\(\sigma\ge\theta_0+\delta\) 上，
\[
 |L(s,\eta^*)^{-1}|\ll_{\eta,\delta,\varepsilon}
 (1+|\Im s|)^\varepsilon .
\]
原来源1539–1542及1547–1551行正是这种任意小幂控制；
一般 polynomial height bound 本身不足以推出报告 (3) 的
\(U^\varepsilon\)。这是明确引用前件的含义，不是本审查新证明任意
Gaussian \(\eta\) 的零自由半平面。

若固定原 \(\eta=\chi\circ N\)，ordinary base-change factorization
\[
 L_{\mathbb Q(i)}(s,\chi\circ N)=L(s,\chi)L(s,\chi\chi_{-4})
\]
可以在 split、inert、ramified rational primes 逐 Euler 因子核对。
使用相同零延拓的 natural Dirichlet characters 时为准确恒等式；
改为 primitive representatives 时可能有有限 Euler 因子，其零只在
\(\Re s=0\)。因此既有 Dirichlet 全族 [R] 可以提供
\(\theta_0=7/8\) 的 fixed-gap 控制。这里不能为获取该性质而更换原目标。

自然 mask 删除的 \(r\)-Euler 因子在 \(\Re s=a>0\) 满足
\[
 \prod_{\pi\mid r}|1-\eta^*(\pi)(N\pi)^{-s}|^{-1}
 \ll_{a,\varepsilon}(Nr)^\varepsilon .
\]
固定坏素数以同样方式处理。把 Mellin contour 从绝对收敛线移到
固定 \(a>\theta_0\)，不跨 \(1/L\) 的 pole；principal \(s=1\) 反而是
zero。Mellin 变换仍是同一个平滑窗口的变换；原 norm phase只平移
reciprocal 的 height，不需微分 phase。先固定
\(|\omega|\le U^A\) 的 \(A\)，subpower 界与固定窗口的快速下降便给
\[
 |M_{r^4}(D')|\ll D'^{\,a-1/2}U^\varepsilon .
\]
非空小尺度有固定正下界；余下有限小尺度以常数支付。
由于最终前件明取 \(1/2\le\theta_0<1\)，所选 \(a>\theta_0\)
确实保证 \(a>1/2\)，对 \(0<D'\le D\)、\(D\ge1\) 取 supremum 得 (3)。
若原有更强的 \(\theta_0<1/2\) 控制，先改用 \(\theta_0=1/2\)
仍保留该零自由性及 fixed-gap bound；不会引用负幂 scale 单调性。

计数并平方给 (4)。若 \(U\ge D^{1+c}\)，则
\[
 U^{1/4}D^{2a-1}
 \le U^{1/4+(2a-1)/(1+c)}
 =U^{1-\chi},\qquad
 \chi=\frac34-\frac{2a-1}{1+c}.
\]
由 \(\theta_0\le7/8\) 和 \(a-\theta_0\le3c/16\)，
\(2a-1\le3/4+3c/8\)，所以
\(\chi\ge3c/[8(1+c)]>0\)。另一个上界
\(a-\theta_0\le(1-\theta_0)/2\) 保证 \(a<1\)；
所有间隙先固定后让尺度增长。这个 saving 只控制上述第四幂子族，
不能覆盖变化的 quartic primitive conductors。

## 4. 普通 FE、恢复 polynomial 与全行误差

报告 §3 保留459的同一个 natural/primitive inverse identity。
Gaussian finite-order普通 completion有一个 complex-place
\(\Gamma(s)\)，conductor 幂为 \(C^{1/2-s}\)；
它没有声称是 quartic Gauss/theta completion，更没有搬运任意 angular
profile 的新反射合同。Norm height只在同一 Mellin profile中平移，
不被改称新的 finite-order角色。

截断 \(Nh\le D^\vartheta\)、\(1/2<\vartheta<1\) 时，
finite restoration polynomial准确为
\(G_u(s)=\sum\psi_u^*(h)(Nh)^{-s}\)；
每个短尺度使用同一 profile、同一个 row rectangle及原长列 height。
这与459 (7)–(14) 的推导相符。可能的 multiple zeros、trivial zeros、
horizontal joins仍在 \(Z\) 内，不能用外部 tail order消去 joins。
普通 principal FE 的 meromorphic情形也合法：
functional-equation Gamma pole在0与 \(1/L(1-s)\) 的zero抵消，
不会新增一个本来没有的 reciprocal pole。

若列含 \(Nn^{i\omega}\)，写
\(f(y)=y^{-1/2+i\omega}W(y)\) 时实际和为
\(D^{i\omega}M(D;f)\)。报告明确保留该global factor；
恢复中 \(Nh\) 的 phase也由同一 \(f\) 准确产生。
不能给每个 \(h\) 另换短尺度 test，再声称保持原对象。

Gaussian rows数 \(O(U)\)，逐行的
\(D^{1/2-\vartheta+\varepsilon}U^\varepsilon\) 误差平方后求和
确实给 (7)。在 \(\vartheta=3/4\) 的 fixed large scale，
relative费用为 \(D^{-1/2+\varepsilon}\)，不是新的 cancellation。
对 scale supremum，固定小尺度以 \(O(U)\) 支付；大尺度误差因
\(1-2\vartheta<0\) 有统一 \(O(U^{1+\varepsilon})\) 的总平方能量。
Hilbert norm三角给 linear-budget 双向比较，无需把逐尺度大筛的
supremum移出 row sum。该比较不把 whole-sup 误差仍写成
fixed-scale 的 \(D^{-1/2}\) saving。

## 5. 单位项的真实基线与限定结论

固定非零 smooth \(W\) 支撑在 [1,2]，可取
\(y_0\in(1,2)\) 使 \(W(y_0)\ne0\)，令 \(D_0=1/y_0\le1\)。
在 \([D_0,2D_0]\subset[1/2,2]\) 内的 odd Gaussian ideals只有单位
理想1；norm2的 ramified \(\lambda\) ideal被 odd condition排除。
\(\mu(1)=\eta(1)=1\)，mask \((1,u)=1\)，故
\(M_u(D_0)=W(y_0)\) 对全部rows准确成立。
全部非零 Gaussian元素数 \(\asymp U\)，因此 whole row-scale sup
能量确有报告 (8) 的 \(\Omega_W(U)\) 基线。

该观察与第四幂子族的 saving不矛盾：第四幂rows只有
\(O(U^{1/4})\)，whole-small-scale baseline计的是全部实际rows。
若原test删除单位项或仅允许大尺度，这个基线不适用。
它也不是460 arbitrary-column fourth-power峰的实际 Möbius反例。

PASS 只验收已明定 [Z_eta] 下的第四幂子族节省、459同对象 primitive
联合能量归约及单位项 baseline。一般 \(\eta\) 的[Z_eta]、
变化 conductors 的 primitive residues/joins联合估计、Gaussian
近临界全 raw、once-prime slots及完整 marked/plain 递归仍未支付。
没有新的 \(\sigma\) 数值或零点比例登记。
