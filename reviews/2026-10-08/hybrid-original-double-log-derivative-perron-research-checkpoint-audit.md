# 原 Type II 双因子 Perron：Λ 留数付款与条件 43/75 完整误差

2026-10-08，checkpoint_audit。父线程给定基线 main fdf86cb。
仅新增本研究文件，不修改旧来源、笔记、审查、输出或 Git。
状态：完整条件证明，待不同作者全文审查。

在同一个普通 ζ 全高度 [Rθ] 下，本稿将 482 的短 Λ 因子
√A 替换为 A^(θ−1/2+δ) 的真实 weighted prefix 付款。
与已付短 μ 界共同消费有限三因子 Perron 后，完整短项第四费用为
1/3+(2θ−1)(a+v)，而非仅对独立矩形积认领此费用。
保持 H=V² 和原实际 small-squarefull core，θ=7/8 时得到

\[
 \boxed{\mathcal M_{E_{\Lambda\mu}}\ll X^{43/75+\varepsilon},
 \quad P_H=R_{\Lambda\mu}+E_{\Lambda\mu},}
 \qquad
 \boxed{\mathcal M_{P_H}=\mathcal M_{R_{\Lambda\mu}}
                  +O(X^{713/1050+\varepsilon}).}                 \tag{1}
\]

这改善完整分区误差与传递，whole 上界仍为 5/7。
Λ sharp prefix 和 pole regularization 已见 446；本稿不声称该接口首次。
新增用途是普通 degree-one 输入下的统一 guard、与 μ 的共同 sharp
product Perron 消费、真实新分区及 43/75 费用族优化。

## 1. 固定输入、同一个函数与量词

本轮 FULL READ 482、其 477 行 source、280 行 peer、446、
476 和原 113 行 short-μ source。下表前六项为本轮全文实读；
最后两项是同一连续研究链此前全文实读的冻结付款，本轮重新核 hash。
canonical UTF-8 LF 只统一 CRLF/lone CR，不 trim，不改变 EOF。

| 输入 | 行数 / LF bytes | canonical SHA256 |
|---|---:|---|
| [482](../../notes/482-original-conditional-mobius-perron-remainder.md) | 139 / 5125 | c0abff933a180f5591412f82772634091f8db0e2079f846772f8a7047ed4a912 |
| [有限三因子 Perron source](hybrid-original-optimized-type-ii-remainder-research-checkpoint-audit.md) | 477 / 17007 | 2d43aa69d79bde9a3aeac00ff4c9ee79696640f816df28eba051011ab255b25d |
| [不同作者 peer](hybrid-original-conditional-perron-remainder-review-peer.md) | 280 / 14200 | 245f4c0c89a8034224e9a031a3087796752a9f47361c367fda47ebb3c1e37784 |
| [446 原 logarithmic-control 与 sharp Λ](../../notes/446-uniform-prime-twists-on-the-original-gabor-frame.md) | 218 / 9890 | 08060477a6ea806d559fd67533d9e6d3b96483a755842cca9a048b6ab5e110cf |
| [476 条件 whole 5/7](../../notes/476-original-fourth-growth-five-sevenths-with-ivic-density.md) | 96 / 4448 | 179829dd25f92ff187359f73455aafad9f957d714df13cf871db47a76e9408b6 |
| [原 short-μ proof](hybrid-short-mobius-twist-and-vaughan-zero-residue-research-radial.md) | 113 / 6064 | a970366e68b8d3526c0dadac49b8ee8f4a7b6984e763712a851f8b6d353a291d |
| [481 全参数 Vaughan 与费用](../../notes/481-original-type-ii-squarefull-tail-and-optimized-moment-transfer.md) | 239 / 10661 | 4ce3ea2ac087d734142c8788607c1c54fc6887bcf535c806c88097447afdc63e |
| [完整 squarefull tail](hybrid-original-type-ii-large-single-prime-part-research-checkpoint-audit.md) | 401 / 15353 | 66c35eb3ed43cec836ff1d10ed01322f115684c44b771d3db7364637994c3cab |

