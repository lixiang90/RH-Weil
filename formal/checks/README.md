# 验证记录

2026-09-09：完整框架验收通过，状态为 `passed_with_explicit_admissions`。

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
