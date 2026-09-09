# 工程与最终接口的只读复核

2026-09-09，Gibbs 子代理；非外部同行评审。以下是修订前意见。

采纳：增加 admissions.json 精确文件／声明清单与一次出现检查；完整名由 Lean 公理输出名单进一步检查。bootstrap 改为要求已初始化的固定 Git checkout；不导出源码，按 Cache.IO.mkBuildPaths 包含 C 产物和可选 extra，直接复制，trace 最后写入；缺失完整产物时不写 trace。

**数学边界确认通过；工程侧有两项实质问题。** 未运行构建或缓存，不确认Lake已通过。

1. **审计未强制限定这十个经典`sorry`。**
   [audit.py:43](F:/codex-build/RH/RH-Weil/formal/scripts/audit.py:43)会把任何新增`sorry`自动标为`classical_sorry`；[verify.py:43](F:/codex-build/RH/RH-Weil/formal/scripts/verify.py:43)只检查固定声明名单。因此新增未列入名单的`sorry`定理，仍可能得到`passed_with_explicit_admissions`。

   **修正：**对白名单中的完整声明名、文件及出现次数作精确比对，拒绝额外或缺失项；继续保留现有传递axiom检查。无需补完经典证明。

2. **可选bootstrap不能按当前说明视为独立fresh初始化，而且可能留下不完整缓存标记。**
   [bootstrap_from_cache.py:46](F:/codex-build/RH/RH-Weil/formal/scripts/bootstrap_from_cache.py:46)只导出源码，不创建mathlib Git仓库；直接用于fresh目录后，`get_cache.py`的HEAD检查不能通过。另在第99–107行，它复制`.trace`却未复制官方缓存要求的全部配套产物，并仅按大小判断是否覆盖。官方`get`可能因trace匹配而跳过缺失产物；README中的`--repair`可以补救，但不是bootstrap本身完整。

   **修正：**明确要求bootstrap在`lake update`之后使用并校验目标仓库；未复制完整产物时不复制trace；文件覆盖使用字节哈希或直接覆盖，不只比较大小。

其余所查边界一致：

- 八个vendor路径与manifest对应；已跟踪的`vendor/.gitattributes`保留原始字节，避免fresh clone换行转换破坏SHA校验。
- 正常缓存入口保留Lake源码路径、使用上游manifest的方案与官方缓存源码逻辑相符；此次仅作静态核对。
- Sheaf修改只调整态射包装，仍是真实余极限stalk的**集合等价**。
- degree/codegree交换正确；`SectionExistence`已使用正自交，条件证明显式调用`trace_identification`。
- README／蓝图没有宣称RH证明、实际平方实例或Lake验收完成。

## 修订后复核

Gibbs 再次只读核对后确认：“两项已闭合，所查范围未发现遗留实质问题。”
其确认范围是 admission 白名单／出现次数／直接 sorryAx 禁止，以及 bootstrap 的版本前提、
源码比较、完整产物复制和 trace 最后安装。`--check-only` 仅验证版本前提，
不认证缓存完整性或 Lake 通过。本次复核没有运行构建或缓存工具。
