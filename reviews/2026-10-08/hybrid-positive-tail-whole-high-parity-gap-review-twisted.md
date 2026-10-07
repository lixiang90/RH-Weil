# whole high正尾parity gap：独立全文审查

2026-10-08，审查人 twisted_research。结论：**限定 PASS**。
本次从磁盘全文读取被审稿，独立重算有限恒等式、尾项消元及有理证书；
未改被审稿、旧笔记、math、Goal或Git。

## 1. 最终版本与范围

| 被审来源 | canonical UTF-8 LF SHA-256 | 原始bytes / 行数 |
|---|---|---|
| [whole正尾来源](hybrid-positive-tail-whole-high-parity-gap-research-compression.md) | 568f2c80d9773db7c13bc3605e7d56ed032e3fba7f5d4dc7c34bbea5ac7cb611 | 8059 / 202 |

canonical处理仅为CRLF及lone CR转LF，不trim，不删EOF。
四个冻结输入也逐文件重算，分别吻合被审稿表中的
highGram `3f4c714b…bbb2`、466 `0b955bdc…bbbe`、
parity residual `6a5fb7db…c6f6`、468 `ad4cf9f8…baf7`。

通过的是原实际有限矩阵的整个必要界

\[
 \liminf_T(q_T^{\mathrm e}-q_T^{\mathrm o})\ge41/15120.
\]

它无需新的[R]、先验高第四矩上限、bounded-q或a=o(L²)。
本审查以冻结输入给出的实际K、α、ω及PSD W为前件；
不把这条必要界升级为q上界、whole31/22净预算或零点比例。
§5的Q=1/350继续是未付款条件。

## 2. clip与finite commutator

H、H_R、W、Γ均保留原finite carrier，U仍是原S的谱符号。
特别没有以物理J替换U或删除任何内部P。

对A=H、B=−UHU，实1-Lipschitz函数h_R满足
HS谱投影重叠公式
\(\|h_R(A)-h_R(B)\|_2\le\|A-B\|_2\)。
h_R奇性给h_R(B)=−UH_RU，故clip的反对称误差≤α。
再用\(\|H_R\|_{\rm op}\le R\)，
平方差的HS范数≤2Rα，而奇投影有1/2，准确得到
e_R≤Rα+ω，没有错误调用operator-norm Lipschitz。

我也重推(5)的sharp有限界。H_R特征基中令
δ_i=λ_i²−w_i、ρ_i=Σ_(j≠i)|W_ij|²。
PSD约束W²≤MW给ρ_i≤w_i(M−w_i)。
\((λ_i-λ_j)^2\le2λ_i^2+2λ_j^2\)与对称求和给
K_R≤4τΣ_iλ_i²ρ_i；随后
δ_iρ_i≤Mδ_i²/4+ρ_i²/M和
w_iρ_i+ρ_i²/M≤Mρ_i给
K_R≤M q_diag+4M q_off≤4M q_R。
不需要TrΓ_R=0或Γ_R为PSD。

commutator三角界以
\(\|H-H_R\|_{2,d}^2\le\tau(H^2-H_R^2)=t_R\)
付款，故\(\sqrt{K_R}\ge(\sqrt K-2M\sqrt{t_R})_+\)正确。
这里没有引入随未知第四矩增长的尾误差。

## 3. scalar恒等、双随机求和与cross符号

独立分三种区间核算(6)：u,v≤R；u≥R≥v；u,v≥R。
后一两种都精确化为(uv−R²)²，边界与第一种一致。
因此(7)是全实x,y的不等式；
替换\((u-v)^2\)为\((x+y)^2\)的方向正确。

在H特征基中，U*=U且U²=I使|U_ij|²为双随机矩阵。
两个d_R求和各给t_R，
Σ_(ij)(λ_i+λ_j)²|U_ij|²/d准确等于
\(\|H+UHU\|_{2,d}^2=α^2\)。
这核定(8)，并且其常数不依赖谱最大值或d。

展开Γ与Γ_R的两个反射二次式，精确差为

\[
 \tau(H^2UH^2U)-\tau(H_R^2UH_R^2U)
             -2\tau(WUD_RU).
\]

两次cross相等仅使用有限迹循环性；没有交换W与H。
因UD_RU≥0、0≤W≤MI，
0≤τ(WUD_RU)≤Mt_R。故(9)保留的
2(R²−M)t_R正成本及负号正确。
\(\tau(\Gamma U\Gamma U)=q-2q^{\mathrm o}\)
也由两个正交parity投影直接得到。

## 4. tail消元与moving clip量词

对c=2(R²−M)>0、z=√t_R，(10)右侧在
0≤z≤√K/(2M)等于
K/(4M)−√K z+(M+c)z²。
其极小点z=√K/[2(M+c)]属于该段，最小值为
Kc/[4M(M+c)]。
剩余半轴的cz²≥cK/(4M²)也不更小；K=0直接成立。
故尾消元是精确有限推导，不能仅解释为fixed-R渐近式。

由此(11)同时适用于每个R²>M。
原实际对象选R_T²=L时，
R_Tα_T=O(L^−1/2)、ω_T=o(1)，
2(R_Tα_T+ω_T)²+R_T²α_T²=O(1/L)+o(1)。
M_T保持固定有界且趋3/8，factor趋1，K_T趋41/10080；
最终constant是(41/10080)/(4·3/8)=41/15120。
所有R依赖已显式写出，因此没有把fixed-R的未知o项
用于moving R，也无需控制q_T或t_R的增长。

先T后R的替代两极限也正确：消元后没有未知t_R，
因此可固定任意R²>M_*，再R→∞。
whole gap蕴含q≥41/15120−o(1)，以及
limsup(q_o/q)≤1/2；后者不蕴含q bounded。

## 5. 条件covariance证书与最终限制

独立以Fraction重算Q=1/350后得到

\[
 r_{\max}=11/151200,\quad
 A=4631/72576000,\quad B=143/72576000.
\]

对于q=Q，\(\sqrt{(Q-r)\delta_e}+\sqrt{r\delta_o}\)
的增大区间终点为Qδ_o/(δ_e+δ_o)=13/8400，
确实包含全部允许r。
h=47/5000时，两个严格平方差分别为
365807/16200000000与155910001/22325625000000000000，
均吻合正文。
C±h分别为1747/120000、4003/120000。
其范围仅在未来另付limsup q≤Q后成立。

本次未发现阻断性数学缺口。新付款是无需增长前件的
actual whole parity gap，而不是原高第四矩的固定上限；
没有Lean认证、RH证明、无零边界升级或实际比例提升的声明。
