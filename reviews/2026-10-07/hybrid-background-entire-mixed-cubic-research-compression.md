# 原背景 entire mixed cubic：近核与 signed far/alias 的付款

2026-10-07。新推导，待另一作者全文独审。只新增本文件；冻结源、旧稿、
Goal、math、Git 未改。本稿不宣布新的比例或无零边界。

新接口：原低三次与一高二低的 weighted cubic 为 o(d)，无需 [R]；
二高一低的每个 placement 在原 fixed-gap θ<9/10 合同下为 o(d)。
没有预先假 high4 bounded。整个背景 ACΛ³ 的小量结论则明确需要
whole high4 bounded，用来合并已付 high³ 的相对界并恢复 actual 背景。

## 1. 同对象、weights 与完整源快照

原 X=T/(2π)、L=log X、d=floor(XL)、I=[−L/2,L/2]、
Ee_k=L^-1/2 1_I exp(iτ_k u)，τ_k=T+2πk/L，P=EE*、Q=1−P。
φ 为原 even C² compact taper，a_L=||φ||²/L→aψ>0。
B_H、B_L 是原 genuine-prime high/low physical channels，
H=E*B_HE、C_L=E*B_LE，全部 translations 在实线上零延拓。
prime coefficients b_p=log p/(a_LL sqrt p)。

|输入|canonical UTF-8 LF SHA-256|
|---|---|
|notes/454 原背景|8ab99d60c1b748dc561cac57ee498057a0c9fb19b9778a041261b1bad0750db7|
|notes/455 proper-power S4|6bf2025dcc8f56d7b35d9c8b764ac2ff3b911a6e054bf9c496042c7f3e11ce41|
|notes/461 entire13|f9fdf0b721c76a5cc4c4e4821748007e62975286417e6bec9700e39b6778170b|
|notes/462 entire low4|868adfeb0d742043f39bd08e0783d66b7a9db11316067b0b3b43d80150cdf680|
|notes/463 height|6554ebc80616917d00b68f626329e8464e6ccc218c456608bff74e9da5a17d90|
|finite-band source|bc6ad6b1a007422c7678cd540b4127b81d2adc168faf5b090a58b6676778e35f|
|weighted high cubic source|2f883e521bd8f729084530aa8273acc397b528ce66392df1d7a803e53b43bbae|

令 D=E*M_wE。physical 论证允许任意 unshifted complex bounded w(u)，只用
||w||∞≤M；finite 论证另要求原 admissibility：
max(||QM_wE||HS,||QM_bar(w)E||HS)≤C sqrt L，
以及 wφ 的 C² Fourier tail bounds 一致。两个 leakage 实际相等：
其平方分别为 Tr E*|w|²E−TrD*D 与 Tr E*|w|²E−TrDD*，
有限迹相等；因 φ 实值，bar(w)φ 的 tail bounds 亦相同。原背景
w=h_L=φ²/a_L−1 满足更强 leakage O(sqrt(log(2L)))，完全属于此类。
fixed bounded C² scaled profiles 及其原 admissible products 也可使用。
不把 arbitrary L∞ weight 的 finite leakage 免费当成 sqrt L。

结论覆盖 C_L³、H C_L²、C_L H C_L、C_L² H，以及
H²C_L、H C_L H、C_L H²；是每个原 finite placement 的 complex
absolute o(d)，不是只删 real part 或 repeated labels。

## 2. 每个 physical signed word 的准确积分

对三个 prime labels p_i、signs σ_i=±1，置 s_i=σ_i log p_i，
t_1=s_1、t_2=s_1+s_2、S=s_1+s_2+s_3。直接作用原 Ee_k 给

\[
 \frac1d\operatorname{Tr}(E^*M_w B_{R_1}B_{R_2}B_{R_3}E)
 =-\sum_{p_i\in R_i}\prod_i b_{p_i}\,K_d(S)\,
   \frac1L\int_I w(u)\phi(u)\phi(u+S)
           \phi(u+t_1)^2\phi(u+t_2)^2\,du,
 \tag{1}
\]

summed over all eight signs。K_d(S)=d^-1Σ_(k<d)e^(iτ_kS)。
所有 middle windows、原 finite k、label repeats 都在 (1)。
physical support 准确要求 |S|<L；|S|≥L 的 endpoint product 为零。
取固定 c>0 足够小，使 2c<log 2。smooth near cutoff κ=1 于 |S|≤c，
κ=0 于 |S|≥2c；far 为 1−κ。没有硬 near gate 的免费分离。

