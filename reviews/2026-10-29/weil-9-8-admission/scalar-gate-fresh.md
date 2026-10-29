# 固定 L=9/8 scalar 首门的独立核验

2026-10-29；限定 fresh 审查。只消费实际新 scalar 脚本和结果，不改原 source、STATE、cadence 或 Git，不执行完整矩阵、inverse、Gram certificate。该记录不证明新窗口完整 Weil 型正性，不构成研究轮结算。

## 1. 实际核验对象与字节绑定

已读 555 §1–2 的原 du 全复源 Schur 运输、当前脚本全本、当前 scalar receipt、解析迁移稿 §2–4，以及 frozen `scalar.py` 的原七 cell/q 首门和 `14-ru_producer.py` 的 `32B−29A`/493 入口。源文件只作为审查材料，没有执行其 top-level driver 或改动。恢复入口、实际 Goal/主合同/宏观前沿也已按只读范围恢复。

当前文件绑定：

| 文件 | SHA256 |
|---|---|
| `scripts/weil_9_8_cosh_row_gate.py` | `d1250bc3e5f2eeebed2b94dbe58110fb06f76fb9bb6bb5f7529fd4cf36256feb` |
| `cosh-row-first-gate.json` | `9856d2acc3e4b23fbf4ef8e144b5a8f2df1a7b0ed21220bc51d35f7b9c0a37d1` |

通过 importlib 只调用具有 `__main__` guard 的新脚本 `calculate()`，重算结果与 receipt 去除 `script_sha256` 字段后逐项相等；当前源码 SHA 与 receipt 一致。没有调用该脚本的输出写入函数，没有覆盖 receipt。早期 13/4 assert 失败不在本记录中改写为通过；本审查绑定的是当前保留失败字段的新版本。

## 2. 原对象和 shift 方向正确

`A_L=Σ_n Λ(n)/√n (T_log(n)^I+T_−log(n)^I)`，原 Hilbert 空间是 `L²((-L,L),du;C)`。辅助权 `W(u)=cosh(u/2)` 仅用于 Schur，不改变 physical norm。令 `x=e^u`、`E=e^L`，在 `u≥0`：

* 负移 `u−log n` 在 `x>n/E` 活跃，weighted row 为 `Λ(n)(x/n+1)/(x+1)`。
* 正移 `u+log n` 在 `x<E/n` 活跃，weighted row 为 `Λ(n)(x+1/n)/(x+1)`。

这里 `Λ(4)=Λ(8)=log2`、`Λ(9)=log3`，不是 `log n`。当前脚本的 BASE 和两个方向系数完全相符。n={2,3,4,5,7,8,9} 是本窗口全部 contributing proper powers；下一个 n=11 不贡献。每条 partial shift 与其 adjoint 都在，未遗漏 factor2。负半轴由偶性覆盖。

精确事件顺序是 `1<E/3<4/E<E/2<5/E<7/E<8/E<9/E<E`。八 cell 活跃负移依次为 `{2,3}`、`{2,3}`、`{2,3,4}`、`{2,3,4}`、`{2,3,4,5}`、`{2,3,4,5,7}`、`{2,3,4,5,7,8}`、全部七个；正移依次 `{2,3}`、`{2}`、`{2}`、空、空、空、空、空。尤其 ±log3 同时活跃的中心 cell 实际存在。

每 cell 的实际 row 是 `(Ax+B)/(x+1)`，固定非负系数的导数号恒定，故检两侧端点左右极限足够。分母区间正，所有区间加乘除均向外；独立包围分子/分母虽略宽，但方向安全。事件本身的单点取值不影响 ess sup。

## 3. 不同算法的精确独立重算

除重放当前脚本，还另写即时 Python/stdlib Fraction 运算，不调用 `calculate()` 的 log、exp 或 interval helpers。对 p=2,3,5,7 直接取 `z=(p−1)/(p+1)`，用 128 项

`2Σ_(k=0)^127 z^(2k+1)/(2k+1)`，余项上界 `2z^257/[257(1−z²)]`。

