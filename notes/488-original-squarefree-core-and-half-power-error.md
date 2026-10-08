# 488. 原平方自由主项与无条件半幂完整误差

2026-10-08。基线 main `a4e4c8cf3de71450325174028f0ed09dd5ef4dec`。
继续原数域和真实素数函数。本轮由实际生成函数的极点消除得到
\[
\boxed{P_H=R_{\rm sf}+E_{\rm sf},\qquad
\mathcal M_{E_{\rm sf}}\ll X^{1/2+\epsilon}.}
\]
该完整误差界不使用无零假设。在476的原普通 zeta 全高度
\([R_{7/8}]\) 及其完整增长合同下，另有
\[
\boxed{\mathcal M_{P_H}=\mathcal M_{R_{\rm sf}}
       +O(X^{37/56+\epsilon}).}
\]
剩余主项的完整四矩仍未改善；没有常数级中心四阶预算、
新零点比例或新无零边界。

完整连续推导见[平方自由核心研究源](../reviews/2026-10-08/hybrid-original-squarefree-core-euler-perron-research-perron.md)，
不同作者全文复核见[独立审查](../reviews/2026-10-08/hybrid-original-squarefree-core-euler-perron-review-peer.md)。
有限系数与费用复核见[检查器](../scripts/hybrid_squarefree_remainder_checkpoint.py)
和[保存输出](../output/hybrid-squarefree-remainder-checkpoint.json)。
有限检查不认证无限 Euler 乘积、移线或零点计数。

## 1. 原函数及准确的新主项

保持 \(X=T/(2\pi)\)、\(L=\log X\)、\(J_T=[T/4,4T]\)、\(a_L\ge c_\phi>0\)，
\[
P_H(t)=\frac1{a_LL}\sum_{\sqrt X<p\le X}\frac{\log p}{\sqrt p}p^{it},
\qquad \mathcal M_F=T^{-1}\int_{J_T}|F(t)|^4dt.
\]
取
\[
U=V=\lfloor X^{1/8}\rfloor,\quad H=V^2,\quad Y=X^{3/4},
\qquad b_V(k)=\sum_{d\mid k,d\le V}\mu(d).
\]
剩余准确为
\[
R_{\rm sf}(t)=-\frac1{a_LL}
\sum_{\substack{m>U\ {\rm prime},\ k>V\ {\rm squarefree}\\Y<mk\le X}}
\frac{\Lambda(m)b_V(k)}{\sqrt{mk}}(mk)^{it}.
\]
保留原负号、全部 \(m,k\) 方面比、共同乘积两端及精确 floors，
不增加 \((m,k)=1\)。它与486的配置不同，不能互当 signed 子族。
这里只留下 valuation 恰为1的平方自由 \(k\)，不是按指数奇偶取核。

## 2. 两个完整算术子域的付款

唯一写 \(k=s(k)r(k)\)，\(s\) squarefree、\(r\) squarefull、\((s,r)=1\)。
原401行尾源给真实局部因子 \(F_{V,r}(w)\)，准确保留所有
\(e\mid\operatorname{rad}(r)\)、\(ae\le V\)、\((a,r)=1\) 和 Möbius 符号。
置 \(C_{\ge2}(w)=\sum_{2\le r\le H,\ r\ \mathrm{squarefull}}r^{-w}F_{V,r}(w)\)。
在初始绝对收敛域，严格有
\[
\sum_{\substack{k>V\\2\le r(k)\le H}}b_V(k)k^{-w}
 =\frac{\zeta(w)}{\zeta(2w)}C_{\ge2}(w).
\]
这部分不产生 \(k=1\)，且 \(2\le k\le V\) 的 \(b_V(k)=0\)，
所以没有“减一”项。相反，平方自由部分仍准确为
\(\zeta(w)F_{V,1}(w)/\zeta(2w)-1\)。

真正素数外因子为
\[
A_U=-\zeta'/\zeta-Q_{\rm pp}-F_U^{\rm prime},
\]
其中 \(Q_{\rm pp}\) 含全部 proper powers，\(F_U^{\rm prime}\) 仅含 \(p\le U\)，
不能用全部 \(\Lambda_{\le U}\) 再重复扣除小 proper powers。
因此全部 genuine \(m>U\)、\(2\le r(k)\le H\) 的原负生成函数成为
\[
\frac{[\zeta'+(Q_{\rm pp}+F_U^{\rm prime})\zeta]C_{\ge2}}
     {a_LL\zeta(2w)}.
\]
普通 zeta 零点处的极点准确消失。全部 proper-power \(m>U\) 的原生成函数另为
\(-Q_{>U}(\zeta G_V-1)/(a_LL)\)，其中 \(G_V=\sum_{d\le V}\mu(d)d^{-w}\)。

在 \(\Re w=1/2+1/L\)，有限局部因子绝对界给
\(|C_{\ge2}|\ll\sqrt V X^\epsilon\log^C X\)；
\(1/\zeta(2w)\)、全部 proper powers 均可用绝对收敛支付。
经典 \(\zeta\) 四矩和其 Cauchy 导数四矩分别支付两个实际子域为
\(X^{4v+\epsilon}\)、\(X^{2v+\epsilon}\)，\(U=V=\lfloor X^v\rfloor\)。

## 3. 无限尾和新完整账本

先在 \(\Re w=1+1/L\) 用无限 Dirichlet 系数身份，
对两个半整数乘积端点施截断 Perron，再移到 \(1/2+1/L\)。
完整远尾的准确权是 \(n^{-1-1/L}\)，以 \(\zeta^3\) 的导数支付；
不能把固定 \(n^\eta\) divisor 界用到无穷。
正高度 guard 排除 pole1，已消除的零点极点没有隐藏留数；
全部水平边界用长有限 Euler 截断给负幂。

原 Type II 重新不交分成：全部 proper-power \(m>U\)、
genuine-prime 的 \(r>H\) 尾、genuine-prime 的 \(2\le r\le H\)、
以及上述平方自由主项。尾证明对 \(M_0=U\) 有效，允许 \(m\mid r\)。
原低段、Type I 和 scalar proper-power 迁移完整保留，费用为
\[
\max\{2y-1,4v,2v,1-4v,0\}.
\]
取 \(v=1/8,y=3/4\)，五项为 \((1/2,1/2,1/4,1/2,0)\)。
合成的正是 \(E_{\rm sf}=P_H-R_{\rm sf}\)，没有使用子集范数单调性。

## 4. 完整传递及真正未付款项

仅在接受476的完整条件增长后，\(R_{\rm sf}=P_H-E_{\rm sf}\) 继承 \(5/7\)。
两个完整函数的 Hölder 差给 \((3(5/7)+1/2)/4=37/56\)。
相对486，误差指数节省 \(1/34\)，传递指数节省 \(1/136\)。

接受451既有边界及全部引用前件时，用476的 \(B_I(\theta_*)\) 可同样得到
传递指数 \((3B_I(\theta_*)+1/2)/4\)，严格位于
\((0.6606485022147674,0.6606485022147714)\)。
该代数应用没有降低451的依赖或产生新边界。

平方自由生成函数仍有 \(-1\)，其 prime 卷积在每个 \(\Re\rho>1/2\)
的 zeta 零点处保留原留数 \(-m_\rho\)。
新付款只消除 \(r\ge2\) 子域的极点，尚未控制真正 prime/squarefree 联合四阶。
已知比例、既有条件无零边界及完整增长基线保持。
