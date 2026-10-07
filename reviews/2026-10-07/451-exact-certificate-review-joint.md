# 451 的连续代数、有限证书与反馈常数独立审核

2026-10-07。审查者 type_ii_joint。结论：本报告所限定的连续代数、
严格有理区间、geometry/count/feedback 数值不等式全部 PASS，未发现错误。
这不是原 source 的 plain moment、prime inputs、无限轮廓或全族无零结论的
独立审查；那些分析前件由另外的全文审查承担。

## 1. 版本与复现范围

canonical SHA-256 的规则为 UTF-8 文本 CRLF/CR 统一为 LF，不改其他字符。
本次直接读取、重跑并绑定：

| 文件 | canonical LF SHA-256 |
| --- | --- |
| [451](../../notes/451-kappa-feedback-cubic-boundary-and-family-continuation.md) | 17ce7fea8c881ebd4034657b7039e99897d4ff9532348993ba329c46e3c4d487 |
| [exact audit script](../../scripts/hybrid_kappa_feedback_exact_audit.py) | e03d6536378fff4b51625ab71fa5eace9fcbf4fe1156ccb6ae048f03bf96bc68 |
| [stored JSON](../../output/hybrid-kappa-feedback-exact-audit.json) | 309f275701a1d96c245eb067d49b00598df4af8e380d220944de250fd2e9d7ba |

原脚本实际重跑为 PASS、checks=149、direct_endpoint_models=49。
解析后的重跑 JSON 与现存 JSON 完全相同。未改这三个文件。
独立符号复算使用 SymPy 1.14.0 的 QQ 多项式 remainder/inverse；
独立区间复算使用 Fraction 与 Bernstein 系数，均未调用原 Cubic 类。

原脚本的 source_sha256_canonical_lf 是固定 metadata 字符串：
42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3。
脚本不读取该外部 source，也不读取或校验 451；它只动态校验自身哈希。
所以 PASS149 不能独自证明外部 source 或 451 的版本绑定。
上表的三个实际哈希与本文的逐式复核另行提供绑定。

## 2. 域算术与根隔离

令
\[
p(e)=657e^3-954e^2+21e+20,\quad
L=\frac{16683858898627}{10^{14}},\quad
H=\frac{16683858898628}{10^{14}} .
\]
独立有理运算给
\[
1/6<L<H<167/1000,\qquad p(L)>0>p(H).
\]
在 \([1/6,167/1000]\)，
\[
p'(e)\le1971(167/1000)^2-1908(1/6)+21<0.
\]
因此确有唯一指定实根 \(e_*\in(L,H)\)，不是仅找到两端异号。

模 7 的 \(p(0),\ldots,p(6)\) 依次为 \(6,3,4,3,1,6,5\)。
最高项系数非零且三次多项式无根，故模 7 不可约；
整数系数 primitive，故在 QQ 上也不可约。
于是 \(\mathbb Q[e]/(p)\) 是域，基底为 \(1,e,e^2\)。

原 Cubic 乘法先卷积至四次，再依次消去四次、三次项，
使用 \(e^3=(-20-21e+954e^2)/657\)，顺序正确。
inverse 的矩阵第 \(j\) 列是 self 乘第 \(j\) 个基向量的坐标；
求解 \(Mv=(1,0,0)^t\) 的有理 Gauss–Jordan 运算正确。
不可约性保证所有实际非零除数有逆，代码还逐次断言乘回为 1。
这些内部断言不计入 require 的 149 项。
interval Horner 使用四种端点乘积的最小/最大值，负系数也正确处理；
positive 要求区间下端严格 \(>0\)，没有把零端点判为正。

旧 \(e_0\) 的多项式 \(1653e_0^2-66e_0-35\) 在
\[
16683838746/10^{11}<e_0<16683838748/10^{11}
\]
的端点分别为负、正，正根唯一。又 \(L>16683838748/10^{11}\)，
故 \(e_*>e_0\)，\(\sigma_*=11/12-e_*/4\) 严格小于旧边界。
整个比较没有使用浮点近似。
独立展开还给
\[
p(11/3-4\sigma)=-\frac{16}{3}
(7884\sigma^3-18819\sigma^2+14643\sigma-3686).
\]

## 3. 一般 optimizer 与连续平方完成

沿用 451 的 \(D,P,J,K,W,h\)，取 \(\alpha=5/6\)，定义
\[
R=1-\delta+\frac{(\alpha-\delta)\delta P}{2J},
\qquad E=K+W\delta-h(1-R).
\]
独立在一般 \(e,b,\kappa,y,\delta\) 的有理函数域中展开，恒等地有
\[
-2JE=A(y)\delta^2-B(y)\delta+C(y),
\]
其中 \(A,B,C\) 与 451 完全相同。
这是符号恒等式，不依赖任何有限取样。

