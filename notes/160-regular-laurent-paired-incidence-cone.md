# Regular Laurent no-go、paired incidence cone 与 forced-physical 通道

文档 159 证明 Vaughan principal-part image 严格位于 physical direction 的正交补，
因此不能直接解释 observed rank-two core。本节完成它提出的两个后续检查：

1. 计算四个 Dirichlet series 的 Laurent constant terms；
2. 从 Vaughan identity 本身抽出 pair-incidence boundary coordinates。

结果一负一正。regular Laurent vector 及 singular annihilator 都不接近 observed
plane；但四分量 identity 确实规范地产生一个二维 paired-difference space，并把
固定 `(8,-8,-3,3)` 的未解释部分压缩成一个复 ratio 与一个 coarse leakage。

这解释了候选的形状，却仍不证明其 uniform capacity；而且精确包含 physical
direction 的 plane 有文档 159 定理 ABX 的 Feshbach 退化，不能仅凭小 angle/excess
冒充 RH 证明。

## 1. Laurent constant terms

沿用文档 159 的记号，置 `z=s-1`，并写

`M_U=m_0+m_1z+m_2z^2+O(z^3)`,                    (1)

`L_V=ell_0+ell_1z+O(z^2)`,                        (2)

其中

`m_2=(1/2)sum_(d<=U)mu(d)log(d)^2/d`,

`ell_1=-sum_(n<=V)Lambda(n)log(n)/n`.             (3)

采用 Stieltjes convention

`zeta(1+z)=z^(-1)+gamma-gamma_1z+O(z^2)`.         (4)

### 定理 ABZ（exact regular Vaughan Laurent theorem）

文档 159 式 (4) 的四个未中心化 components 的 constant vector

`c=(c_1,c_2,c_3,c_4)`                             (5)

为

`c_1=m_2+m_0gamma_1`,                             (6)

`c_2=-(m_0ell_0gamma+m_1ell_0+m_0ell_1)`,         (7)

`c_3=-gamma-ell_0-m_0gamma_1+m_0ell_1`

`    +m_0gamma ell_0+m_1ell_0-m_2`,              (8)

`c_4=ell_0`.                                      (9)

特别地，

`e^Tc=-gamma`,                                    (10)

正好重构 `-zeta'/zeta=z^(-1)-gamma+O(z)` 的 constant term。任意实
cutoff weights `sum w_j=1` 混合后仍满足式 (10)，所以

`c_perp=c+(gamma/4)e in e^perp`                   (11)

给一个 canonical-`s`-coordinate regular transverse vector。

#### 证明

除文档 159 的展开外还需

`-zeta'=z^(-2)+gamma_1+O(z)`,

`-zeta'/zeta=z^(-1)-gamma`

` +(gamma^2+2gamma_1)z+O(z^2)`.                  (12)

第一项 `M_U(-zeta')` 的 constant 是式 (6)。令 `A=M_UL_V`；
`-A zeta` 的 constant 为

`-[m_0ell_0gamma+(m_1ell_0+m_0ell_1)]`,          (13)

即式 (7)。再写

`1-M_Uzeta=-m_0z^(-1)+(1-m_0gamma-m_1)`

` +(m_0gamma_1-m_1gamma-m_2)z+O(z^2)`,           (14)

乘以

`-zeta'/zeta-L_V=z^(-1)-gamma-ell_0`

` +(gamma^2+2gamma_1-ell_1)z+O(z^2)`             (15)

并取 constant，得到式 (8)。第四项给式 (9)。逐项求和全部 cutoff moments
消去，只余 `-gamma`。`□`

函数 `vaughan_laurent_channel_data` 已返回每个 cutoff 的 `m_2,ell_1,c`、混合
constant、式 (10) residual 与 `span{e,c_perp}`。

## 2. Regular 与 annihilator 两条 no-go

还有一个此前未审计的自然候选：若 principal matrix

`R_sing=[d,b]`                                    (16)

满秩，则它的 annihilator

`C_ann=ker(R_sing^*)=S_sing^perp`                 (17)

也是二维且自动包含 `e`。因此本节比较：

- `C_ann`；
- `span{e,c_perp}`；
- 文档 159 的 principal 与 paired candidates。

在九个 `(N,Y,T)` blocks 上，

