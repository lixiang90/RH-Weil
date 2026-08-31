# Block weight-purity overlap 与 classical cancellation audit

文档 125 把 external period 的平方写成 response/probe dual representers 的 normalized
correlation。本节把 observation polarization 分成 positive blocks，并抽取一个最接近
Weil 权重纯性的充分结构：若 response harmonic class 与 external Tate probe 的能量
落在不相交的 weight blocks，则二者自动正交；一般 correlation 由两种正能量分布的
Hellinger/Bhattacharyya overlap 控制。

这给出广泛 positive Hodge packages 的 block-purity centerline theorem。经典
Möbius--Farey audit 则显示 dyadic energy distributions 高度重叠，真实小 correlation
主要来自 block 内不对齐与跨 block signed cancellation。因此该结构解释了 Weil
几何为何有效，却尚不能关闭经典 RH。

## 1. Positive Hodge block decomposition

令

`W=sum_(j in J)W_j>0`, `W_j>=0`,                 (1)

并置

`x_D=W^(-1)D`, `x_q=W^(-1)q`.                    (2)

沿用 capacities

`C_D=x_D^*Wx_D`, `C_q=x_q^*Wx_q`,                (3)

并定义 normalized block masses

`d_j=x_D^*W_jx_D/C_D`,                            (4)

`e_j=x_q^*W_jx_q/C_q`.                            (5)

它们都是 probability vectors：`d_j,e_j>=0` 且各自求和为 `1`。定义 normalized
block current 与 local coherence

`r_j=x_D^*W_jx_q/sqrt(C_DC_q)`,                  (6)

`gamma_j=|r_j|^2/(d_je_j) in [0,1]`              (7)

（零 denominator 时取零）。全局 normalized correlation 为

`rho=sum_jr_j`, `beta_ext=|rho|^2`.               (8)

### 定理 WW（block Hodge overlap bound）

令 Bhattacharyya overlap

`B(d,e)=sum_j sqrt(d_je_j)`.                       (9)

则

`beta_ext<=B(d,e)^2<=1`.                          (10)

等价地，若 Hellinger distance 采用

`H^2(d,e)=1-B(d,e)`,                              (11)

则 `beta_ext<=[1-H^2(d,e)]^2`。

#### 证明

在 semidefinite form `W_j` 中用 Cauchy--Schwarz，

`|r_j|<=sqrt(d_je_j)`.                            (12)

再用 triangle inequality 对式 (8) 求和得到第一不等式。probability vectors 的
Cauchy--Schwarz 给 `B(d,e)<=1`。`□`

如果 `d,e` 支撑不交，则 `B=0`，response 与 probe 精确正交。这正是 abstract
weight purity：不同 weights 的 harmonic classes 在 polarization 下没有 mixed period。

## 2. Local coherence 与 signed hierarchy

仅比较 masses 会丢掉同一 block 内的方向信息。由式 (7)，

`|r_j|=sqrt(d_je_jgamma_j)`.                      (13)

### 定理 WX（mass--coherence--phase hierarchy）

有 sharp hierarchy

`beta_ext=|sum_jr_j|^2`

` <=[sum_j sqrt(d_je_jgamma_j)]^2`

` <=[sum_j sqrt(d_je_j)]^2<=1`.                  (14)

第一层松弛只删除跨 block phases；第二层再删除 block 内 response/probe angle。

#### 证明

第一不等式是 triangle inequality，式 (13) 给 middle expression；因
`0<=gamma_j<=1` 得第二不等式；最后应用定理 WW。`□`

因此 failure 可以被精确分类为三层：weight-support overlap、local Hodge
coherence、global signed phase alignment。

## 3. Block masses 是 positive capacity susceptibilities

对任一 covector `f` 与 block `W_j` 定义

`C_(f,j)(t)=f^*(W+tW_j)^(-1)f`, `t>=0`.           (15)

### 定理 WY（positive susceptibility recovery）

有

`-C_(f,j)'(0)=x_f^*W_jx_f>=0`.                   (16)

所以 `d_j,e_j` 分别由 response/probe positive-update capacity derivatives 给出。
对 real data，block current满足

`4x_D^*W_jx_q`

` =-C_(D+q,j)'(0)+C_(D-q,j)'(0)`.                (17)

每个 capacity 又是 positive determinant quotient

`C_(f,j)(t)=det(W+tW_j+ff^*)/det(W+tW_j)-1`.      (18)

故式 (14) 的 mass bound 与 local-coherence bound 都能由 positive matrices 的
susceptibilities/determinants恢复。

