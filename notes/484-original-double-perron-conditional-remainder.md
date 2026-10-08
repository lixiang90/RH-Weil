# 484. 原路线双因子 Perron 的条件完整误差改进

2026-10-08。基线 main `fdf86cb439a6c5df8ca0a8e8a526b2b9d177d286`。
本笔记记录在原无零引用输入下的实际误差归约；不重新认证引用输入本身。

在普通 zeta 的整个 \(\Re s>7/8\) 无零这一前件下，保持同一真实素数函数，
完整分区误差第四矩从482的 \(49/81\) 降到
\[
\boxed{\mathcal M_{E_{\Lambda\mu}}\ll X^{43/75+\epsilon}},
\qquad P_H=R_{\Lambda\mu}+E_{\Lambda\mu}.
\]
结合476已有的完整 \(5/7\) 增长输入，完整第四矩传递误差为
\[
\boxed{\mathcal M_{P_H}=\mathcal M_{R_{\Lambda\mu}}
       +O(X^{713/1050+\epsilon})}.
\]
它们分别节省 \(64/2025\)、\(16/2025\) 的指数。
完整余项仍只继承已有增长界；没有得到常数级中心四阶预算、
更高零点比例或新无零边界。

完整连续证明见
[研究源](../reviews/2026-10-08/hybrid-original-double-log-derivative-perron-research-checkpoint-audit.md)，
不同作者的量词、极点及费用复核见
[独立审查](../reviews/2026-10-08/hybrid-original-double-log-derivative-perron-review-peer.md)。
446已有 sharp \(\Lambda\) 接口；本轮新用途是它与真实 Möbius 因子在共同乘积
截断中的联合消费及完整误差重优化。

## 1. 两个内部接口与同一共同乘积截断

保持 \(X=T/(2\pi)\)、\(L=\log X\)、\(J_T=[T/4,4T]\)、
\(a_L\ge c_\phi>0\)，以及
\[
P_H(t)=\frac1{a_LL}\sum_{\sqrt X<p\le X}
 \frac{\log p}{\sqrt p}p^{it},\qquad
\mathcal M_F=T^{-1}\int_{J_T}|F(t)|^4dt.
\]
先固定 \([R_\theta]\)：普通 zeta 在整个 \(\Re s>\theta\) 无零，
\(1/2\le\theta<1\)。再固定正 buffer
\(\delta<(1-\theta)/4\) 及最终小损失。

对全部真实 prefixes \(1\le N\le X\)、全部
\(\tau\in[T/8,33T/8]\)，degree-one 对数导数给
\[
\sum_{n\le N}\Lambda(n)n^{-1/2+i\tau}
=\frac{(N^\sharp)^{1/2+i\tau}}{1/2+i\tau}
 +O\left(N^{\theta-1/2+\delta}\log^2T
        +\sqrt N\,T^{-2}\{\log^2(2N)+\log T\}\right).
\]
\(N^\sharp=\lfloor N\rfloor+1/2\)；\(N<2\) 直接处理。
内部 Perron 高度是 \(T^2\)，移线不跨零点或核的原点，
但必须跨并支付 zeta 的主极点留数，其绝对费用为 \(O(\sqrt N/T)\)。
全部无穷 Dirichlet 尾、半整数最近项及水平线均包含在上式。

Abel 保留全部 prefixes，给实部 \(1/2+1/L\) 的同样上界。
genuine-prime prefix另以明确 proper-power 差 \(O(\log^2(2N))\) 支付，
不能从全 \(\Lambda\) signed 范数推出任意子集范数。
原 Möbius prefix在同一 guard 给
\[
\left|\sum_{d\le V}\mu(d)d^{-1/2-1/L+i\tau}\right|
 \ll V^{\theta-1/2+\delta}X^\rho.
\]

原短项保持全部 \(\mu\) 符号和 \(Y<mk\le X\)。
对有限三因子 \(F_\Lambda G_VW_{\lfloor X\rfloor}\) 先施外层 Perron，
其高度 \(T/8\) 与上述内部高度分开，移位 \(\tau=t-\omega\) 始终正。
半整数的两个端点恢复原 sharp 乘积掩码；矩形中的全部额外 \(n>X\)
在负幂截断误差中付款。随后才取三个因子的绝对上界。
结合 \(W\) 的原 Weyl 界和原实际二矩，得
\[
\mathcal M_{S_{B,A,q}}
 \ll X^{1/3+(2\theta-1)(a+v)+\epsilon},
\quad U\le B<A,\quad q(m)=1\text{ 或 }1_{\mathrm{prime}}(m).
\]
这里 \(U=V=\lfloor X^v\rfloor\)、\(A=\lfloor X^a\rfloor\)、
\(Y=X^y\)，要求 \(0<v<a\)、\(v<1/4\)、
\(\max(1/2,a+v)<y<1\)。这个费用估计针对原子项自身。

## 2. 完整费用族及限定最优性

保持 \(H=V^2\)，原 low、Type I、proper-power 与完整平方丰满尾付款不变。
合成成本为
\[
C=\max\{2y-1,\ 1/3+2v,\ 1/3+(2\theta-1)(a+v),
          \ 1-2a,\ 1-4v,\ 0\}.
\]
这个费用族的最优值是
\[
c_\theta=\max\left\{\frac59,\frac{18\theta-5}{18\theta+3}\right\}.
\]
两个下界分别来自 Type I 与尾，以及 short 与 proper/tail。
\(\theta\le5/6\) 时取 \((v,a,y)=(1/9,2/9,7/9)\)；
\(\theta\ge5/6\) 时取
\[
v=\frac2{18\theta+3},\quad a=2v,
\quad y=\frac{18\theta-1}{18\theta+3}.
\]
这是所列费用和 \(H=V^2\) 域的最优性，不是所有算术方法的最优性。

