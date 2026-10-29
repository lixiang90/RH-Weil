# 固定9/8：实际有限目标负方向的独立整数复核

2026-10-29。限定结论：**保存的偶扇区整数目标确有严格负方向；这一个固定充分比较矩阵不能是半正定。** 本审查没有重跑Gram、odd、source、trial或compiler，没有改变L/Ω/N/μ/θ/精度，没有改STATE、cadence、Git或原程序。数学结算仍由root执行。

## 1. 实际对象、范围与字节绑定

按README/STATE、check后show、G20261027、C058、D20261029S和宏观前沿恢复。实际STATE为C058 reviewing，原cadence0/history58/latest594/formal19；长Goal完成门与冻结0c4f保持。已读新inverse原件的原norm、rawΓ、正合同变换、全部六系数及充分性方向，定向核当前core代码的proposal、exact方向计算、保存失败与audit分支，并读595冻结草稿§3的结论范围。

这里的Kcert是新source数据与actual trial编译出的224×224**有限充分比较目标**，不是完整Weil型中的compact operator K。读取实际`core-run-02`的完整目标、224维向量、trial/compile receipts、Gram proposal/failure/access；没有调用worker的`failed_direction`或其他算术函数，不使用Decimal作本次符号判据。

| 文件 | bytes | SHA256 |
|---|---:|---|
| ignored `even-target.json` | 43104610 | `14dcbebe5b553d7fa30e5e0d2ded203c32d75693cc3f2e39525fc236673f6401` |
| ignored `even-gram.json` | 4765 | `37f2063826e9c61c0141337d56de4a8113436f52a5855d7005e45b46eae5c4e7` |
| ignored `compile-receipt.json` | 3447 | `988771c0b99a2bc2f4f8badd882904b00d4c482144c4e5ea94050844db4feafd` |
| ignored `trial-receipt.json` | 2926 | `c8f268ad4a1555bb66dbe7dc4814e65ffcf12a7b28f10c7d30ea2dc26abbeead` |
| ignored `gram-failure.json` | 509 | `b5b470135be57870daeb7f1d33b0b314a5565452cb7fdefb3a314f11d7093e88` |
| ignored `gram-access.json` | 2646 | `fdf7b2feb1064daf4516f78dae823a9ff874f9496ecf1b97368a96f2e4315d69` |
| current core worker | 29732 | `d9ac746c3d56199ea65385f9883390c19a64b06ba8397f52ad96201d20485961` |

Compile receipt确实绑定上述whole-target SHA、当前worker/config，并记录本偶扇区全部224²=50176项compiler equality、actual normPower3及V列整性。另将compile receipt的14项输入pins、trial receipt的11项输入pins逐文件重新hash，全部与当前bytes一致。这是对实际已生成数据的版本核验，不冒充重新证明全部source oracle或解析费用。

## 2. 不同求和顺序的严格复算

先读取并核完整224×224整数矩阵对称性、全部224个canonical整数向量项。向量恰在zero-based indices0至13非零，其余210项精确为零。令这些整数为v_i，保存的实际有理方向为w=v/2^512。本fresh以对角加严格上三角的不同组织计算

    N = Σ_i Kcert_ii v_i² + 2Σ_(i<j) Kcert_ij v_i v_j。

结果严格小于零，且`str(N)`与原proposal的`quadraticNumerator`**逐字相等**；N绝对值为3851 bits，完整带符号整数保存在附属JSON，字符串SHA256为

`ef10199df62e18072e62d9d4836d14b5807ba549232d94bf24f70d8d0ef00a47`。

因此w* Kcert w=N/2^1024<0。原proposal的pivot13只是如何找到方向；严格符号来自另行读取实际整数Kcert和v的exact乘加，未依赖failed Decimal pivot的可信度，也没有从一个positive方向推PSD。

目标实际bit scale为2849。以Kcert/2^2849及**合同坐标的Euclidean向量范数**归一化，另用精确Fraction交叉乘核

    −2^−79 < N/[2^2849 Σ_i v_i²] < −2^−80 < 0。

显示值约−8.595411710699295×10^−25仅供量级说明。这个严格负值不是480-bit Gram shift的误差符号，也不会由提高同一目标的proposal精度而变为PSD；它不提供原physical norm中的同样数值下界。

## 3. 可公开、自足复核的紧凑witness

[negative-direction-independent-replay.json](negative-direction-independent-replay.json)为101277 bytes（约98.9KiB），SHA256：

