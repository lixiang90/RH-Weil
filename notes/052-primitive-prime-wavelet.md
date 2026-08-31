# Tate 消元、纯素数 Gram 与 primitive Weil 结构

文档 050 的局部公式仍显式含有 continuum 主项 `L log2`；文档 051
用 `Lambda-1` 把它吸收到系数中。本笔记给出更贴近 Weil 上同调的处理：
对相邻两个尺度作一次精确 Tate 消元。所得信号只含 von Mangoldt atoms，
没有 continuum、prime--continuum cross 或 background；其 kernel 虽变号，
平方积分仍给出正 Gram。

这一投影不会损失临界谱：归一化尺度多项式在单位圆上有严格谱隙，且有
显式 Wiener inverse。于是 zeta 的全部有限 primitive 结构可以无条件构造；
尚缺的只有实际素数向量的 subpower Gram bound，而该界仍与 RH 等价。

## 1. 精确 Tate 消元

沿用命题 HS 的

`z(L)=sum_n Lambda(n)phi(n/L)-Llog2`,                (1)

其中 `phi` 支撑于 `(1/2,2]`。定义

`u(L)=z(L)-2z(L/2)`,                                (2)

`chi(r)=phi(r)-2phi(2r)`.                           (3)

### 命题 IE（pure-prime primitive formula）

有精确有限公式

`u(L)=sum_n Lambda(n)chi(n/L)`,                     (4)

其中

`chi(r)=0`,                                  `r<=1/4`,

`chi(r)=r^(-1)-4`,                       `1/4<r<=1/2`,

`chi(r)=4-3r^(-1)`,                         `1/2<r<=1`,

`chi(r)=2r^(-1)-1`,                            `1<r<=2`,

`chi(r)=0`,                                      `r>2`. (5)

此外

`int_0^infinity chi(r)dr=0`,                         (6)

`A_chi=int_0^infinity chi(r)^2dr=26-36log2>0`.       (7)

#### 证明

把式 (1) 在 `L` 与 `L/2` 处相减；两个 continuum 项都是 `Llog2`，
故精确消去，得到式 (3)–(4)。将命题 HS 中 `phi` 的三段公式代入即得
式 (5)。变量代换 `s=2r` 给

`int 2phi(2r)dr=int phi(s)ds`，

所以式 (6) 成立。最后逐段积分

`int_(1/4)^(1/2)(r^(-1)-4)^2dr=6-8log2`,

`int_(1/2)^1(4-3r^(-1))^2dr=17-24log2`,

`int_1^2(2r^(-1)-1)^2dr=3-4log2`,

相加得式 (7)。`□`

这正是有限域上从总上同调剥离 Tate class 的数域类比：式 (6) 是
degree-zero 条件，而式 (4) 是只由 closed points/prime powers 生成的
primitive current。

## 2. 临界谱上稳定、Tate 谱上为零

令 `h=log2`，并归一化

`y(t)=e^(-t/2)z(e^t)`, `v(t)=e^(-t/2)u(e^t)`.      (8)

记 `T_hg(t)=g(t+h)`。

### 定理 IF（primitive scale polynomial and Wiener inverse）

有

`v=(I-sqrt2 T_(-h))y`.                              (9)

在任意酉 translation representation `U_h` 上，

`A=I-sqrt2 U_(-h)`                                 (10)

可逆，并且

`sqrt2-1<=|1-sqrt2 e^(-itheta)|<=sqrt2+1`,          (11)

`A^(-1)=-sum_(n>=1)2^(-n/2)U_(nh)`,                (12)

`||A^(-1)||<=sqrt2+1`.                              (13)

另一方面，归一化 Tate mode `e^(t/2)` 的 `U_(-h)` 特征值是
`2^(-1/2)`，故被式 (10) 精确消去。

#### 证明

式 (9) 直接由式 (2) 归一化得到。单位圆谱变量上，式 (10) 的 symbol
为 `1-sqrt2 e^(-itheta)`；反三角不等式给式 (11)。令
`r=2^(-1/2)`，几何级数给

