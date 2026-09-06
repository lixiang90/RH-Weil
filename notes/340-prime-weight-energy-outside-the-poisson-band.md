# 340. 实际素数权的Fourier能量不集中于Poisson长度

2026-09-07。周期8第5动作：实际系数局部化检查。[T候选，待独立复核]。
这是经典定量PNT和Parseval的应用，不宣称新的素数定理或普遍Kloosterman障碍。

## 1. 真实一变量权与准确结论

沿用335–336的Y=X^(3/4)、I=[ceil(.70Y),floor(1.30Y)]和p约Y²。
对n in F_p使用固定整数代表，定义
\[
 w(n)={\Lambda(n)\over\sqrt n}{\bf1}_{n\in I},\qquad
 v(n)={1\over\sqrt n}{\bf1}_{n\in I},
\quad \widehat w(\alpha)=\sum_nw(n)e_p(-\alpha n).
\]
这里w确实是q_ab四个因子中各自的一变量权；没有换成任意系数。
频率使用有符号代表|alpha|<=p/2，定义
Q=floor((p/Y)B_Y)，Omega_Q={alpha:|alpha|<=Q}。

取任意固定A>0，B_Y=(log Y)^A。则无RH有
\[
 \sum_{\alpha\bmod p}|\widehat w(\alpha)|^2
       \sim p\log Y\log(13/7),                         \tag{1}
\]
\[
 \sum_{\alpha\in\Omega_Q}|\widehat w(\alpha)|^2
       \sim p\log(13/7),                               \tag{2}
\]
从而该带捕获的能量比例渐近为1/log Y，带外比例趋于1。
特别是不能将实际prime-power权按普通平滑Poisson直觉截在p/Y乘任意固定log幂，
再声称l2尾项可忽略。

## 2. 采用的外部输入

既有原件Fiori–Kadiri–Swidinsky，
[arXiv:2204.02588v3](https://arxiv.org/abs/2204.02588v3)，
[本地PDF](../literature/background/fiori-kadiri-swidinsky-psi-v3.pdf)第2页Corollary1.4给无条件
|psi(x)-x|<9.22022 x(log x)^(3/2) exp(-.8476836 sqrt(log x))（x>2）。
本次重新核读第1–4页的定义、陈述和依赖说明，未重新认证全篇显式常数及数值包。
这里只采用其经典定量PNT弱化：对固定c=.8、t约Y，
\[
 \psi(t)-t=O(Y\epsilon_Y),\qquad
 \epsilon_Y=\exp(-c\sqrt{\log Y}).                     \tag{3}
\]
较小c吸收固定区间比例和log因子；不需要优化.8476836。
该经典输入不依赖RH，也不以有限RH验证替代全RH。

## 3. 带内prime权与平滑密度接近

对每个alpha，分部求和作用于sum_(n<=t)(Lambda(n)-1)=psi(t)-floor(t)。
在I内取g(t)=t^(-1/2)e(-alpha t/p)，其端点与导数给
\[
 |\widehat w(\alpha)-\widehat v(\alpha)|
 \ll \sqrt Y(1+|\alpha|Y/p)\epsilon_Y.                 \tag{4}
\]
整数端点引起的有限跳跃由同一个部分和界包含；取整不改变估计。
于是
\[
 \sum_{\Omega_Q}|\widehat w-\widehat v|^2
 \ll p B_Y(1+B_Y)^2\epsilon_Y^2=o(p).                  \tag{5}
\]
此处需要Q<p/2，对固定A及充分大Y成立。

平滑v的完整Parseval质量为
\[
 \sum_\alpha|\widehat v(\alpha)|^2
 =p\sum_{n\in I}{1\over n}
 =p\{\log(13/7)+o(1)\}.                               \tag{6}
\]
几何和及单调分部求和在0<|alpha|<=p/2上给
|vhat(alpha)|<<p/(sqrt(Y)|alpha|)，同时零频大小O(sqrt Y)。
因此带外
\[
 \sum_{|\alpha|>Q}|\widehat v(\alpha)|^2
 \ll {p^2\over YQ}\ll {p\over B_Y}=o(p).               \tag{7}
\]
由(5)的l2距离、(6)(7)及Cauchy–Schwarz控制交叉项，得到(2)。

## 4. 全部prime权能量与更宽范围

Parseval给全能量=p sum_I Lambda(n)^2/n。
高次素数幂部分用每项O(log²Y/Y)及O(sqrt Y log Y)项
界为O(Y^(-1/2)log³Y)=o(1)。
素数部分写为integral_(.70Y)^(1.30Y) (log t)/t dtheta(t)；
theta(t)=t+o(Y)，分部求和得
\[
 \sum_{n\in I}{\Lambda(n)^2\over n}
       =\log Y\log(13/7)+o(\log Y),
\]
端点的单项O(log²Y/Y)不影响，证明(1)。

证明实际上对任意B_Y趋于无穷、B_Y=o(Y)且
B_Y(1+B_Y)^2 epsilon_Y²趋于0的带宽成立。
例如B_Y=exp(kappa sqrt(log Y))、0<kappa<2c/3也满足。
这仍是p^(1/2+o(1))级带宽，却不能保留实际权的主要l2能量。

## 5. 对当前映射的作用和边界

精确支持也不能直接变短：非零多项式
sum_(n in I)w(n)z^n的次数至多floor(1.30Y)，
故它在p个不同p次单位根上至多有floor(1.30Y)个零。
充分大Y时I中有素数，因而w非零，傅里叶变换至少p-O(Y)处非零。
这一精确支持观察本身不排除近似局部化；(1)(2)才提供特定带的误差证据。

由(1)(2)，把单个w替换为只保留Omega_Q的正交Fourier投影，
其相对l2误差趋于1。335–336的prime权不能免费拥有该短频率支撑。
但是：

- 结论只针对零频附近的上述带，不声称所有平移／非连续频率集合都无用；
- 四变量F_h有相互耦合的mask、W和核；单权l2尾大不证明其最终有符号响应大；
- Pascadi/MQW允许任意系数，仍可考虑合法Vaughan分解、不同完成或直接处理长尾；
- 不排除更大带宽或以算术相消处理尾项，也不据此宣称四矩预算不可能。

这使“用实际素数权的平滑Poisson短带截断来接合现有平方根双线性定理”
失去所需的免费l2近似；它明确新增了尾项必须由真实算术处理这一接口。
第十节C仍未满足，不能以此局部经典机制审计结束整个GOAL。
