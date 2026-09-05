# 275. 历史记录包络与增长低频的无条件闭合

日期：2026-09-06。主线：NCE-8 / B1z；论文归属：Vaughan--Brownian response。

状态：[T/R] 新的共尾大质量与历史路径联合选择；
[T] 增长低频闭合及双侧移动频带归约；
[N] 端点质量不能替代路径包络的正源反例；
[E] 有限路径复算；[O] 中间频带、完整 Gamma/显式公式及上同调桥梁。
本轮仅 Markdown。没有证明 RH/GRH、新的零点比例或文献新颖性。

后续审计：[277](277-continuum-channel-coercivity-and-double-discrepancy-interface.md)
补出增长中频的连续正通道下界，故本篇(30)的无通道版本在该频带同样必要；
[278](278-fixed-positive-integer-source-record-envelope-obstruction.md)给出满足指定历史guard的固定
正整数替代源反例。两者不改变本篇真实 \(\Lambda\) 新序列的低频证明，
也没有证明其剩余中频预算失败。

## 1. 结论及与旧序列的区别

固定可计算的 \(0<\sigma<\beta<1/2\)，令
\[
 \delta=\beta-\sigma>0,\quad
 L=\log Y,\quad W=\log(2L),\quad
 \ell(Y)=\max(1,\log\log\log Y),\qquad Y=2^m,\ m\ge4 .
 \tag{1}
\]
实际源、\(M,S,D,\mu,J_4\) 与[268](268-prime-jump-cutoffs-and-mass-relative-frequency-reduction.md)、
[274](274-sublinear-frequency-tail-and-remaining-joint-response.md)完全相同。特别
\[
 R(t)=\psi(t)-t,\quad \psi(t)=\sum_{n\le t}\Lambda(n),\quad
 w_Y(t)=t^{-\sigma}e^{-t/Y},
\]
\[
 M(Y,t)=\sum_{2\le n\le t}\Lambda(n)w_Y(n)-\int_1^t w_Y(x)\,dx,
 \quad P_\beta(N)=\max_{1\le n\le N}\frac{|R(n)|}{n^\beta}.
 \tag{2}
\]
最大值只在整数上取；\(R(1)=-1\)，所以 \(P_\beta(N)\ge1\)。

本篇构造一条新的、可认证的共尾 \((Y_j,N_j)\)，满足
\[
 Y_j\le N_j\le2Y_j,\qquad
 |M(Y_j,N_j)|>Y_j^{1/2-\sigma}\sqrt{\ell(Y_j)},\qquad
 P_\beta(N_j)N_j^\delta<C_{\sigma,\beta}|M(Y_j,N_j)|.
 \tag{3}
\]
第二个质量相对条件控制整个历史，不是完整 Weil 正性或未知谱结论。
其存在性由独立 Littlewood 振荡与有限记录选择证明。

沿同一条新序列，
\[
 \boxed{\quad
 \frac{J_{4,\le T}}{\mu^4}\ll_{\sigma,\beta}1+\frac{T^2}{L}
 \quad(T>0).\quad} \tag{4}
\]
因而 \(T_{\rm low}=\sqrt L\) 的低频已无条件闭合。再用274的高频定理，
置 \(T_*=Y\sqrt{W/L}\)，得到
\[
 \boxed{\quad
 J_4=O(\mu^4)
 \quad\Longleftrightarrow\quad
 J_{4,\sqrt L<|\xi|\le T_*}=O(\mu^4).
 \quad} \tag{5}
\]
这里两端都随尺度增长。不是把274同一序列的低频自动补出：
本篇强化了自由 cutoff 选择，不能回填给271原认证程序的任意输出，
也不能回填给268的每 dyadic 首素数规则。原问题256允许自由共尾选择，
故仍在原存在性目标内。

## 2. 记录点保留大质量，而非消耗其强度 [T/R]

记
\[
 d_\beta=1-2^{-\beta},\qquad
 c_1=\frac{2^{-\sigma}e^{-2}d_\beta}{8}>0.
 \tag{6}
\]

### 定理275-A

有共尾 dyadic \(Y\) 及整数 \(N\in[Y,2Y]\) 使
\[
 |M(Y,N)|\gg_{\sigma,\beta}Y^{1/2-\sigma}\ell(Y),\qquad
 P_\beta(N)N^\delta\le\frac{2^\delta}{c_1}|M(Y,N)|.
 \tag{7}
\]
第一式只断言存在正的、未指定常数；不是每个充分大 dyadic 窗口。