\(\theta=7/8\) 的真实整数参数为
\[
U=V=\lfloor X^{8/75}\rfloor,\quad
A=\lfloor X^{16/75}\rfloor,\quad H=V^2,\quad Y=X^{59/75}.
\]
五项费用依次为 \((43/75,41/75,43/75,43/75,43/75)\)。
最终余项保持
\[
R_{\Lambda\mu}(t)=-\frac1{a_LL}
\sum_{\substack{m>A,\ m\ \mathrm{prime}\\k>V,\ r(k)\le H\\Y<mk\le X}}
\frac{\Lambda(m)b_V(k)}{\sqrt{mk}}(mk)^{it},
\]
\[
b_V(k)=\sum_{d\mid k,d\le V}\mu(d),\qquad
r(k)=\prod_{v_p(k)\ge2}p^{v_p(k)}.
\]
\(H=V^2\) 保证 nonzero 剩余仍有一次素因子部分 \(s(k)\ge2\)，
\(A\ge H\) 保证素数 \(m\) 与 \(r\) 互素。全部 floors和端点保留。
与482的不同参数余项不能互当子族。

先用 \(R=P_H-E\) 取得完整余项的同幂范数，再作完整 Hölder 差，
\[
\frac{3(5/7)+43/75}{4}=\frac{713}{1050},
\qquad\frac57-\frac{713}{1050}=\frac{37}{1050}.
\]
增长误差相对 \(X^{5/7}\) 有省幂，不能当成常数级 \(o(1)\)。

## 3. 消费已经交付的三次边界

[451](451-kappa-feedback-cubic-boundary-and-family-continuation.md)和
[正式边界论文](../papers/kappa-feedback-cubic-boundary-paper.tex)
在其明确引用输入下给普通 zeta 的 \(\Re s>\sigma_*\) 无零，其中
\[
657e_*^3-954e_*^2+21e_*+20=0,\quad
\sigma_*=11/12-e_*/4,
\]
\[
16683858898627/10^{14}<e_*<16683858898628/10^{14}.
\]
因此同一个条件费用族也可以取已经交付的 \(\theta=\sigma_*>5/6\)。
这使用既有边界，没有证明新边界，也不降低451本身的引用依赖。
精确写成
\[
c_* =\frac{23-9e_*}{39-9e_*},\quad
v_* =\frac4{39-9e_*},\quad a_*=2v_*,
\quad y_* =\frac{31-9e_*}{39-9e_*}.
\]
同时，476已经证明整个 \(5/6<\theta\le7/8\) 域的完整增长
\[
B_I(\theta)=4\theta-3+\frac{3(1-\theta)}{2\theta}.
\]
于是条件误差和完整传递的较强版本是
\[
\mathcal M_{E_*}\ll X^{c_*+\epsilon},\qquad
\mathcal M_{P_H}=\mathcal M_{R_*}
 +O(X^{\gamma_*+\epsilon}),
\quad \gamma_* =\frac{3B_I(\sigma_*)+c_*}{4}.
\]
由上述有理根区间与单调性，严格包围为
\[
0.5733157277613751<c_*<0.5733157277613762,
\]
\[
0.6789774341551112<\gamma_*<0.6789774341551154.
\]
这是条件完整误差的新应用；完整余项仍只继承476的
\(B_I(\sigma_*)\approx0.714198002953028\)，没有常数级中心四阶预算。

## 4. 原482对象的扩大截断及仍开放的主项

保持482的全部 \(V,H,Y,b_V\)，将其 genuine-prime 截断从
\(A_0=\lfloor X^{16/81}\rfloor\) 扩至
\(A_1=\lfloor X^{64/243}\rfloor\)。完整该 \(m\) 带先付全部 \(k\)，
再直接付相同 \(m\) 掩码的 \(r>H\) 尾；两完整函数相减得到原小 \(r\)
余项中的该带费用 \(49/81\)，原矩传递仍为 \(779/1134\)。
\(A_1/A_0\asymp X^{16/243}\) 是同一原对象中的实际扩大。

这个一点接口直接用于 whole只给 \(2\theta-1\)，在 \(7/8\) 为
\(3/4>5/7\)。三因子费用若扩大到 \(m\asymp X^{1/2}\)，并要求尾费
不超过 \(5/7\)，则短项费用至少 \(16/21\)，同样不能支付 balance core。
这是当前费用法的限制，不能当作实际主项的下界或普遍不可能性。

原生成函数的零点留数仍为 \(-m_\rho\)。剩余任务是同一实际
signed prime/squarefree 余项的联合四阶均值、真实次弧及完整谱常数预算。
项目已知简单临界线比例67.3482429920796…%和无零边界保持，
本笔记未触发新纪录或新边界论文发布。

## 5. 精确检查的有限范围

[检查脚本](../scripts/hybrid_double_perron_checkpoint.py)与
[保存输出](../output/hybrid-double-perron-checkpoint.json)绑定最终研究源、独立审查、
本笔记及451/476输入的 canonical LF 身份。使用
`python -B scripts/hybrid_double_perron_checkpoint.py --check` 只读复核。
检查覆盖费用的有理运算、三次根的有理隔离和 \(c_*,\gamma_*\) 包围；
它不证明 Perron、无零前件、实际 Möbius 相消、无限矩估计或 RH。
连续数学依据仍是所链接的完整证明与审查，有限 PASS 不能替代它们。