保留 X=T/(2π)、L=logX、J_T=[T/4,4T]、a_L≥cφ>0，
\[
 P_H(t)=\frac1{a_LL}\sum_{\sqrt X<p\le X}
                 \frac{\log p}{\sqrt p}p^{it},\qquad
 \mathcal M_F=T^{-1}\int_{J_T}|F(t)|^4dt.                         \tag{2}
\]
[Rθ] 是普通 ζ 在整个 Re s>θ 无零，1/2≤θ<1。
不把密度估计替代这个全高度输入，不在本文重新认证 [Rθ]。

先固定 δ∈(0,(1−θ)/4)，置 α=θ−1/2+δ，所以 0<α<1/2。
τ 的 guard 可为任意固定 0<c0<C0：
c0T≤τ≤C0T；本轮使用 [T/8,33T/8]。
所有 δ、最终损失和 c0,C0 都先于 T、N 固定。
不取 δ=1/logT。以下 uniform prefix 为全部实数 1≤N≤X，
其 n≤N 指原整数集合。

## 2. Ordinary log derivative 与 pole 的明确分离

记 Dζ(s)=−ζ′(s)/ζ(s)。其 s=1 有 residue +1，故不能写
整个 σ≥θ+δ 上无例外的 Dζ≪(1+|t|)^ρ。
准确的全高度表达是
\[
 D_\zeta(s)=\frac1{s-1}+D_{\rm reg}(s),\qquad
 |D_{\rm reg}(\sigma+ih)|
 \ll_{\theta,\delta}\log(2+|h|),\quad \sigma\ge\theta+\delta.
                                                                    \tag{3}
\]
Dreg 在 s=1 以 removable continuation 解释。

这里只需普通 ζ，不能免费调用 446 的全导子 Hecke 前件。
自足的 degree-one 推导如下。对 |h| 足够大，在 2+ih 为中心、
半径 R=2−θ−δ/4 的盘中，[Rθ] 保证无零，也不含 pole 1。
从中心 Euler logarithm 选择解析 logζ 分支，中心值 O(1)。
固定实部带内 ζ 的 polynomial height growth 给
Re logζ≤C log(2+|h|)。
Borel–Carathéodory 在内半径 r=2−θ−δ/2 给
|logζ|≪θ,δ log(2+|h|)。

对 θ+δ≤σ≤2，以 σ+ih 为中心的小圈半径 δ/4
完全位于上述内盘；Cauchy 给
|ζ′/ζ(σ+ih)|≪θ,δ log(2+|h|)。
σ≥2 由 Euler Dirichlet series 的绝对收敛处理。
减去 1/(s−1) 不改变这个大高度界。
低高度时 Dreg 在固定 compact 带上解析无极点，
右侧再由 Euler 处理，故 (3) 成立。

这个步骤复用了原 ordinary logarithmic-control 的盘、分支和增长合同；
不要求未付的 critical-line reciprocal，也没有把 reciprocal 次幂
错误写成 pure polylog。log derivative 的 log 界由 BC+Cauchy 单独取得。

## 3. 全 Λ sharp prefix：内部 Perron、唯一 pole 与全部尾

定义
\[
 Q_N(\tau)=\sum_{n\le N}\Lambda(n)n^{-1/2+i\tau},
 \qquad z_\tau=1/2-i\tau.                                        \tag{4}
\]
N<2 时 Q_N=0，直接付款。N≥2 时取
\[
 x=N^\sharp=\lfloor N\rfloor+1/2,\quad
 c_N=1/2+1/\log x,\quad H_{\rm in}=T^2.                           \tag{5}
\]
x 与 N 可比，且每个整数离 x 至少 1/2。
在 Re(zτ+w)=1+1/logx>1，Dζ 的 series 绝对收敛。
原截断 Perron 因此为
\[
 Q_N(\tau)=\frac1{2\pi i}
 \int_{c_N-iH_{\rm in}}^{c_N+iH_{\rm in}}
       D_\zeta(z_\tau+w)\frac{x^w}{w}\,dw
 +O\!\left(\frac{\sqrt x}{H_{\rm in}}\log^2(2x)\right).            \tag{6}
\]

