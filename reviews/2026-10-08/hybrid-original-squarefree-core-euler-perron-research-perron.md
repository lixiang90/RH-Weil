# 原 Type II 的平方自由核心：Euler 消极点与无条件 1/2 完整误差

2026-10-08，perron_reviewer。研究基线 main
`a4e4c8cf3de71450325174028f0ed09dd5ef4dec`。
只新增本研究源，不修改冻结来源、笔记、输出、检查器或 Git。
**状态：完整新证明，待 root 和不同作者 FULL READ 后准入。**

本稿直接支付两个原算术子族，而不是重新优化486的同一费用表：
全部 proper-prime-power 外因子 \(m>U\)，以及 genuine-prime \(m>U\)
的全部 \(2\le r(k)\le V^2\) 部分。后者的生成函数带 \(\zeta\) 因子，
准确消掉 prime 因子的零点极点；\(r=1\) 的平方自由部分仍含原 \(-1\)。

因此可以不再使用486的 \(m\le A\) 分区，保留同一原函数而得到
\[
 \boxed{P_H=R_{\rm sf}+E_{\rm sf},\qquad
        \mathcal M_{E_{\rm sf}}\ll_{\phi,\epsilon}X^{1/2+\epsilon}.}
\tag{1}
\]
这个完整误差界不使用无零前件。在476的原 \([R_{7/8}]\) 及其已有
完整增长界下，另外得到
\[
 \boxed{\mathcal M_{P_H}=\mathcal M_{R_{\rm sf}}
            +O_{\phi,\epsilon}(X^{37/56+\epsilon}).}
\tag{2}
\]
相比486的 \(9/17\)、\(159/238\)，分别节省 \(1/34\)、\(1/136\)。
没有新的 whole 上界、中心四阶常数预算、零点比例或无零边界。
新的主项是明确的 genuine-prime 与 squarefree 带符号卷积，仍待付款。

## 1. 冻结输入与原实际对象

本作者在连续研究轮已 FULL READ 下列原证明；本轮重读486、481、
401行平方丰满/Euler源、short-Möbius源，并重新核原 Vaughan 低段及
最大 prefix 证明的实际量词。哈希仅把 CRLF/lone CR 转 LF，不 trim。

| 输入 | canonical LF SHA256 |
| --- | --- |
| [486及完整分区](../../notes/486-original-padded-perron-fourth-mean-remainder.md) | 5e98058d6d47545aedb98b6e70f66f4e11a904b623351903e3846e01bbe7eaf7 |
| [505行长因子第四均值源](hybrid-original-extended-inner-zeta-fourth-perron-research-perron.md) | 54d39f22b370be40a780fac6fe80968e24c014fc48d1156ab87248d5310a2549 |
| [481完整分区](../../notes/481-original-type-ii-squarefull-tail-and-optimized-moment-transfer.md) | 4ce3ea2ac087d734142c8788607c1c54fc6887bcf535c806c88097447afdc63e |
| [401行实际平方丰满尾与Euler源](hybrid-original-type-ii-large-single-prime-part-research-checkpoint-audit.md) | 66c35eb3ed43cec836ff1d10ed01322f115684c44b771d3db7364637994c3cab |
| [477 Vaughan恒等式与低段源](hybrid-original-vaughan-type-i-and-type-ii-reduction-research-radial.md) | cf58086aeb9eee63832ccd06f5499110ea236b4bd94396893757b62e75bdb9d4 |
| [479实际最大prefix与疏项源](hybrid-original-type-ii-short-lambda-factor-fourth-research-radial.md) | b39876e0b9d91a06de57d1069cf6adac676252bd1fe737186bb065716015abb0 |
| [原短Möbius与完整留数源](hybrid-short-mobius-twist-and-vaughan-zero-residue-research-radial.md) | a970366e68b8d3526c0dadac49b8ee8f4a7b6984e763712a851f8b6d353a291d |
| [476已有完整增长界](../../notes/476-original-fourth-growth-five-sevenths-with-ivic-density.md) | 179829dd25f92ff187359f73455aafad9f957d714df13cf871db47a76e9408b6 |

