# 中心化增长比较的经典输入与使用范围

2026-10-11。服务于[521](../../notes/521-f1-moving-source-correction-and-uniform-resolvent.md)、
[522](../../notes/522-f1-optimal-centered-growth-and-rh-equivalence.md)、
[523](../../notes/523-f1-natural-hilbert-collapse-and-growth-gap.md)。

本轮在线核读NIST DLMF的[25.2.8](https://dlmf.nist.gov/25.2#E8)、
[25.2.11](https://dlmf.nist.gov/25.2#E11)与
[25.4.3](https://dlmf.nist.gov/25.4#E3)。前两条分别提供右半平面的
Euler–Maclaurin表示和Re s>1的Euler积；后一条提供ξ(s)=ξ(1−s)的对称。
没有归档整站，也没有声称核读其全部推导。

521取25.2.8的N=1，再乘s−1，得到整函数
Z(s)=s−s(s−1)∫₁∞{x}x^(−s−1)dx。
积分绝对值至多1/Re s，故固定正实部条带上Z有二次多项式上界，包含s=1。
Euler逆的绝对收敛在固定σ*>1给非零锚点下界。
有限圆盘Poisson核的比值3在521直接支付Harnack链，没有引用零距下界。
反射对称只用于把零点右边缘写成1/2+β；β没有被独立算出或缩小。

522直接从实际平移群构造每个Banach完成，支付初始Laplace积分、
Gaussian近似单位反演和二阶正则化移线；没有借抽象谱界猜测增长界。
移线上的原商预解不被冒称为整个Banach生成元的预解。
523的单线密度用Plancherel、Cauchy–Schwarz及L¹ Fourier唯一性直接证明。

前序Meyer源像及谱机制的阅读范围仍见
[既有原件核读](2026-10-11-meyer-radial-source-and-spectrum-audit.md)。
其后续核迹与可和性证明未在本轮新增审计。没有新PDF、文献清点变化或世界优先权声明。
新结果是本仓库实际接口中的解析比较与指定完成障碍；
不提供独立算术次指数界、RH、简单性、全局Weil负性、principal或全局HH链。