`(1-sqrt2 e^(-itheta))^(-1)`

`=-sum_(n>=1)r^n e^(intheta)`,

由连续函数演算得到式 (12)–(13)。最后代入 Tate mode。`□`

所以这里的“投影”并非临界 Hilbert 空间中的不可逆商：它只在单位圆外
的 Tate 特征值处为零，在中心线的酉谱上反而一致可逆。

## 3. Mellin 非消失与零点检测

文档 048 的 Mellin multiplier 为

`W(rho)=[2^rho+2^(1-rho)-3]/(rho-1)`,              (14)

且在 `0<Re rho<1` 无零。

### 定理 IG（primitive multiplier theorem）

零点 mode `rho` 对 `u(L)` 的系数 multiplier 是

`W_prim(rho)=(1-2^(1-rho))W(rho)`.                 (15)

它在开临界条带 `0<Re rho<1` 无零；新增因子只在 `Re rho=1` 上有零，
并在 `rho=1` 消去主极点/Tate mode。

令

`C_prim(X)=int_X^(2X)|u(L)|^2L^(-2)dL`,            (16)

`Theta=sup_rho Re rho`。在文档 IC 使用的标准有限阶显式公式条件下，

`limsup_(X->infinity) log(max(1,C_prim(X)))/logX`

`=max(0,2Theta-1)`.                                (17)

特别地，以下条件等价：

1. RH；
2. `C_prim(X)=O(1)`；
3. `C_prim(X)=X^(o(1))`。

#### 证明

式 (2) 对 `L^rho` 乘以 `1-2^(1-rho)`，得到式 (15)。若新增因子为零，
则 `(1-rho)log2` 是纯虚数，故 `Re rho=1`；结合式 (14) 的非消失即得
开条带结论。文档 IC 的 Mellin singularity 证明逐字适用，给式 (17)。

也可直接使用定理 IF：`y -> v` 是有限尺度差，反向则是几何衰减的
未来尺度和。因此所有 dyadic blocks 上的 boundedness 或 subpower
boundedness 在 `y` 与 `v` 之间等价。再用定理 HV。`□`

这里必须强调：式 (17) 是 detector theorem，不是对式 (16) 的新上界。

## 4. 无背景的有限正 Gram

定义

`K_X^prim(m,n)=int_X^(2X)L^(-2)`

`                         chi(m/L)chi(n/L)dL`.      (18)

### 定理 IH（pure-prime Gram and diagonal law）

对每个有限 `X`，

`C_prim(X)=sum_(m,n)Lambda(m)Lambda(n)`

`                         K_X^prim(m,n)>=0`.        (19)

矩阵 `K_X^prim` 是实对称正半定；它只连接

`X/4<n<=4X`, `1/8<m/n<8`.                          (20)

其 diagonal

`D_prim(X)=sum_n Lambda(n)^2K_X^prim(n,n)`         (21)

满足

`D_prim(X)=(26-36log2)log2 logX+O(1)`.             (22)

所以 RH 等价于 signed off-diagonal 精确抵消 logarithmic diagonal 到
`O(1)`；证明 RH 已不需要估计任何 continuum cross term。

#### 证明

式 (19) 是有限和的平方积分，故即使 `chi` 变号，kernel matrix 仍为
Gram 正半定。式 (5) 给式 (20)。变量代换 `r=n/L` 给

`K_X^prim(n,n)=n^(-1)int_(n/(2X))^(n/X)chi(r)^2dr`.

标准 `sum_(n<=x)Lambda(n)^2=xlogx+O(x)` 与式 (7) 经分部求和，得到
式 (22)。`□`

注意 Gram 正性不表示 off-diagonal 本身为正。相反，实际算术向量必须让
它贡献约 `-D_prim(X)`，这正是所需的 prime-pair cancellation。

## 5. Primitive Gamma--Euler 结构定理

上一构造并不依赖数字 `2` 或中心 `1/2`。设函数方程中心为 `c/2`，
取任意 `q>1`、`h=logq`。假设某 compact Mellin wavelet 有局部公式

`z_Z(L)=Euler_Z(L)-aL^c`，                         (23)

