# Core-renormalized 负谱迹与 prolate factorial 迹尾

文档 027 证明不剥离中心井时，纯 phase-volume 证书有严格大于 `1` 的障碍。
本笔记证明有限 core 如何精确改变 phase-space 密度：从 evaluation vector 中
减去 core Fourier profiles 后，剩余密度控制余空间负谱的**总质量**，而不
只是负方向个数。对中心 prolate core，该密度积分正好是 prolate 特征值迹
尾；文档 020 的 factorial 单特征值界可以求和成 factorial 迹尾。

## 1. 全空间的负谱迹界

沿用文档 027 的闭非负 form

`p(f)=int_R M(t)|hat f(t)|^2dt/(2pi)+r(f)`,            (1)

其中 `M>=0`、`M(t)->infinity`、`r>=0`。令 `A` 为其算子，并考虑 scalar
threshold form

`q_a=A-aI`, `a>0`.                                    (2)

### 定理 DI（phase-space negative-trace bound）

`q_a` 的负部是 trace class，且

`Tr[(q_a)_-]`

`<=ell/pi int_R [a-M(t)]_+ dt`.                       (3)

#### 证明

取 `q_a` 的规范负谱本征向量 `{f_n}`，相应本征值为 `-eta_n<0`。由
`r>=0`，

`eta_n=a-p(f_n)`

`<=int_R[a-M(t)]_+|hat f_n(t)|^2dt/(2pi)`.            (4)

固定 `t`，Fourier evaluation vector `y mapsto exp(ity)` 在
`L^2([-ell,ell])` 中的范数平方为 `2ell`。Bessel 不等式给出

`sum_n|hat f_n(t)|^2<=2ell`.                          (5)

对式 (4) 求和并用 Tonelli、式 (5)，得到式 (3)。因 `M(t)->infinity`，
`[a-M]_+` 紧支撑可积，右侧有限，所以负部 trace class。`□`

式 (3) 是文档 027 计数定理的能量版本；它还给出 operator 下界

`q_a>=-Tr[(q_a)_-] I`.                               (6)

## 2. 剥离有限 core 后的精确 evaluation 密度

令 `Q subset Dom(p)` 是 `r_0` 维空间，规范正交基为
`phi_1,...,phi_(r_0)`，`P_Q` 是其投影。定义

`d_Q(t)=2ell-sum_(j=1)^(r_0)|hat phi_j(t)|^2>=0`.     (7)

### 定理 DJ（core-renormalized negative-trace bound）

令 `q_(a,Q)` 是 `q_a` 到 `Q^perp` 的 form compression，则

`Tr[(q_(a,Q))_-]`

`<=eta_Q(a)`

`:=int_R[a-M(t)]_+d_Q(t)dt/(2pi)`.                   (8)

特别地，

`q_(a,Q)>=-eta_Q(a) I` 在 `Q^perp` 上成立。          (9)

#### 证明

取 compression 的规范负谱本征向量 `{g_n} subset Q^perp`。固定 `t`，
这些向量都位于 Fourier evaluation vector 的 `Q^perp` 投影空间中，所以
Bessel 给出

`sum_n|hat g_n(t)|^2`

`<=||(I-P_Q)exp(ity)||^2=d_Q(t)`.                    (10)

将式 (5) 替换为式 (10)，重复定理 DI 的证明得到式 (8)。最大负特征值的
绝对值不超过全部负特征值绝对值之和，得到式 (9)。`□`

DJ 保留了 core profiles 与坏 multiplier 的位置关系；若 core 正好集中在
最深坏井，`d_Q` 会在那里显著小于粗界 `2ell`。

## 3. 中心 prolate core 的 factorial 迹尾

考虑频率井 `I=[tau-r,tau+r]`，time--bandwidth 参数

`c=ell r<=1`.                                         (11)

令 `chi_0(c)>=chi_1(c)>=...>=0` 是对应 concentration operator 的 prolate
本征值。取前 `2R-1` 个 modulated prolate 本征函数作为 `Q_R`，即索引
`0,...,2R-2`。

### 引理 DK（explicit prolate trace tail）

