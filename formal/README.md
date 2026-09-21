# F₁ 路线的 Lean + mathlib 形式化蓝图

## 2026-09-20：谱迹根空间与双矩修正

[TraceRadical.lean](F1/Analysis/TraceRadical.lean)新增八条代数引理，已实际通过Lean编译，
传递公理仅含propext、Classical.choice、Quot.sound。
它核对谱迹与完整配对之间的两矩项、1/16残差、双矩基和精确根空间识别。
所有解析比较均为显式前提；没有形式化Gaussian积分、完整显式公式或几何主除子。

[检查脚本](scripts/check_trace_radical.py)复用可配置的定向检查器，
结果另存[trace-radical-verification.json](checks/trace-radical-verification.json)。
本机先用prepare_local_trace_runtime.py的--entry F1.Analysis.TraceRadical准备依赖，
再以相同--cache-backup及--runtime-dir运行check_trace_radical.py。
既有LocalTrace及2026-09-10完整构建报告保留；本轮未重建整个F1库。

## 2026-09-20：连续研究中的即时Lean检查

当前持续GOAL为active；下方2026-09-09“暂停”文字是当时的历史状态。
按用户新增要求，推导不确定时直接用Lean检查，并将可复用证明保存在本目录。
新增[LocalTrace.lean](F1/Analysis/LocalTrace.lean)，检查404的反射、自卷积单位元值、
非零连续紧支函数的严格正性，以及单位元修正的不可见性／非零自配对差异。
八条结果已通过Lean 4.32.2实际检查，传递依赖仅为propext、Classical.choice、Quot.sound，
不调用原有weil_convergence或weilCriterion的admission。公共测试函数定义已移入
[TestFunctions.lean](F1/Analysis/TestFunctions.lean)，保持原有名称和定义。

定向验证入口：[check_local_trace.py](scripts/check_local_trace.py)；
[结果](checks/local-trace-verification.json)、[实际编译输出](checks/local-trace-build.txt)、
[传递公理](checks/local-trace-axioms.txt)记录当前状态。运行命令：

    python scripts/check_local_trace.py

本机旧构建junction指向已不存在的C:\Users\ip目录；可使用同一项目内已核对提交的备份：

    python scripts/prepare_local_trace_runtime.py --cache-backup .lake/hdd-backup-05156b5b --runtime-dir "$env:TEMP/rh-weil-local-trace-20260920"
    python scripts/check_local_trace.py --cache-backup .lake/hdd-backup-05156b5b --runtime-dir "$env:TEMP/rh-weil-local-trace-20260920"

第二组命令用于PowerShell。准备脚本逐项核对导入闭包所需的olean／server／private／IR文件；
缺失时须先从固定提交的官方缓存恢复，再运行检查。正式研究源码始终保存在formal。
本机实际检查在临时本地盘运行，以避开旧junction及H盘缓存加载问题；不改旧junction。
不用--runtime-dir时，新编译产物放在.lake/local-trace-check。
本轮还用准备脚本的--entry F1.Analysis.Weil和检查脚本的--check-weil，
对移动定义后的Weil模块进行兼容性编译，保留它原有两处显式admission。
该定向运行不冒充整个F1库重建；原[完整构建验收](checks/README.md)仍保留其日期和范围。
本轮未形式化局部域全部迹定理、几何主关系、RR或RH。


首次阅读可先看[本科背景讲义](../docs/f1-route-from-undergraduate-math.md)：
解释实际对象、精确条件与条件证明；技术细节再查本目录。

2026-09-09。当前工作按用户新指令暂停原持续研究，先建立可检查的形式化框架。
数学起点为[笔记363](../notes/363-f1-arithmetic-geometry-and-existence-audit.md)。
这是允许 `sorry` 的研究蓝图；不是 RH 证明，也没有证明全局算术几何对象存在。
初版已通过完整构建及 20 项传递公理检查，十个经典 `sorry` 精确登记；
见[验收记录](checks/README.md)。原持续研究保持暂停。

2026-09-10：新增 [G0–G8 几何实现条件包](blueprint/geometric-realization.md) 和
`F1/Geometry/GeometricRealization.lean`。源相对的局部层、有效性、全局比较与截面
条件已编码；六个新增条件推论不增加 `sorry`。完整算术来源及相对迹实现仍开放。
本次完整构建 3472 个任务及全部 26 项传递公理检查通过，结果见 `checks/verification.json`。

## 目录与入口

