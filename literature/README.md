# RH-Weil 文献索引

索引续记更新至2026-09-20；最新批次、范围和保存状态见文末。以下2026-09-09统计为历史快照。首批归档聚焦67.25%之后的零点比例进展及直接依赖（15份、220页）；后续原始版本与核读范围按轮次列在文末。当前本地共50份外部原始PDF、1676页，其中49份、1647页纳入Git保存；Schur扫描29页按来源封面要求仅本地保存，出处和哈希同步。获取失败单列。研究判断见 [305文献审计](../notes/305-post-6725-literature-baseline-audit.md)。

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

2026-09-08为[351实际传递候选](../notes/351-fixed-radius-stability-and-actual-zero-transfer.md)
再次核对Lamzouri固定v1的§3去权步骤及BGST固定v3的保留旧Lemma5脚注、前缀式(3.5)。
见[准确核读范围](../reviews/2026-09-08/fixed-radius-analytic-source-check.md)；
现有PDF原件及哈希不变，未重审全文或新增版本。

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
  2026-09-08重读PDF第3–6页，并固定归档其证明说明和验证器源文件；
  仅核读Hessian／LDL／切线接口，未复跑完整认证。见[来源回查](../reviews/2026-09-08/subaction-verifier-source-check.md)。

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

## 自由整数变量Poisson背景（2026-09-08）

