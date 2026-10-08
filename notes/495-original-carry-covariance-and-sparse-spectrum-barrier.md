# 495. 素数目标进位协方差与稀疏谱的输入限制

2026-10-08。基线 main 84670bce2bf0d6109ff37fdee4862b27ea7d3641。
这是上次复盘后的第5轮，继续[494](494-original-double-deviation-and-upper-cauchy-core.md)。
保持原数域、真实素数函数与完整研究目标。

本轮把外素数权读取的乘积进位写成准确有限公式，并证明现有
条带、比例下界、密度及全包二阶信息在抽象谱类中仍允许当前四阶幂。
这明确了下一步须使用的算术信息，没有提高实际零点比例或无零边界。
没有新的完整四阶增长幂或实际中心常数，新纪录论文条件仍未满足。

| 结论及范围 | 完整来源 | 不同作者全文独审 |
| --- | --- | --- |
| 原实际 prime-target carry、mask 与角色边界；无新省幂 | [128行 carry 源](../reviews/2026-10-08/hybrid-original-prime-target-carry-and-character-contract-research-high-product.md) | [carry 独审](../reviews/2026-10-08/hybrid-original-prime-target-carry-and-character-contract-review-checkpoint-audit.md) |
| 同形状抽象全包的二阶小、四阶饱和；不是ζ反例 | [184行谱模型](../reviews/2026-10-08/hybrid-original-sparse-cauchy-spectrum-input-audit-research-root.md) | [谱模型独审](../reviews/2026-10-08/hybrid-original-sparse-cauchy-spectrum-input-audit-review-perron.md) |

## 1. 外素数权匹配商，乘法角色读取余数

保留191与494的准确对象，令 \(pr=qz+v\)、\(0\le z,v<q\)。
真实整数素数满足 \(v\ne0\)，所以 \(\chi(v)=\chi(p)\chi(r)\)；
外 \(F_q(a)=\sum_s c_s e_q(as)\) 则读取整数商z。
零ν-twist下，对共同完整j窗I，定义
\[
 D_I(v)=\sum_{j\in I}e_q(-jv),\quad
 B_{z,h,I}=\sum_{v<q}C_{q,qz+v}D_I(v)(v/q)^h,\quad
 \widehat\Omega_h(b)=q^{-1}\sum_{a\in\Omega_q}(a/q)^h e_q(-ab).
\]
完整慢相位Taylor和准确给
\[
 \sum_{a\in\Omega_q}F_q(a)\sum_{j\in I}G_q(a+qj)
 =q\sum_{h\ge0}\frac{(-2\pi i)^h}{h!}
                  \sum_{s,z}c_s\widehat\Omega_h(z-s)B_{z,h,I}.
\]
形式全q个residues的h=0项才是 \(q\sum_s c_s B_{s,0,I}\)；
它不是完整实际统计的值。实际minor mask还保留卷积与全部Taylor阶。
恢复原ν-twist后，\(\widehat\Omega_h\) 变为保留
\(((j+a/q)/X)^{it_\nu}\) 的逐j加权Fourier系数，两个端period也参与。
准确展开沿用191的工具，不重新认领为新增费用节省。

因此把外素数目标再作乘法角色变换，留下
\(\chi(pr\bmod q)\psi(\lfloor pr/q\rfloor)\)，
carry因子不能由通常Gauss／Jacobi公式分成两条prime角色腿。
494的 \(\Delta\mu=\mu_{\rm pr}-\mu_0\) 又含连续负measure；
Dirichlet角色的整数因子化不能直接用于真实连续p/r。
只有恢复后的完整带F signed层已知
\(K_{\Delta,\Delta}=K_{\rm pr}+O(\log^C X)\)，
未支付逐角色投影或centered正能量。

可消费的一级输入是同一公共正参数包络下的完整统计
\[
 {\cal T}(\lambda)=\sum_{q\sim Q}b_q\omega_q(\lambda){\cal J}_q(\lambda),
 \qquad \int W(\lambda)|{\cal T}(\lambda)|d\lambda
       \ll Q^2X^{-r}\log^C X.
\]
它若被证明，可给原box费用 \(QS X^{-1-r}\log^C X\)，
并保留已付的s排除修正；跨过5/7需 \(r>u+w-12/7\)。
这是充分输入门槛，尚未证明；只估零twist、h=0或完整period均不够。

## 2. 普通前缀误差直接消费仍不足

