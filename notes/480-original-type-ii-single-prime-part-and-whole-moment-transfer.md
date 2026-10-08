# 480. 原 Type II 一次素因子部分与完整增长矩的传递

2026-10-08。基线 main 0cb98a7de5c92c949efbe9cfb3012d7716194e0c。
继续原路线，保留479的全部参数和实际系数。
新增小一次素因子部分的完整 \(7/10\) 四矩付款；
另在476的引用输入下，将原 scalar 与新余项的完整第四矩作带明确误差幂的传递。
利用同一对子族截断的一致估计，进一步把截断扩到 \(X^{5/96}\)，
不增加479的合成误差幂。
这些归约均不降低已有 whole 增长幂或无零边界。

## 1. 原系数的自然分解

保持 \(X=T/(2\pi)\)、\(J_T=[T/4,4T]\)、\(\ell=\log X\)、
\(U=V=\lfloor X^{1/8}\rfloor\)、\(M_0=\lfloor X^{1/4}\rfloor\)、
\(Y=X^{5/6}\) 和原归一化 \(a_\ell\ell\)。
记479的余项为 \(R_0\)：\(m>M_0\) 为 genuine prime，\(k>V\) 非平方丰满，
同一 \(Y<mk\le X\) 和系数 \(-\Lambda(m)b_V(k)/\sqrt{mk}\)。

对整数 \(k\ge1\)，令
\[
 s(k)=\prod_{v_p(k)=1}p,\qquad t(k)=k/s(k).
\]
这准确给唯一的互素分解：\(s\) 平方自由，\(t\) 平方丰满；
非平方丰满条件等价于 \(s(k)\ge2\)。
这里 \(s\) 取指数恰为一的素因子，不能换为按奇偶指数定义的 squarefree kernel。

原 \(b_V(k)=\sum_{d\mid k,d\le V}\mu(d)\) 若 \(\operatorname{rad}(k)\le V\) 就精确为零。
非零系数故满足
\[
 s\operatorname{rad}(t)>V,\qquad k=st>V^2/s.
\]
置 \(S=\lfloor X^{1/20}\rfloor\)，令 \(D_S\) 为 \(R_0\) 中
\(2\le s(k)\le S\) 的完整子族，\(R_1\) 为 \(s(k)>S\) 的完整余项。
准确有 \(R_0=D_S+R_1\)，没有重复479的 \(s=1\) 付款。

## 2. 全部端点和子族四矩

每个 dyadic \(K<k\le2K\) 中，该子族项数至多
\[
 \sum_{s\le S}O(\sqrt{K/s})\ll\sqrt{KS},
\]
所以原外加权 \(L^1\) 至多 \(X^\varepsilon\sqrt S\)。
所有非零项从 \(k>V^2/S\) 开始，真实 dyads 取
\(K=2^j(V^2/S)\)，\(j\ge0\)。固定 \(k\) 后，
原 \(m\) 区间仍是 \((\max(M,M_0,Y/k),\min(2M,X/k)]\)，
使用479已经证明的实际 \(q=\Lambda1_{\rm prime}\) 最大 prefix 四矩
\(X^\varepsilon(1+M^2/X)\)。

非空 dyadic pair 有 \(MK<X\)，且 \(K\ge V^2/S\)，故 \(M<XS/V^2\)。
完整原子族因此满足
\[
 \boxed{\mathcal M_{D_S}\ll_{\phi,\varepsilon}
 X^\varepsilon(S^2+XS^4/V^4)
 \ll_{\phi,\varepsilon}X^{7/10+\varepsilon}.}
\]
这里 \(\mathcal M_F=T^{-1}\int_{J_T}|F(t)|^4dt\)。
证明包括全部 aspect ratios、原 Möbius 系数、两个 sharp endpoints、
正高度窗、有限 dyads、floor 和先固定 \(\varepsilon\) 的损失分配。
确定性计数估计没有调用零自由输入。

完整证明见
[研究源](../reviews/2026-10-08/hybrid-original-type-ii-small-single-prime-part-fourth-research-radial.md)，
canonical LF SHA256
f0b740a85b09f70b68653bf3ec06288150876f1f761920ffb1107620fbf44580；
[不同作者审查](../reviews/2026-10-08/hybrid-original-type-ii-small-single-prime-part-fourth-review-checkpoint-audit.md)
单独核对该无限渐近证明。
\[
 17/24-7/10=1/120,\qquad 17/96-7/40=1/480.
\]
先合成误差函数再用一次三角，仍有
\[
 \|P_H-R_1\|_{4,T}\ll X^{17/96+\varepsilon},
 \quad \mathcal M_T\le8\mathcal M_{R_1}+O(X^{17/24+\varepsilon}),
 \quad \mathcal M_{R_1}\le8\mathcal M_T+O(X^{17/24+\varepsilon}).
\]

## 3. 使用完整增长上界后，第四矩可以作定量 additive 传递

这一节明确额外使用[476](476-original-fourth-growth-five-sevenths-with-ivic-density.md)
在原 \([R_{7/8}]\) 下给出的 \(\mathcal M_{P_H}\ll X^{B+\varepsilon}\)，\(B=5/7\)。
它不由第2节单独推出，也不把上面的通用三角等同为 additive 关系。

一般地，若 \(\|F-G\|_{4,T}\ll X^{c/4+\varepsilon}\)、
\(\mathcal M_F\ll X^{B+\varepsilon}\) 且 \(c<B\)，
Minkowski 先给 \(\mathcal M_G\ll X^{B+\varepsilon}\)。
再用逐点
\[
 \bigl||F|^4-|G|^4\bigr|
 \le4\,\bigl||F|-|G|\bigr|\,\max(|F|,|G|)^3
 \le4|F-G|(|F|+|G|)^3
\]
及 Hölder，重新分配固定损失，得到完整窗口的
\[
 |\mathcal M_F-\mathcal M_G|
 \ll X^{(3B+c)/4+\varepsilon}.
\]
先证明两个完整范数的上界后才使用此式；没有忽略未知余项范数。

