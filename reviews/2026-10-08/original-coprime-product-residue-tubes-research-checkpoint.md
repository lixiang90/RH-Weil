# 实际互素产品短窗：完整模 q 零核附近的绝对付款

2026-10-08，checkpoint_audit；本轮基线 main 609fe754。
新结论是实际短窗 Gram 的互素产品 residue tubes 可严格支付一个幂：
固定目标指数 \(1/2<B<17/20\)，任意固定 \(0<\eta<2B-1\)，
令 \(H_{Q,S}=\lfloor X^{1+2B-\eta}/(QS)\rfloor\)，则这些 tubes 经原 F 消费
给 \(O_\varphi(X^{B-\eta/2+\epsilon})\)。完整互素余额仍未支付。
这是平方展开中的真实子项付款，不是原 physical 四全异词的 signed 子族上界。
没有新的 whole 幂、中心常数、比例、κ 或无零边界；不修改任何冻结源或 Git。

## 1. 固定实际对象与身份

本轮 FULL READ 原174行源；复用此前 FULL READ 的172、425、191行输入并重核身份。
canonical UTF-8 LF 采用 CRLF/lone CR→LF，保留 EOF。

| 输入 | 行／LF字节 | SHA-256 |
|---|---|---|
| [真实产品短窗](original-product-fiber-short-window-research-checkpoint.md) | 174／10878 | 06f4d873d5a7b181c21dfd0284a82a3657a80a159d424783deac70da8fecf5ed |
| [真实窄方面比](original-high-prime-narrow-aspect-research-perron.md) | 172／10494 | c56cb22bf3e0977998eec400fc17dee12dc7647e92dc12a61f251cdd79fcf9da |
| [actual unit](hybrid-whole-fourth-unit-unit-actual-research-whole.md) | 425／16428 | b3f14cf4ee5659f8e23bd51dc9bf71e853e783bd2d55e42ee8846d6e8d1e41dc |
| [coherent 能量](hybrid-original-coherent-period-energy-research-checkpoint-audit.md) | 191／8960 | fe19e50f955c47b7abb22933d0b406a9bc339ac68056d8d115d1f7277be22c5f |

保留 q,s,p,r 全部 genuine primes>X⁹ᐟ¹⁰，q最大，p,r,s<q≤X。
固定 q≈Q、s≈S、p≈P、r≈R，A=PR≈QS，Pmin≥cφS，Q,S≲X。
原共同 u、C² profiles、g、sharp prime intervals 和全部参数 λ 均保留。
原 ν 主分量的 n>q 已在分离前准确恢复；n=a+qj 的全部 j≥1。
公共完整 j interval 与至多两个不完整端 period 的 packets 不重叠。
其长度 \(J_\kappa\le C(X/S+1)\ll q\)，edge 用 J=1，空 packet 用0。
原 ν 的全部 t/ω 尾按原 weighted2 包络支付；φ和g没有新增 weighted moment。

