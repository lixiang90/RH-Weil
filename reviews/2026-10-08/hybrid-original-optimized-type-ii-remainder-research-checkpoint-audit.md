# 原优化Type II余项：短Perron保留μ相消与条件49/81完整误差

2026-10-08。作者：checkpoint_audit。父线程提供基线main6149e0a。
仅新增本源；481、旧证明、旧审查、输出及Git均保持。

**状态：完整条件子项证明及误差归约，待不同作者全文独审。**
本轮真正新增的准入是：先对有限三因子施短Perron，保留共同sharp
乘积截断，再使用已有[Rθ]下的短Möbius界。对真实short-m子项得到

\[
 \boxed{\ \mathcal M_{S_A}\ll_{\phi,\theta,v,a,y,\varepsilon}
 X^{1/3+a+(2\theta-1)v+\varepsilon}.\ }
 \tag{1}
\]

它替代旧的1/3+a+v费用，未把一个依赖(m,d)的已取绝对inner误差
再套一次μ相消。在同一个[R7/8]输入下，重新联合选辅助cut给

\[
 \mathcal M_{E_\mu}\ll X^{49/81+\varepsilon},\qquad
 P_H=R_\mu+E_\mu,
\]
\[
 \boxed{\ \mathcal M_{P_H}=\mathcal M_{R_\mu}
               +O(X^{779/1134+\varepsilon}).\ }
 \tag{2}
\]

新的whole upper仍是5/7，原比例与sigma*均不变。
另在固定481对象中完整支付一个更宽的genuine-prime m带，
将原M=X^(4/21)提高到A=X^(3/14)，仍使用13/21误差预算。
这是实际aspect扩大，不是整个Ropt mixed4的新upper。

## 1. 本轮全文输入与同一个scalar

canonical UTF-8 LF仅统一CRLF/lone CR，不trim或改变EOF。
以下均已全文读取并核canonical hash；没有以旧PASS或数值输出代读。

| 完整输入 | canonical LF SHA256 |
|---|---|
| [481完整参数化Vaughan及误差归约](../../notes/481-original-type-ii-squarefull-tail-and-optimized-moment-transfer.md) | 4ce3ea2ac087d734142c8788607c1c54fc6887bcf535c806c88097447afdc63e |
| [原Vaughan系数、lower-block证明](hybrid-original-vaughan-type-i-and-type-ii-reduction-research-radial.md) | cf58086aeb9eee63832ccd06f5499110ea236b4bd94396893757b62e75bdb9d4 |
| [原Weyl、实际二矩及maximal prefix](hybrid-original-type-ii-short-lambda-factor-fourth-research-radial.md) | b39876e0b9d91a06de57d1069cf6adac676252bd1fe737186bb065716015abb0 |
| [原短Möbius统一准入及留数](hybrid-short-mobius-twist-and-vaughan-zero-residue-research-radial.md) | a970366e68b8d3526c0dadac49b8ee8f4a7b6984e763712a851f8b6d353a291d |
| [其不同作者全文审查](hybrid-short-mobius-twist-and-vaughan-zero-residue-review-twisted.md) | 9236813c4a6089210419b702d656e8e5e747a1c5f74a31b75f78e81d62818cf2 |
| [完整平方满尾及Euler留数源](hybrid-original-type-ii-large-single-prime-part-research-checkpoint-audit.md) | 66c35eb3ed43cec836ff1d10ed01322f115684c44b771d3db7364637994c3cab |
| [原scalar proper-power准入](hybrid-short-carrier-canonical-scalar-fourth-admission-research-radial.md) | f04279a9de54303d772859b2ee5e05010567404c53143c928a14e905eb51a0d7 |
| [476 conditional whole输入](../../notes/476-original-fourth-growth-five-sevenths-with-ivic-density.md) | 179829dd25f92ff187359f73455aafad9f957d714df13cf871db47a76e9408b6 |