476给 \(P_H\) 的完整增长界；479及第2节的误差范数再由 Minkowski
分别给 \(R_0,R_1\) 同一完整增长界。因此两个应用的范数前件都已支付。
对 \(F=P_H,G=R_1,c=17/24\)，以及 \(F=R_0,G=R_1,c=7/10\)，分别得到
\[
 \boxed{\mathcal M_{P_H}=\mathcal M_{R_1}
       +O_{\phi,\varepsilon}(X^{479/672+\varepsilon}),}
 \qquad
 \boxed{\mathcal M_{R_0}=\mathcal M_{R_1}
       +O_{\phi,\varepsilon}(X^{199/280+\varepsilon}).}
\]
准确幂余量为 \(1/672\)、\(1/280\)。
当最后 \(\varepsilon\) 小于相应余量时，两者在 \(X^{5/7}\) 尺度归一化后的差趋零。
误差本身仍增长；这些式子没有给出常数级四矩或负的四素数相关常数。
它们将已有完整增长预算的主要部分传给同一 \(R_1\)，而非只保存因子8的粗耦合。

### 3.1. 一般截断与不增加原误差的更大归约

研究源§5(18)对全部整数 \(2\le S\le V\) 一致给出
\(\mathcal M_{D_S}\ll X^\varepsilon(S^2+XS^4/V^4)\)，
其原项、归一化与两个乘积端点都不变。先固定
\(0<\delta<3/56\)，置
\[
 a_\delta=3/56-\delta,\quad
 S_\delta=\lfloor X^{a_\delta}\rfloor,\quad
 R_\delta=R_0-D_{S_\delta}.
\]
大 \(X\) 下 \(2\le S_\delta<V\)。由于
\(1/2+4a_\delta>2a_\delta\)，同一 floor 单侧界给
\[
 d_\delta=1/2+4a_\delta=5/7-4\delta,\qquad
 \mathcal M_{D_{S_\delta}}\ll_{\phi,\delta,\varepsilon}
 X^{d_\delta+\varepsilon}.
\]
这里 \(d_\delta<5/7\)，且476及479先给
\(\mathcal M_{R_0}\ll X^{5/7+\varepsilon}\)。
对同一完整窗口应用第3节的 Hölder 引理，并合成
\(P_H-R_\delta=(P_H-R_0)+D_{S_\delta}\)，得到
\[
 \boxed{\mathcal M_{R_0}=\mathcal M_{R_\delta}
 +O_{\phi,\delta,\varepsilon}(X^{5/7-\delta+\varepsilon}),}
\]
\[
 \boxed{\mathcal M_{P_H}=\mathcal M_{R_\delta}
 +O_{\phi,\delta,\varepsilon}
 (X^{5/7-\min(\delta,1/672)+\varepsilon}).}
\]
第二式使用的合成第四误差幂是
\(\max(17/24,5/7-4\delta)\)；
\(5/7-17/24=1/168\)，传递时再除以4。
所有 \(\delta\) 先固定，不对 \(\delta\to0\) 声称一致常数。
在增长尺度上得到趋零差还须取最后的 \(\varepsilon\) 小于显示余量。
这不是实际零点四阶常数或非零主项的渐近等价。

取 \(\delta=1/280\) 恢复第2–3节的 \(S=\lfloor X^{1/20}\rfloor\)
和 \(7/10\)、\(199/280\)。取 \(\delta=1/672\) 则得
\[
 S_\sharp=\lfloor X^{5/96}\rfloor,\quad
 R_\sharp=R_0-D_{S_\sharp},\quad
 \mathcal M_{D_{S_\sharp}}\ll X^{17/24+\varepsilon},
\]
\[
 \|P_H-R_\sharp\|_{4,T}\ll X^{17/96+\varepsilon},\qquad
 \mathcal M_{P_H}=\mathcal M_{R_\sharp}
 +O(X^{479/672+\varepsilon}).
\]
\(5/96-1/20=1/480\)，所以新截断逐渐比旧截断大一个
\(X^{1/480}\) 的因子；它仍是原 \(R_0\) 的精确整数子族分解。
在这里的估计 \(\max(2a,1/2+4a)\) 内，
\(a=5/96\) 是不增加479合成第四误差 \(17/24\) 的最大截断幂，
只陈述该估计族内的最优取参，不是原完整四矩问题的最优性。

## 4. 联合目标仍保留的前件

最终未付对象取 \(R_\sharp\)：genuine-prime \(m>M_0\)、\(k>V\)、
\(s(k)>S_\sharp\) 的
完整 signed mixed4，尤其 squarefree \(k\) 和 balanced prime×prime 仍存在。
全高度、小一次素因子部分已支付；不能把这个稀疏子族的上界扩成 whole 新指数。

原 MT 简单比例 \(p_{\rm dg}=0.67305811028197317865\ldots\) 及原引用输入下
\(\sigma_*\approx0.874957019420099\) 保持。
普通 zeta 的简单比例不代替 Hecke 全族深度前件或 \(\kappa\)，
本轮没有新的联合反馈或边界论文。

[精确检查器](../scripts/hybrid_original_single_prime_part_checkpoint.py)
与[检查点](../output/hybrid-original-single-prime-part-checkpoint.json)
核对有理成本、完整矩传递的新增指数、冻结依赖与最终审查绑定。
它们不枚举认证无限分析估计；根线程和不同作者全文核读证明。