为明确无限 Dirichlet series 的截断费用，其 error majorant 为
\[
 \sum_{n\ge2}\Lambda(n)n^{-1/2}(x/n)^{c_N}
       \min\{1,(H_{\rm in}|\log(x/n)|)^{-1}\}.                    \tag{7}
\]
在 n≤x/2 或 n≥2x，|log(x/n)|≥log2。
令 η=1/logx，x^η=e，用
Σ_(n≥2)logn/n^(1+η)≪1+η^(-2)，远端全部费用
≪√x H_in^(-1)log²(2x)，包括无穷 n>x。
近端 x/2<n<2x，Λ(n)≤log(2x)，
|log(x/n)|≳|n−x|/x，且半整数 harmonic sum为 O(log(2x))；
同样得 √x H_in^(-1)log²(2x)。
因此 (6) 不遗漏最邻近整数或无限尾，无 half weight。

把 w 的轮廓左移到 Re w=α>0。
整个矩形的 Re(zτ+w)≥θ+δ，故不跨任何 ζ 零点。
w=0 留在左侧，也不跨；Dζ 的唯一被跨 pole 为
\[
 w_1=1-z_\tau=1/2+i\tau,\qquad
 \operatorname{Res}_{w=w_1}
 D_\zeta(z_\tau+w)x^w/w
       =\frac{x^{1-z_\tau}}{1-z_\tau}.                           \tag{8}
\]
α<1/2<c_N，且 T²>C0T+2 对充分大 T，
所以这个 pole 严格位于内部。
必须保留它；其绝对费用为 O_(c0)(√N/T)。
若把 (4) 的相位改成 n^(−iτ)，轮廓留数取共轭，费用相同。

左线上 Re(zτ+w)=θ+δ<1，与 pole 1 的距离有固定正下界。
由 (3)，|Dζ|≪log(2+T²)，而
∫_(-T²)^(T²)|α+iω|^(-1)dω≪δ logT。
左线费用因此为 Oθ,δ(N^α log²T)。

两条水平线的真实 height 为 ±T²−τ，绝对值≥T²/2。
(3) 给 |Dζ|≪logT，|w|≳T²，
并有 ∫_α^(c_N)x^σdσ≪√x。
所以全部 horizontal joins 为 Oθ,δ(√N T^(-2)logT)。
这是 log derivative 自身的已证费用；μ reciprocal 的水平线仍只用
原 O(√W T^(-2+ρ)) 合同，二者不混同。

由 (6)–(8)，统一于全部 N≤X 与全部正 guard：
\[
 \boxed{
 Q_N(\tau)=\frac{(N^\sharp)^{1/2+i\tau}}{1/2+i\tau}
 +O_{\theta,\delta,c0,C0}\!\left(
       N^\alpha\log^2T+
       \sqrt N\,T^{-2}\{\log^2(2N)+\log T\}\right).}             \tag{9}
\]
特别是任意先固定 ρ>0，
\[
 |Q_N(\tau)|\ll N^\alpha T^\rho+\sqrt N/T
       +\sqrt N\,T^{-2}\{\log^2(2N)+\log T\}.                    \tag{10}
\]
对所有 N≤X，最后两项分别最多 T^(-1/2) 和 T^(-3/2)log²T。
短 prefix 没有改变 uniform 常数；其整数端点都在 (6) 中实际支付。
(9) 与 446 §3 一致，本轮固定 T² 足够覆盖 N≤X、τ~T。

## 4. 真实实部 +c、prime mask 与完整 Λ 带

外层三因子 Perron 实部 c=1/L，与内部 c_N 不同。
对任意 0≤κ≤c，真实全 prefix Abel 精确为
\[
 Q_{N,\kappa}
 =N^{-\kappa}Q_N+
       \kappa\int_1^N Q_u u^{-\kappa-1}du,\qquad
 Q_{N,\kappa}=\sum_{n\le N}\Lambda(n)n^{-1/2-\kappa+i\tau}.       \tag{11}
\]
因为 (10) 对所有 u≤N 成立，u^α、√u 和各 error envelope
均不超过 N 对应 envelope，而
N^(-κ)+κ∫_1^N u^(-κ−1)du=1，
(10) 在实部 1/2+κ 仍成立。特别覆盖原实际 +c，
没有在加权之后丢失 prefix uniformity。

真实 prime mask 由明确的差支付：
\[
 Q_{N,\kappa}^{\rm prime}
 =Q_{N,\kappa}-
       \sum_{\substack{p^j\le N\\j\ge2}}
       (\log p)p^{-j(1/2+\kappa)}p^{ij\tau}.                    \tag{12}
\]
j=2 的 absolute sum ≤Σ_(n≤√N)logn/n≪log²(2N)；
j≥3 的完整 absolute series
Σ_p logp Σ_(j≥3)p^(-j/2) 收敛。
因此 proper-power 差 O(log²(2N))，统一于 κ、τ。
它可被 N^αT^ρ 吸收，不由 full Λ signed norm推出任意 subset norm。

