# 实际 AM 叶切线的仿射恢复与九点统一余量

2026-10-08，perron_reviewer；基线37eb770。
保持483的 AM13 原核、全部真实零点计数前件和498的无损消费。
本文从旧连续 minorant 恢复完整斜率，先重付206个兼容域，再用共享距离 epigraph 支付全部289个域。
结论是在483明确的连续证明与组合计算信任范围下，九点局部式对全部八gap≥4/5满足
\(F_9\ge805103/10^8=c+10^{-6}\)。不是浮点优化的全局最小值，也不是新零点条带。

## 1. 固定输入与实际阅读

canonical LF身份为UTF-8、CRLF/lone-CR→LF、保留EOF。全文重读228行审查、101行桥、
219行公开捕获器、原mcheckP完整定义及mtermTZ/mcheckGZ_sound证明、ydec/leafStep/node/walk核心。
228的旧“数值待核”历史状态不能替代后续483完成的准入。

| 输入 | 行／LF字节 | SHA-256 |
|---|---|---|
| [连续审查](hybrid-original-am-eight-point-full-certificate-audit-pc8.md) | 228／17120 | 6cea584276b25cfd58fd353f8281986898833ae0a335c8f9033ba99a8154fb46 |
| [generic桥](../../formal/certificates/AMPC8MinorantBridge.lean) | 101／5512 | f3947ca27750760322481a87ed5da4a5a8702a92bdf4570a6a4727f957fee114 |
| [原捕获器](../../scripts/am_nine_point_low_slack_cover.py) | 219／10565 | 0c203ae8d05796f73e5ca5018935067342a65f6a9eac3a800b5d36893cfde629 |
| [原闭胞数据](../../output/am-nine-point-low-slack-cover.json) | 6752／131270 | 628fdf422495f15f3b5f5ce7e035f8f439d43c0928883509f39034c87b0c64ff |
| [九点lift](am-nine-point-lift-research-high-product.md) | 161／8823 | 88bd93c28ca361a5be70a48504a186378abba57031ac0f149b08eaf5a8acf045 |

固定上游Solution.lean的raw bytes为1675641，raw SHA为
012c6ac5f9282158a686500dc0c967bf0a9b00e1a6192734d8f237bb23dd2d5f；
已准入抽取NumericCore的SHA为f21a0d9f141a7807a6524f426b64a0c0b7b2e81e12581d3ec528f467e9bd1be3。
本轮隔离捕获只追加日志，不修改旧219、上游源、返回值、cursor或遍历。

## 2. 每叶完整有理仿射式

设SC=32768，SA=10⁸，E=10⁹，O=2E。旧26个非零项按原TS顺序为(i_n,j_n,a_n)，
BS=(28898,57272,75526,80958,75526,57272,28898)，c=805003/SA。
未归一目标为\(F=BS\cdot h+\sum_na_nw(x_n)\)，\(F_8=F/SA\)，\(x_n=\sum_{i_n\le r<j_n}h_r\)，\(w=K_{\rm AM}^2\)。
每闭胞保留七gap的L/U和21个长span的A/B；方向元数据不是几何约束。
L0_n=Σspan L_r，l_n=max(A_n,L0_n)、u_n=min(B_n,Σspan U_r)，相邻项直接用L_r/U_r。
实际tangent范围为[l_n,u_n]；仅区间lb使用uc=max(u_n,l_n+1)，不得把uc当tangent上端。

