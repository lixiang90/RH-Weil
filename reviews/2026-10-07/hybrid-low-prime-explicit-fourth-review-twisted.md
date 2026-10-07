# 453 原低素数显式一侧四矩预算：独立复核

2026-10-07。审查人：`twisted_research`。结论：**限定 PASS [T]**。
独立核对 453 全文、原 finite frame 的正规化、全部实部不平衡词、全 height 尾、
proper-power transfer，以及有限审计脚本及输出。未编辑主稿、旧论文或 math。

这里 [T] 接受明列的经典 Chebyshev–Mertens、Montgomery–Vaughan Hilbert inequality
及 AF 原窗／Fourier 恒等式。不使用项目无零包 [R]、7/8、三次边界或 RH。
结论是同一原低 `Lambda` 压缩的上界；不是它的 exact fourth main term，也不是完整
Hermitian response 的四阶常数。

## 1. 最终文件绑定

以下 hash 按 CRLF/CR→LF、UTF-8 计算；PDF 为二进制。

| 文件 | SHA256 | canonical UTF-8 bytes |
|---|---|---:|
| [453 主稿](../../notes/453-explicit-low-prime-fourth-moment-budget.md) | `0df65e79b5875fc0e5f7110ceaa05723e4db0cca0b3cc443551c7005a700ddf6` | 10115 |
| [有限精确脚本](../../scripts/hybrid_prime_sector_exact_audit.py) | `147f203ebb3f2c6150323bbf65a2be9e5ade99255f6490b0cc23294f050e2302` | 5750 |
| [有限精确输出](../../output/hybrid-prime-sector-exact-audit.json) | `3a5f22466ae69e467b46366d9c1898c566d1437ca65ba3cdfcd56b42bbb91ac6` | 2759 |
| [448](../../notes/448-canonical-type-i-admission-finite-gram-and-low-prime-fourth-norm.md) | `6a7219f929cc50a721227c722fd9553eb7eba1ed9d4dd432bd971b39c2e6eafa` | — |
| [452](../../notes/452-subquarter-padding-and-fourth-trace-stability.md) | `9e6071870a7203ce97e5489cf3178ee8681abf36014db790a8b60d8fa4895bbc` | 12296 |
| [原 proper-power 推导](hybrid-joint-type-ii-fiber-research.md) | `238fd374cad6da451fd186c6f3766d79d869ff8ae92ed6441e0ca516e1398473` | 17846 |
| [AF v2 PDF](../../literature/baseline/2026-alpoge-furman-6725-v2.pdf) | `6de3b156342e7b4a802c34f8ef40432567e9dabe006938da04233f19fc4ef444` | 二进制 478663 |

