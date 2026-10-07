# 三次反馈新论文：编译、版面与证据封存

2026-10-07，root。该记录仅验证产物与布局，数学范围以两份全文审查为准。

最终源稿 papers/kappa-feedback-cubic-boundary-paper.tex：
canonical LF SHA-256
16c0ba50a2917f2ead56843eabf55b62fbbe214e162cff373b4d8554f84315ee，
39,181 UTF-8 bytes，990行，单个EOF换行。
最终 PDF output/pdf/kappa-feedback-cubic-boundary-paper.pdf：
raw SHA-256
791b20f83db7223c75ba9a3ea54611cdc9e89b12831685c004507edabeade6a6，
447,816 bytes，13页，全部A4（595.276×841.89 PDF points）。

## 编译与修订

已请求在内置LaTeX编辑器打开同一源稿；一次内置编译返回环境错误
“Unable to find standard directories for platform”。该错误不确认编译成功。
保持源稿编辑入口，改用已安装MiKTeX pdfLaTeX 1.40.25（MiKTeX 23.5），
未安装TeX、插件或其他依赖。

第一次fallback编译发现审计命令放在math display中的源错误，已改为普通
center环境；长数字与几何公式改为分行。随后消除长URL的Underfull warning，
使参考文献独页、目录完整一页；所有引用稳定后再按数学审查补明
Proposition的逐槽max_i z_i≤η_mesh前件并同步PDF。
最后版本命令从仓库根执行：

~~~
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf papers/kappa-feedback-cubic-boundary-paper.tex
~~~

最后两次编译成功，exit 0；最终log无Overfull、Underfull、Warning、
undefined或Error，引用无需重跑。共8次fallback执行，其中第一次有源错误；
之后各次用于上述修订和必要的引用稳定，没有编译旧论文。

## 全页视觉与文件检查

用pdftoppm -r 96 -png渲染全部13页，逐页检查版面、公式、表格、换页和页码。
审查修订后的最终图像中1、2、3、12、13页与初次完整QA发生变化，重新检查；
4至11页最终pixels与已检查版本完全一致。
目录的附录条目留在第一页，参考文献整体在第13页；表头与长公式无裁剪，
无黑方块、覆盖或不可读符号。第12页的python审计命令有真实空格。
PDF文本提取无“??”；counted checks和fixed metadata说明已出现在最终PDF中。
渲染中间件仅用于QA，不作为论文附件。

新稿数学审查：
[radial全文](kappa-feedback-paper-review-radial.md)、
[twisted全文](kappa-feedback-paper-review-twisted.md)，均绑定上述最终TeX；
[独立有限公式审查](kappa-feedback-paper-exact-review-joint.md)另行限定。
最终声明仍为 [T/R]，没有由编译、图像或脚本取得外部kernel或RH认证。

## 导航、保留和后续工作

公开README仅增加新论文导航与统一范围说明；细节放入notes/reviews/goals。
papers目录登记第六篇论文，check_repo_layout的PAPERS元组同步；
现有12项目录回归测试和实际目录检查均通过，无新增镜像式测试。
精确脚本此前149个计数检查已由完整数学审查者分别重跑；
49模型的98次恒等式检查不替代连续系数正性证明。
脚本source SHA字段是固定metadata；实际源绑定由完整审查及清单另行核对。

两篇已交付无零边界源/PDF、README历史快照逐个核对原哈希，全部一致。
外部math工作区实际HEAD与固定commit一致、状态干净，只读且未编译。
最终构建清单与新研究检查点绑定本轮材料；冻结研究草稿中原有待审措辞
由本轮实际审查和该检查点的最终状态承接，草稿不作追溯修改。
Goal active；没有新临界线比例，下一步按实际临界邻域与物理四阶任务执行。
