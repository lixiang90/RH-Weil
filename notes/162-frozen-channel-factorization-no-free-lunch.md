# Frozen channel 的精确 Type I/II 公式与 compression no-free-lunch

文档 161 构造了 fixed tilted incidence basis，并把经典 RH 的一个具体充分条件写成
core/coupling/tail Feshbach capacity。有限与 held-out audits说明这个 basis稳定，但
稳定的 label geometry不等于 Hodge--Riemann inequality。本节完成两项必要审计：

1. 把四个 frozen channels逐系数化成 truncated Möbius与 high/low Mangoldt
   convolutions；
2. 证明任何只控制 tail、coupling与 projector angle而不独立控制 physical core的
   compression theorem必然失败。

第二点明确了 generalized Weil structure还缺什么：不是另一个更漂亮的 basis，
而是一条排除任意 core rank-one amplification的算术 Hodge relation。

## 1. 两个基本 convolution currents

令

`a_U=mu_(<=U)*1`,                                 (1)

并记

`X=a_U*Lambda_(>V)`, `Y=a_U*Lambda_(<=V)`,        (2)

`L=Lambda`, `V_0=Lambda_(<=V)`.                   (3)

文档 153 的四个未中心化 Vaughan components逐系数可写为

`P_1=X+Y`, `P_2=-Y`,

`P_3=L-V_0-X`, `P_4=V_0`.                         (4)

事实上 `P_1+P_2=X` 是文档 160 中的 `AH`，而 `Y=AL_V`。式 (4) 不使用
asymptotics，是有限 Dirichlet convolution恒等式。

## 2. 四个冻结整数 channels

采用文档 161 定理 ACF 的 normalized columns

`w_0=(21,21,19,19)/(2sqrt401)`,

`w_1=(3,-3,-1,1)/(2sqrt5)`,

`w_2=(19,19,-21,-21)/(2sqrt401)`,

`w_3=(-1,1,-3,3)/(2sqrt5)`.                       (5)

令 `Z_j=<w_j,P>`。

### 定理 ACH（exact frozen Vaughan channel factorization）

相对式 (1)--(3)，四个 channel coefficients逐项满足

`Z_0=(2X+19L)/(2sqrt401)`,                        (6)

`Z_1=(4X+6Y-L+2V_0)/(2sqrt5)`,                   (7)

`Z_2=(40X-21L)/(2sqrt401)`,                       (8)

`Z_3=(2X-2Y-3L+6V_0)/(2sqrt5)`.                  (9)

前两项是 fixed core，后两项是 fixed tail。physical target只使用 sum-sector
channels：

`L=(40/sqrt401)Z_0-(2/sqrt401)Z_2`.               (10)

#### 证明

把式 (4)代入式 (5)。例如

`2sqrt401 Z_0=21(P_1+P_2)+19(P_3+P_4)`

`=21X+19(L-X)=2X+19L`,                            (11)

给式 (6)。同理

`2sqrt5 Z_1=3(P_1-P_2)-P_3+P_4`

`=3(X+2Y)+(X-L+2V_0)`,                           (12)

给式 (7)；另两项相同。将式 (6)、(8)代入式 (10)，`X` 精确消去且 `L`
coefficient为一。`□`

函数 `frozen_vaughan_tilted_channel_coefficients` 对任意 finite cutoff直接从四个
component arrays构造 `Z_j`，并分别验证式 (6)--(9)与式 (10)。

式 (8)--(9)把文档 161 中抽象的 tail `C` 具体化成两个 proof targets：

`R_sum=40(a_U*Lambda_(>V))-21Lambda`,             (13)

`R_pair=2(a_U*Lambda_(>V))-2(a_U*Lambda_(<=V))`

`       -3Lambda+6Lambda_(<=V)`.                 (14)

它们保留 Möbius cancellation、high/low prime split与 modulation phase，可直接进入
Type I/II large-sieve estimates。另一方面 core式 (6)--(7)仍显式含 `L`，所以只把
tail做小并未自动控制 target大小。

## 3. Positive Gram 的 rank-one obstruction

令 `K` 是有限维 component label Hilbert space，`e in K` 是 physical synthesis
vector，`P` 是任意 orthogonal core projector，`Q=I-P`。对 positive Gram

`G=[[A,B],[B^*,C]]`                               (15)

只控制 `B,C` 是否可能控制 `<Ge,e>`？答案是否定的。

### 定理 ACI（component-compression no-free-lunch）

若 `Pe ne0`，则对每个 `M>0` 存在 rank-one `G_M>=0`，使

`PG_MQ=0`, `QG_MQ=0`,                             (16)

但

`<G_Me,e>=M||Pe||^2`.                             (17)

