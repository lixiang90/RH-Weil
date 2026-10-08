# 九点正式论文与真实产品纤维源：全文独立复核

2026-10-08；perron_reviewer。结论：下述最终版本**限定数学 PASS**。
完整读完 root 的 828 行论文与 checkpoint_audit 的 174 行算术源，独推关键等式和范围。
作者修正后的最终论文再次全文读回；没有未解决的实质数学缺口。
本审查人是所引 167 行 affine 研究记录的作者；这里审查两位不同作者的新文本，
不把自己的研究记录另算一份不同作者审查。

## 1. 冻结输入与读取范围

canonical UTF-8 LF 指 CRLF/lone CR→LF，保留 EOF。身份均实际读回。

| 输入 | 行／LF 字节 | SHA-256 |
|---|---|---|
| [正式论文](../../papers/nine-point-joint-minorant-simple-critical-paper.tex) | 828／33967 | 5a7499ddcdd290a25a39f568965c00bcc833975688553f2321ebf02643e538a6 |
| [产品纤维源](original-product-fiber-short-window-research-checkpoint.md) | 174／10878 | 06f4d873d5a7b181c21dfd0284a82a3657a80a159d424783deac70da8fecf5ed |
| [新 verifier](../../scripts/am_nine_point_epigraph_certificate.py) | 236／11009 | af5f2e1974bed92ad515f06ff6047f3e5595ac60c6dc721abd7bfb5cfd930c32 |
| [新证书](../../output/am-nine-point-epigraph-certificate.json) | 68844／1112534 | 0733022044f96b37c6be3d5d5c1e9fa6c269545142d7d535e643c835a7cf38f6 |
| [majorant/energy verifier](../../scripts/am_lossless_majorant_certificate.py) | 154／6671 | 11da56ae04a60fd436d273f39463e6aa85b0f023ebf62a0389c5f9af0b2aabf4 |
| [majorant/energy 输出](../../output/am-lossless-majorant-certificate.json) | 42／1396 | 61023fac589f2a8c8b3f67c8c296c38a2a244663129eb8bc90de6396c60fb915 |
| [先前 affine 记录](am-affine-leaf-minorant-research-perron.md) | 167／10827 | f9616af18e61015682a3c41cebab630af72d9f107da1e9cb7424265875ad5a14 |
| [持久回放日志](../../tmp/pdfs/am-nine-point-epigraph/capture-log.txt) | 351／183580 | 9c0644717933c9afac9e75d90124bfbfebe8869a91f656b6b6480f57c4366c7e |

236 行 verifier 全文复读。全部 70 RAW/YA、289 个 sparse dual 及矩阵/box 的数据检查，
此前已用独立 Fraction 算式重建，未导入作者 verifier 来自证；本次复核最终持久身份不变。
算术所消费的 172、188、425、191 行相关源已读，尤其重新核对 191 §6 的点修正合同。
没有重跑大规模搜索、原 240 项 AM 入库或完整上游 zeta formalization。

## 2. 九点局部全域合同