每项实际解码FS=(k,m,p,r)，0≤m≤1024，对应权(λ₀,λ₁,λ₂)：
k=1为(0,1024,0)，k=2为(1024−m,m,0)，k=3为(0,1024−m,m)，其余为(1024,0,0)。
packed point给三个整数V、P、M，连续前件担保
\[
 v=V/10^{10}\le w(p/SC),\qquad d^-=(P-O)/E\le w'(p/SC)\le d^+=(O-M)/E. \tag{1}
\]
启用点的mokTZ担保其完整真实span上的tangent \(v+w'(p/SC)(x-p/SC)\le w(x)\)，
包括凸段外的导数或零阶延拓、零宽span特例；不是把点值或网格采样当作全域证明。
记lb=lb(l_n,uc)，按两个启用点求和定义
\[
 mv_n=\lambda_0lb+\sum_{\alpha=1}^2\lambda_\alpha V_\alpha,\quad
 msl_n=\sum_\alpha\lambda_\alpha P_\alpha,\quad mw_n=\lambda_1+\lambda_2,\quad
 t_n=\sum_\alpha\lambda_\alpha(M_\alpha-O)(p_\alpha-L0_n).             \tag{2}
\]
这里t_n恰为mcpT−mcnT：启用点p≥l_n≥L0_n，Nat subtraction没有被误当signed subtraction。
令e_r=h_r−L_r/SC≥0，mtermTZ直接给每项完整连续下界
\[
 w(x_n)\ge {mv_n\over1024\,10^{10}}+{t_n\over1024\,SC\,E}
 +{msl_n-O\,mw_n\over1024E}\sum_{\rm span}e_r.                       \tag{3}
\]
其存在的真实导数混合D下界由msl−Omw给出；乘子x_n−L0_n/SC非负，故替换合法。
因而定义整数
\[
 C_r=1024E\,BS_r+\sum_{n:r\in{\rm span}_n}a_n(msl_n-O\,mw_n),\quad
 N_0=1024\,10^{10}BS\cdot L+SC\sum_na_nmv_n+10\sum_na_nt_n,
\]
\[
 \alpha=N_0-10C\cdot L,\quad D=SA\,SC\,1024\,10^{10},
 \qquad F_8(h)\ge{\alpha+10SC\,C\cdot h\over D}.                     \tag{4}
\]
这是每叶实际完整仿射式，包含负斜率；并非只记录一个已付常数。

## 3. YA与原Farkas损失

YA16为P₀…P₆,S₀…S₆,Cp,Cm；ydec的每项非负乘子由实际span lower/upper约束生成，
保证\(Cp-Cm+\sum_r(P_r-S_r)(SC h_r-L_r)\ge0\)。
旧check减去该非负slack，故改为C′=C−P+S、N′₀=N₀+10(Cm−Cp)，再付
\[
 N'_0-10\sum_r(U_r-L_r)(-C'_r)_+\ge SC\,1024\,10^{10}c_N.            \tag{5}
\]
这恰是原Ng和mcheckP guard。减slack后的affine在实际胞上不大于(4)，
独立坐标负斜率角点还忽略span耦合；恢复(4)再求完整联合域最小值可以回收这两项损失。
YA.o只是cursor元数据。复演旧guard的捕获合同为56个胞bounds、26组实际FS与YA16；
本轮RAW10再保(k,m,p,r,l,uc,L0,lb,packed_p,packed_r)，足以独立还原(2)–(5)。

## 4. 两帧的真实交集与第一层付款

九gap-prefix坐标为y₀=0、\(y_{r+1}-y_r=5SC\,g_r\)；八gap需g_r≥4/5。
左帧用g₀…g₆，右帧用g₁…g₇。反射h↦(h₆,…,h₀)使C反序、α不变，没有斜率负号；
raw atoms则按span(i,j)↦(7−j,7−i)反射，不能简单反转26项列表。
两帧闭胞保留原27个不同长span与八gap，共35类实际区间约束；全部写成\(y_j-y_i\le d_{ij}\)。
完整有理闭包及θ约束证明422坐标候选、289个兼容labelled交集；140labelled胞只有132种几何胞。
平均(4)的分子为α_L+α_R+γ·y，分母2D，其中
\[
 w_r=2(C_{L,r}+C_{R,r-1}),\quad
 \gamma=(-w_0,w_0-w_1,\ldots,w_6-w_7,w_7),                           \tag{6}
\]
越界C取0。任意λ≥0且edge incidence(λ)=−γ给\(\gamma\cdot y\ge-\sum\lambda_{ij}d_{ij}\)。
root实际integer flow付206域、尚余83；本文独立不导入作者算法重算70叶和全部289 dual，
另加正λ边反向tight约束构造289个matching primal，确认这些确为联合affine最小值。
不能把206个labelled域说成全域或206种互异几何区域。

## 5. 保留各点有效tangent的更强共享epigraph

原混合权可换为各独立有效下界的最大值，因为每个启用点都由mokTZ单独担保。
对启用点q=p/SC、实际span范围[l,u]=[l_n,u_n]/SC，定义
\[
 L_p(x)=v+d^+(l-q)+d^-(x-l),\qquad
 U_p(x)=v+d^-(u-q)+d^+(x-u).                                      \tag{7}
\]
若真实tangent斜率d∈[d⁻,d⁺]，其与L_p之差为
\((d-d^-)(x-l)+(d^+-d)(q-l)\ge0\)，与U_p之差为
\((d^+-d)(u-x)+(d-d^-)(u-q)\ge0\)。故两条都在整个胞内≤w。
直接把v+max{d⁻(x−q),d⁺(x−q)}当下界会错；(7)的两端锚定不可省。
若联合闭包缩窄范围且排除q，可改用l*=min(l,q)、u*=max(u,q)，同证明仍成立。

