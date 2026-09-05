# 272. 大质量共尾选择与完整响应的缩小频带归约

日期：2026-09-05。主线：NCE-8 / B1x；论文归属：Vaughan--Brownian response。
本轮仅 Markdown，和障碍论文261--262、269--270分开维护。

状态：[T/R] 独立算术输入支持的共尾高频闭合；
[T] 完整四阶预算到更小增长频带的严格归约；
[T/R，原C] 近乘积间距预算所蕴含的线性频带归约，所需(G)已由273证明；
[O] 剩余联合响应及完整 Weil 桥梁。
不声称 RH/GRH、无条件零点比例改进或完整 mass-only 预算成立。

后续273--274已闭合本篇原下一输入(G)，并在同一271序列上进一步缩到
\(|\xi|\le Y\sqrt{\log(2\log Y)/\log Y}=o(Y)\)。
下文保留原B1x的推导和历史决策；最新开放输入与止损条件见274。

## 1. 本轮真正缩小的输入

固定可计算的 \(0<\sigma<1/2\)。采用271的共尾认证选择
\[
 Y=Y_j=2^{m_j},\quad Y\le N=N_j\le2Y,\quad
 |M(Y,N)|>Y^{1/2-\sigma}\sqrt{\ell(Y)},\quad
 L=\log Y,\quad \ell(Y)=\max(1,\log\log\log Y).
 \tag{1}
\]
这条序列存在的独立算术输入是 Littlewood 振荡 [R]；
271给出 Stieltjes、整数化、dyadic 望远镜及认证选择的完整证明。
本篇不是先假定一个未知的质量下界，再把全部存在性留空。

记
\[
 T_0(Y)=\frac{Y\sqrt L}{\ell(Y)},\qquad
 T_1(Y)=Y\sqrt{\frac L{\ell(Y)}}.
 \tag{2}
\]
本篇证明
\[
 \boxed{\quad J_{4,>T_0}=O_\sigma(\mu^4),\qquad
 J_{4,>T_1}=O_\sigma(\ell(Y)^{-1}\mu^4)=o(\mu^4).\quad}
 \tag{3}
\]
因此沿同一条新序列有
\[
 \boxed{\quad
 J_4=O(\mu^4)\ \Longleftrightarrow\
 J_{4,\le T_0(Y)}=O(\mu^4).
 \quad}
 \tag{4}
\]
这里 \(T_0/Y^2\to0\)，确实小于268的 \(Y^2\) 频带。
但268在每一个大 dyadic 尺度使用首素数相邻对，本篇改用271的自由共尾选择。
不能将这个比较说成“同一 schedule 上的改进”，或声称原自由存在性问题
等价于在本篇特定选择上的 (4)。这是一条更小开放输入的充分研究路线；
它可能丢掉其他本来合格的 schedule。

## 2. 完整物理响应与一致归一化

沿用实际源
\[
 A=\sum_{2\le n\le N}\Lambda(n)n^{-\sigma}e^{-n/Y},\quad
 B=\int_1^N x^{-\sigma}e^{-x/Y}\,dx,\quad
 S=A+B,\quad M=A-B,\quad\mu=M/S.
 \tag{5}
\]
令 \(\alpha,\beta\) 为上述正质量在 lag \(\lambda=\log x\) 下的一侧源，
\[
 k_\lambda=(\delta_\lambda+\delta_{-\lambda})/2-\delta_0,\quad
 p=\int k_\lambda\,d\alpha,\quad
 c=-\int k_\lambda\,d\beta,\quad r=p+c.
 \tag{6}
\]
对零质量测度 \(\eta\)，写 \(F_\eta(x)=\eta((-\infty,x])\)，定义
\[
 D=\|F_p\|_2^2+\|F_c\|_2^2,\qquad
 J_4=\frac{\|F_{r*r*p}\|_2^2+\|F_{r*r*c}\|_2^2}{S^4D}.
 \tag{7}
\]
\(J_{4,>T}\) 是 (7) 分子的两个平方范数在 \(|\xi|>T\) 上的
Fourier 正交压缩后所得商；定义 \(J_{4,\le T}\) 同理。
有限支撑与零质量使 primitive 的 \(L^2\) 表达合法。

两个实际 Fourier 源
\[
 F(\xi)=\sum_{n\le N}\Lambda(n)n^{-\sigma}e^{-n/Y}n^{-i\xi},
 \qquad C(\xi)=\int_1^N x^{-\sigma-i\xi}e^{-x/Y}\,dx
 \tag{8}
\]
给精确恒等式
\[
 \widehat p=\Re F-A,\quad \widehat c=B-\Re C,\quad
 \widehat r=\Re F-\Re C-M.
 \tag{9}
\]
不删除中心质量项 \(-M\)。