记 \(\rho(\kappa)=3312\kappa^2-936\kappa+67\)。
一般 \(Q_0=4A(0)C(0)-B(0)^2\) 中 \(b^2\) 的系数精确为
\[
-\frac{\rho(\kappa)}{1728\kappa^2}.
\]
在 \(\kappa\ge37/50\)，
\[
\rho(37/50)=742507/625>0,\qquad
\rho'(\kappa)\ge99144/25>0.
\]
所以是严格凹二次式，451 给的 \(b\) 确为唯一极大点。
独立求导和代入重得其极大值
\[
-\frac{25(6\kappa-1)^2(15\kappa-2)
[(1314\kappa-159)e^2-(36\kappa+6)e-30\kappa+5]}
{162\kappa^2\rho(\kappa)}.
\]
令 \(\kappa=5/6-e/2\)，方括号恒等于 \(-p(e)\)；
模 \(p\) 后，optimizer 正确化为
\[
b=(-5181+156335e-387630e^2)/81941.
\]

用独立 QQ remainder/inverse 运算重建 \(A,B,C,Q=4AC-B^2\) 的每个
基底坐标，与 JSON 全部逐项相同，包括 \(Q_0=0\)。
下一节严格给 \(A_i>0,C_i>0,Q_i>0\ (i\ge1)\)，所以对所有 \(y\ge0\)
有 \(A(y)>0\)、\(Q(y)\ge0\)，且 \(y>0\) 时 \(Q(y)>0\)。
连续地，
\[
A\delta^2-B\delta+C
=A\left(\delta-\frac{B}{2A}\right)^2+\frac{Q}{4A}\ge0.
\]
这是任意实 \(\delta\) 的多项式结论；只在 \(J\ne0\) 时转回 \(E\)。
在实际 \(0\le\delta\le3/4,\ 0\le y\le1/2\) 内，
\[
D>2,\quad P>3/4,\quad
J\ge2(5/6-\delta)+(3/4)\delta
\ge35/48>7/10.
\]
故 \(E\le0\)。唯一等号是
\[
y=0,\quad \delta_*=(5-9e_*)/(6+18e_*)=B(0)/(2A(0)).
\]
独立域运算证实此时 \(R=2/3,E=0\)。
由 \(1/6<e_*<1/5\)，直接有
\(1/3<\delta_*<7/18\)，特别 \(1/50<\delta_*<3/4\)。

## 4. 论文可直接使用的严格有理系数区间

对 JSON 的每个二次域坐标 \(q(e)=a_0+a_1e+a_2e^2\)，令 \(w=H-L\)。
在 \(e=L+wt\), \(0\le t\le1\)，其 degree-2 Bernstein 系数为
\[
\beta_0=q(L),\quad
\beta_1=q(L)+wq'(L)/2,\quad \beta_2=q(H).
\]
因此
\[
q(L+wt)=\beta_0(1-t)^2+2\beta_1t(1-t)+\beta_2t^2
\in[\min\beta_i,\max\beta_i].
\]
全部端点计算只用 Fraction。对下表每项，计算所得
\(\min\beta_i\) 严格大于表列下端，\(\max\beta_i\) 严格小于上端。
这提供独立于原 interval Horner 的严格包络：

| 系数 | 严格区间 |
| --- | --- |
| \(A_0\) | \((47/100,48/100)\) |
| \(A_1\) | \((121/100,122/100)\) |
| \(A_2\) | \((86/100,87/100)\) |
| \(A_3\) | \((29/100,30/100)\) |
| \(C_0\) | \((7/100,8/100)\) |
| \(C_1\) | \((6/100,7/100)\) |
| \(Q_1\) | \((4/100,5/100)\) |
| \(Q_2\) | \((19/100,20/100)\) |
| \(Q_3\) | \((26/100,27/100)\) |
| \(Q_4\) | \((7/100,8/100)\) |

## 5. 全部 displayed geometry 的有限审核

独立从 \(e,b,\sigma,l_x,l_y,h\) 重建 JSON 的全部 20 个 geometry 坐标，
逐项一致。用上一节 Bernstein 方法验证全部严格余量，另验证
\(3/25<b<1/8\)、\(37/50<\kappa_*<3/4\)。
令 \(\zeta_{\max}=1/384000\)，得到：

| 表达式 | 已证严格不等式 |
| --- | --- |
| \(e\) | \(1/6<e<1/5\) |
| \(b,\ 1-3e,\ l_x-e,\ l_y-e,\ l_y/20,\ h/600\) | 均 \(>0\) |
| \(l_y-e-11b/6\) | \(>2/25\) |
| \(5e-h-\zeta_{\max}\) | \(>1/50\) |
| \(h+\zeta_{\max}\) | \(<1\) |
| \(-6/25+(32/25)e+b/6\) | \(<-1/200\) |
| \(-71/600+(329/400)e-(421/1200)b\) | \(<-1/50\) |
| \((13/75)h-l_y/2+63/5000\) | \(<-2/25\) |
| \(\sigma_*-3/50\) | \(>81/100\) |
| \(\sigma_*-1/20\) | \(>82/100\) |
| \(\sigma_*+1/2\) | \(>4/3\) |
| \((e-1/6)/128\) | \(<\zeta_{\max}\) |

