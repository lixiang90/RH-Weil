# 335 独立复核与异议处理

2026-09-07。Franklin只读内部模型复核，未派生代理。以下是主线程按收到报告
整理的范围、发现和处理摘要，不称外部同行评审。
审查原件SHA256：58edbcb63a87249a8fab0883375e66b95540ea598b494ab5c8856c1482ed99e1。

核读335全文，以及mobius_divisor_pullback_audit.py的记录生成、中心响应与pullback；
power_high_prime_measure_audit.py的flat_overlap_weight；
ordinary_seam_kernel_audit.py的flat_support/periodic_shifted_overlap；
power_high_bandpass_audit.py的finite_kernel；240的共同中心与ghost恒等式、
241的物理纤维合并原则。未复审这些旧稿全文，未审外部Kloosterman来源或336–337。

## 结论及处理

1. 三窗先交集再周期化，区间长度L-log max(a,b)在(0,L)；
   位移P_cd(u-Delta)与脚本right+shift+winding*L相同。
   当前shell只需绕周期-1,0,1。W对换对称。
   M=X^.5取自Möbius实验，没有混入另一个实验的X^.25。
2. 中心平均、载频、四Lambda权及有序两倍均正确。
   响应是规范化direct_response，ordinary完整cross_main_term另有beta^4 D。
   **发现finite_kernel的小分母返回1分支错误**：
   X=10^14,t=.5应约-2.97e-16而原实现返回1。
   已改为sinc比值，频率增量模1规约保留全部有限和；
   回归脚本及输出见finite_kernel_stability_audit.py及同目录对应JSON。
   此反例是连续核取值，未构造对应素数四元组。
3. 原文“去掉的不仅是原子对角”在当前cell表述过强。
   当前两个异底素数幂对均互素，ad=bc等价a=c,b=d；
   固定ghost扩展在端点比<2及原mask下也无额外比例别名。
   已改为统一按h=0删除，在当前域等价原子对角；改变整数域需重新检查。
4. gcd参数化包括b'=1、负h、负c0及大gcd层，成立。
   g|h仅保证整数方程可解，不保证cell/mask/素数幂条件可同时满足；
   bc仍随t变化，不能冻结对数相位。
   全shell的h=O(X)与主振荡h=O(X^.5)区分正确。
5. 固定分母纤维O(g+1)成立。当前互素分母可强化至多1点。
   同底分母只能b=d，但非零h=b(a-c)仍可能发生，不能删掉这层。
   单独参数化未产生两条平方根长自由变量，不排除进一步变换。

## 复核者报告的有限实验范围

X=400，I=[63,116]：14个素数幂、182条原始记录、742条ghost扩展记录；
3150个有序有效四元组与gcd参数集合一致。
28466个无序扩展候选的响应与原始有序和差5.27e-17，
有效项上的六窗逐项相同。|h|<=694内检查109090个参数化整数解，
互素纤维最多1点、大gcd最多53点。
另核对五个核值和中心平均。此处数字来自复核者终端报告；
主线程另保存本次独立实现的核回归日志，不冒称重复运行了全部cell实验。

数学定义及整数纤维结论通过复核；上述两项修订不产生新的相关和界、
全cell覆盖或RH结论。
