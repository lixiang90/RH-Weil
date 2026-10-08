# 条件短 Perron 与原 Type II 误差改进：独立全文审查

2026-10-08。审查人：perron_reviewer。结论：**限定 PASS**。
已完整重读作者修订后的 477 行；§4 水平线的次幂费用已修正并冻结。
本审查不修改作者稿、旧证明、旧笔记或 Git。

## 1. 全文输入与批准范围

已独立读取下表每份输入的全文。第一次合并读取输出有截断的
477 和 479 源已分别重新完整读取；没有以旧 PASS 或有限输出代读。
canonical LF 只统一 CRLF 和孤立 CR，不 trim，不改 EOF。

| 实读输入 | canonical LF SHA256 | LF 字节 / 行 |
| --- | --- | ---: |
| [本次被审源](hybrid-original-optimized-type-ii-remainder-research-checkpoint-audit.md) | 2d43aa69d79bde9a3aeac00ff4c9ee79696640f816df28eba051011ab255b25d | 17007 / 477 |
| [481 参数化完整分区](../../notes/481-original-type-ii-squarefull-tail-and-optimized-moment-transfer.md) | 4ce3ea2ac087d734142c8788607c1c54fc6887bcf535c806c88097447afdc63e | 10661 / 239 |
| [477 Vaughan 与原系数](hybrid-original-vaughan-type-i-and-type-ii-reduction-research-radial.md) | cf58086aeb9eee63832ccd06f5499110ea236b4bd94396893757b62e75bdb9d4 | 12260 / 324 |
| [479 sharp Weyl、二矩、maximal prefix](hybrid-original-type-ii-short-lambda-factor-fourth-research-radial.md) | b39876e0b9d91a06de57d1069cf6adac676252bd1fe737186bb065716015abb0 | 21261 / 524 |
| [原短 Möbius 证明](hybrid-short-mobius-twist-and-vaughan-zero-residue-research-radial.md) | a970366e68b8d3526c0dadac49b8ee8f4a7b6984e763712a851f8b6d353a291d | 6064 / 113 |
| [原短 Möbius 独立审查](hybrid-short-mobius-twist-and-vaughan-zero-residue-review-twisted.md) | 9236813c4a6089210419b702d656e8e5e747a1c5f74a31b75f78e81d62818cf2 | 6951 / 107 |
| [完整平方满尾及生成函数](hybrid-original-type-ii-large-single-prime-part-research-checkpoint-audit.md) | 66c35eb3ed43cec836ff1d10ed01322f115684c44b771d3db7364637994c3cab | 15353 / 401 |
| [同一 scalar 与 proper-power 范数迁移](hybrid-short-carrier-canonical-scalar-fourth-admission-research-radial.md) | f04279a9de54303d772859b2ee5e05010567404c53143c928a14e905eb51a0d7 | 14699 / 370 |
| [476 条件 whole 输入](../../notes/476-original-fourth-growth-five-sevenths-with-ivic-density.md) | 179829dd25f92ff187359f73455aafad9f957d714df13cf871db47a76e9408b6 | 4448 / 96 |

旧稿的 473 行完整读取后，审查提出 §4 水平线的局部费用勘误。
作者将两行替换为六行，显式分开有限 Perron 误差与含次幂的水平线。
本审查把最终稿的这一段在内存中准确还原，所得旧 canonical hash
为 `19d3fd62c19100bbeeff0c4accf8cbd87ceccc1b923c4cee53ec117ad5fa7c38`；
因此最终修订除该段外没有其他字节变化。随后已再次完整读取最终稿。

批准范围是原全高度 \([R_\theta]\) 下的真实短 \(m\) 子族估计、
由此重建的完整误差 \(E_\mu\)、两完整第四矩的 Hölder 传递，
以及固定 481 对象中额外 prime \(m\) 带的付款。
本审查不重新证明 \([R_{7/8}]\) 本身，也不声称原整条 Type II
得到 \(49/81\) 的上界。没有新比例、whole 常数或无零边界。

