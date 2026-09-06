# 论文源文件与编译

主 TeX 源文件统一放在本目录；最终 PDF 统一放在 `output/pdf/`。
2026-09-06 的目录迁移不改变论文内容，现有 PDF 按字节原样保留。

外部文献原始 PDF 统一归档于 [`../literature/`](../literature/README.md)，不与本项目论文混放。
2026-09-06 的 [305 文献更新](../notes/305-post-6725-literature-baseline-audit.md)已记录67.3%以上后续草稿及审核边界；下列项目论文PDF仍为既有快照，本次未重编译。

| 论文 | 主源文件 | 最终 PDF | 编译器 |
|---|---|---|---|
| Weil 结构与存在性审计 | [rh-weil-structure-paper.tex](rh-weil-structure-paper.tex) | [PDF](../output/pdf/rh-weil-structure-paper.pdf) | XeLaTeX |
| 部分 Weil 配置 | [partial-weil-configurations-paper.tex](partial-weil-configurations-paper.tex) | [PDF](../output/pdf/partial-weil-configurations-paper.pdf) | XeLaTeX |
| Abel 质量预算障碍 | [abel-mass-obstruction-paper.tex](abel-mass-obstruction-paper.tex) | [PDF](../output/pdf/abel-mass-obstruction-paper.pdf) | pdfLaTeX |

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