268第3节已证明，且 \(N=2Y\) 的端点同样适用，
\[
 S\asymp_\sigma Y^{1-\sigma},\qquad D\asymp_\sigma LS^2.
 \tag{10}
\]
上界只需 Chebyshev 及 \(\log N\le L+\log2\)；
下界来自连续源在 \([Y/2,Y]\) 的正 bulk。
由于 \(|\widehat p|\le2A,\ |\widehat c|\le2B\)，Plancherel 给
\[
 \frac{J_{4,>T}}{\mu^4}
 \ll_\sigma \frac{\mathcal H_T(r)}{M^4L},\qquad
 \mathcal H_T(r)=\frac1{2\pi}
      \int_{|\xi|>T}\frac{|\widehat r(\xi)|^4}{\xi^2}\,d\xi.
 \tag{11}
\]
这里仅对最终正响应方向作幅度控制；两份 discrepancy 仍保留在
\(|\widehat r|^4\) 中。没有用任意系数 Bessel 界替换实际物理方向。

## 3. 缩小频带定理及证明 [T/R]

### 定理272-A

对所有充分大的满足 (1) 质量条件的实际有限源，和任意实 \(T\ge1\)，一致有
\[
 \boxed{\quad
 \frac{J_{4,>T}}{\mu^4}\ll_\sigma
 \frac{L}{T\ell^2}
 +\frac{Y^2L}{T^2\ell^2}
 +\frac1{TL}
 +\frac{Y^2}{T^5L\ell^2}.
 \quad}
 \tag{12}
\]
特别 (3)--(4) 成立。常数不依 \(m_j,N_j\) 或如何选到合格点。

证明：267-E已独立证明实际 prime-power 系数与连续源的四阶尾
\[
 \mathcal H_T(r)\ll_\sigma
 \frac{Y^{2-4\sigma}L^2}{T}
 +\frac{Y^{4-4\sigma}L^2}{T^2}
 +\frac{M^4}{T}
 +\frac{Y^{4-4\sigma}}{T^5}.
 \tag{13}
\]
其输入是实际素数幂乘积纤维、Abel 链预算、Chebyshev、
Montgomery--Vaughan 加权均值 [R] 及保留端点的连续 BV 分部积分。
该定理对任何有限 \(N\ge Y\) 及实 \(T\ge1\) 一致，并非只对整数频率成立。
由 (1)，
\[
 M^4>Y^{2-4\sigma}\ell^2.
 \tag{14}
\]
将 (13)--(14) 代入 (11)，第三项直接约掉实际 \(M^4\)，即得 (12)。

当 \(T=T_0\)，右侧四项依次为
\[
 \frac{\sqrt L}{Y\ell},\qquad 1,\qquad
 \frac{\ell}{YL^{3/2}},\qquad
 \frac{\ell^3}{Y^3L^{7/2}}.
 \tag{15}
\]
它们有界，故第一条 (3) 成立。
当 \(T=T_1\)，依次为
\[
 \frac{\sqrt L}{Y\ell^{3/2}},\qquad\frac1\ell,\qquad
 \frac{\sqrt\ell}{YL^{3/2}},\qquad
 \frac{\sqrt\ell}{Y^3L^{7/2}}.
 \tag{16}
\]
它们为 \(O(1/\ell)\)，且 \(\ell\to\infty\)，得到第二条 (3)。
最后 \(J_4=J_{4,\le T_0}+J_{4,>T_0}\) 是非负分解，
正向丢弃尾项、反向使用 (3)，即得 (4)。\(\square\)

\(T_0,T_1\) 都是显式方便选择，不声称最优。
使用规范频率 \(t=m_j\xi\) 时，剩余范围是
\(|t|\le m_jT_0(Y_j)\)，仍不是固定紧区间。
全部高频积分通过可求和的几何 majorant 处理；
没有以有限数值积分、紧性或 GNS 代替一致误差界。

269的必要质量门槛为 \(Y^{1/4-\sigma}L^{1/4}\)；
(1) 的保证与之相比满足
\[
 \frac{Y^{1/2-\sigma}\sqrt\ell}{Y^{1/4-\sigma}L^{1/4}}
 =\frac{Y^{1/4}\sqrt\ell}{L^{1/4}}\longrightarrow\infty.
 \tag{17}
\]
这消除了该必要条件对本篇选择的排斥，不给剩余频带任何上界。
269的中尺度带 \([K_\sigma Y,2K_\sigma Y]\) 最终仍落在 \(T_0\) 以内。

