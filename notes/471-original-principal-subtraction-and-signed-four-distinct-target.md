# 471：原路线的完整主密度消去与四全异相消目标

2026-10-08。沿用原 Eisenstein / AF 路线。本轮没有得到新的实际零点比例或
无零边界；新增结果是一个不需要未知第四矩有界的完整算子约化，以及
对现有二阶、行权重和奇偶 Gram 信息的严格限制。

## 1. 原对象与新来源

仍取 X=T/(2π)、ell=log X、d=floor(X ell)，保留原 interval carrier E、
P=EE*、实际高度 τ_k、taper φ、high primes sqrt X<p≤X 和 low matrix L。
normalized trace 为 τ=Tr/d。保持原 same-prime diagonal W，并记

\[
 H=E^*B_HE,\qquad \Gamma=H^2-W,\qquad q_T=\tau\Gamma^2 .
 \tag{1}
\]

本轮所有新公式均在这套归一化中解释；以下摘要不替代来源的完整证明。

| 来源 | canonical UTF-8 LF SHA-256 |
| --- | --- |
| [完整主密度消去](../reviews/2026-10-08/hybrid-whole-prime-principal-subtraction-and-product-length-research.md) | 87b98f4f1d176b72c66f07258dfb3c7499ac53844ce076c900d3d8ca9036a02f |
| [整族矩信息的张量审计](../reviews/2026-10-08/hybrid-whole-joint-moment-information-amplification-research-radial.md) | f9e3ffa1aa8c0be583b1c11fc952f8f09bd6deeee9f7bdfa31f3abda1523863e |
| [456：原完整重复标签主项](456-high-opposite-four-word-vanishing-and-repeated-limit.md) | 7de855634f93f9d92f6d0cbdd762f9894effaaf40f788b3e02de89f961eadb96 |
| [465：原平方残差](465-centered-high-square-joint-fourth-budget.md) | a9290d2d847c2a3f7942b26353bd1582a68b391e481acc109c4ac18d3d750464 |
| [470：必要下界](470-centered-spectral-variance-excludes-small-high-residual.md) | 729ddbed2b2d2af08e21e5f1ebabfb5663f906c702f52b13f81aac224402a93a |

canonical 仅将 CRLF 和 lone CR 转 LF，保留其余字符与 EOF。

## 2. 连续主密度可从完整实际算子中减去

取原 Chebyshev 原子测度的连续主密度，定义

\[
 B_0=-\frac1{a_\ell\ell}M_\phi
 \int_{\sqrt X}^{X}x^{-1/2}(R_{\log x}+R_{-\log x})\,dx\,M_\phi,
 \quad C_0=E^*B_0E,\quad \bar H=H-C_0 .
 \tag{2}
\]

这是 strong operator integral：对每个 L² 向量取向量值 Bochner integral。
不要求平移在算子范数中连续。其全高度 Fourier multiplier 准确为

\[
 D_0(t)=-\frac2{a_\ell\ell}\operatorname{Re}
 \frac{X^{1/2+it}-X^{1/4+it/2}}{1/2+it}.
 \tag{3}
\]

在 J=[T/2,3T] 上，sup|D_0|=O(X^{-1/2}/ell)；全高度的粗界为
O(sqrt X/ell)。令 F=𝓕MφE。原 packet 的两端尾满足
||1_{J^c}F||HS²=O(T^{-2})，所以

\[
 \|C_0\|_{\rm op}\le
 \sup_J|D_0|+\sup_{\mathbb R}|D_0|\,\|1_{J^c}F\|_{\rm HS}^2
 =O(X^{-1/2}/\ell).
 \tag{4}
\]

这一步包括 t≈0 的连续主峰；P 始终是原有限 interval 投影。

已付 ||H||2,d+||L||2,d=O(1)、||H||op=O(sqrt X/ell)。
含一个 C0 的任意有序四词，以 C0 和另一因子的 operator norm、
其余两个因子的 normalized S2 norm 作 Schatten Hölder，给
O(ell^{-2})。逐因子替换因而得到

\[
 \begin{gathered}
 \tau\bar H^4-\tau H^4=O(\ell^{-2}),\qquad
 \tau\bar H^3L-\tau H^3L=O(\ell^{-2}),\\
 \tau\bar H^2L^2-\tau H^2L^2=O(\ell^{-2}),\qquad
 \tau(\bar HL\bar HL)-\tau(HLHL)=O(\ell^{-2}).
 \end{gathered} \tag{5}
\]

同样适用于完整 τ(H+L)^4。保持 W 时，
||bar Γ−Γ||2,d=O(X^{-1/2}/ell)，而 ||Γ||2,d=O(sqrt X/ell)；
交费后仍有 bar q−q=O(ell^{-2})。两 parity 残差及 commutator k 的差
也为 O(ell^{-2})。证明没有预设 q=O(1) 或 τH⁴=O(1)。

来源另对每个含连续主密度的 physical 差词，支付原三个内部 P crossing
及全高度替换。这个局部比较不供应不含主密度的 whole actual/physical
等式，也不删除剩余原素数四词的有限投影。

## 3. 消去主密度没有消去长乘积问题

bar H 使用准确 signed measure

\[
 d\nu_H(x)=\sum_{\sqrt X<p\le X}\log p\,\delta_p(dx)
                 -1_{[\sqrt X,X]}dx .
 \tag{6}
\]

每个素数原子的系数仍为 b_p=(log p)/(a_ell ell sqrt p)。
令 c_H(n)=Σ_{pq=n,\ p,q high}b_pb_q。唯一分解给完整原子加权能量

