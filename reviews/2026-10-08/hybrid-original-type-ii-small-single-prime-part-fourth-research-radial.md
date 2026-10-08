# 原Type II小一次素因子部分：完整自然子族的7/10四矩付款

2026-10-08。作者：radial。基线为已提交并推送479的
main0cb98a7de5c92c949efbe9cfb3012d7716194e0c。
只新增本源；479及全部冻结输入、检查点、旧审查和Git均不修改。

**状态：完整子族证明，待不同作者全文独审。** 在479的同一真实剩余中，
令 \(s(k)\) 为所有valuation恰为1的素因子之乘积。
完整子族 \(2\le s(k)\le\lfloor X^{1/20}\rfloor\) 的四矩满足
\[
 \mathcal M_{D_S}\ll_{\phi,\varepsilon}X^{7/10+\varepsilon},
 \qquad \frac{17}{24}-\frac7{10}=\frac1{120}>0.
 \tag{1}
\]
全部允许的genuine-prime m、原 \(b_V(k)\)、正高度窗和共同sharp乘积掩码均保留。
它进一步缩小实际因子余项，不建立新的whole四矩上界、比例、无零条带或κ反馈。

## 1. 同一原对象与最终冻结接口

保持
\[
 X=T/(2\pi),\quad \ell=\log X,\quad
 J_T=[T/4,4T],\quad a_\ell\ge c_\phi>0,
 \quad U=V=\lfloor X^{1/8}\rfloor,
\]
\[
 Y=X^{5/6},\qquad M_0=\lfloor X^{1/4}\rfloor,\qquad
 \|F\|_{p,T}=\left(\frac1T\int_{J_T}|F(t)|^pdt\right)^{1/p}.
 \tag{2}
\]
原genuine高素数scalar仍为
\[
 P_H(t)=\frac1{a_\ell\ell}
 \sum_{\sqrt X<p\le X}\frac{\log p}{\sqrt p}p^{it}.
\]
479精确留下的finite signed scalar是
\[
 R_{479}(t)=-\frac1{a_\ell\ell}
 \sum_{\substack{m>M_0,\ m\ {\rm prime}\\
                  k>V,\ k\ {\rm not\ squarefull}\\Y<mk\le X}}
 \frac{\Lambda(m)b_V(k)}{\sqrt{mk}}(mk)^{it},
 \qquad b_V(k)=\sum_{\substack{d\mid k\\d\le V}}\mu(d).
 \tag{3}
\]
squarefull指每个素因子的valuation至少为2。
原余项m是genuine prime，所以 \(\Lambda(m)=\log m\)；没有把k系数改为μ(k)。

| 最终冻结输入 | canonical LF SHA256 |
|---|---|
| [479实际因子归约](../../notes/479-original-type-ii-factor-reduction-and-diagonal-gauge.md) | 6b6e15f8a3a83d62e1d472cbeaa86a894c9e01740ccd682fc79ec99c2ec5a559 |
| [完整因子证明及最大prefix引理](hybrid-original-type-ii-short-lambda-factor-fourth-research-radial.md) | b39876e0b9d91a06de57d1069cf6adac676252bd1fe737186bb065716015abb0 |

前源§8(22)的实际最大prefix结论对 \(A\ge1,\ A\ll X\)、
\(q(n)=\Lambda(n)1_{\rm prime}(n)\) 和每个先固定 \(\rho>0\) 给
\[
 \frac1T\int_{J_T}
 \max_{A\le u\le2A}
 \left|\sum_{A<n\le u}\frac{q(n)}{\sqrt n}n^{it}\right|^4dt
 \ll_{\phi,\rho}X^\rho(1+A^2/X).
 \tag{4}
\]
其证明使用actual binary blocks、平方后长度4A²的均值、
divisor Cauchy及同层能量 \(2^{-j}\)，不需要ζ四矩或零自由条带。
\(q(n)=\Lambda(n)1_{\rm prime}(n)\) 自身满足每个固定损失的subpower系数前件。
本次直接对这个q使用(4)，没有从完整Λ多项式的norm推出任意prime子集norm。

