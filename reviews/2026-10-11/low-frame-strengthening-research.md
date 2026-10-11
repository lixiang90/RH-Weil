# 2026-10-11：单帧加强突破 high–low 外域预算

发布说明：以下为独立子任务原始记录，涉及tmp路径和开始审计时的基线。当前研究状态见[504](../../notes/504-low-frame-strengthening-and-mixed-sixth-restoration.md)；旧c403形式化与新c4119数学证书分别记录，本文未执行新增Lean验证。

本报告只记录数学研究。没有修改已发布 Lean、README 或论文，没有运行 Lean，没有推送。
`c411` 初稿与最终较强变体分别冻结；最终可用简洁奖励

\[
c_*=\frac{8054119}{10^9},\qquad
\liminf\frac{N_0^s(T)}{N(T)}>
\frac{668124910}{991945881}=67.35497599188075\ldots\%.
\]

它比已发布 `941021/1397107` 提高
`8375086900/1385854533966267` 个百分点，约 `0.0000060432655` 个百分点。
数学证书沿用已准入的连续 AM 核、原完整捕获及全零点计数运输；
没有借旧形式化宣称新数值已经 Lean 或 NaNoDa 认证，也没有网站验收结论。

## 1. 真正改变的输入

503 的强捕获仍为 `805803/10^8`，241 个原闭低胞及 241 个反射完全不动。
此前外域只消费另一帧 `F8≥805003/10^8`，因此外域付 `805403/10^8`。
本轮在单帧实际七个间隙、26 个物理平方中重新支付十个薄弱原胞；
其余 231 个原胞逐一保留原 YA 的**未舍入精确值**，从而闭合

\[
F_8(g)\ge\frac{805021}{10^8}
\quad(g_0,\ldots,g_6\ge4/5).
\]

这是对原全域八点前件的真实加强；没有从 2399 个低–低域的数值余量单独推出全域结论。
最初真实 high→low 联合 LP 也包含左高帧、共享平方和新增左间隙，发现其收益主要来自
单帧低奖励。最终删去这个辅助间隙，采用更简洁的 33 变量单帧证书。

## 2. 十个单帧补丁与合法切线

薄弱原标签完整集合：`17,53,64,74,111,131,148,166,183,213`。
不由浮点采样选择一个不完整集合：检查器逐一计算全部 241 个旧 YA 精确值，
并断言低于新目标的集合恰好等于这十个标签。

| 原标签 | 新下界（仅显示小数；认证使用分数） | 新正切线行 |
|---:|---:|---:|
| 17 | .008050443344744 | 2 |
| 53 | .008053976063179329 | 0 |
| 64 | .008082618514583350 | 0 |
| 74 | .008051018758412208 | 0 |
| 111 | .008055532610483460 | 0 |
| 131 | .008051154462687029 | 13 |
| 148 | .008051337536018454 | 18 |
| 166 | .008054974348931500 | 0 |
| 183 | .008050378201081435 | 0 |
| 213 | .008051373880787128 | 2 |

本轮把旧 atom 的混合付款拆回每条原已合法直线，再用非负乘子整体付款；
没有新的 tangent 的七个补丁也会因此得到不同于原固定 YA 的更强下界。
共 35 条新正切线行、287 个正对偶支持项，涉及原 PTL 的 32 个不同点。
28 点已有旧 1089 点目录；4 个新用点为 `98272,230769,231200,265088`，
也不在已发布 541 点目录中，但四者都在原 2196 点表内，已逐点匹配原源 SHA。
没有生成新的核值包或假设新的凸段。

若新查询区间 `[L,U]`、点 `p` 及其包 `(v,d_-,d_+)` 同时位于原 REG，
令 `l=min(L,p),u=max(U,p)`。使用的两个下界恰是

\[
w(x)\ge v-d_+p+(d_+-d_-)l+d_-x,
\quad
w(x)\ge v-d_-p+(d_--d_+)u+d_+x.
\]

