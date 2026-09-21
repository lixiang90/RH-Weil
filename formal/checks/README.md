# 验证记录

## 2026-09-20 TraceRadical定向检查

[实际报告](trace-radical-verification.json)、[编译输出](trace-radical-build.txt)、
[公理输出](trace-radical-axioms.txt)及[审计入口](TraceRadicalAudit.lean)记录八条新引理：
全部编译通过，没有sorryAx依赖。解析事实作为前提，不由这些代数证明认证。
当前[源码清单](trace-radical-source-audit.json)另存，原十处admission保留。

## 2026-09-20 LocalTrace定向检查

[定向报告](local-trace-verification.json)、[编译输出](local-trace-build.txt)与
[公理输出](local-trace-axioms.txt)是本轮记录；不覆盖下方原完整构建报告。
[LocalTraceAudit.lean](LocalTraceAudit.lean)列出八条新结果的传递公理检查；实际全部通过，
仅依赖Lean标准公理propext、Classical.choice、Quot.sound，无sorryAx。
[源码清单](local-trace-source-audit.json)另存；vendor八包806文件与原版本一致。
数学对应见[404](../../notes/404-f1-adelic-periodic-orbits-and-mixed-local-trace.md)，完整解析／几何迹仍未形式化。


## 2026-09-10 几何实现条件包

新增源相对 `GeometricRealization.lean`、G0–G8 规范和六个条件推论。
最新运行记录为本目录的 `verification.json`、`lake-build.txt`、`axioms.txt`、
`source-audit.json`；本轮已通过 3472 个构建任务、26 个声明（14 个无 `sorryAx`，
12 个保留原有传递 admission 依赖）、十个经典 `sorry` 和 11 个本项目 Lean 文件。
机器报告状态为 `passed_with_explicit_admissions`。八个外部依赖及 806 个源码文件保持原版本。
发布前 Git 字节检查也同步到 11 个 Lean 文件。

新增推论均为带前提的证明：正自交代表非零需要主除子根空间；从可容许截面到
Weil 非正性仍需要未实现的几何 RR、有效刚性与算术识别。
参考算术对象、线丛／正则性、对应积分和相对迹的缺失比较在规范末表明确列出。
独立只读复核见 [geometric-realization-review.md](geometric-realization-review.md)。

## 2026-09-09 初版历史

2026-09-09：完整框架验收通过，状态为 `passed_with_explicit_admissions`。

下列数字记述初版；同名机器日志已由上面的最新运行更新。

- [完整构建](lake-build.txt)：`lake build` 成功，3459 个构建任务。
- [公理输出](axioms.txt)：20 个声明完成传递依赖核查；其中 8 个无 `sorryAx`，
  其余 12 个对应十个经典 admission 及两个间接依赖结论。
- [机器验收结果](verification.json)：固定 Lean 4.32.2、构建、公理与源码审计均返回零。
- [源码清单](source-audit.json)：十个 `sorry` 与蓝图登记精确一致；八个项目的 806 个
  vendored 文件逐字节 SHA256 校验及 Git 跟踪核查通过。
- [缓存工具构建](cache-tool-build.txt)、[官方缓存恢复](cache-restore.txt)：复现步骤已实际运行。
- [发布源码核验](release-source-check.json)：Git 暂存区中的 806 个外部源码文件及
  10 个本项目 Lean 文件，与来源清单和本轮已编译源码快照逐字节一致。

新增的互素参数有理图点集双射没有 `sorry`。`nonpositive_of_existence` 也不依赖
`sorryAx`，但仍有显式几何研究假设；`rh_of_existence` 则依赖经典 Weil 判据 admission。
构建成功不证明这些 admission 或实际算术平方上的几何输入。

[independent-review.md](independent-review.md) 保存只读数学复核和采纳记录。
[source-audit.json](source-audit.json) 是源码哈希及 admission 清单，不是内核证明证书。
工程问题及修订见 [engineering-review.md](engineering-review.md)；本机缓存环境见
[runtime-environment.md](runtime-environment.md)。首次缓存日志中的源码摘要先于最终有理图补强，
当前源码快照以 `source-audit.json` 为准。

### UnitDescent: scoped check