## 4. 原下一算术输入：已由273闭合 [T/R]

为了继续缩小 (4) 而不重写已闭合高频框架，考虑实际乘积系数
\[
 a_n=\mathbf1_{n\le N}\Lambda(n)n^{-\sigma}e^{-n/Y},\quad
 b_k=\sum_{uv=k}a_ua_v,\quad
 \mathcal K=\{k:b_k>0\},\quad
 \delta_k=\min_{\substack{l\in\mathcal K\\l\ne k}}
                 |\log k-\log l|.
 \tag{18}
\]
充分大 \(Y\) 下支撑至少有两点，故 \(\delta_k>0\)。
原下一最小引理是以下由实际有限算术表达式构成的统一加权近乘积间距预算：
\[
 \boxed{\qquad
 \mathcal G(Y,N):=\sum_{k\in\mathcal K}\frac{b_k^2}{\delta_k}
 \ \ll_\sigma\ Y^{4-4\sigma}L
 \qquad(Y\le N\le2Y).
 \qquad} \tag{G}
\]
本篇初稿时 (G) 尚未证明；273现已给更强的
\(\mathcal G\ll_\sigma Y^{4-4\sigma}\log(2L)\)。
初稿的 \(\delta_k\gg1/k\) 和267仅给 \(Y^{4-4\sigma}L^2\)；
新的证明额外控制异常邻点及纯素数固定行列式近碰撞，而不只使用精确 product fibers。
每个有限实例可计算，但未指定统一常数和起点的渐近 \(O\) 命题
不能由单个有限样本证伪；以下旧表也不是(G)的证明。

### 命题272-B [T/R，原C]：(G)蕴含未知频带可缩至 \(Y\)

269所用局部间距 Montgomery--Vaughan 均值 [R] 对
\(F(\xi)^2=\sum_{k\in\mathcal K}b_k k^{-i\xi}\) 给
\[
 \int_V^{V+U}|F(\xi)|^4\,d\xi
 \le U\sum_kb_k^2+C_{\rm MV}\mathcal G(Y,N).
 \tag{19}
\]
因此在 dyadic 高频区间求和，(13) 的第二项可以换为
\(\mathcal G/T^2\)。若 (G) 成立，结合 (14) 得
\[
 \frac{J_{4,>Y}}{\mu^4}\ll_\sigma
 \frac{L}{Y\ell^2}+\frac1{\ell^2}
            +\frac1{YL}+\frac1{Y^3L\ell^2}=o(1).
 \tag{20}
\]
于是本篇所选 schedule 上的 full budget 等价于
\(J_{4,\le Y}=O(\mu^4)\)。\(\square\)

条件 (G) 只涉及有限的实际素数幂系数与最近乘积间距；
不是把 full Weil 正性、负指数有界或 \(J_4\) 本身作为公理。
其成立已由273的无条件算术证明解决，发表新意仍待外部文献审查。
它只是一个高频充分证书，仍不提供剩余联合响应的预算。
一般而言，此类充分证书失败不能自动否定实际交叉抵消；本例(G)已不属失败候选。

### 有限最近间距探针 [E]

运行 `python -B scripts/product_gap_budget_probe.py`，固定 \(\sigma=1/4\)。
每个窗口先重新计算271的浮点最大质量候选，再分别在该 \(N\) 和 \(2Y\)
上按精确整数 product 聚合全部有序对。相邻 log 间距使用
\(\log(1+(k_{\rm next}-k)/k)\) 计算，避免两个大对数直接相减。

| \(Y\) | 浮点最大质量候选 \(N\) | 该点 \(\mathcal G/(Y^3L)\) | \(N=2Y\) 时 |
|---:|---:|---:|---:|
| 16 | 16 | 0.05430838 | 0.14782546 |
| 64 | 96 | 0.12015327 | 0.16776069 |
| 256 | 346 | 0.10625783 | 0.15795030 |
| 1024 | 1422 | 0.09915210 | 0.14279886 |

主代理独立读脚本并重跑八例。两个 \(Y=16\) 实例另用独立整数试除系数、
50位乘积字典复算，\(\mathcal G\) 最大相对差约 \(1.61\cdot10^{-16}\)。
整数乘积与归属精确；系数、log 间距、能量和最大质量比较仍是浮点，
不是区间证书。这些值没有证明(G)，也不能用平均支持稀疏度替代
加权逆最近间距的统一界。代码仅计算有限实例，不读写结果文件。

