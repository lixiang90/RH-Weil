# RH-Weil 文献索引

更新与抓取日期：2026-09-06。首批归档聚焦67.25%之后的零点比例进展及直接依赖（15份、220页）；GOAL 首周期补入两份 Milne 函数域背景及四篇 Abel 直接文献，phase1共21份外部原始PDF、570页；phase2新增清单及获取状态见文末，phase3新增Schur原文扫描29页，持续GOAL周期4新增GM、TTY和ANTEDB共286页，当前本地共32份外部原始PDF、1076页，其中Git保存31份、1047页；Schur扫描按来源封面要求仅本地保存，出处和哈希同步。获取失败单列。研究判断见 [305文献审计](../notes/305-post-6725-literature-baseline-audit.md)。

PDF按来源原样保存，未重排或改写；arXiv固定版本，GitHub固定提交，Zenodo固定记录。下载、全页PDF解析和校验值核验不等于数学证明认证。manifest中的SHA-256标识本次取得的精确字节，原站同一文件名后续变化时仍可区分。

## 快速定位

- 基础证明：AF-2026；直接Hilbert短证：Lamzouri-2026。
- 67.3%的直接出处：ainta-2026（67.3008527928%）。
- 后续候选：Shi-2026（67.3316977142%）；Devine-2026-v3（声称67.3399%）。
- trmdy归档PDF仍是67.3200117013%七点稿；最新67.3312742272%保存在[九点补充文档](supplements/trmdy-nine-point-1610b97.md)。不要把仓库README最新数值误标成PDF正文的主定理。
- 条件性67.92%：Devine-2026-box；高矩待审主张：Yang-2026-7962。

## 论文列表

### 基础比例证明

**AF-2026 — More than two thirds of the zeta zeros are simple and on the critical line**

