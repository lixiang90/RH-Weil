# phase 3 原始文献、内部重叠及保存范围

2026-09-06。只读来源复核者Euclid，ID 01a0763f-503c-7202-974d-306c42b5ebbc。
两次有限任务分别比较分离Gram背景和共同密度／Schur预算；未改文件、未派生代理。
主线程随后保存Schur扫描件并视觉核对原刊1、6、7、28页。
数学主证明由Popper另审；本报告不以来源比较代替证明验收。

## 1. Montgomery–Vaughan原始范围

H. L. Montgomery、R. C. Vaughan，*Hilbert's Inequality*，
JLMS (2) 8 (1974), 73–82。
[DOI](https://doi.org/10.1112/jlms/s2-8.1.73)；
[已归档原始PDF](../../literature/background/montgomery-vaughan-hilbert-1974.pdf)。

Euclid核读原刊74–75、82页，视觉核对74、82页。
第74页Theorem2式(1.6)给实频率最小间距delta下的Hilbert和界pi/delta；
Corollary2式(1.8)给区间积分相对对角项的误差<=2pi/delta乘系数平方和，
第82页§4以展开积分及两个端点的Hilbert和证明该推论。
对常振幅归一化指数族，Gram误差<=2pi/(区间长度*delta)，不依赖列数。

本项目h_j含eta_A与sinh(d_j u)变振幅，展开后为复频率，
不能直接取区间长度2A、delta=D代入MV这个实频率推论。
317采用绝对远核及Schur行和，对数来自sum 1/k，未借用MV振荡相消。
由log M换为log T还使用了实际前缀高度范围。
MV所有辅助引理及Ingham1936原文没有在本轮重新审完。

## 2. Chourasiya–Simonic的统一总数输入

*An explicit form of Ingham's zero density estimate*，
[arXiv:2507.15184v2](https://arxiv.org/abs/2507.15184v2)，2025-09-30；
[已归档PDF](../../literature/background/chourasiya-simonic-ingham-v2.pdf)。
Euclid实读第1–2、4–5页，并视觉核对2、5页。

§1的N(sigma,T)计beta>=sigma、0<gamma<=T，含重数。
Corollary1、式(3)及Table1的16区间覆盖[1/2,1]，适用T>=3*10^12。
三个系数最大值46.06、9.461、167.8，加上对数指数2+nu(v)<=3，
给大高度统一N(1/2+v,T)<=224 L³T^nu(v)。
小高度可另增常数；不能坚持仍是224。
第4–5页推论证明还用式(11)补足左端范围，不能只引有sigma限制的Theorem1。

这是原始前缀总数界，不是移动中心短区间密度，不能把T替换为D。
319的局部O(L²)来自Bellotti–Wong所给单位高度O(L)和第一逆幂求和；
Bellotti–Wong原文本轮承继314的核读报告，没有重新认证其全文。
CS全篇、数值表优化及有限高度零点验证没有由本项目重证。

## 3. Schur原文与现代两权检验

J. (Issai) Schur，*Bemerkungen zur Theorie der beschränkten Bilinearformen
mit unendlich vielen Veränderlichen.*，J. reine angew. Math. 140 (1911), 1–28。
[DOI](https://doi.org/10.1515/crll.1911.140.1)；
[GDZ原文PDF](https://gdz.sub.uni-goettingen.de/download/pdf/PPN243919689_0140/LOG_0004.pdf)。

Euclid读馆藏原刊1–10页OCR，重点[第6页](https://gdz.sub.uni-goettingen.de/gdzocr/PPN243919689_0140/00000010.xml)
及[第7页](https://gdz.sub.uni-goettingen.de/gdzocr/PPN243919689_0140/00000011.xml)。
§2 Satz I给绝对行列和分别受zeta、chi控制时的范数sqrt(zeta*chi)界。
319§2的现代正权p_i、q_j形式有完整Cauchy–Schwarz证明；
准确归类为经典带权Schur的自含应用，不说成原文逐字表述。

主线程取得原始29页文件（馆藏封面1页＋原刊28页），全部页对象可解析，
正文为扫描，视觉核对标题、作者、原刊6–7页定理及证明、末页28。
原件40185885字节，SHA256 e225ba5eecd84d57d603449f00f1e8fbf74d399c82f30c0d4ce1b2342bea490d。
本地位置literature/background/schur-bilinear-1911.pdf。
封面明确限制向其他仓库复制，故保存本地原件并同步元数据和原始下载入口，PDF不推送Git。
全文其余部分没有被视作已核查证明；现代权重与具体尾预算依赖319自身推导。

## 4. 内部比较与实质边界

| 已有文件 | 已有范围 | 与本周期区别 |
|---|---|---|
| 099§1 | 常振幅MV双边积分推论 | 不覆盖变深度h_j |
| 223§3 | Hilbert空间值均值推广 | 系数仍不随积分变量改变 |
| 170、185、197§5 | 共同effect、非正交成本、条件可见性 | 不自动给同一R的共同范数 |
| 287§§2–5 | 同一CS输入，以0为中心全高度逆平方尾 | 没有移动中心第一逆幂与分离目标矩形矩阵 |
| 314§§3–4 | 移动中心局部／总数min和单目标逆平方尾 | 没有任意系数组合的||B_F*Q||、||P_FQ|| |
| 316 | 单簇质量响应与方向逆变换 | 没有增长簇数、Wmax块预算和共同R |

Euclid实读287、314、319、320全文作此有限比较，并读170及185／197相关段落。
319配对第一逆幂深度尾与另一侧分离行和，320通过块矩阵和Wmax选择共同日程，
在所核读的内部及原始条款中没有完全对应的已陈述组合。
这是相对既有基线的具体推进，不是Schur或CS定理本身的新版本。
有限比较不排除所有其他先行结果，不作世界优先权或外部发表认证。
