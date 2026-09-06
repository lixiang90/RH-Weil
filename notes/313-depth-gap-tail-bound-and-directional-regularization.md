# 313. 深度分离的非实正背景尾界与方向性正则化

2026-09-06。VIS-REG第4轮候选；完整自含推导如下，独立复核待完成。
状态：[T，内部候选] 在明确几何条件下的完整算子估计；[C/O] 实际零点满足分离条件的验证。
不假设RH，不断言实际存在离线零点，不声称已经获得零点比例改进或文献优先权。
与310–312的纯线代重写不同，本轮把全部非实正项的一个具体尾区间显式估计掉；
是否达到phase2实质成果门槛，须在证明复核及原始文献比较后另行结算。

## 1. 有限任务与完整配置

仍用实际0<γ≤T全部零点、含重数、同一sharp MT窗及原始高度e^(−izu)。
设L=log T、A=L/2、b=1/sqrt2，所有非实对取上半平面的z=x+id，0<d<1/2。
无条件单位高度含重数计数≤C0 L是唯一外部算术输入。

固定参数
\[
 0<d_0<1/2,\quad 0<\delta<d_0,\quad0<\varepsilon<d_0,
 \qquad s=d_0-\delta,\quad D=T^{1/2-d_0+\varepsilon}.
 \tag{1}
\]
选择任意一个实际目标zT=xT+idT，dT≥d0，单点重数mT≥1。
**额外的几何条件**为：所有其他非实对w=y+ie若e>s，则
\[
 |y-x_T|\ge D. \tag{2}
\]
同一个共轭对只索引一次，自身全部重数不拆成“其他”点。
允许任意多个浅非实对、全部临界线点及所有远处深非实对。
单位高度计数或总体零密度上界本身不保证(2)。

目标是用(2)具体估计312-(7)的αT、βT，保持全部正项。
本任务不要求硬商残余Gram下框架，不先求原负谱。

## 2. 任意有界深度子背景的范数界

先把某一非实对子集的全部实部高度作为实频率，列权仍为sqrt(2m)。
312的Bessel证明只使用实频率局部含重数计数，不要求这些高度本身是临界线零点，
所以相应纯实指数合成算子B0满足 ||B0||≤sqrt(C L)。
即使多个不同非实对有相同高度，计数包含全部权重，结论不变。

对子集内0<ej≤e0，展开cosh(eju)：
\[
 B_G=\sum_{n\ge0}{D_u^{2n}B_0D_e^{2n}\over(2n)!},
 \qquad \|B_G\|\le\sqrt{CL}\cosh(e_0A).
\]
其中Du为乘u、De为列系数乘ej，||Du||≤A、||De||≤e0。
级数在有限层的算子范数中绝对收敛。因此
\[
 \boxed{\|P_{G,e\le e_0}\|\le CL\cosh^2(e_0A)\le CLT^{e_0}.} \tag{3}
\]
同样适用于删去目标或选取远处子集；C只依赖局部计数常数和固定窗。
特别地全部非实正项有 ||PG||≤CLT^(1/2)。这不是原算子A_T的正谱部分。

## 3. MT核的远高度估计

令KA(ζ)=∫ηA²(u)e^(−iζu)du，则直接积分给
\[
 K_A(\zeta)={\sinc(A\zeta-b)+\sinc(A\zeta+b)\over2\sinc b}.
\]
当A≥1、|v|≥1、q∈R时，由|sin(a+ic)|≤e^|c|及
|A(v+iq)±b|≥(1−b)A|v|得到
\[
 |K_A(v+iq)|\le C_b{e^{A|q|}\over A|v|}. \tag{4}
\]
将sinh(dTu)cosh(eu)展开为四个指数，并用312-(5)，有
\[
 |\langle h_{z_T},g_w\rangle|
 \le C_b{e^{A(d_T+e)}\over A|y-x_T|}. \tag{5}
\]
记H=||hzT||²。目标深度dT∈[d0,1/2)时，端点比较一致给
H≥c(d0)T^dT/A（T充分大）；故
\[
 { |\langle h_{z_T},g_w\rangle|^2\over H}
 \le C(d_0){T^e\over A|y-x_T|^2}. \tag{6}
\]

令Pf为其他深非实正项（e>s），它们依(2)全部远离目标。
单位高度计数与Σ_{n≥D−1}n^−2≪1/D给
\[
 \alpha_f={\langle P_fh,h\rangle\over H}
 \le C(d_0){T^{1/2}\over A}\sum_{|y-x_T|\ge D}{m_w\over|y-x_T|^2}
 \le C(d_0){T^{1/2}\over D}. \tag{7}
\]
此处的2倍列权并入常数；没有把深度筛选子和当作全谱带符号和。
因Pf≥0，Pf²≤||Pf||Pf，再用(3)和(7)，
\[
 \beta_f={\|P_fh\|\over\sqrt H}
 \le C(d_0)\sqrt{TL/D}. \tag{8}
\]
这里只用正背景的合法上界；原A的其他负项仍保持在完整算子中。

## 4. 合并浅、深背景并选定日程

