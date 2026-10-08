# 无损八点正式论文：全文数学、归属与持久证书审查

日期：2026-10-08。审读：perron_reviewer；论文作者源：root。
**限定数学 PASS**：最终论文全部 635 行已逐行读完并独立重推，未发现剩余数学阻断。
此前提出的 real-type 向量类型与 Taylor 区间范围修正均已核实。
本报告是内部不同论文作者审读；审读者参与先前研究源，不冒称外部同行评审。
原推论另有 checkpoint/high_product 的不同作者整链审查，不能用本报告替代它们。

## 1. 最终冻结输入与实际执行

以下为完整 canonical LF 字节 SHA-256，保留文件末尾。

| 输入 | 行／字节 | SHA-256 |
| --- | --- | --- |
| [正式论文](../../papers/lossless-eight-point-simple-critical-paper.tex) | 635／24829 | 51c3931e3ce3ba54cd4a8441254ea0c8767009aee57e427f7f3492108b1a204c |
| [持久证书脚本](../../scripts/am_lossless_majorant_certificate.py) | 154／6671 | 11da56ae04a60fd436d273f39463e6aa85b0f023ebf62a0389c5f9af0b2aabf4 |
| [完整保存报告](../../output/am-lossless-majorant-certificate.json) | 42／1396 | 61023fac589f2a8c8b3f67c8c296c38a2a244663129eb8bc90de6396c60fb915 |
| [原方法源](knausgard-673-method-and-am-comparison-research-perron.md) | 186／11880 | 5ff04f61f68687738d02cb04b2d58d6199a91adb8f5991fe2575f20ebff4cbd5 |
| [原推论独审](knausgard-673-lossless-am-review-checkpoint.md) | 167／9737 | 98cb99e58360506d48e2491eda22f4ebc81952e31baf7b70e9aa9b5589495dff |

初稿 630 行 SHA ab4a028f93765782b864a701f2ec03954f41900c2cddd58fe4b03865c207d4c8
与最终稿的实际差仅为：复化/实型声明、机制归属措辞、区间改为 [0,10)、补准确题名。
逐项逆还原严格恢复初稿哈希；脚本逆还原唯一 docstring 也恢复初版 f37fba12… 哈希。
没有借用作者“已修”说明替代实际差异核验，最终稿又完整读了一遍。

本作者全文读最终 154 行脚本、42 行 JSON，并真实运行
~~~text
C:\Python312\python.exe -B -X utf8 scripts/am_lossless_majorant_certificate.py --check
~~~
实际退出码 **0**，完整结构结果与保存 JSON 一致。
初版脚本也曾真实 --check 退出 0；最终修订仅文档与自哈希绑定变化。
本轮没有重跑 PC8 七维证书或 Knausgård 的 535,332,163 盒搜索。

## 2. 原输入、滑窗与连续 majorant

论文 Table 1 与原 PC8 固定 26 个非零权逐项相同；两个零项为 (0,2)、(5,7)。
按 index span 的精确分子是
(199999997,199999998,199999996,199999998,199999998,200000000,200000000)，
分母均 10⁸；七个 gap 权之和为 404350/10⁸。
由非负性，完整 m−7 个窗口的任意 pair 累计权 ≤2、gap 累计费 ≤B，
所以 E≥c(m−7)−B span；m≤7 与空集端项同样成立。
这里直接应用真实全域证书，不从 signed 总能量推断子集单调。

g=γ[sinc θ(u−1/2)+sinc θ(u+1/2)]² 的 Fourier 支撑和 ±θ 端点零正确；
Parseval 给 Λ=(2γ/θ)(1+sinc θ)≤61/32<2。
全域非负 g 与 I 外零延拓的 f 也没有边界漏洞。
脚本所有 129 个半窗节点都是 Fraction，不使用浮点决定是否通过：
Machin 的 24 项交错区间、整数相位 modulo 2、cos/sinc 的 q=x² Taylor，
以及正归一化区间除法均正确，q=0 的可去奇点直接由多项式处理。
第 13 项起尾项比小于 1 在 q<10 成立，余项 q_max¹³/26! 或 /27! 正确。
π 的粗上端平方可略大于真实 π²，因此最终采用 [0,10) 是准确范围。

节点 margin>9/100 与全域 |(g−f)'|<16、偶性及距离 ≤1/512，
严格推出连续 margin>47/800；不是把网格最小值当成连续证书。
近对证明的 Chebyshev covariance 与 sinc 单调合法，即使 cos(2πtu) 部分为负；
得到 K_MT≥sinc θ>7/30，扰动费 S/Z₀<39/550，
故 K_AM>134/825、K_AM²>1/40>c；没有把 MT 的局部证书换给 AM 核。

