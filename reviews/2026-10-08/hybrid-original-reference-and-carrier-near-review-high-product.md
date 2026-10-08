# 连续参考项与原载体四阶近相关：不同作者综合审查

2026-10-08，high_product_joint。研究轮3，基线 main cd95587。
只新增本 peer，不改两份作者源、旧冻结文件、输出、检查器或 Git。
结论：下列两份源在各自明确范围内数学 PASS；未准入任何新 whole、
常数预算、零点比例或无零边界。

## 1. 最终冻结源与完整读取身份

本次逐行 FULL READ 两份最终源；canonical UTF-8 LF 只转换 CRLF/lone CR，
不 trim，也不改变文件末尾。

| 作者源 | 行数／LF bytes | SHA256 |
| --- | --- | --- |
| [连续主项与素数偏差](hybrid-original-product-cell-continuous-main-and-prime-deviation-research-checkpoint-audit.md) | 195／8957 | f55667a3d84405eb183e94a1a3e03ccda127bbe075e920744d0262dfcfea10e9 |
| [原载体四阶远近分解](hybrid-original-squarefree-carrier-fourth-near-research-perron.md) | 188／8655 | 2142645eed724da49a3e6faae7068adb2c8ca907c196a691f09a2b7a7fd6f3ae |

另 FULL READ [scalar 源370行](hybrid-short-carrier-canonical-scalar-fourth-admission-research-radial.md)，
SHA f04279a9de54303d772859b2ee5e05010567404c53143c928a14e905eb51a0d7。
此前已 FULL READ actual425、slice337、coherent191、固定零点包453、
note490全部；本次回核 actual(4)、(5)、(11)–(13)、slice的共同
\(J_q\) 与准确 mask。所用身份与两份源的输入表一致。

## 2. 连续 reference 的完整付款

按定义将仅两内腿的素数原子测度换成 \(dp/(N_L\sqrt p)\)；
外 \(q,s\) 仍是实际素数，所有 dyadic endpoints、\(p,r<q\)、
same-\(u\)、两最大标签位置、产品窗及准确 \(\Omega(q,n,S)\) 都保留。
这是同 actual mask 的模型替换，不是已证的 prime approximation。
pushforward 的 \(dr=dk/p\) 正确，所得 \(k\)-measure 连续；
不得将其采样成整数 \(C_k\)，或借 \(v=0\) 模型值恢复 \(q\mid pr\)。

