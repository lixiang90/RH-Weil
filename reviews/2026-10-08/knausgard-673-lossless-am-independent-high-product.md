# AM 八点证书的无损分离装配：不同作者独立复核

2026-10-08。作者 high_product_joint。结论：限定数学 PASS。
本稿独立核对连续 majorant、旧证书消费、全部零点惯性及极限次序；
不重建旧大证书，不执行新论文 535m 搜索，不编译新论文完整 Lean 工程。
结论复用 483 已准入的旧 PC8CL 全域证书，不消费新论文 headline 的 native_decide。

## 1. 冻结输入与实际阅读

SHA 均为 CRLF/lone-CR 规范为 LF，保留 EOF 的完整字节身份。

| 输入 | 行／LF字节 | SHA-256 |
| --- | --- | --- |
| [不同作者方法源](knausgard-673-method-and-am-comparison-research-perron.md) | 186／11880 | 5ff04f61f68687738d02cb04b2d58d6199a91adb8f5991fe2575f20ebff4cbd5 |
| [旧 AM 解析源](hybrid-original-eight-point-sqrt-pressure-research-compression.md) | 419／17965 | 94dcf6cde41a78dad81a5ed4d7a1513478bbc09746603a2397b677548fdd4161 |
| [实连续域语义](hybrid-original-am-eight-point-full-certificate-audit-pc8.md) | 228／17120 | 6cea584276b25cfd58fd353f8281986898833ae0a335c8f9033ba99a8154fb46 |
| [最终全量抽取审查](hybrid-original-am-eight-point-numerical-extraction-review-pc8.md) | 141／14583 | 6a2a01e8a2474b29fd567c110575cd01ebe64cdbcc2cd090f17ff14044ce8e49 |
| [483 准入笔记](../../notes/483-admission-of-known-am-eight-point-proportion.md) | 166／7342 | 3ab82cdb257a8555b206f90e59c18fb73f68fe9be0a2de5117bb573056efdb7e |
| [实际惯性证明](hybrid-original-multipoint-envelope-and-actual-counting-research-compression.md) | 421／16963 | 59b399445a3022ce9b5ee6c064660e1602dab6d5641d3793649f16f509fc5efa |
| [304 固定平滑二阶桥](../../notes/304-mt-triple-geometry-and-second-moment-stability.md) | 645／26598 | 03f21ab1749157ff45bc4d4f62709e2a5482257c7155e7e8e644da0ac4521bc4 |

本轮 FULL READ 前六文件，核查 304§5 全部证明；上述身份已实际只读重算。
方法源已包含唯一 fixed-ε 勘误 C(f_ε)；其余数学及 checker 与前稿相同。
PC8CL 固定原源 d272437 的 raw SHA 为
012c6ac5f9282158a686500dc0c967bf0a9b00e1a6192734d8f237bb23dd2d5f。

## 2. 连续 majorant 的独立数学及实际执行

保持 AM13 正偶概率密度 f、其 Z₀=√2 sin(1/√2) 和全部十二项原系数。
θ=4/5、γ=61/100，令 g(v)=γ[sinc(θ(v−1/2))+sinc(θ(v+1/2))]²。
归一化 sinc 的 Fourier 因子为矩形；卷积在 ±θ 的重叠长度为零，
故 ĝ 支撑于 [−θ,θ] 且两个端点的值精确为零。
其质量 Λ=(2γ/θ)(1+sinc θ)≤61/32<2；这里 sinc θ≤1/4。

完整审读方法源的 37 行 Fraction checker，独立从 final codeblock 抽取到忽略目录
tmp/pdfs/knausgard-673-local-storage-high-product/am_majorant_from_perron.py。
其无 EOF newline 的 1428 字节 SHA 为
4b3fe24b7bd1a1d136a073335684eb601950e8e7d207e6f5cbaf57b00078efd1。
24 项 Machin 交错级数严格包住 π；各 cos/sinc 的 q=x² 区间余项
为 q¹³/26! 和 q¹³/27!，第 13 项之后递减，整数周期约化精确。
Z₀ 的 q=1/2 无平方根误差；所有除法先保证正分母，sinc(0) 不除以零。
独立逐式核查 interval add/mul/div 的包络方向及 g 的平方下界，未见漏洞。

129 个 k/256 节点各给 g−f>9/100。
由 sinc=(1/2)∫₋₁¹ exp(iπtu)du，|sinc′|≤π/2、|sinc|≤1，
因此 |(g−f)′|≤4γπθ+(√2+2πΣj|c_j|)/Z₀<16。
两函数偶，最近节点距离至多 1/512，故整个闭区间上
g−f>9/100−16/512=47/800>0；区间外 f=0、g≥0。
这是带明确误差的连续证明，不能把网格 PASS 单独称为全域证明。

