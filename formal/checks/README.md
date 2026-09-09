# 验证记录

当前为构建中检查点，尚未完成全项目 `lake build` 与 `F1/Audit.lean` 公理输出。
不得把此检查点描述为完整构建已通过。

已检查：Lean 4.32.2；Lake 生成的根 manifest 使用固定 mathlib 提交与八个本地路径依赖；
806 个 vendored 文件逐字节 SHA256 校验通过；当前源码有十个明确的经典 `sorry`。
PrimeLocalization、FiniteSupport、RationalCorrespondence、ReducedSquare、Jensen、Weil、
Existence 已分别用该版本 Lean 和匹配官方缓存编译通过，保留声明中所列 `sorry`。
Sheaf 模块的整体构建仍待补齐缓存后检查；单独编译不能代替全项目验收。

[independent-review.md](independent-review.md) 保存只读数学复核和采纳记录。
[source-audit.json](source-audit.json) 是源码哈希及 admission 清单，不是内核证明证书。
后续须保存最终 `lake build` 日志和传递公理输出，再更新此状态。