对 E 用 `Σ_(k=0)^64 L^k/k!`，余项上界 `L^65/65! /(1−L/66)`。全部向外舍入到 10^−12 格点。输入结果如下，表中十进制均是精确有理数：

| 输入 | 下界 | 上界 |
|---|---:|---:|
| log2 | 0.693147180559 | 0.693147180560 |
| log3 | 1.098612288668 | 1.098612288669 |
| log5 | 1.609437912434 | 1.609437912435 |
| log7 | 1.945910149055 | 1.945910149056 |
| E | 3.080216848918 | 3.080216848919 |

用该组较粗独立有理包围重算八 cell 全部 16 个一侧端点。最后 cell 的 `9/E` 右限下界严格大于其余 15 个端点上界，所以 cosh row 的实际最大值唯一发生在那里，且

`3.259557212715 < β_cosh < 3.259557212720`。

因此 **13/4=3.25 首提议失败**，当前 receipt `proposed_bound_passed=false` 正确。209/64=3.265625 严格上包围，故 555 的原 du Schur 引理实际支付

`||A_L||<209/64`，`(15/64)I < M=(7/2)I−A_L < (433/64)I`。

这证明的是完整 prime-shift M 的可逆性前提，不是 Γ/pole 全 Weil 型正性。由该界不能保留旧 μ=29/32；当前 false 字段是“未支付”，不能解读成真实 M 最小谱已被上界排除。

## 4. 旧 q 首门的单点精确反测

只检原固定 `q(x)=1+(5/8)x²`，不搜索权重或窗口。取规范坐标 `x=u/L=31/32`，实际物理点 `u=279/256`。上述有理 log 包围严格证明该点处所有七个负 shift 活跃、全部正 shift 不活跃，而且点位于最后开 cell 内。因此这里的 row 由

`R_q(x)=Σ_n [Λ(n)/√n] [1+(5/8)(x−log(n)/L)²]/[1+(5/8)x²]`

给出。以 `isqrt(n·10^24)/10^12` 及下一个格点包围 √n，平方区间按是否跨零分别处理，精确向外求和得

`2.705918929563 < R_q(31/32) < 2.705918929569`。

独立计算的未向下格点舍入的下界为

`1018074548057405666610460601623531267401093489010670376129925468284756056855296342167135110843 / 376239855870981057794545440723551379382077733637942161759832386779785156250000000000000000000`。

与 27/10 交叉相乘严格较大。该 row 在点旁连续，所以 `ess sup R_q>27/10>83/32`；这个原 q 的 best Schur coercivity `7/2−ess sup R_q<4/5<29/32`。因此**原 q 也不能支付旧 inverse/compiler 的 μ=29/32 首门**。这不是新的谱下界、不是 Q 负性、也不排其它权重；只阻止在这两种已执行固定权重下沿用旧 inverse 入口。继续须明确重导新 μ、inverse、congruence 和 Gram 参数，不能仅改 JSON 标签或用有限 Gram 调整掩盖门失败。

## 5. r 整数门和严格剩余责任

独立核 `e<68/25`：`Σ_(k=0)^6 1/k!+1/4410=31967/11760<68/25`；后续项比值至多 1/8 给该余项上界。对解析迁移稿提供的 ellipse 公式 `r²≥81 e^240(2/3)^896`，候选 `r=2^−85` 的充分条件正是

`81·68^240·2^1066 <25^240·3^896`。

独立 Python 大整数比较为 true；指数 1066=896+170 没有漏二次方。它只支付已给 ellipse 公式的数值代入，不独立证明该公式、projection 域运输或完整 block-Schur。

当前可消费的是 555 的一次固定全 shift 算子评估、失败 13/4 和旧 q/μ 门，以及 r 公式的标量检查。新 moments/matrices/columns、576 核精度、225 ordered pairs、归一化 Γ、全部误差预算、full complement/cross、inverse/congruence/完整 residual 仍必须各自支付。有限窗口若日后认证也不能自动移除长期 Goal 的成长/core 或算术 primitive/mixed 瓶颈。无新数学轮、无 Goal 完成、无研究状态写入。

