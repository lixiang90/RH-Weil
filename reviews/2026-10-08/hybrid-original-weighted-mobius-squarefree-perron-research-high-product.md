# 原平方自由归约的条件带权 Möbius 相消与 3/7 完整误差

2026-10-08，high_product_joint。研究基线 main
`a4e4c8cf3de71450325174028f0ed09dd5ef4dec`。
只新增本独立研究源，不修改冻结输入、输出、检查器或 Git。
**状态：连续条件证明，待 root 和不同作者 FULL READ 后准入。**

本稿证明平方自由 Euler 因子中真实有限带权 Möbius prefix 的统一相消，
再把它消费到原 Vaughan Type I 与全部非平方自由 Type II 子族。
在普通 zeta 的整个半平面无零前件
\([R_\theta]:\zeta(s)\ne0\) 对全部 \(\Re s>\theta\)，
\(1/2<\theta<1\)，得到
\[
 P_H=R_{\rm sf}^{(\theta)}+E_{\rm sf}^{(\theta)},\qquad
 \boxed{\mathcal M_{E_{\rm sf}^{(\theta)}}
           \ll_{\phi,\theta,\epsilon}X^{c_\theta+\epsilon},
        \quad c_\theta=1-\frac1{2\theta}.}
\tag{1}
\]
\(\theta=7/8\) 时，完整误差指数为 \(3/7\)。消费476的既有完整
\(5/7\) 增长输入后，完整第四矩传递指数为 \(9/14\)。
这是新的实际误差归约；平方自由主项仍有原零点留数 \(-m_\rho\)，
没有新的 whole 增长界、中心四阶常数预算、比例或无零边界。

## 1. 冻结输入与实际参数

本作者已 FULL READ 下列输入，包括本轮重读395、484及 reciprocal 源。
哈希只将 CRLF/lone CR 转 LF，不 trim。

| 输入 | canonical LF SHA256 |
| --- | --- |
| [395行平方自由 Euler/Perron 主源](hybrid-original-squarefree-core-euler-perron-research-perron.md) | 2f25a678b0c38c95a40469c41a757506c6f1fe64343bed327c7effe298e980c0 |
| [484原条件两个 prefix](../../notes/484-original-double-perron-conditional-remainder.md) | 38c94314687ccddf1cda08b2d7611c0e1409927b0fb62fdfb0760b32256d1cad |
| [113行 buffered reciprocal 自证](hybrid-short-mobius-twist-and-vaughan-zero-residue-research-radial.md) | a970366e68b8d3526c0dadac49b8ee8f4a7b6984e763712a851f8b6d353a291d |
| [505行固定长因子及真实 Type I](hybrid-original-extended-inner-zeta-fourth-perron-research-perron.md) | 54d39f22b370be40a780fac6fe80968e24c014fc48d1156ab87248d5310a2549 |
| [324行原 Vaughan 恒等式与低段](hybrid-original-vaughan-type-i-and-type-ii-reduction-research-radial.md) | cf58086aeb9eee63832ccd06f5499110ea236b4bd94396893757b62e75bdb9d4 |
| [476已有完整增长输入](../../notes/476-original-fourth-growth-five-sevenths-with-ivic-density.md) | 179829dd25f92ff187359f73455aafad9f957d714df13cf871db47a76e9408b6 |

395源的无条件 \(1/2\) 完整误差及其 Euler 续延仍按该源自己的审查状态
解释。本稿重证所需的新相消并独立消费，不把尚未付款的 signed 子集
当成已有函数范数的单调子域。

保持原 \(X=T/(2\pi)\)、\(L=\log X\)、\(J_T=[T/4,4T]\)、
\(a_L\ge c_\phi>0\)，以及
\[
 P_H(t)=\frac1{a_LL}\sum_{\sqrt X<p\le X}
                  \frac{\log p}{\sqrt p}p^{it},\qquad
 \|F\|_{4,T}^4=\mathcal M_F=T^{-1}\int_{J_T}|F(t)|^4dt.
\tag{2}
\]
先固定 \(0<v<1/4\)、\(\max(1/2,2v)<y<1\)，取
\[
 U=V=\lfloor X^v\rfloor,\quad H=V^2,\quad Y=X^y,
 \quad b_V(k)=\sum_{d\mid k,d\le V}\mu(d),\quad c=1/L.
\tag{3}
\]
原 \(k\) 唯一分为 \(k=s(k)r(k)\)：\(s(k)\) 是 valuation 恰为1的
素因子之积，\(r(k)\) 是 valuation 至少2的完整部分。
\(s\) squarefree、\(r\) squarefull、\((s,r)=1\)，两者允许1。
以下仍不给真实外素数 \(m\) 与 \(k\) 添加互素前件。