所有三 prime 的 S=0 都不可能：two-versus-one 等式将要求 prime
等于两个 primes 的乘积；same-sign 更不可能。此论断包含重复 labels。

## 3. near：所有 signs、band masks 与独立 product columns

在 |S|≤2c，准确展开

\[
 K_d(S)=\frac{L}{2\pi i dS}
       \{e^{i(T+2\pi d/L)S}-e^{iTS}\}+O(d^{-1}).
 \tag{2}
\]

κ/S 的主项使用 κ 的固定 Fourier-L1 展开。φ(u+S)、两个 φ² 的
共同 Fourier 展开有 L1 cost O(ell0³)，ell0=log(2+L)。保留
w(u)φ(u) 不展开，normalized u integral≤M。每个 label 的 phase
是各 Fourier variables 的固定整数线性组合；故两正一负比较可按
两-prime integer product n 与 single prime q 分组，用同一 log-integer
union 的 bilinear Hilbert。energy bounds 对全部 Fourier phases 一致。

near support 必须先得到 product prefix，再保持 independent q-side：

* LLL：two-low product n≤e^(2c)q≤2sqrt X。删去不存在的 n=q 后，
  product 与 prime 两侧 weighted energies 均 O(sqrt X/L)。
  Hilbert 与 L/d prefactor 的费用 O(ell0³/(sqrt X L))。
* HLL：只有 high single prime 与 two-low product 的比较可 near。
  若 high 与一个 low 同侧，product>2sqrt X 而另一 low≤sqrt X，
  因 e^(2c)<2 准确排除 near。two-low product 本来≤X，energy O(X/L²)，
  high prime energy O(X/L)，费用 O(ell0³/L^(3/2))。
* HHL：two-high product 对 low single prime 无 near，因为 product>X。
  唯一可能是 high×low product n≤2X 对 high prime q≤X。
  bands disjoint 保证该 product 的 high/low factorization 唯一。
  product 与 prime energies均 O(X/L)，费用 O(ell0³/L)。

对 LLL 与 HHL 的 product energy，统一 elementary upper 为

\[
 \sum_{pr\le Y}pr\,b_p^2b_r^2
 \ll L^{-4}\sum_r\log^2r\sum_{p\le Y/r}\log^2p
 \ll Y/L,\qquad Y=2\sqrt X\text{ 或 }2X.
 \tag{3}
\]

用 Chebyshev Σ_(p≤y)log²p≪y log(2y)、Mertens
Σ_(r≤Y)log²r/r≪L²。low×low columns 的 multiplicity 至多二，
任意 complex phase 下同一 bound 只乘固定常数。
prefix 1_(pr≤Y) 只耦合 product-side 的两个 factors，绝不再耦合 q。
剩下的 smooth κ(log(n/q)) 用其 Fourier integral 才合法分离两侧。
prime-versus-semiprime sets disjoint，union spacing δ_n^-1≪n。

(2) 的 O(1/d) remainder：LLL、HLL 用整个 raw absolute mass即可小量。
HHL 在 n≤2X 的 product-side mass≤C sqrt X/L，prime-side mass≤C sqrt X/L，
故 remainder O(L^-3)。这里没有把未截断长度 X^(3/2) 免费变成 2X。
全部 near terms 因而为 o(1)，每个 placement 都只改变 unit-modulus phases。

## 4. HHL alias 的原 positive mass 与 middlefar Fourier 预算

关键不能用全部 HHL 的 raw mass/X：它为 X^(1/4)/L³，会增长。
先用一个 fixed smooth alias cutoff α_L(S)：在 L−|S|≤A 时为1，
在 L−|S|≥2A 时为0，A>0 固定；只讨论原 physical support |S|<L。
near cutoff 与 alias cutoff 对大 L 支持不交。

原 endpoint overlap 对所有 bounded w 给
|K_d(S)|·L^-1∫_I |wφ(u)φ(u+S)φ(u+t_1)²φ(u+t_2)²|du≪M/X，
在 alias strip 也成立：δ=L−|S| 时 overlap length≤δ，
|K_d|≤C L/(dδ)，两项相乘≤C/d≤C/X。无需把 oscillation 当正数。
只有这段 alias 使用 positive upper，下列算术保持所有 band masks。

记 high p,q>sqrt X、low r≤sqrt X。

