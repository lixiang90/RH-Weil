# 277. 连续响应通道的强制性与双误差中频接口

日期：2026-09-06。主线：NCE-8 / B1z；论文归属：Vaughan--Brownian response。

状态：[T] 固定频率阈值以上的真实正通道双边比较；
[T] 275新序列上的完整双误差导数判据；[E] 有限中频复算；
[O] 实际 von Mangoldt 双误差预算。
本篇的等价判据本身不算新的算术 saving。与[278](278-fixed-positive-integer-source-record-envelope-obstruction.md)的固定正整数源障碍合用，
用于排除“历史包络、正源及一致性足以自动闭合中频”的软推理，
并修正上一轮对最高中频壳及充分/必要性的保守登记。
不证明 RH、Gamma 完备配置或文献新颖性；本轮仅 Markdown。

## 1. 对象与最小输入

固定 \(0<\sigma<1\)，置 \(a=1-\sigma>0,L=\log Y\)。
令 \(Y\ge4\)，有限整数 \(Y\le N\le2Y,\tau=\log N\)，连续 Abel 正源
为 \(w_Y(x)\,dx=x^{-\sigma}e^{-x/Y}\,dx\) 在 \(u=\log x\) 下的推前。
记为 \(b\)，并令 \(\alpha\) 为 \([0,\tau]\) 上任意有限正测度，满足
\[
 A=\alpha([0,\tau])\le C_A Y^a,\qquad
 B=b([0,\tau]),\quad S=A+B,\quad M=A-B .
 \tag{1}
\]
真实 von Mangoldt 源满足(1)，只需 Chebyshev 上界及 Abel 分块；
本篇的通道引理也适用于正整数替代源，不预设 Euler 乘积。

统一使用
\[
 k_u=(\delta_u+\delta_{-u})/2-\delta_0,\quad
 p=\int k_u\,d\alpha,\quad c=-\int k_u\,db,\quad r=p+c,
\]
\[
 D=\|F_p\|_2^2+\|F_c\|_2^2,\qquad
 J_4=\frac{1}{S^4D}\frac1{2\pi}\int_{\mathbb R}
 \frac{|\widehat r|^4(|\widehat p|^2+|\widehat c|^2)}{\xi^2}\,d\xi .
 \tag{2}
\]
\(F_\eta(x)=\eta((-\infty,x])\)，Fourier 约定为 \(e^{-i\xi u}\)。
零质量及紧支撑使全部 primitive 能量合法。设
\[
 C(\xi)=\int_1^N x^{-\sigma-i\xi}e^{-x/Y}\,dx,\quad
 \widehat c(\xi)=B-\Re C(\xi).
 \tag{3}
\]
这里的 \(+B\) 正是中心化项；它不随 \(|\xi|\) 增大而衰减。

## 2. 固定阈值以上，真实第三通道不能隐藏双误差能量 [T]

### 定理277-A

存在仅依赖 \(\sigma\) 的有限 \(K_\sigma>0\)，使所有(1)中的源在
\(|\xi|\ge K_\sigma\) 上满足
\[
 c_{\sigma,C_A}S^2
 \le|\widehat p(\xi)|^2+|\widehat c(\xi)|^2
 \le4S^2,\qquad D\asymp_{\sigma,C_A}S^2L .
 \tag{4}
\]

证明。令
\[
 b_\sigma=e^{-1}\frac{1-2^{-a}}a,\qquad m_\sigma=a^ae^{-a}.
\]
连续 bulk 给
\[
 B\ge\int_{Y/2}^{Y}w_Y(x)\,dx\ge b_\sigma Y^a,\qquad
 B\le\Gamma(a)Y^a,\quad S/B\le1+C_A/b_\sigma.
 \tag{5}
\]
密度 \(g(u)=e^{au-e^u/Y}\) 单峰，最大值不超过 \(m_\sigma Y^a\)。
限制到 \([0,\tau]\) 再零延拓的总变差不超过 \(2m_\sigma Y^a\)；
包括 \(0,\tau\) 两端跳跃。因此 BV 分部积分给
\[
 |C(\xi)|\le\frac{2m_\sigma Y^a}{|\xi|}
 \le\frac{2m_\sigma}{b_\sigma|\xi|}B .
 \tag{6}
\]
取 \(K_\sigma=4m_\sigma/b_\sigma\)，便有
\(\widehat c\ge B/2\)。用(5)及
\(|\widehat p|\le2A,|\widehat c|\le2B\)，得(4)的通道比较。
此处并未把 \(C\) 的衰减错当作 \(\widehat c\) 的衰减。

正源 Brownian 恒等式为
\[
 D=\frac12\iint\min(u,v)
       \bigl(d\alpha(u)d\alpha(v)+db(u)db(v)\bigr).
 \tag{7}
\]
上界为 \(D\le\tau(A^2+B^2)/2\ll S^2L\)。
下界仅保留 \(x\in[Y/2,Y]\) 的连续 bulk，其 lag 至少
\(L-\log2\ge L/2\)，质量至少 \(b_\sigma Y^a\)，故
\(D\ge b_\sigma^2Y^{2a}L/4\gg_{\sigma,C_A}S^2L\)。\(\square\)

