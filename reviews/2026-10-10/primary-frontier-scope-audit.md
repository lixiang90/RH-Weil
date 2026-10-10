# 2026-10-10 研究恢复的 primary 来源与证据边界

独立审查；只读外部来源和本地稿件，没有执行外部 Lean 工程，没有更改公共仓库。

## 本轮开始时的两条基线

项目比例 `66812491/99194740` 指 `liminf N₀ˢ(T)/N(T)`：分子只数简单临界线零点，
分母数所有非平凡零点及重数。它可推出相同值的不同临界线比例；反向推论不成立。
网站只锁定不同临界线计数，不能把排行榜目标的措辞自动读成简单性认证。

本项目无零边界 `σ*=0.874957019420098946…` 的稿件定理显式以完整 imported
package `ℛ` 为前件，其中包括固定 `Q(√−3)` 的全有限阶 Hecke `7/8` bootstrap。
不能只用普通 zeta 的 `7/8` 结论替代全族前件：Poisson 行引入 Hecke twists。
纯 norm twists 只移虚部。主函数允许 `s=1` 极点，严格边界线不含。
数学稿件的 cited-input 推导、核心代数 Lean 核验、完整算术实例化仍是不同状态。

## 重新核准的公开版本

版本查询证据为同目录 `live-repository-heads.json`。

| 来源 | 固定版本及本轮核准的输入 |
|---|---|
| [riemannzeta.fun 当前记录](https://www.riemannzeta.fun/submissions/master-of-puppets) | `66812491/99194876`，2026-10-09 17:13 UTC；[公开提交](https://github.com/josusanmartin/riemann/tree/d95a6d7d11d7836306ec7ec1eb5be3478663718e/submissions/master-of-puppets)。网站专家审查尚未登记。项目值分母更小，但本站尚未验收项目提交。 |
| [Knausgård](https://arxiv.org/abs/2610.08965v1) | primary 仍仅 v1，2026-10-06。`1669159/2478195` 为同口径 simple-critical；其最终 theorem 另信任 `native_decide` 搜索断言。不能仅称标准三公理、也不能因额外计算公理反证数学命题。 |
| [OpenAI math](https://github.com/openai/math/commit/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb) | live HEAD `fd4aeeb2…`，2026-10-08；项目算术来源仍固定最初 `adc7f1241b42e322a6451854ab7e4b4c146bf78a` 的 September-30 稿。该稿当前可读文本与项目 pinned source 的差异应按 hash 核准，不自动切换输入。 |
| [Baiying Liu 新稿](https://arxiv.org/html/2610.12234v1) | primary 仅 v1，2026-10-08 16:18:53 UTC；`34999/40000` 和项目自由 b 同值 `(1507−2√921)/1653`。不是比项目三次边界更优的新数值。 |
| [Argonaut Math](https://github.com/Argonaut-Math/argonaut-math-quasi-riemann-boundary/tree/5971383edcb0b1cf863927eed3b359d2d3ba346e) | fixed HEAD `5971383…`；公告边界 `3499999/4000000=0.87499975`，较项目旧边界弱；本輪未重放其 Lean/Comparator。 |

没有将搜索结果聚合站写的 Liu “10-09 update” 当作版本：arXiv 原始页只列 v1。
没有找到可核准的更强公开比例或更小无零常数；这不是穷尽全球并行结果的证明。

本地当前 September-30 `build/paper.tex` 实读 782993 个 CRLF 字节，转换成 canonical
LF 后为 766316 字节，SHA256 `42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`，
与项目固定原稿一致。项目减去当前网站值的精确差为
`1135812347/1229951241769030`，即约 `0.0000923461279137` 个百分点。

OpenAI [正式 scope note](https://raw.githubusercontent.com/openai/math/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/003.md)
明确全 Dirichlet 与有限阶 Hecke 范围。只读本地对应 `Hecke/Nonvanishing.lean` 确见
`HeckeFamily.LFunction_ne_zero_of_seven_eighths_lt_re` 与 ray-family 入口；本轮没有
独立编译完整上游。`ComparatorChallenges.QuasiRiemannHypothesis.json` 只对应 zeta
目标，不能据它一份配置独立认证全部 Hecke 量词；Hecke 有自己的 challenge。

## 新外部输入可以怎样使用

Liu §25 的三约束正权消元证明可独立核对固定 `κ≥3/4` 窗的代数障碍。它只由
显式约束推出自由 b 边界；全文更广参数系统最优性仍标 expectation。它并没有排除
重新证明更低 κ 后的反馈改善。引言提及该可能但没有开展；项目当前三次稿已经
付出了实际 κ 反馈，后续必须保留其 entire plain range、prime masks 和 shared mesh。

其 [固定代码仓库](https://github.com/liubaiying101/Slightly-improved-zero-free-half-planes-for-the-quasi-Riemann-hypothesis/tree/7d10420de90efa2f082a06a342fc7accbd57ab37)
展示不带 probe/moment 前件的 `V2FullVerification` 入口，以及由旧全 Hecke
bootstrap 构造四字段 moments 的代码。它适合逐引理对照实际构造，不能直接把
固定 κ 实例当成我方移动 κ、cubic 参数下的已证实例。

## Liu 公布形式化包的实际可复现限制

本轮 API tree 未截断，共 235 项，证据 `liu-pinned-tree.json`。
下载 24 份 selected text，235674 字节，原字节 SHA 列在
`liu-fixed-text-manifest.json`；未执行其代码。

观察到的交付路径缺口：

- `verify.py` 要 `RHZeroFreeExtension/CombinedPaperVerification.lean`，实际文件在仓库根。
- `lakefile.lean` 的 OAI `srcDir="vendor"`，公开 tree 没有 `vendor` 副本及 `vendor/LICENSE`。
- V2 文件 import `RHZeroFreeExtension.analytic_high.V2…`；实际公开目录是
  `analytic_high_v2/`，缺所需命名空间目录。
- `upstream/closure_manifest.json` 有上游 commit/blob/SHA 清单，但清单不提供被列举的
  完整上游源文件；运行 verifier 的最早 source-integrity 读取因此也没有输入。

所以本轮不能复现论文所述完整 build/replay。公开所读 entry 没有额外算术前件，
也未发现这 24 份中显式 `axiom`、`sorry` 或 `native_decide`，但这仅是所读文件的
源码事实，不是完整 closure 传递公理认证。缺包/路径错误不反证数学论文，修复包
之前也不构成可用的完整 Lean 验收证据。

## 新候选验收关口

比例 storage 的独立数学审查见同目录
`finite-state-storage-mathematical-review.md`：finite bounded potential 只付一次端项，
其不连续性不增加 smoothing 费用，仍须 exact graph、full cover 及每弧 slack。

无零候选的障碍证明须核 `Rκ` 正分母/κ 单调性、移动 critical δ 所在真实域、
完整 low 几何以及原始高频全部误差。上界接口不能付款表示此方法证书不足，
不能制造实际坏行、真实零点或所有算术方法的最优性。
