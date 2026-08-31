# Positive-real 边界阻抗与 determinant-line anomaly

文档 130 把临界 prime operator 的缺口压缩为 `det_3` 删除的线性、二次
traces。本节继续追问这些 traces 应当属于什么全局对象。答案分成两层：

1. 它们不能延拓为一个无零、单值的普通 scalar counterterm；其 logarithmic
   connection 必须承载 zeta 的完整 divisor；
2. 对任意合适的自对偶完成函数，中心线纯性等价于中心化 logarithmic
   derivative 是右半平面的 **positive-real/passive impedance**。相应 Pick kernel
   是一个精确正 Gram，给出 Weil--Hodge 正性的边界系统版本。

这产生一个新的广义结构定理，也给 zeta 一个完全由 `Lambda(n)`、Gamma 数据与
连续 pole tail 构造的候选逼近。它尚不证明 RH：缺失估计变成该候选族在整个
右半平面的局部一致有界性；本节证明这个估计本身恰有 RH 强度。

## 1. 自对偶 entire divisor

令 `Phi` 是阶数至多 `1` 的非零 entire function，满足

`Phi(conj(z))=conj(Phi(z))`,                         (1)

`Phi(-z)=(-1)^m Phi(z)`,                            (2)

其中 `m=ord_(z=0)Phi`。令

`F(z)=Phi'(z)/Phi(z)`.                              (3)

由于零点在 `alpha -> -alpha` 下配对，Hadamard factors 可成对组合。阶数至多
`1` 保证

`Phi(z)=C z^m product_alpha(1-z^2/alpha^2)`,         (4)

其中每个 `+/-alpha` 对只取一次，且平方 factors 局部一致收敛。可能剩余的
zero-free exponential 是 `exp(az+b)`；式 (2) 迫使 `a=0`，故已吸收到 `C`。

## 2. Positive-real Weil 结构定理

记右半平面 `C_+={z:Re z>0}`，并定义 kernel

`K_F(z,w)=[F(z)+conj(F(w))]/[z+conj(w)]`.            (5)

### 定理 XQ（positive-real/passive Weil theorem）

在上述假设下，下列条件等价：

1. `Phi` 的全部非零 zeros 位于虚轴；
2. `F` 在 `C_+` holomorphic 且 `Re F(z)>=0`；
3. `K_F` 在 `C_+` positive semidefinite，即任意有限点集的 Pick matrix
   `[K_F(z_j,z_k)]` 都半正定；
4. 存在 `R_+` 上的正离散测度 `mu`，满足

   `int (1+t^2)^(-1)dmu(t)<infinity`,                (6)

   且

   `F(z)=m/z+int_(0,infinity) 2z/(z^2+t^2)dmu(t)`.  (7)

`mu` 在 `gamma>0` 的质量恰为虚轴 zero `i gamma` 的 multiplicity。因此
式 (7) 不仅给中心线，也按质量恢复 divisor multiplicity。

#### 证明

若条件 1 成立，式 (4) 变成

`Phi(z)=C z^m product_(gamma>0)(1+z^2/gamma^2)^(m_gamma)`.

逐项 logarithmic differentiation 得

`F(z)=m/z+sum_(gamma>0)m_gamma`

`      *[1/(z-i gamma)+1/(z+i gamma)]`.             (8)

`sum m_gamma/(1+gamma^2)<infinity` 来自 entire order；成对和为
`2z/(z^2+gamma^2)`，故局部一致收敛。对 `Re z>0`，每项
`1/(z-i gamma)` 与 `1/(z+i gamma)` 的实部均为正，得到条件 2 与式 (7)。

进一步，对一个 spectral atom `lambda in R`，有精确恒等式

`{(z-i lambda)^(-1)+(conj(w)+i lambda)^(-1)}`

` /(z+conj(w))`

` =1/[(z-i lambda)(conj(w)+i lambda)].              (9)

中心 atom 同理给 `1/[z conj(w)]`。所以

`K_F(z,w)=m/[z conj(w)]`

` +sum_gamma m_gamma{1/[(z-i gamma)(conj(w)+i gamma)]`

`                    +1/[(z+i gamma)(conj(w)-i gamma)]}`. (10)

右侧是 resolvent feature vectors 的 Gram，故条件 3 成立。

条件 3 的 diagonal 给

`K_F(z,z)=Re F(z)/Re z>=0`,                          (11)

故推出条件 2。若条件 2 成立，`F=Phi'/Phi` 在整个 `C_+` holomorphic，所以
`Phi` 在其中没有 zero。式 (2) 把任何左半平面 zero 映到右半平面；于是全部
zeros 只能在虚轴，得到条件 1。条件 1 已构造条件 4，而条件 4 逐项使用式 (9)
又给条件 3。`□`