## 2. 带权 prefix 的 Euler 分解与绝对初线

固定 \(1/2\le\theta<1\)，先固定
\(0<\delta<(1-\theta)/4\)，令 \(\alpha=\theta-1/2+\delta>0\)。
全部本节结论统一于
\[
 w=1/2+c-i\tau,\qquad T/8\le\tau\le33T/8,
 \qquad r\le H,\quad r\ {\rm squarefull},\quad1\le x\le V.
\]
定义实际系数与实际 sharp prefix
\[
 d_{r,w}(a)=1_{a\ {\rm squarefree},\,(a,r)=1}\mu(a)
                     \prod_{p\mid a}(1+p^{-w})^{-1},
 \quad S_{r,w}(x)=\sum_{a\le x}d_{r,w}(a)a^{-w}.
\tag{4}
\]
它包含原复局部因子，不能先删除这些因子再援引普通 Möbius 相消。
在 \(\Re z>1\) 绝对收敛的真实 Dirichlet 级数是
\[
 H_r(z,w)=\sum_{a\ge1}d_{r,w}(a)a^{-z}
          =\prod_{p\nmid r}\left(1-\frac{p^{-z}}{1+p^{-w}}\right)
          =\frac{K_r(z,w)}{\zeta(z)},
\tag{5}
\]
其中逐素数的准确比值给
\[
 K_r(z,w)=
 \prod_{p\nmid r}\left(1+
       \frac{p^{-z-w}}{(1+p^{-w})(1-p^{-z})}\right)
 \prod_{p\mid r}(1-p^{-z})^{-1}.
\tag{6}
\]
对 \(\Re z\ge\theta+\delta\)，两个分母分别至少为
\(1-2^{-1/2}\)、\(1-2^{-\theta-\delta}\)。第一个无限产品的增量为
\(O_\delta(p^{-\Re z-\Re w})\)，且
\(\Re z+\Re w\ge1+\delta+c\)。因此它局部一致绝对收敛，解析，
模统一有界；常数可依赖固定 \(\theta,\delta\)，不依赖 \(\tau,r,T\)。
不需要这些局部因子无零，也不对该无限产品取 reciprocal。

有限的去 \(r\) 因子满足任意先固定 \(\eta>0\) 的界
\[
 \prod_{p\mid r}|1-p^{-z}|^{-1}
 \le\prod_{p\mid r}(1-p^{-1/2})^{-1}\ll_\eta r^\eta.
\tag{7}
\]
对足够大素数用 \(-\log(1-p^{-1/2})\le\eta\log p\)，
有限小素数的费用并入常数。因此 \(|K_r(z,w)|\ll_{\delta,\eta}r^\eta\)。
同样证明 \(|d_{r,w}(a)|\ll_\eta a^\eta\)，但这个界只用于有限近端区。

Perron 初线需要的完整绝对级数有更精确的界：
\[
 \begin{split}
 \sum_{a\ge1}|d_{r,w}(a)|a^{-1-c}
 &=\prod_{p\nmid r}\left(1+
                     \frac{p^{-1-c}}{|1+p^{-w}|}\right)\\
 &\le\prod_p\left(1+\frac{p^{-1-c}}{1-p^{-1/2}}\right)
 \ll\zeta(1+c)\ll L.
 \end{split}
\tag{8}
\]
最后一步：对数至多 \(\sum_p p^{-1-c}\) 加
\(\sum_p p^{-1-c}p^{-1/2}/(1-p^{-1/2})=O(1)\)，
前者至多 \(\log\zeta(1+c)\)。这支付全部无限系数；
不能将 \(a^\eta\) 插到 \(a^{-1-c}\) 中后声称远尾收敛。

## 3. 保留半整数端点的内部 Perron