## 2. 有限矩形确实恢复原两端截断

保持作者的 \(X=T/(2\pi)\)、\(J_T=[T/4,4T]\)、
\(a_L\ge c_\phi>0\)、原 normalized 时间范数，以及
\[
0<v<a,\qquad v<1/4,\qquad \max(1/2,a+v)<y<1.
\]
这些前件特别给 \(a+v<1\)、\(AV<Y\)，其中
\(U=V=\lfloor X^v\rfloor\)、\(A=\lfloor X^a\rfloor\)。
因此在 \(m\le A\)、\(mk>Y\) 上，\(k>V\) 已被强制，
展开 \(b_V(k)\) 后没有额外截去 \(dj\le V\) 的项。

对 \(q=1\) 或 \(1_{\mathrm{prime}}\)，有限乘积
\(F_{B,A,q}G_VW_N\)、\(N=\lfloor X\rfloor\)，含所有
\(mdj\le X\) 的允许三元组。对每个原允许项，\(j\le N\)
自动成立；矩形本身的额外 \(n>X\) 仍保留到 Perron 误差中。
这一步不要求有限乘积在实部大于 1，也不以一个无限级数替代它。

矩形系数的正确统一界为
\[
|\beta_n|\le L\tau_3(n),\qquad n\le Z=AVN\le X^{1+a+v}<X^2.
\]
归一后可用 \(C_\phi\tau_3(n)/\sqrt n\)；\(\Lambda(m)\le L\)
来自 \(m\le A<X\)，不要求 \(n\le X\)。所以后面求和
\(X<n\le Z\) 时仍有同一系数合同。

\(x^\sharp=\lfloor X\rfloor+1/2\)、
\(y^\sharp=\lfloor Y\rfloor+1/2\) 给
\(1_{n<x^\sharp}-1_{n<y^\sharp}=1_{Y<n\le X}\)。
原始正负号、\(\mu(d)\)、\(q(m)\)、上下 \(m\) 带和共同乘积
掩码都完整保留；没有半权或整数端点补项。

## 3. 截断 kernel 的大小两区与全部有限误差

对 \(c=1/\log X>0\)、\(\mathcal H=T/8\)，作者 kernel 式(9)
可独立核验。无限竖线的条件积分给 step 函数。
当 \(\mathcal H|u|\ge1\)，对正负虚部尾积分分部，
端点项与导数积分
\(\int_\mathcal H^\infty|c+i\omega|^{-2}d\omega\)
各乘 \(1/|u|\) 后，都至多固定倍 \((\mathcal H|u|)^{-1}\)。
当 \(\mathcal H|u|<1\)，用
\[
I_\mathcal H(0)=\pi^{-1}\arctan(\mathcal H/c),\quad
|e^{i\omega u}-1|\le|\omega u|
\]
直接得 \(e^{-cu}I_\mathcal H(u)-I_\mathcal H(0)=O(\mathcal H|u|)\)。
正 \(u\) 时 \(1\le e^{cu}\)，负 \(u\) 时 step 为零，
两区合并给作者的统一 kernel upper。

对每个半整数 \(w=x^\sharp,y^\sharp\)，误差由
\[
X^{2\eta}\sum_{n\le Z}n^{-1/2}(w/n)^c
\min\{1,(\mathcal H|\log(w/n)|)^{-1}\}
\]
控制。这里 \((w/n)^c\le e^2\) 对大 \(X\) 和全部 \(n\ge1\) 成立。
远区 \(n\le w/2\) 或 \(n\ge2w\) 的完整质量
\(\sum_{n\le Z}n^{-1/2}\ll\sqrt Z\) 给 \(\sqrt Z/T\)。
近区有 \(n\asymp w\)、\(|\log(w/n)|\gg|n-w|/w\)，
而每个整数满足 \(|n-w|\ge1/2\)。对两侧各求 harmonic sum，
再用 \(\min(1,z)\le z\)，给 \(\sqrt w\log(2w)/T\)。
所以完整的 uniform 误差为
\[
\sup_{t\in J_T}|\mathcal E_P(t)|
\ll X^{2\eta}\left(X^{-(1-a-v)/2}+X^{-1/2}\log(2X)\right).
\]
取 \(\eta<(1-a-v)/8\) 后第一项仍为负幂；第二项也可保持负幂。
这包含了最近整数与矩形中全部 \(n>X\)，没有未付 finite tail。

