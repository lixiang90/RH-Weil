# Shifted passivity、Abel completion 与 resonance defect

文档 131 把中心线纯性等价成 completed logarithmic derivative 的
positive-real/Pick-kernel 正性，并为 zeta 构造 sharp Chebyshev cutoff。
本节做两件事：

1. 引入 **passivity abscissa**，证明它精确等于最右 zero 离中心线的横向
   偏移；因此 zeta 在 shift `a=1/2` 已无条件拥有 genuine passive structure，
   RH 正是把该结构推进到 `a=0`；
2. 用 exponential Abel smoothing 替换 sharp cutoff。它使每个 arithmetic
   candidate 在整个目标半平面 holomorphic，并在固定低高度显著稳定 Pick
   defect；但新的 resonance audit 找到远离低高度的强负井，排除“加 `1/Y`
   scalar channel 即全局被动”的捷径。

## 1. Passivity abscissa

沿用文档 131：`Phi` 是 real-type、center-self-dual、order 至多 `1` 的 entire
function，

`Phi(-z)=(-1)^m Phi(z)`,                            (1)

且全部 zeros 位于某个有限竖直带。令

`F(z)=Phi'(z)/Phi(z)`,                              (2)

`Theta(Phi)=sup_(Phi(alpha)=0)|Re alpha|`.          (3)

对 `a>=0` 定义 shifted impedance

`F_a(z)=F(z+a)`, `Re z>0`.                         (4)

### 定理 XU（passivity-abscissa theorem）

下列条件等价：

1. `a>=Theta(Phi)`；
2. `F_a` 在右半平面 holomorphic 且 positive real；
3. kernel

   `K_a(z,w)=[F_a(z)+conj(F_a(w))]/[z+conj(w)]`     (5)

   在右半平面 positive semidefinite。

所以

`inf{a>=0:F_a is passive}=Theta(Phi)`.              (6)

特别地，全部 zeros 在中心轴当且仅当该 infimum 等于 `0`。

#### 证明

由 paired Hadamard product，`F_a` 是 central term 与所有 `+/-alpha` 对的
locally normally convergent sum：

`m/(z+a)+sum_alpha[1/(z+a-alpha)+1/(z+a+alpha)]`.   (7)

若 `a>=Theta(Phi)`，式 (7) 中每个 pole `r=alpha-a` 或 `r=-alpha-a`
都满足 `Re r<=0`。对一个这样的 pole，令 `G_r(z)=1/(z-r)`，直接计算

`[G_r(z)+conj(G_r(w))]/[z+conj(w)]`

` =1/[(z-r)(conj(w)-conj(r))]`

` +(-2Re r)/[(z-r)(conj(w)-conj(r))(z+conj(w))]`.  (8)

第一项是 rank-one Gram；第二项是非负常数乘 rank-one multiplier 与右半平面
Szego kernel 的 Schur product，仍半正定。对式 (7) 求和给条件 3，diagonal
给条件 2。

反之，若 `a<Theta(Phi)`，存在 zero `alpha` 满足 `Re alpha>a`；于是
`F_a` 在右半平面的 `z=alpha-a` 有 pole，不可能满足条件 2 或 3。`□`

这是一条 strip-valued Weil structure theorem：`a>0` 时得到 dissipative/passive
边界系统；只有 `a=0` 时退化成文档 131 的 conservative self-adjoint
center-line system。

## 2. zeta 与一般 Gamma--Euler 数据的无条件外层结构

对

`Phi_zeta(z)=xi(1/2+z)`,                            (9)

经典 critical-strip theorem 给

`Theta(Phi_zeta)<=1/2`.                            (10)

### 推论 XV（unconditional outer passive zeta package）

函数

`F_(1/2)(z)=xi'(1+z)/xi(1+z)`                     (11)

在 `Re z>0` 是 positive-real impedance，kernel (5) 正半定；而且该 germ 在
整个右半平面由绝对收敛 Euler logarithmic derivative、Gamma factor 与已知
pole cancellation定义。进一步，

`RH iff Theta(Phi_zeta)=0`

`   iff F_a is passive for every a>0`.              (12)

#### 证明

式 (10) 与定理 XU 给第一项。`s=1+z` 满足 `Re s>1`，故 prime-power series
绝对收敛。最后的等价仍由定理 XU。`□`

