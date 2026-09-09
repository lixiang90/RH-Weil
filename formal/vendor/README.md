# 依赖源码副本

本目录复制 mathlib 固定提交所依赖的 batteries、Qq、aesop、proofwidgets、
importGraph、LeanSearchClient、plausible、Cli。它们由根 Lake 配置通过本地路径加载，
不是仅提供链接。每个项目保留原许可证、版权声明和源码；适用许可请直接阅读各目录 `LICENSE`。

[manifest.json](manifest.json) 记录每个项目的上游 URL、精确 Git 提交、源码归档 SHA256、
每个文件的 SHA256 和字节数。副本由 `../scripts/vendor_mathlib_dependencies.py` 从
匹配提交的官方依赖缓存以 `git archive` 导出，不包含相邻项目的研究代码。
唯一表示调整：batteries 的文档符号链接展开为所指向文件的内容，记录在 manifest 中。
构建产生的 `.lake/` 不纳入版本控制。原上游配置文件予以保留，根配置覆盖依赖解析。

mathlib 本体按用户允许的例外固定版本获取，不在此重复提交。
当前没有借用其他第三方 RH/F₁ 形式化研究项目的代码；今后若引入，须复制实际代码、
许可证和来源版本，并补入清单，不以外部链接替代源码。