- `F1.lean`：完整导入入口；`Target` 是 mathlib 的 `RiemannHypothesis`。
- `F1/Arithmetic`：素数局部化、有限支集截面、实际 `Spec ℤ` 上的预层与 stalk 命题。
- `F1/Analysis`：圆平均、有限 Jensen 提升、弱二阶导数、固定算术 Weil 型及经典桥梁。
- `F1/Geometry`：有理对应点集模型、Newton reduced-square 表示、带显式假设的存在性推理。
- [blueprint/README.md](blueprint/README.md)：依赖图、缺口分类、推进顺序和原文定位。
- [几何实现规范](blueprint/geometric-realization.md)：G0–G8 的量词、公式及 Lean 覆盖边界。
- `vendor/`：mathlib 之外的八个依赖的完整版本化源码与原许可证；见[说明](vendor/README.md)。
- `scripts/`：复制来源、可选缓存复用及验证工具。`checks/` 保存本轮实际验证记录。

## 构建

固定 Lean `v4.32.2`，mathlib `905b95818eb32af7874a58b427f50c1711a5e96c`。
在本目录、已安装 elan 与 Python 3.10+ 的 PowerShell 环境执行：

```powershell
$env:MATHLIB_NO_CACHE_ON_UPDATE='1'
lake update
lake build cache
lake env python scripts/get_cache.py
python scripts/verify.py
```

其他 shell 同样先将环境变量 `MATHLIB_NO_CACHE_ON_UPDATE` 设为 `1`，再运行其余命令。
该变量关闭上游 post-update 自动缓存步骤；后面的脚本在源码校验后完成对应工作。
`verify.py` 实际运行 `lake build`、`lake env lean F1/Audit.lean` 和源码／Git 跟踪校验，
输出保存于 `checks/`。只整理过部分缓存时可用 `get_cache.py --repair` 重建本项目生成的
缓存标记并重新解压匹配的官方归档；该选项不修改 Lean 源码。

`lake build` 允许明确列出的 `sorry`，因此构建成功不表示所有定理完成。
`F1/Audit.lean` 的 `#print axioms` 检查传递依赖；仅搜索证明正文不足以识别
`rh_of_existence` 等间接依赖 `sorryAx` 的结论。审核时应同时阅读蓝图和这些输出。

mathlib 由固定提交获取，其余依赖通过根 `lake-manifest.json` 使用本地 `vendor/`。
缓存工具会将 path 与 git 依赖视为不同版本，因此使用 `get_cache.py`：先核验副本字节与
上游版本一致，再从未改动的 mathlib 目录运行官方缓存工具，保留 Lake 提供的本地源码路径。
官方依赖归档的内部路径仍是 `.lake/packages/NAME`，脚本在成功解压后将生成产物复制到
相应的 `vendor/NAME/.lake/build`，并最后安装 trace；仅改变运行目录不足以完成这一映射。
不需要访问其他研究项目。`scripts/bootstrap_from_cache.py PACKAGES` 是可选缓存复用途径，
**必须先运行 `lake update`**，它不初始化 Git 或复制源树。它只读取与锁定版本一致的
既有官方包缓存，按官方清单复制完整产物后才安装 trace；缺失项仍需正常获取／构建。
可先加 `--check-only` 检查版本前提。此途径不复制其他用户项目的研究代码，也不替代正式构建。
首次下载若需本机代理，可在 PowerShell 设置
`$env:https_proxy='http://127.0.0.1:10808'` 和同值 `http_proxy`；端口仅为本机提示。

## 如何理解完成程度

`nonpositive_of_existence` 检查的是：双次数下降、零双次数有效刚性、以及
**非零有效除子**存在性共同推出固定 Weil 型非正。其假设尚未在实际算术平方上构造。
`rh_of_existence` 另依赖尚未形式证明的经典 Weil 判据。
`BareExistenceProblem` 只是抽象接口的存在量词，没有提供见证；其本身并不编码
与 Connes–Consani 算术平方的自然比较。这样的比较必须另证。

局部幺半群、有限 Jensen 提升和 `2 → 3 → 6` 方程复合是可独立检查的基准。
互素参数且分母为正时的复单位点集参数化双射已无 `sorry` 地形式证明，逆用经典选择。
它们没有自动连到上述存在性假设。蓝图保留这一断点，并将真实研究输入与经典证明待补分开。

### Unit descent checks (2026-09-20)

