# Hard Vaughan gauge、cross-Gram 循环性与 factorization-fiber 障碍

文档 164 把 centered Vaughan 四分量精确压成 Type I/II 二通道，并把
`n<=U` 的低长度部分无条件移出 RH 强度预算。本笔记进一步展开这个 `2 x 2`
对象，得到一项必须先处理的 no-go 和一项新的正面结构：

1. 当 `V>=U` 时，两个 hard arithmetic channels 的和逐项就是
   `Lambda 1_(n>U)`，与 `V` 完全无关；改变 `V` 只是把同一个向量在两通道间
   作 gauge transfer；
2. Hadamard 旋转把二通道 Gram 精确化为 physical tail 与 primitive imbalance；
   所需 cross cancellation 加上四分之一 primitive energy，恒等于四分之一
   原目标能量。因此“先证明完整 cross Gram”若没有外部 signed relation，仍是
   原问题的改写；
3. raw 三因子 translation synthesis 有无界 exact-product fiber multiplicity，
   所以不能在 Möbius signs 求和前期待 uniform Bessel 常数；
4. 文档 166 将截断 Möbius defect 提升为由除数结构无条件构造的有限 Hodge realization：
   它是乘法 threshold simplicial complex 的 reduced Euler characteristic，亦是
   reduced combinatorial Laplacian 的 harmonic/heat supertrace；
5. 该 supertrace 可进一步局部化到一个乘法 boundary shell，并有显式 positive
   gcd-Gram 二阶矩。

这仍未证明 RH。本笔记删除一个循环的 proof target；文档 166 随后把 hard
Type II 中的 Möbius sign 写成不依赖零点的有限 Hodge 超迹。

## 1. Hard channels 的 cutoff gauge

沿文档 164，令

`a_U=mu_(<=U)*1`,

`b_U=mu_(>U)*1=epsilon-a_U`.                     (1)

取 `V>=U`，并记

`R_I=I_(U,V)-Lambda_(<=U)`,

`R_II=II_(U,V)`.                                 (2)

### 定理 ACV（hard-channel cutoff-gauge identity）[U]

逐整数精确成立

`R_I=Lambda_(U<n<=V)+a_U*Lambda_(>V)`,           (3)

`R_II=b_U*Lambda_(>V)`,                          (4)

以及

`R_I+R_II=Lambda_(>U)`.                          (5)

若 `V' >= V >= U`，置

`Delta_(V,V')=Lambda 1_(V<n<=V')`,               (6)

则

`R_I(U,V')-R_I(U,V)=b_U*Delta_(V,V')`,           (7)

`R_II(U,V')-R_II(U,V)=-b_U*Delta_(V,V')`.        (8)

所以 `V` 不是 physical cutoff，而是两通道间的精确 transfer gauge。

#### 证明

文档 164 给 `I=a_U*Lambda_(>V)+Lambda_(<=V)`，减去
`Lambda_(<=U)` 得式 (3)。又

`II=mu_(>U)*Lambda_(>V)*1=b_U*Lambda_(>V)`,       (9)

给式 (4)。由 `a_U+b_U=epsilon`，式 (3)--(4)相加就是式 (5)。把
`Lambda_(>V')=Lambda_(>V)-Delta_(V,V')` 代入式 (3)--(4)，得到

`Delta-a_U*Delta=b_U*Delta`                       (10)

及其相反数，即式 (7)--(8)。`□`

式 (5) 比 support-product gap 更强地说明：`V` 可以改善某一 diagonal channel，
但不能改变 hard physical vector；所有改善必须由另一 channel 或 cross entry 记账。

## 2. Hadamard Gram 正规形

令 `T` 是任意共同线性 synthesis，`c` 是相应 continuum vector。对实数
`alpha` 定义

`u=T(R_I)-alpha c`,

`v=T(R_II)-(1-alpha)c`,                           (11)

以及 physical/primitive 坐标

