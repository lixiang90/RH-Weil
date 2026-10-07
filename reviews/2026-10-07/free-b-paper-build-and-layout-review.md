# 自由 b 正式论文构建与版面验收

2026-10-07。对象为独立新稿 `papers/free-b-compensated-probe-boundary-paper.tex`。
本文只记录构建、最终版本和版面验收；数学全文由两个独立审查报告验收。

## 1. 交付版本与命题范围

最终 TeX canonical LF SHA-256：
`5df2b6ad687572229e2c4d41292bee6cf81b57a13b762173d26732169f1688db`。
876 行，35118 canonical UTF-8 字节。
PDF 为 12 页 A4，401489 字节，raw SHA-256：
`1c1322b67f30c136858fcc2de2fca468fc48f450be2ed573cff93e931774f436`。

相对论文 Definition 1.1 明列的输入包 R，得严格无零边界
(1507−2√921)/1653≈0.874957069799；principal 极点例外，边界线除外。
适用正文指定的有限阶 Hecke、Dirichlet 与 zeta；参数最优性仅限该 low 交点和计数包络。
不是外部整篇证明或 kernel 认证，不证明 RH，也不提高临界线零点比例。

[radial 全文审查](free-b-paper-review-radial.md)及
[twisted 全文逆审](free-b-paper-review-twisted.md)均对本稿重新逐段审查并限定 PASS [T/R]。
它们绑定上列最终 TeX，不以 449 的既有审查代替正式论文全文审查。

## 2. 编译与文本检查

已请求在 Codex 内置编辑器打开保存的 TeX；内置编译调用一次，返回
`compile-failed: Unable to find standard directories for platform`。
随后使用本机既有 MiKTeX pdfLaTeX 1.40.25（MiKTeX 23.5）编译成功；没有安装新依赖。
从仓库根目录可重建：

~~~powershell
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf papers/free-b-compensated-probe-boundary-paper.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf papers/free-b-compensated-probe-boundary-paper.tex
~~~

最终版本编译 exit 0，无 Warning、Overfull、Underfull 或 undefined 条目。
目录与交叉引用已稳定；pypdf 检查全部页面为 A4，提取文本无 `??`。
附录复现命令提取为 `python scripts/hybrid_free_b_geometry_exact_audit.py`，保留必要空格。
PDF raw 哈希只绑定交付字节；重建时编译时间等元数据可能改变字节哈希。

## 3. 全页目视验收

以 Poppler `pdftoppm -r 96 -png` 渲染全部 12 页；逐页目视检查排版、完整公式、
表格跨页、目录和页码、引用与边距，未发现裁切、覆盖、黑方块或不可读字形。
最后修复附录命令因 nolinkurl 丢空格的排版问题，再以 110 dpi 检查第 11 页。
最终 PDF 再次全页渲染：第 1–10、12 页与已验收版本像素完全相同，
第 11 页只有预期命令格式差异；其最终版再次目视通过。

中间渲染文件位于 `tmp/pdfs/free-b-paper-qa/`，交付后清理，不纳入版本管理。

## 4. 复现证据与保留记录

[自由 b 精确审计](../../output/hybrid-free-b-geometry-exact-audit.json)
由[脚本](../../scripts/hybrid_free_b_geometry_exact_audit.py)重跑得 PASS，841 项检查，
包括 189 个直接模型；它仅验证 Q 与 Q(√921) 中显示代数及有限模型。
连续不等式以正文完成平方和系数正性证明，不由有限网格推断；
外部解析输入、素数估计、无穷轮廓及 kernel 不由该脚本认证。

目录检查及已有 `scripts/test_repo_layout.py` 的 12 项回归全部通过。
公开 README 保持项目介绍，仅增加第五稿的出版入口；原阶段记录仍在历史目录。
旧 69999/80000 论文和 PDF 没有重编译或改写，其哈希保持已交付版本：
TeX `92ba93da7cc568579b0b982bcd712e1382af749d05460c1fa4c8b25064df66d6`；
PDF `1604c74dfa37ab576ea8d861604cffa49bb7611c79d34d5d46234d7097d8673f`。
外部 `E:\codex-build\math` 始终只读，最终 commit 与 canonical 源哈希再次核对，工作区干净。

最终文件、独立审查、输入版本和本记录的哈希见
[构建清单](free-b-paper-build-manifest.json)。
