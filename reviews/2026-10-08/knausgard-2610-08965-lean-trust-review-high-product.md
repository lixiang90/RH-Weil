# arXiv:2610.08965v1：67.35% Lean 信任链独立源码审查

2026-10-08，审查者 high_product_joint。只新增本文件，未改附件、上游、Git或旧源。
结论：附件披露的链条一致；它有一个明确的原生计算公理，不能称为纯内核重放。
该公理断言固定有限 checker 返回 true，不直接假设 RH 或 67.35%。
本轮未安装依赖、编译全工程、重算核表或执行约5.35亿节点的完整搜索。

## 1. 固定证据及读取范围

固定 [arXiv v1](https://arxiv.org/abs/2610.08965v1)，
[原始源档案](https://arxiv.org/src/2610.08965v1) 的本地 source.tar 为4746279 bytes，
SHA256 60fb628fb12bdc1ca28d6e849ce9180e9fbcc8b482021bb62d2c92b7827ac3cb。
从 tar 内直接逐条核验 anc/CHECKSUMS.sha256：**354/354匹配，零缺失、零不符**。
本地选择性解压只含其中329项，其余25项未提取，不能据此说附件缺失。
README列出的六个 .clang-format/.clang-tidy 不在原档案中；未作GitHub副本全量对照。

全文读取 anc/README.md、lean/README.md、axioms.txt、upstream_relax.patch，
Solution673、Challenge673、scripts/Compare673、PrintAxioms673、make_compare.py，
Simple673/Main、Local/RunAll、FinalAll、Checker、Search、Soundness，
Kernel/Array、Table、Compute、Sound及 SpotChecks；并读取参考运行JSON和计数驱动。
以下 SHA 按 UTF-8 canonical LF，无 trim；此次所列原文件已经是 LF：

| anc/lean 下关键文件 | 行数 | SHA256 |
|---|---:|---|
| README.md | 296 | 6a7e20802b5e4706b35f70ab950cb73217d91792a0a0b605872df465c879918d |
| axioms.txt | 210 | 73544ee6b53ac69df3eb874eed55370b02854d4afe1646e1164785d9a63ccee7 |
| Simple673/Local/RunAll.lean | 23 | 7e601474d6730736426c72b89d396a0ccda7b3810e7a097c102437e67b9edd76 |
| Simple673/Local/Checker.lean | 567 | b01a26d0b2263757d22c473c51091d9d2a2781e95ce5067531d5453231a20cf6 |
| Simple673/Local/Search.lean | 303 | ad8e64d4d765861016bf4408958610cfe32385090cad910a649e346ac8eff65c |
| Simple673/Local/Soundness.lean | 76 | 12a74dc0a8119eef86f74534ec99af871ffa0d85bf0f6020c9f20336cf1bfc5f |
| Simple673/Kernel/Array.lean | 35 | 781227c0df8f8ae0c66aeaadb9803eea341f02d6f34f7f195f9922baf09896fc |
| Simple673/Kernel/Table.lean | 42 | d6e3fb646001cbe52fafa6c69a7d9039d63e5bb9bfcbead9743ede1a9292ebba |
| Simple673/Local/FinalAll.lean | 28 | 6744a0798d47ffa13acb45f5a42744cae290356f4a7d92814a234a4fd6e885c9 |
| Simple673/Main.lean | 46 | 9bf2476d0008ee89ff1bcf82611d83e64cc5a7627298524248b86949aaae1ff4 |
| Solution673.lean | 20 | 7ad04b241093fc010ea977fd106cf170a974c79fd55f2821040c02c35e48e615 |
| upstream_relax.patch | 560 | 495a0978f44c528e520bd46fded1fe6b88bbb415789a44e03f714767539e6cb0 |

## 2. 公理到底断言什么

Local/RunAll.lean:21 的唯一执行断言为
\[
 \texttt{checkAllPar kTabArray 32 96 = true := by native\_decide}.
\]
自带 axioms.txt 的 PrintAxioms673 段明确列出：
propext、Classical.choice、Quot.sound，
以及 Simple673.Local.check_passes._native.native_decide.ax_1_1。
前三项是该工程采用的普通 Lean/classical 基础；最后一项增加计算信任。
这里“公理”是生成的固定 Boolean 求值事实，仍须信任 Lean编译器、解释器和运行时。
它没有断言零点全在临界线，也没有直接断言某个零点比例。

Soundness.lean:67 由表下界和该 Boolean 推局部不等式；
Search.lean:286 的 frontier/part 覆盖证明处理任意正 parts，
copyTab保持表项，Task的逻辑值取其函数值，未把调度正确性另作数学假设。
Checker只用 Nat、表示有符号差的 Nat pair、有限 fuel；
fuel耗尽与失败节点返回 false，递归接受必须两个半盒均接受。
Array/Table/Sound把准确有理数包络和 cell 下界送到 checker；
FinalAll.lean:24 三者组合，再由 Main.lean:35–44 传到真实计数定理。
自带报告中 of_local、表和 checker 健全性仅列前三基础公理；
该报告是作者生成的文件，本轮未重新执行 #print axioms。

## 3. 隐藏假设与终点语义

检索全部242个附件 .lean：未见显式新增 axiom、unsafe、implemented_by；
实际 sorry 仅在五个 Challenge 开放声明文件。
实际 native_decide 仅在三个 Local/RunAll；673附件导入闭包93个本地模块
只含 Simple673.Local.RunAll，没有导入 Challenge673 的 sorry。
RunCheck中的 partial 计数函数是诊断，不在 Solution673 的证明链中。
对 Simple673 补查动态声明/extern入口，未见额外注入机制。
此扫描不等于审计未附带的整个上游和Mathlib。

Challenge673 的对象明确是 Mathlib riemannZeta 的非平凡零点，
按 analyticOrderAt 定义重数，N0simple要求实部1/2且重数1。
最终常数1669159/2478195约为0.67353820018，结论为全部充分大T的渐近计数下界。
Compare673 在内存按 make_compare.py 精确重建，与附件逐字匹配：
开放 sorry 被同名 Solution theorem 替换，并未被证明链消费。
但该 comparison 的重新 typecheck 本轮未执行。

## 4. 表规模、搜索日志与复现边界

certificate_line/kernel_lower.bin 实核1048576 bytes，即262144个little-endian uint32；
SHA e32c430de69dd92adbfbdb9935a9983eb7e033113c2c87c2a763f549e4401e0a
与 inputs.json、kernel_build.json及manifest匹配。
Lean Array.ofFn 的长度也是 tabR+1=262144，表健全性是对全部cells的形式证明源码，
不是只核若干采样点。它不从这个bin读取证明数据，而是按准确有理公式重算。
“Lean重算表与bin逐项相同”尚是README的作者记录，本轮没有独立重算。
535332163 visited /267666082 accepted是 cpp_verification.json及README所报；
check_passes命题只认证 Boolean，不包含这两个计数；本轮未重跑或认证计数。
四个 decide +kernel spot 定理不进入最终证明，也不能替代全搜索。

固定依赖为Lean v4.33.0-rc2、上游 fbdc36bbf17d20af3fd0447c6d1a8a02773c9844，
Mathlib 51e6992efd06126df61a496bebf8f49482a4e129。
14文件patch只放宽窗口前件常数并调整证明；全文未见添公理、sorry或改真实零点定义。
本机缺固定版本，上游完整构建未复现：不能把作者构建记录说成本次内核检查成功。
本审查支持“披露了准确计算信任的形式化证明源码”，并未发现隐藏RH假设；
它不支持“完全无额外公理”或“我们已独立复现67.35%全Lean证明”。
