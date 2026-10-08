# 小一次素因子部分的完整四矩付款：不同作者全文逆审

2026-10-08。审查人：checkpoint_audit。结论：**限定 PASS**。

已全文实读被审新源329行，独立逆审唯一分解、原自然零域、全带计数、
真实 prime-prefix 接口、全部移动端点、floor 和 ε 分配。
479与旧最大prefix完整证明在本会话前轮已全文实读；本轮重新核其最终哈希一致。
另运行独立内存有理数和有限实际系数检查。没有修改源、旧文件、证书、Git 或论文。

## 1. 最终绑定与实际范围

canonical UTF-8 LF 只统一 CRLF 与孤立 CR；不 trim，不改变 EOF。

| 被审来源或冻结接口 | canonical LF SHA256 | 字节 / 行 |
|---|---|---:|
| [新完整自然子族证明](hybrid-original-type-ii-small-single-prime-part-fourth-research-radial.md) | f0b740a85b09f70b68653bf3ec06288150876f1f761920ffb1107620fbf44580 | 11658 / 329 |
| [479实际因子归约](../../notes/479-original-type-ii-factor-reduction-and-diagonal-gauge.md) | 6b6e15f8a3a83d62e1d472cbeaa86a894c9e01740ccd682fc79ec99c2ec5a559 | 7029 / 140 |
| [旧完整因子证明与最大prefix引理](hybrid-original-type-ii-short-lambda-factor-fourth-research-radial.md) | b39876e0b9d91a06de57d1069cf6adac676252bd1fe737186bb065716015abb0 | 21261 / 524 |

批准的是同一479剩余内 \(2\le s(k)\le\lfloor X^{1/20}\rfloor\) 的完整自然子族。
原 genuine-prime m、\(\Lambda(m)=\log m\)、signed \(b_V(k)\)、
正高度 \([T/4,4T]\)、normalizer 和两条 sharp product endpoints 均保持。
所用前件是已证明的有限系数均值接口；本次付款不依赖零自由条带。

## 2. 唯一分解与必要自然零域

逐素因子检查定义
\(s(k)=\prod_{v_p(k)=1}p\)、\(t(k)=k/s(k)\)。valuation1全放入s，
其余至少2的valuation全放入t。因此分解唯一，s squarefree、t squarefull，
\((s,t)=1\)，允许任一因子为1。反向任一互素的这种分解都逐valuation恢复
相同s；没有允许同一prime同时落入两个部分。
在原 \(k>V\ge2\) 下，non-squarefull准确等价于 \(s(k)\ge2\)。

对 \(k>1\)，若 \(\operatorname{rad}(k)\le V\)，所有非零μ-divisors
都是rad(k)的divisors且均≤V；故原完整有限和准确为0。
只使用必要条件 \(b_V(k)\ne0\Rightarrow\operatorname{rad}(k)>V\)，
没有把原系数替换为radical indicator，也没有使用其逆命题。
例如 \(V=4,k=50\) 的radical是10，而真实 \(b_4(50)=1-1=0\)，
这仍符合作者的单向使用。

互素性给 \(\operatorname{rad}(k)=s\operatorname{rad}(t)\)，
squarefull给 \(\operatorname{rad}(t)^2\mid t\)。所以非零项严格满足
\(\operatorname{rad}(t)>V/s\)、\(t>(V/s)^2\)、\(ks>V^2\)。
对 \(s\le S\)，必有 \(k>V^2/s\ge V^2/S=K_0\)。
这是去掉真实零项后得到的严格起点，既没有人为改mask，也没有重复旧s1子族。
原 \(m>M_0\) 的整数条件另给 \(k\le X/(M_0+1)\)，实际范围有限。

## 3. 全dyad计数和实际外权

