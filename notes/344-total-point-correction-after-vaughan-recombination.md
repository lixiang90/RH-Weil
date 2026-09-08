# 344. Vaughan合并后全部Poisson点修正的总量

2026-09-08。周期9第4动作的一部分。[T]。
Franklin只读[独立复核通过](../reviews/2026-09-08/344-independent-review.md)；
最终余项表示仍以343相关结论为依赖。
沿用335的整数X、固定cell及342的连续核替换；引用343的准确Poisson公式。
343已另行通过Gibbs独立审查。本篇只处理其E_pt，不审查或代替非零频率和。

## 1. 先合并两通道，恢复点上的实际算术权

固定b,c,d为I内prime powers、c!=d，记a0=bc/d、epsilon=X^-1/2，
H(t)=K_infty(t)-bar K_infty(M)，M=sqrt X。对正实a定义
\[
 \phi(a)=a^{-1/2}W(a,b,c,d)H(X\log(a/a_0))
 {\bf1}_{[A,B]}(a){\bf1}_{|\log(a/a_0)|\le\epsilon}
 {\bf1}_{a\ne b}{\bf1}_{a\ne a_0}.
\]
端点按闭区间，两个删除点按原值删除，左右极限照常；phi在支持外作零延拓。
令
\[
 P_{bcd}(a)=\phi(a)-\tfrac12\{\phi(a-)+\phi(a+)\}.
                                                               \tag{1}
\]
343中m=rv>0，f(w)=phi(mw)，正尺度不交换左右极限，故
E_pt(r,v,b,c,d)=sum_(w in Z) P_bcd(rvw)。
所有可能的非零P点在[A,B]，即使端点与删除点重合也由(1)一次处理。

将两个Vaughan通道合并，全部点修正为
\[
 E_X={1\over16\pi^4}
 \sum_{\substack{b,c,d\in I\\c\ne d}}
 {\Lambda(b)\Lambda(c)\Lambda(d)\over\sqrt{bcd}}
 \sum_{\substack{r\ge1,v>V\\rv\le B}}\mu(r)\Lambda(v)
                   \sum_{w\in\mathbb Z}P_{bcd}(rvw).
\]
每个固定X这里都是有限和。在每个整数a in [A,B]上重组，准确得到
\[
 \sum_{\substack{r,v\ge1\\v>V,\ rv\mid a}}\mu(r)\Lambda(v)
 =(\mu*1*\Lambda_{\rm hi})(a)=\Lambda_{\rm hi}(a)=\Lambda(a),       \tag{2}
\]
因为A>V（充分大X）。所以
\[
 \boxed{E_X={1\over16\pi^4}
 \sum_{\substack{b,c,d\in I\\c\ne d}}
 {\Lambda(b)\Lambda(c)\Lambda(d)\over\sqrt{bcd}}
 \sum_{a\in I\cap\mathbb Z}\Lambda(a)P_{bcd}(a).}                  \tag{3}
\]
端点是否被包含、删点是否重合，均只取决于a,b,c,d，不取决于a=rvw的分解。
这一步用的是完整I+II，绝不先以|mu|替代mu再声称恢复Lambda。

## 2. shell两端不能成为整数点

若某整数a,b,c,d及当前整数X满足|X log(ad/bc)|=sqrt X，则
\[
 {ad\over bc}=\exp(\pm1/\sqrt X).
\]
左侧有理，右侧无理：±1/sqrt X是非零实代数数，应用经典Lindemann推论[R]。
本篇只需无理性，不需任何有效超越度或接近有理数的下界。
条款参见已归档Popescu v2第14页Corollary3.1及其从Theorem3.1导出的短证明。
不将该现代背景稿的完整证明视为本项目已重审。

因此整数采样上的P只可能来自a=A、a=B、a=b及a=a0。
A<B时，cell与shell交成单点只能是一个shell端与cell端相接；
上述事实也排除这种整数单点。非整数处的跳跃不进入(3)。
这里明确依赖335的整数X；任意实X不能照搬此无端点结论。

## 3. 两种删除点