## 6. 补审：当前 true-moment 22 scalar leaves

Root 追加的新 scalar reclosure 审查绑定如下：

| 文件 | SHA256 |
|---|---|
| `scripts/weil_9_8_analytic_scalar_gate.py` | `2cdb9523b99eb6a9355c18382273e6c9907747d12623c00514603b67904c754b` |
| `analytic-scalar-reclosure-true-moment.json` | `af09d25bcb68928beaf5ca361f8998168e03822dd0d45a9c458de6deaea286cb` |

实际调用当前 guarded script 的 `calculate()`，22 项全部 true，与新 receipt 去 hash 后逐项相等。另用独立转写的大整数交叉乘比较及 Fraction 公式核以下关键费用，未运行 frozen producer/checker：

* 新 c=288 的非退化下界、81/27 与列范数上界，以及 δ、r/p、complement-positive 各 scalar leaf 均成立。它们只配套所给积分/算子证明；source 区间、column 精度和 full block-Schur 不是这些布尔值本身的后果。
* 实际 Binet 有理余项是 `R=4·513!/[6^514(1025/4)^514]`。精确比较证 `R<2^−1500`、`256R/3<2^−1493`，远强于原打印的弱界。这里 s=1025/4 和 Ω=256 没有改变，新的 L 不改变 R。
* `914·576^2048/2048!<2^−600` 与 `576^2049/[3·2049!]<2^−513` 均通过独立整数比较。π>3 使后一项安全上包围 band operator Taylor 费用；Machin 160 项误差仍 <2^−646。
* **条件是 true θ_q 的 midpoint error ≤2^−1098** 时，完整核预算满足 `(9/4)[914·576^2048/2048!+2^−1098(68/25)^576]<2^−204`。独立精确比较通过；乘 2^204 后约为 3.49·10^−19，仅作量级说明。未生成或验收 1024 个新区间，故此时仍是有明确 oracle 对象的条件结论。
* raw column 的 Γ 乘积 >1/1024、448<32²、raw coordinate error 2^−524 到 normalized column 2^−514 的算术，以及再加 band/Machin 后 <2^−512 的条件预算成立。新 raw U 系数 36、ΩL²=324 均正确。未经新每坐标 oracle，不能据此声称列误差已经取得。

必须保存的语义纠正：最初 21 项 `analytic-scalar-reclosure.json` 将 midpoint radius 与 `256R/3` 相加；若把前者读作已包含 Binet 的 true-moment radius，会重复支付 R。加大误差本身保守，但“只付一次”的说法不准确。Fresh 实际读原 `02-produce.py` 的 `theta=m.sym(theta,delta)` 和独立 `01-check.py` 229–234 的 remainder integration，二者都把 R 纳入 true moment 一次；原 packet 也显式 `binet_remainder_included_once:true`。Root 现已保留旧 receipt 为历史，另生成上述 22 项 true-moment receipt，当前 kernel_total **不再追加 R**。本审查只消费该纠正后的对象/预算；旧 single-payment 读法撤回，不用 finite-part D_q 条件替换当前 true θ 对象。新 producer/checker 仍需实际保留该 single-payment 语义并独立验全区间。

还以第3节独立 log 格点与平方根 isqrt 格点直接核了 M 的完整 coefficient mass `Wabs=7/2+2Σ_n Λ(n)/√n`，严格有 `10<Wabs<11`（约 10.57500562853）。因此这一个 mass 前提已由实际全七个 proper-power 系数支付；中心坐标误差 η=2^−2048 仍是尚待 source oracle 的另一个前提。条件 raw center padding `<2^26η<2^−2021` 的算术正确，不替代完整 raw interval width 或加权 operator row 检查。

旧 q/μ=29/32 门失败只阻止旧常数直接复用，**不排合法新 μ=1/8 的通用 inverse/congruence 重导**；该另行推导与其 finite residual 不在本 fresh 的证明范围。当前强后果仍是 source/analytic 准入的精确 scalar 费用和明确条件，完整窗口正负未知，成长/RH 主瓶颈未变。