[unit-descent-verification.json](unit-descent-verification.json), [build output](unit-descent-build.txt),
[axiom audit](unit-descent-axioms.txt), and [source inventory](unit-descent-source-audit.json)
record four checked algebraic descent results. The concrete source exponentials, Fredholm
determinants, complex divisors, and any arithmetic metric are not formalized here.
Use `python scripts/check_unit_descent.py` with the same pinned dependency options as LocalTrace.
Earlier reports describe their original source snapshots and have not been overwritten.


## WeightedArrows：九项定向验证（2026-09-20）

[报告](weighted-arrows-verification.json)、[编译输出](weighted-arrows-build.txt)、
[公理输出](weighted-arrows-axioms.txt)、[审计入口](WeightedArrowsAudit.lean)、
[源码清单](weighted-arrows-source-audit.json)记录九条已通过结果。
没有sorryAx依赖；16份本项目Lean源码中原十处admission未增减。
vendor8包806文件逐字节及Git跟踪核查通过；旧报告保持原样。
脚本为 scripts/check_weighted_arrows.py，固定Lean4.32.2与原mathlib提交。
这次是定向检查，不是全F1重建；分析、范畴及几何部分未被该模块认证。


## OrbitDecay：四项定向验证（2026-09-20）

[报告](orbit-decay-verification.json)、[编译输出](orbit-decay-build.txt)、
[公理输出](orbit-decay-axioms.txt)、[审计入口](OrbitDecayAudit.lean)、
[源码清单](orbit-decay-source-audit.json)记录四项通过结果。
没有sorryAx依赖；17份项目Lean源码仍只有原十处admission，
vendor8包806文件逐字节及Git跟踪核准，旧报告未覆盖。
本模块只验证有限乘积和区间跨度，完整分析／范畴及RH不在认证范围。

## 2026-09-20 BoundaryResolvent定向检查

[报告](boundary-resolvent-verification.json)、[编译输出](boundary-resolvent-build.txt)、
[公理输出](boundary-resolvent-axioms.txt)与[审计入口](BoundaryResolventAudit.lean)
记录四项已通过检查，仅依赖propext、Classical.choice、Quot.sound，无sorryAx。
[源码清单](boundary-resolvent-source-audit.json)含18份项目Lean源码及原十处admission，
vendor仍为8包806文件。算子范数收敛、无限直和、热迹、实际几何与RH不在本次形式化范围。
历史完整构建与先前定向报告均保留。

## 2026-09-21 BoundaryClutch定向检查

[报告](boundary-clutch-verification.json)、[编译输出](boundary-clutch-build.txt)、
[公理输出](boundary-clutch-axioms.txt)及[入口](BoundaryClutchAudit.lean)
记录五项通过的代数检查，无sorryAx。
[源码清单](boundary-clutch-source-audit.json)包含19份项目Lean源码，原十处admission，
vendor八包806文件原样保留。旧报告不覆盖；连续性、绕数和K理论未由这些引理形式化。

## 2026-09-21 EndpointDefect定向检查

[报告](endpoint-defect-verification.json)、[编译输出](endpoint-defect-build.txt)、
[公理输出](endpoint-defect-axioms.txt)、[入口](EndpointDefectAudit.lean)
记录六项通过的代数检查；两项不依赖公理，四项只依赖propext，均无sorryAx。
[源码清单](endpoint-defect-source-audit.json)包含20份项目源码、原十处admission及
vendor八包806文件校验。历史报告保持。Hilbert正交／收敛、C*、迹和K理论未在此形式化。

## 2026-09-21：TransverseTrace

[七项内核检查](transverse-trace-verification.json)、[传递公理](transverse-trace-axioms.txt)、
[编译日志](transverse-trace-build.txt)及[独立源码清单](transverse-trace-source-audit.json)保存。
几何尾部及加性K读出障碍代数无sorryAx；真实Hilbert悬挂和算子迹尚非Lean形式证明。
21份项目源码、十处旧admission、八个vendor项目806份源码核准，所有历史报告保持。

## 2026-09-21：BoundaryGluing

[七项检查](boundary-gluing-verification.json)、[公理日志](boundary-gluing-axioms.txt)、
[编译日志](boundary-gluing-build.txt)及[源码清单](boundary-gluing-source-audit.json)保存。
有限支平移与秩边界代数没有sorryAx依赖；C*／拓扑／K理论尚非这些形式化的内容。
22份项目源码，十处旧admission和八个vendor项目806份源码已核准，历史报告保持。

## 2026-09-21：BoundaryUnitary

