# F₁ 路线的 Lean + mathlib 形式化蓝图

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