对任意整数 1≤B<A≤X，q(m)仅为 1 或 1_prime(m)，
在实部 1/2+c 上取 A、B 两个真实 prefix 的差，得
\[
 \left|\sum_{B<m\le A}\Lambda(m)q(m)m^{-1/2-c+i\tau}\right|
 \ll A^\alpha T^\rho+\sqrt A/T
       +\sqrt A\,T^{-2}\{\log^2(2A)+\log T\}.                   \tag{13}
\]
prime case 的 O(log²(2A)) 已吸收；不能推广到任意 response mask。
这是本稿向 482 有限 F_(B,A,q) 提供的新合同。

## 5. 保留共同乘积边界的双因子消费

取原一般参数
\[
 0<v<a,\quad v<1/4,\quad \max(1/2,a+v)<y<1,
 \quad U=V=\lfloor X^v\rfloor,\quad A=\lfloor X^a\rfloor,
 \quad Y=X^y,\quad H=V^2.                                      \tag{14}
\]
原 bV(k)=Σ_(d|k,d≤V)μ(d)；任意 U≤B<A 和 q=1 或 1_prime：
\[
 S_{B,A,q}(t)=-\frac1{a_LL}
 \sum_{\substack{B<m\le A,\ k>V\\Y<mk\le X}}
       \frac{\Lambda(m)q(m)b_V(k)}{\sqrt{mk}}(mk)^{it}.          \tag{15}
\]
AV<Y 保证 k>V 的原条件自动成立，但共同 cut不改成矩形。

精确沿用 482 source (6)–(13) 的有限重排：
F_(B,A,q)G_VW_N，N=floorX，矩形长度 Z=AVN<X²，
系数 β_n=Σ_(mdj=n)Λ(m)q(m)μ(d)，
归一后 ≤Cφτ3(n)/√n，包括全部 n>X。
外高度 H_out=T/8、c=1/L、x♯=floorX+1/2、y♯=floorY+1/2，
有限 Perron 积分准确恢复 Y<mk≤X。

其完整 error 仍为
\[
 O_{\phi,\eta}\!\left(
 X^{2\eta}\{\sqrt Z/T+\sqrt X\,T^{-1}\log(2X)\}\right).         \tag{16}
\]
远端包含所有额外 n>X，近端由两个半整数的 harmonic sum支付。
a+v<1 是固定正余量，先选 η 足够小，使 (16) 保持真负幂。
外移位 τ=t−ω始终位于 [T/8,33T/8]；内部 T² 不是这个外积分高度。

同一 τ 和真实 +c 上，原 μ proof 给
|G_V|≪V^αX^ρ，无权 Weyl 给 |W_N|≪X^(1/6)L^C。
把 (13) 放入已保留 product mask 的外 Perron，
主 sup 为
\[
 X^{1/6}(AV)^\alpha X^{2\rho}L^C.                             \tag{17}
\]
Λ pole 的额外 product费用
≪X^(1/6)√A T^(-1)V^αX^ρL^C，
指数为 1/6+a/2−1+vα+ρ。
由于 α<1/2、a+v<1，这小于 −1/3+ρ，为真负幂。
内部 Λ tails 更小；proper-power mask 差已吸收到 (17)。
没有把 pole 删除，也没有把任何已取绝对 error再套 μ 相消。

实际 (15) 只支持 n≤X，原系数 ≤Cφτ3(n)/√n，
故冻结真实二矩合同给 ||S_(B,A,q)||²_(2,T)≪X^ε。
这个二矩求在实际 cut上，不是长度 Z 的矩形上。
sup平方乘真实二矩，δ、ρ、η等按任意最终 ε先预分配，得到
\[
 \boxed{\mathcal M_{S_{B,A,q}}
      \ll_{\phi,\theta,v,a,y,\varepsilon}
             X^{\,1/3+(2\theta-1)(a+v)+\varepsilon}.}           \tag{18}
\]
buffer费用2δ(a+v)在最终 ε之前选定；每个常数可依赖 ε。
(18) 对列出的所有真实 B与两个 q masks统一。

