# Möbius质量、源Taylor和双权近频率的经典输入核对

2026-10-12。服务于[524](../../notes/524-f1-mobius-cutoff-taylor-obstruction-and-repair.md)、
[525](../../notes/525-f1-smoothed-mobius-probes-and-arithmetic-strength.md)和
[526](../../notes/526-f1-faithful-two-weight-hilbert-quotient-and-defect.md)。
这是限定公式与经典定理的使用审计，不重证引用的经典计数或部分和定理，
不声明这些RH等价判据是首次发现。本轮没有新PDF归档、manifest或旧文献清点变化。

## 实际Möbius系数与原点质量

实际在线核读[NIST DLMF 27.4.5](https://dlmf.nist.gov/27.4#E5)：
Möbius Dirichlet级数等于1/ζ的绝对收敛范围为Re s>1。
525的原积分换序只在此范围进行。原点零质量由s→1+的支配收敛取得，
没有在s=1非法交换可能发散的绝对双和。

实际在线核读[DLMF 27.11.12](https://dlmf.nist.gov/27.11#E12)：
Mertens部分和有无条件界 \(O(xe^{-c\sqrt{\log x}})\)，某个c>0。
这里只消费这个经典界，没有将它声称为当前最优估计。
525独立作Stieltjes分部积分、三段切分和固定输入半范数比较，
得到一般原始源T在原点可积及截断质量损失界。
原点Schwartz准入、E后的完整目标误差和RH强度的临界抵消没有由该界付清。

## 平凡零点与真实源Taylor值

实际在线核读[DLMF 25.4.2](https://dlmf.nist.gov/25.4#E2)的ζ函数方程。
在负偶整数展开，得
\[
 \zeta'(-2k)=\frac{(-1)^k(2k)!\zeta(2k+1)}{2(2\pi)^{2k}}\ne0.
\]
524另外调用本仓库519已经证明的实际源接口
\(M_{E\theta}(-2k)=2\zeta'(-2k)\theta^{(2k)}(0)/(2k)!\)。
这条源接口并非从DLMF照搬；它在原E及其因子2下由源Mellin留数证明。
实际h0的二阶系数−3π/2遂给 \(M_{h_0}(-2)=3\zeta(3)/(4\pi)\)。
P3的积分连续成本6/5给严格下界5ζ(3)/(8π)及负时间指数5/2。
该下界只针对flat修正源，不依赖假想的离线零点。

## 固定探针取消条件与既有RH卷积判据

Luis Báez-Duarte，*Möbius-convolutions and the Riemann hypothesis*，
[arXiv math/0504402v1原文](https://arxiv.org/pdf/math/0504402v1)，10页。
核读PDF第3页的Mertens／加权和记号及第6–7页Theorem3.1、4.1的条件与证明接口。
其Mellin卷积使用加权部分和 \(\sum_{n\le x}\mu(n)/n\)。
固定探针需要保留Mellin取消或非消失条件，端点还关联简单性。
525未把此卷积算子当作本项目的原始T；本项目全族与目标Gaussian判据在指定空间独立推导。
该文是已有方法与范围的对照，不是525临界抵消的独立无条件输入。
也不从固定探针的有限采样证明全尺度增长。

## 双权交Gram的Beta因子

实际在线核读[DLMF 5.12.3](https://dlmf.nist.gov/5.12#E3)及
[DLMF 5.5.3](https://dlmf.nist.gov/5.5#E3)。
526以x=e^{4δt}换元，参数 \(u=1/2+q/(4\delta)\) 满足0<Re u<1，
因此Euler Beta积分及Gamma反射公式合法地给π/(4δ)乘sec因子。
连续Mellin jets、源Hilbert闭包、原商单射、伴随和二向量下界均在526另外证明。
Beta公式本身不提供Weil正性，也不证明商群酉。

## 实际中心线近频率：引用经典简单零点输入

J. B. Conrey，*More than two fifths of the zeros of the Riemann zeta function are on the critical line*，
J. reine angew. Math. 399 (1989), 1–26，
[作者原论文PDF](https://aimath.org/~kaur/publications/24.pdf)。
本轮重新核读PDF第1、3、4页：第3页的计数明确限于临界线且ζ'不为0，
第4页Theorem1给该计数的正比例；同时核对第3页通常含重数的零点计数。
只采用“至少cTlogT个不同中心线零点”这一经典结果，与516的输入一致。
不消费本项目近期比例证书，不查询当前比例最优值，不重新证明Conrey全文。

526另外用排序和平均间距给真实不同中心线高度差Δ→0，
再在指定自然商中严格算出近频率Gram成本与无统一有界性。
近频率输入无条件，结论只排除指定固定有限正实指数权商的等价酉化；
不排除非等价或具有独立算术正型的其他Hilbert实现。
完整Weil符号、几何principal及全局HH仍开放。

本轮内部全文审查、有限诊断及执行范围集中在
[验证收据](../../reviews/2026-10-12/f1-mobius-taylor-two-weight-round-verification.json)。
浮点检查没有区间认证，引用的无限计数和部分和定理不由脚本重证。