若 `Pe=0`，则存在 rank-one `G_M>=0` 使 core与 coupling为零，而

`<G_Me,e>=M||e||^2` 全部位于 tail。

#### 证明

当 `Pe ne0`，置 `u=Pe/||Pe||`，取

`G_M=M|u><u|`.                                    (18)

因为 `u in Ran P`，式 (16)成立；又

`<u,e>=<u,Pe>=||Pe||`，                           (19)

得到式 (17)。当 `Pe=0` 时，`e in Ran Q`，取 `u=e/||e||` 同理。`□`

`component_projector_no_free_lunch_certificate` 对任意 supplied projector构造式
(18)，并返回 positive spectrum、core/tail/coupling norms及 physical energy。

对 frozen tilted projector，文档 161 式 (16)给

`||Pe||^2/||e||^2=400/401`.                       (20)

所以即使 tail与 coupling严格为零，仍可把任意大的 `400/401` physical mass放在
core。小 principal angle、small tail edge或small Feshbach correction都不能代替
core estimate。

## 4. 对广义结构定理的必要边界

### 定理 ACJ（noncircular core-input necessity）

设一类 component Grams在某个 fixed projector `P` 下对式 (18) 的 core
rank-one amplification封闭，并且 `Pe ne0`。则不存在只依赖

- `QGQ` 的 tail bounds；
- `PGQ` 的 coupling bounds；
- `P` 与某个 spectral projector的 angles；
- component-label algebra本身

的 uniform criterion能够推出 physical energies `<Ge,e>` 有界。

因此，任何适用于该类数据的 Weil center-line theorem若以 positive component
compression为接口，必须额外假设或证明一个直接约束 `PGe` 的 core input；等价地，
admissible arithmetic Grams必须不对式 (18)封闭。

#### 证明

定理 ACI 的 family `G_M` 对所有列出的 tail/coupling data给相同的零值，projector
也不变，而 physical energy随 `M` 无界。任何只读取这些 data的 uniform conclusion
均被该 family反驳。`□`

ACJ 是对 generalized structure theorem的公理审计，而不是说具体 zeta Grams真的
允许任意式 (18)。恰恰相反，成功证明必须利用 `G` 来自 primes、continuum、Gamma
与 convolution identities这一事实，证明这种 amplification不可能。

有限域 Weil proof中的 Hodge--Riemann relation正提供这种额外约束：primitive
intersection form的signature与 Frobenius similitude把 trace/core action锁在
polarization内，不能任意添加 positive rank-one mass。数域版本若只有 positive
Gram与近 rank-two geometry，而没有相应的 indefinite/Hodge relation，就尚未复制
Weil证明的关键步骤。

## 5. 定理 ACG 的重新解释

文档 161 定理 ACG仍是正确的充分条件，因为其式 (21)明确包含

`x^*Ax`                                           (21)

这一 core physical term。定理 ACI 说明不能从其余 terms自动删除式 (21)。所以 ACG
的未证部分不应笼统表述为“证明 tail很小”，而应拆成：

1. 对式 (6)--(7) 给 noncircular core Hodge bound；
2. 对式 (13)--(14) 给 tail Type I/II bounds；
3. 对 core--tail cross Grams给 bilinear bounds；
4. 把 continuum/Gamma/vector errors加入同一 Loewner enclosure。

第一项是决定性的。直接估计 `||Z_0||` 会再次包含 `19L`，可能只是重述目标。可行的
新输入必须具有至少一种形式：

- 一个 indefinite intersection form，使 large core mass按 Hodge index被正背景抵消；
- 一个 primes/Gamma-built positive current直接 majorize negative Hodge part，而非
  majorize完整 physical norm；
- 一条真正利用 Möbius/Type I/II算术性的 inequality，排除式 (18)方向；
- 一个 operator adjoint/similitude relation，从结构上迫使 core spectrum具有中心
  symmetry。

## 6. 下一步

式 (13)--(14)已经是完全具体的 tail targets，可以继续做 finite/dyadic audits；但在
投入大规模估计前，应优先回到文档 149 的 finite-trace negative Hodge index。目标是
构造一个 component matrix current `H(t)`，使：

1. its negative trace controls the scalar Abel zero obstruction；
2. frozen incidence transform把 negative directions限制到 tail residuals式 (13)--(14)
   与一个有限 core signature，而不是完整 `||L||^2`；
3. core signature由 arithmetic correspondence或 signed orbit Laplacian控制。

这才是从 finite-field Weil proof抽离出的关键结构：positive Gram负责Hilbert空间与
Bessel estimates，indefinite Hodge index负责禁止定理 ACI 的任意 core amplification。