* 两个 high 同号，low 同号时 |S|>L，physical term为空。
  low 反号时，反射 S 后可写 S=log(pq/r)>L/2；physical support给
  pq<Xr。所有这样的 physical tuples（因此也包含 alias）的质量满足

  \[
    \sum_{r\le\sqrt X}b_r\sum_{pq<Xr}b_pb_q
       \ll \sum_{r\le\sqrt X}\frac{\log r}{L\sqrt r}
              \frac{\sqrt{Xr}\log(Xr)}{L^2}
       \ll X/L^2.                                      \tag{4}
  \]

  内层 upper 由 Chebyshev 和 Σ_(p≤Y)log p/p≪log Y 得
  Σ_(pq≤Y) log p log q/sqrt(pq)≪sqrt Y log Y。这里松弛 high masks
  只用于 positive upper；没有更改 signed canonical sums。
* 两个 high 反号。再反射 S 后可写 S=log(p/(qr))。
  positive alias 不可能，因为 p/(qr)≤sqrt X/2<e^(L−2A)。
  negative alias 给 qr/p≥e^(-2A)X，强制 p≤e^(2A)sqrt X。
  这个 short high prefix质量 O(X^(1/4)/L)，其余 q、r 全质量分别
  O(sqrt X/L)、O(X^(1/4)/L)，故 tuple质量 O(X/L³)。

乘 overlap bound M/X，alias总费用 O(M/L²)=o(1)。反射覆盖全部
eight signs；三个 placements只改变 intermediate windows，未改 endpoint bound。

剩下 middlefar：置

\[
 g_L(S)=\frac{(1-\kappa(S))(1-\alpha_L(S))}{L\sin(\pi S/L)},
 \quad |S|<L,\qquad g_L(S)=0\text{ outside},             \tag{5}
\]

是全局 C² compact function，在 |S|≤c 与 L−|S|≤A 均为零。
在 |S|≤L/2，其第 j≤2 导数由 C(1+|S|)^(-j-1) 控制；
在 |S|≥L/2，改用 δ=L−|S|≥A，界为 Cδ^(-j-1)。
fixed transition derivatives同样有界。因此 ||g_L||1≪log(2L)、
||g_L''||1≪1，Fourier-L1≪ell0，|ξ|>c_1T 的 Fourier-L1 tail≪1/T。
即使只采用461的较松固定 L 幂界，也足够以下 fixed-gap幂节省。

K_d 的精确 endpoint公式还原 prefactor L/(2id)，两 heights 为
T−π/L 与 T+(2πd−π)/L，均在 [T−O(1/L),2T+O(1/L)]。
将 g_L、φ(u+S)、两个 intermediate φ² 作共同 Fourier 展开。
原 windows 各自 Fourier-L1≪ell0、二阶 tail≪1/T，所以 joint总variation
O(ell0^4)，任一原 variable>|ξ|>c_1T 的 total tail O(ell0^3/T)。
这里剩下的 nonseparable gate正是 g_L(S)，其 Fourier integral已付。

始终保留 w(u)φ(u) 与固定 u domain I：normalized integral
L^-1∫_I w(u)φ(u)e^(iξu)du 的模≤C M。Fourier prime phase shifts只来自
S、t_1、t_2 的固定线性组合，不依赖 u；arbitrary bounded w无需展开，
不改变 canonical prefix，也没有免费 δ-function integration。

## 5. far 原 canonical prefixes 与 absolute heights

令 q_H、q_L 为原 normalized sharp genuine-prime prefix 在
absolute height [T/2,3T] 的 pointwise bounds。原 [R] 的 fixed
θ<a<9/10、a>3/4 给

\[
 q_H\ll X^{a-1/2}\operatorname{polylog}X,\qquad
 q_L\ll X^{a/2-1/4}\operatorname{polylog}X.
 \tag{6}
\]

low cutoff 是 sqrt X，但其 height 仍是 T≈X。sharp Perron 的
log(2Y(3+|t|)) 一直 O(L)，没有将 height 偷换成 sqrt X。
genuine primes 由完整 Λ prefix减去 same-cutoff proper powers，
high 再减 low prefix；所有系数、normalizer、cutoffs都保持。

good Fourier variables 取每个 |ξ_i|≤c_1T，小 c_1 使所有有限线性组合
的 shifted endpoint heights绝对值均在 [T/2,3T]。negative signs 是同一
real-coefficient canonical prefix 的 conjugate，没有新的 character family。
三 label sums 随每个固定 Fourier tuple 独立分解，重复 labels仍自然在内。
HHL good middlefar 因而为

\[
 O\left(\frac{q_H^2q_L}{X}\operatorname{polylog}L\right)
 =O\left(X^{(5/2)a-9/4}\operatorname{polylog}X\right)=o(1).
 \tag{7}
\]