## 6. H=V² 的实际 core 与完整费用族最优性

其余费用完全保持 481/482 的冻结付款：
low 2y−1、Type I 1/3+2v、large proper powers 1−2a、
完整 r(k)>H squarefull tail 1−4v。
不免费为 Type I认领第二次 μ改善。
于是合成误差成本为
\[
 C=\max\{2y-1,\ 1/3+2v,\
           1/3+\beta(a+v),\ 1-2a,\ 1-4v,\ 0\},
 \qquad\beta=2\theta-1\ge0.                                   \tag{19}
\]

H=V² 保证最终 r≤H 时 pure-squarefull k=r 的 rad(k)≤V，
故其原 bV(k)=0。存活 core仍有 s(k)≥2和 s(k)rad(r(k))>V。
主参数取 a=2v，使精确 floor关系
V²≤floorX^(2v)=A 成立；m>A为prime则自动(m,r)=1。
不添加(m,s)=1，不将 H提高而留下 pure-squarefull项称同一优化。

对 (19) 的下界，proper/tail给
a≥(1−C)/2、v≥(1−C)/4。
Type I与tail又给 C≥1/3+(1−C)/2，即 C≥5/9。
short与 β≥0给
C≥1/3+3β(1−C)/4，即
C≥(4+9β)/(12+9β)=(18θ−5)/(18θ+3)。
因此该固定费用族的最优值是
\[
 \boxed{c_\theta^{\Lambda\mu}
       =\max\left\{\frac59,\frac{18\theta-5}{18\theta+3}\right\}.} \tag{20}
\]

当 1/2≤θ≤5/6，取 v=1/9、a=2/9、y=7/9：
Type I、proper、tail和low均5/9，
short为2θ/3≤5/9，达到下界。
当 5/6≤θ<1，令 D=18θ+3，取
\[
 v=2/D,\quad a=4/D,\quad y=(18\theta-1)/D,
 \qquad c=(18\theta-5)/D.                                     \tag{21}
\]
low、short、proper、tail均c；
Type I=(6θ+5)/D≤c，差(12θ−10)/D≥0。
全部一般前件 (14) 成立。两个分支在 θ=5/6 精确一致。
这是 (19) 与 H=V² 的最优性，不是所有分区或 whole方法的最优性。

## 7. θ=7/8 的真实余项与两完整矩传递

精确取
\[
 U=V=\lfloor X^{8/75}\rfloor,\quad
 A=\lfloor X^{16/75}\rfloor,\quad H=V^2,\quad Y=X^{59/75}.       \tag{22}
\]
(19) 五项依次为 (43/75,41/75,43/75,43/75,43/75)。
按原 Vaughan顺序支付 short m、large proper powers、
large genuine-prime m的全部 r>H tail，剩余严格为
\[
 R_{\Lambda\mu}(t)=-\frac1{a_LL}
 \sum_{\substack{m>A,\ m\ {\rm prime}\\
                 k>V,\ r(k)\le H\\Y<mk\le X}}
        \frac{\Lambda(m)b_V(k)}{\sqrt{mk}}(mk)^{it},
 \quad r(k)=\prod_{v_p(k)\ge2}p^{v_p(k)}.                       \tag{23}
\]
所有原 genuine coefficients、μ signs和共同 product endpoints保留。
合成原 low、Type I、short、proper、tail及 proper-power scalar
范数迁移后，有限次 L4 Minkowski给精确
P_H=R_(Λμ)+E_(Λμ)及 (1) 第一条。

新的 U,V,A,Y与482不同，(23)不是旧 Rμ的子族。
H=V²与 A≥H保留前节所述实际 core；
非零 r=1、balanced prime/squarefree k仍存在。

476在同一 [R7/8] 输入下给 M_(P_H)≪X^(5/7+ε)。
先用 R=P_H−E的完整范数差，取得 M_R同幂，
再用
|M_F−M_G|≪||F−G||4(||F||4+||G||4)³，
得
\[
 \frac{3(5/7)+43/75}{4}=\frac{713}{1050},\qquad
 \frac57-\frac{713}{1050}=\frac{37}{1050}.                     \tag{24}
\]
与482比较：
49/81−43/75=64/2025，779/1134−713/1050=16/2025。
与481比较：
13/21−43/75=8/175，29/42−713/1050=2/175。
任意固定最终 ε先分配各小损失；不要求同阶lower或相对未知主项等价，
没有常数级第四预算，也没有改善原比例或σ_*。

