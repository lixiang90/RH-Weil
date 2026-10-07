# 470 中心化谱方差与整个parity gap：全文独审

2026-10-08。审查者 radial_review。结论：**限定 PASS**。
完整逐节读取最终470，独立逆核有限covariance、行SOS、消元、
liminf子列、移动clip正尾成本及全部显示有理数。
没有修改主稿、旧来源、旧审查、math、Git或输出。

## 1. 最终对象与字节绑定

canonical为UTF-8，仅把CRLF及lone CR转LF，不trim，不删除EOF。

| 实读输入 | canonical LF SHA-256 |
| --- | --- |
| [470最终全文](../../notes/470-centered-spectral-variance-excludes-small-high-residual.md) | 729ddbed2b2d2af08e21e5f1ebabfb5663f906c702f52b13f81aac224402a93a |
| [454原weighted second](../../notes/454-original-background-and-weighted-prime-mixed-traces.md) | 8ab99d60c1b748dc561cac57ee498057a0c9fb19b9778a041261b1bad0750db7 |
| [465实际centered residual](../../notes/465-centered-high-square-joint-fourth-budget.md) | a9290d2d847c2a3f7942b26353bd1582a68b391e481acc109c4ac18d3d750464 |
| [466有限谱基SOS](../../notes/466-high-square-variance-commutator-obstruction.md) | 0b955bdc26b4bf950ce457dec7bf18f635f702d85a73d73c8d6263df969cbbbe |
| [完整正尾源](hybrid-positive-tail-whole-high-parity-gap-research-compression.md) | 568f2c80d9773db7c13bc3605e7d56ed032e3fba7f5d4dc7c34bbea5ac7cb611 |

470最终为8073 bytes / 213行。此前来源的相关定义和完整finite证明已实读，
本次对其用于470的前件与代数另行核查。
本报告不认证外部[R]或完整AF零侧链，也不认证未知高素数上界。
470新增必要下界本身不需[R]。

## 2. 同一实际对象及中心化的已付范围

原flat profile、fixed endpoint taper、全部genuine high primes、
carrier E、所有内部P和normalizer均保持。
470(2)的 \(M\to3/8,K\to41/10080\) 与
\(\mu=\tau(H^2-W)\to0,\varepsilon=\tau((H^2-W)W)\to0\)
确实来自此前unweighted/weighted second，不要求high4有界。
\(\tau W=2\int_0^{1/2}t(t+1)/2\,dt=1/6\)，
\(\tau W^2\to19/480\)，故 \(v\to17/1440\) 正确。
这些o(1)是实际已付trace误差，并非任意moving weight的假设。

H谱基的x、y不同于U-parity的q_even、q_odd，主稿明确区分。
H重复谱不构成障碍：任何正交特征基均满足下列准确式。

## 3. 有限covariance和SOS的独立核对

H谱基中 \(\Gamma_{ii}=\delta_i,\Gamma_{ij}=-W_{ij}\)。
因此
\[
 \tau\Gamma W=\frac1d\sum_i\delta_iw_i-y,\qquad
 \frac1d\sum_i(w_i-m)^2=\tau W^2-m^2-y=v-y.
\]
第二式保留了W的全部off-diagonal variance；
这是比此前粗界 \(y^2\le xv\) 更强的实际信息。
准确centered covariance为 \(y+\varepsilon-\mu m\)，
δ与w的diagonal variance分别是 \(x-\mu^2,v-y\)。
普通scalar Cauchy即470(4)，两个因子非负，
所有finite误差均保留，未对未知增长乘o(1)。

由W²≤MW，\(\rho_i\le w_i(M-w_i)\)。
Young的 \(\delta_i\rho_i\le M\delta_i^2/4+\rho_i^2/M\)，
与 \(w_i\rho_i+\rho_i^2/M\le M\rho_i\)，
代入 \(K\le4d^{-1}\sum\lambda_i^2\rho_i\) 给
\(K\le Mx+4My\)。这里1/4的不同成本没有丢掉。
未声称通用常数4M变小，也未假设Γ为PSD。

## 4. Whole q下界、消元与严格排除

若liminf q无穷，下界显然；否则先取达到finite liminf的有界子列，
再取x、y共同极限。只有这里x≤q有界，才从准确(4)删去中心化误差。
这一量词不需预先证明整个q有界，正确。

极限域为 \(y^2\le x(v-y),A\le x+4y\)，
\(A=41/3780,v=17/1440\)。
置q=x+y，展开并消去y²，准确得到
\(y(q+v)\le qv\)；
继而 \(A\le q+3qv/(q+v)\)，即
\[
 P(q)=q^2+(4v-A)q-Av\ge0.
\]
Av>0，两个根异号；q≥0必须在正根以上，没有最小化方向错误。
正根与主稿闭式完全一致：
\[
 q_*=\frac{\sqrt{104899}-275}{15120}
     =0.003232880359890941970204919231\ldots .
\]

内存Fraction/Sympy独立复算得到
\[
 P(1/350)=-15199/952560000,\qquad
 A-\left[Q+\frac{3Qv}{Q+v}\right]=15199/13967100.
\]
scaled discriminant为104899，正根代回P准确为0。
这是严格有理排除，未依赖浮点root search。
因此旧flat原矩阵Q=1/350前件确实不可能，
附加k条件也无法修复；此前条件公式继续有效但只能作反事实蕴含。
466的通用sharp例中ε=-y不为0，不能反驳新的实际中心化约束。

## 5. 同一下界传到whole U-parity gap，无增长前件

正尾源完整finite式为
\[
 g_T=q_T-2r_T\ge q_{R,T}
      +2(R^2-M_T)t_{R,T}-\zeta_{R,T}.
\]
取 \(R_T^2=\ell\)，其中
\(e_R\le R\alpha_T+\omega_T\)，
\(\alpha_T=O(\ell^{-1}),\omega_T=O(\sqrt{\log(2d)/d})\)。
因此 \(\zeta=2e_R^2+R^2\alpha_T^2=o(1)\) 逐项显式成立；
没有把fixed-R的o_R免费用于移动R。

q_R、t_R非负。若liminf g有限，沿达到该liminf的有界子列，
正成本自动使q_R=O(1)、t_R=O(1/ell)。
这是真实coercivity，未假设q或high4 bounded。
\(\|H-H_R\|_{2,d}^2\le t_R\) 给K_R→K；
core准确中心化为
\(\tau\Gamma_R=\mu-t_R\to0\)，
\(\tau\Gamma_RW=\varepsilon-\tau D_RW\to0\)，
后者由PSD及W≤MI给绝对界M t_R。
W的mean、variance不变。

严格有限covariance/SOS因此可对H_R、W使用。
bounded core子列的共同x_R、y_R极限满足同一必要域，
得liminf q_R≥q_*，再以g≥q_R−ζ推出470(11)。
无穷liminf情形显然。whole q下界也由q≥g恢复，
而第3节不用U的证明仍独立有效。

## 6. 最终限定范围

实际新增付款是更强的whole necessary lower bound，
并严格排除旧Q候选；不是新可支付的upper目标或新比例。
所有显示常数仅限原flat profile。
源仍准确保留原P、prime range、端点taper和四矩尾。
没有新的[R]输入、高第四矩增长前件、零点比例或无零边界。
主稿对冻结历史条件公式及后续算术任务的处理正确，
最终全文未发现数学阻断。