[F1/Analysis/UnitDescent.lean](F1/Analysis/UnitDescent.lean) checks invariance under a specified
regular-unit subgroup, its equivalence to quotient factorization when normality is supplied,
a nonzero-unit obstruction, and the obstruction to retaining a nonzero moment after killing a relation.
[The dedicated report](checks/unit-descent-verification.json) records four Lean 4.32.2 results
without sorryAx dependencies. [The source inventory](checks/unit-descent-source-audit.json)
has 15 project Lean files and the same ten registered admissions.

Run `python scripts/check_unit_descent.py`, adding the cache/runtime options used by
the shared LocalTrace runner if needed. The analytic adele/determinant construction and
the identification of regular units remain outside these formalized statements.
No full F1 build was performed for this addition. Ordinary Cartier descent does not by
itself impose the same vanishing condition on a metrized arithmetic divisor with a Green term.


## 2026-09-20：实际带权箭头的代数检查

[WeightedArrows.lean](F1/Analysis/WeightedArrows.lean)的九条结果已实际通过Lean4.32.2。
包含复合／幂／有限词的箭头标签、非闭合词的零对角、逆标签乘积，
以及留数多项式正性和有下界次数递推。逐项公理仅含标准三项，无sorryAx依赖。
[运行报告](checks/weighted-arrows-verification.json)、[源码清单](checks/weighted-arrows-source-audit.json)
另存，原十处admission与旧检查报告保留。当前项目Lean源码16份，vendor仍为8包806文件。

运行 python scripts/check_weighted_arrows.py；本机可加前述固定cache/runtime参数，
依赖准备脚本入口为 --entry F1.Analysis.WeightedArrows。
这些算子定义在全部函数上，未形式化Hilbert迹、Fredholm、Poisson、导出范畴或RH。
纸面范围与实际算术来源见[407](../notes/407-f1-prime-arrows-fredholm-and-relative-complex.md)。


## 2026-09-20：统一轨道乘积估计

[OrbitDecay.lean](F1/Analysis/OrbitDecay.lean)的四项定向检查已通过Lean4.32.2：
访问权乘积、逐点上界、有限访问次数下的乘积界及等距轨道跨度。
[报告](checks/orbit-decay-verification.json)不含sorryAx依赖；
[源码清单](checks/orbit-decay-source-audit.json)保留旧十处admission，项目源码17份。
运行 python scripts/check_orbit_decay.py；依赖准备入口为 --entry F1.Analysis.OrbitDecay。
可使用与前述相同的固定cache/runtime参数。未重建全F1。
Banach交叉积、谱半径、整数访问计数、边界表示及导出范畴为
[408](../notes/408-f1-orbit-completion-and-prime-boundaries.md)的纸面内容，没有冒称形式化。

## 2026-09-20：边界移位的几何逆与右逆方向

[BoundaryResolvent.lean](F1/Analysis/BoundaryResolvent.lean)新增四项实际Lean4.32.2检查：
幂零链的左右几何逆，以及BS=I下后向移位分解与右逆。
[报告](checks/boundary-resolvent-verification.json)和[源码清单](checks/boundary-resolvent-source-audit.json)
分别记录内核验证与源码审计；无sorryAx依赖，项目源码18份，旧十处admission不变。
运行 python scripts/check_boundary_resolvent.py，依赖准备入口
--entry F1.Analysis.BoundaryResolvent；可使用前述固定cache/runtime参数。
[409](../notes/409-f1-boundary-prime-power-kernels-and-heat-defects.md)的无限直和、核维数、
热迹及群胚解析内容未由这四条代数引理形式化，本轮未重建全F1。

## 2026-09-21：周期过渡与有界整数漂移

[BoundaryClutch.lean](F1/Analysis/BoundaryClutch.lean)新增五项实际Lean4.32.2检查：
移位运输、一次相位因子、带权置换行列式、迭代整数漂移和有界性矛盾。
[报告](checks/boundary-clutch-verification.json)无sorryAx依赖；
[源码清单](checks/boundary-clutch-source-audit.json)为19份项目源码，旧十处admission保持。
运行 python scripts/check_boundary_clutch.py，依赖准备入口
--entry F1.Analysis.BoundaryClutch，可用前述固定cache/runtime选项。
[410](../notes/410-f1-boundary-kernel-bundles-and-relative-k-classes.md)中的连续核丛、
绕数、Fredholm、Morita与K理论另属纸面论证；未重建全F1。

