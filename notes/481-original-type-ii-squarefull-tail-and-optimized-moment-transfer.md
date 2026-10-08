# 481. 原 Type II 平方丰满尾与优化的完整矩传递

2026-10-08。基线 main `f20c94b4833091078e462f86df70eb8c3222ef0f`。
继续原数域和原函数，联合调整辅助截断，降低已付误差，而非改变研究对象。

本轮得到原 genuine-prime scalar 的精确归约
\[
 P_H=R_{\rm opt}+E_{\rm opt},\qquad
 \mathcal M_{E_{\rm opt}}\ll_{\phi,\epsilon}X^{13/21+\epsilon}.
 \tag{1}
\]
在476引用的原 \([R_{7/8}]\) 下，完整正高度第四矩因此满足
\[
 \boxed{\mathcal M_{P_H}=\mathcal M_{R_{\rm opt}}
       +O_{\phi,\epsilon}(X^{29/42+\epsilon}).}
 \tag{2}
\]
误差幂比480的 \(479/672\) 小 \(5/224\)，距已有完整增长尺度 \(5/7\)
的余量从 \(1/672\) 扩大到 \(1/42\)。最终余项仍未取得新第四矩上界；
(1)不是 whole \(13/21\) 的结论，(2)也不是常数级四矩渐近。

## 1. 同一原函数与新有限分区

保持
\[
 X=T/(2\pi),\quad L=\log X,\quad J_T=[T/4,4T],\quad a_L\ge c_\phi>0,
\]
\[
 P_H(t)=\frac1{a_LL}\sum_{\sqrt X<p\le X}
           \frac{\log p}{\sqrt p}p^{it},\qquad
 \mathcal M_F=\frac1T\int_{J_T}|F(t)|^4dt.
\]
只改变 Vaughan 分区的辅助参数：
\[
 U=V=\lfloor X^{2/21}\rfloor,\quad
 M=\lfloor X^{4/21}\rfloor,\quad H=V^2,\quad Y=X^{17/21}.
 \tag{3}
\]
它们在高度极限前固定为这些幂的整数截断。
大 \(X\) 时 \(U<M\)、\(MV<Y\)、\(UV<Y\)、\(\sqrt X<Y<X\)，
且 \(H\le M\)、\(H\asymp X^{4/21}\)。保留所有 sharp endpoints。

仍用实际系数
\[
 b_V(k)=\sum_{d\mid k,\ d\le V}\mu(d),\qquad
 C_4(t)=-\frac1{a_LL}
 \sum_{\substack{m>U,\ k>V\\Y<mk\le X}}
       \frac{\Lambda(m)b_V(k)}{\sqrt{mk}}(mk)^{it}.
 \tag{4}
\]
对 \(k\ge1\)，置
\[
 s(k)=\prod_{v_p(k)=1}p,\qquad r(k)=k/s(k).
\]
这是唯一互素的 squarefree / squarefull 分解，\(1\) 视为平方丰满。
不能替换成按指数奇偶定义的 squarefree kernel。

顺序分成四个不重叠部分：

| 原 \(C_4\) 中的部分 | 精确域；共同保留 \(Y<mk\le X\) |
| --- | --- |
| \(S_M\) | \(U<m\le M\)，全部 \(k>V\) |
| \(Q_{\rm pp}\) | \(m>M\) 为 proper prime power，全部 \(k>V\) |
| \(Q_{>H}\) | \(m>M\) 为 genuine prime，\(r(k)>H\) |
| \(R_{\rm opt}\) | \(m>M\) 为 genuine prime，\(r(k)\le H\) |

