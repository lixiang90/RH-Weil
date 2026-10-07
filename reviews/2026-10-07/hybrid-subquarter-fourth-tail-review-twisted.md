# 452 原矩阵 subquarter padding 与四次迹尾：独立复核

2026-10-07。审查人：`twisted_research`。结论：**限定 PASS [T/R]**。
本报告独立审查 452 全文、上游双侧零点尾与全高度压缩证明、精确脚本和输出；
未以有限脚本替代解析证明。只新增本审查，未编辑主稿、源 math 或任何论文。

## 1. 最终文件绑定及范围

Markdown、TeX、Python、JSON 均按 CRLF/CR→LF、UTF-8 计算。

| 文件 | canonical LF SHA256 | canonical UTF-8 bytes |
|---|---|---:|
| [452 主稿](../../notes/452-subquarter-padding-and-fourth-trace-stability.md) | `9e6071870a7203ce97e5489cf3178ee8681abf36014db790a8b60d8fa4895bbc` | 12296 |
| [精确脚本](../../scripts/hybrid_fourth_tail_exact_audit.py) | `892aabba5cb40e84fd1982600f4c442617ac581130c05e37f7f5875d1ba0200a` | 4079 |
| [精确输出](../../output/hybrid-fourth-tail-exact-audit.json) | `a80f01630284c83657ae04e594977150c96593cb5411047a43966016f229746d` | 1826 |
| [三次边界论文](../../papers/kappa-feedback-cubic-boundary-paper.tex) | `16c0ba50a2917f2ead56843eabf55b62fbbe214e162cff373b4d8554f84315ee` | 39181 |
| [438](../../notes/438-seven-eighths-and-zero-proportion-interfaces.md) | `1b5109396c89efab2f1ad0fa2d4281ab2c7e53ba9ed25900e86f29dc83ea3283` | 9935 |
| [446](../../notes/446-uniform-prime-twists-on-the-original-gabor-frame.md) | `08060477a6ea806d559fd67533d9e6d3b96483a755842cca9a048b6ab5e110cf` | 9890 |
| [padding 完整源审计](hybrid-proportion-source-audit.md) | `0fde3540f6880e34afa784a46b8c6009f098b211f82ac79f65efcc1a7d8b5992` | 16635 |
| [全高度 norm 接口](hybrid-uniform-reciprocal-and-fourth-trace-interface.md) | `25468f8c29dc195d08083dd0fb4b60b5aea48478c9c1ce93053875d5dcc7d83c` | 20998 |

452 的外部 [R] 为原三次边界论文已经明确列出的通用源输入、同族延拓、
quadratic transfer，以及 AF 原显式公式、零点计数、原 C² 窗和全矩阵二矩。
本复核接受它们作为明列输入，不重新认证其完整底层解析／形式化证明。
原 math `paper.tex` 固定提交 `adc7f1241b42e322a6451854ab7e4b4c146bf78a`，
canonical SHA256 `42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`。
只读重核了该源 `lem:logarithmic-control` 的完整 disk 证明及量词。