## 4. 两个 Perron 高度和真实 prefix 的 Abel

外积分的 \(z=c+i\omega\)、\(|\omega|\le T/8\) 给
\[
\tau=t-\omega\in[T/8,33T/8].
\]
下端严格远离 0，故原无权和的正高度 Weyl 节省仍适用。
原短 Möbius 源的内部 Perron 高度为 \(T^2\)，
与这个外部卷积不是同一条轮廓，不能据内部高度把外部 guard 扩到 0。

原证明的 buffered reciprocal 对每个固定 \(\delta>0\)、
每个任意小的 \(\nu>0\) 给
\[
|1/\zeta(\sigma+ih)|\ll_{\theta,\delta,\nu}(1+|h|)^\nu,
\qquad \sigma\ge\theta+\delta.
\]
大高度圆盘的 \(\log\zeta\) 分支、Borel–Carathéodory 和三圆定理
供应该界；有限高度的 reciprocal 解析性另付。\(s=1\) 是其零，
不能当作 reciprocal 极点。左线实部为
\(\theta-1/2+\delta>0\)，没有跨 \(z=0\) 或 ζ 零点。

把外高度窗改为 \([T/8,33T/8]\) 只改变这些固定比较常数。
内部所有真实虚部仍为 \(O(T^2)\)，所以先把 reciprocal 指数
取小到 \(2\nu\) 可吸收到最终预留损失，再吸收 \(\log T\)。
这里需保留正确的水平线费用
\(O(W^{1/2}T^{-2+\rho})\)，\(\rho>0\) 可任意先取小；
原 sharp Perron 误差才是 \(O(W^{1/2}T^{-2}\log^2(2W))\)。
二者在 \(W\le X^v\)、\(v<1/4\) 下都可吸收。
旧稿将水平线写成纯 \(T^{-2}\log^C T\) 不是已证合同。
最终稿已按独审意见分开这两项，并明确内部 reciprocal 指数
预先不大于目标 \(\rho/2\)；需要留出日志时再取更小的指数，
例如 \(\rho/4\)。该修订覆盖了上述局部费用，不改变后续主结论。

原证明于是对全部真实 \(1\le W\le V\) 与全部该 guard 给
\(G_W(1/2-i\tau)\ll W^\alpha X^\rho\)，
其中 \(\alpha=\theta-1/2+\delta>0\)。\(1\le W<2\) 是单项，
不用错误地引入另一个 Perron 端点。
Abel 的准确形式为
\[
G_V(1/2+c-i\tau)=V^{-c}G_V(1/2-i\tau)
+c\int_1^V G_u(1/2-i\tau)u^{-c-1}du.
\]
对真实 step prefix 统一使用该界，并用
\(u^\alpha\le V^\alpha\)、
\(V^{-c}+c\int_1^V u^{-c-1}du=1\)，证明实部移到
\(1/2+c\) 的同一 upper。没有把 \(\mu\) 变成 \(|\mu|\)，
也没有向一个依赖 \((m,d)\) 的已取绝对误差再套 prefix 相消。

## 5. 完整短子项的点值和 normalized 四矩

479 源的三个 Weyl 长度分支和 sharp partial summation，
在 \(\tau/T\in[1/8,33/8]\) 上仍只有固定常数变化。
对所有 \(j\le N\le X\) 的 prefix 给 \(X^{1/6}\log^C X\)，
再对单调权 \(j^{-c}\) 作 Abel，sup 加总变差至多 2，
得到作者 \(W_N(1/2+c-i\tau)\) 的同一幂。
\(F_{B,A,q}\) 则由原非负 upper
\(\Lambda(m)\le L\)、\(q\le1\) 直接给 \(\sqrt A L\)。