故 \(C_4=S_M+Q_{\rm pp}+Q_{>H}+R_{\rm opt}\) 是精确有限恒等式。
对最后一行，\(k>V\) 且 \(s(k)=1\) 会给平方丰满 \(1<k\le V^2\)，
其全部非零 Möbius divisors 都不超过 \(\operatorname{rad}(k)\le V\)，
所以 \(b_V(k)=0\)。真实非零剩余自动满足 \(s(k)\ge2\)；还满足
\(s(k)\operatorname{rad}(r(k))>V\)。因为 \(m>M\ge H\ge r(k)\)，
素数 \(m\) 还自动与 \(r(k)\) 互素。

新的 \(b_V,Y,M\) 与480不同。没有宣称新余项是旧 \(R_\sharp\) 的子集，
也没有把旧余项的任何未证上界搬到新域。

## 2. 原输入与参数化的完整费用

Vaughan 系数恒等式、低段完整平方长度和 proper-power 范数迁移来自
[477证明源](../reviews/2026-10-08/hybrid-original-vaughan-type-i-and-type-ii-reduction-research-radial.md)。
其恒等式对任意精确整数 \(U,V\) 和 \(n>U\) 成立：
\[
 \Lambda(n)=\sum_{d\mid n}g_{U,V}(d)
 +\sum_{d\mid n,\ d\le V}\mu(d)\log(n/d)
 -\sum_{mk=n,\ m>U,\ k>V}\Lambda(m)b_V(k),
\]
其中 \(g_{U,V}(d)=-\sum_{ab=d,a\le U,b\le V}\Lambda(a)\mu(b)\)。
所以 \(Y<n\le X\) 的高段仍精确等于 \(I_2+I_3+C_4\)。

本轮主线程全文重读上述源和
[479因子证明源](../reviews/2026-10-08/hybrid-original-type-ii-short-lambda-factor-fourth-research-radial.md)。
后者§§2–4证明在原 \(t\in J_T\)、每个 sharp 子区间 \(I\subset[1,CX]\) 上
\[
 \left|\sum_{n\in I}n^{-1/2}(\log n)^j n^{it}\right|
 \ll_C X^{1/6}\log^{j+1}(2X),\qquad j=0,1.
 \tag{5}
\]
一次真实差分和二阶导数界支付所有长度，所有 partial endpoints 统一。
这一步不使用零自由前件；没有借一个未写出的指数对改进。

先固定 \(0<v<a\)、\(\max(1/2,a+v)<y<1\)，重新取
\(U=V=\lfloor X^v\rfloor,M=\lfloor X^a\rfloor,Y=X^y\)。
由这些已全文核对的证明逐式得到：

| 部分 | 原系数与完整窗口的第四矩费用 |
| --- | --- |
| \(L_Y\)，\(\sqrt X<n\le Y\) 的 \(\Lambda\) 和 | \(X^\epsilon(1+X^{2y-1})\) |
| \(I_2+I_3\) | \(X^{1/3+2v+\epsilon}\) |
| \(S_M\) | \(X^{1/3+a+v+\epsilon}\) |
| \(Q_{\rm pp}\) | \(X^\epsilon(1+X^{1-2a})\) |

低段是先平方再对长度 \(\le Y^2\) 的实际乘积多项式用时间二矩。
Type I 的 \(g,\mu\) 外权满足总加权质量 \(\ll X^\epsilon\sqrt{UV}\)，
由(5)得 sup \(\ll X^{1/6+v+\epsilon}\)；长度 \(\le X\) 的真实系数
二矩为 \(X^\epsilon\)，故费用 \(1/3+2v\)。
\(S_M\) 因 \(Y/M>V\)，展开有限 \(d\le V\) 后 inner 区间准确为
\((Y/(md),X/(md)]\)；sup 是 \(X^{1/6}\sqrt{MV}\log^C X\)，
其实际系数二矩同样为 \(X^\epsilon\)，给 \(1/3+a+v\)。
大 proper-power 的 dyadic 外权 \(\sum\Lambda(m)/\sqrt m\ll\log^2X\)，
内 \(b_V\) 最大 prefix 四矩在长度 \(K<X/M\) 上为
\(X^\epsilon(1+K^2/X)\)，给最后一行。原 moving product cutoff 都由
两个真实 prefix 之差保留；没有把斜域替成矩形。

