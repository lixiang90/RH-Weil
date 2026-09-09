# 本轮目标验收范围

本轮用户要求是暂停原 GOAL，建立有组织的 F₁ Lean + mathlib 形式化框架，允许中间
`sorry`，并复制 mathlib 之外引用的开源代码。不是要求本轮证明 RH。

| 要求 | 权威证据 | 当前判定 |
|---|---|---|
| 暂停原持续研究 | 仓库 README、RESEARCH_BRANCHES、goals/PROGRESS 顶部说明 | 已记录；原较远期数学目标未宣告完成 |
| 放在 formal 并组织成蓝图 | `F1.lean`，Arithmetic／Analysis／Geometry 模块，blueprint/README.md | 源码与依赖图已建立；实际算术比较仍明确开放 |
| 使用真实 Lean + mathlib 对象 | 实际 `PrimeSpectrum ℤ` 预层／stalk、`Real.circleAverage`、固定算术 Weil 型、`RiemannHypothesis` | 完整构建 3459 个任务通过；目标定义及公理输出已检查 |
| 允许但明确列出 sorry | `source-audit.json`、独立复核、`F1/Audit.lean` | 十个经典待形式化命题精确登记；20 个声明传递公理检查通过 |
| 外部项目保存实际代码 | `vendor/manifest.json`、八个项目源码及许可证 | 806 个文件已复制；SHA256 与 Git 跟踪校验通过 |
| 可重现地检查整个框架 | 固定 toolchain、Lake 清单、get_cache.py、verify.py | 实际命令、完整构建及公理检查通过，见 verification.json 和相邻日志 |
| 保存并推送研究记录 | Git 提交与远端 main 的 SHA 比较 | 两个检查点 7a186f3、d1aec18 已推送；最终验收提交的发布由会话中的远端 SHA 核验认证，避免文件自引用提交号 |

`verify.py` 成功仅认证带显式 admissions 的蓝图。非零有效代表、双次数下降及有效刚性
在实际算术平方上的构造仍是开放研究输入；不能借本轮框架验收将它们视为已证。