| candidate | principal sine range | tail/`lambda_1` range | standardized excess |
|:---|---:|---:|---:|
| `C_ann` | `.695--.858` | `.350--.584` | `3.21%--10.62%` |
| `span{e,c_perp}` | `.827--.937` | `.390--.622` | `3.55%--13.18%` |
| fixed paired `(8:3)` | `.0646--.188` | `.0922--.158` | `.0767%--.634%` |

所以 neither principal image, its orthogonal kernel, nor first regular coefficient
解释 observed transverse line。继续机械计算更高 Laurent coefficients 没有规范性
理由：double-pole components 的 higher jets 还依赖 local coordinate，且 finite Abel
Gram 的主方向显然由整段 lag geometry 而非单点 jet 决定。

## 3. Exact pair-incidence coordinates

令

`A=M_Uzeta`, `H=-zeta'/zeta-L_V`, `L=-zeta'/zeta`. (18)

四个 component series 可重写为

`P_1=AL`, `P_2=-AL_V`,

`P_3=(1-A)H`, `P_4=L_V`.                          (19)

定义 component-label space 的正交单位向量

`e_0=(1,1,1,1)/2`,

`u=(1,-1,0,0)/sqrt(2)`,

`v=(0,0,-1,1)/sqrt(2)`,

`c_0=(1,1,-1,-1)/2`.                              (20)

其中 `u,v` 是两个 internal pair boundaries，`c_0` 是两大 pairs 之间的 coarse
imbalance。

### 定理 ACA（exact Vaughan incidence transform）

相对式 (20)，component vector `P=(P_1,...,P_4)` 的坐标为

`<e_0,P>=L/2`,                                    (21)

`<u,P>=A(L+L_V)/sqrt(2)`,                         (22)

`<v,P>=(AH-L+2L_V)/sqrt(2)`,                      (23)

`<c_0,P>=AH-L/2`.                                 (24)

所以 paired-difference space

`D_pair=span{u,v}`                                (25)

不是数值拟合产物，而是 exact convolution identity 的 internal boundary space；
`D_pair^perp=span{e_0,c_0}`。

#### 证明

由 `L=H+L_V`，

`P_1+P_2=A(L-L_V)=AH`,                            (26)

`P_3+P_4=L-AH`.                                   (27)

式 (21)、(24) 由两 pair sums 得到。又

`P_1-P_2=A(L+L_V)`,                               (28)

`-P_3+P_4=AH-L+2L_V`,                             (29)

给式 (22)--(23)。`□`

式 (20) 是一个固定 Hadamard-type unitary transform，对任何四项 Gamma--Euler
convolution decomposition都可定义；式 (21)--(24) 则使用 Vaughan 的具体乘积关系。

## 4. Forced-physical Ky Fan reduction

令 `G>=0` 是任一四 component Gram。给定 `D subset e_0^perp`，考虑所有

`C_x=span{e_0,x}`, `x in D`, `||x||=1`.            (30)

### 定理 ACB（forced-physical transverse Ky Fan theorem）

令 `V` 是 `D` 的任意 orthonormal frame，`H_D=V^*GV`。则式 (30) 中

`tr(P_(C_x)G)`                                    (31)

的最大值由 `H_D` 的 leading unit eigenvector给出；它与 frame选择无关。

当 `D=D_pair` 且

`H_pair=[[alpha,beta],[conj(beta),delta]]`,        (32)

若 leading line 写成 normalized `(q,1)`，则

`conj(beta)q^2+(delta-alpha)q-beta=0`.             (33)

对任意 fixed real `q_0`，两 paired lines 的 projector angle 满足 exact formula

`sin angle(q,q_0)`

`=|q-q_0|/sqrt[(1+|q|^2)(1+q_0^2)]`.             (34)

#### 证明

因为 `x perp e_0`，

`tr(P_(C_x)G)=<Ge_0,e_0>+<Gx,x>`.                (35)

第一项固定，第二项的最大化正是 Rayleigh--Ritz。把式 (32) 作用于 `(q,1)` 并
消去 eigenvalue 得式 (33)。两个 normalized vectors `(q,1)` 与 `(q_0,1)` 的
Gram determinant 是 `|q-q_0|^2/[(1+|q|^2)(1+q_0^2)]`，得到式 (34)。`□`

实现 `forced_physical_transverse_channel_basis` 完成一般 Ky Fan 构造；
`vaughan_paired_incidence_channel_certificate` 返回式 (20) transform、式 (32)、
式 (33) residual、paired gap 与式 (34) 的 direct/formula residual。

## 5. Coarse leakage 与 fixed-line 两项恒等式

