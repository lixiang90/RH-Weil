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
| 自由 b 的补偿几何与临界边界 | [free-b-compensated-probe-boundary-paper.tex](free-b-compensated-probe-boundary-paper.tex) | [PDF](../output/pdf/free-b-compensated-probe-boundary-paper.pdf) | pdfLaTeX |
| plain moment 范围延伸与三次反馈边界 | [kappa-feedback-cubic-boundary-paper.tex](kappa-feedback-cubic-boundary-paper.tex) | [PDF](../output/pdf/kappa-feedback-cubic-boundary-paper.pdf) | pdfLaTeX |

新稿将笔记 441–445 的结果整理为正式论文：在明确引用原稿通用结果及全 Hecke \(7/8\) 结论的前提下，推出严格半平面 \(\Re s>69999/80000\) 无零。正文给出可变槽 low 证明、局部 Euler 域、实际 detector 容量、联合误差、连续证书及完整延拓反证；不宣称独立验收原稿或完成新的 Lean 认证。最终源稿、PDF 和独立审查的哈希及编译情况见 [构建清单](../reviews/2026-10-07/69999-paper-build-manifest.json)。

自由 b 新稿另行记录 449 的结果：在同一明确引用输入包下得严格边界
\((1507-2\sqrt{921})/1653\approx0.874957069799\)，并给有理见证 \(40773/46600\)。
它重证自由 b 的完整 low、连续代数证书、实际容量与全族延拓，
最优性只限原 low 交点和计数包络，不声称新比例、RH 或外部 kernel 验收。
旧 \(69999/80000\) 论文按已交付版本保留；新稿最终审查与 PDF 见
[自由 b 构建清单](../reviews/2026-10-07/free-b-paper-build-manifest.json)。

κ 反馈新稿另行记录 450–451 的结果：从指定底层输入重证
plain moment 至 37/50≤κ≤1，再用实际 κ=2β*−1 支付反馈费用。
严格边界 σ*=11/12−e*/4，其中 e* 是 657e³−954e²+21e+20=0 的指定根，
σ*≈0.874957019420099。完整引用前件、逐槽 mesh 条件、连续有理证书与全族延拓
均在正文；两份全文审查、最终源/PDF与版面验证见
[三次边界构建清单](../reviews/2026-10-07/kappa-feedback-paper-build-manifest.json)。
前两篇已交付无零边界稿保持原版；该稿仍不宣称新比例或外部 kernel 验收。

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
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf papers/free-b-compensated-probe-boundary-paper.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf papers/free-b-compensated-probe-boundary-paper.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf papers/kappa-feedback-cubic-boundary-paper.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf papers/kappa-feedback-cubic-boundary-paper.tex
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