`W=u+v=T(Lambda_(>U))-c`,

`D=u-v`.                                         (12)

记 `G` 是 `u,v` 的 `2 x 2` Gram，并令

`H=2^(-1/2)[[1,1],[1,-1]]`.                      (13)

### 定理 ACW（two-channel Hadamard normal form）[U]

有精确恒等式

`HGH^*=(1/2)[[||W||^2,<W,D>],`

`              [<D,W>,||D||^2]]`.               (14)

特别地，若

`E=||W||^2`, `F=||D||^2`,

则

`||u||^2+||v||^2=(E+F)/2`,                       (15)

`2Re<u,v>=(E-F)/2`,                              (16)

`E=F+4Re<u,v>`.                                  (17)

#### 证明

Hadamard 变换把有序向量 `(u,v)` 送到 `(W/sqrt2,D/sqrt2)`，故其 Gram
正是式 (14)。取 trace 与式 (14)的 diagonal 差，得到式 (15)--(17)。`□`

### 推论 ACX（full cross-Gram target is algebraically circular）[U]

对任意 blocks `k` 与正 barrier `beta_k`，

`sum_k [Re<u_k,v_k>+||u_k-v_k||^2/4]/beta_k`

` =(1/4)sum_k||u_k+v_k||^2/beta_k`.               (18)

因此若把所需 signed cross estimate写成

`sum_k [Re<u_k,v_k>+||D_k||^2/4]/beta_k<=C`,      (19)

则式 (19)逐字就是目标 physical-energy bound除以四。仅控制 primitive energy
`F_k` 也不能控制 `E_k`：在 Hadamard coordinates 中，任意
`diag(E_k/2,F_k/2)>=0` 都给一个合法二通道 Gram。

这不排除从 Möbius 算术证明式 (19)；它排除的是把“cross Gram”本身当成已经比
原目标更弱的新结构输入。真正非循环的进展必须从同一个 positive Gram 外部导出
额外的 signed incidence、adjoint 或 Hodge-index relation。

## 3. Raw factorization 的 exact-collision 障碍

在 Type II 三因子展开中，令 index `j=(d,m,r)`，product map 为

`pi(j)=dmr`.                                      (20)

在 interval Hilbert space 中使用 normalized columns

`phi_j=h^(-1/2)pi(j)^(-itau)e_(log pi(j))`.       (21)

若 `pi(j)=pi(j')`，则 `phi_j=phi_(j')`，不仅是近似相关。

### 定理 ACY（factorization-fiber Bessel obstruction）[U]

令 `A z=sum_j z_j phi_j`。若

`R(n)=#{j:pi(j)=n}`,                              (22)

则

`||A||^2>=max_n R(n)`.                            (23)

对固定 `U,V` 的 Type II triples `d>U,m>V,r>=1`，式 (23)的右侧沿 product
range 无界。更具体地，取 `k` 个互异素数全都大于 `max(U,V)`，令其乘积为
`n`，则仅取 `m` 为其中一个素数、`d` 为其余素数的任意非空子集，就得到

`R(n)>=k(2^(k-1)-1)`.                             (24)

#### 证明

固定一个最大 fiber `J_n`，取 `z_j=R(n)^(-1/2)` 于该 fiber、其余为零。
则 `||z||=1`，而 `Az=sqrt(R(n))phi_n`，给式 (23)。上述 squarefree `n`
的每个选择都满足 `d>U,m>V`，且 `r=n/(dm)` 为正整数，给式 (24)。`□`

所以 theorem AAU 型 Bessel estimate 若在 raw triples 上对任意 coefficients
工作，必然支付 representation multiplicity。Möbius signs 必须先在每个 exact
product fiber 内求和；但求和后得到的正是式 (1)的 `a_U,b_U`。这解释了为什么
真正的新结构应落在 truncated Möbius defect，而不是未商化的 factor labels 上。
