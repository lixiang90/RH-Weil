# 稀疏上端Cauchy谱：密度、比例与二阶输入的严格能力审查

2026-10-08，root。研究轮5，基线 main 84670bc。
状态：抽象谱模型的解析证明，待不同作者全文审查。
不修改旧来源、检查器或Git，不宣称模型是ζ零点或真实素数函数。

本稿构造满足所用条带、临界线比例下界、局部零数、密度及全包二阶
polylog条件的谱族，其原形状四矩仍达到既有密度费用的幂。
这证明这些抽象数据本身不足以推出新的四矩省幂；
真实Euler乘积、实际有限素数系数和算术相位关系没有被该模型包含。
不能据此否定ζ可能具有更好的实际四矩或新的无零区域。

## 1. 与真实合同的比较范围

本轮全文回读[494](../../notes/494-original-double-deviation-and-upper-cauchy-core.md)、
[纯上端源](hybrid-original-squarefree-upper-cauchy-packet-research-perron.md)及其输入。
用的是以下已冻结形状，不把它的实际算术结论转移给模型：

| 来源 | canonical LF SHA256 |
| --- | --- |
| [189行纯上端源](hybrid-original-squarefree-upper-cauchy-packet-research-perron.md) | f53579b62f4a47418644109893afc3de1c6dd6124e361ec713bbf0003403df43 |
| [453行固定包及全包二阶](hybrid-original-squarefree-signed-zero-gram-research-perron.md) | 0b126138c7bf42e9be3c4352b099a6ab37d88cef93af20593593c8e849aa2a17 |
| [184行全密度包络](hybrid-ivic-density-and-scalar-fourth-growth-research-twisted.md) | a21a19e7bd09892ed705fa7883143e49c138ffe112c561be9413edaf44d72a1d |
| [188行原ν合同](hybrid-original-squarefree-carrier-fourth-near-research-perron.md) | 2142645eed724da49a3e6faae7068adb2c8ca907c196a691f09a2b7a7fd6f3ae |

固定 \(5/6<\theta\le7/8\)，令
\[
 a=\theta-\tfrac12,\quad b=n_I(\theta)=\frac{3(1-\theta)}{2\theta},
 \quad y=1-\frac1{4\theta},\quad X=T/(2\pi),\quad L=\log X.
 \tag{1}
\]
取 \(N_L\asymp_\phi L\)、\(x=\lfloor X\rfloor+1/2\)、
\(z_0=\lfloor X^y\rfloor+1/2\)、\(J=[T/4,4T]\)。
所有模型随T成族；它们不是一个已构造算术函数的真实零点。

## 2. 稀疏高实部数据与简单临界线背景

令 \(K=\lfloor T^b\rfloor\)，在 \([13T/10,17T/10]\) 等距放置
K个高数据点 \(\rho_j=\theta-i\gamma_j\)，相邻间距 \(H\asymp T/K\)。
每个数据点重数1，添加反射 \(1-\theta-i\gamma_j\)，
并在整个抽象谱中添加它们的共轭高度。
其零点实部均不超过θ；两个反射点是不同的简单点。

用 \(\eta=2\pi/L\) 的单一lattice \(\gamma=\eta(k+\alpha)\) 添加
实部1/2的简单背景，取原固定高度区间
\(h_0\in[T/32,T/16]\)、\(h_1\in[5T,6T]\) 中的连续整数k。
可将h0、h1选在lattice间隙中；高数据点远离这两端。
背景数 \(N_0\asymp TL\)。共轭与反射不破坏局部计数：
每单位高度窗口有 \(O(L)\) 个点，稀疏点间距趋于无穷。

临界线简单点比例为
\[
 \frac{N_0}{N_0+2K}\longrightarrow1.
 \tag{2}
\]
因此任何固定 \(\kappa<1\) 的临界线比例下界（包括当前比较值）均相容。
这不是断言真实比例为1；模型的有限高度背景也未满足已核的精确ζ计数公式。

对 \(1/2<\sigma\le\theta\)，高点数 \(O(K)\)，184的各段
密度指数均至少b：低两段最小值3/7，Ivić段单调递减至b≤3/10。
所以同一固定σ的密度上界 \(O_\epsilon(T^{n(\sigma)+\epsilon})\) 全部满足。
σ=1/2处总数 \(O(TL)\)；σ>θ无点。
这里核验的是这些上界，未声称真实ζ密度达到模型规模。

## 3. 分离峰的两阶与四阶范数

模型纯上端包为
\[
 C(t)=-\frac{e^{it\log x}}{N_L}
   \sum_{j=1}^K\frac{x^a e^{-i\gamma_j\log x}}{a+i(t-\gamma_j)}.
 \tag{3}
\]
正实部a在固定紧区间，原上端相位完全保留。
记 \(A=x^a/N_L\)。下面的界甚至对任意模1系数相位均成立。