令 unrestricted forced optimum `x_* in e_0^perp` 写成

`x_*=a u+b v+d c_0`, `|a|^2+|b|^2+|d|^2=1`.      (36)

置 `kappa=|d|`，并在 `b ne0` 时置 `q_*=a/b`。

### 定理 ACC（paired mismatch--coarse leakage identity）

对 fixed paired line

`p_0=(q_0u+v)/sqrt(1+q_0^2)`                     (37)

有 exact identity

`sin^2 angle(p_0,x_*)=kappa^2`

` +(1-kappa^2)|q_*-q_0|^2`

`   /[(1+|q_*|^2)(1+q_0^2)]`.                    (38)

#### 证明

把 `x_*` 正交分成 `D_pair` projection 与 `d c_0`。后者对式 (37) 完全正交，
贡献 `kappa^2`；前者 norm平方为 `1-kappa^2`，应用式 (34)。`□`

式 (38) 把固定 paired channel 的解析任务精确拆成：

1. ratio cone：控制 `q_*` 靠近 fixed `q_0`；
2. coarse suppression：控制 `kappa`；
3. forced physical plane 到 actual leading plane 的剩余 angle。

若三个量分别为 `s_ratio,s_coarse,s_lead`，则 projector triangle inequality给

`||P_(q_0)-P_*||`

`<=sqrt(s_coarse^2+(1-s_coarse^2)s_ratio^2)+s_lead`. (39)

代入文档 158 定理 ABQ 即给 fixed projector 的 tail/coupling bounds。这个结论是
纯有限维的，无需假设 zeros 在中心线。

## 6. 九 block incidence audit

使用与文档 159 相同的九个 blocks。结果为：

- paired-optimal ratio `q` 的实部在 `2.776--3.414`；
- `|Im q|<.0122`；
- 对 `q_0=8/3`，式 (34) 的 sine 在 `.0131--.0737`；
- unrestricted projected ratio `q_*` 的实部在 `2.738--3.553`；
- `|Im q_*|<.0141`；
- coarse leakage `kappa` 在 `.0061--.1389`；
- 式 (38) 的 total fixed-to-unrestricted sine 在 `.0309--.1621`；
- unrestricted forced plane 到每块 leading rank-two plane 的 sine 在
  `.0414--.1572`；
- fixed `(8:3)` plane 到 leading plane 的 direct sine 在 `.0646--.1882`。

因此式 (38) 对实际几何有解释力：固定候选的偏差确实分成较小 ratio mismatch 与
一个有时更显著的 coarse leakage。`N=160,Y=60,T=2` 的 `kappa=.139` 是当前最坏
样本，不能把 coarse channel直接丢弃。

这些是普通高精度 diagnostics，不是 interval bounds。尤其 ratio ranges没有证明在
cofinal blocks上一致成立。

## 7. 对 RH 证明路线的含义

paired incidence 的正面进展是：

- `D_pair` 从 exact Vaughan algebra 导出，不再是 PCA 发明的坐标；
- fixed seed的未知自由度从四维 plane降成一个 ratio `q_0`；
- ratio与 coarse errors有 exact finite certificates；
- 所需 asymptotic input可具体写成式 (32) entries、coarse coupling及 spectral gap
  的 dyadic bounds。

但这里存在一个必须保留的限制：`span{e_0,p_0}` 精确包含 physical direction。
由文档 159 定理 ABX，其 physical Feshbach infimum可通过 `epsilon->infinity` 自动
逼近 exact energy，而 core physical term本身就是待控制的 arithmetic energy。
所以小 Feshbach excess或小 projector angle只解释 component geometry，并未给出
RH-strength bound。

要让 incidence structure真正参与证明，下一步不能只继续拟合 `q_0`，而必须做到
至少一项：

1. 从 Type I/II estimates直接控制式 (22)--(24) 的 transverse/coarse Grams，并给
   physical component一个非循环 Hodge comparison；
2. 从 incidence algebra构造一个略微 tilted、但不把 physical target原样放入 core
   的 fixed plane，同时证明其 core coordinates可独立估计；
3. 回到 finite-trace negative Hodge index，证明 paired/coarse channels控制负谱容量，
   而不是控制完整 positive physical energy。

本节因此完成的是 algebraic identification，而不是中心线证明：regular Laurent 路线
已被有限证据排除，paired boundary space已被精确导出，剩余开放输入被压成 ratio
cone、coarse suppression与真正非循环的 core estimate。