## 3. 固定平滑与全部真实零点

f_ε=fχ_ε²/m_ε 是概率密度，η_ε=√fχ_ε/√m_ε 光滑且实偶。
分离 Gram 只能界为 Λ/m_ε；最终论文正确先固定 m_ε>61/64，
所以无 φ₂ clipping。近对谱 1±|K_ε|≤2 也无 clipping。
所有窗口总权 ≤14、每个平方误差 ≤3d_ε，给 42d_εm；
近对误差 6d_ε/pair 被 42d_εn 吸收，且 7c 只付一次。
极大不交近对后剩余 S 确实 θ-separated；凸谱迹 pinching 只用标量 Jensen。

本轮重新阅读全文所实际使用的 primary 定理及证明：
[BGST Lemma 5](https://catalog.lib.kyushu-u.ac.jp/opac_download_md/7377443/7377443.pdf)，
[2026 修正 §3 的 (3.5) 与证明](https://arxiv.org/html/2501.14545v3#S3)，
及 [Lamzouri §3](https://arxiv.org/html/2609.02882v1#S3) 的固定测试撤权链。
修正 §3 明确恢复 (0,T] 的公式，脚注保留 Lemma 5 的适用结论；
论文没有把只针对 dyadic 范围的陈述直接用于全高度计数。
固定 ε 时 q=f_ε*f_ε、q'' 都是实偶、光滑、紧支撑于 (−1,1)，且可符号变化。
分别应用两个固定测试，再乘外部 L⁻²，准确撤除 w(Δρ)=4/(4−Δρ²)；
复杂参数下的 Fourier 导数恒等式因紧支撑也全纯成立。
q'' 项是 O_ε(N/L²)，不要求对随 T 变化的测试有统一误差。
随后才由 L¹∩L² 收敛取 ε→0，全零点/全重数双和保持完整。

最终修订先在复 L² 定义 v_z，再用 Jv_z=v_barz 说明
v_x（x 实）、g_z、h_z 属实型 Hilbert 空间，类型声明已闭。
Re〈v_z,v_barz〉=1 给 ∥g_z∥²−∥h_z∥²=1；
实型向量的内积实数，tensor 展开与 conjugation 重排给完整 tr A² 双和。
每个重复实点、非实配对贡献至多一个正方向，正部分总秩 ≤r+k；
N≥n+2(r+k) 保留了真正重数，无需任意离线项逐项非负。
计数 lemma 的 minmax λ_{b+i}(A)≤λ_i(P) 来自 Q₊ 的秩 ≤b，
4t−t²≤4p−φ₂(p) 对 t≤p、p≥0 成立，其余非正谱只能降低左边；
补 ambient 零方向不会重复计算 n 维 Gram 的零特征值。

## 4. 能量、极限、归属与范围

论文的 C(f)=∫f²+∬|u−v|ff 与自身 AM 窗口一致。
Tf₀ 为常数，使所有零质量 cosine 扰动的交叉项为零；
T cos(2πju) 的 multiplier 为 1−1/(2π²j²)，能量修正分母是 Z₀²。
独立 Fraction 重算附录短证书 u,z,d,p，严格正余量约 5.6332991×10⁻¹⁰，
大于其写明的 5.6×10⁻¹⁰；不依赖旧保存的 128-bit MT 常数包络。
持久程序的较高阶 Taylor 证书也确实验证了 2−C_AM>67216841/10⁸。

计数与完整 Gram 奖励结合得到 (1−c+42d_ε)n≥2N−tr A²−BX_T−7c；
X_T/N→1，先 T→∞ 再 ε→0，分母为正。严格能量余量足以推出更弱的
liminf n/N≥66812491/99194997，边界 7c 在除 N 后才消失。
对固定外论文比例的准确差为 719712074/81941515196805>0，
约 0.0008783241 个百分点；不是 4% 或 83.9% 简单临界线比例。

论文将窗口、26 权、全域证书归为固定 public PC8 输入，
将无损分离机制表述为适配 Knausgård §5，并列 BGST 修正和 Lamzouri 的解析撤权来源。
它不调用新论文 headline 的 native_decide 计算公理，也不把旧 #eval 复演称为 kernel 证明。
既有连续语义、有限复演与定义桥仍是 PC8 输入的独立信任范围；
本报告不再次认证其全部 Lean 工程，也不证明文献优先权穷尽。
最终限定 PASS 只认证这里给出的实际普通 ζ 简单临界线比例及其明确计算前件。
不推出新的零点无零条带、RH、全 ζ 四矩边界或外部同行评审通过。
