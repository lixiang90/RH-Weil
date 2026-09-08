# 后续输入筛查：多窗谱传递与方法上限

2026-09-08。周期9后续方向的来源准备，不另报新零点纪录。
Alpöge–Furman与Lamzouri的当前arXiv页面仍分别列v2（2026-08-19）、
v1（2026-09-02）；未发现这两个版本页上的更新。
这不是对所有新文献的穷尽检索。

## 多窗非线性谱传递

Devine v1.0.3原18页PDF已在既有文献库，当前重新核读第1–8页。
第7–8页Proposition1把平稳二次pair能量接到截断凸谱余项，
用到了有限块分支保护及最小混合权。
主线程尚未恢复其所需块规模、局部亏损及跨块容量的完整定量链，
所以67.3399%仍为待审来源，不直接导入新研究。
这是一项明确待核查的传递接口，当前没有证明其错误。

公开包入口仍列在[固定Zenodo记录](https://zenodo.org/records/22066689)。
下载页与API内容入口本次均HTTP403，见
[获取记录](devine-public-package-download.json)；
网页可读随包SHA256为
26de675e8362d2fad02433797dc1f5ba79f9d8d11d9f51410b6257f878889f94。
未取得压缩包，未运行其中证书，不能将网页哈希作为已保存原件。
该获取失败不阻塞独立的有限谱传递研究，也不影响已归档PDF。

下一有限问题可直接研究加权多个tr Psi(K_j)，而不是先平均K再取Psi；
若使用平稳pair下界，必须另证明其到非线性谱余项的传递。
只证明经典对偶公式、只增加块数或重放旧常数，均不足以获得新实际比例。

## 带宽一上限附件的复现边界

Hydra的[作者记录](https://www.hydradynamix.com/blog/a-tighter-ceiling)
讨论方法上限；它不提高实际简单零点比例下界。
固定[仓库提交](https://github.com/hydra-dynamix/zeta23-verification/tree/3c1d0ef81bf3af689d699ceefa9dc984a1dedb93)
已由ls-remote核定。技术说明、README、原始law、Python检查器及LICENSE/NOTICE
六份原件已归档，详情见[下载记录](hydra-source-downloads.json)。

主线程已读NOTE的§1–4及§5开头、完整4045字节检查器，并运行原样检查器：
输出保存于[日志](hydra-row-verifier-output.txt)。
这次执行只检查给定整数区间的行不等式、正的p及一个边缘上端。
代码没有从位置／标记／混合权重新构造Fourier区间，
也没有验证p与支持权表的关系；部分文档所列数值一致性只打印而不作断言。
因此日志的PASS只按实际代码范围解释，不能称为本项目已独立重建完整见证。
未编译Lean、未审区间生成器或主定理全部依赖，亦未据此否定原见证本身。