且其 zero multiplier `W_Z(rho)` 在 `0<Re rho<c` 无零。定义

`u_(Z,q)(L)=z_Z(L)-q^c z_Z(L/q)`,                  (24)

`chi_(Z,q)(r)=phi_Z(r)-q^c phi_Z(qr)`.             (25)

若 background 的自然 Mellin density 是 `r^(c-1)dr`，则

`int chi_(Z,q)(r)r^(c-1)dr=0`.                    (26)

### 定理 II（general primitive Weil structure theorem）

在上述条件下：

1. 式 (24) 精确消去 `aL^c`，并给只含 Euler coefficients 的有限
   Hermitian Gram；
2. 归一化后尺度算子为
   `A_(q,c)=I-q^(c/2)U_(-h)`，其单位圆谱隙为 `q^(c/2)-1`，且

   `A_(q,c)^(-1)=-sum_(n>=1)q^(-cn/2)U_(nh)`;      (27)

3. zero multiplier 为
   `(1-q^(c-rho))W_Z(rho)`，在开条带无新增零；
4. 若这些 finite primitive Sobolev Grams 在临界参数 tight、与显式公式
   divisor trace 相容，则其 GNS completion 上有强连续酉群
   `U_t=e^(itA)`，且

   `Theta=c/2+iA`, `Theta*=c-Theta`;                (28)

   因而全部可见 divisor 位于 `Re rho=c/2`。

若测试 wavelet 对 divisor separating，则“可见”可删除，得到完整中心线
结论。

#### 证明

式 (23)–(26) 是变量代换。式 (27) 与定理 IF 相同，只把 `sqrt2` 换成
`q^(c/2)`；新增 Mellin 因子为零只可能在 `Re rho=c`。有限 Gram 正性
来自 feature Gram。临界 tightness 后按定理 GV/HQ 作 GNS completion，
Stone 定理给自伴生成元 `A`，于是式 (28)；谱定理给中心线。`□`

这一定理抽离出的 Weil 机制是：

`Tate 消元 + Euler closed-point Gram + 临界酉 dilation + 正极化`。

它比直接假设一个 Hilbert--Pólya 算子更具体，因为前三项都能在有限素数
层写出；真正的 Hodge--Riemann 输入被隔离为临界 tightness。

## 6. 对经典 zeta 的存在性审计

### 推论 IJ（zeta primitive structure: finite existence and exact gap）

对经典 zeta，定理 II 的以下部分无条件成立：

- compact `chi` 及 degree-zero 恒等式；
- 每个 `X` 的纯素数正 Gram；
- dilation covariance；
- 单位圆 spectral gap `sqrt2-1` 与显式 inverse；
- divisor-separating Mellin multiplier。

剩余且仅剩的解析存在性条件可取为

`C_prim(X)=X^(o(1))`.                              (29)

它由定理 IG 与 RH 等价。因此本笔记没有证明 RH；它证明的是所需结构的
全部有限代数部分确实存在，并把无限维 Hodge completion 的唯一障碍化成
一个不含背景项的纯 prime-pair bound。

一种适合继续攻击的规范目标是 actual arithmetic Rayleigh quotient

`R_prim(X)=C_prim(X)/D_prim(X)=X^(o(1))`.          (30)

由于 `D_prim(X)=O(logX)`，式 (30) 已足以推出式 (29)。不能把它替换成
kernel 对任意 coefficients 的 operator norm；文档 IA 的相邻 feature
平行障碍仍然存在。

## 7. 有限计算审计

脚本直接使用式 (4)，并在所有 kernel 断点之间积分式 (19)：

| `X` | `C_prim(X)` | `D_prim(X)` | off-diagonal | `R_prim(X)` |
|---:|---:|---:|---:|---:|
| 8  | 0.007336996 | 1.231764 | -1.224427 | 0.00595650 |
| 16 | 0.006725987 | 1.650142 | -1.643416 | 0.00407601 |
| 32 | 0.006670120 | 2.208488 | -2.201817 | 0.00302022 |

