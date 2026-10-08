# 原次弧的平方模角色展开：准确逆元相位与系数耦合

2026-10-08，root。基线 main 3afd19318bf9c6fd6b3a1472929d13b4484698d3。
本稿只新增此源，不修改旧冻结解析输入。

本轮尝试把真实次弧转为可用的逆元三线性和。
得到完整有限角色变换，包含全部 primitive conductor q² 角色、
原 rational mask、实际素数权、sharp q-prefix 和共同参数。
它揭示一项必须保留的耦合：出现的 c/a 逆元相位中，
c 与 a、真实素数产品 pr 受 c≡−apr (mod q) 约束。
将角色正交准确求完后，逆元相位变回原 −jpr/q 相位。
所以本变换尚未提供独立的 Kloosterman 节省。

没有新完整四矩、常数预算、比例或无零边界。
这是实际主项的一条准确变换及适用桥审计，不是任意系数反例。

## 1. 全文输入与原完整周期

本轮 FULL READ [actual425](hybrid-whole-fourth-unit-unit-actual-research-whole.md)、
[337新增次弧切片](hybrid-original-high-product-minor-rational-slice-research-high-product.md)、
[246素数腿接口](hybrid-original-high-product-minor-prime-leg-research-checkpoint-audit.md)。
464§7的局部聚簇反例已经存在，本稿不将它重新算成本轮新进展。

保持 X=T/(2π)、原最大 genuine prime q、s<q、p,r<q，
实际共同参数 λ 及原 same-u profile。固定 dyadic Q,S,P,R，
PR≈QS，先用 ν 的零支撑写共同 J_q，再沿337分离 ν、g 与 profiles。
此时真实两腿为
\[
 F_q(a)=\sum_{s\in\mathcal S_q}u_s e_q(as),\qquad
 G_q(n)=\sum_{p,r<q}v_pz_r e_{q^2}(-npr).
\tag{1}
\]
u_s、v_p、z_r 是这一组固定共同参数上的原素数系数；
不能随 a、n 或角色私下另选。q-dependent sharp 区间和全部原 twists 保留。
这里仍先保留 p=s、r=s；它们的精确修正要由原正能量合同另付。

本次 K 的两套删弧条件分别是
d≤W、半径 W/(dS)，以及 W<d≤B、半径1/S。
两者都允许整数平移 m，故其 complement mask 仅依 n mod q，
记 Ω_q(a)。包括 q∤n。对 n=a+qj、1≤a≤q−1，
F_q(n)=F_q(a)，Ω_q(n)=Ω_q(a)。

共同 J_q 的完整 q-period 内部可写成同一个整数区间 j_0≤j≤j_1；
两个不完整端period另保留。以下身份也支持任意准确有限 j 集合，
包括把真实端点放进 w_q(n) 的零支撑。定义
\[
 H_q(a)=\sum_j w_q(a+qj)G_q(a+qj),\qquad
 \mathcal T_q=\sum_{a=1}^{q-1}\Omega_q(a)F_q(a)H_q(a).
\tag{2}
\]
w_q(n) 保留共同参数后的原外相位与有限频率端点。
本稿不估计其 Fourier 尾，也不删掉任何实际 j。

## 2. 全部平方模角色及确切参数

q为奇素数。对 q∤x 定义 Fermat quotient
\[
 Q_q(x)=\frac{x^{q-1}-1}{q}\pmod q.
\tag{3}
\]
它在 units mod q² 上良定义：
Q_q(xy)=Q_q(x)+Q_q(y)，Q_q(1+qz)=−z (mod q)。
这两式直接由整数二项式展开成立。

令 ψ遍历全部 mod q 乘法角色，0≤c≤q−1，置
\[
 \chi_{c,\psi}(x)=\psi(x\bmod q)e_q(-cQ_q(x)).
\tag{4}
\]
这些给全部 q(q−1)=φ(q²) 个 mod q² 角色，且
\[
 \chi_{c,\psi}(1+qz)=e_q(cz).
\tag{5}
\]
不同 c 由 principal-units 限制区分，同 c 下由 ψ区分；
计数与角色群阶相同，所以没有遗漏。
c=0 恰为从 mod q 诱导的角色；c≠0 恰为 conductor q² 的 primitive 角色。

定义 τ(\barχ)=Σ_(x mod q²)^* \barχ(x)e_(q²)(x)。
写 x=a+qj、1≤a≤q−1、0≤j≤q−1。
由(5)，\barχ(a+qj)=\barχ(a)e_q(−cj/a)，于是
\[
 \tau(\bar\chi)=
 \sum_{a=1}^{q-1}\bar\chi(a)e_{q^2}(a)
 \sum_{j\bmod q}e_q(j(1-c\bar a)).
\tag{6}
\]
内和准确为 q·1_(a=c)。因此
\[
 \tau(\bar\chi_{c,\psi})=
 q\,\bar\chi_{c,\psi}(c)e_{q^2}(c)\quad(c\ne0),
 \qquad \tau(\bar\chi_{0,\psi})=0.
\tag{7}
\]
这同时包含 principal 与所有 imprimitive 角色的零Gauss项；
不是把它们当作已经付款的解析误差。

