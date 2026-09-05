# 274. 次线性频带之外的完整响应闭合

日期：2026-09-05。主线：NCE-8 / B1y；论文归属：Vaughan--Brownian response。

状态：[T/R] 实际四阶高频尾的加强；[T] 同一共尾选择上的次线性频带归约；
[E] 完整支撑的间距局部化与异常邻点实验；
[O] 剩余联合响应、完整显式公式与上同调桥梁。
本轮仅 Markdown；没有证明 RH/GRH 或新的零点比例。

## 1. 本轮结论与量词

固定可计算的 \(0<\sigma<1/2\)，沿271已无条件构造的同一共尾序列，
\[
 Y=2^{m_j},\quad Y\le N=N_j\le2Y,\quad
 |M(Y,N)|>Y^{1/2-\sigma}\sqrt{\ell(Y)},\qquad
 \ell(Y)=\max(1,\log\log\log Y).
 \tag{1}
\]
写 \(L=\log Y,\ W=\log(2L)\)，并取
\[
 \boxed{\quad T_*(Y)=Y\sqrt{W/L}=o(Y).\quad} \tag{2}
\]
本篇证明
\[
 J_{4,>T_*}\ll_\sigma\ell(Y)^{-2}\mu^4=o(\mu^4),
 \qquad
 \boxed{\ J_4=O(\mu^4)\ \Longleftrightarrow\
                J_{4,\le T_*}=O(\mu^4).\ }
 \tag{3}
\]
与272相比，这次确实是**同一271序列**上的改进：
\[
 \frac{T_*}{Y\sqrt L/\ell}=\frac{\ell\sqrt W}{L}\longrightarrow0.
 \tag{4}
\]
但它仍不覆盖268在每一个dyadic尺度上的首素数规则，也不声称271特定选择
穷尽原256的自由存在性。剩余频带随 \(Y\) 增长；规范频率是
\(|t|\le m_jT_*(Y_j)\)，不是 fixed compact core。

## 2. 完整响应与改进高频定理

使用273的实际系数 \(a_n\)，并写
\[
 A=\sum a_n,\quad B=\int_1^N x^{-\sigma}e^{-x/Y}\,dx,\quad
 S=A+B,\quad M=A-B,\quad\mu=M/S.
 \tag{5}
\]
按 lag \(\lambda=\log x\) 搬运得到一侧源 \(\alpha,\beta\)，令
\[
 k_\lambda=(\delta_\lambda+\delta_{-\lambda})/2-\delta_0,\quad
 p=\int k_\lambda\,d\alpha,\quad c=-\int k_\lambda\,d\beta,\quad r=p+c.
 \tag{6}
\]
写 \(F_\eta(x)=\eta((-\infty,x])\)，
\[
 D=\|F_p\|_2^2+\|F_c\|_2^2,\qquad
 J_4=\frac{\|F_{r*r*p}\|_2^2+\|F_{r*r*c}\|_2^2}{S^4D}.
 \tag{7}
\]
这里 \(p,c,r\) 及(7)中的卷积均为紧支撑、总质量为零的有限符号测度；
连续源未被有限原子化。Fourier压缩定义与268、272相同。
特别 \(D\asymp_\sigma LS^2,\ S\asymp_\sigma Y^{1-\sigma}\)。

置
\[
 F(\xi)=\sum a_n n^{-i\xi},\quad
 C(\xi)=\int_1^N x^{-\sigma-i\xi}e^{-x/Y}\,dx,\quad
 \widehat r=\Re F-\Re C-M.
 \tag{8}
\]
\(-M\) 及连续cutoff两端仍保留。

### 定理274-A [T/R]

对任意充分大的实 \(Y\)、整数 \(N\in[Y,2Y]\)、实 \(T\ge1\)，一致有
\[
 \mathcal H_T(r):=\frac1{2\pi}
     \int_{|\xi|>T}\frac{|\widehat r(\xi)|^4}{\xi^2}\,d\xi
 \ll_\sigma
 \frac{Y^{2-4\sigma}L^2}{T}
 +\frac{Y^{4-4\sigma}W}{T^2}
 +\frac{M^4}{T}
 +\frac{Y^{4-4\sigma}}{T^5}.
 \tag{9}
\]
这个绝对预算不要求271的质量选择。

