# 九点共同 minorant 正式论文的不同作者完整审查

2026-10-08，checkpoint_audit。结论：**限定数学与有限程序 PASS，无实质阻断**。
本次只新增本文件；没有修改论文、证书、旧研究源、Git 或旧审查。
canonical 身份按 UTF-8、CRLF/lone-CR→LF、保留 EOF 计算。

| 绑定输入 | 行／LF字节 | canonical SHA-256 |
|---|---|---|
| [九点论文](../../papers/nine-point-joint-minorant-simple-critical-paper.tex) | 828／33967 | 5a7499ddcdd290a25a39f568965c00bcc833975688553f2321ebf02643e538a6 |
| [仿射与共享距离源](am-affine-leaf-minorant-research-perron.md) | 167／10827 | f9616af18e61015682a3c41cebab630af72d9f107da1e9cb7424265875ad5a14 |
| [epigraph verifier](../../scripts/am_nine_point_epigraph_certificate.py) | 236／11009 | af5f2e1974bed92ad515f06ff6047f3e5595ac60c6dc721abd7bfb5cfd930c32 |
| [epigraph 数据](../../output/am-nine-point-epigraph-certificate.json) | 68844／1112534 | 0733022044f96b37c6be3d5d5c1e9fa6c269545142d7d535e643c835a7cf38f6 |
| [旧八点论文](../../papers/lossless-eight-point-simple-critical-paper.tex) | 635／24829 | 51c3931e3ce3ba54cd4a8441254ea0c8767009aee57e427f7f3492108b1a204c |
| [majorant／energy verifier](../../scripts/am_lossless_majorant_certificate.py) | 154／6671 | 11da56ae04a60fd436d273f39463e6aa85b0f023ebf62a0389c5f9af0b2aabf4 |
| [majorant／energy 数据](../../output/am-lossless-majorant-certificate.json) | 42／1396 | 61023fac589f2a8c8b3f67c8c296c38a2a244663129eb8bc90de6396c60fb915 |

## 1. 阅读与比较范围

逐行 FULL READ 最终828行论文、167行源、236行 verifier 和219行旧捕获器。
重读旧连续审查的点值、导数、切线及闭胞语义，并直接核隔离 Lean 核心中的
`tcheckPZ`、`mokZ`、`mokTZ`：只有非零混合权才要求相应点的独立有效切线。
旧635行论文复用此前完整审查，重核最终身份；其两个解析 subsection
“The unconditional analytic input”和“Retaining off-line zeros”与新稿逐字节相同。
本次没有把旧审查的 PASS 或哈希代替新增局部切线及滑窗推导。
上游固定 commit 在论文三处均为 `d272437e7ebeb17b87c8c3d7cece592aa23785ab`。

## 2. 连续低松弛覆盖与共享 epigraph

旧七 gap 式对全部非负实 gap 给 $F_8\ge c_0=805003/10^8$。
新式 $F_9=(F_8^-+F_8^+)/2+2K(\mathrm{span})^2$ 只需全部八 gap≥4/5。
任一帧不在 $F_8<c_0+2\delta$ 中即支付 $c_0+\delta$，其中 $\delta=10^{-6}$。
clear COV 单对奖励加 $\theta B=8087/2500000$，large-gap 单费加
$\theta(B-\max b_i)=5053/1953125$，均严格大于 $2\delta$；无穷尾未遗失。
小 gap≤1/2 分支为空，方向跳过的半胞经完整反射补齐，Farkas 叶仅排空胞。
捕获器先保留旧返回值和 cursor，只把 stronger clone 的唯一 reward 改为805203。
因此70个捕获胞来自成功旧叶的全部 strong-false 情况，不来自失败测试点。
旧41结果与原旧值／导数准入是不同层证据；新41项没有重新认证全部旧原子。

七 gap 与21长 span 保留闭区间；相邻两帧共享六 gap 和15 span。
其八 gap、27长 span 的完整差分闭包是实变量约束，5SC 中 θ恰为131072。
140标签／132几何胞、19600→422→289保留了反射、边界及不同 minorant 标签。
没有把这289个外胞说成全部点均低松弛，更没有限制真实 gap 为整数网格点。

对实际有效 tangent $v+d(x-p)$，两端锚定式分别减去
$(d-d_-)(x-l)+(d_+-d)(p-l)$ 与
$(d_+-d)(u-x)+(d-d_-)(u-p)$，均非负。
这证明每个启用点可独立给两条 cut；单点导数区间本身不能证明此事。
零宽查询的扩大值区间只用于常数 cut，真实端点仍用于 tangent。
两帧同一物理距离使用同一个平方变量；33旧距离加新跨度8共34个。
正概率窗给 $0\le K^2\le1$，故42变量的盒费用合法。
新跨度8变量没有正 cut，本次提升已经来自旧33个共享平方的联合消费。