它们从原凸性真切线 `w(x)≥w(p)+w'(p)(x-p)` 推出：
`x-l≥0,l-p≤0,x-u≤0,u-p≥0` 给出各项的正确导数端点。
点可位于查询区间外，但扩大的 `[l,u]` 必须仍在同一原 REG 中。
包的导数端点、正性及 `plus+minus≤4e9` 都逐项核验。
原已启用 atom 直线继续来自固定原证书，不把 hash 本身当作连续核值证明。

设 `x=(g_0,…,g_6,z_{ij})`。完整盒有 7 个 gap 和 26 个实际平方，
所有平方保留 `0≤z≤1`。原 gap/span 条件和原直线，再加新合法直线，写为 `Ax≤b`。
`F8=q·x/10^8`，对任意精确非负有理 λ，令 `r=q+Aᵀλ`，则

\[
F_8\ge\frac{-\lambda^Tb+
\sum_k r_k(L_k\ \text{if}\ r_k\ge0;\ U_k\ \text{otherwise})}{10^8}.
\]

检查器保留全部 33 个残差及每个盒端点；正支持压缩只删零乘子行。
浮点 LP 仅提出乘子，发布数据消费的是每条严格正的精确 Fraction。

反射并不是假设相同标签：`BS` 正反相同，`a_(i,j)=a_(7-j,7-i)`，
因此 `F8(g)=F8(reverse(g))`。每个反射低胞都由对应原胞付款。

最低保留 YA 现为原标签 71：

\[
L_{min}=131894659288349907661/16384000000000000000000
\approx .00805021113820495>805021/10^8.
\]

未捕获分支仍由原强分类付 `F8≥805803/10^8`，高于新全域 F8 下界。
这完成全域单帧加强，而不是只检查低点或低点中的部分盒。

## 3. 九点统一奖励与既有数据重新付款

保持完全相同的

\[
F_9(g)=\tfrac12(F_8(g_0,…,g_6)+F_8(g_1,…,g_7))+2w(\sum_{i=0}^7g_i).
\]

只要至少一个帧未落入低捕获，原强分类和新的全域 F8 下界立即给

\[
F_9\ge (805803+805021)/(2\cdot10^8)
=805412/10^8>8054119/10^9.
\]

两个帧都低时，本轮不重新求 LP。仅消费既有乘子与真实整数盒、原切线、闭分支，
对全部旧 2352 域及 47 替换域／84 闭分支在新阈值逐一精确重算，全部通过。
同时重新运行公开独立 literal 审查器，以实际 Lean 旧 packet 和新 path 数据重建
1224 代表、2399 反射路由、1144 basic 与 55 path 付款。没有运行 Lean 编译器。

必须区分下列量，不能称它们相等：

- 公开有序域的完整最小值
  `M=263917374155379049835090394947/32768000000000000000000000000000`；
- 实际 canonical 内核路由最小值
  `C=32989671769422422651997857781/4096000000000000000000000000000`。

`M<C`，两者约为 `.0080541190843316`，差仅约 `10^-17`。
旧2352的最小值为 M，47补丁/84分支的最小值约 `.008056081553599694`。
全部 actual basic、path 与 branch 下界都严格大于新 `8054119/10^9`。
本轮新增外域安全预算 `.00805412` 也大于 M，故这些固定数学数据能付的
精确统一奖励为 M。相应更强分数另保留：

\[
21893117050880000000000000000000/
32504082625844620950164909605053
\approx67.35497599760703\%.
\]

简洁发布值采用 `8054119/10^9`，不会把上式精确余量舍入后误称精确最大值。
相对新目标，外域严格余量 `10^-9`，公开低–低严格余量
`2763379049835090394947/32768000000000000000000000000000`。

压力 `404350/10^8`、AM 质量/能量输入、跨度总权≤2、近对支付、全线外零点和重数、
平滑误差 `32dε`、九点端项 `8c` 以及取极限顺序完全按503原运输。
端项只把 c 换成较强常数，仍是有界端费用。
不增加无零区域输入，也不反向由网站不同临界线计数声称简单性认证。

## 4. 冻结文件、重放与公开转换

