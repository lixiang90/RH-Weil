# 固定证书的本地定义桥

本目录的两份 AMPC8 辅助源码由
[持久复演器](../../scripts/am_pc8_finite_replay.py)追加到固定公开源的纯数值抽取后，
使用 Lean 4.34.1 和 `import Std` 核验。它们依赖生成的 `NumericCore.lean` 中的
定义，不能作为独立文件直接编译，也未加入现有 Lean 4.32.2 / mathlib 工程。

- [AMPC8StructuralBridge.lean](AMPC8StructuralBridge.lean)：28种分割及根初始收紧
  与通用闭包的29条全参数定义等式。
- [AMPC8MinorantBridge.lean](AMPC8MinorantBridge.lean)：实际展开叶节点判据通向
  通用整数检查器的全参数蕴含。

30条主桥是 Lean 内核证明，传递公理只有标准 `propext`。
同一复演器另检查5个执行适配器等价守卫；240项精确整数 `#eval` 和7项Python
有限结构检查具有各自的求值信任边界，不能称为额外247个内核证明。
实数区间语义、非紧覆盖及实际零点计数仍需独立数学证明。

完整适用范围、固定源身份、工具链与重放命令见
[笔记483](../../notes/483-admission-of-known-am-eight-point-proportion.md)和
[最终抽取审查](../../reviews/2026-10-08/hybrid-original-am-eight-point-numerical-extraction-review-pc8.md)。
