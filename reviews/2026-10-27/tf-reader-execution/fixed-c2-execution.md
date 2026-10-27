# 固定c2执行结算：真实配对通过，full-G尚不准自动继续

2026-10-27；G20261027同runtime createdAt1793085111、原0c4f冻结基线。[前门](next-fixed-pair-test.md)指定的单一c2=<v,U_log2v>已实际执行并通过宽≤1/1024门。前轮分类为progress：其实际向量证书、权威状态和GitHub已改变，而不是只写计划。本次继续该真实输入，没有换h0/F8/source/cutoff或恢复C046预算。

## 1. 实际结果

正式有理区间在[fixed-c2-certificate.json](fixed-c2-certificate.json)。下列短端点向外略化，避免浮点显示被误读为精确端点：

\[
 c_2\in[-0.039604989843303151,\ -0.039604989843302864].
\]

正式总width约2.8560275·10^−16<1/1024，含exact v*求值和真实v−v*输入运输。这个负值是unitary dilation的mixed coefficient，**不是Weil/J/T/E负值、q0负值或Hfin反例**。q0宽1/16仍未通过，fullG、原五源T/E/cross和Hfin均未执行。

## 2. 同一对象、五项和全部误差

H=L²(R+,dx)，F为核2cos(2πxy)的自伴酉，Hcut=1_(1,∞)，U=U_log2，Uf(x)=2^−1/2 f(x/2)。F8和NF=9699690不变；f=B h0为256 finite divisor steps，h0=1_[1,2]。g为384个integer endpoint sin/(πy)项，p*为27个even-monomial确切有理系数，ell*=1_(0,1)(g+p*)，v*=f−HcutFell*；此前真H误差δv<1.061e−16和n=||v||²窄界作为输入。

UHcut=1_(2,∞)U，FU=U^-1 F，因此c2(v*)的准确系数方向是

\[
 \langle f,Uf\rangle
 -\langle\ell_*,F Hcut U^{-1}f\rangle
 -\langle\ell_*,F Hcut U f\rangle
 +\langle\ell_*,U^{-1}\ell_*\rangle
 -\int_0^2(F\ell_*)(x)2^{-1/2}(F\ell_*)(x/2)dx.
\]

这是Plancherel/cutoff运输完整无限尾，不是删掉tail。当前为实输入／linear-first内积；原五源allcomplex与四表一致transpose责任未被简化。

| 项 | 显示值 | 实际认证 |
|---|---:|---|
| f与Uf | −0.2883680173314208 | 256² exact overlap，sqrt2向外；独立endpoint sweep核同分数 |
| ell*与FH U^-1 f | −0.21432708798806835 | 383个clipped endpoints，真实Si／half-integer parity余项 |
| ell*与FH U f | −0.19492157425883638 | 384个endpoints，同一有向算法 |
| ell*与U^-1 ell* | 3.5373752771557125 | 支撑0..1/2，g(2y)的1/2及p(2y)的4^j全部保留 |
| 有限尾修正积分 | 3.6978609119144994 | N32真实cosine余项、exact polynomial product积分及rounding |

前四项[原稿](../tf-reader-c2/mixed-terms.md)和[JSON](../tf-reader-c2/mixed-terms.json)实际约33.05秒，148715个Q值，180位向外算术；Q(k)=πk(π/2−Siπk)，大k为(−1)^k乘Laplace积分，有限几何给signed余项，小k真实integrated sine Taylor及π argument误差另付。sin-product kernel的min及Q差来自exact endpoint积分，高频消去在有理权聚合中完成；p*与sine的odd-moment递推保全部conditioning/rounding。各项width≤1/16384。

第五项[原稿](../tf-reader-c2/tail-term.md)及[JSON](../tf-reader-c2/tail-term.json)实际约0.432秒。33even moments、degree64的cosine多项式，ell* L1≤2+Σ|p_j|/(2j+1)≈28.6685；全x∈[0,2]真实余项ε≤2L1(4π_hi)^66/66!<3.719e−19，product积分运输半径<6.032e−17。1089个exact monomial积分用260位向外算术，最终width约1.2062e−16。未把形式有限多项式当作免费算术，也未重跑旧68037频率scalar。

root[合成脚本](../../../scripts/tf_reader_fixed_c2_certificate.py)实际支付

\[
 |c_2(v)-c_2(v_*)|\le\delta_v(2\cdot389/1000+\delta_v)
 <8.250\cdot10^{-17},
\]

其中389/1000为已核真实||v||上界。五项有理区间按+−−+−合成，再加减该input费，不以有限grid残差替换全H误差。独立fresh重放两个新模块及手工Fraction合成，全部非时间字段相同；root消费实际版本见[前件收据](../tf-reader-c2/root-consumption-scope.json)及[fresh稿](../tf-reader-c2/fresh-audit.md)。

## 3. 真实瓶颈与whole-G再准入

实际改变：已有explicit analytic向量不再只具定义，现已支持一个bounded mixed pair的严格求值、conditioning和全H误差。没有新增独立经典正性、cofinal signed/core/coupling、非零primitive整过滤／截面乘法／mixedRR，亦无whole leading4/5改进。535／560固定窗trace/Gram及此前reader一般式是旧输入；542+555→557仍仅whole leading4/5负惯性UPPER。全部Γ/contact/properpowers/双pole、allcomplex原du/zero-extensionDlog及完整cross责任保留。

独立exact枚举W=∏[(1+1/p)I−p^−1/2(U_p+U_1/p)]给6561个不同ratio，范围[1/NF,NF]，central coefficient=165888/46189。当前ratio2不覆盖它们，更不付||P Wv||²。若直接把本次N32小cutoff Taylor包络延至NF，充分ε上界乘(NF/2)^66，已无信息；这只限制该固定预算复用，不是必要成本下界、所有analytic表示失效或数学方法不可能性。

因此**不准据c2 pass自动执行全部ratio／G／Krylov**。本次固定pair门已耗用并停止重复；新的whole-G action尚无完整费用输入。下一只准[一次trial预算准入比较](../tf-reader-c2/next-one-trial-budget-admission.md)：将新n/c2消费为same-v的a2及rest七prime Loewner界，先扣n=<B*v,h0>、B normal给a≥n²的更强旧source后果，再保相关b≤u a，检查冻结z=v/u_hi的残差包络／J能否达到原门。不得把弱p2 lower改好称whole净值；upper对fixed J的作用与核心残差分开报告。该比较没有unknown action假设，能量化新单pair对验收的实际支付；它不是fullG执行准入。若不够就止该输入/包络的自动续算，不调t、prime或Chebyshev；若够也仍按原完整对象/误差验收，不领取RH。

## 4. 结算与恢复

本次为现有exact身份的标准建设性固定数值实现和成本审查，0数学轮，没有新的全量词定理／完整研究方法边界，不建C047/584。唯一cadence1／历史47／cycle16不增不重置；代码、agent、运行、审查和推送不计轮。长期Goal同实例active、完成门open，不complete或blocked。

本次没有新外部论文、PDF或原字节下载；实际复用已库DLMF6.2.E9/E19、6.7.E13、6.12.E3公式，half-integer parity及finite moment余项在项目中推导。原normalized公式缓存仍本地忽略，文献索引追加实际消费范围；不声称重审整章。状态阶段/真实pending、看板与正常GitHub同步由STATE及远端回执统一，唯一下一动作不从旧q0实施交接或停止C046预算恢复。