原始 AF 约定另对照
[v2 §2、§4、§5](https://arxiv.org/html/2608.13637v2)。
本次对象是固定 ζ 的原 finite Hermitian matrix；不是 moving-conductor
Dirichlet 全族的统一四矩定理。没有审查或绑定 PDF 版面。

## 2. 已纠正的一般范围

审查初稿时发现 §4 的实质范围错误：
`theta>3/4` 和 `r>2theta-3/2` 不一定推出
`theta-1/2-2r<0`。例如 `theta=4/5,r=3/25`，四迹的第一个门槛满足，
但迹范数尾的幂指数为 `3/50>0`。

根节点已将最终 (17) 修正为

\[
 \max\left(2\theta-\frac32,\frac\theta2-\frac14\right)<r<1,
 \tag{R1}
\]

并明确第二项专门保证 trace-norm 尾为 `o(1)`。
当 `theta>5/6` 时，第一项才强于第二项。当前 `theta=sigma_*` 属于该范围，
所以具体 subquarter 实例从未受此错误影响。最终稿的修正已逐字复核；
本 PASS 绑定修正后的 `9e607187...`，不适用于初稿的一般范围原句。

## 3. 原零点矩阵、复转置与双侧尾

452 的 `v_rho v_rho^t` 使用复转置；它不是单个 positive rank-one 矩阵。
对原实偶窗，`hat phi(conj z)=conj hat phi(z)`，反射配对
`rho↔1-conj rho` 保留相同实高度，所以按实高度截断后的总和是 real symmetric，
因而 Hermitian。配对没有被拆开。

所有非平凡零点的深度由 `[R]` 与函数方程控制为
`|Im gamma_rho|<=d_0=theta-1/2`。原 Fourier 界平方的指数因子为
`exp(L d_0)≍T^(d_0)`。半侧物理 grid 与距离 `R>=1` 的积分比较准确给

\[
 \sum_{k\ {m separated}}|\widehat\phi(\gamma_\rho-\alpha_k)|^2
 \ll T^{d_0}(R^{-4}+LR^{-3})\ll T^{d_0}LR^{-3}.
 \tag{R2}
\]

复 rank-one 的 singular value 为 `||v||²`，所以除以实际 `a_L L²` 后，
单零点迹范数尾是 `O(T^(d_0)L^-1 R^-3)`。在 `|t|<=3T` 用单位高度
零点数 `O(log T)`；其 `log T/L` 为常数。远处左右两尾由
`int_(3T)^infinity log t/t³ dt=O(L/T²)` 支付。故统一于 `1<=P<=T/2`，

\[
 \|E_P\|_1\ll T^{\theta-1/2}P^{-2}.
 \tag{R3}
\]

该绝对迹范数估计也证明定义 `H` 的全零点和收敛。矩阵维数是原
`D_T=floor(XL)`，不误用离线深度符号，也不依赖错误的 `D_T=N+O(L)`。

首迹端点账本正确：内侧零点用完整 complex Poisson identity 减外网格尾；
padding 零点必须估计内网格贡献。距离端点不超过 1 的零点只有 `O(L)` 个，
每个截断贡献的绝对值至多 `O(T^(d_0))`。得到
`Tr G_P=N(I)+O(T^(d_0)L)`，再独立付 `N(I_P)-N(I)=O(PL)`。
没有把 padding 点误认为远离全部外网格。

## 4. 全高度算子范数重新核验

固定 `theta<a<1`，其 gap 在 `T` 前选择。原 disk logarithm 证明只使用：
Euler 中心值有界、固定 strip 多项式增长、无零 disk、固定半径余量。
因此把零点右界换成 `theta` 后，在 `Re s=a` 的同一 proof 上得到
`|zeta'/zeta(a+it)|≪_(a-theta,1-a) log(3+|t|)`。
principal regularizer 的导数需再加 `1/(s-1)-1/(s+1)`；固定 `a<1` 的直线
距 pole 正距离，而 Perron horizontal joins 的高度远离 pole。
没有以 moving `a-theta=1/log T` 隐藏常数。

452 保留 sharp `n<=X` 与原 `Lambda(n)/sqrt n`。半整数
`x=floor X+1/2` 和 `Y=(2x(3+|tau|))^4` 使 Perron endpoint 与水平误差可付。
移至 `Re s=a-1/2>0` 只跨越 principal pole
`s=1/2+i tau`；`s=0` 未跨越。其留数确为
`x^(1/2+i tau)/(1/2+i tau)`。左线积分的 `1/s` 付一次 `log Y`，
logarithmic derivative 再付一次，得到原 (10) 的 `log²`。
`tau` 是绝对 height，不是 four-word difference。

原 `||U||²<=2pi L` 与 normalizer `a_L L²` 将 `J=[T/2,3T]`
内的前缀误差除以 `L`，给
`||V_J||op≪T^(a-1/2)log T`。外侧仍保留全 height
`|P_X|≪sqrt X`；所有 carrier centers 到 `J^c` 的距离至少 `T/2`，所以
`Tr(U*1_(Jc)U)≪D_T T^-3≪L/T²`，给原 (12) 的
`sqrt X/(LT²)`。低绝对 height 的 principal 大项在这里付款，没有删掉。

Gamma 压缩在 `J` 内按 `O(L)`、在外侧按真实 `log(2+|t|)` 积分；pole
压缩在内侧按 `sqrt X/T`，外侧按 `sqrt X`。因此原背景减 `I` 的 operator
norm 为 `O(1)`。直接得到整个

\[
 B=H-I,\qquad\|B\|_{\rm op}\ll1+T^{a-1/2}\log T.
 \tag{R4}
\]

这不需要原响应四范数的待证常数，也没有改成 translation-invariant bulk。

## 5. 非交换比较、精确指数与量词

重新在自由非交换字代数中展开原 (14)：中间六项准确消掉，剩下 `A^4-B^4`。
在迹中用 trace-ideal inequality 后是

\[
 |\operatorname{Tr}(B-E_P)^4-\operatorname{Tr}B^4|
 \le4\|E_P\|_1(\|B\|_{\rm op}+\|E_P\|_{\rm op})^3.
 \tag{R5}
\]

没有 scalar binomial replacement。以 (R1) 先保证 `E_P=o(1)`，用 (R3)、(R4)
并除以 `N≍TL`，总幂指数确为

\[
 (\theta-1/2-2r)+3(a-1/2)-1=\theta+3a-3-2r,
 \tag{R6}
\]

日志由 `log³ T` 除以 `L` 后为 `log² T`。

独立有理计算确认 cubic 的根隔离、`theta<437479/500000`、
`a=87497/100000`、`r=6249/25000`。相应三个严格上界是

\[
 \theta-1/2-2r<-62481/500000,
 \quad \theta+3a-3-2r<-13/250000,
 \quad \theta+3a-7/2<-33/250000.
 \tag{R7}
\]

因此归一化四次迹差是 `O(T^-0.000052 log²T)=o(1)`。
按 `log² T≪T^(13/500000)`，进一步弱化为原 (21) 的幂界正确。
旧 `theta=7/8` 时，对固定 `a>theta,r=1/4`，本组输入给正指数；
这只限定这一条 op/trace-tail route。当前界允许每个固定
`r>2sigma_*-3/2≈.249914038840197892`，不支付端点或 moving gap。

量词顺序是：固定 `[R]` 下的 `theta`、固定 profile，再选择严格门槛内的 `r`
与固定 `a`，最后令 `T→infinity`。常数可依赖这些固定 gap；主稿没有把极小
固定 gap 变成可计算有限高度结果。全部实例使用同一个 `H/G_P` 和同一个 normalizer。

## 6. 首迹、二矩与真正成果范围

AF 对完整 `H` 的原二矩先给 `||H||²_HS=O(N)`；由 `E_P=o(1)`，
再推出 `||G_P||²_HS=O(N)`，不存在先假定 `G_P` 二矩再证明自身的循环。
原 (23) 的二次迹比较直接由
`Tr(H-E)^2-TrH²=-2TrHE+TrE²` 给出，费用 `o(N)`。
首迹、`N(I_P)=N+o(N)` 与共轭封闭零点惯性都保持。

若以后在同一实际 `H` 上付出固定 `B_4` 的原 centered fourth bound，
(R5) 确能以相同 `B_4` 传到 `G_P`，不需另加一个循环的 fourth-norm 前件。
但是 452 本身没有计算 `B_4`，也没有支付 prime correlations、four-distinct
words、背景 mixed terms或所有 low/high mixed words。
因此“截断稳定性新接口”成立；“新比例或无零边界”不在其结论内。

## 7. 脚本与输出复现

只读执行 `runpy.run_path(...,run_name='audit_module')['certify']()`：
没有运行脚本的写输出分支。返回对象与当前 JSON 输出逐字段相等；所有读取文件
的 canonical hashes/bytes 与本审查表相符。
另外用 5 个不同有理 `theta` 点检查修正后 max-threshold 的两条门槛及 `a` 区间非空。

脚本确实读取并哈希当前 note、paper 与自身；cubic 符号和 derivative 上界使用
`Fraction`，telescoping 在自由字上精确检查。输出明确写有限代数范围，排除
外部 source theorem、零点尾、算子估计和 prime moments。本审查的解析结论
来自以上独立纸面核验；不把脚本 PASS 视为 Lean、RH 或完整源整链认证。

最终状态：**限定 PASS [T/R]，针对表中最终 452 及原固定 ζ 有限矩阵**。
