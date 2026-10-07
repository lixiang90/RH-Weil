# 数域选择定量逆审：相对放大收益、共同 detector 与 CM 完成

2026-10-07。作者：radial_review。只新增本报告；固定 math、旧论文、旧研究稿、
脚本及输出均只读。本报告独立复核数域报告及 457 全文，并核对实际 source
12362–12460、12531–12600 与 451 的 critical 参数；不以单个放大指数冒充
whole marked/plain 合同、无零边界或 RH/RR 证明。

**限定 PASS：**457 最终全文在所声明的相对/候选范围内通过。相对
order-\(d\) 放大引理的数学推导通过，但前件必须包括
“对每个固定 \(c>0\)”的 raw row-scale supremum 与同族自然零、注入计数及
profile/height uniformity。四次对六次在当前长分支的条件收益是
\(0.010352262232\ldots\)，在原 detector cutoff 下总 count 收益为零。
下文额外保留原 short 合同并重平衡的反事实预算给
\(0.002993619561\ldots\) 的 count 收益；它也不是新 \(\sigma\)。
CM 次数不改变 conductor 的 \(1/2-s\) 指数。换域尚未付完整新源。

## 1. 证据绑定、版本与审查范围

本轮实读：

- [固定 math source](E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)，
  commit adc7f1241b42e322a6451854ab7e4b4c146bf78a，canonical LF SHA256
  42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3。
- [数域主研究报告](hybrid-number-field-choice-review.md)，canonical LF SHA256
  47453b09c0491a201ef39667a123d046c39ed2e2df906c866f101b0796a443bb，
  17196 UTF-8 bytes、335 行；实审其中 §2–§9，特别 §7 的全部前件。
- [457](../../notes/457-number-field-choice-and-relative-amplification.md)：
  canonical LF SHA256
  75079970955602644a9290709f66e2be331ad6116d2a637ed8fc97fb0dde5791，
  15254 UTF-8 bytes、327 行。全文逐项读；(3)–(11) 是本报告主要数学
  审核对象，最终新增 (2a)–(2c) 的 v5 更正、split/inert 与 CRT 也逐项核对。
- [451](../../notes/451-kappa-feedback-cubic-boundary-and-family-continuation.md)，
  canonical LF SHA256
  17ce7fea8c881ebd4034657b7039e99897d4ff9532348993ba329c46e3c4d487。
  此处仅调用其已明确 [R] 范围的参数及 count 定义，不重证底层分析。

外部使用 primary sources：DDHL 的 **v5，2026-01-30**，而不是缺补因子的
v3；Watkins §3.6 的普通 Hecke completion；BGL Theorem 1.3 的实际大筛宽度。
原 source 的 cubic-theta completed reflection 与普通 Hecke completion
在下文始终分别处理。没有编译 math，没有运行或覆写冻结脚本/JSON。

## 2. \(e_d(r)\) 的完整相对命题与量词

这里 \(d\) 是 character/放大次数；**不是数域次数 \([K:\mathbf Q]\)**。
固定数域 \(K\)、整数 \(d\ge2\)、有限坏素数集 \(S\)，将 \(n,u,a\) 看作
\(S\) 外的 integral ideals，或者已经合法选定的 element representatives。
令 \(u\) 为 \(d\)-free row，即所有 good-prime valuations 在 \(0,\ldots,d-1\)。
对同一个零扩张 family 假设

\[
 \psi_{u a^d}(n)=\psi_u(n)1_{(n,a)=1},
 \qquad
 M_u(D;W)=\sum_{n\ {\rm sf}}\frac{\mu_K(n)\psi_u(n)}{\sqrt{Nn}}W(Nn/D).
 \tag{1}
\]

需要以下实际前件，而非仅某个抽象 character 的存在：

1. 对每个固定 \(c>0\)、每个所需的小损失指数 \(\varepsilon>0\)，有
   \[
   \sum_{Nv\le C H}\sup_{0<D'\le D}|M_v(D';W)|^2
   \ll_{K,S,c,\varepsilon,W}H(HD)^\varepsilon,
   \qquad H\ge\max(2,D^{1+c}).
   \tag{2}
   \]
   此 raw family 包含放大后的 \(v\)，包括其非 primitive 元及全部自然零。
   若 \(W\) 随 row 的 \(\sigma,\omega\) 等参数移动，(2) 必须对原 profiles
   和固定 height 范围统一成立，并显示所需的 seminorm/height 费用。
