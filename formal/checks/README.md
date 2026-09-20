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