保持X=T/(2π)、L=logX、J_T=[T/4,4T]、a_L≥c_phi>0，
\(\|F\|_{p,T}=(T^{-1}\int_{J_T}|F|^p)^{1/p}\)，以及

\[
 P_H(t)=\frac1{a_LL}\sum_{\sqrt X<p\le X}
                    \frac{\log p}{\sqrt p}p^{it}.
 \tag{3}
\]

本源的新增估计明确依赖原全高度[Rθ]：普通ζ无零于Re(z)>θ，
1/2≤θ<1。它不是由零密度单独推出，不新增或认证这个输入的证明。
取任意先固定

\[
 0<v<a,\quad v<1/4,\quad \max(1/2,a+v)<y<1,
\]
\[
 U=V=\lfloor X^v\rfloor,\quad A=\lfloor X^a\rfloor,
 \quad Y=X^y,\quad b_V(k)=\sum_{d\mid k,d\le V}\mu(d).
 \tag{4}
\]

允许m带的真实下端为任意整数B≥U、B<A。
q(m)仅取1或1_prime(m)，以同时处理原完整Λ短带与实际prime短带。
定义同一个原C4的真实有限子项

\[
 S_{B,A,q}(t)=-\frac1{a_LL}
 \sum_{\substack{B<m\le A,\ k>V\\Y<mk\le X}}
      \frac{\Lambda(m)q(m)b_V(k)}{\sqrt{mk}}(mk)^{it}.
 \tag{5}
\]

约定S_A=S_{U,A,1}，即主short付款取B=U、q=1；
固定481 corollary取B=M、q=1_prime。
所有原符号与两sharp endpoints保留。因为AV≤X^(a+v)<Y，
原mk>Y、m≤A已强制k>V，不能因此另换一个rectangle。

## 2. 新短Perron：有限系数与正高度guard

令N=floorX，s_t=1/2−it，以及有限entire因子

\[
 F_{B,A,q}(z)=\sum_{B<m\le A}\Lambda(m)q(m)m^{-z},
 \quad G_V(z)=\sum_{d\le V}\mu(d)d^{-z},
 \quad W_N(z)=\sum_{j\le N}j^{-z}.
 \tag{6}
\]

展开原bV后k=dj；在共同mdj≤X下必有j≤N，所以这个finite W_N
截断不删除任何原允许项。定义其真实矩形乘积系数

\[
 F_{B,A,q}(z)G_V(z)W_N(z)=\sum_{n\le Z}\beta_n n^{-z},
 \qquad Z=AVN<X^2,
\]
\[
 \beta_n=\sum_{\substack{mdj=n\\B<m\le A,d\le V,j\le N}}
               \Lambda(m)q(m)\mu(d).
 \tag{7}
\]

有限重排完全保留μ符号；共同乘积条件尚未被删除。
因A≤X、Λ(m)≤L，有\(|\beta_n|\le L\tau_3(n)\)，故归一系数
\(|\beta_n|/(a_LL\sqrt n)\ll_\phi\tau_3(n)/\sqrt n\)。
这对矩形范围n≤Z也成立，而不仅是n≤X。
对任意固定η>0，Z<X²使该上界至多X^(2η)/√n。

置

\[
 c=1/L,\quad \mathcal H=T/8,\quad
 x^\sharp=\lfloor X\rfloor+1/2,\quad
 y^\sharp=\lfloor Y\rfloor+1/2.
 \tag{8}
\]

有限product不要求在Re(s_t+c)>1绝对收敛：它本身只有有限项。
对任何u≠0，kernel

\[
 I_{\mathcal H}(u)=\frac1{2\pi i}
              \int_{c-i\mathcal H}^{c+i\mathcal H}\frac{e^{zu}}z\,dz
\]

满足

\[
 I_{\mathcal H}(u)=1_{u>0}
   +O\left(e^{cu}\min\{1,(\mathcal H|u|)^{-1}\}\right).
 \tag{9}
\]