- **Andrew Sutherland (2015)**，*18.785 Number Theory I, Lecture 16: The functional equation*，MIT讲义，封面日期2015-11-05。
  [本地6页PDF](background/sutherland-poisson-lecture16-20151105.pdf)；
  [原始来源及下载](https://math.mit.edu/classes/18.785/2015fa/LectureNotes16.pdf)。
  主线程经web核读第1–2页Definition16.1/16.2、Theorem16.3及周期化证明；
  其Schwartz假设不直接覆盖343的硬端点核。初次下载403，携带普通浏览器UA和MIT来源头重试成功，原件全页解析通过。
- **Stephen D. Miller; Wilfried Schmid (2003)**，*Summation Formulas, from Poisson and Voronoi to the Present*，arXiv:math/0304187v1，2003-04-15。
  [本地22页PDF](background/miller-schmid-summation-0304187v1.pdf)；
  [固定版本页](https://arxiv.org/abs/math/0304187v1)；
  [原件下载](https://arxiv.org/pdf/math/0304187v1)。
  全页解析通过；主线程核读第1页(1.1)–(1.2)及跳跃点（含端点）的左右极限平均，
  第2–3页只作范围比较。343补出孤立删点修正；未导入GL3公式或认证全篇证明。

SHA、大小、页数及获取时间见manifest和[下载记录](../reviews/2026-09-08/poisson-source-downloads.json)。
两份均保留公开原件，未以整理文字替换PDF。

## shell端点的经典无理性条款（2026-09-08）

- **Sever Angel Popescu**，*A simple and self-contained proof for the Lindemann-Weierstrass theorem*，arXiv:2306.14352v2，上传2023-09-17，PDF首页另标2023-07-29。
  [本地17页PDF](background/popescu-lindemann-weierstrass-2306.14352v2.pdf)；
  [固定版本](https://arxiv.org/abs/2306.14352v2)；
  [原件下载](https://arxiv.org/pdf/2306.14352v2)。
  全页解析；主线程定位第11页Theorem3.1的有理系数线性无关陈述及第14页Corollary3.1和短证明：
  非零实代数数的指数无理。这里只引用经典Lindemann推论[R]，
  用于排除整数X时有理ad/bc恰等于exp(±1/sqrt X)；未核审该文完整新证明或历史优先权。
  相关PDF未改写，SHA和获取信息见manifest及[下载记录](../reviews/2026-09-08/popescu-source-download.json)。

## 多窗与方法上限的后续来源准备（2026-09-08）

- **Devine v1.0.3**：既有18页PDF重读第1–8页，重点Proposition1的平稳二次能量到非线性谱余项传递；完整定量分支链未认证。
  [原公开包入口](https://zenodo.org/records/22066689/files/consecutive_triple_simple_zeros_v3_public.tar.zst?download=1)
  及API内容入口本轮均HTTP403；[随包哈希来源](https://zenodo.org/records/22066689/files/consecutive_triple_simple_zeros_v3_public.tar.zst.sha256?download=1)可读。
  未取得压缩包，不将其算入本地附件。
- **Bryan Carson / Hydra Dynamix**：固定提交3c1d0ef81bf3af689d699ceefa9dc984a1dedb93。
  [来源仓库](https://github.com/hydra-dynamix/zeta23-verification/tree/3c1d0ef81bf3af689d699ceefa9dc984a1dedb93)；
  [技术说明原件](supplements/hydra-3c1d0ef/NOTE.md)、
  [README](supplements/hydra-3c1d0ef/README.md)、
  [law原件](supplements/hydra-3c1d0ef/witness/law_certified.txt)、
  [Python检查器](supplements/hydra-3c1d0ef/witness/verify_law.py)；
  [LICENSE](supplements/hydra-3c1d0ef/LICENSE)及[NOTICE](supplements/hydra-3c1d0ef/NOTICE)同时保留。
  六份原件的固定下载链接、时间、大小、SHA均记入manifest。
  本轮只运行给定整数区间的行检查，不称为从支持重建完整见证，未编译Lean。

完整核读和运行边界见[来源筛查](../reviews/2026-09-08/next-input-source-screen.md)。
PDF仍为42份1354页；新增六份文本／代码附件不计入PDF页数。

## 2026-09-08：势证书验证器附件

固定Tawan提交45149f6d403059a71be73c5e3f884cee7cd62b20和ainta提交040c5e899e658aed7b56a2a87f501798fe10761d。原文件及许可完整保留；源码核读范围见[回查记录](../reviews/2026-09-08/subaction-verifier-source-check.md)。

- [tawan-45149f6/LICENSE](supplements/tawan-45149f6/LICENSE) — [固定原文](https://github.com/tawanerguo-cn/zeta-simple-zeros/blob/45149f6d403059a71be73c5e3f884cee7cd62b20/LICENSE)。
- [tawan-45149f6/BELLMAN_COBBOUNDARY_PROOF.md](supplements/tawan-45149f6/BELLMAN_COBBOUNDARY_PROOF.md) — [固定原文](https://github.com/tawanerguo-cn/zeta-simple-zeros/blob/45149f6d403059a71be73c5e3f884cee7cd62b20/BELLMAN_COBBOUNDARY_PROOF.md)。
- [tawan-45149f6/NEXT_FRONTIER.md](supplements/tawan-45149f6/NEXT_FRONTIER.md) — [固定原文](https://github.com/tawanerguo-cn/zeta-simple-zeros/blob/45149f6d403059a71be73c5e3f884cee7cd62b20/NEXT_FRONTIER.md)。
- [tawan-45149f6/tools/verify_coboundary.cpp](supplements/tawan-45149f6/tools/verify_coboundary.cpp) — [固定原文](https://github.com/tawanerguo-cn/zeta-simple-zeros/blob/45149f6d403059a71be73c5e3f884cee7cd62b20/tools/verify_coboundary.cpp)。
- [tawan-45149f6/tools/generate_coboundary_derivative_table.py](supplements/tawan-45149f6/tools/generate_coboundary_derivative_table.py) — [固定原文](https://github.com/tawanerguo-cn/zeta-simple-zeros/blob/45149f6d403059a71be73c5e3f884cee7cd62b20/tools/generate_coboundary_derivative_table.py)。
- [tawan-45149f6/tools/generate_joint_kernel_table.py](supplements/tawan-45149f6/tools/generate_joint_kernel_table.py) — [固定原文](https://github.com/tawanerguo-cn/zeta-simple-zeros/blob/45149f6d403059a71be73c5e3f884cee7cd62b20/tools/generate_joint_kernel_table.py)。
- [ainta-040c5e8/LICENSE](supplements/ainta-040c5e8/LICENSE) — [固定原文](https://github.com/ainta/zeta-simple-zeros/blob/040c5e899e658aed7b56a2a87f501798fe10761d/LICENSE)。
- [ainta-040c5e8/docs/verifier.md](supplements/ainta-040c5e8/docs/verifier.md) — [固定原文](https://github.com/ainta/zeta-simple-zeros/blob/040c5e899e658aed7b56a2a87f501798fe10761d/docs/verifier.md)。

截至2026-09-08该批归档为42份PDF、1354页（其中Schur扫描原件仅本地）；另有19份补充原件。

<a id="f1-20260909"></a>

## F₁构造与存在性原始文献（2026-09-09）

八份新增PDF共322页，按原字节保存于f1目录。归档及全页解析不等于完整数学复核；
研究判断与局部构造见[363](../notes/363-f1-arithmetic-geometry-and-existence-audit.md)。
本轮还核查了[Connes作者出版目录](https://alainconnes.org/publications/)；
目录列出2026年Jacobian论文为Journal of Noncommutative Geometry forthcoming，本地保存的是固定arXiv v1。
未将网页出现日期或抓取时间当作论文首次发布日期。

**Borger-2009-F1 — Lambda-rings and the field with one element**

- 作者：James Borger；版本：arXiv:0906.3146v1。
- [本地PDF](f1/borger-lambda-rings-0906.3146v1.pdf)（31页）；[固定来源](https://arxiv.org/abs/0906.3146v1)；[原件下载](https://arxiv.org/pdf/0906.3146v1)。
- 核读范围：PDF1–3页：Lambda下降、标准整数初对象、伴随函子；未复核全篇分类定理。PDF首页打印日期2024-11-26，与v1上传日期2009-06-17区分。

**Lorscheid-2012-blueprints — The geometry of blueprints. Part I: Algebraic background and scheme theory**

- 作者：Oliver Lorscheid；版本：arXiv:1103.1745v2。
- [本地PDF](f1/lorscheid-blueprints-1103.1745v2.pdf)（51页）；[固定来源](https://arxiv.org/abs/1103.1745v2)；[原件下载](https://arxiv.org/pdf/1103.1745v2)。
- 核读范围：PDF21–22页Proposition1.12及证明：blueprint张量积和不同子范畴；未审全部scheme理论。

**CC-2015-arithmetic-site — Geometry of the arithmetic site**

- 作者：Alain Connes; Caterina Consani；版本：arXiv:1502.05580v1。
- [本地PDF](f1/cc-arithmetic-site-1502.05580v1.pdf)（43页）；[固定来源](https://arxiv.org/abs/1502.05580v1)；[原件下载](https://arxiv.org/pdf/1502.05580v1)。
- 核读范围：PDF1–3、18–20、23–32、38页：算术几何态射、平方定义、Proposition6.21与Theorem7.7；重点读定义和所列证明段，未逐篇复核全部结果。

**CC-2016-scaling-site — Geometry of the scaling site**

- 作者：Alain Connes; Caterina Consani；版本：arXiv:1603.03191v1。
- [本地PDF](f1/cc-scaling-site-1603.03191v1.pdf)（43页）；[固定来源](https://arxiv.org/abs/1603.03191v1)；[原件下载](https://arxiv.org/pdf/1603.03191v1)。
- 核读范围：PDF32页Theorem5.17与连续维数定义：周期轨道RR；未独立复跑完整证明。

**CC-2018-complex-lift — The Riemann-Roch strategy, Complex lift of the Scaling Site**

- 作者：Alain Connes; Caterina Consani；版本：arXiv:1805.10501v1。
- [本地PDF](f1/cc-complex-lift-1805.10501v1.pdf)（67页）；[固定来源](https://arxiv.org/abs/1805.10501v1)；[原件下载](https://arxiv.org/pdf/1805.10501v1)。
- 核读范围：PDF1–5、17–22页：路线、Jensen下降、五步存在性策略；第7节仅按引言与第3节定位，不宣称已核审全部Frobenius复提升证明。

**CC-2023-RR-Z — Riemann-Roch for the ring Z**

- 作者：Alain Connes; Caterina Consani；版本：arXiv:2306.00456v1。
- [本地PDF](f1/cc-riemann-roch-z-2306.00456v1.pdf)（9页）；[固定来源](https://arxiv.org/abs/2306.00456v1)；[原件下载](https://arxiv.org/pdf/2306.00456v1)。
- 核读范围：PDF1、8页Theorems1.1/5.1：保留右连续取整函数；未完整重审S模维数理论。

**CC-2026-Jacobian — On the Jacobian of $\overline{\operatorname{Spec}\mathbb Z}$**

- 作者：Alain Connes; Caterina Consani；版本：arXiv:2602.15941v1。
- [本地PDF](f1/cc-jacobian-2602.15941v1.pdf)（48页）；[固定来源](https://arxiv.org/abs/2602.15941v1)；[原件下载](https://arxiv.org/pdf/2602.15941v1)。
- 核读范围：PDF3–5页Theorems1.1/1.2及广义除子；PDF18页定位Theorem3.4，未完整重审全adelic分类。

**CC-2026-absolute-geometry — On the Absolute Geometry of Spec Z**

- 作者：Alain Connes; Caterina Consani；版本：arXiv:2606.06604v1。
- [本地PDF](f1/cc-absolute-geometry-2606.06604v1.pdf)（30页）；[固定来源](https://arxiv.org/abs/2606.06604v1)；[原件下载](https://arxiv.org/pdf/2606.06604v1)。
- 核读范围：PDF1–7页：定义、Proposition2.2/2.3及引言Theorems1–4；未重审全部perfectoid/untilt定理。摘要页标题未含PDF副标题and the Fargues-Fontaine curve。

全部SHA-256、字节数和获取时间见[manifest](manifest.json)及[原始下载记录](../reviews/2026-09-09/f1-source-download.json)。
Deitmar／Soulé／其他绝对几何本轮未逐项独立审计，不把本小节称为全部F₁文献的穷尽综述。

## F₁ 本科背景讲义的补充来源（2026-09-10）

**Milne-LEC-2013 — Lectures on Étale Cohomology**

- 作者：James S. Milne；作者版本 v2.21，2013-03-22，202 页。
- [本地 PDF](background/milne-etale-cohomology-v2.21.pdf)；
  [作者 PDF](https://www.jmilne.org/math/CourseNotes/LEC.pdf)；
  [作者目录](https://www.jmilne.org/math/CourseNotes/lec.html)。
- 用途：为[本科背景讲义](../docs/f1-route-from-undergraduate-math.md)提供有限域曲线、
  Frobenius、不动点及 Weil 猜想背景；核读第 25–27 节相关陈述，不宣称复核全书证明。
- 全部 202 页解析通过；PDF 第 150 页（索引 149）无可提取文字，单列记录。
  原始 SHA256、字节数和抓取时间见[下载记录](../reviews/2026-09-10/f1-primer-source-download.json)
  及 `manifest.json`。本文献已保存原始字节，不只保留网站链接。

## 2026-09-10：F₁对应比较的新增核读范围

原始PDF和固定版本均沿用既有归档。本轮核读2015稿PDF26–28页的F(n)求值、
33–38页的对应定义及有理复合分支；2018稿PDF62–65页§7的右作用、
Witt系数、字符族与(93)–(96)，公式页另经渲染核对。
[365比较记录](../notes/365-f1-rational-comparison-and-witt-coefficients.md)区分
正系数Newton层的交换方块、全复截面的相消、固定标量化失配及可用的半线性模型。
未重审所有完备化、全部对应张量积证明或全局RR；下载身份不变，新增核读范围记录于manifest。

## 2026-09-10：字符族主除子、周期线丛与热带theta

2018原件新增核读PDF18–22页Jensen、23–27页Jessen陈述，31–38、42–44及62–65页
指定轨道／字符命题；相关公式另经渲染核对，见[来源审查](../reviews/2026-09-10/f1-classical-orbit-source-audit.md)。
2016原件新增核读PDF21–29页的H_p系数、次数、torsion、theta和仿射余循环；
PDF23页定义及定理经渲染核查。[368](../notes/368-f1-tropical-theta-and-coefficient-obstruction.md)
记录比较的准确范围，未将热带RR认证为所选复结构层的RR。

**Stacks-Divisors-ed88ff78 — Divisors**

- 作者：The Stacks Project Authors；版本ed88ff78，2026-07-14编译，94页。
- [本地PDF](background/stacks-divisors-ed88ff78-20260714.pdf)；
  [原始下载](https://stacks.math.columbia.edu/download/divisors.pdf)；
  [稳定标签Tag01X1](https://stacks.math.columbia.edu/tag/01X1)。
- 使用PDF57页的局部环空间正则截面与亚纯层定义，及茎未必等于全商环的警告；
  该页已渲染核查，全部94页解析通过。未移植scheme专属的维数、平坦性等结论。
- 原件SHA256为`0527740ac9877baff00aaad784e66aae83ff541dad40d4939028059f9f28a493`；
  861390字节，获取时间和解析信息见[下载记录](../reviews/2026-09-10/f1-cartier-source-download.json)。


## 2026-09-10：period ring、FF几何与Jessen归一化

2026固定原件新增核读§§3–5，见[来源审查](../reviews/2026-09-10/f1-2026-period-ring-source-audit.md)。
2018固定原件新增核读PDF23–31页；(22)/(23)/(29)之间的2π归一化用显式函数核对，
见[Jessen审查](../reviews/2026-09-10/f1-jessen-normalization-source-audit.md)。这些不扩大为全文数学认证。

以下均为Jacob Lurie的Math 205（Fall 2018）讲义，由[作者IAS目录](https://www.math.ias.edu/~lurie/205.html)
下载原件；四份共17页，全页解析通过，SHA256和获取时刻见manifest及
[下载记录](../reviews/2026-09-10/f1-lurie-source-download.json)。作者讲义不是本项目的新理论。

| 原件 | 日期／页数 | 本轮使用及范围 |
|---|---|---|
| [Lecture 6: Definition of the Fargues-Fontaine Curve](f1/lurie-2018-lecture06.pdf)／[下载](https://www.math.ias.edu/~lurie/205notes/Lecture6-Curve.pdf) | 2018-10-29／4 | B及Gauss范数完成、Frobenius；全讲核读 |
| [Lecture 8: The Field BdR](f1/lurie-2018-lecture08.pdf)／[下载](https://www.math.ias.edu/~lurie/205notes/Lecture8-BdR.pdf) | 2018-10-29／5 | 一般F的untilt、局部DVR及代数闭前提边界；Singer全讲核读 |
| [Lecture 11: Trivial Eigenspaces of the Frobenius](f1/lurie-2018-lecture11.pdf)／[下载](https://www.math.ias.edu/~lurie/205notes/Lecture11-TrivialEigenspaces.pdf) | 2018-10-31／4 | P8及C9–12的完成轮廓稳定性；全讲核读，PDF3页渲染 |
| [Lecture 19: Line Bundles on the Fargues-Fontaine Curve and Their Cohomology](f1/lurie-2018-lecture19.pdf)／[下载](https://www.math.ias.edu/~lurie/205notes/Lecture19-LineBundles.pdf) | 2018-11-18／4 | 全讲假定F代数闭；Theorem5不可直接搬到372的F，Singer全讲核读 |

[几何接口审查](../reviews/2026-09-10/f1-lurie-geometric-binding-source-audit.md)区分实际Proj有理函数、
完整截面同构与尚缺的除子重数比较；[372](../notes/372-f1-period-ring-tropical-principal-comparison.md)
的热带比较另有本项目证明，已通过内部独立复核。

**Jessen–Tornehave（1945）**，*Mean motions and zeros of almost periodic functions*，
Acta Math.77,137–279；[DOI](https://doi.org/10.1007/BF02392225)／
[YMSC目录](https://archive.ymsc.tsinghua.edu.cn/pacm_paperurl/20170108203121071731656)。
本轮PDF获取HTTP500，未保存有效原件，也未核读原始全文；失败状态已列manifest。


## 2026-09-10：一般perfectoid底域的几何接口来源

- **Fargues–Fontaine，Courbes et fibrés vectoriels en théorie de Hodge p-adique**：
  [作者完整稿](f1/ff-courbe-author-20260910.pdf)，404页；
  [作者出版目录](https://webusers.imj-prg.fr/~laurent.fargues/Publications.html)，
  [原件下载](https://webusers.imj-prg.fr/~laurent.fargues/Courbe_fichier_principal.pdf)。
  此处按2026-09-10抓取的作者版本保存，不声称与Astérisque406出版字节相同。
  已定位第3、7章的一般完美域情形，当前正在核读准确前提／曲线与截面定理，未核审全书。
- **Lurie，Lecture 1: Overview**：
  [本地原件](f1/lurie-ffcurve-overview-20260910.pdf)，14页；
  [作者下载](https://www.math.ias.edu/~lurie/ffcurve/Lecture1-Overview.pdf)。
  来源路径ffcurve/与已存205notes/分开。当前核读PDF13页Remark30、Warning31：
  非代数闭F的闭点描述涉及有限扩张的untilt，不能照搬代数闭情形。

两份均全页解析通过；空白／无可提取文字页、字节、SHA256及获取时间见
[下载记录](../reviews/2026-09-10/f1-general-ff-source-download.json)。
解析通过不等于证明审核，后续来源复核另记。


上述一般F来源已完成[指定范围审核](../reviews/2026-09-10/f1-general-ff-geometric-source-audit.md)：
FF 7.3.3、11.2.2、11.3.1及§11.4可用于实际曲线、线丛与截面；
3.4.4的Newton零点贡献为degree×ord，同半径须相加。主线程另渲染PDF155页核对。
未独立重证几乎纯性、Sen–Tate及Kedlaya–Liu等原始依赖；
[375](../notes/375-f1-geometric-divisor-and-picard-comparison.md)的具体C_p比较已通过独立数学与来源复核，
见[对应记录](../reviews/2026-09-10/f1-geometric-comparison-independent-review.md)；仍非完整RR或ζ结论。

## 2026-09-13：相容系数扩张与实值群

| 作者与标题 | 固定原件／来源 | 本轮阅读边界 |
|---|---|---|
| Bjorn Poonen，Maximally complete fields | [本地PDF](f1/poonen-maximally-complete-author-20260913.pdf)／[作者原件](https://math.mit.edu/~poonen/papers/amsval.pdf)，19页；作者副本日期1992-03-04，出版1993 | PDF5–9构造及最大完成初段；一般G和完美剩余域，不自动给双参数Gauss环 |
| Kiran S. Kedlaya，Power series and p-adic algebraic closures | [本地PDF](f1/kedlaya-power-series-math-9906030v2.pdf)／[arXiv v2](https://arxiv.org/abs/math/9906030v2)，12页；1999-12-16 | PDF1及§2末；主要Theorem1尚未审。PDF排版日期2018-03-13与固定arXiv版本日期分开 |
| Alexander I. Efimov，On the Hahn-Witt series and their generalizations | [本地PDF](f1/efimov-hahn-witt-2406.19163v1.pdf)／[arXiv v1](https://arxiv.org/abs/2406.19163v1)，19页；2024-06-27 | PDF1、5–8定义与Theorem1.4；Q指数与一般G范围，未核审根单位／类域论主定理 |

三份原件全页解析通过；SHA256、字节及UTC获取时刻见manifest和
[下载记录](../reviews/2026-09-13/f1-hahn-witt-source-download.json)。
另新增FF §7.5/PDF279原页及2018 §7.1的独立核读，见
[来源范围报告](../reviews/2026-09-13/f1-real-coefficients-source-audit.md)。
2018共同实系数代数已存在，但单p周期主关系接口不由该事实自动提供。

## 2026-09-13：实系数环的相对几何接口候选来源

以下三份固定原件共451页，下载及全页解析通过，首页作者／标题已核对。
初次归档时仅核对首页；后续对KL的限定核读见本节末，不表示两部著作全文认证。
Tong仍为待深入核读来源。

| 作者／标题 | 原件与固定版本 |
|---|---|
| Kedlaya–Liu，Relative p-adic Hodge theory: Foundations | [本地PDF](f1/kl-foundations-1301.0792v5.pdf)／[arXiv v5](https://arxiv.org/abs/1301.0792v5)，2015-05-09，210页；标题排版日期2015-05-02 |
| Kedlaya–Liu，Relative p-adic Hodge theory, II: Imperfect period rings | [本地PDF](f1/kl-imperfect-1602.06899v3.pdf)／[arXiv v3](https://arxiv.org/abs/1602.06899v3)，2019-10-21，199页 |
| Xin Tong，Period Rings with Big Coefficients and Applications I | [本地PDF](f1/tong-big-coefficients-2012.07338v1.pdf)／[arXiv v1](https://arxiv.org/abs/2012.07338v1)，2020-12-14，42页 |

SHA256、字节、获取时刻及解析状态见[下载记录](../reviews/2026-09-13/f1-relative-period-source-download.json)
与manifest。下一核查按系数域、范数、局部化及层性逐项绑定，不由标题“相对”自动推断适用。

本日续核：[环域来源报告](../reviews/2026-09-13/f1-perfectoid-annulus-source-audit.md)
记录Foundations PDF82、89、92–94和Imperfect §2.4及相关perfectoid定理的限定阅读。
标准完美化环域的层性来源已确认；380的直接环识别及解析线丛实现已独立复核。
有理局部化的pseudoflat性仍要求稳定伪相干，不能仅凭全局非零因子导入Cartier结论。

再续：[有限层Cartier来源报告](../reviews/2026-09-13/f1-finite-level-cartier-source-audit.md)
核对KL1的有限affinoid局部化平坦性及理想严格性。Remark2.4.7印出的明示扰动阈值
经C×C例子发现不足；384保留固定冗余分子λ，以更严格的双向比较完成有限层下降。
这只修正所用数值范围，没有否定充分小扰动机制；原PDF和历史阅读账本保持不变。

[387来源续核](../reviews/2026-09-13/f1-analytic-continuation-source-audit.md)
绑定有理子域复合、uniform的非零谱检测及KL2 Appendix A的公开勘误。
本轮采用KL1 Definition2.8.1(a)–(c)，没有误用一般(d)的充分性。
KL2 Example2.4.2来自一维模曲线无限层，说明非零因子与局部主理想闭性仍须分开。

## 2026-09-13：无限层零测度的经典圆盘来源

Matthew Baker、Robert Rumely，*Potential Theory on the Berkovich Projective Line*，
**DRAFT 10/26/06**，272页：[本地PDF](f1/baker-rumely-potential-20061026-archive20070417.pdf)／
[作者原件的2007-04-17固定存档](https://web.archive.org/web/20070417164809id_/http://www.math.gatech.edu/~mbaker/pdf/BerkBook.pdf)。
不是后来的正式出版版；272页全页解析通过，11个原空白页保留，PDF37已渲染核对。
SHA256、字节及获取时刻见manifest和[下载记录](../reviews/2026-09-13/f1-berkovich-source-download.json)。

本轮仅采用Theorem1.2、Lemma1.3、§1.3／Lemma1.5／Proposition1.6及Theorem2.2的
点分类、圆盘分解和拓扑；[来源报告](../reviews/2026-09-13/f1-berkovich-disk-source-audit.md)
记录页码及推论边界。早期稿Corollary7.8的过强范围和Prop2.8的待补证明条目不采用。
特殊p幂边界、Rouché、perfectoid无限塔和规范测度均由388–389直接证明，未核审全书。

## 2026-09-15：候选几何空间、site大小与态射编码

The Stacks Project Authors，*Sites and Sheaves*，版本**ed88ff78，2026-07-14编译**：
[本地PDF](f1/stacks-sites-20260915.pdf)／[官方原件](https://stacks.math.columbia.edu/download/sites.pdf)。
本文件名记录获取日；不是声称内容版本为2026-09-15。115页全页解析通过，931,481字节，
SHA256为`88ce9f3a1e05a34d23092b4e6158203a85c4aeffef38344e258ec1309b00883f`。
核读PDF7、27–28、63，PDF28渲染；主要用tag00VG、00X9特别是Remark15.4的集合编码，
以及§29的呈现说明，未核审全部115页证明。
[保存与核读记录](../reviews/2026-09-15/f1-candidate-space-source.json)区分完整性和数学阅读。
390的有界候选类与G0类型修正由本项目另作直接论证，不是原文的F₁模空间定理。

<a id="f1-candidate-alternatives-20260915"></a>
## 2026-09-15：候选空间第二次独立审查与替代构造

新增四份公开原始PDF，共317页；文献原件及补充材料合计89份。
[下载与核读记录](../reviews/2026-09-15/f1-candidate-space-second-sources.json)固定SHA256、字节数与版本。
以下均为限定范围核查，未认证全部原文；研究建议见[391](../notes/391-f1-candidate-space-review-and-alternatives.md)。

| 文献 | 本地原件与来源 | 核读定位及用途 |
|---|---|---|
| Stacks，Categories；ed88ff78，2026-07-14编译，103页 | [本地PDF](f1/stacks-categories-ed88ff78-20260915.pdf)；[原件](https://stacks.math.columbia.edu/download/categories.pdf) | PDF31的Lemma21.7：有限非空逆系统；PDF59–61的§31及Example31.3：2纤维；PDF74的Definition35.1：群胚纤维化。相关网页tag086J／003O／003T另核 |
| Stacks，Modules on Sites；ed88ff78，2026-07-14编译，81页 | [本地PDF](f1/stacks-sites-modules-ed88ff78-20260915.pdf)；[原件](https://stacks.math.columbia.edu/download/sites-modules.pdf) | PDF51–53的§32，尤其Lemma32.5／Definition32.6的Picard集合与群；不混同任意ringed site的可逆性与局部自由秩一 |
| Olivia Caramello，An invitation to topos-theoretic model theory；Tehran IPM，2020-05，108页 | [本地PDF](f1/caramello-topos-model-theory-20260915.pdf)；[作者原件](https://www.oliviacaramello.com/Talks/InvitationToposTheoreticModelTheory.pdf) | PDF69、71–73：分类topos、语法site、Morita等价；不作为G0–G8在通常算术中有实例的证明 |
| David Marker，Model Theory for Algebra and Algebraic Geometry，part1；Spring2010–Orsay，25页 | [本地PDF](f1/marker-orsay-model-theory-part1-20260915.pdf)；[作者原件](https://homepages.math.uic.edu/~marker/orsay/orsay1.pdf) | PDF17–18，Theorem2.4紧致性及Proposition2.6非标准模型；固定通常R的额外限制由本项目另说明 |

既有原件的增量阅读：Lorscheid v2的PDF8、13–14及21–22（blueprint、monoid／半环化及张量积）；
Borger v1的PDF2（平坦Z情形的交换Frobenius提升）；CC2018 v1的PDF19–20、§3.2.2（Jensen比较）。
这些PDF字节均保持既有版本。J(1+1)=log2违反max加法不等式，是对原定义的直接检查，
不表示原文曾把Jensen映射断言为非阿基米德赋值。


## 2026-09-20：截面轮廓与参数拓扑的核读

- CC2016 [1603.03191v1](https://arxiv.org/abs/1603.03191v1)：Definitions5.14、5.16，式(25)—(28)，Theorem5.17及Lemma5.18。用于[393](../notes/393-f1-profile-surjectivity-and-filtered-dimension.md)；原PDF复用。
- CC2018 [1805.10501v1](https://arxiv.org/abs/1805.10501v1)：§3.2.1、§3.2.3、§3.4的热带化、有效性及平方RR边界；未认证全部几何构造。
- Ryszard Engelking，*Dimension Theory*，1978，ISBN 0-444-85176-3，[来源原件](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/engelking.pdf)：Theorem3.1.8与Corollary3.1.20（印刷212、216／PDF216、220）。316页；仅核所列页及书目信息。
  本地原件位于 `literature/background/engelking-dimension-theory-1978.pdf`，4,693,683字节，SHA-256为 `54e65f27cb7ea972a36862d0479b8ac4f5d08f2b4b076fb3795080c35e892c53`。
  按原件第2页的再发布限制及GOAL第八节要求，PDF仅本地保存；Git记录索引、哈希与范围。

[393独立复核](../reviews/2026-09-20/f1-profile-dimension-independent-review.md)和[第三次空间审查](../reviews/2026-09-20/f1-candidate-space-third-review.md)保留适用边界。
文献原件数由89增至90，其中新增一份为本地保留；不把复用旧PDF或选择性核读记作全文认证。


## 2026-09-20续记：完整几何主商与双侧对应

The Stacks Project Authors，*Commutative Algebra*，版本 **ed88ff78，2026-07-14编译**：
[归档PDF](f1/stacks-algebra-ed88ff78-20260920.pdf)／[官方原件](https://stacks.math.columbia.edu/download/algebra.pdf)／
[所用Lemma 10.153.7，tag04GK](https://stacks.math.columbia.edu/tag/04GK)。
469页，2,828,052字节，SHA-256为 `b035a1f02104906a1820636cd332a0d7962fef3318d207a056634cb14dc86947`。
仅核读标题、版本及PDF415页的Lemma153.7；用于[395](../notes/395-f1-geometric-measure-principal-quotient.md)
的Hensel剩余扩张论证，没有认证整章。PDF已随[276f674](https://github.com/lixiang90/RH-Weil/commit/276f6741555999891413ec4cf1f14be3a04d2f75)
保存GitHub；现已核验远端PDF blob及同步至H盘的本地原件，字节／SHA256均一致。
文献原件及补充材料的历史累计数由90增至91（包含此前仅本地保存的原件），不等于91份全部都在Git中。

CC2015 *Geometry of the arithmetic site* 的既有
[1502.05580v1原件](f1/cc-arithmetic-site-1502.05580v1.pdf)本轮复用：
核对Proposition6.13、Definition6.22、Definition7.1、式(41)–(42)及Theorem7.7。
双侧作用、约化对应及复合的切向例外作为[下一任务](../reviews/2026-09-20/f1-marked-correspondence-next-proof-plan.md)
的来源基线；重述这些既有定义不算本项目的新几何构造。

## 2026-09-20续记：对角解析平方与闭图理想

复用[KL Foundations v5原件](f1/kl-foundations-1301.0792v5.pdf)，固定版本
[arXiv:1301.0792v5](https://arxiv.org/abs/1301.0792v5)。
为[398](../notes/398-f1-diagonal-square-and-noncartier-graphs.md)重新核读PDF31页的开映射定理、
41–42页的有理局部化闭关系商、89页的有限多变量perfectoid Tate代数、
94页的有理局部化与层性；31、89、94页另渲染核对。
原件2,107,306字节，SHA256仍为`a6a117423db62aec072442bb15b70e3175bcc3b631bdcd6d74f740e3c6cfd942`。
没有新增重复PDF；本轮直接推导、独立审查状态与外部定理的引用范围分别记录。

另存Peter Scholze，*Perfectoid Spaces*，作者稿日期2011-11-19：
[原始PDF](f1/scholze-perfectoid-spaces-20111119.pdf)／
[作者网站](https://www.math.uni-bonn.de/people/scholze/PerfectoidSpaces.pdf)／
[arXiv固定书目条目](https://arxiv.org/abs/1111.4914v1)。
51页，571,464字节，SHA256为`2c7e645a4ec3c56d5ee9e012cfe52d99e45973eefb99f8383e3bb69f0211afd9`。
核对标题、日期及PDF38页Proposition6.18的命题与证明，另渲染该页；全51页文本解析通过。
仅作为398独立审查的纤维积背景比较，未认证完整tilting、几乎纯性或weight-monodromy证明。
此文件来自作者网站，不声称与arXiv或期刊PDF逐字节相同。
历史原件及补充材料累计数由91增至92，仍包含先前仅本地保存的原件。

## 2026-09-20续记：归一化根核的原C基底下降

Kiran S. Kedlaya，*p-adic differential equations: Absolute values*，MIT 18.787，fall 2007。
[作者原PDF](background/kedlaya-absolute-values-2007.pdf)／
[官方来源](https://kskedlaya.org/18.787/absolute-values.pdf)。
6页，76,399字节，SHA256为`8940d4dc58253c247737502e929dbdbfa68f059ce3f074f40ef3cda65341d8f5`。
为[399](../notes/399-f1-normalized-cartier-kernels-and-principal-topology.md)核读PDF3页Theorem4、
PDF4页Theorem6与唯一性证明、PDF5页代数扩张说明，3–4页另渲染核对。
有限扩张范数的存在性在该讲义中转引Newton多边形单元；本项目采用标准定理陈述，
未将该转引证明或整个课程计为已重审。全部六页文本解析不等于全文证明认证。
历史原件及补充材料累计数由92增至93，仍包括先前仅本地保存的原件。


### 2026-09-20：Cartier塔的pro范畴背景增量核读

复用已归档 [Stacks Categories，ed88ff78](f1/stacks-categories-ed88ff78-20260915.pdf)，不重复下载。
核读并渲染PDF33–34的Remark22.5与Example22.6；另核在线
[tag05PX](https://stacks.math.columbia.edu/tag/05PX)及[tag0G2W](https://stacks.math.columbia.edu/tag/0G2W)。
采用的是pro态射的lim-colim定义、逐层代表及共尾等价，不由此导入一般pro层的有效下降。
本轮[400](../notes/400-f1-cartier-tower-limit-and-stalk-defect.md)的解析逆极限和取茎失配是另行推导的限定命题。
原PDF字节和SHA256未变，文献数量不增加。


## 2026-09-20续记：402内在FF对角草稿的原文核读

复用[Fargues–Fontaine原件](f1/ff-courbe-author-20260910.pdf)，
核对一般F中θ满射、次数一untilt点、实际剩余域及scheme局部完成：
§1.1/PDF64，3.1.9/PDF148–149，3.1.11/PDF149–150，3.3.1/PDF153，§3.4.1/PDF154及7.3.3/PDF277–278。
整页渲染并视觉核对148、149、153、154、278；采用所列[R]输入，不声称重审整书依赖。
复用[Stacks Algebra原件](f1/stacks-algebra-ed88ff78-20260920.pdf)，
新增核读PDF331–333的微分商正合列及对角余法模（00RU、00RW），视觉核对331与333。
两份PDF的SHA256与既有manifest一致，没有新下载。
数学应用见[402草稿](../notes/402-f1-intrinsic-ff-diagonal-conormal-obstruction.md)，独立复核尚待完成。


## 2026-09-20续记：独立空间审查的完美性来源

新增[Stacks Cohomology of Sheaves原PDF](f1/stacks-cohomology-ed88ff78-20260920.pdf)，
[原始下载](https://stacks.math.columbia.edu/download/cohomology.pdf)，ed88ff78，137页，1,054,846字节。
SHA256：23fbd6af99fe8f0b36a010c0b69ebb0f0f54761f53b530c685b1375001bb5893。
本轮仅核读并视觉核对PDF114、117–118的08DN、08CL/08CQ；不把归档等同全文认证。
用途见[403](../notes/403-f1-support-locality-and-nonperfect-quotients.md)。


402后续已通过独立复核；主代理补核FF Definition5.1.1/PDF212。数学结论及范围见402和其独立报告。


### Trace formula in noncommutative geometry and the zeros of the Riemann zeta function (archived 2026-09-20)

Alain Connes. arXiv:math/9811068v1; 1998-11-10; preprint associated with Selecta Math. 5 (1999), 29-106.
[PDF](f1/connes-trace-math-9811068v1.pdf); [version](https://arxiv.org/abs/math/9811068v1); [download](https://arxiv.org/pdf/math/9811068v1).
88 pages; SHA-256 dfd4e9924d8980f82e3da11fdea861d318fda8f5c7ba57ee659baf8631975053. Selective reading completed; exact scope and limits are recorded in the 2026-09-20 update below.


### Knots, Primes and the adele class space (archived 2026-09-20)

Alain Connes; Caterina Consani. arXiv:2401.08401v1; 2024-01-16.
[PDF](f1/cc-knots-primes-2401.08401v1.pdf); [version](https://arxiv.org/abs/2401.08401v1); [download](https://arxiv.org/pdf/2401.08401v1).
10 pages; SHA-256 7f9305b4052e45da2a1952fec17697420e13c311737f01b2e6599ecaec74ace3. Selective reading completed; exact scope and limits are recorded in the 2026-09-20 update below.


## 2026-09-20续记：实际周期轨道与混合局部迹

复用[CC2015原件](f1/cc-arithmetic-site-1502.05580v1.pdf)，增量核读§4.1–4.3/PDF14–17及参考文献PDF42–43，PDF16视觉核对。
新存[CC2024原件](f1/cc-knots-primes-2401.08401v1.pdf)，本轮核读PDF1–5、视觉核对PDF4；
原件实际10页，arXiv页面comments所写9页不作为实档页数。
新存[Connes1998原件](f1/connes-trace-math-9811068v1.pdf)，半局部与特定全局迹的[独立来源审计](../reviews/2026-09-20/f1-adelic-local-trace-independent-review.md)已闭环。
下载时本机代理关闭连接，随后直接连接下载成功，原字节未修改。

数学推导和边界见[404](../notes/404-f1-adelic-periodic-orbits-and-mixed-local-trace.md)：
来源的局部固定点分布经独立计算给L/2=N，未建立全局除子交叉、主根空间或RR。

Connes原件实际核读：独立代理PDF21–22、28–36、41–47、76–78，PDF42视觉核对；主线程另读PDF29–32、视觉核对PDF31。
Theorem4可给404的固定有限S迹推论；Theorem5正式陈述为正特征，数域讨论与截断另列，不混写RH等价强度。


## 2026-09-20: CCM restriction map and trace radical

- Connes, Consani, Marcolli, *The Weil proof and the geometry of the adeles class space*,
  arXiv:math/0703392v1 (2007-03-13). [Source](https://arxiv.org/abs/math/0703392v1),
  [PDF](https://arxiv.org/pdf/math/0703392v1), [archived original](f1/ccm-weil-adeles-math-0703392v1.pdf).
- 61 pages, 657051 bytes; SHA256: 88c4e34577e5107f8be2dc8488a71976b94a4efb5ea03f93e9f7d60681c41dee.
- Selective source audit completed; see [report](../reviews/2026-09-20/f1-adelic-restriction-source-review.md) for exact textual and visual scope.
  The trace radical and genuine principal-divisor relations require separate identification.


### Fixed upstream references for CCM2007

- Ralf Meyer, *On a representation of the idele class group related to primes and zeros of L-functions*, arXiv:math/0311468v3; 2005-03-16.
  [Source](https://arxiv.org/abs/math/0311468v3), [PDF](https://arxiv.org/pdf/math/0311468v3), [local original](f1/meyer-ideles-math-0311468v3.pdf).
  53 pages; SHA256 52e911b9b7b8236cdf1eacaeaf01e0174cb1f55a637945f63dfee9cdc24bb87b.
  Title/metadata checked; full proof audit remains pending.
- Alain Connes; Caterina Consani; Matilde Marcolli, *Noncommutative geometry and motives: the thermodynamics of endomotives*, arXiv:math/0512138v2; 2007-03-10.
  [Source](https://arxiv.org/abs/math/0512138v2), [PDF](https://arxiv.org/pdf/math/0512138v2), [local original](f1/ccm-endomotives-math-0512138v2.pdf).
  58 pages; SHA256 68f9c8eaa5e9b46790e5adad0e8cd910da43566e7bc339ea5ecc81ab1f3fe601.
  Title/metadata checked; full proof audit remains pending.


405 completed the fixed identity-normalization comparison and the moment/radical audit.
The two upstream papers above were checked only for title and metadata.
The endomotives v2 PDF has 58 pages, while the arXiv comments say 52.
