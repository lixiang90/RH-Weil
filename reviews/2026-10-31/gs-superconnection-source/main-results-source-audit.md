# Garcia–Sankaran §1.1：真实Green设施，尚无经典physical源桥

2026-10-31；独占来源审查 `/root/gs_main_results_source`。同G20261027、原0c4f基线；只写本稿，不修改STATE、Goal、cadence、库或Git，不创建合同。运行Goal依据root的同实例1793085111观察，不以child-local状态替代。

**裁决建议：本指定引言门SOURCE0停止，不预准C066/603。** 原件确有高维Shimura特殊循环的自然Green构造、带条件的star-product定理及局部archimedean高度公式，是实际新cited文献设施；不能凭“也叫Koszul／theta”就判成旧582同一构造。但所核页未给原physical r→同对象principal／mixed映射、原norm或经典ζ完整型的新符号，不能把新来源当成新RH数学轮。作者证明未审，以下区分statement核验与目标消费。

## 1. 固定原件和实际读取

Luis E. Garcia、Siddarth Sankaran，*Green forms and the arithmetic Siegel-Weil formula*；作者主页 `https://www.homepages.ucl.ac.uk/~ucahljg/preprints/gfasw.pdf`。实际原件90页、838416bytes，SHA256 `27b36f4de90f66a9bd28dae2054f43ec5f89ad62cee27e767653c69b39434625`。本人数核签名、页数、raw hash、Gitignore与metadata；Creation/ModDate为2020-03-24编译元数据，不当作出版或更正发布日期。该作者PDF不等于期刊／arXiv v1的字节版本。

PDF1 correction notice实读并视核：作者报告已更正发表版κ(T,Φ_f)定义，并指向5.2.11；我未读取该定义或验证更正，只记录notice。Root的首次UCL URL 403／后homepages URL 200由下载收据提供，本人未重新下载、不将首次失败当来源不存在。

实际pypdf全文抽取、阅读及Poppler视核PDF2–6全部页；PDF1只作metadata／TOC／notice核验，其abstract随整页图像曝光，不另当定理证明。另仅取PDF7首155字符定位1.2起点，无§1.1续页；该截取曝光少量notation开头，不消费其内容。未读§2、§3、§4、§5、κ5.2.11、参考文献或其它paper。PDF6含proof overview与历史说明，只按引言陈述，不叫作者证明已核。渲染在本人ignored临时目录，原PDF仍local-only。

## 2. 真正对象与Schwartz变量

令F为totally real、E为带CM type的CM扩张。V为F-quadratic或E-Hermitian空间；一个arch place的signature分别为(p,2)、p>0，或(p,q)、p,q>0，其余arch places正定。H为Res GSpin(V)或Res U(V)，D为对应负子空间域；固定compact-open K后有实际canonical Shimura variety及其X_K(C)各嵌入分量。不能把全complex分量积分缩成单一real place而删除degree因子。

特殊循环由(T,φ_f)索引：T为r_GS×r_GS symmetric／Hermitian矩阵，φ_f∈S(V(A_f)^{r_GS})^K。这里r_GS是tuple长度／genus，**不是物理源r(u)**；y是正定矩阵参数。φ_f为finite adelic Schwartz输入，arch侧使用特定Kudla–Millson form及超联络transgression form。引言没有说“任意arch Schwartz向量都已有同一算术cycle functor”，更未提供582的S0 finite完成到此域的延拓。

向量tuple v满足T(v)=T，D_v由垂直条件定义。非退化时codimension为r_GS（orthogonal）或q r_GS（unitary）。这些是实际特殊循环／Green域，不是按Pan像定义的抽象boundary，也不单由正纤维metric生成mixed符号。

## 3. Green和star-product：哪些方向可引用

引言给transgression

    dd^c ν°(√t v)=−t(d/dt)φ°_KM(√t v),
    g°(v)=∫_[1,∞) ν°(√t v) dt/t  （T非退化）。

所核陈述是非退化g°在D\D_v光滑、在D局部可积，满足native Green current方程。这里的缩放衰减／局部可积性不是物理源的du、zero-extension Dlog、全T/y或成长height统一估计；将t改作任意Mellin源积分仍需新map和全部交换／tail费用。