设原实际合并系数 \(d_k=\sum_{pr=k}v_pz_r\)，k<q²、q∤k，
每 k 至多两个有序 genuine-prime factor pairs，允许 p=r。
定义 \(D_\gamma(v)=\sum_{j\in I}\gamma_j e_q(-jv)\)，\(|\gamma_j|\le1\)，
\(x_k=d_kD_\gamma(k\bmod q)\)。完整 v-Parseval及真实 coefficient bound 给
\[
 A_\gamma=\sum_k|x_k|^2\le C_\varphi J(1+q/A)\ll_\varphi J. \tag{1}
\]
这对所有实际 parameters 一致，不要求随机素数或 product fiber 等密度。
原完整 slow 相位未取绝对值，Gram 身份仍为
\[
 N_q=\sum_{a=0}^{q-1}|H_\gamma(a)|^2
   =\sum_{k,k'}x_k\overline{x_{k'}}L_q((k'-k)/q^2),\quad
 L_q(t)=\sum_{a=0}^{q-1}e(at). \tag{2}
\]
a=0只是正 norm 的延伸工具；原 unit mask 不因此增添真实零频。

## 2. 整个差分核的零点与 wrap 支付

对整数 \(|h|<q^2\)，有限等式为
\[
 L_q(h/q^2)=e((q-1)h/(2q^2))
       \frac{\sin(\pi h/q)}{\sin(\pi h/q^2)}. \tag{3}
\]
h=0用原有限和取值q；非零 q|h 时分母非零，核严格为0。
因此同 residue 的不同 product quotients 在完整 a-Gram 中确实正交。
不把这个恒等式扩大为不同 residue 或原 Ω 子和的正交。

**有限行和引理。** 若整数 \(0\le H\le q/4\)，则
\[
 \sum_{\substack{|h|<q^2\\\operatorname{dist}(h,q\mathbb Z)\le H}}
 |L_q(h/q^2)|
 \le 3q(2H+1)+12H(H+1)(1+\log q)
 \ll q(H+1)\log(2q). \tag{4}
\]
证明：每个被选 h 唯一写为 h=mq+d、|d|≤H，|m|≤q。
m=0及m=±q全部用|Lq|≤q；这明确包含首尾 wrap，不漏 h 靠近±q²。
若1≤|m|≤q−1，令 \(a_m=\min(|m|,q-|m|)\ge1\)。
因为 \(|d|/q\le1/4\)，有
\(\|h/q^2\|\ge3a_m/(4q)\)，故分母绝对值≥3a_m/(2q)。
分子≤π|d|/q，所以 \(|L_q|\le3|d|/a_m\)。
对d求和得H(H+1)，正负m的 harmonic sum≤4(1+logq)，即得(4)。
对任何固定 k，实际 k′只是上述整数 h=k′−k 的子集，故同一行界成立。
删掉非互素 pairs 只减少这条 absolute 行和；没有用 signed 子集单调性。

## 3. 真互素 residue tubes 的能量和外 F 预算

在每个 dyad定义完整实际 tube
\[
 \mathcal T_H=\{(k,k'):(k,k')=1,\quad
       \operatorname{dist}(k'-k,q\mathbb Z)\le H\}. \tag{5}
\]
它包括任意 product quotient 差、全部 slow 相位和首尾端点；不是仅同商近差。
邻接 absolute 核对称。逐边 \(2|x_kx_{k'}|\le|x_k|^2+|x_{k'}|^2\)，由(1)(4)
\[
 \sum_{\mathcal T_H}|x_kx_{k'}L_q((k'-k)/q^2)|
       \ll_\varphi qJ(H+1)\log(2q). \tag{6}
\]
这支付真实 tube 的 entire absolute contribution，故也支付其 signed 正部。
不要求 d_k 三系数分离，不改变任何真正素数支撑。

μ为原共同包络及 ν log-Mellin 的正绝对参数测度，总质量≪Lᶜ。
定义 \(E_{\rm tube}=3\sum_\kappa\int\sum_q
\sum_{\mathcal T_H}|x_{\kappa,k}\overline{x_{\kappa,k'}}L_q((k'-k)/q^2)|d\mu\)。
这只是 absolute covariance费用，不把tube本身称为PSD矩阵。
对原三 packets、全部 λ/q按同一(6)聚合，得
\[
 E_{\rm tube}\ll_\varphi Q^2(X/S+1)(H+1)L^C. \tag{7}
\]
原 \(\sum_qb_q^2\sum_a|F_q(a)|^2\ll QL^C\)，box prefactor S/(QX)，
故原 same-parameter F/H Cauchy 消费这个加项的费用为
\[
 \frac{S}{\sqrt Q\,X}\sqrt{E_{\rm tube}}L^C
 \ll_\varphi\sqrt{\frac{QS(H+1)}X}\,L^C. \tag{8}
\]
这里 X/S+1≪X/S，因全部实际 S≲X；+1和两 edge均保留。

取首段的 H=HQS。因QS≳X⁹ᐟ⁵，H≲X^(2B−4/5−η)，而B<17/20，
故 H/q→0，足够大X后H≤q/4；同样 \(H+1\ll X^{1+2B-\eta}/(QS)\)，
因为QS≲X²、η<2B−1，使右端至少为一个增长的固定正幂。
由(8)，任意固定ε>0的费用为 \(X^{B-\eta/2+\epsilon}\)。
若需要显式严格 saving，可预先取ε<η/4。有限小X只进入常数。
顶端Q,S≈X时H≈X^(2B−1−η)；B=5/7时为X^(3/7−η)。
取既有B*时保留其所有前件，不能把B*当本源新无条件 whole 输入。

## 4. 剩余完整 signed 合同与更具体的素数结构

把174的互素 Rq精确拆为 Rtube+Rout，其中Rout只含dist(h,qZ)>H。
保留所有实际 packets 后定义
\[
 C_{\rm out}=3\sum_\kappa\int\sum_q
       \operatorname{Re}\sum_{\substack{(k,k')=1\\
                   \operatorname{dist}(k'-k,q\mathbb Z)>H}}
       x_k\overline{x_{k'}}L_q((k'-k)/q^2)\,d\mu. \tag{9}
\]
整个量聚合后只取一次正部。由174共享因子付款及(7)，
\[
 E_H\le C_\varphi Q^2(X/S)(1+Q/Pmin)L^C
          +E_{\rm tube}+[C_{\rm out}]_+. \tag{10}
\]
于是原 actual主频带费用≤X¹ᐟ²Lᶜ+X^(B−η/2+ε)
+ \(S/(\sqrt QX)\sqrt{[C_{\rm out}]_+}L^C\)，尚不能删最后一项。
顶端仍需 \([C_{\rm out}]_+\ll X^{1+2B-\eta'}\) 的真实聚合输入，η′>0；
本源没有证明它。原Ω仅缩小左侧正 norm；从未限制signed R来借用旧whole界。

进一步令h=k′−k，则互素条件精确为gcd(k,h)=1。所有高素数为奇数，h只能为偶数。
若两个不同产品共享ℓ，则h=ℓ(m′−m)，另两 genuine odd primes的差至少2，
所以0<|h|<2X⁹ᐟ¹⁰时，distinct产品自动互素。未付的中央近差不由共享因子付款覆盖。
展开Dγ后只出现 \(|b|<J\) 的短差频：
\[
 R_q=\operatorname{Re}\sum_{h\ne0}\sum_b L_q(h/q^2)\Gamma_b(h)T_{q,h}(b), \tag{11}
\]
\[
 \Gamma_b(h)=\sum_{j,j+b\in I}\gamma_j\overline{\gamma_{j+b}}e_q((j+b)h),
 \quad T_{q,h}(b)=\sum_{(k,h)=1}d_k\overline{d_{k+h}}e_q(bk). \tag{12}
\]
实际 support之外d=0；(9)给(11)保留dist(h,qZ)>H，且所有q|h项严格为0。
这些是实际 shifted semiprime correlations，不是普通ζ无零已控制的三独立系数。

固定 p≠p′与h，方程p′r′−pr=h的所有整数解准确为
\(r=r_0+p't,\ r'=r'_0+pt\)，其中pr₀≡−h(modp′)、r′₀=(pr₀+h)/p′。
真实 sharp r/r′区间把t限制为一个整数区间，点数
≤1+min(Δr/p′,Δr′/p)≪X¹ᐟ¹⁰+1。两条真正素数条件及原权重全部保留。
还须保留跨腿互素约束；square产品p=r或p′=r′仍允许，不把它们漏删。
这里只得到一个更明确的四prime短线性式相关输入，不宣称已有素数AP估计支付它。

## 5. 完整恢复与结论范围

三packet和原 a^iω diagonal按174恢复；没有截 ν/t/ω尾，没有对φ要求额外光滑性。
s排除仍先保留p=s/r=s，再按191§6同Ω/完整period/edge正 Parseval减两点加双点，
其完整 physical修正Oφ(√X Lᶜ)不受这个 Gram分拆改变。graph/chirp/nn原合同不扩大。
新付款扩大了已控 Gram子项：全部 dist(product difference,qZ)≤H的互素 tubes。
它没有支付整段coprime correlation、canonical任意子块或全部原高产品主项。
没有数值实验、toy或外部定理输入；原完整目标与未付 arithmetic余额保持。