推荐 root 原样复制下列两份到公开路径；它们采用 canonical LF，
`ROOT` 自查已有 output，默认 `--check` 不写任何 tracked 输出：

| Scratch 文件 | 公开目标 | SHA256 |
|---|---|---|
| `am_low_frame_strengthening_certificate.py` | `scripts/am_low_frame_strengthening_certificate.py` | `f5370cf5e01b2a9b76d327aa83b4e416facb26997f3390bb71fe646f74d62b1a` |
| `am-low-frame-strengthening-certificate.json` | `output/am-low-frame-strengthening-certificate.json` | `aa1a8b4f8e8db6cd446604f11e183e9ae1723f0124ef610e8cae376d5eec8152` |

公开 checker 的默认 check 逐项重放十个新补丁与全部231旧YA，**并完整重算全部2399旧域**，
47/84分支覆盖、541点目录及所有旧2352乘子均实际付款至 `8054119/10^9`。
其输出明确 `inherited_2399_certificate_replayed_this_run=true`。
`--replay-inherited` 是默认完整重放模式的显式别名，不启动 LP 或 Lean。
历史gate摘要只被与当次重新算出的每一个精确最小值比较，不代替重放。
原始 `recheck_inherited_c411.py` 和 `inherited-c411-exact-gate.json` 继续保留约5.08秒的
本轮第一次重放证据；文件名保留c411，但最终checker实际使用更强目标。

clean main checkout 的数学证书不需要独立形式化仓库。
默认check中canonical摘要只是有明确scope的信息，**不用它付款**；
若加 `--formal-root E:/codex-build/RH-Zero-Proportion-Formalization`，
则全部13个 `all_source_hashes` 与当前原始字节逐一匹配，独立literal审查器自身hash也匹配，
再实际重算其全部canonical路由，输出 `canonical_literals_replayed_this_run=true` 和
`all_canonical_current_source_hashes_matched=true`。这个可选模式同样不运行Lean。

```powershell
python tmp/research-resume-20261011/proportion/am_low_frame_strengthening_certificate.py --check --certificate tmp/research-resume-20261011/proportion/am-low-frame-strengthening-certificate.json
python tmp/research-resume-20261011/proportion/am_low_frame_strengthening_certificate.py --check --certificate tmp/research-resume-20261011/proportion/am-low-frame-strengthening-certificate.json --source tmp/pc8-am-admission/Solution.lean
python tmp/research-resume-20261011/proportion/am_low_frame_strengthening_certificate.py --check --certificate tmp/research-resume-20261011/proportion/am-low-frame-strengthening-certificate.json --source tmp/pc8-am-admission/Solution.lean --formal-root E:/codex-build/RH-Zero-Proportion-Formalization
python tmp/research-resume-20261011/proportion/recheck_inherited_c411.py
```

前两个及附加canonical模式都仅标准库，完整public重放约5秒；
`--source --formal-root` 的完整源绑定与actual canonical模式实际 `5.453` 秒 PASS。
原源逐字节 SHA `012c6ac5f9282158a686500dc0c967bf0a9b00e1a6192734d8f237bb23dd2d5f`。
所有32点的 `(p,pack,PTL-list)` 和 REG 均与此完整原源逐项匹配。
优化模式 `python -O` 实际退出1，被已有 exact dependency 拒绝，不能悄然关闭断言。

独立初稿 `low-frame-strengthening-certificate.json`（c411）仍原样保留；
更强研究版 `low-frame-complete-point-certificate.json` 同样冻结。
公开payload去掉研究阶段父文件依赖、增加默认完整旧乘子重放和可选canonical源绑定，
不改变任一乘子、行或点包。
目前没有新 Lean/NaNoDa 检验；四点补目录、单帧 33 变量语义、新目标 closed gates
以及最终 constant bridge 是后续形式化所需真实工作。

停止新搜索。下一个数学瓶颈已经从外域转为现有低–低最小域；
继续提升全域单帧阈值本身不会越过 M，除非再次改变这些低–低付款或窗口输入。