保持 \(X=T/(2\pi)\)、\(L=\log X\)、\(J_T=[T/4,4T]\)、
\(a_L\ge c_\phi>0\)，以及
\[
 P_H(t)=\frac1{a_LL}\sum_{\sqrt X<p\le X}
                  \frac{\log p}{\sqrt p}p^{it},\qquad
 \|F\|_{4,T}^4=\mathcal M_F=T^{-1}\int_{J_T}|F(t)|^4dt.
\tag{3}
\]
所有原整数集合、负号、normalizer及正高度保持。
先取固定 \(0<v<1/4\)、\(1/2<y<1\)，
\[
 U=V=\lfloor X^v\rfloor,\quad H=V^2,\quad Y=X^y,
 \quad b_V(k)=\sum_{d\mid k,d\le V}\mu(d).
\tag{4}
\]
大 \(X\) 时 \(UV<Y\)。定义唯一的 valuation 恰为1分解
\[
 s(k)=\prod_{v_p(k)=1}p,\quad r(k)=k/s(k).
\]
\(s\) squarefree、\(r\) squarefull、\((s,r)=1\)，允许1。
这不是按指数奇偶定义的 squarefree kernel。

原高段 Vaughan Type II 是
\[
 C_4(t)=-\frac1{a_LL}
 \sum_{\substack{m>U,k>V\\Y<mk\le X}}
 \frac{\Lambda(m)b_V(k)}{\sqrt{mk}}(mk)^{it}.
\tag{5}
\]
本稿不给 \(m\) 与 \(k\) 增加互素前件，所有 aspect ratios 保留。

## 2. 平方丰满 r≥2 的精确 Euler 身份

暂在 \(\Re w>1\)，各无限级数绝对收敛。对固定 squarefull \(r\) 置
\[
 F_{V,r}(w)=\prod_{p\mid r}(1+p^{-w})^{-1}
 \sum_{\substack{e\mid\operatorname{rad}(r)\\e\le V}}\mu(e)
 \sum_{\substack{a\le V/e\\a\ {\rm squarefree},\ (a,r)=1}}
 \mu(a)a^{-w}\prod_{p\mid a}(1+p^{-w})^{-1}.
\tag{6}
\]
这里 \(e\) 是来自 \(r\) 的真实 Möbius divisor，\(a\) 是来自 \(s\)
的真实 divisor；准确条件 \(ae\le V\) 没有换成独立矩形。
完整401源(18)—(20)的逐素数证明直接给
\[
 \sum_{\substack{s\ {\rm squarefree}\\(s,r)=1}}
 b_V(sr)s^{-w}=\frac{\zeta(w)}{\zeta(2w)}F_{V,r}(w).
\tag{7}
\]
具体写 \(s=a\ell\)、\((\ell,ar)=1\)，其 Euler 乘积为
\(a^{-w}\zeta(w)/\zeta(2w)\prod_{p\mid ar}(1+p^{-w})^{-1}\)。

定义有限、但含全部局部因子的
\[
 C_{\ge2}(w)=\sum_{\substack{2\le r\le H\\r\ {\rm squarefull}}}
                     r^{-w}F_{V,r}(w).
\tag{8}
\]
每个 \(2\le k\le V\) 都满足 \(b_V(k)=0\)。\(r\ge2\) 又不可能
产生 \(k=1\)，所以扣去 \(k\le V\) 不产生任何 \(-1\)：
\[
 B_{\ge2}(w):=\sum_{\substack{k>V\\2\le r(k)\le H}}b_V(k)k^{-w}
             =\frac{\zeta(w)}{\zeta(2w)}C_{\ge2}(w).
\tag{9}
\]
这对每个精确整数 \(V,H\) 成立，不是被估计为小的常数项。
相反，\(r=1\) 的实际生成函数严格为
\[
 B_{\rm sf}(w)=\sum_{\substack{k>V\\k\ {\rm squarefree}}}b_V(k)k^{-w}
             =\frac{\zeta(w)}{\zeta(2w)}F_{V,1}(w)-1.
\tag{10}
\]

## 3. 全部有限局部因子的统一绝对界