对 \(x\ge2\) 令 \(x^\sharp=\lfloor x\rfloor+1/2\)。
它严格保持 \(a\le x\) 的整数集合。取内部高度 \(K=T/32\) 和
相对初线 \(\kappa=1/2\)，于是 \(\Re(w+\kappa)=1+c\)。
逐系数截断 Perron 给
\[
 S_{r,w}(x)=\frac1{2\pi i}\int_{\kappa-iK}^{\kappa+iK}
           H_r(w+\xi,w)\frac{(x^\sharp)^\xi}{\xi}\,d\xi
       +\mathcal E_{r,w}(x),
\tag{9}
\]
其中误差的正上界为
\[
 \sum_{a\ge1}|d_{r,w}(a)|a^{-1/2-c}(x^\sharp/a)^{1/2}
       \min\{1,[K|\log(x^\sharp/a)|]^{-1}\}.
\tag{10}
\]
在 \(a\le x^\sharp/2\) 或 \(a\ge2x^\sharp\)，(8)直接给
\(O(\sqrt{x^\sharp}K^{-1}L)\)。远端是完整无限级数，未截到 \(V\)。
在 \(x^\sharp/2<a<2x^\sharp\) 才用 \(|d_{r,w}(a)|\ll_\eta a^\eta\)。
半整数距离至少 \(1/2\)，并且
\(|\log(x^\sharp/a)|\gg|a-x^\sharp|/x^\sharp\)。harmonic 求和给
\[
 |\mathcal E_{r,w}(x)|\ll_\eta
       x^{1/2+\eta}T^{-1}\log(2x)+\sqrt x\,T^{-1}L.
\tag{11}
\]
最邻近项也已包含在这个和内；\(x\le X^v\ll T\)。

113源§2在 \([R_\theta]\) 下已逐圆盘自证
\[
 |\zeta(\sigma+ih)^{-1}|
        \ll_{\theta,\delta,\rho}(1+|h|)^\rho,
             \qquad\sigma\ge\theta+\delta.
\tag{12}
\]
这是全高度、有固定 buffer 的 reciprocal，不是普通 Lindelöf 前件。
将(9)矩形左线移到
\(\lambda=\theta+\delta-1/2-c=\alpha-c>0\)，
大 \(T\) 时它小于 \(\kappa\)。全矩形 \(\Re(w+\xi)\ge\theta+\delta\)。
内部真实绝对高度范围为 \([3T/32,133T/32]\)，由(12)的全高度量词支付，
不把它偷换为较窄的外 Perron guard。

\(1/\zeta\) 在 \(z=1\) 取零；在 \([R_\theta]\) 的这个矩形无极点。
(6)解析，核 \(\xi=0\) 没有跨过。因而此次内部移线没有任何留数。
左线由(6)、(7)、(12)和 \(\int|d\xi/\xi|\ll_\delta\log T\) 给
\(O(r^\eta x^\alpha T^\rho L)\)。两个水平段的 \(|\xi|\asymp T\)，
长度有界且 \((x^\sharp)^{\Re\xi}\ll\sqrt x\)，故总费用为
\(O(r^\eta\sqrt x\,T^{-1+\rho})\)。
在(11)选足够小 \(\eta\)，将 \(x^\eta\) 吸到任意预定的小 \(T^\rho\)，
并分配各处小损失，得到真实统一接口
\[
 \boxed{|S_{r,w}(x)|\ll_{\theta,\delta,\eta,\rho}
   r^\eta\{x^{\theta-1/2+\delta}T^\rho
                 +\sqrt x\,T^{-1+\rho}\}L^C.}
\tag{13}
\]
\(1\le x<2\) 直接处理，右边第一项至少为固定正量。
端点项对所有 \(x\le V\) 是真负幂
\(O(T^{-1+v/2+\rho})\)。\(\theta=1/2\) 也可使用(13)，但必须保留
\(\delta>0\) 才有绝对 Euler 收敛和正的相对移线。

## 4. 原有限 squarefull Euler 因子的共同消费

395源(6)的精确有限因子保持
\[
 F_{V,r}(w)=\prod_{p\mid r}(1+p^{-w})^{-1}
       \sum_{\substack{e\mid\operatorname{rad}(r)\\e\le V}}
                      \mu(e)S_{r,w}(V/e).
\tag{14}
\]
没有另添 \(e^{-w}\)，没有将 \(ae\le V\) 换成独立矩形。
利用(7)同类有限局部界和(13)，逐个真实 \(e\) 求和得到
\[
 |F_{V,r}(w)|\ll r^{2\eta}\tau(r)
              \{V^\alpha T^\rho+\sqrt V\,T^{-1+\rho}\}L^C.
\tag{15}
\]
这里 \((V/e)^\alpha\le V^\alpha\)，\(e\) 的数量至多 \(\tau(r)\)。

