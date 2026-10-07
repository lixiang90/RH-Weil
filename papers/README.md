# 论文源文件与编译

主 TeX 源文件统一放在本目录；最终 PDF 统一放在 `output/pdf/`。
2026-09-06 的目录迁移不改变论文内容，现有 PDF 按字节原样保留。

外部文献原始 PDF 统一归档于 [`../literature/`](../literature/README.md)，不与本项目论文混放。
2026-09-06 GOAL 周期已将本轮纠错同步到下列三份 PDF：结构稿 45 页、部分配置稿 26 页、Abel 稿 11 页。源稿和 PDF 哈希固定于 [编译清单](../reviews/2026-09-06/paper-build-manifest.json)，核查范围见 [复核记录](../reviews/2026-09-06/README.md)。

结构稿本轮仅认证所改 PLF、65/66 维、AEJ 与 Sobolev 等明确范围；早期全文没有借本次编译获得重新认证。部分配置稿保留真实四阶预算的条件性；Abel 稿完成全文独立复核，按技术重建归类、不作优先权声明。306–309 的完整模型和准入记录仍在笔记，不声称全部并入三篇论文。

| 论文 | 主源文件 | 最终 PDF | 编译器 |
|---|---|---|---|
| Weil 结构与存在性审计 | [rh-weil-structure-paper.tex](rh-weil-structure-paper.tex) | [PDF](../output/pdf/rh-weil-structure-paper.pdf) | XeLaTeX |
| 部分 Weil 配置 | [partial-weil-configurations-paper.tex](partial-weil-configurations-paper.tex) | [PDF](../output/pdf/partial-weil-configurations-paper.pdf) | XeLaTeX |
| Abel 质量预算障碍 | [abel-mass-obstruction-paper.tex](abel-mass-obstruction-paper.tex) | [PDF](../output/pdf/abel-mass-obstruction-paper.pdf) | pdfLaTeX |
| 七分之八无零边界的参数改进 | [seven-eighths-boundary-improvement-paper.tex](seven-eighths-boundary-improvement-paper.tex) | [PDF](../output/pdf/seven-eighths-boundary-improvement-paper.pdf) | pdfLaTeX |

新稿将笔记 441–445 的结果整理为正式论文：在明确引用原稿通用结果及全 Hecke \(7/8\) 结论的前提下，推出严格半平面 \(\Re s>69999/80000\) 无零。正文给出可变槽 low 证明、局部 Euler 域、实际 detector 容量、联合误差、连续证书及完整延拓反证；不宣称独立验收原稿或完成新的 Lean 认证。最终源稿、PDF 和独立审查的哈希及编译情况见 [构建清单](../reviews/2026-10-07/69999-paper-build-manifest.json)。

## 从仓库根目录编译

不能先切换到 `papers/` 再照抄下面命令：结构论文的
`\input{paper-sections/...}` 相对于仓库根目录解析。
`paper-sections/` 仍位于根目录，其内容和引用保持不变。

```powershell
xelatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf papers/rh-weil-structure-paper.tex
xelatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf papers/rh-weil-structure-paper.tex
xelatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf papers/partial-weil-configurations-paper.tex
xelatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf papers/partial-weil-configurations-paper.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf papers/abel-mass-obstruction-paper.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf papers/abel-mass-obstruction-paper.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf papers/seven-eighths-boundary-improvement-paper.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf papers/seven-eighths-boundary-improvement-paper.tex
```

两次编译用于更新引用。编译中间文件由 `.gitignore` 排除。
不覆盖正式 PDF 的迁移检查可用 XeLaTeX 的 `-no-pdf` 或 pdfLaTeX 的
`-draftmode`，将输出目录改为 `tmp/pdfs/` 下的专用子目录。

Overleaf 请上传完整目录结构，分别选取上表主文档和编译器。
PDF 排版同步与数学研究轮次分开安排；不要求每轮重编译。

## 目录回归检查

```powershell
python scripts/check_repo_layout.py
```

该检查只验证目录、论文文件及相对引用，不验证数学定理或 PDF 版面。
版本管理中的PDF允许放在本项目的 output/pdf/ 或外部文献 literature/，其他散落路径仍会报错。
