# 本轮目标验收范围

本轮用户要求是暂停原 GOAL，建立有组织的 F₁ Lean + mathlib 形式化框架，允许中间
`sorry`，并复制 mathlib 之外引用的开源代码。不是要求本轮证明 RH。

| 要求 | 权威证据 | 当前判定 |
|---|---|---|
| 暂停原持续研究 | 仓库 README、RESEARCH_BRANCHES、goals/PROGRESS 顶部说明 | 已记录；原较远期数学目标未宣告完成 |
| 放在 formal 并组织成蓝图 | `F1.lean`，Arithmetic／Analysis／Geometry 模块，blueprint/README.md | 源码与依赖图已建立；实际算术比较仍明确开放 |
| 使用真实 Lean + mathlib 对象 | 实际 `PrimeSpectrum ℤ` 预层／stalk、`Real.circleAverage`、固定算术 Weil 型、`RiemannHypothesis` | 类型与证明的完整验收须看最终构建输出 |
| 允许但明确列出 sorry | `source-audit.json`、独立复核、`F1/Audit.lean` | 十个经典待形式化命题；传递公理审计待运行 |
| 外部项目保存实际代码 | `vendor/manifest.json`、八个项目源码及许可证 | 806 个文件已复制；最终需 `audit.py --tracked` 核验 Git 跟踪 |
| 可重现地检查整个框架 | 固定 toolchain、Lake 清单、get_cache.py、verify.py | 缓存恢复中，尚未完成完整构建与公理输出 |
| 保存并推送研究记录 | Git 提交与远端 main | 蓝图检查点 7a186f3 已推送；最终验收记录待提交推送 |

`verify.py` 成功仅认证带显式 admissions 的蓝图。非零有效代表、双次数下降及有效刚性
在实际算术平方上的构造仍是开放研究输入；不能借本轮框架验收将它们视为已证。