#### 证明

对 inverse 求导给

`d/dt (W+tW_j)^(-1)|_(t=0)=-W^(-1)W_jW^(-1)`.   (19)

两侧配对 `f` 得式 (16)。把 `f=D+q,D-q` 展开并相减得式 (17)。式 (18) 是
matrix determinant lemma。`□`

complex case 另用 `D+/-iq` 的两次 quadrature恢复 imaginary part。

## 4. Block-purity centerline theorem

令

`A_N=sum_j sqrt(d_(N,j)e_(N,j)gamma_(N,j))`.       (20)

### 定理 WZ（block-purity Weil criterion）

在文档 124--125 的 setup 中，

`L_1(N)<=sqrt(C_(q,N)/C_(D,N)) A_N`

`          +Delta_(alt,N).`                       (21)

若

`c_1+|target|[sqrt(C_q/C_D)A_N+Delta_alt]`

` =o(sqrt(log N)/loglog(3N)),`                    (22)

则 fixed principal strata 为 `o(1)`；连同完整 polarized Weil package 与总尾
条件即推出中心线结论。

把 `A_N` 换成更粗的 `B(d_N,e_N)` 仍是充分条件。特别地，在 genuine weight
decomposition 中若 response 与 external probe 渐近支撑分离得足够快，则中心线
结论随之成立。

#### 证明

定理 WT 给 `L_ext=sqrt(C_q/C_D)|rho|`；定理 WX 给 `|rho|<=A_N`。再用
`L_1=L_ext+Delta_alt` 得式 (21)，最后应用定理 WE。`□`

定理 WZ 抽取了 Weil 猜想证明中“purity + polarization implies orthogonality”的
定量版本：不要求先构造一个 global Frobenius operator，只需可验证的 positive
Hodge blocks 与不同 classes 的 weight-energy separation。

## 5. Möbius--Farey dyadic specialization

使用文档 122 的 exact observation factorization `W=O^*O`。将 cell mean row 与
同一 integer cell 的 variance row合并，再按

`{0},[1,1],[2,3],[4,7],...`                       (23)

分成 dyadic blocks。这样式 (1) exact成立，所有 masses、currents 与 coherences
都是有限可计算的 positive cell quantities。

下表中 `BC^2` 是定理 WW 上界，`local^2` 是定理 WX middle upper，`signed` 是
`|sum r_j|/sum|r_j|`。

| `N` | `R` | exact `rho^2` | `local^2` | `BC^2` | `signed` | `H^2` |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 2 | 0.3159 | 0.800 | 0.939 | 0.628 | 0.031 |
| 16 | 2 | 0.2822 | 0.766 | 0.908 | 0.607 | 0.047 |
| 32 | 2 | 0.2991 | 0.726 | 0.859 | 0.642 | 0.073 |
| 64 | 2 | 0.1125 | 0.467 | 0.645 | 0.491 | 0.197 |
| 100 | 2 | 0.00909 | 0.094 | 0.336 | 0.311 | 0.420 |
| 8 | 3 | 0.00837 | 0.210 | 0.833 | 0.200 | 0.087 |
| 16 | 3 | 0.01579 | 0.155 | 0.744 | 0.319 | 0.137 |
| 32 | 3 | `8.89e-4` | 0.286 | 0.833 | 0.0557 | 0.088 |
| 64 | 3 | 0.2048 | 0.431 | 0.728 | 0.689 | 0.147 |
| 100 | 3 | 0.6009 | 0.845 | 0.915 | 0.843 | 0.043 |

dyadic mass distributions 明显不分离：`BC^2=0.34--0.94`。local coherence 可
改善上界，但在 `N=32,R=3` 仍由 `0.833` 只降至 `0.286`，离 exact
`8.89e-4` 很远；主要节省来自 signed block cancellation `0.0557`。因此经典
样本不支持单靠 positive weight-support separation 证明 RH。需要保留 arithmetic
phases，或寻找比 spatial dyadic cells 更接近真正 Frobenius weights 的 block
decomposition。

## 6. 计算实现

新增：

- `dual_observation_block_overlap_certificate`：对任意 exact observation factorization
  与 row partition计算 block masses、currents、local coherences、Hellinger overlap
  及两级 correlation/leverage upper；
- `mobius_endpoint_external_dyadic_overlap_certificate`：构造 unit-cell mean/variance
  dyadic blocks并应用前者。

回归核对 observation Gram、两组 probability masses、block-current求和及完整
hierarchy `exact<=local coherence<=mass overlap`，tolerance 为 `1e-43`。