这是文档 001 定理 E 的 boundary-transfer 版本。虚轴上的 self-adjoint
frequency `gamma` 对应中心线上的 generator eigenvalue `1/2+i gamma`；
positive-real impedance 与 Pick Gram 扮演正极化。与“先列出 zeros 再造
Hilbert 空间”的循环构造不同，有效应用必须从 Euler/Gamma 数据独立给出
`F` 的 passive continuation。

非自对偶数据可先把 `Lambda(s,pi)` 与 `Lambda(s,pi^vee)` 取乘积。在通常
functional equation 与 real-type 条件下，中心平移后的乘积满足式 (1)--(2)；
乘积的全部 zeros 在中心线会逐因子推出 GRH。

## 3. zeta 的 arithmetic impedance germ

取

`xi(s)=(1/2)s(s-1)pi^(-s/2)Gamma(s/2)zeta(s)`,      (12)

`Phi(z)=xi(1/2+z)`.                                 (13)

`Phi` 是 real even entire function of order `1`。在 `Re z>1/2`，令
`s=1/2+z`，Euler series 绝对收敛并给

`F_zeta(z)=Phi'(z)/Phi(z)`

` =1/s+1/(s-1)-(1/2)log pi+(1/2)psi(s/2)`

`  -sum_(n>=2)Lambda(n)n^(-s)`.                    (14)

右侧完全由 prime powers 与 archimedean data 定义，不使用 zeros。

### 推论 XR（passive arithmetic criterion for RH）

RH 等价于式 (14) 的 arithmetic germ 延拓成 `C_+` 上的 holomorphic
positive-real function；也等价于其 kernel (5) 在 `C_+` 的全部有限 Pick
matrices 半正定。

#### 证明

完成 zeta 的解析延拓给式 (14) 唯一的 meromorphic continuation
`xi'/xi(1/2+z)`。应用定理 XQ。`□`

这里必须要求整个半平面及全部 Pick matrices。只在某些竖条或高度证明
`Re xi'/xi>0` 不排除别处的 off-line zero；近期关于 scalar real-part positivity
区域的工作也明确研究了这种局部现象，而没有声称得到全局 kernel positivity。

## 4. `det_3` anomaly 的 connection 与 divisor

沿用文档 130：

`Delta_3(s)=product_p(1-p^(-s))exp[p^(-s)+p^(-2s)/2]` (15)

在 `Re s>1/3` holomorphic 且 zero-free。令

`C_X(s)=P_X(s)+P_X(2s)/2`.                          (16)

有限 prime cutoff 下定义三个 currents：

`J_(<=2,X)(s)=-C_X'(s)`

` =sum_(p<=X)log p[p^(-s)+p^(-2s)]`,               (17)

`J_(>=3,X)(s)=(log Delta_(3,X))'(s)`

` =sum_(p<=X)log p p^(-3s)/(1-p^(-s))`,            (18)

`J_(Euler,X)(s)=-zeta_X'(s)/zeta_X(s)`

` =sum_(p<=X)log p p^(-s)/(1-p^(-s))`.             (19)

逐 prime 的几何级数给精确 identity

`J_(Euler,X)=J_(<=2,X)+J_(>=3,X)`.                 (20)

式 (18) 在 `Re s>1/3` 正常收敛；临界带的 singular/global data 全部留在
式 (17) 的 continuation。

### 定理 XS（anomaly connection carries the full divisor）

在 `Re s>1` 令

`A(s)=zeta(s)^(-1)/Delta_3(s)=exp[-C(s)]`.          (21)

把左侧用 zeta 的已知 meromorphic continuation 延拓到
`{Re s>1/3}`。则：

1. 若 `rho` 是 zeta 的 `m_rho` 重 zero，

   `ord_rho A=-m_rho`,                              (22)

   且 logarithmic connection `omega=d log A` 在 `rho` 的 residue 是
   `-m_rho`；
2. `ord_(s=1)A=1`；
3. 在不包围其它 divisor 的小圈上，low-trace potential 满足

   `oint_rho dC=2pi i m_rho`.                       (23)

所以 missing low traces 不能是全局 single-valued holomorphic potential，
也不能由一个 zero-free normal counterterm承担。它必须成为 determinant line
section / logarithmic connection，或由等价的 nonlocal cohomology 实现。

#### 证明

`Delta_3` 在该区域 zero-free，故不改变任何 local order。`zeta^(-1)` 在
`m_rho` 重 zero 处有 `m_rho` 阶 pole，在 `s=1` 有一阶 zero，给式
(22) 与第二项。logarithmic derivative 的 residue 等于 meromorphic function
的 local order。由 `d log A=-dC` 与 residue theorem 得式 (23)。`□`

定理 XS 把文档 130 的 accountability 要求进一步刚性化：anomaly 不只是
“数值上补回两个 traces”，而是必须有正确的整数 residues、monodromy 与
determinant-line divisor。

## 5. 一个不使用 zeros 的候选 passive completion