证明。Littlewood 的无条件外部定理 [R] 给无界整数 \(Q\) 满足
\[
 |R(Q)|\ge c\sqrt Q\,\ell(Q)
 \tag{8}
\]
（先有任意大实数；取相邻整数的误差至多 \(O(\log Q+1)\)，可吸收）。
在整数 \(1\le n\le Q\) 中取一个真正最大者 \(X\)，写
\[
 K=P_\beta(Q)=|R(X)|X^{-\beta}.
 \tag{9}
\]
则对 \(n\le X\) 有 \(|R(n)|\le Kn^\beta\)，而
\[
 \frac{|R(X)|}{\sqrt X\,\ell(X)}
 \ge c\left(\frac QX\right)^{1/2-\beta}
          \frac{\ell(Q)}{\ell(X)}
 \ge c .
 \tag{10}
\]
此外 \(K\ge cQ^{1/2-\beta}\ell(Q)\to\infty\)，故 \(X\to\infty\)。
这里仅在充分大 \(X,Q\) 使用 \(\ell\)，不存在小自变量的三重对数问题。

令 \(B=2^{\lfloor\log_2X\rfloor}\)、\(a=B/2\)。这些端点均为整数，
且 \(a\le X/2\)。所以
\[
 |R(X)-R(a)|\ge |R(X)|-|R(a)|
             \ge d_\beta |R(X)|.
 \tag{11}
\]
在 \([a,B]\)、\([B,X]\) 两段中，至少一段的振幅不小于
\(d_\beta|R(X)|/2\)。取该段为 \([Y,v]\)，则
\[
 X/4<Y\le X,\qquad Y<v\le2Y,\qquad v\le X .
 \tag{12}
\]
第二段退化时振幅为零，只可能选择第一段。特别，未使用记录点
\(X\) 之后直到 \(2B\) 的任何误差数据。

271-A 的正单调 Stieltjes 振幅引理及整数化误差给
\[
 \max_{Y\le N\le v,\ N\in\mathbb Z}|M(Y,N)|
 \ge \frac{2^{-\sigma}e^{-2}d_\beta}{4}
             Y^{-\sigma}|R(X)|-\frac{e^{-1}}2Y^{-\sigma}.
 \tag{13}
\]
此处 \(w_Y(v)\ge2^{-\sigma}e^{-2}Y^{-\sigma}\)，实 cutoff 到整数
cutoff 的振幅损失不超过 \(w_Y(Y)\)；两个事实的端点均符合271。
因 \(|R(X)|\to\infty\)，选一个真正最大者 \(N\) 后，充分大时
\[
 |M(Y,N)|\ge c_1Y^{-\sigma}|R(X)|
           =c_1KX^\beta Y^{-\sigma}\ge c_1K Y^\delta .
 \tag{14}
\]
结合(10)、\(X\ge Y\) 及 \(\ell\) 非减得到(7)的第一式。
另一方面 \(N\le X\)，所以 \(P_\beta(N)\le K\)；又 \(N\le2Y\)，
故 \(P_\beta(N)N^\delta\le2^\delta K Y^\delta\)，得到第二式。 \(\square\)

### 可认证选择275-B [T]

取固定可计算常数
\[
 C_{\sigma,\beta}=2^{\delta+1}/c_1 .
 \tag{15}
\]
交错搜索全部 \(m\ge4\)、整数 \(Y\le N\le2Y\)，同时认证(3)的两条严格
不等式，每次只输出比上次更大的 \(m\)。
有限和、紧区间积分、\(P_\beta(N)\) 的有限最大值及各阈值都是可计算实数。
有限最大值可以由每项的区间共同夹住，不需要判定平局或识别真正最大者。

(7)第二式相对于(15)留有因子2的严格间隔，第一式相对于
\(\sqrt\ell\) 阈值的比值沿该子族趋于无穷。因此无穷多个窗口存在
严格合格点。采用271的逐阶段精度细化和交错输出，任一严格合格的固定
候选终会被认证；若只有有限输出，最后输出之后的一个合格点给矛盾。
故过程产生(3)的共尾序列，不依赖 Littlewood 常数的有效值。
这不是保证实际可行的复杂度，也不是本轮浮点程序实现了无界认证搜索。

## 3. 由历史误差包络控制整个累计路径 [T]

### 引理275-C

对任意充分大的 \(Y\)、整数 \(N\in[Y,2Y]\)，置
\[
 \tau=\log N,\qquad H(u)=M(Y,e^u)\quad(0\le u\le\tau).
 \tag{16}
\]
令 \(P=P_\beta(N)\)。则
\[
 |H(u)|\le C_0P e^{\delta u},\qquad
 C_0=3+\frac{2\sigma}{\delta}+\frac4{\delta+1},
 \tag{17}
\]
\[
 \|H\|_1\le\frac{C_0}{\delta}PN^\delta,\qquad
 \|H\|_2^2\le\frac{C_0^2}{2\delta}P^2N^{2\delta}.
 \tag{18}
\]
范数只在 \([0,\tau]\) 上取。

