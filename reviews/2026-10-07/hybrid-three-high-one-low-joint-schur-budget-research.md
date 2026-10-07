# 原 finite 31 的联合 Schur 预算：利用已付 entire13 的严格改进

2026-10-07。新推导；尚待另一作者独立全文审查。本报告只新增原 finite
矩阵的代数预算，不修改 461–463、既有物理研究稿、论文、math 或 Git。

**实际进展。** 已证明的 \(\operatorname{Tr}(C_HC_L^3)=o(d)\) 不只是删除
展开中的一个词：它还约束另一个方向
\(\operatorname{Tr}(C_H^3C_L)\) 与 whole high4、整个 22 的联合能量。
以下严格 finite 恒等式保留原 \(P,\phi\)、全部 signs 和 labels，
给出比普通 Hölder 常数 \(1\) 更强的常数
\[
 K_{\rm Schur}=\sqrt{\frac{2}{3\sqrt3}}
 =0.6204032394013997\ldots .
 \tag{1}
\]
这里没有证明 actual whole high4 有界，因而没有得到整个 fourth trace
的 \(O(d)\) 预算或新的零点比例。常数改善以 461 已付的 entire13 为输入，
不是新的无条件 31 算术 cancellation。

## 1. 冻结对象与输入

采用 [461](../../notes/461-original-one-high-three-low-fourth-trace.md)、
[462](../../notes/462-original-low-prime-fourth-path-constant.md) 的原对象：
\[
 \begin{gathered}
 X=T/(2\pi),\quad L_0=\log X,\quad Z=\sqrt X,\quad
 d=\lfloor XL_0\rfloor,\quad I=[-L_0/2,L_0/2],\\
 Ee_k=L_0^{-1/2}1_Ie^{i(T+2\pi k/L_0)u},\quad P=EE^*,\\
 B_R=-\sum_{p\in R}\frac{\log p}{a_{L_0}L_0\sqrt p}
 M_\phi(R_{\log p}+R_{-\log p})M_\phi,\qquad C_R=E^*B_RE .
 \end{gathered}
 \tag{2}
\]
全部平移在实线上零延拓；\(R=L\) 为 \(p\le Z\)，\(R=H\) 为
\(Z<p\le X\)。为避免矩阵 \(L\) 与 \(\log X\) 混淆，下文写
\[
 H=C_H,\qquad L=C_L.
\]
两者都是原 \(d\times d\) Hermitian 矩阵。本报告从此直接在这个有限
空间内工作；没有把 \(\operatorname{Tr}(E^*B_1B_2B_3B_4E)\) 当作
\(\operatorname{Tr}(C_1C_2C_3C_4)\)，也没有删除任何内部 \(P\)。

461 在其明列的 conductor-one zeta [R]（fixed-gap 输入
\(\theta<9/10\)，原 \(7/8\) 足够）下证明
\[
 \eta_T:=d^{-1}\operatorname{Tr}(HL^3)=o(1).
 \tag{3}
\]
462 无需 [R]，证明
\[
 e_T:=d^{-1}\operatorname{Tr}L^4\longrightarrow
 e_0=\mathcal C_L(\psi)>0,\qquad e_0=19/240\quad\hbox{在 flat 情形}.
 \tag{4}
\]
一般原固定正窗的 \(e_0>0\) 来自 462 的非负路径积分；取 sufficiently
small \(x,y\) 后四个 translated bulk factors 同时为正，给严格正质量。

[463](../../notes/463-two-sided-height-stability-for-original-fourth-words.md)
已另付任意原 prime 四词的 raw/good 双侧高度替换。本报告的有限代数
无需调用这个替换；因此不引入新 height、new Fourier ghosts 或额外
full-fourth 前件。原 [13/31
研究](hybrid-one-three-mixed-prime-sector-research.md) 的重复标签付款和
[distinct22 研究](hybrid-distinct-two-two-prime-sector-research.md) 的开放
范围均保持。

本轮根节点指定权威前件 a49bd50；以下是本报告实际读取的 canonical
UTF-8 SHA256（CRLF/lone CR 仅换为 LF，不 trim）：

| 文件 | canonical SHA256 |
|---|---|
| 461 | f9fdf0b721c76a5cc4c4e4821748007e62975286417e6bec9700e39b6778170b |
| 462 | 868adfeb0d742043f39bd08e0783d66b7a9db11316067b0b3b43d80150cdf680 |
| 463 | 6554ebc80616917d00b68f626329e8464e6ccc218c456608bff74e9da5a17d90 |
| 原 13/31 research | 5db2c614ab9d009a15a70f4e0639b95df2d59a6b56bd752216537fcf71e2b405 |
| distinct22 research | daca79cd62b61b7bd82a3b4fdf5a1a956ac0f2a1f44f7e63c0ff3f3b912cfc0d |