## 5. 原B1x周期看板、删除审计与边界

以下“下一”“未证”和止损分支保留初稿时的历史状态；当前周期见274。
原周期至多一条主线、两条辅助线：

- 主线 B1x：271真实共尾质量 + 272缩小频带。下一最小引理优先检查 (G)，
  同时保持 (4) 剩余实际联合响应为最终开放输入。
- 辅助一：有限 \(Y,N\) 的真实 \(\mathcal G/(Y^{4-4\sigma}L)\) 与最大质量探针；
  数值只记 [E]，先不扩写论文或提高阶数。
- 辅助二：核验振荡文献的窗口量词；不把全局 \(\Omega\) 当成每 dyadic 成功。
  268首素数规则和固定大 cutoff 仅保留历史观察。

| 输入 | 用途 | 删除后的失效位置 |
|---|---|---|
| 271独立共尾质量下界、实际非零 \(M\) | (14) 使绝对高频预算可相对化 | PNT上界或抽象选择原理无法支持该除法；接近零质量可使相对尾放大 |
| 固定 \(0<\sigma<1/2\) | 267加权 Abel 链的统一控制 | \(\sigma=1/2\) 的同一证明失去正链指数，未声称端点延拓 |
| 同一有限 \(N\)、保留 \(-M\)、连续端点 BV | (9)、(13) 完整响应 | 不能借纯 Gamma 衰减删除有限 cutoff 端点或中心项 |
| 实际 prime-power 结构与独立均值 [R] | (13) 的两个算术规模 | 对任意外生正源没有这些系数预算 |
| \(S,D\) 统一规模 | (11) 中只剩 \(M^4L\) | 不匹配的 Brownian 分母会改变全部相对幂次 |
| (4)右侧联合预算 [O] | 256的条件性 capture/Schur 接口 | 未由质量分离或尾项闭合产生 |
| 更强的 (G) [原O，现273的T/R] | 用于命题272-B，274已进一步加强 | 不影响定理272-A；单独的gap预算仍不是full预算 |

**循环性审计。** (3)来自已证明的真实算术输入，不是待证结论换名。
(4)的剩余增长频带仍可能包含 RH 级难度；没有声称已经严格弱于 RH。
通过256-C只能条件性接入 prime--continuum 子系统的 capture/Schur。
Gamma 完备化、完整显式公式型 Weil 配置、上同调型结构及二者桥梁仍分别 [O]。
本轮对象为 Riemann 实际正 prime 源；其他 L 函数、函数域需重新证明所用算术输入。

**晋级与止损。** 只有证明 (G)、严格缩小剩余区间，或取得实际联合响应的新上/下界，
才继续晋级。单独验证 (17)、增加小规模矩阵、反复写高频等价均不算新进展。
若真实响应下界迫使 (4) 的比值无界，则停止该具体 schedule；
若只有 (G) 失败，则停止此充分证书。271反例和269--270的连续 no-go
不构成本篇 dyadic schedule 的实际反例。

**文献量词。** 本轮核对的
[Schlage-Puchta，Theorem 3](https://www.mathematik.uni-rostock.de/storages/uni-rostock/Alle_MNF/Mathematik/Struktur/Lehrstuehle/Algebra/papers/Oscillations.pdf)
给带零点与高度条件的 \([X,X^{1+\varepsilon}]\) 振荡；
[Révész，Theorem 5，预印本](https://arxiv.org/pdf/2202.01837)
给参数决定幂次的 \([Y,Y^C]\) 区间。
这里并未核验出可直接用于每个 \([Y,2Y]\) 的结论；
不能让依赖参数随 \(Y\) 变化而忽略原定理阈值。
这只是这两篇来源的适用范围审计，不声称不存在其他相关定理。

271的有限最大质量表未找到满足 (1) 阈值的选点；
本轮没有计算本篇渐近序列的全频响应，也没有任何数值结果升级为渐近定理。
外部新颖性、有效高度、算法效率和论文级独立同行复核仍 [O]。

内部定稿审计：carrier_audit 独立核查271全文及本篇序列量词、归一化和
256接口；sector_compute 独立核查本篇第2--4节全部幂次及(G)的条件性。
两份复核均通过数学主张，并按反馈修正“单个有限样本可证伪未知常数渐近界”
的不当措辞。它们不是外部同行评审。