479另已证明
\[
 \|P_H-R_{479}\|_{4,T}
 \ll_{\phi,\varepsilon}X^{17/96+\varepsilon}.
 \tag{5}
\]
本源只使用这些已独审的finite/mean-value接口。
新算术证明是下文的唯一分解、原divisor零项和完整自然子族计数；
没有新增外部解析输入。

## 2. 唯一互素分解与原系数的自然零域

对每个整数 \(k\ge1\)，定义
\[
 s(k)=\prod_{v_p(k)=1}p,\qquad t(k)=k/s(k).
 \tag{6}
\]
逐素因子看：valuation1全部放入s，valuation至少2全部放入t。
因此这给唯一分解
\[
 k=st,\quad s\ {\rm squarefree},\quad
 t\ {\rm squarefull},\quad(s,t)=1.
\]
允许 \(s=1\) 或 \(t=1\)；1按空素因子条件计入相应类。
特别地，\(s(k)=1\) 当且仅当k squarefull。
在原 \(k>V\ge2\) 下，k1已排除；所以(3)中的non-squarefull条件
准确等价于 \(s(k)\ge2\)。

对所有 \(k>1\)，若 \(\operatorname{rad}(k)\le V\)，则所有非零μ-divisors
均为rad(k)的divisors，且均≤V。因此原有限系数精确为
\[
 b_V(k)=\sum_{d\mid\operatorname{rad}(k)}\mu(d)=0.
 \tag{7}
\]
这是必要零域，不宣称其逆命题成立；未将bV换成一个radical indicator。
反过来，仅由 \(b_V(k)\ne0\) 推出 \(\operatorname{rad}(k)>V\)。

由互素性，\(\operatorname{rad}(k)=s\operatorname{rad}(t)\)；
由于t squarefull，\(\operatorname{rad}(t)^2\mid t\)。
故非零系数满足
\[
 \operatorname{rad}(t)>V/s,\qquad
 t>(V/s)^2,\qquad k=st>V^2/s.
 \tag{8}
\]
取
\[
 S=\lfloor X^{1/20}\rfloor,\qquad K_0=V^2/S.
 \tag{9}
\]
T足够大时 \(2\le S<V\)；对 \(2\le s(k)\le S\)，
所有非零项严格满足 \(k>K_0\)。
同时原 \(m>M_0\)、\(mk\le X\) 给
\(k\le X/(M_0+1)<X\)，所以实际外因子范围有限。
允许在求和中去掉 \(k\le K_0\) 的精确零项；其余项仍使用完整原bV。
\(s=1\) 的旧squarefull付款不被本次重复计入。

## 3. 全dyadic带的自然计数与加权L1

平方满整数r可唯一写为 \(r=a^2b^3\)，b squarefree：
even valuation全放入a²，odd valuation≥3取一个b³。
对任意 \(Z\ge1/2\)，包括r1在内，
\[
 \#\{Z<r\le2Z:r\ {\rm squarefull}\}
 \ll\sqrt Z.
 \tag{10}
\]
证明是取掉b的squarefree限制后，
\[
 \#\{r\le2Z:r\ {\rm squarefull}\}
 \le \sum_{b\le(2Z)^{1/3}}\sqrt{2Z}\,b^{-3/2}
 \ll\sqrt Z.
\]
若 \(0<Z<1/2\)，对应正整数区间为空，(10)仍成立。

对每个真实dyadic k带 \((K,2K]\)，按唯一s,t分解计数，
并仅为upper取掉s的squarefree和互素限制，有
\[
 \begin{split}
 \#\{K<k\le2K:2\le s(k)\le S\}
 &\le\sum_{2\le s\le S}
       \#\{K/s<t\le2K/s:t\ {\rm squarefull}\}\\
 &\ll\sqrt K\sum_{s\le S}s^{-1/2}
 \ll\sqrt{KS}.
 \end{split}
 \tag{11}
\]
本次并未增加 \(\operatorname{rad}(t)\) 或t的人工上限；
所有原k中满足小一次素因子条件的项均被计入。
自然zero与原 \(k>V,\ k\le X/(M_0+1)\) 只会减少这个upper。