这里可直接自证：无限kernel的step值由z=0留数给出。
当Hcal|u|≥1，对左右两个虚部尾各积分分部，端点和导数积分
均≤C/(Hcal|u|)。当Hcal|u|<1，
\(I_{\mathcal H}(0)=\arctan(\mathcal H/c)/\pi\)有界，
又\(|e^{i\omega u}-1|\le|\omega u|\)，
故e^(-cu)I_Hcal(u)与I_Hcal(0)之差≤C Hcal|u|，
从而I_Hcal(u)=e^(cu)(I_Hcal(0)+O(Hcal|u|))；
u>0的step还满足1≤e^(cu)，u<0为0，证明(9)。
没有把一个无限Dirichlet series的未付tail隐藏于(9)。

逐个有限β_n用(9)，在x♯及y♯相减，得到

\[
 S_{B,A,q}(t)=-\frac1{2\pi i\,a_LL}
 \int_{c-i\mathcal H}^{c+i\mathcal H}
 \frac{(x^\sharp)^z-(y^\sharp)^z}{z}
 F_{B,A,q}(s_t+z)G_V(s_t+z)W_N(s_t+z)\,dz
 +\mathcal E_P(t).
 \tag{10}
\]

n<x♯恰为n≤floorX，n<y♯恰为n≤floorY，所以差准确给Y<n≤X。
无半权，无rounding endpoint项，无共同product rectangle替代。
写z=c+iω后真实移位高度为τ=t−ω，始终

\[
 \tau\in[T/8,33T/8].
 \tag{11}
\]

此guard保持全正高度；不让截断高度T²把外层卷积移到height0。
短Möbius准入自己的内部Perron仍可用T²，见§4；二者不是同一积分。

## 3. Perron全部近整数误差与远范围

对w=x♯或y♯，误差的绝对upper按(7)、(9)为

\[
 \ll_{\phi,\eta}X^{2\eta}
 \sum_{n\le Z}n^{-1/2}(w/n)^c
       \min\{1,(\mathcal H|\log(w/n)|)^{-1}\}.
 \tag{12}
\]

因为w≤X+1，c=1/logX，所有(w/n)^c≤e²。
对于n≤w/2或n≥2w，|log(w/n)|≥log2，
直接求\(\sum_{n\le Z}n^{-1/2}\ll\sqrt Z\)给远端√Z/Hcal。
这包括矩形product中n>X的全部项，未把它们当成空support。

对于w/2<n<2w，n^(-1/2)≪w^(-1/2)，
\(|\log(w/n)|\gg|n-w|/w\)。端点w是半整数，因此每个
|n−w|≥1/2，且倒数和≪log(2w)。甚至直接取
min(1,z)≤z，全部近端给

\[
 \ll w^{-1/2}\frac w{\mathcal H}
                 \sum_{w/2<n<2w}|n-w|^{-1}
 \ll\frac{\sqrt w}{\mathcal H}\log(2w).
\]

所以两个实际sharp端点均已付，统一有

\[
 \boxed{\ \sup_{t\in J_T}|\mathcal E_P(t)|
   \ll_{\phi,\eta}X^{2\eta}
           \left(\frac{\sqrt Z}{T}+\frac{\sqrt X}{T}\log(2X)\right).
       \ }
 \tag{13}
\]

Z≤X^(1+a+v)、a+v<1给第一项显示负幂
X^(-(1−a−v)/2)，第二项为X^(-1/2)logX。
这是真正的power saving，只需η预先足够小；
没有把polylog^(-C)写成X^(-C)，也没有遗漏最接近两个端点的整数。

## 4. 短μ在真实移位高度和实部上的统一准入

原短Möbius源证明：先固定正bufferδ<(1−θ)/4，
由全高度[Rθ]和原ζ的多项式增长，经logζ的Borel–Carathéodory、
三圆定理得

\[
 |\zeta(\sigma+i\nu)^{-1}|\ll_{\theta,\delta,\rho}
             (1+|\nu|)^\rho,\qquad \sigma\ge\theta+\delta.
 \tag{14}
\]