取 \(c=1/L\)。对于 \(\sigma=\Re w\ge1/2+c\)，以及每个先固定
\(\eta>0\)，有
\[
 \prod_{p\mid n}|1+p^{-w}|^{-1}
 \le\prod_{p\mid n}(1-p^{-1/2})^{-1}\ll_\eta n^\eta.
\tag{11}
\]
证明：大于某个固定阈值的素数满足
\(-\log(1-p^{-1/2})\le\eta\log p\)；有限小素数只添固定常数。
\((a,r)=1\) 使(6)两个产品正好由 \(ar\) 的不同素因子控制。
直接保留所有 \(e,a\) 得
\[
 |F_{V,r}(w)|\ll_\eta r^\eta\tau(r)V^{1/2+\eta},
 \qquad \sigma\ge1/2+c,
\tag{12}
\]
因为每个 \(e\) 的内层绝对质量至多
\(V^\eta\sum_{a\le V/e}a^{-1/2}\ll V^{1/2+\eta}\)，
而 \(e\) 的数量至多 \(\tau(r)\)。未消费一个未证的带依赖权 Möbius twist。

squarefull \(r\) 每个 dyad 的 \(\sum r^{-1/2}\) 为 \(O(1)\)，
由唯一 \(r=a^2b^3\) 表示证明。因此对 \(H\le X\)，将所有固定
divisor 损失分配后，任意最终 \(\epsilon>0\) 有
\[
 \boxed{|C_{\ge2}(w)|\ll_\epsilon\sqrt V X^\epsilon L^C,
                       \qquad\sigma\ge1/2+c.}
\tag{13}
\]
这是全部 \(2\le r\le H\)、全部真实 \(ae\le V\) 的共同绝对界。
每个分母 \(1+p^{-w}\) 的零点都在 \(\Re w=0\)，所以有限 \(C_{\ge2}\)
在 \(\Re w>0\) 解析。

## 4. 真正 prime 与 proper powers 的两个消极点生成函数

置
\[
 A_U(w)=\sum_{p>U}(\log p)p^{-w},\quad
 F_U^{\rm prime}(w)=\sum_{p\le U}(\log p)p^{-w},
\]
\[
 Q_{\rm pp}(w)=\sum_p\sum_{j\ge2}(\log p)p^{-jw},\quad
 Q_{>U}(w)=\sum_{\substack{p^j>U\\j\ge2}}(\log p)p^{-jw}.
\tag{14}
\]
proper powers 的系列在每个 \(\sigma>1/2\) 局部一致绝对收敛。
在所用 \(\sigma\ge1/2+c\) 上，放大素数到整数给
\[
 |Q_{>U}(w)|\le Q_{\rm pp}(\sigma)\ll c^{-2}\ll L^2,
 \quad |\zeta(2w)^{-1}|\le\zeta(2\sigma)\ll L,
 \quad |F_U^{\rm prime}(w)|\ll\sqrt U L.
\tag{15}
\]
这里使用绝对 Euler 乘积，均不需要无零前件。

