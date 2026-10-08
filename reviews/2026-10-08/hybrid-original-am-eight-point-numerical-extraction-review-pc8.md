# 固定公开八点 AM 证书：数值抽取与纯定义桥复核

日期：2026-10-08。对象：固定公开 PC8CL 证书及本仓库的 `scripts/am_pc8_finite_replay.py`。

**冻结结论：固定 PC8CL 的全量有限证书复演与 30 条主定义桥通过；与前一冻结实区间语义审查合并，可准入原八点 AM 的七维全域核门。** 本文作者独立运行持久提取器 `--check`，实际进程退出 0，240 个唯一有序断言全部为真，七项完整有限结构检查通过，saved output 完整字节相符。下文区分编译求值、Lean 内核证明和实数语义审查，不能互相替代。

## 1. 受审快照与边界

固定源为 [josusanmartin/riemann 的 d272437 提交](https://github.com/josusanmartin/riemann/blob/d272437e7ebeb17b87c8c3d7cece592aa23785ab/submissions/dani-bound-2026/proof/Solution.lean)，提交全名 `d272437e7ebeb17b87c8c3d7cece592aa23785ab`。本地副本为 `tmp/pc8-am-admission/Solution.lean`，1,675,641 字节、19,049 行，原始字节 SHA-256：

`012c6ac5f9282158a686500dc0c967bf0a9b00e1a6192734d8f237bb23dd2d5f`。

本次最终抽取快照如下；这些文件使用 LF，因此原始与规范化 SHA-256 相同。

| 对象 | 字节／行数 | SHA-256 |
| --- | --- | --- |
| `scripts/am_pc8_finite_replay.py` | 13,273／280 | `2db626d7c3fbcc1f6ced7580d0fe847fff743b1039aa58797392e9e05845600f` |
| `tmp/pc8-am-admission/NumericCore.lean` | 990,515／11,608 | `f21a0d9f141a7807a6524f426b64a0c0b7b2e81e12581d3ec528f467e9bd1be3` |
| `tmp/pc8-am-admission/NumericRun.lean` | 1,100,160／11,853 | `170290e9a90bfc23addbcc7803656f1bfad9f1dd475b737d7e417ca9a5085ab2` |
| `formal/certificates/AMPC8StructuralBridge.lean` | 5,906／165 | `98771eceea94a14f3a1be38c1e9c7ab48fffbb0d1c77bbfde636d21358b9ba9f` |
| `formal/certificates/AMPC8MinorantBridge.lean` | 5,512／101 | `f3947ca27750760322481a87ed5da4a5a8702a92bdf4570a6a4727f957fee114` |

完整实区间语义由同目录的 [冻结语义审查](hybrid-original-am-eight-point-full-certificate-audit-pc8.md) 给出。该文保持原样，SHA-256 为 `6cea584276b25cfd58fd353f8281986898833ae0a335c8f9033ba99a8154fb46`。其中“数值复演尚待完成”和“展开表达式的定义等式尚未本地编译”是当时的冻结状态；本文单独记录如何补齐这两个门。

本次未执行上游脚本、上游 Lean/lake 工程，也未重新编译上游涉及 Mathlib 的全部实数分析证明。执行的是本仓库已经完整审读的提取器和本地自写的 `import Std` 证明桥。本文只负责八点 AM 的有限证书门及其与已审实区间语义的衔接，不单独证明一条临界线零点比例，也不构成新纪录声明。

## 2. 全量抽取比对

审查完整阅读了持久提取器。它先检查固定源的字节数、行数和原始哈希，再扫描源码 7184–18649 范围内的纯数值 `def`、`abbrev`、`structure`，排除实数分析依赖和命题定义；共保留 2,744 个原声明。它重建原命名空间，保留 `CellA` 的局部变量上下文，并附加自写适配器及证明桥。

独立比对程序直接读取固定源码和生成文件，没有导入或执行上游脚本，也没有借用提取器函数来决定比较结果。它对全部 2,744 条映射逐项比较完整声明体，并独立恢复源码和生成文件的命名空间上下文：

- 完整声明体：2,744 条相等，0 条差异；
- 命名空间及完整声明名：2,744 条相等，无同名重复；
- 192 个 `PTL_j`：全部原始点列表及编号相等；
- 32 个 `WBj`：其完整大整数定义已包含在声明体逐项比对中；
- 32 个 `wccj_j`：原定理左边的完整执行表达式和右边的正整数逐项相等；
- 240 个 runner 标签和执行表达式：数量、唯一性、顺序及内容全部相等；
- `NumericRun.lean` 的字节前缀恰为整个 `NumericCore.lean`，不存在只审一份核心而运行另一份核心的情形。

比较仅允许下列明确改写，以及移除原编译属性、`private`／`noncomputable` 标记、重建命名空间所需的外壳调整。所有常量、表、编码、算术方向、分支参数顺序和检查表达式保持原定义。

| 适配 | 数学依据 | 本地检查 |
| --- | --- | --- |
| `Bool.rec` 改为自写 `boolRec` | 对任意 `motive : Bool → Sort u` 按 `false`／`true` 两构造子展开即等于原 recursor | 泛型 `cases c <;> rfl` |
| `List.rec` 改为自写 `listRec` | 空表相同，非空表使用相同首项、尾表和递归结果；实际保留声明中的列表均属 `Type` | 对任意列表及 motive 的归纳证明 |
| `forceR`、`forceB`、`forceT` 的原 `Nat.rec` 改为 `k a` | 原 successor 分支完全忽略递归结果，零和 successor 分别定义等于 `k a` | 三个泛型 `cases a <;> rfl` |
| `PyrD.dsel`、`PyrD.dpk` 增加 `@[macro_inline]` | 只添加编译属性，定义体逐字不变；内联避免编译求值时先求两个未选子树 | 两条定义体全量比对 |

适配器共有五个 Lean 内核等价守卫。`macro_inline` 只影响编译求值方式，没有新增公理、计算分支或假设。生成核心未保留上游 theorem 证明，也未引入 `sorry`、自定义 `axiom`、`unsafe` 或外部调用来承认数值结果。

## 3. 全部有限数据检查及实际根

240 项编译检查为 9 个总体检查、7 个连续根外覆盖检查、192 个完整点表检查和 32 个完整根树检查：

| 检查组 | 实际表达式／覆盖范围 |
| --- | --- |
| `win16` | `Pyr.allBelow 16 winOk` |
| `value-top`、`value-block512` | `topOk TOP BK`；`allFrom 0 512 (fun j => blockOk (BK j) j)` |
| `derivative-top`、`derivative-block512` | `topOk2 TOPD BKD`；`allFrom 0 512 (fun j => blockOk2 (BKD j) j)` |
| `convex-regions` | `rgOk REG` |
| `large-gap7` | 所有七个方向的 `cN * SC ≤ BS[r] * SMAX r` |
| `adjacent7` | 所有七个方向的 `cN * 4 ≤ tA TS (ADJ[r])` |
| `root-W` | `7 * KB ≤ 1099511627776` |
| `cover-0` 至 `cover-6` | 完整 `coverChk cN (tA TS (ADJ[r])) (SC / 2) (SMAX r) (COV[r])` |
| 192 个 `point-list-j` | 对该编号的完整原始列表执行 `ptlOk`，不是抽样点 |
| `root-0` 至 `root-31` | 对源码各 `wccj_j` 的原完整表达式与原正整数执行 `Nat.beq` |

这些检查实际调用原有数值闭包、表路由、区间下界、leaf decoder 和有界树递归。所有值表／导数表的 512 块均遍历，所有 192 个点表均遍历，32 棵根树均执行到原声明的消费位置。叶子编码的末尾剩余位不必清零：覆盖证明使用从起始位置读取的合法完整证书前缀，检查的正消费位置与原声明相同。

根使用 `SC = 32768`、`SA = 100000000`、`cN = 805003`。每棵树的初始 cell 有七个 gap、21 个 span、metadata `M = 0`；全部 span 的初始下界为 0，上界为 `1099511627776`。初始 gap 区间如下，五个二选一方向按原根表达式的高位到低位生成全部 32 个笛卡尔组合：

| gap | 初始整数闭区间 |
| --- | --- |
| `g0`、`g6` | `[27136, 917504]` |
| `g1`、`g5` | `[29184, 44544]` 或 `[52736, 466944]` |
| `g2`、`g4` | `[29696, 43008]` 或 `[54784, 352256]` |
| `g3` | `[29696, 43008]` 或 `[54784, 327680]` |

每棵根的 `walkC` fuel 为 128，起始位为 1，根前执行一次 `tm`／`matC`，递归节点按原实现更新闭包。按根编号 0–31，必须且实际检查的消费位置为：

```text
8086,17530,39365,31362,84866,98514,53623,25468,
46633,51837,79730,34388,53774,40814,59698,9391,
17940,47838,59890,27034,76566,63562,42914,63478,
29321,27057,37691,18175,33587,68280,9278,3740
```

此外，独立只读程序从固定源码解析全部 `PR`、`TS`、`SL`、`ADJ`、`BS` 字面数据，再执行七项有限结构检查，全部通过：21 个长度至少为 2 的跨度枚举完整；26 个正权重 pair 的跨度引用正确；全部 28 个端点组合的 `SL` 定位正确；七个 `ADJ` 均指向实际相邻 pair；压力权重和为 404350 且反转对称；pair 权重反转对称；七种 span 长度各自的总权重均不超过 `2 * 100000000`。这些是 Python 精确整数与有限列表检查，不能表述成额外七个 Lean 内核定理。

## 4. 展开分割与通用闭包的内核桥

自写 `AMPC8StructuralBridge.lean` 不导入上游证明。它使用受审纯定义，写出通用 `genericGsplit`、`genericSsplit`，然后对任意 continuation、任意位置和任意 57 字段状态证明：

- 全部 7 个 `gsplit` 等于通用 gap 中点分割；
- 全部 21 个 `ssplit` 等于通用 span 中点分割；
- `tm` 等于把状态转为 `Cl`、执行 `matC PR`、再转回原 continuation。

每条桥使用 `cases s; rfl`，对所有状态成立，没有只验合法状态样本。通用 gap 分割把上／下端点设为 `qG`，分别调用 `cupd 7 PR SL` 的 `(r,r+1)`／`(r+1,r)` 方向；span 分割则用 `qR`、原 `PR` 的两个端点和对应方向。前一子树的正消费位置作为后一子树的开始位置，零值失败分支也与原实现相同。

因此，前一冻结语义审查对通用 `cupd` 的 telescoping 下界、span 约束及两个闭区间子 cell 的覆盖证明，现在通过 28 条通用内核等式连到了实际执行的所有展开分割。`tm` 的第 29 条桥补齐根的初始闭包。这里没有另加对 `genericcupd` 实数语义的未证明假设；该实数语义仍由原逐段审查负责，本桥负责实际计算式的完全相同。

## 5. 实际 minorant 与通用检查器的内核桥

自写 `AMPC8MinorantBridge.lean` 证明对所有纯参数成立的接口：

```text
mcheckP ... = true  →
mcheckGZ ... 8 7 BS TS cN (toCl s) [全部26个minorant记录]
  [P0,...,P6] [S0,...,S6] Cp Cm = true
```

这条桥没有附加对叶子、状态、混合权重或编码的样本假设。证明先建立展开的 `mvK`／`mcK`／`mslK` 与通用版本的等式，再重写整个 `mcheckP` 假设得到上述通用式。各 helper 对 `k = 0,1,2,3` 和 `k ≥ 4` 的所有情况证明，覆盖原 fallback 分支。

为避免 Lean 内核直接展开含大常量的 `Nat.sub` 造成资源耗尽，自写证明先把 slope 偏移量 `2000000000` 抽象为任意 `B : Nat`，证明 `mcpB_eq`／`mcnB_eq`，最后实例化回原常量。改变的是证明组织，原数值定义与偏移量均保持不变。最终得到第 30 条主桥 `mcheckP_bridge`，它把实际 minorant 叶子连到已经逐段审过的通用整数 guard 和实区间下界。

两份 tracked 桥分别与本地先行通过的冻结附录逐字一致。独立生成的 `StructuralBridge.lean` 和 `MinorantBridge.lean` 均曾使用 Lean 4.34.1、`import Std`、`--tstack=32768 -j1` 实际编译退出 0；最终生成器再将这两份 tracked 内容各追加一次，编译检查随完整 runner 重做。30 条主桥的 `#print axioms` 均只列出 Lean 标准的 `propext`，没有 `sorryAx`、自定义公理或把原结果当公理承认。这里的表述是“无新增公理”，不是“零公理”。

## 6. 复演器的失败封闭与求值信任边界

生成器完整审读后确认：

1. `__debug__` 守卫拒绝 Python `-O`，避免优化模式删除关键 `assert`；固定源身份、2,744 个声明和三处 callback 改写数均检查。
2. 两份 tracked 桥内容的哈希纳入保存结果，生成器拒绝其 `sorry`／`axiom` 声明；本次还人工完整阅读和逐字比对了桥文件。
3. Lean 使用固定工具链 `leanprover/lean4:v4.34.1`，参数 `--tstack=32768 -j1`；`subprocess.run` 使用参数数组、`shell=False`，记录真实进程退出码。
4. 日志的实际标签序列必须恰等于 240 项预期顺序，每项均 `true`；少项、重复、换序、假值、非零退出、报错、stack overflow、panic 均拒绝保存 PASS。
5. `--check` 先重新构建忽略目录中的输入、完整运行全部检查，再比较 saved JSON 的规范化完整字节；不能仅凭已有 JSON 文件认定本次通过。

最初临时 runner 曾在 `point-list-355` 出现 stack overflow，并没有通过全部 240 项，因此保留为失败记录。随后该点在 32 MB stack 下单独得到真实退出 0、`true`；这解释运行资源问题，没有替代完整重跑。原 `forceR/B/T` 的忽略递归结果写法和未内联 dispatcher 的 eager 求值也曾导致不必要的大量求值。上述优化均有泛型内核守卫或定义体不变比对，最终全量复演重新覆盖全部检查。

240 个有限断言是 Lean 编译器运行 `#eval` 得到的精确 `Nat`／`Int`／`Bool` 结果，没有浮点数。它们的信任边界包含 Lean 编译器和整数运行时，**不能改称为 240 个 `decide +kernel` 证明**。另一方面，五个适配器守卫和 30 条主桥是实际 Lean 内核证明；实数语义是固定源码的独立人工逐段审查。三者的职责和限制均保留。

## 7. 最终结果与准入范围

本文作者实际执行 `C:\Python312\python.exe -B -X utf8 scripts\am_pc8_finite_replay.py --check`，真实进程退出码为 0，输出 `PASS: 240 compiled checks, 7 exact structure checks; saved output matches`。最终脚本、core、runner、两份桥哈希均与第 1 节对应；保存结果 `output/am-pc8-finite-replay.json` 为 17,001 字节、998 行，原始 SHA-256 为 `48c29521994321837b60ea39661b93f87c28560b5f19932c583ad8b29f5dd549`。

最终 `numeric-replay-log.txt` 的全部 270 行已经完整读回，并独立比较其完整 manifest 与结果 JSON：30 条主桥仅依赖 `propext`，240 项唯一有序检查全部为真，含全部 192 个点表和编号 0–31 的 32 棵根树，无错误、stack overflow 或 panic。`root-W` 属于总体检查，未混计为第 33 棵根。Windows 日志原始字节为 8,011，原始 SHA-256 为 `ea5baa334c30a48d5eed7f7e1f56c7f16cf612d03b9cf6485c0194aa28362577`；规范化为 LF 后的 SHA-256 为 `ab799226a3d23b619c38339bda4e146582eb78f13da5cde8ed55e9b16eda0ffa`。

因此，前一冻结文档的完整数值复演门及实际展开表达式的定义等式门均已补齐。该结论使用完整表、所有根及每类叶子的连续实数语义，不以平台 theorem 状态、哈希或样本替代全域覆盖。

本次准入支持固定原八点 AM 配置的 `805003 / 100000000` 七维全域核门，并依赖前一独立审查的连续实区间和根覆盖语义。它不能跳过后续归一化、谱权重与 pressure 消费接口，也不能替代外部 zeta 定理证明。已有方案的完整证书得到准入，与得到一条新的零点比例纪录，是不同的结论。
