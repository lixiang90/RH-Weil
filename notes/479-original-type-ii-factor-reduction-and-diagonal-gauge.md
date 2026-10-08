# 479. 原 Type II 因子归约与同一 MT 预算的微小改进

2026-10-08。基线 main 5d508871ac3f087319e49c3b444187eaa66a7d30。
按用户要求继续原路线，换域暂缓。

本轮的主要结果是对原 Vaughan Type II 的完整因子子族给出实际四矩估计，
把尚未支付的项收缩到大 genuine-prime \(m\) 与非平方丰满 \(k\)。
同时，原 MT 的六邻域对偶增加一个负常数对角，得到很小的实际比例提升。
完整四矩增长幂和无零边界保持原值；两项成果没有构成新的联合解析桥。

## 1. 原对象与不重叠归约

保留 \(X=T/(2\pi)\)、\(\ell=\log X\)、\(J_T=[T/4,4T]\)、
\(U=V=\lfloor X^{1/8}\rfloor\)、\(Y=X^{5/6}\)，以及原归一化 \(a_\ell\ell\)。
原对象为
\[
 C_4(t)=-\frac1{a_\ell\ell}
 \sum_{\substack{m>U,\ k>V\\Y<mk\le X}}
 \frac{\Lambda(m)b_V(k)}{\sqrt{mk}}(mk)^{it},\qquad
 b_V(k)=\sum_{\substack{d\mid k\\d\le V}}\mu(d).
\]
\(\mathcal M_F=T^{-1}\int_{J_T}|F(t)|^4dt\)。
置 \(M_0=\lfloor X^{1/4}\rfloor\)，按下列顺序作精确有限分区。

| 部分 | 原因子范围；共同保留 \(Y<mk\le X\) | 已付四矩 |
|---|---|---|
| \(S\) | \(U<m\le M_0\)，全部 \(k>V\) | \(X^{17/24+\varepsilon}\) |
| \(P_{\rm pp}\) | \(m>M_0\) 为 proper prime power，全部 \(k>V\) | \(X^{1/2+\varepsilon}\) |
| \(P_{\rm sf}\) | \(m>M_0\) 为 genuine prime，\(k>V\) 平方丰满 | \(X^{1/2+\varepsilon}\) |
| \(R\) | \(m>M_0\) 为 genuine prime，\(k>V\) 非平方丰满 | 尚未改善 |

平方丰满指每个素因子的指数至少为2；proper prime power 为 \(p^j,\ j\ge2\)。
因为 \(\Lambda\) 仅在 prime powers 上非零，准确有 \(C_4=S+P_{\rm pp}+P_{\rm sf}+R\)。
这里没有从带符号全函数的范数推出任意子集范数；每个子族都单独估计。

完整证明、sharp endpoints、实际系数与全部量词见
[因子证明源](../reviews/2026-10-08/hybrid-original-type-ii-short-lambda-factor-fourth-research-radial.md)，
canonical LF SHA256
b39876e0b9d91a06de57d1069cf6adac676252bd1fe737186bb065716015abb0。
不同作者的完整审查见
[twisted](../reviews/2026-10-08/hybrid-original-type-ii-short-lambda-factor-fourth-review-twisted.md)。

## 2. 各子族的实际估计如何闭合