\(F_9=(F_8^-+F_8^+)/2+2K(S)^2\) 的权重及压力从原表直接得到；
八个 index-span 容量均不超过 2，总非负 pair weight 不超过 16，\(\sum b'_r=B\)。
独立整数/Fraction 汇总核过全部 26 项，未把缺失的零权项补成正权。

完整低 slack 外覆盖不是网格采样：
clear COV 的额外 \(\theta B>2\delta\) 与 large-gap 的
\(\theta(B-\max b)>2\delta\) 排除外域；direction 与 empty leaves 只删除确实空的交集。
强 reward clone 保持原 cursor、return 和旧 guard；70 原标签反射为 140 标签、132 几何 cells。
公共 8 gaps 和 27 long spans 的闭 difference constraints 产生 289 非空 labelled intersections，
并不声称它们互不相交；闭边界、零宽 interval 和 gap 无界均有去向。

对每个 enabled TVal，必须已有整 interval 的有效 tangent，不能只有某点导数包络。
论文两条 anchored line 与原 tangent 之差分别为
\((d-d_-)(x-l)+(d_+-d)(p-l)\) 和
\((d_+-d)(u-x)+(d-d_-)(u-p)\)，均非负。
只消费正 mixture weight 的点；反射按物理 span，true U 不用 uc 扩宽替代。
两个帧共享实际 33 个旧 distance squares，加 span08 共 34 个；概率密度保证每个 \(z\in[0,1]\)。

对 \(Ax\le b\)，残差 \(r=q+A^t\lambda\) 的有限 box 修正给
\(q^tx\ge-\lambda^tb+\min_{\mathrm{box}}r^tx\)；
只需精确 \(\lambda\ge0\)，不需要浮点 feasibility 或 exact stationarity。
全部 289 lower 的最小值为
\[
65955289561887369906031994339/
8192000000000000000000000000000>805103/10^8 .
\]
span08 在此证书只用 \(z\ge0\)，因此没有假借未经证实的长距离正下界。
完整 separated 域的局部 reward 闭合；滑窗得到 \(c(m-8)-B\,\mathrm{span}\)，端项不丢。

## 3. 固定平滑、全零点计数与能量

同一 AM window 的连续 majorant 利用 129 节点严格 margin 和全域 derivative \(<16\)，
从 nearest-node 距离 \(1/512\) 得 \(47/800\)；节点检查本身不是连续证明。
Fourier 两端 \(\pm\theta\) 均为零，\(\Lambda\le61/32\)。
实际 normalized smoothing 必须用 \(g/m_\varepsilon\)，
先固定 \(m_\varepsilon>61/64\) 才得 separated Gram \(<2I\)。
close-pair reward、scalar convex pinching、每窗 \(32d_\varepsilon\) 误差和单个 \(8c\) 端项均正确。

已核所用 primary statement/proof：
[BGST v1 Lemma 5](https://arxiv.org/html/2306.04799v1)，
[更正 §3](https://arxiv.org/html/2501.14545v3)，
[Lamzouri v1 §3](https://arxiv.org/html/2609.02882v1)。
更正文献明确保留原 Lemma 5 应用的有效性。
固定 \(q=f_\varepsilon*f_\varepsilon\) 与 signed \(q''\) 分别消费 weighted formula，
\((\widehat q-\widehat{q''}/(4L^2))\,4/(4-\Delta^2)=K_\varepsilon(i\Delta L/(2\pi))^2\)。
没有把随 T 变化的 test 塞进 fixed-test 定理；先 T→∞ 再 ε→0。

先在 complex \(L^2\) 定义 \(v_z\)，再取 conjugate-reflection 的 real-type space。
全部 off-line conjugate pairs 和 multiplicities 进入 \(A_T\)，
\(\mathrm{tr}A_T=N\)、\(\mathrm{tr}A_T^2=(C(f_\varepsilon)+o_\varepsilon(1))N\) 成立。
simple critical features 组成 P；剩余 positive rank \(b\) 满足 \(N\ge n+2b\)。
minmax 与 scalar \(4t-t^2\) 不等式给
\(\mathrm{tr}A_T^2\ge2(N-n)+\mathrm{tr}\phi_2(U)\)；
Gram 的零 eigenvalues 及新增 ambient zero directions 计数正确。
没有要求各个 complex pair term 非负，也没有删除 off-line zeros。

独立 Fraction 检查短能量证书四个 Taylor/Machin 有理数及全部 12 cosine 系数，
得到 \(2-C(f)>67216841/10^8\)，扰动能量已支付。
最终比率 \(66812491/99194897=0.6735476624367078\ldots\) 及两个 exact 比率差均核准。
论文严格区分固定 v1 benchmark 比较与全球优先权、simple-critical 与 distinct/all-zero 计数。
window/local weights 归于原公开 AM；separation 机制归于 Knausgård，信用范围准确。

## 4. 实际执行与信任边界

本人实际运行两个持久 verifier 的 --check，均退出 0；不是只看作者 stdout。
独立 RAW/YA、矩阵/dual 算式以及本次能量、容量、压力和 ratio 算式均退出 0。
作者持久 --replay 实际退出 0，由 root 执行记录确认；本人没有再运行 Lean。
本人另独立解析其全部日志：70 RAW/YA 逐项等于最终证书，
41 PILOT 皆 true（32 roots、7 covers、两个 outer checks），没有 error。
第一次解析误把 PILOT 行当独立 true 行，修正日志格式后上述只读检查退出 0；不是源失败。

PC8 240 compiled integer evaluations 不等于 240 kernel reductions，
本次 41 evaluations 不重复验证旧全部 value/derivative tables。
依赖披露的连续 soundness 与 generic bridges、Python assertions 及 compiled-computation trust。
不消费 Knausgård headline 的 native computation axiom；
不把本报告、两个有限程序或 generic kernel sublemmas 称为完整 Lean zeta proof。
此前指出 checker 未直接验证新 span capacities 的措辞，已由作者修成定义的直接预算推导；
最终准确 commit hash 三处和摘要小数末位也已读回。未修改作者源。

## 5. 算术源的直接 Gram 与实际部分付款

保留全部 genuine \(q,s,p,r>X^{.9}\)、实际 \(\nu\)、共同参数和 sharp q-prefix。
\(X=T/(2\pi)\)、\(\nu\) 下端 \(>T\)、\(s\le X\) 给 \(n>q\)，故 \(j\ge1\)；
短窗 \(J\ll X/S+1<q\)，而两端 period、floors 和 small \(X/S\) 的 +1 保留。
只有 \(\nu\) 的外 twist 需 weighted-two moment；φ/g 原 L¹ 尾合同未升级。

完整 primitive 求和恢复
\(H_\gamma(a)=\sum_k d_kD_\gamma(k\bmod q)e(-ak/q^2)\)，
slow phase 未丢；exact norm 是全部跨 fiber 的 partial-Fourier Gram。
v-Parseval 与每 fiber 的区间长度给 \(A_\gamma\ll J\)，不是均匀产品分布假设。
共享 \(\ell\) 的 m′ circle spacing/wrapgap 至少 \(\ell/q^2\)，
harmonic row bound \((q+q^2/\ell)\log q\) 连同对称 Schur 付款
\(qJ(1+q/P_{\min})\)，含 self、square products 与跨 fiber。

互素余额仍是原 \(L_q((k'-k)/q^2)\) 的完整 signed sum，可能为负。
任意 Ω 只缩小左侧 positive norm；不靠 signed-subset 单调性截右侧。
完整 period 与最多两 edges 按三项 Cauchy付；同 period 不重复，a=0 仅 norm 延伸。
q、参数和 packet 先聚合再只取一次 positive part；该顺序保留正文合同的强度。
外 F 正 Parseval、\(PR\asymp QS\)、\(P_{\min}\gg S\) 给已付幅度 \(Q/\sqrt X\)，
恢复全部 dyads 为 \(X^{1/2}L^C\)。
两点 s 排除用 191 §6 原 ν 的直接 q² Parseval，未引入额外 φ/ω weighted moment。

顶端仍需 actual \([C_{\rm cop}]_+\ll X^{1+2B-\eta}\) 才能省完整核心；
\(B=5/7\) 时要求 exponent \(<17/7\)，仅为充分输入。
这是实际共享因子子项付款，不是原四全异词的 repeated union，
也没有支付互素 covariance、完整 whole 幂或改进 zero-free strip。

## 6. 最终限定结论

论文的九点全域证书和全部实际零点解析运输，在明确的既有 PC8 信任范围内 PASS。
174 行算术源的 \(X^{1/2}\) 共享因子付款与剩余 signed 核范围 PASS。
没有未解决的修改请求；没有认证 PDF 视觉、外部同行评审或穷尽文献优先权。
本审查只新增此文件，其他 frozen source、Git、index/cadence 未动。