定义原有限 \(C_{\ge2}(w)=\sum_{2\le r\le H,\,r\ {\rm squarefull}}
r^{-w}F_{V,r}(w)\)。每个 squarefull 整数唯一写成 \(r=a^2b^3\)，
\(b\) squarefree，因此其每个 dyad 的 \(\sum r^{-1/2}=O(1)\)，
全部 \(r\le H\) 的和为 \(O(\log(2H))\)。
因 \(H\le X\)，将 \(r^{2\eta}\tau(r)\) 与所有固定对数分配到
任意最终 \(X^\epsilon\) 后，(15)给
\[
 \boxed{|C_{\ge2}(1/2+c-i\tau)|
        \ll_{\theta,\delta,\epsilon,\rho}
        X^\epsilon\{V^\alpha T^\rho
                       +\sqrt V\,T^{-1+\rho}\}L^C.}
\tag{16}
\]
第一项支配负幂端点。它统一覆盖全部 \(2\le r\le H\)、全部真实
divisors、全部外移位 \(\tau\)，没有使用不同 \(r\) 的 signed 相消。
这个条件界只声明在所需左线 \(\Re w=1/2+c\)。外 Perron 的水平段仍用
395源§3的无条件 \(\sqrt V X^\epsilon L^C\)，不用未证明的更右实部版本。

## 5. 原 Type I 与 log 项的共同乘积截断

置 \(F_{\Lambda,U}(w)=\sum_{m\le U}\Lambda(m)m^{-w}\)、
\(G_V(w)=\sum_{d\le V}\mu(d)d^{-w}\)。484完整两内部 prefix 和 Abel 给
\[
 |F_{\Lambda,U}(1/2+c-i\tau)|+|G_V(1/2+c-i\tau)|
                       \ll U^\alpha T^\rho L^C.
\tag{17}
\]
这里 \(U=V\)。\(\Lambda\) prefix 的主极点项 \(O(\sqrt U/T)\)
和 \(O(\sqrt U\,T^{-2}L^C)\) 端点项均是真负幂。
genuine-prime prefix由完整 proper-power 差另付 \(O(L^2)\)，故
\(|F_U^{\rm prime}(w)|\ll U^\alpha T^\rho L^C\)。
这一步保留真实 \(\mu\)、\(\Lambda\) 系数。

原 Type I 的 coefficient \(g_{U,V}\) 恰有有限级数身份
\[
 \Gamma_{U,V}(w)=\sum_d g_{U,V}(d)d^{-w}
                  =-F_{\Lambda,U}(w)G_V(w).
\tag{18}
\]
故在真实左线 \(|\Gamma_{U,V}|\ll(UV)^\alpha T^{2\rho}L^C\)。
采用505源的同一 \(N=\lfloor10T\rfloor\) 长有限因子 \(W_N\)，
先对 \(\Gamma_{U,V}W_N\) 作外 Perron 的两个半整数端点恢复
\(Y<dn\le X\)，再消费(18)。全部额外 \(dn>X\) 由505源§3、§4的
完整有限系数初线误差支付；支持最多 \(UVN\ll X^{1+2v}<X^2\)。
外高度仍 \(T/8\)，共享移位 \(t-\omega\) 始终在(17)的 guard。
505源 \(W_N\) 第四均值及同一核的 \(L^1\) 对数界给
\[
 \mathcal M_{I_2}\ll X^{8\alpha v+\epsilon}T^{8\rho},
 \qquad \mathcal M_{I_3}\ll X^{4\alpha v+\epsilon}T^{4\rho}.
\tag{19}
\]
\(I_3\) 是原 \(G_VW_{\log,N}\) 项；使用505源的 log 长因子均值。
这两个有限 products 的外 Perron 直接在 \(c+i\omega\) 上，不需要
移线或水平段。505源(15)的全部有限系数负幂误差保持有效。
不通过 \(\Gamma\) 的 divisor 绝对质量丢弃(18)的两因子相消。

## 6. 完整非平方自由 Type II 的真实付款