更一般地，若一个 self-dual completed Gamma--Euler function 的 nontrivial
divisor 已知位于 `|Re(s-c/2)|<=A`，则中心化 logarithmic derivative 在每个
shift `a>=A` 都产生 passive Pick package。若其 Euler series 在该外层绝对
收敛，这个 package 由 arithmetic coefficients 独立构造。把 passivity
abscissa 从已知 `A` 压到 `0` 就是相应 GRH；每个严格改善的 `a<A` 都会给出
新的全局 zero-free strip，而不必一步跳到完整 GRH。

## 3. Exponential Abel arithmetic completion

对 zeta 令 `s=1/2+z`、`Y>0`，定义

`S_Y(s)=sum_(n>=2)Lambda(n)n^(-s)e^(-n/Y)`,         (13)

`I_Y(s)=int_1^infinity x^(-s)e^(-x/Y)dx`

`      =Y^(1-s)Gamma(1-s,1/Y)`.                   (14)

`S_Y` 与 `I_Y` 都是 `s` 的 entire functions。去掉完成函数中单独的
`1/(s-1)` 后，定义

`F_Y(z)=1/s-(1/2)log pi+(1/2)psi(s/2)`

`                         +I_Y(s)-S_Y(s)`.          (15)

每个 `F_Y` 都在 `C_+` holomorphic，且只使用 prime powers、Gamma data 与
连续 PNT density；没有 zeta zeros 或 zeta continuation作为输入。

### 定理 XW（Abel normal-family criterion）

下列条件等价：

1. RH；
2. `{F_Y:Y>=1}` 在 `C_+` locally bounded；
3. 当 `Y->infinity` 时，`F_Y` locally uniformly 收敛到一个 passive
   impedance；
4. `F_Y` locally uniformly 收敛到 `xi'/xi(1/2+z)`，且相应 Pick kernels
   locally converges to positive kernels。

#### 证明

在 `Re s>1`，dominated convergence 给

`S_Y(s)->-zeta'(s)/zeta(s)`,

`I_Y(s)->1/(s-1)`,                                 (16)

故 `F_Y` 收敛到 arithmetic impedance germ。

若 RH 成立，写 `E(x)=psi(x)-x`，使用经典等价 bound

`E(x)=O(x^(1/2)log^2 x)`.                           (17)

对 `S_Y-I_Y=int x^(-s)e^(-x/Y)dE(x)` 作 Stieltjes partial
summation。在任意 compact `Re s>=1/2+delta` 上，导数产生两项

`O((1+|s|)x^(-1-delta)log^2 x e^(-x/Y))`,

`O(Y^(-1)x^(-delta)log^2 x e^(-x/Y))`.             (18)

第一项有与 `Y` 无关的 integrable majorant，第二项积分为
`O(Y^(-delta)log^2 Y)`；因此 locally uniform convergence 成立。极限由
文档 131 定理 XQ passive。

反之，local boundedness 与每个 `F_Y` 的 holomorphy 给 normal family；
式 (16) 在非空开集确定唯一极限。Vitali/Montel 迫使 arithmetic germ
holomorphically 延拓到整个 `C_+`，从而 `xi'/xi` 在其中没有 zero-poles。
functional equation 再排除左侧 zeros，得到 RH。`□`

同一证明适用于 polynomial-growth logarithmic coefficients `b(n)`：把
式 (14) 换成已知右侧 poles 所对应的连续 densities。于是定理 XW 是一条
广泛 Gamma--Euler 数据的 filtered passive structure theorem。

## 4. Finite passive completion charge

给定右半平面有限点集 `Z={z_1,...,z_d}` 和 impedance values `F(z_j)`，令

`K=[(F(z_j)+conj(F(z_k)))/(z_j+conj(z_k))]`,        (19)

`H=[2/(z_j+conj(z_k))]`.                            (20)

`H` 是正定 Szego Gram。加入 real constant channel `c` 会把 `K` 变成
`K+cH`。

### 定理 XX（least scalar passive completion）

有限点集上的最小 scalar completion 恰为

`c_Z(F)=max(0,-lambda_min(K,H))`,                   (21)