在已保留完整 product mask 的有限 Perron 等式中，
\((x^\sharp)^c,(y^\sharp)^c\le e^2\)，而
\(\int_{-T/8}^{T/8}|c+i\omega|^{-1}d\omega\ll\log X\)。
原 normalizer 消去 \(F\) 的 \(L\) 费用，于是点值 upper 为
\[
X^{1/6+a/2+v(\theta-1/2+\delta)+\rho}\log^C X
+O(X^{-c_0})
\]
对某个 \(c_0>0\)，只需先固定足够小的 \(\eta\)。

二矩另在原 \(Y<n\le X\) 的实际系数上支付；这里没有把长度
\(Z=AVN\) 的矩形作为原函数来求二矩。
\(|\alpha_n|\ll_\phi\tau_3(n)/\sqrt n\) 给能量
\(X^{2\xi}\log X\)，477/479 展开积分得到的时间二矩乘子为
\(1+X\log X/T=O(\log X)\)。所以 normalized 二矩为任意小的
\(X^\varepsilon\)。取 sup 平方乘真实二矩，再按最终 ε
先分配 \(\delta,\rho,\eta,\xi\)，完整给
\[
\mathcal M_{S_{B,A,q}}
\ll X^{1/3+a+(2\theta-1)v+\varepsilon}.
\]
负幂 Perron 误差只增添可吸收的小项。各常数对全部整数
\(U\le B<A\) 和所列两种 \(q\) 统一。

## 6. 新辅助分区的其他费用没有遗失

477 的 Vaughan 恒等式对当前精确整数 \(U,V\) 逐系数成立。
479 对 Type I 的 sharp Weyl 与原系数二矩给
\(1/3+2v\)，没有额外认领一次 μ 相消。
原 low block 先平方再用实际乘积长度 \(Y^2\)，给 \(2y-1\)。
原 large proper-power \(m>A\) 的 dyadic 外权是
\(O(\log^2 X)\)；原 \(b_V\) 的 maximal prefix 四矩内长度
\(K<X/A\)，给 \(1-2a\)。这些步骤均保留两个移动 product endpoints。

完整 squarefull tail 源先合并 \(n=ms\)，其实际系数
\(|c_r(n)|\le\tau(r)\tau_3(n)\) 对当前 \(V,A\) 统一。
最大 prefix 引理的 binary block 平方长度为 \(4N^2\)，
不是 \(N\)，给 \(1+N^2/X\)。对每个平方满 dyad 的外权
\(\sum r^{-1/2}\ll1\) 用 Minkowski，再合成全部非空 dyads，
给 \(1+X/H^2\)；取 \(H=V^2\) 就是 \(1-4v\)。

依次拆 short \(m\)、large proper-power \(m\)、
large genuine-prime \(m\) 且 \(r>H\)，余项恰为作者式(21)。
\(\Lambda(m)=0\) 的整数不贡献，没有重复或遗漏部分。
原 scalar proper-power 迁移另是完整 \(L^4\) 范数
\(O(X^{-1/12})\)，可与前述误差合成；不把它当作未知增长下的
additive \(o(1)\) 第四矩差。

非零余项的 \(s\ge2\)、\(s\operatorname{rad}(r)>V\) 由原 μ 零域
直接成立。\(a=2v\) 时 \(V^2\le\lfloor X^{2v}\rfloor=A\)
是准确整数不等式，故 \(m>A\ge H\ge r\) 自动给 \((m,r)=1\)。
没有添加 \((m,s)=1\)；balanced prime 与 squarefree \(k\) 仍存在。

## 7. 优化、传递及固定 481 prime 带

