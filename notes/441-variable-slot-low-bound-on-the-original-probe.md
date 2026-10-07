# 441. 在原补偿 probe 上支付可变槽的完整 low 估计

2026-10-07。准确的通用反射能量、row sectors、光滑分离和 additive Gram 为外部 [R] 输入；
下述同源低侧扩域为 [T/R]。不引用仅对 ell=1/6 声明的 fixed-geometry low proposition，
也不需要新无零假设。新边界的实际 high、capacity 和全轮廓仍未完成。

## 1. 对象和确切上游输入

来源仍为 OpenAI/math 提交 `adc7f1241b42e322a6451854ab7e4b4c146bf78a` 的
[September-30 paper.tex](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)。
使用原算术数据 S,T,b_*,xi、原 I_eta、finite compensation `eq:compensated-probe-definition`，
原 annular slot windows、Gaussian、ray calibration 和所有 zero-on-nonunit masks。
改变 X、Y 和固定槽的总长度；不另造可平均的 probe。

本稿直接调用并核对如下通用条款，而不调用 `prop:probe-low` 或 `lem:probe-row-norm` 的固定参数结论：

| 原 label | 实际可用范围与保留事项 |
|---|---|
| `lem:smooth-calculus`、`lem:gaussian-annular` | 固定有限维 joint profile；加权 Fourier seminorm 与全部 annular 尾，未限制 ell=1/6 |
| `lem:reflection-row-sectors` | 所有原元素行，包括与 S 相交者；有限单位/ray/reflection sectors 与零延拓保留 |
| `lem:reflected-energy`，7663–7804行 | log lengths 在固定 bounded sets；disjoint slots、product coefficients、actual residual dyad、共同密度和既有 zero mask；已包含 powerful fixed parts 的计数 |
| `prop:probe-gram`，8340–8364行 | 任意 Q,Y′>=1 的固定 polynomial ranges，P_a=Y′²/Q>=1；实际 ray/Gauss 系数，不接受任意 row-dependent 系数 |

这些条款及其系数级原反射身份为 [R]；本项目没有重新证明整篇原论文或其外部依赖。
以下证明逐前件核新参数；这是引用确切已声明的通用分析结果，不增加新的猜想型前件。

## 2. 可变参数与 low 结论

固定 1/6<=ell<=1/5、b=1/8，取有限个固定 disjoint prime slots，ell_i>0、sum ell_i=ell。
槽窗及其 annular norm ratios 在 Z 之前固定；槽系数仍为原 unit-modulus arithmetic phase 乘固定窗。
令

\[
 l_x=(1-\ell-b)/2,\quad l_y=(1-\ell+b)/2,\quad M=1-\ell,
 \quad h=1-l_x+\ell,
 \quad X=Z^{l_x},\ Y=Z^{l_y}.
 \tag{1}
\]

对原有限补偿表达式 I_modified，任意 epsilon>0 有

\[
 \boxed{|I_{\eta,\mathrm{modified}}(Z)|
 \ll_{\mathrm{fixed},\epsilon}Z^{(1-\ell)/4-b/6+\epsilon}.}
 \tag{2}
\]

常数和阈值可依赖固定算术、ell、槽系统、测试及已固定目标，不依赖 moving tuples、当前行或素数标签；
指数中的任意 epsilon 在目标前指定。
这是 low 估计，不是对所有 H_eta/L_eta 的 high 延拓结论。

## 3. 逐 subset 的实际完成行

固定 rescaled subset J，d_J=sum_{i in J}ell_i，ell′=ell−d_J、M′=M−2d_J。
这里 d_J 是补偿 subset 长度，不是 439 的 high 物理行长度。
固定 p_J 的 norm ratio r_J=q_{p_J}/Z^{d_J} 在一个固定紧区间内。
原准确分离的 A_m、B_m^J 保留同一个行球

\[
 Q=q_{b_*}X'Y',\quad X'=XZ^{-d_J}/r_J,\quad
 Y'=YZ^{-d_J}/r_J,\quad Q\asymp Z^{M'}.
\]

所有幸存标记槽在 B^J 内先求和；行球仅依赖固定 p_J，不依赖这些标记标签或 dual variables。
原 completed index 仍是 c n³，c,n 可以共素因子，权重 q_c^{-1/2}q_n^{-1} 不变。
Gaussian 按 r=q_{cn³}/Z^{1+ell′} 作 fixed translate annular partition。
在 annulus log r=k+O(1) 上保留原共同 profile

    chi(log x) W_G(e^k x / product varrho_i) product W_i(varrho_i).

它的所有 weighted Fourier seminorm 对 k 可求和。
选小 kappa_G 后，只丢 |k|>kappa_G log Z+constant 的 whole annuli；这些尾先用原绝对计数，
再用 Gaussian 衰减做到任意负幂。
保留 N_*=1+ell′+theta_N、|theta_N|<=kappa_G+O(1/log Z) 的完成尺度，
共同 Fourier 密度在任何行和 tuple 分离之前固定；归一化不随 e^k 改变。
对每个分离变量，slot coefficients 仍为原相位、annular cutoff 与单位模 norm power 的乘积，
独立于行和其他槽。因此直接符合通用 reflected-energy 的前件。

## 4. 反射行范数中的正损失准确保留

依原 row-sector reduction 冻结 powerful row part，长度 O；实际 residual squarefree dyad 长度 H。
令 Delta_H=M′−O−H>=−epsilon_Z，其中 epsilon_Z=O_fixed(1/log Z)。
f=rho=1，非槽 moving primes 都来自行，故