证明：\(F^2=\sum_k b_k k^{-i\xi}\) 的真实聚合系数正是273的 \(b_k\)。
局部间距 Montgomery--Vaughan 均值 [R]（来源与精确版本已在269核验）给
\[
 \int_V^{V+U}|F(\xi)|^4\,d\xi
 \le U\sum_kb_k^2+C_{\rm MV}\sum_k b_k^2/\delta(k).
 \tag{10}
\]
在 \([2^jT,2^{j+1}T]\) 及负频率上乘 \((2^jT)^{-2}\) 再求和，
得到 \(O(B_0/T+\mathcal G/T^2)\)。
273已独立证明 \(\mathcal G\ll_\sigma Y^{4-4\sigma}W\)，
而267给 \(B_0\ll_\sigma Y^{2-4\sigma}L^2\)。
连续lag密度的零延拓BV界仍给 \(|C(\xi)|\ll_\sigma Y^{1-\sigma}/|\xi|\)。
对 (8) 用三项四次方上界，分别积分连续项和实际中心质量项，即得 (9)。
有限系数、非负积分和可求和几何majorant保证完整尾项，而非有限采样外推。
\(\square\)

### 定理274-B [T]

沿 (1)，对任意实 \(T\ge1\)，有
\[
 \frac{J_{4,>T}}{\mu^4}\ll_\sigma
 \frac{L}{T\ell^2}
 +\frac{Y^2W}{T^2L\ell^2}
 +\frac1{TL}
 +\frac{Y^2}{T^5L\ell^2}.
 \tag{11}
\]
特别 (3) 成立。

证明：\(|\widehat p|\le2A,\ |\widehat c|\le2B\) 及同一 Brownian 分母给
\[
 J_{4,>T}/\mu^4\ll_\sigma \mathcal H_T(r)/(M^4L).
 \tag{12}
\]
这是对最终正响应方向的已证明比较，两份实际 discrepancy 没有被任意系数
Bessel界替换。使用 (1) 的 \(M^4>Y^{2-4\sigma}\ell^2\) 于 (9) 即得 (11)。
令 \(T=T_*\)，四项依次为
\[
 \frac{L^{3/2}}{Y\sqrt W\,\ell^2},\qquad
 \frac1{\ell^2},\qquad
 \frac1{Y\sqrt{LW}},\qquad
 \frac{L^{3/2}}{Y^3W^{5/2}\ell^2}.
 \tag{13}
\]
它们为 \(O(\ell^{-2})\)，且 \(\ell\to\infty\)。
用非负正交分解 \(J_4=J_{4,\le T_*}+J_{4,>T_*}\) 得到等价。\(\square\)

269的中尺度下界不与 (3) 矛盾：该带在 \(T_*=o(Y)\) 之外，
但其保证相对 (1) 的质量尺度至多提出量级
\(L/(Y\ell^2)\to0\) 的必要下界。这里只说已有必要条件不矛盾，
不以此估计真实比值的上界或全频行为。

## 3. 复现计算与两个不同邻点概念 [E]

主代理独立读并运行
`python -B scripts/product_gap_localization_probe.py --max-m 12`。
默认 \(H=\lceil L^2\rceil\) 与273证明一致；
选项 `--h-power 1` 保留本轮早期 \(H=\lceil L\rceil\) 的探索记录。
固定 \(\sigma=1/4\)，在271的浮点最大质量候选和 \(N=2Y\) 上分别计算。

下面所有量仅为有限浮点结果：

| \(Y\) | \(N\) | \(\mathcal G/(Y^3W)\) | 完整gap中异常点自身 / \(Y^3L\) | 异常邻点造成的纯点增量 / \(Y^3L\) |
|---:|---:|---:|---:|---:|
| 16 | 32 | 0.239274 | 0.0307173 | 0.0585309 |
| 64 | 128 | 0.329352 | 0.0223608 | 0.0665624 |
| 256 | 512 | 0.364021 | 0.0107722 | 0.0437982 |
| 1024 | 2048 | 0.376464 | 0.00461703 | 0.0220796 |
| 4096 | 8192 | 0.393492 | 0.00211662 | 0.0110183 |

