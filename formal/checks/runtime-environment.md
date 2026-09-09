# 本机验证环境

2026-09-09，Windows，Lean 4.32.2。工作区 F 盘经系统只读查询确认为 USB HDD，
并行解压和 Lean 导入出现明显随机 I/O 瓶颈；CPU 亲和性实验没有降低 leantar 的线程数，
该无效选项已移除，没有修改全局设置或其他任务。

本机随后将 **生成缓存** 通过目录联接放到 C 盘专用 SSD 缓存目录。
项目自身的 Lean 源码、蓝图、vendored 源码和 Git 仓库仍在原工作区。
原有 HDD 缓存完整保存在 `formal/.lake/hdd-backup-05156b5b/`，未删除。
本机路径映射保存在未纳入 Git 的 `formal/build/ssd-cache-location.json`。

SSD 中的 mathlib 从官方仓库获取同一固定提交，未借用其他研究项目的对象库。
这些缓存目录和目录联接均被 Git 忽略；它们不属于交付源码依赖。
新的检出环境按 formal/README.md 正常建立缓存即可，不需要上述本机目录。
