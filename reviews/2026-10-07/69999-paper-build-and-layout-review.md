# 69999/80000 正式论文构建与版面复核

2026-10-07。对象为 papers/seven-eighths-boundary-improvement-paper.tex
及 output/pdf/seven-eighths-boundary-improvement-paper.pdf。

结论：**构建与版面 PASS**。最终 13 页、A4、13 页全部渲染检查完成。
数学内容由两份独立全文审查限定为引用输入包 R 下的推导；
此记录只认证下述实际构建、版面与可复现检查，不新增分析定理或 Lean 认证。

## 编译与版本

首先打开源文件至 Codex 内置 LaTeX 编辑器并调用内置编译器。
该编译器返回 “Unable to find standard directories for platform”；
这是平台配置错误，没有据此声称编译成功，也未安装新工具或修改外部 math 仓库。

随后使用已安装的 MiKTeX pdfLaTeX 编译并导出仓库 PDF。
源错误与初稿版面问题修复后，对最终冻结源进行了两次成功编译，
退出码均为 0，最终日志没有 Overfull、Underfull、Warning 或未定义引用。
最后一次稳定编译生成的源／PDF 哈希见同目录构建清单。

从仓库根目录复现：

    pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf papers/seven-eighths-boundary-improvement-paper.tex
    pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf papers/seven-eighths-boundary-improvement-paper.tex

PDF 的日期和编译器元数据可能因重建改变字节哈希；源文件的数学内容
及 canonical LF 哈希为审查绑定对象。未重编译其他三篇论文。

## 版面和正文

用 pdftoppm -r 100 -png 渲染最终全部 13 页至专用
tmp/pdfs/69999-paper-qa/。先检查全部页面缩略图，再单独放大
low 核心计算、连续证书、Mellin 收束与附录／参考文献页面。
最后的附录独立分页调整后重新渲染并检查。

实际确认：

- 正文、公式、页码、表格和参考文献没有裁切、重叠或越出页边。
- 输入表跨页重复表头，长标签、源码路径与哈希正确换行。
- 主定理、几何、有理数余量与连续恒等式可读，公式编号可点击。
- 13 页均有正文；没有空白页或丢失字符的可见占位符。
- PDF 文本提取为 13 页，未发现未解析引用 “??”。
- 验证附录与参考文献同页，明确 finite audit 和外部输入的认证范围。

## 其他实际检查

python scripts/hybrid_high_continuation_exact_audit.py 成功退出：
连续 completed-square 身份的 12 个非零系数精确匹配，
16,728 个有限频率分配案例通过；新边界、central、floor、
中间与外小行余量及参考幂账本一致。脚本只认证显示代数及有限模型。

python scripts/check_repo_layout.py 通过；
已有 scripts/test_repo_layout.py 的 12 个回归用例全部通过。
检查新增论文文件和迁移后的历史 README 的论文引用；
完整 README 还原、572 个本地链接的另外复核见
[迁移记录](readme-history-migration-review.md)。

未采用 447 或后续更强参数结果。正式论文严格整理用户指定的
69999/80000 成果，条件、外部依赖和 principal pole 例外均保留。
