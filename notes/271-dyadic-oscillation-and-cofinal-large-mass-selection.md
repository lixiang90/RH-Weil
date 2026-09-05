# 271. Dyadic 局部振幅与实际 Abel 质量的共尾大值选择

日期：2026-09-05。主线：NCE-8 / B1x；论文归属：Vaughan--Brownian response。
本轮以 Markdown 保存，不更新 PDF。

状态：[T] 单调 Stieltjes 变换的双边振幅界及有限候选集；
[R] Littlewood 素数误差振荡；[T/R] 实际 dyadic cutoff 的共尾质量下界；
[T] 可终止的共尾认证选择；[N] 将全局振荡升级为每窗口结论的抽象反例；
[E] 有界最大质量探针；[O] 所选实际响应预算。
内部新引理不声称文献新颖性、RH/GRH 或新的零点比例。

## 1. 问题、独立输入与结论

固定 \(0<\sigma<1\)，\(Y=2^m\)，\(m\ge4\)，\(L=\log Y\)，并置
\[
 \ell(Y)=\max\{1,\log\log\log Y\},\qquad
 w_Y(x)=x^{-\sigma}e^{-x/Y}.
 \tag{1}
\]
以右连续约定 \(\psi(x)=\sum_{n\le x}\Lambda(n)\)，定义
\[
 R(x)=\psi(x)-x,\qquad
 M(Y,t)=\sum_{2\le n\le t}\Lambda(n)w_Y(n)-\int_1^t w_Y(x)\,dx.
 \tag{2}
\]
两个源采用同一有限右端点。记
\[
 O_m=\operatorname{osc}_{[Y,2Y]}R,\qquad
 Z_m=\max_{\substack{Y\le N\le2Y\\N\in\mathbb Z}}|M(Y,N)|,
 \quad \operatorname{osc}_I f=\sup_I f-\inf_I f.
 \tag{3}
\]
振幅允许上、下确界不取到。

本篇证明
\[
 \boxed{\quad
 Z_m\ge\frac{2^{-\sigma}e^{-2}}2Y^{-\sigma}O_m
              -\frac{e^{-1}}2Y^{-\sigma}.
 \quad}
 \tag{4}
\]
再由独立、无条件的 Littlewood 定理 [R]
\[
 R(x)=\Omega_\pm\bigl(\sqrt{x}\log\log\log x\bigr)
 \tag{5}
\]
推出
\[
 \boxed{\quad
 \limsup_{m\to\infty}
 \frac{Z_m}{Y^{1/2-\sigma}\ell(Y)}>0.
 \quad}
 \tag{6}
\]
这里的 limsup 可以无穷。等价地，存在正数 \(c_\sigma\) 及无穷多个 \(m\)
使 \(Z_m\ge c_\sigma Y^{1/2-\sigma}\ell(Y)\)。
结论不是“所有充分大的 \(m\)”。

若 \(\sigma\) 可计算，则还能通过有限算术认证、交错搜索，输出一条
严格递增的共尾 \(m_j\) 和整数 \(N_j\in[Y_j,2Y_j]\)，使
\[
 |M(Y_j,N_j)|>
 Y_j^{1/2-\sigma}\sqrt{\ell(Y_j)},\qquad Y_j=2^{m_j}.
 \tag{7}
\]
不需要知道 (6) 的常数或判定一个窗口确实没有合格点。
今后的研究若要求每一个 dyadic 尺度，不能直接调用本篇；本项目
256-(19) 本来允许一条共尾 matched schedule，故 (7) 没有扩大该存在性问题。
本篇不证明这条 schedule 上的 \(J_4=O(\mu^4)\)。

## 2. 单调 Stieltjes 变换的振幅等价 [T]

### 引理271-A

令 \(a<b\)，\(R\) 是 \([a,b]\) 上实值、右连续的有界变差函数，
\(w\in C^1([a,b])\) 严格为正且非增。令
\[
 A(t)=A(a)+\int_{(a,t]}w(x)\,dR(x).
 \tag{8}
\]
则
\[
 w(b)\operatorname{osc}R
 \le\operatorname{osc}A
 \le w(a)\operatorname{osc}R.
 \tag{9}
\]
这里 \(A(a)\) 任意，不要求变换的总质量为零。