低高度紧集亦包括在内，ζ的pole1是reciprocal的零。
不是未知的Re=1/2 reciprocal，也不把零密度视为无零输入。
原G_W Perron的左线是Re(z)=θ−1/2+δ>0，不跨ζ零点或z=0。
内部矩形虚部最大O(T²)，先选ρ充分小，再吸收其费用。
端点w♯=floorW+1/2保持原μ cut；有限Perron截断误差为
O(W^(1/2)T^(-2)log²T)，水平线则仅有
O(W^(1/2)T^(-2+ρ))，其中目标ρ>0预先取足够小；
内部高度为O(T²)，故(14)的reciprocal指数先取不大于ρ/2。
这保留buffered reciprocal的次幂费用，不将其误写为纯polylog。
W≤X^v、v<1/4时两项仍是真负幂并可一致吸收。

把原外高度窗[T/4,4T]改为(11)只改变固定上下guard常数。
同一(14)全height成立，内部矩形虚部仍O(T²)，W的上限不变，
原证明因此逐式给全部1≤W≤V、全部τ∈[T/8,33T/8]的

\[
 |G_W(1/2-i\tau)|\ll_{\theta,\delta,\rho,v}
              W^{\theta-1/2+\delta}X^\rho.
 \tag{15}
\]

无需把X,V重新圆整为别的参数；W=1是一项，直接付款。
这个guard扩展来自原证明，而不是由一个较窄窗的norm自动推断。

(10)的实部为1/2+c。对实际μ prefix用Abel，严格有

\[
 G_V(1/2+c-i\tau)=V^{-c}G_V(1/2-i\tau)
   +c\int_1^V G_u(1/2-i\tau)u^{-c-1}\,du.
\]

因为(15)对全部真实prefix u统一，且u^α≤V^α、
\(V^{-c}+\int_1^V c u^{-c-1}du=1\)，其中α=θ−1/2+δ>0，
故

\[
 |G_V(1/2+c-i\tau)|\ll V^{\theta-1/2+\delta}X^\rho.
 \tag{16}
\]

没有把μ系数丢成|μ|后再宣称这项节省，也没有对移线穿零点作未付假设。

## 5. 内部三因子、实际二矩与改进short-m四矩

同一guard上原Weyl证明中的τ与T仍相差固定倍，
无权W_N(1/2−iτ)对所有sharp partial endpoints给
X^(1/6)log^C X。对j^(-c)再作partial summation，其sup加总变差≤2，
于是

\[
 |W_N(1/2+c-i\tau)|\ll X^{1/6}\log^C(2X).
 \tag{17}
\]

这一步不是wholeζ四矩；N≤X，所有三种Weyl长度区间及权仍有效。
另由Λ(m)≤logm、m^(-c)≤1，直接

\[
 |F_{B,A,q}(1/2+c-i\tau)|\ll\sqrt A\,L.
 \tag{18}
\]

最后\((x^\sharp)^c,(y^\sharp)^c\le e²\)，
\(\int_{-Hcal}^{Hcal}|c+i\omega|^{-1}d\omega\ll\log(2X)\)。
将(13)、(16)–(18)放入**先保留productmask的**(10)，得

\[
 \sup_{t\in J_T}|S_{B,A,q}(t)|
 \ll X^{1/6}\sqrt A\,V^{\theta-1/2+\delta}X^\rho\log^C(2X)
  +O\left(X^{2\eta}\left(\frac{\sqrt Z}{T}
                   +\frac{\sqrt X}T\log(2X)\right)\right).
 \tag{19}
\]

三个因子分别取upper发生在有限Perron重排之后；不是把原共同cut删掉。
原finite子项本身仍只支持Y<n≤X，其n系数由τ3(n)/√n控制，
与旧short-m实际二矩证明相同。对长度≤X的原正高度窗，
时间二矩乘子至多O(logX)、系数能量X^eps logX，故

\[
 \|S_{B,A,q}\|_{2,T}^2\ll_{\phi,\varepsilon}X^\varepsilon.
 \tag{20}
\]