对每个先固定 \(\delta>0\)，实际 \(|b_V(k)|\le\tau(k)\ll_\delta X^\delta\)
在 \(k\le X\) 上成立，常数对V统一。
于是原有限外L1权满足
\[
 A_K=
 \sum_{\substack{K<k\le2K\\k>V,\ k\le X/(M_0+1)\\
                      2\le s(k)\le S\\b_V(k)\ne0}}
       \frac{|b_V(k)|}{\sqrt k}
 \ll_\delta X^\delta\sqrt S.
 \tag{12}
\]
这不是对μ的随机性或均值假设；保留原系数后使用确定性upper。
计算(12)不要求其他m条件或乘积掩码可分离。

## 4. 完整原子族与全部sharp边界

定义同一(3)的子族
\[
 D_S(t)=-\frac1{a_\ell\ell}
 \sum_{\substack{m>M_0,\ m\ {\rm prime}\\
                   k>V,\ 2\le s(k)\le S\\Y<mk\le X}}
 \frac{\Lambda(m)b_V(k)}{\sqrt{mk}}(mk)^{it}.
 \tag{13}
\]
按(8)–(9)，所有非零k可从 \(K_0\) 开始分成
\(K_j<k\le2K_j,\ K_j=2^jK_0\)。
m从 \(M_0\) 开始分成
\(M_i<m\le2M_i,\ M_i=2^iM_0\)。
这些是真实开左闭右整数交集，不先把实端点圆整为另一个多项式；
相邻带端点没有遗漏或双计。原m,k均≤X，实际带数各为O(logX)。

对一个非空带pair \((M,2M]\times(K,2K]\)，固定实际k后，
原共同乘积条件给m区间
\[
 (\max(M,M_0,Y/k),\ \min(2M,X/k)].
 \tag{14}
\]
若左端≥右端则该inner sum为0。
否则在 \((M,2M]\) 上它精确为两个prefix之差，使用
\(q(n)=\Lambda(n)1_{\rm prime}(n)\)。
对于下端还超出2M或上端低于M的空情况，先判空；
一般情形把prefix端点clamp到 \([M,2M]\) 即得同一整数集合。

置
\[
 F_M(t)=\max_{M\le u\le2M}
 \left|\sum_{M<n\le u}
       \frac{\Lambda(n)1_{\rm prime}(n)}{\sqrt n}n^{it}\right|.
\]
逐t对原k外因子取绝对值，\(|k^{it}|=1\)，有
\[
 |D_{M,K}(t)|\le\frac{2A_K}{a_\ell\ell}F_M(t).
 \tag{15}
\]
式(15)只在建立upper时取绝对值；定义(13)与后文ledger仍为原signed scalar。
共同 \(Y<mk\le X\) 全部由移动prefix端点保留，未换为rectangle，
也没有丢掉m的genuine-prime条件。

由(4)、(12)，对先固定 \(\rho,\delta>0\)，
\[
 \|D_{M,K}\|_{4,T}^4
 \ll_{\phi,\rho,\delta}
   X^{\rho+4\delta}S^2(1+M^2/X).
 \tag{16}
\]
非空带有实际 \(m>M,\ k>K,\ mk\le X\)，故 \(MK<X\)。
又所有k带从 \(K\ge K_0=V^2/S\) 开始，因此
\[
 M<X/K\le XS/V^2,\qquad
 S^2(1+M^2/X)\le S^2+XS^4/V^4.
 \tag{17}
\]
虽然这对某些空带较粗，非空带的统一upper已经足够。
这里没有要求固定高度的未知prime四矩或旧增长范数为常数。

## 5. 有限dyads、ε顺序与7/10成本

对O(log²X)个实际非空带pair使用L4 Minkowski，得
\[
 \|D_S\|_{4,T}
 \le\sum_{M,K}\|D_{M,K}\|_{4,T}.
\]
为给任意最终固定 \(\varepsilon>0\) 的第四均值结论，
先取 \(\rho=\delta=\varepsilon/20\)。
把O(log²X)个项的合计norm取第四幂，日志费用至多O(log⁸X)；
它可用 \(C_\varepsilon X^{\varepsilon/2}\) 控制。
于是 \(\rho+4\delta+\varepsilon/2=3\varepsilon/4<\varepsilon\)，
全部损失在最终ε内，且所有参数先固定。
因此
\[
 \boxed{\quad
 \mathcal M_{D_S}
 \ll_{\phi,\varepsilon}
        X^\varepsilon\bigl(S^2+XS^4/V^4\bigr).
 \quad}
 \tag{18}
\]
此证明对一般整数 \(2\le S\le V\) 的同一子族也成立；
主结果只取(9)，不更改U,V,Y。

