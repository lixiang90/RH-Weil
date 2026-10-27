# c2后的唯一下一动作：一次同对象trial预算准入

2026-10-27；不是full-G执行或新数学合同。只使用已存真实n=||v||²、c2=<v,U_log2v>、原F8谱界及原固定v，量化本次数据对q0验收到底能付多少。不计算其他ratio，不重算c2／scalar，不调源／F／L或自动扩Krylov。

输入为旧lowband-step-certificate.json的n区间、新fixed-c2-certificate.json的真实c2区间、旧variational-cost-certificate.json的prime sqrt／d/u包围。保physical H和v=P B h0∈RanP；全部预算在此实际对象上，不换compressed matrix norm。

定义W2=(3/2)I−(U_log2+U_-log2)/sqrt2，Wrest为其余**七个**prime因子之积，W=W2 Wrest。它们是同一unitary dilation表示中相交换的正算子。exact有

\[
 a_2=\langle v,W_2v\rangle=\tfrac32 n-\sqrt2\,c_2,
 \qquad d_{rest}a_2\le a:=\langle v,Gv\rangle\le u_{rest}a_2.
\]

只允许用原有理sqrt prime包围向外求七因子drest/urest和a2。必须先扣更强的旧source后果：n=<v,Bh0>=<B*v,h0>，||h0||=1且B normal，所以a=||B*v||²≥n²；它比仅dn≤a强得多。实际取a_lo=max(n_lo²,d_lo*n_lo,drest_lo*a2_lo)，a_hi=min(u_hi*n_hi,urest_hi*a2_hi)。不能只改弱p2 lower而称新whole残差改善。新的upper可能改善fixed J/q0 lower，应与残差瓶颈分开报告。

由0<G≤u_hi给b=||Gv||²≤u_hi a。对于同一z=t v，真实残差满足

\[
 \|v-Gz\|^2=n-2ta+t^2b
 \le n+(u_{hi}t^2-2t)a.
\]

冻结t=1/u_hi，向外上界为r²_hi=n_hi−a_lo/u_hi，J=2tn−t²a另用完整n/a区间付费。该t在0≤t≤2/u_hi上最小化上述相关包络：系数≤0，用a_lo，而u_hi t²−2t于1/u_hi取−1/u_hi。这个最优性只属于**本有向充分包络**；不是实际残差下界，不排更好真实a/b/trial。不要把a,b拆成互不相关rectangle而丢掉已付b≤u a。

同一次比较还须核n_lo−a_hi/u_hi：即使免费知道actual a，仍仅使用b≤u_hi*a时，最优的此相关包络为n−a/u_hi；若上述有理下端仍大于d_lo/32，则本固定scalar包络没有足够信息，真正所缺是更紧的同向b/a数据。这是包络的诊断，不是actual residual的下界，也不排其他trial／实际b计算。

唯一门：实际运行有理脚本，输出drest/urest/a2/a/J/残差包络和原q0 variational区间，比较r²_hi≤d_lo/32及总宽≤1/16（包含J算术费），保存one-trial-budget.json和说明。只做这一次预算比较，不把粗数值说成实际Gv已算。若不够，停止此输入／包络的自动续算，不调t、继续prime或重展示收敛式；下一必须有新的同源global mixed/远尾费用或独立算术source实物。若够，也只是这一明确trial的费用准入，仍需按原验收范围核实际可表示trial、J及全H误差，不领取RH。

它为何值得一次：c2是新实际输入，a2可立即消费，以上全由已付有理记录给出，无unknown action假设；结果能决定是否允许该数据直接进入full-G trial验收。全6561 ratio未覆盖、N32小cutoff包络不能直接延NF的成本审查仍保留。此标准数值／准入比较不新开C047/584，也不把fixedq0弱界改善当classic全源／成长signed、primitiveRR或whole4/5UPPER的新净后果。