原始文献独立查核为
[AF v2 §2](https://arxiv.org/html/2608.13637v2#S2) 与
[Montgomery–Vaughan Theorem 2、Corollary 3](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)。
没有引用有限脚本来证明任何无限 prime sum、均值或 projection 估计。

## 2. 乘积碰撞与 weighted mean value

只对 genuine primes 定义 `b_p=log p/sqrt p`、`Q_Z=sum_(p<=Z)b_p p^(it)`。
unique factorization 准确给 `c_(pq)=2b_pb_q`、`c_(p²)=b_p²`。故

\[
 \sum_n|c_n|^2=2\left(\sum_pb_p^2\right)^2-\sum_pb_p^4,
 \quad
 \sum_n n|c_n|^2=2\left(\sum_p(\log p)^2\right)^2-\sum_p(\log p)^4.
 \tag{R1}
\]

不是把同一个 `p=q` collision 算两次。第一项的对角扣除为统一 `O(1)`，
第二个加权总费为 `O(Z² log²(2Z))`；这里少两个日志是真实改善。
若只保留 `Z² sum|c|²` 的粗界，则在 `Z²=X` 无法得到同一主常数。

频率 `log n` 的局部间距至少 `1/(2n)`。MV Hilbert 对 interval 的两个
endpoint 逐个付款，phase `n^(iA)` 是单位相位，因此 bound 对任意起点 `A`
统一，得到主稿 (7)。`Z=X^rho,rho<=1/2` 时，其 error
`Z²log²(2Z)=o(TL⁴)`。原 carrier 高度 `T` 没有被换成 0。

Mertens 的 `S_Z=(1/2)log²Z+O(log(2Z))` 只使用原 `Lambda²/n` 公式及
收敛的 proper-power 差额；`R_Z≪Zlog(2Z)` 用 Chebyshev。

## 3. 实部展开的全部非平衡词

独立展开 `(Q+bar Q)^4/16`，其系数确为

\[
 (\operatorname{Re}Q)^4
 =\frac38|Q|^4+\frac12\operatorname{Re}(Q^3\overline Q)
                 +\frac18\operatorname{Re}Q^4.
 \tag{R2}
\]

四同号的频率至少 `log16`，endpoint exponential integral 的绝对值不超过
`2/|frequency|`。`sum_p b_p≪sqrt Z` 给 `O(Z²)`，不依赖 interval 长度。

三正一负中，正侧整数 `n=p_1p_2p_3` 是合数，故永不等于负侧 prime `p`。
允许所有 repeated prime labels；不存在被漏掉的 resonant diagonal。
`C_3(n)` 的 positive 总和用 Chebyshev 先求第三个 prime，再付两个
`sum(log p)/p`，统一得到 `sum_(n<=y)C_3(n)≪ylog²(2y)`。

在 `p/2<=n<=2p` 中，`n<=2Z`、`sqrt(np)≍n`，
`1/|log(n/p)|≪n/|n-p|`；扩大负侧 prime sum 为整数 harmonic sum，
对每个 `n` 至多付 `C_3(n)log²(2Z)`。近区总费因此是 `O(Zlog⁴(2Z))`。
远区的 log denominator 至少 `log2`，全部 coefficient mass 为
`(sum b_p)^4=O(Z²)`。主稿 (13) 同时保留所有 sharp prefix 和 endpoint phases，
未调用 prime-pair／prime-triple correlation。

由此 balanced coefficient `2S_Z²` 乘 `3/8` 得
`(3/4)H S_Z²=(3/16)H log⁴Z+O(Hlog³(2Z))`。
`H=O(T)` 的全部剩余费用在 endpoint `Z=sqrt X` 仍是 `o(TL⁴)`。

## 4. 原 finite compression 的正确一侧正规化

保留 `D_T=floor(XL)`、`alpha_k=T+2pi k/L`、
`f_k=hat phi(t-alpha_k)`、`F=U/sqrt(2pi L)`。
原 support 内的 exact grid 正交性给 `F*F<=I`。
对任一 finite Hermitian eigenvector，`|Fv|²dt` 的缺失质量放在 0，
scalar Jensen 可用于 `x^4`；它不要求 operator convexity。

直接重算原 `P_Z^pr=2pi/(a_L L) F*M_ZF`，其中
`M_Z=-pi^-1 Re Q_Z`：

\[
 \operatorname{Tr}(P_Z^{\rm pr})^4
 \le\frac{8}{\pi a_L^4L^5}
 \int_{\mathbb R}\sum_{k<D_T}|f_k(t)|^2(\operatorname{Re}Q_Z(t))^4dt.
 \tag{R3}
\]

每个 `pi`、`a_L`、`L` 均与主稿 (15) 相符。完整 grid 的平方和为
`a_L L²`，finite grid 是其正子和；应用它后系数为 `8/(pi a_L³L³)`。

对固定 `epsilon>0`，原 `J_epsilon=[(1-epsilon)T,(2+epsilon)T]` 长度
是 `(1+2epsilon)T`，于是内部正 majorant 为
`8/(pi a_L³L³) × (3/16)(1+2epsilon)T(rho L)^4+o(N)`。
除以 `N∼TL/(2pi)` 并乘 `a_L³`，系数准确为

\[
 3\rho^4(1+2\epsilon).
 \tag{R4}
\]

外侧所有 carrier centers 的真实距离至少 `epsilon T`。
原 C² Fourier 尾給 `sum_k int_(Jc)|f_k|²≪_epsilon D_T T^-3`；
全 height `|Q_Z|≪sqrt Z` 保留后，(R3) 的外费确为
`O_epsilon(Z²/(T²L⁴))=o(N)`。低绝对高度包括在这项内，没有偷用 high-height PNT。

只分割正 scalar majorant，不把 matrix fourth 拆成两个无 mixed words 的四迹。
先固定 profile、rho、epsilon，再令 `T→infinity`，最后 `epsilon→0`。
没有 moving taper、moving epsilon 或未支付导数常数。
因此 (1) 的 prime-only limsup 成立；`a_L` 仅需统一正下界。

## 5. Sharp proper powers 与非循环 transfer

直接对同一个 `p^j<=Z` 前缀，`j>=2`，核验
`||Q_Z^pp||infty≪log(2Z)` 和 squared coefficient mass 的统一收敛。
weighted error 是 `sum_(p^j<=Z)(log p)²≪sqrt Z log²(2Z)`；
`Z<=sqrt X` 使其小于 `O(T)`。这不是从另一 arbitrary subsequence 的取消
移植来的结论。

原 Bessel／normalizer 给 `||E_Z^pp||op=O(log Z/L)=O(1)`；
scalar squared compression 和真实外尾给 `Tr(E_Z^pp)^2≪N/L²`。
谱上 `lambda^4<=||E||op²lambda²` 给 `Tr(E_Z^pp)^4≪N/L²=o(N)`。

prime-only 低矩阵已经由 (R3)–(R4) 独立证明四范数 `O(N^(1/4))`。
因此只在这个已准入 low matrix 上以 Schatten Hölder 和非交换 telescoping
付 proper-power mixed words，差额 `O(NL^-1/2)=o(N)`。
这里不需要完整 high/low response 的待证四范数，故没有循环前件。
原 `Lambda` prefix 的主稿 (1) 因而成立。

flat 合法 smooth taper 的 `a_L→1` 给 `rho=1/2` 的 `3/16`。
MT 等其他 profile 的 `a_infinity` 不等于 1，必须保留 `a_infinity^-3`。
也没有声称 scalar Jensen 在原 compression 上取等。

## 6. 有限脚本及真正结论范围

只读调用脚本的 `certify()` 而不运行写输出分支：返回对象与当前 JSON 完全相同，
实际输入文件／自身的 hashes 和 bytes 与绑定一致。4 个 cyclic free-word 模型、
2 个 formal prime-product coefficient 模型、`19/480` 与 `3/16` 的有理算式均通过。
local residue 部分的 41 次计数来自 `2+3+5+7+11+13` 个 residue classes；
每个 prime 的单位四元组计数与指定 factor 符合，period `30030` 的平均等于 1。

最终绑定复核：critical 草稿收紧量词，并在 §6.1 明确先固定 `ell,m_s` 及
`I_P/total z` 再求和后，重新生成了 JSON；当前 critical 输入 hash 为
`ef85a5e5fd5aef3543aef6eb4b6adff6a1ecd39791575a89704e4b08e04e8983`，
19827 canonical bytes。
再次只读执行 `certify()`，返回对象逐字段等于当前 JSON。输出绑定已更新为表中
`3a5f2246...`，仍为 2759 canonical bytes；脚本、453 正文与全部有限检查结果不变。
该输入绑定更新不扩展本报告的分析审查范围。

这后一有限 reference 计数与 453 的解析证明相互独立。它不认证 actual primes 的
无限 singular series、Hilbert mean value、projection leakage 或实际四点相关；
输出已明确排除这些范围。本 PASS 的无限均值结论来自以上纸面核验。

453 的新成果是 **原低 Lambda 压缩的显式 one-sided 常数**，可作为完整四矩
研究中的一个真实预算。高 prime repeated sector 的 `19/120` 与 low 的 `3/16`
不能简单相加而声称完整 `B_4`：仍有 low/high mixed words、four-distinct primes
及所有原 background mixed terms，也仍需共同 centering／cross-cell／alias 账本。
主稿这些限定完整，未声称新比例、新边界、Lean 或 RH。

最终结论：**限定 PASS [T]，绑定上述最终 453**。