浅非实正项Ps由(3)给 ||Ps||≤CLT^s，故αs、βs均≤CLT^s。
Po=Ps+Pf是除自身g以外全部非实正项，综上
\[
 \alpha_T\le CLT^s+C(d_0)T^{1/2}/D,\qquad
 \beta_T\le CLT^s+C(d_0)\sqrt{TL/D}. \tag{9}
\]
和目标H≥c(d0)T^d0/L比较，
\[
 {CL+\alpha_T\over H}
 \ll_{d_0} L^2T^{-\delta}+LT^{-\varepsilon}+L^2T^{-d_0}=o(1). \tag{10}
\]
定义独立于待证明负谱的明确日程
\[
 \kappa=\max\{d_0-\delta,\ 1/4+d_0/2-\varepsilon/2\}<1/2,
 \qquad \lambda_T=L^2T^\kappa. \tag{11}
\]
则(CL+βT)/λT=O(1/L)（固定参数），所以312-(7)给
\[
 \boxed{\operatorname{tr}(R_{T,\lambda_T}A_TR_{T,\lambda_T})_-
       \ge(1-o(1))\,2m_TH.} \tag{12}
\]
o(1)统一于满足(1)–(2)的目标位置、目标深度dT≥d0及重数mT≥1；
常数可以依赖固定d0、δ、ε和实际计数常数。
证明对含全部实际正负列的算子成立，不只对选出的负秩一项成立。
这里只捕获目标负列的质量尺度，不声称捕获原A的全部负迹比例；多个目标不能不经正交／集体Gram审计就相加。

## 5. 一个全局逆范数证书严格过粗的参数范围

取d0=2/5、δ=1/20、ε=1/5，则s=κ=7/20、D=T^(3/10)，
λ=L²T^(7/20)。近高度只要求其他非实点深度≤7/20，远处保留其余全部点。
若这样的目标配置存在，自身正列已给
\[
 \|P\|\ge2m_T\|g_{z_T}\|^2\gtrsim T^{2/5}/L.
\]
于是用于通用反向负迹转移的乘数满足
\[
 (1+\|P\|/\lambda)^2\gtrsim T^{1/10}/L^6\longrightarrow\infty,
\]
而同一目标测试方向的逆变换范数比由(9)–(11)趋于1，(12)仍成立。
这定位了此前全局条件数比较漏掉的参数范围，非仅把λ放大到||P||。
它是有几何前提的结论；没有证明实际零点在无穷多个高度满足这组前提。

## 6. 适用边界与待审项目

- 唯一外部算术输入是实际单位高度含重数计数，原始出处见Bellotti–Wong v2；Bessel及核估计已在本文自证。
- Rayleigh、合同变换、cosh范数级数属于经典工具；310的Birman–Schwinger改写不作为新颖性证据。
- 197的抽象上下框架判据仍是相关先行内部机制。本篇新增候选内容是(7)–(12)的具体深度／高度尾界和日程，不是再次陈述抽象分离假设。
- 尚需独立逆审所有指数、重数、筛选与一致性，核查是否存在完全对应的原始文献；没有搜索到相同表述不能证明优先权。
- 后续最小实际问题是(2)或其块版本能否独立验证；一般零密度上界不能排除所有深点成簇，不能直接宣布存在这样的目标。

本轮保持VIS-REG探索；313的候选结论尚未用于本阶段验收。

## 7. 本轮原始文献比较记录

| 原始文献与核读位置 | 支持的内容 | 与本篇待审内容的边界 |
|---|---|---|
| [Bellotti–Wong v2](../literature/background/bellotti-wong-zero-counting-v2.pdf)，Theorem1.1 | 实际零点含重数计数的显式误差；本篇只取单位高度O(log T) | 未由该误差推出(2)；全文数值证书未由本项目复跑 |
| [Lamzouri v1](../literature/baseline/2026-lamzouri-6725-hilbert-v1.pdf)，§2及Lemma3.2的证明 | 有限自伴零点接口；sharp MT原始密度；平滑后的二阶全谱估计 | 本篇只借用原始密度及接口。没有把未平滑窗代入其平滑渐近式，也不把其二阶比例定理改称(12) |
| [Douglas1966](../literature/background/douglas-factorization-1966.pdf)，Theorem1及不同定义域推广 | 范围包含、正算子支配与有界因子等价 | 属于311的系数约束背景；本篇不假定存在收缩因子 |
| [Birman1961](../literature/background/birman-singular-spectrum-1961.pdf)，§1.5 Lemma1.1 | 负谱的阈值计数背景（独立审查者核读相关原文） | 本篇(12)用单方向Rayleigh下界；未将阈值计数当作负迹深度 |
| [Tikhonov1963](../literature/background/tikhonov-regularization-1963.pdf)，p.502式(2) | 残差平方与正则化惩罚的共同目标 | 正则化机制是经典；本篇待审的具体内容是深度／高度尾区间的预算 |

2026-09-06另检索了Riemann zeros＋regularization＋positive operator、
nonreal zeros＋Bessel，以及spectral regularization＋negative eigenvalues＋congruence。
结果多为不同的谱zeta正则化／Hamiltonian模型，未作为本篇证明输入或新颖性证据。
本表是有限范围的原始依赖比较，**不构成排除所有先行结果的检索**。
目前只可称内部新增候选估计；是否有完全对应的已发表组合仍[O]。