Th1.1.1声明加权全局current满足(1.1.11)，并在T₁、T₂非退化且Z₁、Z₂ **properly intersect** 时，star product等于具有指定diagonal blocks的T之current和，**仅模 im d＋im d^c**。这不是raw current点态相等、任意双源的无条件乘法，或正definite Hermitian配对。不能把该商偷偷收窄为仅dd^c-exact；本门也不证明各properness／交叉尾费。

有一项字面typing应先保留不消费：PDF3定义tilde-r为rank T（或q rank T），随后把φ_KM写为(tilde-r,tilde-r)，但(1.1.8)的δ_Dv∧Ω_(E∨)^(r_GS−rank T)补次数后属于总r_GS（或q r_GS）degree。退化T时这个引言简写尚未在本门重闭；非退化rank T=r_GS不受此疑义影响。作者明确说退化积分一般不局部可积、另作regularization并用tautological power修正cycle。对此只记录作者all-T statement，不升级退化bidegree／norm／源运输已核，更不宣布作者定理错误或全文失效。

Star-product右端的block-matrix求和原行没有额外写每个总T非退化，故本稿将**整条星积定理保为带原条件的cited statement**，不从非退化T₁/T₂偷领所有退化右端的逐项已核运输。没有为此顺读§2或§4修补。

## 4. 高度公式：局部arch项，不是完整算术正性

Th1.1.2进一步要求V anisotropic、Shimura variety compact，unitary还要求q=1；取正整数1≤r_GS≤p+1，s₀=(p+1−r_GS)/2。对该genus／scalar-weight Eisenstein Fourier系数，引言公式为

    [(-1)^r_GS κ₀ /(2 Vol(X_(V,K),Ω_E))]
      ∫_[X_K(C)] g(T,y,φ_f)∧Ω_E^(p+1−r_GS) · q^T
        = E′_T(τ,Φ_f,s₀) − κ(T,Φ_f) q^T.

κ₀在s₀>0时为1、s₀=0时为2；q^T=e^(2πi tr(Tτ))，与signature参数q区别。符号(-1)^r_GS、2Vol、κ subtraction都不能删。κ定义未审，故不消费其数值或有限部计算。

非退化T的(1.1.17)–(1.1.20)把arch derivative与finite Whittaker factor分开；非totally-positive与totally-positive分支不同，后一分支还保Γ_r／log Norm det T等修正。引言未提供可将这些全归作经典Γ(t)=2θ′的目标身份；我不展开未读notation中的常数m，也不使用一个局部项的符号推出全Weil正型。

PDF6明确把积分称作arith height的**archimedean contribution**，把integral models问题先搁置，剩余纯代数几何、y-independent部分仍是Faltings-type高度的conjectural公式。作者所得非holomorphic terms一致，不能改写成完整finite＋infinite算术Siegel–Weil全已证、RR容量、正极化或所有特殊导数非负。

## 5. 扣旧后净值与停止

旧582已有full-local强域、native Green family、全Pan反测；旧CDM§8有匹配weight3/2 modular输入的cited arithmeticTheta。GS的新cited主结果确实更一般地提供高codimension自然Green／star-product／local-height设施，不能说与旧CM0或有限Petersson source是同一对象。但“高维＋Koszul＋星积”三个标签没有支付physical源域兼容、全405 principal同构／mixed radical、537及全源coverage、du/Dlog／strong/growing费用，也没有给经典ζ无取消zero/pole或完整Q身份。不能把所需箭头作为定理隐含前提再领取。

据本限定页，尚无可直接开启数学合同的新actual input/test/strongest-old-net；建议SOURCE0停止这一§1.1门，不自动打开superconnection证明、star products后章、5.2.11更正或引用链。未来若真有不同actual source→cycle／Green cocycle及完整mixed比较，或独立经典global zero/sign证书，可另准入；本稿不泛排该论文、高维方法、relative／higher、有费unbounded或非逐层Pan的D′路线。

原principal/sections/mixed、危险corecross、成长Ξ及whole leading4/5负惯性UPPER未变，三个Goal完成门仍open。本人实核原cadence6813bytes/SHA0bd41adf…、库142的manifest221943bytes/SHA8d0e293f…当时未改；来源归档／root后续新增书目不由本稿操作或宣称完成。新文献statement不计新数学轮、macro22或Goal完成。

本人仅读旧582§1必要scope与CDM§8 root的对象／输入／费用／限定字段，不把这些nested证明说成本人重审；较广旧比较由root负责。此为当前任务终稿，待root消费，不自改执行状态。