证明。对 \(1\le t\le N\)，右连续约定与单位区间内的线性漂移给
\[
 |R(t)|\le |R(\lfloor t\rfloor)|+1
          \le Pt^\beta+1\le2Pt^\beta ,
 \tag{19}
\]
其中 \(P\ge1\)。精确分部积分为
\[
 M(Y,t)=w_Y(t)R(t)+w_Y(1)
             +\int_1^t R(x)(-w_Y'(x))\,dx .
 \tag{20}
\]
下端项 \(w_Y(1)\) 来自 \(R(1)=-1\)，不能遗漏。
使用 \(e^{-x/Y}\le1\)、\(t/Y\le2\)、\(\delta>0\)，右侧绝对值至多
\[
 2Pt^\delta+1+
 2P\left(\frac{\sigma}{\delta}t^\delta+
              \frac{t^{\delta+1}}{Y(\delta+1)}\right)
 \le C_0Pt^\delta .
 \tag{21}
\]
令 \(t=e^u\) 并分别积分指数及其平方，得(17)--(18)。\(\square\)

沿(3)，于是独立得到
\[
 \boxed{\quad\|H\|_1\ll_{\sigma,\beta}|M|,\qquad
                  \|H\|_2^2\ll_{\sigma,\beta}M^2.\quad} \tag{22}
\]
这是新选择提供的额外内容。仅有 \(M\) 的端点下界或窗口内最大性，
不包含整个历史的包络条件。

## 4. 精确中心化、四阶卷积与增长低频 [T]

使用 Fourier 约定 \(\widehat f(\xi)=\int e^{-i\xi u}f(u)\,du\)。
真实 discrepancy 测度仍是
\(r=\int_{[0,\tau]} k_u\,dH(u)\)，\(k_u=(\delta_u+\delta_{-u})/2-\delta_0\)。
这里使用原有限区间的 Stieltjes 测度，不把 \(H\) 零延拓后在 \(\tau\)
新增的 \(-M\) 跳跃计入 \(dH\)。
Stieltjes 分部积分、\(H(0)=0\)、\(H(\tau)=M\) 给
\[
 \widehat r(\xi)
 =M(\cos(\tau\xi)-1)
       +\xi\int_0^\tau H(u)\sin(\xi u)\,du .
 \tag{23}
\]
与274的 \(\Re F-\Re C-M\) 完全一致；中心质量、下端和连续右端均未删除。

令 \(h(u)=\operatorname{sgn}(u)H(|u|)/2\) 于 \(0<|u|<\tau\)，其余为零。
端点值不影响 Lebesgue 范数。则
\[
 \widehat h(\xi)=-i\int_0^\tau H(u)\sin(\xi u)\,du,\quad
 \|h\|_1=\|H\|_1,\quad \|h\|_2^2=\tfrac12\|H\|_2^2.
 \tag{24}
\]
Plancherel 与卷积 Young 不等式给
\[
 \frac1{2\pi}\int_{\mathbb R}|\widehat h(\xi)|^4d\xi
 =\|h*h\|_2^2
 \le\|h\|_1^2\|h\|_2^2
 =\tfrac12\|H\|_1^2\|H\|_2^2 .
 \tag{25}
\]
所有函数均在 \(L^1\cap L^2\)，所以使用卷积及 Plancherel 没有极限漏洞。
这里保留实际累计误差，不是任意系数 Bessel 输入。

还精确有
\[
 \frac1{2\pi}\int_{\mathbb R}
       \frac{(1-\cos(\tau\xi))^4}{\xi^2}d\xi=\frac54\tau .
 \tag{26}
\]
一个直接核验是 \(k_\tau*k_\tau\) 的 primitive 在四个长度为
\(\tau\) 的相邻区间上依次取 \(1/4,-3/4,3/4,-1/4\)，
故平方积分是 \(2\tau((1/4)^2+(3/4)^2)=5\tau/4\)。
Plancherel 给(26)，且明确处理了 \(\xi=0\) 处的消失。

由 \(|a+b|^4\le8(|a|^4+|b|^4)\)，对任何 \(T>0\) 得
\[
 \boxed{\quad
 \frac1{2\pi}\int_{|\xi|\le T}\frac{|\widehat r(\xi)|^4}{\xi^2}d\xi
 \le 10M^4\tau+4T^2\|H\|_1^2\|H\|_2^2 .
 \quad} \tag{27}
\]
第二项中的 \(T^2\) 来自截带后 \(\xi^2\le T^2\)，并未假定高阶导数有界。

沿(3)，(22)将(27)变成 \(O_{\sigma,\beta}(M^4(L+T^2))\)。
真实两个正通道的已证界
\(|\widehat p|^2+|\widehat c|^2\le4(A^2+B^2)\le4S^2\)，
以及268的 \(D\asymp_\sigma S^2L\)，给
\[
 \frac{J_{4,\le T}}{\mu^4}
 \ll_\sigma\frac1{M^4L}
   \frac1{2\pi}\int_{|\xi|\le T}\frac{|\widehat r|^4}{\xi^2}d\xi
 \ll_{\sigma,\beta}1+\frac{T^2}{L}.
 \tag{28}
\]
这证明(4)。只对最终正响应方向取已知上界，没有拆掉两份 discrepancy。

## 5. 与高频合成以及准确剩余输入 [T/O]

274-A 对所有 \(Y\le N\le2Y\) 成立，不绑定旧选择算法。
(3)第一条质量阈值允许在本篇新序列上逐字使用274-B，得到
\[
 J_{4,>T_*}\ll_\sigma\ell(Y)^{-2}\mu^4=o(\mu^4).
 \tag{29}
\]
低频(28)、高频(29)以及三段非负分解证明(5)。
低频只要求 \(O(\mu^4)\)，本篇没有声称它也为 \(o(\mu^4)\)。

下一最小引理仍须估计真正中间响应：
\[
 \frac1{2\pi}\int_{\sqrt L<|\xi|\le T_*}
 \frac{|\widehat r|^4(|\widehat p|^2+|\widehat c|^2)}{\xi^2}\,d\xi
 \ \ll_{\sigma,\beta} M^4D .
 \tag{30}
\]
其无正通道版本
\(\int_{\sqrt L<|\xi|\le T_*}|\widehat r|^4/(2\pi\xi^2)
 \ll M^4L\) 仍只是充分证书；失败时不能直接否定(30)。
式(25)没有消除该难题：把频率权 \(\xi^2\) 放回整个轴，
等价于要求另一个导数/增量预算，不能由 \(L^1,L^2\) 路径界自动获得。
[276](276-short-increment-and-square-root-input-obstructions.md)审计其中两类过强的候选输入。

## 6. 删除审计、正源反例及适用边界

### 反例275-D [N]

保留 log 区间 \([0,\log(2Y)]\) 上的实际连续 Abel 背景 \(b_Y\)。
它是 \(w_Y(x)\,dx\) 在 \(u=\log x\) 下的推前。取其在
\([L-1,L-1/2]\) 的限制 \(\rho\)，质量 \(K\asymp_\sigma Y^{1-\sigma}\)，
令 \(\rho_{-1}\) 是向左平移1的测度。固定 \(M_0>0\)，构造正源
\[
 a_Y=b_Y-\rho+\rho_{-1}+M_0\delta_{L-1/4}\ge0.
 \tag{31}
\]
对每个 \(N\in[Y,2Y]\)，同时将 \(a_Y,b_Y\) 限制到 \([0,\log N]\)，
令 \(H\) 为两者的累计差异。当 \(Y\) 充分大时全部 lag 为正，新增/移走的
质量均已进入，端点差异恒为 \(M_0\)，所以每个端点都是窗口内最大者。
但其累计差异非负，运输部分的积分恰为 \(K\)；故
\[
 \int_0^{\log N}|H(u)|du
   =K+M_0(\log N-L+1/4)\ge K .
 \tag{32}
\]
取 \(M_0=2Y^{1/2-\sigma}\sqrt{\ell(Y)}\)，端点达到大质量阈值，
而 \(K/M_0\to\infty\)。这是正源结构的反例，不是 von Mangoldt 反例，
不否定原271实际序列；只否定“端点大值/最大性自动控制历史路径”的推理。

| 最小输入 | 在证明中的作用 | 删除后的失效 |
|---|---|---|
| 独立 Littlewood 振荡 [R] | (8)--(10)产生共尾的记录与强质量 | 抽象 \(R=0\) 没有质量下界；记录选择本身不产生振荡 |
| \(\sigma<\beta<1/2\) | 左不等式使路径指数可积，右不等式保证记录继承增长 | \(\delta=0\) 时(18)多出 \(\log N\)；本证明不覆盖 \(\sigma=1/2\) |
| \(N\le X\) 的历史记录覆盖 | (19)对整个路径成立 | 用记录点之后的端点不能继续调用同一个 \(K\) |
| 共同 Stieltjes 源及正单调 Abel 权 | (13)、(20)、(23)保持所有端点 | 非匹配 cutoff 或删掉下端项会改变恒等式 |
| 新的 \(P_\beta(N)\) 相对条件 | 把(18)转为真正的质量尺度(22) | (31)--(32)否定仅端点条件的替代 |
| 实际正通道与 Brownian 分母 | (28)接回真实响应 | 没有 \(D\gg S^2L\) 不能直接由无通道积分推出比例 |

路径引理和(27)适用于满足相应假设的一般实累计误差模型；
实际共尾构造和算术应用目前仅对 Riemann 的 \(\Lambda\) 源完成。
一般 L 函数、函数域和复系数需另证相应振荡、实路径替代及正通道分母。
数域显式公式型 Weil 配置与上同调型配置仍不等价；
本篇只经256-C条件性接入 prime--continuum capture/Schur 子系统。

## 7. 文献核验、计算和本周期决策

Littlewood 输入沿用271，并再次核验 Hardy--Littlewood 原论文的
§5.1（印刷页184）与 Theorem5.8（页194）：
[原论文](https://personal.math.ubc.ca/~gerg/teaching/592-Fall2018/papers/1916.Hardy.pdf)。
两页原文已逐页视觉核对；§5.1 明确说明 RH 若失败有更大的振荡，
所以证明中在 RH 分支展开不把定理变成条件结论。端点约定误差见(8)。
高频使用273--274已有独立乘积间距定理，本轮不继续优化其充分证书。

有限计算见 `scripts/record_path_low_frequency_probe.py`。其输出只记[E]，
不认证所有 cutoff 的最大者、无界搜索或渐近频率积分。
主代理独立运行 `python -B scripts/record_path_low_frequency_probe.py --max-m 12`，
固定 \(\sigma=1/4,\beta=3/8\)，复算结果如下。所选 \(N\) 是271候选集的
浮点窗口最大者，不是275-B理论认证程序的输出。

| \(Y\) | \(N\) | \(P_\beta(N)N^\delta/\lvert M\rvert\) | \(\lVert H\rVert_1/\lvert M\rvert\) | \(\lVert H\rVert_2^2/M^2\) |
|---:|---:|---:|---:|---:|
| 16 | 16 | 1.764629 | 2.023630 | 1.718320 |
| 64 | 96 | 1.952653 | 2.871442 | 2.150746 |
| 256 | 346 | 2.289842 | 3.285302 | 2.359260 |
| 1024 | 1422 | 2.539747 | 2.869785 | 1.539389 |
| 4096 | 5380 | 2.864020 | 3.519447 | 2.085392 |

五个窗口全部未达到(3)的第一条大质量阈值，不能称作已找到新的共尾点。
路径按每个整数的 log 单元分段积分，并分割过零单元；12/24阶 Gauss 比较仅为
误差探针，不是区间证书。最小窗口另用独立试除、50位全整数扫描及分段积分核验：
浮点质量差约 \(8.33\cdot10^{-16}\)，两个路径积分差均小于
\(1.37\cdot10^{-15}\)。在 \(\xi=0,1/8,1/2,\sqrt{\log16}\) 上，
(23)两侧50位最大差约 \(9.36\cdot10^{-51}\)；\(5/4\) 核常数另用有理数精确核验。
使用 numpy 2.5.2、scipy 1.18.1、mpmath 1.3.0；约9.8秒，不写结果文件。
该可选探索脚本需要 SciPy，不在标准 CI 清单中。本轮未计算 full \(J_4\)，
也不把实验计入(3)--(5)的证明。

本周期选择：一条主线（新记录序列的中频双误差响应），一条计算辅助，
一条输入强度审计。**晋级的是已经独立闭合的增长低频与(5)的新序列归约**，
不是再给整个 RH 换一种写法。下一周期只研究(30)中的实际交叉结构；
不把路径大小估计擅自升级为中频平滑性或平方根级 Selberg 输入。
若某充分证书失败，仅停止该证书；只有实际响应下界排除新序列，
才停止该序列。David--Lapidus 线仍在限额观察状态，未启动。

内部审计：carrier_audit 独立复核记录构造、端点、可计算选择及增长低频；
gap_exception_audit 独立复核(23)--(29)、归一化及新旧序列量词。
carrier_audit 已对落盘全文逐段逆向复核通过；主代理复核完整证明、276及全部有限复算，
并补明有限区间 Stieltjes 端点与反例的共同截断。内部完整证明不等于新颖性、外部同行评审或
阶段 Goal 的论文级完成，故完整研究目标仍保持开放。