## 2026-09-21：端点等距元的缺陷代数

[EndpointDefect.lean](F1/Analysis/EndpointDefect.lean)新增六项实际Lean4.32.2检查：
左逆缺陷的左右消失、幂等性、幂抵消、不同幂扇区和非零性。
[报告](checks/endpoint-defect-verification.json)无sorryAx依赖；
[源码清单](checks/endpoint-defect-source-audit.json)包含20份项目源码，原十处admission保持。
运行 python scripts/check_endpoint_defect.py，依赖准备入口
--entry F1.Analysis.EndpointDefect，可用前述固定cache/runtime参数。
[411](../notes/411-f1-full-rational-relative-classes-and-logarithmic-trace.md)的Hilbert收敛、
交叉积、PV、K类及半有限迹另属纸面推导；本轮未重建全F1。

## 412：横向相干尾与加性读出障碍（2026-09-21）

[TransverseTrace.lean](F1/Analysis/TransverseTrace.lean)的七项结果通过Lean4.32.2，无sorryAx。
直接证明几何尾部HasSum、归一化及重叠，另核准仿射／几何二阶差分与共同混合项障碍。
[运行报告](checks/transverse-trace-verification.json)与[源码清单](checks/transverse-trace-source-audit.json)记录范围；
p进空间、Hilbert悬挂、trace-class、来源比较及K理论另由纸面审查，不在这些形式化内。
当前21份项目Lean源码，原十处admission保持，未重建完整F1。

## 413：两位连接映射的代数检查（2026-09-21）

[BoundaryGluing.lean](F1/Analysis/BoundaryGluing.lean)的七项结果通过Lean4.32.2，无sorryAx。
覆盖有限支平移不变必零、秩边界的核／满射／非负秩障碍、带符号等秩条件、
不同长度残差及循环群两个加性次数的行列式为零。
[报告](checks/boundary-gluing-verification.json)与[源码清单](checks/boundary-gluing-source-audit.json)保存实际范围；
商拓扑、Morita、PV、Bott及完整K计算为纸面证明，不在这些形式化内。
项目22份Lean源码，原十处admission及历史报告保持，未重建完整F1。

## 414：实际边界移位与有限通量（2026-09-21）

[BoundaryUnitary.lean](F1/Analysis/BoundaryUnitary.lean)的六项结果已通过Lean4.32.2，无sorryAx。
包括单边正移位在双边序列上的左逆、秩一缺陷及单射性，
有限望远镜和、端点1到0的通量和带权分部求和。
[内核报告](checks/boundary-unitary-verification.json)和[源码清单](checks/boundary-unitary-source-audit.json)限定实际范围；
未形式化Hilbert有界性、C*满角、Fredholm指数、共同Fourier投影或几何构造。
项目23份Lean源码，原十处admission及全部历史报告保持，未重建完整F1。

## 415：真实二阶投影与缺陷恒等式（2026-09-21）

[DefectProjection.lean](F1/Analysis/DefectProjection.lean)的18项定向检查通过Lean4.32.2。
包含非交换二阶矩阵乘法、双侧酉性、相对投影的幂等／自伴、缺陷差／对角和、
平方根交织式的伴随、壳层标量消去及换位子传递恒等式；无sorryAx依赖。
[报告](checks/defect-projection-verification.json)及[源码清单](checks/defect-projection-source-audit.json)保存；
当前24份项目源码，旧十处admission与历史检查保持，未重建整个F1。
运行 python scripts/check_defect_projection.py；依赖准备入口为 --entry F1.Analysis.DefectProjection，
使用上面的固定cache/runtime参数。C*正性与函数演算、理想归属、Hilbert重叠和迹收敛没有被本次形式化。

## 416后候选：投影连接的六条代数检查（2026-09-21）

[ProjectionConnection.lean](F1/Analysis/ProjectionConnection.lean)核验投影导数的角内消失、
双交换子、角内元素平行性、压缩残差及反自伴性；六项通过Lean4.32.2，无sorryAx。
[报告](checks/projection-connection-verification.json)、[源码清单](checks/projection-connection-source-audit.json)保存。
实际Green系数的角内导数为零仍需独立算出；无界定义域、演化与算术迹不在这些代数引理范围。
运行 python scripts/check_projection_connection.py，准备入口 --entry F1.Analysis.ProjectionConnection，
使用前述固定cache/runtime参数。项目25份Lean源码、原十处admission及旧报告保持。
