# C004：Sonin 差额的紧扰动、有限矩与型域独立审查

2026-10-13。独立于 source-audit 的数学组织复核；本文件不改 STATE、cadence 或冻结数值。
恢复了 AGENTS、README、STATE、check/show、当前 Goal、C004、D20261013E 与第七周期复盘。
起始 HEAD 为 `73bc65e`，没有待处理 Python 进程。本审查只拥有此文件。

## 结论及准确对象

候选成立，但“紧修复”必须限定为**在源 L² 上诱导紧有界自伴二次型的修复**。
在下述冻结两 patch 的闭矩子空间上，完整实际 Weil 型与 archimedean Sonin 正迹型的差额是

    Delta = -E_U - w2 J,
    J(u,v)=(v,u),  w2=log(2)/sqrt(2),

其中 E_U 是自伴 Hilbert–Schmidt 算子。因此差额的本质谱恰为 `{−w2,+w2}`，
正、负指数均无限；加任何上述紧修复、任意有限个 Mellin 值/jet 的有界惩罚，
或施加有限个连续源约束，仍有无限负指数。统一质量预算若使差额非负，必要至少 `w2`。
这不称为完整 QW 的负方向；QW 与 Sonin 迹均有未被差额取消的高频 Gamma 能量。

## 原始输入的精确范围与连续性

