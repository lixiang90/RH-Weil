# Expanded nine-point certificate: different-author mathematical review

日期：2026-10-08。审查者：`/root/high_product_joint`，不同于公开验证器、数据及论文作者。
判定：**限定 PASS**。未发现最终证书、完整连续域覆盖及原全零点计数桥中的阻断。
结论保留原 PC8 连续语义与编译计算信任前件；不称完整 Lean 内核证明或外部同行评审。

## 1. 本次绑定和实际读取

canonical LF 指 UTF-8 字节将 CRLF／孤立 CR 变为 LF，保留文件末尾。
以下最终源已实际全文读取；JSON 完整载入，所有 241 记录、237 点和 2399 对偶逐项重建。

| 文件 | 行数／LF 字节 | SHA-256 |
|---|---:|---|
| `scripts/am_expanded_nine_point_certificate.py` | 195／8854 | `05b7500d77bdb41cb5419137a1eee354250d7569572cd5c37d44a19a66b4eb4f` |
| `output/am-expanded-nine-point-certificate.json` | 380105／6252220 | `3a3c8b24015162a4835f5c1d8633a4f9f8bdace26d711631dd6374c689bce04f` |
| `papers/expanded-nine-point-tangent-simple-critical-paper.tex` | 418／18130 | `e69b5c4a34cc2fd3ec5c606faa175a37763fbd64534305b1e616a510afcdae31` |

418 行论文已全文重读；其半空间／方向叶／反射量词澄清未改计算数据或比例。
原 `tmp/pc8-am-admission/Solution.lean` raw SHA 为
`012c6ac5f9282158a686500dc0c967bf0a9b00e1a6192734d8f237bb23dd2d5f`。
已读其 PTF／PTL、REG／rgOk、`tcheckPZ`、`tangent_valZ`、`mokZ`／`mokTZ` 必要定义和证明；
192 个 PTL 列表的 2196 个点及完整 REG 由本次独立程序读取并核对。

旧公开 236 行验证器 SHA 为 `af5f2e1974bed92ad515f06ff6047f3e5595ac60c6dc721abd7bfb5cfd930c32`；
原 70 胞报告 SHA 为 `0733022044f96b37c6be3d5d5c1e9fa6c269545142d7d535e643c835a7cf38f6`。
报告所绑定其余八项依赖与新脚本本身均实际核 SHA；没有替换旧输入。
原两安全锚线与 Farkas 语义已在前轮独审完整核对，本轮再次逐式推导。
本人 126 行额外切线研究是研究输入，不把它列为本人独立审查的 PASS 对象。

## 2. 额外点的连续语义