令

`S_X(s)=sum_(n<=X)Lambda(n)n^(-s)`.                 (24)

定义 `z=s-1/2 in C_+` 上的 half-plane-holomorphic candidate

`F_X(z)=1/s-(1/2)log pi+(1/2)psi(s/2)`

`       +(1-X^(1-s))/(s-1)-S_X(s)`.                (25)

商在 `s=1` 的值按解析延拓取 `log X`。因此每个 `F_X` 在整个 `C_+`
holomorphic，并且只使用有限 von Mangoldt 数据、Gamma factor 与 PNT 主项的
连续 tail。对 `Re s>1`，

`S_X(s)+X^(1-s)/(s-1) -> -zeta'(s)/zeta(s)`,       (26)

故 `F_X->F_zeta`。

### 定理 XT（filtered passive-completion criterion）

下列条件等价：

1. RH；
2. `{F_X}` 在 `C_+` locally bounded；
3. `F_X` 在 `C_+` locally uniformly 收敛到一个 passive impedance `F`；
4. 对每个有限点集，`K_(F_X)` 收敛到一个 positive semidefinite matrix，且
   `{F_X}` locally bounded。

在这些条件下 `F=F_zeta`，其 GNS/resolvent measure 的 atoms 恰为 zeta
critical ordinates，质量为 zero multiplicities。

#### 证明

RH 给经典 bound

`psi(x)-x=O(x^(1/2)log^2 x)`.                       (27)

对式 (24) 作 partial summation，连续主项恰由式 (25) 的
`X^(1-s)/(s-1)` 消去；式 (27) 使余项在每个 `Re s>=1/2+delta`
一致 Cauchy。因此 `F_X` locally uniformly 收敛到式 (14)。定理 XQ 说明极限
passive，给 3--4 与 2。

反之，2 与每个 `F_X` 的 holomorphy 给 normal family。它们已在非空开集
`Re z>1/2` 收敛到 arithmetic germ；Vitali/Montel 与 identity theorem 迫使
整个序列在 `C_+` locally uniformly 收敛到该 germ 的 holomorphic
continuation。于是 `xi'/xi(1/2+z)` 在 `C_+` 无 pole，即 xi 没有中心线右侧
zero；functional equation 排除左侧 zero，得到 RH。条件 3 或 4 显然包含
条件 2，并由极限 kernel与定理 XQ给同一结论。`□`

这是一个具体的“结构存在性”尝试：对象与 cutoff 都已无条件构造，待证项不再是
抽象 Hilbert 空间存在，而是式 (25) 的 normal-family bound。定理 XT 同时警告：
这个 bound 已有 RH 全强度，不能当作普通 compactness。

## 6. 有限 audit

代码实现：

- `prime_regularization_anomaly_current_certificate` 精确检查式 (20)；
- `centerline_passive_impedance_certificate` 从有限中心线 frequencies 构造
  式 (8)、Pick matrix与式 (10) 的 resolvent Gram；
- `positive_real_pick_gram` 检查任意 finite impedance data；
- `zeta_renormalized_prime_impedance` 实现式 (25)，并在 `s=1` 使用解析值；
- `zeta_renormalized_impedance_pick_certificate` 计算有限 Pick spectra。

取点

`z=(0.1, 0.3+i, 0.7-1.4i)`.                        (28)

式 (25) 的最小 Pick eigenvalue 随 cutoff 为：

| `X` | minimum Pick eigenvalue |
|---:|---:|
| 30 | `-0.3214` |
| 100 | `-0.08646` |
| 300 | `-0.3533` |
| 1,000 | `+0.00597` |
| 3,000 | `-0.2502` |

有限阶段既不正也不单调；`X=1000` 的偶然正性不能外推。直接用完成 zeta 数值
求出的极限 Pick eigenvalues约为

`2.62e-7, 2.32e-4, 1.39e-1`,                       (29)

与被动极限一致，但这里只是转录检查，不是 RH 证据。真正需要的是对任意 compact
set 的统一 bound，而非固定点或固定 cutoff 的数值正性。

## 7. 研究边界与下一输入

本节新增的结构关系是

`prime/Gamma germ + continuum pole cancellation`

` -> normal passive completion`

` -> positive Pick/Weil Gram`

` -> self-adjoint boundary frequency measure`

` -> center-line divisor`.                         (30)

对 classical zeta，第一行的 finite candidates 已存在；第二箭头的 normality
仍未证明。下一步应针对式 (25) 研究 dyadic/smoothed cutoffs：sharp cutoff 的
finite Pick negativity表明逐 cutoff positivity不可行，可能需要 Cesaro/Abel
averaging、prime-resonance block large sieve，或把 kernel defect限制在随 cutoff
移动的有限 Hodge core 中。任何方案还必须满足定理 XS 的 integer-residue
determinant-line compatibility。