其中 `lambda_min(K,H)` 是 generalized Hermitian pencil
`Kv=lambda Hv` 的最小 eigenvalue。特别地，`K+c_ZH>=0`，任何更小
`c>=0` 都失败。

#### 证明

取 `H=LL^*`。congruence 给

`K+cH>=0 iff L^(-1)KL^(-*)+cI>=0`.                 (22)

右侧成立当且仅当 `c` 不小于 normalized matrix 最负 eigenvalue 的绝对值，
即式 (21)。`□`

若 RH 成立，定理 XW 说明对每个固定有限 `Z`，

`c_Z(F_Y)->0`.                                     (23)

反向要推出 RH，必须对半平面 exhaustion 给出 uniform completion/normality；
只在一个固定有限点集上有式 (23) 不够。

## 5. Abel 与 sharp cutoff 的数值审计

取与文档 131 相同的三个点

`Z={0.1, 0.3+i, 0.7-1.4i}`.                       (24)

prime sum 截到 `N=40Y`。由 `Lambda(n)<=log n` 和 integrand 单调性，遗漏
tail 满足

`|tail|<=int_N^infinity log(x)x^(-Re s)e^(-x/Y)dx`. (25)

程序把 entrywise bounds 转成 Pick perturbation 的 maximum-row-sum bound，
再用 Weyl inequality enclosure eigenvalues。结果为：

| `Y` | minimum Pick eigenvalue | scalar completion `c_Z` | operator tail bound |
|---:|---:|---:|---:|
| 3 | `-2.6199` | `0.26083` | `4.1e-17` |
| 10 | `-0.91809` | `0.094324` | `8.2e-17` |
| 30 | `-0.30285` | `0.033368` | `1.5e-16` |
| 100 | `-0.082112` | `0.010229` | `2.8e-16` |
| 300 | `-0.025302` | `0.0034306` | `4.9e-16` |

在这个固定低高度 set 上，Abel completion charge 非常接近 `1/Y`，并稳定趋零。
相比之下，sharp cutoff 的 `c_Z` 在

`0.0362, 0.0397, 0.0389, 0, 0.0284`               (26)

间非单调跳动。Abel smoothing 确实移除了 fixed-window Gibbs 型振荡。

但是这不是全局 passivity。取

`Y=100`, `z=0.005+66i`, `N=4000`,                 (27)

得到

`F_Y(z)=-0.7783629333+0.1434175429i`,              (28)

而式 (25) 的 prime tail bound 仅 `5.30e-17`。即使加入低高度提示的
`1/Y` channel，实部仍为 `-0.76836`。同一粗网格还在 heights
`42,49,52,66` 找到负 resonance wells。直接使用完成 zeta 的数值值为

`F(z)=0.01193257+0.65286988i`,                     (29)

说明这些负井来自有限 Abel prime resonance，随后才在更大 `Y` 的全球相消中
消失。式 (28)--(29) 是高精度、带解析 tail majorant 的数值诊断，但不是
interval proof或 RH 证据。

因此以下捷径被 audit 排除：

`F_Y + 1/Y is passive on all C_+`.                 (30)

固定低高度、固定点集的 vanishing completion 不能替代全半平面 normality。

## 6. 实现与下一输入

新增实现：

- `stable_pole_passive_impedance_certificate`：定理 XU 的 finite rational
  resolvent/Szego Gram 分解；
- `zeta_abel_prime_impedance`：式 (13)--(15) 与严格 scalar tail majorant；
- `zeta_abel_impedance_pick_certificate`：Pick spectrum、entrywise error和 Weyl
  operator enclosure；
- `positive_real_completion_certificate`：定理 XX 的 Szego-normalized
  minimal completion charge。

新的存在性边界可以写成

`unconditional shifted passivity at a=1/2`

` -> shrink passivity abscissa a`

` -> control Abel resonance wells uniformly`

` -> passive limit at a=0`

` -> RH`.                                         (31)

下一步不应继续试 scalar global counterterm。式 (28) 表明需要把 Abel prime
polynomial 的负 resonance wells 当成移动的有限 Hodge core：利用文档
018--024 的 packing、modulated-prolate 与 block-large-sieve machinery控制其
余空间，再在 core 上计算 Szego-normalized completion/Feshbach matrix。目标是
证明 core 外 `c->0`，同时给 core rank与耦合的 cofinal bound。