对于可测集 \(E\subset\{|\xi|\ge K_\sigma\}\)，定义
\[
 Q_E=\frac1{2\pi}\int_E\frac{|\widehat r|^4}{\xi^2}\,d\xi .
 \tag{8}
\]
令 \(J_{4,E}\) 为(2)的相应频带贡献。当 \(M\ne0,\mu=M/S\) 时，
定理277-A逐点给
\[
 \boxed{\quad
 \frac{J_{4,E}}{\mu^4}\asymp_{\sigma,C_A}\frac{Q_E}{M^4L}.
 \quad} \tag{9}
\]
不要求 \(E\) 连通，不要求其长度有下界，也不使用有限采样外推。
若 \(M=0\)，保留未除质量的 \(J_{4,E}\asymp Q_E/(S^4L)\)，不能约去 \(M^4\)。

这用的是267-(18)及269中已有的 BV/连续方向机制，现将其固定阈值和全频带
量词单独写出；不声称一种新的 Fourier 定理。
对任意原子背景不能无条件使用(6)：例如 \(\alpha=b=A\delta_{u_0}\) 时，
在 \(\xi=2\pi k/u_0\) 两个中心化通道同时消失，没有(4)的固定阈值下界。
故连续 Abel 背景是实际使用的结构，不能仅写成“两个正源”。

## 3. 接回275的新序列：无通道预算也必要 [T]

以下固定 \(0<\sigma<\beta<1/2\)，沿275-B的新共尾序列。
275-(22)、(27)给
\[
 Q_{\{|\xi|<K_\sigma\}}\ll_{\sigma,\beta}M^4L .
 \tag{10}
\]
由(9)、全频的上界 \(|\widehat p|^2+|\widehat c|^2\le4S^2\) 以及
(10)，有一致仿射比较
\[
 \frac{J_4}{\mu^4}\ll_{\sigma,\beta}\frac{Q_{\mathbb R}}{M^4L},
 \qquad
 \frac{Q_{\mathbb R}}{M^4L}\ll_{\sigma,\beta}1+\frac{J_4}{\mu^4}.
 \tag{11}
\]
因而沿该序列
\[
 \boxed{\quad J_4=O(\mu^4)
       \quad\Longleftrightarrow\quad Q_{\mathbb R}=O(M^4L).\quad}
 \tag{12}
\]
同样，275的剩余中频
\[
 E_Y=\{\sqrt L<|\xi|\le T_*\},\qquad T_*=Y\sqrt{\log(2L)/L}
 \tag{13}
\]
在充分大 \(Y\) 后全落于固定阈值之外，所以(9)直接适用。
275称“无通道版本仅作充分证书”是当时尚未证明逆向比较的保守表述；
本篇现在补出了它对该实际中频的必要性。若其归一化能量沿实际序列无界，
真实响应也无界，不能再以第三正通道或重新命名物理方向规避。
但一般模型的失败不构成真实 \(\Lambda\) 源的反例。

## 4. 两份误差的真正目标，而非单误差平滑性 [T/O]