\[
 2A_0\le O+\epsilon_Z,\quad N_0\le A_0,\quad z_a\le\ell'.
\]

通用 lemma 的可用 dual 长度为

\[
 T_d=2H+2A_0+2z_a-1-\ell'-\theta_N-N_0-3B_0.
\]

由 M′+ell′−1=−3d_J，准确相减给

\[
 T_d-(H-3d_J)
 =H-M'+2A_0+2(z_a-\ell')-N_0-3B_0-\theta_N
 \le 2\epsilon_Z+|\theta_N|. \tag{3}
\]

所以这个关键步骤并不依赖 ell=1/6。
retained dual source ideals n,b 保留原允许的 S-primes 和 shared primes，不添加独立 coprimality mask。
负单位 dyads 只贡献 O(epsilon_Z)；原 retained support 给
max(H,v+ell_b)=H+O(epsilon_ref+kappa_G+epsilon_Z)。

在反射能量的 s_hyb=min{v,z_a,(v+z_a)/3} 分支：若 s_hyb=z_a，直接得
E_ref<=M′−Delta_H+small losses。
否则沿原 retained support 的 y=v+3ell_b+e_lambda，
先从共同密度提取 kernel saving，再平方，再作 positive sieve enlargement；原完整式给

\[
 E_{\rm ref}\le M'+
 \frac{1+3\ell'-2M'-2\Delta_H+\theta_N}{4}
 +O(\epsilon_{\rm ref}+\kappa_G+\epsilon_Z).
\]

分子中的 1+3ell′−2M′=5ell−1+d_J，不能照抄 d_J−1/6。
两分支随 Delta_H 都不增；actual Delta_H>=−epsilon_Z。因此共同 Fourier Minkowski、
Gaussian k 求和与有限 sectors/实际 dyads 求和之后，得到

\[
 \boxed{\sum_{0<Nm\ll Q}|B_m^J|^2
   \ll Z^{M'+((5\ell-1+d_J)/4)_++\epsilon}.} \tag{4}
\]

powerful/supported fixed parts 的计数已经在 E_ref 中，不再额外乘一次行数。
empty surviving slots 时 z_a=0，除 bounded negative unit offsets 外直接属于第一分支，
可得更强的 M′+epsilon；(4) 的较弱统一界仍合法。
不再用旧数字“d_J=1/6”的 endpoint 论证。

## 5. additive Gram 与 tuple 亏损支付

全参数区间 1/6<=ell<=1/5 上有

\[
 M'\ge1-3\ell\ge2/5>0,\quad
 l_x-d_J\ge11/80>0,\quad
 l_y-d_J-11b/6\ge1/30>0.
\]

故 Q,Y′>=1 最终成立、同在固定 polynomial ranges；
P_a=Y′²/Q=q_{b_*}^{−1}Z^b>=1 最终成立，
且 P_a²/Y′<<P_a^{1/6}。
通用 `prop:probe-gram` 因而直接给

\[
 \sum_{Nm\ll Q}|A_m(Y')|^2
 \ll (1+|\nu|)^{J_{\rm Gr}}(Q/Y')P_a^{1/6}Z^{\epsilon}.
 \tag{5}
\]

有限 ray coefficients 与原 Mellin test 的 rapid decay 吸收 height seminorm，
没有赋予 A_m 任意行系数。
把 (4)(5) 在同一个 Q 球 Cauchy，含原 Q^{−1/2} 分离归一化，得到每个 fixed rescaled tuple 至多

\[
 (X')^{1/2}P_a^{1/12}
 Z^{(5\ell-1+d_J)_+/8+\epsilon}.
\]

rescaled tuple 数至多 Z^{d_J+epsilon}、原外系数 O(Z^{−3d_J/2})、
(X′)^{1/2}~X^{1/2}Z^{−d_J/2}。合计额外指数准确为

\[
 -d_J+(5\ell-1+d_J)_+/8\le-7d_J/8\le0,
 \tag{6}
\]

因为 5ell−1<=0。
正 row loss 并未删掉；它被同一源表达式的 tuple 亏损支付。
有限 subsets 和全部原 Mellin 分离合并即得 X^{1/2}Z^{b/12+epsilon}，即 (2)。

先固定 epsilon 与 arithmetic/slot/window data；然后选反射 retention、分离损失和 kappa_G
使其有限总和落在 epsilon 内；各 Fourier seminorm order、尾部 contour order 随后固定，最后提高 Z 阈值。
对数 dyad 数和 fixed annular offsets 只在最后进入任意小幂。
指数不依赖 moving tuples 或 target 的选取；常数可依赖已固定 arithmetic/slot/window data
及已固定 target，不依赖 moving tuples、当前行或素数标签。

## 6. 具体候选及尚未闭合的高侧

取 ell=10003/60000=1/6+1/20000，得

\[
 l_x=42497/120000,\quad l_y=57497/120000,\quad
 h=32503/40000,\quad
 |I_{\rm modified}|\ll Z^{14999/80000+\epsilon}.
\]

Cb(s)=s−11/16 仍不变；Cb(69999/80000)=14999/80000。
因此[439](439-prime-slot-geometry-and-a-conditional-strip-improvement.md)的 low 前件现在由上述确切通用引理支付。
实际 high counts、shared contour 在新边界的完整 statement、全误差统一性及 continuation 仍开放。
本稿没有把 nominal R_* 变成实际行数定理，也没有证明 sigma=69999/80000 的无零性。

完整前件读源报告：`reviews/2026-10-07/hybrid-variable-low-admission-derivation.md`。
独立逆审与有限指数检查另列，不把本项目纸面分析冒称外部 Lean 形式化。
