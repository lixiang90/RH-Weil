# Same-source physical Llow scalar：独立代码fresh

2026-10-29。结论：**当前固定脚本未发现阻断一次既定scalar检验的实现问题。** 本审查只读实际证据与代码，并运行小3×3精确代数对照；没有调用`calculate/main`、执行真实224维scalar、重跑source/trial/compiler/Gram或更改参数。没有改STATE、cadence、Git、Goal或其他代理文件。是否准入实际执行仍由root在消费strongest-old与数学transport原件后决定；代码审查不能预付实际Llow的符号。

## 1. 恢复与当前字节

已恢复README/STATE、check后show、G20261027、C058停止合同、D20261029T、宏观前沿与实际工作树。原冻结0c4f、cadence1/history59/latest595/formal19及长Goal完成门保持；当前是595发布后的独立physical-consumption准入，不是恢复C058的参数预算。

逐段读新脚本全本和`next-physical-lower-comparison-admission.md`；对照新inverse原件§5–6的Γ、Wr/V/Bc及完整解析fresh的source/operator费用。当前绑定如下：

| 对象 | SHA256 |
|---|---|
| `scripts/weil_9_8_physical_lower_gate.py`，8953 bytes | `322756691b82f70a0866bd6da28ff4f60a35020126f8deb55c495127bc930671` |
| 595 root consumption | `7333762b917efbd8fd92b95a177576eea92a7a6f231d8ff7236dca7cdf93a7c3` |
| source-stage verification | `dbb31208d0568feac7c9adff27722d5b55d08381002d23e0a4e35f150b1472c1` |
| core-stage verification | `53225c62a898ca9aef69f072efa349043de8d6e652e5be99f5e6849a1eac0d2d` |
| compact negative witness | `81bf3deaee393796bdf8b5a165904e188c657ff16176eaa9cb5eab1c22a0bab9` |

本fresh实际重新hash根记录全部31项bindings、三份公开metadata、witness的12项输入绑定、private trial/compile receipts所列输入链，以及三个实际source packets；当前全部匹配。也读现有trial输出映射：even-trial SHA为`5c77c19b7af6f36a281d3f7c1ad4dd2fa91613f9955eeefbd8662ae099c282b0`。该过程仅读取/验版本，没有计算实际224维scalar。数值oracle/595全compiler的数学真实性仍消费原已审程序及根记录，不由hash本身证明。

## 2. 输入读取、实际basis与费用对象

脚本先固定ROOT_SHA，再按该不可变root记录取各文件SHA；metadata、witness、private input链与packets在读取时校验，计算完成后再次校验全部已读pins。相对/绝对路径都resolve并限制在REPO内。它不import任何上游科学模块，不调用旧driver或subprocess/network，只用stdlib读取JSON和做exact整数/Fraction运算。

矩阵实际储存顺序为全448的upper parity triangle：i从0至447、k从i至447步长2，每矩阵50400项。脚本完整读顺序并只提取even行到224×224对称矩阵；center取endpoint sum，分母S=2^257。没有再错读成lower triangle。原Legendre degree为2k，因此native q_k=8(4k+1)，不是用sector内部degree直接取8(2k+1)。Γ=18Q^-1对应原du norm。

Tail按column-major896坐标读midTwice=lo+hi，分母2^641，校验全序、640输出格与9/8参数，另一parity必须exact零。两列都保留在raw U更新`36Σt_s t_s*/2^1282`中；even sector的odd列为零不导致重复付款，也没有另乘L²。实际Z取既有even trial，严格要求normPower3，再按native q完整重算ν，核原numerator且ν≤2^518，所以本次y=8不是继承旧数据。

新能量目标确为raw中心

    (a+j)/S +36Σt_s t_s*/2^1282，

其中a表示M、j表示Kcompact，b仅用来确定同一source的V。目标里没有混入λ、β、D0或W^-1；否则将再次只计算旧充分P0而未到真实Llow。Script正确相加εA+εH+σ为`2^-204+2·2^-220+9·2^-512`。B的误差无需再向这个能量添加一次：u是由已经生成的整数中心**定义的确切source**，不是试图近似由真实B重新选择的另一个source；source适应性由统一operator-norm误差覆盖。

## 3. 独立重导u=Vint v

令p=Qv、z=Zp、a_z=aQz、b_z=bQz、a_p=ap。原整数式

    F=18SR(Z+Z*)−Z*QaQZ+8Z*QbQZ−8R(aQZ+Z*Qa)，
    Vint=QFQ+18cQ，c=8Cw+(9y²+16y)2^549，Cw=SR²