对 \(1\le A\le CX\)、原全部 \(t\in J_T\) 和任意 sharp 子区间
\(I\subset[A,2A]\)，一次真实差分和二阶导数界给
\[
 \left|\sum_{n\in I}n^{it}\right|\ll T^{1/6}A^{1/2}.
\]
在 \(A\le T^{1/3}\) 用项数；在 \(T^{1/3}<A<T^{2/3}\)
取 \(H\asymp A/T^{1/3}\)，差分相位满足
\(|f_h''|\asymp hT/A^3\)；在 \(A\ge T^{2/3}\) 用二阶导数界。
partial summation 因而统一支付实际无权内和
\(\sum n^{-1/2}(\log n)^j n^{it}\ll T^{1/6}\log^{j+1}(2X)\)，\(j=0,1\)。
经典引理为[Montgomery–Vaughan 原书](https://personal.science.psu.edu/rcv4/Vol2/Vol2.pdf)
Theorem 16.7 与 Lemma 16.8；证明源对本次相位和全部端点逐式推导。

展开原 \(b_V\) 后，\(S\) 的真实内区间为
\((Y/(md),X/(md)]\)。其 sup 至多
\(X^{1/6}\sqrt{M_0V}\log^C X=X^{17/48}\log^C X\)。
同一子族的实际 \(n\) 系数为 \(O(\tau_3(n)/\sqrt n)\)，
长度至多 \(X\)，二矩为 \(X^\varepsilon\)；
以 sup 平方乘二矩，得到 \(17/24\)。
同一估计把原 Type I 的四矩强化至 \(7/12\)。
冻结 \(Y\) 下低段仍为 \(2/3\)。

稀疏子族使用真实最大 prefix 四矩
\[
 \frac1T\int_{J_T}\max_{A\le u\le2A}
 \left|\sum_{A<n\le u}\frac{q(n)}{\sqrt n}n^{it}\right|^4dt
 \ll X^\varepsilon(1+A^2/X),
\]
其中 \(q=\Lambda,\ \Lambda1_{\rm prime}\) 或 \(b_V\)。
binary blocks 平方后的 product 长度是 \(O(A^2)\)；
同层各块的系数平方能量合计保留 \(2^{-j}\)，可以对层求和。
移动的共同乘积截断通过两个 prefix 之差支付。

若 \(1<k\le V^2\) 平方丰满，则
\(\operatorname{rad}(k)\le\sqrt k\le V\)，所有非零 Möbius divisors 均已收入，
故 \(b_V(k)=\sum_{d\mid\operatorname{rad}(k)}\mu(d)=0\)。
非零平方丰满外因子因此满足 \(k>V^2\)；
其 dyadic 带权项数为 \(X^\varepsilon\)，内 \(m\) 长度至多 \(X/V^2\)，
支付 \(X^\varepsilon(1+X/V^4)\)，即 \(1/2\)。
对 large proper-prime-power \(m\)，dyadic \(\sum\Lambda(m)/\sqrt m\ll\log^2 X\)，
内 \(k\) 长度至多 \(X/M_0\)，同理支付 \(1/2\)。

合成误差函数后只用一次四次范数三角，原 genuine-prime \(P_H\) 满足
\[
 \|P_H-R\|_{4,T}\ll X^{17/96+\varepsilon},\qquad
 \mathcal M_T\le8\mathcal M_R+O(X^{17/24+\varepsilon}),\quad
 \mathcal M_R\le8\mathcal M_T+O(X^{17/24+\varepsilon}).
\]
这不是两第四矩的 additive 等同。\(5/7-17/24=1/168>0\)；
新付款仍高于原低段费用 \(2/3\)，其价值在于缩小真实剩余因子族。
[476](476-original-fourth-growth-five-sevenths-with-ivic-density.md) 的 whole
\(T^{5/7+\varepsilon}\) 保持。

## 3. 原 MT 对角调节的实际小幅提升

保持 [478](478-original-mt-six-neighbor-dual-and-whole-chain-proportion.md)
的全实轴核界和七点证书。有限谱对偶只需 \(B\preceq I\)，
允许取 \(B=-eI+uK\)，其中
\[
 e=\frac1{62500},\quad u=\frac{62501}{63750},\quad
 c=2u-u^2=\frac{4062502499}{4064062500}.
\]
保留对角损失 \(e^2n\)、正确端项 \(6c\tau\) 和固定 profile 误差
\(2(1+e)n\epsilon_\delta\)，得到
\[
 \alpha=c\frac{19}{5000}-e^2,\quad \eta=\frac c{500},\qquad
 p_{\rm dg}=\frac{C_0-\eta}{1-\alpha}
 =\frac{20320312500000C_0-40625024990}{20243124957721},
 \quad C_0=\frac32-\frac1{\sqrt2}\cot(1/\sqrt2).
\]
在原前缀渐近计数合同内，简单临界线零点比例至少
\(p_{\rm dg}=0.67305811028197317865\ldots\)，
不同零点比例至少 \((1+p_{\rm dg})/2\)。
新严格下端减去478旧严格上端为
\[
 \frac{38202658750375724709585783275561655495674769405}
 {223107690410244439578888423481057719096362234296731172864}>0.
\]
实际提升约 \(1.7123\times10^{-10}\)，不作最优性或世界纪录声明。
完整源和不同作者审查分别为
[对角调节证明](../reviews/2026-10-08/hybrid-mt-six-neighbor-diagonal-gauge-and-actual-counting-research-compression.md)
与[独立审查](../reviews/2026-10-08/hybrid-mt-six-neighbor-diagonal-gauge-and-actual-counting-review-twisted.md)。

## 4. 联合目标与复算范围

上述比例没有使用原 \(7/8\) 输入，不能代替 Hecke 全族的
\(\beta_*\le(1+\kappa)/2\) 前件或 whole 四矩常数。
下一算术目标明确为 \(R\) 的完整带符号 mixed4：
大 genuine-prime \(m\)、非平方丰满 \(k\)、真实 \(b_V\) 和共同乘积边界。
原引用输入下 \(\sigma_*\approx0.874957019420099\) 保持；本轮没有新边界论文。

[本轮检查器](../scripts/hybrid_original_type_ii_factor_checkpoint.py)
与[精确检查点](../output/hybrid-original-type-ii-factor-checkpoint.json)
核查成本、严格比例区间、冻结输入、最终审查绑定及链接。
它不认证无限解析估计，不重新执行已冻结的大核/七点覆盖。
根线程全文复核两份证明；不同作者全文复核分析细节，有限检查与数学审查分开记录。