T足够大时 \(V\ge X^{1/8}/2\)，并且 \(S\le X^{1/20}\)，所以
\[
 S^2\le X^{1/10},\qquad
 XS^4/V^4\le16X^{\,1+4/20-4/8}=16X^{7/10}.
\]
由(18)得到(1)。取floor未产生边界误差，也没有把V的取整替成精确幂等式。
所有k零项及s临界端点按原整数集合处理。

对于“严格低于479的17/24付款”，可固定
\(0<\varepsilon<1/120\)；任意较大ε的带损失式仍正确，
但不能据此声称显示幂严格较小。
新范数基准 \(7/40\) 与旧 \(17/96\) 的差为
\[
 \frac{17}{96}-\frac7{40}=\frac1{480}>0.
 \tag{19}
\]
整段证明只使用原有限系数、确定性稀疏计数和已证最大prefix均值。
没有调用零自由条带、普通或Hecke新密度、FE反射或任意字符家族平均。

## 6. 精确新剩余与whole预算保持

在原k>V范围，non-squarefull准确等价于 \(s(k)\ge2\)，故精确finite partition为
\[
 R_{479}=D_S+R_{\rm new},
\]
\[
 R_{\rm new}(t)=-\frac1{a_\ell\ell}
 \sum_{\substack{m>M_0,\ m\ {\rm prime}\\
                   k>V,\ s(k)>S\\Y<mk\le X}}
 \frac{\Lambda(m)b_V(k)}{\sqrt{mk}}(mk)^{it}.
 \tag{20}
\]
本次D_S不含s1，因而不重复479的squarefull-k子族。
m仍为genuine prime，不回加已付proper powers或short-m项。
原negative coefficient和prime/composite cancellation均保留；
(20)没有由某一positive sector替换成另一对象。

由(1)、(5)，重新分配最终固定ε，先合成误差函数
\[
 E_{\rm new}=P_H-R_{\rm new}
           =(P_H-R_{479})+D_S.
\]
L4 Minkowski与 \(7/40<17/96\) 给
\[
 \|E_{\rm new}\|_{4,T}
 \ll_{\phi,\varepsilon}X^{17/96+\varepsilon}.
 \tag{21}
\]
为得到最终第四均值的ε，先在(21)取范数损失ε/4，
然后只用一次两项不等式 \((u+v)^4\le8(u^4+v^4)\)，有
\[
 \boxed{\quad
 \mathcal M_T\le8\mathcal M_{R_{\rm new}}
                 +C_{\phi,\varepsilon}X^{17/24+\varepsilon},
 \qquad
 \mathcal M_{R_{\rm new}}\le8\mathcal M_T
                 +C_{\phi,\varepsilon}X^{17/24+\varepsilon}.
 \quad}
 \tag{22}
\]
这里第二式来自 \(R_{\rm new}=P_H-E_{\rm new}\)；
没有把两第四矩解释为additive相差小量，亦未把连续几次triangle的8误乘后仍记8。

**新增付款的范围**是(13)的全部原允许m,k、全部aspect ratios和原positive-height窗；
不存在一个尚待付款的本子族边界或t-tail。
**尚未付款的范围**是(20)的完整signed mixed4，尤其balanced prime×prime仍在其中。
\(s(k)>S\) 是新剩余的原因子条件，不是其有用whole upper。

479所保持的既有whole \(X^{5/7+\varepsilon}\) 增长结果及
引用输入下 \(\sigma_*\approx0.874957019420099\) 均不由本稿改变。
新的全球第四常数、whole幂改进、κ反馈和新简单比例均未支付。
本稿不改cut参数，不能把另一个 \(U,V\) 的系数合同视作冻结剩余的免费改善。