在作者限定的费用族中，最大费用是
\[
\max\{2y-1,1/3+2v,1/3+a+(2\theta-1)v,1-2a,1-4v,0\}.
\]
由 \(a\ge(1-c)/2\)、\(v\ge(1-c)/4\) 及 \(2\theta-1\ge0\)
推出 \(c\ge(6\theta+7)/(6\theta+15)\) 的推理有效。
作者的 \(v=2/D,a=4/D,y=(6\theta+11)/D\)、\(D=6\theta+15\)
满足全部前件，实现四个 active 费用相等；Type I 不超过它。
这只证明所列费用族的优化，不证明所有可能分区或 whole 的最优性。

对 \(\theta=7/8\)，我用独立 Fraction 算术核得
\[
(v,a,y,c)=(8/81,16/81,65/81,49/81),
\quad\text{费用}=(49/81,43/81,49/81,49/81,49/81,0).
\]
先合成完整误差函数，再作有限次 \(L^4\) Minkowski，给条件
\(\mathcal M_{E_\mu}\ll X^{49/81+\varepsilon}\)。
它比无条件 481 误差幂小 \(8/567\)，但新增 μ 准入明确依赖
同一个全高度 \([R_{7/8}]\)。新 \(b_V,Y,A\) 与 481 不同，
新余项不能直接称为旧余项的子族。

以 476 的既有条件 complete whole \(5/7\) 输入，先由
\(R_\mu=P_H-E_\mu\) 得 \(R_\mu\) 的同幂范数，随后才用
\[
|\mathcal M_F-\mathcal M_G|
\ll\|F-G\|_{4,T}(\|F\|_{4,T}+\|G\|_{4,T})^3.
\]
独立有理复核为
\[
\frac{3(5/7)+49/81}{4}=\frac{779}{1134},\quad
\frac57-\frac{779}{1134}=\frac{31}{1134},\quad
\frac{29}{42}-\frac{779}{1134}=\frac2{567}.
\]
最终 ε 小于 \(31/1134\) 时，差以 \(X^{5/7}\) 归一后趋零；
没有相对未知实际主项的等价，也没有常数级误差预算。

固定 481 corollary 的 \(B=M\)、\(q=1_{\mathrm{prime}}\)、
\(a=3/14\)、\(v=2/21\) 给
\(1/3+3/14+(3/4)(2/21)=13/21\)。
要从全部 \(k\) 的 prime 带到 \(r\le H\) 的原余项带，
作者确实另外在 \(c_r(n)\) 中加入 \(M<m\le A_1\) 掩码，
直接证明 \(r>H\) 带的同一 tail upper，然后用两函数范数差。
因此没有从复杂 signed 大族范数推任意子族的范数。
\(A_1/M\asymp X^{1/42}\) 的真实 aspect 增量成立，
但完整 moment transfer 仍是 \(29/42\)。

## 8. 留数、有限复核与最终范围

small-\(r\) 源的 \(\zeta(z)C_{V,H}(z)/\zeta(2z)-1\)
仍有准确的 \(-1\)。更新辅助 cut 不改此系数恒等式。
在 \(\Re\rho>1/2\) 的普通 ζ 零点，原 genuine-prime 生成函数
与该项相乘仍有 \(-m_\rho\) 留数。有限 short 子项的局部 Perron
没有跨过或删除整条剩余生成函数的这些极点。

本次 Fraction 重放只检查参数和指数，未用有限素数枚举代替
Perron、buffered reciprocal、Weyl、真实二矩或 maximal prefix 的
无限解析证明。没有执行外部程序或宣称 Lean 形式化认证。

条件 \(49/81\) 是完整误差付款；\(779/1134\) 是以旧 whole
\(5/7\) 输入得到的矩传递误差。余项自身只继承 \(5/7\)，
原 \(p_{\rm dg}\)、引用前件下的 \(\sigma_*\)、κ 与 whole 常数
均没有提高。最终源的局部水平线费用勘误已核验，限定 PASS 正式绑定
上表的最终 477 行源；此结论不依赖有限枚举或旧审查状态。