squarefull整数唯一写成 \(t=a^2b^3\)，b squarefree；奇valuation≥3取一个b³，
偶valuation及剩余偶数部分放入a²。允许t1。
以 \(\sum_{b\ge1}b^{-3/2}\le3\) 得
\(\#\{Z<t\le2Z:t\text{ squarefull}\}\le3\sqrt{2Z}\)（\(Z\ge1/2\)）；
\(Z<1/2\) 时该正整数带为空。因而作者使用的统一 \(O(\sqrt Z)\) 正确，
包括K/s可能小于1的情况。

每个原k对应唯一(s,t)。为upper移除s的squarefree和互素限制后，
\[
\#\{K<k\le2K:2\le s(k)\le S\}
\le\sum_{2\le s\le S}\#\{K/s<t\le2K/s:t\text{ squarefull}\}
\ll\sqrt{KS}.
\]
使用 \(\sum_{s\le S}s^{-1/2}\le2\sqrt S\)，还可取统一显式upper
\(6\sqrt{2KS}\)。这是扩大标签对后的计数upper，未从signed范数删项。
全部原t和允许aspect ratios仍在子族中。

真实 \(|b_V(k)|\le\tau(k)\ll_\delta X^\delta\) 对V统一；
在 \(k\asymp K\) 上乘 \(k^{-1/2}\) 得
\(A_K\ll_\delta X^\delta\sqrt S\)。
原k上下条件、自然零项及额外乘积条件只减少此绝对权upper。
没有μ随机性、prime density或新的解析输入。

## 4. 最大prefix、移动两端与成本

旧证明§8(22)的前件是实际固定系数的subpower界，对
\(q(n)=\Lambda(n)1_{\rm prime}(n)\) 直接成立。
其binary-block证明用平方后真实长度4M²，留下 \(1+M^2/X\)，
同层能量 \(2^{-j}\) 和L4 Minkowski支付最大prefix。
这里直接对prime q使用该结论，没有从完整Λ多项式范数推出prime子集范数。

k带从真实实端点 \(K_0=V^2/S\) 起，m带从整数 \(M_0\) 起；
各带开左闭右，全部非零原项准确落入唯一带。
固定实际k后的m区间是
\((\max(M,M_0,Y/k),\min(2M,X/k)]\)。
先判空、再clamp到 \([M,2M]\) 的两个prefix之差，恢复同一个整数集合。
没有取整两条product endpoints，也没有用矩形代替斜cutoff。

外权upper与两prefix常数给
\[
\|D_{M,K}\|_{4,T}^4
\ll X^{\rho+4\delta}S^2(1+M^2/X).
\]
非空带有真实 \(m>M,k>K,mk\le X\)，故 \(MK<X\)。
\(K\ge V^2/S\) 因而给 \(M<XS/V^2\)，准确得到
\(S^2+XS^4/V^4\)。四次方的外权是S²，未漏计或误用S。
所有非空m带满足 \(M<X\)，在旧prefix引理的合法长度域内。

对 \(O(\log^2X)\) 个带在norm层Minkowski，第四次方最多付 \(\log^8X\)。
每个最终固定ε先取 \(\rho=\delta=\varepsilon/20\)，再以
\(\log^8X\ll_\varepsilon X^{\varepsilon/2}\) 支付，总损失为
\(3\varepsilon/4<\varepsilon\)。前件常数对 \(2\le S\le V\) 统一。

对于指定floor，最终大X下 \(V\ge X^{1/8}/2\)，\(S\le X^{1/20}\)，
所以 \(S^2\le X^{1/10}\)、\(XS^4/V^4\le16X^{7/10}\)。
独立 Fraction 重算给
\[
7/10,\qquad17/24-7/10=1/120,\qquad17/96-7/40=1/480.
\]
floor只进入实际整数定义和上述单侧界，没有边界误差。
声称显示指数严格低于17/24时最后应取ε<1/120；作者已说明这一限制。

## 5. 精确新余项及不变的整体coupling

原non-squarefull是 \(s\ge2\)，故 \(2\le s\le S\) 与 \(s>S\)
精确分成两个不交整数集合：\(R_{479}=D_S+R_{\rm new}\)。
m始终是large genuine prime，不重新加入short m、proper powers或s1。
系数负号及原prime/composite相消均留在实际函数里。

合成同一误差函数
\(E_{\rm new}=(P_H-R_{479})+D_S\) 后，
\(7/40<17/96\)，整体norm仍为 \(X^{17/96+\varepsilon}\)。
先为最终第四均值分配norm损失ε/4，再仅用一次
\((u+v)^4\le8(u^4+v^4)\)，两向coupling均保留原
\(O(X^{17/24+\varepsilon})\) 和常数8。不是两第四矩的additive等同。

## 6. 独立有限复算与准入边界

除逐式数学逆审，实际用Python Fraction及整数标签在内存运行：

- 对全部 \(1\le k\le12000\)，另枚举所有互素squarefree×squarefull乘积，
  验证12000个k各恰有唯一分解，并与valuation定义的s、t相同。
- 对 \(2\le V\le32\)，核4583个radical≤V的真实自然零例，
  及7553个nonnull、\(2\le s\le V\) 的严格 \(ks>V^2\) 阈值例。
- 对 \(2\le V\le16,2\le S\le V\)，核1046个从实 \(V^2/S\) 起的dyad带，
  实际小s计数不超过扩大后的squarefull对计数，后者平方不超过72KS。
- 用三组 \((V,M_0,S,Y,X)\)：\((4,9,3,80,800)\)、
  \((6,11,4,200,1800)\)、\((8,13,5,360,3200)\)，以 \(\log p\) 作形式标签，
  逐原 signed 系数核 \(R_{479}=D_S+R_{\rm new}\)，有效项数分别为
  \(225=35+190\)、\(412=10+402\)、\(837=98+739\)。
  D_S的非零项均落入唯一真实实端点带；共同乘积mask与两个prime-prefix差
  的整数集合逐项相同。
- 独立核全部新增有理成本、ε分配、两处严格余量和最大合成费用17/24。

这些有限检查认证所列有限模型与有理式，不能认证无限解析估计。
最大prefix均值及所有量词来自已实读证明与上述数学逆审；没有重新执行旧大核、
七点覆盖或更改冻结文件。

本轮支付完整D_S自然子族的7/10四矩；新剩余仍是 \(s(k)>S\) 的完整signed mixed4，
balanced prime×prime仍在其中。整体5/7增长上界、引用输入下
\(\sigma_*\approx0.874957019420099\) 及原MT比例未由本稿改变。
没有whole新幂、whole常数四矩、新比例、κ反馈、RH或新无零条带结论。