bad tuple 至少一个 variable超过 c_1T，使用 raw全高度
m_H≪sqrt X/L、m_L≪X^(1/4)/L。费用≤
O(m_H²m_L ell0^C/(XT))=O(X^-3/4 ell0^C/L³)=o(1)。
不是在坏 height继续套 [R]。端点 alias 已由第4节独立 positive计数付款，
无需在 alias 内套 canonical prefix 或改变其 nonseparable masks。

LLL、HLL far 甚至无需 [R]：原 endpoint-overlap 消去 alias pole 后，
|K_d|·normalized absolute window≪1/X。raw masses/X 分别为
O(X^-1/4/L³)、O(L^-3)。所有 same-sign、two-versus-one 与反向词均覆盖。

## 6. middle P 与 raw/good physical 高度桥

不能把 physical cubic直接当 finite cubic。LLL、HLL 用原 individual
prime leakage ell_R≪m_R sqrt(ell0) 和 weight leakage≤C sqrt L，
four-operator trace telescoping的每项至少 two crossings，complex weight
左 crossing 使用 QM_bar(w)E，右 crossing 使用 QM_wE，给
weighted finite/physical差=o(d)：最大 raw product为 m_Hm_L²≈X/L³。

HHL 的 raw product=X^(5/4)/L³ 不允许这样支付。改走原 good-band operators：
||B_R^g||op≤q_R、||QB_R^gE||HS≪sqrt L q_R（finite-band source），
weight norm与 leakage保持。four-operator two-cross telescoping给

\[
 |\operatorname{Tr}(D C_{R_1}^g C_{R_2}^g C_{R_3}^g)
 -\operatorname{Tr}(E^*M_w B_{R_1}^g B_{R_2}^g B_{R_3}^gE)|
 \ll L q_H^2q_L=o(d).
 \tag{8}
\]

这是保留原 finite P 的误差估计，不是宣布 good D 与 P/J 交换。

finite raw/good cubic之差用原 finite bad compression S1≤m_R/T²，
给 absolute ≤C M m_H²m_L/T²。physical weighted raw/good 用原
single first-far escape：right φ packet bad HS=O(T^-1)，或之前 φ²
convolutions 首次 far 的 HS=O(T^-1)，left wφ packet HS=O(sqrt d)。
wφ 的 C² tail 是第1节明列前件；weight没有被放进 middle ghost。
归一化 error≤C M m_H²m_L/(T sqrt d)=O(X^-1/4/L^(7/2))=o(1)。
所有 earlier near convolutions的 source band length O(T)，原 cumulative
escape证明逐项保持。使用三个 factors反而比原四因素接口更弱。
没有在未知 high4之前用 S4稳定性替换这一步。

所以 finite raw→finite good→physical good→physical raw 每个接口
都已支付。第3–5节给最后的 raw physical o(d)，完成每个 HHL placement。

## 7. 条件合并 actual 全背景与 proper powers

已得：Tr D C_L³=o(d)、所有 HLL/HHL placements=o(d)，
前两类无需 [R]，第三类只需同一原 θ<9/10 fixed-gap合同。
weighted-high source则给无预先 full4前件的相对界
|Tr A0H³|/d≪sqrt(a_T)/L，a_T=TrH⁴/d。

因此 **若另外支付 limsup a_T<∞**，则 prime C_pr=H+C_L 的第四矩
由 Schatten Minkowski与462有界，所有 static cubic组合给
Tr A0 C_pr³/d→0。actual A=A0+R_T 的 ||R_T||op=O(1/L) 恢复此时才
合法：Tr|C_pr|³/d=O(1)，故 TrR_TC_pr³/d=o(1)。
455 的 original proper-power error normalized S4=O(1/L)，
非交换 cubic telescoping与 normalized Schatten Hölder再给

\[
 \boxed{\frac1d\operatorname{Tr}(A C_\Lambda^3)\longrightarrow0
 \quad\text{if whole genuine-high fourth is bounded}.}
 \tag{9}
\]

低/负 height、pole、全部 proper powers都在恢复中，没有提前删除。
这改善454在这个明确 conditional regime下的 centered-fourth桥：

\[
 \operatorname{Tr}(G-I)^4/N
 =\operatorname{Tr}C_\Lambda^4/N+6Z_\psi-J_\psi+V_\psi+o(1),
 \tag{10}
\]

无需此前 Cauchy 产生的 4sqrt(Zψ F) positive附加费用。
没有 whole high4 bounded前件时，(9)–(10) 不可使用；只能保留已付
mixed小量与 high³/actualR 的 relative budget。

本稿新付款的是 background所有含low的 cubic，及由之导出的条件桥。
它没有支付 whole high4、Γ或commutator目标上限，没有得到新比例。