保留395源逐素数验证的两个实际生成函数：
\[
 \mathcal H_{\ge2}(w)=
 \frac{[\zeta'(w)+(Q_{\rm pp}(w)+F_U^{\rm prime}(w))\zeta(w)]
          C_{\ge2}(w)}{a_LL\zeta(2w)},
\tag{20}
\]
\[
 \mathcal H_{\rm pp}(w)=
      -\frac{Q_{>U}(w)(\zeta(w)G_V(w)-1)}{a_LL}.
\tag{21}
\]
它们在 \(\Re w>1\) 是原全部 genuine-prime \(m>U\)、
\(2\le r(k)\le H\) 族，及原全部 proper-power \(m>U\)、\(k>V\) 族
的准确无限 Dirichlet 系数。\(Q_{\rm pp}\) 和 \(Q_{>U}\) 保留完整
infinite proper powers，\(|Q|\ll L^2\)；\(|1/\zeta(2w)|\ll L\)
在 \(\Re w\ge1/2+c\) 是无条件绝对 Euler 界。

外 Perron 完整沿用395源§5—§7：两个半整数端点、初线全部
\(n\ge1\) 系数和、以及 \(n>X\) 的无限远尾均付款。
远尾使用 \(\sum\tau_3(n)\log(2n)n^{-1-c}\ll L^4\)，
不使用发散的 \(n^{-1-c+\eta}\)。移到 \(\Re w=1/2+c\) 时，
(20)准确消掉 \(\zeta'/\zeta\) 的零点极点；(21)本就没有该 reciprocal。
\(\zeta\) 在1的 pole不在正高度 guard 中，核原点没有跨过。
有限局部因子、proper-power 系列和 \(1/\zeta(2w)\) 在矩形解析。
因此没有漏掉未知普通零点留数。

所有外水平段用395源的无条件绝对有限因子界，以及
\(|\zeta|\ll T^{\max(1-\sigma,0)}L\)、
\(|\zeta'|\ll T^{\max(1-\sigma,0)}L^2\)，总费用
\(O(X^{-1/2+v+\epsilon}L^C)\) 仍是真负幂。
条件(16)、(17)只在外左线消费。505和395已验证的同一实部
\(\zeta\)、\(\zeta'\) 自身第四均值为 \(O(L^4)\)、\(O(L^8)\)，
统一于共享 \(|\omega|\le T/8\)，而不是 \(|\zeta\zeta'|^2\) 的均值。

将(16)、(17)置于同一 \(w=1/2+c-i(t-\omega)\)，再一次共享核的
normalized \(L^4\) Minkowski，得到两个 signed 实际族自身的费用
\[
 \mathcal M_{Q_{\ge2}}\ll X^{8\alpha v+\epsilon}T^{8\rho},
 \qquad \mathcal M_{Q_{\rm pp}^{\rm full}}
                  \ll X^{4\alpha v+\epsilon}T^{4\rho}.
\tag{22}
\]
第一项来自 \((UV)^\alpha\) 的点值因子：
\(\zeta'C_{\ge2}\) 只需 \(V^\alpha\)，
\(F_U^{\rm prime}\zeta C_{\ge2}\) 需要 \((UV)^\alpha\)。
所有 \(m,k,r,s\)、aspect ratios、共同 \(Y<mk\le X\) 均保留。

## 7. 完整新账本与合法参数优化

原 Type II 精确不交分成
\[
 C_4=Q_{\rm pp}^{\rm full}+Q_{>H}^{\rm prime}+Q_{\ge2}
                                      +R_{\rm sf}^{(v,y)},
\tag{23}
\]
其中准确未付主项为
\[
 \boxed{R_{\rm sf}^{(v,y)}(t)=-\frac1{a_LL}
 \sum_{\substack{m>U\ {\rm prime},\ k>V\ {\rm squarefree}\\Y<mk\le X}}
       \frac{\Lambda(m)b_V(k)}{\sqrt{mk}}(mk)^{it}.}
\tag{24}
\]
\(m\mid k\) 也保留。\(Q_{>H}^{\rm prime}\) 的完整原平方丰满尾
按395源§8所绑定的401源直接证明，允许 \(M_0=U\)，费用
\(X^\epsilon(1+X/H^2)\ll X^{1-4v+\epsilon}\)。
原 scalar proper-power 迁移的绝对费用仍仅 polylog；原低段保持
\(\sqrt X< n\le Y\)，由实际平方多项式二矩给 \(X^{2y-1+\epsilon}\)。
它们不需要条件无零输入。

置 \(\beta=2\theta-1\)。为任意最终 \(\epsilon>0\)，先选足够小的
\(\delta,\rho,\eta\)，把(19)、(22)的 \(\delta v\)、\(\rho\)、divisor
和对数损失分配到 \(\epsilon\)。于是 Type I 和小 squarefull 族的
第四矩费用为 \(4\beta v\)，log项及全部 proper-power 族为
\(2\beta v\)。合成完整 \(E_{\rm sf}=P_H-R_{\rm sf}^{(v,y)}\) 后，
一次 \(L^4\) Minkowski 得
\[
 \mathcal M_{E_{\rm sf}}\ll X^{C(\theta,v,y)+\epsilon},\qquad
 C(\theta,v,y)=\max\{2y-1,4\beta v,1-4v,0\}.
\tag{25}
\]
\(\beta\ge0\)，所以 \(2\beta v\) 已被 \(4\beta v\) 支配。

对 \(1/2<\theta<1\)，取
\[
 \boxed{v=\frac1{8\theta},\qquad y=1-\frac1{4\theta},
               \quad H=V^2.}
\tag{26}
\]
严格有 \(0<v<1/4\)、\(1/2<y<1\)，并且
\(y-2v=1-1/(2\theta)>0\)，所以原共同高段合同 \(UV<Y\) 有幂级余量。
三项 \(2y-1\)、\(4\beta v\)、\(1-4v\) 全等于
\(c_\theta=1-1/(2\theta)\)，证明(1)。全部 floors 用
\(V\ge X^v/2\)、\(H\ge X^{2v}/4\) 支付。
由于 \(\max\{4\beta v,1-4v\}\ge c_\theta\)，这是当前费用族的
最优值；不声称所有 prime/Möbius 算术方法的最优性。
\(\theta=1/2\) 的(13)成立，但(26)会取到不合法端点
\(v=1/4,y=1/2\)，本稿不把该端点当成已达成的零指数结论。

\(\theta=7/8\) 的实际参数与各完整费用是
\[
 U=V=\lfloor X^{1/7}\rfloor,\quad H=V^2,\quad Y=X^{5/7},
\]
\[
 (2y-1,4\beta v,2\beta v,1-4v,0)
                  =(3/7,3/7,3/14,3/7,0).
\tag{27}
\]
故 \(\mathcal M_{E_{\rm sf}^{(7/8)}}\ll X^{3/7+\epsilon}\)。
新的 \(V,Y\) 改变了(24)的实际主项；不能将它当成395或486主项的
signed 子集并搬用旧范数。

## 8. 完整矩传递与仍开放的零点包

仅在本节消费476的原 \([R_{7/8}]\) 与已交付的完整
\(\mathcal M_{P_H}\ll X^{5/7+\epsilon}\)。先由
\(R_{\rm sf}=P_H-E_{\rm sf}\) 得完整新余项的同幂界，再用
\[
 |\mathcal M_{P_H}-\mathcal M_{R_{\rm sf}}|
 \ll\|E_{\rm sf}\|_{4,T}
               (\|P_H\|_{4,T}+\|R_{\rm sf}\|_{4,T})^3.
\]
严格得到
\[
 \boxed{\mathcal M_{P_H}=\mathcal M_{R_{\rm sf}^{(7/8)}}
                   +O_{\phi,\epsilon}(X^{9/14+\epsilon}),
           \qquad\frac{3(5/7)+3/7}{4}=\frac9{14}.}
\tag{28}
\]
传递相对原 \(5/7\) 有 \(1/14\) 的指数余量。
相对395无条件误差 \(1/2\)、传递 \(37/56\)，条件版本分别节省
\(1/14\)、\(1/56\)。相对486的 \(9/17\)、\(159/238\)，分别节省
\(12/119\)、\(3/119\)。这些比较均针对完整函数的误差和传递，
不把不同实际主项当成同一 signed 子域。

平方自由实际生成函数仍准确为
\[
 B_{\rm sf}(w)=\frac{\zeta(w)}{\zeta(2w)}F_{V,1}(w)-1.
\tag{29}
\]
在每个 \(\Re\rho>1/2\) 的 zeta 零点处，有限 \(F_{V,1}\) 和
\(1/\zeta(2w)\) 解析，故 \(B_{\rm sf}(\rho)=-1\)。外 prime 因子
\(A_U=-\zeta'/\zeta-Q_{\rm pp}-F_U^{\rm prime}\) 的留数为
\(-m_\rho\)，因此
\[
 \operatorname{Res}_{w=\rho}[-A_U(w)B_{\rm sf}(w)]=-m_\rho.
\tag{30}
\]
两半整数端点核仍给原 \(-m_\rho K_{X,Y}(\rho-s_0)\)，没有新减幅。
条件带权 prefix 付掉的是非平方自由误差，不能据此删除平方自由零点包。
\(3/7\) 误差仍增长，不是常数级 \(o(1)\)；完整主项仍仅继承既有
\(5/7\) 界。真正开放的是(24)全部 genuine-prime/squarefree mixed4
及其常数预算。本稿没有有限采样，也不从有理指数运算认证无限估计。
项目既有零点比例、已引用无零区域和 whole 增长基线均不由本稿更新。