在a=a0且Lambda(a)非零时，ad=bc和gcd(c,d)=1强迫d|b；
当前同区间prime powers满足d|b只能b=d，随后a=c。
故此类点的绝对总贡献至多
\[
 C\sum_{a,b\in I}{\Lambda(a)^2\Lambda(b)^2\over ab}
 \ll L^2.                                                       \tag{4}
\]
这里|H(0)|<<1、W<=1，而sum_(n in I) Lambda(n)^2/n<<L由Chebyshev给出。
若同时为cell端点，只改变(1)中的系数为半个，仍被同一上界覆盖。

在a=b时Delta=log(d/c)，c!=d仍保持。原权成为
Lambda(b)^2 Lambda(c)Lambda(d)/(b sqrt(cd))。
用
\[
 |H(t)|\ll(1+|t|)^{-1}+M^{-1},\qquad
 |X\log(d/c)|\ge{X\over1.30Y}|d-c|
\]
和shell给出的1<=|d-c|<<YM/X，对固定c将d扩到整数：
\[
 \sum_{\substack{d\in I,\ d\ne c\\|\log(d/c)|\le M/X}}
 {\Lambda(d)\over\sqrt{cd}}|H(X\log(d/c))|
 \ll {L\over Y}\sum_{1\le |j|\ll YM/X}
       \left({Y\over X|j|}+{1\over M}\right)
 \ll {L^2\over X}.
\]
随后sum_c Lambda(c)<<Y和sum_b Lambda(b)^2/b<<L给
\[
 \text{a=b删除点绝对总量}\ll {YL^3\over X}=X^{-1/4}L^3=o(1).       \tag{5}
\]
这与338的衰减估计同型，但使用的是本篇实际合并后不同位置的相等层，
没有把338结论直接移植到单个Vaughan通道。

## 4. 两个固定cell端点

固定a=A或B及b,c，允许d遍历I中满足shell的整数。
序列t_d=X log(ad/(bc))严格递增；相邻整数d的间距至少
q=X/(1.30Y)。shell内整数点数N<<YM/X+1。
把离0最近的至多两个点单列，其余按距离排序得
\[
 \sum_d |H(t_d)|
 \ll 1+q^{-1}\log(2+N)+N/M
 \ll 1+{Y\over X}L+M^{-1}\ll1.                                  \tag{6}
\]
此界对区间相对整数格的偏移一致，不假设最接近t=0的点有正下界。
代入Lambda(d)/sqrt(d)<<L/sqrt Y，
Lambda(a)/sqrt(a)<<L/sqrt Y，以及
sum_(b,c in I) Lambda(b)Lambda(c)/sqrt(bc)<<Y，得每个端点
\[
 \text{绝对总量}\ll (L/\sqrt Y)^2Y=O(L^2).                       \tag{7}
\]
若A或B不是prime power，(3)中该端点本来就是零。
端点处(1)至多一个完整原幅度；允许与删除层在上界中有限次重叠，
不以此三角上界改写(3)的准确系数。

## 5. 得到的准确剩余问题

(3)–(7)证明候选结论
\[
 \boxed{|E_X|\ll L^2=o(L^4).}                                   \tag{8}
\]
它只控制完整I+II的点修正；没有证明逐通道绝对点修正也O(L²)。

定义
\[
 \mathcal N_X=\lim_{R\to\infty}
 \sum_{\substack{r\ge1,v>V,rv\le B\\b,c,d\in I,\ c\ne d}}
 {\mu(r)\Lambda(v)\Lambda(b)\Lambda(c)\Lambda(d)
       \over16\pi^4\sqrt{bcd}}
 \sum_{0<|k|\le R}\widehat g_{rv,b,c,d}(k).
\]
根据343，有限外层与同一对称极限相容；没有取无限k和的绝对值。
若343候选核查通过，合并342的一次O(1)、343零频O(L³)及本篇(8)得到
\[
 R_X=\mathcal N_X+O(L^3).
\]
这把同一规范化物理响应的o(L⁴)问题准确留给全部非零Poisson频率。
该剩余仍包括Type I与Type II、全部外层算术权和硬边界频率尾。
本篇没有证明它小，也没有获得RH、零密度或实际高矩的新纪录。