\[
 \sum_n n|c_H(n)|^2
 =2\left(\sum_{p\in H}p b_p^2\right)^2
       -\sum_{p\in H}p^2b_p^4
 \asymp X^2/\ell^2 .
 \tag{7}
\]

连续交叉部分没有改变乘积测度的离散原子。有效 physical high4 虽然
只允许交替方向，仍能有 pr、qs≈X²；31 的相关两侧乘积可到 X^{3/2}。
因此不能因主密度已减，就把标准均值误差的长列改成长度 X 的短列。
原有限 walk 仍须保留共同窗口、载波相位、路径和内部 P。

(7)不是实际第四矩的下界。已知正 near 子族也不是 whole signed sum
的下界；取这些项的绝对值不能完成所需净上界。

## 4. 原完整四全异余额必须取怎样的符号

下面仅使用已付的456、465，flat profile。定义原实际矩阵的完整量

\[
 D_T=\frac1d
 \sum_{\substack{p_1,p_2,p_3,p_4\in H\\p_i\ne p_j\ (i\ne j)}}
 \operatorname{Tr}(C_{p_1}C_{p_2}C_{p_3}C_{p_4}).
 \tag{8}
\]

每个 C_p=E*B_pE，所有内部投影都仍保留。单词未必是实数，但该完整
union 为实数：整个 τH⁴ 与完整 repeated union 都是实数。
456证明 repeated union→19/240；465证明 τWH²、τW²→19/480。
所以不需要第四矩有界，即有

\[
 \tau H^4=19/240+D_T+o(1),\qquad
 q_T=19/480+D_T+o(1).
 \tag{9}
\]

主密度约化保留(9)的整个 high4 和 q；不将连续变量硬归入原重复标签。

470给

\[
 \liminf q_T\ge q_*=\frac{\sqrt{104899}-275}{15120}
 =0.00323288035989094197\ldots .
 \tag{10}
\]

故

\[
 \liminf D_T\ge q_*-19/480
 =-0.03635045297344239136\ldots .                 \tag{11}
\]

若今后想证明某个 limsup q_T≤Q<19/480 的上界，(9)严格等价于

\[
 \limsup D_T\le Q-19/480<0.                     \tag{12}
\]

这要求完整四全异部分的净负相消。只证明 D_T=o(1)，会留下
q_T→19/480≈0.0395833，不能达到接近 q_* 的预算。
(12)解释这种小残差路线的目标，不声称所有比例方法都必须满足它。
旧 Q=1/350 已被470排除；本稿不提出另一未付数值 Q。

## 5. 现有整族矩信息仍缺少一个四阶方向

第二新来源取任意固定 m≥3，

\[
 A_m=\operatorname{diag}(\sqrt{m/2},-\sqrt{m/2},0,\ldots,0),
 \quad \sigma_m=\operatorname{Tr}/m,\quad\gamma_m=m/2 ,
 \tag{13}
\]

满足 σA=σA³=0、σA²=1、σA⁴=γ_m。取 H̃=H⊗A_m，其余
L、W、V、U 和所有 row tests 都 tensor I_m。每个含零或两个 H
的有限 trace word 精确保留，含一个或三个 H 的词变为准确零。
完整 low parity 四词、整族 weighted high second、Γ 的 row 中心化、
两分量 Γ–Δ covariance 与 Z 的 norm 都保持。

置 D_m=A_m²−I_m，则 I_m、A_m、D_m 两两 HS 正交，准确有

\[
 \widetilde\Gamma=\Gamma\otimes I_m+H^2\otimes D_m,\quad
 \widetilde q=q+(\gamma_m-1)\tau H^4 .
 \tag{14}
\]

新增 H²⊗D_m 方向对上述测试不可见。q 和整个 parity gap 的470必要下界
仍保持；gap 的增量为 (γ_m−1)τ(H²UH²U)≥0。
即使 entire31 变成准确零、负 commutator 保留，仍有

\[
 \widetilde\tau(\widetilde H+\widetilde L)^4
 =\gamma_m\tau H^4+\tau L^4+6c-k
 \ge\gamma_m(\tau H^2)^2 .
 \tag{15}
\]

先固定任意 m，再取高度极限。因此所列矩信息类没有与 m 无关的统一
有限 fourth upper，亦不能通过继续优化同一组 scalar Cauchy 来补足。

这是信息接口的有限反模型。它没有实现原 scalar prime coefficients
或原单份 carrier；W⊗I_m 是保留数据的选定 center，字面 tensor 每个
prime 后的 same-prime operator 会是 W⊗A_m²。没有把这一差异当作小误差，
也没有验证原 raw/tail 合同或零侧惯性账本。反模型不否定实际素数结构、
其他零点比例方法或利用谱尾的机会。

## 6. 本轮结论与后续目标

本轮完成原完整算子的连续主密度约化，明确了剩余长乘积的真实尺度。
同时证明现有整族行权重和 split Gram 信息不能单独供应 whole fourth
上界。利用456、465定位的低 q 目标必须是原四全异净负相消。

继续研究应直接使用原 scalar prime 系数与共同 finite walk：控制
τ(ΓH²)，或给整个 D_T 的带符号上界，同时支付原 P crossing。
不把 isolated near 正子族、连续密度替换或额外 static row tests
当成完整第四矩的证明。当前实际比例及依赖原 [R] 的边界均未更新；
尚不满足新增无零边界论文的条件。

新稿的独立审查与有限精确核验会随同本笔记归档。代码核验只覆盖有限
代数和冻结绑定；渐近算子与素数估计仍由来源及全文审查给出。
