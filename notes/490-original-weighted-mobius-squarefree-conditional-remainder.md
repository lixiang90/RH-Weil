# 490. 带权 Möbius 前缀与条件完整误差 3/7

2026-10-08。基线 main a4e4c8cf3de71450325174028f0ed09dd5ef4dec。
继续488的原 prime/squarefree 核心，在普通 zeta 全高度无零前件
\([R_\theta]\colon\zeta(z)\ne0\) 对全部 \(\Re z>\theta\)、
\(1/2<\theta<1\) 下，完整误差四矩为
\[
\boxed{P_H=R_{{\rm sf},\theta}+E_\theta,\qquad
\mathcal M_{E_\theta}\ll X^{c_\theta+\epsilon},\quad
c_\theta=1-\frac1{2\theta}.}
\]
这是有前件的原完整函数差，不是剩余主项的四矩上界。
在476的原 \([R_{7/8}]\) 与完整增长合同下，具体得到
\[
\boxed{\mathcal M_{E_{7/8}}\ll X^{3/7+\epsilon},\qquad
\mathcal M_{P_H}=\mathcal M_{R_{{\rm sf},7/8}}
+O(X^{9/14+\epsilon}).}
\]
488的无条件完整误差 \(1/2\) 仍保留。两套参数对应不同的准确主项，
不能相互用 signed 子族范数推界。

完整证明见[带权前缀研究源](../reviews/2026-10-08/hybrid-original-weighted-mobius-squarefree-perron-research-high-product.md)，
不同作者全文复核见[独立审查](../reviews/2026-10-08/hybrid-original-weighted-mobius-squarefree-perron-review-peer.md)。
有限身份与有理费用检查见[检查器](../scripts/hybrid_squarefree_remainder_checkpoint.py)
及[保存输出](../output/hybrid-squarefree-remainder-checkpoint.json)。
有限系数和实有理 Euler 特化不证明复半平面的收敛、内部移线或零点计数。

## 1. 保留实际局部 Euler 权的前缀

取 \(w=1/2+1/L-i\tau\)，保留所有 \(r\) 的真实互素条件和局部权：
\[
d_{r,w}(a)=\mathbf1_{a\ {\rm squarefree},(a,r)=1}
\mu(a)\prod_{p\mid a}(1+p^{-w})^{-1},\qquad
S_{r,w}(x)=\sum_{a\le x}d_{r,w}(a)a^{-w}.
\]
在独立 Dirichlet 变量 \(z\) 中准确有
\[
\sum_{a\ge1}d_{r,w}(a)a^{-z}
=\frac{K_r(z,w)}{\zeta(z)},\quad
K_r=\prod_{p\nmid r}
\left(1+\frac{p^{-z-w}}{(1+p^{-w})(1-p^{-z})}\right)
\prod_{p\mid r}(1-p^{-z})^{-1}.
\]
当 \(\Re z\ge\theta+\delta\) 时，
\(\Re(z+w)>1+\delta\)，前一乘积绝对且高度一致收敛；
后一有限乘积可用 \(r^\eta\) 吸收。无需 \(K_r\) 的倒数。

内部 Perron 从 \(\Re z=1+1/L\) 起，完整初线绝对级数为
\(O(L)\)。对任意实际 \(x=V/e\)，用 \(\lfloor x\rfloor+1/2\)
保留准确前缀。截断高度 \(T/32\)，远尾用完整初线绝对级数，
固定 divisor 幂界仅用于有限近端。
在原全高度无零前件及带 buffer 的 \(1/\zeta\) 增长估计下，
移至 \(\Re z=\theta+\delta\) 给
\[
S_{r,w}(x)\ll r^\eta
\left(x^{\theta-1/2+\delta}T^\rho
+ \sqrt{x}\,T^{-1+\rho}\right)\log^C X.
\]
内部高度扩到 \([3T/32,133T/32]\)，所以必须使用全高度前件。
内部相对实部始终为正，没有跨越 Perron 核极点。

## 2. 完整分区及外部边界

原局部因子准确为
\[
F_{V,r}(w)=\prod_{p\mid r}(1+p^{-w})^{-1}
\sum_{\substack{e\mid{\rm rad}(r)\\e\le V}}\mu(e)S_{r,w}(V/e).
\]
这里没有额外 \(e^{-w}\)。保留所有 \(e,r\) 后，
\(C_{\ge2}\ll V^{\theta-1/2+\delta}T^\rho X^\eta\)，另有负幂尾。
这只用于外部移线的左边；外部水平边界继续用488的无条件
\(\sqrt V\) 局部界和长 Euler 截断，不能偷换成全条带前缀界。

置 \(\beta=2\theta-1\)、\(U=V=\lfloor X^v\rfloor\)、\(H=V^2\)。
原 Type I 的真实 \(-F_{\Lambda,U}G_V\) 两因子、
genuine-prime 的 \(2\le r\le H\) 子域及全部 proper powers
分别按带权前缀和经典 zeta 四矩付款。
原 \(r>H\) 尾、scalar proper-power 迁移、低段和全部两端继续保留。
完整费用上界为
\[
\max\{2y-1,\,4\beta v,\,1-4v,\,0\}.
\]
取
\[
v=\frac1{8\theta},\qquad y=1-\frac1{4\theta}
\]
得 \(c_\theta=1-1/(2\theta)\)，且 \(0<v<1/4\)、
\(\max(1/2,2v)<y<1\) 严格成立。
具体 \(\theta=7/8\) 时 \(v=1/7,y=5/7,c_\theta=3/7\)。
不把 \(\theta=1/2\) 的非法参数端点 \(v=1/4,y=1/2\) 宣布为零费用。

新的准确主项仍是488给出的原负 prime/squarefree 卷积，
只把 \(U,V,Y\) 改为本节配置，保留全部方面比、
\(Y<mk\le X\)、原 \(b_V(k)\)，不增加 \((m,k)=1\)。
476的完整 \(5/7\) 输入和 Hölder 差给
\((3(5/7)+3/7)/4=9/14\)。
相对488，误差节省 \(1/14\)，传递节省 \(1/56\)；
相对486分别节省 \(12/119\) 与 \(3/119\)。

## 3. 既有边界的应用与研究范围

仅接受451既有边界及其全部引用输入时，代入 \(\theta_*\) 得
\[
0.4285433582424544<c_*<0.4285433582424561,
\]
\[
0.6427843417753810<
\frac{3B_I(\theta_*)+c_*}{4}
<0.6427843417753854.
\]
有理端点、三次根区间符号、参数 guard 和费用均可精确重放。
这没有减少451的 Hecke 全族等前件，也没有产生新无零边界。

平方自由因子的减一项仍保留，prime 卷积在普通 zeta 零点处
仍有原留数 \(-m_\rho\)。本次只加强完整误差付款，
尚未降低剩余主项的完整四矩，也未取得中心四阶常数预算。
实际简单零点比例、已知比较值及既有条件无零边界保持；
新纪录或新边界论文的发布条件尚未满足。