2. \(Na\le P\) 的 eligible multipliers 至少 \(c_{K,S}P\) 个；有
   \(N(u a^d)=Nu(Na)^d\)，且实际 indexing 下 \((u,a)\mapsto u a^d\) 注入。
   不是把所有 norm-bounded elements 直接计数。理想版本的注入来自
   \(v_{\mathfrak p}(v)\bmod d\) 恢复 \(u\)，再整除恢复 \(a\)。
3. 平方自由 divisor 分解、同一 \(W\) 的缩放以及 (1) 的自然零都在 (2)
   的 family 中。元素版本还须处理 unit/class/representative cocycles。
   原 column 的 Möbius 系数及 \(1/\sqrt{Nn}\) 归一化不可换成任意列。

这些正是 source12391–12455 的准入，在 \(d=6\) 的原源已有 [R]；本轮未给
Gaussian \(d=4\) 证明它们。一个 fixed-scale moment 不是 (2)；
source12391–12408 还通过 scale derivative 与 Sobolev 支付 supremum。

取
\[
 H=\max(2U,D^{1+c}),\qquad P=(H/U)^{1/d}.
 \tag{3}
\]
对每个 \(a\)，在平方自由 \(n\) 中唯一分解
\(n=bm,\ b\mid\operatorname{rad}(a),\ (m,a)=1\)。由 (1) 得精确恒等式
\[
 M_u(D;W)=
 \sum_{b\mid\operatorname{rad}(a)}
 \frac{\mu_K(b)\psi_u(b)}{\sqrt{Nb}}
 M_{u a^d}(D/Nb;W).
 \tag{4}
\]
无需 \((u,a)=1\)：与 \(u\) 相交的自然零仍在两边。\(b\) 与 \(m\) 的互素、
平方自由及其符号来自这次精确分解，未删去某个非互素项。

系数绝对值和至多 \(\tau_K(a)\ll_{K,\varepsilon}(Na)^\varepsilon\)，故调整
任意小损失指数后
\[
 |M_u(D;W)|^2\ll P^\varepsilon
 \sup_{D'\le D}|M_{u a^d}(D';W)|^2.
 \tag{5}
\]
这也说明 457(8) 的 \(P^\varepsilon\) 是重新选择小指数后的 bound，并非
将一次 divisor bound 的同一个 \(\varepsilon\) 原封不动用于平方。
平均 \(a\) 后求和 \(Nu\asymp U\)，注入使每个 \(v\) 只计一次，\(Nv\ll H\)。
由 (2) 即得
\[
 \sum_{Nu\asymp U}|M_u(D;W)|^2
 \ll \frac HP(UD)^\varepsilon
 =U^{1/d}H^{1-1/d}(UD)^\varepsilon.
 \tag{6}
\]
固定有界 \(0\le r\le r_{\max}\)、\(D=U^r\)，首先得到
\[
 e_{d,c}(r)=\max\!\left\{1,\frac{1+(d-1)(1+c)r}{d}\right\}.
 \tag{7}
\]
对最终任意损失 \(\varepsilon_{\rm out}\)，先选
\((1-1/d)c r_{\max}<\varepsilon_{\rm out}/2\)，再选 raw/divisor 的小指数，
最后增大 \(U\)。固定域、坏集、所有 height/seminorm 阶数先固定。
因此可以写
\[
 e_d(r)=\max\!\left\{1,\frac{1+(d-1)r}{d}\right\},
 \qquad \alpha_d=1-\frac1d,
 \tag{8}
\]
允许最终任意 \(U^\varepsilon\)；这不是声称 \(c=0\) 的 raw theorem。
若 raw 前件只对某一个固定 \(c_0>0\) 已证，结论必须保留 (7)。
457(5)–(10) 与数域报告 (12)–(13) 在这组明确前件下通过。

## 3. 当前 critical scale 上的精确定量比较

为避免几何槽长度和 detector cutoff 重名，记几何长度为 \(e=e_*\)，
长逆列 cutoff 为 \(\ell\)。使用 451 的隔离根
\[
 657e^3-954e^2+21e+20=0,\quad
 \frac{16683858898627}{10^{14}}<e<
 \frac{16683858898628}{10^{14}},
 \tag{9}
\]
\[
 \kappa=\frac56-\frac e2,\quad
 \delta=\frac{5-9e}{6+18e},\quad x=\frac12,\quad
 \ell=\frac{1+3e}{8e}=1.1242271467860845\ldots .
 \tag{10}
\]
本报告的 decimal 是精确公式的显示值。可直接用 (9) 的有理区间得到
所列数值范围；不靠浮点网格证明严格正性。

