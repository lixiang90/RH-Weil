# 无损八点简单临界线零点论文：不同作者全文审查

2026-10-08。作者 high_product_joint。结论：最终冻结版本限定数学 PASS。
已直接全文读取正式论文，逐式独推有限谱及复零点证明；不是只引用旧研究稿的结论。
本稿不修改论文、旧冻结来源或 Git，不将内部审查称为外部同行评审。

## 1. 实际审查对象和固定身份

以下 Markdown／TeX／Python／JSON 身份均按 CRLF/lone-CR→LF，保留 EOF。

| 对象 | 行／LF字节 | SHA-256 |
| --- | --- | --- |
| [正式论文](../../papers/lossless-eight-point-simple-critical-paper.tex) | 635／24829 | 51c3931e3ce3ba54cd4a8441254ea0c8767009aee57e427f7f3492108b1a204c |
| [持久检验程序](../../scripts/am_lossless_majorant_certificate.py) | 154／6671 | 11da56ae04a60fd436d273f39463e6aa85b0f023ebf62a0389c5f9af0b2aabf4 |
| [全部保存输出](../../output/am-lossless-majorant-certificate.json) | 42／1396 | 61023fac589f2a8c8b3f67c8c296c38a2a244663129eb8bc90de6396c60fb915 |
| [先行独立 AM 消费复核](knausgard-673-lossless-am-independent-high-product.md) | 108／7213 | c3a01e976d6fec5bcabbcc422c0c22492a4d7d94c40de06d4d0518a1a6a91bd2 |

前四文件均 FULL READ；前三身份在实际 --check 后再次只读确认未变。
先行独审绑定的旧 419 解析、228 连续语义、141 全量抽取、483 准入及
421 惯性源均已在本轮全文读过，304§5 全部证明也已核查。
正式稿使用的 computational input 是旧 PC8CL 实七-gap 全域下界；
其窗口、全部 pair／gap 权重和核的质量归一化与旧输入完全一致。

## 2. 窗口、连续证书与轻量程序

原 f 在 I 上严格正，Z₀≥11/12，整数 cosine 模态质量为零，故是偶概率密度。
七种 span capacity 的原整数和核对为
(199999997,199999998,199999996,199999998,199999998,200000000,200000000)。
滑动全部 m−7 八点窗时，任何 pair 的累计权 ≤2，任何 gap 累计权 ≤B；
所以完整 ordered pair energy ≥c(m−7)−Bspan，m≤7 的负右端亦有效。
未假设大块自身的全谱均不截断，也未把局部输入换成整数 gap 采样。

独立推 g 的 sinc Fourier 矩形卷积，ĝ(±θ)=0 由重叠区间长度为零给出；
其质量 2γ(1+sinc θ)/θ≤61/32，不漏两个 shifted sinc 的交叉积分。
129 个节点的有理下界 >9/100，加偶性、最近距离 1/512 与导数 <16，
给全闭区间 margin >47/800；I 外使用 f=0 和 g≥0。
f 在 I 端点的零延拓跳跃不影响区间内均值定理及外部非负性。
近对证明的 Chebyshev covariance 在两个递减 cosine 的同一区间合法；
扰动核仍除以 Z₀，给 K_AM>134/825、K_AM²>1/40>c。

程序完整读取后，实际执行
C:\Python312\python.exe -B -X utf8 scripts/am_lossless_majorant_certificate.py --check。
真实 exit 0，输出 PASS exact continuous majorant, AM energy and committed report。
--check 重新算 certificate() 并比较完整解码 JSON，读取路径由本脚本位置固定；
不写或覆盖保存输出。此比较是 JSON 内容相等，不宣称逐字节重生成相等。
__debug__ 两层守卫拒绝 -O，全部判定使用 Fraction／任意精度整数，无浮点验收。

interval mul 用四角、除法先证明正分母，负系数以 interval scale 正确翻转。
Machin 24 项末项为负，下一正项给上包络；cos/sinc 前十三项加对称余项，
在 q<10 时从第十三项起绝对值递减，因而覆盖所有使用的 q 区间。
实际 π² 包络上端可略大于真实 π²；最终 [0,10) 版本明确支付此点。
相位按模二精确约化，Z₀ 的平方参数为 1/2，sinc(0) 不除以零。
g 的 interval square 是包含真实平方的四角乘法，即使区间相关也安全。
程序的能量除数是 Z₀²=2sin²β 下界，扰动正修正用 π 上界，方向正确。

独立另用 Fraction 重建附录 u,z,d,p 的四个短交错部分和，逐个匹配论文分数，
不调用持久程序函数；实际 exit 0 并证能量 slack >56/10¹¹。
附录“正 margin >5.6×10⁻¹⁰”与持久程序的严格 AM 自身能量界一致。
程序只认证新 majorant、能量和有限代数；不重新认证旧七维局部门。

## 3. 完整有限 Gram 和 maximal pairing

f_ε=fχ_ε²/m_ε，χ_ε≥0；故 η_ε=χ_ε√f/√m_ε 在内区间光滑。
所有列为精确单位，核误差仅在实轴上用 d_ε，不要求增长复带的近似。
固定 m_ε>61/64 时 g≥m_εf_ε，θ-separated 集合 S 的
指数和积分恰为 ΛΣ|z_j|²，因非零距离包含等号 θ 处 ĝ=0。
由此 U_SS≤Λ/m_ε I<2I，φ₂(U_SS)=U_SS²；归一化因子不能省略。