## 3. 新平方丰满尾：先合并 \(m s\)，再付全 \(r>H\)

完整新证明与零点留数接口见
[不同作者研究源](../reviews/2026-10-08/hybrid-original-type-ii-large-single-prime-part-research-checkpoint-audit.md)。
其关键步骤如下，允许全部 \(s\ge1\)，不只小 \(s\) 子族。
固定平方丰满 \(r\)，将 \(n=ms\) 合并，准确系数为
\[
 c_r(n)=\frac1L\sum_{\substack{ms=n,\ m>M\ {\rm prime}\\
             s\ {\rm squarefree},\ (s,r)=1,\ sr>V}}
             \Lambda(m)b_V(sr).
 \tag{6}
\]
各项保留实际 Möbius divisor 符号，\(\Lambda(m)/L\le1\)。
由 \(|b_V(sr)|\le\tau(sr)\le\tau(r)\tau(s)\)，
\[
 |c_r(n)|\le\tau(r)\tau_3(n)\ll_\delta X^{2\delta}
 \quad(r,n\le X)
\]
对每个固定 \(\delta>0\) 一致。系数可依赖 \(r,X,V,M\)，但这个常数统一。
真实 inner 的两个乘积端点现在是 \(Y/r<n\le X/r\)。

479源§8的最大 prefix 四矩引理只要求这种一致 subpower 系数界，给长度
\(N\ll X/r\) 的 inner 费用 \(X^\epsilon(1+N^2/X)\)。
平方丰满 \(r\in(K,2K]\) 的带权质量
\(\sum r^{-1/2}\ll1\)，因为每个平方丰满整数唯一写作 \(a^2b^3\)、
\(b\) 平方自由，其 dyadic 项数为 \(O(\sqrt K)\)。
固定 \(r\) 的真实端点以最大 prefix 支付，对外 \(r\) 用一次 Minkowski，
再对 \(K=2^jH\) 的全部非空 dyads求和；所有日志先分配到最终 \(\epsilon\)，
得到整个 genuine-prime \(m>M\) 的尾族
\[
 \boxed{\mathcal M_{Q_{>H}}\ll_{\phi,\epsilon}
         X^\epsilon(1+X/H^2).}
 \tag{7}
\]
这是对该原 signed 子族自身的证明，不从较大 signed 函数范数推子集范数。
当 \(H=V^2\) 时，它同时包含所有非零平方丰满 \(k\)，无需再单列该项。

## 4. 联合参数优化与 \(13/21\)

在 \(H=V^2\asymp X^{2v}\) 的这套费用中，令最大误差幂为
\[
 c=\max\{2y-1,\ 1/3+2v,\ 1/3+a+v,\ 1-2a,\ 1-4v,\ 0\}.
\]
选择(3)，逐项为
\[
 (2y-1,\ 1/3+2v,\ 1/3+a+v,\ 1-2a,\ 1-4v)
 =\left(\frac{13}{21},\frac{11}{21},\frac{13}{21},
         \frac{13}{21},\frac{13}{21}\right).
\]
floor 仅带来固定常数：\(M\ge X^{4/21}/2\)、
\(H\ge X^{4/21}/4\)，大 \(X\) 时适用。
将低段、Type I、\(S_M,Q_{\rm pp},Q_{>H}\) 和已付完整 proper-power
迁移先合成同一个 \(E_{\rm opt}\)，一次 \(L^4\) Minkowski 证明(1)。
故还无条件有两向范数耦合
\[
 \mathcal M_{P_H}\le8\mathcal M_{R_{\rm opt}}+O(X^{13/21+\epsilon}),
 \quad
 \mathcal M_{R_{\rm opt}}\le8\mathcal M_{P_H}+O(X^{13/21+\epsilon}).
 \tag{8}
\]