独立重推：实际 \(\nu\) 的支撑使
\(\alpha=n/q^2\asymp X/(qs)\)、\(PR\asymp qs\)，故
\(\Lambda=2\pi\alpha PR\asymp X\)。
缩放后的积分区间均在 \([1,2]\)，sharp \(q\)-prefix 可任意变短。
由 scalar 的 \(C^2\) zero extension，
\(\|\phi'\|_\infty\le\|\phi''\|_1=O_\phi(1)\)。
actual 两套 profiles 的 \(p\)-腿、\(r\)-腿分别独立，因此
\(W,W_x,W_y,W_{xy}\) 一致有界；mixed 导数没有要求 \(\phi''\) 的 sup。

对 \(x\)、\(y\) 各分部积分一次，四角、两条 fixed-\(x\) 边、
两条 fixed-\(y\) 边与 bulk 都含 \(\Lambda^{-2}\)。
所有振幅分母仅为 \(x,y\ge1\)，不除以 clipped interval 长度。
因此严格有
\[
 |G_0|\ll_{\phi,g}\frac{\sqrt{PR}}{N_L^2X^2}.
\]
该步骤直接对恢复后的 profiles 证明，没有逐 Fourier 参数求导，
也没有偷用原 \(C^2\) profiles 的 weighted Fourier moments。

\(\nu\) 支撑长度 \(O(X)\)、sup \(O_\chi(X^{-1})\)，
实际 lattice 步长 \(2\pi s/q\le2\pi\)，含 \(+1\) 的整数计数给
\(\sum_n(2\pi s/q)\nu(2\pi sn/q)\ll_\chi1\)。
由 Chebyshev，
\(\sum_{s<q}b_qb_s\sqrt{qs}\ll X^2/N_L^2\)。
固定 \(q,s\) 的兼容 \(p,r\) dyadic pairs 为 \(O(L)\)，
原 \(L^{-1}\int_{I_+}\phi^2\le1/2\)；故
\[
 |K_0|\ll_{\phi,\chi,g}\frac{L}{N_L^4}\ll L^{-3}.
\]
这一正包络逐原 \(n\) 适用任意保留的实际 mask，覆盖 edge 与 fullperiod；
没有从另一 signed 总界截取子族。

cell 的 \(h=0\) 常 density 积分为零，但 \(h=1\) 准确等于
\[
 -\frac{qc_z}{2\pi i}\sum_{j\in I}\frac1j .
\]
非空真实完整周期满足 \(j\ge1\)，\(j\asymp X/S\) 的窗上 harmonic 和
一致有界。作者所作相对 \(O(1/S)\) 的 bulk 比较仅限零 twists、
overlap loglength有固定正下界且远离 product corners，此限制充分。
小的完整 \(K_0\) 不能反推每个 Taylor 阶的 cell 系数小；
上述 endpoint 要在整个 slow 相位、cells 与公共参数中共同恢复。
精确 \(K_{\rm pr}=K_0+K_{\rm dev}\) 保留全部 actual atoms 和 \(s\) 排除，
mixed 两项与 double-deviation 项均未获新界。

## 3. 原 \(\nu\) 下四阶远相关付款

490 的真实有限 \(R\) 系数保留正负、squarefree 条件、
\(p\mid n/p\) 与两端 \(Y<n\le X\)；
\(|r_n|\ll\tau(n)/\sqrt n\)、\(\sum|r_n|\ll\sqrt X L\)。
平方系数满足 \(\sum|g_\ell|\ll XL^2\)、
\(|g_\ell|\ll\tau_4(\ell)/\sqrt\ell\)，
\(\tau_4^2\le\tau_{16}\) 给对角 \(D_\nu\ll L^{16}\)。
这是 polylog 上界，不是中心常数的准确付款。

直接交换有限和与原正概率测度，准确时间核为
\[
 \Psi_T(u)=e^{iTu}\Gamma(s_Tu)d^{-1}\sum_{k<d}e^{ik\eta u}.
\]
原 floor、正 height 与几何核都保留，后者的模长至多1。
原 \(\Delta=1024L^{5/2}/X\) 满足
\(s_T\Delta=2048\pi L^2\)，所以
\(\sqrt{s_T\Delta}/16=\sqrt{8\pi}\,L\)。
全部 \(|\log(\ell/\ell')|\ge\Delta\) 的实际系数相关由正包络给
\[
 |F_\nu|\le X^{-\sqrt{8\pi}}\Big(\sum|g_\ell|\Big)^2
           \ll X^{2-\sqrt{8\pi}}L^4 .
\]
于是 \(M_{\nu,R}=D_\nu+C_{\nu,\rm near}+F_\nu\) 准确成立；
near 顶端仍容许 \(|\ell-\ell'|\ll XL^{5/2}\)，其一侧 signed 上界未付。

同453的固定有限零点包、重数与整个两端函数恢复出的四重积分核正确。
内部 \([6T/5,9T/5]\) 的完整离散 Riemann 和给 \(\nu\asymp T^{-1}\)。
固定 \(\beta-1/2\ge\eta_0>0\) 且 \(\gamma\in[5T/4,7T/4]\) 时，
两端单零点核满足 \(\int\nu|f_\rho|^4\asymp_{\eta_0}X^{4(\beta-1/2)}/T\)；
密度自项费用仍是 \(4\sigma-3+n(\sigma)\)，名义值仍为 \(5/7\)。
这是费用比较，不是假设零点或密度已饱和。

## 4. 消费范围

\(\nu\ll T^{-1}1_J\) 只允许 canonical \(J\) 的完整误差上界迁入 \(\nu\)。
在 \(B\ge c_\theta\) 下，真实 \(R-Z_T\) 的已付 \(L^4\) 差允许
\(M_{\nu,R}\) 与 \(M_{\nu,Z}\) 的上界双向运输；
此处名义 \(c_\theta=3/7\)、第四矩差 \(9/14\) 均为已有费用。
不能逆向从 \(M_{\nu,R}\) 推 canonical whole，也不能搬运某个 signed 子包。
两份新源的付款对象不同：连续 \(K_0\) 与原 \(\nu\)-\(R\) 的 far 和；
没有把 \(E_H\)、\(E_G\)、JSC 或全部 prime covariance 相互替换。
真实 \(K_{\rm dev}\)、近相关及最终 whole 消费合同仍待证明。