实际运行 Python 3.12.5，参数 -B -X utf8，exit 0、stderr 空；
输出为 PASS 129 exact cells and the continuous derivative bridge。
隔离执行记录 am_majorant_replay.json 为 19 行／764 LF字节，SHA
46ac298047b7d68a4eba8b9471793993056c1220741fffb295e9ae578a0adf08。
其中 stdout LF SHA 为 5fce9c7e7ef973c04b7a1383166a258e90be6a04575d0e0fee117ed1c884cd39。
本次运行只检查此小证书；没有执行全 AM replay 或外论文搜索。

对 |t|≤θ，Chebyshev covariance 用 [0,1/2] 上两个递减 cosine，
给 K_MT(t)≥sinc t≥sinc θ>7/30。
AM 扰动模 ≤Σ|c_j|/Z₀<39/550，故 K_AM(t)>134/825；
(134/825)²>1/40>c=805003/10⁸。这里始终是原 AM 核。

## 3. 无损局部消费和全部端项

旧全域证书是全部非负七 gap 上 Σb_rg_r+Σa_ijK_AM(dist)²≥c，
B₀=Σb_r=404350/10⁸；每一 index span 的权重和至多 2。
对 m≥8 个点的全部 m−7 滑窗求和，gap 费用 ≤B₀span，
记 E=2Σi<j|K_AM(dist)|²；pair 费用 ≤E，得到 E≥c(m−7)−B₀span。
不是把 signed 全局统计限制到私有子集。

固定 f_ε=fχ_ε²/m_ε，0≤χ_ε≤1、m_ε→1，d_ε=∥f_ε−f∥₁→0。
选 m_ε>61/64；在任意 θ-separated 点集 S 上，
g≥m_εf_ε 和 ĝ 的端点零给 U_SS≤(Λ/m_ε)I<2I。
φ₂(t)=t²−(t−2)₊² 在此谱上等于 t²。
每个局部窗口总 pair 权重 ≤14，核平方误差 ≤3d_ε；
所以 J(U_SS)=trφ₂(U_SS)−m
≥cm−B₀span(S)−7c−42d_εm。m≤7 亦由非负 E 支付同一端项。

在全部简单临界线点中选极大不交距离 <θ 的点对；剩余集合 θ-separated。
每个真实 2×2 Gram 的谱为 1±|u|，≤2，故 J_pair=2|u|²≥2c−6d_ε。
φ₂ 为标量凸函数，块本征基上的 Jensen 证明 trace pinching；
不需要 operator convexity，也不向 n 列 Gram 补额外零维度。
各块只计一次；空剩余集及不足八点也保留上述端项。
于是完整 n 列满足 J(U)≥cn−B₀span(Y)−7c−42d_εn。

## 4. 同一全零点算子、比例及信任边界

304 的真实 Hermitian A 保留全部离线配对及重数，tr A=N。
P 为全部简单单位列，Q=A−P；正惯性 p 满足 N≥n+2p。
minmax 给 λ_{p+i}(A)≤λ_i(P)；逐谱用 4t−t²≤4 和
max_{t≤s}(4t−t²)=2s+1−j(s)（s≥0），其中 j=φ₂−2t+1。
由此 4N−tr A²≤4p+3n−J(U)，即 tr A²≥2N−n+J(U)。
环境的非正尾谱不会额外贡献 j(0)；离线项从未被删除或当成正 Gram。

先固定 ε，tr A²=(C(f_ε)+o_ε(1))N；span(Y)≤T log T/(2π)=N+o(N)。
代入上一节，再先 T→∞、后 ε→0，给比例 (2−C(f)−B₀)/(1−c)。
独立另用 26 项 cos/sinc 有理交错包络、π 的已验证上界，
重算 AM 自身能量，确认 2−C_AM>67216841/10⁸，未借 MT 能量补入 AM。
最终精确值为 66812491/99194997≈0.6735469834229644。
与外论文 headline 1669159/2478195 的差为 719712074/81941515196805>0。

限定 PASS 的前件是已准入旧 AM 七维全域证书及固定函数无条件二阶定理。
旧证据包括人工连续语义、240 项 #eval 精确整数编译求值、
七项完整结构检查和 30 条通用 Lean 内核桥；240 项不能说成纯内核证明。
本轮不重跑这些旧大型数据，也不把保存日志或 SHA 自身当成证明。
新论文 native_decide 的计算公理既不是 RH 假设，也不是本推论所用证书。
此后果不需要 7/8 条带前件，不改善零点无零区域，不证明 RH。
是否为公开前沿新纪录仍须另核当前文献；本稿只确认上述精确数学推论与消费链。
