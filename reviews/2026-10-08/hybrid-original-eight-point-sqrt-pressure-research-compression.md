# 原八点平方根压力的有限准入与实际计数缩约

2026-10-08。作者 compression。基线 main f20c94b。
只新增本稿，不修改旧证书、数学论文、源文件或 Git。

本稿支付原有限 Gram 的平方根带能量包络、非均匀压力的完整全链端项，
以及修改后的正偶单位窗接回304实际全复零点算子的接口。
它们不需要 RH、全 Weil 正性、常数级四矩或新的零点相关假设。
外部 AM 八点全域证书本轮没有完整重放，故本稿**没有新增项目实际比例**；
当前479的 \(p_{\rm dg}=0.673058110281973\ldots\) 保持。
下面给出精确条件公式及可复核的唯一剩余有限准入目标。

## 1. 来源、计数口径与本轮范围

原合同取[304 §5](../../notes/304-mt-triple-geometry-and-second-moment-stability.md)，
canonical LF SHA256
03f21ab1749157ff45bc4d4f62709e2a5482257c7155e7e8e644da0ac4521bc4；
原计数/惯性取[477作者源](hybrid-original-multipoint-envelope-and-actual-counting-research-compression.md)，
59b399445a3022ce9b5ee6c064660e1602dab6d5641d3793649f16f509fc5efa。
已完整读[477](../../notes/477-original-vaughan-reduction-and-replayed-multipoint-proportion.md)、
[478](../../notes/478-original-mt-six-neighbor-dual-and-whole-chain-proportion.md)、
[479](../../notes/479-original-type-ii-factor-reduction-and-diagonal-gauge.md)及
[公开前沿审计](../../literature/supplements/2026-10-08-proportion-frontier-audit.md)。
其当前 canonical hashes 依次为
9c2da25b665070fe5496b9b02cbe382208cd3b60dc793af1ae018ede395bd6b5，
6ab8384289cf7470b7ee448e381f5e9afdd268b13852f95322c98c1a62dd5c54，
6b6e15f8a3a83d62e1d472cbeaa86a894c9e01740ccd682fc79ec99c2ec5a559，
a84e418e5540dc4694740515680bc8b8287f05d94bbf9a90eccd80721abedabd。