将(19)的sup平方乘(20)，显示成本为
1/3+a+(2θ−1)v+2δv，加上预分配的小损失。
给定最终ε>0，先选δ>0小到2δv<ε/4并满足buffer前件，
再取ρ、η、二矩divisor损失各充分小，最后令X增大并吸收日志。
(13)的负幂亦可保持为负，因为a+v<1是固定正余量。
证明(1)，且对全部U≤B<A、q=1或1_prime使用相同的uniform upper。
这不是新联合whole mixed4：支付的是(5)这个完整真实short子族。

## 6. 原参数费用族的条件重新优化

原Vaughan恒等式对任意精确整数U,V成立。
原low-block平方、Type I Weyl、large proper powers与平方满tail合同
在(4)的一般前件下逐式仍成立。新short合同取B=U、q=1。
取H=V²，顺序支付原C4的
short-m、large-m proper powers、large-genuine-prime/r(k)>H，
留下同一scalar的真实余项

\[
 R_\mu(t)=-\frac1{a_LL}
 \sum_{\substack{m>A,\ m\ {\rm prime}\\k>V,r(k)\le H\\Y<mk\le X}}
      \frac{\Lambda(m)b_V(k)}{\sqrt{mk}}(mk)^{it}.
 \tag{21}
\]

k=s(k)r(k)仍是恰为1与平方满的唯一互素分解。
联合费用是

\[
 c=\max\{2y-1,\ 1/3+2v,\ 1/3+a+(2\theta-1)v,
                  1-2a,\ 1-4v,\ 0\}.
 \tag{22}
\]

Type I这里只沿用已付旧费用，没有为它免费认领第二次μ改善。
设D=6θ+15，取固定

\[
 v=2/D,\quad a=4/D,\quad y=(6\theta+11)/D,
 \qquad c_\theta=(6\theta+7)/D.
 \tag{23}
\]

对1/2≤θ<1：v<1/4、0<v<a、y>max(1/2,a+v)、y<1。
a=2v还使H=V²≤floorX^a=A精确成立。
四个active费用low、short、proper powers、tail全等cθ；
Type I为(2θ+9)/D≤cθ，差(4θ−2)/D≥0。
floor界V≥X^v/2、A≥X^a/2、H≥X^(2v)/4只带固定常数。

这个最小化严格限于(22)、H≤V²的费用族。
因为c≥1−2a,1−4v，a≥(1−c)/2、v≥(1−c)/4；
又2θ−1≥0，故

\[
 c\ge1/3+(1-c)/2+(2\theta-1)(1-c)/4
   \quad\Longrightarrow\quad c\ge(6\theta+7)/(6\theta+15).
 \tag{24}
\]

(23)实现此界。不是whole Type II、所有分区、最佳指数对或无零边界的最优性。

## 7. 原[R7/8]下49/81误差与779/1134完整传递

现在θ=7/8，(23)给新的辅助cut

\[
 U=V=\lfloor X^{8/81}\rfloor,\quad
 A=\lfloor X^{16/81}\rfloor,\quad H=V^2,\quad Y=X^{65/81}.
 \tag{25}
\]

按(22)费用依次为

\[
 (49/81,\ 43/81,\ 49/81,\ 49/81,\ 49/81).
\]

由完整Vaughan与原proper-power scalar迁移，精确PH=Rμ+Eμ；
Eμ先合成low、Type I、short、large proper powers、完整squarefull tail
及原norm差O(X^(-1/12))，再作有限次L4 Minkowski，得到

\[
 \boxed{\mathcal M_{E_\mu}\ll_{\phi,\varepsilon}X^{49/81+\varepsilon}}
 \quad\hbox{在原[R7/8]下。}
 \tag{26}
\]

与481的无条件13/21误差不同，(26)明确使用同一个R7/8来供应μ准入。
与此前误差幂之差13/21−49/81=8/567。
未付Rμ仍含balanced genuine-prime m与squarefree k，r=1。
非零s≥2、s rad(r)>V；m>A≥H≥r自动(m,r)=1，未加(m,s)=1。

