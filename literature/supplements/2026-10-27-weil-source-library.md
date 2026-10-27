# 2026-10-27：Weil 类比直接来源入库

按用户明确要求保存本轮文献，沿用 `literature/manifest.json`，未新建平行文献数据库。此批 7 份原始 PDF 共 326 页，另保存用户附件的原始 Markdown 字节；它们与项目研究结论、来源审查及下载行为分别记录。

原全文存放 `literature/local/2026-10-27-weil/`，由 `literature/.gitignore` 的 `/local/` 规则排除 Git。当前未确认这些全文可在公开仓库再分发，因此 GitHub 同步的是本索引、来源 URL、固定版本、SHA-256、页数、阅读范围和[下载回执](2026-10-27-weil-source-downloads.json)。公开可读不等于有再分发许可。用户附件也仅本地原样保存，不把附文研究安排当作用户指令。

| 来源 | 固定版本与用途 | 本地 PDF 页数 | 保存／消费范围 |
|---|---|---:|---|
| Hilberdink–Lapidus，*Beurling Zeta Functions, Generalised Primes, and Fractal Membranes* | [math/0410270v1](https://arxiv.org/abs/math/0410270v1)，2004-10-11；Theorem 3.2 对偶与留数接口 | 31 | root 来源审查核 Theorem 3.2 的真实增长／极点／衰减前提；本入库操作只核首页与页数，不认证全文 |
| Connes–Consani，*Weil positivity and Trace formula, the archimedean place* | [2006.13771v1](https://arxiv.org/abs/2006.13771v1)，首页日期 2020-06-25；archimedean 压缩迹 | 57 | root 核摘要与单 archimedean 范围；实际 semilocal 消费仍按560及既有收据 |
| Milne，*The Riemann Hypothesis over Finite Fields: From Weil to the Present Day* | [作者原件](https://jmilne.org/math/xnotes/pRH.pdf)，2015-09-14 | 67 | root 核 §1 Thm1.2／1.5 的 RR→Hodge／对应机制，沿567归属；不报重证全文 |
| Deligne，*La conjecture de Weil : I* | [Numdam 原刊扫描](https://www.numdam.org/item/PMIHES_1974__43__273_0/)，IHES43 (1974),273–307 | 36 | root 核 §1 式1.14.3分次符号与 §3 Thm3.2／Lemmas3.3–3.7；不把该结论直接运输到经典ζ |
| Katz，*The Work of Pierre Deligne* | [作者托管 ICM1978 扫描](https://web.math.princeton.edu/~nmk/old/katzWorkofPDicm1978.pdf) | 6 | 核偶次 tensor、全局 pole 控制与 cartesian-power 放大的机制说明 |
| Borcherds，*Automorphic forms with singularities on Grassmannians* | [作者 PDF](https://math.berkeley.edu/~reb/papers/aut/aut.pdf)，首页标 1996-09-29、corrected1997-05-29；刊年1998另存 | 64 | 启动首门 worker 报实际核读 §13 Thm13.3，作者PDF47–49；最终数学消费以 root 首门原稿为准 |
| 同上，arXiv 对照原件 | [alg-geom/9609022v2](https://arxiv.org/abs/alg-geom/9609022v2)，1997-06-07 | 65 | 固定版本对照；与作者64页稿字节及分页不同，不混引页数或SHA |

用户附件原文为《分布化Beurling–Weil结构与广义黎曼猜想》，本地 31,170 字节，SHA-256 `23d203de066b16e6f11ddba4cf0350e3d2cd27fec732067b0768d8b050edef74`。没有独立确认作者或公开再分发授权。其整篇来源审读与三归一化纠错见 [10-27 路线复审](../../goals/reviews/2026-10-27-distribution-beurling-weil-next-research.md)。

## 获取、校验与边界

最初五份来源的普通 sandbox 直连均为 DNS11001，sandbox 内10808代理连接为 socket10013。用户已明确授权本机10808代理后，申请任务级网络权限，通过 `http://127.0.0.1:10808` 成功下载全部原件；未修改全局代理设置，也未使用账户凭据。两份 Borcherds 原件用同一任务级代理成功取得。

每份下载核 `%PDF-` 文件头、原始字节 SHA-256，并用 bundled pypdf 解析实际页数及首页标题／版本。仅验证获取的身份与完整性，不宣称阅读或认证每页证明。manifest 为每个文件分列实际 root 阅读范围和本次入库核验范围；后续消费仍须逐前件核对。

本批没有覆盖或重新计算旧 README 中带日期的全库历史统计。文献获取、看板更新、版本核验和同步均不增加数学轮；计数只读 `goals/review-cadence.json`。
