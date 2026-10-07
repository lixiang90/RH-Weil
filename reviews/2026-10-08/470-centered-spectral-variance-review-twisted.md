# 470：中心化谱方差与whole parity迁移的独立全文审查

2026-10-08，审查人 twisted_research。结论：**限定 PASS**。
全文从最终磁盘读取，独立重推finite行界、centered covariance、两个
liminf量词和moving-clip迁移；不以其他作者review替代证明。
没有修改正文、旧来源或审查、math、Goal、Git。

## 1. 最终绑定与前件

| 被审稿 | canonical UTF-8 LF SHA-256 | 原始bytes / 行数 |
|---|---|---|
| [470](../../notes/470-centered-spectral-variance-excludes-small-high-residual.md) | 729ddbed2b2d2af08e21e5f1ebabfb5663f906c702f52b13f81aac224402a93a | 8073 / 213 |

canonical仅CRLF及lone CR转LF，不trim或删除EOF。
冻结weighted2/commutator输入与此前独审版本一致：454 `8ab99d60…0db7`、
465 `a9290d2d…0464`、466 `0b955bdc…bbbe`。
§5另用[完整正尾来源](hybrid-positive-tail-whole-high-parity-gap-research-compression.md)
`568f2c80d9773db7c13bc3605e7d56ed032e3fba7f5d4dc7c34bbea5ac7cb611`，
该来源已另存[独立全文审查](hybrid-positive-tail-whole-high-parity-gap-review-twisted.md)。

原H、W、Γ与normalized finite trace保持不变。所有显示常数取flat profile，
真实endpoint taper、全部high primes及内部P仍保留。
新结果不需要[R]或预付high4增长上限。
本次不重新认证冻结外部分析内核；核查的是原已付weighted2与finite代数
能否推出本稿新必要界。

## 2. 两个中心化与准确off-diagonal成本

465(4)已经支付τWH²−τW²=o(1)，没有H⁴=O(d)前件；
466(2)已经支付τH²−τW=o(1)。因此本稿
ε=τΓW=o(1)、μ=τΓ=o(1)来自同一实际有限矩阵，
没有将物理ratio方差或另一个row family替换进来。
flat的m=2∫_0^{1/2}t(t+1)/2 dt=1/6，故
v=19/480−(1/6)²=17/1440，独立复算吻合。

H谱基中的δ_i=λ_i²−w_i、ρ_i=Σ_(j≠i)|W_ij|²给
x=τΣδ_i²、y=τΣρ_i，准确q=x+y。
这一y是H谱基下W的off-diagonal成本，和U-odd residual r不同。
重谱任选正交特征基不影响下列必要推导。

精确trace乘法给ε=τΣδ_iw_i−y，而μ=τΣδ_i。
W的总方差包含全部off-diagonal项，因此
τΣ(w_i−m)²=v−y≥0。
对两个真正centered标量序列使用Cauchy，准确得到

\[
 (y+\varepsilon-\mu m)^2
       \le(x-\mu^2)(v-y).
\]

两个因子非负，所有finite误差均保留。
特别不能把v−y免费换回v后仍声称得到本稿较强根。

## 3. 通用finite行界与q的whole下界

我独立重推K≤Mx+4My。W²≤MW给
ρ_i≤w_i(M−w_i)，且
K≤4τΣ_i λ_i²ρ_i。
Young给δ_iρ_i≤Mδ_i²/4+ρ_i²/M，随后
w_iρ_i+ρ_i²/M≤Mρ_i。两式严格合成
K≤Mx+4My，未放宽为4M(x+y)。
此界无需μ=0、ε=0、H/W交换或简单谱。

whole liminf量词也正确。若liminf q=∞结论显然；否则在达到finite
liminf的有界子列上，x,y均有界，可取共同收敛子列。
只有此时删除μ、ε的趋零误差，没有先假定整个q序列有界。
极限中A=41/3780、v=17/1440，保留y²≤x(v−y)与A≤x+4y。
写q=x+y后前一式精确消元为y(q+v)≤qv，而q+v>0。
故

\[
 A\le q+3y\le q+\frac{3qv}{q+v},\qquad
 q^2+(4v-A)q-Av\ge0.
\]

Av>0使两根异号，q≥0必须在正根以上。
独立Fraction核得discriminant为104899/57153600，
(A−4v)·7560=−275，故正根确为

\[
 q_*=(\sqrt{104899}-275)/15120
     =0.003232880359890941970204919231\ldots .
\]

Q=1/350的两个有理证书也逐项复算：
P(Q)=−15199/952560000，
A−[Q+3Qv/(Q+v)]=15199/13967100。
这严格排除该Q，不依赖数值root search。
通用4M sharp例有x=0、ε=−y≠0，确实不满足新增实际centered输入；
本稿没有误称通用4M系数被改善。

## 4. 正尾coercivity的无增长迁移

§5不能只在q bounded后套clip；正文实际采用另一条合法子列。
令g=q−2r，原正尾finite式在R²>M_T域为

\[
 g\ge q_R+2(R^2-M_T)t_R-\zeta_R,
 \quad t_R=\tau(H^2-H_R^2),\quad
 \zeta_R=2e_R^2+R^2\alpha_T^2.
\]

选moving R_T²=ell时，e_R≤Rα+ω且所有常数显式，故ζ_R=o(1)。
q_R,t_R≥0先保证liminf g≥0。
若其liminf无限则结论直接成立；若有限，选g收敛到此finite liminf的
有界子列，正成本自动给q_R=O(1)、t_R=O(1/ell)。
这是关键coercivity，没有先索取q或τH⁴上限。

由||H−H_R||2,d²≤t_R及||W||op≤M_T，
|√K_R−√K_T|≤2M_T√t_R，故K_R趋同一实际K_*。
core的两个centered输入准确为

\[
 \mu_R=\mu-t_R\to0,\qquad
 \varepsilon_R=\varepsilon-\tau(D_RW)\to0,
 \quad0\le\tau(D_RW)\le M_Tt_R.
\]

W的mean与variance没有变化。于是对每个moving H_R与原W应用
§2–3的严格finite covariance和行界，在自动有界的core子列抽取
共同极限，所有core极限都满足q_R≥q_*。
再由g≥q_R−ζ_R得到整个liminf g≥q_*。

此论证不使用只对fixed R成立的未知o_R，也不要求原high fourth tail
统一可积。core有界仅由当前g子列的正尾成本推出。
因此新增whole必要界
liminf(q_e−q_o)≥q_*具有正文声称的无增长域。
q≥g又恢复原q下界；§3不依赖U的证明仍独立有效。

## 5. 旧候选与研究范围

470准确更新467–469数值候选的地位：其finite/条件预算仍正确，
但flat前件limsup q≤1/350现在被整个实际空间严格排除。
附加未付k≥1/40不能修复这一q矛盾。
旧低常数、两个分别的正交及其准确[R]/bounded-q域不因此失效。

本次未发现阻断性数学缺口。新付款是更强的whole必要下界与parity gap，
不是high residual上界、实际full fourth上限、零点比例或新无零区域。
没有Lean构建/认证，也未宣称RH证明；冻结旧来源和审查保持不变。