## 2. 真正 finite Gram 恒等式

在任意同维 Hermitian \(H,L\) 上置（本节省略下标 \(T\)）
\[
 \begin{aligned}
 a&=d^{-1}\operatorname{Tr}H^4,&
 e&=d^{-1}\operatorname{Tr}L^4,\\
 b&=d^{-1}\operatorname{Tr}H^3L,&
 \eta&=d^{-1}\operatorname{Tr}HL^3,\\
 c&=d^{-1}\operatorname{Tr}H^2L^2
    =d^{-1}\|HL\|_{\rm HS}^2,&
 s&=d^{-1}\operatorname{Tr}HLHL,\\
 k&=d^{-1}\|[H,L]\|_{\rm HS}^2=2(c-s),&
 w&=4c+2s=6c-k .
 \end{aligned}
 \tag{5}
\]
\(a,e,c,k,w\ge0\)，\(b,\eta,s\) 都是实数。这里 \(w\) 是原
\((H+L)^4\) 展开中的 **entire22 系数**，不是重复 22 子族的常数。
对 \(HL\) 和 \(LH\) 作 HS Cauchy 得 \(|s|\le c\)，故
\[
 0\le k\le4c,\qquad
 2c\le w\le6c,\qquad c^2\le ae,\qquad w\le6\sqrt{ae}.
 \tag{6}
\]
最后一个 Cauchy 应用于 \(H^2,L^2\)。所有这些公式使用有限矩阵的
合法循环迹。

令 \(S=HL+LH\)。三个真实 HS 向量 \(H^2,L^2,S\) 的 Gram 矩阵为
\[
 \begin{pmatrix}
 a&c&2b\\
 c&e&2\eta\\
 2b&2\eta&2(c+s)
 \end{pmatrix}\succeq0.
 \tag{7}
\]
例如 \(\operatorname{Tr}(H^2S)=2\operatorname{Tr}H^3L\)，
\(\operatorname{Tr}(L^2S)=2\operatorname{Tr}HL^3\)；
这些是整个原有限矩阵的迹，包含全部 repeated/distinct prime labels。

若 \(e>0\)，对 \(L^2\) 的方向作正交投影，得到新的中心化约束
\[
 \boxed{\left|b-\frac{c\eta}{e}\right|^2
 \le\left(a-\frac{c^2}{e}\right)
 \left(\frac{c+s}{2}-\frac{\eta^2}{e}\right)
 =\left(a-\frac{c^2}{e}\right)
 \left(c-\frac{k}{4}-\frac{\eta^2}{e}\right).}
 \tag{8}
\]
两个右因子各自非负。直接核验的方法是对
\[
 U=H^2-\frac ceL^2,\qquad V=S-\frac{2\eta}eL^2
\]
使用 HS Cauchy：归一化平方范数分别为
\(a-c^2/e\)、\(2(c+s)-4\eta^2/e\)，归一化 inner product 为
\(2b-2c\eta/e\)。它也正是 (7) 对中间 diagonal \(e\) 的 Schur
complement。若 \(e=0\)，则 \(L=0\)，\(b=\eta=c=s=w=0\)，可另行直接
处理；实际渐近问题由 (4) 保证 \(e>0\)。

## 3. 用 whole22 消去未知 \(c,s\)

给定 \(a,e,w\)，由 (6) 得
\[
 \frac w6\le c\le\min\left(\frac w2,\sqrt{ae}\right),
 \qquad \frac{c+s}{2}=\frac w4-\frac c2.
 \tag{9}
\]
从 (8) 删除非正的 \(-\eta^2/e\) 后，需控制
\[
 f(c)=\frac12\left(a-\frac{c^2}{e}\right)\left(\frac w2-c\right).
 \tag{10}
\]
在 (9) 的整个区间内
\[
 f'(c)=\frac{3c^2-wc-ae}{2e}
 \le\frac{2c^2-wc}{2e}\le0.
 \tag{11}
\]
第一步用 \(c^2\le ae\)，第二步用 \(c\le w/2\)。因此准确上界在
\(c=w/6\) 处，得到 **每个原 finite \(T\) 都成立** 的预算
\[
 \boxed{
 |b|\le \frac{w|\eta|}{2e}
       +\sqrt{\frac{aw}{6}-\frac{w^3}{216e}} .}
 \tag{12}
\]
radicand 非负由 \(w\le6\sqrt{ae}\) 保证。若 \(w=0\)，(6) 给
\(c=s=0\)，故 \(b=\eta=0\)，(12) 仍准确。