固定 `SC=32768`、`E=10^9`，pack 给
\(v=V/10^{10}\le w(q)\)、\(d_-=(P-2E)/E\le w'(q)\le d_+=(2E-M)/E\)，\(q=p/SC\)。
这三个点值不自行推出全区间切线；真正前件是同一原 REG 凸区间及原列表 PTF。
每个新点分别满足
\[
k=(p+16384)\mathbin{\gg}15<16,\quad
A_k\le\min(L,p)\le p\le\max(U,p)\le B_k,\quad P,M\ge1.
\]
所以 supporting tangent 在整个扩大闭区间有效，原 `tcheckPZ` 的 `n=1` containment 分支亦通过。
单点跨度使用真实 \(U=L\)；常数 LB 查询的 `uc=max(U,L+1)` 不扩大真实切线域。
逐点使用所属 `PTL_i` 的 PTF，无需假设新的合并点表或 dispatch Soundness。

设切线真实导数 \(d\in[d_-,d_+]\)。在含 \(q\) 的 \([l,u]\) 上，两锚线为
\[
v+d_+(l-q)+d_-(x-l),\qquad v+d_-(u-q)+d_+(x-u).
\]
与真实切线的差分别为
\((d-d_-)(x-l)+(d_+-d)(q-l)\) 和
\((d_+-d)(u-x)+(d-d_-)(u-q)\)，均非负。
因此同一真实 \(z=w(x)\) 可同时满足任意多已认证锚线。
没有跨 \(q\) 非法取两条原导数端点切线的最大值，也不依赖浮点曲率。
237 个 catalog pack／list 编号全部和固定原源一致；924 次使用逐次核完整区间前件。

## 3. 完整低集合与重叠覆盖

原 \(c_0=805003/10^8\)，捕获门槛 \(c_L=805803/10^8\)，目标 \(c_*=805260/10^8\)。
只有原捕获程序的 stronger reward 调用和其诊断二分 fuel／上下界改变。
将这两处反向替换后，实际 capture 源逐字节还原冻结旧 `AffineCapture.lean`。
原 `cN`、返回值、整数 guards、树 bit cursors 与旧 root 比较未变。
全部 41 原 outer／root checks 为 true，241 条完整 LOWCELL／LOWPAID／LOWRAW／LOWYA 对齐。
全部 6266 原 atoms 和 YA 付款 guards 已独立整数复算；旧 70 几何胞的 atoms／YA 保持相同。

原 clear COV 支付 \(c_0+(4/5)B\)，large-gap 支付 \(c_0+(4/5)(B-\max b_r)\)；
额外压力分别为 \(0.0032348\)、\(0.002587136\)，都超过 \(8\cdot10^{-6}\)。
small-gap 分支在所有 gap≥4/5 时为空。原 32 root trees 因而仍覆盖剩余 low 情况。
方向叶仅在 \(h_6\ge h_0\) 半域排除；\(u_6<l_0\) 确与该半域不相交。
原成功叶中 stronger false 的 241 闭胞组成 low 集外覆盖；empty 叶真空。
完整反射补另一半域，得到 482 标签，不要求它们互不重叠或都是低点。
反射 \(r\mapsto6-r\)、\((i,j)\mapsto(7-j,7-i)\) 和 atoms 重排已独立核对；
原 YA 不被当成反向的新 witness。

独立枚举全部 \(482^2=232324\) 有序标签对：
共享六 gap 后 4796，对共享十五长 span 后 2405，完整闭包后 2399。
八 gap 和联合 27 个长 span 全约束进入九 prefix 差分图。
使用 \(5SC\) 单位精确加入 θ=4/5；负环判空、最短路 potentials 判真实连续可行。
没有以整数 ceil(θSC) 缩小真实域；所有边界和总跨度经 closure 正确处理。
2399 是可相交的标签对计数，不能宣传为互异几何域计数。

若一个 frame 不在 low 集，另一 frame 的原全域下界给
\[
F_9\ge(c_L+c_0)/2=805403/10^8>c_*.
\]
两个 frame 都低时，全反射 cover 及上述闭包把实际点放入某一已付款域。
这封闭 \([4/5,\infty)^8\) 的整个无界域，不是只在记录盒内或采样点上成立。

## 4. 全部有理付款的独立重建

本次独立程序不导入作者验证器、capture generator、SciPy 或求解器。
用稀疏系数字典重新构造全部真实 42 变量：八 gap、34 共享物理核平方；
其中 span 08 只用非负界，并未要求正的 \(w(\sum g)\)。
目标准确为 \(2\cdot10^8F_9\)，两 old frames 共用同一个物理 distance 的 z；
新增约束不改目标或 index-span≤2 的预算。核平方 box 为 [0,1]。

对每个正有理 sparse λ 独立检索行、核不重号，重算
\[
r=c+A^t\lambda,\qquad
c^tx\ge-\lambda^tb+\sum_i r_i(\ell_i\ {\rm if}\ r_i\ge0,\ u_i\ {\rm otherwise}).
\]
实际处理所有残差和全部闭 box，不假设 stationarity、optimality 或 float feasibility。
237 点／924 次使用的两锚线重新产生；只删 zero-dual extra rows 的压缩逐域不改原下界。
2399 lower 与报告、未压缩原数据完全相同；最弱标签对为 131／389，准确为
\[
M=\frac{26386790900531855994044477203}{3276800000000000000000000000000}.
\]
最小严格余量
\[
M-c_*=\frac{31220531855994044477203}{3276800000000000000000000000000}>0.
\]
因此浮点 LP 仅提供可审查的乘子，最终连续结论由完整有理证书支付。

## 5. 实际运行及可复核的输出

最终不同作者 scratch：`tmp/pdfs/am-more-tangents-high/independent_public_expanded.py`，
335 行／15444 LF 字节／SHA `14dbbd8014972cd4e139a56b7cd22e38ae6f8b9a28c50a4565aef9281a458865`。
最终完整运行 exit 0；结果 `independent-public-expanded-summary.json`，
20 行／751 LF 字节／SHA `daf01a6b7d27dbf2976e9942ebe686666a9abaa5f1fda14cf1b91259246ac2fa`。
两文件已全文读回；这是隔离诊断，不冒充另一个上游或 Lean 全重放。
公开最终 `--check` 实际 exit 0；`-O --check` 实际 exit 1，明确拒绝禁用断言。

已读取并严格解析全部实际 replay 日志：41 true、241 记录、无 error／sorry／panic／遗漏事件。
公开 replay artifacts 与已解析 root capture 逐字节相同：
`ExpandedCapture.lean` 11675／1042598，SHA `246328e2e6f30dad79b56f070ff98b8cc438a1cd5e7e67b3d3f1bc3b81615f9c`；
`capture-log.txt` 1035／601017，SHA `4b939f71d75e98ab5f6cf974c529eb1b7f3e33cecd5f36a770ec1a116626a87d`。
本审查没有另跑重量级 Lean capture；作者 final `--replay` exit 0 的产物已独立核对。
`--check` 验证已提交 packs；固定原源绑定由 `--replay` 和本次独立原 PTL／REG 比对完成。

## 6. 全零点运输与可宣传范围

418 行论文的无损装配逐式核：九点跨度预算≤2、总压力 B、总 pair weight<16，
滑窗扣八点端项和 smoothing 误差 \(32d_\epsilon m\)。
原连续 majorant 的带宽4/5、质量≤61/32、\(m_\epsilon>61/64\) 给 separated Gram norm<2；
最大不交近对删除后的集合确分离，近对原 \(K^2>1/40>c_*\) 支付两点。
凸谱 pinching 把所有简单临界线点纳入 \(J(U)\ge c_*n-B\operatorname{span}-8c_*-32d_\epsilon n\)。
全零点 Hermitian remainder 保留离线反射对及重复实零点，\(N-n\ge2n_+(Q)\)；
原 threshold minmax 给 \(\operatorname{tr}A^2\ge2N-n+J(U)\)，没有借窄条带削减 inertia。
固定 ε 先 T∞、再 ε0 的原无条件 correlation／去权桥保持 \(C(f_\epsilon)\)，不是有限点采样。
代入原 \(2-C(f)>67216841/10^8\) 给
\[
p_*=\frac{66812491}{99194740}=0.6735487284910470051\ldots .
\]
与前九点之差为 \(10489561087/9839612017241780\)，即约 0.0001066054 个百分点；
与固定 Knausgård v1 之差为 \(517622017/49164781738860\)，约 0.0010528309 个百分点。
这是原 PC8 计算信任前件下的真实新比例下界，不改善零点非零区域或原算术四阶预算。
replay clone 没有新增数学 axiom；打印 bridge 的 propext 不等于整条分析链的完整公理统计。
原连续／point／REG／compiled admission 仍须明示，不以 kernel-only、RH 假设或
Knausgård headline `native_decide` 的信任前件替代它，也不宣称已完成全球文献优先权核验。