## 3. 原素数产品和的完整 primitive 展开

对 unit v，角色正交给
\[
 e_{q^2}(v)=\frac1{\phi(q^2)}
 \sum_{\chi\bmod q^2}\tau(\bar\chi)\chi(v).
\tag{8}
\]
所有 p,r<q 的 genuine primes 均为units。固定原系数定义
\[
 A_\chi=\sum_{p<q}v_p\chi(p),\qquad
 B_\chi=\sum_{r<q}z_r\chi(r).
\tag{9}
\]
它们保留实际素数、原两端和共同参数。
对 q∤n，将 v=−npr 代入(8)，用(7)得
\[
 G_q(n)=\frac q{\phi(q^2)}
 \sum_{c=1}^{q-1}e_{q^2}(c)
 \sum_{\psi\bmod q}\bar\chi_{c,\psi}(c)
 \chi_{c,\psi}(-n)A_{\chi_{c,\psi}}B_{\chi_{c,\psi}}.
\tag{10}
\]
全部交换都是有限和，不需要 zeta 或 Dirichlet-L 无零前件。

χ(−a−qj)=χ(−a)e_q(cj\bar a)，故置
\[
 D_{q,a}(c)=\sum_jw_q(a+qj)e_q(cj\bar a)
\tag{11}
\]
可严格把(2)写为
\[
 H_q(a)=\frac q{\phi(q^2)}
 \sum_{c=1}^{q-1}e_{q^2}(c)D_{q,a}(c)
 \sum_{\psi\bmod q}
 \bar\chi_{c,\psi}(c)\chi_{c,\psi}(-a)
 A_{\chi_{c,\psi}}B_{\chi_{c,\psi}}.
\tag{12}
\]
出现了准确逆元 \bar a mod q，然而角色素数和与 c、q 同时变化。
原短 j 和并没有因此变成独立三系数结构。

## 4. 求完 tame 角色后的确切耦合

将(9)展开，内 ψ和对每个真实 pr 给
\[
 \sum_\psi\chi_{c,\psi}(-apr/c)
 =(q-1)\mathbf1_{-apr\equiv c\ (q)}
 e_{q^2}(-apr-c).
\tag{13}
\]
验证最后相位：在同余成立时，x=−apr/c mod q² 有 x≡1 (q)，
由(5) χ(x)=e_q(c(x−1)/q)，而 c(x−1)≡−apr−c (mod q²)。
没有取实部、绝对值或放大同余族。

将(13)代回(12)，因 q(q−1)=φ(q²)，得到
\[
 H_q(a)=
 \sum_{c=1}^{q-1}
 \sum_{\substack{p,r<q\\-apr\equiv c\ (q)}}
 v_pz_r e_{q^2}(-apr)D_{q,a}(c).
\tag{14}
\]
每个 actual unit pr 唯一确定非零 c。
在该准确同余族上 c\bar a≡−pr (q)，所以
\[
 D_{q,a}(c)=\sum_jw_q(a+qj)e_q(-jpr).
\tag{15}
\]
(14)准确恢复(2)；出现逆元不等于产生新的独立相消变量。

## 5. 外部工具及真正需要的新输入

本轮只读取了[Bettin–Chandee原作者摘要](https://arxiv.org/abs/1502.00769)，
确认其目标相位和系数组织是三线性逆元和。
本稿没有读取并消费该论文的主定理，没有据摘要准入任何指数。

若要用这类工具，需要在(12)保留 primitive 角色联合相消，
同时证明 A_χ B_χ 与 c、a、q 的准确组织符合工具的系数合同；
或在(14)对受产品同余约束的实际六腿相关完成合法变换及完整tails。
把 D 的 c/a 相位单独展示，而把其余多变量依赖叫作任意系数，
并不能直接取得三线性估计。

普通ζ的[R_θ]不提供此 conductor q² 的角色素数和联合预算。
本稿也没有把既有Hecke引用输入自动改写为这个新合同。
所有 ν、g、原C² profile、同-u、最大标签位置及 s排除仍须在
实际 signed 主项中恢复；本有限身份本身不能支付那些解析量。

下一项非平凡工作是对(12)的 actual character-product coefficient
或等价(14)的 shifted covariance 建立单侧预算。
当前目标仍是改善完整四阶主项，并最终提高实际比例或无零边界。