这些数值验证 continuum 的精确消失、Gram/diagonal 公式和强烈的 signed
off-diagonal cancellation。它们不控制 `X->infinity`，因而不是 RH 的
数值证据。

## 8. 齐次 ratio profile 与负配对通道

把 block window 暂时移除，定义 full homogeneous kernel

`K_infty^prim(m,n)=int_0^infinity L^(-2)`

`                         chi(m/L)chi(n/L)dL`.      (31)

令 `M=max(m,n)`, `q=min(m,n)/M`，并记

`k_phi(q)=int_0^infinity phi(qr)phi(r)dr`.          (32)

### 命题 IK（three-scale ratio identity）

有

`K_infty^prim(m,n)=M^(-1)k_chi(q)`,                (33)

`k_chi(q)=3k_phi(q)-k_phi(q/2)-2k_phi(2q)`.        (34)

这里对 `x>1` 约定 `k_phi(x)=x^(-1)k_phi(x^(-1))`，而对 `0<q<=1`，

`k_phi(q)=0`,                                     `q<=1/4`,

`k_phi(q)=[-8q+2+(4q+1)log(4q)]/q`,       `1/4<q<=1/2`,

`k_phi(q)=[16q-10-(4q+4)log2-(8q+5)logq]/q`,
`                                                   1/2<q<=1`. (35)

#### 证明

在式 (31) 令 `r=M/L`，得到式 (33)。将
`chi=phi-2phi(2·)` 展开：

`int chi(qr)chi(r)dr`

`=k_phi(q)-2 int phi(qr)phi(2r)dr`

` -2 int phi(2qr)phi(r)dr+4 int phi(2qr)phi(2r)dr`.

分别作 `s=2r` 变量代换，四项合并为式 (34)。对命题 HS 的两段
rational `phi` 直接积分得到式 (35)。`□`

这个恒等式很关键：primitive off-diagonal 不是任意新 pair interaction，
而是原 positive wavelet autocorrelation 在 `q/2,q,2q` 三个相邻尺度的
离散二阶组合。

### 推论 IL（explicit signed cancellation channel）

`k_chi(q)=0` 对 `q<=1/8`；并且

`k_chi(1/4)=8-12log2<0`,                           (36)

`k_chi(1/2)=-24+34log2<0`,                         (37)

`k_chi(1)=26-36log2>0`.                            (38)

因此 full primitive Gram 虽为正半定，其一大段可比但分离的尺度 pair
具有负 entries；diagonal cancellation 已内建于三尺度 kernel，而不是
额外加入的 continuum 项。

#### 证明

支撑结论由式 (34)–(35)；代入三个 ratio 得式 (36)–(38)。Gram 正性仍由
式 (31) 的 feature 表示保证。`□`

数值解闭式 profile 的内部换号点为

`q_*=0.582917939156379...`;                         (39)

即约 `1/8<q<q_*` 的 entries 为负。这个小数只用于审计；后续证明应使用
式 (34)–(35)，不依赖数值求根。

这把下一步进一步缩成：在 geometric prime blocks 上利用三尺度离散差，
证明实际 von Mangoldt vector 落在 full Gram 的近 radical；无需处理远程
ratio，因为 `q<=1/8` 时 coupling 精确为零。

## 9. 下一步

最集中的开放任务现为：直接从 von Mangoldt coefficients 证明纯素数形式

`int_X^(2X)|sum_n Lambda(n)chi(n/L)|^2L^(-2)dL`

至多为 `X^(o(1))`。可尝试的结构性分解必须保留 `chi` 的三段符号：

1. 按比值 `m/n` 将 factor-`8` pair kernel 分解为同尺度与最近邻块；
2. 对 prime powers 用 multiplicative residue/short-interval dispersion；
3. 把零质量条件转成离散导数，使 off-diagonal cancellation 在公式层显现；
4. 寻找 primitive Gram 的低秩 endpoint core 与正局部方差分解。

任何成功的 polylog 或 subpower 完整形式上界都会证明 RH；逐项绝对值估计
则会破坏表中可见的 `D_prim+off-diagonal` 相消。