原476同一[R7/8]给PH complete fourth≪X^(5/7+eps)。
先由Rμ=PH−Eμ取得Rμ的同幂完整norm，再对两完整函数使用
\(|M_F-M_G|\ll\|F-G\|_4(\|F\|_4+\|G\|_4)^3\)，给

\[
 \frac{3(5/7)+49/81}{4}=\frac{779}{1134},\qquad
 \frac57-\frac{779}{1134}=\frac{31}{1134},
\]
\[
 \frac{29}{42}-\frac{779}{1134}=\frac2{567}.
 \tag{27}
\]

任意最终固定eps均经先预分配更小eps满足(2)。
最终eps<31/1134时，以X^(5/7)归一化的差趋0；
不要求同阶lower，不给相对实际主项equivalence，也不是O(1)常数预算。

新的V、A、Y与481都不同，必须使用(25)的原bV及真实剩余。
本稿不将Rμ视为旧Ropt的子族，不迁移旧余项的未证upper。
新C4和Eμ的改变仅为同一PH的辅助有限分区。

## 8. 固定481剩余的真实aspect corollary

这节保持481的V=floorX^(2/21)、M=floorX^(4/21)、
H=V²、Y=X^(17/21)及bV完全不变。
令A1=floorX^(3/14)，并定义原Ropt中的完整band

\[
 B_1(t)=-\frac1{a_LL}
 \sum_{\substack{M<m\le A_1,\ m\ {\rm prime}\\k>V,r(k)\le H\\Y<mk\le X}}
        \frac{\Lambda(m)b_V(k)}{\sqrt{mk}}(mk)^{it}.
 \tag{28}
\]

对这个同m-band的全部k，(1)取q=1_prime、B=M、a=3/14，
θ=7/8、v=2/21，费用
\(1/3+3/14+(3/4)(2/21)=13/21\)。
再将该full band精确拆成r≤H与r>H。
后者直接使用平方满tail证明：inner c_r中加入M<m≤A1的真实mask，
其uniform τ(r)τ3(n) bound仍成立，所以第四费用13/21。
没有从full signed band的norm推子集norm。
一次norm差因此完整给

\[
 \mathcal M_{B_1}\ll X^{13/21+\varepsilon}
 \quad\hbox{在原[R7/8]下。}
 \tag{29}
\]

精确Ropt=B1+R1，R1为原参数下m>A1、r≤H的余项。
原PH−Ropt误差与B1先合成，得PH−R1第四费用仍13/21，
原whole输入下complete moment transfer仍29/42。
A1/M≈X^(1/42)，这是相同原对象中完整genuine-prime m aspect的新增付款。
本节保持全部k及共享乘积mask，非仅positive rectangle或数值实验。

## 9. 留数、whole状态与尚未付真实算术

平方满tail源的small-r生成函数仍严格为
ζ(z)/ζ(2z)乘finite C−1；更新V,H,A没有删掉原−1。
每个Reρ>1/2的ζ零点，真实大prime generating function留数继续−mρ。
(10)是对有限short子项的局部正高度Perron，不是移除这些top residues
的整条C4全Perron换线。两种用法不能互相替代。

本轮没有Rμ或R1的新whole exponent、完整near signed mixed4常数、
新惯性比例、κ反馈或新zero-free输入。原whole5/7、
p_dg=0.673058110281973178650699与引用输入下sigma*保持。
有理数复核只核(23)、(25)–(27)的成本，不认证∞解析；
本源没有写数值实验或有限素数抽样来代替上述proof。

新增付款是(10)–(20)这个完整保留μ和共同sharp cut的准入，
它使真实辅助分区及固定481的允许m aspect得到可审改进。
剩余目标仍为原signed large-genuine-prime、small-squarefull-part的
完整mixed4或真正联合零点包能量；不能只引用新费用替代该付款。