核读作者托管的 [Selecta 作者稿](https://alainconnes.org/wp-content/uploads/Selecta.pdf)，
本地 `tmp/pdfs/c004/Selecta-author.pdf`，与 source-audit 所记 SHA 相同。
作者稿 Theorem 4.6、(84)–(85)（印页24–25）声明对所有乘法紧支光滑 f：

    T_S(f)=Tr(theta(f)S)=W_infty(f)+E(f),
    E(f)=integral f(rho^(-1)) epsilon(rho) d*rho.

这条恒等式没有小支持限制；小支持限制属于后续差额符号定理。
S 是真正 Sonin 空间的正交投影，scaling 不保持该空间，因此不能把压缩当作
Sonin 空间上的酉群表示。对 `f=g*g*`，正迹为 `||theta(g)S||_HS^2`。
这里实际 W_infty 的 multiplier 是 `2 theta'`，不是旧 half helper。

本审查只需要 epsilon 的连续有界性，不需要其光滑性或数值导数。
(85) 的每项为单位向量间 scaling 的矩阵系数，绝对值至多1，且随 rho 连续。
原文 (72) 给 `|lambda(n)|` 快速下降；每个 `|lambda(n)|<1`。
后者也可由不确定性直接看：若截断 Fourier 有模1特征值，则对应非零函数和
Fourier 变换都紧支；紧支函数的 Fourier 变换整延拓且在开集为0，矛盾。
由于 `lambda(n) -> 0`，所有分母 `sqrt(1-lambda(n)^2)` 有统一正下界。
所以 (85) 一致绝对收敛，定义连续函数，并由反演扩成连续偶函数

    e(t)=epsilon(exp(abs(t))).

xi_n 与 zeta_n 的支持正交给 epsilon(1)=0，保证两侧在 t=0 连续。
原文 Lemma 5.4 明确存在一阶导数跳跃；本证明不误称 e 在0光滑。
在有限 U 上，核 `e(x-y)` 有界平方可积，故 E_U 是 Hilbert–Schmidt；
没有使用原文对 E composed with differential Q 的不同非紧主项。
尤其 E 本身与 E composed with Q 不可混淆。

## 冻结域、全部实际源与权重

令 `a=log2`，`b=log(3/2)/4`，`mu=13/5`，`B=(-b,b)`，

    G(y)=u(y+a/2)+v(y-a/2),
    U=(-a/2-b,-a/2+b) union (a/2-b,a/2+b).

两 patch 不交，故源嵌入 `L²(B) directsum L²(B) -> L²(U)` 等距。
`a>2b`、`a+2b=log(sqrt6)<log3`，且 `a/2+b < log(mu)/2`。
因此其自相关实际 primepower 只有2；源内自相关没有 primepower。
共同矩子空间是

    H_F={u in L²(B): integral u=0, integral exp(y/2)u(y)dy=0}.

两项矩连续、线性独立，所以 H_F 是闭的余维2无限维空间。
任意移位保留零矩。实际极点型含 `ell_+(G) conjugate ell_-(G)` 及其共轭；
ell_+(u)=ell_+(v)=0 使每个极点交叉消失，不需要声称 ell_- 也为0。
ell_0 的消失另为小支持 Sonin 准入所需。

两个 prime 相关值互为共轭：在 log2 位，只有两个 patch 的匹配交叉。
原式负贡献恰为 `-2 w2 Re <u,v>`，所以 prime 矩阵为 `-w2 J`。
这里保留正负 log2 原子各一次，没有多算2或删掉其一。
在 H_F directsum H_F 上，定义 P 为其正交投影，E_U 为压缩后的核算子；
完整差额恰为 `Delta=-P E_U P-w2 J`（以后将压缩仍记 E_U）。
因为两个 patch 使用同一 H_F，J 保持该空间，压缩没有改变其主项。

## 生成器的像、闭包与额外有限消失

设 `L=D(D+1/2)`。有精确等式

    L C_c^infty(B) = C_c^infty(B) intersection H_F.

一边由两次分部积分立即成立。反向可完全在有限区间内解 ODE：
给 g 在右边，令 `q(y)=integral_{-b}^y g(t)dt`，则 q 紧支光滑，q'=g。
令

    eta(y)=exp(-y/2) integral_{-b}^y exp(t/2)q(t)dt.

加权总积分为 `integral exp(t/2)q(t)dt=-2 integral exp(t/2)g(t)dt=0`，
故 eta 也紧支光滑；`(D+1/2)eta=q`，于是 Leta=g。
不存在隐藏端点条件或只在 L² 意义成立的准入。

其 L² 闭包恰为 H_F。不同证明：若 z 正交于全部 L eta，则分布意义
`L* z=D(D-1/2)z=0`，从而 `z=A+B exp(y/2)`。
故闭包的正交补恰为这两个矩向量。也可从光滑逼近后以两个固定
光滑函数校正矩实现密度，证明不依赖谱信息。

任意有限个 Mellin 值/jet 在固定 B 上形如 `integral y^j exp(sy)g(y)dy`，
是连续 L² 泛函（复 s 同样适用）。其平方惩罚给有限秩自伴算子。
施加这些等式只给有限余维闭子空间。额外有限约束不必分别作用于两 patch；
可以作用于总 G 并耦合 u,v，下面无限指数证明仍适用。
其光滑核类仍稠密：用原光滑密度加有限维值域的光滑校正即可。
本结论不覆盖无限多个高度约束、不可控系数族或非连续源泛函。

## 型域：差额有界不意味着两个原型有界

QW 与 T_S 均不应自动扩成所有源 L² 上的有界型。
实际 Gamma multiplier `K(t)=2theta'(t)` 下有界、上渐近 log|t|，
自然闭型域要求 Fourier 能量 `integral log(2+|t|)|Ghat(t)|²dt` 有限。
为避免未经证明的端点 core 声明，可只使用下述无歧义的共同域：
取上述紧支光滑、矩零源类在 Gamma 移正闭型范数中的闭包 D_0。
所有本审查反例均属于原光滑类；没有额外域延拓前件。

在该共同 D_0 上，prime、pole 与 E_U 都是有界源型扰动，因此 QW 和
T_S=W_infty+E_U 的闭包有相同型域，差仍是上述 Delta。
对 T_S，光滑级正性传到闭包；而 `theta(G_n)S` 在 HS 范数为 Cauchy，
同时 G_n -> G 在 L²(U) 蕴含 L¹ 收敛，使 theta(G_n) -> theta(G) 在算子范数。
故其 HS 极限就是 theta(G)S，闭包仍确实等于 `||theta(G)S||_HS²`。
这只认证 D_0 上的真实迹延拓；不声明所有 L² 源均 trace class。
有限矩零闭包与有限约束也可在 D_0 内采用同样的光滑校正。

## 本质谱与无限指数：不靠一个负试探

记 K=-E_U。J 的两个无限维特征空间为 `V_+={(h,h)}` 与 `V_-={(h,-h)}`；
`-w2 J` 分别为 `-w2 I` 与 `+w2 I`。
紧自伴 K 可由有限秩自伴 K_r 在算子范数任意逼近。
给任意 epsilon<w2，取 `||K-K_r||<epsilon`；在无限维
`V_+ intersection ker K_r` 上，Delta 的型严格小于
`-(w2-epsilon)||G||²`；在 `V_- intersection ker K_r` 上严格大于
`(w2-epsilon)||G||²`。因此负、正指数都是无限。

任何有限个连续约束只再与有限余维子空间相交，仍无限维。
再加任何紧自伴修复也仍是 K 的紧扰动，完全同一证明有效。
光滑域上的任意有限维严格正/负空间可由密度和有限校正得到，
所以不只是抽象 L² 闭包有无限指数而原合法测试类没有。

本质谱的精确性也可核对：±w2 的各个无限维主空间有正交单位序列；
紧 K 将该序列送至0，给相应的 Weyl 序列。
另一方面 `Delta²-w2² I=(-w2J)K+K(-w2J)+K²` 是紧算子。
故在远离±w2的任何闭谱区间上，谱空间有限维：否则此紧算子
在该空间下有统一正的范数下界，违反紧性。
因此没有其他本质谱点，结论不依赖 RH 或 ζ 零点位置。

若 `Delta+cI+B >=0`，B 紧自伴，则在 V_+ 的弱零单位序列上
型极限为 c-w2，必要 `c>=w2`。该必要预算不是充分预算；
c=w2 时剩余紧谱仍可能有负方向。禁止将“存在有限质量预算”称为新的正性来源。

## 明确生成器与单方向核验

选任意固定非零实 chi 在 C_c^infty(B)，令

    eta_m=chi cos(my),
    h_m=L eta_m / ||L eta_m||_2.

分母为 `m² ||chi||_2 /sqrt2 (1+o(1))`；余项只有 O(m) 的 L² 范数。
因此 `h_m= -sqrt2 chi cos(my)/||chi||_2 + o_L²(1)`，严格矩零且弱收敛0。
将 h_m 同时放入两 patch，源范数平方为2，

    Delta(h_m,h_m) -> -2w2.

反号 patch 则极限 +2w2。故某个有限 m 给严格负差额，但无需指定或
数值拟合该 m；这是一族证明，不把有限样本升级连续证书。
完整 QW(h_m,h_m) 不由此为负，因为 Gamma/Sonin 能量可随 log m 增长。

## 方法类规模、未排除逃逸与消费判定

原文已知的贡献是 Sonin 正 trace 与紧 E；不能把这部分重新记为新增。
新的实际输入消费结论，是在预冻结含真实 p2 的域上将完整差额的
非紧主项精确识别为 `-w2 J`，并排除**全源统一无费用桥与任意紧二次型/有限矩修复**。
它超出单个负样本或一般“Hilbert 正空间不等于算术正性”的提醒，
也与519源像/谱等价及529标准正锥半群类别不同。
但是否已达到旧 Goal 第十节宏观规模，不能仅由“无限指数”自动判定：
该类仍限定为一个 archimedean Sonin 来源在指定两 patch 上的比较。
完整宏观瓶颈没有消除，不支持单独宣告 Goal complete。

未排除的逃逸包括：有实际 signed 算术输入的非紧修复；至少 w2 的真实质量支付
及剩余低谱估计；在非有限余维低域上作合法比较；改变到真正 semilocal 正来源；
允许投影/表示变化但必须另证明真实正性、同源迹身份和全部增长费用。
仅仅“源映射紧”并不足以归入本结论：它与原 unbounded Gamma 型复合后
可能诱导非紧或无界 Gram 差。必须先支付 induced difference 紧性的前件。

停止：全源无费用 Sonin 拼接以及上述紧/有限矩修复类。
重新准入：提供上述未排除逃逸中的独立 actual signed source 定理与可验证费用；
不能复活更多有限 jets、source 内正性自由极化、或把 semilocal 投影乘积当正交投影。
唯一下一动作：主代理核对完整差额归一化与另份逆审后再消费；
本审查没有待处理进程，不单独计轮。