每个真实physical pair只用一个z_ij，汇总两帧的全部正权，并收集两边该pair的
z≥lb/10¹⁰、z≥L_p、z≥U_p及z≥0；零权点不消费未经检验的tangent。
两帧26项的physical union为33对，新(0,8)项再占一个，共34个z和八个g。
AM13原窗在[-1/2,1/2]上满足cos(√2u)≥3/4、Σ|c_j|<13/200，
所以归一窗非负且质量1，|K|≤1，真实w∈[0,1]；因此有限盒0≤z≤1合法。
真实g及z=w赋值满足所有rows/boxes，LP下界就确实是完整F₉的下界。
新(0,8)没有正下界cut，只付非负；此次改善已来自两帧33个共享旧距离。

设矩阵rows为Ax≤b，真赋值下目标c·x=2SA F₉。浮点HiGHS只提出非负有理λ，不作为证明。
任意λ≥0、残量r=c+Aᵀλ及变量盒[lo_i,hi_i]严格给
\[
 F_9\ge {-\lambda\cdot b+\sum_i r_i
          (\mathbf1_{r_i\ge0}lo_i+\mathbf1_{r_i<0}hi_i)\over2SA}.   \tag{8}
\]
不要求浮点feasibility、stationarity或残量为0。本文独立从RAW重建所有289个
220–296行矩阵、42变量盒、目标、λ与residual，用Fraction实跑退出0；
全部(8)≥805103/SA，最弱112/42的值严格为
\[
 {65955289561887369906031994339\over8192000000000000000000000000000}
 >805103/10^8.                                                     \tag{9}
\]

## 6. 完整覆盖、信任与结论

完整域运输不是只保32个root：旧clear COV给某a_adj w≥c，再加θB=.0032348>2δ；
large-gap给某b_i h_i≥c，其余压力≥θ(B−max b_i)=.002587136>2δ；
旧h_i≤1/2分支在θ=4/5域为空。方向叶由反射补齐，fleaf只排空胞。
mleaf的strong clone唯一更换cN为805203；generic连续定理对该reward同样适用。
strongtrue付c+2δ；strongfalse且原成功的叶全部70个按序捕获，原返回/cursor保持。
故若至少一帧不属T₂δ，旧全域F₈≥c及平均已付δ；若两帧皆低，
必落140labelled胞的某兼容交集，由(9)全部付δ。无穷尾、端点、反射和零宽胞都保留。

本轮FULL READ隔离capture.py、joint.py、epigraph.py，独立核日志逐项对应JSON，
删两新增日志严格还原旧生成源；root实际Lean退出0、41旧checks全true、70胞与冻结数据相同。
本文独立有理重建执行退出0，不另重跑535m搜索或Lean，也不把runtime误称纯内核证明。
又FULL READ持久236行检查器并实际运行--check退出0；独立核其70组RAW/YA和全部289组
非负稀疏λ与已独立重建证书逐项相等，故压缩没有删约束、乘子或有限盒residual费用。
依赖旧PTF/LBSound/连续延拓和明确的已准入组合计算信任；不是JSON单独证明了这些前件。
在这些前件下统一δ=10⁻⁶成立。按既有九点滑窗、真实全零点能量及平滑极限顺序消费，
条件代数比例变为66812491/99194897；正式新比例准入需本轮独审与持久证书一起完成。

隔离证据位于tmp/pdfs/am-nine-affine-root；canonical LF身份如下。

| 文件 | 行／LF字节 | SHA-256 |
|---|---|---|
| [持久检查器](../../scripts/am_nine_point_epigraph_certificate.py) | 236／11009 | af5f2e1974bed92ad515f06ff6047f3e5595ac60c6dc721abd7bfb5cfd930c32 |
| [持久证书](../../output/am-nine-point-epigraph-certificate.json) | 68844／1112534 | 0733022044f96b37c6be3d5d5c1e9fa6c269545142d7d535e643c835a7cf38f6 |
| capture.py | 35／1624 | ed7375333042073c028b7f82a86dccb592b8159a17ccf1bd5b363029939ff050 |
| capture-log.txt | 351／183580 | 9c0644717933c9afac9e75d90124bfbfebe8869a91f656b6b6480f57c4366c7e |
| joint.py | 139／6770 | ee56635fccdb5827309526eabd5724eb91e9cee022d378b5dc9183b3eb1e07fb |
| joint.json | 43434／712678 | 11ed7fd4d711c2ca83301de2ede1a57b0157135040fa9ddf1f0eeaf5e52c3401 |
| epigraph.py | 109／5675 | 438a4b1b137762bc25461973d108321ca9dba2f7428437305963719726e80b67 |
| epigraph.json | 94781／1482651 | b910f0465989d07240a4216568091dac744a6fbb6fea6cebef4a678b7009afc9 |

本文没有证明实际ζ的新非零条带、RH、原四高素数预算或不含计算信任的Lean端到端定理。