对 `R>=1,c<=1`，

`sum_(n=2R-1)^infinity chi_n(c)`

`<=5e^2 4^R c^(2R+1)/[pi(2R+1)!]`.                  (12)

而且有精确恒等式

`int_I d_(Q_R)(t)dt/(2pi)`

`=sum_(n=2R-1)^infinity chi_n(c)`.                   (13)

#### 证明

文档 020 定理 BY 给出

`chi_(2r-1)(c)<=C_r`

`:=2e^2 4^r c^(2r+1)/[pi(2r+1)!]`.                  (14)

单调性还给出 `chi_(2r)<=C_r`。因此式 (12) 左侧不超过

`2sum_(r=R)^infinity C_r`.                           (15)

相邻项比值

`C_(r+1)/C_r=4c^2/[(2r+2)(2r+3)]<=1/5`,             (16)

所以式 (15) 不超过 `(5/2)C_R`，即式 (12)。

另一方面，concentration operator 在 `Q_R^perp` 上的 trace，一方面等于
未剥离本征值之和，另一方面由 kernel 对角积分等于式 (13) 左侧。`□`

若负 multiplier 在 `I` 上深度至多 `D`，则 DJ 中该井的贡献至多

`5D e^2 4^R c^(2R+1)/[pi(2R+1)!]`.                  (17)

这正是文档 027 中心 phase-volume 常数障碍被有限秩几何取代后的 factorial
小量。

## 4. 加权坏集分解

令

`W_a(t)=[a-M(t)]_+`.                                  (18)

把其支撑分成中心井 `I_0` 与剩余集合 `E_1`。若中心井 core 为上述 `Q_R`，
且 `D_0=||W_a||_(L^infinity(I_0))`，则定理 DJ/引理 DK 给出

`eta_(Q_R)(a)`

`<=5D_0e^2 4^R c^(2R+1)/[pi(2R+1)!]`

` +int_(E_1)W_a(t)d_(Q_R)(t)dt/(2pi)`.               (19)

第二项仍可用非中心 resonance blocks 继续剥离，或粗估为

`(ell/pi)int_(E_1)W_a(t)dt`.                          (20)

所以正确的全局量不是坏集测度，而是经过 resonance-adapted core
renormalization 后的加权 evaluation-density 积分。

## 5. 到 residual--Feshbach 与中心线的接口

对 zeta，把奇极点锚 `sinh(y/2)` 也加入 core `Q_lambda`；对 entire L 数据
无需此步。令 `q_lambda` 是完整 Weil form，而 `q_(lambda,Q)` 是其余空间
compression。若定理 DJ 及式 (19) 的逐井版本给出

`q_(lambda,Q)>=-eta_lambda I`,                        (21)

取任意 `delta_lambda>0`，则

`q_(lambda,Q)+(eta_lambda+delta_lambda)I`

`>=delta_lambda I`.                                  (22)

### 定理 DL（core-renormalized cofinal Hodge certificate）

若存在 `lambda_j->infinity`、cores `Q_j`，以及
`eta_j->0`,`delta_j->0`，使：

1. DJ/逐井 factorial bounds 严格证明式 (21)；
2. 对 shifted operator

   `B_j=q_(lambda_j)+(eta_j+delta_j)I`                (23)

   的 core block `A_j`、完整 residual Gram `R_j`，有

   `A_j-R_j/delta_j>=0`;                              (24)

则对应 L 数据的全部非平凡零点位于中心线。

#### 证明

式 (22) 是 `B_j` 的余空间隙。文档 024 定理 CT 与式 (24) 给出
`B_j>=0`，即

`q_(lambda_j)>=-(eta_j+delta_j)I`.                   (25)

右侧误差趋零，应用文档 015 定理 AY 及相应 Weil 判据。`□`

DL 把剩余存在性问题改写成两个都保留相消的量：core-renormalized 负迹
`eta_j` 与 residual Gram Schur correction。中心井对 `eta_j` 的贡献已经由
DK 无条件降为 factorial 尾；尚未完成的是所有非中心 resonance blocks 的
联合加权迹尾，以及式 (24) 的 cofinal 裕量。