这个取参在**所列费用且 \(H\le V^2\) 的参数域**内最小化最大误差。
因为 \(c\ge1-2a,1-4v\)，有 \(a\ge(1-c)/2,v\ge(1-c)/4\)；
再用 \(c\ge1/3+a+v\) 得
\(c\ge1/3+3(1-c)/4\)，即 \(c\ge13/21\)。
这里不声称最优的全 Type II、最佳指数对、最佳分区或无零边界。

## 5. 原 \(7/8\) 输入下的完整矩传递

仅在这一节使用[476](476-original-fourth-growth-five-sevenths-with-ivic-density.md)
及其明确引用合同 \([R_{7/8}]\)：原同一 \(P_H\) 在整个 \(J_T\) 满足
\(\mathcal M_{P_H}\ll X^{5/7+\epsilon}\)。
由(1)及 Minkowski 先证明 \(\mathcal M_{R_{\rm opt}}\ll X^{5/7+\epsilon}\)。
然后才对两个完整范数用480中的 Hölder 传递：
\[
 |\mathcal M_F-\mathcal M_G|
 \ll \|F-G\|_{4,T}(\|F\|_{4,T}+\|G\|_{4,T})^3.
\]
重新分配固定 \(\epsilon\) 后，幂为
\[
 \frac{3(5/7)+13/21}{4}=\frac{29}{42},\qquad
 \frac57-\frac{29}{42}=\frac1{42},\qquad
 \frac{479}{672}-\frac{29}{42}=\frac5{224}.
\]
证明(2)。当最终 \(\epsilon<1/42\)，以 \(X^{5/7}\) 归一化的差趋零。
没有证明相对于未知实际主项的相对渐近，也没有把增长误差当成 \(o(1)\)。

## 6. 留数合同与剩余研究目标

新余项仍含 balanced genuine-prime \(m\) 与平方自由 \(k\)（\(r=1\)）。
共同 \(Y<mk\le X\)、实际 \(b_V(k)\) 和全部 aspect ratios 继续保留。
平方丰满尾源另精确计算 small-\(r\) 的 Dirichlet 生成函数：
其平方自由系数含 \(\zeta(z)/\zeta(2z)\) 乘有限局部因子再减1，
因此真实 Type II 在每个 \(\Re\rho>1/2\) 的 zeta 零点仍有
\(-m_\rho\) 留数。低端有限截断不改留数。
这解释了新分区没有自动消除零点障碍；它不是方法不可能性定理。

下一项仍是 \(R_{\rm opt}\) 的完整 signed mixed4 或保留共同轮廓的
实际素数四点近共振常数。当前 whole \(5/7\)、简单比例
67.3058110282…%和引用输入下 \(\sigma_*\approx0.874957019420099\) 保持。
本轮未触发新纪录论文或新无零边界论文。

## 7. 独立审查与精确检查点

新平方丰满尾源的 canonical LF SHA256 为
`66c35eb3ed43cec836ff1d10ed01322f115684c44b771d3db7364637994c3cab`；
其[主线程全文审查](../reviews/2026-10-08/hybrid-original-squarefull-tail-and-euler-review-root.md)
核对完整尾界及局部Euler留数。本文的参数、完整误差和矩传递另经
[不同作者数学审查](../reviews/2026-10-08/hybrid-original-optimized-type-ii-note-review-checkpoint-audit.md)。

[精确检查器](../scripts/hybrid_optimized_type_ii_checkpoint.py)绑定本文和五个
完整证明输入的 canonical hashes；[保存输出](../output/hybrid-optimized-type-ii-checkpoint.json)
记录13/21、29/42、1/42、5/224的有理算术、两个有限X的全部高段
Vaughan系数及四分区、合并平方丰满尾和三个有限prime Euler恒等式。
用 `--write` 保存，`--check` 只读核验。没有把有限重放声明为无穷估计、
新whole上界、真实零点比例或新无零区域的证明。