增量通过同时计算纯支撑自身的 gap 得到；
代码检查 \(\mathcal G_{\rm full}=\mathcal G_P+\text{异常自身}+\text{污染增量}\)，
以及受污染纯点数不超过异常点数的两倍。
这些例子说明“异常点自身小”与“其邻点影响小”是不同账本；
幂次节省由273证明，不由表中趋势推出。

代码另检查通用界 \(\mathcal G\le B_0+B_1/H+E_H\)，
以及实际支撑上可用的两倍版本。
最近整数距离 \(d(k)\) 与最近log距离分别计算，不强行指定同一邻点。
本批不同选择仅发生在整数距离平局；这不保证一般支持或更大实际尺度也如此。

十个实例均通过。两个 \(Y=16\) 例另用独立试除、50位系数和
全邻点 Fraction 账本核验；\(\mathcal G\) 和 \(E_H\) 最大相对差约
\(1.61\cdot10^{-16}\)、\(1.25\cdot10^{-16}\)。
乘积键与表示归属是精确整数；log、Abel权、能量和最大质量排序不是区间认证。
本脚本不实现BC公式，也没有找到271理论大质量筛选的共尾点，更没有计算全频 \(J_4\)。

## 4. 本周期决策与剩余最小输入

**晋级。** 272-(G) 不再保留为开放假设；273给更强的独立算术界，
本篇消除了同一271序列上 \(|\xi|>T_*=o(Y)\) 的相对尾。
本轮之后停止重复优化已够用的最近间距充分证书，把主力转回实际联合响应。

**下一最小引理 [O]。** 先研究同一序列的有限增长区间 \(1\le|\xi|\le T_*\)：
\[
 \frac1{2\pi}\int_{1\le|\xi|\le T_*}
       \frac{|\Re F(\xi)-\Re C(\xi)-M|^4}{\xi^2}\,d\xi
 \ \ll_\sigma M^4L.
 \tag{14}
\]
由 (12) 的同型比较，它足够闭合该中频段的实际响应；
不要求其必要性，也不声称它已弱于RH。
如果这个充分证书失败，仍要检查带 \(|\widehat p|^2+|\widehat c|^2\)
的真正 response，而不是直接宣布full预算失败。
\(|\xi|<1\) 的质量相对低频控制仍单独开放，不能由 (14) 或fixed-frequency PNT补出。

主线仅一条：真实prime--continuum联合四阶控制。
辅助一：有限cutoff的低/中频数值比较，保留实际物理方向及所有中心/端点项。
辅助二：本篇所用外部定理与全部归一化的逆向审计。
只要没有新的算术估计，不继续增加等价矩阵或无限约束族。

| 项目 | 本轮证据或边界 |
|---|---|
| 独立算术输入 | 273的BC行列式公式、有限Selberg权、真实prime-power结构；271的Littlewood振荡 |
| Weil接口 | 仍通过256-C条件性接入prime--continuum capture/Schur；Gamma完备、显式公式与上同调桥梁另立开放输入 |
| 主要反例 | 273稀疏成对支撑反例否定平均密度替代；269--270只排除其准确量词范围 |
| RH循环性 | 完成的尾项来自无条件算术；剩余低/中频预算未被声称更弱、未被选择或紧性制造 |
| 晋级条件 | 证明(14)或真正response中的新交叉抵消/更强下界，进一步缩小开放输入 |
| 止损条件 | 某充分证书失败只停止该证书；真实响应若在所选schedule上迫使归一化比值无界，才停止该schedule |
| 论文归属 | Vaughan--Brownian response；与连续cutoff障碍、广义Weil结构及零点比例论文分开 |

当前作用域为 Riemann 实际正源、固定 \(0<\sigma<1/2\)；
一般L函数和函数域要重建对应的算术接口。
新颖性、外部同行评审、剩余算术预算和完整RH/GRH路线均未完成。

内部定稿复核：carrier_audit 与 gap_exception_audit 分别独立检查
(9)--(13)的四项预算、同一共尾序列量词、269的一致性及(14)仅为充分证书。
两份复核均通过；后者另核查实验脚本的完整/纯支撑、异常自身及污染增量分解。
按反馈澄清连续测度为紧支撑而非有限原子支撑。
主代理独立读并执行脚本；这些内部审计不替代外部同行评审。
