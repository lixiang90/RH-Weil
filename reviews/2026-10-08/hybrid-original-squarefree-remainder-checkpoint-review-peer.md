# 原平方自由余项有限检查点：不同作者短独审

2026-10-08，checkpoint_audit。检查器作者为root，审查作者不同。
仅新增本文件；script、JSON、冻结数学源和已有peer保持原版本。

**限定有限范围 PASS。** 两个最终文件均逐行 FULL READ；独立
exact Fraction、不同参数的有理 Euler 构造和实际只读重放均通过。
本文件不把62项有限检查解释为无限解析证明。

## 1. 固定身份与执行

| FULL READ 对象 | 行数 / canonical LF字节 | canonical UTF-8 LF SHA256 |
| --- | --- | --- |
| [最终脚本](../../scripts/hybrid_squarefree_remainder_checkpoint.py) | 317 / 14772 | b41122299a8492c156b9c1e4bb081b31d109666c220d9445210a3b483815562d |
| [最终保存输出](../../output/hybrid-squarefree-remainder-checkpoint.json) | 432 / 13101 | fcc0b2e6c04b402b8794f8b5594fd536f40c4285c88d1efb79c4004ff20a2976 |

实际在 E:/codex-build/RH-Weil 执行
C:/Python312/python.exe -B -X utf8 scripts/hybrid_squarefree_remainder_checkpoint.py --check。
退出码0，stdout为：

> PASS: 62 finite checks; analytic proofs are separate

代码299—313行核明 --check 只读取保存JSON，不进入 --write 分支；
-B 避免 Python bytecode 输出。重放之前已完整阅读外部待执行代码。
脚本与JSON在执行后再次核hash，均保持上表身份。

## 2. 代码、记录和scope核对

脚本43—177行保留 valuation≥2 的真实 squarefull r、k>V、
ae≤V、(a,r)=1，以及所有 genuine primes / proper powers。
finite local inverse factors 通过全部允许 prime powers 展开；
原 k≤V 的零系数和 squarefree 的 -1 明确检查。
log(p) 作为独立 formal prime basis，避免浮点 log 的误判。
FU只扣 small genuine primes，Qpp扣全部 proper powers；正是实际身份。
172—173行的末尾 proper-power convolution 检查消费已验证的两个
相同 k 数组，因此是再确认，不能计作新的独立解析输入。

62个顶层记录由9个冻结身份、20组正式系数case、10组weighted
有理特化和23个费用/guard/根区间算术记录组成；不是62个解析定理。
各case里的4N是有限系数检查的记录标签，也不是无限参数覆盖。
独立读取JSON并重核全部9个绑定hash；其script字段亦与最终脚本一致。

递归检查所有以 proves_ 开头的键：8个顶层及10个nested特化键，
共18个均为Boolean false。formal_log_prime_basis=true只指该有限
系数表达方式。schema、status及arithmetic分支均未认证 complex
uniform convergence、weighted prefix、∞Euler、∞Perron、ζ四矩、
complete fourth moment、新比例、无零边界或RH。

## 3. 独立 Fraction 费用及根包络

未导入待审script。另写只读内存运算，用 Fraction 直接构造
完整费用向量，得到
(1/2,1/2,1/4,1/2,1/2,0) 和
(3/7,3/7,3/14,3/7,3/7,0)，最大值分别1/2、3/7。
完整传递分别37/56、9/14；前次误差及传递节省1/34、1/136准确。

独立用 Horner 计算451 cubic两端异号，并以导数有理upper验证
整个 e 区间递减。θ两端由11/12−e/4反序得到。
将传递式独立化简为

\[
 \gamma_{\rm half}(\theta)=3\theta-\frac{13}4+\frac9{8\theta},
 \quad C_{\rm weighted}(\theta)=1-\frac1{2\theta},
 \quad \gamma_{\rm weighted}(\theta)=3\theta-\frac{25}8+\frac1\theta .
\]

三式在所见θ区间递增。exact Fraction的两端值与JSON的三对
rational endpoints逐项相同，并验证显示的三个严格decimal包络。
费用分支另核7个不同θ值，包含额外2/3、17/20、19/20；
只作为代数交叉核对，不扩大任一原解析合同的θ范围。

## 4. 独立有理 Euler 系数构造

使用N=211，r∈{25,81,100,200}、w∈{1,3}共8新组，
与脚本的N=128及r列表不同。未调用或导入其factor/convolution函数。
先用sieve取得primes；再通过解1*inv=δ的有限递推构造 inverseζ
系数 inv(n)，而非调用检查器的trial-factor μ。
然后按逐prime几何Euler多项式相乘构造 K 的全部≤211系数：

- p|r 时，K_p(z)=(1−p^(-z))^(-1)；
- p∤r 时，K_p(z)=1+[1/(p^w+1)]Σ_(j≥1)p^(-jz)。

左侧另取 inv(n)1_((n,r)=1)Π_(p|n)p^w/(p^w+1)，
右侧按divisors直接计算 Σ_(d|n)inv(d)K(n/d)。
全部8×211=1688个 rational coefficients相等；内存交叉核退出码0。
这里w是整数特化参数、z是formal Dirichlet变量。它不证明复杂
half-plane上的统一绝对收敛或实际weighted prefix估计。

无限解析范围仍由[395源的独立审查](hybrid-original-squarefree-core-euler-perron-review-peer.md)
及[weighted源的独立审查](hybrid-original-weighted-mobius-squarefree-perron-review-peer.md)
各自限定。有限62项、9个hash和本次1688项交叉核不能替代这些证明。