令 \(H(u)=M(Y,e^u)\) 于 \([0,\tau]\)，并令 \(G\) 为其奇延拓后在
\([-\tau,\tau]\) 外置零。这里 \(H(0)=0,H(\tau)=M\)；
分布导数 \(dG\) 包括零延拓端点，不能删除。
因为 \(G\) 为紧支撑 BV 且属于 \(L^1\cap L^2\)，
\[
 q=G*G,\qquad q'=G*dG\in L^2
 \tag{14}
\]
是对每个有限源合法的恒等式；它本身没有给一致质量预算。
由275的精确 Stieltjes 公式，记
\[
 S_H(\xi)=\int_0^\tau H(u)\sin(\xi u)\,du,\quad
 e(\xi)=M(\cos(\tau\xi)-1),
\]
则 \(\widehat G=-2iS_H,\widehat r=e+\xi S_H\)。因此
\[
 \frac1{2\pi}\int_{\mathbb R}\xi^2|S_H|^4\,d\xi
 =\frac1{16}\|q'\|_2^2,\qquad
 \frac1{2\pi}\int_{\mathbb R}\frac{|e|^4}{\xi^2}\,d\xi
 =\frac54M^4\tau .
 \tag{15}
\]
对 \(\widehat r=e+\xi S_H\) 和 \(\xi S_H=\widehat r-e\)
分别使用四次三角上界，可得
\[
 Q_{\mathbb R}\le10M^4\tau+\frac12\|q'\|_2^2,\qquad
 \|q'\|_2^2\le128Q_{\mathbb R}+160M^4\tau .
 \tag{16}
\]
结合(12)，275同一新序列上的完整实际预算等价于
\[
 \boxed{\quad \|(G*G)'\|_2^2=O(M^4L).\quad} \tag{17}
\]
这明确了双误差对象，不是独立证明了(17)，也不声称它已知弱于 RH。
由276可知，先用 \(\|G\|_1^2\|\Delta_hG\|_2^2\) 代替
\(\|\Delta_h(G*G)\|_2^2\)，再要求单误差的质量相对 Lipschitz 界，会失败。
278进一步检验：即使不拆掉这两份误差，历史包络及正性本身也不能提供(17)。

## 5. 修正下一目标、证据及停止条件

上一轮看板把 \([T_*/2,T_*]\) 列为下一待闭合壳，并不准确。
274-B 对任意固定 \(c>0\)，直接给
\[
 J_{4,>cT_*}=O_{\sigma,c}(\ell(Y)^{-2}\mu^4)=o(\mu^4).
 \tag{18}
\]
所以有限个这样的最高壳已经覆盖，重证它们不算新进展。
全局增量 \(\|\Delta_{1/T_*}(G*G)\|_2\) 又同时测到较低频率；
它的失败不自动否定最高壳本身，这是276接口必须保留的单向性。

主线下一最小问题改为：在(13)中确实未被现有尾界覆盖的增长频率，
例如 \(\log Y\le|\xi|\le2\log Y\)，直接估计实际双误差四阶能量，
或获得一个能覆盖并可和地拼接这些中频段的算术界。
不得仅以(12)/(17)的等价改写晋级。

有限证据由可选脚本 `scripts/midband_double_discrepancy_probe.py` 提供：
实际 prime/continuum 中心化、独立 Brownian 分母、双误差项都保留；
有限窗口仍使用271的浮点最大质量候选，不是275认证序列。
主代理独立运行 `python -B scripts/midband_double_discrepancy_probe.py`，
固定 \(\sigma=1/4,\beta=3/8\)。下表只取内部壳
\(\{\log Y\le|\xi|\le2\log Y\}\)，积分已包含正负两侧，
\(E=(2\pi)^{-1}\int_{\rm shell}\xi^2|S_H|^4\,d\xi\)。

| \(Y\) | 所选 \(N\) | \(Q/(M^4L)\) | \(E/(M^4L)\) | \(J_{4,\rm shell}/\mu^4\) |
|---:|---:|---:|---:|---:|
| 16 | 16 | 0.00857955 | 0.00966036 | 0.0357837 |
| 64 | 96 | 0.0117743 | 0.000743144 | 0.0395009 |
| 256 | 346 | 0.0116426 | 0.000252307 | 0.0359473 |
| 1024 | 1422 | 0.0561814 | 0.00786900 | 0.159672 |

另算了 \(U=\sqrt L,T_*/2\) 的两类对照壳；它们与内部壳可重叠，
所以不将三项相加冒充频带分解。所有样本都未达到275大质量阈值。
连续 lag Gauss10/18 与频率 Gauss8/12 的最大相对差约
\(2.12\cdot10^{-11}\)；首次频率面板宽0.5在最大窗口未通过检查，
改为0.25后通过，不能将阶数差当作认证误差界。
最小窗口的第一完整壳以独立试除、MP50自适应积分核验四个量，
最大相对差约 \(1.56\cdot10^{-14}\)；直接逐整数单元积分 \(H\) 的正弦变换，
Stieltjes恒等式最大差约 \(1.17\cdot10^{-49}\)。
36个连续项 incomplete-gamma 独立样本的最大归一化差约
\(2.49\cdot10^{-15}\)。完整 Brownian 分母另由 prime min-kernel 与连续尾平方积分得到，
不使用截带分母。实际源的下端项、中心质量与右端点全部保留。
使用 numpy 2.5.2、scipy 1.18.1、mpmath 1.3.0，约15.1秒；脚本不写输出文件，
不在标准CI清单中。采样最小 \(\widehat c/B\) 不是全区间下界。
这些数值均不进入(4)--(18)的证明，也没有验证 full \(J_4\) 或275认证选择。

| 审计项 | 结论或边界 |
|---|---|
| 独立算术输入 | 实际源的质量上界只需 Chebyshev；新序列引用275，尾界引用274，无新增平方根级假设 |
| Weil 接口 | 仍是256-C的条件性 prime--continuum capture/Schur；Gamma和上同调桥梁独立开放 |
| 主要反例 | 原子背景可令通道反复消失；278检验保持实际连续背景和固定整数源的更强障碍 |
| 非循环性 | (17)被明确标为开放的等价预算，不作为结构公理；没有从GNS、紧性或选择产生它 |
| 晋级条件 | 实际中频的新增估计，或有完整证明、模型边界清楚的结构障碍 |
| 止损条件 | 不再把最高固定倍数壳当开放任务，不再指望增长中频的第三通道隐藏bare能量 |
| 论文归属 | 独立Vaughan--Brownian response材料；不与四矩比例或完整Weil存在性混篇 |

本篇与264的局部结果不同：这里使用完整有限源、没有局部 carrier 分离条件，
代价是沿275的历史包络序列使用(10)。不能将它无条件回填给任意旧cutoff。
内部复核：carrier_audit 独立逐段复核(4)--(18)的常数、一般正源量词、
零质量分支和全源归一化通过；主代理完整复算脚本并核对恒等式。
更强模型障碍见278；新颖性和外部同行复核仍[O]。
