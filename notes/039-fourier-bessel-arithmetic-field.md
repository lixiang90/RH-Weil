# 单位区间 Fourier--Bessel 算术场

文档 038 的 Hodge 坐标看似是半线上的奇异 current pairing。本笔记通过
`z=x^(-sigma)` 把它化成单位区间上标准 Fourier--Bessel 展开。算术对象
变成一个明确的径向场；Hodge 能量就是普通 Parseval norm。有限素数截断
则给出单调、可计算的 Bessel 部分和证书。

## 1. 规范算术场

固定 `sigma>0`，令

`nu=1/(2sigma)`, `z=x^(-sigma)`.                     (1)

定义单位区间上的 Chebyshev 场

`F_sigma(z)=z^nu[psi(z^(-1/sigma))-z^(-1/sigma)]`,

`0<z<=1`.                                             (2)

由于 `z^nu=x^(-1/2)`，它就是文档 035 的中心化信号在紧化坐标中的表达。

### 命题 FK（Abel energy is a radial L2 norm）

有精确恒等式

`I_sigma=2int_0^1 z|F_sigma(z)|^2dz`.                (3)

#### 证明

由 `dz=-sigma x^(-sigma-1)dx`，

`2int_0^1 z^(2nu+1)|psi(x)-x|^2dz`

`=2sigma int_1^infinity |psi(x)-x|^2`

`                         x^(-2sigma-2)dx`,           (4)

右边正是 `I_sigma`。`□`

所以 `I_sigma` 的临界性完全位于 `z=0`，即算术无穷远被压缩成的单个边界
点。

## 2. Fourier--Bessel 基与 Hodge 坐标

令 `j_n=j_(nu,n)`，并定义

`u_(n,sigma)(z)=sqrt(2)/|J_(nu+1)(j_n)| J_nu(j_n z)`. (5)

这是 `L^2((0,1),z dz)` 的规范正交基。记

`b_(n,sigma)=int_0^1 z F_sigma(z)`

`                         conjugate(u_(n,sigma)(z))dz`. (6)

### 定理 FL（Hodge coordinates are Fourier--Bessel coefficients）

文档 038 的 arithmetic coordinate 满足

`A_(n,sigma)=sqrt(sigma)j_n b_(n,sigma)`.            (7)

因此

`|A_(n,sigma)|^2/lambda_(n,sigma)=2|b_(n,sigma)|^2`. (8)

#### 证明

以分布积分分部，

`A_(n,sigma)=<dE,e_(n,sigma)>`

`=-int_1^infinity E(x)e_(n,sigma)'(x)dx`.            (9)

在 `z` 坐标中，文档 038 式 (4) 为

`e_(n,sigma)=C_n z^(nu+1)J_(nu+1)(j_nz)`,

`C_n=sqrt(2sigma)/|J_(nu+1)(j_n)|`.                 (10)

用 Bessel 导数恒等式得

`d e_(n,sigma)/dz=C_nj_nz^(nu+1)J_nu(j_nz)`.        (11)

式 (9) 换元并使用 `E=z^(-nu)F_sigma`，得到

`A_(n,sigma)=C_nj_n int_0^1 zF_sigma(z)J_nu(j_nz)dz`

`=sqrt(sigma)j_n b_(n,sigma)`.                      (12)

再代入 `lambda_n=(sigma/2)j_n^2` 得式 (8)。`□`

## 3. Parseval 中心线判据

### 定理 FM（Fourier--Bessel Hodge criterion）

对固定 `sigma>0`，以下条件等价：

1. `I_sigma<infinity`；
2. `F_sigma in L^2((0,1),z dz)`；
3. `sum_n |b_(n,sigma)|^2<infinity`。

在这些条件下

`I_sigma=2sum_(n>=1)|b_(n,sigma)|^2`.                (13)

因此 RH 等价于式 (13) 对每个 `sigma>0` 有限。

#### 证明

命题 FK 给 1 与 2；标准 Fourier--Bessel Parseval 定理给 2 与 3 以及
`int z|F|^2=sum|b_n|^2`。乘以二得到式 (13)。最后应用文档 035 推论 EQ。
`□`

FM 表明 Bessel 谱化没有暗中假设零点：它只是把一个由素数定义的径向场
放入固定正交基。中心线问题是该场在所有紧化尺度上的边界可积性。

## 4. 有限素数的 Bessel 证书