`81bf3deaee393796bdf8b5a165904e188c657ff16176eaa9cb5eab1c22a0bab9`。

其中保存actual Kcert在indices0…13上的105个上三角整数、14个非零整数坐标、完整N、norm平方、全部归一化幂、whole-target SHA绑定及12项输入文件bytes/SHA。它只含本次生成数值与元数据，不含第三方全文。另从**序列化后的该JSON本身**重新读取，核105项恰覆盖该14×14上三角、重算N与完整字符串相等、N<0和上列dyadic界。这个小证书的整数符号可不依43MB完整cache复核；它与真实whole Kcert的提取关系由此次全文件读取及SHA记录负责，hash本身不证明这种关系。

自足复核只需stdlib：

```python
import json
from pathlib import Path
from fractions import Fraction
d = json.loads(Path('reviews/2026-10-29/weil-9-8-admission/negative-direction-independent-replay.json').read_text())
v = dict(zip(d['nonzero_support_indices'], map(int, d['integer_vector_on_support'])))
N = sum(int(a)*v[i]*v[j]*(1 if i == j else 2)
        for i,j,a in d['principal_block_upper_triangle'])
assert str(N) == d['integer_quadratic_numerator'] and N < 0
rho = Fraction(N, (1 << d['target_scale_bits'])*sum(x*x for x in v.values()))
assert -Fraction(1, 1 << 79) < rho < -Fraction(1, 1 << 80)
```

v的稀疏性只属于Kcert合同坐标。已付正合同变换是

    Kcert=T0·18²Cw² Bc*P0 Bc，T0>0，Bc非奇异。

因此对应P0系数方向是Bc w，physical有限源还须再经正交embedding E；Bc包含完整Vint，稀疏v不保低阶physical支撑。不能把这个14×14数据块叫原Q的低阶子型或低degree反例。

## 4. 严格结论与没有支付的结论

在root已消费的positive nonsingular congruence和原norm误差前件下，负Kcert方向确证本次P0不是PSD；同一个目标不可能有任何合法正Gram加严格正残差的证书。因此这一次固定配置的充分比较失败有精确数学证据，超出了单纯proposal inconclusive的数值标签。

但一般theorem只给P0≥0 ⇒ M+Kcompact+U≥0 ⇒ Q≥τI。负P0不反推后两者负性，未用tail及保守误差/逆比较余量可能补偿。没有取得9/8完整正性，没有RH反例，也没有排除所有inverse/Weil认证方法。固定配置改变后的目标是另一个对象，不属于本次负证书；本fresh没有安排参数续试。

Odd target虽已编译，odd Gram没有执行：实际`odd-gram.json`和成功`gram-receipt.json`均不存在。Even只有方向packet，没有factor或全部224行residual结果。不能报告两个sector的Gram符号均已检查，亦不能把failure receipt中的空`partialOutputs`读为没有保存even proposal。

## 5. 一条实际audit拒绝的准确限定

实际Gram access含且仅含一条`D:\codex-build\RH-Weil\<unknown>`的被拒绝read，必须原样保留，不能写成audit0或自动审批拒绝。程序的失败分支先在238作整数二次计算，再于508–509保存并回读even proposal，510抛出ValueError；548调用`traceback.print_exc()`，之后保存failure和access。独立负方向复核直接使用固定Kcert/v，不依赖该被拒绝路径。

另交只读子核`/root/weil_9_8_negative_replay/traceback_scope`对本机Python3.14.5异常格式化机制核验；它没有文件写入或science/Gram执行。独立只内存toy异常探针可复现恰一次rawPath=`<unknown>`拒绝，其实际栈为`traceback.print_exc → format_frame_summary:597 → _extract_caret_anchors_from_line_segment:842 → ast.parse:46`。拒绝被格式化路径吸收，原ValueError仍输出；不是linecache直接读取虚拟文件。

原actual access是聚合计数，没有逐事件时间或stack，所以原次精确归因只可说**与实测异常格式化机制一致**，不称原日志已经定位具体子调用或给出时间顺序。此限定既不隐藏audit事件，也不把异常显示读取等同于整数目标的数据输入。

595冻结草稿§3的Kcert/P0/Q方向、合同坐标与未执行odd范围正确；唯一建议是将异常读取归因保留上述推断限定。这个fresh只完成一个实际fixed-comparison失败证据的审查，不增轮、不给Goal完成门或新配置预算。Root仍须消费本原件和witness后统一结算。只读子核已terminal，无pending。