应保留实际小误差的系数 \(w/(2e)\)：只知道 \(\eta=o(1)\)，而不知
\(a,w\) 有界时，不能直接把这整个误差写成 \(o(1)\)。特别不能把
high repeated limit 替代未知的 whole \(a\)，再无条件宣称 entire31
已经是 \(O(d)\)。

保留原 signed 信息时更强的 exact one-sided 版本是
\[
 b\le\frac{c\eta}{e}
 +\sqrt{\left(a-\frac{c^2}{e}\right)
             \left(c-\frac k4-\frac{\eta^2}{e}\right)}.
 \tag{13}
\]
它展示整个 22 的 commutator 能量可以进一步减少 31 预算。不是先对
原 prime coefficients 取绝对值所得的四词 \(\ell^1\) growth。

## 4. 比 ordinary Hölder 更小的 sharp 常数

不用 \(w\)，(8)、\(k\ge0\) 与 \(c\le\sqrt{ae}\) 给
\[
 |b|\le\sqrt{\frac ae}\,|\eta|+
        \sqrt{ac-\frac{c^3}{e}} .
 \tag{14}
\]
函数 \(ac-c^3/e\) 在 \(0\le c\le\sqrt{ae}\) 的最大值发生于
\(c=\sqrt{ae/3}\)，值为
\(\frac{2}{3\sqrt3}a^{3/2}e^{1/2}\)。故准确 finite 上界为
\[
 \boxed{|b|\le
 \sqrt{\frac ae}\,|\eta|+
 K_{\rm Schur}a^{3/4}e^{1/4}.}
 \tag{15}
\]
ordinary Schatten Hölder 的同次幂项系数是 \(1\)。改进来源是已经付清
的反向混合矩 \(\eta\)，因而在实际原对象上，**若另外证明**
\(\limsup a_T<\infty\)，由 (3)–(4) 严格得到
\[
 |d^{-1}\operatorname{Tr}(C_H^3C_L)|
 \le K_{\rm Schur}\,a_T^{3/4}e_0^{1/4}+o(1).
 \tag{16}
\]
全常数不含随 \(T\) 增长的参数；\(o(1)\) 使用这一明确的 whole-high4
boundedness 前件。由 (6)，该前件也自动给 entire22 的 \(w_T=O(1)\)。
bounded high4 本来就能由 Hölder 保证 31 有界；本报告的新收益是
实际 13 输入下的严格更小常数与联合 \(w,k\) 预算，而不是重新声称
这个普通 boundedness 推论。

## 5. 原 prime fourth trace 的单个联合上界

原有限矩阵中的准确 cyclic 展开为
\[
 F_T:=d^{-1}\operatorname{Tr}(H+L)^4
       =a+e+w+4b+4\eta .
 \tag{17}
\]
这里可以合法循环，因为每个词都是同一个 \(d\times d\) finite 词。
没有据此循环带末端 \(P\) 的 physical 四词。

若 \(a_T,w_T\) 有界，则由 (12) 得
\[
 F_T\le a_T+e_0+w_T+
 4\sqrt{\frac{a_Tw_T}{6}-\frac{w_T^3}{216e_T}}+o(1).
 \tag{18}
\]
在显示的 radical 中保留实际 \(e_T\)，避免移动参数靠 feasibility
端点时对 \(e_T\to e_0\) 的不合法代入；连续性和 boundedness 可用于
其后明确的 compact-envelope 极限。

只给未来的 whole-high4 输入
\(\limsup a_T\le A_0<\infty\)，无需另给 \(w_T\) 上界，已经得到
\[
 \boxed{\limsup F_T\le
 \Phi(A_0,e_0),}
 \qquad
 \Phi(a,e)=a+e+
 \max_{0\le v\le1}
 \left[6\sqrt{ae}\,v+
       4a^{3/4}e^{1/4}\sqrt{v-v^3}\right].
 \tag{19}
\]
当 \(ae>0\)，这里取 \(w=6\sqrt{ae}\,v\)；当 \(a=0\)，定义
\(\Phi(0,e)=e\)。对 fixed \(e>0\)，\(\Phi(a,e)\) 关于 \(a\) 单调，
因此 limsup 前件的代入合法。实际 \(a_T\) 有界、\(e_T\to e_0>0\)，
加上 compact \(v\in[0,1]\) 上连续性，保证上述极限步骤。

这给一个具体可检验的未来算术付款条件：一旦 entire high4 得到
真实上界 \(A_0\)，whole prime fourth trace 可直接用 (19) 的
一维极值预算；31、22 的 labels 不必在该粗联合上界中逐个自由付款。
若另有实际 entire22 的上界 \(W_0\)，可把最大域进一步限制为
\[
 0\le w\le\min(W_0,6\sqrt{A_0e_0}),
 \quad
 A_0+e_0+w+4\sqrt{A_0w/6-w^3/(216e_0)} .
 \tag{20}
\]
不能把 (12) 的 radical 单独在 \(w=W_0\) 处替代最大值；它不是
\(w\) 的单调函数。式 (20) 明确保留整个一维 objective。