## 8. 保持482对象的 genuine-prime aspect corollary

这节保持482的 V=floorX^(8/81)、A0=floorX^(16/81)、
H=V²、Y=X^(65/81)与 bV完全不变。
令 A1=floorX^(64/243)，对原 Rμ中整个
A0<m≤A1、m prime、r(k)≤H 带定义 B1。

首先对同 m-band 的全部 k使用 (18)：
1/3+(3/4)(64/243+8/81)=49/81。
然后对该同band的 r>H 直接重用已证 tail付款：
在 tail的 c_r(n)中添加真实 A0<m≤A1 mask，
uniform τ(r)τ3(n)系数界仍成立，第四费用
1−4(8/81)=49/81。
两完整函数相减给 M_B1≪X^(49/81+ε)。
不能从全部 k带的 signed norm直接推 r≤H子族norm。

精确 Rμ=B1+R1，R1是原482参数下 m>A1的余项；
P_H−R1仍付49/81，complete transfer仍779/1134。
A1/A0≈X^(16/243)，是真实原对象中的 aspect扩大。
该corollary与 (22) 的新主参数对象严格分别消费，不混淆包含关系。

## 9. 长 Λ balance 与 whole 5/7 的具体限度

(10) 对全 N≤X已成立，故它也适用于长 Λ prefixes；
不能据此说完整 whole已经变成43/75。

直接对 P_H的两个 genuine-prime prefixes使用 (10)–(12)，
再用真实二矩，sup²×二矩只给
\[
 \mathcal M_{P_H}\ll X^{2\theta-1+\varepsilon}.                 \tag{25}
\]
θ=7/8时为3/4，比5/7差1/28。
在476的 5/6<θ≤7/8域，
(2θ−1)−B_I(θ)=(1−θ)(4θ−3)/(2θ)>0。
这是446已有的长-prefix弱增长机制，不改进原 complete zero-packet付款。

在本稿三因子 sup²消费中，若扩大到 balanced m≈X^(1/2)，
即 a≥1/2，又要求完整 tail不超过5/7，则 v≥1/14。
θ=7/8时 short费用至少
1/3+(3/4)(1/2+1/14)=16/21>5/7。
若只看新参数 v=8/75，则 a=1/2给 short
1/3+(3/4)(1/2+8/75)=473/600>5/7。
这些是已列方法的费用障碍，不是 balanced prime block的真实下界，
也不是 [R7/8] 下所有可能 joint estimates的不可能性定理。

更长 m若 a+v≥y，(15) 的 k>V不再自动：
不能仍使用未改的三因子 rectangle去宣称整个长 C4付款。
必须保留或另付这一真实 k mask。
原 R中的 r≤H也须用完整 r>H尾差迁移，
不能由 unmasked长Λ signed norm推出其任意子族norm。

原完整 C4生成函数仍为
(Dζ−F_U)(1−ζG_V)；每个 Reρ>1/2的 ζ零点
1−ζ(ρ)G_V(ρ)=1，实际 residue仍 −mρ。
内部 Dζ 的 Perron 移线留在 Re≥θ+δ，不跨零点；
外部有限三因子 Perron 的 F·G·W 本身全纯，实部为 1/2+1/L，不涉 ζ 零点。
它没有移除整条真实余项的 top-zero packet。
要改善whole或中心第四常数，仍需原完整 signed near算术、
joint residue能量或实际带符号 Λ/μ product的更强均值。
普通ζ的一点prefix也不供应模 q>1的 primitive-character或加性相位界。

## 10. 完成范围

新增结论是 (13) 在原有限product合同中的可消费准入、
(18)的真实 short第四付款、(20)费用族的分支最优值、
(22)–(24)条件43/75与713/1050，以及固定482的真实 prime-band扩大。
Λ接口本身已有446记录；新degree-one proof显式支付pole、短prefix、
真实+c、无限internal truncation尾和各horizontal joins。

whole仍5/7，p_dg、κ、原zero-free输入和σ_*不变。
所列 Fraction复核只核费用和有理传递，不认证∞解析。
本文没有写有限素数实验或数值采样替代证明，也没有生成检查器/输出。