由 full-J gap 推出 full Gram gap \(l_y-11b/6>0\)。
451 的 \(F(d)\) 每段斜率至多 \(-1+1/2+1/8=-3/8\)；
因 \(5e-1<0\) 且 full Gram gap 正，\(F(0)=0\)，所以全部 \(d\ge0\)
的最大值为 0。low normalizer 精确恒等式
\[
(1-e)/4-b/6=\sigma_*-2/3-b/6
\]
也独立验证。

floor 的显示高侧会计在 \(\delta=1/50,R=1,q\le1/100,d=h\) 给
\(K+1/100+3e/100\)，恰是表列 floor 式。
middle 在无槽 \(R=76/75-2\delta/3,q\le\delta/2\) 下，
\(d\)-斜率为 \(101/150-\delta/6\ge329/600>0\)，故取 \(d=1/2\)。
剩余 \(\delta\)-系数为
\[
5/12+3e/2-h/2=1/6+3e/4-b/4>25/96>0,
\]
故取 \(\delta=3/4\)，独立展开恰得表列 middle 式。
small 的表列数值严格验证；其 D1(1/3) 局部解析来源不由数值替代。
sector、Euler、principal 各显示 exponent 的符号通过；
对应无限级数与轮廓准入仍属另两份全文审核。

## 6. 反馈与供给的连续数值桥

从实际 count 公式独立求导可得
\[
\partial_\kappa R
=\frac{\delta(5/6-\delta)^2x(1-x)^2}{3\kappa^2J^2}\ge0.
\]
用 \(J\ge(5/6-\delta)D,\ D>2,\ \delta\le3/4\) 及
\(\max_{0\le x\le1/2}x(1-x)^2=4/27\)，连续地得到
\[
0\le\partial_\kappa R\le625/36963<1/50.
\]
不是通过 finite grid 估计导数。在 actual \(\kappa\) 路径上，
\(\kappa_{\rm act}-\kappa_*=2\Delta\)，故 count 费用 \(<\Delta/25\)。
因 \(h<1\)，reference \(E\le0\) 加上 normalizer 的 \(-\Delta\)，
得 \(E_{\beta_*}(h)\le-24\Delta/25\)。

高侧 selected \(d\)-斜率 \(S=R+\delta/2-17/50\)：
\(R\ge1-\delta,\delta\le3/4\) 给 \(S\ge57/200>0\)；
actual count 的 trivial cap \(R\le1\) 给 \(S\le207/200<2\)。
所以 \(h\) 至 \(h+\zeta,\zeta=\Delta/32\) 的费用至多 \(\Delta/16\)，
剩余系数精确为
\[
24/25-1/16=359/400.
\]
\(\beta_*\le7/8\) 时
\(\Delta\le(e-1/6)/4\)，故 \(\zeta\le(e-1/6)/128<\zeta_{\max}\)。
由表列 supply gap，
\(5e>h+\zeta+1/50\)，特别有 \(e/(h+\zeta)>1/5\)。

原比较和供给的 scalar 数字亦逐一 Fraction 复核：
\[
25/516<1/20,\quad 1/20-25/516=1/645,\quad
1/[18(37/50)]=25/333<1/5,\quad35/48>7/10.
\]
这些有限常数不能反向证明 marked/plain moments 的分析前件。

## 7. 149 项的真正范围与验收

| require 检查类别 | 项数 |
| --- | ---: |
| 根隔离、导数、模7不可约、旧根隔离及严格比较 | 5 |
| 域关系与 reference κ 区间 | 5 |
| \(Q_0=0\) | 1 |
| 全部 A/C 系数及 \(Q_1,\ldots,Q_4\) 严格正 | 10 |
| equality δ 公式及实际区间 | 3 |
| 49 个有限 \((\delta,y)\) 模型，每个两个恒等式 | 98 |
| critical \(R=2/3,E=0\) | 2 |
| 六个 geometry 正性 | 6 |
| e 的两侧严格界 | 2 |
| 其余 geometry/normalizer 严格界及恒等式 | 11 |
| 最后六个 scalar feedback/comparison/supply/J 检查 | 6 |
| 总计 | 149 |

即 51 项非取样检查和 98 项取样检查。49 个模型没有声称覆盖真实连续域；
连续结论由第3节的符号恒等式、第4节的严格系数包络和 \(J>0\) 证明。
本次额外独立审核包括一般 b optimizer 的凹性/极大值、
全部 A/B/C/Q 域坐标、全部 20 个 geometry 坐标、
22 个 Bernstein geometry 严格检查及论文十个 rational enclosure。
没有发现需要修改原有限证书的事项。
对新论文若公式与参数不变，只需核对新稿逐式转写与表格版本，
无需重复把 49 个模型包装为新的数学证据。