- 作者：Alpöge; Furman。
- 版本：arXiv:2608.13637v2; 2026-08-19。
- [本地PDF](baseline/2026-alpoge-furman-6725-v2.pdf)（21页，478,663字节）；[来源页面](https://arxiv.org/abs/2608.13637v2)；[原始PDF链接](https://arxiv.org/pdf/2608.13637v2)。
- 状态与用途：外部预印本基线；约67.25%。

**Claude-2026 — More than two thirds of the zeros of the Riemann zeta function lie on the critical line**

- 作者：Claude / Anthropic。
- 版本：Anthropic 固定内容 URL；抓取日2026-09-06。
- [本地PDF](baseline/2026-claude-anthropic-zeta-23.pdf)（35页，631,785字节）；[来源页面](https://www.anthropic.com/research/riemann-zeta)；[原始PDF链接](https://www-cdn.anthropic.com/564f962e60643842f5fcb4a17c9dbc8f608f1c37.pdf)。
- 状态与用途：原始研究稿及证明框架；另见AF修订预印本。

**Lamzouri-2026 — A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line**

- 作者：Youness Lamzouri。
- 版本：arXiv:2609.02882v1; 2026-09-02。
- [本地PDF](baseline/2026-lamzouri-6725-hilbert-v1.pdf)（14页，505,955字节）；[来源页面](https://arxiv.org/abs/2609.02882v1)；[原始PDF链接](https://arxiv.org/pdf/2609.02882v1)。
- 状态与用途：新的Hilbert空间短证；仍为67.25%。

### 配对相关与方法背景

**BGST-2023 — An unconditional Montgomery Theorem for Pair Correlation of Zeros of the Riemann Zeta Function**

- 作者：Baluyot; Goldston; Suriajaya; Turnage-Butterbaugh。
- 版本：arXiv:2306.04799v1; 2023-06-07; Acta Arith. 214 (2024),357-376。
- [本地PDF](background/2023-bgst-unconditional-montgomery-v1.pdf)（13页，210,602字节）；[来源页面](https://arxiv.org/abs/2306.04799v1)；[原始PDF链接](https://arxiv.org/pdf/2306.04799v1)。
- 状态与用途：全零点相关输入；勘误须结合BGST-2025v3。

**BGST-2025 — Pair Correlation of Zeros of the Riemann Zeta Function I: Proportions of Simple Zeros and Critical Zeros**

- 作者：Baluyot; Goldston; Suriajaya; Turnage-Butterbaugh。
- 版本：arXiv:2501.14545v3; 2026-09-01。
- [本地PDF](background/2025-bgst-pair-correlation-I-v3.pdf)（16页，376,884字节）；[来源页面](https://arxiv.org/abs/2501.14545v3)；[原始PDF链接](https://arxiv.org/pdf/2501.14545v3)。
- 状态与用途：窄箱条件比例及相关公式修订；不能把条件比例当无条件。

**GS-2025 — Zeta Zeros on the Critical Line**

- 作者：Daniel A. Goldston; Ade Irma Suriajaya。
- 版本：arXiv:2511.20059v2; 2026-02-05。
- [本地PDF](background/2025-goldston-suriajaya-critical-line-v2.pdf)（9页，345,194字节）；[来源页面](https://arxiv.org/abs/2511.20059v2)；[原始PDF链接](https://arxiv.org/pdf/2511.20059v2)。
- 状态与用途：解释移除RH假设与简单临界线计数的关系。

**CGdL-2019 — Pair Correlation Estimates for the Zeros of the Zeta Function via Semidefinite Programming**

- 作者：Andrés Chirre; Felipe Gonçalves; David de Laat。
- 版本：arXiv:1810.08843v2; 2019-11-18。
- [本地PDF](background/2019-chirre-goncalves-delaat-sdp-v2.pdf)（16页，264,978字节）；[来源页面](https://arxiv.org/abs/1810.08843v2)；[原始PDF链接](https://arxiv.org/pdf/1810.08843v2)。
- 状态与用途：SDP配对相关背景；适用假设须逐项保留。

### 后续研究稿：须核对证明与认证范围

**ainta-2026 — More than 67.3% of the zeros of the Riemann zeta function are simple and lie on the critical line**

- 作者：ainta；仓库披露由GPT-5.6 Sol生成。
- 版本：commit 040c5e899e658aed7b56a2a87f501798fe10761d; 2026-08-11。
- [本地PDF](candidates/2026-ainta-6730085-040c5e8.pdf)（7页，86,065字节）；[来源页面](https://github.com/ainta/zeta-simple-zeros/tree/040c5e899e658aed7b56a2a87f501798fe10761d)；[原始PDF链接](https://raw.githubusercontent.com/ainta/zeta-simple-zeros/040c5e899e658aed7b56a2a87f501798fe10761d/paper/riemann.pdf)。
- 状态与用途：67.3008527928%研究草稿；正文推导与常数核查，未重跑七点证书。

**trmdy-2026 — A certified 67.32001% lower-bound candidate for simple zeros of the Riemann zeta function on the critical line**

- 作者：Vivaswat Ojha（归档PDF作者）；trmdy仓库维护者Tormod Haugland。
- 版本：commit 1610b97b7895ff34982260f8dcaf04a0f7b82cf7; 2026-08-12。
- [本地PDF](candidates/2026-trmdy-stability-1610b97.pdf)（6页，274,200字节）；[来源页面](https://github.com/trmdy/zeta-simple-zeros-673137/tree/1610b97b7895ff34982260f8dcaf04a0f7b82cf7)；[原始PDF链接](https://raw.githubusercontent.com/trmdy/zeta-simple-zeros-673137/1610b97b7895ff34982260f8dcaf04a0f7b82cf7/paper/main.pdf)。
- 状态与用途：本PDF为67.3200117013%七点稿（2026-08-11）；仓库最新67.3312742272%在另存九点补充文档中；两者均未获本项目完整认证。

**Shi-2026 — A two-certificate trace-energy deduction for simple zeros of the Riemann zeta function**

- 作者：Yuhang Shi。
- 版本：稿件2026-08-14; commit 7cfd0ce9a9ef1615889b5c1191fac5de41f13960 (2026-08-28)。
- [本地PDF](candidates/2026-shi-673316977-7cfd0ce.pdf)（7页，101,992字节）；[来源页面](https://github.com/yuhangshi888/zeta-simple-zeros-673316977/tree/7cfd0ce9a9ef1615889b5c1191fac5de41f13960)；[原始PDF链接](https://raw.githubusercontent.com/yuhangshi888/zeta-simple-zeros-673316977/7cfd0ce9a9ef1615889b5c1191fac5de41f13960/main.pdf)。
- 状态与用途：67.3316977142%候选；仅新增推导局部Lean化，上游接口与证书仍导入。

**Tawan-2026 — Certified unconditional 67.3192911473% lower bound for simple zeros of the Riemann zeta function**

- 作者：tawanerguo-cn。
- 版本：commit 45149f6d403059a71be73c5e3f884cee7cd62b20; 2026-08-11; PDF日期2026-08-12。
- [本地PDF](candidates/2026-tawan-bellman-6731929-45149f6.pdf)（6页，80,852字节）；[来源页面](https://github.com/tawanerguo-cn/zeta-simple-zeros/tree/45149f6d403059a71be73c5e3f884cee7cd62b20)；[原始PDF链接](https://raw.githubusercontent.com/tawanerguo-cn/zeta-simple-zeros/45149f6d403059a71be73c5e3f884cee7cd62b20/paper/riemann.pdf)。
- 状态与用途：Bellman修正候选；仓库自述外部同行评审未完成。

**npip-2026 — More than 67.3195% of the zeros of the Riemann zeta function are simple and lie on the critical line**

- 作者：Nicholas Pipitone。
- 版本：commit 72a01ac5ea3837f2a4c4583d831f885d005f8af1; 2026-08-12。
- [本地PDF](candidates/2026-npip-673195-72a01ac.pdf)（7页，106,135字节）；[来源页面](https://github.com/npip99/zeta-zeros/tree/72a01ac5ea3837f2a4c4583d831f885d005f8af1)；[原始PDF链接](https://raw.githubusercontent.com/npip99/zeta-zeros/72a01ac5ea3837f2a4c4583d831f885d005f8af1/paper/main.pdf)。
- 状态与用途：67.3195198901%；Lean结论仍有局部七点搜索证书前提。

**Devine-2026-v3 — An Unconditional 67.3399% Bound and Conditional Advances Beyond 67.92% for Simple Critical Zeros of the Riemann Zeta Function**

- 作者：Michael Devine。
- 版本：Zenodo 22066689; version1.0.3; 2026-08-23。
- [本地PDF](candidates/2026-devine-673399-v1.0.3.pdf)（18页，455,218字节）；[来源页面](https://zenodo.org/records/22066689)；[原始PDF链接](https://zenodo.org/records/22066689/files/zeros-v3.pdf?download=1)。
- 状态与用途：作者声称无条件67.3399%；PDF第1、7页说明完整形式化可重放数值包仍在准备；本项目未复核全部解析链和243域证书。

### 明确附加数学假设的结果

**Devine-2026-box — A 67.92% Bound for Simple Critical Zeros in a Vanishing Vertical Box**

- 作者：Michael Devine。
- 版本：Zenodo 21879591; version1.0.0; 2026-08-10。
- [本地PDF](conditional/2026-devine-6792-conditional-box-v1.pdf)（7页，250,094字节）；[来源页面](https://zenodo.org/records/21879591)；[原始PDF链接](https://zenodo.org/records/21879591/files/vanishing_box_simple_zeros.pdf?download=1)。
- 状态与用途：67.92%明确依赖消失窄箱假设；非无条件纪录。

### 尚未核查解析链的高比例主张

**Yang-2026-7962 — More than 79.62% of the zeros of the Riemann zeta function are simple and on the critical line**

- 作者：Yang Hongyi; Yang Shihua。
- 版本：Zenodo21975237; version1.0; 2026-08-17。
- [本地PDF](unreviewed/2026-yang-7962-unreviewed-v1.pdf)（38页，598,532字节）；[来源页面](https://zenodo.org/records/21975237)；[原始PDF链接](https://zenodo.org/records/21975237/files/More%20than%200.7962%20on%20the%20critical%20line-EN.pdf?download=1)。
- 状态与用途：仅归档待审声明；解析高矩链未核查，不导入MOM-1。

## 补充材料与只登记链接的文献

补充文件按固定提交原样归档，其中原有相对链接按上游仓库目录解释；需要跳转时使用下列“固定版本原文”链接。

- [trmdy-nine-point-1610b97.md](supplements/trmdy-nine-point-1610b97.md) — [固定版本原文](https://github.com/trmdy/zeta-simple-zeros-673137/blob/1610b97b7895ff34982260f8dcaf04a0f7b82cf7/docs/nine-point.md)。
- [trmdy-seven-point-1610b97.json](supplements/trmdy-seven-point-1610b97.json) — [固定版本原文](https://github.com/trmdy/zeta-simple-zeros-673137/blob/1610b97b7895ff34982260f8dcaf04a0f7b82cf7/data/candidate-retuned-p2736.json)。
- [trmdy-nine-point-final-1610b97.json](supplements/trmdy-nine-point-final-1610b97.json) — [固定版本原文](https://github.com/trmdy/zeta-simple-zeros-673137/blob/1610b97b7895ff34982260f8dcaf04a0f7b82cf7/data/candidate-nine-point-final.json)。
- [trmdy-nine-point-log-1610b97.txt](supplements/trmdy-nine-point-log-1610b97.txt) — [固定版本原文](https://github.com/trmdy/zeta-simple-zeros-673137/blob/1610b97b7895ff34982260f8dcaf04a0f7b82cf7/certificates/nine-point-final-grid4000.txt)。
- [shi-claim-ledger-7cfd0ce.md](supplements/shi-claim-ledger-7cfd0ce.md) — [固定版本原文](https://github.com/yuhangshi888/zeta-simple-zeros-673316977/blob/7cfd0ce9a9ef1615889b5c1191fac5de41f13960/CLAIM_LEDGER.md)。

- [Shi v0.1.0正式存档（Zenodo）](https://doi.org/10.5281/zenodo.21926962)：本目录PDF采用上述较新固定Git提交；发布存档与后续Lean材料的版本不要混用。
- [Yang–Yang 密度1稿件](https://zenodo.org/records/22065921)：记录处于封存状态，作者注明“版本内容有错误，需要重新修订”。仅保存链接与状态，不取得被封存附件，也不纳入数学基线。此状态不自动判定其较早79.62%稿件的对错。
- [Hydra Dynamix带宽一方法上限](https://github.com/hydra-dynamix/zeta23-verification/tree/3c1d0ef81bf3af689d699ceefa9dc984a1dedb93)：[作者说明](https://www.hydradynamix.com/blog/a-tighter-ceiling)。0.681810782为特定方法类的上限证人，不是实际零点比例的新下界；本轮未独立复算。
- [Lamzouri 2026-09-03 MPIM报告](https://math-events.uni-bonn.de/event/1560/)：新短证的学术报告来源，内容仍为67.25%。

## 文件校验

完整元数据、解析状态、抓取时间与重定向后的地址见 [manifest.json](manifest.json)。以下为PDF的SHA-256：

| ID | SHA-256 |
|---|---|
| AF-2026 | `6de3b156342e7b4a802c34f8ef40432567e9dabe006938da04233f19fc4ef444` |
| Claude-2026 | `6792988e6cd0e17690621ce898abd5d534f98407741bc7cb14bbe7d07c77d72f` |
| Lamzouri-2026 | `fa33485f517b3c94d2f6e4d4366f3ab14a1e413a738db512e1862f4a0944f5f9` |
| BGST-2023 | `133071c4d85c875fe9b1a7d4001f22d7174270ab8f1fa8e6cee6178d20276ee9` |
| BGST-2025 | `0a16b0b0f19b06490111e048a6841f4fe68717c546fae4cb7a44555dc0f96cb3` |
| GS-2025 | `7b4f638cbd0438123b7a54869fc998fc3d4dee9b74572c04cef9da0463ed4c6f` |
| CGdL-2019 | `1f39a719a01801939740fb3647f2a7aa848fc7ee1587f3b40e9236caf304a035` |
| ainta-2026 | `d846f3a73cf3ab012d7c16be78c5bab35fcd5d2b1d99db5bf036bd638a277afc` |
| trmdy-2026 | `7b45f2f8336816aeae4bd4c74bfc6d32c12181f5a3149c03d61c5efa8d2ff825` |
| Shi-2026 | `d463edc46466f101963c918e9e14001097de810ed791f5944ee6105989e020bd` |
| Tawan-2026 | `bbe10cfaa3e8bb3a654acb4cc6a072f1066e2639501b7e83b5f9a6b3ea046c08` |
| npip-2026 | `0132ffc9a65d5b4caecc1e7ae45aa505bd51955cd0b24ab3f86375878be59e2e` |
| Devine-2026-v3 | `4abe6b7281697833d1e207d587ac0346a080eade7585691da6897e01283d8cbd` |
| Devine-2026-box | `afbef3b6c8d61c6e0345a19ab8b6906b4e65d8bd1a0fcd0b728b7b78eb486c2e` |
| Yang-2026-7962 | `0abaa78e0eb4421fdbae647a0b3b6b0299a4dde5d49b0e56ca6f33831c5e3ea0` |

## 后续维护

新增论文时保留作者、准确标题、发布日期、版本/提交、来源页、直链、本地文件与核查边界。不同版本使用不同文件名；源文件发生修订时更新清单和哈希，保留历史对照。引用补充文档中的新结果时，不用较早PDF代替该证明来源。原始论文版权与许可归原作者/来源方，项目自己的论文仍放在 papers/ 与 output/pdf/。

### 函数域模型与极化背景（GOAL 首周期）

**Milne-EC-2021 — Elliptic Curves**

- 作者：J. S. Milne；版本：Second edition, World Scientific, 2021; author-hosted PDF captured 2026-09-06。
- [本地PDF](background/milne-elliptic-curves-second-edition.pdf)（241页）；[作者来源与PDF](https://www.jmilne.org/math/Books/EC2.pdf)。
- 状态与用途：核读 II.6.1–6.2、IV.9.1、9.4 的次数与可分核接口；经典椭圆曲线基准。对应[307 模型基准](../notes/307-odd-polarization-and-elliptic-degree-benchmark.md)。

**Milne-AV-2022 — Abelian Varieties**

- 作者：J. S. Milne；版本：Author revised file dated January 2, 2022; original chapter 1986; captured 2026-09-06。
- [本地PDF](background/milne-abelian-varieties.pdf)（49页）；[作者来源与PDF](https://www.jmilne.org/math/xnotes/AVs.pdf)。
- 状态与用途：核读 §17 正性与 §19 Frobenius 接口；一般 Rosati 背景，不认证全文。对应[307 模型基准](../notes/307-odd-polarization-and-elliptic-degree-benchmark.md)。

## Abel 障碍稿直接文献（2026-09-06）

| 文献／版本 | 本地 PDF | 原始来源 | 核查范围 |
|---|---|---|---|
| Erdős，1932，Beweis eines Satzes von Tschebyschef | [PDF](background/erdos-1932-bertrand.pdf) | [作者档案](https://users.renyi.hu/~p_erdos/1932-01.pdf) | Bertrand 定理；5 页扫描可读 |
| Mahatab–Mukhopadhyay，1512.03144v4，2018-07-26 | [PDF](background/mahatab-mukhopadhyay-oscillations-v4.pdf) | [arXiv 固定版](https://arxiv.org/abs/1512.03144v4) | Theorem 3.1 与 Landau 方法；19 页 |
| Montgomery–Vaughan，Hilbert’s inequality，1974 | [PDF](background/montgomery-vaughan-hilbert-1974.pdf) | [作者档案](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf) | 局部间距不等式与均值应用；10 页 |
| Fiori–Kadiri–Swidinsky，2204.02588v3，2023-05-17 | [PDF](background/fiori-kadiri-swidinsky-psi-v3.pdf) | [arXiv 固定版](https://arxiv.org/abs/2204.02588v3) | Corollary 1.4 无条件 PNT 及常数 0.8476836；26 页 |
| Hardy，Sur les zéros de la fonction ζ(s) de Riemann，1914，158:1012–1014 | 全文 PDF 获取未成功 | [BnF 原刊页](https://gallica.bnf.fr/ark:/12148/bpt6k3111d/f1014)；[原卷档案](https://archive.org/details/ComptesRendusAcademieDesSciences0158) | 2026-09-06 BnF 网页／三页 PDF 均返回 403；保留来源，不能记为已下载 |

四份新增 PDF 共 60 页，均已逐页解析；哈希、字节数、抓取时间及标题见 manifest.json。
现共保存 21 份 PDF、570 页。下载与解析不等于完整证明认证。

## phase 2：正则化、插值及密度原始文献

2026-09-06当前轮补存6份原始PDF、158页；Landau和Anderson–Trapp获取失败，来源照常索引。

**deBoor-2005 — Divided Differences**

- 作者：Carl de Boor。
- 版本：Surveys in Approximation Theory 1 (2005), 46–69; manuscript dated 2004-12-21。
- [本地PDF](background/deboor-divided-differences-2005.pdf)（24页）；[来源页](https://pages.cs.wisc.edu/~deboor/sat/papers/2/2.pdf)；[原始PDF入口](https://pages.cs.wisc.edu/~deboor/sat/papers/2/2.pdf)。
- 获取：downloaded。
- 核读范围：302/303 插值余项直接背景；核读 §9 Genocchi–Hermite 公式。

**Douglas-1966 — On majorization, factorization, and range inclusion of operators on Hilbert space**

- 作者：R. G. Douglas。
- 版本：Proc. AMS 17 (1966), 413–415; DOI 10.1090/S0002-9939-1966-0203464-1。
- [本地PDF](background/douglas-factorization-1966.pdf)（3页）；[来源页](https://doi.org/10.1090/S0002-9939-1966-0203464-1)；[原始PDF入口](https://home.agh.edu.pl/~rudol/Operat/DouglasFactorizationLemma.pdf)。
- 获取：downloaded。
- 核读范围：核读 Theorem 1 及不同定义域推广；310 收缩因子条件的经典背景。

**Tikhonov-1963 — On the solution of ill-posed problems and the method of regularization**

- 作者：A. N. Tikhonov。
- 版本：Dokl. AN SSSR 151(3) (1963), 501–504; Russian original。
- [本地PDF](background/tikhonov-regularization-1963.pdf)（4页）；[来源页](https://www.mathnet.ru/eng/dan28329)；[原始PDF入口](https://www.mathnet.ru/php/getFT.phtml?jrnid=dan&option_lang=eng&paperid=28329&what=fullt)。
- 获取：downloaded。
- 核读范围：独立复核者核读 p.502 式(2)；310 有限矩阵恒等式另行自含推导。

**Birman-1961 — On the spectrum of singular boundary-value problems**

- 作者：M. Sh. Birman。
- 版本：Mat. Sb. 55(97)(2) (1961), 125–174; Russian original。
- [本地PDF](background/birman-singular-spectrum-1961.pdf)（50页）；[来源页](https://www.mathnet.ru/eng/sm4754)；[原始PDF入口](https://www.mathnet.ru/php/getFT.phtml?jrnid=sm&option_lang=eng&paperid=4754&what=fullt)。
- 获取：downloaded。
- 核读范围：独立复核者核读 §1.5 p.132 Lemma 1.1；只作负谱阈值计数背景。

**BTEG-2020 — The Generalized Birman-Schwinger Principle**

- 作者：J. Behrndt; A. F. M. ter Elst; F. Gesztesy。
- 版本：arXiv:2005.01195v4; 2020-08-11。
- [本地PDF](background/behrndt-terelst-gesztesy-birman-schwinger-v4.pdf)（45页）；[来源页](https://arxiv.org/abs/2005.01195v4)；[原始PDF入口](https://arxiv.org/pdf/2005.01195v4)。
- 获取：downloaded。
- 核读范围：补充背景；本轮未审查广义非自伴定理，310 不依赖其全部推广。

**Landau-1967 — Necessary density conditions for sampling and interpolation of certain entire functions**

- 作者：H. J. Landau。
- 版本：Acta Math. 117 (1967), 37–52; DOI 10.1007/BF02395039。
- [来源页](https://doi.org/10.1007/BF02395039)；[原始PDF入口](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6020-11511_2006_Article_BF02395039.pdf)。
- 获取：unavailable: HTTP Error 500: Internal Server Error。
- 核读范围：303 密度定理适用范围比较；固定频带的必要条件不等于增长窗残余控制。

**Anderson-Trapp-1975 — Shorted Operators. II**

- 作者：W. N. Anderson Jr.; G. E. Trapp。
- 版本：SIAM J. Appl. Math. 28(1) (1975), 60–71; DOI 10.1137/0128007。
- [来源页](https://epubs.siam.org/doi/10.1137/0128007)；[原始PDF入口](https://epubs.siam.org/doi/pdf/10.1137/0128007?download=true)。
- 获取：unavailable: HTTP Error 403: Forbidden。
- 核读范围：已核对出版社书目和摘要；尚未核读全文；正算子 shorting 的适用范围比较。

**Bellotti-Wong-2025 — Improved estimates for the argument and zero-counting function of the Riemann zeta-function**

- 作者：Chiara Bellotti; Peng-Jie Wong。
- 版本：arXiv:2412.15470v2; 2025-07-07。
- [本地PDF](background/bellotti-wong-zero-counting-v2.pdf)（32页）；[来源页](https://arxiv.org/abs/2412.15470v2)；[原始PDF链接](https://arxiv.org/pdf/2412.15470v2)。
- 核读范围：独立复核者核读Theorem 1.1陈述；303/304短区间系数比较，不声称全文及数值常数认证已复跑。

## phase 2 第5轮：实际零密度输入

**Chourasiya-Simonic-2025 — An explicit form of Ingham's zero density estimate**

- 作者：Shashi Chourasiya; Aleksander Simonič。
- 版本：arXiv:2507.15184v2; 2025-09-30。
- [本地PDF](background/chourasiya-simonic-ingham-v2.pdf)（33页）；[来源页](https://arxiv.org/abs/2507.15184v2)；[原始PDF链接](https://arxiv.org/pdf/2507.15184v2)。
- 核读范围：已核读v2第1–2、4–5页：计数含重数、Corollary 1、Table 1覆盖、推论调用及统一弱化C=224；未复证全篇、表格优化或有限高度验证。

## phase 3：共同Gram与原始来源复核（2026-09-06）

- **Schur-1911**：J. (Issai) Schur，*Bemerkungen zur Theorie der beschränkten Bilinearformen mit unendlich vielen Veränderlichen.*，J. reine angew. Math. 140 (1911), 1–28。
  [原始来源](https://doi.org/10.1515/crll.1911.140.1)；[GDZ馆藏](https://gdz.sub.uni-goettingen.de/id/PPN243919689_0140)；[原始PDF下载](https://gdz.sub.uni-goettingen.de/download/pdf/PPN243919689_0140/LOG_0004.pdf)。
  本地文件为 `background/schur-bilinear-1911.pdf`，29页（馆藏封面1页＋原刊1–28页），完整原件未改写。
  馆藏封面注明限制向其他仓库复制，因此PDF仅本地保存，Git同步来源、版本、SHA-256和本说明。
  主线程视觉核对原刊1、6、7、28页；只读复核者读取1–10页馆藏OCR，重点§2 Satz I。
  319的现代两权Schur检验另有自含证明，不称为原文逐字定理。
- **MV-1974**：既有10页PDF重新核读原刊74–75、82页，Theorem2及Corollary2；常振幅、实频率范围没有被误用于变深度列。
- **Chourasiya-Simonic-2025**：既有v2 PDF重新核读1–2、4–5页，统一计数含重数，使用Corollary1／Table1而非只用有限sigma范围的Theorem1。
- **Bellotti–Wong v2**：本轮承继314已核读的单位高度计数弱化，不扩大为本轮重新全审。

完整核读及内部287／314重叠边界见[来源报告](../reviews/2026-09-06/phase3-primary-literature-review.md)。
Schur出版社PDF入口返回202空正文；GDZ文章PDF入口成功。所有29页对象解析通过，扫描正文需要视觉核读。

## 持续GOAL周期4核读更新（2026-09-06）

BGST-2025的既有v3原件第7–8页3.3–3.5已重新核对：第7页主声明是移动区间，实际前缀公式在第8页3.5。用于[324候选sharp去权](../notes/324-sharp-mt-second-moment-by-measure-deweighting.md)，其新证明另待交叉复核。没有新增或覆盖PDF版本。

## 持续GOAL周期4：全体零密度比较（2026-09-06）

- **Guth-Maynard-2026**，Larry Guth、James Maynard，*New large value estimates for Dirichlet polynomials*。arXiv:2405.20552v2，2026-04-07。[原始PDF](background/guth-maynard-large-values-2405.20552v2.pdf)，实际52页；[版本页](https://arxiv.org/abs/2405.20552v2)、[下载](https://arxiv.org/pdf/2405.20552v2)。核读第1–2页Thm1.1/1.2及(1.2)/(1.3)；没有重审全文。来源摘要页说48页，与取得PDF实际52页分别记录。
- **Tao-Trudgian-Yang-2025**，Terence Tao、Tim Trudgian、Andrew Yang，*New exponent pairs, zero density estimates, and zero additive energy estimates: a systematic approach*。arXiv:2501.16779v1，上传2025-01-28，PDF标2025-01-29。[原始PDF](background/tao-trudgian-yang-exponents-2501.16779v1.pdf)，44页；[版本页](https://arxiv.org/abs/2501.16779v1)、[下载](https://arxiv.org/pdf/2501.16779v1)。核读Definition37、Thm51及必要条款，发现印刷证明步骤(40)到(42)失败；k=4修补已由主线程核对原始输入、端点逻辑并复跑130项有理连续参数检查，见[328补证](../notes/328-tty-thm51-proof-repair-and-scope.md)。详见[复核记录](../reviews/2026-09-06/326-density-source-review.md)，不声称定理结论错误。
- **ANTEDB-20260905**，Terence Tao、Timothy Trudgian、Andrew Yang，*Database of known results on analytic number theory exponents*。PDF封面日期2026-09-05，本次抓取2026-09-06。[固定原始PDF](background/antedb-blueprint-20260906.pdf)，190页；[作者证明蓝图](https://teorth.github.io/expdb/blueprint/)、[下载](https://teorth.github.io/expdb/blueprint.pdf)。来源站会更新，用manifest完整SHA固定字节；核读第11章相关条款，部分TTY代数问题仍见于蓝图；不视为独立认证，也未认证整个数据库。

三份下载均全页解析，哈希、大小及时间见manifest。网页检索摘要的旧页数／日期不覆盖原始PDF事实。
Bourgain 2000的原始DOI https://doi.org/10.1155/S107379280000009X 本次web未取得全文；不把数据库转述称为核读该原件。

## 持续研究的反向大值输入核查（2026-09-07）

- **Matomäki–Teräväinen (2024)**，*A note on zero density results implying large value estimates for Dirichlet polynomials*。arXiv:2403.13157v1（2024-03-19），16页。[本地PDF](background/matomaki-teravainen-density-to-large-values-2403.13157v1.pdf)；[固定版本](https://arxiv.org/abs/2403.13157v1)；[下载](https://arxiv.org/pdf/2403.13157v1)。2026-09-07检索的arXiv历史仅列v1；全文已归档并全页解析，Theorem1.2与ANTEDB11.6的所列量词及反例已经独立核查，未导入新的算术结果。SHA、字节数与取得时间见manifest。

本次原始范围审计见[反向大值来源记录](../reviews/2026-09-07/reverse-large-values-source-audit.md)：
主线程及Gibbs已核读新原件第1–9页；ANTEDB11.6全tau转述的反例与tau>=2的测度桥梁已通过[独立复核](../reviews/2026-09-07/reverse-large-values-independent-review.md)。
原Theorem1.2的短长度范围保持；未认证原文完整解析证明、其他数据库条款或新的零密度结果。

## 完整节点组与经典插值背景（2026-09-07）

- **Douglas N. Clark (1968)**，*On matrices associated with generalized interpolation problems*，Pacific Journal of Mathematics 27(2), 241–253。[原始PDF](background/clark-generalized-interpolation-1968.pdf)；[出版者下载](https://msp.org/pjm/1968/27-2/pjm-v27-n2-p04-p.pdf)。实际PDF17页，全页可解析。仅核读PDF第1–3页标题与范围介绍，未导入其全定理；332有限Cauchy公式自证。SHA、字节数与取得时间见manifest。
- Tom Alberts的[Cauchy determinant讲义](https://math.utah.edu/~alberts/notes/cauchy-determinant-formula/c_det_formula/)已检索，正文读取返回502，未取得PDF；只保留检索入口，不称为核读原件。

## 下一算术输入筛查：双线性Kloosterman与素数多项式（2026-09-07）

- **Alexandru Pascadi**，*Non-abelian amplification and bilinear forms with Kloosterman sums*，arXiv:2511.08445v2; 2026-06-21。54页。[本地PDF](background/pascadi-kloosterman-2511.08445v2.pdf)；[固定版本](https://arxiv.org/abs/2511.08445v2)；[原件下载](https://arxiv.org/pdf/2511.08445v2)。全文已归档并解析，主定理已初核（范围见下），实际映射未证；不从摘要直接导入幂节省。
- **Djordje Milicevic; Xinhua Qin; Xiaosheng Wu**，*Bilinear forms with Kloosterman sums and moments of twisted L-functions*，arXiv:2511.07550v1; 2025-11-10。37页。[本地PDF](background/milicevic-qin-wu-kloosterman-2511.07550v1.pdf)；[固定版本](https://arxiv.org/abs/2511.07550v1)；[原件下载](https://arxiv.org/pdf/2511.07550v1)。全文已归档并解析，主定理已初核（范围见下），实际映射未证；不从摘要直接导入幂节省。
- **S. K. K. Choi; A. V. Kumchev**，*Mean values of Dirichlet polynomials and applications to linear equations with prime variables*，arXiv:math/0412227v1; 2004-12-12。20页。[本地PDF](background/choi-kumchev-prime-mean-values-0412227v1.pdf)；[固定版本](https://arxiv.org/abs/math/0412227v1)；[原件下载](https://arxiv.org/pdf/math/0412227v1)。全文已归档并解析，主定理已初核（范围见下），实际映射未证；不从摘要直接导入幂节省。

三篇SHA、字节数和取得时间见manifest。Pascadi当前v2含作者标明的修订与小纠正；MQW及Choi–Kumchev版本历史当前仅v1。旧MOM-1的240–241停止条件保持；只核查这些外部估计是否提供真正不同的输入。

原始条款及[独立复核](../reviews/2026-09-07/kloosterman-source-independent-review.md)
已写入[新输入筛查](../reviews/2026-09-07/kloosterman-next-input-screen.md)：
Pascadi第1–5页（另定位Thm7.1/7.8陈述）、MQW第1–4页、Choi–Kumchev第1–2页。
初始／平移区间、互素条件和完整字符族已修订；全证和MOM双线性映射未认证。
Choi–Kumchev PDF首页另标draft 2018-09-26，与arXiv上传2004-12-12及期刊2006分别保留，
不据此声称2018有实质修订。

## Pascadi发表版本补充（2026-09-07）

- **Pascadi, GAFA (2026)**：期刊页确认2026-08-21在线发表，DOI 10.1007/s00039-026-00746-0。[期刊页](https://link.springer.com/article/10.1007/s00039-026-00746-0)；[本地70页PDF](background/pascadi-kloosterman-gafa-2026.pdf)；[原件下载](https://link.springer.com/content/pdf/10.1007/s00039-026-00746-0.pdf)。保留54页arXiv v2独立版本；期刊网页主条款已初核，PDF逐条比较与全证认证未完成。

## 有限域determinant Fourier的经典背景（2026-09-07）

- **Yeşim Demiroğlu Karabulut**，*Cayley Digraphs of Matrix Rings over Finite Fields*，arXiv:1710.08872v1，2017-10-24。[本地PDF](background/karabulut-matrix-digraphs-1710.08872v1.pdf)；[固定版本](https://arxiv.org/abs/1710.08872v1)；[下载](https://arxiv.org/pdf/1710.08872v1)。19页，全文解析；主线程核读第14–16页Thm3.12的逐字符谱公式及Cor3.13，与336的h=1有限域公式对应。未认证全篇图论／sum-product结论或谱值碰撞后的合并重数。[机构期刊记录](https://authors.library.caltech.edu/records/mhw8q-yd829)对应后来题名 *Unit-graphs and special unit-digraphs on matrix rings*，Forum Mathematicum 30(6),2018,1397–1412；不把预印本当成期刊排版版。
- 检索到AIMS DOI 10.3934/math.2025168的相关determinant Fourier论文，[原始页面](https://aimspress.com/article/doi/10.3934/math.2025168)读取失败，未取得PDF或核读定理；暂只保留入口，不作为证明依赖。

## 实际prime权短频带的PNT输入复读（2026-09-07）

既有Fiori–Kadiri–Swidinsky arXiv:2204.02588v3的26页原件未变；
主线程重读第1–4页，特别第2页Corollary1.4的psi误差与x>2量词，
为340仅使用经典exp(-c sqrt(log x))弱化。
第3页区分计算验证高度、全RH与已修正的上游常数；
本次没有重跑全篇显式常数／数值依赖，也不声称更新PNT纪录。