外部固定来源为
[josusanmartin/riemann，d272437 的 Solution.lean](https://github.com/josusanmartin/riemann/blob/d272437e7ebeb17b87c8c3d7cece592aa23785ab/submissions/dani-bound-2026/proof/Solution.lean)。
实际核读了窗定义75–127、WCert5142–5157、带包络6528–6979、
实际简单计数7128–7176，以及最终证书入口/参数18686–19011的相关段落。
这里的机制已有公开先行来源，不声称新颖性或世界纪录。
未声称全文审完19044行、5651个叶子、完整依赖或运行过 Lean/nanoda。
后面的推导是独立数学证明；外部最后的全域数值前件仍明确保留。

\(N(T)\) 计所有 \(0<\Im\rho\le T\) 非平凡零点及重数，
\(s(T)\) 计简单临界线零点，\(D(T)\) 计不同零点。
本稿直接用304前缀接口；没有把不同临界线计数反推为简单计数。

## 2. 原非负 Gram 的带能量平方根包络 [T]

设 \(G\succeq0\) 为有限 Hermitian Gram，给行列注入整数 rank。
固定整数 \(q\ge1\)，令 \(K\) 保留 \(G\) 中满足
\(0<|r_i-r_j|\le q\) 的条目，其余置零。定义
\[
 E=\operatorname{Tr}K^2\ge0,\qquad \tau=(q+1)/q,
 \quad j(t)=(t-1)^2-(t-2)_+^2\quad(t\ge0),
 \quad J(G)=\operatorname{Tr}j(G).
 \tag{1}
\]
\(j\) 非负、凸，在非负轴上2-Lipschitz。
对任意单位向量 \(v\)，Cauchy 给
\[
 |v^*Kv|^2\le E\sum_{0<|r_i-r_j|\le q}|v_i|^2|v_j|^2
 \le E\left(1-\sum_{a=0}^q p_a^2\right)\le E/\tau,
 \quad p_a=\sum_{r_i\equiv a\pmod{q+1}}|v_i|^2.
 \tag{2}
\]
同一 residue class 内没有带边，\(\sum p_a=1\)；故
\(\|K\|_{\rm op}\le\sqrt{E/\tau}\)。它保留实际 Gram 的行序，
不把有限载体换成频率环面，也不需要单位对角。

任意 Hermitian \(B\preceq I\) 满足
\[
 J(G)\ge2\operatorname{Tr}B(G-I)-\operatorname{Tr}B^2.
 \tag{3}
\]
证明：在 \(G\) 本征基上，\(b_{ii}\le1\)，
\(\operatorname{Tr}B^2\ge\sum b_{ii}^2\)；逐个最大化
\(2b(t-1)-b^2\)（\(b\le1,t\ge0\)）恰给 \(j(t)\)。
若 \(E>0\)，取 \(B=\alpha K\)，
\(\alpha=\min\{1,\sqrt{\tau/E}\}\)。由(2)可行，且
\(\operatorname{Tr}K(G-I)=E\)，故
\[
 \boxed{J(G)\ge f_\tau(E)},\qquad
 f_\tau(E)=\begin{cases}E,&0\le E\le\tau,\\
                       2\sqrt{\tau E}-\tau,&E>\tau.\end{cases}
 \tag{4}
\]
\(E=0\) 由 \(J\ge0\) 单独处理。
\(f_\tau\) 连续、递增、1-Lipschitz，\(0\le f_\tau(E)\le E\)。
第二段导数 \(\sqrt{\tau/E}\le1\)；第一段导数1。
这正是外部平方根带机制在原 \(J\) 上的合法有限版本。

## 3. 任意非均匀压力的完整全链证明 [T]

给 \(q+1\) 个局部点，令 \(a_{ij},b_r\ge0\)，并要求每个 index span
\[
 \sum_{i=0}^{q-h}a_{i,i+h}\le2\quad(1\le h\le q).
 \tag{5}
\]
设 \(f\) 为支撑在 \([-1/2,1/2]\) 的实偶概率密度，
\(k=\widehat f\)。对所有非负 gaps 假定一个**全域**证书
\[
 \sum_{r=0}^{q-1}b_rg_r+
 \sum_{0\le i<j\le q}a_{ij}k(x_j-x_i)^2\ge c>0,
 \quad x_0=0,\ x_j=\sum_{r<j}g_r.
 \tag{6}
\]
令 \(B_0=\sum b_r\)、\(m\ge q+1\)、\(A=c(m-q)\)、
\(F=f_\tau(A)\)，并要求 \(F<m\)。
对任意有序 \(m\) 点 \(y_0\le\cdots\le y_{m-1}\)，
将(6)在全部 \(m-q\) 个连续局部窗口相加。
由(5)，每个全局无向带边总系数不超过2；压力恰为
\[
 P_m(y)=\sum_{r=0}^{q-1}b_r(y_{m-q+r}-y_r)\ge0,
 \quad A\le E_q(y)+P_m(y).
 \tag{7}
\]
压力的 telescoping 精确，不是把最大 \(b_r\) 乘跨度。
由(4)和1-Lipschitz，若 \(P_m\le A\)，
\(f_\tau(A)\le f_\tau(E_q)+P_m\)；若 \(P_m>A\)，
由 \(F\le A\)、\(J\ge0\) 得到同样结论。因此
\[
 J(G_y)+P_m(y)\ge F.
 \tag{8}
\]

现在给全部 \(s\) 个有序点。对 \(m\) 个 residue offsets，
各自分成所有完整连续 \(m\) 点主块和剩余端块。
在每个主块的本征基及端块本征基上，标量 Jensen 给
全 \(J\) 不小于主块 \(J\) 之和；不使用 operator convexity。
合计每个起点 \(t=0,\ldots,s-m\) 恰出现一次。
由(7)，每个全局 gap 在固定 \(r\) 的压力中至多出现 \(m-q\) 次，故
\[
 \sum_{t=0}^{s-m}P_m(y_{t:t+m})
       \le B_0(m-q)(y_{s-1}-y_0).
\]
设 \(\operatorname{span}=0\) 当 \(s\le1\)。于是对所有 \(s\)，包括 \(s<m\)，
\[
 \boxed{J(G)\ge \frac Fm s-
       \frac{B_0(m-q)}m\operatorname{span}-\frac{F(m-1)}m.}
 \tag{9}
\]
满块数是 \((s-m+1)_+\)；最后常数由此精确得到。
没有丢失 \(q\) 个局部窗口端项，也没有为每个小簇另付常数。
\(J\) 总是在这个 \(s\times s\) Gram 上计算；环境补零不另计 \(j(0)\)。

## 4. 固定平滑与同一实际有限算子 [T/R]

取固定实偶 \(\eta_\delta\in C_c^\infty((-1/2,1/2))\)，
\(\int\eta_\delta^2=1\)，令 \(f_\delta=\eta_\delta^2\to f\) 于 \(L^1\cap L^2\)。
记 \(\varepsilon_\delta=\|f_\delta-f\|_1\)，则实轴全域
\(\sup|k_\delta-k|\le\varepsilon_\delta\)，两核模均至多1。
每个平方条目误差至多 \(2\varepsilon_\delta\)，
有向带边不超过 \(2qm\)，故每块带能量误差至多
\(4qm\varepsilon_\delta\)。由(8)给实际块增益
\(F-4qm\varepsilon_\delta\)，先固定 \(\delta\) 使它为正。
同一全链证明给
\[
 J(G_{\delta,T})\ge(\alpha-4q\varepsilon_\delta)s(T)
                  -\eta X_T-O_m(1),
 \quad \alpha=F/m,\quad \eta=B_0(m-q)/m,
 \quad X_T=\frac{T\log T}{2\pi}.
 \tag{10}
\]
误差是稀疏带边费用；无需增长维数的稠密 Gram 扰动定理。

304§5对每个固定 \(\delta\) 的两个固定函数
\(Q_\delta=f_\delta*f_\delta\)、\(Q_\delta''\) 去相关权，给原全复零点算子
\[
 \operatorname{Tr}A_{\delta,T}=N(T),\qquad
 \|A_{\delta,T}\|_{\rm HS}^2=(R_\delta+o_\delta(1))N(T),
 \quad R_\delta\to R(f),
\]
\[
 R(f)=\int f(u)^2du+
       \iint |u-v|f(u)f(v)\,du\,dv.
 \tag{11}
\]
这一步保留全部离线共轭对 \(2m(g_z\otimes g_z-h_z\otimes h_z)\)，
不是宣称 \(A\) 正半定。简单临界线列
\(\eta_\delta(u)e^{-2\pi ixu}\) 精确单位，其 Gram 恰为 \(k_\delta(x_i-x_j)\)，
全部位置的跨度至多 \(X_T\)，\(X_T/N(T)\to1\)。

写 \(A=P+Q\)，\(P\) 为简单单位列和，\(n_+(Q)\le b\)。
477§2的有限 minmax 证明给
\[
 4\operatorname{Tr}A-\|A\|_{\rm HS}^2\le4b+3s-J(G).
\]
在环境补零后，前 \(b\) 个谱用 \(4t-t^2\le4\)，
余谱用 \(\lambda_{b+i}(A)\le\lambda_i(P)\) 及
\(4t-t^2\le2p+1-j(p)\)（\(t\le p,p\ge0\)）；其余环境零贡献至多0。
实际重数账本 \(N\ge s+2b\)、\(D\ge s+b\) 因而给
\[
 s\ge2N-\|A\|_{\rm HS}^2+J(G),\qquad
 2D\ge3N-\|A\|_{\rm HS}^2+J(G).
 \tag{12}
\]
把(10)插入(12)，固定足够小 \(\delta\)，先 \(T\to\infty\)，最后 \(\delta\to0\)，得
\[
 \boxed{\liminf\frac{s(T)}{N(T)}\ge
 p(f,c,B_0,m):=\frac{2-R(f)-B_0(m-q)/m}{1-f_\tau(c(m-q))/m}.}
 \tag{13}
\]
当分子为正，第二式给 \(\liminf D/N\ge(1+p)/2\)。
等式化简用 \((1-\alpha)p=2-R-\eta\)；
不是免费使用普遍不成立的 \(D\ge(N+s)/2\)。
所有profile及 \(m\) 均先固定，没有 \(\delta(T)\) 或复增长带一致逼近前件。
这里已给实际前缀合同，未证明任意新窗的 AF 未归一化 S1 尾合同；
该额外 dyadic Gabor 接口不为(13)所需。

## 5. AM13自身的正密度、归一化与二矩 [T/R]

令 \(I=[-1/2,1/2]\)、\(\beta=1/\sqrt2\)、\(Z_0=\sqrt2\sin\beta\)，
\[
 v(u)=\cos(\sqrt2u)+\sum_{j=1}^{12}c_j\cos(2\pi ju),
 \qquad f_{\rm AM}(u)=\frac{v(u)}{Z_0}1_I(u).
 \tag{14}
\]
系数 \(c_j\) 的分母均为 \(10^9\)，分子依次为
\[
 (12310798,-15041681,3867664,6489926,-992327,5580097,
 -6846472,3781297,-5670353,3355089,-450523,-218483).
\]
\(\sum|c_j|=6460471/10^8<13/200\)。在 \(I\) 上
\(\cos(\sqrt2u)\ge1-u^2\ge3/4\)，故 \(v\ge137/200>0\)。
所有整数余弦的积分为0，\(\int_Iv=Z_0>0\)，因此它是正偶概率密度。
外部缩放 \(M_{\rm AM}=5/4\) 只保证未归一化窗上界；
除去真实质量后它完全消去，不应另乘进 \(R\)。
核必须为 \(\int_Ive^{-2\pi ixu}du/Z_0\)，不能除 \(v(0)\)。

固定偶 cutoff \(w_\delta\to1\)，取
\(\eta_\delta=\sqrt v\,w_\delta/\sqrt{\int_Iv w_\delta^2}\)。
它光滑、实偶、紧支撑且单位范数，\(\eta_\delta^2\to f_{\rm AM}\) 于 \(L^1\cap L^2\)，
所以第4节的原域、原全复零点接口确实覆盖此窗。

为独立计算自身 \(R\)，设 \(\mathcal Tf=f+\int_I|u-v|f(v)dv\)。
MT 的 \(f_0=\cos(\sqrt2u)/Z_0\) 满足
\((\mathcal Tf_0)''=f_0''+2f_0=0\)，偶性使 \(\mathcal Tf_0\) 为常数。
置 \(h=f_{\rm AM}-f_0\)，\(\int h=0\)，故交叉项 \(\langle h,\mathcal Tf_0\rangle=0\)。
对 \(j\ge1\)，同样求二阶导数和用偶性给
\[
 \mathcal T\cos(2\pi ju)=
       \left(1-\frac1{2\pi^2j^2}\right)\cos(2\pi ju)+\text{常数}.
\]
整数余弦互相正交，平方积分 \(1/2\)，故准确有
\[
 R_{\rm AM}=R_0+D_{\rm AM},\qquad
 D_{\rm AM}=\frac{\sum_{j=1}^{12}c_j^2
                  (1/2-1/(4\pi^2j^2))}{2\sin^2\beta},
 \quad 2-R_{\rm AM}=C_0-D_{\rm AM}.
 \tag{15}
\]
其中 \(C_0=3/2-\beta\cot\beta\) 为原冻结常数。
所以新窗付出真实二矩损失，绝不与原 MT 的 \(C_0\) 拼接。

## 6. 八点权与明确的唯一未付款项

八点令 \(q=7\)。以下上三角每行依次列 \(a_{i,i+1},\ldots,a_{i,7}\)，
全部分母 \(10^8\)：

~~~text
13630830 0        19565904 20317441 45030671 100000000 200000000
29997996 30621878 47766489 79682558 109938656 100000000
37356140 69378121 65335210 79682558 45030671
38030065 69378121 47766489 20317441
37356140 30621878 19565904
29997996 0
13630830
~~~

压力分子为 \((28898,57272,75526,80958,75526,57272,28898)\)，同分母。
故 \(B_0=404350/10^8\)、\(b_{\min}=28898/10^8>0\)。
精确 span capacities 为
\[
 (199999997/10^8, 99999999/(5\cdot10^7),
 49999999/(25\cdot10^6), 99999999/(5\cdot10^7),
 99999999/(5\cdot10^7), 2, 2),
\]
均不超过2，故第3节前件(5)已付。

剩余 **[O：本项目未重放的有限证书]** 是针对自身 AM 核的
\[
 F_{W_8,\rm AM}(g)\ge c:=805003/10^8
             \quad\text{对全部 }g\in[0,\infty)^7.
 \tag{16}
\]
固定外部入口为 cert_AM → PC8CL_cert_full；其叶表、
反射半域、根盒、区间核/导数表和覆盖正确性仍须整体核验。
本轮只核读入口与部分证明链，没有把作者文件中的 theorem 名称当执行 PASS。
正压力使 \(g_r\ge c/b_r\) 的部分自动成立；其余可限于
\(\prod_r[0,c/b_r]\)。权表在反射 \(g_r\mapsto g_{6-r}\) 下对称，
允许进一步取 \(g_6\ge g_0\)，但这不能代替剩余七维覆盖。
不能用有限采样、单个优化点、旧 MT 七点域或平台验证介绍支付(16)。

## 7. 条件数值是自身预算的精确有理推论 [T]

对(16)取 \(m=152\)、\(\tau=8/7\)，
\(A=c(m-7)=116725435/10^8\)。
已冻结[477有理输出](../../output/hybrid-multipoint-cap-exact-algebra.json)
canonical LF SHA256
d84077ab71b47d1ea253cad9675fa8c25f9aa4dade775ad73ff53033167625c3
给 \(C_0\) 的严格下端
\[
 C_{0,-}=\frac{228840131204026865023004118089085809487}
                  {340282366920938463463374607431768211456}.
\]
自行用 Machin \(\pi=16\arctan(1/5)-4\arctan(1/239)\) 的交错 Taylor，
第一项取至 \(n=4\) 的上界、第二项至 \(n=1\) 的下界，得到
\(\pi<5277328977275528/1679825970703125\)。
由 \(\cos\sqrt2\) 至 \(n=6\) 的上界，
\(2\sin^2\beta=1-\cos\sqrt2>180493/213840\)。
在(15)分子用该 \(\pi\) 上界、分母用该正下界，精确 Fraction 核算给
\[
 2-R_{\rm AM}>67216841/10^8.
 \tag{17}
\]
这是独立证明，不把外部 HW_ge 的字面数值作为新前件。
同时
\((1154991329/10^9)^2<(8/7)A\)，故
\(F>4084939303/3500000000\)、\(F\le A<152\)。
由(13)，**本项目仅在(16)另行核准后**，才可采用保守有理下界
\[
 p\ge\frac{118513839290}{175971686899}
       >\frac{6734824}{10^7}.
 \tag{18}
\]
最后差准确为 \(6581516153/219964608623750000>0\)。
这不是当前项目实际比例声明；它比(16)本身的验证容易，不能用来倒证(16)。

以下本机自写有限代码已实际执行，无外部代码执行、文件写入或浮点比较判定：

~~~python
from fractions import Fraction as Q
from math import factorial
C0lo = Q(228840131204026865023004118089085809487,
         340282366920938463463374607431768211456)
cs = [Q(v,10**9) for v in [12310798,-15041681,3867664,6489926,
 -992327,5580097,-6846472,3781297,-5670353,3355089,-450523,-218483]]
assert sum(map(abs,cs)) == Q(6460471,10**8) < Q(13,200)
rows = [[13630830,0,19565904,20317441,45030671,100000000,200000000],
 [29997996,30621878,47766489,79682558,109938656,100000000],
 [37356140,69378121,65335210,79682558,45030671],
 [38030065,69378121,47766489,20317441],
 [37356140,30621878,19565904],[29997996,0],[13630830]]
bs = [Q(v,10**8) for v in [28898,57272,75526,80958,75526,57272,28898]]
for s in range(1,8):
    assert sum((Q(rows[i][s-1],10**8) for i in range(8-s)),Q(0)) <= 2
assert sum(bs) == Q(404350,10**8)
api5 = sum((Q((-1)**n,(2*n+1)*5**(2*n+1)) for n in range(5)),Q(0))
api239 = sum((Q((-1)**n,(2*n+1)*239**(2*n+1)) for n in range(2)),Q(0))
pihi = 16*api5-4*api239
s2lo = 1-sum((Q((-1)**n*2**n,factorial(2*n)) for n in range(7)),Q(0))
assert pihi == Q(5277328977275528,1679825970703125)
assert s2lo == Q(180493,213840) > 0
Dhi = sum((c*c*(Q(1,2)-1/(4*pihi*pihi*j*j))
           for j,c in enumerate(cs,1)),Q(0))/s2lo
Hlo = Q(67216841,10**8)
assert C0lo-Dhi > Hlo
c, B, m, q, tau = Q(805003,10**8),sum(bs),152,7,Q(8,7)
A, sr = c*(m-q),Q(1154991329,10**9)
assert sr*sr < tau*A
Flo = 2*sr-tau
assert Flo == Q(4084939303,3500000000) and 0 < Flo <= A < m
p = (Hlo-B*(m-q)/m)/(1-Flo/m)
assert p == Q(118513839290,175971686899)
assert p-Q(6734824,10**7) == Q(6581516153,219964608623750000) > 0
print('finite rational checks PASS; global AM8 certificate not checked')
~~~

## 8. 原 MT 不能直接借用 AM 八点常数 [T，有限反例]

在原 MT 核，保持第6节同一权表。以下精确有理 gap 向量
\[
 g=10^{-6}(1032725,1038771,1983851,1982200,
                 1034862,1031769,1970761)
 \tag{19}
\]
给 \(F_{W_8,\rm MT}(g)<726/10^5<805003/10^8\)。
优化搜索只用来定位；下面对最终有理点的 Arb160 正包围才负责严格比较。
全部 pair 距离大于1，故闭式没有可去奇点：
\[
 k_0(x)=\frac{(\beta\cot\beta)(\pi x)\sin(\pi x)
                  -\tfrac12\cos(\pi x)}{(\pi x)^2-\tfrac12}.
\]
本机实际所得 ball 为
\(0.007257968549711223120650248019034694683813725332\pm6.95\cdot10^{-49}\)。

~~~python
from flint import arb, ctx
ctx.prec = 160
def a(t): return arb(t.numerator)/t.denominator
beta = arb(2).sqrt()/2
ct = beta*beta.cos()/beta.sin()
def k0(x):
    t = arb.pi()*a(x)
    return (ct*t*t.sin()-arb(1)/2*t.cos())/(t*t-arb(1)/2)
g = [Q(v,10**6) for v in
     [1032725,1038771,1983851,1982200,1034862,1031769,1970761]]
x = [Q(0)]
for v in g: x.append(x[-1]+v)
FW = sum((a(Q(v,10**8))*k0(x[i+j+1]-x[i])**2
          for i,row in enumerate(rows) for j,v in enumerate(row)),arb(0))
FW += sum((a(bs[i])*a(g[i]) for i in range(7)),arb(0))
assert FW < a(Q(726,10**5)) < a(Q(805003,10**8))
print(FW)
~~~

它只排除把外部 AM 的 \(c\) 免费移到 MT；不排除 MT 存在较小但仍有用的八点证书。
本机探索算得此权、\(m=152\) 击败当前 \(p_{\rm dg}\) 所需
\(c\) 约0.0068758，低于该反例；此探索不证明任何全域最低值。
原已付 MT 七点 \(c=19/5000,B_0=1/500,q=6\) 取 \(m=316\)
代入平方根包络约0.6730476394，低于当前项目值；未主张这是所有块长的最优。

## 9. 当前成果与下一准入目标

新增已付的是(4)、完整端项(9)、稀疏固定profile传递(10)–(13)，
以及 AM 正密度/自身二矩(14)–(17)和不可混窗的严格反例(19)。
外部已知八点结果接入原数域/原 partial-Weil 计数机制没有解析窗障碍；
唯一尚未支付的本轮比例输入明确为(16)的完整有限证书核验。

下一工作应固定外部 PC8CL 全部证明依赖并重放其覆盖/叶子，
或为原 MT 重新制作真正全域的八点下界；不能沿用 AM 的核表。
只有全域证书和不同作者对本稿的完整审查均完成后，才可把(18)记作项目采纳的
已知更强比例。当前仍不声称新比例、最优参数、世界纪录、条带提升或论文发布。
比例是渐近零点计数下界，不是 RH 证明完成百分比。