给

    Fp=18SR(z+Z*p)+Z*Q(8b_z−a_z)−8R(a_z+Z*Q a_p)，
    u=QFp+18cp。

脚本的`transpose_mv`为Z*作用（本次real数据用transpose），`quadratic`与`ztqap`分别对应上式两项；Q的左右位置及c的2^549幂均正确。没有要求Z自伴，也没有把aQZ或Z*Qa互换。总复杂度为固定次数matrix-vector乘加O(224²)，不构造新的trial或整个V、目标矩阵/Gram。

从Bc=Q^-1/2 Vint/(sqrt(18)Cw)和Γ=18Q^-1独立得到

    Γ^-1/2 Bc v = Vint v/(18Cw)。

输入packet的原方向是v/2^512；本脚本明确改用整数v，故选的是同一physical ray上放大2^512的source，sign与Rayleigh不变。返回raw coefficients为u/(18Cw)。E0、N0使用未除共同分母的raw u，必须分别除(18Cw)^2才是这一返回source的physical energy/norm；脚本同时保存该说明和`physical_source_norm_squared`。N0的`original_du_norm`是raw u在Γ中的原du二次型，不是Z或合同坐标的Euclidean norm。

## 4. 实际执行的小型exact对照

只以非__main__名加载guarded新脚本，并核当前SHA；未调用会读实际packets的`calculate`。取3×3非对称

    q=(8,40,72)，v=(2,−3,5)，y=8，
    Z=[[1,2,−1],[0,−2,3],[2,1,1]]，
    a/S=[[3,1,0],[1,4,−1],[0,−1,5]]，
    b/S=[[7,2,1],[2,9,0],[1,0,11]]。

保本次真实S/R/Cw数值，以两种独立路径核全部3个u坐标：一条直接构造完整integer F/V；另一条不用F公式，按Γ、Y=QZ/R和raw inverse expression

    Wr=ΓY+Y*Γ−Y*(a/S)Y
       +8[Γ−(a/S)Y−Y*(a/S)+Y*(b/S)Y]+ΔΓ，
    Δ=(9y²+16y)2^-220，V=Cw QWrQ

作Fraction矩阵运算。两条得到的V全部entries为整数，彼此相等，乘v后与脚本`transport`逐坐标全等。另用v/2^512调用纯transport，结果逐坐标恰为u/2^512。

再取j/S=[[-2,1,0],[1,1,2],[0,2,3]]和两列t=(2,−1,4)、0，用独立raw quadratic直接在x=u/(18Cw)上计算energy与Γ norm，均精确等于脚本相同表达式E0/(18Cw)^2、N0/(18Cw)^2，且两个Rayleigh之比全等。这些只是代数/实现对照，不是实际source、真实M positivity或224维结果。

## 5. Sign与域的消费边界

N0=18Σu_i²/q_i>0，εlow为原du operator误差，故真实mappedsource的Llow Rayleigh位于E0/N0±εlow。脚本只在upper<0或lower>0时声明该**单方向**严格负/正，区间跨0则未决；没有扫描误差/参数来强求一侧。

Raw source是有限even Legendre多项式在I内、外部zero extension，最高degree446。它是compact BV，Fourier尾O(1/|t|)，所以在Dlog；稀疏的合同v不能被当低阶physical源。Strict negative可证真实bounded Llow非PSD，但原完整Q还含未用tail，不能推出Q负。Strict positive仅是这一个physical方向为正，不能证明全Llow或9/8 Q coercivity，也不能把595失败单独归罪W的逆上界：Schur condensation、inverse、α/β及误差付款是合并损失。

脚本相应保持`whole_Llow_nonnegative_certified=false`、`full_Q_negative_certified=false`、`window_coercivity_certified=false`，没有把新数据叫RH结论。输出只允许在独占新目录，既有文件拒绝，exclusive xb保存；强制-I -S -B及assertions，所有数值exact而非新的precision proposal。它不带一般OS sandbox/audit-hook声明，本审查的实现判断针对当前已读固定代码与SHA。

当前代码准入没有数学计轮效力；ROOT仍须先消费另外的strongest-old/transport门，再执行唯一实际test，并依据实际输出和完整前件决定净值/结算。没有发现需要修改当前脚本的必须项。本fresh没有实际scalar结果、STATE/Git/cadence变化或pending子任务。