在 \(\ell>1\) 分支，
\[
 e_6(\ell)-e_4(\ell)=\frac{\ell-1}{12}
 =0.0103522622321737\ldots .
 \tag{11}
\]

| 相对放大次数 | 单个未标记逆列均方指数 | 对六次的条件减少 |
|---|---:|---:|
| 6 | \(1.1035226223217371\ldots\) | \(0\) |
| 4 | \(1.0931703600895634\ldots\) | \(0.0103522622321737\ldots\) |
| 2 | \(1.0621135733930423\ldots\) | \(0.0414090489286948\ldots\) |

这一比较只涉及 (6)。\(r\le1\) 时三者均为1，放大这一步没有收益。
还须注意：\(\alpha_2=1/2\) 低于当前 detector 的 \(\delta\le3/4\) 范围；
若试图把整个长分支 cutoff argument 也替换成 \(d=2\)，其
\(\alpha_d-\delta\) 的符号及端点须重新处理，不能沿用当前全域包络。

## 4. 从 branch gain 到 whole count 的距离

下面是一个刻意明列条件的**反事实预算**，不是 Gaussian count theorem。
除假定 (1)–(8) 在 \(d=4\) 成立，还额外假定新源保留原 short detector 的
actual witnesses、marked/plain widths、共同 profile、自然零、same-row
mask、供槽、height、coefficients 与 \(\kappa\) 合同，只替换未标记长逆矩。
这些额外假定目前未付。此节的作用是防止把 (11) 直接解释为总收益。

在 (10) 的参考 critical 点，原 short/long 两个 count exponents 写作
\[
 c=\frac1{3\kappa},\quad D=\frac52-c,\quad P=1-\frac c2,\quad
 s=\frac{\delta P}{D},
 \tag{12}
\]
\[
 S(t)=1-\delta+s\!\left(\frac32-t\right),\quad
 L_\alpha(t)=1-\delta+(\alpha-\delta)(t-1),\quad t\ge1.
 \tag{13}
\]
实际 \(\kappa_{\rm act}=2\beta_*-1\) 在原反证中仍须用其反馈预算；此处
\(\kappa_*\) 仅用于展示参考临界点，不借用 reference-\(\kappa\) analytic
lemma。原 \(\alpha_6=5/6\)，相对 \(\alpha_4=3/4\)。
由 (9)–(13)，\(S(\ell)=L_{\alpha_6}(\ell)=2/3\)。
长分支等于 \(2/3\) 可直接代入 (10) 验证；短分支的等号使用 (9)。
具体精确余式是
\[
 S(\ell)-\frac23
 =-\frac{657e^3-954e^2+21e+20}{72e(1+3e)(7-5e)}=0.
 \tag{13a}
\]

即使已合法把长分支降为 \(L_{\alpha_4}\)，在同一个原 \(t=\ell\) 仍有
\[
 \max\{S(\ell),L_{\alpha_4}(\ell)\}
 =\max\{2/3,\,2/3-(\ell-1)/12\}=2/3.
 \tag{14}
\]
所以原 cutoff 下，**whole count saving 为零**。

若所假定的全套 short 合同还允许继续增加 \(t\)，则在
\(\alpha>\delta\)、\(s>0\) 的这个点，(13) 唯一交点为
\[
 t_\alpha=1+\frac{s}{2(\alpha-\delta+s)},\quad
 R_\alpha=1-\delta+
 \frac{(\alpha-\delta)s}{2(\alpha-\delta+s)}.
 \tag{15}
\]
这是下降的 \(S\) 与上升的 \(L_\alpha\) 的 max 的最小值；不是新的
actual admissibility 证明。此处 \(t_6=\ell\)，四次的显示值为
\[
 t_4=1.1445876995091053\ldots,\quad
 R_4=0.6636730471049367\ldots .
 \tag{16}
\]
令 \(l_d=\alpha_d-\delta>0\)。精确相减得
\[
 R_6-R_4
 =\frac{s^2}{24(l_6+s)(l_4+s)}
 =\frac{\ell-1}{12}\frac{s}{l_4+s}
 =0.00299361956172998\ldots .
 \tag{17}
\]
故重平衡后的条件 whole-count 收益也严格小于单分支的 (11)。
在原 reference 几何
\[
 b=\frac{-5181+156335e-387630e^2}{81941},\quad
 h=\frac{1+3e+b}{2}=0.8119607261891768\ldots ,
 \tag{18}
\]
同一个 high exponent 中 \(h(1-R)\) 的条件改善是
\(h(R_6-R_4)=0.00243070151327640\ldots\)。
这仍不能解释为可使 \(\sigma\) 减少该小数：原 low 交点、Mellin 留数、
principal cancellation 与 \(C_b(s)=s-2/3-b/6\) 来自 cubic probe 本身。
全 \((\delta,x)\) 连续域、全部物理 \(d\) bins、outliers、strict slots、
actual-\(\kappa\) feedback、共同 normalizer 和全族反证均未随之证明。