对于 $Ax\le b$，$r=q+A^t\lambda$、$\lambda\ge0$ 的完整残量盒修正符号正确：
$q^tx\ge-\lambda^tb+\sum r_i(\ell_i\text{ if }r_i\ge0\text{ else }u_i)$。
不要求残量为0或信任浮点求解状态；目标精确等于 $2\cdot10^8F_9$。
源码逐项重建 captured atoms、原 guard、物理反射、matrix、box、非负 sparse dual。
实际 `--check` 消费全部289组；其最低值及正余量与论文312–318行完全吻合。

## 3. Direct sliding 与固定平滑

独立 Fraction 重算九点八个 span budget 均≤2、全部 $b'_r\ge0$、总费仍为B。
总 pair 权为1599999987/10^8<16；每窗平方改变≤2dε，所以32dε合法。
把 $m-8$ 个完整九点窗相加，任一具体 pair 总权≤2，任一 gap 总费≤B；
得到 $E_S\ge c(m-8)-B\operatorname{span}(S)$。m≤8时右侧非正。
平滑逐窗消费误差至多32dεm，未对整个无权 pair 集合收取 $O(dεm^2)$。

全连续 majorant 使用129节点严格余量9/100及全域导数<16，故余量≥47/800。
其 Fourier 端点在±4/5也为0；质量≤61/32。归一化必须使用
$f_ε=f\chi_ε^2/m_ε$，$m_ε>61/64$ 才有 separated Gram<2。
近对真实核满足 $K^2>1/40>c$，平滑后每对 $J\ge2c-4dε$。
maximal disjoint near pairs 留下 θ-separated 集合，scalar convex pinching 对全 Gram 合法。
所得 $J(U)\ge cn-B\operatorname{span}(Y)-8c-32dεn$ 中8c只扣一次，
空 separated 集、m≤8、边界距离等于θ及配对误差均被包含。

## 4. 全零点计数与极限

每个固定ε的 BGST signed fixed-test 输入用于 $q=f_ε*f_ε$ 和 $q''$。
移除相关权的二阶导数恒等式与2π尺度正确；未假设RH或更高相关猜想。
在复 $L^2$ 先定义 $v_z$，再取真实反射型 g/h；$Jv_z=v_{\bar z}$。
离线对有一个正方向和一个负方向；其完整权是μ，不被临界线投影删除。
重复实点同样保留完整μ；simple P 只含 n 个单位 feature。
直接 tensor 展开给 $\operatorname{tr}A=N$ 及全重数 HS 平方 $C(f_ε)N+o_ε(N)$。

$n_+(Q)\le b=r+k$、$N\ge n+2b$ 对任意真实重数成立。
有限 minmax、填零 Gram 特征及 $4t-t^2\le4p-\phi_2(p)$ 正确；
尾部非正谱未丢成正能量，给 $\operatorname{tr}A^2\ge2N-n+J(U)$。
没有额外收取或消费尚未支付的 strip、Schur residual、负迹或四素数增益。

计数跨度≤$T\log T/(2\pi)$，与N之比→1；先固定ε并令T→∞，再ε→0。
$f_ε\to f$ 的 $L^1\cap L^2$ 收敛支付能量极限；8c仅在除以N后消失。
实际 AM 自身 correction 被完整扣除，绝非替成未扰动MT能量。
独立 Fraction 重算附录短能量包络、close pair、所有 span budgets 和两个比较差值。
结果为 $66812491/99194897=0.67354766243670780766071061095\ldots$，
论文的弱不等式由严格能量余量支持，abstract末位7078正确。

## 5. 实际执行与证据边界

运行 `C:\Python312\python.exe -B -X utf8 scripts/am_nine_point_epigraph_certificate.py --check`，exit0：
`PASS 289 exact nine-point epigraph duals; local reward >=805103/100000000`；
最低值 `65955289561887369906031994339/8192000000000000000000000000000`。
旧 `am_lossless_majorant_certificate.py --check` 实际exit0，连续 majorant／AM energy／report PASS。
本次独立 Fraction 算术运行exit0，不导入这两个作者 verifier 作为独立算术证据。
没有再执行大PC8搜索、Lean捕获或 native headline 搜索；复用已披露的旧连续准入及实际捕获。
**PASS** 指论文完整数学传递和本次有限消费；标准整数执行的旧240项信任边界仍存在。
有限 verifier 本身不证明无限解析输入，不是完整 Lean kernel theorem 或外部同行评审。
新 local reward 的确改进此 simple-critical 比例；未宣称新零点条带、全RH或原四素数省幂。