\(\Re w>1\) 的准确身份为
\[
 A_U(w)=-\zeta'(w)/\zeta(w)-Q_{\rm pp}(w)-F_U^{\rm prime}(w).
\]
于是原负 genuine-prime 系数、全部 \(2\le r(k)\le H\) 的生成函数为
\[
 \mathcal H_{\ge2}(w)=-\frac{A_U(w)B_{\ge2}(w)}{a_LL}
 =\frac{[\zeta'(w)+(Q_{\rm pp}(w)+F_U^{\rm prime}(w))\zeta(w)]
             C_{\ge2}(w)}{a_LL\zeta(2w)}.
\tag{16}
\]
它保持全部 genuine \(m>U\)，不要求 \(m>A\)，也不要求 \((m,k)=1\)。
右式准确消掉 \(\zeta'/\zeta\) 的零点极点。

另一完整原子族是所有 proper-power \(m>U\)、全部 \(k>V\)。
\(\zeta(w)G_V(w)-1\) 的 \(k\le V\) 系数全零，其中
\(G_V(w)=\sum_{d\le V}\mu(d)d^{-w}\)。故它的原负生成函数为
\[
 \mathcal H_{\rm pp}(w)=-\frac{Q_{>U}(w)(\zeta(w)G_V(w)-1)}{a_LL}.
\tag{17}
\]
这里 \(Q_{>U}\) 是完整 infinite proper-power 因子，没有截去 \(m>X\)
以后未付款的尾。两式首先是初线的实际 Dirichlet 系数身份，
然后才在 \(\Re w>1/2\) 续延；\(\zeta\) 在1的 pole保持。

## 5. 无限初线 Perron：两半整数端点与完整远尾

记 \(s_0=1/2-it\)、\(K=T/8\)、\(\kappa=1/2+c\)，
\(x^\sharp=\lfloor X\rfloor+1/2\)、\(y^\sharp=\lfloor Y\rfloor+1/2\)。
它们分别保持 \(n\le X\)、\(n\le Y\) 的整数集合。
写任一(16)、(17)初线系列为 \(\mathcal H(w)=\sum h_n n^{-w}\)。
对全部 \(n\ge1\)，原系数的正绝对上界统一为
\[
 |h_n|\ll_\phi\frac{\log(2n)}L\tau_3(n).
\tag{18}
\]
由 \(|b_V(k)|\le\tau(k)\)、\(\Lambda(m)\le\log(2n)\)
与 \(\sum_{m\mid n}\tau(n/m)=\tau_3(n)\) 直接证明，所有原 masks 保持。

初线 \(\Re(s_0+z)=1+c\) 绝对收敛。
标准单系数截断 Perron 误差因子为
\(\min(1,[K|\log(x/n)|]^{-1})\)。因此在每个
\(x=x^\sharp,y^\sharp\) 上须支付
\[
 \sum_{n\ge1}|h_n|n^{-1/2}(x/n)^\kappa
            \min\{1,(K|\log(x/n)|)^{-1}\}.
\tag{19}
\]
先在 \(x/2<n<2x\) 用固定 divisor 界；半整数距离至少 \(1/2\)，
且 \(|\log(x/n)|\gg|n-x|/x\)。harmonic 求和给
\(O_\eta(X^\eta\sqrt x K^{-1}L^C)\)，统一于两个端点。

在两侧远域仅用 \(|\log(x/n)|\ge\log2\) 和准确绝对 Dirichlet 级数：
\[
 \sum_{n\ge1}\tau_3(n)\log(2n)n^{-1-c}
 =-(\zeta^3)'(1+c)+\log2\,\zeta(1+c)^3\ll c^{-4}.
\tag{20}
\]
于是完整远尾最多 \(x^\kappa K^{-1}L^C\ll X^{-1/2}L^C\)。
这里的权是 \(n^{-1-c}\)，不能误写为 \(n^{-3/2-c}\)，
更不能把 \(n^\eta\) divisor 界使用到无限远端，因为 \(c=1/L<\eta\)。
从(19)—(20)严格得到
\[
 \sum_{Y<n\le X}h_n n^{-s_0}
 =\frac1{2\pi i}\int_{\kappa-iK}^{\kappa+iK}
       \mathcal H(s_0+z)\frac{(x^\sharp)^z-(y^\sharp)^z}{z}\,dz
       +O_{\phi,\eta}(X^{-1/2+\eta}L^C).
\tag{21}
\]
整个 \(n>X\) 的初线尾已付，不以有限系数删除代替这个步骤。

## 6. 移到真实 1/2+c：没有零点留数遗漏

把(21)的矩形移到 \(\Re z=c\)。所有所见
\(t-\Im z\in[T/8,33T/8]\)，仍是原正 guard。
由(16)、(17)的右式，矩形内函数解析：\(Q\) 的系列绝对收敛，
\(\zeta(2w)\) 在 \(\Re w>1/2\) 无零，有限局部因子在 \(\Re w>0\) 解析。
\(\zeta\)、\(\zeta'\) 唯一的 pole1在零高度，guard排除它。
\(z=0\) 也没有跨过。所有未知普通 \(\zeta\) 零点均已由(16)准确消极点，
不是被无零假设排除或删除留数。

水平段还要付款。无需增加新的 convexity 引用：505源§3的固定
\(N=\lfloor10T\rfloor\) Euler/Abel证明，在任意固定紧实部区间
\([1/2,5/4]\) 同样逐式成立，所有积分常数只依该固定区间。
完整尾仍为 \(O(T^{-\sigma})\)。有限 \(W_N\) 的绝对和直接给
\[
 |\zeta(\sigma-i\tau)|\ll T^{\max(1-\sigma,0)}L,
 \quad |\zeta'(\sigma-i\tau)|\ll T^{\max(1-\sigma,0)}L^2,
\tag{22}
\]
统一于 \(1/2+c\le\sigma\le1+c\)、\(T/8\le\tau\le33T/8\)。
第二式在同一个固定 \(N\) 上以半径 \(c/2\) 作 Cauchy；
圈实部至少 \(1/2+c/2\)、高度仍在 \([T/9,5T]\)，
\(T^{c/2}=O(1)\)，只添一个 \(L\)。

结合(13)、(15)及 \(|G_V|\ll\sqrt V\)，水平线上两函数都满足
\[
 |\mathcal H(w)|\ll_\epsilon\sqrt{UV}X^\epsilon
                    T^{\max(1-\sigma,0)}L^C.
\]
核最多 \(C X^{\sigma-1/2}/T\)。对 \(\sigma\le1\)，它与(22)的
\(T^{1-\sigma}\) 相乘为 \(O(X^{-1/2})\)；对 \(1\le\sigma\le1+c\)
只再付 \(X^c=O(1)\)。两段有限水平线的总费用因此为
\[
 O_\epsilon(X^{-1/2+v+\epsilon}L^C).
\tag{23}
\]
固定 \(v<1/4\) 后是负幂；左右两端 Perron 均已包含。

## 7. 共享外 Perron 的第四均值与实际新子域

505源已核读的 [Montgomery–Vaughan 原书 Theorem26.23](https://personal.science.psu.edu/rcv4/Vol3/Vol3.pdf)
给 \(\sigma=1/2+c\) 及其 \(c/2\) 圈上的统一 \(\zeta\) 第四均值。
沿其§2 Cauchy推导，对全部 \(|\omega|\le K\) 有
\[
 \|\zeta(1/2+c-i(t-\omega))\|_{4,T}\ll L,
 \quad \|\zeta'(1/2+c-i(t-\omega))\|_{4,T}\ll L^2.
\tag{24}
\]
其余因子用(13)、(15)的真正同一移位点值界。因此
\[
 \sup_{|\omega|\le K}\|\mathcal H_{\ge2}(1/2+c-i(t-\omega))\|_{4,T}
                  \ll_\epsilon\sqrt{UV}X^\epsilon L^C,
\]
\[
 \sup_{|\omega|\le K}\|\mathcal H_{\rm pp}(1/2+c-i(t-\omega))\|_{4,T}
                  \ll_\epsilon\sqrt V X^\epsilon L^C.
\tag{25}
\]
这里使用的是 \(\zeta'\) 自身的第四均值，而非 \(|\zeta\zeta'|^2\)。

核 \(((x^\sharp)^z-(y^\sharp)^z)/z\) 在 \(z=c+i\omega\) 的绝对
积分为 \(O(L)\)。一次共享 \(\omega\) 的 normalized \(L^4\) Minkowski，
连同(21)、(23)完整误差，故对原两个 signed 子族自身证明
\[
 Q_{\ge2}(t)=-\frac1{a_LL}
 \sum_{\substack{m>U\ {\rm prime},\ k>V\\2\le r(k)\le H\\Y<mk\le X}}
 \frac{\Lambda(m)b_V(k)}{\sqrt{mk}}(mk)^{it},
 \quad \boxed{\mathcal M_{Q_{\ge2}}\ll X^{4v+\epsilon}},
\tag{26}
\]
\[
 Q_{\rm pp}^{\rm full}(t)=-\frac1{a_LL}
 \sum_{\substack{m>U\ {\rm proper\ prime\ power},\ k>V\\Y<mk\le X}}
 \frac{\Lambda(m)b_V(k)}{\sqrt{mk}}(mk)^{it},
 \quad \boxed{\mathcal M_{Q_{\rm pp}^{\rm full}}\ll X^{2v+\epsilon}}.
\tag{27}
\]
所有允许 \(m,k\)、\(m\mid k\)、\(r\) dyads、\(s(k)\) 大小和乘积端点保留。
两项都不由较大 signed 函数的范数对子族作单调推断，也不使用 \([R_\theta]\)。

## 8. 完整新账本及平方自由主项

原 \(C_4\) 精确、不交分成
\[
 C_4=Q_{\rm pp}^{\rm full}+Q_{>H}^{\rm prime}+Q_{\ge2}+R_{\rm sf},
\tag{28}
\]
其中 \(Q_{>H}^{\rm prime}\) 保持全部 genuine \(m>U\)、\(r(k)>H\)，
完整401源的尾证明对 \(M_0=U\) 同样逐式成立，费用
\(X^\epsilon(1+X/H^2)\)。剩余准确是
\[
 \boxed{R_{\rm sf}(t)=-\frac1{a_LL}
 \sum_{\substack{m>U\ {\rm prime},\ k>V\ {\rm squarefree}\\Y<mk\le X}}
 \frac{\Lambda(m)b_V(k)}{\sqrt{mk}}(mk)^{it}.}
\tag{29}
\]
\(m,k\) 不添加互素条件。\(r=1\) 与 squarefree \(k\) 完全等价。
新的 \(U,V,Y\) 配置不是486余项的子集；没有搬用其 signed 范数。

原 \(P_H\) 到 \(\Lambda\) scalar 的 proper-power 迁移仍为 polylog 费用：
甚至可直接以 \(\sum_{p^j\le X,j\ge2}\log p/\sqrt{p^j}\ll L^2\) 的
绝对和证明，无须新零点假设。低段由原实际平方多项式二矩给
\(X^{\max(0,2y-1)+\epsilon}\)。505源长有限因子 Type I 的完整费用
仍为 \(X^{4v+\epsilon}\)，它保留原 \(g_{U,V}\)、\(\mu\) 和两 sharp cuts。

先将这些完整函数合成 \(E_{\rm sf}=P_H-R_{\rm sf}\)，一次 \(L^4\)
Minkowski 给新的实际误差表
\[
 C=\max\{2y-1,\ 4v,\ 2v,\ 1-4v,\ 0\}.
\tag{30}
\]
它删除旧费用表的 short-\(m\) 和 large-proper-power 条目，原因是(26)—(28)
的完整新算术付款，不是未付款子族的剪裁。
选择
\[
 U=V=\lfloor X^{1/8}\rfloor,\quad H=V^2,\quad Y=X^{3/4}
\tag{31}
\]
时 \(UV<Y\)，五项指数为 \((1/2,1/2,1/4,1/2,0)\)，证明(1)。
\(V\ge X^{1/8}/2\)、\(H\ge X^{1/4}/4\) 支付全部 floors。
这个费用族仍有 \(\max(4v,1-4v)\ge1/2\)；不声称所有算术方法的最优性。

## 9. 完整传递与保留的平方自由零点包

仅在本节接受476的完整同函数 \(\mathcal M_{P_H}\ll X^{5/7+\epsilon}\)
及其原 \([R_{7/8}]\) 合同。由(1)先用 Minkowski 得
\(\mathcal M_{R_{\rm sf}}\ll X^{5/7+\epsilon}\)，然后两个完整函数满足
\[
 |\mathcal M_{P_H}-\mathcal M_{R_{\rm sf}}|
 \ll\|E_{\rm sf}\|_{4,T}(\|P_H\|_{4,T}+\|R_{\rm sf}\|_{4,T})^3.
\]
严格指数为 \((3(5/7)+1/2)/4=37/56\)，距原 \(5/7\) 为 \(3/56\)，
相对486传递 \(159/238\) 节省 \(1/136\)。证明(2)，不声明未知主项的相对渐近。

由(10)，平方自由主项的未归一化生成函数是
\(-A_U(w)B_{\rm sf}(w)\)。每个 \(\Re\rho>1/2\) 的 \(\zeta\) 零点处，
\(F_{V,1}\) 和 \(1/\zeta(2w)\) 解析，故 \(B_{\rm sf}(\rho)=-1\)，
\(\operatorname{Res}_{w=\rho}A_U=-m_\rho\)。于是仍准确有
\[
 \operatorname{Res}_{w=\rho}[-A_U(w)B_{\rm sf}(w)]=-m_\rho.
\tag{32}
\]
同一两端 Perron 若跨过该零点，其核仍为
\(-m_\rho[(x^\sharp)^{\rho-s_0}-(y^\sharp)^{\rho-s_0}]/(\rho-s_0)\)。
本稿消去的是完整 \(r\ge2\) 子域的极点，不给 \(r=1\) 留数减幅。
尚未付款的实际核心恰为(29)全部 prime/squarefree 联合 mixed4。
新误差仍增长为 \(X^{1/2+\epsilon}\)，不是常数级 \(o(1)\)。
项目已准入比例、引用输入下既有无零边界与完整增长基线均保持；
不得由本次子域付款或传递宣布新纪录论文。