对整数 `X>=2` 令

`F_(sigma,X)(z)=F_sigma(z)1_(z>=X^(-sigma))`.         (14)

其系数记为 `b_(n,sigma;X)`。换回 `x` 后有显式有限积分

`b_(n,sigma;X)=sqrt(2)sigma/|J_(nu+1)(j_n)|`

` int_1^X [psi(x)-x]x^(-2sigma-3/2)`

`                         J_nu(j_nx^(-sigma))dx`.     (15)

### 命题 FN（finite Fourier--Bessel certificate）

对每个有限 `X`，

`I_sigma(X)=2sum_(n>=1)|b_(n,sigma;X)|^2`,           (16)

且每个有限部分和给出严格下界

`2sum_(n=1)^N|b_(n,sigma;X)|^2<=I_sigma(X)`.         (17)

当 `X->infinity` 且 `I_sigma<infinity` 时，每个固定系数收敛到式 (6)，
并且 Bessel tails 与空间 tail 共同给出 cofinal 证书。

#### 证明

命题 FK 的换元在 `[1,X]` 上给
`I_sigma(X)=2int_0^1z|F_(sigma,X)|^2dz`。对零延拓场应用 Fourier--Bessel
Parseval 得式 (16)，截断正项得到式 (17)。有限能量下，
`F_(sigma,X)->F_sigma` 于 `L^2(z dz)`，所以所有系数及 tails 收敛。`□`

式 (17) 是完全有限、只含 `n<X` 的算术证书；但它是能量下界。证明 RH
仍需要一个控制未计算 Bessel tail 和 `x>X` 空间 tail 的统一上界。

## 5. 一般中心参数

沿用文档 038 的

`q=c+2sigma>1`, `alpha=(q-1)/2`, `nu=1/(q-1)`,

`z=x^(-alpha)`.                                      (18)

对一般 Euler discrepancy `E_Z=Psi_Z-M_Z` 定义

`F_(Z,c,sigma)(z)=z^nu E_Z(z^(-1/alpha))`.           (19)

### 定理 FO（general radial arithmetic-field structure）

有

`I_(Z,sigma)=[4sigma/(q-1)]int_0^1`

`                         z|F_(Z,c,sigma)(z)|^2dz`,  (20)

且若 `b_n` 是阶数 `nu` 的规范 Fourier--Bessel 系数，则

`<nu_Z,e_(n,c,sigma)>=sqrt(alpha)j_(nu,n)b_n`,       (21)

`|<nu_Z,e_n>|^2/lambda_(n,c,sigma)`

`=[4sigma/(q-1)]|b_n|^2`.                            (22)

因此文档 037 定理 FE 的中心条带结论等价于这一径向算术场在相应
`L^2(z dz)` scale 中的 membership。

#### 证明

由 `dx=-(1/alpha)z^(-1/alpha-1)dz` 直接得到式 (20)。文档 038 一般
本征函数在 `z` 坐标仍为
`sqrt(q-1)z^(nu+1)J_(nu+1)(jz)/|J_(nu+1)(j)|`；重复定理 FL 得式
(21)。代入文档 038 式 (25) 得式 (22)。`□`

## 6. 高模态障碍的精确位置

在该坐标中，所有困难集中到 `z=0` 附近累积的素数跳跃：

- 对任意 `epsilon>0`，`F_sigma` 在 `[epsilon,1]` 上只有有限多个跳跃，
  Fourier--Bessel tail 可由普通分段光滑估计控制；
- `z<epsilon` 对应 `x>epsilon^(-1/sigma)`，正是尚未控制的全局素数尾；
- 文档 038 命题 FI 给每个固定模态的安全 Euler 表达，但其随
  `j_(nu,n)->infinity` 的联合相消等价于 `z=0` 的加权 `L^2` 可积性。

所以 Bessel 化把局部谱误差和真正的算术无穷远严格分离，却不会凭形式
正交性消除 RH 强度的边界 tail。

数值转录审计取 `sigma=0.75`,`X=13`。精确有限能量为
`1.19314351919022`；前 3、前 5 个 Bessel 模态的式 (17) 左侧分别为
`1.07075989911389`、`1.10288363917279`，严格单调并低于总能量。这检查了
式 (15) 的 Jacobian、Bessel 规范化与 Parseval 因子二；有限模态逼近本身
不构成无限尾证书。