证明：对 \(a\le u<v\le b\)，分部积分给
\[
 A(v)-A(u)
 =w(v)R(v)-w(u)R(u)+\int_u^vR(x)(-w'(x))\,dx.
 \tag{10}
\]
右端中正权重 \(w(v)\) 及 \(-w'\) 的总和为 \(w(u)\)，负项为
\(-w(u)R(u)\)。两者各自除以 \(w(u)\) 都落在
\([\inf R,\sup R]\) 内，故
\(|A(v)-A(u)|\le w(u)\operatorname{osc}R\le w(a)\operatorname{osc}R\)。

反向令 \(g=1/w\)，它正且非减。测度恒等式 \(dA=w\,dR\) 给
\[
 R(v)-R(u)
 =g(v)A(v)-g(u)A(u)-\int_u^v A(x)g'(x)\,dx.
 \tag{11}
\]
负权重总和为 \(g(u)+\int_u^v g'=g(v)\)，所以
\(|R(v)-R(u)|\le g(v)\operatorname{osc}A\le g(b)\operatorname{osc}A\)。
取所有点对的上确界，得到 (9)。连续权使跳点没有额外交叉项；
所有 Stieltjes 增量统一取 \((u,v]\)。\(\square\)

### 推论271-B：真实连续 cutoff 到整数 cutoff

将引理用于 \([Y,2Y]\) 及 \(A(t)=M(Y,t)\)，因为精确有
\(d_tM(Y,t)=w_Y(t)dR(t)\)。对任意 \(t\in[Y,2Y]\)，
\[
 M(Y,t)=M(Y,\lfloor t\rfloor)
                 -\int_{\lfloor t\rfloor}^{t}w_Y(x)\,dx.
 \tag{12}
\]
故实 cutoff 的上确界等于整数 cutoff 的最大值；
实 cutoff 的下确界不小于整数最小值减 \(w_Y(Y)\)。于是
\[
 \operatorname{osc}_{[Y,2Y]}M
 \le\operatorname{osc}_{N\in[Y,2Y]\cap\mathbb Z}M+w_Y(Y)
 \le2Z_m+w_Y(Y).
 \tag{13}
\]
结合 (9) 下界即得 (4)。端点 \(Y,2Y\) 都是整数，是 (12)--(13)
不丢失窗口边界的具体原因。\(\square\)

### 推论271-C：所有整数极值的有限候选集

令
\[
 \mathcal C_Y=\{Y,2Y\}\ \cup\
 \{n-1,n:\ Y<n\le2Y,\ n\text{ 为素数幂}\}.
 \tag{14}
\]
则 \(Z_m=\max_{N\in\mathcal C_Y}|M(Y,N)|\)。
证明：在没有新素数幂的连续整数段内，prime 质量保持不变，连续质量严格增加；
因此 \(M\) 严格下降，绝对值的最大值在该段两端。所有段端点都在 (14) 内。
允许重复点，取集合即可；\(2Y\) 的素数幂跳跃已包含。\(\square\)

这是精确的候选集缩减；不意味着浮点比较能认证真正最大者。
也不意味着只取268的第一个素数相邻对足够获得 (6)。

## 3. 全局振荡产生共尾 dyadic 局部振幅 [T/R]

### 引理271-D

设 \(R\) 局部有界，且对 (1) 的 \(\ell\)，
\[
 |R(x)|\ne o(\sqrt{x}\ell(x))\quad(x\to\infty).
 \tag{15}
\]
则
\[
 \limsup_{m\to\infty}
 \frac{\operatorname{osc}_{[2^m,2^{m+1}]}R}
      {2^{m/2}\ell(2^m)}>0.
 \tag{16}
\]

证明：若不成立，因比值非负，它趋于零。置
\(h_m=2^{m/2}\ell(2^m)\)。任取 \(\varepsilon>0\)，充分大 \(K\) 后
\(O_k\le\varepsilon h_k\) 对 \(k\ge K\) 成立。
对 \(2^m\le x\le2^{m+1}\)，沿 dyadic 端点望远镜分解给
\[
 |R(x)|\le |R(2^K)|+\sum_{k=K}^{m}O_k
 \le |R(2^K)|+
       \varepsilon\,\ell(2^m)\sum_{k=K}^{m}2^{k/2}
 \le |R(2^K)|+\frac{\varepsilon}{1-2^{-1/2}}h_m.
 \tag{17}
\]
使用了 \(\ell\) 非减，以及 dyadic 的几何增长。因为
\(\sqrt{x}\ell(x)\ge h_m\to\infty\)，先令 \(m\to\infty\)，再令
\(\varepsilon\downarrow0\)，得到与 (15) 矛盾的小量结论。\(\square\)

将 (5) 代入引理，并使用 (4)，其中整数化误差满足
\[
 \frac{Y^{-\sigma}}{Y^{1/2-\sigma}\ell(Y)}
       =\frac1{\sqrt Y\,\ell(Y)}\longrightarrow0,
 \tag{18}
\]
即证明 (6)。这一步不要求 \(\sigma<1/2\)；该限制只在272调用四阶
prime-power 高频预算时加入。

### 外部定理核验 [R]

使用 Hardy--Littlewood 的原始论文
*Contributions to the theory of the Riemann zeta-function and the theory of
the distribution of primes*, Acta Mathematica **41**, 119--196，
[原文 Theorem 5.8，印刷页194；`5.1，页184](https://personal.math.ubc.ca/~gerg/teaching/592-Fall2018/papers/1916.Hardy.pdf)。
`5.1 明确陈述双向、任意大 \(x\) 的结论；证明在 RH 分支展开是因为
RH 若失败已有更大的振荡，而不是定理附加 RH 前提。
原文 prime-power 计数记号见页121的定义；端点左/右或半权约定最多相差
\(\Lambda(n)=O(\log x)=o(\sqrt{x}\ell(x))\)，故本篇固定右连续约定不改变 (5)。
本篇只调用该经典结论，不把它作为本项目新定理。

## 4. 不依赖未知振荡常数的共尾认证选择 [T]

固定可计算的 \(\sigma\in(0,1)\)。由 (6) 沿无穷多个窗口有
\[
 \frac{Z_m}{Y^{1/2-\sigma}\sqrt{\ell(Y)}}
 \ge c_\sigma\sqrt{\ell(Y)}\longrightarrow\infty.
 \tag{19}
\]
因此无穷多个窗口的有限候选集中存在严格满足 (7) 的点。

每个固定 \((m,N)\) 的 \(M\) 是有限个可计算实数之和减紧区间光滑积分。
可用认证有理区间，以任意给定绝对误差计算 \(M\) 和 (7) 右侧正阈值。
下面的交错程序构造一条共尾序列：

1. 按阶段 \(s=4,5,\ldots\)，列出全部 \(4\le m\le s\) 的有限候选集。
2. 对尚未丢弃的每个候选及其阈值，计算宽度不超过 \(2^{-s}\) 的认证区间。
3. 若 \(|M|\) 的区间下界大于阈值区间上界，该点被认证。
   在当前已认证且 \(m\) 大于上次输出指标的点中，按固定次序输出一个；
   以后只保留更大的指标。

每阶段是有限计算。任一严格合格的固定候选在充分晚的阶段一定被认证。
若输出只有有限多个，最后指标以上仍有一个严格合格点，最终必被认证并输出，
矛盾。故输出无限，且 \(m_j\) 严格递增，从而共尾。
不假定能判定两个可计算实数相等，不会停在某个不合格窗口等待；
不保证输出首个合格窗口，也不声称有可用的规模上界或复杂度界。\(\square\)

该存在性证明使用真实素数误差的独立下界 (5)；交错选择本身不产生正性，
更没有产生响应四阶预算。本轮脚本也没有实现认证区间或此无界程序。

## 5. 量词障碍、删除审计及模型边界

### 反例271-E [N]：全局 \(\Omega_\pm\) 不推出每窗口振荡

取非负光滑函数 \(\phi\) 支撑在 \((5/4,7/4)\)，且 \(\phi(3/2)=1\)。
令 \(Y_k=2^{3k}\)，从充分大的 \(k\) 开始定义局部有限和
\[
 R_*(x)=\sum_k(-1)^k\sqrt{Y_k}\ell(Y_k)\phi(x/Y_k).
 \tag{20}
\]
它光滑，且在 \(x=3Y_k/2\) 上正负交替达到
\(\asymp\sqrt{x}\ell(x)\)，所以满足 (5) 同型的双向振荡。
但在每个 \([2^{3k+1},2^{3k+2}]\) 上恒为零。
故不能只靠一个全局 \(\Omega\) 定理把 (6) 改成所有充分大的 \(m\)。
这是逻辑推理的反例，不是 von Mangoldt 或 Euler product 反例。

| 最小输入 | 具体作用 | 删除后的失效 |
|---|---|---|
| 实值 BV、共同 Stieltjes 增量 | (10)--(11) 给双边振幅及整数端点桥 | 脱离同一 \(dM=w\,dR\)，质量可恒零而 \(R\) 任意振荡 |
| \(w>0\)、非增 | \(1/w\) 可逆，分部积分两侧权重各同号 | 允许 \(w=0\) 时下界失败；若端点权都为1而内部权为大数 \(K\)，在内部放一个单位上跳，\(\operatorname{osc}A=K>\operatorname{osc}R\)，上界失败 |
| 整数边界及单位区间连续漂移 | (12)--(14) 的显式误差和候选集 | 非整数窗口不能原样使用其左端 floor 而不检查是否出界 |
| 独立 Littlewood 振荡 [R] | (15) 与共尾大质量 | 取 \(R\equiv0\)，变换恒定且可为零，几何本身没有下界 |
| dyadic 几何增长、\(\ell\) 非减 | (17) 的求和只损失常数 | 不能对任意稀疏/密集尺度不加检查地使用同一论证 |
| 严格阈值、有限认证、交错搜索 | 选择的可终止性和共尾性 | 逐窗口等待一个真值可卡在不合格窗口；浮点排序不是认证 |

没有引入酉谱、Weil 完全正或负指数有界等强公理。
引理271-A是一般实 Stieltjes 模型定理；271-D是一般 dyadic 推理。
实际应用 (6)--(7) 目前仅对 Riemann 的 \(\Lambda\) 源核验。
Dedekind、实 Dirichlet、复自守系数、函数域模型需分别提供适合的误差振荡、
实值/复值替代和响应估计；不能默认两类 Weil 结构等价。

## 6. 有界计算记录 [E]

主代理独立运行
`python -B scripts/dyadic_max_mass_cutoff_probe.py --max-m 20`。
固定 \(\sigma=1/4\)，在 (14) 全部候选上用 float64 搜索，
再对前五名、所选点附近整数及268首素数相邻对作50位全和复算。
下面 \(Z_{\rm float}\) 只表示浮点候选最大值，不是认证最大值。

| \(m\) | 候选所选 \(N\) | \(Z_{\rm float}/L^{1/4}\) | \(Z_{\rm float}/Y^{1/4}\) |
|---:|---:|---:|---:|
| 4 | 16 | 0.625865 | 0.403805 |
| 6 | 96 | 0.748060 | 0.377690 |
| 8 | 346 | 0.818468 | 0.313993 |
| 10 | 1422 | 1.157840 | 0.332108 |
| 12 | 5380 | 1.158518 | 0.245932 |
| 16 | 69990 | 2.226915 | 0.253992 |
| 18 | 302830 | 3.214135 | 0.266965 |
| 20 | 1090696 | 4.220294 | 0.254482 |

八个窗口全部 \(\ell(Y)=1\)，没有一个浮点最大值达到 (7) 阈值。
所以本轮实验尚未找到理论共尾选择中的点，不能将这张表称作该选择的实现。
这也不反驳只在任意大尺度共尾成立的 (6)--(7)。

最小 \(m=4\) 另以独立整数试除确定 \(\Lambda\)，全扫17个整数 cutoff，
50位结果和候选缩减相符。全部检查点的最大浮点质量差约
\(2.87\cdot10^{-10}\)，连续积分差约 \(4.26\cdot10^{-11}\)。
这只是 smoke test；未检查点的排序和全局误差没有区间证明。
脚本使用 numpy 2.5.2、scipy 1.18.1、mpmath 1.3.0，不安装依赖、不写结果文件。

## 7. 路线决策与后续接口

本轮晋级内容是由独立素数振荡证明共尾大质量，并在272把未控制的频率范围缩小。
不是仅检查269必要条件后就声称响应预算成立。
主线改为 (7) 的自由共尾 schedule；268的首素数规则保留观察，不把结论回填给它。
下一最小算术引理、晋级/止损及完整 Weil 接口见272第5节与研究看板。

PDF 暂不加入本篇。下一次同步障碍论文时，另应在旧稿
`lem:uniformmoments` 与 `lem:signedtail` 的陈述中显式加入
“sufficiently large real \(Y\)”；对应269--270 Markdown已有该范围，
这项排版范围修补不改变本篇结论。
内部定稿审计：carrier_audit 独立逐段复核本篇证明、端点约定、可计算选择、
反例与适用范围，全部通过；sector_compute 另复核272使用的质量幂次及本篇
八个有限窗口没有达到理论筛选阈值。主代理独立重跑完整最大质量脚本。
这不是外部同行评审；外部复核及新颖性审查仍 [O]。
