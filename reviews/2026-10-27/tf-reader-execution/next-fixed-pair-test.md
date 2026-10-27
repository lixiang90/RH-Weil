# 显式向量后的唯一准入：一次固定c2配对

2026-10-27；这是一项建设性设施测试，不是新数学合同或已经算得的G action。输入锁定[lowband-vector-input.json](lowband-vector-input.json)的同一f、ell*、v*=f−Hcut F ell*及δv。h0=1_[1,2]、F8和原目标不变。

只求c2=<v,U_log2 v>，认证有理区间总宽≤1/1024，记录实际成本、整个H的误差，输出到同目录fixed-c2-certificate.json及fixed-c2-execution.md。禁止仅输出float、finite-grid residual或再次scalar Pnorm。尚未执行，不能预填pass。

令a=Fell*，U=U_log2。所有函数为本次实输入，用线性在第一腿的实内积。因为UHcut=1_(2,infinity)U，酉F交换U为U^-1，准确有

\[
\begin{split}
 \langle v_*,Uv_*\rangle={}&\langle f,Uf\rangle
 -\langle\ell_*,F Hcut U^{-1}f\rangle
 -\langle\ell_*,F Hcut U f\rangle\\
 &+\langle\ell_*,U^{-1}\ell_*\rangle
 -\int_0^2 a(x)\,2^{-1/2}a(x/2)\,dx .
\end{split}
\]

第一项是finite rational steps加sqrt2区间；中两项只在y∈(0,1)，clipped dilated f仍finite steps；第四项实际支撑(0,1/2)；末项只在x∈(0,2)。无限物理尾没有被丢弃，已用Plancherel／cutoff恒等式运输。若改用另一exact组织，必须证明同值并支付同一对象误差。

finite-domain integrals也需真实quadrature或exact moment余项；它们的定义并不等于reader已实现。g的高频系数会消去，p*的单项系数可能大，必须支付conditioning／rounding。Fell*在有限x上可用低support矩和真实Taylor余项，或其他严格方法；具体选择以实际成本为准，不能只给收敛存在式。

输入运输只需

\[
 |c_2(v)-c_2(v_*)|\le\delta_v(2\sqrt{\|v\|^2_{hi}}+\delta_v),
\]

其现有证书可付约8.3·10^−17；这不替finitepair算术误差。总区间必须包含两类误差。

**停止**：该冻结测试一次，不因失败改t／素数／精度序列来无限续同门。可以修正具体实现bug，须保旧失败证据。若无信息的真界或有向实现成本不支持，保存exact缺项并停止analytic表示的自动扩展。若pass，也只说明这一个mixed pair实际可读；a=<v,Gv>、b=||Gv||²、Gv／J／true-G residual及q0宽1/16和五源表仍欠。必须重新按input/test/net准入，不自动续全部primes或Krylov。

为何现在测：scalar norm已执行不可重计，现有新vector有确切有限系数和全H误差；本项可检验它是否真正支持有限mixed求值，改变实现组织选择。它不会消除主Goal的经典primitiveRR／成长signed及coverage-coupling瓶颈；如有独立实际算术或危险core新输入，优先比较改策。