每个滑窗 pair 权总量 ≤14，平方误差 ≤3d_ε，
得到 J(U_SS)≥cm−Bspan(S)−7c−42d_εm。
对于 m≤7 或空 S，同一非负 ordered pair energy 付单个端项，无每簇累加损失。
有限图的 maximal disjoint matching 剩余点间无距离 <θ；
每个被取点对的 Gram 谱 1±|K_ε(t)|∈[0,2]，J_pair≥2c−6d_ε。

φ₂ 的导数从 2t 增至 4 后恒定，故在正半轴标量凸。
取每块的本征向量组成完整正交基；对 U 的非负谱逐行标量 Jensen，
再用权矩阵的列和为一，得 trφ₂(U)≥Σ块trφ₂(U_块)。
没有使用 operator convexity，也未计额外环境零方向的 φ₂ 或 j。
每点只属一个块，span(S)≤span(Y)，pair 误差 ≤3d_ε(n−m)；
完整结论 J(U)≥cn−Bspan(Y)−7c−42d_εn 因而成立。

## 4. 一手二阶前件、复零点与 minmax

直接读取 [原 BGST Lemma 5 及其全文证明](https://arxiv.org/pdf/2306.04799)，
其前件是固定实偶 L¹ 测试函数、支撑 [−1,1]、原点 Lipschitz，无非负性要求。
还读取本地 BGSTcorr v3 第7–8页 prefix 修正证明及式(3.5)；
该 PDF raw 376884字节 SHA 0a16b0b0f19b06490111e048a6841f4fe68717c546fae4cb7a44555dc0f96cb3。
不是误用后文带窄盒假设的另一条同名 Lemma 5。
修正版归一化主项 L e⁻²ᴸᵃ(1+O(L⁻¹ᐟ²))+α+O(L⁻¹ᐟ²)，
对固定 q 的积分给 q(0)+2∫₀¹αq+O_q(L⁻¹ᐟ²)；
原点 Lipschitz 使指数项主质量误差 O_q(1/L)，签名不改变绝对误差界。

q=f_ε*f_ε 与 q″ 都是固定实偶光滑测试。Fourier 分部积分给
q̂″(z)=−4π²z²q̂(z)，z²=−(ρ−ρ′)²L²/(4π²)，
所以 (q̂−q̂″/(4L²))·4/(4−(ρ−ρ′)²)=K_ε(z)² 精确。
q″ 全部 weighted sum 是 O_ε(N)，外 1/(4L²) 给 O_ε(N/L²)；
所有实际重数和离线零点保留。不能把随 T 变化的 ε 直接代入此前件。

最终稿先在 complex L² 定义 v_z；conjugate reflection Jv_z=v_barz，
从而真实 v_x、g_z、h_z 才在 real-type Hilbert 空间，避免把非实 v_z 当实向量。
g_z=ηe⁻²πⁱˣᵘcosh(2πyu)、h_z=−iηe⁻²πⁱˣᵘsinh(2πyu)，
故 ∥g_z∥²−∥h_z∥²=1。每个非实对保留正负 rank-one 块。
通常复化积分核为 Σ_z μ_zv_z(u)v_z(−v)；反射不改变 HS 范数。
平方积分展开为 Σ_z,w μ_zμ_wK_ε(z−barw)²，
再全多重集共轭重排并用偶性，才接上相关公式；没有逐项宣称为非负。

Q 的正惯性 ≤b=r+k，由重复实点及非实对的正 rank 至多 r+k；
负块只减少惯性。真实重数给 N≥n+2b，无 RH 或零点位置前件。
独立 minmax：去掉 Q_+ 的至多 b 维像及 P 的前 i−1 个谱方向，
在剩余子空间上 Rayleigh 商 ≤p_i，故 λ_{b+i}(A)≤p_i。
对 p∈[0,2]，max_{t≤p}(4t−t²)=4p−p²；
对 p≥2 此最大值为4，统一为4p−φ₂(p)。
前 b 个谱各用 ≤4，后 n 个用上述界，剩余谱非正用 ≤0，
得 4N−tr A²≤4b+4n−trφ₂(U)。
用 4b≤2(N−n) 推出 tr A²≥2N−n+J(U)，包括 rank 不足和 Gram 零谱。

## 5. 能量、两极限及审查范围

T f₀ 的二阶导为零且偶，故为常数；扰动零质量使交叉能量精确消失。
整数 cosine 正交给论文 AM 正修正，未借用较便宜的 MT 自身能量。
固定 ε 时先用 tr A²=(C(f_ε)+o_ε(1))N 与 span≤X_T；
minmax 加完整 J 给 (1−c+42d_ε)n≥2N−tr A²−BX_T−7c。
先高度极限，后 L¹∩L² 平滑极限；单个 7c 只在除以 N 后消失。
分母 1−c>0，严格能量界推出论文声明的弱有理界 66812491/99194997。
与固定 2610.08965v1 基准差 719712074/81941515196805>0 的单位为比例，
乘100才是 0.0008783241 个百分点，没有将比例当 RH 完成率。

限定 PASS 使用旧全域 PC8CL 证书，其已有计算信任边界保持：
240 次编译整数求值不是240次纯内核证明；本轮没有重跑旧大型数据。
本论文的连续证明、全部真实零点桥及小证书已独立核查，
没有额外 native headline 公理、7/8 条带或高阶相关假设。
这不改善无零区域，也不证明世界纪录优先权或完整 Lean 定理。