审查最有利的普通CDF输入
\[
 \sup_{p\in I_P}|E_s(p)|\ll P^{\theta-1/2+\epsilon}/N_L,\qquad
 E_s(p)=\Delta\mu_s((\inf I_P,p]).
\]
这是额外条件输入；正确剔除proper powers和s原子后才与原measure一致。
Stieltjes分部积分保留sharp端点、原profile variation和振荡导数。
对端点及不含n的profile variation部分，令共同n窗
\(N\asymp QX/S\)。把依赖s的 \(E_s(p)\) 留在fixed-p的F系数中，
逐q的F能量为 \(O(N\sup_s|E_s(p)|^2\log^C X)\)；
固定实数p时，整数r频率 \(pr/q^2\) 的圆间距至少 \(p/q^2\)，
Schur界给G能量 \((N+Q^2/P)\log^C X\)。
同样保持原profile及其导数作fixed-p的bounded系数，
不增加C²输入的Fourier加权矩。
恢复 \(S/(QX)\) 及 \(\sum_{q\sim Q}b_q\ll\sqrt Q\log^C X\)，
这一方法的费用为
\[
 \boxed{\sqrt Q\,P^{\theta-1/2}
                 \sqrt{1+\frac{QS}{PX}}\log^C X.}
\]
因 \(PR\asymp QS,\ R\lesssim Q\lesssim X\)，括号有界且 \(P\gtrsim S\)。
名义θ=7/8、\(Q=X^u,S=X^w,P=X^p\) 时，剩余产品域给
\[
 \frac u2+\frac{3p}8\ge\frac u2+\frac{3w}8
 \ge\frac7{16}(u+w)\ge\frac{8351}{11200}-o(1)>\frac57.
\]
最后的o(1)保留跨cutoff的dyadic常数。
振荡导数另有 \(nRP/q^2\asymp X\) 的variation，未由这项费用支付。
这只是普通CDF绝对消费的费用审查，不是实际K的下界，
也不是新的完整prime-deviation估计或所有方法的不可行性定理。

## 3. 二阶信息为何不能单独推出四阶改进

名义配置下，低包仍用整个两端entire核；β≤1/2部分不分开奇异单端。
局部计数和正加权Cauchy给二阶费用
\(T^{-1}\sum_\rho m_\rho X^{2\max(\beta-1/2,0)}\log^C X\)；
β≤1/2的总点数为 \(O(T\log T)\)，其费用仅为polylog。
余下固定实部网格的独立二阶正费用最多
\[
 \max_{\sigma\in[1/2,11/20]}(2\sigma-2+n(\sigma))=9/290.
\]
高包Y端二阶费用为
\((10/7)(\sigma-1/2)-1+n(\sigma)\)：
Ingham段最大 \(29/7-2\sqrt{30/7}<9/290\)，
Huxley段两端为−3/70、−1/7，Ivić段两端为−11/56、−1/4。
通过494的完整包身份及453的全Z二阶polylog，
L²三角给真实 \(M_2(C_X)\ll X^{9/290+\epsilon}\)。
但已有点界平方为 \(X^{3/4}\log^C X\)，直接插值只给
\(M_4(C_X)\ll X^{453/580+\epsilon}\)，仍大于5/7。
这只改善二阶辅助界。

谱模型另给更强的输入能力证明。固定 \(5/6<\theta\le7/8\)，
在原ν内部放置 \(K=\lfloor T^{n_I(\theta)}\rfloor\) 个等距简单高点，
添加反射、共轭，并取间距 \(2\pi/\log X\) 的临界线简单背景。
该有限谱族符合所用密度和局部计数，临界线比例趋1；
背景Fourier平方的周期性使完整两端Z的二阶为O(1)。
高点相隔 \(T/K\to\infty\)，其原上端相位的相消不足以压掉分离峰，
准确两端全包仍满足
\[
 T^{-1}\int_J|Z|^4\asymp T^{B_I(\theta)}/\log^4 X,
 \quad B_I(\theta)=4\theta-3+n_I(\theta).
\]
原ν四矩同阶；θ=7/8时为 \(T^{5/7}/\log^4X\)。
模型没有Euler乘积、真实有限素数系数、精确ζ计数或Perron修正，
并非真实ζ反例。它严格说明这组抽象上界不足以统一推出固定四阶省幂。

## 4. 下一方向与复盘

优先证明真实prime-target carry统计的联合相消，
或真实平方自由系数在覆盖核下的完整近相关一侧界。
零点方向只有引入能排除稀疏高峰的实际算术关系或更强实际密度才值得继续；
减少对普通前缀绝对界、一般Hilbert叠加及二阶日志的重复优化。
JSC仍是未付的一侧signed协方差合同，不能改称已付正能量。
八平移覆盖不扩大固定零点公式的J范围，完整目标继续保留。

已知比例比较值与451的条件边界保持；本轮未满足新论文发布条件。
复盘计数推进至5，默认下一轮即第6轮全面复盘，最迟第8轮。