对每个t选最近的 \(\gamma_j\)，其余项绝对值和至多
\[
 C A H^{-1}\log(2K).
 \tag{4}
\]
因为等距点到t的其余距离按H的倍数增长。
最近项的p次方在整个实轴积分为 \(O_p(A^p)\)，\(p=2,4\)；
各Voronoi区间上使用 \((u+v)^p\le2^{p-1}(u^p+v^p)\)，得到
\[
 \frac1T\int_J|C|^p\ll_p\frac{KA^p}{T}
                         +A^p H^{-p}\log^p(2K)
                         \ll_p\frac{KA^p}{T}.
 \tag{5}
\]
最后一步用 \(H\asymp T/K\)、\(K/T\to0\)。
在互不相交的 \(|t-\gamma_j|\le1\) 内，自己的一项大小至少cA，
其余项由(4)为o(A)。这些区间均在J的固定内部，故亦有反向界。
所以严格地
\[
 \boxed{\frac1T\int_J|C|^2\asymp\frac{Kx^{2a}}{TN_L^2},
 \qquad
 \frac1T\int_J|C|^4\asymp\frac{Kx^{4a}}{TN_L^4}.}
 \tag{6}
\]
原ν在上述内部区间为T^(-1)量级、全支撑内上界 \(O(T^{-1})\)，
同一最近点证明也给原ν两阶、四阶的相同量级。
无需删交叉项或假设随机相位；大间距已经使峰值的相消不足。

相应指数为
\[
 2a-1+b=2\theta-2+n_I(\theta)
       =\frac{(4\theta-3)(\theta-1)}{2\theta}<0,
 \tag{7}
\]
\[
 4a-1+b=B_I(\theta)=4\theta-3+n_I(\theta).
 \tag{8}
\]
名义θ=7/8给模型二阶 \(T^{-1/28}/L^2\)，
四阶 \(T^{5/7}/L^4\)。二阶很小与四阶达到当前幂同时成立。

## 4. 全entire包二阶条件亦相容

定义模型全包Z为453的同一两端entire核之和：
\[
 Z(t)=-N_L^{-1}\sum_{\substack{\rho=\beta-i\gamma\ {\rm in\ model}\\
                              h_0<\gamma<h_1}}
       \frac{x^{\beta-1/2+i(t-\gamma)}
                    -z_0^{\beta-1/2+i(t-\gamma)}}{\beta-1/2+i(t-\gamma)}.
\]
分母零处取entire延拓；包内包括上述背景、高点及反射低点，
符号、重数和共同x、z0均保留。添加的共轭高度仅用于谱的对称性，
不把它们额外加入这个固定负绝对高度包。
临界线背景的Fourier和 \(S_0(u)=\sum_k e^{-i\eta(k+\alpha)u}\)
满足平方绝对值的周期L，且
\[
 \int_c^{c+L}|S_0(u)|^2du=LN_0.
 \tag{9}
\]
因为 \(|[\log z_0,\log x]|<L\)，entire核表示及完整实轴Plancherel给
\[
 \frac1T\int_J|Z_0|^2
 \le\frac{2\pi}{TN_L^2}
          \int_{\log z_0}^{\log x}|S_0(u)|^2du
 \ll1.
 \tag{10}
\]
这里用正上界；没有将J与整个实轴互换为相等。
局部计数与两端核的 \(L/(1+L|t-\gamma|)\) 包络还给
\(\sup_J|Z_0|\ll L\)，所以其四矩仅为polylog。

高点下端用(5)将A换成 \(z_0^a/N_L\)，
反射低点两单端用同一分离峰界将A换成 \(x^{-a}/N_L\)、
\(z_0^{-a}/N_L\)；其实部分母为−a，不为零，模长界相同。
故高、低整个entire稀疏包的二阶不大于(6)的量级，趋于零。
由完整L²三角不等式，模型全包满足
\[
 \boxed{T^{-1}\int_J|Z|^2\ll1.}
 \tag{11}
\]
同样可单向运输到原ν；这匹配全包signed二阶条件，未用子包范数单调。

高点Y端四阶相对(6)小因子 \((z_0/x)^{4a}\to0\)，
反射低点更小，背景为polylog。
完整L⁴三角不等式的上下界于是给
\[
 \boxed{T^{-1}\int_J|Z|^4\asymp
          T^{B_I(\theta)}/L^4,}
 \tag{12}
\]
原ν版本亦然。这里没有把模型CX替换成真实R或真实零点包。

## 5. 对下一步研究的作用

对任何固定δ>0，取ε<δ，(6)、(12)排除仅由上述抽象输入
统一推出 \(T^{B_I(\theta)-\delta+\epsilon}\) 的四矩上界。
临界线比例下界、无零条带、所用密度、局部计数、正实部Cauchy形状，
甚至全包signed二阶polylog，均没有排除这一模型。

这比“密度上界的费用可能大”更强：在明确的抽象类中，实际范数确有该幂。
但类中没有真实ζ的Euler乘积、精确零点计数余项、实际有限素数系数、
Perron全纯修正或Hecke全族算术输入。
故它不否定利用这些额外关系证明真正省幂，也不证明真实ζ有任何离线零点。
尤其不能以模型为依据撤销451的引用边界或已准入的比例结果。

下一项必须使用能排除稀疏高峰配置的真实算术四阶关系，
或严格加强相应实际高实部零点计数；继续仅优化Hilbert叠加、二阶范数
或一般局部计数的日志，不会由这一组抽象条件自动改进完整目标。
没有新的实际whole、中心常数、零点比例或无零边界。