[六项检查](boundary-unitary-verification.json)、[公理日志](boundary-unitary-axioms.txt)、
[编译日志](boundary-unitary-build.txt)及[源码清单](boundary-unitary-source-audit.json)保存。
序列移位和有限通量恒等式无sorryAx依赖；不认证Fredholm或C*理论。
23份项目源码、十处旧admission、八包806份vendor源码已核准，旧审计文件原字节恢复。

## 2026-09-21：DefectProjection

[18项检查](defect-projection-verification.json)、[公理日志](defect-projection-axioms.txt)、
[编译日志](defect-projection-build.txt)、[入口](DefectProjectionAudit.lean)及[源码清单](defect-projection-source-audit.json)保存。
真实二阶矩阵的酉性／投影与缺陷代数无sorryAx依赖；解析前提、理想归属及迹不在形式化范围。
24份项目源码、十处旧admission及八包806份vendor源码核对，历史报告保持。

## 2026-09-21：ProjectionConnection

[六项内核报告](projection-connection-verification.json)、[公理日志](projection-connection-axioms.txt)、
[编译日志](projection-connection-build.txt)、[入口](ProjectionConnectionAudit.lean)及[源码清单](projection-connection-source-audit.json)保存。
投影连接及压缩缺陷的抽象代数无sorryAx依赖，未认证实际交叉积或无界演化。
25份项目源码，十处旧admission与八包806份vendor校验保持；所有历史报告保留。

## 417：cocycle 与连接演化代数（2026-09-21）

[connection-evolution-algebra-verification.json](connection-evolution-algebra-verification.json)：
四项左右 cocycle 群律、压缩残差和相位导数恒等式通过固定 Lean 4.32.2，
仅依赖 propext，无 sorryAx；[源码清点](connection-evolution-algebra-source-audit.json)为26份项目源码及原十处admission。
可由 scripts/check_connection_evolution_algebra.py 按报告中的cache/runtime选项复验。
不将这四项代数核验计为演化分析或全F₁形式化，原检查日志保持原样。

## 419：单边移位与循环迹（2026-09-21）

[shift-trace-obstruction-verification.json](shift-trace-obstruction-verification.json)
记录三项移位缺陷及加性循环泛函限制，固定Lean 4.32.2通过，无sorryAx；
可通过 scripts/check_shift_trace_obstruction.py 按报告路径复验。
[源码清点](shift-trace-obstruction-source-audit.json)为27份项目源码、原十处admission和八包806份vendor。
无限维算子与迹权推导仍须数学审查，未重建全F1，历史报告保持。

## 420：SchurIndexAlgebra（2026-09-21）

[四项内核报告](schur-index-algebra-verification.json)、[公理日志](schur-index-algebra-axioms.txt)、
[编译日志](schur-index-algebra-build.txt)、[入口](SchurIndexAlgebraAudit.lean)及[源码清单](schur-index-algebra-source-audit.json)保存。
固定Lean4.32.2核验任意非交换环的二阶Schur消元和三角逆元，标准依赖propext、Classical.choice、Quot.sound，无sorryAx。
两处战术风格warning保留原输出。28份项目源码、十处旧admission、八包806份vendor不变；历史报告未覆盖。
实际Hardy族及指数、Chern和对偶作用的分析证明不属于这一机器检查范围。

## 421：WeightedTraceDefect（2026-09-21）

[报告](weighted-trace-defect-verification.json)、[公理日志](weighted-trace-defect-axioms.txt)、
[编译日志](weighted-trace-defect-build.txt)、[入口](WeightedTraceDefectAudit.lean)及[源码清单](weighted-trace-defect-source-audit.json)保存。
三条非交换代数恒等式通过Lean4.32.2，仅propext，无sorryAx。
29份项目源码、十处旧admission、八包806份vendor原样保持，历史报告不覆盖。
无分析性迹、BV极限、循环上同调或完整F1形式化声明。

## RadialFinitePart 六项定向与角点账本（2026-09-21）

[验证报告](radial-finite-part-verification.json)、[构建](radial-finite-part-build.txt)、[公理](radial-finite-part-axioms.txt)及[源码清点](radial-finite-part-source-audit.json)保存本轮范围。
六项检查使用Lean4.32.2和固定mathlib，零sorryAx；30份项目源码、十处旧admission与八包806份vendor源码保持。
只证明有限部四分量的代数变换、截止包含排除和源角点系数，完整分析另审；所有历史报告保持原字节，未全构建F1。