式 (19) 的极值也可直接定位。对 \(a,e>0\)，函数
\[
 g(v)=6\sqrt{ae}\,v+
       4a^{3/4}e^{1/4}\sqrt{v-v^3}
\]
在 \(0<v<1\) 严格凹：\(v-v^3\) 严格凹且正，而平方根为单调凹函数。
两端导数分别趋向 \(+\infty,-\infty\)，所以唯一极值点在
\((1/\sqrt3,1)\)，并满足
\[
 (3v^2-1)^2=9\sqrt{\frac ea}\,(v-v^3).
 \tag{21}
\]
这不是原 prime triple/prime resonance 的统计假设，而是新 exact
finite Schur budget 的可核验连续优化。

## 6. sharpness 与必须保留的范围

式 (12) 在 \(\eta=0\) 时，对任意
\(e>0,a>0,0<w\le6\sqrt{ae}\) 都有 commuting finite Hermitian
模型达到等号。置
\[
 c=w/6,\qquad v=c/e,\qquad
 \beta=\sqrt{\frac{a-c^2/e}{c}},
 \qquad t_\pm=\frac{\beta\pm\sqrt{\beta^2+4v}}2 .
 \tag{22}
\]
以
\[
 p_+=\frac{-t_-}{t_+-t_-},\qquad
 p_-=\frac{t_+}{t_+-t_-}
\]
作两点概率；则
\[
 \mathbb Et=0,\quad \mathbb Et^2=v,\quad
 \mathbb Et^3=\beta v,\quad \mathbb Et^4=v^2+\beta^2v.
 \tag{23}
\]
取 \(d=2\)，两个 diagonal entries 满足
\[
 L_\pm^4=2e p_\pm,\qquad H_\pm=t_\pm L_\pm .
 \tag{24}
\]
准确有 \(e,a,c\) 为指定值，\(\eta=0,s=c,w=6c\)，且
\[
 b=\beta c,\qquad b^2=ac-c^3/e=aw/6-w^3/(216e).
 \tag{25}
\]
重复整个 block 可放大偶数维度。由 (22) 取
\(c=\sqrt{ae/3}\) 得 (15) 的常数 \(K_{\rm Schur}\) sharp。
由每个 \(w\) 均可实现，也说明 (19) 是只知道这几个有限矩条件时
的 sharp one-sided envelope。

一个无需数值误差的检查是取
\(p_+=1/3,p_-=2/3,t_+=2,t_-=-1,e=1\)。准确矩为
\[
 (a,c,b,\eta,w)=(6,2,2,0,12),\qquad
 d^{-1}\operatorname{Tr}(H+L)^4=27.
 \tag{26}
\]
本轮以 Python Fraction 实算这五个矩、(25) 及
\(6+1+12+4\cdot2=27\) 均成立。它只检查有限有理 moment arithmetic，
不认证任何 AF 分析极限。

这些模型 **不是原 AF prime matrix 的反例**，不证明其 31 实际非零，
也不证明新的算术 saving 不可能。它们只说明：若只使用
\(\eta=o(1)\)、\(e\to e_0\) 和 finite Gram 正性，没有额外实际 prime
信息，就不能把 (12) 改成无条件 \(b=o(1)\)。同样，本报告没有把
all-high repeated 子族 \(19/240\) 当作 whole \(a_T\)。

## 7. 对下一真实付款的定位

本推导覆盖 entire31 的所有 repeated/distinct labels 和十六个 signs，
因为 (5)–(25) 始终作用于原 actual \(H,L\)；不把 individual signed
path 的 physical 空支持推广成原 finite \(P\) 词空支持。

当前尚未付款的是原 actual entire high4，或足以更强约束
\((a_T,c_T,k_T,b_T)\) 的 joint arithmetic。463 只解决高度尾；
旧 distinct22 报告保留其 actual projection 和 ratio-correlation
缺口。无零的单个 canonical prime prefix 仍不能直接控制这些 joint
量。本报告不重复其已知正幂上界作为新 saving。

这里提供两种明确后续接口：

1. 若直接付 entire high4 的有限常数，则 (19) 给包含整个 31/22 的
   一侧联合预算；相比 ordinary Hölder/Minkowski，已付 entire13
   产生严格常数收益。
2. 若能付更精确的 entire22 product/commutator 数据，则用 (8) 或
   (13) 保留 signed centering 与 \(k_T/4\)，不把四词误差逐二次绝对化。

whole prime fourth trace 当前仍未闭合；原完整零点响应还包含背景
混合预算。本报告没有新零点比例、完整四矩常数或新无零边界。