## 5. 457 的角色同余与 Gaussian signal：v5 修正是必要的

457(3) 是单-shift 模板中 retained \(j=1\) 反射为二次角色的准确算术条件：
\[
 -1-\rho\equiv m\pmod{2m}
 \iff \rho\equiv m-1\pmod{2m}.
 \tag{19}
\]
若 shift 是 \(\chi^\rho\) 的局部 theta Gauss 角色，则
\(\gcd(2m,m-1)=2\)（\(m\) 奇）或1（\(m\) 偶），故 457(4) 的阶数表正确。
它只给该模板的条件，未证明新 quartic completed reflection，也未排除
其他 probe/retained-row 设计。

旧 sextic 的 \(\gamma_2^3=-\alpha\) 直接换成 quartic 的 quadratic
\(\gamma_2\) 会失败，仍是有效的反例测试。但不能从该失败断言所有
Gaussian signal 都失败。按 DDHL 当前
[v5 (3.9)–(3.11)](https://arxiv.org/html/2306.11875v5)，对 primary
degree-one Gaussian prime \(\pi\)、\(q=N\pi\)，记
\[
 \varepsilon_\pi=\left(\frac{-1}{\pi}\right)_4,\qquad
 \zeta_\pi=\left(\frac{\bar\pi}{\pi}\right)_4^{-2},\qquad
 \alpha_\pi=\frac{\pi}{\sqrt q}.
 \tag{20}
\]
规范化 Gauss sums 满足
\[
 \gamma_2(\pi)=\varepsilon_\pi,\quad
 \gamma_1(\pi)^2=-\varepsilon_\pi\zeta_\pi\alpha_\pi,\quad
 \frac{\gamma_1(\pi)^2}{\gamma_2(\pi)}
 =-\zeta_\pi\alpha_\pi.
 \tag{21}
\]
v3 中缺掉 \(\zeta_\pi\)；本报告不承接统一
\(\gamma_1^2/\gamma_2=-\alpha\) 的旧版本断言。Gauss–Jacobi identity
\(\gamma_1^2/\gamma_2=J(\chi,\chi)/\sqrt q\) 本身没有变化。

还可独立给出 degree-one 补因子的化简。写
\(\pi=a+bi\)，\(q=p=a^2+b^2\) 为 rational prime，primary 强制 \(a\) 奇、
\(b\) 偶。模 \(\pi\) 有 \(\bar\pi\equiv2a\)，故
\[
 \zeta_\pi=\left(\frac{2a}{p}\right)_2
 =\left(\frac2p\right)_2=\varepsilon_\pi.
 \tag{22}
\]
中间等号来自 quadratic reciprocity：\(p\equiv1\bmod4\)，
\((a/p)_2=(p/|a|)=(b^2/|a|)=1\)；负 \(a\) 也因 \((-1/p)_2=1\) 无变化。
最后因 \(a^2\equiv1\bmod8\)，\(p\equiv1\) 或5 mod8 给
\((2/p)_2=(-1)^{(p-1)/4}\)。因此在这组 convention 下
\(\gamma_1^2=-\alpha\)，而 Jacobi signal 为
\(-\varepsilon_\pi\alpha\)。norm5 与 norm17 的单位符号可不同。

作为另一个单-prime 核验，inert \(p\equiv3\bmod4\) 的 primary
\(\pi=-p\)、\(q=p^2\)。有限域 Frobenius 将 quartic \(\chi\) 变为
\(\bar\chi\)，DDHL 的 trace additive character 在该变换下不变。
于是 \(\tau(\chi)=\tau(\bar\chi)\)；又 \(\chi(-1)=1\)，故 \(\tau(\chi)\)
实且绝对值 \(p\)。所以 \(\gamma_1^2=1=-\alpha(-p)\)；无需擅定
\(\tau(\chi)\) 本身的正负。这一步仅核单个 inert prime 的平方信号，
不是 composite CRT/Euler 表或 cusp 完成。

最终 457(2c) 的 squarefree 推广也合法。由 DDHL v5 (3.5)–(3.6)，
coprime primary \(a,b\) 的规范化乘法因子是
\[
 \eta(a,b)=\left(\frac ab\right)_4\left(\frac ba\right)_4
 =(-1)^{C(a,b)}\left(\frac ba\right)_4^2\in\{\pm1\}.
 \tag{22a}
\]
所以 \(\eta^2=1\)。逐 prime 的 \(\gamma_1(\pi)^2=-\alpha(\pi)\) 和
primary generator 的精确乘法性遂给 odd primary squarefree \(c\)
的 \(\gamma_1(c)^2=\mu(c)\alpha(c)\)。这是同一 additive/residue
convention 与原 2-mask 内的真实 squarefree signal，不只是两例数值观察。
它没有注册完整 prime-power/ramified Euler quotient 或 incoming-row 反射。

这支持检验一个新的、含正确 Supplementary law 的 Gaussian prime phase。
但 \(\gamma_1^2\) 对 theta coefficient 是非线性操作，不能把它替代原
线性 Gauss coefficient 而继续调用旧 completed reflection。DDHL 给
square-numerator Voronoi 的 quadratic twist；它仍不是本项目全部
incoming \(j\)、moving marks、natural zeros 的同一 uniform 完成。

## 6. 普通 CM completion：degree 增加哪一部分

对固定 CM 域 \(K\)、\([K:\mathbf Q]=2m\)、primitive finite-order Hecke
character，全部 complex infinite type 平凡。略去固定 \(2^m\)，有
\[
 \Lambda_K(s,\psi)=
 (|D_K|N\mathfrak f)^{s/2}(2\pi)^{-ms}
 \Gamma(s)^m L_K(s,\psi).
 \tag{23}
\]
由普通 Hecke FE，令
\(\mathcal C_K=|D_K|N\mathfrak f/(2\pi)^{2m}\)，得到
\[
 L_K(s,\psi)=\epsilon_\psi\mathcal C_K^{1/2-s}
 \left(\frac{\Gamma(1-s)}{\Gamma(s)}\right)^m
 L_K(1-s,\bar\psi),\qquad|\epsilon_\psi|=1.
 \tag{24}
\]
这是 [Watkins §3.6](https://magma.maths.usyd.edu.au/~watkins/papers/hecke.pdf)
的 completion 的直接整理。457(11) 通过。**导子范数的指数仍为
\(1/2-s\)，不是 \(m(1/2-s)\)**；数域次数已经体现在 gamma 的个数。
若以同一个 common height \(T\) 粗略衡量，analytic conductor 具有
\(|D_K|N\mathfrak f(1+|T|)^{2m}\) 的量级。Stirling 在固定 vertical strip
给普通 gamma ratio 的模为 \((1+|T|)^{m(1-2\Re s)}\)。
固定 \(K\) 的判别式只是常数；若 \(K\) 随主参数变化，则不再能吸收。

一个 complex place 的 inverse Mellin Bessel 核不能原样用于 \(m>1\)。
gamma quotient 的 Mellin 乘积产生多次 Mellin convolution/Meijer-G 型核，
极点可为高阶并带 logarithmic tails。含 angular/norm infinite parameters
的 character 已超出 finite-order 情形，必须保留各个 shifted gamma、
相应 kernel 及其统一 height 费用。

CM 的单位 rank 为 \(m-1\)。\(m>1\) 时无限多个 units 的 absolute norm
都是1，所以原样的 element row count 在 \(U=1\) 就不有限。改用 ideals
后 fixed-field ideal count 仍是一阶；formal ideal injection
\((u,a)\mapsto ua^d\) 也仍由 valuations 可核。但 class representatives、
unit quotient、archimedean bounds、product cocycle 和 row-dependent
profiles 必须先付，才得到 (2) 的实际 family。即使 class number one
也不能删除无限单位步骤。含 \(\mu_6\) 的高次 CM 域若仍使用 \(a^6\)，
其 \(e_6\) 本身没有 order-\(d\) 收益。

## 7. 大筛前件不能代替 raw/marked/plain 接口

[BGL Theorem 1.3](https://arxiv.org/html/1112.1650v1) 的指定 higher-order
squarefree ideal family 给 \(H+D+(HD)^{2/3}\)，不是 (2) 的 \(H\)。
例如取 \(H=D^{1+c}\)、固定 \(0<c<1\)，第三项除以 \(H\) 为
\[
 \frac{(HD)^{2/3}}H=D^{(1-c)/3},
 \tag{25}
\]
这是固定正幂，不能对任意小 \(\varepsilon\) 吸入 (2)。该 published
theorem 还需要它自己的 family、squarefree 及 reciprocity 前件；它不是
任意自然 mask 或 row-dependent profile 的 raw theorem。

因而“已存在 quartic large sieve”没有支付 order-four amplification 的
raw 输入。它也没有支付旧 marked 条件
\(r+2z\le m-c_1,\ 2r+8z\le3m-c_2\)、plain 条件
\(n_1+n_2+6\kappa z\le M\)、共同 inducing sectors 和 principal cancellation。
目前没有“将 \(6\kappa\) 换成 \(4\kappa\)”的已证合同；(8) 与这种替换无关。

## 8. 限定验收与下一可核验接口

本报告通过以下有限数学范围：457(3)–(4) 的 single-shift 算术；
在 §2 完整前件下的 (5)–(10) 相对放大；§3 数值比较；§4 有额外相同
short 合同假设的 counterfactual budget；普通 finite-order CM completion
及 conductor 指数；v5 Gaussian split/inert signal 的补因子处理及
(2c) squarefree CRT 推广。457 其余源依赖、有限 density/class、whole-family
Dirichlet transfer 与未付接口措辞均与这些范围一致；无阻断错误。

缺口是具体且相互不同的：新的 quartic uniform completed reflection；
完整 composite/cusp/Euler reciprocal 与 ramified rows；包括 scale supremum、
moving parameters、heights、once prime slots 的 raw/marked/plain moments；
same-source normalizer/principal residue；全物理连续域及 actual count；
最后才是 uniform Mellin family continuation。DDHL 已证的组件值得继续
使用，不能把它概括成不存在 Gaussian 方案，也不能把未付接口省掉。

因此当前 [R] 条件下 \(\sigma_*=0.8749570194200989\ldots\) 的严格半平面
状态没有变化。换域可给研究方向和相对预算，但本轮没有认证新域的
whole chain、新 \(\sigma\)、RH、RR 或 simple critical-line 比例改善。

## 9. 新有限审计的只读方法核验

本轮额外逐行只读
[新脚本](../../scripts/hybrid_number_field_exact_audit.py)，canonical LF SHA256
ac82eb7aac59449ee218b39f33a3e3291e04066cb296a40033cd98f869589389，
4522 bytes、127 行；以及已有
[JSON](../../output/hybrid-number-field-exact-audit.json)，canonical LF SHA256
e670c3ea1a3d8071ca7c124e83bb89d55feb223b3bd730dfab7cfe674e0122d9，
3452 bytes、202 行。未运行脚本或覆写输出。

方法核验通过：split model 先选一个 primary orientation，按
\(i\equiv-a/b\bmod p\) 直接构造 finite-field quartic symbol，以整数对完整求
\(\sum_x\chi(x)\chi(1-x)\)；不是用待证 signal 生成 Jacobi sum。
它独立比较 supplement 与 \(\varepsilon_\pi\)、\(J=-\varepsilon_\pi\pi\)
及范数。44 是 \(5\le p\le500,\ p\equiv1\bmod4\) 的每个 rational prime
选一支 primary orientation，不表示同时穷举两个 conjugate orientations。

inert model 在 \(\mathbf F_p[i]\) 中精确算术，直接核 Frobenius 及各实部
fiber 的 character 和。非零 fiber 和相同，trace additive phase 的
非零实部总和为 \(-1\)，故得到真实 \(\tau\) 的整数值，再核 \(\tau^2=p^2\)。
此闭式没有用浮点 Gauss 和替代实际符号；JSON 的六例也确实包含正负。
十个 single-shift 模型与 \(d=2,\ldots,20\) 的同余/角色阶数一致。

脚本使用的 \(\ell=2810567867/2500000000\) 是明确标注的 rounded rational
模型；其 Fraction exponent identities 不是 451 的代数根证书。本报告 §3–§4
则直接用 (9) 的隔离根与显示有理函数独立计算，并精确核对 (13a)、(17)。
有限脚本与 JSON 的范围措辞准确；它们没有验证 raw moments、completed
reflection、全部 CRT Euler 表、analytic continuation 或无零区域。
